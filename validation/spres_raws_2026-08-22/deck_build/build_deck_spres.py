# -*- coding: utf-8 -*-
"""S-PRES deck builder — consumes specs_a/specs_c12/specs_c34/specs_d,
edits the 18 host slides (form fixes 1-9), authors the new slides,
injects speaker notes (guard 15), asserts the build (join completeness,
font floors, on-slide register lint, figure existence, graph asserts),
and writes SPRES_deck_v1.pptx + DECK_MANIFEST.md.

Run:  python build_deck_spres.py
"""
import json
import os
import re
import sys

from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

import spreslib as L
import typo_canon as TC  # S4 typography canon (measured host values, named)
from spreslib import (Presentation, RED, TEAL, GRAY, LGRAY, WHITE, AMBER,
                      TEAL_BG, RED_BG, FONT, add_text, add_kicker, add_cite,
                      add_img, img_scaled, bullets, add_table, add_card,
                      add_band, add_arrow, new_slide, set_footer, set_notes,
                      move_slide, respath)

from specs_a import SLIDES_A, SLIDES_B
from specs_c12 import SLIDES_C12
from specs_c34 import SLIDES_C34
from specs_d import SLIDES_D

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPPTX = os.path.join(HERE, "SPRES_deck_v1.pptx")

_RAW = SLIDES_A + SLIDES_B + SLIDES_C12 + SLIDES_C34
MAIN_SPECS = [sp for sp in _RAW if not sp.get("to_backup")]
# final order of record (spine wave MOVE-1/MOVE-2, combined walk verified):
# S4v2 (CKP-S4-2): nozzle part = 9 slides; A2 killed; no asks; deck
# closes on the plan slide with the takeaway line.
DECK_ORDER = (["A1", "A3", "A4", "A5", "A7", "A8", "A9", "A10", "A11",
               "A12a", "A12b", "A13", "A14", "A15", "A16", "A17", "A18",
               "A19", "A20", "B1", "A6", "C4", "C7-bis", "C7-ter", "C9",
               "C13", "C13-val", "C11", "C17"])
assert sorted(DECK_ORDER) == sorted(sp["id"] for sp in MAIN_SPECS), \
    "DECK_ORDER out of sync with main specs"
MAIN_SPECS = sorted(MAIN_SPECS, key=lambda sp: DECK_ORDER.index(sp["id"]))
CUT_SPECS = [sp for sp in _RAW if sp.get("to_backup")]
# Backup demarcation slide (user order S4): main-only page numbering,
# backup opens with a "Backup Slides" divider; backup counters = B-n.
DIVIDER_SPEC = dict(id="BKDIV", kind="new", layout="divider", minutes=0,
                    title="Backup Slides", content=dict(),
                    notes="Divider - backup section begins (S4 order: "
                          "main-only numbering; backup slides carry B-n).")
ALL_SPECS = (MAIN_SPECS + [DIVIDER_SPEC] + SLIDES_D
             + CUT_SPECS)  # cuts land after backup, declared

# ----------------------------------------------------------------- lint 18
# on-slide register lint (guard 18 + user rule 2026-08-23: no internal /
# process language on slides; engineering English only)
BANNED_ON_SLIDE = [
    r"\bquery-bounded\b", r"\bNOT-FOUND\b", r"\bfeed\b", r"\bguardia\b",
    r"\bguard \d", r"\bP34\b", r"\bSCHEMA\b", r"\bTHEOREM\*", r"\bM-RED\b",
    r"\bPB-2\b", r"\bS-5F\b", r"\bU3'\b", r"\bC-\d", r"\bLL-\d+\b",
    r"\bCH\d+-feed", r"\bF2-entry\b", r"\bregistry\b", r"\blint\b",
    r"\brefuter\b", r"\borchestrator\b", r"\bsubagent\b", r"\bworkflow\b",
    r"\b23/23\b", r"\b52/52\b", r"\b218/218\b", r"\b91/91\b",
    r"\bX-[A-Z]", r"\b\[REP\]", r"\b\[ADV\]", r"\b\[SE\]", r"\b\[IO\]",
]
_BANNED = [re.compile(p) for p in BANNED_ON_SLIDE]


def lint_text(sid, txt, report):
    for rx in _BANNED:
        if rx.search(txt):
            report.append(f"REGISTER-LINT HIT [{sid}]: '{rx.pattern}' in: {txt[:90]}")


def wcount(txt):
    return len([w for w in re.split(r"\s+", txt) if w.strip("•–-—")])


class Acc:
    """Per-slide accounting for the manifest + asserts."""
    def __init__(self):
        self.rows = []
        self.lint = []
        self.word_warn = []

    def slide(self, sid, title, minutes, body_words, figs, notes_len):
        self.rows.append((sid, title, minutes, body_words, figs, notes_len))


ACC = Acc()


def _collect(sid, *texts):
    """Lint + count body words for on-slide strings."""
    n = 0
    for t in texts:
        if not t:
            continue
        if isinstance(t, (list, tuple)):
            n += _collect(sid, *t)
            continue
        lint_text(sid, t, ACC.lint)
        n += wcount(t)
    return n


# ============================================================ EDIT ops
def _iter_text_shapes(shape):
    if shape.shape_type == 6:  # group
        for sub in shape.shapes:
            yield from _iter_text_shapes(sub)
    elif shape.has_text_frame:
        yield shape


def fix_footer_residual(slide):
    """Fix 1: remove residual 'HEM modeling…' text inside footer group."""
    for shp in slide.shapes:
        if shp.name == "Gruppo 6":
            for ts in _iter_text_shapes(shp):
                if "HEM" in ts.text_frame.text:
                    for p in ts.text_frame.paragraphs:
                        for r in p.runs:
                            r.text = ""


