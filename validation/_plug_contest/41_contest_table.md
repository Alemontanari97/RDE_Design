# Rao at the mean state against the SQP with the phases: the certified table (internal nozzle -10 deg, 87 mm in all)

C_F in units of P0 A* of the Stechmann mean state (619.93 N). 'Tool' = the design tool's own march (MOC, base at the ambient, Summerfield closure; a record counts when every cell is Newton-certified). 'CFD' = the referee: MOSE_open, axisymmetric Euler, one run per RDE phase, the 12 phases with equal weights; a case counts only when its thrust has settled in time (steady: last 3 dumps within 1e-4; unsteady: mean over 2..6 ms with its batch-means uncertainty). Two meshes where stated (9 044 and 36 400 cells). The headline CFD number prices the plug's cut face at the ambient, as the tool does; the base columns price it with the CFD's own pressure (Euler: indicative; read only on runs of 5 ms or more, the base settles late). A difference is a RESULT only when it exceeds the sum of the time uncertainties and of the mesh's effect on the difference.

## Ambient 0.05 bar (p_a/P0 0.0353), the design ambient

| design | method | tool: C_F mean state | tool: C_F 12 phases | tool: certificate | CFD: C_F 12 phases | mesh | time +- | unsteady phases (windowed mean) | mesh effect | CFD base p_b/p_a | base push | C_F with CFD base |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rao | Rao (GENO) at the mean state, the 87 mm length constraint active | 1.386126 | 1.324883 | ok (0.06) | 1.323801 | fine | 9.3e-09 | 0 of 12 | 1.3e-03 | 0.34 (3 phases not settled) | -0.028526 | 1.295275 |
| SQP 12 phases, Rao's freedom | SQP, the 12 phases in the objective, only the plug after the cowl lip free (Rao's own freedom), from Rao's plug; walk not converged | 1.393195 | 1.331747 | ok (0.05) | 1.330586 | fine | 2.0e-06 | 0 of 12 | 1.2e-03 | - | - | - |
| SQP mean state, first landing | SQP at the mean state, whole plug free, designed at 0.05 bar (first walk) | 1.408300 | 1.344997 | ok (0.05) | 1.343476 | fine | 3.7e-08 | 0 of 12 | 1.3e-03 | 0.45 (1 phases not settled) | -0.016651 | 1.326825 |
| SQP mean state | SQP at the mean state, whole plug free, from Rao's plug (three legs); walk not converged | 1.410437 | 1.346772 | ok (0.06) | 1.345199 | fine | 2.6e-06 | 0 of 12 | 1.3e-03 | - | - | - |
| SQP 12 phases | SQP, the 12 phases in the objective, whole plug free, from the first mean-state landing; walk not converged | 1.410940 | 1.347253 | ok (0.04) | 1.345681 | fine | 2.6e-06 | 0 of 12 | 1.3e-03 | - | - | - |

Against Rao:

| design | CFD difference | relative | uncertainty (time + mesh) | verdict | difference with the CFD base | verdict with base | common base pressure for a tie | tool's difference |
|---|---|---|---|---|---|---|---|---|
| SQP 12 phases, Rao's freedom | +0.006785 | +0.51 % | 1.1e-04 | **RESULT** | - | - | 13.7 kPa = 2.74 p_a | +0.006864 |
| SQP mean state, first landing | +0.019676 | +1.49 % | 5.6e-05 | **RESULT** | +0.031550 (+2.44 %) | RESULT | 12.7 kPa = 2.54 p_a | +0.020113 |
| SQP mean state | +0.021398 | +1.62 % | 8.5e-05 | **RESULT** | - | - | 12.5 kPa = 2.49 p_a | +0.021888 |
| SQP 12 phases | +0.021880 | +1.65 % | 3.5e-05 | **RESULT** | - | - | 12.4 kPa = 2.48 p_a | +0.022370 |

