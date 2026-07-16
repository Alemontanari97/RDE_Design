#!/usr/bin/env python3
"""G0 spike EXTENSION [F2-prep/G0, session S8]: axisymmetric source term +
fitted SHOCK POINT + first GENO cross-code interop brick. Twin of
validation/g0_spike_jax_moc.py (S5, untouched — its 52/52 record stands).

Three bricks, each with derived tolerances and negative controls:

(A) AXISYMMETRIC unit processes (interior + inverse wall): the planar
    compatibility invariants acquire the source term. Derived in-house from
    the potential-equation characteristic system (left-eigenvector route,
    planar limit re-verified symbolically in the derivation of record):
        along C+ (slope tan(th+al)):  d(th - nu) = -S+ dx,
        along C- (slope tan(th-al)):  d(th + nu) = +S- dx,
        S+- = delta * sin(th) sin(al) / (y cos(th +- al)),  delta = 1 axisym.
    VERIFICATION IS DUAL-ROUTE: the same unit process is implemented
    independently in the Zucrow-Hoffman conservative (u, v) compatibility
    form  du + lam_mp dv = delta a^2 v / (y (u^2 - a^2)) dx  (their Vol. 2
    Ch. 16 class), and the two routes must agree at the truncation order:
    the route-A/route-B solution difference must scale as ~h^3 under cell
    refinement (both schemes are second order). The scaling band [4, 16]
    per halving is STRUCTURAL (covers orders 2-4, centered on the expected
    8); a sign error in either source term makes the difference O(h)
    (ratio ~2) and is REJECTED — executable negative control included.

(B) SHOCK POINT as an implicit unit process on the Rankine-Hugoniot
    relations (oblique shock, deflection prescribed): z = [beta, M2] solves
    the theta-beta-M relation + RH normal-Mach relation, wrapped in
    custom_vjp with the implicit-function rule (never unrolled). This
    discharges P-B1/O3.1 AT THE SHOCK BRICK (Lemma B register,
    docs/rde_nozzle_P2_lemmaB.md): the reverse-mode adjoint of the fitted
    front satisfies the dot-product identity <w, dz/dp v> = <vjp(w), v>
    against FD directional derivatives with DERIVED tolerance. The
    Lax/Majda transversality of the front == nonsingularity of the local
    Jacobian J_k (Lemma B THEOREM, finite-dim): certified here by (i) the
    Lax inequalities M1n > 1, M2n < 1 with measured margins, (ii) the
    smallest singular value of J_k reported, (iii) NEGATIVE CONTROL at
    detachment (deflection > delta_max: J_k singular at the weak/strong
    merge point — Newton cannot certify, and the brick REJECTS).

(C) GENO CROSS-CODE INTEROP, first brick (gate-G0 criterion, user decision
    S5): FILE EXCHANGE with the GENO TOC case of record
    (GENO/CASES/tocnoz, READ-ONLY: GENO is Fortran and is never touched).
    From the committed reference contour "profile 30.0.dat" this script
    independently recomputes (1) throat radius/location, (2) exit area
    ratio, (3) the maximum wall angle, and cross-checks them against
    GENO's own input.ini (yt, eps) and performance.dat summary (maxtheta
    column, Veen format: type xtronc eps Cd Cf Isp mdot Slat maxtheta),
    with tolerances DERIVED from the contour grid spacing. Negative
    control: a corrupted (rescaled) contour is rejected. DECLARED LIMIT:
    the full O3.4 flowfield cross-code oracle needs the GENO binary
    (x/y/u/v/p.dat are checksummed in reference/ but not committed);
    no Fortran toolchain exists on this host (gfortran absent, verified
    S8) — the flowfield half stays in PROGRESS/NEXT for the G0 decision.

GAMMA STATUS (standing directive 2026-07-16): the unit-process and shock
STRUCTURE (implicit residual + adjoint solve + transversality) is
EOS-general; the Prandtl-Meyer and oblique-shock CLOSED FORMS used here
are gamma = const DECLARED ORACLE INSTANCES (known-answer closures for
the spike; the A1 engine replaces them with the gamma(T) backend and RH
on real thermo, M0 VI.2). gamma = 1.23 is the Rao-1961 spike regime of
record; the GENO tocnoz case is axisymmetric CH4/O2 frozen — the axisym
brick is exercised at wall angles up to the tocnoz maxtheta regime.

Exit code 0 iff ALL checks pass INCLUDING all negative controls.
"""
import os
import sys

