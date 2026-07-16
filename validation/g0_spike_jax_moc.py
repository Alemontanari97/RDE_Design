#!/usr/bin/env python3
"""G0 spike [F2-prep/G0, 90-day plan item 2]: ONE differentiable MOC unit
process pair (interior point + inverse/design-mode wall point) in JAX with
custom_vjp + implicit-function rule, gradient-checked against central
finite differences with a DERIVED tolerance (two-step Richardson error
estimate, no magic numbers) and a NEGATIVE CONTROL that must be REJECTED.

Purpose: instruct gate G0 (JAX vs Julia stack decision, D6) — this spike
demonstrates (a) implicit-diff custom_vjp mechanics on Newton-solved unit
processes (never unrolled, per M0 VI.3), (b) machine-precision-grade
gradient agreement, (c) rejector discipline. It is NOT the A1 engine.

Physics scope (declared): planar (delta = 0), irrotational, homentropic,
CALORICALLY PERFECT gas — the closed-form Prandtl-Meyer function nu(M; g)
is gamma-const-only. GAMMA STATUS (standing directive 2026-07-16): the
unit-process STRUCTURE (implicit residual + adjoint solve) is EOS-general;
only the PM closure is gamma = const — the A1 engine replaces it with the
gamma(T) backend (M0 VI.2). Representative states: gamma = 1.23, M ~ 2.2-2.4
(the Rao-1961 spike Table-1 oracle regime, D2 §b0).

Dual-code note (user decision 2026-07-16): GENO stays Fortran; the
differentiable engine is NEW code with GENO as independent reference
(O3.4 cross-code oracle) — this spike is the first feasibility brick and
must not (and does not) touch GENO.

Exit code 0 iff ALL checks pass INCLUDING the negative control rejection.
"""
import sys

import jax
import jax.numpy as jnp

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)


# ----------------------------------------------------------------------
# gas relations (calorically perfect; see gamma-status note in docstring)
def nu_of_M(M, g):
    """Prandtl-Meyer angle."""
    s = jnp.sqrt((g + 1.0) / (g - 1.0))
    m = jnp.sqrt(M * M - 1.0)
    return s * jnp.arctan(m / s) - jnp.arctan(m)


def alpha_of_M(M):
    """Mach angle."""
    return jnp.arcsin(1.0 / M)


# ----------------------------------------------------------------------
# implicit-solve wrapper: z solves R(z, p) = 0; reverse rule by the
# implicit function theorem (adjoint solve on the transposed Jacobian),
# NEVER differentiating through the Newton iterations.
N_NEWTON = 40  # fixed iteration budget; convergence ASSERTED by caller


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
        w = jnp.linalg.solve(Jz.T, zbar)          # Jz^T w = zbar
        _, vjp_p = jax.vjp(lambda pp: resid_fn(z, pp), p)
        (pbar,) = vjp_p(-w)                       # pbar = -Jp^T w
        return jnp.zeros_like(z), pbar

    solve.defvjp(fwd, bwd)
    return solve


# ----------------------------------------------------------------------
# unit process 1: INTERIOR POINT (planar MOC, average-coefficient form)
# Zucrow/GENO convention: C- slope tan(theta - alpha), C+ slope
# tan(theta + alpha). Point 4 from point 1 (C+ up-right) and point 2
# (C- down-right). Unknowns z = [x4, y4, th4, M4];
# params p = [x1, y1, th1, M1, x2, y2, th2, M2, gamma].
def resid_interior(z, p):
    x4, y4, th4, M4 = z
    x1, y1, th1, M1, x2, y2, th2, M2, g = p
    nu1, nu2, nu4 = nu_of_M(M1, g), nu_of_M(M2, g), nu_of_M(M4, g)
    a1, a2, a4 = alpha_of_M(M1), alpha_of_M(M2), alpha_of_M(M4)
    return jnp.array([
        (th4 - nu4) - (th1 - nu1),                                # C+ invariant
        (th4 + nu4) - (th2 + nu2),                                # C- invariant
        (y4 - y1) - jnp.tan(0.5 * (th1 + th4) + 0.5 * (a1 + a4)) * (x4 - x1),
        (y4 - y2) - jnp.tan(0.5 * (th2 + th4) - 0.5 * (a2 + a4)) * (x4 - x2),
    ])


