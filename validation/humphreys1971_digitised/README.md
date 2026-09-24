# Humphreys, Thompson & Hoffman 1971 -- Fig. 4 digitised

Source: AIAA J 9(8):1581-1587, Fig. 4 "Optimum contour" (p. 1585, top left). The curves are only
plotted in the paper; the printed facts are on p. 1586: two contours of the same length as the
optimum, 0.5 in above and 0.5 in below it at D, with thrusts 32,556 lbf (upper) and 32,601 lbf
(lower) against 32,881 lbf for the optimum (`humphreys1971_tables.json`, key `_fig4`).

Digitised by the owner on 2026-09-23 from a 600-dpi crop of the page. The originals are in
`RDE/codes/GENO/literature/Fig 4/`, with decimal commas and `;` separators. They are converted
here verbatim to `x y` in inches, the format of `dutton1982_digitised/`:

| file | original | curve |
|---|---|---|
| `fig4_optimum.csv` | Optimum Contour.csv | solid: their optimum (Table 2) |
| `fig4_upper.csv` | Comparison Contour 2.csv | dashed, ends 0.5 in ABOVE the optimum at D |
| `fig4_lower.csv` | Comparison Contour 1.csv | dashed, ends 0.5 in BELOW the optimum at D |

The last points of each file lie on the vertical base line at D, as digitised. The reader
(`a1_throat_posing.py`, stage `fig4`) drops them.

The digitised optimum reads Table 2 with an rms of 0.046 in. The error grows towards the tail,
so it is a calibration error common to the three curves; the reader cancels it by marching
Table 2 plus the digitised DIFFERENCE between each comparison curve and the digitised optimum.
