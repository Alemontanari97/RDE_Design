#!/usr/bin/env python3
"""S-PRES session 3 — deck graph renders (L0 ribbon + L1 stage zooms).

[S-PRES/deck authoring] Consumption arc: build_deck_spres.py slides
C13 (L0), C14 (Stage-6 panels a/b/c), C15 (Stages 4-5), backup D1-D8
(all-stage L1 zooms) + Block-2 retro-audit.
Comparison stage: graph_derisk/DERISK_report.md sections 3-5 (record
constraints) + GRAPH_VIZ_SPEC.md.

ASSERT-GATED, NEVER HAND-TYPED: this script imports the de-risk
extractor (graph_derisk/extract_graph.py, unmodified) via importlib,
re-runs it against docs/rde_nozzle_pipeline_decision_map.md, and lets
its 18 asserts gate every render — a failed assert aborts the build.
The extracted JSON is written into deck_build/graph/ (the de-risk
directory is treated as read-only).

Record constraints implemented (DERISK section 4 + section 3 + spec):
  P1  short uppercase display names >= 20 pt (proportional-width boxes,
      Cambria serif measured with the Agg renderer at build time —
      the script FAILS if any name falls below 20 pt).
  P2  Stage 7 (zero ledger nodes) -> neutral grey bar + circled-slash
      count badge.
  P3  arc reserved for cluster A (4<->6); B/C/D as tinted halos with
      labels, D's label kept inside the frame.
  P4  dual-face nodes C55 (St.1+7) / R22-CFD (St.2+8) as a compact
      chain glyph, never long inline text; per-stage count line kept
      clear of the box borders; C46 footnote verbatim.
  3.1 Stage 6 (24 measured ledger nodes) -> 3 panels, <= 12 cards each.
  5   E9/E28/E29 long-range edges carried by L1 stub-arrows labeled
      with the target stage number.
Status encoding, color AND fill/shape (colorblind-safe):
  DECIDED filled teal square / MIXED half-filled amber square /
  NEVER open box with red border (+ owner-window tag on cards) /
  SINGLE-AUTHOR outlined diamond.  Palette: #822433 / #006778 / greys
  (+ amber reserved for MIXED per the record constraint).

Env: PINNED (matplotlib 3.10.8 already present; nothing installed).
"""

import importlib.util
import json
import math
import re
import sys
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, \
    Polygon, Rectangle

BUILD = Path(__file__).resolve().parent
DERISK = BUILD.parent / "graph_derisk"
GRAPH_DIR = BUILD / "graph"
GRAPH_DIR.mkdir(exist_ok=True)

FIG_W, FIG_H, DPI = 13.333, 7.5, 144          # -> 1920 x 1080 px
RED, TEAL = "#822433", "#006778"
AMBER, AMBER_EC = "#DFA524", "#8a6510"
INK, GREY, MGREY, LGREY = "#2b2b2b", "#6c6c6c", "#9a9a9a", "#e8e6e2"
CARD_BG, CARD_EC = "#f8f7f4", "#4a4a4a"
EDGE_C = "#8f8f8f"

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Cambria", "Constantia", "Times New Roman",
                              "DejaVu Serif"]
# NOTE: the circled-slash glyph (U+2298) resolves through the DejaVu
# fallback in REGULAR weight only — never set it in bold text.
NL = "⊘"          # circled slash (non-ledger marker)
PERP = "⊥"        # anti-edge glyph

DISPLAY = {1: "CONTRACT", 2: "REPRESENT", 3: "MARCH", 4: "CERTIFY",
           5: "ESTIMATE", 6: "OPTIMIZE", 7: "AGGREGATE", 8: "VERDICT"}

# --- Stage-6 panel split (DERISK section 3.1: 24 measured ids, 3 panels,
#     never more than 12 cards; membership re-checked against the JSON) --
PANEL_A = ["C31", "C57", "C58", "C60", "C48", "C16", "C32", "C33", "C37"]
PANEL_B = ["C34", "C35", "C36", "C39", "C40", "C27", "C29", "C30", "C62"]
PANEL_C = ["C1", "C2", "C3", "C4", "C7", "C8"]

# Stages 4-5 main-deck selection (certification + estimate core cards)
SEL_S4 = ["C17", "C18", "C19", "C20", "C38", "C47"]
SEL_S5 = ["C9", "C11", "C42", "C43", "C56", "M-RED"]

