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

## 8. The frame march, and the strip from the throat on Chutkey (afternoon; owner: "continua")

**The rotated-frame cells [X-FRMR], `validation/a1_frame_march.py`,
stage frame 4/4 (86 s).** The record's three plug-march cells
(interior bottom-up, bottom wall, free jet) with the ONE frame-bound
term rewritten: the axisymmetric source delta c^2 v / y becomes
delta c^2 v_r / r, v_r = u sin theta_t + v cos theta_t, r = Y_0 +
x sin theta_t + y cos theta_t; threaded through `plug_march(cells=)`
(the S24 swirl seam). The compatibility rows are divided by q_m^3
(root unchanged; A1's damped Newton reads the residual NORM for its
step acceptance, and with the geometric row at 1e-2 and the
compatibility row at 1e6 the wall cell at station 79 of the rotated
Chutkey case, r 0.015 R, accepted a half step and stalled at metric
3.7 while the record's cell at the same physical point converged;
scaled, 3e-14). The A/B on the S31 twin's case ((81,41), the
fan_axi cut at 1.5 mm) with the SAME wall points in both frames:

| gate | result |
|---|---|
| F-0 theta = 0: the wall array equals the record's | 2.9e-15 relative (certification class 8.6e-11), both certified |
| F-1 the throat-frame march (theta_t -56.9 deg) certifies | 0.194 (3862 cells) |
| F-2 wall p vs the record's on the arc, inside the (81,41)->(161,81) band | 81/81; **max |dp|/p_0 1.7e-5** (band 7e-2) |
| F-3 the source is alive: the record's cells in the rotated frame (y' as the radius) | +0.95 of p_0 off, cert 6e16 |

The discrete march is frame-covariant to 1.7e-5 of p_0 (the residual
is the foot-bracket heuristic, which reads the previous wall's u in
the frame). The X0 ladder of the twin extended toward the throat in
both frames (81,41): 1.5 / 1.25 / 1.0 / 0.8 mm -- identical readings
in the two frames at every rung; the record frame does NOT fail down
to 0.8 mm (theta - mu at the wall -77..-83 deg, still downstream);
p_w/p_0 at 20 percent 0.04259 / 0.04271 / 0.04288 / 0.04351, the last
rung with the cut's wall point ON the fan's leading ray (declared
limit of the M_i-1.6 fan). Noted on the side: the cut of record
carries 0.875 of the CHOKED mass at (81,41) -- the twin's mass rows
are relative to the cut, not to the throat.

