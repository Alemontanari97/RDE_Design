# ESCALATION REFUTATION — DOC-1 E-1/E-2 repairs, until-dry ROUND 3, lens l0
# (hyperbolic systems / functional-analytic rigor)

Date: 2026-08-19. Target: `phaseD/phaseD_stop_proof.md` AT REVISION 6 —
ONLY the escalation-repair text for legs 3 and 5 named by the NEWEST
revision-log entries (the §13 REVISION 6 block, lines 3198-3328, and
the body passages it edits — all on the G8/r2 accounting row of leg 5:
the STRICT condition of record + sufficiency note, lines 2116-2138;
the (m3) strictness rung, lines 2157-2175; the AUD-cp strict-discharge
strengthening, lines 2175-2185; the RE-RECALIBRATED falsifier, lines
2186-2204; the grant clause "under the STRICT condition of record",
lines 2205-2209; the four propagation carriers: header audit line
84-92, honest status line 2254-2266, §9 gamma table 2457-2483, §13
EL0-3 entry SUPERSEDED-IN-PART note 3103-3115. Leg 3 received ZERO
edits at revision 6 — examined and handled in its own section below).

FILE-NAME / ROUND-NUMBER DEVIATION, DECLARED (third occurrence of the
same off-by-one, same handling as the two prior rounds, both of which
the revision log ratifies as "declared"): the launching brief named
this slot "until-dry ROUND 2" with output `esc_doc1_r2_l0.md`. That
file EXISTS, is the CONSUMED round-2 record (its IDs E2L0-1/E2L0-2 are
cited of record in the target's REVISION 6 block, lines 3198-3201),
and overwriting it would destroy the artifact the revision log cites.
The brief's operative targeting clause ("the newest revision-log
entries name the edited passages") resolves to the REVISION 6 block,
whose honest-residue item (1) states these revision-6 repairs "await
the next escalation-refutation round" — this document IS that round.
Output therefore goes to `esc_doc1_r3_l0.md`; the round-2 record is
untouched.

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 rows L0-1/L1-1, L0-2,
L1-2 and §4(c) E-1/E-2 (the standing escalation specs); full ROUND-2
objection text `r2pass/esc_doc1_r2_l0.md` (E2L0-1, E2L0-2), read IN
FULL; ROUND-1 texts `r2pass/esc_doc1_r1_l0.md` / `esc_doc1_r1_l1.md`
per the dedup layer (their findings EL0-1..EL0-4, ESC1-F1/F2 are all
consumed at revision 5 with dispositions verified by the round-2
record); original r2-batch texts `refute_r2batch_l0.md` /
`refute_r2batch_l1.md` at the attacked legs (dedup layer). Both duties
executed: (a) derivation-level attack on the revision-6 repair text;
(b) verification that the revision-6 repairs DISCHARGE the round-2
sustained findings they answer (E2L0-1, E2L0-2).

DEDUP REGISTER (dispositioned objections NOT re-raised): L0-1/L1-1,
L0-2, L1-2 (r2-batch — consumed at revisions 4/5); EL0-1==ESC1-F1,
EL0-2, EL0-3==ESC1-F2, EL0-4 (round 1 — consumed at revision 5,
dispositions verified by the round-2 record and re-checked here at
the carrier level); E2L0-1, E2L0-2 (round 2 — consumed at revision 6,
adequacy examined below). Both round-3 findings attack REVISION-6
text that did not exist before revision 6 — zero prior adversarial
coverage — and each declares its distinction from every ID above.
Where a finding touches a dispositioned ID, the ID is cited and the
failure point of the disposition is stated. Every attacked passage:
verbatim quote + attack + class in {BREAKS-THE-LEG, REPAIR-NEEDED,
AMENDMENT}. Every examined passage not broken: CONFIRMED with the
strongest attack tried.

Finding IDs: E3L0-1, E3L0-2. Line numbers are of the revision-6 file.

==============================================================================
## LEG 5 (E-2) — the revision-6 G8/r2 strict-form rewrite

### 5.1 The sufficiency note and the grant's entropy member —
### **OBJECTION E3L0-1, REPAIR-NEEDED**

Quote 1 (the NEW revision-6 sufficiency note, lines 2127-2129):
"Pointwise strictness plus compactness of the comparison-segment
hull yields the uniform c of item (i) below."

Quote 2 (the rewritten grant clause, lines 2205-2207): "Granted,
under the STRICT condition of record: (i) E(V|U) >= c|DeltaW|^2 with
all comparison segments inside the convex physical region".

Quote 3 (the row's standing definition of E, line 2099, the object
item (i) quantifies): "What W-convexity of E = -rho g(S) (Harten;
Godlewski-Raviart — t-EVOLUTION facts) genuinely delivers".

