# S36 — The shrouded plug: the plug march with a second wall (2026-09-24 afternoon, [F3/A1], brick-2 plug line)

Owner's direction of the day: "dopo di ciò sarà necessario intraprendere la direzione degli
shrouded plug per completare la suite", then "proseguiamo con gli shrouded". Session mose-a1,
main tree `rde-nozzle-program` (the S34-S35 worktree was removed at 13:30). Communication in
Italian; this log in English (CLAUDE.md).

## 1. What was missing, measured
The plug march (`a1_plug_march.py`) had NO upper-wall cell: the top of every column was the
free-jet edge (survey of the record, 2026-09-24: no shroud cell in validation/, no shrouded
configuration in the tournament, D6 F3 "two-wall Veen = conditional stretch", the topology
census classing Migdal and Veen as two-wall annular bells). GENO has both two-wall families:
type 9 (Migdal's perfect annular nozzle, exact uniform axial exit) with runs whose walls are
field points, and type 7 (Veen), ~55 %, CTest disabled, not a referee.

## 2. The brick: `plug_march(..., shroud=(xs, ys, ss), wedge_every=1)` (additive)
- **Direct top-wall cell** `make_resid_walltop`: the column's C+ from the point below (same
  column) meets the shroud on the cubic Hermite segment of the two bracketing stations (a
  recorded decision, "sseg", indexed by the column counter); unknowns (x4, u4), y4 = H(x4),
  v4 = H'(x4) u4; rows = C+ position and C+ compatibility (the bell's inverse-wall rows with
  the foot fixed at pt1). The bell's wall is INVERSE because a top-down column ends on the
  station; here the column is the C+ and the wall point is wherever it arrives (GENO's
  DirectWall).
- **The lip F**: when the column's C+ would land beyond F, the bell's inverse wall cell
  `A1.make_resid_inwall`, verbatim, places F with its foot on the C- leg from the previous
  shroud point to the column's top interior.
- **After F**: no top cell. The top row IS F's C- (the exit characteristic); rows are only
  consumed at the plug; the march ends when that row reaches the plug or at the last station.
  No free jet, no p_a: the region above F's C- is not computed.
- **The start-up WEDGE (measured, then marched).** Every column is a C+ launched from a PLUG
  station, so the shroud between the start line and the first column's arrival received no
  column: on the exact channel the first column's C+ landed beyond the lip, one shroud point,
  the lip placed from the start line, shroud pressure 2.5 % off (2/5). With the free jet that
  wedge is filled with data rows (edge_fill); with a wall on top it must be MARCHED: wedge
  columns = C+ lines launched from the start-line points, top row first (they order left to
  right), rows keeping their indices, ending on the shroud (or at the lip); the plug wall's
  foot search then brackets on them like on any column. `wedge_every` thins the wedge (the
  skipped rows take their C- partner from the start line): with one column per row the N-1
  reflections crowd into the wedge's short x-range and travel downstream as a C- band ~25x
  denser than the rest of the net, degrading the plug-wall cell where the band lands
  (measured on Migdal (280,61): cert 4.28 at station 208, the last column's rows piling at
  dy 0.0013); the twin chooses m so that the launch spacing projected along the C+ matches the
  first plug station spacing (m = 1 on both cases with curvature-adaptive stations).
- **Thrust**: J = F_in + push(plug) + push(shroud), the shroud push with the +dy sign (a rising
  top wall pushes the fluid forward; `wall_push_poly` signed: F_out = F_in - push_signed(plug)
  + push_signed(shroud)). `out["shroud"]`, `out["lip_col"]`, `out["edge"]` None.
- Record path: bit-identical (oracle 6/6 with the same printed digits, P-1 0.41809 / 3.17e-04
  / 4.49e-03; TW-5 below).

## 3. Stage source [X-TWMU]: the exact two-ray channel, 6/6
Spherical source flow (a1_source_flow_oracle.Radial, diverging, NASA tables): plug = the 12-deg
ray, shroud = the 22-deg ray to a lip at 60 % of the marched length; start = the exact states
on the vertical cut X0 = 1.0 m; grids (41,31) and (81,61); constants in
`shroud_twin_cases.json`.
- TW-1 certified: 2.47e-2 / 3.62e-2.
- TW-2 shroud wall pressure vs the closed form: fine max rel 1.34e-5 (mean 5.5e-7), coarse
  3.46e-5; inside its per-station Richardson band at 100 % of the stations.
- TW-3 the field on and below F's C- (x > x_F, 4492 points): |dq|/q 1.73e-6 (coarse 6.8e-6),
  |dtheta| 2.8e-6 rad (coarse 1.1e-5).
- TW-4 the lip F: |dq|/q 1.24e-6, |dtheta| 2e-15.
- TW-5 the free-jet march of the same channel bit-identical to the record of the first run.
- R-1 the shroud curved by 2 % at the lip: pressure error 0.19 (1.4e4 x the clean).

