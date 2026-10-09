#!/usr/bin/env python3
"""T19 -- Rao 1961: how the old and the new driver approach the best spline of Rao's contour (walk grid), from the two
starts. Old: the default segmented trust-constr walk, then (by hand) its continuation with one step per segment; new:
the agnostic driver with the settings of every other case. No new computation: the walks' own records.
-> figs/19_rao61_history.png, out/t19_history.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402

plt.rcParams.update({"font.size": 11, "legend.fontsize": 9})
C = "rao61_e381_pbR_mi15"
Jl = lambda n: json.load(open(os.path.join(rv.OUT, "t10_walk_%s_%s.json" % (C, n))))   # noqa: E731
fig, ax = plt.subplots(figsize=(8.2, 5.4), constrained_layout=True)
out = {}
FLOOR = 1e-2
for start, col, lab in (("bump", "C0", "start: Rao's contour deformed (up to 1 %)"),
                        ("half", "C1", "start: average of Rao's contour and a straight line")):
    try:
        old, cont, new = Jl(start), Jl("cont_%s_it2" % start), Jl("%s_qntr" % start)
    except FileNotFoundError as err:
        print("skip %s: %s" % (start, err))
        continue
    Jf, Jg = old["fit"]["J"], old["J_geno"]
    def gap(h):
        return np.maximum(1e6 * (Jf - np.asarray(h)[:, 1]) / Jg, FLOOR)
    h_old, h_cont, h_new = np.asarray(old["hist"]), np.asarray(cont["hist"]), np.asarray(new["hist"])
    n_old = len(h_old)
    x_old = np.arange(n_old)
    x_cont = n_old + np.arange(len(h_cont))
    ax.semilogy(x_old, gap(h_old), "-", color=col, lw=1.0, alpha=0.6)
    ax.semilogy(x_cont, gap(h_cont), "--", color=col, lw=1.0, alpha=0.6)
    ax.semilogy(np.arange(len(h_new)), gap(h_new), "o-", color=col, lw=2.0, ms=4, label="new driver, " + lab)
    ax.annotate("old driver stops\n(%.0f min)" % (old["seconds"] / 60.0), (n_old - 1, gap(h_old)[-1]),
                (n_old + 3, gap(h_old)[-1] * (4.0 if start == "bump" else 0.25)), fontsize=8, color=col,
                arrowprops=dict(arrowstyle="->", color=col, lw=0.7))
    out[start] = dict(old=dict(bases=n_old, seconds=old["seconds"], records=old["records"],
                               landing_minus_fit=(old["landing"]["J"] - Jf) / Jg),
                      cont=dict(bases=len(h_cont), seconds=cont["seconds"], records=cont["records"],
                                landing_minus_fit=(cont["landing"]["J"] - Jf) / Jg),
                      new=dict(bases=len(h_new), seconds=new["seconds"], records=new["records"],
                               landing_minus_fit=(new["landing"]["J"] - Jf) / Jg, stop=(new.get("qntr") or {}).get("stop")))
ax.plot([], [], "-", color="0.4", lw=1.0, label="old driver, default settings")
ax.plot([], [], "--", color="0.4", lw=1.0, label="old driver continued by hand, one short step per segment")
ax.axhline(FLOOR, color="0.6", lw=0.8)
ax.text(0.5, FLOOR * 1.25, "at or above the closest curve", fontsize=8, color="0.4")
ax.set_xlabel("step of the optimiser (accepted)")
ax.set_ylabel("closest curve to Rao's contour minus optimiser (ppm of thrust)")
ax.set_title("Rao 1961: how close the optimiser gets to Rao (on its own grid)")
ax.legend(loc="upper right")
rv.savefig(fig, "19_rao61_history.png")
json.dump(out, open(os.path.join(rv.OUT, "t19_history.json"), "w"), indent=1, default=float)
print(json.dumps(out, indent=1, default=float))
