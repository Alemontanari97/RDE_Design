#!/usr/bin/env python3
"""THERMOTAB C^1 [F2/A1, session S17, brick-2 kickoff duty (d)]:
the C^1 tabulated-closure class of record for the brick-2 engine +
the EOS genuine-nonlinearity audit (ledger channel c4, S16 addition).
Registry ID: [X-THC1]. Normative spec: docs/rde_nozzle_brick2_kickoff.md §2.

DEFECT FIXED (S14 two-lens finding, D6 item 9): the [X-A1IM] closure
interpolates cp INDEPENDENTLY of h with piecewise-linear jnp.interp =>
cp != dh/dT between knots and the state Jacobian jumps at knots.

CLASS OF RECORD (kickoff discovery, declared in the spec §2): QUINTIC
Hermite — cubic Hermite would make cp = h' only C^0 (slope jumps at
knots), against the C^1-coefficients requirement (C-D25U machinery).
  h(T):  node data (h_i, cp_i, cp'_i)                     -> C^2
  s0(T): node data (s0_i, cp_i/T_i, (cp'_i T_i - cp_i)/T_i^2) -> C^2
  cp(T) := d/dT h-interpolant  (EXACT derivative polynomial)  -> C^1
cp'_i from the dense cp table by 4th-order central differences
(2nd-order one-sided at the edges). INVARIANTS: cp = dh/dT STRUCTURAL
(machine-verified vs AD at roundoff); s0' = cp/T exact at nodes,
inter-node within the DERIVED Hermite-remainder floor. Monotone-
VERIFIED class: h' = cp interpolant proven positive on a dense probe
with derived margin (no clamping — clamping would break the
invariant). Inverse T(h): Newton on the quintic (linear-interp seed,
fixed trips), roundtrip-certified at the derived floor.

EOS G > 0 AUDIT (c4): ideal-gas fundamental derivative derived from
G = 1 + (rho/c)(dc/drho)_s with (dT/drho)_s = (gamma-1) T/rho:
    G(T) = (gamma+1)/2 + (gamma-1) T gamma'(T) / (2 gamma)
(reduces to (gamma+1)/2 at gamma' = 0 — verified as known-answer).
gamma' needs cp', defined BECAUSE the closure is C^1. Certified on
the declared box = the full table T range (contains every march-
realized state) on a dense grid with a derived Lipschitz safety
margin (grid audit, declared: not an interval certificate; the
interval upgrade rides the PAP-GMAX substrate if c4 ever becomes
load-bearing at class level).

TOLERANCES — ALL DERIVED (R5):
  * structural invariant cp vs AD(h'): C * eps * scale, C = operation
    count factor (quintic evaluation, ~64 flops -> C = 100, the
    repo's Newton-floor factor convention).
  * s0' = cp/T inter-node: both sides are C^1 piecewise polynomials
    interpolating the same node data; the gap is bounded by the
    Hermite remainder of the DIFFERENCE class ~ K_RICH * dT^2 *
    max|second-difference of (cp/T)| (curvature bound from the data
    itself) + roundoff floor.
  * dual-route vs the certified [X-A1IM] linear closure: the two
    closures interpolate the SAME table; their gap is bounded by the
    LINEAR closure's own interpolation error, dT^2/8 * max|curvature|
    (data second differences), x K_RICH + floor.
  * gconst known-answer: same derived tol_T structure as X-A1IM S1
    (table-spacing^2 curvature bound + 64 eps floor).
  * inverse roundtrip: |h(T(h*)) - h*| <= C_NEWT * eps * |h-scale|.
  * G floor: min_grid(G) - K_RICH * dG_grid, with dG_grid the
    measured max grid-to-grid |delta G| (Lipschitz-from-data bound);
    audit PASSES iff the floor is > 0.

M3 FUSED/FLOOR-INDEX CLOSURE (S25 ENGINE SPEED, dispatch item M3 —
DECLARED version change, session-boundary adoption with fresh
records; [X-THC1] C1-C7 + R1-R6 re-run at adoption): the interval
locate is the O(1) floor index on the uniform grid, LICENSED by a
build-time grid-uniformity REJECTOR (loud refusal names the node);
the Newton inverse consumes the FUSED (h, cp) pair (one locate, one
gather set per trip — expressions VERBATIM eval_f/eval_fp) with the
PER-TABLE DERIVED trip count K_NEWT (seed-error bound + contraction
constant + the table's own roundoff floor + 1 margin trip — the
fixed N_NEWT_INV=8 literal is RETIRED to a negative-control
reference); the state's post-loop cp comes from the same fused pair.
C-A ORACLE (S24 thermo-survey condition, discharged at this touch):
the closure is checked against the NASA FIT ITSELF (not the table) —
in the joint-free window cp is quartic => h is exactly quintic and
the 4th-order cp' estimator is exact => h/cp match at the roundoff
floor; s0 (ln T term) matches within its derived quintic-Hermite
remainder band. Node-tie index control: off-node floor-vs-
searchsorted identity EXACT; node/±ulp probes value-banded via the
oracle.

NEGATIVE CONTROLS (the carrier must REJECT):
  (R1) corrupted cp row (1e-3 relative bump on a band) -> structural
       invariant vs the INDEPENDENT linear-cp route breaks.
  (R2) doctored non-monotone h (local inversion) -> positivity probe
       detects.
  (R3) BZT-doctored table (strong local negative gamma' via a cp
       spike) -> G floor goes negative, audit detects.
  (R4) corrupted inverse (biased seed + zero trips) -> roundtrip
       certification detects.
  (R5) non-uniform grid (one displaced node) -> the floor-index
       license rejector REFUSES the table build (M3).
  (R6) corrupted-D floor index -> disagrees with the searchsorted
       reference (the index-identity check can fire) (M3).

ON-DEMAND CARRIER (env: jax): outside the CI tiers by declaration,
like X-A1IM. Exit code 0 iff ALL checks pass INCLUDING all negative
controls.
"""
import os
import sys

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1  # noqa: E402  (table builders + linear closure)

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
K_RICH = 4.0          # repo two-level safety convention (X-A1IM)
C_OPS = 100.0         # operation-count roundoff factor (repo convention)
N_NEWT_INV = 8        # RETIRED literal (M3): kept ONLY as the R4/M3
#                       negative-control reference and the derived-K
#                       sanity ceiling; the live trip count is the
#                       per-table c1["K_NEWT"] (derived_newton_trips)
N_PROBE = 20001       # dense probe grid (odd, hits nodes and midpoints)


