# ADVISORY — S-ORDINE CONVERGED PLAN OF RECORD (Phase 4, fused judge)
# Date: 2026-08-13. Session: S-ORDINE (census R32; contract =
# validation/ADVISORY_Sordine_prompt_2026-08-12.md, read integral).
# Inputs (all read FULL-TEXT by path, never slice): the contract; the three
# Phase-2 positions (position_P1.md, position_P2.md, position_P3.md); the
# Phase-3 refutation (refutation.md); the seven Phase-1 inventories
# (inventory_seg1_docs.md .. inventory_seg7_literature.md, all in
# validation/sordine_raws_2026-08-13/); docs/findings_registry.yaml
# (20 entries — the dedup authority; NO row re-minted below, existing rows
# cited by id).
# Verdicts S14-S25bis are of record and are NOT re-litigated here.
# JUDGE MEASUREMENT DISCIPLINE (R5 applied to meta-claims, per refutation
# INV-6): every tracking/count claim below was re-measured on the live tree
# by this judge on 2026-08-13 (commands: git ls-files, git status
# --porcelain, ls, find, git log). No count is inherited from a prior
# document without a fresh measurement.

---

## §0 HEADER — COUNTS RECONCILED (per-segment, with the measured corrections of record)

### 0.1 The Phase-1 universe as diagnosed (the brief's 436 + 37 + 137)

| Segment | Scope | Files accounted | Reconciliation |
|---|---|---|---|
| seg1 | docs/ core (41 md + 2 yaml) | 43 | discrepancy 0 (in-file) |
| seg2 | src/tests/data/sdtoolbox/examples/figs/root/.claude | 181 | discrepancy 0 (in-file) |
| seg3 | advisories A (ADR + prompts + S24/S25/S25bis class) | 17 | 17/17 read-integral |
| seg4 | advisories B (audit, gap-map, litmap, panels, dispatches) | 17 | 17/17 (1 declared-partial: AUDIT 277 KB) |
| seg5 | session logs 27 + other md 21 + raws 17 + py 33 + json 25 + log 24 + pyc 18 | 165 | discrepancy 0 (in-file) |
| seg7 root A | repo literature/ | 13 | in seg7's 137 |
| **repo subtotal** | 43+181+17+17+165+13 | **436** | == the brief's "436 excl .git+GENO" — RECONCILED |
| seg6 | memory (outside repo) | 37 | 37/37 read-integral |
| seg7 | literature, three roots 13+47+77 | 137 | discrepancy 0 (in-file) |

### 0.2 MEASURED CORRECTIONS OF RECORD (judge-verified 2026-08-13, refutation GT-1/GT-2/GT-3 all CONFIRMED on the tree)

1. **GT-1 CONFIRMED — the "all untracked" premise was false.** Measured:
   validation/*.md on disk = **88** (not 82); tracked = **47**; untracked =
   **41**. 26 of 27 session logs are TRACKED (only the S24 log +
   this session's live log are untracked); both
   ADVISORY_Scert_prompt (b2de54c) and ADVISORY_Sordine_prompt are TRACKED.
   The genuinely single-copy mass = the ~32 untracked advisory-class files
   (audit, gap-map, panels, EQ-v2 pair, gauntlet, choking, litmap, speed
   audit, topology census, the five 2026-08-13 advisories, S24 log) + 24
   untracked validation .log + raws. [S-ORDINE-REPAIR R-2, declared of
   record: ALL 25 validation gate .json are TRACKED (measured
   `git ls-files "validation/*.json"` = 25/25) — GT-1's and P2
   Appendix-A row-10's "gate .json untracked single-copy" premise is
   FALSE; "gate json" is struck from every single-copy risk-mass wording
   in this plan (here, Q13, UD-1); UD-2 stands for the 24 untracked
   .log only.] Every position's stated
   verification count (82/27/34) is superseded: **all add-lists and
   verification counts derive from `git status --porcelain` + fresh `ls`
   AT EXECUTION TIME** (REF-1 adopted as a plan invariant).
2. **GT-2 CONFIRMED — the Phase-1 universe is stale.** Measured: total
   repo files excl .git+GENO = **518** today (list said 436). Delta
   composition: `literature_review/` — an entire FOURTH literature root
   (**54 files**: 25 paper PDFs + INDEX.md + reports/ with 00_APPARATUS_BRIEF
   + 25 integral per-paper reading reports + assets), in NO segment list —
   plus the five 2026-08-13 parallel-session advisories
   (litmap_extension, litreview_confrontation ["VERDETTO DI RECORD, REV 3
   — CONVERGENZA"], moc_zucrow_fidelity, sota_definition, LEDGER_dubbi_moc),
   this session's own log, and the S-ORDINE raws dir (21 files today,
   still growing). The delta is reconciled BY NAME at STEP S0; an
   unexplained residual = gate failure (both directions).
3. **GT-3 CONFIRMED — P1's "UNRESOLVED S25bis repair" is resolved.**
   Commits 8046434 (repairs R1-R9, [X-DEFTW] UNBLOCKED, R8 machine channel
   in group (xix)), 7fb0f0c (convergence CLOSED, registry 20 entries),
   a021fdd (post-repair gates) are on the tree; registry row
   `persistence:derive-artifact-intra-commit-staleness` = DISCHARGED with
   full evidence; `derive_code_identity` live in
   tests/test_findings_registry.py. P1's UD-6 is DROPPED from the
   open-decision list (carrying it would re-litigate a closed verdict).
4. Literature universe of record = **FOUR roots**: repo literature/ (13) +
   parent (47) + GENO (77, read-only) + literature_review/ (54). The
   "137, three roots, discrepancy 0" of seg7 is superseded; seg7 remains
   the seed for roots A/B/C, the litreview corpus is the seed for root D.

---

## §1 TARGET STRUCTURE OF RECORD (Q1 — tree; convergent core of P1-2/P2-2/P3-1, refuter-repaired)

Principles (all three positions convergent, refuter could not kill):
**extend SCAFFOLD, never fork it** (F-SEG1-3); **index-not-move**;
**supersession is a STATUS, not a LOCATION**; **zero carrier/gate-file
moves, zero renames, zero carrier-body edits this session** (P3 §0.2
measured coupling: 67 registry path anchors, 10+ hardcoded test paths,
line-range dedup keys, per-file ratchet baseline); registries INDEX
prose, never replace it (SCAFFOLD conflict rule).

```
rde-lecture-code/
  CLAUDE.md                        # + T3 delta (user-ratified, UD-7)
  README.md                        # + 1-paragraph program pointer (UD-6)
  .gitignore                       # + GENO/ ignore line (STEP S1, precondition)
  docs/                            # UNCHANGED file set, + 5 new files
    rde_nozzle_SCAFFOLD.md         # + dated amendment §6: layers L7-L9
                                   #   L7 validation record layer (evidence+
                                   #   adjudication, indexed, never normative)
                                   #   L8 literature layer (FOUR roots)
                                   #   L9 governance layer (CLAUDE.md, memory,
                                   #   glossary, flags, standing-rule lints)
    rde_nozzle_PROGRESS.md         # SLIMMED (S8): ORA/NEXT/BLOCCATO + ONE
                                   #   consolidated census table R1-R33
    rde_nozzle_PROGRESS_ARCHIVE.md # NEW: history verbatim, dated banners
    roadmap_geno_rde.md            # + dated supersession banner -> D6 (F-SEG1-1)
    claims_registry.yaml           # untouched
    findings_registry.yaml         # grows by R31 seeding (S7)
    choice_ledger.yaml             # NEW (S5): 45 rows from gap-map annex
    literature_registry.yaml       # NEW (S6): FOUR roots
    glossary.yaml                  # NEW (S10): namespace-qualified   [CF-3 pinned]
    flag_registry.yaml             # NEW (S5): one row per A1_* flag  [CF-3 pinned]
    ... M0, D1-D8, attack docs, paper drafts: UNTOUCHED ...
  validation/                      # stays FLAT; the INDEX is the taxonomy
    ADVISORY_INDEX.md              # NEW (S3): one row per .md + block rows
                                   #   for raws dirs; THE L7 navigation
    INDEX.md                       # KEPT separate (CF-7: existing living doc,
                                   #   session-log index; cross-referenced)
    ADVISORY_*/AUDIT_*/PANEL_*/DISPATCH_*/LEDGER_*  # STAY AT CURRENT PATHS;
                                   #   status = index row + in-file banner
    PROGRESS_*.md (27+)            # STAY (26 already tracked)
    *.py (33 carriers/probes)      # NEVER MOVED, NEVER EDITED this session
    *.json gate artifacts          # NEVER MOVED (gate consumers at coded paths)
    *.log (24)                     # stay; disposition after the registry
                                   #   evidence-field check (named follow-up)
    sordine_raws_2026-08-13/       # RAW block row
    sota_gapmap_raws_2026-08-12/   # RAW block row
    [archive/]                     # ONLY if UD-8 ratifies it; default =
                                   #   banner-in-place (CF-1: P3-2 wins, REF-5)
                                   #   [S-ORDINE-REPAIR R-6: DECLARED
                                   #   DIVERGENCE from contract T2(iii)'s
                                   #   letter "archive/ con banner" — the
                                   #   archive dir is made CONDITIONAL on
                                   #   UD-8 with banner-in-place default,
                                   #   per CF-1/REF-5 adjudication]
  literature_review/               # RECOGNIZED as literature root D:
                                   #   INDEX.md + reports/ = the where-read
                                   #   anchor corpus of the new registry
  memory/ (harness-side)           # swept only (S9): banners, link fixes,
                                   #   stale line, 2 inline entries typed
