# ADVERSARIAL REFUTATION — [SEED-B2] dual-seed re-run (corrected seed)

**Role:** adversarial refuter, S-FOUNDATIONS (R35) hypothesis audit, dual-seed slot.
**Date:** 2026-08-17.
**Seed correction context:** the prior seed ([SEED-B], `refute_SEED-B.md`) was REFUTED AS
GRADED because it fused the theorem-exact identity legs with the observables-to-pattern
propagation leg (of record SCHEMA, [S-T0P]). This re-run audits the corrected seed, in which
co-rotating steadiness is a **granted HYPOTHESIS**, not a claim — the propagation leg is
structurally excised. The target is therefore the pure frame-transport identity, standalone.

**Target claim (verbatim):** "GIVEN a compressible inviscid flow that IS steady in a
reference frame rotating uniformly about the symmetry axis (this steadiness is a HYPOTHESIS
here, not a claim), the long-time-averaged axial thrust evaluated in the laboratory frame
equals the steady axial thrust evaluated in the rotating frame: axial momentum flux,
pressure, and the axial projection of the control-surface integrand are invariant under the
frame rotation (the frame change adds only azimuthal velocity components, which do not enter
the axial momentum balance; centrifugal/Coriolis forces have zero axial component for
rotation about the axis). Rigor class: THEOREM, conditional only on the stated steadiness
hypothesis."

