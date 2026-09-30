# -*- coding: utf-8 -*-
"""Spine-wave repair patch — builder side (layouts + order)."""

p = "build_deck_spres.py"
s = open(p, encoding="utf-8").read()
n0 = len(s)

def rep(old, new, must=True):
    global s
    c = s.count(old)
    if c != 1:
        print(f"!! count {c}: {old[:70]!r}")
        if must:
            raise SystemExit(1)
        return
    s = s.replace(old, new)

# ---- MOVE-1/2: explicit main-deck order
rep('''_RAW = SLIDES_A + SLIDES_B + SLIDES_C12 + SLIDES_C34
MAIN_SPECS = [sp for sp in _RAW if not sp.get("to_backup")]''',
'''_RAW = SLIDES_A + SLIDES_B + SLIDES_C12 + SLIDES_C34
MAIN_SPECS = [sp for sp in _RAW if not sp.get("to_backup")]
# final order of record (spine wave MOVE-1/MOVE-2, combined walk verified):
DECK_ORDER = (["A1", "A2", "A3", "A4", "A5", "A7", "A8", "A9", "A10", "A11",
               "A12a", "A12b", "A13", "A14", "A15", "A16", "A17", "A18",
               "A19", "A20", "B1", "A6", "C1", "C3", "C4", "C5", "C6", "C7",
               "C7-bis-pre", "C7-bis", "C7-ter", "C8", "C8-bis", "C9", "C10",
               "C13", "C14", "C13-val", "C16", "C16-bis", "C11", "C17-pre",
               "C17", "C18", "C19"])
assert sorted(DECK_ORDER) == sorted(sp["id"] for sp in MAIN_SPECS), \\
    "DECK_ORDER out of sync with main specs"
MAIN_SPECS = sorted(MAIN_SPECS, key=lambda sp: DECK_ORDER.index(sp["id"]))''')

# ---- ly_graph_l0: fig note (F-2)
rep('''    f, _ = c["fig"]
    img_scaled(s, respath(f), 0.35, 1.7, 12.65, 3.4)
    add_text(s, 0.6, 5.3, 12.2, 1.5, bullets(c["bullets"], size=15),''',
'''    f, _ = c["fig"]
    img_scaled(s, respath(f), 0.35, 1.7, 12.65, 3.3)
    if c.get("fig_note"):
        add_text(s, 0.6, 5.02, 12.2, 0.28, c["fig_note"], role="cite",
                 size=10, color=LGRAY, italic=True)
    add_text(s, 0.6, 5.35, 12.2, 1.4, bullets(c["bullets"], size=15),''')

# ---- ly_two_problems: theorem band promoted (F-10)
rep('''    add_band(s, 0.5, 5.62, 12.35, 0.95, c["theorem_band"], ec=RED,
             fc=RED_BG, size=13.5, color=GRAY, align=PP_ALIGN.LEFT)''',
'''    tb_pre, tb_bold, tb_post = c["theorem_band_runs"]
    add_band(s, 0.5, 5.58, 12.35, 1.0,
             [[(tb_pre, {"size": 15, "color": GRAY}),
               (tb_bold, {"size": 15, "bold": True, "color": RED}),
               (tb_post, {"size": 15, "color": GRAY})]],
             ec=RED, fc=RED_BG, size=15, align=PP_ALIGN.LEFT)''')

# ---- ly_roadmap_cards: ordered arrow sequence (F-11b)
rep('''    for i, (head, d, e, wdw) in enumerate(c["cards"]):
        x = 0.42 + i * (w + 0.12)
        add_card(s, x, 1.55, w, 3.15, head, None,
                 ec=TEAL if i else RED, head_size=11.5)''',
'''    for i, (head, d, e, wdw) in enumerate(c["cards"]):
        x = 0.42 + i * (w + 0.12)
        add_card(s, x, 1.55, w, 3.15, head, None,
                 ec=TEAL if i else RED, head_size=12)
        if i:
            add_arrow(s, x - 0.13, 3.1, x + 0.01, 3.1, color=GRAY, weight=2.4)''',
    must=False)

