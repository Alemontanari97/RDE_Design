# RED-TEAM (Form-3) ON THE S-ORDINE PHASE-4 JUDGE — BEFORE ABSORPTION
# Date: 2026-08-13. Reader: phase5-redteam.
# Target: validation/ADVISORY_SORDINE_plan_2026-08-13.md (the fused judge).
# Inputs read FULL-TEXT: the judge advisory; position_P1.md / position_P2.md /
# position_P3.md; refutation.md; the session contract
# validation/ADVISORY_Sordine_prompt_2026-08-12.md. Spot-checks executed on
# the LIVE TREE this red-team pass (commands quoted per finding).
# Hunted failure modes (measured classes): judge-ADDED claims no position
# supports; manufactured unanimity; incomplete absorption of refutations;
# silent wording weakenings; header totals never reconciled with the body.
# Verdicts S14-S25bis are of record and were NOT re-litigated.

## VERDICT: ABSORB_WITH_REPAIRS (7 repairs: R-1..R-3 MEDIUM, R-4..R-7 LOW)

The plan is structurally sound: the convergent core is genuinely convergent,
the refutation is genuinely absorbed (all 5 hard preconditions carried, all
14 CFs pinned at real locations, every repair-bearing REF traced to its
absorption point), the contract is covered at the obligation level, and the
nothing-lost gate design has seeded rejectors that can actually fire. The
seven repairs below are count-declaration and pin-level defects — none
invalidates the plan's architecture; three of them are exactly the
stale-premise class the judge's own §9 finding and SR-12 exist to kill,
which is why they cannot ship uncorrected in a plan that mints that finding.

---

## §1 CHECK 1 — EVERY JUDGE CLAIM TRACES (result: PASS with 1 finding)

Method: every §0-§9 substantive claim traced to a position id / REF-n /
GT-n / inventory row, or verified as a declared judge-fresh measurement
re-executed by this red-team on the live tree.

Traced-and-verified highlights (no repair needed):
- §0.2 GT-3 block: commits 8046434 / 7fb0f0c / a021fdd exist on the tree
  with exactly the cited content ([X-DEFTW] UNBLOCKED, R8 channel in (xix),
  registry 20 entries, born-DISCHARGED row) — `git cat-file -t` + `git log`
  verified. Dropping P1 UD-6 is correct, not a silent drop: declared in §6
  preamble with reason (REF-4/GT-3).
- §0.2 GT-1 block: tracked validation .md = 47 (`git ls-files` measured 47);
  tracked PROGRESS_* logs = 26; ADVISORY_Scert_prompt tracked at b2de54c —
  all verified. On-disk .md = 89 today vs the judge's 88: the +1 IS the
  judge advisory itself, written after its own measurement — self-consistent
  with the plan's own "the CLOSING count is the one of record" clause.
- §0.2 GT-2 block: literature_review/ = 54 files (measured: 25 PDFs +
  reports/ 27 + INDEX.md + asset); repo total excl .git/GENO = 520 today vs
  518 at plan time (drift = the judge advisory + growth, declared handling
  at S0). The five 2026-08-13 advisories exist on disk. See R-7 for the one
  internal decomposition defect.
- §7/§9 registry citations: `structure:monolithic-driver-module`,
  `infra:scheduled-ci-multiplatform`,
  `persistence:derive-artifact-intra-commit-staleness` all present in the
  20-row registry (grep verified); NO existing row covers universe-staleness,
  so the §9 proposed row `process:inventory-universe-staleness` is
  dedup-clean and properly labeled as a PROPOSAL to be minted at S7 — a
  judge-added object, correctly declared as such, not a smuggled claim.
- S1 (GENO ignore): verified — .gitignore contains NO GENO line today; the
  step is real, not ritual.
- S9's list of 9 unmarked memories (s14, s15, s18, s19, s20, s21, s22, s24,
  s25): verbatim in seg6 inventory ("UNMARKED (routing half stale, no
  banner)") — judge-named but inventory-sourced, traces.
- S4's banner list "10 files, enumerated": recounted = 10 (roadmap + 6
  prompts + DISPATCH_Sspeed + plan_v2_draft + interface_audit). Note P3-20
  said "9 files" while enumerating the same 10 — the judge's silent
  arithmetic correction is RIGHT on the enumeration; acceptable.