**OUTCOME: SOUND AS LABELED**, with named owed amendments (OB-1..OB-4 below). The
CONCLUSION (average-thrust equality) survives every attack mounted here and is in fact
strictly weaker than what is provable (instantaneous constancy on surfaces of revolution).
One mechanism conjunct as worded ("the axial projection of the control-surface integrand is
invariant") is FALSE on control surfaces with an azimuthal normal component — a concrete
counterexample is given — but the failure does not propagate to the conclusion: an exact
storage–flux cancellation identity (supplied in §3.5) repairs the proof for arbitrary
lab-fixed surfaces. Per the precedent of this same audit wave (`refute_SEED-B.md` SO-3:
perimeter omissions = owed amendment, not grade flip; grade flips reserved for the
propagation leg, which this seed excises), the defect is graded amendment-class.

---

## 1. Formal setup (the objects, pinned)

Cylindrical coordinates (r, θ, z), rotation axis = z = thrust axis (stated: "about the
symmetry axis"), uniform rate Ω. Lab frame K, rotating frame K′ with azimuth θ′ = θ − Ωt.

**Field correspondence (exact, definitional).** A flow steady in K′ means every field is a
function of (r, θ′, z) only. In the lab frame the same physical flow reads, for any scalar s
and for the cylindrical velocity components (the cylindrical basis vectors co-rotate with
the azimuth, so components transform cleanly):

- s_lab(r, θ, z, t) = s̃(r, θ − Ωt, z)  for s ∈ {ρ, p, e, u_r, u_z}
- u_θ,lab(r, θ, z, t) = ũ_θ(r, θ − Ωt, z) + Ω r

i.e. **u_lab = u_rot + Ω ê_z × x**, and Ω ê_z × x = Ω r ê_θ is purely azimuthal. Hence the
lab flow is a rigidly rotating pattern: time-periodic at every fixed lab point with period
T_p = 2π/Ω (or a divisor under discrete symmetry). This periodicity is a consequence of the
granted hypothesis, not an extra assumption.

**Thrust.** The physical object is the axial force on the body (engine). Control-surface
evaluations of it invoke the integral axial momentum balance; the surface conventions are
audited in §3.4–3.5 and OB-3.

## 2. Conjunct-by-conjunct verification (each step recomputed, not quoted)

**(V1) u_z invariance — EXACT.** Ω ê_z × x has zero axial component everywhere, so
u_z,lab(x,t) = ũ_z(r, θ−Ωt, z). No counterexample possible: this is algebra of the
transformation, valid for compressible, shocked, arbitrary-γ fields.

**(V2) ρ, p invariance — EXACT.** Density and thermodynamic pressure are scalars attached
to material states; a rotating change of coordinates relabels points, it does not change
scalar values. (Caveat checked: no "reduced pressure" absorbing the centrifugal potential is
in play — the claim uses true static pressure on both sides. No defect.)

**(V3) Fictitious forces, axial components — EXACT ZERO.** In K′, per unit mass:
- centrifugal: −Ω ê_z × (Ω ê_z × x) = Ω² r ê_r  → axial component 0;
- Coriolis: −2 Ω ê_z × u_rot = 2Ω (ũ_θ ê_r − ũ_r ê_θ) → axial component 0;
- Euler: −Ω̇ ê_z × x = 0 (uniform rotation, stated).
So the axial momentum equation in K′ carries no fictitious source; in conservative form,
∂_t(ρ ũ_z) + ∇·(ρ ũ_z u_rot) + ∂_z p = 0, and steadiness kills ∂_t. Exact as claimed.

**(V4) "Axial projection of the control-surface integrand is invariant" — FALSE AS A
UNIVERSAL; TRUE iff n_θ = 0 a.e. on the surface.** The lab and rotating axial flux
integrands on the same geometric surface element with unit normal n̂ differ by

  [ρ u_z (u_lab·n̂) + p n_z] − [ρ u_z (u_rot·n̂) + p n_z] = ρ u_z Ω r (ê_θ·n̂).

**Counterexample (kills the conjunct as worded):** take any control volume with a meridional
face (a patch of the half-plane θ = const, n̂ = ê_θ), e.g. a wedge CV of a sector model. On
that face the lab integrand exceeds the rotating one by ρ u_z Ω r ≠ 0 wherever axial mass
flux is nonzero. The companion parenthetical "azimuthal velocity components … do not enter
the axial momentum balance" fails on the same face: u_θ enters the axial balance through the
convective flux ρ u_z u_θ n_θ. On **surfaces of revolution about the axis** (exit planes,
cylindrical/conical side surfaces, axisymmetric walls — the surfaces of the T-T0 apparatus
of record) n_θ ≡ 0 and the conjunct is EXACT pointwise. The claim omits this perimeter.
→ OB-1. Whether this flips the grade is adjudicated in §4 (it does not: the conclusion is
insensitive, §3.5).

## 3. The conclusion under attack (attack log)

**A1 — Non-axisymmetric control surface (pointwise leg).** Kills conjunct (V4) as worded
(above). Does NOT kill the conclusion — see A3/§3.5. Outcome: amendment OB-1.

**A2 — Surface-frame convention / ill-posedness probe.** For a lab-fixed surface S that is
NOT a surface of revolution, "the steady axial thrust evaluated in the rotating frame
through S" is ILL-POSED: S rotates in K′, the flux through it is unsteady even though the
field is steady, and no single "steady value" exists. The equality must be read with each
frame's flux on a surface fixed in THAT frame (or, equivalently, thrust = force on the
body, which is surface-free). For surfaces of revolution the two conventions coincide and
the issue is invisible — which is why the intended (of-record) reading is safe. Outcome:
convention pin owed, OB-3; no counterexample to the intended statement.

**A3 — Momentum-storage term (the term the integrand-invariance wording silently drops).**
Lab-frame instantaneous balance on any lab-fixed CV V with outer surface S (body inside,
F_z = axial force on body):

  F_z(t) = − d/dt ∫_V ρ u_z dV − ∮_S [ρ u_z (u_lab·n̂) + (p − p_a) n_z] dS.

Attack: the claim never mentions d/dt ∫ ρu_z dV. Defense that holds: (i) on a CV of
revolution, ∫_V ρ u_z dV is invariant under azimuthal shift of the pattern ⇒ constant in
time ⇒ the term is IDENTICALLY zero, and F_z(t) is itself constant — the instantaneous
statement, stronger than the claim; (ii) on an arbitrary bounded lab-fixed CV, ρ u_z is
bounded and T_p-periodic, so the long-time average of the storage term is exactly
lim (1/T)[M(0)−M(T)] = 0. Outcome: no kill; the averaging in the claim is precisely what
retires this term in the general case.

**§3.5 (repair identity, makes the conclusion surface-free).** For the rotating pattern,
d/dt ∫_V ρ u_z dV = −Ω ∫_V ∂_θ(ρ u_z) dV; and since ∇·(Ω ê_z × x) = 0, the divergence
theorem gives ∮_S ρ u_z (Ω ê_z × x)·n̂ dS = ∫_V ∇·(ρ u_z Ω r ê_θ) dV = Ω ∫_V ∂_θ(ρ u_z) dV.
So the extra convective flux picked up by the lab evaluation on ANY lab-fixed closed surface
(the ρ u_z Ω r n_θ term of §2-V4) is EXACTLY the negative of the storage rate: the two
frame-dependent terms cancel identically, before any averaging. The axial momentum balance —
hence the thrust — is frame-transport-exact on every closed surface; only the pointwise
integrand identity needs n_θ = 0.

**A4 — Time-averaging vs frame-averaging.** At a fixed lab point (r, θ, z), the time
average over one period equals the azimuthal mean of the steady field on the circle of
radius r: ⟨f_lab⟩ = (1/2π)∮ f̃(r, θ′, z) dθ′. This is an exact pointwise transport identity
composed with averaging — the nonlinearity of the integrand is irrelevant because the
identity holds BEFORE averaging (no commutation-of-average-with-nonlinearity step exists to
attack). Integrated over a surface of revolution, the θ-average re-sums to the full steady
integral: equality holds instantaneously, a fortiori in average. On the axis r = 0 the
circle degenerates but single-valuedness of the field forces θ-independence there — no
failure. Outcome: no kill.

**A5 — Existence/convergence of the long-time average.** The lab signal is T_p-periodic
(consequence of the hypothesis), so the Cesàro limit exists for arbitrary (not just
period-commensurate) windows and equals the period average. Outcome: no kill; no extra
hypothesis needed beyond the granted steadiness.

**A6 — Unbounded domains / far-field surface choice.** If thrust is DEFINED via a surface
receding to infinity, the T→∞ average and the improper surface integral must be
interchanged, which requires decay/integrability of ρ u_z (u·n̂) and p − p_a at large
distance. This is a definitional prerequisite for "thrust" to exist at all, identical in
both frames (the frame change alters nothing at large |x| beyond the same Ω r ê_θ term
handled above) — a perimeter item, not a frame-invariance defect. For any finite CV,
irrelevant. Outcome: no kill; perimeter row in OB-2.

**A7 — Shocks and discontinuities (compressible, inviscid).** The integral momentum balance
is the weak form of Euler and holds across shocks (Rankine–Hugoniot consistent); the
transport identities of §1 are pointwise a.e. and survive piecewise smoothness. Genuine
edge: if a steady (in K′) front lies ALONG a positive-area patch of the chosen surface, the
trace of the integrand is two-valued there and the flux integral is ill-defined — the
of-record T-T0 perimeter already prints "piecewise-smooth transversal fronts" for exactly
this reason; the corrected seed dropped it. For a lab-fixed surface of revolution and a
rotating front, tangency occupies measure zero in time and the averaged statement is
unaffected; for the rot-fixed evaluation the transversality hypothesis is genuinely needed.
Outcome: no kill of the conclusion on transversal configurations; tacit-regularity row,
OB-2.

**A8 — Pressure gauge / ambient subtraction.** ∮ n_z dS = 0 on any closed surface, so the
constant p_a shifts both frames' evaluations identically (and not at all, on closed
surfaces). Outcome: no kill.

