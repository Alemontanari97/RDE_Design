# REFUTE — PIPELINE DECISION MAP (dual-proof adversarial pass)
# [PIANO/R35] S-FOUNDATIONS-C4, 2026-08-21. Role: MAP REFUTER.
# Object under attack: docs/rde_nozzle_pipeline_decision_map.md
# (read IN FULL this window). The map is treated as a CLAIM OBJECT:
# every edge (40/40) and every load-bearing status/falsifier citation
# verified at source in THIS window (SR-12; commands run 2026-08-21).

## 0. VERIFICATION PROTOCOL EXECUTED (measured this window)

- Ledger recount: `grep -c "^- id: C" docs/choice_ledger.yaml` = 62;
  `grep -o "^  status: .*" | sort | uniq -c` = 12 DECIDED / 36 MIXED /
  12 NEVER / 2 SINGLE-AUTHOR. Both REPRODUCE the map's SR-12 lines.
- Per-row status identity: id-by-id awk extraction; the machine
  summary's four rosters match the ledger EXACTLY (DECIDED 12 incl.
  C46; MIXED 36 incl. C49/C50/C56/C58; NEVER 12 = C25 C38 C51-C55
  C57 C59-C62; SA 2 = C17 C18). Zero contradictions.
- Node sweep (attack iii): 61 ledger rows appear in stage tables
  (C1-C45 less C46, C47-C62; C55 and R22-CFD declared two-faced,
  counted once); C46 = the single non-listed row, DECLARED with
  reason in `note_C46` (padding policy, engine-internal; evidence
  field verified against ledger C46). 62/62 accounted. Non-ledger
  roster 17/17 matches the ⊘ rows of the stage tables.
- Edge sweep (attacks i/iv): ALL 40 §9 entries verified at their
  quoted authorities (ledger owner/note fields read in full;
  findings :211-212 :300 :328 :599-607 :1468 :1607 :1643-1661 :1668
  :2092+:2100 :2148 :2163 :2299-2353 :2446-2452 :2498 :2509 :2519
  :2530; M0 :668 :977 :1257-1258 :1283 :1344-1345 :1348 :1884-1885
  :1947-1948 :1957 :2177-2178 :2224 :2265-2266 :2616 :3649 :3726
  :3742-3746 :3768 :3853; claims :617 :1900 :2044; literature :426;
  plan :435-438; problem book :348 :553; PROGRESS :390-400 :395;
  ledger header :20 :52-56 :82-83 :113-121 :150; census §3/§5; fork
  adjudication :119 D-1 (O15); diff :266 par.2.10; VERDICT_blocco2
  §4 (:272-297) §6 (:361-435) :330 :600; VERDICT_escalation_c4 §3
  §5.1-5.5 §7 R-ESC-4/R-ESC-5; VERDICT_r22f §4 heading; wave-verdict
  anchor existence greps 5/5). NO invented edge found; the named
  must-have edges (engine cluster A, contract cluster B, ship-gate
  E9, Veen→C61→ADR-D4 arc D incl. DUTY-10 E10/E14, D-44→S-PRES E31,
  P34→S-PRES E32) are ALL present and source-true.
