#!/usr/bin/env python3
"""Generate the figures for docs/rde_nozzle_A1_brick2_thrust.md from the
actual run data (checkpoints, GENO fields, and numbers of record from
the carrier logs). Output: docs/figs_a1/*.png. Rerun after data changes:

    .venv-a1/bin/python docs/build_figs_a1_brick2.py
"""
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FIGD = os.path.join(HERE, "figs_a1")
os.makedirs(FIGD, exist_ok=True)
sys.path.insert(0, os.path.join(ROOT, "validation"))

STEEL = "#1f4e7a"
FLAME = "#b23a12"
GREY = "#5a626b"
SCRATCH = ("/tmp/claude-1700/-data10-falco-MOSE/"
           "92be2bd8-b160-4811-adea-5510ee63a15f/scratchpad")

plt.rcParams.update({
    "figure.dpi": 150, "font.size": 9, "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True,
    "grid.alpha": 0.25, "grid.linewidth": 0.5})


def save(fig, name):
    p = os.path.join(FIGD, name)
    fig.savefig(p, bbox_inches="tight")
    plt.close(fig)
    print("wrote", p)


# ---------------------------------------------------------------- F1
# the two contours: Brick 1's ideal nozzle and GENO's TOC
def fig_contours():
    from g0_geno_crosscode import read_grid
    import a1_ideal_march_jax as A1
    import jax.numpy as jnp
    tab = A1.prep_tab(A1.build_tab_nasa())
    CASE = A1.CASE
    P0 = jnp.array([CASE["yt"], CASE["rtu"], CASE["rtd"], CASE["eps"]])
    cfg = dict(NI=CASE["NI"], Ne=CASE["Ne"], da_deg=CASE["da_deg"])
    ck = os.path.join(FIGD, "_ideal_wall.npz")
    if os.path.exists(ck):
        d = np.load(ck)
        wx, wy = d["x"], d["y"]
    else:
        out, _ = A1.run_march(P0, tab, cfg)
        wx, wy = np.array(out["wall_x"]), np.array(out["wall_y"])
        np.savez(ck, x=wx, y=wy)
    g = read_grid(os.path.join(SCRATCH, "toc_eps4_full"))
    ok = g["rho"][0] > 0
    tx, ty = g["x"][0][ok], g["y"][0][ok]

    fig, ax = plt.subplots(figsize=(5.6, 2.6))
    ax.plot(wx, wy, color=STEEL, lw=2,
            label="ideal nozzle (Brick 1, type 0): L = 7.34")
    ax.plot(tx, ty, color=FLAME, lw=2,
            label="Rao TOC (GENO, type 2): L = 5.5, same eps = 4")
    ax.axhline(0, color=GREY, lw=0.8, ls="-.")
    ax.plot([0], [1.0], "ko", ms=3)
    ax.annotate("throat", (0, 1.0), textcoords="offset points",
                xytext=(4, -12), fontsize=8)
    ax.set_xlabel("x / y_t")
    ax.set_ylabel("y / y_t")
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.set_ylim(-0.1, 2.3)
    save(fig, "contours.png")


