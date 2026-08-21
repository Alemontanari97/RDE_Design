# THROAT FIELD HARVEST — targeted C4 pass (field at/near the throat and nozzle-entry plane)

Session S-FOUNDATIONS-C4, targeted throat/nozzle-entry harvest (user
order 2026-08-21). LENS (single question): what do published
coupled-chamber CFD fields say about the CLASS of data the nozzle
actually sees at the throat/entry plane — the "interface data" the
per-phase machinery consumes?

RELATION TO THE ATLAS: this file EXTENDS
`FIELD_ATLAS_targeted_c4.md` with the throat-plane lens. Atlas entry
IDs (H21-F*, PM22-F*, KP18-F*, M20-F*, L22-F*, T23-F*, W13-F*) are
cited, never re-described. It also extends the four deep-read dossiers
`NOZZLE_RDE_STUDY_pA/pB/pC/pD_*.md` (P-A Liu 2022, P-B Li-Xu 2023,
P-C Li-Xu 2025, P-D Jourdaine 2019) with the same non-duplication
rule.

EVIDENCE CLASS FOR EVERY ENTRY: **[ADV]** (advisory CFD/figure/text
reading; Teasley imagery = qualitative experimental). CT-6 RULE: no
absolute value in this file is proposed as a band/tolerance input —
every number is a faithful figure-axis or text reading with
provenance, consumed as CLASS / mechanism / SHAPE information only.
Tags: [REP] verbatim text, [FIG] figure-axis reading, [INF] labeled
inference.

DECLARED CONSUMERS (in-file, per artifact-connectedness rule):
1. **CFD-1 reference dossier** — section C (reference-configuration
   guidance, class-compliant vs pathological).
2. **CFD-2 inlet construction** — section B (inlet-profile shape
   inventory for per-phase axisymmetric runs).
3. **T0-flatness monitor calibration** — sections A.4/A.5 rows +
   consolidated verdict (a), thermal-steadiness and p0/T0-statistics
   readings (what flatness can and cannot referee).
4. **C59 scoping** — section D (search-proven gaps = what no
   published CFD reports).

ORCHESTRATION + READ-DEPTH DECLARATION (honest provenance):
harvest executed by the orchestrating agent plus FOUR completed
extraction children (Jourdaine+Liu; Li-Xu 2023+2025; Harroun+Teasley;
Miki/KP18/PM22 — the fourth returned late, after the orchestrator had
already re-executed its coverage directly; both passes are merged
below and agree, with the child adding increments credited in
A.6-A.8). Child readings were
spot-verified against the orchestrator's own renders of the same
pages (Jourdaine pp. 4-6; Liu pp. 6-7; P-B pp. 8-10, 18; P-C
pp. 11-12; H21 pp. 4-5) — no contradiction found. Pages actually
rendered visually, per paper (union of orchestrator + children this
window; atlas-pass renders cited where relied on):
- jourdaine_2019 (literature/): PDF pp. 1-9 of 9 (child, full paper) + pp. 4-6 (orchestrator re-render)
- liu_2022 dupcopy (literature/): PDF pp. 1-12 of 14 (child) + pp. 6-7 (orchestrator re-render); pp. 13-14 refs by text sweep
- li_xu_2023 AST136 (literature/): pp. 8, 9, 10, 11, 20 (child) + pp. 8-10, 18 (orchestrator); full 22-page render of record in NOZZLE_RDE_STUDY_pB
- li_xu_2025 AST158 (literature/): pp. 8-17 (child, incl. Figs 15/16 special re-read pp. 12-13) + pp. 11-12 (orchestrator); full 18-page render of record in NOZZLE_RDE_STUDY_pC
- harroun_2021 (literature_review/): p. 6 (child) + pp. 4-5 (orchestrator) + pp. 7-12 (atlas pass); full text pp. 1-14 swept
- harroun_2020 (literature_review/): text pp. 2-12 swept (child); pp. 4-10 rendered in atlas pass
- miki_2020 (literature_review/): pp. 5-6 (orchestrator) + pp. 6, 7, 8 (child) + pp. 4-12 (atlas pass); child text-sweep all 16 pp.
- kaemming_paxson_2018 (literature_review/): pp. 5-6 (orchestrator) + pp. 3, 6, 10 (child) + pp. 2, 3, 10 (atlas pass); child text pp. 2-14
- paxson_miki_2022 (literature_review/): p. 5 (orchestrator + child) + pp. 3-10 (atlas pass); child text pp. 2-5, 7, 10-11
- teasley_2023 (literature_review/): pp. 20-21 (child) + pp. 14, 16 (atlas pass); text pp. 4, 7, 17, 19, 21-23
- nasa_teasley_2025 (literature_review/): pp. 7-9 (child); text all 10 pages
Plus orchestrator pypdf keyword sweep over all pages of all 11 PDFs
(periodicity/spectra/throat/stagnation/swirl/statistics battery) and
per-child sweeps declared in their reports; absence claims in this
file cite those sweeps.

Lens key (per paper): (1) modal content at/near throat; (2)
periodicity quality; (3) radial/azimuthal entry-plane profiles;
(4) thermal steadiness; (5) throat p0/T0 statistics.

==============================================================================
## A. PER-PAPER HARVEST

### A.1 JOURDAINE 2019 (PCI 37:3443; H2/O2 + H2/air micro-RDE, conic aerospike open vs choked, 3D Euler) — P-D

(1) MODAL: single-mode lock is a MODEL artifact declared by the
authors: "in contrary with experiments, only one detonation wave will
propagate in the annulus regardless of the mixture equivalence ratio
and the mass flow rate" [REP p. 3446]. A 2-wave initialization decays
to 1 wave after 15 cycles on the fine grid; a separately completed
2-wave run persisted >= 68 cycles with "no difference... in terms of
performance" but with mass-flow-injection oscillations; wave
creation/disappearance mechanisms "not fully understood" [REP
p. 3446]. NO spectra/FFT/probe time-history anywhere (search-proven).
(2) PERIODICITY: cycle counts only as above; no limit-cycle
criterion, no repeatability metric, no averaging-window statement
(search-proven). **The choked counter-example (criterion of record
for CFD-1):** "For the choked configuration, the flow is essentially
subsonic in the combustion chamber due to the throat at the exit. The
oblique shock wave generated by the detonation is reflected on the
throat and progresses backward into the engine" [REP p. 3446]; "The
flow inside the combustion chamber is mainly subsonic in the choked
configuration allowing the shock wave to propagate backward in the
channel and interact with the upstream flow" [REP p. 3448]. Open
config: gas "is principally sonic or supersonic before entering the
nozzle" [REP p. 3446]. Chamber time-averaged static pressure +50%
(H2/O2) / +60% (H2/air) under choking [REP pp. 3450-3451] — the
interface data are nozzle-DEPENDENT in this regime.
(3) PROFILES: no radial or azimuthal line profile at any plane; only
Fig. 8 [FIG p. 3449] time-avg p(x) axial: plateau + reflected-shock
compression bump (x~1 mm H2/O2, ~12 mm H2/air) + sharp throat drop
(choked); monotone decay (open). Fig. 9 [FIG p. 3449] instantaneous:
oblique shock + triple point + reflected shock crossing the channel
near the throat — rotating shock-jump class (second exhibit beside
Harroun Fig. 18, already of record P-D dossier). Tangential velocity:
never reported (search-proven). Sonic line: never drawn.
(4) THERMAL: no drift data, no convergence claim; inviscid/adiabatic
model — thermal transients out of model class by construction
(search-proven; CEA ideal stagnation T 14-19% above simulation, level
comparison only [REP p. 3450]).
(5) p0/T0 STATS: chamber-level time-averaged only (P_i from
"time-averaged stagnation values" [REP p. 3450]; Tables 4-5 [FIG]:
P_c open 0.83-0.88 vs choked 1.35-1.40 MPa, H2/air). Nothing AT the
throat; no std dev/range/instantaneous anywhere (search-proven).
BOTH SIGNS: FOR pin — robust single-wave attractor in-model, 95-99%
CJ speed, time-avg efflux axisymmetric (Fig. 4, P-D F-6). AGAINST —
single-mode is declared contrary to experiment; 2-wave state
metastable >= 68 cycles; choked config injects an upstream-running
reflected family through a subsonic chamber (pin-class violation at
the interface).

