# -*- coding: utf-8 -*-
"""Typography canon of the S-PRES deck (S4, CKP-S3-5(i) + CKP-S4-2).

Every value here is a MEASURED host-deck datum (probe: _probe_typography.py,
_probe_footerband.py, _probe_subtitles.py on the Heister-template host
slides, 2026-08-23) or a declared layout constant of the S4 rework — named
here once so the builder derives from them instead of carrying magic
numbers (numeric lint R28: validation ratchet tier, "classify or derive").
Units: inches unless the name says pt.
"""

# --- title identity (host canon: 32 pt bold RED textbox at (0.32, 0.38)) ---
TITLE_LEFT_IN = 0.32          # measured host textbox left
TITLE_TOP_IN = 0.38           # measured host textbox top (host s03/s06-s13)
TITLE_W_IN = 12.7             # full-width box (slide 13.33 - 2*0.32)
TITLE_H_IN = 0.95             # two 32-pt lines + leading, TOP-anchored
TITLE_PT = 32                 # measured host title size
TITLE_ZONE_TOP_IN = 1.2       # a text shape above this line is title-zone
SUBTITLE_ZONE_TOP_IN = 1.3    # host teal sub-heads sit at 0.83-1.14
SUBTITLE_PT = 28              # host sub-head canon (majority 28, bold)
SUBTITLE_PT_MIN = 24          # sub-head detection band (24-30 pt)
SUBTITLE_PT_MAX = 30
TITLE_MIN_PT = 28             # detection floor for a title-class run

# --- footer texts (host canon: MIDDLE-anchored inside the red band) ---
BAND_TOP_IN = 6.71            # measured 'Rectangle 23' (red band) top
BAND_H_IN = 0.81              # measured red band height (6.71 -> 7.52)
FOOT_LABEL_LEFT_IN = 1.57     # measured 'Segnaposto pie di pagina' left
FOOT_LABEL_W_IN = 7.48        # measured width
FOOT_TEAM_LEFT_IN = 9.06      # measured 'Segnaposto data' left
FOOT_TEAM_W_IN = 2.2          # measured width
FOOT_PT = 14                  # measured footer text size
GEOM_TOL_IN = 0.02            # host EMU are not round: assert tolerance

# --- S4 layout constants (declared, not measured) ---
DIVIDER_TITLE_TOP_IN = 3.0    # "Backup Slides" centered title
DIVIDER_TITLE_H_IN = 1.2
DIVIDER_PT = 40
ROADMAP_GAPLINE_TOP_IN = 4.95
ROADMAP_KILL_TOP_IN = 5.7
ROADMAP_KILL_H_IN = 0.68
ROADMAP_CLOSING_TOP_IN = 6.45
ROADMAP_CLOSING_H_IN = 0.3
SUMMARY_FIG_LEFT_IN = 1.35
SUMMARY_FIG_TOP_IN = 4.45
SUMMARY_FIG_MAXW_IN = 10.6
SUMMARY_FIG_MAXH_IN = 1.42
SUMMARY_BAND_TOP_IN = 5.98
SUMMARY_BAND_H_IN = 0.68
