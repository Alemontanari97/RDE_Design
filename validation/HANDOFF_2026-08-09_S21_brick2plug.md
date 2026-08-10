# HANDOFF — [F2/A1] Brick-2 plug line, S21 (2026-08-09)

**READ THIS FIRST when resuming the nozzle optimizer.** It is the
short version of `PROGRESS_2026-08-09_S21_brick2plug.md`, which has the
full narrative. Everything below was verified in-session; where it was
not, it says so.

---

## 1. Where things stand in one paragraph

The off-branch Brick-2 plug line was rebased onto upstream S20
(`ed84f6e`) and the spike was given a shape basis. **81 files are
STAGED AND UNCOMMITTED** on branch `brick2-plug` in
`/data10/falco/RDE/RDE_Design`. The document is 82 pp. Two new
carriers exist ([X-PSPL] free-form spike, [X-FMTR] field meter) and
three defects were fixed in GENO. The session's most important result
is **negative**: the free-form spike's thrust gain is NOT resolved by
its own discretization, so the headline claim it was built to make is
not yet established.

---

## 2. State of the trees

| tree | state |
|---|---|
| `/data10/falco/RDE/RDE_Design` | branch `brick2-plug` off `ed84f6e`; **81 staged, 0 unstaged, 0 untracked**; NOT committed |
| `/data10/falco/RDE/RDE_Design-rde-nozzle-program` | the OLD non-git working tree; superseded, kept only for A/B against pre-rebase behaviour |
| `/data10/falco/RDE/codes/GENO` | HEAD `78f9cb5`; **4 files modified in `src/lib`, uncommitted** (referee code — needs owner blessing) |
| venv | `/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python` (py 3.11.5, numpy 2.4.6) — used from the NEW tree by absolute path |

Commit message drafted at
`scratchpad/COMMIT_MSG.txt`; GENO patch at `scratchpad/geno_s21_edits/`.

---

## 3. Five traps — read before touching anything

1. **GENO must be built at `-O0`.** Its binary was compiled with
   **gfortran 7 + MKL 2024.1**, neither now installed. Rebuilt with
   gfortran 12 at the project's `-O3`, it **fails GENO's own reference
   case**; at `-O0` the same source reproduces it exactly. The build
   cache also had to be repointed to MKL 2023.1.0 and gcc-12 libgomp.
   **Do not trust an optimized GENO build** until the underlying UB is
   found or gfortran 7 is restored. This was proven independent of our
   edits by removing them entirely and reproducing the failure.

2. **Never grade a result with a band derived elsewhere.** This is the
   session's recurring error, hit four times, and it produced the one
   claim that had to be retracted. Bands come from a **ladder (≥3
   points)** of the computation that produced the number; where the
   quantity is non-smooth, the ladder's **scatter** is the band, not a
   two-point truncation estimate.

3. **A constraint and its verdict must be the same FUNCTIONAL**, not
   merely the same quantity. `a1_inlet_angle_opt` sized its mass with a
   trapezoid-of-product and graded it with a product-of-midpoint-means;
   the 7e-5 residue was pure instrument difference and looked physical
   for several sessions. Fixed → residue 1e-15..3e-10, and a supposed
   "marching limit" (cert 6.5) dissolved with it.

4. **The march's free-boundary polyline starts at x ≈ 2.69**, not at
   the start line — free-jet points only appear once the marching front
   reaches the boundary. `np.interp` clamps silently outside its range,
   which is how the field meter first reported a 6–7% mass excess. Any
   meter must **refuse to extrapolate**. (A mesh upper-envelope is NOT
   a valid substitute: a vertical cut through a characteristics mesh is
   sparse, so per-station max-y under-reports the jet radius by up to
   96%.)

5. **The Rao-vs-spline A/B at L = 2.5 m is VOID.** Rao's family has two
   degrees of freedom; fixing mass and length consumes both, so ambient
   becomes an OUTPUT (1.7e6 Pa vs our 7.6e5). GENO's wall barely tapers
   there (1.630 → 1.548 → 1.636 m, ε = 2.47) while ours falls to 0.833.
   Different machines — comparing their thrusts measures the expansion
   mismatch, not the two methods.

---

## 4. Results of record

**The rebase is numerically free.** Upstream's S18 while-Newton vs our
fixed-trip loop: ṁ **bit-identical**, J₀/Mₑ/qₑ/pₑ/y_lip agree to
1e-15..1e-13 across four area ratios. No recorded number moved. 13
suites clean; `a1_config_compare` 7/10 and (then) `a1_inlet_angle_opt`
4/6 were verified **identical pre-rebase**, so not regressions.

**[X-PSPL] free-form spike, 7/8.** Design vector = spike radius at m
frozen knots; wall = the **bell engine's own** clamped-left cubic
spline (imported from [X-TOCV], so bell and plug carry equal shape
freedom and [X-AKNO] applies unchanged); mass and length by
construction; reverse-AD adjoint through the recorded schedule;
segmented TR-SQP with the certification gate (load-bearing — reverted a
worst-2.318 record).

**C-6 FAILS and that is the headline.** Band derived at the carrier's
own resolution:

    gain at (K,N)          +0.1302 %
    gain at (2K-1, 2N-1)   +0.0820 %
    band this supports      0.1930 %   <-- LARGER THAN THE GAIN