import numpy as np
import jax
import jax.numpy as jnp

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENO_TOC = os.path.join(ROOT, "GENO", "CASES", "tocnoz")

# ----------------------------------------------------------------------
# gas closures (calorically perfect — DECLARED ORACLE instances, see header)
def nu_of_M(M, g):
    s = jnp.sqrt((g + 1.0) / (g - 1.0))
    m = jnp.sqrt(M * M - 1.0)
    return s * jnp.arctan(m / s) - jnp.arctan(m)


def alpha_of_M(M):
    return jnp.arcsin(1.0 / M)


def V_of_M(M, g):
    """Speed normalized by V_max (homentropic, gamma const)."""
    return 1.0 / jnp.sqrt(1.0 + 2.0 / ((g - 1.0) * M * M))


# ----------------------------------------------------------------------
# implicit-solve wrapper (identical mechanics to the S5 spike: custom_vjp
# + implicit-function rule on the transposed Jacobian, never unrolled)
N_NEWTON = 40


def _newton(resid_fn, z0, p):
    z = z0
    for _ in range(N_NEWTON):
        r = resid_fn(z, p)
        Jz = jax.jacfwd(resid_fn, argnums=0)(z, p)
        z = z - jnp.linalg.solve(Jz, r)
    return z


def make_implicit_solver(resid_fn):
    @jax.custom_vjp
    def solve(z0, p):
        return _newton(resid_fn, z0, p)

    def fwd(z0, p):
        z = _newton(resid_fn, z0, p)
        return z, (z, p)

    def bwd(res, zbar):
        z, p = res
        Jz = jax.jacfwd(resid_fn, argnums=0)(z, p)
        w = jnp.linalg.solve(Jz.T, zbar)
        _, vjp_p = jax.vjp(lambda pp: resid_fn(z, pp), p)
        (pbar,) = vjp_p(-w)
        return jnp.zeros_like(z), pbar

    solve.defvjp(fwd, bwd)
    return solve


# ----------------------------------------------------------------------
# derived-tolerance FD machinery (identical derivation to the S5 spike:
# two-step Richardson + roundoff floor; constants from the FD error
# balance, none tuned)
K_RICH = 4.0
C_FLOOR = 8.0
NEWTON_TOL_FACTOR = 100.0


def fd_jacobian(fn, p, h_scale=1.0):
    p = jnp.asarray(p)
    cols = []
    for i in range(p.size):
        m = max(1.0, abs(float(p[i]))) * h_scale
        h = EPS ** (1.0 / 3.0) * m
        e = jnp.zeros_like(p).at[i].set(1.0)
        cols.append((fn(p + h * e) - fn(p - h * e)) / (2.0 * h))
    return jnp.stack(cols, axis=1)


def check_process(name, solve, resid_fn, z0, p, corrupt=False):
    p = jnp.asarray(p)
    z = solve(z0, p)
    rnorm = float(jnp.max(jnp.abs(resid_fn(z, p))))
    rscale = max(1.0, float(jnp.max(jnp.abs(z))))
    ok_newton = rnorm <= NEWTON_TOL_FACTOR * EPS * rscale
    print("  [%s] Newton residual %.3e (tol %.3e): %s"
          % (name, rnorm, NEWTON_TOL_FACTOR * EPS * rscale,
             "PASS" if ok_newton else "FAIL"))

    fn = lambda pp: solve(z0, pp)
    J_ad = jax.jacrev(fn)(p)
    if corrupt:
        J_ad = J_ad * (1.0 + 1e-5) + 1e-5 * jnp.max(jnp.abs(J_ad))
    J_h = fd_jacobian(fn, p, h_scale=1.0)
    J_h2 = fd_jacobian(fn, p, h_scale=0.5)

    m = jnp.maximum(1.0, jnp.abs(p))[None, :]
    zscale = jnp.maximum(1.0, jnp.abs(z))[:, None]
    floor = C_FLOOR * EPS ** (2.0 / 3.0) * zscale / m
    tol = K_RICH * (jnp.abs(J_h - J_h2) + floor)
    err = jnp.abs(J_ad - J_h2)
    nbad = int(jnp.sum(err > tol))
    worst = float(jnp.max(err / tol))
    print("  [%s] |J_ad - J_fd| vs derived tol: %d/%d out, worst err/tol = %.3e"
          % (name, nbad, err.size, worst))
    return ok_newton, nbad == 0


