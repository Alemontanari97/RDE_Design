"""[X-MGOV] MARGIN GOVERNOR — the F1 A' margin-constrained
formulation: derived KS aggregation of the (G)/Lambda-form validity
field, the G1 finite-negative surrogate, the derived GENO
implementation-magic bands, the [D1]-CONSTRAINED corner metric, and
the decisive-campaign driver (S22, F1 of plan v3; log
validation/PROGRESS_2026-08-11_S22_governor.md).

WHAT THIS IS. The M0 tier-ladder formalization (Part VI, S20 block)
poses the design problem as max J s.t. g = 0 AND margin m(W) >= mu_0
with the margin multiplier KKT grad J = lambda grad g + mu grad m.
This carrier makes that margin EXECUTABLE on the bell tier-0
instance: the traced val field (val_diag replay lanes — every
W-dependent cell of the march), its KS aggregate, and the scipy
NonlinearConstraint entry (run_trsqp margin_factory — a FORMULATION
entry, the policy stack untouched).

DERIVATIONS OF RECORD (R5 — every constant derived or measured, none
tuned; theory classes declared):
 * KS-MIN AGGREGATE [THEOREM-level bounds, standard log-sum-exp]:
     KS_rho(v) = v_min - (1/rho) ln( sum_i exp(-rho (v_i - v_min)) )
   satisfies  v_min - ln(N)/rho <= KS_rho(v) <= v_min  (the min lane
   contributes exp(0) = 1, so the sum is >= 1 and <= N). KS is the
   CONSERVATIVE side (KS <= true min): enforcing KS >= mu_0
   guarantees min val >= mu_0. Shifted form = overflow-free.
 * rho DERIVED: require the conservativeness gap ln(N)/rho to stay
   below the enforcement resolution at the DEEPEST ladder rung:
     rho = K_RICH * ln(N) / mu_0_min,
   N = measured count of real lanes, K_RICH = 4 (registered safety
   constant), mu_0_min = the smallest pre-registered floor.
 * FLOOR LADDER mu_0 DERIVED (pre-registered BEFORE any campaign):
     mu_0_k = m_ref / 2^k,  k = 1..4,
   with m_ref = min val over the baseline W* design-wall-bucket
   lanes (MEASURED healthy reference; the baseline is strictly
   feasible at every rung by construction, k >= 1). Four rungs = the
   minimum giving a three-interval trend for the RT-4 SIGN TEST;
   extrapolation protocol: the multiplier trend over the last two
   rungs is reported as a SIGN statement only (no magnitude claim:
   O1 undischarged => B-STATIONARITY wording, no mu is defined; the
   scipy multiplier is reported as the B-stationarity surrogate
   estimate).
 * G1 SURROGATE [PRACTICE, rejector-gated per the D6 tier-invariant
   clause]: lanes that fail (non-finite states in the plan-fixed
   replay downstream of a march failure) are masked; the margin is
     m = KS_rho(finite lanes) - K_RICH * m_ref * frac_bad - mu_0,
   with KS-part := -K_RICH * m_ref when NO lane survives — finite
   negative at every representable W, continuous at frac_bad = 0
   (exact KS recovered bit-for-bit). Gradient: nonfinite components
   are zeroed AND COUNTED (the same REQ-NONSTALL survive+report
   contract as the S21 f_np/g_np fallback); the counters are
   verdict-bearing in the campaign report.
 * GENO IMPLEMENTATION-MAGIC BANDS (M0 Lambda-form bound (b), the
   F1-entry duty): Lam_FD(dV_pert) = q (alpha(q+dV)-alpha(q-dV))/2dV
   at the GENO step dV_pert = 1.0 and at 0.5 on the baseline q-range
   -> derived band = K_RICH |Lam_FD(1.0) - Lam_FD(0.5)| + 100 eps
   |Lam_AD| per grid point; the cross-check leg (F1b twin) must
   place GENO's Lambda inside this band around our AD Lambda. The
   |den| < 1e-10 GENO fold guard is checked against the measured
   min |den| over the baseline field (statement: can/cannot bite
   in-range). The PM landing window is an F1b consumption, DECLARED
   here, not derived.
 * [D1]-CONSTRAINED CORNER METRIC [COROLLARY of the S20-registered
   constrained-KKT THEOREM; evidence half = this carrier]: at a
   margin-active constrained maximum, the lip component of
   grad J + mu grad m = lambda_e e_lip reads
     dJ/dy_lip + mu dm/dy_lip = lambda_e = corner density (cd),
   so the [D1] metric becomes
     rel_c = |gJ_lip + mu gm_lip - cd| / |cd|,
   reducing bit-for-bit to the unconstrained [D1] at mu = 0.
   VALIDITY CONDITION unchanged (outcome-I only); mu enters as the
   solver multiplier under the B-stationarity qualifier (O1).
   KILL RULE unchanged: rel_c < the S19 baseline 6.6295e-02 at an
   outcome-I margin-constrained optimum supports the design-class
   diagnosis; rel_c >= it falsifies ([C-O33] byproduct).
   DUAL CLAUSE ADDED (repair S1/A37, F-SERVICE 2026-08-13,
   REFUTE_C): rel_c is an identity on the SIGNED value with no dual
   clause of its own; the margin constraint m >= mu_0 is UNILATERAL
   (regime 3, [T-T7CN] taxonomy), so mu carries the required
   direction mu >= 0 + complementarity (mu = 0 at inactive margin) —
   mu_dual_clause, with a seed rejector proven in every stage.
   VERSION CHANGE DECLARED: exit code now also gates the dual-clause
   self-test; no pre-existing row or band was changed.

SURVEY (adopt-or-declare, S22, SOTA search of record in the session
log): KS aggregation for min-type constraint fields under adjoint
gradients = the standard (M0 S20 block). Adaptive-rho lineage
surveyed (Poon-Martins SMO 2007 adaptive KS; interior-point adaptive
aggregation, Comp&Struct 2015; SAKS, ASME JMD 2018): NOT ADOPTED,
with reason — those schemes tune rho to recover accuracy under a
fixed budget when many constraints are active; here rho is DERIVED
to pin the aggregation gap below the enforcement resolution
(ln(N)/rho <= mu_0_min/K_RICH by construction) and the gradients
are exact AD, so the adaptive machinery would add tuning surface
without buying accuracy at N ~ 3e3.

CAMPAIGN (stage "campaign", T4 — max 2 per the F1 budget): the S20
instance (enriched 10-dof class, knots from the regenerated walk),
started at the outcome-II returned certified base, re-optimized
under the margin constraint on the ladder (warm-started
continuation, TIGHTEST rung first — mu_0_1 = m_ref/2 is the largest
floor; MONOTONICITY STOP, derived: activity is monotone in mu_0, so
if the constraint is inactive at the tightest rung it is inactive at
every looser one and the remaining rungs are vacuous — the ladder
stops there with the derivation printed, no silent cap). MANDATORY
LOGS per rung: argmin
val + locus (on-chain vs interior via the [X-LOCD] chain machinery),
ACTIVE-CUSP CENSUS at termination (lanes with val <= mu_0 +
ln(N)/rho, clustered by the stencil radius), multiplier sign
(B-stationarity wording), nonfinite counters. EXIT BRANCHES
(D6 F1, each a valid verdict): margin-active outcome-I (RT-1
consistent-with reading; [D1]-constrained metric measured);
certifiability-limited-under-constraint (bridge falsifier evidence);
interior binding = H2-kill -> tier-1; multi-cusp = H1-kill.

MACHINERY REJECTORS (R5): (R-KS) the KS bounds must hold on the
measured baseline field; (R-GRAD) AD margin gradient vs two-step
Richardson FD directional derivative within the derived band, with
a corrupted-gradient control that must FAIL; (R-G1) a deliberate
beyond-frontier design (gross non-monotone wall) must yield a
FINITE NEGATIVE margin and a finite (zeroed+counted) gradient, and
a short margin-constrained walk must complete without stall/crash;
(R-FD) the magic-band self-check |Lam_FD(1.0) - Lam_AD| <= band
must hold on the grid.

ON-DEMAND CARRIER (env: jax). A1_MGOV_STAGE in {derive, campaign};
"derive" (default) executes every pre-run duty and exits 0/1 —
committed and green BEFORE any decisive campaign (F1 entry gate).
"""
import json
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1        # noqa: E402
import a1_toc_variational_jax as TV    # noqa: E402
import o33_bench as O33                # noqa: E402
import locus_diagnosis as LD           # noqa: E402
from adaptive_knot_optimize import (design_class, march, grad_and_J,
                                    o31_spot)  # noqa: E402

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
HERE = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.environ.get(
    "A1_MGOV_BASE", os.path.join(HERE, "s22_certlim_base.json"))
