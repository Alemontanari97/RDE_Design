"""Figures: how the code represents the literature profiles (S32,
2026-09-21) -- Chutkey 2014's plug and primary nozzle, Dutton & Addy
1982's four throats. Presentation only; no result of record is
computed here (the numbers come from the carriers' stages)."""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                        # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.dirname(HERE)
sys.path.insert(0, VAL)
import a1_chutkey_twin as CT                            # noqa: E402
import a1_annular_kernel as AK                          # noqa: E402
import a1_frame_march as FM                             # noqa: E402
import a1_plug_march as PM                              # noqa: E402
import jax.numpy as jnp                                 # noqa: E402
import a1_ideal_march_jax as A1                         # noqa: E402

# the reference palette (dataviz skill): ours / theirs / measured / fourth
C_OURS, C_THEIRS, C_DATA, C_4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, MUTED, SURF = "#0b0b0b", "#52514e", "#898781", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "axes.grid": True, "grid.color": "#e6e5e1", "grid.linewidth": 0.6,
                     "font.size": 9, "axes.titlesize": 10, "legend.frameon": False,
                     "axes.spines.top": False, "axes.spines.right": False})
MM = CT.MM


def save(fig, name):
    out = os.path.join(HERE, name)
    fig.savefig(out, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print("wrote", out)


# ----------------------------------------------------------------------
# 1. Chutkey 2014: the plug contour and the primary nozzle, record frame
# ----------------------------------------------------------------------
def chutkey_primary_nozzle():
    """Half-contour of the symmetric convergent duct (p. 479) in its own
    X1-Y1 frame, mm: horizontal line, arc R 1.343, 45 deg line, arc R
    0.867 ending horizontal at the throat X1 = 0 with half-height 1.3235."""
    h2 = 0.5 * CT.H_T * 1e3
    R4, R2 = 0.867, 1.343
    x4 = np.linspace(-0.617, 0.0, 60)
    y4 = h2 + R4 - np.sqrt(R4**2 - x4**2)
    y3a, y3b = y4[0], y4[0] + (-0.617 + 2.743)
    x3 = np.array([-2.743, -0.617]); y3 = np.array([y3b, y3a])
    yh = y3b + R2 * (1.0 - np.cos(np.radians(45.0)))
    x2 = np.linspace(-3.744, -2.743, 40)
    y2 = yh - R2 + np.sqrt(np.maximum(R2**2 - (x2 + 3.744)**2, 0.0))
    x1 = np.array([-6.294, -3.744]); y1 = np.array([yh, yh])
    X = np.concatenate([x1, x2, x3, x4]); Y = np.concatenate([y1, y2, y3, y4])
    return X, Y


def to_record_mm(X1, Y1):
    """primary-nozzle frame (mm) -> record frame (mm): X1 along the throat
    flow direction (-56.9 deg), Y1 toward the lip; origin at the throat midpoint."""
    th = np.radians(-CT.TILT_DEG)
    Xm = 0.5 * CT.FOOT[0] * 1e3
    Ym = 0.5 * (CT.FOOT[1] + CT.R_LIP) * 1e3
    return Xm + X1 * np.cos(th) - Y1 * np.sin(th), Ym + X1 * np.sin(th) + Y1 * np.cos(th)


def fig_chutkey():
    w = CT.build_world()
    raw = np.loadtxt(CT.CONTOUR)
    cx, cy = CT.load_contour(True)
    sx, sy, rms = CT.smooth_contour(cx, cy)
    th = np.radians(-CT.TILT_DEG)
    Xm, Ym = 0.5 * CT.FOOT[0] * CT.S_LEN, 0.5 * (CT.FOOT[1] + CT.R_LIP) * CT.S_LEN
    xw, yw, sw = FM._wall_in_frame(w, th, Xm, Ym, "angelino")
    Xa, Ya, _, _ = FM.to_record(xw, yw, np.zeros_like(xw), np.zeros_like(xw), th, Xm, Ym)
    X1, Y1 = chutkey_primary_nozzle()
    fig, (ax, axz) = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw=dict(width_ratios=[1.5, 1]))
    for a in (ax, axz):
        a.set_aspect("equal")
        # the primary nozzle: both walls
        for sgn, lab in ((+1, "primary nozzle, cowl side"), (-1, "primary nozzle, plug side")):
            Xr, Yr = to_record_mm(X1, sgn * Y1)
            a.plot(Xr, Yr, color=INK, lw=1.2, label=lab if a is ax else None)
        Xt, Yt = to_record_mm(np.array([0.0, 0.0]), np.array([-1.3235, 1.3235]))
        a.plot(Xt, Yt, color=C_4, lw=1.4, label="throat line (2.647 mm, 56.9 deg)" if a is ax else None)
        a.plot(sx * MM, sy * MM, color=C_OURS, lw=1.6, label="smoothing spline (the twin's wall)" if a is ax else None)
        a.plot(Xa * MM, Ya * MM, color=C_THEIRS, lw=1.2, ls="--", label="Angelino foot blend (first 3 mm)" if a is ax else None)
        a.scatter(raw[:, 0] * 1e3 + (CT.FOOT[0] * 1e3 - raw[0, 0] * 1e3), raw[:, 1] * 1e3, s=9, color=C_DATA, zorder=3,
                  label="digitised Fig. 2b (registered)" if a is ax else None)
        a.scatter([0.0], [CT.R_LIP * 1e3], s=30, color=INK, marker="v", zorder=4)
        a.scatter([CT.FOOT[0] * 1e3], [CT.FOOT[1] * 1e3], s=30, color=INK, marker="^", zorder=4)
    # the record's cut at 1.5 mm
    x0 = CT.X0_MM
    for a in (ax, axz):
        a.axvline(x0, color=MUTED, lw=0.8, ls=":")
    ax.text(x0 + 1.0, 24.0, "cut of record\nx = 1.5 mm", color=INK2, fontsize=8)
    ax.set_xlim(-9, 110); ax.set_ylim(-1, 36)
    ax.set_xlabel("x [mm], plug axis"); ax.set_ylabel("r [mm]")
    ax.set_title("Chutkey 2014 ATPN: the plug contour and the primary nozzle as the code holds them")
    ax.legend(loc="upper right", fontsize=8)
    axz.set_xlim(-9, 6); axz.set_ylim(24, 38)
    axz.set_title("the throat region (zoom)")
    axz.set_xlabel("x [mm]")
    axz.annotate("lip (0, 32)", (0.0, 32.0), (1.0, 33.2), color=INK2, fontsize=8, arrowprops=dict(arrowstyle="-", color=MUTED))
    axz.annotate("foot (-2.22, 30.55)", (CT.FOOT[0] * 1e3, CT.FOOT[1] * 1e3), (-6.5, 29.0), color=INK2, fontsize=8,
                 arrowprops=dict(arrowstyle="-", color=MUTED))
    axz.text(-8.8, 36.6, "primary nozzle p. 479: 45 deg ramps and arcs\nR 1.343 / 0.867 mm on h/2 1.32 mm\n(R/h 0.66: outside every throat series)", color=INK2, fontsize=8)
    save(fig, "01_chutkey_contour_and_primary_nozzle.png")


