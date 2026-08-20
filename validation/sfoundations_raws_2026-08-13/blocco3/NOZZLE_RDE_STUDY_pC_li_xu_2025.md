# NOZZLE-RDE DEEP STUDY — P-C: Li, Xu, Lv, Yu, Zhou (NUAA) 2025

Session: S-FOUNDATIONS-C4, blocco 3 (nozzle-RDE arrivals campaign).
Brief: BRIEF_nozzle_rde_arrivals_study.md (SLOTS 1-4 spec, SHARED RULES +
CENSUS-DEFECT CONTEXT accepted: env pinned, nothing installed; ONLY this
file written; page anchors on every claim; evidence class per statement).
Confrontation frame read this window: BRIEF_blocco2_phaseD.md (CENTERPIECE
+ forchetta channels (i)-(vi)), BRIEF_blocco2_phaseD_addendum_c4.md,
phaseD/phaseD_r22f_centerpiece.md (parts 1-5), docs/rde_nozzle_PROGRESS.md
BLOCCATO row 9 note (:13-15, trunc 0.20 gated ADR-D4).

READ-DEPTH DECLARATION: **[FULL]** — all 18 pages of
literature_addition_nozzle_rde/1-s2.0-S1270963824010071-main.pdf read;
ALL figure pages rendered VISUALLY (pp. 4, 5, 6, 7, 8, 9, 10, 12, 13, 15,
16, 17); reference list (p. 18) additionally text-extracted verbatim.

EVIDENCE CLASSES USED (per SHARED RULES): [REP] = the paper's own printed
text/number at the cited page (published-CFD claim — external, never a
measurement of ours); [FIG] = my visual reading of a published figure
(ADVISORY, weaker than [REP]); [INFER] = my inference connecting paper
content to our record (weakest; every such statement labeled).

==============================================================================
## 1. IDENTITY + METHOD SUMMARY

IDENTITY (p. 1): Rui Li, Jinglei Xu (corresponding, xujl@nuaa.edu.cn),
Haiyin Lv, Kaikai Yu, Junfei Zhou — State Key Laboratory of Mechanics and
Control of Aeronautics and Astronautics Structures + Jiangsu Province Key
Laboratory of Aerospace Power System, NUAA, Nanjing. "Numerical
investigations of the nozzle performance of a rotating detonation engine
with axially adjustable cowl and spike", Aerospace Science and Technology
158 (2025) 109878, DOI 10.1016/j.ast.2024.109878. Received 17 Feb 2024,
accepted 13 Dec 2024. Same first/second authors as P-B (ref [27] = P-B)
and the nozzle-design paper ref [22] (Li-Xu-Huang JPP 2022).

METHOD (pp. 3-4, 6):
- Equations: transient 3D RANS (eqs. 1-4, p. 3), single-step Arrhenius
  H2/air reaction (eq. 6), ideal gas, Sutherland laminar viscosity (eq. 7),
  k-omega SST turbulence (eqs. 8-10, Menter [41]) [REP p. 3].
- Numerics: finite volume, 2nd-order Roe + MUSCL convective fluxes,
  2nd-order central viscous, 2nd-order implicit transient, nonslip walls
  with y+ close to 1 [REP p. 3]. (No named commercial/open code — solver
  identity NOT stated; [INFER] in-house or unnamed package.)
- Validation 1 (cold annular spike nozzle): vs Verma [44] experiments,
  exit nozzle radius 25±0.1 mm, throat annular gap 9±0.1 mm, protruded
  spike 59.7±0.1 mm; domain 25D x 10D; schlieren + wall-pressure match at
  NPR = 2.10 / 2.57 / 3.82, separation locations captured (Fig. 2, p. 5)
  [REP pp. 3-5].
- Validation 2 (detonation): 2D 283 mm x 45 mm domain, grid independence
  0.1/0.2/0.4 mm — peak-pressure relative error 2.50 % coarse-medium,
  0.85 % medium-fine; grid 0.2 mm retained [REP p. 4, Fig. 3 p. 6].
  ZND check vs SDToolbox (Browne et al. [46]): T_D 2905 vs 2910 K
  (0.17 %), p_D 3.399 vs 3.422 MPa (0.67 %), U_D 1956.3 vs 1980.1 m/s
  (1.20 %) (Table 1, p. 6); ZND induction length 0.774 mm ≈ 3x the medium
  grid size [REP p. 4]. ([INFER] caveat: ~3-4 cells per induction length
  + 1-step kinetics = marginal detonation-structure resolution; the
  authors themselves only claim macroscopic adequacy, p. 3.)
- Geometry (p. 4, Fig. 6 p. 7): annular combustor inner/outer radii
  40/50 mm, length 45 mm; truncated aerospike nozzle downstream:
  contraction ratio A_c,in/A_n,t = 1.115, expansion ratio A_n,out/A_n,t
  = 6.461; cowl length 85 mm; truncated spike hump length 53 mm, base
  radius 23.2 mm; "the curve transitions are designed by the
  characteristic method, as shown in Ref. [27]" (= P-B, max-thrust MoC)
  [REP p. 4]. Walls adiabatic.
- Injection/BCs: premixed stoichiometric H2/air, p0 = 1 MPa, T0 = 300 K,
  micro-injection with combustor-inlet-to-throat area ratio A_c,in/A_c,t
  = 5; piecewise critical-pressure injection functions eqs. (11)-(15)
  (per [47]) [REP pp. 4, 6]; exit pressure-outlet p_b = 8849 Pa,
  T_b = 217 K ("flight height of 17 km") [REP p. 6].
