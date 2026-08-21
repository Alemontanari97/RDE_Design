# COVERAGE GATE — ADVERSARIAL COMPLETENESS CRITIC (S-FOUNDATIONS-C4)
# Executed 2026-08-21. Role: blind-spot hunter on the coverage ACCOUNTING itself
# (spec (C), as extended by the C4 gate brief). Dual-seeded by the orchestrator;
# seeds not disclosed to this agent.
# Read IN FULL this window: COVERAGE_GATE_spec.md, blocco3/COVERAGE_GATE_c4.md,
# blocco3/ORCH_ACTS_SWEEP_c4.md, blocco3/FORK_LEDGER_141.md,
# blocco3/FORK_LEDGER_141_adjudication.md, docs/choice_ledger.yaml id/status/
# title census (60 rows re-measured), SESSION_STATE_checkpoint.md C4 live
# section (:1-:557), COVERAGE_GATE_result.md (prior gate, for continuity
# checks). Every count and every absence claim below is from a command run in
# THIS window (SR-12); the command is quoted at the claim. Mandate discipline:
# the ENUMERATION is attacked, never the adjudications (authorities of record
# — VERDICT_r22f/VERDICT_blocco2/VERDICT_escalation_c4/H13 resolution — not
# re-litigated).

------------------------------------------------------------------------------
## FINDINGS

### CGC-1 (CRITICAL — omitted NOT-COVERED row): **P34 is absent from the
Category-4 matrix; the category denominator is 140 against a source-of-record
denominator of 141.**
- Missing item: fork **P34** (staged evidence hierarchy for engine-level
  claims), adjudicated **GENUINELY NOT-COVERED** — one of exactly TWO genuine
  gaps — by the gate's own declared source: FORK_LEDGER_141_adjudication.md
  table row P34 (:81) and machine summary ("2. P34 — the staged evidence
  hierarchy ...; owner = P-1/G5-G6 claims window"; "139 + 2 = 141.
  Reconciled."). Independently of record in commit a85e355 ("2 genuine gaps
  (H20 F4b; P34 P-1 window); 141 = 139 + 2") and in the findings registry row
  minted THIS window (docs/findings_registry.yaml:2533, P34 magnitude quoting
  the adjudication).
- Search proof of the omission: `grep -c "P34"
  validation/sfoundations_raws_2026-08-13/blocco3/COVERAGE_GATE_c4.md` = **0**
  (measured). The Category-4 header states "V 34 + H 41 + O 32 + P 33 = 140
  rows in this matrix" while its own named source is titled FORK_LEDGER_**141**;
  the P row's COVERED-BY-CLUSTER list carries 14 ids (P34 dropped from the
  adjudication's 14-id list is correct — P34 was never by-cluster — but the P
  NOT-COVERED cell reads 0 with row total 33, i.e. the fork vanished entirely
  rather than landing in NOT-COVERED).
- Where it must appear: (i) Category-4 P row: NOT-COVERED 1, row total 34,
  grand total 141; (ii) ZERO ARITHMETIC (4): **141 == 139 COVERED + 0 PARTIAL
  + 2 NOT-COVERED (H20, P34)**; (iii) the "single NOT-COVERED" paragraph and
  the machine-summary `not_covered_findings` JSON must carry a second entry:
  P34, owner P-1/G5-G6 claims window, nearest record diff §4.10
  (declared "no row"), findings carrier :2533.
- Severity: CRITICAL — the gate's headline arithmetic ("reconciled in all 5
  categories") is false as written; a genuine finding-of-record with a named
  owner is silently absent from the accounting matrix.

### CGC-2 (HIGH — spec category not run): **the spec's inventory category 5,
NOVEL ITEMS, has no accounting in the C4 gate.**
- The binding spec (COVERAGE_GATE_spec.md (A), read in full) names five
  inventory categories; its category 5 = "the 16 Phase-B §2 items +
  hypothesis-audit bundles (6) + contract-blind demands". The C4 brief EXTENDS
  the spec with 3 categories — extension, not substitution. The delivered
  COVERAGE_GATE_c4.md runs: hypotheses / choices / claims / forks / ARRIVALS
  (an extension category). The spec's NOVEL ITEMS category is nowhere:
  `grep -in "novel\|phase-b\|contract-blind"
  blocco3/COVERAGE_GATE_c4.md` = **0 hits** (measured).
