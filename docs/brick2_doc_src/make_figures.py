#!/usr/bin/env python3
"""Generate figures for the A1 Brick 2 document (LaTeX build) from the
actual run data: checkpoints, GENO fields, and numbers of record from
the carrier logs. Style follows docs/theory_doc_src/make_figures.py of
the GENO theory document. Output: docs/brick2_doc_src/figs/*.pdf

    .venv-a1/bin/python docs/brick2_doc_src/make_figures.py
"""
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
ROOT = os.path.dirname(DOCS)
OUT = os.path.join(HERE, "figs")
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.join(ROOT, "validation"))

SCRATCH = ("/tmp/claude-1700/-data10-falco-MOSE/"
           "92be2bd8-b160-4811-adea-5510ee63a15f/scratchpad")
PA = 7.614420e+05                       # ambient of record (steps 3-8)

plt.rcParams.update({
    "font.size": 9, "axes.labelsize": 9, "axes.titlesize": 10,
    "figure.dpi": 150, "savefig.bbox": "tight",
    "legend.frameon": False,
})
GRID = dict(alpha=0.25, lw=0.4)


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p)
    plt.close(fig)
    print("wrote", p)


# ---------------------------------------------------------------- contours
def fig_contours():
    from g0_geno_crosscode import read_grid
    import a1_ideal_march_jax as A1
    import jax.numpy as jnp
    ck = os.path.join(OUT, "_ideal_wall.npz")
    if os.path.exists(ck):
        d = np.load(ck)
        wx, wy = d["x"], d["y"]
    else:
        tab = A1.prep_tab(A1.build_tab_nasa())
        CASE = A1.CASE
        P0 = jnp.array([CASE["yt"], CASE["rtu"], CASE["rtd"],
                        CASE["eps"]])
        cfg = dict(NI=CASE["NI"], Ne=CASE["Ne"], da_deg=CASE["da_deg"])
        out, _ = A1.run_march(P0, tab, cfg)
        wx, wy = np.array(out["wall_x"]), np.array(out["wall_y"])
        np.savez(ck, x=wx, y=wy)
    g = read_grid(os.path.join(SCRATCH, "toc_eps4_full"))
    ok = g["rho"][0] > 0
    tx, ty = g["x"][0][ok], g["y"][0][ok]

    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.plot(wx, wy, "-", color="tab:blue", lw=1.4,
            label=r"ideal, Brick 1 (type 0): $L/y_t = 7.34$")
    ax.plot(tx, ty, "-", color="tab:green", lw=1.4,
            label=r"Rao TOC, GENO (type 2): $L/y_t = 5.5$")
    ax.axhline(0, color="k", lw=0.6, ls="-.")
    ax.plot([0], [1.0], "ko", ms=3)
    ax.annotate("throat", (0, 1.0), textcoords="offset points",
                xytext=(4, -12), fontsize=8)
    ax.text(0.35, 0.12, r"axis of symmetry", fontsize=8, color="k")
    ax.set_xlabel(r"axial position $x$ [m]")
    ax.set_ylabel(r"radius $y$ [m]")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(**GRID)
    ax.set_ylim(-0.12, 2.3)
    save(fig, "fig_contours.pdf")


# ---------------------------------------------------------------- J(eps)
def fig_jeps():
    ck = json.load(open(os.path.join(ROOT, "validation",
                                     "_driver_eps_ckpt.json")))
    pts = []
    for k, v in ck.items():
        if not k.startswith("c:"):
            continue
        e = float(k.split(":")[1])
        J = v["J0"] - PA * np.pi * v["ylip"] ** 2
        pts.append((e, J))
    pts.sort()
    e, J = np.array(pts).T
    EST, EGS = 5.150634, 5.15512
    Jmax = J.max()

    pe = np.array([v["pe"] for k, v in sorted(
        ((k, v) for k, v in ck.items() if k.startswith("c:")),
        key=lambda kv: float(kv[0].split(":")[1]))])
    fig, (ax, axB) = plt.subplots(1, 2, figsize=(9.4, 3.4))
    ax.plot(e, J / 1e6, "o-", color="tab:blue", ms=4, lw=1,
            label=r"$J(\varepsilon)$: the 13 cached march evaluations")
    ax.axvline(EST, color="tab:red", lw=1.1, ls="--",
               label=r"closed form $\varepsilon^{*}=5.1506$"
                     r" (exit-area lemma)")
    ax.axvline(EGS, color="tab:blue", lw=1.1, ls=":",
               label=r"blind golden search: $\varepsilon = 5.1551$")
    ax.set_xlabel(r"area ratio $\varepsilon = A_e/A_t$ [--]")
    ax.set_ylabel(r"thrust $J$ [MN]")
    ax.set_title("(a) the objective the search climbs", fontsize=9)
    ax.grid(**GRID)
    ax.set_ylim(115.94, 116.62)      # headroom band for the legend
    ax.legend(loc="upper left", fontsize=7.5)
    # inset: relative distance from the optimum, no offset notation
    axI = ax.inset_axes([0.58, 0.13, 0.39, 0.44])
    m = (e > 5.0) & (e < 5.35)
    axI.plot(e[m], (J[m] - Jmax) / 1e3, "o-", color="tab:blue",
             ms=3, lw=0.8)
    axI.axvline(EST, color="tab:red", lw=0.9, ls="--")
    axI.axvline(EGS, color="tab:blue", lw=0.9, ls=":")
    axI.axhline(0, color="k", lw=0.5)
    axI.tick_params(labelsize=6.5)
    axI.set_ylabel(r"$J - J_{\max}$ [kN]", fontsize=6.5)
    axI.set_title("the top of the curve, magnified", fontsize=7)
    axI.grid(**GRID)
    # (b) the physics of the optimum: exit pressure crossing ambient
    axB.plot(e, pe / 1e5, "o-", color="tab:blue", ms=4, lw=1.2,
             label=r"$p_e(\varepsilon)$, marched")
    axB.axhline(PA / 1e5, color="tab:red", lw=1.2, ls="--",
                label=r"ambient $p_a$")
    axB.axvline(EST, color="0.35", lw=1.0, ls=":")
    axB.plot([EST], [PA / 1e5], "*", color="k", ms=13, zorder=5)
    axB.annotate("the crossing lands on the peak of (a):\n"
                 r"$p_e = p_a$ is the optimum",
                 xy=(EST, PA / 1e5), xytext=(4.25, 9.4),
                 fontsize=7.5,
                 arrowprops=dict(arrowstyle="->", lw=0.8))
    axB.set_xlabel(r"area ratio $\varepsilon = A_e/A_t$ [--]")
    axB.set_ylabel(r"exit pressure $p_e$ [bar]")
    axB.set_title("(b) why that is the optimum", fontsize=9)
    axB.legend(fontsize=7.5, loc="upper right")
    axB.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_jeps.pdf")


# ---------------------------------------------------------------- ripple
def fig_ripple():
    amps = np.array([-2e-4, -1e-4, 0.0, 1e-4, 2e-4])
    gs = np.array([472516.2, 465233.8, 457993.6, 450790.2, 443386.1])
    A = np.polyfit(amps, gs, 1)
    fig, ax = plt.subplots(figsize=(5.6, 2.9))
    xx = np.linspace(amps[0], amps[-1], 100)
    ax.plot(xx * 1e4, np.polyval(A, xx) / 1e5, "-", color="0.35", lw=1,
            label=r"linear fit: smooth curvature"
                  r" $J'' = -7.3\times10^{7}$ (physical)")
    ax.plot(amps * 1e4, gs / 1e5, "o", color="tab:blue", ms=5,
            label=r"AD samples of $\mathrm{d}J/\mathrm{d}a$"
                  r" (exact derivative of the code)")
    ax.errorbar(amps * 1e4, np.polyval(A, amps) / 1e5,
                yerr=44.1 / 1e5 * 4, fmt="none", ecolor="tab:red",
                capsize=3, lw=1.2,
                label=r"table-kink ripple ($4\sigma$ bars):"
                      r" $\sigma = 44$, 0.010% of the gradient")
    ax.set_xlabel(r"wall bump amplitude $a$ [$10^{-4}$ m]")
    ax.set_ylabel(r"thrust gradient $\mathrm{d}J/\mathrm{d}a$"
                  r" [$10^{5}$ N/m]")
    ax.grid(**GRID)
    ax.legend(fontsize=7.5)
    save(fig, "fig_grad_ripple.pdf")


