# -*- coding: utf-8 -*-
"""Spine-wave repair patch: all 24 attack findings (accepted 24/0) —
spec-side edits. Builder-side edits in _patch_spine_builder.py."""
from _patch_ckps31_a import patch

# ---------------- specs_a.py ----------------
patch("specs_a.py", [
 # F-7: A15 native heading collides with in-body host header -> suppress ours
 ('        edits=["native_heading_a15"],',
  '        edits=[],  # F-7: host in-body header retained; added heading suppressed'),
 # F-17: A6 formula gloss caption
 ('            eq="eqs/eq_eap.png",',
  '''            eq="eqs/eq_eap.png",
            eq_caption="the field's accepted average: a thrust-equivalent pressure — no error bar",'''),
 # F-16: B1 speech duty (notes) + question emphasis handled in builder
 ('''            "SCRIPT: This slide closed the group deck; today it opens the main "''',
  '''            "SIGNPOST: agenda point 2 - the real RDE exhaust. SPEECH DUTY: "
            "read the open question aloud - 'Does an optimal profile exist "
            "for an RDE exhaust?' - as the question of the rest of this "
            "talk.\\n"
            "SCRIPT: This slide closed the group deck; today it opens the main "'''),
])

# ---------------- specs_c12.py ----------------
patch("specs_c12.py", [
 # F-8: C6 footline
 ('            footline="A 1975 Russian precedent is still in procurement: we say so.",',
  '            footline="A 1975 Russian precedent is still in procurement — not yet read against the original.",'),
 # F-19: C5 bullet 3 to speech
 ('''            bullets=[
                "Only the base-pressure model changes: the optimum moves ×2.45 (value: +0.26%).",
                "The same closure is still in use — and RDE hot-fire base pressure sits far from steady predictions: 0.59 vs 0.95 atm (Harroun et al. 2021).",
                "Our design contract demands unimodality, not flatness.",
            ],''',
  '''            bullets=[
                "Only the base-pressure model changes: the optimum moves ×2.45 (value: +0.26%).",
                "The same closure is still in use — and RDE hot-fire base pressure sits far from steady predictions: 0.59 vs 0.95 atm (Harroun et al. 2021).",
            ],'''),
 ('''            "[GLOSS - FD-3] 'truncated plug' = plug nozzle with the spike cut ''',
  '''            "[F-19] Third bullet moved to speech: 'this is why our design "
            "contract demands unimodality of the working variable, not "
            "flatness' - the flatness-to-fragility link is spoken, not "
            "printed.\\n"
            "[GLOSS - FD-3] 'truncated plug' = plug nozzle with the spike cut '''),
 # F-18 + F-22: C7-bis-pre punch card
 ('''                ("This programme",
                 "the variational optimum ON the family — never posed before"),''',
  '''                ("This programme",
                 "the variational optimum on the family — never posed before"),'''),
 # F-10 speech duty on C7-bis
 ('''            "SCRIPT: The heart slide. Left, the field's route - including the "''',
  '''            "SPEECH DUTY (F-10): stop and read the theorem band verbatim; "
            "then give the room its take-away: 'the cycle-optimal nozzle "
            "is optimal at no single operating point'.\\n"
            "SCRIPT: The heart slide. Left, the field's route - including the "'''),
 # F-9: C7-ter band wording
 ('''            honesty_band=("Its size at contouring is open — not presumed small (10:1 inlet, ~6:1 throat, "
                          "~20:1 combustor swings). The machine is ready: it is the first campaign of the "
                          "phase now opening."),''',
  '''            honesty_band=("Its size at contouring is open — not presumed small (10:1 inlet, ~6:1 throat, "
                          "~20:1 combustor swings). The machine is ready: it is the first campaign, "
                          "starting September."),'''),
 # F-14: C8-bis headline bullets + F-9 state line
 ('''            bullets=[
                "The design variable is a solid body in an envelope: bell, plug, shrouded, E–D emerge as classes of the result.",
                "Sectors are finitely many: the global optimum is a tournament among sector optima — every delivered optimum declares its guarantee and its strength.",
                "First verdict on record: at certified closures the plug weakly dominates the bell, tie region characterized — closures at equal area ratio, never hardware.",
                "Route: certified splines per sector, no level-sets — an infinitesimal body in supersonic flow pays only wave drag: sectors are compared whole.",
            ],
            state_line="Honest state: the driver exercises one sector today (bell, 9 DOF); the others have named owners and windows.",''',
  '''            bullets=[
                "Configurations emerge as classes of the result — not presupposed.",
                "The global optimum is a tournament among sector optima.",
                "First verdict: the plug weakly dominates the bell at certified closures.",
                "Certified splines per sector — no level-sets.",
            ],
            state_line="Honest state: the driver exercises one sector today (bell, 9 DOF); the others are assigned, with dates.",''',),
 ('''            "[GUARD 18] M1-M5/X-GRP ids in notes; on-slide 'declares its "
            "globality mechanism and its strength'."''',
  '''            "[F-14] Qualifier prose moved OFF-slide (spoken): the tournament "
            "verdict is a ranking between CLOSURES at equal area ratio, "
            "never between hardware; every delivered optimum declares its "
            "guarantee mechanism and strength; the no-level-set reason: an "
            "infinitesimal body in supersonic flow pays only wave drag, so "
            "whole sectors are compared.\\n"
            "[GUARD 18] M1-M5/X-GRP ids in notes."''',),
 # F-9: C10 campaign wording
 ('                "Both are measurable — the first campaign of the new phase measures them.",',
  '                "Both are measurable — the campaign starting now measures them.",'),
])

