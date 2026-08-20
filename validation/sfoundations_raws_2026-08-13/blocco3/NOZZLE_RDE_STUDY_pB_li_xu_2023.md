# NOZZLE-RDE DEEP STUDY — P-B: Li, Xu, Lv, Lv, Song (NUAA, 2023)

Campaign: BRIEF_nozzle_rde_arrivals_study.md, slot 2 (P-B). Session
S-FOUNDATIONS-C4, 2026-08-20. SHARED RULES accepted: env pinned (nothing
installed); only this file written; every claim page-anchored; evidence
class per statement; figure pages rendered VISUALLY; declared pages;
PAPERS NEEDED section present; authorities of record not re-litigated
(challenges reported as THREAT items with the row's falsifier named).

READ-DEPTH DECLARATION: **[FULL] — all 22 PDF pages read this window**
(printed page number = PDF page number throughout; anchors "p. N" below
are both). Figure pages rendered visually: pp. 2, 4-21 (every figure,
Figs. 1-25). Confrontation frame read first: BRIEF_blocco2_phaseD.md
(CENTERPIECE + forchetta channels (i)-(vi)), BRIEF_blocco2_phaseD_
addendum_c4.md, phaseD/phaseD_r22f_centerpiece.md (all 5 parts),
docs/rde_nozzle_PROGRESS.md BLOCCATO row 9.

EVIDENCE-CLASS KEY (used per statement): [REP] = verbatim text/table
number from the paper; [FIG] = my visual reading of a published figure;
[INF] = my inference from [REP]/[FIG] (labeled, never silent). ALL of
P-B's content is published-CFD evidence = ADVISORY for our program,
never a measurement of ours (SHARED RULES).

==============================================================================
## 1. IDENTITY + METHOD SUMMARY

IDENTITY [REP, p. 1]: Rui Li, Jinglei Xu (corresp.), Haiyin Lv, Dongdong
Lv, Jiazheng Song (State Key Lab. of Mechanics and Control of Aeronautics
and Astronautics Structures + Jiangsu Province Key Lab. of Aerospace
Power System, NUAA, Nanjing), "Numerical investigations of the nozzle
performance for a rocket-based rotating detonation engine with film
cooling", Aerospace Science and Technology 136 (2023) 108221, DOI
10.1016/j.ast.2023.108221. Received 3 Dec 2022, accepted 24 Feb 2023.

SOLVER [REP, p. 3, §2.1]: 3D unsteady RANS with chemical source terms;
one-step Arrhenius kinetics for premixed stoichiometric H2/air (Eq. 5,
parameters from ref. [33]); calorically perfect gas T = p/(R_g rho)
(Eq. 7); total energy with heat release Q and reaction progress beta
(Eq. 6); Sutherland laminar viscosity; k-omega SST turbulence (feasibility
per their ref. [35]); AUSM + MUSCL convection; 2nd-order implicit time
marching; standard wall functions [REP, p. 4].

VERIFICATION [REP, p. 4, §2.2]:
- Aerodynamic: Chutkey et al. annular truncated spike nozzle experiment
  (their [37]); spike by Angelino approximate method, "only retains 20%
  of the total length"; NPR = 60; max relative discrepancy CFD-vs-exp
  4.89% (spike pressures, Fig. 4) and 4.76% (average base pressure vs
  NPR, Fig. 5).
- Thermal: Juhany et al. supersonic film cooling (their [39]); cooling
  effectiveness curves match experiment for M_inj = 1.2 and 1.8 (Fig. 8,
  p. 6).

INDEPENDENCE STUDY [REP, pp. 5, 7, §2.3]: 1D ZND ladder, grids
0.1/0.2/0.4 mm, dt = 1e-7 s with 50 sub-iterations; 0.1-vs-0.2 mm max
discrepancies 0.45% (p) / 0.58% (T); 0.2-vs-0.4 mm: 3.16% / 4.07%
(t = 150 us). Table 2 vs CJ theory: U_D 1965 vs 1972 m/s (0.35%), p_D
1.548 vs 1.532 MPa (1.04%), T_D 2843 vs 2918 K (2.57%). Adopted: 0.2 mm
+ 1e-7 s.

GEOMETRY + BCs [REP, p. 8, §5]: annular combustor inner/outer radii
40/50 mm, combustor length 50 mm; nozzle converging section 5 mm,
diverging section L_cowl = 80 mm; contraction ratio 1.1, expansion ratio
6.2; injection area ratio 10; reactant stagnation 1 MPa, 300 K;
pressure-outlet ambient 6141 Pa (= 19.33 km altitude); ignition zone
T = 2980 K, p = 1.6 MPa. Film cooling: pure-air RADIAL holes, hole area
= circle with D_h = 3 mm, ellipticity a/b in {1.0/1.0, 1.0/1.5, 1.0/2.0,
1.5/1.0, 2.0/1.0}; 5 holes each on inner and outer combustor walls
(dx = 10 mm) + 3 each on nozzle walls; V_sec in {50, 100, 150} m/s,
blowing ratios 0.40/0.68/1.05 (Table 3, p. 7; 15 cases A-O).

CASES [REP, pp. 8-10]: (a) no-cooling truncation sweep DL_spike = 20/40/
60/80% L_cowl, each as a STEADY axisymmetric computation on the
time-averaged inflow AND a TRANSIENT 3D detonation computation (Fig. 14);
(b) film-cooling matrix (5 hole types x 3 velocities) at the fixed
DL_spike = 40% L_cowl nozzle.

TRUNCATION DEFINITION (load-bearing, stated exactly): "L_cowl denotes
the length of the outer nozzle diverging section, and DL_spike represents
the truncated length of the spike" [REP, p. 10] — i.e. DL_spike is the
length REMOVED from the full MoC spike, normalized by the COWL length
(80 mm), NOT by the full spike length. Fig. 14 [FIG, pp. 9-10] confirms:
the spike shortens as DL_spike grows (tip at x ~ 0.115 m at 20%,
~ 0.065 m at 80%). [INF, labeled]: from Fig. 14(a)-(d) tip positions the
full untruncated spike is ~ 80 mm ~ 1.0 L_cowl, so DL_spike = 20/40/60/
80% L_cowl corresponds to RETAINING roughly ~ 80/60/40/20% of the full
spike length — an inference from figure geometry, not a printed number.

==============================================================================
## 2. FINDINGS LEDGER (every result/consideration, with pages)

DESIGN METHOD (§3, pp. 5-8):
F-01 [REP, p. 5]: two design factors: (1) a geometrical throat generating
  choked flow to maintain high chamber pressure; (2) "it is empirically
  recognized that time-averaged stagnation parameters at the combustor
  exits of RDEs can be utilized as the aerodynamic constraints on the RDE
  nozzle design" (their [20,25,41,42]); the time-averaged exhaust
  "behaves similarly to a classic axis-symmetric steady exhaust flow"
  (numerically demonstrated by Jourdaine et al. [22] = our P-D) — hence
  a traditional space-marching steady MoC design "could be employed".
F-02 [REP, pp. 5-6]: axisymmetric MoC: characteristic/compatibility
  Eqs. (8)-(12); unit processes from Zucrow & Hoffman vol. 2 (their [43]).
F-03 [REP, p. 6, §3.2]: maximum-thrust theory: Rao's axisymmetric theory
  + Veen, Gentry & Hoffman shrouded-plug designation method (their [44]),
  under FIXED shroud and spike lengths + constant mass flow; constraint
  system Eqs. (13)-(18) (mass flux across control surfaces ST and KJ,
  thrust integral Eq. 18 includes p_infinity and base-pressure p_b
  terms).
F-04 [REP, pp. 6, 8]: variational solution: left-running control surface
  ST from calculus of variations, phi = theta + alpha, V cos(theta -
  alpha)/cos alpha = C1, r rho V^2 sin^2(theta) tan(alpha) = C2 (Eqs.
  19-21); right-running surface KJ analogous (Eqs. 23-25); corner
  conditions at T with p_infinity (Eq. 22) and at J with AVERAGED BASE
  PRESSURE p_b (Eq. 26); solved by Newton-Raphson on binary nonlinear
  equations. Fig. 13 (p. 8) gives the Zone1/2/3 construction.
F-05 [REP, p. 8, §4]: performance definitions: C_fx = F_actual/F_ideal
  (Eq. 27); discharge coefficient psi = mdot sqrt(T_0,c)/(K p_0,c A_th)
  (Eq. 28); blowing ratio zeta (Eq. 30); cooling effectiveness eta_cool
  (Eq. 31); axial vorticity omega_x (Eq. 32); pressure gain PG =
  EAP/p_0 - 1 with EAP per Kaemming & Paxson (their [45]) (Eq. 33).

NO-COOLING TRUNCATION SWEEP (§5.1, pp. 8-11):
F-06 [REP, p. 8 + FIG p. 9-10]: equivalent steady state built from
  time-averaged stagnation parameters at the throat "averaged in the
  spatial scale at each moment"; steady (left) vs transient (right)
  fields compared at the same instants (Fig. 14).
F-07 [REP, p. 10]: with truncation 20% -> 80%: internal Ma > 3.0 region
  broadens; low-speed recirculation zone enlarges and becomes more
  irregular; at 80% the flow is overexpanded with extra trailing shock
  waves near the spike base; high-temperature zone concentrated near
  triple points and shear layers, "revealing that a big part of reactants
  is still consumed by deflagration".
F-08 [REP, Table 4, p. 10]: time-averaged exit parameters: e.g. 40% case
  p = 6842.1 Pa, V_x = 2019.9 m/s, rho = 0.01722 kg/m^3, gamma = 1.2500;
  40%-case exit pressure lower than 20/60/80% by 3.04/1.78/24.03%; exit
  velocity higher by 1.39/0.88/8.01%; density lower by 4.47/1.51/29.25%.
  gamma across cases 1.2500-1.2515 ("the specific heat ratio changes
  little"); truncation has "no apparent effects on the detonation
  process".
F-09 [REP, p. 10]: under-expansion of the 20% case is severer due to a
  smaller effective expansion ratio (defined approximately by throat
  area, spike base radius, outer exit radius); for DL_spike > 20% the
  practical exit areas are defined only by the outer exit radius.
F-10 [REP, p. 10 + Fig. 15]: STEADY-inflow axial thrust coefficient "is
  not significantly influenced by the length of the truncated spike...
  and is close to 0.9690"; [FIG p. 10] steady curve ~flat 0.965-0.971
  over DL_spike/L_cowl = 0.2-0.8.
F-11 [REP, p. 10 + concl. (1) p. 20]: "When the truncation ratio does
  not exceed 60%, the thrust coefficients of steady cases are
  approximately 2.8% higher than the transient cases, revealing that the
  propagation of the detonation wave and the movement of the induced
  shock wave results in extra flow loss." Conclusion (1): "The
  characteristic method for the steady supersonic flow overestimates the
  axial thrust coefficients of RDEs by approximately 2.8% due to the
  pressure loss caused by the sweeping shock waves and the viscous
  interactions. When the spike truncation ratio exceeds 60%, the
  discrepancy... is significantly enlarged because the flow swirling in
  RDEs induces the trailing shock wave in advance, thereby generating an
  over-expanded flow condition."
F-12 [REP, p. 10]: TRANSIENT truncation dependence: 20% -> 40% gives a
  +0.52% increase in C_fx; 40% -> 80% drops C_fx by 5.78%. [FIG p. 10,
  Fig. 15]: transient curve peaks at 0.4 (~0.9456 per abstract), ~flat
  to 0.6, collapse to ~0.89 at 0.8. Abstract [REP, p. 1]: truncation
  "optimized to DL_spike = 40% L_cowl".
F-13 [REP, pp. 10-11 + Fig. 16]: combustor-exit p_0/p_infinity rises
  monotonically 59.75 -> 63.49 as truncation 20% -> 80%; T_0 rises
  2423 K -> 2440 K (max at 40%) then drops to 2407 K.
F-14 [REP, Table 5, p. 11]: pressure gains PG at DL_spike = 20/40/60/80%:
  -20.67 / -20.12 / -19.68 / -19.70 % (range "-21% ~ -19%"); discharge
  coefficients 0.9410/0.9411/0.9302/0.9400 (range 0.93-0.94).
F-15 [REP, p. 11]: pressure-loss attribution (no-cooling): (a) large
  expansion ratio at the combustor-injection plane inducing over-expanded
  flow; (b) viscous effects magnified by the small scale; (c) boundary-
  layer blocking reducing practical mass flow; (d) spike-truncation
  recirculation zone dissipating kinetic energy. Abstract [REP, p. 1]
  three-part TRANSIENT flow-loss decomposition: (1) pressure loss of
  continuously sweeping shock waves; (2) viscous effect of the flow
  passage; (3) energy dissipation of the base-region recirculation zone.

FILM-COOLING MATRIX (§5.2, pp. 11-19) — secondary bearing, recorded:
F-16 [REP, p. 11]: two combustor holes are immersed in the fresh-reactant
  triangle when detonation height > 1/3 annulus; the second hole distorts
  the reactant/product contact discontinuity; coverage of cold flow
  positively correlates with injection velocity.
F-17 [REP, p. 11 + FIG Figs. 17-18]: hole types a/b <= 1.0/1.0 put
  low-temperature zones on BOTH sides of the hole; a/b >= 1.0/1.0 zones
  deviate toward the trailing/induced shock side; cold-flow coverage
  "bends towards the zone near the induced shock wave" (p. 11) — the
  sweeping wave imprints azimuthal asymmetry on wall films.
F-18 [REP, p. 12 + Fig. 19]: quantitative coverage A_cool,surf (T =
  500-1000 K) 1621.9-3094.3 mm^2 depending on a/b and V_sec; equivalent
  penetration depth in combustor 0.72-1.63 mm; increments at
  x/r_max,combust = 1.7: 308.87/323.77/347.17% for 50/100/150 m/s.
F-19 [REP, pp. 12, 14-15 + Figs. 20-21]: circumferential cooling-
  effectiveness distributions (polar): peaks 0.4-0.8 concentrated near
  the injection holes over ~15-32 deg circumferential angles; away-from-
  wave film covers ~30 deg vs ~15 deg next to the detonation wave
  (asymmetry induced by the rotating wave).
F-20 [REP, p. 14 + Fig. 22]: circumferentially-averaged axial
  effectiveness: FIVE maxima in the combustor and THREE in the diverging
  nozzle (hole stations); at the throat window (x/r_max,combust =
  0.86-1.32) a/b = 1.0/2.0 is 1.15x the other four types.
F-21 [REP, pp. 16-17 + Fig. 23]: axial-vorticity mechanism: radial jet x
  axial mainstream impingement; staggered +/- omega_x pairs; at V_sec =
  150 m/s vorticity enters the mainstream, distorts the outer flowfield,
  and "the effective nozzle expansion ratio significantly decreases".
F-22 [REP, p. 18 + Fig. 24]: exit ensemble averages vs (a/b, V_sec):
  axial velocity ~1903.0-1914.1 m/s; exit T down to 816.1/823.4 K for
  the two named strategies; CIRCUMFERENTIAL VELOCITY V_cir max 383.4 m/s
  (a/b = 1.0/1.5, V_sec = 100), min 327.5 m/s (1.5/1.0, 150); for
  a/b > 1.0/1.0, V_cir = 340-360 m/s "marginally influenced by the
  injection velocity"; hole types a/b < 1.0/1.0 give HIGHER V_cir than
  a/b >= 1.0/1.0.
F-23 [REP, pp. 18-19 + Fig. 25]: with cooling: PG range -22% ~ -24% at
  V_sec = 50; extremes -30.85% (1.0/2.0, 150) and -2.55% (1.0/1.0, 150);
  C_fx 0.940-0.947 for a/b > 1.0/1.0, max 0.9679 (1.0/1.5, 150) —
  coolant pressure-potential energy promotes C_fx for most cases; psi
  global max 0.9522 (1.0/1.0, 100), global min 0.8594 (1.0/2.0, 150).
F-24 [REP, p. 19 + Fig. 25(d)]: RMSD of the flow DEFLECTION angle
  (theta, the meridional MoC flow angle per the p. 2 nomenclature):
  max 18.57 deg (a/b = 1.0/1.5, V_sec = 100); RMSD_theta positively
  correlates with a/b (+22.59% from 1.0/2.0 to 2.0/1.0); "the flat jet
  from the hole type a/b < 1.0/1.0 slows down the flow velocity upstream
  of the nozzle converging section, thereby suppressing the swirling in
  RDEs".
F-25 [REP, p. 1 + p. 20 concl. (4)]: final configuration DL_spike = 40%
  L_cowl, a/b = 1.0/2.0, V_sec = 100 m/s: C_fx = 0.9552, psi = 0.9344,
  PG = -16.48%, RMSD_theta = 14.42 deg; coolant injection reduces psi by
  0.71% but increases C_fx and PG by 1.02% and 18.06%; "the flat jet of
  the hole type a/b < 1.0/1.0 can eliminate the swirling in RDEs in most
  cases" (concl. (2)/(4), p. 20).

==============================================================================
## 3. TOPOLOGY ATLAS (per field figure; what the plot shows; which
##    T-RED term / forchetta channel it informs)

- Fig. 1 (p. 2) [FIG]: PDE/SDE/RDE schematics; RDE panel shows detonation
  wave + oblique shock + shear layer + contact discontinuity rising from
  the wave apex. Informs: the mechanism cartoon behind T-RED's
  advective-helix ray family (channel (ii)); no quantitative content.
- Fig. 3 (p. 4) [FIG]: Mach contours, verification truncated spike at
  NPR 60: inner/outer shear layers bounding the plume, TRAILING SHOCK
  WAVE closing on the axis behind the truncated base; classic closed-wake
  topology. Informs channel (v) base-pressure closure context (R8
  two-regime; this is the steady cold-flow reference topology).
- Fig. 4 (p. 4) + Fig. 5 (p. 5) [FIG/REP]: spike pressure distribution
  (monotone expansion, 4.89% max dev.) and averaged BASE PRESSURE vs NPR
  (P_b/P_0 decays steeply to NPR~30 then flattens ~0.015-0.02 at NPR
  50-70; CFD tracks experiment within 4.76%). Informs channel (v):
  a truncated-PLUG base-pressure dataset (cold-flow, non-RDE) their
  solver reproduces — relevant context for the R8 nozzleless->plug
  ANALOGY (does NOT retire it: cold annular jet rig, not an RDE).
- Fig. 9, 10 (pp. 6-7) [FIG]: ZND structure and grid/time independence
  histories (1D). Method-credibility only; no channel.
- Fig. 11 (p. 7) [FIG]: nozzle grid + cooling-hole layouts; shows the
  five ellipticities. Method only.
- Fig. 12 (p. 7), Fig. 13 (p. 8) [FIG]: MoC characteristic-line
  geometry; truncated-spike construction with zones 1-3, control surfaces
  ST (shroud side, T corner at p_infinity) and KJ (spike side, J corner
  at averaged p_b). Informs: the design-method stage our program's
  variational machinery replaces; direct structural analogue of the
  Rao-class control-surface formulation of record.
- Fig. 14 (pp. 9-10) [FIG — the key topology figure, 4 panels]:
  LEFT (steady, axisymmetric, time-averaged inflow): smooth annular
  expansion, shear layer off the cowl lip, single trailing shock off the
  spike base; larger truncation -> broader Ma > 3 pocket + larger base
  recirculation (dark blue Ma < 0.5 wedge behind base grows from (a) to
  (d)); at 80% extra trailing shocks near the spike base [REP p. 10].
  RIGHT (transient 3D, Mach + T/K surfaces): detonation front visible in
  the annulus (red T ~ 3449 K tongue), OBLIQUE wave descending the
  diverging section, temperature field azimuthally banded (the sweeping
  wave's imprint), high-T ridges along triple points/shear layers;
  deflagrative consumption pockets [REP p. 10]. Informs: channel (ii)
  (the azimuthal structure dropped by a 2D reduction — the sweeping
  oblique wave in the nozzle is the P-B face of the Harroun Fig. 18
  exhibit class, centerpiece §2.3); channel (i) (unsteady wave motion vs
  steady design flow); channel (v) (base recirculation).
- Fig. 15 (p. 10) [FIG — the key performance figure]: C_fx vs
  DL_spike/L_cowl: "Designed Steady Flow" (diamonds) ~flat 0.965-0.971;
  "Simulated Unsteady Flow" (squares) 0.940 -> 0.9456 (0.4) -> ~0.944
  (0.6) -> ~0.888 (0.8). The VERTICAL offset (~2.8%) is the reduction
  gap; the SHAPE difference (flat vs peaked) is an optimum-visibility
  statement. Informs channels (ii), (iv), (vi) directly (see §4/§5).
- Fig. 16 (p. 10) [FIG]: p_0/p_infinity (monotone up) and T_0 (peak at
  0.4) at combustor exit vs truncation — backpressure feedback of the
  nozzle on the combustor. Informs channel (i) boundary (chamber-nozzle
  coupling exists even at fixed operating point; the exit BC is not
  inert) and P-D confrontation (choking raises chamber pressure).
- Figs. 17-18 (pp. 11-13) [FIG]: instantaneous wall-temperature maps
  (outer/inner walls, 3D surface views): finger-like cold-film streaks
  from each hole, BENT AZIMUTHALLY toward the induced shock side;
  cascading low-temperature zones for a/b = 1.0/2.0; streak obliquity =
  visible azimuthal transport at the wall. Informs channel (ii)
  qualitatively (azimuthal advection of wall-adjacent structures by the
  rotating wave system).
- Fig. 19 (p. 14) [FIG]: coverage vs a/b; penetration depth vs x, rising
  sharply in the diverging section (0.72-1.63 mm in combustor,
  ~3-7 mm downstream). Cooling bookkeeping; no channel.
- Figs. 20-21 (pp. 15-16) [FIG]: POLAR plots of eta_cool vs
  circumferential angle at x/r_max,combust = 1.0 and 2.0, inner/outer
  walls: lobed, hole-locked distributions (lobes 15-32 deg), asymmetric
  between wave side and off-wave side. This is measured-in-CFD azimuthal
  NONUNIFORMITY of a scalar at fixed stations. Informs channel (ii)
  (azimuthal structure magnitude at wall stations, ADVISORY).
- Fig. 22 (p. 17) [FIG]: axial eta_cool distributions (circumferentially
  averaged): oscillatory with 5+3 peaks (hole stations), decaying
  downstream of the throat. Cooling bookkeeping.
- Fig. 23 (pp. 18-19) [FIG]: axial-vorticity omega_x fields in the
  meridian plane (range -5.0e4 to +4.8e4 1/s): staggered +/- streamwise
  vortex pairs from each radial jet; at V_sec = 150 the vortical field
  floods the nozzle section. Informs channel (iii) context: streamwise
  vorticity = secondary-flow (swirl-adjacent) content that a
  meridional-plane-only reduction cannot represent; also the mechanism
  by which injection MODIFIES exit swirl (F-22).
- Fig. 24 (p. 20) [FIG]: exit-average maps vs (a/b, V_sec): (a) p/p_ref
  0.88-1.12; (b) T 820-920 K; (c) V_x 1910-2000 m/s; (d) V_cir
  330-380 m/s. Informs channel (iii) NUMERICALLY: V_cir/V_x ~ 0.17-0.20
  [INF from F-22 numbers], exit swirl angle atan(V_cir/V_x) ~ 9.7-11.4
  deg [INF] — inside our B5 10-14 deg band and the DISPATCH §9
  eps_theta = 0.15-0.20 sweep band.
- Fig. 25 (p. 21) [FIG]: performance maps vs (a/b, V_sec): PG -0.30 to
  -0.01; C_fx 0.940-0.965; psi 0.880-0.946; RMSD_theta 14-18 deg.
  Informs channel (iii)/(vi): performance moves by TENS of percent (PG)
  and ~2.5 points (C_fx) along directions (hole ellipticity, injection
  velocity) that are pure 3D/azimuthal mechanisms.

==============================================================================
## 4. CONFRONTATION vs THE DRAFT (per centerpiece part, with anchors)

[T-DISC] (centerpiece Part 1):
- SUPPORTS §1.4(a)+(b) (conviction of p-only, exoneration of full-state
  average): P-B's exit data carry V_cir ~ 327-383 m/s alongside p, T,
  V_x (F-22, Fig. 24) — the swirl content is a real, load-bearing exit
  field of the same order our fiber coordinate sweeps (eps_theta ~
  0.17-0.20 [INF]); a p-only exit description would not distinguish
  configurations whose PG differs by up to 28 points (F-23). One bearing
  sentence: P-B's own exit-average panel is an empirical instance that
  pressure alone underdetermines the exit state at exactly the swirl
  scale [T-DISC-1] postulates (ADVISORY, CFD class).
- DIFFERS (no threat): P-B never poses the projection question; its
  design constraints use time-averaged STAGNATION parameters (F-01),
  i.e. an h0-bearing description, not p-only — consistent with §1.4(b)'s
  exoneration of richer-than-p data.

[T-RED] (centerpiece Part 2):
- SUPPORTS §2.3 (physical exhibit class): Fig. 14 transient panels show
  the rotating oblique wave sweeping the diverging section with
  azimuthally banded temperature — the same phenomenon class as Harroun
  Fig. 18 (the advective-helix ray family), on an INTERNAL
  cowl-plus-spike nozzle. Bearing sentence: P-B independently exhibits
  the sweeping-shock footprint in the nozzle that K's sweep-advective
  rows carry (draft §2.3(a)), at ADVISORY evidence.
- SUPPORTS §2.2 magnitude phrasing ("single-digit % plausible on-ray"):
  the measured steady-vs-transient C_fx gap is ~2.8% uniform for
  truncation <= 60% (F-11) — a published CFD instance of the
  reduction-gap magnitude landing inside the licensed single-digit-%
  band. Bearing sentence: 2.8% is the first same-code steady-averaged vs
  3D-unsteady thrust-coefficient pair in our read corpus, and it sits in
  the band the draft licenses as plausible [SE].
- DIFFERS (definitional, must be carried): P-B's "steady" is a GLOBAL
  time-space-averaged-inflow steady computation, NOT our per-phase
  average; and its 2.8% bundles time-coupling + azimuthal reduction +
  turbulence-model interaction in one number (their own three-part
  decomposition, F-15, is stated but not separately quantified). It
  cannot be read as a measurement of our eps; it is an ADVISORY analogue
  of M-RED leg (A) at coarser averaging.
- THREATENS (mild, channel (vi) — reported per protocol): Fig. 15's
  SHAPE difference (steady flat vs transient peaked at 40% with -5.78%
  at 80%) is an empirical marker of value-adequacy != optimum-adequacy
  along a real design direction (truncation): the averaged functional
  shows ~no gradient where the true functional has structure. This is
  the second empirical marker of the (vi) class after the Paxson-Miki
  shroud line. See THREAT SCAN TH-1.

[M-RED] (centerpiece Part 3):
- SUPPORTS §3.2/§3.5 (the measurement concept): P-B executes, at CFD
  level, exactly the comparison class M-RED formalizes (averaged-input
  prediction vs unsteady truth on the same configuration), and finds a
  stable, small, systematic offset — evidence the protocol's central
  quantity is well-defined and O(single-digit %) on at least one
  configuration family. Bearing sentence: P-B is an external ADVISORY
  anchor point for M-RED band expectations, not a band input (their
  averaging and solver class differ from our certified families).
- DIFFERS: no per-phase decomposition, no (J)/(H) split, no St-sweep —
  none of M-RED's discriminating legs exist in P-B.

[R22-CFD] (centerpiece Part 4):
- SUPPORTS §4.1 CFD-2's cheap-side design: P-B demonstrates the
  feasibility and information yield of exactly the CFD-2 pattern
  (averaged-input steady run vs unsteady run, same code, published
  geometry) — including that the confrontation is readable at
  ~0.5-percent resolution (F-12's +0.52% is resolved by their transient
  campaign). Bearing sentence: P-B lowers the novelty risk of CFD-2's
  method while raising its value (a published comparison exists to
  cross-check against).
- DIFFERS from §4.1 CFD-1: P-B does NOT certify class membership (no
  statement that the wave is a persistent single-mode rotating wave in
  thermal steady state; one-step chemistry; RANS) — CFD-1's premise gap
  stands untouched.

FORCHETTA TABLE (centerpiece Part 5), per channel:
- (i) time-coupling: SUPPORTS the structure of the cell — P-B attributes
  the steady-vs-transient gap to wave propagation + induced shock motion
  (F-11), i.e. a nonzero but small time-coupling+reduction bundle on a
  working configuration; no number for (i) alone is separable. Also
  Fig. 16 shows the nozzle back-reacts on chamber p_0/T_0 with
  truncation — the coupling seam the cell's WORST guards.
- (ii) azimuthal reduction: SUPPORTS BEST-cell phrasing (single-digit %):
  the 2.8% bundled gap (F-11) and the banded transient fields (Fig. 14)
  sit inside the licensed band; nothing in P-B pushes past 10% for
  in-band truncations. The 80% divergence (F-11 tail) shows the gap is
  configuration-dependent and can grow several points when swirl-induced
  early shocks change the flow regime — consistent with the WORST cell's
  refusal to exclude >10% off-ray.
- (iii) swirl: SUPPORTS all three magnitude rows: exit V_cir 327-383 m/s
  on V_x ~ 1910 m/s (F-22) => eps_theta ~ 0.17-0.20 [INF], swirl angle
  ~ 9.7-11.4 deg [INF] (B5 band 10-14 deg, DISPATCH sweep 0.15-0.20);
  "flow swirling in RDEs induces the trailing shock wave in advance"
  (F-11) = a swirl-mediated configuration-scale mechanism, same family
  as the registered swirl-breaker candidate; swirl is SUPPRESSIBLE by
  flat-jet injection (F-24/F-25) — an actuated swirl-breaker instance.
- (iv) averaging adequacy: SUPPORTS BOTH cells, sharply: BEST — the
  2.8% offset is ~UNIFORM for truncation <= 60% (F-11), and a uniform
  offset preserves ranking (the steady design still selects a
  near-optimal truncation among 20-60%); WORST — the offset is NOT
  uniform beyond 60% (ranking breaks at regime change), and the
  transient-only +0.52% (F-12) is exactly the in-class delta scale
  (compare our +0.51% in-class, draft channel (iv) WORST cell) that the
  flat steady curve does NOT resolve. Bearing sentence: P-B gives both
  the ranking-preservation datum and the ranking-blindness datum in one
  figure (Fig. 15), each at ADVISORY class.
- (v) model-form: SUPPORTS the base-pressure row's importance: the
  design method itself consumes an AVERAGED p_b in the KJ corner
  condition (F-04); the verification includes a truncated-plug base-
  pressure dataset (Fig. 5) their solver matches within 4.76% — but this
  is a COLD annular rig, so the R8 "no truncated-plug RDE base
  measurement" vacuum STANDS (the analogy label is not retired).
  gamma-variation datum: exit gamma 1.2500-1.2515 across truncations
  (F-08) — weak ADVISORY support that frozen-gamma modeling is mild at
  their exit states (their chemistry is one-step, so this does NOT test
  the frozen-vs-equilibrium bracket [T-EQBR]).
- (vi) optimum-shift: THE P-B contribution: flat-steady vs
  peaked-transient C_fx along truncation (F-10/F-12, Fig. 15) is a
  published instance of the channel's threat mechanism (reduced
  functional near-blind along a design direction where the true optimum
  has structure). It does not overturn the cell (the cell already
  brackets exactly this); it populates it with a second empirical
  marker. Landing: (vi) cell provenance list.

Addendum (c) (no-external-referee structural fact):
- DIFFERS/AMENDS (wording-level, see TH-2): P-B DOES publish an unsteady
  c_F datum (transient C_fx per truncation, Fig. 15/abstract) confronted
  with a steady averaged-input prediction — at CFD evidence class, with
  GLOBAL (not per-phase) averaging, and with 3D-URANS (not experiment)
  as the "truth". The addendum's fact survives under its own qualifiers
  ("per-phase", "truth"), but its header wording should cite P-B/P-C as
  the nearest existing referees and say why they do not discharge it.

==============================================================================
## 5. THREAT SCAN ("cosa potrebbe schiacciare il progetto")

TH-1 [ADVISORY, CFD class] Optimum blindness along truncation
  (Fig. 15, F-10/F-12): steady-averaged functional ~flat where the true
  unsteady functional has an optimum (+0.52%) and a cliff (-5.78%).
  ROW HIT: forchetta channel (vi) (optimum-shift) + channel (iv) WORST
  (ranking threshold R26). FALSIFIER OF RECORD (named, not re-opened):
  the (vi) cell's |argmax shift| <= delta/mu schema with mu = measured
  engine curvature; M-RED gradient measurement / R22-CFD-2 decide.
  DISPOSITION AT HELD EVIDENCE: does NOT fire — the cell already prices
  exactly this mechanism and P-B's instance is in-family (their cliff is
  driven by a regime change the steady run also eventually sees, and
  their in-band ranking is PRESERVED); it is a second empirical marker,
  strengthening the already-priced threat, not exceeding it.
TH-2 [ADVISORY] Existence of unsteady c_F data vs addendum (c)'s "the
  literature carries NO unsteady c_F datum that discriminates the
  2D-per-phase-averaged prediction against 3D-unsteady truth": P-B
  carries steady-vs-unsteady C_fx pairs (2.8% gap). ROW HIT: addendum
  (c) structural fact (a delivery-check item of the in-flight brief).
  ADJUDICATION AT HELD EVIDENCE: the fact SURVIVES on its two explicit
  qualifiers — P-B's prediction is GLOBALLY-averaged (not per-phase; a
  coarser reduction) and its "truth" is same-family URANS with one-step
  chemistry (not an external/measured truth; solver-family-correlated
  errors cancel in the pair). THE AMENDMENT DUE: the fact's wording
  should name P-B (and P-C) as nearest-referee CFD pairs and state these
  two disqualifiers, else a reader with P-B in hand reads the fact as
  false. Severity: AMENDMENT, not BREAK.
