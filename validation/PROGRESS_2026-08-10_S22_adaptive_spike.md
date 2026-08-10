# PROGRESS — [F2/A1] S22: adaptive knots on the spike (2026-08-10)

Session start: resume from `HANDOFF_2026-08-09_S21_brick2plug.md`,
priority items 1+2 of its open list: apply [X-AKNO] to the [X-PSPL]
wall, and try to resolve the free-form spike's gain, which S21's C-6
left NOT ESTABLISHED (band 0.1930 % > gain +0.1302/+0.0820 %).

Tree state at start: as the handoff left it — 82 staged uncommitted on
`brick2-plug`, GENO edits uncommitted, both owner decisions still
pending. Nothing was committed this session either; all S22 changes
are working-tree only, on top of the stage.

## Result in one paragraph

The adaptive-knot machinery TRANSPLANTS CLEANLY and WORKS: the
enriched-class adjoint indicator concentrates 84–85 % of its mass in
the first knot interval, one inserted knot at x = 0.4575 m buys
+0.1921 % thrust at the working resolution — where a UNIFORM 11th knot
buys +0.0002 % (the A-9 control; adaptivity, not dof count, is what
pays). But the headline question stands: on the 3-point resolution
ladder (61,51)→(121,101)→(241,201) the adaptive spike's gain over the
fan streamline falls 0.313 → 0.186 → 0.080 % and the ladder-derived
band (0.426 %) is still LARGER than the gain, so **"the free-form
spike beats the fan streamline" remains NOT ESTABLISHED**, now at a
resolution 16× the S21 cost. The monotone fall of the measured gain
under refinement — for the uniform control too (0.127 → 0.068 →
0.029 %) — is the finding: a large share of any coarse-grid "gain" is
the optimizer fitting the march's discretization error, and the march
converges too slowly on this difference (d12 1.27e-3 → d23 1.07e-3,
ratio 0.84) for an affordable ladder to resolve what remains.

## New carrier: [X-PAKN] `validation/a1_plug_adaptive.py`

[X-AKNO]'s AFEM skeleton applied to the plug: solve → per-interval
indicator → Doerfler(θ=1/2, 0.3/0.7 printed) → insertion (guarded) →
re-optimize with the untouched [X-PSPL] TR-SQP driver → repeat under
declared stopping rules. Marking machinery IMPORTED from
`adaptive_knot_optimize` (doerfler_mark), basis class unchanged.

The INDICATOR differs from the bell's in route, agrees in object:
the plug has the discrete adjoint directly (reverse-AD through the
recorded schedule), so instead of reading f2-drift off the flow, the
class is enriched with a candidate dof at every interval midpoint
(incumbent re-interpolated — EXACT here, deviation ~4e-16, by spline
uniqueness: re-interpolating a cubic spline at a knot superset with
the same end conditions reproduces it; measured, not assumed) and the
gradient AT the candidate dofs is read from one march + one reverse-AD
pass. At a class optimum that component is the multiplier-
compatibility residual of the enriched optimality system — the same
adjoint-weighted object [X-AKNO] constructs, obtained directly.
Indicator mass = |dJ/dy_cand| × interval width.

Checks A-1..A-9 (see the carrier docstring). Production run
(m0=10, K=61, N=51, ≤3 cycles, ≤2 insertions/cycle): **11/12 PASS,
the sole FAIL being A-8, the verdict itself — the honest outcome.**
Artifacts: `validation/_plug_adaptive/{design.json, cycle_*.npz}`.

## Numbers of record (production run, 12211 s)

- class-0 (m=10 uniform, cold start from the streamline):
  J = 1.15739431e+08, cert 0.093, 17 segments. **Reproduces the S21
  recorded optimum 115739431.39643042 bit-for-bit** — see the incident
  below; this replaces the destroyed checkpoint and doubles as the
  session's record check (different walk, same terminal design).
- cycle 1: indicator total 7.93e+06, interval [0.350, 0.565) carries
  the Doerfler-0.5 mass; insert x = 0.4575 → m = 11;
  J → 1.15961756e+08 (**+0.1921 %**, cert 0.121). Adjoint spot checks
  pass (|d| 1.3e-2 / 8.5e-2 vs bands ~25).
- cycle 2: insert x = 0.4037 → m = 12; the driver cannot extract
  ANYTHING (dJ/J = −1.3e-16, single segment, no motion, node-0
  gradient 5.9e+07 yet every trial rejected) → honest stop, best kept
  from cycle 1. Diminishing returns are immediate after one knot.
- A-8 ladder (both designs FIXED, streamline re-interpolated on the
  final knot set; each rung re-poses the start line at its own N):
      (61,51):   +0.31276 %
      (121,101): +0.18631 %
      (241,201): +0.07970 %   ← quoted (d23 ≤ d12, "converging")
      band = K_RICH·d23 = 0.42641 %  → **A-8 FAIL, gain NOT resolved**
