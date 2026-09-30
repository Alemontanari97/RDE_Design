# Session log 2026-09-30 — F2.ENGINE, session 3 of 6 (census R45): OPEN, orders 1-3 done, PILOT-WF running

Plain rules for this log: short sentences, one fact per line, physics before method.

## Opening (R2, R8)
- Phase F2, step F2.ENGINE, critical path. Prompt: `ADVISORY_F2ENGINE_prompt_2026-09-30.md`.
- Consumer: whoever continues this session, and the owner.
- Exit criteria: the prompt's E1-E5. Orchestration: 0 subagents. Decisive runs used so far: about 10 minutes.
- Check of the prompt against the plan: its order 1 is confirmed as the right first act (see the table: most of
  the march is already there). One addition found while doing it: 39 registered checks of the plug line cannot be
  seen by the age check (below).

## Order 1 — what of the general engine already exists (re-run today on the reunited tree where a script exists)
| what F2 must deliver | today | evidence |
|---|---|---|
| A march for layered inflow: every streamline keeps its own entropy and total enthalpy | EXISTS, passes today | `a1_rot_march.py` 9/9: an exact layered jet is held to round-off; it agrees with the uniform-flow march within a band that shrinks with the mesh; it creates no entropy |
| Gas model given speed, entropy and total enthalpy | EXISTS, passes today | same script, check R-0: reduces exactly to the uniform model |
| Gradient of the thrust exact on the layered march | EXISTS, passes today | `o31_rot.py` PASS: gradient test through the layered plug march agrees to 9e-8 against a floor of 3e-6; a corrupted gradient is rejected |
| Agreement with GENO on a layered case, plus independent balances | PARTIAL | the march was ported from GENO's and conserves mass and entropy (check W-4); no run against GENO's layered solver is on file |
| Checks on the input data (is the RDE outflow given as input consistent: jump relations, entropy, balances, uncertainty) | MISSING | no auditor in the code; ten open findings wait for it |
| Monitor that the input is ONE wave turning rigidly and repeating itself (the record calls it the flatness monitor: in the wave's frame the pattern must not change in time), with a derived limit and a loud reject when two modes or a change in the number of waves are present | MISSING | finding problem-statement:flatness-monitor-unarmed (critical). CORRECTION 2026-09-30 evening: the first version of this row called it a check on the total temperature; that was a misreading of the name |
| Layers separated by a jump (contact surfaces): a declared treatment | PARTIAL | the march carries smooth layers and bounds them (check W-5); the statement and the wave-crossing check across a jump are not written |
| Is there, per phase, a supersonic surface at the RDE exit where the data can be taken (choking) | PARTIAL | measured on one source: the Q2D THOR exit is supersonic in every cell (axial Mach 1.44 to 1.84); the general rule and its monitor are not written |
| The check that stops a design when waves of one family cross, for layered flow, with a test that it can fire | MISSING for layered flow | it exists for uniform flow (bell: `margin_governor.py`; plug: the no-fold class); not extended |
| The cell check stable against solver variants | MISSING | order 2 of this session; finding certification:pass-line-tighter-than-machine-arithmetic-near-the-axis |
| Swirl | out of the design by decision; the free-vortex cells EXIST and pass today | `a1_swirl_march.py` 9/9; the symbolic swirl kernel cannot run here (symbolic package absent) |
| Free jet at the lip, separation closure, gas tables per phase, fast replay, two-wall optimiser | EXIST (plug line), pass today | `a1_lipjet.py` 9/9, `a1_rde_tournament.py` 9/9 |
| Reduction error of the frozen pictures (F2.M-RED) | NOT STARTED | PILOT-WF defined, not launched (3-D launch = owner) |
| Paired CFD demonstration (F2.CFD-2) | PARTLY IN HAND | the per-phase CFD referee on the cluster with certified convergence exists (S41-S42); the paired demonstration as the plan defines it is not done |
| Methods frozen and the theory half of the paper | NOT DONE | - |

Reading: the core of the engine (layered march and its gradient) is built and passes. What separates F2 from its
exit is around it: the checks on the input data, the wave-crossing check for layered flow, the cell check, the
measure of the frozen-picture error, the paired demonstration, the freeze.

## Found while doing it: 39 checks whose age the lint cannot see
The rule of the plan line says a check is old when a script it imports changed after its last pass. The lint reads
the age from the file named in the `doc` field. For 39 checks of the plug line that field names a log or a text,
not the script, so changes to their scripts are invisible and the lint is green for them whatever happened.
Three of them re-run today and re-stamped: X-RMAR, X-O31R, X-LJET. The other 36 are owed (list in the finding
registry:age-check-blind-for-checks-documented-by-a-text).

## Order 2 — the cell check judged against the arithmetic (E2)
What was wrong. The check says a cell is solved when one more Newton step moves it by less than 100 rounding units
of its own scale. Near the axis at the end of the bell contour the residual is a difference of large numbers read
from tables; the last step cannot go below the noise of that difference, and there the noise is above the line.
The same design read 1.20 / 0.46 / 2.07 with three solver variants (damped Newton; plain steps continued;
polished) where pass is below 1: the verdict was a coin toss on the arithmetic, not a judgement on the flow.
What is done (`A1_CERT_KAPPA=1`, opt-in; unset = the check of record, bitwise; row in the flag registry; M0
block NTF-6). The check now measures the cell's own floor: two more plain Newton steps from the returned root.
Where they no longer shrink, that is the floor, and the line is 100 times it. Where they still shrink by orders
(a cell not yet solved) the line of record applies. The line never goes below the record's and never above a
relative correction of 2e-10. Why 100 and not less: two samples of a noisy floor sit several times below its
peaks (measured 7x on the S22 campaign), so a smaller factor gives the verdict back to chance.
Demonstrations (logs `RDE/handoff/plug_2026-09-29/carriers_2026-09-30/final_*.log`):
- the S22 base now reads 0.115 / 0.141 / 0.166 with the three solver variants (`certdiag_locus.py`): stable;
- the five designs the S22 campaign rejected certify in all three variants (their rejection was the arithmetic);
- a solver starved to 3 iterations is still rejected, at 1239 (`certdiag_kat.py` KAT-1): a guard on convergence;
- a record with a non-finite cell is still rejected (the campaign below, segment 3);
- the default path is untouched: `a1_ideal_march_jax.py` PASS bitwise, `a1_rde_tournament.py` gates 9/9.
Not done: the population study the M0 duty asks for (quantiles of the floor across production marches); one
design family measured. The mesh-error criterion the S-REVIEW asked for is not this: this check judges the cell
against its own arithmetic. Judging it against the mesh error needs the two-level march at every cell; left to
the population study.

## Order 3 — the S22 bell campaign re-run with the new check (E3)
Command: `A1_CERT_KAPPA=1 A1_NEWTON_RESCUE=1 adaptive_knot_optimize.py` (log `final_AKNO_newcheck.log`).
- Cycle 1 CONVERGED in class for the first time on file: optimality residual 6.5e4 -> 0.78 (target 0.96), margin
  audit and gradient spot check pass. Every earlier run of this campaign ended "limited by certification".
- The pre-declared kill test [D1] is therefore TESTED, and it FAILS: the enriched design's corner mismatch is
  6.68e-2 against the 8-knot baseline 6.63e-2 (worse by 5e-4, above the stop tolerance 3e-4). Thrust
  2.7775716e7 N (the baseline 2.7777077e7 at segment 0: the walk did not gain). Reading: adding wall freedom
  where the sensitivity is concentrated does not bring the exit lip closer to the optimality condition; the
  design class was not what held the corner off.
- The script printed "[D1] UNTESTABLE: no cycle converged" for this case: wrong wording (it treated a converged
  cycle that did not beat the baseline as no converged cycle). Fixed today in `adaptive_knot_optimize.py`: the
  test is reported as tested and failed with both numbers. X-AKNO stays declared failing (`fail=`), now for the
  right reason.
- The record file `validation/s20_adaptive_design.json` was overwritten by the run and restored from git; the
  run's copy is in `carriers_2026-09-30/`.

## The 33 owed checks (finding registry:age-check-blind-for-checks-documented-by-a-text)
Every script re-run with its DEFAULT protocol (three lanes, `run_owed.sh`), then those whose pass of record used
other settings re-run with the settings of record (`run_record.sh`, `run_record2.sh`). Read against the registry
rows, not against "PASS" alone: four rows are negative results whose run of record fails by construction.
| outcome | rows |
|---|---|
| pass today, default protocol | X-ANKR 4/4, X-PGRS 5/5, X-PLUG 6/6, X-AFAN 8/8, X-FRMR 4/4, X-PSPL 8/8, X-TKRN 7/7, X-TWMU + X-MGDL 5/5, X-BPRS 10/10, X-OWO3, X-OWNM, X-OWTW, X-RAOPO, X-PMRG 11/11, X-TWOP 6/6, X-RDET 2/2 |
| the record reproduced (rows that record a failing gate) | X-FMTR 2/3 (P0-1: the two routes differ by 1 percent, the row's own statement), X-CHTW 8/9 (T-4b mass along the march, open since S31), X-HMPH 4/6 (R-1/R-3 fail by construction, declared in the row), X-RAOWD (its falsifier FIRED is the result) |
| pass with the settings of record | X-RAOO3 7/7 (`RAO_GENO_RUN=GENO/CASES/raoplug_run_legacy`), X-TPOS gates 4/4 (`HMPH_CASE=opt HMPH_ZCUT=0.12 ANK_ETA=8 HMPH_K=160 HMPH_N=41`; the default posing raises "tri column rows not ordered" at every commit back to the row's own, so the default was never the record), X-IVLT (through X-TPOS) |
| pending at the time of writing | X-RAOSQ, X-RAOHM, X-PTRN (`PSPL_FAN=axi PTRN_K=81 PTRN_N=41`), X-OWAB, X-OWSQ + X-OWS3, X-RAOFN, X-RAOTW, X-PAKN (4-hour cap; the 1-hour cap ran out at cycle 1) |
The default runs of the scripts rewrite their cache files under `validation/_*/` (derive.json, npz): restored from
git before the commit; the caches of record are the committed ones.

## A mistake of the cleaning (2026-09-30 morning), repaired
`validation/_rde_tournament/stech/class_nofold_2026-09-28.json` was deleted as uncited: my check looked only at
tracked files, and the file was cited by the contest scripts outside the repo. Rebuilt from
`class_2026-09-27.json` with the recorded floor m_ref/64 (rho 1233.07, m_ref 0.47021): thrust and certificate
identical to the record, class margin 0.605218 against the logged 0.605229 (the exact original settings are
lost at the fifth digit). Committed now as reconstructed. No other deleted file is referenced by a script
outside the repo (scan of `RDE/handoff` and `THOR_GPU/NOZZLE_2026-09-27`).

### Order 4(d) — result (carrier `validation/single_wave_monitor.py`, row X-SWAV; logs `carriers_2026-09-30/swav_*.log`)
Amendment to the gates above, declared when the first form failed its own rejector: W-2/W-3 measured on the raw
samples could not see a 30 percent counter-turning wave (R-1 did not fire), because the detonation peak is a
spike a few samples wide and a measure on the samples measures where the spike falls. The gates were re-formed
on the quantity the design consumes, the 12 SECTOR MEANS of the pattern, with two derived lines: the SHIFT of
their average (what moves the cycle thrust, which follows the phases' pressure) below PILOT-WF's line, 0.17
percent; the REDISTRIBUTION among sectors (RMS) below the typical step between adjacent sector means of the
record (below it the 12-sector description does not tell two patterns apart; the smallest step is not used, two
sectors can be equal by chance: 0.0008 on the wall probes). All three rejectors fire on both probe groups.
Result on the record (piastra probes, x 23.4 mm; the wall probes at 18.8 mm agree):
- W-1 PASS: one wave, 4246 Hz (period 235.53 us), the delays between probes exactly the angle over the wave
  speed (47.1 and 94.2 us for 72 and 144 degrees), the same count in both halves of the window.
- W-2 FAIL: probe to probe (72 degrees apart, hence different turns) the sector means differ by 0.9 percent in
  average and 2.8 percent RMS.
- W-3 FAIL: turn to turn the sector means change by 2.2 percent in average and 6.8 percent RMS (8 turns).
Reading (physics). The THOR_CAv3 outflow is one wave turning rigidly in PHASE, but its STRENGTH wanders from
turn to turn by about 2 percent of the mean pressure (the manifold-chamber coupling of the Q2D limit cycle;
memory of the Q2D work: manifold oscillation). The 12 phases of record come from ONE snapshot (t 15.5 ms): they
carry that wander as an uncertainty of about 2 percent on the cycle's mean level, larger than the +1.65 percent
margin of the rehearsal (S42) and than any line of the decisive comparison. Consequence, proposed to the owner:
the family mu of the decisive comparison must be built from MANY turns (the phase states averaged over turns
at the same wave phase), not from one snapshot; the monitor's W-3 gives the number of turns needed (the shift
falls as one over the square root of the turns if the wander is not drifting). PILOT-WF itself is unaffected:
its two arms consume the same 12 frozen states.
X-SWAV is declared FAILING (`fail=2026-09-30`) owned by the finding
data-contract:thor-cav3-wave-strength-wanders-two-percent-turn-to-turn. Data of record committed:
`validation/_single_wave/thor_cav3_probes_last3ms.npz` (1.2 MB).

## PILOT-WF — declared BEFORE any result is read (R8), 2026-09-30 18:55
Launched on the owner's order "chiudiamo F2" (my reading: it covers the 3-D launch the prompt left to the owner).
Question: does the thrust averaged over 12 frozen phases equal the thrust of the real rotating flow?
- Case: Rao's plug of S42 (internal nozzle -10 degrees, 87 mm), ambient 0.05 bar, frozen chemistry, Euler.
- Run A (the rotating flow): 3-D, 814 thousand cells (the 2-D referee grid turned around the axis, 2-degree cells),
  solved in the frame that turns with the wave (4246 Hz, toward decreasing angle). In that frame the inlet pattern
  stands still: 12 sectors of 30 degrees, each with its phase state, axial in the laboratory, no swirl. Same inlet
  data as the 12 per-phase runs. Outer boundary at 100 mm (still air moves at Mach 7.8 there in that frame).
- Run B (control of the instrument): the same 3-D run with the mean state all around. The flow is then
  axisymmetric and must reproduce the 2-D run of the mean state.
- Run C (the frozen pictures): the 12 phases and the mean state in 2-D on the SAME grid section (outer boundary
  at 100 mm), 3 ms, 12 dumps.
- Same thrust definition everywhere (wall pressure on plug and cowl plus inlet momentum, base priced apart).
- PASS LINE (from the S-REVIEW closure, LOG-11 item 1): |A - C(12 phases)| below 0.17 percent of thrust: the frozen
  pictures may carry the decisive number. Above: every arm of the decisive comparison is judged in the wave frame.
- The answer counts only if the instrument is sound: |B - C(mean state)| below the same 0.17 percent, run B flat
  around the annulus, the far-field pressure still at ambient, thrust steady over the last three dumps (1e-4) or
  read as a window mean with its uncertainty. If B fails, the pilot says nothing about the physics and the fault
  is in the rotating-frame run (suspect first: the hypersonic still air at the outer boundary).
- One azimuthal resolution. A difference within a factor 3 of the pass line calls for a 1-degree run before any
  reading.
Tools (outside the repo): `THOR_GPU/NOZZLE_2026-09-27/waveframe_case.py` (case builder; the boundary builder takes
a per-cell supersonic inlet with its direction), `handoff/plug_2026-09-29/post_waveframe.py`, `wf_run.sbatch`.
Smoke test on s2: 40 steps, no fault, the solver echoes the frame. Jobs 303409 (A), 303410 (B), 303411 (C).

## Order 4(d) — the single-wave monitor of the data contract: gates declared BEFORE authoring (R8), 19:25
What it checks. The design and the wave-frame judge both assume the RDE outflow is ONE wave that turns rigidly and
repeats itself. The monitor reads pressure histories at probes spread around the annulus and answers three
questions: how many waves; does the pattern turn rigidly (the signal at one probe is the signal at another,
delayed by the angle between them over the wave speed); does the pattern change from turn to turn.
Data of record: the Q2D THOR_CAv3 run that gave the 12 phases (`RDE/codes/Q2D/test/THOR_CAv3/OUTPUT`, probes
wall1..5 and piastra1..5 at 72-degree spacing, one sample per step, dt 3.12e-8 s; time from the residual
history's last segment). The last 3 ms (12.7 turns) are extracted into the repo, decimated by 4.
Gates (carrier `validation/single_wave_monitor.py`, row X-SWAV):
- W-1 ONE WAVE: every probe has the same period within 1 percent; the cross-correlation delay between probes 72
  and 144 degrees apart identifies the wave count n (delay = n x angle/360 x period, mod the period); n = 1;
  the count is the same in the first and the second half of the window.
- W-2 RIGID: after the delay, the relative RMS difference between two probes' signals (the pattern's change in
  the wave's frame) is below the LIMIT derived from the representation itself: the RMS of the pattern about
  its 12 sector means (what the 12-phase description already discards). A pattern that moves in its own frame
  by less than the sector averaging smooths is within the contract.
- W-3 REPEATS: the turn-to-turn change of the peak and of the mean pressure is below the same limit.
- R-1 (must fire): a second, counter-turning wave of 30 percent amplitude added to the record: W-2 fails.
- R-2 (must fire): the wave count doubled in the second half of the window (synthetic): W-1 fails.
- R-3 (must fire): a slow drift of the mean added (10 percent over the window): W-3 fails.
Not covered: probes at one radius and one axial station; the exit plane's own history is not on file (the
snapshot is one instant), so the monitor speaks for the chamber probes nearest the exit (piastra, x 23.4 mm).

## Where the session stands
Done: order 1. Next: order 2 (the cell check), then order 3 (the S22 bell campaign re-run).
