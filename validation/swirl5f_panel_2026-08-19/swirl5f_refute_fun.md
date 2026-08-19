# REFUTATION REPORT — lens 'fun' — adversarial referee pass on
# swirl5f_fun.md ("cycle-mean thrust = mu-integral of per-phase
# thrusts": exact half / approximation half / error magnitude /
# value transfer)
#
# Referee: independent subagent, 2026-08-19. NO repo file modified.
# Method: the central algebra was RE-DERIVED FROM SCRATCH from the
# record sources (all read at the cited anchors this window: M0
# 341-685, T3QS whole, problem book SS2/3/5/8/9, theorem ledger SS3
# block 90-190, phaseD_meanswirl D.9/D.10/D.17/D.18/D.19/D.20/S.22,
# VERDICT SS3.2, N6 whole, C51, D6:280-291/484-493/773-780), THEN
# diffed against the target file. Discipline labels as in the target.
#
# HEADLINE: no CRITICAL defect. 2 MAJOR defects, both localized in
# the SS2.3 corrector-identification link (an internally inconsistent
# dual-normalization equation chain — the target's own FLAG F-5
# hazard, committed in its own display — and a silent argument switch
# K(V_3D) -> K(W_A)); both are repairable by declared sentences with
# NO change to any conclusion's order. 5 MINOR defects. All four
# main claims otherwise reproduce under independent derivation.

==============================================================================
## SS-A INDEPENDENT DERIVATIONS (done first, before the diff)

### A.1 Sector-decomposition identity (target Prop. 1)

Hypotheses taken: strict T0 (q(x,r,theta,t) = q~(x,r,phi),
phi = theta - Omega t, q~ 2pi/n-periodic in phi, piecewise-C^1,
transversal wave-steady fronts); S fixed axisymmetric enclosing the
engine; Pa constant; G := rho u_x (u.n) + (p - Pa) n_x in
L^1(C_S x S^1).

Step 1 (constancy). F_S(t) = Int_0^{2pi} Int_{C_S} G(l, theta -
Omega t) r dl dtheta; the substitution theta -> theta + Omega t is a
measure-preserving rotation of S^1 at each fixed t, so F_S(t) =
F_S(0). Hence J_exact := lim_T (1/T) Int_0^T F_S dt = F_S(0).
[= M0 [T-T0](i); reproduced.]

Step 2 (Fubini). F_S(0) = Int_0^{2pi} F_sect(phi) dphi,
F_sect(phi) := Int_{C_S} G(l,phi) r dl. Legitimate by Tonelli-Fubini
on the product; front traces on S are 1-D curves (measure zero), G
bounded. [Reproduced.]

