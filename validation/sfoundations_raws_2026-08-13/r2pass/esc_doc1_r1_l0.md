# ESCALATION REFUTATION — DOC-1 E-1/E-2 repairs, until-dry ROUND 1, lens l0
# (hyperbolic systems / functional-analytic rigor)

Date: 2026-08-18. Target: `phaseD/phaseD_stop_proof.md` AT REVISION 4 —
ONLY the escalation-repair text named by REVISION LOG §13 (E-1 = leg 3,
the rewritten §4 PERIODIZATION STEP incl. the (EU-x) equality rider and
the §13 entry with its falsifier; E-2 = leg 5, the G8/r2 repricing edits:
thermal-stability condition, s = 0 / two-point rewording, mediant clause,
honest status line, audit-line and §9 gamma-table consistency
annotations). Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 rows
L0-1/L1-1, L0-2, L1-2 and §4(c) E-1/E-2; full objection texts
`r2pass/refute_r2batch_l0.md` (L0-1, L0-2) and
`r2pass/refute_r2batch_l1.md` (L1-1, L1-2). Both duties executed:
(a) derivation-level attack on the repair text; (b) verification that the
repairs DISCHARGE the sustained objections they answer.

DEDUP RULE APPLIED: no objection already dispositioned is re-raised
unless the disposition itself fails; where a finding touches a
dispositioned ID, the ID is cited and the failure of the disposition is
stated. Every attacked passage: verbatim quote + attack + class in
{BREAKS-THE-LEG, REPAIR-NEEDED, AMENDMENT}. Every examined passage not
broken: CONFIRMED with the strongest attack tried.

Finding IDs: EL0-1 .. EL0-4. Line numbers are of the revision-4 file.

==============================================================================
## LEG 3 (E-1) — the rewritten PERIODIZATION STEP, §4 proof head
## (~lines 1176-1225) + §13 entry (~lines 2812-2836)

### 3.1 Retraction preamble (divergence ground) — CONFIRMED

Quote (lines 1176-1183): "the revision-3 mechanism 'summing telescopes
by periodicity' is RETRACTED: for T-periodic V the pairings
<mu, psi chi_k> below are EQUAL for every k, so the literal sum over
k in Z diverges unless the common value is zero, and nothing telescopes
among identical terms".

Strongest attack tried: sought a reading of the revision-3 line under
which the sum converges (conditional summation, telescoping of adjacent
window overlaps). None survives: <mu, psi chi_k> = <mu, psi chi_0> is an
exact identity (mu = -(div of the quadruple) is T-periodic as a
distribution since V and the quadruple are T-periodic; chi_k is the
kT-translate; psi T-periodic), so the partial sums are N * const and the
carve-out "unless the common value is zero" is exactly right. The
retraction ground is CORRECT as written.

### 3.2 Step (p1), single-window pairing — CONFIRMED

Quote (lines 1192-1197): "(p1) SINGLE-WINDOW PAIRING: for any T-periodic
torus test psi >= 0 (in x, y, z compactly supported in Omega_march as
before), <mu, psi chi_0> >= 0 is ONE legitimate compact-support
D'-pairing; it is k-independent (<mu, psi chi_k> = <mu, psi chi_0> by
joint T-periodicity of mu and psi). NO sum over k is taken anywhere."

