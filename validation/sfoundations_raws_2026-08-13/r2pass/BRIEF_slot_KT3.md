# ADVERSARIAL REFUTATION BRIEF — slot KT-3 (single claim)

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

## TARGET CLAIM [KT-3] — rigor class THEOREM (as labeled by its author)

**Statement.** Let D be an open subset of the meridional half-plane with
inf_D r > 0, and Omega the open axisymmetric domain in R^3 it generates.
Let (u, rho, p) with u = (u_r, 0, u_z) (swirl-free) be a steady solution
of the compressible Euler equations on Omega satisfying:
(H1) axisymmetry: all fields independent of theta; azimuthal velocity
     identically zero;
(H2) inviscid, barotropic: p = P(rho) with P in C^1, P' > 0;
(H3) inertial frame, zero body force;
(H4) regularity: u, rho, p in C^1(Omega), rho > 0, |u| > 0 on every
     streamline arc considered.
Then the azimuthal vorticity omega_theta := d(u_r)/dz - d(u_z)/dr is
constant along every streamline of the flow.

**EOS status.** Barotropic class: includes the isentropic perfect gas
p = K rho^gamma and frozen per-streamline-entropy thermally-perfect
reductions; the statement is uniform over the class.

**FALSIFIER.** Evaluate omega_theta along streamlines of any committed
steady axisymmetric swirl-free compressible barotropic solution with
nonzero azimuthal vorticity (e.g. a rotational converging-nozzle inflow
field); drift of omega_theta along a single streamline beyond a
discretization-derived band (local truncation estimate propagated along
the arc) refutes the theorem.

**Proof route (author's, supplied).** In swirl-free axisymmetric flow
the vorticity field is purely azimuthal: omega = omega_theta e_theta.
Take the curl of the steady momentum equation
(u . grad)u = -(1/rho) grad p. Under barotropy (H2) the baroclinic
production (grad rho x grad p)/rho^2 vanishes identically. The
stretching-tilting term (omega . grad)u equals (omega_theta / r)
d(u)/d(theta), which vanishes by axisymmetry (H1). The curl of the
convective term therefore reduces the equation to
(u . grad) omega_theta = 0: the azimuthal vorticity is convected,
i.e. constant along streamlines; steadiness identifies pathlines with
streamlines.
