# ADVERSARIAL REFUTATION BRIEF — slot KT-2 (single claim)

Role: adversarial refuter. Attack the target claim below as delivered.
Binding standard for the THEOREM label: explicit hypothesis list, named
function spaces, every proof step justified, falsifier attached,
EOS/variable-gamma status declared. Attack BOTH truth (counterexamples
against the literal hypothesis set) and label (unjustified steps).

Verdict vocabulary (mandatory, exactly one):
- SOUND-AS-LABELED — the claim as delivered earns its label; no valid
  objection found (record rejected attack attempts for honesty).
- REPAIRABLE — true core, but the label is not earned as delivered; name
  each defect and its mechanical repair.
- BROKEN — the claim is false; produce a concrete counterexample with the
  falsification at source (which step of the supplied proof route fails
  and why).

Write your full refutation to the output file named in your task order.
End the file with `VERDICT: <one of the three>` and a falsifier for your
own refutation.

---

## TARGET CLAIM [KT-2] — rigor class THEOREM (as labeled by its author)

**Statement.** Let D be an open subset of the meridional half-plane
{(r, z): r >= 0} and Omega the open axisymmetric domain in R^3 it
generates. Let (u, rho, p), u = (u_r, w, u_z) in cylindrical components,
be a steady solution of the compressible Euler equations on Omega with:
(H1) axisymmetry: all fields independent of theta;
(H2) inertial frame; the body force has zero azimuthal component
     (f_theta = 0; axis-aligned conservative forces such as gravity
     admissible);
(H3) regularity: u, rho, p in C^1(Omega), rho > 0; at the axis the C^1
     condition forces w = O(r). Piecewise-C^1 weak solutions are
     admitted provided every discontinuity surface is axisymmetric (its
     normal lies in the meridional plane, n_theta = 0).
Then Gamma := r*w (angular momentum per unit mass about the axis) is
constant along every streamline arc on which |u| > 0. Across each
axisymmetric shock Gamma is conserved (Rankine-Hugoniot tangential
momentum with n_theta = 0 forces [w] = 0, and r is continuous across
the surface); streamlines do not cross slip/contact surfaces, so no
further obligation arises there. On the axis Gamma = 0 identically.

**EOS status.** EOS-FREE: no step of the proof consumes the equation of
state; the statement holds verbatim for gamma = const, thermally-perfect
gamma(T), and any inviscid fluid. The result is kinematic
(angular-momentum class), not thermodynamic.

**FALSIFIER.** Trace streamlines through any committed steady
axisymmetric swirling Euler solution with f_theta = 0 (e.g. a certified
method-of-characteristics field with nonzero w); test
max |Gamma - Gamma_inlet| along each streamline against a
discretization-derived band (local truncation estimate propagated along
the arc); a single compliant C^1 solution with Gamma drifting beyond the
band refutes the theorem.

**Proof route (author's, supplied).** The azimuthal component of steady
Euler momentum reads
u_r dw/dr + u_z dw/dz + u_r w / r = -(1/(rho r)) dp/dtheta + f_theta.
Axisymmetry (H1) kills the pressure term; (H2) kills f_theta.
Multiplying by r gives (u . grad)(r w) = 0, i.e. Gamma is a material
invariant; steadiness identifies pathlines with streamlines. For the
piecewise extension: RH tangential momentum on an axisymmetric surface
(n_theta = 0) gives [w] = 0, r is continuous, hence [Gamma] = 0 across
shocks; slip/contact surfaces are not crossed by streamlines. At the
axis, w = O(r) gives Gamma -> 0.
