# -*- coding: utf-8 -*-
"""S-PRES deck build primitives.

Reuses the host pipeline's idioms (project_build/scripts/decklib.py,
READ-ONLY import) and adds: footer-band copy with image rels, title
placeholders on new slides (style pact E: outline/accessibility),
role-typed text helpers that ENFORCE the font floors (body >= 18 pt,
caption >= 12 pt, citation 9-10 pt) so the build can assert them.
"""
import copy
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# repo root = ...\rde-lecture-code ; host pipeline lives beside the repo
_REPO = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_PB_SCRIPTS = os.path.abspath(os.path.join(_REPO, "..", "project_build", "scripts"))
sys.path.insert(0, _PB_SCRIPTS)

from decklib import (  # noqa: E402  (read-only import of host idioms)
    RED, TEAL, GRAY, LGRAY, WHITE, FONT, parse_rich, _apply_subsup,
)
from pptx import Presentation  # noqa: E402
from pptx.util import Inches, Pt, Emu  # noqa: E402
from pptx.dml.color import RGBColor  # noqa: E402
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR  # noqa: E402
from pptx.enum.shapes import MSO_SHAPE  # noqa: E402
from pptx.oxml.ns import qn  # noqa: E402

AMBER = RGBColor(0xB8, 0x86, 0x0B)
ZEBRA = RGBColor(0xF2, 0xEC, 0xED)
TEAL_BG = RGBColor(0xE8, 0xF1, 0xF2)
RED_BG = RGBColor(0xF6, 0xEC, 0xEE)

TEMPLATE = os.path.join(_REPO, "reference_presentations", "ppt_Heister.pptx")
FIG = os.path.join(_HERE, "figs") + os.sep
FIGP = os.path.join(_HERE, "figs_paper") + os.sep
EQ = os.path.join(_HERE, "eqs") + os.sep
GRAPH = os.path.join(_HERE, "graph") + os.sep

# role-typed font floors (style pact E, machine-assertable)
# title = 32 (host canon, CKP-S3-5(i): one title identity everywhere)
ROLE_SIZES = dict(body=18, body_big=20, caption=12, chip=13, cite=10,
                  head=15, kicker=24, title=32)

# typography canon (CKP-S3-5(i), measured from the host deck 2026-08-23):
# titles 32 pt bold RED at (0.32, 0.38); footer texts on the red band at
# top 6.76 — label left-aligned at 1.57, team CENTERED in its box at 9.06.
TITLE_LEFT, TITLE_TOP = 0.32, 0.38
# footer texts: same box as the red band (6.71 x 0.81), MIDDLE-anchored —
# the band's page number is MIDDLE-anchored, so all three center together
FOOT_TOP, FOOT_H, FOOT_LABEL_LEFT, FOOT_TEAM_LEFT = 6.71, 0.81, 1.57, 9.06
_SIZE_LOG = []   # (slide_idx_hint, role, size) — consumed by build asserts


def respath(rel):
    """Resolve a spec-relative resource path ('figs/x.png', '../../y.png')."""
    return os.path.normpath(os.path.join(_HERE, rel))


# --------------------------------------------------------------- text core
def add_text(slide, left, top, width, height, runs, role="body", size=None,
             color=GRAY, bold=False, align=PP_ALIGN.LEFT, italic=False,
             font=FONT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0,
             space_after=4, wrap=True):
    if size is None:
        size = ROLE_SIZES[role]
    floor = {"body": 18, "body_big": 18, "caption": 12, "chip": 12,
             "cite": 9, "head": 12, "kicker": 20, "title": 28}[role]
    assert size >= floor, f"role {role} below floor: {size} < {floor}"
    _SIZE_LOG.append((role, size))
    tb = slide.shapes.add_textbox(Inches(left), Inches(top),
                                  Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, Emu(0))
    if isinstance(runs, str):
        runs = [[(runs, {})]]
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        p.space_before = Pt(0)
        if line_spacing:
            p.line_spacing = line_spacing
        if isinstance(para, str):
            para = [(para, {})]
        # hanging indent for bulleted paragraphs (host-deck idiom)
        first = para[0][0] if para and isinstance(para[0], tuple) else ""
        if first.strip().startswith(("•", "–")):
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(int(Inches(0.28))))
            pPr.set("indent", str(-int(Inches(0.28))))
        for txt, ov in para:
            base = ov.get("size", size)
            for frag, kind in parse_rich(txt):
                if frag == "":
                    continue
                r = p.add_run()
                r.text = frag
                r.font.name = ov.get("font", font)
                r.font.bold = ov.get("bold", bold)
                r.font.italic = ov.get("italic", italic)
                r.font.color.rgb = ov.get("color", color)
                _apply_subsup(r, kind, base)
    return tb