# ======================================================================
# derivative estimation on the uniform table grid
# ======================================================================
def d_dT_table(f, dT):
    """4th-order central differences, 2nd-order one-sided edges."""
    fp = np.empty_like(f)
    fp[2:-2] = (-f[4:] + 8.0 * f[3:-1] - 8.0 * f[1:-3] + f[:-4]) / (12.0 * dT)
    fp[0] = (-3.0 * f[0] + 4.0 * f[1] - f[2]) / (2.0 * dT)
    fp[1] = (f[2] - f[0]) / (2.0 * dT)
    fp[-2] = (f[-1] - f[-3]) / (2.0 * dT)
    fp[-1] = (3.0 * f[-1] - 4.0 * f[-2] + f[-3]) / (2.0 * dT)
    return fp


# ======================================================================
# quintic Hermite evaluation (values f, first derivs d, second derivs s)
# ======================================================================
def _quintic_coeffs(t):
    """Quintic Hermite basis at normalized t in [0,1]:
    H = f0 B0 + f1 B1 + D d0 B2 + D d1 B3 + D^2 s0 B4 + D^2 s1 B5."""
    t2, t3 = t * t, t * t * t
    t4, t5 = t2 * t2, t2 * t3
    B0 = 1.0 - 10.0 * t3 + 15.0 * t4 - 6.0 * t5
    B1 = 10.0 * t3 - 15.0 * t4 + 6.0 * t5
    B2 = t - 6.0 * t3 + 8.0 * t4 - 3.0 * t5
    B3 = -4.0 * t3 + 7.0 * t4 - 3.0 * t5
    B4 = 0.5 * t2 - 1.5 * t3 + 1.5 * t4 - 0.5 * t5
    B5 = 0.5 * t3 - t4 + 0.5 * t5
    return B0, B1, B2, B3, B4, B5


def _quintic_dcoeffs(t):
    """d/dt of the quintic basis (exact derivative polynomials)."""
    t2, t3 = t * t, t * t * t
    t4 = t2 * t2
    dB0 = -30.0 * t2 + 60.0 * t3 - 30.0 * t4
    dB1 = 30.0 * t2 - 60.0 * t3 + 30.0 * t4
    dB2 = 1.0 - 18.0 * t2 + 32.0 * t3 - 15.0 * t4
    dB3 = -12.0 * t2 + 28.0 * t3 - 15.0 * t4
    dB4 = t - 4.5 * t2 + 6.0 * t3 - 2.5 * t4
    dB5 = 1.5 * t2 - 4.0 * t3 + 2.5 * t4
    return dB0, dB1, dB2, dB3, dB4, dB5


