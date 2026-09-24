# S34-S35 — The class in R, THEIR throat as the start, and the first re-obtentions of the plug optimiser (2026-09-23/24, [F3/A1], brick-2 plug line)

Sessions and trees:
- **S34**, night 09-22/23 and morning 09-23 (session mose-10). Handoff
  `RDE/handoff/NOZZLE_HANDOFF_2026-09-23.md`.
- **S35**, afternoon 09-23: the throat posing. Handoff
  `RDE/handoff/NOZZLE_HANDOFF_2026-09-23_gola.md` sections 1-7.
- **S35 evening/night**, 09-23/24 (session mose-a1): sections 8-9 of that handoff and this log.

All the work ran in the isolated worktree `RDE_Design_tri` (branch `tri-experiment` from
742f9b7). It is landed here in one window, per the owner's word of 2026-09-24: "se i test
avessero successo e sqp si dimostrasse in grado di lavorare sui plug, voglio che tu prepari un
commit, seguendo tutte le regole della git". The tests of that condition are section 7.
Communication with the owner in Italian; this log in English (CLAUDE.md).

## 1. S34 (night + morning): where the class must be measured, and the base as THEY price it

Code: `a1_plug_march.py` margin `vec`/`region="R"`, `a1_plug_spline_opt.py` PB_FROZEN and
PSPL_WLOG, `a1_humphreys_twin.py` stage mderive and the opt() knobs. All additive; unset they
are bit-identical.

- **The margin, vectorised.** `margin["vec"]` computes the same KS field with every point
  stacked once, identical to the in-loop margin (value rel 2e-16, gradient rel 2e-13, same
  schedule) and 6.4x cheaper (27 s against 174 s per value+gradient).
- **The margin constants on Humphreys' posing** (stage mderive, [X-PMRG] D0-D4):
  - on the whole net, 11/11: m_ref 0.1102, floors m_ref/2^k, rho 4807.7, h* 8.1e-4 R;
  - restricted to R (HMPH_MREGION=R), 9/9: rho 3386.0 over 340 cells, h* 1.30e-2 R.
- **THE REGION R.** The thrust (wall pressure up to D, and the state at D for the base)
  depends only on Humphreys' region R: below the exit characteristic DB, downstream of the C+
  from T (p. 1582-1584). The topological R of the march is a cell whose C- ends on the wall
  before D.
  - The folds of the whole-net census sit in the jet, above DB. The S34 readers counted them
    on 14 designs: the old landings, the straight wall, their contour marched 'come loro'.
  - Those readers are in RDE/handoff/s34_2026-09-23/ and are NOT committed. The count is
    therefore a READING of the handoff, not a number of record (R5).
  - What is of record: every design the committed throat posing walks and reads below prints
    its minimum margin in R (read_design). That is the class used from here on.
  - Consequence: "their optimum is out of class" (S33, the whole net) was a whole-net
    artefact.
- **THE BASE AS THEY PRICE IT** (p. 1582-1583). The base pressure is a constant of the
  variational problem, recomputed between iterations. PB_FROZEN implements it.
  - Differentiating the Veen closure inside the walk was the spurious lever of S33, the
    +40 deg tail up-turn. Frozen, it is gone.
- **Declared**: the certification floor of the wall cells stopped every S34 walk in R
  (handoff G-9). The S34 walks started from OUR planar-fan cut and could not reach their
  contour (handoff G-1/G-11): the start was the defect.

## 2. S35 (afternoon): the throat posing — the optimiser starts where THEY start

Owner: "fintanto che non riusciamo a cominciare dallo stesso punto è infattibile ottenere il
loro profilo". The new carrier is `validation/a1_throat_posing.py` ([X-TPOS]).
- **The start**: their throat A-E through the annular kernel, and the start 'come loro'.
  That start is the domain of dependence of the start line, marched with certified cells
  (`validation/a1_ivl_triangle.py`, [X-IVLT]).
- **The wall**: the lip fan in the kernel's field, the rotated cells, and their arc A -> T
  FIXED. After T comes the design, anchored C^1 at T, to D at their length T -> D (12.0004 in).
