#!/usr/bin/env python3
"""ADAPTIVE DESIGN CLASS [F1/P-2][F2/A1, session S20]: the discharge
procedure of [C-O33]'s design-class residual — error-indicator-driven
knot construction + re-optimization. Registry ID: [X-AKNO].

DECISION OF RECORD (S20 log step 3; D6 item 9 S20 annotation): the
AFEM/FITPACK skeleton — solve -> per-interval GOAL indicator ->
Doerfler bulk marking -> knot insertion at the residual-carrying
station -> re-optimize (TR-SQP under DIR-RKG, unchanged policy stack)
-> repeat under a measured stopping rule. Free-knot optimization,
THB/hierarchical bases and a control-point basis switch are REJECTED
with declared reasons (survey, log step 3). The basis class is
UNCHANGED: clamped-left natural cubic spline (U1 C_geo, C^2 on any
strictly increasing knot set); only knot PLACEMENT adapts.

THE INDICATOR (adjudicated DWR-conformant, log step 3): the drift of
f2 = u + v tan(alpha) per segment of the classical Rao control
surface (the C+ from the kernel boundary to the lip, S19 locus of
record), attributed to the EMITTING wall station via the march's own
topology (the `owner` array of [X-O33B] cplus_chain: each chain node
was solved in some column, and a column IS the C- emitted by one
wall station). By Prop. A3, f2 = -lambda2 is the adjoint variable
itself, so its segment drift is an adjoint-weighted optimality
residual of the goal J — a multiplier-compatibility defect, exactly
the object Becker-Rannacher weighting constructs. No exclusion mask
is applied: the indicator is a refinement driver, not a verdict row
(the pre-registered norms bind FIELD-LEVEL CHECKS; declared).

MARKING (Doerfler bulk criterion, theta = 1/2 declared canonical;
sets for theta in {0.3, 0.5, 0.7} printed for audit): the minimal
set of knot intervals carrying >= theta of the total indicator mass,
CAPPED at A1_AKN_MAXINS insertions per cycle (default 3 — a BUDGET
constraint, declared: each new dof adds n+1 gradient evaluations to
every segment-base Hessian measurement of the driver).

INSERTION SITE: the residual-mass MEDIAN station inside the marked
interval (equidistribution principle, de Boor Ch. XII; FITPACK
places knots at data sites inside the max-residual interval —
source read, S20 log step 3: scipy 1.18 _fitpack_repro.py). A site
closer than one local station spacing to an existing knot is SKIPPED
(declared — the GENO double-point lesson: a degenerate interval
poisons the spline solve).

WARM START (NURBS-shape-opt practice, progressive enrichment): each
cycle starts from the incumbent optimum re-interpolated at the
enriched knot set. NOT claimed geometry-preserving (interpolation is
not Boehm insertion): the representation deviation is MEASURED and
printed each cycle.

STOPPING RULE (gate [D3], measured quantities only): the goal metric
is the R3 corner mismatch |dJ/dy_lip - corner density| / |corner
density| at r=1 on the re-optimized design. Its noise floor is
MEASURED at the baseline: tol_stop = K_RICH * |rel(r=1) - rel(r=2)|
(the metric's own mesh dependence — S19 measured the mismatch
mesh-INDEPENDENT, so this floor is small and honest). The loop stops
when the per-cycle improvement falls below tol_stop, when the goal
rises (reported, best design kept), when the marked set is empty, or
when the declared budget (A1_AKN_MAXCYC cycles / A1_AKN_BUDGET_S
wall seconds) is exhausted.

GATES PER CYCLE (all of record, none new): per-cell Newton
certification + axial-margin rejector inside every march (run_trsqp
raises); P4 margin-floor audit of each converged design against
delta_inst = min_margin(baseline W*)/K_RICH; RK-G monitor (i) replay
fidelity inside the driver; O3.1 dot-product spot check on the
gradient at each cycle's optimum (FD two-step Richardson band, the
[X-TOCV] recipe). KILL LINK ([D1], pre-declared in the S20 gate
BEFORE any adaptive run): the final goal must fall BELOW the S19
baseline 6.6295e-02, else the design-class diagnosis is FALSIFIED —
this carrier prints the comparison; the verdict of record is the
[X-O33B] re-run (T3), two-knob form unchanged.

MACHINERY REJECTORS (must be able to reject, R5): (S1) known-answer
indicator test on synthetic chains — a single-interval f2 jump must
put >= 99% of the mass in that interval and Doerfler(0.5) must mark
exactly it; a flat-drift chain must mark MORE THAN ONE interval (no
false concentration); (S2) the marking on the live design must be a
STRICT subset of intervals (an indicator that marks everything
carries no information and is rejected).

ON-DEMAND CARRIER (env: jax). Stages: A1_AKN_STAGE in
{selftest, baseline, cycle, all}. Artifacts: the design of record is
written to validation/s20_adaptive_design.json (text, full
precision) for the T3 bench re-run ([X-O33B] env A1_O33_DESIGN).
Exit code 0 iff all executed checks pass INCLUDING the rejectors.
"""
import json
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1   # noqa: E402
import a1_toc_variational_jax as TV   # noqa: E402
import thermotab_c1_jax as TH     # noqa: E402
import o33_bench as O33           # noqa: E402

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
d2r = np.pi / 180.0

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "s20_adaptive_design.json")