# ---- ly_three_gaps: heel optional; band sizes
rep('''    add_band(s, 0.5, 3.6, 12.4, 0.95, c["hypothesis"], ec=TEAL, fc=TEAL_BG,
             size=13.5, color=GRAY)
    add_band(s, 0.5, 4.66, 12.4, 0.95, c["heel"], ec=RED, fc=RED_BG,
             size=13.5, color=GRAY)
    add_band(s, 0.5, 5.72, 12.4, 0.8, c["death_line"], ec=GRAY, fc=WHITE,
             size=13, color=GRAY)''',
'''    add_band(s, 0.5, 3.6, 12.4, 1.5, c["hypothesis"], ec=TEAL, fc=TEAL_BG,
             size=14, color=GRAY)
    if c.get("heel"):
        add_band(s, 0.5, 5.2, 12.4, 0.7, c["heel"], ec=RED, fc=RED_BG,
                 size=13.5, color=GRAY)
    add_band(s, 0.5, 5.25, 12.4, 0.75, c["death_line"], ec=GRAY, fc=WHITE,
             size=13.5, color=GRAY)''')

# ---- ly_cards4_timeline: eq inside punch card (F-18)
rep('''    w = 3.02
    for i, (head, body) in enumerate(c["cards"]):
        col = RED if i == len(c["cards"]) - 1 else TEAL
        add_card(s, 0.5 + i * (w + 0.14), 1.75, w, 3.3, head, body,
                 ec=col, head_size=13.5, body_size=12)
    if c.get("eq"):
        add_img(s, respath(c["eq"]), 3.4, 5.5, width=6.5)''',
'''    w = 3.02
    for i, (head, body) in enumerate(c["cards"]):
        col = RED if i == len(c["cards"]) - 1 else TEAL
        last = i == len(c["cards"]) - 1
        add_card(s, 0.5 + i * (w + 0.14), 1.75, w, 4.0 if last else 3.3,
                 head, body, ec=col, head_size=13.5, body_size=12,
                 fc=RED_BG if last else None)
    if c.get("eq"):
        x4 = 0.5 + 3 * (w + 0.14)
        add_img(s, respath(c["eq"]), x4 + 0.12, 4.55, width=w - 0.24)''')

# ---- ly_fig_plus_eq: eq caption (F-17)
rep('''    add_img(s, respath(c["eq"]), 7.9, 2.3, width=5.0)
    add_text(s, 7.9, 3.6, 5.0, 2.6, bullets(c["bullets"], size=18),''',
'''    add_img(s, respath(c["eq"]), 7.9, 2.3, width=5.0)
    if c.get("eq_caption"):
        add_text(s, 7.9, 3.28, 5.0, 0.3, c["eq_caption"], role="cite",
                 size=10.5, color=LGRAY, italic=True)
    add_text(s, 7.9, 3.72, 5.0, 2.5, bullets(c["bullets"], size=18),''')

# ---- ly_dichotomy_figs: clear the footer (F-5)
rep('''    img_scaled(s, respath(f), 0.45, 1.8, 8.3, 3.9)
    add_cite(s, cap, top=5.75, left=0.45, width=8.3)
    y = 1.8
    for tf_, tcap in c["thumbs"]:
        img_scaled(s, respath(tf_), 9.0, y, 3.9, 1.8)
        add_cite(s, tcap, top=y + 1.82, left=9.0, width=3.9)
        y += 2.15
    add_text(s, 0.6, 6.05, 12.2, 0.9, bullets(c["bullets"], size=18),
             role="body", size=18, line_spacing=1.0, space_after=2)''',
'''    img_scaled(s, respath(f), 0.45, 1.72, 7.7, 3.5)
    add_cite(s, cap, top=5.26, left=0.45, width=7.7)
    y = 1.72
    for tf_, tcap in c["thumbs"]:
        img_scaled(s, respath(tf_), 8.55, y, 4.3, 1.62)
        add_cite(s, tcap, top=y + 1.64, left=8.55, width=4.3)
        y += 1.95
    add_text(s, 0.6, 5.62, 12.2, 1.0, bullets(c["bullets"], size=16),
             role="body", size=18, line_spacing=1.0, space_after=2)''')

