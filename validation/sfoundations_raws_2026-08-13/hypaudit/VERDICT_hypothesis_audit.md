# VERDICT — Hypothesis-legitimacy audit (S-FOUNDATIONS raws 2026-08-13, executed 2026-08-17)

Judge fusion of: 6 confront_*.md assessments + 6 refute_*.md adversarial refutations +
dual-seed verification-layer report (refute_SEED-A.md, refute_SEED-B.md).
Sources: in-repo only throughout the chain. `ADVISORY_litreview_confrontation_2026-08-13.md`
cited by every layer strictly as PENDING-RATIFICATION evidence (CAVA NON RATIFICATA), never
as decided.

---

## ⚠️ PROMINENT: REFUTER LAYER STATUS = UNPROVEN ⚠️

Dual-seed report of record: `{"canary_fired": true, "knowntrue_survived": false}`.

- **Canary (SEED-A, deliberately false verdict "gamma=const, no error bar, LEGITTIMA-ESATTA"):
  FIRED correctly** — refuted on measured in-repo numbers (+3.6% Isp_f gamma-swap,
  [T-EQBR] +6.3..+7.0% bracket, Sun 2019 design-point migration, `validation/gamma_audit.md`).
  Positive falsification power of the refuter layer is demonstrated.
- **Known-true seed (SEED-B, wave-frame thrust identity graded LEGITTIMA-ESATTA): DID NOT
  SURVIVE** — refute_SEED-B.md returns REFUTED-AS-GRADED, splitting the bundle into an
  exact conditional identity core (B)+(C) plus a SCHEMA-grade propagation leg (A)
  ([S-T0P], REFUTE_A Linea (1)/(4)).

**Per the null=failure / dual-seed protocol, the refuter layer is UNPROVEN in this run.**
The specificity direction (a true verdict surviving refutation) was not demonstrated.
Consequences, stated without softening:

1. The six `refuted:false` outcomes below CANNOT be certified as "survived a proven
   verification layer". They are the assessor's verdicts, unrefuted by an aggressive but
   uncalibrated refuter.
2. The failure direction is OVER-refutation (refuter willing to strike a nominally-true
   seed), not under-refutation. An over-aggressive refuter does not manufacture false
   survivals — if anything the six survivals faced a harsher-than-calibrated adversary —
   but the formal proof obligation is unmet and the verdicts carry this caveat.
3. Caveat on the caveat, for the re-run designer: refute_SEED-B is a substantive,
   repo-anchored graded-split argument (the seed statement fused a THEOREM-exact identity
   with the [S-T0P] SCHEMA propagation leg, which the sibling confront_axisym also refuses
   to grade exact). The failure may therefore sit in the SEED-B design (statement not
   actually knowntrue AS GRADED) rather than in the refuter. That adjudication belongs to a
   dedicated dual-seed re-run with a cleanly-scoped known-true seed (e.g. SEED-B's own
   surviving clause (i), the conditional identity core alone); until it runs, UNPROVEN
   stands.

**Required action:** re-run the dual-seed with a corrected known-true seed before any of
the verdicts below is consumed as certified-of-record. Owner: next hypaudit window / F2.

Coverage accounting: NULL slots from Confront = **0** (all six assessments delivered;
null = coverage failure semantics did not trigger). Refuter coverage = 6/6 + 2 seeds.

---

## REFUTER-OVERTURNED VERDICTS: NONE

All six refuters returned `refuted: false`. No assessment verdict was overturned.
Every refuter attached surviving objections — these are binding completeness/wording
amendments folded into the monitor and duty lists below, not verdict changes.
The only REFUTED verdicts in the run are the two seeds (SEED-A by design; SEED-B see above).

---

## PER-HYPOTHESIS VERDICT TABLE

### 1. [I-GEO + I-STATE] Design axisymmetry + per-phase state axisymmetry (`confront_axisym.md`)

**VERDICT: LEGITTIMA-DICHIARATA-MONITORATA** (refuter: stands, 5 completeness duties).

**Strongest surviving literature evidence (paper-anchored):**
- [I-GEO] corpus-conformant: every corpus RDE nozzle is a body of revolution — Harroun 2021
  aerospikes (`reports/harroun_2021_jpp_nozzle_perf.md` §2), Paxson-Miki 2022 shrouded plug
  (`reports/paxson_miki_2022_nasa_opt.md` §2), Miki 2020 six axisymmetric geometries; plus
  (refuter addition) Liu 2022 and Zhu 2020 as further axisymmetric precedent. Lone asymmetric
  instance = Kraiko 2016 vectorial-thrust planar nozzles, a declared non-containment of (P)
  (claim 18, confrontation §1.4, pending ratification).
- Geometric kernel machine-verified: n_theta≡0 on any surface of revolution, zero axial
  pressure torque [T-SLRW]; genuine asymmetry channels (injector orifices, wall shear,
  swirled injection) all upstream of Gamma_d and declared (mean-swirl panel P1/S1).
