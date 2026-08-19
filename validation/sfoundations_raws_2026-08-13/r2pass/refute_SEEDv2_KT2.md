# ADVERSARIAL REFUTATION — slot KT-2

Target: claim [KT-2] (Gamma = r*w streamline invariant, steady axisymmetric
compressible Euler, f_theta = 0), labeled THEOREM by its author.
Source consumed: BRIEF_slot_KT2.md ONLY (per task order).
Binding standard applied: explicit hypothesis list, named function spaces,
every proof step justified, falsifier attached, EOS/variable-gamma status
declared. Both truth and label attacked.

---

## 1. Summary

The mathematical core is TRUE. It is the classical steady-swirl circulation
invariant (the Gamma = Gamma(psi)-type result underlying the
Bragg–Hawthorne/Squire–Long formulation, here stated in the weaker and safer
per-arc form). Every counterexample channel I opened is closed by an
explicitly declared hypothesis — the hypothesis set is well-chosen and does
real work. The EOS-FREE declaration survives audit. However, the proof route
AS DELIVERED contains three elisions, one of which (the shock step) cites a
literally insufficient mechanism: the quoted justification, read as written,
is satisfied by a configuration in which [w] != 0. All three defects have
purely mechanical repairs and none hides a falsity. Under the binding
standard "every proof step justified", the label is not earned as delivered.

**VERDICT: REPAIRABLE** (defects L1–L3 below, each with its repair).

---

## 2. Truth attacks (all REJECTED — recorded for honesty)

### T-A. Direct verification of the core transport identity
At r > 0, multiply the (correct, general) azimuthal momentum component by r:
r*(u_r dw/dr + u_z dw/dz) + u_r w
  = u_r d(rw)/dr + u_z d(rw)/dz          [since d(rw)/dr = w + r dw/dr,
                                           d(rw)/dz = r dw/dz]
and the azimuthal advection term (w/r) dw/dtheta contributes
(w/r) d(rw)/dtheta = 0 under H1. With H1 killing dp/dtheta and H2 killing
f_theta, (u . grad)(r w) = 0 exactly. The algebra CHECKS. No division by r
is ever performed (multiplication only), so r = 0 causes no singularity in
the identity. Attack fails.

### T-B. Rotating-frame counterexample
In a rotating frame the Coriolis force has an azimuthal component and
Gamma_relative = r*w_rel is NOT conserved (Gamma based on absolute swirl
is). This would break the claim — but H2 explicitly pins the inertial frame.
Excluded by hypothesis. Attack fails.

### T-C. Azimuthal body force
Any f_theta != 0 (e.g. an azimuthal MHD Lorentz force) sources Gamma along
streamlines. Excluded verbatim by H2. Attack fails.

### T-D. Helical / non-axisymmetric shock
A discontinuity surface with n_theta != 0 has e_theta partly NORMAL to the
surface; RH normal momentum then permits [w] != 0 through the pressure jump,
and Gamma jumps across it. This is the realistic RDE configuration (spinning
detonation front). It would refute the piecewise extension — but H3
explicitly restricts to axisymmetric discontinuity surfaces (n_theta = 0),
so it is out of scope by declared hypothesis, not by omission. Attack fails
against the literal hypothesis set. (Scope remark, not a defect: the
hypothesis is declared, so the theorem honestly does not cover the spinning
wave itself.)

### T-E. Contact/slip surfaces carrying [w] != 0
Real: an axisymmetric slip surface can carry an arbitrary swirl jump
(m = rho*u_n = 0 kills the tangential-momentum constraint). But the claim
never asserts [Gamma] = 0 there; it asserts streamlines do not cross such
surfaces. u_n = 0 on both sides indeed forbids transversal crossing. Attack
fails. (See L3 for the related label gap on arcs that REACH such a surface.)

