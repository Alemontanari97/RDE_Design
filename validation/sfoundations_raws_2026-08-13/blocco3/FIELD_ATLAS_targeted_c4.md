# FIELD ATLAS — targeted C4 pass (T-RED-bearing published flow fields)

Session S-FOUNDATIONS-C4, targeted field-atlas agent (user-ordered
anticipation, injection (6)(a) 2026-08-20). Carrier authority:
BRIEF_blocco2_phaseD.md CENTERPIECE part (2) [T-RED] + FORCHETTA
channel list (i)-(vi); BRIEF_blocco2_phaseD_addendum_c4.md item (a).

EVIDENCE CLASS FOR EVERY ENTRY: **ADVISORY (published-figure
reading)** — a faithful reading of a rendered published figure, never
a measurement, never a record grade. No entry may be cited above this
class. Where a number appears, it is read off the figure axis/caption
or quoted from the surrounding text of the SAME rendered page.

SCOPE HONESTY: this is the targeted pass only (Harroun 2021 Figs
12-20 first, then the root-D read-integral corpus swept for
azimuthal-structure field figures). The FULL systematic corpus
field-reading pass remains with the unratified BLOCCATO-16 proposed
session. The 4 PDFs in literature_addition_nozzle_rde/ are owned by a
disjoint dedicated campaign and were NOT read here (filenames only,
opaque DOI-style — no dedup against them was possible).

Read-depth declaration (pages actually rendered visually):
- harroun_2021_computational_experimental_rdre_nozzle_performance.pdf: PDF pp. 7-12 (journal pp. 666-671)
- paxson_miki_2022_rdre_nozzle_cfd_optimization.pdf: PDF pp. 3-10
- kaemming_paxson_2018_equivalent_available_pressure.pdf: PDF pp. 2, 3, 10
- miki_2020_rde_nozzle_design_methodology.pdf: PDF pp. 4-12
- harroun_2020_rde_nozzle_simulation_validation.pdf: PDF pp. 4-10
- liu_2022_aerospike_rde_ga_gradient_optimization.pdf: PDF pp. 7-11 (= article pp. 7-11, AST 120 (2022) 107300)
- teasley_2023_nasa_rdre_state.pdf: PDF pp. 14-16
- wolanski_2013_detonative_propulsion_survey.pdf: PDF pp. 23-25 (journal pp. 147-149)
Plus a text-layer caption sweep (pypdf extraction, no page render) of
the full corpus to locate/exclude field figures; papers excluded on
that basis are in the skip list with reason.

Channel key (FORCHETTA, brief part (5)): (i) time-coupling /
unsteadiness; (ii) azimuthal-structure reduction (T-RED core);
(iii) swirl/tangential content; (iv) averaging adequacy; (v)
model-form bars; (vi) OPTIMUM-SHIFT.

---

## 1. HARROUN 2021 (J. Prop. Power style pagination 666-671) — THE EXHIBIT PAPER

3D unsteady RANS (Loci/CHEM per the 2020 companion), IE-aerospike and
nozzleless geometries, analytic rotating two-wave inlet BC (Eq. 7:
P(theta) log-decay 30->~2 atm, 13,800 Hz, non-rotating inflow with no
vorticity — i.e. NO imposed swirl: any tangential structure downstream
is wave-induced).

### H21-F11 — Fig. 11, journal p. 666 (PDF p. 7)
Analytically derived inlet pressure waveform vs azimuth at t=0 and
t=1/2f: two sawtooth waves, peak ~30 atm decaying logarithmically to
~2-6 atm over each 180-deg sector.
FIELD CONTENT: the imposed azimuthal inlet profile — O(10:1) pressure
ratio within one sector; uniform temperature (3400 K), frozen 2-species
gas, zero inlet swirl.
BEARING: defines the admissible-data-class end-member for T-RED
hypotheses (pure rotating wave, p-only azimuthal structure, no
tangential velocity at inlet); every downstream helical/tangential
feature in this paper is generated INSIDE the nozzle domain by the
rotating footprint — clean carrier for the reduction-residual notion.
ADVISORY.

### H21-F12 — Fig. 12, journal p. 667 (PDF p. 8)
Instantaneous P (annulus/chamber inner surfaces) + Mach (cross plane)
contours, NOZZLELESS geometry, detonation-wave case. One of the two
high-pressure waves visible in rotation around the annulus; plume Mach
structure 0-3.4; entire base region subatmospheric (text: area-averaged
base pressure 0.59 atm vs 0.95 atm for constant-pressure inflow —
approximately eightfold base-drag increase).
BEARING: channel (v) base-pressure model-form (R8 two-regime, the
nozzleless->plug ANALOGY leg): the rotating wave changes the base-flow
regime itself, not just its average level. ADVISORY.

### H21-F13 — Fig. 13, journal p. 667 (PDF p. 8)
Cycle-averaged base surface pressure vs radius, CFD detonation-wave
(dashed) vs CFD constant-pressure (solid) vs 5 experimental tests.
Detonation-wave curve ~0.55-0.8 atm, flat; constant-pressure curve up
to ~1.2 atm near centerline; experiments follow the detonation-wave
curve.
BEARING: channel (iv)/(v): a cycle-averaged 2D-per-phase surrogate
built on constant-pressure closure would mispredict base pressure by
~30-50% of ambient — an experimentally refereed CYCLE-MEAN datum (mean
level only; no per-phase discrimination). ADVISORY.

### H21-F14 — Fig. 14, journal p. 668 (PDF p. 9)
Cross-sectional Mach (left) + pressure (right) at ONE azimuthal
location at t0, +25 us, +50 us, nozzleless detonation-wave case.
Cyclic formation/reformation of an oblique-normal shock system in the
plume: barrel shock at t0 -> barrel + normal shock at +50 us -> back to
oblique at cycle start; wave-peak location marches axially in the
pressure panels; text: period of the detonation-induced pressure wave
faster than base-region adjustment time, so the base NEVER reaches the
steady condition.
BEARING: channels (i)+(ii) jointly: at fixed azimuth the front
topology is PHASE-DEPENDENT (normal<->oblique) — an interior front
segment class that a per-phase steady 2D slice can represent only if
the phase family carries topology change; candidate content for the
residual operator's front-segment terms and for the G3/corrector
boundary statement. ADVISORY.

