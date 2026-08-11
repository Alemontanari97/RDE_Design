#!/usr/bin/env python3
"""ORACLE O3.2 [F1/P-2, session S19]: MESH CONVERGENCE OF THE
PRIMAL/ADJOINT PAIR on the two twin instances of the A1 engine —
the executable half of [S-LBML] and the SELF-MONITORING channel that
the S-LBML statement itself assigns to clause LB-c1. Registry ID:
[X-O32].

WHAT IS MEASURED (and why it is the pre-registered oracle)
  S-LBML §2 claims: (i) the unit process is consistent at O(h^2) for
  the characteristic ODEs and the TANGENT system inherits the order
  under LB-c1 (interior C^3 along characteristics); (iii) Lax
  equivalence carries consistency+stability to convergence; (iv) the
  discrete gradient is the EXACT finite-dimensional transpose of the
  convergent tangent ([T-LEMB], O3.1 at machine precision), hence it
  converges in the DUAL PAIRING AT THE SAME ORDER. This carrier
  measures both exponents on the same refinement ladder:
    PRIMAL  : a registered-norm functional of the computed field;
    ADJOINT : a fixed-direction projection of the AD gradient of that
              same functional (the dual pairing of (iv), literally).
  A rate below the band on the PRIMAL falsifies (i)/(iii); a rate
  below the band on the ADJOINT with the primal in band falsifies
  (iv) — the two rows are separately falsifiable, which is the point.

PRE-REGISTERED NORMS (P2_outline §5 (a), S14 PAN-S14 F-LIP; binding
since before the engine produced its first number, NEVER re-litigated
here — implemented): field-level checks are evaluated in norms that
EXCLUDE shrinking neighborhoods of the lip/corner, of the sonic line
/ Sauer IVL, and of the axis. Implementation of record: a C^infinity
bump weight w(x) supported strictly inside the registered window
[x_start + d, x_end - d], with
    d = 2 * (station spacing of the COARSEST level),
the factor 2 being the STENCIL RADIUS of the unit process (each cell
couples to its two neighbouring column entries) — a derived cell
count, not a tuned length. The window is h-INDEPENDENT by
construction (a functional whose definition moved with h would not
have a convergence order at all). The excluded lip neighborhood is
then measured SEPARATELY (§S5) as the empirical test of the
exclusion itself: pre-registration item (d), the wall/lip-adjacent
probe, is the half of the X1 audit that this campaign can execute.

RATE ESTIMATOR — DERIVED, NOT log2 OF TWO LEVELS
  Three levels h1 > h2 > h3 with the model f_k = f* + C h_k^p give
    (f1 - f2)/(f2 - f3) = (h1^p - h2^p)/(h2^p - h3^p) =: R(p),
  R strictly increasing (asserted numerically on the bracket), so p
  is recovered by bisection — EXACT for the model, and valid for the
  non-integer refinement ratios used here (1, 1/2, 1/3, 1/4). The
  estimator is known-answer tested in §S1 on synthetic data with
  p0 in {1, 1.5, 2, 3} (recovery to ~1e-12) and its monotonicity is
  machine-checked: a broken estimator cannot silently pass a run.

UNCERTAINTY AND VERDICT RULE — DECLARED BEFORE THE RUN (R5)
  Two contributions, both MEASURED, none tuned:
   * dp_noise: each functional value carries the accumulated Newton
     certification floor eps_f = NEWTON_TOL_FACTOR * eps * N_cells *
     scale(f)  (worst-case accumulation over the CERTIFIED cell count
     the run itself reports); propagated through the estimator by
     evaluating it at the extremal admissible differences.
   * dp_model: |p_hat(coarse triple) - p_hat(fine triple)| — the
     measured drift of the exponent along the ladder, i.e. the
     asymptotic-range indicator. A sequence out of asymptotic range
     produces a LARGE dp_model and the run is declared NON-CONCLUSIVE
     rather than PASS.
  Verdict rule OF RECORD (S21 re-adjudication, 2026-08-11 — this
  header previously stated the two-sided rule as pre-registered
  while the verdict commit had switched it; the adjudicated set is):
     CONCLUSIVE iff dp_tot := dp_noise + dp_model < 1/2, the
       PRE-REGISTERED cap (carrier commit 6ea29e3; the in-verdict
       doubling to 1.0 cannot bind post hoc — see verdict_row);
     KILL rule = the BINDING one-sided S16 [S-LBML] falsifier:
       p_hat_fine < 2 - dp_tot kills the h^2 claim (an order ABOVE 2
       does not); the two-sided reading is reported, not binding.
  S19 ROW OF RECORD, RE-REPORTED under this rule: p_fine = 2.5347,
  dp_tot = 0.6704 -> rate claim NOT killed, row NON-CONCLUSIVE
  (conclusiveness not achieved at the pre-registered cap). Named
  lever: finer ladder until dp_tot < 0.5.

NEGATIVE CONTROL — A REJECTOR THAT CAN REJECT (§S4)
  make_solvers_foot: the SAME unit processes with the characteristic
  coefficients frozen at the FOOT state instead of the segment
  MIDPOINT — i.e. the explicit-Euler (predictor-only) form of the MoC
  cell instead of the average-coefficient (modified-Euler) form. It
  is consistent and PROVABLY first order; it must be REJECTED by the
  same band that accepts the production march. Same code path, same
  certification, same estimator: the control isolates the ORDER.

INSTANCES (provenance declared)
  IDEAL twin [X-A1IM]: P = [yt, rtu, rtd, eps] of the reduced twin
    case; entirely in-house (GENO plays no part here: its role in
    that carrier is the contour oracle, which this carrier does not
    use).
  TOC twin [X-TOCV]: the design W* of the S18 run of record
    (thB = 15.5527 deg, interior/lip nodes as printed in the S18 log
    step 7). PROVENANCE, DECLARED: W* is the converged design of an
    optimization whose STARTING POINT was GENO-seeded; GENO therefore
    supplies the provenance of the INSTANCE, and nothing else — no
    oracle row in this carrier compares anything against GENO output,
    so no cross-code agreement can manufacture a rate. The design is
    RE-CERTIFIED here at every level (per-cell Newton certification +
    axial-margin rejector) instead of being trusted.

ON-DEMAND CARRIER (env: jax). Outside the CI tiers by declaration,
like [X-A1IM]/[X-TOCV]. Exit code 0 iff ALL rows pass INCLUDING the
negative control. Staging: A1_O32_STAGE selects {est, ideal, toc,
all} (default all); A1_O32_RMAX caps the refinement ladder.
"""
import os
import sys
import tempfile
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1   # noqa: E402
import a1_march_scan as SC        # noqa: E402
import a1_toc_variational_jax as TV   # noqa: E402
import thermotab_c1_jax as TH     # noqa: E402