N_RUNGS = 4
S19_D1_BASELINE = 6.6295e-02          # [X-O33B] R3 corner mismatch


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# traced margin (val field -> masked KS -> G1 surrogate)
# ======================================================================
def make_alpha_lam(state_fn):
    ta = None

    def alpha_of(q):
        c = state_fn(q, ta)[3]
        return jnp.arcsin(jnp.minimum(1.0, c / q))

    dalpha = jax.grad(alpha_of)
    return alpha_of, jax.vmap(lambda q: q * dalpha(q))


def make_margin_fn(tab, cfg, plan, state_fn, solvers, rho, mu0,
                   m_ref, q_ref):
    """Traced W -> margin (G1-surrogate form). q_ref = a measured
    safe speed (baseline field mean) for the double-where guard on
    masked lanes."""
    runv = TV.make_run_toc_scan_jit(tab, cfg, plan, state_fn=state_fn,
                                    solvers=solvers, val_diag=True)
    alpha_of, lam_of = make_alpha_lam(state_fn)

    def margin_W(W):
        _wall, q_l, th_l, act = runv(W)
        q = q_l.reshape(-1)
        th = th_l.reshape(-1)
        a = act.reshape(-1)
        fin = a & jnp.isfinite(q) & jnp.isfinite(th) & (q > 0.0)
        # double-where guard: masked lanes evaluate at the safe
        # reference state so no NaN enters the graph forward
        q_z = jnp.where(fin, q, q_ref)
        th_z = jnp.where(fin, th, 0.0)
        al = jax.vmap(alpha_of)(q_z)
        lam = lam_of(q_z)
        A = jnp.tan(th_z - al)
        B = jnp.tan(al)
        val = (lam * B * (A + B) - (A - B)) / (1.0 + lam * (A + B))
        fin2 = fin & jnp.isfinite(val)
        n_fin = jnp.sum(fin2)
        n_act = jnp.maximum(jnp.sum(a), 1)
        vmin = jnp.min(jnp.where(fin2, val, jnp.inf))
        vmin_s = jnp.where(n_fin > 0, vmin, 0.0)
        e = jnp.where(fin2, jnp.exp(-rho * (jnp.where(fin2, val,
                                                      vmin_s)
                                            - vmin_s)), 0.0)
        ks = vmin_s - jnp.log(jnp.maximum(jnp.sum(e), 1e-300)) / rho
        ks_part = jnp.where(n_fin > 0, ks, -A1.K_RICH * m_ref)
        frac_bad = (n_act - n_fin) / n_act
        return ks_part - A1.K_RICH * m_ref * frac_bad - mu0

    return margin_W


