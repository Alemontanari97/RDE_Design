#!/usr/bin/env python3
"""T22 -- is the bell engine's objective a sawtooth in the attachment angle? The coded J starts at the first throat-arc
station theta_1 = theta_B / n_B, n_B = ceil(theta_B / da): the panel [0, theta_1] is left out, and its size jumps when
n_B changes (every da = 0.5 deg of theta_B). J_A (A1_OBJDOM=A, the engine's own panel-inclusive objective) adds it.
Here theta_B is swept around the second top of the ideal-bell walk (8.16 deg) with the other knots fixed; both
objectives are read from the same marches.  -> figs/22_bell_panel.png, out/t22_bell_panel.json"""
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
import a1_toc_variational_jax as TV                # noqa: E402

d = json.load(open(os.path.join(rv.OUT, "t15_bell_ideal_stretched_NI81.json")))
bp = BP.BellPosing(d["L"], d["yL"], NI=41, Nw=120, M=8)
V0 = np.asarray(d["landing"]["V"], float)
throat = TV.throat_station(bp.cfg, bp.tab)
ths = np.radians(np.arange(7.55, 8.80, 0.05))
rows = []
for th in ths:
    V = V0.copy()
    V[0] = th
    out, plan = bp.record(V)
    Jc = float(TV.thrust_J(out["wall"], bp.tab, state_fn=bp.state))
    Ja = float(TV.thrust_J_A(out["wall"], bp.tab, throat, state_fn=bp.state))
    nB = int(np.ceil(np.degrees(th) / bp.cfg["da_deg"] - 1e-12))
    rows.append((float(np.degrees(th)), Jc, Ja, nB, float(out["cert_worst"])))
    print("  theta_B %.2f deg  n_B %d  J coded %.10e  J with the panel %.10e  cert %.2f" % rows[-1][:1] + rows[-1][1:3]
          if False else "  theta_B %.2f deg  n_B %2d  J coded %.10e  J with the panel %.10e  cert %.2f"
          % (rows[-1][0], rows[-1][3], rows[-1][1], rows[-1][2], rows[-1][4]), flush=True)
r = np.asarray(rows)
fig, ax = plt.subplots(figsize=(8.2, 4.6), constrained_layout=True)
J0 = r[0, 2]
ax.plot(r[:, 0], 1e6 * (r[:, 1] - r[0, 1]) / J0, "o-", label="the engine's coded thrust (first arc panel left out)")
ax.plot(r[:, 0], 1e6 * (r[:, 2] - J0) / J0, "s-", label="thrust with that panel (the engine's option A1_OBJDOM=A)")
for k in range(16, 19):
    ax.axvline(k * bp.cfg["da_deg"], color="0.6", lw=0.8, ls=":")
ax.set_xlabel("attachment angle theta_B (deg); dotted: multiples of 0.5 deg, where the arc gains a station")
ax.set_ylabel("thrust change (ppm)")
ax.set_title("Bell engine: thrust vs attachment angle, other wall points fixed")
ax.legend(loc="best")
rv.savefig(fig, "22_bell_panel.png")
json.dump(dict(theta_B=r[:, 0].tolist(), J_coded=r[:, 1].tolist(), J_panel=r[:, 2].tolist(), n_B=r[:, 3].tolist()),
          open(os.path.join(rv.OUT, "t22_bell_panel.json"), "w"), indent=1)