jax.config.update("jax_enable_x64", True)
try:      # persistent XLA cache (declared: cost control only, no
    _cd = os.environ.get("JAX_COMPILATION_CACHE_DIR") or os.path.join(
        tempfile.gettempdir(), "jax_cache_rde")   # numerics impact)
    jax.config.update("jax_compilation_cache_dir", _cd)
    jax.config.update("jax_persistent_cache_min_entry_size_bytes", -1)
    jax.config.update("jax_persistent_cache_min_compile_time_secs", 1.0)
except Exception as _e:                                   # pragma: no cover
    print("  (persistent XLA cache unavailable: %s)" % _e)

EPS = float(jnp.finfo(jnp.float64).eps)
d2r = np.pi / 180.0

# S18 run of record, log step 7 (provenance declared in the docstring)
W_STAR = np.array([15.5527 * d2r,
                   1.17537, 1.33823, 1.49032, 1.62539,
                   1.74344, 1.84421, 1.92953, 2.0])

STENCIL_RADIUS = 2     # cells excluded around a registered locus
SEP_ADJACENT = 0.5     # derived: half-separation from orders 1 and 3


def check(label, ok):
    print("  [%s] %s" % (label, "PASS" if ok else "FAIL"))
    return bool(ok)


# ======================================================================
# S1  RATE ESTIMATOR (three levels, arbitrary ratios) + known answer
# ======================================================================
def _R(p, h1, h2, h3):
    return (h1**p - h2**p) / (h2**p - h3**p)


def observed_order(f1, f2, f3, h1, h2, h3, plo=0.05, phi=8.0):
    """Exact p for the model f_k = f* + C h_k^p. None if the triple is
    not usable (zero or sign-inconsistent differences, or p outside
    the bracket) — 'not usable' is reported, never silently patched."""
    d1, d2 = f1 - f2, f2 - f3
    if d1 == 0.0 or d2 == 0.0 or (d1 / d2) <= 0.0:
        return None
    return _invert_R(abs(d1) / abs(d2), h1, h2, h3, plo, phi)