# ---------------------------------------------------------------- f2
def fig_f2():
    from g0_geno_crosscode import read_grid
    import a1_ideal_march_jax as A1
    from a1_o33_toc import geno_terminal, toc_wall, f2_lam3
    from scipy.interpolate import griddata
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    g = read_grid(os.path.join(SCRATCH, "toc_eps4_full"))
    xs, ys, ug, vg, pg, rg, gg, sp, icol = geno_terminal(g)
    Vg = np.sqrt(ug ** 2 + vg ** 2)
    ag = np.sqrt(gg * pg / rg)
    thg = np.arctan2(vg, ug)
    alg = np.arcsin(np.clip(ag / Vg, 0, 1))
    f2g = Vg * np.cos(thg - alg) / np.cos(alg)
    d = np.load(os.path.join(SCRATCH, "o33_march_41.npz"))
    mp = d["mesh"]
    ui = griddata(mp[:, :2], mp[:, 2], (xs, ys), method="linear")
    vi = griddata(mp[:, :2], mp[:, 3], (xs, ys), method="linear")
    ok = np.isfinite(ui) & np.isfinite(vi)
    f2o, _, _ = f2_lam3(xs[ok], ys[ok], ui[ok], vi[ok], ta)
    xw, yw, _ = toc_wall(g)
    f2w_pts = []
    for k in range(0, xw.size, 3):
        d2 = (mp[:, 0] - xw[k]) ** 2 + (mp[:, 1] - yw[k]) ** 2
        i = int(np.argmin(d2))
        if d2[i] < 1e-16:
            f2w_pts.append((yw[k], mp[i, 2], mp[i, 3], xw[k]))
    a = np.array(f2w_pts)
    f2w, _, _ = f2_lam3(a[:, 3], a[:, 0], a[:, 1], a[:, 2], ta)

    def arclen(x, y):
        ds = np.hypot(np.diff(x), np.diff(y))
        return np.concatenate([[0], np.cumsum(ds)])
    o = np.argsort(ys[ok])
    yt_, xt_ = ys[ok][o], xs[ok][o]
    f2o_s, f2g_s = f2o[o], f2g[ok][o]
    s_term = arclen(xt_, yt_)
    s_wall = arclen(a[:, 3], a[:, 0])

    fig, (axL, axM, axR) = plt.subplots(
        1, 3, figsize=(9.6, 3.0),
        gridspec_kw={"width_ratios": [1.15, 1.0, 1.0]})
    # (a) where the two curves live
    axL.plot(xw, yw, color="0.4", lw=1.6)
    axL.plot(xt_, yt_, "o-", color="tab:blue", ms=2.5, lw=1.6)
    axL.annotate("sampled segment of the\nterminal characteristic\n"
                 "(GENO col. 192, at the lip)",
                 (xt_[len(xt_) // 2], yt_[len(yt_) // 2]),
                 textcoords="offset points", xytext=(-118, -48),
                 fontsize=7.5, color="tab:blue",
                 arrowprops=dict(arrowstyle="->", color="tab:blue",
                                 lw=0.8))
    axL.annotate("wall (a streamline)",
                 (xw[len(xw) // 3], yw[len(xw) // 3]),
                 textcoords="offset points", xytext=(2, 12),
                 fontsize=7.5, color="0.3")
    axL.plot([0], [1.0], "ko", ms=3)
    axL.annotate("throat", (0, 1.0), textcoords="offset points",
                 xytext=(4, -10), fontsize=7)
    axL.set_ylim(0.85, 2.15)
    axL.set_xlabel(r"axial position $x$ [m]")
    axL.set_ylabel(r"radius $y$ [m]")
    axL.set_title("(a) where the two curves are", fontsize=9)
    axL.grid(**GRID)
    # (b) f2 along each curve, full range
    axM.plot(s_wall, f2w, "s-", color="0.4", ms=2.5, lw=1,
             label=r"along the wall: $+64\%$ (not invariant)")
    axM.plot(s_term, f2o_s, "-", color="tab:blue", lw=1.4,
             label="along the terminal characteristic: flat")
    axM.set_xlabel("distance along the curve [m]")
    axM.set_ylabel(r"first integral $f_2$ [m/s]")
    axM.set_title(r"(b) $f_2$ is invariant ONLY on the"
                  " characteristic", fontsize=9)
    axM.legend(fontsize=7, loc="lower right")
    axM.grid(**GRID)
    # (c) zoom on the characteristic: the two codes on the same nodes
    axR.plot(s_term, f2o_s, "o-", color="tab:blue", ms=3.5, lw=0.9,
             label="our field (JAX march)")
    axR.plot(s_term, f2g_s, "x", color="tab:red", ms=6, mew=1.4,
             label="GENO, same nodes")
    axR.set_ylim(2626, 2643)
    axR.set_xlabel("distance along the curve [m]")
    axR.set_ylabel(r"first integral $f_2$ [m/s]")
    axR.set_title(r"(c) zoom: flat to $4\times10^{-3}$,"
                  r" codes agree to $9\times10^{-5}$", fontsize=9)
    axR.legend(fontsize=7, loc="upper right")
    axR.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_f2.pdf")


# ---------------------------------------------------------------- stationarity
def fig_stationarity():
    toc = [1.166e4, 3.028e4, 3.573e4, 1.755e4, 1.882e3, 9.705e4]
    pert = [1.4e6, 6.2e5, 3.9e6, 7.0e5, 1.3e6, 2.1e5]
    lip = 1.3103e7
    fig, ax = plt.subplots(figsize=(6.0, 3.0))
    ix = np.arange(6)
    ax.bar(ix - 0.18, np.abs(toc), 0.36, color="tab:blue",
           label=r"$|\mathrm{d}J/\mathrm{d}a|$ at the TOC"
                 " (stationary, as Rao requires)")
    ax.bar(ix + 0.18, np.abs(pert), 0.36, color="0.55",
           label=r"same bumps on a perturbed wall ($40\times$ larger)")
    ax.bar([6.2], [lip], 0.5, color="tab:red",
           label=r"lip-moving direction at the TOC ($1000\times$:"
                 " the vacuum theorem)")
    ax.set_yscale("log")
    ax.set_xticks(list(ix) + [6.2])
    ax.set_xticklabels([r"$0.20L$", r"$0.32L$", r"$0.45L$",
                        r"$0.58L$", r"$0.71L$", r"$0.85L$", "lip"])
    ax.set_xlabel("bump center along the wall (fraction of length"
                  " $L$); last bar = lip variation")
    ax.set_ylabel(r"$|\mathrm{d}J/\mathrm{d}a|$, thrust change per"
                  r" metre of bump [N/m]")
    ax.grid(axis="y", **GRID)
    ax.legend(fontsize=7.5, loc="upper left")
    save(fig, "fig_stationarity.pdf")


# ---------------------------------------------------------------- cycle
def _cycle_phases(tab0, stage):
    """The EXACT phase states of the current cycle construction
    (mirrors a1_cycle_layer.py). Returns (P0s, T0s)."""
    import a1_cycle_layer as CL
    xi = (np.arange(CL.NXI) + 0.5) / CL.NXI
    I1 = (1.0 - 1.0 / CL.PR) / np.log(CL.PR)
    P0s = (tab0["ps"] / I1) * CL.PR ** (-xi)
    if stage == "t3":
        T0s = np.full(CL.NXI, tab0["ts"])
    else:
        gm = tab0["gammamedio"]
        T0s = 3850.0 * (CL.PR ** ((gm - 1.0) / gm)) ** (-xi)
    return P0s, T0s


def fig_cycle():
    import a1_ideal_march_jax as A1
    ck = json.load(open(os.path.join(ROOT, "validation",
                                     "_cycle_ckpt.json")))
    tab0 = A1.prep_tab(A1.build_tab_nasa())

    def curve(stage):
        """J_cycle(eps) ONLY from full, consistent phase sets: for a
        cached eps accept it iff all five keys of the CURRENT phase
        construction are present (stale phase families in the shared
        checkpoint are thereby excluded — they caused the zigzag in an
        earlier version of this figure). A second filter keeps the
        survey family only: the golden-search trajectory was cached at
        a different march resolution and sits on its own parallel
        curve ~1% below — mixing the two families on one curve is
        meaningless (the search's LANDING point enters the figure as a
        vertical line, not as curve points)."""
        P0s, T0s = _cycle_phases(tab0, stage)
        eps_seen = sorted({float(k.split(":")[0]) for k in ck})
        pts = []
        for e in eps_seen:
            ks = ["%.6f:%.6e:%.3f" % (e, P0s[i], T0s[i])
                  for i in range(len(P0s))]
            if all(k in ck for k in ks):
                F = [ck[k]["mdot"] * ck[k]["qe"]
                     + (ck[k]["pe"] - PA) * np.pi * ck[k]["ylip"] ** 2
                     for k in ks]
                pts.append((e, np.mean(F)))
        a = np.array(sorted(pts)).T
        keep = a[1] >= 0.995 * a[1].max()      # survey family only
        return a[0][keep], a[1][keep]

    eT, JT = curve("t3")
    eM, JM = curve("mock")
    mT, mM = eT < 6.0, eM < 6.0

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(8.6, 3.1),
                                   sharey=True)
    # (a) T3 blowdown
    axL.plot(eT[mT], (JT[mT] - JT.max()) / 1e3, "o-",
             color="tab:blue",
             ms=4, lw=1, label=r"$J_{\rm cycle}(\varepsilon)$,"
                               " 5 marches per point")
    axL.axvline(5.150634, color="tab:red", lw=1.1, ls="--",
                label=r"design at $\langle P\rangle$:"
                      r" $\varepsilon = 5.1506$")
    axL.axvline(5.16845, color="tab:blue", lw=1.1, ls=":",
                label=r"blind cycle optimum: $\varepsilon = 5.1685$")
    axL.set_title("(a) pressure-only blowdown: zero gain\n"
                  "over mean-pressure design (collapse)", fontsize=9)
    axL.set_xlabel(r"area ratio $\varepsilon = A_e/A_t$ [--]")
    axL.set_ylabel(r"$J_{\rm cycle}$ below its own maximum [kN]")
    axL.legend(fontsize=7, loc="lower center")
    axL.grid(**GRID)
    # (b) mock RDE
    axR.plot(eM[mM], (JM[mM] - JM.max()) / 1e3, "o-",
             color="tab:green",
             ms=4, lw=1, label=r"$J_{\rm cycle}(\varepsilon)$,"
                               " 5 marches per point")
    axR.axvline(5.177829, color="tab:red", lw=1.1, ls="--",
                label=r"design at $\langle P\rangle,\ \langle PT"
                      r"\rangle/\langle P\rangle$:"
                      r" $\varepsilon = 5.1778$")
    axR.axvline(5.13951, color="tab:green", lw=1.1, ls=":",
                label=r"blind cycle optimum: $\varepsilon = 5.1395$")
    axR.set_title("(b) mock RDE ($P$ and $T$ profiles):\n"
                  "one-number design within $2.5\\times10^{-6}$",
                  fontsize=9)
    axR.set_xlabel(r"area ratio $\varepsilon = A_e/A_t$ [--]")
    axR.legend(fontsize=7, loc="lower center")
    axR.grid(**GRID)
    axR.annotate(r"peak design $\varepsilon = 10.29$:"
                 "\n$-4\\%$ of $J$ (far off scale)",
                 (0.04, 0.90), xycoords="axes fraction", ha="left",
                 va="top", fontsize=7.5, color="0.3")
    axL.set_ylim(-8.5, 2.2)
    fig.tight_layout()
    save(fig, "fig_cycle.pdf")


# ---------------------------------------------------------------- votes
def fig_votes():
    import a1_ideal_march_jax as A1
    import a1_cycle_layer as CL
    ck = json.load(open(CL.CKPT))
    tab0 = A1.prep_tab(A1.build_tab_nasa())
    P0s, T0s = _cycle_phases(tab0, "mock")
    xi = (np.arange(CL.NXI) + 0.5) / CL.NXI

    def votes(eps):
        return np.array([ck["%.6f:%.6e:%.3f" % (eps, P0s[k], T0s[k])
                         ]["pe"] - PA for k in range(CL.NXI)])
    R = votes(5.139510)
    Rb = votes(10.289200)
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    ax.axhspan(-0.48, 0.48, color="tab:blue", alpha=0.10,
               label="balance band (derived): where `zero' lives")
    ax.bar(xi - 0.033, R / 1e5, 0.06, color="tab:blue",
           label=r"votes at the cycle optimum"
                 r" ($\varepsilon = 5.14$): mean $\approx 0$")
    ax.bar(xi + 0.033, Rb / 1e5, 0.06, color="0.55",
           label=r"votes at the peak design ($\varepsilon = 10.29$):"
                 r" mean $= -4.6$")
    ax.axhline(R.mean() / 1e5, color="tab:blue", lw=1.1, ls="--")
    ax.axhline(Rb.mean() / 1e5, color="0.4", lw=1.1, ls="--")
    ax.axhline(0, color="k", lw=0.7)
    ax.set_xticks(xi)
    ax.set_xticklabels(["wave\npassage", "early", "mid", "late",
                        "tail"], fontsize=8)
    ax.set_xlabel(r"cycle phase $\xi$ [--] (0 = wave passage)")
    ax.set_ylabel(r"corner vote $R = p_e - p_a$ [bar]")
    ax.annotate("underexpanded:\n``lengthen me''",
                (xi[0] - 0.033, R[0] / 1e5),
                textcoords="offset points", xytext=(18, -12),
                fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.7))
    ax.annotate("overexpanded:\n``shorten me''",
                (xi[-1] - 0.033, R[-1] / 1e5),
                xytext=(0.46, -8.2), textcoords="data",
                fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.7))
    ax.set_ylim(-9.0, 9.6)
    ax.grid(axis="y", **GRID)
    ax.legend(fontsize=7.3, loc="upper right")
    save(fig, "fig_votes.pdf")


# ---------------------------------------------------------------- plug
def _plug_data(consume=True):
    """Run (or load) the coarse plug-oracle march and return
    everything the figure needs. consume=False reproduces the
    measured ghost-limb regression (diagnostic, for the appendix).
    Cached per variant: rebuilds are free. NOTE the start line runs
    wall -> edge (row 1 = wall), matching the carrier — an earlier
    figure driver fed it inverted, which is why old renders never
    showed the real march."""
    ckf = os.path.join(OUT, "_plug_march.npz" if consume
                       else "_plug_march_noconsume.npz")
    if os.path.exists(ckf):
        d = np.load(ckf)
        return {k: d[k] for k in d.files}
    import a1_ideal_march_jax as A1
    import a1_plug_march as PM
    from a1_freejet_unit import q_at_pa
    import jax.numpy as jnp
    tg = A1.prep_tab(A1.build_tab_gconst())
    ta = A1.tab_arrays(tg)
    gam, Rg, ts = tg["_g"], tg["Rg"], tg["ts"]
    M1, M2 = 1.5, 2.2
    dnu, field, q_of = PM.pm_exact(gam, Rg, ts, M1, M2)
    q2 = q_of(M2)
    pa = float(A1.state_q(jnp.float64(q2), ta)[1])
    qpa = q_at_pa(pa, ta, tg["_as"])
    lip = (0.0, 2.0)
    x0, x_end = 0.5, 3.0
    xs, ys = PM.exact_streamline(field, lip, (0.0, 1.0), x_end)
    y_wall0 = float(np.interp(x0, xs, ys))
    y_edge0 = lip[1] + np.tan(dnu) * x0
    yline = np.linspace(y_wall0, y_edge0, 21)
    us, vs = [], []
    for yy in yline:
        q, th = field(x0, yy, lip)
        us.append(q * np.cos(th))
        vs.append(q * np.sin(th))
    start = (x0, yline, np.array(us), np.array(vs))
    tgrid = np.linspace(0, 1, 41)
    sxa = x0 + tgrid[1:] * (x_end - x0)
    st = (jnp.array(sxa), jnp.array(np.interp(sxa, xs, ys)),
          jnp.array(np.interp(sxa, xs, np.gradient(ys, xs))))
    out, _ = PM.plug_march(st, start, qpa, tg, 0.0,
                           consume=consume)
    w = np.array(out["wall"])
    qw = np.hypot(w[:, 2], w[:, 3])
    pw = np.array(A1.state_q(jnp.array(qw), ta)[1])
    qex = np.array([field(w[k, 0], w[k, 1], lip)[0]
                    for k in range(w.shape[0])])
    pex = np.array(A1.state_q(jnp.array(qex), ta)[1])
    d = dict(mesh=np.array(out["mesh_pts"]),
             edge=np.array(out["edge"]),
             wall_x=w[:, 0], p_march=pw, p_exact=pex,
             q_march=qw, q_exact=qex,
             spike_x=xs, spike_y=ys, dnu=np.float64(dnu),
             pa=np.float64(pa), M1=np.float64(M1), M2=np.float64(M2),
             qs=np.float64(np.sqrt(gam * Rg * ts * 2 / (gam + 1))))
    np.savez(ckf, **d)
    return d


def fig_plug_cycle():
    """The truncated plug under the cycle (step 10): (a) per-phase
    wall pressures with the shared ambient and the nested crossings
    l(xi); (b) the truncation family J_cycle(l) and per-phase F(l)
    with the break; (c) the votes at l* (the mu-averaged corner
    condition). Reads the carrier's phase cache."""
    ck = os.path.join(ROOT, "validation", "_plug_cycle_ckpt")
    kits = []
    for k in range(5):
        f = os.path.join(ck, "mock_p%d_K65.npz" % k)
        if not os.path.exists(f):
            print("plug-cycle cache missing, skipping fig_plug_cycle")
            return
        kits.append(np.load(f))
    meta = json.load(open(os.path.join(ck, "meta.json")))
    pa, lstar = meta["pa"], meta["lstar"]
    lgrid = np.linspace(0.6, 2.98, 400)

    def J_of(d):
        xw, pw, yw, Fin = d["xw"], d["pw"], d["yw"], float(d["Fin"])
        dy = np.diff(yw)
        w = 2*np.pi*0.5*(yw[1:]+yw[:-1])
        pm = 0.5*(pw[1:]+pw[:-1])
        cum = np.concatenate([[0.0], np.cumsum((pm-pa)*w*(-dy))])
        return Fin + np.interp(lgrid, xw, cum)

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.4, 3.2))
    cols = plt.cm.viridis(np.linspace(0.05, 0.85, 5))
    labs = ["wave passage", "early", "mid", "late", "tail"]
    # (a) wall pressures: the adaptation waves
    for k, d in enumerate(kits):
        a1.semilogy(d["xw"], d["pw"] / 1e5, "-", color=cols[k],
                    lw=1.2,
                    label=labs[k] if k in (0, 4) else None)
    a1.axhline(pa / 1e5, color="tab:red", lw=1.2, ls="--")
    a1.text(2.96, pa/1e5*1.08, r"ambient $p_a$", fontsize=7.5,
            color="tab:red", ha="right")
    a1.axvline(lstar, color="k", lw=0.9, ls=":")
    a1.text(lstar-0.09, float(kits[0]["pw"].max())/1e5*0.80,
            r"cycle $l^{*}$", fontsize=7.5, rotation=90)
    a1.set_xlabel(r"axial position $x$ along the spike [m]")
    a1.set_ylabel(r"wall pressure $p_{\rm wall}$ [bar]")
    a1.set_title("(a) per-phase wall pressures: adaptation\nwaves"
                 r" oscillating about $p_a$", fontsize=9)
    a1.legend(fontsize=7, loc="upper right")
    a1.grid(**GRID)
    # (b) truncation families, per-phase normalized: the break
    Js = [J_of(d) for d in kits]
    Jc = np.mean(Js, axis=0)
    for k, J in enumerate(Js):
        a2.plot(lgrid, (J-J.max())/1e3, "-", color=cols[k],
                lw=1.0, alpha=0.9)
        i = int(np.argmax(J))
        a2.plot(lgrid[i], 0.0, "v", color=cols[k], ms=5)
    a2.plot(lgrid, (Jc-Jc.max())/1e3, "k-", lw=2.0,
            label=r"$J_{\rm cycle}(l)$ (cycle mean)")
    a2.axvline(lstar, color="k", lw=0.9, ls=":")
    a2.set_ylim(-330, 30)
    a2.set_xlabel(r"truncation length $l$ [m]")
    a2.set_ylabel(r"thrust below that curve's own maximum [kN]")
    a2.set_title("(b) truncation families: per-phase maxima\n"
                 r"($\nabla$) spread; each falls past its own"
                 r" $l(\xi)$", fontsize=9)
    a2.legend(fontsize=7, loc="lower right")
    a2.grid(**GRID)
    # (c) votes at l*
    votes = np.array([float(np.interp(lstar, d["xw"], d["pw"]))
                      - pa for d in kits])
    xi = (np.arange(5)+0.5)/5
    a3.bar(xi, votes/1e5, 0.12, color=[cols[k] for k in range(5)])
    a3.axhline(0, color="k", lw=0.8)
    a3.axhline(votes.mean()/1e5, color="k", lw=1.0, ls="--")
    a3.text(0.08, votes.mean()/1e5+0.6, r"mean $\approx 0$",
            fontsize=7.5)
    a3.set_xticks(xi)
    a3.set_xticklabels(["wave\npassage", "early", "mid", "late",
                        "tail"], fontsize=7.5)
    a3.set_xlabel(r"cycle phase $\xi$ [--]")
    a3.set_ylabel(r"vote $p_{\rm wall}(l^{*})-p_a$ [bar]")
    a3.set_title("(c) votes at $l^{*}$: oscillation-scrambled,\n"
                 "but the cycle mean balances",
                 fontsize=9)
    a3.grid(axis="y", **GRID)
    fig.tight_layout()
    save(fig, "fig_plug_cycle.pdf")


