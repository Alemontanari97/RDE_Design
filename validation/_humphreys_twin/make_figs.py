"""Figures of the Humphreys 1971 twin (S32, 2026-09-22): the objective
and where our walks arrive, and what a FOLDED cell is. Presentation
only -- every number drawn here is re-read from the carriers' own
marches (a1_humphreys_twin._pose, a1_plug_margin's census), none is
computed for the first time in this file."""
import os
import sys
import json
import glob

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                         # noqa: E402
from matplotlib.collections import PolyCollection       # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.dirname(HERE)
sys.path.insert(0, VAL)
os.environ.setdefault("HMPH_CASE", "opt")
import jax.numpy as jnp                                 # noqa: E402
import a1_humphreys_twin as H                           # noqa: E402

C_OURS, C_THEIRS, C_DATA, C_4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, MUTED, SURF = "#0b0b0b", "#52514e", "#898781", "#fcfcfb"
BAD = "#c2332e"
plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK2, "xtick.color": INK2,
    "ytick.color": INK2, "axes.grid": True, "grid.color": "#e6e5e1",
    "grid.linewidth": 0.6, "font.size": 9, "axes.titlesize": 10,
    "legend.frameon": False, "axes.spines.top": False,
    "axes.spines.right": False})


def save(fig, name):
    out = os.path.join(HERE, "figs", name)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print("wrote", out)


st = H._pose("figs", "the figures of the twin")
P, w, c, ta = st["P"], st["w"], st["c"], st["ta"]
S, IN, LBF, F_ref = st["S"], H.IN, H.LBF, st["F_ref"]
import a1_plug_margin as PMG                            # noqa: E402  (after _pose)

TAB2 = np.array(H.TABLES["table2_optimum_lip7.55_inj-34"])


def theirs_curve(xq):
    """THEIR contour: the cubic Hermite through their (x, y) with their
    OWN printed wall angle as the slope. The table is sparse downstream
    (gaps to 2.66 in) and convex, so straight chords ride ABOVE it --
    this is the objective as the paper drew it, not as we read it."""
    return H.read_table(xq, TAB2)
GRID = H.TABLES["_grid_class_lbf"]
ELL2 = PMG.station_spacing(P.K_ST) ** 2
MG = PMG.margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=1.0,
                     f_edge=0.0, ell2=ELL2)


def design(name, W):
    W = np.asarray(W, float)
    out, sch = P.march_record(W, w, c, margin=MG)
    J = float(P.J_replay(jnp.asarray(W), w, c, sch, ta)) / S / S / LBF
    sx, sy, _ = P.wall_stations(W, c)
    return dict(name=name, W=W, out=out, sch=sch, J=J,
                x=np.asarray(sx) / S / IN, y=np.asarray(sy) / S / IN,
                cert=float(out["cert_worst"]))


def cells(d):
    """The net's true cells as polygons, with the census's margin and
    its resolved flag -- np_margin's own quadrilateral and indexing."""
    out, sch = d["out"], d["sch"]
    keys, pts = out["mesh_keys"], np.asarray(out["mesh_pts"])
    idx = {k: n for n, k in enumerate(keys)}
    ms, _, _, fl = PMG.np_margin(out, sch, P.N_ROW, 1.0, 0.0, ELL2,
                                 with_depth=True, with_floor=True)
    orient = float(np.sign(np.median(ms)))
    polys, marg, res = [], [], []
    M, n = P.N_ROW, 0
    for kst, (b, jf) in enumerate(sch.d["wfoot"]):
        i = 2 + kst
        jsrc0 = (jf + 1) if b == 1 else 2
        top = M - jsrc0 + 2
        for jnew in range(PMG.JMIN, top + 1):
            jprev = jnew + jsrc0 - 2
            q4 = [(jprev - 1, i - 1), (jprev, i - 1), (jnew, i),
                  (jnew - 1, i)]
            if not all(k in idx for k in q4):
                continue
            if not (top - jnew > 0.0):        # np_margin's f_edge = 0
                continue
            polys.append(np.array([pts[idx[k], :2] for k in q4])
                         / S / IN)
            marg.append(orient * ms[n])
            res.append(not bool(fl[n]))
            n += 1
        M = max(j for (j, ii) in keys if ii == i)
    return polys, np.array(marg), np.array(res, bool)


pool = [("the fan's streamline (start)", np.asarray(c["W0"], float),
         C_DATA, "--")]
for nm, pat, col, ls in (
        ("walk from the fan", "opt_opt_fan_veen.json", C_4, "-"),
        ("walk from their Table 2", "opt_opt_table_veen.json", C_OURS, "-"),
        ("walk from Table 2 + 0.30 in",
         "opt_opt_table_veen_perturb*.json", "#7a4fd6", "-")):
    g = sorted(glob.glob(os.path.join(HERE, pat)))
    if g:
        pool.append((nm, np.array(json.load(open(g[0]))["W_in"]) * IN * S,
                     col, ls))
