# Session log 2026-09-30 — F2.ENGINE, session 3 of 6 (census R45): OPEN, order 1 done

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
| Monitor that the total temperature of the input is flat enough, with a derived limit and a loud reject | MISSING | finding problem-statement:flatness-monitor-unarmed (critical) |
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

## Where the session stands
Done: order 1. Next: order 2 (the cell check), then order 3 (the S22 bell campaign re-run).
