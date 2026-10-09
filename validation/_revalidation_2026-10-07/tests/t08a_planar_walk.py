#!/usr/bin/env python3
"""T08a (one walk) -- the model's SQP driver (a1_plug_spline_opt.run_trsqp, the production switches PSPL_BACKTRACK=4,
PSPL_JSCALE=radius, PSPL_TRFOLLOW=1) on the planar plug posing of ref/planar_posing.py, whose exact optimum is the
ideal plug (T <= mdot V_a for every shock-free contour with the base at p_a; equality iff the exit is uniform, axial,
at p_a). usage: t08a_planar_walk.py <start A|B|C> <class 0|1> [K N [floor_div]]   -> out/t08a_walk_<start><class>_K<K>[_f<div>].json
  A = the class member closest to the ideal plug (least squares) + a bump 0.02 sin(pi x / L) (a perturbed optimum)
  B = the ideal plug of a 15-degree lip fan (a smooth design for the wrong ambient)
  C = the straight line from the start point to the ideal tip height (a generic start)
Walk: 40 segments x 8 iterations, radius 0.02 (4 percent of the inlet height), floor radius / 16, backtracking 4.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
os.environ.setdefault("PSPL_JSCALE", "radius")
os.environ.setdefault("PSPL_TRFOLLOW", "1")
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import numpy as np                                 # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import planar_posing as PP                         # noqa: E402
import a1_plug_spline_opt as P                     # noqa: E402

start, cls = sys.argv[1], int(sys.argv[2])
K, N = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (80, 21)
FDIV = float(sys.argv[5]) if len(sys.argv) > 5 else 16.0          # radius floor = tr0 / FDIV
tag = "t08a_walk_%s%d_K%d" % (start, cls, K) + ("" if FDIV == 16.0 else "_f%d" % int(FDIV))
QN_ON = P.DRIVER == "qntr"     # the agnostic driver (a1_qntr, default since 2026-10-08): one setting for every case
if QN_ON:
    tag += "_qntr"
QN_SEGS, QN_TR0 = 100, 0.01
t00 = time.time()
pp = PP.PlanarPlug(K=K, N=N, m=12, L=2.0)
W_fit = pp.fit_ideal()
if start == "A":
    W0 = W_fit + 0.02 * np.sin(np.pi * (pp.xk - PP.X0) / (pp.L - PP.X0))
elif start == "B":
    G = pp.G
    M2b = G.M_of_nu(float(G.nu(pp.M1)) + np.radians(15.0))
    fanb = exact.CenteredFan(G, pp.M1, pp.th1, M2b, PP.XF, pp.yF)
    yb, _, _, _ = fanb.streamline(PP.X0, PP.Y_L, pp.L)
    W0 = np.asarray(yb(pp.xk), float)
else:
    W0 = PP.Y_L + (pp.W_ideal_knots[-1] - PP.Y_L) * (pp.xk - PP.X0) / (pp.L - PP.X0)
CLASS = json.load(open("/data10/falco/RDE/RDE_Design/validation/_rde_tournament/stech/class_nofold_2026-09-28.json"))
mg = None
if cls:
    mg = pp.margin_dict(mu0=CLASS["floors"][0], rho=CLASS["rho"], m_ref=CLASS["m_ref"])
    mg["tol"] = CLASS["gap"]


def reading(W, label):
    out, S = pp.march_record(W, margin=pp.margin_dict(mu0=CLASS["floors"][0], rho=CLASS["rho"], m_ref=CLASS["m_ref"]))
    J = float(pp.J_of(out))
    g = np.asarray(jax.grad(lambda z: pp.J_replay(z, S))(jnp.asarray(W)))
    B, c = pp.basis()
    y = B @ np.asarray(W) + c
    dy = y - np.asarray(pp.y_ideal(pp.sx))
    r = dict(J=J, gap=J / pp.T_ideal - 1.0, cert=float(out["cert_worst"]),
             ks=float(out["margin_ks"]) - CLASS["floors"][0], m_min=float(out["margin_min"]),
             grad_inf=float(np.max(np.abs(g))) / pp.T_ideal, dy_max=float(np.max(np.abs(dy))),
             dy_rms=float(np.sqrt(np.mean(dy ** 2))), W=np.asarray(W).tolist(), y=y.tolist())
    print("  %-8s J/T_ideal - 1 = %+.4e | max |y - y_ideal| %.3e (rms %.3e) | cert %.3f | KS - mu0 %+.4f (min cell %+.4f)"
          " | |grad|_inf / T_ideal %.3e" % (label, r["gap"], r["dy_max"], r["dy_rms"], r["cert"], r["ks"], r["m_min"],
                                             r["grad_inf"]), flush=True)
    return r


print("== %s: start %s, class %s, K %d N %d; T_ideal %.8e (mdot %.6e, V_a %.6f)" % (tag, start, bool(cls), K, N,
                                                                                    pp.T_ideal, pp.mdot, pp.T_ideal / pp.mdot), flush=True)
r_fit = reading(W_fit, "fit")
r_0 = reading(W0, "start")
c = dict(throat=pp)
Wf, hist, n_rec = P.run_trsqp(np.asarray(W0, float), {}, c, pp.ta, sign=+1.0, max_segments=(QN_SEGS if QN_ON else 40), maxiter_per_seg=8,
                              margin=mg, tr0=(QN_TR0 if QN_ON else 0.02), tr_floor=0.02 / FDIV, bounds=None, backtrack=4)
r_f = reading(np.asarray(Wf, float), "landing")
res = dict(tag=tag, start=start, cls=cls, K=K, N=N, T_ideal=pp.T_ideal, fit=r_fit, start_r=r_0, landing=r_f,
           segments=len(hist), records=n_rec, hist=[list(map(float, h)) for h in hist], seconds=time.time() - t00,
           switches=dict(PSPL_JSCALE=os.environ.get("PSPL_JSCALE"), PSPL_TRFOLLOW=os.environ.get("PSPL_TRFOLLOW"),
                         backtrack=4, tr0=0.02, tr_floor=0.02 / FDIV, max_segments=40, maxiter=8),
           counters=(dict(mg.get("counters", {})) if mg else {}))
json.dump(res, open(os.path.join(rv.OUT, tag + ".json"), "w"), indent=1, default=float)
if QN_ON:
    json.dump(__import__("a1_qntr").LAST, open(os.path.join(rv.OUT, tag + "_report.json"), "w"), indent=1,
              default=float)
print("== %s done: %d accepted bases, %d records, %.0f s" % (tag, len(hist), n_rec, time.time() - t00), flush=True)