**A9 — Rigidly co-rotating non-axisymmetric body (the TDW-hardware reading).** If the body
itself co-rotates with K′ (so steadiness in K′ is natural), the lab body-surface is moving;
the axial pressure force ∮ p n_z dS over the rigidly rotated configuration is invariant
under rotation about z (n_z and dS are rotation-invariant, p co-rotates), hence CONSTANT in
lab time and equal to the K′ steady value. The theorem extends to this case; the claim
under-claims. Outcome: no kill; strengthening note OB-4.

**A10 — Non-uniform Ω (Euler force), axis misalignment, external body forces.** All
excluded by the wording ("uniformly", "about the symmetry axis", inviscid Euler with no
body force). An axial gravity, if added, contributes identically in both frames and cancels
in the equality. Outcome: no kill.

**A11 — Density weighting / compressibility probe.** Every step above used ρ as a field
with no constancy assumption; γ-law or tabulated thermo never enters (momentum balance
only). Variable-gamma status: γ-free. Outcome: no kill.

**A12 — Consistency with the granted hypothesis.** A lab-FIXED non-axisymmetric body is
generically inconsistent with K′-steadiness (its boundary condition rotates in K′) — but
the steadiness is granted BY HYPOTHESIS, so any such instance simply falls outside the
hypothesis; the theorem is conditional and takes no damage. Outcome: no kill (this is the
propagation-leg firewall of the corrected seed working as designed).