### H21-F15 — Fig. 15, journal p. 668 (PDF p. 9)
Same cross-section, CONSTANT-pressure case, t0 and +80 us: a single
barrel shock, quasi-steady (~7400 Hz weak oscillation only), no
normal-shock replenishment.
BEARING: the counterfactual field: removing the rotating wave removes
the cyclic shock-topology change — isolates channel (i)/(ii) content
from geometry effects. ADVISORY.

### H21-F16 — Fig. 16, journal p. 668 (PDF p. 9)
Area-averaged base pressure vs mass flow, experiment vs Stechmann
analytical model: model adequate midrange, deviates at low/high mass
flow.
BEARING: channel (v): the only published analytic base-pressure
closure fails outside midrange — bounds the model-form bar for any
base-pressure term in the reduced functional. ADVISORY.

### H21-F17 — Fig. 17, journal p. 669 (PDF p. 10)
Normalized base pressure Pb/Pc vs NPR, nozzleless: open-wake ->
closed-wake transition at NPR ~ 6.7; open-wake base pressures BELOW
ambient (unlike constant-pressure aerospike literature where Pb ~ Pa)
— RDE ejector action suctions the base even in open wake.
BEARING: channel (v) R8 two-regime bar DIRECTLY: regime boundary
(NPR~6.7) + the sign of the RDE departure from constant-pressure
aerospike closure in the open-wake branch. ADVISORY.

