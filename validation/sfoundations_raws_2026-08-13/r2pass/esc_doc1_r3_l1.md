# ESCALATION REFUTATION — DOC-1 E-1/E-2 repairs, until-dry ROUND 3, lens l1
# (gas dynamics / physics, RH algebra, counterexamples)

Date: 2026-08-19. Target: `phaseD/phaseD_stop_proof.md` AT REVISION 7 —
ONLY the escalation-repair text for legs 3 and 5 named by the NEWEST
revision-log entries (the §13 REVISION 7 block, lines 3447-3670, and
the body passages it edits — all on the G8/r2 accounting row of leg 5:
the DOMAIN-COMPLETED condition of record + three itemized theta
consumptions, lines 2122-2150; the quadruple pin + general-member
clause + WRITTEN sufficiency assembly, lines 2151-2193; the AUD-cp
revision-7 additions, lines 2239-2256; the RE-CALIBRATED falsifier
parenthetical, lines 2257-2283; the grant head, lines 2284-2293; the
four propagation carriers: header audit line 88-101, honest status
line 2338-2355, §9 gamma table 2546-2576, §13 revision-6 entries'
SUPERSEDED-IN-PART note 3365-3386. Leg 3 received ZERO revision-7
edits — its dry-at-both-lenses status is TESTED at this lens in its
own section below, per the brief's "legs 3 and 5" scope).

ROUND/LENS PLACEMENT, DECLARED: revision 7 consumed the round-3 l0
refutation (`esc_doc1_r3_l0.md`, E3L0-1/E3L0-2) and the round-2 l1
completion (`esc_doc1_r2_l1.md`, ER2L1-1); its honest-residue item (1)
declares the revision-7 repairs "themselves UNADJUDICATED and await
the next escalation-refutation round (both lenses, per the restored
two-lens coverage)". This document is the lens-l1 half of that round.
Output file `esc_doc1_r3_l1.md` — the round-3 l1 slot, previously
empty on disk; no existing artifact is overwritten.

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 rows L0-1/L1-1, L0-2,
L1-2 and §4(c) E-1/E-2 (the standing escalation specs); full objection
texts `refute_r2batch_l0.md` / `refute_r2batch_l1.md` at the attacked
legs; ALL prior escalation rounds `esc_doc1_r1_l0.md` (EL0-1..EL0-4),
`esc_doc1_r1_l1.md` (ESC1-F1/F2), `esc_doc1_r2_l0.md` (E2L0-1/E2L0-2),
`esc_doc1_r2_l1.md` (ER2L1-1 — my lens's own round-2 record),
`esc_doc1_r3_l0.md` (E3L0-1/E3L0-2). Both duties executed: (a)
derivation-level attack on the revision-7 repair text; (b)
verification that the revision-7 repairs DISCHARGE the round-3
sustained findings they answer (E3L0-1, ER2L1-1, E3L0-2) and that the
standing dispositions hold at revision 7. Per the target's own
honest-residue item (2) (spec-seeding pattern, four named instances),
the revision-7 text was attacked AS repair-spec-derived text.

DEDUP REGISTER (dispositioned objections NOT re-raised): L0-1/L1-1,
L0-2, L1-2 (r2-batch, consumed revisions 4/5); EL0-1==ESC1-F1, EL0-2,
EL0-3==ESC1-F2, EL0-4 (round 1, consumed revision 5); E2L0-1, E2L0-2
(round 2, consumed revision 6, dispositions verified at both lenses);
E3L0-1, ER2L1-1, E3L0-2 (round 3 / l1-round-2, consumed revision 7,
adequacy examined below). All three findings below attack REVISION-7
text (or a revision-6 clause whose truth conditions revision 7
CHANGED under it) — zero prior adversarial coverage — and each
declares its distinction from every ID above. Every attacked passage:
verbatim quote + attack + class in {BREAKS-THE-LEG, REPAIR-NEEDED,
AMENDMENT}. Every examined passage not broken: CONFIRMED with the
strongest attack tried.

Finding IDs: ER3L1-1, ER3L1-2, ER3L1-3. Line numbers are of the
revision-7 file.

==============================================================================
## LEG 5 (E-2) — the revision-7 quadruple pin, written assembly, and
## hull-theta domain completion

### 5.1 The written sufficiency assembly — CONFIRMED (the mathematical
### heart of the revision-7 delivery; attacked hardest, survives)

Quote (lines 2175-2193): "The assembly, written: given the condition
of record, at a rest state the W-Hessian of -rho S is BLOCK-DIAGONAL —
the (rho, E) block is tau B^T Hess(-s) B (the (m2) perspective
congruence run in the sufficiency direction; strict s-concavity
transfers to strict slice positivity because B is invertible), the
momentum block is (1/(rho theta)) I > 0 by the hull-theta clause
(d^2(-rho s)/dm_i dm_j = (s_eps/rho) delta_ij = delta_ij/(rho theta)
at m = 0), and the m-(rho, E) cross terms VANISH at m = 0 (each
carries a factor m_i); boost affinity transports positive-definiteness
to all velocities by congruence; continuity of Hess_W E (EOS C^2 — a
§1-implicit consumption, now stated) plus compactness of the hull's
state image give the uniform lower eigenvalue bound lambda_min > 0,
and the Bregman double integral gives item (i) with c = lambda_min/2."

Strongest attacks tried at my lens, all failed:

(a) *Sign and value of the momentum block, direct differentiation*
(hunting a sign slip in the one line nobody had computed of record
before this loop): with eta = -rho s(1/rho, eps), eps = E_tot/rho -
|m|^2/(2 rho^2): d eta/dm_i = -rho s_eps (-m_i/rho^2) =
+(s_eps/rho) m_i, so d^2 eta/dm_i dm_j|_{m=0} = (s_eps/rho) delta_ij
= delta_ij/(rho theta) (s_eps = 1/theta). Sign POSITIVE exactly as
printed, positive iff theta > 0 — the hull-theta clause is consumed at
precisely the printed site. Checks.

(b) *Exactness of the (rho, E)-block congruence* (the strongest
attack: hunt an uncontrolled remainder in "tau B^T Hess(-s) B"): full
second-derivative computation of eta(rho, E_tot) = rho F(1/rho,
E_tot/rho), F = -s, at m = 0: eta_rhorho = tau (tau, eps) HessF
(tau, eps)^T, eta_rhoE = -tau (tau F_taueps + eps F_epseps), eta_EE =
tau F_epseps — assembled, EXACTLY tau B^T HessF B with
B = [[-tau, 0], [-eps, 1]], det B = -tau != 0. No remainder, no
first-order F-terms survive in the Hessian. The congruence is an
identity, not an approximation. Checks.

(c) *Strictness leak in the Legendre transfer* ("strict s-concavity
transfers to strict slice positivity"): I closed this with an EXACT
congruence the document does not print but its clause implies: for any
straight line gamma(t) in (v, S), s(v(t), e(gamma(t))) = S(t) is
affine in t, and twice differentiating gives (DPhi gamma')^T Hess s
(DPhi gamma') = -(1/theta) (gamma'^T Hess e gamma') with
Phi(v, S) = (v, e(v, S)), DPhi invertible for theta != 0. Hence
Hess e(v, S) PD + theta > 0 <=> Hess s(v, eps) strictly ND, pointwise
and rank-faithfully — no strictness can leak in either direction. My
round-2 step (1) is thereby re-verified in a sharper form. Checks.

(d) *Boost transport vs the condition's domain* (a genuinely new
attack surface opened by the revision-7 phrasing): the boost
congruence Hess_W E(W) = A^T Hess_W E(A_{-u} W) A needs PD at the
REST state A_{-u} W, which need not lie in the hull as a W-point. But
A_{-u} W has the SAME (rho, eps), hence the SAME (v, S), as W — and
the condition of record is imposed on "(the (v, S)-image of) the
comparison-segment hull", i.e. exactly on thermodynamic states, which
the boost preserves. The phrasing survives the attack it invites.
Checks.

(e) *Uniformity and the Bregman constant*: hull compact (union of
segments between compact endpoint sets, or its convex hull —
Caratheodory in R^5), Hess_W E continuous on it (EOS C^2 + theta != 0
+ chart defined — the definedness presupposition is ER3L1-2 below,
carried there), pointwise PD by (a)-(d) => lambda_min > 0 attained;
E(V|U) = Int_0^1 (1-s) DeltaW^T Hess E(W_s) DeltaW ds >=
(lambda_min/2)|DeltaW|^2. c = lambda_min/2 exact. Checks.

The assembly matches my own round-2 pen-grade chain (esc_doc1_r2_l1.md
§5.1 steps (1)-(4)) clause for clause, with the two additions revision
7 owed (hull-theta at the m-block; EOS C^2 stated). The revision-7
block's claim that my steps are "the adversarial check of record on
the written assembly's content" is fair AND correctly does not count
as adjudication of the written text (honest residue (1) declares it
unadjudicated — this section is that adjudication at my lens).

### 5.2 The quadruple pin and general-member clause — **OBJECTION
### ER3L1-1, AMENDMENT** (one clause; the pin itself is CONFIRMED)

Quote (lines 2164-2174): "item (i) is granted FOR THE CERTIFIED
QUADRUPLE g(S) = S, E = -rho S — the member §4 actually consumes (H7',
'Take the certified entropy quadruple g(S) = S'; the kill chains
(m1)-(m3) also instantiate it). For a general Harten member the
g-condition enters ADDITIONALLY (the kept ideal-gas iff is its
instance; its abstract-EOS form is unstated and NOT needed — one
convex member suffices for the device); at g = S it reads 0 < 1/c_v,
i.e. c_v > 0, which the strict pair already contains — exactly why
the printed condition self-suffices at the certified quadruple and at
no strongly-convex g."

Echo site (§13 revision-7 block, lines 3486-3488): "at g = S the
g-condition reads c_v > 0, contained in the strict pair."

CONFIRMED first, with the strongest attacks tried: (i) *consumption
audit of the pin* — line 1175 ("Take the certified entropy quadruple
g(S) = S (H7')"), line 1422 ("(EI-x) in D' for the certified
g(S) = S"), line 799 ("instance used in §4 is g(S) = S (H7')"): every
§4 consumption runs at g = S; the pin matches use exactly, and my own
round-2 witness family g = exp(lambda S) is correctly fenced out by
it. (ii) *"at no strongly-convex g"* — for any g with g''(S_0) > 0 at
an attained S_0, an ideal gas with c_v > g'(S_0)/g''(S_0) is in-class
and breaks -rho g(S) convexity by the kept iff: the universal negative
is right. (iii) *"one convex member suffices for the device"* — the
Dafermos machinery consumes one entropy/entropy-flux quadruple, the
H7' one: checks. (iv) *"0 < 1/c_v"* at g = S: g'' = 0, g' = 1,
g''/g' = 0 < 1/c_v <=> c_v > 0: checks.

Attack (the surviving clause): "**which the strict pair already
contains**" is FALSE as printed. c_v = theta/e_SS (the row's own
identity, line 2148). The strict pair (e_vv > 0 AND
e_vv e_SS > (e_vS)^2) delivers e_SS > 0 — and then c_v > 0 iff
theta > 0, which is NOT in the strict pair: it is the OTHER member of
the condition of record, the hull-theta clause. In-class witness,
riding the E3L0-2 mechanism already of record: the quadratic patch
with a0 large NEGATIVE (theta = a0 + a1 v + bS < 0 on the patch,
e0'' b > a1^2 strict) satisfies the strict pair everywhere on the
patch with c_v = theta/e_SS < 0 — the strict pair does not contain
c_v > 0 any more than it contains theta > 0 (both first-order data;
the row's own line 2136-2137 sentence "theta is FIRST-order EOS data
no Hessian condition controls" cuts against its own attribution two
sentences later). The CONCLUSION ("the printed condition self-suffices
at the certified quadruple") is TRUE — the printed condition of record
conjoins hull-theta, and hull-theta + strict pair do contain c_v > 0
on the hull — the ATTRIBUTION to the strict pair alone is what is
wrong, at both sites (body + §13 echo).

Class: **AMENDMENT** — benign reading available and in force (the
hull-theta clause sits in the same condition of record two lines up;
no consumer reads the strict pair in isolation), no statement, label,
or route-level conclusion moves. Repair, one phrase at two sites:
"which the condition of record (strict pair + hull-theta) already
contains" — or "which e_SS > 0 gives GIVEN the hull-theta clause".

PROVENANCE, declared per the standing lesson (honest residue (2)
names four spec-seeded instances and mandates attacking revision-7
text as repair-spec-derived): the clause was transplanted VERBATIM
from MY OWN round-2 repair spec (esc_doc1_r2_l1.md §5.1: "at g = S it
reduces to c_v > 0, which the strict pair already contains") — whose
in-body justification "(e_SS > 0 => c_v = theta/e_SS > 0)" silently
consumed theta > 0 at a time when the hull-theta clause did not yet
exist (E3L0-2 landed in the same window). The FIFTH consecutive
spec-seeded defect on this row, this one seeded by this refuter's own
lens — repair-spec text is not exempt, including mine.

DEDUP DECLARATION: not a re-raise of E3L0-2 (theta as a condition
MEMBER — consumed; this prices a false ATTRIBUTION between the two
members of the delivered condition, text that did not exist before
revision 7); not a re-raise of ER2L1-1 (quadruple scope — delivered);
not of E2L0-1/EL0-3/L1-2 (Hessian-side naming ladder). The revision-6
shadow sentence at line 2148 ("e_SS > 0 (= c_v > 0 via c_v =
theta/e_SS ...) then FOLLOWS from the strict pair") is NOT attacked:
there the identity is printed with its theta dependence visible and
was two-lens confirmed at round 3 l0 (5.3(a)); the revision-7 clause
drops the visible dependence and asserts containment — that is the
delta.

### 5.3 The hull-theta condition of record and the "(v, S)-image"
### parenthetical — **OBJECTION ER3L1-2, AMENDMENT**

Quote 1 (condition of record, lines 2143-2147): "theta > 0 AND
Hess e(v, S) positive DEFINITE on (the (v, S)-image of) the
comparison-segment hull, i.e. the hull-theta clause PLUS the strict
pair e_vv > 0 (= c^2 > 0, already a §1 pin) AND the strict Grueneisen
cross-term bound e_vv e_SS > (e_vS)^2 (unpinned by §1)".

Quote 2 (the chart itemization, lines 2129-2131): "the chart
W -> (v, S) inverts eps = e(v, S) in S and needs e_S = theta != 0
along the hull before any Hessian can be read there".

Quote 3 (§1 gas model, lines 195-198): "abstract EOS p = p(rho, S),
e = e(rho, S), Gibbs closure e_rho = p/rho^2, e_S = theta
(temperature), c^2 = p_rho|_S > 0 and theta > 0 on the state region
of interest."

Attack (derivation level — the domain ladder has one more rung).
theta > 0 licenses the chart's UNIQUENESS (monotone inversion of
eps = e(v, S) in S), not its EXISTENCE: for a hull state W_s, a
(v, S)-preimage exists only if eps_s lies in the RANGE of
e(v_s, . ) over the EOS's S-domain — a surjectivity condition no
printed line delivers. §1 (Quote 3) pins neither the EOS's (v, S)
domain nor the range of e; and the row itself has ALREADY accepted
partially-defined EOS as in-class — the (m2)/(m3) witnesses of record
are "quadratic e(v, S) PATCH" constructions ("a0 large", compact
patch). For such an in-class EOS, take endpoints U, V in K with a
thin S-band [S_-, S_+]: along a W-segment eps_s is NOT the linear
interpolation of the endpoint eps values (eps is nonlinear in W), and
mid-segment eps_s can exit the band [e(v_s, S_-), e(v_s, S_+)]. At
such W_s: S(W_s) is UNDEFINED, E = -rho S is undefined, the Bregman
integral of item (i) traverses undefined territory — while the
printed condition of record, quantified over "(the (v, S)-image of)
the comparison-segment hull", is SATISFIED on the (partial) image,
vacuously omitting exactly the states where the grant dies. The
assembly's "compactness of the hull's STATE IMAGE" and "continuity of
Hess_W E" (5.1(e)) silently consume the same totality. Three
consumptions were itemized by the E3L0-2 repair (chart monotonicity,
Legendre, m-block); the ZEROTH one — the chart's totality, S(W)
DEFINED hull-wide — is still unwritten.

The asymmetry that makes this a genuine accounting item and not
pedantry: at the standing gamma(T) closure the row DOES price exactly
this ("hull evaluability inside the tabulated range is the
table-domain precondition already priced once for all consumers in
this row", lines 2251-2254 — and my own round-2 5.4(c) verified that
pricing). The abstract-EOS side of the SAME condition carries no
counterpart clause. The domain ladder of this row — K (E2L0-2's axis)
-> hull (E3L0-2's axis) -> theta-pin region (E3L0-2) — has the EOS
chart's domain as its outermost rung, and the revision-7 parenthetical
stopped one rung short.

Class: **AMENDMENT**, by the loop's own severity calculus, and NOT
REPAIR-NEEDED like E3L0-2, for a stated reason: "(the (v, S)-image
of) X" in standard mathematical usage PRESUPPOSES X ⊆ dom(chart) — a
benign reading is genuinely available (writing f(A) asserts A in the
domain of f), unlike E3L0-2's theta, where no reading of §1 reached
the hull. Under the presupposition reading the condition is complete
and my patch witness VIOLATES it rather than satisfying it. The
repair makes the presupposition explicit — one clause: "with S(W)
defined on the whole hull (the chart's totality — the abstract-EOS
counterpart of the table-domain precondition priced at the closure)",
either as a stated precondition of the condition of record or as its
zeroth member. No statement, label, or route-level conclusion moves;
at the closure the clause is already priced, so the abstract-EOS-only
scoping survives — and the repair once more (fifth time) STRENGTHENS
the no-viable-abstract-EOS-route conclusion.

PROVENANCE, declared: "(the (v, S)-image of)" was transplanted
VERBATIM from the round-3 l0 repair spec (esc_doc1_r3_l0.md §5.2
repair: "on (the (v, S)-image of) the comparison-segment hull") —
the spec introduced the presupposition without stating it; sixth
spec-seeded instance on this row, per the pattern the target itself
names.

DEDUP DECLARATION: not a re-raise of E3L0-2 — that priced theta on
the hull (monotonicity/Legendre/m-block: the chart's INJECTIVITY
side) and is DISCHARGED as delivered (5.5 below); this prices the
chart's TOTALITY (existence of the preimage), a hypothesis the
delivered parenthetical newly presupposes — revision-7 text. Not a
re-raise of E2L0-2 (falsifier restoration domain — discharged) or of
my own ER2L1-1 round-2 5.4(c) (which verified the CLOSURE's
evaluability pricing; this is its missing abstract-EOS counterpart).

### 5.4 The re-calibrated falsifier parenthetical and its consequent —
### **OBJECTION ER3L1-3, AMENDMENT** (parenthetical itself CONFIRMED)

Quote (lines 2268-2283): "derive joint s-concavity IN THE STRICT FORM
on the comparison-segment hull (equivalently: wherever the §1 pins
hold, PROVIDED the pins are read on the whole EOS domain — else on
the hull itself; parenthetical RE-CALIBRATED in revision 7 per E3L0-2:
§1 pins theta only 'on the state region of interest', and no printed
line places the hull inside that region, so the unconditioned
'equivalently' retained residual false-restoration power on the
domain — a pins-only derivation concludes only where the pins hold)
from Gibbs closure + c^2 > 0 + theta > 0 ALONE, with no K-geometry
input — THAT kills the condition-claim and restores the unconditional
grant".

CONFIRMED first: the delivered parenthetical does exactly what the
E3L0-2 spec demanded — the "PROVIDED ... else on the hull itself"
split closes the hull-⊆-pin-region equivalence gap (strongest attack
tried: construct a pins-only derivation that fires under the
"equivalently" reading while leaving hull states uncovered — under
the delivered text it cannot: the else-branch pins the conclusion
domain to the hull itself). Checks.

Attack (the consequent, one clause to its right): "**restores the
unconditional grant**" is now MIS-CALIBRATED against the very
condition revision 7 enlarged. The demanded deliverable is "joint
s-concavity IN THE STRICT FORM" — the HESSIAN member of the
two-member condition of record. The hull-theta member is FIRST-ORDER
data that no concavity derivation controls (the row's own sentence,
lines 2136-2137, in its own voice) — so NO firing of this falsifier
can restore it, except accidentally under the whole-EOS-domain
reading (where the theta pin itself goes hull-wide, modulo ER3L1-2's
totality). Concrete false-restoration mechanism, in the exact form
E2L0-2 was sustained for: a (hypothetical) derivation from Gibbs
closure alone — which holds EOS-wide by definition — concluding
strict s-concavity everywhere would FIRE the falsifier as printed and
"restore the unconditional grant", while item (i) STILL breaks at a
theta < 0 hull state through the negative momentum block
(1/(rho theta)) I — E3L0-2's own consumed mechanism (c), untouched by
any Hessian-side derivation (strict Hess s ND is compatible with
theta < 0: theta = 1/s_eps is first-order data). The falsifier's
firing condition guards the Hessian member; its consequent claims
both members. Revision 7 changed the condition under an unchanged
consequent — a propagation-completeness miss, not a spec-seeded one
(the consequent predates the loop and was accurate at every revision
up to 6, when the condition had only Hessian members).

Class: **AMENDMENT** — auxiliary falsifier text; no proof content,
statement, or label exposed (the r2b-F4/EL0-1/E2L0-2 lineage's exact
class, all sustained AMENDMENT). Repair, one clause: "... THAT kills
the condition-claim and restores the grant's HESSIAN member (the
hull-theta member is first-order data no concavity derivation
controls: it is restored only under the whole-EOS-domain reading of
the pins, never by the derivation itself)".

DEDUP DECLARATION: not a re-raise of E2L0-2 (restoration DOMAIN,
K vs hull — discharged, 5.6c of the l0 round-3 record) nor of E3L0-2
(condition domain + the "equivalently" parenthetical — discharged as
delivered above): both priced WHERE a firing concludes; this prices
WHAT a firing delivers (one member vs two) — a question that could
not exist before revision 7 made the condition two-membered.

### 5.5 The DOMAIN-COMPLETED condition and the three itemized theta
### consumptions — CONFIRMED (modulo ER3L1-2 carried above)

Quote (lines 2127-2143, the E3L0-2 delivery): "DOMAIN-COMPLETED in
revision 7 per E3L0-2 (the transfer from 'Hess e(v, S) PD' to item
(i) consumes theta > 0 AT HULL STATES three separate times — the
chart W -> (v, S) inverts eps = e(v, S) in S and needs e_S = theta
!= 0 along the hull before any Hessian can be read there; the partial
Legendre step above is flagged '(theta > 0)' and runs pointwise where
applied, i.e. hull-wide; and the momentum block of the sufficiency
assembly below is (1/(rho theta)) I, NEGATIVE at a hull state with
theta < 0 even with Hess e(v, S) PD — theta is FIRST-order EOS data
no Hessian condition controls — while §1 pins theta > 0 only 'on the
state region of interest', segments LEAVE K, {theta > 0} is NOT
convex in W (theta composes the non-affine S(W)), and the grant's
convex physical region below carries no theta clause: the consumption
was real, named, and unpinned)".

Strongest attacks tried, all failed: (a) *each itemized consumption
re-derived* — chart monotonicity (theta != 0 for the S-inversion:
checks), Legendre pointwise (my 5.1(c) congruence carries the 1/theta
factor explicitly: checks), m-block sign (my 5.1(a) direct
computation: positive iff theta > 0: checks); (b) *{theta > 0}
W-non-convexity* — theta = e_S(v, S(W)) composes S(W), which is not
affine in W (the row's own mediant/mixing argument for c, verified at
my round 1, runs on the same non-affineness): no convexity rescue
exists; (c) *is the third consumption redundant given the first?* —
no: the chart could be read at boundary/limit states where theta -> 0
keeps monotonicity a.e. while the m-block bound degenerates; the
m-block needs the strict sign uniformly, a separate consumption
correctly itemized. The one residual is the totality presupposition,
carried as ER3L1-2 — the delivery is otherwise complete and exact.

### 5.6 The AUD-cp revision-7 additions — CONFIRMED

Quote (lines 2248-2256): "and the revision-7 hull-theta clause and
quadruple pin are FREE there: theta = T > 0 wherever the closure is
DEFINED (T is the table coordinate; hull evaluability inside the
tabulated range is the table-domain precondition already priced once
for all consumers in this row), and g = S is the certified quadruple
of record — the condition prices the ABSTRACT-EOS accounting only."

Strongest attacks tried, all failed: (a) *theta = T at the closure* —
thermally-perfect gamma(T): e_S = theta is the thermodynamic
temperature = the table coordinate T by the Gibbs closure's own
definition; positive wherever the table is defined. Checks. (b)
*quadruple freeness* — g = S is the H7' certified quadruple; nothing
at the closure re-opens the g-condition. Checks. (c) *push ER3L1-2
through the discharge* (the strongest): the totality gap at the
closure IS the table-domain precondition, and this very sentence
prices it — the closure discharge is airtight, which is exactly why
ER3L1-2 is abstract-EOS-only and AMENDMENT-grade. Attack fails.

### 5.7 Propagation carriers — CONFIRMED (all four verified on disk,
### modulo the source-clause inheritances)

Examined verbatim: header audit line (lines 88-98: "... and
DOMAIN-COMPLETED — theta > 0 on the hull added to the condition,
granted half pinned to the certified quadruple g(S) = S — per
revision 7, E3L0-1/E3L0-2/ER2L1-1"); honest status line (lines
2343-2355: "theta > 0 AND STRICT joint s-concavity ... on the
comparison-segment hull — positive-definite Hess e(v, S), granted
half pinned to the certified quadruple g(S) = S — ... discharged IN
FULL, strict form and hull-theta included, at the standing gamma(T)
closure ... separable s and theta = T > 0 there"); §9 gamma table
(lines 2558-2569: "DOMAIN-COMPLETED — hull-theta clause added, grant
pinned to the certified quadruple g = S — in revision 7 ...
(separable s, strict form automatic, theta = T > 0 free there)"); §13
revision-6 entries' SUPERSEDED-IN-PART note (lines 3365-3386 —
accurate on all three residuals, prior text preserved per the
document's supersession convention). Strongest attack tried: hunt a
stale carrier of the revision-6 theta-free or quadruple-free form —
grep over "strict", "hull", "quadruple", "granted": every surviving
theta-free form sits inside preserved superseded §13 text under a
supersession note or in necessity-direction context; the status
line's "e_SS > 0 = c_v > 0 its necessary scalar shadow" reads under
the hull-theta clause conjoined in the same sentence (the ER3L1-1
defect is at the SOURCE clause's attribution, carried there once, not
per carrier). NO stale carrier of record found. All four carriers
inherit ER3L1-1/2/3 only through the clauses they transcribe.

### 5.8 The revision-7 log block (bookkeeping) — CONFIRMED

Examined (lines 3447-3670) against the two input refutations: the
E3L0-1, ER2L1-1, E3L0-2 consumption entries transcribe the findings
faithfully, including my own ER2L1-1's witness family (g =
exp(lambda S), lambda > 1/c_v, ">= for the degenerate (m3)-style
break" — matches my text), the MERGED-AT-THE-CLAUSE record, and all
three PROVENANCE declarations; the counts ("3 distinct defects across
2 files, 2 REPAIR-NEEDED + 1 AMENDMENT, 0 BREAKS-THE-LEG") are exact;
the ROUND-NUMBER NOTE (fourth off-by-one) is declared and accurate;
the discharge-verdicts section matches both input files' own
discharge sections; "no orphan objection remains in any input file on
disk" verified (every ID in every esc_doc1_r* file has a standing
disposition); the dryness ledger, NO-label-motion claim
(VERDICT_r2pass §4(a): [T-T0P] main already SCHEMA), closed Blocco-2
gate, and honest residues (1)-(4) all check. Strongest attack tried:
the "TWO-LENS coverage at every round" claim — the revision-5 text as
such was never l1-read, but every revision-5 clause that SURVIVED
into revision 6 was covered by my round-2 pass and the superseded
remainder needs no coverage: the claim holds in substance; attack
fails. Also tried: an over-claim hunt on "the l1 refuter's own
pen-grade verification ... is the adversarial check of record on the
written assembly's content" — fair as stated, and the block correctly
does NOT treat it as adjudication of the written text (residue (1)
declares these repairs unadjudicated; this document is the l1 half of
that adjudication).

==============================================================================
## LEG 3 (E-1) — ZERO revision-7 edits; dry-at-both-lenses status
## TESTED at this lens, round 3

Revision 7 names no leg-3 passage; the on-disk leg-3 repair text
((p1)-(p3) core, lines 1186-1226; (EU-x) rider with its two written
consumptions, lines 1226-1248; §13 E-1 falsifier bracket, lines
3051-3058) is verbatim the revision-5 state my round-2 pass covered.
Dedup: EL0-1==ESC1-F1, EL0-2 dispositioned and verified at both
lenses; not re-raised.

Fresh attacks tried on the dry verdict itself (owed under the brief's
"legs 3 and 5" scope), all failed:

(a) *Direction-of-minting / seam attack* (gas-dynamics lens): if the
torus form were primitive and the R_t form derived, the periodic
extension would owe a distributional check across the seams t = kT
(concentrated defect measures at gluing hypersurfaces are exactly how
RH fronts enter this document). The text runs the OTHER direction —
(EI-x) is minted in D'(Omega_march x R_t) and the torus form is
DERIVED by (p1)-(p3) — so no seam term can exist to be dropped.
Attack fails on the printed architecture.

(b) *Representation independence*: the torus pairing is built through
ONE window chi_0; a different admissible window tilde-chi_0 could a
priori give a different value. It cannot: mu >= 0 in D' is a Radon
measure (order argument), and the (p2) unfolding applied AT MEASURE
LEVEL gives <mu, psi chi_0> = Int_{one cell} psi dmu = <mu, psi
tilde-chi_0> for any admissible window — and the derived torus form
only ever asserts the sign against each torus test, for which one
representation suffices. Attack fails.

(c) *Partition-nonnegativity convention*: (p1)'s sign claim consumes
chi_0 >= 0, which "partition of unity subordinate to ..." supplies by
standard convention; the (p2)/(p3) identities are sign-free. No
loophole. Attack fails.

(d) *Flux integrability at the rider* (my lens's residual duty): the
d_t flux W(M) composed with V in L^inf(K) is L^inf and T-periodic;
(p2) needs T-periodic L^1_loc — met with room (re-verified; my
round-2 3.1(b) chain unchanged by revision 7).

**LEG 3 remains DRY at lens l1 at round 3** — with this pass the
leg-3 thread has zero sustained findings at both lenses for two
consecutive l1 rounds and three l0 rounds.

==============================================================================
## §D DISCHARGE VERDICTS (round-3 sustained findings vs the
## revision-7 repairs; standing dispositions re-verified)

- **E3L0-1 (REPAIR-NEEDED): DISCHARGED AS SPECIFIED, with the
  ER3L1-1 residual in the delivered clause** — both demanded elements
  landed and are verified at pen grade: the quadruple pin with the
  general-member clause (5.2: consumption audit at lines 1175/1422/
  799; the kept ideal-gas iff correctly re-scoped as the g-condition's
  instance) and the WRITTEN sufficiency assembly (5.1: m-block sign by
  direct differentiation, exact congruence, strictness-tight Legendre
  transfer, boost-image membership, uniform Bregman constant — every
  clause checks). The disposition fails ONLY at the transplanted
  attribution "which the strict pair already contains" (ER3L1-1,
  seeded by MY OWN round-2 spec) and nowhere else.
- **ER2L1-1 (AMENDMENT, my lens's own): DISCHARGED** — the scoping
  clause is delivered merged with E3L0-1's repair, the written
  assembly matches my §5.1 steps (1)-(4) clause for clause, and my
  witness family is correctly fenced out by the pin. Same residual as
  E3L0-1's (the defective attribution came from my spec; held to the
  harshest reading per the standing lesson).
- **E3L0-2 (REPAIR-NEEDED): DISCHARGED AS SPECIFIED, with two named
  residuals in the delivered text** — the condition is DOMAIN-
  COMPLETED with all three consumptions itemized and verified (5.5),
  the falsifier parenthetical is re-calibrated exactly as demanded
  (5.4 CONFIRMED half), the carriers all propagate (5.7). Residual
  (i): the delivered "(the (v, S)-image of)" parenthetical presupposes
  chart totality — the domain ladder's outermost rung (ER3L1-2, seeded
  by the l0 spec's own wording). Residual (ii): the consequent
  "restores the unconditional grant" was left uncalibrated against
  the newly two-membered condition (ER3L1-3 — propagation-
  completeness, not spec-seeded).
- Standing dispositions re-verified against the revision-7 state:
  **L0-1/L1-1, L0-2, L1-2** (r2-batch) hold — the leg-3 text and the
  s = 0/two-point/mediant passage (lines 2296-2338) are unchanged by
  revision 7 and were two-lens verified at rounds 2-3; the L1-2
  residue chain (L1-2 -> ESC1-F2 -> E2L0-1 -> E3L0-1+E3L0-2) is fully
  consumed modulo the three amendments above. **EL0-1==ESC1-F1, EL0-2,
  EL0-3==ESC1-F2, EL0-4, E2L0-1, E2L0-2**: all discharged of record
  at both lenses; nothing at revision 7 re-opens any of them. No
  orphan objection remains in any input file on disk.

The round is NOT dry at this lens: 3 findings sustained-by-this-
refuter (0 REPAIR-NEEDED + 3 AMENDMENT, 0 BREAKS-THE-LEG).

==============================================================================
## SUMMARY

| ID | Leg | Passage | Class | One-line |
|---|---|---|---|---|
| ER3L1-1 | 5 | general-member clause (l.2172-2174) + §13 echo (l.3486-3488) | AMENDMENT | "c_v > 0, which the strict pair already contains" is a false attribution: c_v = theta/e_SS, and the strict pair delivers only e_SS > 0 — c_v > 0 needs the hull-theta MEMBER (in-class witness: the E3L0-2 quadratic patch with a0 large negative has the strict pair everywhere and c_v < 0); the containment belongs to the full condition of record; seeded verbatim by my own round-2 repair spec — fifth spec-seeded instance |
| ER3L1-2 | 5 | condition of record "(the (v, S)-image of)" (l.2143-2144; §13 l.3550-3552) + assembly's "hull's state image" (l.2188) | AMENDMENT | theta > 0 licenses the chart's uniqueness, not its EXISTENCE: S(W) defined hull-wide (hull ⊆ chart range) is the domain ladder's unwritten outermost rung — in-class patch EOS (the row's own (m2)/(m3) class) with a thin S-band leaves E undefined at mid-segment states while the printed condition holds vacuously on the partial image; benign presupposition reading available (hence not REPAIR); closure counterpart already priced (table-domain precondition) |
| ER3L1-3 | 5 | falsifier consequent "restores the unconditional grant" (l.2279-2280) vs the revision-7 two-member condition | AMENDMENT | the demanded derivation delivers only the HESSIAN member; hull-theta is first-order data no concavity derivation controls (the row's own l.2136-2137 sentence) — a Gibbs-closure-wide firing would restore "the unconditional grant" as printed while item (i) still breaks at a theta < 0 hull state through the negative m-block; condition enlarged under an unchanged consequent (propagation miss) |

CONFIRMED (cannot break; strongest attacks recorded in-section): the
WRITTEN sufficiency assembly (5.1 — m-block sign by direct
differentiation, EXACT tau B^T Hess(-s) B congruence with no
remainder, strictness-tight -(1/theta) Legendre congruence derived in
full, boost-image (v, S)-membership attack failed, Bregman constant
exact); the quadruple pin + general-member clause minus its one
attributed phrase (5.2 — consumption audit, "at no strongly-convex
g", "one convex member suffices"); the DOMAIN-COMPLETED condition and
all three itemized theta consumptions (5.5 — each re-derived;
{theta > 0} W-non-convexity; non-redundancy of the third
consumption); AUD-cp revision-7 additions (5.6 — theta = T at the
closure; ER3L1-2 pushed through and absorbed by the priced
table-domain precondition); the re-calibrated falsifier parenthetical
itself (5.4 — the PROVIDED/else split closes E3L0-2's equivalence gap
as specified); all four propagation carriers (5.7 — no stale
theta-free or quadruple-free form of record); the revision-7 log
block (5.8 — transcriptions, merges, counts, provenance notes,
declared off-by-one, dryness ledger, gate status); LEG 3 dry status
at this lens (fresh direction-of-minting/seam, representation-
independence, partition-sign, and rider-integrability attacks — all
failed).

Counts: 3 findings total = 0 REPAIR-NEEDED + 3 AMENDMENT;
**BREAKS-THE-LEG: 0**. No statement, rigor label, or route-level
conclusion is touched by any finding: all three repairs, applied,
leave the quadruple-pinned grant intact and — for ER3L1-2 — add a
fifth named clause to the abstract-EOS accounting, STRENGTHENING the
no-viable-abstract-EOS-route conclusion once more; all three are
discharged automatically at the standing gamma(T) closure (hull-theta
and table-domain priced there; the attribution fix is textual). The
leg-3 (E-1) escalation thread remains DRY at both lenses. Leg 5 is
one wording pass from dry at this lens: zero derivation-content
defects survive in the revision-7 mathematics — the three residues
are attribution, presupposition-explicitness, and consequent
calibration.

## SELF-FALSIFIERS (what kills each finding)

- ER3L1-1: a derivation of c_v > 0 from e_vv > 0 AND
  e_vv e_SS > (e_vS)^2 ALONE (without any theta sign input) — cannot
  exist (c_v = theta/e_SS flips sign with theta at fixed strict pair:
  the a0-negative patch is the witness; refute the patch's in-class
  membership to revive); or a printed definition of c_v in this
  document that is theta-sign-free (none: line 2148 is the definition
  site of record).
- ER3L1-2: a printed line delivering S(W) defined on the whole hull
  for abstract in-class EOS (none found: §1 pins no EOS domain; the
  grant certifies only {rho >= rho_min}; the closure's evaluability
  clause is scoped "on the standing gamma(T) tabulated model"); or a
  proof that §1-class EOS are necessarily globally defined in S with
  e(v, . ) surjective onto the segment eps-range (refuted by the
  row's own patch-defined (m2)/(m3) witnesses being accepted
  in-class); or a ruling that the f(A)-presupposition reading is the
  unique admissible one AND that presupposed hypotheses need no
  written statement — the second half contradicts the document's own
  "the line must be WRITTEN" standard, which is why the finding
  stands at AMENDMENT.
- ER3L1-3: a proof that any derivation of strict joint s-concavity
  from the §1 pins necessarily also delivers theta > 0 at hull states
  (false: Gibbs closure is EOS-wide by definition and theta-sign-free;
  strict Hess s ND is compatible with theta < 0 since theta = 1/s_eps
  is first-order data — the row's own line 2136-2137 argument); or a
  reading of "the unconditional grant" of record that excludes the
  hull-theta member (none: the grant head at lines 2284-2288
  conditions on "the STRICT + hull-theta condition of record" as one
  object).
- Any CONFIRMED verdict above: a derivation-level break of the quoted
  passage that the recorded strongest attack missed.

END — until-dry round-3 escalation refutation, lens l1 (completes
two-lens round-3 coverage; leg 3 dry at both lenses; leg 5 not yet
dry pending consumption of ER3L1-1/2/3 — all wording-class). Machine
summary: {objections: 3, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc1_r3_l1.md}
