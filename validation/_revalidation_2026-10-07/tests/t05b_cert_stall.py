#!/usr/bin/env python3
"""T05b -- the one certificate failure of T05 (air Migdal, eps 6, grid (140,31): worst ratio 1.96 at the plug-wall
cell of station 34), taken apart.

The certificate (a1_ideal_march_jax.make_implicit_solver): one extra Newton step at the returned root must be below
100 eps |z|; a march with a ratio > 1 is REJECTED by the walk (a1_plug_spline_opt.run_trsqp). Questions:
  B1 is the returned point a root on the right branch, i.e. does plain Newton from it converge quadratically
     (second step << first)? -> a STALL of the damped Newton, not a wrong or missing root;
  B2 why the damped Newton stalls: its trial steps are chosen by the residual NORM, whose two rows have different
     units (position ~ y, compatibility ~ u^3); if the full step RAISES that norm, the damped loop keeps a shorter
     or zero step and exits on its trip cap -- measured here: |r| before / after the full step;
  B3 why this cell: the wall cell parameterises its foot by y on the chord A-B of the previous column
     (a1_plug_march.make_resid_wallbot: D = (y2 - yA)/(yB - yA)), so dx2/dy2 = (xB - xA)/(yB - yA) = cot(phi) with
     phi the chord's angle; the previous column is a C+ line, phi = theta + mu, and near theta_wall = -mu the C+ is
     horizontal: the Jacobian's condition grows like cot(theta + mu);
  B4 the rescue of the model (A1_NEWTON_RESCUE: plain Newton steps from the stalled iterate, kept only if
     certified) certifies the same march and moves the wall pressures by no more than one Newton step.
The rescue is the model's DEFAULT since 2026-10-08: this test switches it OFF for the first march (the stall it takes
apart) and back ON for B4.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import geno_io as GI                               # noqa: E402
import numpy as np                                 # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_plug_march as PM                         # noqa: E402
import a1_shroud_twin as ST                        # noqa: E402

R = rv.Report("t05b_cert_stall")
A1.NEWTON_RESCUE = False           # the stall is shown WITHOUT the rescue (default on since 2026-10-08)
A1._SOLVERS.clear()
d = os.path.join(rv.RV, "geno", "migdal_air_eps6_ni1001_ne2000")
c = json.load(open(os.path.join(d, "case.json")))
th = c["thermo"]
g_, R_, T0, P0 = th["gamma"], th["R"], c["gas"][2], c["gas"][3]
G = exact.PerfectGas(g_, R_, T0, P0)
tab, ta = rv.model_table(g_, R_, T0, P0, [0.2 * T0 / (1 + 0.5 * (g_ - 1) * 4.5 ** 2), 1.02 * T0])
w = GI.migdal_walls(d)
up, lo = ("cm", "cp") if w["cm"][1][0] > w["cp"][1][0] else ("cp", "cm")
plug_d, shroud_d = ST.dedup(np.stack(w[lo], 1)[:, :2]), ST.dedup(np.stack(w[up], 1)[:, :2])
x0, y_l, y_u = float(plug_d[0, 0]), float(plug_d[0, 1]), float(shroud_d[0, 1])
Mi = c["Mi"]
q_i = float(G.q(Mi))
K, N = 140, 31
sx, sy, ssl = ST.stations_from(plug_d, K)
Ks = max(8, int(K * (shroud_d[-1, 0] - shroud_d[0, 0]) / (plug_d[-1, 0] - plug_d[0, 0])))
xs, ys_, ss_ = ST.stations_from(shroud_d, Ks)
xs, ys_, ss_ = np.r_[x0, xs], np.r_[y_u, ys_], np.r_[0.0, ss_]
yline = np.linspace(y_l, y_u, N)
start = (x0, yline, np.full(N, q_i), np.zeros(N))
m_w = max(1, int(round((sx[0] - x0) * np.tan(np.arcsin(1.0 / Mi)) / ((y_u - y_l) / (N - 1)))))


def march():
    return PM.plug_march((np.asarray(sx), np.asarray(sy), np.asarray(ssl)), start, q_i, tab, 1.0,
                         shroud=(xs, ys_, ss_), wedge_every=m_w, fast=True)


out, S = march()
tag = out["cert_where"]
R.note("march without the rescue: worst certificate %.3f at %s (%d cells)" % (out["cert_worst"], tag, out["cert_n"]))
kst = tag[1]
i = S.d["K_cols"][kst]
b, jf = S.d["wfoot"][kst]
Gm = {k: np.asarray(v) for k, v in zip(out["mesh_keys"], out["mesh_pts"])}
ptA, ptB, wp = Gm[(jf, i - b)][:4], Gm[(jf + 1, i - b)][:4], Gm[(1, i)]
sl = wp[3] / wp[2]
p = jnp.asarray(np.r_[ptA, ptB, [wp[0], wp[1], sl]])
resid = PM.make_resid_wallbot(1.0)
solver = A1.get_solver(("wb", 1.0), lambda: PM.make_resid_wallbot(1.0))
z, step = solver[3](jnp.asarray([0.5 * (ptA[1] + ptB[1]), ptA[2]]), p, ta)
sc = max(1.0, float(jnp.max(jnp.abs(z))))
line = A1.NEWTON_TOL_FACTOR * A1.EPS * sc
R.note("the cell: column %d, foot on the previous column's rows %d-%d; returned z = (y2 %.10f, u4 %.10f); one more "
       "Newton step %.3e = %.2f x the line %.3e" % (i, jf, jf + 1, float(z[0]), float(z[1]), float(step),
                                                   float(step) / line, line))
Jf = jax.jacfwd(resid, argnums=0)
zz, steps, norms = jnp.asarray(z), [], []
for k in range(4):
    r = resid(zz, p, ta)
    dz = jnp.linalg.solve(Jf(zz, p, ta), r)
    steps.append(float(jnp.max(jnp.abs(dz))))
    norms.append(float(jnp.sum(r * r)))
    zz = zz - dz
R.note("plain Newton from the returned point: steps %s; residual norm^2 %s" % (
    " ".join("%.2e" % s for s in steps), " ".join("%.2e" % v for v in norms)))
R.check("B1 plain Newton converges quadratically from the returned point (second step / first)", steps[1] / steps[0],
        1e-2)
R.check("B2 the full step raises the mixed-unit residual norm (norm after / before > 1)", norms[1] / norms[0], None,
        ok=norms[1] > norms[0])
Jz = np.asarray(Jf(jnp.asarray(z), p, ta))
cond = float(np.linalg.cond(Jz))
M_w = float(A1.state_q(jnp.float64(np.hypot(wp[2], wp[3])), ta)[5])
th_w, mu_w = np.degrees(np.arctan(sl)), np.degrees(np.arcsin(1.0 / M_w))
phi = np.degrees(np.arctan2(ptB[1] - ptA[1], ptB[0] - ptA[0]))
R.note("geometry: wall angle %.3f deg, Mach %.4f (mu %.3f deg): theta + mu = %.3f deg; foot chord angle %.4f deg; "
       "dx2/dy2 = cot(chord) = %.1f; cond(J) = %.2e" % (th_w, M_w, mu_w, th_w + mu_w, phi, 1.0 / np.tan(np.radians(phi)),
                                                       cond))
R.check("B3 the C+ is near horizontal at the cell (|theta + mu| < 3 deg) and the foot chord too (|phi| < 1 deg)",
        th_w + mu_w, 3.0, ok=abs(th_w + mu_w) < 3.0 and abs(phi) < 1.0)
# B4: the model's rescue (its default), the same march
A1.NEWTON_RESCUE = True
A1._SOLVERS.clear()
out_r, _ = march()
pw = lambda o: np.asarray(A1.state_q(jnp.asarray(np.hypot(np.asarray(o["wall"])[:, 2], np.asarray(o["wall"])[:, 3])), ta)[1])  # noqa: E731
dp = float(np.max(np.abs(pw(out_r) / pw(out) - 1.0)))
R.note("with A1_NEWTON_RESCUE: worst certificate %.3f at %s; max relative change of the wall pressures %.2e"
       % (out_r["cert_worst"], out_r["cert_where"], dp))
R.check("B4 the rescued march is certified", out_r["cert_worst"], 1.0)
R.check("B4 the rescue moves the wall pressures by less than 1e-10 (one Newton step at the floor)", dp, 1e-10)
sys.exit(R.save(dict(cell=dict(column=int(i), rows=[int(jf), int(jf) + 1], steps=steps, norms=norms, cond=cond,
                               theta_wall=th_w, mu=mu_w, chord=phi), cert_default=float(out["cert_worst"]),
                     cert_rescue=float(out_r["cert_worst"]), dp=dp)))