def fig_moc_primer():
    """How the march computes: (a) characteristics at a point,
    (b) the interior cell, (c) columns, sweep and the wall foot.
    Didactic figure for readers who do not know MoC internals."""
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.0, 3.1))

    # ---- (a) characteristics at a point
    th, al = 0.30, 0.42                  # flow angle, Mach angle
    P = (0.1, 0.15)
    a1.annotate("", xy=(P[0] + 1.15 * np.cos(th),
                        P[1] + 1.15 * np.sin(th)),
                xytext=P, arrowprops=dict(arrowstyle="-|>",
                                          color="k", lw=1.6))
    a1.text(P[0] + 1.22 * np.cos(th), P[1] + 1.22 * np.sin(th),
            "flow direction\n(angle $\\theta$, Mach $M$)",
            fontsize=7.5, ha="left", va="center")
    for s, c in ((+1, "tab:red"), (-1, "tab:blue")):
        a = th + s * al
        a1.plot([P[0], P[0] + 1.25 * np.cos(a)],
                [P[1], P[1] + 1.25 * np.sin(a)],
                "--", color=c, lw=1.3)
    a1.text(P[0] + 1.30 * np.cos(th + al),
            P[1] + 1.30 * np.sin(th + al),
            "$C^{+}$ at $\\theta+\\alpha$", fontsize=8,
            color="tab:red", ha="left", va="bottom")
    a1.text(P[0] + 1.30 * np.cos(th - al),
            P[1] + 1.30 * np.sin(th - al),
            "$C^{-}$ at $\\theta-\\alpha$\n$\\sin\\alpha = 1/M$",
            fontsize=8, color="tab:blue", ha="left", va="top")
    a1.plot([P[0]], [P[1]], "ko", ms=5)
    a1.text(P[0] - 0.05, P[1] - 0.13, "any point of the\nsupersonic"
            " flow", fontsize=7.5, ha="left", va="top")
    a1.set_xlim(-0.1, 2.05)
    a1.set_ylim(-0.55, 1.15)
    a1.set_xticks([]); a1.set_yticks([])
    a1.set_title("(a) two characteristics per point", fontsize=9)

    # ---- (b) the interior cell
    p1 = (0.0, 0.18)                     # known, sends C+
    p2 = (0.10, 0.95)                    # known, sends C-
    p4 = (0.75, 0.60)                    # solved
    a2.plot(*p1, "o", color="k", ms=6)
    a2.plot(*p2, "o", color="k", ms=6)
    a2.plot(*p4, "o", mfc="white", mec="tab:green", ms=8, mew=1.6)
    a2.plot([p1[0], p4[0]], [p1[1], p4[1]], "--", color="tab:red",
            lw=1.3)
    a2.plot([p2[0], p4[0]], [p2[1], p4[1]], "--", color="tab:blue",
            lw=1.3)
    a2.plot([(p1[0]+p4[0])/2], [(p1[1]+p4[1])/2], "D",
            color="tab:red", ms=4)
    a2.plot([(p2[0]+p4[0])/2], [(p2[1]+p4[1])/2], "D",
            color="tab:blue", ms=4)
    a2.text(p1[0] - 0.04, p1[1], "known\npoint 1", fontsize=7.5,
            ha="right", va="center")
    a2.text(p2[0] - 0.02, p2[1] + 0.06, "known point 2",
            fontsize=7.5)
    a2.text(p4[0] + 0.07, p4[1], "new point 4:\n4 unknowns"
            " $(x,y,u,v)$", fontsize=7.5, color="tab:green",
            va="center")
    a2.text(0.40, 0.33, "$C^{+}$ from 1", fontsize=7.5,
            color="tab:red", rotation=24)
    a2.text(0.26, 0.85, "$C^{-}$ from 2", fontsize=7.5,
            color="tab:blue", rotation=-25)
    a2.text(-0.32, -0.10, "2 line equations (where the"
            " characteristics cross)\n+ 2 compatibility relations,"
            " with coefficients at\nthe segment midpoints"
            " ($\\diamond$, 2nd order)\n= 4 equations; solved by"
            " Newton", fontsize=7.5, va="top")
    a2.set_xlim(-0.35, 1.55)
    a2.set_ylim(-0.62, 1.15)
    a2.set_xticks([]); a2.set_yticks([])
    a2.set_title("(b) the interior cell", fontsize=9)

    # ---- (c) columns, sweep, and the wall foot
    wall = lambda x: 0.05 + 0.02 * x
    topb = lambda x: 1.00 + 0.13 * x
    cols = [0.0, 0.45, 0.9, 1.35]
    for xc in cols[:-1]:
        n = 5
        ys_ = wall(xc) + np.arange(n) / (n - 1.0) \
            * (topb(xc) - wall(xc))
        a3.plot([xc] * n, ys_, "o", color="k", ms=3.5)
    xc = cols[-1]
    n = 5
    ys_ = wall(xc) + np.arange(n) / (n - 1.0) * (topb(xc) - wall(xc))
    a3.plot([xc] * n, ys_, "o", mfc="white", mec="tab:green", ms=5,
            mew=1.2)
    a3.text(1.44, 1.22, "column\nbeing solved",
            fontsize=7, color="tab:green", va="top")
    xx = np.linspace(-0.15, 1.7, 20)
    a3.plot(xx, wall(xx), "k-", lw=1.6)
    a3.text(-0.12, wall(-0.12) - 0.06, "prescribed wall",
            fontsize=7.5, ha="left", va="top")
    a3.text(0.0, 1.52, "the march sweeps column by column",
            fontsize=7.5, color="0.35")
    a3.annotate("", xy=(1.45, 1.44), xytext=(0.05, 1.34),
                arrowprops=dict(arrowstyle="->", color="0.4",
                                lw=1.0))
    # the wall cell: position known, foot found on the previous column
    wp = (cols[-1], wall(cols[-1]))
    a3.plot(*wp, "o", color="tab:red", ms=6)
    a3.annotate("wall point:\nposition known", (wp[0], wp[1]),
                xytext=(1.42, 0.50), textcoords="data", va="top",
                fontsize=7, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.6))
    foot = (cols[-2], 0.40)
    a3.plot([wp[0], foot[0]], [wp[1], foot[1]], "--",
            color="tab:blue", lw=1.3)
    a3.plot(*foot, "s", color="tab:orange", ms=6)
    a3.annotate("the FOOT: found by interpolating between\nthe"
                " previous column's stored points",
                foot, xytext=(0.0, 0.26), textcoords="data",
                va="top", fontsize=7, color="tab:orange",
                arrowprops=dict(arrowstyle="->", color="tab:orange",
                                lw=0.7))
    a3.set_xlim(-0.15, 1.75)
    a3.set_ylim(-0.14, 1.62)
    a3.set_xticks([]); a3.set_yticks([])
    a3.set_title("(c) columns, the sweep, and the foot", fontsize=9)
    fig.tight_layout()
    save(fig, "fig_moc_primer.pdf")


def fig_fan_singularity():
    """Why ordinary cells cannot march across the lip fan: the
    singular point, what breaks, and the construct-don't-march cure.
    Drawn in the oracle world."""
    d = _plug_data()
    dnu = float(d["dnu"])
    M1, M2 = float(d["M1"]), float(d["M2"])
    lip = (0.0, 2.0)
    mu1, mu2 = np.arcsin(1 / M1), np.arcsin(1 / M2)
    sx, sy = d["spike_x"], d["spike_y"]

    def world(ax, nray=9, ray_kw=None):
        """Cowl, spike and lip fan; returns the ray angles."""
        ray_kw = ray_kw or dict(color="0.75", lw=0.6)
        ax.plot([-0.85, 0], [2, 2], "k-", lw=2.2)
        m = sx <= 2.7
        ax.plot(np.concatenate([[-0.85], sx[m]]),
                np.concatenate([[1.0], sy[m]]), "k-", lw=1.5)
        phis = np.linspace(-mu1, dnu - mu2, nray)
        for phi in phis:
            ax.plot([lip[0], lip[0] + 3.0 * np.cos(phi)],
                    [lip[1], lip[1] + 3.0 * np.sin(phi)], **ray_kw)
        ax.plot([lip[0]], [lip[1]], "o", color="tab:red", ms=5,
                zorder=5)
        return phis

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.2, 3.4))

    # ---- (a) the singular point
    world(a1)
    xe = np.linspace(0, 1.6, 8)
    a1.plot(xe, lip[1] + np.tan(dnu) * xe, "--", color="tab:blue",
            lw=1.2)
    a1.text(1.02, 2.62, "jet edge", color="tab:blue", fontsize=7.5,
            rotation=22)
    for yy in (1.30, 1.60, 1.90):
        a1.annotate("", xy=(-0.18, yy), xytext=(-0.68, yy),
                    arrowprops=dict(arrowstyle="-|>",
                                    color="tab:blue", lw=1.1))
    a1.text(-0.80, 1.10, "uniform\n$M_1 = 1.5$", fontsize=7.5,
            color="tab:blue")
    for x0_, y0_ in ((0.55, 2.12), (0.95, 2.28)):
        a1.annotate("", xy=(x0_ + 0.42 * np.cos(dnu),
                            y0_ + 0.42 * np.sin(dnu)),
                    xytext=(x0_, y0_),
                    arrowprops=dict(arrowstyle="-|>",
                                    color="tab:blue", lw=1.1))
    a1.text(1.55, 2.30, "uniform\n$M_2 = 2.2$", fontsize=7.5,
            color="tab:blue")
    a1.text(2.42, 1.62, "each ray carries ONE state;\nacross the fan"
            " $M$ runs 1.5$\\to$2.2", fontsize=7.5, color="0.35",
            ha="right")
    a1.annotate("the lip: one geometric point,\nEVERY state"
                " $M_1\\to M_2$ at once\n(multivalued, infinite"
                " gradient)", lip, xytext=(-0.80, 2.72),
                textcoords="data", va="top", fontsize=7.5,
                color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.7))
    a1.set_xlim(-0.85, 2.55)
    a1.set_ylim(0.82, 2.95)
    a1.set_xticks([]); a1.set_yticks([])
    a1.set_title("(a) the lip is a singular point", fontsize=9)

    # ---- (b) what breaks if ordinary cells march across
    world(a2, nray=13)
    pA = (-0.14, 1.80)
    pB = (0.24, 1.44)
    p4 = (0.56, 1.74)
    a2.plot(*pA, "o", color="k", ms=5)
    a2.plot(*pB, "o", color="k", ms=5)
    a2.plot(*p4, "o", mfc="white", mec="tab:red", ms=7, mew=1.5)
    a2.plot([pA[0], p4[0]], [pA[1], p4[1]], "--", color="tab:red",
            lw=1.2)
    a2.plot([pB[0], p4[0]], [pB[1], p4[1]], "--", color="tab:blue",
            lw=1.2)
    a2.plot([(pA[0] + p4[0]) / 2], [(pA[1] + p4[1]) / 2], "D",
            color="tab:red", ms=4)
    a2.text(-0.31, 1.86, "known,\n$M = 1.5$", fontsize=7,
            ha="left")
    a2.text(0.16, 1.36, "known, mid-fan", fontsize=7)
    a2.annotate("the segment spans the fan: the\nmidpoint"
                " ``average'' mixes states\nthat differ by the"
                " whole jump\n-- an order-one closure error",
                ((pA[0] + p4[0]) / 2, (pA[1] + p4[1]) / 2),
                xytext=(-0.32, 2.66), textcoords="data", va="top",
                fontsize=7.5, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.7))
    a2.text(0.78, 2.44, "and near the lip all\n$C^{-}$ meet at one"
            " point:\nthe position crossing\ndegenerates. Measured:"
            "\ncert $8.9\\times10^{9}$ when tried", fontsize=7.5,
            color="tab:red", va="top")
    a2.set_xlim(-0.35, 1.42)
    a2.set_ylim(0.95, 2.70)
    a2.set_xticks([]); a2.set_yticks([])
    a2.set_title("(b) what breaks if you march across", fontsize=9)

    # ---- (c) the cure: construct the fan, march between rays
    phis = world(a3, nray=9,
                 ray_kw=dict(color="0.55", lw=0.8))
    for phi in phis:
        tt = np.array([0.35, 0.62, 0.90])
        a3.plot(lip[0] + tt * 2.2 * np.cos(phi),
                lip[1] + tt * 2.2 * np.sin(phi), "o", color="k",
                ms=2.6)
    # one ordinary cell between adjacent rays
    i = 4
    pa_ = (lip[0] + 0.62 * 2.2 * np.cos(phis[i]),
           lip[1] + 0.62 * 2.2 * np.sin(phis[i]))
    pb_ = (lip[0] + 0.62 * 2.2 * np.cos(phis[i + 1]),
           lip[1] + 0.62 * 2.2 * np.sin(phis[i + 1]))
    pc_ = ((pa_[0] + pb_[0]) / 2 + 0.28, (pa_[1] + pb_[1]) / 2)
    a3.plot([pa_[0], pc_[0]], [pa_[1], pc_[1]], "--",
            color="tab:red", lw=1.0)
    a3.plot([pb_[0], pc_[0]], [pb_[1], pc_[1]], "--",
            color="tab:blue", lw=1.0)
    a3.plot(*pc_, "o", mfc="white", mec="tab:green", ms=6, mew=1.4)
    a3.annotate("between adjacent rays the flow\nis smooth again:"
                " ordinary cells\nresume", pc_,
                xytext=(1.72, 2.12), textcoords="data", va="top",
                fontsize=7.5, color="tab:green",
                arrowprops=dict(arrowstyle="->", color="tab:green",
                                lw=0.7))
    a3.text(-0.80, 2.86, "seed the fan as DATA: each ray's state"
            " is exact\n(Prandtl-Meyer, the fan is self-similar)"
            " -- the corner\nis constructed, never marched",
            fontsize=7.5, va="top")
    x0 = 0.5
    ysl = np.linspace(float(np.interp(x0, sx, sy)),
                      lip[1] + np.tan(dnu) * x0, 8)
    a3.plot([x0] * 8, ysl, "k.", ms=3)
    a3.plot([x0, x0], [ysl[0], ysl[-1]], "k:", lw=0.9)
    a3.annotate("the oracle goes further: the start\nline sits"
                " downstream, carrying the\nexact field -- the"
                " corner lives in\nthe data", (x0, ysl[2]),
                xytext=(-0.80, 1.42), textcoords="data", va="top",
                fontsize=7.5, color="k",
                arrowprops=dict(arrowstyle="->", color="0.3",
                                lw=0.7))
    a3.set_xlim(-0.85, 2.55)
    a3.set_ylim(0.82, 2.95)
    a3.set_xticks([]); a3.set_yticks([])
    a3.set_title("(c) the cure: construct, don't march", fontsize=9)
    fig.tight_layout()
    save(fig, "fig_fan_singularity.pdf")


