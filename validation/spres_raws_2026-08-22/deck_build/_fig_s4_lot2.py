# S4 lot 2 (CKP-S3-5(c)/(d)): two home figures.
# 1) figs/fig_c9_gauge.png  — same-gauge/different-thrust cartoon (C9 rework)
# 2) figs/fig_cadj_cost.png — finite-difference vs adjoint cost schematic
# Deck palette (spreslib): RED 822433, TEAL 006778, grays.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import os

RED, TEAL, GRAY, LGRAY = "#822433", "#006778", "#4a4a4a", "#9a9a9a"
plt.rcParams.update({"font.family": "serif", "font.size": 13,
                     "axes.linewidth": 0})
HERE = os.path.dirname(os.path.abspath(__file__))


def gauge(ax, cx, cy, r=0.55, needle_deg=135):
    ax.add_patch(mp.Circle((cx, cy), r, fc="white", ec=GRAY, lw=2.2, zorder=5))
    for a in np.linspace(200, -20, 9):
        x0 = cx + 0.82 * r * np.cos(np.radians(a))
        y0 = cy + 0.82 * r * np.sin(np.radians(a))
        x1 = cx + 0.95 * r * np.cos(np.radians(a))
        y1 = cy + 0.95 * r * np.sin(np.radians(a))
        ax.plot([x0, x1], [y0, y1], color=LGRAY, lw=1.4, zorder=6)
    a = np.radians(needle_deg)
    ax.plot([cx, cx + 0.8 * r * np.cos(a)], [cy, cy + 0.8 * r * np.sin(a)],
            color=RED, lw=2.6, zorder=7)
    ax.add_patch(mp.Circle((cx, cy), 0.05 * r, fc=RED, ec=RED, zorder=8))


def duct(ax, x0, y0, w=3.4, h=1.7):
    """Simple converging duct, side view; returns interior box."""
    up = [(x0, y0 + h), (x0 + 0.62 * w, y0 + h), (x0 + w, y0 + 0.70 * h)]
    lo = [(x0, y0), (x0 + 0.62 * w, y0), (x0 + w, y0 + 0.30 * h)]
    ax.plot(*zip(*up), color=GRAY, lw=3, solid_capstyle="round")
    ax.plot(*zip(*lo), color=GRAY, lw=3, solid_capstyle="round")
    return x0, y0, w, h


def fig_c9():
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 4.4))
    cases = [("Flow A — no swirl", "straight"),
             ("Flow B — swirling", "swirl")]
    for ax, (label, kind) in zip(axs, cases):
        ax.set_xlim(0, 7.4)
        ax.set_ylim(-1.15, 4.4)
        ax.axis("off")
        x0, y0, w, h = duct(ax, 0.6, 0.55)
        # inflow arrows
        for i, yy in enumerate(np.linspace(y0 + 0.32, y0 + h - 0.32, 3)):
            if kind == "straight":
                ax.annotate("", xy=(x0 + 1.5, yy), xytext=(x0 + 0.25, yy),
                            arrowprops=dict(arrowstyle="-|>", color=TEAL,
                                            lw=2.4))
            else:
                xs = np.linspace(x0 + 0.25, x0 + 1.55, 60)
                ys = yy + 0.17 * np.sin(2 * np.pi * (xs - x0) / 1.05
                                        + i * 2.1)
                ax.plot(xs, ys, color=TEAL, lw=2.4)
                ax.annotate("", xy=(xs[-1] + 0.16, ys[-1]),
                            xytext=(xs[-1] - 0.05, ys[-1]),
                            arrowprops=dict(arrowstyle="-|>", color=TEAL,
                                            lw=2.4))
        # gauge on top, SAME needle position
        gx = x0 + 1.15
        gy = y0 + h + 1.15
        ax.plot([gx, gx], [y0 + h, gy - 0.55], color=GRAY, lw=2)
        gauge(ax, gx, gy)
        ax.text(gx + 0.75, gy + 0.05, "same\nreading", color=GRAY,
                fontsize=12, va="center")
        # thrust arrow out of the exit
        Ln = 1.55 if kind == "straight" else 1.0
        yex = y0 + 0.5 * h
        ax.annotate("", xy=(x0 + w + 0.35 + Ln, yex),
                    xytext=(x0 + w + 0.35, yex),
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=4.5))
        ax.text(x0 + w + 0.4, yex - 0.62,
                "thrust F" if kind == "straight" else "thrust F′ ≠ F",
                color=RED, fontsize=15, ha="left", fontweight="bold")
        ax.text(x0 + 0.5 * w, -0.85, label, color=GRAY, fontsize=14,
                ha="center")
    fig.suptitle("Two flows, identical at the pressure gauge — "
                 "different thrust", color=RED, fontsize=16, y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    out = os.path.join(HERE, "figs", "fig_c9_gauge.png")
    fig.savefig(out, dpi=220)
    print("wrote", out)


def fig_cadj():
    fig, ax = plt.subplots(figsize=(10.6, 4.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.6)
    ax.axis("off")

    def box(x, y, w, h, txt, ec, fs=11, fc="white", bold=False):
        ax.add_patch(mp.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.06", fc=fc, ec=ec, lw=1.8))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center",
                fontsize=fs, color=ec,
                fontweight="bold" if bold else "normal")

    # top row: finite differences
    ax.text(0.1, 5.15, "one-at-a-time (finite differences)", color=GRAY,
            fontsize=14, va="center")
    n = 9
    for i in range(n):
        box(0.1 + i * 0.92, 3.85, 0.8, 0.75, "flow\nsolve", LGRAY, fs=9)
    ax.text(0.1 + n * 0.92 + 0.12, 4.22, "… one per parameter",
            color=GRAY, fontsize=12, va="center")
    ax.text(11.9, 4.22, "cost ∝ N", color=GRAY, fontsize=14,
            ha="right", va="center", style="italic")

    # bottom row: adjoint
    ax.text(0.1, 2.35, "the adjoint way", color=TEAL, fontsize=14,
            va="center")
    box(0.1, 0.85, 2.1, 0.95, "flow solve\n(forward)", TEAL, fs=11)
    box(2.65, 0.85, 2.4, 0.95, "adjoint solve\n(backward)", TEAL, fs=11,
        bold=True)
    ax.annotate("", xy=(2.62, 1.32), xytext=(2.23, 1.32),
                arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.2))
    ax.annotate("", xy=(5.85, 1.32), xytext=(5.1, 1.32),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.6))
    box(5.9, 0.72, 4.1, 1.2,
        "dJ/d(shape) for every parameter\n— exact, in one pass", RED,
        fs=12, bold=True, fc="#f7eef0")
    ax.text(11.9, 1.32, "cost ≈ 2", color=TEAL, fontsize=14,
            ha="right", va="center", style="italic")
    fig.tight_layout()
    out = os.path.join(HERE, "figs", "fig_cadj_cost.png")
    fig.savefig(out, dpi=220)
    print("wrote", out)


