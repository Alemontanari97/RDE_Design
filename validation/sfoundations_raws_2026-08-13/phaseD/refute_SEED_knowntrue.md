# ADVERSARIAL REFUTATION — dual-seed slot (known-true seed)

- **Target claim (verbatim, standalone):** "In steady axisymmetric inviscid flow of a perfect or
  thermally-perfect gas, the quantity Gamma = r*w (angular momentum per unit mass about the axis)
  is constant along streamlines; rigor class THEOREM."
- **Refuter lens:** counterexample-and-hypothesis-minimality (attack the literal hypothesis set
  with concrete counterexamples; audit the proof obligations the THEOREM label incurs under the
  binding SOTA standard: named function spaces, explicit hypothesis list, every step justified,
  falsifier attached, variable-gamma status declared).
- **Round:** 1. **Date:** 2026-08-17.

---

## 1. Reconstruction of the intended proof (what the label THEOREM must deliver)

Cylindrical coordinates (r, theta, z), velocity u = (u_r, w, u_z) with w = u_theta the swirl
component. The azimuthal component of the compressible Euler momentum equation is

    u_r dw/dr + (w/r) dw/dtheta + u_z dw/dz + u_r w / r
        = -(1/(rho r)) dp/dtheta + f_theta.                                   (E-theta)

Under **axisymmetry** (d/dtheta of every field = 0) the pressure term vanishes identically.
Multiplying the remainder by r and using d(rw)/dtheta = 0:

    u_r d(rw)/dr + u_z d(rw)/dz = (u . grad)(rw) = r f_theta.                 (*)

If **f_theta = 0** (no azimuthal body force, inertial frame), then (u . grad)(Gamma) = 0 with
Gamma = r w, i.e. Gamma is a material invariant; under **steadiness** pathlines coincide with
streamlines, giving the claimed conclusion. Required regularity for every step: u, rho, p in
C^1(Omega), rho > 0, on an open axisymmetric domain, fields read on the meridional half-plane
{r >= 0}. Note what the proof **never uses**: the equation of state. The result is
EOS-independent — valid for any inviscid fluid, barotropic or not, any gamma(T).

This reconstruction is the strongest available route; the attacks below are against the claim
**as stated**, measured against this route and the binding standard.

## 2. Attacks

### A1 — Missing load-bearing hypothesis: no azimuthal body force / inertial frame (VALID)

The stated hypothesis list is {steady, axisymmetric, inviscid, perfect-or-thermally-perfect gas}.
"Inviscid" does not exclude body forces or non-inertial frames. Equation (*) shows
D(Gamma)/Dt = r f_theta, so **any nonzero azimuthal specific force refutes the literal claim**
while satisfying every stated hypothesis.

Concrete counterexamples, all steady, axisymmetric, inviscid, thermally-perfect:

1. **Actuator/blade-row momentum source** (Euler turbine equation): an axisymmetric inviscid
   through-flow with a distributed azimuthal force f_theta modeling a rotor gives
   Delta(r w) = integral of r f_theta dt along the streamline != 0. This is the textbook
   *mechanism by which Gamma changes* in turbomachinery; the flow violates none of the stated
   hypotheses.
2. **Wave-fixed rotating frame** (directly relevant to the RDE program): a flow steady in a
   frame rotating at Omega has an azimuthal Coriolis contribution; the relative-swirl invariant
   is r w_rel + Omega r^2 (rothalpy-companion form), **not** r w_rel. A claim consumer working
   in the detonation-wave frame and applying the statement literally gets a false invariant.
3. **MHD/Lorentz azimuthal forcing**: inviscid, steady, axisymmetric, f_theta = (J x B)_theta/rho
   != 0; Gamma varies along streamlines.

**Threat class:** the THEOREM label is falsified on the literal hypothesis set. **Repair:** add
"in an inertial frame, with body force having zero azimuthal component (conservative axisymmetric
body forces such as axis-aligned gravity admissible)". With that clause the counterexamples are
excluded and the proof in §1 closes.

### A2 — No regularity / function-space hypotheses; weak solutions unaddressed (VALID)

The differential proof requires u, rho, p in C^1 and rho > 0 on an open axisymmetric Omega. The
claim names no function space (binding standard: named function spaces). Compressible regime of
interest contains **shocks**: the C^1 proof is void across them, so the claim as labeled is
silent exactly where the program operates (transonic/supersonic nozzle flow).

