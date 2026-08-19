# VERDICT — S-FOUNDATIONS-C escalation window (Blocco 1-bis), FINAL JUDGE

Date: 2026-08-19. Judge of record for the escalation window mandated by
`VERDICT_r2pass.md` §4(c) (E-1..E-4) and §1/§4 E-5/E-6 (seed protocol v3,
landing gate). Baseline = the J-r2p downgrades of VERDICT_r2pass (J-r2p-1,
J-r2p-2, J-r2p-3); ceiling for restoration = the standing labels BEFORE
those downgrades (proofs-1 §3 / contract B.3), grantable ONLY on a repair
fully closed at dry. Paths relative to
`validation/sfoundations_raws_2026-08-13/`.

Inputs read IN FULL: `r2pass/VERDICT_r2pass.md`; ALL twenty escalation
refutation files `r2pass/esc_doc{1,2,3}_r*_l*.md` (doc1: r1_l0/l1, r2_l0/l1,
r3_l0/l1, r4_l0; doc2: r1_l0/l1, r2_l0/l1, r3_l0/l1; doc3: r1_l0/l1,
r2_l0/l1, r3_l0/l1, r4_l0); `r2pass/SEED_PROTOCOL_v3.md`,
`r2pass/refute_SEEDv3_KT3.md`, `r2pass/refute_SEEDv3_KT4.md`,
`r2pass/BRIEF_slot_KT3.md`, `r2pass/BRIEF_slot_KT4.md`; the newest
revision-log blocks and every attacked body passage of the three target
documents (`phaseD/phaseD_stop_proof.md` REVISION 7/8 blocks + G8-row body
lines ~2116-2300; `phaseD/phaseD_meanswirl_formalization.md` r6/r7 blocks +
register row + disposition tables; `phaseD_L4_implies_R1.md` r3.4/r3.5
blocks + NG-3 row). Quote spot-checks and pen-grade re-derivations by this
judge are listed in §5.

NULL=FAILURE CHECK: all twenty escalation slots and both seed slots exist
on file, non-empty, well-formed, each ending in a machine summary or a
mandatory-vocabulary verdict; every round with a missing lens is DECLARED
in the surviving file or in the target's revision log (doc1 round-2 l1
asymmetry declared and later closed by `esc_doc1_r2_l1.md`; doc3 round-2
ran l0 only, declared, l1 coverage restored at rounds 3-4). The recurrent
brief/disk round-number off-by-ones are declared in every affected file's
header with no artifact overwritten (audit chain intact). No slot is
dry-counted. PASS.

==============================================================================
## §1 ⚠️ SEED LAYER (prominent) — {canary_killed: TRUE, knowntrue_survived: TRUE}
## LAYER PROVEN IN BOTH DIRECTIONS THIS WINDOW

