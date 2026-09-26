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

## 3bis. Step 2 opened: ONE length cap for both walls (the owner's 2026-09-26 afternoon: "i profili
## delle circonferenze non cambiano molto rispetto a Migdal ... proviamo ad introdurre un constraint sulla lunghezza")
THE CAP POSING (`TWOP_CAP` = the cap as a fraction of Migdal's plug length; the arc posing underneath):
one cap L for both walls; the plug tip and the shroud lip ABSCISSAE are design variables
x_end = x_a + (L - x_a) sigmoid(u) (never beyond L, each wall free to end where it wants under it);
the exit HEIGHTS stay pinned (the exit area is the datum, so the vacuum C_F stays a meaningful
objective: in vacuum a larger exit would always win); every station and knot a fixed fraction of its
wall's length, so the station abscissae are TRACED (plug_march x_traced=True; the wavefront replay
gained a wall step on traced stations). Design vector 28 = 22 heights + 4 arc parameters + 2 ends.
The start: a COMPRESSED MIGDAL -- Migdal's arcs, Migdal's heights at the same fractions, both ends at
95 percent of the way from the arc's end to L. Measured first (probe `RDE/handoff/f3_2026-09-25/
twop_cap_probe.py`): the compressed Migdal marches certified (0.21 at cap 0.8, 0.58 at cap 0.6) but
FOLDS -- 1159 / 2670 negative cells (a compressed perfect nozzle carries compressions that
coalesce) -- with C_F 1.57493 / 1.55501 against the full length's 1.57988; the thrust gradient in
the end variables is positive (longer is better in vacuum, as it must be). So a capped walk starts
OUT of class and opens in the driver's RESTORATION phase (S30); the class floors are the uncapped
reference's at the same rung (`_twowall_arc/class_2026-09-26.json`, declared: the fold class is a
property of the net's cells, not of the nozzle's length; ell2 likewise the reference's spacing).
MEASURED, then corrected -- the restoration, three attempts (all logs kept in `_twowall_cap0.8/`,
`_twowall_cap0.6/`): (i) the driver's own restoration phase with the reference's class-scale radius
5.9e-5 m: "no motion" at once at both caps (`run_walk_AN_nomotion_*`); (ii) the same with the station
spacing 1.06e-2 m as the radius: no motion again (`run_walk_AN_ell_nomotion_*`); (iii) a restoration
BEFORE the driver, written in `walk()`: ascent of a SOFT KS margin (rho_r = ln n / max(violation, mu0),
so that the aggregate spans the whole violation and its gradient lifts every folded cell together --
the class rho makes the KS the min cell, whose ascent moves one cell at a time: with it, "no step at
ell/2"), line search from ell down by halves, continuation in rho as the violation shrinks: from the
compressed Migdal it MOVES but does not arrive -- 32 iterations, 100 records, 40 min, soft KS -0.98 ->
-0.83 while the class KS (the min cell) stays at -0.62 (`run_walk_AN_softks_stalled_*`). A compressed
perfect nozzle is not a folded design with a few bad cells: its re-turning walls coalesce compressions
over the last 40 percent of the length (census `twop_cap_starts_probe.py`: at cap 0.8 the 1159
negative cells sit at x fractions 0.4-1.0 of the length and beyond the lip, at cap 0.6 they spread from
0.3 on). Finding row `driver:restoration-phase-no-motion` (the driver's phase 1 never moved, three
times today; the soft ascent works for a MARGINAL violation, see below).

THE START, THEN, IS THE POSING'S OWN QUESTION, and two generic starts were measured (same probe):
- C, the CONE: each wall an arc made C1 with the chord from the arc's end to the pinned exit point
  (the arc's end slope = the chord's, a smaller turning: 0.24 / 0.18 rad against Migdal's 0.39 /
  0.34), then the chord. Fold-free at both caps (min cell +0.0061 / +0.0068 against the floor 0.0057),
  C_F 1.568009 / 1.562623. The walks from it (`run_walk_CN_*`, Newton metric) climb at 2e-4 per
  segment glued to the class boundary (the cone's net is marginal everywhere along the straight
  wall): 1.5691 after 9 segments at cap 0.8, 1.5631 and giving up at cap 0.6 -- stopped, a
  measured NEGATIVE (the cone is in class but too far, the far-start stall of section 3 again).
- T, the TRUNCATED MIGDAL: Migdal's own contour up to the cap's end (NOT compressed), plus a tail
  deflection Delta t^2 (t the fraction of [x_a, end], zero slope at the arc's end so the clamp holds)
  bringing each wall to its pinned exit height -- an EXPANSION on both walls (the pinned tip is
  below and the pinned lip above Migdal's contour at the cut), which cannot fold. In class at both
  caps (KS +0.0081 / +0.0057), C_F 1.579355 / 1.573248 with the ends at 0.953 L (the sigmoid's u0 = 3).
  Its reading is the physics of the whole step: under a cap the optimiser keeps Migdal's arcs and
  Migdal's contour where it exists and spends the missing length on a final expansion to the exit
  area. `TWOP_START=C` and `=T` in `a1_twowall.py` (cone_start, trunc_start).

THE BASELINE the owner asked for ("confrontiamo con il Migdal troncato a quella lunghezza"):
Migdal's walls CUT at x = L, both, the plug's cut face at vacuum like the posing's pinned base; the
thrust exact from ONE record (the walls beyond the cut do not touch the supersonic flow upstream: the
cut nozzle's thrust is the record's wall-pressure partial sum up to the cut, plus the interpolated
point AT the cut so that the curve is continuous in L). `twop_trunc_migdal.py` ->
`_twowall_cap/truncated_migdal_2026-09-26.json`: C_F 1.578393 at f 0.8 (A_e/A_i 3.952, 99.906 percent
of the full length's 1.579880), 1.569476 at f 0.6 (A_e/A_i 3.715, 99.341 percent), 1.543487 at f 0.4.

THE CAPPED WALKS (T start, Newton metric, 8 workers, 16 x 6, coarse rung; the ends first free below L
with u0 = 3, then AT L with `TWOP_U0=10`, artifacts `_twowall_cap{0.8,0.6}/` and `_twowall_cap{0.8,
0.6}_atL/`; ~17-19 min each):

| cap | L - x0 [m] | Migdal cut at L | T start (ends at L) | OPTIMUM (ends at L) | gain over the cut | of the full length |
|-----|-----------|-----------------|---------------------|---------------------|-------------------|--------------------|
| 0.8 | 1.187 | 1.578393 | 1.579661 | **1.579836** | +1.44e-3 (+0.091 %) | 99.997 % |
| 0.6 | 0.890 | 1.569476 | 1.575035 (*) | **1.575268** | +5.79e-3 (+0.369 %) | 99.708 % |

(*) the T start at cap 0.6 with the ends at L sits at KS +0.0056 < mu0 0.0057 (in the walk's class by
the gap, NOT by the driver's test KS >= mu0: the driver opened its restoration and took no step,
`run_walk_TN_nomotion_*`); the walk's restoration is now triggered by the driver's own test, and the
soft-KS ascent repaired the 7e-5 violation in ONE step (1.3e-3 m along +grad soft KS: KS +0.0056 ->
+0.0059, C_F 1.574988 -> 1.575035, 4 records).
With the ends FREE below L (u0 = 3): 1.579551 / 1.573361, the ends did not move (gradient in u 1e-8
to 1e-3, three orders below the knots'; the sigmoid's derivative at u = 3 is 0.045): a POSING
ARTEFACT worth 2.9e-4 / 1.9e-3 -- since the vacuum thrust is monotone in the length (the cut Migdal's
curve), the cap is ACTIVE and the ends belong AT L; the at-L runs are the numbers of record.

THE READING (coarse rung, 140 x 31; the fine-rung confirmation is the pending item, as for step 1):
1. Where the lip goes: at the cap, and the plug tip too -- both ends at L, the cap active. Under the
   cap the optimiser does not make an internal-external nozzle (a plug protruding beyond the lip)
   nor a shorter shroud: a longer wall is always worth more within the class.
2. How the arcs change: they do NOT (cap 0.8: plug x_a 0.0729 -> 0.0727, t_a 0.3913 -> 0.3914,
   shroud 0.0646 -> 0.0647, 0.3415; cap 0.6: plug x_a 0.0729 -> 0.0711 (most of it in the
   restoration step), the rest unchanged). The arc gradients are not zero (0.0125 / -0.053 in x_a):
   the walk is class-bound in those directions too -- the multipliers of the fold class are ACTIVE
   at both landings (-0.104 at cap 0.8, -0.018 at 0.6; KS - mu0 +0.0024 / +0.0003): the capped
   optimum sits ON the fold-class boundary. A shorter nozzle wants to turn faster, and the
   shock-free constraint is what stops it -- the same wall the S21-S23 plug optima left.
3. What the cap buys over the cut Migdal: +0.09 percent at 80 percent length, +0.37 percent at 60
   percent, of which the walk's polish is +1.8e-4 / +2.3e-4 and the rest is the T start itself,
   i.e. the pinned EXIT AREA (A_e/A_i 4.0 against the cut's 3.95 / 3.72) reached by a final expansion.
   The comparison is at equal LENGTH, as asked, not at equal exit area: the cut Migdal is the
   practice's truncated-ideal contour, the capped optimum keeps the datum area. The gains are 10-40
   times the coarse-rung artefacts of step 1 (gains of 1e-5 to 3e-5 that fell under refinement),
   which is why the coarse reading is reported; the fine rung decides the size, not the sign.
4. The two walls stay a shrouded plug of Migdal's family: no new kernel, no new topology. What the
   length constraint changes is the END of both walls (a stronger final expansion) and the
   activity of the fold class. At 80 percent length the capped nozzle keeps 99.997 percent of the
   full-length thrust: Migdal's last 20 percent of length is worth 3e-5 in C_F on this grid.

Figure 26 `_twowall_cap/figs/26_cap_vs_truncated_migdal.png` (generator `RDE/handoff/f3_2026-09-25/
twop_cap_fig.py`): (a) the walls -- Migdal full, cut at L, the capped optima with the ends at L and
free; (b) zoom on the arcs; (c) C_F against length: the cut Migdal's curve and every start and
landing of the day (cone, T, ends free, ends at L); (d) the table.

Records: `_twowall_cap0.8_atL/walk_TN_2026-09-26.json`, `_twowall_cap0.6_atL/walk_TN_2026-09-26.json`
(the numbers of record), `_twowall_cap0.8/walk_TN_2026-09-26.json`, `_twowall_cap0.6/walk_TN_2026-09-
26.json` (ends free), logs of every attempt beside them. Probe logs in `RDE/handoff/f3_2026-09-25/`:
`twop_cap_starts_probe_{0.8,0.6}.log`.

WHAT COMES NEXT (the owner, 2026-09-26 evening): the procedure for the RDE nozzle -- all phases at
once, each voting by duration, temperature and initial-line state, in the wave frame, with the
centrifugal term. Written as a proposal, anchored to what the corpus already proves (T0, O1, VI.1,
T-NSW, the seams of the march): `validation/ADVISORY_2026-09-26_RDE_multiphase_procedure.md`.

## 3ter. Step 2 bis: the cap AT AMBIENT (the owner, 2026-09-26 night: "se invece ci mettiamo in ambiente
## invece che nel vuoto?")
THE POSING (a1_twowall.py, additive; the vacuum path gated bitwise): TWOP_PA = p_a/P0, "adapted" = the
1-D exit pressure of Migdal's pair (2.3081e-2: the full Migdal then exactly adapted), "adaptedx2" =
twice it (Migdal over-expanded by 2). The ambient acts on the outside of the engine and, by the
open-wake convention p_b = p_a (declared: Sule & Mueller 1973; Fiore 2019 sec. 6.1, where strong
over-expansion is the open-wake regime), on the plug's cut face, so C_F,amb = C_F,vac - p_a/P0 x
pi (y_lip^2 - y_tip^2) / A*, the heights read from the march's own last wall points (J_of). The exit
area is no longer a datum: TWOP_FREE_EXIT = lip makes the lip height a design variable with the plug
tip height PINNED at the cut Migdal's (the base area then the same for every profile at a cap, so an
error of the base convention is common to all of them: the owner's fair-comparison rule); "both"
frees the tip height too. With a free exit the T start is Migdal CUT at the cap, exactly, in the
spline posing (no tail deflection). Design vector 29 (lip) / 30 (both); the tail of the vector is now
addressed by positive indices. The cap posing's generic starts (T, C) are taken whole, never ramped
toward the reference (the compressed Migdal folds), and repaired by the walk's restoration when out
of class (measured: the cut Migdal at mid-cap sits at KS +0.0020 under the floor 0.0057, and every
blend toward the compressed Migdal folded -- "nothing to walk", log `_twowall_cap0.8_amb2_free/
run_walk_TN_noramp_2026-09-26.log`).
GATES (probe `RDE/handoff/f3_2026-09-25/twop_ambient_gate.py`): A1 p_a = 0, exit pinned: the step-2
record's start reproduced BITWISE (J 1.579660988049); A2 adapted, lip free: replay = record to 2.2e-16;
the adjoint against central differences of the frozen replay along the lip height 9e-5 .. 1.4e-4,
a plug knot 5.3e-4 (h 1e-5), the shroud arc end 2.3e-3 (h 1e-5, falling with h).
THE CEILING: at the adapted ambient the 1-D ideal (expansion to p_a from the same inlet) is C_F
1.471005; the instrument's full Migdal gives 1.471292, +2.86e-4 -- the coarse rung's bias, measured
again (step 1: +2.9e-4 in vacuum).
THE CUT MIGDAL AT AMBIENT (`twop_trunc_migdal.py`, the same JSON gains CF_amb and CF_amb_x2):
adapted: 99.987 / 99.818 percent of the full length's ambient thrust at 80 / 60 percent length (in
vacuum 99.906 / 99.341) -- cutting removes exit area the ambient no longer pays for; the curve's
maximum is the full length. Twice the adapted ambient: full 1.362703, and the curve PEAKS at 44
percent length (1.370230, +0.55 percent): an over-expanded perfect nozzle gains by truncation.
THE WALKS (T start, Newton metric, 16 x 6, coarse rung, ends AT the cap, lip free, tip pinned;
records `_twowall_cap{0.8,0.6}_{amb,amb2}/walk_TN_2026-09-26.json`, ~20-25 min each):

| ambient | cap | Migdal cut | optimum | gain | lip y [m] | p_lip / p_a | vacuum optimum judged here |
|---------|-----|-----------|---------|------|-----------|-------------|----------------------------|
| adapted | 0.8 | 1.471096 | 1.471297 | +2.0e-4 (+0.014 %) | 1.2010 -> 1.2013 | 1.09 -> 1.14 | 1.471247 |
| adapted | 0.6 | 1.468618 | 1.468693 | +7.5e-5 (+0.005 %) | 1.1869 -> 1.1867 | 1.40 -> 1.46 | 1.466679 |
| 2 x     | 0.8 | 1.363798 | 1.364396 | +6.0e-4 (+0.044 %) | 1.2010 -> 1.1989 | 0.54 -> 0.57 | 1.362659 |
| 2 x     | 0.6 | 1.367760 | 1.367947 | +1.9e-4 (+0.014 %) | 1.1869 -> 1.1863 | 0.70 -> 0.73 | 1.358090 |

THE READING:
1. At the adapted ambient the capped optimum IS the cut Migdal within the instrument's resolution
   (+2e-4 / +7.5e-5, below the coarse bias): the lip stays where the cut puts it, the arcs
   unchanged. The vacuum gains of step 2 (+0.09 / +0.37 percent) were the pinned exit AREA; at the
   adapted ambient that area is worth nothing, and the vacuum capped optimum judged at this ambient
   LOSES to it (-5e-5 at 80 percent, -2.0e-3 = -0.14 percent at 60 percent).
2. Over-expanded (2 x), the optimiser lowers the lip (2.1 mm at 80 percent; A_e/A_i 3.953 -> 3.935)
   and gains +0.044 / +0.014 percent -- but a SHORTER nozzle does better: the cut Migdal at 44 percent
   length is +0.43 percent above the 80 percent capped design. At this ambient the cap is not active:
   the length is an outcome, and a posing with both ends pinned at the cap and the tip height pinned
   cannot find it. The sigmoid ends cannot either when saturated (u0 = 3: derivative 0.045; u0 = 10:
   pinned); the free walk starts at u0 = 0 (derivative 0.25).
3. For the RDE (ADVISORY_2026-09-26_RDE_multiphase_procedure.md section 6.2): with walls ending at the
   exit, the phase average collapses to the mean-pressure design (T3's argument: F linear in P0);
   the ambient enters every phase alike through p_a A_e. The phases disagree only through the free
   jet after the lip, the base, separation, gamma(T) and the line profiles.
[pending: the free walk, cap 0.8, 2 x ambient, ends and both heights free]

Figures 27 `_twowall_cap/figs/27_cap_at_ambient.png`, 28 `28_cap_at_ambient_x2.png` (generator
`RDE/handoff/f3_2026-09-25/twop_amb_fig.py amb|amb2`): walls, the shroud's last 35 cm, wall pressure
over p_a, C_F at the ambient against length with the cut Migdal's curve, table.

THE PLAN REVIEW (the owner's request the same night) is section 6 of
`validation/ADVISORY_2026-09-26_RDE_multiphase_procedure.md`.

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
(the fine rung was run), twowall:far-start-stalls-at-fold-cliff minted. Figures (confirmation, generators in
`RDE/handoff/f3_2026-09-25/`): `_twowall_arc_fine/figs/24_arc_step_fine.png` (twop_fine_fig.py: the fine walks'
trajectories, the landings against Migdal's walls, coarse vs fine departure), `25_profiles_and_circles.png`
(twop_profiles_fig.py: the five profiles found and the initial circles with their radii and end angles).
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
Step 2 (evening): restoration attempts ~1 h of processes (three, all negative from the compressed
Migdal); starts probe 2 x 4 min; cone walks ~25 min (stopped); truncated-Migdal walks 4 x 14-19 min
(ends free, ends at L); the cut-Migdal curve 1 min; figure 26. About 2.5 h of machine time in all.

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
- Step 2 commit (evening): `a1_twowall.py` gains the cap posing's restoration in `walk()` (soft-KS
  ascent with continuation, triggered by the driver's own feasibility test), the starts C (cone) and
  T (truncated Migdal), `TWOP_U0` (the ends' start; 10 = at the cap); `twowall_cases.json` gains the
  `restore` block; `a1_plug_march.py` the graph's x_traced guard; `a1_wavefront_replay.py` the wall
  step on traced stations. Registry: findings `driver:restoration-phase-no-motion` minted,
  `twowall:design-posing-open` updated (step 2 concluded at the coarse rung); X-TWOP's statement
  gains the cap reading (pass 2026-09-26 unchanged: the derive of record is the same). New doc:
  `ADVISORY_2026-09-26_RDE_multiphase_procedure.md` (the proposal for the RDE procedure; SR-1 index
  row). Records `_twowall_cap*/`, figure 26 untracked as all figures. Lints and suite re-run before
  the commit (numbers in the commit message).
- Step 2 bis commit (night): `a1_twowall.py` gains the ambient objective (TWOP_PA, adapted[x factor],
  J_of minus p_a times the exit annulus), the free exit heights (TWOP_FREE_EXIT lip / both), positive
  tail indices, the exit readout (heights, wall pressure over p_a) in the walk's record, the cap
  starts taken whole and repaired by the restoration; the vacuum path gated bitwise. Registry:
  findings `twowall:cap-ends-sigmoid-saturate` minted, `twowall:design-posing-open` updated; X-TWOP
  gains the ambient reading. The advisory gains section 6 (the plan review) and the Stage-0
  amendment; index rows extended; PROGRESS block in place + archive; D6 note; M0 addendum item (4);
  handoff section 11. The free walk (`_twowall_cap0.8_amb2_free/`) was still restoring at the
  commit: its result goes in a follow-up commit.