def add_kicker(slide, text, top=1.02):
    return add_text(slide, 0.37, top, 12.5, 0.5, text, role="kicker",
                    color=TEAL)


def add_cite(slide, text, top=6.36, left=0.5, width=12.33):
    return add_text(slide, left, top, width, 0.26, text, role="cite",
                    size=10, color=LGRAY, italic=True)


def add_img(slide, path, left, top, width=None, height=None):
    kw = {}
    if width:
        kw["width"] = Inches(width)
    if height:
        kw["height"] = Inches(height)
    assert os.path.exists(path), f"missing figure: {path}"
    return slide.shapes.add_picture(path, Inches(left), Inches(top), **kw)


def img_scaled(slide, path, left, top, max_w, max_h):
    """Place image fit inside (max_w, max_h), centered in that box."""
    from PIL import Image
    with Image.open(path) as im:
        w, h = im.size
    ar = w / h
    bw, bh = max_w, max_w / ar
    if bh > max_h:
        bh, bw = max_h, max_h * ar
    return add_img(slide, path, left + (max_w - bw) / 2,
                   top + (max_h - bh) / 2, width=bw)


def bullets(items, size=18, marker=True):
    out = []
    for it in items:
        if isinstance(it, str):
            it = (it, 0, False, GRAY)
        txt, lvl, bold, color = (tuple(it) + (0, False, GRAY))[:4]
        pre = "   " * lvl + ("•  " if marker and lvl == 0 else ("–  " if marker else ""))
        out.append([(pre, {"color": RED, "size": size, "bold": False}),
                    (txt, {"color": color, "size": size, "bold": bold})])
    return out


def add_table(slide, left, top, width, rows, col_widths=None,
              header_fill=RED, body_size=13, header_size=13.5, row_h=0.34):
    nr, nc = len(rows), len(rows[0])
    gt = slide.shapes.add_table(nr, nc, Inches(left), Inches(top),
                                Inches(width), Inches(row_h * nr))
    tbl = gt.table
    tbl.first_row = True
    tbl.horz_banding = False
    if col_widths:
        tot = sum(col_widths)
        for j, w in enumerate(col_widths):
            tbl.columns[j].width = Inches(width * w / tot)
    for i, row in enumerate(rows):
        tbl.rows[i].height = Inches(row_h)
        for j, val in enumerate(row):
            c = tbl.cell(i, j)
            c.margin_left = Inches(0.06)
            c.margin_right = Inches(0.05)
            c.margin_top = Inches(0.02)
            c.margin_bottom = Inches(0.02)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = c.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if j > 0 else PP_ALIGN.LEFT
            c.fill.solid()
            if i == 0:
                c.fill.fore_color.rgb = header_fill
            else:
                c.fill.fore_color.rgb = ZEBRA if i % 2 == 0 else WHITE
            base = header_size if i == 0 else body_size
            for frag, kind in parse_rich(str(val)):
                if frag == "":
                    continue
                r = p.add_run()
                r.text = frag
                r.font.name = FONT
                if i == 0:
                    r.font.bold = True
                    r.font.color.rgb = WHITE
                else:
                    r.font.color.rgb = GRAY
                    if j == 0:
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(0x00, 0x4D, 0x59)
                _apply_subsup(r, kind, base)
    _SIZE_LOG.append(("caption", body_size))
    return gt