def make_margin_factory(tab, cfg, state_fn, solvers, rho, mu0,
                        m_ref, q_ref, counters):
    """run_trsqp margin_factory: (plan, Dv) -> (m_np, gm_np) with the
    G1 finite-fallback + REQ-NONSTALL counters."""
    def factory(plan, Dv):
        margin_W = make_margin_fn(tab, cfg, plan, state_fn, solvers,
                                  rho, mu0, m_ref, q_ref)
        mval_grad = jax.jit(jax.value_and_grad(margin_W))
        # M2 (S25 ENGINE SPEED): one-slot m+gm memo — scipy requests
        # value and jacobian as separate callbacks at the same u;
        # the memo deletes the duplicated compiled execution,
        # bit-transparently. Counters additive (reporting-only);
        # legacy path via A1_VG_MEMO=0.
        vg_on = os.environ.get("A1_VG_MEMO", "1") != "0"
        slot = dict(key=None, v=None, g=None)
        counters.setdefault("m_exec", 0)
        counters.setdefault("m_dedup", 0)

        def _mvg(u):
            Wb = np.asarray(u) * Dv
            k = Wb.tobytes() if vg_on else None
            if vg_on and slot["key"] == k:
                counters["m_dedup"] += 1
                return slot["v"], slot["g"].copy()
            v, g = mval_grad(jnp.asarray(Wb))
            v = float(v)
            g = np.asarray(g)
            counters["m_exec"] += 1
            if vg_on:
                slot.update(key=k, v=v, g=g.copy())
            return v, g

        def m_np(u):
            v, _ = _mvg(u)
            if not np.isfinite(v):
                counters["m_nonfinite"] += 1
                return -2.0 * A1.K_RICH * m_ref      # G1: always finite
            return v

        def gm_np(u):
            _, g = _mvg(u)
            g = g * Dv
            if not np.all(np.isfinite(g)):
                counters["gm_nonfinite"] += 1
                g = np.where(np.isfinite(g), g, 0.0)
            return g

        return m_np, gm_np

    return factory