- Cases: 5 FIXED relative positions (Spike−/Spike+/baseline Spike 0 with
  Cowl 0; Cowl−/Cowl+ with Spike 0; ±10 mm), each with a transient RDE
  run AND a "reference steady state" computed with "mass-weighted average
  inflow parameters equivalent to the transient conditions" [REP p. 8];
  plus 2 DYNAMIC strategies (axially moving spike / moving cowl, slipping
  velocity 20 m/s, dynamic mesh Fig. 7 p. 7) [REP pp. 1, 6].
- Cycle: single-wave, period 0.147 ms [REP p. 12] ([INFER] ≈ 6.8 kHz).

==============================================================================
## 2. FINDINGS LEDGER (every result/consideration, with pages)

Design-method steps and geometry findings:
- L1. Nozzle profile design chain: max-thrust theory + MoC transplanted
  from steady theory (Ref. [27] = P-B); this paper takes that design as
  baseline and studies axial misalignment + actuation [REP pp. 2, 4].
- L2. Area-law bookkeeping under actuation (Fig. 8, p. 7): spike shift
  −10 → +10 mm makes throat-to-combustor-inlet area ratio go
  0.9538 → 0.8970 → 0.9429; cowl shift the same distance:
  0.9429 → 0.8970 → 0.9538 — "the effects caused by positive and negative
  deviations of spikes and cowls from the baseline configuration are
  asymmetric" [REP p. 6]. Contraction/expansion-ratio variation ranges
  during dynamic adjustment: 0.054–0.067 and 0.316–0.387 [REP p. 7].
- L3. Performance metrics defined: C_fx = I_ex/F_ideal (eqs. 16-18),
  mass-flux-weighted Mach_ave (eq. 19), RMSD_theta =
  sqrt((1/mdot) Σ mdot_i (theta_i − π/2)^2) — exit flow-angle RMS
  deviation from AXIAL, mass-weighted (eq. 20); lateral force F_L from
  wall-pressure + shear integrals (eqs. 21-23) [REP p. 7-8].

Fixed-configuration results (§4.1):
- L4. Detonation fronts occupy ~half the combustor length; hot zones
  > 3000 K post-shock/post-detonation; "The circumferential propagation
  of the detonation wave inevitably leads to asymmetry of flowfields in
  the meridian plane" [REP p. 8].
- L5. Shock-origination switching (the title finding): when the maximum
  spike radius sits downstream of the minimum cowl radius, the
  asymmetric internal shock is issued FROM THE SPIKE and extends toward
  the cowl; otherwise the origination converts TO THE COWL; Mach
  reflection near the cowl exit for Spike−/Cowl+ replaced by regular
  reflection in the mirrored cases [REP pp. 8, 16 conclusion (1)].
- L6. All four misaligned states deviate to OVERexpanded conditions vs
  baseline; inward-turning internal flow path near throat pushes
  diverging-section shocks closer to the cowl wall, outward-turning
  reverses the locations [REP p. 8].
- L7. Steady reference states: recirculation zones and shocks become
  AXISYMMETRIC, meridian Mach never exceeds 3.6; transient states carry
  high-Mach portions Mach > 3.71 at the nozzle exit [REP pp. 8, 11].
- L8. Transient vs steady base region: for (Spike−, Cowl 0) and
  (Spike 0, Cowl +) the axial length of the closed recirculation zone at
  the transient state is SMALLER than steady; for (Spike +, Cowl 0) and
  (Spike 0, Cowl −) the base-wake radius at transient is LARGER than
  steady — "interactions between the nozzle diverging profiles and the
  flow swirling caused by the circumferential movement of detonation
  waves" [REP p. 11].
- L9. Time-averaged wall pressures (Fig. 11, p. 10): injection plane
  0.48–0.50 MPa; combustor drop to 0.23–0.26 MPa (triple-point expansion
  fans); converging-section reflections raise local maxima; extra local
  maxima 0.10 MPa on the spike (Spike−/Cowl+ cases) and 0.07 MPa on the
  cowl (Spike+/Cowl− cases) behind the internal shock; axial misalignment
  attenuates pressure on the relatively DOWNSTREAM component more
  effectively than the upstream one [REP p. 11].
- L10. Work-potential shift: shortened combustor length reduces the
  number of passes through the reactant-triangle shock; axial retractions
  of spike and cowl BOTH raise time-average total pressure at the throat
  by approximately 3.89 % vs reference [REP pp. 1 abstract, 11, 16
  conclusion (2)]. Time-average total temperature stays near 2414 K, max
  relative discrepancy 0.91 % ("more connected with the upper limit of
  fuel properties", i.e. heat addition per mass capped by premixed
  stoichiometry) [REP pp. 1, 11, 16].
