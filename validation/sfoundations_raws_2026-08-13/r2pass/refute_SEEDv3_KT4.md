# ADVERSARIAL REFUTATION — slot KT-4, seed v3

Target: claim [KT-4] (Gamma = r*w constant along streamline arcs and
admissibly-concatenated arcs; steady axisymmetric compressible Euler,
f_theta = 0), labeled THEOREM by its author. Attack executed at
derivation level against BOTH truth and label, per the brief's binding
standard (explicit hypotheses, named function spaces, every step
justified, falsifier attached, EOS status declared).

## 1. Verification of the label checklist (mechanical)

- Explicit hypothesis list: H1/H2/H3 present, each consumed at a named
  step (H1 in Step 1 twice, H2 in Step 1, H3 in Steps 1/2/4/5). PASS.
- Named function spaces: C^1(Omega \ S) for (u, rho, p); one-sided C^0
  limits on S; piecewise-C^1 weak solution class named. PASS.
- Falsifier attached: yes (streamline-trace with discretization-derived
  band on committed MoC fields). Executable in principle against the
  literal hypothesis set. PASS.
- EOS/variable-gamma status declared: EOS-FREE, with the declaration
  checkable against the proof (see attack A7). PASS.

## 2. Truth attacks (counterexample hunts) — all REJECTED

**A1. Contact/slip discontinuity with [w] != 0 at r > 0.** The classical
killer of naive "Gamma conserved everywhere" claims: a cylindrical
vortex sheet carries [w] != 0, hence [Gamma] != 0, and a
position-continuous curve through it would break the conclusion.
REJECTED: the quantified class excludes it *definitionally* — a
streamline arc lies in Omega \ S, and concatenation is permitted ONLY
at mass-crossing points (m != 0 both sides). Step 3 does not smuggle a
dynamical non-attainment claim; it openly concedes trajectories may
reach S and relies purely on the definition of the arc class. The
exclusion is honest scoping, not a hidden hypothesis: the Statement
itself (Definitions block) carries it, so the theorem's quantifier is
visible to any consumer. No counterexample constructible in-class.

**A2. Swirling shock with angular-momentum jump.** Attempted: an
axisymmetric shock surface (n_theta = 0 by H3) in a swirling flow with
[w] != 0. REJECTED at source: RH tangential momentum. With [m] = 0 and
m != 0, [m w] = 0 forces [w] = 0; I verified the projection myself from
the Cartesian vector RH condition [rho (u.n) u + p n] = 0 dotted with
e_theta at a point r > 0: [m w] + [p] n_theta = [m w] since n_theta = 0
(H3). The step is not merely quoted; it is re-derivable in one line
from the hypothesized RH conditions. Any in-class shock preserves
Gamma across mass-crossing points. This matches the classical record
(tangential-velocity continuity across gasdynamic shocks).

**A3. Vanishing one-sided density limit (vacuum-adjacent S point).**
H3 imposes rho > 0 only on Omega \ S; a one-sided C^0 limit of rho on S
may be 0, producing m = 0 from one side with u.n != 0 — a point that is
NEITHER mass-crossing NOR slip/contact, so the Classification sentence
is not exhaustive as written. Pushed as a truth attack: can such a
point host a Gamma jump on a concatenated arc? REJECTED: matching
points are required to have m != 0 from both sides; at such points the
one-sided rho limits are automatically positive (m = rho u.n with u
C^0-bounded forces rho_limit > 0 when m != 0), so Step 2's argument is
self-consistent exactly where it is consumed. The non-exhaustiveness
of the classification touches no step of the proof (Step 4 uses only
mass-crossing points; Step 3 discharges only the slip/contact class;
no step asserts the dichotomy is exhaustive). Residual: cosmetic
wording only — see §4, not label-relevant.