- **Stations and functional**: the stations after T are frozen in record-frame x
  (`a1_plug_march` x_traced, additive). J = F_in + wall push + base, with PB_FROZEN honoured.
- **Driver**: it delegates march_record, J_replay and margin_replay to the posing when the
  case carries "throat"; the TR-SQP itself is unchanged.

Gates (stage gates):
- TP-1: the chain = stage kernel, J 32,494.5587 lbf at (160,41), rel 2.2e-16.
- TP-2: the basis holds their contour, 0.027-0.030 in.
- TP-3: replay = record, rel 0-2.2e-16.
- TP-4: adjoint = FD ladder.
- 4/4 at (40,21) in y and in angle, and at (160,41) in y.

**The walks** (stage walk, (40,21), angle basis, PSPL_ITERS 10, PSPL_BACKTRACK 3, p_b frozen
and recomputed over 3 outer walks):

| start | start's knots - theirs [in] | landing's knots - theirs [in] | J [lbf] | tip [in] | min margin in R | cert |
|---|---|---|---|---|---|---|
| generic, uniform turn to 0 deg | -0.147 .. -0.700 | +0.019 .. +0.074 | 32,481.4 | 1.029 | +0.0067 | 0.034 |
| generic, uniform turn to +10 deg | -0.328 .. +1.040 | +0.018 .. +0.072 | 32,481.5 | 1.026 | +0.0067 | 0.035 |
| their contour through the basis | -0.030 .. +0.015 | +0.011 .. +0.031 | 32,482.0 | 0.985 | +0.0066 | 0.037 |

- **RE-1 in contour**: every knot is inside the class of permanence (0.15 in) of Table 2.
- **RE-1 in value**: their contour in the same posing reads 32,482.5 lbf, and J/mdot is
  228.56 against 228.51 for the paper per consistent mass.
- **RE-3**: the two generic landings coincide within 0.0025 in, and their angle increments
  within 0.022 deg.
- No fold inside R at any landing; about 12 % of the whole net folds, in the jet.

## 3. S35 evening (mose-a1): fine grid, T on the arc, Table 4, Fig. 4, Rao, regressions

- **(160,41) re-read** (stage walk, TPOSE_OUTER=0). J(landing) - J(their contour) = -1.1 lbf
  at both grids (32,488.1 against 32,489.2). The gradient at the landing is grid-converged
  (cosine 0.990, |g| 9.5e3 -> 9.9e3). Along the line from their contour to our landing the
  directional derivative goes +215 -> -67, so the maximum lies between the two. The (40,21)
  walk from their contour lands on that line (projection 0.99).
- **T ON THE ARC (TPOSE_THT_DEG).** The paper (p. 1584, 1585-1586): T is "fixed, but not
  predetermined", the C^1 junction of the relaxed wall with the prescribed arc, and "this
  portion of the nozzle wall will not necessarily be an optimum". It is not an optimisation
  variable of theirs.
  - Gates of the knob (stage tslide, 3/3): the start is bit-identical at their theta_T; J
    moves by 0.0809 lbf there, below the basis error 5.28 lbf; every theta_T of the study is
    downstream of the cut and its re-anchored start certifies.
  - The study (stage walk with TPOSE_START=reanchor: the landing's knot angles kept at the
    new T), plug-side turning on the arc 7 / 9.5 / 12 (theirs) / 15 / 18 deg:
    - J = 32,413.9 / 32,458.3 / 32,482.1 / 32,483.2 / 32,449.6 lbf;
    - the landings at 15 and 18 deg FOLD inside R (margin -0.016, -0.059).
  - Reading: **their T is the best landing that does not fold in R**. More plug-side
    expansion brings a recompression after T that coalesces inside R. The walk at their T
    closes the p_b fixed point with |grad J| 98, the most stationary landing of the line.