- [I-STATE] posed in the refuter-survived form: per-phase = exact rotation quotient +
  declared rung-2 sweep residual, never "the correct object tout court" (REFUTE_A verdetto;
  ASSESSMENT §3.1). Residual SOURCE is O(1) by measured fields: Miki 2020 Fig.4 (P0 4x,
  T0 1400–2200 K, tangential ±300 m/s vs axial 500–800 m/s); Paxson-Miki sigma/mu≈0.70,
  covariance weight ≈0.5 "first-order, not cosmetic" (mean-swirl panel P3); refuter adds
  Liu 2022 §4.4 measured 14.2% deviation-from-mean-design penalty from azimuthal
  non-uniformity as a second confirming witness.
- Empirical vacuum unanimous: no time-mean tangential field/profile/AM-flux reported
  anywhere in the read corpus (Harroun 2021 imposes zero-swirl inflow by construction,
  p.666; Paxson-Miki Fig.3 is total-velocity Mach).
- Standing confounded threat: Harroun 2021 per-phase 2-D axisymmetric surrogate is
  discrimination-blind (c_F=1.25 both aerospikes) while 3-D CFD + paired experiments
  discriminate; 2-D-ness vs averaging undisentangled; R22 decides (REFUTE_B: evaluators
  informationally incomparable).

**Monitors/audits REQUIRED for legitimacy:**
1. T0-flatness certificate stated in the WAVE frame (lab-frame traces non-flat on healthy data).
2. Harmonic/contract audit for injector-locked lab-frame asymmetry s(theta, theta−Wt) —
   flatness provably blind to this channel (REFUTE_A line 4).
3. TRIPLE (Gamma, h0, s) per-phase spread monitor, derived threshold + psi-monotonicity C1
   guard, wired as G6 rejector (mean-swirl panel S4).
4. Angular-momentum balance-residual audit row, normalized by gross flux, ≥2 stations,
   derived tolerance.
5. B-lite meter of the rung-2 sweep/D2 residual (M0 r.1208); (refuter addition) name
   nozzle-axial penetration of wave-locked unsteadiness (KTH LES Jan 2026 row, web-tier)
   in the B-lite/R22 monitor set once PDF-verified.
6. Axial-Mach L4 margin measured on data — never total-velocity Mach (Paxson-Miki F4).
7. R22 disentanglement experiment (3-D unsteady vs 3-D per-phase avg vs 2-D per-phase avg)
   — the decider of averaging-vs-reduction blame.

**Refuter-imposed completeness duties (surviving objections):** (a) cite-and-rebut Wolanski
2013 p.147 "very little loss for the rotational component" (assertion-not-demonstration)
instead of omitting it from the vacuum claim; (b) extend [I-GEO] residue to
installation-geometry constraints (Kraiko 2016 arrangement-box driver); (c) add Harroun 2019
Purdue M.S. thesis (procurement P0, carrier of the 2-D surrogate threat) to the residual-risk
list; (d) add Liu 2022 / Zhu 2020 to the [I-GEO] census; (e) KTH LES row as above.