TH-3 [ADVISORY + INF geometry] Truncation optimum 40% L_cowl vs our
  default 0.20 (BLOCCATO row 9: "default troncamento RESTA 0.20 (banda
  0.20-0.40 stampata)"). DEFINITIONS DIFFER: P-B's DL_spike = length
  REMOVED / L_cowl (cowl = 80 mm diverging section); by figure-geometry
  inference [INF] their full spike ~ 1.0 L_cowl, so their optimum
  (DL = 40% L_cowl) RETAINS ~60% of the full spike, their 20% case
  retains ~80%, and their 80% case retains ~20% — i.e. their WORST case
  (-5.78%) is approximately a retained-20% plug. IF our 0.20 default
  means "retain 20% of the ideal plug length" (the classical convention
  of the Chutkey rig P-B verifies against, "only retains 20%", p. 4),
  then P-B's transient data argue AGAINST the low end of our band on
  THEIR configuration (highly-truncated plug = overexpansion + early
  trailing shock + recirculation growth at 19.33 km ambient). ROW HIT:
  BLOCCATO 9 (execution gated ADR-D4). FALSIFIER/DECIDER of the row:
  the ADR-D4 implementation window re-evaluation; our own band 0.20-0.40
  is printed and the re-bless is constrained-class. DISPOSITION: does
  not fire now (definitions must first be mapped exactly — synthesis
  item (e) duty; their ambient (6141 Pa) and base-flow class differ from
  our design point; and their OWN optimum at ~60%-retained shows
  mild truncation, not zero truncation, wins on their config).
  CARRY: a definition-mapping note must ride the ADR-D4 dossier.
