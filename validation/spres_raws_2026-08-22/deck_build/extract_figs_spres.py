#!/usr/bin/env python3
"""Extract original paper figures as high-res PNG crops for the S-PRES deck.

Sources are pre-rendered 250-dpi page PNGs (pdftoppm) living in
deck_build/tmp_pages/<tag>/. Each entry: name -> (page_png_relative_to_BUILD,
(left, top, right, bottom) in px). Boxes estimated visually on the 250-dpi
renders and verified crop-by-crop (same method as
project_build/scripts/extract_figs.py of the reference pipeline).

Page render sizes @250dpi:
  liu_2022 AST 120:107300 (pa)     : 2126 x 2815
  li_2023  AST 136:108221 (pb)     : 2126 x 2815
  li_2025  AST 158:109878 (pc)     : 2067 x 2756
  jourdaine_2019 PCI 37 (pd)       : 1688 x 2500
  kaemming_paxson_2018 AIAA (kp18) : 2125 x 2750
  paxson_miki_2022 (pm)            : 2125 x 2750
  humphreys_1971 AIAA J (hum)      : 2028 x 2848 (p6) / 2014 x 2841 (p7)
  rao_1958 Jet Propulsion (rao)    : 2139 x 2761

Run from anywhere:  python extract_figs_spres.py
"""
import os
from PIL import Image

BUILD = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BUILD, "figs_paper")

# name: (source page png, (l, t, r, b))
FIGS = {
    # --- P-A: Liu, Cheng, Zhang et al. 2022, AST 120:107300 ---
    "pa_ramp_profile":       ("tmp_pages/pa/pa250-05.png",   (1015, 760, 1866, 1170)),   # Fig 3(b): isentropic-ramp (Angelino) construction, p.5
    # --- P-B: Li, Xu, Lv, Lv, Song 2023, AST 136:108221 ---
    "pb_moc_profile":        ("tmp_pages/pb/pb250-08.png",   (185, 195, 1000, 880)),     # Fig 13: MoC truncated-spike construction (ST/KJ), p.8
    "pb_fig15_cfx":          ("tmp_pages/pb/pb250-10.png",   (1203, 978, 1892, 1702)),   # Fig 15 (+caption): C_fx steady vs transient, p.10
    "pb_fig16_feedback":     ("tmp_pages/pb/pb250-10.png",   (1140, 1731, 1899, 2392)),  # Fig 16: p0/T0 at combustor exit vs truncation, p.10
    # --- P-C: Li, Xu, Lv, Yu, Zhou 2025, AST 158:109878 ---
    "pc_fig10_dichotomy":    ("tmp_pages/pc/pc250-09.png",   (300, 175, 1760, 870)),     # Fig 10(a): transient (left) vs steady (right), p.9
    "pc_fig13_ranking":      ("tmp_pages/pc/pc250-11.png",   (1096, 179, 1964, 730)),    # Fig 13: C_fx transient vs steady bars, p.11
    "pc_fig21_lateral":      ("tmp_pages/pc/pc250-17.png",   (179, 179, 1805, 930)),     # Fig 21: lateral force magnitude+direction, p.17
    # --- P-D: Jourdaine, Tsuboi, Hayashi 2019, PCI 37:3443 ---
    "pd_setup_cone":         ("tmp_pages/pd/pd250-2.png",    (963, 173, 1419, 550)),     # Fig 1: conic aerospike domain, PDF p.2 (j. 3444)
    "pd_fig4":               ("tmp_pages/pd/pd250-5.png",    (231, 181, 1563, 694)),     # Fig 4: time-averaged exhaust, PDF p.5 (j. 3447)
    "pd_fig9":               ("tmp_pages/pd/pd250-7.png",    (169, 1356, 831, 1956)),    # Fig 9: instantaneous internal flow, PDF p.7 (j. 3449)
    # --- KP18: Kaemming & Paxson 2018, AIAA (EAP) ---
    "kp18_fig6_sonicline":   ("tmp_pages/kp18/kp18250-10.png", (570, 1546, 1553, 2300)), # Fig 6 (+caption): exit axial Mach crossing M=1, p.10
    "kp18_tab1_throat":      ("tmp_pages/kp18/kp18250-06.png", (522, 261, 1601, 756)),   # Table 1 (+title): throat/exit stats, ~6:1 Pt excursion, p.6
    # --- P-M: Paxson & Miki 2022, NASA Glenn / AIAA ---
    "pm_contour":            ("tmp_pages/pm/pm250-07.png",   (254, 1065, 1882, 1505)),   # Fig 6: time-avg p and Mach contours, baseline nozzle, p.7
    "pm_shroud_5871":        ("tmp_pages/pm/pm250-09.png",   (247, 1738, 1855, 2426)),   # Fig 10: nozzle thrust % ideal vs Ash/Ae (58.1 -> ~71.5), p.9
    # --- HUM: Humphreys, Thompson & Hoffman 1971, AIAA J 9(8) ---
    "hum_contour":           ("tmp_pages/hum/hum250-7.png",  (1044, 199, 1910, 568)),    # Fig 6: optimum contour, alternate base-pressure model, p.1587
    "hum_table":             ("tmp_pages/hum/hum250-7.png",  (121, 1910, 973, 2745)),    # Table 4 (+title): alternate-model contour coords, p.1587
    # --- RAO: Rao 1958, Jet Propulsion 28(6) ---
    "rao_eq14_transversality": ("tmp_pages/rao/rao250-3.png", (1245, 1001, 1926, 1119)), # Eq. [14] strip, journal p.379 (PDF p.3)
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (src, box) in FIGS.items():
        path = os.path.join(BUILD, src)
        im = Image.open(path)
        l, t, r, b = box
        l = max(0, l); t = max(0, t); r = min(im.width, r); b = min(im.height, b)
        crop = im.crop((l, t, r, b))
        out_path = os.path.join(OUT, name + ".png")
        crop.save(out_path)
        print(f"{name}: {crop.size[0]}x{crop.size[1]}  <- {os.path.basename(src)} {box}")


if __name__ == "__main__":
    main()