- **TABLE 4** (their optimum for the Panov-Shvets base, Eq. 38; same throat; T at -45.75 deg,
  D at 11.58406 in). The last two rows were lost in the 09-18 transcription and are recovered
  from the paper's text (`_table4_recovered_rows`); the knob is TPOSE_TABLE=table4.
  - Their Eq. (38) is written on p_inf, M_inf, and the nomenclature (p. 1581) reads "inf =
    freestream conditions". For a base, that is the stream that reaches it: the state at D.
  - base_pressure's `panov_shvets` member is written on the AMBIENT. The posing-local knob
    TPOSE_PS_REF=corner reads it on the state at D; the repo member is unchanged.
  - Reads at (40,21):

    | contour | Veen (their Table 2 model) | Panov-Shvets on the ambient | Panov-Shvets on the state at D |
    |---|---|---|---|
    | their Table 2 | 32,482.5 (\|g\| 2.3e4) | 32,490.8 (6.3e4) | 32,531.6 (2.7e5) |
    | their Table 4 | 32,326.3 (4.3e5) | 32,431.3 (2.3e5) | **32,561.5 (2.2e4)** |

  - With the state-at-D reading, J4 - J2 = **+79 lbf against the paper's +84**, and Table 4 is
    as stationary as Table 2 under its own closure. Each optimum is far from stationary under
    the other closure.
  - With the ambient reading the sign flips: -51 lbf.
  - **The walks, ad armi pari** (stage walk, TPOSE_TABLE=table4, TPOSE_PS_REF=corner, angle
    basis, (40,21)). With p_b frozen over a whole walk of 10 segments (the Table 2 protocol) the
    closure on the state at D oscillates between walks (2.5 -> 0.9 -> 1.5 p_a) and the generic
    starts land 0.6-0.7 in off, FOLDED in R. With THEIR update frequency -- p_b recomputed at
    every accepted step (TPOSE_PB_EVERY, PSPL_ITERS=3, 30 outer steps) -- all three walks land
    on ONE design:

    | start | start's knots - Table 4 [in] | landing's knots - Table 4 [in] | J [lbf] | p_b [p_a] | \|grad J\| | min margin in R |
    |---|---|---|---|---|---|---|
    | generic, uniform turn to 0 deg | -0.135 .. -1.185 | +0.027 .. +0.041 | 32,555.5 | 1.306 | 3.8 | +0.0057 |
    | generic, uniform turn to +10 deg | -0.089 .. -0.523 | +0.027 .. +0.041 | 32,555.5 | 1.306 | 4.9 | +0.0057 |
    | their Table 4 through the basis | +0.001 .. +0.041 | +0.027 .. +0.041 | 32,555.5 | 1.306 | 2.9 | +0.0057 |

    RE-1 in contour and value (their contour in the same posing reads 32,561.5 lbf; the
    landing is 6 lbf below it with the p_b fixed point closed at 1.3059 p_a over the last
    10 steps), RE-3 (the three landings coincide to the printed digit), 3/3 each. The tip
    lands at 2.38 in against their 2.34.
- **FIG. 4** (stage fig4, 2/4; the owner digitised the figure on 2026-09-23, now in
  `validation/humphreys1971_digitised/`). The two contours of the same length, +/-0.5 in at D
  (printed 32,556 / 32,601 lbf against 32,881), are marched as Table 2 plus the digitised
  DIFFERENCE, so the calibration error common to the three curves cancels.
  - F4-1 PASS: the digitised optimum reads Table 2 at rms 0.046 in, max 0.118 in (tail).
  - F4-2 PASS (SIGN): both contours lose thrust.
  - F4-3 FAIL (ORDER, at the random-noise smoothing, 0.0067 in): upper -88.5 lbf, lower
    -170.8 lbf, against the paper's -325 / -280.
  - F4-4 FAIL (CLASS): both march FOLDED inside R (margin -0.054, -0.091). Their faster turn
    back after T compresses the flow into a shock that the march cannot carry.
  - At the whole-noise smoothing (0.046 in) the numbers are upper -110.7, lower -44.3 lbf.
  - The magnitudes, and even the order, move with the smoothing of the digitised near-throat
    shape by more than their own size: the comparison is ill-conditioned AND out of class.
    Only the sign is a reading; nothing is certified by it (G1).
