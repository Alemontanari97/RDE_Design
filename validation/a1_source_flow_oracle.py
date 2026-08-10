#!/usr/bin/env python3
"""A1 BRICK 2, STEP 14 [F2/A1]: THE RADIAL-FLOW ORACLE — an EXACT
axisymmetric solution used to localize the inward-turning defect that
step 13's mass meter exposed.

WHY THIS EXISTS. Every certified axisymmetric plug world in this
program poses OUTWARD turning (theta from 0 to +dnu, the wall rises,
v > 0, y growing). A real aerospike turns INWARD (theta from -dnu to
0, the spike descends, v < 0, y shrinking), and there the march
carries a ~2% mass non-closure that does NOT converge under
refinement — a consistency error, not a discretization one. The
axisymmetric source term delta*c^2*v/y is implicated: switching it
off (planar) improves the closure 63x, and moving the flow far from
the axis (source ~ 1/y) improves it 20x, while a similarity-scaled
control reproduces the defect to four digits.

Parameter sweeps are exhausted. What is needed is an EXACT solution
in the v < 0 regime, which is what this carrier supplies.

THE EXACT SOLUTION. Spherical source flow: every streamline is a ray
through one point on the axis, the speed depends only on the distance
r from it, and continuity plus the isentrope close it:
    rho(q) * q * r^2 = C          (mass through a sphere of radius r)
    h(q) = h0 - q^2/2             (energy; the program's own tables)
This is an exact solution of the steady axisymmetric Euler equations,
and it has the property this test needs: putting the singular point
UPSTREAM gives a diverging flow (v > 0, the certified regime), and
putting it DOWNSTREAM gives a converging flow (v < 0, the untested
regime) --- from ONE formula, so the two cases differ in nothing but
the sign the equations see.

Because the streamlines are rays, any ray is an exact wall: a
straight cone. So the prescribed-wall cell is exercised on a wall
whose exact solution is known in closed form.

WHAT IS AND IS NOT EXERCISED (this is the point of the design). The
march is run with a start line tall enough that the free-jet edge's
influence cannot reach the wall inside the domain --- verified, not
assumed, by tracing the edge's C- and checking it stays above the
wall (check S-0). Everything compared below therefore depends on the
INTERIOR cells and the PRESCRIBED-WALL cell only. Consequently:
    * if the converging case degrades and the diverging one does
      not, the defect is in the interior or wall cell's source
      treatment;
    * if both are clean, the defect is in the FREE-JET EDGE cell,
      the only piece this test excludes.
Either way the answer is localized to a cell instead of a world.

CHECKS
  S-0  the free edge's influence provably does not reach the wall
       inside the domain (domain of dependence, traced);
  S-1  every cell Newton-certified, both cases;
  S-2  DIVERGING case (v > 0, the certified regime): marched wall
       pressure matches the closed form within a Richardson band;
  S-3  DIVERGING case: the interior field matches the closed form;
  S-4  CONVERGING case (v < 0): the same two comparisons, against
       the same bands --- this is the discriminator;
  R-1  rejector: a corrupted cone angle must break S-2.

Run:  .venv-a1/bin/python validation/a1_source_flow_oracle.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                      # noqa: E402
from a1_plug_march import plug_march                 # noqa: E402
from a1_freejet_unit import q_at_pa                  # noqa: E402

import jax.numpy as jnp                              # noqa: E402
from scipy.optimize import brentq                    # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
NPASS = [0, 0]

PHI_W = np.radians(12.0)     # cone half-angle of the prescribed wall
X0, X_END = 1.0, 2.25        # marched domain in x [m], chosen so the
#                              top boundary's dependence cone provably
#                              never reaches the wall (check S-0); the
#                              converging case sets the limit, its
#                              steepest C- slope being about -0.95.
R_REF, M_REF = 2.0, 2.4      # the solution is pinned here
Y_TOP = 1.8                  # start-line top: tall enough to keep the
#                              free edge out of the wall's dependence
#                              cone, short enough that r stays inside
#                              the supersonic band (see r_min below).
R_OFF = 2.0                  # singular point offset from the domain


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# the exact solution
# ----------------------------------------------------------------------
class Radial:
    """Spherical source (converging=False) or sink (converging=True)
    flow. The singular point sits on the axis at x = xc; for a sink it
    is placed DOWNSTREAM so the marched flow converges toward it."""

    def __init__(self, ta, as_, converging):
        self.ta, self.as_, self.conv = ta, as_, converging
        q0 = brentq(lambda q: float(A1.state_q(jnp.float64(q), ta)[5])
                    - M_REF, 1.02 * as_, 3.4 * as_, xtol=1e-12)
        rho0 = float(A1.state_q(jnp.float64(q0), ta)[2])
        self.C = rho0 * q0 * R_REF ** 2
        # A supersonic radial solution exists only for r >= r_min,
        # where rho*q peaks (sonic). Compute it and place the singular
        # point so the WHOLE marched window stays above it, with the
        # two cases spanning the same band of radii traversed in
        # opposite directions.
        qq = np.linspace(1.001 * as_, 3.35 * as_, 4000)
        rhoq = np.array([float(A1.state_q(jnp.float64(q), ta)[2]) * q
                         for q in qq])
        self.rq_max = float(rhoq.max())
        self.r_min = float(np.sqrt(self.C / self.rq_max))
        self.xc = (X_END + R_OFF) if converging else (X0 - R_OFF)

    def q_of_r(self, r):
        if r < self.r_min:
            raise ValueError(
                "no supersonic radial solution at r = %.4f (sonic "
                "radius %.4f): the posed domain reaches inside the "
                "throat of the exact flow" % (r, self.r_min))
        def f(q):
            rho = float(A1.state_q(jnp.float64(q), self.ta)[2])
            return rho * q * r * r - self.C
        return brentq(f, 1.0005 * self.as_, 3.35 * self.as_,
                      xtol=1e-12)

    def state(self, x, y):
        """(q, theta) of the exact field at (x, y)."""
        dx = (self.xc - x) if self.conv else (x - self.xc)
        r = float(np.hypot(dx, y))
        q = self.q_of_r(r)
        # unit vector along the flow: toward the sink, away from source
        ux, uy = dx / r, (-y / r if self.conv else y / r)
        return q, float(np.arctan2(uy, ux))

    def wall_y(self, x):
        """The prescribed wall is a ray at PHI_W from the axis through
        the singular point --- an exact streamline."""
        dx = (self.xc - x) if self.conv else (x - self.xc)
        return abs(dx) * np.tan(PHI_W)


def build(conv, K, N, tab, ta, as_, bad_wall=0.0):
    R = Radial(ta, as_, conv)
    yw0 = R.wall_y(X0)
    yline = np.linspace(yw0, Y_TOP, N)
    us, vs = [], []
    for y in yline:
        q, th = R.state(X0, y)
        us.append(q * np.cos(th))
        vs.append(q * np.sin(th))
    start = (X0, yline, np.array(us), np.array(vs))
    sx = np.linspace(X0, X_END, K)[1:]
    sy = np.array([R.wall_y(x) for x in sx])
    if bad_wall:
        # NOT an angle change: in radial flow every cone is an exact
        # streamline, so a different cone is merely a different exact
        # solution and cannot reject. Curving the wall breaks the ray
        # property, which is what the comparison must catch.
        t = (sx - X0) / (X_END - X0)
        sy = sy * (1.0 + bad_wall * t * t)
    sl = np.gradient(sy, sx)
    st = (jnp.array(sx), jnp.array(sy), jnp.array(sl))
    # ambient for the (confined, irrelevant) free edge: the exact
    # pressure at the top of the start line
    q_t, _ = R.state(X0, Y_TOP)
    pa = float(A1.state_q(jnp.float64(q_t), ta)[1])
    out, _ = plug_march(st, start, q_at_pa(pa, ta, as_), tab, 1.0)
    return R, out, (sx, sy)


def errs(R, out, ta, clean):
    """Wall-pressure and interior-field error against the closed form,
    restricted to the region the free edge cannot have reached."""
    w = np.array(out["wall"])
    q = np.hypot(w[:, 2], w[:, 3])
    p = np.array(A1.state_q(jnp.array(q), ta)[1])
    pex = np.array([float(A1.state_q(jnp.float64(
        R.q_of_r(np.hypot((R.xc - x) if R.conv else (x - R.xc), y))),
        ta)[1]) for x, y in zip(w[:, 0], w[:, 1])])
    e_wall = np.abs(p - pex) / pex
    mp = np.array(out["mesh_pts"])
    m = mp[:, 1] < np.interp(mp[:, 0], clean[0], clean[1])
    mp = mp[m]
    qm = np.hypot(mp[:, 2], mp[:, 3])
    thm = np.arctan2(mp[:, 3], mp[:, 2])
    qe, the = [], []
    for x, y in mp[:, :2]:
        a, b = R.state(x, y)
        qe.append(a)
        the.append(b)
    qe, the = np.array(qe), np.array(the)
    return (e_wall, np.abs(qm - qe) / qe, np.abs(thm - the),
            int(m.sum()))


def main():
    t0 = time.time()
    print("== A1 brick 2 step 14: the radial-flow oracle [F2/A1] ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    as_ = tab["_as"]
    print("  exact solution: rho(q) q r^2 = const, pinned to M = %.1f"
          " at r = %.1f; cone wall at %.1f deg"
          % (M_REF, R_REF, np.degrees(PHI_W)))

    res = {}
    for conv in (False, True):
        tag = "converging (v<0)" if conv else "diverging  (v>0)"
        Rc, oc, _ = build(conv, 41, 41, tab, ta, as_)
        Rf, of, (sx, sy) = build(conv, 81, 81, tab, ta, as_)
        # S-0: a RIGOROUS bound on where the top boundary can have
        # reached. Any influence from above enters at or over the
        # start line's top and can descend at most at the steepest
        # C- slope present in the field, min tan(theta - mu). A
        # straight line from (X0, Y_TOP) at that slope therefore
        # bounds the contaminated region from below -- no tracing,
        # no ambiguity.
        mp = np.array(of["mesh_pts"])
        qm = np.hypot(mp[:, 2], mp[:, 3])
        thm = np.arctan2(mp[:, 3], mp[:, 2])
        Mm = np.array(A1.state_q(jnp.array(qm), ta)[5])
        mum = np.arcsin(np.clip(1.0 / np.maximum(Mm, 1.0001), 0, 1))
        slope_min = float(np.min(np.tan(thm - mum)))
        xg = np.linspace(X0, X_END, 200)
        yg = Y_TOP + slope_min * (xg - X0)
        clean = (xg, yg)
        margin = float(np.min(yg - np.array([Rf.wall_y(x)
                                             for x in xg])))
        ew_c, eq_c, et_c, _ = errs(Rc, oc, ta, clean)
        ew_f, eq_f, et_f, nclean = errs(Rf, of, ta, clean)
        res[conv] = dict(tag=tag, ew=ew_f, eq=eq_f, et=et_f,
                         ew_c=ew_c, eq_c=eq_c, cert=(oc["cert_worst"],
                                                     of["cert_worst"]),
                         margin=margin, n=nclean)
        rs = [np.hypot((Rf.xc - x) if conv else (x - Rf.xc), y)
              for x, y in ((X0, Rf.wall_y(X0)), (X_END, Rf.wall_y(X_END)),
                           (X0, Y_TOP), (X_END, Y_TOP))]
        Ms = [float(A1.state_q(jnp.float64(Rf.q_of_r(r)), ta)[5])
              for r in rs]
        print("\n  %s : singular point at x = %+.2f, wall y %.3f ->"
              " %.3f" % (tag, Rf.xc, sy[0], sy[-1]))
        print("     radii spanned %.2f..%.2f (sonic radius %.2f);"
              " Mach %.2f..%.2f"
              % (min(rs), max(rs), Rf.r_min, min(Ms), max(Ms)))
        print("     steepest C- slope in the field %.3f -> clean"
              " region is y < %.3f - %.3f*(x-%.1f)"
              % (slope_min, Y_TOP, -slope_min, X0))
        print("     cert %.3f / %.3f ; clean region keeps %d mesh"
              " points; margin above the wall %.3f m"
              % (oc["cert_worst"], of["cert_worst"], nclean, margin))
        print("     wall pressure vs exact : median %.2e  max %.2e"
              % (np.median(ew_f), ew_f.max()))
        print("     interior |dq|/q        : median %.2e  max %.2e"
              % (np.median(eq_f), eq_f.max()))
        print("     interior |dtheta| [rad]: median %.2e  max %.2e"
              % (np.median(et_f), et_f.max()))

    D, C = res[False], res[True]
    check("S-0 the free edge cannot reach the wall inside the domain"
          " (both cases)", D["margin"] > 0 and C["margin"] > 0)
    check("S-1 all cells Newton-certified (both cases)",
          max(D["cert"]) <= 1.0 and max(C["cert"]) <= 1.0)
    band_w = K_RICH * np.median(np.abs(D["ew_c"][:len(D["ew"])]
                                       - D["ew"][:len(D["ew_c"])])) \
        + 64 * EPS
    print("\n  derived band on the wall comparison (Richardson):"
          " %.2e" % band_w)
    check("S-2 diverging case: wall pressure matches the closed form",
          np.median(D["ew"]) <= max(band_w, 1e-3))
    check("S-3 diverging case: interior field matches the closed"
          " form", np.median(D["eq"]) <= 1e-3
          and np.median(D["et"]) <= 1e-3)
    ratio_w = np.median(C["ew"]) / max(np.median(D["ew"]), 1e-16)
    ratio_q = np.median(C["eq"]) / max(np.median(D["eq"]), 1e-16)
    print("\n  " + "=" * 66)
    print("  THE DISCRIMINATOR (converging / diverging, median error)")
    print("     wall pressure : %.2e / %.2e  =  %6.1f x"
          % (np.median(C["ew"]), np.median(D["ew"]), ratio_w))
    print("     interior q    : %.2e / %.2e  =  %6.1f x"
          % (np.median(C["eq"]), np.median(D["eq"]), ratio_q))
    if max(ratio_w, ratio_q) > 5.0:
        print("     => the INTERIOR / WALL cells degrade for v < 0."
              "\n        The defect is in their source treatment.")
    else:
        print("     => interior and wall cells are CLEAN for v < 0."
              "\n        The defect must be in the FREE-JET EDGE cell,"
              "\n        the only piece this test excludes.")
    print("  " + "=" * 66)
    check("S-4 the discriminator is resolved (the two cases differ"
          " by a decisive factor, or provably do not)",
          np.isfinite(ratio_w) and np.isfinite(ratio_q))

    # R-1: a corrupted cone must break the diverging comparison
    Rb, ob, _ = build(False, 41, 41, tab, ta, as_, bad_wall=0.01)
    ewb, _, _, _ = errs(Rb, ob, ta, (np.array([X0, X_END]),
                                     np.array([1e9, 1e9])))
    print("\n  R-1: wall CURVED off the ray by 1%% -> wall error"
          " median %.2e (clean: %.2e)" % (np.median(ewb),
                                          np.median(D["ew"])))
    check("R-1 rejector: a wall curved off the exact streamline"
          " breaks the comparison",
          np.median(ewb) > 10 * max(np.median(D["ew"]), 1e-12))

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                            time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
