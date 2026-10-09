#!/usr/bin/env python3
"""T20 -- the Humphreys slide's figure before the finer-grid check ends: their Table 3 (Rao's contour, printed) and our
SQP results (the two walks, out/t10_walk_hth71_rao_mi17_*_qntr.json) on GENO's Rao contour of the same problem
(geno/hth71_rao_mi17), and the differences; t17 hth replaces figs/17_hth.png when its three-grid reading ends.
Also writes the provisional doc/num_hth*.tex (optimiser's-grid numbers only)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402
import rao1961 as R61                              # noqa: E402
import rao_posing as RP                            # noqa: E402
import json                                        # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval     # noqa: E402

plt.rcParams.update({"font.size": 11, "legend.fontsize": 9})
h = R61.hth_rao(n=20001)
rp = RP.RaoPosing(os.path.join(rv.RV, "geno", "hth71_rao_mi17"), K=120, n_fan=20, m=10, design=True, n_cplus=56)
g = rp.g
x0 = float(g.x_s)          # the designed part only: upstream of x_s GENO's internal part depends on its lip Mach
xd = np.linspace(x0, g.D[0], 800)
yg = rp.wall_of(xd)[0]
tx, ty = R61.TAB3_HTH[:, 0] / h["R_E_in"], R61.TAB3_HTH[:, 1] / h["R_E_in"]
fig, ax = plt.subplots(2, 1, figsize=(8.2, 5.6), constrained_layout=True, sharex=True,
                       gridspec_kw=dict(height_ratios=[1.7, 1]))
A, B = ax
A.plot(xd, yg, "-", color="0.2", lw=6, alpha=0.3, label="GENO, Rao's method (this problem)")
kk = tx >= x0 - 1e-9
A.plot(tx[kk], ty[kk], "o", mfc="none", mec="k", ms=6, label="Humphreys 1971, Table 3 (Rao's contour, printed)")
A.text(0.02, 0.04, "the part the optimiser designs: from x_s (first lip wave) to the end D", transform=A.transAxes,
       fontsize=8, color="0.3")
A.set_ylabel("y / R_E")
A.set_title("Humphreys et al. 1971: their Rao plug (148 lbm/s, 500 psia, 14.7 psia, 11.52 in)")
A.legend(loc="upper right")
xk = np.r_[g.x_s, rp.xk]


def dense(W):
    yk = np.r_[g.y_s, np.asarray(W), g.D[1]]
    Mc = spline_coeffs(jnp.asarray(xk), jnp.asarray(yk), rp.slope_s)
    return np.asarray(jax.vmap(lambda xx: spline_eval(xx, jnp.asarray(xk), jnp.asarray(yk), Mc)[0])(jnp.asarray(xd)))


W_ = {}
for st, lab, col in (("bump", "SQP result from Rao's contour deformed (up to 1 %)", "C0"),
                     ("half", "SQP result from the average of Rao's contour and a straight line", "C1")):
    d = json.load(open(os.path.join(rv.OUT, "t10_walk_hth71_rao_mi17_%s_qntr.json" % st)))
    W_[st] = d
    y0, y1 = dense(d["start_r"]["W"]), dense(d["landing"]["W"])
    A.plot(xd, y0, ":", color=col, lw=1.3, label=lab.replace("SQP result from", "start:"))
    A.plot(xd, y1, "-", color=col, lw=1.3, label=lab)
    B.plot(xd, 1e3 * (y1 - yg), "-", color=col, lw=1.8)
B.plot(xd, 1e3 * (dense(rp.fit_geno()) - yg), "--", color="k", lw=1.0, label="closest curve to Rao (same number of points)")
B.legend(loc="lower left", fontsize=8)
A.legend(loc="upper right", fontsize=8)
k = (tx >= x0) & (tx <= g.D[0] + 1e-3)
B.plot(tx[k], 1e3 * (ty[k] - rp.wall_of(tx[k])[0]), "o-", color="k", ms=5)
B.axhline(0, color="0.5", lw=0.8)
B.set_ylim(-1, 1)
B.set_ylabel("(y - y_GENO) x 1000")
B.set_xlabel("x / R_E (from the lip)")
rv.savefig(fig, "17_hth.png")
# provisional numbers (optimiser's grid only; t18 hth replaces them after the three-grid reading)
b, hlf = W_["bump"], W_["half"]
gb, gh = b["landing"]["gap"], hlf["landing"]["gap"]
fit = b["fit"]["gap"]
rb, rh = b.get("qntr") or {}, hlf.get("qntr") or {}
DOC = os.path.join(rv.RV, "doc")
open(os.path.join(DOC, "num_hth.tex"), "w").write(
    "%% provisional (optimiser's grid; finer-grid check running): written by tests/t20_hth_context.py\n"
    "\\newcommand{\\HthLbf}{%s\\,lbf (%+.2f / %+.2f\\,lbf vs Rao, optimiser's grid)}\n"
    "\\newcommand{\\HthProv}{two starts land %+.2f and %+.2f\\ppm\\ from Rao's contour on the optimiser's grid "
    "(%.3f\\ppm\\ apart; the closest curve to Rao with the same number of points is %+.2f\\ppm), in %s and %s steps; walls "
    "%.2f\\,mm per m from Rao's}\n" % (
        "{:,.0f}".format(34375.0 * (1 + gb)).replace(",", "\\,"), 34375.0 * gb, 34375.0 * gh, 1e6 * gb, 1e6 * gh,
        1e6 * abs(gb - gh), 1e6 * fit, rb.get("segments", "?"), rh.get("segments", "?"),
        1e3 * max(b["landing"]["dy_max"], hlf["landing"]["dy_max"])))
open(os.path.join(DOC, "num_hth_table.tex"), "w").write(
    "%% provisional: written by tests/t20_hth_context.py\n\\begin{tabular}{@{}lrrr@{}}\\toprule\n"
    "SQP start & vs Rao, optimiser's grid & steps & time\\\\\\midrule\n"
    "Rao's contour deformed (up to 1\\,\\%%) & %+.2f\\ppm & %s & %.0f\\,min\\\\\n"
    "average of Rao's contour and a straight line & %+.2f\\ppm & %s & %.0f\\,min\\\\\n"
    "\\midrule closest curve to Rao & %+.2f\\ppm & & \\\\\n\\bottomrule\n\\end{tabular}\n" % (
        1e6 * gb, rb.get("segments", "?"), rb.get("seconds", 0) / 60, 1e6 * gh, rh.get("segments", "?"),
        rh.get("seconds", 0) / 60, 1e6 * fit))
print("provisional numbers written")
