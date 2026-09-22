# S33 — The wall angle as the independent variable (2026-09-22 evening, [F3/A1], brick-2 plug line)

Entry point of the line: `RDE/handoff/NOZZLE_HANDOFF_2026-09-22.md`
(S32 closure, HEAD c3ec26f, 38 commits ahead of the remote, not
pushed). This log records the session that opened the handoff queue's
item 1 -- the parametrisation in ANGLE proposed in S32 section 20 after
the owner's reading of figure 02 ("the out-of-class events may be caused
by the optimiser's profile coming out WAVY") -- on the owner's word
"riprendi l'handoff". Criterion in force: [DIR-REOB] (an optimum is
certified only when re-obtained from elsewhere, in contour and value).

## 1. The brick: `PSPL_PARAM` in the driver (additive, bit-identical by default)

`validation/a1_plug_spline_opt.py` gains the COORDINATES of the design
vector as a knob read at import, like every PSPL_* constant:

- `y` (unset; every row of record): the spline radii at the frozen
  knots, unchanged;
- `angle`: W = the INCREMENTS of the wall angle from knot to knot, the
  first from the flow angle at the cut (theta_0 = the record's clamped
  slope: a wall is a streamline), theta_k = theta_0 + W_1 + ... + W_k;
  the SLOPE tan(theta) is linear between knots, so on every interval the
  angle is monotone (arctan of a linear function) and the contour is the
  slope's EXACT integral -- piecewise quadratic, C^1, the curvature
  jumping at the knots while the direction, which is what the
  characteristics see, stays continuous. The bounds W >= 0
  (`design_bounds`, scipy `Bounds(keep_feasible=True)`) ORDER the angle:
  a wall whose angle turns is not representable;
- `angle_free`: the same coordinates without the bounds -- the A/B that
  tells whether the order carries the result.

Helpers: `angle_W0` (the incumbent streamline in angle coordinates: its
own direction at the knots), `angle_wall` (design -> y, slope at any
concrete abscissae; the anchor (X0, y_w0, slope0) movable by `c["x0"]`
for a contour read from another start point), `design_bounds`,
`knot_radii` (the space in which designs of either coordinates are
compared: W itself in y, the integrated contour in angle).
`build_case` returns W0 in the active coordinates; `wall_stations`
branches before the y path, whose operations are untouched.

**Bit-identity of the default, measured**: stage class re-run with the
new code (the census closure factored into the module-level `_census`,
same operations): 10/10, 162.8 s, and `class_opt_veen.json` BYTE-
IDENTICAL (`cmp`) to the record written at 18:02 before any edit.

**The bounds in trust-constr, measured on a toy** (the driver's cadence:
8 iterations per segment, restarted each segment, optimum on the bound
for two of four coordinates): the interior-point iterates reach
1.9e-5 / 6.3e-5 of the bound in five segments and then stop moving --
in the driver that reads as "no motion at the radius floor -> converged".
1e-5 rad of wall angle is 6e-4 deg: a bound that is active in the
answer is met to far below anything the march resolves.

`validation/a1_humphreys_twin.py` follows: `opt()` passes
`bounds=P.design_bounds(c)` (None in y: the same call as before),
compares knots through `knot_radii`, prints the landing's wall-angle
range and turns in angle coordinates, and files the landing as
`opt_<case>_fan_<base>_<param>.json` with `W_rad` and `yk_in` (never a
`W_in` that a y-coordinate reader would march as a spline); the table
start and the knot perturbation are refused in angle coordinates (they
are y tests; RE-2 in angle coordinates needs its own perturbation, not
posed yet). `read_table` takes an explicit `mode`; the Hermite of their
rows is factored into `_hermite`, which also returns the contour's
DIRECTION as drawn; `n_turns` counts turns with exact zeros (a straight
piece, which an active bound produces) skipped -- K-10's count on every
design without one.

## 2. Stage angle (HMPH_STAGE=angle PSPL_PARAM=angle): A-1..A-5, 7/7 before the legs (96 s); run of record with the legs' census 10/11 (168.9 s, section 4)