### H21-F18 — Fig. 18, journal p. 669 (PDF p. 10) — **EXHIBIT OF RECORD** (read carefully)
Instantaneous field, IE-AEROSPIKE, detonation-wave case: pressure
contours on chamber inner surface + plug wall (P 0.3-6.8 atm), Mach on
cross plane (0-2.6), particle flow paths as solid black lines on the
plug, gray iso-volumes = REVERSE flow (negative axial velocity) at the
end of the plug.
FAITHFUL READING: (a) the particle paths on the plug are visibly
HELICAL — they wind azimuthally while descending the ramp, with the
winding sense set by the rotating oblique-shock footprint (single
rotation direction; pitch not quantified in figure or caption, but the
paths cross a large azimuthal arc over the plug length near the wave
and straighten between waves); (b) the high-pressure footprint on the
plug is a single azimuthally-localized band spiraling from the cowl
lip toward the plug tip; (c) the gray separated/reverse-flow region at
the aft plug is NON-AXISYMMETRIC — a lobed, azimuthally-localized
volume ("The separated flow region for the RDE had a complex geometry,
contrary to the axisymmetric separated flow region geometry expected
for a constant-pressure engine" — authors' words, same page).
BEARING (the phenomenon class T-RED must carry, per the brief):
(1) helical characteristic paths = azimuthal transport terms dropped
by the per-phase-2D reduction (channel (ii) core); (2) the
azimuthally-localized separated region is FED azimuthally by the
rotating footprint — this is the data-anchored-shadow pin instance
(swirl5f dispatch §3 row 13: azimuthally-fed interior front/separation
segments unreachable by the axial march); (3) separation geometry is a
DESIGN-relevant surface-load feature, so its non-axisymmetry bears on
the OPTIMUM-SHIFT channel (vi): the reduced functional sees an
axisymmetric separation surrogate while the true design response
includes the lobed structure. ADVISORY.

### H21-F19 — Fig. 19, journal p. 670 (PDF p. 11)
Cycle-averaged plug surface pressure vs axial distance,
detonation-wave (dashed) vs constant-pressure (solid) CFD vs 3
experiments (tests 69/70/77). Three features (text, same page):
recompression x~0.7-3.0 cm shared; detonation-wave pressures LOWER up
to end of recompression (confirmed by experiment); at x~7.0 cm the
constant-pressure case separates (pressure rise) while the
detonation-wave cycle-average stays attached further downstream —
mechanism (text): the 72-us re-energization of the boundary layer by
the rotating wave prevents steady-state boundary-layer growth and
delays separation.
BEARING: channels (iv)+(v): an UNSTEADY-3D mechanism (periodic BL
re-energization) shifts a cycle-MEAN observable (separation onset) —
i.e. the mean field itself is not reachable from any steady 2D closure
with standard separation criteria; also the sharpest published
instance of an azimuthal/unsteady term changing a design-relevant
surface integral. ADVISORY.

### H21-F20 — Fig. 20, journal p. 670 (PDF p. 11)
Cross-sectional Mach + pressure, IE-aerospike, t0/+25/+50 us at one
azimuth: labeled flow-separation location MOVES upstream (t0->+25 us,
as incoming pressure decays) then is pushed back downstream (+50 us,
next wave peak exhausting over the plug); wave-peak trace in pressure
panels.
BEARING: channel (i)+(ii): separation point oscillates WITH the wave
phase at fixed azimuth == a rotating (helical) separation-line in the
lab frame; per-phase 2D slices carry a phase-indexed separation
location, and T-RED's residual must say what of the azimuthal feeding
between neighboring phases is dropped. ADVISORY.

### H21-F21 — Fig. 21, journal p. 671 (PDF p. 12) — context (non-field, kept for channel (iv))
C_F vs NPR per surface (IE/flared, plug/cowl) from axisymmetric
constant-pressure computations across the cycle's pressure ratios;
text: quasi-cycle-averaged C_F ~ 1.25 for BOTH IE and flared — "these
simulations were two-dimensional and averaged... did not account for
the difference that a fully three-dimensional detonation-wave inflow
would have" (authors' words).
BEARING: this is the 1.25-flat NON-DISCRIMINATION datum verbatim at
source (addendum C4 item (c)): the literature's only per-design
unsteady-adjacent c_F number is itself a 2D-averaged construction —
it cannot referee the 2D-per-phase vs 3D-unsteady gap. Channel (iv)
header note of the FORCHETTA table. ADVISORY.

### H21-F22 — Fig. 22, journal p. 671 (PDF p. 12)
Experimental paired-test normalized plug surface pressures (IE vs
flared) at low/mid/high chamber pressure: IE plug holds ~0.20-0.27
normalized pressure to x~3.5 cm then drops; flared drops almost
immediately after cowl exit; separation on flared by x~5 cm (low/mid).
BEARING: experimental referee EXISTS for cycle-mean surface-pressure
PROFILES (usable by M-RED as an anchor family), but again mean-level
only — no phase-resolved surface data anywhere in the corpus. Channel
(iv) provenance note. ADVISORY.

---

## 2. PAXSON-MIKI 2022 (AIAA, RDRE nozzle CFD optimization) — THE WORST-DIRECTION-MARKER PAPER

Q2D annulus solution (detonation frame, CPG, 2 waves) mapped as
rotating unsteady inlet BC (assumed RADIALLY UNIFORM) onto 3D unsteady
frozen-species RANS (OpenNCC) of the shrouded-plug nozzle; ~4M cells,
15 wave revolutions to limit cycle.

### PM22-F2 — Fig. 2, PDF p. 4
Unwrapped Q2D temperature contours (x = circumference, y = axial,
annulus depth y in 0-0.15): two detonation fronts with trailing
oblique shocks crossing the FULL axial extent of the annulus to the
exit plane; fresh-gas triangles; T/Tm up to ~20.
BEARING: the annulus hands the nozzle an inlet state whose azimuthal
structure includes shock DISCONTINUITIES, not smooth modulation —
T-RED hypothesis list must admit piecewise-smooth data with moving
discontinuities (front-segment terms), not only Fourier-smooth
profiles. ADVISORY.

### PM22-F3 — Fig. 3, PDF p. 5
Circumferential exit-plane (== nozzle-inlet) distributions at a moment
in time: p/Pm ~ 0.33 to ~2.1 (~6:1), T/Tm ~ 9.5 to ~16.5, Mach
(axial+circumferential) ~1.1 to ~1.4 with sharp jumps at the two
oblique-shock crossings; text same page: standard deviations of the
fluid state ~70% of the means.
BEARING: QUANTIFIED azimuthal nonuniformity magnitude of the
admissible inlet class (channel (ii) hypothesis constants; also
FORCHETTA provenance for how large the azimuthal terms are BEFORE any
reduction bound is applied). Mach never subsonic here (1.1-1.4) but
close to 1 — feeds the G-c near-sonic caution. ADVISORY.

### PM22-F5 — Fig. 5, PDF p. 6
Instantaneous pressure (log scale, p/pamb 0.55-46.5), baseline nozzle
at limit cycle: upper contour = mid-annulus axial/circumferential
surface; lower three = radial/circumferential cross-sections at three
axial stations.
FAITHFUL READING: (a) the two oblique shocks originating at the
detonations propagate through the FULL LENGTH of the nozzle (helical
footprint persisting to the exit), weakening considerably in the
expanding section; (b) the cross-sections show the waves transitioning
from RADIALLY UNIFORM near the inlet to RADIALLY DISTORTED (S-shaped
spiral arms in the annular sections) downstream; authors verbatim: "It
is not clear why this occurs or what impact it has on performance.
Further investigation is warranted"; (c) same passage: "the
fundamentally unsteady, multi-dimensional phenomena associated with
RDRE flow fields require the 3D CFD analysis... to accurately assess
performance".
BEARING: channel (ii) core: the residual operator cannot assume axial
decay of azimuthal structure inside the nozzle (it survives to the
exit), AND a radial-azimuthal coupling term exists that even the
source authors do not explain — a named hypothesis-risk line for
T-RED (any radial-uniformity reduction inside the nozzle is
data-contradicted downstream). ADVISORY.

### PM22-F6 — Fig. 6, PDF p. 7
TIME-AVERAGED pressure (0.33-20.7 p/pamb) and Mach (0.01-3.12)
contours, baseline: smooth, attached everywhere except small
plug-tip region; most thrust from the initial expansion region near
the plug outer diameter.
BEARING: channel (iv): the time-averaged FIELD is well-behaved and
looks like a steady nozzle solution — value-level averaging adequacy
is visually plausible while Figs 5/11 show the instantaneous truth;
the pair (F5,F6) is the canonical value-vs-structure contrast for the
FORCHETTA header. ADVISORY.

### PM22-F7/F8 — Figs. 7-8, PDF pp. 7-8 (design-line context, non-field)
Area-ratio series V1-V4 (Ash/Ae also drifting): nozzle thrust 58.1%
of ideal at baseline Ae/Ach=5 -> ~65% near Ae/Ach=6.5 (~7%
improvement), coinciding with near-perfect expansion ON A TIME-AVERAGED
BASIS; steady 1D pre-design analysis had already put the baseline
within 4% of ideal specific thrust (31% area-ratio mismatch <-> ~4%
thrust).
BEARING: channel (iv) sizing leg of record (the ~1%-class area-ratio
agreement family): along the AREA-RATIO design direction the averaged
description ranks correctly. ADVISORY.

### PM22-F9/F10 — Figs. 9-10, PDF p. 9 (design-line context, non-field) — **WORST-DIRECTION MARKER**
Shroud series V1,V5,V6,V7 at FIXED Ae/Ach=5, Ash/Ae = 0 -> 0.66:
nozzle thrust 58.1% -> ~71.5-72% of ideal (V7 +13.4% over baseline);
text verbatim: "the well-known direct relationship between area and
pressure expansion ratio is based on uniform, steady flow. This flow
field is neither"; thrust production migrates from the plug surface to
the shroud inner surface; "An observation is not an explanation
however, and more study is needed"; recommended V5 (58.1->~70%,
1.5% below best, smaller diameter).
BEARING: channel (vi) OPTIMUM-SHIFT empirical marker MANDATED for the
FORCHETTA table: a design direction (shroud split at fixed area ratio)
whose thrust response (~13%) EXCEEDS the entire area-ratio design line
(~7%) and is not predicted by any steady/uniform closure — the
registered swirl-breaker candidate; also the concrete instance of
|argmax shift| along a direction the reduced functional under-weighs.
ADVISORY.

