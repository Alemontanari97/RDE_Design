# EXPERT POSITION P3 — Repo constraints & right-sizing
# S-ORDINE Phase 2 (census R32), 2026-08-13.
# Contract: validation/ADVISORY_Sordine_prompt_2026-08-12.md (read in full).
# Inputs: all 7 Phase-1 inventories (seg1-seg7, read in full) +
# docs/findings_registry.yaml (20 rows, read in full) + spot-checks of
# originals listed in §0.2. Verdicts S14-S25bis are of record and are
# NOT re-litigated here. Proposals numbered P3-1.. for refuter/judge.

---

## 0. THE LENS, AND THE MEASURED CONSTRAINT FACTS

### 0.1 What R1-R6 structurally require of any target structure
- R1 (no orphan step): every artifact must carry a nameable plan need.
  Structural consequence: the PLAN-ANCHOR field is not a nicety — it is
  the machine form of R1, and the target structure must make an artifact
  WITHOUT an anchor loudly visible (index lint), not silently absorbed.
- R2 (session opening): the opening read-set is memory + M0 + PROGRESS.
  Structural consequence: whatever we build must be REACHABLE from those
  three (a pointer in PROGRESS/CLAUDE.md to the index and registries),
  or it will not be read and will rot. A structure the opening protocol
  does not surface is entropy with better formatting.
- R3 (closure): PROGRESS ORA/NEXT/BLOCCATO + LOG must remain the single
  living-state object. Structural consequence: the census consolidation
  (T2(iv)) changes the SHAPE of PROGRESS, not the R3 contract; the
  closure checklist is the correct insertion point for new duties
  (one line, not a new document).
- R4 (nothing lost / retro-propagation): archive != delete; every
  supersession explicit and dated. The corpus ALREADY has a working
  convention (seg1 F-SEG1-4: original preserved + dated in-place
  marker). Structural consequence: we lint the existing convention;
  we do not invent a second one.
- R5 (numbers/claims discipline): every lint must have a seeded
  rejector that fires each run. Structural consequence: a proposed lint
  without a rejector does not ship; a lint nobody re-runs is entropy
  (this position holds new lint groups to the same bar as carriers).
- R6 (gates): suite is exit-code-gated, redirect-only. Structural
  consequence: new lints go INTO tests/run_all.py tiers (FAST), not
  into free-standing scripts that drift.

