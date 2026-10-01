# CFD-2 — the paired demonstration (F2 close, 2026-10-01)

Plain rules: short sentences, physics before method. One page.

Decision of record: the owner's answer 3(b) of 2026-10-01 12:30-12:45 (`ADVISORY_F2CLOSE_prompt_2026-10-01.md`): the
methane table of 09-30/10-01 is the paired demonstration of the plan's CFD-2; Harroun's aerospike (JPP 2021) is
re-owned to the paper.

## What is paired
Every design is judged three ways, on the same case, with the same normalisation (C_F = wall push over P0_mean A* =
8964.6 N; walls only):
1. the design tool: the characteristics march over the 12 phases of the RDE cycle;
2. 2-D Euler CFD of each phase (MOSE_open, frozen chemistry; level c, and level f for the shrouded pair);
3. 3-D Euler CFD of the whole nozzle in the frame that turns with the detonation wave (the RDE flow itself).
Case: CH4/O2 phi 1, 20 atm mean chamber pressure (12-phase blowdown, 68 to 2 atm), THOR annulus, 0.5 atm outside.

## Table 1 — plugs (87 mm, internal cowl), gain over the textbook plug (Rao, designed at the mean state)
| design | tool, 12 phases | 2-D, 12 phases | 3-D, rotating | gain: tool / 2-D / 3-D |
|---|---|---|---|---|
| Rao (textbook) | 1.414724 | 1.412844 | 1.407115 | — |
| SQP plug, mean state, 10 segments (SaSDT) | 1.421056 | 1.419177 | 1.412733 | +0.448 / +0.448 / +0.399 % |
| SQP plug, 12 phases, 8 segments (SbSDT) | 1.419703 | 1.417788 | 1.411675 | +0.352 / +0.350 / +0.324 % |
| SQP plug + cowl, mean state, 10 segments (SjSDT) | 1.426231 | 1.424774 | 1.419340 | +0.813 / +0.844 / +0.869 % |
| SQP plug, mean state, 24 segments (Sa24SDT, 10-01) | 1.427734 | 1.425752 | 1.417983 | +0.920 / +0.914 / +0.772 % |
| SQP plug, 12 phases, 24 segments (Sb24SDT, 10-01) | 1.432445 | not run | not run | +1.253 % (tool only) |
| SQP plug + cowl, 12 phases, 10 + 10 segments (Sj12SDT, 10-01) | 1.424022 | not run | not run | +0.657 % (tool only) |

## Table 2 — shrouded plug (two walls, 133 mm), the SQP walked at the mean state against the cut ideal nozzle
| design | tool, 12 phases | 2-D level c | 2-D level f | 3-D, rotating |
|---|---|---|---|---|
| cut ideal (Migdal, TSh65) | 1.535034 | 1.522620 | 1.524489 | 1.515563 |
| two-wall SQP (SSh65, wavy walls) | 1.539009 | 1.520854 | 1.521349 | 1.513620 |
| gain | +0.259 % | -0.116 % | -0.206 % | -0.128 % |

## The bands (measured)
- Tool against 2-D, same phases: +0.10 to +0.14 % for every plug (the tool reads slightly high, by the same amount).
- Frozen phases (2-D) against the rotating flow (3-D): -0.38 to -0.45 % for the first four plugs; -0.55 % for Sa24SDT.
  Between designs the offset cancels to 0.07 % for the first four; Sa24SDT's gain shrinks from +0.91 % (frozen) to
  +0.77 % (rotating), a 0.14 % difference.
- Time scatter of the 2-D phases: <= 2e-4 in C_F (phases 7-11 are unsteady; the base never settles and is excluded).
- 3-D steadiness: wall C_F constant to <= 4e-5 over 1.5-2 ms.
- 2-D resolution (shrouded pair): the loss grows from level c to level f (-0.116 to -0.206 %): it is not a resolution
  artefact.

## What is shown
1. For the plugs, the three judges rank the five designs the same way; the gains over the textbook plug agree to
   0.05-0.15 %.
2. The tool can be wrong, and the CFD catches it: the two-wall SQP gained +0.26 % in the tool from small wall
   undulations; both 2-D levels and the 3-D run give a loss (finding twowall:tool-credits-wall-undulations). Since then
   the walls are smooth by rule (owner, 2026-10-01).
3. The frozen-phase pictures overstate the absolute thrust by ~0.4-0.55 % against the rotating flow, but they keep the
   differences between designs (to 0.07 %, 0.14 % in the worst case).

## What is not shown
- Friction, heat loss, burning in the nozzle (Euler, frozen chemistry).
- The base and the outside air: the 3-D far field (MOSE_open 406) drains the still air (finding
  waveframe:far-field-406-drains-outside-air); the base is not judged.
- The combustion chamber: the 12 phases are a model of its exhaust (Stechmann matched cycle).
- Optimality: every SQP walk was stopped by budget; the gains are lower bounds.
- Phases against mean state at equal budget, judged by CFD: the matched pairs (Sb24SDT against Sa24SDT, Sj12SDT against
  SjSDT) have the tool's 12-phase reading only (+1.25 against +0.92 percent for the plug, +0.66 against +0.81 for plug +
  cowl, the latter from a less advanced start); no 3-D by the owner's decision of 10-01 22:20, the 2-D pending.
- An experiment or a second code: Harroun's case is not built (re-owned to the paper).

Sources: `validation/_plug_contest/SDT/table_2026-09-30.{md,json}`; Sa24SDT: `RDE/handoff/plug_2026-09-29/sdt/
twop_phase_eval_sqpA24_sdt.log`, `referee_cert_sdtA24c.log`, `wf_one_Sa24SDT.log`; shrouded:
`sdt/twop_phase_eval_shroud_{TSh65,SSh65}.log`, `referee_cert_sdtsh{c,f}.log`, `RDE/Nozzle/CASE_3D/wf_{TSh65,SSh65}_phases/
wf_post.json`.