TH-4 [ADVISORY] Design-method premise risk: P-B (with P-A/P-D) states
  the time-averaged-constraints design premise as "empirically
  recognized" (F-01) — if the field's premise were WRONG at ranking
  level, our program's per-phase refinement is the fix, not the victim;
  P-B's 2.8%-uniform offset actually bounds the premise's error on their
  config. ROW HIT: none (supports the program's framing that averaging
  adequacy is the open question R26). DISPOSITION: no fire; context.
NO OTHER PROJECT-LEVEL THREATS FOUND: explicitly, nothing in P-B
  threatens [T-T0P], [T-DISC-1/2], K-bar = 0, the flux-nullity block,
  the MoC/engine machinery, or G1/certification rows; the film-cooling
  half (F-16..F-25) is out of our current scope (no film cooling in the
  program) and carries no row-level tension.

==============================================================================
## 6. CONSUMPTION ARC (per finding — exact landing target; no orphans)

- F-01 (averaged-constraints premise + Jourdaine justification) ->
  forchetta channel (iv) BEST cell provenance note + synthesis item (e)
  "averaging bet" row; also candidate cross-cite in M0 T-T3-MAP context
  at landing (orchestrator).
- F-02/F-03/F-04 (MoC + Veen-Rao shrouded-plug + averaged p_b corner) ->
  choice-ledger context row for the Rao-class baseline (no new
  adjudication; ADVISORY comparison anchor); Veen-Gentry-Hoffman 1974 ->
  MISSED-CLUSTER WANTED candidate (see §8, ref [44]).
