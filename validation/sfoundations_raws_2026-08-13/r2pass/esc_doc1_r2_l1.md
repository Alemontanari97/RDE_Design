# ESCALATION REFUTATION — DOC-1 E-1/E-2 repairs, until-dry ROUND 2, lens l1
# (gas dynamics / physics, RH algebra, counterexamples)

Date: 2026-08-19. Target: `phaseD/phaseD_stop_proof.md` AT REVISION 6 —
ONLY the escalation-repair text for legs 3 and 5 named by the NEWEST
revision-log entries (the §13 REVISION 6 block, lines 3198-3328, and
the body passages it edits: the G8/r2 CONDITION OF RECORD strict
rewrite + (m3) mechanism + AUD-cp strict discharge + re-recalibrated
falsifier, lines ~2116-2204; the grant clause "under the STRICT
condition of record", lines ~2205-2209; the propagation carriers:
header audit line ~88-92, honest status line ~2255-2265, §9 gamma
table ~2469-2476, §13 EL0-3 SUPERSEDED-IN-PART note ~3103-3115), PLUS
the revision-5 leg-3/leg-5 passages that have had NO lens-l1
adversarial coverage since they were written (the (EU-x) rider's two
written consumptions, lines ~1228-1241; the §13 E-1 falsifier bracket,
lines ~2958-2965; the (m2) chain and AUD-cp separability at their
revision-6 state).

ROUND-NUMBER / TARGET-REVISION DEVIATION, DECLARED: the launching
brief named the target's newest state as carrying "the escalation-
repair text for legs 3 and 5" and this consumption "until-dry ROUND
2" — the on-disk state is REVISION 6, which has ALREADY consumed the
round-2 lens-l0 refutation (`esc_doc1_r2_l0.md`, E2L0-1/E2L0-2). The
target's own revision-6 honest-residue item (2) declares the round-2
coverage asymmetry ("round 2 ran lens l0 only (no esc_doc1_r2_l1.md
on file) ... A lens-l1 pass over the revision-6 text is the natural
next round"). This document IS that lens-l1 pass: it completes the
two-lens round-2 coverage on the revision-6 text (leg 5) and gives
first lens-l1 coverage to the revision-5 leg-3 rider/falsifier edits
that l0 confirmed at its round 2. Output: `esc_doc1_r2_l1.md`, the
exact file the asymmetry declaration names.

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 rows L0-1/L1-1, L0-2,
L1-2 and §4(c) E-1/E-2 (the standing escalation specs, verified
discharged below); full objection texts `refute_r2batch_l0.md`
(L0-1/L0-2) and `refute_r2batch_l1.md` (L1-1/L1-2); prior escalation
rounds `esc_doc1_r1_l0.md` (EL0-1..EL0-4), `esc_doc1_r1_l1.md`
(ESC1-F1/F2 — my own round-1 record), `esc_doc1_r2_l0.md`
(E2L0-1/E2L0-2), all read at the attacked legs. Both duties executed:
(a) derivation-level attack on the revision-6 repair text; (b)
verification that the revision-6 repairs DISCHARGE the round-2
sustained findings they answer (and that the standing r2-batch and
round-1 dispositions hold).

DEDUP REGISTER (dispositioned objections NOT re-raised): L0-1/L1-1,
L0-2, L1-2 (r2-batch, consumed revisions 4/5, dispositions verified
§D below); EL0-1==ESC1-F1, EL0-2, EL0-3==ESC1-F2, EL0-4 (round 1,
consumed revision 5, verified discharged by the round-2 l0 pass; my
own ESC1-F1/F2 re-verified at my lens below); E2L0-1, E2L0-2 (round-2
l0, consumed revision 6, adequacy examined below). The one finding
below attacks REVISION-6 text that did not exist before revision 6 —
zero prior adversarial coverage at either lens — and declares its
distinction from every ID above. Every attacked passage: verbatim
quote + attack + class in {BREAKS-THE-LEG, REPAIR-NEEDED, AMENDMENT}.
Every examined passage not broken: CONFIRMED with the strongest
attack tried.