# ======================================================================
# derivation stage helpers
# ======================================================================
def baseline_val_stats(tab, cfg, state_fn, solv, W, xi=None):
    """Record + concrete val over the design-wall-bucket lanes."""
    out, plan = march(W, xi, tab, cfg, state_fn, solv)
    with design_class(xi, m=len(W) - 1):
        runv = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn,
                                        solvers=solv, val_diag=True)
        _w, q_l, th_l, act = runv(jnp.asarray(np.asarray(W,
                                                        dtype=float)))
    q = np.asarray(q_l).reshape(-1)
    th = np.asarray(th_l).reshape(-1)
    a = np.asarray(act).reshape(-1)
    alpha_of, lam_of = make_alpha_lam(state_fn)
    fin = a & np.isfinite(q) & (q > 0.0)
    qf, thf = q[fin], th[fin]
    al = np.asarray(jax.vmap(alpha_of)(jnp.asarray(qf)))
    lam = np.asarray(lam_of(jnp.asarray(qf)))
    Aa = np.tan(thf - al)
    Bb = np.tan(al)
    den = 1.0 + lam * (Aa + Bb)
    val = (lam * Bb * (Aa + Bb) - (Aa - Bb)) / den
    good = np.isfinite(val)
    return dict(out=out, plan=plan, N=int(good.sum()),
                q=qf[good], val=val[good], den=den[good],
                m_ref=float(val[good].min()),
                q_ref=float(qf[good].mean()))