- F-05 (EAP/PG definitions) -> no landing needed (Kaemming-Paxson EAP
  already of record via litreview corpus); anchor refresh only.
- F-06..F-09, F-13 (field/topology + exit tables) -> TOPOLOGY
  CONSOLIDATION input for the R22F in-flight loop (synthesis item (d));
  Fig. 14 reading -> T-RED §2.3 exhibit-class note (P-B as second
  instance beside Harroun Fig. 18).
- F-10/F-11/F-12 (2.8% uniform gap; flat-vs-peaked; +0.52%/-5.78%) ->
  THREE landings: (1) forchetta (ii) BEST provenance (single-digit-%
  external instance); (2) forchetta (iv) BEST+WORST provenance (ranking
  preserved in-band / blind at in-class-delta scale); (3) forchetta (vi)
  cell provenance (second empirical marker). Carrier = synthesis graft
  list -> centerpiece Part 5 cell notes at the landing window.
- F-11 tail (swirl-induced early trailing shock at 80%) -> forchetta
  (iii) WORST cell note (swirl-mediated configuration-scale mechanism,
  same family as the shroud marker).
- F-14/F-15 (PG -19..-21%; loss decomposition 3 parts) -> forchetta (v)
  provenance note (their decomposition maps onto our channel structure:
  sweeping shocks -> (ii), viscous -> outside inviscid class/boundary-
  priced, base recirculation -> (v) base-pressure row); synthesis item
  (a) commonality matrix (loss-decomposition column).
