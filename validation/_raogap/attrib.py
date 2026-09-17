"""Which knot produced the overnight gain, and what does the free tip
cost that J does not charge?

The walk moved two knots: the first +6.864 mm and the tip +5.247 mm,
everything between under 0.36 mm. Evaluates J with each move ALONE on
the same instrument, and prices the base each tip position creates with
the N2 slot's incumbent closure (which J does NOT contain).
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
import a1_ideal_march_jax as A1                             # noqa: E402
import a1_config_compare as CC                              # noqa: E402
import a1_plug_spline_opt as P                              # noqa: E402
import base_pressure as BP                                  # noqa: E402

w = CC.build_world(); ta = w["ta"]; c = P.build_case(w)
W0 = np.asarray(D["W0"], float); Ws = np.asarray(R["walks"][0]["W"], float)
d = Ws - W0
cases = [("W0 (the member)", W0),
         ("first knot only", W0 + np.where(np.arange(len(d)) == 0, d, 0.0)),
         ("tip only", W0 + np.where(np.arange(len(d)) == len(d) - 1, d, 0.0)),
         ("all but the two ends", W0 + np.where(
             (np.arange(len(d)) > 0) & (np.arange(len(d)) < len(d) - 1), d, 0.0)),
         ("W* (the walk's return)", Ws)]
print("== which knot carries the gain, and what the free tip costs ==",
      flush=True)
for tag, W in cases:
    t0 = time.time()
    out, sch = P.march_record(W, w, c)
    J = float(P.J_replay(jnp.asarray(W), w, c, sch, ta))
    wall = np.asarray(out["wall"])
    q = np.hypot(wall[:, 2], wall[:, 3])
    T, p, rho, cs, gam, M = [np.asarray(v) for v in A1.state_q(jnp.asarray(q), ta)]
    yb = float(wall[-1, 1])
    pb = float(np.asarray(BP.p_base(jnp.asarray(p[-1]), jnp.asarray(M[-1]),
                                    jnp.asarray(gam[-1]), float(P.PA))))
    jb = float(np.asarray(BP.base_term(pb, yb, float(P.PA))))
    # the sub-ambient stretch of wall the tip lift removes
    sub = p < float(P.PA)
    print("   %-22s J %.8e (dJ %+.4e N) | tip y %.5f m, p_w(tip)/p_a %.4f,"
          " wall below ambient over the last %d of %d stations |"
          " UNPRICED base term %+.4e N (cert %.3f, %.0f s)"
          % (tag, J, J - float(D["J0"]), yb, p[-1] / float(P.PA),
             int(sub.sum()), len(p), jb, float(out["cert_worst"]),
             time.time() - t0), flush=True)
