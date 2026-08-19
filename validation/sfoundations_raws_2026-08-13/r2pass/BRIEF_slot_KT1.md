# ADVERSARIAL REFUTATION BRIEF — slot KT-1 (single claim)

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

## TARGET CLAIM [KT-1] — rigor class THEOREM (as labeled by its author)

**Statement.** Let Omega be an open connected subset of R^2 and let
(u, rho, p) be a steady planar solution of the compressible Euler
equations on Omega with:
(H1) inviscid, barotropic: p = P(rho) with P in C^1, P' > 0;
(H2) inertial frame, zero body force;
(H3) regularity: u, rho, p in C^1(Omega), rho > 0, and |u| > 0 on every
     streamline arc considered.
Then the scalar vorticity omega := d(u_y)/dx - d(u_x)/dy is constant
along every streamline of the flow.

**EOS status.** Barotropic class: includes the isentropic perfect gas
p = K rho^gamma and frozen per-streamline-entropy thermally-perfect
reductions; the statement is uniform over the class.

**FALSIFIER.** Evaluate omega along streamlines of any committed steady
planar compressible barotropic solution with nonzero vorticity (e.g. a
rotational nozzle inflow field); drift of omega along a single streamline
beyond a discretization-derived band (local truncation estimate
propagated along the arc) refutes the theorem.

**Proof route (author's, supplied).** Take the curl of the steady
momentum equation (u . grad)u = -(1/rho) grad p. Under barotropy (H1),
grad(1/rho) x grad p = 0, so the baroclinic production term vanishes
identically; the curl of the convective term reduces the equation to
(u . grad) omega = 0, i.e. omega is convected: constant along
streamlines. Steadiness identifies pathlines with streamlines.
