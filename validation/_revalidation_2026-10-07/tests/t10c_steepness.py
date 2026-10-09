#!/usr/bin/env python3
"""T10c -- how steep is each optimiser case's plug? min over the designed plug wall of theta_wall + mu (the angle of the
C+ column at the wall): defect 1 (Newton stall) and the Rao 1961 stall live where it approaches 0. Read on the march of
the best spline of each reference (no new physics)."""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import rv                                          # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402

rep = rv.Report("t10c_steepness")


def thmu(wall, ta, x_from=-np.inf):
    w = np.asarray(wall)
    w = w[w[:, 0] >= x_from]
    q = np.hypot(w[:, 2], w[:, 3])
    M = np.asarray(A1.state_q(jnp.asarray(q), ta)[5])
    th = np.arctan2(w[:, 3], w[:, 2])
    v = np.degrees(th + np.arcsin(1.0 / np.maximum(M, 1.0 + 1e-12)))
    k = int(np.argmin(v))
    return float(v[k]), float(w[k, 0])


res = {}
import rao_posing as RP                            # noqa: E402
for case, nc, lab in (("rao_sdt_L0448", None, "Rao, methane, lip Mach 1.556"),
                      ("rao61_e381_pbR_mi15", 56, "Rao 1961, eps 3.81"),
                      ("axial_e381_RD04_mi15", 56, "axial exit")):
    rp = RP.RaoPosing(os.path.join(rv.RV, "geno", case), K=120, n_fan=20, m=10, design=True, n_cplus=nc)
    out, _ = rp.march_record(rp.fit_geno())
    v, x = thmu(out["wall"], rp.ta, rp.g.x_s)
    res[lab] = dict(min_theta_plus_mu=v, at_x=x)
    rep.note("%-30s min(theta_wall + mu) on the designed plug = %+.2f deg at x %.3f" % (lab, v, x))
import planar_posing as PP                         # noqa: E402
pp = PP.PlanarPlug(K=80, N=21, m=12, L=2.0)
out, _ = pp.march_record(pp.fit_ideal())
v, x = thmu(out["wall"], pp.ta)
res["planar ideal plug"] = dict(min_theta_plus_mu=v, at_x=x)
rep.note("%-30s min(theta_wall + mu) on the plug = %+.2f deg at x %.3f" % ("planar ideal plug", v, x))
os.environ.update(dict(TWOP_GAS=os.path.join(rv.OUT, "t08c_gas.json"),
                       TWOP_ART="/tmp/claude-1700/-data10-falco-MOSE/92599c7b-9637-4352-802d-d26f8eac9fd5/scratchpad/twop_art"))
import a1_twowall as T                             # noqa: E402
tw = T.TwoWall()
out, _ = tw.march_record(np.asarray(tw.W_ref, float))
v, x = thmu(out["wall"], tw.ta)
res["annular (Migdal) plug"] = dict(min_theta_plus_mu=v, at_x=x)
rep.note("%-30s min(theta_wall + mu) on the plug = %+.2f deg at x %.3f" % ("annular (Migdal) plug", v, x))
rep.check("Rao 1961 is the steepest plug of the set (smallest theta + mu)", res["Rao 1961, eps 3.81"]["min_theta_plus_mu"],
          0.0, ok=bool(res["Rao 1961, eps 3.81"]["min_theta_plus_mu"] == min(r["min_theta_plus_mu"] for r in res.values())))
sys.exit(rep.save(res))