Attack (derivation level). As printed, the sufficiency note is FALSE
for the object item (i) is written about, and the row's OWN kept
sentence supplies the refuting instance.

(a) *The entropy member is unpinned, and an in-class member breaks
item (i) WITH the strict condition of record satisfied.* E is of
record "-rho g(S)" with g constrained nowhere in the condition
clause (only "g' > 0" appears upstream, via the Harten family). Take
the standing ideal-gas instance (a fortiori inside the abstract-EOS
class; gamma-law, c_v > 0 constant): joint s-concavity holds in its
STRICT form everywhere (s = c_v ln eps + c_v(gamma-1) ln tau,
Hess s = diag(-c_v(gamma-1)/tau^2, -c_v/eps^2) strictly negative
definite), so the strict condition of record holds on EVERY
comparison-segment hull. Now pick the member g = f with
f(S) = exp(kS), k >= 1/c_v: f' > 0, f''/f' = k >= 1/c_v. By the
row's OWN kept sentence (lines 2138-2140: "At ideal gas -rho f(S) is
strictly convex iff f' > 0 AND f''/f' < 1/c_v — a condition on g
beyond g' > 0 (the g-condition instance, kept)"), -rho f(S) is NOT
strictly convex in W — its Hessian is somewhere not positive
definite, and along a degenerate (or negative) direction at such a
state the Bregman expansion gives E(V|U) = o(|DeltaW|^2): for EVERY
fixed c > 0, item (i) fails at small |DeltaW|. The strict condition
of record is satisfied; printed item (i) breaks. The row contains
its own separating instance — the same internal-refutation pattern
the r2-pass judge sustained at leg 6 (L0-3: a display "refuted by
its own recorded example").

(b) *What is actually true, and what is missing in writing.* The
sufficiency note is TRUE exactly for the member g = id (E = -rho S)
— and for THAT member the proof needs an assembly that is NOWHERE in
the document: the recorded congruence chain ("at rest states the
(rho, E)-slice Hessian of -rho s(1/rho, E/rho) is CONGRUENT to
Hess(-s) via ... B; boost affinity", lines 2150-2154) is architected
for and only delivers the NECESSITY direction (a bad s-direction
lifts to a bad W-direction along the affine slice). SUFFICIENCY —
strict s-concavity implies the FULL W-Hessian of -rho S is positive
definite — additionally needs the momentum block and cross terms:
at a rest state, d^2(-rho s)/dm_i dm_j = (s_eps/rho) delta_ij
= delta_ij/(rho T) (positive precisely when theta > 0 — see
E3L0-2), the m-(rho,E) cross terms VANISH at m = 0 (both carry a
factor m_i), so the full Hessian is block-diagonal =
[slice block congruent to tau B^T Hess(-s) B] + [(1/(rho T)) I];
boost affinity then transports positive-definiteness to all
velocities; continuity of Hess e (an EOS C^2 consumption, implicit
in §1) plus compactness of the hull's state image then gives the
uniform lower eigenvalue bound and, by segment-Taylor, the uniform
c. None of these clauses is printed; the note asserts their
conclusion. Held to the standard this document itself minted and the
judge enforced at leg 3 ("one line, but the line must be WRITTEN",
VERDICT_r2pass §2.1 row L0-1/L1-1), the written line is not the
proof of the note — and unlike leg 3's case the printed conclusion
is not even true under the printed quantification, by (a).

Class: **REPAIR-NEEDED** — the same severity test the judge applied
to L1-2 and the prior rounds applied to EL0-3 and E2L0-1 decides it:
a mathematical object in class (the ideal-gas pair EOS + member
f = exp(kS), k >= 1/c_v) separates the printed condition from the
printed grant, so the accounting text must change, not merely its
wording. Not BREAKS: no statement, rigor label, or route-level
conclusion moves — the OPEN verdict, the two-piece residue, and the
no-viable-abstract-EOS-route conclusion all survive; the repair
SCOPES the grant rather than shrinking it (the granted half is real,
for the named member).

Repair (two clauses + one written line): (1) pin the member in the
grant and in the sufficiency note — "item (i) is granted for the
member g = id, E = -rho S; other family members additionally require
the g-condition (the kept ideal-gas iff f' > 0 AND f''/f' < 1/c_v is
its instance; its abstract-EOS form is unstated and NOT needed —
one convex member suffices for the device)"; (2) write the
sufficiency assembly in one line — rest-state block-diagonal
splitting (slice congruence + m-block 1/(rho T) + vanishing cross
terms at m = 0), boost transport, Hess-continuity + hull compactness
=> uniform c; noting that the necessity-direction chains (m1)-(m3)
are untouched (they only ever consume the slice).

DEDUP DECLARATION: NOT a re-raise of E2L0-1 — that priced the
STRICTNESS of the condition (non-strict ">=" in the sufficiency
slot); revision 6 delivered the strict form (verified in 5.4 below),
and THIS finding prices the delivered sufficiency note's
QUANTIFICATION (which E) and its unwritten mechanism — text that did
not exist before revision 6. Not a re-raise of EL0-3/ESC1-F2 (scalar
vs joint naming) or L1-2 (absence of any condition) or r2b-F1
(coercivity conflation). PROVENANCE, declared per the standing
lesson of this thread (both prior rounds seeded a defect through
their own repair specs): the round-2 repair spec's own clause
("with the note that pointwise strict + compactness of the segment
hull yields the uniform c of item (i)", esc_doc1_r2_l0.md §5.1)
seeded this note verbatim — the spec too left the member and the
mechanism unnamed; repair-spec text is not exempt from refutation.
The E2L0-1 disposition fails at exactly this transplanted note and
nowhere else.

### 5.2 The hull's missing theta pin (condition domain) —
### **OBJECTION E3L0-2, REPAIR-NEEDED**

Quote 1 (condition of record, lines 2121-2124): "Hess e(v, S)
positive DEFINITE on the comparison-segment hull, i.e. the strict
pair e_vv > 0 (= c^2 > 0, already a §1 pin) AND the strict
Grueneisen cross-term bound e_vv e_SS > (e_vS)^2 (unpinned by §1)".

Quote 2 (the re-recalibrated falsifier's new parenthetical, lines
2197-2199): "derive joint s-concavity IN THE STRICT FORM on the
comparison-segment hull (equivalently: wherever the §1 pins hold)".

Quote 3 (§1 gas model, lines 190-192): "c^2 = p_rho|_S > 0 and
theta > 0 on the state region of interest".

Attack (derivation level — a load-bearing consumption on the hull
that no printed line delivers). The condition of record is imposed
on the comparison-segment hull, but the transfer from "Hess e(v, S)
PD" to "item (i) for E = -rho S" consumes theta > 0 AT HULL STATES
three separate times, and nothing printed puts the hull inside
{theta > 0}:

(a) *The chart.* "Hess e(v, S) ... on the comparison-segment hull"
evaluates a (v, S)-object on a W-set: the state map W -> (v, S)
inverts eps = e(v, S) in S, which needs e_S = theta != 0 (monotone
inversion) along the hull — before any Hessian can even be read
there.

(b) *The Legendre step.* The equivalence "STRICT joint s-concavity
... — positive-definite Hess e(v, S) —" (honest status line, lines
2259-2261) runs on the partial Legendre inversion, which the row
itself flags as "(theta > 0, partial Legendre inversion)" (line
2115) — pointwise at the states where it is applied, i.e. hull-wide.

(c) *The momentum block.* In the sufficiency assembly (E3L0-1(b)),
the m-block of the W-Hessian of -rho S at a rest state is
(1/(rho T)) I: at a hull state with theta < 0 it is NEGATIVE — the
W-Hessian acquires a negative direction there even with Hess e(v, S)
positive definite (theta is FIRST-order data, unconstrained by any
Hessian condition), and comparison pairs straddling such a state
along that direction give E(V|U) < c|DeltaW|^2 for every fixed
c > 0: item (i) breaks with the full printed condition of record
satisfied.

Now the domain accounting. §1 pins theta > 0 only "on the state
region of interest" (Quote 3); H5' puts the SOLUTIONS' values in K;
the row's own central point is that comparison segments LEAVE K
(lines 2192-2193, the falsifier's own recital); and the only region
the grant certifies the segments to stay in is "the convex physical
region ({rho >= rho_min} IS convex in W — this half of the pricing
was correct)" (lines 2206-2209) — a region that carries NO theta
clause. {theta > 0} is not convex in W for an abstract EOS (theta
composes S(W), which is not affine in W — the row makes exactly this
non-affineness argument for c two sentences later), so hull
membership does not come free from endpoint membership in K. The
consumption is real, named, and unpinned: the SAME defect class as
L1-2 (a named condition missing from the granted half's accounting)
and the SAME axis as E2L0-2 (the domain: K -> hull), one rung
further out (hull -> pin region).

The falsifier parenthetical inherits it: "(equivalently: wherever
the §1 pins hold)" is an EQUIVALENCE only if the hull lies inside
the region where the pins hold; under §1's literal text ("on the
state region of interest") that inclusion is exactly what is
missing, so a pins-only derivation — which concludes only where the
pins hold — could be declared, via the parenthetical, to cover hull
states OUTSIDE that region: residual false-restoration power on the
domain, the precise defect class E2L0-2 was consumed for. Carried
here, not counted separately.

Class: **REPAIR-NEEDED** — the granted half's condition accounting
is incomplete by one named, load-bearing consumption (theta > 0 on
the hull), with an in-class breaking mechanism at (c); judge
precedent L1-2 (SUSTAINED-REPAIR) is on all fours. Not BREAKS: at
the standing gamma(T) thermally-perfect closure theta = T > 0 holds
wherever the closure is defined, so the AUD-cp discharge and every
route-level conclusion survive unchanged; the gap prices the
ABSTRACT-EOS accounting only, exactly like its three predecessors,
and the repair once more STRENGTHENS the
no-viable-abstract-EOS-route conclusion (a fourth named condition
on the granted half).

Repair (one clause + falsifier touch + carrier propagation): state
the condition of record as "theta > 0 AND Hess e(v, S) positive
definite on (the (v, S)-image of) the comparison-segment hull" —
the theta clause both licenses the chart/Legendre steps and makes
the m-block positive; recalibrate the falsifier parenthetical to
"(equivalently: wherever the §1 pins hold, PROVIDED the pins are
read on the whole EOS domain — else on the hull itself)"; propagate
to the four carriers by the same one-word route the strict form
took ("STRICT" -> "STRICT + hull-theta" or equivalent).

DEDUP DECLARATION: NOT a re-raise of E2L0-2 — that priced the
falsifier's restoration DOMAIN ("on K" vs hull) and is DISCHARGED as
delivered (5.5 below); this finding prices the CONDITION's domain
hypotheses on the hull itself (chart, Legendre, m-block), text whose
strict form did not exist before revision 6. Not a re-raise of L1-2
/ EL0-3 / E2L0-1 (thermal-stability condition naming/strictness —
all Hessian-level; theta is first-order data no Hessian condition
controls). PROVENANCE: the round-2 repair spec transplanted
"(equivalently: wherever the §1 pins hold)" from its own defense
analysis (esc_doc1_r2_l0.md §5.2, "a pins-only derivation holds
wherever the pins hold") without checking §1's own domain clause —
the third consecutive spec-seeded defect; the E2L0-2 disposition
fails at exactly this parenthetical and nowhere else.

### 5.3 The strict condition's algebra and the "matching neither"
### parenthetical — CONFIRMED

Quote (lines 2121-2138): "Hess e(v, S) positive DEFINITE on the
comparison-segment hull, i.e. the strict pair e_vv > 0 (= c^2 > 0,
already a §1 pin) AND the strict Grueneisen cross-term bound
e_vv e_SS > (e_vS)^2 (unpinned by §1); e_SS > 0 (= c_v > 0 via
c_v = theta/e_SS: the necessary scalar shadow, the part revision 4
named) then FOLLOWS from the strict pair ... The revision-5 printed
NON-strict triple (e_vv > 0 AND e_SS > 0 AND e_vv e_SS >= (e_vS)^2)
does NOT suffice for item (i): it sits strictly between
positive-SEMIdefiniteness of Hess e (which is what W-convexity
itself FORCES — the necessity direction, where '>=' is the correct
form; the (m1)/(m2) kill chains run there) and
positive-DEFINITENESS, matching neither ((m3) separates it from PD;
the PSD state e_SS = e_vS = 0 with e_vv > 0 separates it from PSD)."

Strongest attacks tried, all failed:
(a) *Sylvester*: PD of a symmetric 2x2 <=> leading minors e_vv > 0
and det > 0 — exact; e_SS > (e_vS)^2/e_vv >= 0 follows — exact;
c^2 = v^2 e_vv identifies the first minor with the §1 pin (p = -e_v,
c^2 = dp/drho|_S = (-e_vv)(-v^2)) — checks; c_v = theta/e_SS (at
fixed v, d eps = T dS, dT = e_SS dS) — checks.
(b) *The lattice claim*: triple => PSD (positive diagonal +
nonnegative determinant) — checks; PD => triple — checks; both
inclusions strict by the two named separators — (m3) is in the
triple, not PD (det == 0); the state e_SS = e_vS = 0, e_vv > 0 is
PSD (eigenvalues e_vv, 0), not in the triple. "Matching neither" is
exactly right; no counter-object found.
(c) *The necessity re-scope*: non-strict W-convexity forces
non-strict s-concavity (slice congruence + Legendre, given theta >
0 at the states used — in-K states, where the pin holds), i.e. PSD:
">=" is indeed the correct necessity form. Checks. (The theta
consumption at HULL states is E3L0-2's, not this passage's: the
(m1)/(m2)/(m3) kill chains run at in-patch states with theta > 0 by
construction.)

### 5.4 The (m3) strictness rung — CONFIRMED

Quote (lines 2157-2175): "(m3) — the strictness rung, revision 6 per
E2L0-1 — the (m2) quadratic family AT its determinant boundary:
e0'' = a1^2/b CONSTANT (quadratic e0, a1 != 0, b > 0, a0 large), so
e_vv e_SS - (e_vS)^2 = (a1^2/b) b - a1^2 == 0 on the whole patch:
Gibbs closure, theta > 0, c^2 = v^2 a1^2/b > 0, e_SS = b > 0 and the
NON-strict determinant bound ALL hold, but Hess e(v, S) =
[[a1^2/b, a1], [a1, b]] is rank 1 — e is convex, NOT strictly,
affine along the constant null direction d0 = (b, -a1); through the
same boost-affinity + perspective-congruence chain the W-Hessian of
E = -rho S is positive SEMIdefinite with a nontrivial null direction
at every state over the patch, and along it the Bregman expansion
gives E(V|U) = 0 + O(|DeltaW|^3), so for EVERY fixed c > 0 the bound
E(V|U) >= c|DeltaW|^2 FAILS at small |DeltaW|".

Strongest attacks tried, all failed:
(a) *Null-direction algebra*: [[a1^2/b, a1],[a1, b]] . (b, -a1) =
(a1^2 - a1^2, a1 b - a1 b) = 0 — checks; det = (a1^2/b) b - a1^2
== 0, rank 1 for a1 != 0 — checks; patch pins theta = a0 + a1 v +
b S > 0 (a0 large), c^2 = v^2 a1^2/b > 0, e_SS = b > 0, Gibbs by
construction — all check.
(b) *Does the KILL need the unwritten sufficiency assembly of
E3L0-1(b)?* No — attacked and survived: the kill needs only the
NULL direction, and the lifted direction at a rest state has zero
m-component, so its Hessian quadratic form reads the (rho, E)-slice
block alone (the cross terms are hit by the zero m-component
regardless of their value): d^T Hess d = d_slice^T [slice] d_slice
= 0 by the slice congruence. The printed "positive SEMIdefinite"
adjective DOES consume the fuller assembly (with in-patch theta > 0
it is true), but it is decorative for the kill — the operative
clause is the null direction plus the Bregman expansion.
(c) *"E(V|U) = 0 + O(|DeltaW|^3)" for a quadratic e*: the Bregman
functional is of E = -rho S in W, and the perspective map is
nonlinear in W even when e is quadratic in (v, S) — so the cubic
remainder is genuinely present, not identically zero; and
|O(|DeltaW|^3)| < c|DeltaW|^2 at small |DeltaW| for every fixed c.
Checks. The witness that non-strict does not suffice is airtight.

### 5.5 The AUD-cp strict discharge — CONFIRMED

Quote (lines 2175-2185): "On the STANDING gamma(T) thermally-perfect
closure the FULL condition is DISCHARGED by the AUD-cp-class finite
audit (c_v > 0): s(tau, eps) = phi(eps) + R ln tau is SEPARABLE
there (cross term identically zero, Hessian diagonal), so joint
concavity reduces EXACTLY to c_v > 0 — and the revision-6 STRICT
form is discharged VERBATIM: the diagonal Hessian diag(-R/tau^2,
-1/(c_v T^2)) is strictly negative definite iff c_v > 0, uniformly
on compacts, with strict determinant R/(tau^2 c_v T^2) > 0 automatic
— the condition prices the ABSTRACT-EOS accounting only."

Strongest attacks tried, all failed:
(a) *The diagonal entries*: s_tautau = -R/tau^2 (from R ln tau);
s_epseps = phi''(eps) = d(1/T)/d eps = -(1/T^2)(dT/d eps) =
-1/(c_v T^2) — both check; cross term identically zero — checks;
strict ND iff c_v > 0 with det R/(tau^2 c_v T^2) > 0 automatic —
checks. "Uniformly on compacts" — c_v(T) continuous and positive on
a compact T-range gives the uniform bound — checks.
(b) *Push E3L0-2 through the discharge* (the strongest attack): does
the theta gap survive at the gamma(T) closure? No — theta = T > 0
holds wherever the closure is DEFINED (T is the table coordinate),
so the chart/Legendre/m-block consumptions of E3L0-2 are free there;
the hull's evaluability inside the tabulated range is a
table-domain precondition the row already prices once for all
consumers ("certified table-interpolation enclosures — stated once
in the G8 row"). The scoping sentence "prices the ABSTRACT-EOS
accounting only" survives BOTH round-3 findings — which is exactly
why neither is BREAKS.
(c) *Does the strict form need more than c_v > 0 here?* No — the
separable Hessian's determinant strictness is automatic; the
revision-6 "discharged VERBATIM" claim is exact.

### 5.6 The re-recalibrated falsifier — CONFIRMED modulo the E3L0-2
### parenthetical

Quote (lines 2186-2204): "FALSIFIER of the condition-claim
(RECALIBRATED in revision 5 ...; RE-RECALIBRATED in revision 6 per
E2L0-2 — the revision-5 clause 'on K' had FALSE-RESTORATION power on
the DOMAIN ...): derive joint s-concavity IN THE STRICT FORM on the
comparison-segment hull (equivalently: wherever the §1 pins hold)
from Gibbs closure + c^2 > 0 + theta > 0 ALONE, with no K-geometry
input — THAT kills the condition-claim and restores the
unconditional grant; deriving e_SS > 0 alone kills only the (m1)
necessity exhibit and leaves the grant conditional on the strict
cross-term bound (m2 and m3 stand as the witnesses)."

Strongest attacks tried:
(a) *Dead-falsifier attack* (strongest): with (m2)/(m3) on file as
in-class witnesses that the pins do NOT imply strict joint
s-concavity, the demanded derivation is provably impossible — the
falsifier can fire only by first refuting a witness. Is unfirable
falsifier text a defect? NO — an unfirable falsifier for a
witness-PROVEN claim is the correct epistemic state (that is what
"proven" means operationally), and the row names the witnesses in
the same clause; the residual live channel (refute m2/m3 at a pin)
is exactly what my 5.4 attack (a) executed and failed. Attack fails.
(b) *The scalar-shadow clause*: "deriving e_SS > 0 alone kills only
the (m1) necessity exhibit" — checks (m1's witness has e_SS <= 0);
"leaves the grant conditional on the strict cross-term bound" —
checks (e_vv > 0 is already pinned; m2/m3 witness the cross-term
bound's independence in both the strict and non-strict readings).
(c) *"with no K-geometry input"* — the explicit exclusion E2L0-2's
strongest-defense analysis asked for, now printed: the K-restricted
reading is closed. Checks.
(d) The "(equivalently: wherever the §1 pins hold)" parenthetical
carries E3L0-2's domain gap (§1 pins theta > 0 only "on the state
region of interest"; the equivalence needs hull ⊆ pin-region, which
no line delivers) — carried in E3L0-2, not counted again.

### 5.7 Propagation carriers — CONFIRMED (all four verified on disk)

Examined verbatim: header audit line (lines 88-92: "... and in its
STRICT form — positive-definite Hess e(v, S) on the
comparison-segment hull — per revision 6, E2L0-1"); honest status
line (lines 2254-2266: "STRICT joint s-concavity in (specific
volume, internal energy) on the comparison-segment hull —
positive-definite Hess e(v, S) — / Bethe-Weyl class ... discharged
IN FULL, strict form included"); §9 gamma table (lines 2469-2476:
"stated STRICT — positive-definite Hess e on the comparison hull —
in revision 6 per E2L0-1 ... (separable s, strict form automatic);
table conclusions UNCHANGED"); §13 EL0-3 entry SUPERSEDED-IN-PART
note (lines 3103-3115, prior text preserved — conforms to the
document's supersession convention, matching the §13 L1-2 note's
form). Strongest attack tried: hunt a stale carrier of the
revision-5 non-strict form — grep over ">=", "SUFFICIENT",
"Grueneisen", "strict": every surviving ">=" instance sits either
in a necessity-direction context (line 2131's quoted revision-5
triple inside its own retraction; line 2135's "(m1)/(m2) kill
chains run there") or inside preserved superseded §13 text under a
supersession note (lines 3068, 3104-3106) — NO stale sufficiency
carrier of record found. The §9 abbreviation "comparison hull" for
"comparison-segment hull" is referentially unambiguous (single
antecedent). All four carriers inherit E3L0-1/E3L0-2 through the
condition they transcribe — carried there once, not counted per
carrier.

==============================================================================
## LEG 3 (E-1) — ZERO revision-6 edits; dry status TESTED

REVISION 6 names no leg-3 passage, and the on-disk leg-3 repair text
is verbatim the revision-5 state the round-2 record adjudicated:
the §13 E-1 falsifier bracket ("Firing condition of record: a finite
value of Sum_k <mu, psi chi_k> WITH <mu, psi chi_0> != 0", lines
2959-2965) and the (EU-x) rider's two written consumptions (lines
1228-1242) both MATCH the round-2 quotes character-for-character
(compared this pass). Dedup: EL0-1==ESC1-F1 and EL0-2 are
dispositioned and their dispositions were verified DISCHARGED by the
round-2 record; not re-raised.

Fresh attack tried on the dry verdict itself (owed under the brief's
"legs 3 and 5" scope): *well-definedness of the recalibrated firing
condition* — the criterion presumes Sum_k <mu, psi chi_k> has a
value to be "finite"; with mu >= 0, admissible psi >= 0, chi_k >= 0
the terms are nonnegative, so the sum is unconditionally
well-defined in [0, +inf] with no ordering/conditional-convergence
ambiguity, and the criterion is decidable as printed; under genuine
k-independence with <mu, psi chi_0> != 0 the partial sums diverge
(N x positive constant), so the falsifier fires exactly on a
k-independence FAILURE — the correct calibration, re-confirmed.
Attack failed. **LEG 3 remains DRY at lens l0 as of revision 6.**

==============================================================================
## THE REVISION-6 LOG BLOCK ITSELF (bookkeeping) — CONFIRMED

Examined (lines 3198-3328) against the round-2 record: the consumed
IDs, classes and counts ("2 distinct defects (1 REPAIR-NEEDED + 1
AMENDMENT, 0 BREAKS-THE-LEG)") MATCH esc_doc1_r2_l0.md exactly; the
ROUND-NUMBER NOTE correctly declares the stale brief; the coverage
asymmetry (round 2 = lens l0 only, no esc_doc1_r2_l1.md — verified
absent on disk) is DECLARED and carried in honest residue (2); the
"ROUND-1 l1 DISPOSITIONS VERIFIED ... no orphan objection remains in
either input file" claim matches the round-2 record's discharge
section; "LEG 3 (E-1): ZERO round-2 findings" matches; "NO label
motion" is consistent with VERDICT_r2pass §4(a) ([T-T0P] main
already SCHEMA); the strengthening claim ("the condition of record
gets strictly stronger ... the third time in a row") is
arithmetically right (absence -> scalar -> joint non-strict ->
strict); honest-residue item (1) correctly declares the revision-6
repairs UNADJUDICATED and the loop NOT dry — this document is that
adjudication; item (3) correctly keeps the Blocco-2 gate CLOSED
(E-5/E-6 not this document's to discharge). Strongest attack tried:
hunt a mis-transcribed verdict, an over-claim of dryness, or a
premature gate motion — none found. The block's E2L0-1 entry
parentheticals re-checked at pen grade: "(m3) ... null direction
d0 = (b, -a1)" (checks, 5.4(a)); "Bregman O(|DeltaW|^3) along the
null direction" (checks, 5.4(c) — genuinely cubic, not zero, since
the perspective map is nonlinear in W). The substantive defects of
the revision-6 delivery are in the BODY row's new sufficiency note
and domain hypotheses — carried as E3L0-1/E3L0-2, which the block's
"Statement, labels, route-level OPEN conclusion ... UNCHANGED"
framing survives (both findings confirm exactly that framing).

==============================================================================
## DISCHARGE VERDICTS (round-2 sustained findings vs revision-6 repairs)

- **E2L0-1 (REPAIR-NEEDED): DISCHARGED AS SPECIFIED, with a NEW
  named residual in the delivered note** — every demanded element
  landed and is verified correct: the STRICT form of record
  (Sylvester-exact, 5.3(a)); the non-strict triple re-scoped to the
  necessity direction with the correct lattice placement ("matching
  neither", both separators verified, 5.3(b)); (m3) recorded and
  verified airtight (5.4); the grant clause re-headed "under the
  STRICT condition of record"; the AUD-cp discharge strengthened to
  the strict form VERBATIM (5.5); propagation to all four carriers
  verified on disk with zero stale sufficiency-slot ">=" (5.7). But
  the spec's own sufficiency note ("pointwise strict + compactness
  ... yields the uniform c of item (i)"), transplanted verbatim,
  leaves the entropy member unpinned and the sufficiency assembly
  unwritten — the row's own kept ideal-gas iff separates the
  delivered condition from the delivered grant (E3L0-1). The
  disposition fails at exactly that transplanted note and nowhere
  else.
- **E2L0-2 (AMENDMENT): DISCHARGED AS SPECIFIED, with the spec's own
  equivalence parenthetical carrying a residual** — the demanded
  domain repair landed ("IN THE STRICT FORM on the
  comparison-segment hull ... from ... ALONE, with no K-geometry
  input" — the K-restricted reading is closed, the strictness gap is
  closed, 5.6(c)); but the transplanted "(equivalently: wherever the
  §1 pins hold)" assumes hull ⊆ pin-region while §1 pins theta > 0
  only "on the state region of interest" — residual
  false-restoration power on the domain, one rung out (carried
  inside E3L0-2). The disposition fails at exactly that
  parenthetical and nowhere else.

The round is NOT dry: 2 findings sustained-by-this-refuter
(2 REPAIR-NEEDED + 0 AMENDMENT, 0 BREAKS-THE-LEG).

==============================================================================
## SUMMARY

| ID | Leg | Passage | Class | One-line |
|---|---|---|---|---|
| E3L0-1 | 5 | sufficiency note (l.2127-2129) + grant clause (l.2205-2207) against E = -rho g(S) (l.2099); inherited by the four carriers | REPAIR-NEEDED | "Pointwise strictness plus compactness ... yields the uniform c of item (i)" is FALSE for the printed family-quantified E (the row's OWN kept ideal-gas iff supplies the in-class separating member f = exp(kS), k >= 1/c_v, which satisfies the strict condition and breaks item (i)); true exactly for the unnamed member g = id, whose full-Hessian sufficiency assembly (slice + m-block 1/(rho T) + vanishing cross terms + boost + compactness) is nowhere written — the recorded congruence chain runs the necessity direction only |
| E3L0-2 | 5 | condition of record (l.2121-2124) + falsifier parenthetical (l.2197-2199) vs §1 (l.190-192) | REPAIR-NEEDED | theta > 0 ON THE HULL is a load-bearing unpinned consumption (chart inversion, Legendre step, m-block sign): §1 pins theta only "on the state region of interest", segments leave K, {theta > 0} is not W-convex, and the grant's "convex physical region" carries no theta clause; in-class mechanism: hull state with theta < 0 gives m-block 1/(rho T) < 0 and breaks item (i) with Hess e PD satisfied; "(equivalently: wherever the §1 pins hold)" inherits the gap |

CONFIRMED (cannot break, strongest attacks recorded in-section):
strict-condition algebra + lattice placement "matching neither"
(5.3 — Sylvester, both separators, necessity re-scope); (m3)
strictness rung (5.4 — null-direction algebra, kill needs only the
slice, genuinely cubic Bregman remainder); AUD-cp strict discharge
(5.5 — diagonal Hessian re-derived, E3L0-2 pushed through and
absorbed by theta = T > 0 at the closure); re-recalibrated falsifier
core (5.6 — dead-falsifier attack fails: unfirable-because-proven is
the correct state; scalar-shadow clause exact; "no K-geometry input"
closes E2L0-2's reading) modulo the E3L0-2-carried parenthetical;
all four propagation carriers (5.7 — zero stale sufficiency ">=" of
record); leg-3 dry status re-tested with a fresh well-definedness
attack (failed — leg 3 stays DRY at lens l0); the revision-6 log
block's bookkeeping (IDs, classes, counts, declared round-number and
coverage asymmetries, honest residue).

Counts: 2 findings total = 2 REPAIR-NEEDED + 0 AMENDMENT;
**BREAKS-THE-LEG: 0**. No statement, rigor label, or route-level
conclusion is touched by either finding: both repairs, applied,
STRENGTHEN the no-viable-abstract-EOS-route conclusion a fourth time
(the granted half gets a pinned member and a fourth named condition),
mirroring the L1-2 -> EL0-3 -> E2L0-1 pattern; both gaps are
discharged automatically at the standing gamma(T) closure (g = id is
available there and theta = T > 0 by definition), so the
abstract-EOS-only scoping of the row is confirmed yet again. The
leg-3 (E-1) escalation thread remains DRY at lens l0.

## SELF-FALSIFIERS (what kills each finding)

- E3L0-1: a reading of the printed row under which item (i)'s E is
  demonstrably pinned to g = id of record (none found: line 2099
  introduces E = -rho g(S) and no later line selects the member); or
  a proof that strict joint s-concavity implies W-convexity of
  -rho f(S) for EVERY f with f' > 0 at ideal gas (refuted by the
  row's own kept iff — exhibit an error in that iff to revive this
  route); or a demonstration that the sufficiency assembly IS
  written somewhere in the document (grep for the m-block 1/(rho T)
  or the rest-state cross-term vanishing: no occurrence outside this
  refutation).
- E3L0-2: a printed line placing the comparison-segment hull inside
  the region where §1's theta > 0 pin holds (none found: §1 line
  190-192 is the only pin site and names "the state region of
  interest"; the grant certifies only {rho >= rho_min} convexity);
  or a proof that endpoint membership in K forces theta > 0 along
  W-segments for every §1-class EOS (the mechanism cannot exist:
  theta is first-order EOS data unconstrained by c^2 > 0/Hessian
  conditions off K, and S(W) is not affine); or a demonstration that
  Hess e(v, S) PD on the hull's image itself forces theta > 0 there
  (false: PD constrains second derivatives only; add any linear
  -M.S term to e to flip theta without touching the Hessian —
  Gibbs closure survives since p, theta are DEFINED from e).
- Any CONFIRMED verdict above: a derivation-level break of the
  quoted passage that my recorded strongest attack missed.

END — until-dry round-3 escalation refutation, lens l0. Machine
summary: {objections: 2, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc1_r3_l0.md}