- S6 WANTED-survivor list: = union of the positions' WANTED lists minus the
  on-disk falsifications of REF-3(ii) (Ancourt, K-T 2004/2015/2016, Teasley,
  Wolanski). Consistent; "L-P Aerospace 10:267" = the positions' "L-P 2023"
  with fuller identity.
- §5 SR-1..SR-12: each rule traces to its named source (P1/P2/P3 SR sets,
  REF-6/7/11/24 placements; SR-11 = P3 SR-10 verbatim; SR-12 = INV-6
  elevated — a judge-added rule but explicitly sourced to the refutation's
  own lesson and labeled as such).

FINDING → R-2 (MEDIUM): §0.2(1)'s "24 untracked validation .json/.log" and
the GT-1-CONFIRMED framing carry a FALSE sub-premise uncorrected. Measured
this pass: ALL 25 validation/*.json are TRACKED (`git ls-files
'validation/*.json'` = 25/25); untracked non-md mass = exactly the 24 .log
+ raws. The refutation's GT-1 ("+ 25 gate .json" in the single-copy set),
P2 §0 ("25 .json gate memos — untracked. s25_spdb_m6.json IS the M6
rejection verdict"), and P2 Appendix-A row 10 are all FALSE on this point,
and the judge — whose own §9 finding is about exactly this failure class —
never names the correction: the "24 .json/.log" phrasing is numerically
right (0 json + 24 log) but reads as a combined untracked class, UD-1's
add-list repeats it, and Q13's risk-mass language (via the REF-28 citation:
"advisory corpus + gate json") inherits the phantom risk. The porcelain-
at-execution rule (REF-1) self-heals the ADD-LIST, so nothing would be
lost — but a "MEASURED CORRECTIONS OF RECORD" section that leaves a false
measured claim standing inside a CONFIRMED verdict is the one defect class
this plan cannot carry. Repair: one explicit line in §0.2 ("the 25 gate
.json are TRACKED — GT-1's and P2 App-A row 10's json claim corrected of
record; the untracked non-md mass is the 24 .log + raws"), and strike
"gate json" from the single-copy-mass wording where inherited.

---

## §2 CHECK 2 — COUNTS RECONCILED (header vs body vs inventories) (result: PASS with 2 findings)

- §0.1 header table vs the seven inventories' OWN in-file reconciliations,
  re-read this pass: seg1 43 ("43 files listed = 43 accounted, Discrepancy
  0"), seg2 181 ("181/181 accounted"), seg3 17 ("17/17 accounted, 17 read
  integrally"), seg4 17 ("17/17 accounted"), seg5 165 ("27+21+17+33+25+24
  +18 = 165. MATCHES"), seg6 37 ("37/37 accounted"), seg7 137 ("13+47+77 =
  137 = list total, discrepancy 0"). Repo subtotal 43+181+17+17+165+13 =
  436 — arithmetic re-verified. The brief's 436/37/137 reconcile
  header-to-body-to-inventories. PASS.
- §8 internal tallies: Q14's "12 standing rules" == §5's SR-1..SR-12; §3's
  group map is used consistently by every S-step lint reference; S7's
  "~90-91 unseeded" is consistent with §8 Q6's "3-4 already seeded" against
  audit 94. PASS.

FINDING → R-3 (MEDIUM): the gap-map Q-count correction is SILENT. The
contract (T2(i)) says "gap-map 36/16/10"; P1 M-6 repeats 36/16/10; the
judge uses "36 GAP + 16 AC + 11 Q" (S7(b), §8 Q6) with no reconciliation
anywhere. Measured this pass on the source
(ADVISORY_S24_sota_gapmap_2026-08-12.md): GAP headings = 36, AC rows = 16,
Q rows = Q1..Q11 = **11**, choice rows = 45. The judge's number is RIGHT
and the contract's is stale — but a plan that eats its own SR-12 must say
so once: "contract said 10 Q; source measures 11 (Q1-Q11, grep); 11 is of
record." Without the declaration, the S7 tranche reconciliation would
surface a mystery +1 against the contract count.

FINDING → R-1 (MEDIUM): §3 header contradicts §3 body. Header: "hard cap 3
new test modules per P3-30.6, REF-30". Body: FOUR new modules —
tests/test_advisory_index.py (xx), tests/test_anchor_resolution.py (xxi),
tests/test_literature_registry.py (xxii), tests/test_glossary.py (xxiii)
(choice/flag checks folded, correctly, elsewhere). P3-30.6's cap was "~3"
and REF-30 endorsed it as "the anti-sprawl budget the runner needs";
declaring it as a hard "3" and then specifying 4 is a header-total-vs-body
defect. Repair (either): (a) fold (xxi) anchor-resolution into an existing
module (test_findings_registry.py is the natural host — it already owns
registry schema checks) keeping the cap at 3; or (b) restate the cap
honestly as 4 with a one-line justification ((xxi) is the durable 4-ter
half per REF-22 and earns its module). Pin one; do not ship the
contradiction.

---

## §3 CHECK 3 — EVERY REFUTATION ADOPTED OR ANSWERED (result: PASS)

Traced REF-1..REF-35 individually to their absorption points in the judge:
REF-1→§0.2(1)+S2+SR-12 | REF-2→S0 (hard precondition #1) | REF-3→S6
four-root repair | REF-4→UD-6-old dropped, declared in §6 preamble |
REF-5→§1 hygiene block + UD-8 extended-grep clause | REF-6→SR-6 placed at
R3 closure | REF-7→raws block rows in (xx)+SR-1 | REF-8→S8(iv) weight
correction | REF-9→S8(i) line-multiset adopted, char-sum/spot-check
REJECTED verbatim | REF-10→S9 recompute (38) | REF-11→§3 HONEST-SCOPE
declaration + SR-4 payoff wording | REF-12→S11 no-deletion + UD-3 default |
REF-13→UD-5 dated-snapshot semantic | REF-14→S2 skip-degraded-mode (no
tarball) | REF-15→CF-2 pinned in §3 + fold caveat honored (code-span rule
not applied to codeless choice rows) | REF-16→env-read-pinned census in §3
and S5 | REF-17→CF-3 pinned in tree (glossary.yaml, flag_registry.yaml) |
REF-18→§2 merged enum (UNRESOLVED kept, LECTURE-ERA qualifier,
CONSUMED-with-residue) | REF-19→S13(d) bounded amendment | REF-20→ORPHAN
ratcheted form in (xx) | REF-21→§2 priced warning + named-tranche rule |
REF-22→(xxi) fragment convention in docstring | REF-23→S1 mandatory
precondition | REF-24→§5 placements | REF-26→§2 ratcheted marker lint |
REF-27→UD-5 copy-in/move split | REF-28→S12(i) Appendix-A regeneration
from git truth | REF-29→S12 gated on S0, canary-vs-universe distinction
carried verbatim | REF-30→§7 right-sizing survives | REF-31→§3 prose
declaration | REF-32→§2(4) tie-break of record | REF-33→§8 Q9 | REF-34→UD-4
| REF-35→UD-2/UD-6 evidence-check-first clause.
REF-25 (ratcheted baselines SURVIVE) is the only REF never cited by number:
it is a SURVIVES verdict demanding no repair, and its content is adopted
everywhere ratchets appear ((xx) marker family, (xxiii), ORPHAN ratchet) —
not a dropped refutation. The refutation §5's five HARD PRECONDITIONS: all
five carried, at the exact locations the judge's coverage note claims.
INV-1..INV-6: absorbed via GT-1/GT-2 corrections, S12(i) (INV-4 recount
ordered), §9 (INV-3/INV-6 elevated to a finding + SR-12). No refutation
silently dropped. PASS.

---

## §4 CHECK 4 — EVERY "ABSORBED/COVERED" POINTED AT ITS COVERING ITEM (result: PASS)

- §8 table: every Q row names positions adopted AND refutations answered by
  id; sampled cells re-verified (Q4's "REF-2 count clause repaired", Q5's
  "REF-9 multiset adopted", Q8's "REFUTED-AS-SOURCED repaired at S6", Q13's
  precondition chain) — all point at real §-locations in the body.
- §6: each dropped/kept decision names its authority (UD-6-old → REF-4/GT-3;
  no-tarball → REF-14; snapshot semantic → REF-13).
- §7: fuori-scope items 1-2 CITED to existing registry rows (verified
  present); item 3 correctly declared NOT-a-row-yet with a proposed id.
- CF-1..CF-14 pin-map (§8 note): each location checked — all real. One
  wobble: the FLAG-REGISTRY fold destination is left as "(xx) or (xxiii)"
  in §3 — an unpinned either/or inside the very plan that makes CF-pinning
  a discipline. → R-4 (LOW): pin the fold destination before any test code
  (recommend (xx): the index module already owns bijection-style checks;
  (xxiii) is the glossary's token world).
- "All 15 CONVERGED" (§8 header): NOTE, no repair — this is
  judge-convergence, not position unanimity; every row that adjudicates
  AGAINST a position's clause says so with the REF id (Q1 zero-moves vs P1
  M-3; Q3 re-scope vs all three; Q4 ORPHAN wording vs P2-8). Substance is
  not manufactured; the word "CONVERGED" is doing double duty but the
  dissent trail is intact in every row.

---

## §5 CHECK 5 — CONTRACT COVERAGE (result: PASS with 2 letter-level findings)

Obligation-by-obligation against ADVISORY_Sordine_prompt_2026-08-12.md:
- T2(i) R31 seeding → S7 (tranches, three-way counts, declared split) ✓
- T2(ii) choice ledger → S5 (45 rows, tallies, fold) ✓
- T2(iii) ADVISORY_INDEX + micro-lint → S3 + lint (xx) ✓; archive/ → see R-6
- T2(iv) PROGRESS slim → S8 ✓ | T2(v) memory sweep → S9 ✓
- T2(vi) literature registry → S6 (four roots, repaired) ✓
- T2(vii) per-move nothing-lost → every S-step carries its named
  verification; reconciliation at S12(v) ✓
- T2-bis(a) glossary+lint → S10/(xxiii) ✓ | (b) flag registry → S5 ✓
  | (c) orchestration-weight standing rule → SR-9 + S13(e) ✓
  | (d) flat-dir hygiene under the priced constraint → §1 block ✓
- 4-ter(i) ledger+destination map → S12(i-ii), FAIL-not-footnote wording
  preserved ✓ | (ii) adversarial loss-hunter with all three duties
  (sample + pre/post diff + 10 historical traces) at FULL contract
  strength, no wording weakening found ✓ | (iii) BOTH seeded rejectors
  (in-memory destination removal must FAIL the gate; absent canary must be
  flagged by the hunter; detector-not-firing = session does not close) ✓
  | (iv) zero-discrepancy reconciliation as R3 closure PRECONDITION, delta
  vs 428/436 by name both directions ✓
- T3: CLAUDE.md delta proposed (UD-7) ✓; ONE R3 checklist line ✓;
  lints-that-fire doctrine ✓; → R-5 for the third T3 item.
- Phase-4 spec (full-text by path, dedup vs findings_registry, target
  structure / taxonomy / step-plan / standing rules / open user decisions
  incl. the commit question in primis): all delivered ✓.
- TERMS: no S14-S25bis re-litigation found; pending decisions
  (filelock/O5/M6) explicitly left in their windows ✓; R4 no-deletion
  honored (S11/UD-3, REF-12) ✓.

FINDING → R-5 (LOW): T3's middle deliverable — "riga di censimento
standing" (a STANDING census row registering the converged education
regime, the same pattern as R29's standing-directive row) — is not
explicitly delivered: S13(c) only updates R32 (consumed/split), which is
the session row, not the standing rule row. Repair: add to S13 one line
minting the standing census row for the SR-1..SR-12 regime (or explicitly
declare the CLAUDE.md delta + R32 row as its agreed carrier — but say it).

FINDING → R-6 (LOW): T2(iii)'s letter includes "archive/ con banner"; the
judge makes archive/ conditional on UD-8 with default banner-in-place.
The adjudication is well-founded (P3-2 + REF-5, priced) and this red-team
AGREES with it on the merits — but P3 declared it as "divergence from the
prompt letter, declared" and that declaration was dropped in fusion. Per
R3 discipline (deviations DECLARED), add one line: "T2(iii) letter
divergence declared: archive/ is made conditional on UD-8; banner-in-place
is the default of record, per CF-1/REF-5."

---

## §6 CHECK 6 — NOTHING-LOST GATE: CAN THE REJECTORS ACTUALLY FIRE? (result: PASS with 1 finding)

- Design audit of S12: the gate is a one-shot exit-code-gated script over a
  typed ledger (item | source | destination); rejector (iii-a) removes a
  destination-map item IN-MEMORY → a bijection/resolution check over a
  finite typed list deterministically fails on a removed item: CAN fire.
  Rejector (iii-b) plants a canary absent from the corpus → the
  loss-hunter's mandate (default "something IS lost") + the 10-trace duty
  makes a planted absent item detectable: CAN fire, and the plan carries
  REF-29's honest limit verbatim (canary tests the DETECTOR, not the
  universe — hence the S0 hard gate, which is what makes the firing
  meaningful rather than theatrical).
- Per-lint rejectors in §3: every group ships named seeds (phantom row /
  missing file / unflagged orphan / unparsed marker; doctored dead anchor;
  unregistered PDF / UNREAD-with-summary; unknown token / baseline bump;
  ownerless NEVER row; phantom flag) — the R5 "a lint without a firing
  rejector does not ship" bar is met in the design.
- S12(v) reconciliation input = the S0-REGENERATED count + FOUR roots,
  never the stale 436 — the GT-2 failure mode is closed at the input, not
  patched at the output.

FINDING → R-7 (LOW): S0's parenthetical freezes a stale sub-count:
"literature_review/ (INDEX.md + 26 reports + 25 PDFs + assets)". Measured
this pass: reports/ holds **27** files — the 26 named in GT-2 PLUS
VERIFICATION_FABLE_2026-08-13.md, a file that appears in NO input document.
The total 54 still reconciles, and S0's own logic says enumerate fresh —
but a hard precondition step should not carry an inherited sub-count that
is already wrong on disk (SR-12's own rule). Repair: reword the S0
parenthetical to "reports/ contents at fresh ls" (or update to 27 with the
fable file named), so the supplementary reader pass cannot inherit 26.

---

## §7 REPAIR LIST (numbered, for the judge/executor)

- **R-1 (MED)** §3: resolve the module-count contradiction — fold (xxi)
  into test_findings_registry.py keeping the cap at 3, OR restate the cap
  as 4 with REF-22 justification. Pin one form.
- **R-2 (MED)** §0.2(1)/UD-1/Q13: declare of record that all 25 validation
  gate .json are TRACKED (measured `git ls-files` 25/25); correct GT-1's
  and P2 Appendix-A row 10's json claim explicitly; strike "gate json"
  from single-copy risk-mass wording; UD-2 stays (the 24 .log are the real
  untracked evidence set).
- **R-3 (MED)** S7(b)/§8-Q6: declare the Q-count correction — contract
  said 36/16/10; the source gap-map measures 36 GAP / 16 AC / 11 Q
  (Q1-Q11, grep-verified); 11 is of record.
- **R-4 (LOW)** §3 flag-registry row: pin the fold destination ((xx)
  recommended); no "or" in a pinned group map.
- **R-5 (LOW)** S13: deliver T3's "riga di censimento standing" explicitly
  (mint the standing census row for the SR regime, or declare its carrier).
- **R-6 (LOW)** §1: add the one-line declared divergence from T2(iii)'s
  letter (archive/ → UD-8-conditional, banner-in-place default).
- **R-7 (LOW)** S0: unfreeze the "26 reports" sub-count (fresh-ls wording;
  reports/ = 27 files today incl. VERIFICATION_FABLE_2026-08-13.md).

## §8 WHAT THIS RED-TEAM VERIFIED CLEAN (for the record)

Header/body/inventory count chain 436/37/137 reconciled at every hop;
GT-1/GT-2/GT-3 re-verified on the live tree (47 tracked .md, 26 tracked
logs, Scert tracked, 3 cited commits present with matching content, 54-file
fourth root present, no GENO line in .gitignore, 20-row registry with the 3
cited rows and NO collision for the §9 proposed row); all 35 REFs and 14
CFs traced to real absorption points with zero silent drops; the 5 hard
preconditions carried in order; contract obligations T2(i-vii),
T2-bis(a-d), 4-ter(i-iv), T3 all mapped (two letter-level gaps → R-5/R-6);
loss-hunter and 4-ter wording at full contract strength (no silent
weakening found anywhere in the plan); no judge-added claim without either
a source pointer or a declared-and-reproducible fresh measurement; no
S14-S25bis verdict re-litigated; the plan's PLAN-ANCHOR spine answers the
PRIMARY LENS structurally (§1 navigation chain + ORPHAN-ratchet + census
artifacts pointers).

END OF RED-TEAM — phase5-redteam, 2026-08-13. Verdict:
ABSORB_WITH_REPAIRS (R-1..R-7; none blocks the architecture).