def add_card(slide, left, top, w, h, head, body, ec=TEAL, fc=None,
             head_color=None, head_size=15, body_size=13, body_color=GRAY):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(left), Inches(top), Inches(w), Inches(h))
    sh.adjustments[0] = 0.06
    sh.fill.solid()
    sh.fill.fore_color.rgb = fc or WHITE
    sh.line.color.rgb = ec
    sh.line.width = Pt(1.6)
    sh.shadow.inherit = False
    add_text(slide, left + 0.14, top + 0.10, w - 0.28, 0.4, head,
             role="head", size=head_size, color=head_color or ec, bold=True)
    if body:
        add_text(slide, left + 0.14, top + 0.52, w - 0.28, h - 0.62, body,
                 role="caption", size=body_size, color=body_color,
                 line_spacing=1.02, space_after=2)
    return sh


def add_band(slide, left, top, w, h, text, ec=RED, fc=RED_BG, size=14,
             color=GRAY, bold=False, align=PP_ALIGN.LEFT):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(left), Inches(top), Inches(w), Inches(h))
    sh.adjustments[0] = 0.10
    sh.fill.solid()
    sh.fill.fore_color.rgb = fc
    sh.line.color.rgb = ec
    sh.line.width = Pt(1.4)
    sh.shadow.inherit = False
    add_text(slide, left + 0.16, top + 0.08, w - 0.32, h - 0.16, text,
             role="caption", size=size, color=color, bold=bold, align=align,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05, space_after=2)
    return sh


def add_arrow(slide, x1, y1, x2, y2, color=GRAY, weight=2.2):
    conn = slide.shapes.add_connector(2, Inches(x1), Inches(y1),
                                      Inches(x2), Inches(y2))
    conn.line.color.rgb = color
    conn.line.width = Pt(weight)
    le = conn.line._get_or_add_ln()
    he = le.makeelement(qn("a:tailEnd"), {"type": "triangle"})
    le.append(he)
    return conn


# ------------------------------------------------------- slide scaffolding
_RE_EMBED = re.compile(r'r:(?:embed|link)="(rId\d+)"')


def _copy_rels_for_element(src_slide, dst_slide, el_xml):
    """Copy image/media rels referenced by an element's xml into dst,
    remapping rIds if taken; returns {old_rId: new_rId}."""
    remap = {}
    for rid in set(_RE_EMBED.findall(el_xml)):
        rel = src_slide.part.rels[rid]
        if rel.is_external:
            new_rid = dst_slide.part.rels.get_or_add_ext_rel(
                rel.reltype, rel.target_ref)
        else:
            new_rid = dst_slide.part.relate_to(rel.target_part, rel.reltype)
        remap[rid] = new_rid
    return remap


def copy_shape(src_slide, dst_slide, shape):
    """Deepcopy one shape (incl. groups/pictures) with its image rels."""
    el = copy.deepcopy(shape._element)
    xml = el.xml if isinstance(el.xml, str) else el.xml.decode()
    remap = _copy_rels_for_element(src_slide, dst_slide, xml)
    if remap:
        s = xml
        for old, new in remap.items():
            s = s.replace(f'r:embed="{old}"', f'r:embed="{new}"')
            s = s.replace(f'r:link="{old}"', f'r:link="{new}"')
        from pptx.oxml import parse_xml
        el = parse_xml(s)
    dst_slide.shapes._spTree.append(el)
    return el


def new_slide(prs, footer_src_slide, title_text, kicker=None):
    """New slide on the 'Titolo e contenuto' layout: real title
    placeholder (accessibility, style pact E), footer band copied from
    a host slide, content placeholder removed."""
    layout = prs.slide_masters[0].slide_layouts[1]
    s = prs.slides.add_slide(layout)
    for ph in list(s.placeholders):
        keep_title = (ph.placeholder_format.idx == 0
                      or "titolo" in ph.name.lower())
        if not keep_title:
            ph._element.getparent().remove(ph._element)
    # title placeholder, repositioned & styled to host visual identity
    t = s.shapes.title
    t.left, t.top = Inches(TITLE_LEFT), Inches(TITLE_TOP)
    t.width, t.height = Inches(12.7), Inches(0.95)
    tf = t.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = title_text
    r.font.size = Pt(ROLE_SIZES["title"])
    r.font.bold = True
    r.font.name = FONT
    r.font.color.rgb = RED
    _SIZE_LOG.append(("title", ROLE_SIZES["title"]))
    # footer band (Gruppo 6) copied from host slide; HEM residual cleaned
    for shp in footer_src_slide.shapes:
        if shp.name == "Gruppo 6":
            copy_shape(footer_src_slide, s, shp)
    _clean_hem(s)
    if kicker:
        add_kicker(s, kicker)
    return s


