# Session log 2026-09-30 — F2.REPR: how the flow is described (F2 session 2 of 6, census R44)

Plain rules for this log: short sentences, one fact per line, physics before method.

## Opening (R2, R8)
- Read: START_HERE, the review's assessment (GO for this step), PROGRESS, the plan's F2 text and its addendum of
  2026-09-05, the derived roadmap (regenerated, its lint PASS). Phase F2, step F2.REPR, critical path.
- Consumer: whoever builds the engine next (F2.ENGINE) and whoever runs the decisive comparison.
- Exit criteria: the carrier's E1-E6 (`ADVISORY_F2REPR_prompt_2026-08-31.md`).
- Orchestration: 0 subagents. The carrier proposed a census with one advocate per option and a refuter (4-6 agents).
  NOT RUN: the owner decided the four opening questions directly, and their answers are the step's declared
  fallback plus one choice of judge. Declared deviation from the carrier.

## Check of the carrier against the record (its order 1, done inline)
- Its counts are those of 2026-09-05; re-measured today by the roadmap tool (235 open findings, 24 blocking rows).
- It assumes the review's assessment exists with a GO: true since today (closed on file, not refereed).
- It does not know the plug line: the free-vortex swirl cells, the per-phase CFD referee and the RDE outflow cut
  into phases already exist; the wave-frame judge is available as a CFD option. Its cost estimates for the
  five-field engine and the wave-frame solver are therefore upper bounds for what is needed now.
- Its field reading is on Harroun's aerospike figures. Replaced here by our own RDE outflow (below); Harroun's
  figures not read in this session (declared).

## What the RDE outflow looks like (our own field: Q2D THOR run, exit plane, one instant = one full wave)
| feature of the flow | size | design description (per phase, axisymmetric, no swirl) | swirl check (free vortex per phase) | judge (3-D, frame turning with the wave) |
|---|---|---|---|---|
| total pressure changes along the wave | factor 7 between phases (0.46 to 3.1 bar) | carried | carried | carried |
| static pressure at the exit | 0.13 to 0.93 bar | carried | carried | carried |
| axial Mach number | 1.44 to 1.84 | carried | carried | carried |
| flow direction off the axis (swirl) | -34 to +25 degrees, net zero, 8 percent of the kinetic energy | LOST | approximate: each phase a swirling axisymmetric flow | carried |
| gas moving sideways between neighbouring phases inside the nozzle | 3 to 4 phases share an 87 mm nozzle | LOST | LOST | carried |
| time the gas needs to cross the nozzle against the wave's passage | ratio 0.7 to 1.4 on the truncated plug | LOST (frozen pictures) | LOST | exact for one wave turning rigidly |
| layers across the annulus (hot and cold gas side by side radially) | absent in this 2-D source; present in 3-D runs | not needed for this source | - | carried |
What the swirl does to thrust, measured on the plug line (S41): the free vortex per phase lowers the 12-phase thrust
by 0.2 to 0.3 percent and detaches the flow in three low-pressure phases of every design.

## The owner's four decisions (2026-09-30)
- T1 swirl: DESIGN WITHOUT SWIRL; check the final designs with the free vortex per phase. The five-field engine
  is not built.
- T2 judge: 3-D CFD in the frame turning with the wave (MOSE_open, rotating frame). No wave-frame marching solver.
- T3 other search strategy (explore freely, certify at the end): NOT NOW. First the cell check is repaired.
- T4 second optimiser (Uno): NOT INSTALLED. The Python environment stays as it is.

## The verdict
ONE description for both arms of the decisive comparison:
- both arms are DESIGNED per phase, axisymmetric, without swirl (the engine's four fields); this is the step's
  declared fallback;
- both final designs are CHECKED with the free-vortex swirl per phase;
- the difference between the arms is JUDGED on one evaluator: the 3-D steady flow in the wave's frame by CFD.
  It is a measure, not certified by the engine's own checks. It becomes the judge of record when PILOT-WF has
  shown that it reproduces the laboratory-frame thrust of one plug.
What this costs: no new engine. What it leaves out of the design: swirl and sideways transport (seen only by the
judge). If the judge moves the difference between two designs by more than one third of the thrust-stand band, the
swirl must enter the design (trigger for the five-field engine).

## Landed
- Ledger: C49 DECIDED (the design marches with fitted waves; the captured solver is the judge), C51 DECIDED (no
  wave-frame marching solver now; re-owned to F6), C59 DECIDED (cycle average for the design, steady wave-frame
  flow for the judge; other time forms re-owned to F5b), C57 note (no pilot now).
- Blocking rows: B-S5F decided (path A as a check), B-UNO decided (no).
- Protocol of the decisive comparison: amendment A-REPR appended (section 9).
- Plan: dated note under the addendum of 2026-09-05. Roadmap regenerated: F2.REPR consumed, F2.ENGINE next.
- Carrier for the next step: `ADVISORY_F2ENGINE_prompt_2026-09-30.md`.

## Not done, declared
- The census with advocates and a refuter; the reading of Harroun's figures.
- No run in this session (budget of decisive runs: 0 of 3 hours used).