### PM22-F11 — Fig. 11, PDF p. 10
Instantaneous pressure contours, OPTIMIZED V5 nozzle at limit cycle
(same layout as F5): same two-armed helical shock footprint through
the full (shroud-extended) nozzle; radial distortion of the wave
fronts again visible in the annular cross-sections; text: flow "highly
unsteady and spatially non-uniform throughout the nozzle interior"
yet time-averaged flow attached and well-behaved (Fig. 12, not
re-rendered); grid-refinement note same page: 2x cells -> total thrust
within 0.4%.
BEARING: the azimuthal structure PERSISTS at the optimizer's chosen
design — the residual operator is not driven to zero by the
optimization; grid-doubling invariance (0.4%) certifies the 3D datum
class against numerical-noise objections (provenance strength note for
FORCHETTA cells citing this paper). ADVISORY.

---

## 3. KAEMMING-PAXSON 2018 (EAP paper) — INLET-CLASS QUANTIFIERS

### KP18-F1 — Fig. 1, PDF p. 3
Unwrapped RDE CFD (detonation frame, H2/air, 4 atm feed): T/Tref
(1-11) with white particle paths, Log(P/Pref) (0-1.5+), and AXIAL Mach
Mx (0 to >1) in (circumference, axial) space; detonation + oblique
shock reaching the exit plane; text same/facing page: exit static
pressure varies roughly 3:1 azimuthally at >1000 rev/s, exit-plane
temperatures approach an order of magnitude above inflow.
BEARING: channel (ii) hypothesis constants (3:1 p, ~10:1 T azimuthal
variation at the interface); the Mx panel shows the exit plane
containing BOTH subsonic and supersonic patches — the sonic surface is
corrugated and pierces the interface. ADVISORY.

### KP18-F6 — Fig. 6, PDF p. 10
Axial exit-plane Mach vs circumference: Mx ~ 0.85 -> 1.33 with the
supersonic spike just behind the wave and subsonic recovery elsewhere
(A3.1/A3.2=0.6, A8/A3.2=0.8 case).
BEARING: the QUANTIFIED corrugated-sonic-line datum: any T-RED
hypothesis of a uniformly-supersonic (or uniformly-choked) matching
surface is data-contradicted at the combustor exit; directly feeds the
G-c (adjoint near-sonic growth transfer) caution — the near-sonic
region is azimuthally localized and periodic, exactly where adjoint
gradients can amplify. ADVISORY.

---

## 4. MIKI 2020 (AIAA, RDE nozzle design methodology, NPS validation) — WALL-FOOTPRINT FIELDS

Q2D combustor -> unsteady rotating inlet profile -> 3D unsteady
OpenNCC of the NPS "aerospike" nozzle (two waves; ~600k cells; 3-day
turnaround; chemistry off downstream).

### M20-F4 — Fig. 4, PDF p. 6
Q2D unsteady inflow profiles vs azimuth (the mapped nozzle-inlet BC):
total pressure ~4.2e5 -> ~1.75e6 Pa (~4:1) with the oblique shock at
~270 deg; total temperature ~1450-2050 K; THREE velocity components:
one dominant (400-800 m/s) and two oscillating between roughly -300
and +400 m/s, all jumping at the shock crossing.
BEARING: the inlet class carries O(300-400 m/s) in-plane/tangential
velocity content alongside the p,T structure — channels (ii)+(iii):
a p-only or swirl-free interface parameterization discards a velocity
field of the same order as the local sound-speed fraction; also the
concrete inlet-profile-structure entry for T-DISC's fiber
characterization (what the p-only projection forgets). ADVISORY.

### M20-F5 — Fig. 5, PDF p. 7
Instantaneous u-velocity (-100..1500 m/s), Mach (0..2.5), temperature
(500..2200 K), static pressure (8.5e4..1e6 Pa) around the nozzle:
max Mach ~2.5; small recirculation right before the (sharp-edged)
throat; recompression near the nozzle tip; tip recirculation zone.
BEARING: baseline field anatomy for the M-RED anchor family on a
second, independent geometry/code pair (vs Harroun/Loci-CHEM);
channel (iv) provenance breadth. ADVISORY.

### M20-F6 — Fig. 6, PDF p. 7
Instantaneous SURFACE fields on the 3D nozzle: (a) pressure, (b) shear
stress, (c) adiabatic wall temperature.
FAITHFUL READING: a rotating spiral (helical) band is visible on the
plug in all three surface fields — the wall footprint of the two
rotating waves; a distinguished low-shear (blue) region = flow
SEPARATION due to the adverse pressure gradient, azimuthally
structured, not an axisymmetric ring; authors: "a complex distribution
of the shear stress is observed... the steep gradient of the shear
stress related to the complex inflow profiles remains downstream of
the nozzle."
BEARING: channel (ii): independent (second-code) confirmation of the
Harroun Fig. 18 phenomenon class — helical wall footprint +
non-axisymmetric separation; additionally puts the VISCOUS surface
fields (shear, wall temperature) in the dropped-structure inventory,
i.e. the residual operator's trace on the wall involves more than
pressure (model-form (v) contact point for friction/heat-flux terms).
ADVISORY.

### M20-F7 — Fig. 7, PDF p. 7
Instantaneous gauge-pressure iso-surfaces (+/-12000 Pa) of the
exhaust: authors' annotation and text: "There is a SPIRAL propagation
generated by the two rotating detonation waves, and then high- and
low-pressure regions at the tip of the nozzle" — two interleaved
helical pressure sheets (pitch set by 2 waves at the operating
frequency; direction = wave rotation) winding downstream, then
tip-region high/low cells and pressure waves radiating to far field.
BEARING: channel (ii): the helical footprint is not wall-confined — it
is a volumetric two-start helix filling the plume; per-phase 2D
reduction replaces the two-start helix by phase-indexed axisymmetric
sheets; the residual carries the inter-phase (azimuthal-derivative)
coupling of these sheets. ADVISORY.