pool.append(("their Table 2 (the objective)", np.asarray(st["W_ref"], float),
             "#8b2f6b", "-"))

D = [dict(design(nm, W), color=col, ls=ls) for nm, W, col, ls in pool]

# ======================================================================
# FIGURE 1 -- the objective and where we arrive
# ======================================================================
os.environ["HMPH_TABLE"] = "hermite"
xs = np.linspace(TAB2[0, 0], TAB2[-1, 0], 500)
ys = theirs_curve(xs)
os.environ["HMPH_TABLE"] = "chord"

fig = plt.figure(figsize=(9.2, 8.8))
gs = fig.add_gridspec(3, 2, height_ratios=[2.0, 1.25, 1.0], hspace=0.42,
                      wspace=0.22)
ax = fig.add_subplot(gs[0, :])
zx = fig.add_subplot(gs[1, 0])
zy = fig.add_subplot(gs[1, 1])
bx = fig.add_subplot(gs[2, :])

for a in (ax, zx):
    a.plot(xs, ys, "-", lw=2.4, color=C_THEIRS, alpha=0.85, zorder=4,
           label="THEIR contour (Table 2: their x, y and printed wall "
                 "angle) -- 32,881 lbf")
    a.plot(TAB2[:, 0], TAB2[:, 1], "o", ms=4.2, color=C_THEIRS,
           mec="white", mew=0.6, zorder=6,
           label="the 20 points they print")
for d in D:
    lab = ("their knots, OUR wall (start radius set by the mass)"
           if d["name"].startswith("their") else d["name"])
    for a in (ax, zx):
        a.plot(d["x"], d["y"], d["ls"], lw=1.7, color=d["color"],
               zorder=3, label="%s -- %.0f lbf, y_D %.2f in"
               % (lab, d["J"], d["y"][-1]))
th = [d for d in D if d["name"].startswith("their")][0]
ax.plot(np.asarray(c["xk"]) / S / IN, np.asarray(st["W_ref"]) / S / IN,
        "s", ms=5, mfc="none", mec=C_OURS, mew=1.3, zorder=7,
        label="our 6 knots (read off their table)")
yw0, x0 = float(c["yw0"]) / S / IN, float(P.X0) / S / IN
for a in (ax, zx):
    a.plot([x0], [yw0], "D", ms=6, color=INK, zorder=8)
ax.set_xlabel("x from the cowl lip [in]")
ax.set_ylabel("plug radius y [in]")
ax.set_title("Humphreys 1971, fixed-inlet optimum (lip 7.55 in, injection"
             " -34 deg):\nthe objective, and where our walks arrive")
ax.legend(loc="upper right", fontsize=7.6)
ax.set_xlim(-1.0, 12.0)

# --- the zoom: the first three inches, where the posing is frozen
zx.set_xlim(-0.75, 3.1)
zx.set_ylim(3.7, 7.0)
zx.annotate("their foot\n6.72 in @ x -0.56", xy=(TAB2[0, 0], TAB2[0, 1]),
            xytext=(-0.68, 4.9), fontsize=7.4, color=C_THEIRS,
            arrowprops=dict(arrowstyle="->", color=C_THEIRS, lw=0.8))