### A.2 LIU 2022 (AST 120:107300; kerosene/air RDE + aerospike A-D, 3D reactive) — P-A

(1) MODAL: wave count never stated in text; ONE front per unwrapped
snapshot in every case [FIG Figs. 8/11, atlas L22-F8/F10-F11] —
single-mode by figure reading only. Frequency statement generic
("greater than several thousand Hertz" [REP p. 4]). No spectra/FFT,
no probes (search-proven).
(2) PERIODICITY: run = 1500 us, dt 5e-9 s [REP p. 6]; no cycle
count, no limit-cycle statement, no averaging window declared
(search-proven). Reflected shock from throat (B) / cowl lip (C) "is
very weak and does not disturb the stable propagation" [REP p. 7] —
qualitative stability assertion only. No phase averaging of any kind.
(3) PROFILES: **Fig. 6b [FIG p. 6] — the only azimuthal line profile
in the coupled-chamber corpus**: p(theta) along the INLET surface
(r = 1.36 cm, z = 0), Case D: sawtooth — detonation spike ~40 atm
relaxing to ~5-8 atm plateau (axis reading). NOT the throat plane,
but the only quantitative azimuthal shape published. Entry-plane
increment: the top strip (z = 4 cm = chamber exit) of unwrapped
Figs. 8/11 IS the nozzle-entry azimuthal profile — shock-jump +
relaxation class, T banded ~2000-3200 K [FIG]; reflected-shock second
family crosses it upstream in B/C. Radial profiles at throat: none.
Velocity profiles (any component): none; tangential never appears
(nomenclature defines only axial W) (search-proven).
Sonic surface: never drawn; instead the closure ASSERTION "exhaust
flow is congested at nozzle throat... M_t = 1.0" for all cases incl.
throatless Case A [REP pp. 7, 9] (= standing A-L6). Counter-reading
in the same paper: exit Mach 2.58 vs design 2.69 blamed on "the
nonhomogeneous flow at nozzle throat" [REP p. 7]; "The non-uniformity
of exhaust flow at chamber exit on a time slice makes the nozzle
deviate from the design point" [REP p. 12] — the authors NAME the
throat plane as the seat of the miss (atlas L22-F12).
(4) THERMAL: no drift/convergence data (search-proven); wall thermal
BCs never discussed.
(5) p0/T0 STATS: Table 5 [REP p. 10]: throat time-avg STATIC P_t =
4.10/4.82/5.02/5.01 atm (A/B/C/D); chamber P_c RECONSTRUCTED via
isentropic Eq. (14) with asserted M_t = 1.0 (P_c 7.41-9.06 atm vs
P_0 = 8 atm; eta -7.4% to +13.2%). The throat "total pressure" is a
mean-static-times-isentropic-factor construct, not a measured p0. No
T0 at throat; no second moments (search-proven). Interface
design-dependence datum: reflected shocks "block the fuel intake",
m_dot_f 6.17 -> 6.00 g/s A -> D [REP p. 12].

### A.3 LI-XU 2023 (AST 136:108221; H2/air RDE + truncated-spike nozzle family, film cooling) — P-B

(1) MODAL: no spectra/FFT (search-proven, 22/22 pages); wave count
never stated; single wave inferable from Fig. 14 right panels (one
detonation tongue per snapshot) [FIG pp. 9-10] and singular
"fresh-reactant triangle" [REP p. 8].
(2) PERIODICITY: NO time histories at all in the paper; no cycle
count; no averaging window (search-proven). Only "After several
detonation cycles, a typical fresh-reactant triangle and related
shock waves can be formed" [REP p. 8]. Weak indirect steadiness
evidence: the steady-vs-transient C_fx offset ~2.8% is uniform across
truncations <= 60% [REP pp. 10, 20] (of record, pB top5-1).
(3) PROFILES: no radial/azimuthal line profile at throat or entry
plane (search-proven). **The averaging recipe is itself the finding**
[REP p. 8]: "The equivalent steady state is based on the
time-averaged stagnation parameters at the throat that have been
averaged in the spatial scale at each moment" — spatial-average-first,
then time-average: all radial/azimuthal throat structure is collapsed
by construction and never shown. Fig. 14 right [FIG pp. 9-10]:
transient Mach labels ~0.50-1.4 around the entry region (subsonic
patches beside supersonic flow), azimuthally banded T — corrugated
sonic surface [INF]; M=1 surface never plotted. Tangential velocity:
only at the EXIT plane — V_cir 327.5-383.4 m/s on V_x ~1910-2000 m/s
[REP/FIG pp. 18, 20] (= pB swirl datum, eps_theta ~0.17-0.20 [INF],
already of record); nothing upstream of the exit.
(4) THERMAL: no transient/drift statement (search-proven). T0 at
combustor exit: single time-avg value per configuration, 2423 -> 2440
(max, 40% truncation) -> 2407 K [REP pp. 10-11; FIG Fig. 16 right
axis 2400-2450 K] — config-to-config band ~1.4% [INF], NOT a time
drift.
(5) p0/T0 STATS: **Fig. 16 [FIG/REP p. 10]: combustor-exit
time-averaged p_0/p_inf = 59.75 -> 63.49 (monotone with truncation
20 -> 80%) and T_0 as above — the nozzle-entry-plane mean stagnation
data the design consumes; means only, zero statistics** (no std dev/
range/instantaneous — search-proven). EAP adopted from
Kaemming-Paxson [REP p. 8, Eq. (33) PG = EAP/p0 - 1]. Discharge
coefficient psi = 0.9302-0.9411 [REP p. 11], attributed to
boundary-layer blockage/overexpansion/viscosity — the unsteadiness/
nonuniformity share is not decomposed. BOTH-SIGNS interface note:
spike truncation "has no apparent effects on the detonation process"
[REP p. 10] (interface insensitive to THIS design axis; contrast P-C
+3.89% on the axial-retraction axis).