### M20-F8 — Fig. 8, PDF p. 8
Time series (7 frames, half cycle) of Mach/gauge-p/T near the throat:
strong shock forming at the sharp throat edge when the high-pressure
high-Mach flow enters; choking at throat; expansion at outer-body
corner; text: "The size and the location of the separation bubble
slightly vary over a half cycle."
BEARING: channels (i)+(ii): phase-dependent throat shock + oscillating
separation bubble = the near-throat front-segment content T-RED must
either bound or hand to G3/corrector (time-coupling half); note the
per-phase variation here is described as SLIGHT — a favorable
(BEST-side) datum for the FORCHETTA bracket on this geometry class.
ADVISORY.

### M20-F9 — Fig. 9, PDF p. 9 (integral context, non-field)
Time histories of mass flow (+/-1.5%) and thrust components (PRT ~51,
NZT ~ -7.6, MOT ~441, OBT ~ -0.9 lbf) over the limit cycle: high-freq
oscillation superimposed on low-freq; nozzle-surface contribution
slightly NEGATIVE and few-% of gross thrust; validation vs NPS: Isp
within ~12%, both experiment and CFD agree the nozzle-cone thrust is
negative and few-%.
BEARING: channel (iv): integral outputs fluctuate at the % level while
the fields fluctuate at O(1) — the value-level averaging adequacy
datum on this geometry; ALSO a caution: when the nozzle-surface term
itself is few-% of gross, a few-% residual bound is NOT small relative
to the design-bearing quantity (normalization warning for FORCHETTA
cells). ADVISORY.

### M20-F13 — Fig. 13, PDF p. 12
Time-AVERAGED fields (Ma, T, log p, gauge p) for NPS + Cases 1-5:
design ranking read entirely off averaged fields; Case 4 large
negative-gauge wake (~10% of total thrust as drag), Case 5
recirculation bubble in concave region; Table 3 same page: total
thrust spread 473.7-499.3 lbf (~5%) across designs with component
migration (PRT 91.8 -> -49 lbf, NZT -46.5 -> +35.9 lbf across cases).
BEARING: channel (vi)-adjacent: design DISCRIMINATION at the few-%
level is carried by component terms that swing sign across designs —
the reduced functional must get component-level structure right, not
just totals; provenance for the FORCHETTA statement that ranking
thresholds are ~1-5% class (R26 OPEN). ADVISORY.

---

## 5. HARROUN 2020 (AIAA, simulation + validation companion)

### H20-F3 — Fig. 3, PDF p. 4
Analytic inlet pressure waveform (Eqs. 1-2, Pa units) for Test #53
two-wave detonation at t=0 and t=1/2f — same construction as H21-F11
(30 -> ~2 atm log decay per 180-deg sector); products frozen,
kinetics ignored.
BEARING: same admissible-data-class end-member as H21-F11 (p-only
azimuthal structure, no inlet swirl); included for provenance
completeness of the exhibit chain (2020 methodology -> 2021 fields).
ADVISORY.

