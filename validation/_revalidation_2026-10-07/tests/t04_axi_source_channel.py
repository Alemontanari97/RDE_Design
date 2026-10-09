#!/usr/bin/env python3
"""T04 — the assembled AXISYMMETRIC two-wall march (plug + shroud, the internal channel of the SQP's posing) and
the model's thrust functional, against the EXACT spherical source flow between two coaxial cones.

Exact problem (ref/exact.SphericalSource): radial flow from the origin, A/A* = (r/r*)^2 (supersonic branch), SDT
mean gas; inner wall (plug) = cone of half-angle 10 deg, outer wall (shroud) = cone of 25 deg, both through the
origin, so both are streamlines and the field between them is exactly the source flow (v != 0 everywhere off the
axis: the axisymmetric source term and both wall cells are exercised). Start line: vertical at x0 = 1.4 r*, the
exact states on it.

Model: plug_march(delta = 1, shroud = cone stations, wedge rule of the carrier, fast) -- the same call as
TwoWall._march_record_ctx without the lip jet; thrust = the carrier's functional TwoWall._gauge_push / _J_gen
(called on a stub carrying only the attributes those functions read) with F_in = col_fluxes of the start line.

Checks on (K, N) = (40,11) (80,21) (160,41) (320,81):
  S1 wall pressure on plug and shroud vs exact: L1/max relative error, decreasing under refinement, order >= 1.5
  S2 interior field: every net point's speed vs the exact q(r) at its own position
  S3 mass flux through the last column vs exact
  S4 thrust (the carrier's functional) vs the exact thrust of the same walls: band 2|T_f - T_c| and order >= 1.5
  S5 certificates <= 1
Reference self-check R0: exact (F_in - pa A_in - push_plug + push_shroud) = exact flux through the vertical
exit plane at the plug end, shroud integrated to the same x (momentum theorem, independent quadratures).
"""
import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_plug_march as PM                         # noqa: E402
import a1_twowall as T                             # noqa: E402

R = rv.Report("t04_axi_source_channel")
gm = rv.sdt_gas()
G = exact.PerfectGas(gm["gamma"], gm["R"], gm["T0"], gm["P0"])
tab, ta = rv.model_table(gm["gamma"], gm["R"], gm["T0"], gm["P0"], gm["T_tab"])
src = exact.SphericalSource(G, 1.0)
thp, ths = np.radians(10.0), np.radians(25.0)
x0, x_e = 1.4, 3.0
y_l, y_u = x0 * np.tan(thp), x0 * np.tan(ths)
pa = 0.5 * float(G.p(src.M(np.hypot(x_e, x_e * np.tan(ths)))[0]))     # an ambient below the exit pressure


def exact_uv(x, y):
    M, u, v = src.state(np.atleast_1d(x), np.atleast_1d(y))
    return M, u, v


def exact_p(x, y):
    return G.p(src.M(np.hypot(x, y)))


# reference thrust of a channel from x0 to (x_plug_end, x_shroud_end)
def exact_thrust(xpe, xse, n=20001):
    yl = np.linspace(y_l, y_u, n)
    M, u, v = exact_uv(np.full(n, x0), yl)
    p, rho = G.p(M), G.rho(M)
    w = 2.0 * np.pi * yl
    f = (rho * u * u + p - pa) * w
    F_in = float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(yl)))
    xp = np.linspace(x0, xpe, n)
    xs = np.linspace(x0, xse, n)
    push_p = exact.wall_push(xp, xp * np.tan(thp), exact_p(xp, xp * np.tan(thp)), pa, axi=True)
    push_s = exact.wall_push(xs, xs * np.tan(ths), exact_p(xs, xs * np.tan(ths)), pa, axi=True)
    return F_in - push_p + push_s, F_in


# R0: momentum theorem on the exact solution, both walls to x_e
T_ref, _ = exact_thrust(x_e, x_e)
ye = np.linspace(x_e * np.tan(thp), x_e * np.tan(ths), 20001)
M, u, v = exact_uv(np.full(ye.size, x_e), ye)
f = (G.rho(M) * u * u + G.p(M) - pa) * 2.0 * np.pi * ye
F_exit = float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(ye)))
R.check("R0 reference: momentum theorem (walls + inlet) / exit-plane flux - 1", T_ref / F_exit - 1.0, 2e-7)
mdot_ex = G.mass_flux_star() * src.r_star ** 2 * 2.0 * np.pi * (np.cos(thp) - np.cos(ths))     # between the cones
mdot_plane = float(np.sum(0.5 * ((G.rho(M) * u * 2 * np.pi * ye)[1:] + (G.rho(M) * u * 2 * np.pi * ye)[:-1]) * np.diff(ye)))
R.check("R0 reference: mass through the exit plane / analytic rate - 1", mdot_plane / mdot_ex - 1.0, 2e-7)
R.note("source flow: M on the start line %.4f .. %.4f, at the exit %.4f .. %.4f; p_a / P0 = %.5f"
       % (src.M(np.hypot(x0, y_l))[0], src.M(np.hypot(x0, y_u))[0], src.M(np.hypot(x_e, x_e * np.tan(thp)))[0],
          src.M(np.hypot(x_e, x_e * np.tan(ths)))[0], pa / G.P0))