# --- short display titles (<= 6 words, compressed from the JSON choice
#     field — authoring compression, cite-only; ids/statuses stay
#     extracted). Anything not listed falls back to auto-compression. --
SHORT = {
    "C31": "scipy trust-constr; segmented TR-Newton driver",
    "C57": "local-only: continuation + warm starts",
    "C58": "JAX primary per G0 decision",
    "C60": "NAND reduced-space, never weighed",
    "C48": "sequential per-segment FD, nonfinite-lane guard",
    "C16": "step ladder, bare argmin non-increase",
    "C32": "fresh full FD Hessian per segment",
    "C33": "scipy default BFGS, no hess=",
    "C34": "TR_FLOOR 1e-3, tr0 0.05, cap 0.25",
    "C35": "literal 1e-10 at every call site",
    "C36": "Jacobi Dv once per walk, objective-only",
    "C37": "any (N,Nv) flip ends segment",
    "C39": "res.v raw; convention closed S24-T1",
    "C40": "LinearConstraint row, adjudicated-conditional",
    "C27": "KS-min, rho = K_RICH ln(N)/mu0",
    "C29": "rung-frozen + C3 drift gate",
    "C30": "overlap crop + occurrence counter",
    "C62": "uniform trapezoid, incumbent-declared",
    "C1": "cubic heights-as-dofs; B-spline direction",
    "C2": "natural y''(L)=0, adjudicated-conditional",
    "C3": "clamped tan(thB), constructional",
    "C4": "uniform xi + goal-indicator insertion",
    "C7": "insertion-only ratchet; insert+remove direction",
    "C8": "print-only dev_warm to armed rejector",
    "C17": "30 (rung count)",
    "C18": "NEWTON_TOL_FACTOR=100, C_FLOOR=8",
    "C19": "scalar sc = max(1, max|z|)",
    "C20": "unqualified one-extra-step ratio",
    "C21": "asserted O(h) predictor, stale seeds",
    "C23": "full record then P4 gate",
    "C28": "binary outside gates only",
    "C38": "ratchet exhaustion, raw KKT-open number",
    "C47": "frozen baseline ratchet + multiset fingerprint",
    "C9": "goal-oriented adapted placement = TARGET",
    "C10": "refine(r) joint global scaling",
    "C11": "DWR primary; Richardson/GCI referee",
    "C41": "K=4 pointwise two-level",
    "C42": "one numeral, 8 roles",
    "C43": "presumed h^p; premise retired",
    "C44": "fixed sqrt(eps), eps^(1/3) FD scales",
    "C56": "discrete AD-adjoint everywhere; roles closed",
    "C50": "no contract-site metric; Form-2 adjudicated",
    "C52": "subsonic patches = declared case-class",
    "C53": "Gamma_d fixed per case, no trade",
    "C54": "I4 kept bare; Jensen counterexample",
    "C55": "single-point default P_amb = {Pa0}",
    "C49": "fitted-front characteristic marching, S1 class",
    "C51": "implicit BVP: freezing + Newton-Krylov",
    "C59": "cycle-average, canonical inside the pin",
    "C12": "Sauer first-order, gamma const, mirrored",
    "C13": "GENO foot-ratio guard v1/y1",
    "C14": "axis-cell Me only, adjudicated-converged",
    "C22": "linear index scan, full Newton",
    "C15": "1e-5 GENO-mirrored (S19 knob)",
    "C45": "hardcoded 400-point grid [1.01, 2.8]",
    "C24": "quintic C1 tables (backend-1)",
    "C25": "literals 1050/3900 K, N_TAB=8192",
    "C26": "silent clamp / quintic extrapolation",
    "C5": "normalized xi re-anchored to live xB",
    "C6": "dx_loc = median station spacing",
    "C61": "Veen 0.846p/M^1.3, legacy chain only",
    "PIN-WAVE": "pure periodic rotating wave pin",
    "CONTRACT-F1..F10-block": "product-ball acceptance, phase-aligned "
                              "fields",
    "S-5F": "five-field optimality system [S-5F]",
    "ROUTE-B": "deferred deriver: helical sheets native",
    "R22-CFD": "re-scoped CFD-1/CFD-2 irreducible core",
    "CLG": "CLG-D1..D7 landed, chain floor law",
    "SDP-CAND-8": "SOTA-survey candidate, no ledger row",
    "M-RED": "O5-lite legs (A)-(E), bands B-1..B-4",
    "R22F-FORCHETTA": "per-channel BEST/WORST bracket, 2D-vs-3D gap",
    "T-DISC": "p-only reduction convicted; theorems landed",
    "OBJ-DOM": "fix-A objective-of-record at F2 entry",
    "DELTA-CARRIER": "delta-carrier theorems DC-1..DC-4 landed",
    "OPTSHIFT": "argmax-shift bound, schema-licensed only",
    "D-44": "public adequacy claims gated",
    "P34": "staged evidence: verify, validate, predict",
    "H20": "plug/E-D sectors need shape-adjoint solve",
    "DUTY-10": "lit-born duty, plan-slotted (Veen row)",
}

TOKEN_LABEL = {"findings": "findings", "plan": "plan D6",
               "S-PRES": "deck", "uniformity fork": "unif. fork",
               "forchetta": "St.7", "Stage-7": "St.7", "NTF-4": "NTF-4",
               "NTF-block": "NTF", "vander_veen_1974": "Veen-1974",
               "ADR-D4": "ADR-D4", "[P-IPADJ]": "[P-IPADJ]",
               "R8": "Veen/R8", "Veen": "Veen/R8"}
ALIAS = {"forchetta": "R22F-FORCHETTA"}