### T-F. Pure-swirl circles (|u| > 0, meridional velocity = 0)
If u_r = u_z = 0 but w != 0 at a point, axisymmetry makes the whole circle
r = r0, z = z0 the unique integral curve (u is C^1, hence locally Lipschitz,
so uniqueness holds). Along it dGamma/dt = (w/r) d(rw)/dtheta = 0 by H1.
The claim holds on these degenerate arcs too. Attack fails.

### T-G. Axis behavior
For a C^1(Omega) Cartesian vector field whose cylindrical components are
theta-independent: w = -u_x sin(theta) + u_y cos(theta); theta-independence
at r -> 0 forces u_x = u_y = 0 on the axis, and C^1 then gives u_x, u_y =
O(r), hence w = O(r) and Gamma = O(r^2) -> 0. The H3 assertion "C^1 forces
w = O(r)" is TRUE as stated (given H1). Attack fails.

### T-H. Recirculation bubbles / closed streamlines
Closed meridional streamlines (vortex breakdown bubbles) are still integral
curves of a C^1 field satisfying (u.grad)Gamma = 0; constancy holds; no
monodromy obstruction because the invariant is transported, not integrated
from a multivalued potential. Attack fails.

### T-I. EOS audit (attack on the EOS-FREE declaration)
Steps consumed by the proof: azimuthal momentum (pressure enters ONLY
through dp/dtheta, killed kinematically by H1, never through an EOS); RH
mass and RH tangential momentum (no energy RH, no caloric relation). No
step evaluates p(rho, T) or gamma. EOS-FREE stands for gamma = const,
gamma(T), and any inviscid fluid, as declared. Attack fails.

### T-J. Falsifier adequacy
The attached falsifier is operational (trace Gamma along streamlines of a
certified swirling MoC field against a discretization-derived band). Attack
attempted: "a numerical field is not an exact C^1 Euler solution, so it can
never literally produce the refuting object." Rejected: the
truncation-propagated band is exactly the device that converts numerical
drift into evidence against the exact statement; band-exceeding drift on a
certified field is a genuine refutation channel. Falsifier attached and
non-vacuous. Attack fails.

Conclusion on truth: NO counterexample exists against the literal
hypothesis set. The core is a textbook-solid kinematic theorem.

---

## 3. Label attacks (defects found — this is where the label fails)

### L1 (principal defect). The shock step cites an insufficient mechanism.
Delivered text (theorem statement AND proof route): "Rankine-Hugoniot
tangential momentum with n_theta = 0 forces [w] = 0."
This is literally false as a standalone implication. RH tangential momentum
on a surface with n_theta = 0 reads
  [ m * w ] = 0,   with m := rho * u_n
(the pressure term p*n_theta vanishes). This alone does NOT force [w] = 0:
the configuration m1*w1 = m2*w2 with m1 != m2 and w1 != w2 satisfies the
cited condition with [w] != 0. What closes the leak is RH MASS conservation,
[m] = 0, which is nowhere invoked in the delivered route, PLUS the shock
property m != 0 (only implicit in the word "shock"), giving
  [m] = 0, m != 0  ==>  m*[w] = 0  ==>  [w] = 0.
The limiting case proves the insufficiency is real, not pedantic: on a
slip surface (m = 0) the cited tangential-momentum condition holds
identically while [w] is arbitrary — the delivered justification cannot
distinguish the two cases; the omitted mass step is what does.
**Repair (mechanical, two lines):** state RH mass [rho*u_n] = 0; define
shock by m != 0; conclude m*[w] = 0 hence [w] = 0; note r continuous;
hence [Gamma] = 0.