- F-22 (V_cir 327-383 m/s) + Fig. 24 reading -> forchetta (iii)
  magnitude-cell provenance (independent exit-swirl datum inside B5/
  DISPATCH bands); ALSO -> T-DISC-2(ii) magnitude leg external anchor
  (ADVISORY). Landing: (iii) cell note + lit-registry where_read.
- F-24/F-25 (RMSD_theta 14.42-18.57 deg = MERIDIONAL deflection RMS;
  swirl suppressible by flat jets) -> two landings: (1) DEFINITIONAL
  GUARD note for the synthesis (RMSD_theta is NOT a swirl angle; do not
  book it against B5 — the brief's P-B abstract line "RMS flow
  deflection angle 14.42 deg" must not be consumed as channel-(iii)
  swirl); (2) swirl-breaker candidate family note (actuated suppression
  instance) beside the registered Paxson-Miki candidate.
- TH-1 -> forchetta (vi) cell provenance (carried by synthesis threat
  ledger, disposition "does not fire / strengthens priced threat").
- TH-2 -> addendum (c) wording amendment (synthesis item (e), explicit
  brief duty "unsteady c_F present or absent — check honestly": PRESENT
  at CFD class with the two disqualifiers named).
- TH-3 -> BLOCCATO row 9 rider note (definition mapping duty into the
  ADR-D4 dossier; synthesis item (e) truncation comparison).
