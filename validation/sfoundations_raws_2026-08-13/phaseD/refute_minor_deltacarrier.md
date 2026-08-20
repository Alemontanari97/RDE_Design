# REFUTATION — PHASE D MINOR (c) DELTA-CARRIER
# S-FOUNDATIONS-C4, Blocco 1 v2 continuation, 2026-08-20. REFUTER slot
# per BRIEF_blocco2_phaseD.md MINORS (one round + auto-escalation; v1
# refuter slot died pre-launch, author file on disk is the input).
# Target: validation/sfoundations_raws_2026-08-13/phaseD/
# phaseD_minor_deltacarrier.md. This file is the ONLY file this slot
# writes. Findings ID-prefixed MIN-DELTACARRIER-<n>; classes
# CONTENT-OBJECTION / WORDING / NOTE. Zero inflation: every finding
# anchored; everything not listed under FINDINGS was checked and found
# sound (see VERIFIED-CLEAN — including a full symbol-by-symbol
# re-derivation of the DC-1 proof, which SURVIVES).
# SEQUENCING DUTY (SR-C4-9) DISCHARGED IN THIS FILE: MIN-OBJDOM-3
# (refute_minor_objdom.md, declared BINDING on this minor's hypotheses)
# is applied to the author's hypothesis list below; verdict = the list
# does NOT survive as written; repairs named (findings 1-2).

## FINDINGS

### MIN-DELTACARRIER-1 [CONTENT-OBJECTION] — (H6) is exactly the
"same objective domain" hypothesis that MIN-OBJDOM-3 killed as
insufficient: the two sides of delta live on different walls, so the
same-domain clause does not deliver the value-class invariance the
carrier needs; the sufficient hypothesis must replace it