def stub(q_i):
    """The attributes TwoWall._gauge_push reads (x0, sep) -- the carrier's own function, unchanged."""
    return types.SimpleNamespace(x0=x0, sep="", pa=pa / G.P0, P0=G.P0)


def run(K, N, delta=1.0):
    sx = x0 + (x_e - x0) * np.arange(1, K + 1) / K
    Ks = max(8, K)
    xs = x0 + (1.6 * x_e - x0) * np.arange(0, Ks + 1) / Ks
    yline = np.linspace(y_l, y_u, N)
    M_, u_, v_ = exact_uv(np.full(N, x0), yline)
    start = (x0, yline, u_, v_)
    dy_row = (y_u - y_l) / (N - 1)
    m_w = max(1, int(round(1.0 * (sx[0] - x0) * np.tan(np.arcsin(1.0 / M_[0])) / dy_row)))
    out, S = PM.plug_march((sx, sx * np.tan(thp), np.full(K, np.tan(thp))), start, float(np.hypot(u_[0], v_[0])),
                           tab, delta, shroud=(xs, xs * np.tan(ths), np.full(Ks + 1, np.tan(ths))), wedge_every=m_w,
                           fast=True)
    Wp, Ws = np.asarray(out["wall"]), np.asarray(out["shroud"])
    errs = {}
    for key, Wk in (("plug", Wp), ("shroud", Ws)):
        pm_ = np.asarray(A1.state_q(jnp.asarray(np.hypot(Wk[:, 2], Wk[:, 3])), ta)[1])
        pe_ = exact_p(Wk[:, 0], Wk[:, 1])
        e = (pm_ - pe_) / pe_
        errs[key] = (float(np.mean(np.abs(e))), float(np.max(np.abs(e))))
    mp = np.asarray(out["mesh_pts"])
    qm = np.hypot(mp[:, 2], mp[:, 3])
    qe = G.q(src.M(np.hypot(mp[:, 0], mp[:, 1])))
    e_field = float(np.max(np.abs(qm / qe - 1.0)))
    lc = np.asarray(out["last_col"])
    md, _ = PM.col_fluxes(lc, ta, pa, 1.0)
    # exact mass through the same last column: in source flow rho q r^2 = rho* a* r*^2 on every ray, so the rate
    # between the plug cone and the ray through the column's TOP point (after the lip that top point lies on F's
    # C-, not on the shroud) is rho* a* r*^2 2 pi (cos thp - cos th_top)
    th_top = float(np.arctan2(lc[-1, 1], lc[-1, 0]))
    md_lc = G.mass_flux_star() * src.r_star ** 2 * 2.0 * np.pi * (np.cos(thp) - np.cos(th_top))
    col0 = np.stack([np.full(N, x0), yline, u_, v_], 1)
    md0, F_in = PM.col_fluxes(col0, ta, 0.0, 1.0)
    # THE CARRIER'S FUNCTIONAL: [F_in - p_a A_in - gauge_push(plug) + gauge_push(shroud)]
    A_in = np.pi * (y_u ** 2 - y_l ** 2)
    ctx_p = dict(q_i=float(np.hypot(u_[0], v_[0])), ta=ta)
    ctx_s = dict(q_i=float(np.hypot(u_[-1], v_[-1])), ta=ta)
    gp = float(T.TwoWall._gauge_push(stub(None), jnp.asarray(Wp), y_l, ctx_p, pa))
    gs = float(T.TwoWall._gauge_push(stub(None), jnp.asarray(Ws), y_u, ctx_s, pa))
    Tm = F_in - pa * A_in - gp + gs
    Tx, F_in_ex = exact_thrust(float(Wp[-1, 0]), float(Ws[-1, 0]))
    return dict(K=K, N=N, plug=errs["plug"], shroud=errs["shroud"], field=e_field, mass=md / md_lc - 1.0,
                mass_in=md0 / mdot_ex - 1.0, T=Tm, Tx=Tx, eT=Tm / Tx - 1.0, cert=float(out["cert_worst"]),
                lip=out["lip_col"], n=int(out["cert_n"]), out=out)


grids = [(40, 11), (80, 21), (160, 41), (320, 81)]
res = []
for K, N in grids:
    r = run(K, N)
    res.append(r)
    R.note("K %4d N %3d (%6d cells): plug p L1 %.2e max %.2e | shroud p L1 %.2e max %.2e | field q max %.2e | "
           "mass %+.2e (inlet col %+.2e) | thrust %+.3e | cert %.2e | lip reached %s"
           % (K, N, r["n"], r["plug"][0], r["plug"][1], r["shroud"][0], r["shroud"][1], r["field"], r["mass"],
              r["mass_in"], r["eT"], r["cert"], r["lip"]))