def make_quintic(Tg, f, d, s):
    """Returns (eval_f, eval_fprime) for the quintic Hermite with node
    values f, first derivatives d, second derivatives s on the uniform
    grid Tg. Differentiable in T (piecewise polynomial, C^2).

    M3 (S25 ENGINE SPEED, dispatch item M3 — DECLARED version change,
    session-boundary adoption with fresh records): the interval
    locate is the O(1) FLOOR INDEX on the uniform grid (licensed by
    the build_c1 grid-uniformity REJECTOR, gauntlet V5 — this maker
    is consumed only by build_c1 in this repo), replacing the
    per-eval searchsorted. Off-node points produce the IDENTICAL
    index and the identical t = (T - Tg[i]) / D; at node ties the
    index may legally differ by one — covered by the node-tie
    index-identity control run per table at build (values agree
    within the derived C^2-continuity band)."""
    Tg = jnp.asarray(Tg)
    f, d, s = jnp.asarray(f), jnp.asarray(d), jnp.asarray(s)
    D = Tg[1] - Tg[0]
    n = Tg.shape[0]
    Tg0 = Tg[0]
    invD = 1.0 / D

    def _locate(T):
        i = jnp.clip(jnp.floor((T - Tg0) * invD).astype(jnp.int32),
                     0, n - 2)
        t = (T - Tg[i]) / D
        return i, t

    def eval_f(T):
        i, t = _locate(T)
        B0, B1, B2, B3, B4, B5 = _quintic_coeffs(t)
        return (f[i] * B0 + f[i + 1] * B1
                + D * (d[i] * B2 + d[i + 1] * B3)
                + D * D * (s[i] * B4 + s[i + 1] * B5))

    def eval_fp(T):
        i, t = _locate(T)
        dB0, dB1, dB2, dB3, dB4, dB5 = _quintic_dcoeffs(t)
        return ((f[i] * dB0 + f[i + 1] * dB1) / D
                + d[i] * dB2 + d[i + 1] * dB3
                + D * (s[i] * dB4 + s[i + 1] * dB5))

    def eval_f_fp(T):
        """M3 fused (value, derivative): ONE locate, ONE 6-node
        gather set shared by both expressions (the per-trip body of
        the fused Newton inverse). The two expressions are VERBATIM
        eval_f/eval_fp — only WHO gathers changes."""
        i, t = _locate(T)
        f0, f1 = f[i], f[i + 1]
        d0, d1 = d[i], d[i + 1]
        s0_, s1 = s[i], s[i + 1]
        B0, B1, B2, B3, B4, B5 = _quintic_coeffs(t)
        dB0, dB1, dB2, dB3, dB4, dB5 = _quintic_dcoeffs(t)
        val = (f0 * B0 + f1 * B1
               + D * (d0 * B2 + d1 * B3)
               + D * D * (s0_ * B4 + s1 * B5))
        der = ((f0 * dB0 + f1 * dB1) / D
               + d0 * dB2 + d1 * dB3
               + D * (s0_ * dB4 + s1 * dB5))
        return val, der

    return eval_f, eval_fp, eval_f_fp


# ======================================================================
# the C^1 closure of record (brick-2 engine backend)
# ======================================================================
def grid_uniformity_reject(Tg):
    """M3/V5 grid-uniformity REJECTOR (licenses the O(1) floor
    index): every node must sit on the uniform law Tg0 + i*D within
    the derived roundoff band C_OPS*eps*max|T|, and that band must
    be DEEP below the spacing. Loud refusal names the interval."""
    Tg = np.asarray(Tg)
    n = len(Tg)
    D = (Tg[-1] - Tg[0]) / (n - 1)
    dev = np.abs(Tg - (Tg[0] + np.arange(n) * D))
    band = C_OPS * EPS * np.max(np.abs(Tg))
    i_bad = int(np.argmax(dev))
    if not (dev[i_bad] <= band and band < 0.5 * D):
        raise RuntimeError(
            "table grid fails the uniformity rejector: node %d "
            "deviates %.3e from the uniform law (band %.3e, D %.3e) "
            "— the O(1) floor index is NOT licensed for this table"
            % (i_bad, dev[i_bad], band, D))
    return D, band


def derived_newton_trips(Tg, cpg, cpp):
    """M3/V4: the inverse-Newton trip count K COMPUTED FROM THIS
    TABLE'S OWN DATA (never a literal): seed = linear interp of
    T(h) => seed error e0 = max_i (cp_i dT)^2/8 * |cp'_i|/cp_i^3
    (remainder with T''(h) = -cp'/cp^3, h-spacing cp_i dT); Newton
    contraction e+ <= M e^2 with M = max|cp'|/(2 min cp); target =
    the table's own roundoff floor C_OPS*eps*max|T| (the C6 floor
    scale); +1 trip margin (bound-slack guard, K_RICH spirit).
    Refuses (loudly) if the bound cannot certify contraction."""
    Tg = np.asarray(Tg)
    cpg = np.asarray(cpg)
    cpp = np.asarray(cpp)
    dT = float(Tg[1] - Tg[0])
    e0 = float(np.max((cpg * dT) ** 2 / 8.0
                      * np.abs(cpp) / cpg ** 3))
    M = float(np.max(np.abs(cpp)) / (2.0 * np.min(cpg)))
    floor = C_OPS * EPS * float(np.max(np.abs(Tg)))
    if M * max(e0, floor) >= 1.0:
        raise RuntimeError(
            "derived-K refusal: Newton contraction not certified "
            "from the table data (M*e0 = %.3e >= 1)"
            % (M * max(e0, floor)))
    e, K = max(e0, floor), 0
    while e > floor and K < 64:
        e = M * e * e
        K += 1
    K += 1                      # declared margin trip
    return K, e0, M, floor