# ======================================================================
# BRICK A — axisymmetric unit processes
# ======================================================================
# Route A residuals: (theta, nu) invariant form with average-coefficient
# source. delta = 1 (axisymmetric); delta = 0 must reduce to the planar
# spike EXACTLY (known-answer control below).
def _Splus(th, M, y):
    a = alpha_of_M(M)
    return jnp.sin(th) * jnp.sin(a) / (y * jnp.cos(th + a))


def _Sminus(th, M, y):
    a = alpha_of_M(M)
    return jnp.sin(th) * jnp.sin(a) / (y * jnp.cos(th - a))


def make_resid_interior_axi(delta):
    def resid(z, p):
        x4, y4, th4, M4 = z
        x1, y1, th1, M1, x2, y2, th2, M2, g = p
        nu1, nu2, nu4 = nu_of_M(M1, g), nu_of_M(M2, g), nu_of_M(M4, g)
        a1, a2, a4 = alpha_of_M(M1), alpha_of_M(M2), alpha_of_M(M4)
        sp = 0.5 * (_Splus(th1, M1, y1) + _Splus(th4, M4, y4))
        sm = 0.5 * (_Sminus(th2, M2, y2) + _Sminus(th4, M4, y4))
        return jnp.array([
            (th4 - nu4) - (th1 - nu1) + delta * sp * (x4 - x1),   # C+ compat
            (th4 + nu4) - (th2 + nu2) - delta * sm * (x4 - x2),   # C- compat
            (y4 - y1) - jnp.tan(0.5 * (th1 + th4) + 0.5 * (a1 + a4)) * (x4 - x1),
            (y4 - y2) - jnp.tan(0.5 * (th2 + th4) - 0.5 * (a2 + a4)) * (x4 - x2),
        ])
    return resid


# Route B residuals: Zucrow-Hoffman conservative (u, v) compatibility
# du + lam_mp dv = delta a^2 v / (y (u^2 - a^2)) dx along C+ (lam_mp =
# tan(th - al)) and du + lam_pl dv = same source along C- (lam_pl =
# tan(th + al)); independent algebra, same continuous content.
def make_resid_interior_axi_uv(delta):
    def uva(th, M, g):
        V = V_of_M(M, g)
        return V * jnp.cos(th), V * jnp.sin(th), V / M

    def resid(z, p):
        x4, y4, th4, M4 = z
        x1, y1, th1, M1, x2, y2, th2, M2, g = p
        u1, v1, c1 = uva(th1, M1, g)
        u2, v2, c2 = uva(th2, M2, g)
        u4, v4, c4 = uva(th4, M4, g)
        a1, a2, a4 = alpha_of_M(M1), alpha_of_M(M2), alpha_of_M(M4)
        lam_m = 0.5 * (jnp.tan(th1 - a1) + jnp.tan(th4 - a4))
        lam_p = 0.5 * (jnp.tan(th2 + a2) + jnp.tan(th4 + a4))
        s1 = c1 * c1 * v1 / (y1 * (u1 * u1 - c1 * c1))
        s2 = c2 * c2 * v2 / (y2 * (u2 * u2 - c2 * c2))
        s4 = c4 * c4 * v4 / (y4 * (u4 * u4 - c4 * c4))
        return jnp.array([
            (u4 - u1) + lam_m * (v4 - v1)
            - delta * 0.5 * (s1 + s4) * (x4 - x1),                # C+ compat
            (u4 - u2) + lam_p * (v4 - v2)
            - delta * 0.5 * (s2 + s4) * (x4 - x2),                # C- compat
            (y4 - y1) - jnp.tan(0.5 * (th1 + th4) + 0.5 * (a1 + a4)) * (x4 - x1),
            (y4 - y2) - jnp.tan(0.5 * (th2 + th4) - 0.5 * (a2 + a4)) * (x4 - x2),
        ])
    return resid


# axisymmetric inverse wall (C+ from interior point 1 to prescribed wall)
XW0 = 0.1


def wall_y(x, yw0, a, b):
    return yw0 + a * (x - XW0) + b * (x - XW0) ** 2


def wall_th(x, a, b):
    return jnp.arctan(a + 2.0 * b * (x - XW0))