# ---------------- specs_c34.py ----------------
patch("specs_c34.py", [
 # F-2: C13 bullets + fig note; signpost in notes
 ('''            fig=("figs/fig_method_flow.png", None),  # CKP-S3-3: method flow; dense graphs -> backup
            bullets=[
                "Eight stages, data contract → verdict; adjudicated choices carry weighed alternatives and a test that can reject them — open ones are declared, with owner and window.",
                "No published design method ships inside a chain built to reject it.",
            ],''',
  '''            fig=("figs/fig_method_flow.png", None),  # CKP-S3-3: method flow; dense graphs -> backup
            fig_note="six stages shown — the full eight-stage engineering record is in backup",
            bullets=[
                "Every choice on a register, with alternatives and a test that can reject it — open choices declared, with a named lead and date.",
                "No published design method ships inside a chain built to reject it.",
            ],''',),
 ('''            "SCRIPT: The machine, end to end. Engine data give the cycle at "''',
  '''            "SIGNPOST: agenda point 4 - the design machine.\\n"
            "SCRIPT: The machine, end to end. Engine data give the cycle at "'''),
 # F-8: C14 census card
 ('''                ("What we will re-examine",
                 "at next phase entry: a 2026 solver candidate, comparison pre-registered at equal constraints — the solver census is dated, and we say so"),''',
  '''                ("What we will re-examine",
                 "a 2026 solver candidate, comparison pre-registered at equal constraints — the solver census is dated"),'''),
 # C13-val: relabeled presentation figure (F-6)
 ('''            fig=("../../brick2_profiles_record.png",   # validation/brick2_profiles_record.png (record S18)
                 "Variational contour vs classical Rao contour, with deviation panel — in-house, two independent routes"),''',
  '''            fig=("figs/fig_c13val_clean.png",  # F-6: presentation relabel of the record figure
                 "Variational contour vs classical Rao contour, with deviation panel — in-house, two independent routes"),'''),
 ('''            "[PROVENANCE - guard 15] Figure = validation/"
            "brick2_profiles_record.png, record run S18 [X-TOCV] (carrier "''',
  '''            "[F-6] On-slide figure = fig_c13val_clean.png: presentation "
            "relabel of the record figure (title + legend text plain-"
            "English; internal ids GENO/S18/K_RICH and the 91/91 count "
            "moved here; DATA PIXELS UNTOUCHED - relabel script "
            "relabel_c13val.py, declared in BUILD_LOG).\\n"
            "[PROVENANCE - guard 15] Source figure = validation/"
            "brick2_profiles_record.png, record run S18 [X-TOCV] (carrier "'''),
 # F-21: C16 title
 ('title="Speed was engineered, not found — validation becomes an economic act",',
  'title="Speed was engineered, not found — validation becomes affordable",'),
 # F-13: C16-bis scope + wording
 ('''                ("Audit 2 — hostile, commissioned", "verdict: not certifiable — two named defects; one repaired and declared, one with owner and deadline"),''',
  '''                ("Audit 2 — hostile, on the certification chain", "verdict: not certifiable — two named defects; one repaired and declared, one with a named lead and date"),'''),
 ('                "Across the audits, defects moved from the object to the certifier: the floor rose.",',
  '                "Across the audits, defects moved from the object to the certifier: the standard got stricter.",'),
 ('''            "SCRIPT: The slide I most want you to remember. We commissioned "''',
  '''            "SCOPE FIRST (speech duty, F-13): the audit judged our "
            "CERTIFIER, not the flow solutions - and it found the "
            "certifier wanting.\\n"
            "SCRIPT: The slide I most want you to remember. We commissioned "'''),
 # F-22: C17-pre caps
 ('''                ("mean-state design", "the comparator — which NOBODY has computed in this head-to-head, us included"),''',
  '''                ("mean-state design", "the comparator — which nobody has computed in this head-to-head, us included"),'''),
 # F-11c: C17-pre bands 3 -> 2
 ('''            hypothesis=("Working hypothesis (declared, falsifiable): at fixed constraints the formulation "
                        "gap dominates — three suppression results on the model gap, none on formulation."),
            heel=("Stated with its weak point: front jumps are unsuppressed — no number yet; if large, the "
                  "model gap can dominate."),''',
  '''            hypothesis=("Working hypothesis (declared, falsifiable): at fixed constraints the formulation "
                        "gap dominates — three suppression results on the model gap, none on formulation. "
                        "Its weak point, stated with it: front jumps are unsuppressed, no number yet — if "
                        "large, the model gap can dominate."),
            heel=None,'''),
 # F-9 + F-12: C17 card window + closing
 ('                 "phase just opened — September milestone"),',
  '                 "campaign starting now — September milestone"),'),
 ('            closing="Every outcome is pre-registered: we already know what we will conclude in each case.",',
  '            closing="Every outcome is pre-registered: the decision rule is fixed before the data arrive.",'),
 # F-4: C18 exactly 3 cards, open-items to notes; F-9 wording; F-8 band
 ('''                ("What is still open — declared",
                 "mean-swirl route · one wall closure · data contract (choking hypothesis, owner named) · one gate threshold to be derived as a number",
                 "no decision requested today",
                 "said before you ask"),
            ],''',
  '''            ],'''),
 ('                 "WHEN: within the phase now opening (milestone early/mid September)"),',
  '                 "WHEN: starting now — September milestone"),'),
 ('''            input_band=("'What input does your method need?' — Specs suffice to design; every extra datum "
                        "climbs a declared reliability ladder. Data is not fed in: it is ADMITTED — the entry "
                        "gate can say no. (A contract prediction, not yet exercised on real data; we say so.)"),
            ladder_fig=("figs/fig_c18_ladder.png", None),  # Annex B cases A-G compressed ladder''',
  '''            input_band=("'What input does your method need?' — Specs suffice to design; every extra datum "
                        "climbs a declared reliability ladder (full ladder in backup). Data is not fed in: "
                        "it is admitted — and the entry gate can say no. (A contract prediction — not yet "
                        "exercised on real data.)"),'''),
 ('''            "SCRIPT: Three asks, each decision-ready - what we ask, what "''',
  '''            "[F-4] Open-items card moved OFF-slide (three asks means three "
            "cards): still open, said if asked - mean-swirl route; one "
            "wall closure; data contract (choking hypothesis, named lead); "
            "one gate threshold to be derived as a number. Full open-items "
            "slide in backup. Reliability ladder: backup slide.\\n"
            "SCRIPT: Three asks, each decision-ready - what we ask, what "'''),
 # F-1 + F-21 + F-22: C19
 ('''            eng_bullets=[
                "the first per-phase variational design method for RDE nozzles",
                "what the reduction discards is an explicit, MEASURABLE operator",
                "an honest error bracket, channel by channel, each cell with its evidence level",
            ],''',
  '''            eng_bullets=[
                "the first per-phase variational design method for RDE nozzles",
                "what the reduction discards is an explicit, measurable operator",
                "an honest error bracket, channel by channel, each cell with its evidence level",
            ],'''),
 ('''            prog_bullets=[
                "validation campaigns as economic acts (minutes, not weeks)",
                "an incremental plan, already priced, with pre-registered outcomes — and a declared honest-death criterion",
            ],''',
  '''            prog_bullets=[
                "validation in minutes, not weeks",
                "an incremental plan, already priced, with pre-registered outcomes — and a declared stop criterion",
            ],'''),
 ('            fig=("graph/L0_slide.png", "signature"),  # miniature, light variant',
  '            fig=("figs/fig_method_flow.png", "signature"),  # F-2/F-23: same naming as C13, legible size'),
 # F-8 backup C17-bis card
 ('''                ("One gate still lacks a rejecting threshold",
                 "we will derive it as a NUMBER — and we say so in the meantime"),''',
  '''                ("One gate still lacks a rejecting threshold",
                 "we will derive it as a number"),'''),
 # C7 signpost (agenda point 3)
 ('''            "SCRIPT: After that chain, read the field's own conclusion - "''',
  '''            "SIGNPOST: agenda point 3 - our formulation.\\n"
            "SCRIPT: After that chain, read the field's own conclusion - "'''),
])

