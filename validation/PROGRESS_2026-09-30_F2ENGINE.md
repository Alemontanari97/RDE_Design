# Session log 2026-09-30 — F2.ENGINE, session 3 of 6 (census R45): OPEN, orders 1-5 done, PILOT-WF read (PASS at 0.05 bar)

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
| pass with the settings of record, read later in the evening | X-RAOSQ PASS (the SQP returns to Rao's optimum, 3621 s), X-RAOHM 7/7 (Humphreys' Rao nozzle in Rao's world), X-PTRN 10/10 (`PSPL_FAN=axi PTRN_K=81 PTRN_N=41`) |
| read at 21:10 | X-RAOTW PASS (our march reproduces GENO's kernel below ED, with RAO_GENO_RUN), X-RAOFN PASS (our objective is Rao's) |
| read at 21:15: X-OWAB 8/8 PASS (2492 s, over the 1-hour cap) | read at 22:20: X-PAKN 12/14 (9392 s): A-8 and A-9 fail, the two rows the registry records as failing/void since S22 (the record reproduced) | still running: X-OWSQ + X-OWS3 | read and stamp at the next session (logs `carriers_2026-09-30/record_*_long.log`) |
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

## Order 4(a, b, c, e) — the other inherited items, read against the sector of the decisive comparison
- 4(c) X-LOCD (the locus diagnosis of the S20 rejections): its premise was that the rejections were genuine
  certification failures to be localised. With the new check (order 2) the five rejected designs certify in
  every solver variant: there is no locus to diagnose. The row stays declared failing on its own falsifier
  ("a rejected design whose re-record does not reproduce cert_worst > 1"), now for the right reason, and the
  finding that owned the cross-recorder flips is DOWNGRADED with the measured cause (the fixed line inside the
  arithmetic noise of the near-axis cells). No re-form of the script: it did its job, the answer is "none".
- 4(c) X-O32 (mesh convergence of the bell engine's objective and adjoint), 4(a) [P-IPADJ] (the multiplier
  rejector of the bell driver), 4(b) [OBJ-DOM-IMPL] (the panel-inclusive objective domain, the throat-angle
  gradient of the bell), 4(e) [P-QNCARRY] / [P-HESSREJ] (quasi-Newton carry and Hessian-symmetry rejector of
  the bell driver): ALL FOUR ARE BELL-ENGINE DUTIES (`a1_toc_variational_jax.py`). The decisive comparison is
  on the truncated plug (protocol section 2), whose engine is the spline walker with its no-fold class, its
  secant Hessian confirmed by second differences (X-TWOP DUTY-11) and the two walls decoupled. On the plug line
  the counterparts of these duties are on file; on the bell they are not, and no F2 exit gate on the plug
  sector consumes them. PROPOSED to the owner (decision P-F2-1, added to the pending list): re-home the four to
  the bell sector, off the critical path; F2 exits on the plug engine. Not executed here: the owner decides.

## F2a item U3' — the choking monitor of the extraction surface: gates declared BEFORE authoring (R8), 20:02
What it checks. Taking the outflow phase by phase presupposes a surface downstream of the throat where, in every
phase, the gas leaves axially faster than sound (no wave can travel back through it and the phases are
independent data). The monitor reads the extraction surface (the Q2D THOR_CAv3 exit column, 1799 cells, one
instant) and reports the axial Mach margin M_x - 1 cell by cell; the extraction surface is admissible when the
margin is positive everywhere and the smallest margin is above the uncertainty of the data (the wander of
X-SWAV: 2 percent of pressure is about 1 percent of Mach, so the line is 0.02 in Mach). The total Mach is NOT the
audit quantity (M0: the meridional normal Mach is): here the surface is a plane x = const, so M_x is exact.
Gates (carrier `validation/exit_choking_monitor.py`, row X-CHOK): C-1 M_x - 1 > 0.02 in every cell; C-2 the same
on the previous column (the surface is not a fluke of one column); R-1 (must fire): a subsonic patch planted on
30 degrees of the column (M_x 0.9) is rejected with its location printed.
Limit of the monitor: one instant (the snapshot); the wander in time is X-SWAV's business.

### U3' — result (carrier `validation/exit_choking_monitor.py`, row X-CHOK, log `carriers_2026-09-30/chok.log`)
PASS 3/3: on the exit column the margin M_x - 1 is 0.442 at its smallest (theta 99.5 deg) and 0.841 at its
largest; on the column before it 0.261 to 0.662; the planted subsonic patch is rejected and located. Reading:
on this source the outflow leaves axially faster than sound everywhere, by a margin twenty times the data's
uncertainty; the per-phase decomposition has its surface. U3' is answered YES for THOR_CAv3 by an executable
monitor; the general rule is the monitor itself, to be run on every new source.

## E4 — every F2a / F2b exit item of the plan (D6 F2 block), met with its check or listed with an owner and a date
| plan item | state 2026-09-30 evening | check / owner and date |
|---|---|---|
| F2a: certified stratified-data forward march | MET | `a1_rot_march.py` 9/9 (X-RMAR, pass 2026-09-30) |
| F2a: stage-A data-contract audits: Crocco residual, characteristic completeness, H-I2 margins | MISSING (Crocco, completeness), MET in part (H-I2/choking: X-CHOK) | owner F2.ENGINE session 4/6; needs the full exit field, not the last column; proposed date: the next session |
| F2a: T0 flatness monitor with derived threshold, G6 loud reject | MET as the single-wave monitor X-SWAV (rejects the data of record: the loud reject is operative); its harmonic-decay half NOT written | owner F2.ENGINE session 4/6 (harmonic-decay audit: a spectral row on the folded pattern) |
| F2a: contact/slip adjudication (smeared contact marched as smooth stratified data, declared rigor class) | PARTIAL: the march carries and bounds smooth layers (check W-5 of X-RMAR); the statement with its rigor class not in M0 | owner F2.ENGINE session 4/6: one M0 paragraph (PRACTICE: linear degeneracy, no self-steepening) + the extended margin covering the jump |
| F2a: U3' choking adjudication with an executable monitor | MET for the source of record: X-CHOK (M_x - 1 >= 0.44 on the exit column); the general rule = the monitor | run on every new source; owner = whoever brings a new source |
| F2b: adjoint / O3.1 at machine precision on the stratified march | MET | `o31_rot.py` PASS (X-O31R, pass 2026-09-30) |
| F2b: GENO moc_gen twin agreement in derived bands + independent invariants | PARTIAL: invariants met (mass, entropy, W-4); no run against GENO's layered solver | owner F2.ENGINE session 4/6 (one layered GENO case, derived band); GENO read-only |
| F2b: extended (q; s, h0) fold/validity margin WITH rejector | MISSING for layered flow (uniform flow: the no-fold class + `margin_governor.py`) | owner F2.ENGINE session 4/6: the fold census on the layered march's own cells + a seeded folded design that must be rejected |
| F2b: P-1 theory half + general-engine methods freeze at exit | NOT DONE | owner F2 session 5/6 (freeze) -- after the data contract closes on many-turn data (X-SWAV) |
| the fallback (two-family transport, h0 a named residual) | NOT NEEDED so far: the three-family march exists and passes | - |
| F2.M-RED first act: PILOT-WF | RUNNING (read below when the runs end) | this log |
| F2.CFD-2 paired demonstration | PARTLY IN HAND (the per-phase referee with certified convergence, S41-S42) | owner F2 session 5/6 |
Sessions: 3/6 consumed by this session. The exit of F2 is not declared tonight: two items are missing with an
owner and a date (the layered fold margin with rejector; the two data audits), one is partial (GENO layered
twin), and the freeze waits for the data contract. What blocks nothing: the plug-sector program (F3.TWIN
preparation) can proceed on the plug engine, whose counterparts of these items are on file.

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

### PILOT-WF — result of the 2-degree runs (read 20:40; cases `THOR_GPU/NOZZLE_2026-09-27/CASE_3D/wf_Ra10_*`, records `wf_post.json`; 2-D control `CASE_2D/Ra10w_phase*_wfc`, `referee_cert_wfcc.log`)
The instrument is sound.
- Run B (uniform inlet, wave frame, 3-D): C_F 1.383621 at 2.75 ms, the last three dumps within 1.5e-5; flat around
  the annulus (the 180 columns within 2e-4, std 1.1e-4); the 2-D run of the mean state on the same grid section:
  1.383607. Difference +0.001 percent, two hundred times below the line. The frame terms, the periodic block
  connections, the 405 relative inlet and the 406 far field do not move the thrust.
- Run C (the frozen pictures, 2-D, same grid section, outer boundary at 100 mm): all 13 cases CONVERGED (last
  three dumps within 4e-7); 12-phase C_F 1.322536 with the weights of record, 1.322119 with equal weights; the
  earlier grid with the outer boundary at 160 mm gave 1.322538: the boundary position is immaterial.
The answer at 2 degrees.
- Run A (12 sectors, wave frame, 3-D): C_F 1.320511 at 2.75 ms, steady to 1e-5 from 0.25 ms on. Against the 12
  frozen pictures: -0.153 percent (weights of record), -0.122 percent (equal weights, the like-for-like: the 3-D
  sectors are 30 degrees each). INSIDE the 0.17 percent line, but within a factor 3 of it: by the rule declared
  above the 1-degree run decides (job 303476, running).
- Sector by sector the rotating flow is NOT the frozen picture: the weak phases (3 to 8) give 2.5 to 3.3 percent
  MORE thrust than their frozen runs, the strong phase 9 (just behind the wave) 4.8 percent LESS, phase 10 1.9
  percent less. Physics: in the wave's frame the sector boundary 8|9 is the detonation's foot standing still;
  the high-pressure gas behind it spreads sideways into the low-pressure sectors along the plug, so the plug at
  the strong sector sees less pressure and at the weak sectors more. The redistribution is several percent per
  sector and cancels to a tenth of a percent in the total: the per-phase average is a good estimate of the
  cycle thrust even though every single frozen sector is off by percents.
- The base (priced apart): 3-D 12-sector -0.0369 of C_F, 3-D uniform -0.0352, 2-D mean state -0.0372; settled by
  1.5 ms in 3-D (the 2-D per-phase bases were not settled at 3 ms: -0.0279, flagged).
- Cost: 30 ranks x 2 threads on one node, 0.14 s per step, 33066 steps for 3 ms = 77 min (A); the wall thrust
  is steady from 0.25 ms, so 1 ms would have done for the thrust.
Reading against the pass line, PROVISIONAL until the 1-degree run: per-phase numbers may carry the decisive
number at THIS ambient (0.05 bar: every phase under-expanded at the lip, plume attached). The pilot says nothing
about 0.2 bar, where the frozen per-phase runs were unsteady and some phases over-expanded: a second pilot there
is the natural next act of F2.M-RED (the wave-frame run is steady by construction and may be the more robust
instrument exactly where the per-phase runs struggle).

### PILOT-WF — the 1-degree run and the reading (21:00; case `CASE_3D/wf_Ra10d1_phases`, 1.63 M cells, 1 ms)
- At the same instant (0.75 ms) the 1-degree run gives 1.320464 against 1.320533 at 2 degrees: -0.005 percent;
  sector by sector the largest change is 0.06 percent (sector 9, the one behind the wave). The azimuthal grid
  is converged for this question; the difference between the rotating flow and the frozen pictures is real,
  thirty times the instrument's error (run B) and twenty-five times the grid's.
- Number of record (2-degree run at 2.75 ms, corrected by the 1-degree offset): C_F 1.320442. Against the 12
  frozen pictures on the same grid section: -0.127 percent with equal weights (the like-for-like: the 3-D
  sectors are 30 degrees each), -0.158 percent with the weights of record (a Q2D cell-count artefact on phase
  6, kept for the record).
- READING AGAINST THE PASS LINE (0.17 percent, declared before the read): PASS, by a small margin. At 0.05 bar
  the average of the 12 frozen pictures carries the cycle thrust of Rao's plug to 0.13 percent, and per-phase
  numbers may carry the decisive number at this ambient. What the pilot does NOT say: anything about 0.2 bar
  (phases over-expanded at the lip, unsteady frozen runs) or about a design other than this plug. The margin to
  the line is 0.04 percent: a second pilot at 0.2 bar is the next act of F2.M-RED before the per-phase judge
  is used where phases are over-expanded.
- Physics of the residual: the frozen picture overestimates the thrust of the strong sector behind the wave
  (its pressure leaks sideways along the plug) and underestimates the weak sectors; the two nearly cancel
  because the plug's pressure integral is close to linear in the sector pressure. The residual -0.13 percent
  is the part that does not cancel.
- Records: `CASE_3D/wf_*/wf_post.json`, `case.json`, `run.log`; the fields, the initial conditions and the
  1-degree mesh deleted here, the cluster copy removed (12 GB); the 2-degree mesh kept for the 0.2 bar pilot.

## 21:30 — the owner's order for the night: Rao's plug against the SQP plug, both run with the RDE solution, on the SD Toolbox case
Order: "vorrei che stasera arrivassimo a fare un confronto tra plug fatto con rao e girato con la soluzione rde e
plug fatto con sqp ottimizzato e girato con rde". Data: stoichiometric methane at high pressure, from the
literature on disk. The case on disk: Stechmann, Heister & Harroun (JSR 2019), CH4/O2 phi 1, mean chamber
pressure 20 atm, fill temperature 200 K, ambient 1 atm (their aerospike row): the matched detonation cycle is
already computed in the repo (`data/st_nozzle_opt.json`, state det|CH4|20|1.00: post-detonation stagnation
80.9 atm, fill 1.77 atm, pressure ratio 45.1 over the cycle, T_CJ 3897 K, R 388, c* 1934 m/s) by the CJ chain
of `src/thrust/stechmann_nozzle.py` (Cantera + SD Toolbox).
### CycleFamily v0 (plan item 5) — gates declared BEFORE authoring (R8)
The family: Pc(xi) = P0 exp(-xi ln PR) (the paper's Eqs. 13-14), T(xi) isentropic from T_CJ with the paper's
gamma_s, 12 sectors of equal time (= equal angle in the wave frame), each sector's (P0, T0) = its time mean;
gas of the design tool per phase: constant gamma and R = the FROZEN products at the extraction state of the
phase (equilibrium composition at the phase's own stagnation state, then frozen; the CFD runs the same
composition with its tabulated thermo); extraction Mach M_in = 1.556 (the S42 posing, kept so the internal
nozzle and the annulus are the THOR hardware: a THOR-sized CH4/O2 engine at 20 atm); ambient 1 atm.
Gates (carrier `validation/cycle_family_v0.py`, row X-CYCF): F-1 the cycle mean of Pc equals Pcp (1 + DC) of
the matched state to 1e-6; F-2 the 12 sector means integrate the exponential exactly (analytic vs quadrature
to 1e-9); F-3 mass per cycle = the CP combustor's (the matching, recomputed) within the matched tolerance 1e-2;
F-4 every phase's composition sums to one and its frozen gamma lies in (1, 5/3); F-5 the single-wave contract
holds by construction (one period, rigid, no wander: the monitor's W-1..W-3 on a synthetic probe record give
zero residual) and the extraction plane is supersonic in every phase (X-CHOK's rule); R-1 (must fire): a
family whose mean pressure is off by 1 percent is refused by F-1.
Consequence for the comparison: with a pressure ratio of 45 over the cycle and 1 atm outside, the last third
of the cycle leaves the lip below ambient: the case the S-REVIEW asked for.

### CycleFamily v0 — result (carrier `validation/cycle_family_v0.py`, X-CYCF; records `validation/_cycle_family/sdt_ch4_phi1_pcp20/`)
PASS 8/8 (F-1..F-5b and the rejector). The family: 12 sectors with P0 from 68.5 atm (just behind the wave) down
to 2.1 atm (the refill), T0 3824 to 2522 K; the products recombine as the gas cools, so R falls from 384 to
325 J/kg/K and the frozen gamma runs 1.188 to 1.216; mean state P0 20.5 atm, T0 3132 K, gamma 1.1935, R 343.8.
THE AMBIENT: at 1 atm (the paper's) the last three phases leave the extraction plane BELOW ambient (0.57 to 1.08
of p_a at M_in 1.556): the internal nozzle would carry a shock inside for a quarter of the cycle, which the
design tool has no model for (F4b). The pilot posing is 0.5 atm: every phase leaves the plane above ambient
(1.14 to 37 of p_a); after the internal expansion the last three phases are over-expanded at the lip -- the case
the S-REVIEW asked for, at the tool's edge but inside it. Declared; a 1 atm column of the same two plugs in the
CFD costs nothing more and is owed.
The design tool's gas: constant gamma and R per phase (its own model); the CFD: the equilibrium products of the
phase frozen through the nozzle, on a 14-species methane kit (the frozen kit of MOSE_open's rocket-nozzle test,
13 species to 5000 K, plus N2 for the ambient air; traces the kit lacks, below 1e-6, dropped and renormalised).
The referee chain (mesh, bc, ic, wave-frame case, post) now reads its species from the kit in use (`kit.py`,
`NOZ_KIT`, `NOZ_PHASES`; a case records its kit and its P0 A* normalisation: 8964.6 N here = P0_mean x A* of the
THOR annulus at M_in, the design tool's own). Smoke test: a methane wedge case runs 60 steps.
A mistake, repaired: the internal-nozzle tool writes `start_intnoz_b10p0.json` beside itself, so the methane run
overwrote the S42 THOR record; regenerated on the THOR posing bit for bit (lip 35.761 mm / 66.484 mm, M 1.8039,
-8.707 deg, C_F 1.390969: the S42 numbers), the methane one moved to `sdt/start_intnoz_sdt_b10p0.json`.
The chain of the night (all under `RDE/handoff/plug_2026-09-29/sdt/`): internal nozzle -10 deg at the methane
mean state (lip at 35.20 mm / 66.53 mm, M 1.784, -8.74 deg, p/p_a 7.83; start nozzle+cone C_F 1.4206, in class)
-> Rao's mass-matched member from that lip by GENO (constant-gamma thermo written for the methane mean state,
`geno_base/`) at 0.5 atm and the 87 mm budget -> the graft -> the SQP walk with the 12 phases from Rao's plug
(PSPL_FLOOR_LIMIT, RESCUE) -> both plugs in the wave frame (3-D) and per phase (2-D) at 0.5 atm.

### The classical arm on the methane case (22:20; `sdt/rao_sdt/rao.json`, `sdt/start_rao_sdt.json`)
Rao's members from the lip state (r 66.53 mm, M 1.784, -8.74 deg) are all designed for 2.0 to 2.6 bar: the ambient
of Rao's own optimum at the budget's length is 2.62 bar, five times the 0.5 atm the plug will run at (the same
situation as the THOR rehearsal: Rao's member of the budget's length is under-expanded at the mean state).
Rule applied: the budget's length (the length constraint active): Me_fixed 2.0942, L 51.81 mm (total 87.01),
theta_E +2.40 deg, mass matched to 1e-6. Grafted on the internal nozzle at the lip plane (shift +0.217 mm, the
direction jumps from -10.0 to -12.09 deg: a corner, declared as in S42). Marched at the mean state: C_F 1.412293
(certificate 0.139, class +0.607); the tool's 12-phase reading and the CFD follow. The wave frame of the methane
engine: the CJ speed 2439 m/s (the chain's own CJ state) over the mid-annulus circumference: 6364 Hz, declared
(a real wave runs at 80-90 percent of D_CJ; both plugs are judged at the same speed).
Runs launched 22:27: `wf_RaSDT_phases` (3-D, 1 ms, job 303530; the still air's relative Mach at the outer
boundary is now 12) and the 13 wedge cases `RaSDT_phaseNN_sdt` at 0.5 atm (job 303531, 1.5 ms, 6 dumps, window
from 1 ms); the SQP walk with the 12 phases from Rao's plug (`_plug_contest/SDT/BcowlB_sdt_fromRao`, 8 segments,
PSPL_FLOOR_LIMIT, RESCUE) launched 22:25.

### Order 5 — the demonstration walk read (23:05; `_plug_contest/L87/BcowlB_intnoz10_fromRao_pa020_floorlimit`, v1 = the first form)
The 0.2 bar 12-phase walk from Rao's plug (the one that stopped after one segment in S42, C_F 1.122714):
- first form (distance along the ascent, v1): "infinite" at every base -- the margin GROWS along the gradient
  -- the floor stayed 2.02e-3 and the walk stopped exactly as in S42, at 1.122714. The measure was blind.
- second form (the constrained step with the class active is the distance): at segment 1 the step 2.07e-4 under
  the floor with the multiplier 7.5 lowered the floor to 1.26e-4; the walk went on: 1.122714 -> 1.122891 (seg 2)
  -> 1.122898 -> 1.122904 (seg 4), then steps of 1e-5 with the multiplier at 84: the walk sits ON the class
  boundary. Gain +0.017 percent over the S42 landing; the +0.18 percent the S42 note quotes for "a four times
  finer step" came from a walk whose class file was the lost original, not reproduced here.
Reading (physics): at 0.2 bar the plug from Rao's design is held by the no-fold class, not by the floor; the floor
hid it by one segment. The measured-distance rule is the right stop rule; the finding's magnitude (0.18 percent)
is not reproduced, the finding stays open on that number. Class file used: the reconstructed one.

### Rao's methane plug run with the RDE solution (23:10; `CASE_3D/wf_RaSDT_phases/wf_post.json`, `referee_cert_sdtc.log`)
- Per phase (2-D, 0.5 atm, 1.5 ms, window from 1 ms): C_F 4.831 (phase 0, just behind the wave) down to 0.102
  (phase 11); phases 7, 10, 11 UNSTEADY (over-expanded at the lip: separation, the last three of the cycle);
  12-phase average 1.412844 +- 1.6e-4 (equal weights: the family's). Mean state 1.410272 (tool 1.412293: +0.14
  percent, the tool and the CFD agree on this gas as on the THOR one).
- Wave frame (3-D, 6364 Hz, 0.75 ms, steady to 1e-5 from 0.25 ms): C_F 1.407115. Against the 12 frozen pictures:
  -0.405 percent -- OUTSIDE the 0.17 percent line. Sector by sector, monotone from the wave: the strong sector
  behind the wave -6.4 percent, then -3.8, -1.0, +2.4 ... up to +16.8 percent on the weakest sector. With a
  pressure ratio of 45 over the cycle the sideways spreading of the high-pressure gas along the plug moves 5 to
  17 percent per sector and 0.4 percent of the total. Reading for F2.M-RED: at THIS data class the frozen
  pictures do NOT carry the number to the line; the wave-frame judge is the judge of record here (the pilot's
  second question answered without a second 0.2 bar THOR run: a stronger cycle is the harder case).
- The 3-D run: 13632 steps for 1 ms, 35 min on one node (14 species); the relative Mach of the still air at the
  outer boundary is 12 and the 406 far field held.

### THE COMPARISON OF THE NIGHT (00:00): Rao's plug against the SQP plug, both run with the RDE solution, on the methane case
Table of record `validation/_plug_contest/SDT/table_2026-09-30.md` (+ .json).
| design | tool mean | tool 12 ph | CFD 2-D mean | CFD 2-D 12 ph | CFD 3-D wave frame | 2-D unsteady phases |
|---|---|---|---|---|---|---|
| Rao (budget's length, from the lip state) | 1.412293 | 1.414724 | 1.410272 | 1.412844 | 1.407115 | 7, 10, 11 |
| SQP at the mean state, from Rao's plug (10 segments by budget, not at its optimum) | 1.418513 | 1.421056 | 1.416519 | 1.419177 | 1.412733 | 7, 9, 10, 11 |
- SQP over Rao: +0.44 percent by every frozen judge (tool mean and 12 phases, CFD mean and 12 phases, all within
  0.01 of each other), +0.40 percent in the rotating flow. The difference between the designs is real, it is
  small, and it survives the change of judge. It is a LOWER bound for the SQP: the walk stopped by budget with
  |grad| 0.72; the 12-phase walk (`BcowlB_sdt_fromRao`) runs on and its column is owed.
- Where the SQP gains, sector by sector in the rotating flow: 0.0 percent right behind the wave, +0.6 to +0.8 in
  the middle of the cycle (sectors 2 to 8), +0.4 and +0.1 in the last, over-expanded sectors. The SQP moved the
  tip inward (41.8 -> 40.6 mm) and put the gain where the pressure ratio is moderate.
- The frozen pictures overestimate BOTH plugs by 0.40 to 0.45 percent (outside the 0.17 line): the offset is the
  flow's, not the design's, and it cancels in the comparison to 0.05 percent. For a comparison the per-phase judge
  is adequate at this class; for the absolute number the wave-frame judge is needed.
- The tool and the CFD agree to 0.14 percent on the methane gas at every reading (as on the THOR gas): the tool's
  per-phase model with the separation closure holds up on the over-expanded phases too (phase 11: tool 0.101,
  CFD 0.102).
- Both plugs are of the 87 mm budget: Rao's member is designed for 2.6 bar (under-expanded at the mean state
  by five); the length constraint, not the ambient, sets Rao's contour here as in the THOR rehearsal.
Cost of the night's CFD: 2 x 35 min (3-D, one node each) + 2 x 25 min (13 wedge cases, one node); 4.6 GB on the
cluster, removed; fields removed here; the records kept (wf_post.json, cert.json, case.json, logs).

## Where the session stands (00:05)
Done (night): the methane case built (CycleFamily v0), Rao vs SQP-at-the-mean-state judged in the wave frame (+0.40 percent SQP,
lower bound), Rao's frozen pictures vs rotating flow -0.4 percent at this class. Running: the 12-phase SQP walk, X-OWSQ/X-OWS3.
Earlier in the evening: orders 1-5 (order 5's second measurement landed after the first proved blind; its demonstration walk is
running); the single-wave and choking monitors; 27 owed checks re-stamped; PILOT-WF read at 0.05 bar: PASS.
Not done for the F2 exit (table E4 above, owners and dates): the two data audits, the layered fold margin with
rejector, the GENO layered twin, the harmonic-decay half of the monitor, the freeze. Counter: 3/6 consumed.
Owner's request at 20:30: input data from SD Toolbox (case A of Annex B: CJ + blowdown) instead of the THOR
outflow (1.5 bar, weak signal, and the 2 percent wander of X-SWAV). Answer: yes, it is the protocol's own data
class; the CJ chain is in the repo (`src/detonation/cj_states.py`, `src/cycles`, Cantera 3.2 in the venv); the
CycleFamily v0 generator (plan item 5) is the first act of session 4/6, with the owner's specs (CH4/O2 pinned,
phi, mean pressure, p_a, annulus).
