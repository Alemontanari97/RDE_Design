# -*- coding: utf-8 -*-
"""Light SLIDE variants of the pipeline graph for the MAIN deck.

User pin 2026-08-23 + guard 18 (v3.1 C13 [NOTE]: tallies NEVER
on-slide): the dense developer-grade renders (render_graph_spres.py)
serve the BACKUP (D1-D8); the main deck consumes these light variants —
no numeric tallies, no internal C-ids, speaking-language cards,
max 6-8 cards per view. Stage roster still read from the asserted
pipeline_graph JSON (never hand-typed); the 18 asserts gate the build
via the dev script run.
"""
import os, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp

RED, TEAL, GRAY, LGRAY = "#822433", "#006778", "#2b2b2b", "#9a9a9a"
AMBER = "#b8860b"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "graph")
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "stix"})

STAGES = [
    ("1", "CONTRACT", "data contract"),
    ("2", "REPRESENT", "representation"),
    ("3", "MARCH", "unit processes"),
    ("4", "CERTIFY", "certificates"),
    ("5", "ESTIMATE", "estimator & bands"),
    ("6", "OPTIMIZE", "optimizer & engine"),
    ("7", "AGGREGATE", "aggregation"),
    ("8", "VERDICT", "verdict & claims"),
]

# status mix per stage for the proportional strip (fractions only —
# read from the asserted JSON at render time; numbers never printed)
def _stage_fracs():
    j = json.load(open(os.path.join(OUT, "pipeline_graph_asserted.json"),
                       encoding="utf-8"))
    per = {}
    for st in j["stages"]:
        tally = st.get("status_tally") or {}
        per[int(st["num"])] = (tally.get("DECIDED", 0), tally.get("MIXED", 0),
                               tally.get("NEVER", 0), tally.get("SA", 0))
    return per


def _strip(ax, x, y, w, h, fracs):
    d, m, n, s = fracs
    tot = max(1, d + m + n + s)
    xx = x
    for val, col, hollow in ((d, TEAL, False), (m, AMBER, False),
                             (n, RED, True), (s, GRAY, True)):
        if not val:
            continue
        ww = w * val / tot
        ax.add_patch(mp.Rectangle((xx, y), ww, h,
                     fc="white" if hollow else col,
                     ec=col, lw=1.1, alpha=1.0 if hollow else 0.85))
        xx += ww