- A-9 control (uniform class, same m=11, same driver, same ladder):
  J_opt = 1.15739172e+08 at working resolution — i.e. the uniform
  11th knot buys +0.0002 % where the adaptive one bought +0.1921 %.
  Ladder: +0.127 → +0.068 → +0.029 %, band 0.157 % (also unresolved
  vs the streamline). At the finest rung the adaptive design carries
  +0.0538 % more thrust than the uniform one — same instrument, same
  resolution, difference of two optimized designs — but graded
  against the ladder band this too is inside noise. **A-9 PASS**
  (adaptive does not lose to uniform beyond the band).

Note on locations: C-1's representation ladder put the REPRESENTATION
error peak at x ≈ 0.56–0.61 m; the thrust-gradient indicator put its
mass at x ≈ 0.40–0.46 m, further left, where the 2πy thrust weight is
largest. Different functionals peak in different places; the indicator
is goal-driven and its knot is the one that paid.

## Incident of record: the S21 checkpoint was destroyed by its own carrier

A quick verification run of `a1_plug_spline_opt.py` at (M=6, K=81,
N=61, ITERS=4) — run to confirm the world reproduces before building
on it — OVERWROTE `validation/_plug_spline/spline_opt.npz`, because
that carrier saved its checkpoint UNCONDITIONALLY to a fixed name at
whatever settings it ran. The S21 10-knot design vector was never
git-tracked and is unrecoverable as a file. Bounded damage: every
NUMBER of record survives in the S21 log/registry, and the cold-start
class-0 optimization reproduced the recorded optimum J bit-for-bit,
re-deriving the design vector (now preserved in
`_plug_adaptive/design.json` and `cycle_01.npz`).

FIX AT THE SOURCE, both carriers: [X-PSPL] now saves to a
settings-tagged name (`spline_opt_m%d_k%d_n%d.npz`), [X-PAKN] loads
the tagged name first with a class-match guard either way; the
overwriting artifact was renamed to its truthful tag
(`spline_opt_m6_k81_n61.npz`). Lesson, same family as S21's: the
INSTRUMENT (a checkpoint namespace shared across settings) destroyed
the record, not the object. Verification runs must not be able to
write where production records live.

## Also this session

- **Registry drift fixed**: the [X-PSPL] entry still asserted the
  RETRACTED "+0.0908 % vs band 0.0094 %" headline (statement) and its
  falsifier list stopped at C-5 — S21's step-11 correction reached
  ch_spline.tex but not the registry. Statement rewritten to the C-6
  finding, falsifier extended with C-6; claims lint PASS.
- INDEX row for S21 likewise carried the retracted gain; corrected
  with a bracketed note (audit layer: correction appended, row not
  rewritten).
- Default-settings observation, recorded not chased: at (M=6, K=81,
  N=61) trust-constr takes NO step from the raw streamline in either
  direction ("no motion", both the maximizer and the R-1 minimizer),
  so C-6/R-1 degenerate at those settings; the S21 7/8 record was at
  the production settings (M=10, K=61, N=51), where the driver walks.
  Not a regression (no recorded number at defaults exists); worth an
  eye if defaults are ever used for a record.

## What is open, updated priority order

1. **Resolving the gain now requires a better INSTRUMENT, not more
   knots**: the march's convergence on the design-difference is too
   slow (ratio ~0.84 rung-to-rung). Candidates, in order: optimize AT
   (121,101) so the incumbent is not tuned to the coarse instrument
   (cost: TR-SQP segments at 6× march cost — feasible, the S22 ladder
   already paid 2×4300 s at rung 3); Richardson-extrapolate the
   PAIRED difference across the existing 3-rung ladder (both ladders
   converge monotonically, d-ratios 0.84/0.66 — an extrapolated gain
   with its own derived band may resolve either sign); or the exact
   thrust functional route ([X-FMTR] two-route reading on the finest
   field, though its ~1 % field residual currently dwarfs the
   effect).
2. The rest of the S21 open list stands unchanged: O3.3 locus fixed a
   priori; the plug's ~1 % momentum residual; Rao comparison at full
   expansion (L = 5.825 m); config_compare closures onto a1_flux_meter;
   CFD P1 (SU2 not installed).

**Owner decisions pending (unchanged + one new):** commit the 81/82
staged files; bless the GENO edits; the -O0 pinning; and now also
whether `a1_plug_adaptive.py` + the S22 working-tree edits
(claims_registry, INDEX, the two carrier fixes) join the same commit
or a follow-up one.

Steps 1-6, 2026-08-10, single session, no usage-wall events.
