# REFUTATION — dual-seed canary slot (adversarial proof refuter)

- **Slot**: SEED_canary (dual-seed batch, S-FOUNDATIONS Phase D)
- **Date**: 2026-08-17
- **Lens**: conservation-law / explicit-counterexample
- **Target claim (verbatim, standalone)**: "For steady axisymmetric flow with
  swirl, the azimuthal velocity w itself (NOT r*w) is transported unchanged
  along streamlines, so w is constant on each streamline; rigor class THEOREM."
- **VERDICT: BROKEN** (claim is false as stated; the "NOT r*w" clause makes it
  the explicit negation of the true theorem, so no repair preserves the claim)

## 1. Setting and hypothesis reconstruction

The claim names no function space and no hypothesis list (already a violation
of the binding SOTA standard for the label THEOREM). The most favorable
reading: steady (∂_t ≡ 0) axisymmetric (∂_θ ≡ 0) inviscid flow, velocity
`(u, v, w)` in cylindrical components (radial, axial, azimuthal), fields
C¹ on an open set Ω ⊂ {r > 0}, no azimuthal body force. Density law
unrestricted (incompressible or compressible, any equation of state — the
refutation below is purely kinematic/momentum-based, so it is
**gas-model independent: valid for γ(T) thermally-perfect frozen mixture and
for γ = const alike**; the claim itself declares no variable-γ status,
a second standard violation).

## 2. The defect, from the momentum equations (one line)

The θ-component of the steady Euler equations under axisymmetry is

    u ∂w/∂r + v ∂w/∂z + (u w)/r = 0                                   (θ-mom)

(the (u w)/r term is the metric/Coriolis term of cylindrical coordinates; it
is present for ANY density law since the θ pressure gradient vanishes under
∂_θ ≡ 0). Multiplying by r and regrouping:

    u ∂(r w)/∂r + v ∂(r w)/∂z = 0        ⇔        D(r w)/Ds = 0.

So the streamline invariant is the **angular momentum per unit mass r·w**
(equivalently the circulation Γ = 2π r w), and along a streamline

    Dw/Ds = −(u w)/r,

which is **nonzero wherever the streamline changes radius (u ≠ 0) with
nonzero swirl (w ≠ 0)**. The claim asserts Dw/Ds = 0; that holds only in the
degenerate subclass u·w ≡ 0 (cylindrical streamsurfaces r = const, or no
swirl), which is not what "for steady axisymmetric flow with swirl" states.
The claim is the negation of the classical result (Batchelor, *An
Introduction to Fluid Dynamics*, §7.5; Vazsonyi/Long axisymmetric
Bragg–Hawthorne setting, where C(ψ) = r w is one of the two streamfunction
invariants).

## 3. Explicit counterexample (exact steady Euler solution)

Inviscid strained line vortex (Burgers vortex at ν = 0), incompressible:

    u = −a r,   v = 2 a z,   w = Γ/(2π r),      a > 0, Γ ≠ 0,  on r > 0.

- Continuity: (1/r)∂(r u)/∂r + ∂v/∂z = −2a + 2a = 0. ✔
- θ-momentum: u ∂w/∂r + (u w)/r = (−a r)(−Γ/2πr²) + (−a r)(Γ/2πr)/r = 0. ✔
- r- and z-momentum are closed by the exact pressure
  p/ρ = C − a²(r² + 4z²)/2 − Γ²/(8π²r²) (radial: −u∂u/∂r + w²/r =
  a²r + Γ²/(4π²r³) = ∂(p/ρ)/∂r ✔; axial: v∂v/∂z = 4a²z = −∂(p/ρ)/∂z ✔).

Along any streamline, r(t) = r₀e^{−at} decreases, so w = Γ/(2πr) **grows
without bound**, while r·w = Γ/2π is exactly constant. A single smooth
steady axisymmetric swirling Euler solution on which w is unbounded along a
streamline: the THEOREM label is refuted with maximal prejudice.

## 4. Numeric confirmation (pinned env, nothing installed)

Script: scratchpad `canary_check.py` (analytic residuals on a 41×41 grid in
[0.5,3.0]×[0.1,2.0] + RK4 particle trace, dt = 1e-4, t ∈ [0, 0.7], seed-free
deterministic). Measured output:

    continuity  max|res| = 0.000e+00
    theta-mom   max|res| = 2.220e-16   (D(rw)/Dt)
    Dw/Dt       max|val| = 2.000e+00   (NONZERO)
    particle: r 2.000000 -> 0.993270
    w  along streamline: 0.500000 -> 1.006776  rel change = 1.014e+00
    rw along streamline: 1.000000 -> 1.000000 rel change = 1.110e-16

w changes by **101%** along the traced streamline; r·w is conserved to
machine epsilon. Both rejector asserts (r·w drift < 1e-10; w change > 0.5)
armed and passed.

## 5. Why BROKEN and not REPAIRABLE

The true statement ("r·w is constant on streamlines of steady axisymmetric
inviscid flow, absent azimuthal forcing") is a different claim that the
target explicitly disavows ("NOT r*w"). Repairing means replacing the claim
with its negation-in-part; under the batch's labeling discipline that is
BROKEN, not REPAIRABLE. Secondary independent defects, each alone fatal to
the THEOREM label: (i) no hypothesis list (inviscidity, no azimuthal body
force, and r > 0 are all load-bearing and unstated); (ii) no function space;
(iii) no variable-γ declaration; (iv) no falsifier attached; (v) even in the
viscous case the claim stays false (D(rw)/Dt = ν(∇² − 1/r²)(…) sources rw,
it does not rescue w).

## 6. Program cross-check (consistency, not authority)

The program's own mean-swirl M0 treatment and the MoC swirl branch are built
on the r·w (angular-momentum) invariant; accepting the canary claim would
contradict the certified engine's transport structure. Per the doubts-ledger
discipline this cross-check is corroborative only — the refutation stands on
§§2–4 alone.

## FALSIFIER (for this refutation)

If someone exhibits C¹ fields (u, v, w) on an open Ω ⊂ {r > 0} satisfying
steady axisymmetric Euler (any barotropic or thermally-perfect closure, no
azimuthal force) with u·w ≢ 0 on some streamline and w constant along that
streamline, this refutation is rejected. By §2 that requires (u w)/r = 0
where u·w ≠ 0 — impossible on r > 0 — so the falsifier is well-posed and
provably unsatisfiable, which is the strongest form a refutation can take.

**Verdict: BROKEN. The streamline invariant is r·w; w itself is not
transported. Rigor class of the refutation: THEOREM (complete proof, §2–§3,
+ machine-precision numeric witness §4). γ-status: gas-model independent.**