Attacks tried, all failed:
(a) *Sign of chi_0*: (p1)'s ">= 0" needs psi chi_0 >= 0, i.e.
chi_0 >= 0 — not restated in the clause; killed because nonnegativity
(0 <= chi_k <= 1) is part of the standard definition of a partition of
unity, which the display invokes by name ("whose translates ... form a
partition of unity"); no non-standard signed PoU reading is available.
(b) *Existence of the translate-structured PoU*: an arbitrary
subordinate PoU need not consist of translates of one window; killed
because the translate PoU is constructible in one line (any bump chi
supported in (-T, T), positive on [-T/2, T/2]; chi_0 :=
chi / Sum_k chi(. - kT), the denominator smooth, T-periodic, bounded
below) — folklore below the "line must be WRITTEN" bar for this step,
whose minted content was the cancellation structure, not PoU existence.
(c) *Legitimacy of the pairing*: mu >= 0 in D' makes mu a nonnegative
Radon measure; psi chi_0 is C^inf compactly supported; pairing
legitimate. k-independence re-derived: <mu, psi chi_k> =
<mu(. + kT), psi(. + kT) chi_0> = <mu, psi chi_0>. No hole.

### 3.3 Step (p2), field terms — CONFIRMED

Quote (lines 1198-1203): "(p2) FIELD TERMS via Sum_k chi_k == 1: for
T-periodic h in L^1_loc(R_t), Int_R h chi_0 dt = Int_0^T h
(Sum_k chi_k) dt = Int_0^T h dt (unfold the k-translates onto one
period)."

Strongest attack tried: the sum/integral interchange in the unfolding
Int_R h chi_0 = Sum_k Int_0^T h(t) chi_0(t + kT) dt =
Int_0^T h(t) Sum_k chi_0(t + kT) dt. Killed: chi_0 has compact support,
so on [0, T] the translate sum is FINITE (locally finite family) — no
convergence theorem is consumed; and Sum_k chi_0(t + kT) =
Sum_j chi_j(t) = 1 (re-indexing j = -k). The identity is exact for every
T-periodic h in L^1_loc. The application is licensed: each field term of
<mu, psi chi_0> is (quadruple component o V) x (spatial/temporal
derivative of psi), T-periodic (H8' for V; psi torus test) and L^inf x
L^inf in t on compacts, hence L^1_loc. No hole.

### 3.4 Step (p3), cutoff-derivative cancellation — CONFIRMED

Quote (lines 1204-1213): "(p3) CUTOFF-DERIVATIVE TERMS KILLED by
Sum_k chi_k' == 0: the d_t term pairs against d_t(psi chi_0) =
(d_t psi) chi_0 + psi chi_0', producing the extra term
Int (q_t o V) psi chi_0' dt dV_x = Int over one period of
(q_t o V) psi (Sum_k chi_k') = 0, since differentiating
Sum_k chi_k == 1 gives Sum_k chi_k' == 0."

Strongest attack tried: term-by-term differentiation of Sum_k chi_k == 1
(an infinite sum). Killed: local finiteness again — on any compact
t-interval only finitely many chi_k are nonzero, so the sum is locally a
finite sum and differentiates term-by-term; alternatively (p2) applied
verbatim to h = (q_t o V) psi with chi_0 replaced by chi_0', whose
translate sum is 0. I also checked completeness of the term inventory
for the (EI-x) pairing: chi_0 depends on t only, so d_x, d_y, d_z of
(psi chi_0) generate NO cutoff-derivative terms — the single chi_0' term
is the whole correction, exactly as written. Recombining
(p1)-(p2)-(p3): <mu, psi chi_0> = [torus integral of the field terms]
+ 0 >= 0, which IS the torus form of (EI-x) against nonnegative
T-periodic tests. The sustained core of L0-1/L1-1 — single-window
pairing, Sum chi_k == 1 on field terms, Sum chi_k' == 0 as the entire
nontrivial content — is now WRITTEN and correct. The E-1 rewrite
DISCHARGES clauses (1)-(3) of L0-1 and the whole of L1-1.

### 3.5 The (EU-x) EQUALITY rider — **OBJECTION EL0-2, AMENDMENT**

Quote (lines 1216-1225): "THE (EU-x) EQUALITY PAIRING RIDES THE SAME
IDENTITY (stated per L0-1's second clause — the revision-3 text
periodized only (EI-x) while the same display silently consumed the
periodized EQUALITY pairing): the weak form of (EU-x) for V is tested
against the non-compactly-supported Lipschitz field D_W E(U), which is
T-periodic in t (U is T-periodic on the slab, H8'); testing against
D_W E(U) . (test) chi_0 componentwise and applying (p1)-(p3) verbatim
(with equality in place of the inequality sign) yields the torus form of
the equality pairing."

Attack (derivation level). "Verbatim" is not literally available: (p1)
is minted for SMOOTH torus tests psi, while the composite multiplier
(D_W E(U))_row psi placed in the test slot is only LIPSCHITZ in
(x, y, z, t) (D_W E is C^1 in W away from vacuum and U is C^1 on the
stratum-(A) slab, but the composite is not C^inf), and the weak form of
(EU-x) is minted against C_c^inf tests. Two consumptions ride
unwritten: (i) admissibility of compactly-supported Lipschitz tests for
the L^inf-coefficient weak form (standard mollification: fluxes in
L^inf, test in W^{1,inf}_c — one line, but under this document's OWN
minted standard for exactly this step, the line must be WRITTEN); (ii)
the reader must take the composite (D_W E(U))_row psi AS the "psi" of
(p1)-(p3) — otherwise d_t produces a third term
(d_t D_W E(U)) psi chi_0 that (p3)'s two-term decomposition
d_t(psi chi_0) = (d_t psi) chi_0 + psi chi_0' does not display (under
the composite reading it is absorbed into (p2)'s field terms, which are
still T-periodic L^1_loc since d_t D_W E(U) is L^inf on the slab — so
the argument is SOUND, but the sound reading is the one the text leaves
to the reader). The adjacent G2 itemization (lines 1230-1236) covers
the Gauss-Green consumption of the NEXT step against the
non-compactly-supported Lipschitz field; the rider's windowed
(compact-support) Lipschitz-test consumption is strictly weaker and is
covered a fortiori — which is why this is not REPAIR-grade.
Class: **AMENDMENT** — add one clause: "the composite Lipschitz
multiplier is an admissible test by mollification (fluxes L^inf); it is
taken as the psi of (p1)-(p3), whose field-term identity (p2) absorbs
the d_t D_W E(U) term". No statement, hypothesis or label moves.
Dedup: this attacks the ADEQUACY of the E-1 disposition of L0-1's
second clause (newly written text, zero prior coverage) — not a
re-raise of L0-1.

### 3.6 §13 E-1 falsifier of the retraction — **OBJECTION EL0-1,
### AMENDMENT** (falsifier calibration: false-positive power)

Quote (§13, lines 2832-2836): "FALSIFIER of the retraction: a finite
value of Sum_k <mu, psi chi_k> for some nonzero T-periodic mu >= 0 and
admissible psi, {chi_k} — kills the divergence claim (and with it the
ground of the rewrite, not the rewritten argument itself, which never
sums over k)."

Attack (derivation level). The divergence claim being guarded (lines
1179-1181) is "the literal sum over k in Z diverges UNLESS THE COMMON
VALUE IS ZERO" — it carves out the zero-value case. The falsifier as
printed fires on: nonzero mu + finite sum. Exhibit firing it against
the TRUE claim: take any nonzero T-periodic mu >= 0 and choose the
admissible test psi >= 0 supported (per period, in a spacetime region)
where mu vanishes — e.g. psi supported in an open subset of
Omega_march x T_t disjoint from supp(mu). Then <mu, psi chi_k> = 0 for
every k, the sum is 0 (finite), all falsifier conditions are met — and
the divergence claim is UNREFUTED (the common value IS zero). This is
FALSE-POSITIVE power, the precise defect class the document itself
repaired at the [T-T0P-E] falsifier in revision 3 (r2-F6 / l1's F10:
"the old falsifier had FALSE-POSITIVE power — a benign ... would have
fired it against a true THEOREM"), and it violates the R5 calibration
discipline (a rejector must be able to reject the CLAIM, not fire on
its truth). Repair is one clause: require the common value nonzero —
"a finite value of Sum_k <mu, psi chi_k> WITH <mu, psi chi_0> != 0".
Class: **AMENDMENT** (the falsifier guards only the retraction GROUND —
the §13 text itself notes a kill would not touch the rewritten
argument, which never sums over k — so no proof content or label is
exposed; but the printed rejector is miscalibrated). Dedup: new
revision-4 text; the r2-F6 disposition is cited as PRECEDENT, not
re-raised — that disposition (the [T-T0P-E] falsifier rewrite) stands.

### E-1 discharge verdict

L0-1 (SUSTAINED-REPAIR) and L1-1: **DISCHARGED**. All four demanded
elements are present and correct: single-window pairing (p1);
Sum chi_k == 1 on field terms (p2); Sum chi_k' == 0 killing the
cutoff-derivative terms, flagged as the entire nontrivial content (p3);
the equality pairing stated to ride the same identity with its H8'
consumption named. Statement, hypotheses, labels unchanged as the E-1
spec requires. Residue: EL0-2 (one written clause owed on the rider),
EL0-1 (falsifier calibration) — both amendment-grade; neither reopens
the sustained objections.

==============================================================================
## LEG 5 (E-2) — the G8/r2 repricing edits (~lines 2076-2162), audit
## line (~lines 84-91), gamma table (~lines 2341-2363), §13 entries

### 5.1 The named thermal-stability condition + its falsifier —
### **OBJECTION EL0-3, REPAIR-NEEDED**

Quote (lines 2084-2094): "What W-convexity of E = -rho g(S) (Harten;
Godlewski-Raviart — t-EVOLUTION facts) genuinely delivers — MODULO A
NAMED THERMAL-STABILITY CONDITION (added in revision 4 per L1-2):
W-convexity of -rho g(S) is NOT a free consequence of the §1 gas model
(Gibbs closure + c^2 > 0 + theta > 0 pin NO sign of e_SS); the
classical results cited additionally require thermal stability —
e_SS > 0 (equivalently c_v-type positivity / s-concavity in (specific
volume, internal energy) / Bethe-Weyl class: the same class G7 route
r-a already names)".

And the attached falsifier (lines 2099-2102): "FALSIFIER of the added
condition-claim: derive e_SS > 0 from Gibbs closure + c^2 > 0 +
theta > 0 alone (kills L1-2 and restores the unconditional grant)."

Attack (derivation level, two joined defects in the repair's own text).

(a) *The "equivalently" chain is false as an equivalence, and the
headline member is INSUFFICIENT.* e_SS > 0 <=> c_v > 0 is correct
given theta > 0 (c_v = theta / e_SS: with e(v, S), T = e_S and
c_v = e_S / e_SS). But e_SS > 0 is NOT equivalent to s-concavity in
(specific volume tau, internal energy eps): joint concavity of
s(tau, eps) is (by Legendre duality with theta > 0) joint CONVEXITY of
e(v, s), whose Hessian condition is e_vv >= 0 AND e_ss >= 0 AND
e_vv e_ss - e_vs^2 >= 0. The §1 pins give e_vv > 0 (c^2 = v^2 e_vv)
and the named condition gives e_ss > 0 — the CROSS-TERM (Grueneisen
coupling e_vS) determinant clause is pinned by NOTHING. In-class
breaking exhibit (same shape as the row's own e_SS <= 0 exhibit, one
rung deeper): e(v, s) = e0(v) + (a0 + a1 v) s + (b/2) s^2 on a compact
state region, with e0'' > 0 (so c^2 = v^2 e0'' > 0 — the s-coupling is
linear in v, so a'' = 0 leaves c^2 s-independent), b > 0 (so
e_SS = b > 0, c_v > 0), a0 large (theta = a0 + a1 v + b s > 0), Gibbs
closure automatic (p := rho^2 e_rho defines p); choose a1^2 > e0'' b:
then e_vv e_ss - e_vs^2 = e0'' b - a1^2 < 0 on the region — s(tau, eps)
is NOT concave there. That W-convexity of -rho g(S) (g = id) then FAILS
is forced, not merely plausible: a Galilean boost is AFFINE on
W = (rho, m, E) and leaves -rho S invariant, so the W-Hessian at any
velocity is congruent to the rest-state Hessian at the same
(rho, eps); and at rest states, restricting to the (rho, E) 2-plane,
h(rho, E) := rho f(1/rho, E/rho) with f = -s has (direct computation)
Hess h = (1/rho) B^T (Hess f) B with B = [[-tau, 0], [-eps, 1]]
invertible — a pointwise CONGRUENCE. Hence -rho S convex in W at a
state ==> s concave at its (tau, eps): the determinant-violating point
kills delivered item (i) (the lower sandwich E(V|U) >= c|DeltaW|^2
turns negative along the negative-curvature direction) at every state,
supersonic K-states included, whose (rho, eps)-shadow meets the
failure set — while the printed headline condition e_SS > 0 HOLDS.
So the repaired row, read at its headline member, still under-prices
the granted half by one clause — the defect CLASS of L1-2 (a needed
condition not named), now one condition deeper.

(b) *The falsifier's restoration clause over-claims.* "derive e_SS > 0
... restores the unconditional grant" commits to SUFFICIENCY of
e_SS > 0 for the grant; by (a) that is false — a derivation of
e_SS > 0 from the §1 pins (were one to exist) would kill L1-2's
necessity exhibit yet leave the grant conditional on the cross-term
clause. The falsifier is calibrated to the weakest member of a falsely
equivalenced list. (Note VERDICT_r2pass §5 uses the same form for
killing the OBJECTION — legitimate there; the document's added clause
"and restores the unconditional grant" is the over-reach.)

What SURVIVES my attack (stated so the repair is not over-corrected):
the AUD-cp discharge note is ROBUST to the strengthened condition — at
the standing thermally-perfect gamma(T) closure, s(tau, eps) =
phi(eps) + R ln tau is SEPARABLE (cross term identically zero), so
joint concavity reduces exactly to phi'' = -1/(T^2 c_v) < 0, i.e.
c_v > 0: the AUD-cp-class audit discharges the FULL condition there,
and the row's scoping "it prices the ABSTRACT-EOS accounting only"
remains true. The route-level conclusion (NO named viable abstract-EOS
G8 route; r2 a partial reduction) is STRENGTHENED again, exactly as
L1-2's was.

Class: **REPAIR-NEEDED** (not BREAKS: no statement, label, or
route-level conclusion moves — the defect is in the accounting text
and falsifier calibration, the same severity shape the judge gave
L1-2). Repair: name the condition in its sufficient form — joint
s-concavity in (tau, eps) / thermodynamic-stability (Bethe-Weyl)
class, WITH e_SS > 0 (= c_v > 0) recorded as its necessary scalar
shadow and the ideal-gas iff kept as the g-condition instance; delete
"equivalently" or scope it to the c_v member alone; recalibrate the
falsifier ("derive JOINT s-concavity on K from the §1 pins alone
restores the grant; deriving e_SS > 0 alone kills only the necessity
exhibit"); propagate the same one-word strengthening to the §13 L1-2
entry and the honest status line ("named thermal-stability condition"
-> unchanged wording works once the row defines the condition in the
joint form).

Dedup declaration: NOT a re-raise of L1-2. L1-2 established that a
thermal-stability condition is missing and wrote "the route runs
through concavity of s ... which NEEDS e_SS > 0" (necessity —
correct). The revision-4 transcription inverted necessity into the
equivalence chain and minted the restoration clause; both are NEW
revision-4 text, and the attack is on the adequacy of THAT disposition.
Not a re-raise of r2b-F1 either (coercivity conflation — untouched
here; the x-flux coercivity piece remains correctly priced OPEN).

### 5.2 The s = 0 / two-point rewording — CONFIRMED

Quote (lines 2110-2126): "the segment-Taylor integrand D^2 G_U(W_s) is
at every s > 0 a TWO-POINT object (U != W_s: curvature evaluated at W_s
against the multiplier D_W E(U) anchored at U, congruent to NO
M-Hessian at all) with NO definiteness certificate, on or off the
branch — THIS is the open obstruction. (Reworded in revision 4 per
L0-2: the revision-3 sentence attached [S-XCONV] R1 at s = 0, where the
congruence D^2 G_U(W_U) = DF_x^T Hess_M(eta)(M_U) DF_x ... in fact
yields the certified DEFINITE block ...; at subsonic W_s even the
ONE-POINT congruent object is indefinite by [S-XCONV] R1 — an
auxiliary fact, not the mechanism.)"

Attacks tried, all failed to break:
(a) *Two-point decomposition*: re-derived D^2 G_U(W_s) =
DF_x^T Hess_M(eta)(M_s) DF_x + (D_M eta(M_s) - D_M eta(M_U)) . D^2
F_x(W_s) — matches the judge's act (iii); at s = 0 the second term
vanishes and the base point is on the certified supersonic branch:
DEFINITE, exactly as now printed. The rewording states the true
obstruction (no certificate for the two-point object at s > 0) and
demotes the subsonic one-point fact to auxiliary. Correct.
(b) *Strongest residual attack*: the auxiliary sentence "at subsonic
W_s even the ONE-POINT congruent object is indefinite by [S-XCONV] R1"
silently consumes invertibility of DF_x at the subsonic state (a
congruence transfers inertia only through an invertible factor;
det D_U F_x vanishes at u = 0 and u = c). Killed as an objection: at
subsonic states with 0 < u < c the determinant is nonzero (the L-XSON3
factorization), u = 0 is a measure-zero edge outside any comparison
segment of interest, and the sentence is explicitly flagged
NOT-the-mechanism — no load path runs through it. Recorded as attack
tried, not a finding.

### 5.3 The restored mediant clause and the transfer conclusion —
### **OBJECTION EL0-4, AMENDMENT**

Quote (lines 2126-2140): "And the supersonic set {u > c} is NON-convex
in W: u = m1/rho is a mediant under convex combination AND c moves with
(rho, S) — S is not affine in W, and W-averaging deposits velocity
variance into internal energy, raising c (the mixing mechanism,
verified by l1's exhibit) — so two supersonic states can average
subsonic (the 'c moves with (rho, S)' clause is load-bearing and had
been dropped in the revision-3 transcription ...; the pair is
EXPECTED-NOT-EXHIBITED — no certified subsonic-average pair is on
file, and none is needed for the OPEN verdict: the burden sits on r2's
unproven coercivity, not on this pricing): the hull obstruction
TRANSFERS to W-space."

Attack (derivation level). The mechanism restoration is correct and I
could not break it: W-averaging gives u_avg the mass-weighted mediant,
and the kinetic term |m|^2/(2 rho) is jointly convex in (rho, m), so
the averaged state's internal energy EXCEEDS the average of internal
energies by the convexity deficit (velocity variance) — internal
energy up, c generically up: the mixing mechanism as stated. The
defect is one clause downstream: the CONCLUSION after the colon — "the
hull obstruction TRANSFERS to W-space" — is printed CATEGORICALLY,
while its sole support ("two supersonic states can average subsonic")
is, by the row's own marker three lines earlier, EXPECTED-NOT-EXHIBITED
(and "raising c" is itself EOS-generic, not certified on K). A
categorical claim resting on a marked-unexhibited premise inside a
pricing row is the residual of the exact defect L0-2 named ("a claim
without falsifier inside a gap row whose function is pricing"); the
disposition applied the demanded marker to the premise but let the
downstream conclusion escape it. The direction is conservative (if the
transfer failed, r2 would look BETTER and the OPEN verdict would still
be safe), which is why this is not repair-grade. Class: **AMENDMENT** —
extend the marker across the colon: "the hull obstruction is EXPECTED
to transfer to W-space (pair not exhibited; either way the burden sits
on r2's unproven coercivity)". Dedup: attacks the adequacy of the L0-2
disposition on its own terms (the marker's scope), cited as such; the
premise-level disposition itself stands.

### 5.4 Honest status line + consistency edits — CONFIRMED

Quotes examined: (i) STATUS line (lines 2144-2150): "a PARTIAL
reduction MODULO the named thermal-stability condition (e_SS > 0 /
s-concavity / Bethe-Weyl class; discharged at the standing gamma(T)
closure by the AUD-cp-class c_v > 0 audit) + OPEN x-flux segment
coercivity (a G8-equivalent problem)"; (ii) audit line (lines 84-91):
"r2 is a PARTIAL reduction with an open coercivity piece AND, per
revision 4 / L1-2, a named thermal-stability condition on its granted
half"; (iii) gamma table (lines 2349-2356): same two-piece residue with
"table conclusions UNCHANGED"; (iv) §13 label summary (lines
2879-2884): "NO label motion ... G8's r2 residue now TWO named pieces".

Strongest attacks tried: (a) hunted for a consumer of the OLD one-piece
r2 residue left un-annotated — the three residue carriers (audit line,
G8 row, gamma table) and the §13 summary all carry the two-piece form;
grep-level scan of the G5/G4 dependent rows found them consuming the
G8 SEGMENT CONSTANTS (unchanged object), not the r2 residue — no stale
consumer found. (b) Checked the E-2 spec conformance item-by-item:
condition added on the granted half with AUD-cp note (spec clause 1 —
present, modulo EL0-3's calibration defect); L0-2 rewording applied
(spec clause 2 — present, modulo EL0-4's marker scope); route-level
OPEN conclusion and gamma table unchanged (spec clause 3 — verified).
(c) The status line inherits EL0-3's naming defect by reference
("the named ... condition") — carried under EL0-3, not double-counted.

### E-2 discharge verdict

L1-2 (SUSTAINED-REPAIR): **DISCHARGED IN SUBSTANCE, with one residual
defect in the repair's own text (EL0-3)** — the condition is named, the
in-class breaking mechanism recorded, the AUD-cp discharge and the
honest status line landed, all conclusions conservative; but the
condition's SUFFICIENT form is mis-stated by the false "equivalently"
chain and the falsifier's restoration clause, leaving the granted-half
accounting one clause short at abstract EOS. L0-2 (AMENDMENT riding
E-2): **DISCHARGED** modulo the marker-scope residual (EL0-4).

==============================================================================
## SUMMARY

| ID | Leg | Passage | Class | One-line |
|---|---|---|---|---|
| EL0-3 | 5 | G8/r2 named condition + falsifier (l.2084-2102) | REPAIR-NEEDED | "e_SS > 0 (equivalently ... s-concavity ...)" false as equivalence; headline member insufficient (Grueneisen cross-term unpinned; boost+perspective congruence forces failure of item (i) at an in-class EOS with e_SS > 0); falsifier's "restores the unconditional grant" over-claims |
| EL0-1 | 3 | §13 E-1 retraction falsifier (l.2832-2836) | AMENDMENT | false-positive power: fires on nonzero mu with zero common pairing value, against the true divergence claim; add "with <mu, psi chi_0> != 0" |
| EL0-2 | 3 | (EU-x) equality rider (l.1216-1225) | AMENDMENT | "verbatim" passes a Lipschitz composite through machinery minted for smooth tests; one written clause owed (mollification admissibility + composite-as-psi reading absorbing the d_t D_W E(U) term) |
| EL0-4 | 5 | mediant/transfer conclusion (l.2126-2140) | AMENDMENT | categorical "TRANSFERS to W-space" outruns its EXPECTED-NOT-EXHIBITED premise; extend the marker across the colon |

CONFIRMED (cannot break, strongest attacks recorded in-section):
retraction preamble (3.1); (p1)/(p2)/(p3) core rewrite (3.2-3.4 — the
E-1 proof content is correct and complete as written); s = 0 /
two-point rewording (5.2 — judge act (iii) re-derived, DF_x
invertibility attack killed); mediant mechanism restoration (5.3,
premise level); honest status line + audit-line + gamma-table + §13
consistency edits (5.4 — no stale consumer found). Discharge verdicts:
E-1 discharged; E-2 discharged in substance with EL0-3 as the named
residual on the repair text itself.

Counts: 4 findings total = 1 REPAIR-NEEDED + 3 AMENDMENT;
**BREAKS-THE-LEG: 0**. No sustained objection re-opens; no statement,
rigor label, or route-level conclusion is touched by any finding
(EL0-3's repair, applied, STRENGTHENS the no-viable-abstract-EOS-route
conclusion a second time, mirroring L1-2's own effect).

## SELF-FALSIFIERS (what kills each finding)

- EL0-3(a): a proof that Gibbs closure + c^2 > 0 + theta > 0 + e_SS > 0
  imply e_vv e_ss - e_vs^2 >= 0 on any compact state region (kills the
  counterexample class — note my exhibit e0(v) + (a0 + a1 v) s +
  (b/2) s^2 with a1^2 > e0'' b is a direct refutation target: show it
  violates a §1 pin); or a classical W-convexity theorem for -rho g(S)
  consuming ONLY e_SS > 0 at general EOS (kills the insufficiency
  claim); or a demonstration that the boost map is not affine on W /
  the (rho, E)-slice Hessian congruence B^T (Hess f) B fails (kills the
  necessity chain).
- EL0-3(b): a derivation that e_SS > 0 + §1 pins imply the full grant
  (same as above — sufficiency).
- EL0-1: a proof that the falsifier's conditions (nonzero T-periodic
  mu >= 0, admissible psi, finite sum) force <mu, psi chi_0> != 0 —
  i.e. that my supp-disjoint psi is inadmissible under some clause of
  the display I missed.
- EL0-2: a citation of in-document text (before or at the rider) that
  states the Lipschitz-test admissibility for the WINDOWED pairing, or
  a demonstration that (p1)'s "torus test" class as minted includes
  Lipschitz tests.
- EL0-4: a derivation of the transfer claim NOT routed through the
  unexhibited subsonic-average pair (e.g. a proof that non-convexity of
  {u > c} in W holds unconditionally at abstract EOS — which would also
  upgrade the row).
- Any CONFIRMED verdict above: a derivation-level break of the quoted
  passage that my recorded strongest attack missed.

END — round-1 escalation refutation, lens l0. Machine summary:
{objections: 4, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc1_r1_l0.md}
