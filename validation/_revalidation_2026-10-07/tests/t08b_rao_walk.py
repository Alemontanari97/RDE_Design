#!/usr/bin/env python3
"""T08b (one walk) -- the model's SQP driver (run_trsqp, production switches PSPL_BACKTRACK=4, PSPL_JSCALE=radius,
PSPL_TRFOLLOW=1) re-designing the plug of GENO's Rao design downstream of the point where the lip's first wave lands
(x_s) up to the end D (pinned), with everything else GENO's own data (ref/rao_posing.py: GENO's last internal C+ as the
start line, its internal contour up to x_s, the lip fan to GENO's lip ambient p_a = 96086 Pa, the free jet).

Why GENO's contour is the optimum of this problem: GENO builds it by Rao's variational method (the C- control surface
ED with f2 = const, the corner conditions at E for p_a and at D) and marches it BACKWARD to the throat, so its inflow
is an output of the design (verified on GENO's code: the only inputs are the lip state and one constraint). Every
contour of this posing has a C- from E carrying the same mass to the same end point D, i.e. it belongs to Rao's
admissible set; Rao's contour belongs to this posing (with its own upstream data); so it maximises the thrust here.
usage: t08b_rao_walk.py <start A|C> <class 0|1> [floor_div]  -> out/t08b_walk_<start><class>.json
  A = GENO's contour fitted by the spline + a bump 0.01 sin(pi t) on [x_s, D]; C = the chord from (x_s, y_s) to D.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
os.environ.setdefault("PSPL_JSCALE", "radius")
os.environ.setdefault("PSPL_TRFOLLOW", "1")
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import rao_posing as RP                            # noqa: E402
import a1_plug_spline_opt as P                     # noqa: E402

start, cls = sys.argv[1], int(sys.argv[2])
FDIV = float(sys.argv[3]) if len(sys.argv) > 3 else 256.0
tag = "t08b_walk_%s%d" % (start, cls)
QN_ON = P.DRIVER == "qntr"     # the agnostic driver (a1_qntr, default since 2026-10-08): one setting for every case
if QN_ON:
    tag += "_qntr"
QN_SEGS, QN_TR0 = 100, 0.01
t00 = time.time()
rp = RP.RaoPosing(os.path.join(rv.RV, "geno", "rao_sdt_L0448"), K=120, n_fan=20, m=10, design=True)
g = rp.g
W_fit = rp.fit_geno()
t = (rp.xk[:-1] - g.x_s) / (g.D[0] - g.x_s)
W0 = W_fit + 0.01 * np.sin(np.pi * t) if start == "A" else g.y_s + (g.D[1] - g.y_s) * t
CLASS = json.load(open("/data10/falco/RDE/RDE_Design/validation/_rde_tournament/stech/class_nofold_2026-09-28.json"))
mg = None
if cls:
    mg = rp.margin_dict(mu0=CLASS["floors"][0], rho=CLASS["rho"], m_ref=CLASS["m_ref"])
    mg["tol"] = CLASS["gap"]
out_g, _ = rp.march_record(None)
J_geno = float(rp.J_of(out_g))


def reading(W, label):
    out, S = rp.march_record(W, margin=rp.margin_dict(mu0=CLASS["floors"][0], rho=CLASS["rho"], m_ref=CLASS["m_ref"]))
    J = float(rp.J_of(out))
    gr = np.asarray(jax.grad(lambda z: rp.J_replay(z, S))(jnp.asarray(W)))
    B, c = rp.basis()
    y = B @ np.asarray(W) + c
    dy = (y - rp.sy_g)[rp.free]
    r = dict(J=J, gap=J / J_geno - 1.0, cert=float(out["cert_worst"]), ks=float(out["margin_ks"]) - CLASS["floors"][0],
             grad_inf=float(np.max(np.abs(gr))) / J_geno, dy_max=float(np.max(np.abs(dy))),
             dy_rms=float(np.sqrt(np.mean(dy ** 2))), W=np.asarray(W).tolist(), y=y.tolist(), grad=gr.tolist())
    print("  %-8s J/J(GENO contour) - 1 = %+.4e | max |y - y_GENO| %.3e (rms %.3e) | cert %.3f | KS - mu0 %+.4f |"
          " |grad|_inf / J %.3e" % (label, r["gap"], r["dy_max"], r["dy_rms"], r["cert"], r["ks"], r["grad_inf"]),
          flush=True)
    return r


print("== %s: start %s, class %s; J(GENO contour) %.10e (cert %.3f); x_s %.5f -> D %s; %d knots (%d free)" % (
    tag, start, bool(cls), J_geno, float(out_g["cert_worst"]), g.x_s, g.D, rp.m, rp.m - 1), flush=True)
r_fit = reading(W_fit, "fit")
r_0 = reading(W0, "start")
Wf, hist, n_rec = P.run_trsqp(np.asarray(W0, float), {}, dict(throat=rp), rp.ta, sign=+1.0, max_segments=(QN_SEGS if QN_ON else 30),
                              maxiter_per_seg=6, margin=mg, tr0=(QN_TR0 if QN_ON else 0.01), tr_floor=0.01 / FDIV, bounds=None, backtrack=4)
r_f = reading(np.asarray(Wf, float), "landing")
json.dump(dict(tag=tag, start=start, cls=cls, J_geno=J_geno, fit=r_fit, start_r=r_0, landing=r_f, segments=len(hist),
               records=n_rec, hist=[list(map(float, h)) for h in hist], seconds=time.time() - t00,
               switches=dict(PSPL_JSCALE=os.environ.get("PSPL_JSCALE"), PSPL_TRFOLLOW=os.environ.get("PSPL_TRFOLLOW"),
                             backtrack=4, tr0=0.01, tr_floor=0.01 / FDIV, max_segments=30, maxiter=6)),
          open(os.path.join(rv.OUT, tag + ".json"), "w"), indent=1, default=float)
if QN_ON:
    json.dump(__import__("a1_qntr").LAST, open(os.path.join(rv.OUT, tag + "_report.json"), "w"), indent=1,
              default=float)
print("== %s done: %d accepted bases, %d records, %.0f s" % (tag, len(hist), n_rec, time.time() - t00), flush=True)
