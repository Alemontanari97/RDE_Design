# BASE-PRESSURE HARVEST — targeted C4 pass (on-disk RDE-nozzle corpus)

Session S-FOUNDATIONS-C4, targeted base-pressure harvest agent (user
catch 2026-08-20: prior reads used a T-RED/azimuthal-topology lens;
this pass harvests base-pressure data/models/correlations for the
R8/N2 closure). Anchoring question: what base-pressure information
exists in the on-disk corpus — values, regime statements, models with
constants and validity class, validation data — usable as [ADV]
context for (i) the R8 base-pressure two-regime row (channel (v) row
of record: phaseD_r22f_centerpiece.md:1154; residue R-8 :1337),
(ii) the ADR-D4 truncation dossier (PROGRESS BLOCCATO row 9 + G-11
rider), (iii) the N2 closure work at F4b (problem book :347-348, H-T4
row :499), (iv) forchetta channel (v) (BRIEF_blocco2_phaseD.md
:110-112).

**CT-6 RULE (binding, restated)**: NO CFD absolute value in this
document may be proposed as a band/bar input — CFD numbers are
CONTEXT ONLY. Only measured data (with its own instrument caveats)
can even be a candidate, and none of it is a certified band input
either: everything here is [ADV].

**EVIDENCE-CLASS KEY**: [ADV-EXP-HOT] = hot-fire RDE experiment
(published-figure/text reading); [ADV-EXP-COLD] = cold-rig
experiment; [ADV-CFD] = CFD value (CT-6: context only);
[MODEL-UNREL] = model with declared unreliability; [MODEL-VAL] =
model with in-source validation against experiment; [PRACTICE] =
design-practice statement of record.

**EXTENSION DISCIPLINE**: G-06 graft (SYNTHESIS_nozzle_rde_arrivals
.md:252-259) and FIELD_ATLAS_targeted_c4.md entries H21-F12/F13/F16/
F17 already carry: P-A ~0.16 atm bubble, P-C L8 deformation, P-B
Chutkey Figs. 4-5 status, Harroun 0.59-vs-0.95 atm, Stechmann-model
midrange failure, NPR~6.7 transition. Those are cited, not
re-derived; every entry below marked NEW is an extension.

**READ-DEPTH DECLARATION (pages actually rendered visually)**:
- harroun_2021_...rdre_nozzle_performance.pdf: PDF pp. 1-4, 7-10, 13-14 (journal 660-663, 666-669, 672-673). NOT rendered: pp. 5-6 (CFD numerics), 11-12 (plug-surface pressure/thrust; zero base-keyword hits in text layer — declared skip).
- harroun_2020_rde_nozzle_simulation_validation.pdf: PDF pp. 1-2, 5-8; pp. 11-12 via text layer (conclusions + refs).
- paxson_miki_2022_rdre_nozzle_cfd_optimization.pdf: PDF pp. 1-2, 9-11.
- kaemming_paxson_2018_equivalent_available_pressure.pdf: PDF p. 9; p. 15 ref [19] via text layer.
- miki_2020_rde_nozzle_design_methodology.pdf: PDF pp. 7, 11, 15; p. 2 via text layer.
- teasley_2023_nasa_rdre_state.pdf: p. 11 via text layer only (skip, see below).
- nasa_teasley_2025_rdre_development.pdf: PDF p. 9; p. 4 via text layer.
- li_xu_lv_lv_song_2023_..._ast136_108221.pdf: PDF pp. 4-5, 8, 10-11; pp. 3, 6, 22 via text layer (refs + intro mentions).
- liu_2022_aerospike_rde_design_ast120_107300_dupcopy.pdf: PDF pp. 10-12.
- li_xu_lv_yu_zhou_2025_..._ast158_109878.pdf: PDF pp. 8, 14; pp. 2, 6, 7, 11 via text layer.
- jourdaine_2019_h2_rde_aerospike_pci37_3443.pdf: full text-layer sweep of all 9 pp. (zero truncation/base sentences) — declared skip, no page rendered.
- GENO/literature/Veen.pdf (READ-ONLY): PDF pp. 1-5 (all).
- GENO/literature/migdal.pdf (READ-ONLY): PDF pp. 1, 4.
- GENO/literature/NASA_SP8120_liquid_rocket_nozzles.pdf (READ-ONLY): PDF pp. 34-37 (doc pp. 20-23), 83-84 (doc pp. 69-70); refs p. 117 via text layer.
- GENO/literature/ADA455494.pdf (READ-ONLY): PDF pp. 1, 10-19 (doc pp. 9-18); refs pp. 23-26 via text layer.
- GENO/literature/design-of-maximum-thrust-plug-nozzles-for-fixed-inlet-geometry.pdf (READ-ONLY): PDF pp. 1-2, 6-7 (journal 1581-1582, 1586-1587).

---

## 1. HARROUN-HEISTER-RUF 2021 (JPP 37(5):659-673) — THE R8 SOURCE PAPER

Registry: harroun_2021 (:273). The paper channel-(v) line 1154 cites
as "Harroun p.8 via R8"; this pass upgrades the reading from [REP] to
direct page-verified for every claim below.

### 1.1 Instrument caveats on the base "measurement" (journal pp. 662-663, PDF pp. 3-4) — NEW
- Stechmann V1.3 hardware had a SINGLE centerline base port; during
  RDE operation the pressure "never reached a steady-state condition"
  (short heat-sink firings + large sampling port), so the V1.3 base
  pressure had to be ESTIMATED with the analytical model (p. 662).
- The usable base dataset is the SECOND campaign (Humble & Lim,
  liquid RP-2/gox): 7 base-surface CTAP ports (1 centerline + 6
  radial, Fig. 5, p. 663), port paths ~23 cm; transducers GE UNIK
  5000 (0.04% FS) and Druck PMP 1260 (0.25% FS); error bars in
  Fig. 13 = transducer accuracy. CTAP = capillary-tube-averaged,
  CYCLE-MEAN only — no per-phase content. 6 plug-surface ports
  (~30 cm paths) on the aerospike (Fig. 6).
- CEA check: kerosene-vs-methane post-detonation properties < 1%
  apart — the kerosene tests are used to referee the methane-based
  CFD (p. 663).