# ---------------------------------------------------------------------------
# 1. assert-gated graph load (extractor imported, never modified)
# ---------------------------------------------------------------------------
def load_asserted_graph():
    src = DERISK / "extract_graph.py"
    spec = importlib.util.spec_from_file_location("extract_graph", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.OUT_PATH = GRAPH_DIR / "pipeline_graph_asserted.json"  # keep the
    # de-risk directory read-only: the re-extracted JSON lands in BUILD.
    rc = mod.main()                     # runs the 18 asserts; raises on fail
    if rc != 0:
        raise AssertionError("extract_graph.main() returned %r" % rc)
    G = json.loads(mod.OUT_PATH.read_text(encoding="utf-8"))
    checks = G["asserts"]
    if len(checks) != 18 or not all(c["pass"] for c in checks):
        raise AssertionError(
            "assert gate: %d/%d PASS — render refused"
            % (sum(1 for c in checks if c["pass"]), len(checks)))
    return G, checks


# ---------------------------------------------------------------------------
# 2. shared helpers
# ---------------------------------------------------------------------------
def short_title(node):
    if node["id"] in SHORT:
        return SHORT[node["id"]]
    t = re.sub(r"`[^`]*`", "", node["choice"]).replace("\\|", "|")
    t = re.split(r"[;(]| — ", t)[0].strip().rstrip(",.")
    words = t.split()
    return " ".join(words[:6]) + ("…" if len(words) > 6 else "")


def owner_tag(node):
    t = node.get("open_duty") or node.get("conditions") or ""
    t = re.sub(r"`[^`]*`", "", t)
    t = re.split(r"[(,;:]", t)[0].strip()
    return " ".join(t.split()[:5])


def draw_glyph(ax, cx, cy, status, s=0.085, lw=1.5):
    """Status glyph: color AND fill/shape channel (colorblind-safe)."""
    if status == "DECIDED":
        ax.add_patch(Rectangle((cx - s, cy - s), 2 * s, 2 * s,
                               fc=TEAL, ec=TEAL, lw=lw, zorder=6))
    elif status == "MIXED":
        ax.add_patch(Rectangle((cx - s, cy - s), 2 * s, 2 * s,
                               fc="white", ec=AMBER_EC, lw=lw, zorder=6))
        ax.add_patch(Rectangle((cx - s, cy - s), 2 * s, s,
                               fc=AMBER, ec="none", zorder=6))
    elif status == "NEVER":
        ax.add_patch(Rectangle((cx - s, cy - s), 2 * s, 2 * s,
                               fc="white", ec=RED, lw=lw + 0.3, zorder=6))
    elif status == "SA":
        ax.add_patch(Polygon([(cx, cy - 1.25 * s), (cx + 1.25 * s, cy),
                              (cx, cy + 1.25 * s), (cx - 1.25 * s, cy)],
                             closed=True, fc="white", ec="#555555",
                             lw=lw, zorder=6))
    else:                                   # non-ledger: circled slash
        ax.text(cx, cy, NL, ha="center", va="center", fontsize=13,
                color=GREY, zorder=6, family="DejaVu Serif")


def chain_glyph(ax, x, y, r=0.042, color=INK):
    ax.add_patch(Circle((x, y), r, fc="none", ec=color, lw=1.3, zorder=6))
    ax.add_patch(Circle((x + 1.35 * r, y), r, fc="none", ec=color, lw=1.3,
                        zorder=6))


def new_fig(title, subtitle=None):
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.text(0.35, 7.16, title, ha="left", va="center", fontsize=13,
            fontweight="bold", color=INK)
    if subtitle:
        ax.text(FIG_W - 0.35, 7.16, subtitle, ha="right", va="center",
                fontsize=9, color=GREY)
    return fig, ax


def footer(ax, extra=None):
    ax.text(FIG_W - 0.35, 0.18,
            "source: docs/rde_nozzle_pipeline_decision_map.md — extracted "
            "+ 18 asserts", ha="right", va="center", fontsize=7.2,
            color=MGREY)
    if extra:
        ax.text(0.35, 0.18, extra, ha="left", va="center", fontsize=7.5,
                color=GREY)


def glyph_legend(ax, x=0.35, y=0.45, fs=8.2, tallies=None):
    items = [("DECIDED", "DECIDED"), ("MIXED", "MIXED (half-fill)"),
             ("NEVER", "NEVER (open, owner-tagged)"),
             ("SA", "SINGLE-AUTHOR")]
    for key, lab in items:
        if tallies:
            lab = "%s %d" % (lab, tallies[key])
        draw_glyph(ax, x + 0.07, y, key, s=0.062)
        ax.text(x + 0.21, y, lab, ha="left", va="center", fontsize=fs,
                color=INK)
        x += 0.36 + 0.058 * len(lab)
    ax.text(x + 0.05, y, NL + " = non-ledger (status verbatim)",
            ha="left", va="center", fontsize=fs, color=GREY)


# ---------------------------------------------------------------------------
# 3. L0 ribbon
# ---------------------------------------------------------------------------
def render_L0(G):
    fig, ax = new_fig(
        "Design pipeline — L0 overview",
        "8 stages · 62 + 17 nodes · 45 edges of record")
    r = fig.canvas.get_renderer()

    # proportional box widths so every display name sits at >= 20 pt
    M, GAP = 0.30, 0.13
    NAME_PT = 20.0
    widths = []
    for i in range(8):
        t = ax.text(0, 0, DISPLAY[i + 1], fontsize=NAME_PT,
                    fontweight="bold")
        widths.append(t.get_window_extent(renderer=r).width / DPI)
        t.remove()
    total_box = FIG_W - 2 * M - 7 * GAP
    pad = (total_box - sum(widths)) / 8.0
    if pad < 0.10:
        raise AssertionError(
            "P1 regression: %.2f in padding/box at %.0f pt — name floor "
            "not met" % (pad, NAME_PT))

    BOX_Y, BOX_H = 3.55, 2.2
    top = BOX_Y + BOX_H
    boxes = {}
    x = M
    for i, st in enumerate(G["stages"]):
        w = widths[i] + pad
        boxes[st["num"]] = (x, w)
        x += w + GAP

    # cluster halos B / C / D (single-stage: tint + label, NO arc — P3)
    halos = {"B": (1, TEAL, 0.07), "C": (7, "#666666", 0.10),
             "D": (8, RED, 0.07)}
    surf_title = {s["surface"]: s for s in G["surfaces"]}
    halo_lab = {
        "B": ("B · CONTRACT", "C52·C53·C54 (+C50)"),
        "C": ("C · SHIP-GATE", "OBJ-DOM " + "↔" + " DELTA-CARRIER"),
        "D": ("D · EXT. EXPANSION", "Veen" + "→" + "C61" + "→"
              + "ADR-D4"),
    }
    for letter, (snum, col, alpha) in halos.items():
        bx, bw = boxes[snum]
        ax.add_patch(FancyBboxPatch(
            (bx - 0.06, BOX_Y - 0.78), bw + 0.12, BOX_H + 0.92,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            fc=col, ec="none", alpha=alpha, zorder=0.4))
        cx = bx + bw / 2
        l1, l2 = halo_lab[letter]
        ha, lx = "center", cx
        if letter == "D":                       # clamp inside the frame
            ha, lx = "right", FIG_W - 0.14
        ax.text(lx, BOX_Y - 0.47, l1, ha=ha, va="center", fontsize=8.2,
                color=col if letter != "C" else "#555555",
                fontweight="bold", zorder=5)
        ax.text(lx, BOX_Y - 0.66, l2, ha=ha, va="center", fontsize=7.2,
                color=col if letter != "C" else "#555555", zorder=5)

    # cluster A arc (the only arc — spans stages 4..6)
    xa = boxes[4][0] + boxes[4][1] / 2
    xb = boxes[6][0] + boxes[6][1] / 2
    ax.add_patch(FancyArrowPatch(
        (xa, top + 0.06), (xb, top + 0.06),
        connectionstyle="arc3,rad=-0.30", arrowstyle="-", lw=2.2,
        color=RED, shrinkA=0, shrinkB=0, zorder=3))
    for xe in (xa, xb):
        ax.add_patch(Circle((xe, top + 0.06), 0.035, fc=RED, ec=RED,
                            zorder=4))
    ax.text((xa + xb) / 2, top + 0.60,
            "A · ENGINE cluster:  C31 · C57 · C58 · C60 · [P-IPADJ] · "
            "SDP-CAND-8", ha="center", va="center", fontsize=8.6,
            color=RED, fontweight="bold", zorder=4)

    # stage boxes
    for st in G["stages"]:
        num = st["num"]
        bx, bw = boxes[num]
        cx = bx + bw / 2
        ax.add_patch(FancyBboxPatch(
            (bx, BOX_Y), bw, BOX_H,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            fc="#f4f4f2", ec="#3a3a3a", lw=1.5, zorder=2))
        ax.text(cx, top - 0.22, "STAGE %d" % num, ha="center", va="center",
                fontsize=9.5, color=GREY, fontweight="bold", zorder=5)
        ax.text(cx, top - 0.60, DISPLAY[num], ha="center", va="center",
                fontsize=NAME_PT, fontweight="bold", color=INK, zorder=5)
        sub = textwrap.fill(st["name"].title(), 16)
        ax.text(cx, top - 1.02, sub, ha="center", va="center", fontsize=7.4,
                color=GREY, zorder=5, linespacing=1.05)

        # dual-face chain badge (compact glyph, never long inline text)
        for fid, faces in (("C55", "1+7"), ("R22-CFD", "2+8")):
            fnode = next(n for n in G["nodes"] if n["id"] == fid)
            if num in fnode["stage_faces"]:
                chain_glyph(ax, cx - 0.52, BOX_Y + 0.80)
                ax.text(cx - 0.36, BOX_Y + 0.80,
                        "%s · St.%s" % (fid, faces), ha="left",
                        va="center", fontsize=6.8, color=INK, zorder=5)

        # status mini-bar (color AND fill coding; P2 for stage 7)
        bar_x, bar_w = bx + 0.10, bw - 0.20
        bar_y, bar_h = BOX_Y + 0.42, 0.26
        n_led = len(st["ledger_ids"])
        if n_led == 0:
            ax.add_patch(Rectangle((bar_x, bar_y), bar_w, bar_h,
                                   fc="#dedede", ec="#9a9a9a", lw=1.1,
                                   zorder=5))
            ax.text(bar_x + bar_w / 2, bar_y + bar_h / 2,
                    NL + " %d" % len(st["nonledger_ids"]), ha="center",
                    va="center", fontsize=8.5, color="#555555", zorder=6)
        else:
            xx = bar_x
            for key in ("DECIDED", "MIXED", "NEVER", "SA"):
                k = st["status_tally"][key]
                if not k:
                    continue
                w = bar_w * k / n_led
                if key == "DECIDED":
                    ax.add_patch(Rectangle((xx, bar_y), w, bar_h, fc=TEAL,
                                           ec=TEAL, lw=1.0, zorder=5))
                    ax.text(xx + w / 2, bar_y + bar_h / 2, str(k),
                            ha="center", va="center", fontsize=7.5,
                            color="white", zorder=6)
                elif key == "MIXED":
                    ax.add_patch(Rectangle((xx, bar_y), w, bar_h,
                                           fc="white", ec=AMBER_EC, lw=1.0,
                                           zorder=5))
                    ax.add_patch(Rectangle((xx, bar_y), w, bar_h / 2,
                                           fc=AMBER, ec="none", zorder=5))
                    ax.text(xx + w / 2, bar_y + bar_h / 2, str(k),
                            ha="center", va="center", fontsize=7.5,
                            color=INK, zorder=6)
                elif key == "NEVER":
                    ax.add_patch(Rectangle((xx, bar_y), w, bar_h,
                                           fc="white", ec=RED, lw=1.4,
                                           zorder=5))
                    ax.text(xx + w / 2, bar_y + bar_h / 2, str(k),
                            ha="center", va="center", fontsize=7.5,
                            color=RED, zorder=6)
                else:                                     # SA: diamond
                    ax.add_patch(Rectangle((xx, bar_y), w, bar_h,
                                           fc="white", ec="#777777",
                                           lw=1.0, zorder=5))
                    dy = bar_y + bar_h / 2
                    ax.add_patch(Polygon(
                        [(xx + 0.07, dy - 0.075), (xx + 0.135, dy),
                         (xx + 0.07, dy + 0.075), (xx + 0.005, dy)],
                        closed=True, fc="white", ec="#555555", lw=1.2,
                        zorder=6))
                    ax.text(xx + w - 0.055, dy, str(k), ha="center",
                            va="center", fontsize=7.5, color="#555555",
                            zorder=6)
                xx += w

        # per-stage count line BELOW the box, clear of the border
        n_nl = len(st["nonledger_ids"])
        cnt = ("%d choices" % n_led) if n_led else ""
        if n_nl:
            cnt += (" + " if cnt else "") + "%d %s" % (n_nl, NL)
        ax.text(cx, BOX_Y - 0.20, cnt, ha="center", va="center",
                fontsize=9.2, color=INK, zorder=5)

        # inter-stage arrow
        if num < 8:
            gx = bx + bw
            ax.add_patch(FancyArrowPatch(
                (gx + 0.015, BOX_Y + BOX_H / 2),
                (gx + GAP - 0.015, BOX_Y + BOX_H / 2),
                arrowstyle="-|>", mutation_scale=13, color="#3a3a3a",
                lw=1.5, zorder=2))

    # legend with the L0 status tallies (graph semantics, allowed here)
    tallies = {"DECIDED": 12, "MIXED": 36, "NEVER": 12, "SA": 2}
    glyph_legend(ax, x=0.38, y=2.42, fs=8.6, tallies=tallies)

    # takeaway (verbatim, spec L0)
    ax.text(FIG_W / 2, 1.50,
            "“62 recorded choices — 48 adjudicated at convergence with "
            "weighed alternatives + a falsifier;\n12 open (owner + "
            "trigger) and 2 single-author — declared, never hidden.”",
            ha="center", va="center", fontsize=13.5, style="italic",
            color=INK, linespacing=1.25)

    # C46 footnote (verbatim record wording) + anti-edge note
    ax.text(FIG_W / 2, 0.62,
            "per-stage sums = 61; C46 is count-bearing, not stage-placed"
            "   ·   anti-edge E34 (C6 " + PERP + " C42) recorded, not an "
            "omission", ha="center", va="center", fontsize=8.2,
            color=GREY)
    footer(ax)
    out = GRAPH_DIR / "L0_ribbon.png"
    fig.savefig(out, dpi=DPI, facecolor="white")
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
# 4. L1 zoom machinery (cards + in-stage edges + labeled stub arrows)
# ---------------------------------------------------------------------------
def build_edge_views(G):
    nodes = {n["id"]: n for n in G["nodes"]}
    ids_desc = sorted(nodes, key=len, reverse=True)
    views = []
    for e in G["edges"]:
        eps = list(e["endpoints"])
        header = e["header"]
        # augment endpoints with node ids the parser left in the header
        for nid in ids_desc:
            if nid in eps:
                continue
            if re.search(r"(?<![\w])" + re.escape(nid) + r"(?!\d)", header):
                eps.append(nid)
        if not [p for p in eps if p in nodes]:      # E29-style: scan text
            for nid in ids_desc:
                if re.search(r"(?<![\w])" + re.escape(nid) + r"(?!\d)",
                             e["text"]) and nid not in eps:
                    eps.append(nid)
        eps = [ALIAS.get(p, p) for p in eps]
        # token endpoints (non-node) from the header
        tmp = header
        for tok in ("vander_veen_1974", "uniformity fork", "NTF-block",
                    "NTF-4", "[P-IPADJ]", "ADR-D4", "findings", "plan",
                    "S-PRES", "Stage-7", "Veen", "R8"):
            if tok in tmp and tok not in eps and ALIAS.get(tok, tok) \
                    not in eps:
                eps.append(tok)
                tmp = tmp.replace(tok, "")
        node_eps = [p for p in eps if p in nodes]
        tok_eps = [p for p in eps if p not in nodes]
        src, dst = [], []
        if "→" in header:
            left = header.split("→")[0]
            # dst = the MAIN clause after the arrow only (a parenthetical
            # like E45's "the C8 leg is already E16" must not mint a leg)
            right_main = header.split("→", 1)[1].split("(")[0]
            for p in eps:
                if p in left or p == "forchetta":
                    src.append(p)
                elif p in right_main:
                    dst.append(p)
        views.append({"id": e["id"], "kind": e["kind"], "header": header,
                      "node_eps": node_eps, "tok_eps": tok_eps,
                      "src": src, "dst": dst,
                      "directed": "→" in header
                      and "↔" not in header})
    return nodes, views


def rect_anchor(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    t = min((w / 2) / abs(dx) if dx else 9e9,
            (h / 2) / abs(dy) if dy else 9e9)
    return cx + dx * t, cy + dy * t


def draw_card(ax, node, x, y, w, h, fs_title=10.0, fs_id=12.0,
              stub_lines=None, small=False):
    is_nl = node["type"] == "nonledger"
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.05",
        fc=CARD_BG, ec=MGREY if is_nl else CARD_EC,
        lw=1.2, linestyle=(0, (4, 2.4)) if is_nl else "solid", zorder=3))
    top = y + h
    idfs = fs_id * (0.85 if small else 1.0)
    ax.text(x + 0.10, top - 0.17, node["id"], ha="left", va="center",
            fontsize=idfs, fontweight="bold", color=INK, zorder=6)
    gx = x + w - 0.16
    if is_nl:
        draw_glyph(ax, gx, top - 0.17, None, s=0.07)
        tag = re.split(r"[(,]", node["status"])[0].strip()
        ax.text(x + 0.10, top - 0.38, tag.upper(), ha="left", va="center",
                fontsize=6.6 if small else 7.4, color=TEAL, zorder=6)
        ty0 = top - 0.56
    else:
        draw_glyph(ax, gx, top - 0.17, node["status"],
                   s=0.062 if small else 0.078)
        ty0 = top - 0.40
    if len(node["stage_faces"]) > 1:
        chain_glyph(ax, x + w - 0.42, top - 0.38, r=0.034)
        ax.text(x + w - 0.30, top - 0.38,
                "St.%s" % "+".join(str(s) for s in node["stage_faces"]),
                ha="left", va="center", fontsize=6.4, color=INK, zorder=6)
    # title
    tfs = fs_title * (0.84 if small else 1.0)
    maxc = max(10, int(w / (tfs / 72.0 * 0.50)))
    lines = textwrap.wrap(short_title(node), maxc)[: 2 if small else 3]
    ax.text(x + 0.10, ty0, "\n".join(lines), ha="left", va="top",
            fontsize=tfs, color=INK, zorder=6, linespacing=1.12)
    # owner-window tag for NEVER (record: the encoding must show the owner)
    yy = y + 0.14
    nstub = len(stub_lines or [])
    if node["status"] == "NEVER" and node["type"] == "ledger":
        tag = owner_tag(node)
        if tag:
            ax.text(x + 0.10, yy + 0.17 * nstub, "owner: " + tag,
                    ha="left", va="center", fontsize=6.2 if small else 7.0,
                    color=RED, style="italic", zorder=6)
    # stub lane(s): text + a small arrow poking out of the card edge
    for k, (txt, anti) in enumerate(stub_lines or []):
        ly = yy + 0.17 * (nstub - 1 - k)
        ax.text(x + 0.10, ly, txt, ha="left", va="center",
                fontsize=6.2 if small else 7.0,
                color=RED if anti else "#4d4d4d", zorder=6)
        ax.add_patch(FancyArrowPatch(
            (x + w - 0.16, ly), (x + w + 0.10, ly),
            arrowstyle="-|>", mutation_scale=7,
            color=RED if anti else EDGE_C, lw=1.0,
            linestyle=(0, (3, 2)) if anti else "solid", zorder=5))
        if anti:
            ax.text(x + w + 0.13, ly, "×", ha="left", va="center",
                    fontsize=8, color=RED, zorder=6)