def fig_freejet():
    """The free-jet cell and the sign trap, redrawn in the document
    style (replaces the old sch_freejet.png)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.1))

    # ---- (a) the cell
    sl = 0.34                            # edge slope
    e_of = lambda x: 0.55 + sl * x
    xe = np.linspace(-0.1, 0.62, 5)
    a1.plot(xe, e_of(xe), "-", color="tab:blue", lw=1.6)
    xe2 = np.linspace(0.62, 1.45, 5)
    a1.plot(xe2, e_of(xe2), ":", color="tab:blue", lw=1.3)
    a1.text(-0.08, 0.66, "jet edge so far\n(a streamline)",
            fontsize=7.5, color="tab:blue")
    p3 = (0.62, e_of(0.62))
    p1 = (0.62, 0.22)
    p4 = (1.18, e_of(1.18))
    a1.plot(*p3, "o", color="tab:blue", ms=6)
    a1.plot(*p1, "s", color="k", ms=6)
    a1.plot(*p4, "o", mfc="white", mec="tab:green", ms=8, mew=1.6)
    a1.plot([p1[0], p4[0]], [p1[1], p4[1]], "--", color="tab:red",
            lw=1.2)
    a1.plot([p3[0], p4[0]], [p3[1], p4[1]], "-", color="tab:blue",
            lw=1.0, alpha=0.5)
    a1.text(p3[0] - 0.03, p3[1] + 0.06, "pt3: previous\nedge point",
            fontsize=7.5, color="tab:blue", ha="right")
    a1.text(p1[0] + 0.04, p1[1] - 0.02, "pt1: interior neighbor\n"
            "(same column, below)", fontsize=7.5, va="top")
    a1.text(0.80, 0.44, "$C^{+}$", fontsize=8, color="tab:red")
    a1.annotate("pt4, solved: position AND turn\nangle free;"
                " pressure fixed,\n$p = p_a$ exactly, so $|q| ="
                " q_{p_a}$;\n$(u,v) = q_{p_a}(\\cos\\theta_4,"
                " \\sin\\theta_4)$", p4,
                xytext=(0.62, 1.42), textcoords="data", va="top",
                fontsize=7.5, color="tab:green",
                arrowprops=dict(arrowstyle="->", color="tab:green",
                                lw=0.7))
    a1.set_xlim(-0.12, 1.5)
    a1.set_ylim(0.0, 1.45)
    a1.set_xticks([]); a1.set_yticks([])
    a1.set_title("(a) the free-jet cell (certified 6/6)", fontsize=9)

    # ---- (b) the sign trap
    P = (0.15, 0.62)
    a2.plot([-0.25, P[0]], [P[1], P[1]], "-", color="0.3", lw=1.6)
    a2.plot(*P, "ko", ms=5)
    for ang, ls, c in ((0.42, ":", "0.5"), (-0.38, "-", "tab:red")):
        a2.annotate("", xy=(P[0] + 0.85 * np.cos(ang),
                            P[1] + 0.85 * np.sin(ang)), xytext=P,
                    arrowprops=dict(arrowstyle="-|>", ls=ls,
                                    color=c, lw=1.4))
    a2.text(P[0] + 0.90 * np.cos(0.42), P[1] + 0.90 * np.sin(0.42),
            "the modulus form $v = +\\sqrt{q_{p_a}^2 - u^2}$\ncan"
            " only turn OUTWARD", fontsize=7.5, color="0.4",
            va="bottom", ha="center")
    a2.text(P[0] + 0.92 * np.cos(-0.38),
            P[1] + 0.92 * np.sin(-0.38) - 0.03,
            "but a COMPRESSING jet must turn\nINWARD -- caught by"
            " rejector U-3", fontsize=7.5, color="tab:red",
            va="top", ha="center")
    a2.text(-0.25, 1.28, "fix: make the ANGLE $\\theta_4$ the"
            " unknown --\nthe sign lives inside it, both turns"
            " reachable", fontsize=7.5, color="tab:green",
            va="top")
    a2.set_xlim(-0.3, 1.6)
    a2.set_ylim(-0.05, 1.35)
    a2.set_xticks([]); a2.set_yticks([])
    a2.set_title("(b) the sign trap it survived", fontsize=9)
    fig.tight_layout()
    save(fig, "fig_freejet.pdf")


def fig_edge_root_geometry():
    """The corrected geometry of lesson 1: (a) a sender on pt3's own
    characteristic can only re-find its recorded exit; (b) the fix --
    a steeper C+ from below catches the SHALLOWER streamline through
    pt3 strictly downstream. th = flow angle, al = Mach angle."""
    th, al = 0.32, 0.45
    se, sc = np.tan(th), np.tan(th + al)     # streamline / C+ slopes
    e_of = lambda x: 0.5 + se * x            # the (straight) edge
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.3))

    # ---- (a) the broken feed
    xe = np.linspace(-0.05, 1.55, 8)
    a1.plot(xe, e_of(xe), "--", color="tab:blue", lw=1.6)
    a1.text(0.02, e_of(0.02) + 0.07, "free jet edge (straight)",
            color="tab:blue", fontsize=7.5, rotation=17)
    p3 = (1.0, e_of(1.0))
    S = (p3[0] - 0.45, p3[1] - 0.45 * sc)
    for dy in (0.0, 0.16, 0.32):             # previous column's data
        a1.plot([S[0]], [S[1] - dy], "o", color="k", ms=4)
    a1.text(S[0] - 0.03, S[1] - 0.45, "previous column's\ntop data",
            fontsize=7.5, ha="center", va="top")
    a1.annotate("", xy=p3, xytext=S,
                arrowprops=dict(arrowstyle="-|>", color="tab:red",
                                lw=1.6))
    a1.text(0.63, 0.50, "the recorded $C^{+}$ segment\nthat BUILT"
            " pt3: its exit through\nthe edge IS pt3", fontsize=7.5,
            color="tab:red")
    xr = np.linspace(p3[0], p3[0] + 0.42, 5)
    a1.plot(xr, p3[1] + sc * (xr - p3[0]), ":", color="tab:red",
            lw=1.2)
    a1.text(1.14, 1.32, "beyond pt3 the same line\nis already OUTSIDE"
            " the jet", fontsize=7, color="tab:red", ha="center")
    a1.plot(*p3, "o", color="tab:blue", ms=6)
    a1.plot(*p3, "o", mfc="none", mec="tab:red", ms=13, mew=1.4)
    a1.annotate("re-drawing the same line can only\nre-find its"
                " recorded exit:\npt4 = pt3, zero step",
                p3, xytext=(0.02, 1.42), textcoords="data", va="top",
                fontsize=7.5, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.7))
    a1.set_xlim(-0.05, 1.55)
    a1.set_ylim(-0.12, 1.5)
    a1.set_xticks([]); a1.set_yticks([])
    a1.set_title("(a) broken feed: a characteristic that has\n"
                 "already exited", fontsize=9)

    # ---- (b) the fix: the next characteristic of the family
    p3 = (0.6, e_of(0.6))
    xe = np.linspace(-0.05, p3[0], 5)
    a2.plot(xe, e_of(xe), "-", color="tab:blue", lw=1.6)
    xs2 = np.linspace(p3[0], 2.0, 6)
    a2.plot(xs2, e_of(xs2), ":", color="tab:blue", lw=1.4)
    a2.plot(*p3, "o", color="tab:blue", ms=6)
    a2.text(p3[0] - 0.04, p3[1] + 0.08, "pt3", color="tab:blue",
            fontsize=8, ha="right")
    a2.text(1.98, e_of(1.98) - 0.46,
            "streamline through pt3:\nslope $\\tan\\theta$"
            " (shallower)", color="tab:blue", fontsize=7.5,
            ha="right")
    p1 = (0.70, 0.40)
    d = (e_of(p1[0]) - p1[1]) / (sc - se)
    p4 = (p1[0] + d, p1[1] + sc * d)
    a2.plot([p1[0]], [p1[1]], "o", color="k", ms=5)
    a2.plot([p1[0]], [p1[1] - 0.18], "o", color="k", ms=3.5)
    a2.text(1.30, 0.32, "pt1: top interior of\nthe CURRENT column --"
            "\non the NEXT\ncharacteristic of the family",
            fontsize=7.5, va="top")
    a2.annotate("", xy=p4, xytext=p1,
                arrowprops=dict(arrowstyle="-|>", color="tab:red",
                                lw=1.4))
    a2.annotate("$C^{+}$: slope $\\tan(\\theta+\\alpha)$ (steeper)",
                (0.96, 0.66), xytext=(0.02, 0.42),
                textcoords="data", fontsize=7.5, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.7))
    a2.plot(*p4, "o", mfc="white", mec="tab:green", ms=8, mew=1.6)
    a2.annotate("pt4: a steeper line launched below\nthe edge"
                " catches the shallower one\nstrictly DOWNSTREAM --"
                " a genuine\nadvanced root",
                p4, xytext=(0.02, 1.55), textcoords="data", va="top",
                fontsize=7.5, color="tab:green",
                arrowprops=dict(arrowstyle="->", color="tab:green",
                                lw=0.7))
    a2.annotate("", xy=(p4[0], 0.08), xytext=(p3[0], 0.08),
                arrowprops=dict(arrowstyle="<->", color="0.35",
                                lw=0.9))
    a2.text(0.5 * (p3[0] + p4[0]), -0.02, "advance", fontsize=7.5,
            color="0.35", ha="center")
    a2.set_xlim(-0.05, 2.0)
    a2.set_ylim(-0.15, 1.65)
    a2.set_xticks([]); a2.set_yticks([])
    a2.set_title("(b) the fix: hand the cell the next\n"
                 "characteristic", fontsize=9)
    fig.tight_layout()
    save(fig, "fig_edge_root_geometry.pdf")


def fig_plug_lessons():
    """The three measured lessons, drawn IN the oracle world (same
    lip/spike/edge/fan geometry as fig_plug) instead of as abstract
    dot sketches."""
    d = _plug_data()
    dnu = float(d["dnu"])
    M1, M2 = float(d["M1"]), float(d["M2"])
    lip = (0.0, 2.0)
    sx, sy = d["spike_x"], d["spike_y"]

    def e_of(x):
        return lip[1] + np.tan(dnu) * np.asarray(x, float)

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.0, 3.4))

    # ---- (1) the degenerate edge root -> sweep bottom-up
    xe = np.linspace(0.55, 2.3, 10)
    a1.plot(xe, e_of(xe), "--", color="tab:blue", lw=1.6)
    a1.text(0.62, e_of(0.62) + 0.06, "free jet edge", color="tab:blue",
            fontsize=7.5, rotation=24)
    for xc, lab in ((1.0, "column $k-1$"), (1.5, "column $k$")):
        a1.plot([xc, xc], [2.08, e_of(xc)], color="0.75", lw=0.9)
        a1.text(xc, 2.02, lab, ha="center", fontsize=7.5, color="0.35")
    a1.plot([1.0], [e_of(1.0)], "o", color="tab:blue", ms=6)
    a1.plot([1.0], [e_of(1.0)], "o", mfc="none", mec="tab:red",
            ms=13, mew=1.4)
    a1.plot([1.5], [e_of(1.5)], "o", mfc="none", mec="tab:blue",
            ms=6, mew=1.2)
    a1.annotate("intended new\nedge point",
                (1.5, e_of(1.5)), textcoords="offset points",
                xytext=(8, -20), fontsize=7.5, color="tab:blue",
                arrowprops=dict(arrowstyle="->", color="tab:blue",
                                lw=0.7))
    for dx in (0.035, 0.07):             # the stagnation pile-up
        a1.plot([1.0 + dx], [e_of(1.0 + dx)], "o", mfc="none",
                mec="tab:red", ms=6, mew=1.0, alpha=0.7)
    a1.annotate("Newton returns pt4 = pt3:\non a straight edge the"
                " old\npoint is itself a root (zero step)\n-- and it"
                " repeats: the edge\npiles up, never advancing",
                (1.0, e_of(1.0)), textcoords="offset points",
                xytext=(-58, 40), fontsize=7.5, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.7))
    a1.annotate("", xy=(1.435, e_of(1.5) - 0.05), xytext=(1.0, 2.32),
                arrowprops=dict(arrowstyle="->", ls="--",
                                color="0.45", lw=0.9))
    a1.text(1.02, 2.24, "$C^{+}$ fed from the\nPREVIOUS column",
            fontsize=7, color="0.35")
    a1.text(0.58, 2.98, "fix: sweep each column bottom-up --\n"
            "the edge cell is fed from its OWN column,\n"
            "whose interior points are already solved",
            fontsize=7.5, color="k")
    a1.set_xlim(0.5, 2.35)
    a1.set_ylim(1.98, 3.15)
    a1.set_xlabel(r"axial position $x$ [m]")
    a1.set_ylabel(r"radius $y$ [m]")
    a1.set_title("(1) the degenerate edge root", fontsize=9)
    a1.grid(**GRID)

    # ---- (2) rows must grow with the widening jet
    m = sx <= 2.75
    a2.plot(sx[m], sy[m], "k-", lw=1.4)
    xe = np.linspace(0, 2.75, 10)
    a2.plot(xe, e_of(xe), "--", color="tab:blue", lw=1.4)
    yw = lambda x: np.interp(x, sx, sy)
    colsL = [0.15, 0.45, 0.75, 1.05]
    top = 1.62                          # mesh top stuck: rows do not grow
    for i in range(4):
        rows = [yw(x) + (i / 3.0) * (top - yw(x)) for x in colsL]
        a2.plot(colsL, rows, "-", color="tab:red", lw=0.8, alpha=0.8)
        a2.plot(colsL, rows, ".", color="tab:red", ms=3)
    # the near-horizontal cross-family dragging down through the rows
    for ya, yb in ((1.66, 1.30), (1.46, 1.12), (1.26, 1.02)):
        a2.plot([0.15, 1.05], [ya, yb], "-", color="tab:red",
                lw=0.7, alpha=0.45)
    a2.plot([0.66], [1.335], "x", color="tab:red", ms=7, mew=1.6)
    a2.annotate("fixed row count: the mesh top\nfalls away from the"
                " widening jet\n(and the cross-family tangles)",
                (0.95, top), xytext=(0.10, 1.78), textcoords="data",
                fontsize=7.5, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.7))
    colsR = [1.55, 1.85, 2.15, 2.45]
    for k, x in enumerate(colsR):
        n = 4 + k                       # one row added per column
        ys_ = yw(x) + np.arange(n) / (n - 1.0) * (e_of(x) - yw(x))
        a2.plot([x] * n, ys_, ".", color="tab:green", ms=3.5)
        a2.plot([x, x], [ys_[0], ys_[-1]], "-", color="tab:green",
                lw=0.7, alpha=0.6)
    a2.annotate("fix: grow one row per column\n(the bell's $j_2$ +="
                " 1): the mesh\nfills the jet",
                (1.62, 2.42), xytext=(0.10, 2.70), textcoords="data",
                fontsize=7.5, color="tab:green",
                arrowprops=dict(arrowstyle="->", color="tab:green",
                                lw=0.7))
    a2.set_xlim(-0.05, 2.75)
    a2.set_ylim(0.85, 3.05)
    a2.set_xlabel(r"axial position $x$ [m]")
    a2.set_title("(2) rows must grow with the jet", fontsize=9)
    a2.grid(**GRID)

    # ---- (3) foot adjacency vs step accuracy (real geometry)
    mu1, mu2 = np.arcsin(1 / M1), np.arcsin(1 / M2)
    for phi in np.linspace(-mu1, dnu - mu2, 9):
        a3.plot([lip[0], lip[0] + 3.2 * np.cos(phi)],
                [lip[1], lip[1] + 3.2 * np.sin(phi)],
                color="0.8", lw=0.5)
    m = sx <= 2.35
    a3.plot(sx[m], sy[m], "k-", lw=1.4)
    for xc in [0.8, 1.1, 1.4, 1.7, 2.0, 2.3]:
        a3.plot([xc, xc], [yw(xc), yw(xc) + 0.55], color="0.6",
                lw=0.8)
    a3.text(2.34, 1.58, "paced march columns ($\\Delta x = 0.3$)",
            rotation=90, fontsize=6.5, color="0.35", va="top")
    # the REAL arriving C-: a straight ray through the lip
    xw_, ywall = 2.0, 1.078
    rx = np.linspace(lip[0], xw_, 40)
    ry = lip[1] + (ywall - lip[1]) / (xw_ - lip[0]) * rx
    ray_y = lambda x: float(np.interp(x, rx, ry))
    mray = rx > 0.33
    a3.plot(rx[mray], ry[mray], "-", color="tab:blue", lw=1.3)
    a3.text(0.33, 2.42, "the arriving $C^{-}$ is a straight ray from"
            " the lip:\nconstant state ALONG it, strong fan gradient"
            "\nACROSS it", fontsize=7.5, color="tab:blue", va="top")
    a3.plot([xw_], [ywall], "o", color="tab:red", ms=6)
    a3.annotate("wall station", (xw_, ywall), xytext=(2.05, 1.30),
                textcoords="data", fontsize=7, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.6))
    foot = (1.7, ray_y(1.7))
    a3.plot([foot[0], xw_], [foot[1], ywall], "-",
            color="tab:orange", lw=5, alpha=0.35,
            solid_capstyle="round")
    a3.plot([foot[0]], [foot[1]], "s", color="tab:orange", ms=6)
    a3.plot([(xw_ + foot[0]) / 2], [(ywall + foot[1]) / 2], "D",
            color="tab:orange", ms=4)
    a3.annotate("current: the foot must sit on the ADJACENT column"
                " --\none midpoint closure over the whole long"
                " chord\n(biased: endpoint states interpolated"
                " across rays)",
                ((xw_ + foot[0]) / 2, (ywall + foot[1]) / 2),
                xytext=(0.55, 0.92), textcoords="data", va="top",
                fontsize=7.5, color="tab:orange",
                arrowprops=dict(arrowstyle="->", color="tab:orange",
                                lw=0.7))
    for xq in (1.8, 1.9):
        a3.plot([xq], [ray_y(xq)], "o", color="tab:green", ms=4)
    a3.annotate("fix: multi-column foot search --\nclose the"
                " compatibility in short\nsub-segments, column by"
                " column",
                (1.8, ray_y(1.8)), xytext=(1.48, 2.10),
                textcoords="data", va="top", fontsize=7.5,
                color="tab:green",
                arrowprops=dict(arrowstyle="->", color="tab:green",
                                lw=0.7))
    a3.set_xlim(0.3, 2.45)
    a3.set_ylim(0.60, 2.45)
    a3.set_xlabel(r"axial position $x$ [m]")
    a3.set_title("(3) foot adjacency vs step accuracy", fontsize=9)
    a3.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_plug_lessons.pdf")


def _plug_panels(d, titleL, titleR):
    """Shared two-panel layout: (a) oracle world + marched edge and
    mesh, (b) wall pressure vs the closed form."""
    dnu = float(d["dnu"])
    M1, M2 = float(d["M1"]), float(d["M2"])
    lip = (0.0, 2.0)
    x0 = 0.5
    fig, (axL, axR) = plt.subplots(
        1, 2, figsize=(9.4, 3.3),
        gridspec_kw={"width_ratios": [1.25, 1.0]})
    mu1, mu2 = np.arcsin(1 / M1), np.arcsin(1 / M2)
    for phi in np.linspace(-mu1, dnu - mu2, 9):
        axL.plot([lip[0], lip[0] + 3.2 * np.cos(phi)],
                 [lip[1], lip[1] + 3.2 * np.sin(phi)],
                 color="0.6", lw=0.4, alpha=0.6)
    mp = d["mesh"]
    m = (mp[:, 0] < 3.3) & (mp[:, 1] < 3.5)
    axL.plot(mp[m, 0], mp[m, 1], ".", ms=1.5, color="tab:blue",
             alpha=0.45)
    axL.plot(d["spike_x"], d["spike_y"], color="tab:red", lw=1.8,
             label="exact spike (prescribed wall)")
    xe = np.linspace(0, 3.0, 10)
    axL.plot(xe, lip[1] + np.tan(dnu) * xe, color="tab:blue",
             lw=1.6, ls="--",
             label=r"exact jet edge (angle $\Delta\nu$)")
    ysl = np.linspace(float(np.interp(x0, d["spike_x"],
                                      d["spike_y"])),
                      lip[1] + np.tan(dnu) * x0, 9)
    axL.plot([x0] * 9, ysl, "k.", ms=3)
    axL.plot([x0, x0], [ysl[0], ysl[-1]], "k:", lw=0.9,
             label="start line (exact field data)")
    e = d["edge"]
    ex = np.concatenate([[x0], e[:, 0]])       # the edge polyline
    ey = np.concatenate([[ysl[-1]], e[:, 1]])  # starts at the start
    axL.plot(ex, ey, "o-", ms=3.0, lw=1.0,     # line's top state
             color="tab:orange",
             label="marched free edge")
    axL.plot([lip[0]], [lip[1]], "k^", ms=6)
    axL.annotate("cowl lip\n(PM fan)", lip,
                 textcoords="offset points", xytext=(-40, 8),
                 fontsize=7.5)
    axL.set_xlabel(r"axial position $x$ [m]")
    axL.set_ylabel(r"radius $y$ [m]")
    axL.set_xlim(-0.45, 3.25)
    axL.set_ylim(0.15, 3.45)
    axL.set_title(titleL, fontsize=9)
    axL.legend(fontsize=7, loc="upper left")
    axL.grid(**GRID)
    pa = float(d["pa"])
    axR.plot(d["wall_x"], d["p_exact"] / 1e5, "-", color="tab:red",
             lw=1.6, label="exact wall pressure (closed form)")
    axR.plot(d["wall_x"], d["p_march"] / 1e5, "o", color="tab:blue",
             ms=4, label="marched wall pressure (coarse run)")
    axR.axhline(1.0, color="k", lw=0.7, ls="--")
    axR.text(0.98, 1.12, r"ambient $p_a$", fontsize=7.5, ha="right",
             transform=axR.get_yaxis_transform())
    axR.set_xlabel(r"axial position $x$ along the spike [m]")
    axR.set_ylabel(r"wall pressure $p_{\rm wall}$ [bar]")
    axR.set_title(titleR, fontsize=9)
    axR.legend(fontsize=7, loc="upper right")
    axR.grid(**GRID)
    return fig, axL, axR


def fig_plug():
    """The CERTIFIED march vs the closed-form oracle (5/5 PASS)."""
    d = _plug_data()
    fig, axL, axR = _plug_panels(
        d, "(a) the certified march in the oracle world",
        "(b) the P-2 meter: wall pressure\non the closed form")
    e = d["edge"]
    axL.annotate("the marched free edge tracks the\nexact jet-edge"
                 " line: tail angle within\n$3\\times10^{-4}$ rad of"
                 " $\\Delta\\nu$ (in band)",
                 (e[2, 0], e[2, 1]), xytext=(1.00, 2.72),
                 textcoords="data", va="top", fontsize=7.5,
                 color="tab:orange",
                 arrowprops=dict(arrowstyle="->", color="tab:orange",
                                 lw=0.7))
    kw = int(0.55 * len(d["wall_x"]))
    pa = float(d["pa"])
    axR.annotate("98% of stations inside the derived\nband; max"
                 " deviation $9.8\\times10^{-3}\\,p_a$",
                 (d["wall_x"][kw], d["p_march"][kw] / 1e5),
                 xytext=(1.35, 1.85), textcoords="data", va="top",
                 ha="center", fontsize=7.5, color="tab:blue",
                 arrowprops=dict(arrowstyle="->", color="tab:blue",
                                 lw=0.7))
    fig.tight_layout()
    save(fig, "fig_plug.pdf")


def fig_plug_before():
    """The ghost-limb regression: the march one fix short of
    certification (row consumption disabled). Reproduced live via
    plug_march(consume=False) — the diagnostic switch kept in the
    carrier for exactly this."""
    d = _plug_data(consume=False)
    fig, axL, axR = _plug_panels(
        d, "(a) one fix short: the ghost mesh limb",
        "(b) the same run on the P-2 meter:\nnothing wrong here")
    mp = d["mesh"]
    ghost = mp[(mp[:, 1] < np.interp(np.clip(mp[:, 0], 0.5, 3.0),
                                     d["spike_x"], d["spike_y"])
                - 1e-3)]
    axL.plot(ghost[:, 0], ghost[:, 1], ".", ms=1.4, color="tab:red",
             alpha=0.7)
    axL.annotate("terminated characteristics prolonged\npast the"
                 " wall: a ghost mesh limb\ngrows BELOW the spike"
                 " (wrong-branch\nNewton roots, all ``certified'')"
                 " --\ncaught by the MASS check: +9%",
                 (float(ghost[:, 0].mean()),
                  float(ghost[:, 1].mean())),
                 xytext=(1.98, 2.96), textcoords="data",
                 ha="left", va="top", fontsize=7.5,
                 color="tab:red",
                 arrowprops=dict(arrowstyle="->", color="tab:red",
                                 lw=0.7))
    axL.set_ylim(-0.2, 3.45)
    kw = int(0.7 * len(d["wall_x"]))
    pa = float(d["pa"])
    axR.annotate("wall pressure already sits on the\nclosed form:"
                 " the defect is INVISIBLE\nto P-2 and P-1 -- only"
                 " the mass\nbalance sees the limb",
                 (d["wall_x"][kw], d["p_march"][kw] / 1e5),
                 xytext=(1.55, 1.80), textcoords="data", va="top",
                 ha="center", fontsize=7.5, color="tab:blue",
                 arrowprops=dict(arrowstyle="->", color="tab:blue",
                                 lw=0.7))
    fig.tight_layout()
    save(fig, "fig_plug_before.pdf")


def fig_plug_posing():
    """The step-10 posing lessons, drawn from the engine's own
    machinery and the numbers of record (Appendix A.7):
    (a) the valley spike — the same lip fan posed at PA_M = 2.35
        (fan turn past axial, the 'spike' climbs above the lip)
        vs the corrected PA_M = 1.95 (descending spike);
    (b) the shock-free cycle bound — the phase pressure ladder at
        the start line vs the shared ambient, PR = 2.5 (all
        underexpanded) vs PR = 10 (low phases far below pa:
        shocked start, outside the isentropic march);
    (c) where the optimum landed — the l number line with the
        transplanted-T3 expectation (mean design), the measured
        cycle optimum, the peak design, and the nested per-phase
        optima (t3 numbers of record)."""
    import a1_ideal_march_jax as A1
    import a1_plug_cycle as PC
    import jax.numpy as jnp
    from scipy.optimize import brentq

    tab0 = A1.prep_tab(A1.build_tab_nasa())
    ta0 = A1.tab_arrays(tab0)
    as0 = tab0["_as"]

    def pa_of_M(Mt):
        q = brentq(lambda qq: float(
            A1.state_q(jnp.float64(qq), ta0)[5]) - Mt,
            1.0001 * as0, 3.4 * as0, xtol=1e-11)
        return float(A1.state_q(jnp.float64(q), ta0)[1])

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.4, 3.3))

    # ---- (a) the valley spike ------------------------------------
    lip = PC.LIP
    for Mamb, col, lab, ls in ((2.35, "tab:red",
                                r"posed at $M_{p_a}=2.35$: valley",
                                "--"),
                               (1.95, "tab:blue",
                                r"posed at $M_{p_a}=1.95$: spike",
                                "-")):
        field, q1, q2, th2 = PC.fan_of(tab0, pa_of_M(Mamb))
        sx, sy = PC.streamline(field, (0.0, PC.Y_SP0), 3.0)
        a1.plot(sx, sy, ls, color=col, lw=1.6, label=lab)
        # free edge from the lip at the exit angle
        xe = np.linspace(0, 3.0, 20)
        a1.plot(xe, lip[1] + np.tan(th2) * xe, ls, color=col,
                lw=0.8, alpha=0.45)
        a1.text(3.02, lip[1] + np.tan(th2) * 3.0,
                r"$\theta_E=%+.0f^\circ$" % np.degrees(th2),
                fontsize=7.5, color=col, va="center")
    a1.plot(*lip, "ko", ms=5)
    a1.text(lip[0] - 0.07, lip[1] + 0.06, "lip", fontsize=8,
            ha="right")
    a1.axhline(lip[1], color="k", lw=0.5, ls=":", alpha=0.5)
    a1.annotate("climbs above\nthe lip", xy=(2.55, 2.32),
                xytext=(1.45, 2.52), fontsize=7.5, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.8))
    a1.set_xlim(-0.3, 3.9)
    a1.set_xlabel(r"$x$")
    a1.set_ylabel(r"radius $y$ [m]")
    a1.set_title("(a) the valley spike: fan turned past axial\n"
                 r"vs the $\theta_E\approx0$ posing", fontsize=9)
    a1.legend(fontsize=7, loc="lower left")
    a1.grid(**GRID)

    # ---- (b) the shock-free cycle bound --------------------------
    ck = os.path.join(ROOT, "validation", "_plug_cycle_ckpt")
    kits = [np.load(os.path.join(ck, "mock_p%d_K65.npz" % k))
            for k in range(5)]
    meta = json.load(open(os.path.join(ck, "meta.json")))
    pa = meta["pa"]
    pw0 = np.array([float(d["pw"][0]) for d in kits])
    xi = (np.arange(5) + 0.5) / 5.0

    def ladder(PR):
        I1 = (1.0 - 1.0 / PR) / np.log(PR)
        return (1.0 / I1) * PR ** (-xi)
    # phase start pressures scale with the phase P0 (Lemma A):
    # rescale the measured PR = 2.5 ladder to the PR = 10 posing
    pw0_10 = pw0 * ladder(10.0) / ladder(2.5)
    xb = np.arange(5)
    a2.bar(xb - 0.19, pw0 / 1e5, 0.34, color="tab:blue", alpha=0.85,
           label=r"$PR=2.5$ (posed)")
    a2.bar(xb + 0.19, pw0_10 / pa, 0.34, color="tab:red",
           alpha=0.75, label=r"$PR=10$ (the certified mock)")
    a2.axhline(1.0, color="k", lw=1.1)
    a2.text(4.45, 1.09, r"$p=p_a$", fontsize=7.5, ha="right")
    a2.set_yscale("log")
    ylo = (pw0_10 / pa).min() * 0.5
    a2.axhspan(ylo, 1.0, color="tab:red", alpha=0.10, hatch="//",
               lw=0)
    a2.text(2.0, ylo * 1.35, "overexpanded at the start line:\n"
            "shocked plug operation, outside\nthe isentropic march",
            fontsize=7, color="tab:red", ha="center", va="bottom",
            bbox=dict(fc="white", alpha=0.85, ec="none", pad=1.5))
    a2.set_ylim(ylo, (pw0 / pa).max() * 2.2)
    a2.set_xticks(xb)
    a2.set_xticklabels(["wave\npassage", "early", "mid", "late",
                        "tail"], fontsize=7.5)
    a2.set_ylabel(r"start-line wall pressure $p_w(x_0;\xi)$ [bar]")
    a2.set_title("(b) the plug feels the ambient:\nthe shock-free"
                 r" bound $PR_{\rm plug}=2.5$", fontsize=9)
    a2.legend(fontsize=7, loc="upper right")
    a2.grid(axis="y", **GRID)

    # ---- (c) where the optimum landed (t3 numbers of record) -----
    l_mean, l_star, l_peak = 1.280, 2.103, 2.336
    l_phase = [2.336, 2.061, 1.125, 1.047, 1.006]
    a3.axhline(0, color="k", lw=1.0)
    a3.plot(l_phase, [0.0] * 5, "v", color="0.55", ms=6,
            label=r"per-phase optima $l(\xi)$ (nested)")
    a3.plot([l_mean], [0.0], "x", color="tab:red", ms=10, mew=2.5)
    a3.plot([l_star], [0.0], "*", color="tab:blue", ms=15)
    a3.plot([l_peak], [0.0], "^", color="0.3", ms=7)
    a3.annotate("transplanted bell collapse:\n\"design at the mean\"\n"
                "--- REFUTED", xy=(l_mean, 0.0),
                xytext=(0.98, 0.55), fontsize=7.5, color="tab:red",
                arrowprops=dict(arrowstyle="->", color="tab:red",
                                lw=0.8))
    a3.annotate("measured cycle optimum\n$l^{*}=2.103$:"
                " anti-collapse,\na strict interior compromise",
                xy=(l_star, 0.0), xytext=(1.28, -0.72),
                fontsize=7.5, color="tab:blue",
                arrowprops=dict(arrowstyle="->", color="tab:blue",
                                lw=0.8))
    a3.annotate("peak design 2.336:\nheld short of it by the\n"
                "real adaptation break", xy=(l_peak, 0.0),
                xytext=(1.95, 0.55), fontsize=7.5, color="0.3",
                arrowprops=dict(arrowstyle="->", color="0.3",
                                lw=0.8))
    a3.set_xlim(0.9, 2.55)
    a3.set_ylim(-1.0, 1.0)
    a3.set_yticks([])
    a3.set_xlabel(r"truncation length $l$ [m]")
    a3.set_title("(c) the theory rejecting the wrong test:\nthe"
                 " optimum landed near the peak, not the mean",
                 fontsize=9)
    a3.legend(fontsize=7, loc="lower right")
    a3.grid(axis="x", **GRID)

    fig.tight_layout()
    save(fig, "fig_plug_posing.pdf")


def fig_geno_twin():
    """The GENO full-field plug twin (step 11): (a) wall pressure on
    GENO's spike, our march vs GENO's own, with the deviation and
    the declared threshold; (b) the settled-field deviation at
    GENO's nodes vs the thresholds; (c) the forensic drift: wall
    velocity deviation vs marched length (x0 sweep, numbers of
    record) against GENO's own step-halving shift."""
    ck = os.path.join(ROOT, "validation", "_geno_twin")
    if not os.path.exists(os.path.join(ck, "ref.npz")):
        print("geno-twin cache missing, skipping fig_geno_twin")
        return
    import a1_ideal_march_jax as A1
    import jax.numpy as jnp
    from scipy.interpolate import griddata
    R = np.load(os.path.join(ck, "ref.npz"))
    wall, ivl, ph1 = R["wall"], R["ivl"], R["ph1"]
    gam, Rg, ts, ps = R["gas"]
    tab = A1.prep_tab(A1.build_tab_gconst(
        g=float(gam), Rg=float(Rg), ts=float(ts), ps=float(ps)))
    ta = A1.tab_arrays(tab)
    zf = np.load(os.path.join(ck, "blend_K161.npz"))
    w = zf["wall"]
    qw = np.hypot(w[:, 2], w[:, 3])
    pw = np.array(A1.state_q(jnp.array(qw), ta)[1])
    pg = np.interp(w[:, 0], wall[:, 0], wall[:, 5])

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.4, 3.3))
    # (a) wall pressure overlay + deviation
    mg = (wall[:, 0] > 0.15) & (wall[:, 0] <= 0.93)
    a1.plot(wall[mg, 0], wall[mg, 5] / 1e5, "-", color="0.55",
            lw=2.2, label="GENO wall $p$")
    a1.plot(w[:, 0], pw / 1e5, "--", color="tab:blue", lw=1.1,
            label="our march on GENO's spike")
    a1.set_xlabel(r"axial position $x$ along the spike [m]")
    a1.set_ylabel(r"wall pressure $p_{\rm wall}$ [bar]")
    a1b = a1.twinx()
    a1b.plot(w[:, 0], np.abs(pw - pg) / pg * 1e3, ":",
             color="tab:red", lw=1.0)
    a1b.axhline(3.0, color="tab:red", lw=0.7, alpha=0.5)
    a1b.text(0.55, 3.08, "declared 3e-3", fontsize=6.5,
             color="tab:red", ha="center")
    a1b.set_ylabel(r"$|\Delta p|/p \times 10^{3}$ (dotted)",
                   fontsize=8, color="tab:red")
    a1b.set_ylim(0, 4.0)
    a1b.tick_params(axis="y", labelcolor="tab:red", labelsize=7)
    a1.set_title("(a) the wall twin: two independent\n"
                 "constructions, one contour", fontsize=9)
    a1.legend(fontsize=7, loc="upper left")
    a1.grid(**GRID)
    # (b) settled-field deviation at GENO nodes
    nx, ny = ph1[:, 2], ph1[:, 3]
    yiv = np.interp(nx, ivl[:, 0], ivl[:, 1])
    ywa = np.interp(nx, wall[:, 0], wall[:, 1])
    gap = yiv - ywa
    m = ((nx > 0.16) & (nx < 0.91) & (ny < yiv - 0.03 * gap)
         & (ny > ywa + 0.03 * gap))
    sel = np.where(m)[0]
    sel = sel[np.linspace(0, len(sel) - 1, 3000).astype(int)]
    pts = ph1[sel][:, 2:4]
    mp = zf["mesh"]
    u = griddata(mp[:, :2], mp[:, 2], pts, method="linear")
    v = griddata(mp[:, :2], mp[:, 3], pts, method="linear")
    ok = ~np.isnan(u)
    dq = np.abs(np.hypot(u, v) - ph1[sel, 5])       # [m/s]
    xb = np.linspace(0.16, 0.91, 16)
    xm = 0.5 * (xb[1:] + xb[:-1])
    med = [np.median(dq[ok & (pts[:, 0] >= a) & (pts[:, 0] < b)])
           for a, b in zip(xb[:-1], xb[1:])]
    p95 = [np.percentile(dq[ok & (pts[:, 0] >= a)
                            & (pts[:, 0] < b)], 95)
           for a, b in zip(xb[:-1], xb[1:])]
    a2.semilogy(xm, med, "o-", color="tab:blue", ms=3, lw=1.0,
                label=r"median $|\Delta q|/q$")
    a2.semilogy(xm, p95, "s--", color="tab:blue", ms=3, lw=0.8,
                alpha=0.6, label="p95")
    q_ref = float(np.median(ph1[sel, 5]))
    a2.axhline(1e-3 * q_ref, color="tab:red", lw=0.8)
    a2.text(0.89, 1.15e-3 * q_ref, "declared threshold"
            r" ($10^{-3}$ of $q$)", fontsize=6.5,
            color="tab:red", ha="right")
    a2.axvspan(0.16, 0.35, color="0.8", alpha=0.35, lw=0)
    a2.text(0.05, 0.06, "start\ntransient\nzone", fontsize=7,
            ha="left", color="0.35", transform=a2.transAxes)
    a2.set_xlabel(r"axial position $x$ [m]")
    a2.set_ylabel(r"speed difference $|\Delta q|$ between the two"
                  r" codes [m/s]")
    a2.set_title("(b) the field twin: transient washes out,\n"
                 "settled gap $\\approx 4\\times10^{-4}$",
                 fontsize=9)
    a2.legend(fontsize=7, loc="upper right")
    a2.grid(**GRID)
    # (c) the forensic drift (numbers of record, session 2026-08-07)
    lens = np.array([0.23, 0.43, 0.63, 0.78])
    Q_WALL = 2.40e3        # wall speed scale [m/s], this case
    drift = np.array([6.58e-5, 1.91e-4, 2.68e-4, 3.05e-4]) * Q_WALL
    a3.plot(lens, drift, "o", color="tab:blue", ms=7,
            label="measured wall-speed difference\n"
                  "(same window, start line moved)")
    cfit = np.polyfit(lens, drift, 1)
    ll = np.linspace(0, 0.85, 10)
    a3.plot(ll, np.polyval(cfit, ll), "-", color="tab:blue",
            lw=0.9, alpha=0.55)
    a3.text(0.24, 0.20, "the difference grows in proportion to how\n"
            "far the march has run: a per-length drift,\nnot a"
            " local error", fontsize=7.5, color="tab:blue")
    a3.axhline(3.5e-6 * Q_WALL, color="0.4", lw=1.2, ls="--")
    a3.text(0.02, 3.5e-6 * Q_WALL + 0.03, "GENO's own step-halving"
            " shift: 0.008 m/s (it is converged)", fontsize=7,
            color="0.35")
    a3.set_xlabel("distance marched from the start line [m]")
    a3.set_ylabel(r"speed drift at the wall, $\Delta q$ [m/s]")
    a3.set_ylim(-0.05, 0.95)
    a3.set_title("(c) the measured gap: linear in length,\n"
                 "0.5\\% of the axisymmetric source effect",
                 fontsize=9)
    a3.legend(fontsize=7, loc="upper left")
    a3.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_geno_twin.pdf")


