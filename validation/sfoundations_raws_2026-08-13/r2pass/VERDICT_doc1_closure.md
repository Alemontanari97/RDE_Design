# VERDICT — DOC-1 CLOSURE JUDGE (revision-9 two-lens confirming round)

Date: 2026-08-19. Closure judge of record for DOC-1
(`phaseD/phaseD_stop_proof.md`), mandated by `r2pass/VERDICT_escalation.md`
§6 R-1 + `r2pass/VERDICT_confirm.md` §6 R-1' (DOC-1 residue). Paths relative
to `validation/sfoundations_raws_2026-08-13/`.

Inputs read IN FULL: `r2pass/esc_doc1_r9confirm_l0.md` (R9L0-1..3),
`r2pass/esc_doc1_r9confirm_l1.md` (R9L1-1..3), and the revision-9 delta of
`phaseD/phaseD_stop_proof.md` at every attacked passage (condition of record
l.2140-2230; assembly splice l.2270-2305; falsifier consequent l.2390-2440;
grant head l.2441-2459; §13 REVISION 9 block l.4179-4460 incl. the ECL0-1
entry, leg-3 status, label summary, honest residues (1)-(4)). Mandate context:
VERDICT_confirm preamble (dry criterion of record) + §1 DOC-1 + §6
R-1'/R-5'; VERDICT_escalation §6 R-1. Every quoted passage adjudicated below
was spot-checked verbatim against the on-disk revision-9 file THIS window;
every refuter-vs-text and refuter-vs-refuter divergence was re-derived at pen
grade (§3).

