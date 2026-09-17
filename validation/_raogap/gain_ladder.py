"""Does the overnight leg's gain survive refinement?

J(W*) - J(W0) is +5.57e4 N at the rung the walk ran on, 2.4 percent of
that rung's band_J. If the gain is physics it must persist as the
station count is refined; if it is the optimizer eating the
discretisation at the two ends (the walk moved the FIRST knot +6.9 mm
and the tip +5.25 mm, the two places the march is weakest), it will
shrink. Same schedule-frozen replay, same N, K on the doubling ladder.
"""
import os, sys, json, time
import numpy as np
HERE = "/data10/falco/RDE/RDE_Design/validation"
sys.path.insert(0, HERE)
D = json.load(open(os.path.join(HERE, "_plug_tournament", "k81n41_v2",
                                "derive.json")))
R = json.load(open(os.path.join(HERE, "_plug_tournament", "k81n41",
                                "campaign_s20_i8_st3_A.json")))
os.environ.setdefault("PSPL_FAN", "axi")
os.environ["PSPL_L"] = "%.10f" % D["L"]
os.environ["PSPL_M"] = str(D["m"]); os.environ["PSPL_K"] = str(D["K"])
os.environ["PSPL_N"] = str(D["N"])
import jax.numpy as jnp                                     # noqa: E402
import a1_config_compare as CC                              # noqa: E402
import a1_plug_spline_opt as P                              # noqa: E402

w = CC.build_world(); ta = w["ta"]; c = P.build_case(w)
# THE MESH MUST BE REFINED IN BOTH DIRECTIONS (first attempt, 15:00:
# stations alone gave 161x41 with cert 6.301 -- an unbalanced mesh does
# not certify, so its dJ is not a measurement). The rungs are the
# tournament's own: (81,41) -> (161,81) -> (321,161).
W0 = np.asarray(D["W0"], float)
Ws = np.asarray(R["walks"][0]["W"], float)
print("== does the leg's gain survive refinement? ==", flush=True)
print("   |W* - W0| max %.3e m (first knot %+.3e, tip %+.3e)"
      % (np.max(np.abs(Ws - W0)), (Ws - W0)[0], (Ws - W0)[-1]), flush=True)
for K, N in ((81, 41), (161, 81), (321, 161)):
    t0 = time.time(); row = {}
    cK = P.build_case(w, N=N)
    cK["xk"] = c["xk"]
    for tag, W in (("W0", W0), ("W*", Ws)):
        out, sch = P.march_record(W, w, cK, K=K)
        row[tag] = (float(P.J_replay(jnp.asarray(W), w, cK, sch, ta, K=K)),
                    float(out["cert_worst"]))
    dJ = row["W*"][0] - row["W0"][0]
    print("   (%d,%d): J(W0) %.8e (cert %.3f)  J(W*) %.8e (cert %.3f)"
          "  ->  dJ %+.4e N = %+.2e of J   (%.0f s)"
          % (K, N, row["W0"][0], row["W0"][1], row["W*"][0], row["W*"][1],
             dJ, dJ / row["W0"][0], time.time() - t0), flush=True)
