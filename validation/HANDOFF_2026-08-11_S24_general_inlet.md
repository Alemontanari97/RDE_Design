# HANDOFF — [F2/A1] S23+S24 (2026-08-11)

**READ THIS FIRST when resuming the nozzle optimizer.** Supersedes the
S23 handoff (which supersedes S21/S22 and stays authoritative for the
rebase story and GENO). Narratives:
`PROGRESS_2026-08-10_S23_gain_resolve.md`,
`PROGRESS_2026-08-11_S24_general_inlet.md`.

---

## 1. The two results, one paragraph each

**S23 — the gain question is CLOSED.** The free-form spike does NOT
beat the fan streamline: on a six-rung paired ladder to (1921,1601),
incumbent re-optimized at (121,101), model forced to predict its last
rung before seeing it (miss = step/18), the gain limit is
**−0.011 % ± 0.017 %** — zero within band. **The truncated fan
streamline is optimal at L = 2.5 m, θ_E = 0 to within 0.028 %.**
Every coarse-grid gain of S21/S22 was the optimizer fitting the
march's discretization error. Carrier [X-PGRS]
`a1_plug_gain_resolve.py`, verdict in `_plug_gain/verdict.json`,
3/3 PASS at stage `final`.

**S24 — the general (rotational) inlet is ported but NOT clean.** The
march now accepts a full per-row (p, T, M, θ) initial line: nodes
carry per-streamline (s, h₀), interior cells solve Zucrow's (p,θ)
compatibility plus a streamline-foot row, wall/edge ride their own
invariants. 8 of 9 checks pass. **The 9th, W-5, FAILS and that is the
result of record: the port CREATES entropy in 1.6 % of interior
cells** (96 of 1488 nodes outside the inlet's range, worst overshoot
57 % of the physical span, one band of the spike). Carrier [X-RMAR]
`a1_rot_march.py`.

---

## 2. State of the trees

| tree | state |
|---|---|
| `RDE_Design` @ `brick2-plug` | ed84f6e + **12 commits**, tip `ff4e8d6`. Working tree DIRTY (see §6). |
| push | **BLOCKED**: `AlexFalco5` is read-only on `Alemontanari97/RDE_Design`; no fork exists. Fetch clean — upstream has not moved since S20. |
| GENO | HEAD `78f9cb5` + 4 uncommitted `src/lib` files, `-O0` pinning, owner blessing pending (unchanged since S21). |
| venv | `RDE_Design-rde-nozzle-program/.venv-a1` (py 3.11.5, numpy 2.4.6, py-spy added S23) |
| document | `docs/rde_nozzle_A1_brick2_thrust.pdf`, **99 pp**, and now **in ITALIAN** (see §5) |

---

## 3. THE OPEN DEFECT (S24) — read before using the rotational march

**What is wrong.** For ~1.6 % of interior cells the backward
streamline crosses **no segment of the previous column**, so no chord
brackets its foot; the invariant interpolation then extrapolates
(measured foot parameters up to **t = 12**, i.e. twelve chords past
the end of the chord) and manufactures entropy the inlet never
supplied.

**What hid it.** W-4 grades the **mean** entropy per unit mass (drift
5.2e-4, passing) while local values overshoot by half a span. A mean
hides exactly this; the figure did not. The defect was found by
*drawing the entropy field for the document*, not by the suite.

**Three fixes measured and rejected (do not re-try blind):**