# ---- ly_ask_cards: three cards, no ladder, wide band (F-4)
rep('''    add_band(s, 0.45, 4.25, 8.3, 2.15, c["input_band"], ec=TEAL, fc=TEAL_BG,
             size=12.5, color=GRAY)
    lf, _ = c["ladder_fig"]
    img_scaled(s, respath(lf), 8.95, 4.2, 4.0, 2.3)''',
'''    add_band(s, 0.45, 4.45, 12.4, 1.6, c["input_band"], ec=TEAL, fc=TEAL_BG,
             size=14, color=GRAY)''')

# ---- ly_three_panel_bifurcation: band fits text, type up (F-20)
rep('''        add_text(s, 0.6 + i * (w + 0.17), 2.35, w - 0.3, 0.5, verdict,
                 role="caption", size=14, color=col, bold=True)
        add_text(s, 0.6 + i * (w + 0.17), 2.95, w - 0.3, 1.2, sub,
                 role="caption", size=12, color=GRAY)
    add_band(s, 0.45, 4.5, 12.45, 1.85, c["honesty_band"], ec=RED,
             fc=WHITE, size=14, color=GRAY)''',
'''        add_text(s, 0.6 + i * (w + 0.17), 2.35, w - 0.3, 0.5, verdict,
                 role="caption", size=15, color=col, bold=True)
        add_text(s, 0.6 + i * (w + 0.17), 2.98, w - 0.3, 1.2, sub,
                 role="caption", size=12.5, color=GRAY)
    add_band(s, 0.45, 4.75, 12.45, 1.15, c["honesty_band"], ec=RED,
             fc=WHITE, size=14, color=GRAY)''')

# ---- ly_summary: legible miniature (F-23)
rep('    img_scaled(s, respath(f), 3.2, 5.6, 7.0, 1.15)',
    '    img_scaled(s, respath(f), 1.95, 5.52, 9.5, 1.6)')

# ---- ly_backup_table: real table (F-3)
rep('''def ly_backup_table(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    add_text(s, 0.7, 2.4, 12.0, 1.0, c["note_line"], role="body", size=18,
             italic=True)
    add_band(s, 0.7, 3.7, 12.0, 0.9,
             "content assembled from the record at Q&A-map time (Block 2)",
             ec=TEAL, fc=TEAL_BG, size=14, color=GRAY)
    return s, 0''',
'''def ly_backup_table(prs, fs, spec):
    s = title_and_content(prs, fs, spec)
    c = spec["content"]
    rows = [c["table_header"]] + [list(r) for r in c["table"]]
    add_table(s, 0.5, 1.75, 12.4, rows, col_widths=[1.5, 1.0, 1.0, 1.3, 1.4],
              body_size=12.5, row_h=0.5)
    add_text(s, 0.6, 5.6, 12.2, 0.6, c["note_line"], role="caption",
             size=13, color=LGRAY, italic=True)
    return s, 0''')

# ---- B1: question emphasis (F-16)
rep('''    if "b1_kicker_band" in ops:
        c = spec["content"]''',
'''    if "b1_kicker_band" in ops:
        c = spec["content"]
        for shp in slide.shapes:
            if shp.has_text_frame and "optimal" in shp.text_frame.text:
                for pp in shp.text_frame.paragraphs:
                    if "profile exist" in "".join(r.text for r in pp.runs):
                        for r in pp.runs:
                            r.font.color.rgb = TEAL
                            r.font.bold = True''')

open(p, "w", encoding="utf-8").write(s)
print(f"builder patched ({n0} -> {len(s)} chars)")
