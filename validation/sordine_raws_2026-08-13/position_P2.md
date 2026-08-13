# EXPERT POSITION P2 — PROVENANCE & RESEARCH DURABILITY
# S-ORDINE Phase 2, 2026-08-13. Reader: P2 (provenance/durability lens).
# Contract: validation/ADVISORY_Sordine_prompt_2026-08-12.md (read integral).
# Inputs: all seven Phase-1 inventories (seg1-seg7, read integral) +
# spot-checks: docs/findings_registry.yaml (read integral, 20 rows
# confirmed), the contract sections 2/4/4-bis/4-ter/5.
# Verdicts S14-S25bis are of record and are NOT re-litigated here.
# Proposals numbered P2-1..P2-16 (P2-14/P2-15 intentionally unassigned)
# + P2-SR-1..P2-SR-10 + P2-D1..P2-D6, for refuter/judge citation.

---

## 0. LENS VERDICT (the provenance stakes, stated up front)

A research program whose bar is "SOTA academic + industrial, precision
and rigor above all" (repo-sota-standard) currently keeps its OF-RECORD
adjudication corpus in the single most fragile storage class available:
**untracked single-copy files on one Windows disk**. Measured (fresh
diagnosis 2026-08-13, authoritative over the prompt's 2026-08-12
numbers 428/238):

- 34 advisory-class .md (ADVISORY/AUDIT/DISPATCH/PANEL/ADR) — ALL
  untracked, zero git history. These carry: the EQ-v2 hypothesis
  structure of record, the SOTA gap map (~108 adjudicated objects:
  36 GAP + 16 AC + 11 Q + 45 choice-ledger rows), the 34-row generality
  ledger with user scope-pin verbatim text, the topology census with 11
  user pins and ZERO registry rows, the engine-speed plan with measured
  numbers that appear nowhere else, the S-CERT session contract (R33),
  and the S25bis diff-convergence repair record whose execution status
  seg3 flags as the highest-priority loss-hunter item.
- 27 session logs PROGRESS_* — untracked. They are the ONLY step-level
  evidence chain: commit messages cite them; PROGRESS.md carries only
  summaries; the registry cites two of them as `source:` anchors
  (PROGRESS_2026-08-12_S25bis_speed.md is the source of THREE registry
  rows including the cross-lowering floor).
- 25 .json gate memos — untracked. `validation/s25_spdb_m6.json` IS the
  M6 rejection verdict of record; the GAP-29 flip datum
  (s25bis_gap29_ntf50.json) is a registry `magnitude:` citation.
- 17 raws + 24 run logs — untracked (three M6 probe logs carry
  mechanism-isolation evidence flagged borderline-at-risk by seg5).
- Memory (37 files) lives OUTSIDE the repo entirely, in the harness
  profile directory: the verbatim Italian user orders — the primary-
  source form of every standing rule — exist nowhere else (seg6).
- Parent root: VALIDATION.md §3 (7 substantive corrections incl. the
  SK Table-1 "704 s is a paper typo" finding), SDToolbox.zip (the audit
  input), brick2_profiles_record.png (S18 record figure, misplaced) —
  single copies outside any git.

The provenance CHAIN the program has built is excellent — finding ->
carrier (.py, tracked) -> gate (json/log) -> registry row (tracked,
linted) -> theory doc (tracked) — but its middle links (gate evidence)
and its adjudication layer (advisories, logs) are the untracked part.
One disk failure, one aggressive `git clean -fdx`, one accidental
directory cleanup, and the program keeps its code and theory but loses
its EVIDENCE and its DECISIONS: exactly the part JPP peer review and
the S-CERT audit will ask for. R4 says "nulla si perde"; today that
guarantee is aspirational, not structural.

**Headline recommendation (P2-D1 below): COMMIT the of-record corpus.
Everything else in this position is designed to work whether or not
the user ratifies that, but the honest ranking is: git tracking is the
single highest-value, lowest-cost durability move available, and the
original reasons for the ADR-untracked pattern are all superseded by
machinery that now exists (index + status taxonomy + registries).**

Why the ADR-untracked pattern existed (weighed honestly, per brief):
1. ORIGIN: ADR_panel_2026-07-16.md was "NOT YET RATIFIED / AWAITING
   USER RATIFICATION" — untracked encoded "not yet normative". Valid
   then; superseded now: the status taxonomy (P2-6) + index row encode
   normativity explicitly, so location/tracking no longer needs to.
2. FREEZE DISCIPLINE: tracked files are frozen while consumers run;
   advisories are repaired IN PLACE ([S25-REPAIR], RT-1..RT-6 inline
   annotations) — untracked files could be edited without commit-
   protocol friction mid-session. Valid concern; answered by
   commit-at-session-boundary (R3 close), not by permanent untracking.
