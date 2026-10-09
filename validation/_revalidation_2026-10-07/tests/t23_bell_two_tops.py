#!/usr/bin/env python3
"""T23 -- are there really two tops? The thrust (grid 81 x 240, the walks' own grid, 8 points) along the straight line
in design space from the landing of the stretched start (theta_B 8.16 deg) to the landing of the cylinder start (12.53
deg). A valley between them = two tops, and the driver's CONVERGED was right; a monotone rise = the driver stopped
where it should not have.  -> out/t23_bell_two_tops.json, figs/23_bell_two_tops.png"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402
import bell_posing as BP                           # noqa: E402

a = json.load(open(os.path.join(rv.OUT, "t15_bell_ideal_stretched_NI81.json")))
b = json.load(open(os.path.join(rv.OUT, "t15_bell_ideal_extended_NI81.json")))
bp = BP.BellPosing(a["L"], a["yL"], NI=81, Nw=240, M=8)
Va, Vb = np.asarray(a["landing"]["V"], float), np.asarray(b["landing"]["V"], float)
ts = np.r_[np.linspace(-0.04, 0.04, 5), np.linspace(0.1, 0.9, 9), np.linspace(0.96, 1.04, 5)]
rows = []
for t in ts:
    out, _ = bp.record(Va + t * (Vb - Va))
    rows.append((float(t), bp.J_of(out), float(out["cert_worst"])))
    print("  t %+.3f  theta_B %.3f deg  J %.10e  cert %.2f" % (t, np.degrees((Va + t * (Vb - Va))[0]), rows[-1][1],
                                                              rows[-1][2]), flush=True)
r = np.asarray(rows)
J0 = r[np.argmin(np.abs(r[:, 0] - 1.0)), 1]
fig, ax = plt.subplots(figsize=(8.2, 4.4), constrained_layout=True)
ax.plot(r[:, 0], 1e6 * (r[:, 1] - J0) / J0, "o-")
ax.axvline(0, color="C1", ls=":", label="result from the stretched start (theta_B 8.16 deg)")
ax.axvline(1, color="C2", ls=":", label="result from the cylinder start (theta_B 12.53 deg)")
ax.set_xlabel("position on the straight line between the two results")
ax.set_ylabel("thrust vs the ideal-bell result (ppm)")
ax.set_title("Ideal bell, 8-point wall, grid 81 x 240: thrust between the two results")
ax.legend(loc="best")
rv.savefig(fig, "23_bell_two_tops.png")
json.dump(dict(t=r[:, 0].tolist(), J=r[:, 1].tolist(), cert=r[:, 2].tolist()),
          open(os.path.join(rv.OUT, "t23_bell_two_tops.json"), "w"), indent=1)
