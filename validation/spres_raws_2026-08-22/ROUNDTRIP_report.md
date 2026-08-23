# ROUND-TRIP fidelity report — ppt_Heister.pptx (S-PRES Block 0)

Command of record: python validation/spres_raws_2026-08-22/roundtrip_test.py
Env: python-pptx 1.0.2 (pinned fingerprint openSPRES).

SOURCE: 149 zip parts; classes [('layout', 2), ('master', 1), ('media', 49), ('notes', 18), ('other', 58), ('slide', 18), ('theme', 3)]
SOURCE pptx stats: {'n_slides': 18, 'n_masters': 1, 'n_layouts': 2, 'w_emu': 12192000, 'h_emu': 6858000}

T0 (open->save): 149 parts; classes [('layout', 2), ('master', 1), ('media', 49), ('notes', 18), ('other', 58), ('slide', 18), ('theme', 3)]
T0 stats: {'n_slides': 18, 'n_masters': 1, 'n_layouts': 2, 'w_emu': 12192000, 'h_emu': 6858000}
T0 parts LOST vs source (0): []
T0 parts GAINED vs source (0): []

T1 layouts available (2): [(0, 0, 'Diapositiva titolo'), (0, 1, 'Titolo e contenuto')]
T1: added slide on layout [0][1] 'Titolo e contenuto'; title set: True
T1 (open->add->save): 151 parts; classes [('layout', 2), ('master', 1), ('media', 49), ('notes', 18), ('other', 59), ('slide', 19), ('theme', 3)]
T1 stats: {'n_slides': 19, 'n_masters': 1, 'n_layouts': 2, 'w_emu': 12192000, 'h_emu': 6858000}
T1 parts LOST vs source (0): []
T1 parts GAINED vs source (2): ['ppt/slides/_rels/slide19.xml.rels', 'ppt/slides/slide19.xml']

## VERDICT
PASS — no content part lost, counts preserved, extension slide landed.