**A4. Axis pathologies.** Attempted three ways. (i) Chain rule on
Gamma = r w at r = 0, where r is not differentiable in R^3: PREEMPTED
by the author's axis dichotomy — the cylindrical computation is
consumed only at r > 0, and the dichotomy proof (u_r = O(r) from C^1 +
axisymmetry, axis invariance, local Lipschitz uniqueness, then
open-closed continuation in the arc's connected parameter interval) is
complete; I checked that axisymmetry forces the horizontal Cartesian
components to vanish at axis points (u(Rx) = R u(x) with Rx = x forces
u_horiz = 0), so u_r, w = O(r) is genuinely a consequence of C^1, not
an extra hypothesis. (ii) On-axis point of S where e_theta is
undefined: PREEMPTED in Step 2 — [Gamma] = 0 there needs only r = 0
and finite one-sided w limits, both granted by H3. (iii) Arc matched
at an on-axis mass-crossing point: both pieces meet the axis, hence by
the dichotomy lie entirely on the axis, where Gamma == 0 (Step 5);
consistent. All REJECTED.

**A5. Infinite concatenation / accumulating crossings.** A Zeno-type
arc crossing S infinitely often would break the finite-induction
transfer of the constant. REJECTED: the arc class is defined as a
FINITE concatenation, and Step 4 explicitly refuses the (unsound)
inference of finiteness from isolation — no obligation remains.

**A6. Endpoint-limit mismatch at matching points.** For Step 4 the
limit of Gamma ALONG the arc must equal the one-sided FIELD limit at
the S point. REJECTED: H3's piecewise-C^1/one-sided-C^0 class gives
continuous one-sided extension to S; an arc approaching the point from
one side inherits that limit; r is continuous. Transversality at
mass-crossing points is in fact automatic (limit u.n = m/rho_limit
!= 0), so the definitional "crossed transversally" is redundant but
harmless.

**A7. EOS smuggling.** Audited every step for EOS consumption: Step 1
uses only H1 (kills both theta-derivative terms, including the
pressure term BEFORE any EOS could enter) and H2; Step 2 uses RH mass
+ tangential momentum, neither of which involves p or the EOS (the
[p] n_theta term dies by geometry, H3); the energy RH condition is
never touched. The EOS-FREE declaration is TRUE as stated, including
for a general inviscid fluid. REJECTED.

**A8. Body-force loophole.** H2's parenthetical (conservative,
axis-aligned) is stricter than what the proof needs (f_theta = 0
suffices); a non-conservative meridional force cannot break the
azimuthal balance. No counterexample available through f. REJECTED.

## 3. Label attacks (unjustified steps) — all REJECTED

**L1. Quoted cylindrical Euler form.** The azimuthal momentum equation
is quoted, not derived. Rejected as a label defect: it is written in
FULL generality (all theta terms present) before H1/H2 are applied, so
the epistemically dangerous move — term cancellation — is explicit and
hypothesis-tagged; the quoted form itself is textbook coordinate
algebra, independently checkable, and I re-verified the collection
step u_r d(rw)/dr + u_z d(rw)/dz = u_r(w + r dw/dr) + u_z r dw/dz = 0
is an identity. No gap at THEOREM grade.

**L2. "Pathlines coincide with streamlines."** Rhetorical only; the
operative argument is the chain rule along a C^1 integral curve, which
stands on its own. Not load-bearing. Rejected.

**L3. |u| > 0 hypothesis.** Superfluous (u.grad Gamma = 0 needs no
non-degeneracy; a stagnant arc is a point), but an over-restriction
never endangers a THEOREM label. Rejected.

**L4. Pairwise-disjoint components of S.** Excludes shock-shock
intersections (Mach stems, triple points) — a real physical class. But
the exclusion sits in the explicit hypothesis list, so the label is
earned for the stated scope; scope narrowness is not a label defect
under the brief's standard. Rejected (flagged as consumer caveat only).

## 4. Residue (below label threshold, recorded for honesty)

- The Classification sentence reads as a dichotomy but is not
  exhaustive when a one-sided rho limit vanishes on S (A3). No proof
  step consumes exhaustiveness; a one-word repair ("a point of S is
  called...", dropping any implication of exhaustiveness) would
  remove even the cosmetic ambiguity. Not label-blocking.
- "Crossed transversally" in the Definitions is provably redundant at
  mass-crossing points (A6). Harmless redundancy.

## 5. Verdict

The claim as delivered survives every truth attack I could mount —
the two classical counterexample families (contact sheets, swirling
shocks) are respectively excluded-by-visible-definition and killed by
the hypothesized RH conditions — and every step of the supplied route
is justified at the declared function-space granularity, including
the historically error-prone axis and on-axis-S cases, which the
author preempts correctly. The EOS-FREE declaration is verified
against the proof. The residues in §4 are cosmetic and touch no
quantified statement.

VERDICT: SOUND-AS-LABELED

**Falsifier for this refutation.** My verdict is refuted by any ONE
of: (i) a concrete piecewise-C^1 steady axisymmetric weak Euler
solution satisfying H1-H3 and the RH conditions, together with a
streamline arc or admissibly-concatenated arc (matchings only at
m != 0 points) along which Gamma is provably non-constant; (ii) a
demonstration that some step of the supplied route consumes a
hypothesis absent from H1-H3 (in particular any EOS input, or
smoothness beyond C^1 / one-sided C^0); (iii) execution of the
claim's own attached falsifier on a compliant committed field with
Gamma drift outside the discretization-derived band traced to the
theorem (not to numerics). Any of these lands my SOUND-AS-LABELED
verdict as wrong at source.
