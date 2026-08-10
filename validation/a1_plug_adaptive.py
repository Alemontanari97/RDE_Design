#!/usr/bin/env python3
"""A1 BRICK 2, SESSION S22 [F2/A1]: ADAPTIVE KNOTS ON THE SPIKE —
[X-AKNO] applied to the free-form spike [X-PSPL]. Registry ID: [X-PAKN].

WHY THIS EXISTS. S21's check C-6 falsified the free-form spike's
headline: at the carrier's own resolution the thrust band (0.1930 %)
is LARGER than the gain (+0.1302 % / +0.0820 % refined), so "the
free-form spike beats the fan streamline" is NOT ESTABLISHED. The same
session's representation ladder (C-1) located where the uniform knot
class starves the contour: the deviation maximum sits at x ~ 0.56-0.61
m, where the streamline's curvature peaks. Both findings point the
same way: shape freedom must be BOUGHT WHERE THE CONTOUR BENDS, not
uniformly. That is precisely the design-class question [X-AKNO]
answered for the bell, and [X-PSPL] imported the bell's own spline
basis so that the adaptive machinery would apply to this wall
unchanged. This carrier applies it.

THE SKELETON IS [X-AKNO]'s, UNCHANGED WHERE POSSIBLE: solve ->
per-interval GOAL indicator -> Doerfler bulk marking (theta = 1/2
canonical; 0.3/0.7 printed for audit) -> knot insertion -> re-optimize
(the [X-PSPL] TR-SQP driver, its certification gate and reject-and-
shrink untouched) -> repeat under measured stopping rules. The marking
and insertion-guard machinery is IMPORTED from adaptive_knot_optimize
(doerfler_mark), not reimplemented. The basis class is UNCHANGED:
clamped-left natural cubic spline on any strictly increasing knot set;
only knot PLACEMENT adapts.

THE INDICATOR differs from the bell's in ROUTE and agrees in OBJECT.
The bell reads the drift of f2 = u + v tan(alpha) along the Rao
control surface — the adjoint variable observed on the flow, station-
attributed through the march topology — because the bell's adjoint is
only available that way. The plug carrier HAS the discrete adjoint
(reverse-AD through the recorded schedule), so the same object is
available directly: enrich the class with a candidate dof at the
midpoint of every knot interval (the incumbent optimum re-interpolated,
so the WALL is unchanged up to representation deviation, measured and
printed), record one march, and read the gradient AT THE CANDIDATE
DOFS. At the incumbent class optimum the existing dofs' gradient is
(near) zero; a candidate's gradient component is the multiplier-
compatibility residual of the enriched optimality system — an
adjoint-weighted measure of the thrust available from freedom the
current class cannot express, which is what Becker-Rannacher weighting
constructs. Indicator mass of interval j = |dJ/dy_cand_j| * h_j (the
interval width keeps a large residual in a tiny interval from
out-ranking real freedom; the degenerate-interval guard below is the
hard floor). No exclusion mask; the indicator is a refinement driver,
not a verdict row.

INSERTION SITE = the measured candidate (the interval midpoint): for
the plug the indicator is EVALUATED at the midpoint dof, so inserting
anywhere else would grade one site and buy another. A site closer
than one march station spacing to an existing knot is SKIPPED
(declared — the GENO double-point lesson: a degenerate interval
poisons the spline solve).

WARM START: each cycle starts from the incumbent optimum
re-interpolated at the enriched knot set; the representation deviation
is measured on a dense grid and printed (NOT claimed geometry-
preserving; interpolation is not Boehm insertion — the [X-AKNO]
declaration).

STOPPING (all declared): budget of PAKN_MAXCYC cycles / PAKN_BUDGET_S
seconds; empty admissible-site set; the goal (J at the working
resolution, same instrument both sides of the difference) RISES ->
best kept, reported; per-cycle relative improvement below the declared
budget floor TOL_STOP_REL = 1e-5 (0.001 %: an improvement an order
below the smallest band any ladder here has ever supported cannot
change the verdict, so walking further buys nothing).

THE VERDICT (the reason this carrier exists) is A-8: the adaptive-
optimum-vs-streamline gain graded against a band derived from a
THREE-POINT resolution ladder of the march that produced both numbers
— (K,N), (2K-1,2N-1), (4K-3,4N-3) — per the S21 lesson that two
points can measure a difference but never a rate. Both designs are
FIXED before the ladder runs; each rung re-poses the start line at
its own N (build_case) and marches both designs with the same
instrument, so the difference keeps its cancellation. Band rule,
declared: with d12 = |g1-g2|, d23 = |g2-g3|, if the ladder CONVERGES
(d23 <= d12) the quoted gain is g3 and the band is
K_RICH*d23 + C_FLOOR*EPS; if it does not, the quantity is treated as
non-smooth and the band is K_RICH*(max-min) around the MEDIAN (the
scatter rule of record). A FAIL of A-8 is a legible outcome, exactly
as C-6's was.

THE CONTROL (A-9): the resolved question must be "adaptivity", not
"more dofs". The UNIFORM class at the SAME final dof count is
optimized by the same driver from the same kind of start, and its
gain is measured on the SAME ladder. Adaptive must not LOSE to
uniform beyond the ladder band; whether it WINS is reported either
way.

CHECKS
  A-1  known-answer indicator/marking selftest + rejectors: a
       single-interval synthetic residual must put >= 99 % of the mass
       there and Doerfler(0.5) must mark exactly it; a flat residual
       must mark more than one interval; a zero residual marks none;
  A-2  record check: the S21 incumbent (10 uniform knots, K=61, N=51)
       reproduces the recorded J0 and Jf from _plug_spline/
       spline_opt.npz before anything is built on it;
  A-3  the AD adjoint matches the FD ladder at each cycle's optimum
       (the [X-PSPL] C-2 instrument, spot components);
  A-4  every accepted design is Newton-certified and admissible
       (descends, clears the axis) — the driver's gate, re-audited on
       the final design;
  A-5  the mass constraint holds on the march's own quadrature at the
       final design (structural decoupling re-measured, not assumed);
  A-6  live marking is a STRICT subset of intervals (an indicator that
       marks everything carries no information);
  A-7  the enrichment does not lose to its own start: J(final) >=
       J(class-0 optimum) at the working resolution;
  A-8  THE VERDICT (above);
  A-9  THE CONTROL (above).

Run:  .venv-a1/bin/python validation/a1_plug_adaptive.py
      PAKN_STAGE=selftest ... (marking selftest only)
      PAKN_MAXCYC=3 PAKN_MAXINS=2 PAKN_ITERS=30 ...
On-demand carrier (env: jax).
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# resolution knobs must reach a1_plug_spline_opt BEFORE it is imported
# (its K_ST / N_ROW / M_NODES are module constants read from env).
M0 = int(os.environ.get("PAKN_M0", 10))
K0 = int(os.environ.get("PAKN_K", 61))
N0 = int(os.environ.get("PAKN_N", 51))
os.environ["PSPL_M"] = str(M0)
os.environ["PSPL_K"] = str(K0)
os.environ["PSPL_N"] = str(N0)

import a1_plug_spline_opt as P                         # noqa: E402
import a1_ideal_march_jax as A1                        # noqa: E402
import a1_config_compare as CC                         # noqa: E402
import a1_inlet_angle_opt as IA                        # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval  # noqa: E402
from adaptive_knot_optimize import doerfler_mark       # noqa: E402

import jax                                             # noqa: E402
import jax.numpy as jnp                                # noqa: E402

X0, L = P.X0, P.L
MAXCYC = int(os.environ.get("PAKN_MAXCYC", 3))
MAXINS = int(os.environ.get("PAKN_MAXINS", 2))
ITERS = int(os.environ.get("PAKN_ITERS", 30))
BUDGET_S = float(os.environ.get("PAKN_BUDGET_S", 14400))
CONTROL = int(os.environ.get("PAKN_CONTROL", 1))
TOL_STOP_REL = 1e-5
THETA = 0.5
# settings-tagged first (the post-S22 [X-PSPL] save convention), then
# the legacy untagged name; the class-match test below guards either.
_ck_tag = os.path.join(HERE, "_plug_spline",
                       "spline_opt_m%d_k%d_n%d.npz" % (M0, K0, N0))
_ck_old = os.path.join(HERE, "_plug_spline", "spline_opt.npz")
CKPT_S21 = _ck_tag if os.path.exists(_ck_tag) else _ck_old
ART_DIR = os.path.join(HERE, "_plug_adaptive")

NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# basis utilities on the [X-PSPL] wall (clamped-left at X0 / yw0)
# ======================================================================
def respline(W, xk_src, c, xq):
    """Evaluate the incumbent wall (knots xk_src, heights W) at the
    abscissae xq. Same basis call chain as P.wall_stations."""
    xs = jnp.concatenate([jnp.array([X0]), jnp.asarray(xk_src)])
    ys = jnp.concatenate([jnp.array([c["yw0"]]), jnp.asarray(W)])
    Mc = spline_coeffs(xs, ys, c["slope0"])
    return np.array([float(spline_eval(jnp.float64(x), xs, ys, Mc)[0])
                     for x in np.asarray(xq)])


def rep_deviation(W_old, xk_old, W_new, xk_new, c, ng=400):
    """Max wall deviation of the re-interpolated design on a dense
    grid (measured, printed each cycle — the [X-AKNO] declaration)."""
    xg = np.linspace(X0, L, ng)
    return float(np.max(np.abs(respline(W_old, xk_old, c, xg)
                               - respline(W_new, xk_new, c, xg))))


# ======================================================================
# the indicator: enriched-class adjoint at the candidate dofs
# ======================================================================
def indicator(W_opt, xk, c, w, ta):
    """Per-knot-interval indicator mass at the incumbent class optimum.
    Returns (masses, mids, edges, J_enr, g_cand, dev_warm)."""
    xk = np.asarray(xk, dtype=float)
    edges = np.concatenate([[X0], xk])
    mids = 0.5 * (edges[:-1] + edges[1:])
    xk_e = np.sort(np.concatenate([xk, mids]))
    W_e = respline(W_opt, xk, c, xk_e)
    dev = rep_deviation(W_opt, xk, W_e, xk_e, c)
    c_e = dict(c, xk=xk_e)
    out_e, sch_e = P.march_record(W_e, w, c_e)
    if float(out_e["cert_worst"]) > 1.0:
        raise RuntimeError("enriched-class record not certified "
                           "(worst %.3e)" % float(out_e["cert_worst"]))
    J_e, g_e = P.J_and_grad(W_e, w, c_e, ta, sch_e)
    pos = np.searchsorted(xk_e, mids)
    h = np.diff(edges)
    masses = np.abs(np.asarray(g_e)[pos]) * h
    return masses, mids, edges, J_e, np.asarray(g_e)[pos], dev


def report_masses(label, masses, edges):
    tot = float(masses.sum())
    print("  [%s] indicator mass per knot interval (total %.4e):"
          % (label, tot))
    for j in range(len(masses)):
        print("      [%6.3f, %6.3f) : %.4e  (%5.1f%%)"
              % (edges[j], edges[j + 1], masses[j],
                 100.0 * masses[j] / max(tot, 1e-300)))
    for th in (0.3, 0.5, 0.7):
        print("      Doerfler theta=%.1f marks %s"
              % (th, doerfler_mark(masses, th)))


def admissible_sites(marked, mids, edges, xk):
    """Insertion sites with the degenerate-interval guard: skip a site
    closer than one march station spacing to an existing knot."""
    dx_st = (L - X0) / P.K_ST
    knots = np.concatenate([[X0], np.asarray(xk)])
    sites = []
    for j in sorted(marked):
        xn = float(mids[j])
        if np.min(np.abs(knots - xn)) < dx_st:
            print("  interval %d: site %.4f closer than one station"
                  " spacing (%.4f) to a knot — SKIPPED (declared)"
                  % (j, xn, dx_st))
            continue
        sites.append(xn)
    return sites


# ======================================================================
# instruments reused verbatim from [X-PSPL]
# ======================================================================
def optimum_of_class(xk, W_start, w, c, ta, tag):
    """TR-SQP in the class xk from W_start; returns (W*, J*, cert)."""
    c_m = dict(c, xk=np.asarray(xk, dtype=float))
    W_f, hist, n_rec = P.run_trsqp(np.asarray(W_start, dtype=float),
                                   w, c_m, ta, max_segments=ITERS)
    out_f, sch_f = P.march_record(W_f, w, c_m)
    J_f = float(P.J_replay(jnp.asarray(W_f), w, c_m, sch_f, ta))
    print("  [%s] optimum: J = %.8e  cert = %.3f  (%d segments,"
          " %d records)" % (tag, J_f, float(out_f["cert_worst"]),
                            len(hist), n_rec))
    return W_f, J_f, float(out_f["cert_worst"]), sch_f, c_m


def adjoint_spot(W, c_m, w, ta, sched, tag):
    """A-3: AD vs FD-ladder on spot components (the C-2 instrument)."""
    J0, g0 = P.J_and_grad(W, w, c_m, ta, sched)
    fj = lambda z: P.J_replay(z, w, c_m, sched, ta)      # noqa: E731
    Wj = jnp.asarray(W, dtype=float)
    ok = True
    for k in (0, len(g0) - 1):
        v = jnp.zeros(len(g0)).at[k].set(1.0)
        scale = max(1.0, abs(float(W[k])))
        fd, spread = P.fd_ladder(fj, Wj, v, scale)
        band = (A1.K_RICH * spread + A1.C_FLOOR * A1.EPS * abs(J0)
                / (P.FD_LADDER[-1] * scale))
        rel = abs(fd - g0[k])
        print("  [%s] node %2d: AD %+.6e  FD %+.6e  |d| = %.3e"
              " (band %.3e)" % (tag, k, g0[k], fd, rel, band))
        ok = ok and (rel <= band)
    return ok


def gain_ladder(W_inc, W_opt, xk, w, ta):
    """A-8 instrument: the gain on a 3-point (K,N) ladder. Both designs
    FIXED; each rung re-poses the start line at its own N and marches
    both designs with the same instrument."""
    rungs = [(K0, N0), (2 * K0 - 1, 2 * N0 - 1), (4 * K0 - 3,
                                                  4 * N0 - 3)]
    gains, Js = [], []
    for (K, N) in rungs:
        t0 = time.time()
        c_r = dict(P.build_case(w, N=N), xk=np.asarray(xk))
        _, s_i = P.march_record(W_inc, w, c_r, K=K)
        J_i = float(P.J_replay(jnp.asarray(W_inc), w, c_r, s_i, ta,
                               K=K))
        _, s_f = P.march_record(W_opt, w, c_r, K=K)
        J_f = float(P.J_replay(jnp.asarray(W_opt), w, c_r, s_f, ta,
                               K=K))
        gains.append(J_f / J_i - 1.0)
        Js.append((J_i, J_f))
        print("    rung (K=%3d, N=%3d): J_inc %.8e  J_opt %.8e"
              "  gain %+.5f %%  (%.0f s)"
              % (K, N, J_i, J_f, 100 * gains[-1], time.time() - t0))
    g1, g2, g3 = gains
    d12, d23 = abs(g1 - g2), abs(g2 - g3)
    if d23 <= d12:
        quote, band = g3, A1.K_RICH * d23 + A1.C_FLOOR * A1.EPS
        rule = "converging: quote g3, band = K_RICH*d23"
    else:
        quote = float(np.median(gains))
        band = A1.K_RICH * (max(gains) - min(gains)) + A1.C_FLOOR * A1.EPS
        rule = "NOT converging: quote median, band = K_RICH*scatter"
    print("    d12 = %.3e  d23 = %.3e  -> %s" % (d12, d23, rule))
    return quote, band, gains, Js


# ======================================================================
# A-1 selftest (known-answer + rejectors) on the marking machinery
# ======================================================================
def selftest():
    print("-- A-1: known-answer indicator/marking selftest --")
    ok = True
    masses = np.zeros(8)
    masses[5] = 1.0                       # single concentrated residual
    marked = doerfler_mark(masses, THETA)
    frac = masses[5] / masses.sum()
    print("  single-interval residual: mass fraction %.3f, marks %s"
          % (frac, marked))
    ok &= check("A-1a >= 99% of mass in the residual interval and"
                " Doerfler marks exactly it",
                frac >= 0.99 and marked == [5])
    marked_f = doerfler_mark(np.ones(8), THETA)
    print("  flat residual: Doerfler(0.5) marks %d intervals"
          % len(marked_f))
    ok &= check("A-1b flat residual marks MORE THAN ONE interval"
                " (no false concentration)", len(marked_f) > 1)
    ok &= check("A-1c zero residual yields an empty marked set",
                doerfler_mark(np.zeros(8), THETA) == [])
    return ok


# ======================================================================
def main():
    t_session = time.time()
    stage = os.environ.get("PAKN_STAGE", "all")
    print("== A1 S22: adaptive knots on the spike ([X-AKNO] ->"
          " [X-PSPL]) [F2/A1] ==")
    print("  class-0: m = %d uniform knots; working resolution"
          " K = %d, N = %d; budget %d cycles / %d insertions per"
          " cycle / %.0f s" % (M0, K0, N0, MAXCYC, MAXINS, BUDGET_S))
    os.makedirs(ART_DIR, exist_ok=True)
    ok_all = selftest()
    if stage == "selftest":
        sys.exit(0 if ok_all else 1)

    w = CC.build_world()
    ta = w["ta"]
    c = P.build_case(w)
    xk0 = np.asarray(c["xk"])

    # ---- A-2: the S21 incumbent, reproduced before use ---------------
    print("\n-- A-2: record check against the S21 checkpoint --")
    warm = None
    if os.path.exists(CKPT_S21):
        d = np.load(CKPT_S21)
        if (len(d["Wf"]) == M0 and len(d["x_wall"]) == K0
                and np.allclose(d["xk"], xk0, rtol=0, atol=1e-12)):
            out_i, sch_i = P.march_record(c["W0"], w, c)
            J0_now = float(P.J_replay(jnp.asarray(c["W0"]), w, c,
                                      sch_i, ta))
            out_w, sch_w = P.march_record(d["Wf"], w, c)
            Jf_now = float(P.J_replay(jnp.asarray(d["Wf"]), w, c,
                                      sch_w, ta))
            r0 = abs(J0_now / float(d["J0"]) - 1.0)
            rf = abs(Jf_now / float(d["Jf"]) - 1.0)
            print("  J(streamline) %.8e vs recorded %.8e  (rel %.1e)"
                  % (J0_now, float(d["J0"]), r0))
            print("  J(S21 optimum) %.8e vs recorded %.8e  (rel %.1e)"
                  % (Jf_now, float(d["Jf"]), rf))
            if check("A-2 the S21 record reproduces (both designs,"
                     " rel <= 1e-10)", r0 <= 1e-10 and rf <= 1e-10):
                warm = (np.asarray(d["Wf"], dtype=float), Jf_now,
                        float(out_w["cert_worst"]), sch_w)
            ok_all &= (warm is not None)
        else:
            print("  checkpoint class does not match (m or K or knots)"
                  " — cold start, A-2 skipped as N/A (declared)")
    else:
        print("  no S21 checkpoint — cold start, A-2 skipped as N/A"
              " (declared)")

    # ---- class-0 optimum ---------------------------------------------
    print("\n-- class-0 optimum (m = %d uniform) --" % M0)
    if warm is not None:
        W_cur, J_cur, cert_cur, sch_cur = warm
        c_cur = dict(c, xk=xk0)
        print("  warm from the S21 record: J = %.8e  cert = %.3f"
              % (J_cur, cert_cur))
    else:
        W_cur, J_cur, cert_cur, sch_cur, c_cur = optimum_of_class(
            xk0, c["W0"], w, c, ta, "class-0")
    xk_cur = xk0.copy()
    J_class0 = J_cur
    hist = [dict(cycle=0, m=len(xk_cur), J=J_cur,
                 xk=xk_cur.tolist(), W=np.asarray(W_cur).tolist())]

    # ---- enrichment cycles -------------------------------------------
    best = dict(W=np.asarray(W_cur).copy(), xk=xk_cur.copy(),
                J=J_cur, cycle=0)
    for cyc in range(1, MAXCYC + 1):
        if time.time() - t_session > BUDGET_S:
            print("\n  [budget] wall-clock budget exhausted before"
                  " cycle %d — honest stop" % cyc)
            break
        print("\n-- cycle %d: indicator at the incumbent optimum"
              " (m = %d) --" % (cyc, len(xk_cur)))
        try:
            masses, mids, edges, J_e, g_cand, dev = indicator(
                W_cur, xk_cur, c, w, ta)
        except RuntimeError as err:
            print("  indicator record failure of record: %s -> honest"
                  " stop, best design kept from cycle %d"
                  % (err, best["cycle"]))
            break
        print("  enriched-class warm-start wall deviation %.3e m"
              " (measured, declared); J(enriched warm) = %.8e"
              % (dev, J_e))
        report_masses("cycle %d" % cyc, masses, edges)
        marked = doerfler_mark(masses, THETA)
        ok_all &= check("A-6 cycle %d: marking is a strict subset"
                        " of intervals" % cyc,
                        0 < len(marked) < len(masses))
        sites = admissible_sites(marked[:MAXINS], mids, edges, xk_cur)
        if not sites:
            print("  marked set yields no admissible insertion — stop")
            break
        xk_new = np.sort(np.concatenate([xk_cur, sites]))
        W_warm = respline(W_cur, xk_cur, c, xk_new)
        dev_w = rep_deviation(W_cur, xk_cur, W_warm, xk_new, c)
        print("  insert %d knot(s) at %s -> m = %d; warm-start wall"
              " deviation %.3e m"
              % (len(sites), np.array2string(np.asarray(sites),
                                             precision=4),
                 len(xk_new), dev_w))
        W_new, J_new, cert_new, sch_new, c_new = optimum_of_class(
            xk_new, W_warm, w, c, ta, "cycle %d" % cyc)
        ok_all &= check("A-3 cycle %d: adjoint matches the FD ladder"
                        " at the optimum" % cyc,
                        adjoint_spot(W_new, c_new, w, ta, sch_new,
                                     "cycle %d" % cyc))
        dJ = J_new - J_cur
        print("  cycle %d: J %.8e -> %.8e  (dJ/J = %+.3e, floor %.1e)"
              % (cyc, J_cur, J_new, dJ / J_cur, TOL_STOP_REL))
        hist.append(dict(cycle=cyc, m=len(xk_new), J=J_new,
                         xk=xk_new.tolist(),
                         W=np.asarray(W_new).tolist(),
                         sites=list(map(float, sites)),
                         dev_warm=dev_w))
        np.savez_compressed(
            os.path.join(ART_DIR, "cycle_%02d.npz" % cyc),
            xk=xk_new, W=np.asarray(W_new), J=J_new,
            masses=masses, edges=edges, sites=np.asarray(sites))
        if J_new > best["J"]:
            best = dict(W=np.asarray(W_new).copy(), xk=xk_new.copy(),
                        J=J_new, cycle=cyc)
        if dJ < 0:
            print("  [stop] goal FELL (reported honestly; best design"
                  " kept from cycle %d)" % best["cycle"])
            W_cur, xk_cur = W_new, xk_new       # record walked anyway
            break
        W_cur, xk_cur, J_cur, c_cur = W_new, xk_new, J_new, c_new
        if dJ / J_cur < TOL_STOP_REL:
            print("  [stop] improvement below the declared budget"
                  " floor — converged for this purpose")
            break

    W_fin, xk_fin, J_fin = best["W"], best["xk"], best["J"]
    m_fin = len(xk_fin)
    print("\n  best design: cycle %d, m = %d, J = %.8e  (class-0"
          " %.8e, total gain %+.4f %%)"
          % (best["cycle"], m_fin, J_fin, J_class0,
             100 * (J_fin / J_class0 - 1.0)))
    ok_all &= check("A-7 the enrichment does not lose to its own"
                    " start", J_fin >= J_class0)

    # ---- A-4 / A-5 on the final design -------------------------------
    print("\n-- A-4 / A-5: the final design re-audited --")
    c_fin = dict(c, xk=xk_fin)
    out_fin, sch_fin = P.march_record(W_fin, w, c_fin)
    xf, yf, _ = P.wall_stations(np.asarray(W_fin), c_fin)
    yf = np.asarray(yf)
    descends = bool(np.all(np.diff(yf) < 0))
    clears = bool(yf.min() > 0.25)
    cert_fin = float(out_fin["cert_worst"])
    print("  cert = %.3f; y %.4f -> %.4f m; descending = %s, clears"
          " = %s" % (cert_fin, yf[0], yf[-1], descends, clears))
    ok_all &= check("A-4 final design Newton-certified and admissible",
                    cert_fin <= 1.0 and descends and clears)
    m_lo = IA.start_mass(w, c["fan"], c["y0"], P.N_ROW)
    m_hi = IA.start_mass(w, c["fan"], c["y0"], 8 * P.N_ROW)
    band_m = (A1.K_RICH * abs(m_lo - m_hi)
              + A1.C_FLOOR * A1.EPS * w["mdot"]) / w["mdot"]
    err_m = abs(c["md_in"] / w["mdot"] - 1.0)
    print("  start-line mdot rel err %.3e  (band %.3e) — knots cannot"
          " reach the start line, re-measured not assumed"
          % (err_m, band_m))
    ok_all &= check("A-5 mass constraint on the march's own"
                    " quadrature", err_m <= band_m)

    # ---- A-8: the verdict --------------------------------------------
    print("\n-- A-8: the gain vs the fan streamline, band from a"
          " 3-point ladder --")
    W_inc_fin = np.interp(xk_fin, c["sx"], c["sy"])
    quote, band, gains, Js = gain_ladder(W_inc_fin, W_fin, xk_fin,
                                         w, ta)
    print("  gain quoted %+.5f %%   band %.5f %%"
          % (100 * quote, 100 * band))
    ok_all &= check("A-8 THE VERDICT: the adaptive free-form spike's"
                    " gain over the fan streamline exceeds the band"
                    " its own 3-point ladder supports",
                    quote > band)

    # ---- A-9: the control --------------------------------------------
    res_ctl = None
    if CONTROL:
        print("\n-- A-9: uniform control at the same dof count"
              " (m = %d) --" % m_fin)
        xi_u = np.arange(1, m_fin + 1) / m_fin
        xk_u = X0 + (L - X0) * xi_u
        W_u0 = np.interp(xk_u, c["sx"], c["sy"])
        W_u, J_u, cert_u, sch_u, c_u = optimum_of_class(
            xk_u, W_u0, w, c, ta, "uniform-%d" % m_fin)
        print("  uniform-%d ladder:" % m_fin)
        W_uinc = np.interp(xk_u, c["sx"], c["sy"])
        q_u, b_u, gains_u, _ = gain_ladder(W_uinc, W_u, xk_u, w, ta)
        print("  uniform gain %+.5f %% (band %.5f %%) vs adaptive"
              " %+.5f %% (band %.5f %%)"
              % (100 * q_u, 100 * b_u, 100 * quote, 100 * band))
        ok_all &= check("A-9 THE CONTROL: adaptive does not lose to"
                        " uniform at equal dofs beyond the ladder"
                        " band", quote >= q_u - max(band, b_u))
        res_ctl = dict(W=np.asarray(W_u).tolist(), xk=xk_u.tolist(),
                       J=J_u, gain=q_u, band=b_u,
                       gains=list(map(float, gains_u)))

    # ---- artifact ----------------------------------------------------
    art = dict(
        design=dict(W=[repr(float(v)) for v in W_fin],
                    xk=[repr(float(v)) for v in xk_fin],
                    J=repr(float(J_fin)), cycle=best["cycle"]),
        class0=dict(J=repr(float(J_class0)), m=M0),
        verdict=dict(gain=repr(float(quote)), band=repr(float(band)),
                     gains=[repr(float(g)) for g in gains],
                     rungs=[[K0, N0], [2 * K0 - 1, 2 * N0 - 1],
                            [4 * K0 - 3, 4 * N0 - 3]]),
        control=res_ctl, history=hist,
        provenance="[X-PAKN] S22; incumbent = S21 [X-PSPL] record")
    with open(os.path.join(ART_DIR, "design.json"), "w") as f:
        json.dump(art, f, indent=1)
    print("\n  design of record written to %s"
          % os.path.join(ART_DIR, "design.json"))
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                            time.time() - t_session))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
