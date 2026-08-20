# CONFIRM-ON-REPAIRS — WAVE 2 (first instance, retro wave-1 included)
S-FOUNDATIONS-C2, 2026-08-19. Dedicated confirming lens of record per
BRIEF_wave2_refuter_judge.md §CONFIRM-ON-REPAIRS (stage adopted
2026-08-19 on the doc1 evidence; ALWAYS-ON first instance). BASE =
validation/sfoundations_raws_2026-08-13. Finding IDs CR-W2-*.

Scope executed:
- (a) ALL judge-repaired clauses of VERDICT_wave2.md — sustained
  repairs = 4 (> 0, stage triggered per §4.18): RC31T-1 (F-C31-1/2/3
  definitions), RC31T-2 (arm-B same-lowering pin + DIR-RKG landing
  item + §2.5 hit-set correction), RC1R-1 (F-C1a re-pin), RC1R-2
  (driver leg). Wave-2 has NOT landed: its repair consumers are the
  verdict's own restatements (§2/§4/§6), the panel texts the §4
  deltas append, and the registry/tree anchors the repair texts cite.
- (b) retroactively (first instance only) the 11 wave-1 repaired
  clauses of VERDICT_wave1.md §1 (RC28-1/-2/-3, RC27-1/-2/-3,
  RC911-1/-2/-3/-4/-5), verified verbatim against their consumers in
  the LANDED ledger rows of docs/choice_ledger.yaml: C28 :421-429,
  C27 :409-419, C9 :219-228, C11 :240-250, C43 :583-591, C56
  :731-740 (C42 :573-581 read as the notification-only sibling).

Duties executed: verify each adopted repair text verbatim against its
consumers; hunt defects MINTED BY the repairs themselves (the
restatement class). Every witness below was re-measured in THIS
window (SR-12), never inherited.

## 0. MEASURED WITNESSES (this window)

- `grep -n "F-C31" PANEL_C31TRIO.md` -> EXACTLY ONE hit, :909, whose
  text is "Falsifiers F-C31-1/2/3 (see panel §4.3)" — the dangling
  pointer inside the panel's OWN proposed ledger note (§4.1 note
  text), reproducing RC31T-1's premise and identifying the citation
  site the repair must replace.
- `grep -n 'id: (C1|C9|C11|C27|C28|C42|C43|C56)'` on
  docs/choice_ledger.yaml -> C1:135, C9:219, C11:240, C27:409,
  C28:421, C42:573, C43:583, C56:731 — all six mandated consumer rows
  read verbatim at those sites.
- claims_registry.yaml:1193-1204 read verbatim = the DIR-RKG row:
  scope carries "the driver of record measures Jacobi scaling once +
  the FULL Hessian at every segment base by forward differences of
  the exact adjoint gradient, held frozen within the segment
  (policy-conformant: re-measured fresh, never carried)"; falsifier
  carries "a brick-2 run that mixes gradients across a re-record
  event ... is NONCONFORMING" — the RC31T-2(c) anchor
  (claims_registry.yaml:1193-1204) is CURRENT and verbatim-true.