## 4. Hypothesis-completeness audit and grade adjudication

| Needed item | Stated? | Class | Grade impact |
|---|---|---|---|
| K′-steadiness, uniform Ω, rotation axis = thrust axis | YES (explicit) | hypothesis | — |
| Surfaces of revolution (n_θ = 0) for the POINTWISE integrand-invariance conjunct | NO | missing perimeter on one conjunct; conclusion repaired surface-free by §3.5 | OB-1, amendment |
| Piecewise-smooth fields, fronts transversal to the evaluation surface; integrability (and decay, if far-field surfaces define the thrust) | NO | tacit regularity (T-T0 prints it of record) | OB-2, amendment |
| Each frame's flux on a surface fixed in that frame (equivalently thrust = force on body) | NO | definitional convention | OB-3, amendment |
| Existence of the long-time average | not needed separately | consequence of the hypothesis (periodicity) | — |

**Adjudication.** The conclusion — long-time-averaged lab axial thrust equals K′-steady
axial thrust — admits NO counterexample under the granted hypothesis plus standard
definitional conventions: every frame-dependent term is either exactly zero axially
(V3), exactly cancelling (§3.5), or exactly average-free (A3), and the identity legs V1–V3
are unconditionally exact. The one false-as-worded conjunct (V4 universal reading) is a
perimeter omission on the MECHANISM, repairable inside the same hypothesis set, and this
audit wave's own precedent (`refute_SEED-B.md`: SO-3 perimeter omissions = owed amendments;
grade flips SO-1/SO-2 reserved for the propagation leg) grades exactly this defect
amendment-class. The propagation leg — the only grade-flipping content of the prior seed —
is absent here by construction. THEOREM is the correct label for the conclusion; the
phrase "conditional only on the stated steadiness hypothesis" is accurate for the
conclusion under standard conventions, and inaccurate only for the unqualified pointwise
conjunct, which the amendments below repair.

**Owed amendments (objections, none grade-flipping):**
- **OB-1:** restrict the integrand-invariance conjunct (and "azimuthal velocity does not
  enter the axial balance") to surfaces of revolution (n_θ = 0 a.e.), OR replace the
  mechanism by the storage–flux cancellation identity of §3.5, which makes the conclusion
  hold on arbitrary lab-fixed closed surfaces. Counterexample on meridional faces
  (ρ u_z Ω r n_θ term) must be recorded.
- **OB-2:** print the regularity perimeter: piecewise-smooth fields with fronts transversal
  to the evaluation surface (well-defined traces a.e.); integrals convergent; for
  far-field-surface definitions of thrust, decay sufficient to interchange average and
  improper integral (frame-symmetric).
- **OB-3:** pin the convention: each frame's flux is evaluated on a surface fixed in that
  frame (for non-axisymmetric surfaces the "same-surface" rotating-frame reading is
  ill-posed); equivalently state the theorem for the force on the body.
- **OB-4 (strengthening, under-claim):** on surfaces of revolution the INSTANTANEOUS lab
  thrust is already constant in time and equal to the K′ value (averaging is a corollary,
  not a need), and the result extends to rigidly co-rotating non-axisymmetric bodies. The
  averaged form should cite the instantaneous form as the parent statement (consistent with
  T-T0(i) of record).

## 5. Verdict

**SOUND AS LABELED** (THEOREM, conditional on the granted steadiness hypothesis), with owed
amendments OB-1..OB-4. The corrected seed does its job: with the propagation leg excised,
the residue is an exact frame-transport identity; the only defect found is a perimeter
omission on one mechanism conjunct, repaired herein without new hypotheses.

**Limits of this refutation:** first-principles verification (all steps recomputed above,
none quoted on authority); in-repo sources consulted for precedent-consistency only
(`refute_SEED-B.md`); no environment changes, no installs, no numerics required (all legs
are closed-form identities).