def apply_edit(prs, spec, slide):
    ops = spec.get("edits", [])
    fix_footer_residual(slide)
    if "title_slide_frontmatter" in ops:
        add_text(slide, 2.28, 3.05, 10.24, 0.4,
                 "ESA Technical Briefing — September 2026 — v1.0",
                 role="caption", size=16, color=LGRAY, italic=True)
    if "fix_bellenoue" in ops:
        for shp in slide.shapes:
            if shp.has_text_frame and "Belleonue" in shp.text_frame.text:
                for p in shp.text_frame.paragraphs:
                    for r in p.runs:
                        r.text = r.text.replace("Belleonue", "Bellenoue")
    if "open_lines_pointer" in ops:
        for shp in slide.shapes:
            if shp.has_text_frame and "nozzle design" in shp.text_frame.text:
                for p in shp.text_frame.paragraphs:
                    for r in p.runs:
                        r.text = r.text.replace(
                            "nozzle design",
                            "nozzle design (→ dedicated section today)")
    if "lighten_a7" in ops or "lighten_a8" in ops:
        pass  # host card text kept intact: no content removal (v1 rule);
              # pacing handled by speech. Declared in BUILD_REPORT.
    if "remove_offcanvas_a14" in ops:
        for shp in list(slide.shapes):
            try:
                if shp.left is not None and shp.left > Inches(13.35):
                    shp._element.getparent().remove(shp._element)
            except Exception:
                pass
    if "native_heading_a15" in ops:
        add_text(slide, 0.32, 0.95, 12.3, 0.45,
                 "Λ sweep: stagnation-pressure losses grow with wave number",
                 role="kicker", size=24, color=TEAL)
    if "b1_kicker_band" in ops:
        c = spec["content"]
        for shp in slide.shapes:
            if shp.has_text_frame and "optimal" in shp.text_frame.text:
                for pp in shp.text_frame.paragraphs:
                    if "profile exist" in "".join(r.text for r in pp.runs):
                        for r in pp.runs:
                            r.font.color.rgb = TEAL
                            r.font.bold = True
        # narrow the host citation box so the stakes card fits at right
        for shp in slide.shapes:
            if (shp.has_text_frame and "Harroun" in shp.text_frame.text
                    and "Stechmann" in shp.text_frame.text):
                shp.width = Inches(7.9)
        add_band(slide, 8.55, 5.80, 4.42, 0.86,
                 [[("The stakes are real:  ", {"size": 12.5, "bold": True,
                                               "color": RED}),
                   ("+4–7% Isp (choked interface) · 58.1→71.5% of ideal "
                    "(shroud) — the next section is the group's answer",
                    {"size": 12, "color": GRAY})]],
                 ec=RED, fc=RED_BG, size=12)
        _collect(spec["id"],
                 "The stakes are real: +4-7% Isp (choked interface) "
                 "58.1-71.5% of ideal (shroud) - the next section is the "
                 "group's answer")


# ============================================================ NEW layouts
def title_and_content(prs, footer_src, spec):
    s = new_slide(prs, footer_src, spec["title"], spec.get("kicker"))
    return s


def ly_bluf(prs, fs, spec):
    # A2 agenda form (CKP-S3-2): numbered agenda lines, no minutes
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    rows = [[(f"{i+1}   ", {"size": 22, "bold": True, "color": RED}),
             (lab, {"size": 22, "color": GRAY})]
            for i, lab in enumerate(c["agenda"])]
    add_text(s, 1.6, 1.9, 10.5, 3.6, rows, role="body_big", size=22,
             line_spacing=1.25, space_after=14)
    add_text(s, 1.6, 5.6, 10.5, 0.5, c["closing"], role="body", size=18,
             color=TEAL, italic=True)
    n = _collect(spec["id"], c["closing"], *c["agenda"])
    return s, n