- literature_registry.yaml: `grep -n lozano` -> lozano_ponsin_2025 at
  :122 (plus the registry's own :744 comment "ancourt_peter_
  atinault_2023 and lozano_ponsin_2025 EXIST above") — the landed C11
  note's rider-correction claim ("the row EXISTS, no new mint;
  registry :122-128") verified TRUE at source.
- PANEL_C31TRIO.md read at §1.1 (:103-137 W1-W5 axes + WIN RULE),
  §3.1 (:555-646 dispositions + A/B spec), §3.2 (:709-796 [P-QNCARRY]
  protocol + F-C32-1..4), §4.1-4.6 (:891-997 delta texts + counting
  rule). PANEL_C1REP.md read at §4.1 (:896-942 duty items (0)-(6) +
  F-C1a/b/c as filed). VERDICT_wave1.md and VERDICT_wave2.md read IN
  FULL.
- Pen-checks re-run: r^2+4r+1=0 -> decaying root -2+sqrt(3) =
  -(2-sqrt(3)) ~ -0.2679 (RC1R-1's :1293 form) — CONFIRMED; cubic
  B-spline (order 4) control-point support <= 4 spans — CONFIRMED;
  wave-2 dropped-hit arithmetic 10 - 4 = 6 with 1 material + 5
  token-noise — CONFIRMED; wave-1 "eleven closed" C27 list = 11 items
  — CONFIRMED; carried-ID counts 4+15=19 (wave-2) and 11+18=29
  (wave-1) match both §1 totals and both machine summaries —
  CONFIRMED; p >= log2(4/3) = 0.415 (landed C11 reuse bound) —
  CONFIRMED.

---

## 1. WAVE-2 HALF — the 4 adopted repair texts vs their carriers

### 1.1 RC31T-1 (F-C31-1/2/3 definitions, row C31) — ONE DEFECT MINTED + ONE POINTER NIT

**Faithfulness verified:** F-C31-1 is the exact De Morgan negation of
the frozen WIN RULE's incumbent branch (panel :130-137: "[P-IPADJ]
source adjudication certifies its optimality/multiplier semantics AND
the measured barrier-restart overhead is inside existing derived
bands") — FAITHFUL. F-C31-2's W5 carve-out ("W5 is out of scope
inside the A/B — the install decision is already taken at the F2
boundary, declared") is FAITHFUL to already-adjudicated content, not
a criterion drift: the panel's own A/B spec (§3.1(iii)) pins metrics
W1-W4 only, its §4.1 delta says "W1-W4 metrics", and the §1.1 W5 axis
itself routes the install to an O5-class session-boundary decision —
the carve-out is the panel's design, and the repair DECLARES it.
F-C31-3 restates the panel's guard ("any divergence = protocol red",
:643-644) — FAITHFUL. Consumers §2.1 / §4.1 / §6 cite the
definitions by pointer ("AS DEFINED IN VERDICT_wave2 §1.1") —
consistent chain, no restatement decay.

**CR-W2-1 — REPAIR-NEEDED-ON-REPAIR (row C31; defect MINTED by the
repair).** F-C31-2's middle branch as adopted reads verbatim: "arm A
wins => IP path CERTIFIED and the flip candidate CLOSES". The
certification clause is UNCONDITIONAL on the A/B result, while
certification of the IP path is defined by the frozen WIN RULE's
incumbent branch (source-semantics adjudication + in-band overhead)
and is exactly what F-C31-1 REFUSES when it fires. Composition hole:
F-C31-1 fires on EITHER (i) semantics not certifiable OR (ii)
overhead out of band, and then makes the A/B MANDATORY; in branch
(i), if arm B fails to beat arm A on W2+W3 (the A/B metrics
W1..W4 are all program-side measurables — KKT/B-residual closure,
[P-BSTAT] agreement, crispness vs F-4 band, churn, evals — so arm A
can win them while its source semantics remain UNADJUDICABLE), the
pin as written declares "IP path CERTIFIED", i.e. certifies an
engine whose optimality/multiplier semantics FAILED §4bis-grade
source adjudication. That contradicts (a) the WIN RULE it claims
faithfulness to, (b) the verdict's own §2.1 adopted text (engine
stays under the standing INFORMATION-ONLY multiplier discipline
"until [P-IPADJ]" — which in this branch has run and FAILED), and
(c) §5-C31(i), which reserves incumbent-branch selection for
"[P-IPADJ] source adjudication PASSING with in-band restart overhead
(F-C31-1's clean branch)". The panel never granted an A/B-dominance
certification route; the judge's restatement minted it. This is the
falsifier-partition/composition class the record itself polices
(RC27-3, RC911-3, RC2021-2 precedents) — caught pre-instantiation,
but the clause lands in the ledger via §4.1 ("falsifiers named ...
AS DEFINED IN VERDICT_wave2 §1.1") unless repaired, so
REPAIR-NEEDED, not amendment.
**Proposed repair text (judge adjudicates; re-opens ONLY row C31):**
F-C31-2 middle branch -> "otherwise (flip criterion not met, F-C31-3
guard green) the flip candidate CLOSES; the IP path is CERTIFIED iff
F-C31-1's SEMANTICS leg passed. An arm-A win can discharge at most
the OVERHEAD leg (the A/B directly measures what the derived band
proxied — adopted as a DECLARED criterion refinement, §0-ter(b)
marker) [or, judge's stricter option: certification also keeps the
in-band-overhead requirement — then an arm-A win with out-of-band
overhead closes the flip candidate with certification still
REFUSED]. It can NEVER discharge the semantics leg: in the
F-C31-1(i) branch certification stays REFUSED, the INFORMATION-ONLY
discipline persists, and the engine axis re-opens toward the named
orbit (C28-F-1 bundle/MPCC fallback or a new flip candidate)."

**CR-W2-3 — NOTE (self-inconsistent pointer sentence inside the
repair).** RC31T-1's trailing sentence "The §4.1 note text cites
these definitions at their panel site" cannot be executed as
written: the definitions HAVE no panel site (that absence is the
repaired defect — the panel's sole "F-C31" token is the :909
dangling reference "(see panel §4.3)", and panel §4.3 is the C33
delta). The operative delta text is correct and unambiguous
(VERDICT_wave2 §4.1: "AS DEFINED IN VERDICT_wave2 §1.1"), so no
consumer is misdirected; the sentence should read "at their VERDICT
site (§1.1), replacing the panel note's '(see panel §4.3)' citation
at :909". Wording fix only.

### 1.2 RC31T-2 (arm-B same-lowering pin + DIR-RKG landing item + hit-set correction, row C32) — VERIFIED, ONE RESTATEMENT-DECAY AMENDMENT

**Verified this window:** (leg c) the DIR-RKG anchor
claims_registry.yaml:1193-1204 is current; "policy-conformant:
re-measured fresh, never carried" and the gradient-mixing
NONCONFORMING falsifier stand verbatim in the registered directive —
the repair's premise (a carry promotion cannot land while that text
stands unamended) is TRUE at source, and naming the amendment as a
landing item is the correct R7-grade consumption. (leg b) The full
quoted pin is internally coherent with DIR-RKG: same-lowering pairs
ARE obtainable in the segmented driver (base + accepted-trial
gradients are both evaluated under the base segment's frozen plan,
BEFORE the on-acceptance re-record), no gradient pair straddles a
re-record event (so arm B does not trip DIR-RKG's mixing falsifier),
and the verdict honestly pins the obtainability question as its own
overturn condition (§5-C32(ii)). (leg a) dropped-hit arithmetic
10-4=6, one material (:1196 = DIR-RKG), five token-noise —
CONFIRMED; the §2.5 correction is carried-not-yet-applied, normal
for the pre-landing state, with the landing as its declared carrier.

**CR-W2-2 — AMENDMENT (restatement decay across the consumer
chain).** The adopted pin of record is the QUOTED string in §1.1(b),
whose middle clause — "the carried matrix crosses segment boundaries
only as a prior with flip-touched columns invalidated (facet G4
mechanism)" — is the clause that makes arm B a CARRY at all: it is
what licenses cross-segment persistence of the matrix while the
same-lowering clause forbids cross-segment PAIRS. Every downstream
restatement drops it: §2.2 ("secant pairs SAME-LOWERING ONLY ...,
flip-touched columns invalidated, cross-lowering pairs rejected at
update time"), §4.2 ("(C48 B-shape; flip-touched columns
invalidated; cross-lowering pairs rejected at update time)"), and §6.
Read without the prior clause, "same-lowering only" + per-segment
re-records can be misread as forbidding any cross-segment carry —
collapsing arm B into fresh-FD, i.e. deleting the challenger the row
is gated on. Nothing on the page contradicts the pin (all three
restatements point back via "the RC31T-2 repairs"), so this is decay
risk, not error: the landing must apply the §1.1(b) QUOTED pin in
full, and the §4.2 delta text should bind to it explicitly ("pin AS
QUOTED IN VERDICT_wave2 §1.1", mirroring §4.1's "AS DEFINED IN"
convention) rather than carrying only the parenthetical summary.

### 1.3 RC1R-1 (F-C1a re-pin, row C1) — VERIFIED CLEAN

Faithfulness to the panel: "items 1/5" are exactly the panel's item
(1) exact conversion + equivalence gate and item (5) seed-protocol
re-pin (PANEL_C1REP :907-915) — the per-use conversion-map pin
attaches the exact bijection to precisely the two uses the panel
gave it; "F-C1b: correct as written" is consistent (F-C1b's job IS
exact-conversion reproduction, :925-930). The re-pin keeps the
panel's statistic and derived floor and changes only the measured
OBJECT (innocent-data response via the Schoenberg/VD map and/or the
slope-mismatch driver probe); the -(2-sqrt(3)) mechanism form
re-derived this window; the <=4-segment support claim is the correct
order-4 support fact; the W1 instantiation stays a NAMED duty item
(panel item (6)), so no proof-grade overreach is smuggled in by the
re-pin. FIRES-consequences preserved verbatim (structural-removal
claim refuted, flip DEAD, incumbent stands, GAP-21 re-opens on a new
axis). Consumer chain §2.4 / §4.5 / §6 consistent, each naming
RC1R-1 and the innocent-data + per-use-pin content; the
"continuity check, not the twin" clause survives in §2.4 verbatim.
NO finding.

### 1.4 RC1R-2 (driver leg, row C1) — VERIFIED CLEAN

Faithfulness: the revalidation list the repair extends is panel item
(4) ("constraint re-map ... + revalidation-scope report (named
list ...)", :910-913) — "added to item (4)'s named revalidation
list" is exact. The EITHER/OR structure (chart-map conditioning
bound derived — de Boor-class expectation stated at census level
with the derivation itself MANDATED to ship — OR in-chart re-baseline
of the recorded S18/S24 walk inside derived bands) imports no
unproven theorem: the arm is "derive", not "cite". The chart-
dependence mechanism (H_c = A^T H_x A, A non-orthogonal) is the
judge's own §0.1 pen-check, re-followed here — sound. Consumer chain
consistent: §2.4 duty ("items (0)-(6) as paneled PLUS the RC1R-2
DRIVER LEG"), §4.5 (same, with TR geometry + Jacobi preconditioner
named onto the revalidation list), §3.2 (the binding composition
rule: chart-migration = re-record-class boundary; carried curvature
invalidated across it; Jacobi/TR constants re-measured in-chart with
the driver leg as instrument; rule written into BOTH duty texts) —
one rule, stated once, referenced consistently. NO finding.

---

## 2. RETRO WAVE-1 HALF — the 11 repaired clauses vs the LANDED ledger rows

Convention verified first: all five adjudicated rows landed with
status enum MIXED and the verdict wording ("adjudicated-split" /
"adjudicated-with-C11") DECLARED in-note as "ledger-enum MIXED";
evidence fields repoint to the VERDICT_wave1 sections. The mapping is
declared per-row, uniform, and loses nothing — verified NOT a defect.

- **RC28-1 (F-3 re-pin) — VERIFIED.** Landed C28 :429 imports the
  pins by pointer ("Protocol + reporting pins land as repaired per
  the verdict's sustained-amendment list") with evidence ->
  VERDICT_wave1 §2.1, where F-3 is quoted as repaired (matched
  engine path/constraint set; mu_c = 0 strictly at accepted iterates;
  deltas inside existing derived bands; bitwise only where the path
  is provably identical; path-switch delta routed to [P-IPADJ]) —
  §1.1/§2.1 verbatim-consistent. See CR-W2-5 on the pointer's NAME.
- **RC28-2 (Probe B relabel) — VERIFIED VERBATIM.** Landed C28
  carries "Probe B evidence = scratchpad-run toy reproduced by both
  S24 verifiers, numbers in the committed advisory (NOT a committed
  carrier)" = §4.1's exact delta text; the [P-CERTKS]
  commit-own-carrier clause rides §2.1's reporting pins via the
  evidence pointer. No "committed" label survives anywhere in the
  landed row.
- **RC28-3 (adaptive-accuracy/inexact family added + closed) —
  VERIFIED, cross-wave consumer POSITIVE.** §2.1(5) counts it into
  "nine alternatives ... none by omission"; the genuine downstream
  consumer is wave-2: PANEL_C31TRIO §3.2 disposition 6 cites it
  correctly ("CLOSED at wave-1 (RC28-3, both halves of
  K = K_phys ∩ K_budget) — cited, binding, not re-opened; only its
  acceptance-guard survives inside the A/B") and the panel §4.6
  count carries "inexact-TR-family[wave-1-bound]". The repair's
  closure is consumed with both halves intact. (Its M0 anchors
  :2010-2011/:2058-2062 have since DRIFTED; VERDICT_wave2 §0.1
  already declares the drift with the correct current sites and
  rules it not-a-wave-1-defect — consumed here, not re-minted.)
- **RC27-1 (option (m) grouped aggregation) — VERIFIED.** "eleven
  closed by stated reason" enumerates to exactly 11; the landed C27
  note carries "Alternatives closed by stated reason incl.
  grouped/regional aggregation (per-group fencing = optional
  refinement)" — faithful; the rho_g arithmetic (ln 55/ln 3498 =
  0.491) re-confirmed.
- **RC27-2 (arm-B arity/cadence/w pins + guard rewording) —
  VERIFIED.** §2.2 carries the full pins verbatim; landed C27
  compresses to "Protocol arity/cadence/band-width pins ... land as
  repaired per the verdict's sustained list" — "band-width" = w
  (consistent with RC27-8(iv)'s role naming; the landed C42 note's
  "near-binding band width" names the same object). Pointer-name nit
  folded into CR-W2-5.
- **RC27-3 (falsifier partition alpha/beta/gamma) — VERIFIED.** §2.2
  restates all three branch assignments verbatim-equivalent; §5-C27
  (iii) consistently treats (gamma) as trigger-sufficiency
  falsification; landed C27 imports by the same pointer.
- **RC911-1 (C43 adjudicated-with-C11) — VERIFIED with ONE quote
  drift (CR-W2-4 below).** Landed C43: owner "F2 (aligned with C11;
  was S25)" — the S25->F2 alignment rode as specified; note carries
  content identity + "Not a fresh adjudication — a declared
  alignment; the landing window confirms"; C11's landed note carries
  the reciprocal "C43 adjudicated-with-C11 (same window edit)".
  Deferral (option 2) confirmed NOT taken.