def check(label, ok):
    print("  [%s] %s" % (label, "PASS" if ok else "FAIL"))
    return bool(ok)


class design_class:
    """Set (M_NODES, KNOT_XI) of [X-TOCV] and restore on exit — the
    same set/restore pattern as [X-O33B] march_design, extended to
    the knot vector. xi = None means the uniform class (bit-identical
    default path)."""

    def __init__(self, xi, m=None):
        self.xi = None if xi is None else np.asarray(xi, dtype=float)
        self.m = (len(self.xi) if self.xi is not None else
                  (m if m is not None else TV.M_NODES))

    def __enter__(self):
        self._old = (TV.M_NODES, TV.KNOT_XI)
        TV.M_NODES = self.m
        TV.KNOT_XI = self.xi
        return self

    def __exit__(self, *exc):
        TV.M_NODES, TV.KNOT_XI = self._old
        return False


# ======================================================================
# S1  the indicator: f2 drift per segment -> emitting wall interval
# ======================================================================
def f2_of_chain(chain, state_fn):
    pr = O33.props(chain, state_fn)
    return pr["u"] + pr["v"] * pr["tana"]


def indicator_masses(out, state_fn, xs_knots):
    """Per-knot-interval indicator mass on the classical control
    surface. Returns (masses[j], stations, station_mass) where j
    indexes knot intervals [xs_knots[j], xs_knots[j+1]).

    Attribution: segment (i, i+1) of the control-surface chain gets
    mass |f2[i+1] - f2[i]|, attributed to the wall station that EMITS
    the downstream node's column (owner[i+1]); the station abscissa
    is that column's own wall point cols[k].cline[0], never an index
    reconstruction."""
    chain, owner = O33.cplus_chain(out["cols"])
    des = O33.locus_split(owner, out["n_fan"], out["n_arc"])
    f2 = f2_of_chain(chain, state_fn)
    cols = out["cols"]
    # wall abscissa of each owning column (control-surface nodes only)
    idx = np.where(des)[0]
    x_st, m_st = [], []
    for i in idx[1:]:                      # segment (i-1, i) inside CS
        if not des[i - 1]:
            continue
        k = int(owner[i])
        xw = float(cols[k]["cline"][0, 0])
        x_st.append(xw)
        m_st.append(abs(float(f2[i] - f2[i - 1])))
    x_st = np.asarray(x_st)
    m_st = np.asarray(m_st)
    a = np.argsort(x_st)
    x_st, m_st = x_st[a], m_st[a]
    j = np.clip(np.searchsorted(xs_knots, x_st, side="right") - 1,
                0, len(xs_knots) - 2)
    masses = np.zeros(len(xs_knots) - 1)
    np.add.at(masses, j, m_st)
    return masses, x_st, m_st


def doerfler_mark(masses, theta):
    """Minimal set of intervals carrying >= theta of the total mass
    (Doerfler bulk marking), largest-first."""
    order = np.argsort(masses)[::-1]
    tot = float(masses.sum())
    if tot <= 0.0:
        return []
    acc, marked = 0.0, []
    for j in order:
        marked.append(int(j))
        acc += float(masses[j])
        if acc >= theta * tot:
            break
    return marked