- L11. Thrust coefficients (Fig. 13, p. 11): ALL configurations, transient
  and steady, remain above 0.94 (range read [FIG] ≈ 0.9425–0.968).
  Steady C_fx > transient for (Spike +, Cowl 0), (Spike 0, Cowl −), and
  baseline ("total pressure loss and viscous loss ... increased by the
  asymmetric moving shock waves"); REVERSED (transient > steady) for
  (Spike −, Cowl 0) and (Spike 0, Cowl +) because "the high-Mach-number
  portions (Mach > 3.71) of the transient states at the RDE nozzle exit
  are more significant" [REP p. 11]. Gap magnitude [FIG] ≈ 0.002–0.015
  in C_fx (~0.2–1.5 %), configuration spread ≈ 0.9425–0.968 (~2.5 pts).
- L12. Exit Mach: reference case (Spike 0, Cowl 0) reaches maximum
  average exit Mach 3.03 — "implying that the maximum thrust theory for
  the steady supersonic axisymmetric flow proposed by Veen et al. [48]
  is approximately applicable to the RDE nozzle under the premise that
  the propagation frequency of detonation waves are in the magnitude of
  kHz" [REP p. 11; conclusion (3) p. 16].
- L13. RMSD_theta (fixed configs, Fig. 14 p. 11): below 10° for
  (Spike +, Cowl 0) and (Spike 0, Cowl −); reference case roughly 4.5 %
  ABOVE 10°; (Spike −, Cowl 0) and (Spike 0, Cowl +) show +38.52 % and
  +33.49 % vs reference ([FIG] ≈ 13.5–14.5°) — "more flow expansion
  provided by the truncated spike is more beneficial for axial flow
  guiding" [REP p. 11].
- L14. Detonation robustness: von Neumann pressure spikes 3.2–3.6 MPa at
  x/L = 0.11 for ALL five adjustment states, decaying exponentially to
  0.15 MPa within the 0.147 ms cycle — "changes in the meridian geometric
  configuration of flow paths only have limited effects on the detonation
  intensity" [REP p. 12].
- L15. Axial pressure-pulse decay along the nozzle: peaks 0.5–0.6 MPa
  (shock-exposed points) vs 0.27–0.29 MPa (expansion-fan-exposed) at
  x/L = 1.11; below 0.14 MPa at x/L = 1.56; below 0.084 MPa at exit
  x/L = 2.00; a diverging path with relatively downstream spike dampens
  the exit pressure pulse by up to 87.8 % [REP p. 12].
- L16. Spike/cowl wall unsteady peak deviations across configs: Point 5
  8.18 % / 6.49 %, Point 7 15.08 % / 11.28 % [REP p. 13]; "the transient
  pressures along the spike and cowl also essentially obey the
  area-variational law in a steady state" [REP p. 13; repeated in
  conclusion (3) p. 16-17].

Dynamic-actuation results (§4.3):
- L17. Mass-flow response: moving-cowl oscillation ≤ 0.067 kg/s over
  1 ms; moving-spike oscillation shrinks 0.205 → 0.081 kg/s — mass flow
  more sensitive to INNER-wall (spike) mutation; spike extremes
  0.900 kg/s @2.22 ms / 0.695 @2.32 ms; cowl 0.839 @2.28 / 0.769 @2.52
  [REP pp. 13-14, Fig. 17].
- L18. Thrust response: practical-thrust oscillation ≤ 152.9 N (cowl) vs
  491.4 → 215.8 N (spike); peak C_fx 0.9734 @2.18 ms (spike) vs 0.9466
  @2.34 ms (cowl); spike local max drops 4.09 % between 2.18 and 2.72 ms
  with local minima below 0.92; max total thrust 1861.2 N; spike axial
  adjustment range "evenly two times the axial moving cowl" [REP pp. 1,
  14, 16-17, Fig. 20].
- L19. Lateral force: moving spike 673.6 → 476.8 N (high+low frequency);
  moving cowl +43.93 % (458.5 → 659.9 N, high frequency small amplitude);
  DIRECTIONS of the two strategies almost coincide — "the dynamic
  redistributions of flow properties on the nozzle and combustor walls
  cannot significantly affect the propagation velocities of the flow
  structures"; direction angle phi_L sweeps 0–360° each cycle (Fig. 21b
  sawtooth) [REP pp. 14, 17, Fig. 21]. [INFER] instantaneous lateral
  force ≈ 25–35 % of instantaneous axial thrust (450–670 N vs
  1500–1860 N), rotating at wave frequency.
- L20. Exit-state response: moving-spike Mach_ave larger than cowl ~95 %
  of the time, peaks 3.32/3.33 @2.63/2.73 ms; cowl max 3.16 @2.48 ms;
  RMSD_theta: spike drops from 14.63° then fluctuates below 11°
  (oscillating 9°–11° per abstract/conclusion (4)); cowl first drops
  15.96 % then rises to 12.89° [REP pp. 1, 14, 17, Fig. 22].
- L21. Mechanism color: axial movements "pull the high-temperature vortex
  blobs along the shear layer into the nozzle diverging section",
  promoting high-temperature concentration of transverse waves on the
  inner wall; outer wall = compression component, inner wall = expansion
  component [REP p. 14].
- L22. Recommendation: axial moving spike recommended (fast response +
  force superiority) [REP pp. 1, 17 conclusion (4)].

==============================================================================
## 3. TOPOLOGY ATLAS (per field figure; all rendered visually)

- Fig. 1 (p. 4), Fig. 2 (p. 5) — validation geometry/mesh + cold-flow
  schlieren vs simulation at NPR 2.10/2.57/3.82: overexpansion shock,
  lambda-shock pattern, separated/reattached flow on the spike; numerical
  schlieren reproduces separation points [FIG]. Informs: none of the
  forchetta channels directly; establishes the ADVISORY weight of P-C's
  spike-flow topology claims (validated separation capture).
- Fig. 3/4/5 (p. 6) — grid effects on the detonation peak; dynamic
  reactant triangle temperature contour vs Bykovskii schlieren; ZND
  profiles. Informs channel (v) at the meta level (their model-form
  choices: 1-step, 0.2 mm grid) [FIG].
- Fig. 6 (p. 7) — baseline meridian drawing with monitoring points 1-8;
  geometric parameters of record for any future CFD-2-style reuse [FIG].
- Fig. 8/9 (pp. 7-8) — area-ratio distributions and their time histories:
  the area-variational law realized by each actuation; asymmetric
  throat-ratio response (L2) [FIG]. Informs the delta-carrier/fixed-area
  discussion (see §4, Part-1/minor (c) confrontation).