def derive(tab, cfg, state_fn, solv, verbose=True):
    """The F1-entry derivations + rejectors. Returns the governor
    parameter dict (or raises via exit code in main)."""
    ok = True
    print("-- D1: baseline W* val field (design-wall bucket) --")
    st = baseline_val_stats(tab, cfg, state_fn, solv, O33.W_STAR)
    ok &= check("baseline certified", st["out"]["cert_worst"] <= 1.0)
    m_ref, N, q_ref = st["m_ref"], st["N"], st["q_ref"]
    print("  N = %d real finite lanes; m_ref = %.6e; median val "
          "%.4e; q range [%.1f, %.1f]"
          % (N, m_ref, float(np.median(st["val"])), st["q"].min(),
             st["q"].max()))
    ok &= check("healthy reference positive (m_ref > 0)", m_ref > 0.0)

    ladder = [m_ref / 2.0**k for k in range(1, N_RUNGS + 1)]
    rho = A1.K_RICH * np.log(N) / ladder[-1]
    gap = np.log(N) / rho
    print("  ladder mu_0 = %s" % ["%.4e" % x for x in ladder])
    print("  rho = K_RICH ln(N)/mu_0_min = %.6e (gap ln(N)/rho = "
          "%.4e = mu_0_min/K_RICH)" % (rho, gap))

    # ---- R-KS: the log-sum-exp bounds on the measured field
    v = st["val"]
    vmin = v.min()
    ks = vmin - np.log(np.sum(np.exp(-rho * (v - vmin)))) / rho
    print("  KS = %.6e vs vmin = %.6e (gap %.3e <= ln(N)/rho %.3e)"
          % (ks, vmin, vmin - ks, np.log(N) / rho))
    ok &= check("R-KS: vmin - ln(N)/rho <= KS <= vmin",
                (vmin - np.log(N) / rho - 1e-15 <= ks) and
                (ks <= vmin + 1e-15))

    # ---- R-GRAD: AD margin gradient vs FD two-step Richardson
    print("-- D2: margin gradient O3.1-style spot (baseline plan) --")
    margin_W = make_margin_fn(tab, cfg, st["plan"], state_fn, solv,
                              rho, ladder[0], m_ref, q_ref)
    mj = jax.jit(margin_W)
    gm = np.asarray(jax.grad(margin_W)(
        jnp.asarray(np.asarray(O33.W_STAR, dtype=float))))
    rng = np.random.default_rng(3)
    dv = rng.standard_normal(len(O33.W_STAR))
    dv /= np.linalg.norm(dv)
    W0j = jnp.asarray(np.asarray(O33.W_STAR, dtype=float))

    def dd(hsc):
        h = EPS ** (1.0 / 3.0) * hsc
        return (float(mj(W0j + h * jnp.asarray(dv)))
                - float(mj(W0j - h * jnp.asarray(dv)))) / (2.0 * h)

    d1, d2 = dd(1.0), dd(0.5)
    lhs = float(gm @ dv)
    tol_g = A1.K_RICH * (abs(d1 - d2)
                         + A1.C_FLOOR * EPS ** (2.0 / 3.0)
                         * max(1.0, abs(float(mj(W0j)))))
    print("  <grad m, v> = %.10e  FD = %.10e  |diff| %.3e (tol %.3e)"
          % (lhs, d2, abs(lhs - d2), tol_g))
    ok &= check("R-GRAD: AD margin gradient inside derived band",
                abs(lhs - d2) <= tol_g)
    ok &= check("R-GRAD control: corrupted gradient rejected",
                abs(float((gm * 1.01 + 1e-3 * np.abs(gm).max()) @ dv)
                    - d2) > tol_g)

    # ---- R-G1: finite negative surrogate at a broken design
    print("-- D3: G1 surrogate at a deliberate beyond-frontier "
          "design --")
    W_bad = np.asarray(O33.W_STAR, dtype=float).copy()
    W_bad[1:-1] = W_bad[1:-1] * np.array(
        [0.55 if i % 2 == 0 else 1.35
         for i in range(len(W_bad) - 2)])       # gross non-monotone
    counters = dict(m_nonfinite=0, gm_nonfinite=0)
    factory = make_margin_factory(tab, cfg, state_fn, solv, rho,
                                  ladder[0], m_ref, q_ref, counters)
    Dv1 = np.ones(len(W_bad))
    m_np, gm_np = factory(st["plan"], Dv1)
    mb = m_np(W_bad)
    gb = gm_np(W_bad)
    print("  m(W_bad) = %.6e (finite %s, negative %s); grad finite "
          "%s; counters %s"
          % (mb, np.isfinite(mb), mb < 0.0,
             bool(np.all(np.isfinite(gb))), counters))
    ok &= check("R-G1a: margin at broken design FINITE", np.isfinite(mb))
    ok &= check("R-G1b: margin at broken design NEGATIVE", mb < 0.0)
    ok &= check("R-G1c: gradient finite (zeroed+counted allowed)",
                bool(np.all(np.isfinite(gb))))
    m_base = m_np(np.asarray(O33.W_STAR, dtype=float))
    ok &= check("G1 control: baseline margin POSITIVE at rung 1 "
                "(m = %.4e)" % m_base, m_base > 0.0)

    # ---- R-G1d: RECOVERED SQP STEP (the tier-invariant clause's
    # operative half): a SHORT margin-constrained walk from the
    # baseline must complete without stall/crash — the optimizer
    # steps THROUGH constraint evaluations (any returned outcome
    # counts; a raise/hang is the FAIL).
    print("-- D3b: G1 recovery — short margin-constrained walk --")
    yL = cfg["yt"] * np.sqrt(TV.TCASE["eps"])
    t0 = time.perf_counter()
    try:
        opt_s = TV.run_trsqp(np.asarray(O33.W_STAR, dtype=float),
                             tab, cfg, yL, gtol=1e-1, xtol=1e-10,
                             max_segments=2, maxiter_per_seg=4,
                             state_fn=state_fn, solvers=solv,
                             verbose=0, margin_factory=factory)
        print("  short walk: %d segments, nit %d, %d evals, %.0f s, "
              "cert_lim %s (counters %s)"
              % (opt_s["n_segments"], opt_s["nit_total"],
                 opt_s["n_eval"], time.perf_counter() - t0,
                 bool(opt_s.get("certifiability_limited")), counters))
        ok &= check("R-G1d: margin-constrained walk completes with "
                    "steps taken (recovered SQP stepping)",
                    opt_s["n_eval"] > 0)
    except RuntimeError as err:
        print("  short walk RAISED: %s" % err)
        ok &= check("R-G1d: margin-constrained walk completes "
                    "(stall/crash = FAIL)", False)

    # ---- R-FD: GENO magic bands (bound (b) duty)
    print("-- D4: GENO implementation-magic bands (dV_pert; "
          "den-guard) --")
    alpha_of, lam_of = make_alpha_lam(state_fn)
    qs = np.linspace(st["q"].min(), st["q"].max(), 24)

    def lam_fd(q, dv):
        return q * (float(alpha_of(jnp.float64(q + dv)))
                    - float(alpha_of(jnp.float64(q - dv)))) / (2 * dv)

    lam_ad = np.asarray(lam_of(jnp.asarray(qs)))
    fd10 = np.array([lam_fd(q, 1.0) for q in qs])
    fd05 = np.array([lam_fd(q, 0.5) for q in qs])
    band = A1.K_RICH * np.abs(fd10 - fd05) + 100 * EPS * np.abs(lam_ad)
    worst = np.max(np.abs(fd10 - lam_ad) / band)
    print("  max |Lam_FD(1.0) - Lam_AD| / band = %.3f  (band range "
          "[%.2e, %.2e])" % (worst, band.min(), band.max()))
    ok &= check("R-FD: GENO dV_pert=1.0 FD Lambda inside the derived "
                "band around AD (the F1b cross-check leg band)",
                worst <= 1.0)
    dmin = float(np.min(np.abs(st["den"])))
    print("  min |den| over baseline field = %.4e vs GENO guard "
          "1e-10 -> the guard %s bite in-range"
          % (dmin, "CANNOT" if dmin > 1e-10 else "CAN"))
    print("  (PM landing window: F1b consumption, DECLARED — not "
          "derivable from this repo's own quantities)")

    return dict(ok=ok, m_ref=m_ref, q_ref=q_ref, N=N, rho=float(rho),
                ladder=ladder, st=st)