NULL=FAILURE CHECK: both confirming slots exist on file, non-empty,
well-formed, one per lens with per-lens ID prefixes (R-4' applied), each
ending in a machine summary, each declaring its scope sweep (grep-measured in
its own window), dedup register, and R-4 binding-rule audit. Neither slot
dry-counted; neither filename overwrote a prior artifact. PASS.

DRY CRITERION APPLIED (refined, per this judge's mandate): DRY = ZERO
sustained BREAKS-THE-LEG + ZERO sustained REPAIR-NEEDED at BOTH lenses;
sustained AMENDMENTS do not block dryness — they are adjudicated here and
listed for carry (applied at the M0-landing composition; no further round).

==============================================================================
## §1 PER-FINDING ADJUDICATION (cross-lens merge declared)

The two lenses raised 3 + 3 findings on the SAME three clauses with
compatible mechanisms; merged at the clause (same rule as VERDICT_confirm §1
ECL0-2 ≡ ECR1-1): R9-A = R9L0-1 ≡ R9L1-1; R9-B = R9L0-2 ≡ R9L1-2;
R9-C = R9L0-3 ≡ R9L1-3. Distinct findings adjudicated: 3.

### R9-A (R9L0-1 ≡ R9L1-1) — the slice-connectedness clause's root-map
### CONTINUITY conclusion (l.2196-2202) + assembly splice (l.2296-2302) +
### fallback branch (l.2213-2215) + §13 entry echo (l.4222-4227):
### **SUSTAINED-REPAIR-NEEDED.**

Quote verified verbatim against revision 9 (l.2193-2202): "... is an
INTERVAL — under which the parity bracketing runs ..., the root is unique,
the (v, S)-image and the chart are single-valued, the root map W -> S(W) is
continuous on the compact hull (single-upcrossing structure: ...), and each
per-segment continuation lands on the DATA root". The "under which" makes
continuity a DERIVED claim of the printed members, and the derivation is
FALSE. Judge re-derivation (full, at pen grade, on the l1 witness W-A):

(i) Along a rest W-segment (m ≡ 0) between U = (2, 0, E_U) and
V = (2/3, 0, E_V), rho and E are affine in the segment parameter, so
eps = E·v with E affine in 1/v gives eps(v) = alpha·v + beta EXACTLY —
the witness's linearity premise is an identity, not an approximation.
(ii) With F(v) := eps(v) - e0(v) = 4 + 3(v-1) - (v-1)^2:
F' = 3 - 2(v-1) ∈ [2, 4] > 0 on [0.5, 1.5], F(0.5) = 2.25, F(1) = 4,
F(1.5) = 5.25 — so F maps [0.5, 1) into [2.25, 4) ⊂ [1, 4] = range of
h_1 = (1+S)^2 over [0, 1], and [1, 1.5] into [4, 5.25] ⊂ [4, 7] = range of
h_2 = 4 + 2(S-10) + (S-10)^2 over [10, 11]: TOTALITY holds at every segment
point. (iii) Every other member checks: dom e = ([0.5,1)×[0,1]) ∪
([1,1.5]×[10,11]) has every S-slice a single INTERVAL
(slice-connectedness satisfied); the strips are separated (S-distance ≥ 9)
so the piecewise e is C^2 on dom; Gibbs closure by construction; c^2 =
v^2 e0'' = 2v^2 > 0; Hess e = diag(2, 2) PD (strict pair); theta = h_i' ≥ 2
> 0 everywhere on dom, hence at every S-root (root-quantifier) and every
hull state (hull-theta); per-slice roots unique, chart single-valued.
(iv) The root map: S(W) = sqrt(F(v)) - 1 → 1 as v → 1^-, and S(W) =
9 + sqrt(F(v) - 3) = 10 at v = 1 — a JUMP of magnitude 9 at the hull point
v = 1, which any segment with v_U < 1 < v_V crosses. The printed conclusion
"the root map W -> S(W) is continuous on the compact hull" is FALSE with
EVERY printed member satisfied. (v) Downstream, exactly as both lenses
state: the hull's (v, S)-image is NOT compact (branch-1 image accumulates at
(1, 1) ∉ dom e) — the assembly splice's "compactness of the hull's state
image" (l.2300-2302) loses its premise and the lambda_min > 0 chain
collapses; E(W) = -rho·S(W) is discontinuous, so on straddle pairs
E(V_n|U_n) → -rho*·(10 - 1) = -9 < 0 while |DeltaW|^2 → 0 (the l1
mechanical sequence -8.918 / -8.9992 / -8.99918 is consistent with the -9
limit; judge-re-derived as -rho*·ΔS at leading order): the granted item (i)
E(V|U) ≥ c|DeltaW|^2 fails at ORDER ONE, and segment interior points ARE
comparison states of record (E3L0-2's consumed sentence). (vi) The fallback
branch ("root UNIQUENESS is imposed directly as a member in its place")
inherits the hole a fortiori — it delivers even less than the interval
member, while the assembly still cites "the three chart clauses" for
continuity in both branches.

Mechanism located exactly and IDENTICALLY by both lenses (independent
witnesses, same class): single-upcrossing is a PER-SLICE (fixed-v) sign
structure; NO printed member constrains how the S-fiber family varies with
v; §1 pins no EOS domain (of record, ER3L1-2/ECL0-1). The unwritten
hypothesis is slice-FAMILY regularity (fiber endpoints continuous in v /
hull (v,S)-image compact), under which — and only under which — the
sign-bracketing argument propagates to W-continuity.

Class adjudication: NOT wording — a MISSING CONDITION MEMBER under which
the printed condition of record fails to be sufficient on an in-class
witness: the exact ECL0-1/E3L0-2 shape one rung further out, REPAIR-NEEDED
by the loop's own severity calculus (and here the strongest break of the
ladder: item (i) negative at order one, not merely non-uniform). NOT
BREAKS-THE-LEG, correctly argued at both lenses: the route-level OPEN
verdict is unmoved (the finding is the SEVENTH consecutive strengthening of
the no-viable-abstract-EOS-route conclusion), no statement or rigor label
moves, and the clause is FREE at the standing gamma(T) closure (§3, item
(b)). Provenance accepted as declared: spec-seeded — the confirming l0
spec's continuity sentence was carried verbatim into VERDICT_confirm R-1'
and transcribed by revision 9; an R-4 transplant-misfit instance (§3, item
(c) for the count reconciliation).

Repair spec of record (the two lenses' named repairs are equivalent; the
union adopted): add FIBER-REGULARITY as the chart's fourth member (or fused
into the third) — "over the hull's v-range the S-fiber family of dom e
varies continuously (fiber endpoints continuous in v, fibers closed
intervals — equivalently the hull's (v, S)-image compact), under which
single-upcrossing DOES deliver root-map continuity on the compact hull
(closed fibers + per-slice uniqueness + continuity of e force any root-
sequence limit into the limit fiber and onto THE root); where fiber
regularity is not available, root-map continuity / image compactness is
imposed directly as a member in its place" — with SAME-PASS propagation to:
the clause's "under which ... continuous" (re-scoped to the new member);
the assembly splice l.2296-2302; the falsifier-consequent enumeration
l.2403-2404 (jointly with R9-B); the grant-head epithet (jointly with
R9-C); header l.110-116; §9 table; honest status line; the AUD-cp note (one
clause: fibers continuous at the closure); the §13 ECL0-1 entry's delivery
sentence + falsifier list (which currently carries NO falsifier for the
continuity sub-claim — the moving-slice witness is the missing one); and
the domain-ladder sentence l.4251-4254 (new outermost rung: ... ->
chart-domain TOPOLOGY (slice-connectedness) -> slice-FAMILY regularity).

### R9-B (R9L0-2 ≡ R9L1-2) — the consequent's geometry bucket mis-sorts the
### root-quantifier member (l.2399-2412; §13 echo l.4274-4283):
### **SUSTAINED-AMENDMENT.**

Quote verified verbatim (l.2403-2408). Judge re-derivation: the
root-quantifier member as defined (l.2178-2180) is "theta > 0 is read at
EVERY S-root of eps(W) = e(v, S) over each hull point" — a pointwise
theta-sign statement at points that are BY DEFINITION points of dom e; the
whole-domain branch's own proviso (l.2390-2391, "PROVIDED the pins are read
on the whole EOS domain") pins theta > 0 there, delivering the member
tautologically. "those are domain/range GEOMETRY no reading of the pins and
no concavity derivation delivers" is TRUE of totality and
slice-connectedness (the printed a0-positive witness supports exactly the
totality half) and FALSE of the root-quantifier member. The member's
uniqueness CONSEQUENCE correctly stays with the interval member
(l.2180-2181), so nothing else moves. The strained collective-bundle
reading was hunted by both lenses and is rejected by this judge on the
sentence's own per-member falsifier individuation ("stay STANDING members
with THEIR OWN §13 falsifiers") and the ECL0-2 precedent. Direction
CONSERVATIVE (under-restoration; no false-restoration power) — which caps
severity at AMENDMENT per the unbroken lineage class (EL0-4, E2L0-2,
E4L0-3/ER3L1-3, ECL0-2/ECR1-1); the defect was MINTED by the revision-9
restatement itself and is spec-seeded (the l0 repair clause's bucket).
Repair of record (both lenses equivalent): "... restores the grant's
PIN-READABLE members — the Hessian member, hull-theta, AND the
root-quantifier member (theta read at roots, which are domain points the
whole-domain reading covers) — MODULO totality and slice-connectedness
(and, post-R9-A, fiber regularity): domain/range GEOMETRY no reading of the
pins delivers ...", at both sites.

### R9-C (R9L0-3 ≡ R9L1-3) — the grant-head epithet vs the same revision's
### stage-name taxonomy (l.2443-2445; §13 ECR1-3 entry meta-claim
### l.4353-4357): **SUSTAINED-AMENDMENT.**

Quotes verified verbatim: the grant head prints "under the STRICT +
hull-theta + CHART-COMPLETE condition of record" (l.2443-2444) while the
SAME revision mints TOPOLOGY-COMPLETED as a SEPARATE stage (condition
carrier l.2161-2162; header; §9; label summary l.4424-4426, which spells
the four-stage form "STRICT + hull-theta + chart-complete +
TOPOLOGY-COMPLETE"), and the §13 ECR1-3 entry claims "the ECR1-3 pattern
not reproduced one revision later" — over-certifying: the grant head IS a
carrier of the revision-9-enlarged condition left on the rev-8 epithet
(five-of-six carriers extended; this one missed). The mechanism is ECR1-3's
own, reproduced at the margin by transplanting ECR1-3's rev-8-calibrated
spec phrase while revision 9 enlarged the condition — one token, divergent
enumerations across same-revision carriers (the CR-2/R4L1-1 species).
Held at AMENDMENT, bottom of band, for the reason both lenses name and this
judge confirms on the page: a benign defined-term reading exists ("condition
of record" = the defined singular object at l.2140-2215, which contains
slice-connectedness; the body labels it "the chart's THIRD clause"; the
grant head's own parenthetical cites ECL0-1 among the genuine additions) —
no consumer that follows the definition moves; the exact rescue that held
ECR1-3 itself at AMENDMENT. Repair of record: grant head extended to
"... + CHART-COMPLETE + TOPOLOGY-COMPLETE condition of record" (or, the
alternative route, CHART-COMPLETE redefined as the three-clause bundle and
harmonized at ALL five printed variants in one pass), plus one annotation
on the §13 ECR1-3 entry's "not reproduced" sentence naming the grant head
as the carrier the sweep missed. To be carried in the SAME pass as R9-A's
grant-head touch.

==============================================================================
## §2 DISCHARGE VERDICTS ADOPTED

The two lenses' §D discharge verdicts on the six revision-9-consumed
findings AGREE verdict-by-verdict and are ADOPTED: ECL0-1 DISCHARGED IN
PART (fails at the transplanted continuity conclusion = R9-A; every
per-slice delivery verified at both lenses); ECL0-2 ≡ ECR1-1 DISCHARGED IN
PART / AS DEMANDED (caveat de-inversion + else-branch completion verified;
residual = R9-B, minted by the restatement); ECL0-3 DISCHARGED CLEAN;
ECR1-2 DISCHARGED CLEAN (both determinant regimes arithmetically verified,
l1 mechanically); ECR1-3 DISCHARGED WITH RESIDUAL (= R9-C); ECR1-4
DISCHARGED CLEAN (partition independently regenerated at both lenses).
Standing dispositions (r2-batch; rounds 1-4; confirming round) re-verified
at both lenses against the revision-9 state: none reopened; no orphan
objection on disk. Leg-3 body: ZERO revision-9 edits (grep-verified at both
lenses); the leg-3 thread stays DRY of record — held open by the per-doc
rule only.

==============================================================================
## §3 REFUTER-VS-REFUTER / REFUTER-VS-TEXT DIVERGENCES, RE-DERIVED

(a) **l1 recital slip, immaterial:** the l1 file prints S_U = 0.803 for its
witness endpoint, but F(0.5) = 2.25 with h_1 = (1+S)^2 gives
S_U = sqrt(2.25) - 1 = 0.5. Judge ruling: a recital slip (any root in
[0, 1] serves; the printed member checks and the jump at v = 1 are
unaffected — the witness class is robust and the l0 witness is independent
and clean). Does not move any class.
(b) **Closure fiber description, l0 vs l1:** l0 derives the gamma(T)
closure's S-fibers as [phi(T_min) + R ln v, phi(T_max) + R ln v]
(continuously moving); l1 calls the tabulated domain "a fixed PRODUCT
(v-range x T-interval), the slice family constant in v". RECONCILED, not a
conflict: l1 describes the (v, T) chart (a product), l0 its (v, S) image
(R ln v-shifted fixed interval, endpoints continuous in v). Both satisfy
the fiber-regularity member; R9-A discharges automatically at the closure
under either description — the AUD-cp sentence needs only l0's one added
clause.
(c) **R-4 instance count, l0 "ninth and tenth" vs l1 "nine through
eleven":** l0 numbers only R9L0-1 and its restatement-audit failures as new
instances; l1 numbers all three merged findings (continuity bucket, geometry
bucket, epithet) as instances nine/ten/eleven. Judge ruling: l1's
enumeration is adopted (each of the three is a distinct transplant-
calibration misfit under the R-4 rule as written); the count of record
advances to ELEVEN declared instances; the absorbing form "eight-plus"
(VERDICT_confirm R-1') stays true. Bookkeeping only — no class or dryness
effect.

==============================================================================
## §4 DRY ADJUDICATION AND CONSEQUENCES

Sustained at this round, both lenses concurring: **1 REPAIR-NEEDED (R9-A) +
2 AMENDMENT (R9-B, R9-C); 0 BREAKS-THE-LEG.**

Under the dry criterion of this mandate (zero sustained BREAKS + zero
sustained REPAIR at both lenses): **DOC-1 is NOT DRY.** Consequences, per
mandate:

- **Legs 3 and 5 STAY OPEN.** No leg closes. (Leg 3's own thread is dry of
  record at both lenses — zero revision-9 body edits — but it is held by
  the per-doc rule, which this verdict does not and cannot waive.)
- **NO FURTHER ROUNDS under this mandate.** The until-dry loop ENDS here by
  the caller's design; the residue is NAMED (below), not re-cycled.
- The [T-T0P] main statement stays **SCHEMA** (no label motion — none was
  in prospect at either lens). The route-level OPEN verdict, two-piece r2
  residue, quadruple-pinned grant, and gamma-table conclusions stand.
- The gated items stay **BLOCKED** (they unblock only on DRY): the [T-T0P]
  main-statement landing (split gap lists etc.), the G8/[C-XBVP](a')
  registry row + gap-graph edges, and the [T-XWS] retro-annotation — the
  legs-3/5 held-out set of VERDICT_confirm §6 R-5' is UNCHANGED.

**RESIDUE OF RECORD (named owner, no further rounds here):**

- **RES-DOC1-1 (the sustained REPAIR, R9-A):** the TOPOLOGY-COMPLETED
  condition of record lacks a slice-FAMILY regularity member; the printed
  root-map-continuity conclusion is underivable and the assembly's
  compactness step + the bridge's uniformity clause consume it. Repair spec
  converged across both lenses and adopted verbatim in §1 R9-A (one member
  + fallback + same-pass carrier propagation, incl. the domain ladder's new
  outermost rung). All three findings discharge automatically at the
  standing gamma(T) closure — the defect lives in the abstract-EOS
  accounting only. Owner: the revision-10 consumption pass at the
  M0-landing composition window (S-FOUNDATIONS-C orchestrator; F2 window if
  the landing composition is deferred), applied TOGETHER with the two
  carried amendments below in one pass; adjudication authority for that
  pass = this verdict (no new confirming round is owed by this mandate —
  any re-opening is a NEW user/orchestrator decision).
- **RES-DOC1-2 (carried AMENDMENTS, applied with RES-DOC1-1's pass):**
  (1) R9-B: falsifier-consequent member re-sort at both sites (root-
  quantifier member is pin-delivered in the whole-domain branch; MODULO
  totality + slice-connectedness + fiber regularity only; uniqueness
  consequence stays with the interval member). (2) R9-C: grant-head epithet
  extended (+ TOPOLOGY-COMPLETE) or the CHART-COMPLETE taxonomy harmonized
  at all five printed variants; §13 ECR1-3 entry's "not reproduced"
  meta-claim annotated (five-of-six sweep).

==============================================================================
## §5 FALSIFIERS FOR THIS VERDICT

- A derivation of root-map continuity on the compact hull from the printed
  revision-9 members alone (refuted by two independent in-class witnesses,
  one re-derived in full by this judge at §1 R9-A).
- A printed line of record making v-moving fiber families out-of-class
  (none: §1 pins no EOS domain — of record at ER3L1-2/ECL0-1, both
  falsifier lines cite it).
- A break of the W-A witness at any checked member (each re-verified at pen
  grade in §1 R9-A(i)-(iii)).
- A reading of record under which some S-root lies outside dom e, or the
  whole-domain proviso does not pin theta there (kills R9-B; none exists —
  roots are domain points by definition).
- A printed line defining CHART-COMPLETE as the three-clause bundle FOR ALL
  CARRIERS (kills R9-C; the same header separately mints TOPOLOGY-COMPLETED
  as its own stage, and the label summary prints it as a separate axis).
- For the NOT-DRY verdict itself: a demonstration that R9-A is wording-class
  (refuted: an in-class witness satisfies every printed member while the
  granted item (i) is violated at order one — a missing condition member by
  the loop's own severity calculus and its ECL0-1/E3L0-2 precedents).

END — DOC-1 closure verdict. Machine summary:
{doc1_dry: false, legs_closed: [], sustained: {breaks: 0, repairs: 1 (R9-A),
amendments: 2 (R9-B, R9-C)}, no_further_rounds: true,
residues: [RES-DOC1-1, RES-DOC1-2],
file: validation/sfoundations_raws_2026-08-13/r2pass/VERDICT_doc1_closure.md}