# ---------------------------------------------------------------- F2
# J(eps) landscape from the step-3 driver checkpoint
def fig_jeps():
    ck = json.load(open(os.path.join(ROOT, "validation",
                                     "_driver_eps_ckpt.json")))
    pa = 7.614420e+05
    pts = []
    for k, v in ck.items():
        if not k.startswith("c:"):
            continue
        e = float(k.split(":")[1])
        J = v["J0"] - pa * np.pi * v["ylip"] ** 2
        pts.append((e, J))
    pts.sort()
    e, J = np.array(pts).T
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    ax.plot(e, J / 1e8, "o-", color=STEEL, ms=4, lw=1,
            label="J(eps): 13 march evaluations (cached)")
    ax.axvline(5.150634, color=FLAME, lw=1.2, ls="--",
               label="closed-form eps* = 5.1506 (exit-area lemma)")
    ax.axvline(5.15512, color=STEEL, lw=1.2, ls=":",
               label="blind golden search: eps = 5.1551")
    ax.set_xlabel("area ratio eps")
    ax.set_ylabel("J(eps) x 1e-8")
    ax.legend(frameon=False, fontsize=7.3, loc="lower center")
    axI = ax.inset_axes([0.60, 0.55, 0.37, 0.40])
    m = (e > 5.0) & (e < 5.35)
    axI.plot(e[m], J[m] / 1e8, "o-", color=STEEL, ms=3, lw=0.8)
    axI.axvline(5.150634, color=FLAME, lw=1, ls="--")
    axI.axvline(5.15512, color=STEEL, lw=1, ls=":")
    axI.tick_params(labelsize=6)
    axI.set_title("zoom at the top: the two lines\ndiffer by 0.09%",
                  fontsize=6.3)
    save(fig, "jeps.png")


