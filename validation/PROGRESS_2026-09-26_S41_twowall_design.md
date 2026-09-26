# S41 — The two-wall DESIGN posing, step 1: the initial arc decided by the optimiser (2026-09-25/26, [F3/A1])

Owner's direction (2026-09-25, after the Migdal confirmation of S40): "andiamo con la tua proposta"
-- 1) the initial arc as a design variable with the ends still pinned; 2) the objective at the
operating ambient with the constraints; 3) the free jet after the lip; 4) the truncation. Two
precisions: the LENGTH constraint will probably be ONE cap for plug and shroud, each free to end
where it wants under it; for the truncation, a base-pressure CONVENTION applied identically to every
profile, so that profiles compare on equal footing even if the absolute base pressure is wrong --
and a documented physical model (Chapman-Korst) is admissible ("la fisica non e' mai rigettata se
documentata"); Fiore 2019 sec. 6.1 gives the regime criterion (where the lip's last wave lands
against the reattachment E and the sonic point S). This log is step 1. F3 stays closed; no session
counter. Session mose-a1, main tree `rde-nozzle-program`. Communication in Italian; log in English.

## 1. The arc posing (carrier `validation/a1_twowall.py`, `TWOP_KERNEL=arc`, artifacts `_twowall_arc/`)
Each wall's initial stretch is a circular arc tangent to the axial inlet whose END abscissa x_a and
end slope t_a = |tan theta_a| are design variables (radius R = (x_a - x_0) sqrt(1 + t_a^2) / t_a);
downstream, the spline of the kernel posing clamped to the arc's end, its 12 knots at FIXED
FRACTIONS of [x_a, end] (they move with the arc's end); the lip and the tip pinned at Migdal's; the
vacuum C_F. Design vector 11 + 11 knot heights + (x_a, t_a) per wall = 26. The reference = Migdal's
arcs (GENO's arc ends 0.0729 / 0.0646 m, end angles 21.4 / 18.9 deg: R 0.2000 / 0.2000 m). The
owner's argument, which this posing tests: circular arcs with the ends pinned leave few degrees of
freedom, so the thrust should pick the best arc (the free-KERNEL family of S40 was the family of
ALL initial stretches, not of circular arcs).
- Stage class (`run_class_2026-09-25.log`, 3/3): the reference in class (worst cell +0.0113 = GENO's
  exact walls, 0 folded), KS brackets the minimum, the unconstrained first move (0.33 mm along
  +grad J) infeasible (KS -0.042). The gradient at Migdal's arcs is NOT zero in the arc ends:
  dC_F/dx_a = +0.021 (plug), -0.016 (shroud) per metre; the thrust prefers a different arc pair.
- The generic start R: each arc's radius x 1.5 (0.30 m) at the reference's end angles, the
  downstream wall the cubic Hermite from the arc's end to the pinned end (axial exit). In full it
  folds (493 cells, KS -0.10); the walk takes the largest in-class ramp toward it: 0.5 (R ~0.25 m,
  7.8 / 5.9 mm off the reference, C_F 2.2e-4 below).

## 2. DUTY-11 on the arc posing, and the identifiability floor corrected
First derive (`run_derive_2026-09-25.log`, 6/6, the S40 criterion): the two softest directions are
almost purely the two arc END SLOPES (t_a of the plug, curvature 0.032; t_a of the shroud, 0.19),
called "near-null" against the GLOBAL floor K_RICH x the Hessian's asymmetry = 1.23 -- yet G-5a
verifies those curvatures by J's own second difference to 8.5e-4 and 1.4e-3: they are measured,
not noise; the global floor was far too crude for a design that mixes knot heights, arc ends and end
slopes. CORRECTED (S41): identifiability PER DIRECTION -- each eigenvalue against K_RICH x its own
verified error (G-5a) plus the rounding floor; the shape band quoted in design units AND as the wall
displacement it makes; the global floor stays a reading. Both derives re-run with the corrected
criterion (arc and kernel posings, 2026-09-26; the kernel posing's "1 near-null" of S40 is expected
to become identifiable: its curvature 0.80 was verified to 2.1e-4). RE-RUN (2026-09-26, both
6/6): ARC posing (`_twowall_arc/run_derive_2026-09-26.log`) 26 of 26 directions identifiable at
their own verified floors (the global floor would have called 3 near-null), condition 4.6e3; the two
softest directions are the arcs' end slopes -- the plug's resolved to 0.175 deg of end angle
(curvature 0.032, floor 3.4e-3), the shroud's to 0.06 deg (0.19, floor 5.6e-3) -- and the widest
shape band is 2.35e-4 m of wall; the Newton step from Migdal's arcs in the identifiable subspace is
2.1 cm (arc ends) for a predicted gain 5.6e-5 of C_F (430 x delta), the gradient's share outside
the identifiable subspace zero. KERNEL posing (`_twowall/run_derive_kernel_2026-09-26.log`) 22 of
22 identifiable (the S40 "1 near-null" was the global floor's artefact), widest band 7.3e-5 m of
wall -- the [X-TWOP] statement is corrected in this session's registry edit. So: circular arcs with
the ends pinned are IDENTIFIED by the thrust (the owner's argument holds at the level of the
curvature); whether the thrust's preferred arc is Migdal's is the walks' question.

## 3. The walks, and the cause of the lost walks isolated
Three walks of the arc posing were lost to "LLVM compilation error: Cannot allocate memory" (the
failure that took the Euclidean walk H of S40 at 04:04): A at segment 4 (16:26, its base already at
C_F 1.579918, +3.8e-5 over Migdal's arcs, in class), R at segment 1 (16:05), and R again at 01:01
after the first mitigation (MALLOC_ARENA_MAX=2). CAUSE ISOLATED (2026-09-26 01:02, measured on the
live processes): the walk process had 32742 memory mappings after two segments against the kernel's
per-process cap of 65530 (vm.max_map_count), the derive processes 5200-5800; a walk accumulates
COMPILED EXECUTABLES -- every march has its own cell count, every count is a new set of array shapes
in the vectorised margin, every shape a new compilation kept in jax's cache -- and dies at the cap.
Not a machine-wide memory event (the page cache was 90-100 GB, available ~100 GB throughout). Fix,
declared: the walk runs the driver one chunk of segments at a time (TWOP_CHUNK), writes a
checkpoint after every chunk (the landing, the Newton metric T, the radius) and CLEARS the
compilation caches (jax.clear_caches) between chunks, reporting the mapping count before and after;
TWOP_RESUME=1 restarts from the checkpoint with the metric read back (no second Hessian). The radius
restarts at tr0 each chunk (declared). Logs of the lost walks kept trimmed
(`run_walk_{A,R}N_oom_2026-09-25.log`, `run_walk_RN_oom2_2026-09-26.log`).
THE GAIN OVER MIGDAL'S ARCS UNDER GRID REFINEMENT, first reading (probe
`RDE/handoff/f3_2026-09-25/twop_refine_probe.py`, log `twop_refine_probe_ckptA.log`, on walk A's
checkpoint after 6 segments, C_F 1.579906467 at (140,31), in class): PAIRED on the same grid the
design beats Migdal's arcs by +2.61e-5 at (140,31) and by +1.22e-6 at (280,61) -- a ratio 0.05 on
one doubling. The preference for a different arc pair is the march's DISCRETISATION (the coarse grid
overshoots the 1-D ideal by +2.9e-4, the fine by +6.1e-5; both designs converge to the same fine
value within 1.2e-6), as the S30 foot-knot gain was; both designs are fold-free on both grids. THE LANDINGS (Newton metric, 12 x 8, backtracking, checkpointed; `run_walk_{A,R}N_2026-09-26.log`,
records `walk_{A,R}N_2026-09-26.json`; grade `run_grade_2026-09-26.log`):

| walk | start | C_F landing (140,31) | gap to Migdal's arcs | plug arc x_end / R / angle | shroud arc x_end / R / angle | |grad|inf | in class |
|---|---|---|---|---|---|---|---|
| Migdal (reference) | -- | 1.579880408 | 0 | 0.0729 / 0.2000 / 21.37 deg | 0.0646 / 0.2000 / 18.85 deg | -- | yes |
| A | Migdal's arcs | 1.579930741 | +5.0e-5 | 0.0761 / 0.2088 / 21.36 | 0.0633 / 0.1960 / 18.85 | 4.1e-3 | yes (KS +0.0118) |
| R | arcs R 0.30 (ramp 0.5: ~0.25) | 1.580100554 | +2.2e-4 | 0.0847 / 0.2313 / 21.47 | 0.0812 / 0.2511 / 18.86 | 1.4e-1 (budget out) | yes (KS +0.0144) |

On the coarse grid the two landings do NOT coincide (RE-1 FAIL: 1.7e-4 apart in C_F, the arcs
2.3 / 5.5 cm apart in radius) and R keeps climbing when its 12 segments end: the coarse-grid thrust
prefers larger arcs, and the more the arcs grow the more it gains. Whether that is physics or the
discretisation preference measured on A's checkpoint (ratio 0.05 on one doubling) is the paired
fine-grid check on both landings (`twop_refine_probe_landings.log`, the same designs re-marched at
(280,61), reference 1.579655122 there):

| design | paired gain at (140,31) | paired gain at (280,61) | ratio | fold census at (280,61) |
|---|---|---|---|---|
| A landing | +5.03e-5 | +1.78e-5 | 0.35 | 0 / 33632, min +0.0099 |
| R landing | +2.20e-4 | -1.65e-4 | -0.75 | 238 FOLDED / 33166, min -0.606 |

VERDICT OF STEP 1: on the (140,31) instrument the arc optimiser does not re-obtain Migdal's arcs,
and its departures are the instrument's, not the flow's -- A's gain falls by 2/3 on one doubling
(a residue +1.8e-5 not resolved at one rung), and R's design, in class on the coarse net, FOLDS on
the fine one (the coarse fold class missed a coalescence the finer net resolves) and is 1.6e-4 WORSE
than Migdal's arcs there. The coarse grid overshoots the 1-D ideal by 2.9e-4 and the fine by 6.1e-5:
the differences the arc question turns on (1e-5 .. 1e-4) sit inside the coarse grid's own error,
and the fold class must be judged where folds resolve. Migdal's arcs are NOT beaten at this
resolution; the owner's expectation ("la spinta indica il miglior raccordo") is TESTABLE only with
the finer instrument: a two-rung posing (the class and the paired value both read at (280,61), or
Richardson-paired on the ladder), which costs ~25 min per march at (280,61) against 30 s -- the
walk budget must be re-planned (the Newton metric's 52 gradient evaluations alone are ~24 h at
that rung). Findings row twowall:arc-design-coarse-instrument-unfit.

## 4. What is measured about the base-pressure convention (for step 4)
Fiore 2019 sec. 6.1 (after Nasuti & Onofri 2012): open wake when the lip's last expansion wave
lands on the separated region behind the base (the base feels p_a); closed wake when it lands
downstream of the sonic point S on the axis (the base is isolated; p_b set by the flow at the
corner); a weak transition band between the reattachment E and S; "there still is no clear
definition of the transition point". Sec. 6.2 lists the closed-wake correlations on the corner
state (mean, conical, cylindrical, Rocketdyne, Sapienza, Chutkey) -- the same family S30 measured
in disagreement by 2-3 x the truncation loss. For Migdal's shrouded plug the lip flow is M 3.11,
the Mach lines from the lip 18.8 deg, reaching the axis 3.5 m behind the lip: the closed wake is
the natural regime unless a strong over-expansion puts a steep shock at the lip (figure
`_twowall/figs/22_wake_regimes_schematic.png`, generator `RDE/handoff/f3_2026-09-25/
wake_schematic_fig.py`; the pocket, E, S and the shock angles are schematic). Convention proposed,
not yet posed: the regime by Fiore's criterion (with S approximated in an inviscid march, declared),
p_b = p_a in the open branch, ONE closed-wake closure for every profile (a correlation or the
Chapman-Korst balance, documented), and a ranking that flips between closures declared unresolved.

## 5. The instrument's speed, before the fine-rung tests (the owner's question, 2026-09-26)
Measured on the arc posing's reference (probes and logs in `RDE/handoff/f3_2026-09-25/twop_speed_bench*.log`,
`twop_fast_bench.log`, `twop_jitsolve_bench_*.log`; a cProfile of the (140,31) record march):
- WHERE THE RECORD MARCH'S TIME WENT: 62 percent in the interior seed predictor -- two eager
  `state_q` calls per cell for an approximate Mach number --, 30 percent in the custom_vjp Python
  wrapper and a second dispatch per cell (the certificate). FAST LANE (`plug_march(fast=True)`,
  additive, default False): one fused dispatch per cell (solve_cert, the verbatim step metric, M5a)
  and the seeds' Mach by numpy on host copies of the tables. BITWISE identical to the legacy lane on
  the reference -- 8999 cells, every z, every decision, J, the KS, the minimum -- at 9 s against 29 s.
- WHERE THE FINE MARCH'S TIME WENT: the vectorised margin's `jnp.stack` of ~34k points compiles a new
  XLA module for every point count (the "Very slow compile" of the (280,61) probes: 1400-1800 s per
  march, 104-112 s when the module happened to be cached). FIXED-BLOCK STACK (`margin["pad"]`,
  additive, default 0): blocks of 1024 points, the cell arrays padded and masked by +inf (exp(-inf) =
  0 exactly). Bitwise identical KS and minimum; the (280,61) march with the fast lane: 35 s. Both
  switches are now the two-wall posing's defaults (twowall_cases.json fast/pad), graded bitwise
  against the legacy lane by the class stage's new gate C-F at every run (arc posing, 2026-09-26:
  4/4, C-F PASS, 9.1 s against 29.3 s). The limit of the identity, measured on the class stage's
  ladder: OFF the reference the fused certificate differs by one ulp (0.1062271882999730 6 vs 2: the
  fused module's own rounding of the step metric, a diagnostic ratio), and on the FOLDED step
  (h 3.3e-4, KS -0.042) the KS differs by 2.4e-11 relative -- the seed's last bits through an
  ill-conditioned cell; on in-class designs every value of record is identical.
- NULL RESULTS: a single XLA thread (`--xla_cpu_multi_thread_eigen=false`) changes nothing on the
  march and slows the compiles; wrapping the cell solver's custom_vjp in `jax.jit` leaves the replay
  gradient unchanged (30 / 36 s against 29 / 36 s; gradients bitwise identical) -- the reverse pass
  is op-by-op eager dispatch over the whole net, not the wrapper.
- WHAT REMAINS: the replay gradients (the walk's unit of work: ~30 s for J and ~36 s for the KS at
  (140,31), machine load permitting) are the cost now; their structural lever is a wavefront
  (anti-diagonal) batching of the cells -- ~400 batched dispatches instead of ~16k -- which is a
  rewrite of the march's control flow, declared and not done.
- THE FINE RUNG'S COST, measured (twop_speed_bench_default.log, machine load ~50): the replay
  gradient of J 158 s and of the KS 154 s at (280,61) against 38 / 52 s at (140,31) -- 4x for 4x
  the cells, no compile cliff; a single XLA thread gives 132 / 143 s there (less contention) and is
  slower at the coarse rung: not adopted. Budget of a fine-rung Newton walk: the metric 52 gradients
  ~2.3 h; a segment = one record (33 s) + iterations x 5.2 min + backtracking records; 10 segments x
  6 iterations ~5.5 h; ~8 h per walk, the two starts in parallel. The runs of S41 at the coarse rung
  are unchanged by the speed work (their records predate it and the lane is graded equivalent).
- THE FINE RUNG'S CLASS (`_twowall_arc_fine/run_class_2026-09-26.log`, 4/4, 528 s): C-F within the
  certificate's band (35303 cells, max |dz| 2.3e-11 = 0.47 of the Newton tolerance, decisions
  identical, J identical, KS 1.8e-16; 33 s against 111 s -- the legacy lane pays its slow stack
  compile once per process); the reference in class, worst cell +0.0130 (33368 cells), floors
  0.0065 / 0.0033 / 0.0016 / 0.0008, rho 51153, gap 2.0e-4; the class breaks along +grad J in the
  same bracket as the coarse rung [1.7e-4, 3.3e-4] m and the first move out of it is infeasible at
  every floor (KS -0.362). Two gate corrections came out of the first fine run (kept as text, the
  log was superseded): C-F was posed BITWISE and fails at the fine rung by 2.3e-11 in one cell (the
  seed's last bits through a near-singular cell) -- re-posed on the certificate's band; C-R was
  posed at the fixed step ell 2^-5, which halves with ell and fell below the break at the fine rung
  -- re-posed as the ladder's first infeasible step. The coarse class re-run under the corrected
  gates: 3/3, C-F bitwise (`_twowall_arc/run_class_2026-09-26.log`).
- THE GRADIENTS, both things the owner asked for (2026-09-26 afternoon, "fai entrambe le cose"):
  (i) THE METRIC IN PARALLEL: the 2n gradients of the secant Hessian are independent, so
  `secant_hessian_parallel` spreads the columns over TWOP_WORKERS processes (stage hesscol of this
  file, the same environment, each recording the same deterministic schedule at W0); gate H-P of
  stage class: two columns in-process against the workers' -- max |dH| 0.0 (bitwise), 8 workers
  366 s for the 26 columns at (140,31) against ~30 min in series (each worker 3-4 columns in
  226-342 s: the per-column cost is 80 s, so the wall time scales with the workers up to n).
  (ii) THE WAVEFRONT REPLAY (`validation/a1_wavefront_replay.py`, the record writing its dataflow
  graph through plug_march(graph=...), additive): the frozen schedule re-executed by anti-diagonal
  LEVELS -- 8999 cells in 368 levels, 566 batches at (140,31) -- every level's cells of one kind in
  one jitted step (gather, parameters, the vmapped implicit solve on the recorded seeds, the
  post-processing, the scatter), batches padded to multiples of 16 lanes so that the steps compile
  once per (kind, size). Gate stage wavefront at (140,31), 3/3: J equal to 1.1e-16 relative, its
  gradient to 2.2e-12, the class margin bitwise and its gradient to 7.6e-14 (tolerance K_RICH x EPS
  x n_cells = 8e-12; the batched solve is the same Newton per lane, its arithmetic not bitwise);
  steady-state cost of J with its gradient 2.5 s against 44.7 s (17.7x), of the margin with its
  gradient 2.3 s against 48.9 s (21.4x); the first call of a process compiles for ~135 s. The
  measured road here: without padding 566 distinct batch sizes recompiled at every schedule (170 s
  per replay); with padding but 8 dispatches per batch 17 s; fused into one jitted step per batch
  2.5 s. AT THE FINE RUNG (280,61), 3/3: J BITWISE equal, its gradient to 5.7e-12, the margin
  1.8e-16 and its gradient 8.4e-14 (tolerance 3.1e-11); steady state 3.8 s against 132 s for J
  with its gradient (35x) and 3.6 s against 199 s for the margin (55x); the first call 253 s. The
  wavefront replay and the parallel metric are now the two-wall posing's defaults
  (twowall_cases.json wavefront, lane 16; TWOP_WAVEFRONT / TWOP_WORKERS override). Budget of a
  fine-rung walk on them: the metric ~5 min on 8 workers, a segment ~2 min -- the sequential
  walks launched at 14:15 (8 h) were stopped at 15:05 and relaunched on the fast replay.
  MEASURED ON THOSE, then corrected (15:35): the first wavefront steps were jitted with the REAL
  batch size as a static argument (for the output slice), so they compiled once per distinct batch
  size -- ~150 per kind -- not once per padded size: 39.5k memory mappings at the walk's start, a
  2-4 min compile at every new schedule, and both walks died at the cap during segment 1 (57 / 11
  allocation failures; logs `run_walk_{A,R}N_staticn_2026-09-26.log`). The padded lanes now scatter
  into a scratch row and the steps take padded shapes only: the coarse gate re-run 3/3 with the
  first call at 26 s (was 135 s) and the steady state 1.7 s (24.6x / 28.4x). The per-segment cache
  clearing is now conditional (above map_clear = 55000 mappings) so the compiled steps survive the
  segments. The walks and the fine derive relaunched at 15:41.
- THE FINE-RUNG WALKS (relaunched 15:41 on the corrected wavefront replay, the metric on 8 workers
  in ~2 min; 10 segments x 6 iterations, checkpointed; `_twowall_arc_fine/run_walk_{A,R}N_2026-09-26.log`,
  44 and 47 min):

| walk (280,61) | start | C_F landing | vs Migdal's arcs (1.579655122) | walls off Migdal | |grad|inf | class |
|---|---|---|---|---|---|---|
| A | Migdal's arcs | 1.579656811 | +1.7e-6 | 0.09 / 0.09 mm | 1.6e-3 (start 1.6e-3) | in, KS +0.0129 |
| R | gentler arcs, ramp 0.5 (7.8 / 5.9 mm off, -1.9e-4) | 1.579544034 | -1.1e-4 | 7.9 / 5.8 mm | 5.3e-2 | in, KS +0.0093, radius at its floor |

  From Migdal's arcs the fine-rung walk moves 0.09 mm and gains 1.7e-6 of C_F (13 x delta; the
  coarse rung gave +5.0e-5 at 0.9 mm: the departure shrinks 30 x with one doubling, discretisation
  as diagnosed); from the gentler arcs the walk recovers 40 percent of its gap in the first
  segments and then STALLS at the class boundary (every trial INFEASIBLE or worse, the radius at its
  floor 1.0e-4 in z), 1.1e-4 below Migdal's arcs and 8 / 6 mm away: the same fold-cliff stall as the
  single-wall finder (f3-residual:finder-stalls-at-fold-cliff), now on two walls.