- **RC911-2 (matched TOTAL unit-process count) — VERIFIED.** Landed
  C9 note: "F9a (matched TOTAL unit-process count, BOTH counts
  reported, ...)" — faithful; no column-count equation survives in
  the landed row. The row's SUPPLEMENT fold is itself a CONSUMER of
  the repaired rule and applies it correctly to the new r-arm
  ("matched TOTAL count EXPECTED by construction and VERIFIED by the
  repaired-F9a rule (both counts reported per arm, no exemption)") —
  the repair propagated into text written AFTER it, with no
  exemption minted. POSITIVE consumer check.
- **RC911-3 (promotion-threshold derivation before first use) —
  VERIFIED.** Landed C9: "promotion-threshold derivation published
  before first use" — faithful; the supplement's r-arm promotion is
  bound to "the same E_A <= E_U/2 rule", importing the
  publish-before-first-use clause rather than evading it. The
  discipline also propagated by name into wave-2 (PANEL_C1REP F-C1c:
  "RC911-3 discipline transplanted WITH recalibration" — the
  transplant done right, recalibration declared). POSITIVE.
- **RC911-4 (leg (a) ordered before the twin arm) — VERIFIED,
  stronger-form landing declared consistent.** Landed C11 owner:
  "leg (a) ORDERED before leg (b)" — STRONGER than the minimal
  repair (orders all of leg (b), not just its twin arm), but it is
  the verdict's own §2.4 binding-duty wording and §3's binding order
  ("C11 leg (a) runs FIRST"), and the stronger ordering implies the
  repair (the twin arm cannot run early). Not a defect; recorded as
  the strengthened form of record. The twin-arm validity condition
  (CONCLUSIVE observed p; degraded-p via propagation band;
  ORACLE-ONLY labeling) lives at the evidence pointer (§2.4 F11a).
- **RC911-5 (Ancourt consumed; nearest-hits corrected) — VERIFIED at
  source.** Landed C11: "consumes HELD ancourt_peter_atinault_2023 +
  the HELD lozano_ponsin_2025 row (registry :122-128, read-partial,
  PDF on disk — rider corrected per the sustained
  supplement-refutation note: the row EXISTS, no new mint)". Both
  registry rows verified present this window (:199-208 class for
  Ancourt per wave-1 §0.1; lozano_ponsin_2025 at :122 re-measured
  here, plus the registry's own :744 existence comment). Note the
  wave-1 §4.7 rider had listed Lozano-Ponsin 2025 among
  "grep-proven absent" rows — a rider-level defect in repair-ADJACENT
  text that the landing CAUGHT, corrected, and declared in the
  landed row itself; the correction is verified TRUE and needs no
  new finding (already of record). This retro-instance is direct
  evidence for the stage's premise: repaired/adjacent restatements
  are the record's most defect-prone class, and the one that slipped
  was caught only at the next consumer.
- **C56 consumer coherence (rows C11 <-> C56, the mandated sixth
  row) — VERIFIED.** C11's landed F11d clause ("EITHER leg firing
  blocks F11a promotion and re-opens the WEIGHT realization only —
  architecture stands") and C56's note ("a fired F11d re-opens THIS
  row, not C11") state the same re-open semantics from both ends;
  C56's owner field ("gradient role OWED TO wave-2 C31TRIO
  (forecast, not consumed — landing verified 2026-08-19 that wave-2
  had not yet run)") is exactly the state VERDICT_wave2 §2.10
  consumed. No repair-minted inconsistency across the pair.

**CR-W2-4 — AMENDMENT (landed quote drift, row C43; retro).** The
landed C43 note quotes the row's listed alternative as "'per-site
observed-order check + NON-CONCLUSIVE propagation'", eliding
"(o32 estimator reuse)" WITHOUT ellipsis. Both the row's own
alternatives field four lines above (:587) and VERDICT_wave1 §4.5's
exact delta text carry the parenthetical. Meaning unchanged (the
o32-reuse content survives in the same sentence via "F2-C11-
ESTIMATOR-CAMPAIGN leg (a) (GAP-9 ...)"), but a quoted string of
record must be verbatim or marked (R5/SR discipline). Fix at the
next touch of the row: restore the parenthetical inside the quote or
mark the elision "[...]". No re-open needed.

**CR-W2-5 — NOTE (pointer naming in landed C28/C27; retro).** Both
rows import the repaired pins via "as repaired per the verdict's
sustained-amendment list" (C28) / "per the verdict's sustained list"
(C27). VERDICT_wave1 contains no list literally so named: the carried
set is named "repair+amendment texts CARRIED" in §1's totals and
keyed `amendments_carried` in the machine summary — a key which
INCLUDES the 11 REPAIR-class items. A class-pedantic reading of
"sustained-amendment list" (= the 18 AMENDMENT-class findings only)
would exclude exactly the repaired pins (e.g. RC28-1's F-3) from the
import. Harmless in practice — the evidence fields land on §2.1/§2.2
where every pin is quoted as repaired — but the next touch of either
row should name the pointer "the verdict's carried repair+amendment
list (§1 totals / machine-summary amendments_carried)". No re-open.

---

## 3. FINDINGS REGISTER (CR-W2-*)

| ID | class | object | affected row | disposition sought |
|----|-------|--------|--------------|--------------------|
| CR-W2-1 | REPAIR-NEEDED-ON-REPAIR | RC31T-1's F-C31-2 clause "arm A wins => IP path CERTIFIED and the flip candidate CLOSES" (unconditional certification route minted; contradicts WIN RULE incumbent branch + F-C31-1 semantics-FAIL branch + §2.1/§5 of the same verdict) | C31 (re-opens ONLY this row per protocol) | judge adjudicates the proposed conditional split (semantics leg never dischargeable by A/B; overhead leg = judge's declared-refinement vs strict-rule call) BEFORE the §4.1 delta lands |
| CR-W2-2 | AMENDMENT | RC31T-2(b) restatement chain (§2.2/§4.2/§6) drops the load-bearing "carried matrix crosses segment boundaries only as a prior (facet G4 mechanism)" clause of the §1.1(b) quoted pin | C32 (no re-open; landing hygiene) | landing applies the §1.1(b) QUOTED pin in full; §4.2 delta text binds "AS QUOTED IN VERDICT_wave2 §1.1" |
| CR-W2-3 | NOTE | RC31T-1 trailing sentence "cites these definitions at their panel site" self-inconsistent (definitions have no panel site; panel citation site = :909 "(see panel §4.3)") | C31 (wording only) | reword to "at their verdict site (§1.1), replacing the panel's :909 citation"; operative §4.1 delta already correct |
| CR-W2-4 | AMENDMENT | landed C43 note's quoted alternative elides "(o32 estimator reuse)" without ellipsis vs :587 and VERDICT_wave1 §4.5 | C43 (no re-open) | restore parenthetical or mark elision at next touch |
| CR-W2-5 | NOTE | landed C28/C27 pointer "sustained-amendment list"/"sustained list" names a list the verdict does not literally have; pedantic reading excludes the REPAIR-class pins | C28, C27 (no re-open) | rename pointer at next touch to "carried repair+amendment list (§1 totals / amendments_carried)" |

Clean verifications: RC1R-1, RC1R-2 (wave-2) and RC28-2, RC28-3,
RC27-1, RC27-2, RC27-3, RC911-1 (content), RC911-2, RC911-3, RC911-4,
RC911-5 (wave-1 retro) — every adopted repair text traced verbatim or
by declared pointer into its consumers, with two POSITIVE
propagation checks (the repaired F9a rule and the RC911-3 discipline
both correctly consumed by text written AFTER them) and one already-
declared, source-verified landing correction (lozano rider).

## 4. DRY / SUNSET ACCOUNTING (per the brief's clause)

- Findings as filed by this lens: 0 breaks, 1 repair-needed
  (CR-W2-1), 2 amendments (CR-W2-2, CR-W2-4), 2 notes (CR-W2-3,
  CR-W2-5). NOT DRY as filed; sustainment is the wave judge's call —
  a sustained CR-W2-1 re-opens ROW C31 ONLY (escalation rule applies
  to it), everything else carries to the landing as usual.
- Sunset clause: this first instance has filed one repair-class
  defect ON repaired text (plus one decay-risk amendment on repaired
  text). If the judge sustains CR-W2-1, the stage has caught a real
  defect of exactly the class it was built for (an unconditional
  certification branch minted by a judge restatement of a
  conditional WIN RULE) and per the adoption clause it STAYS. If the
  judge overrules it, the zero-sustained count for instance 1 is the
  overruled outcome, and the wave-3 instance decides the demotion —
  the accounting either way is the wave-3 landing's, declared here
  for it.

## 5. MACHINE SUMMARY

```json
{
  "lens": "CONFIRM-ON-REPAIRS",
  "instance": 1,
  "trigger": "VERDICT_wave2 sustained repairs = 4 (> 0)",
  "scope": {
    "wave2_repairs_checked": ["RC31T-1", "RC31T-2", "RC1R-1", "RC1R-2"],
    "wave1_retro_repairs_checked": ["RC28-1", "RC28-2", "RC28-3", "RC27-1", "RC27-2", "RC27-3", "RC911-1", "RC911-2", "RC911-3", "RC911-4", "RC911-5"],
    "consumers_verified": ["docs/choice_ledger.yaml C28:421-429 C27:409-419 C9:219-228 C11:240-250 C43:583-591 C56:731-740 C42:573-581", "VERDICT_wave2 par.2/3/4/5/6 restatement chains", "PANEL_C31TRIO par.1.1/3.1/3.2/4.1-4.6", "PANEL_C1REP par.4.1", "claims_registry.yaml:1193-1204 DIR-RKG", "literature_registry.yaml:122 lozano_ponsin_2025"]
  },
  "findings": [
    {"id": "CR-W2-1", "class": "REPAIR-NEEDED-ON-REPAIR", "repair": "RC31T-1", "row": "C31", "summary": "F-C31-2 'arm A wins => IP path CERTIFIED' is unconditional: in the F-C31-1 semantics-FAIL branch it certifies an engine whose source adjudication failed, contradicting the frozen WIN RULE incumbent branch, verdict par.2.1 and par.5; repair = condition certification on the semantics leg (A/B dominance may discharge only the overhead leg, as a declared refinement or per the judge's stricter option)", "reopens": "C31 only, judge adjudicates"},
    {"id": "CR-W2-2", "class": "AMENDMENT", "repair": "RC31T-2", "row": "C32", "summary": "par.2.2/4.2/6 restatements drop the quoted pin's 'carried matrix crosses segment boundaries only as a prior (facet G4)' clause; landing must apply the par.1.1(b) QUOTED pin in full ('AS QUOTED IN par.1.1' binding in the 4.2 delta)"},
    {"id": "CR-W2-3", "class": "NOTE", "repair": "RC31T-1", "row": "C31", "summary": "trailing sentence 'cites these definitions at their panel site' self-inconsistent (no panel site exists; panel citation site = :909); operative par.4.1 delta already correct"},
    {"id": "CR-W2-4", "class": "AMENDMENT", "repair": "RC911-1 (retro, landed)", "row": "C43", "summary": "landed note's quoted alternative elides '(o32 estimator reuse)' without ellipsis vs ledger :587 and VERDICT_wave1 par.4.5; restore or mark at next touch"},
    {"id": "CR-W2-5", "class": "NOTE", "repair": "RC28-1/RC27-2/RC27-3 (retro, landed pointers)", "row": "C28+C27", "summary": "'per the verdict's sustained-amendment list' names a list the verdict does not literally have (carried set = repair+amendment, JSON key amendments_carried); rename pointer at next touch"}
  ],
  "totals": {"breaks": 0, "repairs": 1, "amendments": 2, "notes": 2, "clean": {"wave2": ["RC1R-1", "RC1R-2"], "wave1_retro": ["RC28-2", "RC28-3", "RC27-1", "RC27-2", "RC27-3", "RC911-1", "RC911-2", "RC911-3", "RC911-4", "RC911-5", "RC28-1"]}},
  "positive_propagation_checks": ["repaired F9a rule consumed correctly by the C9 supplement r-arm (no exemption)", "RC911-3 publish-before-first-use discipline transplanted WITH declared recalibration into wave-2 F-C1c", "RC28-3 closure consumed by wave-2 C32 with both halves intact", "lozano rider defect caught+corrected+declared at wave-1 landing, verified true at registry :122"],
  "dry": false,
  "reopens": ["C31 (iff CR-W2-1 sustained by the wave judge)"],
  "sunset_accounting": "instance 1 filed 1 repair-class defect on repaired text; if sustained the stage stays per the adoption clause; demotion decision remains the wave-3 landing's",
  "file": "validation/sfoundations_raws_2026-08-13/blocco3/confirm_repairs_wave2.md"
}
```