# ---------------------------------------------------------------- F3
# f2 on the terminal characteristic vs along the wall (O3.3 data)
def fig_f2():
    from g0_geno_crosscode import read_grid
    import a1_ideal_march_jax as A1
    from a1_o33_toc import geno_terminal, toc_wall, f2_lam3
    from scipy.interpolate import griddata
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    g = read_grid(os.path.join(SCRATCH, "toc_eps4_full"))
    xs, ys, ug, vg, pg, rg, gg, sp, icol = geno_terminal(g)
    Vg = np.sqrt(ug**2 + vg**2)
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

    # arc-length parameterization of both curves
    def arclen(x, y):
        ds = np.hypot(np.diff(x), np.diff(y))
        s_ = np.concatenate([[0], np.cumsum(ds)])
        return s_ / s_[-1]
    o = np.argsort(ys[ok])
    yt_, xt_ = ys[ok][o], xs[ok][o]
    f2o_s, f2g_s = f2o[o], f2g[ok][o]
    s_term = arclen(xt_, yt_)
    s_wall = arclen(a[:, 3], a[:, 0])

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(7.6, 3.1),
                                   gridspec_kw={"width_ratios":
                                                [1.0, 1.35]})
    # LEFT: where the two curves live
    axL.plot(xw, yw, color=GREY, lw=2, label="TOC wall")
    axL.plot(xt_, yt_, "-", color=STEEL, lw=2)
    axL.plot(xt_, yt_, "o", color=STEEL, ms=3)
    axL.annotate("sampled segment of the\nterminal characteristic\n"
                 "(GENO col 192, near the lip)",
                 (xt_[len(xt_) // 2], yt_[len(yt_) // 2]),
                 textcoords="offset points", xytext=(-130, -42),
                 fontsize=7.5, color=STEEL,
                 arrowprops=dict(arrowstyle="->", color=STEEL, lw=0.8))
    axL.annotate("wall (a streamline)",
                 (xw[len(xw) // 3], yw[len(xw) // 3]),
                 textcoords="offset points", xytext=(-10, 12),
                 fontsize=7.5, color=GREY)
    axL.plot([0], [1.0], "ko", ms=3)
    axL.annotate("throat", (0, 1.0), textcoords="offset points",
                 xytext=(4, -10), fontsize=7)
    axL.set_ylim(0.85, 2.15)
    axL.set_xlabel("x / y_t")
    axL.set_ylabel("y / y_t")
    axL.set_title("where the two curves are", fontsize=8.5)
    # RIGHT: f2 along each curve, normalized arc length
    axR.plot(s_wall, f2w, "s-", color=GREY, ms=3, lw=1,
             label="wall: +64% (not invariant)")
    axR.plot(s_term, f2o_s, "o-", color=STEEL, ms=4, lw=0.8,
             label="terminal char. - OUR field")
    axR.plot(s_term, f2g_s, "x", color=FLAME, ms=6, mew=1.5,
             label="same nodes - GENO")
    axR.set_xlabel("normalized position along each curve")
    axR.set_ylabel("f2  [m/s]")
    axR.legend(frameon=False, fontsize=7, loc="center left",
               bbox_to_anchor=(0.02, 0.42))
    axR.set_title("the first integral f2 = -lambda2", fontsize=8.5)
    # inset: zoom on the flat line — constancy + cross-code agreement
    axI = axR.inset_axes([0.44, 0.10, 0.53, 0.36])
    axI.plot(s_term, f2o_s, "o-", color=STEEL, ms=3, lw=0.8)
    axI.plot(s_term, f2g_s, "x", color=FLAME, ms=5, mew=1.2)
    axI.set_ylim(2626, 2643)
    axI.tick_params(labelsize=6)
    axI.set_title("zoom: flat to 4e-3, codes agree to 9e-5",
                  fontsize=6.5)
    fig.tight_layout()
    save(fig, "f2_first_integral.png")


# ---------------------------------------------------------------- F4
# gradient ripple decomposition (numbers of record, step-4 log)
def fig_ripple():
    amps = np.array([-2e-4, -1e-4, 0.0, 1e-4, 2e-4])
    gs = np.array([472516.2, 465233.8, 457993.6, 450790.2, 443386.1])
    A = np.polyfit(amps, gs, 1)
    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    xx = np.linspace(amps[0], amps[-1], 100)
    ax.plot(xx * 1e4, np.polyval(A, xx) / 1e5, "-", color=GREY, lw=1,
            label="linear fit: smooth curvature J'' = -7.3e7 (physical)")
    ax.plot(amps * 1e4, gs / 1e5, "o", color=STEEL, ms=5,
            label="AD samples dJ/damp (exact derivative of the code)")
    ax.errorbar(amps * 1e4, np.polyval(A, amps) / 1e5,
                yerr=44.1 / 1e5 * 4,
                fmt="none", ecolor=FLAME, capsize=3, lw=1.2,
                label="table-kink ripple: std 44 = 0.010% of the"
                      " gradient")
    ax.set_xlabel("wall bump amplitude x 1e4")
    ax.set_ylabel("dJ/damp x 1e-5")
    ax.legend(frameon=False, fontsize=7.5)
    save(fig, "grad_ripple.png")


# ---------------------------------------------------------------- F5
# stationarity at the TOC (numbers of record, step-6 log)
def fig_stationarity():
    toc = [1.166e4, 3.028e4, 3.573e4, 1.755e4, 1.882e3, 9.705e4]
    pert = [1.4e6, 6.2e5, 3.9e6, 7.0e5, 1.3e6, 2.1e5]
    lip = 1.3103e7
    fig, ax = plt.subplots(figsize=(5.6, 2.9))
    ix = np.arange(6)
    ax.bar(ix - 0.18, np.abs(toc), 0.36, color=STEEL,
           label="|dJ/da| at the TOC (stationary)")
    ax.bar(ix + 0.18, np.abs(pert), 0.36, color=GREY,
           label="same, on a perturbed wall (40x larger)")
    ax.bar([6.2], [lip], 0.5, color=FLAME,
           label="lip-moving direction at the TOC (1000x: vacuum"
                 " theorem)")
    ax.set_yscale("log")
    ax.set_xticks(list(ix) + [6.2])
    ax.set_xticklabels(["b1", "b2", "b3", "b4", "b5", "b6", "lip"])
    ax.set_ylabel("|projected gradient|")
    ax.legend(frameon=False, fontsize=7.5, loc="upper left")
    save(fig, "stationarity.png")




# ---------------------------------------------------------------- F6
# the cycle layer: J_cycle(eps) for the T3 cycle and the mock RDE
def fig_cycle():
    ck = json.load(open(os.path.join(ROOT, "validation",
                                     "_cycle_ckpt.json")))
    pa = 7.614420e+05
    by_eps = {}
    for k, v in ck.items():
        e, P0, T0 = k.split(":")
        e, T0 = float(e), float(T0)
        kind = "t3" if abs(T0 - 3740.0) < 1 else "mock"
        F = v["mdot"] * v["qe"] + (v["pe"] - pa) * np.pi * v["ylip"]**2
        by_eps.setdefault((kind, e), []).append(F)
    curves = {"t3": [], "mock": []}
    for (kind, e), Fs in by_eps.items():
        if len(Fs) == 5:
            curves[kind].append((e, np.mean(Fs)))
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    for kind, col, lab in (("t3", GREY,
                            "P-only blowdown (T3 class)"),
                           ("mock", STEEL,
                            "mock RDE: P AND T profiles in theta")):
        pts = sorted(curves[kind])
        e, J = np.array(pts).T
        ax.plot(e, J / 1e8, "o-", color=col, ms=4, lw=1, label=lab)
    ax.axvline(5.15063, color=GREY, lw=1, ls="--",
               label="design at <P> (T3 collapse)")
    ax.axvline(5.17783, color=FLAME, lw=1.2, ls="--",
               label="pressure-weighted mean-state design")
    ax.axvline(5.13951, color=STEEL, lw=1.2, ls=":",
               label="blind cycle optimum (mock)")
    ax.set_xlabel("area ratio eps")
    ax.set_ylabel("J_cycle x 1e-8")
    ax.set_xlim(4.15, 6.45)
    ax.legend(frameon=False, fontsize=7, loc="lower left")
    save(fig, "cycle_layer.png")




# ---------------------------------------------------------------- F7
# the transversality votes (step 8) — from the cycle checkpoint
def fig_votes():
    import a1_ideal_march_jax as A1
    import a1_cycle_layer as CL
    ck = json.load(open(CL.CKPT))
    tab0 = A1.prep_tab(A1.build_tab_nasa())
    ts, ps = tab0["ts"], tab0["ps"]
    pa = 7.614420e+05
    xi = (np.arange(CL.NXI) + 0.5) / CL.NXI
    I1 = (1.0 - 1.0 / CL.PR) / np.log(CL.PR)
    P0s = (ps / I1) * CL.PR ** (-xi)
    gm = tab0["gammamedio"]
    T0s = 3850.0 * (CL.PR ** ((gm - 1) / gm)) ** (-xi)

    def votes(eps):
        return np.array([ck["%.6f:%.6e:%.3f" % (eps, P0s[k], T0s[k])
                         ]["pe"] - pa for k in range(CL.NXI)])
    R = votes(5.139510)
    Rb = votes(10.289200)
    fig, ax = plt.subplots(figsize=(6.0, 3.0))
    ax.bar(xi - 0.033, R / 1e5, 0.06, color=STEEL,
           label="votes at the cycle OPTIMUM (eps = 5.14)")
    ax.bar(xi + 0.033, Rb / 1e5, 0.06, color=GREY,
           label="votes at the PEAK design (eps = 10.29)")
    ax.axhspan(-0.48, 0.48, color=STEEL, alpha=0.10,
               label="balance band (derived): where 'zero' lives")
    ax.axhline(R.mean() / 1e5, color=STEEL, lw=1.2, ls="--")
    ax.axhline(Rb.mean() / 1e5, color=GREY, lw=1.2, ls="--")
    ax.axhline(0, color="k", lw=0.7)
    ax.text(0.93, R.mean() / 1e5 + 0.35, "mean ~ 0", color=STEEL,
            fontsize=7.5, ha="right")
    ax.text(0.93, Rb.mean() / 1e5 - 0.75, "mean far below zero",
            color=GREY, fontsize=7.5, ha="right")
    ax.set_xticks(xi)
    ax.set_xticklabels(["wave\npassage", "early", "mid", "late",
                        "tail"], fontsize=7.5)
    ax.set_xlabel("cycle phase")
    ax.set_ylabel("corner vote R = p_e - p_a  [1e5 Pa]")
    ax.annotate("underexpanded:\n'lengthen me'",
                (xi[0] - 0.033, R[0] / 1e5),
                textcoords="offset points", xytext=(16, -16),
                fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.7))
    ax.annotate("overexpanded:\n'shorten me'",
                (xi[-1] - 0.033, R[-1] / 1e5),
                textcoords="offset points", xytext=(-70, -26),
                fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.7))
    ax.legend(frameon=False, fontsize=7.3, loc="upper right")
    save(fig, "votes.png")


# ---------------------------------------------------------------- F8
# the plug oracle and the measured mesh pathology (step 9b)
def fig_plug():
    import a1_ideal_march_jax as A1
    import a1_plug_march as PM
    from a1_freejet_unit import q_at_pa
    import jax.numpy as jnp
    tg = A1.prep_tab(A1.build_tab_gconst())
    ta = A1.tab_arrays(tg)
    gam, Rg, ts = tg["_g"], tg["Rg"], tg["ts"]
    M1, M2 = 1.5, 2.2
    dnu, field, q_of = PM.pm_exact(gam, Rg, ts, M1, M2)
    q1, q2 = q_of(M1), q_of(M2)
    pa = float(A1.state_q(jnp.float64(q2), ta)[1])
    qpa = q_at_pa(pa, ta, tg["_as"])
    lip = (0.0, 2.0)
    x0, x_end = 0.5, 3.0
    xs, ys = PM.exact_streamline(field, lip, (0.0, 1.0), x_end)
    # run the (current) march, coarse, to expose the mesh
    y_wall0 = float(np.interp(x0, xs, ys))
    y_edge0 = lip[1] + np.tan(dnu) * x0
    yline = np.linspace(y_edge0, y_wall0, 21)
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
    out, _ = PM.plug_march(st, start, qpa, tg, 0.0)
    mp = np.array(out["mesh_pts"])
    e = np.array(out["edge"])

    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    # exact structures
    mu1, mu2 = np.arcsin(1 / M1), np.arcsin(1 / M2)
    for phi in np.linspace(-mu1, dnu - mu2, 9):
        ax.plot([lip[0], lip[0] + 3.2 * np.cos(phi)],
                [lip[1], lip[1] + 3.2 * np.sin(phi)],
                color=GREY, lw=0.5, alpha=0.5)
    ax.plot(xs, ys, color=FLAME, lw=2, label="exact spike (streamline)")
    xe = np.linspace(0, 3.0, 10)
    ax.plot(xe, lip[1] + np.tan(dnu) * xe, color=STEEL, lw=2,
            ls="--", label="exact jet edge (angle dnu)")
    ax.axvline(x0, color="k", lw=1, ls=":",
               label="start line (exact field data)")
    # the marched mesh (pathology visible downstream)
    ax.plot(mp[:, 0], mp[:, 1], ".", ms=1.5, color=STEEL, alpha=0.5)
    ax.plot(e[:, 0], e[:, 1], "o", ms=3, color=STEEL,
            label="marched edge points")
    ax.plot([lip[0]], [lip[1]], "k^", ms=6)
    ax.annotate("cowl lip (PM fan)", lip, textcoords="offset points",
                xytext=(6, 6), fontsize=7.5)
    ax.annotate("the current march degrades downstream:\nonce the"
                " wall-speed bias sets in (lesson 3),\nmesh points"
                " scatter below the exact spike\nand the edge never"
                " reaches its line",
                (1.45, 1.62), fontsize=7.5, color=GREY)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-0.15, 3.25)
    ax.set_ylim(0.55, 3.35)      # frame the physical window: diverged
    # mesh points from the failing region must not stretch the axes
    ax.legend(frameon=False, fontsize=7, loc="upper left")
    save(fig, "plug_oracle.png")


if __name__ == "__main__":
    fig_jeps()
    fig_ripple()
    fig_stationarity()
    fig_contours()
    fig_f2()
    fig_cycle()
    fig_votes()
    fig_plug()
    print("all figures written to", FIGD)
