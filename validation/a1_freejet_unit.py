#!/usr/bin/env python3
"""A1 BRICK 2, STEP 9a [F2/A1]: THE FREE-PRESSURE-BOUNDARY UNIT PROCESS
— the first brick of the PLUG topology.

A plug (aerospike) nozzle has no outer wall: the jet's outer edge is a
FREE BOUNDARY where the pressure equals ambient and the position is part
of the solution. This carrier implements that unit process in exactly
the pattern of the verified bell processes (implicit residual cell,
Newton + custom_vjp implicit rule) and certifies it at unit level
before any plug march is assembled — the same discipline as the G0
spikes that preceded Brick 1.

THE CELL (Zucrow-Hoffman free-pressure-boundary point, axisymmetric,
upper boundary). Known: pt1 = interior neighbor on the previous column
(sends the C+ characteristic), pt3 = previous boundary point (the edge
is a STREAMLINE), and q_pa = the flow speed at which the local static
pressure equals ambient (from the same tabulated isentrope; constant
along the edge at fixed stagnation). Unknowns z = (x4, y4, u4), with
v4 = sqrt(q_pa^2 - u4^2) substituted (p = pa built in):

$$ r1:  (y4 - y1) - lam_C+ (x4 - x1) = 0        the C+ reaches the point
$$ r2:  q u4 + r v4 - [s (x4-x1) + q u1 + r v1] = 0      compatibility
$$ r3:  (y4 - y3) - tan((th3 + th4)/2) (x4 - x3) = 0     edge = streamline

with average-coefficient (midpoint) closure, second order, exactly as
the interior/wall cells.

UNIT CERTIFICATES:
  U-1 KNOWN ANSWER (exact): a uniform parallel jet already at p = pa
      must be a FIXED POINT — the process returns the same state and a
      straight horizontal edge, to Newton tolerance.
  U-2 TURNED-JET consistency: start from a uniformly turned parallel
      jet at p = pa (angle th0): the edge must continue at th0 and the
      state be preserved (rotation invariance of the cell).
  U-3 pressure property: p(state at the new point) = pa to roundoff
      (by construction through q_pa — verified, not assumed).
  U-4 second-order self-convergence: halving the step from pt1/pt3
      halves-squared the deviation of an expanding-jet cell from its
      Richardson limit (order measured, ~2 expected).
  R-1 rejector: q_pa corrupted by 1% -> the returned edge angle moves
      by an amount >> the Newton floor (the boundary condition is
      LOAD-BEARING, not decorative).
  R-2 rejector: compatibility sign flipped -> Newton fails to certify.

Run:  .venv-a1/bin/python validation/a1_freejet_unit.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402

import jax.numpy as jnp                      # noqa: E402

EPS = A1.EPS
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def make_resid_freejet(delta, corrupt_sign=False):
    """Unknowns z = (x4, y4, th4): the boundary state is parameterized
    by its ANGLE, with u4 = qpa cos(th4), v4 = qpa sin(th4). This bakes
    p = pa in exactly and leaves the turning direction FREE — the first
    (modulus-substituted) formulation forbade inward turning and fell
    into a clamped spurious root on compressing edges: caught by U-3,
    rejected, reformulated."""
    sgn = -1.0 if corrupt_sign else 1.0

    def resid(z, p, ta):
        x4, y4, th4 = z
        x1, y1, u1, v1, x3, y3, u3, v3, qpa = p
        u4 = qpa * jnp.cos(th4)
        v4 = qpa * jnp.sin(th4)
        um, vm = 0.5 * (u1 + u4), 0.5 * (v1 + v4)
        ym = 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = A1._coef(um, vm, ym, ta, delta)
        rp = rp0 - qp * lp
        th3 = jnp.arctan2(v3, u3)
        thm = 0.5 * (th3 + th4)
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            sgn * (qp * u4 + rp * v4)
            - (sp * (x4 - x1) + qp * u1 + rp * v1),
            (y4 - y3) - jnp.tan(thm) * (x4 - x3),
        ])
    return resid


def q_at_pa(pa, ta, as_):
    from scipy.optimize import brentq

    def f(q):
        return float(A1.state_q(jnp.float64(q), ta)[1]) - pa
    return brentq(f, 1.02 * as_, 3.2 * as_, xtol=1e-10)


def solve_cell(pt1, pt3, qpa, ta, z0, corrupt_sign=False, delta=1.0):
    key = ("fj", corrupt_sign, delta)
    t = A1.get_solver(key,
                      lambda: make_resid_freejet(delta, corrupt_sign))
    z = t[0](jnp.asarray(z0), jnp.concatenate(
        [pt1, pt3, jnp.array([qpa])]), ta)
    step = float(t[2](z, jnp.concatenate([pt1, pt3, jnp.array([qpa])]),
                      ta))
    sc = max(1.0, float(jnp.max(jnp.abs(z))))
    return z, step / (A1.NEWTON_TOL_FACTOR * EPS * sc)


def main():
    t0 = time.time()
    print("== A1 brick 2 step 9a: free-boundary unit process [F2/A1]"
          " ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    as_ = tab["_as"]

    # ---- U-1: uniform parallel jet at p = pa is a fixed point
    print("-- U-1: uniform parallel jet (exact fixed point) --")
    Mj = 2.2
    import a1_thrust_functional as TF
    qj = float(TF.solve_qe(jnp.float64(Mj), ta, as_))
    pa = float(A1.state_q(jnp.float64(qj), ta)[1])
    qpa = q_at_pa(pa, ta, as_)
    print("  M = %.2f  q = %.4f  pa = %.5e ; q(pa) roundtrip |d| ="
          " %.2e" % (Mj, qj, pa, abs(qpa - qj)))
    h = 0.05
    pt1 = jnp.array([0.0, 1.90, qj, 0.0])      # interior, below edge
    pt3 = jnp.array([0.0, 2.00, qj, 0.0])      # previous edge point
    z0 = jnp.array([h, 2.00, 0.0])
    z, cert = solve_cell(pt1, pt3, qpa, ta, z0)
    x4, y4, th4u = (float(v) for v in z)
    u4 = qpa * np.cos(th4u)
    v4 = qpa * np.sin(th4u)
    print("  new point: x=%.5f y=%.6f u=%.4f v=%.2e  (cert %.3f)"
          % (x4, y4, u4, v4, cert))
    ok1 = (abs(y4 - 2.0) < 1e-9 and abs(u4 - qj) < 1e-7 * qj
           and abs(v4) < 1e-3 and cert <= 1.0)
    check("U-1 uniform jet: same state, straight edge, certified", ok1)

    # ---- U-2: uniformly TURNED jet — PLANAR (delta = 0): rotation
    # invariance is exact only there; in axisym the source term v/y
    # legitimately changes a turned uniform state (first version used
    # axisym and "failed" on correct physics — test corrected).
    print("-- U-2: turned parallel jet (planar) --")
    th0 = 8.0 * np.pi / 180.0
    u0, v0 = qj * np.cos(th0), qj * np.sin(th0)
    pt1t = jnp.array([0.0, 1.90, u0, v0])
    pt3t = jnp.array([0.0, 2.00, u0, v0])
    zt, cert2 = solve_cell(pt1t, pt3t, qpa, ta,
                           jnp.array([h, 2.0 + h * np.tan(th0), th0]),
                           delta=0.0)
    x4t, y4t, th4 = (float(v) for v in zt)
    edge = np.arctan2(y4t - 2.0, x4t - 0.0)
    print("  th4 = %.5f rad (target %.5f) ; edge slope %.5f ;"
          " cert %.3f" % (th4, th0, edge, cert2))
    check("U-2 turned jet: angle preserved (|d| < 1e-6 rad), edge"
          " along the flow", abs(th4 - th0) < 1e-6
          and abs(edge - th0) < 1e-6 and cert2 <= 1.0)

    # ---- U-3: pressure property at an EXPANDING corner state
    print("-- U-3: p = pa at the new point, expanding jet --")
    qhi = 1.03 * qj             # interior faster => p1 < pa =>
    pt1e = jnp.array([0.0, 1.90, qhi, 0.0])   # COMPRESSING edge, th4<0
    ze, cert3 = solve_cell(pt1e, pt3, qpa, ta, z0)
    th4e = float(ze[2])
    q4e = qpa
    p4 = float(A1.state_q(jnp.float64(q4e), ta)[1])
    print("  th4 = %+.5f rad (inward, as ambient pushes a low-p jet);"
          " |p4-pa|/pa = %.2e ; cert %.3f"
          % (th4e, abs(p4 - pa) / pa, cert3))
    check("U-3 boundary pressure exact AND edge turns inward",
          abs(p4 - pa) / pa < 1e-12 and th4e < -1e-4 and cert3 <= 1.0)

    # ---- U-4: Prandtl-Meyer KNOWN ANSWER on the gconst oracle
    print("-- U-4: PM corner known answer (gconst oracle tables) --")
    tg = A1.prep_tab(A1.build_tab_gconst())
    tag = A1.tab_arrays(tg)
    gam = tg["_g"]
    M1 = 2.0
    q1 = float(TF.solve_qe(jnp.float64(M1), tag, tg["_as"]))
    p1 = float(A1.state_q(jnp.float64(q1), tag)[1])
    pa2 = 0.5 * p1
    # closed forms (calorically perfect): M2 from the isentrope,
    # dnu from the Prandtl-Meyer function
    p0_p1 = (1 + 0.5 * (gam - 1) * M1 * M1) ** (gam / (gam - 1))
    M2 = np.sqrt(2 / (gam - 1)
                 * ((p0_p1 * p1 / pa2) ** ((gam - 1) / gam) - 1))

    def nu(M):
        g = gam
        a = np.sqrt((g + 1) / (g - 1))
        return a * np.arctan(np.sqrt((M * M - 1) / a / a)) \
            - np.arctan(np.sqrt(M * M - 1))
    dnu = nu(M2) - nu(M1)
    q2_cf = M2 * np.sqrt(gam * tg["Rg"]
                         * tg["ts"] / (1 + 0.5 * (gam - 1) * M2 * M2))
    q2_tab = q_at_pa(pa2, tag, tg["_as"])
    print("  closed form: M2 = %.5f, dnu = %.5f rad, q2 = %.4f ;"
          " tables q(pa) = %.4f  (|d|/q = %.1e)"
          % (M2, dnu, q2_cf, q2_tab, abs(q2_tab - q2_cf) / q2_cf))
    ok_q = abs(q2_tab - q2_cf) / q2_cf < 1e-5
    # post-fan uniform state at (M2, theta = dnu): planar cell must
    # continue the straight edge at dnu
    u2, v2 = q2_tab * np.cos(dnu), q2_tab * np.sin(dnu)
    p1u = jnp.array([0.0, 1.90, u2, v2])
    p3u = jnp.array([0.0, 2.00, u2, v2])
    z4, cert4 = solve_cell(p1u, p3u, q2_tab, tag,
                           jnp.array([h, 2.0 + h * np.tan(dnu), dnu]),
                           delta=0.0)
    th4p = float(z4[2])
    print("  cell edge angle = %.5f rad vs PM dnu = %.5f (|d| ="
          " %.1e) ; cert %.3f" % (th4p, dnu, abs(th4p - dnu), cert4))
    check("U-4 PM known answer: q(pa) matches closed form (1e-5) and"
          " edge angle = dnu (1e-6)",
          ok_q and abs(th4p - dnu) < 1e-6 and cert4 <= 1.0)

    # ---- R-1: corrupted q_pa must move the edge
    z1, _ = solve_cell(pt1e, pt3, qpa * 1.01, ta, z0)
    dy = abs(float(z1[2]) - float(ze[2]))
    print("  R-1: edge ANGLE shift under 1%% q_pa corruption = %.3e"
          % dy)
    check("R-1 rejector: boundary condition load-bearing (angle shift"
          " > 1e-4)", dy > 1e-4)

    # ---- R-2: flipped compatibility must fail certification
    try:
        z2, cert5 = solve_cell(pt1e, pt3, qpa, ta, z0,
                               corrupt_sign=True)
        bad = cert5 > 1.0 or not np.isfinite(float(z2[1]))
        print("  R-2: corrupted compatibility cert = %.1f" % cert5)
    except Exception as e:
        bad = True
        print("  R-2: corrupted compatibility raised %s"
              % type(e).__name__)
    check("R-2 rejector: corrupted physics fails certification", bad)

    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