Per phase (fine mesh; the phase's weight in the 12-phase sum; a phase in brackets did not settle and is a windowed mean):

| phase | weight | Rao: C_F | SQP 12 phases, Rao's freedom minus Rao | SQP mean state, first landing minus Rao | SQP mean state minus Rao | SQP 12 phases minus Rao |
|---|---|---|---|---|---|---|
| 0 | 0.083 | 2.04869 | +0.01256 +- 8e-07 | +0.03546 +- 5e-08 | +0.03843 +- 1e-06 | +0.03947 +- 2e-06 |
| 1 | 0.083 | 1.57175 | +0.00853 +- 6e-07 | +0.02619 +- 5e-08 | +0.02869 +- 5e-06 | +0.02936 +- 5e-06 |
| 2 | 0.083 | 1.18029 | +0.00541 +- 3e-06 | +0.01738 +- 1e-08 | +0.01913 +- 1e-06 | +0.01950 +- 1e-06 |
| 3 | 0.083 | 0.92056 | +0.00341 +- 6e-06 | +0.01128 +- 9e-09 | +0.01245 +- 3e-06 | +0.01261 +- 3e-06 |
| 4 | 0.083 | 0.75410 | +0.00215 +- 2e-06 | +0.00725 +- 3e-09 | +0.00801 +- 1e-06 | +0.00804 +- 2e-06 |
| 5 | 0.083 | 0.69788 | +0.00175 +- 6e-07 | +0.00578 +- 7e-09 | +0.00637 +- 3e-06 | +0.00635 +- 2e-06 |
| 6 | 0.083 | 0.57200 | +0.00081 +- 3e-06 | +0.00282 +- 5e-09 | +0.00311 +- 4e-06 | +0.00300 +- 4e-06 |
| 7 | 0.083 | 0.48797 | +0.00018 +- 2e-06 | +0.00073 +- 3e-09 | +0.00079 +- 2e-06 | +0.00060 +- 1e-06 |
| 8 | 0.083 | 0.42527 | -0.00030 +- 3e-06 | -0.00089 +- 6e-08 | -0.00102 +- 5e-06 | -0.00125 +- 4e-06 |
| 9 | 0.083 | 2.18962 | +0.01278 +- 3e-06 | +0.04250 +- 1e-08 | +0.04705 +- 2e-06 | +0.04821 +- 2e-06 |
| 10 | 0.083 | 2.66835 | +0.01829 +- 5e-07 | +0.04739 +- 2e-07 | +0.05080 +- 3e-06 | +0.05238 +- 3e-06 |
| 11 | 0.083 | 2.36413 | +0.01581 +- 6e-07 | +0.04010 +- 9e-08 | +0.04285 +- 2e-06 | +0.04417 +- 2e-06 |
| mean state | - | 1.38497 | +0.00698 +- 2e-06 | +0.02170 +- 3e-08 | +0.02379 +- 2e-06 | +0.02431 +- 2e-06 |

## Ambient 0.2 bar (p_a/P0 0.141)

One mesh (coarse). 7 phases of 12 do not settle (the plug over-expanded): windowed means. Four cases were stopped by the solver at 3.5 - 4.4 ms (a non-physical state in the base region) and are read on the dumps they have.

| design | method | tool: C_F mean state | tool: C_F 12 phases | tool: certificate | CFD: C_F 12 phases | mesh | time +- | unsteady phases (windowed mean) | mesh effect | CFD base p_b/p_a | base push | C_F with CFD base |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rao | Rao (GENO) at the mean state, the 87 mm length constraint active | 1.181248 | 1.121759 | ok (0.03) | 1.129884 | coarse | 4.4e-04 | 6 of 12 (1 stopped early) | - | 0.81 (6 phases not settled) | -0.033799 | 1.096085 |
| SQP mean state, first landing | SQP at the mean state, whole plug free, designed at 0.05 bar (first walk) | 1.168917 | 1.108210 | ok (0.03) | 1.121430 | coarse | 2.0e-04 | 6 of 12 (1 stopped early) | - | 0.65 (4 phases not settled) | -0.042769 | 1.078661 |
| SQP mean state (0.2 bar) | SQP at the mean state, designed at 0.2 bar from Rao's plug | 1.183885 | 1.120993 | ok (0.11) | 1.128380 | coarse | 3.1e-04 | 7 of 12 | - | 0.64 (6 phases not settled) | -0.061698 | 1.066682 |
| SQP 12 phases (0.2 bar) | SQP, the 12 phases in the objective, designed at 0.2 bar from Rao's plug; stopped twice by the walk's resolution (non-finite gradients in the over-expanded phases) | 1.181042 | 1.122869 | ok (0.03) | 1.129797 | coarse | 4.3e-04 | 6 of 12 (2 stopped early) | - | 0.80 (6 phases not settled) | -0.034103 | 1.095694 |

Against Rao:

| design | CFD difference | relative | uncertainty (time + mesh) | verdict | difference with the CFD base | verdict with base | common base pressure for a tie | tool's difference |
|---|---|---|---|---|---|---|---|---|
| SQP mean state, first landing | -0.008454 | -0.75 % | 6.3e-04 (time only) | **RESULT (one mesh)** | -0.017424 (-1.59 %) | RESULT | 16.7 kPa = 0.83 p_a | -0.013549 |
| SQP mean state (0.2 bar) | -0.001504 | -0.13 % | 7.5e-04 (time only) | **RESULT, marginal (under 3 uncertainties) (one mesh)** | -0.029403 (-2.68 %) | RESULT | 11.8 kPa = 0.59 p_a | -0.000766 |
| SQP 12 phases (0.2 bar) | -0.000087 | -0.01 % | 8.6e-04 (time only) | **NOT SEPARATED (one mesh)** | -0.000391 (-0.04 %) | NOT SEPARATED | 14.3 kPa = 0.72 p_a | +0.001110 |

Per phase (coarse mesh; the phase's weight in the 12-phase sum; a phase in brackets did not settle and is a windowed mean):

| phase | weight | Rao: C_F | SQP mean state, first landing minus Rao | SQP mean state (0.2 bar) minus Rao | SQP 12 phases (0.2 bar) minus Rao |
|---|---|---|---|---|---|
| 0 | 0.083 | 1.84238 | -0.00288 +- 7e-07 | -0.00216 +- 6e-07 | -0.00012 +- 1e-06 |
| 1 | 0.083 | 1.36602 | -0.01201 +- 8e-06 | -0.00246 +- 3e-05 | -0.00023 +- 7e-05 |
| 2 | 0.083 | 0.97509 | -0.01180 +- 5e-05 | -0.00087 +- 2e-04 | -0.00014 +- 1e-06 |
| 3 | 0.083 | [0.72020] | -0.01959 +- 7e-04 | -0.00053 +- 1e-03 (tie) | +0.00035 +- 1e-03 (tie) |
| 4 | 0.083 | [0.55702] | -0.02196 +- 8e-04 | +0.00339 +- 9e-04 | -0.00016 +- 3e-04 (tie) |
| 5 | 0.083 | [0.51185] | -0.02461 +- 3e-03 | -0.00022 +- 4e-03 (tie) | +0.00047 +- 5e-03 (tie) |
| 6 | 0.083 | [0.39980] | -0.00709 +- 1e-03 | -0.00415 +- 1e-03 | -0.00009 +- 2e-03 (tie) |
| 7 | 0.083 | [0.31866] | -0.00728 +- 7e-04 | -0.00188 +- 6e-04 | -0.00024 +- 1e-03 (tie) |
| 8 | 0.083 | [0.26040] | -0.00881 +- 1e-03 | -0.00420 +- 9e-04 | -0.00076 +- 8e-04 (tie) |
| 9 | 0.083 | 1.98331 | +0.00423 +- 1e-07 | -0.00227 +- 3e-08 | -0.00008 +- 3e-08 |
| 10 | 0.083 | 2.46148 | +0.00882 +- 7e-08 | -0.00125 +- 2e-08 | -0.00000 +- 2e-08 |
| 11 | 0.083 | 2.15755 | +0.00153 +- 1e-07 | -0.00147 +- 4e-08 | -0.00003 +- 3e-08 |
| mean state | - | 1.17942 | -0.01505 +- 6e-04 | -0.00183 +- 3e-04 | -0.00014 +- 2e-05 |

## Ambient 1 bar (p_a/P0 0.706)

The design tool cannot be posed at 1 bar (pressure ratio 1.42 under the critical 1.82): the designs judged here are those of 0.05 bar, off design; only the CFD speaks. One mesh (coarse); every phase unsteady.

| design | method | tool: C_F mean state | tool: C_F 12 phases | tool: certificate | CFD: C_F 12 phases | mesh | time +- | unsteady phases (windowed mean) | mesh effect | CFD base p_b/p_a | base push | C_F with CFD base |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rao | Rao (GENO) at the mean state, the 87 mm length constraint active | - | - | - | 0.363520 | coarse | 1.1e-03 | 12 of 12 | - | 1.02 (3 phases not settled) | +0.020487 | 0.384006 |
| SQP mean state, first landing | SQP at the mean state, whole plug free, designed at 0.05 bar (first walk) | - | - | - | 0.343263 | coarse | 1.2e-03 | 12 of 12 | - | 0.99 | -0.006706 | 0.336558 |

Against Rao:

| design | CFD difference | relative | uncertainty (time + mesh) | verdict | difference with the CFD base | verdict with base | common base pressure for a tie | tool's difference |
|---|---|---|---|---|---|---|---|---|
| SQP mean state, first landing | -0.020256 | -5.57 % | 2.3e-03 (time only) | **RESULT (one mesh)** | -0.047449 (-12.36 %) | RESULT | 92.1 kPa = 0.92 p_a | - |

Per phase (coarse mesh; the phase's weight in the 12-phase sum; a phase in brackets did not settle and is a windowed mean):

| phase | weight | Rao: C_F | SQP mean state, first landing minus Rao |
|---|---|---|---|
| 0 | 0.083 | [0.97183] | -0.04459 +- 4e-03 |
| 1 | 0.083 | [0.51407] | -0.04337 +- 4e-03 |
| 2 | 0.083 | [0.26061] | -0.01279 +- 4e-03 |
| 3 | 0.083 | [0.02915] | -0.00114 +- 9e-04 |
| 4 | 0.083 | [-0.12147] | -0.00069 +- 6e-04 |
| 5 | 0.083 | [-0.17288] | -0.00011 +- 2e-04 (tie) |
| 6 | 0.083 | [-0.28877] | -0.00014 +- 2e-04 (tie) |
| 7 | 0.083 | [-0.36568] | -0.00022 +- 2e-04 |
| 8 | 0.083 | [-0.42301] | -0.00028 +- 4e-04 (tie) |
| 9 | 0.083 | [1.09769] | -0.04818 +- 3e-03 |
| 10 | 0.083 | [1.56609] | -0.04192 +- 5e-03 |
| 11 | 0.083 | [1.29025] | -0.04950 +- 5e-03 |
| mean state | - | [0.42495] | -0.00947 +- 7e-03 |

## Reading notes

1. **The SQP rows are lower bounds.** No SQP walk reached a stationary point (gradient norms 0.20 .. 0.40 at the landings; 24 to 90 segments each); every accepted step is certified and in the no-fold class. Rao's row is a closed design.
2. **0.05 bar: the SQP beats Rao, and the referee confirms the tool step by step.** Rao < SQP on Rao's own freedom (+0.51 %) < SQP mean state < SQP 12 phases (+1.65 %), the same order and the same differences (to 2 %) in the tool and in the CFD, on both meshes, steady in every phase.
3. **The phases are not what makes the difference at 0.05 bar.** 'SQP 12 phases' is ahead of 'SQP mean state' by +0.00048 (CFD, fine), but it is ahead by +0.00052 at the mean state itself: it is the further-walked design of the same hill, not a different optimum. The ratio C_F(12 phases) / C_F(mean state) is 0.95487 and 0.95488 for the two (CFD, fine): the phases' own effect on the ranking is of order 1e-5. The two plugs differ by 0.3 mm at the tip. The gain over Rao comes from the SQP's posing (the ambient, the finite length and the truncation inside the objective, the whole plug free), not from the phase model.
4. **0.2 bar: Rao is not beaten.** Rao's member of this length is, by its own lip condition, the optimum of an ambient of 0.164 bar: it sits at its design point. The mean-state SQP at 0.2 bar improves the mean state (+0.0026, tool) and LOSES under the phases (tool -0.0008, CFD -0.0015): here the phases matter and the mean state misleads. The SQP with the phases, started from Rao's plug, gains +0.0011 in the tool and ties in the CFD (-0.0001 +- 0.0009); its walk was stopped twice by the tool itself (non-finite gradients: the over-expanded lip of phases 6-8 has no model). One mesh, unsteady phases, four cases stopped early by the solver: the 0.2 bar verdicts are indications.
5. **The base.** The tool and the headline CFD number price the plug's cut face at the ambient. At 0.05 bar the CFD puts a LOWER pressure on Rao's larger base (p_b/p_a 0.34 against 0.45, fine; 0.24 against 0.50, coarse): with the CFD's base the SQP's margin grows (+1.49 % -> +2.44 %); a tie would need a common base pressure of 2.5 p_a. Rao's plug is not helped by the convention at its losing ambient. At 0.2 bar Rao's lead over the 0.05 bar SQP design (0.0085) is of the size of the base terms: it would vanish with a common base pressure of 0.83 p_a and it doubles with the CFD's own (unsettled) base pressures; against the 0.2 bar SQP designs the bases are equal in area and the base plays no role. At 1 bar the base sits at the ambient and plays no role. The Euler base pressure is mesh-dependent and indicative.
6. **1 bar, and the bare exit.** Rao's plug is ahead of the 0.05 bar SQP design by 5.6 % (one mesh), made entirely in the high-pressure phases; phases 4-8 give negative thrust for both. The bare exit (no nozzle: the inlet's momentum and pressure against the ambient, 12 phases) gives 1.2392 at 0.05 bar, 1.1081 at 0.2 bar and 0.4091 at 1 bar: the plugs add +6.8 % (Rao) to +8.6 % (SQP) at 0.05 bar, +2.0 % at 0.2 bar, and at 1 bar either plug is WORSE than none (-11 % and -16 %).
7. **What the referee does not judge.** The CFD shares the tool's quasi-steady model of the phases (one steady inflow per phase, axisymmetric): it certifies the tool's fluid dynamics, not the phase model. A 3D unsteady run (laboratory or wave frame) is the judge of record for that.

Records: CFD tables `RDE/THOR/THOR_GPU/NOZZLE_2026-09-27/CASE_2D/cert_{long005,fin005}{c,f}_table.json`, `cert_avg020c_table.json`, `cert_avg1bc_table.json` (per case `cert.json`); tool records `RDE/handoff/plug_2026-09-29/twop_phase_eval_*.json`; designs `design_*.json`, `start_rao_b10.json` there; profiles `41_contest_profiles_b10.png`.