**Residual risks:** percent-level ranking power of rung-2 aggregate unproven (null in tier-1
corner); jump-localized sweep residual absorption = CONJECTURE P-ii until O5; residual
magnitude never directly measured in corpus; propagation lemma unwritten in M0 (duty R4 —
"T-T0 exactness" alone is over-citation); vectorial-thrust family excluded (declared class
restriction); no scope over base/wake/separated regions (H2' fence; mu(Xi_sub)>0 generic).

---

### 2. [H-DATA] Pure periodic single-mode rotating-wave data family (`confront_hdata.md`)

**VERDICT: LEGITTIMA-DICHIARATA-MONITORATA — conditional on ARMING the monitor suite**
(refuter: stands, 4 surviving objections; the unarmed state is itself a breach of
M0 VI.4bis(v), `docs/rde_nozzle_MASTER.md:1441`).

**Strongest surviving literature evidence:**
- [Wolanski 2013, `reports/wolanski_2013_survey.md` F4/F8, pp.141–145] stable regular
  single-head regimes are real AND galloping/deflagrative degeneration is organized by Wave
  Number W=t_r/t_mf — both halves of the pin corroborated; W adopted as provenance label,
  not certificate.
- [Teasley 2023, `reports/teasley_2023_nasa_state.md` F3] mode zoo on hardware: 2–4
  counter-propagating, 1–5 co-rotating, 2-wave slapping; >12 CW/CCW transitions in 9 s;
  3-to-2 transition — mode transition is a first-order operating fact.
- [Confrontation §3.22, PENDING RATIFICATION] transitions mostly at startup/one contaminated
  test, but the pin "loses all hardware provenance": no published dataset certifies a
  persistent steady-state single mode.
- [Teasley 2025, T-4/T-5] wave mode = f(Pc, propellant) (H2 deflagrates >250 psia CTAP);
  mode boundaries INSIDE supp(mu) on throttle sweeps; flatness monitor must declare its
  measurable (stand force ≠ axial momentum flux).
- [Harroun 2020, H-U3] the SOTA validation CFD adopts exactly this single-mode scope
  SILENTLY; refuter strengthens: Harroun 2021 Eq.(7) two-wave inflow with NO periodicity
  certificate, Kaemming-Paxson 2018 and Paxson-Miki 2022 as further silent adopters — the
  de-facto-scope claim is 4x-supported.
- [VERIFICATION_FABLE:184–198 + Rubino 2018 F9/F10] inside the pin the wave-frame reduction
  is EXACT; outside, the named escalation is HB/ZP adjoint + mode-measure nu.
- [Mean-swirl panel S1] counter-wave admixture = THEOREM-level NON-channel for net swirl,
  but aperiodic storage during mode transitions violates H-AM1 — transitions break a
  load-bearing conservation identity.
- [Teasley 2023 F11i] no time-resolved measurement near the nozzle interface exists in the
  published corpus — the T0-flatness/harmonic-decay certificate is the ONLY admission monitor.

**Monitors/audits REQUIRED (the arming list):**
- M1: T0 thrust-trace flatness in wave frame + harmonic-decay audit, ARMED (mandatory per
  M0 VI.4bis(v); currently unarmed = breach), with the T-5 disambiguation clause.
  (Refuter SO-1) M1/M4 must run on the MULTI-PERIOD SOURCE TRACE, never on the extracted
  single-period family (flat by construction).
- M2: wave-count n + rotation-direction identification (azimuthal phase-slope/spectral fit).
- M3: Wave Number W provenance label per CycleFamily (label, never certificate).
- M4: in-window mode-transition/stationarity detector; startup excluded by construction.
- M5: angular-momentum balance-residual audit row (fires on H-AM1 aperiodic storage).
- M6: mu-support mode audit for imported operating measures (D2.3 raised to real audit).
- M7: branch/hysteresis bookkeeping — certified (n, direction) in dataset identity; no mode
  reproducibility assumed without re-certification.
- **M8 (refuter-imposed, SO-1): window-convergence/source-trace audit** per Schotthofer 2024
  (`reports/schotthofer_2024_windowing.md` H-U3, F-A1/A2/A3): 9% vector error, gradient sign
  flips from a 29%-of-period window shift, mode-competing regime where no window works,
  period-mean drift — extraction fragility of simulation-sourced families.

**Refuter-imposed amendments:** (SO-2) add Harroun 2021 F6 open/closed wake-mode transition
at NPR≈6.7 (crossed EVERY cycle in plug/E-D configs, invisible to M1–M7) to the
violating-regime census — pressures D2.3/per-state map; (SO-3) scope the "no dedicated
longitudinal-mode study" absence to RDE modes (Ornano 2017 is an in-corpus pulsed-detonation
axial-pulsation study); (SO-4) cite the pending advisory's R20 registry row (APERTO, owner
F5) and D-12 nu-gating as the named owner/decision lever.

**Residual risks:** monitor suite unarmed today (owner F2; verdict conditional on arming);
no steady-state hardware provenance anywhere (families simulation-sourced by necessity);
wave-count bistability/hysteresis has no quantified in-corpus anchor (Anand & Gutmark 2019
lives only in the Phase A tree — litmap procurement gap; M7 threshold underivable);
longitudinal/feed-coupled modes covered only by the HB/ZP escalation lever; throttled/
multi-point claims exceed a single family (mode-measure nu registered but unbuilt; cross-mode
aggregation = non-collapsing T-T3-MAP class); §3.22 downgrades ride the NON-RATIFIED
confrontation advisory — re-check at ratification.

---

### 3. [R1-CAUSAL] Causal separation / no upstream influence through Gamma_d (`confront_r1.md`)

**VERDICT: CONDIZIONATA** — the ONLY non-LDM verdict of the six. Legitimate solely on the
named validity window W1–W4, with audits A1–A6 armed; the unconditional reading is
contradicted by the corpus (refuter: verdict stands; evidence-wording corrections binding).

**Validity window (all four clauses required):** W1 every patch of the extraction surface
axially supersonic with measured margin (theorem-exact there via [T-NSW],
`00_APPARATUS_BRIEF.md` ll.129–131 — the only theorem-backed version of R1 in the
landscape); W2 design vector strictly downstream of the CERTIFIED interface (refuter: enforce
as geometry-invariance downstream of the certified interface; throat-area invariance is
necessary-NOT-sufficient — Liu 2022 B-vs-C defeats a fixed-A_t operational test, eta
8.9→13.2% at same eps=87.3%); W3 operating-point exogeneity (mode definite and stable on
supp(mu)); W4 axially-subsonic patches routed to the declared two-regime closure, never
silently extended.

