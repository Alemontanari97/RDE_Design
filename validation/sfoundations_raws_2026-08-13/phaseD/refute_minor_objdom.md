# REFUTATION — PHASE D MINOR (b) [OBJ-DOM]
# S-FOUNDATIONS-C4, Blocco 1, 2026-08-20. REFUTER slot per
# BRIEF_blocco2_phaseD.md MINORS (one round + auto-escalation).
# Target: validation/sfoundations_raws_2026-08-13/phaseD/
# phaseD_minor_objdom.md. This file is the ONLY file this slot writes.
# Findings ID-prefixed MIN-OBJDOM-<n>; classes CONTENT-OBJECTION /
# WORDING / NOTE. Zero inflation: every finding anchored; everything
# not listed under FINDINGS was checked and found sound (see
# VERIFIED-CLEAN).

## FINDINGS

### MIN-OBJDOM-1 [CONTENT-OBJECTION] — OBJDOM-1(a) exactness claim is
false under its own definitions (discrete/continuum mix in a
THEOREM-class statement)

Anchor: author file §1 OBJDOM-1, definition display (DJ_panel =
`2*pi * Int_0^{th1} p(th)*y(th)*rtd*sin(th) dth`) vs clause (a)
("J_declared = J_coded + DJ_panel exactly, where J_declared is the
header objective ... evaluated by the same trapezoid rule extended
with the theta=0 station") and the proof sketch ("(a) is additivity
of the integral over [0,th1] u [th1,L]").

Reason: J_coded is a trapezoid SUM (verified in the current tree:
validation/a1_toc_variational_jax.py:1179-1186 trapezoids supplied
points; stations :530-534 start at k=1). A trapezoid-extended
J_declared therefore satisfies EXACTLY the discrete identity
J_declared = J_coded + 0.5*(p(0)y(0)+p(th1)y(th1))*(y(th1)-y(0)),
i.e. J_coded plus the TRAPEZOID panel term — not plus the exact
integral DJ_panel as defined in the display. The two differ by the
single-interval trapezoid truncation error (generically nonzero
since p*y is not linear in y on the panel; order O((Dy)^3) with
Dy = rtd*(1-cos th1) = O(th1^2), so numerically tiny but not zero).
The proof sketch invokes additivity of the INTEGRAL, which does not
prove an identity in which one side is a discrete sum. As stated,
a THEOREM-class "exactly" is false; the statement mixes three
objects (continuum declared integral, discrete coded sum, hybrid
J_A of protocol P-1) without fixing which pair the identity binds.

Failure/consequence: the exactness class of OBJDOM-1(a) — the
declared load-bearing statement of the adjudication — does not hold
as written; any downstream consumer citing "J_declared = J_coded +
DJ_panel exactly" for the trapezoid-extended functional inherits a
false identity. Scope note (honesty, no inflation): the adjudication
OBJDOM-4 does NOT rest on the exactness of (a) — it rests on
OBJDOM-2/OBJDOM-3 and the (b)/(c) clauses, which survive (see
VERIFIED-CLEAN). The repair is one definitional sentence: either
define DJ_panel as the discrete trapezoid panel term (then (a) is
exact by discrete additivity, and (c) must be restated for the
discrete term), or keep DJ_panel = Int and state (a) as
J_A := J_coded + DJ_panel (a DEFINITION of the fix-A functional,
per protocol P-1) with the trapezoid-extended reading dropped or
given with its declared O(th1^6)-class discrepancy.

### MIN-OBJDOM-2 [CONTENT-OBJECTION] — F-1's acceptance bar is
incomplete under the endpoint panel-pressure rule that P-1 itself
permits: the primary falsifier can fire spuriously

Anchor: author file §2 (P-1) ("kernel arc-flow evaluation vs p(th1)
frozen-endpoint approximation ... declare the resulting order and
its bar") vs (F-1) ("|dJ_A/dthB - dJ_B/dthB -
2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B| <= derived AD/FD bar (bar
derivation = the O3.1 machinery of record, not a new constant)");
also §1 OBJDOM-1 falsifier ("within derived AD/FD bars").

Reason: if the endpoint approximation DJ~ = p(th1)*G(th1),
G(th1) = Int_0^{th1} y*rtd*sin(th) dth, is the implemented rule
(explicitly allowed by P-1), then AD of J_A gives
d(DJ~)/dthB = [p(th1)*G'(th1) + p'(th1)*G(th1)]/n_B: the first term
is F-1's analytic prediction; the second is a MODELING term of
relative order O(th1) ((p'/p)*th1/2-class) that the O3.1 AD/FD noise
machinery does not and cannot cover (it is not roundoff/FD noise;
at the S20 record constants th1 ~ 8.7e-3 it is percent-fraction of
the 5.36e3 J-units/rad row — orders above any AD/FD bar;
SCALING-ESTIMATE from record numbers, illustration only, no new
number of record). F-1 as pinned would then exceed its bar and
"falsify OBJDOM-1" with NO hidden W-dependence and NO geometry
error — a spurious kill of the primary assert, i.e. the pinned
falsifier is not sound across the protocol's own declared
implementation freedom.

Failure/consequence: an F2 executor implementing the endpoint rule
per P-1 and asserting F-1 per its letter reports OBJDOM-1 falsified
and re-opens the adjudication on an artifact. Repair is one clause:
F-1's bar = derived AD/FD bar PLUS the declared panel-rule term of
P-1 when the endpoint rule is used (zero extra term iff the kernel
arc-flow integral rule is used). The brief's mandate for this minor
is "pin the protocol + falsifier"; as pinned, the falsifier is
defective in one of its two allowed branches — content-level.

### MIN-OBJDOM-3 [CONTENT-OBJECTION] — OBJDOM-5's delta-cancellation
mechanism is insufficient as stated: "same domain convention" does
not make the panel term common to the two sides of delta

Anchor: author file §1 OBJDOM-5 ("the panel term is common to both
sides of the distance at fixed thB-convention, so it cancels in
delta IF both sides use the same domain convention — that
same-convention hypothesis is the one (c) must declare") vs the
delta semantics of record: registry row pipeline:delta-carrier-F2-
entry (docs/findings_registry.yaml:292-300, read [FULL]) "delta
semantics of record = distance to the L-unconstrained fixed-eps
ceiling"; ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md
§3.2 (:213-250, read [FULL]): delta = J_ideal(eps) - J_TOC, item 4
"the ceiling evaluation inherits the throat-panel omission", item 3
"an under-estimated ceiling is anti-conservative for delta".

Reason: the two sides of delta are evaluated on DIFFERENT walls —
the ideal-march ceiling contour and the TOC design wall — each with
its own first-station panel: different turn angles (thB_ideal !=
thB_TOC in general), hence different th1 = thB/n_B with n_B =
ceil(thB/da) (the ceil-seam makes th1 differ even at equal da; the
advisory §1 records the O(da^3) jump seam). Adopting the same
DOMAIN CONVENTION on both sides (both coded, or both
panel-inclusive) therefore does NOT make the panel term "common to
both sides": the net contamination of delta is
DJ_panel(ideal wall) - DJ_panel(TOC wall), a difference of two
O(da^2)-class values that cancels only to leading order (shared
throat arc geometry via the Sauer/IVL contract), not exactly — and
the ceiling-side omission is precisely the ANTI-CONSERVATIVE
direction the advisory's §3.2 item 3 flags. So the hypothesis
OBJDOM-5 instructs minor (c) to declare (same-convention) is NOT
sufficient for its "unaffected in value class / it cancels" claim;
the sufficient hypothesis is equal panel terms (same th1, same arc
geometry, same n_B — effectively same-thB-and-plan), or else an
explicit net-panel band with its anti-conservative sign declared.

Failure/consequence: OBJDOM-5 is a BINDING composition note for
minor (c) ("a lemma silent on the domain is non-compliant with this
verdict"); (c) declaring only the same-convention hypothesis, as
instructed, would ship a delta carrier whose value-class invariance
claim fails exactly in the anti-conservative direction the advisory
sequenced [OBJ-DOM] to prevent. Content-level: changes the
hypothesis (c) must declare. (The SCHEMA class and the transfer of
proof obligation are correct form; it is the named sufficient
condition that is wrong.)

### MIN-OBJDOM-4 [WORDING] — misattribution: the quoted fix-A phrase
is the advisory's, not the audit's

Anchor: author file §1 OBJDOM-1(b) ("the audit's fix-A wording
'makes the omitted area W-independent exactly'"). The phrase occurs
in ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md §1.4 (:151)
and NOWHERE in AUDIT_agnostic_2026-08-07.md:507-519 (checked at the
cited range, read [FULL]; the audit's fix language is the suggested
test :517). Reason: provenance discipline — the sentence should
cite the advisory. No conclusion moves.

### MIN-OBJDOM-5 [WORDING] — "§ verbatim" claim that is not verbatim

Anchor: author file §3 header ("trigger = registry row :212
verbatim: before the first F2 verdict consuming dJ/dthB AND before
the R2 delta-carrier ships"). The row text at
docs/findings_registry.yaml:212 reads "first F2 verdict consuming
dJ/dthB AND before the R2 delta-carrier ships; ..." — no leading
"before the" (that prefix is the advisory §1.4 two-sided phrasing,
:155-156). Reason: under this program's citation discipline a
"verbatim" flag must be character-exact or dropped; the content is
faithful, so WORDING only.

### MIN-OBJDOM-6 [NOTE] — F-2's threshold silently departs from the
audit's literal suggested test

Anchor: author file §2 F-2 (threshold 10*gtol) vs
AUDIT_agnostic_2026-08-07.md:517 (suggested assert "< gtol at W*").
Reason: the protocol is titled "the audit's analytic throat-panel
A/B, protocol of record" while the acceptance constant is 10*gtol
(the O3 acceptance of record, advisory §1.3 :131 — defensible and
arguably the more correct comparator) and the pass/fail semantics
are inverted to expected-to-fire. Both are improvements, but the
delta from the audit's literal test should be declared in §2 (one
sentence) so the F2 executor does not face two nominally
"of-record" asserts with different constants. No conclusion moves
(5.36e3 exceeds either threshold by >= 5.7e2x / 5.8e2x).

### MIN-OBJDOM-7 [NOTE] — AG-1 valve label on OBJDOM-2 is in tension
with its load-bearing role in the adjudication

Anchor: author file §1 OBJDOM-2 hypotheses ("sufficient-not-
optimized, declared per AG-1 — this is gap-accounting arithmetic")
vs §1 OBJDOM-4 ground 1, which rests the governing gradient-axis
ground entirely on OBJDOM-2. Reason: per the load-class valve of
record (user-ratified 2026-08-20), gap-accounting treatment is for
non-load-bearing rows; a statement carrying ground 1 of the
decision is load-bearing. Substantively harmless here because the
hypotheses (S20 governing instance; Dv <= 6) are strong, trivially
checkable, AND each is separately covered by the two-sided A/B
falsifier (F-2), so no conclusion moves — but the label should
match OBJDOM-1's treatment ("valve NOT invoked, load-bearing") or
the asymmetry be justified in one clause.

### MIN-OBJDOM-8 [NOTE] — "after the Dv discount" is not pinned to an
executable operation in F-2

Anchor: author file §2 F-2 ("|dJ_A/dthB - dJ_B/dthB| > 10*gtol at
W* after the Dv discount") vs AUDIT_agnostic_2026-08-07.md:527-533:
scipy's optimality lives in Dv-scaled u-coordinates (jac = g*Dv)
while the tilt row is physical. Reason: the brief mandates pinning
the protocol; an executor needs the exact operation — divide the
physical thB-row by the recorded Dv_thB coordinate scale (exact),
or by the worst-case spread 6 (conservative bound of record, audit
:533). Either is fine; F-2 should name which. Expected-fire margin
(>= 96x, verified arithmetic) makes this outcome-irrelevant at the
S20 instance, hence NOTE.

## VERIFIED-CLEAN (checked, no finding — listed so the judge sees
the coverage; all in THIS window)

- Registry row variational-driver:objective-omits-throat-panel
  (docs/findings_registry.yaml:204-213, [FULL]): status/magnitude/
  owner/trigger quoted faithfully by the author; the row's code
  anchors :516-522/:1130-1137 ARE drifted (verified: :516-522 is
  now column-stack code; thrust_J now :1179-1186; stations loop now
  :530-534) — the author's re-verified anchors and the §4 refresh
  proposal are CORRECT.
- Code facts (validation/a1_toc_variational_jax.py :22-27, :530-534,
  :1179-1186, [FULL]): objective header "(0, theta_B]" + Pa clause
  :25-27; stations start k=1 (no theta=0 station); trapezoid over
  supplied points only. All as the author states.
- OBJDOM-1(c) Leibniz derivative: re-derived symbol-for-symbol;
  matches the advisory formula (:64) under the declared
  W-independent-p hypothesis. Sound.
- OBJDOM-2 arithmetic: 5.36e3/9.3 = 5.8e2; /6 => 96x >= ~1e2-class.
  Matches advisory §1.3 (:119, :131-133) and audit :533. The
  REFUTED-component reading of the gtol derivation (1e-8 =
  trust-constr's own default = derived-by-declaration) is quoted
  correctly. Sound; classification THEOREM* appropriate.
- OBJDOM-3 (a)+(b): both proofs check (constancy on the feasible
  set under fix-A; dA(th1)/dthB = 2*pi*y(th1)*rtd*sin(th1)/n_B > 0
  under fix-B); consistent with audit verifier note :519 (Pa-anchor
  sub-finding) and advisory folded precision (iv) (:95-99).
  The vacuum-objective proviso is correctly carried. Sound.
- OBJDOM-4: the decision structure (fix-A of record at F2 entry,
  fix-B scoping as interim) is grounded in the brief's binding
  gradient-axis clause and the advisory §1.3/§1.4 verdict wording;
  ground 3's value-axis figures (1.0767e-4*p_t, O(da^2),
  Richardson-scoped, F7-cancelling) match advisory :86-91, :120.
  The two-sided rejector design (F-1/F-2 can each kill a different
  statement) is genuinely falsifying, modulo MIN-OBJDOM-2's bar
  repair. The adjudication itself is NOT overturned by any finding
  in this file.
- §3 F2 duties: measured halves all named with owner+trigger; the
  interim doc-scoping covers all three axes (value/gradient/Pa) per
  precision (v) (:100-102). Compliant with the brief's "any
  measured half = F2 duty named".
- §4 landing text: numbers and anchors verified (tilt 5.36e3,
  acceptance 9.3, refreshed code anchors correct).
- Author's "no external literature bears on it": checked the
  brief's arrivals list against the item's content — agreed; the
  optimization/adjoint corpus feeds minors (a)/(d), not this
  domain adjudication. PAPERS NEEDED empty is legitimate.

## READ-DEPTH DECLARATION

All internal, no papers consulted:
- phaseD_minor_objdom.md [FULL] (whole file);
- BRIEF_blocco2_phaseD.md [FULL] (whole file);
- docs/findings_registry.yaml:190-239, :290-303 [FULL];
- validation/ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md
  :40-199, :213-267 [FULL];
- validation/AUDIT_agnostic_2026-08-07.md:500-544 [FULL];
- validation/a1_toc_variational_jax.py:18-47, :520-549, :1170-1194
  [FULL].

PAPERS NEEDED: (empty)

## SUMMARY FOR THE JUDGE

3 CONTENT-OBJECTION (MIN-OBJDOM-1 exactness class of OBJDOM-1(a);
MIN-OBJDOM-2 F-1 falsifier unsound in one allowed protocol branch;
MIN-OBJDOM-3 OBJDOM-5's insufficient cancellation hypothesis,
binding on minor (c)), 2 WORDING, 3 NOTE. None of the three content
objections overturns the OBJDOM-4 adjudication (fix-A of record,
fix-B scoping interim), which this refuter verified as grounded;
all three are repairable by short definitional/clause edits, but
each changes a derivation, a falsifier's soundness, or a hypothesis
another minor is bound to declare — hence content class, honestly
held. Escalation per the standing rule is the judge's call.