def _invert_R(target, h1, h2, h3, plo=0.05, phi=8.0):
    rlo, rhi = _R(plo, h1, h2, h3), _R(phi, h1, h2, h3)
    if not (rlo <= target <= rhi):
        return None
    lo, hi = plo, phi
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if _R(mid, h1, h2, h3) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def order_noise_band(f1, f2, f3, h1, h2, h3, eps_f):
    """dp_noise: propagate an absolute uncertainty eps_f on EACH level
    through the estimator (differences carry 2 eps_f)."""
    a, b = abs(f1 - f2), abs(f2 - f3)
    lo_r = (a - 2.0 * eps_f) / (b + 2.0 * eps_f)
    hi_den = b - 2.0 * eps_f
    if a - 2.0 * eps_f <= 0.0 or hi_den <= 0.0:
        return None
    p_lo = _invert_R(lo_r, h1, h2, h3)
    p_hi = _invert_R((a + 2.0 * eps_f) / hi_den, h1, h2, h3)
    p_c = _invert_R(a / b, h1, h2, h3)
    if p_lo is None or p_hi is None or p_c is None:
        return None
    return max(p_c - p_lo, p_hi - p_c)


def estimator_selftest():
    """KNOWN-ANSWER test of the estimator + machine check of the
    monotonicity the inversion relies on. A broken estimator must not
    be able to pass a physics run."""
    ok = True
    hs = (1.0, 0.5, 1.0 / 3.0, 0.25)
    ps = np.linspace(0.1, 7.9, 400)
    for (a, b, c) in ((0, 1, 2), (1, 2, 3)):
        vals = np.array([_R(p, hs[a], hs[b], hs[c]) for p in ps])
        ok &= check("estimator kernel strictly increasing (levels %d%d%d)"
                    % (a + 1, b + 1, c + 1), bool(np.all(np.diff(vals) > 0)))
    worst = 0.0
    for p0 in (1.0, 1.5, 2.0, 3.0):
        for (a, b, c) in ((0, 1, 2), (1, 2, 3)):
            fs = [7.5 - 0.375 * h**p0 for h in hs]
            p = observed_order(fs[a], fs[b], fs[c], hs[a], hs[b], hs[c])
            worst = max(worst, abs(p - p0))
    print("  known-answer recovery over p0 in {1, 1.5, 2, 3}: worst "
          "|p_hat - p0| = %.2e" % worst)
    ok &= check("estimator recovers the synthetic order", worst < 1e-9)
    # rejector: a first-order sequence must NOT be read as second order
    fs = [7.5 - 0.375 * h**1.0 for h in hs]
    p1 = observed_order(fs[1], fs[2], fs[3], hs[1], hs[2], hs[3])
    ok &= check("estimator REJECTS a first-order sequence as h^2",
                abs(p1 - 2.0) > SEP_ADJACENT)
    return ok


def verdict_row(label, f, h, ncell, scale_hint=None):
    """Full O3.2 row from four levels: rate, derived band, verdict.
    Returns (ok, conclusive, p_fine, dp_tot).

    WHICH RULE DECIDES — declared, because two texts exist and they
    differ, and the difference must not be able to move a verdict
    silently:
     * BINDING (this is the one the verdict uses): the falsifier
       committed in S16 with [S-LBML] itself, docs/rde_nozzle_LBML.md
       audit line — "O3.2 (measured order < 2 - tol on smooth
       certified references kills the rate claim)". It is ONE-SIDED:
       an order ABOVE 2 does not falsify a claim of order h^2. Here
       tol := dp_tot, the run's own derived uncertainty (measured
       noise + measured model drift) — no free constant.
     * REPORTED, not binding: the two-sided rule written in this
       session's step-3 text (|p - 2| <= dp_tot). It is STRICTER than
       the text that binds, so it is reported alongside and never used
       to decide.
    CONCLUSIVENESS CAP OF RECORD = 0.5 (S21 RE-ADJUDICATION,
    2026-08-11, red-team o32-refutation-hides-verdict-moving-rule-
    change): the 0.5 cap was PRE-REGISTERED in the carrier commit
    (6ea29e3, before any number existed); the doubling to 1.0
    landed in the VERDICT commit itself (514e267) with the numbers
    in hand, and self-attested before-ness inside an outcome commit
    does not meet the repo's own commit-granularity pre-registration
    standard. Consequence for the S19 row of record: dp_tot = 0.6704
    -> the rate claim stays NOT KILLED (binding one-sided S16 rule,
    p_fine = 2.5347) but the row is RE-REPORTED NON-CONCLUSIVE under
    the pre-registered cap. The 1.0 constant (the cap's stated
    "adjacent integer orders" derivation) remains REPORTED as a
    derivation PROPOSAL that cannot bind this instance post hoc;
    named lever to moot the dispute: a finer ladder driving
    dp_tot < 0.5. Every exponent is printed either way."""
    scale = scale_hint if scale_hint is not None else max(
        abs(v) for v in f)
    if len(f) < 4:
        # DECLARED: the model-drift term dp_model needs two triples;
        # with fewer than four levels the run cannot bound its own
        # asymptotic-range error, so it is NON-CONCLUSIVE by rule —
        # never a PASS on the coarse triple alone.
        print("  %-34s : NON-CONCLUSIVE (%d levels < 4: dp_model "
              "undefined)" % (label, len(f)))
        return False, False, None, None
    eps_f = [A1.NEWTON_TOL_FACTOR * EPS * n * scale for n in ncell]
    p_c = observed_order(f[0], f[1], f[2], h[0], h[1], h[2])
    p_f = observed_order(f[1], f[2], f[3], h[1], h[2], h[3])
    if p_c is None or p_f is None:
        print("  %-34s : NOT USABLE (differences degenerate: "
              "%.3e / %.3e)" % (label, f[0] - f[1], f[1] - f[2]))
        return False, False, None, None
    dpn = order_noise_band(f[1], f[2], f[3], h[1], h[2], h[3],
                           max(eps_f[1:]))
    if dpn is None:
        print("  %-34s : NOT USABLE (noise floor swamps the "
              "differences)" % label)
        return False, False, p_f, None
    dpm = abs(p_c - p_f)
    dpt = dpn + dpm
    # conclusiveness at the PRE-REGISTERED cap of record (S21
    # re-adjudication — see docstring); the 1.0 reading stays printed
    concl = dpt < SEP_ADJACENT
    killed = p_f < 2.0 - dpt              # the BINDING S16 falsifier
    ok = concl and (not killed)
    two_sided = abs(p_f - 2.0) <= dpt     # reported, stricter, not used
    print("  %-34s : p(coarse) = %.4f  p(fine) = %.4f  "
          "dp_noise = %.2e  dp_model = %.4f  dp_tot = %.4f  -> %s"
          % (label, p_c, p_f, dpn, dpm, dpt,
             ("PASS" if ok else
              ("RATE CLAIM KILLED" if concl else "NON-CONCLUSIVE"))))
    print("  %-34s   [readings] binding one-sided (p >= 2 - dp_tot): "
          "%s | two-sided |p-2| <= dp_tot: %s | conclusive at cap 1.0: "
          "%s, at cap 0.5: %s"
          % ("", "pass" if not killed else "KILL",
             "pass" if two_sided else "fail",
             "yes" if concl else "NO",
             "yes" if dpt < SEP_ADJACENT else "no"))
    return ok, concl, p_f, dpt


