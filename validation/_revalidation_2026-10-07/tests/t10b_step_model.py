#!/usr/bin/env python3
"""T10b -- how far is the walk's step model valid? The SQP models a step by the frozen replay (the recorded schedule of
discrete decisions, replayed at the new design); a step is real only where the replay equals the re-recorded march.
Measured along +grad J from the best spline of GENO's contour in the three Rao posings (T08b methane, T10 Rao 1961,
T10 axial exit), at h = 1e-4 ... 1e-2 (wall displacement), finely between 1e-3 and 3e-3 where the decisions break.
Measured: where a decision breaks and how large the replay error is then. Run with A1_NEWTON_RESCUE=1 (as the walks)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import rv                                          # noqa: E402
import rao_posing as RP                            # noqa: E402

rep = rv.Report("t10b_step_model")
H = np.array([1e-4, 3e-4, 1e-3, 1.2e-3, 1.5e-3, 2e-3, 2.5e-3, 3e-3, 1e-2])
CASES = [("rao_sdt_L0448", None, "Rao, methane plug"), ("rao61_e381_pbR_mi15", 56, "Rao 1961, eps 3.81 (steep plug)"),
         ("axial_e381_RD04_mi15", 56, "axial exit, theta_E = 0")]
res = {}
for case, nc, lab in CASES:
    rp = RP.RaoPosing(os.path.join(rv.RV, "geno", case), K=120, n_fan=20, m=10, design=True, n_cplus=nc)
    W = rp.fit_geno()
    out, S = rp.march_record(W)
    J0 = float(rp.J_of(out))
    g = np.asarray(jax.grad(lambda z: rp.J_replay(z, S))(jnp.asarray(W)))
    d = g / np.linalg.norm(g)
    # the wall's steepness at the first designed station: theta + mu
    k = int(np.argmax(rp.free))
    th = np.degrees(np.arctan(np.asarray(rp.walls(W)[2])[k]))
    err, gain = [], []
    for h in H:
        Jr = float(rp.J_replay(jnp.asarray(W + h * d), S))
        o2, _ = rp.march_record(W + h * d)
        Jc = float(rp.J_of(o2))
        err.append(abs(Jr - Jc) / J0)
        gain.append((Jc - J0) / J0)
    res[case] = dict(label=lab, err=err, gain=gain, theta_wall_first=float(th))
    rep.note("%-22s |replay - record| / J: %s ; record gain: %s" % (
        case, " ".join("%.1e" % v for v in err), " ".join("%+.1e" % v for v in gain)))
valid = {c: float(H[np.where(np.array(r["err"]) > 1e-9)[0][0] - 1]) if np.any(np.array(r["err"]) > 1e-9) else float(H[-1])
         for c, r in res.items()}
rep.note("largest h with replay = record (1e-9): %s" % valid)
# the measured reach of the step model: exact (<= 1e-9) up to h_exact in every posing; beyond, a broken decision costs up
# to 1e-2 in all three (methane 1.2e-2 at 2.5e-3, Rao 1961 3.5e-2 at 3e-3, axial 1.5e-2 at 1e-2): the steep plug's model
# is NOT shorter-ranged -- its stall is ill-conditioning (see the record gain along +grad J: best step ~2e-4)
h_exact = min(valid.values())
rep.check("the step model (frozen replay) equals the re-recorded march to 1e-9 up to h = 1.5e-3 in all three posings",
          h_exact, 1.5e-3, ok=bool(h_exact >= 1.5e-3))
for c, r in res.items():
    gn = np.array(r["gain"])
    k = int(np.argmax(gn))
    rep.note("%-22s best record gain along +grad J: %+.1e at h = %.0e" % (c, gn[k], H[k]))
fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
for (case, r), mk in zip(res.items(), ("o", "s", "^")):
    ax.loglog(H, np.maximum(r["err"], 1e-17), mk + "-", label=r["label"])
ax.axhline(1e-9, color="0.6", lw=0.8, ls="--")
ax.set_xlabel("wall displacement h along +grad J (units of y_E)")
ax.set_ylabel("|J(frozen replay) - J(re-recorded march)| / J")
ax.set_title("How far the SQP's step model is exact (from the best spline, along +grad J)")
ax.legend(fontsize=8)
ax.grid(alpha=0.3, which="both")
rv.savefig(fig, "10b_step_model.png")
sys.exit(rep.save(dict(h=H.tolist(), res=res, valid=valid)))