### 0.2 Measured coupling facts (spot-checked this session — the priced constraint is real)
1. `docs/claims_registry.yaml` carries **67 occurrences of
   `validation/...` paths** (doc/carrier anchors). Moving or renaming
   any validation/*.py invalidates registry anchors checked by lint
   group (xv).
2. `tests/test_rigor_carriers.py` **hardcodes 10 carrier paths**
   (`validation/pa1_symbolic_lemmaA.py` ... `validation/gbe_ergodic_envelope.py`);
   test_rigor_dualroute / test_t3qs / test_rigor_interval do the same
   for X-P2A1 / X-T3QS / X-IVXC.
3. `docs/findings_registry.yaml` code-dedup keys are **path:line-RANGE
   anchors** (`validation/a1_toc_variational_jax.py:516-522` etc.).
   Moving a file breaks them; even heavy in-place editing shifts lines.
   (Consequence beyond moves: any hygiene edit to a carrier body is
   registry-anchor-relevant — an argument for touching carriers ZERO
   times in this session.)
4. `validation/numeric_lint_baseline_validation.json` (R28 ratchet) is
   keyed **per-file path** for 33 validation/ files with 622 baselined
   literals; a move = unbaselined-file FAIL by design.
5. Advisories cross-cite each other and the logs by full
   `validation/<name>.md` paths in prose (hundreds of textual
   citations, e.g. every "cited by" row in seg3/seg4). Prose citations
   are not lint-resolved; a physical move silently strands them.
6. Windows/env: MS-Store Python 3.13, cp1252 console (memory
   python-env-cantera), single host, numpy pin history + BLOCCATO-8
   filelock lesson (adding a dependency is a USER decision). New lints
   must be **stdlib-only, ASCII-safe output, redirect-only**.
7. ONE-SESSION-AT-A-TIME + freeze-on-tracked-files-while-consumer-runs:
   the migration must be serial, small-step, each step verified before
   the next; any spill-over queue must be a NAMED first duty (never
   generic), per never-postpone-resolvables.

### 0.3 The P3 thesis in one paragraph
The repo already contains its own de-entropy prior art: SCAFFOLD L0-L6
(typed registry + layered reading order + lint + migration-with-
acceptance, executed S9) and the R28/R31 lint patterns (ratchet
baseline; strict-subset schema; seeded rejectors). The SOTA move here
is NOT new machinery — it is EXTENDING those three proven patterns to
the layers they do not yet cover (validation/ index, literature,
glossary, choices) while moving **zero code files**, renaming
**nothing**, and converting archive/supersession into a **status
system readable by machine** rather than a directory reshuffle. Every
instrument below is priced against its maintenance cost; anything that
does not earn a rejector-gated lint or a one-line checklist duty is
deliberately not built (§7).

---

## 1. TARGET STRUCTURE (P3-1 .. P3-7)

**P3-1 (physical tree: minimal delta, zero moves of anchored files).**

```
docs/                                    [UNCHANGED file set, + 4 new]
  rde_nozzle_MASTER.md .. D1-D8, attacks  (untouched; in-place dated
                                           supersession markers remain
                                           the mechanism, now linted)
  rde_nozzle_development_plan.md          (untouched)
  rde_nozzle_PROGRESS.md                  (SLIMMED: ORA/NEXT/BLOCCATO +
                                           ONE consolidated census table
                                           R1-R33 + open LOG pointers)
  rde_nozzle_PROGRESS_ARCHIVE.md          [NEW] (delta blocks, stale
                                           NEXT blocks, fossil S1-S13
                                           LOG tail — moved verbatim
                                           under dated banners)
  claims_registry.yaml                    (untouched)
  findings_registry.yaml                  (grows via R31 seeding)
  choice_ledger.yaml                      [NEW] (T2(ii), 45 rows from
                                           gap-map annex C1-C45)
  literature_registry.yaml                [NEW] (T2(vi), 3 roots)
  glossary.yaml                           [NEW] (T2-bis(a), namespace-
                                           qualified tokens)
  flag_registry.yaml                      [NEW, small] (T2-bis(b), one
                                           row per A1_* env flag)
  roadmap_geno_rde.md                     (+ dated supersession banner
                                           pointing at D6 — F-SEG1-1)
validation/                              [NO .py MOVED, NO FILE RENAMED]
  ADVISORY_INDEX.md                       [NEW] one row per validation/
                                           *.md: file | class | status |
                                           plan-anchor | supersession ->
                                           | at-risk pointer
  INDEX.md                                (existing session-log index;
                                           kept; referenced by
                                           ADVISORY_INDEX, not merged)
  ADVISORY_*.md / AUDIT_* / PANEL_* /     (IN PLACE; status lives in the
  DISPATCH_* / PROGRESS_*.md               index + in-file banner where
                                           superseded/consumed)
  sordine_raws_2026-08-13/, sota_gapmap_  (IN PLACE; class RAW in index)
  raws_2026-08-12/
  *.py carriers/probes (33)               (UNTOUCHED — priced constraint)
  *.json gate memos (25), *.log (24)      (IN PLACE; classed in index)
memory/                                  (sweep only: banners on stale
                                          routing halves, 3 link fixes,
                                          1 stale MEMORY.md line fix —
                                          no restructure)
```

**P3-2 (logical archive over physical archive — divergence from the
prompt letter, declared).** The prompt T2(iii) names `archive/` with
banners. P3 prices a physical `validation/archive/` move against fact
0.2(5) (prose citations by full path in ~80 documents) and finds the
default should be **archive-as-status**: dated banner AT THE TOP of the
superseded/consumed file + `status: ARCHIVED(<reason>)` in
ADVISORY_INDEX. A physical `archive/` directory is created ONLY IF the
judge wants visual separation, and then admits ONLY files that pass a
pre-move check: (a) zero machine anchors (registries, tests) AND
(b) repo-wide grep of the basename shows only citations the mover
updates or declares acceptably-stale in the index row. Candidate set
today is small and known: the 6 CONSUMED session prompts,
ADVISORY_plan_v2_draft (superseded), DISPATCH_Sspeed_to_S25 (fully
redundant per seg4). Everything else stays put. Rationale: a banner
gives 100% of the R4 value at ~0% of the breakage risk; a directory
gives a nicer `ls` at real risk. Right-sizing verdict: banner first.

**P3-3 (PLAN-ANCHOR as the default navigation).** The traceability
"need -> artifact -> SOTA proof" becomes the default navigation by
making it a COLUMN, not a doc:
- ADVISORY_INDEX row: `plan-anchor` = D6 phase / census row / registry
  id / gate / standing directive (at least one, else the row is an
  ORPHAN FINDING and the lint fails — R1 mechanized).
- findings/choice/literature registry rows: already carry (or gain)
  owner/plan-anchor fields in schema.
- Navigation spine, written once in ADVISORY_INDEX header and pointed
  to from PROGRESS opening block: **D6 phase -> census row (PROGRESS
  consolidated table) -> registry rows (findings/claims/choices/lit)
  -> artifacts (index rows) -> carriers/gates**. A cold reader (the
  S-CERT MC6 navigation test is the named consumer) starts at D6 or
  PROGRESS and reaches any artifact through typed rows only.

**P3-4 (SCAFFOLD is extended, not duplicated — F-SEG1-3).** The target
structure registers itself as a SCAFFOLD amendment: one new dated
section in docs/rde_nozzle_SCAFFOLD.md declaring the added layers
(validation index; literature registry; glossary; choice ledger; flag
registry) as extensions of L0-L6. No second architecture document is
created. This is the cheapest possible defense against the "two
competing taxonomies = new entropy" failure mode.

**P3-5 (LECTURE-ERA layer tag).** The 17 lecture-era validation docs
(seg5 §B) get index rows with layer tag `LECTURE-ERA` (plan-anchor =
repo-sota-standard / G1 substrate). A tag, not a move: they are the
certification substrate G1 inherits from and their paths are cited by
README badges.

**P3-6 (memory target state).** No restructure. Deliverables of the
sweep (T2(v)): dated supersession banner on the ROUTING half of the 9
unmarked historical session memories (verdict halves untouched, per
seg6 F2); fix the 3 broken [[links]] (seg6 F3); fix the stale MEMORY.md
numpy line (seg6 F1); type the two inline-only entries (POST-S20,
POST-S21-SERA) into small backing files or an explicit "inline
window-record" marker. research-cycle-averaged-rao.md S1-S13 accretion:
banner the historical half, do NOT rewrite (same pattern as PROGRESS,
but memory is outside the repo — no lint reaches it, so this stays a
checklist duty, honestly declared as such).

**P3-7 (things that stay exactly where they are).** All docs/ theory
files; all validation/*.py; all data/; all tests/; GENO/ (read-only,
never committed from here); the parent directory (outside repo
jurisdiction — its at-risk items become REGISTERED duties, §6/UD-8,
never executed by reaching outside the repo in this session).

---

## 2. STATUS TAXONOMY (P3-8 .. P3-10)

**P3-8 (the enum — six values + two qualifiers, no more).**
- `OF-RECORD` — current authority for its content. May be qualified
  `OF-RECORD(living)` (PROGRESS, INDEX, registries).
- `SUPERSEDED-BY:<path-or-id>` — replaced; dated banner in-file;
  pointer must resolve.
- `CONSUMED` — an order/prompt/dispatch fully executed; pointer to the
  consumer (log/commit/advisory) required. Variant
  `CONSUMED-with-residue:<pointer>` when named rows remain live (e.g.
  ADVISORY_engine_speed_audit N1-N8/DEAD/quarantine until re-homed).
- `RAW` — agent output whose adjudicated verdicts live upward; never
  citable as authority (existing rule, now written on the row).
- `DERIVED` — regenerable evidence/cache (.log, .pyc, extracts,
  figures); listable without unique content.
- `PENDING-CONTRACT` — a live future-session prompt
  (ADVISORY_Scert_prompt: may not be archived or altered; seg3 flag).
Qualifiers (tags, orthogonal to status): `LECTURE-ERA`;
`AT-RISK:<ledger-id>` (points into the consolidated at-risk ledger
while an item still lacks its destination).

**P3-9 (supersession discipline = the existing convention, linted).**
Format of record (already in corpus use, seg1 F-SEG1-4):
`SUPERSEDED (YYYY-MM-DD[, session]) -> <pointer>` as an in-place
marker; original text preserved below/around it. New rule with teeth:
every occurrence of the string `SUPERSED` in docs/*.md and
validation/*.md must parse to date + resolvable pointer — enforced by
lint (xxiii) with a frozen baseline for legacy free-form markers (R28
ratchet pattern: baseline == reality, growth of unparsed markers
forbidden, baseline ratchets down as legacy markers are normalized).

**P3-10 (status change protocol).** A status is changed only by editing
the index row (and in-file banner where applicable) with a date, in the
same window as the event that changes it (e.g. a prompt flips to
CONSUMED in the closure window of the session that executed it). One
status per artifact; disagreements between banner and index are a lint
(xx) failure, index is authoritative for STATUS, file content remains
authoritative for CONTENT (mirror of the SCAFFOLD "registry = index
never content" conflict rule).

---

## 3. WHAT GETS TYPED + LINTED (P3-11 .. P3-17)

All new lints: stdlib-only, text-parsing, FAST tier, each with >=1
seeded rejector firing every run (R5), each < ~1 s wall. Registry
schemas follow the strict-subset precedent (findings_registry schema as
the parent shape; claims lint as the anchor-resolution precedent).

**P3-11 — Group (xx): advisory-index coverage lint**
(`tests/test_advisory_index.py`). Checks: (a) every `validation/*.md`
(recursive, incl. raws dirs) has exactly one ADVISORY_INDEX row;
(b) every row's path exists; (c) status in the P3-8 enum; (d) every
SUPERSEDED/CONSUMED row's pointer resolves (file exists or registry id
exists); (e) every row has a non-empty plan-anchor (R1 mechanized) or
carries the explicit token `ORPHAN-FLAGGED` (which is a visible state,
not a pass — count reported); (f) rejectors: a seeded phantom row, a
seeded missing-file, a seeded orphan. This is the single highest-value
new lint: it converts the flat directory from "77 untracked mysteries"
into a machine-checked catalog without moving anything.

**P3-12 — Group (xxi): literature registry lint**
(`tests/test_literature_registry.py`). Schema per row: path (per root:
REPO/PARENT/GENO), bibliographic identity, class
(literature-pdf/vendor-doc/extract/asset/presentation-lineage),
read-status enum `READ-INTEGRAL / READ-PARTIAL / UNREAD / WANTED`,
where-read anchor (advisory/doc/log path that must exist; for
WANTED — owner), dedup key (doi/identity string). Checks: enum
validity; anchor existence; WANTED => owner; the seg7 rule "UNREAD
never carries a content summary" (a row with read-status UNREAD and a
non-empty content field = violation); count reconciliation against the
three root lists. Rejectors: seeded UNREAD-with-summary; seeded
dead anchor. Right-sizing: one row per real literature item (13 + 10
+ 20 = 43 papers + named assets); the 52 GENO vendor-docs and 26 pptx
lineage enter as CLASS-LEVEL bulk rows with counts (typing 78 vendor
manuals individually is entropy, not rigor — declared limit in the
registry header).

**P3-13 — Group (xxii): glossary resolution lint, RATCHETED**
(`tests/test_glossary.py`). glossary.yaml rows: token, NAMESPACE
(mandatory — seg4/seg6 measured collisions: O5, M1, T2, F4, C1, L4,
A1, U1 each carry 2+ meanings), one-line meaning, home pointer
(registry id / doc anchor / index row). Lint: (a) schema; (b) every
glossary pointer resolves; (c) RESOLUTION CHECK with R28-style frozen
baseline — the checked corpus is the TYPED artifacts + docs/*.md status
blocks (first 40 lines), NOT the full history (scanning 82 advisories
+ 27 logs for token resolution would produce thousands of legacy
misses and a lint nobody keeps green = entropy). Tokens matching the
codename patterns (`\[X-[A-Z0-9]+\]`, `GAP-\d+`, `R\d+\b` in census
context, `C-[A-Z]`, `DIR-[A-Z]+`, `A1_[A-Z_]+`, `[MS]C?\d`-families as
declared) in the checked corpus must resolve to a glossary or registry
row; the unresolved set is baselined and may only shrink. Rejectors:
seeded unknown token; seeded baseline +1 bump. Seed content: the 5
Phase-1 token tables (214 + 178 + ~120 + 231 + 78 + 70 collected
entries, deduped — the readers already did the harvest; Phase-2 cost
is merge + namespace tags, not re-reading).

**P3-14 — Group (xxiii): supersession-marker lint** (P3-9 mechanics;
can live inside test_advisory_index.py as a second check-family to
avoid runner sprawl — one module, two families, both rejector-seeded).

**P3-15 — choice_ledger.yaml lint**: clone of the findings pattern
(group (xxiv) or folded as a section of test_findings_registry.py —
P3 prefers FOLDING: same strict-subset schema, same anti-re-mint span
rule where rows cite code, one runner already wired into (xix); a new
group number for an identical shape is runner sprawl). Status enum for
choices: `DECIDED / MIXED / SINGLE-AUTHOR / NEVER` with owner
obligatory on NEVER (the gap-map annex already carries exactly this —
extraction is mechanical, 45 rows).

**P3-16 — flag_registry.yaml lint** (inside (xix)'s module or the
index module): mechanical grep of `A1_[A-Z_]+` over validation/*.py +
tests/; every distinct flag found must have a row (default, meaning,
covering gate, tested-pairs list, cartesian-product-untested
declaration — the row content the S25-bis docstrings already carry);
a flag in code without a row = FAIL; a row without a flag in code =
FAIL (stale row). Rejector: seeded phantom flag. This is the cheapest
lint in the set and closes T2-bis(b) exactly.

**P3-17 — the 4-ter nothing-lost gate is SESSION-SCOPED, not a suite
group.** The at-risk ledger -> destination-map gate + loss-hunter +
seeded canary (contract 4-ter i-iii) run as one-shot scripts in
sordine_raws_2026-08-13/ during T2, gated on exit code, logged in the
session log. The PERMANENT residue is lint (xx)+(xxi)+(xxiii) coverage
— building the loss-hunter into the suite would be a lint nobody
re-runs on a corpus that no longer changes shape (anti-overengineering
verdict, declared).

---

## 4. MIGRATION PLAN (ordered; each step with its nothing-lost verification) (P3-18 .. P3-27)

Order rationale (fact 0.2(7)): durability first (commit), then
index (the map), then registries (the content), then slimming (the
only destructive-looking edit, done last when everything it references
is typed), then the gate. NO step moves or renames a file except the
optional P3-2 archive set, which runs LAST if ratified.

- **P3-18 / STEP 0 — durability snapshot (needs UD-1).** If the user
  ratifies committing: `git add` the of-record validation/*.md + *.json
  + the 7 inventories AS THEY ARE, before any banner edits, one commit
  `[F-SERVICE/SORDINE][PIANO/R32] pre-edit snapshot of untracked
  of-record corpus`. Verification: `git status` untracked .md/.json
  count drops to 0 for the declared set; file count in commit ==
  inventory counts (34 advisory-class + 27 logs + 21 other + 17+N raws
  + 25 json). Nothing-lost: trivially conservative (pure add).
  If UD-1 = NO: skip; the single-copy risk stays priced and OWNED
  (index rows gain tag `UNTRACKED-SINGLE-COPY`).
- **P3-19 / STEP 1 — ADVISORY_INDEX.md + lint (xx).** Build rows
  directly from seg3/seg4/seg5 inventories (they already contain
  class/status/plan-anchor per file). Verification: row count ==
  `ls validation -Recurse -Filter *.md` count, discrepancy 0; lint
  (xx) green with its 3 rejectors observed firing.
- **P3-20 / STEP 2 — banners.** Dated banners: roadmap_geno_rde.md
  (-> D6), ADVISORY_plan_v2_draft (-> plan_v3_panel, already
  self-declared), the 6 CONSUMED session prompts, DISPATCH_Sspeed
  (-> engine_speed_audit), interface_audit.md (CONSUMED note).
  Verification: lint (xxiii) parses every new marker; grep count of
  banners added == the enumerated list (9 files); no other file
  modified (git diff name-only check).
- **P3-21 / STEP 3 — R31 seeding into findings_registry.yaml, in
  tranches** (audit 94 -> then gap-map 36/16/10 -> then refuter/
  red-team S25/S25-bis). Dedup against the existing 20 rows is the
  registry's own machine rule. Verification PER TRANCHE: source row
  count == (new rows + explicitly-deduped rows + explicitly-declared
  not-seeded rows with reason) — the three-way count is written into
  the session log; lint (xix) green each tranche. NOTE the seg3 flag:
  before seeding, VERIFY the S25bis_diff_convergence repair-list
  R1-R13 execution status on the tree (registry row
  persistence:derive-artifact-intra-commit-staleness EXISTS and is
  DISCHARGED with evidence — the repair landed; confirm the R8 group-
  (xix) channel is in the suite) — highest-priority loss-hunter item,
  cheap to check first.
- **P3-22 / STEP 4 — choice_ledger.yaml (45 rows) + folded lint.**
  Verification: 45 == 45 (5 DECIDED + 3 MIXED + 12 SINGLE-AUTHOR + 25
  NEVER, the gap-map's own tallies); every NEVER has owner; lint
  green; gap-map annex gains a one-line pointer banner ("extracted to
  docs/choice_ledger.yaml <date>; this annex remains the provenance").
- **P3-23 / STEP 5 — literature_registry.yaml + lint (xxi).**
  Sources: seg7 (the direct source, self-declared), litmap advisory,
  choking advisory, lit_b0bis + its named session-log dependency
  (seg1 F-SEG1-5: PROGRESS_2026-07-16_rigore_PA.md step 13).
  Verification: 137-file reconciliation of seg7 reproduced (43 paper
  rows + bulk class rows summing to 137, discrepancy 0); WANTED rows
  (AIAA 2019-0197, Peter-Desideri 2022, Ancourt 2023, L-P 2023,
  Tillyaeva 1975, Naumova 1967, Breitkopf arXiv) each with owner;
  the seg7 glob line (`plt/mira_*.pdf`) expanded to literal files and
  recounted (declared list repair).
- **P3-24 / STEP 6 — PROGRESS slim + PROGRESS_ARCHIVE.** Mechanics
  (from seg1's measured block map): (a) create ARCHIVE file; move
  VERBATIM under dated banners: census delta blocks L295-491, stale
  NEXT blocks L1919-2149, fossil LOG tail L2183-2498, per-session
  summary blocks older than S24 (L~560-1918 below the S24 line);
  (b) in PROGRESS, write the ONE consolidated census table R1-R33
  (fold the S24 snapshot + S25 + S25-bis deltas + ORA-carried rows;
  one row per item: id | state | owner | trigger | last-touch date);
  (c) ORA/NEXT/BLOCCATO/current-session blocks unchanged.
  Verification (nothing-lost, mechanical): (i) every census row id
  R1-R33 appears EXACTLY once in the new table, and for each row the
  folded state cites the newest delta block that touched it (fold
  audit written to the session log); (ii) line-conservation: lines
  removed from PROGRESS == lines landed in ARCHIVE (verbatim move,
  byte-diff spot check on 3 random blocks); (iii) BLOCCATO 1-8
  preserved verbatim; (iv) R2 opening protocol still resolves (the
  ARCHIVE is pointed to from the PROGRESS header).
- **P3-25 / STEP 7 — glossary.yaml + lint (xxii).** Merge the 5
  Phase-1 token tables; namespace-qualify the measured collisions;
  baseline the unresolved remainder. Verification: merged-table count
  reported (source counts 214/178/231/78/70 + seg4's table -> deduped
  N declared); lint green with rejectors firing.
- **P3-26 / STEP 8 — flag_registry.yaml + memory sweep.** Flags: grep
  harvest, rows written, lint green (P3-16). Memory: the P3-6 list
  (9 banners, 3 link fixes, 1 index-line fix, 2 inline entries
  typed). Verification: memory sweep is checklist-verified in the
  session log (no repo lint reaches memory/ — honest limit, declared).
- **P3-27 / STEP 9 — garbage adjudication + 4-ter gate.**
  (a) `current_commit_messages.txt`: run the seg2-prescribed diff vs
  `git log --format=%B`; identical -> DERIVED, disposal per UD-3;
  different -> OF-RECORD provenance, commit it. (b) `er.name` +
  `t --count HEAD:q`: byte-identical derived debris — UD-3.
  (c) `mailmap.txt`: CONSUMED; keep-or-dispose UD-3. (d) parent hash
  lists: verify vs reflog, then UD-3/UD-8. THEN the 4-ter gate:
  consolidated at-risk ledger (from the 7 inventories' at-risk
  sections) -> destination map -> gate run -> seeded-canary rejector
  observed to FAIL -> loss-hunter run (10 random historical findings
  traced to their current home) -> 436-file + 3-root reconciliation
  at discrepancy 0. Session R3 closure is CONDITIONED on this gate
  (contract 4-ter(iv)).

**Budget honesty (0.2(7)):** Steps 0-2 + 5-9 are one-session-sized.
STEP 3 (audit 94-row seeding with find->verify) is the known heavy
item; if the budget breaks, the split point is DECLARED THERE and the
remaining tranches become the named first duty of the next window
(the registry's own SEEDING STATUS comment already carries this
pattern) — never a generic "finish later".

---

## 5. STANDING RULES DRAFT — the education half (P3-28)

Rules that FIRE (lint/gate), plus the two honest checklist-only rules
declared as such. Proposed CLAUDE.md/R3 deltas go to the user for
ratification (T3).

- **SR-1 (index-same-window).** Every new validation/*.md = its
  ADVISORY_INDEX row (+ registry rows for any finding of record) in
  the SAME session window. FIRES: lint (xx) at the closing suite run
  — an unindexed file fails R3 closure. [The T2-bis/T3 "R3 checklist
  line" of the contract, verbatim intent.]
- **SR-2 (dated supersession).** Any supersession = dated in-place
  marker + resolvable pointer. FIRES: lint (xxiii), ratcheted.
- **SR-3 (no unregistered codename).** A new [X-*]/GAP-*/C-*/DIR-*/
  A1_* token entering a typed artifact or doc status block = glossary
  or registry row in the same window. FIRES: lint (xxii) ratchet
  (baseline growth forbidden).
