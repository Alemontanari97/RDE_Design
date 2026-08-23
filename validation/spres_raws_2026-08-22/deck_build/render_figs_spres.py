# -*- coding: utf-8 -*-
"""Home diagrams for the S-PRES deck (style pact (b): serif matplotlib,
in-figure interpretive annotations, house palette #822433/#006778,
white opaque background, 200 dpi).

Consumers: build_deck_spres.py (slides C2, C8, C8-bis, C9, C10, C16,
C18). Content sources cited per figure in comments; no number here is
new — every value re-anchored to the spec notes of the consuming slide.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np

RED, TEAL, GRAY, LGRAY = "#822433", "#006778", "#2b2b2b", "#9a9a9a"
AMBER = "#b8860b"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "stix",
    "axes.edgecolor": GRAY, "text.color": GRAY,
})


def _save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, facecolor="white",
                bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("rendered", name)


# ------------------------------------------------------------- C2 interface
def fig_c2_interface():
    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis("off")
    # chamber + nozzle walls (upper half sketch, axis at bottom)
    ax.plot([0.3, 4.0], [5.6, 5.6], color=GRAY, lw=2.4)          # chamber outer
    ax.plot([4.0, 6.2, 9.6], [5.6, 4.4, 5.9], color=GRAY, lw=2.4)  # converge-diverge
    ax.plot([0.3, 9.6], [1.0, 1.0], color=GRAY, lw=1.2)          # axis
    ax.annotate("", xy=(9.55, 1.0), xytext=(8.9, 1.0),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.2))
    # heat release zone
    ax.add_patch(mp.Rectangle((0.8, 1.0), 2.6, 4.6, color=RED, alpha=0.08))
    ax.text(2.1, 1.5, "heat release\n(rotating front)", color=RED,
            fontsize=10.5, ha="center")
    # corrugated sonic line near the geometric throat
    y = np.linspace(1.0, 4.4, 200)
    x = 6.2 + 0.55 * np.sin(6.5 * y) * (0.35 + 0.65 * (y - 1.0) / 3.4)
    ax.plot(x, y, color=RED, lw=2.2)
    ax.text(6.15, 6.15, "sonic surface: corrugated,\ncrosses M = 1 twice per cycle",
            color=RED, fontsize=10.5, ha="center")
    # design interface, downstream with margin
    ax.plot([8.5, 8.5], [1.0, 5.75], color=TEAL, lw=2.4, ls=(0, (5, 3)))
    ax.text(8.62, 3.1, "design interface:\naxially supersonic,\nwith margin,\ndownstream of\nheat release",
            color=TEAL, fontsize=10.5, va="center")
    ax.text(5.05, 0.35, "geometric throat $\\neq$ design interface", fontsize=11,
            color=GRAY, ha="center", style="italic")
    _save(fig, "fig_c2_interface.png")


# ------------------------------------------------------------- C8 quotient
def fig_c8_quotient():
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    ax.set_xlim(0, 16); ax.set_ylim(0, 8); ax.axis("off")
    # (a) annulus, lab frame
    c = (2.3, 4.6)
    ax.add_patch(mp.Circle(c, 1.7, fill=False, color=GRAY, lw=2))
    ax.add_patch(mp.Circle(c, 1.05, fill=False, color=GRAY, lw=2))
    th = np.linspace(0.35, 1.25, 40)
    ax.plot(c[0] + 1.37 * np.cos(th), c[1] + 1.37 * np.sin(th), color=RED, lw=5)
    ax.annotate("", xy=(c[0] + 1.95 * np.cos(1.55), c[1] + 1.95 * np.sin(1.55)),
                xytext=(c[0] + 1.95 * np.cos(0.75), c[1] + 1.95 * np.sin(0.75)),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6,
                                connectionstyle="arc3,rad=0.28"))
    ax.text(c[0], 1.9, "lab frame:\nperiodic, unsteady", fontsize=11, ha="center")
    # arrow ->
    ax.annotate("", xy=(6.05, 4.6), xytext=(4.7, 4.6),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.8))
    ax.text(5.35, 5.05, "rotate with\nthe wave", fontsize=10, ha="center")
    # (b) wave frame steady
    c2 = (7.9, 4.6)
    ax.add_patch(mp.Circle(c2, 1.7, fill=False, color=GRAY, lw=2))
    ax.add_patch(mp.Circle(c2, 1.05, fill=False, color=GRAY, lw=2))
    for k in range(12):
        a = 2 * np.pi * k / 12
        ax.plot([c2[0] + 1.05 * np.cos(a), c2[0] + 1.7 * np.cos(a)],
                [c2[1] + 1.05 * np.sin(a), c2[1] + 1.7 * np.sin(a)],
                color=TEAL, lw=1.0)
    ax.text(c2[0], 1.9, "wave frame: STEADY —\nazimuth $=$ phase $\\xi$",
            fontsize=11, ha="center", color=TEAL)
    # (c) two reductions
    ax.annotate("", xy=(11.6, 6.0), xytext=(9.8, 5.3),
                arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.8))
    ax.annotate("", xy=(11.6, 2.6), xytext=(9.8, 3.7),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8))
    ax.add_patch(mp.FancyBboxPatch((11.55, 4.95), 4.15, 2.5,
                 boxstyle="round,pad=0.12", fc="#e8f1f2", ec=TEAL, lw=1.6))
    ax.text(13.6, 7.02, "per-phase family $\\{s(\\xi)\\}$", fontsize=11,
            ha="center", color=TEAL, weight="bold")
    ax.text(13.6, 5.85, "phases kept separate:\nan EXACT quotient\n(one declared O(St) approx.)",
            fontsize=9.5, ha="center", color=GRAY)
    ax.add_patch(mp.FancyBboxPatch((11.55, 0.85), 4.15, 2.5,
                 boxstyle="round,pad=0.12", fc="#f6ecee", ec=RED, lw=1.6))
    ax.text(13.6, 2.92, "global time average $\\bar s$", fontsize=11,
            ha="center", color=RED, weight="bold")
    ax.text(13.6, 1.75, "mixes the phases:\nthe crudest reduction —\nthe field's, not ours",
            fontsize=9.5, ha="center", color=GRAY)
    _save(fig, "fig_c8_quotient.png")


# --------------------------------------------------------- C8-bis envelope
def _bell(ax, x0, y0, s=1.0, color=GRAY):
    t = np.linspace(0, 1, 60)
    xu = x0 + s * (0.15 + 0.85 * t)
    yu = y0 + s * (0.16 + 0.30 * t ** 0.7)
    ax.plot(xu, yu, color=color, lw=1.8)
    ax.plot(xu, 2 * y0 - yu + 2 * s * 0.0, color=color, lw=1.8)  # mirror about y0
    ax.plot([x0, x0 + 0.15 * s], [y0 + 0.28 * s, y0 + 0.16 * s], color=color, lw=1.8)
    ax.plot([x0, x0 + 0.15 * s], [y0 - 0.28 * s, y0 - 0.16 * s], color=color, lw=1.8)


def _plug(ax, x0, y0, s=1.0, color=GRAY, truncated=True, shroud=False):
    t = np.linspace(0, 1, 60)
    L = 0.85 if truncated else 1.15
    xs = x0 + s * L * t
    ys = y0 + s * 0.30 * (1 - t) ** 1.6
    ax.plot(xs, ys, color=color, lw=1.8)
    ax.plot(xs, 2 * y0 - ys, color=color, lw=1.8)
    if truncated:
        ax.plot([xs[-1], xs[-1]], [2 * y0 - ys[-1], ys[-1]], color=color, lw=1.8)
    ax.plot([x0 - 0.05 * s, x0 + 0.1 * s], [y0 + 0.42 * s, y0 + 0.33 * s], color=color, lw=1.8)
    ax.plot([x0 - 0.05 * s, x0 + 0.1 * s], [y0 - 0.42 * s, y0 - 0.33 * s], color=color, lw=1.8)
    if shroud:
        ax.plot([x0 + 0.05 * s, x0 + 0.6 * s], [y0 + 0.5 * s, y0 + 0.44 * s], color=color, lw=1.8)
        ax.plot([x0 + 0.05 * s, x0 + 0.6 * s], [y0 - 0.5 * s, y0 - 0.44 * s], color=color, lw=1.8)


def fig_c8bis_envelope():
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    ax.set_xlim(0, 16); ax.set_ylim(0, 8); ax.axis("off")
    # envelope
    ax.add_patch(mp.FancyBboxPatch((0.4, 1.4), 4.1, 5.0, boxstyle="round,pad=0.15",
                 fc="none", ec=TEAL, lw=2.2, linestyle=(0, (6, 3))))
    ax.text(2.45, 6.85, "the design variable:\na SOLID BODY inside an envelope",
            fontsize=11.5, ha="center", color=TEAL, weight="bold")
    _plug(ax, 1.6, 3.9, s=1.9, color=GRAY, truncated=True)
    ax.text(2.45, 1.85, "attachment at the lip,\nuniform-cone condition",
            fontsize=9.5, ha="center", color=GRAY)
    ax.annotate("", xy=(6.1, 3.9), xytext=(5.0, 3.9),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2.0))
    ax.text(5.55, 4.55, "the classes\nEMERGE", fontsize=9.5, ha="center")
    # sector cards (text-only: name + status chip)
    cards = [
        ("bell", "driver today — 9 DOF", TEAL),
        ("truncated plug", "named campaign —\nthe programme's configuration", RED),
        ("shrouded plug", "named campaign", GRAY),
        ("expansion–deflection", "admissible class", GRAY),
    ]
    for i, (name, status, col) in enumerate(cards):
        x = 6.6 + (i % 2) * 4.85
        yy = 4.45 - (i // 2) * 3.1
        ax.add_patch(mp.FancyBboxPatch((x, yy), 4.35, 2.5, boxstyle="round,pad=0.1",
                     fc="white", ec=col, lw=1.9))
        ax.text(x + 2.17, yy + 1.85, name, fontsize=11.5, ha="center",
                color=col, weight="bold")
        ax.text(x + 2.17, yy + 0.85, status, fontsize=9.0, ha="center",
                color=GRAY, style="italic")
    _save(fig, "fig_c8bis_envelope.png")


# ------------------------------------------------------------- C9 fiber
def fig_c9_fiber():
    fig, ax = plt.subplots(figsize=(9.2, 4.2))
    ax.set_xlim(0, 16); ax.set_ylim(0, 8); ax.axis("off")
    # left: fixed pressure trace
    xi = np.linspace(0, 2 * np.pi, 200)
    p = 3.4 + 1.5 * np.exp(-2.2 * ((xi - 1.2) % (2 * np.pi)) ** 2) + 0.35 * np.sin(2 * xi)
    ax.plot(1.0 + 3.4 * xi / (2 * np.pi), 2.2 + 0.62 * p, color=GRAY, lw=2.4)
    ax.add_patch(mp.FancyBboxPatch((0.8, 3.0), 3.9, 3.3, boxstyle="round,pad=0.1",
                 fc="none", ec=GRAY, lw=1.4))
    ax.text(2.75, 6.85, "the SAME pressure trace $P(\\xi)$", fontsize=11,
            ha="center", weight="bold")
    ax.text(2.75, 2.35, "fixed at the interface", fontsize=9.5, ha="center",
            style="italic")
    # middle: the fiber = family of compatible states
    ax.annotate("", xy=(6.3, 4.6), xytext=(5.0, 4.6),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.8))
    for k, (dy, sw, lab) in enumerate([(1.62, 0.55, "high swirl"),
                                       (0.0, 0.22, "medium swirl"),
                                       (-1.62, 0.02, "no swirl")]):
        y0 = 4.35 + dy
        col = [RED, AMBER, TEAL][k]
        ax.add_patch(mp.FancyBboxPatch((6.6, y0 - 0.68), 3.6, 1.36,
                     boxstyle="round,pad=0.08", fc="white", ec=col, lw=1.6))
        th = np.linspace(0, 3.4, 40)
        ax.plot(7.15 + 0.3 * np.cos(th) * (1 + 0.14 * th),
                y0 + sw * 0.48 * np.sin(th) * (1 + 0.14 * th), color=col, lw=1.5)
        ax.text(7.85, y0, f"$s_{k+1}$ — {lab}", fontsize=9.6, va="center", color=col)
    ax.text(8.4, 7.35, "a whole FAMILY of\ndistinct states remains", fontsize=10.5,
            ha="center", color=GRAY, weight="bold")
    # right: different thrusts
    ax.annotate("", xy=(11.5, 4.35), xytext=(10.6, 4.35),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.8))
    for k, (dy, ln) in enumerate([(1.62, 3.0), (0.0, 2.5), (-1.62, 2.1)]):
        col = [RED, AMBER, TEAL][k]
        y0 = 4.35 + dy
        ax.annotate("", xy=(11.9 + ln, y0), xytext=(11.9, y0),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.6))
        ax.text(11.9 + ln + 0.12, y0, f"$F_{k+1}$", fontsize=11, va="center", color=col)
    ax.text(13.5, 7.35, "DIFFERENT thrust", fontsize=11.5, ha="center",
            color=RED, weight="bold")
    ax.text(13.5, 1.35, "established without one CFD run", fontsize=9.8,
            ha="center", style="italic")
    _save(fig, "fig_c9_fiber.png")


# ------------------------------------------------------------ C10 operator
def fig_c10_operator():
    fig, ax = plt.subplots(figsize=(9.2, 4.0))
    ax.set_xlim(0, 16); ax.set_ylim(0, 8); ax.axis("off")
    ax.add_patch(mp.FancyBboxPatch((0.5, 3.0), 3.9, 2.4, boxstyle="round,pad=0.12",
                 fc="white", ec=GRAY, lw=2))
    ax.text(2.45, 4.65, "full azimuthal physics", fontsize=11, ha="center", weight="bold")
    ax.text(2.45, 3.6, "(wave-frame steady field)", fontsize=9.3, ha="center")
    ax.annotate("", xy=(6.0, 4.2), xytext=(4.5, 4.2),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2.2))
    ax.text(5.25, 5.75, "reduction", fontsize=10, ha="center", color=GRAY)
    ax.add_patch(mp.FancyBboxPatch((6.1, 3.0), 3.9, 2.4, boxstyle="round,pad=0.12",
                 fc="#e8f1f2", ec=TEAL, lw=2))
    ax.text(8.05, 4.65, "per-phase family", fontsize=11, ha="center",
            color=TEAL, weight="bold")
    ax.text(8.05, 3.6, "(what the machine designs on)", fontsize=9.3, ha="center")
    # discarded operator branch
    ax.annotate("", xy=(8.05, 1.85), xytext=(8.05, 2.9),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2))
    ax.text(8.5, 2.35, "what is discarded is an EXPLICIT operator\n(machine-verified identities)",
            fontsize=9.6, color=RED, va="center")
    chans = [
        ("mean channel", "exactly ZERO — proven", TEAL, True),
        ("jumps at the fronts", "the declared HEEL:\nno number yet", RED, False),
        ("covariance", "measured by the first\ncampaign of the phase", AMBER, False),
    ]
    for i, (name, sub, col, struck) in enumerate(chans):
        x = 1.2 + i * 4.9
        ax.add_patch(mp.FancyBboxPatch((x, 0.25), 4.3, 1.45, boxstyle="round,pad=0.1",
                     fc="white", ec=col, lw=1.8))
        ax.text(x + 2.15, 1.28, name, fontsize=10.5, ha="center", color=col, weight="bold")
        ax.text(x + 2.15, 0.62, sub, fontsize=8.8, ha="center", color=GRAY)
    _save(fig, "fig_c10_operator.png")


# ------------------------------------------------------------- C16 bars
def fig_c16_bars():
    # targets MET — values of record (CH4-feed-4; S25-bis formal MET)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    items = [
        ("design segment [s]", 20.0, 15.0, 30.0),
        ("full campaign [min]", 14.0, 10.0, 25.0),
    ]
    for i, (lab, hi, lo, tgt) in enumerate(items):
        y = 1 - i
        ax.barh(y, tgt, height=0.42, color="#e6e6e6", edgecolor=LGRAY)
        ax.barh(y, hi, height=0.42, color=TEAL, alpha=0.35, edgecolor=TEAL)
        ax.barh(y, lo, height=0.42, color=TEAL, edgecolor=TEAL)
        ax.plot([tgt, tgt], [y - 0.32, y + 0.32], color=RED, lw=2.4)
        ax.text(tgt, y + 0.38, "target", color=RED, fontsize=10, ha="center")
        ax.text(lo * 0.5, y, f"{lo:g}–{hi:g}", color="white", fontsize=11,
                ha="center", va="center", weight="bold")
        ax.text(-0.6, y, lab, fontsize=11, ha="right", va="center")
    ax.set_xlim(0, 33); ax.set_ylim(-0.65, 1.8); ax.axis("off")
    ax.text(16, 1.72, "measured (range)  vs  target — both MET",
            fontsize=11.5, ha="center", color=GRAY, weight="bold")
    _save(fig, "fig_c16_bars.png")


# ------------------------------------------------------------- C18 ladder
def fig_c18_ladder():
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    steps = [
        ("A — engine specs only", "enough to design"),
        ("B/C — cycle frequency,\nmean conditions", ""),
        ("D/E — high-speed pressure\nat the station", ""),
        ("F/G — hot-fire imaging,\nclass-verified", "highest reliability"),
    ]
    for i, (lab, sub) in enumerate(steps):
        x0, y0 = 0.45 + i * 0.62, 0.5 + i * 1.85
        ax.add_patch(mp.FancyBboxPatch((x0, y0), 5.6, 1.55, boxstyle="round,pad=0.09",
                     fc="#e8f1f2" if i else "white", ec=TEAL, lw=1.7))
        ax.text(x0 + 2.8, y0 + (0.98 if sub else 0.78), lab, fontsize=8.8,
                ha="center", color=TEAL, weight="bold")
        if sub:
            ax.text(x0 + 2.8, y0 + 0.32, sub, fontsize=8.0, ha="center",
                    color=GRAY, style="italic")
    ax.annotate("", xy=(8.6, 7.35), xytext=(7.0, 0.85),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2.0))
    ax.text(9.1, 4.0, "each datum climbs\nthe declared ladder", fontsize=9.0,
            rotation=90, va="center", ha="center", color=GRAY)
    # entry gate glyph, top-left free corner
    ax.add_patch(mp.FancyBboxPatch((0.35, 8.35), 4.5, 1.25, boxstyle="round,pad=0.09",
                 fc="#f6ecee", ec=RED, lw=1.7))
    ax.text(2.6, 8.97, "entry gate: data is ADMITTED —\nand the gate can say no",
            fontsize=9.0, ha="center", color=RED)
    _save(fig, "fig_c18_ladder.png")


ALL = [fig_c2_interface, fig_c8_quotient, fig_c8bis_envelope, fig_c9_fiber,
       fig_c10_operator, fig_c16_bars, fig_c18_ladder]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f in ALL:
        f()