# ======================================================================
# [D1]-constrained corner metric (corollary; evidence half)
# ======================================================================
def d1_constrained(gJ, gm, mu, cd):
    """rel_c = |gJ_lip + mu gm_lip - cd| / |cd| (reduces to the
    unconstrained [D1] metric at mu = 0). LEXICON OF RECORD
    (REFUTE_C, F-SERVICE 2026-08-13): this is an identity on the
    SIGNED value — the modulus is of the DIFFERENCE — and it carries
    NO dual clause by itself; the dual half lives in mu_dual_clause
    (repair S1/A37 extension to this carrier)."""
    return abs(gJ[-1] + mu * gm[-1] - cd) / abs(cd)


def mu_dual_clause(mu, margin_active, slack=None):
    """Repair S1/A37 extension (F-SERVICE 2026-08-13, REFUTE_C): the
    margin constraint m >= mu_0 is UNILATERAL — its multiplier is
    regime-3 in the [T-T7CN] cone taxonomy and carries a REQUIRED
    direction, mu >= 0 (under the B-stationarity qualifier until O1),
    plus complementarity: mu = 0 identically at an inactive margin.
    Returns (ok, msg); a wrong-side mu at an active margin must FIRE."""
    if not margin_active:
        ok = bool(mu == 0.0)
        return ok, ("mu = %.4e at INACTIVE margin: complementarity "
                    "requires mu = 0 -> %s"
                    % (mu, "ok" if ok else "VIOLATED"))
    ok = bool(mu >= 0.0)
    comp = abs(mu * (0.0 if slack is None else slack))
    return ok, ("mu = %+.4e at ACTIVE margin (unilateral, regime 3): "
                "required mu >= 0 -> %s; |mu x slack| = %.3e "
                "[B-stationarity qualifier until O1]"
                % (mu, "dual-FEASIBLE" if ok else "dual-INFEASIBLE",
                   comp))


# ======================================================================
# campaign (T4) — margin-constrained re-optimization on the ladder
# ======================================================================
def active_cusp_census(val, pts, mu0, gap, nodes, r_loc):
    """Active set = lanes with val <= mu0 + gap; clustered by the
    stencil radius against the control-surface chain; returns
    (n_active, n_on_chain, n_interior, n_clusters)."""
    act = val <= mu0 + gap
    if not act.any():
        return 0, 0, 0, 0
    P = pts[act]
    on = 0
    for p in P:
        d, r, _ = LD.dist_to_chain(p, nodes, r_loc)
        on += int(d <= r)
    # spatial clustering by chain-local radius (greedy)
    used = np.zeros(len(P), dtype=bool)
    ncl = 0
    for i in range(len(P)):
        if used[i]:
            continue
        ncl += 1
        _, r_i, _ = LD.dist_to_chain(P[i], nodes, r_loc)
        dd = np.linalg.norm(P - P[i][None, :], axis=1)
        used |= dd <= r_i
    return int(act.sum()), on, int(act.sum()) - on, ncl