def make_resid_wall_axi(delta):
    def resid(z, p):
        x4, M4 = z
        x1, y1, th1, M1, yw0, a, b, g = p
        th4 = wall_th(x4, a, b)
        y4 = wall_y(x4, yw0, a, b)
        nu1, nu4 = nu_of_M(M1, g), nu_of_M(M4, g)
        a1, a4 = alpha_of_M(M1), alpha_of_M(M4)
        sp = 0.5 * (_Splus(th1, M1, y1) + _Splus(th4, M4, y4))
        return jnp.array([
            (th4 - nu4) - (th1 - nu1) + delta * sp * (x4 - x1),
            (y4 - y1)
            - jnp.tan(0.5 * (th1 + th4) + 0.5 * (a1 + a4)) * (x4 - x1),
        ])
    return resid


def brick_A():
    print("== BRICK A: axisymmetric unit processes (source term, dual-route) ==")
    g = 1.23
    d2r = jnp.pi / 180.0
    ok = True

    p_int = [0.00, 0.50, 8.0 * d2r, 2.20,
             0.05, 0.90, 4.0 * d2r, 2.35, g]
    z0_int = jnp.array([0.30, 0.70, 6.0 * d2r, 2.30])

    # A.1 known-answer control: delta = 0 must equal the PLANAR residual
    # of the S5 spike exactly (same algebra path, source multiplied out).
    r_axi0 = make_resid_interior_axi(0.0)(z0_int, jnp.asarray(p_int))
    # planar residual re-stated inline (verbatim S5 spike form):
    def resid_planar(z, p):
        x4, y4, th4, M4 = z
        x1, y1, th1, M1, x2, y2, th2, M2, gg = p
        nu1, nu2, nu4 = nu_of_M(M1, gg), nu_of_M(M2, gg), nu_of_M(M4, gg)
        a1, a2, a4 = alpha_of_M(M1), alpha_of_M(M2), alpha_of_M(M4)
        return jnp.array([
            (th4 - nu4) - (th1 - nu1),
            (th4 + nu4) - (th2 + nu2),
            (y4 - y1) - jnp.tan(0.5 * (th1 + th4) + 0.5 * (a1 + a4)) * (x4 - x1),
            (y4 - y2) - jnp.tan(0.5 * (th2 + th4) - 0.5 * (a2 + a4)) * (x4 - x2),
        ])
    r_pla = resid_planar(z0_int, jnp.asarray(p_int))
    d0 = float(jnp.max(jnp.abs(r_axi0 - r_pla)))
    ok_red = d0 == 0.0
    print("  [planar-reduction] max|resid(delta=0) - resid_planar| = %.1e: %s"
          % (d0, "PASS" if ok_red else "FAIL"))
    ok &= ok_red

    # A.2 axisym interior: Newton + gradient vs FD (derived tol)
    solve_axi = make_implicit_solver(make_resid_interior_axi(1.0))
    a_, b_ = check_process("interior-axi", solve_axi,
                           make_resid_interior_axi(1.0), z0_int, p_int)
    ok &= a_ and b_

    # A.3 axisym inverse wall: Newton + gradient vs FD (derived tol)
    p_wal = [0.10, 0.80, 10.0 * d2r, 2.30,
             1.00, 0.212557, -0.50, g]
    z0_wal = jnp.array([0.25, 2.30])
    solve_wal = make_implicit_solver(make_resid_wall_axi(1.0))
    a_, b_ = check_process("inverse-wall-axi", solve_wal,
                           make_resid_wall_axi(1.0), z0_wal, p_wal)
    ok &= a_ and b_

    # A.4 DUAL-ROUTE order-scaling test (the source-term rejector).
    # Shrink the cell by factors 1, 1/2, 1/4 around point 1; route-A vs
    # route-B solved-point difference must scale ~h^3 (both schemes 2nd
    # order): per halving, ratio in the STRUCTURAL band [4, 16]
    # (covers orders 2-4; a source sign error gives O(h) difference,
    # ratio ~2 -> REJECTED).
    solve_A = make_implicit_solver(make_resid_interior_axi(1.0))
    solve_B = make_implicit_solver(make_resid_interior_axi_uv(1.0))
    resid_A_ref = make_resid_interior_axi(1.0)
    resid_B_ref = make_resid_interior_axi_uv(1.0)

    def cell(hs):
        x1, y1, th1, M1 = 0.00, 0.50, 8.0 * d2r, 2.20
        x2 = x1 + hs * 0.05
        y2 = y1 + hs * 0.40
        th2 = th1 + hs * (-4.0 * d2r)
        M2 = M1 + hs * 0.15
        return jnp.array([x1, y1, th1, M1, x2, y2, th2, M2, g])

    def diff_at(hs):
        p = cell(hs)
        z0 = jnp.array([float(p[0]) + 0.2 * hs + 0.05,
                        float(p[1]) + 0.2 * hs,
                        float(p[2]), float(p[3])])
        zA = solve_A(z0, p)
        zB = solve_B(z0, p)
        # certify both Newtons before trusting the difference; a Newton
        # that cannot certify is itself a REJECTION of that route
        rA = float(jnp.max(jnp.abs(resid_A_ref(zA, p))))
        rB = float(jnp.max(jnp.abs(resid_B_ref(zB, p))))
        if not (rA < NEWTON_TOL_FACTOR * EPS and rB < NEWTON_TOL_FACTOR * EPS):
            return None
        return float(jnp.max(jnp.abs(zA - zB)))

    def scaling_verdict(route_name, solve_B_used, resid_B_used):
        nonlocal solve_B, resid_B_ref
        solve_B = solve_B_used
        resid_B_ref = resid_B_used
        ds = [diff_at(1.0), diff_at(0.5), diff_at(0.25)]
        if any(d is None for d in ds):
            print("  [dual-route %s] Newton NOT certified on some cell -> "
                  "FAIL (route rejected)" % route_name)
            return False
        d1, d2_, d4 = ds
        r12, r24 = d1 / d2_, d2_ / d4
        in_band = (4.0 <= r12 <= 16.0) and (4.0 <= r24 <= 16.0)
        print("  [dual-route %s] |zA-zB| = %.3e / %.3e / %.3e, "
              "ratios %.2f, %.2f (band [4,16]): %s"
              % (route_name, d1, d2_, d4, r12, r24,
                 "PASS" if in_band else "FAIL"))
        return in_band

    ok &= scaling_verdict("clean",
                          make_implicit_solver(make_resid_interior_axi_uv(1.0)),
                          make_resid_interior_axi_uv(1.0))

    # A.5 NEGATIVE CONTROL: flip the source sign in route B -> the
    # difference becomes O(h) (ratio ~2), the band test MUST fail (a
    # non-certifying Newton on the corrupted route is also a rejection).
    rejected = not scaling_verdict(
        "SIGN-CORRUPTED",
        make_implicit_solver(make_resid_interior_axi_uv(-1.0)),
        make_resid_interior_axi_uv(-1.0))
    print("  [negative control] corrupted source sign rejected: %s"
          % ("PASS" if rejected else "FAIL (test cannot reject!)"))
    ok &= rejected

    # A.6 NEGATIVE CONTROL: corrupted vjp on the axisym interior
    _, clean = check_process("interior-axi-CORRUPTED", solve_axi,
                             make_resid_interior_axi(1.0), z0_int, p_int,
                             corrupt=True)
    rej2 = not clean
    print("  [negative control] corrupted vjp rejected: %s"
          % ("PASS" if rej2 else "FAIL (test cannot reject!)"))
    ok &= rej2
    return ok