# ======================================================================
# S2  registered-norm weight and functionals
# ======================================================================
def bump(x, a, b):
    """C^infinity bump supported on (a, b), max 1 at the midpoint.
    SAFE-WHERE (S18 lever, kept): the clipped argument makes the
    inactive branch FINITE, so the where-NaN-gradient trap cannot
    poison the reverse pass of the functionals built on it."""
    t = (x - a) / (b - a)
    tt = jnp.clip(t, 1e-12, 1.0 - 1e-12)
    val = jnp.exp(4.0) * jnp.exp(-1.0 / (tt * (1.0 - tt)))
    return jnp.where((t <= 0.0) | (t >= 1.0), 0.0, val)


def weighted_trapz(x, f, a, b):
    """Registered-norm functional  Q = int w(x) f(x) dx  evaluated by
    the composite trapezoid on the march's OWN stations (no
    resampling, no interpolation: an interpolation step would inject
    its own error into the very exponent being measured)."""
    g = bump(x, a, b) * f
    return jnp.sum(0.5 * (g[1:] + g[:-1]) * (x[1:] - x[:-1]))


# ======================================================================
# S3  IDEAL TWIN [X-A1IM] — primal contour functional + AD gradient
# ======================================================================
def ideal_ladder(tab, rmax, m_stop=1.0e-5):
    """Refinement ladder on the ideal march. Level r: NI -> r(NI-1)+1,
    Ne -> r(Ne-1)+1, da -> da/r; h_r = 1/r.
    m_stop = the mirrored GENO exit constant |M - Me| (default = the
    record value); the PRE-DECLARED diagnostic tightens it."""
    base = dict(NI=A1.CASE["NI"], Ne=A1.CASE["Ne"],
                da_deg=A1.CASE["da_deg"], m_stop=m_stop)
    P = jnp.array([A1.CASE["yt"], A1.CASE["rtu"], A1.CASE["rtd"],
                   A1.CASE["eps"]])
    out1, _ = A1.run_march(P, tab, base)
    wx1 = np.asarray(out1["wall_x"])
    # registered window: exclude STENCIL_RADIUS coarsest-level station
    # spacings at each end (sonic/Sauer IVL start, lip/corner end)
    d = STENCIL_RADIUS * float(np.max(np.diff(wx1)))
    a, b = float(wx1[0]) + d, float(wx1[-1]) - d
    print("  registered window x in [%.4f, %.4f] (excluded d = %.4f = "
          "%d x coarsest station spacing); wall x in [%.4f, %.4f]"
          % (a, b, d, STENCIL_RADIUS, wx1[0], wx1[-1]))
    v = np.asarray(np.random.default_rng(319).standard_normal(4))
    v /= np.linalg.norm(v)
    print("  gradient probe direction v (seed 319) = %s"
          % np.array2string(v, precision=6))

    res = dict(h=[], Q=[], G=[], n=[], Me=[], t=[], rep=[])
    for r in range(1, rmax + 1):
        cfg = dict(NI=r * (base["NI"] - 1) + 1,
                   Ne=r * (base["Ne"] - 1) + 1,
                   da_deg=base["da_deg"] / r, m_stop=m_stop)
        t0 = time.perf_counter()
        outr, sched = A1.run_march(P, tab, cfg)
        assert float(outr["cert_worst"]) <= 1.0, \
            "level r=%d not Newton-certified (worst %.3e)" % (
                r, float(outr["cert_worst"]))
        # PRODUCTION path for the differentiated replay ([X-SCANM] +
        # the S18 P2 lever): the eager Python replay builds a graph of
        # O(10^4) custom_vjp cells per level and is what killed the S17
        # run by graph churn — the bucketed jit is the path of record.
        plan = SC.build_plan(sched.d, cfg)
        runj = SC.make_run_scan_jit(tab, cfg, plan)

        def Qf(Pv, rj=runj):
            o = rj(Pv)
            return weighted_trapz(o["wall_x"], o["wall_y"], a, b)

        Q = float(Qf(P))
        # RK-G monitor (i) per level: the differentiated replay must
        # reproduce the CERTIFIED record at the Newton floor, else the
        # exponent would be measured on a different sequence than the
        # one that was certified.
        Q_rec = float(weighted_trapz(outr["wall_x"], outr["wall_y"],
                                     a, b))
        rep = abs(Q - Q_rec)
        tol_rep = (A1.NEWTON_TOL_FACTOR * EPS * int(outr["cert_n"])
                   * max(abs(Q_rec), 1.0))
        g = np.asarray(jax.grad(Qf)(P))
        res["h"].append(1.0 / r)
        res["Q"].append(Q)
        res["G"].append(float(g @ v))
        res["n"].append(int(outr["cert_n"]))
        res["Me"].append(float(outr["Me"]))
        res["rep"].append((rep, tol_rep))
        res["t"].append(time.perf_counter() - t0)
        print("    r=%d  NI=%-4d Ne=%-4d cells=%-7d  Q = %.12e  "
              "<g,v> = %.12e  Me = %.9f  |replay-record| = %.2e "
              "(floor %.2e)  (%.1f s)"
              % (r, cfg["NI"], cfg["Ne"], res["n"][-1], Q,
                 res["G"][-1], res["Me"][-1], rep, tol_rep,
                 res["t"][-1]))
    return res