**Strongest surviving literature evidence:**
- [Paxson-Miki 2022 §4] decoupling "ASSUMED, not demonstrated": BC-enforced + one-way
  architecture; axial Mach never shown (published 1.15–1.45 is total-velocity with
  "significant tangential components").
- [Miki 2020 T-3/F-3] verbatim p.4 choking "assumption"; interface in SUBSONIC flow with
  full-state Dirichlet that mechanically suppresses the very influence being assumed.
- [Kaemming-Paxson 2018, choking advisory §1(b)/C1] healthy-case throat AXIAL Mach
  0.86–1.33 (avg 0.99), M~0.5 at low PR: axially-subsonic patches on part of EVERY cycle —
  mu(Xi_sub)>0 is the generic case; the supersonic premise fails patch-wise generically.
- [Harroun 2021, choking advisory §1(d)/C4] throat restrictions can QUENCH detonation at
  rocket conditions (p.661 via ref [9]) — design-to-family back-channel removing the
  detonative branch entirely.
- [Teasley 2025 T-4] wave mode = f(chamber pressure, propellant); exit restriction sets
  chamber pressure, so nozzle design can move the wave mode — family-level, not perturbative.
- [Stechmann 2019, choking advisory §1(a)] exit-plane sonic condition a DECLARED ASSUMPTION
  (p.889 verbatim) — the 0-D ancestor also assumes, never proves.
- **Refuter-mandated CORRECTION of a false absolute:** "no two-way coupled run / no
  back-pressure sensitivity run exists in any read source; the experiment has never been
  run" is FALSE as written — Liu 2022 (`reports/liu_2022_aerospike_rde.md`, omitted by the
  assessment) is a fully coupled 3-D chamber+nozzle series varying nozzle geometry and
  measuring chamber response (eta = −7.4/+8.9/+13.2/+13.1% across configs A–D, Table 5;
  mdot Table 7); Ornano 2017 stage 3 is a second coupled counterexample (PDE class).
  RE-SCOPE to: no coupled/back-pressure run in the NASA decoupled-architecture line, and no
  controlled impedance-only perturbation with the interface family as measured object.
  The Liu data cuts FOR the verdict on both sides: measured back-channel outside the window
  (A-vs-B, B-vs-C) AND measured chamber-invariance under a purely-downstream change inside
  it (C-vs-D: eta 13.2→13.1%, mdot 6.01→6.00 — the corpus's only MEASURED instance of the
  R1-safe subspace).

**Monitors/audits REQUIRED:**
- A1 axial-margin monitor min_xi(M_axial−1) ≥ derived margin, per patch per phase,
  tangential separated (total Mach forbidden as evidence; C24 ban pending ratification);
  must consume the (Gamma,h0,s)-aware decomposition (mean-swirl P4) or it can falsely
  certify L4.
- A2 outgoing-characteristics certificate on the extraction surface at every phase, else
  LOUD REJECT (certified version of the Paxson-Miki BC, choking C3).
- A3 H-EXO falsifier armed: measured dGamma_d/dSigma and dmu/dSigma vs null band; MANDATORY
  at F5. (Refuter) Liu 2022 supplies a coarse published order-of-magnitude anchor for the
  null band (~4.3 points eta under fixed-constriction contour change; ≤0.1 point under
  purely-downstream truncation; ~1% mdot spread) — viscous/reacting non-containment caveats
  declared; "no external anchor" was overclaimed.
- A4 restriction/quench data-validity flag (Harroun p.661; choking C4).
- A5 mode-definiteness + family-provenance (W label PRACTICE-grade + T0-flatness + D2.3);
  interface family RE-GENERATED, never reused, if design can move chamber pressure across a
  mode boundary.
- A6 two-regime routing: measure mu(Xi_sub) per dataset; if >0 engage the declared O1/O2/O3
  closure — J undefined otherwise.

**Residual risks:** empirical vacuum on the margin (no read source publishes a measured
axial/choking margin at the interface; the L4 window may be empty on part of every cycle for
real hardware — the two-regime closure is then the operative path); quench threshold
unmapped (A4 flags, does not predict); sharpest formulations (H-EXO/D-02, C24, R25) ride the
NON-RATIFIED confrontation advisory — consume duty wording post-ratification; F5 phase
change: at coupled RDE the measure becomes design-coupled, R1's protected content shrinks to
W1–W2 and the verdict does NOT carry over — re-audit at F5 entry.

---

### 4. [GAS-FROZEN] Frozen thermally-perfect mixture pin (`confront_gas.md`)

**VERDICT: LEGITTIMA-DICHIARATA-MONITORATA** (refuter: stands, 3 surviving objections
including one evidence mis-binning that must be corrected wherever quoted).

