# -*- coding: utf-8 -*-
"""CKP-S3-3/-4 patch: method-flow wiring + slide cuts (51->45 main).
Cuts go through the DECLARED cut-list: to_backup flag routes the spec
after the backup section; residue lines added to C1/C11; merges
C3-bis->C3, C13-pre->C13, C17-bis->C18 with notes absorbed."""
from _patch_ckps31_a import patch

# ---------------- specs_c12.py ----------------
patch("specs_c12.py", [
 # C2 -> backup (cut-pos 4), residue line in C1
 ('        id="C2", kind="new", layout="c2_throat", minutes=1.0, cut="pos4",',
  '        id="C2", kind="new", layout="c2_throat", minutes=0, cut="pos4", to_backup=True,'),
 ('''            bullets=[
                "Instantaneous: a rotating oblique shock. Averaged: a clean axisymmetric plume.",
                "Four independent codes, same phenomenology.",
            ],''',
  '''            bullets=[
                "Instantaneous: a rotating oblique shock. Averaged: a clean axisymmetric plume.",
                "Four independent codes, same phenomenology.",
                "Even the throat is unsteady: a corrugated sonic surface, ~6:1 excursions — we design downstream of it.",
            ],'''),
 # C3-bis -> merged into C3: table goes to backup, claim goes to C3 band
 ('        id="C3-bis", kind="new", layout="table_claim", minutes=1.5, cut="no",',
  '        id="C3-bis", kind="new", layout="table_claim", minutes=0, cut="merged-into-C3", to_backup=True,'),
 ('            takeaway="Best of a sweep is not an optimum: none of the four closes the loop.",',
  '''            takeaway=("Best of a sweep is not an optimum — and in a systematic census, no published "
                      "work poses the optimum on the real RDE exhaust: the substitution error is never "
                      "quantified."),'''),
 # C12 -> backup (cut-pos 7), residue in C11
 ('        id="C12", kind="new", layout="fig_bullets", minutes=1.0, cut="pos7",',
  '        id="C12", kind="new", layout="fig_bullets", minutes=0, cut="pos7", to_backup=True,'),
 ('''            bullets=[
                "Channels do not sum. Best case: single-digit %; off-axis, >10% not excluded.",
                "Our one in-class number: +0.51% ± ~30% — Rao's classical scale: 0.04–0.34%.",
                "No external referee exists: we close the bracket, or it stays open.",
            ],''',
  '''            bullets=[
                "Channels do not sum. Best case: single-digit %; off-axis, >10% not excluded.",
                "Largest adverse marker, published: +13 points of ideal from a shroud at fixed area ratio — unexplained (Paxson & Miki 2022).",
                "Our one in-class number: +0.51% ± ~30% — Rao's classical scale: 0.04–0.34%.",
                "No external referee exists: we close the bracket, or it stays open.",
            ],'''),
])

# ---------------- specs_c34.py ----------------
s = open("specs_c34.py", encoding="utf-8").read()
# delete the whole C13-pre dict (merged into C13); locate block by markers
start = s.index("    # -------------------------------------------------------------- C13-pre")
end = s.index("    # -------------------------------------------------------------- C13-val")
s = s[:start] + s[end:]
open("specs_c34.py", "w", encoding="utf-8").write(s)
print("C13-pre removed (merged into C13)")

