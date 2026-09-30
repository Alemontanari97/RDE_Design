# Session log 2026-09-30 — REUNION AND ORDER (service window, census R43)

Plain rules for this log: short sentences, one fact per line, physics before method.

## Why this window exists
Since 2026-08-23 the repository has two lines that never met.
- Plan line (`origin/wip_alessandro_pre_alex`, 25 commits): ESA presentation closed, derived roadmap, F2 opened
  (block 0 done on 2026-09-05, session 1 of 6), foundations review suspended on 2026-09-05.
- Plug line (`rde-nozzle-program`, 119 commits): the plug nozzle work S26-S41, F3 opened and closed on 2026-09-24.
The owner, 2026-09-30: keep what was done, go back to the plan, close F2; the repository rules decide; clean the
`validation` folder and the language.

## Declared start (R2)
Out of phase: a service window before the plan's next step (resume the foundations review, then F2.REPR).
It consumes no F2 session. Roadmap step served: F2.REPR (it cannot open on a split repository).

## Gate-first declaration (R8)
- Consumer: the owner, and the next session that resumes the plan from ONE branch.
- Exit criteria:
  1. the night's plug work (log S42 `PROGRESS_2026-09-29_S42_internal_nozzle.md`, the opt-in options, the certified table and figure) committed on
     `rde-nozzle-program`, lints green, suite quoted;
  2. the two lines merged into one local branch; every lint of both lines green or red only for a named
     machine reason; derived roadmap regenerated;
  3. `validation/`: no untracked file left; each file is either a cited record (committed) or deleted;
  4. PROGRESS says where the plan resumes; the owner's ratifications listed in one place.
- Orchestration ceiling: 0 subagents.
- No push.

## Done so far (2026-09-30 afternoon)
- The pre-registered protocol of the decisive comparison read against the night's Rao-versus-SQP table:
  the table is a rehearsal, not the decisive comparison (inflow description not fixed by F2.REPR, case not fixed
  before the runs, RDE outflow from a hydrogen CFD instead of the methane case of the protocol, exit area and
  truncation free in one arm only, classical arm taken from GENO instead of the same engine).
- Trial merge in a separate worktree (`RDE_Design_reunion`, branch `reunion-f2-plug-2026-09-30`), staged, not
  committed: 8 files in conflict, all resolved as plan text plus the plug line's additions; no registry entry was
  created twice; the plug line's census rows R37, R38 become R41, R42.
- What the merged tree still fails: 20 plug-line checks lack the machine fingerprint required since 2026-08-31;
  12 plan-line checks must be re-run because the plug line changed shared files; 10 open plug-line findings have no
  critical-path label; 13 glossary terms; 2 numeric-lint rows.
- `validation/` measured: 475 untracked files, 383 cited by no log or script (228 throat-kernel scans, 138 plug
  walk folders and logs, 12 Hessian scratch, 5 others).

## The `validation` folder cleaned (owner's decision: what no log cites is deleted)
- Deleted: 298 untracked files, 2.8 MB, cited by no log and read by no script: throat-kernel scan outputs of S32-S35
  (declared "not committed" in the S32 log), old plug-walk folders of the first posings, Hessian scratch, smoke logs,
  checkpoints of closed walks, cached arrays. All are outputs of committed scripts and can be produced again.