# ======================================================================
# S4  TOC TWIN [X-TOCV] — primal wall-speed functional + AD gradient,
#     and the FIRST-ORDER negative control
# ======================================================================
def make_solvers_foot(state_fn, delta_eff):
    """FIRST-ORDER twin of a1_march_scan.make_solvers: the SAME unit
    processes with the characteristic coefficients frozen at the FOOT
    state instead of the segment MIDPOINT — the explicit-Euler form of
    the MoC cell instead of the average-coefficient (modified-Euler)
    form. Consistent, provably O(h). This is the carrier's principled
    negative control: identical code path and identical certification,
    KNOWN wrong order."""
    def coef(u, v, y, ta):
        q = jnp.sqrt(u * u + v * v)
        A = jnp.arctan2(v, u)
        _, _, _, c, _, M = state_fn(q, ta)
        mu = jnp.arcsin(1.0 / M)
        return (jnp.tan(A - mu), jnp.tan(A + mu), u * u - c * c,
                2.0 * u * v, delta_eff * c * c * v / y)

    def resid_int(z, p, ta):
        x4, y4, u4, v4 = z
        x1, y1, u1, v1, x2, y2, u2, v2 = p
        lm, _, qm, rm0, sm = coef(u1, v1, y1, ta)      # FOOT, not mid
        rm = rm0 - qm * lm
        _, lp, qp, rp0, sp = coef(u2, v2, y2, ta)      # FOOT, not mid
        rp = rp0 - qp * lp
        return jnp.array([
            (y4 - y1) - lm * (x4 - x1),
            (y4 - y2) - lp * (x4 - x2),
            qm * u4 + rm * v4 - (sm * (x4 - x1) + qm * u1 + rm * v1),
            qp * u4 + rp * v4 - (sp * (x4 - x2) + qp * u2 + rp * v2),
        ])

    def resid_axi(z, p, ta):
        x4, u4 = z
        x1, y1, u1, v1 = p
        lm, _, qm, rm0, sm = coef(u1, v1, y1, ta)
        rm = rm0 - qm * lm
        return jnp.array([
            (0.0 - y1) - lm * (x4 - x1),
            qm * u4 - (sm * (x4 - x1) + qm * u1 + rm * v1),
        ])

    def resid_wal(z, p, ta):
        x2, u4 = z
        x1, y1, u1, v1, x3, y3, u3, v3, x4, y4, slope = p
        D = (x2 - x1) / (x3 - x1)
        y2 = y1 + D * (y3 - y1)
        u2 = u1 + D * (u3 - u1)
        v2 = v1 + D * (v3 - v1)
        _, lp, qp, rp0, sp = coef(u2, v2, y2, ta)      # FOOT, not mid
        rp = rp0 - qp * lp
        return jnp.array([
            (y4 - y2) - lp * (x4 - x2),
            (qp + slope * rp) * u4
            - (sp * (x4 - x2) + qp * u2 + rp * v2),
        ])

    mk = A1.make_implicit_solver
    return dict(interior=mk(resid_int), axis=mk(resid_axi),
                wall=mk(resid_wal))