def fig_swirl():
    """The free-vortex swirl extension (step 12): (a) the exact
    radial-equilibrium duct state carried entirely by the swirl term
    in the energy closure; (b) the expansion world's wall pressure
    with swirl, without swirl, and with the centrifugal source
    deliberately dropped (the two alive controls); (c) what the free
    vortex is: the time-mean azimuthal velocity w = Gamma/y.
    Recomputes three coarse marches (~40 s)."""
    import a1_swirl_march as SW
    import a1_ideal_march_jax as A1
    from a1_plug_march import plug_march
    import jax.numpy as jnp
    from scipy.optimize import brentq
    tb = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tb)
    as_ = tb["_as"]
    Y1, Y2 = 1.0, 1.6
    u0 = brentq(lambda q: float(SW.state_sw(
        jnp.float64(q), jnp.float64(Y2), 0.0, ta)[5]) - 1.7,
        1.05 * as_, 3.2 * as_, xtol=1e-11)
    GAM = 0.35 * u0 * Y1
    G2 = GAM * GAM
    qpa_tot = float(np.sqrt(u0 * u0 + G2 / (Y2 * Y2)))
    pa_eq = float(SW.state_sw(jnp.float64(u0), jnp.float64(Y2), G2,
                              ta)[1])

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.4, 3.3))
    # (a) exact equilibrium profiles
    yy = np.linspace(Y1, Y2, 200)
    st = SW.state_sw(jnp.full(200, u0), jnp.array(yy), G2, ta)
    p_y = np.array(st[1]) / 1e5
    Mm = np.array(st[5])
    a1.plot(p_y, yy, "-", color="tab:blue", lw=1.6,
            label=r"$p(y)$ [$10^5$ Pa]")
    a1.set_xlabel(r"static pressure $p$ [bar]", color="tab:blue")
    a1.tick_params(axis="x", labelcolor="tab:blue")
    a1.set_ylabel(r"radius $y$ [m]")
    a1t = a1.twiny()
    a1t.plot(Mm, yy, "--", color="tab:red", lw=1.4,
             label=r"$M_m(y)$")
    a1t.set_xlabel(r"meridional Mach number $M_m$ [--]",
                   color="tab:red", fontsize=8)
    a1t.set_xticks(np.round(np.linspace(Mm.min(), Mm.max(), 3), 3))
    a1t.tick_params(axis="x", labelcolor="tab:red", labelsize=7)
    a1.axhline(Y1, color="0.3", lw=1.6)
    a1.axhline(Y2, color="0.6", lw=1.0, ls=":")
    a1.text(p_y.min() + 0.02, Y1 + 0.01, "wall", fontsize=7.5)
    a1.text(p_y.min() + 0.02, Y2 - 0.03, "free edge", fontsize=7.5,
            color="0.4")
    a1.set_title("(a) the equilibrium duct: uniform $u$,\nall the"
                 " structure in the swirl energy term", fontsize=9)
    a1.grid(**GRID)
    # (b) the expansion world, three variants
    N, K = 17, 41
    start = (0.0, np.linspace(Y1, Y2, N), np.full(N, u0),
             np.zeros(N))
    sx = np.linspace(0, 1.5, K)[1:]
    t = np.clip((sx - 0.25) / 0.75, 0.0, 1.0)
    s = t * t * (3.0 - 2.0 * t)
    ds = np.where((sx > 0.25) & (sx < 1.0),
                  6.0 * t * (1.0 - t) / 0.75, 0.0)
    AMP = 0.18
    stns = (jnp.array(sx), jnp.array(Y1 - AMP * s),
            jnp.array(-AMP * ds))
    qe = lambda yy_: jnp.sqrt(qpa_tot ** 2 - G2 / (yy_ * yy_))  # noqa: E731
    out_sw, _ = plug_march(stns, start, qpa_tot, tb, 1.0,
                           cells=SW.swirl_cells(1.0, G2, G2),
                           q_edge=qe)
    out_ns, _ = plug_march(stns, start, qpa_tot, tb, 1.0,
                           cells=SW.swirl_cells(1.0, G2, 0.0),
                           q_edge=qe)
    qpa0 = float(A1.state_q(jnp.float64(u0), ta)[1])
    from a1_freejet_unit import q_at_pa
    out_g0, _ = plug_march(stns, start, q_at_pa(qpa0, ta, as_), tb,
                           1.0)
    for out, G2p, lab, stl, col in (
            (out_sw, G2, r"$\Gamma \neq 0$ (full)", "-",
             "tab:blue"),
            (out_ns, G2, r"$\Gamma$ in state, source dropped",
             ":", "tab:red"),
            (out_g0, 0.0, r"$\Gamma = 0$", "--", "0.45")):
        w = np.array(out["wall"])
        q = np.hypot(w[:, 2], w[:, 3])
        p = np.array(SW.state_sw(jnp.array(q), jnp.array(w[:, 1]),
                                 G2p, ta)[1])
        a2.plot(w[:, 0], p / 1e5, stl, color=col, lw=1.4,
                label=lab)
    a2.set_xlabel(r"axial position $x$ [m]")
    a2.set_ylabel(r"wall pressure $p_{\rm wall}$ [bar]")
    a2.set_title("(b) the expansion world: the two alive\ncontrols"
                 " --- swirl and its source both matter",
                 fontsize=9)
    a2.legend(fontsize=7, loc="upper right")
    a2.grid(**GRID)
    # (c) the free vortex, as a profile: w(y) and its energy share
    yy2 = np.linspace(Y1, Y2, 200)
    w_prof = GAM / yy2
    a3.plot(yy2, w_prof, "-", color="tab:blue", lw=2.0,
            label=r"swirl velocity $w = \Gamma/y$")
    a3.axhline(0, color="0.6", lw=0.6)
    a3.set_xlabel(r"radius $y$ [m]")
    a3.set_ylabel(r"azimuthal (swirl) velocity $w$ [m/s]",
                  color="tab:blue")
    a3.tick_params(axis="y", labelcolor="tab:blue")
    a3.plot([Y1, Y2], [GAM / Y1, GAM / Y2], "o", color="tab:blue",
            ms=6)
    a3.annotate(r"inner wall: $w/u = %.2f$" % (GAM / Y1 / u0),
                xy=(Y1, GAM / Y1), xytext=(Y1 + 0.06,
                                           GAM / Y1 * 0.985),
                fontsize=7.5, color="tab:blue")
    a3.annotate(r"outer edge: $w/u = %.2f$" % (GAM / Y2 / u0),
                xy=(Y2, GAM / Y2), xytext=(Y2 - 0.30,
                                           GAM / Y2 * 1.02),
                fontsize=7.5, color="tab:blue")
    a3b = a3.twinx()
    a3b.plot(yy2, 100.0 * (GAM / yy2) ** 2
             / (u0 ** 2 + (GAM / yy2) ** 2), "--", color="tab:red",
             lw=1.5)
    a3b.set_ylabel("share of the kinetic energy carried by the"
                   " spin [\\%]", color="tab:red", fontsize=8)
    a3b.tick_params(axis="y", labelcolor="tab:red")
    a3.set_title("(c) what the free vortex is: swirl falling\n"
                 r"as $1/y$, one constant $\Gamma$ for the flow",
                 fontsize=9)
    a3.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_swirl.pdf")


