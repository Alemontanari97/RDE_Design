# Session log 2026-10-05 — F3.TWIN opened; the laboratory frame against the wave frame; plan step 2 started

Plain rules for this log: short sentences, one fact per line, physics before method.

## Opening (R2, R8)
- Phase F3 (F2 closed 2026-10-02, stamps commit 071a24a). Consumer: the owner.
- Owner's words, 2026-10-05: a status of the tool (literature reproduced, certified optima, can phase-aware design be shown
  viable and useful; a method that moves freely inside the envelope -- length, area ratio -- without oscillations); after
  the status: "vai con il piano" + "avviare una simulazione 3D di confronto tra un caso puramente unsteady con il sistema
  di riferimento fisso ed uno nel sistema di riferimento della detonazione per vedere se sono equivalenti".
- The plan read to the owner (three steps): (1) the decisive comparison on the plug -- walks to convergence, bands at two
  resolutions, CFD 2-D and 3-D on both; (2) the representation -- the wall by its angle with a monotonicity/curvature rule,
  the envelope as inequalities, a margin that sees converging waves; (3) the tournament between classes at one envelope.
- Exit criteria of this session: LAB-WF read against its pass line; F3.TWIN opened by a dated amendment before the arms'
  final runs; both arms resumed; a first number on step 2. Orchestration: 0 subagents; s2 <= 12 threads, nice 19, taskset.

## 1. LAB-WF: the laboratory frame against the wave frame (3-D, Rao's plug, methane case)
- Why it matters beyond the owner's question: amendment A-REPR makes the 3-D wave-frame CFD the evaluator of record of the
  twin only once a laboratory-frame run of one plug reproduces its wall thrust within 0.17 percent (one third of the
  0.5 percent thrust-stand band). PILOT-WF (2026-09-30) compared the wave frame with 12 FROZEN pictures, not with the
  laboratory frame: that gate was still open.
- Design of the pair: everything identical but the frame. Same mesh (`RDE/Nozzle/MESH/wf3d_RaSDT.dat`, 30 blocks,
  2-degree columns, rmax 0.10 m), same kit, same 12 sector states (`phases_cfd.json` 8302efd2), same far field (406),
  same CFL 0.4, RK2/HLLC/MUSCL-minmod, same binary (MOSE_open dcc627d8, built 2026-09-29 17:37). Wave arm = the run of
  record `wf_RaSDT_phases` (1 ms) and its kept field at 0.5 ms (`wf_RaSDTview_phases`). Laboratory arm = new.
- Builder `RDE/Nozzle/labframe_case.py` (new): the inlet is BC 410 "state mapped from a file, periodic" (MOSE_open
  interpolates each primitive linearly in time; checked in `Lib_Ghost.f90` / `Series_Data_m.f90`): the face at theta
  takes, at time t, the sector of theta + Omega t (the wave travels toward decreasing theta at 6364.5 Hz, as in the wave
  builder), axial velocity, no swirl; 181 samples per period (one 2-degree column per sample, the last = the first).
  Initial field: the channel = the pattern at t = 0, the exhaust at rest. Probes: 5 on the plug wall, 2 on the cowl,
  1 on the base (index-position = block i j k; files pre-created because the run restarts from the initial field).
- Checks BEFORE the launch: bc.txt identical to the wave case's record by record (311 021 lines) except the 5760 inlet
  records (405 -> 410); the 410 table at t = 0 equals the 405 sector pressures to 2.8e-16; at t = T/12 the pattern has
  moved exactly 15 columns (30 deg) the right way; every inlet column carries one sector (no straddling).
- Readers checked on the wave field itself: `RDE/handoff/plug_2026-09-29/post_labframe.py` (C_F with the inlet flux the
  410 table imposes at the dump time, sectors binned on theta + Omega t) gives 1.4071237187 against the wave reader's
  1.4071237187 (0.0e+00; sectors 4e-16); `compare_lab_wave.py` on the wave field turned by 30 deg and labelled t = 3T + T/12:
  C_F, sectors and the whole field equal to 1e-12. Pass line written in the reader before the run ended: 0.17 percent.