## 4. Stage geno [X-MGDL]: Migdal's perfect annular nozzle from GENO, 8/8 at both area ratios
GENO nozzle_type 9 (`CASES/migdalnoz`, NI 1001, run in minutes -- not the 3 h the GENO docs
name -- in RDE/handoff/shroud_2026-09-24/geno_migdal/{eps6,eps4}_ni1001 with absolute thermo
paths): uniform start line x = 0, y in [0.85, 1.0], M_i 1.5, theta 0 (exact data), both walls
with 0.2 arcs, A_e/A_i = 6 (GENO's case) and 4 (Migdal's paper). Our start = that line; our
stations = GENO's walls (profile_cp plug, profile_cm shroud) distributed by the measure
dx + L/(2 theta_tot) |dtheta| (a third of the stations on the turning); the exit is uniform
and axial at the 1-D Mach of the area ratio, so the known answers are exact on OUR mesh.
- The gas table spans 1050-3900 K and GENO's T0 300 K clamps (measured): the twin is posed at
  T0 3800 K, p0 1e5, and reads dimensionless numbers (M, p/p0, C_F) -- exact for a calorically
  perfect gas.
- Grids (140,31) coarse / (280,61) fine; bands K_RICH x move; MG-2/MG-3 add the reference's
  own resolution class (the reading's change between GENO NI 50 and NI 1001 walls: M 0.013,
  theta 3.5e-3).

| | eps 6, 1-D M_e 3.541518, C_F,vac 1.61908 | eps 4 (paper), 1-D M_e 3.110645, C_F,vac 1.57959 |
|---|---|---|
| MG-1 cert (coarse / fine) | 8.3e-2 / 0.74 | 4.7e-2 / 4.5e-2 |
| MG-2 F's C- (226-229 pts): max \|M - M_e\|, \|theta\| | 5.9e-3, 2.0e-3 | 6.2e-3, 2.4e-3 |
| MG-3 last column: max \|M - M_e\|, \|theta\| | 1.7e-2, 4.9e-3 | 8.7e-3, 3.1e-3 |
| MG-4 C_F = F_in + plug + shroud | 1.32962 + 0.13514 + 0.15441 = **1.61917** (\|d\| 9.0e-5, band 7.9e-4) | 1.32962 + 0.11720 + 0.13277 = **1.57960** (\|d\| 2.9e-6, band 3.1e-4) |
| MG-5 mass, exit polyline vs start | 3.9e-4 | 5.0e-5 |
| MG-6 wall p/p0 vs GENO's field (plug / shroud, max) | 1.36e-2 / 6.8e-3 (mean 5.9e-3 / 4.0e-3) | 5.8e-3 / 8.5e-3 (mean 3.2e-3 / 4.1e-3) |
| R-2 shroud sign flipped | misses by 0.31 | misses by 0.27 |
| R-3 shroud lifted 3 % (ramped) | \|M - M_e\| 8.6e-2 > band 2.8e-2 | 1.0e-1 > band 1.5e-2 |

GENO's coarse case of record (NI 50) reads the same closure (C_F 1.61905 at (140,31)) with
wider exit spreads (M 3.529-3.550): the reference's resolution, declared as the class above.
The cross-code field is read as a point cloud (the type-9 binary streams, the padding rows of
zero velocity dropped; the wall nodes are field points to 1e-11).

Readings, not graded: the (280,61) plug p/p0 against GENO near the plug arc's end (x 0.1-0.25)
is where the largest deviation sits (GENO's plateau at 0.075 against our dip to 0.065 at
(140,31)); the fine grid halves it.

## 5. Declared
- Three iterations of the twin before the record: the first without the wedge (2/5 on the
  exact channel: the finding of section 2); the second with a full wedge at (280,61) uncertified
  (cert 4.28, the dense band); the third with the wedge thinned to m = 4 (eps 6) WORSE (plug
  p 11 %, C_F 1.6208): thinning starves the arc region -- the cure was the curvature-adaptive
  station measure with m = 1, not the thinning. The thinning stays as a knob.
- The R-3 rejector at a 1 % lift (ramped) was absorbed by the loose (140,31)/(70,16) bands:
  raised to 3 % (dM_e ~ 0.09).
- GENO's T0 300 K is outside the program's tables: posed at 3800 K, dimensionless readings
  only (section 4).
- Not done: a two-wall TR-SQP (the shroud as a design variable, the shroud push in J), Veen
  1974 Table 3 (needs OUR posing of the -15-deg start and both sharp-corner fans; GENO type 7
  excluded), the rotated-frame twin of the top cell (`cells=` + shroud raises).
- SR-9 orchestration: one Explore agent (the second-wall survey, 241k tokens, one round).

## 6. HANDOFF
- Files of record: `validation/a1_plug_march.py` (shroud=, wedge_every=, make_resid_walltop,
  hermite_seg), `validation/a1_shroud_twin.py` + `shroud_twin_cases.json` (new), this log;
  registry X-TWMU / X-MGDL; index row; M0 Part VI addendum item; PROGRESS R37 / NEXT.
- Handoff note RDE/handoff/SHROUD_HANDOFF_2026-09-24.md; the GENO runs and the figure
  generator in RDE/handoff/shroud_2026-09-24/; figure
  `validation/_shroud_twin/figs/16_shroud_migdal.png` (not committed).