- Fig. 10 (pp. 9-10, five pairs) — THE CENTRAL TOPOLOGY EXHIBIT:
  transient (left) vs steady-reference (right) meridian Mach + inner-wall
  temperature contours for the 5 fixed configs. Visual content [FIG]:
  transient meridian fields are visibly ONE-SIDED — the internal shock
  and its Mach/regular reflection appear on one side of the axis only
  (the instantaneous meridian cut of a rotating 3D structure); wall
  temperature maps show azimuthally banded hot streaks winding along the
  annulus (the rotating wave's thermal footprint); steady counterparts
  are mirror-symmetric with axisymmetric base recirculation. Base zone:
  transient recirculation visibly deformed vs the steady closed torus
  (L8). Informs: T-RED channel (ii) (azimuthal-structure reduction — this
  is the phenomenon class the K operator carries: rotating one-sided
  shock footprint = advective-helix ray family); channel (iii) (flow
  swirling interacting with diverging profiles, L8); channel (iv)
  (what the steady/averaged solution erases). Companion exhibit class to
  Harroun 2021 Fig. 18 (centerpiece §2.3).
- Fig. 11 (p. 10) — time-average wall-pressure axial profiles, inner vs
  outer: pressure plateaus + internal-shock local maxima (L9); the
  time-AVERAGED wall load already follows a steady-like area law [FIG].
  Informs channel (iv) BEST (averaging adequacy at wall-load level).
- Fig. 12/13/14 (p. 11) — throat total pressure/temperature bars (L10);
  transient-vs-steady C_fx bars (L11); Mach_ave + RMSD_theta bars (L13).
  Informs channels (i)/(ii)/(iv) quantitatively (see §4) and channel
  (iii) via RMSD_theta magnitudes [FIG].
- Fig. 15/16 (pp. 12-13) — monitoring-point pressure histories (annulus,
  spike, cowl): clean single-mode periodicity at every station across all
  five configs (five nearly identical cycles, no mode transition);
  amplitude decay along the nozzle (L14/L15) [FIG]. Informs channel (i)
  guard (T0-flatness/pure-periodic pin realized in a published coupled
  simulation) and channel (ii) (unsteady content magnitude vs station).
- Fig. 17 (p. 13) — mass-flow histories with labeled extremes (L17):
  chamber-nozzle coupling channel visible in mdot [FIG].
- Fig. 18 (p. 15, six frames) / Fig. 19 (p. 16, two frames) — transient
  meridian Mach + wall-temperature during actuation: normal-shock
  accumulation near combustor exit at local max mdot; severely distorted
  flowfield at 2.32 ms; high-Mach region deflecting from cowl to spike;
  central exit Mach > 4.15 patches; high-temperature vortex blobs drawn
  along the shear layer (L21); helical/banded wall-temperature streaks
  visible on the annulus surfaces [FIG]. Informs channel (ii) (worst-case
  azimuthal structure under off-design/transient operation) and channel
  (v) (base-zone state sensitivity).
- Fig. 20/21/22 (pp. 16-17) — thrust, C_fx, lateral force (magnitude +
  rotating direction), exit Mach_ave and RMSD_theta histories: the
  rotating lateral-force sawtooth (L19) is the cleanest published face of
  "instantaneous azimuthal asymmetry is O(10x) the time-averaged percent
  effects" [FIG]. Informs channel (ii) structure (large per-phase
  content, near-cancelling mean — the K-bar = 0 phenomenology) and the
  addendum-(c) discussion (unsteady c_F trace EXISTS here).

==============================================================================
## 4. CONFRONTATION vs THE DRAFT (phaseD_r22f_centerpiece.md)

Part 1 [T-DISC] (draft §§1.0-1.4): **SUPPORTS (weak, indirect)** — P-C
never uses a p-only projection (full-state CFD throughout), and nothing
in it constrains E_theta from P(xi), so the fiber theorem is untouched;
its exit-angle magnitudes (RMSD_theta 8.16°–14.63°, L13/L20) sit exactly
in the B5 10–14° class the draft books at [T-DISC-2](ii) (draft
:146-148). Bearing sentence: an independent NUAA solver on a MoC-designed
truncated aerospike returns mass-weighted exit flow-angle RMS deviations
of 9–14.6° [REP pp. 11, 14], consistent with the corpus band the
magnitude leg cites. CAVEAT [INFER]: RMSD_theta measures deviation from
AXIAL of the total flow angle at the exit plane (eq. 20, p. 8) — it
conflates meridional divergence with azimuthal swirl; it is an UPPER
proxy for the swirl-angle entry of channel (iii), not a swirl measurement
(definition flag for the synthesis, brief SLOT 5 (e)).

Part 2 [T-RED] (draft §§2.0-2.5, exhibit §2.3): **SUPPORTS** — P-C is a
second, independent physical exhibit of the phenomenon class K carries:
"the circumferential propagation of the detonation wave inevitably leads
to asymmetry of flowfields in the meridian plane" [REP p. 8], one-sided
internal shocks switching origination between spike and cowl (L5),
transient base zones deformed by "flow swirling caused by the
circumferential movement of detonation waves" (L8, [REP p. 11]), and a
lateral force of ~25-35 % of axial thrust rotating at wave frequency with
near-zero implied mean (L19, [FIG]+[INFER]) — large per-phase azimuthal
content with cancelling mean is precisely the K-bar = 0 + (J)/(H)
fluctuation-channel structure (draft §2.2(i)). The steady references
axisymmetrize exactly the structures K drops (Fig. 10 right columns).
Bearing sentence: Fig. 10's transient-vs-steady pairs (pp. 9-10) are a
published side-by-side of the field WITH and WITHOUT the azimuthal
structure the reduction residual must price — citable ADVISORY companion
to Harroun Fig. 18 in the draft's §2.3 exhibit slot. No claim in P-C
contradicts the operator census, the mean-nullity theorem, or the seam
declaration (time-coupling vs azimuthal halves).