Step 3 (Z_n). 2pi/n-periodicity of G in phi gives
Int_0^{2pi} F_sect dphi = n Int_{cell} F_sect dphi. [= the group
step inside D.9(ii)'s r2 proof; reproduced.]

Step 4 (change of variables). At fixed lab theta, phi(xi) =
theta - (2pi/n) xi over one cycle t_c = 2pi/(n Omega), xi = t/t_c:
affine, |dphi| = (2pi/n) dxi, orientation reversal absorbed by |.|.
So n Int_{cell} F_sect dphi = 2pi Int_0^1 F_sect(phi(xi)) dxi.
With F_true(xi;S) := 2pi F_sect(phi(xi);S):

    J_exact = Int_Xi F_true(xi;S) dmu(xi),   mu = Lebesgue on [0,1).

**MATCH with target Prop. 1: EXACT** (all four steps, the sign of
phi(xi), and the emergence of uniform mu reproduce independently).
Type-check R1.1 (phi-independent fields => F_true = F_S for every
xi): reproduced. Note mu = Lebesgue is also DEFINITIONALLY immediate
from Def. 3.4 (pushforward of normalized time under a linear map);
the target's "emergence" reading is a legitimate re-derivation, not
new content — consistent with its own F-2 framing.

### A.2 The S-dependence remark (target R1.2)

Lab x-momentum row: d_t(rho u_x) + d_x(rho u_x^2 + p) +
(1/r) d_r(r rho u_x u_r) + (1/r) d_theta(rho u_x u_theta) = 0.
Under T0, d_t -> -Omega d_phi, d_theta -> d_phi; the two phi terms
combine into (1/r) d_phi(rho u_x (u_theta - Omega r)) =
(1/r) d_phi(rho u_x w_rel). **Matches the target's display exactly.**
Weighting by r dx dr over a wedge D between nested no-wall surfaces
S' inside S and applying the divergence theorem (closed boundary
S u S', constant Pa integrating to zero on a closed boundary):

    F_sect(phi;S) - F_sect(phi;S') = - d_phi M(phi),
    M(phi) = Int_D rho u_x w_rel dx dr,

M single-valued and 2pi-periodic; the distributional derivative of a
periodic BV function on the circle has TOTAL SIGNED INTEGRAL zero
(atoms included), so the phi-mean of the station dependence
vanishes. **Sign and structure reproduce.** Two caveats become
DEF-3 (wording) and DEF-6 (front-crossing/wall-branch scope) below.

### A.3 Error representation (target SS2.2-2.3)

Cor. 2.1 is subtraction of (AVG) from A.1 — trivial, reproduced.

(ER): with N_0 the five-field per-phase operator, D.18's
UNCONDITIONAL OPERATOR IDENTITY (r4 restatement, the definitional
level only — verified: it is exactly the level the VERDICT SS3.2
leaves at DEFINITION, the two iffs never being consumed) gives
N_0(V_3D(xi)) = -K(V_3D)(xi) with the exact trace as data; N_0(V(xi))
= 0 with data s(xi). Under (H-DATA) s = s_3D and (H-SEG):
FTC along the segment: N_0(V_3D) - N_0(V) = L~ dV = -K, dV with
ZERO interface data, homogeneous wall (slip minus slip) and nothing
imposed at supersonic outflow. F(V_3D) - F(V) = <dF~, dV>. The
Lagrange identity h.(L dV) - dV.(L* h) = exact divergence (N6 SS4(c))
holds for each DN_0(V_tau) and hence, by linearity in the operator
slot, for the tau-averages L~, L~*; with adjoint BC absorbing the
boundary flux and L~* psi~ = dF~:

    F_true(xi) - F_2D(xi) = <psi~_xi, L~ dV> = -<psi~_xi, K(V_3D)(xi)>,
    J_exact - J_avg = -Int_Xi <psi~_xi, K(V_3D)(xi)> dmu.   (ER)

**MATCH: EXACT, as labeled** (PROVEN-HERE under (H-DATA)+(H-SEG);
the front-carrying OPEN status via S.22 g2a/g2b is honestly declared
in the target). One check the target leaves implicit: F(V_3D(xi)) =
F_true(xi;S) — verified via R1.1: both are 2pi Int_{C_S} G r dl at
phi(xi), same integrand G, so the LHS of (ER) is well-typed.
Background conditions the target does NOT state -> DEF-6.

FIRST-ORDER FORM — here the target's chain does NOT reproduce as
printed. My derivation: replacing psi~ by the per-phase adjoint
psi_xi costs O(||dV||^2) [target declares this]; replacing the
ARGUMENT of K, K(V_3D) -> K(W_A) (the record's corrector object),
costs a SECOND term <psi_xi, K(V_3D) - K(W_A)> = O(DK . dV) =
O(K^2) [target does NOT declare this — DEF-2]; and the resulting
object equals the record J_1 only after a NORMALIZATION conversion
between the ledger convention (N = N_0 + St . S_sweep, J_1 = the
COEFFICIENT of St) and the T3QS convention (D(W) carries the
dimensional Omega; -Int<psi, D(W_A)> dxi = the WHOLE first-order
error) [target equates the two outright — DEF-1]. The operator
dictionary itself, D(W) = (1/r) d_theta'[F_theta(W) - Omega r W] ==
div-form K row (F_phi,rel = F_theta - Omega r W): re-derived,
**EXACT** — the defect is only in the printed equation chain, not in
the dictionary.

### A.4 Mean-zero / covariance decomposition (target Prop. 3.2)

Algebra: Int <psi_xi, K_xi> dmu = <psi_bar, K_bar> +
Int <psi_xi - psi_bar, K_xi - K_bar> dmu (cross terms vanish by
Bochner-mean definition). Reproduced.

(i) Fiberwise mean-zero: at fixed (x,r), the pairing weight r dx dr
cancels the 1/r; phi |-> F_phi,rel(x,r,phi) is periodic BV, so its
distributional phi-derivative has zero total SIGNED integral —
atoms included, and including any DATA-CYCLE jump atom. Hence
K_bar = 0 pointwise UNCONDITIONALLY on periodic BV composites (the
target conditions this on data-cycle continuity — misplaced
conditional, DEF-5). Crucially this fiberwise (1-D in phi) reading
bypasses the D.18 r4 Jacobian/surface-measure normalization issue
entirely — the target's G-f-robustness claim for Prop 3.2 is
CORRECT, and for a reason worth stating (the differentiation is 1-D
in phi at fixed (x,r), no front-surface measure ever enters).

(ii) Ray recovery: W_A = k(xi) W_hat; P2 degree-1 homogeneity +
linearity of Omega r W give F_phi,rel(k W_hat) = k F_phi,rel(W_hat);
K_xi = k'(xi) Z_hat (affine phi(xi) absorbs the constant dphi/dxi
into Z_hat); P3-P4 give psi_xi = psi_hat. Covariance vanishes
identically; smooth periodic cycle: Int k' dxi = 0 => J_1 = 0;
sawtooth: Int^{ac} k' dxi = -[k]_jump => J_1 = <psi_hat, Z_hat>
[k]_jump. **Sign and structure MATCH T3QS P5-P6 and the target.**

(iii) General split: with A := the atom ("jump content"),
Int^{ac} d_phi F = -A, the a.c.-only (frame-legitimate, T3QS B3)
corrector is J_1^{ac} = <psi_bar, A> - Cov^{ac}(psi, K).
Reproduces the target's formula — but ONLY as the a.c.-only
convention with the jump priced against psi_bar; pairing against
psi(xi_jump) differs by a covariance-class term (DEF-5, second
half). The TWO-CHANNEL STRUCTURE is convention-independent; the
individual channel VALUES are not.

### A.5 2-eps lemma (target SS4.1)

Chain: J_e(Sig*) >= J_a(Sig*) - eps >= J_a(Sig) - eps >=
J_e(Sig) - 2 eps; sup over Sig. Reproduced. Sharpness: the
two-point example is valid (both points satisfy (U) with equality
at the second; Sig_1 a legitimate argmax selection; deficit exactly
2 eps). eta-variant: chain gives 2 eps + eta. Two-point weakening:
only (U)@Sig* and (U)@comparator are consumed; with Sig an
eta-argmax of J_exact inside the eps_2-certified set the bound is
eps_1 + eps_2 + eta. **All MATCH.** The uniformization route
(Chenais SCHEMA per problem book SS5 — anchor verified verbatim:
"Sector decomposition (SCHEMA) ... per-sector existence via Chenais
compactness"; margin floor; uniform S1) and its double-OPEN status
reproduce. One unsurfaced class-wide hypothesis -> DEF-7.

==============================================================================
## SS-B NUMBERED DEFECTS

------------------------------------------------------------------------------
DEF-1 — MAJOR — SS2.3 first-order form: internally inconsistent
dual normalization (the target's own FLAG F-5 hazard, committed in
its own display).

Faulty step (target SS2.3, lines ~283-291):
    J_exact - J_avg = -Int <psi_xi, K(xi)> dmu + O(K^2)
                    = St . J_1 + O(St^2)
followed in the same paragraph by
    J_1 = -<psi_J, S_sweep(U_0)>  (ledger SS3)
        = -Int <psi_J(xi), D(W_A(.;xi))> dxi  (T3QS SS1),
with the dictionary D == div-form K asserted exact.

Why it is inconsistent: in the ledger convention (verified at
theorem ledger 163-185) the problem is N(U;St) = N_0(U) +
St . S_sweep(U), so S_sweep is the O(1)-NORMALIZED sweep and J_1 is
the COEFFICIENT of St. In the T3QS convention (verified at T3QS
SS1) D(W) = (1/r) d_theta'[F_theta - Omega r W] carries the
DIMENSIONAL Omega, so -Int <psi_J, D(W_A)> dxi is the WHOLE
first-order error. Since D == K exactly (re-derived, A.3), the
target's three displayed equalities force St . J_1 = J_1: false for
St != 1. The two record conventions are BOTH honest in their own
documents; the target — which itself flags exactly this as F-5
("dual St-normalization of J_1 ... double-pricing hazard") — states
them as equal without the conversion.

Corrected version: pin ONE convention in the chain. E.g. define
J_1^K := -Int <psi_xi, K(W_A)(xi)> dmu (dimensional; equal to the
full first-order error), state
    J_exact - J_avg = J_1^K + O(K^2),
and add: "in the ledger's nondimensionalization N = N_0 +
St . S_sweep one has S_sweep = K/St up to the declared scaling, so
J_1^K = St . J_1^{ledger}; T3QS's J_1 is J_1^K." One sentence; no
conclusion changes order. (This INCIDENTALLY strengthens the
target's own F-5: the hazard is real enough to have caught its
author.)

------------------------------------------------------------------------------
DEF-2 — MAJOR — SS2.3: silent argument switch K(V_3D) -> K(W_A)
in the identification with the record corrector.

Faulty step: (ER) and its declared first-order reduction carry
K(xi) = K evaluated ON THE RESTRICTED EXACT FIELD (N_0(V_3D) =
-K(V_3D) is how K enters). The record's J_1 (ledger: S_sweep(U_0);
T3QS: D(W_A)) and the target's own Prop. 3.2 setup ("K_xi :=
div-form K(W_A)(.,.,phi(xi))") evaluate K ON THE COMPOSITE OF
PER-PHASE SOLUTIONS. The replacement K(V_3D) -> K(W_A) is a THIRD
first-order commitment, of size <psi, DK[segment].dV> = O(K . dV) =
O(K^2) — same order as the declared psi~ -> psi replacement, so
harmless in order, but NOWHERE DECLARED. Under the target's own
binding discipline (every dropped/substituted term stated with its
order) and adjacent to the S.22 (g4) double-pricing surface this is
a defect, not a nicety: a reader pricing the O(K^2) remainder from
the text as written would count two commitments where there are
three.

Corrected version: after "commits an O(||dV||^2) error", add:
"and replacing the residual's argument, K(V_3D) -> K(W_A), commits
a further O(K . dV) = O(St^2) error (linearization of K along the
same segment); with both replacements declared, (ER) becomes
J_exact - J_avg = -Int <psi_xi, K(W_A)(xi)> dmu + O(St^2), which is
the record's corrector object."

------------------------------------------------------------------------------
DEF-3 — MINOR — R1.2 and Prop. 3.2(i): "the total mass of the
derivative of a periodic BV function over the circle is zero".

The TOTAL MASS of the derivative measure of a periodic BV function
is its total variation |DF|(S^1), which is zero only for constants.
What vanishes — and what both proofs actually use — is the total
SIGNED integral DF(S^1) = 0 (F single-valued and periodic). Both
proofs are correct as executed; the sentence as printed asserts a
false statement of measure theory. Corrected: "the distributional
derivative of a single-valued periodic BV function integrates to
zero over the circle (its total signed measure is zero; atoms
included)".

------------------------------------------------------------------------------
DEF-4 — MINOR — SS2.1(b) and R-6: the 3-6% tangential-energy-
fraction number is misanchored to D.10.

D.10's measured content (verified at phaseD_meanswirl 930-971) is
sigma/mu ~= 0.70 (P-M p.5) hence covariance/KE weight (sigma/mu)^2
~= 0.5; D.10 contains NO 3-6% figure, and its own instrument for
exactly this quantity — falsifier A4, the swirl-KE flux fraction —
has NEVER been computed on any dataset (VERDICT gap G-e: "empirical
vacuum: F1-F4, A4 never computed"). The 3-6% figure is a
literature-corpus number (EAP/K-P line: e.g.
validation/ADVISORY_Scollapse_prompt_2026-08-11.md:77 "3-6% EAP,
K-P verbatim"; validation/ADVISORY_litreview_confrontation_
2026-08-13.md ~911-918 discusses precisely this 3-6% debit). Citing
it as "(D.10, PROVEN-IN-RECORD as THEOREM + measured PRACTICE)"
overstates the provenance: the THEOREM part of D.10 is positivity/
unconstrainedness, the measured part is sigma/mu — the 3-6% is
neither. Corrected: keep the number, re-anchor it to the EAP/
litreview corpus, and note that the program's own measurement of it
(A4) is outstanding (G-e).

------------------------------------------------------------------------------
DEF-5 — MINOR — Prop. 3.2(i)/(iii): misplaced conditional and
undeclared pairing convention.

(a) As printed, "if the composite data cycle ... is CONTINUOUS
(BV, no data-cycle jump), K_bar = 0 pointwise" attaches the
continuity hypothesis to K_bar = 0. False attachment: K_bar = 0
holds UNCONDITIONALLY for periodic BV composites, data-cycle jump
atoms included (total signed measure zero, A.4(i)). Continuity is
needed only for the CONSEQUENCE J_1 = -Cov (no jump channel, and
first-order frame valid everywhere). (b) In (iii), the two-channel
formula J_1 = <psi_bar, jump content> - Cov^{ac} is the A.C.-ONLY
convention with the jump priced against the MEAN adjoint; pricing
it against psi(xi_jump) shifts a covariance-class term between the
channels. The two-channel STRUCTURE is convention-free; the channel
VALUES are not, and O5-lite comparison (C) will measure a
convention-dependent split unless the convention is pinned.
Corrected: state K_bar = 0 unconditionally; attach continuity to
the J_1 = -Cov conclusion; declare the a.c.-only/psi_bar pairing as
the convention of record for the (J)/(H) split (it is the T3QS-B3-
consistent one).

------------------------------------------------------------------------------
DEF-6 — MINOR — (ER) and R1.2: three used-but-unstated background
conditions.

(a) F_true(xi;S) is defined for EVERY admissible S; (ER) is derived
only for S whose meridional trace lies inside the per-phase
computational domain (the adjoint machinery lives there). Prop. 1
and Cor. 2.1 are S-uniform; (ER) is not — one sentence of scope.
(b) The thrust functional is an interior-surface functional, so
dF~ is a surface source and psi~ has the standard jump across C_S;
unstated (harmless, but the N6 SS4(c) citation covers volume
Lagrange identities, not the surface-source bookkeeping).
(c) R1.2's wedge integration is executed in classical divergence
form while the standing class carries fronts through the wedge; for
an exact WEAK solution the identity survives distributionally (RH
absorbs the front content — the same reading D.18 r4 fixes), but
the sentence should say so; and the "otherwise the standard
wall-pressure bookkeeping ... is added" branch is asserted, never
shown — scope-restrict R1.2 to no-wall wedges (every use of R1.2 in
the document survives the restriction).

------------------------------------------------------------------------------
DEF-7 — MINOR — SS4.1-4.2: the operational reading of the 2-eps
lemma consumes class-wide strict T0, surfaced only as H-F1.

The lemma itself needs only (U). But every route the document names
for ESTABLISHING (U) — Prop. 1 + (B) pointwise, then uniformize —
requires strict T0 (H-A1) to hold FOR EVERY Sigma in A (each
design's flow a pure rotating pattern with the SAME n and Omega, so
that J_exact[Sigma] is the T0 object Prop. 1 prices). The frozen
family H-F1 (s, mu, Omega independent of Sigma) is stated; the
class-wide validity of H-A1 itself (no design in A triggers a mode
change) is a DISTINCT hypothesis — it is exactly the PB-5 boundary
— and belongs in SS4.2's uniformization list alongside uniform S1.
Corrected: add "(0) H-A1 uniformly on A (no design-induced mode
change; PB-5 boundary otherwise)" to the SS4.2 route hypotheses.

==============================================================================
## SS-C ANCHOR/MISQUOTE AUDIT (record sources re-read this window)

- [T-T0] M0:442-459 — cited content (steadiness, w.n = u.n on
  axisymmetric S) VERIFIED verbatim.
- [T-TH0] M0:356-362 (mean equality), 374-380 ("only
  approximation", "+O(St)"), 381-391 (storage-vs-flux) — VERIFIED;
  F-1's target line confirmed at M0:376.
- [S-T0P] M0:486-489 stage-2 wording — VERIFIED.
- [T-O2] M0:428-439 measure-agnostic note (atomic mu, switch-phase
  re-verification) — VERIFIED as used in R1.4.
- Theorem ledger 90-190: C-T1 CONJECTURE + P4-periodic "THEOREM* at
  the STATEMENT level" + named residues (i)/(ii) — VERIFIED; the
  target's status quotes are faithful. (The normalization DEFECT-1
  is in the target's equation, not in its status quotes.)
- T3QS SS1-SS3: D(W) operator, P1-P6, R1-R3, B1-B4 — VERIFIED; the
  target's rejector/boundary imports are faithful; P6 sign matches.
- phaseD D.9(ii) (Z_n step), D.17 (xi <-> phi affine), D.18 r4
  (unconditional operator identity; triangular recombination "part
  of this DEFINITION"; atoms n_phi[F_phi,rel]; judge THEOREM*
  downgrades of the two iffs) — VERIFIED; the target's scope note
  (definitional content only, iffs never consumed) is ACCURATE and
  its G-f-robustness argument is correct (and can be strengthened,
  A.4(i)).
- S.22 g1/g2a/g2b/g3/g4 — the target's R-3, bound structure, and
  V_data mirror the schema faithfully, including the g2b
  "known-broken, no finite C on contact regime" — VERIFIED.
- VERDICT SS3.2 judge labels — target's usage consistent.
- D6:286, 488-490, 776-778 — G2 bound-ladder rung-2-internal;
  F-4's reading VERIFIED fair (G3's "St|J1|" further confirms the
  ledger normalization, feeding DEF-1).
- Problem book SS5 ("Sector decomposition (SCHEMA) ... Chenais
  compactness"), SS8 (St_n = n Omega tau_n / 2pi; "out of
  contract" sentence) — VERIFIED; the target's SS3.3 close and
  SS4.2 route wording are faithful.
- C51 — read; not consumed by the target beyond listing; no misuse.

MISQUOTES FOUND: one (DEF-4, the 3-6% anchor). All other anchors
checked are faithful.

==============================================================================
## SS-D PER-MAIN-CLAIM VERDICTS

| Target claim | Verdict | Basis |
|---|---|---|
| 1. Prop. 1 exact-half identity + mu-emergence + R1.1 type-check + R1.2 S-dependence | **CONFIRMED** | Independently re-derived end-to-end (SS-A.1/A.2); DEF-3/DEF-6(c) are wording/scope repairs, no content change. |
| 2a. Single-substitution census; (ER) exact under (H-DATA)+(H-SEG); (H-SEG) OPEN on fronts; contract term (II) | **CONFIRMED** | Re-derived (SS-A.3); hypothesis surfacing honest; F-3 precision correct. |
| 2b. "First-order form = the record's J_1; dictionary exact" | **GAP-NAMED** | Operator dictionary D == div-form K re-verified EXACT, but the printed identification commits DEF-1 (inconsistent dual normalization — St.J_1 = J_1 as displayed) and DEF-2 (silent K(V_3D)->K(W_A)). Both repairable by declared sentences; orders unchanged. |
| 3a. Bound structure C.St_n.V_data; six reasons C not provably small; no finite C on front/contact classes | **CONFIRMED** | Scaling re-derived (per-transit impulse rho.St_n.Delta_cell V; St_n matches PB SS8); R-1..R-5 check against C-T1/S.22 anchors; R-6 rides DEF-4's re-anchoring but survives it. |
| 3b. Prop. 3.2 decomposition; ray recovery = T3QS P5-P6; two channels (J)/(H) | **CONFIRMED** (with DEF-5 convention caveat) | Algebra and ray case re-derived, signs match T3QS; K_bar = 0 is in fact UNCONDITIONAL (stronger than printed); channel split needs its convention pinned. |
| 3c. Honest conclusion + O5-lite protocol incl. new comparison (C) | **CONFIRMED** | Consistent with C-T1 CONJECTURE, S.22 SCHEMA, PB SS8 contract sentence; (C) is genuinely licensed by Prop. 1. |
| 4. 2-eps lemma + sharpness + eta-variant + two-point weakening; uniformity OPEN twice over | **CONFIRMED** (with DEF-7 addition) | All four parts re-derived (SS-A.5); the shock-free sub-scope theorem target is a fair reading of g2a. |
| 5. Flags F-1..F-5 + confirmations | **CONFIRMED** (F-1 slightly under-reaches; F-5 strengthened) | F-1: M0:376 verified untagged — AND M0:377's "exact as St -> 0" is itself C-T1 content and should ride the same tag. F-2: within the cited anchors the numbered identity indeed does not exist (this referee did not run an exhaustive corpus search; the mint recommendation stands on the anchors checked). F-3/F-4 verified fair. F-5: verified — and committed by the target's own SS2.3 (DEF-1), which is the strongest possible evidence the hazard is real. |

==============================================================================
## SS-E REFEREE'S NET ASSESSMENT

The document's load-bearing mathematics is sound and independently
reproducible: the exact half is a genuine identity, the error
representation is correctly conditioned, the covariance/mean-zero
mechanics agree with T3QS by a genuinely independent route, and the
2-eps transfer is correct and sharp. The two MAJOR defects both
live in the single paragraph that welds the new (ER) machinery onto
the record's corrector — precisely the seam S.22 (g4) and the
target's own F-5 warn about — and both are repairable by declared
one-sentence normalizations with no change of order or conclusion.
The claim-label discipline is otherwise well kept; the one anchor
error (DEF-4) transfers a literature number onto a record theorem's
citation line and must be fixed before any R4 landing quotes it.
Recommended disposition: REPAIR-THEN-LAND (fix DEF-1/DEF-2 in the
SS2.3 text and re-anchor DEF-4 before the F-2 mint or any M0 delta
consumes this artifact).