# ---------------- specs_d.py ----------------
patch("specs_d.py", [
 # F-3: real honesty table in backup D-F
 ('''        dict(
            id="D-F", kind="new", layout="backup_table", minutes=0, cut="backup",
            title="Backup — the honesty table, complete",
            content=dict(
                note_line=("all six channels with verbatim cells and evidence classes; "
                           "the main deck showed the highlights (C11) — this is the full record"),
            ),''',
  '''        dict(
            id="D-F", kind="new", layout="backup_table", minutes=0, cut="backup",
            title="Backup — the honesty table, complete",
            content=dict(
                note_line=("all six channels, best/worst, evidence class, and what tightens each — "
                           "the main deck showed the highlights (C11)"),
                table_header=["channel", "best case", "worst case", "evidence", "what tightens it"],
                table=[
                    ("Mean azimuthal residual", "exactly 0", "exactly 0", "theorem (declared perimeter)", "—"),
                    ("Swirl booking debt", "1.5% of thrust", "3% of thrust", "order estimate", "residual-measurement campaign"),
                    ("Data-fidelity biases", "0.6% of pressure", "9% of pressure", "order estimate + literature", "data contract + campaign"),
                    ("Front jumps (weak point)", "no number yet", "—", "declared open", "derivation chain, then campaign"),
                    ("Sizing level", "~1%", "~1%", "literature, page-verified", "paired coupled run"),
                    ("Optimum shift", "no number at any grade", "—", "declared open", "head-to-head comparison"),
                ],
            ),''',),
])

# F-4: ladder backup slide appended
s = open("specs_d.py", encoding="utf-8").read()
add = '''
SLIDES_D.append(dict(
    id="D-L", kind="new", layout="backup_graph", minutes=0, cut="backup",
    title="Backup — what input the method needs: the reliability ladder",
    content=dict(
        fig=("figs/fig_c18_ladder.png", None),
        note_line="cases A–G: from engine specs alone to class-verified hot-fire data — the entry gate can reject",
    ),
    notes=("Annex-B ladder moved from C18 (F-4: three asks = three cards; "
           "ladder legibility). Source: CH10-feed-1 specs ladder; entry "
           "gate G6 loud-reject (never exercised - said in C18 notes)."),
))
'''
if "D-L" not in s:
    open("specs_d.py", "a", encoding="utf-8").write(add)
    print("D-L ladder backup slide appended")
print("SPINE SPEC PATCH DONE")
