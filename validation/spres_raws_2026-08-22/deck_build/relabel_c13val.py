# -*- coding: utf-8 -*-
"""F-6 repair: presentation relabel of the C13-val record figure.
Data pixels untouched — only the title and the two legend TEXT areas are
overlaid with plain-English labels (internal ids GENO/S18/Brick-2/K_RICH
and the 91/91 count move to speaker notes per guard 18). Source record:
validation/brick2_profiles_record.png (S18 [X-TOCV]) — never modified;
output is a derived presentation copy, declared in BUILD_LOG.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "..", "brick2_profiles_record.png"))
OUT = os.path.join(HERE, "figs", "fig_c13val_clean.png")

im = Image.open(SRC).convert("RGB")
W, H = im.size
sx, sy = W / 1320.0, H / 1100.0   # measured boxes on the 1320-wide view


def box(x0, y0, x1, y1):
    return (int(x0 * sx), int(y0 * sy), int(x1 * sx), int(y1 * sy))


d = ImageDraw.Draw(im)
GRAY = (60, 60, 60)


def font(px):
    for name in ("pala.ttf", "georgia.ttf", "times.ttf"):
        try:
            return ImageFont.truetype(f"C:\\Windows\\Fonts\\{name}", int(px * sy))
        except OSError:
            continue
    return ImageFont.load_default()


# 1) title block
d.rectangle(box(95, 3, 1318, 78), fill="white")
d.text((int(120 * sx), int(12 * sy)),
       "The classical maximum-thrust benchmark, recovered by an independent route",
       font=font(24), fill=GRAY)
d.text((int(120 * sx), int(45 * sy)),
       "two routes, one contour — max deviation 1.9e-3 of throat radius, inside the derived band",
       font=font(21), fill=(110, 110, 110))

# 2) top-plot legend texts (keep the coloured sample strokes at left)
d.rectangle(box(736, 610, 1312, 678), fill="white")
d.text((int(742 * sx), int(616 * sy)), "classical construction (Rao)",
       font=font(19), fill=GRAY)
d.text((int(742 * sx), int(648 * sy)), "variational route (adjoint gradient)",
       font=font(19), fill=GRAY)

# 3) bottom-plot legend: full clean legend box (old text + samples covered,
#    samples redrawn inside)
d.rectangle(box(305, 736, 1312, 824), fill="white", outline=(205, 205, 205))
d.rectangle(box(322, 752, 362, 768), fill=(222, 226, 230))          # band sample
d.line(box(322, 796, 362, 796)[:2] + box(322, 796, 362, 796)[2:],
       fill=(31, 119, 180), width=int(4 * sy))                       # |dy| sample
d.text((int(378 * sx), int(748 * sy)), "independent cross-code tolerance band",
       font=font(18), fill=GRAY)
d.text((int(378 * sx), int(786 * sy)), "|dy| between the two routes",
       font=font(18), fill=GRAY)

im.save(OUT)
print("saved", OUT, im.size)