# ----------------------------------------------------------------------
# 2. Chutkey's primary nozzle throat in the kernel (indicative, R_c 0.33)
# ----------------------------------------------------------------------
def fig_chutkey_kernel():
    d_m, rc = CT.H_T, AK.CASES["chutkey_primary_arc_radius_m"]
    gam, eta = CT.GAMMA, 2.0
    P = AK.throat_params(CT.FOOT[1], d_m, CT.TILT_DEG, rc, rc, eta, gam)
    grid, fields, _ = AK.solve_kernel(P["y_i"], P["g1"], P["g2"], P["h1"], P["h2"], P["b1"], gam, eta)
    eps, K = P["eps"], P["K"]
    X1, Y1 = chutkey_primary_nozzle()
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.set_aspect("equal")
    ax.plot(X1, Y1, color=INK, lw=1.2); ax.plot(X1, -Y1, color=INK, lw=1.2)
    ax.plot([0, 0], [-1.3235, 1.3235], color=C_4, lw=1.4, label="throat line")
    # the kernel field on the throat region, x in [-0.6, 0.6] d
    xs = np.linspace(-0.6, 0.6, 121) * d_m * 1e3
    ys = np.linspace(-1.3235, 1.3235, 81)
    XX, YY = np.meshgrid(xs, ys)
    z = (XX / (d_m * 1e3)) / (K * eps**0.5)
    yk = P["y_i"] + (YY + 1.3235) / (d_m * 1e3)
    # mask the wall region (the kernel's parabolic walls)
    for nt, col, ls in ((3, C_OURS, "-"), (1, C_THEIRS, "--")):
        u, v = AK.series_uv(grid, fields, eps, gam, z.ravel(), yk.ravel(), nt)
        q2 = (u**2 + v**2).reshape(XX.shape)
        M = np.sqrt(q2 / (0.5 * (gam + 1) - 0.5 * (gam - 1) * q2))
        wall_o = 1.3235 + XX**2 / (2 * rc * 1e3); wall_i = -wall_o
        M = np.where((YY < wall_o) & (YY > wall_i), M, np.nan)
        cs = ax.contour(XX, YY, M, levels=[0.8, 0.9, 1.0, 1.1, 1.2, 1.3], colors=col, linewidths=1.2, linestyles=ls)
        if nt == 3:
            ax.clabel(cs, fmt="M %.1f", fontsize=7, colors=INK2)
    ax.plot([], [], color=C_OURS, label="kernel, 3 terms (eta 2)")
    ax.plot([], [], color=C_THEIRS, ls="--", label="kernel, 1 term")
    ax.set_xlim(-4.0, 1.6); ax.set_ylim(-2.4, 2.4)
    ax.set_xlabel("X1 [mm], along the primary nozzle axis"); ax.set_ylabel("Y1 [mm]")
    ax.set_title("Chutkey's primary nozzle throat in the annular kernel: R_c 0.33, NOT converged (indicative)")
    ax.legend(loc="lower left", fontsize=8)
    save(fig, "02_chutkey_primary_throat_kernel_indicative.png")