def insertion_site(j, xs_knots, x_st, m_st):
    """Residual-mass median station inside interval j
    (equidistribution; knots are a subset of station sites, the
    FITPACK rule read at source). Returns None if the interval has
    no interior station or the site would create a degenerate
    interval (closer than one local station spacing to a knot)."""
    lo, hi = xs_knots[j], xs_knots[j + 1]
    sel = (x_st >= lo) & (x_st < hi)
    if not sel.any():
        return None
    xi_, mi_ = x_st[sel], m_st[sel]
    cum = np.cumsum(mi_)
    x_new = float(xi_[int(np.searchsorted(cum, 0.5 * cum[-1]))])
    dx_loc = float(np.median(np.diff(xi_))) if len(xi_) > 1 else hi - lo
    if (x_new - lo) < dx_loc or (hi - x_new) < dx_loc:
        return None
    return x_new


# ======================================================================
# S2  marches, goal metric, O3.1 spot check
# ======================================================================
def march(W, xi, tab, cfg, state_fn, solv, margin_floor=0.0):
    with design_class(xi):
        out, plan = TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                                      solvers=solv,
                                      margin_floor=margin_floor,
                                      return_field=True)
    return out, plan


def grad_and_J(W, xi, tab, cfg, plan, state_fn, solv):
    with design_class(xi):
        runj = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn,
                                        solvers=solv)

        def scalar_J(Wv):
            return TV.thrust_J(runj(Wv), tab, state_fn=state_fn)

        J = float(scalar_J(jnp.asarray(W)))
        g = np.asarray(jax.grad(scalar_J)(jnp.asarray(W)))
    return J, g, scalar_J


def goal_metric(W, xi, tab, cfg, state_fn, solv, r=1):
    """R3 corner mismatch at resolution r: |dJ/dy_lip - classical
    corner density| / |classical| — the quantity this session exists
    to move ([D1])."""
    cfg_r = O33.refine(cfg, r) if r > 1 else cfg
    out, plan = march(W, xi, tab, cfg_r, state_fn, solv)
    _, g, _ = grad_and_J(W, xi, tab, cfg_r, plan, state_fn, solv)
    cd, _ = O33.corner_density(np.asarray(out["wall"][-1]), state_fn)
    return abs(g[-1] - cd) / abs(cd), out, g, cd


def o31_spot(W, xi, scalar_J, g, J0):
    """O3.1 dot-product spot check at a design ([X-TOCV] recipe:
    FD two-step Richardson band + roundoff floor)."""
    v = np.asarray(np.random.default_rng(1).standard_normal(len(W)))
    v /= np.linalg.norm(v)
    Wj = jnp.asarray(W)

    def dirder(hsc):
        h = EPS ** (1.0 / 3.0) * hsc * max(1.0, float(np.abs(W).max()))
        return (float(scalar_J(Wj + h * jnp.array(v)))
                - float(scalar_J(Wj - h * jnp.array(v)))) / (2 * h)

    d1, d2 = dirder(1.0), dirder(0.5)
    tol = A1.K_RICH * (abs(d1 - d2) + A1.C_FLOOR * EPS ** (2.0 / 3.0)
                       * max(abs(J0), 1.0))
    return abs(d2 - float(g @ v)), tol


# ======================================================================
# S3  self-test of the indicator machinery (rejector-grade)
# ======================================================================
def selftest():
    print("-- S1 selftest: known-answer indicator + marking "
          "rejectors --")
    ok = True
    xs = np.linspace(0.0, 4.0, 9)              # 8 intervals
    x_st = np.linspace(0.05, 3.95, 79)
    # (a) single jump inside interval 5: all mass must land there
    m_st = np.zeros_like(x_st)
    m_st[(x_st >= xs[5]) & (x_st < xs[6])] = 1.0 / 10
    j = np.clip(np.searchsorted(xs, x_st, side="right") - 1, 0, 7)
    masses = np.zeros(8)
    np.add.at(masses, j, m_st)
    frac = masses[5] / masses.sum()
    marked = doerfler_mark(masses, 0.5)
    print("    single-jump chain: interval-5 mass fraction %.3f, "
          "Doerfler(0.5) marks %s" % (frac, marked))
    ok &= check("known-answer: >= 99% of mass in the jump interval "
                "and Doerfler marks exactly it",
                frac >= 0.99 and marked == [5])
    # (b) flat drift: marking must NOT concentrate on one interval
    m_flat = np.ones_like(x_st)
    masses_f = np.zeros(8)
    np.add.at(masses_f, j, m_flat)
    marked_f = doerfler_mark(masses_f, 0.5)
    print("    flat chain: Doerfler(0.5) marks %d intervals"
          % len(marked_f))
    ok &= check("flat-drift control: more than one interval marked "
                "(no false concentration)", len(marked_f) > 1)
    # (c) the estimator refuses an empty indicator
    ok &= check("zero-mass chain yields an empty marked set",
                doerfler_mark(np.zeros(8), 0.5) == [])
    return ok


