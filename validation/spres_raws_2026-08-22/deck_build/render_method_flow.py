# -*- coding: utf-8 -*-
"""Method-flow diagram for C13 (CKP-S3-3, user order 2026-08-23):
explain HOW the machine works — the functional, why the adjoint, which
optimizer, what each stage produces — in plain engineering language.
Replaces the status-graph on the main deck; dense graphs stay in backup.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp

RED, TEAL, GRAY, LGRAY = "#822433", "#006778", "#2b2b2b", "#9a9a9a"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "stix"})

BLOCKS = [
    ("ENGINE DATA", "specs or measurements\n→ the cycle at the interface:\nstates $s(\\xi)$, one per phase", TEAL),
    ("THE FUNCTIONAL", "cycle-averaged thrust of the\nshared contour $\\Sigma$:\n$J[\\Sigma]=\\int_\\Xi F[\\Sigma;s(\\xi)]\\,d\\mu$", RED),
    ("FLOW SOLVE", "supersonic march,\nphase by phase\n(fast, checked)", GRAY),
    ("ADJOINT", "ONE extra backward solve\n→ exact gradient of $J$\nfor ALL wall parameters", RED),
    ("OPTIMIZER", "trust-region Newton,\ncurvature measured —\ncontour update", GRAY),
    ("CERTIFY", "independent checks\nthat can reject;\nerror bars attached", TEAL),
]


def main():
    fig, ax = plt.subplots(figsize=(12.6, 3.7))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.65); ax.axis("off")
    bw, gap = 2.35, 0.29
    x0 = (16 - 6 * bw - 5 * gap) / 2
    centers = []
    for i, (name, sub, col) in enumerate(BLOCKS):
        x = x0 + i * (bw + gap)
        centers.append(x + bw / 2)
        ax.add_patch(mp.FancyBboxPatch((x, 1.35), bw, 2.35,
                     boxstyle="round,pad=0.07", fc="white", ec=col, lw=2.0))
        ax.text(x + bw / 2, 3.38, name, fontsize=10.2, ha="center",
                color=col, weight="bold")
        ax.text(x + bw / 2, 2.28, sub, fontsize=7.6, ha="center",
                color=GRAY, linespacing=1.3)
        if i < 5:
            ax.annotate("", xy=(x + bw + gap - 0.03, 2.5),
                        xytext=(x + bw + 0.03, 2.5),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.8))
    # iterate loop: optimizer -> flow solve
    ax.annotate("", xy=(centers[2], 1.02), xytext=(centers[4], 1.02),
                arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.7,
                                connectionstyle="arc3,rad=0.22"))
    ax.text((centers[2] + centers[4]) / 2, 0.28,
            "iterate — seconds per design step", fontsize=9.5, ha="center",
            color=TEAL, style="italic")
    # output chip
    ax.text(centers[5], 3.85, "output: contour + certificates + error bars,\ntogether",
            fontsize=9.5, ha="center", color=TEAL, weight="bold")
    # gradient annotation under adjoint
    ax.text(centers[3], 0.55, "why the adjoint: the whole gradient\nat the cost of one extra solve",
            fontsize=9.0, ha="center", color=RED, style="italic")
    os.makedirs(OUT, exist_ok=True)
    fig.savefig(os.path.join(OUT, "fig_method_flow.png"), dpi=200,
                facecolor="white", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("rendered fig_method_flow.png")


if __name__ == "__main__":
    main()