def stage_label(nodes, p, cur_stages=()):
    if p in nodes:
        st = nodes[p].get("stage")
        if st in cur_stages:
            return p          # same-stage partner: name it, "St.n" is vacuous
        return "St.%d" % st if st else p
    return TOKEN_LABEL.get(p, p)


def compute_edge_plan(nodes, views, shown, cur_stages):
    """Returns (in_lines, stubs): in-panel links + per-card stub texts."""
    in_lines = []                      # (a, b, eid, directed, anti)
    stubs = {}                         # id -> list of (sym, target, eid, anti)
    for v in views:
        node_shown = [p for p in v["node_eps"] if p in shown]
        if not node_shown:
            continue
        ext_nodes = [p for p in v["node_eps"] if p not in shown]
        ext_toks = [t for t in v["tok_eps"]
                    if not (t == "Stage-7" and 7 in cur_stages)]
        anti = v["kind"] == "anti-edge"
        # in-panel links
        if len(node_shown) >= 2 and not anti:
            if v["directed"]:
                s_sh = [p for p in v["src"] if p in shown]
                d_sh = [p for p in v["dst"] if p in shown]
                if s_sh and d_sh:
                    for b in d_sh:
                        in_lines.append((s_sh[0], b, v["id"], True, False))
            else:
                base = node_shown[0]
                for b in node_shown[1:]:
                    in_lines.append((base, b, v["id"], False, False))
        elif len(node_shown) >= 2 and anti:
            in_lines.append((node_shown[0], node_shown[1], v["id"],
                             False, True))
        # stubs toward external endpoints
        if ext_nodes or ext_toks:
            tset = []
            for p in ext_nodes + ext_toks:
                lab = stage_label(nodes, p, cur_stages)
                if lab not in tset:
                    tset.append(lab)
            tgt = "·".join(tset[:3]) + ("…" if len(tset) > 3 else "")
            for sid in node_shown:
                if v["directed"]:
                    sym = "→" if sid in v["src"] else \
                        ("←" if sid in v["dst"] else "↔")
                else:
                    sym = PERP if anti else "↔"
                stubs.setdefault(sid, []).append((sym, tgt, v["id"], anti))
    return in_lines, stubs