- Kept and to be committed: the 14 numbered figures (they are what the owner looks at), and every file a log cites.
- Walk folders of record for the internal-nozzle comparison (`_plug_contest/L87/`): `AcowlB_intnoz10_plug` (first
  mean-state landing), `AcowlB_intnoz10_fromRao`, `AcowlB_intnoz10_fromRao2`, `AcowlB_intnoz10_fromRao3` (mean state
  from Rao's plug, three legs), `AcowlB_intnoz10_fromRao_pa020` (mean state at 0.2 bar), `BcowlB_intnoz10_fromA`
  (12 phases), `BcowlB_intnoz10_ext_fromRao` (12 phases, only the plug after the cowl lip free),
  `BcowlB_intnoz10_fromRao_pa020`, `BcowlB_intnoz10_fromRao2_pa020` (12 phases at 0.2 bar),
  `BcowlB_intnoz10_joint_fromRao_pa020` (plug and cowl together at 0.2 bar, first leg), `AcowlB_intnoz5_plug`,
  `AcowlB_intnoz14_plug` (the other two injection angles, mean state only).
- Still running at 15:40, stopped or ended later and recorded below: `BcowlB_intnoz10_fromA2`,
  `AcowlB_intnoz10_fromRao4`, `BcowlB_intnoz10_joint_fromRao2_pa020`; stopped at its checkpoint to free the machine:
  `BcowlB_intnoz10_ext_fromRao2`.

## The merge (branch `reunion-f2-plug-2026-09-30`, not yet on `rde-nozzle-program`)
- Plug work committed on `rde-nozzle-program`: 4d26d66 (S42) and e27b693 (this window's opening). Own checks on
  the default path PASS (ideal march, plug march 6/6, RDE tournament 9/9); lints green; suite quoted in 4d26d66.
- Merge of the plan line: 8 conflicts resolved by `RDE/handoff/plug_2026-09-29/reunion_resolve.py` and
  `reunion_progress.py` (plan text, then the plug line's additions).
- PROGRESS rebuilt on the plan's slim form. It now says: F2 open, session 1 of 6; F3 opened and closed on the plug
  line out of order; next = close the foundations review on what is on file, then F2.REPR.
- Census: the plug line's R37, R38 are R41, R42. This window is R43.
- The derived roadmap no longer marks the decisive comparison as done: F3.RK1 and F3.PLUG closed on the plug line,
  F3.TWIN and F3.TOURNAMENT not run.
- Registries: the plug line's 31 check stamps carry this machine's fingerprint; 10 open plug findings labelled
  (3 critical: the optimiser stalling from far starts, the validity margin blind to converging waves, GENO's Rao
  plug building its own inlet); 5 findings of S42 added; 13 labels resolved in the glossary; 2 plan-line scripts
  given their numeric baseline rows; theory document: registration block S42.
- Lints on the merged tree: numeric PASS, advisory index PASS, roadmap PASS, glossary at its baseline (its 4 reds
  and the findings lint's reds are files this machine does not have: literature PDFs, GENO sources).

## Owed before the merge moves to `rde-nozzle-program` (the claims lint is red for these)
- 12 checks of the bell sector are old by the plan's rule (a file they import changed after their last pass):
  X-THC1, X-SCANM, X-LSG0, X-TOCV, X-O33B, X-CDKAT, X-VMON, X-MGOV, X-TBAK, X-DEFTW, X-SPDB, X-O31CS. Re-run each
  on this machine and stamp it.
- 7 checks were last passed on the other machine (fingerprint e100f996): X-SCANM, X-O32, X-AKNO, X-CDKAT, X-LOCD,
  X-TBAK, X-STSC. Re-run here, or declare the two machines.
- Then: full suite on the merged tree, fast-forward `rde-nozzle-program`, remove the worktree.

## The checks re-run on this machine (2026-09-30 afternoon; logs in `RDE/handoff/plug_2026-09-29/carriers_2026-09-30/`)
- Passed and stamped with today's date and this machine's fingerprint (10): X-VMON, X-CDKAT, X-THC1, X-O31CS, X-TBAK,
  X-MGOV, X-STSC, X-SPDB, X-TOCV, X-O33B.
- Re-run and failing as already recorded on 2026-09-05 (3): X-O32, X-LOCD, X-AKNO. X-LOCD fails because the design
  returned by the S22 campaign no longer passes the cell check (1.20 against a pass line of 1): the noise near the
  axis described in the review's closure (LOG-11).
- Re-run and not passing for reasons of the machine (3): X-SCANM (the system's cap on memory mappings is hit while
  compiling), X-LSG0 (needs a quiet machine; the shared machine ran at load 66), X-DEFTW (a GENO case is missing in
  this machine's GENO). Declared failing here, with a finding that owns them.
- A re-run overwrote one recorded measurement file (`validation/s25_spdb_m0.json`); restored, this machine's output
  kept aside.
- The last plug walks were stopped or ended: 12 phases 1.34844 (segment 15, stopped), mean state 1.41733 (ended by
  its budget), 12 phases on Rao's freedom 1.33437 (stopped), plug and cowl at 0.2 bar 1.12373 (stalled, stopped).
  None reached its optimum.