| gate | reading |
|---|---|
| A-1a their contour T..D, read as drawn (the Hermite through their x, y and printed angle, 12 rows) | -48.25..-13.26 deg, **0 turns** |
| A-1b ORDERED ANGLE basis from THEIR T, m 6 / 12 / 24 | max dy 0.0299 / 0.0272 / 0.0030 in, max dtheta 1.44 / 1.43 / 0.31 deg, 0 turns at every rung |
| A-1c the Y basis from THEIR T (clamped at their slope), m 6 / 12 / 24 | max dy 0.0269 / 0.0027 / 0.0021 in, max dtheta 1.44 / 0.45 / 0.31 deg, **0 turns at every rung** |
| A-2 the inlet: flow angle at our cut vs their wall there (x 0.378 in) | **-26.65 deg vs -43.47 deg**; the lowest ordered wall (straight at theta_0) sits 0.729 / 0.759 / 0.598 / 0.318 / -0.045 / -0.487 in above their contour at the six knots |
| A-3 the incumbent in angle coordinates, representation ladder m 6 / 12 / 24 / 48 | 0.0658 / 0.0165 / 0.0041 / 0.0010 in (second order); march cert 0.034, 782 resolved cells, **0 folded, 0 turns**, J 30,087.7 lbf (the y incumbent 29,946.2) |
| A-4 AD vs the FD ladder, W_0 / W_3 / W_5 and the directional identity | differences 8e-5 / 5e-6 / 2e-4 / 3e-4 against bands 0.67 / 0.78 / 0.77 / 0.70 |
| A-5 ORDER => NO TURN on the march's stations | 12/12 random ordered designs turn-free; one increment reversed: 2 turns (the counter sees it); **y designs inside the stay class (+-0.15 in per knot): 11 of 12 turn, 1-5 times** |

READ.

1. **A-5 is why the coordinates matter to a WALKER.** Inside the class
   within which the S31/S32 walks were said to "stay", the y basis turns
   in eleven random draws out of twelve: a walk in y coordinates can
   trade a wiggle for a little thrust at every step, and K-10 measured
   that every turn folds the net. In ordered angle coordinates the same
   neighbourhood has no wavy member at all.