# ----------------------------------------------------------------------
# 3. Dutton & Addy 1982, Fig. 6: wall Mach
# ----------------------------------------------------------------------
def fig_dutton6():
    D = AK.dutton_case("fig6")
    ser = AK._load("fig6_series.csv"); exp = AK._load("fig6_exp_wall.csv"); od = AK._load("fig6_onedim.csv")
    Z = np.linspace(-0.55, 0.5, 200)
    Mo = D["M_at"](Z, np.full_like(Z, D["grid"].y_o))
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.plot(od[:, 0], od[:, 1], color=MUTED, lw=1.0, ls=":", label="1-D (digitised)")
    ax.plot(ser[:, 0], ser[:, 1], color=C_THEIRS, lw=1.6, ls="--", label="Dutton & Addy series (digitised)")
    ax.plot(Z, Mo, color=C_OURS, lw=1.8, label="our series, read at y = y_o")
    ax.scatter(exp[:, 0], exp[:, 1], s=28, color=C_DATA, zorder=3, label="measured wall Mach (full + half nozzle)")
    ax.set_xlabel("Z (throat radii)"); ax.set_ylabel("M on the wall")
    ax.set_title("Dutton & Addy Fig. 6 -- axisymmetric nozzle, R_co 1.0, eta 2")
    ax.legend(loc="upper left", fontsize=8)
    ax.text(0.02, 0.35, "vs their series: rms 0.021\nvs data: rms 0.050 (their series 0.065)", color=INK2, fontsize=8)
    save(fig, "03_dutton_fig6_wall_mach.png")