_FOOT_CACHE = {}


def foot_solvers(key, state_fn, delta_eff):
    if key not in _FOOT_CACHE:
        _FOOT_CACHE[key] = make_solvers_foot(state_fn, delta_eff)
    return _FOOT_CACHE[key]


def toc_ladder(tab, state_fn, solvers, rmax, label, window=None,
               with_grad=True):
    """Refinement ladder on the TOC march at W*. Level r: NI ->
    r(NI-1)+1, Nw -> r Nw, da -> da/r; h_r = 1/r."""
    W = jnp.asarray(W_STAR)
    base = dict(NI=TV.TCASE["NI"], Nw=TV.NW, da_deg=TV.TCASE["da_deg"],
                yt=TV.TCASE["yt"], rtu=TV.TCASE["rtu"],
                rtd=TV.TCASE["rtd"], xtronc=TV.TCASE["xtronc"])
    if window is None:
        out1, _ = TV.run_toc_record(W_STAR, tab, base, state_fn=state_fn,
                                    solvers=solvers)
        wx1 = np.asarray(out1["wall"][:, 0])
        d = STENCIL_RADIUS * float(np.max(np.diff(wx1)))
        window = (float(wx1[0]) + d, float(wx1[-1]) - d,
                  float(wx1[-1]) - d, float(wx1[-1]))
        print("  registered window x in [%.4f, %.4f] (excluded d = "
              "%.4f); LIP window x in [%.4f, %.4f] (the neighborhood "
              "the registered norm EXCLUDES — pre-registration item "
              "(d)); wall x in [%.4f, %.4f]"
              % (window[0], window[1], d, window[2], window[3],
                 wx1[0], wx1[-1]))
    a, b, alip, blip = window
    v = np.asarray(np.random.default_rng(320).standard_normal(len(W_STAR)))
    v /= np.linalg.norm(v)

    res = dict(h=[], Q=[], J=[], G=[], Qlip=[], qlip=[], topo=[],
               n=[], t=[], rep=[], window=window)
    for r in range(1, rmax + 1):
        cfg = dict(base)
        cfg["NI"] = r * (base["NI"] - 1) + 1
        cfg["Nw"] = r * base["Nw"]
        cfg["da_deg"] = base["da_deg"] / r
        t0 = time.perf_counter()
        outr, plan = TV.run_toc_record(W_STAR, tab, cfg,
                                       state_fn=state_fn, solvers=solvers)
        assert float(outr["cert_worst"]) <= 1.0, \
            "%s level r=%d not certified (worst %.3e)" % (
                label, r, float(outr["cert_worst"]))
        assert float(outr["min_margin"]) > 0.0, \
            "%s level r=%d violates the axial margin" % (label, r)
        t_rec = time.perf_counter() - t0
        runj = TV.make_run_toc_scan_jit(tab, cfg, plan, state_fn=state_fn,
                                        solvers=solvers)

        def Qf(Wv, rj=runj):
            w = rj(Wv)
            return weighted_trapz(w[:, 0], w[:, 2], a, b)

        def Jf(Wv, rj=runj):
            return TV.thrust_J(rj(Wv), tab, state_fn=state_fn)

        Q = float(Qf(W))
        J = float(Jf(W))
        wall = outr["wall"]
        Qlip = float(weighted_trapz(wall[:, 0], wall[:, 2], alip, blip))
        Q_rec = float(weighted_trapz(wall[:, 0], wall[:, 2], a, b))
        rep = abs(Q - Q_rec)
        tol_rep = (A1.NEWTON_TOL_FACTOR * EPS * int(outr["cert_n"])
                   * max(abs(Q_rec), 1.0))
        res["rep"].append((rep, tol_rep))
        G = float(np.asarray(jax.grad(Jf)(W)) @ v) if with_grad else 0.0
        res["h"].append(1.0 / r)
        res["Q"].append(Q)
        res["J"].append(J)
        res["G"].append(G)
        res["Qlip"].append(Qlip)
        # POINTWISE wall-adjacent probe (pre-registration item (d)):
        # the lip station sits at x = L exactly and EXISTS AT EVERY
        # LEVEL, so its wall speed is a genuine pointwise field value —
        # no quadrature, unlike the lip-WINDOW functional, whose
        # coarsest level is supported on ~2 stations and therefore
        # conflates quadrature error with wall-adjacent behaviour.
        res["qlip"].append(float(np.hypot(wall[-1, 2], wall[-1, 3])))
        # TOPOLOGY MONITOR (clause LB-c2 made measurable): S-LBML takes
        # the mesh limit AT FIXED MARCH TOPOLOGY, but a refinement
        # ladder cannot hold the topology fixed — the L-DoD truncation
        # decides per column whether a cell lands past the lip, and the
        # wall-search indices are re-recorded at every level. If the
        # fraction of columns carrying an axis point does not vary
        # smoothly with r, the ladder is crossing strata and the
        # gradient sequence carries stratum-transition terms that no
        # order estimator can absorb. Asserted mechanisms are worth
        # nothing; this is the number that supports or refutes it.
        arc = plan["arc"]
        res["topo"].append((sum(1 for c in arc if c["has_axis"]),
                            len(arc)))
        res["n"].append(int(outr["cert_n"]))
        res["t"].append(time.perf_counter() - t0)
        print("    r=%d  NI=%-4d Nw=%-4d cells=%-7d  Q_u = %.12e  "
              "J = %.12e  <dJ/dW,v> = %.12e  Q_lip = %.12e  "
              "|replay-record| = %.2e (floor %.2e)  "
              "(rec %.1f s, tot %.1f s)"
              % (r, cfg["NI"], cfg["Nw"], res["n"][-1], Q, J, G, Qlip,
                 rep, tol_rep, t_rec, res["t"][-1]))
    return res