**Strongest surviving literature evidence:**
- [Paxson-Miki 2022] SOTA nozzle side IS exactly the pin (frozen thermally-perfect CEA
  mixture). **Refuter correction (MIS-BINNING, binding):** the −15.6% mdot / −10.5% ideal
  thrust remap is CPG(gamma=1.182, R_g=60.12) → frozen TPG CEA mixture (R_g=71.05) — BOTH
  endpoints frozen-composition. It is quotable only as thermo-closure/interface-bookkeeping
  dominance, NEVER as "a live instance of the [T-EQBR] frozen/equilibrium bracket"
  (category slip in report F8 l.296–297, inherited by the assessment).
- [Harroun 2021] frozen 2-species thermally-perfect model with quantified species-truncation
  cost: 9→2 species = 0.28–0.58% normalized thrust error (Table 2 p.667); "reactions minimal
  in nozzle" is judgement, not measurement.
- [Sun 2019] Fig.5: kinetics gamma strictly INTERIOR to [frozen 1.385, equilibrium 1.26] at
  AR~200 — published corroboration of the [T-EQBR] bracket ordering; Sun NOT citable as a P1
  instance (varying composition with constant R, T5/C13).
- [Wintenberger-Shepherd 2004] dissociation/recombination "significantly influence" results
  (p.13, first-order); fuel-air beats fuel-oxygen near stoichiometry (Fig.19) — frozen error
  largest for hot fuel-oxygen products; magnitude evidence is 0-D cycle, not nozzle flow.
- [Janc 2025 T-4] even the SOTA differentiable finite-rate solver falls back to frozen
  gamma=1.29 one-step chemistry when optimizing — field practice corroborates the pin.
- [Internal, M0 ll.970–980 + ledger C-IGMIX] executable bracket [T-EQBR]: equilibrium
  ceiling +6.34..+6.97% above frozen on every PR, bars ≤0.003 s, THEOREM* within C-IGMIX,
  falsifier = finite-rate leaving the bracket. First-orderness survives on this internal
  instance + Wintenberger even after the mis-binning strike.

**Monitors/audits REQUIRED:**
1. [T-EQBR] bracket re-executed per propellant/PR instance; frozen number quotable only as
   the [frozen, equilibrium] pair with bars.
2. [C-IGMIX] falsifier (finite-rate leaving the bracket); Sun-2019-T4 kinetics-informed
   c_p(T) freeze as registered bracket-narrowing practice.
3. H-R1 total-enthalpy-flux rejector across Gamma_d (afterburning channel), guarding the
   PLACEMENT clause. (Refuter SO-2) feed it the corpus-side magnitude hooks the assessment
   ignored: Teasley 2023 "90+%" combustion completeness (with the unnamed-CEA caveat) and
   Kaemming-Paxson's calibrated ~6% deflagrative throughflow.
4. Species-reduction functional-error rung (pre-registered thrust-error acceptance) in
   Cantera table generation (Harroun 2021 F11 pattern).