### A.4 LI-XU 2025 (AST 158:109878; adjustable cowl/spike, five fixed states + dynamic actuation) — P-C

(1) MODAL: no spectra/FFT anywhere (search-proven 18/18 pages; all
results figures are time histories/bars/contours — verified
visually). Single wave; "a single cycle of 0.147 ms" [REP p. 12]
(~6.8 kHz [INF]). Wave-count stability strong across the campaign:
Fig. 15(a) [FIG p. 12] shows 5 equal-period von-Neumann spikes for
ALL five geometries with no period offset; Fig. 21(b) [FIG p. 17]
lateral-force direction sweeps 0-360 deg in a clean sawtooth ~7x/ms
EVEN DURING wall actuation; actuation "cannot significantly affect
the propagation velocities of the flow structures" [REP p. 14]. No
mode transition anywhere.
(2) PERIODICITY — **the cleanest published exhibit (Figs 15/16
re-read, special order):** sampling "after a long time segment
(t > 1.1 ms)" with first peaks phase-aligned to dt = 0.02 ms [REP
p. 12] (~7.5 cycles settling [INF]); 5 cycles displayed; cycle-to-
cycle repeatability visually excellent at all 4 stations
(x/L_combust = 0.11, 1.11, 1.56, 2.00) and all 5 geometries — peak
heights, decay shapes, baselines repeat with no drift [FIG pp. 12-13].
Fig. 16 wall points: waveforms are NOT single sawtooths — primary
jump + structured secondary peaks (triple-point + reflected-shock
arrivals [REP p. 12]) — but the multi-peak fine structure repeats
identically: **phase-locked multi-shock structure, single mode**. No
explicit limit-cycle criterion stated (steadiness shown, not
certified). BOTH SIGNS: under actuation the derived scalars degrade
immediately (C_fx swings 0.9068-0.9734 with irregular sub-cycle
content, m_dot "three drastic changes" [REP p. 14; FIG Fig. 20(b)]) —
forced unsteadiness, but it marks how quickly the periodic
idealization erodes off the fixed-geometry manifold.
(3) PROFILES: no radial/azimuthal line profiles at the throat plane
(search-proven). Time-azimuth surrogate (single rotating wave): the
monitoring-point histories ARE the azimuthal shape at their station
[INF]: x/L = 0.11 — von-Neumann spike 3.2-3.6 MPa decaying
exponentially to 0.15 MPa within one cycle [REP p. 12] = jump +
exponential-relaxation class, peak/trough ~20:1 [INF]; axial decay of
the corrugation quantified: peaks 0.5-0.6 MPa (post-throat wall
points) -> < 0.14 MPa (x/L = 1.56) -> < 0.084 MPa (exit); diverging
path "dampen[s] the exit pressure pulse by 87.8% at most" [REP
p. 12]. Wall radial structure: Fig. 11 [FIG p. 10] inner vs outer
time-avg wall p(x) (injection plane 0.48-0.50 MPa; combustor plateau
0.23-0.26 MPa; converging-section reflection maxima; post-internal-
shock maxima 0.10/0.07 MPa [REP p. 11]). **Corrugated sonic surface,
direct textual evidence: "an approximately normal shock wave appears
in the upper converging section" at baseline [REP p. 8]** — one
azimuth carries a normal shock (subsonic pocket) inside the
converging section while the opposite azimuth is shock-free [INF:
azimuthally mixed subsonic/supersonic throat state]. Tangential
velocity: absent; only exit RMSD of flow angle 8.16-14.63 deg
(conflates divergence and swirl — pB/pC definitional caveat stands)
[REP pp. 11, 14].
(4) THERMAL: throat time-avg T0 "remains near 2414 K with a maximum
relative discrepancy of 0.91%" — ACROSS the five configurations, not
a time drift [REP pp. 1, 11, 16]; attributed to the fixed
heat-addition-per-mass of the premixed stoichiometric mixture; walls
adiabatic; no drift trace (search-proven). Indirect: 5-cycle traces
show no baseline creep [FIG].
(5) p0/T0 STATS: **Fig. 12 [FIG/REP p. 11] — the single most
throat-relevant exhibit in the corpus: mass-weighted time-average
TOTAL pressure AND TOTAL temperature AT THE THROAT, per
configuration** — p_0 ~0.474-0.508 MPa (axis 0.46-0.52), T_0
~2395-2425 K (axis 2380-2440); axial retraction of spike or cowl
raises p_0 ~+3.89% [REP pp. 1, 11] = design-dependent interface data
(threat T-C2 of record). Means only: no std dev/range/instantaneous
p0 statistics (search-proven; the only fluctuation numbers are wall
static-pressure PEAK deviations config-to-config: 8.18%/6.49%
(Point 5), 15.08%/11.28% (Point 7) [REP p. 13]).

### A.5 HARROUN 2020/2021 (Purdue/JPP; IE-aerospike + nozzleless, analytic rotating BC — NOT chamber-coupled)

