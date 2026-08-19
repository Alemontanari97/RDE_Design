# REFUTATION — slot KT-1 (SEEDv2)

Target: claim [KT-1], labeled THEOREM by its author: for steady planar
compressible barotropic Euler flow (H1-H3), the scalar vorticity
omega = d(u_y)/dx - d(u_x)/dy is constant along every streamline.

## 1. Summary of attack

The claim is FALSE as stated. The supplied proof route contains a
concrete algebraic error at the curl step: the curl of the convective
term in 2D is

    curl[(u . grad)u] = (u . grad) omega + omega (div u),

not (u . grad) omega. The author silently dropped the dilatation term
omega (div u), which vanishes identically only for solenoidal
(incompressible) flow. For compressible barotropic flow the correct
streamline invariant under exactly hypotheses (H1)-(H3) is the
potential vorticity omega / rho, not omega. A rigorous local
counterexample within the literal hypothesis set is constructed in
Section 3. Verdict: BROKEN.

## 2. Falsification at source (which step fails and why)

Author's route: "the curl of the convective term reduces the equation
to (u . grad) omega = 0."

Compute the curl exactly. Use the vector identity

    (u . grad)u = grad(|u|^2 / 2) + omega k x u,        (2D, omega = scalar)

where k is the out-of-plane unit vector. The curl of the gradient term
is zero. For the second term, with omega k x u = (-omega u_y, omega u_x):

    curl[omega k x u] = d(omega u_x)/dx + d(omega u_y)/dy
                      = div(omega u)
                      = (u . grad) omega + omega (div u).

The pressure side is handled correctly by the author: under barotropy
(H1), curl[-(1/rho) grad p] = -grad(1/rho) x grad p
= (1/rho^2) grad rho x P'(rho) grad rho = 0. So the exact steady
vorticity equation under (H1)-(H3) is

    (u . grad) omega + omega (div u) = 0.                          (*)

The author's route asserts (*) with the second term absent. That is the
defective step: it is a false identity for any flow with div u != 0,
and compressible flow generically has div u != 0 (indeed, a barotropic
flow with rho identically constant is incompressible; the whole point
of the compressible class is that rho varies).

The correct theorem under the same hypotheses. Combine (*) with steady
continuity div(rho u) = 0, i.e. (u . grad) rho = -rho (div u):

    (u . grad)(omega / rho)
      = (1/rho)(u . grad) omega - (omega / rho^2)(u . grad) rho
      = (1/rho)(-omega div u) - (omega / rho^2)(-rho div u)
      = 0.

So omega / rho — not omega — is constant along streamlines. This is
the classical 2D barotropic potential-vorticity theorem. The delivered
statement is the incompressible corollary mislabeled as a compressible
theorem.

## 3. Concrete counterexample (within the literal hypothesis set)

We exhibit a steady planar barotropic Euler solution satisfying
(H1)-(H3) on an open connected Omega, with a streamline along which
omega is strictly non-constant. The construction is a local
Cauchy-Kovalevskaya solution plus an explicit pointwise derivative
computation; both are checkable independently.

**Setup.** EOS: P(rho) = K rho^gamma, K > 0, gamma > 1 (inside the
author's declared class; P in C^1, P' = gamma K rho^(gamma-1) > 0).
Sound speed c^2(rho) = P'(rho). Unknowns w = (rho, u, v). The steady
Euler system:

    (1)  u rho_x + v rho_y + rho (u_x + v_y) = 0
    (2)  u u_x + v u_y + (c^2/rho) rho_x = 0
    (3)  u v_x + v v_y + (c^2/rho) rho_y = 0.

**Cauchy data** on the line x = 0, in a neighborhood of y = 0:

    u(0,y) = U0 > 0   (constant),
    v(0,y) = V0 != 0  (constant),
    rho(0,y) = R(y) = R0 (1 + eps y),   R0 > 0, eps != 0,

with U0 chosen non-sonic, e.g. U0 = 0.5 c(R0), and |eps y| small so
that rho > 0 and u != 0 on the neighborhood.

**Existence.** All data and coefficients are real-analytic (rho^gamma
is analytic for rho > 0). The line x = 0 is non-characteristic: writing
the system as A w_x + B w_y = 0 with ordering (rho, u, v),

    A = [[u, rho, 0], [c^2/rho, u, 0], [0, 0, u]],
    det A = u (u^2 - c^2) != 0

on the data (u = U0 != 0, U0^2 != c^2 by the subsonic choice). By
Cauchy-Kovalevskaya applied to w_x = -A^{-1} B w_y there exists a
unique real-analytic solution on an open connected neighborhood Omega
of the origin. Shrinking Omega keeps rho > 0 and |u| > 0 everywhere,
so (H1)-(H3) hold in full — the fields are C^1 (indeed C^omega).