def campaign(gov, tab, cfg, state_fn, solv):
    """One decisive A' campaign: ladder continuation from the
    outcome-II certified base. Every branch is a verdict."""
    ok = True
    if not os.path.exists(BASE_PATH):
        print("FATAL: no certified-base artifact at %s" % BASE_PATH)
        return False, dict(outcome="blocked-no-base")
    base = json.load(open(BASE_PATH))
    W_cur = np.array([float(x) for x in base["W"]])
    xi = np.array([float(x) for x in base["xi"]])
    print("-- campaign: start = outcome-II certified base (m = %d "
          "dofs) --" % (len(W_cur) - 1))
    m_ref, q_ref, rho = gov["m_ref"], gov["q_ref"], gov["rho"]
    counters = dict(m_nonfinite=0, gm_nonfinite=0)
    yL = cfg["yt"] * np.sqrt(TV.TCASE["eps"])
    gap = np.log(gov["N"]) / rho
    results = []
    # H3 (S25-bis, campaign rung-boundary dedup): the rung-end O4
    # march of rung k IS the rung-start march of rung k+1 (same W,
    # same engine objects/class in scope — bitwise-keyed reuse); the
    # walk consumes the rung-start record as preplan (seg-0 dup
    # killed, gated by the M1 first-hit controls) and returns its
    # last certified field-record for the rung-end O4 logs. 3
    # records/rung where 1 suffices -> 1.
    rec_carry = None                     # (W, out, plan)
    for k, mu0 in enumerate(gov["ladder"], start=1):
        print("-- rung %d/%d: mu_0 = %.6e --" % (k, N_RUNGS, mu0))
        if (rec_carry is not None
                and np.array_equal(np.asarray(rec_carry[0]), W_cur)):
            out_w, plan_w = rec_carry[1], rec_carry[2]
            print("  [rung %d H3] start record = carried rung-end "
                  "record (bitwise key match, march deduped)" % k)
        else:
            out_w, plan_w = march(W_cur, xi, tab, cfg, state_fn, solv)
        rec_carry = None
        if out_w["cert_worst"] > 1.0:
            print("  [rung %d] start design not certified (worst "
                  "%.3e) — declared, campaign stops here" %
                  (k, out_w["cert_worst"]))
            break
        J_w, g_w, scalJ_w = grad_and_J(W_cur, xi, tab, cfg, plan_w,
                                       state_fn, solv)
        dp, tol_dp = o31_spot(W_cur, xi, scalJ_w, g_w, J_w)
        ok &= check("rung %d O3.1 at start" % k, dp <= tol_dp)
        gtol = max(tol_dp, 1e-8 * float(np.linalg.norm(g_w)))
        factory = make_margin_factory(tab, cfg, state_fn, solv, rho,
                                      mu0, m_ref, q_ref, counters)
        t0 = time.perf_counter()
        try:
            with design_class(xi):
                opt = TV.run_trsqp(W_cur, tab, cfg, yL, gtol=gtol,
                                   xtol=1e-10, state_fn=state_fn,
                                   solvers=solv, verbose=0,
                                   margin_factory=factory,
                                   preplan=(out_w, plan_w),
                                   field_records=True)
        except RuntimeError as err:
            print("  [rung %d] walk gate failure of record: %s — a "
                  "REQ-NONSTALL breach IS a G1 rejector firing; "
                  "campaign stops, branch adjudicated below"
                  % (k, err))
            results.append(dict(rung=k, mu0=mu0, outcome="raise",
                                error=str(err)))
            ok = False
            break
        dt = time.perf_counter() - t0
        res = opt["res"]
        cert_lim = bool(opt.get("certifiability_limited"))
        W_new = np.asarray(opt["W"], dtype=float)
        print("  [rung %d] %.0f s, segments %d, nit %d, status %s, "
              "KKT %.3e (gtol %.3e), cert_lim %s, nf-counters "
              "obj/grad %d/%d margin m/gm %d/%d"
              % (k, dt, opt["n_segments"], opt["nit_total"],
                 getattr(res, "status", None),
                 float(getattr(res, "optimality", np.nan)), gtol,
                 cert_lim, opt["n_nonfinite_obj"],
                 opt["n_nonfinite_grad"], counters["m_nonfinite"],
                 counters["gm_nonfinite"]))
        # mandatory O4 logs on the returned design
        lc = opt.get("last_cert")
        if (lc is not None
                and np.array_equal(np.asarray(lc["W"]), W_new)
                and "cols" in lc["out"]):
            # H3: the walk's last certified field-record IS the
            # record of W_new
            out_n, plan_n = lc["out"], lc["plan"]
            print("  [rung %d H3] O4 march deduped (walk last_cert "
                  "bitwise match)" % k)
        else:
            out_n, plan_n = march(W_new, xi, tab, cfg, state_fn, solv)
        stats = baseline_val_stats(tab, cfg, state_fn, solv, W_new,
                                   xi=xi)
        with design_class(xi):
            nodes, r_loc = LD.chain_geometry(
                out_n["cols"], out_n["n_fan"], out_n["n_arc"])
        pts_f, val_f, _ = LD.field_val(
            out_n["cols"], out_n["n_fan"] + out_n["n_arc"],
            state_fn, LD.make_lambda_fn(state_fn))
        i_min = int(np.argmin(val_f))
        d_min, r_min, _ = LD.dist_to_chain(pts_f[i_min], nodes, r_loc)
        n_act, n_on, n_int, n_cl = active_cusp_census(
            val_f, pts_f, mu0, gap, nodes, r_loc)
        m_final = stats["m_ref"]        # min val of the NEW design
        margin_active = m_final <= mu0 + gap
        print("  [rung %d] O4 log: min val %.6e at (%.4f, %.4f), "
              "d(argmin,chain) %.3e vs r_st %.3e (%s); active census: "
              "%d lanes (%d on-chain, %d interior, %d clusters); "
              "margin %s"
              % (k, m_final, pts_f[i_min][0], pts_f[i_min][1],
                 d_min, r_min,
                 "ON-CHAIN" if d_min <= r_min else "interior",
                 n_act, n_on, n_int, n_cl,
                 "ACTIVE" if margin_active else "inactive"))
        # multiplier (B-stationarity qualifier — O1 undischarged)
        mu_est = None
        try:
            vlist = [np.atleast_1d(np.asarray(vv)).ravel()
                     for vv in res.v]
            mu_est = float(vlist[-1][0]) if len(vlist) > 1 else None
        except Exception:
            pass
        print("  [rung %d] multiplier (B-STATIONARITY estimate, no "
              "mu defined until O1): %s" % (k, mu_est))
        # [D1]-constrained metric on outcome-I only
        rel_c = None
        if (not cert_lim and getattr(res, "status", 0) in (1, 2)
                and float(res.optimality) <= 10.0 * gtol):
            J_n, g_n, _sj = grad_and_J(W_new, xi, tab, cfg, plan_n,
                                       state_fn, solv)
            mfn = make_margin_fn(tab, cfg, plan_n, state_fn, solv,
                                 rho, mu0, m_ref, q_ref)
            gmv = np.asarray(jax.grad(mfn)(jnp.asarray(W_new)))
            cd, _ = O33.corner_density(
                np.asarray(out_n["wall"][-1]), state_fn)
            mu_use = (mu_est if (mu_est is not None
                                 and margin_active) else 0.0)
            rel_c = d1_constrained(g_n, gmv, mu_use, cd)
            print("  [rung %d] [D1]-constrained corner metric rel_c "
                  "= %.4e (S19 baseline %.4e; mu_use %.4e, "
                  "B-stationarity wording)"
                  % (k, rel_c, S19_D1_BASELINE, mu_use))
            dok, dmsg = mu_dual_clause(mu_use, bool(margin_active),
                                       slack=0.0)
            print("  [rung %d] dual clause (repair S1/A37): %s"
                  % (k, dmsg))
            ok &= dok
        results.append(dict(
            rung=k, mu0=mu0, J=float(-res.fun) if res else None,
            kkt=float(getattr(res, "optimality", np.nan)),
            cert_lim=cert_lim, margin_active=bool(margin_active),
            min_val=m_final, argmin_on_chain=bool(d_min <= r_min),
            census=(n_act, n_on, n_int, n_cl), mu_est=mu_est,
            rel_c=rel_c, outcome=(
                "outcome-II" if cert_lim else
                ("outcome-I" if getattr(res, "status", 0) in (1, 2)
                 else "open"))))
        W_cur = W_new
        rec_carry = (W_new, out_n, plan_n)   # H3: next rung's start
        if not margin_active:
            print("  [ladder] MONOTONICITY STOP (derived, declared): "
                  "the constraint is INACTIVE at the tightest rung "
                  "mu_0_%d = %.4e (min val %.4e >> mu_0 + gap); "
                  "activity is monotone in mu_0, so every looser "
                  "rung is vacuous — remaining rungs not run, "
                  "mu = 0 identically on the ladder (B-stationarity "
                  "reduces to the unconstrained KKT; the RT-4 sign "
                  "statement is trivially mu = 0)." % (k, mu0,
                                                       m_final))
            break
    # ---------------- branch adjudication (D6 F1 exit) --------------
    print("-- BRANCH ADJUDICATION (D6 F1; every branch a valid "
          "exit) --")
    return ok, dict(results=results, counters=counters)


