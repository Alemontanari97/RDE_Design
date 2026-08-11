# HANDOFF — [F2/A1] S23: the gain question is CLOSED (2026-08-11)

**READ THIS FIRST when resuming the nozzle optimizer.** Supersedes the
S22 handoff. Full narrative: `PROGRESS_2026-08-10_S23_gain_resolve.md`.

## 1. The result, one paragraph

**The free-form spike does NOT beat the fan streamline, and this is
now ESTABLISHED, not merely unresolved:** on a six-rung paired ladder
(61,51)→(1921,1601), with the incumbent re-optimized at (121,101) and
the extrapolation model forced to predict its last rung before seeing
it (miss = step/18), the gain limit is **−0.011% ± 0.017%** — zero
within band. **The truncated streamline is optimal at L = 2.5 m,
θ_E = 0 to within 0.028%.** Every gain S21/S22 measured was the
optimizer fitting the march's discretization error. Carrier [X-PGRS]
`a1_plug_gain_resolve.py`, verdict rule declared before the decisive
rung; 3/3 PASS at stage final; `_plug_gain/verdict.json`.

## 2. State of the trees

| tree | state |
|---|---|
| `RDE_Design` @ `brick2-plug` | 4 commits on ed84f6e: a751db2 (S21) / 82282f3 (S22) / 071fe49, 6256975 (doc+figure). S23 set NOT yet committed at handoff-write time (see the commit that carries this file). |
| push | **BLOCKED**: AlexFalco5 is read-only on Alemontanari97/RDE_Design; no fork exists. Fetch clean — upstream still at ed84f6e. |
| GENO | HEAD 78f9cb5 + 4 src/lib files modified, uncommitted (owner blessing pending, unchanged since S21). |
| venv | `RDE_Design-rde-nozzle-program/.venv-a1` (py 3.11.5, numpy 2.4.6, + py-spy added S23) |

## 3. Traps (new ones first; S21's five still stand)

1. **The de-tuning transient.** ANY optimized design's J-ladder is
   non-monotone one rung past its tuning resolution. Never extrapolate
   an optimized design's own ladder near its tuning rung; the PAIRED
   gain ladder becomes single-mode once the design leaves that window
   and is the verdict object of record ([X-PGRS] rule).
2. **The no-motion wedge.** scipy trust-constr, given an initial
   radius beyond the replayed surface's fold scale (~1e-3 in design
   units), lets its first rejected trial poison the BFGS model and
   returns the start point unchanged with f-evals frozen — while
   improvement is measurably available. `run_trsqp` now shrink-retries
   no-motion on the same record (only no-motion at the radius floor is
   convergence). Verified bit-identical on all unwedged paths.
3. **Never `jnp.stack` a large python list of arrays.** The mesh
   record's stack (~193k operands at (481,401)) wedged two marches for
   7 h inside one XLA compile. It is numpy now (concrete record-mode
   artifact; every consumer converts anyway). If a march at a new
   resolution "hangs at 100% CPU with no output", py-spy it before
   waiting: the march may be done and the stack compiling.
4. **March certification MARGIN degrades at high K** (one wall/edge
   cell at 2.7–4× a round-off-scale bound at rungs 4–5; rung 6 clean
   on both designs; J-effect ~1e-13 — nil). Reported, not binding, at
   rungs ≥ 4 by declaration. The K-trend is an open march-contract
   item: find the cell mechanism before trusting cert as a gate at
   K ≥ 481.
5. **Launch long runs with ABSOLUTE paths** (a session restart reset
   the cwd and a rung-6 launch died silently on a relative path,
   costing 2 h) — and settings-tagged artifact names everywhere (the
   S22 design.json was clobbered by a smoke run and restored from
   git; both carriers now tag).

## 4. Numbers of record

    paired gains   +0.30283  +0.19609  +0.10761  +0.05261  +0.02216  +0.00618 %
    diff ratios     0.8290    0.6216    0.5538    0.5244    (march order 0.5)
    J_inc limit     1.16022775e+08  (windows shift 1.9e3; r = 0.500 exactly)
    gain limit      −0.01144 %   band 0.01688 %   BAR 0.04 %   → RESOLVED
    fine optimum    J(121) = 1.16037436e+08 (+0.0098% over S22 at (121,101))
    61-tuned limit  −0.0115 % (below the streamline: the overfit, measured)

Scope: at the OPTIMIZED inlet split (θ_E = 0) and L = 2.5 m (57%
truncation of the ideal). The inlet split is the design variable that
pays (percent scale); shape refinement after it is bounded by 0.028%.

## 5. What is open, in priority order

1. **Full-expansion Rao-vs-spline A/B** (S21 item 5) — now THE open
   experiment: both machines at L ≈ 5.825 m, mass AND ambient matched
   (`a1_config_compare` reaches X_END = 6.0; the spline carrier is
   pinned to L = 2.5 — needs the L knob promoted to env).
2. **L-sweep of the resolved question**: below what length does shape
   freedom start to pay? The whole optimize+ladder cycle costs ~2 h
   per length since the mesh fix. Also worth pairing with a
   deliberately suboptimal inlet split (the near-zero result is
   conditional on θ_E = 0).
3. **The ~1% two-route momentum residual** ([X-FMTR]) — unchanged.
4. **O3.3 locus** (a priori, stop at the kernel boundary) — unchanged.
5. **March cert-margin K-trend** (trap 4) — new.
6. CFD track: P1 still blocked (SU2 absent); P0 done.

**Owner decisions pending:** push (needs write access or a fork);
GENO blessing; the `-O0` pinning (all unchanged).

## 6. Commands

```bash
U=/data10/falco/RDE/RDE_Design
PY=/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python
cd $U

$PY validation/a1_plug_gain_resolve.py            # selftest + analysis
PGRS_STAGE=fineopt $PY validation/a1_plug_gain_resolve.py
PGRS_STAGE=rung4 PGRS_RUNG=5 PGRS_DESIGN=inc $PY validation/a1_plug_gain_resolve.py
PGRS_STAGE=final $PY validation/a1_plug_gain_resolve.py   # the verdict
$PY tests/test_claims_lint.py                     # 130 entries
cd $U/docs/brick2_doc_src && bash build.sh        # PDF (85 pp)
```

Artifacts: `validation/_plug_gain/` (fineopt.npz, rung{4,5,6}_{inc,fine}.npz,
verdict.json, analysis.json); ladders re-derivable from the carrier at
~25 min for rungs 1–4, ~3 h for 5–6.

## 7. The lesson worth carrying

S21's lesson ("the instrument, not the object") now has a sharper
corollary: **an optimizer is part of the instrument.** A design tuned
at resolution h carries the instrument's error inside its geometry,
and measurements of that design near h inherit it. The cure that
worked: pair the designs, ladder the difference, make the model
predict a rung it has not seen, and let the band come from the
extrapolation's own stability — then a three-session claim closes in
one day.