1. **Clamp t to [0,1]** — GENO's own rule (`t_foot = max(0, min(1,
   t_foot))`). Stores invariants the cell did not solve with, so the
   node leaves the thermodynamic manifold and poisons its
   neighbours: **certification 3.5e11**. GENO may clamp because its
   predictor-corrector recomputes the foot state each iteration; our
   cells are CERTIFIED against their own residual, so the stored
   state must BE the solved state.
2. **Take the foot on the wall segment** (streamline off a descending
   wall) — physically right for that case, fires on **one** cell and
   breaks it identically; the other 22 are not wall-foot cells.
3. **Iterate the bracket against the SOLVED foot** — KEPT (principled;
   certification 0.058 → 0.047) but cannot close those cells, because
   the containing segment is not in that column at all.

**The remaining fix: a MULTI-COLUMN foot search** — exactly the
generalization `wall_foot_search` already carries (it steps back up
to three columns, `for b in (1, 2, 3)`). Apply the same idea to the
streamline foot: scan columns i-1, i-2, i-3 for the segment that
brackets, and record (b, j) as the decision instead of j alone. The
driver hook is `_scan()` inside `plug_march`'s interior loop; the
schedule key is `sfoot`.

**Declared consequence:** the port is valid for inlets whose
streamlines bracket cleanly (both jet oracles, uniform invariants,
the certified-march regression — all passing) and carries a known
localized defect on the stratified spike. **No design conclusion may
rest on a stratified spike march until W-5 passes.**

---

## 4. Traps (the sharp ones; S21's five still stand)

1. **GENO builds at `-O0` only** (fails its own reference at -O3).
2. **Bands come from ladders (≥3 points) of the computation that
   produced the number**; scatter for non-smooth quantities.
3. **The de-tuning transient**: ANY optimized design's J-ladder is
   non-monotone one rung past its tuning resolution — never
   extrapolate it there; the PAIRED gain ladder is the verdict object
   ([X-PGRS] rule). *An optimizer is part of the instrument.*
4. **trust-constr no-motion wedge**: an initial radius past the
   replayed surface's fold scale (~1e-3) lets the first rejected
   trial poison the BFGS model; x0 is returned with improvement
   available. `run_trsqp` now shrink-retries no-motion (only
   no-motion AT the floor is convergence).
5. **Never `jnp.stack` a large python list** (the mesh record's
   193k-operand stack wedged two marches for 7 h inside one XLA
   compile). It is numpy now. If a march "hangs at 100 % CPU with no
   output", **py-spy it before waiting**.
6. **Settings-tagged artifact names everywhere**; **absolute paths**
   for nohup'd runs (a session restart reset the cwd and killed a
   rung-6 launch silently, costing 2 h).
7. **Rao-vs-spline at L = 2.5 is VOID** (mass+length exhaust Rao's two
   dof; ambient becomes an output). Fair only at full expansion.
8. **March certification MARGIN degrades at K ≥ 481** (one cell,
   round-off-scale, J-nil; rung 6 certifies clean). Reported, not
   binding at rungs ≥ 4 by declaration — open march-contract item.
9. **A rejector world must CARRY LOAD**: the corrupted-compatibility
   rejector is invisible on an exact parallel jet (the bracket
   vanishes identically); it lives on the plug world.

---

## 5. The document (Italian, 99 pp)

The deliverable was **translated into Italian** this session
(babel `italian`, Italian title/abstract/bibliography) and gained
**two new chapters/sections**:

- ch. on **the general inlet** (`ch_general_inlet.tex`, wired after
  `ch_swirl`) with `fig_s24_rotational.pdf`;
- S23 material in `ch_spline.tex`: the **SQP method in full** (what
  SQP is, the decisions/record/replay vocabulary made concrete, the
  segmented walk, all three driver defects), **"the gain, resolved"**
  with `fig_s23_ladder.pdf`, the driver figure `fig_s23_driver.pdf`,
  and a closing **worked example end-to-end** (`fig_worked_example.pdf`).

**Terminology of record** (established by the already-translated
files): *corner* = **spigolo**; *march* = **marcia**; *carrier* kept
as `carrier`; *rejector* = **rigettatore**; *band* = **banda**;
*trust region* = **regione di fiducia**.

**Left undone in the document** (the translation thread was stopped
on owner's order):
- `ch_general_inlet.tex` still describes the port as clean — it must
  be updated with §3's defect and W-5 before the document is quoted;
- `ch_status.tex` ledger row for `a1_rot_march.py` still reads
  **8/8 PASS**; correct to **8/9 (1 aperta)**;
- the S24 figure `fig_s24_rotational.pdf` was regenerated from data
  that shows the overshoot — its caption does not yet say so;
- a terminology sweep (`condizione d'angolo` → `condizione di
  spigolo`) was never run.

---

## 6. Working tree is DIRTY — what is uncommitted

    M docs/brick2_doc_src/ch_appendix.tex      (translation)
    M docs/brick2_doc_src/ch_spline.tex        (translation)
    M docs/brick2_doc_src/make_figures.py      (fig_s24_rotational generator)
    M docs/brick2_doc_src/figs/data_s24_rot.npz, fig_s24_rotational.pdf
    M docs/rde_nozzle_A1_brick2_thrust.pdf     (99 pp build)
    D  validation/_plug_gain/*.npz, _plug_adaptive/cycle_02.npz
       (deliberately UNTRACKED again: the repo's no-npz convention;
        their content lives in verdict.json / design_fine.json)
    ?? validation/.gitignore                   (new, enforces that)

Decide: commit the Italian document as-is (with §5's four corrections
first), or keep it out until the S24 chapter tells the truth.

---

## 7. Numbers of record

    S23 paired gains  +0.30283 +0.19609 +0.10761 +0.05261 +0.02216 +0.00618 %
        diff ratios    0.8290   0.6216   0.5538   0.5244   (march order 0.5)
        gain limit    -0.01144 %   band 0.01688 %   BAR 0.04 %  -> RESOLVED
        fine optimum  J(121) = 1.16037436e+08 (+0.0098 % over S22)
        61-tuned lim  -0.0115 % (BELOW the streamline: the overfit, measured)

    S24 R-0 closure identity 0.0 | W-3 (p,T,M) round-trip 2.4e-15
        W-2a exact jet 3.2e-8 bulk / 3.9e-8 band (535 cells, cert 0.020)
        W-2b bulk ladder 2.16e-5 -> 6.47e-6 -> 7.54e-7 (ratios 3.34, 8.59)
        W-1  vs certified march 3.00e-5 -> 8.83e-6 (ratio 3.4)
        W-4  stratified spike cert 0.047, post-wedge mass 7.9e-3
        W-5  FAIL: 96/1488 nodes out of range, worst 57 % of the span
        R-1 385x | R-2 1350x separation

    Physics: Rao's ideal spike for our world L = 5.825 m, eps 5.148,
    theta_E ~ 0; our 2.5 m = 57 % truncation costing 0.39 % of Isp
    (278.54 s vs 279.62 s, the perfect-expansion ceiling that the
    optimum bell also reaches). Cross-code, unbanded.

---

## 8. Open queue, in priority order

1. **Fix W-5** (multi-column streamline-foot search, §3) — blocks
   every rotational-inlet result.
2. **Correct the document** (§5's four items) before quoting it.
3. **Full-expansion Rao-vs-spline A/B** at L ≈ 5.825 m with mass AND
   ambient matched — the decisive open experiment; needs the spline
   carrier's `L` promoted to an env knob and X_END extended.
4. **L-sweep + suboptimal-θ_i sweep** of the resolved question
   (~2 h/point since the mesh fix): below what length, or how far
   off the optimal inlet split, does shape freedom start to pay?
5. **Cross-code twin on a rotational inlet** — the same (p, T, M)
   line drives GENO (`final_plug=3`, `ivl_file_plug`) and our march.
6. The plug's **~1 % two-route momentum residual** ([X-FMTR]).
7. **O3.3 locus** (fix a priori, stop at the kernel boundary).
8. **Swirl + stratification** composition (unverified).
9. **Adjoint through stratified marches** (should work — same
   implicit-solver machinery — unverified).

**Owner decisions pending:** push access or a fork; GENO blessing;
the `-O0` pinning; whether to commit the Italian document now.

---

## 9. Commands

```bash
U=/data10/falco/RDE/RDE_Design
PY=/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python
cd $U

$PY validation/a1_rot_march.py                     # S24, expect 8/9 (W-5 FAIL)
$PY validation/a1_plug_march.py                    # certified planar 6/6
STAGE=axi $PY validation/a1_plug_march.py          # certified axi 5/5
PGRS_STAGE=final $PY validation/a1_plug_gain_resolve.py   # S23 verdict
$PY tests/test_claims_lint.py                      # 131 entries, PASS
cd $U/docs/brick2_doc_src && bash build.sh         # -> 99 pp PDF
```

**The bit-identity gate** (run after ANY edit to `a1_plug_march.py`):
`/tmp/.../scratchpad/gate_meshfix.py` re-marches the S22 design at
(61,51) and requires `rel 0.0` against `_plug_adaptive/design.json`.
Re-create it from that description if the scratchpad is gone — it is
the single most useful guard in this line.

---

## 10. The lesson worth carrying

S23's: **an optimizer is part of the instrument** — a design tuned at
resolution h carries that instrument's error inside its geometry.

S24's: **a mean can hide a defect that a picture cannot.** Eight
checks passed on a march that was manufacturing entropy; the failure
appeared the moment the field was drawn. When a quantity is
*transported*, check its **bound**, not its average.
