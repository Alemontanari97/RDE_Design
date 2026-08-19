# REFUTATION — slot KT-3 (SEEDv3)

Target: claim [KT-3], labeled THEOREM by its author — "in steady swirl-free
axisymmetric compressible barotropic Euler flow (H1–H4), the azimuthal
vorticity omega_theta = d(u_r)/dz − d(u_z)/dr is constant along every
streamline."

**Verdict up front: BROKEN.** The claim is false as stated, under its own
literal hypothesis set, for every flow in the class with nonzero azimuthal
vorticity on a streamline along which rho·r is non-constant — i.e. for the
generic rotational member of the class, including the very field the
author's own falsifier names. The conserved quantity is omega_theta/(rho r),
not omega_theta. Two independent, individually fatal errors sit in the
supplied proof route; a concrete counterexample with an explicit data set
and a computed nonzero drift is produced below.

---

## 1. Falsification at source — the two failing steps of the supplied proof

### 1.1 Error A (fatal even in the incompressible limit): the stretching
### term does NOT vanish by axisymmetry

The author writes: "the stretching-tilting term (omega . grad)u equals
(omega_theta / r) d(u)/d(theta), which vanishes by axisymmetry (H1)."

This confuses theta-independence of the *components* with vanishing of the
theta-derivative of the *vector field*. In cylindrical coordinates the
basis vectors rotate:

    d(e_r)/d(theta) = e_theta,   d(e_theta)/d(theta) = -e_r,   d(e_z)/d(theta) = 0.

With u = u_r(r,z) e_r + u_z(r,z) e_z (components theta-independent by H1):

    d(u)/d(theta) = u_r * d(e_r)/d(theta) = u_r e_theta  ≠ 0   whenever u_r ≠ 0.

Hence

    (omega . grad)u = (omega_theta / r) d(u)/d(theta) = (omega_theta u_r / r) e_theta,

which is exactly the classical vortex-ring stretching by radial motion. It
vanishes only where u_r = 0 or omega_theta = 0 — neither is granted by
H1–H4 (H4 grants |u| > 0, not u_r = 0). This term alone already breaks the
claim in the incompressible limit, where the true conserved quantity is
omega_theta / r (the classical axisymmetric result; e.g. Hill's spherical
vortex has omega_theta = A·r varying along its closed streamlines).

### 1.2 Error B (fatal for the compressible class as claimed): the
### dilatation term is silently dropped

The curl of the steady momentum equation in the form
grad×[(u·grad)u] = grad×[ω×u] + grad(|u|²/2) uses

    grad×(ω×u) = (u·grad)ω − (ω·grad)u + ω (div u) − u (div ω).

