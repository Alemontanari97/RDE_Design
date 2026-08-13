# POSITION P1 — knowledge-management / docs-as-code SOTA
# S-ORDINE Phase 2, 2026-08-13. Author lens: ADR (Nygard) discipline,
# Diataxis role separation, docs-as-code pipelines, typed registries,
# supersession discipline, coverage lint.
# Inputs: session contract (ADVISORY_Sordine_prompt_2026-08-12.md, read
# integrally) + ALL SEVEN inventories (seg1-seg7, read integrally) +
# spot-checks: docs/findings_registry.yaml (schema + seed rows),
# run_all lint-group map (seg2 §C.1). Verdicts S14-S25bis not re-litigated.
# All proposals numbered P1-n for refuter/judge citation.

## 0. DIAGNOSIS ACCEPTED, ONE REFRAME

The seven inventories confirm the prompt's diagnosis with one crucial
positive finding I build everything on (seg1 F-SEG1-3): **this corpus
already contains its own proven de-entropy instrument** — the SCAFFOLD
L0-L6 layering + typed registry + lint-with-seeded-rejector pattern
(claims registry S9, findings registry R31, 19 executable lint groups).
The entropy is NOT in docs/ (0 orphans, status blocks everywhere); it is
concentrated in exactly four places:

1. validation/ = 82 .md flat, ALL advisory-class + logs UNTRACKED
   single-copy, no index of status/supersession (seg3/seg4/seg5);
2. PROGRESS.md bidirectional accretion: census readable only by folding
   >=3 delta blocks; 5 stale NEXT blocks; fossil LOG tail (seg1 F-SEG1-2);
3. memory: 9 unmarked-stale session memories, 3 broken links, 1 stale
   index line, 2 untyped inline entries (seg6 F1-F3);
4. findings/choices/literature adjudications living as prose in
   single-copy advisories (~90 unseeded audit rows, 45 choice-ledger
   rows, 137-file literature corpus with no machine registry).

REFRAME (P1 thesis): the target is not a new architecture. It is ONE
amendment to SCAFFOLD (extend the layers over validation/, literature
and governance), THREE new typed registries + ONE index + ONE glossary
on the existing lint pattern, and a supersession/banner sweep. Anything
beyond that is scope creep = new entropy.

---

## 1. TARGET STRUCTURE

### P1-1 — Extend SCAFFOLD, never fork it
The converged plan MUST be written as a dated amendment to
`docs/rde_nozzle_SCAFFOLD.md` (new §6: layers L7-L9 below), not as a new
architecture doc. Rationale: SCAFFOLD is the in-corpus prior art for
exactly this operation (typed registry + layered reading order + lint +
migration-with-acceptance, executed S9). Two competing architectures
would themselves be an entropy source. New layers:
- **L7 — validation record layer**: session logs, advisories, carriers,
  gate artifacts, raws — indexed by ADVISORY_INDEX, never normative
  (theory lives in L0-L6; L7 is evidence + adjudication provenance).
- **L8 — literature layer**: three roots (repo literature/, parent,
  GENO read-only) indexed by docs/literature_registry.yaml.
- **L9 — governance layer**: CLAUDE.md + memory + glossary + flag
  registry + the standing-rule lints.

### P1-2 — Target tree (explicit; moves are minimal and priced)

