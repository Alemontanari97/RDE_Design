# PROGRESS — [F2/A1] S24: the general inlet — rotational MoC (2026-08-11)

**Carrier:** `validation/a1_rot_march.py` ([X-RMAR]).
**Question:** can the march accept a full per-row (p, T, M, θ) initial
line — rotational, non-uniform total state, the real RDE exhaust —
instead of the homentropic two-of-three? GENO already could (its
generic MoC transports (s, h₀) as streamline invariants, Zucrow ch.
17); this session ports that machinery into the certified
cell/record framework, with GENO's `inter_solve_gen` read at source
as the fidelity target and the S20 base tree's carrier format as the
model.

## The port

- **Nodes widen 4 → 6**: (x, y, u, v, s, h₀), invariants stored;
  closure `state_qs(q, s, h₀)` generalizes `state_q` and reduces to
  it EXACTLY at (s₀, h₀) — measured 0.0, not assumed (R-0).
- **Interior cell** z = (x₄, y₄, u₄, v₄, t): two characteristic
  position rows, two (p, θ)-form compatibility rows (Q = √(M²−1)/ρq²,
  S = δ sinθ/(yM cos(θ±α)), midpoint coefficients — the converged
  limit of GENO's predictor-corrector), one streamline-foot row; the
  foot's (s₄, h₀₄) lerped at t on the bracketed chord.
- **Wall and edge are streamlines**: invariants = bottom/top
  start-row constants, appended by the driver; the edge speed is
  q_pa(s_e, h₀_e) via the entropy inversion.
- **Driver** (`plug_march`): additive 6-wide path; the certified
  4-wide path untouched — **every edit gated on the S22 record
  reproducing at rel 0.0**.
- **(p, T, M, θ) is now exactly determined** (three numbers, three
  state dofs): `ivl_from_ptm`, round-trip 2.4e-15 (W-3).

## Declared: why (p, θ) and not the certified (u, v) form

The certified compatibility assumes irrotationality; entropy
gradients make the flow rotational (Crocco) and that form wrong. The
(p, θ) Mach-line form needs no irrotationality and is what the
reference implementation solves. Consequence: at uniform invariants
the two forms are the same continuum equations but DIFFERENT
discretizations — the regression (W-1) is ladder-banded (deviation
must shrink at the schemes' common order), not the swirl precedent's
1e-9 (its Γ→0 limit is the identical equation set; our s→s₀ is not).

## Two port defects found by the oracles, both instructive

1. **The single-chord streamline foot extrapolated.** First build
   lerped the foot on the chord pt1–pt2. The stratified-jet oracle
   refused to converge (error N-independent at ~1e-3); the row-level
   probe showed the mesh SHEARING down by tanμ·dx per column, so at
   fine N the foot lands BELOW the chord — t < 0, extrapolation,
   a systematic transport ramp. GENO does not have this defect: its
   `present(col)` branch searches the whole previous column for the
   exact intersection. Ported as a RECORDED DRIVER DECISION (like
   the wall-foot search): searched once, replayed frozen. Bulk error
   fell 9.5e-4 → 6.5e-6 at N=41.
2. **The rejector world must carry load.** R-2 (corrupted
   compatibility sign) was first posed on the exact parallel jet —
   where the compatibility bracket vanishes identically and the
   corruption is INVISIBLE (the corrupted march converged to the
   same answer). Moved to the plug world: separation 1350×.

## Known topology artifact, measured and reported (not masked)

On a NON-WIDENING jet the driver's one-row-per-column growth crams
former edge rows at the stationary edge while the interior shears
down; a mid-column gap opens (0.509 m on the 12-column jet) and foot
chords spanning it lerp a curved profile across it — an
N-INDEPENDENT error (~5e-4) confined to the crammed band (band
N-stability ×1.01 across rows 21→81). The oracle grades transport
below the column's largest inter-row gap and reports the band. The
plug worlds (widening) do not develop the artifact; a growth rule
aware of non-widening jets is possible future driver work, not
needed for the nozzle program's geometries.

## The record (8/8 PASS, `_rot_march_run_of_record_S24.log`)

    R-0   closure identity at (s0, h0):            0.0
    W-3   (p, T, M) round-trip:                    2.4e-15
    W-2a  linear-stratified jet (EXACT):           3.2e-8 bulk,
          3.9e-8 crammed band, 535 cells cert 0.020
    W-2b  curved stratification, bulk ladder:      2.16e-5 -> 6.47e-6
          -> 7.54e-7  (ratios 3.34, 8.59; band stable x1.01)
    R-1   frozen-foot rejector:                    385x separation
    W-1   vs certified march (uniform invariants): 3.00e-5 -> 8.83e-6
          (ratio 3.4, joint (K,N) refinement)
    R-2   corrupted-compatibility rejector:        1350x separation
    W-4   stratified spike world:                  cert 0.058,
          post-wedge mass 7.9e-3, entropy-flux drift 5.2e-4,
          wedge 3.4e-2 = 2.2x its uniform baseline (S21 property)

## What this opens

- RDE exhausts with hot/cold streaks (per-streamline total state)
  marched directly; the (p, T, M) interface matches GENO's IVL file
  format in content, so the same inlet can drive both codes — the
  cross-code twin on a rotational inlet is the natural next
  validation (open).
- The adjoint: the rot cells run through the same implicit-solver
  machinery (custom_vjp), so the optimizer should differentiate
  through stratified marches — unverified, open.
- The free-jet/wall closures inherit; the swirl seam composes in
  principle (free-vortex + stratification) — unverified, open.