# ======================================================================
# PRIMER FIGURES (front matter): the physics and the method, from zero.
# Every panel carries dimensional axes; every curve is real run data
# unless the panel is explicitly a labelled schematic.
# ======================================================================
def _ideal_wall_state():
    """The reference nozzle's wall: position and the gas state on it,
    from Brick 1's own march (cached)."""
    import a1_ideal_march_jax as A1
    import jax.numpy as jnp
    ck = os.path.join(OUT, "_ideal_wall_state.npz")
    if os.path.exists(ck):
        d = np.load(ck)
        return {k: d[k] for k in d.files}
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    C = A1.CASE
    P0 = jnp.array([C["yt"], C["rtu"], C["rtd"], C["eps"]])
    out, _ = A1.run_march(P0, tab,
                          dict(NI=C["NI"], Ne=C["Ne"],
                               da_deg=C["da_deg"]))
    wx = np.array(out["wall_x"])
    wy = np.array(out["wall_y"])
    q = np.hypot(np.array(out["wall_u"]), np.array(out["wall_v"]))
    st = A1.state_q(jnp.array(q), ta)
    d = dict(x=wx, y=wy, q=q, p=np.array(st[1]), T=np.array(st[0]),
             M=np.array(st[5]), P0=np.array([tab["ps"]]),
             T0=np.array([tab["ts"]]))
    np.savez(ck, **d)
    return d