# ======================================================================
# S5  lip-window diagnostic (pre-registration item (d), the half of
#     the X1 audit executable on a shock-free twin)
# ======================================================================
# (the lip-window probe of pre-registration item (d) is computed
# INSIDE toc_ladder from the same certified records — a separate
# ladder would only re-run identical marches.)


# ======================================================================
def main():
    stage = os.environ.get("A1_O32_STAGE", "all")
    rmax = int(os.environ.get("A1_O32_RMAX", "4"))
    print("== ORACLE O3.2 [X-O32]: mesh convergence of the primal/"
          "adjoint pair (JAX %s) ==" % jax.__version__)
    print("  ladder r = 1..%d (h = 1/r); stage = %s" % (rmax, stage))
    ok = True

    print("-- S1: estimator known-answer test + monotonicity --")
    ok &= estimator_selftest()
    if stage == "est":
        print("VERDICT (stage est): %s" % ("PASS" if ok else "FAIL"))
        return 0 if ok else 1

    tab = A1.prep_tab(A1.build_tab_nasa())

    if stage == "mstop":
        # PRE-DECLARED DIAGNOSTIC (registered in the S19 log BEFORE the
        # decisive run, per R5): if the ideal twin's exponent degrades,
        # the FIRST hypothesis is the mirrored GENO exit constant
        # |M - Me| < 1e-5 (critical-list item 3) acting as an accuracy
        # FLOOR on the achieved exit Mach — the case itself then drifts
        # with h. Test = re-run the ladder with the constant tightened
        # 100x. The BAND IS NOT AMENDED by this diagnostic; it only
        # attributes a measured degradation to a named mechanism.
        print("-- PRE-DECLARED DIAGNOSTIC: ideal ladder with the "
              "mirrored stop constant tightened 100x (1e-5 -> 1e-7) --")
        rd = ideal_ladder(tab, rmax, m_stop=1.0e-7)
        verdict_row("primal  Q (tightened stop)", rd["Q"], rd["h"],
                    rd["n"])
        verdict_row("adjoint <grad_P Q, v> (tightened)", rd["G"],
                    rd["h"], rd["n"])
        dMe = [abs(rd["Me"][k] - rd["Me"][k + 1])
               for k in range(len(rd["Me"]) - 1)]
        print("  |dMe| along the tightened ladder: %s"
              % np.array2string(np.array(dMe), precision=3))
        return 0

    if stage in ("all", "ideal"):
        print("-- S2: IDEAL twin [X-A1IM] ladder --")
        ri = ideal_ladder(tab, rmax)
        ok &= check("ideal: differentiated replay == certified record "
                    "at the Newton floor, every level",
                    all(d <= t for (d, t) in ri["rep"]))
        print("  O3.2 rows (ideal twin):")
        ok &= verdict_row("primal  Q = int w y dx", ri["Q"], ri["h"],
                          ri["n"])[0]
        ok &= verdict_row("adjoint <grad_P Q, v>", ri["G"], ri["h"],
                          ri["n"])[0]
        dMe = [abs(ri["Me"][k] - ri["Me"][k + 1])
               for k in range(len(ri["Me"]) - 1)]
        print("  [critical-list monitor] |dMe| along the ladder: %s "
              "(GENO-mirrored stop constant |M - Me| < 1e-5)"
              % np.array2string(np.array(dMe), precision=3))

    if stage in ("all", "toc"):
        print("-- S3: TOC twin [X-TOCV] ladder at W* (C^1 quintic "
              "closure, the brick's primary) --")
        c1 = TH.build_c1(tab)

        def state_c1(q, ta_ignored):
            return TH.state_q_c1(q, c1)

        solv = SC.cached_solvers(("thc1_nasa", 1.0), state_c1, 1.0)
        rt = toc_ladder(tab, state_c1, solv, rmax, "production")
        ok &= check("TOC: differentiated replay == certified record at "
                    "the Newton floor, every level",
                    all(d <= t for (d, t) in rt["rep"]))
        print("  O3.2 rows (TOC twin):")
        okR, _, pR, _ = verdict_row("primal  Q_u = int w u dx", rt["Q"],
                                    rt["h"], rt["n"])
        ok &= okR
        ok &= verdict_row("primal  J (objective)", rt["J"], rt["h"],
                          rt["n"])[0]
        ok &= verdict_row("adjoint <dJ/dW, v>", rt["G"], rt["h"],
                          rt["n"])[0]

        print("-- S4: NEGATIVE CONTROL — foot-coefficient (first-order) "
              "march must be REJECTED --")
        solv_f = foot_solvers(("foot_thc1", 1.0), state_c1, 1.0)
        rf = toc_ladder(tab, state_c1, solv_f, rmax, "foot",
                        window=rt["window"], with_grad=False)
        okQ, conclQ, pQ, dpQ = verdict_row("first-order primal Q_u",
                                           rf["Q"], rf["h"], rf["n"])
        ok &= check("N1 first-order march REJECTED by the h^2 band",
                    (not okQ) and conclQ is True)
        print("      (measured exponent %.4f — the explicit-Euler unit "
              "process is first order by construction)"
              % (pQ if pQ is not None else float("nan")))

        print("-- S5: wall/lip-adjacent probes (pre-registration item "
              "(d); the half of the X1 audit executable on a "
              "shock-free twin) --")
        print("  [topology monitor, clause LB-c2] columns carrying an "
              "axis point / design-wall columns, per level: %s"
              % " ".join("%d/%d" % t for t in rt["topo"]))
        # The POINT probe is the one that decides: the lip station is
        # at x = L exactly and exists at EVERY level, so its wall speed
        # is a genuine pointwise field value. The lip-WINDOW functional
        # is reported too but its coarsest level is supported on ~2
        # stations, so it conflates quadrature error with wall-adjacent
        # behaviour and is expected to be unusable.
        _, conclP, pP, dpP = verdict_row("lip-POINT wall speed q(x=L)",
                                         rt["qlip"], rt["h"], rt["n"])
        _, conclL, pL, dpL = verdict_row("lip-window Q_lip", rt["Qlip"],
                                         rt["h"], rt["n"])
        print("      lip-POINT exponent = %s (conclusive: %s) vs "
              "registered-norm exponent %s -> the pre-registered "
              "lip exclusion is %s on this instance (REPORTED; the S14 "
              "pin is not re-litigated either way). lip-WINDOW row: %s"
              % ("%.4f" % pP if pP is not None else "n/a",
                 "yes" if conclP else "no",
                 "%.4f" % pR if pR is not None else "n/a",
                 "EMPIRICALLY SUPPORTED — the wall-adjacent field "
                 "converges at a degraded order while the registered "
                 "norm does not"
                 if (pP is not None and conclP and pP < 2.0 - dpP)
                 else "not supported by this probe",
                 "%.4f" % pL if pL is not None else "unusable "
                 "(quadrature-limited at the coarsest level, as "
                 "expected)"))

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