def segment_blocked(pa, pb, rects, skip):
    """True if segment pa-pb passes through any card rect not in skip."""
    for key, (x, y, w, h) in rects.items():
        if key in skip:
            continue
        m = 0.04
        for k in range(1, 24):
            t = k / 24.0
            px, py = pa[0] + (pb[0] - pa[0]) * t, pa[1] + (pb[1] - pa[1]) * t
            if x - m < px < x + w + m and y - m < py < y + h + m:
                return True
    return False


def merge_stub_lines(stub_list, max_lines=2):
    """Group stubs by (sym,target); render '-> St.5 (E44·E45)' lines."""
    grouped = {}
    for sym, tgt, eid, anti in stub_list:
        grouped.setdefault((sym, tgt, anti), []).append(eid)
    lines = []
    for (sym, tgt, anti), eids in grouped.items():
        lines.append(("%s %s (%s)" % (sym, tgt, "·".join(eids)), anti))
    if len(lines) <= max_lines:
        return lines
    if max_lines == 1:
        # small cards: one merged line, targets only
        tgts, anti_any = [], False
        for (sym, tgt, anti), _ in grouped.items():
            anti_any = anti_any or anti
            for t in tgt.split("·"):
                if t not in tgts:
                    tgts.append(t)
        extra = "" if len(tgts) <= 3 else " +%d" % (len(tgts) - 3)
        return [("↔ " + "·".join(tgts[:3]) + extra, anti_any)]
    keep = lines[:max_lines - 1]
    rest = len(lines) - (max_lines - 1)
    keep.append(("+%d more edges" % rest, False))
    return keep