- Run: job 304078, premium, wn10, 30 ranks x 2 threads, 1 ms (6.4 periods), dumps every half period, started 15:37.
- Early reading of the probes (periods 2-2.9, against the wave field at 0.5 ms on the same cell row): plug wall median
  |error| 0.36-0.43 percent, cowl 0.70-0.73 percent, time means within -0.66..+0.29 percent; with the opposite turning
  sense 29-90 percent (the control). The 95th percentile (up to 8 percent) sits on the fronts between sectors. Base
  probe 18 percent: the base is not judged (the 406 far field drains the outside air).
- RESULT (16:19, job 304078 ended rc 0, 11 680 iterations to 1.0 ms; reader `post_labframe.py`, comparison
  `compare_lab_wave.py`, record `RDE/Nozzle/CASE_3D/lab_RaSDT_phases/{lab_post,compare_lab_wave}.json`):
  - Wall thrust, laboratory frame, 9 dumps from 2 to 6 turns: C_F 1.406303 (min 1.406292, max 1.406317: the annulus
    integral does not depend on time, as a rigidly turning pattern requires). Wave frame: 1.407115 (steady to 1e-5 over
    its four dumps). Difference -0.058 percent: PASS the 0.17 percent line.
  - Where the -0.058 percent comes from: -0.051 percent is the inlet DATA, not the frame -- the 410 table at one sample per
    2-degree column interpolates the primitives across each sector jump, so the columns in transition carry less momentum
    flux than the sectors' own (computed from the table alone: -5.4e-4 of the inlet term at 180 samples, halving with every
    doubling: -2.7e-4 / -1.3e-4 / -6.7e-5 / -3.4e-5 at 360 / 720 / 1440 / 2880, first order, to zero). The walls (plug and
    cowl pushes) differ by -0.0065 percent of C_F.
  - Sector by sector, walls only (the lab columns interpolated onto the wave grid): sectors 1-11 within 5e-4 C_F units
    per unit angle; sector 0, just behind the front (columns 185-203 deg), -3 percent of its own wall term: the front moves
    across the cells in the laboratory and stands in the wave frame. A first binning of the shifted columns without
    interpolation gave +69 percent on the weakest sector: a reader artefact, corrected and re-checked on the turned wave
    field (3e-14).
  - Probes (2-6 turns): time means within -0.66..+0.30 percent of the wave wall at the same cell row; instantaneous median
    |error| 0.35-0.40 percent on the plug, 0.65-0.67 percent on the cowl. Base probe -26 percent and the exhaust field
    (median 2-6 percent outside the nozzle): the 406 far field acts differently in the two frames (in the wave frame the
    still air is a Mach-8 cross flow); the base is not judged in either.
  - Reading: for the wall thrust the two frames are EQUIVALENT to 0.007 percent once the inlet momentum is the same; the
    3-D wave-frame CFD passes the A-REPR gate and is the evaluator of record of F3.TWIN (one plug, one instance, 2-degree
    grid, frozen chemistry). Not shown: the base and the plume (the far field), a second design, a finer grid.