- THE FINE DERIVE (`_twowall_arc_fine/run_derive_2026-09-26.log`, 6/6, 52 min on the fast replay):
  the functional's resolution delta 2.66e-7 at (280,61) (the decisions' J jump); the secant
  spectrum 25 identifiable directions and ONE not: the softest, a shroud mode, reads -6.49 by the
  secant Hessian at 1 mm but +5.08 by J's own second difference along it (the record's +5.22) --
  a kink of the frozen replay in that direction, not an ascent direction (its own floor 46 covers
  it; the global floor would have called 17 near-null). Widest shape band 3.4e-4 m of wall; the
  Newton step from Migdal's arcs in the identifiable subspace 1.3 cm for a predicted +4.4e-6.
- THE GRADE AT THE FINE RUNG (`run_grade_2026-09-26.log`, 1/3): RE-0 both landings certified and
  in class; RE-1 VALUE FAIL (1.13e-4 apart against K_RICH x delta 1.07e-6); RE-1 SHAPE FAIL. The
  arcs: A lands on Migdal's -- R 0.2001 / 0.2005 m, end angles 21.33 / 18.87 deg against 0.2000 /
  0.2000 and 21.37 / 18.85 --; R stops at R 0.254 / 0.250 m.
VERDICT OF STEP 1 AT THE FINE RUNG: with circular arcs as design variables and the ends pinned,
Migdal's arcs are RE-OBTAINED FROM THEMSELVES (the walk moves 0.09 mm and 1.7e-6 of C_F, 1.6 x the
resolution band: stationary at this instrument) and NOT BEATEN; the owner's expectation that the
thrust picks the arc holds in this sense -- Migdal's arcs are the local thrust optimum of the
circular-arc family at pinned ends. From 8 mm away the class-constrained walk does NOT come back:
it climbs 40 percent of the gap and stalls at the fold-class boundary, exactly as the single-wall
finder did at the nominal ambient. The finder property from far starts is negative on two walls
too; the re-obtention certificate stands from near starts only (the Hermite start of S40, 6 mm off
on the kernel posing, did land). Findings: twowall:arc-design-coarse-instrument-unfit DISCHARGED
(the fine rung was run), twowall:far-start-stalls-at-fold-cliff minted.
- THE CLASS STAGE AT BOTH RUNGS with the corrected gates (`_twowall_arc/run_class_2026-09-26.log`
  4/4, 150 s; `_twowall_arc_fine/run_class_2026-09-26.log` 4/4, 528 s): C-F at (280,61) -- 35303
  cells, max |dz| 2.3e-11 = 0.47 of the Newton tolerance, decisions identical, J identical, KS
  1.8e-16 relative; the fine reference in class (min cell +0.0130, 0 folded), floors 0.0065 ..
  0.0008, rho 51153; the class breaks along +grad J in the SAME bracket 0.17-0.33 mm as at the coarse
  rung (a fixed step ell 2^-5 would have fallen below it there: C-R is now the first infeasible ladder
  step, infeasible at every floor, KS -0.362). The fine-rung walks A (Migdal's arcs) and R (the
  gentler arcs' in-class ramp) launched 14:15 with the Newton metric at their own start, 10 x 6,
  checkpointed (`_twowall_arc_fine/run_walk_{A,R}N_2026-09-26.log`).

## 6. Budget
Fine-rung runs on the fast replay: class 9 min (the legacy-lane gate included), walks 44 + 47 min
(the metric ~2 min on 8 workers), derive 52 min. Machine time lost to the three coarse-rung walk
deaths and the two fine-rung false starts (sequential replay 8 h projection, the static-size
compile): ~4 h of processes, no results lost that were not re-obtained.
No F3 counter (the phase is closed; this is the design posing's step 1 on the owner's word). Runs:
speed benchmarks and the class stages at both rungs ~45 min;
class 4 min; derives 106 + 90 min (arc, kernel, the corrected criterion); walks A 92 + 19 min and
R 150 min after three lost walks (~3 h of machine time lost to the mapping cap); refinement probes
50 + 60 min. Nothing of the plug instance's campaign budget is touched.

## 7. Conformity
- Branch `rde-nozzle-program`, main tree; identity AlexFalco5; explicit pathspecs; GENO never
  added; push on the owner's standing word.
- R1: `[F3/A1][S41]`. R3: this log; PROGRESS residual block (the S40 line extended with step 1's
  verdict) + archive; D6 note; the handoff section 9. R4: M0 LINE ADDENDUM S41 (two items).
- R5 / SR-2: X-TWOP's statement corrected (per-direction identifiability, 22 of 22; the arc posing
  as a reading with its verdict), pass 2026-09-26 = the kernel derive re-run today; findings:
  twowall:arc-design-coarse-instrument-unfit minted, twowall:design-posing-open updated (step 1
  taken, its lesson), numerics row unchanged. SR-1: the index row.