- **HUMPHREYS' RAO NOZZLE** (their Table 3). THEIR start = a GENO RaoPlug run posed by Rao's
  own method: lip transversality at their p_a, D at their x_D, their Veen base as a fixed
  point (`validation/humphreys1971_rao_geno/input.ini`).
  - Stage raogeno (a1_humphreys_twin), 2/2: the GENO wall reproduces Table 3 at mean |dy|
    1.32e-4 y_E, max 0.00132 in, against the Rao-world level of record 2.44e-3 ([X-RAOTW]).
    D is inside the band; the wall angle is within 0.011 deg on the unflagged rows.
  - Their "approximately -58.5 deg" is not Rao's sonic-line direction of that design
    (-55.84 deg).
  - The printed angle -28.40556 at x 3.03421 repeats the decimals of its own y: probably a
    second misprint, flagged by the stage.
  - In Rao's world, with the Rao carriers' new knobs (RAO_PA_PC = 14.7/500, RAO_PB = their
    Veen p_b over p0, RAO_TH/RAO_APERT scaled by the length ratio; unset = Rao 1961):
    - twin PASS;
    - O3.3 **7/7** at x0 0.10 m. At x0 0.0746 m the march reaches D 1.3 % low in Mach and the
      tip/corner checks fail, 5/7. The cut must lie where the twin verifies the march.
    - SQP return **6/6** at x0 0.10 m once the driver's initial trust radius is scaled by
      the length ratio (RAO_TR0 = 0.05 x 0.29258/1.1766 = 0.0124): from a 1.5 % perturbation
      (17x its band in the worst eigen-direction) the landing is inside every band (worst
      0.08), |J(W*) - J(Rao)| = 7e-3 N against a band of 599 N, and the sign-flipped driver
      walks away (2.9x the start's distance). At the record's radius 0.05 the rejector's
      every trial left the class (14/14 uncertified) and R1 read 5/6: an instrument setting,
      declared, now a knob.
- **REGRESSIONS of the record path, run from the worktree: 16/16 as recorded.**
  - Carriers: oracle 6/6; frame 4/4 (F-0 2.9e-15); kernel chain cut 4/7 and char 5/7, with
    JSON == branch; class 10/10 and angle 10/11, with md5 == branch; rao 4/6; throat 4/6;
    Moore 7/7; Dutton verify 4/4 and dutton 8/8; axi 5/5; source-flow 6/6; free-jet 6/6;
    bit-identity gate rel 0.00e+00.
  - Rao 1961 in his world with today's code: O3.3 7/7, SQP return 6/6. With the new knobs
    unset, the O3.3 output is line-identical to the run before the knobs.
  - The bit-identity gate needs `validation/_driver_eps_ckpt.json`, an UNTRACKED file of the
    main tree (declared; copied into the worktree to run it).

## 4. Theory landed (R4)

M0 Part VI, LINE ADDENDUM S34-S35: the class in R; closures frozen and iterated, and the
update frequency; the reference's initial condition is the posing (owner's rule 2026-09-23);
T is not their variable, and their T sits at the class edge; Panov-Shvets on the stream that
reaches the base; Humphreys' Rao nozzle = Rao's method with their base; Fig. 4 folds in R.

## 5. Declared deviations and incidents

