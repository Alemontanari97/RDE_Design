#!/usr/bin/env python3
"""T03 — the assembled two-wall march WITH THE LIP JET (the SQP's configuration: cowl to the lip, centred fan at
the lip, free edge at p_a, plug running on under the jet), planar, against the EXACT centred-expansion solution.

Exact problem (ref/exact.CenteredFan, written independently): uniform inflow M1 = 1.556 (SDT mean gas) at
theta1 = -20 deg through a vertical start line between y = 0.5 and 1.0; a straight cowl at theta1 ends at the lip
F (x = 0.3); the ambient p_a = p(M2) with nu(M2) = nu(M1) + 20 deg, so the lip fan turns the flow to theta2 = 0.
The plug is the exact streamline through the start line's lower end: the fan's waves land on it without
reflection, so the exact field is (uniform 1) + (centred fan) + (uniform 2, axial, p = p_a), the jet edge is the
straight line from F at theta2, and the exact thrust per unit depth is the exit momentum flux rho2 q2^2 h2.

Model call = what a1_twowall does (TwoWall._march_record_ctx): plug_march(plug stations, uniform start, ...,
shroud = cowl stations from x0 to F, wedge_every m_w by the carrier's rule, fast = True, lip_jet = dict(qpa =
the carrier's brentq speed at p_a, n_fan = round(N/2), n_gl = 16)), delta = 0 (planar).

Checks on a grid ladder (K plug stations, N start rows) = (40,11) (80,21) (160,41) (320,81):
  P1 plug wall pressure vs exact: L1 and max relative error (in units of p1) decrease under refinement
  P2 jet edge position vs the exact straight edge
  P3 mass: last column vs inlet
  P4 thrust per unit depth (F_in - push(plug) + push(cowl), the carrier's functional with planar weights) vs exact
     band: |T_finest - T_exact| <= 2 |T_finest - T_previous| (valid for any observed order >= 0.6) AND observed
     order of the thrust error between the two finest grids >= 1.0
  P5 every march certified (Newton certificate <= 1)
Reference self-check R0: exact F_in - push(plug) + push(cowl) = exact exit momentum flux (momentum theorem).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
from scipy.optimize import brentq                  # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_plug_march as PM                         # noqa: E402

R = rv.Report("t03_planar_lipfan_plug")
gm = rv.sdt_gas()
G = exact.PerfectGas(gm["gamma"], gm["R"], gm["T0"], gm["P0"])
tab, ta = rv.model_table(gm["gamma"], gm["R"], gm["T0"], gm["P0"], gm["T_tab"])

M1, th1 = gm["M_in"], np.radians(-20.0)
M2 = G.M_of_nu(float(G.nu(M1)) + np.radians(20.0))
pa = float(G.p(M2))
x0, y_l, y_u, xF = 0.0, 0.5, 1.0, 0.3
yF = y_u + (xF - x0) * np.tan(th1)
fan = exact.CenteredFan(G, M1, th1, M2, xF, yF)
y_of, slope_of, P_in, P_out = fan.streamline(x0, y_l, 2.0)
x_end = P_out[0] + 0.5 * (P_out[0] - P_in[0])
q1, q2 = float(G.q(M1)), float(G.q(M2))
R.note("M1 %.4f th1 %.1f deg -> M2 %.6f th2 %.6f deg; p_a/P0 %.5f; plug enters the fan at x %.4f, leaves at x %.4f"
       " (y %.5f); plug end x %.4f" % (M1, np.degrees(th1), M2, np.degrees(fan.th2), pa / G.P0, P_in[0], P_out[0],
                                       P_out[1], x_end))

# ------------------------------------------------------------------ exact thrust (per unit depth)
xd = np.linspace(x0, x_end, 40001)
yd = y_of(xd)
pd = np.array([float(G.p(fan.state(x, y)[0])) for x, y in zip(xd[::4], yd[::4])])
pd = np.interp(xd, xd[::4], pd)        # the exact p is piecewise smooth; 1e4 samples, then linear in x
p1 = float(G.p(M1))
rho1, rho2 = float(G.rho(M1)), float(G.rho(M2))
u1 = q1 * np.cos(th1)
F_in_ex = (rho1 * u1 * u1 + p1 - pa) * (y_u - y_l)
push_plug_ex = exact.wall_push(xd, yd, pd, pa, axi=False)
push_cowl_ex = (p1 - pa) * (yF - y_u)
T_ex = F_in_ex - push_plug_ex + push_cowl_ex
h2 = yF - float(y_of(x_end))
T_exit_ex = rho2 * q2 * q2 * h2
mdot_ex = rho1 * u1 * (y_u - y_l)
R.check("R0 reference: momentum theorem, (F_in - push_plug + push_cowl) / exit flux - 1", T_ex / T_exit_ex - 1.0,
        2e-6)

# the carrier's speed at p_a (a1_twowall.TwoWall.__init__ _qpa)
fq = lambda qq: float(A1.state_q(jnp.float64(qq), ta)[1]) - pa        # noqa: E731
lo, hi = 1.02 * tab["_as"], 3.2 * tab["_as"]
while not (np.isfinite(fq(hi)) and fq(hi) < 0.0):
    hi = lo + 0.9 * (hi - lo)
qpa = brentq(fq, lo, hi, xtol=1e-12 * tab["_as"])


def run(K, N, qpa=qpa):
    sx = x0 + (x_end - x0) * np.arange(1, K + 1) / K
    sy, ssl = y_of(sx), slope_of(sx)
    Ks = max(8, int(round(K * (xF - x0) / (x_end - x0))))
    xs = x0 + (xF - x0) * np.arange(0, Ks + 1) / Ks
    ys_s, ss_s = y_u + (xs - x0) * np.tan(th1), np.full(Ks + 1, np.tan(th1))
    yline = np.linspace(y_l, y_u, N)
    start = (x0, yline, np.full(N, q1 * np.cos(th1)), np.full(N, q1 * np.sin(th1)))
    dy_row = (y_u - y_l) / (N - 1)
    m_w = max(1, int(round(1.0 * (sx[0] - x0) * np.tan(np.arcsin(1.0 / M1)) / dy_row)))
    out, S = PM.plug_march((sx, sy, ssl), start, q1, tab, 0.0, shroud=(xs, ys_s, ss_s), wedge_every=m_w,
                           fast=True, lip_jet=dict(qpa=qpa, n_fan=int(round(0.5 * N)), n_gl=16))
    W = np.asarray(out["wall"])
    pw = np.asarray(A1.state_q(jnp.asarray(np.hypot(W[:, 2], W[:, 3])), ta)[1])
    pex = np.array([float(G.p(fan.state(x, y)[0])) for x, y in zip(W[:, 0], W[:, 1])])
    e_p = (pw - pex) / p1
    E = np.asarray(out["edge"])
    E = E[E[:, 0] > xF + 1e-12]
    e_edge = (E[:, 1] - (yF + np.tan(fan.th2) * (E[:, 0] - xF))) / (y_u - y_l)
    md, _ = PM.col_fluxes(np.asarray(out["last_col"]), ta, pa, 0.0)
    col0 = np.stack([np.full(N, x0), yline, start[2], start[3]], 1)
    _, F_in = PM.col_fluxes(col0, ta, pa, 0.0)
    plug_poly = np.vstack([[x0, y_l, start[2][0], start[3][0]], W[:, :4]])
    cowl_poly = np.vstack([[x0, y_u, start[2][0], start[3][0]], np.asarray(out["shroud"])[:, :4]])
    T = F_in - PM.wall_push_poly(plug_poly, ta, pa, 0.0) + PM.wall_push_poly(cowl_poly, ta, pa, 0.0)
    return dict(K=K, N=N, x=W[:, 0], e_p=e_p, L1=float(np.mean(np.abs(e_p))), Linf=float(np.max(np.abs(e_p))),
                edge=float(np.max(np.abs(e_edge))), mass=md / mdot_ex - 1.0, T=T, eT=T / T_ex - 1.0,
                cert=float(out["cert_worst"]), m_w=m_w, n_cells=int(out["cert_n"]), out=out)


grids = [(40, 11), (80, 21), (160, 41), (320, 81)]
res = []
for K, N in grids:
    r = run(K, N)
    res.append(r)
    R.note("K %4d N %3d (wedge every %d, %6d cells): wall p err L1 %.3e max %.3e | edge %.3e | mass %+.3e | thrust %+.3e"
           " | cert %.2e" % (K, N, r["m_w"], r["n_cells"], r["L1"], r["Linf"], r["edge"], r["mass"], r["eT"], r["cert"]))

o = lambda a, b: np.log(abs(a) / abs(b)) / np.log(2.0)      # noqa: E731
for k in range(1, len(res)):
    R.note("orders %d->%d: wall L1 %.2f, max %.2f, edge %.2f, mass %.2f, thrust %.2f"
           % (k - 1, k, o(res[k - 1]["L1"], res[k]["L1"]), o(res[k - 1]["Linf"], res[k]["Linf"]),
              o(res[k - 1]["edge"], res[k]["edge"]), o(res[k - 1]["mass"], res[k]["mass"]),
              o(res[k - 1]["eT"], res[k]["eT"])))
f, c = res[-1], res[-2]
R.check("P1 wall pressure L1 error decreases at every refinement", 0.0, 0.0,
        ok=all(res[k]["L1"] < res[k - 1]["L1"] for k in range(1, len(res))))
R.check("P1 wall pressure L1 error (finest), units of p1", f["L1"], 2.0 * abs(f["L1"] - c["L1"]) + 1e-9)
R.check("P2 jet edge max error decreases at every refinement", 0.0, 0.0,
        ok=all(res[k]["edge"] < res[k - 1]["edge"] for k in range(1, len(res))))
R.check("P2 jet edge max error (finest), band 2|change|", f["edge"], 2.0 * abs(f["edge"] - c["edge"]))
R.check("P3 mass, last column vs inlet (finest), band 2|change|", f["mass"], 2.0 * abs(f["mass"] - c["mass"]) + 1e-12)
R.check("P4 thrust vs exact (finest), band 2|T_f - T_c|/T_ex", f["eT"], 2.0 * abs(f["T"] - c["T"]) / T_ex + 1e-12)
R.check("P4 thrust error order between the two finest grids (>= 1.0)", o(c["eT"], f["eT"]), None,
        ok=o(c["eT"], f["eT"]) >= 1.0)
R.check("P5 worst Newton certificate over the ladder <= 1", max(r["cert"] for r in res), 1.0)
# REJECTOR (R5): the P4 thrust check with the lip jet's ambient 2 % too high (a wrong free-boundary condition)
fqx = lambda qq: float(A1.state_q(jnp.float64(qq), ta)[1]) - 1.02 * pa        # noqa: E731
lo_x, hi_x = 1.02 * tab["_as"], 3.2 * tab["_as"]
while not (np.isfinite(fqx(hi_x)) and fqx(hi_x) < 0.0):
    hi_x = lo_x + 0.9 * (hi_x - lo_x)
qpa_x = brentq(fqx, lo_x, hi_x, xtol=1e-12 * tab["_as"])
cx, fx = run(*grids[-2], qpa=qpa_x), run(*grids[-1], qpa=qpa_x)
# Measured 2026-10-09: the THRUST does not see this corruption (error +5.3e-8 at the finest grid against a band of
# 3.0e-6): downstream of the fan the plug is the exact streamline of the axial region 2, a horizontal wall, so a wrong
# pressure there pushes nothing axially. The jet EDGE sees it (its angle is set by the ambient): the rejector is P2.
R.note("rejector: jet ambient x1.02 -> thrust error %+.3e (finest; P4 is blind to it, see above), edge error %.3e "
       "(finest), %.3e (previous)" % (fx["eT"], fx["edge"], cx["edge"]))
R.reject("P2 jet edge max error (finest), lip jet's ambient x1.02", fx["edge"], 2.0 * abs(fx["edge"] - cx["edge"]))

import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
fig, ax = plt.subplots(1, 3, figsize=(16, 4.3))
out = f["out"]
mp = np.asarray(out["mesh_pts"])
ax[0].plot(mp[:, 0], mp[:, 1], ",", color="0.6")
ax[0].plot(xd, yd, "k-", lw=1.5, label="plug = exact streamline")
ax[0].plot([x0, xF], [y_u, yF], "k-", lw=2.5, label="cowl")
Eg = np.asarray(out["edge"])
ax[0].plot(Eg[:, 0], Eg[:, 1], "r-", lw=1.2, label="model jet edge")
for ang in (fan.phi1, fan.phi2):
    ax[0].plot([xF, xF + 0.6 * np.cos(ang)], [yF, yF + 0.6 * np.sin(ang)], "b--", lw=0.8)
ax[0].set_aspect("equal"); ax[0].set_title("Planar lip fan: net (K 320, N 81)"); ax[0].legend(fontsize=7)
xs_ = np.linspace(x0, x_end, 2000)
ax[1].plot(xs_, [float(G.p(fan.state(x, float(y_of(x)))[0])) / p1 for x in xs_], "k-", lw=2, label="exact")
for r in res:
    W = np.asarray(r["out"]["wall"])
    pw = np.asarray(A1.state_q(jnp.asarray(np.hypot(W[:, 2], W[:, 3])), ta)[1])
    ax[1].plot(W[:, 0], pw / p1, "-", lw=1.0, label="model K %d N %d" % (r["K"], r["N"]))
ax[1].set_xlabel("x"); ax[1].set_ylabel("p_wall / p1"); ax[1].legend(fontsize=7); ax[1].grid(alpha=0.3)
ax[1].set_title("plug wall pressure")
h = np.array([1.0 / r["K"] for r in res])
for key, lab in (("L1", "wall p L1"), ("Linf", "wall p max"), ("edge", "jet edge"), ("mass", "mass"), ("eT", "thrust")):
    ax[2].loglog(h, [abs(r[key]) for r in res], "o-", label=lab)
ax[2].loglog(h, 0.5 * abs(res[0]["L1"]) * (h / h[0]) ** 2, "k--", lw=0.8, label="slope 2")
ax[2].loglog(h, 0.5 * abs(res[0]["L1"]) * (h / h[0]), "k:", lw=0.8, label="slope 1")
ax[2].set_xlabel("1/K"); ax[2].set_ylabel("relative error"); ax[2].legend(fontsize=7); ax[2].grid(alpha=0.3, which="both")
ax[2].set_title("convergence to the exact solution")
rv.savefig(fig, "03_planar_lipfan_plug.png")
sys.exit(R.save(dict(grids=[{k: v for k, v in r.items() if k not in ("out", "x", "e_p")} for r in res],
                     T_exact=T_ex, M2=M2)))