def main():
    stage = os.environ.get("A1_MGOV_STAGE", "derive")
    print("== [X-MGOV] margin governor (JAX %s; stage %s) =="
          % (jax.__version__, stage))
    tab = A1.prep_tab(A1.build_tab_nasa())
    state_c1, solv, cfg = O33.make_case(tab)
    gov = derive(tab, cfg, state_c1, solv)
    ok = gov.pop("ok")
    # repair S1/A37 self-test (F-SERVICE 2026-08-13, REFUTE_C): the
    # dual clause on mu must accept the right side and FIRE on the
    # wrong one — pure float logic, runs in every stage.
    d_ok1, _ = mu_dual_clause(+1.0, True, slack=0.0)
    d_ok2, _ = mu_dual_clause(-1.0, True, slack=0.0)
    d_ok3, _ = mu_dual_clause(0.0, False)
    print("  [S1/A37 dual clause] positive control %s; seed rejector "
          "(wrong-side mu at active margin) %s; complementarity at "
          "inactive margin %s"
          % ("PASS" if d_ok1 else "FAIL",
             "FIRES" if not d_ok2 else "FAILS-TO-FIRE",
             "PASS" if d_ok3 else "FAIL"))
    ok &= d_ok1 and (not d_ok2) and d_ok3
    if stage == "campaign" and ok:
        ok2, rep = campaign(gov, tab, cfg, state_c1, solv)
        ok &= ok2
        print("  campaign report: %s" % json.dumps(
            rep["results"], default=str))
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