- F-16..F-21, F-23 (film-cooling body) -> single archival row: out of
  program scope; retained in this study file as the paper's record; no
  further landing (declared non-orphan by this line).
- Reference-list extraction (§8) -> synthesis MISSED-CLUSTER WANTED
  consolidation (dedup vs docs/literature_registry.yaml).
- This file -> lit-registry READ-INTEGRAL row mint for P-B at the
  landing (orchestrator; where_read = this file).

==============================================================================
## 7. PAPERS NEEDED

None blocking for this slot. Opportunistic (feed §8 consolidation
instead of separate procurement calls): Veen-Gentry-Hoffman 1974 (the
shrouded-plug max-thrust designation method P-B implements — the closest
published ancestor of our Rao-class baseline formulation); Li-Xu-Huang
2022 JPP 38(5) 849-865 (the authors' own prior RDE nozzle design-method
paper, method parent of P-B); Chutkey et al. 2014 (truncated-plug
base-pressure verification dataset — candidate partial R8-adjacent
source, though cold-flow, NOT the RDE base measurement R8 needs).

==============================================================================
## 8. CENSUS-DEFECT REPAIR DUTY — REFERENCE-LIST EXTRACTION
##    (entries bearing on RDE-nozzle design/efflux/experiments; full
##    identities from pp. 21-22; tier: CORE = nozzle design/efflux/
##    performance; SEC = RDE thermal/film-cooling; CTX = review/method)