```
rde-lecture-code/
  CLAUDE.md                      # + T3 delta (user-ratified)
  README.md                      # + 1-paragraph program pointer (UD-5)
  docs/                          # UNCHANGED structure (L0-L6 stand)
    rde_nozzle_MASTER.md         # M0 — untouched
    rde_nozzle_SCAFFOLD.md       # + §6 amendment (L7-L9)  [P1-1]
    rde_nozzle_PROGRESS.md       # SLIMMED (see P1-5)
    rde_nozzle_PROGRESS_ARCHIVE.md   # NEW: banner'd history  [P1-5]
    rde_nozzle_development_plan.md   # untouched (two-spine layering
                                     # is governed, seg1; no rewrite)
    roadmap_geno_rde.md          # + dated supersession banner (F-SEG1-1)
    ... D1-D8, attack docs, papers: UNTOUCHED ...
    claims_registry.yaml         # existing, untouched
    findings_registry.yaml       # existing; grows by R31 seeding
    choice_ledger.yaml           # NEW  [P1-9]
    literature_registry.yaml     # NEW  [P1-10]
    flag_registry.yaml           # NEW, small  [P1-13]
    glossary.md                  # NEW, namespace-qualified  [P1-12]
  validation/                    # stays FLAT for live content
    ADVISORY_INDEX.md            # NEW: one row per .md + status [P1-3]
    INDEX.md                     # kept (session-log index); row in
                                 # ADVISORY_INDEX points at it
    PROGRESS_*.md (27)           # STAY IN PLACE (anchor targets;
                                 # tracked per UD-1)
    ADVISORY_*/AUDIT_*/PANEL_*/DISPATCH_* (live of-record)  # STAY
    *.py (33 carriers/probes)    # NEVER MOVED (priced constraint)
    *.json gate artifacts (25)   # NEVER MOVED (gate consumers)
    *.log (24)                   # stay; archive candidates ONLY after
                                 # registry evidence-field check (seg5 §F note)
    archive/                     # NEW: CONSUMED/SUPERSEDED docs, each
                                 # with banner + index row  [P1-8]
    sordine_raws_2026-08-13/     # this session's raws (RAW class)
    sota_gapmap_raws_2026-08-12/ # stays (RAW class, indexed)
  memory/ (user-side)            # swept: banners + link fixes  [P1-6]
```

Deliberate NON-moves (right-sizing, §7): carriers, gate json, live
advisories, session logs. The flat directory is NOT the problem once an
index types every file; moving anchor-bearing files is the one operation
that can actually lose something here.

### P1-3 — ADVISORY_INDEX.md design (the L7 single source of truth)
One row per `validation/*.md` (and one per raws subdirectory as a
block-row). Columns — this exact schema, because each column answers a
gate the session must pass:

| column | answers |
|---|---|
| path | identity |
| class | advisory / session-prompt / session-log / panel / dispatch / raw / lecture-era / doc-plan |
| status | taxonomy of §2 (P1-7) |
| plan-anchor | PRIMARY LENS: phase/census-row/registry-row/gate/directive that NEEDS this doc; `ORPHAN` is a legal loud value |
| supersedes / superseded-by / consumed-into | pointer(s), dated |
| at-risk | YES/no — carries unique-at-risk content per the Phase-1 inventories (feeds the 4-ter ledger) |