The exhibit papers (atlas Section 1) consume an IMPOSED interface —
their value here is the exact BC contract, i.e. the published
end-member of the admissible-data class:
(1)+(2) BC contract [REP 2021 p. 7, extends H21-F11]: variation ONLY
azimuthal (radially constant); constant T = 3400 K; constant
velocities; "only pressure changed with azimuthal direction and
temporally"; "the incoming flow was not rotating and had no
vorticity"; exactly 2 waves at the experimental 13,800 Hz; frozen
2-species gas (2-species choice = 0.28% thrust error vs 9-species,
Table 2 p. 8). Perfectly periodic and mono-modal BY CONSTRUCTION.
Author-declared fidelity boundaries: detonation fine detail "not
critical to determining the first-order effects" (claim, not
demonstrated); uniform T chosen DELIBERATELY although the upstream
unwrapped-RDE source showed a "complicated, nonuniform temperature
profile post-detonation" [REP p. 7]; future "sensitivity studies
should be conducted" on pressure ratio/frequency — none exists in
either paper [REP p. 13]. BC applied ONE ENGINE DIAMETER (9.86 cm)
upstream of the channel exit on a constant-area annulus with a
slip-wall stabilization section [FIG/REP p. 6] — the throat-plane
field is the CFD-evolved product of a diameter of propagation and is
never separately plotted. Limit cycle: "10 to 15 wave revolutions"
[REP p. 5, dt 0.1 us]; no convergence metric reported.
(3) Entry profiles = Eq. 7 sawtooth (30 -> ~2-6 atm log decay per
180-deg sector; atlas H21-F11/H20-F3); radial flat and swirl-free by
assumption. No sonic/subsonic classification of the imposed inflow,
no characteristic/Riemann discussion, no imposed-velocity value
(deferred to thesis ref [19]) (search-proven).
(4) THERMAL: T fixed forever; adiabatic walls ("omitted for
simplicity") — drift impossible by construction.
(5) p0/T0 STATS: ABSENT at any interface plane; only momentum-level
bookkeeping ("average mass flow rates and speeds of sound were
identical... inflow-plane thrust... similar" [REP p. 10]).
EXPERIMENTAL REFEREE CLASS [REP/FIG 2021 pp. 663-664, Figs 5-7]: all
surface anchors are CTAP — 23-30 cm capillary lines, deliberately
low-pass ("to eliminate temporal variation"), windowed to
steady-state operation — **the experiment CANNOT falsify any
unsteady/phase-resolved content of the BC class; it referees
cycle-means only.** 2020 conclusions: the "relatively simplistic
pressure model... appears to produce results that agree well with the
experiment" (cycle-mean level), while the IE-vs-flared ranking
dichotomy names "the axisymmetric cycle-averaging is too simplistic"
as a candidate explanation [REP 2020 p. 11].

### A.6 MIKI 2020 (AIAA; Q2D combustor -> 3D nozzle, NPS validation)

(1)+(2) The interface is a RECORDED Q2D limit-cycle segment: data
file = "total pressure; total temperature; and velocity components
and species concentration, at each time step"; "The duration of data
collection is long enough for a detonation wave to circumferentially
travel the combustion chamber once. In OpenNCC, the unsteady outflow
profile from Q2D is repeatedly used as the inflow boundary condition,
under the assumption that the limit cycle was achieved during the Q2D
calculation" [REP p. 5] — **exact periodicity is imposed by
periodic replay of one wave transit; the pin's data class is the
paper's working assumption, declared as such.** Q2D validated against
the rig: mass flow, detonation speed, two interior time-avg
pressures correct; gross thrust from throat-exit flow within 15% of
measured [REP p. 5]. 3D runs "each case was run to a limit cycle"
[REP p. 8]; no criterion stated. No spectra/FFT (search-proven).
(3) **Fig. 4 [FIG p. 6, re-read] — the full-state azimuthal
inlet-profile set (the only published one): total pressure ~4.2e5 ->
~1.75e6 Pa (~4:1) with the oblique-shock jump at ~270 deg; total
temperature ~1450-2050 K (~1.4:1); THREE velocity components: one
dominant ~400-800 m/s (through-flow) with a spike at the shock, two
oscillating ~-300..+400 m/s and ~-300..+150 m/s, all jumping at the
shock crossing.** Component provenance (child increment): the paper
never labels u/v/w orientations for Fig. 4, but Fig. 1's data-
conversion box shows the Q2D detonation-frame data as (Pt, Tt, u, v)
— axial + circumferential ONLY, no radial component by construction —
with w introduced at the frame-change step ("Convert data from
detonation to lab. frame -> (Pt, Tt, u, v, w, yi)") [REP p. 3];
consistent reading [INF]: the dominant positive panel = through-flow,
the two sign-changing O(+/-300 m/s) panels = in-plane/tangential
content ("no overall net swirl... there is typically a local
tangential component of velocity at each circumferential location"
[REP p. 2]) — the atlas M20-F4 class reading stands. Shape detail
(child): Tt(theta) is NOT a simple sawtooth — smooth double-lobed
hump (peak ~2050 K near 140 deg, trough ~1450 K, shock jump to ~1900
K). Radial structure: none — radial uniformity is STRUCTURAL in the
source data (made explicit only in PM22's "assumed radially
uniform"). Wave-count tension INTERNAL to the paper (child): Fig. 4
shows exactly ONE front per 360 deg and the collection window is one
circumference transit, yet p. 7 speaks of "the two rotating
detonation waves" (Fig. 7 spiral) and p. 5 calls Q2D "multi-wave" —
unresolved in the source; atlas M20-F7's "pitch set by 2 waves"
carries this caveat. Near-throat phase variation of the separation
bubble "slightly vary over a half cycle" [REP p. 8, atlas M20-F8];
counter-datum: the 3D integrals carry a "high-frequency oscillation
super-imposed on a low-frequency oscillation" [REP p. 8, Fig. 9] —
the low-frequency content is unexplained (mild deviation from pure
single-period phase-locking).
(4) THERMAL: no drift data; chemistry frozen downstream; adiabatic
wall temperature appears only as an instantaneous surface field
(atlas M20-F6).
(5) p0/T0 STATS: the interface p0/T0 are TIME-RESOLVED single-period
functions (Fig. 4), but no statistics (mean/std/range) of them are
published; integral outputs oscillate at the % level (m_dot +/-1.5%,
atlas M20-F9). Decoupling premise stated: "the flow is chocked at the
throat. As a result, the change of the nozzle shape should not
significantly affect the combustor" [REP p. 4].

### A.7 KAEMMING-PAXSON 2018 (EAP paper; unwrapped H2/air RDE CFD, stations 3/3.2/4/8)

(1)+(2) Q2D detonation-frame construction: azimuthal periodic BCs;
inflow with check-valve model; "Rather than specify Vy = 0 (i.e. no
swirl) which is the laboratory or fixed frame condition, the negative
of the detonation speed, Vdet, is prescribed instead. As a result of
this change to the detonation reference frame, the computational
space becomes one where a steady-state solution is possible" [REP
p. 5] — **wave-frame steadiness (= exact lab-frame periodicity) is
the construction, not a measurement.** The scheme is DELIBERATELY
diffusive "to eliminate the highest frequency unsteadiness (e.g.
detonation cells, Kelvin-Helmholtz phenomena)... The result is a
flowfield solution that is invariant with time when converged" [REP
p. 4, child render] — single-mode purity is engineered in. **AND the
published counter-datum: for A3.1/A3.2 = 0.6 = A8/A3.2 "the CFD does
not achieve a converged solution because the mass fluxes and
pressures continue to oscillate... It is not known if this is a CFD
numerical issue or an indication of some true RDE flow instabilities"
[REP p. 8] — a documented configuration where the pure-periodic
(frame-steady) ansatz FAILS to close, inside the very code family
that defines the data class.** Outflow: constant-pressure with
characteristic equations, disregarded when outflow sonic/supersonic,
normal-shock accommodation [REP p. 5]. 6% of throughflow deflagrates,
94% detonates (calibrated split) [REP p. 5].
(3) Entry-plane azimuthal profiles of record: atlas KP18-F1 (3:1 p,
~10:1 T at exit plane) and **KP18-F6 (corrugated sonic line: axial
Mach 0.85 -> 1.33 across circumference — subsonic recovery +
supersonic spike behind the wave)**; "with a non-uniform flow, any
choking condition (i.e. maximum mass flow rate) will have a range of
axial Mach numbers... typically will contain both subsonic and
supersonic portions" [REP p. 10] — the "effectively choked"
corrugated-throat concept, verbatim. Shape detail (child re-render of
Fig. 6): the sonic line is crossed TWICE per cycle — near-unity
plateau ~1.01, dip to ~0.96 ahead of the wave, jump to 1.33, smooth
relaxation through M=1 down to a BROAD ~0.85 minimum; the supersonic
patch is the narrow post-shock relaxation tail. Radial dimension
absent (Q2D). Averaging semantics [REP p. 6]: Table-1 "Avg" = simple
area-weighted average, "equivalent to a time-average in this frame of
reference".
(4) THERMAL: exit-plane T ratios order-10 azimuthally; no thermal
transients (CPG, frame-steady).
(5) **p0/T0 STATISTICS — THE published quantitative set (Table 1
[FIG p. 6], station 8 = throat/exit): Pt8/Pt3 max 4.07 / min 0.67 /
avg 1.43 — (max-min)/avg = 237%; Tt8/Tt3 8.07 / 5.37 / 6.57 — 41%;
M8x 1.33 / 0.86 / 0.99 — 48%; inflow recovery Pt3.2/Pt3 0.85 / 0.64 /
0.74 — 29%.** Fig. 2 [FIG p. 6]: per-cell total-pressure scatter —
station-4 spread ~2.4-16 atm (burned-gas peak 93 atm at 3.2); "total
pressure varies over 200%" [REP p. 5]. **The EAP construction is the
corpus's only published statistical processing of the unsteady throat
state** [REP pp. 4-5]: mass-flux-averaged ideal axial exit velocity
(1572 m/s in the example) + mass-flux-averaged total temperature
(2080 K) + total-energy conservation including non-axial energy ->
equivalent static T -> EAPi (87.9 psia = 6.0 atm = 49% gain in the
example). Explicit warning that naive statistics mislead: CFD
mass-flux-averaged and momentum-flux-averaged total pressures
"significantly higher" than EAPi (area/time-averaged Pt ~ EAPi);
combustor-exit static + M8x=1 reconstruction "significantly lower"
[REP p. 13, Fig. 11] — i.e. **the choice of averaging operator on the
throat state is itself a first-order modeling decision, with a
published ORDERING** (bears on T-DISC/M-RED interface definitions and
on P-A's Eq.-(14)-style reconstructions). **Swirl-weight pin (child,
channel (iii)): EAPi deliberately EXCLUDES non-axial kinetic energy;
including it (eq. 9) raises EAPi by 6% (CFD baseline) / +3%
(experimental counterpart)** [REP pp. 7, 11] — the published
quantification of tangential-content weight inside a throat
total-pressure statistic, consistent with the 3-6% swirl-energy class
of record (W13-F44 note). Experimental-EAP construction [REP pp.
10-11, 14]: from measured gross thrust with an assumed uniform
M8x = 1 (justified as the minimum/conservative choice, error < 5.4%
over the observed Mach range; degrades to ~15% under-prediction when
the exit is substantially subsonic, M8x ~ 0.5, low-loss-inlet
cases); over 28 CFD cases EAP tracks EAPi from below, 25 cases within
1.7-8.7%.