5. gamma(T) status line per theory piece; gamma=const only as declared oracle.
6. Citation discipline: Sun 2019 never as P1 instance; frozen and equilibrium numbers never
   quoted as the same object; (refuter) the Paxson-Miki remap never quoted as a bracket
   instance (SO-1); Liu 2022 added to the SOTA census (SO-3: only in-corpus
   finite-rate-through-nozzle RDE evaluation, 21-species/37-reaction — verdict-preserving
   because its design layer is frozen gamma=1.26 by fiat and no frozen-vs-finite-rate delta
   is published; Liu F10's gamma-inconsistency reinforces monitors 5–6).

**Residual risks:** bracket magnitude rests on ONE internal executable instance; hot
stoichiometric fuel-oxygen products = largest frozen error exactly where RDRE hardware runs
(+6.3..+7.0% may be optimistic there until re-executed); condensables/soot corpus-silent
(P2 declared exclusion, not priced); no published finite-rate vs frozen nozzle-flow delta
for an actual RDE nozzle; confrontation confirmations (3bis-J, 3.21, C13) pending
ratification.

---

### 5. [EULER-GSEP] Euler core + declared viscous layer + attached-flow constraint (`confront_euler.md`)

**VERDICT: LEGITTIMA-DICHIARATA-MONITORATA** (both Q1 model-form and Q2 constraint-form;
refuter: stands, 4 completeness objections).

**Strongest surviving literature evidence:**
- [Kraiko 2001, `reports/kraiko_2001_plug.md`] direct precedent: Euler design + empirical
  separation criterion Eq.(4); the school's own claim that RANS closures are "not more
  reliable" for shock/turbulent-BL separation; ships the separation-point insensitivity
  instrument.
- [Harroun 2021 F2] g_sep is history-dependent (Eq.9 residence time; Fig.20 in-cycle
  migrating separation point), BUT sign favorable: cycle forcing DELAYS separation — the
  pointwise quasi-steady g_sep is conservative on the computed instance.
- [Harroun 2020 F6] the purpose-built experiment closes NEITHER g_sep nor p_b: any g_sep is
  a modeling choice with falsifier, not a validated closure. [F2/F7] no base-pressure model
  exists and Pb/Pa=1 is sign-wrong for RDE → the attached-flow CONSTRAINT is the only
  certifiable form.
- [Miki 2020] the viscous RANS alternative carries 12–17% validation error on separating
  flow vs 3.2% design deltas — not a certified route either.
- [Teasley 2023] off-design separation across throttle empirically priced; T-T3 caps to the
  attached segment (scope cap must be printed).
- [ADVISORY_rde_choking §4-bis] internal adjudication of record matches literature: HONEST
  GAP declared; delay benefit "never claimable from the inviscid tool".
- [Fernandes 2023 / Ornano 2017] separation-blind optimizers drift to the separated/box
  boundary — g_sep is load-bearing for the optimizer, not decoration.

**Monitors/audits REQUIRED:**
- M1 Strouhal/residence-time admission audit (t_res vs 1/f); failing regimes out of (P)
  scope or g_sep reparameterized by (f, t_res). (Refuter) wire the A32 f_cycle data-contract
  hook.
- M2 pre-registered separation-point insensitivity instrument (Kraiko-2001-style, queued
  A-1); certified thrust only where the insensitivity verdict holds.
- M3 per-phase H2' monitor (supersonic-exit/full-flowing/g_sep-margin every phase); failures
  route to the two-regime contract.
- M4 g_sep shipped with named falsifier + calibration debt printed + conservative-direction
  evidence grade. (Refuter SO-4) split the grade: ejector-suction SIGN experimentally
  corroborated cross-campaign/cross-fuel; the 8x MAGNITUDE from the least grid-converged
  configuration and externally contested (Schwer, per pending-ratification C28/C29).
- M5 T3-CONTROL claim fence: no ranking claims over separated/base-coupled/cowl-coupled
  configurations; Harroun counter-example named externally.
- M6 viscous model layer as declared bands, never inside the certificate. (Refuter SO-1)
  attach the two in-corpus calibration anchors — Paxson-Miki 2022 F9 (base drag −9.5% of
  nozzle thrust, truncated plug under genuine RDE cycle flow) and Liu 2022 F12
  (P_b/P_a≈0.44, 0.65% of thrust) — with the three-geometric-class separation discipline
  (pending-ratification C28). (Refuter SO-3) add the skin-friction/wall-shear debit, an
  attached-flow viscous term LARGER than the 3.2% design deltas (Sun 2019 Table 5:
  D_w≈37 N ≈5% of F_v; Miki 2020 Hyp.16 pressure-only accounting named defect).

**Residual risks:** g_sep conservatism proved on ONE computed instance (a regime where
forcing PROMOTES separation would flip the safe direction); sea-level record hardware sits
outside H2' (attached-feasible set may be small/empty there); inviscid-only-ours ranking
incomparability vs viscous evaluators where separation discriminates (R22 unexecuted);
calibration base could shift — Harroun 2019 MS thesis UNREAD (procurement P0), Mueller NASA
reports unprocured, and (refuter SO-2) Ostlund & Muhammad-Klingmann 2005 (the standard
separation review, named in-repo in Sun 2019 refs) is an unprocured calibration carrier for
the criterion CLASS — "no dataset to calibrate against" is true only for the RDE line;
confrontation advisory pending ratification.

---

### 6. [CONTRACT-MU] Interface-contract bundle E1–E5 (`confront_contract.md`)

**VERDICT (bundle): LEGITTIMA-DICHIARATA-MONITORATA**, with element grades E1 LDM, E2 LDM,
**E3 CONDIZIONATA** (L4 window = audit-passed instances only; the subsonic branch is
load-bearing generically), E4 LDM, E5 LEGITTIMA-ESATTA within scope (ambient datum) with
MANDATORY scope boundary. Refuter: stands (the aggregation attack — bundle should be
CONDIZIONATA — FAILS because the conditionality is disclosed and the two-regime posture is
exactly what the ratified choking advisory C1 mandates); 5 surviving objections.

**Strongest surviving literature evidence:**
- Heat-release end never measured in corpus: "reactions minimal" asserted [Harroun 2021
  p.666]; frozen-downstream by fiat [Paxson-Miki p.5]; ~6% of throughflow reacts
  deflagratively in the field's own reference cycle model [Kaemming-Paxson pp.4–5] — "ALL
  heat release" is a convention, not a verified station.
- L4 generically fails on record data: throat AXIAL Mach 0.86–1.33 avg 0.99, M_8x~0.5 at
  low PR — mu(Xi_sub)>0 page-verified [K-P Table 1 p.6 + §VI.H p.14].
- Published NASA exit Mach 1.15–1.45 is TOTAL-velocity; axial never reported;
  choking/decoupling BC-imposed [Paxson-Miki §4+F4; choking advisory C1–C3].
- mu pushforward formalizes what the field asserts without proof ("area avg = time avg in
  wave frame", K-P p.5) and leaves undeclared (Harroun's averaging weight).
- Second published cycle measure is exponential-in-pressure [Harroun 2020 Eq.(2)] —
  MODEL-DERIVED label mandatory; mode transitions occur INSIDE mu support on throttle
  sweeps [Teasley 2025 T-4].
- Stationarity certifiable but windowed: CFD limit-cycle triple [Paxson-Miki F12]; hardware
  CTAP windowed, one chain never settled in 0.9 s [Harroun 2021].
- Pa constant matches every record test environment exactly BUT couples at first order via
  the base: matched-mdot twin errs 50–100% of measured base pressure; open-wake Pb<Pa in
  SIGN vs classical closure [Harroun 2020 F1/F7]; base term has no accepted predictive
  closure (12% gross thrust K-P; −9.5% nozzle thrust Paxson-Miki).

**Monitors/audits REQUIRED (consolidated, with refuter completions):**
1. Gamma_d placement audit: cycle-resolved enthalpy-flux settling, threshold DERIVED from
   the (v) budget via Rayleigh sensitivity + always-on downstream heat-release residual
   (C014/H-R1).
2. Stage-A axial-Mach margin audit min_{xi,patch}(M_axial−1), swirl separated; total Mach
   never accepted; L4 proven per instance, never presumed.
3. Causal-separation certificate: all normal characteristics outgoing at every phase, else
   loud reject. (Refuter SO1) carry H-EXO BY NAME with its falsifier dmu/dSigma≠0: E2's
   exogeneity premise is guaranteed only on the L4 class [Schotthofer F-T2; confrontation
   D-02, pending ratification] — outside the audit-passed window E2 rides the same window
   E3 is conditioned on.
4. H-DATA single-mode monitor with mode-transition exclusion declared in mu provenance.
   (Refuter SO2) frame-specification MANDATORY: stated in the WAVE frame — as written it
   falsely fires on Miki 2020's healthy lab-frame traces (T0 1400→2200 K over one
   revolution).
5. Limit-cycle stationarity triple (mass-flow limit cycle; cycle-averaged thrust constant;
   cycle-integrated in/out mass balance).
6. Measure-invariance falsifier vs Harroun's exponential-in-P measure (MODEL-DERIVED label);
   averaging/matching convention declared in the same sentence as any J value.
   (Refuter SO3) extend the library: Miki 2020 empirical non-atomic pushforward from a
   fixed-Pt airbreathing rig (third structural measure class) and Liu 2022 Eq.14
   state-averaged stagnation reconstruction (third undeclared convention) join the
   falsifier/declared-convention sets.
7. Swirl channel in the s(xi) contract (Gamma=r·u_theta transport + swirl-uniformity
   monitor); f_cycle as required data-contract field.
8. H2'/base-region scope fence: constant-Pa never applied to wake/base surfaces; wake-mode
   transition (NPR≈6.7 class) treated as switch/mode phase. (Refuter SO4) bind the
   T3-CONTROL citation obligation for Harroun 2020 F3/F10 ("axisymmetric cycle-averaging is
   too simplistic", computed 1%-Isp ranking contradicted by measured wall pressures — the
   field's only direct published indictment of cycle-averaged evaluation) into the
   consolidated monitor list.
9. (Refuter SO5) (a) declared window + declared k + period-shift rejector on any mu/cycle
   family extracted from an unsteady simulation [Schotthofer F-A2: 29%-of-period shift ⇒
   9.1% sensitivity error with sign flips]; (b) per-phase Delta-s_min/Delta-s_irr
   entropy-budget audit on imported interface data, PRACTICE grade [Wintenberger-Shepherd F6].

**Residual risks:** in-nozzle heat release unmeasured either way (falsifier: if settling
never occurs inside E, model class rejected → late re-scope to reacting layer); L4 window
may be empty on real engines (declared-closure branch load-bearing generically);
design→data back-reaction only ever BC-imposed in SOTA; hardware stationarity windowed
sub-second; Pa≠0 first-order base coupling with no predictive closure (bracketed, never
predicted, for any based configuration); confrontation advisory pending ratification.

---

## CROSS-CUTTING OBSERVATIONS

1. **One shared empirical vacuum drives most conditionality:** no read source publishes a
   measured axial Mach margin, a time-mean tangential field, a time-resolved
   nozzle-interface measurement, or a coupled back-pressure sensitivity run in the NASA
   decoupled line. The program's stage-A audits are non-redundant work the SOTA never did.
2. **Shared monitor spine:** the wave-frame T0-flatness certificate (+ harmonic audit +
   TRIPLE monitor), the axial-Mach margin audit with swirl separated, and the
   two-regime/H-EXO routing recur across four of six hypotheses — arming them once
   discharges monitor debt across the whole bundle. Owner of the arming: F2.
3. **Pending-ratification dependency is systemic:** every assessment and refuter correctly
   quarantined `ADVISORY_litreview_confrontation_2026-08-13.md` as CAVA NON RATIFICATA.
   Several duty wordings (H-EXO/D-02, C24/D-36 citation bans, C28/C29, R20, R25, §3.22)
   must be consumed at ratification, not re-derived.
4. **Liu 2022 is the recurring blind spot of the assessor layer** (missed in axisym census,
   R1 coupled-run sweep, GAS-FROZEN SOTA census, EULER-GSEP base anchors, CONTRACT-MU
   convention library) — every miss was verdict-preserving or verdict-strengthening, but
   the citation corrections above are binding.
5. **R22 (3-D unsteady vs 3-D per-phase averaged vs 2-D per-phase averaged) is the single
   named decider** for the two heaviest residual threats (Harroun c_F=1.25
   discrimination-blindness; inviscid-only-ours ranking incomparability). It is unexecuted.

## FINAL TABLE

| Hypothesis | Verdict | Refuter outcome | Grade-limiting fact |
|---|---|---|---|
| [I-GEO+I-STATE] axisymmetry | LEGITTIMA-DICHIARATA-MONITORATA | stands (5 completeness duties) | O(1) residual sources measured; propagation lemma unwritten (duty R4); R22 unexecuted |
| [H-DATA] single-mode family | LEGITTIMA-DICHIARATA-MONITORATA, conditional on ARMING | stands (4 SO; +M8 Schotthofer) | monitor suite unarmed = live breach of M0 VI.4bis(v); no steady-state hardware provenance |
| [R1-CAUSAL] causal separation | **CONDIZIONATA** (window W1–W4) | stands (false-absolute correction: Liu 2022) | mu(Xi_sub)>0 generic; quench back-channel; mode=f(Pc); theorem-exact only on L4 |
| [GAS-FROZEN] frozen TPG pin | LEGITTIMA-DICHIARATA-MONITORATA | stands (mis-binning correction binding) | bracket = ONE internal instance; P-M remap not a bracket instance |
| [EULER-GSEP] Euler + g_sep | LEGITTIMA-DICHIARATA-MONITORATA | stands (4 SO: anchors, friction debit, Ostlund, grade split) | g_sep uncalibrated (modeling choice with falsifier); H2' scope cap at sea level |
| [CONTRACT-MU] E1–E5 bundle | LEGITTIMA-DICHIARATA-MONITORATA (E3 CONDIZIONATA inside) | stands (5 SO: H-EXO by name, wave-frame spec, measure library, F3/F10, Schotthofer rejector) | L4 possibly empty on real engines; base coupling closure-less |

**Overturned verdicts: none.**
**Verification layer: UNPROVEN this run (knowntrue_survived=false) — all verdicts above are
assessor-verdicts-unrefuted, NOT certified survivals, until the dual-seed re-run passes.**
**NULL slots: 0.**

---

## ADDENDUM — DUAL-SEED RE-RUN OF RECORD (2026-08-17, same window)

Per the "Required action" above, the dual-seed was RE-RUN on a
dedicated batch with a corrected known-true seed (the original
SEED-B improperly fused the exact conditional identity with the
[S-T0P] propagation leg — an over-label planted by the seed
designer, correctly caught; adjudication: seed-design defect, not
refuter defect).

- SEED-C (fresh canary: "interface data independent of nozzle
  geometry in ALL regimes, THEOREM, no monitor"): **FIRED** —
  REFUTED-AS-GRADED with 5 repo-anchored objections
  (refute_SEED-C.md).
- SEED-B2 (corrected known-true: conditional frame-invariance
  identity, steadiness as HYPOTHESIS): **SURVIVED** —
  SOUND-AS-LABELED; objections amendment-class only (n_theta!=0
  surface perimeter -> restrict to surfaces of revolution or use the
  storage-flux cancellation identity; regularity perimeter;
  convention pin; plus an identified UNDER-claim: instantaneous
  constancy on surfaces of revolution is provable and STRONGER —
  independently re-deriving the record's own T0 constancy clause)
  (refute_SEED-B2.md).

**VERIFICATION LAYER: PROVEN in both directions
(canary_fired=true, knowntrue_survived=true).**
The six per-hypothesis verdicts above are hereby upgraded from
"assessor-verdicts-unrefuted" to CERTIFIED SURVIVALS of a proven
verification layer. The binding refuter amendments (citation
corrections, monitor additions M8, Liu-2022 census insertions)
remain binding as stated.