# ----------------------------------------------------------------------
# 4. Dutton & Addy Fig. 8, 9, 10: iso-Mach contours
# ----------------------------------------------------------------------
def fig_dutton_contours():
    figs = ("fig8", "fig9", "fig10")
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.8))
    for ax, name in zip(axes, figs):
        D = AK.dutton_case(name)
        c = D["c"]
        # registration of the inclined cases on their series (as the stage does)
        if c["Z_star"] is None:
            pts = []
            for lev in AK.CASES["dutton_levels"]:
                try:
                    S = AK._load("%s_series_m%.1f.csv" % (name, lev))
                except OSError:
                    continue
                pts.extend([(lev, a, b) for a, b in S])
            pts = np.array(pts)
            best = None
            for dz in np.linspace(*AK.CASES["zstar_search"][:2], int(AK.CASES["zstar_search"][2])):
                D["frm"]["Zs"] = D["Zs"] + dz
                r = np.sqrt(np.mean((D["M_at"](pts[:, 1], pts[:, 2]) - pts[:, 0])**2))
                if best is None or r < best[1]:
                    best = (dz, r)
            D["frm"]["Zs"] = D["Zs"] + best[0]
        prof = AK._load("%s_profile.csv" % name)
        ax.scatter(prof[:, 0], prof[:, 1], s=6, color=MUTED, label="digitised walls")
        # the posed walls (the kernel's parabolic arcs) through the map
        xx = np.linspace(-0.9, 0.9, 200) / D["d"]
        for yfun, lab in ((lambda x: D["grid"].y_o + x**2 / (2 * c["R_co"]), "posed arcs"),
                          (lambda x: D["grid"].y_i - x**2 / (2 * c["R_ci"]), None)):
            Zw, Rw = D["to_fig"](xx, yfun(xx))
            ax.plot(Zw, Rw, color=INK, lw=1.0, label=lab)
        # our field on a grid
        Zg = np.linspace(-0.75, 0.75, 181); Rg = np.linspace(0.2, 1.3, 161)
        ZZ, RR = np.meshgrid(Zg, Rg)
        xk, yk = D["from_fig"](ZZ, RR)
        zk = xk / (D["P"]["K"] * D["eps"]**0.5)
        inside = (yk > D["grid"].y_i - xk**2 / (2 * c["R_ci"])) & (yk < D["grid"].y_o + xk**2 / (2 * c["R_co"])) & (np.abs(zk) <= 1.05)
        M = D["M_at"](ZZ.ravel(), RR.ravel()).reshape(ZZ.shape)
        M = np.where(inside, M, np.nan)
        cs = ax.contour(ZZ, RR, M, levels=AK.CASES["dutton_levels"], colors=C_OURS, linewidths=1.4)
        ax.clabel(cs, fmt="%.1f", fontsize=7, colors=INK2)
        for lev in AK.CASES["dutton_levels"]:
            for kind, col, mk, ms in (("series", C_THEIRS, "x", 18), ("exp", C_DATA, "o", 22)):
                try:
                    A = AK._load("%s_%s_m%.1f.csv" % (name, kind, lev))
                except OSError:
                    continue
                ax.scatter(A[:, 0], A[:, 1], s=ms, color=col, marker=mk, zorder=3, linewidths=1.0)
        ax.plot([], [], color=C_OURS, label="our series (iso-M 0.6..1.4)")
        ax.scatter([], [], color=C_THEIRS, marker="x", label="their series (digitised)")
        ax.scatter([], [], color=C_DATA, marker="o", label="measured")
        ax.set_aspect("equal"); ax.set_xlim(-0.75, 0.75); ax.set_ylim(0.2, 1.3)
        ax.set_xlabel("Z"); ax.set_ylabel("R" if ax is axes[0] else "")
        ax.set_title("%s: R_ci %.2f R_co %.2f y_i %.2f beta %+.3f" % (name.upper(), c["R_ci"], c["R_co"], c["y_i"], c["beta_rad"]), fontsize=9)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=5, fontsize=8, bbox_to_anchor=(0.5, 0.93))
    fig.suptitle("Dutton & Addy 1982, annular throats: the derived kernel against their series and their measurements"
                 " (frames registered on their series; the series' reach |z| <= 1)", fontsize=10)
    save(fig, "04_dutton_fig8_9_10_contours.png")


if __name__ == "__main__":
    fig_chutkey()
    fig_chutkey_kernel()
    fig_dutton6()
    fig_dutton_contours()