- **R3**: S34 and S35 closed with handoffs, not with logs in validation/ (the worktree was
  uncommitted by the owner's directive). This log consolidates them at commit time; the
  handoffs stay the working record.
- **R5**: the S34 whole-net/R census on 14 designs came from scratch readers and is quoted as
  a reading (section 1).
- **The Table 4 walks were relaunched twice** in the evening:
  - PSPL_ITERS=1 records the base and never steps;
  - PSPL_ITERS=2 loses a step accepted by backtracking, because the driver returns the best
    CERTIFIED base.
  
  The knob's comment now says PSPL_ITERS=3. The runs were renamed *_NOSTEP_ITERS1 and
  *_LOSTSTEP_ITERS2 and are not read.
- **The first Humphreys-Rao chain ran with Rao 1961's ambient** (PA_PC 0.0355, hard-wired);
  it was discarded, and RAO_PA_PC added.
- **SR-9 orchestration** (shape + rounds + tokens):
  - two read-only survey agents, one round each: repository verification cases 405k tokens,
    literature 360k tokens;
  - one general-purpose agent posing Humphreys' Rao nozzle in GENO: one round, 7 attempts,
    488k tokens, outside the repos.

## 6. HANDOFF (parallel-session closure block)

- HEAD: the S34-S35 commits on `rde-nozzle-program` (this log + code + data, then the
  registry half), fast-forwarded from the worktree branch `tri-experiment`, and PUSHED on the
  owner's word of 2026-09-24 ("purche' il commit sia in linea con il lavoro della git, puoi
  pushare direttamente su rde-nozzle-program"); the worktree removed afterwards, as asked.
- Parallel sessions of the window: the multirate line (mose-a9 / mose-36) works on other
  repositories; no file of this repo was written by another session. The GENO agent of the
  night wrote only under RDE/handoff/throat_2026-09-23/geno_rao_humphreys/.
- Handoffs (the working record, outside the repo): RDE/handoff/NOZZLE_HANDOFF_2026-09-23.md
  (S34) and NOZZLE_HANDOFF_2026-09-23_gola.md (S35, sections 8-9 = this window); figures in
  validation/_humphreys_twin/figs/10-14 with their generators in
  RDE/handoff/throat_2026-09-23/ (presentation only, not committed).
- NEXT (atomic, owner 2026-09-24): the SHROUDED PLUG to complete the suite -- first check that
  the march carries a second wall; candidates Vander Veen 1974 Table 3 (C_F of 8 shroud/plug
  pairs, contours to regenerate) and Migdal 1972's perfect annular nozzle (exact 1-D M_e 3.1107,
  C_F,vac 1.5796; GENO CASES/migdalnoz). Open on the plug line: the owner's decision on
  Panov-Shvets (BLOCCATO 20 i); a (160,41) walk; T as a design variable with the other inlet
  knobs when the inlet becomes the RDE outflow.
- Untracked artefacts of this window (declared, not committed, not deleted; the line's
  practice): validation/_humphreys_twin/ run logs and JSONs named in sections 2-3
  (tpose_gates_*, tpose_walk_*, tpose_wlog_*, run_tpose_*, kernel_*_tri_*, margin_opt_veen*,
  opt_opt_fan_veen_* of S34, raogeno.json), the S34 handoff readers in RDE/handoff/s34_2026-09-23/,
  the GENO runs (regenerable bit-identically from validation/humphreys1971_rao_geno/input.ini),
  validation/_driver_eps_ckpt.json (untracked in the main tree too; the bit-identity gate reads it).

## 7. The owner's condition and conformity

**The condition** ("sqp si dimostra in grado di lavorare sui plug"), read as [DIR-REOB] on four
references, each from ITS start:

| reference | start | tests | verdict |
|---|---|---|---|
| Humphreys Table 2 (Veen base) | their throat, the start 'come loro' | RE-1 contour <= 0.074 in, value ~1 lbf; RE-3 0.0025 in; no fold in R; (160,41) re-read | PASS |
| Humphreys Table 4 (Panov-Shvets on the state at D, their p_b scheme) | same | RE-1 <= 0.041 in, J 32,555.5 on all three starts; RE-3 to the printed digit; p_b fixed point 1.306 p_a | PASS |
| Rao 1961 (his world, GENO field, x0 0.30 m), code of today | GENO RaoPlug legacy run | O3.3 7/7; SQP return 6/6 | PASS |
| Humphreys' Rao nozzle (Table 3; GENO A3 field, x0 0.10 m, their ambient and p_b) | GENO RaoPlug by Rao's method | stage raogeno 2/2; twin PASS; O3.3 7/7; SQP return 6/6 (RAO_TR0) | PASS |

Also of record: the regressions of the record path 16/16 identical to the branch (section 3),
and the owner's check page `validation/_humphreys_twin/figs/15_reobtention_summary.png`
(generator RDE/handoff/throat_2026-09-23/reob_fig.py, presentation only).