- Code: `a1_plug_spline_opt.run_trsqp` gains the additive `on_segment` callback (default None,
  bit-identical); `a1_plug_march.py` gains `fast=` (the fused record lane) and `margin["pad"]` (the
  fixed-block stack), both additive with the legacy lane as default; `a1_twowall.py` gains the arc
  posing (TWOP_KERNEL=arc), the per-direction identifiability, the Newton metric's checkpoint/resume
  with cache clearing, the arc readout in the grade, the K/N overrides for the fine rung, the gates
  C-F (lane equivalence within the certificate's band) and C-R at the ladder's first infeasible step. Records: `_twowall_arc/` (class, derive, walks, grade), `_twowall/derive_2026-09-26.json`
  + log (the kernel derive re-run), the probes in RDE/handoff/f3_2026-09-25/.
- Measured on the tree of the first commit (2026-09-26 ~05:50; the later commits of the day re-measured, see their messages): numeric lint PASS (128 files, 0 ratchet
  violations); claims lint PASS (0 violations; X-TWOP fresh, pass 2026-09-26 >= last commit of its
  doc); advisory index PASS (133 rows); findings lint 0 violations on its rows (259 entries, 213
  open; the H4 channel and families e+f red at HEAD as before); FULL suite 16/23 = the seven
  environmental reds, 117 s; data/phase_diagram.*, data/q_mapping.* and figs/phase_diagram_op11.png
  restored with git checkout before the commit. One commit: the registry rows edited here cite the
  S40 log as their doc (unchanged), so the ordering rule does not apply.
