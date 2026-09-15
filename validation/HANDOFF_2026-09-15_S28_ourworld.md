# HANDOFF — [F3/A1] S28 (2026-09-15)

**READ THIS FIRST when resuming the nozzle optimizer.** Supersedes the
S26 handoff (`HANDOFF_2026-08-27_S26_rao_twin.md`, which stays
authoritative for the Rao-world chain and its traps). Narrative:
`PROGRESS_2026-09-15_S28_ourworld.md`; the rebuild after the deletion:
`PROGRESS_2026-09-09_S27_line_reconstruction.md`.

## 1. State

- Branch `brick2-plug` = `origin/rde-nozzle-program` 6be51b9 (unchanged
  upstream since 2026-08-23; `origin/main` 2d2fdbc) + the line re-authored
  on 2026-09-09 + S28. Push read-only. **Bundle the branch to
  `/data10/falco/RDE/handoff/` at every closure** (`git bundle create
  ../handoff/brick2-plug_<date>.bundle brick2-plug`); the S27 lesson.
- Carriers run on **s2 only** (`/data10/falco/RDE/RDE_Design-rde-nozzle-
  program/.venv-a1/bin/python`; the base interpreter does not exist on
  pcprop4).
- The rebuilt tree holds at the level the SQP consumes: `rao1961_o33`
  7/7 and `rao1961_sqp_return` 6/6 re-run identical to the S26 records
  (logs `_rao1961_twin/rerun_*_2026-09-15.log`).
- **F3 EXIT leg on OUR world, twin mode:** [X-OWTW] 6/6 (gap 1.5e-4),
  [X-OWO3] 4/4 (N2 ~340x), [X-OWSQ] see the S28 log addendum. Baseline
  = GENO `CASES/raoplug_ch4o2/run_val_repro` (rao_val member: theta_E
  −0.02 deg, L 5.926, closes on the axis), OUR gas verified against the
  field, ambient = the member's lip ambient 7.575953e5 Pa (0.9949 PA),
  tip cut 0.01 y_E (x_end 5.6102), cut x0 1.50, K 161.
- Regeneration chain of the artifacts lost on 09-04 (S22 design.json,
  S23 verdict/analysis/design_fine, figures, PDF): driver
  `RDE/handoff/recovery_brick2_2026-09-06/scratch_s2_2026-09-15/
  regen_driver.sh`, log `regen_2026-09-15.log`; the data npz are back
  (`docs/brick2_doc_src/figs/data_rao_walls.npz`, `data_s24_rot.npz`).
  **Not bit-identical to the S22 record (the plug march changed after
  S22); the S23 selftest R-2b will fail on the opt half — declared.**

## 2. Numbers of record (S28)

GENO member (validation mode Me_fixed 2.8020): M_E 2.76032, theta_E
−0.01991 deg, L 5.92567, eps 5.15063, F 1.160476e8 N, mdot 4.232020e4
(target 4.247552e4: −0.37 %, = IVL-vs-target posing; invariant under
NI 101/201/401 and under the C- step /200 /400 /800), lip p_a
7.575953e5. Twin: cert ≤ 0.41 (edge cells), 0 nonfinite, coverage
99.6 % (q) / 97.7 % (theta), floor 3e-6, ladder 1.55e-4 / 1.49e-4 /
2.69e-4. O3.3: J(ref) 6.44510141e7 N (F_in 6.25071e7 + push 1.944e6),
interior AD 1e2..5e3 vs bands 6e5..2.7e6, perturbed 4e4..1.8e6, J(ref) −
J(pert) = +4.4288e4 N.

## 3. Traps (new; the S24/S26 lists still hold)

1. **The member closes on the axis; the plug march has no axis cell.**
   Without the tip cut the last wall station certifies in 4 of 6
   marches and blows up (1e11) in the other two. `OW_YCUT` (0.01 y_E)
   is the declared cut; do not "fix" it by raising K.
2. **GENO's phase-1 fan fails for theta_E >= 0** (NaN in
   solve_T_from_entropy) and the mass+ambient posing falls into a hole
   of the 21-point scan with the binary of record: the documented L
   5.825 member is NOT reproducible. Use validation mode (`Me_fixed`),
   and read theta_E from `raoplug_performance.dat`.
3. **NI does not touch the C- curve; its step is hard-coded**
   (`dx = y_E/200`, Rao_m.f90). The scratch probe build
   (`geno_dxtest`, env `GENO_CMINUS_DIV`) is NOT the committed code.
4. **A mass deficit against p_c A_t/c* is a posing question, not a
   step question** — compare the IVL mass GENO prints (`RaoPlug IVL:
   mfr`) with the target before touching any integrator.
5. **Ambient for an oracle chain = the reference's own ambient**
   (Rao's Eq. (8) in his world; the lip p_a here). The tournament at
   the NOMINAL ambient is a separate posing (open queue 2).
6. The world adapter re-points a rao1961 module's names
   (`ourworld_geno.install`): set `RAO_X0`/`RAO_K` in the environment
   BEFORE importing `rao1961_sqp_return` (its constants are read at
   import).

## 4. Open queue

(1) close the regeneration chain; decide the status of the S22 record
log; (2) tournament-grade A/B at the nominal ambient: a GENO member at
exact PA (GENO protocol) or the declared 0.5 % residual, then
Rao-vs-spline at PSPL_L 5.926 from the GENO cut; (3) Table-1 oracle
bands on our world + a stratified plug instance (F3 EXIT); (4)
findings rows for [X-RAOIS]/[X-RAOWD]; (5) the Italian document
(§vsrao to the rao_val member); (6) the twin's P1 seam on the
2-constraint field (S26 residual).

## 5. Commands

```bash
U=/data10/falco/RDE/RDE_Design
PY=/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python
cd $U            # on s2
$PY validation/ourworld_twin.py                 # ~15 min
$PY validation/ourworld_o33.py                  # ~11 min
$PY validation/ourworld_sqp_return.py           # ~1.5-2 h
# knobs: OW_GENO_RUN, OW_YCUT (0.01), OW_CUTS, OW_K (161); RAO_X0 (1.50),
#        RAO_K (161), RAO_M, RAO_PERT, RAO_SEG, RAO_FREEZE, RAO_SEG_R1
# the Rao-world records, unchanged:
RAO_GENO_RUN=/data10/falco/RDE/codes/GENO/CASES/raoplug_run_legacy \
  $PY validation/rao1961_o33.py
# GENO member (committed 2026-08-09 binary, -O0):
cd /data10/falco/RDE/codes/GENO/CASES/raoplug_ch4o2/run_val_repro && ../../../bin/GENO
```

## 6. Owner decisions

Push access or fork; GENO blessing (RaoPlug N-65/N-66, `raoplug_ch4o2`,
the fan at theta_E >= 0, the C- step knob); the Italian document; the
status of the S22 record vs its regeneration.
