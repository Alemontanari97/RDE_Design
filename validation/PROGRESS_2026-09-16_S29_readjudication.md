# S29 — Re-adjudication of the free-form spike (S22/S23) with the amended instruments, and the closing of the S28 night (2026-09-16, continuation of S28 after midnight)

Tag [F3/A1][S29] (brick-2 plug line, branch `brick2-plug`). Written in
its own log because the claims lint's staleness link binds a carrier's
pass-of-record date to the last commit touching its `doc`: the S28 log
(`PROGRESS_2026-09-15_S28_ourworld.md`, four rows stamped 2026-09-15) is
FROZEN as committed in 5105457; everything after midnight lives here.
Read the S28 log addenda A/B first (the measured attribution of the
SQP-return P3 failure, the v3 instrument, the (121,101) sweep, the fold
finding); the 20:23 chain is described there and closed here.

## 1. S22 v2 — the amended carrier's run of record (closed 2026-09-15 23:57)

`validation/a1_plug_adaptive.py` amended (declared in its docstring):
every rung of the A-8/A-9 ladders is a measurement only if BOTH marches
certify; an uncertified rung makes the ladder VOID and the verdict FAIL
by discipline; artifact dir configurable (`PAKN_ART`). Run of record
`validation/_plug_adaptive/rerun_S22_2026-09-15b.log` (12834 s, same
posing as the 18:28 re-run: PAKN_M0 10, K 61, N 51, 3 cycles, 2
insertions, ITERS 30, CONTROL 1; artifacts in `_plug_adaptive_v2/`,
removed after the check below): **11/13** —
- DETERMINISM: `design` and `class0` identical to the 18:28 re-run
  (checked field by field by `regen2_driver.sh`: True). The design of
  record is therefore the m 12 design of 18:28 (`design.json` /
  `design_m10_k61_n51.json`, J 1.16199981e8 at (61,51), knots 0.4037 +
  0.4575 + 10 uniform), committed here.
- A-8 THE VERDICT: FAIL, **ladder VOID** — rung (121,101) adaptive
  cert 3.25e11 (the first-column edge cell, S28 addendum B), rung
  (241,201) INCUMBENT cert 1.59 (marginal: the margin degradation S23
  had booked for rungs >= 4 reaches rung 3 for the streamline); the
  printed gain +0.429 % (band 1.04 %) is not trusted.
- A-9 THE CONTROL: FAIL, ladder VOID — the uniform m 12 control's
  rung (241,201) cert 16.7.
- A-1..A-7 PASS as before (A-4 certifies the design at its own
  resolution only — that is the gap the fold finding exposes).
Reading of record: with the gate in place the S22 carrier says what it
could only imply before — its ladder cannot grade these designs,
because the designs it produces leave the march's certified class
(compression corner at the foot, tangled net downstream; S28 addendum
B). [X-PAKN] re-stamped from this run; the 08-10 log stays as history.

## 2. S23 re-adjudication — in flight at the time of writing

`validation/a1_plug_gain_resolve.py` amended (R-2c: the warm start must
certify at the fine instrument, else the declared fallback; see S28
addendum B). Chain `regen2_driver.sh` (20:23): S23 default 5/5; fineopt
warm start FELL BACK to the fan streamline on the S22 knots (cycle-2 m 12
cert 3.25e11, cycle-1 m 11 cert 4.17 at (121,101), both printed), then
TR-SQP at (121,101) with PGRS_ITERS 40 — at 00:12 at segment 26, J
1.15809e8 -> 1.16280e8 (+0.41 %), radius ~4e-3, converging. Then rungs
4-6 x inc/fine (six parallel processes), verdict, design_fine, figures,
build. Outcome, the fold census of the fine optimum and the re-stamp of
[X-PGRS] go in Sec. 4 below when the chain closes.

## 3. Declared
- The S22 log of 08-10 and the S23 log of 08-11 are HISTORY (their
  designs were produced by the pre-S23 driver and are not reproducible;
  the record's design vectors are lost since the 09-04 deletion); the
  runs of record for the amended carriers are the 2026-09-15/16 logs.
- `_plug_adaptive/design.json` and `design_m10_k61_n51.json` are the
  same design (the carrier writes the tagged name, `make_figures.py`
  reads the legacy one); both committed, duplication declared.
- The rerun logs of the first pass (`rerun_S22_2026-09-15.log`,
  `rerun_S23_*_2026-09-15.log`: the un-amended instruments, the crash
  at fineopt) are committed as the evidence trail of addendum B.

## 4. Closing of the chain
(filled when `regen2_2026-09-15b.log` says ALL DONE)

## 5. NEXT (plan drafted with the owner 2026-09-16 00:30; see the
## PROGRESS ORA/NEXT-PARALLELO blocks)
(filled after the discussion)