# ======================================================================
def report_indicator(label, masses, xs_knots):
    tot = masses.sum()
    conc = float(masses.max() / max(np.mean(masses), 1e-300))
    print("  [%s] indicator mass per knot interval (total %.4e, "
          "max/mean concentration %.2f):" % (label, tot, conc))
    for jj in range(len(masses)):
        print("      [%6.3f, %6.3f) : %.4e  (%5.1f%%)"
              % (xs_knots[jj], xs_knots[jj + 1], masses[jj],
                 100.0 * masses[jj] / max(tot, 1e-300)))
    for th in (0.3, 0.5, 0.7):
        print("      Doerfler theta=%.1f marks %s"
              % (th, doerfler_mark(masses, th)))
    return conc


def xs_of(W, xi, cfg):
    thB = float(W[0])
    xB = cfg["rtd"] * np.sin(thB)
    L = cfg["xtronc"]
    m = len(W) - 1
    x_i = (np.asarray(xi) if xi is not None
           else np.arange(1, m + 1) / m)
    return np.concatenate([[xB], xB + (L - xB) * x_i])


def main():
    stage = os.environ.get("A1_AKN_STAGE", "all")
    max_cyc = int(os.environ.get("A1_AKN_MAXCYC", "4"))
    max_ins = int(os.environ.get("A1_AKN_MAXINS", "3"))
    budget_s = float(os.environ.get("A1_AKN_BUDGET_S", "5400"))
    theta = 0.5
    print("== ADAPTIVE KNOT CLASS [X-AKNO] (JAX %s; stage %s; budget "
          "%d cycles / %.0f s / %d insertions-per-cycle) =="
          % (jax.__version__, stage, max_cyc, budget_s, max_ins))
    t_session = time.perf_counter()
    ok = True

    if stage in ("selftest", "all"):
        ok &= selftest()
        if stage == "selftest":
            return 0 if ok else 1

    tab = A1.prep_tab(A1.build_tab_nasa())
    state_c1, solv, cfg = O33.make_case(tab)
    W8 = np.asarray(O33.W_STAR, dtype=float)

    # ---------------- baseline: incumbent 8-node uniform optimum ----
    print("-- baseline: S18 optimum W* (8 uniform nodes) --")
    out0, plan0 = march(W8, None, tab, cfg, state_c1, solv)
    print("  record: %d cells, cert worst %.3e, min margin %.4f m/s"
          % (out0["cert_n"], out0["cert_worst"], out0["min_margin"]))
    ok &= check("baseline re-certified", out0["cert_worst"] <= 1.0
                and out0["min_margin"] > 0.0)
    delta_inst = float(out0["min_margin"]) / A1.K_RICH
    print("  [P4] instance margin floor delta = min_margin(W*)/K_RICH "
          "= %.4f m/s" % delta_inst)
    xs0 = xs_of(W8, None, cfg)
    masses0, x_st0, m_st0 = indicator_masses(out0, state_c1, xs0)
    conc0 = report_indicator("W* 8-node", masses0, xs0)
    marked0 = doerfler_mark(masses0, theta)
    ok &= check("S2 live marking is a STRICT subset of intervals "
                "(indicator carries information)",
                0 < len(marked0) < len(masses0))

    # goal metric + its measured noise floor (r=1 vs r=2), gate [D3]
    print("  goal metric at baseline (r=1 and r=2 -> measured noise "
          "floor)...")
    rel1, _, g1, cd1 = goal_metric(W8, None, tab, cfg, state_c1, solv,
                                   r=1)
    rel2, _, _, _ = goal_metric(W8, None, tab, cfg, state_c1, solv,
                                r=2)
    tol_stop = A1.K_RICH * abs(rel1 - rel2)
    print("  baseline corner mismatch: %.4e (r=1), %.4e (r=2) -> "
          "tol_stop = K_RICH x |diff| = %.4e"
          % (rel1, rel2, tol_stop))
    if stage == "baseline":
        print("VERDICT (stage baseline): %s" % ("PASS" if ok else
                                                "FAIL"))
        return 0 if ok else 1

    # ---------------- the enrichment cycles --------------------------
    print("-- enrichment cycles (Doerfler theta = %.1f; stop on "
          "measured improvement < tol_stop, rise, empty set, or "
          "budget) --" % theta)
    W_cur = W8.copy()
    xi_cur = None
    goal_hist = [rel1]
    best = dict(W=W8.copy(), xi=None, goal=rel1, cycle=0)
    masses, x_st, m_st = masses0, x_st0, m_st0
    yL = cfg["yt"] * np.sqrt(TV.TCASE["eps"])
    for cyc in range(1, max_cyc + 1):
        if time.perf_counter() - t_session > budget_s:
            print("  [budget] wall-clock budget exhausted before "
                  "cycle %d — honest stop" % cyc)
            break
        xs_cur = xs_of(W_cur, xi_cur, cfg)
        marked = doerfler_mark(masses, theta)[:max_ins]
        sites = []
        for j in sorted(marked):
            xn = insertion_site(j, xs_cur, x_st, m_st)
            if xn is None:
                print("  [cycle %d] interval %d: no admissible site "
                      "(skipped, declared)" % (cyc, j))
            else:
                sites.append(xn)
        if not sites:
            print("  [cycle %d] marked set yields no admissible "
                  "insertion — stop" % cyc)
            break
        # new knot vector (normalized), warm-start heights
        thB = float(W_cur[0])
        xB = cfg["rtd"] * np.sin(thB)
        L = cfg["xtronc"]
        xi_old = (np.asarray(xi_cur) if xi_cur is not None
                  else np.arange(1, len(W_cur)) / (len(W_cur) - 1))
        xi_new = np.sort(np.concatenate(
            [xi_old, (np.asarray(sites) - xB) / (L - xB)]))
        with design_class(xi_cur, m=len(W_cur) - 1):
            _, _, oxs, oys, oM = TV.wall_geometry(
                jnp.asarray(W_cur),
                jnp.array([cfg["yt"], cfg["rtu"], cfg["rtd"]]), L)
            y_new = np.array([float(TV.spline_eval(
                jnp.float64(xB + (L - xB) * t), oxs, oys, oM)[0])
                for t in xi_new])
        y_new[-1] = yL
        W_warm = np.concatenate([[thB], y_new])
        # measured warm-start representation deviation (dense grid)
        xg = np.linspace(xB, L, 400)
        with design_class(xi_cur, m=len(W_cur) - 1):
            y_old_g = np.array([float(TV.spline_eval(
                jnp.float64(x), oxs, oys, oM)[0]) for x in xg])
        with design_class(xi_new):
            _, _, nxs, nys, nM = TV.wall_geometry(
                jnp.asarray(W_warm),
                jnp.array([cfg["yt"], cfg["rtu"], cfg["rtd"]]), L)
            y_new_g = np.array([float(TV.spline_eval(
                jnp.float64(x), nxs, nys, nM)[0]) for x in xg])
        dev_warm = float(np.max(np.abs(y_new_g - y_old_g)))
        print("  [cycle %d] insert %d knot(s) at %s -> class m = %d; "
              "warm-start wall deviation %.3e (measured, declared)"
              % (cyc, len(sites),
                 np.array2string(np.asarray(sites), precision=4),
                 len(xi_new), dev_warm))
        # re-optimize in the enriched class (derived tolerances, the
        # [X-TOCV] recipe at the warm start)
        out_w, plan_w = march(W_warm, xi_new, tab, cfg, state_c1, solv)
        J_w, g_w, scalJ_w = grad_and_J(W_warm, xi_new, tab, cfg,
                                       plan_w, state_c1, solv)
        dp, tol_dp = o31_spot(W_warm, xi_new, scalJ_w, g_w, J_w)
        ok &= check("cycle %d O3.1 at warm start" % cyc, dp <= tol_dp)
        gtol = max(tol_dp, 1e-8 * float(np.linalg.norm(g_w)))
        t_opt = time.perf_counter()
        try:
            with design_class(xi_new):
                opt = TV.run_trsqp(W_warm, tab, cfg, yL, gtol=gtol,
                                   xtol=1e-10, state_fn=state_c1,
                                   solvers=solv, verbose=0)
        except RuntimeError as err:
            # honest stop: a genuine gate failure (reject-and-shrink
            # exhausted down to the radius floor) ends the enrichment
            # loop with the incumbent best kept — reported, never
            # masked (general-vision-nondivergence).
            print("  [cycle %d] TR-SQP gate failure of record: %s -> "
                  "enrichment stopped, best design kept from cycle %d"
                  % (cyc, err, best["cycle"]))
            break
        t_opt = time.perf_counter() - t_opt
        res = opt["res"]
        print("  [cycle %d] TR-SQP: segments %d, re-records %d, nit "
              "%d, %.0f s; status %d, KKT %.3e (gtol %.3e), constr "
              "%.3e" % (cyc, opt["n_segments"], opt["re_records"],
                        opt["nit_total"], t_opt, res.status,
                        res.optimality, gtol, res.constr_violation))
        W_new = opt["W"]
        cert_lim = bool(opt.get("certifiability_limited"))
        # OUTCOME CLASSES, both declared BEFORE the decisive run
        # (log steps 6-7): outcome I = CONVERGED in-stratum (the S18
        # gate unchanged); outcome II = CERTIFIABILITY-LIMITED
        # (reject-and-shrink exhausted; the driver returned the last
        # CERTIFIED base with the KKT reported OPEN). [D1] VALIDITY
        # CONDITION (log step 7, R5, fixed before any decisive run):
        # the corner identity is DERIVED FROM OPTIMALITY — [X-O33B]'s
        # own R3 control requires it to BREAK at non-optimal designs
        # — so outcome-II designs are EXCLUDED from the [D1] goal
        # comparison; their goal is printed as INFORMATION ONLY and
        # the enrichment loop STOPS (the obstruction goes to
        # adjudication: the armed certdiag, then a user decision).
        if cert_lim:
            print("  [cycle %d] CERTIFIABILITY-LIMITED outcome "
                  "(declared, outcome II): reject-and-shrink "
                  "exhausted, KKT OPEN at %.3e — [D1]-INELIGIBLE by "
                  "the validity condition" % (cyc, res.optimality))
        else:
            ok &= check("cycle %d TR-SQP converged in-stratum" % cyc,
                        res.status in (1, 2)
                        and res.constr_violation <= gtol)
        # P4 audit of the converged design against the instance floor
        out_n, plan_n = march(W_new, xi_new, tab, cfg, state_c1, solv,
                              margin_floor=delta_inst)
        print("  [cycle %d] P4 audit: min margin %.4f >= floor %.4f"
              % (cyc, out_n["min_margin"], delta_inst))
        ok &= check("cycle %d P4 margin-floor audit" % cyc,
                    out_n["min_margin"] >= delta_inst)
        J_n, g_n, scalJ_n = grad_and_J(W_new, xi_new, tab, cfg,
                                       plan_n, state_c1, solv)
        dp, tol_dp = o31_spot(W_new, xi_new, scalJ_n, g_n, J_n)
        ok &= check("cycle %d O3.1 at the new optimum" % cyc,
                    dp <= tol_dp)
        cd_n, _ = O33.corner_density(np.asarray(out_n["wall"][-1]),
                                     state_c1)
        goal = abs(g_n[-1] - cd_n) / abs(cd_n)
        if cert_lim:
            # J_n and goal come from W_new's OWN P4-audited record
            # (plan_n) — never from a replay on another design's plan.
            print("  [cycle %d] J(warm start) = %.7e -> J(returned "
                  "certified base) = %.7e; corner mismatch = %.4e "
                  "[INFORMATION ONLY: non-stationary design, "
                  "excluded from [D1] by the validity condition]"
                  % (cyc, float(J_w), J_n, goal))
            ok &= check("cycle %d certifiability-limited stop still "
                        "produced a CERTIFIED objective improvement "
                        "over its warm start" % cyc, J_n > float(J_w))
            W_cur, xi_cur = W_new, xi_new
            # S22 T2 (retro-diagnosis entry row): persist the returned
            # certified base WITH its class when asked — the C-1
            # three-way locus test runs on the last certified base AND
            # the rejected designs, and a design without its class is
            # not re-recordable. Additive, env-gated, default off.
            path_cl = os.environ.get("A1_AKN_CERTLIM_SAVE")
            if path_cl:
                with open(path_cl, "w") as fh:
                    json.dump(dict(
                        W=[repr(float(x)) for x in W_new],
                        xi=[repr(float(x)) for x in xi_new],
                        cycle=int(cyc),
                        provenance="[X-AKNO] certifiability-limited "
                                   "returned base (outcome II)"), fh,
                        indent=1)
            print("  [stop] enrichment OBSTRUCTED at the "
                  "certifiability boundary of cycle %d's walk — "
                  "adjudication (certdiag + user decision) is the "
                  "named next step" % cyc)
            break
        impr = goal_hist[-1] - goal
        print("  [cycle %d] J = %.7e; goal (corner mismatch) = %.4e "
              "(prev %.4e, improvement %.4e vs tol_stop %.4e)"
              % (cyc, J_n, goal, goal_hist[-1], impr, tol_stop))
        goal_hist.append(goal)
        if goal < best["goal"]:
            best = dict(W=W_new.copy(), xi=xi_new.copy(), goal=goal,
                        cycle=cyc)
        # refresh the indicator on the new optimum for the next cycle
        masses, x_st, m_st = indicator_masses(out_n, state_c1,
                                              xs_of(W_new, xi_new,
                                                    cfg))
        report_indicator("cycle %d optimum" % cyc, masses,
                         xs_of(W_new, xi_new, cfg))
        W_cur, xi_cur = W_new, xi_new
        if impr < 0:
            print("  [stop] goal ROSE (reported honestly; best design "
                  "kept from cycle %d)" % best["cycle"])
            break
        if impr < tol_stop:
            print("  [stop] improvement below the measured floor "
                  "tol_stop — converged")
            break

    # ---------------- verdict + artifact ------------------------------
    print("-- summary --")
    print("  goal history: %s"
          % np.array2string(np.asarray(goal_hist), precision=6))
    print("  best: cycle %d, m = %d dofs, goal = %.4e  (S19 baseline "
          "6.6295e-02)" % (best["cycle"],
                           len(best["W"]) - 1, best["goal"]))
    # [D1] semantics (validity condition, log step 7): the kill test
    # is DEFINED only over outcome-I (in-stratum converged) cycles.
    # best[] is updated only by those, so best.cycle == 0 means no
    # eligible design exists: [D1] is then UNTESTABLE — the diagnosis
    # is neither confirmed nor falsified, the campaign did not reach
    # its verdict, and the carrier exits nonzero by construction
    # (the [X-O32] precedent: exit 1 = "not all rows conclude").
    if best["cycle"] > 0:
        ok &= check("[D1] the adaptive-class optimum pulls the "
                    "corner mismatch BELOW the S19 baseline (else "
                    "the design-class diagnosis is FALSIFIED)",
                    best["goal"] < rel1)
    else:
        print("  [D1] UNTESTABLE on this run: no cycle converged "
              "in-stratum, so no [D1]-eligible design exists — the "
              "design-class diagnosis is NEITHER confirmed NOR "
              "falsified; the obstruction goes to adjudication "
              "(certdiag + user decision)")
        ok = False
    art = dict(
        W=[repr(float(w)) for w in best["W"]],
        xi=([repr(float(t)) for t in best["xi"]]
            if best["xi"] is not None else None),
        goal=repr(float(best["goal"])),
        goal_history=[repr(float(gh)) for gh in goal_hist],
        cycle=best["cycle"],
        baseline_r1=repr(float(rel1)), baseline_r2=repr(float(rel2)),
        tol_stop=repr(float(tol_stop)), theta=theta,
        d1_eligible=bool(best["cycle"] > 0),
        provenance="[X-AKNO] S20; incumbent = S18 W* of record")
    with open(ART, "w") as f:
        json.dump(art, f, indent=1)
    print("  design of record written to %s" % ART)
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
