#!/usr/bin/env python3
"""T02 — the model's interior MOC cell (a1_plug_march.make_resid_interior_bu, solved by the model's own
certified Newton A1.get_solver/solve_cert) against EXACT smooth fields:

  (a) planar centred Prandtl-Meyer fan (delta = 0), SDT mean gas, point 4 inside the fan;
  (b) axisymmetric spherical source flow (delta = 1), SDT mean gas, point 4 off the axis (v != 0, so the
      axisymmetric source term delta c^2 v / y is exercised).

Construction (independent of the model): point 4 is chosen in the field; its two feet are found by tracing the
EXACT C+ and C- characteristics backward from 4 for an arc length h (solve_ivp, rtol 1e-13), with the exact
states there. The cell is given the two feet and must return point 4 and its state.

Error model: the cell is the average-coefficient (trapezoidal) discretisation of the characteristic and
compatibility ODEs -> LOCAL error O(h^3). PASS iff the observed order between the two finest h is >= 2.7 for
position and velocity, in both fields. Rejector (must FAIL the order test, i.e. show order ~2): the planar cell
(delta = 0) used in the axisymmetric field (the source term dropped).

Also: uniform-flow exactness of every cell kind used by the plug/two-wall march (interior, plug wall, shroud
wall, lip/inverse wall, free edge): the uniform state must be returned to rounding (1e-12 relative).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
from scipy.integrate import solve_ivp              # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_plug_march as PM                         # noqa: E402
import a1_freejet_unit as FJ                       # noqa: E402

R = rv.Report("t02_cells")
gm = rv.sdt_gas()
G = exact.PerfectGas(gm["gamma"], gm["R"], gm["T0"], gm["P0"])
tab, ta = rv.model_table(gm["gamma"], gm["R"], gm["T0"], gm["P0"], gm["T_tab"])


def solver(kind, delta):
    fac = dict(int=lambda: PM.make_resid_interior_bu(delta), wb=lambda: PM.make_resid_wallbot(delta),
               wt=lambda: PM.make_resid_walltop(delta), lip=lambda: A1.make_resid_inwall(delta),
               fj=lambda: FJ.make_resid_freejet(delta))[kind]
    return A1.get_solver(("rv_" + kind, delta), fac)


def solve(kind, delta, z0, p):
    s = solver(kind, delta)
    z, step = s[3](jnp.asarray(z0, dtype=jnp.float64), jnp.asarray(p, dtype=jnp.float64), ta)
    sc = max(1.0, float(jnp.max(jnp.abs(z))))
    return np.asarray(z), float(step) / (A1.NEWTON_TOL_FACTOR * A1.EPS * sc)


# ---------------------------------------------------------------- exact fields: (x, y) -> (u, v)
fan = exact.CenteredFan(G, gm["M_in"], 0.0, 2.922, 0.0, 1.0)
src = exact.SphericalSource(G, 1.0)


def uv_fan(x, y):
    M, th = fan.state(x, y)
    q = float(G.q(M))
    return q * np.cos(th), q * np.sin(th)


def uv_src(x, y):
    M, u, v = src.state(x, y)
    return float(u[0]), float(v[0])


def trace_back(uv, x4, y4, sgn, h):
    """Exact characteristic C(sgn) (+1: theta+mu, -1: theta-mu) traced BACKWARD from (x4, y4) over arc length h."""
    def rhs(s, X):
        u, v = uv(X[0], X[1])
        q = np.hypot(u, v)
        M = float(G.M_q(q))
        a = np.arctan2(v, u) + sgn * np.arcsin(1.0 / M)
        return [-np.cos(a), -np.sin(a)]
    sol = solve_ivp(rhs, (0.0, h), [x4, y4], rtol=1e-13, atol=1e-15, method="DOP853")
    x, y = sol.y[0, -1], sol.y[1, -1]
    u, v = uv(x, y)
    return np.array([x, y, u, v])


def order_study(uv, x4, y4, delta, hs, label):
    u4, v4 = uv(x4, y4)
    ex = np.array([x4, y4, u4, v4])
    errs, certs = [], []
    for h in hs:
        p1 = trace_back(uv, x4, y4, +1, h)          # C+ foot (below, same column)
        p2 = trace_back(uv, x4, y4, -1, h)          # C- foot (previous column)
        z0 = PM.predict_bu(jnp.asarray(p1), jnp.asarray(p2), ta)
        z, cr = solve("int", delta, z0, np.r_[p1, p2])
        qs = np.hypot(u4, v4)
        e_pos = np.hypot(z[0] - x4, z[1] - y4) / h          # relative to the cell size
        e_vel = np.hypot(z[2] - u4, z[3] - v4) / qs
        errs.append((h, e_pos * h, e_vel))
        certs.append(cr)
    e = np.array(errs)
    o_pos = np.log(e[-2, 1] / e[-1, 1]) / np.log(hs[-2] / hs[-1])
    o_vel = np.log(e[-2, 2] / e[-1, 2]) / np.log(hs[-2] / hs[-1])
    R.note("%s: h %s" % (label, " ".join("%.2e" % h for h in hs)))
    R.note("%s: |dx4| %s" % (label, " ".join("%.2e" % v for v in e[:, 1])))
    R.note("%s: |dq4|/q %s   worst Newton cert %.2e" % (label, " ".join("%.2e" % v for v in e[:, 2]), max(certs)))
    return e, o_pos, o_vel, max(certs)


hs = 0.08 / 2.0 ** np.arange(6)
# (a) planar fan, point 4 mid-fan at distance 0.6 from the lip corner
phim = 0.5 * (fan.phi1 + fan.phi2)
x4, y4 = fan.xF + 0.6 * np.cos(phim), fan.yF + 0.6 * np.sin(phim)
ea, oa_p, oa_v, ca = order_study(uv_fan, x4, y4, 0.0, hs, "planar fan")
R.check("A1 planar fan: local order, position (>= 2.7)", oa_p, None, ok=oa_p >= 2.7)
R.check("A2 planar fan: local order, velocity (>= 2.7)", oa_v, None, ok=oa_v >= 2.7)
R.check("A3 planar fan: Newton certificate <= 1 at every h", ca, 1.0)
# (b) spherical source, point 4 at r = 2.2 r*, 25 deg off the axis
r4, a4 = 2.2, np.radians(25.0)
x4, y4 = r4 * np.cos(a4), r4 * np.sin(a4)
eb, ob_p, ob_v, cb = order_study(uv_src, x4, y4, 1.0, hs, "axi source")
R.check("B1 axi source: local order, position (>= 2.7)", ob_p, None, ok=ob_p >= 2.7)
R.check("B2 axi source: local order, velocity (>= 2.7)", ob_v, None, ok=ob_v >= 2.7)
R.check("B3 axi source: Newton certificate <= 1 at every h", cb, 1.0)
# rejector: planar cell in the axisymmetric field (source term dropped) must lose an order
er, or_p, or_v, _ = order_study(uv_src, x4, y4, 0.0, hs, "REJECTOR planar cell in axi field")
R.check("B4 rejector: dropping the source term degrades the velocity order to < 2.5", or_v, None, ok=or_v < 2.5)

# (c) uniform-flow exactness of every cell kind
qU = float(G.q(2.0))
for delta, th in ((0.0, np.radians(12.0)), (1.0, 0.0)):
    uU, vU = qU * np.cos(th), qU * np.sin(th)
    M = 2.0
    mu = np.arcsin(1.0 / M)
    tp, tm = np.tan(th + mu), np.tan(th - mu)
    # interior: 1 below on the C+ through 4, 2 on the C- through 4
    X4, Y4 = 1.0, 1.0
    p1 = [X4 - 0.05, Y4 - 0.05 * tp, uU, vU]
    p2 = [X4 - 0.04, Y4 - 0.04 * tm, uU, vU]
    z, cr = solve("int", delta, [X4 + 1e-3, Y4 - 1e-3, uU * 1.001, vU], p1 + p2)
    e = max(abs(z[0] - X4), abs(z[1] - Y4)) + max(abs(z[2] - uU), abs(z[3] - vU)) / qU
    R.check("C1 uniform (delta %d): interior cell exact" % delta, e, 1e-12)
    # plug wall (bottom): wall y = Y4 + slope (x - X4), slope = tan(th); foot chord A-B crossing the C- from 4
    sl = np.tan(th)
    A = [X4 - 0.06, Y4 - 0.06 * tm - 0.02, uU, vU]
    B = [X4 - 0.06, Y4 - 0.06 * tm + 0.02, uU, vU]
    z, cr = solve("wb", delta, [Y4 - 0.06 * tm, uU * 1.001], A + B + [X4, Y4, sl])
    e = abs(z[1] - uU) / qU
    R.check("C2 uniform (delta %d): plug-wall cell exact (u4)" % delta, e, 1e-12)
    # shroud wall (top): the C+ from pt1 meets a straight shroud through (X4, Y4) with slope tan(th)
    P1 = [X4 - 0.05, Y4 - 0.05 * tp, uU, vU]
    xA, xB = X4 - 0.1, X4 + 0.1
    z, cr = solve("wt", delta, [X4 + 0.01, uU * 1.001], P1 + [xA, Y4 + sl * (xA - X4), sl, xB, Y4 + sl * (xB - X4), sl])
    e = abs(z[0] - X4) + abs(z[1] - uU) / qU
    R.check("C3 uniform (delta %d): shroud-wall cell exact (x4, u4)" % delta, e, 1e-12)
    # lip / inverse wall: point 4 given; foot on the chord pt1-pt3 crossing the C+ through 4
    Cx, Cy = X4 - 0.05, Y4 - 0.05 * tp                      # the C+ through 4, 0.05 upstream
    P1 = [Cx - 0.01, Cy + 0.03, uU, vU]                         # chord through C, not along the C+
    P3 = [Cx + 0.01, Cy - 0.03, uU, vU]
    z, cr = solve("lip", delta, [Cx + 0.002, uU * 1.001], P1 + P3 + [X4, Y4, sl])
    e = abs(z[1] - uU) / qU
    R.check("C4 uniform (delta %d): lip (inverse-wall) cell exact (u4)" % delta, e, 1e-12)
    # free edge: pt1 below on the C+ through 4, pt3 = previous edge point on the edge streamline through 4
    P1 = [X4 - 0.05, Y4 - 0.05 * tp, uU, vU]
    P3 = [X4 - 0.08, Y4 - 0.08 * sl, uU, vU]
    z, cr = solve("fj", delta, [X4 + 0.01, Y4, th + 0.01], P1 + P3 + [qU])
    e = abs(z[0] - X4) + abs(z[1] - Y4) + abs(z[2] - th)
    R.check("C5 uniform (delta %d): free-edge cell exact (x4, y4, theta4)" % delta, e, 1e-12)

import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
for e, lab, c in ((ea, "planar fan (delta 0)", "C0"), (eb, "axi source (delta 1)", "C1"),
                  (er, "rejector: planar cell in axi field", "C3")):
    ax[0].loglog(e[:, 0], e[:, 1], "o-", color=c, label=lab)
    ax[1].loglog(e[:, 0], e[:, 2], "o-", color=c, label=lab)
for k_, a_ in enumerate(ax):
    h_ = np.array([hs[0], hs[-1]])
    a_.loglog(h_, 0.5 * ea[0, 1 + k_] * (h_ / hs[0]) ** 3, "k--", lw=0.8, label="slope 3")
    p_rej = 2 if k_ == 0 else 1          # the rejector: position O(h^2), velocity O(h) (the dropped source term)
    a_.loglog(h_, 0.5 * er[0, 1 + k_] * (h_ / hs[0]) ** p_rej, "k:", lw=0.8, label="slope %d" % p_rej)
    a_.set_xlabel("cell size h"); a_.grid(alpha=0.3, which="both"); a_.legend(fontsize=7)
ax[0].set_ylabel("|position error of point 4|"); ax[1].set_ylabel("|velocity error| / q")
ax[0].set_title("Interior cell: position error"); ax[1].set_title("Interior cell: velocity error")
rv.savefig(fig, "02_cell_local_order.png")
sys.exit(R.save(dict(orders=dict(fan=(oa_p, oa_v), src=(ob_p, ob_v), rejector=(or_p, or_v)))))