Finding ID: ER2L1-1. Line numbers are of the revision-6 file.

==============================================================================
## LEG 5 (E-2) — the revision-6 G8/r2 strict-condition rewrite

### 5.1 The sufficiency clause of the CONDITION OF RECORD — **OBJECTION
### ER2L1-1, AMENDMENT**

Quote (G8 row, lines 2116-2129, the revision-6 rewrite):
> "CONDITION OF RECORD, stated in its STRICT form in revision 6 per
> E2L0-1 (...): Hess e(v, S) positive DEFINITE on the
> comparison-segment hull, i.e. the strict pair e_vv > 0 (= c^2 > 0,
> already a §1 pin) AND the strict Grueneisen cross-term bound
> e_vv e_SS > (e_vS)^2 (unpinned by §1); e_SS > 0 (...) then FOLLOWS
> from the strict pair and remains the recorded shadow. Pointwise
> strictness plus compactness of the comparison-segment hull yields
> the uniform c of item (i) below."

and the grant it conditions (lines 2205-2206):
> "Granted, under the STRICT condition of record: (i) E(V|U) >=
> c|DeltaW|^2 with all comparison segments inside the convex physical
> region"

where E is introduced for the whole row at lines 2099-2100 as the
GENERIC Harten quadruple:
> "What W-convexity of E = -rho g(S) (Harten; Godlewski-Raviart —
> t-EVOLUTION facts) genuinely delivers"

Attack (derivation level — counterexample, my lens). The revision-6
sentence "Pointwise strictness plus compactness ... yields the
uniform c of item (i)" is the FIRST place the row asserts the
SUFFICIENCY direction (revisions 4/5 priced only necessity), and it
asserts it for E = -rho g(S) with g of record GENERIC. Under that
literal reading the claim is FALSE, by a witness built entirely from
facts of record IN THIS ROW:

Take the ideal gas at constant gamma (in-class instance; c_v =
R/(gamma-1) > 0). Its e(v, S) = K e^{S/c_v} v^{-(gamma-1)} satisfies
the STRICT condition of record everywhere: e_vv = gamma(gamma-1)e/v^2
> 0 and e_vv e_SS - (e_vS)^2 = (gamma-1) e^2/(c_v^2 v^2) > 0 (strict
PD Hess e, uniformly on compacts). Now take the quadruple
g(S) = exp(lambda S) with lambda > 1/c_v: g' = lambda g > 0
(admissible in the Harten family the row cites), and g''/g' = lambda
> 1/c_v. By the row's OWN recorded equivalence (lines 2138-2140:
"At ideal gas -rho f(S) is strictly convex iff f' > 0 AND
f''/f' < 1/c_v — a condition on g beyond g' > 0 (the g-condition
instance, kept)"), -rho g(S) is NOT convex in W — for lambda strictly
above 1/c_v the condition fails state-independently, so the W-Hessian
of E carries a NEGATIVE direction at every state, and E(V|U) < 0 for
in-hull pairs V near U along it: item (i) fails for EVERY c > 0,
WITH the strict condition of record satisfied. (At the boundary
lambda = 1/c_v the failure is the (m3)-style degenerate-direction
break, E(V|U) = o(|DeltaW|^2).) The printed condition of record,
read at the row's own generic g, does not deliver the printed grant.