zx.annotate("OUR cut: %.2f in @ x %.2f\n(mass-set, frozen)"
            " -- %+.2f in ABOVE their wall"
            % (yw0, x0, yw0 - float(theirs_curve(np.array([x0]))[0])),
            xy=(x0, yw0), xytext=(0.30, 4.15), fontsize=7.4, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
zx.axvline(1.88, color=BAD, lw=1.1, ls="--")
zx.text(1.93, 6.72, "first folded\ncolumn, x 1.88 in", color=BAD,
        fontsize=7.4, va="top")
zx.set_title("the first three inches: no knot before x 2.22 in",
             fontsize=8.5)
zx.set_xlabel("x [in]")
zx.set_ylabel("y [in]")

# --- the wall angle: theirs is done turning before our cut
angt = TAB2[:, 2]
sxw, _, sslw = P.wall_stations(np.asarray(st["W_ref"], float), c)
angw = np.degrees(np.arctan(np.asarray(sslw)))
zy.plot(TAB2[:, 0], angt, "o-", ms=3.4, lw=1.6, color=C_THEIRS,
        label="their printed wall angle")
zy.plot(np.asarray(sxw) / S / IN, angw, "-", lw=1.6, color=C_OURS,
        label="our wall from their knots")
zy.axvline(x0, color=INK, lw=0.9, ls=":")
zy.text(x0 + 0.1, -52, "our cut", fontsize=7.4, color=INK)
zy.plot([TAB2[int(np.argmin(angt)), 0]], [angt.min()], "v", ms=7,
        color=C_THEIRS)
zy.plot([float(np.asarray(sxw)[int(np.argmin(angw))] / S / IN)],
        [angw.min()], "v", ms=7, color=C_OURS)
zy.axvline(1.88, color=BAD, lw=1.1, ls="--")
zy.set_xlim(-0.75, 6.0)
zy.set_title("THEY are steepest at x -0.035 in (before our cut);\nWE are"
             " steepest at x 1.47 in, inside the field", fontsize=8.5)
zy.set_xlabel("x [in]")
zy.set_ylabel("wall angle [deg]")
zy.legend(loc="lower right", fontsize=7.4)

# --- the thrust ladder, zoomed on the cluster
order = sorted([d for d in D if d["J"] > 32000], key=lambda d: d["J"])
ypos = np.arange(len(order))
bx.axvspan(GRID[0], GRID[1], color=C_THEIRS, alpha=0.14,
           label="their own 20-run grid (Table 1): 178 lbf wide")
bx.axvline(F_ref / LBF, color=C_THEIRS, lw=1.5)
bx.text(F_ref / LBF - 10, -0.5, "their optimum 32,881 lbf",
        color=C_THEIRS, fontsize=8, ha="right")
for k, d in zip(ypos, order):
    bx.errorbar([d["J"]], [k], xerr=[[48.6], [48.6]], fmt="o", ms=7,
                color=d["color"], ecolor=d["color"], elinewidth=1.5,
                capsize=3)
    bx.text(d["J"] + 14, k + 0.22,
            ("their knots, our wall" if d["name"].startswith("their")
             else d["name"]), fontsize=7.6, color=INK2)
fan = [d for d in D if d["J"] <= 32000]
bx.set_yticks(ypos)
bx.set_yticklabels(["%.0f" % d["J"] for d in order], fontsize=8)
bx.set_xlim(32700, 33020)
bx.set_ylim(-0.7, len(order) - 0.15)
if fan:
    bx.annotate("the fan's streamline (the walks' start) is off scale "
                "at %.0f lbf" % fan[0]["J"], xy=(32712, -0.45),
                fontsize=7.6, color=C_DATA)
bx.set_xlabel("thrust J [lbf] -- bars = 48.6 lbf, the band our march "
              "supports ON A MOVE at (161,81)")
bx.grid(axis="y", alpha=0.0)
save(fig, "02_objective_and_arrivals.png")

# ======================================================================
# FIGURE 2 -- what a folded cell is
# ======================================================================
theirs = [d for d in D if d["name"].startswith("their")][0]
inc = [d for d in D if d["name"].startswith("the fan")][0]
fig, axs = plt.subplots(1, 3, figsize=(12.4, 4.3))
for axk, d, ttl in ((axs[0], inc, "the incumbent: the fan's own "
                     "streamline\n0 folded cells of 852 resolved"),
                    (axs[1], theirs, "their Table 2 through OUR cut\n"
                     "677 folded cells of 2352 resolved (28.8 %)")):
    polys, marg, res = cells(d)
    good = [p for p, m, r in zip(polys, marg, res) if not (r and m <= 0)]
    bad = [p for p, m, r in zip(polys, marg, res) if (r and m <= 0)]
    axk.add_collection(PolyCollection(good, facecolors="none",
                                      edgecolors="#c9c8c4", lw=0.25))
    if bad:
        axk.add_collection(PolyCollection(bad, facecolors=BAD, alpha=0.55,
                                          edgecolors=BAD, lw=0.3))
    axk.plot(d["x"], d["y"], "-", lw=1.6, color=d["color"])
    axk.set_title(ttl, fontsize=9)
    axk.set_xlabel("x [in]")
    axk.set_xlim(-0.3, 12.0)
    axk.set_ylim(0.0, 7.2)
axs[0].set_ylabel("y [in]")

# the zoom: one folded neighbourhood, cells drawn as they are
polys, marg, res = cells(theirs)
bad_idx = [n for n, (m, r) in enumerate(zip(marg, res)) if r and m <= 0]
cen = np.mean(np.concatenate([polys[n] for n in bad_idx[:60]]), axis=0)
axs[2].add_collection(PolyCollection(
    [p for p, m, r in zip(polys, marg, res) if not (r and m <= 0)],
    facecolors="none", edgecolors="#b9b8b4", lw=0.5))
axs[2].add_collection(PolyCollection(
    [p for p, m, r in zip(polys, marg, res) if (r and m <= 0)],
    facecolors=BAD, alpha=0.55, edgecolors=BAD, lw=0.5))
axs[2].plot(theirs["x"], theirs["y"], "-", lw=1.8, color=C_THEIRS)
axs[2].set_xlim(cen[0] - 0.75, cen[0] + 0.75)
axs[2].set_ylim(cen[1] - 0.55, cen[1] + 0.55)
axs[2].set_title("zoom: the net crossing itself\n(red = negative signed "
                 "area = characteristics crossed)", fontsize=9)
axs[2].set_xlabel("x [in]")
fig.suptitle("What a FOLDED cell is: the characteristic net of the same "
             "machine on two designs, (81,41)", fontsize=10)
save(fig, "03_folded_cells.png")