# ======================================================================
# BRICK B — fitted shock point (RH implicit + Lax/Majda transversality)
# ======================================================================
def resid_shock(z, p):
    """Oblique shock, deflection prescribed: z = [beta, M2],
    p = [M1, defl, g]. R1 = theta-beta-M; R2 = RH normal-Mach relation.
    Weak branch selected by the initial guess; Lax/Majda == J_k
    nonsingular fails exactly at detachment (weak/strong merge)."""
    beta, M2 = z
    M1, defl, g = p
    M1n2 = (M1 * jnp.sin(beta)) ** 2
    R1 = jnp.tan(defl) - 2.0 / jnp.tan(beta) * (M1n2 - 1.0) / (
        M1 * M1 * (g + jnp.cos(2.0 * beta)) + 2.0)
    M2n2 = (1.0 + 0.5 * (g - 1.0) * M1n2) / (g * M1n2 - 0.5 * (g - 1.0))
    R2 = M2 - jnp.sqrt(M2n2) / jnp.sin(beta - defl)
    return jnp.array([R1, R2])


def delta_max_of(M1, g):
    """Max deflection over the attached-shock family (numpy scan +
    parabolic refinement; used only to PLACE the negative control)."""
    mu = float(np.arcsin(1.0 / M1))
    betas = np.linspace(mu * (1.0 + 1e-6), np.pi / 2.0 * (1.0 - 1e-6), 4001)
    M1n2 = (M1 * np.sin(betas)) ** 2
    defl = np.arctan(2.0 / np.tan(betas) * (M1n2 - 1.0) /
                     (M1 * M1 * (g + np.cos(2.0 * betas)) + 2.0))
    i = int(np.argmax(defl))
    return float(defl[i]), float(betas[i])