def ly_two_fig_primer(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    lf, lcap = c["left_fig"]
    rf, rcap = c["right_fig"]
    img_scaled(s, respath(lf), 0.45, 1.75, 6.0, 3.55)
    img_scaled(s, respath(rf), 6.95, 1.75, 5.95, 3.55)
    add_cite(s, lcap, top=5.38, left=0.45, width=6.0)
    add_cite(s, rcap, top=5.38, left=6.95, width=5.95)
    add_text(s, 0.6, 5.75, 12.2, 1.0, bullets(c["bullets"], size=18),
             role="body", size=18, line_spacing=1.05)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_fig_plus_eq(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, cap = c["fig"]
    img_scaled(s, respath(f), 0.45, 1.7, 7.1, 3.9)
    add_cite(s, cap, top=5.66, left=0.45, width=7.1)
    add_img(s, respath(c["eq"]), 7.9, 2.3, width=5.0)
    if c.get("eq_caption"):
        add_text(s, 7.9, 3.28, 5.0, 0.3, c["eq_caption"], role="cite",
                 size=10.5, color=LGRAY, italic=True)
    add_text(s, 7.9, 3.72, 5.0, 2.5, bullets(c["bullets"], size=18),
             role="body", size=18, line_spacing=1.05)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_dichotomy_figs(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, cap = c["main_fig"]
    img_scaled(s, respath(f), 0.45, 1.72, 7.7, 3.5)
    add_cite(s, cap, top=5.26, left=0.45, width=7.7)
    y = 1.72
    for tf_, tcap in c["thumbs"]:
        img_scaled(s, respath(tf_), 8.55, y, 4.3, 1.62)
        add_cite(s, tcap, top=y + 1.64, left=8.55, width=4.3)
        y += 1.95
    add_text(s, 0.6, 5.62, 12.2, 1.0, bullets(c["bullets"], size=16),
             role="body", size=18, line_spacing=1.0, space_after=2)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_c2_throat(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f1, cap1 = c["fig1"]; f2, cap2 = c["fig2"]; f3, _ = c["fig3"]
    img_scaled(s, respath(f1), 0.4, 1.7, 4.4, 3.1)
    add_cite(s, cap1, top=4.85, left=0.4, width=4.4)
    img_scaled(s, respath(f2), 4.95, 1.7, 4.3, 3.1)
    add_cite(s, cap2, top=4.85, left=4.95, width=4.3)
    img_scaled(s, respath(f3), 9.4, 1.7, 3.6, 3.15)
    add_text(s, 0.5, 5.25, 12.4, 1.6, bullets(c["bullets"], size=16),
             role="body", size=18, line_spacing=1.0, space_after=3)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_grid4_methods(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    cells = [(0.4, 1.6), (6.85, 1.6), (0.4, 3.95), (6.85, 3.95)]
    for (fp, chip, cite), (x, y) in zip(c["grid"], cells):
        img_scaled(s, respath(fp), x, y, 4.0, 2.0)
        add_band(s, x + 4.05, y + 0.25, 2.05, 1.05,
                 [[(chip, {"size": 12, "bold": True, "color": GRAY})]],
                 ec=TEAL, fc=TEAL_BG, size=12)
        add_cite(s, cite, top=y + 2.02, left=x, width=6.1)
    add_band(s, 0.5, 6.28, 12.3, 0.5, c["takeaway"], ec=RED, fc=RED_BG,
             size=15, color=GRAY, bold=True, align=PP_ALIGN.CENTER)
    n = _collect(spec["id"], c["takeaway"], *[g[1] for g in c["grid"]])
    return s, n


def ly_table_claim(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    rows = [c["table_header"]] + [list(r) for r in c["table"]]
    add_table(s, 0.55, 1.7, 12.2, rows, col_widths=[1, 3.4],
              body_size=13.5, row_h=0.55)
    add_band(s, 0.55, 5.55, 12.2, 1.05, c["claim"], ec=RED, fc=RED_BG,
             size=15, color=GRAY, align=PP_ALIGN.CENTER)
    n = _collect(spec["id"], c["claim"],
                 *[a + " " + b for a, b in c["table"]])
    return s, n


def ly_c4_chain(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, cap = c["main_fig"]
    img_scaled(s, respath(f), 0.4, 1.65, 4.6, 4.1)
    add_cite(s, cap, top=5.8, left=0.4, width=4.6)
    f2, cap2 = c["side_fig"]
    img_scaled(s, respath(f2), 5.15, 1.65, 3.6, 2.4)
    add_cite(s, cap2, top=4.1, left=5.15, width=3.6)
    f3, cap3 = c["thumb"]
    img_scaled(s, respath(f3), 5.15, 4.55, 3.6, 1.55)
    add_cite(s, cap3, top=6.15, left=5.15, width=3.6)
    y = 1.65
    for num, txt in c["steps"]:
        add_band(s, 8.95, y, 4.05, 1.5,
                 [[(num + " · ", {"size": 16, "bold": True, "color": RED}),
                   (txt, {"size": 12.5, "color": GRAY})]],
                 ec=RED if num != "3" else GRAY,
                 fc=WHITE, size=12.5)
        y += 1.62
    n = _collect(spec["id"], *[t for _n, t in c["steps"]])
    return s, n


def ly_fig_bullets(prs, fs, spec, tag=None):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, cap = c["fig"]
    if c.get("fig2"):
        img_scaled(s, respath(f), 0.4, 1.7, 6.6, 2.5)
        img_scaled(s, respath(c["fig2"][0]), 0.4, 4.28, 6.6, 1.75)
    else:
        img_scaled(s, respath(f), 0.4, 1.7, 6.6, 4.35)
    if cap:
        add_cite(s, cap, top=6.1, left=0.4, width=6.6)
    if c.get("fig3"):
        add_text(s, 7.25, 1.75, 5.75, 1.85, bullets(c["bullets"], size=15),
                 role="body", size=18, line_spacing=1.0, space_after=4)
        f3, cap3 = c["fig3"]
        img_scaled(s, respath(f3), 7.25, 3.62, 5.75, 2.55)
        if cap3:
            add_cite(s, cap3, top=6.2, left=7.25, width=5.75)
    else:
        add_text(s, 7.25, 1.8, 5.75, 4.5, bullets(c["bullets"], size=16),
                 role="body", size=18, line_spacing=1.03, space_after=6)
    if c.get("tag") or tag:
        add_band(s, 7.25, 5.9, 5.75, 0.85, c.get("tag", tag), ec=TEAL,
                 fc=TEAL_BG, size=13, color=GRAY)
    n = _collect(spec["id"], c["bullets"], c.get("tag"))
    return s, n


def ly_timeline_rao(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    xs = 0.55
    w = 2.02
    add_arrow(s, 0.5, 2.35, 12.9, 2.35, color=LGRAY, weight=2.0)
    for i, (yr, who, what) in enumerate(c["timeline"]):
        x = xs + i * (w + 0.08)
        col = RED if i == len(c["timeline"]) - 1 else TEAL
        add_card(s, x, 2.6, w, 1.9, f"{yr} · {who}", what, ec=col,
                 head_size=13, body_size=12)
        add_arrow(s, x + w / 2, 2.6, x + w / 2, 2.38, color=col, weight=1.4)
    f, cap = c["eq_fig"]
    img_scaled(s, respath(f), 0.7, 4.85, 5.6, 1.0)
    add_cite(s, cap, top=5.9, left=0.7, width=5.6)
    add_text(s, 6.7, 5.05, 6.2, 0.9, c["footline"], role="body", size=18,
             italic=True)
    n = _collect(spec["id"], c["footline"],
                 *[f"{a} {b} {d}" for a, b, d in c["timeline"]])
    return s, n


def ly_quote_twolevel(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    add_band(s, 0.7, 1.75, 11.9, 1.35,
             [[(c["quote"], {"size": 21, "italic": True, "color": GRAY})]],
             ec=TEAL, fc=TEAL_BG, size=21, align=PP_ALIGN.CENTER)
    add_cite(s, c["quote_src"], top=3.18, left=0.7, width=11.9)
    y = 3.85
    for name, txt, kind in c["levels"]:
        col = TEAL if kind == "known" else RED
        add_band(s, 1.4, y, 10.6, 0.75,
                 [[(name + " — ", {"size": 15, "bold": True, "color": col}),
                   (txt, {"size": 14, "color": GRAY})]], ec=col,
                 fc=WHITE, size=14)
        y += 0.92
    add_text(s, 1.4, y + 0.1, 10.6, 0.55, c["thesis"], role="body_big",
             size=20, color=RED, bold=True, align=PP_ALIGN.CENTER)
    n = _collect(spec["id"], c["quote"], c["thesis"],
                 *[a + " " + b for a, b, _k in c["levels"]])
    return s, n


def ly_cards4_timeline(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    w = 3.02
    for i, (head, body) in enumerate(c["cards"]):
        col = RED if i == len(c["cards"]) - 1 else TEAL
        last = i == len(c["cards"]) - 1
        add_card(s, 0.5 + i * (w + 0.14), 1.75, w, 4.0 if last else 3.3,
                 head, body, ec=col, head_size=13.5, body_size=12,
                 fc=RED_BG if last else None)
    if c.get("eq"):
        x4 = 0.5 + 3 * (w + 0.14)
        add_img(s, respath(c["eq"]), x4 + 0.12, 4.55, width=w - 0.24)
    n = _collect(spec["id"], *[h + " " + b for h, b in c["cards"]])
    return s, n


def ly_two_problems(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    for side, x, col, bg in ((c["left"], 0.5, GRAY, WHITE),
                             (c["right"], 6.85, TEAL, TEAL_BG)):
        add_card(s, x, 1.6, 6.0, 3.1, side["head"], None, ec=col, fc=bg,
                 head_size=16)
        y = 2.25
        for i, step in enumerate(side["chain"]):
            add_text(s, x + 0.45, y, 5.3, 0.42, step, role="caption",
                     size=13, color=GRAY,
                     bold=(i == len(side["chain"]) - 1))
            if i < len(side["chain"]) - 1:
                add_arrow(s, x + 0.28, y + 0.1, x + 0.28, y + 0.5,
                          color=col, weight=1.4)
            y += 0.52
        add_text(s, x + 0.2, 4.28, 5.6, 0.4, side["foot"], role="caption",
                 size=12.5, color=RED if x < 6 else TEAL, italic=True)
    add_img(s, respath(c["eqs"][0]), 0.85, 4.85, width=2.9)
    add_img(s, respath(c["eqs"][1]), 4.35, 4.90, width=6.1)
    tb_pre, tb_bold, tb_post = c["theorem_band_runs"]
    add_band(s, 0.5, 5.58, 12.35, 1.0,
             [[(tb_pre, {"size": 15, "color": GRAY}),
               (tb_bold, {"size": 15, "bold": True, "color": RED}),
               (tb_post, {"size": 15, "color": GRAY})]],
             ec=RED, fc=RED_BG, size=15, align=PP_ALIGN.LEFT)
    n = _collect(spec["id"], "".join(c["theorem_band_runs"]), c["left"]["head"],
                 c["right"]["head"], c["left"]["foot"], c["right"]["foot"],
                 c["left"]["chain"], c["right"]["chain"])
    return s, n


def ly_three_panel_bifurcation(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    w = 4.05
    for i, (head, verdict, sub, ours) in enumerate(c["panels"]):
        col = RED if ours else TEAL
        bg = RED_BG if ours else WHITE
        add_card(s, 0.45 + i * (w + 0.17), 1.65, w, 2.6, head, None,
                 ec=col, fc=bg, head_size=13)
        add_text(s, 0.6 + i * (w + 0.17), 2.35, w - 0.3, 0.5, verdict,
                 role="caption", size=15, color=col, bold=True)
        add_text(s, 0.6 + i * (w + 0.17), 2.98, w - 0.3, 1.2, sub,
                 role="caption", size=12.5, color=GRAY)
    add_band(s, 0.45, 4.75, 12.45, 1.15, c["honesty_band"], ec=RED,
             fc=WHITE, size=14, color=GRAY)
    n = _collect(spec["id"], c["honesty_band"],
                 *[f"{h} {v} {su}" for h, v, su, _o in c["panels"]])
    return s, n


def ly_fig_bullets_tag(prs, fs, spec):
    return ly_fig_bullets(prs, fs, spec)


def ly_envelope_sectors(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, _ = c["fig"]
    img_scaled(s, respath(f), 0.35, 1.6, 6.4, 3.3)
    add_text(s, 6.95, 1.62, 6.05, 4.6, bullets(c["bullets"], size=13),
             role="body", size=18, line_spacing=1.0, space_after=5)
    add_band(s, 0.45, 6.15, 12.4, 0.62, c["state_line"], ec=TEAL,
             fc=TEAL_BG, size=14, color=GRAY, align=PP_ALIGN.CENTER)
    n = _collect(spec["id"], c["bullets"], c["state_line"])
    return s, n


def ly_operator_fig(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    sf, _ = c["schema"]
    img_scaled(s, respath(sf), 0.4, 1.65, 6.6, 3.1)
    f, cap = c["fig"]
    img_scaled(s, respath(f), 7.25, 1.65, 5.7, 2.6)
    add_cite(s, cap, top=4.3, left=7.25, width=5.7)
    add_text(s, 0.5, 4.95, 12.4, 1.85, bullets(c["bullets"], size=14),
             role="body", size=18, line_spacing=1.0, space_after=3)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_honesty_table(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    rows = [c["table_header"]] + [list(r) for r in c["table"]]
    add_table(s, 0.5, 1.62, 12.35, rows, col_widths=[1.6, 1.4, 1.0, 1.3],
              body_size=12.5, row_h=0.42)
    add_text(s, 0.55, 4.85, 12.3, 1.9, bullets(c["bullets"], size=14),
             role="body", size=18, line_spacing=1.0, space_after=4)
    n = _collect(spec["id"], c["bullets"],
                 *[" ".join(map(str, r)) for r in c["table"]])
    return s, n


def ly_cards4(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    pos = [(0.5, 1.7), (6.85, 1.7), (0.5, 4.15), (6.85, 4.15)]
    for (head, body), (x, y) in zip(c["cards"], pos):
        add_card(s, x, y, 6.0, 2.25, head, body, ec=TEAL, head_size=15,
                 body_size=12.5)
    n = _collect(spec["id"], *[h + " " + b for h, b in c["cards"]])
    return s, n


def ly_cards3(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    w = 4.05
    for i, (head, body) in enumerate(c["cards"]):
        add_card(s, 0.45 + i * (w + 0.17), 2.0, w, 3.0, head, body,
                 ec=TEAL if i < 2 else RED, head_size=14, body_size=13)
    n = _collect(spec["id"], *[h + " " + b for h, b in c["cards"]])
    return s, n


def ly_big_fig(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, cap = c["fig"]
    img_scaled(s, respath(f), 0.5, 1.6, 8.4, 4.7)
    if cap:
        add_cite(s, cap, top=6.32, left=0.5, width=8.4)
    add_text(s, 9.15, 1.9, 3.85, 4.4, bullets(c["bullets"], size=14),
             role="body", size=18, line_spacing=1.05, space_after=8)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_graph_l0(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, _ = c["fig"]
    img_scaled(s, respath(f), 0.35, 1.7, 12.65, 3.3)
    if c.get("fig_note"):
        add_text(s, 0.6, 5.02, 12.2, 0.28, c["fig_note"], role="cite",
                 size=10, color=LGRAY, italic=True)
    add_text(s, 0.6, 5.35, 12.2, 1.4, bullets(c["bullets"], size=15),
             role="body", size=18, line_spacing=1.03, space_after=4)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_graph_stage6(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, _ = c["fig"]
    img_scaled(s, respath(f), 0.35, 1.65, 12.65, 3.55)
    add_text(s, 0.6, 5.4, 12.2, 1.4, bullets(c["bullets"], size=15),
             role="body", size=18, line_spacing=1.03, space_after=4)
    n = _collect(spec["id"], c["bullets"])
    return s, n


def ly_graph_certs(prs, fs, spec):
    return ly_graph_stage6(prs, fs, spec)


def ly_numbers_bars(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    rows = [c["table_header"]] + [list(r) for r in c["table"]]
    add_table(s, 0.55, 1.75, 6.3, rows, col_widths=[2.2, 1.4, 1.0],
              body_size=14, row_h=0.5)
    f, _ = c["fig"]
    img_scaled(s, respath(f), 7.15, 1.75, 5.8, 2.9)
    add_band(s, 0.55, 5.15, 12.4, 0.95, c["footline"], ec=TEAL, fc=TEAL_BG,
             size=15, color=GRAY, align=PP_ALIGN.CENTER)
    n = _collect(spec["id"], c["footline"],
                 *[" ".join(map(str, r)) for r in c["table"]])
    return s, n


def ly_audit_timeline(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    x = 0.5
    for head, body in c["timeline_cards"]:
        add_card(s, x, 1.7, 6.05, 1.75, head, body, ec=RED, head_size=14,
                 body_size=12.5)
        x += 6.35
    add_arrow(s, 6.35, 2.55, 6.7, 2.55, color=RED, weight=2.2)
    add_text(s, 0.6, 3.85, 12.3, 2.7, bullets(c["bullets"], size=15),
             role="body", size=18, line_spacing=1.05, space_after=7)
    n = _collect(spec["id"], c["bullets"],
                 *[h + " " + b for h, b in c["timeline_cards"]])
    return s, n


def ly_three_gaps(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    w = 3.95
    for i, (head, sub) in enumerate(c["columns"]):
        col = TEAL if i == 1 else GRAY
        add_card(s, 0.5 + i * (w + 0.22), 1.62, w, 1.35, head, sub,
                 ec=col, head_size=14, body_size=12)
        if i < 2:
            add_arrow(s, 0.5 + (i + 1) * w + i * 0.22 + 0.02, 2.3,
                      0.5 + (i + 1) * (w + 0.22) - 0.02, 2.3,
                      color=RED, weight=2.0)
    add_text(s, 0.55, 3.1, 12.3, 0.35, c["gaps_label"], role="caption",
             size=13, color=RED, italic=True, align=PP_ALIGN.CENTER)
    add_band(s, 0.5, 3.6, 12.4, 1.5, c["hypothesis"], ec=TEAL, fc=TEAL_BG,
             size=14, color=GRAY)
    if c.get("heel"):
        add_band(s, 0.5, 5.2, 12.4, 0.7, c["heel"], ec=RED, fc=RED_BG,
                 size=13.5, color=GRAY)
    add_band(s, 0.5, 5.25, 12.4, 0.75, c["death_line"], ec=GRAY, fc=WHITE,
             size=13.5, color=GRAY)
    n = _collect(spec["id"], c["gaps_label"], c["hypothesis"], c["heel"],
                 c["death_line"], *[a + " " + b for a, b in c["columns"]])
    return s, n


def ly_roadmap_cards(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    w = 3.05
    for i, (head, d, e, wdw) in enumerate(c["cards"]):
        x = 0.42 + i * (w + 0.12)
        add_card(s, x, 1.55, w, 3.15, head, None,
                 ec=TEAL if i else RED, head_size=12)
        if i:
            add_arrow(s, x - 0.13, 3.1, x + 0.01, 3.1, color=GRAY, weight=2.4)
        add_text(s, x + 0.12, 2.2, w - 0.24, 2.4,
                 [[(d, {"size": 12, "color": GRAY})],
                  [(e, {"size": 12, "color": GRAY})],
                  [(wdw, {"size": 12, "color": TEAL, "italic": True})]],
                 role="caption", size=12, line_spacing=1.0, space_after=4)
    add_text(s, 0.5, TC.ROADMAP_GAPLINE_TOP_IN, 12.35, 0.62, c["gap_line"], role="caption",
             size=13, color=GRAY, italic=True)
    add_band(s, 0.5, TC.ROADMAP_KILL_TOP_IN, 12.35, TC.ROADMAP_KILL_H_IN, c["kill_line"], ec=RED, fc=RED_BG,
             size=13, color=GRAY)
    if c.get("closing"):
        add_text(s, 0.5, TC.ROADMAP_CLOSING_TOP_IN, 12.35, TC.ROADMAP_CLOSING_H_IN, c["closing"], role="caption",
                 size=14, color=RED, bold=True, align=PP_ALIGN.CENTER)
    n = _collect(spec["id"], c["gap_line"], c["kill_line"],
                 c.get("closing", ""), c.get("timeline_label", ""),
                 *[" ".join(cc) for cc in c["cards"]])
    return s, n


def ly_open_cards(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    add_band(s, 0.5, 1.6, 12.35, 0.8, c["intro"], ec=TEAL, fc=TEAL_BG,
             size=14, color=GRAY)
    w = 4.05
    for i, (head, body) in enumerate(c["cards"]):
        add_card(s, 0.45 + i * (w + 0.17), 2.7, w, 2.6,
                 "OPEN · " + head, body, ec=RED, head_size=12.5,
                 body_size=12)
    n = _collect(spec["id"], c["intro"],
                 *[h + " " + b for h, b in c["cards"]])
    return s, n


def ly_ask_cards(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    w = 4.05
    for i, (head, what, dec, when) in enumerate(c["cards"]):
        x = 0.45 + i * (w + 0.17)
        add_card(s, x, 1.55, w, 2.5, head, None, ec=RED, head_size=13)
        add_text(s, x + 0.12, 2.1, w - 0.24, 1.9,
                 [[(what, {"size": 12, "color": GRAY})],
                  [(dec, {"size": 12, "color": GRAY})],
                  [(when, {"size": 12, "color": TEAL, "italic": True})]],
                 role="caption", size=12, line_spacing=1.0, space_after=3)
    add_band(s, 0.45, 4.45, 12.4, 1.6, c["input_band"], ec=TEAL, fc=TEAL_BG,
             size=14, color=GRAY)
    n = _collect(spec["id"], c["input_band"],
                 *[" ".join(cc) for cc in c["cards"]])
    return s, n


def ly_summary(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    add_text(s, 0.6, 1.7, 6.1, 0.4, c["eng_head"], role="head", size=17,
             color=TEAL, bold=True)
    add_text(s, 0.6, 2.15, 6.1, 2.2, bullets(c["eng_bullets"], size=15),
             role="body", size=18, line_spacing=1.05, space_after=5)
    add_text(s, 7.0, 1.7, 6.0, 0.4, c["prog_head"], role="head", size=17,
             color=TEAL, bold=True)
    add_text(s, 7.0, 2.15, 6.0, 2.2, bullets(c["prog_bullets"], size=15),
             role="body", size=18, line_spacing=1.05, space_after=5)
    # S4: pipeline reprise ABOVE the closing band, clear of the footer
    # (Listener-1 layout defect: old placement collided with the band at
    # 6.76); band becomes the final statement before the footer.
    f, _ = c["fig"]
    img_scaled(s, respath(f), TC.SUMMARY_FIG_LEFT_IN, TC.SUMMARY_FIG_TOP_IN,
               TC.SUMMARY_FIG_MAXW_IN, TC.SUMMARY_FIG_MAXH_IN)
    add_band(s, 0.6, TC.SUMMARY_BAND_TOP_IN, 12.3, TC.SUMMARY_BAND_H_IN, c["closing"], ec=RED, fc=RED_BG,
             size=15, color=GRAY, align=PP_ALIGN.CENTER)
    n = _collect(spec["id"], c["closing"], c["eng_bullets"],
                 c["prog_bullets"])
    return s, n


def ly_backup_graph(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    f, _ = c["fig"]
    img_scaled(s, respath(f), 0.35, 1.55, 12.65, 4.5)
    add_text(s, 0.6, 6.15, 12.2, 0.5, c["note_line"], role="caption",
             size=12, color=LGRAY, italic=True)
    return s, 0


def ly_backup_card(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    add_card(s, 1.2, 2.2, 10.9, 3.0, c["card_title"], c["card_body"],
             ec=TEAL, head_size=17, body_size=14)
    return s, 0


def ly_backup_table(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    rows = [c["table_header"]] + [list(r) for r in c["table"]]
    add_table(s, 0.5, 1.75, 12.4, rows, col_widths=[1.5, 1.0, 1.0, 1.3, 1.4],
              body_size=12.5, row_h=0.5)
    add_text(s, 0.6, 5.6, 12.2, 0.6, c["note_line"], role="caption",
             size=13, color=LGRAY, italic=True)
    return s, 0


def ly_divider(prs, fs, spec):
    """Backup demarcation slide (user order S4): one big centered title."""
    s = new_slide(prs, fs, spec["title"])
    t = s.shapes.title
    t.top, t.height = Inches(TC.DIVIDER_TITLE_TOP_IN), Inches(TC.DIVIDER_TITLE_H_IN)
    p = t.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    for r in p.runs:
        r.font.size = Pt(TC.DIVIDER_PT)
    return s, 0


LAYOUTS = {name[3:]: fn for name, fn in list(globals().items())
           if name.startswith("ly_")}


# ================================================================== main
def main():
    prs = Presentation(L.TEMPLATE)
    host = list(prs.slides)
    footer_src = host[12]  # S13: simple slide, clean footer band

    # ---- fix master + layouts (fix 3): remove stale defaults
    for m in prs.slide_masters:
        for holder in [m] + list(m.slide_layouts):
            for shp in holder.shapes:
                if not shp.has_text_frame:
                    continue
                t = shp.text_frame.text
                if "M. Fiore" in t or "Modular Aerospike" in t or "/17" in t:
                    for p in shp.text_frame.paragraphs:
                        for r in p.runs:
                            r.text = (r.text
                                      .replace("M. Fiore et al", "T(H)RUST team")
                                      .replace("Modular Aerospike Nozzles for Upper Stage Applications",
                                               "Rotating Detonation Engine Activities")
                                      .replace("/17", ""))

    # ---- build slides in storyboard order
    built = []   # (spec, slide, body_words)
    for spec in ALL_SPECS:
        if spec["kind"] == "edit":
            slide = host[spec["src"] - 1]
            apply_edit(prs, spec, slide)
            built.append((spec, slide, 0))
        else:
            fn = LAYOUTS[spec["layout"]]
            slide, nwords = fn(prs, footer_src, spec)
            title_words = 0  # titles excluded from net budget by rule
            built.append((spec, slide, nwords))
        set_notes(built[-1][1], ALL_SPECS[len(built) - 1]["notes"])

    # ---- order: move slides into spec order
    for target_idx, (spec, slide, _n) in enumerate(built):
        move_slide(prs, slide, target_idx)

    # ---- footers/counters (fix 2 + S4 order): main-only numbering
    total = len(built)
    n_main_phys = len(MAIN_SPECS)
    from spreslib import fix_page_total, add_footer_texts

    def set_backup_counter(slide, label):
        """Replace the copied band counter (field + '/18') with a literal."""
        for sh0 in slide.shapes:
            for ts in _iter_text_shapes(sh0):
                if "/18" in ts.text_frame.text:
                    ts.text_frame.text = label
                    runs = ts.text_frame.paragraphs[0].runs
                    if runs:
                        runs[0].font.size = Pt(14)
                        runs[0].font.bold = True
                        runs[0].font.color.rgb = L.WHITE
                        runs[0].font.name = FONT

    for i, (spec, slide, _n) in enumerate(built, start=1):
        if spec["id"] == "A1":
            continue
        if i <= n_main_phys:
            set_footer(slide, i, n_main_phys)
            fix_page_total(slide, n_main_phys)
        else:
            label = "" if spec["id"] == "BKDIV" else f"B-{i - n_main_phys - 1}"
            set_backup_counter(slide, label)
        if spec["kind"] == "new":
            add_footer_texts(slide)

    # ---- typography normalization + machine asserts (CKP-S3-5(i))
    # host canon measured 2026-08-23: title 32pt bold RED at (0.32, 0.38);
    # footer texts at top 6.76 (label left 1.57 / team centered at 9.06).
    from pptx.util import Inches as _In, Emu as _Emu
    from pptx.enum.text import PP_ALIGN as _AL
    typo_problems = []

    def _first_run(sh):
        for p_ in sh.text_frame.paragraphs:
            for r_ in p_.runs:
                if r_.text.strip():
                    return r_, p_
        return None, None

    def _title_shape(slide):
        best = None
        for sh in slide.shapes:
            if not getattr(sh, "has_text_frame", False):
                continue
            if sh.top is None or sh.top > _In(TC.TITLE_ZONE_TOP_IN):
                continue
            r_, _p = _first_run(sh)
            if r_ is None or not r_.font.size:
                continue
            if r_.font.size.pt >= TC.TITLE_MIN_PT:
                if best is None or sh.top < best.top:
                    best = sh
        return best

    for i, (spec, slide, _n) in enumerate(built, start=1):
        if spec["id"] in ("A1", "BKDIV"):
            continue
        t = _title_shape(slide)
        if t is None:
            typo_problems.append(f"TYPO {spec['id']}: no title shape found")
            continue
        # ENFORCE the full title identity on every slide (host included),
        # once and for all (user order S4): identical box, TOP anchor,
        # zero margins, autofit KILLED (PowerPoint shrinks placeholder
        # titles on overflow — LibreOffice does not show it), every run
        # forced to 32pt bold RED in the deck font.
        from pptx.enum.text import (MSO_ANCHOR as _AN,
                                    MSO_AUTO_SIZE as _AS)
        from pptx.util import Pt as _Pt
        t.left, t.top = _In(TC.TITLE_LEFT_IN), _In(TC.TITLE_TOP_IN)
        t.width, t.height = _In(TC.TITLE_W_IN), _In(TC.TITLE_H_IN)
        _tf = t.text_frame
        _tf.vertical_anchor = _AN.TOP
        _tf.word_wrap = True
        try:
            _tf.auto_size = _AS.NONE
        except Exception:
            typo_problems.append(f"TYPO {spec['id']}: autofit not killable")
        for _m in ("margin_left", "margin_right", "margin_top",
                   "margin_bottom"):
            setattr(_tf, _m, _Emu(0))
        for _p2 in _tf.paragraphs:
            _p2.alignment = _AL.LEFT
            for _r2 in _p2.runs:
                _r2.font.size = _Pt(TC.TITLE_PT)
                _r2.font.bold = True
                _r2.font.name = FONT
                _r2.font.color.rgb = RED
        r_, _p = _first_run(t)
        if spec["kind"] == "new":
            if r_.font.size.pt != TC.TITLE_PT:
                typo_problems.append(
                    f"TYPO {spec['id']}: title size {r_.font.size.pt} != 32")
            if not r_.font.bold:
                typo_problems.append(f"TYPO {spec['id']}: title not bold")
        # SUBTITLE canon (user order S4, istanza 3): host slides carry teal
        # sub-heads in mixed 24/28pt, bold/non-bold — the visible "some
        # titles bold, some not". Enforce ONE identity on the heading line
        # (first paragraph only — some boxes carry body below): 28pt teal
        # bold, deck font.
        for sh0 in slide.shapes:
            if sh0 is t or not getattr(sh0, "has_text_frame", False):
                continue
            if sh0.top is None or sh0.top > _In(TC.SUBTITLE_ZONE_TOP_IN):
                continue
            fr, fp = _first_run(sh0)
            if fr is None or not fr.font.size:
                continue
            if TC.SUBTITLE_PT_MIN <= fr.font.size.pt <= TC.SUBTITLE_PT_MAX:
                for _r3 in fp.runs:
                    _r3.font.size = _Pt(TC.SUBTITLE_PT)
                    _r3.font.bold = True
                    _r3.font.name = FONT
                    _r3.font.color.rgb = TEAL
        # footer texts: ENFORCE one exact geometry + format on every slide
        # (host placeholders included; group children only reformatted —
        # their position is the band's, already canonical).
        def _near(v, target_in, tol=TC.GEOM_TOL_IN):
            return v is not None and abs(_Emu(v).inches - target_in) <= tol
        for sh0 in slide.shapes:
            for ts in _iter_text_shapes(sh0):
                txt0 = ts.text_frame.text.strip()
                # stale template page-number field inside the host band
                # group ("n/17"): blank it (the real counter is the
                # regenerated placeholder)
                if re.fullmatch(r"\d+/17", txt0):
                    ts.text_frame.text = ""  # removes stale field element
                    continue
                if txt0 in ("Rotating Detonation Engine Activities",
                            "T(H)RUST team"):
                    _team = txt0.startswith("T(H)")
                    if ts is sh0:  # top-level: safe to move
                        ts.left = _In(TC.FOOT_TEAM_LEFT_IN if _team
                                      else TC.FOOT_LABEL_LEFT_IN)
                        ts.top = _In(TC.BAND_TOP_IN)   # = red band box
                        ts.width = _In(TC.FOOT_TEAM_W_IN if _team
                                       else TC.FOOT_LABEL_W_IN)
                        ts.height = _In(TC.BAND_H_IN)
                    _ftf = ts.text_frame
                    _ftf.vertical_anchor = _AN.MIDDLE
                    for _m in ("margin_left", "margin_right", "margin_top",
                               "margin_bottom"):
                        setattr(_ftf, _m, _Emu(0))
                    for _p2 in _ftf.paragraphs:
                        _p2.alignment = _AL.CENTER
                        for _r2 in _p2.runs:
                            _r2.font.size = _Pt(TC.FOOT_PT)
                            _r2.font.bold = True
                            _r2.font.name = FONT
                            _r2.font.color.rgb = L.WHITE
        for sh0 in slide.shapes:
            for ts in _iter_text_shapes(sh0):
                txt = ts.text_frame.text.strip()
                if txt == "Rotating Detonation Engine Activities":
                    if not (_near(ts.top, TC.BAND_TOP_IN)
                            and _near(ts.left, TC.FOOT_LABEL_LEFT_IN)):
                        typo_problems.append(
                            f"TYPO {spec['id']}: foot label at "
                            f"({_Emu(ts.left).inches:.2f},"
                            f"{_Emu(ts.top).inches:.2f}) != (1.57,6.71)")
                    if (spec["kind"] == "new"
                            and ts.text_frame.paragraphs[0].alignment
                            != _AL.CENTER):
                        typo_problems.append(
                            f"TYPO {spec['id']}: foot label not centered "
                            "(host canon = centered placeholder)")
                elif txt == "T(H)RUST team":
                    if not (_near(ts.top, TC.BAND_TOP_IN)
                            and _near(ts.left, TC.FOOT_TEAM_LEFT_IN)):
                        typo_problems.append(
                            f"TYPO {spec['id']}: team text at "
                            f"({_Emu(ts.left).inches:.2f},"
                            f"{_Emu(ts.top).inches:.2f}) != (9.06,6.71)")
                    if (spec["kind"] == "new"
                            and ts.text_frame.paragraphs[0].alignment
                            != _AL.CENTER):
                        typo_problems.append(
                            f"TYPO {spec['id']}: team text not centered")
    ACC.lint.extend(typo_problems)

    out = OUTPPTX
    for suffix in ("", "_new", "_new2", "_new3"):
        out = OUTPPTX.replace(".pptx", suffix + ".pptx")
        try:
            prs.save(out)
            break
        except PermissionError:
            continue
    else:
        raise PermissionError("all candidate output names locked")
    if out != OUTPPTX:
        print("NOTE: canonical file locked (open in PowerPoint?) — saved as",
              os.path.basename(out))

    # ---- asserts + manifest
    ok = True
    problems = list(ACC.lint)
    # join completeness: every spec exactly once, order preserved
    ids = [sp["id"] for sp in ALL_SPECS]
    assert len(ids) == len(set(ids)), "duplicate slide ids"
    n_main = len(MAIN_SPECS)
    n_cut = len(CUT_SPECS)
    # S4v2 (CKP-S4-2): 19 host + B1 + 9 nozzle = 29 main; 22 cuts
    assert n_main == 29, f"main census {n_main} != 29 (CKP-S4-2)"
    assert n_cut == 22, f"cut census {n_cut} != 22 (CKP-S4-2 cut-list)"
    # word budget report
    manifest = [
        "# DECK_MANIFEST — SPRES_deck_v1 (join carrier for Block 2)",
        "",
        f"Slides: {total} total = {n_main} main + 1 divider + "
        f"{len(SLIDES_D)} backup + {n_cut} CUT-to-backup (cut-list S4: "
        "C3-bis, C12, C15, C17-bis, C16-bis(S4e); C2 PROMOTED to main "
        "post-C9 (S4); C-ADJ added (S4); merges: C13-pre->C13, C3-bis "
        "claim->C3, C17-bis->C18 card; A6 post-B1, CKP-S3-2). Main-only "
        "numbering; backup counters B-n (S4 order). Storyboard join "
        "unit = 50 (A12 = declared pair).",
        "",
        "Net-word rule (declared): body strings of the spec (bullets, bands,"
        " cards, chips) — titles, kickers, citations, figure labels and"
        " speaker notes excluded. Budget 60 (style pact E); overflow"
        " tolerated only on evidence-card slides, declared per row.",
        "",
        "| # | id | minutes | net words | budget | notes |",
        "|---|----|---------|-----------|--------|-------|",
    ]
    for i, (spec, slide, nw) in enumerate(built, start=1):
        cap = 180 if spec.get("layout") in ("table_claim", "honesty_table",
                                            "roadmap_cards", "ask_cards") else 110
        flag = "ok" if nw <= 60 else ("DECLARED-OVER" if nw <= cap else "FAIL")
        if flag == "FAIL":
            ok = False
            problems.append(f"WORD-BUDGET FAIL {spec['id']}: {nw}")
        manifest.append(f"| {i} | {spec['id']} | {spec.get('minutes','')} | "
                        f"{nw} | {flag} | notes={len(spec['notes'])}ch |")
    # graph asserts consumed
    gj = json.load(open(os.path.join(HERE, "graph",
                                     "pipeline_graph_asserted.json"),
                        encoding="utf-8"))
    n_ass = len(gj.get("asserts", []))
    all_pass = all(a.get("pass", a.get("ok", True)) for a in gj["asserts"]) \
        if isinstance(gj.get("asserts"), list) else True
    manifest.append("")
    manifest.append(f"Graph extraction asserts: {n_ass} recorded, all_pass={all_pass}")
    if not all_pass:
        ok = False
        problems.append("GRAPH ASSERTS NOT ALL PASS")
    if problems:
        manifest.append("")
        manifest.append("## PROBLEMS")
        manifest += [f"- {p}" for p in problems]
    with open(os.path.join(HERE, "DECK_MANIFEST.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(manifest) + "\n")
    print(f"saved {out}")
    print(f"slides {total}; register-lint hits {len(ACC.lint)}; "
          f"build {'OK' if ok and not ACC.lint else 'WITH PROBLEMS'}")
    for p in problems[:30]:
        print(" -", p)
    return 0 if ok and not ACC.lint else 1


if __name__ == "__main__":
    sys.exit(main())