patch("specs_c34.py", [
 # C13: method-flow figure + absorbed C13-pre speech/provenance
 ('        id="C13", kind="new", layout="graph_l0", minutes=1.5, cut="no",',
  '        id="C13", kind="new", layout="graph_l0", minutes=2.0, cut="no",'),
 ('            fig=("graph/L0_slide.png", None),  # light slide variant (user pin + guard 18); dense L0_ribbon -> backup',
  '            fig=("figs/fig_method_flow.png", None),  # CKP-S3-3: method flow; dense graphs -> backup'),
 ('''        notes=(
            "SCRIPT: The whole machine in one ribbon: contract, "
            "representation, march, certificates, estimation, optimization, "
            "aggregation, verdict. Every box you see carries registered "
            "choices - each with weighed alternatives and a falsifier - and "
            "the graph shows the undecided ones too, with owner and window. "
            "That last property is the field comparison: no published "
            "design method ships inside a chain built to reject it.\\n"''',
  '''        notes=(
            "SCRIPT: The machine, end to end. Engine data give the cycle at "
            "the interface - one state per phase. We form the cycle-averaged "
            "thrust of the shared contour: that integral IS the objective. A "
            "fast supersonic march solves each phase. Then the adjoint - and "
            "here is why: ONE extra backward solve returns the exact "
            "gradient of the objective with respect to ALL wall parameters "
            "at once; it is Hoffman's 1967 multiplier fields, made exact for "
            "the discrete problem (identity verified at machine precision). "
            "A trust-region Newton with measured curvature updates the "
            "contour - robust where curvature is irregular, with steps you "
            "can certify. And nothing ships alone: independent checks that "
            "can reject, error bars attached. Iterations take seconds.\\n"
            "[CKP-S3-3/-4 wired] C13-pre MERGED here (user cut order): its "
            "four concepts (adjoint / discrete-exact / optimizer / "
            "certificate) live in the flow blocks and this script; its "
            "provenance rows absorbed below. Status-graphs -> backup only.\\n"
            "[PROVENANCE - absorbed from C13-pre] reverse-AD = transposed "
            "adjoint -> CH9-feed-4 (THEOREM T-LEMB; mesh-limit SCHEMA "
            "S-LBML); continuous-first / per-role AD -> CH2-feed-5 (C56 "
            "CLOSED; O3.1 PRACTICE); optimizer adjudication -> C31 card "
            "(full card in backup).\\n"''')
])

patch("specs_c34.py", [
 # C14 -> plain cards, no fig
 ('''        content=dict(
            # light slide variant (user pin + guard 18): speaking-language
            # cards, no C-ids; the 3 dense DERISK panels live in backup D1-D8
            fig=("graph/L1_stage6_slide.png", None),
            bullets=[
                "The driver: segmented trust-region Newton on an exact gradient.",
                "Declared: this cluster is re-examined at next phase entry — 2026 candidate named, comparison pre-registered.",
            ],
        ),''',
  '''        content=dict(
            cards=[
                ("Why Newton with a trust region",
                 "curvature along these designs is irregular: measured curvature and a certifiable step beat quasi-Newton guesses"),
                ("Exact gradient underneath",
                 "the adjoint gradient is exact for the discrete problem — the optimizer never chases noise"),
                ("What we will re-examine",
                 "at next phase entry: a 2026 solver candidate, comparison pre-registered at equal constraints — the solver census is dated, and we say so"),
            ],
        ),'''),
 ('        id="C14", kind="new", layout="graph_stage6", minutes=1.5, cut="no",',
  '        id="C14", kind="new", layout="cards3", minutes=1.5, cut="no",'),
 # C15 -> backup with the dense stage 4-5 graph
 ('        id="C15", kind="new", layout="graph_certs", minutes=1.0, cut="pos2",',
  '        id="C15", kind="new", layout="graph_certs", minutes=0, cut="pos2", to_backup=True,'),
 ('            fig=("graph/L1_stage45_slide.png", None),  # light variant; dense L1_stage45 -> backup',
  '            fig=("graph/L1_stage45.png", None),  # dense: backup slide'),
 # C17-bis -> backup; C18 gains the open-items card
 ('        id="C17-bis", kind="new", layout="open_cards", minutes=1.0, cut="pos5",',
  '        id="C17-bis", kind="new", layout="open_cards", minutes=0, cut="pos5", to_backup=True,'),
 ('''                ("3 · Publication & procurement",
                 "WHAT: venues for the method papers + three key papers we cannot access",
                 "TO DECIDE: endorsement of channels",
                 "WHEN: at your convenience"),
            ],''',
  '''                ("3 · Publication & procurement",
                 "WHAT: venues for the method papers + three key papers we cannot access",
                 "TO DECIDE: endorsement of channels",
                 "WHEN: at your convenience"),
                ("What is still open — declared",
                 "mean-swirl route · one wall closure · data contract (choking hypothesis, owner named) · one gate threshold to be derived as a number",
                 "no decision requested today",
                 "said before you ask"),
            ],'''),
])
print("PATCH CKP-S3-3/-4 DONE")