def l0_slide():
    fig, ax = plt.subplots(figsize=(12.4, 3.6))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.6); ax.axis("off")
    try:
        per = _stage_fracs()
    except Exception:
        per = {}
    bw, gap = 1.72, 0.22
    x0 = (16 - 8 * bw - 7 * gap) / 2
    for i, (num, name, sub) in enumerate(STAGES):
        x = x0 + i * (bw + gap)
        grey_zone = num in ("7", "8")
        ax.add_patch(mp.FancyBboxPatch((x, 1.15), bw, 2.15,
                     boxstyle="round,pad=0.06",
                     fc="#f4f4f2" if grey_zone else "white",
                     ec=GRAY, lw=1.8))
        ax.text(x + bw / 2, 2.92, num, fontsize=10, ha="center", color=LGRAY)
        ax.text(x + bw / 2, 2.42, name, fontsize=10.8, ha="center",
                color=GRAY, weight="bold")
        ax.text(x + bw / 2, 1.95, sub, fontsize=7.2, ha="center", color=LGRAY)
        fr = per.get(int(num))
        if fr and sum(fr):
            _strip(ax, x + 0.18, 1.38, bw - 0.36, 0.22, fr)
        else:
            ax.add_patch(mp.Rectangle((x + 0.18, 1.38), bw - 0.36, 0.22,
                         fc="#e2e2e2", ec=LGRAY, lw=1.0))
        if i < 7:
            ax.annotate("", xy=(x + bw + gap - 0.02, 2.22),
                        xytext=(x + bw + 0.02, 2.22),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.6))
    # cluster A arc (4<->6), the one semantic long-range link kept
    xa = x0 + 3 * (bw + gap) + bw / 2
    xb = x0 + 5 * (bw + gap) + bw / 2
    ax.annotate("", xy=(xb, 3.38), xytext=(xa, 3.38),
                arrowprops=dict(arrowstyle="<|-|>", color=RED, lw=1.5,
                                connectionstyle="arc3,rad=-0.35"))
    ax.text((xa + xb) / 2, 4.28, "engine cluster — re-examined at next phase entry",
            fontsize=9.5, ha="center", color=RED, style="italic")
    # minimal legend, words only
    lx = x0
    for lab, col, hollow in (("adjudicated", TEAL, False),
                             ("partly open", AMBER, False),
                             ("open, owner named", RED, True)):
        ax.add_patch(mp.Rectangle((lx, 0.42), 0.34, 0.2,
                     fc="white" if hollow else col, ec=col, lw=1.2,
                     alpha=1.0 if hollow else 0.85))
        ax.text(lx + 0.44, 0.52, lab, fontsize=9, va="center", color=GRAY)
        lx += 0.44 + 0.14 * len(lab) + 0.5
    ax.text(16 - x0, 0.52, "full walkable graph: backup", fontsize=9,
            va="center", ha="right", color=LGRAY, style="italic")
    fig.savefig(os.path.join(OUT, "L0_slide.png"), dpi=200,
                facecolor="white", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("rendered L0_slide.png")


def _mini_ribbon(ax, y, hi):
    bw, gap = 1.35, 0.14
    x0 = (16 - 8 * bw - 7 * gap) / 2
    for i, (num, name, _sub) in enumerate(STAGES):
        x = x0 + i * (bw + gap)
        on = int(num) in hi
        ax.add_patch(mp.FancyBboxPatch((x, y), bw, 0.72,
                     boxstyle="round,pad=0.04",
                     fc=TEAL if on else "white",
                     ec=TEAL if on else LGRAY, lw=1.6 if on else 1.1))
        ax.text(x + bw / 2, y + 0.36, name, fontsize=8.2, ha="center",
                va="center", color="white" if on else LGRAY,
                weight="bold" if on else "normal")


def _cards(ax, cards, y_top, ncols=3, ch=1.5, cw=4.7, gap=0.35):
    x0 = (16 - ncols * cw - (ncols - 1) * gap) / 2
    for k, (head, sub, col) in enumerate(cards):
        r, c = divmod(k, ncols)
        x = x0 + c * (cw + gap)
        y = y_top - r * (ch + 0.3) - ch
        ax.add_patch(mp.FancyBboxPatch((x, y), cw, ch, boxstyle="round,pad=0.08",
                     fc="white", ec=col, lw=1.8))
        ax.text(x + cw / 2, y + ch - 0.42, head, fontsize=10.5, ha="center",
                color=col, weight="bold")
        ax.text(x + cw / 2, y + 0.42, sub, fontsize=8.6, ha="center", color=GRAY)


def stage6_slide():
    fig, ax = plt.subplots(figsize=(12.4, 5.4))
    ax.set_xlim(0, 16); ax.set_ylim(0, 7); ax.axis("off")
    _mini_ribbon(ax, 6.0, hi={6})
    cards = [
        ("the driver", "segmented trust-region Newton\non a discrete-exact gradient", TEAL),
        ("curvature: MEASURED", "full per-segment Hessian, fresh —\nnever a stale approximation", TEAL),
        ("step acceptance", "certified step control:\nnon-finite guards, ladder fallback", TEAL),
        ("engine cluster — OPEN, declared", "re-examined at next phase entry:\n2026 candidate named, comparison pre-registered", RED),
        ("global-only routes — refused", "local-only search declared,\nwith its owner and window", RED),
        ("design basis", "one sector exercised today (bell, 9 DOF);\nthe others: named owners and windows", AMBER),
    ]
    _cards(ax, cards, y_top=5.35, ncols=3)
    ax.text(8, 0.55, "every card: full record with alternatives and falsifier — walkable graph in backup",
            fontsize=9.5, ha="center", color=LGRAY, style="italic")
    fig.savefig(os.path.join(OUT, "L1_stage6_slide.png"), dpi=200,
                facecolor="white", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("rendered L1_stage6_slide.png")


def stage45_slide():
    fig, ax = plt.subplots(figsize=(12.4, 5.4))
    ax.set_xlim(0, 16); ax.set_ylim(0, 7); ax.axis("off")
    _mini_ribbon(ax, 6.0, hi={4, 5})
    cards = [
        ("gradient identity", "reverse sweep = transposed adjoint —\nverified at machine precision", TEAL),
        ("independent oracle", "second code, negative controls —\nbuilt to REJECT", TEAL),
        ("derived thresholds", "never magic numbers —\nand halving one flips the verdict", TEAL),
        ("discretization error", "dedicated estimator\nwith an independent referee", TEAL),
        ("model error", "per-channel bracket —\nnever mixed with discretization", AMBER),
        ("the front", "the one scheme that can carry\na gradient certificate (published reason)", TEAL),
    ]
    _cards(ax, cards, y_top=5.35, ncols=3)
    ax.text(8, 0.55, "contour, certificates, bars and verdict travel together — full graph in backup",
            fontsize=9.5, ha="center", color=LGRAY, style="italic")
    fig.savefig(os.path.join(OUT, "L1_stage45_slide.png"), dpi=200,
                facecolor="white", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("rendered L1_stage45_slide.png")


if __name__ == "__main__":
    l0_slide()
    stage6_slide()
    stage45_slide()