**Pointwise computation at the origin.** From the data, all
y-derivatives on x = 0 are: u_y = 0, v_y = 0, rho_y = R'(y) = R0 eps.
Solve for the x-derivatives at (0,0) from (1)-(3):

From (3):  U0 v_x = -V0 v_y - (c^2/rho) rho_y
    =>  v_x = -(c^2 R0 eps) / (U0 R0) = -(c^2 eps)/U0  != 0.

From (1) and (2), with a := -(V0 R0 eps + R0 * 0) = -V0 R0 eps and
b := -V0 u_y = 0:

    U0 rho_x + R0 u_x = a,
    (c^2/R0) rho_x + U0 u_x = 0   =>   rho_x = -(R0 U0 / c^2) u_x.

Substituting, with M = U0/c:

    R0 u_x (1 - M^2) = a   =>   u_x = -V0 eps / (1 - M^2)  != 0.

Therefore at the origin:

    omega  = v_x - u_y = -(c^2 eps)/U0                != 0,
    div u  = u_x + v_y = -V0 eps / (1 - M^2)          != 0,

and by the exact vorticity equation (*):

    (u . grad) omega = -omega (div u)
                     = -(c^2 V0 eps^2) / (U0 (1 - M^2))  != 0.

The directional derivative of omega along the velocity at the origin is
nonzero, and by continuity it is nonzero on a neighborhood; hence omega
is strictly monotone (non-constant) along an arc of the streamline
through the origin. The streamline arc satisfies |u| > 0 (|u| >=
U0/2 > 0 near the origin). Every hypothesis (H1)-(H3) holds; the
conclusion fails. The claim is refuted by counterexample, not merely by
a gap.

**Consistency cross-check** (guards against an error in my own
algebra): the same pointwise data give

    (u . grad)(omega/rho) = (1/rho)(u.grad)omega - (omega/rho^2)(u.grad)rho
                          = -(omega/rho) div u + (omega/rho) div u = 0,

using continuity (u . grad) rho = -rho div u. The correct invariant
omega/rho is indeed conserved on the same counterexample flow — the
failure is specific to the delivered statement, exactly as the
source-level diagnosis predicts.

## 4. Note on the author's own FALSIFIER

The attached falsifier is well-posed and would FIRE against the claim:
evaluating omega along streamlines of any committed rotational
compressible solution with density variation along streamlines (e.g. a
rotational nozzle inflow accelerating through an area change) will show
omega drift = (omega/rho) * (rho drift), far beyond any truncation
band whenever the density ratio along the arc is order-one. The
falsifier refutes the theorem it accompanies; it does not save the
label.

## 5. Why not REPAIRABLE

REPAIRABLE requires a true core with only label defects. Here the
literal statement is false on its literal hypothesis set (Section 3
counterexample). The nearest true statements are different claims:
(i) omega/rho constant along streamlines (same hypotheses), or
(ii) omega constant along streamlines under the added hypothesis
div u = 0 (which collapses the compressible scope the claim
advertises). Replacing the conclusion or strengthening the hypotheses
produces a different theorem, not a relabeling of this one. Per the
brief's vocabulary, a false claim with falsification at source is
BROKEN.

## 6. Rejected attack lines (recorded for honesty)

- Attack on (H1) well-posedness of the barotropic class: rejected; the
  class is standard and the author's baroclinic-term cancellation under
  (H1) is correct as computed.
- Attack via special solutions (pure vortex with circular streamlines;
  parallel shear with constant pressure): rejected as counterexample
  sources — in those flows rho is constant along each streamline, so
  omega = rho * (omega/rho) happens to be streamline-constant too and
  the claim's conclusion accidentally holds. This is why the generic
  counterexample of Section 3 needs density variation along the
  streamline (nonzero V0 and eps), and it also explains how the false
  claim can survive casual spot-checks on symmetric test flows.
- Attack on "steadiness identifies pathlines with streamlines":
  rejected; that step is correct for steady fields with |u| > 0.

## Falsifier for this refutation

Two independent kill-switches, either of which refutes me:

1. Symbolic: verify the identity curl[(u . grad)u] = (u . grad)omega +
   omega div u in 2D with a CAS on generic C^2 fields (u(x,y), v(x,y)).
   If the CAS returns (u . grad)omega with no omega div u term, my
   source-level diagnosis is wrong and the refutation falls.
2. Numerical: march the Cauchy problem of Section 3 (analytic data
   U0 = 0.5 c(R0), V0 != 0, eps != 0, gamma = 1.4) with a high-order
   solver from x = 0; track omega and omega/rho along the streamline
   through the origin with a discretization-derived truncation band.
   If omega stays constant within band while (u.grad)omega's predicted
   nonzero value -omega div u fails to materialize — and omega/rho
   drifts instead — the counterexample construction is wrong and the
   refutation falls.

VERDICT: BROKEN