Adversarial resolution attempted and **failed to produce a counterexample**: for an axisymmetric
shock surface the normal lies in the meridional plane (n_theta = 0), Rankine–Hugoniot tangential
momentum gives w continuous across the shock, r is continuous, hence Gamma is conserved across
axisymmetric shocks as well; across slip/contact surfaces streamlines do not cross, so no
obligation arises. The truth therefore extends to piecewise-C^1 weak solutions with axisymmetric
discontinuities — **but this is a separate proof step the claim neither states nor discharges**.
Subsidiary gap, same class: "along streamlines" needs a parametrization hypothesis (|u| != 0 on
the arc considered, or continuity-limit language through stagnation points; on-axis streamlines
carry Gamma = 0 trivially provided w = O(r), which is exactly the C^1-at-axis condition).

**Threat class:** label-threatening under the binding standard (steps not justified, spaces not
named), not truth-threatening. **Repair:** state C^1 hypotheses for the field version; add the
one-line RH tangential-momentum lemma for the piecewise-C^1 extension.

### A3 — Hypothesis list is not the load-bearing set: the gas-model clause is inert (VALID, scope mislabel)

The proof in §1 never touches the EOS. Restricting to "perfect or thermally-perfect gas" is
logically harmless but **mislabels the theorem's scope** while the actually load-bearing clause
(A1) is absent: the stated list is simultaneously non-minimal and incomplete. Under the binding
standard (explicit hypothesis list; variable-gamma status declared) the correct declaration is:
**EOS-independent — holds verbatim for gamma = const, gamma(T) thermally-perfect frozen mixture,
and any inviscid fluid**; the gas clause should be demoted from hypothesis to a remark. Kinematic
theorem, not thermodynamic.

### A4 — No falsifier attached (VALID, house-standard violation)

The claim as delivered ends with no FALSIFIER, which the binding standard requires of every
claim. A compliant falsifier exists and is cheap: *trace streamlines through any committed
steady axisymmetric swirling Euler solution (e.g. a GENO/MoC field with nonzero w) and test
max |Gamma - Gamma_inlet| along each streamline against a discretization-derived band; a single
C^1 zero-azimuthal-force solution with Gamma drifting beyond the band refutes the theorem.*
Its absence is a defect of the deliverable, not of the mathematics.

### Attacks attempted and REJECTED (for the record, dual-seed honesty)

- **Unsteadiness needed?** No: Gamma is a material invariant even unsteady; steadiness is used
  only to identify pathlines with streamlines. Hypothesis is correctly present, not superfluous.
- **Baroclinicity kills it?** No: the pressure term dies by axisymmetry alone, before any
  barotropy assumption could be needed. Non-barotropic (thermally-perfect, non-uniform entropy)
  fields are covered.
- **3D helical streamlines vs meridional projections?** Since d(Gamma)/dtheta = 0, constancy
  along the true helical streamline and along its meridional projection are equivalent. No gap.
- **Cross-shock violation?** Refuted in A2: RH tangential momentum protects Gamma.
- **Axis singularity?** Gamma = 0 on the axis; smoothness at the axis forces w = O(r). No gap.

## 3. Verdict

The mathematical core is a bedrock classical theorem (angular-momentum/Kelvin class; standard in
Batchelor and in the turbomachinery through-flow literature) and **survives every
truth-directed attack** — the known-true seed is confirmed as *true*. But the claim **as
labeled** does not meet THEOREM under the binding standard: the literal hypothesis set admits
concrete counterexamples (A1), no function space or weak-solution treatment is given (A2), the
hypothesis list is non-minimal-and-incomplete (A3), and no falsifier is attached (A4). All four
defects have named, mechanical repairs that a competent author closes in one pass; the repaired
statement is a genuine THEOREM (EOS-independent, valid at variable gamma).

**VERDICT: REPAIRABLE** (true statement, label not earned as delivered; repairs named above).

FALSIFIER for this refutation itself: exhibit a proof of the claim on the literal hypothesis set
that excludes counterexample A1 without adding the no-azimuthal-force clause — i.e., show
"inviscid" formally entails f_theta = 0 in the governing convention of record; that would void
A1 and promote the verdict to SOUND-AS-LABELED modulo A2–A4.