```

**validation/ hygiene under the priced constraint (contract 4-bis(d))**:
adjudicated AGAINST physical moves. The flat directory is fully
de-entropized by ADVISORY_INDEX + status taxonomy; moving anchor-bearing
files is the one operation that can actually lose something (P1 §7, P2-13,
P3-2 convergent; REF-5). If the user ratifies UD-8 (a physical archive/),
it admits ONLY files with (a) zero machine anchors computed by the
anchor-resolution lint AND (b) a repo-wide basename grep whose scope
INCLUDES memory/ and parent-dir prose (REF-5 repair) — candidate set
today: the 6 consumed session prompts, ADVISORY_plan_v2_draft,
DISPATCH_Sspeed_to_S25. Everything else: banner-in-place.

**Plan-anchor traceability = the default navigation** (P1-4/P2-3/P3-3
convergent, REF-20): the chain of record is
`D6 phase / census row (NEED) -> registry or index row (TYPED OBJECT) ->
of-record document (ADJUDICATION) -> carrier/gate (SOTA PROOF)`.
Every ADVISORY_INDEX row carries a mandatory plan-anchor cell; the
consolidated census rows gain an `artifacts:` pointer; the navigation
spine is written once in the ADVISORY_INDEX header and pointed to from
the PROGRESS opening block (R2-reachable, per P3 §0.1). The S-CERT MC6
navigation test is the named consumer.

---

## §2 STATUS TAXONOMY OF RECORD (Q2 — merged enum per REF-18; one enum, no coexisting variants)

Core statuses (per-document; index row + in-file banner where applicable):
- **OF-RECORD** — current authority for its content class; sub-tag
  `(living)` for files that legitimately mutate (PROGRESS, indices,
  registries, numeric_allowlist).
- **SUPERSEDED-BY:<path-or-id>** — authority transferred; dated banner at
  head naming the successor; full text preserved (R4).
- **CONSUMED** — order/prompt/dispatch fully executed; pointer to consumer
  (log/commit/doc) required. Variant **CONSUMED-with-residue:<pointer>**
  when named rows remain live (engine_speed_audit N1-N8/DEAD/Q rows;
  claims_to_code C-4/C-5/C-6) — consumption is per-row, tracked in the
  index note or a per-row consumption map (P2-7; priced warning REF-21:
  after audit seeding this is the largest hidden workload — if deferred,
  it is a NAMED tranche with counts, never generic).
- **RAW** — agent working output whose adjudicated verdicts live in a
  judged advisory; never normative, never deleted; indexed as block rows.
- **DERIVED** — regenerable by a named owner (.log, .pyc, extracts,
  report copies, figures); regeneration owner named in the index.
- **PENDING-CONTRACT** — live prompt for a future session
  (ADVISORY_Scert_prompt: may not be archived or altered).
- **UNRESOLVED** — the honest state when a ratification/execution status
  is recorded nowhere (today exactly one occupant: ADR_panel_2026-07-16
  ratification, REF-34; the S25bis repair-list occupant is DISCHARGED
  per GT-3). UNRESOLVED rows are session duties, never archive candidates.

Qualifiers (orthogonal tags, combinable): **LECTURE-ERA** (qualifier, not
a status — REF-18(ii); the 17 pre-program V&V docs are also OF-RECORD
frozen, plan-anchor = repo-sota-standard/G1 substrate);
**AT-RISK:<ledger-id>** (item still lacking its destination);
**UNTRACKED-SINGLE-COPY** (applied only if UD-1 is refused, P3-18
degraded mode — the risk stays priced, owned, and visible).

Supersession discipline (P1-8 + P2-6 + P3-9/P3-10 merged, REF-26/REF-32):
1. Every `SUPERSED*` marker carries a DATE and a resolvable POINTER on
   the same line/block; format of record =
   `SUPERSEDED (YYYY-MM-DD[, session]) -> <pointer>`; original text
   preserved.
2. The lint is RATCHETED (R28 pattern): legacy free-form markers enter a
   frozen baseline; growth of unparsed markers is forbidden; the baseline
   only shrinks (REF-26 — an unratcheted lint is red at birth or forces
   edits to frozen text).
3. Reciprocity: if doc A declares it supersedes B, B carries the banner
   (the roadmap_geno_rde gap, F-SEG1-1) — checked for the named
   file-level pairs.
4. Status changes are append-only dated events; banners are never edited
   beyond appending. Banner and index row are redundant BY DESIGN
   (human-first / machine-first); the lint checks agreement; TIE-BREAK OF
   RECORD (REF-32): the INDEX is authoritative for STATUS, the file for
   CONTENT.
5. Archive move (if any, UD-8) = banner + index row update + anchor lint
   green in the same window; archive is append-only (SR-10).

---

## §3 TYPED + LINTED LAYER — LINT GROUP MAP PINNED (CF-2 resolved; numbering continues from (xix); hard cap 3 new test modules per P3-30.6, REF-30)

| Group | Module | Checks | Seeded rejectors |
|---|---|---|---|
| **(xx)** | tests/test_advisory_index.py | index coverage: bijection files<->rows over validation-tree .md (raws dirs as BLOCK rows — CF-5: P1 form wins, REF-7); status in the §2 enum; SUPERSEDED/CONSUMED rows carry date+resolving pointer; plan-anchor non-empty OR explicit `ORPHAN-FLAGGED` (visible, COUNTED, ratcheted — new unflagged orphans fail, existing flagged ones report; CF/REF-20: P3-11(e) form wins); + supersession-marker family (ratcheted, P3-14 fold); + banner/index agreement | phantom row; missing file; unflagged orphan; unparsed marker beyond baseline |
| **(xxi)** | FOLDED into tests/test_findings_registry.py as an anchor-resolution check-family [S-ORDINE-REPAIR R-1: the §3 header's hard cap of 3 new modules (P3-30.6/REF-30) is the pinned form; (xxi) folds rather than raising the cap — it already extends the (xix) module's span-resolution machinery to all registries] | THE durable nothing-lost half (P2-9, strongest single lint per REF-22): every source:/evidence:/code: anchor in findings/choice/literature registries resolves to an existing file; `#fragment` resolution = NORMALIZED SUBSTRING grep in the target (convention written in the docstring — existing registry fragments are prose headings, REF-22 repair); doubles as the pre/post gate of any future move | doctored dead anchor |
| **(xxii)** | tests/test_literature_registry.py | schema (§S6); four-root coverage; enum {READ-INTEGRAL, READ-PARTIAL, UNREAD, WANTED} with `READ-PARTIAL(triaged)` as the pinned mapping for seg7's TRIAGED (CF-10 — one enum, no coexistence); WANTED/UNREAD => owner; **UNREAD row with non-empty content summary = FAIL** (the never-fake-a-summary rule as a machine check); where-read anchors resolve | unregistered PDF; UNREAD-with-summary |
| **(xxiii)** | tests/test_glossary.py | glossary schema (namespace mandatory); pointer resolution; RATCHETED token-resolution check over the scoped corpus (§S10) | unknown token; baseline +1 bump |
| choice-ledger checks | FOLD into tests/test_findings_registry.py as a second check-family (CF-11: P3-15 wins on runner-sprawl grounds; REF-15 caveat honored: schemas stay distinct, the (xix) anti-re-mint code-span rule is NOT applied to codeless choice rows) | enum {DECIDED/MIXED/SINGLE-AUTHOR/NEVER}; NEVER => owner; anchors resolve; 45==45 at seed | ownerless NEVER row |
| flag-registry checks | FOLD into (xx) module [S-ORDINE-REPAIR R-4: destination PINNED to (xx) per the plan's own pin-before-code discipline] | bijection registry rows <-> flags found by a census PINNED TO ACTUAL ENV READS (`os.environ.get("A1_`/`os.getenv(`) — REF-16 repair: bare `grep -o A1_*` hits docstrings/reporting strings and makes both failure directions unfalsifiable; string mentions declared out-of-scope; row content: default, meaning, covering gate, tested pairs, cartesian product DECLARED untested | phantom flag |

All new lints: stdlib-only, ASCII-safe, redirect-only, FAST tier inside
tests/run_all.py, each < ~1 s, every one rejector-seeded (R5/R6 — a lint
without a firing rejector does not ship). What deliberately stays PROSE
(P1-16/P2 §7/P3-30.4, REF-31): advisories, panels, session logs, theory
docs — the typed layer is index + registries + glossary, nothing else.

HONEST-SCOPE DECLARATION on the glossary (REF-11, binding wording): the
glossary lint delivers COLLISION DISAMBIGUATION + NAVIGATION. It does NOT
prevent finding re-minting — that is the (xix) dedup clause's job
(demonstrator: `variational-driver:objective-omits-throat-panel`). No
S-ORDINE artifact may sell the glossary as anti-re-mint machinery.

---

## §4 STEP-BY-STEP EXECUTION PLAN FOR T2 (14 ordered steps S0-S13; each with its nothing-lost verification and its lint; sized for THIS session with the declared split at S7)

Ordering rationale: universe first (nothing downstream is trustworthy
before it), safety rails second, durability third, index before banners
before extractions, the slim last among edits (its census rows point at
destinations created earlier), the firing gate at the end, education at
close. Serial, small-step, one-session-at-a-time (P3 §0.2(7)).

**S0 — UNIVERSE REPAIR (hard precondition #1, REF-2/GT-2; nothing else
starts before it).** Regenerate the authoritative file list fresh
(`find` excl. .git/GENO + `git ls-files`); run a SUPPLEMENTARY READER
PASS (Phase-1 schema, PLAN-ANCHOR included) over: the five 2026-08-13
advisories + LEDGER_dubbi_moc + the live session log +
`literature_review/` (INDEX.md + reports/ + PDFs + assets — contents
enumerated by FRESH `ls` at S0 execution per SR-12, never a frozen
sub-count [S-ORDINE-REPAIR R-7: the plan-time "26 reports" was already
stale on disk — reports/ holds 27 files today incl.
VERIFICATION_FABLE_2026-08-13.md, absent from every Phase-1 input]) +
the current sordine_raws contents. Assign every new file to a segment.
- Nothing-lost verification: fresh total (518 measured at plan time; the
  number moves as raws grow — the CLOSING count is the one of record)
  reconciled against the segment sums at discrepancy 0; the delta vs the
  stale 436 named FILE-BY-FILE; unexplained residual = FAIL.
- Lint: none yet (this step CREATES the input every later lint uses).

**S1 — GENO ignore + explicit-pathspec rule (P2-16; REF-23: required
precondition of any commit; cheapest risk-kill in the plan).** Add
`GENO/` to .gitignore; record the "adds by explicit pathspec only, never
`git add -A`" rule (lands in the CLAUDE.md delta, UD-7).
- Verification: `git status` shows no GENO/ paths; .gitignore diff = the
  one insertion.

**S2 — Durability snapshot (gated on UD-1; if refused, SKIP — no
tarball, REF-14: the degraded mode is the UNTRACKED-SINGLE-COPY index
tag, risk priced and owned).** Explicit-pathspec `git add` of the
untracked of-record set DERIVED FROM `git status --porcelain` AT
EXECUTION TIME (today's measure: 41 .md + 24 .log [S-ORDINE-REPAIR R-2:
.json struck — all 25 are already tracked] + raws dirs —
re-measure at the step). Pure-add snapshot commit tagged
`[F-SERVICE/S-ORDINE][PIANO/R32]`, BEFORE any banner edit (git history
becomes the undo path of every later step).
- Verification: porcelain-clean for the declared set; count added ==
  count measured in the same step (never a position's number, REF-1).

**S3 — ADVISORY_INDEX.md + lint (xx).** Rows generated from the
seg3/seg4/seg5 inventories PLUS the S0 supplementary pass; raws dirs as
block rows; the ADR panel row = UNRESOLVED; the Scert prompt row =
PENDING-CONTRACT; LECTURE-ERA qualifier on the 17 pre-program docs
(seg5 §B); DISPATCH_S24_generality row = CONSUMED-with-residue (two
sharper-only items until the literature registry absorbs them, seg4 §15).
- Nothing-lost verification: bijection lint green against the FRESH
  file count from S0 (never 82/88 hard-coded); no file touched.
- Lint: (xx) green with all rejectors observed firing.

**S4 — Banner sweep (insertions only; no move).** Dated banners:
roadmap_geno_rde.md -> D6 (F-SEG1-1); the 6 consumed session prompts
(S21, S21-addendum, S25, S25bis, Scollapse, Sgauntlet);
DISPATCH_Sspeed_to_S25 (fully redundant per seg4); ADVISORY_plan_v2_draft
-> plan_v3_panel; interface_audit.md CONSUMED note. 10 files, enumerated.
- Nothing-lost verification: `git diff` shows insertions only (zero
  content lines removed); banner count == the enumerated list.
- Lint: (xx) supersession family parses every new marker; legacy
  baseline frozen (REF-26).

**S5 — Registry extractions: choice_ledger.yaml + flag_registry.yaml.**
Choice ledger: 45 rows from the gap-map annex C1-C45 (5 DECIDED +
3 MIXED + 12 SINGLE-AUTHOR + 25 NEVER, the annex's own tallies,
P3-22-verified); the annex stays in place as prose authority with a
one-line pointer banner. Flags: env-read-pinned census (REF-16) over
validation/*.py + tests/; known population A1_COLEXEC, A1_VMAP_HESS,
A1_FUSED_CERT, A1_PLAN_ARGS, A1_MEMO_PROBE, A1_CERT_ARGMAX, A1_REJ_SAVE
+ census-found others.
- Nothing-lost verification: 45 == 45 with per-state tallies; every
  NEVER row has owner; flag census bijection both directions.
- Lint: choice family (in xix module) + flag family green, rejectors fire.

**S6 — literature_registry.yaml over FOUR roots (REF-3 repair).**
Seed = seg7 (roots A/B/C verbatim: identities, read-status, where-read
anchors, dedup pairs, bulk class rows for 52 vendor docs + 26 pptx
lineage + GENO figures with the `plt/mira_*` glob EXPANDED) + root D
from literature_review/INDEX.md + the reports/ corpus fresh-enumerated
at execution (27 files at repair time; each report = a where-read
anchor of record) + the two 2026-08-13 lit advisories.
RE-RUN the dedup across all four roots (measured duplicates:
harroun_2021, kaemming_paxson, paxson_miki, wintenberger_shepherd,
wolanski between PARENT and literature_review/ — one row, multiple
paths). RE-DERIVE the WANTED list against disk (Ancourt 2023,
Kraiko-Tillyaeva 2004/2015/2016, Teasley 2023/2025 are ON DISK in root
D; Wolanski now has an integral report — seg7's "never research-read"
duty is falsified; survivors of the WANTED list keep owners: AIAA
2019-0197, Peter-Desideri 2022, L-P Aerospace 10:267, Tillyaeva 1975,
Naumova-Shmyglevskii 1967, Breitkopf-Ulbrich). Parent at-risk notes
(VALIDATION.md §3 seven corrections incl. the SK Table-1 704-s
paper-typo finding; CONTINUATION_PROMPT §5 per-paper notes) land in the
registry note fields (copy-in only, REF-27).
- Nothing-lost verification: FOUR-root reconciliation at discrepancy 0
  against fresh `ls` per root (137 declared stale-superseded); the six
  seg7 at-risk rows each have a destination row or an explicit UD-5
  pointer; dedup pairs recorded, none dropped.
- Lint: (xxii) green incl. the UNREAD-with-summary rejector; (xxi)
  anchors resolve.

**S7 — R31 seeding tranches into findings_registry.yaml (the absorbed
first duty; THE DECLARED SPLIT POINT).** Tranches, each closed by lint
before the next: (a) audit 94 rows (~90-91 unseeded, seg4-measured;
per-row: seed OR map to an existing row OR record
consumed-at-S21/S25-with-evidence); (b) gap-map 36 GAP + 16 AC + 11 Q
[S-ORDINE-REPAIR R-3, correction DECLARED once of record: the contract
T2(i) says "36/16/10" but the source document measures 36 GAP + 16 AC +
**11** Q (Q1-Q11, grep-verified) — the contract's 10 is stale; 11 is
the count of record];
(c) refuter/red-team S25/S25-bis residues; (d) per-row consumption maps
for the high-density partially-consumed advisories (claims_to_code
C-1..C-6; engine_speed_audit N1-N8/DEAD/Q1-Q6/survey rows; redteam
ISS-1..ISS-6 consumption verification; mean_swirl F2a deltas) per P2-7.
Dedup against the 20 existing rows is the registry's own machine rule
(id + code-span); a merged row is COUNTED and NAMED, never dropped.
- Nothing-lost verification PER TRANCHE (P3-21 three-way form): source
  row count == new rows + explicitly-deduped rows + declared-not-seeded
  rows with reason — arithmetic reconciled to 0 and written in the
  session log.
- Lint: (xix) green after every tranche; (xxi) on the new anchors.
- BUDGET SPLIT (contract T2 rule + never-postpone: structurally-gated
  split with named owner is legitimate): if the session budget breaks,
  it breaks HERE. The queue is the NAMED tranche list with counts —
  e.g. "audit rows 41-94 (54 rows) + tranche (d) consumption maps
  (4 advisories)" — as the FIRST duty of the next window; never
  "finish seeding later".

**S8 — PROGRESS slim + PROGRESS_ARCHIVE.** Fold the census (S24
consolidated snapshot L492-560 + S25 delta + S25-bis delta + ORA-carried
rows) into ONE table R1-R33, one row per item: id | state | owner +
trigger | artifacts pointer. Move VERBATIM under dated provenance
banners ("moved from PROGRESS.md L<a>-<b>, 2026-08-13, S-ORDINE"): the
delta blocks, the five stale NEXT blocks (L1919-2149), the per-session
mini-ORA blocks older than S24, the S1-S13 LOG tail. Live file keeps:
ORA, current NEXT chain, BLOCCATO 1-8, the consolidated table,
one-liner session pointers to validation/PROGRESS_* logs.
- Nothing-lost verification (REF-9: the adopted mechanical form is P1
  M-7(b), the only one that proves the claim): (i) LINE-MULTISET check —
  every line removed from PROGRESS.md appears verbatim in the ARCHIVE
  (old_lines ⊆ live ∪ archive, counted exceptions = new table/banner
  lines, reconciled to 0; char-sum inequalities and random spot-checks
  are REJECTED as verifications); (ii) fold audit — each R-row's state
  cites the newest delta block mentioning it, ambiguity = loud finding;
  (iii) BLOCCATO 1-8 + NEXT chain + F2 counter grep-verified in the
  live file; (iv) at-risk weighting corrected per REF-8: tracked logs
  exist from 2026-07-16 — only the S1-S2 entries and per-entry narrative
  deltas are genuinely single-home; they land in the ARCHIVE verbatim.
- Lint: census single-table grep (exactly one CENSIMENTO table in
  PROGRESS.md — scoped to PROGRESS.md only, the ARCHIVE legitimately
  carries many, REF-24).

**S9 — Memory sweep (T2(v)).** (a) Dated supersession banner on the
ROUTING half of the 9 unmarked HISTORICAL-SESSION memories (s14, s15,
s18, s19, s20, s21, s22, s24, s25 — verdict halves untouched; the s23
in-file block is the template); (b) fix the 3 broken links ([[s24-deftw]]
-> s24-f1b-def-twin; the [[s24-*]] wildcard; the scope-pins pseudo-link);
(c) fix the stale MEMORY.md numpy line (actively misleading vs O5);
(d) type the two inline-only entries (POST-S20, POST-S21-SERA) into
backing files with index lines; (e) research-cycle-averaged-rao.md:
banner the S1-S13 historical half, keep the overview head.
- Nothing-lost verification (REF-10 arithmetic repair): counts RECOMPUTED
  at execution — after (d), backing files = 38 and MEMORY.md index lines
  == 38; link check re-run = 0 broken (was 3); banners present = 9.
- Lint: none reaches memory/ (outside the repo) — HONESTLY DECLARED
  checklist-verified in the session log (P3-6/P3-26 form).

**S10 — glossary.yaml + lint (xxiii).** Merge the five Phase-1 token
tables (214 + 178 + 78 + 231 + 70, dedup at build); namespace-qualified
(measured collisions of record: O5, M1, T2, F4, C1, L4, U1-U4, A1, P*,
B1, T1/T2, F1-F7 each 2-4 meanings); PREFIX-FAMILY RULE (P1-12): tokens
resolving to a registry row get ONE family entry pointing at the
registry as resolver — full rows only for collisions and unregistered
tokens (no 700-row glossary). Enforcement scope at introduction
(P3-13, REF-11): typed artifacts + docs/*.md status blocks, RATCHETED
baseline for the unresolved remainder; widening to the historical
validation/ corpus = a registered later ratchet, not a birth obligation.
- Nothing-lost verification: merged-table count declared (sources ->
  deduped N); every collision from the inventories has a disambiguating
  entry.
- Lint: (xxiii) green; both rejectors fire.

**S11 — Garbage adjudications (verification only; NO deletion inside
S-ORDINE — REF-12/CF-9: the contract TERMS are categorical, deletion
happens only on explicit user order recorded outside this session's
action set; default = leave-in-place/archive-with-banner).**
(a) `current_commit_messages.txt` diffed vs `git log --format=%B`
(identical -> DERIVED; different -> OF-RECORD pre-rewrite provenance,
commit it); (b) `er.name` + `t --count HEAD:q` byte-verified derived
debris (md5-identical, seg2/refuter-confirmed); (c) `mailmap.txt`
CONSUMED; (d) parent old_*_hashes.txt checked vs reflog (possible only
pre-rewrite provenance map). Results feed UD-3.
- Nothing-lost verification: each diff/reflog outcome recorded in the
  session log with the command output; zero files deleted.

**S12 — THE 4-TER NOTHING-LOST GATE (runs ONLY after S0 — REF-29 hard
precondition: a seeded canary proves the detector fires, it proves
nothing about universe completeness).**
(i) AT-RISK LEDGER CONSOLIDATION: merge the seven inventories' at-risk
feeds + P2 Appendix A REGENERATED from `git ls-files` truth (REF-28: its
rows 7/9 were false — tracked files are not at-risk; the six NEW
unlisted files and root D, absent from every position's ledger, are IN);
weights corrected per REF-8; seg1's self-contradictory recount (39 vs
41) re-counted at consolidation (INV-4). The ledger is a typed session
artifact in sordine_raws (item | source | destination) — session
tooling, RAW class, not a standing registry (P1-15/P3-17: no "ledger of
ledgers").
(ii) DESTINATION MAP: every ledger item resolves to a registry row id /
archived-or-bannered file + index row / glossary entry / ARCHIVE block.
Gate = a one-shot script, exit-code gated: item without destination =
SESSION FAIL, not a footnote.
(iii) SEEDED REJECTORS, both detectors: remove one destination-map item
in-memory -> the gate MUST fail; plant one canary item absent from the
corpus -> the loss-hunter MUST flag it. A detector that does not fire on
its seed is broken; the session does not close on it.
(iv) ADVERSARIAL LOSS-HUNTER (one dedicated agent, default "something IS
lost until proven otherwise"): samples the ledger, diffs pre/post
inventories, traces 10 random HISTORICAL findings to their current home.
One untraceable item = FAIL. Session-scoped, NOT a permanent suite
member (P3-17/REF-29: the durable residue is lint (xxi)).
(v) FINAL RECONCILIATION at discrepancy 0 against the S0-regenerated
count (which exceeds 436; 518 at plan time) + FOUR literature roots; the
delta vs the prompt's 428 and the brief's 436 reconciled BY NAME, both
directions. This reconciliation is the R3 CLOSURE PRECONDITION
(contract 4-ter(iv)).

**S13 — T3 EDUCATION (close).** (a) CLAUDE.md delta PROPOSED for user
ratification (UD-7): one short block under R3 naming the closure-
checklist rules (SR-1/2/6/7/9 below) + the GENO-ignore/explicit-pathspec
line + a pointer to SCAFFOLD §6 for the layer/registry map — under ~15
lines, governance not manual; (b) ONE line added to the R3 closure
checklist: "every new advisory = index row + registry rows in the same
window; index/registry/glossary lints green; census table edited
one-row-per-item"; (c) census R32 row updated (consumed or
split-declared) AND a STANDING census row minted for the SR-1..SR-12
regime (the T3 deliverable "riga di censimento standing" delivered
explicitly [S-ORDINE-REPAIR R-5], carrying the standing-rule set +
its enforcement map as a permanent census item); (d) SCAFFOLD §6
amendment written (dated, bounded: layer list + registry map — REF-19);
(e) every orchestration this session reports its weight line in the
session log (SR-9's first enforced instance).
- Verification: R3 closure runs the full suite gated on exit code; the
  S12 gate has passed; PROGRESS/log/memoria updated per R3.

---

## §5 CONVERGED STANDING RULES (the education half; every rule names its enforcement — a lint that fires or a gated checklist line, never a recommendation; merged from P1 SR-1..10 / P2-SR-1..10 / P3 SR-1..10 per REF-24, REF-6, REF-7, REF-11)

- **SR-1 (index-or-it-doesn't-exist).** Every new validation-tree .md =
  ADVISORY_INDEX row in the SAME window. FIRES: lint (xx) bijection at
  every suite run; raws covered as block rows so mid-orchestration
  artifact drops never turn the lint red (REF-7).
- **SR-2 (findings/choices land as rows).** Adjudicated findings/choices
  get registry rows in the same window; prose-only findings are re-mint
  fuel. FIRES: (xix) dedup/anti-re-mint + R3 checklist line.
- **SR-3 (supersession is explicit).** Dated banner/marker + resolvable
  pointer, reciprocal for file-level pairs, append-only. FIRES: (xx)
  supersession family, ratcheted.
- **SR-4 (glossary resolution).** New codename tokens entering typed
  artifacts or doc status blocks resolve (glossary or registry) in the
  same window; new namespace = new section. FIRES: (xxiii) ratchet
  (baseline growth forbidden). Declared payoff: disambiguation +
  navigation — NOT anti-re-mint (REF-11).
- **SR-5 (flag registry).** A new A1_* env flag cannot ship without its
  row (default, covering gate, tested pairs, untested product declared).
  FIRES: env-read-pinned census bijection (REF-16).
- **SR-6 (no single-copy of-record — placement per REF-6/CF-6: R3
  CLOSURE, never a mid-session suite lint).** Conditional on UD-1: new
  of-record validation files are committed by session close, or
  explicitly listed in the session log as pending-commit with reason;
  closing `git status` check on the declared set, exit-code gated. If
  UD-1 refused: rule DECLARED-INACTIVE-BY-USER-DECISION in the index
  header — visible, not silent.
- **SR-7 (census one-row discipline).** The census is edited IN PLACE in
  the consolidated table; delta blocks are banned; history goes to
  PROGRESS_ARCHIVE at close. FIRES: single-table grep scoped to
  PROGRESS.md + R3 checklist line.
- **SR-8 (literature honesty).** New paper on any root = registry row at
  arrival with honest read-status; UNREAD never carries a summary
  (machine-checked); WANTED carries an owner. FIRES: (xxii).
- **SR-9 (orchestration weight measured).** Every orchestration reports
  shape + rounds + approximate token weight in the session log entry of
  the step that ran it. HONESTLY CHECKLIST-ONLY (P3 SR-9 form wins,
  REF-24: a grep-lint would police formatting, not truth): R3 closure
  line; the S-CERT MC-audit and any loss-hunter sample it.
- **SR-10 (archive is append-only).** PROGRESS_ARCHIVE and any archive/
  receive content only with banner + provenance line; nothing inside an
  archive is ever edited beyond its banner. FIRES: R3 checklist + git
  diff review at close.
- **SR-11 (carrier-touch discipline — P3 SR-10 adopted verbatim, REF-24:
  the only rule addressing the measured line-anchor fragility).** Any
  move/rename/edit of a validation/*.py carrier = same-window anchor
  verification: lints (xv) + (xix) + numeric ratchet (vii) green before
  the window closes; file MOVES additionally require the priced
  procedure of contract 4-bis(d) and are BANNED inside
  ordering/service sessions.
- **SR-12 (measure-before-stating — the refutation's INV-6 lesson,
  elevated).** Any artifact stating a tracking-status or count claim
  cites the command output measured in its own window, never a prior
  document. R5 applied to meta-claims. FIRES: R3 checklist line;
  S-CERT MC7 samples it.

---

## §6 OPEN USER DECISIONS (numbered, each with the converged recommendation + trade-offs; P1 UD-6 DROPPED per REF-4/GT-3 — the S25bis repair status is DISCHARGED on the tree and recorded as such, not re-opened)

**UD-1 — COMMIT the of-record untracked corpus? (Q3 — THE decision;
converged recommendation of all three positions, refuter-re-scoped.)
RECOMMENDATION: YES** — commit, at S2, the execution-time-measured
untracked set: today 41 validation .md (the ~32 advisory-class
single-copy files carrying the audit's ~90 unseeded findings, the
gap-map's ~108 adjudicated objects, EQ-v2, the topology census with 11
user pins, the gauntlet ledger, the five 2026-08-13 advisories, the S24
log) + 24 untracked .log [S-ORDINE-REPAIR R-2: .json struck — all 25
tracked] + the raws dirs.
- FOR: single-copy untracked is the highest-concentration risk in the
  corrected diagnosis (GT-1 shrank the mass but the advisory core IS
  untracked); git = free replication, tamper evidence, bisectable
  provenance, and the undo path of every migration step; the S-CERT
  audit (R33) and JPP/P-1 review interrogate exactly this evidence
  chain; the four original reasons for the ADR-untracked pattern
  (not-yet-ratified encoding, freeze friction, parallel sessions, noise)
  are each superseded by machinery that now exists (status taxonomy,
  commit-at-boundary, owning-session commits, RAW class) — P2 §0,
  refuter-verified.
- AGAINST (priced): commit noise (bounded: one snapshot + per-close
  commits); in-place repair visibility as diffs (a provenance FEATURE);
  repo weight trivial (~2-3 MB text); freeze-discipline surface grows
  (already the norm for docs/).
- Fallbacks if NO: track advisories only (weaker); NO tarball fallback
  (REF-14) — the honest degraded mode is the UNTRACKED-SINGLE-COPY index
  tag with the risk owned by this decision.

**UD-2 — Run-log (.log) tracking policy.** RECOMMENDATION: commit all
24 in the same snapshot (small text; simplest rule). Acceptable
alternative: cited-subset only (the three M6 probe logs m6diag/m6fix/
m6locus carry mechanism-isolation evidence for registry row
`engine:cross-lowering-gradient-floor` — seg5 §F; verify the row's
evidence pointers before ANY later log disposition; REF-35).

**UD-3 — Disposal of verified debris** (`er.name`, `t --count HEAD:q`,
`mailmap.txt`, `current_commit_messages.txt` post-diff, parent
old_*_hashes.txt post-reflog, `hr.txt` md5-twin,
.claude/scheduled_tasks.lock). RECOMMENDATION: after the S11
verifications, register the disposition decision; DEFAULT (no decision)
= leave-in-place/archive-with-banner; any deletion is a recorded user
order executed OUTSIDE S-ORDINE's action set (REF-12 — the contract's
"mai cancellare" is categorical for this session).

**UD-4 — ADR_panel_2026-07-16 ratification status** (in-file "NOT YET
RATIFIED" + ">>> OPEN QUESTION FOR USER" while downstream cites its
content as adopted; refuter-verified, REF-34). RECOMMENDATION: user
adjudicates in one minute — (a) ratified-in-practice -> CONSUMED-with-
residue, the open question answered or registered as a conditional row
with owner; (b) still pending -> the open question becomes a BLOCCATO
row. Until then the index row says UNRESOLVED. Cannot be decided by
agents: it is the user's own pending question.

**UD-5 — Parent-root items, SPLIT per REF-27/CF-8:** COPY-IN actions
(read-only stance preserved, no user gate beyond this plan's
ratification): brick2_profiles_record.png copied into validation/ with
index row (S18 record figure, single copy outside the repo);
VALIDATION.md §3 + CONTINUATION_PROMPT §5 notes into
literature_registry note fields (S6). MOVE/DISPOSE actions (touch
parent state — USER-GATED): SDToolbox.zip (recommend register-in-place:
4.5 MB, stable); hash lists (with UD-3); pptx lineage stays in parent
with one registry block row. MEMORY MIRROR sub-decision (REF-13): if a
tracked copy of the verbatim-order memory corpus is wanted, it is a
DATED SNAPSHOT with a non-authority banner ("memory wins; durability
copy as of <date>"), refreshed only by explicit decision — recommend
YES with exactly that semantic, else refuse.

**UD-6 — README one-paragraph pointer to the research program** (the
front door hides the program; seg2 finding 5). RECOMMENDATION: YES, one
paragraph, user-ratified wording (REF-35).

**UD-7 — CLAUDE.md delta ratification** (S13(a): the SR-block + GENO
pathspec rule + SCAFFOLD §6 pointer). By definition user-ratified (T3).

**UD-8 — Physical validation/archive/ vs banner-in-place.**
RECOMMENDATION: banner-in-place (CF-1: P3-2 wins on the refuter's
weighing, REF-5 — a banner gives ~100% of the R4 value at ~0% breakage
risk; memory-side and parent-side prose citations are outside every
proposed grep scope unless extended). Create the directory only on
explicit preference, restricted to the zero-inbound-anchor set with the
EXTENDED grep scope (memory/ + parent .md included) and post-move lint
(xx)+(xxi) green.

(NOT consumed here, windows unchanged per contract TERMS: BLOCCATO-8
filelock [registry row `conditional:filelock-lru-cap`]; O5 numpy 2.5.2;
M6 adoption [registry row `engine:vmap-hessian-adjoint-divergence`,
adoption-ready at F2/session boundary].)

---

## §7 FUORI-SCOPE REGISTRATIONS (registered with owner + trigger, never executed here; dedup against the registry — existing rows CITED, not re-minted)

1. **Driver split** — ALREADY REGISTERED: registry row
   `structure:monolithic-driver-module` (owner F2 window WITH perimeter
   sense-review; trigger recorded in-row). No action here beyond the
   flag registry (S5), which lands regardless per the row's own text.
2. **Scheduled CI / multi-platform** — ALREADY REGISTERED: registry row
   `infra:scheduled-ci-multiplatform` (owner: user infra window;
   triggers in-row). No action.
3. **P-1 distillation / provenance package** — NOT yet a registry row:
   propose ONE new row `pipeline:P1-provenance-package` (owner: P-1
   submission window, D6 §3; trigger: post-G5/M1 submission window;
   seed content = P2 Appendix B's six reviewer-requirement mappings).
   Minted at S7 alongside the seeding tranches.
4. **Run-log archival pass** — post-evidence-check window (after the
   registry evidence-field verification of UD-2); named follow-up,
   never a silent drop.
5. **Glossary-lint scope ratchet** to the historical validation/ corpus
   — any later hygiene window (S10 declared limit).
6. **Any algorithmic touch** — excluded by contract; the only .py
   written this session are new test modules.

---

## §8 PER-QUESTION ADJUDICATION TABLE (Q1-Q15: verdict, positions cited, refutations answered)

| Q | Verdict (all 15 CONVERGED) | Positions adopted | Refutations answered |
|---|---|---|---|
| Q1 target structure + validation/ hygiene | CONVERGED: SCAFFOLD amendment L7-L9; index-not-move; flat dir stands; zero carrier/json moves or edits; banner-first archive; plan-anchor navigation spine | P1-1/2/4, P2-1/2/3/13, P3-1/3/4/7 (convergent core, REF-19/17/20 survive) | REF-2 (universe precondition S0); REF-5 (extended grep scope if UD-8); REF-17 naming pinned §1/CF-3 |
| Q2 taxonomy + supersession | CONVERGED: merged 7-status enum + 3 qualifiers; UNRESOLVED kept (P1-only, needed); LECTURE-ERA = qualifier; CONSUMED-with-residue kept; ratcheted marker lint; index=STATUS / file=CONTENT tie-break | P1-7/8, P2-5/6, P3-8/9/10 merged per REF-18 | REF-26 (ratchet adopted over P1-14's unratcheted form); REF-32 (tie-break declared) |
| Q3 tracked-vs-untracked (USER DECISION) | CONVERGED RECOMMENDATION: YES commit, re-scoped to execution-time porcelain truth; GENO-ignore precondition; no tarball fallback | P1 UD-1, P2-D1 (§0 four-reasons analysis), P3 UD-1 — unanimous | REF-1 (all counts re-derived at execution); REF-14 (P3 degraded mode wins); REF-23 (P2-16 mandatory); REF-6 (tracked-check at closure, not suite) |
| Q4 ADVISORY_INDEX + archive/ + micro-lint | CONVERGED: index design survives; built AFTER S0; raws = block rows; ORPHAN = ratcheted visible state; INDEX.md kept separate; archive/ gated on UD-8, banner default | P1-3/11 (block rows win CF-5), P2-8 (rest), P3-11 (ORPHAN-ratchet wins) | REF-2 (count clause repaired: fresh ls, never 82); REF-7 (per-file raws indexing refuted); REF-20 (P2-8 ORPHAN-fails wording refuted) |
| Q5 PROGRESS slim + census + ARCHIVE | CONVERGED: one-row-per-item R1-R33 fold, newest-block-wins audit; verbatim archive with provenance lines; line-multiset nothing-lost check | P1-5 (its M-7(b) is THE check), P2 STEP-4, P3-24 mechanics/block map | REF-9 (char-sum and spot-check verifications refuted; multiset adopted); REF-8 (S1-S13 at-risk weight corrected: only S1-S2 single-home) |
| Q6 findings-registry seeding scope | CONVERGED: sources = audit 94 + gap-map 36/16/11 + refuter/red-team residues + P2-7 consumption maps; three-way per-tranche count; dedup = the registry's own id+code-span rule vs the 20 rows; declared split at S7 with named tranche queue | P1 M-6, P2 STEP-2/P2-7, P3-21 (three-way count form adopted) | REF-21 (consumption-map workload priced, named-tranche rule); REF-4 (verify-first instruction confirmed already executed — no re-open); dedup: 3-4 audit rows already seeded (seg4 measure), cited not re-minted |
| Q7 choice ledger | CONVERGED: docs/choice_ledger.yaml, 45 rows, strict-subset schema, NEVER=>owner, annex stays prose authority; lint FOLDED into (xix) module as distinct family | P1-9 schema, P2-12 nothing-lost check, P3-15/22 (fold + tallies 5/3/12/25) | REF-15 (numbering conflict pinned §3; fold caveat: no code-span rule on codeless rows); CF-11 resolved fold |
| Q8 literature registry | CONVERGED-WITH-REPAIR: FOUR roots; seed = seg7 + literature_review corpus + 2 new lit advisories; 4-root re-dedup; WANTED list re-derived vs disk; enum pinned with READ-PARTIAL(triaged); UNREAD-empty-summary machine rule; bulk class rows; glob expanded | P1-10, P2-11 (honesty rules), P3-12 (bulk right-sizing) — designs survive | REF-3 (REFUTED-AS-SOURCED: three-root seeding falsified by root D — repaired at S6); CF-10 (enum pinned); REF-22 (fragment convention) |
| Q9 memory sweep | CONVERGED: 9 routing-half banners, 3 link fixes, stale index line, 2 inline entries typed, rao-file banner treatment; honest no-lint-reaches-memory limit; mirror only as dated snapshot (UD-5) | P1-6, P2 STEP-5, P3-6/26 (convergent; REF-33 spot-verified) | REF-10 (count recomputed: 38 after typing); REF-13 (living mirror refused; snapshot semantic only) |
| Q10 glossary + resolution lint | CONVERGED: docs/glossary.yaml, namespace-qualified, prefix-family rule, ratcheted scope = typed artifacts + status blocks; honest payoff declaration (not anti-re-mint) | P1-12 (family rule), P2-10 (namespace evidence), P3-13 (ratchet scope wins) | REF-11 (overclaim struck; ratchet adopted as the only widenable form); CF-3 (yaml pinned) |
| Q11 A1_* flag registry | CONVERGED: docs/flag_registry.yaml, one row per flag, census pinned to env reads, bijection both directions, folded lint, seeded phantom-flag rejector | P1-13, P2-10 (bidirectional), P3-16 (fold + cheapness) | REF-16 (bare-grep false-positive class repaired: os.environ.get/getenv pattern, string mentions declared out) |
| Q12 orchestration-weight rule | CONVERGED: SR-9, honestly checklist-only; mandatory weight line per orchestration in the session log; R3 line; sampled by S-CERT/loss-hunter | P3 SR-9 (honest form wins), P1 SR-9 wording compatible, P2-SR-8 same | REF-24 (placement adjudicated; token-lint version rejected as formatting police) |
| Q13 NOTHING-LOST gate | CONVERGED: ledger consolidation from regenerated git truth; destination map; both seeded rejectors; adversarial loss-hunter session-scoped; discrepancy-0 reconciliation vs the S0 count + 4 roots as R3 precondition; durable residue = lint (xxi) | P1-15, P2 STEP-7/P2-9, P3-17 (session-scoped, no permanent hunter) | REF-29 (S0 hard precondition — canary tests the detector, not the universe); REF-28 (Appendix-A regeneration; rows 7/9 false); REF-8 (weights); INV-4 (recount) |
| Q14 education / CLAUDE.md delta | CONVERGED: 12 standing rules SR-1..SR-12 (incl. SR-11 carrier-touch verbatim and SR-12 measure-before-stating, the refutation's own lesson); CLAUDE.md delta <15 lines proposed for ratification; ONE R3 checklist line | P1 §5, P2 §5, P3 §5 merged per REF-24 | REF-6 (P2-SR-3 re-placed at closure); REF-7 (raws block rows in SR-1); REF-11 (SR-4 honest payoff) |
| Q15 fuori-scope registrations | CONVERGED: driver split + CI cited to their EXISTING registry rows (no re-mint); P-1 provenance package = ONE proposed new row `pipeline:P1-provenance-package`; log-archival + glossary-ratchet named follow-ups | P1 §7, P2 §7 (Appendix B as seed), P3-30/§7 (rows verified in-registry) | REF-30 (right-sizing lists survive); dedup: `structure:monolithic-driver-module` + `infra:scheduled-ci-multiplatform` verified present in the 20-row registry this read |

Refutation coverage note: all 5 HARD PRECONDITIONS of the refutation §5
are carried — (1) S0 universe repair before index/registries/gate;
(2) execution-time count derivation everywhere (REF-1, SR-12);
(3) UD-6-old dropped, discharged state recorded (§6 preamble);
(4) GENO ignore + pathspec at S1 before any commit; (5) S12 gated on S0.
All 14 CF conflicts pinned: CF-1 §1/UD-8, CF-2 §3, CF-3 §1 tree,
CF-4 §2, CF-5 §3(xx), CF-6 SR-6, CF-7 §1 tree, CF-8 UD-5, CF-9 S11/UD-3,
CF-10 §3(xxii), CF-11 §3 fold, CF-12 §0.2(3), CF-13 S2, CF-14 UD-5.

---

## §9 PROPOSED NEW SYSTEM-LEVEL FINDING (dedup-checked against the 20 registry rows — no existing row covers it; to be minted at S7)

- id: `process:inventory-universe-staleness`
  status: CONFIRMED; severity: medium
  finding: the S-ORDINE Phase-1 inventory inherited the prompt's
  2026-08-12 universe (436 files / three literature roots / "all
  untracked") without re-measuring; the fresh tree had 518 files, a
  fourth literature root (54 files, several of-record single-copy), 6
  unlisted validation .md, and 47 tracked .md — the zero-discrepancy
  reconciliation was being run against an incomplete universe, exactly
  the failure class the 4-ter gate exists to catch (refutation GT-1/GT-2,
  judge-verified).
  mechanism: stale-baseline-inheritance
  owner: SR-12 (measure-before-stating) is the standing discipline; the
  S-CERT MC7 provenance audit samples it.
  trigger: any future artifact stating tree/tracking counts.

END OF CONVERGED PLAN — S-ORDINE Phase-4 fused judge, 2026-08-13.
Phase-5 (Form-3 red-team on this judge BEFORE absorption, per contract
T1) is the next phase of the workflow: counts reconciled here are its
first target; every "adopted/absorbed" above is pointed at its source.

---

## §10 [S-ORDINE-REPAIR] — PHASE-5 RED-TEAM REPAIRS APPLIED IN-DOCUMENT
## (Form-3 verdict: ABSORB_WITH_REPAIRS, 7 repairs — 3 MED, 4 LOW;
## raw report: validation/sordine_raws_2026-08-13/redteam_judge.md.
## Applied 2026-08-13 by the session lead; facts re-verified on the
## live tree before application, commands in the session log.)

- R-1 (MED, §3): header/body contradiction pinned — the 3-new-module
  hard cap (P3-30.6/REF-30) is the form of record; (xxi)
  anchor-resolution FOLDS into tests/test_findings_registry.py.
- R-2 (MED, §0.2/S2/UD-1): declared of record that ALL 25 validation
  gate .json are TRACKED (re-verified: `git ls-files` 25/25); "gate
  json" struck from every single-copy risk wording; UD-2 stands for
  the 24 untracked .log only.
- R-3 (MED, S7): the gap-map Q-count correction DECLARED once of
  record: contract says 36/16/10, source measures 36/16/11
  (re-verified: Q11 present) — 11 is the count of record.
- R-4 (LOW, §3): flag-registry check-family fold destination PINNED
  to module (xx).
- R-5 (LOW, S13): the T3 "standing census row" deliverable made
  explicit at S13(c) — a permanent census row for the SR-1..SR-12
  regime is minted at close.
- R-6 (LOW, §1 tree): one-line DECLARED DIVERGENCE from contract
  T2(iii)'s letter added — archive/ conditional on UD-8,
  banner-in-place default (CF-1/REF-5).
- R-7 (LOW, S0/S6): frozen sub-count "26 reports" replaced by
  fresh-ls enumeration per SR-12 (re-verified: reports/ = 27 files
  today incl. VERIFICATION_FABLE_2026-08-13.md, absent from every
  Phase-1 input).