### L2. The starting equation is internally inconsistent as delivered, and
H1's consumption is miscredited.
The route opens: "The azimuthal component of steady Euler momentum reads
u_r dw/dr + u_z dw/dz + u_r w / r = -(1/(rho r)) dp/dtheta + f_theta."
The GENERAL azimuthal component contains the advection term
(w/r) dw/dtheta, which is absent here even though the theta-derivative
dp/dtheta is retained. So the displayed equation is neither the general
form (missing a term) nor the axisymmetric form (retaining dp/dtheta):
axisymmetry has been half-applied silently. The route then credits H1 only
with killing the pressure term, concealing that H1 was already consumed to
delete the advection term. Under "every proof step justified" this is an
unjustified (because invisible) step.
**Repair (mechanical):** display the full component
u_r dw/dr + (w/r) dw/dtheta + u_z dw/dz + u_r w/r
 = -(1/(rho r)) dp/dtheta + f_theta,
then invoke H1 once to kill BOTH theta-derivative terms and H2 for f_theta.

### L3. Streamline continuation across the shock is asserted, not
constructed.
The theorem's conclusion composes per-piece constancy with [Gamma] = 0 into
constancy "along every streamline arc", including arcs crossing shocks. For
a piecewise-C^1 field the trajectory is defined only piecewise; the
concatenation of the two C^1 arcs into ONE streamline arc requires that the
trajectory actually crosses: u_n traces nonzero and of the SAME sign on
both sides. This is derivable — [rho*u_n] = 0 with rho > 0 on both sides
gives sign(u_n^+) = sign(u_n^-) != 0 at a shock — but it is nowhere stated,
and it is the step that makes "streamline arc" well-defined through the
discontinuity at all. (It also silently consumes rho > 0 from H3, a
dependence the delivered route never declares for this purpose.)
**Repair (mechanical, three lines):** from [m] = 0, m != 0, rho > 0
conclude u_n same-signed and nonzero; define the crossing arc as the
concatenation of the two one-sided integral curves at the transversal
crossing point; per-piece constancy + [Gamma] = 0 then yields constancy on
the concatenated arc.

None of L1–L3 threatens the truth of the statement; each is a hole in the
DELIVERED justification with a named, purely mechanical repair. With the
three repairs applied, the claim earns THEOREM in full.

---

## 4. Items examined and cleared (non-defects)

- Hypothesis list: explicit, and each hypothesis is load-bearing (H1 kills
  two terms; H2 kills the source; H3 delivers uniqueness of integral
  curves, the axis behavior, rho > 0 for L3's repair, and the n_theta = 0
  restriction). PASS.
- Function spaces: named (C^1(Omega); piecewise-C^1 with axisymmetric
  discontinuity surfaces). PASS.
- Falsifier: attached, operational, non-vacuous (T-J). PASS.
- EOS/variable-gamma status: declared and verified correct (T-I). PASS.
- The |u| > 0 restriction correctly excises stagnation points where arcs
  are ill-defined; degenerate pure-swirl circles covered (T-F). PASS.
- "On the axis Gamma = 0 identically": follows from the verified w = O(r)
  (T-G). PASS.

---

## 5. Verdict and falsifier for this refutation

**VERDICT: REPAIRABLE**

Falsifier for this refutation (how to kill it): the verdict downgrades on
label only, so it is refuted by showing the delivered route is already
complete at the flagged points — concretely, ANY of:
(1) a derivation that [w] = 0 follows from RH tangential momentum alone on
an m != 0 surface WITHOUT invoking RH mass — i.e. exhibit why
m1*w1 = m2*w2 with m1 != m2, w1 != w2 is excluded using only the cited
condition (defeats L1);
(2) a demonstration that the displayed opening equation IS the correct
general azimuthal Euler component, i.e. that (w/r) dw/dtheta does not
belong in it (defeats L2);
(3) a demonstration that "streamline arc" is well-defined across a
discontinuity of a piecewise-C^1 field without any same-sign/nonzero
condition on the u_n traces (defeats L3).
If all three are defeated, the correct verdict becomes SOUND-AS-LABELED
(the truth analysis of §2 already stands unconditionally). Conversely, a
concrete compliant counterexample to the statement itself would upgrade the
refutation to BROKEN; §2 records my failure to produce one across nine
channels.
