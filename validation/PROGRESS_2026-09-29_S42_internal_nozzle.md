# Session log 2026-09-29 / 09-30 — S42: the plug with a short cowl and an internal expansion nozzle; Rao against the SQP

Plain rules for this log: short sentences, one fact per line, physics before method.
The long text at the bottom is the record as it was written during the windows (it sat, uncommitted, inside the S41
log as sections T to T12; moved here unchanged so that the S41 log stays as committed).

## Where this sits in the plan
- Plug line, F3 material, done while the plan's open phase is F2. Out of order, declared.
- The Rao-versus-SQP comparison below is a REHEARSAL of the plan's decisive comparison, not the comparison itself:
  it did not follow the pre-registered protocol (`validation/TWIN_PROTOCOL_preregistration_2026-08-31.md`, plan line).
  The differences are listed in `PROGRESS_2026-09-30_reunion.md`.

## What the owner asked
1. Put the inlet turning inside the plug optimisation; plug and cowl walked together (shocks are expected when
   they are designed apart).
2. Then: an internal expansion nozzle that sets the angle at which the RDE outflow meets the plug; 87 mm in all;
   no imposed envelope; ambients 0.05, 0.2 and 1 bar; angles -5, -10, -14 degrees.
3. The comparison to make: Rao's plug designed at the mean state against the SQP that sees the 12 phases of the
   RDE cycle. Do they give two shapes, and which is better? The CFD decides.
4. Deliverable of the night: a certified table and a figure of the two profiles. CFD runs count only when converged.
   Read the result with scepticism. Check whether Rao's advantage comes from the base pressure.

## What was found
1. A cowl turned toward the axis, kept inside the engine's outer radius, gains nothing: it ties the straight cowl.
   The turned wall faces forward and its pressure is paid as drag. Only a cowl flared outward gains (0.7 % at
   0.05 bar, mean state).
2. With the internal nozzle at -10 degrees the flow reaches the cowl lip at Mach 1.80, turned 8.7 degrees toward
   the axis. Rao's plug and the SQP's plug are different shapes: tip radius 41.5 mm against 33.8 mm, tip angle
   +1.6 against -7.2 degrees.
3. At 0.05 bar the SQP's plug gives 1.65 % more thrust than Rao's over the 12 phases (CFD, two meshes, every phase
   steady; uncertainty 0.003 %). The design tool had said 1.69 %. On Rao's own freedom (only the plug after the cowl
   lip) the gain is 0.51 %.
4. The gain does NOT come from seeing the phases. The SQP at the mean state and the SQP with the 12 phases land on
   almost the same plug (tips 34.1 and 33.8 mm); the difference between them is walk progress. The gain over Rao
   comes from letting the ambient pressure, the length and the cut of the plug enter the design.
5. At 0.2 bar half of the phases (3 to 8) reach the cowl lip below ambient pressure. In those phases a shock system
   sits on the plug and moves; the thrust does not settle. Rao's plug is not beaten there: the SQP with the phases
   ties it in the CFD. The SQP at the mean state is slightly worse than Rao once the phases are counted: at this
   ambient the mean state misleads.
6. At 1 bar both plugs give less thrust than the bare RDE exit. In five phases the nozzle is pure drag.
7. Base pressure: at 0.05 bar the CFD puts a lower pressure on Rao's larger base, so pricing the base with the CFD
   widens the SQP's lead (1.49 % to 2.44 % for the first mean-state landing). Rao is not helped by the base convention where he loses.
   The wall thrust settles in under a millisecond; the base region needs five.
8. No SQP walk reached its optimum: every SQP number is a lower bound. On the afternoon of 09-30 the walks were
   continued: the mean-state plug reached 1.4172 (from 1.4104), the 12-phase plug 1.34798 (from 1.34725) over the
   phases, both still climbing at 15:25.
9. At 0.2 bar the walk used to stop after one step. Cause: its smallest allowed step was larger than the distance
   to the limit where the flow model stops being valid (characteristics of the same family crossing: a shock forming). With a four
   times finer step the plug-and-cowl walk gains 0.18 % over Rao in the tool after four segments (1.12373 against
   1.12176); the cowl moves by 0.06 mm only, the gain is the plug's. Not yet checked by the CFD.

## Defects found
- The cell solver of the flow march could stall 0.12 mm short of its answer and flag the whole result as not
  trustworthy. With 12 phases this happened on almost every evaluation and stopped every 12-phase walk. Fixed by
  an opt-in continuation (`A1_NEWTON_RESCUE=1`); results that were already trusted are reproduced bit for bit.
- The march shows a small jump in thrust (3 to 4 parts in ten thousand) when a cowl wall point appears next to the
  lip. Open. Nothing below that size can be certified by the march alone in the plug-plus-cowl posing.
- Phases whose lip pressure is below ambient have no model in the tool (no shock at the lip). Open; it is the
  plan's fitted-shock step (F4b).

## Where things are
- Table: `validation/_plug_contest/41_contest_table.md` (+ `.json`). Profiles: `41_contest_profiles_b10.png`.
- Walk folders: `validation/_plug_contest/L87/` (named in `PROGRESS_2026-09-30_reunion.md`).
- Tools, design files and the CFD referee live outside this repository, as for the earlier referee work:
  `RDE/handoff/plug_2026-09-29/` and `RDE/THOR/THOR_GPU/NOZZLE_2026-09-27/`. Italian handoff:
  `RDE/handoff/PLUG_CONTEST_HANDOFF_2026-09-29_sera.md`.
- Code options added, all off by default: `TWOP_BASIS`, `TWOP_REGION=RC` (a1_twowall, a1_plug_march),
  `PSPL_TRFOLLOW=2` (a1_plug_spline_opt), `A1_NEWTON_RESCUE` (a1_ideal_march_jax).

## Detailed record, as written during the windows (sections T to T12)