### 1.2 Nozzleless base values and the regime data (journal pp. 666-669, PDF pp. 7-10)
- Area-averaged base pressure 0.59 atm (detonation-wave CFD) vs 0.95
  atm (constant-pressure CFD, same mean mass flow 1.24 kg/s):
  "approximately eightfold increase in base drag" (p. 666)
  [ADV-CFD, experimentally refereed — atlas H21-F12/F13].
- Fig. 13 (p. 667): base pressure vs radius; detonation-wave CFD
  ~0.55-0.8 atm flat; constant-pressure CFD up to ~1.2 atm near
  centerline; FIVE hot-fire tests (#54, 55, 65, 66, 79; mass flows
  within ~1% of the 1.24 kg/s computation) follow the detonation-wave
  curve [ADV-EXP-HOT]. Mechanism: RDE ejector action — the
  high-frequency replenishing of high-momentum gases continuously
  entrains fluid out of the base region; the wave period is FASTER
  than the base-region adjustment time, so the base never reaches a
  steady condition (p. 667) — the physical basis of the two-regime
  bar's RDE-specific offset. NEW: the counter-finding on record —
  Schwer et al. [15 = AIAA 2018-4968, registry
  wanted_schwer_2018_aerospike_pressure] found base pressures "did
  not vary substantially between steady-flow and RDE conditions" on
  an airbreathing RDE with a TRUNCATED aerospike; Harroun attributes
  the disparity to lower feed pressure, weaker airbreathing waves,
  and a much larger plug surface, "an area demanding more focused
  study" (p. 667, incl. private communication with D. Schwer, NRL,
  Jan. 2021). CONSEQUENCE for R8: the sign/size of the RDE departure
  from constant-pressure closure is CONFIGURATION-DEPENDENT at held
  evidence — the nozzleless rocket-condition result does not
  transfer to truncated plugs even directionally without the analogy
  label.
- Stechmann analytical model, Eq. (8) p. 668 — NEW (exact form):
      P_b = P_a − ṁ v_t (1 − cos α) / (π r_b²)
  control-volume theory; calibrated on PREBURNER warm-oxygen flow
  (not detonation) base data [MODEL-UNREL]. Fig. 16: adequate
  midrange mass flow only; deviates at low AND high mass flow (atlas
  H21-F16). Discrepancy explained by regime change (below).
- TWO-REGIME statement of record (p. 669) — the R8 row's source,
  now page-verified: at low NPR the wake is OPEN (recirculation
  influenced by ambient); at sufficiently high chamber-to-ambient
  ratio the exhaust plume isolates the base: CLOSED wake
  (recirculation influenced only by chamber conditions). Humble &
  Lim data (Fig. 17): open wake at NPR ≈ 4.5-6.7; transition at
  NPR ≈ 6.7; closed-wake P_b/P_c constant ≈ 0.075-0.085 for NPR up
  to ~17; open-wake P_b/P_c from ~0.185 (NPR ~4.5) falling to ~0.08.
  CAVEAT IN-SOURCE: "Additional tests with NPRs between 4.5 and 6.7
  are required to determine the precise NPR at which the wake
  transitions" [ADV-EXP-HOT].
- OPEN-WAKE RDE ANOMALY (p. 669): constant-pressure truncated
  aerospike literature (refs [29, 30] = Mueller et al. NASA reports)
  has open-wake base pressures tracking at/just below ambient
  (P_b = P_a dotted line); the RDE open-wake points sit SIGNIFICANTLY
  below ambient — ejector suction operates even in open wake.
  VERDICT SENTENCE (verbatim, p. 669): "Neither the analytical model
  in Eq. (8) nor the previous theory for the closed-wake regime for
  constant-pressure engine aerospike nozzles are appropriate for
  predicting base pressures with an RDE cycle."
- Aerospike plug (p. 669, Fig. 18): the RDE separated-flow/reverse-
  flow region at the end of the plug has a complex 3D geometry,
  "contrary to the axisymmetric separated region" of a
  constant-pressure engine [ADV-CFD] — base-zone-topology
  deformation on the PLUG side (consistent with P-C L8).

### 1.3 Conclusions + reference identities (journal pp. 672-673, PDF pp. 13-14) — NEW
- Conclusion verbatim (p. 672): "The base pressure on an annular,
  nozzleless RDE was shown to be poorly predicted with either
  analytical models or previous empirical results for
  constant-pressure engines. These discrepancies demonstrated the
  need for direct simulations or enhanced testing diagnostics."
- Ref identities used above: [9] Stechmann PhD diss., Purdue 2017;
  [15] Schwer, Kelso & Brophy, AIAA 2018-4968; [17] Lim, Humble &
  Heister, AIAA 2020-0195 (RP-2/GOX campaign = the base dataset's
  primary source); [19] Harroun MS thesis, Purdue 2019 (registry
  wanted_harroun_thesis_2019, P0); [29] Mueller, Sule, Fanning, Giel
  & Galanga, NASA N-73-12282, 1972 (axisymmetric truncated plug
  flow fields, analytical + experimental); [30] Mueller, Sule &
  Hall, NASA N-71-18990, 1971 (separated flow regions in altitude
  compensating nozzles).
- CONSUMERS: R8 (primary source, all cells); channel (v) BEST/WORST
  provenance; N2-F4b (the verdict sentence = the statement that no
  inherited closure is admissible for RDE); ADR-D4 (base drag ~10%
  of thrust on annular nozzleless topology, p. 661, [ADV]).

## 2. HARROUN-HEISTER-RUF 2020 (AIAA conf., experimental-validation companion)

Registry: harroun_2020 (:632).
- V1.4 campaign: base ports DID reach steady values within the
  sub-1 s hot fires (p. 5) — unlike the V1.3 single port; 23
  nozzleless tests total (p. 6).
- Surface-area-averaged base pressures for tests 54/55/65/66/79:
  "0.58 to 0.60 psia" (p. 7) — UNIT TYPO IN SOURCE: figure axes and
  the 2021 journal version give atm (0.59 atm); flagged, use atm.
  Within 1% of the V1.3 detonation-wave CFD [ADV-EXP-HOT].
- NEW (p. 7, verbatim): "Unfortunately, at present there is no way
  to create an analytical model predicting the base pressure — and
  thus the base drag — with respect to the operating conditions."
  Stechmann's linear model: "mid-range mass flow rate cases are
  sufficiently predicted"; "at higher mass flow rates ... the
  physics in the base region changes drastically, limiting the
  applicability of the model."
