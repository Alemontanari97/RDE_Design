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
   [CORRECTED the same night, section 3quater: the binding cells are TINY healthy cells at the
   plug's inlet arc, whose margin is their area over the reference's ell^2 -- a SIZE floor that
   the cap tightens by compressing the stations; the smallest SHAPE margin of both landings is
   0.44-0.45 (Migdal's own 0.42). The "shock-free boundary" reading of this item is RETRACTED
   (finding twowall:class-floor-size-artefact); the C_F numbers stand as optima under that floor.]
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
The free walk (cap 0.8, 2 x ambient, ends from u0 = 0 and both heights free, started from the cut
Migdal at mid-cap, C_F 1.370147) was STOPPED in its restoration: the cut Migdal at 42 percent length
reads KS +0.0020 under the floor 0.0057, and sixteen soft-KS steps only enlarged healthy tiny inlet
cells (KS +0.0020 -> +0.0032, C_F 1.37016) -- the size floor of 3quater, not a fold
(`_twowall_cap0.8_amb2_free/run_walk_TN_stopped_size_floor_2026-09-26.log`).

Figures 27 `_twowall_cap/figs/27_cap_at_ambient.png`, 28 `28_cap_at_ambient_x2.png` (generator
`RDE/handoff/f3_2026-09-25/twop_amb_fig.py amb|amb2`): walls, the shroud's last 35 cm, wall pressure
over p_a, C_F at the ambient against length with the cut Migdal's curve, table.

THE PLAN REVIEW (the owner's request the same night) is section 6 of
`validation/ADVISORY_2026-09-26_RDE_multiphase_procedure.md`.

## 3quater. The class's positive floor is a SIZE floor (found the same night)
Why the free walk crept: the cut Migdal is a piece of a fold-free net, yet its class margin falls with
the length (KS 0.0081 / 0.0056 / 0.0020 at 80 / 60 / 42 percent). The cell margin is orient x signed
area / max(lp lm, ell2) (a1_plug_march.margin_of_corners), ell2 the reference's plug station spacing
squared: a cell smaller than ell2 scores its AREA, whatever its shape. Probe
`RDE/handoff/f3_2026-09-25/twop_class_size_probe.py` (logs beside it; worst cells by the class margin
v, their shape margin area/(lp lm) = the sine of the angle between the characteristic legs, lp lm / ell2):

| design | min v | its lp lm / ell2 | its shape | where | min SHAPE margin (where) |
|--------|-------|------------------|-----------|-------|--------------------------|
| Migdal, coarse | 0.0113 | 0.018 | 0.62 | plug inlet arc, x 0.058 | 0.42 (plug tip) |
| cap 0.8 vacuum landing | 0.0081 | 0.013 | 0.64 | x 0.051 | 0.44 (plug end) |
| cap 0.6 vacuum landing | 0.0060 | 0.008 | 0.76 | x 0.011 | 0.45 (plug end) |
| cut Migdal at mid-cap | 0.0020 | 0.003 | 0.70 | x 0.030 | 0.50 (plug end) |
| Migdal, fine (280,61) | 0.0130 | 0.022 | 0.60 | x 0.062 | 0.42 (plug tip) |
| step-1 fine A landing | 0.0129 | 0.021 | 0.60 | x 0.062 | 0.42 (plug tip) |
| step-1 fine R landing | 0.0093 | 0.015 | 0.62 | x 0.071 | 0.42 (plug tip) |

In every design, Migdal's own included, the class floor mu0 = m_ref/2 is set by tiny cells at the
plug's inlet arc (x < 0.07 m, y 0.84-0.85: the start-up region where the net is finest) whose shape
is healthy; the nearest thing to a fold anywhere is a shape margin of 0.42-0.50, at the plug's end.
Consequences:
1. The cap posing compresses the stations with the wall, so the inlet cells shrink and the floor
   becomes a LENGTH penalty. The S41 capped landings (vacuum: multipliers -0.10 / -0.02; 2 x ambient
   at cap 0.6: 13 rejections at KS - mu0 -0.0018) were held by this floor, not by a shock: the
   reading "the capped optimum sits on the shock-free boundary" (3bis item 2, M0 addendum item 3) is
   RETRACTED. Their C_F values stand, as optima UNDER this floor; the arcs "unchanged" may be the
   floor too (the binding cells sit on the plug's arc).
2. The step-1 fine far start (twowall:far-start-stalls-at-fold-cliff) is floor-bound the same way at
   its landing (KS - mu0 +0.0028, multiplier -0.033, binding cells at x 0.071); a GENUINE fold lies
   ~1.3 mm further along the Newton direction (its start ladder: KS -0.43 on a regular-sized cell).
   Whether the far start reaches Migdal under a size-free floor is open.
3. The genuine fold detection is unaffected: negative margins mean inverted cells (the compressed
   Migdal's 1159 / 2670, the start ladders' -0.21 .. -0.62 at ~1.3 mm).
The fix, not taken tonight (it changes the class of record of S40-S41): a size-free positive floor --
the shape margin with a degeneracy guard, or ell2 scaled with the design's own station spacing --
re-derived under the tier-invariant transition duty (C-1 / C-2 / C-R and a KAT), then the S41 capped
and ambient walks and the step-1 far start re-run. Finding `twowall:class-floor-size-artefact`.

## 3quinquies. The class corrected (the owner, 2026-09-26 night: "per quanto la taglia risolviamo il problema")
TWO DEFECTS, ONE CLASS. (i) The SIZE floor of 3quater. (ii) Found while re-running under the shape
margin: the free walk (twice the adapted ambient, ends and heights free) crept at 1e-6 per segment
against a wall 40 um away -- eighteen cells flipping from absent to "inverted" (v -0.63) at x 1.22-
1.24 m, far beyond both walls' ends (0.63 m). Probe `RDE/handoff/f3_2026-09-25/twop_afterlip_probe.py`:
those cells, and the ten of the 70 percent cut of 3quater (x 1.35-1.38 m, walls ending at 1.04 m),
are SIMPLE quads traversed backwards -- legs 0.4 mm by 7.6 mm, diagonals crossing, no edge crossing --
the row-growth slivers of the free-edge rows that the single-wall carrier excludes by f_edge (the
two-wall margin took f_edge 0, S40), sitting in the net marched beyond both walls: the PLUME. They
appear and vanish with the design: a discontinuity of the class, not a fold (RK-G in D6's own risk
register: march-topology non-differentiability).
THE CORRECTED CLASS (`TWOP_SHAPE=1 TWOP_NOPLUME=1`; `twowall_cases.json` margin block; the mode of
record without the switches bitwise, gated): the cell margin is the SHAPE margin, signed area over
the legs' product floored only at a degeneracy guard eps2 = 1e-6 ell2 (the sine of the angle between
the two characteristics at every size), and the cells beyond the last wall's end are out of the class
(they touch no wall and cannot feed back upstream in supersonic flow; margin["x_max"] set by the
carrier, traced with the ends in the replays). Both switches live in the ONE margin formula
(a1_plug_march.margin_of_corners) so the record, the sequential replay and the wavefront replay
aggregate the same numbers. Transition duty (tier-invariant clause iii), stage class, gates added:
C-S(a) KAT against the closed form -- parallelograms with legs down to 3e-3 ell score |sin phi| to
1.1e-16; C-S(b) the reference's cells scaled by 0.1 about their centroids keep their margins to
6.9e-10, inside the shoelace formula's own cancellation band 5.1e-7 (derived: EPS x the |x y| products
over the scaled legs' product of the smallest cell); C-S(c) the guard's headroom on the reference
1.8e4. Class records `_twowall_arc_shape/class_2026-09-26.json` (coarse, 8/8) and
`_twowall_arc_shape_fine/class_2026-09-26.json` (fine): m_ref 0.4208 / 0.4196 (the plug's last cells,
where Migdal's characteristics meet at 25 degrees), floors 0.2104 / 0.2098 ..., rho 1373 / 1589; the
plume is 1762 of Migdal's 8331 cells at the coarse rung; the rejector break along +grad J moves from
3.3e-4 m (a plume flip) to 6.6e-4 m (a fold, KS -0.61) -> tr0 1.17e-4 m. The 8-knot unconstrained
landing reads KS -0.90: rejected as before. The intermediate shape-only records (before the plume
cut) are kept as `*_shapeonly_*` beside the records of record.
After the plume cut the 70 percent cut of Migdal has 0 inverted cells (min 0.457) and the free walk's
landing +- 0.4 mm reads KS 0.5198 -> 0.5196: smooth.
THE WALKS RE-RUN under the corrected class (T start, Newton metric, 16 x 6, coarse rung, ends at the
cap unless said; records `_twowall_*_shape/walk_TN_2026-09-27.json`, ~17-21 min each; the "size floor"
column = the same walk under the class of 3bis/3ter):

| case | Migdal cut at L | under the size floor | CORRECTED class | gain over the cut | note |
|------|-----------------|----------------------|-----------------|-------------------|------|
| vacuum, cap 0.8, exit pinned | 1.578393 | 1.579836 | **1.580026** | +1.6e-3 (+0.103 %) | +1.5e-4 over the FULL Migdal 1.579880: inside the coarse bias 2.9e-4 -- indistinguishable from the full length at this rung |
| vacuum, cap 0.6, exit pinned | 1.569476 | 1.575268 | **1.575936** | +6.5e-3 (+0.412 %) | 99.75 % of the full length |
| adapted ambient, cap 0.8, lip free | 1.471096 | 1.471297 | **1.471819** | +7.2e-4 (+0.049 %) | lip +1.0 mm, p_lip/p_a 1.09 -> 1.34 (a recompression at the lip: the length-constrained optimum exits above ambient, Rao's corner) |
| adapted ambient, cap 0.6, lip free | 1.468618 | 1.468693 | **1.469346** | +7.3e-4 (+0.050 %) | lip +0.5 mm |
| 2 x ambient, cap 0.8, lip free | 1.363798 | 1.364396 | **1.364872** | +1.07e-3 (+0.079 %) | lip -2.3 mm, A_e/A_i 3.953 -> 3.933 |
| 2 x ambient, cap 0.6, lip free | 1.367760 | 1.367947 | **1.369544** | +1.78e-3 (+0.130 %) | lip -6.8 mm, A_e/A_i 3.716 -> 3.658 |
| 2 x ambient, cap 0.8, ENDS FREE from mid-cap (u0 0) + both heights free | best cut 1.370230 (at 44 %) | 1.370898 (shape only) | **1.371714** | +1.48e-3 (+0.108 %) over the BEST cut | ends stay at 42 % (x 0.629 / 0.626); tip +4.5 mm, lip -2.4 mm, A_e/A_i 3.27 -> 3.23; p/p_a at the exit 1.08 / 0.95 -> 1.31 / 1.31 |

THE READING under the corrected class:
1. What the size floor had hidden: the knots now move 2-9 mm (they moved 0.3-1 mm before) and the arcs
   move too (plug x_a 0.0729 -> 0.0737 / 0.0711 / 0.0754 / 0.0701, t_a within 1e-3; the shroud's within
   1e-3): the class no longer pins the inlet. The landings are NOT stationary (|grad| 0.1-0.3; the arc
   gradient -0.27 at cap 0.6, 2 x): the 16-segment budget and the driver's radius stop them, not the
   class (KS 0.46-0.53 against the floor 0.21, multipliers ~ -0.002). More budget would move them
   further; the SIGNS of the readings below do not depend on it.
2. In vacuum at 80 percent length the capped design reaches the full Migdal's thrust (+1.5e-4, inside
   the instrument's bias): at this rung Migdal's last 20 percent of length is worth nothing; at 60
   percent the cost is 0.25 percent. The gain over the CUT Migdal is +0.10 / +0.41 percent.
3. At ambient the exit becomes a design: adapted, the lip rises and the exit RECOMPRESSES (p 1.3 p_a at
   both walls); over-expanded, the lip drops (2-7 mm). The gains over the cut Migdal are 0.05-0.13
   percent, three to ten times what the size-floored class allowed (3ter's "the cut Migdal within the
   bias" is superseded for the optimum; it still holds for the START).
4. The length as an outcome (2 x ambient): the free design keeps its ends at 42 percent of Migdal's
   length -- the cut Migdal's own maximum sits at 44 percent -- with a smaller exit (A_e/A_i 3.23)
   compressed to 1.31 p_a, and beats the best truncated ideal by 0.11 percent and the 80 percent
   design by 0.50 percent. The ends' gradient at the landing is +0.045 per metre (the optimum a little
   longer than 42 percent); the Newton metric floors that direction (two negative eigenvalues in the
   knots' block, asymmetry 2-4 at these starts) and the walk does not take it: a driver limit,
   recorded, not a physics one.
5. Both walls still end together in every capped run: the cap is active in vacuum and at the adapted
   ambient; over-expanded the free run keeps them together too (0.629 / 0.626), with the plug's part
   beyond the lip's last characteristic still unrepresentable without the free jet.
Figures 26 / 27 / 28 `_shape` in `_twowall_cap/figs/` (`TWOP_FIGTAG=_shape` on the same generators).
The findings: `twowall:class-floor-size-artefact` DISCHARGED, `twowall:plume-sliver-cells-flip` minted
and DISCHARGED in the same window (the plume cut), `twowall:cap-ends-sigmoid-saturate` re-read (the
u0 = 0 walk moved its ends 1 mm on a gradient of +0.045 per metre: the metric, not the sigmoid).
The fine far start (ramp 0.75, 11.6 / 8.8 mm off Migdal -- the size floor had rejected this ramp and
sent S41 to 0.5) under the corrected class (`_twowall_arc_shape_fine/walk_RN_2026-09-27.json`, 10 x 6,
31 min): 1.579275 -> 1.579436, +1.6e-4 of the 3.8e-4 gap to Migdal's arcs in ten segments, still
climbing (+2e-6 per segment at the end, |grad| 0.096, KS 0.43 against the floor 0.21: not class-bound)
and not yet toward Migdal in shape (plug gap 11.6 mm unchanged, shroud 8.8 -> 8.7 mm). Under the shape
margin alone the same start stalled at 1.579327 in nine records with ten rejected probes (the plume
slivers, `walk_RN_shapeonly_2026-09-26.json`). The "fold cliff" of section 3 is therefore two
artefacts of the class, not a cliff; what remains is a BUDGET question (a segment chain from this
landing, TWOP_START=F) -- the far-start finding is re-read, not closed.
Class records of record: `_twowall_arc_shape/class_2026-09-27.json` (the re-derivation with the
committed code; its 2026-09-26 twin, identical in every number, removed) and
`_twowall_arc_shape_fine/class_2026-09-27.json`.

## 3sexies. The RDE procedure on a Q2D outflow: the tournament, the free jet, the separation (the owner, 2026-09-27 night)
THE OWNER'S WORDS, in order: "nel frattempo puoi girare un caso ... Q2D di un RDE con gola e poi prendiamo il suo outflow
e lo espandiamo in ugello facendo un torneo"; "beh espandi direttamente il flusso chocked termicamente"; "il confronto
sarà tra gli ugelli creati con lo stato mediato alla stechmann contro i nostri creati con le fasi che votano"; before
bed: "In ordine le cose da fare sono: setup delle run con l'outflow del RDE (+ possibile aggiunta del problema
meridiano), getto libero, trattazione della separazione". The meridional problem = the swirl the meridional march
leaves out (8.8 percent of the exit's kinetic energy), added as a free vortex (item C below).

A. THE SOURCE AND THE TWO DESIGN STATES (`validation/a1_rde_tournament.py` [X-RDET], constants
`rde_tournament_cases.json`, artifacts `_rde_tournament/`). The Q2D THOR_CAv3 limit cycle (leg D, t 15.5 ms): the last
chamber cell column (x 104.80 mm), 1799 azimuthal cells, EVERY one supersonic (M_x 1.442 .. 1.841: thermally choked,
no throat needed), extracted by `RDE/handoff/f3_2026-09-25/q2d_exit_extract.py` into
`_rde_tournament/q2d_thor_cav3_exit_t15.5ms.npz`; mass flow through the inlet annulus (outer radius 68 mm, gap
14.15 mm) 0.4536 kg/s; P0 0.41 .. 3.33 bar, T0 1504 .. 2658 K, v -922 .. +510 m/s (theta-mean +172 m/s). One snapshot
holds a whole period (T0: a single rotating wave, time at a point = angle at an instant), so equal azimuthal sectors
are equal durations. The STECHMANN state (Stechmann, Heister & Harroun: gamma and M frozen, the nozzle designed at
the time-mean chamber state) = the theta-arithmetic mean of the exit's meridional stagnation state: gamma 1.27744,
R 342.65, T0 2000.6 K, P0 1.4166 bar, M_x 1.5561 (`gas_stechmann.json`); the mass-weighted mean, reported as the
sensitivity, is very different in pressure (P0 1.899 bar, T0 2147 K, M_x 1.604). The PHASES: K = 12 and 24 equal
sectors (`family_K12.json`, `family_K24.json`), each with its own gamma, R, T0, P0, M_x and v; K 12 spans P0
0.46 .. 3.09 bar, M 1.459 .. 1.785; the sectors' mean mass flow = the exit's inside K_RICH eps n.
The STECHMANN NOZZLE: GENO's Migdal perfect pair (nozzle_type 9) for the time-mean state adapted at p_a 0.05 bar
(an altitude ambient: the exit's mean static pressure is 0.34 bar), `RDE/handoff/f3_2026-09-25/geno_rde/stech_run`
(A_e/A_i 3.3674, 1-D M_e 2.7738, C_F,vac 1.593085; GENO's NASA-7 entropy inversion needed the a7 shift of the
constant-cp polynomial, declared). The tournament's posing = the S41 cap posing on that pair: cap 0.8 of its
length, ends at the cap (u0 10), the lip height free, the corrected class (shape + plume cut, class record
`_rde_tournament/stech/class_2026-09-27.json`), Summerfield closure; the start S0 = the pair cut at the cap + the
tail deflection (T start).

B. THE TABLE CLAMP (found in the first tournament pass, every number of that pass withdrawn). The constant-gamma
tables were built by `a1_ideal_march_jax.build_tab_gconst` on its absolute range [1050, 3900] K; the RDE exhaust
expands below 1000 K (the Stechmann exit is at 968 K), so the table CLAMPED: the wall pressure stuck at 7280 Pa where
the isentrope gives 5000 Pa. `a1_twowall.tab_gconst` builds the same formula on a declared range (T_tab [300, 3900]
K); gate T-0: the extended table at the Stechmann exit p 5000.000 Pa vs the closed-form isentrope, rel 9.1e-8 inside
the grid's interpolation band 4.7e-7, and the builder's table REJECTED there (7280.1 Pa). The first pass's records
are archived in `_rde_tournament/*/clampedtab/` (S1 1.449944, the class record, the V1 attempt); none is used.

C. THE CARRIER'S NEW OPTIONS (`a1_twowall.py`; the default path BITWISE: T-1 the S41 record 1.579660988049).
TWOP_GAS (the posing's gas and state from a file: T-2 the defaults bitwise); TWOP_MU = the PHASES VOTE (a family of
inflow states on the same walls, each with its own table and uniform start at its Mach; J = sum_k w_k C_F,k in units
of the posing's P0 A*; T-4 one phase = the posing bitwise; T-6 the replay's adjoint vs central differences rel
4.5e-3); TWOP_MU_CLASS = where the fold class is read (ref = the time-mean state only; all = every phase, a KS
soft-min over the phases); TWOP_SWIRL = every phase's FREE VORTEX (Gamma = y_mid v, the table at the total
stagnation state, the five swirl cells of `a1_swirl_march.swirl_cells_2w`: SW-1 the two-wall radial-equilibrium duct
preserved to 1.7e-14, SW-2 Gamma = 0 bitwise, SW-3 alive: -2.85e-3 on the cut Stechmann pair's 12-phase C_F, SW-4 the swirl replay = the record and its adjoint
inside the central-difference LADDER's band (the knot derivative is 5e-5 with the swirl and the closure: one step of
1e-5 misses it by 4 percent in truncation, 1e-6 by 3.5e-3, with or without the closure -- `twop_sw4_kink_probe.py`),
SW-5 the swirl phases' margin replayed sequentially = the record's inside the Newton tolerance over the smallest leg); TWOP_JET (item E); TWOP_SEP / TWOP_SEP_CLASS (item F); TWOP_U0_S (the shroud's own end), TWOP_START=F.
Gates of record: `_rde_tournament/gates_2026-09-27.log` 9/9 (T-0 .. T-7; T-7 = the table box: every phase's coldest state
above T_tab[0] -- 745.6 .. 1109.4 K, where the builder's 1050 K edge would clamp 10 of the 12 phases), `swirlgates_2026-09-27.log` 5/5,
`jetgates_2026-09-27.log` 5/5, `sepgates_2026-09-27.log` 3/3; the lip-jet oracle [X-LJET] 9/9; the wavefront replay
WF-1..4 (`a1_twowall.py` stage wavefront: WF-4 the row padding of item G bitwise).

D. THE TOURNAMENT (stage eval, `_rde_tournament/eval_2026-09-27.json`; p_a 0.05 bar, Summerfield; C_F in units of the
Stechmann P0 A*; the mixture specific impulse on the Q2D mass flow). The Stechmann designs first:

| judge | S0 = the cut Stechmann pair | S1 = walked on the time-mean state | S1 - S0 |
|-------|-----------------------------|------------------------------------|---------|
| time-mean state | 1.446124 (896.50 N, 201.54 s) | 1.446724 | +6.0e-4 |
| 12 phases | 1.376235 (853.17 N, 191.80 s) | 1.376099 | -1.4e-4 |
| 24 phases | 1.374853 | 1.374727 | -1.3e-4 |
| 12 phases + swirl | 1.373383 | 1.373061 | -3.2e-4 |
| 24 phases + swirl | 1.371726 | 1.371512 | -2.1e-4 |

The PAIRED REFINEMENT (the same designs re-marched at the fine rung (280, 61): the '@fine' judges of
`_rde_tournament/eval_2026-09-27.json`; M0 S41 item (1): a coarse difference counts only if it survives it):

| judge, fine rung | S0 | S1 | S1 - S0 (coarse) |
|------------------|----|----|------------------|
| time-mean state | 1.445830 | 1.445958 | +1.3e-4 (+6.0e-4) |
| 12 phases | 1.375898 | 1.375674 | -2.2e-4 (-1.4e-4) |

S1's gain at its own state shrinks to a fifth, and at the fine rung S1 FOLDS at its own state too (1 of 1 out of the
class: the lip compression's focus resolved inside the walls); its loss under the phases survives and grows. S0's
coarse bias: -2.9e-4 (mean) and -3.4e-4 (12 phases).

READING (Stechmann designs). (1) The time-mean state OVERSTATES the nozzle: the 12-phase judge gives the cut pair
C_F 1.3762 against 1.4461 (-4.8 percent) and the nozzle's gain over the bare exit 0.1367 against 0.1545 (-11.5
percent); K 24 moves the 12-phase numbers by -1.4e-3 (the binning's own error), the swirl by -2.9e-3 more. (2) The
pair itself is not shock-free in every phase: the two post-wave sectors (M 1.78, P0 2.8-3.1 bar) fold 74-87 mm
downstream, mid-channel (70 / 86 inverted cells; `RDE/handoff/f3_2026-09-25/twop_phase_fold_probe.py`); every
other phase keeps +0.50. (3) A walk on the time-mean state (S1, 16 x 6, 1221 s: +0.041 percent there, lip raised,
p_lip 1.06 -> 1.32 p_a) is WORSE under every phase judge: its lip recompression puts a compression focus just past
the exit AT the time-mean state (its class reads +0.51) that moves 0-3 mm inside the nozzle in EVERY other phase --
all 12 fold: phases 0-9 with 1-4 inverted cells at the lip (bow-tie crossings among them, probed in phases 2 and 8,
`twop_lip_cells_probe.py`), phases 10-11 on top of their own folds (76 / 85 cells) -- and phase 10's march
loses certification (62x); at the design ambient phases 7 and 8 detach (Summerfield margins -0.005 / -0.139; the
pair's own phase 8 sits at +0.025). The shape margin cannot warn of such a fold: it reads the sine of the angle
between the families until the characteristics cross (finding twowall:shape-margin-blind-to-convergence). (4) The
phase view of the exit: the lips range 0.36-1.97 p_a on the pair (the low-pressure phases carry a lip shock in the
jet), the coldest states 746-1109 K. (5) The phases voting: with the class read at the time-mean state only (V1m)
the start ladder finds a phase's march uncertified 1.4 mm along the gradient (23.6x on the walk's own ladder; the
same point re-marched on the corrected closure: 1.07, in phase 2, `twop_v1m_ladder_probe.py`), so the trust region
starts at 2.5e-4 m (the single-state walk: 1.0e-3 m). [CORRECTED the same night: a first reading said V1m "took no
step in two segments" -- a misreading of the checkpoints: a segment's trial is judged at the NEXT segment's base and
each V1m run was interrupted before that (the mapping cap, the padding restart, a stop on that very misreading); no
V1m trial had been judged; the walk was resumed.] The class must hold in every phase on PRINCIPLE: a phase whose net
folds has no shock-free thrust (the march sums a multi-valued net), so a vote that counts it is not a design of the
class; the operative posing is V1, every phase shock-free
AND attached (TWOP_MU_CLASS=all TWOP_SEP_CLASS=1), and V1s = V1 with the swirl (state in H).

D2. THE TOURNAMENT'S TABLE (stage eval with the seven judges in parallel + evalmerge, `_rde_tournament/eval_2026-09-27
.json`, the walks' RECORDS: V1 16 x 6 in 13703 s, V1m 16 x 6; a provisional table at V1's segment 8 was committed in
7abddeb and is replaced here). C_F in units of the Stechmann P0 A*, p_a 0.05 bar, Summerfield; then the phases out of
the fold class / with a detached wall / uncertified:

| judge | S0 | S1 | V1m | V1 |
|-------|----|----|-----|----|
| time-mean state | 1.446124 | 1.446724 | 1.446150 | 1.446149 |
| 12 phases | 1.376235 | 1.376099 | 1.376254 | 1.376283 |
| 24 phases | 1.374853 | 1.374727 | 1.374871 | 1.374896 |
| 12 phases + swirl | 1.373383 | 1.373061 | 1.373386 | 1.373362 |
| 24 phases + swirl | 1.371726 | 1.371512 | 1.371733 | 1.371692 |
| time-mean state, fine (280, 61) | 1.445830 | 1.445958 | 1.445833 | 1.445795 |
| 12 phases, fine (280, 61) | 1.375898 | 1.375674 | 1.375904 | 1.375904 |
| 12 phases: folded / detached / uncertified | 2 / 0 / 0 | 12 / 2 / 1 | 2 / 0 / 0 | 0 / 0 / 0 |
| 24 phases | 5 / 1 / 0 | 19 / 3 / 0 | 5 / 0 / 0 | 2 / 0 / 1 |
| 12 phases + swirl | 4 / 3 / 0 | 5 / 3 / 2 | 2 / 3 / 0 | 0 / 3 / 1 |
| 24 phases + swirl | 8 / 7 / 1 | 10 / 7 / 1 | 5 / 7 / 0 | 2 / 6 / 1 |
| 12 phases, fine | 2 / 0 / 0 | 12 / 2 / 0 | 3 / 0 / 1 | 1 / 0 / 1 |

READING. (1) THE PHASES VOTING FIND NO MORE THRUST THAN THE INSTRUMENT RESOLVES on this capped posing: V1 - S0 over 12
phases is +4.8e-5 at the coarse rung and +5.9e-6 at the fine -- the time-mean design, once its two post-wave folds are
removed (two sub-millimetre restoration steps), is the phase vote's optimum within the coarse bias; T3's argument
survives the mild per-phase variation of gamma (1.268-1.293) and M (1.46-1.79) here. V1 beats the walk on the
time-mean state S1 by +1.8e-4 / +2.3e-4 (coarse / fine). (2) What the vote DOES deliver is the class: V1 is shock-free,
attached and certified in all 12 phases of its judge at its rung (S0: 2 folded; S1: 12 folded, 2 detached, 1
uncertified). (3) Its measured limits: 24 bins expose 2 folded sectors and 1 uncertified (the extreme post-wave
states between the 12-bin means); the swirl detaches three low-pressure phases of EVERY design (the free vortex lowers
the plug-side pressure; V1 was designed without it); the fine rung resolves one fold and one uncertified phase that
the coarse class did not see -- each a limit of the 12-bin, swirl-free, coarse design, the next rung of the vote.
(4) Off design (12 phases, Summerfield; `offdesign_2026-09-27.json`, figure 30 panel d) V1 trades a little of the low
ambient for the high one: -1.1e-4 against S0 at 0.02 bar, +1.3e-4 .. +4.6e-4 from 0.15 to 0.4 bar, and it detaches
fewer phases at 0.25 / 0.30 bar (9 / 11 against 11 / 12) -- it expands slightly less (its lip at 1.16 p_a against
1.06 on the time-mean state). (5) V1m (the class read at the time-mean state only; 16 segments after the checkpoint
misreading was corrected): +1.9e-5 over S0 on 12 phases and the pair's two post-wave folds kept (its class cannot see
them); at the fine rung 3 folded and 1 uncertified -- the all-phase class is what makes V1 a design of the class.

E. THE FREE JET (`a1_plug_march.plug_march(lip_jet=...)`, `validation/a1_lipjet.py` [X-LJET] + `lipjet_cases.json`):
at the lip F a centred Prandtl-Meyer fan from the lip speed to the ambient speed (Gauss-Legendre on the tabulated
gas, `pm_turn`), then the free-edge cell at p_a after the lip -- the plug may run on under the jet; an OVER-expanded
lip (needs a lip shock) freezes the jet at the lip's speed and enters the class as the lip margin p(q_F)/p_a - 1 < 0.
The planar simple-wave oracle with the fan born mid-march: 9/9 (quadrature 4.4e-16; every station in band; the
no-jet march past F's C- uncertified). On the tournament posing (jetgates 5/5): JT-1 both ends at the cap -- the jet
changes no wall point (bitwise) and joins the lip margin +0.0586 (under-expanded) to the class; JT-2a the plug run on
beyond a lip at mid-way: the LIP'S FIRST CHARACTERISTIC LANDS PAST THE PLUG TIP (the no-jet top row ends at x 1.90
against the tip 1.279), so the jet leaves every plug point and J bitwise -- the plug is in the internal flow's domain
of dependence; JT-2b the jet region's momentum and mass residuals are second-order discretisation (1.52e-3 -> 3.78e-4
and 1.64e-3 -> 4.02e-4 from (140,31) to (279,61), ratios 4.02 / 4.07); JT-3 replay = record, adjoint vs FD 8.3e-3;
JT-4 an over-expanded lip (0.6 bar) out of class, the march finite. Probes `twop_jet_closure_probe.py` and a shorter
shroud (lip at 16 percent of the length): even there the first characteristic lands past the tip. READING: under the
cap the jet cannot reach the plug; the capped designs' thrust is jet-independent and the jet enters only through the
lip margin -- and that entry would forbid the ordinary over-expanded lips of the low-pressure phases (a lip shock in
the jet, not on a wall), so the tournament's class does not carry it; separation is the wall-side constraint (F).
Two gate defects found and fixed on the way: the harness rebuilt the carrier without clearing TWOP_JET (JT-2's
"without the jet" march ran WITH it: both certificates 0.466), and JT-2's first premise ("without the jet the march
past F's C- is uncertified") holds only when the plug reaches past F's C-, which no capped posing does.

F. THE SEPARATION (D-GSEP, criterion class R2 declared empirical; `twowall_cases.json` separation block). The CLOSURE
(TWOP_SEP = summerfield | schmucker): free-shock separation -- the wall's gauge push weighted by an attachment weight
that follows the RUNNING MINIMUM of the margin p_w/p_sep - 1 (sigmoid width 0.02; 1/2 exactly at the first point below
p_sep; a separated wall never reattaches). Its first form, a cumulative product of the sigmoids, ACCUMULATED the
near-separation factors: it detached the cut Stechmann plug at 0.30 bar 2.3 stations early (x 0.646 against the
criterion's 0.667) and discounted the attached wall upstream -- found by SC-2, replaced. T-5a inert at 0.05 bar
(bitwise); T-5b at 0.30 bar both walls detach (plug x 0.667, shroud x 0.565) and the closure J 0.851696 lies between
the hard cuts at margins -/+3 widths (0.833023, 0.869776; the criterion's own 0.851174; attached 0.718047). The CLASS
option (TWOP_SEP_CLASS): every wall point's margin joins the KS as mu0 + margin, so an in-class design keeps both
walls attached: SC-1 inert at 0.05 bar (smallest margin +2.02, KS unchanged inside its union bound), SC-2 at 0.30 bar
out of class and the first negative-margin point = the closure's detachment on both walls, SC-3 replay = record to
1.8e-13 (8.1e-12 band over 9086 entries), adjoint vs FD 6.2e-8. The OFF-DESIGN sweep (stage offdesign, `_rde_tournament/offdesign_2026-09-27.json`; one record per design and
judge, the march being independent of p_a without the jet), the cut pair S0 (C_F; phases with a detached wall):

| p_a (bar) | 0.02 | 0.05 | 0.075 | 0.10 | 0.15 | 0.20 | 0.30 |
|-----------|------|------|-------|------|------|------|------|
| time-mean, attached | 1.53349 | 1.44612 | 1.37332 | 1.30051 | 1.15489 | 1.00928 | 0.71805 |
| time-mean, Summerfield | 1.53349 | 1.44612 | 1.37332 | 1.30051 | 1.15515 | 1.02677 (1) | 0.85170 (1) |
| time-mean, no nozzle | 1.31785 | 1.29164 | 1.26979 | 1.24795 | 1.20426 | 1.16057 | 1.07320 |
| 12 phases, attached | 1.46360 | 1.37623 | 1.30342 | 1.23061 | 1.08500 | 0.93938 | 0.64815 |
| 12 phases, Summerfield | 1.46360 | 1.37623 (0) | 1.30507 (3) | 1.23906 (5) | 1.12697 (7) | 1.04277 (8) | 0.90597 (12) |
| 12 phases, Schmucker | 1.46360 | 1.37636 (1) | 1.30796 (5) | 1.24832 (6) | 1.15677 (8) | 1.08006 (9) | 0.94975 (12) |
| 12 phases, no nozzle | 1.26578 | 1.23957 | 1.21772 | 1.19588 | 1.15219 | 1.10850 | 1.02113 |

READING: the time-mean state separates at ONE ambient (0.20 bar), the phases at a spread of them -- the three
lowest-pressure phases already at 0.075 bar, half the cycle by 0.10-0.15 bar; the closure keeps the separated wall
from pulling (the 12-phase C_F at 0.30 bar 0.906 against 0.648 attached) but the cut pair falls below the bare exit
between 0.10 and 0.15 bar under Summerfield and between 0.15 and 0.20 bar under Schmucker (the walls over-expand
every phase before it detaches); Schmucker detaches earlier than Summerfield at these wall Mach numbers and prices the
separated nozzle higher. S1 differs from S0 by at most 1.6e-3 (0.25 bar) and detaches 2 phases already at 0.05 bar. With the swirl (12 phases + swirl) three phases
detach at 0.035-0.05 bar.

G. INSTRUMENT DEFECTS FOUND AND DISCHARGED IN THE WINDOW. (i) The wavefront replay closed over the FIRST phase's gas
tables in its jitted steps (record/replay mismatch 0.036 on the 12-phase posing): the tables are now an argument of
every step (WF-1..3 PASS). (ii) The 12-phase walks died of the kernel's memory-mapping cap 65530 ("LLVM ERROR: Unable to allocate section
memory"): V1 in its first restoration step, V1m inside segment 2. Cause, measured (`RDE/handoff/f3_2026-09-25/
twop_mapcap_probe.py`): every jitted step of the wavefront replay takes the WHOLE point array, whose row count differs
per phase and per design -- ONE 12-phase J gradient added +46051 mappings. The row count is now rounded up to
rows_block 1024 (the extra rows never read; WF-4 bitwise): +5733 for the same gradient. The cache is also cleared above
map_clear at every record (Metric.march_record) and inside the restoration; V1m resumed from its checkpoint, V1
relaunched. (iii) The swirl march's certificate 2.15 of the first pass was the table clamp (0.772 on
the extended tables; SW-3 keeps the strict <= 1). (iv) GENO's NASA-7 entropy inversion (a7 shift). (v) The jet
gates' harness (E).

H. HOW THE NIGHT WENT (the state at the first commit, ~05:00, kept as written; the landings are in D2). V1 -- the
phases voting with every phase
shock-free AND attached (TWOP_MU_CLASS=all TWOP_SEP_CLASS=1, K 12, the tournament's posing, T start = S0) -- is in
its restoration: the pair starts out of that class by the two post-wave folds (KS -0.657 against the floor 0.2351);
two restoration steps (3.6e-4 then 1.8e-4 m along the soft-KS gradient, 10 records) put it IN CLASS in every phase
(KS +0.2598, the binding entry a separation margin +0.025 -- the low-pressure phase 8) with C_F 1.376236 (+1.4e-6
over S0): the post-wave folds of the Stechmann pair are MARGINAL, a sub-millimetre wall change removes them. The
walk then started (Newton metric: asymmetry 4.59, floor 18.4; |grad| 8.6e-3). Its landing, the eval and the off-design sweep of it follow in a
follow-up commit. V1m (the class at the time-mean state only) was resumed after the checkpoint misreading of D
(its log carries the correction). V1s (V1 with the swirl) died of the mapping cap in its first restoration step:
the swirl phases replay SEQUENTIALLY (no wavefront kinds for the swirl cells) and that branch did not pad the margin
stack for a fresh margin dict (one module per cell count; fixed the same night, gate SW-5). Measured after the fix
(`twop_mapcap_probe.py 1024 swirl`): one 12-phase swirl design step (record + J and margin gradients) +36089 mappings,
the next +15 -- bounded -- but 22-25 min per step, so a swirl WALK (hours per segment) waits for the swirl cells in
the wavefront replay with the circulation as a parameter: the next engineering step for the meridional problem. The swirl JUDGES
run (the designs above are all judged with their swirl). Figure 30 `_rde_tournament/figs/30_rde_tournament.png`
(generator `RDE/handoff/f3_2026-09-25/twop_rde_tournament_fig.py`, untracked like figures 26-29): (a) the 12 sectors'
P0, M_x, v; (b) the walls against S0; (c) per-phase C_F against S0 under the 12-phase judge; (d) off design, 12
phases, Summerfield, against S0 and the bare exit.

## 3septies. The independent referee (the owner, 2026-09-27 morning)
THE OWNER'S WORDS, in order: "fare un comparison tra stechmann sempre attaccato e la nostra run sqp non è molto
fair. I due metodi devono produrre un profilo che viene percorso indipendentemente da un terzo runner che calcola
la pressione. Questo perchè sono due metodi di design"; "Sarebbe anche il caso di trovare una maniera ridotta per
fare questa valutazione, come sottomodelli della separazione locale"; "risolvi questa cosa e prepara due mesh 3D";
"22 milioni di celle è esagerato"; "la camera non mesharla, la mesh parte da una soluzione rde sulla parete di
entrata e comprende solo l'ugello"; "quello che testeremo è un ugello alla stechmann (con l'entrata fissa allo
stato medio) vs il nostro ottimizzato col torneo (tutti e due devono tenere in conto delle separazioni e devono
essere troncati ad un valore da te scelto di lunghezza)".

A. THE FLAW OF SECTION 3sexies' JUDGE. The tournament's judge was our own two-wall march with the Summerfield
closure: the engine the SQP optimises against (V1 is tuned to the judge's class, S0 is not) and a shock-free MOC
that sums a multi-valued net where a phase folds (S0 was judged on 2 folded phases). Twice biased toward our
method. The per-phase MOC numbers stay the DESIGN-side diagnostics; the verdict belongs to a runner independent
of both methods, shock-capturing, with separation modelled and not closed by a formula: CFD.

B. THE CONTEST AS THE OWNER FIXED IT. S0 = Stechmann's method: GENO's perfect pair for the theta-mean (time-mean)
state of the Q2D exit, its inlet FIXED at that state, attached at its design point (Summerfield margin +2.0 at
0.05 bar), cut at the chosen length; V1 = our tournament: the 12 phases voting, every phase shock-free AND attached
(TWOP_MU_CLASS=all TWOP_SEP_CLASS=1), the same length. The length: 86.95 mm = 80 percent of Stechmann's plug (the
tournament's cap). Reason: past it the plug still yields 2.6e-5 of C_F per mm over the 12 phases (the 22 mm to the
full plug are worth 1.3e-4 in all, `twop_ends_probe.py`) and the shroud's end yields nothing (its slope is ~0
there); a convenient truncation, not an optimum -- the chain re-runs at 60-70 percent unchanged. Both walls end
together because the posing pins both ends at the one cap (S41 step 2, the owner's rule) and, at this ambient, the
shroud is length-indifferent; a plug longer than the shroud is computable now (the jet), a shroud longer than the
plug is not (the wake behind the tip is not a boundary of the march).

C. THE REDUCED EVALUATION (2D axisymmetric, per phase). `RDE/THOR/THOR_GPU/NOZZLE_2026-09-27/run_wedge_phase.py`:
a 1-degree wedge of the nozzle alone (the meridional mesh of the 3D generator, 47 x 32 cells, 2 cells in theta,
rotational periodicity 200), the phase's inlet state on a 405 supersonic inlet (M, static T and p from the
sector's (gamma, M, T0, P0) of `family_K12.json`, the sector's composition from the Q2D exit; `phases_405.json`),
Euler, ONERA-7 (finite-rate or frozen), slip walls, the ambient at 0.05 bar at rest, MOSE_open (CPU, 3 ranks x 8
threads) time-accurate to 1 ms (18 flow-throughs). Post (`post_wedge.py`): the wall pressure on plug and shroud,
C_F in the p_a gauge with the MOC's own definition, shocks (rises > 5 percent), and the LOCAL SEPARATION SUB-MODEL:
Summerfield (p_w < 0.35 p_a) or Schmucker on the computed wall pressure gives the separation point, downstream of
which the wall is credited p_a (free-shock separation open to the ambient -- the same convention as the MOC
closure, now on a shock-capturing pressure). Frozen chemistry runs a phase in 1.25 min; finite-rate in 22 min
(RADAU5 per cell as the plume forms); phase 0 frozen vs reacting differ by 1.2e-3 in C_F (0.06 percent).
Found and worked around: MOSE_open's [MOSE-Probes] section kills a time-accurate run at step 1 (NaN, then an
integer divide by zero) -- probes off; the binary takes 32 OpenMP threads per rank when OMP_NUM_THREADS is unset
(load 220 on 96 cores) -- pinned to 8.
| phase | S0 CFD | S0 MOC | V1 CFD | V1 MOC | CFD/MOC - 1 | separation (Schmucker) |
|---|---|---|---|---|---|---|
| 0 | 2.15685 | 2.16307 | 2.15660 | 2.16290 | -0.29 % | none |
| 1 | 1.64608 | 1.65089 | 1.64593 | 1.65086 | -0.29 % | none |
| 2 | 1.22086 | 1.22464 | 1.22081 | 1.22477 | -0.31 % | none |
| 3 | 0.93748 | 0.94055 | 0.93749 | 0.94072 | -0.33 % | none |
| 4 | 0.75529 | 0.75788 | 0.75534 | 0.75807 | -0.34 % | none |
| 5 | 0.69321 | 0.69565 | 0.69328 | 0.69585 | -0.35 % | none |
| 6 | 0.55585 | 0.55791 | 0.55595 | 0.55810 | -0.37 % | none |
| 7 | 0.46356 | 0.46537 | 0.46369 | 0.46557 | -0.39 % | none |
| 8 | 0.39441 | 0.39611 | 0.39455 | 0.39625 | -0.43 % | plug 181 / shroud 167 mm (both designs) |
| 9 | 2.32911 | 2.33497 | 2.32878 | 2.33501 | -0.25 % | none |
| 10 | 2.81997 | 2.82780 | 2.81956 | 2.82753 | -0.28 % | none |
| 11 | 2.48747 | 2.49451 | 2.48714 | 2.49430 | -0.28 % | none |
| **12-phase average** | **1.372132** | 1.376235 | **1.372048** | 1.376283 | -0.30 % | Schmucker credit +1.5e-04 / +1.4e-04 |

READING OF THE REFEREE (2D axisymmetric Euler per phase, frozen chemistry, the same 12 states both designs were
judged on; `CASE_2D/batch_frozen_table.json`, figure `CASE_2D/batch_frozen.png`): (1) the CFD sits 0.28-0.31
percent BELOW the MOC in every phase for both designs -- the coarse 2D discretisation (47 x 32, MINMOD) against the
MOC's own coarse bias (+2.9e-4 over the 1-D ideal in the S41 gates), a systematic offset that cancels in the
comparison; (2) NO shock and NO separation in any phase for either design at 0.05 bar (Summerfield never
triggers; Schmucker flags only the lowest-pressure phase 8 at the last cells of both walls, where p_w falls to
0.9 p_a: +1.8e-3 on that phase, +1.5e-4 on the average, identical for the two designs); (3) V1 - S0 = -8.4e-5 by
the referee against +4.8e-5 by the MOC: the two designs differ by less than the referee resolves, in either
direction -- the tournament's conclusion "no more thrust than the instrument resolves" stands under an
independent runner; (4) reacting vs frozen chemistry on phase 0: +1.2e-3 (0.06 percent), the frozen batch is the
one of record (1.25 min per phase against 22). The 3D nozzle-only runner is built but not run.


D. THE 3D REFEREE, NOZZLE ONLY. The first build attached the two nozzles to the THOR coarse-ambient v2 chamber
(chamber + injector verbatim, point-matched, 22.3 M cells; then 13.7 M with the new blocks at 0.4 degree and a
1:2 theta chimera at the chamber exit) -- the owner: too many cells, and no chamber at all: the mesh starts from an
RDE solution on the inlet plane. Those meshes, bc and ICs were deleted; the generator keeps both modes.
`gen_nozzle_mesh.py --nozzle-only`: 10 sectors x {Ambient, Nozzle, Outer}, 30 blocks, 3.24 M cells (channel 47 x
32 x 90 per sector, dx 1.85 mm, dr 0.44 -> 1.55 mm, 0.4 degree; the exhaust beside the shroud to r 160 mm and
150 mm downstream, the plug base a wall, a 5 mm slip sting for the polar axis); every interface a 101 connection.
bc (`build_bc_thor_nozzle.py`): the inlet = MOSE's 410 "mapped state from a time-varying file, periodic" -- the
Q2D THOR_CAv3 exit snapshot rotated at the wave speed (T0), `q2d_inlet.py`: period 235.5 us (4246 Hz) and the
travel direction (toward decreasing theta) MEASURED on the Q2D wall probes (lags 47.0 / 94.5 us between probes
84.6 / 169.1 mm apart, expected 47.1 / 94.2), 181 samples per period (2 degrees), no radial variation (the Q2D has
none); the IC = the snapshot at t = 0 extruded along the channel, the exhaust at rest at 0.05 bar. Walls slip
(300), ambient 407 at 0.05 bar. Cases `CASE_3D/nozzle3d_S0`, `nozzle3d_V1` complete (mesh, bc, inlet410 1.6 GB,
ic 1.4 GB, ONERA-7 kit, input.ini: Euler, frozen, cfl 0.6, 3 periods, a field every quarter period). Smoke test
(MOSE_open, 10 ranks, 30 steps): the 410 data load and map on every rank, 3 238 200 cells, dt ramping to 7.7e-8 s
(~3000 steps per lap) -- then a SIGSEGV on 4 ranks at the run's end (the solution write with 10 ranks: to be
isolated; the wedge cases write cleanly on 3 ranks). NOT launched in production: the owner's call (GPU MOSE_GPU
has the 410 too, `IO_BC_Open.f90`). Mesh screenshots: figure `MESH/nozzle3d_*_mesh.png`, artifact
https://claude.ai/artifact/5GtezfynUut8BJ14d17oxw.
Geometric fact recorded: the THOR chamber's hub reaches its exit at -17.5 degrees (the boat-tail flare) while both
profiles start axial -- a 17-degree concave corner if the nozzle is attached to the chamber; the nozzle-only case
has no corner, but its Q2D inlet carries no radial inclination: a limit of the datum, equal for both contestants.

E. THE OWNER'S REDIRECTION (14:55): "cerchiamo il plug ottimo di stechmann e sqp invece dello shroud ... ottimo con
lo stato di stechmann (usando i metodi classici tipo rao ecc) vs ottimo di sqp con lo stato effettivo in output
dell'rde. Quindi non shrouded, semplice plug." The contest moves to SIMPLE PLUGS (external expansion from the
cowl lip at the inlet radius, the free jet at p_a, no shroud): A = the classical ideal plug for Stechmann's
time-mean state (Rao / Angelino: the [X-AFAN] inverse-march construction or GENO's plug member), truncated; B =
the SQP plug with the 12 phases voting (the [X-PSPL] free-form spike carrier, single-state today: the phase loop
of TWOP_MU to be ported), the same truncation, the base at a declared closure (N2 rows), separation by the class.
Tooling in place for it: the single-wall plug march with the axisymmetric lip fan, the PSPL walker, the two
referees (the plug-only mesh topology is a simplification of the nozzle-only one). Not started in this window.

## 3octies. The SIMPLE-PLUG contest (the owner, 2026-09-27 afternoon)
THE OWNER'S WORDS: "cerchiamo il plug ottimo di stechmann e sqp invece dello shroud. L'idea deve essere, ottimo con lo
stato di stechmann (usando i metodi classici tipo rao ecc ecc) vs ottimo di sqp con lo stato effettivo in output
dell'rde. Quindi non shrouded, semplice plug."

A. THE POSING (declared). The RDE annulus at x = 0 (r 53.85 -> 68 mm, the Q2D state, AXIAL: the chamber's, not a
design feature), the cowl ending AT the exit (the lip at (0, 68 mm)), the plug continuing the hub with slope 0,
the free jet at p_a 0.05 bar from the lip, the base an open wake p_b = p_a (Sule & Mueller 1973, the tournament's
convention), separation by Summerfield / Schmucker in the class, one length for both contestants.

B. THE CLASSICAL CONTESTANT, MEASURED. GENO's Rao plug (nozzle_type 8, RaoPlug_m: the single dof theta_E, the
variational C- curve from the lip, the mass-terminated tip) run at the Stechmann LIP state (M_i 1.556097, theta_i 0
at the lip point, y_E 68 mm, the Stechmann gas tables, p_a = p_b 5000 Pa, the mass target 0.49653 kg/s of the
annulus): RDE/handoff/f3_2026-09-27/geno_rao/. (1) The sweep over theta_E (sweep_th0): the C- curve closes on
the mass only for theta_E in [-17, -1] deg (M_E 1.58 -> 1.96; L 17.6 -> 35.8 mm; the curve goes non-finite before
the axis at larger turns, 97 percent of the mass at -18.6 deg): at an AXIAL lip Rao's family holds only SHORT
plugs, L <= 38 mm. (2) The member whose mass-set tip carries the implied base pressure p_a (Me_fixed 1.9526, the
fine scan): theta_E -13.03 deg, L 29.20 mm (0.429 y_E), eps 2.297, tip radius 37.7 mm, F 864.8 N -> C_F 1.3950
in the tournament's units (the shrouded pair cut at 87 mm 1.4461 at the same state, the bare exit 1.2916); the
corner's own ambient 7259 Pa (the member is Rao-optimal at 7.3 kPa, not 5 kPa; the p_a-adapted member M_E ~2.0
stops at the p_b corner with 9 percent of the mass unpassed). (3) NOT OUR INLET: at the lip plane GENO's plug
wall sits at y 51.9 mm with slope -32 deg and p 40.4 kPa (constant to x 8 mm) -- GENO's Phase 3 builds its own
internal canted throat (Rc_plug arc -> sonic) upstream of the lip; the flow reaching the lip plane is not the
uniform axial annulus of the RDE, so the member cannot be put in front of the referee on the RDE inlet plane.
The record: geno_rao/A_rao_lipstate_ref/summary.json (the reference curve, not a contestant). GENO's direct plug
(nozzle_type 10/11, the forward march from a uniform IVL) is WIP, disabled in main.f90.
THE CLASSICAL METHOD FOR A FIXED INLET is Humphreys, Thompson & Hoffman 1971 (parametric family + MOC, their
Table 2), which this line's TR-SQP RE-OBTAINS ([X-HMPH] S35, [DIR-REOB]); so the classical contestant is posed as
the VARIATIONAL OPTIMUM AT THE MEAN STATE on the same carrier -- the SQP on the Stechmann state -- with a
parametric classical family (cone / arc plugs at the mean state) as its cross-check. The owner informed 15:xx.

C. THE CARRIER FOR BOTH: the two-wall march as a SIMPLE-PLUG march. (1) The shroud reduced to a straight 2 mm
cowl at the inlet radius (TWOP_FIX = the shroud's knots, arc and end FROZEN -- a1_twowall.full/red, the reduced
design vector the driver sees; unset = bitwise), the lip jet from its end (TWOP_JET), the plug at the cap, its tip
height FREE (TWOP_FREE_EXIT=both: the base radius is a design outcome, priced at p_b = p_a by J_of's gauge term).
Probe 1 (twop_plugonly_probe.py, the Migdal plug cut at 87 mm under the jet, mean state): record 16.5 s, cert
0.057, m_lip +6.47 (the lip under-expanded: p_lip 7.5 p_a), J 1.3594; the 12-phase record 156 s, but the SEQUENTIAL
replay's 12-phase J + gradient 734 s: a walk of 16 x 6 segments would take days. (2) THE WAVEFRONT REPLAY EXTENDED
TO THE JET (a1_plug_march graph: 'fan' cells = the corner relation from the lip point, 'jet' cells = the free-edge
cell at max(q_pa, q_lip) with the lip point an input, graph['lip_out']; a1_wavefront_replay kinds fan / jet, the
lip_q returned for the lip margin; a1_twowall no longer forces the sequential path with the jet). Probe 2
(twop_wfjet_probe.py, WF-5): on the simple-plug posing (18120 cells, 496 levels: int 17794, wall 140, shroud 3,
lip 1, fan 16, jet 166) the wavefront J is BITWISE the sequential one, grad J to 3.9e-13 relative (tol 1.6e-11),
the class margin with the lip margin and its gradient bitwise; J + grad 55.6 s -> 1.7 s (33x), margin + grad
29.9 -> 1.9 s; the 12-phase J + grad 734 s -> 23.5 s, margin + grad 24.4 s. A 12-phase segment (record 152 s +
6-8 iterations) ~ 9 min: the walks are affordable.

D. THE CLASS ON THE PLUG POSING. Stage class run on the simple-plug posing at the mean state (cap 0.8,
_plug_contest/L87/class_run.log): the posing's reference -- Migdal's plug cut at the cap under the free jet, the
tip free -- is FOLDED (worst cell -0.5612 in shape mode, cert 7.6): the class stage's rules (floors = the
reference's own worst cell / 2^k) have no meaning on a folded reference (C-2 FAIL, rho negative). The fold class is
a GEOMETRIC criterion on the net (the sine of the angle between the characteristics), the same net (140, 31) and
knots: the plug contest uses the TOURNAMENT'S class record (stech/class_2026-09-27.json: floor 0.2351, rho 1233,
gap 0.0073, m_ref 0.470) -- as the capped tournament walks did, whose reference (the compressed Migdal) folds too.
The failed record kept as class_FAILED_2026-09-27.json.

E. THE REFEREE'S PLUG-ONLY TOPOLOGY (RDE/THOR/THOR_GPU/NOZZLE_2026-09-27, gen_nozzle_mesh.py --plug-only
--walls, build_bc_thor_nozzle.py): the 'shroud' of the walls JSON is the straight lip line r = 68 mm to the cap,
the Nozzle / Outer faces on it 101 CONNECTIONS (the free jet crosses it), the cowl lip AT the inlet plane (the
march's 2 mm cowl is not meshed: a straight wall in uniform flow), the Outer block's first cell 0.5 mm (25 nodes to
160 mm). Smoke on the placeholder P0 (the S0 plug under the jet), phase 0 frozen: 0.53 min, no shock, C_F 2.021
(the MOC's phase-0 value of the same plug under the jet 2.025: the referee reads the free jet). Batch scripts
generalised to a design list (DESIGNS / TAG / EVAL; post_batch --designs --eval).

F. THE STARTS AND THE WALKS (L87, launched 16:49). Starts under the mean state (twop_plugstart_probe): T (Migdal's
plug cut + the tail deflection) J 1.3653, cert 0.10, KS -0.276; C (arc + chord) 1.3534, 0.31, -0.565; L (nearly
straight) 1.3577, 0.04, -0.651 -- all out of class, all certified. THE CLASSICAL PARAMETRIC FAMILY at the mean
state (twop_plugfamily_probe_L87: arcs x_a/L 0.05-0.5 x tips 0.30-0.62 lip radii, 25 members): the best IN-CLASS
member J 1.34942 (x_a/L 0.1, tip 0.4865 = Migdal's, cone 14.1 deg), the best ignoring the class 1.35729 (folded);
the restored T start of walk A (1.36449, KS +0.48) already beats the family by 1.5e-2 -- as Humphreys' 20-run grid
(within 0.5 percent) is beaten by the variational contour. Walk A (mean state): restoration 2 iterations (KS
-0.276 -> +0.482), Newton metric 62 s (15 dofs), class scale h* 8.1e-3 -> tr0 2.0e-3; by segment 6 C_F 1.364679
with KS - mu0 +0.0066: THE CLASS BINDS from the third segment (the ascent trials 'INFEASIBLE'), the gain over the
restored start 1.9e-4. Walk B (the 12 phases) REFUSED its T start: cert 5.87 -- the certificate probe
(twop_plugcert_probe_L87) puts the uncertified cells in phase 10 (P0 3.09 bar, a 'jet' cell at column 91, cert 5.9)
and phase 6 (a wall cell, 1.12); T is out of class in 10 phases (min cell -0.74); the cone start C is CERTIFIED in
all 12 (worst 0.57) and out of class in 9; A's segment-5 landing is uncertified in phase 11 (a jet cell, 1.64). B
relaunched from C (17:2x): the restoration over 12 phases has 9 to lift. At L29 both T starts are certified and
in class from the outset (A: KS +0.588; B: cert 0.30, KS +0.531, C_F 1.2836 at the 12 phases): both walk.

G. LANDINGS (mean-state walks). A87: C_F 1.364679 (start 1.364493, the compressed-Migdal reference 1.361531), cert
0.10, KS +0.242 in class, 13 records, 1417 s; the tip 33.08 -> 33.10 mm, the tip pressure 1.17 p_a, the lip 7.47
p_a (under-expanded by 7.5: the free jet's first fan turns the whole 39 degrees at the lip). A29 (from T): 1.343042
(start 1.342782), KS +0.591, cert 0.054, 16 records, 1449 s -- BELOW the classical family's best in-class member
(1.345469: arc x_a/L 0.1, tip 46.2 mm, cone 15.4 deg): at 29 mm the SQP from Migdal's cut plug does not reach the
classical designer's best cone in 16 segments (its start is 2.7e-3 lower and the walk gains 2.6e-4). A2 (from the
family's best, TWOP_START=F): 1.345877 at segment 7 -- the SQP refines the classical member by +4.1e-4; its
landing is the mean-state contestant at 29 mm (the classical optimum IS its start: the honest form of the fixed-
inlet contest, Humphreys' own procedure being a parametric grid). The wavefront gate on the jet posing (stage
wavefront under the plug env, _plug_contest/L87/wavefront_jet_run.log): WF-1 3.1e-15, WF-2 9.4e-13, WF-3 bitwise,
WF-4 bitwise, 4/4 PASS in 217 s (16x / 5.6x under a load of 120; the first run crashed in WF-4, which replayed
without the jet posing: lip_jet passed).

H. THE JUDGES AND THE REFEREE ON A87 vs ITS START (eval_2026-09-27.json under TOUR_POSING=L87; the referee
CASE_2D/*87_phase*_plug, batch_plug87): MOC mean A 1.364679 / T 1.364493 (+1.9e-4); mean@fine 1.364533 / 1.364327
(A out of the fold class at the fine rung); 12 phases A 1.304317 / T 1.304155 (+1.6e-4; A 9 of 12 phases out of the
class, 1 uncertified 1.3; T 8 / 1 uncertified 3.0; the lip 2.75 .. 12.35 p_a across the phases); 12 phases @fine
1.304176 / 1.303997 (+1.8e-4; 12 of 12 out of class for both). THE REFEREE (2D axisymmetric Euler, frozen, 12
phases): T87 1.297148, A87 1.296474: A - T = -6.7e-4 (Schmucker +1.1e-4 / +0.8e-4, phases 7-8's last cells; no
shock in any phase) -- the mean-state refinement of the cut Migdal plug is NOT better under the phases by the
independent runner; the MOC's +1.6e-4 is read on nets that fold in 9 of 12 phases (section 3septies A's flaw, live
here). CFD / MOC: T -0.54 percent, A -0.60 percent (the shrouded pair: -0.28 .. -0.31 for both designs).
The simple plug against the shrouded pair at the same 87 mm, by the referee: 1.297 against 1.372 (-5.5 percent);
against no nozzle (J0 12 phases 1.2395 by the MOC): +0.058 against the pair's +0.133.
A2 LANDED (17:39): C_F 1.347554 at the mean state (start F 1.345469: +2.1e-3, 0.15 percent; A29 from Migdal's cut
1.343042), cert 0.72, KS +0.622 in class, 10 records, 1605 s; the tip 46.2 -> 45.7 mm, the tip pressure 3.04 p_a
(a 29 mm plug leaves the flow at 3 p_a: strongly under-expanded, the classical member's length is short for
0.05 bar -- Rao's own family said so). At 29 mm the SQP REFINES the classical designer's best cone by 0.15
percent; at 87 mm it refines Migdal's cut plug by 0.014 percent and the classical cone family sits 1.1 percent
below both. The mean-state contestant at 29 mm is A2 (F its start, both judged).

I. THE ALL-PHASE CLASS AT 87 mm IS NOT RESTORABLE IN THE TIME AVAILABLE. B87 from the cone C (certified in all 12
phases, out of class in 9: min cell -0.70): the restoration by ascent of the soft KS moves 1.4e-3 (one station) per
iteration for 4-7 records of 12 phases each and lifts the soft KS by 0.002 per iteration on a deficit of 1.4 (the
class KS -0.699 -> -0.7015: not moving) -- hundreds of iterations at ~10 min each. Read with the certificate probe
(T out of class in 10 phases, C in 9, A87 in 9): a simple plug at 87 mm under an axial supersonic inlet folds
SOMEWHERE in most phases -- the lip fan in axisymmetric flow converges its C- rays toward the axis and the plug's
re-turning reflects them into a same-family coalescence; the low-pressure phases fold the cone, the high-pressure
ones fold Migdal's cut plug. Whether the 12-phase shock-free class of a simple plug at this length is EMPTY or only
far from every start we own is not decided by this evening's walks (the class stage's rejector logic cannot say
either: its floors are Migdal's). DECISION (18:00): the phases' contestant at 87 mm is posed as Bm = the 12 phases
voting in J with the class at the MEAN state (TWOP_MU_CLASS=ref, the tournament's V1m posing), from the cone start;
B (the class in every phase) is left running for the record of its restoration and stopped when the Bm walk lands.
At 29 mm the T start is in class in all 12 phases from the outset and B29 walks with the all-phase class.
The fallback probe (twop_plugcert_probe_L87_fallback): A87's landing under the 12 phases -- cert 1.345 (a jet cell
at phase 10), out of class in 9 phases (min -0.734); the classical member F87 -- certified (0.495), out of class in 8
phases (min -0.679, phases 2-9). Every simple plug we own at 87 mm (T, C, A87, F87) folds in the phases with P0
below ~1.3 bar (2-8) and is in class only in the three post-wave phases (0, 10, 11) and, for some, phase 1: the fold
sits where the weaker fans of the low-pressure phases land on the plug (wall cells at columns 75-98 of 140, i.e.
x 47-61 mm) -- a fixed wall cannot un-fold the low-pressure phases without folding the high-pressure ones is the
conjecture the restoration's crawl supports; not proven here.
REFEREE AT 29 mm: the 2D wedges die at the first step at cfl 0.8 (NaN in the channel, all four designs; the 87 mm
wedges ran at 0.8): cfl 0.4 and 0.2 both run to 1 ms and give the SAME C_F on A29 phase 0 (1.986960 at either):
the 29 mm batch runs at cfl 0.4 (CFL passthrough in run_all_phases.sh), the two test cases deleted after the
reading.
B87 (the all-phase class) STOPPED at 18:00 after two restoration iterations (50 min, 11 twelve-phase records: soft
KS -1.3966 -> -1.3926, class KS -0.699 -> -0.702): its cost was slowing Bm87 and B29; its record is the log
_plug_contest/L87/B/run_walk_TN_2026-09-27.log (and the refused T start's).
(Tooling: the batch's "running" census counted a crashed wedge as running -- its run.log has neither "Time of
operation" nor "forrtl" -- and deadlocked at four crashed cases; the census now reads BAD TERMINATION / NaN /
KILLED as finished. The 29 mm batch relaunched at cfl 0.4 at 18:03.)

J. THE JUDGES AT 29 mm (eval under TOUR_POSING=L29; B29 still walking): mean A 1.343042 / T 1.342782 / A2 1.347554 /
F 1.345469; 12 phases A 1.283883 / T 1.283626 / A2 1.288677 / F 1.286992 -- every design IN CLASS in all 12 phases
and certified (the short plug keeps the class: its fan lands on a wall that has not yet re-turned). A2 - F: +2.1e-3
at the mean state, +1.7e-3 over the phases (0.13 percent): the SQP's refinement of the classical cone survives the
phases by the design-side judge. A2's profile (figure 33): the arc shrunk to a corner at the inlet (its wall
pressure drops from 5.7 to 3.5 p_a within the first station) then a straighter cone to a 45.7 mm tip; F keeps the
0.1 L arc.

K. THE REFEREE AT 29 mm (48 wedges at cfl 0.4, batch_plug29): no shock and no separation in any phase for any design;
mu-average CFD / MOC: T29 1.281935 / 1.283626, A29 1.282192 / 1.283883, F29 1.284781 / 1.286992, A2 1.287254 /
1.288677 (CFD 0.11-0.17 percent below the MOC, the offset common). A2 - F = +2.5e-3 by the REFEREE (+1.7e-3 by the
MOC over the phases, +2.1e-3 at the mean state): at 29 mm the SQP's refinement of the classical designer's best
cone SURVIVES the independent runner (+0.19 percent); A2 - T = +5.3e-3 (the Migdal-cut start was the wrong start
there). At 87 mm the same walk from Migdal's cut plug did not: -6.7e-4 by the referee.
Bm87 from the cone: the restoration at the MEAN state also crawls (3 iterations in 60 min: soft KS -0.863 ->
-0.822, class KS -0.556 -> -0.560, 12 records the last) -- stopped 19:02 and RESTARTED from the classical member
F87 (certified in all 12 phases, IN CLASS at the mean state, KS +0.435: no restoration): the phases' contestant at
87 mm walks from the classical designer's cone, as A2 does at 29 mm. B29 (the all-phase class, from T) at segment
3 of 16 (1.283656, +3e-5): ~15 min per segment, lands around 22:30; its checkpoint is the provisional design.

L. "THE PROFILES ALL LOOK CONICAL" (the owner, 19:15) -- MEASURED. Wall angles at 29 mm (x 0.5 / 1 / 2 / 4 / 8 /
15 / 22 / 28 mm): T and A -2 -4 -9 -17 -20.5 -21 -21 -19 deg (Migdal's cut: a turn over the first 4-8 mm, then
straight); F -3 -5 -10 -15.4 then -15.4 (the 0.1 L arc, then the cone); A2 -15.7 from the FIRST station (a corner
at the inlet) then straight. The SQP's own move at 29 mm was to sharpen the classical arc into a corner and keep the
straight wall. THE CURVED FAMILY (twop_plugcurved_probe: y = y_l - (y_l - y_tip)(x/L)^p, p 0.4 .. 1.3, the tip free,
a 0.02 L arc at the start; mean state): at 29 mm the CONE (p 1) is the best, in class, 1.346798 (tip 0.68); every
concave member (p < 1, the Rao-like fast turn) is worse AND folds (p 0.85: 1.346269 out of class; p 0.4: 1.3354);
convex p 1.3 in class but worse (1.3446); A2 1.347554 beats the whole family. At 87 mm the concave p 0.7 with the
tip at 0.40 (27 mm) reaches 1.364055 -- 6e-4 under A87 -- but OUT of class (KS -0.80), as is every member of the
family at 87 mm (the cone 1.3600, out); Migdal's cut plug (A87 1.364679, in class, gently curved -20 -> -4 deg) is
the best in class. READING: turn-then-straight is what the instruments prefer for a short plug (29 mm); at 87 mm
the class keeps the design at Migdal's curvature and the concave alternative folds. The landings are budget-limited
(16 segments; in A2 the trust-constr step returned a point WORSE than the base in 7 of 16 segments -- the
projected ascent carried the walk, 14 accepted steps of +2e-4 -- and the landing's |grad|inf 2.8e-2 is not small):
A3 = A2 continued for 16 more segments launched 19:20 to read where the shape goes with more budget.
A3 (A2 continued, 16 more segments budgeted): landed after 8 records at 1.347770 (+2.2e-4), the tip unchanged
(0.6717), cert 0.949 -- at the certificate's edge -- and the replay's gradient NON-FINITE at the landing (8
non-finite margin gradients, "no motion -> stop" at segment 13): the continuation adds 1.6e-4 per segment for two
segments and then runs into a numerically fragile record; the shape does not leave the corner-and-cone. The 29 mm
mean-state contestant of record stays A2 (cert 0.72); A3 is the continuation reading.

M. Bm87 FROM THE CONE F87 (19:03 -> the first segment 19:47): the 12-phase J at the start 1.293283, the Newton metric
757 s (three negative eigenvalues, floored), the class scale at the mean state h* 1.0e-3 -> tr0 2.5e-4 lip radii
(0.017 mm): the class binds from the first step along +grad J -- Bm87 will land within a fraction of a millimetre of
F87. Since the phases' walk cannot start from Migdal's cut plug (uncertified under the phases) while A87 does, A87
and Bm87 do not share a start; AF87 = the MEAN-STATE walk from the same cone F87 launched 19:50 so that the 87 mm
contest has a start-matched pair (AF87 vs Bm87) beside A87.
AF87 LANDED (20:09): 1.353615 at the mean state (from the cone F87 1.349423: +4.2e-3, 0.31 percent), in class (KS
+0.451), cert 0.078, |grad|inf 0.13 (budget-limited, non-finite margin gradients in the last segments), 16 records,
1171 s -- still 1.1e-2 below A87 (Migdal's cut start): at 87 mm the cone's basin is the poorer one, and the walk
does not cross to Migdal's shape in 16 segments; the start-matched pair at 87 mm is AF87 vs Bm87.

N. B29 LANDED (21:07): the phases voting with the class in EVERY phase, from T (Migdal's cut): 12-phase C_F 1.283752
(start 1.283626: +1.3e-4), in class in all 12 phases (KS +0.533), cert 0.50, 16 records, 15001 s (4.2 h under the
evening's load). Against A2 (the mean-state walk from the cone, 1.288677 over the phases): -4.9e-3 -- the START
decides more than the vote at 29 mm (B29 shares its start with A29, 1.283883 over the phases, and sits 1.3e-4 BELOW it:
the vote bought nothing there either). BF29 = the phases' walk from the cone F launched
21:10 (start-matched with A2). The L29 judges and referee re-run with B29 and the concave member Cc29 (chain
started 21:07).

O. THE 29 mm TABLE WITH B29 AND THE CONCAVE MEMBER (22:34; chain of 21:07; batch_plug29_table.json, eval under
TOUR_POSING=L29): 12-phase MOC / referee CFD -- T 1.283626 / 1.281935; A 1.283883 / 1.282192; B (the phases' walk
from T, all-phase class) 1.283752 / 1.282058; F (the classical cone) 1.286992 / 1.284781; A2 (the mean-state walk
from F) 1.288677 / 1.287254; Cc (the concave power-law member p 0.85, the same tip 0.68, FOLDED by the march's class
in all 12 phases, one phase uncertified 3.6) 1.287795 / 1.286951. READINGS: (1) the vote buys +1.2e-4 over its
start T by the referee (+1.3e-4 MOC): nothing, as at 87 mm and in the shrouded tournament; (2) the START decides:
the cone family's best F beats every walk from Migdal's cut by 2.6e-3 (CFD); (3) THE OWNER'S POINT ("come fa il
cono a essere migliore"): by the independent runner the CONCAVE wall Cc BEATS the cone F by +2.2e-3 (+0.17
percent) -- the march's class had discarded it (folded nets), the MOC on those nets gave it +0.8e-3 over F; the
SQP's corner-and-cone A2 still edges the concave by +3.0e-4 (CFD) / +8.8e-4 (MOC). So: a concave wall is NOT worse
than the cone by the referee -- it is worse than the corner-and-cone the SQP found, by 0.02 percent, and it is out
of the shock-free class; the class is what the vote and the walk buy, the thrust differences are 1e-4 .. 1e-3.
The referee's wall record of Cc29: NO pressure rise above 5 percent on the plug in any phase (the largest 2.5
percent at phase 8, x 4 mm from the inlet, where the concave wall turns back); the fold the march's class flags is
a compression the Euler wedge resolves as a 2.5 percent rise, not a shock of consequence: the class is conservative
here, a reading to carry into the class revision (twowall:shape-margin-blind-to-convergence's sibling: the margin
flags a coalescence whose strength is not measured).

P. THE 87 mm TABLE, COMPLETE (00:00, 2026-09-28; eval under TOUR_POSING=L87, batch_plug87_table.json; CFD none /
Summerfield / Schmucker, then the 12-phase MOC): T87 1.297148 / 1.297148 / 1.297257 | 1.304155; A87 1.296474 /
1.296474 / 1.296554 | 1.304317; F87 (the classical cone, tip 33.1 mm) 1.283042 / 1.285974 / 1.286644 | 1.293283
(5 phases detached per the MOC); AF87 (mean-state walk from F) 1.286903 / 1.288322 / 1.288902 | 1.295939; Bm87
(the phases in J, the class at the mean state, from F; landed 1.294249 from 1.293283, +9.7e-4, cert 0.54, KS +0.458)
1.284235 / 1.286574 / 1.287487 | 1.294249 (6 detached); Cc87 (the CONCAVE power-law member p 0.7, tip 27.2 mm,
folded by the class in 12 of 12 phases) 1.299544 / 1.299888 / 1.300720 | 1.303411. VERDICT OF THE REFEREE AT 87 mm:
the concave wall is the BEST design of the evening, +2.4e-3 (none) .. +3.5e-3 (Schmucker) over T87 and +3.1e-3 ..
+4.2e-3 over A87 (0.2-0.3 percent) -- the MOC on its folded nets had it 7e-4 BELOW T87 and the class had excluded it
from every walk. The cone family (F, AF, Bm) is 1.0-1.4e-2 below Migdal's cut plug by the referee: at 87 mm the
start decides by an order of magnitude more than either method's walk (A87 - T87 -6.7e-4, Bm87 - F87 +1.2e-3, AF87 -
F87 +3.9e-3 at the referee). The Summerfield / Schmucker credits are 1-3e-3 on the cone-based designs (their tails
separate in the low-pressure phases: p_wall < 0.35 p_a) and 0 .. 1e-3 on Migdal's cut and the concave.
THE REFEREE'S WALL RECORD AT 87 mm (rises above 5 percent between neighbouring cells, all 12 phases): T87 0, A87 0,
F87 0, Bm87 0 -- Cc87 36 (three per phase, the largest 15.7 percent), AF87 30 (the largest 8.6 percent). The
concave winner DOES carry the recompressions the class flagged -- weak shocks on the wall, 5-16 percent jumps,
where the wall turns back toward the axis -- and wins by +0.2-0.3 percent despite them: at 87 mm the shock-free
class is not the thrust-optimal class for a simple plug on this inlet, by the independent runner. AF87 (the
mean-state walk from the cone, in class at the mean state, out of class in 9 of 12 phases) carries them too; the
walks from Migdal's cut plug (T, A) and the cone-based F / Bm do not. The over-expanded tails: Bm87 and F87 reach
0.15-0.30 p_a in the low-pressure phases (Summerfield credits 2-3e-3), Cc87 0.28 p_a at phase 8 (Summerfield at
phases 7-8), T87 / A87 0.37 (none).

Q. CORRECTION (03:10, 2026-09-28) TO SECTIONS I AND M: it was NOT the fold class that pinned the phases' walk at 87 mm.
Fasi-da-cono 87's start ladder (its log): KS +0.4352 at every rung -- the class never broke -- and the ladder went
OUT at h 1.4e-3 on the CERTIFICATE (1.59), after rungs at 0.87 / 0.49 / 0.84 / 0.99: the 12-phase record's worst
cell (a free-edge 'jet' cell of a high-P0 phase) sits at the certification limit and crosses it under a 0.1 mm
move, so the class scale read 1.0e-3 and the trust radius 0.017 mm. The direct probe (twop_classbreak_L87: the cone
pushed 0.03-0.27 mm along +grad of the phases and of the mean, the cell census at the mean state) confirms it: 0
cells below the floor at every step, KS +0.435 unchanged. Stechmann-da-cono 87's ladder went to 4.6e-2 (32x
further) and broke on the class (KS -0.52 at 3.1 mm). SECOND MECHANISM: the phases' Newton metric at the cone --
the secant Hessian of the 12-phase gradient -- came out with an asymmetry of 18.5 (the mean's 0.05), three
negative eigenvalues, floored at 74: a Newton step 100x smaller than the mean's (|D| 2.3e-3 against 0.19). Both
are the same defect: the jet cells of the strongest fans certify marginally (plug-march:jet-cell-uncertified-
strong-fan), their gradients are noisy, and the 12-phase machinery inherits it. WHAT THE TWO METHODS ASK FOR
(twop_newton_shapes: the Newton step of each functional at the cone in the MEAN's metric): at 87 mm both ask
for a concave-then-flat wall -- the mean -3.7 mm at mid-plug (x 36 mm), the arc shrunk to a corner, the tip
RAISED by 6.2 mm; the phases the same pattern at 60-70 percent amplitude and the tip raised 1.5 mm (their five
low-pressure phases, P0 0.46-0.77 bar, pull ORTHOGONALLY to the mean with 3-4x the gradient: cos -0.2 .. +0.06,
|g| 0.8 against 0.2-0.3; the seven others align, cos 0.8-1.0). At 29 mm both ask for less than 0.4 mm (the arc to
a corner, the tail 0.1 mm lower): the corner-and-cone is near-optimal for both there; the disagreement (cos 0.93)
sits in the two highest-P0 phases. WHAT CHANGED against the shrouded and Humphreys walks, which bent within the
class: there the states were one (or the shroud / the canted throat kept every state's net regular and the
certificates at 0.01-0.1); here a single wall under a free jet from an axial lip carries, in the strongest
phases, edge cells at the certificate's limit -- the instrument, not the class, is what pinned the phases.
THE AMBIENT AT 0.3 AND 1 bar BY THE MARCH: not posable -- the jet's speed at p_a has no root above the sonic
speed when a phase's inlet static pressure is below ~p_a x 1.9 (phase 8 at 0.3 bar: p_in 0.12 bar); the design
method has no answer there, only the referee.

R. THE JET CELL'S CERTIFICATE, FOUND AND FIXED (03:30-04:00). twop_jetcell_probe on the cone under the 12 phases: the
worst 'jet' cells (stations 43-52, columns 75-84, chords 0.015 lip radii, theta 5-8 deg, the edge speed = q_pa
exactly) have |R| 1e-14 on the position rows and 1e-6 on the compatibility row (units ~u^3: roundoff), cond(J)
0.7-1.5e10, and a Newton step at the recorded root of 0.7-2.5e-14 against a bound of 3.6-5.3e-14: certificates
0.18-0.60. ONE more Newton iteration from the recorded root drops the step to 1e-16 (certificate 0.002): the root
is right, the record stops one iteration short. MECHANISM: the damped Newton picks its iterate by the residual
NORM among trial steps {1, 1/2, ..., 0}; at the end that norm is the big row's roundoff and the argmin no longer
sees the small rows, so the full step loses to a damped or zero one exactly when it would reach the floor. FIX
(a1_ideal_march_jax.make_implicit_solver polish=True, opted in by the free-edge solver alone -- a1_plug_march
JET_POLISH, PLUG_JET_POLISH=0 restores the record's solver bitwise; the key carries the flag): once the undamped
step is inside the certification bound, take it in full. GATES (this section's rows to follow): the plug march's
exact planar oracle P-1..P-4 + R-1/R-2; the 12-phase certificates of the cone and of Stechmann-from-Migdal 87
(the jet cells at the floor, J per phase unchanged to 1e-12); the wavefront stage WF-1..4 on the jet posing; the
tournament's gates (T-0..T-7 default path bitwise) and jetgates JT-1..4.
Gate 1 of the polish: the plug march's exact planar oracle (a1_plug_march.py, the corner-fan simple wave twin with
the free edge; the fj solver polished): all cells certified, P-1 the edge angle within the Richardson band, P-2
the wall pressure, P-3 mass, P-4 momentum in the p_a gauge, R-1 the corrupted ambient rejected -- 6/6 PASS, 41 s.
Gate 2: the wavefront stage on the jet posing with the polished solver -- WF-1 3.1e-15, WF-2 9.4e-13, WF-3 and
WF-4 bitwise, 4/4 PASS (142 s; the sequential and the wavefront replays share the polished solver).
Gate 3: the 12-phase records of the cone and of Stechmann-from-Migdal 87 with the polished solver: J per phase
UNCHANGED to the last digit (max |dJ| 0.0 on both), the cone's worst certificate 0.495 -> 0.153 (its jet cell 0.046)
-- but Stechmann-from-Migdal 87's phase-10 jet cell 1.345 -> 1.831: for THAT cell the full step does not reach a
floor under the bound (probed next). Gate 4: the tournament's gates T-0..T-7 9/9 (T-1 the default posing bitwise with
the S41 record 1.579660988049, T-3/T-4 bitwise) and the jet gates JT-1..4 5/5 with the same numbers as 2026-09-27
(JT-3 replay = record 1.439698070323, adjoint -2.473706e-04): the polish changes no recorded number. The walks
Stechmann-from-cone 87 (polished) and Phases-from-cone 87 (polished), 32 segments each, launched 04:25 (AF2, Bm2).

S. THE POLISH WINDOW (11:00-11:40). The cell of Stechmann-from-Migdal 87 at phase 10 that stayed at 1.83 with the
first polish (twop_jetcell_probe on that record: station 104, column 136, chord 0.016, theta 1.5 deg, cond(J)
1.6e10; the step at the recorded root 1.6e-13 against a bound of 8.1e-14, one more full step 8.8e-17): with the
full step allowed only INSIDE the bound, the damped argmin kept halving from 1e-12 down and the Newton hit its cap
(N_NEWTON 30) one iteration short. POLISH_WINDOW = 1e4 (a1_ideal_march_jax: the full step is taken within 1e4 x
the bound, i.e. a relative step below ~1e-10 -- the quadratic regime of a well-posed cell; a wrong branch never
enters the window, the corrupted-ambient rejector guards it). GATES with the window: the plug march's exact planar
oracle 6/6 (31 s); Stechmann-from-Migdal 87 under the 12 phases: worst certificate 1.345 -> 0.417 (a wall cell
now), J per phase unchanged to the last digit; the wavefront stage WF-1..4 4/4 (120 s); the tournament's gates
9/9 (T-1 bitwise with the S41 record) and jet gates 5/5 (JT-3 the same replay and adjoint as 2026-09-27).
Stechmann-da-cono 87 with the first polish and 32 segments (AF2) LANDED 11:38: 1.354147 (16 segments: 1.353615;
the start 1.349423), cert 0.042, KS +0.462, |grad|inf 0.155 -- +5e-4 for 16 more segments, still not stationary.
Fasi-da-cono 87 (Bm2, 32 segments) continues with the first polish from the cone (its cells at the floor).

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
- Follow-up commit (night): the size-floor finding (section 3quater), the retraction of the
  "shock-free boundary" reading everywhere it was written (3bis item 2, M0 addendum item 3, X-TWOP,
  twowall:design-posing-open, D6 note, PROGRESS block + archive, handoff), the far-start row re-read,
  the advisory's 6.4 corrected (the cap is not active over-expanded), the free walk's stopped log.
- Class-correction commit (2026-09-27 early): `a1_plug_march.margin_of_corners` gains the shape mode
  (eps2 guard) and the plume cut (x_max), both opt-in, the mode of record bitwise (C-F, and the step-2
  start reproduced bitwise after the edit); `a1_twowall.py` gains TWOP_SHAPE / TWOP_NOPLUME, the C-S
  gates, the class-record fields shape/noplume and their check, TWOP_START=F (a walk from a record's
  landing); `twowall_cases.json` the margin block. Class records `_twowall_arc_shape/class_2026-09-26
  .json` (8/8), `_twowall_arc_shape_fine/class_2026-09-27.json`; the shape-only intermediates kept as
  `*_shapeonly_*`. Registry: X-TWOP statement + pass 2026-09-27; findings as listed in 3quinquies.
- RDE-procedure commit (2026-09-27 night, section 3sexies): NEW carriers `a1_lipjet.py` [X-LJET] (+
  `lipjet_cases.json`) and `a1_rde_tournament.py` [X-RDET] (+ `rde_tournament_cases.json`: units, source,
  gates, eval, offdesign, swirl_gates, jet_gates), both new-file clean under the numeric lint (the bar
  conversion a declared SPEC constant, the family check's band derived). `a1_plug_march.py`: pm_turn,
  plug_march(lip_jet=...), the five-cell swirl seam of the shroud posing, the margin's shape/plume modes
  unchanged (the default path bitwise). `a1_swirl_march.py`: the two swirl wall cells, swirl_cells_2w.
  `a1_wavefront_replay.py`: the gas tables an argument of every step; rows_block (WF-4 bitwise).
  `a1_twowall.py`: tab_gconst, TWOP_GAS / MU (+ CLASS) / SWIRL / JET / SEP (+ CLASS) / U0_S, the
  separation closure on the running minimum, the mapping-cap guard at every record, stage wavefront's
  WF-4; `twowall_cases.json` blocks separation, jet, wavefront.rows_block. Registry: claims X-LJET and
  X-RDET minted, X-TWOP's statement extended; findings wavefront:gas-table-closure,
  twowall:walk-mapping-cap-multiphase, twowall:sep-closure-cumprod-bias, rdet:jet-gate-harness-env
  (minted and discharged) and twowall:shape-margin-blind-to-convergence (minted, CONFIRMED, the owner's);
  engine-core:F3-table-clamp-silent re-read (its second live instance, the tournament's rejector T-7).
  Records `_rde_tournament/` (gas and family files, the class record, S1's walk, the gate / eval /
  off-design logs and JSONs, the aborted walks' logs in their subfolders), `_lipjet/run_2026-09-27.log`,
  `_twowall/wavefront_K140_N31_2026-09-27.json`; the Q2D extract `.npz` (500 kB) and figure 30
  untracked. The V1 landing and its judgement follow in a follow-up commit.
- Follow-up commit (2026-09-27 morning): the tournament JUDGED (section 3sexies D2, provisional at V1's segment 8:
  the seven judges in parallel, `TOUR_JUDGE` + stage evalmerge; the fine-rung judges `@fine`; the per-phase lip
  pressure, separation margin and coldest state in stage eval; the design loader reading a running walk's
  checkpoint); corrections written where the first commit had them: V1m's "no step" (a checkpoint misreading),
  "1-4 cells each" (phases 0-9 only), the swirl walk's cause (the sequential replay's unpadded margin stack, fixed in
  `a1_twowall._replay_out`, gate SW-5); SW-4 on the central-difference ladder; the Q2D figure 30 regenerated
  (untracked). V1's landing replaces the provisional table in the next commit.
- Landing commit (2026-09-27 morning): V1 and V1m landed (records `_rde_tournament/V1/walk_TN_2026-09-27.json`,
  `_rde_tournament/V1m/walk_TN_2026-09-27.json` with their logs); the final chain (seven judges + off design in
  parallel, merge, figure 30) re-run on the records; D2's table and reading replace the provisional ones everywhere
  they were written (X-RDET, M0 item (5), advisory section 7, PROGRESS block + archive, handoff section 14). The
  per-judge JSONs, the provisional chain log and the walks' Hessian scratch folders removed (reproducible).
- Referee commit (2026-09-27 afternoon, section 3septies): records only in this repo (log, advisory 7.1, X-RDET
  statement); the carriers, meshes, cases and results live in `RDE/THOR/THOR_GPU/NOZZLE_2026-09-27/` (README.md
  there) and the probes in `RDE/handoff/f3_2026-09-25/` (twop_ends_probe, twop_shroud_cut_probe). The shrouded
  contest is closed by the referee at "indistinguishable"; the plug contest opens next.