def brick_B():
    print("== BRICK B: fitted shock point (RH implicit, Lax/Majda == J_k) ==")
    g = 1.23
    d2r = np.pi / 180.0
    ok = True

    M1, defl = 2.20, 10.0 * d2r
    mu = float(np.arcsin(1.0 / M1))
    p_sh = jnp.array([M1, defl, g])
    z0_sh = jnp.array([mu + 1.3 * defl, 0.9 * M1])   # weak-branch guess
    solve_sh = make_implicit_solver(resid_shock)

    # B.1 Newton + full-Jacobian gradient check (derived tol)
    a_, b_ = check_process("shock", solve_sh, resid_shock, z0_sh, p_sh)
    ok &= a_ and b_
    z = solve_sh(z0_sh, p_sh)
    beta, M2 = float(z[0]), float(z[1])

    # B.2 Lax certificate: M1n > 1 (front supersonic upstream) and
    # M2n < 1 (subsonic downstream normal) with measured margins.
    M1n = M1 * np.sin(beta)
    M2n = M2 * np.sin(beta - defl)
    lax_ok = (M1n > 1.0) and (M2n < 1.0)
    print("  [shock] beta = %.4f deg, M2 = %.4f; Lax margins: M1n-1 = %+.4f, "
          "1-M2n = %+.4f: %s" % (beta / d2r, M2, M1n - 1.0, 1.0 - M2n,
                                 "PASS" if lax_ok else "FAIL"))
    ok &= lax_ok

    # B.3 transversality margin: smallest singular value of J_k at the
    # solution (Lemma B: Lax/Majda == J_k nonsingular).
    Jk = jax.jacfwd(resid_shock, argnums=0)(z, p_sh)
    smin_reg = float(jnp.linalg.svd(Jk, compute_uv=False)[-1])
    print("  [shock] transversality margin sigma_min(J_k) = %.4e" % smin_reg)

    # B.4 DOT-PRODUCT identity (O3.1 at the shock brick, discharges P-B1
    # at brick level): <w, dz/dp v> vs <vjp(w), v>, forward side by
    # central FD with the same Richardson-derived tolerance machinery.
    fn = lambda pp: solve_sh(z0_sh, pp)
    rng_v = jnp.array([0.7, -0.4, 0.2])      # fixed test directions
    rng_w = jnp.array([0.6, 0.8])            # (any nonzero pair works;
    #                                           values are structural)
    def dirder(hsc):
        m = 1.0 * hsc
        h = EPS ** (1.0 / 3.0) * m
        return (fn(p_sh + h * rng_v) - fn(p_sh - h * rng_v)) / (2.0 * h)
    dv_h, dv_h2 = dirder(1.0), dirder(0.5)
    lhs = float(rng_w @ dv_h2)
    _, vjp_fn = jax.vjp(fn, p_sh)
    (JTw,) = vjp_fn(rng_w)
    rhs = float(JTw @ rng_v)
    tol_dp = K_RICH * (abs(float(rng_w @ (dv_h - dv_h2)))
                       + C_FLOOR * EPS ** (2.0 / 3.0))
    err_dp = abs(lhs - rhs)
    dp_ok = err_dp <= tol_dp
    print("  [O3.1 dot-product] |<w,Jv> - <J^Tw,v>| = %.3e (tol %.3e): %s"
          % (err_dp, tol_dp, "PASS" if dp_ok else "FAIL"))
    ok &= dp_ok

    # B.5 NEGATIVE CONTROL (corrupted vjp must break O3.1)
    lhs_c = lhs
    rhs_c = float((JTw * (1.0 + 1e-5) + 1e-5 * jnp.max(jnp.abs(JTw))) @ rng_v)
    rej_dp = abs(lhs_c - rhs_c) > tol_dp
    print("  [negative control] corrupted vjp breaks O3.1: %s"
          % ("PASS" if rej_dp else "FAIL (test cannot reject!)"))
    ok &= rej_dp

    # B.6 NEGATIVE CONTROL (Lax/Majda): deflection beyond detachment —
    # no attached solution exists, J_k is singular at the weak/strong
    # merge, Newton CANNOT certify. The brick must REJECT.
    dmax, beta_dmax = delta_max_of(M1, g)
    p_bad = jnp.array([M1, 1.02 * dmax, g])
    z_bad = _newton(resid_shock, z0_sh, p_bad)
    r_bad = float(jnp.max(jnp.abs(resid_shock(z_bad, p_bad))))
    detach_rejected = not (np.isfinite(r_bad)
                           and r_bad <= NEWTON_TOL_FACTOR * EPS)
    print("  [negative control] defl = 1.02*delta_max (%.2f deg): residual "
          "%.3e NOT certified -> rejected: %s"
          % (1.02 * dmax / d2r, r_bad,
             "PASS" if detach_rejected else "FAIL (test cannot reject!)"))
    ok &= detach_rejected

    # B.7 transversality collapse toward detachment (executable Lemma-B
    # correspondence): detachment is a FOLD of the theta-beta-M relation,
    # so the transversality margin degenerates with exponent 1/2:
    # sigma_min(J_k) ~ C * sqrt(1 - defl/delta_max). DERIVED scaling
    # test: measure sigma_min at e = 1e-2 and e = 2.5e-3 (ratio 4 in e);
    # the sigma ratio must be 4^p with p in the structural band
    # [0.25, 0.75] centered on the fold exponent 1/2, i.e. ratio in
    # [4^0.25, 4^0.75]. A non-degenerating Jacobian (p = 0, ratio ~1)
    # is rejected by construction.
    def smin_at(e):
        p_near = jnp.array([M1, (1.0 - e) * dmax, g])
        z_g = jnp.array([beta_dmax * (1.0 - 0.3 * np.sqrt(e)), 0.7 * M1])
        z_n = _newton(resid_shock, z_g, p_near)
        r_n = float(jnp.max(jnp.abs(resid_shock(z_n, p_near))))
        if not (r_n <= NEWTON_TOL_FACTOR * EPS
                and float(z_n[0]) < beta_dmax):
            return None
        Jn = jax.jacfwd(resid_shock, argnums=0)(z_n, p_near)
        return float(jnp.linalg.svd(Jn, compute_uv=False)[-1])

    s1, s2 = smin_at(1e-2), smin_at(2.5e-3)
    if s1 is None or s2 is None:
        print("  [transversality collapse] weak-branch Newton not "
              "certified near the fold: FAIL")
        ok = False
    else:
        ratio = s1 / s2
        lo, hi = 4.0 ** 0.25, 4.0 ** 0.75
        fold_ok = lo <= ratio <= hi
        print("  [transversality collapse] sigma_min(e=1e-2) = %.3e, "
              "sigma_min(e=2.5e-3) = %.3e, ratio %.3f (fold band "
              "[%.3f, %.3f], exponent ~1/2): %s"
              % (s1, s2, ratio, lo, hi, "PASS" if fold_ok else "FAIL"))
        ok &= fold_ok
    return ok