3. PARALLEL SESSIONS: advisory sessions (S-SPEED, S-GAUNTLET, litmap)
   run read-only in parallel and cannot commit. Answered the same way:
   the OWNING session commits the landed advisories at its R3 close.
4. NOISE AVERSION: not polluting the commit history with drafts.
   Answered by the taxonomy: RAW stays untracked-or-archived by
   POLICY (a declared class), OF-RECORD gets committed. The
   distinction becomes typed instead of accidental.
None of the four reasons, examined, justifies keeping VERDICTS OF
RECORD in single copy. The one real hazard of committing — an
accidental `git add -A` sweeping GENO/ — is neutralized structurally
(P2-16: .gitignore GENO/ + explicit-pathspec rule).

---

## 1. TARGET STRUCTURE (deliverable 1)

**P2-1 — Extend SCAFFOLD L0-L6, do not invent a parallel taxonomy.**
Seg1 F-SEG1-3 is right: docs/rde_nozzle_SCAFFOLD.md is the in-corpus
prior art for exactly this operation (typed registry + layers + lint +
migration-with-acceptance, executed S9). The S-ORDINE target adds
layers/registries to it; a second competing architecture would itself
be entropy. Proposed delta: SCAFFOLD gains L7 (evidence layer =
validation/) and L8 (literature layer), plus the new registries listed
below, via a dated amendment section (original preserved).

**P2-2 — Target tree (explicit; moves are minimal by design, see P2-13):**

```
docs/
  rde_nozzle_MASTER.md (M0)          [unchanged — top of authority]
  rde_nozzle_*.md (D1-D8, attacks,   [unchanged; roadmap_geno_rde.md
    governance, P-1/P-2 drafts)        gains its missing banner]
  rde_nozzle_SCAFFOLD.md             [amended: L7/L8 + registry list]
  rde_nozzle_PROGRESS.md             [SLIM: ORA/NEXT/BLOCCATO +
                                      ONE consolidated census table
                                      R1-R33 one-row-per-item]
  rde_nozzle_PROGRESS_ARCHIVE.md     [NEW: historical blocks, stale
                                      NEXT blocks, S1-S13 LOG tail —
                                      verbatim, banner at head]
  claims_registry.yaml               [unchanged, lint (xv)]
  findings_registry.yaml             [grows: R31 corpus seeding]
  choice_ledger.yaml                 [NEW T2(ii): C1-C45 extracted,
                                      strict-subset schema, linted]
  literature_registry.yaml           [NEW T2(vi): one row per paper
                                      across THE THREE ROOTS, honest
                                      read-status, WANTED with owner]
  glossary.yaml                      [NEW T2-bis(a): namespace-
                                      qualified tokens, linted]
  flags_registry.yaml                [NEW T2-bis(b): one row per A1_*
                                      env flag; may live as a typed
                                      section of glossary.yaml if the
                                      judge prefers one file]
validation/
  ADVISORY_INDEX.md                  [NEW T2(iii): ONE ROW PER
                                      DOCUMENT — path | class |
                                      status | PLAN-ANCHOR |
                                      supersession ptr | at-risk
                                      destination. THE navigation.]
  INDEX.md                           [stays: session-log index;
                                      cross-referenced from
                                      ADVISORY_INDEX or merged into
                                      it — judge's call, one index
                                      is cleaner]
  ADVISORY_*.md, AUDIT_*, PANEL_*,
    DISPATCH_*, ADR_*                [STAY AT CURRENT PATHS —
                                      they are anchor targets of
                                      findings_registry source: rows;
                                      status lives in the INDEX +
                                      in-file banner, NOT in location]
  PROGRESS_*.md (27 session logs)    [stay; indexed; committed if D1]
  *.py carriers (33)                 [NEVER MOVED — priced constraint;
                                      registry doc/carrier anchors +
                                      imports break]
  *.json gate artifacts (25)         [stay: consumed by gates/tests
                                      at coded paths]
  *.log (24)                         [stay OR archive/ move for the
                                      non-cited subset only (P2-13)]
  sordine_raws_2026-08-13/           [stays as the S-ORDINE raw layer]
  sota_gapmap_raws_2026-08-12/       [stays: RAW class, indexed]
  archive/                           [NEW but MINIMAL: only files
                                      with ZERO inbound machine
                                      anchors move here (P2-13);
                                      every moved file gets banner +
                                      index row update]
memory/ (harness-side)
  MEMORY.md                          [stale numpy line fixed; 2
                                      inline entries typed into
                                      backing files]
  session memories                   [dated supersession banner on
                                      routing half of the 9 unmarked
                                      HISTORICAL-SESSION files]
```

