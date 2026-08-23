#!/usr/bin/env python3
"""L0 overview render prototype (de-risk of LAYOUT, not beauty).

[S-PRES W-A slot A6] Consumes pipeline_graph.json (extract_graph.py,
asserted against the map). Implements GRAPH_VIZ_SPEC.md L0:
8-stage left-to-right ribbon, per-stage node count + stacked status
mini-bar (DECIDED green / MIXED amber / NEVER open grey / SA outlined
violet), the 4 cluster surfaces as labeled arcs over the ribbon,
takeaway line. Target frame: 1920x1080 (13.333x7.5 in at 144 dpi).

De-risk instrumentation: stage-name font size auto-shrinks to fit the
box and the script PRINTS which stages fall below the 20 pt spec
floor (comms-refuter check L0) -- that printout is the measurement,
not a failure of the build.

matplotlib is already in the pinned env (3.10.8, verified; NOTHING
installed).
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

HERE = Path(__file__).resolve().parent
G = json.loads((HERE / "pipeline_graph.json").read_text(encoding="utf-8"))
OUT = HERE / "render_L0_prototype.png"

FIG_W, FIG_H, DPI = 13.333, 7.5, 144  # -> 1920x1080
SPEC_MIN_NAME_PT = 20.0               # comms-refuter L0 floor

COL = {
    "DECIDED": dict(fc="#1b7f3b", ec="#1b7f3b"),
    "MIXED": dict(fc="#e6a817", ec="#b3820f"),
    "NEVER": dict(fc="#ffffff", ec="#8a8a8a"),
    "SA": dict(fc="#ffffff", ec="#7b3fbf"),
}
STATUS_ORDER = ["DECIDED", "MIXED", "NEVER", "SA"]

# ribbon geometry (inches = data units)
X0, X1 = 0.35, FIG_W - 0.35
GAP = 0.18
BOX_W = (X1 - X0 - 7 * GAP) / 8
BOX_Y, BOX_H = 3.05, 2.25
CHAR_W_FRAC = 0.74  # avg BOLD glyph width as fraction of font size
                    # (calibrated on the first render: 0.60 under-measured
                    # DejaVu Sans Bold -> names bled out of the boxes)


def wrap_to_fit(name, box_w_in, start_pt=SPEC_MIN_NAME_PT, min_pt=9.0):
    """Greedy word-wrap; shrink font until the widest line fits.
    Returns (lines, pt). Measurement heuristic, good enough for de-risk."""
    words = name.split()
    pt = start_pt
    while pt >= min_pt:
        # max chars per line at this pt: box_w_in / (pt/72 * CHAR_W_FRAC)
        max_chars = max(1, int(box_w_in / (pt / 72.0 * CHAR_W_FRAC)))
        lines, cur = [], ""
        ok = True
        for w in words:
            cand = (cur + " " + w).strip()
            if len(cand) <= max_chars:
                cur = cand
            else:
                if cur:
                    lines.append(cur)
                cur = w
                if len(w) > max_chars:
                    ok = False  # single word overflows
        lines.append(cur)
        if ok and len(lines) <= 3:
            return lines, pt
        pt -= 1.0
    return [name], min_pt


def main():
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    ax.text(FIG_W / 2, 7.12,
            "PIPELINE DECISION MAP - L0 OVERVIEW (8 stages, 62+17 nodes, "
            "45 edges of record)",
            ha="center", va="center", fontsize=17, fontweight="bold")
    ax.text(FIG_W / 2, 6.78,
            "source: docs/rde_nozzle_pipeline_decision_map.md (refereed; "
            "counts asserted by extract_graph.py)",
            ha="center", va="center", fontsize=9.5, color="#555555")

    shrunk = []
    centers = []
    for i, st in enumerate(G["stages"]):
        x = X0 + i * (BOX_W + GAP)
        cx = x + BOX_W / 2
        centers.append(cx)
        ax.add_patch(FancyBboxPatch(
            (x, BOX_Y), BOX_W, BOX_H,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            fc="#f4f6f8", ec="#33475b", lw=1.6))
        ax.text(cx, BOX_Y + BOX_H - 0.22, "STAGE %d" % st["num"],
                ha="center", va="center", fontsize=11, color="#33475b",
                fontweight="bold")
        lines, pt = wrap_to_fit(st["name"], BOX_W - 0.12)
        if pt < SPEC_MIN_NAME_PT:
            shrunk.append((st["num"], st["name"], pt))
        ax.text(cx, BOX_Y + BOX_H - 0.72, "\n".join(lines),
                ha="center", va="center", fontsize=pt, fontweight="bold",
                linespacing=1.0)
        n_led = len(st["ledger_ids"])
        n_nl = len(st["nonledger_ids"])
        cnt = "%d scelte" % n_led if n_led else ""
        if n_nl:
            cnt += (" + " if cnt else "") + "%d ⊘" % n_nl
        if st["secondary_faces"]:
            cnt += "  (+%s)" % ",".join(st["secondary_faces"])
        ax.text(cx, BOX_Y + 0.62, cnt, ha="center", va="center",
                fontsize=9.5, color="#333333")
        # stacked status mini-bar (ledger nodes only)
        bar_x, bar_w, bar_y, bar_h = x + 0.10, BOX_W - 0.20, BOX_Y + 0.16, 0.26
        tot = max(1, n_led)
        xx = bar_x
        for key in STATUS_ORDER:
            k = st["status_tally"][key]
            if not k:
                continue
            w = bar_w * k / tot
            ax.add_patch(Rectangle((xx, bar_y), w, bar_h, lw=1.2, **COL[key]))
            ax.text(xx + w / 2, bar_y + bar_h / 2, str(k), ha="center",
                    va="center", fontsize=7.5,
                    color="white" if key == "DECIDED" else "#333333")
            xx += w
        if n_led == 0:
            ax.text(bar_x + bar_w / 2, bar_y + bar_h / 2, "⊘ only",
                    ha="center", va="center", fontsize=7.5, color="#8a8a8a")
        if i < 7:  # ribbon arrows
            ax.add_patch(FancyArrowPatch(
                (x + BOX_W + 0.01, BOX_Y + BOX_H / 2),
                (x + BOX_W + GAP - 0.01, BOX_Y + BOX_H / 2),
                arrowstyle="-|>", mutation_scale=16, color="#33475b", lw=1.6))

    # ---- the 4 cluster surfaces as labeled arcs OVER the ribbon ----------
    surf_geom = {   # surface letter -> (stage span, arc apex height, label)
        "A": ((4, 6), 1.15, "A  ENGINE cluster (C31/C57/C58/C60/[P-IPADJ]/"
                            "SDP-CAND-8)"),
        "B": ((1, 1), 0.52, "B  CONTRACT (C52/C53/C54 +C50)"),
        "C": ((7, 7), 0.52, "C  SHIP-GATE (OBJ-DOM ↔ DELTA-CARRIER)"),
        "D": ((8, 8), 0.86, "D  EXT. EXPANSION (Veen→C61→ADR-D4)"),
    }
    top = BOX_Y + BOX_H
    for letter, ((s0, s1), h, label) in surf_geom.items():
        xa, xb = centers[s0 - 1], centers[s1 - 1]
        if s0 == s1:
            xa, xb = xa - BOX_W * 0.38, xb + BOX_W * 0.38
        ax.add_patch(FancyArrowPatch(
            (xa, top + 0.05), (xb, top + 0.05),
            connectionstyle="arc3,rad=%.3f" % (-h / max(0.6, (xb - xa))),
            arrowstyle="-", lw=2.0, color="#b5443c", linestyle="-",
            shrinkA=0, shrinkB=0))
        lx_mid = (xa + xb) / 2
        ha = "center"
        if lx_mid < 1.8:            # keep labels inside the frame
            lx_mid, ha = 0.15, "left"
        elif lx_mid > FIG_W - 1.8:
            lx_mid, ha = FIG_W - 0.15, "right"
        ax.text(lx_mid, top + h * 0.62 + 0.12, label, ha=ha,
                va="bottom", fontsize=8.5, color="#b5443c")

    # ---- legend (slide 1 carries it; later slides must not need it) ------
    lx, ly = 0.45, 2.55
    items = [("DECIDED", "square"), ("MIXED", "square"),
             ("NEVER", "circle"), ("SA", "diamond")]
    labels = {"DECIDED": "DECIDED (12)", "MIXED": "MIXED (36)",
              "NEVER": "NEVER (12, owner-tagged)",
              "SA": "SINGLE-AUTHOR (2: C17 C18)"}
    for key, shape in items:
        c = COL[key]
        if shape == "square":
            ax.add_patch(Rectangle((lx, ly - 0.07), 0.14, 0.14, lw=1.4, **c))
        elif shape == "circle":
            ax.add_patch(plt.Circle((lx + 0.07, ly), 0.07, lw=1.4, **c))
        else:
            ax.add_patch(plt.Polygon(
                [(lx + 0.07, ly - 0.09), (lx + 0.16, ly),
                 (lx + 0.07, ly + 0.09), (lx - 0.02, ly)], lw=1.4,
                closed=True, **c))
        ax.text(lx + 0.24, ly, labels[key], ha="left", va="center",
                fontsize=9.5)
        lx += 0.44 + 0.082 * len(labels[key])
    ax.text(0.45, ly - 0.42,
            "⊘ = non-ledger node (status verbatim from source)   |   "
            "C46 (DECIDED) not stage-placed by the map (note_C46)   |   "
            "anti-edge E34 (C6 ⊥ C42) recorded, not an omission",
            ha="left", va="center", fontsize=8.5, color="#555555")

    # ---- takeaway line (verbatim, spec L0) -------------------------------
    ax.text(FIG_W / 2, 1.05,
            '"62 scelte, ognuna a registro con alternative + falsificatore;\n'
            '12 DECIDED / 36 MIXED / 12 NEVER / 2 SINGLE-AUTHOR '
            '- dichiarate, non nascoste."',
            ha="center", va="center", fontsize=15, style="italic",
            color="#222222")

    fig.savefig(OUT, dpi=DPI, facecolor="white")
    print("WROTE: %s (%dx%d px)" % (OUT, FIG_W * DPI, FIG_H * DPI))
    if shrunk:
        print("LAYOUT MEASUREMENT - stage names BELOW the 20 pt spec floor:")
        for num, name, pt in shrunk:
            print("  Stage %d %-28s fitted at %.0f pt" % (num, name, pt))
    else:
        print("LAYOUT MEASUREMENT: all stage names fit at >= 20 pt")


if __name__ == "__main__":
    main()