Why this is a SCOPE defect and not a broken grant: the quadruple the
§4 proof actually consumes is FIXED — line 1169: "Take the certified
entropy quadruple g(S) = S (H7')." At g = S the sufficiency chain is
SOUND, and I verified it at pen grade: (1) strict PD of Hess e(v,S)
<=> strict concavity of s(v, eps) given theta > 0 (the null-line
transfer is rank-preserving: an affine direction of e maps to a
straight line in (v, eps) along which s is affine, and conversely);
(2) at rest states the W-Hessian of -rho S is BLOCK-DIAGONAL: the
(rho, E) block = tau B^T Hess(-s) B (the row's perspective
congruence, B = [[-tau, 0], [-eps, 1]] invertible), and the momentum
block = (1/(theta rho)) I > 0 — computed directly: d^2 eps/dm_i dm_j
= -delta_ij/rho^2 at m = 0, so d^2 E/dm_i dm_j = (s_eps/rho)
delta_ij, cross blocks vanishing by parity; (3) boost affinity
extends PD to all velocities by congruence; (4) continuity of
Hess_W E + pointwise PD on the compact hull gives the uniform
lambda_min, and the Bregman double integral gives item (i) with
c = lambda_min/2. NOTE the closing of the loop: at g = S the Harten
g-condition reads 0 < 1/c_v, i.e. c_v > 0 — which FOLLOWS from the
strict pair (e_SS > 0 => c_v = theta/e_SS > 0). That is exactly WHY
the printed condition self-suffices at the certified quadruple and at
no generic one: the strict pair contains the g-condition for g = S
and for no strongly convex g.

Class: **AMENDMENT** — by the loop's own severity calibus: the
delivered grant AS CONSUMED (g = S fixed by H7', the only quadruple
any §4 step uses) is intact; no in-class object breaks it; what is
defective is the false generality of the new sufficiency sentence,
whose benign reading is available and is the one every consumer uses
(all three kill chains (m1)/(m2)/(m3) instantiate g = id; §4 pins
g = S). Same class logic as E2L0-2 (ambiguous clause with a benign
reading, one-clause fix), NOT E2L0-1 (whose ">=" had no benign
reading of record). Repair, one clause: scope the condition-of-record
sufficiency sentence and the grant to the certified quadruple —
"yields the uniform c of item (i) below FOR THE CERTIFIED QUADRUPLE
g(S) = S (for a general Harten g the g-condition — ideal-gas instance
recorded below — enters additionally; at g = S it reduces to c_v > 0,
which the strict pair already contains)". Statement, labels,
route-level OPEN conclusion, gamma-table conclusions untouched; if
anything the accounting gets sharper (the abstract-EOS condition is a
condition on the (EOS, quadruple) PAIR, pinned at the pair actually
used).

PROVENANCE, declared: the unscoped sufficiency sentence was seeded by
the round-2 l0 repair spec itself (esc_doc1_r2_l0 §5.1 repair: "with
the note that pointwise strict + compactness of the segment hull
yields the uniform c of item (i)" — no g-scope) — the THIRD instance
in this loop of a repair-spec clause seeding the next round's finding
(after the ">=" of E2L0-1 and the "on K" of E2L0-2). Repair-spec text
is not exempt from refutation.

DEDUP DECLARATION: NOT a re-raise of L1-2 (absence of any named
condition), EL0-3/ESC1-F2 (scalar vs joint form), E2L0-1 (strictness
of the determinant member), or E2L0-2 (falsifier domain): all four
priced the EOS side of the condition; this prices the QUADRUPLE scope
of the sufficiency direction, asserted for the first time by
revision-6 text. The E2L0-1 disposition fails at exactly this new
clause and nowhere else (see §D).

### 5.2 The (m3) mechanism (determinant-boundary witness) — CONFIRMED

Quote (lines 2157-2175): "(m3) — the strictness rung, revision 6 per
E2L0-1 — the (m2) quadratic family AT its determinant boundary:
e0'' = a1^2/b CONSTANT (quadratic e0, a1 != 0, b > 0, a0 large), so
e_vv e_SS - (e_vS)^2 = (a1^2/b) b - a1^2 == 0 on the whole patch:
Gibbs closure, theta > 0, c^2 = v^2 a1^2/b > 0, e_SS = b > 0 and the
NON-strict determinant bound ALL hold, but Hess e(v, S) =
[[a1^2/b, a1], [a1, b]] is rank 1 — e is convex, NOT strictly, affine
along the constant null direction d0 = (b, -a1); through the same
boost-affinity + perspective-congruence chain the W-Hessian of
E = -rho S is positive SEMIdefinite with a nontrivial null direction
at every state over the patch, and along it the Bregman expansion
gives E(V|U) = 0 + O(|DeltaW|^3), so for EVERY fixed c > 0 the bound
E(V|U) >= c|DeltaW|^2 FAILS at small |DeltaW|".

Strongest attacks tried at my lens, all failed:
(a) *Pin audit on the patch*: Hess e = [[a1^2/b, a1], [a1, b]]
constant (e globally quadratic), null vector check
Hess.(b, -a1) = (a1^2 - a1^2, a1 b - a1 b) = 0 — checks; theta =
a0 + a1 v + b S > 0 for a0 large on a compact patch — checks; c^2 =
v^2 e_vv = v^2 a1^2/b > 0 — checks; Gibbs closure by DEFINING
p := -e_v, theta := e_S — checks against the §1 model (lines 188-192:
Gibbs closure + c^2 > 0 + theta > 0 "on the state region of
interest", NO stability pin, NO p-sign pin; and if a p > 0 convention
were pressed, shifting e0 by a steeply decreasing linear term keeps
e0'' and restores p > 0 on the patch — the witness is robust).
(b) *Null-direction transfer through the Legendre step*: along the
line (v, S) = (v0 + tb, S0 - t a1), e is affine, so its image in
(v, eps)-space is a STRAIGHT line along which s = S0 - a1 t is
affine — Hess s degenerates along a genuine direction; conversely s
strictly concave would force e strictly convex: transfer is
rank-faithful. Checks.
(c) *Does the W-null direction survive the momentum block?* At rest
states the full W-Hessian is block-diagonal with momentum block
(1/(theta rho)) I strictly positive (my §5.1 computation), so the
null vector lives purely in the (rho, E) plane, delivered by the
perspective congruence from the s-degenerate direction — exists,
nontrivial. Boost affinity carries it to every velocity. Checks.
(d) *Third-order honesty*: E is smooth in W over the patch (rho
bounded away from 0; s obtained by inverting a nondegenerate-in-S
quadratic), so the Bregman remainder along the null direction is a
genuine O(|DeltaW|^3) (and even o(|DeltaW|^2) would suffice to kill
every fixed c). Checks. (m3) does exactly what revision 6 needs it
to do: it separates the revision-5 non-strict triple from the grant.

### 5.3 The non-strict-triple placement sentence — CONFIRMED

Quote (lines 2130-2138): "The revision-5 printed NON-strict triple
(e_vv > 0 AND e_SS > 0 AND e_vv e_SS >= (e_vS)^2) does NOT suffice
for item (i): it sits strictly between positive-SEMIdefiniteness of
Hess e (which is what W-convexity itself FORCES — the necessity
direction, where '>=' is the correct form; the (m1)/(m2) kill chains
run there) and positive-DEFINITENESS, matching neither ((m3)
separates it from PD; the PSD state e_SS = e_vS = 0 with e_vv > 0
separates it from PSD)."

Strongest attack tried: break one of the four containment claims.
PD => triple (det > 0 with e_vv > 0 forces e_SS > 0): holds. Triple
=> PSD (2x2, positive diagonal, det >= 0): holds. (m3) is
triple-not-PD: holds (5.2). The exhibited state e_SS = e_vS = 0,
e_vv > 0 is PSD-not-triple and violates no §1 pin: holds. Also
checked the (m1) subcases against the necessity claim: e_SS < 0 or
(e_SS = 0, e_vS != 0) give det < 0 => not PSD => sign-reversal break;
(e_SS = 0, e_vS = 0) gives a degenerate direction => (m3)-style
break — "the (m1)/(m2) kill chains run there" is right in every
subcase. No hole.

### 5.4 The AUD-cp strict discharge — CONFIRMED

Quote (lines 2175-2185): "On the STANDING gamma(T) thermally-perfect
closure the FULL condition is DISCHARGED by the AUD-cp-class finite
audit (c_v > 0): s(tau, eps) = phi(eps) + R ln tau is SEPARABLE there
(cross term identically zero, Hessian diagonal), so joint concavity
reduces EXACTLY to c_v > 0 — and the revision-6 STRICT form is
discharged VERBATIM: the diagonal Hessian diag(-R/tau^2,
-1/(c_v T^2)) is strictly negative definite iff c_v > 0, uniformly on
compacts, with strict determinant R/(tau^2 c_v T^2) > 0 automatic".

Strongest attacks tried, all failed:
(a) *Re-derive the diagonal entries with VARIABLE c_v(T)* (the
gamma(T) point): s_tautau = -R/tau^2 unconditionally; phi'(eps) =
1/T(eps) with d eps = c_v dT gives phi''(eps) = -1/(c_v T^2) at the
state's own c_v(T) — the printed entries are exact for
thermally-perfect NON-constant c_v, no frozen-c_v approximation is
smuggled. Checks.
(b) *Strictness transfer to the condition of record*: strict ND of
diag(...) <=> c_v > 0, and via the (Legendre) equivalence of 5.1(1)
this IS strict PD of Hess e — "VERBATIM" is earned, and the strict
determinant is automatic exactly as printed. Checks.
(c) *Coverage channel — audit range vs hull*: could the hull's
temperature image exit the audited c_v > 0 range, holing the
"discharged IN FULL"? No: at the standing closure the EOS of record
IS the tabulated model — its domain is the table range, the §1 pins
are pinned on that domain, and hull states are states OF the model
(W-segments between physical states keep rho >= rho_min by convexity
and keep internal energy positive because rho*eps = E - |m|^2/(2 rho)
is CONCAVE along W-segments, hence above its chord); a hull point
outside the table range would be outside the model, not a discharge
hole. Attack fails.

### 5.5 The re-recalibrated falsifier (E2L0-2 repair) — CONFIRMED

Quote (lines 2196-2204): "derive joint s-concavity IN THE STRICT FORM
on the comparison-segment hull (equivalently: wherever the §1 pins
hold) from Gibbs closure + c^2 > 0 + theta > 0 ALONE, with no
K-geometry input — THAT kills the condition-claim and restores the
unconditional grant; deriving e_SS > 0 alone kills only the (m1)
necessity exhibit and leaves the grant conditional on the strict
cross-term bound (m2 and m3 stand as the witnesses)."

Strongest attacks tried, all failed:
(a) *Re-open the E2L0-2 domain hole*: the "no K-geometry input"
clause closes the K-restricted-derivation reading DIRECTLY — hull
geometry is K-derived, so a derivation exploiting hull bounds is
K-geometry input and is excluded by the literal text; the
"(equivalently: wherever the §1 pins hold)" parenthetical is then a
true paraphrase (a pins-only derivation holds on the whole pinned
region, which contains the hull by 5.4(c)) and carries no independent
restoration power. No false-restoration reading survives.
(b) *Residual-condition arithmetic*: with e_vv > 0 already pinned,
"e_SS > 0 derived" leaves exactly the strict cross-term bound as the
unpinned member — correct; and both named witnesses are the right
ones (m2: det < 0 with e_SS > 0; m3: det = 0 with e_SS > 0). Checks.
(c) *Unsatisfiability direction*: the demanded derivation is
impossible (m2/m3 are in-class), which is the correct calibration for
a falsifier of a TRUE condition-claim — it can fire only if the claim
is false. Checks. **E2L0-2: DISCHARGED** (and cleanly: no third
recalibration owed on this clause).
(One reading NOT closed by this clause is the quadruple scope of the
"restores the unconditional grant" consequent — but that is ER2L1-1's
defect in the condition clause itself, carried there, not
double-counted here.)

### 5.6 Propagation carriers — CONFIRMED modulo ER2L1-1 inheritance

Examined all four: header audit line (lines 88-92: "...and in its
STRICT form — positive-definite Hess e(v, S) on the
comparison-segment hull — per revision 6, E2L0-1"); honest status
line (lines 2255-2265: STRICT joint form + scalar shadow + "strict
form included" AUD-cp discharge); §9 gamma table (lines 2469-2476:
"stated STRICT — positive-definite Hess e on the comparison hull —
in revision 6 per E2L0-1 ... (separable s, strict form automatic);
table conclusions UNCHANGED"); §13 EL0-3 entry SUPERSEDED-IN-PART
note (lines 3103-3115 — accurate on both the ">=" and the "on K"
defects, prior text preserved per the document's supersession
convention). Strongest attack tried: hunt a stale carrier of the
revision-4 scalar form, the revision-5 non-strict triple, or a
"SUFFICIENT"-only claim outside a supersession/history context — grep
over SUFFICIENT/sufficient, s-concavity, Grueneisen, Bethe-Weyl,
comparison-segment: every hit is either the layered historical form
("SUFFICIENT ... per revision 5, and STRICT ... per revision 6") or
lives inside a superseded §13 entry or the historical revision-5
label summary (line 3177), which the revision-6 label summary (line
3303) supersedes in place. No stale carrier of record. All four
carriers speak the strict form; all four also carry the unscoped
sufficiency by reference to the condition of record — ER2L1-1 is
carried at the source clause once, not counted again.

### 5.7 The revision-6 log block (bookkeeping) — CONFIRMED

Examined (lines 3198-3328) against `esc_doc1_r2_l0.md`: the E2L0-1
and E2L0-2 consumption entries transcribe the l0 findings faithfully
(including the declared provenance notes); "ROUND-1 l1 DISPOSITIONS
VERIFIED" matches the l0 file's discharge section (my ESC1-F1/F2 are
correctly recorded as merged and consumed, with the ESC1-F2 residual
correctly identified as E2L0-1+E2L0-2); the round-number note and the
lens-l0-only coverage asymmetry are DECLARED and accurate against the
disk state; the dryness ledger ("leg 3 dry at lens l0; leg 5 not yet
dry"), the no-label-motion claim (consistent with VERDICT_r2pass
§4(a), [T-T0P] main already SCHEMA), the closed Blocco-2 gate (E-5/
E-6 not this document's to discharge), and the "third time in a row
STRENGTHENS" claim (L1-2 -> EL0-3 -> E2L0-1: each repair made the
named condition strictly stronger) all check. Strongest attack tried:
mis-transcription hunt + an over-claim of dryness or gate motion —
none found.

==============================================================================
## LEG 3 (E-1) — lens-l1 coverage of the revision-5 edits
## (zero revision-6 edits on this leg)

My round 1 (esc_doc1_r1_l1 P3.1-P3.4) already confirmed the
retraction ground and the (p1)-(p3) core at this lens; those verdicts
stand (strongest attacks on file there; re-checked only where the
rider interacts with them). New lens-l1 coverage below is of the
revision-5 text.

### 3.1 The (EU-x) rider's two written consumptions (EL0-2
### disposition) — CONFIRMED

Quote (lines 1228-1241): "TWO CONSUMPTIONS WRITTEN in revision 5 per
EL0-2 (...): (i) the composite Lipschitz multiplier (D_W E(U))_row
psi is an ADMISSIBLE test for the L^inf-coefficient weak form by
standard mollification (fluxes in L^inf on the slab; the windowed
test is W^{1,inf} with compact support — strictly weaker than the
non-windowed Gauss-Green consumption already itemized in G2); (ii)
the composite is taken AS the psi of (p1)-(p3), so the extra d_t-term
(d_t D_W E(U)) psi chi_0 is a FIELD term absorbed by (p2) —
d_t D_W E(U) is L^inf and T-periodic on the stratum-(A) slab (U C^1
there, H8') — and NOT a third cutoff-derivative term outside (p3)'s
two-term split d_t(psi chi_0) = (d_t psi) chi_0 + psi chi_0'."

Strongest attacks tried at my lens, all failed:
(a) *Mollification against merely-L^inf fluxes* (no continuity to
lean on): grad of the mollified test converges at every Lebesgue
point of the Lipschitz test's gradient (full measure, Rademacher)
with a uniform L^inf bound, so every flux pairing passes to the limit
by dominated convergence REGARDLESS of the coefficient's regularity —
the "standard mollification" claim needs nothing about F(V) beyond
L^inf. Checks.
(b) *Chain-rule/boundedness for (ii)*: d_t D_W E(U) = D^2_W E(U) d_t
U classically (U C^1 on the compact stratum-(A) slab, values in K
with rho >= rho_min keeping D^2_W E continuous there) — continuous on
a compact set, hence L^inf; T-periodic by H8'. (p2) needs T-periodic
L^1_loc: met with room. Checks.
(c) *Term inventory / no third cutoff term*: with Psi := D_W E(U) psi
in W^{1,inf}, d_t(Psi chi_0) = (d_t Psi) chi_0 + Psi chi_0'
distributionally (Lipschitz x smooth product rule), and d_t Psi =
(d_t D_W E(U)) psi + D_W E(U) d_t psi — BOTH field terms. The split
is exhaustive; no term escapes (p2)/(p3). Checks.
(d) *Sign discipline*: the equality pairing never invokes (p1)'s
nonnegativity — k-independence and (p2)/(p3) are sign-free, so the
composite test needs no sign, exactly as used. Componentwise testing
of the system then summing is legitimate. Checks.
(e) *A-fortiori accounting*: compactly-supported W^{1,inf} testing is
strictly contained in the itemized G2 consumption (Gauss-Green for
divergence-measure fields against NON-compactly-supported Lipschitz
tests on a per-sector C^{1,1} domain) — the comparison direction is
right, and no new conditional is silently minted. Checks.
**EL0-2: DISCHARGED at this lens too** (concurring with l0 round 2).

### 3.2 The §13 E-1 falsifier bracket (EL0-1/ESC1-F1 disposition —
### my own round-1 finding) — CONFIRMED

Quote (§13, lines 2958-2965): "[FALSIFIER RECALIBRATED in revision 5
per EL0-1/ESC1-F1 — as printed it has FALSE-POSITIVE power (the r2-F6
defect class): psi supported away from supp(mu) meets every printed
condition with a finite (zero) sum while the divergence claim, which
carves out the zero-common-value case, stands unrefuted. Firing
condition of record: a finite value of Sum_k <mu, psi chi_k> WITH
<mu, psi chi_0> != 0.]"

Strongest attacks tried (author of the merged finding, so held to the
harshest reading), all failed: (a) satisfiability — with mu >= 0 and
admissible psi, chi_k >= 0 every term is nonnegative; joint
T-periodicity makes them equal, so a nonzero window value forces
divergence: the recalibrated condition can fire ONLY on a genuine
k-independence failure, i.e. only by refuting the (p1) ground — the
correct calibration, and my round-1 supp-disjoint exhibit no longer
fires; (b) sign-cancellation orderings — excluded by the sign
constraints; (c) scope creep — the bracket still guards ONLY the
retraction ground and still records that a kill would not touch
(p1)-(p3) (which never sum over k). **ESC1-F1: DISCHARGED — verified
by its own author's lens.**

LEG 3 VERDICT AT THIS LENS: ZERO findings — with this pass the leg-3
escalation thread is DRY AT BOTH LENSES as of revision 6.

==============================================================================
## §D DISCHARGE VERDICTS (sustained findings vs the repairs of record)

- **E2L0-1 (REPAIR-NEEDED): DISCHARGED, with the ER2L1-1 residual in
  the NEW text it produced** — every demanded element landed and is
  verified above: strict pair of record with e_SS > 0 derived as
  shadow (5.1 check), non-strict triple re-scoped to the necessity
  direction with correct placement (5.3), (m3) recorded and verified
  at pen grade (5.2), grant clause re-headed "under the STRICT
  condition of record", AUD-cp discharge strengthened VERBATIM (5.4),
  propagation to all four carriers (5.6). The disposition fails ONLY
  at the unscoped sufficiency sentence it added (ER2L1-1, seeded by
  the l0 repair spec's own clause) and nowhere else.
- **E2L0-2 (AMENDMENT): DISCHARGED** (5.5 — the demanded strict-form
  + hull-domain + no-K-input clause, verified with no surviving
  false-restoration reading).
- Standing r2-batch objections, verified against the revision-6
  state: **L0-1/L1-1 DISCHARGED** ((p1)-(p3) written and confirmed at
  both lenses; the (EU-x) rider now carries its two written
  consumptions — 3.1); **L0-2 DISCHARGED** (s = 0 / two-point
  rewording and restored mediant clause confirmed at my round 1
  P5.4/P5.5, unchanged since); **L1-2 (my lens's own) DISCHARGED**
  (condition named, now in the strict joint form, AUD-cp-discharged
  at the standing closure, honest status line of record — the
  residue chain L1-2 -> ESC1-F2 -> E2L0-1 is fully consumed, modulo
  the ER2L1-1 scope clause).
- Round-1 findings **EL0-1==ESC1-F1, EL0-2, EL0-3==ESC1-F2, EL0-4:
  all DISCHARGED** (3.2, 3.1, 5.1-5.6, and the marker extension
  confirmed at l0 round 2 with nothing left for this lens to add —
  my round-1 mixing exhibit remains mechanism-level, so
  EXPECTED-NOT-EXHIBITED stays the honest marker).

The round is NOT dry: 1 finding sustained-by-this-refuter
(0 REPAIR-NEEDED + 1 AMENDMENT, 0 BREAKS-THE-LEG).

==============================================================================
## SUMMARY

| ID | Leg | Passage | Class | One-line |
|---|---|---|---|---|
| ER2L1-1 | 5 | condition-of-record sufficiency sentence (l.2127-2129) + grant head (l.2205-2206), E generic at l.2099 | AMENDMENT | the revision-6 sufficiency claim ("pointwise strictness + compactness yields the uniform c of item (i)") is unscoped over the quadruple: at ideal gas (strict PD Hess e holds) the Harten quadruple g = e^{lambda S}, lambda > 1/c_v breaks item (i) by the row's OWN recorded iff — the chain closes only at the certified g(S) = S, where the strict pair contains the g-condition (c_v > 0); repair = one scoping clause |

CONFIRMED (cannot break; strongest attacks recorded in-section):
(m3) determinant-boundary witness (5.2 — pin audit, rank-faithful
Legendre transfer, momentum-block computation, Bregman order);
non-strict-triple placement between PSD and PD (5.3 — all four
containments + (m1) subcases); AUD-cp strict discharge (5.4 —
variable-c_v(T) re-derivation, table-range attack rejected);
re-recalibrated falsifier (5.5 — no surviving false-restoration
reading; residual-condition arithmetic exact); propagation carriers
(5.6 — no stale form of record); revision-6 log block (5.7 —
transcriptions, merges, dryness ledger, gate status all accurate);
(EU-x) rider consumptions (3.1 — mollification vs L^inf
coefficients, chain rule, term inventory, sign discipline,
a-fortiori comparison); §13 E-1 falsifier bracket (3.2 —
satisfiability at the author's own lens). LEG 3: dry at BOTH lenses
as of this pass.

Counts: 1 finding total = 0 REPAIR-NEEDED + 1 AMENDMENT;
**BREAKS-THE-LEG: 0**. No statement, rigor label, or route-level
conclusion is touched; the repair, applied, PINS the abstract-EOS
condition to the (EOS, quadruple) pair actually consumed — the
accounting gets sharper, the OPEN verdict and the
no-viable-abstract-EOS-route conclusion stand.

## SELF-FALSIFIERS (what kills the finding and the verdicts)

- ER2L1-1: a demonstration that the row's E is of record PINNED to
  g(S) = S at the condition-of-record clause (some in-row text my
  read missed that scopes the quantifier — then the sentence has no
  false reading and the finding dies); or a proof that strict PD of
  Hess e(v, S) on the hull yields item (i) for EVERY Harten
  quadruple with g' > 0 — refuted in advance by my witness unless
  the witness itself fails: check that at ideal gas
  g''/g' = lambda > 1/c_v makes -rho g(S) non-convex (the row's own
  recorded iff at l.2138-2140) and that the strict condition of
  record holds at ideal gas (det Hess e = (gamma-1)e^2/(c_v^2 v^2)
  — re-derive; if either leg fails, the finding dies).
- Any CONFIRMED verdict above: a derivation-level break of the
  quoted passage that the recorded strongest attack missed.

END — until-dry round-2 escalation refutation, lens l1 (completes
the two-lens round-2 coverage; leg 3 dry at both lenses, leg 5 not
yet dry pending consumption of ER2L1-1). Machine summary:
{objections: 1, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc1_r2_l1.md}