def _iter_text_shapes(shape):
    if shape.shape_type == 6:  # group
        for sub in shape.shapes:
            yield from _iter_text_shapes(sub)
    elif getattr(shape, "has_text_frame", False):
        yield shape


def _clean_hem(slide):
    for shp in slide.shapes:
        for ts in _iter_text_shapes(shp):
            if "HEM" in ts.text_frame.text:
                for p in ts.text_frame.paragraphs:
                    for r in p.runs:
                        r.text = ""


def fix_page_total(slide, total):
    """Replace the literal '/18' page-total (band field or placeholder)
    with '/<total>' everywhere on the slide, groups included."""
    for shp in slide.shapes:
        for ts in _iter_text_shapes(shp):
            if "/18" in ts.text_frame.text:
                for p in ts.text_frame.paragraphs:
                    for r in p.runs:
                        if "/18" in r.text:
                            r.text = r.text.replace("/18", f"/{total}")


def add_footer_texts(slide):
    """Footer texts for NEW slides (placeholders removed): foot label +
    team, white bold 14 pt on the red band. Geometry/alignment replicate
    the HOST footer placeholders exactly (CKP-S3-5(i) istanza 2, measured:
    top 6.76; label left at 1.57; team CENTERED in its 2.2-in box at 9.06)."""
    add_text(slide, FOOT_LABEL_LEFT, FOOT_TOP, 7.48, FOOT_H,
             "Rotating Detonation Engine Activities", role="caption",
             size=14, color=WHITE, bold=True, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, FOOT_TEAM_LEFT, FOOT_TOP, 2.2, FOOT_H, "T(H)RUST team",
             role="caption", size=14, color=WHITE, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def set_footer(slide, page, total, foot_text="Rotating Detonation Engine Activities"):
    for shp in slide.shapes:
        nm = shp.name
        if not shp.has_text_frame:
            continue
        if "numero" in nm:
            shp.text_frame.clear()
            p = shp.text_frame.paragraphs[0]
            r = p.add_run()
            r.text = f"{page}/{total}"
            r.font.size = Pt(14); r.font.bold = True
            r.font.color.rgb = WHITE; r.font.name = FONT
        elif "pi" in nm and "pagina" in nm:
            shp.text_frame.clear()
            p = shp.text_frame.paragraphs[0]
            r = p.add_run()
            r.text = foot_text
            r.font.size = Pt(14); r.font.bold = True
            r.font.color.rgb = WHITE; r.font.name = FONT
        elif nm.startswith("Segnaposto data"):
            shp.text_frame.clear()
            p = shp.text_frame.paragraphs[0]
            r = p.add_run()
            r.text = "T(H)RUST team"
            r.font.size = Pt(14); r.font.bold = True
            r.font.color.rgb = WHITE; r.font.name = FONT


def ensure_footer_placeholders(prs, slide, like):
    """New slides from layout already carry footer phs; make sure text set."""
    pass


def move_slide(prs, slide, new_index):
    xml_slides = prs.slides._sldIdLst
    slides = list(xml_slides)
    for sld in slides:
        if prs.slides._sldIdLst is not None:
            pass
    # find the sldId element whose rId resolves to this slide part
    target = None
    for sld in slides:
        rId = sld.get(qn("r:id"))
        if prs.part.related_part(rId) is slide.part:
            target = sld
            break
    xml_slides.remove(target)
    xml_slides.insert(new_index, target)


def set_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text