### A.8 PAXSON-MIKI 2022 (AIAA; Q2D -> 3D shrouded plug, optimization) 

(1)+(2) Q2D: "Two waves are assumed present in the solution" [REP
p. 4] — mode number is an input. Mapped exit distribution used as
"unsteady (but periodic) inlet boundary condition"; "The inlet flow
was assumed radially uniform" [REP p. 5]. **The corpus's only
explicit limit-cycle criterion: the simulation "was run until a limit
cycle formed in the nozzle exit plane mass flow rate, the cycle
averaged thrust remained constant, and the cycle averaged mass flow
rates into and out of the nozzle matched"; ~15 wave revolutions**
[REP p. 5] (30 days on 480 cores for the V5 case [REP p. 10]). No
spectra/FFT (search-proven).
(3) Entry-plane profiles: atlas PM22-F3 of record (p/Pm 0.33-2.1,
T/Tm 9.5-16.5, M 1.1-1.4 with two shock jumps); verbatim frame:
"large spatial fluctuations... large temporal fluctuations as well"
(rotating at 7,557 ft/s) [REP p. 5]. **Interface-placement
quantifier (new): the nozzle domain includes 0.6 in of annulus, so
the BC should have been taken upstream of the exit plane; the states
0.6 in upstream "differed from those of Fig. 3 by less than 6% as
measured by ratios of their standard deviations... the standard
deviations themselves were approximately 70% of the means"** [REP
p. 5] — (i) fluctuation scale ~70% of means AT the entry plane;
(ii) axial drift of the interface distribution over 0.6 in is <6% in
std-dev ratio — a published interface-plane-placement insensitivity
datum. Radial distortion develops INSIDE the nozzle (atlas PM22-F5,
unexplained by authors). Mach never subsonic at this entry (1.1-1.4)
— configuration-dependent contrast with KP18-F6's subsonic patches.
(4) THERMAL: CPG frozen species; no thermal transients; T/Tm ~9.5-
16.5 azimuthal spread instantaneous.
(5) p0/T0 STATS: no p0/T0 table at the interface (the std-dev remark
above is the only second-moment statement; child sweep confirms the
70% figure is not broken out per variable); ideal-thrust referencing
via mass-flux-averaged ideal velocities (KP18-family statistic) [REP
p. 4]; the CEA re-speciation step consumes the TIME-AVERAGED exit
STATIC pressure and temperature (Rg 60.12 -> 71.05 ft-lbf/lbm-R)
[REP p. 4, child]. Semantics note (child): their "cycle time" = the
time for ONE of the two waves to travel the full circumference [REP
p. 7]. Exit-plane time-and-area-averaged pressure = 6 psig, 4.3% of
total thrust [REP p. 7] — value-level averaging-adequacy datum at the
nozzle EXIT, not the interface. Decoupling premise stated at the top:
the chamber "is choked at its exit so that its cyclic behavior is
unaffected by any changes to the nozzle design" [REP p. 1]. Grid
doubling: total thrust within 0.4% (atlas PM22-F11).

### A.9 TEASLEY 2023 + NASA-TEASLEY 2025 (experimental reality check on the data class)