NOTE (read-depth honesty): in the rendered pp. 4-10 the 2020 paper
carries NO 3D field contours — its figures are the domain schematic
(Fig. 4, p. 5), hardware/port drawings (Figs. 5-6, p. 6), and
line-plot validation (Figs. 7-11, pp. 7-10: base pressure vs radius,
base pressure vs mass flow, open/closed-wake transition at Pa/Pc ~
0.15, ramp pressure vs axial distance, paired IE/flared normalized
pressures). Field reading for this configuration lives in the 2021
paper (Section 1). The line plots duplicate/anticipate H21-F13/16/17/
19/22 content, including the delay of ramp flow separation under
detonation-wave inflow ("the constantly re-pressurizing flow of the
RDE re-energized the boundary layer at the end of the ramp") and the
explicit statement that 3D transient-BC computations were NOT run for
the flared geometry (2D axisymmetric only) — a coverage gap in the
source corpus itself. ADVISORY.

---

## 6. LIU 2022 (AST 120:107300, kerosene/air RDE + aerospike family A-D)

3D reactive (reduced-mechanism) simulations of the full chamber +
nozzle + plume; Cases: A flat open throat, B flat + constriction
(eps=87.3%), C isentropic full-length aerospike, D 40% truncated.

### L22-F7 — Fig. 7, article p. 7 (PDF p. 7)
Instantaneous 3D fields, flat aerospike: pressure (0-50 atm) on
chamber inner wall + ramp, temperature (200-2600 K) on symmetry plane;
Mach disk flagged in the plume; text: oscillatory inflow makes the
exhaust plume time-varying and NOT symmetric (vs steady supersonic-jet
reference); sudden expansion at chamber exit orients flow radially
outward -> axial-momentum (divergence) loss.
BEARING: channel (ii)+(vi): the azimuthal wave imprints a rotating
high-pressure patch on the ramp (visible as the bright sector), and
the induced radial turning is a THRUST-DIRECTION loss a 2D-per-phase
average can misattribute; third independent code/geometry instance of
the footprint class. ADVISORY.

### L22-F8 — Fig. 8, article p. 8 (PDF p. 8)
Unwrapped chamber fields (r*theta vs z), flat aerospike, Cases A and
B: temperature (800-3200 K) and density-gradient (numerical schlieren)
with labeled detonation front, oblique shock, slip line, deflagration
surface; Case B (constricted throat): a REFLECTED SHOCK WAVE from the
throat travels BACK INTO the chamber (labeled in panel d); text: weak,
does not disturb the rotating detonation.
BEARING: channel (ii) + data-anchored-shadow pin: the nozzle boundary
actively re-injects an azimuthally-structured characteristic (the
reflected helical shock) UPSTREAM into the annulus — an explicit
azimuthally-fed interior front segment crossing the interface in the
wrong-way direction for an axial-march reduction; T-RED's interface
hypothesis list must state whether reflected-family terms are in or
out. ADVISORY.

### L22-F9 — Fig. 9, article p. 8 (PDF p. 8)
TIME-AVERAGED plume fields, flat aerospike A/B: pressure (expansion
fan + Mach disk labeled) and Mach (free-jet boundary labeled), r-z
plane; text: "the averaged solution is the typical configuration of
axisymmetric under-expanded supersonic jets."
BEARING: channel (iv): time averaging restores axisymmetry of the
plume field (value-level adequacy of the averaged description; the
quotient picture's empirical face on a third code). ADVISORY.

### L22-F10/F11 — Figs. 10-11, article p. 9 (PDF p. 9)
Instantaneous 3D fields with ISENTROPIC aerospikes (C full, D 40%
truncated) + unwrapped chamber fields for C: same detonation/oblique
shock/slip-line anatomy; with the inward-bent cowl lip the oblique
shock STRIKES THE COWL LIP and reflects UPSTREAM (labeled reflected
shock), same class as Case B's throat reflection; lateral expansion
suppressed, no Mach disks in plume.
BEARING: reinforces the reflected-family interface term (see L22-F8)
now generated by a DESIGN feature (cowl lip) — i.e. the residual
operator's reflected terms are design-dependent, which is exactly what
makes them optimum-shift-relevant (channel (vi)) and not just
value-relevant. ADVISORY.

### L22-F12 — Fig. 12, article p. 9 (PDF p. 9) — **QUANTIFIED AVERAGE-DESIGN MISS**
Time-averaged plume fields, isentropic aerospikes C/D: Prandtl-Meyer
expansion over the ramp, only weak recompression waves (C); lip +
trailing shocks and closed base recirculation (D); text verbatim: at
the nozzle exit plane "the mass-weighted average Mach number is about
2.58, which is slightly less than the designed point, Me = 2.69. This
may be caused by the nonhomogeneous flow at nozzle throat, no exact
Prandtl-Meyer expansion and so on."
BEARING: channel (vi)/(iv) NUMBER: a nozzle designed by
time-averaged 1D isentropic relations, evaluated in the 3D-unsteady
truth, misses its own design point by delta-M ~ 0.11 (2.58 vs 2.69),
with the authors attributing the miss to azimuthal/temporal
nonuniformity of the throat state — a published, quantified instance
of the reduced-design vs true-field gap at the value level on the
design target itself. ADVISORY.

### L22-F13 — Fig. 13, article p. 10 (PDF p. 10)
Time-averaged streamlines (overall + around ramp) B/C/D: B (parallel
shroud) exhaust expands OUTWARD (divergence loss); C streamlines exit
parallel to axis (design intent recovered on average); D parallel with
small closed base recirculation (bubble visible at the truncation
base).
BEARING: channel (iv): the averaged streamline field is the object the
cycle-averaged variational design controls; the B->C contrast shows
the averaged description DOES rank the divergence-loss design
direction correctly (BEST-side datum for the bracket). ADVISORY.

### L22-F15 — Fig. 15, article p. 11 (PDF p. 11)
Ramp surface pressure vs axial position + segmented (16-segment) ramp
thrust distribution, B vs C: Pw highest at chamber exit decaying under
expansion waves; C holds Pw > Pa to z~2.0 cm (B only to 0.72 cm);
F_ramp 7.24 N (B) vs 34.45 N (C); text: "almost all of the F_ramp is
provided by the first 40% of the aerospike"; total thrust 144.11 ->
166.36 N (+15.4%) flat->isentropic at same eps.
BEARING: channel (iv)/(vi) context: the design-bearing surface
integral is concentrated in the first 40% of the plug — precisely the
region where the helical footprint and reflected-shock structures live
(H21-F18, M20-F6, L22-F10) — so azimuthal residual terms are weighted
by the LARGEST thrust-density region, not a tail correction
(normalization datum for FORCHETTA cell weighting). ADVISORY.

---

## 7. TEASLEY 2023 (NASA RDRE state, experimental imagery)

### T23-F18 — Fig 18, PDF p. 14
Experimental high-speed side-profile frames (frame-by-frame) of
NOZZLE wave activity: leading edge of the wave (red arrow) propagating
clockwise around the annulus ON the nozzle, with a resultant shock at
the NOZZLE TIP (blue arrow) rotating with it.
BEARING: channel (ii) EXPERIMENTAL anchor: the rotating wave footprint
survives the full nozzle length to the tip in a real engine (not only
in CFD) — hot-fire visual counterpart of PM22-F5/M20-F7 helical
persistence. ADVISORY (qualitative imagery; no quantitative field).

### T23-F19 — Fig 19, PDF p. 14
High-speed head-on frames, liquid/liquid LOX/LCH4: 2-3 co-rotating
waves visible as bright arcs; text: instances of counter-propagation
transitioning back, direction switching several times within a single
hot fire.
BEARING: hypothesis-scope datum for T-RED: wave NUMBER and rotation
DIRECTION are not fixed parameters of the data class in real
operation — the residual operator's helical pitch/direction enter as
(piecewise-constant-in-time) parameters, and the periodic-rotating-
wave pin (monitor T0) is an idealization the atlas must flag at its
boundary. ADVISORY.

### T23-F23/F24 — Figs 23-24, PDF p. 16
IR plume imaging, hydrogen (test 007) and methane (test 028) at three
throttle points: under-expanded shock halos at low pc; shock anchoring
at the plug tip at 150-170 psia; text + image: a "bulge" of rapidly
expanding gases RIGHT AT THE COWL EXIT plane, insignificant at low
pressure, clearly shown at high pressure (asymmetric bright annular
lobes visible in the frames).
BEARING: channel (ii)/(iv): experimentally visible azimuthal/annular
nonuniformity of the near-cowl expansion at high chamber pressure —
the regime where the FORCHETTA's worst column should sit; also a
candidate observable for M-RED's data-anchored shadow (the bulge is a
cycle-visible structure at the interface region). ADVISORY.

---

## 8. WOLANSKI 2013 (Proc. Combust. Inst. 34:125-158, survey) — CHAMBER-SIDE 3D STRUCTURE

### W13-F44 — Fig. 44, journal p. 147 (PDF p. 23)
2D CRD structure (unwrapped): temperature-class contour with labeled
detonation front, contact surface, burnt gas, expansion fan, shock
wave; computational "soot print"; velocity vectors in LAB frame; text
verbatim: "although the detonation is rotational, flow of the products
from the CRD chamber is basically axial, so in RDE there will be very
little loss of energy for the rotational component of the flow."
BEARING: channel (iii): the survey's published claim that
product-flow rotationality is energetically small — corpus-side
support for the 3-6% swirl-energy class already of record (cite as
claim, not proof; the claim is 2D-derived). ADVISORY.

### W13-F45 — Fig. 45, journal p. 148 (PDF p. 24)
3D surface pressure + temperature of TWO detonation heads propagating
in a cylindrical (annular) chamber: each head an azimuthally-localized
band with helical trailing structure on the cylinder surface.
BEARING: channel (ii): baseline visual of the two-start helical
source structure entering any attached nozzle. ADVISORY.

### W13-F46 — Fig. 46, journal p. 148 (PDF p. 24)
Chamber DEPTH influence, three channel thicknesses (4, 10, 14 mm),
p/p0 surfaces: with small depth the front is radially uniform; as
depth grows the front visibly curves/distorts radially; text: "When
the chamber depth is greater, the radial dimensional phenomenon is
more and more evident... transverse detonation wave structure in the
radial direction is becoming more noticeable."
BEARING: names the validity boundary of the thin-annulus
(radially-uniform) hypothesis that most reduction chains (and the
Q2D->3D mappings of PM22/M20) assume at the interface — a T-RED
hypothesis-list line with a published breakdown direction (large
channel depth), and the chamber-side cousin of PM22-F5's unexplained
in-nozzle radial distortion. ADVISORY.

### W13-F47 — Fig. 47, journal p. 148 (PDF p. 24)
Enlarged 3D numerical schlieren of detonation in a cylindrical channel
(Delta = 5 mm, d = 35 mm): leading shock, transverse shocks,
detonation cells resolved on the front.
BEARING: sub-front-scale structure (transverse waves/cells) exists
below the wave-scale helical structure — T-RED's hypothesis list
should declare it OUT of scope (scale separation) explicitly rather
than silently. ADVISORY.

### W13-F48 — Fig. 48, journal p. 149 (PDF p. 25)
3D CRD structure: (a) six co-rotating heads in a narrow chamber, T
field with fine streak texture; (b) chamber with COMPLEX geometry
(converging outlet section) with streamlines drawn crossing the
contraction — the near-nozzle streamline field remains predominantly
axial with visible azimuthal shear near the heads.
BEARING: channels (ii)/(iii): multi-head operation multiplies the
helical footprint count (pitch scales with wave number — links to
T23-F19 variability); the streamline panel is the survey's only
nozzle-adjacent field and supports "basically axial" mean flow with
localized azimuthal shear. ADVISORY.

---

## 9. SKIPPED PAPERS (one line each, with reason)

- ancourt_2023_adjoint_direct_characteristic_equations.pdf — adjoint/MoC mathematics, no flow-field figures bearing on RDE azimuthal structure.
- janc_2025_differentiable_reacting_solver_adjoint.pdf — differentiable-solver methodology; no RDE nozzle/plug azimuthal field data.
- zahr_persson_2016_time_periodicity_constrained_adjoint.pdf — periodic-adjoint method paper (airfoil-class cases); no RDE fields.
- schotthofer_2024_windowing_unsteady_shapeopt.pdf — windowing/shape-opt methodology; no RDE fields.
- rubino_2018_harmonic_balance_adjoint_periodic_shapeopt.pdf — HB adjoint turbomachinery; no RDE fields.
- giles_pierce_2000_intro_adjoint_design.pdf / giles_pierce_2001_analytic_adjoint_quasi1d_euler.pdf — adjoint theory; no fields in scope.
- kraiko_2001, kraiko_2016, kraiko_tillyaeva_2004, kraiko_tillyaeva_2015 — steady axisymmetric/ideal-flow variational nozzle theory; no unsteady/azimuthal field data.
- hoffman_1987_compressed_truncated_perfect.pdf — steady axisymmetric nozzle contours; out of azimuthal scope.
- sun_2019_rao_contour_thermally_perfect_large_area_ratio.pdf — steady Rao contour computation; out of scope.
- fernandes_2023_moc_shape_optimization_rocket_nozzles.pdf — steady MoC shape opt; out of scope.
- wintenberger_shepherd_2004_thermo_detonation_cycles.pdf — thermodynamic cycle analysis; no field figures.
- ornano_2017_pulsed_detonation_nozzle_shapeopt.pdf — unsteady FIELD figures exist (Fig. 8, axial-velocity/density/Mach time frames) but the model is 2D AXISYMMETRIC pulsed-detonation: zero azimuthal degrees of freedom by construction; bears on channel (i) only, not T-RED's azimuthal scope (caption-sweep verified; pages not rendered).
- nasa_teasley_2025_rdre_development.pdf — programmatic/hardware paper (photos, thrust traces, PSD/spectrograms, nozzle-extension hardware in Fig 11); caption sweep pp. 2-9 found no flow-field figures.
- CF_ASO_Paper_PrePrint.pdf — aerodynamic shape-optimization preprint outside the RDE corpus; no RDE fields.
- literature_addition_nozzle_rde/ (4 PDFs) — EXCLUDED by orchestrator order: owned by the disjoint dedicated deep-read campaign.

---

# MACHINE SUMMARY

FIGURES READ (rendered + faithfully described): 48 distinct figures in
44 atlas entries across 8 papers (grouped double-figure entries counted
once as entries, twice as figures):
- harroun_2021: Figs 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 (journal pp. 666-671 = PDF pp. 7-12; Fig. 18 p. 669/PDF p. 10 = exhibit of record, read carefully) [12 figs / 12 entries]
- paxson_miki_2022: Figs 2, 3, 5, 6, 7/8 (context), 9/10 (context, worst-direction marker), 11 (PDF pp. 3-10) [9 figs / 7 entries]
- kaemming_paxson_2018: Figs 1, 6 (PDF pp. 3, 10) [2 figs / 2 entries]
- miki_2020: Figs 4, 5, 6, 7, 8, 9 (context), 13 (PDF pp. 4-12) [7 figs / 7 entries]
- harroun_2020: Fig 3 + no-field-contours note (PDF pp. 4-10) [1 fig / 1 entry]
- liu_2022: Figs 7, 8, 9, 10/11, 12, 13, 15 (article/PDF pp. 7-11) [8 figs / 7 entries]
- teasley_2023: Figs 18, 19, 23/24 (PDF pp. 14-16) [4 figs / 3 entries]
- wolanski_2013: Figs 44, 45, 46, 47, 48 (journal pp. 147-149 = PDF pp. 23-25) [5 figs / 5 entries]

PAPERS SKIPPED (with reason, see Section 9): ancourt_2023, janc_2025,
zahr_persson_2016, schotthofer_2024, rubino_2018, giles_pierce_2000,
giles_pierce_2001, kraiko_2001, kraiko_2016, kraiko_tillyaeva_2004,
kraiko_tillyaeva_2015, hoffman_1987, sun_2019, fernandes_2023,
wintenberger_shepherd_2004, ornano_2017 (axisymmetric-only fields),
nasa_teasley_2025 (no field figures), CF_ASO_Paper_PrePrint,
literature_addition_nozzle_rde/ (4 PDFs, disjoint campaign).

TOP-5 BEARING STATEMENTS FOR THE T-RED REVISER (all ADVISORY):
1. EXHIBIT CONFIRMED AND TRIPLED: the helical wall footprint +
   NON-axisymmetric, azimuthally-FED separation region appears in
   Harroun 2021 Fig. 18 (Loci/CHEM), Miki 2020 Figs. 6-7 (OpenNCC,
   incl. shear/heat-flux footprint and an explicit two-start spiral
   plume), and Liu 2022 Figs. 7/10 (rhoCentralFoam-class reactive
   code) — three independent codes/geometries; the residual operator's
   phenomenon class is code-independent. Direct instance of the
   data-anchored-shadow pin (azimuthally-fed interior segments).
2. NO AXIAL DECAY ASSUMPTION: Paxson-Miki 2022 Figs. 5/11 show the
   oblique-shock helix persisting through the FULL nozzle length (and
   in the OPTIMIZED design), developing a radial distortion the
   authors explicitly cannot explain; Teasley 2023 Fig 18 shows the
   rotating wave at the nozzle tip in hot fire. T-RED must not assume
   the azimuthal terms decay before the exit plane, and must carry a
   radial-azimuthal coupling hypothesis line. Liu 2022 Figs. 8/11 add
   design-dependent REFLECTED helical shocks traveling upstream across
   the interface (throat constriction, cowl lip) — the reflected
   family must be declared in/out of the interface hypothesis.
3. QUANTIFIED INLET CLASS: azimuthal variation at the combustor-nozzle
   interface is O(1), not perturbative — static p ~3:1 (KP18 Fig 1)
   to ~6:1 (PM22 Fig 3, std dev ~70% of means), total p ~4:1 with
   tangential velocity content +/-300-400 m/s (M20 Fig 4), and a
   CORRUGATED SONIC SURFACE with Mx 0.85-1.33 crossing unity (KP18
   Fig 6) — the near-sonic azimuthally-localized band is exactly the
   G-c (adjoint near-sonic growth) locus; hypothesis constants for
   the bound schema should be anchored to these ranges.
4. OPTIMUM-SHIFT CHANNEL (vi) EVIDENCE, BOTH SIGNS: worst-direction —
   Paxson-Miki shroud migration 58.1% -> ~71.5% of ideal at FIXED
   area ratio (larger than the whole area-ratio line, unexplained by
   steady/uniform closure; mandated FORCHETTA marker); plus a second,
   smaller published value-level miss: Liu 2022 Fig. 12 —
   average-designed isentropic aerospike achieves exit Mach 2.58 vs
   design 2.69, authors attributing the miss to nonhomogeneous throat
   flow. Best-side — the averaged description ranks the area-ratio
   line (~1%-class, PM22 Figs 7-8) and the divergence-loss direction
   (L22 Fig 13) correctly, and per-phase throat-separation variation
   is "slight" on the NPS geometry (M20 Fig 8).
5. AVERAGING LOOKS BENIGN AT VALUE LEVEL EVERYWHERE, AND THAT IS THE
   TRAP: time-averaged fields are smooth/attached/axisymmetric (PM22
   Fig 6, L22 Fig 9) and integral outputs fluctuate only at %-level
   (M20 Fig 9), while cycle-MEAN observables still shift through
   unsteady-3D mechanisms (Harroun Fig 19 separation delay via 72-us
   BL re-energization; Fig 13 base-pressure regime change, open/closed
   wake NPR~6.7 Fig 17) and NO published unsteady c_F discriminates
   2D-per-phase vs 3D truth (Harroun Fig 21's 1.25-flat is itself a
   2D-averaged construction — the non-discrimination datum, addendum
   (c) verbatim). Note also the normalization warning: nozzle-surface
   thrust can be few-% of gross (M20 Fig 9/Table 3), so "few-%"
   residual bounds are NOT small vs the design-bearing term, and the
   thrust density is concentrated in the first ~40% of the plug (L22
   Fig 15) exactly where the footprint lives.

PAPERS NEEDED (may inform T-RED if procured; none blocking):
- Schwer et al. (Harroun 2021 ref [15], NRL): the prior airbreathing
  aerospike base-pressure study whose conclusions CONFLICT with
  Harroun's ("an area demanding more focused study") — bears on the
  R8 base-pressure two-regime bar.
- Humble & Lim RDE test-campaign source document (Purdue tests
  54-87): the only phase-adjacent experimental surface-pressure
  provenance behind H21 Figs 13/19/22.
- Any follow-up to Paxson-Miki 2022 on the unexplained radial
  distortion of in-nozzle waves and the shroud-migration mechanism
  (none in the read corpus).
  CAVEAT: the 4 unread PDFs in literature_addition_nozzle_rde/ (opaque
  filenames) may already cover part of this list — dedup at the
  dedicated campaign's landing before any procurement.