CORE:
1.  [13] E.M. Braun, F.K. Lu, D.R. Wilson, J.A. Camberos, "Airbreathing
    rotating detonation wave engine cycle analysis", Aerosp. Sci.
    Technol. 27 (2013) 201-208.
2.  [14] D.P. Stechmann, S.D. Heister, A.J. Harroun, "Rotating
    detonation engine performance model for rocket applications",
    J. Spacecr. Rockets 56 (3) (2019) 887-898.
3.  [15] T. Kaemming, M.L. Fotia, J. Hoke, F. Schauer, "Thermodynamic
    modeling of a rotating detonation engine through a reduced-order
    approach", J. Propuls. Power 33 (5) (2017) 1170-1178.
4.  [16] D.M. Davidenko, Y. Eude, I. Gokalp, F. Falempin, "Theoretical
    and numerical studies on continuous detonation wave engines", AIAA
    Paper 2011-2334, 2011.
5.  [17] Y. Shao, L. Meng, J. Wang, "Continuous detonation engine and
    effects of different types of nozzle on its propulsive performance",
    Chin. J. Aeronaut. 23 (2010) 647-652.
6.  [18] J. Braun, B.H. Saracoglu, G. Paniagua, "Unsteady performance of
    rotating detonation engines with different exhaust nozzles",
    J. Propuls. Power 33 (1) (2017) 121-130.
7.  [19] D.A. Schwer, R. Kelso, C.M. Brophy, "Pressure characteristics
    of an aerospike nozzle in a rotating detonation engine", AIAA Paper
    2018-4968, 2018.
8.  [20] Y. Zhu, K. Wang, Z. Wang, M. Zhao, Z. Jiao, Y. Wang, W. Fan,
    "Study on the performance of a rotating detonation chamber with
    different aerospike nozzles", Aerosp. Sci. Technol. 107 (2020)
    106338.