- **SR-4 (no unregistered flag).** New A1_* env flag in code = flag
  registry row with default + covering gate + tested-pairs. FIRES:
  P3-16 lint (code-grep vs registry symmetric diff).
- **SR-5 (census one-row-per-item).** The census is edited IN PLACE in
  the consolidated table (state/owner/trigger/date); delta blocks are
  BANNED; history goes to PROGRESS_ARCHIVE at close. FIRES: weakly
  lintable (a grep for `CENSIMENTO DELTA` headers in PROGRESS could be
  added to (xx) — cheap, include it); primarily an R3 checklist line.
- **SR-6 (prompt lifecycle).** A session prompt flips to CONSUMED
  (banner + index) in the closure window of the session that executed
  it. FIRES: lint (xx) status/pointer checks catch the banner-index
  mismatch half; the flip itself is a checklist line.
- **SR-7 (literature honesty).** Any new PDF on any root = registry
  row with honest read-status; UNREAD never carries a summary; WANTED
  carries an owner. FIRES: lint (xxi).
- **SR-8 (commit-in-window).** If UD-1 = YES: of-record .md/.json in
  validation/ are committed in the window that writes them (the
  single-copy pattern ends). FIRES: closing `git status` check line in
  the R3 checklist (a porcelain-clean gate on the declared set is a
  one-line script; include it in the closure protocol, exit-code
  gated).