## 2. F3.TWIN opened (amendment A-INST, commit e32835a)
- A-INST appended to `TWIN_PROTOCOL_preregistration_2026-08-31.md` and committed BEFORE any resumed segment was read:
  instance hashes, constraint vector, arms (P = 12 phases in J, C = the same walk at the mean state, Rao = anchor), the
  identical stopping rule (the walk's own stop or 64 segments), delta = the C_F ratio, bands, the evaluator gate = LAB-WF.
- Both arms resumed at 15:37 from their segment-23 checkpoints (budget 64): P on CPUs 36,37,38,43,44,47, C on 24,25,28.
  Cost: C ~3 min per segment (one march per evaluation), P ~30 min (12 marches).
- `validation/twin_harness.py` (new): R-TWIN-0/3 (hashes + identical walk settings but the objective), R-TWIN-1 (held
  hardware and lip identical; rejector: the lip moved by 2 x tol must be refused), R-TWIN-2 (each arm replays its walk's
  record to 1e-10; rejector: a design moved by 1e-4 on one knot must be refused), then delta over mu with A-1 quotability.
- ARM C ENDED (16:53) BY BUDGET: 64 segments (log counter: checkpoint at segment 63; the record's `segments` field, 27,
  is not the total), C_F at the mean state 1.437323777, certificate 0.038, in class, |grad|inf 0.52: stationarity NOT
  claimed. Design `validation/_plug_contest/SDT/twin/armC_design.json`. Wall smooth (turn to -15.1 deg at 59.4 mm, then the
  straightening to -6.9 deg; reversal <= 0.09 deg); tip r 36.50 mm against 39.27 (A24) and 38.19 (B24, the rehearsal's
  phase design): the rehearsal's "the 12-phase plug expands more" was the budget, not the phases.
- CFD evaluator of arm C launched at once (`RDE/handoff/plug_2026-09-29/sdt/twin_judge_sdt.sh`, walls in a dedicated file
  `RDE/Nozzle/plug_walls_sdt_twin.json`): 3-D wave frame job 304096 (mesh `wf3d_TwCSDT.dat`, 2 deg); 13 wedges at levels c
  and f (referee_cert.py, tag _twin).
- ARM P: 12 marches per evaluation, ~45-70 min per segment on s2; at 17:10 its first resumed segment is done.

## 3. Plan step 2: the wall in angle-increment coordinates
- No change to the frozen code: `RDE/handoff/plug_2026-09-29/sdt/angle_increment_basis.py` writes a TWOP_BASIS map whose
  coordinates are the increments of the chord slope between consecutive knots (kernel arcs held); the heights follow by
  cumulative sums (linear, invertible: as many coordinates as the knot-height walk). The smooth-angle rule = one curvature
  sign change per wall (the turn, then the straightening) = the box lb/ub the driver already takes. A knot-scale
  undulation alternates the increments' sign: it is outside the box by construction.
- First test where the undulations appeared: the methane shrouded posing, cap 0.65 (133 mm), mean state, from the cut
  Migdal TSh65, every knot of both walls free (11 + 11 + lip = 23 coordinates; the plug turns then straightens, the shroud
  turns one way only, as Migdal's), settings of the 5-mode smooth walk otherwise (24 x 12, tr0 0.008).
  Folder `_plug_contest/SDT/shroud_cap065_angleinc`. References: knot heights (wavy) +0.296 percent at the mean state;
  5 smooth modes +0.007 percent (stationary from segment 4).
- Smoothness measured (`sdt/wall_angle_check.py`: the excess angle variation = total variation of the wall angle minus that
  of one turn plus one straightening; 0 for a smooth wall): cut Migdal TSh65 0 / 0 deg (plug / shroud); 5 smooth modes
  0 / 0; 5 modes + kernel 0 / 0.12; the knot-height walk SSh65 (rejected by the CFD) 11.9 / 8.5 deg.
- RESULT (16:40, best base J 1.529757 = +0.051 percent at the mean state; from segment 12 every other segment's base fails
  to certify (the march blows up, worst 4e17) and is reverted: the radius 0.008 was tuned for the 5-mode basis, where one
  coordinate does not move the whole downstream wall): the shroud is smooth (0.03 deg), the PLUG IS NOT (21.2 deg, 4
  slope sign changes). Cause, read on the knots' chord angles: monotone up to the last knot (-26.6 ... -11.0, -6.0 deg),
  then the last chord, to the PINNED plug tip, returns to -13.4 deg. With a pinned end the last chord's slope is dependent,
  its increment is the one left out of the box, and the walk used it for a bump at the tip.
- Reading: the angle-increment box works where the wall's end is free (the shroud's lip here; the twin's plug, whose tip
  is free) with the driver as it is. A pinned end, or an envelope bound on an exit radius, is a LINEAR INEQUALITY on the
  coordinates, which the driver does not take (only a box and the class margin). That extension (scipy LinearConstraint
  in run_trsqp, rows in the TWOP_BASIS file) touches the frozen driver: by A-1 a code change after an arm's run re-fires
  R-TWIN-0, so it is developed in a separate worktree and merged only after the twin's verdict, followed by the record
  runs of every check whose closure it touches.

## 4. Plan step 2: the driver extension, in the worktree `RDE/RDE_Design_step2` (detached at e32835a; NOT in the tree of record)
- Why outside: by A-1 a code change after an arm's run re-fires R-TWIN-0; the arms run on the tree of record until the
  twin's verdict; the patch is merged afterwards, followed by the record runs of every check whose closure it touches.
- `a1_plug_spline_opt.run_trsqp(..., lin_cons=(A, lb, ub))` (default None = bit-identical): LinearConstraint to
  trust-constr; every point the driver proposes (backtracking, ascent, the solver's trial) cut back along its segment from
  the feasible base to the polytope's boundary.
- `PSPL_TRCAP=1` (unset = bit-identical): the solver's trial cut to the driver's radius before it is marched, the radius
  grown from the cut step. Defect it removes, read in the angle-increment shroud log (segments 12-24): with a box active
  trust-constr returned a step of 0.21 under a radius of 0.009; the end of the segment grows the radius from the SOLVER's
  step (min(0.25, 1.5 step)), so every revert (radius 0.25 -> 0.125) was undone at the next proposal and the same
  uncertified trial was re-proposed until the budget ran out.
- `a1_twowall`: the TWOP_BASIS file may carry rows A, A_lb, A_ub (inequalities in z, counted from the start like the box).
- `sdt/angle_increment_basis.py --linear`: the pinned end's increment as one row (checked against the geometry: the
  row's prediction equals the increment rebuilt from the knots to 1e-12 for three random z).
- Test (launched ~16:50, CPUs 31,32,34): the shroud posing again, same start and settings, the basis with the row, the
  trial cut on; folder `RDE_Design_step2/validation/_plug_contest/SDT/shroud_cap065_angleinc_lin`.
- RESULT (17:04): C_F 1.530090 = +0.073 percent over the cut Migdal at the mean state (box only: +0.051; 5 smooth modes
  +0.004; knot heights +0.296, wavy); certificate 0.121, in class, |grad| 0.23; no more re-proposed trial (the cut works).
  Smoothness: plug excess 0.705 deg (3 slope sign changes), shroud 0.015 deg. The chords are monotone by construction; the
  residue is the cubic between monotone chords overshooting.
- SECOND FORM (`sdt/curvature_sign_basis.py`): the carrier's wall is a cubic spline whose second derivative is piecewise
  linear between the knots, with the knot values (the moments) LINEAR in the heights, and sign(d theta/dx) = sign(y''): one
  sign change of the moments = one turn and one straightening of the continuous wall, exactly. Coordinates = every free
  knot height (23, as the knot-height walk), 24 rows (12 moments per wall; the natural end carries none); linearity of the
  rows checked at a random z: 3e-11. Walk launched ~17:15 in the worktree (`shroud_cap065_curvsign`, CPUs 31,32,34).
- RESULT 2: (pending)

## 5. The harness on the rehearsal pair (B24 against A24, anchor Rao)
- First run: arm P read 2e-8 off its record and a 12-phase certificate of 1e9: the harness imported the march module
  before setting the walks' env, and A1_NEWTON_RESCUE is read at import. Fixed (imports after the env). Second run:
  arm P replays its record exactly (0.0), certificate 0.044 over the 12 phases (quotable by A-1, bound 0.25).
- RESULT (third run, the K_RICH import fixed; record `RDE/handoff/plug_2026-09-29/sdt/twin_harness_rehearsal_B24_A24.json`):
  VERDICT PASS 9/9 -- instance hashes = A-INST; the walks read the pinned files; settings identical but the objective;
  P on mu, C on the mean state; hardware + lip identical, and the lip moved by 2 x tol refused; both arms replay their
  records exactly; a design moved by 1e-4 on one knot refused (2.8e-6 against 1e-10). Over mu: P 1.432445101, C
  1.427734389, Rao 1.414724322 -> delta +0.3299 percent (P +1.2526, C +0.9196 over Rao); certificates 0.044 / 0.047.
  This is the REHEARSAL pair; it reproduces the 10-01 table to the last digit.
