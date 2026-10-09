#!/usr/bin/env python3
"""T08c (one walk) -- the PRODUCTION carrier (a1_twowall.TwoWall, its default two-wall posing: GENO's arcs as data, a
clamped spline through 12 + 12 knots after them, the exit points pinned, vacuum) with the driver run_trsqp (production
switches), on GENO's new Migdal walls (T05: SDT mean gas, M_i 1.556, eps 4, Ne 2000) given through TWOP_GAS.

Known optimum (value): in vacuum with the inlet and the exit annulus fixed, the thrust is the exit momentum flux
int (rho u^2 + p) dA; for a fixed mass and exit area it is largest for the uniform axial exit, F_1D = mdot V_e + p_e A_e
(the perfect nozzle: GENO's pair). The carrier's discrete C_F of GENO's own walls, J_ref, is the reference AT THE SAME
RESOLUTION (T05: the march's thrust error at (140,31) is +1.5e-4); a landing above it by more than that error is a
symptom (folding: the MOC credits coalescing compressions isentropically).
usage: t08c_migdal_walk.py <class 0|1> [amplitude]   -> out/t08c_walk_<class>[_a<amp>].json
Start: the reference + a bump amplitude sin(pi t) on both walls' knots (t = knot fraction along the wall), default 0.01.
"""
import json
import os
import sys
import time

RV = "/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07"
sys.path.insert(0, os.path.join(RV, "ref"))
import rv                                          # noqa: E402
gas_json = os.path.join(rv.OUT, "t08c_gas.json")
c = json.load(open(os.path.join(RV, "geno", "migdal_sdt_eps4_ni1001_ne2000", "case.json")))
g_, R_, T0, P0 = c["thermo"]["gamma"], c["thermo"]["R"], c["gas"][2], c["gas"][3]
json.dump(dict(gamma=g_, R=R_, T0=T0, P0=P0, M_in=c["Mi"], geno_run=os.path.join(RV, "geno", "migdal_sdt_eps4_ni1001_ne2000"),
               T_tab=[0.2 * T0 / (1 + 0.5 * (g_ - 1) * 4.5 ** 2), 1.02 * T0]), open(gas_json, "w"), indent=1)
cls = int(sys.argv[1])
AMP = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01
os.environ.update(dict(TWOP_GAS=gas_json, PSPL_JSCALE="radius", PSPL_TRFOLLOW="1",
                       TWOP_ART="/tmp/claude-1700/-data10-falco-MOSE/92599c7b-9637-4352-802d-d26f8eac9fd5/scratchpad/twop_art"))
import numpy as np                                 # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import a1_twowall as T                             # noqa: E402
import a1_plug_spline_opt as P                     # noqa: E402

tag = "t08c_walk_%d" % cls + ("" if AMP == 0.01 else "_a%g" % AMP)
QN_ON = P.DRIVER == "qntr"     # the agnostic driver (a1_qntr, default since 2026-10-08): one setting for every case
if QN_ON:
    tag += "_qntr"
QN_SEGS, QN_TR0 = 100, 0.01
t00 = time.time()
tw = T.TwoWall()
CL = json.load(open("/data10/falco/RDE/RDE_Design/validation/_rde_tournament/stech/class_nofold_2026-09-28.json"))
W_ref = np.asarray(tw.W_ref, float)
tp = (tw.kp[:-1] - tw.kp[0]) / (tw.kp[-1] - tw.kp[0])
ts = (tw.ks[:-1] - tw.ks[0]) / (tw.ks[-1] - tw.ks[0])
W0 = W_ref + AMP * np.r_[np.sin(np.pi * tp), np.sin(np.pi * ts)]
mg = None
if cls:
    mg = tw.margin_dict(mu0=CL["floors"][0], rho=CL["rho"], m_ref=CL["m_ref"])
    mg["tol"] = CL["gap"]


def reading(W, label):
    out, S = tw.march_record(W, margin=tw.margin_dict(mu0=CL["floors"][0], rho=CL["rho"], m_ref=CL["m_ref"]))
    J = float(tw.J_of(out))
    g = np.asarray(jax.grad(lambda z: tw.J_replay(z, S))(jnp.asarray(W)))
    gp, gs = T.wall_gap(tw, W, W_ref)
    r = dict(J=J, cert=float(out["cert_worst"]), ks=float(out["margin_ks"]) - CL["floors"][0],
             m_min=float(out["margin_min"]), grad_inf=float(np.max(np.abs(g))), gap_plug=gp, gap_shroud=gs,
             W=np.asarray(W).tolist())
    print("  %-8s C_F %.9f (1-D %.9f: %+.3e) | gap to GENO plug %.2e shroud %.2e | cert %.3f | KS - mu0 %+.4f (min cell"
          " %+.4f) | |grad|_inf %.3e" % (label, J, tw.CF_1d, J / tw.CF_1d - 1.0, gp, gs, r["cert"], r["ks"], r["m_min"],
                                          r["grad_inf"]), flush=True)
    return r


print("== %s: class %s; C_F,1D %.9f" % (tag, bool(cls), tw.CF_1d), flush=True)
r_ref = reading(W_ref, "GENO")
r_0 = reading(W0, "start")
Wf, hist, n_rec = P.run_trsqp(W0, {}, dict(throat=tw), tw.ta, sign=+1.0, max_segments=(QN_SEGS if QN_ON else 30), maxiter_per_seg=8, margin=mg,
                              tr0=(QN_TR0 if QN_ON else 0.01), tr_floor=0.01 / 256.0, bounds=None, backtrack=4)
r_f = reading(np.asarray(Wf, float), "landing")
json.dump(dict(tag=tag, cls=cls, CF_1d=tw.CF_1d, ref=r_ref, start_r=r_0, landing=r_f, segments=len(hist), records=n_rec,
               hist=[list(map(float, h)) for h in hist], seconds=time.time() - t00), open(os.path.join(rv.OUT, tag + ".json"), "w"),
          indent=1, default=float)
if QN_ON:
    json.dump(__import__("a1_qntr").LAST, open(os.path.join(rv.OUT, tag + "_report.json"), "w"), indent=1,
              default=float)
print("== %s done: %d accepted bases, %d records, %.0f s" % (tag, len(hist), n_rec, time.time() - t00), flush=True)