The author's reduction keeps only (u·grad)ω. Besides Error A (the
(ω·grad)u term), the term ω(div u) is nonzero in any genuinely
compressible flow — and H2 with P' > 0 finite forces genuine
compressibility on any non-trivial solution: a solution of the barotropic
system with rho ≡ const has p = P(rho) ≡ const, hence (u·grad)u = 0, which
excludes every flow the claim is about. So the dropped dilatation term is
active precisely on the claim's domain. Dropping it assumes
incompressibility, contradicting the claimed EOS class ("uniform over the
class").

### 1.3 The correct transport law, derived at component level (no vector
### identities, so no identity-level traps)

Steady, axisymmetric, swirl-free momentum in cylindrical components:

    (r):  u_r ∂r u_r + u_z ∂z u_r = −(1/rho) ∂r p
    (z):  u_r ∂r u_z + u_z ∂z u_z = −(1/rho) ∂z p

Apply ∂z to (r) minus ∂r to (z). The right side is the baroclinic bracket
(1/rho²)(∂z rho ∂r p − ∂r rho ∂z p), which vanishes identically under H2
(p = P(rho) makes grad p parallel to grad rho) — this step of the author's
route is CORRECT and was not contested. The left side, expanded and
regrouped with omega := omega_theta = ∂z u_r − ∂r u_z, is identically

    u·grad(omega) + omega (∂r u_r + ∂z u_z) = 0.                     (T1)

(Verified symbolically: sympy residual of [∂z(mom_r) − ∂r(mom_z)] minus
[u·grad ω + ω(∂r u_r + ∂z u_z)] simplifies to 0; script quoted in §4.)

Since div u = ∂r u_r + u_r/r + ∂z u_z, (T1) reads

    u·grad(omega) = omega ( u_r/r − div u ).                          (T2)

Steady continuity div(rho u) = 0 gives div u = −(u·grad rho)/rho, and
u_r/r = u·grad(ln r); hence

    u·grad(omega) = omega · u·grad( ln(rho r) )
    ⇔  u·grad( omega_theta / (rho r) ) = 0.                           (T3)

The invariant of the class is omega_theta/(rho r). The claim's invariant
omega_theta is conserved iff additionally u·grad(rho r) = 0 on the
streamline — a hypothesis nowhere in H1–H4 and false for generic members
(any streamtube of varying area/radius). The right side of (T2) is the
exact sum of the two terms the proof route discarded: Error A contributes
omega u_r/r, Error B contributes −omega div u.

## 2. Concrete counterexample (explicit data, local analytic solution,
## computed nonzero drift)

Take P(rho) = rho (so P' = 1 > 0, C^1: H2 holds; this is the barotropic
class member c² = 1). Prescribe analytic Cauchy data on the segment
{z = 0, r ∈ (1/2, 3/2)}:

    u_r(r,0) = 1,    u_z(r,0) = 2 − (r − 1),    rho(r,0) = 1.

The steady system (continuity + r-momentum + z-momentum), viewed as an
evolution in z for U = (u_r, u_z, rho), has z-coefficient matrix with
determinant u_z (u_z² − c²); at the point (r0,z0) = (1,0) this equals
2·(4 − 1) = 6 ≠ 0, so the data surface is non-characteristic there. All
coefficients and data are real-analytic near (1,0) (r bounded away from 0),
so Cauchy–Kovalevskaya yields a unique real-analytic solution (u_r,u_z,rho)
on a neighborhood N of (1,0). Take D ⊂ N a small disc around (1,0): then
inf_D r > 0, and by continuity rho > 0, |u| ≥ ~√5 > 0, all fields analytic
⊂ C^1 on D — H1, H2, H3, H4 all hold on the generated axisymmetric Omega.
This is a bona fide member of the claim's class.

First derivatives at (1,0) are determined algebraically by the data and the
three PDEs (this is the CK first step, so they belong to the solution, not
to a choice of mine):

    from (r)-momentum:  ∂z u_r = 0            (since ∂r u_r = 0, ∂r rho = 0)
    from (z)-momentum + continuity:  ∂z u_z = 1,  ∂z rho = −1.

Hence at (1,0):

    omega_theta = ∂z u_r − ∂r u_z = 0 − (−1) = 1 ≠ 0,
    ∂r u_r + ∂z u_z = 0 + 1 = 1,

and by (T1), which holds on any solution using only first derivatives:

    u·grad(omega_theta) |_(1,0) = −(1)·(1) = −1 ≠ 0.

The streamline arc through (1,0) exists (|u| = √5 > 0, H4's own condition)
and along it d(omega_theta)/ds = −1/√5 ≠ 0 at s = 0: omega_theta is
strictly decreasing there, not constant. Cross-check via the true invariant
(T3): u·grad(ln(rho r)) = u_r/r + (u·grad rho)/rho = 1 + (1·0 + 2·(−1)) = −1,
and omega·(−1) = −1 — consistent. The three PDE residuals at the point
evaluate to (0, 0, 0) with these derivatives (verified numerically, §4).

This falsifies the theorem on its literal hypothesis set: one flow in the
class, one streamline, non-constant omega_theta.

## 3. Independent confirmation (second route) and scope of the true result

Crocco form of steady barotropic momentum: grad H = u × omega with
H = |u|²/2 + Pi(rho), Pi' = P'/rho. With the compressible Stokes stream
function (∂r psi = rho r u_z, ∂z psi = −rho r u_r) one gets
grad H = −(omega_theta/(rho r)) grad psi, hence wherever grad psi ≠ 0,
H = H(psi) and

    omega_theta = −rho r H'(psi):

omega_theta/(rho r) is the streamline invariant, and omega_theta itself is
constant along a streamline only in the degenerate subcases (i) H'(psi) = 0
on that streamline (irrotational there — then the claim is trivially true
with omega_theta ≡ 0), or (ii) rho r constant along the streamline (e.g.
purely columnar u_r ≡ 0, div u = 0 flows). The claim asserts the conclusion
for EVERY flow in H1–H4 and is therefore false. Note also that if the claim
were true, combining it with (T3) would force u·grad(rho r) = 0 on every
rotational streamline — a strong kinematic constraint manifestly not
implied by H1–H4.

Honesty notes (attacks that FAILED, and one credit):
- The baroclinic-cancellation step of the author's route is correct under
  H2; I could not break it. The failure is strictly downstream of it.
- H4's |u| > 0 and inf_D r > 0 do not rescue the claim (both hold in the
  counterexample); no reading of H1–H4 I could construct excludes the
  counterexample.
- Credit: the author's FALSIFIER is well-posed and would itself have caught
  the error — a rotational converging-nozzle inflow has H' ≠ 0 and varying
  rho r along streamlines, so the prescribed omega_theta-drift test fires.
  The falsifier refutes its own theorem; this is a falsification the
  committed-field test would deliver, consistent with §2.

Why BROKEN and not REPAIRABLE: the verdict vocabulary reserves REPAIRABLE
for a true core whose label is unearned. Here the stated conclusion is
false; the true statement (omega_theta/(rho r) constant along streamlines,
equivalently omega_theta = −rho r H'(psi)) is a DIFFERENT claim, not a
mechanical repair of this one (the invariant itself changes). That corrected
statement, with the §1.3 component-level proof, hypothesis list H1–H4 as
given, spaces C^1 as given, and EOS status unchanged, would earn THEOREM —
but as a replacement, not a repair.

## 4. Executable evidence

Symbolic + numeric verification script (sympy; run under the pinned env,
exit clean):

```python
import sympy as sp
r, z = sp.symbols('r z', positive=True)
ur = sp.Function('u_r')(r, z); uz = sp.Function('u_z')(r, z)
rho = sp.Function('rho')(r, z); P = sp.Function('P'); p = P(rho)
mom_r = ur*sp.diff(ur,r) + uz*sp.diff(ur,z) + sp.diff(p,r)/rho
mom_z = ur*sp.diff(uz,r) + uz*sp.diff(uz,z) + sp.diff(p,z)/rho
w = sp.diff(ur,z) - sp.diff(uz,r)
curl_mom = sp.diff(mom_r,z) - sp.diff(mom_z,r)
res = sp.simplify(curl_mom - (ur*sp.diff(w,r) + uz*sp.diff(w,z)
      + w*(sp.diff(ur,r) + sp.diff(uz,z))))
print(res)   # -> 0  : identity (T1); baroclinic bracket cancels under p=P(rho)
```

Output obtained: identity residual `0`; conservation residual for
u·grad(omega/(rho r)) under (T1)+continuity `0`; counterexample PDE
residuals at (1,0) `(0.0, 0.0, 0.0)`; omega_theta = 1;
u·grad(omega_theta) = −1; CK determinant = 6.

---

VERDICT: BROKEN

**Falsifier for this refutation.** This refutation is itself refuted if any
one of the following is exhibited: (i) an algebra error in the
component-level identity (T1) — checkable in one line by the quoted sympy
script (a nonzero simplified residual kills §1.3 and §2); (ii) a proof that
the Cauchy data of §2 is characteristic at (1,0) or otherwise admits no
local analytic solution (i.e. det = u_z(u_z² − c²) = 0 there, contradicting
the computed value 6, or a demonstrated failure of Cauchy–Kovalevskaya
applicability despite analytic, non-characteristic data); or (iii) a valid
derivation, from H1–H4 alone, that u·grad(rho r) = 0 along every streamline
of every flow in the class (which would reconcile (T3) with the target
claim). Absent all three, BROKEN stands.
