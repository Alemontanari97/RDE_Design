# REFUTATION — S-ORDINE Phase 3 (dedicated refuter, default-refute)
# Date: 2026-08-13. Reader: phase3-refuter.
# Targets: position_P1.md (P1-1..16, SR-1..10, M-0..M-9, UD-1..6),
#          position_P2.md (P2-1..13, P2-16, P2-SR-1..10, P2-D1..D6),
#          position_P3.md (P3-1..30, SR-1..10, UD-1..8),
#          + the seven Phase-1 inventories (sampled adversarially).
# Method: every numbered proposal attacked on axes (a) loss risk,
# (b) migration hazard, (c) drift regrowth, (d) overengineering,
# (e) R1-R6/standing-directive conflict, (f) cross-position
# contradiction. Default = REFUTED unless it survived a genuine
# attack. All tree evidence below was MEASURED THIS SESSION on the
# live tree (commands quoted); verdicts S14-S25bis not re-litigated.
# Verdict vocabulary: REFUTED / REFUTED-AS-SPECIFIED (the load-bearing
# clause dies, the intent may survive re-formed) / WEAKENED (survives
# only with the named repair) / SURVIVES (attack ran, held).

---

## §0 GROUND-TRUTH MEASUREMENTS THAT OVERTURN SHARED PREMISES