def fig_nozzle_primer():
    """What a rocket nozzle is, what it does to the gas, and why an
    optimum exists at all --- for a reader who has never designed
    one. Panels (b) and (c) are measured, not sketched."""
    d = _ideal_wall_state()
    wx, wy, Mw, pw = d["x"], d["y"], d["M"], d["p"]
    P0_bar = float(d["P0"][0]) / 1e5
    T0 = float(d["T0"][0])

    fig = plt.figure(figsize=(10.4, 3.4))
    a1 = fig.add_subplot(1, 3, 1)
    a2 = fig.add_subplot(1, 3, 2)
    a3 = fig.add_subplot(1, 3, 3)

    # (a) the machine
    xc = np.array([-1.3, -0.9, -0.45, 0.0])
    yc = np.array([2.6, 2.3, 1.35, 1.0])
    a1.fill_between(np.concatenate([xc, wx]),
                    np.concatenate([yc, wy]), 0.0,
                    color="tab:blue", alpha=0.13, lw=0)
    a1.plot(np.concatenate([xc, wx]), np.concatenate([yc, wy]),
            "-", color="k", lw=1.8)
    a1.plot(np.concatenate([xc, wx]), -np.concatenate([yc, wy]),
            "-", color="k", lw=1.8)
    a1.axhline(0, color="0.5", lw=0.7, ls="-.")
    a1.plot([0, 0], [-1, 1], color="tab:red", lw=1.2, ls="--")
    a1.plot([wx[-1], wx[-1]], [-wy[-1], wy[-1]], color="tab:green",
            lw=1.2, ls="--")
    a1.annotate("", xy=(-0.6, 0), xytext=(-1.25, 0),
                arrowprops=dict(arrowstyle="-|>", color="tab:blue",
                                lw=2.0))
    a1.text(-1.28, 0.35, "chamber\n$P_0=%.0f$ bar\n$T_0=%.0f$ K"
            % (P0_bar, T0), fontsize=7.5, color="tab:blue")
    a1.text(0.05, -0.55, "throat\n$M=1$, $y_t$", fontsize=7.5,
            color="tab:red")
    a1.text(wx[-1] - 2.4, 1.45, "exit plane\n$M_e=%.2f$,"
            " $p_e$" % Mw[-1], fontsize=7.5, color="tab:green")
    a1.text(4.0, -1.9, "ambient $p_a$", fontsize=7.5, color="0.35")
    a1.text(3.4, 0.25, "supersonic exhaust", fontsize=7.5,
            color="0.25")
    a1.set_xlabel(r"axial position $x$ [m]")
    a1.set_ylabel(r"radius $y$ [m]")
    a1.set_title("(a) the machine: a converging--diverging\nnozzle"
                 " (throat radius $y_t = 1$ m here)", fontsize=9)
    a1.set_xlim(-1.5, 8.2)
    a1.set_ylim(-3.0, 3.0)
    a1.grid(**GRID)

    # (b) what the nozzle does to the gas, measured on its own wall
    a2.plot(wx, Mw, "-", color="tab:blue", lw=1.8)
    a2.set_xlabel(r"axial position $x$ [m]")
    a2.set_ylabel(r"Mach number $M$ [--]", color="tab:blue")
    a2.tick_params(axis="y", labelcolor="tab:blue")
    a2.axhline(1.0, color="tab:red", lw=0.8, ls=":")
    a2.text(0.15, 1.06, "sonic, $M=1$", fontsize=7,
            color="tab:red")
    a2b = a2.twinx()
    a2b.semilogy(wx, pw / 1e5, "--", color="tab:green", lw=1.6)
    a2b.set_ylabel(r"static pressure $p$ [bar]", color="tab:green")
    a2b.tick_params(axis="y", labelcolor="tab:green")
    a2b.axhline(PA / 1e5, color="0.35", lw=0.9, ls="-.")
    a2b.text(4.3, PA / 1e5 * 1.35, r"ambient $p_a = %.1f$ bar"
             % (PA / 1e5), fontsize=7, color="0.35")
    a2.set_title("(b) what it does to the gas, measured along\nthe"
                 " wall: pressure into speed", fontsize=9)
    a2.grid(**GRID)

    # (c) why there is an optimum: exit pressure vs area ratio
    ck = json.load(open(os.path.join(ROOT, "validation",
                                     "_driver_eps_ckpt.json")))
    pts = sorted((float(k.split(":")[1]), v["pe"])
                 for k, v in ck.items() if k.startswith("c:"))
    ee = np.array([p[0] for p in pts])
    pe = np.array([p[1] for p in pts]) / 1e5
    a3.plot(ee, pe, "o-", color="tab:blue", ms=4, lw=1.2,
            label=r"$p_e(\varepsilon)$, marched")
    a3.axhline(PA / 1e5, color="tab:red", lw=1.2, ls="--",
               label=r"ambient $p_a$")
    a3.axvline(5.150634, color="0.35", lw=1.0, ls=":")
    a3.plot([5.150634], [PA / 1e5], "*", color="k", ms=13, zorder=5)
    a3.annotate("the optimum:\n$p_e = p_a$ exactly\n"
                r"($\varepsilon^{*}=5.1506$)",
                xy=(5.150634, PA / 1e5), xytext=(4.35, 9.3),
                fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    a3.text(4.15, 7.0, "under-expanded:\nstill worth lengthening",
            fontsize=7, color="0.3")
    a3.text(5.45, 6.55, "over-expanded:\nevery extra ring\ncosts"
            " thrust", fontsize=7, color="0.3")
    a3.set_xlabel(r"area ratio $\varepsilon = A_e/A_t$ [--]")
    a3.set_ylabel(r"exit pressure $p_e$ [bar]")
    a3.set_title("(c) why an optimum exists at all:\nthe exit"
                 " pressure crosses the ambient", fontsize=9)
    a3.legend(fontsize=7, loc="upper right")
    a3.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_nozzle_primer.pdf")


def fig_bell_vs_plug():
    """The two nozzle families this document builds, and the single
    physical difference between them: the bell encloses its exhaust,
    the plug lets the atmosphere bound it. Panels (b) and (c) are
    computed --- (b) is GENO's designed spike with our own marched
    plume boundary, (c) is the plume angle as a function of ambient
    pressure on that same gas."""
    import a1_ideal_march_jax as A1
    import jax.numpy as jnp
    from scipy.optimize import brentq
    d = _ideal_wall_state()
    wx, wy = d["x"], d["y"]

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.4, 3.4))
    # ---- (a) the bell: the gas is enclosed --------------------------
    a1.fill_between(wx, wy, 0.0, color="tab:blue", alpha=0.13, lw=0)
    a1.plot(wx, wy, "-", color="k", lw=2.2, label="solid wall")
    a1.axhline(0, color="0.5", lw=0.7, ls="-.")
    a1.plot([wx[-1], wx[-1]], [0, wy[-1]], "--", color="tab:green",
            lw=1.4, label="exit plane")
    a1.annotate("", xy=(wx[-1] + 1.5, 1.0), xytext=(wx[-1], 1.0),
                arrowprops=dict(arrowstyle="-|>", color="tab:blue",
                                lw=1.8))
    a1.text(1.0, 0.35, "the gas is fully enclosed:\nthe exit state"
            " is fixed by the\ngeometry, whatever the altitude",
            fontsize=7.5)
    a1.text(0.15, 1.75, "axis of symmetry below", fontsize=7,
            color="0.45")
    a1.set_xlabel(r"axial position $x$ [m]")
    a1.set_ylabel(r"radius $y$ [m]")
    a1.set_title("(a) the bell: one design point,\nbuilt into the"
                 " shape", fontsize=9)
    a1.set_ylim(-0.2, 3.0)
    a1.set_xlim(-0.4, 9.2)
    a1.legend(fontsize=7, loc="upper left")
    a1.grid(**GRID)

    # ---- (b) the plug: GENO's spike, our marched plume boundary -----
    ck = os.path.join(ROOT, "validation", "_geno_twin")
    R = np.load(os.path.join(ck, "ref.npz"))
    gw = R["wall"]
    o = np.argsort(gw[:, 0])
    gx, gy = gw[o, 0], gw[o, 1]
    m = gx >= 0.0
    gx, gy = gx[m], gy[m]
    z = np.load(os.path.join(ck, "blend_K161.npz"))
    ed = z["edge"]
    a2.plot(gx, gy, "-", color="k", lw=2.4,
            label="the spike (solid wall)")
    a2.fill_between(gx, gy, 0.0, color="0.82", lw=0)
    a2.plot([0.0, ed[0, 0]], [1.0, ed[0, 1]], ":", color="0.55",
            lw=1.4, label="lip expansion fan (constructed)")
    a2.plot(ed[:, 0], ed[:, 1], "-", color="tab:blue", lw=2.0,
            label=r"plume boundary, marched ($p = p_a$)")
    a2.plot([0.0], [1.0], "ko", ms=6)
    a2.text(0.02, 1.03, "cowl lip", fontsize=7.5)
    a2.plot([gx[-1], gx[-1]], [0.0, gy[-1]], "-", color="tab:red",
            lw=2.4)
    a2.text(gx[-1] - 0.30, 0.10, "base (cut face)", fontsize=7.5,
            color="tab:red")
    a2.annotate("nothing but atmosphere\nbounds the jet here",
                xy=(1.78, 0.862), xytext=(1.00, 0.47), fontsize=7.5,
                color="tab:blue",
                arrowprops=dict(arrowstyle="->", color="tab:blue",
                                lw=0.9))
    a2.axhline(0, color="0.5", lw=0.7, ls="-.")
    a2.set_xlabel(r"axial position $x$ [m]")
    a2.set_ylabel(r"radius $y$ [m]")
    a2.set_title("(b) the plug: the exhaust's outer edge\nis a free"
                 " boundary, not a wall", fontsize=9)
    a2.set_xlim(-0.1, 2.35)
    a2.set_ylim(0.0, 1.32)
    a2.legend(fontsize=6.6, loc="upper right")
    a2.grid(**GRID)

    # ---- (c) altitude compensation, computed ------------------------
    # On the twin's own gas: expand the lip state down to a range of
    # ambient pressures and read the resulting plume turn angle.
    gam, Rg, ts, ps = R["gas"]
    tab = A1.prep_tab(A1.build_tab_gconst(g=float(gam), Rg=float(Rg),
                                          ts=float(ts),
                                          ps=float(ps)))
    ta = A1.tab_arrays(tab)
    as_ = tab["_as"]
    ivl = R["ivl"]
    q_lip, th_lip = float(ivl[0, 3]), float(ivl[0, 4])
    M_lip = float(A1.state_q(jnp.float64(q_lip), ta)[5])
    qs = np.linspace(1.0005 * as_, 3.6 * as_, 700)
    Ms = np.array([float(A1.state_q(jnp.float64(q), ta)[5])
                   for q in qs])
    pss = np.array([float(A1.state_q(jnp.float64(q), ta)[1])
                    for q in qs])
    dth = np.sqrt(np.maximum(Ms ** 2 - 1.0, 0.0)) / qs
    nu = np.concatenate([[0.0], np.cumsum(
        0.5 * (dth[1:] + dth[:-1]) * np.diff(qs))])
    nu_lip = float(np.interp(q_lip, qs, nu))
    pa_grid = np.linspace(0.35, 4.0, 60) * 1e5
    q_of_pa = np.array([brentq(
        lambda q: float(A1.state_q(jnp.float64(q), ta)[1]) - pa,
        1.0005 * as_, 3.55 * as_, xtol=1e-9) for pa in pa_grid])
    th_E = th_lip + (np.interp(q_of_pa, qs, nu) - nu_lip)
    a3.plot(pa_grid / 1e5, np.degrees(th_E), "-", color="tab:blue",
            lw=2.0)
    p_des = float(A1.state_q(jnp.float64(q_lip), ta)[1]) / 1e5
    a3.plot([p_des], [np.degrees(th_lip)], "ko", ms=7)
    a3.annotate("sea level: little expansion,\nthe plume hugs the"
                " spike", xy=(3.35, np.degrees(
                    np.interp(3.35e5, pa_grid, th_E))),
                xytext=(1.30, -6.0), fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    a3.annotate("altitude: the jet expands\nand the boundary swings"
                " out", xy=(0.55, np.degrees(
                    np.interp(0.55e5, pa_grid, th_E))),
                xytext=(0.95, 20.5), fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    a3.annotate("the design point\n(this spike's own $p_a$)",
                xy=(p_des, np.degrees(th_lip)),
                xytext=(1.95, 8.5), fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    a3.axhline(0, color="0.5", lw=0.7, ls=":")
    a3.set_xlabel(r"ambient pressure $p_a$ [bar]")
    a3.set_ylabel(r"plume boundary angle $\theta_E$ [deg]")
    a3.set_title("(c) altitude compensation, computed:\nthe plume"
                 " re-shapes itself with $p_a$", fontsize=9)
    a3.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_bell_vs_plug.pdf")


def fig_rde_cycle():
    """What a rotating detonation engine hands the nozzle: not one
    operating point but a periodic family of them. Panel (b) is the
    mock cycle actually used by the carriers; panel (c) computes,
    phase by phase, the area ratio that phase would want."""
    import a1_ideal_march_jax as A1
    import a1_cycle_layer as CL
    tab0 = A1.prep_tab(A1.build_tab_nasa())
    ps, gm = tab0["ps"], tab0["gammamedio"]
    xi = (np.arange(CL.NXI) + 0.5) / CL.NXI
    I1 = (1.0 - 1.0 / CL.PR) / np.log(CL.PR)
    P0s = (ps / I1) * CL.PR ** (-xi)
    TR = CL.PR ** ((gm - 1.0) / gm)
    T0s = 3850.0 * TR ** (-xi)

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.4, 3.3))
    # (a) the annular chamber, seen from downstream
    th = np.linspace(0, 2 * np.pi, 400)
    for r in (1.0, 1.35):
        a1.plot(r * np.cos(th), r * np.sin(th), "-", color="k",
                lw=1.5)
    thw = np.linspace(0.10, 0.62, 40)
    a1.fill_between(np.cos(thw), np.sin(thw), 1.35 * np.sin(thw),
                    color="tab:red", alpha=0.0, lw=0)
    for f in np.linspace(1.0, 1.35, 14):
        a1.plot(f * np.cos(thw), f * np.sin(thw), "-",
                color="tab:red", lw=2.0, alpha=0.55)
    a1.annotate("", xy=(1.18 * np.cos(1.15), 1.18 * np.sin(1.15)),
                xytext=(1.18 * np.cos(0.72), 1.18 * np.sin(0.72)),
                arrowprops=dict(arrowstyle="-|>", color="tab:red",
                                lw=1.8,
                                connectionstyle="arc3,rad=0.25"))
    a1.text(-0.02, -1.62, "detonation wave: one lap per cycle,"
            "\na few thousand times a second", fontsize=7.5,
            color="tab:red", ha="center")
    a1.text(0, 0, "annular\nchamber", fontsize=8, ha="center",
            va="center")
    a1.text(-0.02, 1.52, "a fixed nozzle section sees the wave"
            "\nsweep past it once per lap", fontsize=7.5,
            ha="center", color="0.3")
    a1.plot([1.175], [0.0], "ks", ms=6)
    a1.text(1.30, -0.10, "section", fontsize=7.5)
    a1.set_xlabel(r"chamber $x$ [m]")
    a1.set_ylabel(r"chamber $y$ [m]")
    a1.set_aspect("equal")
    a1.set_xlim(-1.7, 1.9)
    a1.set_ylim(-1.75, 1.85)
    a1.set_title("(a) the source of the cycle: a detonation\nwave"
                 " rotating in an annulus", fontsize=9)
    a1.grid(**GRID)
    # (b) what that section sees, phase by phase
    a2.step(np.concatenate([[0], xi, [1]]),
            np.concatenate([[P0s[0]], P0s, [P0s[-1]]]) / 1e5,
            where="mid", color="tab:blue", lw=1.8)
    a2.plot(xi, P0s / 1e5, "o", color="tab:blue", ms=6,
            label=r"$P_0(\xi)$: the five phases marched")
    a2.set_xlabel(r"cycle phase $\xi$ [--] (0 = wave passage)")
    a2.set_ylabel(r"chamber pressure $P_0$ [bar]", color="tab:blue")
    a2.tick_params(axis="y", labelcolor="tab:blue")
    a2.set_yscale("log")
    a2b = a2.twinx()
    a2b.plot(xi, T0s, "s--", color="tab:red", ms=5, lw=1.2)
    a2b.set_ylabel(r"chamber temperature $T_0$ [K]",
                   color="tab:red")
    a2b.tick_params(axis="y", labelcolor="tab:red")
    a2.legend(fontsize=7, loc="upper right")
    a2.set_title("(b) what the nozzle is handed: a periodic\nfamily"
                 " of chamber states (the mock cycle)", fontsize=9)
    a2.grid(**GRID)
    # (c) each phase wants its own nozzle; only one gets built
    eps_star = [CL.eps_star_at_pa(P0s[k], T0s[k], PA, tab0)
                for k in range(CL.NXI)]
    a3.plot(xi, eps_star, "o-", color="tab:blue", ms=6, lw=1.2,
            label=r"$\varepsilon$ that phase would want")
    a3.axhline(float(np.mean(eps_star)), color="0.4", lw=1.0,
               ls=":")
    a3.set_xlabel(r"cycle phase $\xi$ [--]")
    a3.set_ylabel(r"perfectly matched area ratio"
                  r" $\varepsilon$ [--]")
    a3.annotate("but only ONE nozzle is built:\nthe design is a"
                " compromise over\nthe whole family",
                xy=(0.5, float(np.mean(eps_star))),
                xytext=(0.30, float(np.mean(eps_star)) * 1.42),
                fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    a3.text(0.30, float(np.mean(eps_star)) * 0.90,
            r"dotted: the mean of what the phases want",
            fontsize=7, color="0.35")
    a3.set_title("(c) the design problem the cycle creates:\nfive"
                 " phases, one piece of hardware", fontsize=9)
    a3.legend(fontsize=7, loc="lower left")
    a3.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_rde_cycle.pdf")


def fig_method():
    """How this program decides that something passed: bands that
    the computation derives about itself, and deliberate corruptions
    that must be caught. Every point is a result of record."""
    # (name, measured, band) for positive checks, and rejectors as
    # multiples of their own band -- all quoted from the carriers.
    pos = [
        ("thrust: two routes agree", 2.85e3, 4.01e4),
        ("thrust: constant-pressure gauge", 3.35e-8, 1.78e-6),
        ("corner meter at matched ambient", 3.7e-10, 42.8),
        (r"first optimization: $p_e = p_a$", 916.0, 7958.0),
        ("prescribed wall: thrust twin", 1.37e4, 1.58e5),
        ("prescribed wall: mass", 12.3, 152.0),
        ("wall gradient (envelope)", 29.0, 109.0),
        ("plug: edge angle", 3.2e-4, 4.5e-3),
        ("plug: mass", 2.33, 26.0),
        ("plug: momentum", 6.9e3, 7.2e4),
        ("plug axisymmetric: mass", 505.0, 986.0),
        ("swirl: equilibrium preserved", 1.63e-15, 4.6e-15),
        (r"swirl: $\Gamma \to 0$ regression", 2.1e-13, 1.95e-6),
    ]
    rej = [
        ("corrupted ambient (plug)", 20.0),
        ("corrupted spike slope", 5.0),
        ("corrupted ambient (plug cycle)", 2.3),
        ("swirl switched off", 8.6),
        ("centrifugal source dropped", 12.0),
        ("corrupted circulation", 1.05e12),
        ("wrong characteristic feet", 84.0),
        ("design at the peak phase", 500.0),
        (r"$f_2$ along the wall", 149.0),
        ("lip-moving direction", 1000.0),
    ]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 5.0),
                                 gridspec_kw=dict(width_ratios=[1.5,
                                                                1]))
    yp = np.arange(len(pos))[::-1]
    rp = np.array([m / b for _, m, b in pos])
    a1.barh(yp, rp, 0.55, color="tab:blue", alpha=0.85)
    yr = np.arange(len(rej))[::-1] - len(pos) - 1.5
    rr = np.array([r for _, r in rej])
    a1.barh(yr, rr, 0.55, color="tab:red", alpha=0.8)
    a1.axvline(1.0, color="k", lw=1.4)
    a1.set_xscale("log")
    a1.set_xlim(1e-13, 1e13)
    a1.set_yticks(list(yp) + list(yr))
    a1.set_yticklabels([p[0] for p in pos] + [r[0] for r in rej],
                       fontsize=8)
    a1.set_xlabel("measured deviation, in units of that check's own"
                  " derived band [--]")
    a1.text(1e-11, yp[0] + 0.9, "POSITIVE CHECKS land here"
            r" ($<1$)", fontsize=7.5, color="tab:blue")
    a1.text(3.0, yr[-1] - 1.2, "REJECTORS land here"
            r" ($>1$)", fontsize=7.5, color="tab:red")
    a1.text(1.35, yr[0] + 0.3, "the band", fontsize=7,
            rotation=90, va="center")
    a1.set_ylim(yr[-1] - 2.2, yp[0] + 1.9)
    a1.set_title("(a) every check of this document, against its"
                 " own\nderived band --- and every deliberate"
                 " corruption", fontsize=9)
    a1.grid(axis="x", **GRID)
    # (b) where a band comes from
    h = np.array([1.0, 0.5])
    err = np.array([4.52, 1.0])
    a2.loglog(h, err, "o-", color="tab:blue", ms=8, lw=1.6)
    a2.loglog(h, err[1] * (h / h[1]) ** 2, "--", color="0.5",
              lw=1.0)
    a2.text(0.60, 2.6, "the same quantity,\ncomputed twice\n"
            r"(slope $\approx h^2$)", fontsize=7.5,
            color="tab:blue")

    band = 4.0 * (4.52 - 1.0)
    a2.axhspan(0.2, band, color="tab:green", alpha=0.13, lw=0)
    a2.axhline(band, color="darkgreen", lw=1.2, ls="-")
    a2.text(0.315, band * 1.15, r"band $= K_{\rm RICH}\,"
            r"|{\rm coarse}-{\rm fine}| + $ roundoff floor"
            + "\n" + r"($K_{\rm RICH}=4$): what the check is"
            r" allowed to be", fontsize=7, color="darkgreen")
    a2.text(0.315, 0.42, "PASS region --- derived by the"
            " computation about\nitself, never chosen by hand",
            fontsize=7, color="darkgreen")
    a2.set_xlabel("grid spacing $h$, relative [--]")
    a2.set_ylabel("residual of the check, relative [--]")
    a2.set_title("(b) where the band comes from: the scheme\n"
                 "measures its own error (no chosen tolerance)",
                 fontsize=9)
    a2.set_xlim(0.3, 1.7)
    a2.set_ylim(0.35, 90.0)
    a2.set_xticks([0.5, 1.0])
    a2.set_xticklabels(["0.5\n(fine grid)", "1.0\n(coarse grid)"])
    from matplotlib.ticker import NullFormatter
    a2.xaxis.set_minor_formatter(NullFormatter())
    a2.grid(**GRID, which="both")
    fig.tight_layout()
    save(fig, "fig_method.pdf")