2. **A-3: the incumbent is represented, in class, at second order.** The
   angle basis loses more than the y spline at m 6 (0.066 in at the tip,
   the error accumulating downstream by integration, against the
   spline's 0.005 pinned at the knots), and falls by 4x per doubling; J
   at the represented incumbent is +141 lbf above the y-represented one
   -- the representation, not the physics (the walks move J by ~3000).

## 3. CORRECTION to S32 section 20 and to the X-HMPH clause "the PRIMARY defect is the parametrisation"

S32 section 20 read K-10 as: "the out-of-class problem is not primarily
the driver's missing constraint but the PARAMETRISATION: a spline in y
with a pinned start can only approach their contour by wiggling in
angle", and the registry row carries "The PRIMARY defect is therefore
the parametrisation". Stage angle separates the two things that
sentence joined -- the BASIS and the PINNED START -- and they do not
carry the same weight:

- **A-1c: from THEIR OWN start T the y basis holds their contour without
  a turn at every rung** (m 6: 0.027 in, 1.44 deg -- as good as the
  angle basis, 0.030 in, 1.44 deg). A six-knot spline in y is not wavy
  on their contour; it wiggles only when pinned where they are not.
- **A-2: from OUR cut NO non-turning wall reaches their contour.** The
  planar fan hands the wall a flow angle of -26.65 deg at the cut where
  their wall runs at -43.47 (the plug-side expansion over their
  prescribed arc, which the planar corner fan does not contain), at a
  radius 0.33 in above theirs (K-7); every ordered wall lies above the
  straight wall at theta_0, which passes 0.73 in above their contour at
  the first knot. Reaching their contour from our cut takes a
  steepening turn -- in ANY coordinates.

So the PRIMARY defect is the INLET (K-7's own reading: "the cause is the
posing's own start radius, not the paper's contour"), and the
parametrisation is what decides what a walk DOES about it: in y
coordinates it approaches their contour with a turn and folds (K-10);
in ordered angle coordinates the turn does not exist and the walk must
find the best monotone wall this inlet admits. Consequences for the
certification criterion: RE-1 against Table 2 is impossible in this
posing with a non-turning wall -- it needs their inlet (route (ii), the
kernel / the numerical transonic line, queue item 4); RE-2 and RE-3 --
the certificates of a real problem -- are posable in angle coordinates
now. The two cures of section 20 keep their roles, re-weighted: the
ordered angle is the representation half of the class constraint (a
wavy design cannot be proposed), the margin its march half (a design
that folds by other means is rejected) -- and "by other means" is not
hypothetical: a monotone wall that turns toward the flow faster than
the incident expansion is cancelled is a net compression, and a
compression coalesces (section 4).

## 4. The legs: the fan-start walk in angle coordinates, ordered and free (A-6, A-7)

The S32 leg's posing exactly (HMPH_CASE=opt HMPH_START=fan
PSPL_ITERS=30 PSPL_BACKTRACK=3, 30 x 8, base veen, (81,41), 6 knots),
PSPL_PARAM=angle and =angle_free, launched in parallel on s2 at 20:07
(`_humphreys_twin/run_opt_opt_fan_angle{,_free}_2026-09-22.log`,
landings `opt_opt_fan_veen_angle{,_free}.json`); both open from the
represented streamline, J 30,088 lbf, and are identical at segment 0
(J 3.63926605e+06, |grad| 2.457e+06).

| | S32 walk in y (backtrack 3) | ORDERED angle | FREE angle |
|---|---|---|---|
| records / probes (accepted) | 19 / 14 (11) | 26 / 38 (4) | 20 / 20 (10) |
| wall time | 1678 s | 2191.5 s | 1471.9 s |
| thrust (their 32,881) | 32,820 lbf | **33,308 lbf (+1.30 %)** | **33,353 lbf (+1.44 %)** |
| cert / y_D | 0.198 / 2.72 in | 0.202 / 3.739 in | 0.105 / 3.543 in |
| wall angle / turns | 5 turns | -26.65..+37.89 deg, **0 turns** | -32.56..+37.45 deg, 1 turn |
| increments (deg) | -- | 0.0008, 5.31, 6.38, 4.57, 8.01, **40.27** | -6.12, 17.18, 0.20, 3.51, 7.51, **41.81** |
| FOLDED resolved cells (A-6) | not censused | **635 of 2051 (30.96 %)** | 1022 of 2760 (37.03 %) |

The ordered walk parks at 4.0288e6 from segment 11 on: every later
trial is uncertified (worst 6.6e12..8.9e16), the backtracking finds no
certified point along any of them, the radius shrinks to 5.9e-3.

THE ANATOMY (A-7, J = F_in + wall push + base term, each on the
design's own replay; A-7a: the three re-add to the replayed J exactly,
0.0 against a band of 1.4e-13):

| design | J | F_in | push | base | p_D / p_a | M_D | p_b / p_a (Veen) | first fold |
|---|---|---|---|---|---|---|---|---|
| their Table 2 (y, same grid) | 32,765.1 | 29,290.6 | 3,495.8 | -21.4 | 1.968 | 2.474 | 0.513 | x 1.88 in (3 turns) |
| ORDERED landing | 33,308.5 | 29,290.6 | 2,552.6 | **+1,465.2** | **7.578** | 1.679 | **3.269** | **x 9.66 in**, last interval |
| FREE landing | 33,353.4 | 29,290.6 | 2,642.5 | +1,420.2 | 7.854 | 1.656 | 3.449 | x 2.43 in (the early dip) |

READ.

1. **The ordered coordinates did what they were built for -- no turn --
   and the walk still left the class.** 30.96 percent of the resolved
   cells fold, every folded column in the last knot interval (A-7c: the
   first at x 9.66 in, the interval starting at 9.60), where the wall
   turns +40.3 deg. K-10's own falsifier FIRES: "a design with no turn
   that folded ... would send the mechanism elsewhere". The mechanism is
   COMPRESSION -- a wall turning toward the flow faster than the
   incident expansion is cancelled; a turn in the wall angle is one way
   to produce a compression half (K-10's pool), a monotone up-turn is
   another. K-10 stands as measured on its pool (turns => folds); its
   reading as THE mechanism is withdrawn.
2. **The lever the walks found belongs to the FUNCTIONAL, not to the
   representation.** The ordered landing's +543.4 lbf over their contour
   on the same grid is +1,486.6 lbf of BASE against -943.2 of wall push
   (A-7b): an up-turn of 40 deg in the last 1.84 in compresses the wall
   flow from 2.1 to 7.6 p_a at D (M 1.68), and the Veen closure, read on
   that wall state (0.846 p / M^1.3), returns a base pressure of 3.27
   p_a on a base of radius 3.74 in. A base pressure three times ambient
   is outside what the closure was fitted on and what the base data of
   the line show (closed-wake P_b/P_at 0.5-1.1 for Sule & Mueller, S30;
   p_b/p_lip 0.51 +- 0.075 on Chutkey's ten points, S31), and the state
   it is read from is a FOLDED march: in a real flow that compression is
   a shock, and ahead of a base a separation. The free walk finds the
   same lever (last increment 41.8 deg, p_b 3.45 p_a) and adds an early
   dip (-6.1 deg, folding from x 2.43 in): two coordinate systems, one
   answer -- the tail compression priced by the base closure.
3. **So the S32 "32,820" (5 turns, not censused) and tonight's 33,308
   and 33,353 are no gains: out of class by the S29 precedent**
   ([X-PGRS]: "the number is taken from a folded march and is NOT a
   gain"). The value of the best IN-CLASS design of this posing is not
   known tonight.
4. **What it makes of the queue.** The class constraint (queue item 2,
   and the first prerequisite of [DIR-REOB]) is no longer one of two
   cures: it is the only thing standing between the walker and this
   lever, in any coordinates. And once it is active the walk will
   compress the tail up to the fold threshold -- the Veen base still
   pays for p_D -- so the in-class optimum is expected ON the margin at
   the tail (M0's margin-active expectation for the plug sector, now
   with a named lever), and the base closure's domain becomes the next
   question the functional must answer (the owner's open decision 5 --
   adopting `chutkey` -- and a guard on reading a closure off a state it
   was not fitted for).

## 5. The certification line after tonight [DIR-REOB]

- RE-1 against Table 2 is impossible in this posing with a non-turning
  wall (A-2: 0.73 in at the first knot): it needs their inlet (route
  (ii), queue item 4), not a basis.
- RE-2 / RE-3 are posable in angle coordinates (the perturbation of an
  angle-coordinate design is to be posed: HMPH_PERTURB is a y test and
  is refused there), but only on IN-CLASS landings: none exists yet.
- No row of the line certifies the optimiser as a finder (unchanged).

## 6. The queue, re-ordered by tonight's numbers

1. **The class constraint on Humphreys' posing** (item 2 of the S32
   handoff): derive the margin's constants for this world ([X-PMRG]'s
   stages D0-D4 -- orient, f_edge at the doubled resolution, m_ref and
   the floors from the incumbent, rho, AD vs FD, the folded designs of
   this row as the rejector: their Table 2 through our cut, the y and
   angle landings; the fold scale h* along +grad J in ANGLE coordinates
   -> tr0), then the fan-start walk with `margin=` in ordered angle
   coordinates: the first in-class landing of the row, and whether it
   is margin-active at the tail.
2. **The base closure's domain** (owner's decision 5 and a guard): at
   the in-class landing, the p_b the closure returns against the data
   band; the argmax sensitivity to the closure (Veen / chutkey /
   ambient) measured on in-class designs.
3. **The prices of S32 section 15 re-taken on in-class designs**, and
   the flat valley re-read (it was measured on folded marches).
4. RE-2 / RE-3 in angle coordinates on the in-class landing.
5. Their inlet for RE-1 (the numerical transonic line; the floor at
   R_c 0.70 of S32 section 18 stays open).

## 8. Why the start line is vertical, and the start line ON A CHARACTERISTIC (2026-09-22 night; owner: "why must our IVL be a vertical line?", then "si" to the characteristic)

**Why it is vertical: history, not physics.** The record's start line
is a cut x' = const through the planar corner fan (whose field is exact
everywhere); through a cut upstream of every wall node the mass depends
on the fan and y_w0 alone, so it decouples from the shape (the driver's
C-3), and `build_case` passes a scalar x0. Measured costs: near a sonic
lip the fan's first rays lean past the vertical (to M 1.17 on this
posing, 1.83 on Chutkey's), so the cut is pushed to X0 0.05 R with a
declared strip; and the first marched column must bridge from the
vertical to the characteristic geometry. `plug_march` already accepts a
per-row abscissa -- "which lets the caller pose the start data ALONG A
CHARACTERISTIC ... Posing the start on a characteristic removes the
transition entirely" -- and no caller had ever used it.

