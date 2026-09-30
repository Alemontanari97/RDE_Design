# Session prompt — F2.ENGINE (F2 session 3 of 6), written at the close of F2.REPR, 2026-09-30

Plain rules: short sentences, physics before method. Single author: the session opens by checking this prompt
against the plan (D6 F2 text and its notes), the derived roadmap and PROGRESS.

## What F2 must deliver to close (D6, F2a and F2b)
A flow solver for the design tool that accepts the RDE outflow as it is: a state that changes from phase to phase
and, when the source provides it, layers of hot and cold gas across the annulus, each keeping its own entropy and
total enthalpy along its streamline. With: checks that the input data are physically consistent, a check that stops
a design when waves of one family start to cross (a shock forming), a gradient exact to machine precision, agreement
with GENO where GENO can run the same case, and the methods frozen for the paper.

## Decided before this session (do not reopen)
- Design per phase, axisymmetric, no swirl; final designs checked with the free-vortex swirl; the difference between
  designs judged by 3-D CFD in the frame turning with the wave (F2.REPR, owner, 2026-09-30).
- No second optimiser, no rival search pilot for now (owner, 2026-09-30).

## Orders, in this order
1. INVENTORY. The plug line built engine parts while the plan was on hold: a march for layered inflow
   (`a1_rot_march.py`, gradient check `o31_rot.py`), swirl cells (`a1_swirl_march.py`), the free jet at the lip
   (`a1_lipjet.py`), gas tables per phase, the separation closure, the fast replay (`a1_wavefront_replay.py`), the
   two-wall optimiser (`a1_twowall.py`). One table: each exit item of F2a and F2b -> exists (file, its check, date of
   the last pass) / partial / missing. Nothing is rebuilt before this table is on file.
2. THE CELL CHECK. Today a cell passes if its last correction is below a multiple of machine rounding. Near the
   axis that line is below what the arithmetic holds and the verdict is noise (one design: 1.20, 0.46, 2.07 with
   three solver variants). New rule: a cell passes when its remaining error is small against the mesh error at
   that cell, and the solver must be seen converging. Show that it still rejects a cell that truly did not
   converge (planted), and that the verdict no longer changes with the solver variant.
3. ONE BELL CAMPAIGN RE-RUN (the S22 case) with the new check. Read what stops it: the physics (waves crossing), the
   optimiser, or nothing. Only if it stops short again is the rival search pilot reconsidered.
4. The items inherited from the F2.REPR carrier, order 7 (`ADVISORY_F2REPR_prompt_2026-08-31.md`): the interior-point
   comparison input, the objective-domain guard before any verdict that uses the throat-angle gradient, the
   re-forms of X-O32 and X-LOCD, the flatness monitor of the data contract, the two armed rejectors.
5. The smallest step of the walker derived from the measured distance to the validity limit (finding
   driver:smallest-step-larger-than-distance-to-the-validity-limit).
6. Closing: PROGRESS (counter 3/6), lints, suite, commit.

## In parallel, not part of this session's counter
PILOT-WF (first campaign of F2.M-RED): one plug of S42, one ambient, 3-D steady in the frame turning with the wave
(MOSE_open rotating frame, on the cluster) against its 12 per-phase runs. Known obstacles: the mapped-inlet
boundary condition has no rotating-frame handling (use a per-cell supersonic inlet taken from the outflow at each
angle); the still ambient moves at relative Mach 5 to 12 in that frame and its relative total temperature exceeds
the gas tables beyond a radius of about 100 mm (shrink the outer domain). Launching 3-D runs is the owner's decision.

## Exit criteria
E1 the inventory table on file. E2 the new cell check with its two demonstrations. E3 the S22 re-run read.
E4 every F2a / F2b exit item either met with its check or listed with an owner and a date. E5 PROGRESS, lints,
suite, commit. Budget: 3 hours of decisive runs. Orchestration: 0 subagents unless the owner says otherwise.
