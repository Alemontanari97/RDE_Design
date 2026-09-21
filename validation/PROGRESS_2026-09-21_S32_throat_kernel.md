# S32 — Why the walk does not find the optimum from afar, the driver's restoration step, and the throat kernel opened on Moore 1965 (2026-09-21, [F3/A1], brick-2 plug line)

Entry point of the line: `RDE/handoff/NOZZLE_HANDOFF_2026-09-19.md`
(S31 closure, HEAD 699eace, 10 commits ahead of the remote, not
pushed). This log records the session that opened the queue's item 1
(the throat kernel) and, in parallel, the S30 queue's item 1 (the
driver's own restoration step), after the owner's two questions of the
morning: "why do we not reach the optimum from afar?" and "so we need
to handle sonic lines?".

## 1. The reading: four causes, not one (from the S31 legs, no new run)

Measured on `_humphreys_twin/run_opt_opt_2026-09-18.log` (the opt case
7.55 in / -34 deg from the fan's streamline, 30 segments x 8):

1. **J is a flat valley** (physics, not curable): the paper's own
   20-run grid lies within 0.5 percent; our fat contour (y_D 3.47 in)
   and their optimum (0.954 in) differ by 0.65 percent of thrust. The
   value does not discriminate; stationarity does (S31 §10.2: from
   their contour the walk STAYS).
2. **The driver stalls before convergence** (ours): 11 rejections in
   30 segments in the fixed cadence "one step, two rejections"
   (accepted at 0, 3, 4, 5, 10, 15, 20, 23; increments 0.20, 0.05,
   0.02, 0.03, 0.007, 0.015, 0.014 x 1e6 N); the frozen-schedule model
   says "better", the re-march says "worse", and the only answer is
   revert-and-halve (radius 0.095 -> 0.018). The walk ends by BUDGET,
   not by convergence: |grad J| 5.4e5 on J 3.95e6 at the last base
   (relative 0.14). This is the S30 queue's item 1, never done.
3. **The inlet is frozen and is not theirs**: y_w0 set by the mass
   constraint at X0 = 0.05 R, slope at the cut not a variable; a planar
   fan with the mass imposed is not their sonic throat at the lip
   (their foot 6.72 in at x -0.6 in). Even from THEIR contour the first
   knot sits +0.34 in off Table 2. From afar the walk searches a family
   that does not contain their optimum.
4. **Parametrisation and start**: 6 uniform knots with a free tip
   (bounded below by the tip floor) make a ramp, not Rao's downward
   bend (y_D 2.11 vs 1.375); Veen rewards corner compression
   (p_b ~ p_w / M^1.3) and inflates the tip at no cost in the flat
   valley; the fan's streamline start is far (-9 percent) AND in the
   wrong family (at fixed inlet the ideal member does not exist,
   -24 percent of mass).

The S31 remedy (start from their tables) bypasses 2 and 4, cures
neither. Owner's reading of the second question, "so we need to handle
sonic lines": yes for the REGION, no for the line — the sonic line as
Cauchy data is ill-posed (double characteristic, measured 2026-09-18:
cert 1e18), nobody starts there (the bell starts from Sauer, GENO from
Migdal, Humphreys from Moore-Hall). What is missing on the plug is the
kernel the bell has: the transonic field from the wall curvature,
delivering a slightly supersonic start line WITH the direction
variation across it.

## 2. The restoration step in the driver ([X-PTRN] driver, `a1_plug_spline_opt.run_trsqp`, additive, PSPL_BACKTRACK)

Patch (bit-identical for every existing caller: `backtrack = 0`
default, the record's reject-and-shrink): on a rejected trial (worse,
infeasible, OR an uncertified base — 3 of the 11 rejections of the
reference leg were "record not certified") the driver, with
`backtrack = n`, first walks BACK along the segment's displacement
d = W_trial - W_best at 1/2, 1/4, ... 1/2^n, re-marching each point
and adopting the first certified, in-class, improving one (a line
search on the true objective, the march being the model); if none,
the same halvings on a PROJECTED ASCENT step from the incumbent along
its recorded gradient (length = the radius, clipped to the bounds);
only when both fail does it revert and shrink as before. An accepted
point becomes the next base with its record CARRIED (no second march)
and the radius = the length of the accepted step. Steps below the
radius floor are not tried. The log prints the frozen model's own
prediction at the rejected trial and rho = actual/predicted. Numeric
lint: no new literal class (fractions and small integers only).

**The test (owner: "lancia il test")**: the S31 opt leg from the fan,
identical posing (HMPH_CASE=opt HMPH_START=fan PSPL_ITERS=30, base
veen, 30 x 8), with PSPL_BACKTRACK=3, on s2 (pid 37716, 02:58;
`_humphreys_twin/run_opt_opt_fan_bt3_2026-09-21.log`, result
`opt_opt_fan_veen.json`). Reference: 32,666 lbf (-0.65 percent), the
walk parked; the discriminating outcome is 32,88x (the optimum the
table-start reaches) or a stationary point. First-segment identity
with the reference (J 3.62214703e+06 at seg 0) confirms the posing.
Read while running (seg 0-8): EVERY rejection of the reference is
now converted into an accepted step — seg 1 (uncertified base) at
1/2, seg 3 at 1/4 (1/2 worse), seg 5 at 1/2 (model predicted
4.157e6, re-march 3.704e6, rho -0.34), seg 7 at 1/2 (rho -0.05);
J 3.622 -> 3.776 -> 3.819 -> 3.850 -> 3.863 (x1e6) by seg 8 with
|grad| 7.6e5 (the reference had 3.888 at seg 5 and 2.6e6). The frozen
model's gain is a fantasy beyond half the step: rho < 0 on every
rejected trial. The closure of the leg is in §6: 32,820 lbf (-0.19 percent), 11/11 rejections converted.

An aborted first launch (`..._aborted_v1.log`, 4 segments) ran the
patch WITHOUT the uncertified-base branch; discarded, bit-identical
to the reference up to its abort.

## 3. The sources for the kernel (reading of record)

- **Humphreys 1971 p. 1587, "Importance of start line"** (re-read for
  this brick; the S30 reading recorded the 2-lbf agreement, not the
  mechanism): Rao's straight sonic line with UNIFORM direction gives
  compression — subsonic Mach in the throat — unless M >= 1.5 on it;
  a LINEAR 6 deg decrease of the direction along the line (E -56 deg
  to A -62 deg) cures the compression, reproduces Rao's contour
  "reasonably well" and leaves the thrust 2700 lbf (8 percent) LOW; a
  right-running characteristic from Rao's transonic field as the
  start line gives Rao's contour and 34,373 against 34,375 lbf. Their
  own start line is a "modified Moore-Hall" (Ref. 8 = the first
  author's thesis; Moore & Hall, ARC 26-543, 1965, "Transonic flow in
  the throat region of an annular nozzle with an arbitrary smooth
  profile"). Their Fig. 1: the start line AE from the plug (A) to the
  cowl lip (E), T downstream of A. READ: the uniform tilted line
  (Migdal, GENO's annular start, the queue's own first idea) is NOT a
  start line at the 1 percent level; the direction variation across
  the throat is the physics, and it is what a transonic kernel gives.
- **Moore, A. W., ARC R&M 3481 (1965/1967)**, "The transonic flow in
  the throat region of a two-dimensional nozzle with walls of
  arbitrary smooth profile", in hand (Cranfield AERADE, handle
  1826.2/4059, 28 pp; page 5 of the scan — definitions (2.6)-(2.15)
  — is BLANK in the archive copy, content-stream error): Hall's
  successive approximation generalised to walls of different
  curvature; series in eps = R^(-1/2), R the mean radius in
  half-heights, K the asymmetry ((h''-j'')/(h''+j''), reconstructed
  from the wall conditions and confirmed by §4.3 where a straight wall
  gives K = 1); first three terms; sonic line and branch line
  (4.4)-(4.5); mass defect (4.6); §4.3 the choked wind tunnel = one
  wall straight. READ-INTEGRAL for §§1-4; §5 (inverse problem) read
  for structure only.
- **NOT in hand** (paywall/DTIC unreachable 2026-09-21): Moore & Hall
  ARC 26-543 (the annular sequel, Humphreys' start line); Dutton &
  Addy, AIAA J. 20(9) 1236-1243, 1982, "Transonic flow in the throat
  region of annular supersonic nozzles" (the general
  axisymmetric/planar/annular series with measurements on three
  annular nozzles; DTIC ADA084787 = Dutton's report). REQUEST TO THE
  OWNER: the AIAA PDF (10.2514/3.7973) through the institutional
  access; it is the axisymmetric completion of what is transcribed.
- Migdal 1972 (in hand): design method, uniform inclined start line —
  a declared datum, not a throat solution; not a source for this
  brick beyond the frame.
- Zucrow & Hoffman vol. 2: scanned without text; §15 transonic
  (Sauer, Hall, Kliegel-Levine) not re-read.

## 4. `validation/a1_throat_kernel.py` — Moore transcribed and VERIFIED (stage verify 7/7, 5.1 s)

Transcribed: u1, v1 (2.32)-(2.33); u3 = u3s + u3K, v3 = v3s + v3K
(2.36), l3 = m3 = l4 = m4 = 0 (parabolic walls: circular, hyperbolic
and parabolic arcs are equivalent unless O(R^-3) is kept, the paper's
own statement); the isobars/sonic line (4.4); the mass defect (4.6).

**The paper is its own rejector.** Symbolically (sympy, exact
rationals, system python; the pinned venv has no sympy): the residuals
of irrotationality (2.23) and continuity (2.24)/(2.25) with Phi_2 —
Phi_2 RE-DERIVED from (2.17) at O(eps^5): 2 v1 u1_y + (gamma-1) u1 v1_y
+ u1^2 u1_z / 2, agreeing with the print up to the irrotationality
identity u1_y = v1_z — the wall conditions (2.30)-(2.31), and the
sonic-line formula (4.4) to O(eps^4) are IDENTICALLY ZERO once ONE
misprint of the scan is corrected: v3K's z-linear constant reads
(2 gamma+8)/8 in the image and must be (2 gamma+8)/3 (irrotationality
fails by K (5 gamma/12 + 5/3) otherwise). Numerically in the venv
(jax derivatives, stage verify):

| gate | result |
|---|---|
| T-1 (2.23)-(2.24) first order, 64 random (y, z, K) | 2.2e-16 |
| T-1 (2.23), (2.25)+Phi_2 third order | 2.7e-15 |
| T-2 wall conditions at both walls | 1.1e-15 |
| T-3 (4.4) is the sonic line to O(eps^4): observed order on the 0.1/0.2/0.4 ladder | 3.95/3.81 (K 0), 3.87/3.59 (K 0.5), 3.81/3.45 (K 1) |
| T-4 mass defect (4.6) by Simpson quadrature at z = 0 | rel gap 2.9e-5 .. 9.2e-3 at eps 0.1/0.2 |
| T-5 K = 0 first order = the record's Sauer (delta 0) shifted by 1/6: sonic z = 1/6 - y^2/2, v = 0 on z = 1/6 - y^2/6 | 6e-11, 2e-26 |
| T-6 K = 1 (straight lower wall): sonic points z = -4/3 (curved) and +2/3 (straight), singular point on the straight wall | exact |

T-5 is the known answer against an INDEPENDENT source already in the
record (a1_thrust_functional.ivl_flux: alpha, c1, c2 of Sauer with
delta): Moore's first approximation at K = 0 IS Sauer planar, the
origin moved from the axis sonic point to the throat plane (1/6).

**The reading for the posing (K = 1: curved plug wall, straight
cowl — the plug throat's planar limit), gamma 1.4:**

| R (mean, half-heights) | sonic line x (half-heights) | theta on the sonic line | M on the first all-supersonic z = const line | 1 - W/W* |
|---|---|---|---|---|
| 5 | -0.53 .. +0.34 | -13.6 .. +0.2 deg | 1.000 .. 1.453 | 5.5e-3 |
| 10 | -0.48 .. +0.29 | -5.7 .. 0.0 deg | 1.000 .. 1.239 | 2.6e-3 |
| 20 | -0.39 .. +0.22 | -2.3 .. 0.0 deg | 1.000 .. 1.120 | 8.4e-4 |

Three facts the posing must carry: (i) the sonic line is TILTED
across the throat — sonic on the curved (plug) wall 0.4-0.5
half-heights UPSTREAM of the throat plane, on the straight (cowl)
wall 0.2-0.3 DOWNSTREAM, the singular point ON the straight wall;
(ii) the direction varies by 2-14 deg across it (Humphreys' "6 deg"
is R ~ 10); (iii) a transverse line at the downstream sonic point is
M 1.00 at the cowl and 1.12-1.45 at the plug — NOT a uniform line at
any M_i, and the M-1 point is the cowl side, i.e. the lip side.

## 5. The posing of the brick (proposal, owner's call on the frame and on the lip)

**Object.** The transonic field in the throat between the plug wall
and the cowl, computed from the two wall curvatures at the throat ON
the contour (the plug's foot curvature becomes a design quantity),
delivering (a) the mass flow (no longer imposed through y_w0), (b) a
start line downstream of the sonic line, slightly supersonic
everywhere, with q(y) and theta(y) from the kernel, (c) the state at
the cowl lip for the lip fan.

**Frame.** Moore's frame is the throat's own: x along the mean flow
direction at the throat (tilted by theta_t = nu(M_e) in Angelino's
posing, by theta_i in Humphreys'), y across, half-height = unit. The
kernel is evaluated there; the hand-over to the record's x-march
(a1_plug_march, Cauchy data on a transverse line) is a ROTATION of
the start line's points and angles into the record's frame — no
rotated-frame CELL is needed for the kernel itself. The near-vertical
characteristics of S31 §3.3 (rays with theta - mu < -90 deg in the
record's frame, M < 1.47 at a sonic lip) are the region BETWEEN the
kernel's start line and the first transverse line on which every
characteristic points downstream in x: that region is marched in the
THROAT frame (where the flow is nearly axial and the record's cells
certify — planar 0.07) and only then rotated. This is the "frame
ruotato" of the queue, applied to a strip, not to the cells.

**The lip.** Moore's walls are smooth; the cowl ENDS at the lip. Two
posings, to be decided by a measurement, not by preference:
(L-a) the cowl is straight up to the lip and the lip sits at the
throat plane (Angelino/Chutkey): Moore's field is then subsonic at
the lip (the straight wall's sonic point is 0.2-0.3 half-heights
downstream) and the corner accelerates the flow to sonic AT the lip —
the smooth solution is modified in a neighbourhood of the lip whose
size is the question (Humphreys' "modification" of Moore-Hall, Ref.
8, unread). (L-b) the cowl is a smooth wall through the throat and the
lip lies downstream at M_lip > 1 (Humphreys' Fig. 1, GenoPlug's
internal-external posing): Moore applies up to the lip unmodified and
the lip fan starts from the kernel's own state there. THE MEASUREMENT:
Chutkey's twin (X-CHTW) has the contour, the measured wall state, and
a -6.2 percent mass defect attributed to the cut data: run the
kernel's start line at K = 1 on Chutkey's foot curvature (planar
limit first, the annular terms being the gap) and read whether the
first-column mass closes; Humphreys' Rao case has the 34,373-lbf
exhibit as the oracle of the start line.

**The gap declared.** Planar only. The annular (axisymmetric) terms
are Moore-Hall / Dutton-Addy, not in hand: on Chutkey (throat height
2.647 mm at radius ~30 mm, h/r ~ 0.09) and on Humphreys (throat
height ~1 in at radius 7.5 in, 0.13) the curvature-of-revolution
correction is of that order relative — small against the 6 percent of
the mass defect, not against the 1 percent of thrust. Their
acquisition is the owner's request above; failing it, the annular
correction can be built by the same successive approximation on the
axisymmetric equations (Hall 1962 for the symmetric case is the
pattern) — a brick of its own, sized after the planar kernel is read
on Chutkey.

**Order of work (proposal):**
1. `a1_throat_kernel.py` stage `startline`: given (c_h, c_j, gamma,
   z_line), the start line's (x, y, q, theta) in the throat frame,
   its mass, and its rotation into the record's frame; gate: mass on
   the line = W of (4.6) x W* (self-consistency), every point M > 1,
   theta - mu monotone along the line.
2. Chutkey: the kernel on the foot curvature of the smoothing spline
   (K = 1, the cowl straight — L-a — as the first measurement), the
   march from the kernel's line in the throat frame to the first
   downstream-pointing transverse line, hand-over to plug_march;
   gate: the first-column mass closes (the -6.2 percent) and T-5/T-6
   hold.
3. Humphreys' Rao case: the same, oracle 34,373 lbf and Table 3.
4. Only then the optimiser: y_w0 and the foot curvature as design
   variables, the mass an output — the inlet unfrozen (cause 3 of §1).

## 6. The leg's closure (03:26, 1678 s, 30 segments, 2/2)

| | reference S31 (reject-and-shrink) | S32 (backtrack 3) |
|---|---|---|
| rejections / converted | 11 / 0 | 11 / **11** (14 probes, 0 on the ascent) |
| records (segment marches) | 30 | 19 (+14 probes) |
| wall time | 2032 s | 1678 s |
| J final (x1e6 N) | 3.95108 | **3.96979** (+0.47 %) |
| thrust | 32,666 lbf (-0.65 %) | **32,820 lbf (-0.19 %)** of 32,881 |
| |grad J| at the last base | 5.4e5 | 3.2e5 (1.1e5 at seg 26) |
| cert | 0.522 | 0.198 |
| y_D | 3.47 in | 2.72 in (paper 0.954) |

READ. (i) The driver's defect is cured: every rejected segment of the
reference now yields an accepted step, always along the segment
(1/2 in nine cases, 1/4 in two: the frozen-schedule model is good to
about half its step), the ascent fallback never needed; the walk is
cheaper (fewer segment marches, the probes being marches without the
8 trust-constr iterations) and lands 0.47 percent higher. (ii) The
walk is STILL not at their optimum: 0.19 percent below, |grad| 3e5
(relative 0.08), the tip at 2.72 in against 0.954 — the flat valley
and the free tip (causes 1 and 4 of section 1) remain, and the
inlet (cause 3). The driver alone takes the fan-start walk from
"parked 0.6 percent low" to "0.2 percent low and still climbing":
the remaining gap is the parametrisation/inlet brick, not the
driver. (iii) Radius policy observed: the accepted step becomes the
radius (0.354 after seg 1 — larger than the 0.25 growth cap of the
record — then self-corrected to 0.088 at seg 3 by the next
backtrack); a cap at 0.25 would be consistent with the growth rule
and is left as a one-line option, not applied (the leg of record ran
without it).

Artefacts: `_humphreys_twin/run_opt_opt_fan_bt3_2026-09-21.log`,
`opt_opt_fan_veen.json` (not committed, as the S31 artefacts).

## 7. Conformity

- Branch `rde-nozzle-program`; identity AlexFalco5; no push.
- Files: `validation/a1_plug_spline_opt.py` (driver, additive knob),
  `validation/a1_throat_kernel.py` (new carrier, baseline row 65 in
  `numeric_lint_baseline_validation.json`, measured by the lint),
  this log; registry row X-TKRN; ADVISORY_INDEX row; living PROGRESS
  parallel-line block.
- Not committed: `_humphreys_twin/*.log|json` of the leg (artefacts,
  as the S31 ones), the aborted v1 log.
- Lints 3/3 after the two-step commit (log first, registry row second — the claims lint's pass= rule); full suite 14/23 before the commit = the seven S26 reds + (xv)/(xvii) on the uncommitted X-TKRN doc, expected to return to 16/23 once the log has history; data/q_mapping.*, data/phase_diagram.*, figs/phase_diagram_op11.png restored with git checkout.