9.  [21] M.L. Fotia, F. Schauer, T. Kaemming, J. Hoke, "Experimental
    performance of a rotating detonation with nozzle", J. Propuls.
    Power 32 (3) (2016) 674-681. (the brief's "Fotia nozzle configs")
10. [23] J. Sun, J. Zhou, S. Liu, Z. Lin, W. Lin, "Plume flowfield and
    propulsive performance analysis of a rotating detonation engine",
    Aerosp. Sci. Technol. 81 (2018) 383-393.
11. [24] R.T. Fievisohn, J.L. Hoke, F. Schauer, "Quasi-2D simulations of
    nozzled rotating detonation engines with the method of
    characteristics", AIAA Paper 2018-0881, 2018.
12. [25] Y. Huang, H. Xia, X. Chen, Z. Luan, Y. You, "Shock dynamics and
    expansion characteristics of an aerospike nozzle and its interaction
    with the rotating detonation combustor", Aerosp. Sci. Technol. 117
    (2021) 106969.
13. [26] K. Goto, J. Nishimura, A. Kawasaki, K. Matsuoka, J. Kasahara,
    A. Matsuo, I. Funaki, D. Nakata, M. Uchiumi, H. Higashino,
    "Propulsive performance and heating environment of rotating
    detonation engine with various nozzles", J. Propuls. Power 35 (1)
    (2019) 213-223. (the brief's "Goto vacuum" experiments: vacuum-
    chamber spike-nozzle throat-geometry tests per p. 3 body text)
14. [33] T. Yi, J. Lou, C. Turangan, J. Choi, P. Wolanski, "Propulsive
    performance of a continuously rotating detonation engine",
    J. Propuls. Power 27 (1) (2011) 171-181.
15. [34] R. Li, J. Xu, S. Huang, "Nozzle design method for rotating
    detonation engine", J. Propuls. Power 38 (5) (2022) 849-865.
    (the authors' own method parent of P-B — HIGH priority)
16. [37] K. Chutkey, B. Vasudevan, N. Balakrishnan, "Analysis of annular
    plug nozzle flowfield", J. Spacecr. Rockets 51 (2) (2014) 478-490.
    (verification dataset: truncated-plug pressures + base pressure)
17. [38] G. Angelino, "Approximate method for plug nozzle design",
    AIAA J. 2 (10) (1964) 1834-1835.
18. [42] L. Deng, H. Ma, X. Liu, C. Zhou, "Secondary shock wave in
    rotating detonation combustor", Aerosp. Sci. Technol. 95 (2019)
    105517.
19. [44] R.V. Veen, R. Gentry, J.D. Hoffman, "Design of shrouded-plug
    nozzles for maximum thrust", AIAA J. 12 (1974) 1193-1197.
    (Rao-class shrouded-plug variational method — HIGH priority for the
    program's method-ancestry line)
20. [45] T.A. Kaemming, D.E. Paxson, "Determining the pressure gain of
    pressure gain combustion", AIAA Paper 2018-4567, 2018.
21. [46] J. Sun, J. Zhou, S. Liu, Z. Lin, J. Cai, "Effects of injection
    nozzle exit width on rotating detonation engine", Acta Astronaut.
    140 (2017) 388-401.
22. [35-Sun] J. Sun, J. Zhou, S. Liu, Z. Lin, "Effects of air injection
    throat width on a non-premixed rotating detonation engine", Acta
    Astronaut. 159 (2019) 189-198. (printed as the second [35]-numbered
    entry on p. 22, between [34] and [36]; numbering collision with the
    Menter turbulence reference noted verbatim)
23. [47] S. Yao, J. Wang, "Multiple ignitions and the stability of
    rotating detonation waves", Appl. Therm. Eng. 108 (2016) 927-936.
24. [12] F.K. Lu, E.M. Braun, "Rotating detonation wave propulsion:
    experimental challenges, modeling, and engine concepts", J. Propuls.
    Power 30 (5) (2014) 1125-1142. (CTX-grade review, kept for the
    cluster map)
25. [43] M.J. Zucrow, J.D. Hoffman, Gas Dynamics, vol. 2, John Wiley and
    Sons, New York, 1976. (method source of record already in program
    use — cross-check only, no procurement)

SEC (RDE thermal/film-cooling experiments+CFD, extracted for
completeness of the citation neighborhood):
26. [27] D. Lim, S.D. Heister, J. Humble, A.J. Harroun, "Experimental
    investigation of wall heat flux in a rotating detonation rocket
    engine", J. Spacecr. Rockets 58 (5) (2021) 1444-1452.
27. [28] K. Wu, L. Zhang, M. Luan, J. Wang, "Effects of isothermal wall
    boundary conditions on rotating detonation engine", Combust. Sci.
    Technol. 192 (2) (2020) 211-224.
28. [29] S.W. Theuerkauf, P.I. King, F.R. Schauer, J.L. Hoke, "Thermal
    management for a modular rotating detonation engine", AIAA Paper
    2013-1176, 2013.
29. [30] K. Goto, K. Ota, A. Kawasaki, H. Watanabe, N. Itouyama,
    K. Matsuoka, J. Kasahara, A. Matsuo, I. Funaki, "Cylindrical
    rotating detonation engine cooling by means of propellant
    injection", AIAA Paper 2020-3855, 2020.
30. [31] T. Sada, A. Matsuo, E. Shima, H. Watanabe, A. Kawasaki,
    K. Matsuoka, J. Kasahara, "Numerical investigation of rotating
    detonation engine with injection from the combustor side wall",
    AIAA Paper 2022-4108, 2022.
31. [32] J. Tian, Y. Wang, J. Zhang, X. Tan, "Numerical investigation on
    flow and film cooling characteristics of coolant injection in
    rotating detonation combustor", Aerosp. Sci. Technol. 122 (2022)
    107379.

CROSS-REFERENCE (not a new candidate): [41] X. Liu, M. Cheng, Y. Zhang,
J. Wang, AST 120 (2022) 107300 = P-A (already registry :615 per the
census-defect context; path note only). [22] Jourdaine et al. PCI 37
(2019) = P-D (this campaign). NOTE on the brief's expected names: "Ma
hot-fire" does not appear as a distinct hot-fire entry in P-B's list
(H. Ma appears only in [42] Deng-Ma; F. Ma [3] is PDE-scope); "Zhou
conical" has no conical-nozzle entry here (J. Zhou appears in [23],
[35-Sun], [46]) — absence stated, not implied; those two are expected
from the other slots' lists.

EXTRACTION COUNT: 31 bearing entries with full identities (25 CORE +
6 SEC), + 2 cross-references (P-A, P-D) + 1 numbering-collision note.

==============================================================================
## 9. MACHINE SUMMARY

paper: P-B Li-Xu-Lv-Lv-Song AST 136 (2023) 108221, DOI 10.1016/j.ast.2023.108221
pages_read: 22/22 [FULL]; figure_pages_rendered_visually: pp. 2, 4-21 (Figs. 1-25, all)
findings_ledger_rows: 25 (F-01..F-25)
topology_atlas_entries: 14 figure-groups
confrontation_verdicts: T-DISC SUPPORTS(2)/DIFFERS(1); T-RED SUPPORTS(2)/DIFFERS(1)/THREATENS-mild(1); M-RED SUPPORTS(1)/DIFFERS(1); R22-CFD SUPPORTS(1)/DIFFERS(1); forchetta cells informed: (i),(ii),(iii),(iv),(v),(vi) all six; addendum(c) AMENDS(1)
threat_count: 4 (TH-1..TH-4); fires: 0 BREAK; 1 AMENDMENT-class (TH-2, addendum (c) wording); 1 rider-note duty (TH-3 -> BLOCCATO 9 / ADR-D4 definition mapping); 2 strengthen-already-priced (TH-1, TH-4)
top5_bearing:
1. Steady MoC-design flow overestimates C_fx by ~2.8%, UNIFORM for truncation <= 60% (pp. 10, 20) — published same-code averaged-vs-3D-unsteady pair, single-digit-% and ranking-preserving in-band (feeds forchetta (ii)/(iv) BEST).
2. Steady C_fx ~flat (0.969) vs transient optimum at DL_spike = 40% L_cowl (+0.52% vs 20%; -5.78% at 80%) (p. 10, Fig. 15) — second empirical marker of the channel-(vi) optimum-blindness class.
3. Exit circumferential velocity 327.5-383.4 m/s on V_x ~ 1910 m/s (p. 18, Fig. 24d) => eps_theta ~ 0.17-0.20, swirl angle ~ 10-11.4 deg [INF] — independent datum inside our B5/DISPATCH bands (forchetta (iii)).
4. Unsteady c_F data EXIST at CFD class in P-B (Fig. 15) — addendum (c) no-external-referee fact survives ONLY via its "per-phase" and "truth" qualifiers; wording amendment due (TH-2).
5. Truncation definition: DL_spike = removed length / L_cowl (p. 10), full spike ~ 1.0 L_cowl [INF] => their optimum retains ~60% of the spike; NOT commensurable with our 0.20 default without the ADR-D4 definition mapping (TH-3, BLOCCATO 9 rider).
reference_extraction_count: 31 bearing entries (25 CORE + 6 SEC) + 2 cross-refs (P-A, P-D)
papers_needed: none blocking; opportunistic: Veen-Gentry-Hoffman 1974, Li-Xu-Huang 2022 (JPP 38:5), Chutkey 2014
output_file: validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pB_li_xu_2023.md
