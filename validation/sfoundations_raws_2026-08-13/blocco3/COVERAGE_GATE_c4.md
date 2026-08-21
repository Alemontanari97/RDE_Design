# COVERAGE GATE — S-FOUNDATIONS-C4 (ENUMERATOR: machine inventory + three-way accounting)
# Executed 2026-08-21. Spec = validation/sfoundations_raws_2026-08-13/COVERAGE_GATE_spec.md
# (read IN FULL this window), as EXTENDED by the C4 gate brief.
# Every count below is from a command run in THIS window (SR-12); the command is
# quoted per category. Mid-window growth declared: docs/choice_ledger.yaml grew
# 58 -> 60 rows DURING this window (C59/C60 minted 2026-08-21 by the same-gate
# FOUNDATION-CHOICE ENUMERATION slot, file mtime 13:03:21); the accounting below
# uses the LATEST measurement (13:06), never the inherited one.
# Disposition legend (spec (B)): COVERED(anchor) / PARTIAL(named owner+trigger) /
# NOT-COVERED (= a finding). Content-level coverage (no literal tag, question
# weighed inside an adjudicated row/section) is marked COVERED-BY-CLUSTER, same
# convention as FORK_LEDGER_141_adjudication.md.
# REPAIR PASS 2026-08-21: critic COVERAGE_GATE_critic_c4.md CONSUMED IN FULL
# (CGC-1..CGC-8, all repaired in-place below; repair sites marked "REPAIR"/
# "repair pass"); companion artifacts: FOUNDATION_ENUM_census_c4.md (CGC-3),
# ledger mints C61/C62 (CGC-4/CGC-5), ORCH_ACTS_SWEEP_c4.md scope fix (CGC-8).
# The VERDICT-INPUTS section at the end discharges sweep findings F-1/F-3.

------------------------------------------------------------------------------
## CATEGORY 1 — HYPOTHESES (problem-book H-ledger)

Denominator command: `awk 'NR>=486 && NR<=506 && /^\| [HD]/' docs/rde_nozzle_problem_book.md | grep -vc "^| ID"` = **17**
(docs/rde_nozzle_problem_book.md §9 ledger, rows at :488-:504).

BASIS-SWITCH DECLARATION (added at the repair pass per critic CGC-6): the
spec fixes Category 1 on the 12-item problem-statement table (I-GEO ... GEOM,
S1); the prior gate (COVERAGE_GATE_result.md (B)1) accounted THAT basis as
"12 == 10 COVERED + 2 PARTIAL-with-owner (GEOM, S1) + 0 NOT-COVERED". This
gate runs the 17-row problem-book §9 H-ledger basis instead (the of-record
hypothesis ledger, superset in hypothesis content). Mapping declared: the 12
problem-statement items map into the 17 §9 rows for all HYPOTHESIS content
(the S1 prior-gate PARTIAL maps onto row D3 and is landed there — see the D3
row); the one prior-gate item with NO §9 target row is **GEOM**
(cone/attachment admissibility — a geometric-admissibility item, not a flow
hypothesis; the §9 ledger contains no geometric-admissibility row for it to
map onto, grep re-verified at repair). GEOM is therefore carried below as an
explicit out-of-basis row, so the basis switch loses nothing.