T. 2026-09-29 -- THE WALKER'S TWO DEFECTS, THE CLASS IN REGION R, THE INLET POSING'S OMISSION, PLUG + SHORT COWL
(PENDING-COMMIT, declared: every code change below is opt-in, unset = the record's path, and NOT committed; the
bit-identity gates with the options unset, the lints and the fast suite have NOT been run in this window. Scripts,
logs and backups: RDE/handoff/plug_2026-09-29/; state: RDE/handoff/PLUG_CONTEST_HANDOFF_2026-09-29.md.)
THE OWNER'S WORDS (in order): "ho ucciso le simulazioni perche' tenevano in ostaggio s2"; "SQP deve essere in grado di
certificare i profili indipendentemente dalla cfd, che rimane una verifica finale"; "gli urti sono un problema solo
qualora influenzino il profilo direttamente, sui bordi del getto sono attesi"; "mi pare che l'angolo di entrata sia
gia' stato considerato in passato"; "apriamo questa strada, considera di poter anche generare una cowl non riflessiva".
T1. THE DESIGN TOOL'S OWN MODEL HOLDS A BETTER PLUG THAN EVERY WALK'S LANDING (twop_anglelaw_probe): the referee's
50-member angle-law family written in the carrier's vector and marched at the mean state. March vs referee: correlation
0.983, offset -6.2e-3 +- 1.4e-3. Best member Pf87t24e02q10 (corner -24 deg, tail -2 deg): C_F 1.367734, cert 0.067,
smallest cell +0.49, against the cut Migdal 1.364816, AF2 1.354147, the cone 1.349423.
T2. WHY THE WALK STOPPED (twop_stall_probe, twop_barrier_probe; at the landing of the mean-state walk from the cone,
|grad| 0.2137, the class 0.44 inside): the adjoint = the frozen model's central difference = the re-march's, component
by component; along +grad the re-march gains +1.59e-3 at h 8e-3 and +2.81e-3 at h 1.6e-2, certified, in class. The
driver's segment (scipy trust-constr, 6 iterations) returns NO step; a barrier parameter of 1e-5 changes nothing; the
objective times 1/(|g| radius) (the linear model gains one at the radius) steps 4.4e-3 (+8.07e-4), 1.0e-2 in 12
iterations (+1.97e-3), the gain equal to the re-march's to 2e-6; ten times that scale walks through the class. The
re-obtainments of record had J in newtons (1.4e5, |grad|inf 1.5e5; throat_2026-09-23/rao_humphreys/run_sqp_*.log),
here J is C_F: six orders. Opt-in PSPL_JSCALE=radius (a1_plug_spline_opt.run_trsqp). Second defect, same driver: the
radius grows 1.5x on EVERY accepted base whatever the length walked (steps of 1e-10 accepted, the radius at its cap
0.25 after 12 segments, the scale down by 20): opt-in PSPL_TRFOLLOW=1 (the growth applies to the step; two steps in a
row under the radius floor = the instrument's resolution, stop).
T3. THE CLASS COUNTED CELLS THAT CANNOT REACH THE WALL (twop_foldcensus, twop_cminus_tracer): with the free jet above
the plug the whole-net no-fold class puts 38 of the 50 members out; on four members read cell by cell, every cell
under the floor has its C- leaving above the tip (7, 23, 524 and 0 cells; 15 to 57 mm above the tip), and in the wall's
domain of dependence (traced geometrically, and by the march's own region R of S34) the smallest cell is +0.47 ..
+0.51. Along +grad from the best member the whole-net KS goes +0.49 -> -0.49 between 0.05 and 0.1 mm: a step, not a
fold. The owner's ruling: the class is read where the wall feels it. Opt-in TWOP_REGION=R (a1_twowall.margin_dict;
a1_plug_march applies region R's mask to the census keys and to the wavefront replay's quads; the certificate stays on
the whole net, margin["cert_net"]). GATE RG-1..4 (twop_regionR_gate): the record's KS = the wavefront's = the
sequential replay's to 12 digits, J untouched, the margin's adjoint = the re-marched central difference, the certificate
unchanged: PASS on three designs.
T4. THE MEAN-STATE WALKS ON THE SIMPLE PLUG (87 mm; scale + region R, then the radius that follows the step):
  from the cone 1.349423 -> 1.365833 -> 1.368163; from the best member 1.367734 -> 1.368313 -> 1.368313.
Two starts 1.8e-2 apart in C_F land 1.5e-4 apart; their walls 2.0 mm apart at most (rms 1.3), the largest gap toward the
tip (35.8 against 33.9 mm): a flat direction. Common shape: turn at once to about -20 deg, hold to x 25 mm, return
almost linearly to about -1 deg at the tip. NOT CERTIFIED AS AN OPTIMUM: KKT residual 0.111 and 0.070, the walks stopped
at the radius floor (2.0e-3 lip radii). Figure validation/_plug_contest/36_plug_walks_mean_preliminary.png.
T5. THE INLET POSING'S OMISSION (found by the owner). The standing directive of 2026-08-08 makes the inlet turning
theta_i a DESIGN variable (the RDE outlet axial, the turning applied by the nozzle's inlet hardware) and step 15
(a1_inlet_angle_opt.py, 2026-08-09) measured the optimum at the exhaust angle 0. Section 3octies A above froze the inlet
axial ("the chamber's, not a design feature"): every number of the simple-plug contest is at theta_i = 0. At the
contest's pressure ratio the full turn is about 37 deg (M 1.556 -> 2.774). Rao's family at an axial lip (B above) is
one-parameter for the same reason: the throat's cant is the freedom the posing takes away.
T6. PLUG + SHORT COWL, FIRST MAP (march only, mean state, the plug of T4 NOT re-optimised, base 1.368313; the two-wall
carrier with the cowl's stub and length frozen and its knots and lip free): straight cowl 10 / 20 / 30 / 40 mm 1.388593
/ 1.406724 / 1.410494 / 1.410503; flared +5 deg 30 / 40 mm 1.419525 / 1.424332 (68 / 108 cells under the floor in the
channel); a straight cowl canted toward the axis from x 2 mm loses (-5 deg 1.3777 .. 1.3902, -10 deg below the base,
cells folded in the channel): it compresses. THE NON-REFLECTING COWL (twop_nonreflecting_cowl, v3): the streamline through
(x0, y_u) of the field of the plug alone in the inflow continued above the annulus (start line three annuli high, top
edge at the inflow's static pressure), the inflow's state imposed above the plug's leading C+; straight to x 17 mm (a
jump of -3.6 deg there: the fan of the arc's first 0.15 mm, unresolved), -4.0 / -6.3 / -9.2 / -11.7 / -14.7 deg at 20 /
25 / 30 / 35 / 40 mm, mass constant to 0.9 percent. At 30 mm: C_F 1.399132, lip radius 66.69 mm, -8.7 deg, Mach 1.82;
the plug's wall pressure follows the plug-alone field's to 40 mm, then a COMPRESSION STEP of +11 .. 13 percent at 43-45
mm -- 233 cells under the floor, the worst AT the plug wall at x 41-42 mm: the spline rounds the 17 mm corner and starts
turning before the wave arrives (cowl pressure 0.2716 against 0.2636 at 18 mm). That is a shock ON the wall: this start
is out of class by the owner's own rule, and the class says so (KS -0.9423). Earlier versions of the generator are
WRONG and archived as such (v1: a scattered interpolation turned the line from x 2 mm; v2: 7 columns of 141).
Figure validation/_plug_contest/37_plug_cowl_first_map.png. Opt-in TWOP_REGION=RC (region R + the cells between the
walls, a recorded decision S.d["chan_keep"]); with a 30 mm cowl region R already holds the channel (4638 cells both
ways). GATE on the non-reflecting start: RG-2..4 PASS, RG-1 FAIL as coded -- the three KS agree to the 12th digit
(-0.942255835530 / ...529 / ...529) against an absolute tolerance of 1e-12: the tolerance is not derived, to be redone.
T7. OPEN AT THE WINDOW'S END: the plug + cowl walks (Acowl_straight30 restored into class in 3 steps, KS -0.7534 ->
+0.5607, C_F 1.410522 -- its start was out by 33 SLIVERS of the lip's fan, x 45.5 mm, 19.4 mm above the wall, legs 0.77 x
0.005 mm, INSIDE region R with the lip at 30 mm, the plug's pressure smooth there: the class can still step during a
walk; Acowl_nonrefl30 and Acowl_flared30 chained); the 12 phases on any of today's designs; the
referee's 12-phase sweep of the q = 1 family (134 of 204 cases, 3 threads per case: the same C_F to 12 digits as with
24); Rao grafted at 29 mm; the stationarity of T4; the gates with the options unset.

T8. 18:05, AFTER THE CLOSE: THE FIRST PLUG + COWL WALK DID NOT WALK. Acowl_straight30: 1.410522 -> 1.410717 in two
segments, stopped by PSPL_TRFOLLOW's rule (two steps under the radius floor) with |grad|inf 2.94: not an optimum. The
landing's gradient is the cowl's knots with ALTERNATING signs (+1.52, -2.94, +1.67, +0.60, -1.46, +0.38, +1.04; the
plug's knots 0.02 .. 0.13): the knot-scale zig-zag -- eleven knots 2.5 mm apart on a 30 mm cowl -- whose ascent folds the
net within hundredths of a millimetre (class multipliers -4.8, -10). To be answered by the carrier's Newton metric
(TWOP_METRIC=start) or by a smooth cowl of two or three parameters; the stop rule needs a gradient test.

T9. 2026-09-29 EVENING -- THE INLET ANGLE IN THE JOINT WALK: THE COWL IN SMOOTH COORDINATES (PENDING-COMMIT, declared,
as T: the code change is opt-in and NOT committed; lints and suite NOT run in this window. Scripts, logs, starts and
backups: RDE/handoff/plug_2026-09-29/; state: RDE/handoff/PLUG_CONTEST_HANDOFF_2026-09-29_sera.md.)
THE OWNER'S WORDS: "stavamo sondando l'introduzione dell'angolo iniziale nell'ottimizzazione del plug. Vorrei precisare
che la presenza di shock e' normale se plug e cowl vengono ottimizzati separatamente."
T9.1 T6's READING RETRACTED AS A DESIGN READING. T6's map kept the plug FROZEN at the simple plug's landing and added a
cowl: its folded cells, its ranking of the cowl's cants ("a straight cowl canted toward the axis ... loses: it
compresses") and the out-of-class verdict on the non-reflecting start are the signature of two walls designed apart.
They are a list of STARTS. theta_i is judged on joint walks only (plug and cowl walked together). T8's list of "the
cowl's knots" is corrected too: its last entry (+1.04) is the plug's hub-arc end x_a, not a cowl knot (reduced layout:
0-10 the plug's knots, 11-21 the cowl's, 22 x_a plug, 23 t_a plug, 24 u plug, 25 the lip height, 26 the tip height).
T9.2 THE RAW GRADIENT AT THE FIRST JOINT LANDING (twop_stall_probe_cowl_straight30): the adjoint is the model's and the
march's (components 16-22 to three digits by re-marched central differences); along +grad the re-march follows it
(ratio 0.98 .. 0.99 to h 2e-4) and the net folds between h 1e-4 and 2e-4 lip radii (KS +0.5607 -> -0.9273): 0.014 mm.
T9.3 THE SMOOTH PART OF THE COWL'S MOTION (twop_cowl_metric_probe_straight30; the carrier's Metric hook, W = W_s + T z,
the plug's components untouched, the cowl's 11 knots + lip height through four smooth modes of s = (x - x_a) / (x_lip -
x_a): s, s^2 and the square and cube of the hinge at s_w 0.5311, x_w 16.87 mm -- the landing on the cowl of the hub's
leading C+, M_in 1.5561, mu 39.99 deg, annulus 14.15 mm, the posing's own datum). The cowl's gradient on the modes
(unit z = the lip moves one lip radius): cant +0.160, curvature +0.299, hinge^2 +0.474, hinge^3 +0.513 (the cant:
+1.15e-3 per degree, outward) against +-3 on the knots. Along T T^T g the re-march stays IN CLASS to h 8e-3 (the
cowl moved 0.35 mm, KS +0.172, gain +5.50e-3, 0.85 of the adjoint's prediction) and leaves it at h 1.6e-2 (KS
-0.745): the class scale is 60 times the raw direction's. Two smoothers of the 12 heights (first / second
differences, length 0.5) give the plug's own direction (the cowl's share of |u|^2 0.000 / 0.002): in class to h 4e-3
(+4.27e-3 / +4.28e-3), out at 8e-3; there the plug's gradient is its hub arc's end (+1.04): see T9.6.
T9.4 THE OPTION (a1_twowall.walk, opt-in TWOP_BASIS=<json {"T", "lb", "ub"}>, unset = the path of before): the walk in
the coordinates z of a declared map, T n x m with m <= n, the Metric hook with a map of record instead of the start's
secant Hessian; an optional box in z, counted from the start file's design; the restoration ascends the soft margin
along T T^T grad inside the box and its displacement is carried into the box handed to the driver (keep_feasible
False: with it a start ON the box freezes its components -- measured on a quadratic, scipy 1.17.1). Records
walk_FB_<date>.json carry basis, Z, Z_restoration. GATE twop_basis_gate BG-1..4, PASS 4/4 on two starts (one inside
the box, one ON it): BG-1 the chain rule, |grad_z J - T^T grad_W J|inf 2.1e-17 and 0 against the derived round-off
bound 2.4e-14 / 2.3e-14, the margin's 0 and 8.9e-16 against 5.7e-14 / 2.2e-12; BG-2 the identity map is the carrier
to the last bit (J, certificate, KS, both replays); BG-3 the box is the envelope on its 8 corners and 200 random
points, and one coefficient 1e-3 outside it breaks the envelope by 1.0e-3 (the rejector); BG-4 the restoration's
clipped move outward is zero from a start on the box.
T9.5 THE ENVELOPE (DECLARED by the session, the owner's confirmation asked): the cowl stays inside the engine's outer
radius, y <= y_u. Without it the smooth gradient says "flare" (T9.3: every mode outward), which answers another
question (more exit area at 0.05 bar). The family (twop_cowl_basis): y = y_u up to x_w, then y = y_u + h^2 sum_i c_i
B_i(h), h = (x - x_w) / (x_lip - x_w), Bernstein polynomials of degree 2, c_i <= 0 (sufficient for the envelope;
exact for degree 1). The non-reflecting cowl of T6 is in it to 0.04 mm (c -0.0612, -0.0182, -0.0193; lip 66.69 mm,
lip cant -11.9 deg).
T9.6 THE MARCH'S OWN JUMP (twop_jump_probe, twop_jump_scan; finding to mint: twowall:cowl-lip-wall-point-jump). Along
three different directions from the first joint landing the re-marched C_F follows the adjoint to h 1e-4 and is LOWER
at h 3e-4 (-1.8e-4, -2.3e-4, -2.3e-4 against a model at +2.5e-4, +3.4e-4, +3.4e-4). Bisected along the plug's
direction: between h 1.0547e-4 and 1.0625e-4 (5e-5 mm of wall motion) C_F goes 1.410834205 -> 1.410447113
(-3.87e-4), the cowl's wall points 32 -> 33, the cells 3886 -> 3885, the certificate and the class unchanged; 40 of
the plug's 140 wall points change state, the largest at the tip. Scanned at the rung of record (140, 31), 13 points to
h 3e-4: ONE jump, -3.84e-4, and the local slope is 1.10 .. 1.11 before it and 0.19 .. 0.26 after it (the adjoint's
1.0994 is the slope of the tooth the design sits on). Mechanism, read in a1_plug_march: the lip is a vertex of the net
whose state comes from an inverse cell with its foot on the C- leg from the last cowl wall point to the next
column's top interior; a wall point appearing next to the lip changes that leg at once, and with it the lip state,
the fan and the plug's pressure downstream. At the doubled rung (280, 61; the same design reads 1.412316940, +1.60e-3) the
same scan: ONE jump of -2.72e-4 where the cowl's wall points go 64 -> 65, smaller teeth of 2e-5 .. 5e-5 elsewhere, local
slopes +0.2 .. +2.1 before it and -0.24 .. -0.57 after it: the jump does NOT halve with the rows doubled (0.71 of the
coarse one), a defect of the lip's treatment, not a resolution error. CONSEQUENCE: below about 3e-4 .. 4e-4 in C_F the
march alone does not tell two designs apart, at either rung, and a landing's gradient can be a tooth's (T9.3's +1.04
on the hub arc's end is one: 1.10 before the jump, 0.2 after it); the free joint walk's rejected trials after its
fifth base are 3.3e-4 and 4.2e-4 below the incumbent. This bounds what the SQP can certify by itself (the owner's
directive 4) until the lip is treated as a smooth function of the design.
T9.7 THE REFEREE'S 12-PHASE SWEEP ENDED (20:48; 204 of 204 cases, 3 ranks x 1 thread, the frozen binary): the simple
plug's q = 1 family at theta_i = 0, 17 members, judged at the mean state (inlet index 12) and over the 12 phases
(tables CASE_2D/family87q1_mean_table.json, family87q1_K12_table.json). The two judges choose the SAME member and the
same order of the first four: Pf87t24e02q10 1.36182 / 1.30189, Pf87t24e08q10 1.36095 / 1.30069, Pf87t31e02q10
1.36018 / 1.29939, Pf87t31e08q10 1.35878 / 1.29773 (mean / 12 phases); they differ from the fifth place on
(Pf87t17e02q10 seventh / fifth). At the grid's resolution (7 deg on the corner, 6 deg on the tail) the mean-state
optimum and the 12-phase optimum of the simple plug coincide; the mean state overstates C_F by 4.6 percent. A map of
the referee, not the method's verdict (the owner, 2026-09-28).
T9.8 THE JOINT WALKS (mean state, march only; plug_cowl_walk_basis.sh; 24 segments x 12 iterations, radius declared
8.074e-3, the scale and the radius that follows the step; records _plug_contest/L87/AcowlB_*; readings
twop_joint_read_evening{1,2}.log).
(a) FREE, no envelope, the four smooth modes of T9.3, from the first joint landing (AcowlB_straight30_poly): 1.410717
-> 1.411707 -> 1.418592 -> 1.419068 -> 1.421089 in five bases, then the same trial rejected at the radius floor
(1.420755, 1.420672: the jump's size) -- stopped by the session at segment 11 (it was cycling), the landing is its
checkpoint. The cowl FLARES: lip radius 69.52 mm, lip angle +16.8 deg, lip Mach 2.565, p / p_a 1.43 at the lip, A_e /
A_i 2.146; the plug's hub arc 0.74 -> 0.51 mm, its tip angle -0.8 -> -3.1 deg; in class (+0.438), certificate 0.28,
|T^T g| 1.74: not stationary. Without an envelope the walk buys exit area.
(b) THE NON-REFLECTING START REPAIRED BY THE JOINT RESTORATION (AcowlB_env_nonrefl30; the family of T9.5 fitted to T6's
non-reflecting cowl, the plug of T4): KS -0.9341 -> +0.1996 in FOUR restoration steps along T T^T grad of the soft
margin (2.85e-3, 4.5e-5, 1.8e-4, 7.1e-4 lip radii: 0.26 mm in all), C_F 1.399938, where the raw-knot restoration of
T8's window had stalled at -0.9356 with steps of 1e-6. What moved: the cowl's FIRST coefficient, -0.0612 -> -0.0299
(the turn begins later and more gently, the heights after x_w 0.011 .. 0.13 mm further out), the lip where it was
(66.72 against 66.69 mm, -10.3 deg); the plug's largest wall-pressure rise +18.3 percent at x 42.5 mm -> +4.2 percent
at x 44.0 mm. The half-cant start (the same cowl times 0.5, AcowlB_free_nonrefl30x05) is repaired in TWO steps, KS
-0.8016 -> +0.0749, C_F 1.406290, the first coefficient -0.0306 -> +0.0185 (11 micrometres outside the envelope at two
heights). The owner's statement measured: the shock of T6 belongs to two walls designed apart, and a joint move of a
quarter of a millimetre removes it.
(c) WITH THE BOX IN THE SOLVER the walks do not walk (AcowlB_env_straight30: two segments, steps 2.7e-4 and 4.7e-4
under a radius 6.4e-3, stopped by PSPL_TRFOLLOW's rule; AcowlB_env_nonrefl30 after its restoration: 1.399938 ->
1.400244, steps 4e-4 and 1.2e-3), and neither does the plug alone under the frozen straight cowl
(AcowlB_env_straight30_frozen: 1.410345 -> 1.410380, steps 1.6e-4 and 2.1e-4), which has no box: the cause is the
solver next to the class. twop_trbox_probe at that base: KS - mu0 +0.0089, |grad_z KS| 367, the class 2.4e-5 away in
the linearisation (0.0016 mm: the lip fan's slivers of T7); today's segment steps 1.6e-4 and moves AWAY from the class
(+0.0564); the trust region posed as the solver's own box with a unit radius steps 2.2e-2 .. 4.9e-2 THROUGH the class
(KS -0.87 .. -0.91): rejected as a remedy. scipy's trust-constr measures its trust region in slack-scaled variables: next
to the class its step is proportional to the distance from it. Two answers, both in place: the box is handled as an
ACTIVE SET by hand (twop_cowl_basis COWL_FROZEN / COWL_DROP: the coefficients on the box are left out of the map and
the landing's gradient on them is the KKT test), and the stop rule tries the projected ascent from the incumbent
before stopping (a1_plug_spline_opt, opt-in PSPL_TRFOLLOW=2; unset or 1 = the path of before).
(d) THE FIRST-ORDER TEST OF THE ENVELOPE (twop_joint_read_evening2; the gradient of C_F on the family's three scaled
coefficients, positive = outward): under the straight cowl with the plug re-walked (1.410380) +0.248, +0.062, +0.463;
at the repaired non-reflecting design (1.400244, lip 66.72 mm, -10.3 deg) -0.005, +0.279, +0.629; at the repaired
half-cant design (1.406829, lip 67.48 mm, -0.35 deg) +0.291, -0.091, +0.628. With c <= 0 the straight cowl satisfies
the first-order condition of the box (every inward motion loses), and from both inward starts the gradient points back
to the envelope. NOT A VERDICT YET: no walk has landed stationary, the gradients carry the teeth of T9.6, one cowl
length (30 mm), the mean state only.
T9.9 THE LANDINGS INSIDE THE ENVELOPE (the family of T9.5 with no box in the solver, the active set by hand; the stop
rule with the ascent for the last two; twop_joint_read_evening3.log). Mean state, march only, cowl 30 mm:
  the straight cowl held, the plug re-walked (AcowlB_env_straight30_frozen, then AcowlB_frozen2_straight30): 1.410345
    -> 1.410380 -> 1.410420, lip 68.00 mm, 0 deg, lip Mach 2.044; class +0.118; the ascent's probe 3.0e-3 further reads
    1.411395 OUT of class (the lip fan's slivers): the landing is bound by that wall, not by the thrust;
  from the repaired non-reflecting design (AcowlB_free_nonrefl30, 12 accepted bases of 18 segments): 1.400244 ->
    1.410533, the lip 66.72 -> 67.64 mm, the lip angle -10.3 -> -5.35 deg, lip Mach 1.77 -> 1.88, the plug's tip angle
    -0.8 -> -3.2 deg, class +0.547, largest wall-pressure rise +3.8 percent at x 65.7 mm;
  from the repaired half-cant design with its first coefficient held at zero (AcowlB_free2_nonrefl30x05): 1.406448 ->
    1.408512, the lip 67.47 -> 67.69 mm, lip angle +0.58 deg, class +0.532.
The gradient of C_F on the family's three coefficients at the three landings (positive = outward): +0.225, +0.097,
+0.451; +0.214, +0.659, +0.271; +0.178, +0.199, +0.460 -- outward everywhere. READING: both inward starts walk BACK
toward the envelope and gain as they do (+1.03e-2 and +2.1e-3); the best inward landing (lip 0.36 mm inside, -5.35
deg) and the straight cowl differ by 1.1e-4, a third of the instrument's jump (T9.6): TIED at this instrument. No
landing is stationary (|T^T g| 0.62 .. 0.83); every walk ended at the radius floor with the ascent failing or out of
class. Inside the envelope, at 30 mm and at the mean state, turning the cowl toward the axis has not produced a design
better than the straight cowl; the FREE walk of T9.8 (a), which flares, is +0.75 percent above both.
T9.10 THE SAME DESIGNS UNDER THE 12 PHASES (twop_phase_eval_cowl30{,b}.log; the tournament's family_K12, the class
read at the mean state, J = sum_k w_k C_F,k): mean state / 12 phases --
  free, flared (no envelope)                 1.421089 / 1.354753
  straight cowl, plug re-walked              1.410380 / 1.345222
  from the non-reflecting design, landed     1.410533 / 1.345000
  from the half-cant design, landed          1.408512 / 1.343834  (one phase uncertified, 8.0e9)
  the half-cant design as repaired           1.406829 / 1.341480
  the non-reflecting design as repaired      1.400244 / 1.335291  (one phase uncertified, 4.6e10)
The ratio 12 phases / mean is 0.9533 .. 0.9541 on all six: the mean state orders these designs as the phases do; the
two tied designs are tied under the phases too (2.2e-4). For scale: the simple plug's best family member reads
1.36182 / 1.30189 by the referee (T9.7): the straight 30 mm cowl is worth about +3.4 percent under the phases (march
against referee, the offset of T1 not removed: a reading, not a graded number).
Figure validation/_plug_contest/38_plug_cowl_joint_walks.png (script RDE/handoff/plug_2026-09-29/plug_cowl_joint_fig.py).
T9.11 A PHYSICAL READING OFFERED TO THE OWNER (a proposal, not a claim of record): step 15 (2026-08-09) delivered the
flow ALREADY turned -- theta_i an inflow condition, the hardware that turns it outside the control volume -- and found
the optimum at an axial exhaust; here the RDE's exit is axial and the hardware that turns it is INSIDE the control
volume: a cowl wall canted toward the axis faces forward, and its pressure (2 to 5 p_a at the lip) is paid as drag
before the plug collects anything. The plug's own hub corner (-23.6 deg in every landing) is the inward turn that
costs nothing, and the straight cowl is what contains it.
T9.12 OPEN AT THE WINDOW'S END: the envelope and the cowl's length are the OWNER's to set (68 mm and 30 mm assumed);
the lip's jump (T9.6) before any claim under 4e-4; the lip fan's slivers in region R (the straight cowl's landing is
bound by them); no walk with the 12 phases voting (12 times the cost: one segment about an hour on three threads);
the gates with the options unset; the referee on the finalists; Rao grafted at 29 mm; the registry rows (five, drafted
in the evening handoff section 9); docs/rde_nozzle_PROGRESS.md and M0 (R3 / R4 PENDING, declared).
CONFORMITY OF THE WINDOW: lints run on the working tree at 21:37 -- numeric PASS (131 files, 0 ratchet violations),
claims PASS (0 violations), advisory index PASS (134 rows, 0 violations); the suite NOT run; nothing committed.
Machine: at most 12 threads, nice 19, pinned; one process of the session killed by its PID (the cycling free walk).

T10. 2026-09-29 NIGHT -- THE OWNER RE-POSES: AN INTERNAL EXPANSION NOZZLE BEFORE THE PLUG (PENDING-COMMIT as T9).
THE OWNER'S WORDS: "plug o shrouded plug (cowl+plug) si mischiano percio' cominciano a sovrapporsi. Vedo che il plug
continua a cominciare piu' o meno alla base della initial value line mentre io pensavo di introdurre un ugello di
espansione interna quando parlavo di trattare l'angolo iniziale con cui l'outflow RDE incontra il plug, humprey non
diceva nulla sull'impatto dell'inclinazione della IVL sull'ottimizzazione? il confronto che dobbiamo riuscire a fare
e' tra un metodo di rao applicato utilizzando lo stato medio di stechmann come riferimento dell'RDE contro SQP che
tiene in conto delle fasi."
T10.1 WHAT HUMPHREYS SAYS (Humphreys, Thompson and Hoffman 1971, pp. 1585-1586, re-read in this window): the
formulation "assumes specified values for the cowl lip radius and initial injection angle"; both "have a significant
influence upon the total thrust"; they are NOT variables of the variational problem, they are found by a PARAMETRIC
study outside it (20 runs + 1 at the optimum; the throat height varied to hold the mass flow): lip radius 7.55 in,
injection angle -34 deg, 32,881 lbf; Rao's method on the same case gives 8.33 in and about -58.5 deg, 34,253 lbf. The
total thrust (their Eq. 36) separates what crosses the start line and the ambient on the inlet's frontal area (set by
the lip radius and the injection angle) from the wall and the base (what the contour optimisation maximises). The
difference from Rao is attributed to the START LINE (Rao: a linear sonic line of constant direction); "a parallel
uniform flow with the flow direction toward the axis of symmetry is one of compression" unless the start line's Mach
number is about 1.5. THE DIFFERENCE FROM OUR CASE: their inlet is a sonic throat fed by a subsonic stream, whose
inclination is the inlet's geometry; ours arrives SUPERSONIC and AXIAL (M 1.556), so an inclined start line has to be
made by a supersonic internal nozzle.
T10.2 THE INTERNAL NOZZLE, A PLANAR ESTIMATE (internal_nozzle_pm_table.py; Prandtl-Meyer about the hub's corner, the
outer wall on the fan's streamline through the outer radius, constant gamma 1.2774, the Stechmann mean state; PLANAR
relations on an annulus 53.85 - 68 mm: an estimate, the annulus is axisymmetric -- see T10.3): injection angle /
Mach delivered / cowl length / lip radius: -5 deg 1.707, 23.2 mm, 67.71 mm; -10 deg 1.859, 30.9 mm, 66.68 mm; -15
deg 2.014, 40.6 mm, 64.54 mm; -20 deg 2.174, 52.7 mm, 60.68 mm; -25 deg 2.340, 68.2 mm, 54.20 mm; -30 deg 2.514,
88.3 mm, 43.68 mm; the full turn to the ambient -36.98 deg, 2.774, 127.2 mm, 17.74 mm. The angle and the cowl's
length are ONE choice. The turn that ends with an axial, fully expanded exhaust is HALF the full turn: -18.49 deg
(Mach 2.125, cowl 48.7 mm, lip radius 62.07 mm), the other half by the lip's own fan; the ideal C_F 1.4460 (the bare
exit 1.2916). The evening's 30 mm cowl was the -10 deg member of this family.
T10.3 THE SAME WALLS IN THE CARRIER (twop_internal_nozzle_oracle_b10.log; hub arc 0.5 mm, straight plug wall at -10
deg, the cowl on the planar streamline, lip at 30.94 mm, 66.685 mm): the march reads Mach 1.786 and -9.55 deg at the
lip (the planar estimate 1.8595, -10 deg), Mach 1.70 .. 1.857 along the plug's wall where the estimate is uniform,
largest wall-pressure rise +1.7 percent; class +0.516; THE RECORD IS NOT CERTIFIED (worst certificate 1.1e11, one
cell), so these are readings. NOT A GATE: the known answer is planar and the carrier is axisymmetric; the afternoon's
non-reflecting cowl, built on the carrier's own axisymmetric field (T6), delivers -8.7 deg and Mach 1.82 at 30 mm. An
exact answer for this posing needs either the planar mode or a fan treatment of the hub's corner (one station on a
0.5 mm arc carries the whole turn).
T10.4 THE POSING PROPOSED TO THE OWNER (decisions asked, nothing launched): the same internal nozzle, designed at the
mean state, for both contestants; the classical contestant = Rao's method from the inclined start line at the
Stechmann mean state; ours = the SQP from the same start line with the 12 phases voting; both judged under the 12
phases by the march, the referee as the final check. Asked: the injection angle (one value or a scan as Humphreys),
the length budget (does the 87 mm include the internal nozzle), the envelope.

T11. 2026-09-30 NIGHT -- RAO AT THE MEAN STATE AGAINST THE SQP ON ONE INTERNAL NOZZLE, JUDGED BY THE REFEREE (PENDING-
COMMIT as T9; state: RDE/handoff/PLUG_CONTEST_HANDOFF_2026-09-29_sera.md sections 12-16).
THE OWNER'S WORDS: the scan of the injection angle, 87 mm IN ALL, no imposed envelope ("questo aspetto deve essere
figlio dell'ottimizzazione e delle condizioni di ambiente che non saranno sempre di vuoto"); "proviamo anche 1 BAR,
proviamo gli angoli da te proposti"; "chiaramente lo scopo del lavoro e' dimostrare una procedura, vogliamo scoprire se
fare un ugello con Rao usando lo stato medio o uno con sqp producano due figure diverse e quale delle due e' ottima (ce
lo dice la cfd)"; "potresti sfruttare il cluster per girarle invece di s2 ... mettersi nel frame della detonazione
sfruttando la rotating frame feature di mose_open"; "sii pulito e non accumulare troppe soluzioni".
T11.1 THE INTERNAL NOZZLE, AXISYMMETRIC (twop_internal_nozzle_family; hub arc of 6 mm from the axial hub to beta, then
straight; the cowl on the streamline of the inner wall's own field in the inflow continued above the annulus, ended
where the arc's last C+ lands): beta -5 / -10 / -14 / -18.49 / -25 deg -> the lip at x 28.76 / 35.76 / 42.30 / 50.65
/ 64.72 mm and r 67.53 / 66.48 / 65.07 / 62.70 / 57.57 mm, delivering Mach 1.685 / 1.804 / 1.872 / 1.934 / 1.906 and
-4.41 / -8.71 / -11.61 / -14.68 / -15.77 deg at the lip (the planar estimate of T10.2: 1.708 / 1.860 / 1.983 / 2.125 /
2.340): the inward stream recompresses by convergence (Humphreys p. 1586), beyond -18.5 deg the lip's Mach stops
growing.
T11.2 THE ANGLE GENO TAKES -- AN ERROR OF THE SESSION, CORRECTED. GENO's Rao plug (nozzle_type 8) prints its angles
in the usual sign (its wall reproduces Humphreys' Table 3, -60.7 .. -13.3 deg; the control surface's first segment
has the slope tan(theta_E - alpha)) and its fan reads theta_E = theta_i_plug - dnu; the PHYSICAL flow direction at
the lip before the lip's fan is theta_E - dnu = 2 theta_E - theta_i_plug (the validated Humphreys-Rao run: 2 (-6.00)
- 45.35 = -57.35 deg, the paper's "approximately -58.5 deg"). The input for a lip flow theta_lip is theta_i_plug =
theta_lip + 2 dnu (rao_member.py, the fan's turn read from GENO's own first run). Every GENO run of the session made
with theta_i_plug = -+ theta_lip was WRONG and is removed; the "Rao graft" 1.401409 of the first attempt was Rao's
plug for a lip flow of -13.1 deg on a nozzle delivering -8.71 deg: not the classical contestant (it served as the
walks' start only).
T11.3 RAO'S MEMBERS (the rule: Rao's optimum at the ambient if it fits the budget, otherwise the member of the
budget's length; only members that pass the whole mass): for the three lips the lip condition gives Rao's ambient
0.12 .. 0.25 bar over the whole family, so at 0.05 AND at 0.2 bar the length constraint is active and the member is
the same: -5 deg 58.20 mm (theta_E +12.1 deg), -10 deg 51.19 mm (+1.8 deg), -14 deg 44.64 mm (-5.2 deg).
T11.4 THE TWO SHAPES AT -10 DEG (figure validation/_plug_contest/39_rao_vs_sqp_shapes_b10.png). Rao grafted at the lip
plane (the cone r 48.077 mm at -10.0 deg, Rao's wall r 48.265 mm at -12.0 deg, shifted by -0.19 mm): -10 deg under
the cowl, then back to +1.6 deg at the tip, tip radius 41.5 mm. The SQP at the mean state (the hub arc and the cowl
held, the plug's 11 knots and tip height walking; AcowlB_intnoz10_plug, 24 segments): -12 .. -16 deg, -5.8 deg at the
tip, tip radius 34.9 mm. The walls are 6.6 mm apart at the tip, 9.8 deg in angle: TWO DIFFERENT PLUGS.
T11.5 THE REFEREE'S VERDICT (2D axisymmetric Euler per phase, MOSE_open, the referee extended to the short cowl:
gen_nozzle_mesh.py --cowl, a wall to the lip and a connection after it; 78 cases on the cluster in minutes; figure
validation/_plug_contest/40_rao_vs_sqp_cfd_verdict_b10.png; tables CASE_2D/referee_cowl*_table.json). Average over
the 12 phases / the mean state's case:
  0.05 bar   Rao 1.32253 / 1.38360    SQP 1.34213 / 1.40530    SQP ahead by 1.48 percent; no wall-pressure rise above 7 percent
  0.2 bar    Rao 1.12902 / 1.17926    SQP (designed at 0.05) 1.12341 / 1.16385    SQP designed at 0.2 bar 1.12529 / 1.16869
  1 bar      Rao 0.36337 / 0.36836    SQP (designed at 0.05) 0.34255 / 0.33358    (no nozzle, 2026-09-28: 0.4095)
The march at 0.05 bar: Rao 1.386126 / 1.324883 (mean / 12 phases; one uncertified free-edge cell in one phase), SQP
1.408300 / 1.344997; referee minus march -0.18 and -0.21 percent. READING: at the design point, where the nozzle runs
without shocks on its walls, the SQP's plug beats Rao's by 1.5 percent and the independent runner confirms it; at 0.2
and 1 bar the walls carry shocks (pressure rises of 130 .. 280 percent) and Rao's plug is ahead, also of the SQP
designed at 0.2 bar. [The cause first written here -- "shocks that the design tool does not see" -- is RETRACTED: see
T11.6.] The MOC tool cannot be posed at 1 bar at all (mean P0 1.417 bar, pressure ratio 1.42 below the critical 1.82;
exit static pressure 0.14 .. 0.62 bar in the 12 phases).
LIMITS, declared: the SQP of this table is the MEAN-STATE SQP (the walk with the 12 phases voting is running from its
landing: it is the contestant the owner asked for); one injection angle closed end to end; a 2D per-phase referee
(3 to 4 phases live together in an 87 mm nozzle and the azimuthal motion is ignored: the 3D run, or the wave-frame
run, is the judge of record); eight cases of 78 died at start-up at CFL 0.8 and were redone at 0.4.
T11.6 THE CAUSE OF THE 0.2 BAR RESULT, MEASURED (the owner: "come farebbe rao a vedere gli urti scusa?"). Rao's method
is isentropic: it sees no shock. The three designs judged by the MARCH ITSELF at 0.2 bar, with its separation closure
(Summerfield), mean state / 12 phases (twop_phase_eval_pa020_*.log, every record certified, class +0.25):
  Rao 1.181248 / 1.121759;  the SQP designed at 0.2 bar 1.173895 / 1.112116;  the SQP designed at 0.05 bar 1.168917 /
  1.108210  --  the referee's own order (1.12902 > 1.12529 > 1.12341).
So (i) the design tool's model RANKS these designs as the referee does: the model is not what lost; (ii) the SQP's
landing at 0.2 bar is WORSE than Rao's plug by the SQP's own objective: the walk (AcowlB_intnoz10_plug_pa020, from the
superseded graft, 5 records, closed by the stop rule) did not reach the optimum; (iii) Rao's member of this length is,
by its own lip condition, the optimum of an ambient of 0.164 bar (T11.3): it sits near its design point at 0.2 bar
and far from it at 0.05 bar. The walks from RAO'S OWN PLUG at 0.2 and at 0.05 bar are launched
(AcowlB_intnoz10_fromRao_pa020, AcowlB_intnoz10_fromRao): a walk from the reference can only tie or improve, and a
landing under it is a broken walk.
WHAT THE TOOL DOES AND DOES NOT MODEL: a wall that falls under k p_a is priced at the ambient from there on (the
separation closure: the simplest model of a shock-induced separation) and the attached class keeps it from happening in
the design; an OVER-EXPANDED LIP (the lip's pressure under the ambient: phases 6, 7, 8 at 0.2 bar enter at 0.14 .. 0.18
bar) has no model -- the lip's fan has no rays and the lip margin only says so; a wall compression that folds the net
is excluded by the class, not computed. Ways to add them, by cost: an oblique shock at the lip for the over-expanded
phases (a fitted discontinuity at one known point); a shock-capturing space-marching Euler solver in place of the
MOC net (the flow is supersonic throughout, the march stays a march, and it differentiates); the referee in the loop
is NOT among them (the owner, 2026-09-28).

T12. 2026-09-30 NIGHT, SECOND PART -- THE CERTIFIED TABLE (PENDING-COMMIT as T9). The owner's deliverable: "una tabella
certificata con il confronto tra i metodi e un png che mostra i due profili. Assicurati che le run cfd arrivino a
convergenza prima di considerarle. Guarda i risultati con scetticismo"; and "butterei un occhio sul se il vantaggio di
rao sia dovuto alla pressione di base". Tools in RDE/handoff/plug_2026-09-29/ (referee_cert.py, post_cert.py,
contest_table.py + contest_spec.json, twop_stall_probe.py, twop_rescue_gate.py).
T12.1 THE 12-PHASE WALKS WERE STOPPED BY A FALSE ALARM OF THE CERTIFICATE, NOT BY AN OPTIMUM. Three walks with the 12
phases voting took no step: from the mean-state optimum (start 1.344997, |grad|inf 0.196; start ladder out of class at
h 1.8e-4 with certificate 5.5e9; both ascent probes "record not certified"; closed by the stop rule after 4615 s), from
Rao's plug on Rao's own freedom (ladder 8.9e-5: 7.6e10; segment 1 "base not certified (worst 2.3e11)") and at 0.2 bar
(ladder 8.9e-5: 1.6e10). With 12 phases a record has 12 times the cells of a mean-state record, and one cell over the
bound rejects it. THE CELL (twop_stall_probe.py on the record of the lip scan, the free-edge cell ('jet', 31),
certificate 8.1e10, cond(J) 5.4e9): the damped Newton chooses its trial by the residual NORM, whose rows mix units
(position ~1, compatibility ~u^3 ~1e9); from the stalled iterate the full step toward the root RAISES that norm (0.67
-> 1.6e5) and so does every damped trial (0.81 at t = 1/64), so the trial t = 0 is kept and the cell stops 1.8e-3 lip
radii (0.12 mm) from its root. The plain Newton from the same iterate converges in 3 steps (1.8e-3, 3.2e-7, 3.8e-14):
the cell is well posed. REMEDY, opt-in (a1_ideal_march_jax.py NEWTON_RESCUE, env A1_NEWTON_RESCUE=1; unset = the
code path of record): a cell that ends OVER the bound is continued with plain Newton steps from its stalled iterate
and the root is kept only if certified; a cell that ends certified never enters it. GATE (twop_rescue_gate.py, the 7
records of the lip scan, off / on): RG-1 the 4 records certified with the option off are reproduced BITWISE (thrust,
certificate, class) PASS; RG-2 the 3 failing records (two at ('jet', 31), one at ('wall', 128)) certified with it on
(0.041, 0.044, 0.034) PASS; RG-3 their thrust on the parabola through the certified neighbours (off it by 4.2e-6,
2.7e-6, 3.8e-6; the neighbours' own residual 2.1e-6) PASS. The thrust of the two free-edge records is unchanged to the
last digit (that cell's C- leaves above the tip), the wall cell's record moves by -1.7e-6. Rao's plug under the 12
phases at 0.05 bar is now CERTIFIED at the same number (1.324883, worst certificate 0.055; it was 1.3e11 in phase 1).
The three walks are relaunched with the option on (BcowlB_intnoz10_fromA, BcowlB_intnoz10_ext_fromRao,
BcowlB_intnoz10_fromRao_pa020).
T12.2 THE REFEREE, CERTIFIED IN TIME (referee_cert.py: several dumps per case, sol-overwrite false; post_cert.py: a case
is CONVERGED when its last three dumps agree within 1e-4 of the last, otherwise UNSTEADY; the batch on the cluster, one
80-core node per 26 coarse or 13 fine cases, every case pinned; the cases that die at start-up at CFL 0.4 re-run at 0.2;
fields stripped and the cluster copy removed after the post). WHAT THE CLOCKS SAY. At 0.05 bar the walls' thrust settles
within 0.75 ms on both meshes (last-3 spread under 1e-5 at 2 ms, under 1e-7 at 5 ms); the BASE has its own clock: the
region under the tip is subsonic and fed by the start (p_b/p_a 1.8 at 0.25 ms -> 0.15 at 2 ms on Rao's plug, phase 12)
and the low-pressure phases (6, 7, 8) have not settled it at 5 ms; the base is therefore certified apart
(post_cert base_converged) and read on the 5 ms runs only. At 0.2 bar 7 phases of 12, at 1 bar 12 of 12, never settle
(the plug over-expanded, a shock system moving on it): those are run to 6 ms with 60 dumps and read as the MEAN over
2..6 ms with a batch-means uncertainty (4 batches of 1 ms) and a drift flag (window mean vs its halves). A defect of
the night found and fixed: three drivers at once shared one temporary sbatch name, the 1 bar cases ran twice on two
nodes into the same folders (the batch discarded and re-run clean; per-tag names and a resume mode since).
T12.3 THE 0.05 BAR VERDICT (the design ambient; cert_long005c / cert_long005f tables, 5 ms, 20 dumps, 26 + 26 cases all
CONVERGED). C_F over the 12 phases, coarse / fine: Rao 1.322538 / 1.323801; the mean-state SQP (Sa10) 1.342158 /
1.343476. SQP minus Rao = +0.019620 (coarse), +0.019676 (fine): the mesh moves each number by 1.3e-3 and their
DIFFERENCE by 5.6e-5; the time uncertainty is under 1e-5. The tool's own difference is +0.020114 (1.344997 - 1.324883,
both certified). So at the design ambient the mean-state SQP beats Rao by +1.48 %, a RESULT by 400 times its
uncertainty, and the tool had it right to 2 %. Per phase (coarse, 2 ms): the SQP wins the high-pressure phases (0, 9,
10, 11: +0.035 .. +0.047) and the middle ones (+0.006 at phase 5), Rao wins the lowest one (phase 8: -0.0009); the
phases weigh equally (1/12 each).
T12.4 THE BASE (the owner: "se il vantaggio di rao sia dovuto alla pressione di base"). The tool and the headline CFD
number price the plug's cut face at the ambient. Rao's plug has the larger base (tip r 41.5 mm, 5421 mm2, against 34.9
mm, 3836 mm2) and the CFD puts a LOWER pressure on it at 0.05 bar (p_b/p_a 0.24 against 0.50 at 5 ms, coarse): its
gauge push is -0.0331 against -0.0154, so with the CFD's base the SQP's margin GROWS, +0.0196 -> +0.0373 (+2.8 %). The
common base pressure at which the two would tie is 2.5 p_a: Rao's advantage, where it appears, is not a base-pressure
artefact of the convention -- the convention favours the larger base. (An Euler base pressure is indicative: no
shear layer, no recirculation model.)
T12.5 AT 1 BAR (cert_avg1bc: 6 ms, the 2..6 ms window, coarse, one mesh; every phase unsteady; the tool cannot be
posed there and both designs are those of 0.05 bar): Rao 0.363520 +- 1.1e-3, Sa10 0.343263 +- 1.2e-3: Rao ahead by
0.0203 (5.6 %), a RESULT on one mesh; with the CFD's base Rao 0.384 against 0.337 (the base sits at the ambient,
p_b/p_a 0.99 .. 1.02: the base is not the cause here either). Phases 4..8 give NEGATIVE thrust for both (the nozzle
is drag at 1 bar in those phases, and identical between the designs to 3e-4); the whole difference is made in the
high-pressure phases (0, 1, 9, 10, 11: -0.043 .. -0.050 for the SQP). Both are under the bare exit (0.4091): at 1 bar
either plug is worse than none. So Rao's off-design advantage at 1 bar is real, made where the plug wall still runs
attached under a shock, and it says nothing about the method at its design point.
T12.6 THE PHASE-AWARE CONTESTANTS (the walks of T12.1, relaunched 03:13 with the rescue on; all their ladders certified
and in class). Progress by 05:05: from the mean-state optimum (full freedom) J12 1.344997 -> 1.345586 (segment 5,
|grad| 0.087); from Rao's plug on Rao's own freedom 1.324883 -> 1.326832 (segment 5, |grad| 0.26); at 0.2 bar from
Rao's plug 1.121759 -> 1.122714 in one segment, then stopped by the radius floor with 8 non-finite gradients of 24
(the over-expanded lip of phases 6-8 has no model), continued with the ascent probe (BcowlB_intnoz10_fromRao2_pa020).
PREVIEW by the referee (cert_prevB, coarse, 2 ms, 26 cases CONVERGED) of the segment-3 checkpoints: from the
mean-state optimum 1.342609 against Sa10's 1.342158 (+4.5e-4; the tool +2.6e-4); from Rao on Rao's freedom 1.323432
against Rao's 1.322538 (+8.9e-4; the tool +8.9e-4). The referee confirms the direction of both walks at their first
steps. The mean-state walk from Rao's plug (AcowlB_intnoz10_fromRao, three legs) reaches 1.406210 at 05:05 and still
climbs (|grad| 0.19) toward Sa10's 1.408300 (tip height 0.584 -> 0.548, Sa10 0.514): one basin so far.
T12.7 THE LANDINGS AND THE TABLE (validation/_plug_contest/41_contest_table.md + .json, built by contest_table.py from
contest_spec.json; the profiles in 41_contest_profiles_b10.png, which replaces figures 39 and 40, removed with the
uncertified batches they drew). The walks ended by their segment budgets, none at a stationary point: 12 phases, whole
plug free, from Sa10: 1.344997 -> 1.347253 (16 accepted bases, |grad|inf 0.29; design Sb10); 12 phases on Rao's own
freedom (the plug after the cowl lip) from Rao's plug: 1.324883 -> 1.331747 (14 bases, 0.40; Se10); the mean state from
Rao's plug, three legs: 1.386126 -> 1.410437 (0.20; Sm10) -- ABOVE the first landing Sa10 (1.408300), which was
therefore not an optimum; at 0.2 bar, 12 phases from Rao's plug, two legs both closed by the radius floor: 1.121759 ->
1.122869 (Sb20). THE TOOL, mean state / 12 phases at 0.05 bar, every record certified: Rao 1.386126 / 1.324883; Se10
1.393195 / 1.331747; Sa10 1.408300 / 1.344997; Sm10 1.410437 / 1.346772; Sb10 1.410940 / 1.347253. THE REFEREE at 0.05
bar (12 phases; coarse / fine; 2 ms runs for Se10, Sm10, Sb10, 5 ms for Rao and Sa10; 65 + 65 cases all CONVERGED):
Rao 1.322538 / 1.323801; Se10 1.329427 / 1.330586; Sa10 1.342158 / 1.343476; Sm10 1.343854 / 1.345199; Sb10 1.344386 /
1.345681. Against Rao (fine): Se10 +0.006785 (+0.51 %), Sa10 +0.019676 (+1.49 %), Sm10 +0.021398 (+1.62 %), Sb10
+0.021880 (+1.65 %), uncertainties 3.5e-5 .. 1.1e-4 (time + the mesh's effect on the difference): RESULTS, and the
tool's differences are the same to 2 % (+0.006864, +0.020113, +0.021888, +0.022370). Per phase the SQP wins 11 phases
of 12 (+0.003 .. +0.052) and loses the lowest-pressure one (phase 8: -0.0013).
T12.8 READ WITH SCEPTICISM. (i) THE PHASES ARE NOT WHAT WINS AT 0.05 BAR. Sb10 is ahead of Sm10 by +0.00048 under the
12 phases (CFD fine) and by +0.00052 AT THE MEAN STATE: the phase-aware design is also the better mean-state design,
i.e. the two walks climb the same hill and Sb10 is further up it. The ratio C_F(12 phases) / C_F(mean state) is 0.95487
and 0.95488 for the two (CFD fine; 0.9558 for Rao): the phases change the ranking at the 1e-5 level here, and the two
plugs differ by 0.3 mm at the tip (33.8 and 34.1 mm, Rao 41.5 mm). The gain over Rao is the posing's: the ambient, the
finite length and the truncation inside the objective, the whole plug free; a third of it (+0.51 %) is there on Rao's
own freedom. (ii) AT 0.2 BAR THE PHASES DO MATTER AND RAO IS NOT BEATEN (cert_avg020c: coarse, one mesh, 6 ms, windowed
means over 2..6 ms; 6-7 phases of 12 unsteady; FOUR cases stopped by the solver at 3.5 - 4.4 ms -- "Non-physical state
detected at the interface" / "Integration failed" in the Ambient block near the axis, at CFL 0.4 and again at 0.2 --
read on the dumps they have, post_cert --accept-early): Rao 1.129884 +- 4.4e-4; the 0.05 bar SQP design Sa10 1.121430
(-0.75 %, off design); the mean-state SQP at 0.2 bar Sr20 1.128380 (-0.0015 +- 0.0008: better at the mean state by
+0.0026 in the tool, WORSE under the phases in the tool, -0.0008, and in the CFD); the 12-phase SQP from Rao's plug Sb20
1.129797 (-0.0001 +- 0.0009: a tie; the tool +0.0011). Rao's member of this length is by its own lip condition the
optimum of 0.164 bar (T11.3): it is at its design point, and the SQP's walk there is stopped by the tool (8 non-finite
gradients of 24: no model of the over-expanded lip). (iii) THE BASE at 5 ms on both meshes (0.05 bar): p_b/p_a Rao 0.24
(coarse) / 0.34 (fine), Sa10 0.50 / 0.45; base push -0.0331 / -0.0285 against -0.0154 / -0.0167: with the CFD's base
the SQP's margin grows to +2.44 % (fine); the value is mesh-dependent, the sign is not. At 0.2 bar Rao's lead over Sa10
(0.0085) is of the size of the base terms (a common base pressure of 0.83 p_a cancels it; the CFD's own unsettled base
pressures double it); against Sr20 and Sb20 the base areas are equal and the base plays no role. (iv) THE BARE EXIT (no
nozzle, 12 phases): 1.2392 / 1.1081 / 0.4091 at 0.05 / 0.2 / 1 bar: the plugs add +6.8 % (Rao) .. +8.6 % (SQP) at 0.05
bar and +2.0 % at 0.2 bar; at 1 bar either plug is worse than none (-11 %, -16 %). (v) THE REFEREE SHARES THE TOOL'S
QUASI-STEADY PHASE MODEL: it certifies the tool's fluid dynamics, not the phase model (3D or wave-frame run: open).
T12.9 CLEANLINESS. Removed: the uncertified first batches (cowl, cowl020, cowl1b), the superseded certified ones
(cert005, cert020, cert1b, prevB: 235 stripped case folders, their tables and logs), the preview designs and meshes,
the first referee scripts (cluster_referee*, referee_cowl_*), the verdict figure's script, the walks' empty nohup
outputs, the three blocked 12-phase walks' folders. What stays per certified case: case.json, cert.json, the logs.
OPEN: converge the SQP walks (more segments; the 12-phase walk costs ~12 min per segment on one core); the angle
between the mean-state and the 12-phase gradients at one design (a direct measure of what the phases add); a second
mesh and a base model at 0.2 bar; the over-expanded lip in the tool; the angles -5 and -14 deg end to end; the 3D /
wave-frame referee.

