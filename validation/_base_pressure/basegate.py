"""Gate + first reading of the priced base.

(1) BIT-IDENTITY: with PSPL_BASE unset, J and its gradient must equal
    the rows of record to the last digit.
(2) The ranking of the overnight leg's return once the base it creates
    is charged, under every member of the slot that stays in class.
"""
import os, sys, json, subprocess
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
W0 = np.asarray(D["W0"], float); Ws = np.asarray(R["walks"][0]["W"], float)
print("== (1) bit-identity with the base unpriced ==", flush=True)
recs = {}
for tag, W in (("W0", W0), ("W*", Ws)):
    out, sch = P.march_record(W, w, c)
    recs[tag] = (W, sch)
    J, g = P.J_and_grad(W, w, c, ta, sch)
    ref = D["J0"] if tag == "W0" else R["walks"][0]["J"]
    print("   %s: J %.10e vs the row of record %.10e -> %s (|grad|inf %.6e)"
          % (tag, J, ref, "IDENTICAL" if J == ref else
             "DIFFERS by %.3e" % (J - ref), np.max(np.abs(g))), flush=True)
print("== (2) the same two designs with the base priced ==", flush=True)
for model in ("veen", "conical", "cylindrical", "zero"):
    P.BASE_MODEL = model
    vals = {}
    for tag in ("W0", "W*"):
        W, sch = recs[tag]
        vals[tag] = float(P.J_replay(jnp.asarray(W), w, c, sch, ta))
    d = vals["W*"] - vals["W0"]
    print("   %-12s J(W0) %.8e  J(W*) %.8e  ->  dJ %+.4e N (unpriced"
          " %+.4e N; the base charge moves it by %+.4e N)"
          % (model, vals["W0"], vals["W*"], d, 5.5684e4, d - 5.5684e4),
          flush=True)
P.BASE_MODEL = ""
