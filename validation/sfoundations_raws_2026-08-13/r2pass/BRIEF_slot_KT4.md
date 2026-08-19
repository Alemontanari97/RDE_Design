# ADVERSARIAL REFUTATION BRIEF — slot KT-4 (single claim)

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

## TARGET CLAIM [KT-4] — rigor class THEOREM (as labeled by its author)

**Statement.** Let D be an open subset of the meridional half-plane
{(r, z): r >= 0} and Omega the open axisymmetric domain in R^3 it
generates. Let (u, rho, p), u = (u_r, w, u_z) in cylindrical components,
be a steady solution of the compressible Euler equations on Omega with:
(H1) axisymmetry: all fields independent of theta;
(H2) inertial frame; the body force has zero azimuthal component
     (f_theta = 0; axis-aligned conservative forces such as gravity
     admissible);
(H3) regularity: u, rho, p in C^1(Omega \ S), rho > 0, where S is a
     finite union of pairwise-disjoint axisymmetric C^1 surfaces, each
     closed as a subset of Omega — so S is closed in Omega and
     Omega \ S is open — with normals in the meridional plane
     (n_theta = 0), across which the
     fields have one-sided C^0 limits (piecewise-C^1 weak solution
     satisfying the Rankine-Hugoniot conditions on S); at the axis the
     C^1 condition forces w = O(r).
Classification on S (steady flow): a point of S is MASS-CROSSING where
m := rho u . n != 0 (same sign from both sides), and SLIP/CONTACT where
u . n = 0 from both sides; a component is called mass-crossing
(slip/contact) where its points are.
Definitions (arc objects). A STREAMLINE ARC is a C^1 integral curve of
u contained in Omega \ S — the open set on which u is defined and C^1;
a curve through a point of S cannot satisfy the streamline ODE there,
since u is not defined on S. A CONCATENATED ARC is a finite
concatenation of streamline arcs in which consecutive pieces are
matched in position ONLY at mass-crossing points of S (m != 0 from
both sides at the matching point) crossed transversally; matching at
slip/contact points is excluded by definition.
Then Gamma := r*w (angular momentum per unit mass about the axis) is
constant along every streamline arc on which |u| > 0, and along every
concatenated arc on which |u| > 0. On the axis Gamma = 0 identically.

**EOS status.** EOS-FREE: no step of the proof consumes the equation of
state; the statement holds verbatim for gamma = const, thermally-perfect
gamma(T), and any inviscid fluid. The result is kinematic
(angular-momentum class), not thermodynamic.

**FALSIFIER.** Trace streamlines through any committed steady
axisymmetric swirling Euler solution with f_theta = 0 (e.g. a certified
method-of-characteristics field with nonzero w); test
max |Gamma - Gamma_inlet| along each streamline against a
discretization-derived band (local truncation estimate propagated along
the arc); a single compliant solution with Gamma drifting beyond the
band refutes the theorem.

**Proof route (author's, supplied).**

*Step 1 (smooth regions — the field equation).* The azimuthal component
of the steady compressible Euler momentum equation in cylindrical
coordinates reads, in full generality,

    u_r dw/dr + (w/r) dw/dtheta + u_z dw/dz + u_r w / r
        = -(1/(rho r)) dp/dtheta + f_theta.

Under (H1) BOTH theta-derivative terms vanish: (w/r) dw/dtheta = 0 and
dp/dtheta = 0. Under (H2), f_theta = 0. What remains is
u_r dw/dr + u_z dw/dz + u_r w / r = 0. Multiplying by r and collecting,

    u_r d(rw)/dr + u_z d(rw)/dz = 0,

and since d(rw)/dtheta = 0 by (H1), this is (u . grad)(Gamma) = 0 with
Gamma = r w: a material invariant of the steady field. By steadiness,
pathlines coincide with streamlines; on any C^1 streamline arc with
|u| > 0 the chain rule along an arc parametrization gives
d(Gamma along arc)/ds = 0, so Gamma is constant on the arc.
*Axis dichotomy (which point of the arc class each computation
covers):* every streamline arc in the quantified class lies either
entirely on the axis or entirely in {r > 0}. Indeed, C^1 regularity of
the three-dimensional field forces u_r = O(r) as well as w = O(r) at
the axis (the same argument H3 invokes for w), so the axis {r = 0} is
invariant under the flow of u; by local Lipschitz uniqueness of
integral curves of the C^1 field, an arc meeting the axis at one point
lies on the axis entirely. The cylindrical computation above is
therefore consumed only at points with r > 0, where it is valid
(u_r w / r is well-defined there); arcs lying entirely on the axis are
covered by Step 5.

*Step 2 (mass-crossing points of S).* At any point of S, the steady
Rankine-Hugoniot conditions include conservation of mass, [m] = 0 with
m = rho u . n, and conservation of tangential momentum, [m w_t] = 0
for every tangential direction t. Since n_theta = 0, the azimuthal
direction e_theta is tangential to S, so the theta-component of
tangential momentum gives [m w] = 0. At a MASS-CROSSING point m != 0,
so combining with [m] = 0: m [w] = 0, hence [w] = 0 there. The radius
r is continuous across S, so [Gamma] = [r w] = 0 at every
mass-crossing point of S with r > 0. At an ON-AXIS point of S (r = 0),
where e_theta is undefined and no tangential-momentum argument is
available or needed, [Gamma] = [r w] = 0 holds trivially: r = 0 and
the one-sided limits of w are finite — indeed zero, by the H3 axis
condition w = O(r) applied on each side of S. The e_theta argument
above is used, and valid, only at r > 0.

*Step 3 (slip/contact points).* By the Definitions (arc objects), a
streamline arc lies in Omega \ S and a concatenated arc admits
position-matching of its pieces ONLY at mass-crossing points crossed
transversally; a position-continuous curve that is a streamline on
both sides of a slip/contact point is therefore NOT in the quantified
class. The exclusion is definitional, and it is necessary: a contact
discontinuity permits [w] != 0 at r > 0, hence [Gamma] != 0 across
such a point. No dynamical non-attainment claim is made or needed (H3
grants C^1 only on the open set Omega \ S with one-sided C^0 limits,
which does not control whether trajectories reach S). No obligation
arises on slip/contact points.

*Step 4 (concatenation through mass-crossing points).* Let a
concatenated arc be given. By the Definitions (arc objects) it is a
FINITE concatenation of streamline arcs, so it has finitely many
matching points by construction; no finiteness inference from
isolation of crossing parameters is made or needed. Each constituent
streamline arc lies in the open set Omega \ S (S closed in Omega, H3)
and Gamma is constant on it (Step 1). At each matching point — a
mass-crossing point of S crossed transversally, by definition — the
one-sided limits of Gamma along the two matched pieces exist
(one-sided C^0 limits of the fields, H3, and continuity of r) and are
equal (Step 2, applicable pointwise since m != 0 from both sides at
the matching point, even on a component that is slip/contact
elsewhere). Hence Gamma takes a single constant value on the whole
concatenated arc.

*Step 5 (axis).* C^1 regularity of the three-dimensional field at the
axis forces w = O(r) as r -> 0, so Gamma -> 0; on-axis streamlines
carry Gamma = 0.