So **it is not established that the free-form spike beats the fan
streamline.** The earlier "+0.0908%, ten times the band" used step 13's
band from a different computation. The machinery itself remains
verified (adjoint vs ladder, basis density 28× over 6→48 knots, mass to
5e-12, rejector).

**[X-FMTR] field meter, 3/4** — CFD gate P0. Two independent routes
(wall pressure integral vs momentum flux through a cut), solver-
agnostic. Cut-independence 0.40%; reproduces the record to 1.0e-04;
gauge-mismatch rejector separates 5.8×. **OPEN:** the two routes differ
by **0.99%** against a 0.09% band and the difference survives
refinement (0.99 → 0.97) — so ~1% is a property of the FIELD. This
sharpens the old 1.49% last-column figure: inflated by its meter, but
not wholly caused by it.

**Rao's answer for our world** (only computable after the step-cap
fix): mass-matched and expanded to our ambient →
**L = 5.825 m, ε = 5.148, θ_E = 0.02504°**, p_a 7.619e5 (0.06% from
target). Our step-15 blind sweep, from the divergence argument alone,
put the optimum at θ_E = 0; our sweep resolves ±2°, so this is a
**consistency check between independent routes**, not a precision
match. Consequence: our 2.5 m design is a **57% truncation** of the
ideal spike.

**GENO fixes (3), each gated on the reference case reproducing
EXACTLY** (θ_E −8.25001, L 0.93873, deficit −0.0001%, exit 3):
(i) non-finite guard — increments tested before accumulating, distinct
exit reason 4, so a non-closing curve no longer returns NaN;
(ii) two-constraint validity — a length root on a corner-terminated
branch missing mass by 63.6% is no longer accepted;
(iii) step cap 500 → 5000 — it was a budget, not a physics limit.
The repaired direct path and the outer-Mach workaround then agree
independently (θ_E 7.590 vs 7.604; M_E 2.63429 vs 2.63390).

---

## 5. What is open, in priority order

1. **Adaptive knots on the spike** ([X-AKNO] applied). *The* next step:
   C-6 says shape freedom must be bought where the contour bends, and
   the representation ladder locates that at x ≈ 0.56–0.61 m. Our wall
   already uses [X-AKNO]'s basis, so it should apply with little
   adaptation. **Not started.**
2. **Resolve the [X-PSPL] gain**: a resolution where the band falls
   below the effect. Pairs with (1).
3. **O3.3 locus** — still selected by minimising the f₂ spread it then
   reports (circular). Fix a priori. *Partial obstacle*: the S19
   correction says stop the surface at the kernel boundary, and the
   kernel boundary's location in GENO's grid indexing was never
   identified — an hour of investigation. The honest half (fix the
   locus a priori, report the spread wherever it lands) needs none of
   that. **Not started.**
4. **The plug's ~1% momentum residual** — measured on a good surface,
   survives refinement. The branch's outstanding physical question.
5. **Rao comparison at full expansion**: both at L = 5.825 m with mass
   AND ambient matched. `a1_config_compare` reaches X_END = 6.0 so the
   domain exists; `a1_plug_spline_opt` is pinned to L = 2.5.
6. **Re-run the configuration comparison** with both sides free-form —
   only after (2), else the margin inherits an unresolved gain.
7. CFD track: P1 blocked (SU2 not installed; meson/ninja/swig missing).
   P0 is done — that is [X-FMTR].

**Owner decisions pending:** commit the 81 staged files (note: upstream
tracks zero PDFs and zero `.npz`, but 3.4 MB of figure binaries + the
deliverable PDF are staged so the document builds from a clone);
commit/bless the GENO changes; the `-O0` pinning.

---

## 6. Commands

```bash
U=/data10/falco/RDE/RDE_Design
PY=/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python
cd $U

$PY validation/a1_plug_spline_opt.py     # the free-form spike
PSPL_M=10 PSPL_K=61 PSPL_N=51 PSPL_ITERS=30 $PY validation/a1_plug_spline_opt.py
$PY validation/a1_field_meter.py         # two-route meter (CFD P0)
$PY validation/a1_inlet_angle_opt.py     # 6/6 after the instrument fix
STAGE=stationarity $PY validation/a1_o33_toc.py   # the second stage
$PY tests/test_claims_lint.py            # registry lint (128 entries)
$PY tests/run_all.py --fast              # 13/15; the 2 fails are missing sympy

cd $U/docs/brick2_doc_src && bash build.sh   # -> docs/rde_nozzle_A1_brick2_thrust.pdf

# GENO (must stay -O0)
cd /data10/falco/RDE/codes/GENO/build && make GENO -j4
cd <case-dir> && /data10/falco/RDE/codes/GENO/bin/GENO
```

GENO cases used this session are preserved under `scratchpad/`:
`rao_ref` (GENO's own reference — the gate), `rao_val` (validation
mode, our world), `rao_run` (bisection on length), `rao_pa` (mass +
ambient). Two carriers need data they do not generate:
`a1_geno_plug_twin` reads `validation/_geno_twin/`, and `a1_o33_toc`
reads a GENO-designed contour.

---

## 7. The one lesson worth carrying

Four times this session a defect was blamed on the object being
measured — the basis, the flow, the adjoint, our GENO patch — and four
times the **instrument** was at fault. Two points can measure a
difference but never a rate, nor the reliability of the instrument that
produced them. Before fixing, reproduce the failure with the suspect
change **removed**; after fixing, require the untouched reference case
to come back **exact**, not merely passing.