**P2-3 — PLAN-ANCHOR traceability as the default navigation.**
The primary lens (need -> artifact -> SOTA proof) becomes navigable
in exactly one place: ADVISORY_INDEX.md carries a mandatory PLAN-ANCHOR
column (D6 phase / census row / registry row / gate / standing
directive), mirroring the Phase-1 inventory schema. The registries
already carry owner+trigger (need side) and source+code anchors (proof
side). Navigation of record becomes: plan (D6) -> census row
(PROGRESS consolidated table) -> registry row (findings/claims/choice)
-> source anchor (advisory/log at its stable path) -> carrier/gate.
Every hop machine-resolvable (P2-9). An artifact with an empty
PLAN-ANCHOR cell = ORPHAN FINDING = lint failure, never silent.
Known orphans already flagged by Phase 1 and inherited here loudly:
`t --count HEAD:q`, `er.name`, `.claude/scheduled_tasks.lock`,
PARENT old_commit_hashes.txt / old_short_hashes.txt, mailmap.txt +
current_commit_messages.txt (pending verification, P2-D3/D5).

**P2-4 — The lecture-era layer gets an explicit banner-type.**
Seg5's finding stands: the 17 LECTURE-ERA validation docs answer the
tool-credibility need (G1 inherits from it), not a D6 phase. They get
index class `LECTURE-ERA` (orthogonal tag, still OF-RECORD frozen) so
the plan-lens navigation never mixes substrate V&V with program
artifacts. No moves.

---

## 2. STATUS TAXONOMY (deliverable 2)

**P2-5 — Status enum (per-document, in index + in-file banner):**

- **OF-RECORD** — current authority for its content. Sub-tag
  `(living)` for files that legitimately mutate (PROGRESS, INDEX,
  registries, numeric_allowlist).
- **OF-RECORD-PENDING-CONTRACT** — live prompt for a future session
  (ADVISORY_Scert_prompt: may not be archived or altered; consumed at
  its session).
- **SUPERSEDED-BY-\<path\>** — replaced as authority; dated banner at
  head pointing to the successor; text preserved verbatim (R4).
  Existing exemplars: the two historical notes; the gauntlet ledger's
  "SUPERSEDED SAME DAY" note.
- **CONSUMED** — an order/dispatch fully executed; pointer to the
  executing session log + commit. Sub-form `CONSUMED-with-residue`
  when named rows are not yet re-homed (e.g. engine_speed_audit
  N1-N8/DEAD/Q1-Q6 until registry rows exist — the file stays
  OF-RECORD until then; consumption is per-row, tracked in the index
  note, not hand-waved).
- **RAW** — agent working output whose judged content lives in a named
  advisory (gapmap raws, refuter files). Never normative, never
  deleted; archived-in-place with index row.
- **DERIVED** — regenerable by a named owner (pyc, run logs, report
  copies, figs, txt extracts). Regeneration owner named in index.
- **LECTURE-ERA** — orthogonal layer tag (P2-4), combinable with
  OF-RECORD/CONSUMED.

**P2-6 — Supersession discipline (extends the working convention
F-SEG1-4):** the corpus-wide convention "original preserved + dated
in-place marker" is already applied consistently INSIDE docs/; it
becomes typed: every `SUPERSEDED` marker MUST carry (a) date, (b)
pointer to successor, (c) an index row whose status matches. The
in-file banner and the index row are redundant BY DESIGN (one is
human-first, one is machine-first); the lint (P2-9) checks they agree.
Status changes are append-only events (a new dated banner line), never
edits of old banners — the supersession history is itself provenance.