# ----------------------------------------------------------------------
# unit process 2: WALL POINT, inverse/design mode (wall PRESCRIBED,
# flow computed — the pipeline's contour-evaluation brick). Wall
# y_w(x) = yw0 + a (x - xw0) + b (x - xw0)^2, slip: th4 = atan(y_w'(x4)).
# C+ from interior point 1 to the wall. Unknowns z = [x4, M4];
# params p = [x1, y1, th1, M1, yw0, a, b, gamma]  (xw0 fixed datum).
XW0 = 0.1


def wall_y(x, yw0, a, b):
    return yw0 + a * (x - XW0) + b * (x - XW0) ** 2


def wall_th(x, a, b):
    return jnp.arctan(a + 2.0 * b * (x - XW0))


def resid_wall(z, p):
    x4, M4 = z
    x1, y1, th1, M1, yw0, a, b, g = p
    th4 = wall_th(x4, a, b)
    nu1, nu4 = nu_of_M(M1, g), nu_of_M(M4, g)
    a1, a4 = alpha_of_M(M1), alpha_of_M(M4)
    return jnp.array([
        (th4 - nu4) - (th1 - nu1),                                # C+ invariant
        (wall_y(x4, yw0, a, b) - y1)
        - jnp.tan(0.5 * (th1 + th4) + 0.5 * (a1 + a4)) * (x4 - x1),
    ])


# ----------------------------------------------------------------------
# derived-tolerance gradient check.
# Central FD at steps h and h/2; Richardson: err(fd_h2) ~ trunc(h)/4 +
# roundoff, and |fd_h - fd_h2| ~ (3/4) trunc(h), so err(fd_h2) <~
# |fd_h - fd_h2| / 3 + roundoff-floor. Tolerance = K * (|fd_h - fd_h2| +
# floor) with K = 4 (covers the 1/3 factor with margin ~12x) and
# floor = 8 eps^(2/3) * zscale / m (FD roundoff 2 eps |z| / h at
# h = eps^(1/3) m, safety 4). All constants derived from the FD error
# balance — none tuned to make the test pass.
K_RICH = 4.0
C_FLOOR = 8.0
NEWTON_TOL_FACTOR = 100.0  # residual <= 100 eps scale: Newton certified


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
    # Newton convergence rejector (derived: solve() must certify itself)
    rnorm = float(jnp.max(jnp.abs(resid_fn(z, p))))
    rscale = max(1.0, float(jnp.max(jnp.abs(z))))
    ok_newton = rnorm <= NEWTON_TOL_FACTOR * EPS * rscale
    print("  [%s] Newton residual %.3e (tol %.3e): %s"
          % (name, rnorm, NEWTON_TOL_FACTOR * EPS * rscale,
             "PASS" if ok_newton else "FAIL"))

    fn = lambda pp: solve(z0, pp)
    J_ad = jax.jacrev(fn)(p)                      # uses the custom bwd
    if corrupt:                                   # negative control
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
    print("  [%s] |J_ad - J_fd| vs derived tol: %d/%d entries out, "
          "worst err/tol = %.3e" % (name, nbad, err.size, worst))
    return ok_newton, nbad == 0


def main():
    g = 1.23
    d2r = jnp.pi / 180.0
    ok = True

    print("== G0 spike: differentiable MOC unit processes (JAX %s) =="
          % jax.__version__)

    # interior point, TOC-regime states
    p_int = [0.00, 0.50, 8.0 * d2r, 2.20,
             0.05, 0.90, 4.0 * d2r, 2.35, g]
    z0_int = jnp.array([0.30, 0.70, 6.0 * d2r, 2.30])
    solve_int = make_implicit_solver(resid_interior)
    a, b = check_process("interior", solve_int, resid_interior, z0_int, p_int)
    ok &= a and b

    # inverse/design-mode wall point
    p_wal = [0.10, 0.80, 10.0 * d2r, 2.30,
             1.00, 0.212557, -0.50, g]          # a = tan(12 deg)
    z0_wal = jnp.array([0.25, 2.30])
    solve_wal = make_implicit_solver(resid_wall)
    a, b = check_process("inverse-wall", solve_wal, resid_wall, z0_wal, p_wal)
    ok &= a and b

    # NEGATIVE CONTROL: a corrupted adjoint MUST be rejected
    _, clean = check_process("interior-CORRUPTED", solve_int, resid_interior,
                             z0_int, p_int, corrupt=True)
    rejected = not clean
    print("  [negative control] corrupted vjp rejected: %s"
          % ("PASS" if rejected else "FAIL (test cannot reject!)"))
    ok &= rejected

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
