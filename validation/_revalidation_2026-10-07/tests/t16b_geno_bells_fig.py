#!/usr/bin/env python3
"""T16b -- context figure: GENO's bells used as optima and as starts (CH4/O2 frozen, r_t = 1, eps 4). No computation."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402

plt.rcParams.update({"font.size": 11, "legend.fontsize": 9})


def wall(case):
    d = os.path.join(rv.RV, "geno", case)
    fn = [f for f in os.listdir(d) if f.startswith("profile")][0]
    a = np.loadtxt(os.path.join(d, fn))
    return a[:, 0], a[:, 1], open(os.path.join(d, "performance.dat")).read().split()


fig, ax = plt.subplots(figsize=(8.2, 4.2), constrained_layout=True)
for case, lab, st in (("bell_ideal_e4", "ideal bell (type 0), L 7.34", "-"),
                      ("bell_toc_e4_L4", "Rao TOC (type 2), L 4", "-"),
                      ("bell_toc_e4_L6", "Rao TOC (type 2), L 6", "--"),
                      ("bell_top_e4_L4", "TOP parabola (type 4), L 4", ":")):
    x, y, perf = wall(case)
    ax.plot(x, y, st, lw=1.6, label="%s: C_F %s" % (lab, perf[4]))
ax.set_xlabel("x / r_t")
ax.set_ylabel("y / r_t")
ax.set_title("GENO's bells, eps 4, CH4/O2 frozen gas (vacuum C_F, 4 decimals)")
ax.set_xlim(-0.6, 7.6)
ax.set_ylim(0.9, 2.15)
ax.grid(alpha=0.3)
ax.legend(loc="lower right", framealpha=0.95)
rv.savefig(fig, "16_geno_bells.png")