(1) SPECTRA: T23 has NO PSD/FFT figures (search-proven; Figs. 29-30
are scatter plots from HIGH-SPEED CAMERA post-processing: wave
velocity 4000-5000 ft/s, per-wave frequency ~2600-3200 Hz, 2-5
waves). High-speed pressure transducers sit in the propellant
MANIFOLDS on ~3-ft sense lines; chamber pressure = CTAP-class
injector-face ports — **no sensor characterizes the chamber/throat
FIELD spectrally in either paper.** T25 Fig. 10 [FIG p. 8]: far-field
MICROPHONE PSD + spectrogram (fundamental 8.25 kHz, harmonics to ~71
kHz) with the fundamental band essentially unbroken across the full
burn — the corpus's only whole-burn spectral-steadiness exhibit;
acoustic, engine-integrated, not a throat measurement.
(2) PERIODICITY/MODES (extends T23-F19): startup census: 2-4-wave
counter-propagating, 1-5-wave co-rotating, 2-wave SLAPPING modes;
zero longitudinal. Test 026: 4-wave CW -> 3-wave CCW within seconds;
3-wave/3846 Hz -> 2-wave/3850 Hz (per-wave frequency stable ~0.1%
across the count change); throttle step -> 3-wave/2800 Hz; CW<->CCW
"more than a dozen times" in 9 s. Test 028: 3 -> 2 waves with
velocity drop 4230 -> 3520 ft/s coincident with water ingress
(diluent sensitivity). T25: single-wave mode thrust oscillation "in
some cases, an order of magnitude greater than the mean" (destroys
seals/interfaces; multi-mode operation now a design REQUIREMENT);
hydrogen -> pure deflagration above ~250 psia CTAP (fuel-dependent
existence boundary of the rotating-wave class).
(4) THERMAL: T23 explicitly distinguishes "thermal steady state" and
reports wave activity "often only captured at the engine startup and
rarely within the thermal steady state" — **published modal
statistics are startup-weighted by admission; thermally-converged
wave data are sparse.** No T0 measurement at any plane.
(5) p0/T0: chamber-mean CTAP only; "wave parameters were found to be
independent of mean chamber stagnation pressure and mixture ratio"
[REP T23 p. 23]; "no correlation between thrust chamber performance
parameters and wave performance parameters" [REP T23 p. 21] — weak
FOR-side datum (means decoupled from modal content) sitting beside
the mode-ledger AGAINST-side.

==============================================================================
## B. CONSOLIDATED VERDICT

### (a) The pure-periodic single-mode rotating-wave pin AT THE THROAT PLANE — both signs, honestly [all ADV]

FOR (what the published corpus exhibits):
1. **Cleanest direct exhibit: P-C Figs. 15/16** — 5 identical,
   phase-locked cycles at 4 axial stations x 5 geometries, INCLUDING
   repeating multi-shock fine structure; period 0.147 ms invariant
   even under wall actuation (Fig. 21b).
2. **Limit cycles are reached and (once) certified**: PM22's
   three-part criterion (exit-plane m_dot cycle + constant
   cycle-avg thrust + m_dot in=out) at ~15 revolutions; Harroun
   10-15 revolutions (asserted); Miki "each case run to a limit
   cycle"; P-C ~7.5-cycle settling protocol.
3. Wave-frame steadiness is REALIZED in the Q2D constructions (KP18
   detonation-frame steady state; Miki single-period replay) — the
   pin's mathematical form is exactly the field's standard modeling
   idiom for the chamber side.
4. Value-level corroborations: single-wave attractor robust in
   Jourdaine's model; T25 microphone fundamental unbroken across a
   full burn; T23 per-wave frequency stable to ~0.1% within/across a
   mode change; T23 mean-performance decoupling from wave parameters;
   L22/P-D time-averaged efflux axisymmetric.
AGAINST (what the corpus also shows):
1. **Mode number and direction are NOT constants of real operation**
   (T23 mode ledger: 1-5 waves, counter-propagating and slapping
   modes, dozen+ direction flips in 9 s; T25 fuel-dependent
   deflagration takeover; Jourdaine's single mode declared contrary
   to experiment; Tsuboi 2-wave -10% Isp conflict of record P-D
   F-2). The pin idealizes a k-wave state that hot-fire holds only
   piecewise in time — T0-flatness monitor is load-bearing exactly
   here (pin memory: deviation detected BEFORE out-of-scope use).
2. **Upstream-running reflected families cross the interface in 3 of
   the coupled configs** (Jourdaine choked: chamber "mainly
   subsonic", reflected shock into the engine, Pc +50-60%; Liu B/C:
   weak reflected shocks, m_dot_f block; P-C: converging-section
   reflections + one-azimuth normal shock) — interface data are then
   nozzle-DESIGN-dependent (P-C p0 +3.89%), violating the
   fixed-pure-outgoing-wave reading of the pin. Design-dependence
   spans configuration axes non-uniformly (P-B truncation axis:
   insensitive; P-C axial-retraction axis: 3.89%).