- **SR-9 (orchestration weight, measured).** Every orchestration
  reports shape + rounds + approx token weight in the session log
  (contract T2-bis(c); memory orchestration-weight-sota). HONESTLY
  DECLARED CHECKLIST-ONLY: no lint can measure tokens post-hoc; the
  rule lands as a mandatory line in the R3 closure checklist + a
  field in the session-log template. [Checklist, not lint — flagged
  per my own bar; the alternative (a lint grepping session logs for a
  WEIGHT: line) is buildable but polices formatting, not truth;
  judge's call whether the grep version earns its keep.]
- **SR-10 (carrier-touch discipline, the P3 addition).** Any move/
  rename/edit of a validation/*.py carrier = same-window anchor
  verification: claims lint (xv) + findings lint (xix) + numeric
  ratchet (vii) green BEFORE the window closes; file MOVES
  additionally require the priced-constraint procedure (contract
  T2-bis(d)) and are banned inside ordering/service sessions. FIRES:
  the three existing lints already fire on breakage — the rule makes
  the firing a NAMED closure gate instead of a surprise.

(Count: 10 standing rules; 8 fully or partially lint-backed, 2
honestly checklist-only.)

---

## 6. OPEN USER DECISIONS (recommendation + trade-offs) (P3-29)

- **UD-1 — COMMIT the of-record untracked corpus? REC: YES**
  (advisories + session logs + raws + gate-memo .json; the .log files
  see UD-2). FOR: single-copy untracked = zero git history, no
  integrity check, one `rm -rf`/disk fault from R4 violation; the
  durability question is THE named risk of the ADR pattern (prompt
  §2(b)); commit cost ~0 (text, a few MB); S-CERT (R33) expects to
  consume these files — a certification audit over uncommitted
  evidence is structurally weaker; P-1/JPP provenance (P2 lens) wants
  history. AGAINST: history noise (mitigable: one snapshot commit +
  per-window commits after); the ADR-pattern "single copy" was a
  deliberate lightweight choice (but it predates 82 files and 20
  registry rows of load-bearing content — the pattern outgrew its
  price); freeze-discipline interactions (tracked files freeze while
  consumers run — real but already the norm for docs/). Residual
  trade-off honestly stated: committing makes in-place red-team
  corrections visible as diffs — that is a FEATURE for provenance,
  a (mild) cost in commit-message discipline.
- **UD-2 — commit the 24 .log run evidences? REC: YES-cheap**
  (bundle into the same snapshot; they are small text, and 3 of them
  (m6diag/m6fix/m6locus) are borderline at-risk mechanism evidence
  per seg5 §F note). Acceptable alternative: leave DERIVED-untracked
  with index rows; then the findings-registry evidence pointer for
  cross-lowering-gradient-floor must be verified to not depend on
  them (seg5 flag).
- **UD-3 — disposal of verified garbage** (`er.name`,
  `t --count HEAD:q`, `mailmap.txt`, `current_commit_messages.txt`
  post-diff, parent hash lists post-reflog-check). REC: after the
  STEP-8 verifications prove DERIVED/regenerable, DELETE with
  explicit user OK recorded in the session log (R4 permits disposal
  of proven-regenerable debris only as a USER decision; default
  absent OK = leave in place with index/garbage tag). Trade-off:
  archive-with-banner keeps them but institutionalizes shell debris.
- **UD-4 — physical `validation/archive/` vs banner-in-place.**
  REC: banner-in-place (P3-2); create the directory only on explicit
  preference, restricted set, post-move grep verification.
- **UD-5 — ADR_panel_2026-07-16 ratification status.** The file says
  NOT-RATIFIED with an OPEN QUESTION FOR USER; downstream cites its
  content as adopted (seg3 file 1). REC: user adjudicates in one
  minute: (a) "ratified-in-practice" -> status CONSUMED-with-residue,
  the open question either answered or registered as a conditional
  row with owner; or (b) still pending -> PENDING-CONTRACT tag +
  BLOCCATO row. Cannot be decided by agents (it is the user's own
  pending question).
- **UD-6 — README one-paragraph pointer to the research program**
  (seg2 finding 5). REC: YES (one paragraph, user-ratified text) —
  cold-reader navigation (S-CERT MC6) currently dead-ends at the
  lecture layer.
- **UD-7 — CLAUDE.md delta** (the SR-1..SR-10 education half + the
  navigation-spine pointer). By definition user-ratified (T3).
- **UD-8 — parent-directory at-risk items** (outside repo):
  brick2_profiles_record.png (S18 record figure, misplaced single
  copy) — REC: copy INTO validation/ with index row (needs user OK to
  touch parent scope); SDToolbox.zip, Presentazione_CVA.pptx +
  template, VALIDATION.md §3 corrections list, CONTINUATION_PROMPT
  §4-§5 notes — REC: register as literature_registry / index rows
  with `PARENT-SCOPE` tag + a named backup duty owned by the user
  (the repo cannot durably protect files it does not contain).
- (NOT consumed here, their window unchanged, per contract TERMS:
  BLOCCATO-8 filelock; O5 numpy 2.5.2; M6 adoption.)

(Count: 8 open user decisions.)

---

## 7. RIGHT-SIZING — WHAT P3 DELIBERATELY DOES NOT DO (P3-30)

Not done, with the price that justifies it:
1. **No move/rename of ANY validation/*.py** — 0.2(1-4): 67+ machine
   anchors, 10+ hardcoded test paths, per-file ratchet baseline,
   line-range dedup keys. Buys nothing the index does not.
2. **No edits to carrier bodies at all this session** (even comment
   banners) — line-range anchors in findings_registry shift (0.2(3));
   carrier hygiene belongs to the F2 window with the perimeter
   sense-review (registry row structure:monolithic-driver-module
   already owns it).
3. **No docs/ restructure, no new architecture doc** — SCAFFOLD is
   amended (P3-4); two taxonomies = new entropy.
4. **No YAML front-matter retrofit** on the 82 validation .md / 41
   docs .md — the index row IS the metadata; per-file headers would be
   a second copy that drifts.
5. **No per-file typing of GENO vendor docs / pptx lineage** — bulk
   class rows (P3-12); itemizing 78 third-party manuals is inventory
   theater.
6. **No new suite groups beyond the priced set** — (xx) index (+
   supersession family), (xxi) literature, (xxii) glossary-ratchet;
   choice-ledger and flag checks FOLD into existing modules (P3-15,
   P3-16). Hard cap ~3 new test modules; every one rejector-seeded
   and < 1 s, or it does not ship.
7. **No permanent loss-hunter in the suite** (P3-17) — session-scoped
   gate; a standing adversarial agent over a static corpus is a lint
   nobody re-runs.
8. **No new dependencies** for any lint (stdlib only) — the
   BLOCCATO-8/filelock lesson: dependency adoption is a user decision
   with a rejector, and none is needed for text checks.
9. **No re-litigation** of S14-S25bis verdicts, no touching of the
   PENDING-CONTRACT S-CERT prompt, no consumption of BLOCCATO
   decisions.
10. **No reaching outside the repo to "fix" the parent dir or GENO**
    — registered duties with owner (UD-8), read-only stance preserved.

FUORI-SCOPE registrations (register with owner, NEVER execute here —
contract 4-bis; all three already have registry rows, verified in
docs/findings_registry.yaml this read):
- Driver split: `structure:monolithic-driver-module` (owner F2 window
  + perimeter sense-review; trigger recorded). NO ACTION here beyond
  the flag registry (T2-bis(b)) which lands regardless.
- Scheduled CI / multi-platform: `infra:scheduled-ci-multiplatform`
  (owner: user infra window; trigger recorded). NO ACTION.
- P-1 distillation for third parties: NOT yet a registry row — P3
  proposes adding one row `pipeline:P1-distillation` (owner: P-1
  publication stream D6 §3; trigger: post-G5/M1 submission window) so
  the fuori-scope item has the same machine home as the other two.
- Any algorithmic touch: excluded by contract; nothing in this plan
  executes one (the only .py written are new test modules).

---

## 8. SUMMARY FOR THE REFUTER (attack surface, honestly listed)

The load-bearing choices a refuter should hit: (a) banner-in-place vs
the prompt's literal `archive/` (P3-2 — a declared divergence);
(b) the glossary ratchet SCOPE (typed artifacts + status blocks only —
is that too narrow to stop re-minting in advisories?); (c) folding
choice-ledger/flag lints into existing modules vs separate groups
(runner clarity vs sprawl); (d) UD-1 YES recommendation (the ADR
single-copy pattern was a deliberate user-era choice — does P3
overweight durability vs the user's original intent?); (e) the STEP-3
budget split point (is deferring audit-seeding tranches a
never-postpone violation? P3 answer: no — structurally gated with
named owner, the registry's own declared pattern); (f) SR-9 honesty
(checklist-only rule inside an "education = lints that fire" mandate).

END OF POSITION P3. 30 numbered proposals (P3-1..P3-30), 10 standing
rules (SR-1..SR-10), 8 open user decisions (UD-1..UD-8).