**The march's column family is the C+.** `plug_march` builds each
column bottom-up: a new interior point is the crossing of the C+ from
the point below it in the same column and the C- from the previous
column (`foot_lm` is the C- slope; the wall "receives the C- family").
So a start line on a characteristic must be a C+ from the plug wall to
the jet boundary (the owner's question was answered with "a
right-running characteristic" after Humphreys, whose march runs C-
columns; ours runs C+ columns -- corrected here).

**Test 0, edge_fill (HMPH_EDGEFILL, additive; 0 = the S32 runs, the
rerun reproducing them to the printed digit).** At eta 8, z 0.12, the
march capped at 2 d: the first-column step goes -4.57 -> -4.01 -> -4.00
percent with 0 / 5 / 20 rows seeded in the edge wedge: the wedge is
0.57 points of the step, not the bulk.

**The characteristic start (HMPH_IVL=char, stage kernel, additive;
`corner_fan(x_stop=)` in a1_frame_march, default unchanged).** Through
the SAME wall point as the cut: (i) the C+ from that wall point traced
through the kernel's field to the leading ray (RK4, the fan's own
step), the fan rebuilt with the leading ray's last point exactly at
that crossing and every ray run to the same index, and the kernel part
re-traced BACKWARD from that fan point to the wall, 41 rows (the wall
row reset to the wall's slope, as on the cut); (ii) the corner fan's own
C+ line n_pts (its Goursat cells join point j of ray k-1 to point j of
ray k along a C+), 25 rows; (iii) the FREE-JET TRIANGLE between the
terminal ray and the jet boundary, solved with the march's own rotated
interior and free-jet cells for every C+ line up to n_pts (12 rows,
certified 0.035) -- the S32 uniform wedge would have carried 14.7
percent of the mass on this line (0.4 on the cut). Gate H-1 (char):
supersonic on every row and the triangle certified.

| run (march capped at 2 d) | first-column step | last column | folded |
|---|---|---|---|
| their throat, eta 8, vertical cut (S32) | -4.57 % | -4.68 % | 6.56 % |
| their throat, eta 8, C+ start | **-0.12 %** | -0.09 % | 1.53 % |
| R_c 4 control, vertical cut (S32) | -1.20 % | -0.96 % | 16.2 % |
| R_c 4 control, C+ start | **-0.04 %** | +0.20 % | 18.8 % |

**The eta ladder with the C+ start:** only eta 8 poses. At eta 2 / 4 / 6
the C+ from the cut's wall point meets the leading ray at z 0.71 / 0.80
/ 0.90 (x' 0.46 / 0.39 / 0.37 in, M 1.71 / 1.45 / 1.36) and the fan's
first ray, built through the series' field, lands BELOW the leading ray
there (rows not ordered at the junction); at eta 8 the junction is at z
1.00 (x' 0.36 in, M 1.32) and the construction holds. z 0.25 at eta 8
fails the same way (junction at z 1.12).

## 9. The A/B of the two poses on their wall (marched to D, eta 8, z 0.12, two rungs)

| | vertical cut, K 169 / N 61 | cut, K 322 / N 95 | C+ start, K 169 / N 78 | C+, K 322 / N 118 |
|---|---|---|---|---|
| start mass | 142.13 lbm/s (0.988 of 1-D) | 142.14 | 139.28 (0.968) | 139.27 |
| first-column step | -4.57 % | -4.57 % | -0.12 % | -0.11 % |
| mass at D vs the start | -5.99 % | -6.00 % | +0.53 % | +0.53 % |
| folded resolved cells | 3.12 % | 2.21 % | 14.60 % | 9.40 % |
| J / mdot vs their 222.05 | +2.92 % | +2.94 % | +3.07 % | +3.07 % |

(A second C+ start with the wall point at z 0.06: step -0.12 %, D
+0.54 %, J/mdot +2.99 %.)

READ.

1. **The S32 first-column step is the hand-over, and it is
   structural.** It is the same -4.57 percent at both rungs (the cells
   that bridge from a vertical cut to the first C+ column reach from the
   cut to ~1.2 in downstream at the top whatever the resolution), 0.57
   points of it is the edge wedge, and a start line of the column
   family removes it (-0.12 percent; the R_c 4 control -1.20 -> -0.04).
   **The S32 section 18 attribution to "the series at a sharp throat"
   is withdrawn for the step** (the eta dependence of the cut's step,
   7.4 -> 4.6 percent, is the data's consistency entering the same
   oversized cells).
2. **But the C+ start is not a clean pose either (the peer review's
   caution, confirmed by measurement).** A C+ from the plug wall to the
   jet boundary must cross the whole transonic triangle A-E-W_L: at
   R_c 0.70 it meets the leading ray at z ~1, where the three-term
   series is outside its reach (Dutton's twin, S32 10.2: the series on a
   true wall diverges beyond z ~0.5). The series' own discharge is
   0.992 on the throat plane, 0.988 on the cut at z 0.12 and 0.968 along
   the C+: **a truncation band of ~2.5 percent on the discharge**, beside
   the eta spread on the cut (W/W* 0.9763..0.9876 for eta 2..8, 1.1
   percent). The mass defect moved from the march (4.5 percent,
   structural) to the start data (2.5 percent, series).
3. **The A/B downstream says the two poses are NOT the same problem
   (stage kab, 1/3: AB-2 FAILS, the finding; AB-3 PASSES).** Beyond 2 d
   along their wall (144 stations at the finer rung) the C+ pose's wall
   pressure exceeds the cut's by 1.25e-3 p_0 on average, 1.97e-3 at
   worst (1.34 percent of p_w there), at EVERY station, and the
   difference moves by less than its band under refinement (band K_RICH
   x the rung move: 9.8e-5 at the worst station, 2.6e-4 at most): a
   real difference, of the sign of the mass each march actually carries
   at D -- the cut's 133.6 lbm/s (6 percent lost), the C+'s 140.0
   (conserved). And the C+ march folds more (9.4 against 2.2 percent at
   the finer rung, first fold ~0.7 in from the start): the start data
   taken from the series at z ~1 are not a consistent field. Neither
   pose is in class; neither discharge is certified. DECLARED (the peer
   review's reading): the folded fractions FALL under refinement in both
   poses (3.12 -> 2.21, 14.60 -> 9.40 percent), unlike the design's
   folds of stage class (28.78 -> 28.86, grid-stable): part of these
   folds is the net's, and a third rung is owed before either pose is
   called out of class on the folds alone. The C+ start fixed one
   functional (the mass) and worsened the other (the folds); without the
   margin in the driver there is no instrument to choose between the
   poses.
4. **Specific thrust on their contour (for the record, not a verdict):
   +2.9 to +3.1 percent above theirs in every pose**, their shear (0.2
   percent) not in ours. Against their stated 148.08 lbm/s -- which
   their own geometry cannot pass (T-6: 1.029 of the choked 1-D of
   A -> E). Read against their thrust over the choked 1-D mass of their
   line (32,881 / 143.89 = 228.5 lbf s/lbm; stage kab) our J/mdot is
   +0.01 / +0.02 percent (cut, two rungs) and +0.15 percent (C+); over a
   smooth-throat discharge 0.99 of it, about -0.8 percent. The
   comparison is bounded by THEIR mass inconsistency, not by our march.
   Three independent channels say the same thing at the same size: their
   stated mass is 1.029 of the choked 1-D mass of their own line (T-6);
   the discharge our marches carry through it is 0.968-0.988 of it; our
   specific thrust is +2.9..+3.1 percent over their stated one. The
   reading that closes the geometry-faithful twin is therefore not "H-6
   within 1 percent of 222.05" -- a pose that got there would get there
   by compensation -- but: on their geometry our machine reads
   228.5-228.9 lbf s/lbm, stable across two poses and two grids, and
   their 222.05 rests on a mass their throat does not pass; per unit of
   the mass it CAN pass, the two agree within 0.2 percent (the 2.5-percent
   series band and the folds declared beside it). Recorded; the owner's
   call whether the row closes on it.
5. **What it makes of the queue.** The binding constraint of the
   geometry-faithful twin is now explicit and measured: the start line
   must be a characteristic of the march (else the hand-over loses 4.6
   percent) AND lie in a field that satisfies the equations over the
   whole transonic triangle (else the start data carry the series'
   2.5-percent band and fold the march). The three-term series gives
   the second only near the throat plane; the numerical transonic
   solution of their throat (queue item 4 of the S32 handoff: an
   axisymmetric Euler time-march on the throat region, once per posing,
   outside the SQP loop) gives both: the C+ start line read from it with
   this session's machinery (`_char_start` with the field replaced).

Artefacts (not committed): `_humphreys_twin/run_kernel_eta8.0_{rerun,ef5,ef20}.log`,
`run_kernel_char_eta{2,4,6,8}.0.log`, `run_kernel_char_parabola_rc5.69.log`,
`run_kernel_char_eta8.0_toD_z{0.06,0.12,0.25}.log`,
`run_kernel_cut_eta8.0_toD_z0.12.log`, `run_kernel_{cut,char}_eta8.0_toD_K319N81.log`,
`kernel_{cut,char}_toD_eta8_K{160N41,319N81}.json` (the four tagged
records, HMPH_TAG, the inputs of stage kab), `run_kab_2026-09-22.log`,
`kab_opt.json`.

## 7. Conformity

- Branch `rde-nozzle-program`; identity AlexFalco5; no push.
- Files: `validation/a1_plug_spline_opt.py` (PSPL_PARAM, angle_W0,
  angle_wall, design_bounds, knot_radii; default bit-identical, measured
  on stage class), `validation/a1_humphreys_twin.py` (stage angle
  A-1..A-7, `_census` and `_j_parts` at module level, `_hermite`,
  `n_turns`, `read_table(mode=)`, opt() in angle coordinates), this log;
  registry row X-HMPH re-printed (committed after the log); ADVISORY_INDEX
  row; M0 Part VI addendum (the lever of the tail with the base priced);
  living PROGRESS parallel block.
- Not committed (the line's practice): `_humphreys_twin/run_*_2026-09-22.log`
  of tonight, `opt_opt_fan_veen_angle{,_free}.json`,
  `angle_opt_veen_angle.json`, the re-written `class_opt_veen.json`
  (byte-identical to the 18:02 record).
- Night (sections 8-9): `validation/a1_humphreys_twin.py` stage kernel
  gains HMPH_EDGEFILL and HMPH_IVL=char (`_char_start`, the free-jet
  triangle), both additive (the default rerun reproduces S32 to the
  printed digit); `validation/a1_frame_march.py` `corner_fan(x_stop=)`,
  default unchanged.
- Lints and suite: quoted in the commit messages.