- Why it is live, not vestigial: the prior gate closed this category only
  with a queue — COVERAGE_GATE_result.md F2-repair block: "32 == 8 minted +
  13 mapped/certified + **11 queued-by-name** + 0 uncarried". The landing
  status of those 11 queued-by-name items (F-4..F-10, D-1/D-2/D-4, §4.5,
  §4.10) is exactly what a C4 re-run would have to account — note that one of
  them, **§4.10, is the P34 locus of CGC-1**: the one category that was
  skipped is the one that owned the fork the matrix lost.
- Where it must appear: a Category (spec-5) section in the gate file with the
  32-item denominator re-measured and a disposition per item (most will be
  COVERED with C3/C4 anchors; the point is the arithmetic, not the outcome).
- Severity: HIGH — a whole spec denominator is missing from "full
  zero-arithmetic" (checkpoint clause (E) wording), and its absence provably
  correlates with the CGC-1 loss.

### CGC-3 (HIGH — extension category run without an accounting carrier):
**the FOUNDATION-CHOICE ENUMERATION category has no enumeration section or
file — only its mint side-effects exist.**
- The C4 gate brief adds FOUNDATION-CHOICE ENUMERATION as a gate category.
  What exists on disk: the C59/C60 ledger rows (:785/:797, notes "Minted
  2026-08-21 at the S-FOUNDATIONS-C4 COVERAGE GATE, FOUNDATION-CHOICE
  ENUMERATION category", each with its own dedup grep), the G-14 home note
  (lit :428) and the H20/P34 findings rows (:2522/:2533). What does NOT
  exist: any section of COVERAGE_GATE_c4.md, or any blocco3 file, recording
  the ENUMERATION itself — the class definition swept, the record surfaces
  searched, the candidate list weighed, and the closing census ("N instances,
  no further found"). Search proof: the full blocco3 directory listing
  (globbed this window, 81 files) contains no FOUNDATION_* / enumeration
  artifact; `grep -cn "glossary" blocco3/COVERAGE_GATE_c4.md` = 0 and the
  gate file's only trace of the category is the header's mid-window-growth
  note on C59/C60.
- Consequence, proven by CGC-4 below: without the census step the enumeration
  stopped at the two instances already named in its inputs (the injection's
  temporal-form candidate and the adjudication's D-1 rider) — it never HUNTED.
  A category whose mandate is "find what is practiced but unrowed" that only
  executes pre-named mints is not run; it is transcribed.
- Where it must appear: an enumeration section in the gate file (or a
  dedicated blocco3 artifact) with: class definition, the sweep commands, the
  candidate table (found / rejected-with-reason), and the mints as outcomes.
- Severity: HIGH — the category's arithmetic is unfalsifiable as delivered.

### CGC-4 (HIGH — the hunted SIXTH instance): **the base-pressure closure
model (p_b) is a practiced-but-unrowed foundation choice — the sixth instance
of the C49/C56/C58/C59/C60 class, missed by the enumeration.**
- Practiced: the Veen constant closure p_b = 0.846·p/M^1.3 is IN the compiled
  legacy chain of record (lit row vander_veen_1974 :428 summary: "base
  constants 0.846/M^1.3 -> sec.7.5 unreliability row"; GENO practice of
  record).
- Weighed of record OUTSIDE the ledger, THIS window: BASE_PRESSURE_HARVEST_c4.md
  adjudicates the full closure stack — Veen traced to a 1966 cold near-wake
  curve fit FAILED by WG10 ("N2 MUST REPLACE IT"), WG10 bracket [+19%,−15%]
  best pure-empirical on cold data, Nasuti-Onofri transition-PR the only
  validated classical piece — and the Humphreys 1971 exhibit shows the p_b
  closure choice moves the design ARGMAX ×2.45 at +0.26% value (a
  channel-(vi)-shaped, i.e. FOUNDATION-grade, sensitivity). The open question
  is carried only by findings rows (litreview:residue-r8-r23-base-pressure-
  pb2-blocking :2092, trigger "PB-2 base-pressure closure window"; H20 :2522
  carries the neighboring solve mechanics, not the closure-model choice).
- Search proof of unrowedness: `grep -niE "base.pressure|p_b|Veen|base-pressure"
  docs/choice_ledger.yaml` = **0 hits** (measured); the 60 `choice:` titles
  (listed this window) contain no p_b/base axis — "Thermo closure" (:399) and
  "leggeAree bracket" (:624) are different axes.
- This is the C60 precedent shape verbatim (C60 note: "WEIGHED of record
  OUTSIDE this ledger ... but NO ledger row carried it"): alternatives exist
  and were compared at record grade (Veen / WG10 bracket / Nasuti-Onofri /
  N2 mechanistic / Purdue-datum-anchored), an incumbent is practiced, a
  replacement is mandated — and no C-row exists for a future flip to consume
  via a pinned falsifier.
- Where it must appear: choice-ledger mint (status NEVER or MIXED,
  incumbent-declared = legacy Veen with the FAILED verdict on its face, owner
  = N2/F4b window, evidence = BASE_PRESSURE_HARVEST_c4.md + findings :2092)
  + a row in the CGC-3 enumeration census.
- Severity: HIGH — the exact defect class the category exists to catch,
  demonstrated live in the same window the category claims to have run.

### CGC-5 (MEDIUM — seventh candidate, same class): **phase quadrature over
Ξ (the discretization of the phase AVERAGE itself) has no ledger row.**
- Weighed: diff §2.10 "phase-quadrature stratification" is the sole coverage
  anchor for FOUR forks across all trees (V4, H33, O2, P10 — FORK_LEDGER_141
  rows), plus the §4.3 FFT probe; a bar-accounting residue rides findings
  :988 (phase-diagrams:eps-tolerance-omits-quadrature-bar). Practiced: every
  averaged-functional evaluation of record uses a finite phase set.
- Search proof: `grep -niE "quadrat" docs/choice_ledger.yaml` = **0 hits**
  (measured); C27 (:429 "Constraint aggregation") is the CONSTRAINT
  aggregation axis, not the objective's quadrature rule.
- Caveat kept honest (zero inflation): unlike CGC-4 no in-record adjudication
  AMONG alternatives (equispaced-FFT vs stratified vs Gauss vs adaptive) has
  been performed — the axis is weighed once, in one place, with no
  alternatives table; it may deserve a row OR a declared canonicity argument
  (the C59 pattern: periodic pin makes trapezoid/FFT spectrally optimal —
  but then THAT should be the row's incumbent text). Either outcome needs a
  carrier; today there is none.
- Where: the CGC-3 enumeration census, with a mint-or-canonicity decision.
- Severity: MEDIUM.

### CGC-6 (MEDIUM — dropped prior-gate PARTIAL): **the Category-1 basis
switch (spec 12-item table → problem-book 17-row §9 ledger) silently drops
the prior gate's open GEOM PARTIAL.**
- The spec fixes the Category-1 denominator as the 12-item problem-statement
  table (I-GEO ... GEOM, S1). The prior gate accounted it "12 == 10 COVERED +
  2 PARTIAL-with-owner (**GEOM** cone/attachment -> census-lemma window,
  F2-exit user pin; **S1** ...) + 0 NOT-COVERED" (COVERAGE_GATE_result.md
  (B)1, read this window). The C4 gate switches to the 17-row §9 H-ledger
  (denominator command quoted, 17 measured — correct for THAT basis) without
  declaring the mapping. The S1 PARTIAL was carried forward (D3 row cites
  "prior-gate PARTIAL owner ... — both landed"); the GEOM PARTIAL was not:
  `grep -cn "GEOM\|census-lemma" blocco3/COVERAGE_GATE_c4.md` = **0**
  (measured), and the §9 ledger (read this window, :488-:504) contains no
  geometric-admissibility row for it to map onto.
- Where: Category 1 needs either (i) the declared 12→17 mapping with GEOM
  carried as a PARTIAL row (owner census-lemma window / F2-exit pin,
  unchanged), or (ii) an explicit discharge citing where GEOM closed since
  2026-08-17 — if such an anchor exists it is not in this gate file.
- Severity: MEDIUM — an open PARTIAL with a named owner fell out of the
  accounting chain between gates; owner still exists, so no loss yet, but
  the gate-to-gate continuity the spec's standing-adoption clause promises
  is broken exactly where it matters.

### CGC-7 (LOW — verdict-input recount missing): **the gate file does not
recount the six same-window mint duties (ORCH sweep F-3) nor consume the
sweep's F-1/F-2 repair paths.**
- ORCH_ACTS_SWEEP_c4.md F-3 (binding): "the gate verdict MUST recount these
  six before PASS". Recount performed by THIS critic (measured): C59 :785 OK,
  C60 :797 OK, G-14 vander_veen_1974 note :428 OK, H20 findings :2522 OK,
  P34 findings :2533 OK — **5/6 landed**; the 6th (glossary 85→52
  resolution) has NO carrier found: blocco3 holds only the C3-era
  GLOSSARY_SR4_resolution_report.md (158→52, tokens_end 52), and
  `grep -cn "glossary" blocco3/COVERAGE_GATE_c4.md` = 0.
- F-2 still open at critic delivery: `git status --short` shows
  SESSION_STATE_checkpoint.md **M** (uncommitted) — the dual-seed
  pre-registration's tamper-evidence repair ("commit before consuming the
  critic's output") is unexecuted as of this file's writing.
- F-1's repair path (re-run the 13 JUDGE-DELIVERY checks from files inside
  the gate result) is absent from the gate file; OBS-1's ask (state the
  lit-count basis, 165 lint vs 174 raw ids) is likewise unaddressed anywhere
  in it (`grep -n "165\|174"` on the gate file hits only a claims line-number
  coincidence, :99).
- Where: the gate VERDICT section (still to be written) must carry the
  six-item recount (this critic's five confirmations may be cited but the
  glossary item needs an actual carrier), the 13-check file-based re-run, and
  the checkpoint commit before PASS.
- Severity: LOW individually — but PASS without these is a spec-(D)
  violation, so they are gate-blocking in aggregate.

### CGC-8 (LOW — sweep scope miscount): **ORCH_ACTS_SWEEP_c4.md's own scope
line miscounts its commit denominator: "the 10 C4 commit messages `git log
--oneline 3db05d5~1..HEAD`" — the quoted command yields 11.**
- Measured this window: `git log --oneline 3db05d5~1..HEAD | wc -l` = **11**.
  The commit never cited in any carrier cell of the act table is **b3da86d**
  (mid-window 5, base-pressure harvest). No phantom act results — act 24
  covers the harvest via checkpoint :364-397 — but the sweep's denominator
  claim fails its own SR-12 standard, and the uncited commit is precisely the
  carrier of the CGC-4 subject matter (the harvest whose choice-axis the
  enumeration missed). Where: sweep scope line correction + b3da86d added to
  act 24's carrier cell.

------------------------------------------------------------------------------
## DECOY / NON-FINDINGS DISCIPLINE (zero inflation)

Items examined and deliberately NOT flagged, with grounds:
- **C50**: fully covered — closed 2026-08-20 with authority of record
  (VERDICT_C50_form2 per checkpoint (B)), Category-2 MIXED row with owner,
  consumed as anchor by Category-1 H-mu and by fork adjudications V3/P4/P8.
  Its enumeration is clean everywhere it appears. No finding.
- Category-2 arithmetic: independently re-measured this window
  (`grep "^  status:"` census: DECIDED 12 / MIXED 36 / NEVER 10 / SA 2 = 60;
  DECIDED id set matches the gate's 12) — confirmed, no finding.
- Category-1 denominator 17 on the §9-ledger basis: re-counted from the
  table read this window — correct on its own basis (the basis itself is
  CGC-6).
- Category-5 arrivals denominator: manifest grep re-run this window = 21;
  +4 campaign rows = 25 — confirmed; the Uno dedup (2 files → 1 row) and the
  3 declared-unread-with-owner rows are correctly accounted. No finding.
- Category-3's lint-based blanket COVERED for the 150 pre-C4 claims follows
  the prior gate's declared BY-COMPOSITION convention (COVERAGE_GATE_result.md
  (B)3: per-theorem re-derivation "was NEVER this session's mandate"),
  inherited without restatement. Borderline as a declaration defect, but the
  convention is of record and the 13 in-window rows are individually
  anchored — not flagged as an omission.
- H13 resolution, K1 convention, D-1 discharge-by-C60: adjudications of
  record — not re-litigated per mandate.

------------------------------------------------------------------------------
## MACHINE SUMMARY

```json
{
  "critic": "S-FOUNDATIONS-C4 COVERAGE GATE — ADVERSARIAL COMPLETENESS CRITIC",
  "verdict": "MATRIX-HAS-OMISSIONS",
  "findings": [
    {"id": "CGC-1", "severity": "CRITICAL", "class": "omitted NOT-COVERED row", "item": "fork P34 absent from Category-4 matrix; denominator 140 vs 141 of record", "where": "Category-4 P row + ZERO ARITHMETIC (4) + not_covered_findings JSON", "proof": "grep -c P34 COVERAGE_GATE_c4.md = 0; FORK_LEDGER_141_adjudication.md 141=139+2; findings :2533"},
    {"id": "CGC-2", "severity": "HIGH", "class": "spec category not run", "item": "NOVEL ITEMS (spec (A)5: 16 diff-§2 items + 6 hypaudit bundles + contract-blind demands; prior gate left 11 queued-by-name)", "where": "new Category (spec-5) section", "proof": "grep -in 'novel|phase-b|contract-blind' COVERAGE_GATE_c4.md = 0"},
    {"id": "CGC-3", "severity": "HIGH", "class": "category without accounting carrier", "item": "FOUNDATION-CHOICE ENUMERATION has mints but no enumeration census artifact", "where": "gate-file enumeration section or blocco3 artifact", "proof": "blocco3 glob (81 files): no enumeration artifact; gate file carries only the C59/C60 header note"},
    {"id": "CGC-4", "severity": "HIGH", "class": "practiced-but-unrowed foundation choice (SIXTH of the C49/C56/C58/C59/C60 class)", "item": "base-pressure closure model p_b (Veen practiced; harvest-adjudicated Veen-FAILED/N2-must-replace; no ledger row)", "where": "choice-ledger mint, owner N2/F4b window", "proof": "grep -niE 'base.pressure|p_b|Veen' docs/choice_ledger.yaml = 0; BASE_PRESSURE_HARVEST_c4.md; findings :2092"},
    {"id": "CGC-5", "severity": "MEDIUM", "class": "same class, seventh candidate", "item": "phase quadrature over Xi (objective's phase-average discretization) unrowed; needs mint or declared canonicity", "where": "enumeration census", "proof": "grep -niE 'quadrat' docs/choice_ledger.yaml = 0; sole anchor diff §2.10 covering V4/H33/O2/P10"},
    {"id": "CGC-6", "severity": "MEDIUM", "class": "dropped prior-gate PARTIAL", "item": "GEOM cone/attachment PARTIAL (owner census-lemma window) lost in the 12-item->17-row basis switch", "where": "Category-1 mapping declaration or discharge anchor", "proof": "grep -cn 'GEOM|census-lemma' COVERAGE_GATE_c4.md = 0; COVERAGE_GATE_result.md (B)1"},
    {"id": "CGC-7", "severity": "LOW", "class": "verdict-input recount missing", "item": "F-3 six-mint recount absent from gate file (critic recount: 5/6 landed, glossary 85->52 carrierless); F-2 checkpoint still uncommitted; F-1 13-check file re-run absent; OBS-1 basis unaddressed", "where": "gate VERDICT section before PASS", "proof": "git status M on checkpoint; grep glossary = 0; mints verified :785/:797/:428/:2522/:2533"},
    {"id": "CGC-8", "severity": "LOW", "class": "sweep scope miscount", "item": "ORCH sweep claims 10 commits, command yields 11; b3da86d (harvest) uncited in any carrier cell", "where": "sweep scope line + act 24 carrier cell", "proof": "git log --oneline 3db05d5~1..HEAD | wc -l = 11"}
  ],
  "not_flagged": ["C50 (fully covered, verified)", "Category-2 arithmetic (independently confirmed 12/36/10/2=60)", "Category-5 arrivals denominator (21+4=25 confirmed)", "Category-3 by-composition convention (inherited of record)", "H13/K1/D-1 (adjudications, out of mandate)"],
  "all_counts_measured_in_window": true
}
```