- Stale-label check (attack v): C18/NTF, OBJ-DOM, DELTA-CARRIER,
  CLG labels compared clause-by-clause against VERDICT_escalation_c4
  §5.1-5.4 + machine summary: NTF-1/4 SCHEMA, NTF-2/3 THEOREM*,
  NTF-5 PRACTICE; OBJDOM-1/3 THEOREM, OBJDOM-2 THEOREM*; DC-1/2
  THEOREM*, DC-3 THEOREM (V1-V2), DC-4 THEOREM/SCHEMA-dormant, DC-5
  PRACTICE, DC-6 SCHEMA; CLG-D2 THEOREM*, D5 THEOREM*/SCHEMA-cond-H8,
  D4-ALT CONJECTURE. ALL CURRENT — zero stale labels. Ship-gate
  wording ("[OBJ-DOM-IMPL] landed and used on both sides, OR the
  net-panel band included"; SATISFIED §3, ARMED for F2 rows) is the
  §3 text verbatim. Forchetta worst-direction marker verified IN the
  tail of M0:1345 ("58.1% → ~71.5% of the notional ideal at FIXED
  area ratio"), so the map's anchor is correct despite the duplicate
  at M0:1490.

## 1. FINDINGS

### PM-1 — AMENDMENT (plan-slot precision: DUTY-10(a) is F5b, not F5)
Map (Stage-8 DUTY-10 row + E14): "DUTY-10(a) base forced-response
validity = F5 ... (`docs/rde_nozzle_development_plan.md:436-438`)".
Measured: the plan block at :435-437 slots DUTY-10(a) under **F5b**
(":435 `F5b : DUTY-4(ii) ... :436 derivation; DUTY-10(a) base
forced-response validity :437 note.`"); F5a is a distinct sibling
slot (:425). "F5" is the coarse phase family, not the slot of record.
Fix: write "F5b" in the DUTY-10 row and in E14. No verdict moves.

### PM-2 — AMENDMENT ("verbatim" enum claim is not verbatim)
Map header: "STATUS ENUM (verbatim from `docs/choice_ledger.yaml`
header): `DECIDED` | `MIXED` | `NEVER` | `SA` (= SINGLE-AUTHOR)".
Ledger :20 reads "status: DECIDED | MIXED | SINGLE-AUTHOR | NEVER"
— different order, and the literal token is SINGLE-AUTHOR (never
"SA"). Content-equivalent, but the word "verbatim" is false as
written and the map's own recount line correctly prints
"2 SINGLE-AUTHOR". Fix: drop "verbatim" or quote in header order
with SA declared as this map's abbreviation.

### PM-3 — AMENDMENT (C61: WG10-FAILED sits in the choice field, not
the alternatives field)
Map C61 conditions cell: "WG10-FAILED noted in the row's alternatives
field". Ledger C61: the token "WG10-FAILED" is in the CHOICE field
("Veen 0.846p/M^1.3 (legacy-practiced, WG10-FAILED)") and the failure
fact in the note ("FAILED by WG10 + Humphreys 1971 exhibit"); the
alternatives field carries the WG10 empirical BRACKET as an
alternative and the N2 "MUST REPLACE IT" verdict. Fix: re-point the
field name. Substance (Veen failed by WG10) is source-true.

### PM-4 — AMENDMENT (edge-id over-assignment in two Edges cells)
C28's Edges cell reads "E1 (surface)" and C31's cell includes E6, but
the §9 definitions bind E1 = C31↔C57 and E6 = C34→[P-IPADJ]; neither
definition names C28 (or makes C31 an E6 endpoint). The underlying
connections are REAL — C28's owner "[P-IPADJ] same critical path" and
C31's owner "F2 [P-IPADJ]" put both on SURFACE A — so no edge is
invented; the defect is labeling: per-row cells assign edge ids whose
printed endpoint sets do not contain the row. Fix: mark these cells
"surface A ([P-IPADJ])" or extend the E1/E6 definitions to name the
surface membership explicitly.

### PM-5 — AMENDMENT (both-side-documented couplings absent from §9,
completeness boundary undeclared)
§9 claims soundness ("every edge REAL"), and the machine summary
prints a bare "edges_total: 40" with no non-exhaustiveness clause;
the F2-entry carrier consumer will read the edge set as the coupling
enumeration. The following couplings satisfy the map's OWN edge
standard (endpoints cite each other or a shared authority) and are
not in §9 nor declared out:
  (a) C20↔C28 — C20 note "dependencies of record: C20 -> C28,
      C56/C11-estimator"; C28 note wave-2 rider "wrong-branch
      discrimination WAITS on C20 Tier-0".
  (b) C20↔C56 — C56 note "the C20 branch monitor guards F11d's
      premise at estimator sites"; C20 note names C56.
  (c) C34↔C41 — C34 note R3FAM-2 "NOTIFIED to C41 (a P-tag applies
      at composition time)"; C41 note "the C34 K² instance ... is a
      live P-tag case for this policy's first pass".
  (d) C34/C21/C27↔C42 — the C42 role census names the three notified
      roles from C27 (wave-1), C21 (wave-2), and the C34 K²
      composition instance; C21 note "NOTIFIED to C42" (the map
      carries only the C8 leg, E16).
  (e) C32↔C37 — C37 note "the [P-QNCARRY] arm-B pin stands"
      ([P-QNCARRY] = C32's pinned challenger duty).
Fix (either suffices): add the edges, or add one declared line that
§9 enumerates the CLUSTER/duty-coupling edges of record and is not
the closure of all pairwise note-level citations.

### PM-6 — NOTE (FORK-141 gap ordinals swapped relative to registry)
Registry: H20 magnitude "1 of the 2 genuine gaps in 141 forks"
(:2521 block), P34 magnitude "2 of the 2 genuine gaps" (:2530
block). Map: P34 "(1 of 2 genuine FORK-141 gaps with H20)", H20
"(2 of 2 genuine FORK-141 gaps)". Read as set membership both are
true; read as ordinals they are swapped. Zero substantive effect
(both rows present, both OPEN, homes correct); flagged so the
S-PRES consumer does not cite the ordinals.

### PM-7 — NOTE (H20 open-duty cell adds "N2" beyond the registry
homing)
Map H20 open-duty: "N2/F4b-adjacent (row's own homing)". Registry
homing is "F4b external-expansion window (rides the diff par.2.9
base-pressure agenda entry)"; N2 is C61's declared slot (problem book
:348), not H20's. The cite-only declaration makes placement
non-verdict-bearing, and the distinct-by-declaration clauses are
correctly carried, so this is compression drift only. Tightening to
"F4b window (rides diff par.2.9)" would remove the drift.

### PM-8 — NOTE (path/compression nits, no verdict touched)
(a) The authority for C51/C52/C53/C54 (`VERDICT_contract_and_L4R1.md`
    #D-1/2/4/5, anchors verified at :129/:135/:146/:149) lives at
    `validation/sfoundations_raws_2026-08-13/` (parent dir), but the
    map's PRIMARY SOURCES block lists only `.../blocco3/`; the bare
    filename cites resolve one directory up. One path line fixes it.
(b) OPTSHIFT row quotes two of the registry row's three triggers
    (omits "M-RED rider execution", :2498 block trigger field);
    within the map's declared "cited, verbatim where short" policy,
    but listed here so the omission is on the record.

### PM-9 — NOTE (positive verification record — what did NOT break)
For the record of this pass: (1) status enums 62/62 identical to the
ledger, tally line reproduced by command; (2) all 40 edges source-
true, including the four load-bearing arcs the brief named; (3) the
three id-gaps E33/E37/E40 confirmed absent from §9 exactly as
declared; (4) every ⊘-row status literal (STANDING PIN, USER-PENDING,
DEFERRED DERIVER, USER-DECISION PENDING, LANDED, NAMED-NOT-MINTED,
F2-QUEUED, bracket-not-adequacy, ADJUDICATED-IMPL-OPEN, SHIP-GATE
ARMED, SCHEMA-LICENSED ONLY, ARMED GATE, OPEN, PLAN-SLOTTED) matched
its source row; (5) the §5-label transcriptions are current, not
stale; (6) C46 accounted by declared reason; (7) the census §3/§5
quotes (SDP-CAND-8, interop-inside-C24/C25/C26, Lowering row,
float64 sub-axis, contract F-1..F-10 stage-1 row) are verbatim-true;
(8) the R22-CFD dossier cell (paired-run template, ~12M-cell class,
M-RED dependency, G1 haste-risk) matches VERDICT_blocco2 §6 items at
:395-430. The map's CITE-ONLY declaration held everywhere tested: no
cell was found performing new adjudication.

## 2. VERDICT

The map SURVIVES the adversarial pass: **0 BREAK, 0 REPAIR,
5 AMENDMENT (PM-1..PM-5), 4 NOTE (PM-6..PM-9)**. All amendments are
precision/labeling fixes; none moves a status, an edge's existence,
or a label of record. Recommended: apply PM-1..PM-5 in the next map
touch (same-window edit class); PM-6/PM-7/PM-8 at editor's option.

## 3. MACHINE SUMMARY

```
object: docs/rde_nozzle_pipeline_decision_map.md
pass: MAP REFUTER (dual-proof; edges 100%, load-bearing citations 100%)
window: 2026-08-21 (S-FOUNDATIONS-C4), all counts measured in-window (SR-12)
rows_swept: 62 ledger (61 staged + C46 declared) + 17 nonledger
edges_verified: 40/40 (39 edges + anti-edge E34); id-gaps E33/E37/E40 confirmed unassigned
status_check: 62/62 identical to ledger; tally 12/36/12/2 reproduced by command
stale_labels: 0 (all §5 escalation labels current)
findings: BREAK 0 | REPAIR 0 | AMENDMENT 5 (PM-1 F5->F5b; PM-2 enum not verbatim;
  PM-3 WG10-FAILED field attribution; PM-4 E1/E6 cell over-assignment;
  PM-5 six undeclared both-side couplings / completeness boundary) |
  NOTE 4 (PM-6 gap ordinals; PM-7 H20 N2 drift; PM-8 path+trigger nits;
  PM-9 positive record)
verdict: map SURVIVES as navigation object of record, amendments owed at next touch
```
