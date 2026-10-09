# Session log 2026-10-07 .. 10-09 — the revalidation of the rde-nozzle optimiser and the registry triage (census R46)

Plain rules for this log: short sentences, one fact per line, physics before method. Detail of 10-07/08 in the
harness: `validation/_revalidation_2026-10-07/HANDOFF_2026-10-08.md`; deliverable `doc/slides.pdf`; triage
`doc/TRIAGE_2026-10-09.md`.

## Opening (R2, R8)
- Phase F3 (F3.TWIN opened 2026-10-05, e32835a; F2 closed 2026-10-02, stamps 071a24a).
- Owner's order, 2026-10-07: revalidate the SQP model from scratch; every result before it is not trusted; Rao's
  method on the same problem is the optimum (a landing above it is a defect on our side); every miss explained with
  equations and in plain words; one document. Added 2026-10-08: cover the bells; the tool must find optima AGNOSTICALLY
  (one default setting, no per-case knobs); the document is a slide show, case by case; no code names; every figure
  shows what OUR optimiser obtains; Rao against Humphreys against our solver.
- Consumer: the owner. Exit criteria: (1) known optima re-obtained from at least two distant starts with one setting,
  every miss explained; (2) the slide show with every number generated from the measured files; (3) the registry
  triaged, every surviving carrier re-run with the code to be committed; (4) nothing committed without the owner's go.
- Orchestration: 0 subagents, 0 workflows. s2 shared: at most 12 niced threads in total (7 used at most on 10-09).

## 2026-10-07/08: what was measured (harness tests t01-t24)
- The model against exact solutions and GENO: cells (order >= 2.7), the planar lip expansion, the axisymmetric source
  channel, GENO's Migdal walls and Rao field, the derivatives on the production posing, the 12-phase objective, Rao
  1961 and Humphreys 1971 tables by an independent solver of Rao's equations and by GENO, the bell engine against
  GENO's two bells. Two defects of the model found and fixed: a damped-Newton stall at horizontal C+ characteristics
  (rescue, default since 2026-10-08) and the former driver's stall on steep plugs.
- The agnostic driver `validation/a1_qntr.py` (default of run_trsqp since 2026-10-08; PSPL_DRIVER=legacy restores
  the former one): quasi-Newton trust region on the true march, every trial marched and certified.
- Results, two distant starts per case, finest grid, ppm against the known optimum (closest curve of the design class
  in brackets): planar ideal plug -10.3 (-9.0); methane Rao -2.11/-2.18 (-0.24); Rao 1961 -1.30/-1.35 (-0.43; former
  driver -8.9/-14.3); ideal spike -3.31/-3.47 (-2.31); Humphreys 1971 -0.90/-0.91 (-0.89; their method -58); Migdal
  two walls -1.33/-1.32; bell TOC +0.34/+0.35 over its closest curve on the grid twice as fine. Checks 57/60: the three
  failures are the ideal bell, whose second strict local maximum is proven for the computed thrust and open for the
  continuous problem.