# ------------------------------------------------- the designs, side by side
def fig_spike_designs():
    """S22: the designs as physical contours. (a) our theta_E = 0
    truncated spike at L = 2.5 m against GENO's Rao construction
    expanded to the same ambient (the full-length machine ours is a
    57% truncation of) and against GENO's mass+length design at 2.5 m
    (the VOID A/B: ambient becomes an output and the wall barely
    tapers). (b) what the optimizers actually moved at L = 2.5:
    adaptive and uniform optima minus the fan streamline, in mm.
    GENO walls from figs/data_rao_walls.npz (S21 gate-verified -O0
    build; provenance string inside)."""
    d = np.load(os.path.join(OUT, "data_rao_walls.npz"))
    import a1_config_compare as CC
    import a1_plug_spline_opt as PS
    import a1_plug_adaptive as AD

    w = CC.build_world()
    c = PS.build_case(w)
    art = json.load(open(os.path.join(ROOT, "validation",
                                      "_plug_adaptive", "design.json")))
    xk_a = np.array([float(eval(v)) for v in art["design"]["xk"]])
    W_a = np.array([float(eval(v)) for v in art["design"]["W"]])
    xk_u = np.array(art["control"]["xk"], dtype=float)
    W_u = np.array(art["control"]["W"], dtype=float)

    xg = np.linspace(PS.X0, PS.L, 500)
    y_str = np.interp(xg, c["sx"], c["sy"])
    y_ada = AD.respline(W_a, xk_a, c, xg)
    y_uni = AD.respline(W_u, xk_u, c, xg)

    fig, (a1, a2) = plt.subplots(
        1, 2, figsize=(9.6, 3.4),
        gridspec_kw=dict(width_ratios=[1.45, 1.0]))

    # (a) the machines, full view
    a1.plot(d["ideal_x"], d["ideal_y"], color="tab:green", lw=1.4,
            label=r"Rao construction, same ambient (GENO), $\theta_E \approx 0.03^\circ$")
    a1.plot(d["masslen_x"], d["masslen_y"], color="tab:red", lw=1.2,
            ls=":", label="mass+length at 2.5 m (GENO): the void A/B")
    sx, sy = c["sx"], c["sy"]
    keep = sx <= PS.L
    a1.plot(sx[keep], sy[keep], color="tab:blue", lw=1.6,
            label=r"fan streamline, $\theta_E = 0$, cut at $L=2.5$ m")
    a1.plot(xg, y_ada, color="tab:blue", lw=0.9, ls="--",
            label="free-form optimum ($m=11$): tail drops 87 mm")
    a1.plot([0.0], [w["RMAX"]], marker="o", ms=4, color="k")
    a1.annotate("lip", (0.0, w["RMAX"]), textcoords="offset points",
                xytext=(4, 4))
    a1.axvline(PS.L, color="0.55", lw=0.7, ls="-.")
    a1.axvspan(PS.L, float(d["ideal_x"].max()), color="tab:green",
               alpha=0.08)
    a1.annotate("the 57% the truncation removes",
                (0.5 * (PS.L + float(d["ideal_x"].max())), 0.45),
                ha="center", fontsize=8, color="tab:green")
    a1.set_xlabel("x [m]")
    a1.set_ylabel("y [m]")
    a1.set_title("(a) three machines, one world")
    a1.legend(loc="upper right", fontsize=7.2)
    a1.grid(**GRID)
    a1.set_xlim(-0.15, 6.1)
    a1.set_ylim(0.0, 2.75)

    # (b) what the optimizer moved, in mm
    a2.axhline(0.0, color="0.4", lw=0.7)
    a2.plot(xg, 1e3 * (y_ada - y_str), color="tab:blue", lw=1.4,
            label="adaptive optimum $-$ streamline ($m=11$)")
    a2.plot(xg, 1e3 * (y_uni - y_str), color="tab:orange", lw=1.2,
            ls="--", label="uniform optimum $-$ streamline ($m=11$)")
    for xkk in xk_a:
        a2.axvline(xkk, color="0.75", lw=0.4, zorder=0)
    x_new = float(art["history"][1]["sites"][0])
    a2.axvline(x_new, color="tab:blue", lw=0.8, ls=":")
    a2.annotate("inserted knot\n$x = %.4f$" % x_new, (x_new, None
                if False else 1e3 * (AD.respline(W_a, xk_a, c,
                np.array([x_new]))[0]
                - np.interp(x_new, c["sx"], c["sy"]))),
                textcoords="offset points", xytext=(10, 8),
                fontsize=7.5, color="tab:blue")
    a2.set_xlabel("x [m]")
    a2.set_ylabel(r"$\Delta y$ [mm]")
    a2.set_title("(b) what shape freedom bought at $L = 2.5$ m")
    a2.legend(fontsize=7.2)
    a2.grid(**GRID)
    fig.tight_layout()
    save(fig, "fig_spike_designs.pdf")


# --------------------------------------------- S23: the resolved ladder
def fig_s23_ladder():
    """The gain resolution of [X-PGRS], drawn from the committed
    verdict.json. (a) both designs' thrust vs march resolution: the
    streamline converges monotonically at first order onto its
    extrapolated limit; the fine-tuned optimum overshoots (the
    de-tuning transient) and descends onto the SAME limit. (b) the
    paired gain minus its extrapolated limit, log scale: a straight
    line = geometric convergence at the march's own order; the open
    marker is the model's prediction of rung 6 made before rung 6
    ran."""
    v = json.load(open(os.path.join(ROOT, "validation", "_plug_gain",
                                    "verdict.json")))
    Ji, Jf, g = (np.array(v["Ji"]), np.array(v["Jf"]),
                 np.array(v["gains"]))
    rungs = ["(61,51)", "(121,101)", "(241,201)", "(481,401)",
             "(961,801)", "(1921,1601)"]
    x = np.arange(1, 7)
    # limits of record (verdict.json): gain limit and band; inc limit
    # from its last window
    d45 = Ji[-2] - Ji[-3]; d56 = Ji[-1] - Ji[-2]
    r_i = d56 / d45
    Ji_lim = Ji[-1] + d56 * r_i / (1 - r_i)
    g_lim, band = float(v["gain"]), float(v["band"])

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.5))
    a1.axhline(Ji_lim / 1e6, color="0.45", lw=0.8, ls="--")
    a1.annotate("common limit %.5f MN" % (Ji_lim / 1e6),
                (0.98, Ji_lim / 1e6), xycoords=("axes fraction",
                                                "data"),
                ha="right", va="bottom", fontsize=7.5, color="0.35")
    a1.plot(x, Ji / 1e6, "o-", color="tab:blue", lw=1.3,
            label="fan streamline (ratios 0.51, 0.50, 0.50, 0.50)")
    a1.plot(x, Jf / 1e6, "s-", color="tab:orange", lw=1.3,
            label="free-form optimum, tuned at rung 2")
    a1.annotate("tuning rung", (2, Jf[1] / 1e6),
                textcoords="offset points", xytext=(8, -14),
                fontsize=7.5, color="tab:orange")
    a1.annotate("the de-tuning transient:\novershoot, then descent\n"
                "onto the same limit", (4.6, 115.90),
                fontsize=7.5, color="tab:orange", ha="center",
                xytext=(4.6, 115.90), xycoords="data",
                textcoords="data")
    a1.set_xticks(x, rungs, rotation=30, fontsize=7)
    a1.set_ylabel("thrust J [MN]")
    a1.set_xlabel("march resolution (K, N)")
    a1.set_title("(a) two designs, one limit")
    a1.legend(fontsize=7.2, loc="lower right")
    a1.grid(**GRID)

    a2.semilogy(x, 100 * (g - g_lim), "o-", color="tab:blue", lw=1.3,
                label=r"measured gain $-$ limit")
    # the model's prediction of rung 6 from rungs 3-5, made first
    dg = np.diff(g)
    g6_pred = g[4] + dg[3] * (dg[3] / dg[2])
    a2.semilogy([6], [100 * (g6_pred - g_lim)], "o", mfc="none",
                mec="tab:red", ms=9,
                label="rung 6 as PREDICTED before it ran")
    for k in range(1, 5):
        r = dg[k] / dg[k - 1]
        a2.annotate("%.2f" % r, (x[k] + 0.08,
                    100 * (g[k] - g_lim)), fontsize=7,
                    color="0.35")
    a2.set_xticks(x, rungs, rotation=30, fontsize=7)
    a2.set_xlabel("march resolution (K, N)")
    a2.set_ylabel(r"gain $-$ extrapolated limit  [%]")
    a2.set_title("(b) geometric convergence of the paired gain")
    a2.annotate("limit $%+.3f\\%%$, band $%.3f\\%%$\n"
                r"$\Rightarrow$ ZERO within band"
                % (100 * g_lim, 100 * band),
                (0.03, 0.06), xycoords="axes fraction", fontsize=8,
                bbox=dict(boxstyle="round", fc="white", ec="0.6"))
    a2.legend(fontsize=7.2, loc="upper right")
    a2.grid(**GRID, which="both")
    fig.tight_layout()
    save(fig, "fig_s23_ladder.pdf")


# --------------------------------------- S23: the driver, seen working
def fig_s23_driver():
    """The segmented TR-SQP driver at work, from the committed
    run-of-record log. (a) the accepted staircase of the (121,101)
    re-optimization with every rejection mechanism marked. (b) the
    no-motion wedge, measured: thrust along +grad on a step ladder is
    smooth and improving up to the fold at h ~ 3e-3; the first trial
    at radius 0.05 lands far past it (numbers of record, S23 probe)."""
    import re
    logp = os.path.join(ROOT, "validation", "_plug_gain",
                        "run_of_record_S23_fineopt.log")
    seg_re = re.compile(r"\[seg\s*(\d+)\] J = ([\d.e+]+)\s")
    rej_re = re.compile(r"\[seg\s*(\d+)\] trial J = ([\d.e+]+) REJ")
    nom_re = re.compile(r"\[seg\s*(\d+)\] no motion at radius")
    cer_re = re.compile(r"\[seg\s*(\d+)\] base REJECTED \(record not")
    acc, rej, nom, cer = [], [], [], []
    in_fine = False
    for ln in open(logp):
        if "fine optimization at" in ln:
            in_fine = True
        if "fresh ladders" in ln:
            break
        if not in_fine:
            continue
        m = seg_re.search(ln)
        if m:
            acc.append((int(m.group(1)), float(m.group(2))))
        m = rej_re.search(ln)
        if m:
            rej.append((int(m.group(1)), float(m.group(2))))
        if nom_re.search(ln):
            nom.append(int(nom_re.search(ln).group(1)))
        if cer_re.search(ln):
            cer.append(int(cer_re.search(ln).group(1)))
    J0 = acc[0][1]
    kN = lambda J: (J - J0) / 1e3

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.5))
    xs = [s for s, _ in acc]
    ys = [kN(J) for _, J in acc]
    a1.step(xs, ys, where="post", color="tab:blue", lw=1.4)
    a1.plot(xs, ys, "o", color="tab:blue", ms=4,
            label="certified base (accepted)")
    for s, J in rej:
        a1.annotate("", (s, min(kN(J), -1.5)), (s, 0.0),
                    arrowprops=dict(arrowstyle="->", color="tab:red",
                                    lw=1.1))
        a1.annotate("%.0f" % kN(J), (s, -1.9), ha="center",
                    fontsize=6.5, color="tab:red")
    a1.plot([], [], marker=r"$\downarrow$", ls="none",
            color="tab:red", label="trial rejected (J shown, kN)")
    a1.plot(nom, [0.4] * len(nom), "^", color="tab:orange", ms=6,
            label="no-motion retry (radius halved, same record)")
    a1.plot(cer, [-0.6] * len(cer), "x", color="tab:purple", ms=7,
            label="base rejected: not Newton-certified")
    a1.set_ylim(-2.4, 13)
    a1.set_xlabel("segment")
    a1.set_ylabel(r"$J - J_{\mathrm{start}}$ [kN]")
    a1.set_title("(a) the segmented walk at (121,101)")
    a1.legend(fontsize=6.8, loc="center right")
    a1.grid(**GRID)

    # (b) the wedge probe, numbers of record (S23 step 2)
    h = np.array([1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 5e-2])
    dJ = np.array([6.01738e-1, 6.01627e0, 6.00474e1, 5.87754e2,
                   7.09353e4, -7.51098e4, -1.62450e6])
    pred = 6.01751e6 * h
    a2.plot(h, pred, "--", color="0.5", lw=1.0,
            label=r"linear prediction $|\nabla J|\,h$")
    up = dJ > 0
    a2.plot(h[up], dJ[up], "o", color="tab:blue",
            label=r"measured $\Delta J$ along $+\nabla J$ ($>0$)")
    a2.plot(h[~up], -dJ[~up], "v", color="tab:red",
            label=r"measured $-\Delta J$ (fold: worse)")
    a2.set_xscale("log")
    a2.set_yscale("log")
    a2.axvspan(3e-3, 5e-2, color="tab:red", alpha=0.07)
    a2.annotate("the fold:\nevery step here\nlooks worse",
                (1.2e-2, 3e1), fontsize=7.5, color="tab:red",
                ha="center")
    a2.annotate("first trial,\nradius 0.05", (5e-2, 1.62450e6),
                textcoords="offset points", xytext=(-52, -6),
                fontsize=7.5, color="tab:red")
    a2.set_xlabel(r"step size $h$ along $+\nabla J/|\nabla J|$")
    a2.set_ylabel(r"$|\Delta J|$ [N]")
    a2.set_title("(b) the no-motion wedge, measured")
    a2.legend(fontsize=7.2, loc="upper left")
    a2.grid(**GRID, which="both")
    fig.tight_layout()
    save(fig, "fig_s23_driver.pdf")

if __name__ == "__main__":
    fig_nozzle_primer()
    fig_bell_vs_plug()
    fig_rde_cycle()
    fig_method()
    fig_contours()
    fig_jeps()
    fig_ripple()
    fig_f2()
    fig_stationarity()
    fig_cycle()
    fig_votes()
    fig_plug()
    fig_plug_before()
    fig_plug_cycle()
    fig_plug_posing()
    fig_geno_twin()
    fig_swirl()
    fig_plug_lessons()
    fig_moc_primer()
    fig_fan_singularity()
    fig_freejet()
    fig_edge_root_geometry()
    fig_spike_designs()
    fig_s23_ladder()
    fig_s23_driver()
    print("ALL FIGURES DONE ->", OUT)