All three positions (and parts of the Phase-1 inventories and the
session prompt's own diagnosis) share premises that are FALSE ON THE
TREE as measured 2026-08-13 during this refutation. These are not
matters of judgment; they are `git ls-files` / `ls` facts.

**GT-1 — The "all untracked single-copy" premise is false for the
session-log corpus and two prompts.**
Measured: `git ls-files validation/PROGRESS_*` returns **26 of the 27
session logs TRACKED** (S4..S25bis; e.g. PROGRESS_2026-07-16_S4_G5venue.md
was added in commit 0d00964, July window — tracked all along). Only
PROGRESS_2026-08-12_S24_f1b.md and the live S-ORDINE log are untracked.
Additionally `validation/ADVISORY_Scert_prompt_2026-08-12.md` is
TRACKED (committed at b2de54c, "[PIANO/R33] S-CERT session NAMED,
RATIFIED and PLACED... committed prompt") and
`validation/ADVISORY_Sordine_prompt_2026-08-12.md` is TRACKED.
Total tracked validation .md = 47; untracked = 41 (of 88 on disk).
The genuinely single-copy set is the ~32 advisory-class files
(AUDIT_agnostic, gap-map, panels, EQ-v2 pair, gauntlet, choking,
litmap, speed audit, topology census, S24 log...) + 25 gate .json +
24 .log + raws. Consequence: the risk MASS every position argues from
is materially smaller than claimed, and every stated verification
count in the migration steps is wrong (see REF-1).

**GT-2 — The Phase-1 universe is stale: ~57 substantive files are in
NO segment list, including an entire FOURTH literature root.**
Measured: `validation/*.md` on disk = **88**, segment lists sum to 82.
The six unlisted: ADVISORY_litmap_extension_2026-08-13.md,
ADVISORY_litreview_confrontation_2026-08-13.md (172 KB, "VERDETTO DI
RECORD, giudice fuso, REVISIONE 3 — CONVERGENZA"),
ADVISORY_moc_zucrow_fidelity_2026-08-13.md (54 KB, campaign partially
closed with declared residues §7), ADVISORY_sota_definition_2026-08-13.md
(96 KB, judge-after-refuter v2), LEDGER_dubbi_moc_2026-08-13.md
(open-doubts ledger with states), PROGRESS_2026-08-13_Sordine.md (this
session's own log — expected). The first five are of-record-class
parallel-session artifacts landed today. Further:
`literature_review/` at REPO ROOT contains 25 paper PDFs +
INDEX.md + reports/ with 26 files (00_APPARATUS_BRIEF + 25 per-paper
INTEGRAL reading reports, the litreview advisory's own evidence base)
— and `grep -c literature_review authoritative_repo_files.txt` = **0**
(the 436-line authoritative list excludes the whole root).
Consequence: the "reconciliation at discrepancy 0" of Phase 1 is
against an incomplete universe; the 4-ter nothing-lost gate as
currently fed would certify zero-loss while ~57 files (several
of-record, several single-copy) are unaccounted. This is exactly the
failure mode the gate exists to catch — the canary tests the
detector, not the universe.

**GT-3 — P1's highest-priority "UNRESOLVED" item is resolved on the
tree.** Measured: commits 8046434 ("diff-convergence repairs,
RECORD-PATH half... R9 stage_derive re-run EXIT 0... [X-DEFTW]
UNBLOCKED; R8 NEW MACHINE CHANNEL in group (xix)"), 7fb0f0c
("diff-convergence CLOSED... registry 20 entries... SESSION S25-bis
FULLY CLOSED"), a021fdd (post-repair gate artifacts) all landed AFTER
ea8143c and BEFORE this session. `tests/test_findings_registry.py`
lines 188-235 carry `derive_code_identity()` + the doctored-code_id
seeded rejector (the R8 channel, live). findings_registry row
`persistence:derive-artifact-intra-commit-staleness` = DISCHARGED with
the full evidence chain (verified in the registry read; 20 entries).

---

## §1 REFUTATION VERDICTS (REF-n, with target proposal ids)

**REF-1 [targets: P1 M-0, P2 STEP-0, P3-18; premise layer of P1 UD-1,
P2-D1, P3 UD-1] — REFUTED-AS-SPECIFIED (axis a/b + measured).**
Every stated verification arithmetic is wrong on the real tree:
P1 M-0 "count committed == count on disk (82)" — disk is 88 and 47
are already tracked; P3-18 "file count in commit == 34 advisory-class
+ 27 logs + 21 other + 17+N raws + 25 json" — 26 logs and 2 prompts
are already in git, `git status` shows 75 untracked paths total;
P2 STEP-0 "file count added == the untracked count from the fresh
diagnosis" — the fresh diagnosis itself is stale (GT-1/GT-2).
The COMMIT RECOMMENDATION ITSELF (UD-1 = YES) SURVIVES — the ~32
advisory-class files carrying the audit/gap-map/EQ-v2/census corpus
ARE untracked single-copy and the durability argument holds for them
— but the step must derive its add-list and its verification counts
from `git status --porcelain` + a fresh `ls` AT EXECUTION TIME, never
from any position's numbers. Any judge plan that copies the 82/27/34
numbers forward inherits a false nothing-lost baseline.

**REF-2 [targets: P1-3, P1-11, M-1; P2-8, STEP-1; P3-11, P3-19] —
REFUTED-AS-SPECIFIED on the count clause; index design itself
SURVIVES.** "Row count == 82 + raws dirs" (P1 M-1), "82 + raws
subdirs, reconciled to discrepancy 0 against ls" (P2 STEP-1), "row
count == ls validation -Recurse count" seeded from the inventories
(P3-19): the inventories cover 82 of 88; an index generated from them
either fails its own bijection lint at birth (best case) or is
reconciled against the stale list and silently omits six files
(worst case — among them four of-record advisories and an open-doubts
ledger). REQUIRED REPAIR before M-1/STEP-1: regenerate the
authoritative file list, run a supplementary Phase-1 reader pass over
the five 2026-08-13 files + `literature_review/` (INDEX + 26 reports
+ 25 PDFs), and only then build the index. This is a hard
precondition, not a nicety: the index is the destination map of the
4-ter gate.

**REF-3 [targets: P1-10, M-5; P2-11, STEP-3; P3-12, P3-23] —
REFUTED-AS-SOURCED.** All three seed the literature registry
exclusively from seg7 (137 files, three roots, "discrepancy 0").
Measured: a FOURTH root exists (`literature_review/`, 25 PDFs + 25
integral per-paper reports + INDEX.md). Concrete falsifications of
seg7-derived seed rows:
(i) seg7 duty 4: "Wolanski PCI 2013: research-grade read never done —
register READ-PARTIAL with owner" — `literature_review/reports/
wolanski_2013_survey.md` is a 2026-08-13 integral report;
(ii) WANTED rows: Ancourt 2023 is ON DISK
(`literature_review/ancourt_2023_adjoint_direct_characteristic_
equations.pdf`); Kraiko-Tillyaeva 2004/2015/2016 and Teasley 2023/2025
are ON DISK; the WANTED list of P1-10/P2-11/P3-23 is stale;
(iii) seg7 "no paper PDF duplicated across the three roots" — true
only in stale scope: harroun_2021, kaemming_paxson_2018,
paxson_miki_2022, wintenberger_shepherd, wolanski are duplicated
between PARENT/ and literature_review/;
(iv) the per-paper reports are precisely the "where-analyzed" anchors
the registry schema demands — omitting them produces a registry that
is born wrong on read-status AND misses its best anchor corpus.
The registry design (schema, honesty enum, lints) SURVIVES; the seed
source must be seg7 + the litreview corpus + the two new lit
advisories, with a re-run dedup pass across FOUR roots.

**REF-4 [target: P1 UD-6] — REFUTED BY THE TREE (GT-3).** The
repair-list execution status is not an open user decision: R1-R13
executed (8046434), derive re-run byte-identical (R9), R8 channel
live in group (xix), [X-DEFTW] UNBLOCKED, registry row DISCHARGED,
session "FULLY CLOSED" (7fb0f0c). P2 Appendix-A row 1 and P3-21's
verify-first instruction are CONFIRMED-correct. UD-6 must be dropped
from the judge's open-decision list (carrying it would re-litigate a
closed verdict, TERMS violation); the only residue is nothing.

**REF-5 [targets: P1 M-3; interacts with P2-13, P3-2] — WEAKENED
(axis a/b).** P1's physical-archive move of 8 files verifies anchors
by grepping "docs/*.yaml + docs/*.md + validation/*.md" — the scope
omits (i) memory/ (the POST-S20 inline MEMORY.md entry cites
ADVISORY_plan_v2_draft by name; topology-census-pins bridges to the
panel path; no lint reaches memory), and (ii) parent-dir prose.
A move that passes P1's own check still strands memory-side pointers
silently. Also archived paths remain cited inside of-record verdict
files (Scollapse verdict REFS cite the Scollapse prompt path);
"updating" those citations means editing verdict documents — churn on
frozen text. P3-2 (banner-in-place default, physical archive only for
the zero-inbound-anchor set after a basename grep whose scope
includes EVERYTHING) SURVIVES and should win; P2-13 SURVIVES as the
compatible middle. If the judge keeps any physical move, the anchor
grep scope MUST include memory/ and the parent .md prose.

**REF-6 [target: P2-SR-3 as a lint inside group (xx)] —
REFUTED-AS-PLACED (axis c/e).** A suite lint "OF-RECORD must be
git-tracked" fails EVERY mid-session suite run between a parallel
session landing an advisory and the owning session's R3 close — and
the suite is run mid-session as a gate consumer (S25-bis practice:
gates re-run after every repair). The rule would make gate outcomes
red for reasons unrelated to the gated change, corroding the
exit-code discipline (R6). Correct placement is the R3 CLOSURE
checklist with a declared pending-commit escape: exactly P1 SR-6
("or explicitly listed in the session log as pending-commit with
reason") and P3 SR-8 (closure `git status` check). Judge adopts
those; P2-SR-3's DECLARED-INACTIVE fallback wording survives.

**REF-7 [targets: P2-8 and P3-11 recursive per-file coverage of raws
dirs; conflicts with P1-3 block rows] — REFUTED-AS-SPECIFIED for the
raws clause (axis c).** Measured: sordine_raws_2026-08-13/ grew to 20
files DURING this session (inventories, positions, this file).
Per-file index rows for raws force an index edit for every agent
artifact — "artefatti su file SUBITO" (standing orchestration rule)
would make the coverage lint red mid-orchestration, or worse, train
sessions to batch-index raws ritually. P1-3's block-row-per-raws-dir
design SURVIVES and must win. (Everything else in P2-8/P3-11
survives; see REF-20 for the ORPHAN clause.)

**REF-8 [targets: P1-5 note + P2 STEP-4(iv); inherited from seg1] —
WEAKENED (measured).** The claim "S1-S13 LOG entries are
at-risk-unique (no validation/ log exists for them)" is false:
tracked validation logs exist from 2026-07-16 (sessions S3/S4
onward — S4_G5venue, fase0, fase1 S5/S7/S8, rigore S6/S8, S9..S13),
and they are IN GIT. The genuinely single-home content is the S1-S2
entries plus per-entry narrative deltas. The archive move remains
right; the at-risk WEIGHTING (and the loss-hunter's sampling
priorities) must be corrected, or the 4-ter ledger overstates risk
where there is none and dilutes attention from the real single-copy
mass (advisory corpus + gate json).

**REF-9 [target: P2 STEP-4(ii); interacts with P3-24(ii), P1 M-7(b)]
— REFUTED as a nothing-lost verification (axis a).**
"chars(slim) + chars(archive) >= chars(original)" is satisfiable
while dropping arbitrary lines (banner text inflates chars). P3-24's
byte-diff "spot check on 3 random blocks" samples, it does not
verify. The only mechanical form that proves the archive claim is a
line-multiset difference: every line removed from PROGRESS.md appears
verbatim in the ARCHIVE (old_lines ⊆ live_lines ∪ archive_lines,
with counted exceptions = the new table/banner lines, reconciled to
0). P1 M-7(b) states essentially this — judge adopts P1's form as THE
check for both PROGRESS and any future archive move.

**REF-10 [target: P1 M-8] — WEAKENED (arithmetic).** After P1-6(d)
types the two inline entries into files, backing files = 38, not 36;
"MEMORY.md index lines == memory files (36)" would fail its own
verification. Recompute at execution; P2 STEP-5's "37+2 accounted" is
directionally right. Trivial but it is a stated gate number.

**REF-11 [targets: P1-12, P2-10, P3-13 glossary lint scope] —
WEAKENED (axis c/d).** None of the three scopes covers newly-written
advisories at write time (P1: docs OF-RECORD + index rows; P3: typed
artifacts + docs status blocks, ratcheted; P2: "the OF-RECORD doc
set", vaguest). Therefore the glossary lint does NOT stop advisory
re-minting — the demonstrator (throat-panel) class is covered by the
(xix) dedup clause, not by token resolution. Any judge wording that
sells the glossary as anti-re-mint machinery overclaims. P3-13's
ratcheted-baseline design is the only one that can later widen scope
without a permanently red lint — adopt it, and state the payoff
honestly: collision disambiguation + navigation, not re-mint
prevention. (The namespace-collision need itself is real and
measured: O5, M1, T2, F4, C1, L4, U1, A1 all multi-meaning across
segments.)

**REF-12 [targets: P2-D3; P1 UD-2; P3 UD-3] — P2-D3
REFUTED-AS-WORDED (axis e).** The session contract TERMS are
categorical: "R4: mai cancellare, solo archiviare con banner+indice".
An S-ORDINE deliverable that RECOMMENDS deletion (even of
byte-verified debris, even user-approved) puts the judge's plan in
direct letter-conflict with its own contract. The honest form is
P3 UD-3's: verification first, then a REGISTERED user decision with
default = leave-in-place/archive; the deletion itself, if the user
orders it, happens outside S-ORDINE's action set and is recorded.
P1 UD-2's default ("archive everything, delete nothing") SURVIVES;
its "deletion is legitimate" sentence should be dropped by the judge.

**REF-13 [target: P2 STEP-5/D-4 tracked mirror of memory verbatim
orders] — WEAKENED (axis c/f).** A living mirror of the memory
corpus inside the repo is a second source of truth that WILL drift
(memory files are updated by the harness every session; the mirror is
updated by discipline). P2's own right-sizing §7 rejects exactly this
duplication class ("two-sources-of-truth entropy"). Acceptable only
as a DATED SNAPSHOT with a non-authority banner ("memory wins; this
is a durability copy of the verbatim orders as of <date>"), refreshed
only by explicit decision — or refused. Judge must pick the snapshot
semantic explicitly if D-4 is accepted.

**REF-14 [target: P1 M-0 degraded mode (tar/zip snapshot in the
parent dir)] — REFUTED (axis a/e/f).** If UD-1 is refused, P1 writes
a tarball OUTSIDE the repo: an untracked single copy of the single
copies, same failure class as the risk it mitigates, in a directory
P3-7/UD-8 declares outside jurisdiction ("the repo cannot durably
protect files it does not contain"), and P2's own fallback analysis
calls the off-repo backup "strictly weaker". The honest degraded mode
is P3-18's: skip, tag the set UNTRACKED-SINGLE-COPY in the index, and
leave the risk priced and owned by the user's decision.

**REF-15 [targets: P1-9/P1-10/P1-11/P1-12/P1-13 vs P2-8..12 vs
P3-11..16 — suite group NUMBERING] — CONFLICT, judge must pin
(CF-2).** The three positions assign (xx)-(xxiv) to five different
group maps (P1: xx=choice, xxi=lit, xxii=index, xxiii=glossary,
xxiv=flags; P2: xx=index, xxi=anchors, xxii=glossary+flags, xxiii=lit,
xxiv=choice; P3: xx=index+supersession, xxi=lit, xxii=glossary,
choice/flags folded). Group numbers are load-bearing in commit
messages and session logs (the corpus cites "(xix)" as an identity).
One map must be pinned in the judge's plan before any test file is
written. On fold-vs-new-groups (P3-15/16 vs P1-9/P2-12): folding
SURVIVES on runner-sprawl grounds with one caveat — the (xix)
anti-re-mint span rule does not apply to choice rows without code
spans; folding is file-level convenience, the schemas stay distinct.

**REF-16 [targets: P1-13, P3-16, P2-10 flag-registry bijection] —
SURVIVES with one repair.** A bare `grep -o "A1_[A-Z_]*"` census over
validation/*.py + tests/ will hit flag NAMES in strings/docstrings
and reporting code (engine_speed_bench prints flag attributions),
making "row without a flag in code = FAIL" unfalsifiable and "flag
without row" over-inclusive. Pin the census pattern to actual reads
(`os.environ.get("A1_...`/`os.getenv`) OR declare string mentions
in-scope explicitly. Otherwise the lint ships with an undeclared
false-positive class — against P3's own R5 bar for lints.

**REF-17 [targets: P1-2, P2-2, P3-1 target trees] — SURVIVE
(convergent, minimal-move, priced); naming conflicts for the judge
(CF-3):** glossary.md (P1) vs glossary.yaml (P2/P3);
flag_registry.yaml (P1/P3) vs flags_registry.yaml (P2, optionally
folded into glossary.yaml). Trivial but must be pinned once — two
names for one registry is self-inflicted entropy.

**REF-18 [targets: P1-7, P2-5, P3-8 status taxonomy] — no kill;
CONFLICT the judge must merge to ONE enum (CF-4).** Divergences that
matter: (i) UNRESOLVED exists only in P1 — and is NEEDED (ADR panel
ratification is a real, verified in-file open state; forcing it into
CONSUMED-or-PENDING lies); (ii) LECTURE-ERA is a status in P2 but a
qualifier in P1/P3 (qualifier is right — those files are also
OF-RECORD); (iii) CONSUMED-with-residue exists in P2/P3 but not P1's
core set (P1 handles via per-row maps — fine, but the enum value is
the machine-visible form). A merged enum must carry all three
capabilities or an honest state gets forced into a wrong bucket —
which is precisely a nothing-lost failure at the semantic level.

**REF-19 [targets: P1-1, P2-1, P3-4 SCAFFOLD amendment] — SURVIVES.**
Convergent across all three, evidence-backed (F-SEG1-3 verified:
SCAFFOLD exists, 216 lines, migration-with-acceptance precedent).
Attack attempted on "amendment vs new doc" (could the amendment bloat
SCAFFOLD?): the amendment is bounded (§6, layer list + registry map);
no kill.

**REF-20 [targets: P1-3 plan-anchor column, P2-3, P3-3; P2-8 ORPHAN
clause] — design SURVIVES; P2-8's ORPHAN wording REFUTED-AS-SPECIFIED
(axis c).** P2-8 says plan-anchor non-empty "or the row is explicitly
flagged ORPHAN (a visible state, not a pass)" — if ORPHAN rows fail
the lint, the four verified root orphans (er.name, t-file, parent
hash lists) keep the suite red until a user disposition that is
explicitly out of agent hands → a lint nobody can keep green =
entropy by P3's own bar. P3-11(e)'s form (ORPHAN-FLAGGED = visible,
COUNTED, reported; failure only on NEW unflagged orphans — a ratchet)
is the correct mechanization of "loud, never silent" and must win.

**REF-21 [target: P2-7 per-row consumption maps] — SURVIVES (honest,
needed for claims_to_code/engine_speed_audit/redteam residues);
priced warning: after audit-94 seeding this is the largest hidden
workload in the plan; if deferred it must be a NAMED tranche with
counts (never-postpone-resolvables), and the judge should say so.**

**REF-22 [target: P2-9 anchor-resolution lint] — SURVIVES; strongest
single lint proposed (it is the durable half of 4-ter). One repair:
`#section` fragments in existing registry rows are prose headings
("#THE MERGED SLIVER ROW", "#M6", "#STEP 13" — verified in
findings_registry.yaml); the lint must define fragment resolution as
normalized substring grep in the target, and that convention must be
written into the lint docstring, else the first run either
false-fails half the registry or silently skips fragments.**

**REF-23 [target: P2-16 GENO .gitignore + explicit-pathspec rule] —
SURVIVES; REQUIRED precondition of any snapshot commit; no position
opposes; cheapest risk-kill in the whole plan.**

**REF-24 [targets: standing-rule sets P1 SR-1..10, P2-SR-1..10,
P3 SR-1..10] — SURVIVE as a family, with the placements already
adjudicated above (REF-6 tracked-check to closure; REF-7 raws block
rows; REF-11 glossary scope).** Residual notes: P1 SR-7 / P3 SR-5
census-single-table lint must scope to PROGRESS.md only (the ARCHIVE
legitimately contains many CENSIMENTO headers) — both already do,
keep it that way. P3 SR-9's honesty (checklist-only, no token lint)
is the correct form; P1 SR-9's "closure violation" wording is
compatible. P3 SR-10 (carrier-touch discipline) SURVIVES and is the
only rule that addresses the measured line-anchor fragility (0.2(3));
adopt verbatim.

**REF-25 [targets: P3-9, P3-13 ratcheted baselines] — SURVIVE
(R28-pattern precedent, the only lint form that tolerates legacy
corpus without lying).**

**REF-26 [target: P1-14 supersession lint, unratcheted] — WEAKENED
(axis c).** P1-14 greps docs/ + validation/ OF-RECORD for SUPERSED*
markers requiring date+pointer with NO legacy baseline; seg1 verified
the convention is "applied consistently" only on the files it
sampled — nobody has verified that EVERY historical marker parses.
Without a frozen baseline the lint is red at birth or forces edits to
frozen text. Adopt P3-9's ratcheted form (baseline == reality,
growth forbidden, normalize down); P1-14's reciprocity check
(P1-8(e)) survives and folds in.

**REF-27 [targets: P1 UD-4, P2 parent rescues in STEP 2/3, P3 UD-8]
— CONFLICT (CF-8), middle ground survives.** P2 executes parent-root
rescues as ordinary plan steps; P3 gates ALL parent-scope action on
user OK. Distinguish: COPYING a parent file INTO the repo (brick2
png, VALIDATION.md §3 notes into registry fields) modifies nothing
outside the repo — read-only stance preserved, no user gate strictly
needed beyond the plan's ratification; MOVING/DISPOSING parent files
(hash lists, SDToolbox relocation) touches parent state = user-gated
(P3 right). Judge should split the rescue list along exactly that
line instead of adopting either extreme.

**REF-28 [target: P2 Appendix A at-risk table] — WEAKENED
(measured).** Row 7 ("S-CERT contract... untracked prompt") — FALSE,
tracked at b2de54c. Row 9 ("27 session logs... untracked") — FALSE
for 26/27 (GT-1). Row 1 — verified CORRECT (and now discharged,
GT-3). The table is the seed of the STEP-7 destination map: it must
be regenerated from `git ls-files` truth before the 4-ter gate runs,
or the gate protects phantom risks while under-weighting the real
single-copy mass (advisory corpus + gate json + the six NEW unlisted
files, which appear in NO position's ledger at all).

**REF-29 [targets: P1-15, P3-17 session-scoped 4-ter gate; P2 STEP 7]
— design SURVIVES (right-sized, convergent: no permanent loss-hunter
in the suite; P2-9 is the durable residue). HARD PRECONDITION added
by GT-2: the gate must not run until the coverage repair of REF-2
lands. A seeded canary proves the detector fires; it proves nothing
about universe completeness. The reconciliation input must be the
REGENERATED file list (which will exceed 436) + FOUR literature
roots, and the delta vs the prompt's 428/436 must be reconciled BY
NAME per the gate's own both-directions rule.**

**REF-30 [targets: right-sizing lists P1 §7, P2 §7/P2-20, P3-30] —
SURVIVE.** Attacks attempted: (i) "no log archival" (P1) vs P2-D2
commit-the-cited-subset — compatible (tracking ≠ moving); (ii) "no
CI" registration — all three register with owner, consistent with
never-postpone (structurally gated, named trigger); (iii) P3's hard
cap ~3 new test modules — survives, it is the anti-sprawl budget the
runner needs. No kills.

**REF-31 [targets: P1-16, P2's no-yaml-ification, P3-30.4] —
SURVIVE (convergent; the registries index prose, never replace it —
consistent with the SCAFFOLD conflict rule).**

**REF-32 [targets: P1-8, P2-6, P3-10 supersession/status discipline]
— SURVIVE; one merge note: P3-10 pins "index authoritative for
STATUS, file for CONTENT" while P2-6 pins "banner and index redundant
by design + lint checks agreement". Adopt both (agreement lint +
declared tie-break) — without the tie-break the first banner/index
disagreement is an unadjudicable lint failure.**

**REF-33 [targets: P1-6, P2 STEP 5, P3-6, P3-26 memory sweep] —
SURVIVE (spot-verified: MEMORY.md line 1 stale numpy pin confirmed;
[[s24-deftw]] and [[s24-*]] broken links confirmed on disk; the
routing-half banner design respects R4).** One count repair per
REF-10.

**REF-34 [targets: P1 UD-3, P3 UD-5 (ADR panel)] — SURVIVE
(spot-verified: the file header says "NOT YET RATIFIED" and carries
">>> OPEN QUESTION FOR USER" with the 242.5/245.3 and trunc-default
calls, exactly as seg3 reported). It is a genuine pending user
decision; the UNRESOLVED status value (REF-18) is its home.**

**REF-35 [targets: P1 UD-5, P2-D6, P3 UD-6 README pointer; P2-D2/P3
UD-2 log tracking] — SURVIVE (cheap, user-ratified, no attack
found beyond noting the three M6 probe logs' evidence-pointer check
(seg5 §F) must precede any log disposition — all positions carry
it).**

---

## §2 CROSS-POSITION CONFLICTS THE JUDGE MUST ADJUDICATE (CF-n)

- **CF-1 (archive default):** P1 M-3 physically moves 8 files; P2-13
  moves only zero-inbound-anchor files; P3-2 defaults to
  banner-in-place, archive/ only on explicit preference. Refuter
  weight: P3-2 (REF-5) — with the grep scope extended to memory/.
- **CF-2 (lint group numbering):** three incompatible (xx)-(xxiv)
  maps (REF-15). Pin one before any code.
- **CF-3 (artifact naming):** glossary.md vs glossary.yaml;
  flag_registry vs flags_registry vs folded-into-glossary (REF-17).
- **CF-4 (status enum):** UNRESOLVED (P1-only, needed);
  LECTURE-ERA status (P2) vs qualifier (P1/P3, right);
  CONSUMED-with-residue (P2/P3) absent from P1 core (REF-18).
- **CF-5 (raws indexing):** block rows (P1) vs per-file recursive
  (P2/P3). Refuter weight: P1 (REF-7).
- **CF-6 (tracked-check placement):** suite lint (P2-SR-3) vs
  closure checklist (P1 SR-6/P3 SR-8). Refuter weight: closure
  (REF-6).
- **CF-7 (INDEX.md):** merge into ADVISORY_INDEX (P2 floats) vs keep
  separate (P1/P3). Low stakes; keeping avoids touching an existing
  living doc — refuter leans keep.
- **CF-8 (parent rescues):** plan steps (P2) vs user-gated (P3).
  Split copy-in vs move/dispose (REF-27).
- **CF-9 (deletion):** P2-D3 recommends deletes; contract TERMS say
  never inside S-ORDINE (REF-12).
- **CF-10 (literature read-status enum):** P1 has TRIAGED; P2/P3
  four values. seg7 uses "READ-PARTIAL (triaged)" — either encode
  TRIAGED or define the mapping; do not let two enums coexist.
- **CF-11 (choice/flag lints):** own groups (P1/P2) vs folded
  (P3). Either; pin one (REF-15).
- **CF-12 (S25bis repair status):** P1 UD-6 "UNRESOLVED,
  highest-priority" vs P2/P3 "verified discharged" — resolved by
  tree evidence in favor of P2/P3 (REF-4/GT-3).
- **CF-13 (M-0 fallback):** parent-dir tarball (P1) vs no-outside
  action (P3). Refuter: P3 (REF-14).
- **CF-14 (memory mirror):** P2 D-4 tracked mirror vs
  anti-duplication right-sizing (P2's own §7, P3-30.4). Snapshot
  semantic or refusal (REF-13).

---

## §3 INVENTORY ATTACK (sampling + tree checks; per brief, >=5 files
## across segments checked against originals)

Samples verified against originals this session:
1. `er.name` vs `t --count HEAD:q` — md5 6de03c69... BOTH:
   byte-identical, seg2's claim CONFIRMED.
2. `PARENT/hr.txt` vs `PARENT/harroun.txt` — md5 782a3f45... both:
   seg7's dedup claim CONFIRMED.
3. `docs/roadmap_geno_rde.md` head — no supersession banner, presents
   itself as "Third document of the set": seg1 F-SEG1-1 CONFIRMED.
4. `validation/ADR_panel_2026-07-16.md` — "(NOT YET RATIFIED)" in the
   title line + ">>> OPEN QUESTION FOR USER" at L64: seg3 CONFIRMED.
5. `MEMORY.md` line 1 ("numpy must be pinned to 2.2.6") + broken
   links [[s24-deftw]] / [[s24-*]]: seg6 F1/F3 CONFIRMED.
6. `docs/rde_nozzle_SCAFFOLD.md` = 216 lines; PROGRESS = 2498;
   findings_registry = 20 entries: seg1 counts CONFIRMED.
7. validation counts: 33 .py / 25 .json / 24 .log / 18 .pyc /
   17 gapmap-raws CONFIRMED; **.md = 88, NOT 82** (GT-2).

Inventory FINDINGS (misclassifications / stale claims):
- **INV-1 (seg5, HIGH):** "ALL 27 [session logs] ARE UNTRACKED
  (single-copy, zero git history)" — FALSE for 26/27 (GT-1, measured
  `git ls-files`). The whole durability framing of seg5 §A, and
  every downstream consumer of it (P2 §0, P2 App-A row 9, P3-18
  arithmetic, the prompt's own §2(b)), inherits the error.
- **INV-2 (seg3, MEDIUM):** file 13 (Scert prompt) "single-copy
  untracked contract" and the segment-wide "every file is UNTRACKED
  single-copy... applies to ALL 17" — FALSE for the Scert prompt
  (tracked, b2de54c). 16/17 claim would have been correct.
- **INV-3 (all segments + master list, HIGH):** the Phase-1 universe
  omits 6 on-disk validation .md and the entire literature_review/
  root (~52 files) — GT-2. "COVERAGE = THE WHOLE TREE, NESSUN FILE
  ESCLUSO" is not met; every "discrepancy 0" reconciliation is
  against a stale list.
- **INV-4 (seg1, MEDIUM):** "S1-S13 LOG entries not duplicated in
  validation/ logs, which start S14-era" — FALSE: tracked logs exist
  from 2026-07-16 covering S3/S4 onward (REF-8). Also seg1's own
  at-risk recount is self-contradictory ("39 of 43... FINAL: 41
  at-risk / 2 none-material") — the 4-ter ledger feed needs one
  number, recount at consolidation.
- **INV-5 (seg7, MEDIUM):** three-root scope stale w.r.t. the
  fourth root; WANTED list (Ancourt, Tillyaeva-adjacent, Teasley)
  and the Wolanski "never research-read" duty falsified by files on
  disk (REF-3). Credit: seg7 itself flagged the project_build/specs
  coverage gap honestly (duty 7) — the same class of gap it missed
  for literature_review/.
- **INV-6 (context for fairness):** on CONTENT the sampled inventory
  rows are accurate (7/7 content spot-checks confirmed); the failure
  class is uniformly TRACKING-STATUS and UNIVERSE-SCOPE — facts that
  were checkable with one `git ls-files` and one fresh `ls`, and
  were instead inherited from the prompt's 2026-08-12 diagnosis.
  Lesson for the standing rules: any de-entropy artifact that states
  a tracking or count claim must cite the command output, not a
  prior document (this is R5 applied to meta-claims).

---

## §4 COVERAGE TABLE (every numbered proposal -> verdict)

P1: P1-1 SURVIVES (REF-19) | P1-2 SURVIVES (REF-17) | P1-3 SURVIVES,
count clause REFUTED-AS-SPECIFIED (REF-2), raws block-row wins REF-7 |
P1-4 SURVIVES (REF-20) | P1-5 SURVIVES, S1-S13 note WEAKENED (REF-8),
fold-check adopted (REF-9) | P1-6 SURVIVES (REF-33) | P1-7 merge
needed (REF-18) | P1-8 SURVIVES (REF-32) | P1-9 SURVIVES, numbering
CF-2 (REF-15) | P1-10 REFUTED-AS-SOURCED (REF-3) | P1-11
count clause REFUTED-AS-SPECIFIED (REF-2) | P1-12 WEAKENED scope
(REF-11) | P1-13 SURVIVES w/ repair (REF-16) | P1-14 WEAKENED, adopt
ratchet (REF-26) | P1-15 SURVIVES w/ precondition (REF-29) | P1-16
SURVIVES (REF-31).
P1 SR-1..SR-10: SURVIVE (REF-24; SR-6 wins CF-6).
P1 M-0 REFUTED-AS-SPECIFIED + fallback REFUTED (REF-1, REF-14) |
M-1 count REFUTED-AS-SPECIFIED (REF-2) | M-2 SURVIVES | M-3 WEAKENED
(REF-5) | M-4 SURVIVES (REF-15/16) | M-5 REFUTED-AS-SOURCED (REF-3) |
M-6 SURVIVES (tranche discipline honest) | M-7 SURVIVES, its (b) is
the adopted check (REF-9) | M-8 WEAKENED arithmetic (REF-10) | M-9
SURVIVES w/ REF-29 precondition.
P1 UD-1 SURVIVES re-scoped (REF-1) | UD-2 SURVIVES minus the
delete-legitimacy sentence (REF-12) | UD-3 SURVIVES (REF-34) | UD-4
SURVIVES (REF-27) | UD-5 SURVIVES (REF-35) | UD-6 REFUTED BY TREE
(REF-4).

P2: P2-1 SURVIVES (REF-19) | P2-2 SURVIVES (REF-17) | P2-3 SURVIVES
(REF-20) | P2-4 SURVIVES (qualifier form, REF-18) | P2-5 merge
needed (REF-18) | P2-6 SURVIVES (REF-32) | P2-7 SURVIVES w/ price
warning (REF-21) | P2-8 count + ORPHAN + raws clauses
REFUTED-AS-SPECIFIED (REF-2/20/7), rest survives | P2-9 SURVIVES w/
fragment convention (REF-22) | P2-10 WEAKENED scope (REF-11), flag
census repair (REF-16) | P2-11 REFUTED-AS-SOURCED (REF-3) | P2-12
SURVIVES (REF-15) | P2-13 SURVIVES (REF-5) | P2-16 SURVIVES,
mandatory (REF-23).
P2-SR-1/2/4/5/6/7/9/10 SURVIVE (REF-24) | P2-SR-3
REFUTED-AS-PLACED (REF-6) | P2-SR-8 SURVIVES (honest checklist).
P2 STEP-0 counts REFUTED-AS-SPECIFIED (REF-1) | STEP-1 count
REFUTED-AS-SPECIFIED (REF-2) | STEP-2 SURVIVES (tranche counts) |
STEP-3 REFUTED-AS-SOURCED (REF-3) | STEP-4 (ii) REFUTED (REF-9),
(iv) WEAKENED (REF-8), rest survives | STEP-5 SURVIVES, D-4 mirror
WEAKENED (REF-13), count REF-10-adjacent | STEP-6 SURVIVES (REF-5
scope repair) | STEP-7 SURVIVES w/ REF-29 precondition + REF-28
regeneration.
P2-D1 SURVIVES re-scoped (REF-1) | D2 SURVIVES (REF-35) | D3
REFUTED-AS-WORDED (REF-12) | D4 mirror-half WEAKENED (REF-13),
rescue-half split per REF-27 | D5 SURVIVES (diff-first, honest) |
D6 SURVIVES (REF-35). Appendix A rows 7/9 FALSE, row 1 verified
(REF-28); Appendix B SURVIVES (registered fuori-scope).

P3: P3-1 SURVIVES (REF-17) | P3-2 SURVIVES, wins CF-1 (REF-5) |
P3-3 SURVIVES (REF-20) | P3-4 SURVIVES (REF-19) | P3-5 SURVIVES |
P3-6 SURVIVES (REF-33) | P3-7 SURVIVES, wins CF-13 (REF-14) | P3-8
merge needed (REF-18) | P3-9 SURVIVES (REF-25/26) | P3-10 SURVIVES
w/ tie-break note (REF-32) | P3-11 raws + count clauses
REFUTED-AS-SPECIFIED (REF-7/2), ORPHAN-ratchet clause WINS (REF-20) |
P3-12 REFUTED-AS-SOURCED (REF-3) | P3-13 SURVIVES, adopted scope
(REF-11) | P3-14 SURVIVES | P3-15 SURVIVES (REF-15 caveat) | P3-16
SURVIVES w/ repair (REF-16) | P3-17 SURVIVES w/ precondition
(REF-29) | P3-18 counts REFUTED-AS-SPECIFIED (REF-1), degraded mode
WINS (REF-14) | P3-19 count REFUTED-AS-SPECIFIED (REF-2) | P3-20
SURVIVES | P3-21 SURVIVES — its verify-first instruction CONFIRMED
executed (REF-4) | P3-22 SURVIVES (45-count verified vs seg3) |
P3-23 REFUTED-AS-SOURCED (REF-3) | P3-24 SURVIVES, (ii) upgraded per
REF-9 | P3-25 SURVIVES | P3-26 SURVIVES (REF-33) | P3-27 SURVIVES w/
REF-29 precondition + REF-12 deletion gate | P3-28 SURVIVES
(REF-24) | P3-29 SURVIVES (REF-34 et al.) | P3-30 SURVIVES (REF-30).
P3 SR-1..SR-10 SURVIVE (REF-24; SR-8 wins CF-6; SR-10 adopt
verbatim).
P3 UD-1 SURVIVES re-scoped (REF-1) | UD-2 SURVIVES (REF-35) | UD-3
SURVIVES as conditional (REF-12) | UD-4 SURVIVES (CF-1 winner) |
UD-5 SURVIVES (REF-34) | UD-6 SURVIVES (REF-35) | UD-7 SURVIVES |
UD-8 SURVIVES split per REF-27.

---

## §5 SUMMARY FOR THE JUDGE

- Proposals attacked: 120 (P1: 42; P2: 30 + 8 steps; P3: 48 — every
  numbered id covered in §4).
- REFUTED or REFUTED-AS-SPECIFIED (proposal or load-bearing clause):
  18 — P1 M-0(+fallback), M-1-count, M-3-scope→weakened*, M-5, P1-10,
  P1-11-count, P1-14→weakened*, UD-6; P2-SR-3, P2-8 (three clauses),
  P2-11, STEP-0, STEP-1, STEP-3, STEP-4(ii), P2-D3, App-A rows;
  P3-11 (two clauses), P3-12, P3-18-counts, P3-19-count, P3-23.
  (*items marked weakened in §4 are counted only where a stated
  gate/verification clause dies, not the intent.)
- WEAKENED with named repair: 8 (REF-5, 8, 10, 11, 13, 16, 26, 28).
- Cross-position conflicts named: 14 (CF-1..CF-14).
- Inventory findings: 5 substantive (INV-1..INV-5) + 7/7 content
  spot-checks confirmed (INV-6).
- HARD PRECONDITIONS the converged plan must carry, in order:
  (1) regenerate the authoritative file list + supplementary reader
  pass over literature_review/ and the five 2026-08-13 files
  (REF-2/GT-2) — before index, registries, or any gate;
  (2) re-derive all tracking/count baselines from git at execution
  time (REF-1/GT-1);
  (3) drop UD-6, record the discharged state (REF-4/GT-3);
  (4) GENO ignore + explicit pathspec before any commit (REF-23);
  (5) 4-ter gate runs only after (1) (REF-29).
- The three positions CONVERGE (and the refuter could not kill):
  SCAFFOLD amendment not fork; index-not-move; plan-anchor column
  with loud-ratcheted ORPHAN; typed registries as indexes over prose;
  ratcheted lints with seeded rejectors; banner-based supersession;
  R3-closure education; right-sizing exclusion lists. That core is
  sound. What was uniformly missing is the discipline the corpus
  itself preaches: MEASURE the tree before stating it (R5 applied to
  the de-entropy session's own claims).

END OF REFUTATION — phase3-refuter, 2026-08-13.