- NEW Fig. 9 (p. 8): transition coordinates in pressure-RATIO form:
  open-to-closed at approximately P_a/P_c = 0.15 (the channel-(v)
  row's number, now page-verified); closed-wake P_b/P_c ≈ 0.08;
  open-wake P_b adjusts toward ambient "but will still be suctioned
  lower than the ambient pressure" — at the lowest tested mass flow
  (~0.85 kg/s) P_b ≈ 0.83 atm ≈ 17% below ambient (Fig. 8) — the
  "~20% below ambient in open wake" cell of line 1154, confirmed.
- Conclusion 1 (p. 11): experiments CONFIRMED the ejector action
  enhancing base drag beyond constant-pressure estimates; "previous
  aerospike literature for constant pressure engines is not
  sufficient for estimating the nozzle performance for RDEs".
- Refs [15]-[16] = the same Mueller NASA reports as 2021 [29]-[30].
- CONSUMERS: R8 (the transition number P_a/P_c ≈ 0.15 and closed
  P_b/P_c ≈ 0.08 as [ADV] anchors), channel (v), N2-F4b.

## 3. PAXSON-MIKI-PERKINS-YUNGSTER 2022 (AIAA, shrouded truncated plug optimization)

- NEW (p. 10): the bluff-body (truncated-plug) region of the
  optimized Version 5 nozzle generated drag equal to −9.5% of NOZZLE
  thrust = −1.4% of TOTAL thrust; "possible that this small drag
  force could be eliminated by extending the plug to a point", at
  the cost of actively-cooled material and mass; drag "deemed
  acceptable" [ADV-CFD, CT-6 context only]. This is the only
  RDE-cycle truncated-plug base-DRAG value in the corpus.
- Fig. 12 (p. 11): time-averaged pressure contours show the
  subatmospheric base zone (instantaneous min p/p_amb = 0.12 at
  p. 10 Fig. 11 colorbar) [ADV-CFD].
- No p_b model, no regime statement (the chamber exit is choked, a
  single operating point).
- CONSUMERS: ADR-D4 (the truncation-cost decomposition: −1.4% total
  thrust at their truncation, beside P-A's 1.2% Isp), channel (v)
  WORST cell context.

## 4. KAEMMING-PAXSON 2018 (EAP paper)

- NEW (p. 9): with nozzle divergence removed, base areas around the
  RDE combustor exit contribute axial forces; a previous RDE CFD
  with this geometry (ref [19] = Schwer & Kailasanath, AIAA
  2012-3943) "indicated sub-ambient base pressures"; base drag "was
  nearly 12% of the gross thrust"; failing to account for it can
  reduce reported EAP pressure-gain "by as much as 38%".
  Recommendation: subtract base forces via DIRECT static-pressure
  measurement on the base areas (Fig. 5 suggested test setup)
  [ADV-CFD for the numbers; PRACTICE for the recommendation].
- CONSUMERS: R8 (independent CFD witness of RDE base suction on a
  second code/geometry), channel (v) (the 38% figure = how large the
  model-form bar is on a PG accounting if the base term is dropped);
  the EAP-based PG numbers used across the program (P-B Table 5)
  inherit this sensitivity.

## 5. MIKI-PAXSON-PERKINS-YUNGSTER 2020 (design methodology)

- p. 7: on their near-full conical plug, "the size of the
  recirculation zone is very small. As intended" — the methodology
  DESIGNS AWAY the base region rather than modeling it; low-pressure
  (cold) region associated with the expansion at the nozzle tip;
  flow-separation blue zone in shear stress [ADV-CFD].
- p. 11 (Fig. 12-13 five test geometries): blunt Case 3 = "large
  wake" baseline for maximum-thrust bounding; Case 4 shows "a large
  negative gauge pressure region in the wake, which can be a
  significant drag"; wake flow "very unstable" [ADV-CFD,
  qualitative].
- NEW p. 15 refs: [7] Geron, Paciorri, Nasuti, Filippo & Martelli,
  "Transition between open and closed wake in 3D linear aerospike
  nozzles," AIAA 2005-5408; [8] Nasuti & Onofri, "Prediction of
  Open and Closed Wake in Plug Nozzles," ESA SP-487, 2002 — the
  RDE-nozzle literature itself cites the classical open/closed-wake
  school (procurement pointers for R8's classical leg).
- CONSUMERS: channel (v) context; ADR-D4 (design practice:
  minimal-truncation as a base-closure avoidance strategy).

## 6. TEASLEY 2023 / TEASLEY 2025 (NASA RDRE state / TDM) — SKIPS

- teasley_2023: NO truncated-base content (p. 11 text-layer hit =
  injector-face erosion by recirculating combustion products). SKIP.
- nasa_teasley_2025 (p. 9 rendered): subscale C-103 radiatively
  cooled nozzle extensions varied in "length, or truncation" as a
  hot-fire parameter of interest — but NO base-pressure data or
  regime content disclosed. One-line relevance: NASA's own test
  matrix treats truncation as a first-order design variable
  (ADR-D4-adjacent motivation), nothing harvestable for R8.

## 7. LI-XU-LV-LV-SONG 2023 (AST 136:108221, P-B) — film-cooling truncated spike

- Chutkey validation (p. 4, Figs. 3-5): cold annular truncated
  spike (Angelino contour, 20% retained length), sea-level ambient;
  spike-pressure CFD-vs-exp max discrepancy 4.89% (Fig. 4, NPR 60);
  Fig. 5: AVERAGED BASE PRESSURE vs NPR over NPR ≈ 5-70 —
  P_b/P_0 ≈ 0.20-0.22 at NPR ~5 falling to ≈ 0.015-0.02, flat
  beyond NPR ~40; CFD-vs-exp max base discrepancy 4.76%
  [ADV-EXP-COLD via P-B's reproduction of Chutkey 2014, registry
  wanted_chutkey_2014_annular_plug Tier 1]. G-06's status ruling
  UNCHANGED: cold annular rig — does NOT retire the
  nozzleless->plug ANALOGY label.
- NEW (p. 8, Eq. (26)): their MoC DESIGN method carries a
  base-pressure closure at the spike truncation corner J:
      (p − p_b) cot α / (½ρV²) = sin(−2θ),
  "where p_b represents the averaged base pressure" — the Rao/Veen
  plug corner condition with p_b as input. The paper does NOT state
  where its p_b value comes from (no model, no measurement cited
  for the design value) — a live instance of the N2 closure hole in
  the current RDE-nozzle design literature.
- p. 3 (text layer): prior truncated-spike design work "required
  dedicated handling of the interior points and ignored the
  influence of base recirculation" — field admission, NEW.
- p. 10 (rendered): truncation sweep (ΔL_spike/L_cowl = 20-80%,
  P-B's REMOVED-fraction convention per ADR-D4 rider G-11):
  recirculation zone enlarges and turns irregular; at 80% extra
  trailing shocks near the spike base; time-averaged exit gamma
  1.2500-1.2515 (Table 4); C_fx steady ≈ 0.9690 nearly flat vs
  truncation, transient peaked (+0.52% at 40%, −5.78% by 80%)
  [ADV-CFD] (D-6 topology note; numbers restated only to anchor the
  base-zone role in the transient cliff).
- CONSUMERS: R8 (Chutkey = the corpus's only truncated-plug
  base-pressure EXPERIMENTAL dataset, cold), N2-F4b (Eq. (26) = the
  exact slot our N2 closure must fill; the field currently fills it
  silently), ADR-D4 (recirculation growth along the truncation
  band), channel (v).

## 8. LIU-CHENG-ZHANG et al. 2022 (AST 120:107300, P-A) — aerospike RDE, 40% truncated case

- pp. 11-12 (rendered): Case D (40%-truncated aerospike, ambient
  0.36 atm): "closed recirculation zone at the nozzle base, the
  average pressure on base surface is about 0.16 atm" → P_b/P_a ≈
  0.44, base force F_base = −1.07 N vs total F = 164.15 N (−0.65%
  of total; Table 6 decomposition F_exit/F_ramp/F_base/F_fric);
  total only 2.21 N (−1.3%) below full-spike Case C; Isp penalty
  1.2% [ADV-CFD, CT-6 context only]. Consistent with G-06/D-5
  (bubble topology, Fig. 13(e)-(f) streamlines p. 10 rendered; D-5
  cites Fig. 12b).
- NEW precision on the closed-bubble claim: P-A's own regime is
  CLOSED at its single operating point (high altitude, P_c/P_a
  large); no open-wake case exists in P-A — it cannot inform the
  transition side of R8.
- CONSUMERS: channel (v) BEST-side anchor (closed-bubble,
  sub-percent thrust effect at altitude), ADR-D4 (1.2% Isp at 40%
  truncation + F_base magnitude), R8 (closed-regime CFD value
  P_b/P_a ≈ 0.44 as context).

## 9. LI-XU-LV-YU-ZHOU 2025 (AST 158:109878, P-C) — adjustable cowl/spike

- p. 8 (rendered): transient actuation states — trailing shocks
  "cannot directly interact with the boundary layers on the spike
  and the base recirculation zones"; steady reference states:
  "recirculation zones downstream of the base ... become
  axisymmetric" [ADV-CFD].
- NEW p. 11 (text layer): "the axial length of the closed
  recirculation zone at the transient state is smaller than the
  steady state" for (Spike −, Cowl 0) and (Spike 0, Cowl +) — a
  DIRECTION for the L8 deformation (transient bubble SHORTER),
  config-dependent per D-5.
- p. 14 (rendered): moving spike "brings severe deformation of the
  recirculation zone", high-Mach fluid intrudes into the dead zone;
  "the ejection of the spike pushes the fluid in front of the spike
  base straightforwardly and violently"; low-frequency force
  oscillations tied to "compression of the spike base on the
  recirculation zone" [ADV-CFD, actuation-transient].
- NEW p. 2 (text layer): "Braun's, Sun's, and Li's discussions did
  not consider the recirculation zone near the base region,
  limiting further application to the engineering scenarios" —
  second field admission that base closure is the missing piece.
- CONSUMERS: channel (v) WORST cell (base model-form unpriced under
  unsteadiness, now with a direction instance), N2-F4b (admissions).

## 10. JOURDAINE ET AL. 2019 (PCI 37:3443, P-D) — SKIP

Full-length aerospike (no truncation): full text-layer sweep of all
9 pages found ZERO truncation/base-region sentences. Confirmed N/A
for base pressure; nothing harvestable beyond G-06's existing P-D
citations.

## 11. VANDER VEEN-GENTRY-HOFFMAN 1974 (AIAA J 12(9):1193-1197) — GENO Veen doctrine source

READ-ONLY corpus. All 5 pages rendered.
- p. 1194: plug corner condition Eq. (8):
  sin(−2θ) = (p − p_b) cot α / (ρ_b V²/2) at plug tip H — p_b enters
  the maximum-thrust design as corner-condition input. Verbatim:
  "The base pressure is an average pressure over the plug face, and
  it is heavily dependent upon the viscous-inviscid interaction in
  the base region. A very simplified approach is taken wherein the
  base pressure is determined from an empirical model which relates
  the base pressure to the freestream properties at point H."
- p. 1195, Eq. (9) — the GENO "0.846/M^1.3" constants, exact form:
      p_b = p_H (C / M_H^E),  C = 0.846,  E = 1.30
  No validation in-paper; base thrust EXCLUDED from the reported
  thrust results (for comparability with Migdal) [MODEL-UNREL — see
  §13/§14 for the model's lineage and the WG10 unreliability
  verdict].
- Design mechanics (p. 1195, Fig. 2): plug solution points = where
  p_b from the CORNER CONDITION equals p_b from the EMPIRICAL MODEL
  — i.e., the closure model directly selects the truncation point
  family. Example case: γ = 1.4, R = 60, P = 500 psia, T = 5000 R.
- CONSUMERS: N2-F4b (the exact closure architecture GENO inherits:
  p_b input → corner condition → truncation family; N2 must replace
  Eq. (9)); ADR-D4; R8 (model stack member, bottom rank).

## 12. MIGDAL 1972 (JSR 9(1):3-6, "Supersonic Annular Nozzles") — identified

READ-ONLY corpus. Page-1 identity confirmed: analytical design of
annular nozzles for uniform axial exit flow; plug types survey
(external/inverted/internal-external/internal expansion); notes
inverted-plug "large base areas ... of undefined flow" and zero-base
height conditions (p. 3).
- p. 6 (PDF p. 4), Contour Truncation: truncation optimizes length/
  surface area; verbatim: for the inner contour "truncation does not
  lead to a complete thrust loss and where semiempirical methods are
  required to include the base pressure effect." NO base-pressure
  model of its own — Migdal is NOT a base-model source, only the
  practice statement. Ref [8] therein: Ahlberg, Hamilton, Migdal &
  Nilson, "Truncated Perfect Nozzles in Optimum Nozzle Design," ARS
  J. 31(5), 1961 (classical truncation lineage).
- CONSUMERS: ADR-D4 (lineage), N2-F4b (the 1972 statement of the
  same closure hole).

## 13. HUMPHREYS-THOMPSON-HOFFMAN 1971 (AIAA J 9(8):1581-1587) — THE Eq. (5.1) ORIGIN

READ-ONLY corpus; registry humphreys_thompson_hoffman_1971 (:363).
- p. 1582: maximum-thrust plug design WITH base term in the
  functional: Φ = (η_D − δ'_D)² p_b/2 (Eq. 11) added to the thrust
  integral. Treatment of p_b (verbatim): "since the base pressure
  does not affect the flow properties in the region R, it must be
  treated in the variational problem as a constant which is not
  known a priori"; iterated to compatibility; "The optimization
  procedure is independent of the model used to calculate the base
  pressure." Model used, Eq. (12): p_b = 0.846 p / M^1.3 — "a curve
  fit of the data presented in Ref. 9" = Rom, "Analysis of the
  Near-Wake Pressure in Supersonic Flow Using the Momentum Integral
  Method," JSR 3(10), 1966 — so the Veen/GENO constants are a 1966
  near-wake (projectile-class) curve fit, NOT plug data. NEW.
- pp. 1586-1587, "Effect of the Base Pressure Model" — NEW, the
  design-sensitivity exhibit of record for N2: swapping Eq. (12)
  for Eq. (38) (= Panov & Shvets 1966, Prikladnaya Mekhanika 2(6):
  p_b = p_∞[1 − 0.715γ(M_∞^2.3 − 0.92M_∞^2 − 0.03)/M_∞^2.7],
  higher p_b) changed the OPTIMUM: base height y_D 0.954 → 2.34 in
  (×2.45), wall slope at D −13.26° → −3.08°, thrust 32,881 →
  32,965 lbf (+0.26%). Verbatim: "the base pressure model
  significantly influences the shape of the optimum contour."
  I.e., the p_b closure moves the ARGMAX (truncation height and tip
  slope) by O(1) while moving the VALUE by O(0.3%) — the
  channel-(vi)-shaped warning at the design level, from 1971,
  [ADV, classical numerical study].
- Example-case conditions: 500 psia / 6000 °R chamber, γ = 1.23,
  R = 56 ft-lbf/lbm-°R, p_a = 14.7 psia, ṁ = 148 lbm/s.
- CONSUMERS: N2-F4b (primary classical anchor: closure-as-constant
  + iteration architecture + the sensitivity exhibit), ADR-D4
  (truncation height set by p_b model), channel (v)/(vi) context.

## 14. ONOFRI 2002 WG10 SURVEY (ADA455494, RTO-TR-AVT-007-V1) — THE CLASSICAL MODEL STACK + UNRELIABILITY VERDICTS

READ-ONLY corpus. Doc pp. 9-18 rendered (PDF 10-19).
- Doc p. 9 (Fig. 2.7): truncated plug C_F split into primary/plug/
  base contributions (inviscid + viscous CFD): base contribution
  ranges from small drag or neutral (overexpanded regime) to
  POSITIVE at higher PR; 20%-length η ≈ 0.89 at PR 8.9-20; 100%
  length η = 0.98-0.99.
- Regime DEFINITIONS of record (doc p. 9): open wake = base pressure
  DEPENDS on ambient; closed wake = base pressure INDEPENDENT of
  ambient. NEW sharpening (doc p. 14, Reijasse): the designation is
  a SENSITIVITY statement "totally de-correlated with the
  recirculation flow pattern" — a closed recirculation BUBBLE can
  exist at all PRs (ref 19 config) while the pressure is still
  ambient-sensitive. R8's two regimes should be worded as
  sensitivity regimes, not bubble topology.
- Measured transition example (doc p. 10, Fig. 3.1): p_b vs PR flat
  above PR ≈ 168 for the ARPT clustered config [ADV-EXP-COLD].
- TRANSITION-PREDICTION MODEL [MODEL-VAL] (doc pp. 10-11, Nasuti &
  Onofri JPP 15(4) 1999 = ref 18): transition when the last
  Prandtl-Meyer characteristic g from the module lip impinges at
  the reattachment region; Eq. (3.1):
      β' = μ(M_tr,γ) − ν(M_tr,γ) + ν(M_e,γ) + θ,
      M_tr = [2/(γ−1) (PR_tr^((γ−1)/γ) − 1)]^0.5
  with bubble extension CE ≈ 2.65×BC, corrected Eq. (3.2):
  CE/BC = 2.65 − 0.00144 φ² (φ = plug exit-wall angle, deg);
  Δβ = 5° annular, 0° linear. Table 2.2 validation (clustered cold
  rigs): PR_tr model vs experiment 166/168, 117/112, 78/73,
  155/165, 108/108, 72/77, 38/40, 129/130, 96/100 — ~5% class.
  Hagemann's MoC criterion (right-running characteristic from lip
  intersects separated shear layer at trailing-shock foot) "slightly
  underestimates" transition (Fig. 5.2, doc p. 15).
- External-flow effect (doc pp. 11-13): slipstream moves transition
  to LOWER PR and lowers open-wake base pressure below ambient
  (Tab. 4.1: computed plug-base p_pb 11568 Pa at M∞ = 0 → 4543 Pa
  at M∞ = 3, p_amb = 12800 Pa, PR = 61.7; open wake at M∞ ≤ 2,
  closed at 3) [ADV-CFD]. NOTE for R8: below-ambient open-wake base
  pressure has a CLASSICAL analogue under external flow — the RDE
  ejector suction is a distinct mechanism producing the same sign
  in STILL air; do not conflate.
- Doc p. 14 (Reijasse): NS computations (ref 29 = Ito, Fujii &
  Hayashi, AIAA 99-3211): 20%-truncated plug base drag "only 5% of
  the total thrust ... at high PR" [ADV-CFD]; base contribution
  negligible when base height small vs total plug height.
- BASE PRESSURE PREDICTION, pure-empirical stack (doc p. 15) — NEW,
  with the unreliability verdicts:
  - Eq. (5.1): p_b = 0.846 p_e / M_e^1.3 and Eq. (5.2) = the
    Panov-Shvets form — both "issued from Ref. 30" (= Humphreys et
    al. 1971, §13 above): per Fick & Schmucker (JSR 33(4) 1996)
    they "FAILED to produce reliable results" [MODEL-UNREL — the
    GENO/Veen closure Eq. (9) is verbatim Eq. (5.1): the inherited
    closure is the one judged unreliable by WG10].
  - Eq. (5.3): p_b = k(p_e + p_d), k = 0.5 — "slightly better" for
    12-16% plug lengths; k must drop to 0.3 for linear aerospikes
    (constant not universal) [MODEL-UNREL].
  - Eq. (5.4) "conical-approximation" (from Lamb & Oberkampf, ref
    31, cylinders/cones): p_b = p_e (0.025 + 0.906/(1 +
    (γ−1)/2 M_e²))^0.35, exponent 0.35 SET on cold-flow plug tests
    — "agreement with measured base pressure has been attainable"
    [MODEL-VAL, cold, tuned].
  - Eq. (5.5) "cylindrical-approximation": p_b = p_e M_e
    (2/(γ+1))^{γ/(γ−1)} (0.05 + 0.967/(1 + (γ−1)/2 M_e²)) — "good
    agreement" cold [MODEL-VAL, cold].
  - Eq. (5.6) Rocketdyne: p_b/p_c = 0.58 (C_F,max,d − C_F,core)/ε_b.
  - Eq. (5.7) Univ. Rome: p_b = p_e (0.05 + 0.967/(1 +
    (γ−1)/2 M_e²))^Φ, Φ = (−0.2φ⁴ − 5.89φ² + 20179.84)/(φ⁴ +
    20179.84).
  - WG10 VERDICT (doc p. 16, Fig. 5.4): the Univ. Rome model gives
    "the smallest percentage of error [+19%, −15%] relatively to
    measured data" — THE unreliability bracket of the brief: the
    BEST classical pure-empirical p_b model carries a +19/−15%
    error band on cold measured data.
- Multi-component (Korst-class) model (doc pp. 16-17): four-domain
  Korst 1956 extension (PM lip expansion, erf mixing layer Eq. 5.8,
  Carrière-Sirieix angular reattachment criterion); "reliable
  predictions of base pressure can be obtained" ONLY under: closed
  recirculation bubble + 2D planar/axisymmetric + cold gas + model
  initialized with the EXACT incoming Mach line (the straight-line
  constant-M_e assumption is "mostly wrong" for truncated plugs in
  overexpanded regimes → "significant error on base pressure";
  clustered 3D worse) [MODEL-VAL within the stated envelope,
  MODEL-UNREL outside].
- §6 Hagemann-Immich (doc p. 18): truncated-plug quasi-steady
  numerical simulation predicted ~15% pressure loss in the wake at
  the open/closed transition altitude; thrust loss increases for
  shorter plugs; ~1% base-bleed mass flow slightly RAISES open-wake
  base pressure (positive efficiency effect) [ADV-CFD + cold-flow
  refs 42-45].
- Reference identities (text layer, doc pp. 22-23): 11 = Sule &
  Mueller JSR 10(11) 1973 (annular truncated plug base-pressure
  characteristics); 17 = ARPT ESTEC final report 1998; 18 = Nasuti
  & Onofri JPP 15(4) 1999; 19 = Ruf & McConnaughey AIAA 97-3217
  (registry wanted_ruf_mcconaughey_1997); 20 = Fick & Schmucker JSR
  33(4) 1996; 22 = Korst 1956; 25/26 = Reijasse et al.
  multicomponent 1987/1998; 30 = Humphreys et al. 1971; 31 = Lamb
  & Oberkampf JSR (base pressure/heating correlations review).
- CONSUMERS: R8 (the regime definitions + the entire ranked model
  stack + the [+19%, −15%] bracket), N2-F4b (which closure families
  exist and their envelopes; the transition-PR model as the only
  validated piece), ADR-D4 (base drag 5%-of-thrust class at 20%
  truncation, high PR, cold), channel (v) (the classical model-form
  bar floor: ±(15-19)% on p_b even before RDE effects).

## 15. NASA SP-8120 (Liquid Rocket Engine Nozzles, 1976) — DESIGN PRACTICE OF RECORD

READ-ONLY corpus. Doc pp. 20-23 + 69-70 rendered.
- §2.1.2.2 (doc p. 20), verbatim [PRACTICE]: "A method for directly
  optimizing truncated aerospike or plug nozzles has not been
  developed. The bell-nozzle optimization procedure can be applied
  to plug nozzles, but to obtain a solution it is necessary to
  assume that the base pressure is zero. ... Currently, truncated
  ideal nozzles are used; these nozzles produce higher overall
  nozzle (base included) efficiency than the optimum nozzles with
  zero base pressure." — the 1976 state: p_b = 0 in the variational
  problem loses to non-variational truncated-ideal practice; the
  exact gap N2 formalizes.
- §2.1.2.2.1 (doc p. 22): base pressure ADDITIVE to thrust; base
  region gas stagnation temperature near chamber total unless
  shielded by bleed; porous-plate vs deep-cavity base designs.
- Doc p. 23: "Most predictions of base pressure are made by a
  method that is based on scaling the results from a cold-flow
  model (ref. 32 = Martinez, Aerodynamic Nozzle Study, R-6582,
  Rocketdyne 1966). The method is limited to truncated ideal plug
  nozzles because of the lack of test data for other
  configurations." Little/no base bleed → ref 33 (= Alber & Lees,
  AIAA J 6(7) 1968, integral theory); large base-bleed → ref 34
  modified (= Chow & Addy, AIAA J 2(4) 1964, ejector interaction).
  Overexpanded (doc p. 23): below ~1/3 of design pressure ratio the
  first wave from the outer jet boundary reaches the base jet
  boundary and RAISES base pressure.
- Design criteria §3.1.2.2 (doc pp. 69-70) [PRACTICE]: "The
  plug-nozzle configuration shall maximize nozzle performance
  including the thrust from the base"; scale cold-flow tests
  (ref 32) for truncated ideal; theoretical methods (refs 33-34)
  for other annular configs; base heating "predicted only
  approximately and must be verified experimentally".
- CONSUMERS: N2-F4b (the practice baseline + the "shall include
  base thrust" requirement), ADR-D4, R8 (cold-flow-scaling as the
  historical validation class).

---

## CONSOLIDATED

### (a) Does ANY RDE-specific (hot, detonation) base-pressure MEASUREMENT or CORRELATION exist in the corpus?

MEASUREMENT — YES, ONE, NOZZLELESS ONLY: the Purdue V1.4 (Humble &
Lim, RP-2/gox) hot-fire campaign: 23 nozzleless tests; 5 paired
tests with radially resolved cycle-mean base pressure (CTAP, 7
ports, transducer-accuracy error bars; Harroun 2020 Figs. 7-9,
Harroun 2021 Figs. 13, 16, 17). It is cycle-MEAN only (CTAP), on
the annular blunt-body (nozzleless) base, at one geometry, with the
open/closed transition bracketed only as NPR ∈ [4.5, 6.7]
(P_a/P_c ≈ 0.15) and closed-wake P_b/P_c ≈ 0.08.
FOR A TRUNCATED PLUG UNDER AN RDE CYCLE: NO measurement exists in
the corpus — confirmed; residue R-8 ("truncated-plug base-pressure
measurement vacuum") STANDS. All truncated-plug RDE base values on
disk are CFD (P-A 0.16 atm; Paxson-Miki −9.5% nozzle thrust;
Kaemming-Paxson 12%-of-gross-thrust via Schwer-Kailasanath) — CT-6:
context only, never band inputs.
CORRELATION — NO. No RDE-specific base-pressure correlation exists
anywhere in the corpus; both Harroun papers state the negative
result explicitly (2021 p. 669 verdict sentence; 2020 p. 7 "no way
to create an analytical model"). The nozzleless→plug transfer
remains an ANALOGY, declared (G-06 ruling unchanged).

### (b) Classical-model stack, ranked by validity class

1. [MODEL-VAL, narrow envelope] Multi-component/Korst-class
   (Reijasse; WG10 doc pp. 16-17): reliable for closed bubble, 2D
   planar/axi, cold gas, exact incoming Mach line; degrades sharply
   (overexpanded truncated plug, clustered/3D). Handles base bleed.
2. [MODEL-VAL, transition only] Nasuti-Onofri transition-PR model
   (Eqs. 3.1-3.2, WG10 doc pp. 10-11): predicts open→closed
   transition PR within ~5% on clustered cold rigs — the ONLY
   validated piece directly usable for the R8 regime-BOUNDARY leg
   (RDE applicability untested).
3. [MODEL-VAL, cold, tuned] Lamb-Oberkampf-derived conical Eq. (5.4)
   (exponent 0.35 tuned) and cylindrical Eq. (5.5).
4. [MODEL-UNREL, best-of-class ±] Univ. Rome Eq. (5.7): WG10 verdict
   = smallest error, [+19%, −15%] vs cold measured data — the
   classical model-form FLOOR for any p_b bar in channel (v).
5. [MODEL-UNREL] Averaging Eq. (5.3) (k = 0.5 annular / 0.3 linear:
   constant not universal); Rocketdyne Eq. (5.6).
6. [MODEL-UNREL, FAILED per WG10] Eq. (5.1) p_b = 0.846 p_e/M_e^1.3
   (Rom-1966 near-wake curve fit via Humphreys 1971) and Eq. (5.2)
   (Panov-Shvets 1966): "failed to produce reliable results" (Fick
   & Schmucker evaluation). WARNING OF RECORD: this Eq. (5.1) is
   verbatim the Veen 1974 Eq. (9) closure inherited by the GENO
   Veen doctrine — the inherited closure is the stack's bottom.
7. [MODEL-UNREL, regime-blind] Stechmann control-volume Eq. (8)
   (Harroun 2021 p. 668): calibrated on non-detonation preburner
   flow; midrange-only; misses both RDE ejector suction and the
   open/closed physics.
8. [PRACTICE] SP-8120: cold-flow scaling (Martinez R-6582) for
   truncated ideal only, "lack of test data for other
   configurations"; p_b = 0 in optimization loses to truncated-ideal
   practice.
DESIGN-SENSITIVITY EXHIBIT (binds the stack to N2/channel (vi)):
Humphreys 1971 pp. 1586-1587 — switching model 6a→6b (Eq. 12→38)
moved the optimum base height ×2.45 and the tip wall slope from
−13.26° to −3.08° while moving thrust only +0.26%: the p_b closure
moves the ARGMAX at O(1) with the VALUE nearly flat. Any N2 closure
choice must therefore be priced at the design-gradient level, not
the value level.

### (c) What would close R8 (named)

- THE closer: a truncated-plug RDE hot-fire base-pressure
  MEASUREMENT — concretely, V1.4-class CTAP instrumentation (7+
  ports, radially resolved, transducer-accuracy error bars) on a
  TRUNCATED plug base under a rocket-condition RDE, swept across
  the open/closed transition (NPR ~4-20). No such test exists in
  any read source; procurement class, external (residue R-8
  wording confirmed).
- Nearest existing data, in order: (1) Schwer-Kelso-Brophy AIAA
  2018-4968 (CFD + possibly test, airbreathing truncated aerospike;
  the registered counter-datum — registry wanted_schwer_2018, Tier
  2); (2) Chutkey 2014 (cold annular truncated plug, measured base
  pressure vs NPR 5-70 — registry wanted_chutkey_2014, Tier 1);
  (3) Lim-Humble AIAA 2020-0195 (the V1.4 campaign's primary
  document: full nozzleless base dataset + the un-tested NPR
  4.5-6.7 gap); (4) Mueller et al. NASA N-73-12282 / N-71-18990
  (the constant-pressure truncated-plug baseline Harroun compares
  against).
- Interim analytic leg: the Nasuti-Onofri transition model (b.2) is
  the only validated regime-boundary predictor; an RDE-side check
  of it against the Purdue transition bracket (predicts PR_tr for
  the Purdue geometry; datum NPR ≈ 6.7) is a cheap falsifiable
  step executable once Lim-Humble/Stechmann-thesis geometry is
  procured.

### (d) PAPERS NEEDED (dedup vs docs/literature_registry.yaml WANTED rows, grep-verified this window)

Already-registered rows (cite, do NOT re-mint):
- wanted_harroun_thesis_2019 (:776) — P0 row, exists as stated in
  the brief; ALSO the primary of Harroun 2021 ref [19].
- wanted_chutkey_2014_annular_plug (:1263, Tier 1).
- wanted_schwer_2018_aerospike_pressure (:1287, Tier 2).
- wanted_ruf_mcconaughey_1997 (:1371) — WG10 ref 19.
- wanted_angelino_1964 (:1323); wanted_hagemann_1998_advanced_nozzles
  (:1329); wanted_fotia_2016_rde_nozzle / wanted_fotia_2019_aerospike
  _configs (plug-RDE test campaigns, possible base data).
NEW candidates surfaced by THIS harvest (absent from the registry by
grep on author names this window; priority-ordered for R8/N2):
1. Lim, Humble & Heister, "Experimental Testing of an RP-2-GOX
   Rotating Detonation Rocket Engine," AIAA 2020-0195 — primary
   source of the ONLY hot-fire RDE base-pressure dataset (a).
2. Stechmann, D. P., PhD dissertation, Purdue 2017 — origin of the
   analytical base model Eq. (8) + V1.3 base-port data + calibration
   provenance.
3. Schwer & Kailasanath, "Modeling Exhaust Effects in Rotating
   Detonation Engines," AIAA 2012-3943 — source of the 12%
   base-drag / 38% EAP-error figures (Kaemming-Paxson ref [19]).
4. Nasuti & Onofri, "Theoretical Analysis and Engineering Modeling
   of Flowfields in Clustered Module Plug Nozzles," JPP 15(4):
   544-551, 1999 — the validated transition-PR model (b.2).
5. Fick & Schmucker, "Performance Aspects of Plug Cluster Nozzles,"
   JSR 33(4):507-512, 1996 — the unreliability evaluation behind
   the WG10 verdict on Eqs. (5.1)/(5.2).
6. Mueller, Sule, Fanning, Giel & Galanga, NASA N-73-12282 (1972)
   and Mueller, Sule & Hall, NASA N-71-18990 (1971); plus Sule &
   Mueller, JSR 10(11):689-695, 1973 — the constant-pressure
   truncated-plug base baseline (Harroun refs [29]/[30], WG10 ref
   11).
7. Lamb & Oberkampf, "Review and Development of Base Pressure and
   Base Heating Correlations in Supersonic Flow," J. Spacecraft &
   Rockets — the correlation review behind Eqs. (5.4)/(5.5).
8. Nasuti & Onofri, "Prediction of Open and Closed Wake in Plug
   Nozzles," ESA SP-487, 2002; Geron, Paciorri, Nasuti et al.,
   AIAA 2005-5408 (3D linear-aerospike wake transition).
9. Lower priority (mechanism classics): Korst 1956; Rom JSR 3(10)
   1966; Panov & Shvets 1966; Martinez R-6582 1966; Alber & Lees
   1968; Chow & Addy 1964; Reijasse & Delery 1998; Ahlberg et al.
   ARS J 31(5) 1961.

---

## MACHINE SUMMARY

BASE_PRESSURE_HARVEST_c4: 16 sources processed (10 literature_review/
+literature/ papers, 5 GENO/literature classics READ-ONLY, 1 skip
P-D); pages rendered/declared per paper (see READ-DEPTH block).
KEY FINDINGS: (1) ONE hot-fire RDE base-pressure MEASUREMENT exists
— Purdue V1.4 nozzleless CTAP dataset (5 radially-resolved tests
~0.59 atm at 1.24 kg/s; open/closed transition P_a/P_c ≈ 0.15 [NPR
4.5-6.7 untested gap]; closed-wake P_b/P_c ≈ 0.08; open-wake ~17-20%
below ambient = RDE ejector suction) — NOZZLELESS only; truncated-
plug RDE base measurement vacuum (residue R-8) CONFIRMED; NO
RDE-specific correlation exists (both Harroun papers state the
negative result verbatim). (2) Registered counter-datum sharpened:
Schwer 2018 airbreathing truncated aerospike saw NO substantial
RDE-vs-steady base change — RDE base departure is configuration-
dependent; analogy label stands. (3) Classical stack harvested with
constants + verdicts: WG10 bracket [+19%,−15%] = best pure-empirical
error on COLD data; GENO/Veen closure p_b = 0.846 p/M^1.3 traced to
Rom-1966 near-wake curve fit and judged FAILED by WG10 (Fick-
Schmucker) — N2 must replace it; only validated classical piece =
Nasuti-Onofri transition-PR model (~5% on cold clustered rigs).
(4) Design-sensitivity exhibit (Humphreys 1971): swapping p_b model
moved optimum base height ×2.45 and tip slope 13.26°→3.08° at +0.26%
thrust — p_b closure moves the ARGMAX, value nearly flat (channel
(vi)-shaped, design level). (5) Field admissions: Li-Xu 2023 Eq.
(26) uses p_b at the design corner with NO source; Li-Xu 2025 p. 2
"did not consider the recirculation zone"; SP-8120: no truncated-
plug optimization method, p_b = 0 assumption loses to practice.
(6) WG10 regime sharpening: open/closed = SENSITIVITY-to-ambient
regimes, de-correlated from bubble topology — R8 wording should
follow. CT-6 held: all CFD values (P-A 0.16 atm/0.44 P_a; Paxson-
Miki −9.5% nozzle thrust; Schwer-Kailasanath 12%/38%; Ito 5%;
Hagemann 15%) labeled context-only. CONSUMERS FED: R8 (regime data
+ model stack + bracket), ADR-D4 (base-drag-at-truncation figures),
N2-F4b (closure architecture + sensitivity exhibit + validated
transition model), channel (v) (classical ±15-19% model-form floor
under the RDE-specific unpriced bars). PAPERS NEEDED: 3 existing
WANTED rows cited (harroun_thesis P0, chutkey, schwer_2018) + 9 new
procurement candidates named, priority 1-3 = Lim-Humble 2020-0195,
Stechmann PhD 2017, Schwer-Kailasanath 2012-3943.