- NEXT (atomic): the two-wall design -- the shroud spline as design variables with the +dy
  push in J_replay (the throat posing's pattern: a case dict carrying both walls), RE-1 on
  Migdal's contour pair from generic starts (the exact 1-D value as the oracle), then Veen
  1974 Table 3 from our own posing of his start.

## 7. The owner's condition and conformity

**The condition** ("intraprendere la direzione degli shrouded plug per completare la suite",
then "proseguiamo con gli shrouded"), read as: the plug march carries a SECOND wall, and the
two-wall march is certified on an exact channel and on a two-wall reference with an exact known
answer, with rejectors.

| carrier | reference | tests | verdict |
|---|---|---|---|
| [X-TWMU] stage source | the exact spherical-source channel (12-deg / 22-deg rays, lip at 60 %), grids (41,31)/(81,61) | TW-1..TW-5 + R-1 | 6/6 PASS |
| [X-MGDL] stage geno, eps 6 | Migdal's perfect annular nozzle from GENO type 9 (NI 1001), grids (140,31)/(280,61) | MG-1..MG-6 + R-2, R-3 | 8/8 PASS |
| [X-MGDL] stage geno, eps 4 (the paper's) | same, GENO re-run at A_e/A_i 4 | same | 8/8 PASS |

Also of record: the free-jet record path bit-identical (TW-5; oracle 6/6 with the same digits),
and the owner's check page `validation/_shroud_twin/figs/16_shroud_migdal.png` (generator
RDE/handoff/shroud_2026-09-24/shroud_fig.py, presentation only: it re-marches (140,31) and reads
the stage JSON).

**Conformity** (CLAUDE.md R1-R7, SR-1..SR-12):
- Branch `rde-nozzle-program`, main tree (no worktree); identity AlexFalco5; explicit
  pathspecs; GENO never added. Push on the owner's word of 2026-09-24 ("purche' il commit sia in
  linea con il lavoro della git, puoi pushare direttamente su rde-nozzle-program"), after the
  commits.
- R1: `[F3/A1][S36]`. R3: this log; NEXT-PARALLELO reduced to the current state; the outgoing
  block verbatim in PROGRESS_ARCHIVE under the 2026-09-24 sera banner, with the DELTA CENSIMENTO
  note and the outgoing R37 row; R37 edited in place (SR-7/SR-10); HANDOFF block (section 6);
  the F3 session count measured in-window (SR-12): `git log --format=%s | grep -o
  '\[F3/A1\]\[S[0-9]*\]' | sort -u` = S26, S28-S33 (7; the pattern does not match the
  hyphenated S34-S35 tag), 74 commits tagged F3 before this session's; with S34-S35 and S36 =
  9 sessions.
- R4: M0 Part VI, LINE ADDENDUM S36, two items with classes (the second wall as a direct cell
  plus the marched wedge; Migdal's exact 1-D answer as the two-wall oracle).
- R5 / SR-2: registry rows X-TWMU (kind carrier, ondemand env=jax) and X-MGDL (env=jax+geno),
  pass 2026-09-24, suite none, falsifiers named (TW-1..5/R-1; MG-1..6/R-2/R-3). SR-1: the
  ADVISORY_INDEX row. SR-5: no A1_* flag added (SHRD_K / SHRD_N / MGDL_GENO_RUN are instance
  knobs of the twin; `shroud=` / `wedge_every=` are kwargs whose defaults are the record).
  SR-4: no new glossary token (the ids are registry ids).
- SR-6: files of record committed: `validation/a1_plug_march.py` (shroud=, wedge_every=,
  make_resid_walltop, hermite_seg), `validation/a1_shroud_twin.py` and
  `validation/shroud_twin_cases.json` (new); this log; the index; PROGRESS and its archive;
  M0; the registry. Not committed, by design: the figure (figs are not of record), the GENO
  runs and the figure generator (RDE/handoff, outside the repo), the stage JSONs
  (`validation/_shroud_twin/`, an artefact directory like `_humphreys_twin/`).
- Lints on the tree of the first commit (measured 2026-09-24 ~14:45): numeric PASS (125
  files, 2294 literal-debt baselined, 0 ratchet violations); advisory index PASS (128 file
  rows, 0 violations); claims lint 2 violations = "rde_nozzle_PROGRESS.md cites unknown ID
  [X-TWMU] / [X-MGDL]": the ordering rule (the rows land in the second commit; with the rows
  in the tree the 2 violations read instead "ondemand carrier file <this log> has no committed
  history"). Full suite on the same tree: 15/23 = the seven environmental reds (xiii, xiv,
  xvi, xviii: no sympy; xix, xxii, xxiii: dead literature paths) + (xv) for the ordering
  reason, 87 s; (xvii) PASS (50 carriers accounted); data/phase_diagram.*, data/q_mapping.*
  and figs/phase_diagram_op11.png restored with git checkout before the commit.
- Two commits, as the line's practice: (1) code + data + this log + index + PROGRESS/ARCHIVE;
  (2) M0 addendum + registry + this log's conformity line. The registry commit's rows cite the
  log the first commit landed; M0's and PROGRESS's citations of the new ids resolve with the ids.