**Conformity** (CLAUDE.md R1-R7, SR-1..SR-12, the 09-17 branch directive):
- Branch `rde-nozzle-program` (fast-forwarded from the worktree branch `tri-experiment`);
  identity AlexFalco5; explicit pathspecs; GENO never added (the worktree's GENO symlink is
  ignored). Push on the owner's word of 2026-09-24, after the commits.
- R1: `[F3/A1][S34-S35]`. R3: this log; ORA-PARALLELO / NEXT-PARALLELO reduced to the current
  state; the outgoing blocks verbatim in PROGRESS_ARCHIVE under the 2026-09-24 banner, with the
  DELTA CENSIMENTO note; R37 and BLOCCATO 20 (a, h, i) edited in place (SR-7/SR-10); HANDOFF block
  (section 6); the F3 session count measured in-window (SR-12): `git log --format=%s | grep -o
  '\[F3/A1\]\[S[0-9]*\]' | sort -u` = S26, S28-S33 (7, 72 commits), with S34-S35 = 8.
- R4: M0 Part VI, LINE ADDENDUM S34-S35, seven items with classes (section 4).
- R5 / SR-2: registry rows X-TPOS, X-IVLT, X-RAOHM (kind carrier, ondemand env=jax[+geno],
  pass 2026-09-24, suite none, falsifiers named); X-HMPH re-printed (the S34-S35 head, doc ->
  this log, its inner double quotes replaced by single quotes: they broke the PyYAML cross-check
  since S32 -- the pinned venv has no PyYAML, /opt/anaconda3's parse now succeeds); X-RAOTW /
  X-RAOO3 / X-RAOSQ re-run today and re-dated (pass 2026-09-24; the knobs unset = the record,
  the O3.3 output line-identical). SR-1: the ADVISORY_INDEX row. SR-5: no A1_* flag added
  (TPOSE_* / HMPH_* / RAO_* are instance knobs). SR-4: no new glossary token (the ids are
  registry ids; the glossary lint's unresolved count stays at its baseline 52).
- SR-6: files of record committed: `validation/a1_throat_posing.py`, `a1_ivl_triangle.py`
  (new); `a1_plug_march.py` (margin vec / region R, x_traced), `a1_plug_spline_opt.py`
  (PB_FROZEN, PSPL_WLOG, the delegation to a posing), `a1_humphreys_twin.py` (stage mderive,
  opt() knobs, HMPH_IVL=tri, stage raogeno), `a1_frame_march.py` (corner_fan ray0=, x_stop),
  `rao1961_twin.py` (RAO_PA_PC), `rao1961_o33.py` (RAO_TH / RAO_APERT / RAO_PB),
  `rao1961_sqp_return.py` (RAO_TR0); data `humphreys1971_tables.json` (_table4_recovered_rows,
  _fig4, _rao_geno_band_rel), `humphreys1971_digitised/` (the owner's Fig. 4, 3 csv + README),
  `humphreys1971_rao_geno/input.ini` (+ README); this log; the index; PROGRESS and its archive;
  M0; the registry. Every default of every knob is the record (measured: the regressions of
  section 3, JSON and md5 identical to the branch).
- Lints on the final working tree (measured 2026-09-24 ~13:15): numeric PASS (124 files, 0
  ratchet violations); advisory index PASS (127 rows, 0 violations); claims lint 4 violations,
  all "ondemand carrier file <this log> has no committed history" -- the ordering rule (the log
  lands in the first commit, the rows in the second). Full suite on the same tree: 14/23 = the
  seven environmental reds (xiii, xiv, xvi, xviii: no sympy; xix, xxii, xxiii: dead literature
  paths -- violation counts identical to the main tree's, findings 78 / literature 82 /
  glossary 4) + (xv) and (xvii) for the same ordering reason. The measurement after the first
  commit is appended below in the second.
- Two commits, as the line's practice: (1) code + data + this log + index + PROGRESS/ARCHIVE;
  (2) M0 addendum + registry + this log's conformity line. The registry commit's rows cite the
  log the first commit landed; M0's citations of the new ids land with the ids.