**KT-3 (canary): KILLED — criterion MET (BROKEN with positive falsification
at source).** The refuter identified BOTH seeded route errors independently
and at source: Error A — (omega·grad)u = (u_r omega_theta/r) e_theta ≠ 0 by
the rotating basis (theta-independence of components ≠ vanishing of the
vector field's theta-derivative); Error B — the dropped omega(div u)
dilatation term, active on the whole claimed class (rho ≡ const forces the
trivial flow). It derived the correct invariant omega_theta/(rho r) and
built an explicit-data Cauchy–Kovalevskaya counterexample.
JUDGE RE-DERIVATION (all check at pen grade): (i) the component-level
transport identity (T1) u·grad(omega) + omega(∂r u_r + ∂z u_z) = 0 re-derived
from ∂z(mom_r) − ∂r(mom_z) with the baroclinic bracket cancelling under
p = P(rho); (ii) the chain (T2)→(T3) to u·grad(omega/(rho r)) = 0 via steady
continuity and u_r/r = u·grad(ln r); (iii) the counterexample algebra at
(r,z) = (1,0) with data u_r = 1, u_z = 2−(r−1), rho = 1, P(rho) = rho:
r-momentum gives ∂z u_r = 0; z-momentum + continuity give the 2×2 system
−1 + 2a + b = 0, 1 + 2b + a = 0 ⇒ (a, b) = (∂z u_z, ∂z rho) = (1, −1);
omega = 1, div-part = 1, u·grad(omega) = −1 ≠ 0; non-characteristic
determinant u_z(u_z² − c²) = 2·3 = 6 ≠ 0. Kill on pure mathematical
content; packaging compliant. The KILL direction is PROVEN — third time.

**KT-4 (known-true): SURVIVED — criterion MET (SOUND-AS-LABELED).** The
third delivery carries all three v2 elisions repaired IN THE ROUTE, judge-
verified against `BRIEF_slot_KT4.md`: (L2) the general azimuthal component
displayed IN FULL — both theta-terms (w/r)∂w/∂theta and ∂p/∂theta present
before H1 is applied; (L1) the shock step closed from RH mass [m] = 0 PLUS
m ≠ 0 PLUS tangential momentum [mw] = 0 ⇒ [w] = 0, with the slip-surface
case excluded by the arc-class definition, not asserted away; (L3) the
cross-shock concatenation CONSTRUCTED (finite concatenation by definition,
matching only at mass-crossing points crossed transversally, one-sided
limits matched by Step 2 pointwise). The refuter's verdict rests on nine
truth attacks and four label attacks, all correctly rejected; judge
re-checks: the Step-1 reduction u_r ∂r(rw) + u_z ∂z(rw) = 0 is exact; the
A2 tangential-RH projection is a genuine one-line derivation; the axis
dichotomy (u_r, w = O(r), flow-invariance, Lipschitz uniqueness) is
complete; the EOS-FREE declaration is true (no step consumes p beyond the
[p] n_theta = 0 geometry). SOUND-AS-LABELED is the correct verdict.

**Rule-7 pre-launch route audit (E-5 machine constraint): EXECUTED.**
Audit chain 1-4 of record in `SEED_PROTOCOL_v3.md` (three genuine
boundary-class delivery defects found and repaired pre-launch; audit 4
COMPLIANT). The v2 failure mode (seed-authoring elision) did not recur.

**BINARY OUTCOME:** canary_killed AND knowntrue_survived — the v3 success
condition is MET. **The verification layer is PROVEN IN BOTH DIRECTIONS
this window.** Per SEED_PROTOCOL_v3 rule 8 and its success condition:
LG-1 (`orchestration:until-dry-confirm-direction-unproven`) confirm
direction DISCHARGED for this window and this pool configuration; the
VERDICT_r2pass §4 escrow becomes RELEASABLE (gate composed in §4 below).
The registry-row update for LG-1 rides the Blocco-2 landing window (R7).
The VERDICT_r2pass §5 second falsifier (re-attribution toward layer
miscalibration on a third pre-audited failure) does NOT fire: the third
delivery survived.

==============================================================================
## §2 Per-doc dryness adjudication (until-dry loop at cap)

Dryness criterion of record (the documents' own): a round returning ZERO
sustained findings at both lenses. Caller loop state: all three docs
NOT-DRY-AT-CAP after 3 recorded rounds. Judge verification: the caller's
status labels are CONFIRMED for all three docs — with one structural
finding the caller's per-doc counters do not show, stated per doc.

**DOC-1 (`phaseD/phaseD_stop_proof.md`, legs 3 + 5 — E-1/E-2).**
Round trajectory verified against files: r1 = 4 distinct findings
(EL0-1..4 ≡ ESC1-F1/F2 merged; 1 R + 3 A, 0 B) consumed at revision 5;
r2 = 3 (E2L0-1/2 + ER2L1-1; 1 R + 2 A, 0 B) consumed at revisions 6-7;
r3-window (two-lens adjudication of revision 7) = 7 (ER3L1-1..3 l1 +
E4L0-1..4 l0; 0 R + 7 A, 0 B) — matches the caller's round-3 count —
consumed at REVISION 8 (log block verified at lines 3768+, all seven
FIXED with the chart clauses, Legendre bridge, attribution and consequent
repairs landed as specified). **The final adjudicated round did NOT
confirm** (7 sustained amendments), and revision 8 carries ZERO
adversarial coverage. DOC-1 = NOT-DRY-AT-CAP. CONFIRMED.
— Special finding, prominent: **the LEG-3 (E-1) thread is DRY at both
lenses** and has been for three consecutive l0 rounds (revisions 5/6/7
re-tested with fresh attacks: well-definedness, unfolding-interchange)
and two consecutive l1 rounds (seam/direction-of-minting, representation
independence, partition sign, rider integrability — all failed). The
leg-3 text is character-for-character stable since revision 5. The
doc-level NOT-DRY status is due entirely to leg 5.

**DOC-2 (`phaseD/phaseD_meanswirl_formalization.md`, leg 6 — E-3; leg-7
A-1 carrier).** Round trajectory verified: r1 = 8 (ESC-L0-1..4 +
ESC-1..4; 1 B + 2 R + 5 A) consumed at r5; r2 = 7 (ESC2-L0-1..4 +
R2L1-1..3; 1 B [R2L1-1] + 1 R + 5 A) consumed at r6; r3 = 8 (F-1..4 +
R3L1-1..4; 0 B + 2 R [F-1, R3L1-1] + 6 A) — matches the caller —
consumed at REVISION r7 (log block + §6-quinquies ROUND 4 disposition
table verified; class pin restated to price N_F front-H²-null directly,
structure clauses re-stated at derived grades, (u1) written,
over-certification counter honestly at FOUR). **The final adjudicated
round did NOT confirm** (2 REPAIR-NEEDED among 8), and r7 carries zero
adversarial coverage. DOC-2 = NOT-DRY-AT-CAP. CONFIRMED. The theorem's
core (∂_φV = 0, the containment, the ⟸ direction, the n_m = 0 case's RH
algebra, Γ_G = γ(T) − 1 in-model line) survived every round at both
lenses; every conclusion-display defect since r4 has been in printed
grade/certification/supporting-claim text — but two of round 3's findings
are proof-content (F-1's pin price; R3L1-1's grade-vs-certification),
which is exactly why the leg cannot close on an unadjudicated r7.
**A-1 (leg 7): verified landed VERBATIM and re-confirmed with no
regression by both lenses at every round r5/r6/r7 (D.2 untouched by any
escalation edit — grep-verified in the refutation files and by this
judge).**

**DOC-3 (`phaseD_L4_implies_R1.md`, leg 14 — E-4; leg-17 A-2 carrier).**
Round trajectory verified: r1 = 13 raised / 10 distinct (ESC-L0-1..7 +
F-1..6 with merges ESC-L0-2≡F-1, ESC-L0-5≡F-3, ESC-L0-4≡F-5; 2 R + 8 A,
0 B) consumed at r3.2; r2 = 9 raised (ESC2-1..5 l0 on r3.2 + ESC2-6..9 l1
on r3.3; 2 R [ESC2-1, ESC2-8] + 7 A) consumed at r3.3/r3.4; r3-window
(two-lens adjudication of r3.4) = 5 (ESC3-4..6 l1 + ESC4-1..2 l0;
1 R [ESC4-2] + 4 A, 0 B) — matches the caller — consumed at REVISION
r3.5 (log block + disposition table + NG-3 register mirror verified,
including the ESC4-2 honesty clause: in the motivating class the Gamma_in
uniform-noncharacteristicity condition is generically VIOLATED, so the
Status-(a) H^1 leg there carries the residual, not the discharge).
**The final adjudicated round did NOT confirm** (ESC4-2 REPAIR-NEEDED
among 5), and r3.5 carries zero adversarial coverage. DOC-3 =
NOT-DRY-AT-CAP. CONFIRMED. The two-face proof core (Claim with
(cl-C)/(cl-F), (D-coll), (H-UP-fam), eps_1', STEPs 1-3, UNION) is
byte-stable since r3.2 and was CONFIRMED at both lenses at every round
(fresh attacks each time: swirl-dominated base, wall contact, cover
exactness, retracted-defect re-runs — all failed); the judge's
proves-too-much test passes substantively on seven instances per round.
All five r3.5-consumed findings live in honesty commentary / Status-(a)
premise / register mirror — none touches a proof step.
**A-2 (leg 17): verified FULLY LANDED** — the sign-classification-jump
mechanism of record, with the F-6 refinement ("adjacent gaps = c-bar, all
pairwise separations ≥ c-bar", correcting the judge's own act-(vii)
"mutual gaps = c" wording for the extreme pair 2c-bar) adversarially
re-confirmed at rounds 2, 3, and 4 by direct spectrum computation
(judge re-check: spectra {−c, 0(×3), +c} and {−2c, −c(×3), 0};
multiplicity pattern (1,3,1) constant; eigenvectors u·n-independent).

**docs_dry = [] (none).** The caller's NOT-DRY-AT-CAP labels are all
accurate. The structural state at cap, for the record: EVERY raised
objection across all twenty files has a landed disposition in its
document's newest revision; NO round ever returned zero findings; the
newest revisions (doc1 rev 8, doc2 r7, doc3 r3.5) are UNADJUDICATED.
The loop is one two-lens confirming round per document away from dry —
and the trend is monotone (doc1: 0 breaks ever, final round all
wording-class; doc2: breaks 1→1→0, REPAIR 2→1→2 but final-round repairs
are grade/pin accounting with the core confirmed; doc3: final round
0 breaks, 1 inherited-accounting repair).

==============================================================================
## §3 Per-leg final adjudication (legs 3, 5, 6, 14)

Binding rule applied (caller mandate): a doc NOT-DRY-AT-CAP cannot close
its legs. All three docs are NOT-DRY-AT-CAP. Therefore **no leg closes
this window**; the ceiling labels are NOT grantable; the J-r2p downgrades
stand with residues named. Per leg:

**LEG 3 (DOC-1 §4 periodization, escalation E-1): OPEN — held by the
per-doc rule ONLY.** Thread state: DRY at both lenses, zero open
objections, text stable since revision 5, freshly re-attacked and
confirmed at every subsequent round. Final label: **[T-T0P] main
statement stays SCHEMA** — unchanged (no J-r2p downgrade existed for this
leg; the repair is text-level; VERDICT_r2pass §4(a): "no further label
motion"). Lands in M0 this window: NOTHING — the [T-T0P] main-statement
landing (which consumes the §4 proof head) stays HELD OUT until doc1
closes dry. Note of record: this leg closes automatically with doc1's
next dry round; no further work on the leg-3 text itself is owed.

**LEG 5 (DOC-1 G8/r2 accounting row, escalation E-2): OPEN.** Final
label: no rigor-label motion (the leg is a gap-accounting row; [T-T0P]
main already SCHEMA); the route-level OPEN verdict, the two-piece r2
residue (STRICT + hull-theta + chart-complete thermal-stability condition
at abstract EOS; x-flux coercivity), and the gamma-table conclusions
stand — strengthened five consecutive times by the loop (L1-2 → EL0-3 →
E2L0-1 → E3L0-1+E3L0-2 → E4L0-2+ER3L1-2). Residue: the revision-8 repairs
(consuming ER3L1-1..3 + E4L0-1..4 — all seven wording/attribution-class,
mathematics verified sound at both lenses) are UNADJUDICATED. Lands in
M0: NOTHING — the G8/[C-XBVP](a') registry-row + gap-graph landing stays
HELD OUT.

**LEG 6 (DOC-2 D.18, escalation E-3): OPEN.** Final labels: **first iff
SCHEMA per J-r2p-2 (KEPT); second iff SCHEMA per J-r2p-3 (KEPT)** —
ceiling (the proofs-1 THEOREM*-tier labels) NOT grantable: the r7 state
is unadjudicated and the last adjudicated round sustained two
REPAIR-NEEDED (F-1: the r6 class pin priced a nullness it did not
deliver, judge-verified genuine via the phantom-front fat-Cantor witness;
R3L1-1: structure clauses printed above their derived grade under a
completeness certification — the FOURTH consecutive over-certification,
honestly counted in-document). Restoration path unchanged: E-3 closure at
dry, then the G-f battery per proofs-1. Residue: r7 repairs (pin
restatement (p1)-(p3), grade-aligned clauses, (u1) written, exemplar
re-scoped, G-f re-bind) UNADJUDICATED. Lands in M0: NOTHING for D.18.
(A-1 for leg 7 is an escrow matter — §4.)

**LEG 14 (DOC-3 Proposition 1'', escalation E-4): OPEN.** Final label:
**SCHEMA per J-r2p-1 (KEPT)** — ceiling ("THEOREM modulo (H-UP)") NOT
grantable at cap despite the two-face proof core having survived every
round at both lenses with delivered strength "THEOREM modulo (H-UP-fam)"
in both refuters' assessment: the until-dry criterion was not met (r3.5
unadjudicated; ESC4-2 REPAIR-NEEDED in the last adjudicated round — the
Status-(a) H^1 discharge clause inherited 1.5.3's uninventoried
variable-type loci on Gamma_in, judge-verified genuine and now repaired
with the honest generically-violated clause). Theorem 1' (leg 12) and
Lemma 1.4 (leg 13) are untouched and release with the escrow (§4).
Residue: r3.5 repairs UNADJUDICATED; the Gamma_in/Gamma_mid variable-type
trace residual is owned by NG-3 (F2) with the W^{1,1} Gauss-Green
alternative named-not-consumed. Lands in M0: NOTHING for Prop 1''.
(A-2 for leg 17 is an escrow matter — §4.)

==============================================================================
## §4 GATE — landing_gate_open = TRUE (escrow release; held-out set named)

Test of record: seed layer passed both directions (§1: YES) AND every
escrow item of VERDICT_r2pass §4 releasable (verified: YES). Per
SEED_PROTOCOL_v3's success condition, the v3 dual-seed PASS is exactly
the named condition under which "M0 promotion of these becomes unblocked"
(VERDICT_r2pass §4(a)/(b)) — **the Blocco-2 landing gate OPENS for the
escrow set.**

**RELEASED PACKAGE (explicit; escrow legs 1, 2, 4, 7-13, 15-18 — all 14
confirmed legs; none of 3/5/6/14 joins):**
- DOC-1: leg 1 [L-INC] both strata; leg 2 [L-STD] no-topology pointwise
  argument; leg 4 [P-HB3](i') data-space mollification — land at their
  proofs-1 §3.1 labels. (Judge stability check: untouched by revisions
  4-8, which edited only the §4 periodization step, the G8 row, and §13.)
- DOC-2: legs 8 (D.16 gross normalizer), 9 (D.20 contact split — three
  independent derivations of record), 10 (D.10 theta-halves exhibit),
  11 (D.8 plane-stress rewording) at their §3.2 labels; **leg 7 (D.2
  psi-existence + H-CVX arc) WITH amendment A-1 LANDED** ("i.e. genuinely
  nonlinear WITH the convex (compressive-shock) orientation") — verified
  verbatim on disk and re-confirmed no-regression by both lenses at every
  escalation round. (Stability check: no r4-r7 marker touches D.2.)
- DOC-3: legs 12 (Theorem 1' — THEOREM), 13 (Lemma 1.4 — THEOREM),
  15 (Lemma 3.2 — THEOREM*), 16 (Corollary 4 row-(a) — THEOREM in-class),
  18 (Lopatinskii display) at their B.3 labels; **leg 17 (Remark 1.5.5
  (ii')) WITH amendment A-2 LANDED in its adversarially-improved form**
  (sign-classification jump of the incoming/outgoing split; gap wording
  "adjacent gaps = c-bar, all pairwise separations ≥ c-bar" — the F-6
  refinement supersedes the A-2 act-(vii) "mutual gaps = c" phrasing,
  three-round confirmed). (Stability check: no r3.x proof-step edit;
  legs 12/13/15/16/18 grep-verified untouched by every round's machine
  sweep.)

Citation status: the E-6 caveat of VERDICT_r2pass ("judge-read, layer
unproven in confirm direction") is SUPERSEDED for this release — the
layer is proven in both directions this window (§1); released items may
be cited at their labels with provenance "VERDICT_r2pass §3 +
VERDICT_escalation §4".

**HELD OUT of the package (regardless of the open gate):** the [T-T0P]
main-statement landing (leg 3), the G8/[C-XBVP](a') registry-row +
gap-graph landing (leg 5), every D.18 landing item (leg 6, labels
J-r2p-2/3), the Proposition-1'' landing item (leg 14, label J-r2p-1).
These wait for their docs' dry rounds and the successor adjudication.

==============================================================================
## §5 Judge verification acts backing this verdict

Quote fidelity: every final-round quoted passage spot-checked against the
on-disk documents at the cited revision or its superseding annotation —
doc1 body 2116-2300 (condition of record, quadruple pin, written assembly
with the revision-8 Legendre first link, (m1)-(m3), corrected glosses)
and §13 REVISION 7/8 blocks; doc2 r6/r7 log blocks, register row (D.18),
ROUND 4 disposition table (all eight r3-window findings FIXED with
mechanisms transcribed faithfully); doc3 r3.4/r3.5 blocks, disposition
table, NG-3 row (r3.4 mirror + r3.5 Gamma_in extension present verbatim).
NO misquote found; no disposition table misstates its source objection
(checked row-against-file for the final round of each doc).

Spot re-derivations at pen grade (beyond §1's seed-layer set):
(i) doc1 E3L0-1/ER2L1-1 mechanism — at ideal gas the strict condition
holds everywhere while g = exp(kS), k ≥ 1/c_v breaks W-convexity by the
row's own kept iff (f' > 0 AND f''/f' < 1/c_v): the quadruple pin is the
correct repair, and the g = S closure "0 < 1/c_v = c_v > 0" indeed needs
the hull-theta member (c_v = theta/e_SS; the strict pair constrains no
first-order sign) — ER3L1-1/E4L0-4(b) genuine, revision-8 attribution
correct. (ii) E4L0-2's level-crossing parity — two theta > 0 roots of
e(v,·) = eps bracket a theta ≤ 0 root for continuous e_S: exact; the
universal-over-roots clause closes the branch ambiguity. (iii) doc2
F-1's consumption map — the r6 pin's operative clause bounds only
pairwise intersections; the structure-change component is unbounded; the
r7 (p1)-(p3) restatement prices exactly what the chain consumes.
(iv) doc3 ESC4-1's kernel-jump subfamily — for a linear symmetric system
a piecewise-C^1 jump across a fixed surface is a distributional solution
iff A(n)[U] = 0; at u·n = 0 the kernel is the 3-D entropy+shear subspace:
the r3.4 universal was false, the r3.5 certification-relative rewrite is
the true statement. (v) ESC3-6's ∂_t S term — differentiating
E(t) = ∫<S(W̄)U, U> produces <(∂_t S)U, U>, whose bound is the time half
of W^{1,∞} on the cylinder: the fix is exactly the (H1.1)/(H1.1')
convention. (vi) A-2 spectra re-computed (§2). (vii) Doc-level dryness
arithmetic re-counted from the files (per-round objection/break counts
match the caller's loop state under the two-lens-per-revision grouping).

==============================================================================
## §6 Residues and next-step map (owner = the S-FOUNDATIONS-C orchestrator)

- **R-1 (doc1 / leg 5):** revision-8 repairs UNADJUDICATED — one two-lens
  confirming round owed on the rev-8 delta (7 consumed amendments; the
  refuters' own assessment: zero derivation-content defects remain; the
  residue class has been wording/attribution for two consecutive rounds).
  On a zero-finding round, doc1 is DRY and legs 3 AND 5 close together.
- **R-2 (doc2 / leg 6):** r7 repairs UNADJUDICATED — one two-lens round
  owed on the r7 delta (restated pin, grade-aligned clauses, (u1),
  exemplar, G-f re-bind). The over-certification counter stands at FOUR:
  the next revision must not mint a fifth. On dry: E-3 closes, labels
  restore per the proofs-1 upgrade path THROUGH the G-f battery only.
- **R-3 (doc3 / leg 14):** r3.5 repairs UNADJUDICATED — one two-lens
  round owed. Standing owned residual: NG-3 (F2) carries the
  variable-type trace theory on Gamma_mid AND Gamma_in's grazing loci
  (generic in the motivating class); the W^{1,1} Gauss-Green route is the
  named debt-free alternative, not yet verified. On dry: E-4 closes; the
  ceiling "THEOREM modulo (H-UP)" (in its honest (H-UP-fam) form) becomes
  grantable by the successor judge.
- **R-4 (spec-seeding pattern, standing lesson):** SIX-plus declared
  instances across the loop of a repair-spec clause seeding the next
  round's finding (both lenses affected, including self-seeding). Binding
  for the confirming rounds: every repair clause is restated against the
  row's own hypotheses, never transplanted verbatim from a refutation
  file.
- **R-5 (seed line):** LG-1 confirm direction discharged for THIS window
  and THIS pool configuration only (v2 rule 5 / v3 rule 8); a new pool
  configuration re-spends a dual-seed certification. The LG-1 registry
  row update rides the Blocco-2 landing window (R7 discipline).
- **R-6 (landing execution):** the released package of §4 is the Blocco-2
  landing input; A-1 and A-2 land in their as-on-disk (improved) forms;
  held-out items stay on the E-1..E-4 escalation ledger.

==============================================================================
## §7 Falsifiers for THIS verdict

- §1 canary adjudication: refuted if (T1) fails symbolically (the quoted
  sympy residual nonzero) or the CK counterexample's first-derivative
  system (a, b) = (1, −1) is inconsistent with the three PDEs at (1,0) —
  both mechanically checkable.
- §1 known-true adjudication: refuted by an in-class piecewise-C^1
  axisymmetric weak Euler solution with an admissibly-concatenated arc
  along which Gamma = rw is provably non-constant, or by exhibiting a
  route step consuming a hypothesis outside H1-H3 (in particular any EOS
  input).
- §2 dryness verdicts: refuted if any doc's newest revision (rev 8 / r7 /
  r3.5) is shown to CARRY adversarial coverage on file (no esc_* file
  targets those states — grep-checkable), or if any final-round sustained
  finding is shown judge-overruled-worthy (each was verified at
  derivation level; overturning one requires breaking the specific
  re-derivation recorded in §5 or in the refuter's self-falsifier).
- §3 non-closures: refuted if the caller's binding rule is shown not to
  apply (the loop state says NOT-DRY-AT-CAP for all three docs; the files
  confirm) — note leg 3's non-closure is EXPLICITLY rule-bound, not
  evidence-bound: evidence of its thread-dryness is on the record and
  unrebutted.
- §4 gate: refuted if any released escrow leg's text is shown edited by
  an escalation revision (machine sweeps say no; grep-checkable), or if
  SEED_PROTOCOL_v3's success condition is shown not to bind the escrow
  release (it is the protocol's own printed consequence clause).

END OF VERDICT — machine summary returned via structured output:
{canary_killed: true, knowntrue_survived: true,
layer_proven_both_directions: true, docs_dry: [],
legs_closed: [], legs_open: [3, 5, 6, 14],
landing_gate_open: true (escrow legs 1, 2, 4, 7-13, 15-18 released;
legs 3, 5, 6, 14 held out),
verdict_file: validation/sfoundations_raws_2026-08-13/r2pass/VERDICT_escalation.md}