# ======================================================================
# BRICK C — GENO TOC cross-code interop (file exchange, READ-ONLY)
# ======================================================================
def _read_profile(path):
    xy = np.loadtxt(path)
    return xy[:, 0], xy[:, 1]


def brick_C():
    print("== BRICK C: GENO tocnoz interop (file exchange, read-only) ==")
    prof = os.path.join(GENO_TOC, "ch16_ref", "profile 30.0.dat")
    perf = os.path.join(GENO_TOC, "ch16_ref", "performance.dat")
    ini = os.path.join(GENO_TOC, "input.ini")
    if not (os.path.exists(prof) and os.path.exists(perf)
            and os.path.exists(ini)):
        print("  GENO tocnoz reference not found -> SKIP (declared)")
        return True

    # parse GENO artifacts (independent parsers; GENO untouched)
    x, y = _read_profile(prof)
    row = np.loadtxt(perf)
    # Veen performance format: type xtronc eps Cd Cf Isp mdot Slat maxtheta
    eps_ini = yt_ini = None
    for line in open(ini, encoding="utf-8"):
        s = line.strip().replace(" ", "")
        if s.startswith("eps="):
            eps_ini = float(s.split("=")[1])
        if s.startswith("yt="):
            yt_ini = float(s.split("=")[1])
    maxtheta_geno = float(row[-1])
    eps_geno = float(row[2])
    ok = True

    d2r = np.pi / 180.0
    # C.1 throat: min radius vs yt (tolerance = local grid resolution:
    # y is quadratic at the throat, error <= curvature * (dx/2)^2 with
    # curvature 1/rtd from the ini circle; conservative structural bound
    # = one grid step of the neighboring y-differences)
    i_t = int(np.argmin(y))
    dx_loc = np.max(np.abs(np.diff(x[max(0, i_t - 2):i_t + 3])))
    dy_step = np.max(np.abs(np.diff(y[max(0, i_t - 2):i_t + 3])))
    tol_t = dy_step + dx_loc ** 2
    err_t = abs(float(y[i_t]) - yt_ini)
    t_ok = err_t <= tol_t
    print("  [throat] min y = %.6f at x = %.4f vs yt(ini) = %.3f "
          "(err %.2e, tol %.2e): %s"
          % (y[i_t], x[i_t], yt_ini, err_t, tol_t, "PASS" if t_ok else "FAIL"))
    ok &= t_ok

    # C.2 exit area ratio: y_end^2/yt^2 vs eps (both ini and performance
    # col 3 must agree). Tolerance derived from the endpoint slope and
    # last grid step: |d(y^2)| <= 2 y_e tan(theta_e) dx_last.
    eps_prof = float(y[-1] ** 2 / yt_ini ** 2)
    th_e = np.arctan((y[-1] - y[-2]) / (x[-1] - x[-2]))
    dx_last = float(abs(x[-1] - x[-3]))
    tol_e = 2.0 * float(y[-1]) * np.tan(th_e) * dx_last / yt_ini ** 2
    e_ok = (abs(eps_prof - eps_ini) <= tol_e
            and abs(eps_geno - eps_ini) == 0.0)
    print("  [eps] contour %.4f vs ini %.1f vs performance %.1f "
          "(err %.3f, derived tol %.3f): %s"
          % (eps_prof, eps_ini, eps_geno, abs(eps_prof - eps_ini), tol_e,
             "PASS" if e_ok else "FAIL"))
    ok &= e_ok

    # C.3 max wall angle: central-difference recomputation from the
    # contour vs GENO's own maxtheta (performance col 9, degrees).
    # Derived tolerance: FD angle error ~ |Delta theta| between adjacent
    # central-difference samples around the max (curvature term), plus
    # the half-grid phase error; both measured from the file itself.
    thw = np.arctan(np.gradient(y, x))
    i_m = int(np.argmax(thw))
    th_max = float(thw[i_m] / d2r)
    dth_loc = float(np.max(np.abs(np.diff(
        thw[max(0, i_m - 3):i_m + 4])))) / d2r
    tol_th = 2.0 * dth_loc + 4.0 * EPS ** (1.0 / 3.0) / d2r
    err_th = abs(th_max - maxtheta_geno)
    th_ok = err_th <= tol_th
    print("  [maxtheta] recomputed %.4f deg vs GENO %.4f deg "
          "(err %.3f, derived tol %.3f): %s"
          % (th_max, maxtheta_geno, err_th, tol_th,
             "PASS" if th_ok else "FAIL"))
    ok &= th_ok

    # C.4 NEGATIVE CONTROL: a rescaled contour (wrong units/semantics)
    # must be REJECTED by the eps cross-check.
    y_bad = y * 1.05
    eps_bad = float(y_bad[-1] ** 2 / yt_ini ** 2)
    rej = abs(eps_bad - eps_ini) > tol_e
    print("  [negative control] 5%%-rescaled contour rejected by eps "
          "check (err %.3f > tol %.3f): %s"
          % (abs(eps_bad - eps_ini), tol_e,
             "PASS" if rej else "FAIL (test cannot reject!)"))
    ok &= rej

    print("  [declared limit] full O3.4 flowfield cross-check needs the "
          "GENO binary (x/y/u/v/p.dat not committed; gfortran absent on "
          "this host) -> stays in PROGRESS/NEXT for the G0 decision.")
    return ok


def main():
    print("== G0 spike EXTENSION: axisym + shock + GENO interop (JAX %s) =="
          % jax.__version__)
    ok = True
    ok &= brick_A()
    ok &= brick_B()
    ok &= brick_C()
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