def fig_c2_interface():
    """SOTA re-draw (user order S4): meridional cut of the annular
    channel + plug throat; corrugated sonic surface with subsonic
    pockets; design interface downstream. Overwrites the S3 micro-schema."""
    fig, ax = plt.subplots(figsize=(9.6, 5.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    # channel walls (meridional cut): outer wall + center-body with throat
    xs = np.linspace(0.4, 11.6, 300)
    outer = np.full_like(xs, 5.0)
    inner = 1.0 + 1.9 * np.exp(-((xs - 7.2) / 1.9) ** 2)   # plug hump
    ax.plot(xs, outer, color=GRAY, lw=3.5, solid_capstyle="round")
    ax.plot(xs, inner, color=GRAY, lw=3.5, solid_capstyle="round")
    ax.fill_between(xs, 0.35, inner, color="#ececec", zorder=0)
    ax.text(7.2, 1.15, "center-body (plug)", color=GRAY, fontsize=11,
            ha="center")

    # heat-release zone (rotating front), near injection
    ax.fill_betweenx([1.02, 5.0], 0.9, 2.6, color="#f3dfe3", zorder=0)
    ax.text(1.75, 5.35, "heat release\n(rotating front)", color=RED,
            fontsize=11.5, ha="center", va="bottom")

    # flow arrows
    for yy in (2.2, 3.4, 4.5):
        ax.annotate("", xy=(4.0, yy), xytext=(2.9, yy),
                    arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.2))

    # corrugated sonic surface across the channel at the throat
    yy = np.linspace(inner[np.argmin(np.abs(xs - 7.2))] + 0.03, 4.97, 200)
    xson = 7.2 + 0.55 * np.sin(2 * np.pi * (yy - 1.0) / 1.15)
    ax.plot(xson, yy, color=RED, lw=2.8)
    ax.text(7.2, 5.55, "sonic surface M = 1 — corrugated,\nsubsonic and "
            "supersonic bands coexist", color=RED, fontsize=12,
            ha="center", va="bottom", fontweight="bold")
    # subsonic pockets (left lobes of the corrugation)
    for yc in (3.05, 4.2):
        ax.text(6.15, yc, "M<1", color=RED, fontsize=10, ha="center",
                style="italic")
        ax.text(8.35, yc, "M>1", color=TEAL, fontsize=10, ha="center",
                style="italic")

    # design interface, downstream with margin
    ax.plot([10.4, 10.4], [1.16, 5.0], color=TEAL, lw=2.6, ls=(0, (5, 3)))
    ax.text(10.6, 3.0, "design interface:\naxially supersonic,\n"
            "with margin", color=TEAL, fontsize=12, va="center")

    # geometric throat marker
    ax.annotate("geometric throat", xy=(7.2, 2.95), xytext=(4.6, 0.62),
                color=GRAY, fontsize=11,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.4))
    fig.tight_layout()
    out = os.path.join(HERE, "figs", "fig_c2_interface.png")
    fig.savefig(out, dpi=220)
    print("wrote", out)


fig_c9()
fig_cadj()
fig_c2_interface()