3. **Periodicity is exhibited, never spectrally verified**: no
   FFT/PSD of any field/probe quantity exists in ANY of the 9 CFD
   papers (search-proven, Section D) — mode purity at the throat is
   an input (Harroun Eq. 7; PM22 "two waves are assumed"; Miki
   single-period replay; KP18/PM22 Q2D "invariant with time when
   converged" with cells/K-H deliberately diffused away) or a
   figure-inference, never a measured spectrum. **And the ansatz has
   a published failure: KP18's A3.1/A3.2 = 0.6 case never converges
   (persistent mass-flux/pressure oscillation, cause unknown —
   "numerical issue or... true RDE flow instabilities")**; Miki's 3D
   integrals carry unexplained low-frequency content under the wave
   frequency (Fig. 9); Miki also has an internal wave-count tension
   (Fig. 4 one front vs text "two rotating detonation waves").
4. Within-period the throat state is violently structured (sawtooth
   20:1 at combustor station; std devs ~70% of means AT the entry
   plane; Pt spread 237% of avg; corrugated sonic surface with
   subsonic patches KP18-F6/P-B/P-C) — the pin's "pure wave" must be
   read as pure-PERIODIC, not smooth/uniform; harmonic-decay
   regularity of s(xi) (pin memory item 4) must accommodate shock
   discontinuities (atlas PM22-F2 hypothesis line).
5. Experimental phase-resolved verification at the interface DOES NOT
   EXIST (CTAP low-pass by design; camera/microphone integrate the
   engine) — the pin is unfalsified, not validated, by experiment at
   the throat plane.
T0-FLATNESS CALIBRATION NOTE (consumer 3): the corpus supports
time-mean T0 flatness as a natural monitor — P-C throat T0 "near
2414 K" varying <= 0.91% across configurations while p0 moves 3.89%,
and P-B T0 band ~1.4% across truncations [ADV] — but KP18's Tt8/Tt3
spread 41% WITHIN the cycle says the monitor must be a
cycle-mean-flatness (drift) monitor, not an instantaneous-uniformity
monitor; and Miki Fig. 4's T0(theta) 1450-2050 K gives the azimuthal
shape the monitor sees per phase.

### (b) Inlet-profile SHAPES usable for CFD-2 per-phase construction [ADV]

| # | Source (paper, figure) | Quantity | Shape class | Caveats |
|---|---|---|---|---|
| S1 | Harroun 2021 Eq. 7 / Fig. 11 (H21-F11; H20 Eqs. 1-2) | p(theta) | log-decay sawtooth, 30 -> ~2-6 atm per 180-deg sector; p-only, radially flat, swirl-free, T uniform | the analytic end-member; authors flag uniform-T as counterfactual to their own source |
| S2 | Miki 2020 Fig. 4 (M20-F4, re-read) | p0, T0, 3 velocity components vs theta | full-state single-period profile: p0 shock jump ~4.2:1 + sawtooth relaxation; **T0 double-lobed smooth hump 1450-2050 K + shock jump (NOT a sawtooth)**; through-flow plateau ~500-550 m/s + narrow ~800 m/s spike; two in-plane components +/-150-400 m/s multi-lobed, all jumping at the shock | component orientations unlabeled in-paper (Q2D source carries (Pt,Tt,u,v) only — no radial DOF; w introduced at the frame change); radially uniform by construction; the ONLY published full-state interface profile |
| S3 | Paxson-Miki 2022 Fig. 3 (PM22-F3) | p/Pm, T/Tm, M vs circumference | two-shock piecewise-smooth: p 0.33-2.1, T 9.5-16.5, M 1.1-1.4; std devs ~70% of means; <6% std-dev drift over 0.6 in axially | 2-wave case; CPG; radially uniform assumption |
| S4 | KP18 Figs. 1/6 (KP18-F1/F6) | p, T, Mx vs circumference | 3:1 p, ~10:1 T; **corrugated sonic line Mx 0.85 -> 1.33, crossing M=1 TWICE per cycle** (broad subsonic minimum ~0.85, narrow supersonic post-shock tail) | Q2D; the sonic-corrugation shape template |
| S5 | Liu 2022 Fig. 6b (new this file) | p(theta), inlet surface z=0 | sawtooth: ~40 atm spike -> ~5-8 atm plateau | inlet plane, not throat; single snapshot; the only azimuthal LINE profile in a coupled 3D chamber |
| S6 | P-C Fig. 15(a-d) + Fig. 16 (new this file) | p(t) at 4 stations = azimuthal surrogate | jump + exponential relaxation, peak/trough ~20:1 at combustor station; multi-peak phase-locked fine structure post-throat; axial decay law 3.2-3.6 MPa -> <0.084 MPa (87.8% pulse damping) | station histories, wave-frame equivalence [INF]; gives WHERE to place the interface for a target corrugation size |
| S7 | P-B Fig. 16 / P-C Fig. 12 (new this file) | throat time-avg p0, T0 scalars | mean anchors per configuration (p0/p_inf 59.75-63.49; p0 0.474-0.508 MPa; T0 2395-2443 K) | means only; CT-6: anchors for shape normalization, not band inputs |
| S8 | P-B Fig. 24(d) (pB, of record) | V_cir at EXIT plane | tangential content 327.5-383.4 m/s on ~1910-2000 m/s axial | exit not throat; the only tangential line datum in the coupled corpus |
CONSTRUCTION GUIDANCE (mechanism-level): a per-phase family built
from S1 (p-only) and from S2/S3 (full-state) BRACKETS the published
interface class — the delta between them isolates what the p-only
projection forgets (T-DISC fiber content: T0(theta) structure +
O(300-400 m/s) in-plane velocity). S4/S6 set the shape of the
near-sonic corrugation the G-c caution watches. No published radial
profile exists: any radial structure in CFD-2 inlets is modeler's
choice, and should be declared as outside published anchors
(W13-F46 names the thin-annulus breakdown direction).

### (c) CFD-1 reference-configuration guidance [ADV]

CLASS-COMPLIANT (pin-compatible interface, published):
- **Paxson-Miki 2022 baseline/V5**: no physical chamber throat, yet
  entry flow sonic/supersonic at ALL phases (M 1.1-1.4); decoupling
  premise explicit ("choked at its exit so that its cyclic behavior
  is unaffected by any changes to the nozzle design"); the only
  published limit-cycle criterion; grid-doubling 0.4%. The cleanest
  published realization of the fixed-interface data contract.
- **Harroun 2021 IE-aerospike/nozzleless**: interface imposed (not
  coupled) — pin-compliant BY CONSTRUCTION; useful as the
  analytic-BC reference twin, with cycle-mean experimental referee
  (CTAP class only).
- **Miki 2020 NPS**: coupled via recorded Q2D period; choked-throat
  decoupling assumed and thrust-validated within 15%; per-phase
  throat variation "slight" (M20-F8) — a BEST-side reference.
- **P-C fixed-geometry states**: cleanest periodicity exhibit; but
  carries converging-section reflections and design-dependent p0
  (+3.89% axis) — compliant on periodicity, marginal on
  interface-independence.
PATHOLOGICAL (the Jourdaine micro-scale counter-example criterion):
- **Jourdaine 2019 CHOKED config**: hard constriction (eps = 0.8,
  Ae/At 3.47) on a micro-scale chamber (tens-of-N thrust class)
  drives the chamber "essentially subsonic" -> upstream-running
  reflected shock -> interface data nozzle-dependent (Pc +50-60%).
  CRITERION: a reference config for CFD-1 must either (i) keep the
  interface plane sonic/supersonic at all phases (PM22-style), or
  (ii) explicitly price the reflected-family/subsonic-chamber
  coupling as a scope extension (T-1 of record, pD dossier). A
  subsonic-chamber choked micro-RDE is the published counter-example
  to the fixed-interface class — do not pick it as the reference; DO
  keep it as the falsifier configuration.
- **KP18 A3.1/A3.2 = 0.6 non-convergent case**: second falsifier
  class — a LOW-INLET-AREA-RATIO configuration where the
  frame-steady (pure-periodic) solution never closes (persistent
  oscillation, cause undetermined by the authors). CFD-1's
  reference config should stay away from this corner too, and the
  corner is a candidate stress test for the T0-flatness monitor.
- Intermediate: Liu Case B/C (reflected shocks present but "very
  weak", detonation undisturbed; interface shift at the
  m_dot/Pc-percent level) — usable as a sensitivity case between the
  compliant and pathological poles.
OPERATIONAL MONITORS for CFD-1 (from the corpus): (i) phase-resolved
Mach sign on the interface (sonic-surface corrugation: does M_x < 1
anywhere at any phase — KP18-F6 says yes at low contraction, PM22-F3
says no on that config: configuration-dependent, must be measured,
not assumed); (ii) reflected-family strength crossing the interface
upstream; (iii) T0-flatness (cycle-mean drift), per pin memory;
(iv) limit-cycle certificate PM22-style (three-part criterion) rather
than bare revolution counts.

### (d) WHAT NO PUBLISHED CFD REPORTS — search-proven gaps (C59 scoping)

Method: per-paper pypdf keyword sweeps (patterns incl. FFT / spectr /
Fourier / PSD / standard deviation / rms / fluctuat / statistic /
tangential / swirl / circumferential velocity / limit cycle /
converg / thermal / stagnation / total pressure / total temperature /
sonic surface / probe / monitor / time history) over ALL pages of the
11 PDFs, plus the visual renders declared in the header; per-child
sweep batteries declared in their reports.
- G1 **No spectrum of any throat/chamber/nozzle FIELD quantity in any
  of the 9 CFD papers.** Zero FFT/PSD figures; the only spectral
  exhibits in the corpus are experimental and engine-integrated (T25
  far-field microphone; T23 camera-derived scatter). Mode purity at
  the throat has never been published as a spectrum.
- G2 **No radial profile at the throat plane in any paper.** Radial
  uniformity is always an ASSUMPTION (Harroun BC, PM22/Miki mapping)
  — and PM22-F5's in-nozzle radial distortion plus W13-F46's
  depth-dependence show the assumption has a named breakdown
  direction. No paper measures radial structure AT the interface.
- G3 **Throat p0/T0 second-moment statistics exist ONCE** (KP18
  Table 1 max/min/avg; plus PM22's std-dev ratio remark). No coupled
  3D paper publishes std dev/range of throat p0/T0; P-A's throat p0
  is an isentropic reconstruction from mean static; P-B/P-C publish
  configuration means only.
- G4 **No thermal-convergence certificate in any CFD** (fixed-T or
  adiabatic by construction in all 9; T23 says experimental wave data
  at thermal steady state are RARE) — the "thermal steady state
  reached?" question is unanswered corpus-wide.
- G5 **No phase-resolved experimental interface data** (CTAP
  low-pass by design, 23-30 cm capillaries; manifold transducers on
  3-ft sense lines) — the CFD interface class has no experimental
  phase-level referee anywhere.
- G6 **No sensitivity study of nozzle response to interface-class
  perturbations** (Harroun names it as future work; none exists in
  the corpus) — the pin's robustness margin is unpublished.
- G7 **No M=1 surface (sonic surface) plot in any paper** — KP18
  Fig. 6's axial-Mach line is the closest object; corrugation
  topology (surface vs line, radial piercing) is unpublished.
- G8 **No tangential-velocity datum AT the throat plane** in any
  coupled paper (Miki Fig. 4 in-plane components are the interface
  end-member but unlabeled — and the Q2D source has no radial DOF at
  all; P-B's V_cir is at the exit; P-C's RMSD conflates divergence
  and swirl) — channel (iii) constants at the interface remain
  CFD-1's to produce; the only published swirl-weight number inside a
  throat statistic is KP18's +6% non-axial-energy delta on EAPi
  (A.7).
- G9 **No paper verifies its assumed wave count against a multi-mode
  alternative** (PM22 says so explicitly: "If the RDRE chamber
  operates with something other than 2 detonation waves, it is
  unclear how performance will be affected" [REP p. 11]); and the
  PM22 70%-std figure is never broken out per variable (p vs T vs
  M).

### (e) MACHINE SUMMARY

scope: targeted throat/nozzle-entry-plane harvest, 11 PDFs (9 CFD + 2
Teasley experimental), user order 2026-08-21, extends
FIELD_ATLAS_targeted_c4.md + NOZZLE_RDE_STUDY_pA/pB/pC/pD (zero
duplication: atlas/dossier entries cited by ID).
evidence_class: ADV throughout; CT-6 respected (all numbers =
figure/text readings with provenance, none proposed as band inputs).
orchestration: 4 extraction children launched, ALL 4 returned and
were consumed (Jourdaine+Liu; P-B+P-C; Harroun+Teasley; Miki/KP18/
PM22 — returned late, after orchestrator had re-executed its
coverage; both passes merged, in agreement); child readings
spot-verified against orchestrator renders of the same pages (no
contradictions); ~18 pages rendered by orchestrator this window +
child renders as declared; full-corpus keyword sweep run by
orchestrator; child token usage ~111k/119k/110k/102k, orchestrator
consolidation on top.
new_beyond_atlas (top 8):
 1. P-C Figs 15/16: cleanest published periodicity exhibit (5
    phase-locked cycles x 4 stations x 5 geometries, repeating
    multi-shock fine structure; settling ~7.5 cycles; period 0.147 ms
    actuation-invariant).
 2. P-C Fig 12 + P-B Fig 16: the only published throat-plane
    time-mean p0/T0 anchors; T0 config-band <= 0.91% / ~1.4% while p0
    moves 3.89% (T0-flatness monitor support at cycle-mean level).
 3. KP18 Table 1: the only quantified throat p0/T0/Mx statistics
    (Pt spread 237% of avg, Tt 41%, Mx 0.86-1.33) + EAP =
    the corpus's only statistical-processing recipe for the throat
    state, with a published ORDERING of averaging operators
    (mass-flux/momentum-flux high, area/time ~ EAPi,
    static-reconstruction low) and the +6%/+3% non-axial-energy
    swirl-weight pin; PLUS the published failure case of the
    periodic ansatz (A3.1/A3.2 = 0.6 never converges).
 4. Harroun BC contract fully extracted (p-only, radially flat,
    swirl-free, uniform-T deliberately counterfactual, applied 1
    diameter upstream, slip-wall stabilization, no sensitivity study,
    limit cycle asserted without metric) = the published end-member
    of the admissible class + its declared fidelity boundaries.
 5. PM22: only explicit limit-cycle criterion (3-part); std devs ~70%
    of means AT the entry plane with <6% axial drift over 0.6 in
    (interface-placement insensitivity datum); mode number an input
    ("two waves are assumed"). Miki component provenance: Q2D source
    = (Pt,Tt,u,v), no radial DOF, w born at the frame change; T0
    profile double-lobed (not sawtooth); internal wave-count tension;
    unexplained low-frequency content in 3D integrals.
 6. Jourdaine choked-config counter-example criterion sharpened for
    CFD-1 (subsonic chamber + upstream reflected family + Pc +50-60%
    = pathological pole; PM22 = compliant pole; Liu B/C =
    intermediate).
 7. Liu Fig. 6b: the only azimuthal p(theta) LINE profile in a
    coupled 3D chamber (sawtooth ~40 -> 5-8 atm, inlet plane).
 8. Teasley increment: T23 modal statistics are startup-weighted by
    admission (thermal-steady wave data rare); T25 microphone
    fundamental unbroken across a burn; single-wave thrust
    oscillation up to order-of-magnitude of mean; no throat-field
    sensor exists in the experimental corpus.
verdict_(a): pin EXHIBITED (P-C traces, PM22 limit cycle, wave-frame
constructions) but never spectrally verified in any CFD and violated
in real operation on >1 s horizons (mode/direction ledger) and in
subsonic-chamber choked configs (reflected family); within-period
structure is O(1) and shock-bearing — pin reads as pure-PERIODIC,
not smooth; monitor duty confirmed load-bearing.
consumers: CFD-1 (section c), CFD-2 (section b, S1-S8), T0-monitor
(sections a-note, A.4/A.5 rows), C59 (section d, G1-G9).
gaps: G1-G9 search-proven (sweep batteries declared in-file).
output_file: validation/sfoundations_raws_2026-08-13/blocco3/THROAT_FIELD_HARVEST_c4.md (only file written).