def render_zoom(G, fname, title, groups, subtitle=None, footnote=None,
                small=False, fs_title=10.0, legend=True):
    """groups: list of dicts(header, ids, x0, y0, x1, y1, ncols)."""
    nodes, views = build_edge_views(G)
    fig, ax = new_fig(title, subtitle)
    placed = {}
    shown = set()
    for g in groups:
        for i in g["ids"]:
            shown.add(i)
    cur_stages = {nodes[i]["stage"] for i in shown if nodes[i]["stage"]}
    in_lines, stubs = compute_edge_plan(nodes, views, shown, cur_stages)

    for g in groups:
        ids = g["ids"]
        x0, y0, x1, y1 = g["x0"], g["y0"], g["x1"], g["y1"]
        ncols = g["ncols"]
        nrows = math.ceil(len(ids) / ncols)
        if g.get("header"):
            ax.text(x0, y1 + 0.14, g["header"], ha="left", va="center",
                    fontsize=9.5, fontweight="bold", color=TEAL)
        gapx, gapy = (0.16, 0.16) if small else (0.30, 0.32)
        cw = (x1 - x0 - (ncols - 1) * gapx) / ncols
        ch = min((y1 - y0 - (nrows - 1) * gapy) / nrows, 1.75)
        for k, nid in enumerate(ids):
            rr, cc = divmod(k, ncols)
            x = x0 + cc * (cw + gapx)
            y = y1 - (rr + 1) * ch - rr * gapy
            placed[nid] = (x, y, cw, ch)

    # in-panel edge links (under the cards; visible in the gaps)
    for a, b, eid, directed, anti in in_lines:
        if a not in placed or b not in placed:
            continue
        xa, ya, wa, ha_ = placed[a]
        xb, yb, wb, hb = placed[b]
        ca, cb = (xa + wa / 2, ya + ha_ / 2), (xb + wb / 2, yb + hb / 2)
        pa = rect_anchor(*ca, wa, ha_, *cb)
        pb = rect_anchor(*cb, wb, hb, *ca)
        ax.add_patch(FancyArrowPatch(
            pa, pb, connectionstyle="arc3,rad=0.12",
            arrowstyle="-|>" if directed else "-",
            mutation_scale=9, lw=1.3,
            color=RED if anti else EDGE_C,
            linestyle=(0, (4, 3)) if anti else "solid", zorder=2))
        mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2 + 0.07
        ax.text(mx, my, eid + (" anti" if anti else ""), ha="center",
                va="center", fontsize=6.4, color=RED if anti else GREY,
                zorder=2.5,
                bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.85))

    for nid, (x, y, w, h) in placed.items():
        sl = merge_stub_lines(stubs.get(nid, []),
                              max_lines=1 if small else 2)
        draw_card(ax, nodes[nid], x, y, w, h, fs_title=fs_title,
                  stub_lines=sl, small=small)

    if legend:
        glyph_legend(ax, x=0.35, y=0.45, fs=7.6)
    footer(ax, extra=footnote)
    out = GRAPH_DIR / fname
    fig.savefig(out, dpi=DPI, facecolor="white")
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
# 5. the render suite
# ---------------------------------------------------------------------------
def stage_ids(G, num):
    st = next(s for s in G["stages"] if s["num"] == num)
    return st["ledger_ids"] + st["nonledger_ids"] + st["secondary_faces"]