| ID | Disposition | Anchor (this-session re-examination) |
|---|---|---|
| H-A1 (single rotating wave, exact periodicity) | COVERED | hypaudit [H-DATA] bundle (hypaudit/confront_hdata.md + refute_H-DATA.md; VERDICT_hypothesis_audit.md §2 + summary row "LEGITTIMA-DICHIARATA-MONITORATA, conditional on ARMING", dual-seed re-run addendum :494) + pure-periodic scope pin adjudication (FORK_LEDGER_141_adjudication P3: diff §4.3 ME-2/ME-3 + §2.11 certificate-moves-on-trip) |
| H-A2 (axisymmetric wall/control surfaces) | COVERED | hypaudit [I-GEO+I-STATE] bundle (hypaudit/confront_axisym.md + VERDICT_hypothesis_audit.md §1) + steadification-exactness refute chain (phaseD/refute_S-T0P_r1-r3; [T-T0P]/[T-T0P-E] claims rows :1966/:2044) |
| H-F1 (frozen family: s, mu, Omega_w independent of Sigma) | COVERED | hypaudit [CONTRACT-MU] E1-E5 bundle (confront_contract.md) + causal-separation escalation ladder adjudicated (diff §2.3, forks P6/H14 COVERED in FORK_LEDGER_141.md) + phaseD_L4_implies_R1.md |
| H2 (choked feed all cycle) | COVERED | discharged-on-L4-DEFAULT of record (problem book PASS-2 note :510-:519); this session: VERDICT_contract_and_L4R1.md + phaseD_L4_implies_R1.md ([L4=>R1] THEOREM, quotable form M0:684-714 read per RETRO_SWEEP PAIR 8); revival case-class typed at ledger C52 (owner F2 contract window); uncertified-choking census A-L6 landed (SYNTHESIS_nozzle_rde_arrivals.md G-13/CT-8, re-homed on lit-registry liu_2022 row :622) |
| H-I2 (no mean upstream influence through Gamma_d) | COVERED | same [L4=>R1] theorem block (phaseD_L4_implies_R1.md; M0:684-714) + agenda items typed to ledger rows C52 (mixed signature) and C53 (Gamma_d placement band), both minted this campaign with owners |
| D1 (St_n -> 0 quasi-steady) | COVERED | [R22F-FORCHETTA] channel (i) time-coupling landed in M0 (:1283ff, C4 landing commit 15a2dd6) + [T-T0P] steadification + the T-DISC/T-RED decomposition rows landed (claims_registry :2148-:2264) |
| D2 (azimuthal decoupling) | COVERED | [R22F-FORCHETTA] channel (ii) azimuthal-structure reduction (K-bar=0 THEOREM*, Lambda scale [SE]) + [T-RED]/[T-RED-1/2/2G] rows (claims :2213-:2264) + diff §3.1 azimuthal-flux commutator (fork H2 COVERED) + swirl5f consumption on C51 note |
| D3 (per-phase MOC-regularity S1, uniqueness) | COVERED | diff §3.3 certified-solution-class blind re-derivation (T-XWS/C-MAJDA road) + C49 wave-2 adjudication of record (fit-vs-capture two-tier; prior-gate PARTIAL owner "phaseD proof labels + C49, session C" — both landed) + [C-DCRX-CERT] scope (c) piecewise-C1 S1 fields (claims :2135) |
| H-T3.1 (one frozen gamma / frozen mixture) | COVERED | hypaudit [GAS-FROZEN] bundle (confront_gas.md; verdict LEGITTIMA-DICHIARATA-MONITORATA) + [R22F-FORCHETTA] channel (v) model-form (frozen-vs-equilibrium bracket priced, P-F14 duty = findings :1627 scope-pins:frozen-model-form-bar-at-champions) |
| H-T3.2 (fixed wall, full-flowing, supersonic exit) | COVERED | hypaudit [EULER-GSEP] bundle (confront_euler.md: g_sep + attached-flow) + diff §2.15 g_sep = integral-BL margin (forks V12/O13/P15 COVERED) + [C-DCRX-CERT] conditional (a): per-cell exit axial supersonicity as a-posteriori certificate (claims :2135-:2147, consumed by [T-DCRX] :2265) |
| H-T3.3 (phase-independent nondimensional inflow shape) | COVERED-BY-CLUSTER | the [T-DISC] fiber-separation block landed this window (claims :2148-:2212 + M0 [T-DISC] block; T-DISC-1 fiber non-degeneracy = the N3 breaker channel formalized at record grade) + P8 adjudication (full-radial-fidelity datum = contract of record by construction, FORK_LEDGER_141_adjudication P8). No literal tag hit in the raws (grep "H-T3.3" = 0, measured) — coverage is content-level, declared |
| H-T4 (ideal-adaptation closure of the free boundary) | PARTIAL(named) | touched: BASE_PRESSURE_HARVEST_c4.md (harvest of record) + diff §2.9 truncation/base-pressure agenda + [R22F-FORCHETTA] channel (v) two-regime base-pressure closure (transition Pa/Pc ≈ 0.15, R8). Missing half NAMED: free-plume-boundary SOLVE mechanics incl. its adjoint/shape term = the category-4 finding of this gate (H20), owner = F4b external-expansion window, trigger = plug/E-D sector campaign entry (rides the diff §2.9 agenda entry) |
| H-P1 (spectral non-degeneracy beyond group mode) | PARTIAL(named) | touched: diff §2.11 H-DATA/mode-detection monitor architecture adjudicated (forks P11/V34 COVERED). Missing half NAMED as typed rows: findings :826 problem-statement:flatness-monitor-unarmed (owner pre-F5 / D6 item 5-bis, CycleFamily v0 + T0-flatness carrier) + findings :1926 item (A20) orbit-spectral (Floquet/monodromy modulo the symmetry group) certificate — contract addition registered, not wired; trigger = CycleFamily build |
| H-mu (mu known, nominal blowdown) | COVERED | hypaudit [CONTRACT-MU] bundle + refute_CONTRACT-MU.md + ledger C50 CLOSED 2026-08-20 (product-ball acceptance + U-slot certified mu-sensitivity instrument with arming triggers; forks V3/P4 adjudicated on it) |
| H-E4 (per-phase Rao/corner theory, gamma frozen) | COVERED-BY-CLUSTER | diff §3.2 blind re-derivation of the per-phase-Rao + averaged-T7 road (forks H35/V20/V21/P26 COVERED) + [R22F-FORCHETTA] channel (iv) Hoffman in-class scaling clause + Hoffman oracle verified [ABS] (MANIFEST ask #9 "CONSUMED by the D1 judge (Hoffman verified [ABS])"). No literal tag hit (grep "H-E4" over raws = 0, measured) — content-level, declared |
| H-Pa (Pa constant over the cycle) | COVERED | discharged of record (problem book PASS-2 note); re-confronted this campaign at the boundary touchpoint: C55 P_amb slot mint (problem book "P_amb SLOT OF RECORD" + ledger C55, user-ratified single-point default; adjudication owner = first multi-point instantiation, the slot's own sequencing clause) |
| H-R1 (causal separation of heat release) | COVERED | hypaudit [R1-CAUSAL] bundle (confront_r1.md; verdict CONDIZIONATA window W1-W4, dual-seed re-run addendum) + phaseD_L4_implies_R1.md ([L4=>R1] THEOREM/THEOREM*) + diff §2.3 escalation ladder |

Carried-forward prior-gate PARTIAL, out-of-basis (restored at the repair
pass per critic CGC-6 — it had silently fallen out in the basis switch):

| ID | Disposition | Anchor |
|---|---|---|
| GEOM (cone/attachment admissibility; prior-gate 12-item basis, no §9 target row) | PARTIAL(named) — carried forward UNCHANGED | owner = **census-lemma window, F2-exit user pin** (unchanged since COVERAGE_GATE_result.md (B)1); locus of record = phaseB_tree_diff.md §4.8 ("cone condition vs sharp features ... GENUINE TENSION not explicitly priced in the record — agenda item for the census-lemma window (F2-exit, user pin respected) + note at the A_gen definition site at next M0 touch") + memory pin topology-census-pins (cono su Ω/Chenais). No discharge anchor exists as of this repair window (search: no census-lemma execution artifact in the record since 2026-08-17) — the PARTIAL stands OPEN with its owner |

**ZERO ARITHMETIC (1): 17 (§9-ledger basis) == 15 COVERED + 2 PARTIAL(named: H-T4 -> F4b window; H-P1 -> flatness/orbit-spectral typed rows) + 0 NOT-COVERED; PLUS 1 carried-forward out-of-basis PARTIAL (GEOM -> census-lemma window, F2-exit) — accounted total 18 == 15 COVERED + 3 PARTIAL + 0 NOT-COVERED.**

------------------------------------------------------------------------------
## CATEGORY 2 — CHOICES (docs/choice_ledger.yaml, status-based accounting)

Denominator command: `grep -c "^- id:" docs/choice_ledger.yaml` = **60**
(re-measured 2026-08-21 13:06 after the in-window C59/C60 mint; the earlier
in-window measurement read 58 — growth declared above, latest wins).
Status tally command: `grep -oP "^  status: \S[^#]*" docs/choice_ledger.yaml | sed 's/  status: //' | sort | uniq -c`
= DECIDED 12, MIXED 36, NEVER 10, SINGLE-AUTHOR 2 (12+36+10+2 = 60).

Rule applied (gate brief): DECIDED/MIXED with named duty = COVERED;
NEVER/SINGLE-AUTHOR = PARTIAL, valid only with owner+trigger verified per row.

- COVERED (48 = 12 DECIDED + 36 MIXED): DECIDED = C3, C4, C15, C19, C23, C24,
  C26, C30, C45, C46, C47, C48; MIXED = the remaining 36 (C1, C2, C5-C14, C16,
  C20-C22, C27-C29, C31-C37, C39-C44, C49, C50, C56, C58). Owner-field audit
  (measured): every row except the five DECIDED rows C3/C4/C15/C23/C24 carries
  an explicit `owner:` field; those five are DECIDED closed rows (no open duty
  to own — named duty = the decided incumbent itself). All 36 MIXED rows carry
  owner fields naming the open half's duty.
- PARTIAL (12 = 10 NEVER + 2 SINGLE-AUTHOR), owner+trigger VERIFIED row by row
  (read in full this window):

| ID | status | owner+trigger (quoted from the row) |
|---|---|---|
| C17 | SINGLE-AUTHOR | owner "F2 (owner delta of record, VERDICT_wave3 par.3 ...; C43/C21 bookkeeping-alignment precedent)" |
| C18 | SINGLE-AUTHOR | owner "S25 halved-constants sweep (executed; derivation duty now F2-live)" |
| C25 | NEVER | owner "F2 (with C-C/C-D)" (annex pointer GAP-11; H-F6 reachable-set box = C25's object, cross-slot consumption of record) |
| C38 | NEVER | owner "F2" (annex pointer GAP-2; landing-priority note in row prevents re-mint; trigger = F2 stationarity-declaration window) |
| C51 | NEVER | owner "rung-3a implementation window (adjudication owed at implementation time, not before — the judge's own sequencing)" |
| C52 | NEVER | owner "F2 contract window (the judge's agenda: pin which reading governs; feeds the chi character-map finding row)" |
| C53 | NEVER | owner "F2 contract window: a placement-band remark in M0 D2.4 ... naming the two monotone pressures and the emptiness verdict" |
| C54 | NEVER | owner "next M0 D2.4 touch (one-line I4 annotation; when the line lands this row flips DECIDED with the M0 anchor as evidence)" |
| C55 | NEVER | owner "first multi-point instantiation of P_amb (adjudication owed at instantiation time ... single-point default keeps the question empty)" |
| C57 | NEVER | owner "F2-entry adjudication window (interacts with C31 A/B and C49 explorer; user directive axis 4 ...)" |
| C59 | NEVER | owner "F2-entry census window; trigger = any weakened-pin regime (multi-frequency / aperiodic / windowed) entering scope" |
| C60 | NEVER | owner "F2-entry engine window (the C31 A/B decision surface; adjudicated as a CLUSTER with C57/C58/[P-IPADJ]); trigger = the F2-entry engine act" |
| C61 | NEVER | owner "N2/F4b window"; trigger "first truncated-plug (value,delta) row entering the record, or F4b window entry" (minted at the REPAIR pass, CGC-4) |
| C62 | NEVER | owner "F2 engine window (numerics cluster)"; trigger "first accuracy budget of the F2 campaign" (minted at the REPAIR pass, CGC-5) |

All 14 PARTIAL rows verified to carry owner+trigger — zero unowned.
Repair-pass growth declared: the ledger grew 60 -> 62 at the CGC-4/CGC-5
mints (C61 base-pressure closure model, C62 phase quadrature over Xi);
denominator re-measured `grep -c "^- id:" docs/choice_ledger.yaml` = **62**,
status tally = DECIDED 12 / MIXED 36 / NEVER 12 / SINGLE-AUTHOR 2.

**ZERO ARITHMETIC (2): 62 == 48 COVERED (DECIDED+MIXED w/ named duty) + 14 PARTIAL(owner+trigger verified: C17, C18, C25, C38, C51, C52, C53, C54, C55, C57, C59, C60, C61, C62) + 0 NOT-COVERED.**

------------------------------------------------------------------------------
## CATEGORY 3 — THEORY CLAIMS (docs/claims_registry.yaml)

Denominator command: `grep -c "^- id:" docs/claims_registry.yaml` = **163**
(independently confirmed by the lint's own parse count: "parsed 163 entries:
carrier 48, conditional 15, conjecture 3, definition 8, directive 10, oracle 3,
paper 10, schema 19, theorem 47").

Coverage evidence, both legs measured this window:
1. Lint (xv) run: `python tests/test_claims_lint.py` =
   **"claims lint: registry coherent + rejector proven PASS (0 violations)"**
   (4/4 seeded rejectors REJECTED-as-designed; PyYAML absent, subset parser
   primary — declared by the lint itself).
2. The 13 new C4 rows present, grep command:
   `grep -c "^- id: \(C-R22F-DISC\|C-RED-SBV\|C-DCRX-CERT\|T-DISC\|T-DISC-1\|T-DISC-2\|T-DISC-3\|T-DISC-4\|T-RED\|T-RED-1\|T-RED-2\|T-RED-2G\|T-DCRX\)$"` = **13**
   (lines: C-R22F-DISC :2109, C-RED-SBV :2122, C-DCRX-CERT :2135, T-DISC :2148,
   T-DISC-1 :2161, T-DISC-2 :2174, T-DISC-3 :2187, T-DISC-4 :2200, T-RED :2213,
   T-RED-1 :2226, T-RED-2 :2239, T-RED-2G :2252, T-DCRX :2265 — the
   S-FOUNDATIONS-C4 landing-completion block, header comment :2101).

**ZERO ARITHMETIC (3): 163 == 163 COVERED (lint (xv) PASS in-window + 13/13 C4 rows present by grep) + 0 PARTIAL + 0 NOT-COVERED.**

------------------------------------------------------------------------------
## CATEGORY 4 — DE-NOVO FORKS (reconciled matrix of this gate)

Sources read in full this window: blocco3/FORK_LEDGER_141.md (mechanical
extraction) + blocco3/FORK_LEDGER_141_adjudication.md (Fable judgment pass).
This gate's matrix covers the fork rows enumerated below:
V 34 + H 41 + O 32 + P 34 = **141 rows in this matrix** (REPAIRED per critic
CGC-1: the delivered matrix read P 33 / 140 total, silently dropping fork P34
from the accounting — see the P-row NOT-COVERED cell below. [SEED-OMIT
discharged: planted by pre-registration 634b972, caught CGC-1]).

| Tree | mechanical COVERED | COVERED-BY-CLUSTER (adjudication pass) | resolved AMBIGUOUS | NOT-COVERED | row total |
|---|---|---|---|---|---|
| V | 19 | 15 (V1, V3, V8, V10, V11, V14, V16, V17, V18, V19, V20, V21, V22, V33, V34) | 0 | 0 | 34 |
| H | 31 | 8 (H12, H17, H22, H25, H30, H31, H32, H38) | 1 (H13 — ambiguity RESOLVED as genuine second anchor, reg:1606 + diff §3.3 + reg:1615; no registry edit required) | 1 (**H20**) | 41 |
| O | 21 | 11 (O1, O5, O10, O12, O14, O15, O26, O27, O28, O29, O31) | 0 | 0 | 32 |
| P | 19 | 14 (P1, P2, P3, P4, P7, P8, P13, P18, P23, P24, P25, P29, P30, P32) | 0 | 1 (**P34**) | 34 |
| TOT | 90 | 48 | 1 | 2 | 141 |

The TWO NOT-COVERED, typed as this gate's findings:
- **H20** — free plume boundary (p = Pa) SOLVE mechanics, incl. the
  free-boundary position in the state vector and its adjoint/shape-derivative
  term; required exactly in plug/E-D sectors (wetted solid inside the plume
  region); owner = **F4b external-expansion window** (rides the diff §2.9
  base-pressure agenda entry). Same residue named in Category 1 as the
  missing half of H-T4's PARTIAL — one finding, two faces, one owner.
  Findings carrier: docs/findings_registry.yaml:2519
  (plume:free-boundary-solve-mechanics-missing).
- **P34** — staged evidence hierarchy for engine-level claims (V0 continuous
  verification -> per-champion validation -> pre-registered, prediction-first
  rig/thrust-stand terminal test, ordering and gaps published beforehand);
  adjudicated GENUINELY NOT-COVERED by this gate's own declared source
  (FORK_LEDGER_141_adjudication.md table row P34 + machine summary
  "139 + 2 = 141. Reconciled."); nearest record = diff §4.10, declared
  "no row"; owner = **P-1/G5-G6 claims window**. Findings carrier:
  docs/findings_registry.yaml:2530
  (claims:engine-level-staged-evidence-hierarchy-missing).
  [SEED-OMIT discharged: planted by pre-registration 634b972, caught CGC-1 —
  the fork was the orchestrator's planted omission seed and the delivered
  matrix omitted it exactly as planted; restored at this repair pass with
  arithmetic re-reconciled to the 141 source-of-record denominator.]

Adjudication-pass conventions inherited and declared: K1 (minted-but-open
ledger rows C51/C52/C55/C57 count as coverage — the row's function is that the
question cannot close by omission); D-1 (O15's covering adjudication lives in
docs/rde_nozzle_pipeline_audit.md:105 + docs/rde_nozzle_general_scheme_panel.md:29;
its no-row rider is now EXECUTED — ledger row C60 minted in this window, so the
D-1 deviation is DISCHARGED at this gate).

**ZERO ARITHMETIC (4): 141 == 139 COVERED (90 mechanical + 48 by-cluster + 1 resolved-ambiguous H13) + 0 PARTIAL + 2 NOT-COVERED (H20, owner F4b; P34, owner P-1/G5-G6 claims window).**

------------------------------------------------------------------------------
## CATEGORY 5 — ARRIVALS -> CONSUMER (2026-08-20 arrivals)

Denominator commands: `grep -c "^| [a-z].*\.pdf" validation/sfoundations_raws_2026-08-13/MANIFEST_papers_foundations_c.md`
= **21** foundations-c PDF files (13 main table + 4 addendum + 1 Becker-Rannacher
+ 3 addendum-2); + the 4 nozzle-RDE campaign rows (lit-registry ids liu_2022 :616,
li_xu_lv_lv_song_2023 :684, li_xu_lv_yu_zhou_2025 :691, jourdaine_2019 :698,
campaigns P-A..P-D) = **25 arrivals**.
Dedup declared: the 2 Uno files (uno_paper.pdf + arXiv:2406.13454v2 preprint)
share ONE registry row (vanaret_leyffer_2026_uno, same-paper multi-path rule),
so 21 files map to 20 registry rows; the file-level accounting below is over 25.

| # | Arrival (file) | Registry row (line) | Status + consumer/where_read anchor |
|---|---|---|---|
| 1 | byrd_hribar_nocedal_1999_..._siopt9.pdf | byrd_hribar_nocedal_1999 (:971) | READ-PARTIAL; RETRO_SWEEP_arrivals.md PAIR 1 + PAIR 8; consumer [P-IPADJ]/C31 |
| 2 | nocedal_wright_2006_..._2ed.pdf | nocedal_wright_2006_2ed (:980) | READ-PARTIAL; phaseD/phaseD_minor_ntf.md#6 + phaseD_minor_crosslowering.md#6; consumer [P-QNCARRY]/[P-HESSREJ] |
| 3 | yamamoto_1986_..._numermath48.pdf | yamamoto_1986_numermath48 (:1047) | READ-PARTIAL; phaseD/phaseD_minor_ntf.md#6; consumer C20 Tier-2 r_K |
| 4 | giles_pierce_1997_..._aiaa97_1850.pdf | giles_pierce_1997 (:989) | READ-INTEGRAL (C4 promotion); RETRO_SWEEP PAIR 8 + phaseD/phaseD_r22f_centerpiece.md#2.4; consumer R27 bridge + F11d leg-1 oracle |
| 5 | venditti_darmofal_2000_..._jcp164.pdf | venditti_darmofal_2000 (:999) | READ-PARTIAL; RETRO_SWEEP PAIR 5; consumer C11 leg (b) |
| 6 | hicken_zingg_2014_..._jcp256.pdf | wanted_hicken_zingg_2014 (:920) | READ-PARTIAL; RETRO_SWEEP PAIR 2; consumer F11d criteria (C56 note anchored) |
| 7 | fidkowski_darmofal_2011_..._aiaaj.pdf | wanted_fidkowski_darmofal_2011 (:876) | READ-PARTIAL; RETRO_SWEEP PAIR 6; consumer C9/C11 canon |
| 8 | huang_zahr_2022_..._jcp454.pdf | huang_zahr_2022 (:1007) | READ-PARTIAL; RETRO_SWEEP PAIR 4; consumer C49 entry gate |
| 9 | thakur_nadarajah_2025_..._jcp523.pdf | wanted_thakur_nadarajah_2024 (:928) | READ-PARTIAL; RETRO_SWEEP PAIR 4; consumer C9 steelman + C49 |
| 10 | masters_etal_2017_..._aiaaj.pdf | masters_etal_2017 (:1023) | READ-PARTIAL; RETRO_SWEEP PAIR 7; consumer C1 dof-budget prior |
| 11 | lauer_ansell_2025_..._pas.pdf | lauer_ansell_2025_pas (:1031) | READ-PARTIAL; RETRO_SWEEP PAIR 7; consumer C1 modern layer |
| 12 | breitkopf_ulbrich_2025_..._arxiv250922076.pdf | wanted_breitkopf_ulbrich (:754) | READ-PARTIAL; RETRO_SWEEP PAIR 8 + phaseD/phaseD_r22f_centerpiece.md#2.6; consumer D25U front-terms (retained as named F2 TEMPLATE, not consumed — declared on the row) |
| 13 | deuflhard_2011_..._csm35.pdf | deuflhard_2011_csm35 (:1039) | READ-PARTIAL; phaseD/phaseD_minor_ntf.md#6; consumer C20 Tier-1 band |
| 14 | uno_paper.pdf | vanaret_leyffer_2026_uno (:1055) | READ-PARTIAL (visual pp., no text layer, declared); RETRO_SWEEP PAIR 1 + PAIR 8 + DOSSIER_uno_fullread.md (arm-B §3 inputs ENTER the [P-IPADJ] spec per C4 injection-bis, C31 ledger note); consumer F2-C31-ENGINE-AB |
| 15 | vanaret_leyffer_2026_..._arxiv2406_13454.pdf | same row :1055 (multi-path dedup, declared) | READ-PARTIAL; same anchors as #14 |
| 16 | vanaret_montoison_2026_uno_joss10229.pdf | vanaret_montoison_2026_joss (:1064) | READ-PARTIAL; RETRO_SWEEP PAIR 1; consumer C31 software identity |
| 17 | huang_zahr_2023_arxiv_2304_11427_companion.pdf | huang_zahr_2023_companion (:1015) | READ-PARTIAL; RETRO_SWEEP PAIR 4; consumer C49 W4 entry-gate re-evaluation |
| 18 | becker_rannacker.pdf | wanted_becker_rannacher_2001 (:862) | READ-PARTIAL; RETRO_SWEEP PAIR 3; consumer C11/DWR canon |
| 19 | sun_nocedal_2023_..._arxiv2201_00973.pdf | sun_nocedal_2023_noisy_tr (:1072) | **declared-UNREAD-with-owner**: "C34 trigger window (VERDICT_wave3 §9 ask 4: consumed deliberately at the [P-TRFLOOR] trigger)" |
| 20 | shi_xie_xuan_nocedal_2022_..._arxiv2110_06380.pdf | shi_xie_xuan_nocedal_2022_fd_interval (:1078) | **declared-UNREAD-with-owner**: "F2-C44-FDSTEP duty (VERDICT_wave3 §9 ask 5)" |
| 21 | metivier_etal_2021_ot_misfit_arxiv2101_00904.pdf | messud_etal_2021_ot_kr_misfit (:1084) | **declared-UNREAD-with-owner**: "C50 OT-closure optional enrichment (non-blocking)"; attribution flag (Messud vs Metivier) declared on the row, settled at first read |
| 22 | liu_2022 duplicate copy (campaign P-A) | liu_2022 (:616) | READ-INTEGRAL; re-read [FULL] 14/14 pp. this campaign = NOZZLE_RDE_STUDY_pA_liu_wang_2022.md (row note; errata Delta-8 + A-L6 choking note registered on the row); consumer SYNTHESIS_nozzle_rde_arrivals.md + census:liu-2022-binding-insertions (findings :2433) |
| 23 | li_xu_lv_lv_song_2023_..._ast136_108221.pdf (P-B) | li_xu_lv_lv_song_2023 (:684) | READ-INTEGRAL; where_read = NOZZLE_RDE_STUDY_pB_li_xu_2023.md#1; consumer SYNTHESIS + REFUTE_nozzle_rde_synthesis chain |
| 24 | li_xu_lv_yu_zhou_2025_..._ast158_109878.pdf (P-C) | li_xu_lv_yu_zhou_2025 (:691) | READ-INTEGRAL; where_read = NOZZLE_RDE_STUDY_pC_li_xu_2025.md#1; consumer SYNTHESIS + FORCHETTA (nearest-referee disqualification, [GRAFT-G10]) |
| 25 | jourdaine_2019_..._pci37_3443.pdf (P-D) | jourdaine_2019 (:698) | READ-INTEGRAL; where_read = NOZZLE_RDE_STUDY_pD_jourdaine_2019.md#(1); consumer SYNTHESIS + P-A[26] choking corpus number |

**ZERO ARITHMETIC (5): 25 == 22 COVERED (read, with where_read/consumer anchor on the registry row) + 3 PARTIAL (declared-unread-with-owner: sun_nocedal_2023_noisy_tr, shi_xie_xuan_nocedal_2022_fd_interval, messud_etal_2021_ot_kr_misfit) + 0 NOT-COVERED / 0 unaccounted.**

------------------------------------------------------------------------------
## CATEGORY (SPEC-5) — NOVEL ITEMS (ADDED AT THE REPAIR PASS per critic CGC-2)

The binding spec's inventory category 5 (COVERAGE_GATE_spec.md (A)5) was not
run in the delivered gate — the C4 brief's 3 extension categories extend, not
substitute. Run here as of TODAY (2026-08-21, repair window; every anchor
re-measured by grep in THIS window, SR-12). Denominator per the prior gate's
F2-repair arithmetic (COVERAGE_GATE_result.md (C)): **32 == 16 phaseB diff §2
items + 10 contract-blind demands (F-1..F-10, VERDICT_contract_and_L4R1.md)
+ 6 hypothesis-audit bundles**. Convention: COVERED = carried by a
registry/ledger row or adjudicated mapping of record (K1: a minted-but-open
row with owner+trigger counts as coverage — the question cannot close by
omission); PARTIAL = carried only partly, missing half named with owner.

### (a) The 16 phaseB diff §2 items

| § | Item | Disposition | Anchor as of TODAY |
|---|---|---|---|
| 2.1 | Discrete control-surface invariance rejector | COVERED | findings :1589 carriers:control-surface-invariance-rejector-missing (minted prior gate, owner F2 carrier duty) |
| 2.2 | Per-phase branch selection + fold-margin monitor | COVERED | findings :1598 engine:flow-branch-selection-unpinned + the wave-2 C20 Tier-0 branch-monitor premise guard (C56 note, of record) |
| 2.3 | Causal-separation escalation ladder | COVERED | findings :835 problem-statement:stage-a-audits-premised-not-implemented (enriched) + forks P6/H14 COVERED (FORK_LEDGER_141; Category-1 H-F1 row above) |
| 2.4 | Plume vortex-sheet stability + decoupling certificate | COVERED | findings :1607 plume:vortex-sheet-stability-unchecked (owner F4b/F5-adjacent); DISTINCT-by-declaration from the H20 solve-mechanics row :2519 |
| 2.5 | Gamma_d placement residual accounting | COVERED | findings :835 (same stage-A row) + ledger C53 (placement band, minted 2026-08-19, owner F2 contract window) |
| 2.6 | Fundamental-derivative audit | COVERED | findings :1616 thermotab:fundamental-derivative-audit-missing + C25 cross-slot consumption (H-F6 reachable-set box = C25's object, Category-2 row above) |
| 2.7 | Frozen-vs-equilibrium model-form (v) bar | COVERED | findings :1625 scope-pins:frozen-model-form-bar-at-champions; CONSUMED by [R22F-FORCHETTA] channel (v) (P-F14 duty, Category-1 H-T3.1 anchor) |
| 2.8 | Swirl first-order mandate | COVERED | mapped of record (§2.8's own verdict: "no new row needed") — swirl-f2a rows + swirl5f panel §8 verifier landing (C51 note INPUT APPENDED block) |
| 2.9 | Base-pressure / truncated-plug Euler-uncertifiable zone | COVERED (UPGRADED from the prior gate's sole AGENDA disposition) | BASE_PRESSURE_HARVEST_c4.md (harvest of record, commit b3da86d) + findings :2519 (H20 solve mechanics) + **ledger C61 minted at THIS repair pass** (closure-model axis, CGC-4) + ADR-D4 rider items 4-6 (PROGRESS BLOCCATO 9) |
| 2.10 | Phase-quadrature stratification at events | COVERED (UPGRADED from mapped) | **ledger C62 minted at THIS repair pass** (CGC-5; owner F2 numerics cluster, trigger = first F2 accuracy budget) + findings :988 phase-diagrams:eps-tolerance-omits-quadrature-bar |
| 2.11 | H-DATA monitor w/ adjoint-based sensitivity carrier | PARTIAL(named) | typed rows exist — findings :826 problem-statement:flatness-monitor-unarmed + findings :1926 orbit-spectral certificate — but the monitor is UNARMED and the carrier unwired; mirrors Category-1 H-P1 PARTIAL, same owner (pre-F5 / D6 item 5-bis; trigger = CycleFamily build) |
| 2.12 | Existence discrete-shadow split | COVERED | mapped of record to the P7/Chenais road (problem book sector-decomposition SCHEMA) with the O-F30/V-F15 instruments mechanically COVERED in the Category-4 matrix (neither appears in any exception list of FORK_LEDGER_141_adjudication) |
| 2.13 | Front-terms in the adjoint designed-in | COVERED | giles_pierce_1997 lit row :989 READ-INTEGRAL (C4 promotion) + the M0 NTF derivation block landed at 15a2dd6 (Category-3 rows) + R27 carrier append |
| 2.14 | Two-instrument twin doctrine | COVERED | mapped of record (moc-critical-independent-invariants standing) + C49 two-tier row carries the |J_capture − J_fitted| (v)-carrier increment |
| 2.15 | g_sep carrier = integral-BL margin | COVERED | forks V12/O13/P15 COVERED (Category-4) + hypaudit [EULER-GSEP] bundle + the F2a criterion-class adjudication agenda named in Category-1 H-T3.2 above |
| 2.16 | Averaged-system regression oracles | COVERED | classical-oracle program of record + Hoffman oracle verified [ABS] (Category-1 H-E4 anchor, MANIFEST ask #9) + forks H35/P19/P26 mechanically COVERED (no exception-list hit) |

### (b) The 10 contract-blind demands (F-1..F-10)

All ten carried as findings-registry rows, measured this window
(`grep -n "id: contract:" docs/findings_registry.yaml` = 10 rows):
F-1 :1643 (data-class-function-space-unpinned), F-2 :1652
(datum-internal-rh-entropy-audits-missing), F-3 :1661
(datum-uncertainty-contract-missing; metric half CLOSED by C50,
VERDICT_C50_form2 of record), F-4 :2299 (global-budget-closure),
F-5 :2308 (design-sweep-invariance), F-6 :2317 (phase-gauge/jitter),
F-7 :2326 (chi character map; cross-referenced by the C52 owner field),
F-8 :2335 (quasi-steady a-priori number), F-9 :2344 (wave-asymmetry
demotion), F-10 :2353 (wall-corner trace audit). **10 COVERED.**

### (c) The 6 hypothesis-audit bundles

[H-DATA], [I-GEO+I-STATE], [CONTRACT-MU], [GAS-FROZEN], [EULER-GSEP],
[R1-CAUSAL] — all six verdicts of record (hypaudit/VERDICT_hypothesis_audit.md
+ 6 confront files on disk, verified this window) and each is a live anchor
in Category 1 above (rows H-A1, H-A2/H-T3.2, H-F1/H-mu, H-T3.1, H-T3.2,
H-R1). **6 COVERED.**

### (d) Prior-gate queued-by-name landing recount (the CGC-2 live point)

The prior gate closed this category with 11 queued-by-name items; their
landing status, measured TODAY: F-4..F-10 -> LANDED as findings rows
:2299-:2353 (above); D-1/D-2/D-4 -> LANDED as ledger rows C52/C53/C54
(minted 2026-08-19, Blocco-2 landing); §4.5 (quiescent-ambient declaration
line) -> LANDED as the P_amb SLOT OF RECORD (problem book :553) + ledger C55;
§4.10 (thrust-stand anchoring, the P34 locus) -> LANDED as findings :2530 +
the Category-4 P34 NOT-COVERED row of THIS gate (owner P-1/G5-G6). The queue
is EMPTY — exactly as the critic predicted, the one skipped category owned
the fork the matrix lost (CGC-1/CGC-2 correlation confirmed).

**ZERO ARITHMETIC (SPEC-5): 32 == 31 COVERED (15 §2 + 10 contract-blind + 6
hypaudit) + 1 PARTIAL(named: §2.11 -> pre-F5 / CycleFamily-build trigger,
mirroring Category-1 H-P1) + 0 NOT-COVERED / 0 uncarried.**

------------------------------------------------------------------------------
## MACHINE SUMMARY (all counts measured this window, 2026-08-21)

```json
{
  "gate": "S-FOUNDATIONS-C4 COVERAGE GATE — ENUMERATOR (A)+(B)",
  "categories": {
    "1_hypotheses":   {"denominator": 17,  "covered": 15,  "partial": 2,  "not_covered": 0, "carried_forward_out_of_basis_partial": 1, "note": "GEOM prior-gate PARTIAL restored at repair (CGC-6): accounted total 18 = 15+3+0"},
    "2_choices":      {"denominator": 62,  "covered": 48,  "partial": 14, "not_covered": 0, "note": "re-measured at repair after the C61/C62 CGC-4/CGC-5 mints (62 = 12 DECIDED + 36 MIXED + 12 NEVER + 2 SINGLE-AUTHOR); C61/C62 carry owner+trigger, PARTIAL by the same rule as the other NEVER rows"},
    "3_theory_claims":{"denominator": 163, "covered": 163, "partial": 0,  "not_covered": 0},
    "4_denovo_forks": {"denominator": 141, "covered": 139, "partial": 0,  "not_covered": 2, "note": "P34 restored at repair (CGC-1, SEED-OMIT discharged)"},
    "5_arrivals":     {"denominator": 25,  "covered": 22,  "partial": 3,  "not_covered": 0},
    "spec5_novel_items": {"denominator": 32, "covered": 31, "partial": 1, "not_covered": 0, "note": "category ADDED at repair (CGC-2); prior-gate 11-item queue recounted EMPTY"}
  },
  "zero_arithmetic": "reconciled in all 6 categories (17=15+2+0 basis + 1 carried GEOM => 18=15+3+0; 62=48+14+0; 163=163+0+0; 141=139+0+2; 25=22+3+0; 32=31+1+0)",
  "not_covered_findings": [
    {"id": "H20", "category": 4, "what": "free plume boundary (p=Pa) solve mechanics incl. free-boundary adjoint/shape term", "owner": "F4b external-expansion window (diff par.2.9 agenda entry)", "also_faces": "Category-1 H-T4 PARTIAL missing half", "findings_carrier": "docs/findings_registry.yaml:2519"},
    {"id": "P34", "category": 4, "what": "staged evidence hierarchy for engine-level claims (V0 verification -> validation -> pre-registered prediction-first terminal test)", "owner": "P-1/G5-G6 claims window", "nearest_record": "diff par.4.10, declared no-row", "findings_carrier": "docs/findings_registry.yaml:2530", "seed": "SEED-OMIT discharged: planted by pre-registration 634b972, caught CGC-1"}
  ],
  "partial_owners_verified": ["H-T4->F4b", "H-P1->findings:826+findings:1926", "GEOM->census-lemma window F2-exit (carried forward, CGC-6)", "C17", "C18", "C25", "C38", "C51", "C52", "C53", "C54", "C55", "C57", "C59", "C60", "C61", "C62", "spec5-2.11->CycleFamily build", "sun_nocedal->C34 trigger", "shi_xie->F2-C44-FDSTEP", "messud->C50 OT optional"],
  "in_window_growth_declared": "choice_ledger 58->60 during the gate window (C59/C60 same-gate mint), 60->62 at the repair pass (C61/C62, CGC-4/CGC-5); latest measurement used",
  "lint_xv": "PASS (0 violations, 163 entries, 4/4 rejectors proven)",
  "d1_rider_status": "FORK_LEDGER_141_adjudication deviation D-1 DISCHARGED by the C60 mint (verified in-window)",
  "repair_pass": "2026-08-21, critic COVERAGE_GATE_critic_c4.md CONSUMED: CGC-1..CGC-8 all repaired (CGC-1 P34 restored; CGC-2 spec-5 category added; CGC-3 FOUNDATION_ENUM_census_c4.md written; CGC-4 C61 minted; CGC-5 C62 minted; CGC-6 GEOM PARTIAL restored + basis-switch declared; CGC-7 VERDICT-INPUTS section below; CGC-8 sweep scope line fixed)"
}
```

------------------------------------------------------------------------------
## VERDICT-INPUTS (ADDED AT THE REPAIR PASS — discharges critic CGC-7 and
## ORCH_ACTS_SWEEP_c4.md findings F-1/F-3; every count measured in THIS
## repair window, 2026-08-21, commands quoted, SR-12)

### (i) Six-mint recount (sweep F-3: "the gate verdict MUST recount these
### six before PASS") — 6/6 CARRIED

| # | Declared mint | Carrier, measured THIS window | Command |
|---|---|---|---|
| 1 | temporal-form row | ledger C59 at docs/choice_ledger.yaml:795 | `grep -n "^- id: C59$" docs/choice_ledger.yaml` = 795 |
| 2 | NAND-vs-SAND row | ledger C60 at docs/choice_ledger.yaml:807 | `grep -n "^- id: C60$" docs/choice_ledger.yaml` = 807 |
| 3 | G-14 home append (vander_veen_1974) | literature registry :434 — REPAIRED IN-WINDOW: the as-delivered append used a `note:` field on an entry row, which the four-roots lint declares for bulk rows only; measured FAIL "VIOLATION vander_veen_1974: fields missing [] / undeclared ['note']" — content folded VERBATIM into the row's `summary` field (allowed), re-run = "literature registry lint (four roots) PASS (165 entries [79 WANTED], 9 bulk rows, disk A/B/C/D = 39/47/77/59, 0 violations)" | `grep -n "G-14 HOME" docs/literature_registry.yaml` = 434 |
| 4 | H20 findings row | docs/findings_registry.yaml:2519 (plume:free-boundary-solve-mechanics-missing) | `grep -n` by id = 2519 |
| 5 | P34 findings row | docs/findings_registry.yaml:2530 (claims:engine-level-staged-evidence-hierarchy-missing) | `grep -n` by id = 2530 |
| 6 | glossary 85->52 resolution | outcome carrier = the passing ratchet AT baseline: "glossary lint (collision + navigation, NOT anti-re-mint) PASS (47 families, 238 entries, 0 violations)", unresolved tokens 52 == frozen baseline 52, measured this window; end-state cross-carrier = blocco3/GLOSSARY_SR4_resolution_report.md (tokens_end 52) | `python tests/test_glossary.py` (line quoted) |

Line-drift declaration (SR-12): the critic's recount cited findings :2522/:2533
and lit :428; THIS window measures :2519/:2530 and :434 — same rows, verified
BY ID, shifted by intervening working-tree edits (the rows' identity, not
their line numbers, is the carrier).

### (ii) The 13 GATE JUDGE-DELIVERY checks re-run FROM FILES (sweep F-1
### repair path: retiring the conversation-only evidentiary basis)

Checklist = SENSE_REVIEW_centerpiece_plan_c4.md "GATE JUDGE-DELIVERY"
section (:429-:459). Targets: CP = phaseD/phaseD_r22f_centerpiece.md,
M0 = docs/rde_nozzle_MASTER.md, R = VERDICT_r22f.md, B = VERDICT_blocco2.md,
E = VERDICT_escalation_c4.md (blocco3). All greps run 2026-08-21:

| Check | Grep basis (this window) | Counts | Verdict |
|---|---|---|---|
| SR-C4-1 forchetta completeness | `grep -c "SCALING-ESTIMATE"` CP/M0; `grep -c "58.1\|71.5"` CP/M0 | CP 9, M0 8; CP 3, M0 3 | GREEN |
| SR-C4-2 declaration (c) referee/c_F | `grep -ci referee` CP/R; `grep -c c_F` CP | CP 9, R 6; CP 1 | GREEN |
| SR-C4-3 Fig.18 dispositions + citations | `grep -c "Fig. 18\|Fig.18\|Fig 18"` CP; `grep -c "C51\|S-5F\|row 13\|row-13"` CP | 6; 16 | GREEN |
| SR-C4-4 channel (vi) + hypothesis list | `grep -c "channel (vi)"` CP; `grep -ci "projected Hessian\|basin\|dual norm\|active constraint"` CP | 2; 20 | GREEN |
| SR-C4-5 part (4) presents-not-decides + dossier | `grep -ci "presents\|scheduling"` B; `grep -ci "R22-CFD"` B | 4; 6 | GREEN |
| SR-C4-7 deliverables tick-list | `grep -ci deliverable` R/B | R 2, B 6 | GREEN |
| SR-C4-8 provenance spot-checks + ADVISORY labels | `grep -ci swirl5f` CP/R; `grep -ci Paxson` CP; `grep -ci ADVISORY` CP | CP 17, R 0; 6; 28 | GREEN (spot-check carriers live in the centerpiece + checkpoint; R count 0 declared honestly — the duty was on the draft) |
| SR-C4-9 OBJ-DOM/delta-carrier consistency in B | `grep -ci "OBJ-DOM\|delta-carrier\|SR-C4-9"` B | 18 | GREEN (explicit, incl. the literal SR-C4-9 line) |
| SR-C4-10 per-amendment not-a-BREAK in R | `grep -ci "not a BREAK\|not-a-BREAK"` R | 3 | GREEN |
| SR-C4-16 threat-ledger dispositions | `grep -ci threat` R/B | R 1, B 2 | GREEN (B carries "threat ledger 8/8 ADOPTED" of record) |
| SR-C4-17 landing list duties | `grep -c "1459\|PAPERS NEEDED\|landing site"` B/R | B 6, R 4 | GREEN |
| SR-C4-18 G-c outcome greppable | `grep -c "G-c"` R/B/E | R 6, B 1, E 0 | GREEN (present in the two verdicts that own it) |
| SR-C4-19 no judge-minted temporal-form row | `grep -ci "temporal-form\|temporal form"` R/B | R 0, B 1 ("temporal-form correctly not minted") | GREEN (negative check holds; C59's mint provenance = the gate, per its own note) |

13/13 GREEN from file-based re-runs — sweep F-1's conversation-only basis is
RETIRED; this section is the file carrier of record.

### (iii) Sweep F-2 status

DISCHARGED before this repair pass: commit 634b972 committed the checkpoint
COVERAGE GATE LAUNCH + DUAL-SEED block (message declares the late-commit
posture and the harness-persisted workflow script as independent
tamper-evidence; both seed outcomes recorded: SEED-OMIT P34 CAUGHT (CGC-1),
SEED-DECOY C50 NOT FLAGGED).

### (iv) OBS-1 basis statement (lit-count arithmetic)

Measured this window: `grep -c "^- id:" docs/literature_registry.yaml` =
**174** raw id rows; the lint's own line = "165 entries [79 WANTED], 9 bulk
rows" — i.e. **174 == 165 paper entries + 9 bulk rows** (binary/lineage/
manuals blocks, not papers). The landing's "lit 165 PASS" uses the
paper-entry basis; this gate's Category-5 arithmetic uses neither (it is
file-level over the 25 arrivals) — bases now all named, no drift
(re-measured vs 15a2dd6 by the sweep, OBS-1).

==============================================================================
## GATE VERDICT (orchestrator, 2026-08-21, clause-D file carrier)

**PASS.** Basis (per COVERAGE_GATE_spec.md (D)): (1) arithmetic at zero
in ALL categories post-repair — hypotheses 18 = 15+3+0 (GEOM restored);
choices 62 = 48 COVERED + 14 PARTIAL(owner+trigger verified) + 0;
claims 163 lint-covered; forks 141 = 139 + 0 + 2 (H20, P34 — both
seeded as findings rows with owners); novel items 32 = 31+1+0 (prior
queue recounted EMPTY); arrivals 25 = 22+3+0. (2) CRITIC consumed:
verdict MATRIX-HAS-OMISSIONS -> ALL CGC-1..8 repaired this window
(recounts + mints C61/C62 + census artifact + 13-check file carrier);
candidate-8 (SDP backend) NAMED with home, not minted (declared).
(3) DUAL-SEED PROVEN both directions: SEED-OMIT P34 caught (CGC-1,
CRITICAL, grep-proven); SEED-DECOY C50 not flagged ("fully covered,
verified" in not_flagged). Pre-registration carrier: commit 634b972
(late-commit F-2 declared and discharged). Lints at verdict (verbatim
in the repair report + VERDICT-INPUTS): findings 249/207 PASS,
glossary 47/238 PASS (unresolved 52 == baseline), literature 165
[79 WANTED] PASS, claims PASS. The no-row class stands at SEVEN
caught instances (C49/C56/C58/C59/C60/C61/C62) + 1 named candidate;
the enumeration is now census-carried (FOUNDATION_ENUM_census_c4.md).
