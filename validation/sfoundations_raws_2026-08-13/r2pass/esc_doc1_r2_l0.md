# ESCALATION REFUTATION — DOC-1 E-1/E-2 repairs, until-dry ROUND 2, lens l0
# (hyperbolic systems / functional-analytic rigor)

Date: 2026-08-19. Target: `phaseD/phaseD_stop_proof.md` AT REVISION 5 —
ONLY the escalation-repair text for legs 3 and 5 named by the NEWEST
revision-log entries (the §13 REVISION 5 block, lines 2989-3125, and
the body passages it edits: the G8/r2 condition clause + (m2) mechanism
+ AUD-cp strengthening + recalibrated falsifier, lines ~2099-2153; the
transfer-marker extension, lines ~2190-2198; the (EU-x) rider's two
written consumptions, lines ~1226-1240; the §13 E-1 falsifier bracket,
lines ~2901-2908; the propagation carriers: header audit line ~84-90,
honest status line ~2202-2211, §9 gamma table ~2402-2426, §13 L1-2
SUPERSEDED-IN-PART note ~2932-2939).

FILE-NAME / ROUND-NUMBER DEVIATION, DECLARED: the launching brief named
this slot "until-dry ROUND 1" with output `esc_doc1_r1_l0.md`. That
file EXISTS, is the CONSUMED round-1 record (its IDs EL0-1..EL0-4 are
cited of record in the target's REVISION 5 block), and overwriting it
would destroy the artifact the revision log cites. The brief's
operative targeting clause ("the newest revision-log entries name the
edited passages") resolves to the REVISION 5 block, whose honest-residue
item (1) states these round-2 repairs "await the next
escalation-refutation round" — this document IS that round. Output
therefore goes to `esc_doc1_r2_l0.md`; round-1 record untouched.

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 rows L0-1/L1-1, L0-2,
L1-2 and §4(c) E-1/E-2 (the standing escalation specs); full ROUND-1
objection texts `r2pass/esc_doc1_r1_l0.md` (EL0-1..EL0-4) and
`r2pass/esc_doc1_r1_l1.md` (ESC1-F1/F2), both read IN FULL; original
r2-batch texts `refute_r2batch_l0.md` / `refute_r2batch_l1.md` at the
attacked legs (dedup layer). Both duties executed: (a) derivation-level
attack on the revision-5 repair text; (b) verification that the
revision-5 repairs DISCHARGE the round-1 sustained findings they
answer.

DEDUP REGISTER (dispositioned objections NOT re-raised): L0-1/L1-1,
L0-2, L1-2 (r2-batch — consumed at revisions 4/5, dispositions verified
below); EL0-1==ESC1-F1, EL0-2, EL0-3==ESC1-F2, EL0-4 (round 1 —
consumed at revision 5, adequacy examined below). Where a finding
touches a dispositioned ID, the ID is cited and the failure point of
the disposition is stated. Both round-2 findings below attack
REVISION-5 text that did not exist before revision 5 — zero prior
adversarial coverage — and each declares its distinction from the ID
whose disposition produced the attacked line. Every attacked passage:
verbatim quote + attack + class in {BREAKS-THE-LEG, REPAIR-NEEDED,
AMENDMENT}. Every examined passage not broken: CONFIRMED with the
strongest attack tried.

Finding IDs: E2L0-1, E2L0-2. Line numbers are of the revision-5 file.

==============================================================================
## LEG 5 (E-2) — the revision-5 G8/r2 condition rewrite

### 5.1 The condition of record ("THREE conditions") — **OBJECTION
### E2L0-1, REPAIR-NEEDED**

Quote (G8 row, lines 2109-2119): "the classical results cited run on
FULL thermodynamic stability = JOINT concavity of s as a function of
(specific volume, internal energy) — the Bethe-Weyl class, the same
class G7 route r-a already names — equivalently (theta > 0, partial
Legendre inversion) JOINT convexity of e(v, S), i.e. THREE conditions:
e_vv > 0 (= c^2 > 0, already a §1 pin) AND e_SS > 0 (= c_v > 0 via
c_v = theta/e_SS: the necessary scalar shadow, the part revision 4
named) AND the Grueneisen cross-term bound e_vv e_SS >= (e_vS)^2
(equally unpinned by §1)."

And the grant it conditions (lines 2153-2157): "Granted, under that
condition: (i) E(V|U) >= c|DeltaW|^2 with all comparison segments
inside the convex physical region".

Attack (derivation level). The determinant member is printed NON-STRICT
(">="), and that is the NECESSITY-direction inequality transplanted
into the SUFFICIENCY slot. Provenance is visible: both round-1 texts
used ">=" where it is correct — in the necessity chains ("joint
convexity of e(v, s), i.e. to the THREE conditions ... AND the
determinant/cross-term condition e_vv e_SS >= (e_vS)^2", esc_doc1_r1_l1
P5.1 step (1); same in esc_doc1_r1_l0 §5.1(a)) — i.e. in deriving what
W-convexity FORCES. Revision 5 ported that inequality into the
condition OF RECORD under which item (i) is GRANTED. The two roles need
different strictness:

(a) *In-class breaking exhibit (m3) — the full printed condition
satisfied, delivered item (i) broken.* Take the row's OWN (m2)
quadratic family at its determinant boundary: e(v, S) = e0(v)
+ (a0 + a1 v) S + (b/2) S^2 with b > 0, a1 != 0, and e0'' = a1^2/b
CONSTANT (a quadratic e0), a0 large. Then on a compact patch:
Gibbs closure holds by construction (p := -e_v, theta := e_S);
theta = a0 + a1 v + b S > 0 (a0 large); e_vv = a1^2/b > 0, so
c^2 = v^2 e_vv > 0; e_SS = b > 0; and the printed Grueneisen bound
HOLDS: e_vv e_SS - (e_vS)^2 = (a1^2/b) b - a1^2 = 0 >= 0. ALL THREE
printed conditions are satisfied on the whole patch. But the
(v, S)-Hessian [[a1^2/b, a1], [a1, b]] is singular (rank 1): e(v, S)
is convex but NOT strictly — it is affine along the constant null
direction d0 = (b, -a1). Through the row's own verified chain (theta >
0 partial-Legendre inversion; then, at rest states, the perspective
congruence Hess_(rho,E)[-rho s] = tau B^T Hess(-s) B with
B = [[-tau, 0], [-eps, 1]] invertible; boost affinity extends to all
velocities), the W-Hessian of E = -rho S is positive SEMIdefinite with
a nontrivial null direction at every state over the patch. Along that
null direction at any base state U: E(V|U) = (1/2)(DeltaW)^T
Hess E(W_U) DeltaW + O(|DeltaW|^3) = 0 + O(|DeltaW|^3), so for EVERY
fixed c > 0 the bound E(V|U) >= c|DeltaW|^2 FAILS for small enough
|DeltaW| along that direction. Delivered item (i) breaks WITH the full
revision-5 condition of record satisfied. This is exactly the
degenerate-direction mechanism the round-1 record already holds for
the DIAGONAL member (esc_doc1_r1_l1 P5.2: "e_SS = 0 kills the UNIFORM
quadratic lower bound c|DeltaW|^2 (degenerate direction)") — revision
5 consumed that logic for e_SS (kept strict, > 0) and dropped it for
the determinant member (printed >=).

(b) *The "i.e." gloss fails as an equivalence in both readings.*
Joint convexity of e(v, S) (the standard, non-strict reading of "JOINT
concavity of s" through the Legendre step) is PSD of the Hessian:
e_vv >= 0 AND e_SS >= 0 AND det >= 0 — it does NOT imply the printed
strict diagonal members (e_SS = e_vS = 0 with e_vv > 0 is PSD and
in-§1-class). STRICT joint convexity (what the classical strict
statements and the grant's uniform c actually run on) is e_vv > 0 AND
det > 0 — strictly stronger than the printed triple, by (a). The
printed "i.e. THREE conditions" matches NEITHER: it sits strictly
between PSD and PD. (The two-way implications that ARE true: the
printed triple => PSD, since a symmetric 2x2 with positive diagonal
and nonnegative determinant is PSD; and PD => the printed triple.)

Class: **REPAIR-NEEDED** — same severity logic the judge applied to
L1-2 and round 1 applied to EL0-3/ESC1-F2, and the same test decides
it: a mathematical object in class separates the printed condition
from the delivered grant, so the accounting text must change, not
merely its wording. Not BREAKS: no statement, label, or route-level
conclusion moves — the OPEN verdict, the two-piece residue, and the
no-viable-abstract-EOS-route conclusion all survive and are (a third
time) STRENGTHENED, mirroring L1-2's and EL0-3's own effect. Repair
(one clause + propagation): state the condition of record in its
STRICT form on the comparison region — e_vv > 0 AND
e_vv e_SS > (e_vS)^2 on the comparison-segment hull (equivalently:
Hess e(v, S) positive DEFINITE there; e_SS > 0 then follows and stays
as the recorded scalar shadow) — with the note that pointwise strict
+ compactness of the segment hull yields the uniform c of item (i);
scope the "i.e." to the strict pair; keep (m2) as the interior witness
and record (m3) (the det = 0 boundary case) as the witness that
non-strict does not suffice. Propagation by reference: the header
audit line ("stated in its SUFFICIENT ... form", lines 88-89), the §9
gamma table ("named in its SUFFICIENT form", lines 2415-2417), the
honest status line (lines 2205-2210), the §13 revision-5 entry (lines
3015-3021) and the revision-5 label summary ("now stated in its
sufficient JOINT form", lines 3106-3107) all inherit this finding by
their word "SUFFICIENT" — carried here once, not double-counted.

DEDUP DECLARATION: NOT a re-raise of EL0-3/ESC1-F2 — those priced the
revision-4 SCALAR naming as insufficient and demanded the joint form;
revision 5 delivered the joint form and the demanded pieces (verified
in 5.3-5.4 below), but the delivered transcription mis-calibrates the
determinant member's strictness — text that did not exist before
revision 5. The round-1 dispositions themselves seeded the ">=" (their
necessity-direction displays), so the disposition of EL0-3 fails at
exactly this point and nowhere else: cited per the dedup rule. Not a
re-raise of L1-2 (absence of any condition) or r2b-F1 (coercivity
conflation) either.

### 5.2 The recalibrated falsifier — **OBJECTION E2L0-2, AMENDMENT**

Quote (G8 row, lines 2144-2153): "FALSIFIER of the condition-claim
(RECALIBRATED in revision 5 — the revision-4 clause 'derive e_SS > 0
... restores the unconditional grant' over-claimed sufficiency of the
scalar shadow): derive JOINT s-concavity on K from Gibbs closure +
c^2 > 0 + theta > 0 alone — THAT kills the condition-claim and
restores the unconditional grant; deriving e_SS > 0 alone kills only
the (m1) necessity exhibit and leaves the grant conditional on the
cross-term bound (m2 stands as the witness)."

Attack (derivation level — false-restoration power on the DOMAIN, plus
inherited strictness). The grant (i) quantifies over "all comparison
segments inside the convex physical region"; W-segments between
K-states LEAVE K — that is this row's own central point (the hull
problem; "the Mach-box preimage is non-convex in m-coordinates"). The
printed restoration clause accepts a derivation of joint s-concavity
"ON K". The clause "from the §1 pins alone" admits the reading "using
the pins PLUS K-membership" (a derivation exploiting, e.g., the
supersonic bounds of K, valid only on K) — under that reading the
falsifier declares the grant RESTORED while the condition remains
uncertified at segment points OUTSIDE K, where item (i) needs it. That
is false-restoration power: the same defect class as the revision-4
clause this falsifier was recalibrated to fix (over-claiming what a
weaker derivation restores), one axis over (domain instead of condition
strength). Secondarily, "JOINT s-concavity" non-strict does not
restore the STRICT sandwich (E2L0-1(a)); the restoring derivation must
deliver the strict form on the hull. Strongest defense considered
(recorded per the falsifier discipline): if "from the §1 pins alone"
is read as excluding any K-geometry input, a pins-only derivation
holds wherever the pins hold — the whole §1 model region — and "on K"
is then merely redundant. But a rejector/restoration clause must be
unambiguous under its LITERAL reading (R5; this document's own
standard, twice applied at exactly this defect class: r2-F6 and
EL0-1/ESC1-F1), and the literal reading admits the K-restricted
derivation. Class: **AMENDMENT** (falsifier calibration; auxiliary
text — no proof content or label exposed; same class as EL0-1).
Repair, one clause: "derive joint s-concavity, in the strict form,
on the comparison-segment hull (equivalently: wherever the §1 pins
hold) from the pins alone". Provenance note, declared: "on K" was
transcribed verbatim from round-1 esc_doc1_r1_l0 §5.1's own repair
clause — the round-1 spec seeded the defect; this attack is on the
of-record revision-5 text, and the EL0-3 disposition fails only at
this transcribed clause. DEDUP: not a re-raise of EL0-3(b) (which
priced the SCALAR restoration over-claim, now fixed).

### 5.3 The (m2) breaking mechanism + boost/perspective kill chain —
### CONFIRMED

Quote (lines 2124-2137): "(m2) — one rung deeper, revision 5 —
abstract EOS with ALL of c^2 > 0, theta > 0, e_SS > 0 but the
determinant bound violated (quadratic patch e = e0(v) + (a0 + a1 v) S
+ (b/2) S^2 with e0'' > 0, b > 0, a0 large, a1^2 > e0'' b: Gibbs
closure holds by construction, all §1 pins + e_SS > 0 hold, yet
s(tau, eps) is NOT concave) ALSO breaks item (i): a Galilean boost is
AFFINE on W and leaves -rho S invariant, and at rest states the
(rho, E)-slice Hessian of -rho s(1/rho, E/rho) is CONGRUENT to
Hess(-s) via the invertible perspective factor B = [[-tau, 0],
[-eps, 1]], so W-convexity FORCES joint s-concavity — the FULL joint
condition, not its e_SS shadow, is LOAD-BEARING for the granted half."

Strongest attacks tried, all failed:
(a) *Patch pins*: theta = a0 + a1 v + b S > 0 on a compact patch for
a0 large — holds; c^2 = v^2 e0''(v) > 0 — holds (the S-coupling is
linear in v, so e_vv = e0''); e_SS = b > 0 — holds; Gibbs closure by
construction — holds (p, theta DEFINED from e). det = e0'' b - a1^2
< 0 by choice: e not jointly convex, hence (theta > 0 Legendre step)
s not concave. Exhibit checks.
(b) *Boost affinity*: for fixed u0 the map (rho, m, E) -> (rho,
m + rho u0, E + m.u0 + rho|u0|^2/2) is linear in W; eps' = E'/rho
- |u'|^2/2 = eps (the cross terms cancel identically — re-derived);
so S and -rho S are boost-invariant and Hessians at boosted states are
congruent to rest-state Hessians. Checks.
(c) *Perspective congruence at pen grade*: with f(tau, eps) = -s and
h(rho, E) = rho f(1/rho, E/rho), direct differentiation gives
h_EE = tau f_ee, h_rhoE = -tau(tau f_te + eps f_ee), h_rhorho =
tau(tau^2 f_tt + 2 tau eps f_te + eps^2 f_ee) — assembling,
Hess h = tau B^T (Hess f) B with B = [[-tau, 0], [-eps, 1]],
det B = -tau != 0. EXACTLY the printed congruence (the positive scalar
tau = 1/rho is the "perspective factor" prose). Checks.
(d) *Slice sufficiency*: {m = 0} and the (rho, E) 2-plane are affine
in W, so W-convexity restricts to slice convexity and the congruence
transfers a negative f-direction back to a negative W-direction:
"W-convexity FORCES joint s-concavity" checks, and the
determinant-violating point kills item (i) at every in-region state
over the patch. No hole. (The strictness point of E2L0-1 lives in the
CONDITION clause, not in this mechanism, whose logic is the necessity
direction — where >= / contrapositive reasoning is the correct form.)

### 5.4 The AUD-cp strengthening (separability) — CONFIRMED

Quote (lines 2137-2143): "On the STANDING gamma(T) thermally-perfect
closure the FULL condition is DISCHARGED by the AUD-cp-class finite
audit (c_v > 0): s(tau, eps) = phi(eps) + R ln tau is SEPARABLE there
(cross term identically zero, Hessian diagonal), so joint concavity
reduces EXACTLY to c_v > 0 — the condition prices the ABSTRACT-EOS
accounting only."

Strongest attack tried: push the E2L0-1 strict form through the
discharge — does c_v > 0 still discharge it? Yes, and only the strict
reading makes "EXACTLY" right: the Hessian is diag(-R/tau^2,
-1/(c_v T^2)) — s_tautau < 0 unconditionally, s_epseps < 0 iff
c_v > 0, cross term IDENTICALLY zero, so the Hessian is strictly
negative definite iff c_v > 0, uniformly on compacts. The discharge
note survives the E2L0-1 repair VERBATIM (strict determinant
= R/(tau^2 c_v T^2) > 0 automatic given c_v > 0). Also verified:
s(tau, eps) = Int deps/T(eps) + R ln tau for p = rho R T, e = e(T) —
the separable form is correct. No hole; and this section is the reason
E2L0-1 touches the abstract-EOS accounting ONLY, exactly as the row
scopes it.

### 5.5 The transfer-marker extension (EL0-4 disposition) — CONFIRMED

Quote (lines 2190-2198): "the hull obstruction is EXPECTED to transfer
to W-space (marker extended across the colon in revision 5 per EL0-4 —
the revision-4 text printed the transfer CATEGORICALLY while its sole
support, the subsonic-average pair, carries the EXPECTED-NOT-EXHIBITED
marker above; the conclusion now inherits it; the direction is
conservative — were the transfer to fail, r2 would look BETTER and the
OPEN verdict is safe either way)."

Strongest attacks tried: (a) does "r2 would look BETTER" over-claim in
the failure branch? No — if {u > c} were convex in W the hull
obstruction disappears but the two-point coercivity obstruction (the
row's named open piece) stands untouched; one obstruction fewer =
"better", burden allocation unchanged. (b) Does the extended marker
under-claim (the mechanism IS verified)? No — the row keeps the
mechanism/pair honesty split of record ("the mixing mechanism,
verified by l1's exhibit ... the pair is EXPECTED-NOT-EXHIBITED"),
and only the conclusion's modality moved. Exactly the round-1 demanded
amendment, correctly scoped. **EL0-4: DISCHARGED.**

### 5.6 Propagation carriers — CONFIRMED modulo E2L0-1 inheritance

Examined: header audit line (lines 84-90: "... a named
thermal-stability condition on its granted half, stated in its
SUFFICIENT joint s-concavity / Bethe-Weyl form per revision 5,
EL0-3/ESC1-F2"); honest status line (lines 2202-2211: joint form +
scalar shadow + AUD-cp separability); §9 gamma table (lines 2402-2426:
"named in its SUFFICIENT form, joint s-concavity / Bethe-Weyl class,
in revision 5 per EL0-3/ESC1-F2 ... separable s; table conclusions
UNCHANGED"); §13 revision-4 L1-2 entry SUPERSEDED-IN-PART note (lines
2932-2939, prior text preserved — conforms to the document's
supersession convention). Strongest attack tried: hunt a stale carrier
of the revision-4 scalar form or of the false "equivalently" chain
outside a retraction/supersession context — grep over e_SS /
s-concavity / Bethe-Weyl / "equivalently" found NONE (the only scalar
"equivalently" survivors are the correctly scoped e_SS/c_v pair, body
and §13; the rev-4 wording survives only inside its superseded §13
entry). All four carriers speak the joint form coherently; all four
carry the word "SUFFICIENT(-form)", inheriting E2L0-1 by reference —
carried there, not counted again.

==============================================================================
## LEG 3 (E-1) — the revision-5 edits

### 3.1 The §13 falsifier recalibration (EL0-1/ESC1-F1 disposition) —
### CONFIRMED

Quote (§13, lines 2901-2908): "[FALSIFIER RECALIBRATED in revision 5
per EL0-1/ESC1-F1 — as printed it has FALSE-POSITIVE power (the r2-F6
defect class): psi supported away from supp(mu) meets every printed
condition with a finite (zero) sum while the divergence claim, which
carves out the zero-common-value case, stands unrefuted. Firing
condition of record: a finite value of Sum_k <mu, psi chi_k> WITH
<mu, psi chi_0> != 0.]"

Strongest attacks tried, all failed:
(a) *False-positive channel re-opened?* No: with mu >= 0 and
admissible psi >= 0 all pairings are >= 0; under k-independence they
are equal, so <mu, psi chi_0> != 0 forces partial sums N x (positive
const) -> +inf — the firing condition is unsatisfiable exactly when
the divergence claim is TRUE, which is the correct calibration for a
rejector of that claim (fires only via a genuine k-dependence failure,
e.g. terms decaying to 0 with a nonzero window value — precisely a
refutation of the (p1) ground). The round-1 supp-disjoint exhibit no
longer fires (its common value is zero).
(b) *Sign-cancellation channel*: closed by the sign constraints
(mu >= 0, psi >= 0) — no conditionally-convergent ordering exists.
(c) *Ambiguity of record*: the miscalibrated revision-4 clause still
stands above the bracket — but the bracket names the "firing condition
OF RECORD", the document's established supersession form (same
convention as the §13 L1-2 note); no consumer of the old clause found.
(d) *Coverage*: the falsifier still guards ONLY the retraction ground,
and the entry still records that a kill would not touch (p1)-(p3),
which never sum over k — unchanged, correct. **EL0-1/ESC1-F1:
DISCHARGED** — the demanded one-clause form, correctly calibrated.

### 3.2 The (EU-x) rider's two written consumptions (EL0-2
### disposition) — CONFIRMED

Quote (lines 1226-1240): "TWO CONSUMPTIONS WRITTEN in revision 5 per
EL0-2 (the revision-4 'applying (p1)-(p3) verbatim' left both to the
reader): (i) the composite Lipschitz multiplier (D_W E(U))_row psi is
an ADMISSIBLE test for the L^inf-coefficient weak form by standard
mollification (fluxes in L^inf on the slab; the windowed test is
W^{1,inf} with compact support — strictly weaker than the non-windowed
Gauss-Green consumption already itemized in G2); (ii) the composite is
taken AS the psi of (p1)-(p3), so the extra d_t-term
(d_t D_W E(U)) psi chi_0 is a FIELD term absorbed by (p2) —
d_t D_W E(U) is L^inf and T-periodic on the stratum-(A) slab (U C^1
there, H8') — and NOT a third cutoff-derivative term outside (p3)'s
two-term split d_t(psi chi_0) = (d_t psi) chi_0 + psi chi_0'."

Strongest attacks tried, all failed:
(a) *Boundedness chain for (ii)*: d_t D_W E(U) = D^2_W E(U) . d_t U;
U is C^1 on the compact stratum-(A) slab with values in K (rho >=
rho_min keeps D^2_W E continuous and bounded on the compact state
range), so d_t D_W E(U) is continuous on a compact set, hence L^inf;
T-periodicity from H8'. (p2) needs exactly T-periodic L^1_loc — met
with room. Checks.
(b) *Product rule with a Lipschitz psi in (p3)*: d_t(Psi chi_0) =
(d_t Psi) chi_0 + Psi chi_0' holds distributionally for
Psi in W^{1,inf} times chi_0 in C_c^inf — standard; and with the
composite AS Psi, d_t Psi = (d_t D_W E(U)) psi + D_W E(U) d_t psi,
both field terms: the term inventory is complete, no third
cutoff-derivative term exists. Checks.
(c) *The a-fortiori comparison*: the windowed test is W^{1,inf} with
COMPACT support, so its admissibility is plain mollification-density
with no boundary/trace terms; the itemized G2 consumption (Gauss-Green
for divergence-measure fields against non-compactly-supported
Lipschitz tests on a per-sector C^{1,1} domain) strictly contains it.
"Strictly weaker ... covered a fortiori" is sound accounting, and the
word "verbatim" is confirmed dropped from the sentence (grep: no
occurrence in the rider). Checks. **EL0-2: DISCHARGED** — both owed
clauses written, and the written clauses are correct.

==============================================================================
## THE REVISION-5 LOG BLOCK ITSELF (bookkeeping) — CONFIRMED

Examined (lines 2989-3125) against both round-1 files: the discharge
verdicts transcribed ("E-1 DISCHARGED (both lenses); E-2(b)/L0-2
DISCHARGED; E-2(a)/L1-2 PARTIALLY DISCHARGED (l1) /
discharged-in-substance-with-named-residue (l0)") MATCH the round-1
records verbatim in substance; the merges (EL0-1 == ESC1-F1,
EL0-3 == ESC1-F2) are correct; the distinct-defect count "4 (1
REPAIR-NEEDED + 3 AMENDMENT, 0 BREAKS-THE-LEG)" is arithmetically
right under the merges; the CONFIRMED-passages ledger matches the two
files' confirmed sections item-for-item (incl. the L-XSON3
subsonic-invertibility kill and l1's pen-grade mixing construction);
"NO label motion" is consistent with VERDICT_r2pass §4(a) ([T-T0P]
main already SCHEMA); honest-residue items (1)-(3) are accurate — in
particular item (1) correctly declares the round-2 repairs
UNADJUDICATED and the loop NOT dry, and item (2) correctly keeps the
Blocco-2 gate CLOSED (E-5/E-6 not this document's to discharge).
Strongest attack tried: hunt a mis-transcribed verdict or an
over-claim of dryness/closure — none found. The one substantive
defect in the block is the §13 EL0-3 entry's condition transcription
(lines 3015-3021, ">=" + "on K" falsifier), already carried as
E2L0-1/E2L0-2.

==============================================================================
## DISCHARGE VERDICTS (round-1 sustained findings vs revision-5 repairs)

- **EL0-1 == ESC1-F1 (AMENDMENT): DISCHARGED** (3.1 — the demanded
  clause, verified correctly calibrated).
- **EL0-2 (AMENDMENT): DISCHARGED** (3.2 — both owed consumptions
  written and correct).
- **EL0-3 == ESC1-F2 (REPAIR-NEEDED): DISCHARGED AS SPECIFIED, with a
  NEW named residual in the transcription** — every demanded element
  landed (joint/Bethe-Weyl naming; "equivalently" scoped to the
  e_SS/c_v pair; (m2) witness recorded and verified; AUD-cp discharge
  strengthened to the full joint condition via separability; falsifier
  recalibrated off the scalar shadow; propagation to all four
  carriers); but the delivered condition-of-record mis-calibrates the
  determinant member (non-strict ">=", E2L0-1) and the recalibrated
  falsifier carries a domain over-claim ("on K", E2L0-2) — both partly
  seeded by the round-1 repair specs' own wording, both breaking the
  printed grant/restoration at in-class witnesses. The dispositions
  fail at exactly these two clauses and nowhere else.
- **EL0-4 (AMENDMENT): DISCHARGED** (5.5 — marker extended, correctly
  scoped).

The round is NOT dry: 2 findings sustained-by-this-refuter (1
REPAIR-NEEDED + 1 AMENDMENT, 0 BREAKS-THE-LEG).

==============================================================================
## SUMMARY

| ID | Leg | Passage | Class | One-line |
|---|---|---|---|---|
| E2L0-1 | 5 | condition of record, G8 row (l.2109-2119) + grant (l.2153-2157); inherited by header/status/§9/§13 "SUFFICIENT" | REPAIR-NEEDED | Grueneisen member printed non-strict (">=") — the necessity-direction inequality in the sufficiency slot; (m3) boundary witness (quadratic patch, e0'' = a1^2/b, det == 0) satisfies ALL printed conditions yet breaks item (i)'s uniform c (null-direction Bregman O(|DeltaW|^3)); "i.e. THREE conditions" matches neither PSD nor PD |
| E2L0-2 | 5 | recalibrated falsifier (l.2144-2153) | AMENDMENT | restoration clause "joint s-concavity ON K ... restores the grant" has false-restoration power on the domain (segments leave K — the row's own hull point) and inherits the strictness gap; repair: strict form on the comparison-segment hull |

CONFIRMED (cannot break, strongest attacks recorded in-section):
(m2) mechanism + boost-affinity + perspective-congruence kill chain
(5.3 — congruence re-derived at pen grade, Hess h = tau B^T Hess f B);
AUD-cp separability strengthening (5.4 — survives the E2L0-1 strict
form verbatim; "EXACTLY" right only in the strict reading); EL0-4
marker extension (5.5); propagation carriers (5.6 — no stale scalar
form of record); EL0-1/ESC1-F1 falsifier recalibration (3.1 —
satisfiability analysis: fires only on a genuine k-independence
failure); EL0-2 rider consumptions (3.2 — boundedness chain, Lipschitz
product rule, a-fortiori comparison all check); the revision-5 log
block's bookkeeping (verdict transcriptions, merges, counts, honest
residue).

Counts: 2 findings total = 1 REPAIR-NEEDED + 1 AMENDMENT;
**BREAKS-THE-LEG: 0**. No statement, rigor label, or route-level
conclusion is touched by either finding; E2L0-1's repair, applied,
STRENGTHENS the no-viable-abstract-EOS-route conclusion a third time
(the condition gets strictly stronger), mirroring L1-2's and EL0-3's
own effects. The E-1 side (leg 3) is CLEAN at this round: zero
findings — its escalation thread is dry at lens l0 as of revision 5.

## SELF-FALSIFIERS (what kills each finding)

- E2L0-1: a proof that item (i) (E(V|U) >= c|DeltaW|^2, some c > 0
  uniform on the comparison region) HOLDS for the (m3) patch — i.e.
  that the null direction of the constant-rank-1 Hessian does not
  produce E(V|U) = o(|DeltaW|^2) at some in-region base state (my
  chain: boost reduction to rest states + the slice congruence + the
  second-order Taylor of the Bregman functional — refute any link);
  or a demonstration that the (m3) patch violates a §1 pin on every
  neighborhood (checked: theta > 0, c^2 = v^2 a1^2/b > 0, e_SS = b >
  0, Gibbs by construction — exhibit the violation); or a reading of
  the printed row under which the condition of record is demonstrably
  the STRICT form (no such reading found: ">=" is the operative
  of-record inequality in body and §13 both).
- E2L0-2: a demonstration that the printed clause "from Gibbs closure
  + c^2 > 0 + theta > 0 alone" EXCLUDES, as of-record text, any
  K-membership input (making "on K" redundant rather than
  miscalibrated), together with a strictness-carrying reading of
  "JOINT s-concavity" — then the falsifier has no false-restoration
  reading and the finding dies.
- Any CONFIRMED verdict above: a derivation-level break of the quoted
  passage that my recorded strongest attack missed.

END — until-dry round-2 escalation refutation, lens l0. Machine
summary: {objections: 2, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc1_r2_l0.md}