Anchor: author file §1 (H6) ("the delta carrier evaluates ceiling and
J[S*] on the SAME objective domain — it ships only after the [OBJ-DOM]
fix lands (fix-A or fix-B) or with the throat-panel sliver banded into
the carrier") vs refute_minor_objdom.md MIN-OBJDOM-3 (declared BINDING
on minor (c)'s hypotheses): "the sufficient hypothesis is equal panel
terms (same th1, same arc geometry, same n_B — effectively
same-thB-and-plan), or else an explicit net-panel band with its
anti-conservative sign declared"; also ADVISORY_S25_pipeline_sense_
CONVERGED_2026-08-12.md §3.2 items 3 (:237-241, anti-conservative
direction) and 4 (:242-245, ceiling inherits the omission).

Reason: the author wrote (H6) to the letter of OBJDOM-5's instruction
(phaseD_minor_objdom.md §1, "that same-convention hypothesis is the one
(c) must declare") — compliant with the instruction as it stood when
the author slot ran, but that instruction was then refuted:
MIN-OBJDOM-3 shows the ceiling contour and the TOC design wall each
carry their OWN first-station panel (thB_ideal != thB_TOC in general,
hence different th1 = thB/n_B, with the ceil-seam n_B = ceil(thB/da)
making th1 differ even at equal da), so under a shared CODED (panel-
omitting) convention the contamination of delta is the NET difference
DJ_panel(ideal wall) − DJ_panel(TOC wall), which cancels only to
leading order — and the ceiling-side omission is precisely the
anti-conservative direction (advisory §3.2 item 3) that the [OBJ-DOM]
sequencing exists to prevent. The equal-panel-terms branch of
MIN-OBJDOM-3's repair is unavailable here (the two walls have
different turn angles by construction), so (H6) as written names no
sufficient condition at all: "same objective domain" is declared, and
neither remaining sufficient branch (fix-A-both-sides, or explicit
net-panel band) is stated as the hypothesis.

Failure/consequence: a delta carrier shipped on (H6) as written can be
formally compliant while its (value, delta) row is contaminated by the
un-banded net-panel difference in the anti-conservative direction —
delta under-stated, "closer-to-optimal than true", the exact defect
class DC-5(a) exists to forbid. Repair (one hypothesis rewrite, no
conclusion of DC-1/DC-2 moves): restate (H6) as the disjunction of the
two surviving sufficient branches — (H6') EITHER the fix-A
panel-inclusive functional is used on BOTH sides (ceiling march AND
J[S*]; then no panel is omitted anywhere and no cancellation
hypothesis is needed — the clean branch, and the one consistent with
OBJDOM-4's adjudication of fix-A as the F2-entry objective of record),
OR both sides are coded under the interim fix-B scoping AND the net
two-wall panel difference is banded into the carrier with its
anti-conservative direction declared, the band folded into the
DC-5(a) upper-edge rule (delta quoted against the ceiling edge
worsened by the net-panel band). The same-domain sentence survives
only as a NECESSARY condition, never sufficient. DC-5(b)'s printed
hypothesis line gains the domain-disposition entry (which branch of
(H6') the row shipped under).

### MIN-DELTACARRIER-2 [CONTENT-OBJECTION] — the (H6) ship-gate branch
"after the [OBJ-DOM] fix lands (fix-A or fix-B)" is weaker than the
registry trigger it flags as verbatim: fix-B is a scoping declaration,
not a repair, and a row shipping on fix-B-landed alone is unbanded

Anchor: author file §1 (H6) tail "(row trigger verbatim)" and §6
DC-5(c) vs docs/findings_registry.yaml:300 (read [FULL]): trigger =
"sequenced with/after [OBJ-DOM]; ships only with the sliver banded or
repaired"; phaseD_minor_objdom.md OBJDOM-4 (fix-B survives ONLY as its
scoping clause, never as an absorption; fix-A = the repair, adopted at
F2 entry; fix-B scoping = interim regime).

Reason: the row's two licensed states are BANDED or REPAIRED. "Fix-B
lands" produces neither: under fix-B the coded J is merely DECLARED
(value/gradient/Pa statements scoped), the sliver is still omitted on
both walls and the net-panel difference of MIN-DELTACARRIER-1 is still
un-banded. The author's paraphrase "(fix-A or fix-B) or with the
sliver banded" therefore adds a third, unlicensed shipping branch —
and flags the paraphrase "(row trigger verbatim)" when it is not
verbatim (the row text contains no fix-A/fix-B disjunction; under the
program's citation discipline a verbatim flag must be character-exact,
cf. MIN-OBJDOM-5, but here the deviation also CHANGES the gate's
content, hence content class, not wording).

Failure/consequence: an F2 executor reading (H6)/DC-5(c) in good faith
ships the first (value, delta) row as soon as the interim scoping
lands — with the contamination of finding 1 intact and no band. Repair
(one clause): the gate is "[OBJ-DOM-IMPL] (fix-A implementation)
landed and used on both sides, OR the net-panel band of (H6') included
in the carrier"; drop the "verbatim" flag or quote the row text
character-exact.

### MIN-DELTACARRIER-3 [CONTENT-OBJECTION] — DC-2's class-level sup
chain asserts more than DC-1 delivers: without (H3)-class regularity
IN THE CLASS DEFINITION the pointwise bound genuinely fails, so
sup over A(eps) is not proven <= J_ideal(eps) as written

Anchor: author file §3 display "sup_{A(c)} J <= sup_{A(eps)} J <=
J_ideal(eps)" and the decomposition "Pi_c := J_ideal(eps) −
sup_{A(c)} J >= 0", with A(eps) defined as "the same class with every
c-slot except the exit-area/eps slot (and the class-defining
regularity) removed"; vs §2 WHY-THEOREM* clause (a) ("(H3) is an
a-posteriori per-design certification ... the lemma binds
design-by-design conditional on that certificate") and the DC-1
falsifier's own breakout clause ("a rejector that artificially
violates (H3) ... must be ABLE to break the bound").

Reason: DC-1 is proved design-by-design under (H1)-(H5b), and the
author's THEOREM* clause correctly says so; but the DC-2 display then
takes a sup over a CLASS, which requires every member to satisfy the
hypotheses. That requirement is load-bearing, not cosmetic: the
author's own G-analysis breaks without (H3). Analytic counter-state
(executable-counterexample preference; symbolic, no new number of
record): drop (H3) and admit an exit cell with u = u_x -> 0+ at speed
q in (c*, lambda) (near-tangential crossing flow); then G(q, u) ->
p(q) > p(lambda) since p is strictly decreasing in q along the
isentrope and q < lambda — the pointwise Lagrangian bound of step (ii)
fails, and nothing in the proof bounds C_exit for a field carrying
such cells (high-pressure slow patches push on the exit disk; this
confirms, analytically, exactly the H3-breakout the DC-1 falsifier
demands be possible). Consequently, IF the (P)-admissible class A(c)
of M0 D2.6 (read at :250-266 — the c-vector is geometric; per-cell
exit axial supersonicity is not one of its slots, it is the S1
margin machinery's a-posteriori certificate) contains any member not
certifiable under (H3), then "sup_{A(eps)} J <= J_ideal(eps)" and
"Pi_c >= 0" are UNPROVEN as stated, and the chain's consequence
"delta >= sup_{A(c)} J − J[S*]" — consumed downstream by DC-6's
"delta^c -> delta_true" degeneration — can fail. The parenthetical
"(and the class-defining regularity)" is doing this entire job
silently; a THEOREM*-class display may not leave it implicit.

Failure/consequence: the decomposition delta = Pi_c + delta_true with
both parts nonnegative — the semantic backbone of the carrier — holds
only over the certified subclass, and nothing in DC-2's text says so.
Repair (one clause, no conclusion moves for any certified row): define
W_cert = the (H1)-(H5b) subclass of §1 and state DC-2's sups over
A(c) ∩ W_cert and A(eps) ∩ W_cert, carrying DC-1's THEOREM*
conditionality explicitly into DC-2's statement (and into the DC-2
falsifier, whose "exhibit S in A(c) with J[S] > J_ideal(eps)" must
read "S in A(c) ∩ W_cert" — an uncertified exhibit breaks nothing).
delta := J_ideal − J[S*] >= 0 for the certified S* is untouched.

### MIN-DELTACARRIER-4 [CONTENT-OBJECTION] — Pa-convention scope
mismatch: the lemma's (H4) demands Pa > 0, the engine's only existing
certified objective is the VACUUM one, and no carrier hypothesis pins
the convention — the third [OBJ-DOM] axis (Pa) is unconsumed

Anchor: author file §1 (H4) ("Constant ambient Pa > 0; objective =
per-phase wall gauge thrust"), §1 J_ideal definition (C_exit^id
carries −Pa), §6 DC-5(b) hypothesis line ("same eps, same thermo
leaf/tables, same Sauer IVL/mdot — printed in the Verdict row") vs
phaseD_minor_objdom.md OBJDOM-3(b) + OBJDOM-4 ground 4 (of record: the
coded objective is the VACUUM objective, "no Pa term exists anywhere",
audit verifier note :519 / advisory folded precision (iv); the interim
scoping covers value AND gradient AND Pa — precision (v)).

Reason: two defects, one seam. (i) Scope: as stated the lemma does not
cover the objective the executed carrier actually computes — (H4)'s
strict Pa > 0 excludes the vacuum functional that produced every
existing certified J[S*] and the twin numbers DC-5(a) quotes
(4.4938e-3 lip/eps residual). The proof nowhere uses Pa > 0 (Pa
enters Phi and p(lambda) − Pa symmetrically and cancels in the
comparison), so the repair is literally Pa >= 0 — but a THEOREM*
statement whose hypothesis excludes its only intended instances is a
content defect, not a typo (precedent: MIN-OBJDOM-1, definitional
mismatch in a THEOREM-class statement = content). (ii) Carrier: the
DC-5(b) printed hypothesis line reproduces advisory §3.2.5 verbatim
(eps / thermo / IVL-mdot) and omits the Pa convention. Gauge-vs-vacuum
wall integrals differ by Pa·Int_wall n_x dA — a class-constant under
fixed eps and shared IVL (so the argmax is untouched), but a delta row
computed with a gauge ceiling against a vacuum J[S*] (or vice versa)
is numerically wrong by exactly that constant. Sign not asserted here
(R5); the defect is the un-pinned convention, either mixing direction
is an error.

Failure/consequence: a shipped (value, delta) row mixing conventions
carries a silent constant offset; and the minor (c) draft, which is
the designated consumer of the [OBJ-DOM] seam, consumes only the
domain axis and leaves the Pa axis of the three-axis interim scoping
dangling. Repair: (H4) restated with Pa >= 0 (vacuum = Pa = 0 case,
proof unchanged, one line); DC-5(b) hypothesis line gains "same Pa
convention (gauge/vacuum), declared" alongside the domain-disposition
entry of finding 1.

### MIN-DELTACARRIER-5 [WORDING] — the synthesis-mandated scope
sentence (fixed-interface class; constriction/choking = class-changing)
is absent, and its named landing site is THIS draft

Anchor: SYNTHESIS_nozzle_rde_arrivals.md (e).3 (:413-423, read
[FULL]): "the papers supply the honest scope sentence: the largest
published performance lever lives outside the class the lemma prices
... Landing: scope-context note on the minor (c) draft"; G-12
(:280-283, "scope context for the lemma's delta semantics, no
statement change"). The author file contains no such sentence: its
declared scope limits are bell-only/annular-plug (H2 parenthetical,
§2 clause (b)) and the (H1) data contract — (H1) IS the
fixed-interface premise doing the exclusion, but the honest scope
note is nowhere stated, and the §9 [T-DCRX] landing text does not
carry it.

Reason: the synthesis (confirm-verified, [ADV]) names this draft as
the landing site; per the artifact-connectedness rule the note must
ride the lemma into M0, or the graft orphans. WORDING, not content:
G-12 says "no statement change" and no statement of the draft is
false — every DC statement is conditional on (H1)-(H2), which
excludes class-changing moves by hypothesis. Repair (one sentence in
§9's [T-DCRX] text, [ADV] provenance, CT-6-clean — no paper number
enters any bound): "Scope [ADV, synthesis (e).3/G-12]:
J_ideal(eps) prices designs INSIDE the fixed-interface data class
(H1); constriction/choking/exit-area moves that rewrite the chamber
state are class-changing and outside what delta prices — the largest
published performance lever lives there; pricing it is CFD-1's core."

### MIN-DELTACARRIER-6 [WORDING] — "with equality for the uniform
axially-aligned exit" reads as in-class attainment; the ceiling may be
strict on the class

Anchor: author file §2 STATEMENT ("with equality for the uniform
axially-aligned exit at M_e(eps)") and §4 DC-3(c) ("J_ideal_cycle(eps)
= B_fam({eps}) restricted to the uniform-exit relaxation").

Reason: equality is attained by the uniform aligned exit STATE (the
relaxation's maximizer), which no finite-length class member need
realize; as worded a reader can take J_ideal(eps) as attained in W,
i.e. sup_W J = J_ideal, which is not proven (and DC-3(c)'s own hedge
"restricted to the uniform-exit relaxation" concedes B_fam({eps}) <=
J_ideal_cycle may be strict — an "=" sign carrying a "restricted to"
qualifier is not an identity). No conclusion moves (the lemma is a
ceiling; ceilings need no attainment). Repair: "with equality attained
by the uniform axially-aligned exit state (the relaxation maximizer;
in-class attainment not claimed)" and in DC-3(c) replace "=" with
"<=, with equality exactly on the uniform-exit relaxation".

### MIN-DELTACARRIER-7 [NOTE] — DC-4's rung is dormant today: per the
consumed T7(c) text, ALL executed instances live in regime 2, whose
multipliers DC-4 itself rules inadmissible

Anchor: author file §5 regime clause vs rde_nozzle_P1_sections_5_7.md
:79-84 (read [FULL]): "K = {point} (fixed-(eps, L)) => ... lambda =
components of D with free sign (the fixed-eps bookkeeping in which all
executed instances live)". Reason: the regime gate is correct and
well-drawn (verified against the T7(c) cone form, KT2015 (2.10)), but
its consequence is unstated: no existing run produces admissible
(unilateral-regime) multipliers, so [DC-F2-3] is contingent on
(P)-as-posed capped runs existing first. One sentence in §5 or at
[DC-F2-3] spares the F2 executor a dead-end; expected outcome
unchanged. NOTE (no statement is wrong; the gate correctly rejects
what exists).

### MIN-DELTACARRIER-8 [NOTE] — (H2b)'s per-design check is assigned
to no one

Anchor: author file §1 (H2b) ("[For eps > 1 this holds up to the
Sauer-vs-1D mdot correction; checkable per design.]") vs §8 duties
[DC-F2-1..5] and §6 DC-5(b). Reason: (H2b) underwrites existence/
uniqueness of lambda — load-bearing for everything — and is declared
"checkable per design", but no F2 duty executes the check and the
printed hypothesis line does not carry it ((H3) by contrast has a
named owner, the S1 margin machinery, and a breakout test in
[DC-F2-5]). Repair: one clause adding the (H2b) check (mdot/A_e vs
rho* c* from the same tables) to [DC-F2-5]'s rejector or to the
DC-5(b) printed line. NOTE: trivially satisfied at sane eps, but an
unowned load-bearing hypothesis is the S-CERT defect pattern.

## VERIFIED-CLEAN (checked, no finding — listed so the judge sees the
coverage; all in THIS window)

- DC-1 PROOF, full symbol-by-symbol re-derivation: d(rho q)/dq =
  rho(1 − M^2) (existence/uniqueness of lambda under (H2b)); the
  momentum-theorem decomposition (i) with Pa closing over the closed
  surface and axis nullity; linearity step C_exit − lambda·mdot =
  Int Phi; convexity in u (ii.a); A'(q) = rho(q − lambda)(1 − M^2)
  re-derived from dp = −rho q dq, drho = −(rho q/c^2) dq — matches;
  branch max A(lambda) = p(lambda) with both endpoint checks; (ii.c)
  case split exhaustive, algebra B − A = rho(c − q)(c + q − lambda)
  correct, second case correctly closes via q > c (H3) and
  gamma_s >= 1 (H5b, = gamma for ideal gas, table-checkable as
  claimed); assembly equality at the uniform exit exact. The bound
  SURVIVES; no analytic counterexample exists inside (H1)-(H5b) (my
  finding-3 counter-state requires violating (H3), exactly as the
  author's falsifier demands).
- Advisory §3.2 corrections 1-5 (read [FULL] at :213-250): all five
  consumed faithfully — proof obligation is the relaxation lemma (no
  dF/dA truncation argument anywhere in DC-1, correction 1
  discharged as claimed); delta wording (correction 2) = DC-2
  SEMANTIC RULE verbatim; ceiling qualifications + 4.4938e-3
  (correction 3) = DC-5(a); sequencing (correction 4) = (H6) modulo
  findings 1-2; hypothesis list (correction 5) = DC-5(b) modulo
  finding 4.
- Registry rows: pipeline:delta-carrier-F2-entry (:292-300) and
  bound-ladder:constraint-aware-rungs-missing (:1669-1677) both read
  [FULL]; author's quotes of semantics, owner, and the two named
  refinements are faithful; the B1^c/Rao/Guderley-Armitage/Kraiko and
  KKT-rung descriptions match the row text; T3-collapse clause (DC-6)
  matches "T3's collapse is precisely attainment of B1^c under
  pressure similarity".
- DC-2 inclusion logic A(c) ⊆ A(eps) and the last ">= 0" (S* in
  A(c)): sound modulo finding 3's class restriction; the SEMANTIC
  RULE and the user-catch loose-direction declaration match the row
  and advisory verbatim.
- DC-3: (a) pointwise-domination argument correctly avoids any
  sup/integral interchange; (b) monotonicity direction correct
  (larger C = more constraints = smaller sup); B1^c <= J_ideal(eps)
  chain correct given DC-1; (V1)/(V2) valve treatment compliant with
  the brief's LOAD-CLASS split and AG-1.
- DC-4 inequality: one-line weak duality verified (each penalty term
  >= 0 on A(c)); regime clause verified against
  rde_nozzle_P1_sections_5_7.md:72-94 [FULL] — free-sign regime-2
  exclusion and KT2015 (2.10) sign+complementarity faithfully
  consumed (see finding 7 for the unstated dormancy).
- DC-5(a) direction logic: under-estimated ceiling => under-stated
  delta => anti-conservative; upper-band-edge rule is the
  conservative choice. Correct.
- DC-6: degeneration logic sound as SCHEMA (attainment of B1^c by a
  phase-shared design collapses the L-price), correctly consumes
  registry/M0 without re-derivation.
- Brief MINORS (c) mandate coverage: lemma with rigor class + M0 site
  (§9), delta semantics of record, composition with BOTH named rungs,
  derivable-now halves derived, F2 rungs left as named duties
  ([DC-F2-1..5] with owners/triggers), LOAD-CLASS declaration
  compliant. Complete.
- CT-6 evidence rule: no number from the four nozzle papers appears
  anywhere in the author file (checked; the only measured numbers are
  program record numbers with sources). Compliant; finding 5's repair
  sentence keeps it so.
- Addendum_c4 bearing: items (b)/(e) do not touch this minor; item
  (c) binds the forchetta table, not this file — no obligation
  imported. Checked for bearing, none found.
- §10 read-depth + PAPERS NEEDED (none blocking): legitimate — the
  proof is self-contained from the ratified proof obligation; checked
  the brief's arrivals bearing on (c): the four nozzle papers feed
  scope context only ((e).3, finding 5), no load-bearing paper claim.
- M0 anchors spot-checked: D2.6 c-vector at :250-266 (geometric
  slots, PROXY note) and the (iv) ladder at :349-356 (delta = B −
  J[S*], sonic-capped J_ideal a named member) — consistent with the
  author's use; OP-0 sharpening block confirmed in the :1268+ region
  for the §9 landing adjacency.

## SEQUENCING-DUTY VERDICT (SR-C4-9, explicit)

MIN-OBJDOM-3 applied to the author's hypothesis list: the list DOES
NOT SURVIVE as written — (H6) instantiates the killed same-convention
hypothesis and its ship-gate admits an unlicensed fix-B branch
(findings 1-2). The repair is named and local: (H6') two-branch
sufficient condition (fix-A-both-sides OR net-two-wall-panel band with
anti-conservative direction declared, folded into the DC-5(a)
upper-edge rule), ship-gate re-pinned to [OBJ-DOM-IMPL]-or-band,
DC-5(b) line extended (domain disposition + Pa convention). With
(H6') substituted, DC-1/DC-2's proofs are untouched (neither uses
(H6); it is carrier-shipping hypothesis, not proof hypothesis) — the
lemma survives, the carrier contract as drafted does not.

## READ-DEPTH DECLARATION

All internal, no papers consulted (none needed: no paper claim is
load-bearing for this refutation; CT-6 kept):
- phaseD_minor_deltacarrier.md [FULL] (whole file, target);
- BRIEF_blocco2_phaseD.md MINORS + JUDGE sections [FULL] (:150-210);
- BRIEF_blocco2_phaseD_addendum_c4.md [FULL] (whole file);
- phaseD_minor_objdom.md [FULL] (whole file);
- refute_minor_objdom.md [FULL] (whole file; MIN-OBJDOM-3 applied);
- docs/findings_registry.yaml :285-309, :1660-1678 [FULL];
- validation/ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md
  :200-279 [FULL] (§3.2 whole);
- docs/rde_nozzle_P1_sections_5_7.md :70-99 [FULL slice, T7(c)];
- docs/rde_nozzle_MASTER.md :248-269, :345-359, OP-0 block location
  grep-verified [targeted slices];
- SYNTHESIS_nozzle_rde_arrivals.md (e).3 :413-423, G-12 :280-283,
  CT-1/CT-8 slices [targeted, confirm-read].

PAPERS NEEDED: (empty)

## SUMMARY FOR THE JUDGE

4 CONTENT-OBJECTION (MIN-DELTACARRIER-1 (H6) fails MIN-OBJDOM-3, the
binding sequencing finding — repair (H6') named; MIN-DELTACARRIER-2
ship-gate's unlicensed fix-B branch under a false "verbatim" flag;
MIN-DELTACARRIER-3 DC-2's class-level sup needs the certified-subclass
restriction, backed by an analytic H3-off counter-state that confirms
the author's own breakout falsifier; MIN-DELTACARRIER-4 Pa-convention
scope mismatch, third [OBJ-DOM] axis unconsumed), 2 WORDING, 2 NOTE.
The DC-1 proof itself was re-derived in full and SURVIVES; DC-2's
decomposition and the rung composition survive under the named
one-clause repairs; no shipped number moves (no delta row exists yet —
that is the row's own finding). All four content objections are
carrier-contract and hypothesis-bookkeeping defects with local, named
repairs — none kills the lemma; each, unrepaired, ships a wrong or
unlicensed delta row. Escalation per the standing rule (any surviving
content objection => full form) is the judge's call.