o = lambda a, b: np.log(abs(a) / abs(b)) / np.log(2.0)      # noqa: E731
for k in range(1, len(res)):
    R.note("orders %d->%d: plug L1 %.2f, shroud L1 %.2f, field %.2f, mass %.2f, thrust %.2f"
           % (k - 1, k, o(res[k - 1]["plug"][0], res[k]["plug"][0]), o(res[k - 1]["shroud"][0], res[k]["shroud"][0]),
              o(res[k - 1]["field"], res[k]["field"]), o(res[k - 1]["mass"], res[k]["mass"]),
              o(res[k - 1]["eT"], res[k]["eT"])))
f, c = res[-1], res[-2]
for key in ("plug", "shroud"):
    R.check("S1 %s wall pressure L1 decreases at every refinement" % key, 0.0, 0.0,
            ok=all(res[k][key][0] < res[k - 1][key][0] for k in range(1, len(res))))
    R.check("S1 %s wall pressure L1 order, two finest grids (>= 1.5)" % key, o(c[key][0], f[key][0]), None,
            ok=o(c[key][0], f[key][0]) >= 1.5)
R.check("S2 field speed max error order, two finest grids (>= 1.5)", o(c["field"], f["field"]), None,
        ok=o(c["field"], f["field"]) >= 1.5)
R.check("S3 mass, last column (finest), band 2|change|", f["mass"], 2.0 * abs(f["mass"] - c["mass"]) + 1e-12)
R.check("S3 mass, start column (finest) vs analytic, band 2|change|", f["mass_in"],
        2.0 * abs(f["mass_in"] - c["mass_in"]) + 1e-12)
R.check("S4 thrust (carrier's functional) vs exact (finest), band 2|change|", f["eT"],
        2.0 * abs(f["eT"] - c["eT"]) + 1e-12)
R.check("S4 thrust error order, two finest grids (>= 1.5)", o(c["eT"], f["eT"]), None, ok=o(c["eT"], f["eT"]) >= 1.5)
R.check("S5 worst certificate <= 1", max(r["cert"] for r in res), 1.0)
# REJECTOR (R5): the S4 thrust check on the PLANAR march (axisymmetric source term dropped) in the same axisymmetric field
cx, fx = run(*grids[-2], delta=0.0), run(*grids[-1], delta=0.0)
R.note("rejector: planar march -> thrust error %+.3e (finest), %+.3e (previous)" % (fx["eT"], cx["eT"]))
R.reject("S4 thrust vs exact (finest), march without the axisymmetric source term", fx["eT"],
         2.0 * abs(fx["eT"] - cx["eT"]) + 1e-12)

import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
fig, ax = plt.subplots(1, 3, figsize=(17, 4.8), constrained_layout=True, gridspec_kw=dict(width_ratios=[1.3, 1, 1]))
mp = np.asarray(f["out"]["mesh_pts"])
qm = np.hypot(mp[:, 2], mp[:, 3])
sc = ax[0].scatter(mp[:, 0], mp[:, 1], c=qm / G.q(src.M(np.hypot(mp[:, 0], mp[:, 1]))) - 1.0, s=1, cmap="coolwarm")
plt.colorbar(sc, ax=ax[0], label="q_model / q_exact - 1", fraction=0.05, pad=0.02)
ax[0].set_aspect("equal"); ax[0].set_title("Axisymmetric source flow between cones (K 320, N 81)")
for r in res:
    W = np.asarray(r["out"]["wall"])
    pm_ = np.asarray(A1.state_q(jnp.asarray(np.hypot(W[:, 2], W[:, 3])), ta)[1])
    ax[1].plot(W[:, 0], pm_ / exact_p(W[:, 0], W[:, 1]) - 1.0, lw=1, label="plug K %d" % r["K"])
ax[1].set_xlabel("x"); ax[1].set_ylabel("p_model / p_exact - 1 (plug)"); ax[1].legend(fontsize=7); ax[1].grid(alpha=0.3)
h = np.array([1.0 / r["K"] for r in res])
for key, lab, fn in (("plug", "plug p L1", lambda r: r["plug"][0]), ("shroud", "shroud p L1", lambda r: r["shroud"][0]),
                     ("field", "field q max", lambda r: r["field"]), ("mass", "mass", lambda r: abs(r["mass"])),
                     ("eT", "thrust", lambda r: abs(r["eT"]))):
    ax[2].loglog(h, [fn(r) for r in res], "o-", label=lab)
ax[2].loglog(h, res[0]["plug"][0] * (h / h[0]) ** 2, "k--", lw=0.8, label="slope 2")
ax[2].set_xlabel("1/K"); ax[2].set_ylabel("relative error"); ax[2].legend(fontsize=7); ax[2].grid(alpha=0.3, which="both")
ax[2].set_title("convergence to the exact solution")
rv.savefig(fig, "04_axi_source_channel.png")
sys.exit(R.save(dict(grids=[{k: v for k, v in r.items() if k != "out"} for r in res])))