Coverage micro-lint (P1-11): file without a row = FAIL; row without a
file = FAIL; status SUPERSEDED/CONSUMED without pointer = FAIL;
plan-anchor empty = FAIL (ORPHAN must be written explicitly, per the
prompt's "never silently absorbed").

### P1-4 — Plan-anchor traceability as THE default navigation
The user's primary lens becomes the reading order of the repo. The chain
of record is:

  D6 phase / census row (the NEED)
    -> registry row or index row (the TYPED CLAIM/FINDING/CHOICE)
      -> of-record document (the ADJUDICATION, prose)
        -> carrier/gate (the SOTA PROOF, executable)

Operationally: (a) every ADVISORY_INDEX row carries plan-anchor
(machine-checked non-empty); (b) every registry row already carries
source+code anchors (findings) / doc+carrier (claims) — the new
registries copy that strict-subset schema; (c) PROGRESS census rows
gain a one-line "artifacts:" field pointing at index/registry ids, so a
cold reader navigates need->artifact->proof without folding history.
This is navigation-by-need, which is precisely Diataxis discipline
applied to a research corpus: the plan is the how-to spine, registries
are reference, advisories are explanation, logs are the record.

### P1-5 — PROGRESS slim (T2(iv)), concrete fold
Structure of the slimmed file (target <= ~600 lines from 2498):
1. Header + opening protocol (unchanged).
2. ORA (rewritten each close, unchanged mechanism).
3. NEXT chain of record (one block, current only).
4. BLOCCATO (live rows only, currently 8).
5. **CENSIMENTO CONSOLIDATO — ONE ROW PER ITEM R1-R33** (fold of the
   S24 snapshot + S25 delta + S25-bis delta + ORA-block new rows), each
   row: id | state (ORA/SCHED/GATED/LOCK/CHIUSA) | owner+trigger |
   artifacts pointer. This is the fold of L295-560 the seg1 inventory
   mapped 1:1.
6. Session-summary one-liners (S1..S25bis) each pointing at its
   validation/PROGRESS_* log — NOT the frozen mini-ORA blocks.
Everything folded out (mini-ORA blocks L560-1918, five stale NEXT
blocks, fossil LOG tail S1-S13) moves VERBATIM to
`docs/rde_nozzle_PROGRESS_ARCHIVE.md` under a dated banner. Nothing is
rewritten in the archive — cut-and-paste with a per-block provenance
line ("moved from PROGRESS.md L<a>-L<b>, 2026-08-13, S-ORDINE").
NOTE the seg1 at-risk items that must SURVIVE IN THE LIVE FILE: census
row states, BLOCCATO, NEXT chain, F2 session counter. The S1-S13 early
LOG entries are at-risk-unique (no validation/ log exists for them):
they go to the ARCHIVE (not deleted), and the archive gets an index row.

### P1-6 — Memory target structure (T2(v))
No re-architecture; a sweep with four fixes (all from seg6 F1-F4):
(a) dated supersession banner on the ROUTING HALF of the 9 unmarked
historical session memories (verdict half untouched — the s23 in-file
"SUPERSEDING UPDATE" block is the template of record);
(b) fix 3 broken [[links]] (s24-deftw -> s24-f1b-def-twin; the s24-*
wildcard; the pseudo-link in scope-pins);
(c) fix the STALE MEMORY.md numpy line (actively misleading vs the O5
decision);
(d) type the two inline-only entries (POST-S20, POST-S21 SERA) into
real memory files with the standard header, index lines updated.
Also: research-cycle-averaged-rao.md gets the PROGRESS treatment
(overview head kept; S1-S13 blocks banner'd as historical, pointing at
the committed logs) — same pattern, same session, cheap.

---

## 2. STATUS TAXONOMY

### P1-7 — Five core statuses + three qualifiers (no more)
Core (exactly the prompt's set, with hard definitions):
- **OF-RECORD** — current authority for its content class. Sub-flag
  `living` for files rewritten in place (PROGRESS, INDEX, registries).
- **SUPERSEDED-BY-<path>** — authority transferred; file KEPT with
  dated banner at top naming the successor (R4). A doc may also carry
  section-level dated in-place markers (the working corpus convention,
  seg1 F-SEG1-4) without being file-level superseded.
- **CONSUMED(-into <pointer>)** — an order/prompt/dispatch fully
  executed; substance lives in the named consumer (log/commit/doc).
  Consumed docs are the archive/ population of choice.
- **RAW** — agent working output whose adjudicated verdicts live in a
  judged advisory; never normative; kept, indexed as a block.
- **DERIVED** — regenerable by a named owner (logs, .pyc, report
  copies, figure renders); no unique content by construction.
Qualifiers (needed by real rows found in Phase 1, kept to three):
- **PENDING-CONTRACT** — a live prompt for a future session
  (ADVISORY_Scert_prompt: may not be archived or altered; seg3 file 13).
- **LECTURE-ERA** — pre-program V&V layer (seg5 §B): OF-RECORD frozen,
  anchored to repo-sota-standard not to D6; the index types it so the
  plan-lens navigation does not mix layers.
- **UNRESOLVED** — the honest state when ratification/execution status
  is not recorded anywhere (today: ADR_panel_2026-07-16 ratification;
  S25bis_diff_convergence repair-list R1-R13 execution). UNRESOLVED
  rows are session duties, not archive candidates (feeds UD-6).

### P1-8 — Supersession discipline (the rules that make R4 real)
(a) File-level: dated banner AT TOP, naming successor + what survives
    here uniquely (the two historical notes are the template).
(b) Section-level: dated in-place marker `SUPERSEDED <date> <session>
    -> <pointer>`, original text preserved (already the corpus
    convention; now linted, P1-14).
(c) Archive move = banner + ADVISORY_INDEX row update + anchor-lint
    pass in the same window. An archived file keeps its full text;
    archive != delete, ever.
(d) Memory: routing-half banner (P1-6a); verdict half never banner'd.
(e) Nothing is superseded implicitly: if doc A's status block says it
    supersedes B, B must carry the banner (this is exactly the
    roadmap_geno_rde gap, F-SEG1-1) — linted by P1-14.

---

## 3. WHAT GETS TYPED + LINTED (extending groups (i)-(xix))

Precedent: strict-subset schema of claims/findings registries; every
lint ships with seeded rejector(s) that fire every run (the (xix)
pattern, 4 rejectors). New suite groups, in execution-cost order:

### P1-9 — docs/choice_ledger.yaml + group (xx)
Extraction of the 45-row C1-C45 annex from ADVISORY_S24_sota_gapmap
(T2(ii)). Schema (strict subset of findings schema): id, status
(DECIDED/MIXED/SINGLE-AUTHOR/NEVER), decision-of-record, evidence
anchor (doc#anchor must resolve), owner (REQUIRED for NEVER rows),
alternatives-considered. Lint: enum checks; NEVER => owner; anchors
resolve; count vs source annex reconciled at seed time (45 == 45);
1 seeded rejector (ownerless NEVER row).

### P1-10 — docs/literature_registry.yaml + group (xxi)
One row per paper across the THREE roots (T2(vi); direct source =
seg7 inventory, 137 files + WANTED list). Schema: path(s) (multi for
dedup pairs), bib-identity, read-status HONEST enum (READ-INTEGRAL /
READ-PARTIAL / TRIAGED / UNREAD / WANTED), where-analyzed anchors
(advisory/litmap/log — must resolve for any READ-* row), plan-anchor,
notes. Vendor-docs and GENO figure sets enter as BLOCK rows (52
vendor manuals = 1 row with count; the plt/mira_* glob expanded per
seg7 duty 6). WANTED rows (AIAA 2019-0197, Peter-Desideri 2022,
Ancourt 2023, L-P 2023, Tillyaeva 1975, Breitkopf-Ulbrich) carry
owner — no faked summaries, per the contract. Lint: enum; anchor
resolution; every repo-literature/ file has a row (coverage against
`ls literature/`); READ row without where-anchor = FAIL; 1 seeded
rejector (READ-INTEGRAL row with dangling anchor).

### P1-11 — ADVISORY_INDEX coverage micro-lint + group (xxii)
As specified in P1-3: bijection files<->rows over validation/*.md
(+ raws dirs as blocks), pointer presence per status, plan-anchor
non-empty. Seeded rejector: an in-memory row deletion must FAIL the
bijection check (doubles as the 4-ter(iii) detector rejector).

### P1-12 — Glossary + resolution lint + group (xxiii)
docs/glossary.md, **namespace-qualified** — the four token collections
(seg1: 214, seg3: 178, seg6: 231, seg4/seg5/seg7 partials) prove heavy
collisions (O5, M1, T2, F4, C1, L4, U1-U4, A1 each 2-4 meanings; seg4
codifies this as the audit's own label-namespace-collisions finding).
Design: one section per NAMESPACE (census R-*, gates G-*, gaps GAP-*,
carriers X-*, registry T-*/S-*/C-*/D-*/DIR-*, phases F-*/A-*, speed
M-*/H-*, flags A1_*, panels/session-local ids), each entry: token |
meaning | home (registry row / doc anchor). PREFIX-FAMILY RULE
(right-sizing): tokens that already resolve to a registry row (all
X-*, T-*, S-*, C-*, GAP-*, DIR-*) get ONE family entry pointing at
the registry as resolver, not 200 duplicate rows — the glossary
resolves what the registries do not, and disambiguates collisions.
Lint (the T2-bis(a) order): every [X-*]/GAP-*/R-*/C-*/M-* token used
in OF-RECORD docs must resolve to a glossary entry OR a registry row;
session-local ids (RT-n, ISS-n, DR-n, panel C-n...) resolve via their
advisory's index row (family entry declares the scoping rule). Scope
of enforcement at introduction: docs/*.md OF-RECORD + ADVISORY_INDEX
rows (not the whole historical validation/ corpus — ratchet later if
wanted). 1 seeded rejector (unregistered token in a doc fixture).

### P1-13 — docs/flag_registry.yaml + group (xxiv) (T2-bis(b))
One row per arbitration env-flag (known population from Phase 1:
A1_COLEXEC, A1_VMAP_HESS, A1_FUSED_CERT, A1_PLAN_ARGS, A1_MEMO_PROBE,
A1_CERT_ARGMAX, A1_REJ_SAVE + any grep-found others): default,
meaning, covering gate, tested pairs, cartesian-product DECLARED
untested. Lint: registry rows == `grep -o "A1_[A-Z_]*"` census over
validation/*.py + tests/ (bijection, so a new flag cannot ship without
a row); covering-gate field must name an existing gate/test. 1 seeded
rejector (in-memory phantom flag).

### P1-14 — Supersession-marker lint (folds into group (xxii))
Corpus grep over docs/ + validation/ OF-RECORD files: every
`SUPERSED*` marker must carry a date and a pointer token on the same
line/block (the F-SEG1-4 cheap extension); every index row with
status SUPERSEDED/CONSUMED must have the pointer column filled; and
the P1-8(e) reciprocity check for the named file-level pairs.

### P1-15 — The nothing-lost ledger as a machine artifact (4-ter)
This session's at-risk ledger (consolidated from the seven
inventories' UNIQUE-AT-RISK rows + at-risk feeds) is written as a
typed file in sordine_raws (item | source | destination), and gate
4-ter(i) is a script check: every item has a destination that
resolves (registry row id / archived path + index row / glossary
entry). Seeded rejector per 4-ter(iii). This artifact is session
tooling (RAW), not a permanent registry — permanent homes are the
registries/index themselves (right-sizing: no standing "ledger of
ledgers").

### P1-16 — What deliberately stays PROSE (anti-overengineering)
Advisories, panels, session logs, theory docs are NOT converted to
yaml. The typed layer is index + five registries + glossary, nothing
else. Typing prose wholesale would destroy the adjudication record's
readability and add schema debt with no lint payoff. The registries
INDEX prose; they never replace it (the claims-registry "index never
content" conflict rule extends unchanged to all new registries).

---

## 4. MIGRATION PLAN (ordered; each step with nothing-lost verification)

PRICED CONSTRAINT honored throughout: NO validation/*.py move, NO
gate-json move, NO live-advisory move. Safe-move set = consumed
prompts/dispatches + superseded drafts + (later, optional) logs.

**M-0. Durability snapshot FIRST (gated on UD-1).**
If the user ratifies committing the of-record corpus: `git add` of
validation/*.md (+ decision-scoped .json/.log per UD-1) BEFORE any
move or edit, as a pure snapshot commit. Verification: `git status`
shows zero untracked *.md under validation/; count committed ==
count on disk (82). Rationale: every later step then has git history
as its undo path — the single cheapest nothing-lost mechanism that
exists. If UD-1 is refused, M-0 degrades to a dated tar/zip snapshot
in the parent dir (still single-copy-breaking, still cheap).

**M-1. ADVISORY_INDEX.md + coverage lint (P1-3, P1-11).**
Generate rows from the seg3/seg4/seg5 inventories (status calls
already proposed per file). Verification: bijection lint green over
82 .md + raws dirs; row count == `ls validation/*.md | wc -l`;
seeded rejector fires. No file touched.

**M-2. Banner sweep (P1-8).** roadmap_geno_rde.md banner (F-SEG1-1);
UNRESOLVED annotations on ADR_panel + S25bis_diff_convergence index
rows; PENDING-CONTRACT flag on Scert prompt row. Verification: P1-14
lint green; zero content lines removed (diff shows insertions only).

**M-3. archive/ moves — CONSUMED set only.**
Population (from seg3/seg4 status calls): 6 executed session prompts
(S21, S21-addendum, S25, S25bis, Scollapse, Sgauntlet) +
DISPATCH_Sspeed_to_S25 (fully redundant, seg4) +
ADVISORY_plan_v2_draft (superseded). 8 files, none an anchor target
of registry code/source fields (verify before move). Each: banner +
index row update. Verification per move: source count == destination
count (8==8); post-move anchor lint = grep of each moved path across
docs/*.yaml + docs/*.md + validation/*.md — every stale reference
either updated or the move REVERTED (a moved file that something
of-record cites by path is cheaper left in place; the index carries
its status either way). NOTE: DISPATCH_S24_generality_findings is
CONSUMED-as-channel but carries two sharper-only items (seg4 §15) —
stays live until literature_registry absorbs them (M-5), then joins
archive in a later window.

**M-4. Registry extractions (P1-9 choice ledger, P1-13 flags).**
Choice ledger: 45 rows extracted; verification: row count == annex
count (45), every evidence anchor resolves, lint (xx) green with
rejector. Flags: grep census == registry rows; lint (xxiv) green.

**M-5. literature_registry.yaml (P1-10).**
Direct transcription of seg7 (137 accounted + WANTED rows + dedup
pairs + the two cross-segment anchor notes F-SEG1-5). Verification:
row-sum reconciliation 13+47+77 == 137 with glob expansion delta
declared; lint (xxi) green; the 6 at-risk parent items (seg7 ledger)
each have a destination row or an explicit UD-4 decision pointer.

**M-6. R31 seeding tranches (the absorbed first duty).**
Mechanical find->verify extraction into findings_registry.yaml:
audit 94 (per-row: seed OR map to existing row OR record
consumed-at-S21/S25 evidence), gap-map 36/16/10, refuter/red-team
S25/S25-bis residues. Verification per tranche: source-row count ==
(new rows + dedup-mapped rows + consumed-with-evidence rows) —
arithmetic reconciled to 0; lint (xix) green after every tranche;
anti-re-mint rule exercised (the registry's own dedup clause is the
verifier). This step is the largest and may be split across the
session boundary ONLY as a named tranche list with counts (never
generic), per the contract.

**M-7. PROGRESS slim + PROGRESS_ARCHIVE (P1-5).**
Verification: (a) census fold — consolidated table has exactly one
row per R1-R33 and every state matches the LATEST delta block
mention (fold audit: for each row, the newest block wins; ambiguity
= loud finding, not a silent pick); (b) archive completeness — every
line removed from PROGRESS.md appears verbatim in the ARCHIVE block
(mechanical diff: len(old) == len(new_live) + len(archived) modulo
the new table/banner lines, reconciled to 0); (c) at-risk survivors
(P1-5 list) grep-verified present in the live file.

**M-8. Memory sweep (P1-6).**
Verification: 9 banners present; link-checker over [[...]] targets =
0 broken (was 3); MEMORY.md index lines == memory files (36) + 0
inline-only entries (was 2); stale numpy line corrected.

**M-9. Loss-hunter + gate close (4-ter).**
Run the destination-map gate (P1-15) over the consolidated at-risk
ledger; seeded rejector both sides; adversarial loss-hunter samples
+ 10 historical findings traced to current homes; 428-file (fresh:
436) + 3-root reconciliation at discrepancy 0 as R3 precondition.

Ordering rationale: snapshot before touch (M-0); index before moves
(M-1, so every move has a row to update); banners before archive
(M-2/M-3); extractions before the slim (M-4/M-5/M-6 create the
destinations that M-7's census rows point at); detector last (M-9).

---

## 5. STANDING RULES (the education half — every rule IS a lint or a
## gated checklist line, never a recommendation)

- **SR-1 (index-or-it-doesn't-exist).** Every new validation/*.md in a
  session = ADVISORY_INDEX row in the SAME window. Enforced by lint
  (xxii) bijection at every suite run — the R3 closure suite fails on
  an unindexed doc. This is the contract's own T3 line ("ogni advisory
  nuovo = riga indice + righe registry nella stessa finestra").
- **SR-2 (registry-before-close).** Findings/choices adjudicated in a
  session get their registry rows in the same window; the census R3
  sweep line adds: "registry rows written for every new
  finding/choice; lint (xix)/(xx) green". Enforced: (xix)/(xx) +
  anti-re-mint dedup.
- **SR-3 (supersession is explicit).** No document/memory is
  superseded by implication: dated banner/marker + pointer, reciprocal
  where a successor names a predecessor. Enforced by P1-14 lint.
- **SR-4 (glossary resolution).** New codename tokens in OF-RECORD
  docs must resolve (glossary entry or registry row). Enforced by lint
  (xxiii). New NAMESPACE = new glossary section in the same window.
- **SR-5 (flag registry).** A new A1_* env-flag cannot ship without a
  flag_registry row naming default + covering gate. Enforced by lint
  (xxiv) grep-bijection.
- **SR-6 (single-copy is a state, not a fate).** Any new OF-RECORD
  artifact is committed (or explicitly listed in the session log as
  pending-commit with reason) by session close — conditional on UD-1
  ratification. Enforced: R3 checklist line + `git status` gate in the
  closure step (untracked *.md under validation/ = closure FAIL).
- **SR-7 (census one-row discipline).** PROGRESS census is updated by
  EDITING the consolidated row, never by stacking a new delta block;
  session log carries the delta narrative instead. Enforced: R3
  checklist line + (cheap) lint: at most one CENSIMENTO table in
  PROGRESS.md.
- **SR-8 (literature honesty).** New paper on any root = registry row
  with honest read-status at the window it arrives; UNREAD is a legal
  status, a fake summary is not. Enforced by lint (xxi) coverage on
  repo literature/ + WANTED owner requirement.
- **SR-9 (orchestration weight measured — T2-bis(c)).** Every
  orchestration reports shape + rounds + token weight in the session
  log entry of the step that ran it. Enforced: R3 checklist line
  (LOG entry for an orchestration step without a weight line =
  closure violation); precedent = CONVERGED §7 instrument-weight
  report, now mandatory.
- **SR-10 (archive is append-only).** validation/archive/ and
  PROGRESS_ARCHIVE receive content only with banner + provenance
  line; nothing is ever edited inside an archive beyond its banner.
  Enforced: R3 checklist line + git diff review at close.

CLAUDE.md delta (proposed for user ratification, T3): one short block
under R3 naming SR-1/2/6/7/9 as closure-checklist lines, plus a
pointer to SCAFFOLD §6 for the layer/registry map. Keep it under ~15
lines — CLAUDE.md is governance, not a manual.

---

## 6. OPEN USER DECISIONS (with recommendation + trade-offs)

- **UD-1 (FIRST, the durability question): commit the OF-RECORD
  advisories + session logs — YES/NO.**
  RECOMMENDATION: **YES — commit all validation/*.md (82) + the 25
  gate/artifact .json; logs (.log) optional-in; keep .pyc ignored.**
  For: (a) single-copy untracked is the highest-concentration risk in
  the whole diagnosis — among the untracked: the S-CERT contract
  (R33), the topology census with 11 user pins, the gap-map with ~100
  adjudicated objects, the audit with ~90 unseeded findings, all 27
  session logs (the R3 record itself); one disk fault or bad `clean`
  erases the program's adjudication history. (b) The ADR lineage this
  pattern cites actually COMMITS ADRs — "untracked ADR pattern" is a
  local mutation, not the SOTA practice; docs-as-code means the record
  travels with the code and gets history/diff/blame. (c) Every
  migration step (§4) gains git as its undo path. (d) The R1 commit
  tag discipline extends naturally to record docs.
  Against (priced): repo weight (~a few MB of text — negligible);
  commit noise (mitigated: snapshot commit M-0 + normal R3 commits
  after); the psychological "advisories are drafts" framing dies —
  but that framing is already false: they are verdicts of record.
  Middle option if refused: track only advisory-class + logs, leave
  raws untracked with the tar snapshot of M-0.
- **UD-2: disposition of the four root garbage-candidates** (`t
  --count HEAD:q`, `er.name`, `mailmap.txt`,
  `current_commit_messages.txt`) + parent `old_*_hashes.txt` orphans.
  RECOMMENDATION: run the seg2 T2 diff duty (dump vs `git log
  --format=%B`); if clean, the two shell-debris files and the dump are
  DERIVED with zero unique content — user-approved deletion is
  legitimate (R4 protects content, and these have none, byte-verified);
  if the diff is NOT clean, the dump becomes OF-RECORD provenance and
  is committed. mailmap/old-hashes: archive-with-banner (tiny,
  possibly the only pre-rewrite provenance). Default on no-decision:
  archive everything, delete nothing.
- **UD-3: ADR_panel_2026-07-16 ratification status** — the file still
  carries ">>> OPEN QUESTION FOR USER" and downstream docs cite its
  content as adopted (seg3 file 1). RECOMMENDATION: user adjudicates
  ratified-and-executed (mark CONSUMED with pointer) vs still-pending;
  until then the index row says UNRESOLVED. Cheap, closes a 4-week
  ambiguity.
- **UD-4: parent-root misplaced items** — `brick2_profiles_record.png`
  (S18 record figure, single copy OUTSIDE the repo): RECOMMENDATION
  move-copy into validation/ with index row (trivial, closes a real
  at-risk row). The lecture-lineage pptx set: leave in parent, one
  literature_registry/lecture block row records the deliverable +
  template as of-record (no repo import — different project).
- **UD-5: README one-paragraph pointer** to the research program
  (seg2 finding 5). RECOMMENDATION: yes, one paragraph, user-ratified
  wording — the front door currently hides the program entirely.
- **UD-6: S25bis_diff_convergence repair-list R1-R13 execution
  status** (seg3's highest-priority at-risk item: if unexecuted,
  [X-DEFTW] is blocked and a registry row is unminted).
  RECOMMENDATION: this is a VERIFY duty, not strictly a decision —
  but it lands here because if verification finds the repairs
  unexecuted, the user must schedule the micro-commit (this window or
  F2-entry, named). The judge must carry it either way; S-ORDINE
  cannot close calling itself nothing-lost with this row UNRESOLVED
  and unnamed.

---

## 7. RIGHT-SIZING — what P1 deliberately does NOT do

- **No carrier/gate-file moves, no driver split.** Moving
  validation/*.py or gate .json breaks registry anchors and imports;
  the flat directory is fully de-entropized by the index alone. The
  monolithic-driver split is REGISTERED fuori-scope: owner F2 window +
  pipeline-sense review (it touches carriers), per contract.
- **No new directory taxonomy beyond archive/.** Subdividing
  validation/ by class (advisories/ logs/ carriers/) reads nicely and
  breaks dozens of anchors for zero lint payoff — the index IS the
  taxonomy.
- **No wholesale prose->yaml conversion** (P1-16). No "session log
  schema", no typed advisories. Logs stay append-only prose.
- **No glossary maximalism.** One row per registry-resolved token
  family, full rows only for collisions and unregistered tokens
  (P1-12). A 700-row glossary would itself be entropy and rot
  instantly.
- **No D6 rewrite.** The two-spine layering (F0-F6 live / A0-A7
  historical) is internally governed by its §0-pre note; folding it is
  cosmetic churn on the highest-traffic plan file. Not touched.
- **No re-litigation** of any S14-S25bis verdict; status calls here
  are archival, never substantive.
- **No CI / scheduled automation.** REGISTERED fuori-scope with owner:
  infra/env decision row (census), user-owned; the lints run in the
  existing suite.
- **No P-1 distillation pipeline.** REGISTERED fuori-scope: owner P-1
  window (D6 §3), per contract.
- **No GENO-side action of any kind.** Read-only throughout;
  GENO-internal duplication (sundials trees) recorded, out of
  jurisdiction.
- **No log-file archival in this window.** The 24 .log stay in place
  until the findings-registry evidence-field check (seg5 §F note on
  the three M6 probe logs) is done — a named follow-up, not a silent
  drop.

FUORI-SCOPE REGISTRATIONS (each = a census/registry row with owner,
never executed here): driver split (F2 + sense-review); CI (infra
row, user); P-1 distillation (P-1 window); log archival pass
(post-evidence-check window); optional ratchet of glossary lint to
historical validation/ corpus (any later hygiene window).

---
## RECONCILIATION OF THIS POSITION AGAINST THE BRIEF
Deliverables 1-7 delivered in §1-§7. Proposals numbered P1-1..P1-16;
standing rules SR-1..SR-10; migration steps M-0..M-9 each with its
nothing-lost verification; user decisions UD-1..UD-6 (UD-1 first =
the commit/durability question, recommendation YES). T2-bis items
covered: glossary+lint (P1-12/SR-4), A1_* flag registry (P1-13/SR-5),
measured orchestration-weight (SR-9), R3-closure checklist lines
(SR-1/2/6/7/9/10 + CLAUDE.md delta), flat-dir hygiene priced (P1-2,
M-3, §7). Primary lens realized structurally in P1-3/P1-4 (plan-anchor
column mandatory + ORPHAN loud + need->artifact->proof as the default
navigation chain).