def build_c1(tab):
    """From an [X-A1IM] table dict, build the C^1 closure pack.
    M3 (S25): the pack carries the fused (value, derivative)
    evaluators, the grid-uniformity license, and the PER-TABLE
    DERIVED Newton trip count K_NEWT (printed; stored; never a
    literal — gauntlet V4/V5)."""
    Tg = np.asarray(tab["T"])
    hg = np.asarray(tab["h"])
    s0g = np.asarray(tab["s0m"])
    cpg = np.asarray(tab["cp"])
    grid_uniformity_reject(Tg)                   # V5 license (loud)
    dT = Tg[1] - Tg[0]
    cpp = d_dT_table(cpg, dT)                    # cp'_i estimates
    h_f, h_fp, h_ffp = make_quintic(Tg, hg, cpg, cpp)  # h: (h,cp,cp')
    s0_d = cpg / Tg                              # s0' = cp/T at nodes
    s0_s = (cpp * Tg - cpg) / (Tg * Tg)          # (cp/T)' at nodes
    s0_f, s0_fp, _ = make_quintic(Tg, s0g, s0_d, s0_s)
    K, e0, M, floorK = derived_newton_trips(Tg, cpg, cpp)
    return dict(Tg=jnp.asarray(Tg), hg=jnp.asarray(hg),
                cpg=jnp.asarray(cpg), cpp=jnp.asarray(cpp),
                h=h_f, cp=h_fp,                  # cp := d/dT h (structural)
                h_cp=h_ffp,                      # M3 fused pair
                s0=s0_f, s0p=s0_fp,
                K_NEWT=int(K), K_derivation=dict(
                    e0=float(e0), M=float(M), floor=float(floorK)),
                Rg=jnp.float64(tab["Rg"]), h0=jnp.float64(tab["h0"]),
                s0_ref=jnp.float64(tab["s0"]), dT=float(dT),
                name=tab["name"])


def invert_h(c1, ht):
    """T(h): Newton on the monotone quintic, linear-interp seed.
    M3: fused (h, cp) per trip (one locate, one gather set) and the
    trip count = the PER-TABLE DERIVED c1["K_NEWT"] (V4; the old
    fixed N_NEWT_INV=8 literal is retired to the module constant
    for the R4 negative control only)."""
    T0 = jnp.interp(ht, c1["hg"], c1["Tg"])
    K = int(c1.get("K_NEWT", N_NEWT_INV))

    def body(_, T):
        h_v, cp_v = c1["h_cp"](T)
        return T - (h_v - ht) / cp_v

    return jax.lax.fori_loop(0, K, body, T0)


def state_q_c1(q, c1):
    """C^1 closure q -> (T, p, rho, c, gam, M) — the brick-2 twin of
    [X-A1IM] state_q with the quintic backend. M3: post-loop cp
    comes from the SAME fused pair evaluation (one locate); s0 is
    the remaining single-family evaluation."""
    ht = c1["h0"] - 0.5 * q * q
    T = invert_h(c1, ht)
    _, cp = c1["h_cp"](T)
    p = A1.PREF * jnp.exp((c1["s0"](T) - c1["s0_ref"]) / c1["Rg"])
    rho = p / (c1["Rg"] * T)
    gam = cp / (cp - c1["Rg"])
    c = jnp.sqrt(gam * c1["Rg"] * T)
    return T, p, rho, c, gam, q / c


def gamma_of_T(c1, T):
    cp = c1["cp"](T)
    return cp / (cp - c1["Rg"])


def G_of_T(c1, T):
    """Fundamental derivative G(T) = (gam+1)/2 + (gam-1) T gam'/(2 gam)
    (ideal gas, derivation in the kickoff spec §2). gam' by AD of the
    C^1 gamma — defined because cp is C^1."""
    gam = gamma_of_T(c1, T)
    gamp = jax.vmap(jax.grad(lambda t: gamma_of_T(c1, t)))(T)
    return 0.5 * (gam + 1.0) + (gam - 1.0) * T * gamp / (2.0 * gam)


# ======================================================================
# checks
# ======================================================================
def check(label, ok):
    print("  [%s] %s" % (label, "PASS" if ok else "FAIL"))
    return bool(ok)