**P2-7 — Per-row consumption maps for high-density advisories.** For
the files whose consumption is inherently partial (claims_to_code
C-1..C-6; engine_speed_audit N/DEAD/Q rows; redteam ISS rows;
mean_swirl F2a deltas), the index row links to a short per-claim
consumption note (a table in the index entry or the file's banner):
row -> CONSUMED-at(session/commit) / OPEN-with-owner. This is the
honest alternative to both "mark the whole file consumed" (loses open
rows) and "keep it all of-record forever" (entropy). The R31 seeding
(T2(i)) produces most of these rows mechanically.

---

## 3. WHAT GETS TYPED + LINTED (deliverable 3)

Pattern precedent: strict-subset schema + seeded rejectors + suite
group, exactly as (xv)/(xix). Proposed NEW groups, extending (i)-(xix):

**P2-8 — (xx) index-coverage lint.** Every `validation/*.md` (and
`validation/*/ *.md`) has exactly one ADVISORY_INDEX/INDEX row; every
row's path exists; status from the P2-5 enum; PLAN-ANCHOR cell
non-empty or the row is explicitly flagged ORPHAN (a visible state,
not a pass); SUPERSEDED rows have date+pointer and the pointed file
exists. Seeded rejectors: an unindexed doctored file; a row with
status outside the enum; a SUPERSEDED row missing its pointer.

**P2-9 — (xxi) anchor-resolution lint — THE nothing-lost machine
guarantee.** Every `source:`/`evidence:`/`code:` anchor in
findings_registry, choice_ledger, literature_registry (and the doc
paths in claims_registry, already covered by (xv)) resolves to an
existing file; `#section` fragments grep-resolve in the target. This
lint is ALSO the pre/post-move gate of the migration (P2-13): any
archive move that breaks an anchor turns the suite red. Seeded
rejector: one doctored anchor to a non-existent path must fail.
(This makes "a file was lost/moved silently" a machine event forever —
the durable half of the 4-ter gate.)

**P2-10 — (xxii) glossary + flags resolution lint.** glossary.yaml is
NAMESPACE-QUALIFIED (seg4/seg6 both measured heavy collisions: O5,
M1, T2, F4, C1, L4, U1 each carry 2+ meanings — an unqualified
glossary would re-mint the ambiguity it exists to kill). Schema:
token, namespace (census-row / gate / theorem / carrier / phase /
speed-lever / probe / panel-local...), meaning, defining anchor.
Lint: every [X-*]/GAP-*/[T-*]/[S-*]/[C-*]/[D-*]/DIR-*/R\d+ token used
in the OF-RECORD doc set resolves to a glossary or registry row;
every A1_* flag grep-found in validation/*.py has a flags_registry
row (default, meaning, covering gate, tested pairs, cartesian product
DECLARED untested) and every registry row's flag exists in code
(bidirectional). Seeded rejectors both directions. Seed corpus: the
Phase-1 token tables (214 + 178 + 78 + 231 + 70 tokens collected —
dedup at build time).

**P2-11 — (xxiii) literature-registry lint.** One row per paper
across the three roots (13 + 10 + 20 research-grade; vendor-docs and
GENO figures registered as bulk classes, not per-row — right-sizing).
Schema: file path(s) (dedup key: the same paper in two roots = ONE
row, two paths), bibliographic identity, read-status enum
{READ-INTEGRAL, READ-PARTIAL, UNREAD, WANTED}, where-read anchor
(advisory/log/litmap section — must resolve), content-of-record
one-liner, notes. Lint: every literature/ PDF has a row; every
where-read anchor resolves; WANTED/UNREAD rows carry owner; UNREAD
rows have EMPTY content fields (the "never fake a summary" rule as a
machine check — a non-empty summary on an UNREAD row FAILS). Seeded
rejectors: doctored unregistered PDF; UNREAD row with summary text.
Seg7's inventory is the direct seed source; the WANTED list (AIAA
2019-0197, Peter-Desideri 2022, Ancourt 2023, L-P 2023, Tillyaeva
1975, Naumova-Shmyglevskii 1967, Breitkopf-Ulbrich) lands as WANTED
rows with owners, not as fetch work in this session.

**P2-12 — (xxiv) choice-ledger lint.** docs/choice_ledger.yaml
extracted from the gap-map annex (C1-C45): strict-subset schema
(id, question, status {DECIDED/MIXED/SINGLE-AUTHOR/NEVER}, evidence
anchor, owner for every non-DECIDED row), lint mirrors (xix): status
enum, owner required on open rows, anchors resolve, dedup by id.
Nothing-lost check at extraction: 45 source rows == 45 yaml rows,
each carrying its source anchor back into the gap-map annex (which
stays in place as the prose authority — the yaml is the index, per
the SCAFFOLD "registry = index never content" conflict rule).

Deliberately NOT a new lint (right-sizing, P2-20): supersession-marker
grep folds into (xx); orchestration-weight reporting stays a checklist
line (P2-SR-8) because its natural home (session log prose) is not a
machine-checkable schema without over-engineering.

---

## 4. MIGRATION PLAN (deliverable 4 — ordered, each step with its
## nothing-lost verification; priced constraint respected: NO .py
## moves, NO json moves, physical moves last and minimal)

**P2-13 — Minimal-move doctrine (the provenance-lens rule).**
Supersession is a STATUS, not a LOCATION. Every advisory-class file is
(or will be, after seeding) an anchor target; physical relocation
buys nothing durability-wise (git tracking does) and risks anchor
breakage. Therefore archive/ receives ONLY files proven to have ZERO
inbound machine anchors (computed by running the P2-9 lint against a
candidate move-list) AND status CONSUMED/SUPERSEDED/DERIVED. Expected
qualifying set is small: ADVISORY_plan_v2_draft (superseded),
DISPATCH_Sspeed_to_S25 (fully redundant per seg4), consumed session
prompts IF nothing anchors them, and the non-cited subset of the 24
run logs. If in doubt, banner-in-place and DON'T move.

Ordered steps:

**STEP 0 (conditional on user decision D-1): commit the corpus.**
Durability precedes reorganization — if the disk dies during the
migration, steps 1-6 saved nothing. Explicit pathspec adds
(validation/*.md, validation/*.json, validation/*.log by list, raws
dirs), never `git add -A`; GENO/ ignored first (P2-16). Verification:
`git status --porcelain` empty for validation/ afterwards; file count
added == the untracked count from the fresh diagnosis; the commit is
tagged [F-SERVICE/S-ORDINE][PIANO/R32].

**STEP 1: build ADVISORY_INDEX.md + in-file banners (no moves).**
Source: the four advisory/log inventory files (seg3, seg4, seg5) —
their PATH/CLASS/STATUS/PLAN-ANCHOR rows convert mechanically.
Verification: lint (xx) green; row count == fresh count of
validation-tree .md files (82 + raws subdirs), reconciled to
discrepancy 0 against `ls`.

**STEP 2: registry seeding + extraction (the R31 first duty).**
Tranches, each with its own count reconciliation and lint (xix)/(xxi)
green before the next: (a) audit 94 rows (find->verify bounded, dedup
against the 20 existing — seg4 measured ~90-91 unseeded); (b) gap-map
36 GAP + 16 AC + 11 Q; (c) choice ledger 45 -> choice_ledger.yaml
(P2-12); (d) refuter/red-team S25/S25-bis residues; (e) the
per-row consumption maps of P2-7. Verification per tranche: source
count == destination count + explicitly-listed dedup merges (a merged
row is COUNTED and named, not dropped — the throat-panel demonstrator
is the precedent); every new row's source anchor resolves (lint xxi).

**STEP 3: literature_registry.yaml.** Seed = seg7 inventory rows
verbatim (identities, read-status, where-read anchors). Verification:
137 files - 52 vendor-docs - 5 GENO figs - 26 pptx-lineage - assets =
paper rows all present; 3-root reconciliation discrepancy 0; lint
(xxiii) green incl. the UNREAD-empty-summary rejector; the two
cross-root dedup pairs (harroun.txt=hr.txt; CVA.pdf=CVA.pptx render)
recorded as dedup rows.

**STEP 4: PROGRESS slim + PROGRESS_ARCHIVE.** Fold the census (S24
consolidated snapshot + S25 delta + S25-bis delta + ORA-block new
rows) into ONE one-row-per-item table R1-R33; move the five stale
NEXT blocks, the reverse-chronological session blocks, and the S1-S13
LOG tail to PROGRESS_ARCHIVE.md verbatim under a dated banner.
Verification (nothing-lost): (i) every census row id R1-R33 appears
EXACTLY ONCE in the new table and its state is traceable to the
newest delta block mentioning it (spot-audited by the loss-hunter);
(ii) line-conservation: chars(slim) + chars(archive) >= chars(original)
minus only the delta-block headers, diff reviewed; (iii) BLOCCATO 1-8
and the NEXT chain present verbatim; (iv) S1-S13 LOG entries (which
have NO validation/ log files — seg1 flagged this as unique-at-risk)
land in the ARCHIVE verbatim, never summarized.

**STEP 5: memory sweep (T2(v)).** (a) dated supersession banner on
the routing half of the 9 unmarked HISTORICAL-SESSION memories
(verdict halves untouched); (b) fix the 3 broken [[links]] (s24-deftw
-> s24-f1b-def-twin; s24-* wildcard; the gauntlet pseudo-link); (c)
fix the stale MEMORY.md numpy line (actively misleading vs the O5
decision); (d) type the two inline-only entries (POST-S20, POST-S21
SERA) into backing files with index lines. Verification: 37+2 files
accounted; link-check re-run clean; MEMORY.md index lines == file
count. DURABILITY NOTE (open decision D-4): memory lives outside the
repo; the verbatim user orders should additionally land in a tracked
mirror (docs/ or validation/ standing-orders file) — cheap, one file.

**STEP 6: physical archive moves (optional, last).** Compute the
zero-inbound-anchor list (P2-13); move; banner; index update.
Verification: lint (xxi) + (xx) green POST-move; pre/post tree diff
shows moves only, no deletions.

**STEP 7: the 4-ter gate.** (i) consolidated at-risk ledger (the
Phase-1 "NOTHING-LOST LEDGER FEED" sections of all seven inventories,
merged) -> per-item destination map (registry row / archived file
with index row / glossary row / ARCHIVE block); (ii) seeded rejector:
remove one item in-memory, gate must FAIL; (iii) adversarial
loss-hunter with the canary item; (iv) final reconciliation at
discrepancy 0 against the fresh 436-file count (note of record: the
prompt says 428/238, fresh diagnosis 436/240 — the DELTA ITSELF must
be reconciled by name: S-ORDINE's own raws + any new files since
2026-08-12; an unexplained delta is a gate failure, both directions).

**Parent-root rescues (inside STEP 2/3, priced small):**
- Copy brick2_profiles_record.png into validation/ with index row
  (the S18 record figure currently misplaced outside the repo).
- VALIDATION.md §3 seven-corrections list + CONTINUATION_PROMPT §5
  per-paper notes -> literature_registry note fields (destination for
  seg7 at-risk rows 1-2).
- SDToolbox.zip: registered in the index/literature registry as the
  single-copy audit input at its parent path (moving a 4.5 MB zip
  into the repo = user decision D-4; registering it costs nothing).
- Garbage adjudications (D-3/D-5): current_commit_messages.txt diffed
  against `git log --format=%B` (if identical -> DERIVED, dispose per
  user; if not -> OF-RECORD provenance of the author rewrite);
  old_*_hashes.txt checked against reflog before any disposal.

---

## 5. STANDING RULES DRAFT (deliverable 5 — the education half;
## each rule names its enforcing lint or its checklist line)

- **P2-SR-1 (index-or-fail):** every new document under validation/
  gets its index row + status IN THE SAME WINDOW it is created.
  Enforced: lint (xx) fails the suite on any unindexed file. This is
  the T3 "ogni advisory nuovo = riga indice + righe registry nella
  stessa finestra" R3-checklist line, made mechanical.
- **P2-SR-2 (findings land as rows):** any advisory that adjudicates
  findings/gaps/choices mints or updates registry rows in the same
  window; prose-only findings are re-mint fuel. Enforced: (xix)
  dedup/anti-re-mint + R3 checklist line; loss-hunter samples.
- **P2-SR-3 (no single-copy of-record):** a document with index
  status OF-RECORD must be git-tracked. Enforced: lint (xx) gains a
  tracked-check (`git ls-files`) IF D-1 is ratified; until then this
  rule is DECLARED-INACTIVE-BY-USER-DECISION in the index header —
  visible, not silent.
- **P2-SR-4 (supersession is dated, pointed, append-only):** P2-6
  discipline. Enforced: lint (xx) SUPERSEDED-row checks.
- **P2-SR-5 (anchors never break):** renames/moves of anchor targets
  only with lint (xxi) green in the same commit. Enforced: (xxi) in
  the FAST tier.
- **P2-SR-6 (glossary resolution):** a new codename token in an
  OF-RECORD doc must resolve (glossary or registry) in the same
  window; new namespaces declared. Enforced: lint (xxii). [T2-bis(a)]
- **P2-SR-7 (flag registry):** a new A1_* flag ships with its
  registry row (default, gate, tested pairs, untested product
  DECLARED). Enforced: lint (xxii) bidirectional check. [T2-bis(b)]
- **P2-SR-8 (measured orchestration weight):** every orchestration
  reports shape + agent count + token order in the session log
  (orchestration-weight-sota made checkable). Enforced: R3-closure
  checklist line (declared honest limit: prose check, not lint; the
  S-CERT MC-audit and the loss-hunter can sample it). [T2-bis(c)]
- **P2-SR-9 (literature honesty):** every new PDF gets a registry row
  at arrival; UNREAD stays UNREAD (empty summary enforced by xxiii);
  reads upgrade status with a where-read anchor in the same window.
- **P2-SR-10 (R3 closure sweep, one added line):** the R3 checklist
  gains exactly ONE line — "index/registries/glossary lints green +
  new documents indexed + census table updated one-row-per-item" —
  keeping R3 short (education by lint, not by longer checklists).

CLAUDE.md delta (T3, user-ratified): one short paragraph under R3
naming the index + registries as closure obligations and pointing to
the lint groups; plus the GENO-ignore line of P2-16. Proposed text
lands in the judge's plan, not unilaterally.

---

## 6. OPEN USER DECISIONS (deliverable 6 — recommendation + trade-offs)

**P2-D1 (FIRST — the single-copy durability question): commit the
OF-RECORD advisory corpus + session logs + gate .json (+ raws) to
git. RECOMMENDATION: YES, at S-ORDINE close, one dedicated commit.**
- FOR (provenance lens): git history = free replication, tamper
  evidence, bisectable provenance; the S-CERT audit (R33) and JPP
  review both interrogate the evidence chain — an auditor told "the
  adjudication corpus is untracked single-copy" will (correctly)
  flag it; the 4-ter nothing-lost gate is hollow if the ledger it
  protects can vanish with the disk; the ADR-untracked reasons are
  superseded (§0).
- AGAINST (weighed honestly): (a) repo weight — trivial, the corpus
  is text (~2-3 MB; AUDIT_agnostic 277 KB is the largest); (b)
  in-place repair friction — advisories get edited ([S25-REPAIR]);
  answered: commits at session boundaries only, edits stay free
  intra-session; (c) history noise — bounded by one-commit-per-close;
  (d) GENO sweep risk — neutralized by P2-16 BEFORE the add; (e) the
  "raw layer should not look normative" worry — answered by the
  status taxonomy: tracking ≠ normativity, the index says what is
  of record.
- Fallback options if NO: (b1) commit advisories only, logs stay
  untracked (protects verdicts, still loses the step-evidence);
  (b2) scheduled off-repo backup of validation/ (protects bytes,
  loses history/tamper-evidence and adds an infra dependency).
  Both strictly weaker; named for completeness.

**P2-D2: run-log (.log) tracking policy.** Recommend: commit the
evidence-cited subset (the three M6 probe logs + gate finals + the
GAP-5/GAP-29 runs — anything a registry `evidence:`/`magnitude:` row
cites), leave the rest DERIVED-untracked with index rows; alternative
= commit all 24 (they are small text; simpler rule). Low stakes;
either is durable enough once D-1 covers the json memos.

**P2-D3: garbage-candidate disposal** (`t --count HEAD:q`, er.name,
scheduled_tasks.lock, PARENT old_*_hashes.txt, hr.txt duplicate) —
after the STEP-2 verification diffs prove DERIVED/duplicate status:
archive-with-banner vs delete is R4-adjacent and the user's call.
Recommend: delete the two byte-identical shell accidents + the lock
(zero content, verified), archive the hash files IF reflog shows a
rewrite (provenance map), else delete; hr.txt delete (md5-identical
twin retained).

**P2-D4: parent-root rescues** — copy brick2_profiles_record.png into
the repo (recommend YES, it is a record figure); move/copy
SDToolbox.zip into the repo vs register-in-place (recommend
register-in-place: 4.5 MB, stable, single well-known location); add a
tracked mirror of the memory verbatim-orders (recommend YES, one
docs/ file, cheap durability for the primary-source user orders).

**P2-D5: mailmap.txt + current_commit_messages.txt** disposition
pending the STEP-2 diff check (if messages identical post-rewrite:
DERIVED, dispose; else: the only pre-rewrite record -> commit as
provenance). Recommendation follows the diff, not a preference.

**P2-D6: README.md one-paragraph pointer** to the research program
layer (seg2 finding: the front door doesn't mention the program).
Recommend YES, user-ratified text at T3.

(6 decisions. D-1 is the one this position exists to argue.)

---

## 7. RIGHT-SIZING — WHAT P2 DELIBERATELY DOES NOT DO (deliverable 7)

- **No physical reorganization of the flat validation/ dir** into
  thematic subdirs. The index IS the navigation; moves burn anchor
  risk for aesthetics. (Scope creep = entropy.)
- **No .py carrier moves, no driver split** — registered:
  findings_registry `structure:monolithic-driver-module`, owner F2
  window with perimeter sense-review. Not touched here.
- **No CI / scheduled suite** — registered:
  `infra:scheduled-ci-multiplatform`, owner = user infra window.
- **No P-1 distillation pipeline** — FUORI-SCOPE per contract;
  registration proposed: one census/registry row "P-1 provenance
  package" (owner: P-1 submission window; content: the Appendix-B
  mapping below is its seed). Never executed here.
- **No literature fetching or re-reading** — WANTED rows with owners
  only (P2-11); the SK re-read and Wolanski research-grade read stay
  queued rows.
- **No re-summarization of theory or verdicts** — archives are
  verbatim-with-banner; S14-S25bis verdicts untouched (TERMS).
- **No per-row yaml-ification of everything** — the gap-map/audit
  PROSE stays the content authority in place; registries are indexes
  (SCAFFOLD conflict rule). I explicitly REJECT any proposal to
  transcribe full advisory bodies into yaml: that duplicates content,
  creating the two-sources-of-truth entropy this session exists to
  kill.
- **No new lint beyond the five groups (xx)-(xxiv)** — in particular
  no prose-quality lints, no orchestration-weight lint (checklist
  line instead, declared honestly in P2-SR-8).
- **No consumption of pending user decisions** (filelock/O5/M6
  adoption) — they remain BLOCCATO rows of their F2/session-boundary
  windows (TERMS).
- **P2-16 (do execute — safety precondition, 2 lines):** add `GENO/`
  to .gitignore + a CLAUDE.md line "adds by explicit pathspec only,
  never `git add -A`" BEFORE any STEP-0 commit. This is the one
  structural mitigation the D-1 recommendation depends on.

---

## APPENDIX A — SINGLE-COPY AT-RISK CONCENTRATION (top of the merged
## nothing-lost ledger, provenance-ranked; feeds STEP 7 destination map)

| # | Item (single-copy today) | Where | Destination under this plan |
|---|---|---|---|
| 1 | S25bis diff-convergence repair R1-R13 EXECUTION STATUS (X-DEFTW block risk) | ADVISORY_S25bis_diff_convergence | LOSS-HUNTER VERIFY FIRST (seg3 flag): git log after ea8143c + registry row `persistence:derive-artifact-...` EXISTS (verified: it does, DISCHARGED with R7-R9 evidence — the repair landed; index row must still record the advisory as consumed-by-that-row) |
| 2 | AUDIT_agnostic ~90-91 unseeded finding bodies | untracked advisory | STEP-2(a) registry rows + commit (D-1) |
| 3 | Gap-map 36+16+11+45 adjudicated objects | untracked advisory | STEP-2(b,c) + commit |
| 4 | Topology census: 11 CEN pins + user decisions 2026-08-02, zero registry rows | untracked panel + memory pointer pair | commit (D-1) + glossary/census rows; promotion session stays queued with owner |
| 5 | EQ-v2 full hypothesis structure + O1-O5 obligations | def_equivalence panel | commit; registry consumption map P2-7 |
| 6 | Gauntlet 34-row ledger + DUTY ratifications + scope-pin verbatim | untracked advisory | commit; rows already partly in D6/M0 — index consumption map |
| 7 | S-CERT contract MC1-MC8 (R33 depends on it) | untracked prompt | commit; status OF-RECORD-PENDING-CONTRACT, untouchable |
| 8 | Engine-speed audit measured numbers + N1-N8/DEAD/Q rows | untracked advisory | commit + STEP-2(d) residue rows |
| 9 | 27 session logs (only step-level evidence; 3 are registry source anchors) | untracked | commit (D-1) |
| 10 | Gate .json incl. m6 rejection verdict + GAP-29 flip artifacts | untracked | commit (D-1/D-2) |
| 11 | Memory verbatim user orders (37 files, outside repo) | harness dir | STEP-5 sweep + D-4 tracked mirror |
| 12 | PROGRESS census R1-R33 states + S1-S13 LOG (tracked but single consolidated home) | PROGRESS.md | STEP-4 slim+archive, both tracked |
| 13 | PARENT VALIDATION.md §3 corrections + CONTINUATION §5 notes + SDToolbox.zip + brick2 png | parent dir | STEP 2/3 rescues + D-4 |
| 14 | ADR panel ratification status + its OPEN QUESTION FOR USER | ADR_panel file | index row flags the unresolved ratification; user decision row minted (it may be a still-pending decision — never silently absorbed) |

## APPENDIX B — WHAT JPP PEER REVIEW / P-1 WILL DEMAND (provenance
## requirements mapped to artifacts of this plan)

1. Every number in the paper -> committed script + test (R5; already
   structural via carriers + golden tests). No change needed.
2. Novelty claims query-bounded -> D2 G1-G14 table + litmap advisory
   + choking census (the misquote CORRECTION of record is itself a
   reviewable asset). Requires: those advisories durable (D-1) and
   literature_registry rows anchoring where each source was
   page-verified (STEP 3).
3. Citation integrity -> literature_registry read-status (READ-PARTIAL
   sources never quoted beyond their page-verified content; UNREAD
   never cited — P2-SR-9 enforces the discipline the litmap refuter
   already demanded, e.g. E4 spot-check-before-print).
4. Correction history -> dated supersession chain (P2-6) gives the
   reviewer-facing story "we found X wrong on date D and here is the
   fix" — a strength, not an embarrassment, IF preserved.
5. Reproducibility of verdicts -> gate .json + logs tracked (D-1/D-2);
   the cross-lowering-floor row already declares the honest
   platform-dependence limit.
6. Human gate G5 (Kraiko/PMM) -> commission docs already of record;
   the index makes their pending state visible.
This mapping is the seed of the FUORI-SCOPE "P-1 provenance package"
row (owner: P-1 submission window) — registered, not executed.

---
END OF POSITION P2. Proposals P2-1..P2-16, standing rules
P2-SR-1..P2-SR-10, user decisions P2-D1..P2-D6.