Part 3 [M-RED] (draft §§3.1-3.5): **SUPPORTS (methodological precedent) /
DIFFERS (object measured)** — P-C's transient-vs-steady-reference
protocol (same solver, mass-weighted averaged inflow, L7/L11) is the
field's crude cousin of O5-lite leg (A) (J_exact vs J_avg per family):
it demonstrates the comparison is meaningful and lands at percent scale.
DIFFERS: their "averaged" object is a steady axisymmetric solution fed by
inflow means — NOT a per-phase-averaged family; their comparison prices a
STRONGER reduction than ours (it discards per-phase structure entirely),
so its gap is an upper-class analog, not a calibration of our eps
[INFER, definitional]. Bearing sentence: steady-vs-transient C_fx gaps of
~0.2–1.5 % [FIG p. 11] with BOTH signs across configurations set the
published scale for what leg (A) should expect — and their sign flip
(L11) previews that eps need not be single-signed across families.

Part 4 [R22-CFD] (draft §§4.1-4.3): **SUPPORTS CFD-1's motivation +
provides a CFD-2 template** — P-C empirically exhibits the
class-membership/back-coupling premise CFD-1 exists to price: moving the
nozzle walls changes the chamber state (throat time-average total
pressure +3.89 %, L10) while leaving detonation intensity nearly
unchanged (von Neumann 3.2–3.6 MPa across all states, L14) — i.e.
interface DATA are design-dependent at percent level even when the WAVE
is robust [REP pp. 11-12]. Bearing sentence: a coupled 3D unsteady
simulation shows nozzle-geometry changes feed back ~4 % into the
interface stagnation state our program treats as given — exactly the
premise CFD-1 (draft §4.1, "no in-house family can test its own class
membership premise") is scoped to test; and P-C's paired
transient/steady-reference runs are a working template for the CFD-2
confrontation mechanics (paired runs, one geometry family, same solver).
Note for §4.3 scheduling inputs: P-C also shows the CHEAP half (steady
reference runs) is standard practice; the expensive half remains the
coupled transient.

Part 5 FORCHETTA TABLE (draft Part 5 + addendum (c)), per channel:
- (i) time-coupling: **SUPPORTS the pin's realizability** — clean
  single-mode periodicity at all stations for all five configurations
  (Fig. 15/16, L14) is a published instance of the pure-periodic-wave
  class; no mode transition observed within the windows shown [FIG
  pp. 12-13]. No number for our (i) gap (their unsteadiness is never
  decomposed); WORST cell unaffected.
- (ii) azimuthal reduction: **SUPPORTS BEST cell** ("single-digit %
  plausible") — total steady-vs-transient C_fx gap 0.2–1.5 % [FIG p. 11]
  even though their reduction is cruder than per-phase; does NOT probe
  the off-ray >10 % worst cell.
- (iii) swirl/tangential: **SUPPORTS** the B5 band — RMSD_theta 9–14.6°
  vs the draft's 10–14° per-phase exit-swirl booking (with the eq.-20
  definitional caveat above); the base-zone/swirl interaction (L8) is a
  qualitative face of the B1/B2 phase-coherent content.
- (iv) averaging adequacy: **SUPPORTS BEST (sizing) + feeds WORST
  (ranking)** — time-average wall pressure obeys the steady
  area-variational law (L16) and max exit Mach 3.03 on the MoC-designed
  profile (L12) support sizing-level adequacy of steady design; BUT the
  configuration ORDERING flips between steady and transient evaluation
  for the two overexpanded-with-high-Mach-exit cases (L11: Spike−/Cowl+
  rank differently, [FIG] gap ~0.5–1 pt where config spread is ~2.5 pt)
  — a documented instance of averaging-error comparable to design deltas,
  i.e. the R26 ranking concern, at ADVISORY figure-read class.
- (v) model-form: **SUPPORTS (nothing breaks the bars)** — their own
  model-form stack (1-step premixed, k-omega SST, adiabatic, ~3 cells per
  induction length) bounds the evidence weight of L11-class numbers;
  transient-vs-steady base-recirculation differences (L8) reinforce the
  draft's refusal to price truncated-plug base pressure from steady
  analogies (WORST cell "base-pressure model-form UNPRICED" stands).
- (vi) optimum-shift: **DOES NOT FIRE, but brushes** — the argmax over
  their 5-config family is the SAME (baseline Spike 0/Cowl 0 tops both
  steady and transient orderings, Fig. 13 [FIG]); the mid-ranking flip
  (L11) shows reduced-vs-true ordering CAN differ along real design
  directions at their gap scale, without moving the argmax here.
- Addendum (c) (no-external-referee fact): **DIFFERS — refinement
  needed, narrow claim survives.** P-C DOES publish an unsteady c_F
  (time-resolved C_fx, Fig. 20(b) p. 16) AND a steady-vs-unsteady C_fx
  comparison (Fig. 13 p. 11). It is still NOT a referee for the
  per-phase thrust error: the steady companion is an averaged-INFLOW
  axisymmetric CFD (not a 2D-per-phase-averaged prediction), same
  solver, zero experimental thrust. So the addendum's operative claim
  ("no datum that DISCRIMINATES the 2D-per-phase-averaged prediction
  against 3D-unsteady truth") stands; its broad-sounding phrasing "the
  literature carries NO unsteady c_F datum" should be tightened at the
  synthesis to name P-C/P-B as CFD-internal unsteady-c_F data that fail
  the discriminator test for a different reason (wrong steady companion,
  no experiment). [REP pp. 11, 16 + INFER, definitional].

BLOCCATO row 9 (truncation 0.20, gated ADR-D4): **no bearing from P-C**
— P-C fixes one truncated spike (hump 53 mm, base radius 23.2 mm,
truncation fraction not stated as a ratio) and never optimizes
truncation; the 40 %-optimum claim lives in P-B. No confrontation here.

==============================================================================
## 5. THREAT SCAN ("cosa potrebbe schiacciare il progetto")

T-C1 [RANKING-SCALE ALIASING INSTANCE — moderate, ADVISORY]. Fig. 13
(p. 11, [FIG]): steady-averaged evaluation mis-orders two of five
configurations relative to transient evaluation, with averaging gaps
(~0.2–1.5 % C_fx) comparable to configuration deltas (~2.5 pts total
spread, sub-point neighbors). Row hit: forchetta channel (iv) WORST cell
/ R26 ranking threshold (draft Part 5 row (iv); registry :2147 "adequacy
NOT demonstrated for percent-level ranking"). It does not FIRE the row —
it is an instance of exactly what the row already declares OPEN, and the
paper's steady reduction is cruder than our per-phase average [INFER].
Row's own falsifier protocol: M-RED eps vs in-class deltas → R22-CFD-2
(the draft's stated tighteners) — the threat is retired or confirmed by
that protocol, not by this reading.

T-C2 [DESIGN-DEPENDENT INTERFACE DATA — moderate, ADVISORY]. L10:
nozzle-side geometry changes shift the chamber time-average total
pressure by ~3.89 % and the throat area ratio by ~6 % (L2) [REP pp. 6,
11]. Row hit: the fixed-interface-data premise (pins H3/P1/H9 as
design-INDEPENDENT data; draft §4.1 CFD-1). If interface data drift with
the design variables at percent level, a fixed-data optimum can be
displaced — a chamber-coupling sibling of channel (vi) that no in-house
family can price. Falsifier protocol: CFD-1 as already scoped (draft
§4.1 is verbatim the test of this premise); the P-D choked +50–60 %
datum (brief PAPERS P-D) is the stronger form of the same threat and the
synthesis should join them. Mitigation of record: P-C's wave itself is
robust (L14), so the drift is in the stagnation state, not the wave
class.

T-C3 [ADDENDUM-(c) WORDING EXPOSURE — low, definitional]. A referee
could cite P-C Fig. 20(b)/Fig. 13 against the sentence "the literature
carries NO unsteady c_F datum" (addendum (c)). The operative
discriminator claim survives (see §4); the exposure is purely phrasing.
Row hit: forchetta table header/notes declaration (addendum (c),
delivery-check item). Falsifier: none needed — repair is a wording
tightening at the synthesis/landing ("no unsteady c_F datum WITH a
per-phase-averaged or experimental steady companion that discriminates
...").

T-C4 [NONE-CLASS: evidence-weight caveat, not a threat]. P-C's own
stack (1-step premixed Arrhenius, ~3 cells/induction length, k-omega
SST, adiabatic, no named solver) caps every number above at ADVISORY
weight; nothing in our rows consumes P-C numbers as bounds.

EXPLICIT ABSENCE STATEMENT: no threat found in P-C against [T-DISC-1/2]
(fiber non-degeneracy and sign leg), K-bar = 0, [T-T0P], the delta-
carrier lemma, the choice of MoC max-thrust design (P-C actively uses
and validates it, L1/L12), or BLOCCATO row 9's truncation default. No
claim in P-C challenges an authority of record; per SHARED RULES no row
re-opening is proposed anywhere in this file.

==============================================================================
## 6. CONSUMPTION ARC (per finding; no orphan rows)

| Finding | Landing target |
|---|---|
| L4, L5, L8, L19, Fig. 10/18/19 atlas rows | T-RED exhibit slot: draft §2.3 gains P-C as second ADVISORY exhibit (rotating one-sided shock + deformed base zone + rotating lateral force); cite in the R22F in-flight loop via SYNTHESIS (d) topology consolidation |
| L11 (transient-vs-steady C_fx, both signs, 0.2–1.5 %) | forchetta channel (iv) cell — provenance line "P-C Fig. 13 [FIG] steady-vs-unsteady C_fx gap ≤ ~1.5 %, sign config-dependent"; ALSO M-RED §3.2 leg (A) expectation note; ALSO threat T-C1 → R26 row watch-list |
| L12, L16 (area-variational law time-average; exit Mach 3.03 on MoC profile) | forchetta channel (iv) BEST cell supporting provenance + the averaging bet discussion in SYNTHESIS (e) (P-A confrontation axis) |
| L13, L20 (RMSD_theta 8.16–14.63°) | forchetta channel (iii) cell provenance (B5 band external consistency), WITH the eq.-20 definitional caveat — SYNTHESIS (e) "state the definitions carefully" duty |
| L10 + L2 (total pressure +3.89 %; asymmetric throat-ratio response) | Part 4 CFD-1 scheduling dossier (design-dependent interface data exhibit) + threat T-C2; joins P-D's choked +50–60 % in SYNTHESIS (b)/(e) |
| L14 + Fig. 15/16 periodicity | forchetta channel (i) notes: published realization of the pure-periodic pin class (guard = T0-flatness monitor unchanged); scope memory `periodic-wave-data-scope` unaffected |
| L11 sign mechanism + L7 (Mach > 3.71 exit portions) | forchetta channel (ii) BEST-cell note (single-digit % consistent) — no cell value change |
| Addendum-(c) refinement (§4 last bullet, T-C3) | SYNTHESIS (e) mandatory item "unsteady c_F present or absent — check honestly": answer PRESENT-but-non-discriminating; wording repair rides the landing |
| L8 base-zone transient-vs-steady differences | forchetta channel (v) WORST cell supporting provenance (base model-form unpriced) + R8-analogy residue R-8 of the draft (still no MEASUREMENT — analogy label stands) |
| L1, L22, L17-L21 (actuation dynamics, spike recommendation) | candidate lit-registry row summary text for pC (minted at LANDING per brief); no theory row consumes actuation dynamics — declared registry-summary-only |
| Fig. 13 argmax stability (channel (vi) brush) | forchetta channel (vi) cell note: external instance where reduced-vs-true ordering differs mid-ranking while argmax holds [FIG]; strengthens the case for the delta/mu perturbation frame, no number |
| §7 reference extraction below | SYNTHESIS MISSED-CLUSTER WANTED consolidation (census-defect repair duty) |

==============================================================================
## 7. CENSUS-DEFECT DUTY — REFERENCE-LIST EXTRACTION (p. 18, text-extracted)

Bearing on RDE-nozzle design/efflux/experiments (full identities; dedup
hints vs docs/literature_registry.yaml grep this window):

1. [12] J.Z. Ma, W. Bao, J. Wang, "Experimental research of the
   performance and pressure gain in continuous detonation engines with
   aerospike nozzles", Aerosp. Sci. Technol. 140 (2023) 108464. — Ma
   hot-fire (RDE aerospike sea-level experiments; injection/expansion
   ratios critical, p. 1-2 context). NOT in registry (grep).
2. [13] S. Zhou, Y. Ma, F. Liu, N. Hu, "Experimental investigation on
   pulse operation characteristics of rotating detonation rocket
   engine", Fuel 354 (2023) 129408. — conical-nozzle pulse operation.
   NOT in registry.
3. [14] M.L. Fotia, F. Schauer, T. Kaemming, J. Hoke, "Experimental
   study of the performance of a rotating detonation engine with
   nozzle", J. Propuls. Power 32 (3) (2016) 674-681. — Fotia nozzle
   configs (choked aerospike benefit vs bluff/unchoked). NOT in registry.
4. [15] K. Goto, J. Nishimura, A. Kawasaki, K. Matsuoka, J. Kasahara,
   A. Matsuo, I. Funaki, D. Nakata, M. Uchiumi, K. Higashino,
   "Propulsive performance and heating environment of rotating
   detonation engine with various nozzles", J. Propuls. Power 35 (1)
   (2019) 213-223. — Goto vacuum-chamber aerospike (Isp reaches
   theoretical optimum per base pressure, conical spike). NOT in registry.
5. [16] A.J. Harroun, S.D. Heister, J.H. Ruf, JPP 37(5) (2021) 660-673.
   — ALREADY OF RECORD (registry id harroun_2021, :273). Dedup: no row.
6. [17] Y. Zhu, K. Wang, Z. Wang, M. Zhao, Z. Jiao, Y. Wang, W. Fan,
   "Study on the performance of a rotating detonation chamber with
   different aerospike nozzles", Aerosp. Sci. Technol. 107 (2020)
   106338. — conical vs flat aerospike experiments; peak pressure raised;
   Anglino-method profile raises Isp. NOT in registry.
7. [18] Y. Zhu, K. Wang, M. Zhao, Z. Wang, W. Fan, "Experimental study
   on wave propagations in a rotating detonation chamber with different
   outlet configurations", Acta Astronaut. 200 (2022) 388-399. — throat
   size vs stability/equivalence-ratio range. NOT in registry.
8. [19] M. Zhao, K. Wang, Y. Zhu, Z. Wang, Y. Yan, Y. Wang, W. Fan,
   "Effects of the exit convergent ratio on the propagation behavior of
   rotating detonations utilizing liquid kerosene", Acta Astronaut. 193
   (2022) 35-43. — contraction ratio vs detonation establishment. NOT in
   registry.
9. [20] J. Braun, B.H. Saracoglu, G. Paniagua, "Unsteady performance of
   rotating detonation engines with different exhaust nozzles",
   J. Propuls. Power 33 (1) (2017) 121-130. — OpenFoam, 5 nozzles,
   Bezier outer wall vs conical. NOT in registry (ornano_2017 same group
   IS in registry :624 — cross-note).
10. [21] C. Sun, H. Zheng, N. Zhao, Z. Li, W. Zhu, "Performance
    evaluation and outlet load improvement of a rotating detonation
    combustor with different outlet nozzles", Int. J. Hydrog. Energy 46
    (2021) 18644-18660. NOT in registry.
11. [22] R. Li, J. Xu, S. Huang, "Nozzle design for rotating detonation
    engine", J. Propuls. Power 38 (5) (2022) 849-865. — the P-B/P-C
    group's own area-variational quasi-2D design-method paper
    (geometric-throat + parabolic-divergent findings, p. 2). NOT in
    registry; HIGH-bearing WANTED candidate (design-method lineage of
    P-B/P-C).
12. [23] Y. Huang, H. Xia, X. Chen, Z. Luan, Y. You, "Shock dynamics and
    expansion characteristics of an aerospike nozzle and its interaction
    with the rotating detonation combustor", Aerosp. Sci. Technol. 117
    (2021) 106969. — integrated combustor-nozzle design; shock
    intensity/inclination lower with aerospike than nozzle-less. NOT in
    registry.
13. [24] N. Jourdaine, N. Tsuboi, K. Ozawa, T.K. Hayashi, Proc. Combust.
    Inst. 37 (2019) 3443-3451. — = P-D of this campaign (row minted at
    LANDING). Dedup: campaign-internal.
14. [25] X. Liu, M. Cheng, Y. Zhang, J. Wang, AST 120 (2022) 107300. —
    = P-A (already read-integral, lit-registry :615 class per brief).
    Dedup: no new row.
15. [26] X. Huang, Z. Lin, Y. Liu, Q. Wu, "Numerical simulation on the
    operating characteristics of rotating detonation ramjet engines at
    high flight Mach number", Int. J. Hydrog. Energy 48 (2023)
    9109-9116. — supporting-block disturbance consideration (p. 2).
    Marginal bearing (ramjet operating characteristics). NOT in registry.
16. [27] R. Li, J. Xu, H. Lv, D. Lv, J. Song, AST 136 (2023) 108221. —
    = P-B of this campaign. Dedup: campaign-internal.
17. [42] J. Sun, J. Zhou, S. Liu, Z. Lin, W. Lin, "Effects of air
    injection throat width on a non-premixed rotating detonation
    engine", Acta Astronaut. 159 (2019) 189-198. — injector-coupling
    datum class. NOT in registry; low-moderate bearing.
18. [43] M. He, L. Qin, Y. Liu, "Numerical investigation of flow
    separation behavior in an over-expanded annular conical aerospike
    nozzle", Chin. J. Aeronaut. 28 (4) (2015) 983-1002. — cold aerospike
    separation topology (P-C's validation lineage). NOT in registry;
    moderate bearing (base/separation model-form channel (v)).
19. [44] S.B. Verma, "Performance characteristics of an annular conical
    aerospike nozzle with freestream effect", J. Propuls. Power 25 (3)
    (2009) 783-791. — the cold-flow validation experiment of P-C
    (schlieren + wall pressure at NPR 2.10-3.82). NOT in registry;
    moderate bearing (any CFD-2-style validation reuse).
20. [47] X. Tang, J. Wang, Y. Shao, "Three-dimensional numerical
    investigations of the rotating detonation engine with a hollow
    combustor", Combust. Flame 162 (4) (2015) 997-1008. — source of the
    critical-pressure injection-BC model (eqs. 11-15). NOT in registry;
    moderate bearing (interface-data modeling convention).
21. [48] R.V. Veen, R. Gentry, J.D. Hoffman, "Design of shrouded-plug
    nozzles for maximum thrust", AIAA J 12 (1974) 1193-1197. — ALREADY
    OF RECORD (registry id vander_veen_1974, :427-429, GENO/literature/
    Veen.pdf; note P-C's "Veen et al." = Vander Veen-Gentry-Hoffman).
    Dedup: no row; P-C's L12 leans on exactly the shrouded-plug
    max-thrust lineage our record carries (incl. the "Veen constants
    UNRELIABLE vs WG10" note :441 — synthesis should NOT let P-C's
    approving citation upgrade Veen constants).

Non-bearing (surveyed, excluded with reason): [1]-[11] reviews/detonation
fundamentals; [28]-[40] mode-switching and variable-nozzle actuation
hardware (memory-alloy/TBCC/pintle — actuation technology, not RDE-nozzle
efflux/design); [41] turbulence model; [45] Bykovskii validation datum;
[46] SDToolbox report (tool, already the class of our Cantera/SDT usage).

## PAPERS NEEDED (per SHARED RULES; = WANTED candidates for the synthesis)
None BLOCKING for this study. Highest-value procurement candidates from
the missed cluster (ranked): [22] Li-Xu-Huang JPP 2022 (design-method
parent of P-B/P-C), [14] Fotia 2016, [15] Goto 2019, [12] Ma 2023,
[17] Zhu 2020, [23] Huang 2021, [44] Verma 2009, [43] He 2015,
[20] Braun 2017, [47] Tang 2015.

==============================================================================
## 8. MACHINE SUMMARY

paper: pC_li_xu_2025 | AST 158 (2025) 109878 | DOI 10.1016/j.ast.2024.109878
pages_read: 18/18 [FULL]; figure_pages_rendered_visually: 4,5,6,7,8,9,10,12,13,15,16,17
findings_ledger_rows: 22 (L1-L22)
topology_atlas_entries: 12 figure groups (Figs. 1-22)
confrontation_verdicts: T-DISC SUPPORTS(weak); T-RED SUPPORTS; M-RED SUPPORTS/DIFFERS; R22-CFD SUPPORTS(motivation)+template; forchetta (i) SUPPORTS-pin, (ii) SUPPORTS-BEST, (iii) SUPPORTS+def-caveat, (iv) SUPPORTS-BEST+feeds-WORST, (v) SUPPORTS, (vi) no-fire-but-brushes; addendum(c) DIFFERS-refinement
threats: 3 named (T-C1 ranking-aliasing instance -> R26/channel-(iv), falsifier = M-RED+R22-CFD-2; T-C2 design-dependent interface data +3.89% -> CFD-1 premise, falsifier = CFD-1; T-C3 addendum-(c) wording exposure, repair = wording tightening) + 1 evidence-weight caveat (T-C4); explicit-absence statement given for T-DISC/K-bar/T-T0P/delta-carrier/BLOCCATO-9
reference_extraction: 21 bearing entries with full identities (2 already of record: harroun_2021, vander_veen_1974; 2 campaign-internal: P-B, P-D; 17 registry-absent WANTED candidates), 20 non-bearing excluded with reason
top5_bearing_statements:
 1. Steady-averaged vs 3D-unsteady C_fx gaps are 0.2-1.5% with BOTH signs and one mid-ranking flip while the argmax holds (Fig. 13 p.11 [FIG]) — feeds forchetta (iv) BEST and WORST and brushes (vi).
 2. "Transient pressures along the spike and cowl essentially obey the area-variational law in a steady state" + max-thrust MoC profile reaches exit Mach 3.03 under kHz waves (pp. 11, 13, 16 [REP]) — external support for the averaging bet at ADVISORY class.
 3. Axial retraction of spike or cowl raises chamber time-average total pressure ~3.89% while detonation intensity stays fixed (pp. 11-12 [REP]) — design-dependent interface data, the CFD-1 premise made concrete (threat T-C2).
 4. Rotating one-sided internal shocks, deformed base zones, and a wave-locked lateral force of ~25-35% of axial thrust with rotating direction (Figs. 10, 21 [FIG/REP]) — second physical exhibit of the K-operator phenomenon class (T-RED §2.3).
 5. A published unsteady c_F EXISTS here (Fig. 20b) but its steady companion is averaged-inflow CFD, not per-phase or experiment — addendum (c)'s discriminator claim survives, its phrasing needs tightening (T-C3).
output_file: validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pC_li_xu_2025.md