def render_all(G):
    outs = [render_L0(G)]
    s6 = next(s for s in G["stages"] if s["num"] == 6)
    assert set(PANEL_A + PANEL_B + PANEL_C) == set(s6["ledger_ids"]), \
        "stage-6 panel split no longer matches the extracted ids"
    assert max(len(PANEL_A), len(PANEL_B), len(PANEL_C)) <= 12

    box = dict(x0=0.6, y0=1.0, x1=12.55, y1=6.45)
    panels = [
        ("L1_stage6_a.png", "panel a: engine cluster & driver", PANEL_A, 3),
        ("L1_stage6_b.png", "panel b: numerics & tolerances", PANEL_B, 3),
        ("L1_stage6_c.png", "panel c: design basis C1–C8", PANEL_C, 3),
    ]
    for fname, plab, ids, ncols in panels:
        outs.append(render_zoom(
            G, fname,
            "Design pipeline — Stage 6: OPTIMIZE (%s)" % plab,
            [dict(header=None, ids=ids, ncols=ncols, **box)],
            subtitle="stage 6 holds 24 of the 62 recorded choices — "
                     "3 panels"))

    # main-deck stages 4-5 selection
    outs.append(render_zoom(
        G, "L1_stage45.png",
        "Design pipeline — Stages 4–5: CERTIFY & ESTIMATE "
        "(core cards)",
        [dict(header="STAGE 4 · CERTIFY — certificates & qualification "
                     "(6 of 11 cards)",
              ids=SEL_S4, ncols=2, x0=0.6, y0=1.0, x1=6.25, y1=6.35),
         dict(header="STAGE 5 · ESTIMATE — estimator & bands "
                     "(6 of 9 cards)",
              ids=SEL_S5, ncols=2, x0=7.05, y0=1.0, x1=12.7, y1=6.35)],
        footnote="full stage zooms in backup"))

    # backup: all 8 stage zooms
    fullbox = dict(x0=0.6, y0=1.0, x1=12.55, y1=6.4)
    for num in range(1, 9):
        if num == 6:
            continue
        ids = stage_ids(G, num)
        ncols = 3 if len(ids) <= 9 else 4
        fn = None
        if num in (3, 5):
            fn = ("anti-edge E34 (C6 " + PERP + " C42): recorded "
                  "non-coupling, not an omission")
        outs.append(render_zoom(
            G, "L1_stage%d.png" % num,
            "Design pipeline — Stage %d: %s (%s)"
            % (num, DISPLAY[num],
               next(s for s in G["stages"] if s["num"] == num)["name"]
               .title()),
            [dict(header=None, ids=ids, ncols=ncols, **fullbox)],
            footnote=fn))

    # backup stage 6: the 3 panels mounted as columns on one sheet
    cols = [
        ("(a) ENGINE & DRIVER", PANEL_A, 0.45, 4.45),
        ("(b) NUMERICS & TOLERANCES", PANEL_B, 4.75, 8.75),
        ("(c) DESIGN BASIS C1–C8", PANEL_C, 9.05, 13.05),
    ]
    groups = [dict(header=h, ids=ids, ncols=2, x0=x0, y0=0.85, x1=x1,
                   y1=6.30) for h, ids, x0, x1 in cols]
    outs.append(render_zoom(
        G, "L1_stage6.png",
        "Design pipeline — Stage 6: OPTIMIZE (all 24 choices, "
        "3 panels)", groups, small=True, legend=False,
        footnote="panel slides a/b/c carry the readable version"))
    return outs


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    G, checks = load_asserted_graph()
    outs = render_all(G)
    print("\n=== RENDER SUMMARY ===")
    print("assert gate: %d/%d PASS (extract_graph.py re-run, "
          "map-measured)" % (sum(1 for c in checks if c["pass"]),
                             len(checks)))
    for o in outs:
        print("  wrote %s" % o)
    print("renders: %d files in %s" % (len(outs), GRAPH_DIR))
    return 0


if __name__ == "__main__":
    sys.exit(main())
