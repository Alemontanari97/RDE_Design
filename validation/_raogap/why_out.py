"""WHERE does Rao's transplant lose its margin, and to what?

Marches three contours on the same instrument: our member, Rao's
contour transplanted onto our 16 knots (the one measured out of class),
and Rao's contour AS WRITTEN on the march's own stations (measured in
class). Reports where the worst cells sit and what the wall angle does,
so the loss can be attributed to the curve or to its 16-knot image.
"""
import os, sys, json, time
import numpy as np
HERE = "/data10/falco/RDE/RDE_Design/validation"
sys.path.insert(0, HERE)
D = json.load(open(os.path.join(HERE, "_plug_tournament", "k81n41_v2",
                                "derive.json")))
os.environ.setdefault("PSPL_FAN", "axi")
os.environ["PSPL_L"] = "%.10f" % D["L"]
os.environ["PSPL_M"] = str(D["m"]); os.environ["PSPL_K"] = str(D["K"])
os.environ["PSPL_N"] = str(D["N"])
import a1_config_compare as CC                              # noqa: E402
import a1_plug_spline_opt as P                              # noqa: E402
from a1_plug_margin import np_margin, margin_dict           # noqa: E402

w = CC.build_world(); c = P.build_case(w)
K, N = D["K"], D["N"]
mg = margin_dict(D["rho"], D["floors"][0], D["m_ref"], D["orient"],
                 D["f_edge"], D["ell2"])
print("== where the margin is lost ==", flush=True)
print("   floor mu0_1 %.4f = m_ref/2 (m_ref %.4f = OUR member's own worst"
      " cell); fold at 0" % (D["floors"][0], D["m_ref"]), flush=True)
for tag, W in (("ours", np.asarray(D["W0"], float)),
               ("rao-on-our-16-knots", np.asarray(D["W_rao"], float))):
    out, sch = P.march_record(W, w, c, margin=mg)
    ms, dep, where = np_margin(out, sch, N, mg["orient"], mg["f_edge"],
                               mg["ell2"], with_depth=True)
    ms = np.asarray(ms); k = np.argsort(ms)[:12]
    cols = [where[i][0] for i in k]
    xq, yq, sq = P.wall_stations(W, c)
    th = np.degrees(np.arctan(np.asarray(sq)))
    d2 = np.diff(th, 2)
    print("   %-20s min cell %+.4f at %s; 12 worst in columns %s"
          % (tag, ms.min(), str(where[int(np.argmin(ms))]), sorted(set(cols))),
          flush=True)
    print("   %-20s wall angle: %.3f -> %.3f deg; |second difference| max"
          " %.3e deg, rms %.3e deg (the representation's own waviness)"
          % ("", th[0], th[-1], np.max(np.abs(d2)), float(np.sqrt(np.mean(d2**2)))),
          flush=True)
    print("   %-20s cells below the floor: %d of %d (%.2f %%)"
          % ("", int((ms < D["floors"][0]).sum()), ms.size,
             100.0 * (ms < D["floors"][0]).mean()), flush=True)