## 2026-10-09: the owner's triage and the re-runs
- Questions answered to the owner before deciding: which of the flagged carriers the revalidation redid; how
  Humphreys was redone without their throat (their own last test starts from a characteristic of Rao's field, and so
  does ours; GENO's designed plug is identical for inflow Mach 1.1-2.0 within 2e-7 R_E); why their fixed-inlet optimum
  is not Rao (a different problem: their real throat against Rao's ideal sonic line, plus friction, about 70 lbf).
- Owner, after the proposal: "procedi con l'ordine e le priorita' da te date. Per il commit finale aspetta il mio nulla
  osta."
- The lint flags 46 carriers (an earlier count said 40; six more: X-AFAN, X-LJET, X-OWNM, X-PTRN, X-RDET, X-TWOP).
  Decision per carrier, reasons and numbers: `validation/_revalidation_2026-10-07/doc/TRIAGE_2026-10-09.md`.
- Model tests re-run with the committed defaults, each with a rejector (a corrupted variant that must fail the check
  it mirrors): t01 39/39, t02 17/17, t03 10/10, t04 13/13, t05 21/21 (the stalled cell of 10-07 certifies with the
  default rescue), t05b 5/5, t06 6/6, t07 20/23 (the 3 failures: the 12 phases at the posing's reference design, where the march is not certified, as on 10-07; the 12-phase derivatives are certified by t07b), t07b 7/7, t09 19/21 (the two misses are the
  paper's printing), t16 6/6.
- A rejector that did not fire is a finding about the check: on t03 the thrust does not see a 2 percent error of the
  jet's ambient (the plug downstream of the fan is axial); the rejector moved to the jet edge, which sees it.
- Old verifiers re-run with today's code (artifacts in the harness `logs/old_art/`, equal field by field to the working-tree records of 10-02, times excepted; they replace them in the canonical paths at the commit):
  X-PMRG 11/11, X-PLUG (plug march 6/6, swirl march 9/9), X-THC1 PASS, X-VMON PASS, X-BPRS 10/10, X-CHTW 8/9 (as at
  record), X-AFAN 8/8, X-RMAR 9/9, X-O31R PASS.
- The eight slide readings t17 re-run WITHOUT their ladder cache: identical to 2026-10-08 value by value (the slides do not change); the reading-based carriers are stamped 2026-10-09.
- The tool's code is the revalidated one: no validation/*.py changed after 2026-10-08 22:05 (the three files of the revalidation: a1_ideal_march_jax.py and a1_plug_spline_opt.py 10-08 12:12, a1_qntr.py 10-08 22:05, report fields only); the old verifiers ran unchanged (only their artifact folder redirected by their own variables). Check: the certified planar walk B0 re-run today with the current driver (output redirected, the record untouched) equals the record of 10-08 bit for bit (landing, history, stop CONVERGED, 5 records, 2 secants); the report only gains the diagnostic fields. Changed today: the test harness only (rejectors; t05b's explicit rescue switch; t03's rejector moved to the jet edge; t07's rejector on the mean state, NaN not counted as a detection).
- Registry: 15 carriers re-pointed (same IDs), 9 re-stamped, 22 retired (fail=2026-10-09, owned by the OPEN finding
  revalidation:carriers-retired-2026-10-09), 4 new (X-RVGAS, X-RVGRD, X-RVPHS, X-RVBEL, the last declared failing and
  owned by bell:ideal-bell-second-top-open). Nothing deleted: the IDs are cited 182 times in docs/*.md, 73 in the
  append-only archive.
- Theory (R4): M0 gains the dated revalidation block (driver, rescue, what is certified, the second top, the rejector
  lesson, the triage).

## Deviations from the plan (declared)
- The revalidation ran on the owner's order between F3.TWIN's opening and its arms' final runs; it re-certifies the
  tool F3.TWIN depends on.
- The owner parked the SDT constant-Mach inlet on 2026-10-07 ("l'entrata a mach costante non e' realistica"); the
  instance amendment A-INST had pinned F3.TWIN on methane case A, which uses that inlet. DECIDED by the owner on
  2026-10-09: "L'entrata SDT o THOR sono state rimpiazzate dalla nuova pratica di usare il vero OUTFLOW di un nozzle come
  input, percio' possono essere scartati." The decisive comparison's inflow is the real outflow (the Q2D-HP line);
  A-INST's instance and the THOR rehearsal (B-TWIN-PROVA) are superseded. Kept: the validation tests that use the SDT
  gas only as a test gas (model and reference on the same gas: t01, t03-t06, the methane Rao case), and t07/t07b as
  checks of the derivative machinery on the SDT posing, to be re-run on the real-outflow posing when it exists.

## The commit (awaiting the owner's go) and the day-granular staleness
- The claims lint compares the DAY of the last commit touching a carrier's import closure with its pass date. Every
  proof is stamped 2026-10-09: a commit today needs nothing more; on a later day re-run the proofs that day (about 45
  minutes in two waves), stamp, commit the stamps.
- Pathspecs only (never `git add -A`); GENO/ never; the GENO run outputs of the harness (4.7 GB), its logs and the
  PDF/figures stay out unless the owner says otherwise. Not mine and left untouched: the other sessions' uncommitted
  edits (PROGRESS_2026-10-05_F3TWIN.md, TWIN_PROTOCOL_preregistration_2026-08-31.md, `_q2d_hp_*`).

## Commit-day checklist (do in this order, only after the owner's go)
1. If the day is not 2026-10-09: re-run every proof that day (two waves inside the 12-thread cap: model tests and old
   verifiers, then the t17 readings without their ladder cache) and re-stamp the registry.
2. Copy the re-run artifacts `validation/_revalidation_2026-10-07/logs/old_art/<script>/*` into the canonical paths
   (`_plug_margin/derive.json`, `_axi_fan/derive.json` + `oracle_walls.npz`, `_base_pressure/derive.json`,
   `_chutkey_twin/derive.json`) BEFORE `git add` (the canonical files hold the 10-02 content, equal except for times).
3. Stage the 76 tracked deletions of `validation/_plug_contest/SDT` with `git add -u -- validation/_plug_contest/SDT`.
   `git checkout --` the five suite-regenerated files (data/phase_diagram.*, data/q_mapping.*,
   figs/phase_diagram_op11.png), as approved by the owner.
4. `git add` the commit set by explicit pathspecs only (list `validation/_revalidation_2026-10-07/logs/commit_set_2026-10-09.txt`; 404 paths, 4.6 MB: code,
   harness tests/ref/doc sources/out JSONs/run scripts, GENO decks + the outputs' md5 manifest, registries, M0,
   PROGRESS + archive, ROADMAP, this log, the index, the numeric baseline). Not GENO/, not the GENO run outputs (8 GB),
   not the logs, not the PDFs and figures unless the owner says so.
5. Commit message with the phase tag `[F3.TWIN][PIANO/R46]`; then the fast suite in a clean copy (green except the
   environmental reds xiii, xvi, xix, xxii, xxiii, measured 2026-10-09: sympy absent, literature PDFs and GENO/ not in
   git). No push without the owner's word.
6. Owner's decisions still open for the other sessions' files (left untouched): the 10-02 artifacts of retired
   carriers (`_frame_march`, `_humphreys_twin`, `_ourworld`, `_ourworld_nominal`, `_rao1961_posing`, `s25_spdb_m0.json`)
   and the F3.TWIN session's files of 10-05/06 (`_plug_contest/SDT/*`, `_twowall*`, `twowall_inlet_family*`).

## Commit and quick regression (2026-10-09, owner's go: "ok possiamo committare")
- Commit b5ccf96 (480 files: 388 added, 76 deleted, 16 modified; tag [F3.TWIN][PIANO/R46]); after it the claims lint
  has 0 violations (every stamp fresh) and the fast suite on a clean copy of HEAD is 15/20 with the five
  environmental reds of before.
- THE QUICK REGRESSION (owner, 2026-10-09: "prove rapide ed indicative che ci permettano di certificare possibili versioni future con casi passati"): validation/_revalidation_2026-10-07/tests/quick_regression.py, carrier X-RVQCK, run by every full suite (on-demand tier, about 7.5 minutes on one core, nothing written into the repository). It re-runs the fast model checks (gas, cells, the papers' tables) against their certified verdicts, re-marches every certified landing of the eight optimiser cases on its walk grid against the certified thrust (IDENTICAL / DRIFT / CHANGED, the band = a tenth of what one grid doubling does to the same gaps in the certified reading), re-runs the certified planar walk bit for bit, and must catch a rejector (the planar landing on the next grid). Rule for a future version: no case CHANGED; a DRIFT case is quoted only after its full protocol is re-run; a CHANGED case is re-certified with its full protocol.

## HANDOFF
- State: committed (b5ccf96, then the quick regression); push never without the owner's word.
- Next atomic step: F3.TWIN on the real outflow (the Q2D-HP line); every future version of the tool passes the quick
  regression first.
- Done on the owner's yes ("per quei 3 hai il mio si"): X-CYCF retired; `RDE/handoff/plug_2026-09-29/sdt` (985 files,
  31 GB) and `validation/_plug_contest/SDT` (96 files, 76 tracked) deleted; X-FRES noted (its SDT inputs are gone).
- Open: the ideal bell's second top; the shape-mode margin that does
  not see converging characteristics (finding twowall:shape-margin-blind-to-convergence, F3.PLUG critical).