def main():
    print("== THERMOTAB C^1 [X-THC1]: quintic-Hermite closure + G>0 "
          "audit (JAX %s) ==" % jax.__version__)
    ok = True

    tab_n = A1.prep_tab(A1.build_tab_nasa())
    tab_c = A1.prep_tab(A1.build_tab_cantera())
    c1n = build_c1(tab_n)
    c1c = build_c1(tab_c)
    Tg = np.asarray(c1n["Tg"])
    dT = c1n["dT"]
    Tp = jnp.linspace(Tg[0], Tg[-1], N_PROBE)    # dense probe (nodes+mids)

    # ---------------- C1: monotone-verified class (h' = cp > 0)
    print("-- C1: monotonicity of h (positivity of the cp interpolant) --")
    cp_prob = jax.vmap(c1n["cp"])(Tp)
    cp_min = float(jnp.min(cp_prob))
    # derived margin: the interpolant between probe points can dip at
    # most Lip_grid * probe spacing; Lip from the data's own max slope
    lip_cp = float(np.max(np.abs(np.diff(np.asarray(c1n["cpg"])))) / dT)
    dip = lip_cp * float(Tp[1] - Tp[0]) * K_RICH
    print("  min cp on probe = %.6f J/(kg K); worst-dip margin %.3e"
          % (cp_min, dip))
    ok &= check("h monotone (cp interpolant positive with margin)",
                cp_min - dip > 0.0)

    # ---------------- C2: STRUCTURAL invariant cp == dh/dT (vs AD)
    print("-- C2: structural invariant cp = dh/dT (AD cross-check) --")
    ad_hp = jax.vmap(jax.grad(c1n["h"]))(Tp)
    scale = float(jnp.max(jnp.abs(cp_prob)))
    err = float(jnp.max(jnp.abs(ad_hp - cp_prob)))
    # derived roundoff bound for TWO evaluation orders of the same
    # polynomial derivative: each order rounds at its worst
    # INTERMEDIATE magnitude — the basis-derivative coefficients reach
    # 60 (dB1 term), applied to node values |h| and divided by D, plus
    # the cp-sized terms; C_OPS covers the op count.
    hscale = float(jnp.max(jnp.abs(c1n["hg"])))
    tol = C_OPS * EPS * (60.0 * hscale / dT + scale)
    print("  max|AD(h') - cp| = %.3e (derived intermediate-magnitude"
          " tol %.3e)" % (err, tol))
    ok &= check("cp = dh/dT structural (roundoff)", err <= tol)

    # ---------------- C3: s0' = cp/T (nodes exact, inter-node floor)
    print("-- C3: invariant s0' = cp/T --")
    s0p_prob = jax.vmap(c1n["s0p"])(Tp)
    tgt = cp_prob / Tp
    gap = np.abs(np.asarray(s0p_prob - tgt))
    # nodes: exact by construction (verify at the node subset)
    node_idx = np.arange(0, N_PROBE, (N_PROBE - 1) // (len(Tg) - 1))[: len(Tg)]
    # derived inter-node floor: second differences of (cp/T) data
    q_data = np.asarray(c1n["cpg"]) / Tg
    curv = np.max(np.abs(np.diff(q_data, 2))) / dT**2
    floor = K_RICH * dT**2 * curv + C_OPS * EPS * float(np.max(np.abs(tgt)))
    print("  max|s0' - cp/T| = %.3e (derived floor %.3e; node-set max "
          "%.3e)" % (gap.max(), floor, gap[node_idx].max()))
    ok &= check("s0' = cp/T within derived floor", gap.max() <= floor)

    # ---------------- C4: gconst known-answer closure
    print("-- C4: gconst known-answer (closed forms) --")
    tab_g = A1.prep_tab(A1.build_tab_gconst())
    c1g = build_c1(tab_g)
    g, Rg, ts, ps, cpc = (tab_g["_g"], tab_g["Rg"], tab_g["ts"],
                          tab_g["ps"], tab_g["_cp"])
    qs = jnp.linspace(600.0, 2600.0, 7)
    T_t, p_t, _, c_t, gam_t, M_t = jax.vmap(
        lambda q: state_q_c1(q, c1g))(qs)
    T_ex = ts - qs**2 / (2.0 * cpc)
    p_ex = ps * (T_ex / ts) ** (g / (g - 1.0))
    M_ex = qs / jnp.sqrt(g * Rg * T_ex)
    # h = cp T is linear (quintic exact); s0 = cp ln T is not — derived
    # interp floor from the s0 remainder propagated through exp/Rg
    dTt = (A1.T_TAB_HI - A1.T_TAB_LO) / (A1.N_TAB - 1)
    curv_s0 = np.max(np.abs(np.diff(np.asarray(c1g["s0"](c1g["Tg"])), 2))) \
        / dTt**2
    tol_T = C_OPS * EPS * ts
    tol_p = (K_RICH * dTt**2 * curv_s0 / Rg) + 64.0 * EPS * g / (g - 1.0)
    errT = float(jnp.max(jnp.abs(T_t - T_ex)))
    errp = float(jnp.max(jnp.abs(p_t / p_ex - 1.0)))
    errM = float(jnp.max(jnp.abs(M_t - M_ex)))
    print("  |dT| %.2e (tol %.2e)  |dp/p| %.2e (tol %.2e)  |dM| %.2e"
          % (errT, tol_T, errp, tol_p, errM))
    ok &= check("gconst known-answer (h linear exact, s0 in floor)",
                errT <= tol_T and errp <= tol_p and errM <= tol_p)
    # gamma-const reduction of G: known-answer (gam+1)/2
    G_g = G_of_T(c1g, jnp.linspace(1100.0, 3800.0, 101))
    errG = float(jnp.max(jnp.abs(G_g - 0.5 * (g + 1.0))))
    tolG = C_OPS * EPS + K_RICH * dTt**2  # cp' estimator floor on const
    print("  [G known-answer] max|G - (g+1)/2| = %.3e (tol %.3e)"
          % (errG, tolG))
    ok &= check("G reduces to (gamma+1)/2 at gamma' = 0", errG <= tolG)

    # ---------------- C5: dual-route vs the certified linear closure
    print("-- C5: C^1 closure vs [X-A1IM] linear closure (derived band) --")
    ta_n = A1.tab_arrays(tab_n)
    qs2 = jnp.linspace(700.0, 2400.0, 401)
    T_lin = A1.state_q(qs2, ta_n)[0]
    T_c1 = jax.vmap(lambda q: state_q_c1(q, c1n))(qs2)[0]
    # the gap is bounded by the LINEAR closure's own interp error:
    # dT^2/8 * curvature of T(h) data, via |dT/dh| = 1/cp
    curv_h = np.max(np.abs(np.diff(np.asarray(tab_n["h"]), 2))) / dT**2
    band_T = K_RICH * (dT**2 / 8.0) * curv_h / float(jnp.min(cp_prob)) \
        * 1.0 + C_OPS * EPS * float(np.max(Tg))
    gap_T = float(jnp.max(jnp.abs(T_lin - T_c1)))
    print("  max|T_lin - T_c1| = %.3e K (derived band %.3e K)"
          % (gap_T, band_T))
    ok &= check("dual-route closure gap inside interpolation band",
                gap_T <= band_T)

    # ---------------- C6: inverse roundtrip certification
    print("-- C6: inverse T(h) roundtrip --")
    hs = jnp.linspace(float(c1n["hg"][2]), float(c1n["hg"][-3]), 1001)
    Ts = jax.vmap(lambda h: invert_h(c1n, h))(hs)
    back = jax.vmap(c1n["h"])(Ts)
    rerr = float(jnp.max(jnp.abs(back - hs)))
    tol_rt = C_OPS * EPS * float(jnp.max(jnp.abs(hs)))
    print("  max|h(T(h)) - h| = %.3e (tol %.3e)" % (rerr, tol_rt))
    ok &= check("inverse roundtrip at roundoff floor", rerr <= tol_rt)

    # ---------------- C7: G > 0 audit on the declared box (c4)
    print("-- C7: EOS G > 0 audit (ledger channel c4) --")
    for c1x in (c1n, c1c):
        Gv = G_of_T(c1x, Tp)
        Gmin = float(jnp.min(Gv))
        dG = float(jnp.max(jnp.abs(jnp.diff(Gv))))
        floor_G = Gmin - K_RICH * dG
        gmn = float(jnp.min(gamma_of_T(c1x, Tp)))
        gmx = float(jnp.max(gamma_of_T(c1x, Tp)))
        print("  [%s] gamma in [%.4f, %.4f]; min G = %.6f; grid "
              "|dG| max %.2e; certified floor %.6f"
              % (c1x["name"], gmn, gmx, Gmin, dG, floor_G))
        ok &= check("G > 0 on box (%s, Lipschitz-margin floor)"
                    % c1x["name"], floor_G > 0.0)

    # ---------------- M3 rows (S25): derived K + floor-index license
    print("-- M3: per-table derived Newton count + floor-index "
          "license --")
    for c1x in (c1n, c1c):
        kd = c1x["K_derivation"]
        print("  [%s] K_NEWT = %d DERIVED (seed bound e0 = %.3e K, "
              "contraction M = %.3e 1/K, roundoff floor %.3e K; +1 "
              "margin trip) — replaces the retired literal %d"
              % (c1x["name"], c1x["K_NEWT"], kd["e0"], kd["M"],
                 kd["floor"], N_NEWT_INV))
        ok &= check("%s: derived K certifies the roundoff floor "
                    "in <= %d trips" % (c1x["name"], c1x["K_NEWT"]),
                    1 <= c1x["K_NEWT"] <= N_NEWT_INV + 2)
    # node-tie AMENDED index-identity control (V5): off-node probes
    # must agree EXACTLY with a searchsorted reference; node/±ulp
    # probes may differ by one interval and are VALUE-banded via the
    # C-A oracle below.
    n_g = len(Tg)
    Tg_j = jnp.asarray(Tg)
    T_off = jnp.asarray(Tg[:-1] + np.linspace(0.21, 0.79,
                                              n_g - 1) * dT)
    i_fl = jnp.clip(jnp.floor((T_off - Tg_j[0]) * (1.0 / dT))
                    .astype(jnp.int32), 0, n_g - 2)
    i_ss = jnp.clip(jnp.searchsorted(Tg_j, T_off, side="right") - 1,
                    0, n_g - 2)
    n_dis = int(jnp.sum(i_fl != i_ss))
    print("  off-node index identity (floor vs searchsorted): %d/%d "
          "disagreements" % (n_dis, n_g - 1))
    ok &= check("floor index == searchsorted off nodes", n_dis == 0)

    # ---------------- C-A (S24 thermo-survey condition, owner = THIS
    # X-THC1 touch): NASA-DIRECT EXACTNESS ORACLE — closure vs the
    # FIT ITSELF, not through the table. In the joint-free window
    # the NASA cp is QUARTIC => h is EXACTLY quintic (the a6 term is
    # constant in h) and the 4th-order cp' estimator is exact on
    # quartics => quintic-Hermite h/cp reproduce the fit at the
    # roundoff floor; s0 carries the ln T term => derived quintic-
    # Hermite remainder band |s0^(6)| D^6/46080 (s0^(6) = 120 Rg a1
    # / T^6) + roundoff.
    print("-- C-A: NASA-direct exactness oracle (in-window, "
          "off-node) --")
    a_bl, mixM_bl = A1.blend_nasa(tab_n["_sp"], tab_n["_x"])
    f_direct = A1.nasa_funcs(a_bl, mixM_bl, A1.RUNI_GENO)
    T_orc = np.linspace(Tg[0] + 0.37 * dT, Tg[-1] - 0.37 * dT, 2003)
    h_d, s_mol_d, cp_d = f_direct(T_orc)
    s0_dct = (s_mol_d - tab_n["_mixE"]) * 1000.0 / tab_n["_mixM"]
    To_j = jnp.asarray(T_orc)
    h_cl = np.asarray(jax.vmap(c1n["h"])(To_j))
    cp_cl = np.asarray(jax.vmap(c1n["cp"])(To_j))
    s0_cl = np.asarray(jax.vmap(c1n["s0"])(To_j))
    hscale_o = float(np.max(np.abs(h_d)))
    tol_h_o = C_OPS * EPS * hscale_o
    tol_cp_o = C_OPS * EPS * (60.0 * hscale_o / dT
                              + float(np.max(np.abs(cp_d))))
    Rg_m = float(tab_n["Rg"])
    a1_up = float(a_bl[0, 0])
    s6max = 120.0 * Rg_m * abs(a1_up) / float(Tg[0]) ** 6
    tol_s0_o = (K_RICH * s6max * dT ** 6 / 46080.0
                + C_OPS * EPS * float(np.max(np.abs(s0_dct))))
    e_h = float(np.max(np.abs(h_cl - h_d)))
    e_cp = float(np.max(np.abs(cp_cl - cp_d)))
    e_s0 = float(np.max(np.abs(s0_cl - s0_dct)))
    print("  |h - fit| %.3e (tol %.3e)  |cp - fit| %.3e (tol %.3e)  "
          "|s0 - fit| %.3e (tol %.3e)"
          % (e_h, tol_h_o, e_cp, tol_cp_o, e_s0, tol_s0_o))
    ok &= check("C-A: closure EXACT vs the NASA fit in-window "
                "(h/cp roundoff; s0 derived remainder)",
                e_h <= tol_h_o and e_cp <= tol_cp_o
                and e_s0 <= tol_s0_o)
    # node/±ulp value-band half of the tie control (via the oracle):
    T_tie = np.concatenate([Tg[1:-1],
                            np.nextafter(Tg[1:-1], np.inf),
                            np.nextafter(Tg[1:-1], -np.inf)])
    h_tie_d = f_direct(T_tie)[0]
    h_tie_cl = np.asarray(jax.vmap(c1n["h"])(jnp.asarray(T_tie)))
    e_tie = float(np.max(np.abs(h_tie_cl - h_tie_d)))
    print("  node/±ulp value band: max|h - fit| = %.3e (tol %.3e)"
          % (e_tie, tol_h_o))
    ok &= check("tie control: node/±ulp values inside the roundoff "
                "band (either-interval evaluation legal)",
                e_tie <= tol_h_o)

    # ---------------- R1: corrupted cp row -> invariant vs data breaks
    print("-- negative controls --")
    tab_bad = dict(tab_n)
    cp_bad = np.asarray(tab_n["cp"]).copy()
    i0 = len(cp_bad) // 2
    cp_bad[i0:i0 + 50] *= 1.001                  # 1e-3 band bump
    tab_bad["cp"] = jnp.asarray(cp_bad)
    c1b = build_c1(tab_bad)
    # the h-interpolant still carries the TRUE h data: the corrupted
    # cp shows up as an h'-vs-data-slope mismatch beyond the class band
    slope_data = np.diff(np.asarray(tab_n["h"])) / dT
    mid = jnp.asarray(Tg[:-1] + 0.5 * dT)
    hp_mid = jax.vmap(c1b["cp"])(mid)
    dev_bad = float(jnp.max(jnp.abs(hp_mid - jnp.asarray(slope_data))))
    hp_mid_ok = jax.vmap(c1n["cp"])(mid)
    dev_ok = float(jnp.max(jnp.abs(hp_mid_ok - jnp.asarray(slope_data))))
    band_slope = K_RICH * dT**2 * curv_h / 8.0 \
        + C_OPS * EPS * scale
    print("  [R1] midpoint |h' - data slope|: clean %.3e, corrupted "
          "%.3e (class band %.3e)" % (dev_ok, dev_bad, band_slope))
    ok &= check("R1 corrupted cp row detected",
                dev_ok <= band_slope and dev_bad > band_slope)

    # ---------------- R2: doctored non-monotone h detected
    tab_nm = dict(tab_n)
    h_nm = np.asarray(tab_n["h"]).copy()
    cp_nm = np.asarray(tab_n["cp"]).copy()
    h_nm[i0] = h_nm[i0 - 1] - 0.5 * (h_nm[i0 + 1] - h_nm[i0 - 1])
    cp_nm[i0] = -cp_nm[i0]                       # consistent doctoring
    tab_nm["h"], tab_nm["cp"] = jnp.asarray(h_nm), jnp.asarray(cp_nm)
    c1m = build_c1(tab_nm)
    cp_pr = jax.vmap(c1m["cp"])(Tp)
    ok &= check("R2 non-monotone doctored h detected",
                float(jnp.min(cp_pr)) - dip <= 0.0)

    # ---------------- R3: BZT-doctored table -> G floor breaks
    tab_bzt = dict(tab_n)
    cp_bz = np.asarray(tab_n["cp"]).copy()
    T_np = Tg
    bump = 0.35 * cp_bz * np.exp(-((T_np - 2400.0) / 12.0) ** 2)
    tab_bzt["cp"] = jnp.asarray(cp_bz + bump)    # sharp cp spike:
    c1z = build_c1(tab_bzt)                      # strong local gamma'
    Gz = G_of_T(c1z, Tp)
    Gz_min = float(jnp.min(Gz))
    dGz = float(jnp.max(jnp.abs(jnp.diff(Gz))))
    print("  [R3] BZT-doctored min G = %.4f (floor %.4f)"
          % (Gz_min, Gz_min - K_RICH * dGz))
    ok &= check("R3 BZT-doctored table detected (G floor violated)",
                Gz_min - K_RICH * dGz <= 0.0)

    # ---------------- R4: corrupted inverse -> roundtrip detects
    def bad_invert(c1x, ht):
        return jnp.interp(ht, c1x["hg"], c1x["Tg"]) * (1.0 + 1e-6)
    Tb = jax.vmap(lambda h: bad_invert(c1n, h))(hs)
    backb = jax.vmap(c1n["h"])(Tb)
    ok &= check("R4 corrupted inverse detected",
                float(jnp.max(jnp.abs(backb - hs))) > tol_rt)

    # ---------------- R5 (M3/V5): non-uniform grid must be REFUSED
    tab_nu = dict(tab_n)
    T_nu = Tg.copy()
    T_nu[len(T_nu) // 3] += 0.25 * dT            # one displaced node
    tab_nu["T"] = jnp.asarray(T_nu)
    fired_nu = False
    try:
        build_c1(tab_nu)
    except RuntimeError as e_nu:
        fired_nu = "uniformity" in str(e_nu)
        print("  [R5] refusal text: %s" % str(e_nu)[:90])
    ok &= check("R5 non-uniform grid REFUSED by the license rejector",
                fired_nu)

    # ---------------- R6 (M3/V5): corrupted-D floor index must
    # disagree with the searchsorted reference (the control that
    # proves the index-identity check CAN fire). CONTROL SIZED TO
    # ITS OWN DETECTION FLOOR (the S24 R-GRAD lesson, honored at
    # first firing of this carrier: a D corruption shifts probe i by
    # ~i*epsD intervals, so it is detectable only when the shift at
    # the far end exceeds the probes' distance to the interval
    # boundary — epsD is DERIVED from the measured probe geometry,
    # never a literal).
    # per-probe detectability: scaling D by (1+epsD) shifts probe k
    # (at interval i_k, fraction fr_k) DOWN by epsD*(i_k+fr_k)
    # intervals — it flips iff epsD > fr_k/(i_k+fr_k). The DERIVED
    # firing corruption = 2 x the MOST SENSITIVE probe's own floor
    # (exact per-probe formula — the first sizing used the global
    # boundary distance and ignored the fr<->i correlation of the
    # probe set: caught by this control's own first FAIL, declared).
    fr_off = np.asarray((T_off - Tg_j[0]) / dT) % 1.0
    i_off = np.arange(n_g - 1, dtype=float)
    sens = fr_off / (i_off + fr_off)
    epsD = 2.0 * float(np.min(sens))
    i_bad6 = jnp.clip(jnp.floor((T_off - Tg_j[0])
                                * (1.0 / (dT * (1.0 + epsD))))
                      .astype(jnp.int32), 0, n_g - 2)
    n_dis6 = int(jnp.sum(i_bad6 != i_ss))
    print("  [R6] corrupted-D (epsD = %.3e = 2 x min per-probe "
          "detectable rel-D error) index disagreements: %d/%d"
          % (epsD, n_dis6, n_g - 1))
    ok &= check("R6 corrupted-D control fires", n_dis6 > 0)

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
