"""Is the gap to Rao a matter of CONSTRAINT or of INFORMATION?

Walks the straight segment W(lam) = W0 + lam (W_rao - W0) between our
member and Rao's transplanted contour on the SAME knots, the SAME start
line and the SAME march, and reports J, the fold margin and the
certificate along it; then projects the adjoint gradient at our member
onto that direction and checks it against the segment's own slope.

Reading: if |J(lam) - J(0)| stays under band_J for every lam, the
functional cannot tell the two contours apart at the resolution the
ladder resolves -- the optimum is a VALLEY and the geometry is decided
by the constraints, not by the objective.
"""
import os, sys, json, time
import numpy as np

HERE = "/data10/falco/RDE/RDE_Design/validation"
sys.path.insert(0, HERE)
D = json.load(open(os.path.join(HERE, "_plug_tournament", "k81n41_v2",
                                "derive.json")))
os.environ.setdefault("PSPL_FAN", "axi")
os.environ["PSPL_L"] = "%.10f" % D["L"]
os.environ["PSPL_M"] = str(D["m"])
os.environ["PSPL_K"] = str(D["K"])
os.environ["PSPL_N"] = str(D["N"])
import jax.numpy as jnp                                    # noqa: E402
import a1_config_compare as CC                             # noqa: E402
import a1_plug_spline_opt as P                             # noqa: E402
from a1_plug_margin import margin_dict, np_margin          # noqa: E402

w = CC.build_world(); ta = w["ta"]; c = P.build_case(w)
W0 = np.asarray(D["W0"], float)
WR = np.asarray(D["W_rao"], float)
d = WR - W0
mg = margin_dict(D["rho"], D["floors"][0], D["m_ref"], D["orient"],
                 D["f_edge"], D["ell2"])
band_J = float(D["band_J"]); band_W = float(D["band_W_rep"])
print("== the segment from our member to Rao's contour ==", flush=True)
print("   |W_rao - W0|inf %.4e m, |.|2 %.4e m; band_W(rep) %.3e;"
      " band_J %.3e N (%.2e of J)"
      % (np.max(np.abs(d)), np.linalg.norm(d), band_W, band_J,
         band_J / D["J0"]), flush=True)
rows = []
for lam in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
    t0 = time.time()
    W = W0 + lam * d
    out, sch = P.march_record(W, w, c, margin=mg)
    J = float(P.J_replay(jnp.asarray(W), w, c, sch, ta))
    ms, dep, where = np_margin(out, sch, D["N"], mg["orient"], mg["f_edge"],
                               mg["ell2"], with_depth=True)
    rows.append(dict(lam=lam, J=J, dJ=J - D["J0"], cert=float(out["cert_worst"]),
                     mmin=float(np.min(ms))))
    print("   lam %.2f: J %.8e (dJ %+.4e N = %+.2e of J, %.3f of band_J),"
          " cert %.3f, min cell %+.4f (%.0f s)"
          % (lam, J, J - D["J0"], (J - D["J0"]) / D["J0"],
             abs(J - D["J0"]) / band_J, float(out["cert_worst"]),
             float(np.min(ms)), time.time() - t0), flush=True)

# the adjoint at our member, projected on the direction of Rao
out0, sch0 = P.march_record(W0, w, c, margin=mg)
J0, g0 = P.J_and_grad(W0, w, c, ta, sch0)
u = d / np.linalg.norm(d)
proj = float(np.dot(g0, u))
print("   |grad J|inf %.4e N/m; its projection on the Rao direction"
      " %.4e N/m; the segment's own slope (J(1)-J(0))/|d| %.4e N/m"
      % (np.max(np.abs(g0)), proj,
         (rows[-1]["J"] - rows[0]["J"]) / np.linalg.norm(d)), flush=True)
print("   the whole traverse in units of the band: |dJ|max/band_J %.4f"
      % (max(abs(r["dJ"]) for r in rows) / band_J), flush=True)
json.dump(dict(rows=rows, grad_inf=float(np.max(np.abs(g0))), proj=proj,
               band_J=band_J, band_W=band_W, dnorm=float(np.linalg.norm(d))),
          open(os.path.join(HERE, "_raogap", "segment.json"), "w"), indent=1)