**The strip from the throat line on Chutkey: NEGATIVE, measured.**
Stage strip: a uniform line at M_i on the throat line, tilted by
nu(M_i) so the lip fan (the record's planar corner wave) ends axial,
the cut at d half-heights, the wall clustered from 0.05 h, the march
in the throat frame with the rotated cells. Every configuration fails
at the wall cells within 0.7 mm of the foot and the mesh folds
downstream:

| M_i | d | wall | cert (where) | mass mid / last vs cut |
|---|---|---|---|---|
| 1.02 | 0.1 | digitised | 5e14 (wall 2) | -2.9 % / -0.4 % (ran through; p_w +14..+25 %) |
| 1.05 | 0.1 | digitised | 1e15 (int 17,14) | +144 % / +294 % |
| 1.10 | 0.1 | digitised | 3e23 (int 119,135) | garbage |
| 1.20 | 0.1 | digitised | 3e15 (int 11,3) | +213 % / +368 % |
| 1.05 | 0.1 | Angelino foot | 4e15 (wall 10) | +478 % / +950 % |
| 1.10 | 0.1 | Angelino foot | 1e13 (wall 7) | +280 % / +614 % |
| 1.05 | 0.5 | Angelino foot | 5e12 (wall 1) | +441 % / +969 % |

Two obstacles, both measured: (i) **the digitised contour's foot is
noise at the 0.1-mm scale**: the raw chords from the foot read -52,
-56, -50, -47, -62, -40 deg (0.12 mm of noise on 0.5-mm chords) and
the clamped smoothing spline turns 5.1 deg within 0.2 mm of the foot
(the ideal wall turns 10 deg over ~2.4 mm); the record never marched
that region (its cut is at 1.5 mm). Replacing the first 3 mm by the
design rule itself -- the planar sonic-lip fan's streamline from the
foot (`FRM_WALL=angelino`, ramped into the digitisation over 1 mm) --
removes the artefact and does not cure the march. (ii) **The
near-sonic wall cells**: at M 1.02-1.2 (mu 57-79 deg) with the
corner fan 0.1-0.5 h away, the wall cell's foot search and the
damped Newton fail within the first ten stations in the throat frame
too -- the S31 section 3.3 conditioning limit, now measured in the
frame where no characteristic passes the vertical. The record's
construction marches because it starts at wall M 1.72.

**And the kernel on Chutkey is excluded by the paper itself**:
Chutkey p. 479 defines the primary nozzle as a SYMMETRIC convergent
duct about the tilted axis whose walls end in circular arcs of radius
0.867 mm at the throat, on a half-height of 1.32 mm: R/h = 0.66,
eps = 1.24 -- outside Moore's series ("neither of the walls may have
a small radius of curvature"), outside every throat series
(Kliegel-Levine's small-radius expansion reaches R ~ 0.5 with poor
accuracy, axisymmetric symmetric throats only). The throat is K = 0
(symmetric) upstream and a corner + curvature jump downstream (the
paper's CFD sees "a mild compression wave at the intersection of the
primary nozzle and the plug contour"). The transonic field of this
throat is a numerical problem, not a series.

**Read for the posing (section 5 revised).** The kernel brick as
posed applies to smooth throats with R/h >~ 3 (eps <= 0.6): Humphreys'
(radius unknown, thesis) possibly, Chutkey's not. On Chutkey the
declared strip is the record's 1.5-mm cut on the ideal fan; its
ladder to 1.0 mm moves the 20-percent reading by +0.7 percent and
the mass reference is the cut's 0.875 W*. What would close Chutkey's
throat is a numerical transonic solution of the primary nozzle (not
in the toolset) or the paper's own CFD sonic line (Fig. 7-8, not
digitised). The frame march stands as an asset for any start line at
M_w >~ 1.5 in a tilted throat.

## 9. Dutton & Addy 1982 in hand (owner, 14:19), Lord 1959 fetched; the sources re-read for EXPLICIT geometry

Filed at `RDE/codes/GENO/literature/dutton1982.pdf` (moved from the
repo root) and `lord1959_rm3227.pdf` (AERADE handle 1826.2/3800).
Moore & Hall is ARC **R&M 3480** (Dutton's ref. 3), NOT in the AERADE
catalogue (only 3481 is); Dutton's report with the coefficients is
UILU-ENG-80-4001 = DTIC ADA084787, unreachable from here.

**Dutton & Addy, read-integral.** THE FRAME IS OURS: Fig. 1, the x-y
system rotated by the inclination beta with y along the minimum-area
cross section, lengths in the throat separation d, the gas-dynamic
equation (11) with the axisymmetric term [v + (1+u) tan beta] /
(y + x tan beta) -- exactly the rotated cells' v_r / r of section 8.
Expansion parameter eps = (R_c + eta)^(-1), eta free (Kliegel-Levine's
device), R_c = 2 / (h'' - g'') the mean dimensionless radius;
z = ((gamma+1)/2)^(-1/2) eps^(-1/2) x; the series (20)-(21) to third
order with the annular term (beta_1 + v_1)/y at FIRST order, eq. (23),
tan beta / y assumed small (throats far from the axis: Chutkey y_i =
R_i/d = 11.5, tan beta 1.53 -> 0.13). Boundary conditions (25)-(30)
on both walls in Maclaurin form. THE COEFFICIENTS ARE NOT IN THE
PAPER ("too long to be included", ref. 19, the TRANNOZ program):
what is in hand is the complete framework and its reductions
(Hall/Kliegel-Levine at y_i -> 0, Thompson & Flack planar at y_i ->
inf). WHAT IT SETTLES FOR US: (i) the small-radius regime IS covered
-- Fig. 2-3 and 7: the conventional axisymmetric nozzle with R_co =
0.625 and 1.0, the series at eta = 2 "well-behaved" and matching the
measured Mach contours; Chutkey's R/h = 0.66 (section 8) is inside
this regime, i.e. the throat kernel on Chutkey is NOT excluded by the
method, only by the coefficients we do not have; (ii) measured
throat fields with EXPLICIT geometry -- four configurations (Fig.
4-10): axisymmetric R_co = 1.0; annular R_ci 3.2 / R_co 1.6 / y_i
0.6 / beta 0; the same centerbody shifted to beta = +0.095 and -0.095
rad (R_ci 3.01, R_co 1.50, y_i 0.51), Mach contours 0.6-1.4 from 67-79
splitter-plate taps at +-1.5 kPa (+-1.3 percent in M at 0.6): the
twin for ANY throat kernel, ours included, before Chutkey or
Humphreys; (iii) the minimum-area cross section and the
minimum-distance section do not coincide for an inclined annular
throat (Fig. 9-10) -- our "throat line" from the lip to the foot is
the latter.

**Lord 1959 (R&M 3227), read for structure**: annular nozzles with a
coaxial CYLINDER (inner wall straight), the throat region as a series
near the sonic point on the cylinder to second order (section 3) --
the limit R_ci -> inf, beta = 0 of Dutton's family; a check for the
annular terms once derived.

**Humphreys 1971, the theory (pp. 1581-1583, re-read on the owner's
remark)**: the variational problem for the AXISYMMETRIC plug with
fixed inlet -- functional (6)-(11) with the multipliers lambda_1..4,
Euler equations (13)-(14), compatibility along the characteristics
(15), transversality along TD (17)-(19), along the exit
characteristic DB (20), corner conditions at D (21)-(22), and Rao's
conditions (25)-(27) recovered as the fixed-length special case with
lambda_1 = eta rho V sin theta, lambda_2 = lambda_3 = V cos theta.
The base enters as Phi = (eta_D - delta'_D)^2 p_b / 2 with p_b a
constant during each iteration (recalculated between iterations).
Our M0 carries the same necessary conditions in the record's own
form; the cross-check of (20) and (27) against the plug adjoint is a
reading item, not a brick.

**READ FOR THE DIRECTION (owner: "reference con geometria
esplicitata")**: the explicit-geometry references are Chutkey's
primary nozzle (lines + arcs, p. 479, R/h 0.66) and Dutton's four
throats (radii, y_i, beta, with measured fields). A kernel that serves
them is Dutton's annular series in OUR frame -- the framework is
complete in the paper; the third-order coefficients are either
ADA084787 (owner's fetch) or a derivation of our own by the same
successive approximation (the Moore transcription's sympy path,
extended to the annular source term: the assumed forms are
polynomial in z with y-dependence fixed by the 1/y term), gated on
Dutton's own reductions (Hall at y_i -> 0, Moore/Thompson-Flack
planar at y_i -> inf) and on his measured contours. Gate order:
Dutton's axisymmetric R_co 1.0 (Fig. 6-7) -> annular beta 0 (Fig. 8)
-> inclined (Fig. 9-10) -> Chutkey's primary nozzle -> the plug.

## 10. The annular kernel DERIVED (evening; owner: the report is not obtainable) [X-ANKR], `validation/a1_annular_kernel.py`, stage verify 4/4

Dutton & Addy's series in our own hands: the framework of the paper
(eqs. (10)-(11), scalings (16)-(21), wall conditions (25)-(30)) and
the coefficients derived, not transcribed.

**The forcing terms.** Eq. (11) expanded in eps with sympy (system
python; `validation/_annular_kernel/derive_fn_sympy.py.txt`): at order n,
u_n,y = v_n,z and -2 u_1 u_n,z - 2 u_1,z u_n + v_n,y + v_n/y = f_n,
with f_1 = -beta_1/y (eq. (23) reproduced verbatim), f_2 and f_3 the
lower-order products (coded in `_f2`, `_f3`; f_3 carries the terms
of the (y + x tan beta) denominator, beta_1^2 z/(2y^2) and beta_1 z
v_1/(2y^2), and of the a^2/a*^2 factor).

**The solution.** First order: the z^2 wall condition forces the
z-coefficient of u_1 to be a constant D, so u_1 = D z + a(y) with
a' = D^2 y + C_1/y -- the annular constant C_1 brings the logarithms
-- and D^2, C_1 follow from the two wall values of v_1's z-coefficient
(D^2 = 2 on the axis: Sauer; 1 in the planar limit: Moore); v_1 = z a'
+ c(y), (y c)' = 2 y a D - beta_1. Every higher order is linear and
TRIANGULAR: u_n = sum z^k A_k(y), v_n = sum z^k B_k(y), (y B_k)' =
y [F_k + 2D(k+1) A_k + 2a(k+1) A_{k+1}], A_k' = (k+1) B_{k+1}, from the
top degree down, each (A_k, B_k) pair of constants fixed by the two
wall values of B_k: a chain of quadratures. The y-dependence lives on
a Chebyshev-Lobatto grid (48 nodes) with spectral differentiation and
integration: exact in z, spectral in y, no closed-form explosion.

**The gates (all derived, all rejectors):**

| gate | result |
|---|---|
| V-1 residual of the FULL eq. (11) (jax) on the truncated series, eps 0.04/0.02/0.01, generic annular inclined asymmetric throat (y_i 0.6, g_2 -0.6, h_2 1.4, g_1 0.1, h_1 -0.05, beta_1 0.3, eta 2) | observed orders 1.02/1.01, 2.05/2.02, **3.06/3.03** with 1/2/3 terms |
| V-2 the wall conditions (12)-(13) on both parabolic walls | orders 1.06/1.03, 2.05/2.03, **3.05/3.02** |
| irrotationality (10) | 5e-15 |
| V-3 axis limit y_i = 1e-3, first order = the record's Sauer (delta 1) | D^2 = 2 - 2e-3 (= 2/(1 + y_i/y_o)), C_1 -2e-6, sonic-line shape 7.5e-5 |
| V-4 planar limit y_i = 1000: the 2-term series vs Moore's third approximation [X-TKRN] (eps_M^2 = eps/2, x_M = 2 x_D), K_M 0/0.5/1 | gap 4e-6/8e-6/1.3e-5 at eps 0.05 = the annular O(1/y_i) term: **ratio 4.00** under y_i x 4 |
| V-5 Chebyshev N 48 vs 96 | 2e-12 |

Two readings from the gates: (i) Moore's third approximation is
Dutton's SECOND term (eps_M^4 = eps^2/4); Dutton's third term is
Moore's unpublished fifth -- the 3-term series against Moore differed
by eps^3 u_3 before this was understood; (ii) the annular correction
at first order is C_1 ln y with C_1 = O(y_i^2) cancelling against
D^2 y^2/2: at y_i 1000 six digits cancel and the Chebyshev sums keep
1e-10 (Dutton's footnote on his roundoff at y_i ~ 1000 is the same
cancellation).

**What this gives the line.** A throat kernel for ANY annular,
inclined, asymmetric throat with parabolic walls, in the frame of the
rotated cells (section 8): Chutkey's primary nozzle (arcs R 0.867 mm
on d 2.647 mm: R_c = 0.33 in separations, eta 2 -> eps 0.43, y_i 11.5,
beta_1 = tan(56.9 deg)/(K eps^1.5) = 5.0, beta_1/y_i 0.43), Dutton's
four measured throats, Humphreys' annular throat when its radii are
known. NEXT (proposal): stage `dutton` -- the axisymmetric R_co 1.0
wall Mach (Fig. 6) and the annular/inclined contours (Fig. 8-10) as
the measured oracle (digitisation by the owner, as for Chutkey's
Fig. 2b); stage `chutkey` -- the sonic line and the throat-plane
profile of the primary nozzle, the discharge coefficient, and the
1/2/3-term convergence at R_c 0.33 (the paper's Fig. 2-3 pattern);
then the start line for the frame march at the first all-supersonic
transverse line, and the twin's mass.

### 10.1 Stage chutkey (1/2) and stage domain (1/1): where the series converges

Chutkey's primary nozzle in the kernel's parameters: d 2.647 mm, beta
56.9 deg, both walls arcs R 0.867 mm -> R_c 0.3275 (separations),
y_i = R_i/(d cos beta) = 21.1, beta_1 4.97 (beta_1/y_i 0.24), g_2 -1,
h_2 +1, eta 2 -> eps 0.430. The 1/2/3-term series on the throat plane
x = 0: M 1.016-1.153 / 0.961-1.206 / 0.935-1.265, direction +-0.5 /
+-1.3 / +-2.0 deg, W/W* 0.9959 / 0.9950 / 0.9924; the sonic line at
the walls -0.21 / -0.18 / -0.19 d (0.5 mm upstream), at mid-throat
-0.02 / +0.04 / +0.06 d. **C-1 FAILS, and that is the finding**: the
third term moves the throat-plane Mach as much as the second (0.058
vs 0.055, ratio 1.05) and eta 1/3 vs 2 move it by 0.12 -- at R_c 0.33
the series is NOT converged, as Dutton's own domain says (R_c >= 0.5).
What is bounded: the discharge coefficient W/W* = 0.985-0.995 across
eta 1-3; the sonic line's shape (walls 0.5 mm upstream, mid-throat
~0.15 mm downstream); the first all-supersonic transverse line
+0.16 mm from the throat plane with M 1.00-1.37 and +-3.5 deg of
direction. C-2 PASS (W/W* 0.9924 in [0.95, 1]).

Stage domain, the convergence map on Chutkey's annulus (y_i 21,
beta 56.9) and on the axis, symmetric walls, eta 2, the throat-plane
Mach: ratio |M_3 - M_2| / |M_2 - M_1| = 1.05 / 0.91 / 0.83 / 0.63 /
0.35 / 0.16 at R_c 0.33 / 0.5 / 0.625 / 1 / 2 / 4 on the annulus
(0.93 / 0.86 / 0.82 / 0.71 / 0.52 / 0.35 on the axis), eta-spread
0.12 / 0.08 / 0.06 / 0.03 / 0.008 / 0.002 (0.21 / 0.14 / 0.10 / 0.05 /
0.012 / 0.003); W/W* on the axis 0.980 / 0.984 / 0.987 / 0.991 /
0.9965 / 0.9988 (R_c 2: 0.9965; the measured discharge coefficients of
Back et al. for R_c ~ 2 are ~0.996). D-1 PASS: converged at R_c >= 1
on both; marginal at 0.5-0.625 (Dutton's edge); not at 0.33.

**Read for the direction.** The kernel is validated and its domain
is measured: R_c >= 1 clean, >= 0.5 marginal. Dutton's four throats
(R_co 1.0; R_ci 3.2 / R_co 1.6; R_ci 3.0 / R_co 1.5 inclined) are all
inside -- the oracle with explicit geometry AND measured fields is
exactly where the kernel works. Chutkey's throat (R_c 0.33) is outside
by design of his rig; its throat field remains a numerical problem,
but its discharge coefficient and sonic-line shape are bounded by the
kernel at the 1 percent / 0.1 mm level. Humphreys' throat radius is
the unknown that decides his case.

### 10.2 Stage dutton 8/8: the kernel against Dutton & Addy's own series and their measured throats (the owner's digitisation, 16:00-16:30)

Data: `validation/dutton1982_digitised/` (34 files from the owner's
GENO/literature/DuttonF6, F8, F9, F10; the number format
normalised; `fig8_series_m0.6.csv` was a duplicate of the 0.8 curve
and is dropped). Parameters from the captions, in the kernel's own
units (the wall separation d): Fig. 6 axisymmetric R_co 1.0, eta 2
(R_c 2, eps 0.25); Fig. 8 annular R_ci 3.2 / R_co 1.6 / y_i 0.6 /
beta 0 (R_c 2.13, eps 0.242; the digitised outer arc fits radius
1.007 in figure units = 1/0.625 = 1.6 d, the centerbody 2.0 = 3.2 d:
the captions' radii ARE in d); Fig. 9/10 R_ci 3.01 / R_co 1.50 /
y_i 0.51 / beta +-0.095 rad (R_c 2.00, eps 0.25, beta_1 +-0.70).
Figure units -> frame: d = 1/R_co(fig); Z* the frame origin on the
axis: 0 for beta = 0 (the R axis through the outer centre of
curvature, p. 1240), for the inclined cases posed from the outer foot
(sin beta (1 + d y_o) = +-0.190) and REGISTERED on their series
(one parameter, as Chutkey's X_SHIFT): +0.228 / -0.220.

| figure | ours vs THEIR series | ours vs the MEASURED field (throat region Z >= -0.25) |
|---|---|---|
| 6, wall Mach vs Z (32 pts) | rms 0.021, 32/32 inside the digitisation band; **their "wall" Mach is the series read at y = y_o**, not on the arc (on the arc ours diverges beyond z ~ 0.5: 2.96 vs 2.19 at Z 0.45; at y_o 2.119 vs their 2.185) | 7 pts rms 0.050, their own series 0.065 on the same data (the inlet cone upstream of Z -0.3) |
| 8, contours M 0.8-1.4 (51 pts) | **rms 0.006**, max 0.021, 51/51 in band | 24 pts: bias +0.022, de-biased rms 0.011 |
| 9, M 0.6-1.4 (61 pts) | rms 0.012 after registration (0.044 posed), 61/61 | 27 pts: bias +0.017, de-biased rms 0.026 |
| 10, M 0.6-1.2 (60 pts) | rms 0.013 (0.034 posed), 60/60 | 17 pts: bias +0.033, de-biased rms 0.014 |

READ. (i) The derived kernel IS Dutton & Addy's third-order series:
on the interior iso-Mach points of the beta = 0 annular case the two
agree to 0.006 rms in Mach (the digitisation class is 0.06), on the
inclined cases to 0.012 once the figure's origin is registered, on
the wall of the axisymmetric case to 0.021 -- the annular term, the
inclination term beta_1 and the eta re-summation all reproduced;
the coefficients "too long to be included" are recovered. (ii) The
measured fields: the data lie 0.02-0.03 in Mach downstream of the
inviscid series on every configuration -- the bias the paper itself
reports and attributes to wall friction shifting the sonic line
downstream (p. 1242) -- and about that bias the scatter is 1.1-2.6
percent rms, inside the measurement class (their +-1.3 percent at
M 0.6, +-0.6 at 1.4, plus the digitisation). (iii) A subtlety of
record: the series' wall values are its values at the throat radius
y_o (the wall conditions hold there in Taylor form); read on the
actual arc at |z| > 0.5 the series diverges. A start line for the
march must therefore be taken at |z| <= 0.5 and its wall point read
at y_o with the wall's own slope, or the wall's excursion x^2/(2R_c)
kept below the series' reach. Gates F6-1/2, FIG8/9/10-1/2 all PASS.

## 11. The kernel-fed march (night; owner: "vai"): the line is sound, the corner is the missing brick

`a1_frame_march.py` stage kernel (L-b posing on Chutkey's plug with
the Angelino foot; the plug-wall throat radius POSED 1.5 d -- the
Angelino wall leaves the foot with 1/181 d of curvature, and with it
the kernel's transonic length vanishes and the inclination term's
axial-flow branch takes over (M ~ 2 on the line: measured) -- cowl
straight, R_c 3, eps 0.20, y_i 21.1, beta_1 15.7; the cut at z 0.5 =
0.65 mm from the throat plane, the lip 0.13 mm upstream on the cowl).
THE LINE: M 1.11 at the cowl to 1.55 at the plug, direction -7.4 to
0 deg, the kernel's mass through the section 0.954 of the choked 1-D
(the start line's, wall to edge, 0.937) -- the transonic start the
twin never had, converged (the domain map: R_c 3). THE MARCH: cert
2e19, mass +2 percent in the first column, +9 percent by column 6,
+480 percent by mid-plug. CAUSE, read: the lip fan was posed as the
record's planar corner wave on the cut, whose rows start from the
lip state M 1.08 while the kernel field at the leading ray's crossing
is M 1.15 -- a jump across the leading ray in the start data. In a
NON-UNIFORM incoming field the corner wave is not a simple wave; the
fan must be marched as a Goursat problem from the lip through the
kernel field (each ray a C- from the lip with the corner relation's
state, its points found by the C+ from the previous ray; the bell's
step (3) structure with a centred corner). The record has no such
piece -- the bell's throat corner is a circular arc, the plug's fans
(planar, fan_axi) assume a uniform incoming flow -- so THIS is the
next brick: "the lip corner in the kernel's field", after which the
cut carries continuous data and the march of section 8 (frame
covariance 1.7e-5) does the rest. Kept as the negative of record
(K-1/K-2 FAIL) with the FRM_ZCUT/FRM_RCIN/FRM_RCOUT knobs.

## 12. The corner fan in the kernel's field -- DONE -- and the geometry that stops the pipeline (late night; owner: "vai")

`a1_frame_march.corner_fan`: the lip's centred expansion marched as a
Goursat problem through the kernel field. The leading ray is the C-
from the lip traced through the field (RK4 on tan(theta - mu) with
the local kernel state, its states the field's); every next ray is a
C- from the lip with the corner relation's state (theta - nu constant
across the fan: theta_k = theta_L + nu(q_k) - nu(q_L), q_k from q_L
to q(p_a)); each point is solved by the record's TOP-DOWN interior
cell in the rotated frame (`make_resid_interior_td_rot`: the C- from
the previous point on the ray, the C+ from the same-index point on
the previous ray -- the bell's step-(3) structure with a centred
corner), seeded by the straight-line crossing. MEASURED on the
kernel-fed case (lip M 1.079, 24 rays x 12 points to the cut 0.13 mm
downstream): every cell certified, worst 0.016; the cut data are
continuous across the leading ray (kernel row M 1.109, theta -0.10
deg -> first fan row 1.134, +0.58 deg) and the fan reaches M 3.41 at
+56.0 deg on the terminal ray = the axial exhaust in the record's
frame. The corner in a non-uniform field is done.

The march then holds the mass to 2.4 percent over the first eleven
columns (the −2.4 percent is the first column's wedge, the record's
own vertical-start effect, edge_fill 0) and folds at x' 1.7 mm where
the wall cell consumes 18 rows at once. CAUSE, geometric: the kernel's
inner wall is a parabola curving AWAY from the channel (every throat
series has both walls diverging downstream of the minimum section),
while the Angelino plug turns INTO the channel from a flat foot -- a
9 deg wall-angle gap at the cut when the kernel is read on the real
wall (first attempt), and, when the wall is posed to follow the
parabola up to 0.4 d and then transition to the Angelino contour
(`FRM_WALL=lb`), a 20 deg concave turn over 3 mm: a compression, a
shock, which no march of characteristics carries. The external plug
is not a series-kernel geometry; the consistent L-b geometry is an
INTERNAL-EXTERNAL plug (the plug wall keeps diverging past the lip,
the cowl smooth through the throat): Humphreys' Fig. 1 exactly.

STATE OF THE BRICK. Tools complete and each verified on its own
gates: the annular kernel (X-ANKR, ≡ Dutton on four measured
throats), the corner fan in a non-uniform field (certified, continuous
data), the rotated-frame march (X-FRMR, covariant 1.7e-5). Their
first physical twin is an internal-external plug: Humphreys 1971 once
its throat radii are read (the thesis / Fig. 1), or a posed one. On
Chutkey's external plug the record's construction (the fan cut at 1.5
mm) stands, with its ladder to 1.0 mm as the declared band.

## 13. Figures: how the code holds the literature profiles (owner's request)

`validation/_literature_profiles/make_figs.py` (presentation only) ->
`01_chutkey_contour_and_primary_nozzle.png` (the plug contour of
Fig. 2b as digitised, registered, smoothed, with the Angelino foot
blend; the primary nozzle of p. 479 redrawn from its segments in the
record frame; the throat line, lip, foot, and the cut of record),
`02_chutkey_primary_throat_kernel_indicative.png` (the kernel's
iso-Mach field in the primary nozzle throat, 1 vs 3 terms, labelled
NOT converged: R_c 0.33), `03_dutton_fig6_wall_mach.png` (our series
at y_o vs theirs vs the measured wall Mach vs 1-D),
`04_dutton_fig8_9_10_contours.png` (posed arcs and digitised walls,
our iso-Mach 0.6-1.4 against their series' points and the measured
points, the inclined frames registered on their series). Earlier
figures of the line: `_humphreys_twin/figs/01_contours_vs_paper.png`,
`_chutkey_twin/figs/01-04`.

## 14. Two walker tests (2026-09-22 early morning; owner: "vai" on the SQP test list)

`a1_humphreys_twin.py` gains HMPH_PERTURB (seeded normal perturbation
of the start's knots, in inches) and HMPH_FAN=axi (the axisymmetric
fan for the Rao case, theta_E = 0), with the gates P-1 (return from
the perturbation within delta/3 on every knot but the first) and P-2
(from the ideal member the walk stays on Table 3 within the measured
stay class 0.15 in, `humphreys1971_tables.json:_knot_class_in`).

**Return from perturbation (opt case, Table 2 + delta 0.30 in, seed 1,
backtrack 3, 30 x 8; s2, 1545 s).** dW = [+0.10, +0.25, +0.10, -0.39,
+0.27, +0.13] in; start J 32,352 lbf (-1.6 percent). Landing 32,869
lbf (-3.7e-4 of 32,881; the unperturbed table start landed at 32,864):
**the value returns**. The knots against Table 2: [0.31, 0.18, 0.06,
0.001, 0.03, 0.13] in -- the interior knots 3-5 return (from 0.10/0.39/
0.27 to 0.06/0.001/0.03), the first is the planar inlet's own +0.3,
**the tip does not move at all (0.134 -> 0.134: y_D 1.11 vs 0.975)**
and the second returns by half (0.25 -> 0.18). P-1 FAILS at delta/3 =
0.10, and the log shows why: from segment 7 on, every trial and every
backtracked point is "record not certified" with cert 1.5-22 -- not a
fold (1e10), the Newton's round-off floor of a few cells one decade
above the strict metric 100 eps -- and the radius shrinks to 6e-3 with
the walk parked at |grad| 1.2e5 (the smallest yet; 5.4e5 in S31). Two
readings: (i) the tip knot's gradient is nil in this posing (the base
term with Veen is 21 lbf; the flat valley IS the tip), so a
perturbation of the tip is not restored -- the base closure (chutkey)
or the adaptive tip knots are what would restore it, not the driver;
(ii) near the optimum the walk is stopped by the CERTIFICATION FLOOR
(G1 strict) of marginal cells, the S31 section 3.3 decision (a) -- a
conditioning-aware metric -- now measured as the thing that ends walks
in the flat valley. The walker itself did what a walker must: value
back to 4e-4, the well-conditioned knots back to 1e-3..6e-2 in.

**Rao from the ideal member (HMPH_FAN=axi).** Posed but NOT a walker
result: the axisymmetric fan certifies (0.036 at M_i 1.6) and the
6-knot spline through its wall with the fan's cut at X0 0.05 R starts
uncertified (3e10) -- the posing (the coarse spline on the member's
fast turn near the lip, the cut inside the declared strip) is
inconsistent, and the S31 Table-3 start already answered the question
("stays", +0.13 percent, y_D 1.44 vs 1.375). Dropped.

## 15. The gradient AT the optimum, and the band on a MOVE (2026-09-22 midday; the two open readings of section 14)

Section 14 left two questions a walk cannot answer, the walk being the
instrument under test: (i) near the optimum, where every trial sits on
the certification floor, is the reverse-AD gradient the driver follows
still the derivative of the RE-MARCHED value, and (ii) is the paper's
own contour stationary for OUR functional -- read against what our
march can resolve, not against a wish. `a1_humphreys_twin.py` gains
STAGE grad (no walk; `_pose()` factored out of `opt()`, bit-identical
to the record's lines) which differentiates three designs on the same
posing -- their Table 2, our table-start landing, the perturbed
landing -- and grades five gates.

**THE BAND A PRICE IS GRADED AGAINST.** A first-order price is a
DIFFERENCE between two designs, never a value, and the march's
discretisation error is COMMON to designs of the same family on the
same grid. Graded against the band on the VALUE (K_RICH x the
refinement's own move, the C-6 rule as it stands) nothing could ever
be live: at their contour the value moves 241.6 lbf under
(81,41) -> (161,81), a band of 966.6 lbf = 2.9e-2 of J, FIVE TIMES the
span of the paper's own 20-run grid (178 lbf) -- the gate would be
measuring the grid. The band on a MOVE is the amount by which the
refinement moves the DIFFERENCE, and it is an order tighter:

| | (81,41), band from (161,81) | (161,81), band from (321,161) |
|---|---|---|
| J at their table | 32,765.1 lbf (-3.5e-3) | 33,006.7 lbf (+3.8e-3) |
| cert at their table | 0.546 | **2.96e8 (uncertified)** |
| band on the VALUE | 966.6 lbf (2.9e-2 of J) | 504.3 lbf (1.5e-2) |
| our landing - their table | +99.0 -> +67.9 lbf (moves 31.0) | +67.9 -> +55.7 (moves 12.2) |
| perturbed - their table | +103.8 -> +79.0 lbf (moves 24.8) | +79.0 -> +69.0 (moves 10.0) |
| **band on a MOVE** | **124.2 lbf (3.8e-3 of J)** | **48.6 lbf (1.5e-3)** |
| price of a stay-class move, inlet knot | 97.3 lbf | **82.1 lbf** |
| price, the five shape knots | 4.7-14.5 lbf | 5.6-13.7 lbf |
| G-1 / G-2 / G-3 / G-4 / G-5 | PASS/PASS/**FAIL**/PASS/PASS (4/5) | PASS/PASS/**PASS**/PASS/PASS (**5/5**) |

READ.

1. **G-1: the gradient is sound where the walk stops.** At their
   optimum AD and central differences agree to 1e-3..7e-1 against the
   ladder's own scatter (bands 0.8-16): what ends the walks is not the
   gradient. Measured at both rungs.
2. **The value is NOT grid-converged; the differences are.** J at their
   contour reads 32,765 / 33,007 / 33,133 lbf on the three grids --
   increments 241.6 then 126.1, ratio 1.92, first order -- so the
   Richardson limit is about 33,270 lbf, +1.2 percent above their
   32,881 (0.2 of which is their shear, not in our J). The S31 reading
   "our functional reads their thrust to 0.3 percent" was, in part, the
   grid error: what survives refinement is the DIFFERENCE between
   designs, which is what the walk uses. Both bands on a move fall
   BELOW the paper's own grid span: our machine discriminates designs
   finer than their 20-run grid did.
3. **G-5: the landscape is resolved where the value is not.** Under
   (K,N) -> (2K-1,2N-1) the price of a stay-class move changes by at
   most 15.2 lbf (first rung) and 5.5 lbf (second); the inlet knot's
   price converges 97.3 -> 82.1 -> 76.6 lbf. The walk walks on a
   landscape the grid resolves, on a value it does not.
4. **G-2/G-3: THEIR CONTOUR IS STATIONARY FOR US IN SHAPE; THE ONE
   LIVE DIRECTION IS THE FROZEN INLET.** The five shape knots buy
   5.6-13.7 lbf over their whole measured stay class (0.15 in), an
   order below the band on a move. The inlet knot buys 82.1 lbf
   against 48.6: at the first rung it was 97.3 against 124.2 and G-3
   FAILED -- the gate flips with the rung, and it is the rung that
   changed, not the physics (the price converges, the band shrinks
   4x). This is the first-order form of "the model verifies an optimum
   but does not find it from afar" (section 1): in shape there is
   nothing left to find; at the inlet there is, and the inlet is the
   posing's own frozen dof (planar fan, y_w0 set by the mass at
   X0 0.05 R -- their foot is 6.72 in at x -0.6 in, ours 6.04 in at
   X0 0.38 in).
5. **G-4: the tip is not restored because nothing pays for it.** The
   0.134-in tip residue the perturbed walk left is worth 2.5 / 1.5 lbf
   on its own gradient, an order below the band: the P-1 failure of
   section 14 read at the gradient. The tip is priced by the base
   closure, not by the driver.

**OPEN, and the first item of the next brick.** At (161,81) the record
on THEIR contour does not certify -- cert 2.96e8 -- while both of our
landings do (0.192, 1.593). Per G1 the second rung's numbers are
therefore a reading, not science, until that 3e8 is ATTRIBUTED:
near-lip conditioning (the S31 section 3.3 mechanism, kappa ~ 1e6 at a
sonic lip, which the strict metric 100 eps cannot satisfy however good
the root) or a genuine fold (the geometric margin [X-PMRG] decides it
in one march). The gate that decided G-3 is itself gated by the
certification floor.

**OWNER'S DECISIONS ON THIS READING (2026-09-22).** (3) The
certification floor of S31 section 3.3: **option (b)** -- the cell in a
rotated frame, removing the ill-conditioning at its geometric source
(near-vertical characteristics) instead of widening the metric. In S31
this was a brick; [X-FRMR] has since made it frame-covariant to 1.7e-5
of p_0, so the rotation is available per cell. (4) The inlet: route
(i) first -- free y_w0 and the slope at the cut as design variables
with the mass as an explicit constraint of the TR-SQP, inside the
current machine -- then route (ii), the kernel start line, posed on
the INTERNAL-EXTERNAL geometry of section 12 (Humphreys' Fig. 1), not
on Chutkey's external plug.

Artefacts (not committed, as the line's others):
`_humphreys_twin/run_grad_opt_2026-09-22.log` (the first, 3/4, whose
G-3 was graded against the value's band -- superseded),
`run_grad_opt_2026-09-22_band.log` (4/5, rung one),
`run_grad_opt_2026-09-22_K161.log` (5/5, rung two, 1311.8 s),
`grad_opt_veen_K81N41.json` and `grad_opt_veen.json` (rung two).

## 16. The attribution, and what it found underneath (2026-09-22 afternoon; owner: "for 3 go with option (b), for 4 the order you suggested")

Section 15 left ONE declared open item -- attribute the 2.96e8 on the
paper's contour at the finer rung, conditioning or fold -- as the first
item of the rotated-frame brick. The attribution is `a1_humphreys_twin.py`
STAGE class (5/5, 170 s), and it found the answer plus something the row
did not know about itself.

**THE CENSUS.** The margin carrier's own ([X-PMRG]): the signed area of
the net's TRUE cell over its mean legs, floored at the station spacing
squared, orient-signed by the median; a RESOLVED cell (leg product above
the floor -- the floored ones are the free-jet slivers the criterion does
not resolve) with a non-positive margin is a fold. The control is the
incumbent of this posing, the fan's own streamline, the start the
record's walks open from.

| design | J | cert | resolved cells | FOLDED |
|---|---|---|---|---|
| fan streamline (incumbent) | 29,946.2 lbf | 0.034 | 852 | **0 (0.00 %)** |
| their Table 2 | 32,765.1 | 0.546 | 2352 | **677 (28.78 %)** |
| our landing | 32,864.0 | 0.098 | 1361 | 87 (6.39 %) |
| perturbed landing | 32,868.9 | 3.495 | 1489 | 182 (12.22 %) |
| their Table 2 at (161,81) | 33,006.7 | 2.96e8 | 9410 | 2716 (28.86 %) |

READ.

1. **The two certification failures of this row are NOT the same
   mechanism.** (K-3) The 1.5-22 band that parks the walks near the
   optimum (section 14) is NOT a fold: at the perturbed landing's worst
   cell, ('wall', 25) at cert 3.495, the adjacent resolved census cell
   carries margin +0.5651 -- a healthy neighbourhood, the near-wall
   conditioning of S31 section 3.3. **The owner's option (b), the cell
   in a rotated frame, is aimed at the right mechanism.** (K-4) The
   2.96e8 at the finer rung IS a fold: its own column carries 19 folded
   cells. The rotated frame is not its cure and was never going to be.
2. **(K-5) The fold is the DESIGN's, not the net's**: the folded
   fraction of their contour is 28.78 percent at (81,41) and 28.86 at
   (161,81), the same within the census's own granularity (band
   0.17 pp). Refining does not dissolve it; it resolves it.
3. **(K-1/K-2) AND THIS IS THE FINDING: the thrust rows of this twin
   rest on FOLDED marches.** The incumbent is clean (0 of 852 resolved
   cells), so the criterion discriminates; the paper's own contour,
   marched with OUR frozen planar inlet, folds over 28.8 percent of its
   resolved cells, our landings over 6.4 and 12.2. By this line's own
   S29 precedent -- [X-PGRS] re-stamped OUT OF CLASS because the fine
   optimum's march was folded, "the number is taken from a folded march
   and is NOT a gain" -- the readings of S31 and S32 on their contour
   ("our functional reads their thrust to 0.3 percent", "the walk
   STAYS", the landing at -5e-4, and the section-15 prices and bands
   taken at those designs) are OUT OF CLASS and must be re-taken.
4. **Why it happened, and it is nobody's slip**: the driver has carried
   the class constraint since S29 (`run_trsqp(margin=...)`, the phase-1
   restoration that minimises the violation before the objective), and
   `a1_humphreys_twin.opt()` calls it WITHOUT the margin. The twin was
   posed in S31 before the margin was routine on this line.

**WHAT IT DOES TO THE QUEUE.** The inlet (the owner's 4(i)) rises from
"the one live direction" to "the suspect for the fold as well": the
incumbent whose inlet is consistent with the fan by construction is
clean, and every design that carries their contour through OUR cut --
+0.34 in at the first knot, a wall angle the fan did not produce --
folds. The rotated-frame cell (3, option (b)) keeps its place for the
band that parks the walks, but it is now measured as the SECOND cause,
not the first.

**WHERE THE FOLD COMES FROM (K-6/K-7/K-8, added the same afternoon
after the owner read figure 02: "their Table 2 profile waves, it does
not follow the paper's points, and it starts at a higher radius than
Humphreys' point").** The owner's eye was on the cause.

- **(K-7) The start radius is not theirs.** y_w0 is set by the imposed
  mass at the cut, 5.960 in against their 5.627 in there: we begin
  **+0.33 in ABOVE their wall**, the deviation peaks at +0.375 in at
  x 0.92, and the first knot is only at x 2.22 in -- nothing holds the
  wall to their contour over the first two inches. Their contour is
  steepest at x -0.48 in, UPSTREAM of our cut, and climbs monotonically
  from there; ours is steepest at x 1.47 in, INSIDE the marched field:
  the throat turn is re-done in the middle of the flow. The first
  folded column is at x 1.88 in, just downstream of it.
- **(K-8) And the wall ANGLE is what the characteristics see.** Six
  knots pinned at a start radius that is not theirs reproduce y to
  0.375 in, but the wall's DIRECTION oscillates about their printed
  angle: +10.47 deg at x 0.51, -11.85 deg at x 1.74, rms 4.14 deg,
  crossing their angle five times and turning three times where their
  own angle column is monotone. At M 2-3 the Mach angle is 20-30 deg,
  so a ten-degree wall error is not a detail of the drawing: it is an
  alternation of expansion and compression, and the compression halves
  are where the net crosses itself.
- **(K-6) And it reaches what the row argues about.** J is the momentum
  through the cut (fixed by the imposed mass) plus the wall push, and
  only the push is marched: 3496 lbf of the 32,765. The first fold sits
  at 12 percent of the wall, and **1745 lbf of push -- 50 percent --
  lies downstream of it**, against the 178 lbf span of the paper's own
  20-run grid, which is the scale at which this twin's verdicts are
  read. Our own landing is milder: first fold at x 5.84 in, 349 lbf
  (10 percent) downstream.

**(K-9) AND WHY THE CUT IS NOT ON THEIR WALL -- the owner's question,
"what is Table 2, and why do we not start from their foot?".** Table 2
is the contour of THEIR optimum: twenty (x, y, wall angle) rows from
the plug's throat point A -- the foot, (-0.56069, 6.71874) in at
-36.25 deg, where the plug meets their start line AE -- to the
truncation D at (11.51707, 0.95441) at -13.26 deg. We do not start
there because a march of characteristics cannot start on a sonic line
(ill-posed as Cauchy data, measured 2026-09-18: cert 1e18) and barely
survives the near-vertical characteristics just past it (S31 section
3.3, kappa ~ 1e6): nobody starts there -- they start from a transonic
kernel ("modified Moore-Hall"), the bell starts from Sauer, GENO from
Migdal. Our substitute is an idealised PLANAR corner fan at a sonic
lip, read on a vertical cut at X0 = 0.05 R, and that fan is not their
throat: **with the wall placed AT their contour at the cut (5.746 in
against our 6.037) our fan would pass +19.2 percent mass and carry
+25 percent inlet momentum.** The cut can hold THEIR MASS or THEIR
WALL, not both. The record holds the mass -- thrust is proportional to
it and a thrust compared at another mass is not a comparison -- and
pays with the 0.33-in geometric offset that K-7 and K-8 then price.
The posing that holds both is a start line from a real transonic
throat with their geometry: the kernel brick (the owner's route (ii)).

**A SECOND, SMALLER DEFECT IN THE OBJECTIVE ITSELF.** Their Table 2 is
TWENTY rows, nine of them crowded into the first 0.08 in at the foot
and gaps of up to 2.66 in downstream -- and it prints THREE columns:
x, y and the wall angle. The S31 posing read y by straight chords
(`np.interp`), which on a convex contour rides ABOVE it: measured
+0.005 to +0.030 in on the six knots (worst at x 4.07). `read_table`
(HMPH_TABLE, default `chord`, every row of record bit-identical) reads
it instead as the cubic Hermite through their (x, y) with THEIR printed
angle as the slope -- their own data, read as they drew it. The switch
is for the in-class re-take, not for this log's numbers.

**Figures** (`_humphreys_twin/make_figs.py`, presentation only, every
physical number re-read from the carriers' marches):
`figs/02_objective_and_arrivals.png` -- their contour drawn from their
own three columns, our wall from their knots drawn separately (they are
NOT the same curve), the six knots, the mass-set cut, a zoom of the
first three inches with the first folded column marked, the wall-angle
panel where their monotone angle and our oscillating one are put side
by side, and the thrust ladder with the band on a move against their
own grid span; `figs/03_folded_cells.png` -- the characteristic net of
the same machine on the incumbent (clean) and on their contour (the
folded cells filled), with a zoom on the net crossing itself.

Artefacts: `_humphreys_twin/class_opt_veen.json`; the scratch probes
that found it (`RDE/_scratch_s32/attrib_cert*.py`) are superseded by
the stage. Trap paid on the way, for the record: `a1_plug_margin`
imports the driver at module level, whose constants (PSPL_M,
A1_BASE_MODEL, ...) are read at IMPORT time -- importing it before
`_pose()` has posed the environment silently marches a different design
(6 knots became the driver's default, the base model vanished, and the
census read cert 0.418 where the record reads 2.96e8).

## 17. Their throat, from their own table and text (2026-09-22 evening; owner: "proceed, and make sure R_c is 1")

The owner asked how to start from Humphreys' throat, whether Sauer could
be applied locally, and what GENO does. The answers of record, then the
measurement (`a1_humphreys_twin.py` STAGE throat, 4/6, 0.3 s).

**Sauer, locally: no.** (i) Sauer IS the one-term truncation of the
series we hold to three terms -- X-TKRN's gate T-5 measured Moore's
first approximation at K = 0 to be Sauer planar (6e-11). (ii) Sauer
presumes a symmetric throat with an axis or a midplane; their passage
is annular and asymmetric, and at K = 1 (X-TKRN T-6) the sonic points
sit at z = -4/3 on the curved wall and +2/3 on the straight one, the
singular point ON the straight wall -- a symmetric Sauer would put the
sonic line elsewhere. (iii) At their throat there is barely a small
parameter at all (below). **GENO**: `InitialValues_m.f90` holds a true
Sauer IVL (`IVLINE_solve`, wall to AXIS, the bell's) and, for the
annulus, `IVLINE_annular_solve`, whose own comment says "Migdal 1972
Fig. 2: IVL is the line A-B, normal to theta_i": ONE Mach, q0 constant,
theta constant on a straight inclined segment. No transonic solution on
the annulus -- the uniform inclined line Humphreys p. 1587 prices at
2700 lbf (8 percent).

**THE PAPER'S OWN THROAT (p. 1585-1586, read verbatim for this
stage).** "The parametric study was conducted for a nozzle which has a
mean radius of curvature at the throat of 0.705 in., a downstream
radius of curvature of 0.5 in., and a length from point T to point D of
12.0 in." (p. 1586); "the plug curvature in this region [downstream of
A] is specified ... point T is located so that no discontinuity in the
plug contour arises ... point T will always be downstream from point A"
(p. 1585); "the start line will always be from point A to point E".

- **(T-1) Table 2's nine crowded rows at the foot ARE the prescribed
  arc**: eight consecutive intervals turn at a constant radius
  **0.5000 in** (spread 8e-4, band 6e-3), from -36.25 to -48.25 deg --
  the paper's "downstream radius of curvature of 0.5 in." to the
  fourth digit. A known answer of the transcription.
- **(T-2) The arc ends at T = (-0.48331, 6.64846) in, and T -> D =
  12.0004 in** against the paper's 12.0: the second known answer. The
  optimised contour of Table 2 begins at T, not at A.
- **(T-3) A -> E: h = 1.0027 in at 56.00 deg from the axis = exactly
  90 + (-34)**, normal to their injection. (If h were exactly 1.0 in
  the lip would sit at (-0.0015, 7.5478) in; "7.55" cannot tell.)
- **(T-4, FAIL, the correction) R_c = 0.705 / 1.0027 = 0.703, NOT 1.**
  The first reading of the day took the downstream arc (0.5 in) for the
  throat curvature and got R_c ~ 1; the paper's Moore-Hall input is the
  MEAN radius at the throat, 0.705 in, and Dutton's R_c = R_mean /
  separation whatever the split between the two walls (the split sets
  only K). 0.703 is BELOW the kernel's declared convergence domain
  (`rc_converged_from` 1.0): the gate rejects the posing as declared.
- **(T-5, PASS) But measured AT that throat the series still
  converges**: symmetric split (K 0), throat-plane Mach 1.071 / 1.049 /
  0.971..1.208 by 1/2/3 terms, |M2-M1| 0.046, |M3-M2| 0.034, **ratio
  0.73** -- the truncation band, declared; W/W* 0.9947; first
  all-supersonic line at x +0.03 d with M 1.00..1.25 and theta
  -1.5..+1.5 deg, W/W* 0.9915. The straight-cowl split (K 1) is
  stretched at this R_c: M(x=0) 0.87..1.65 at three terms, ratio 0.76,
  W/W* 0.9645, the first supersonic line at x +0.19 d with M up to 2.09
  and theta to -14.7 deg. The split is the ONE datum the paper does not
  print; "mean radius of curvature" reads as two finite radii, i.e.
  nearer K 0, which is also the better-conditioned posing.
- **(T-6, FAIL, THE FINDING ON THE MASS) Their 148.08 lbm/s is 1.029
  times the choked 1-D mass of the line A -> E.** The surface of
  revolution of A -> E is 44.95 in^2; at p_c 500 psia, T_c 6000 R,
  R 56 ft-lbf/(lbm-R), gamma 1.23 the choked 1-D mass through it is
  143.89 lbm/s, and no line of that area can pass more (rho u peaks at
  M = 1). The kernel's own discharge is 0.9947 (K 0) / 0.9645 (K 1) of
  it: **their stated mass exceeds what their stated geometry can pass by
  3.4 to 6.7 percent.** This is the S31 "mass convention" item (Rao's
  member passing 137.8 against their 148.08) with a number and a gate:
  the paper's mass, lip, foot and gas are not mutually consistent under
  1-D choking at the 3-percent level. "The mass flow rate ... were
  SELECTED as 148.08 lbm/sec" (p. 1586): an input, not a discharge.

**WHAT IT DOES TO ROUTE (ii).** The cut can hold their mass or their
wall (section 16, K-9), and now: **a perfect kernel on their geometry
would pass ~143 lbm/s, 3.4 percent short of their number, by their own
inconsistency.** The geometry-faithful twin must therefore compare
SPECIFIC thrust (J / mdot, or C_F), not J -- the only metric the mass
inconsistency does not touch. And the kernel is posable: R_c 0.70 with
the K 0 split, truncation ratio 0.73 declared, y_i 8.08 (thin annulus,
the annular term small), the first supersonic line at +0.03 d from the
throat plane. The alternative if 0.73 proves too wide for the gates is
the one already named: solve the transonic region numerically with the
three-term series as the upstream condition.

**THE CHUTKEY COMPARISON (owner: "is this not like the Chutkey contour?
how did we solve the twin there?").** Same setup -- external plug, cowl
lip, a march from a cut with the strip to the throat declared -- and one
shortcut that does not carry over. Chutkey's plug IS an Angelino
contour (X-CHTW T-0: throat tilt 56.9 deg = nu(M_e) to 0.01 deg), so the
ideal centred fan at the lip is consistent with the wall BY DESIGN: the
fan's streamline through the foot is the wall, the twin compared WALL
STATE (p_w to +0.7..+1.8 percent, M to -0.4 at the four truncations)
and paid a declared -6.2 percent of first-column mass. Humphreys'
optimum is not ideal (the ideal member at their lip passes -24 percent
of their mass, S31) and the twin compares THRUST, which needs the mass:
hence the mass-set radius, the 0.33-in offset, the fold. And the
Chutkey kernel path failed for two reasons that Humphreys does not
have: the digitised foot is noise at 0.1 mm on a 1.32-mm throat, and
the Angelino foot is flat then turns INTO the channel (section 12);
here the foot is an exact printed arc that curves AWAY from the passage
-- a series-kernel geometry, as section 12 predicted ("Humphreys'
Fig. 1 exactly").

Artefacts: `_humphreys_twin/throat_opt.json`; constants in
`humphreys1971_tables.json` (`_throat_mean_radius_in`,
`_downstream_radius_in`, `_table_precision_in`, `_lip_precision_in`,
`_length_TD_precision_in`, each cls SPEC with the page).

## 18. The march from their throat, and the series' verdict (2026-09-22 night; owner: "C_F against C_F, go", then "can you solve the transonic up to where the SQP march starts?")

**The pipeline on their geometry** (`a1_humphreys_twin.py` STAGE kernel):
the annular kernel [X-ANKR] posed on their throat (plug rc 0.5 in = the
arc, cowl rc 1.195 in from their mean 0.705 in in the harmonic sense,
R_c 0.703, the plug wall's -2.25 deg at A carried as the kernel's inner
slope), its field handed to the lip corner fan as a Goursat problem
[X-FRMR corner_fan] from E on the throat line, the start line on a
vertical cut of the throat frame (kernel rows to the leading ray, the
fan's ray crossings, the uniform wedge to the jet boundary), the march
with the rotated-frame cells along THEIR wall -- the prescribed arc A ->
T, then Table 2 read with their printed angles -- to D. Gates H-0 (fan
certified), H-1 (start line space-like), H-2 (march certified), H-3
(mass conserved to the last column), H-4 (in class), H-5 (a physical
discharge), H-6 (J / mdot within the thrust class).

**What runs, and this is new.** On Chutkey's external plug this
pipeline folded at 1.7 mm (section 12); on Humphreys' geometry it runs
to D: the fan certifies (0.014-0.016), the start line is space-like on
every row (+5.8..+13 deg), the march is Newton-certified (0.04-0.08 on
17,000 cells), y_D comes out 0.954 in -- theirs, since the wall is
theirs -- and **the mass through the cut is 139.5-141.6 lbm/s = 0.969-
0.984 of the choked 1-D of A -> E**, a physical discharge, against their
stated 148.08 = 1.029: the third independent route (after the 1-D bound
and Rao's member) to the same reading of their mass.

**What does not, and its attribution.** The march loses mass at its
FIRST column and keeps losing it, and 3-5 percent of its resolved cells
fold (census floor = this march's own station spacing; a first version
had used the driver's constants). Eleven runs isolate the cause:

| knob | first-column step | last column |
|---|---|---|
| z_cut 0.12 / 0.25 / 0.40 (their wall) | -7.4 / -6.0 / -3.6 % | -12.9 / -11.9 / -11.3 % |
| z_cut 0.08 / 0.06 | -6.3 / -5.7 % | -9.8 / -8.1 % |
| N 41 -> 81 | -6.0 -> -6.1 % | -11.9 -> -12.1 % |
| the wall's slope at A on / off | -6.0 / -6.7 % | |
| wedge rows 0 / 2 / 10 | -6.9 / -7.4 / -7.4 % | |
| fan rays 25 / 49 | -7.4 / -7.4 % | |
| **wall = the kernel's own parabola, R_c 0.703** | **-7.2 %** | (the parabola plunges beyond 0.5 d) |
| **wall = the kernel's own parabola, R_c 4.0** | **-1.2 %** | **-1.0 % (flat, certified 0.84)** |

Not the wedge, not the fan, not the rows, not the wall mismatch (the
kernel's own parabola loses the same 7.2 percent as their arc), not the
cut (moving it toward the throat plane shrinks the step but never below
5.7 percent while the flow is supersonic). **The same pipeline on a
throat where the series converges (R_c 4.0, third/second 0.16) steps
1.2 percent -- the vertical-start wedge class of the Chutkey kernel run
(2.4 percent) -- and then holds the mass.** The step is the three-term
series' own residual in the equations at R_c 0.70: the march, which
satisfies them cell by cell, rejects 7 percent of the start line's mass
at once. The eta spread that section 17 read as the truncation band
(0.84-1.6 percent at z 0.06-0.12) UNDERSTATES that residual by a factor
of five: the march is the judge, not the re-summation.

**THE ETA LADDER (2026-09-22 late night) CORRECTS THE ATTRIBUTION
ABOVE.** Section 18 as first written called the first-column step "the
three-term series' own residual in the equations at R_c 0.70", implying
the O(eps^3) truncation. The re-summation parameter eta is the lever on
exactly that (eps = 1/(R_c + eta)), so the ladder is the test:

| eta | eps | series W/W* at the cut | first-column step | folded | drift col 2 -> last |
|---|---|---|---|---|---|
| 2 | 0.370 | 0.9763 | **-7.38 %** | 23.6 % | -0.62 % |
| 4 | 0.213 | 0.9841 | -5.94 % | 18.0 % | -0.32 % |
| 6 | 0.149 | 0.9868 | -5.08 % | 10.3 % | -0.19 % |
| 8 | 0.115 | 0.9876 | **-4.57 %** | **6.6 %** | **-0.11 %** |

(z 0.12, their wall, the march capped at 2 d so J is not comparable
across these rows and is not read.) TWO READINGS, one of them against
the earlier claim.

1. **The truncation is a real part of it, and eta buys a lot**: the
   step falls monotonically 7.4 -> 4.6 percent, the folded fraction
   COLLAPSES 23.6 -> 6.6 percent, and the drift after the first column
   almost vanishes (0.62 -> 0.11 percent): at eta 8 the march takes its
   step and then HOLDS. The start line is far more self-consistent.
2. **But it is NOT the O(eps^3) residual, and eps is not the governing
   parameter.** eps^3 falls by 34 from eta 2 to eta 8; the step falls
   by 1.6. And the decisive comparison is at EQUAL eps: R_c 4.0 with
   eta 2 (eps 0.167) steps **1.2 percent**, while R_c 0.703 with eta 8
   (eps 0.115, SMALLER) steps **4.6 percent**. Smaller expansion
   parameter, four times the step. What R_c changes besides eps is the
   flow: at R_c 0.703 the line spans M 1.04-1.55, at R_c 4.0 M
   1.12-1.28 -- a transverse gradient five times steeper. The step is
   not "the truncation" simply; it is the series at a sharp throat, of
   which the truncation is a lever and not the whole.
   The attribution of record is therefore narrowed: the R_c-4 control
   still separates "the series" from "the hand-over" (the pipeline is
   sound where the throat is smooth), but the floor at R_c 0.70 is NOT
   explained by the expansion parameter and is OPEN.

**J / mdot, for the record and not as a verdict**: +2.0..+3.1 percent
above theirs across every configuration (C_F on A -> E -1.5..-6.3
percent, the mass), read on marches that lose 8-13 percent of their
mass; not citable.

**THE ANSWER TO THE OWNER'S QUESTION.** Yes, the transonic region can
be solved up to where the SQP march starts -- and at this throat it
MUST be, because the series cannot: (i) Humphreys fix the geometry
upstream of the characteristic BT, prescribe the arc A -> T and let T
slide on it (p. 1585), so the start line is computed ONCE per (lip,
injection angle) and frozen -- OUTSIDE the SQP loop, neither
differentiable nor fast; (ii) the solver is a small axisymmetric Euler
march in time to steady state on the throat region (analytic walls,
subsonic inflow at their p_c, T_c, gamma, supersonic outflow, slip
walls), in JAX like the rest; (iii) its oracle is our OWN series where
the series converges -- at R_c 4 the series' sonic line, throat-plane
Mach and W/W* are known to the 3-term band, and this section has just
measured that the march accepts that line to 1.2 percent -- the T-5/T-6
pattern of X-TKRN; (iv) its gates at R_c 0.703 are this stage's H-3/H-4
(the march holds the mass and stays in class from the numerical line)
and the discharge against their geometry. The corner fan and the
rotated-frame march, both certified here, are its consumers unchanged.

Artefacts (not committed): `_humphreys_twin/run_kernel_*.log`,
`kernel_opt_*.json` (one per configuration, the knobs in the name).

## 19. The certification criterion (owner's directive, 2026-09-22 night) [DIR-REOB]

The owner, after the day's readings: "the objective of the program is
not to certify other people's optima but to provide a tool capable of
finding an optimum given a line of initial values"; and then, verbatim
in intent: **"we certify the optimum only if we manage to RE-OBTAIN it,
not if, starting from the same profile, it stays stationary -- because
in real problems we do not know what the optimum is."** Recorded as the
binding criterion of the line, [DIR-REOB] in the registry.

**THE CRITERION.** An optimum is CERTIFIED only when the tool re-obtains
it from elsewhere, in CONTOUR and in value. A walk started ON the
reference profile that stays there certifies the stationarity of that
point -- a property of the point, not of the tool's capacity to find
it. In production the optimum is unknown, so the only certificate that
counts is the one that does not use it as a start.

**THE THREE TESTS.**
- **RE-1, re-obtention from a reference** (where the optimum is known):
  the SAME initial-value line and the SAME functional as the reference,
  a GENERIC start -- the fan's streamline, a cone, random knots -- and
  the landing on the reference contour within the stay class (0.15 in
  per knot, measured) AND on the value within the band on a move.
  Several starts, not one.
- **RE-2, self-re-obtention** (production, the optimum unknown): a
  design D* the tool found, perturbed GROSSLY -- inches, or a restart
  from the fan -- not within the instrument's bands, and the tool's
  return to D* in contour. The falsifier of "the tool finds the
  optimum, not a stationary point that depends on the start".
- **RE-3, coincidence across starts**: from N different starts the
  landings coincide in contour within the class; where they do not, the
  spread in value against the band on a move tells the tool
  (start-dependent: a defect) from the problem (a flat valley: to be
  declared).
RE-2 and RE-3 are the only certificate available in a real problem;
RE-1 on the twins that carry THEIR OWN initial-value line is the
calibration of that certificate -- it says whether "the landings
coincide" implies "this is the optimum".

**WHERE THE FUNCTIONAL DOES NOT DISCRIMINATE CONTOURS** the criterion
cannot ask for the contour: the certifiable statement is re-obtention
of the VALUE within the band, and the ambiguity of contour is declared
as a property of the problem -- or the functional is enriched (the
base, off-design) until it discriminates. Whether Humphreys' valley IS
flat is itself not yet known: the prices of section 15 were read on
marches that section 16 found folded.

**THE RECORD RE-LABELLED under the criterion** (the rows carry the
clause from tonight):
- X-HMPH: the table-start landing ("the walk STAYS", -5e-4) is a
  stays test; the +0.30-in return is a basin test, and its tip did not
  return; the one re-obtention attempted, from the fan's streamline,
  PASSED in value (-0.19 percent) and FAILED in contour (y_D 2.72
  against 0.954 in). Not a finder certificate. All three on marches
  since found out of class.
- X-OWS3 (our world, the SQP-return v3, 6/6): the perturbation is 1.5
  percent off GENO's contour, inside the instrument's own bands -- a
  basin test. It holds the motion half of O3.3 (the optimum is a local
  attractor of the certified walk); it is not re-obtention from afar.
- No row of the line certifies the optimiser as a FINDER tonight.

**PREREQUISITES, IN ORDER**: the class constraint active in the driver
(built in S29, never used by the Humphreys legs); a resolution at which
the band on a move discriminates (48.6 lbf at (161,81) against the
paper's 178); for RE-1, the reference's OWN initial-value line -- which
for Humphreys the paper does not tabulate (their start line is Ref. 8's
"modified Moore-Hall"; the S31 posing replaced it with a planar fan on
a vertical cut with the wall radius set by the mass: a different line,
sections 16-18).

**WHAT CHUTKEY GAVE ON THE SONIC-LINE PROBLEM (the owner's question).**
Chutkey et al. 2014 do not march: their flowfield is RANS (HiFUN, Roe,
SA, y+ < 1, two grids) on the WHOLE geometry, primary nozzle included
-- the sonic line is computed, never posed -- and their plug surface
pressure is grid-converged and matches their taps (Fig. 9d, five taps
on the 20-percent plug). What our twin took from them: (i) the plug is
an Angelino contour (throat tilt = nu(M_e) to 0.01 deg), so the ideal
centred fan at the lip IS its construction, and the wall state
downstream of ~1.5 mm is reproduced to 1-2 percent from that fan cut
at M_i 1.6 with the throat strip DECLARED (X-CHTW; the price, -6.2
percent of first-column mass); (ii) the sonic line itself cannot be a
start (a double characteristic, cert 1e18) and a sonic lip's fan has
rays past the vertical in the record's frame (theta - mu < -90 deg
until M 1.83), which the throat frame cures (X-FRMR); (iii) their
primary nozzle ends in arcs of R 0.867 mm on a 1.32-mm half-height,
R_c 0.33 in Dutton's units -- OUTSIDE every series kernel (X-ANKR:
the third term moves the throat-plane Mach as much as the second),
so at that throat the transonic field is CFD's or nobody's; (iv) their
own note that a mild compression wave sits at the primary-nozzle/plug
junction (p. 483) is the physical counterpart of section 12's finding
that the Angelino foot turns INTO the channel. Chutkey therefore
frames the sonic-line problem exactly and answers it by not marching
through it; the geometry that lets a march start from a series kernel
is Humphreys' (an arc curving away, R_c 0.70, sections 17-18), and
even there the three-term series is rejected by the march at its first
column.

## 7. Conformity

- Branch `rde-nozzle-program`; identity AlexFalco5; no push.
- Files (S32 midday/afternoon, sections 15-16):
  `validation/a1_humphreys_twin.py` (stages grad, class, throat and
  kernel, `_pose()` factored out bit-identically, `read_table`, the
  docstring),
  `validation/humphreys1971_tables.json` (`_grid_class_lbf`, cls SPEC
  = their Table 1 span), this log; registry row X-HMPH re-printed.
- Files: `validation/a1_plug_spline_opt.py` (driver, additive knob),
  `validation/a1_throat_kernel.py` (new carrier, baseline row 65 in
  `numeric_lint_baseline_validation.json`, measured by the lint),
  `validation/a1_frame_march.py` (new carrier, baseline row 31), `validation/a1_annular_kernel.py` (new carrier, baseline row 36, with `_annular_kernel/derive_fn_sympy.py`); NOT
  `a1_rot_march.py`, which is the S24 rotational-inlet carrier X-RMAR
  -- overwritten by mistake for twenty minutes and restored from HEAD
  untouched), this log; registry rows X-TKRN, X-FRMR; ADVISORY_INDEX
  row; living PROGRESS parallel-line block.
- Not committed: `_humphreys_twin/*.log|json` of the leg (artefacts,
  as the S31 ones), the aborted v1 log.
- Lints 3/3 after the two-step commit (log first, registry row second — the claims lint's pass= rule); full suite 14/23 before the commit = the seven S26 reds + (xv)/(xvii) on the uncommitted X-TKRN doc, expected to return to 16/23 once the log has history; data/q_mapping.*, data/phase_diagram.*, figs/phase_diagram_op11.png restored with git checkout.
