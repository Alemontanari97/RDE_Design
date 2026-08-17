# HYPOTHESIS AUDIT — [H-DATA] pure periodic single-mode rotating-wave data family

**Session:** S-FOUNDATIONS (R35), Phase C hypothesis-legitimacy audit.
**Auditor:** subagent, 2026-08-17. **Sources: in-repo only** (25-paper corpus in
`literature_review/` + reports, validation advisories, M0, PROGRESS). No web.

**Hypothesis as posed** (frozen problem statement, cf. `phaseA_problem_brief.md:31`):
interface data are a pure periodic single-mode rotating wave — fixed wave count n, no
mode transitions inside the family; monitor = flatness in the wave frame, **currently
unarmed**.

**Verdict: LEGITTIMA-DICHIARATA-MONITORATA** — conditional on the monitor suite being
ARMED. The "currently unarmed" state is itself a breach of the repo's own mandatory
data-contract clause (M0 VI.4bis(v): "The flatness monitor itself is mandatory in every
data contract", `docs/rde_nozzle_MASTER.md:1441`), so the verdict is legitimacy *as
declared and monitored*, not legitimacy of the present unmonitored state.

---

## 1. What the literature record says, adversarially read

### 1.1 The regime exists — the hypothesis is not vacuous

- **[Wolanski 2013, `reports/wolanski_2013_survey.md` F4 (lines 136–146)]**: p.141–142
  compensation photographs — "the structure of the rotating detonation is very regular
  and stable"; Fig. 38 (p.144) is a stable single-head trace. Direct experimental
  support that stable single-mode operating windows are a **real** regime, for the
  mixture parameters tested.
- **[Harroun 2020, `reports/harroun_2020_validation.md` H-U3 (line 95)]**: the field's
  own validation CFD imposes exactly our hypothesis — Eq. (2) is Eq. (1) with
  t → θ/(180 f), "a pure single-mode rotating wave in the wave frame. This is our own
  periodic-wave data scope, adopted **silently**." The SOTA practice already lives
  inside H-DATA; the delta we add is that we *declare and monitor* what they assume by
  fiat.
- **[VERIFICATION_FABLE 2026-08-13, `reports/VERIFICATION_FABLE_2026-08-13.md:184–198`]**:
  within the pin, the per-phase steady adjoint "IS the correct symmetry-reduced object";
  the naive time-domain periodic adjoint would be ill-posed without the same quotient
  (trivial Floquet multiplier 1 along the group orbit; Zahr–Persson App. A assumes
  (I − monodromy) non-singular, verified at source p.28–29). So H-DATA is not merely
  convenient: it is the hypothesis under which the entire wave-frame reduction is
  *exact* (T-T0), and the reduction is strictly stronger than harmonic balance for this
  class ([Rubino 2018, `reports/rubino_2018_hb_adjoint.md` F10]).

### 1.2 The regime is violated on real hardware — frequently, and by every named mechanism

- **Mode transitions + mode zoo.** [Teasley 2023, `reports/teasley_2023_nasa_state.md`
  F3 (lines 91–93)]: p.19 "Several different wave modes were observed at startup ranging
  from 2-4 wave counter propagating modes, one through five wave co-rotating modes, and
  two wave slapping modes"; p.22 CW↔CCW transition ">12 times in 9 s" (one test); p.22
  test 028: 3-wave → 2-wave transition with velocity 4230 → 3520 ft/s. The report's own
  conclusion: mode transition is "a first-order operating fact", which "caps the
  physical reach of any single-mode cycle family".
- **Refinement (PENDING RATIFICATION — cite as pending, never as decided).**
  [`validation/ADVISORY_litreview_confrontation_2026-08-13.md` §3.22 (lines 650–661),
  CAVA NON RATIFICATA]: the O(1 Hz) transition rate comes from ONE water-contaminated
  test, and the observations are almost all at STARTUP, not thermal steady state — so
  the robust layer is NOT promoted from "idle" to "load-bearing" by this datum. But the
  same section lands the sharper blow: **"il pin 'onda periodica pura a modo singolo'
  perde ogni provenienza hardware — nessun dato pubblicato certifica un modo singolo
  persistente in stato stazionario."** H-DATA has no published hardware instance
  certified at steady state; it survives as a per-dataset-certified scope, not as a
  physical fact about RDREs.
- **Mode identity is an operating-point function; transitions sit INSIDE μ-support on
  throttle sweeps.** [Teasley 2025, `reports/teasley_2025_rdre_dev.md` T-4 (lines
  111–123)]: p.9 hydrogen "yields a vastly different number of wave at low pressure, and
  pure deflagration at higher pressures exceeding 250 psia CTAP"; p.7 "future designs
  must implement strategies by which multi-mode operation is achieved even at throttled
  conditions." Consequence of record: on a blowdown/throttle μ, wave-count changes occur
  inside supp(μ), not on a μ-null set — the D2.3 "switch phases are μ-null" clause is
  raised "from formality to a real audit" for imported measures. (This pressures the
  adjacent D2.3 measure hypothesis more than H-DATA itself, which is per-family; but it
  bounds any multi-point design claim built on a single family.)
- **Galloping / degeneration + the field's own regime criterion.** [Wolanski 2013, F4 +
  F8 (lines 140–146, 180–192)]: p.143–145 "galloping rotational detonation" with
  velocity fluctuating about C–J, degeneration to deflagration at reduced parameters,
  organized by the **Wave Number** W = t_r/t_mf (Eq. (4), reduced Eq. (5)
  W = 2 V_max/(l_cr h u_D), p.144). W ≈ integer ⇒ n-head periodic hypothesis physically
  plausible; W ≪ 1 ⇒ galloping/decaying, outside the averaged model. Adopted of record
  as a *provenance label*, explicitly NOT a certificate (undefined V_cr, no derivation).
- **Longitudinal / feed-coupled pulsation.** [Rubino 2018, F10 (lines 299–312)]: named
  as one of the cases "T-T0 does not cover" — incommensurate multi-mode operation,
  "longitudinal/feed-coupled pulsation, or genuinely non-wave-frame-reducible
  unsteadiness" — with the escalation route named (HB adjoint / ZP
  periodicity-constrained adjoint; + LSS/NILSS for chaotic, registered at
  VERIFICATION_FABLE A10, line 198). The corpus contains no dedicated longitudinal-mode
  (LP) study; the coverage of this failure mode in-repo is via the named escalation
  lever, not via data.
- **Counter-rotating waves.** Observed on hardware ([Teasley 2023 p.14, p.19]); handled
  in-repo as declared out-of-scope (generality ledger C004,
  `validation/ADVISORY_Sgauntlet_generality_ledger_2026-08-11.md:135`). Important
  THEOREM-level negative from the mean-swirl panel
  (`validation/ADVISORY_mean_swirl_panel_2026-08-11.md:19`, S1 line 24): unequal wave
  counts and **counter-wave admixture are NON-channels for net axial angular momentum**
  — so counter-rotating contamination does not corrupt the swirl-flux balance, but
  **aperiodic storage during mode transitions IS an H-AM1 violation** (channel (4) of
  the torque census) and invalidates the T0-periodicity hypothesis of the flux-nullity
  theorem. Mode transitions therefore break not only the averaging but a load-bearing
  conservation identity used elsewhere in the theory.
- **Bistability / hysteresis — honest evidentiary status.** The 25-paper corpus contains
  **no dedicated wave-count bistability/hysteresis study**: grep over
  `literature_review/**` finds hysteresis only in [Harroun 2020 H-U8, line 100] (base
  pressure "treated as a scalar operating-point function ... no hysteresis / history
  dependence is entertained" — i.e. the corpus is *silent*, not negative) and in an
  unrelated line-search context ([Janc 2025:299]). The Anand & Gutmark 2019 citation for
  wave-count bistability appears only in this session's Phase A derivation trees
  (`phaseA_tree_propulsion.md:228`), which are NOT part of the in-repo read corpus — it
  must not be cited as corpus evidence. Indirect in-corpus evidence exists (Teasley 2023
  p.22: sustained CW↔CCW alternation and chaotic modal transitions imply multistability
  of the mode attractor), but a quantified mode-locking-window / hysteresis map is a
  **named absence** in the corpus.

### 1.3 Two facts that discipline the monitor design itself

- **No time-resolved measurement exists near the nozzle interface in the published
  hardware corpus.** [Teasley 2023, F11(i) (line 122)]: high-speed transducers sit on
  manifolds behind 3-ft sense lines; nothing at the nozzle entrance. Therefore
  experimentally-sourced CycleFamilies are unobtainable; imported families are
  simulation-sourced by necessity, and "the T0-flatness / harmonic-decay certificate
  remains the **only available admission monitor**." The monitor is not decoration — it
  is the sole gate between H-DATA and its data.
- **The flatness monitor must declare its measurable.** [Teasley 2025, T-5 (lines
  125–135)]: Fig. 7 single-wave thrust trace scatters ±1500 lbf about ~4500 lbf — stand
  force is the structural response to a rotating transverse unbalance at 8.25 kHz, NOT
  the axial momentum flux T-T0 constrains. T-T0 and its monitor "must ship with a named
  disambiguation clause ('measured stand force ≠ ∮ axial momentum flux')". An armed
  monitor lacking this clause would be *falsified by hardware data that are actually
  consistent with the theorem*.
- Also noted: [Teasley 2023, F6 (line 102)] — the practitioners' claim "control over
  wave mode operation may not be necessary or useful from a design standpoint" (p.21) is
  an ~8-point assertion, must NOT be read as licence to ignore mode identity.

---

## 2. Adjudication

The literature supports every clause of H-DATA **as a declared, monitored, per-dataset
hypothesis** and refutes it **as an unmonitored physical assumption about RDRE
hardware**:

1. Stable single-mode windows exist (Wolanski) and the entire SOTA nozzle-CFD line
   already computes inside them, silently (Harroun H-U3). H-DATA is the field's de facto
   modeling scope, made explicit.
2. Within the pin, the hypothesis buys an *exact* symmetry reduction (T-T0,
   VERIFICATION_FABLE), not an approximation — the strongest possible justification for
   pinning it.
3. The violating regimes (mode transitions, counter-rotation, slapping, galloping,
   deflagrative degeneration, feed-coupled pulsation) are documented, first-order, and
   frequent at startup/throttle boundaries (Teasley 2023/2025, Wolanski) — so the
   hypothesis is only defensible with an armed rejector and a named validity window.
4. No published dataset certifies a persistent steady-state single mode
   (litreview-confrontation §3.22, pending ratification) — so H-DATA can never be
   *asserted* for a dataset; it can only be *certified* per dataset by the monitor.
5. The architecture already anticipates all of this (M0 VI.4bis: algorithm fully
   general, periodic structure exploited only when certified; robust CVaR/DRO layer
   "idle — not absent"; mode-measure ν registered-not-adopted with cross-mode
   aggregation routed to the T-T3-MAP non-collapsing class). Nothing in the literature
   forces a re-scope of the *problem statement*; it forces the monitor suite from
   "declared" to "armed".

**DA-RISCOPARE rejected** because the hypothesis governs the admitted *data family*,
not the hardware, and the machinery stays fully general (VI.4bis amendment of
2026-07-16). **CONDIZIONATA alone rejected** because a validity window cannot be named
a priori in operating-parameter space (mode identity is propellant- and Pc-dependent and
possibly history-dependent — Teasley 2025 p.9; corpus silent on hysteresis maps): the
window is *defined by the monitor verdict per dataset*, which is exactly the
DECLARED+MONITORED form. **LEGITTIMA-ESATTA rejected** because the monitor is unarmed
and the pin has no steady-state hardware provenance.

### Validity window (as the literature permits naming it)

Per-dataset certified windows with ALL of: (i) steady thermal state — startup
transients excluded (Teasley 2023 mode zoo is a startup phenomenon per §3.22, pending
ratification); (ii) monitor-certified mode purity at fixed (n, direction); (iii)
W ≈ integer (not galloping/decaying, Wolanski Eq. 4–5); (iv) no mode transition inside
the certified window; (v) for imported operating measures μ, no mode boundary inside
supp(μ) (D2.3 audit, Teasley 2025 T-4). Outside the window the named escalation is:
mode-measure ν over the mode set with T-T3 applied mode-by-mode (registered, not
adopted; cross-mode aggregation = T-T3-MAP a_eff mixture class), robust CVaR/DRO layer,
and HB/ZP periodic adjoint for non-wave-frame-reducible unsteadiness (Rubino F9/F10,
VERIFICATION_FABLE stage-3).

---

## 3. Monitor requirements the literature imposes (the arming list)

M1. **T0 thrust-trace flatness in the wave frame + harmonic-decay audit** — the
    executable mode-purity falsifier (M0 VI.4bis(i)/(v), `00_APPARATUS_BRIEF.md:345`).
    MANDATORY in every data contract; currently unarmed ⇒ arm before any H-DATA-scoped
    production claim. With the **T-5 disambiguation clause**: the monitored measurable
    is ∮ axial momentum flux through axisymmetric surfaces, never stand force
    [Teasley 2025 T-5].
M2. **Wave-count + direction identification** (azimuthal phase-slope / spectral fit):
    flatness alone cannot distinguish n=2 from n=3 pure modes, and cannot see a
    co-rotating vs counter-rotating pair of the documented zoo [Teasley 2023 p.19].
    The family fixes n; the monitor must therefore *measure* n and direction, not
    assume them.
M3. **Wave Number W provenance label** (W = t_r/t_mf, reduced form
    2 V_max/(l_cr h u_D)) on every imported/generated CycleFamily — W ≈ integer
    plausible, W ≪ 1 ⇒ route to robust layer. Label, NOT certificate
    [Wolanski 2013 F8, adopted of record].
M4. **In-window transition detector / stationarity check**: zero mode transitions
    inside the certified window; startup segment excluded by construction
    [Teasley 2023 F3; §3.22 pending-ratification refinement].
M5. **Angular-momentum balance-residual audit row** (mean-swirl panel P5): |measured
    Γ-flux − declared J_inj − declared torque budget| ≤ derived tolerance — an H-AM1
    (T0-periodicity) violation via aperiodic storage during mode transitions fires
    here; counter-wave admixture provably does NOT, so this row complements rather
    than duplicates M2 [`ADVISORY_mean_swirl_panel_2026-08-11.md` S1 + torque census
    channel (4); `ADVISORY_rde_choking_2026-08-11.md:198`].
M6. **μ-support mode audit for imported operating measures** (D2.3): certify no mode
    boundary inside supp(μ) — raised "from formality to a real audit" by
    [Teasley 2025 T-4].
M7. **Branch/hysteresis bookkeeping**: record the certified (n, direction) as part of
    the dataset identity; corpus entertains no hysteresis (Harroun H-U8 — a silence,
    not a clearance), and wave-count bistability has NO in-corpus quantified anchor —
    so identical operating points must not be assumed to reproduce the same mode
    without re-certification.

---

## 4. Residual risks (named, with owners where the record assigns them)

R1. Monitor suite unarmed today: the frozen statement currently violates M0
    VI.4bis(v)'s own mandatory clause. Verdict is conditional on arming (owner: F2
    data-contract implementation).
R2. No steady-state hardware provenance for a persistent single mode anywhere in the
    published corpus (litreview-confrontation §3.22 — **pending ratification**);
    simulation-sourced families only (Teasley 2023 F11i). Any hardware-facing claim
    inherits this cap.
R3. Bistability/hysteresis of wave count: in-corpus evidence is indirect only
    (Teasley 2023 CW↔CCW alternation); the Anand & Gutmark 2019 anchor lives only in
    the Phase A tree, outside the read corpus — a litmap procurement gap if M7 is ever
    to carry a quantitative threshold.
R4. Longitudinal/pulsed (LP) modes: no dedicated in-corpus study; coverage is by the
    named escalation lever (HB/ZP) only.
R5. Multi-point/throttled design claims: Teasley 2025 p.7 makes multi-mode operation a
    design requirement across throttle — a single-family H-DATA answer does not span
    such a mission profile; the mode-measure ν extension is registered but unbuilt,
    and its cross-mode aggregation is a genuinely new averaged problem (T-T3-MAP
    non-collapsing class).
R6. §3.22's downgrades and the ν-registration ride the NON-RATIFIED confrontation
    advisory: if ratification amends it, M4's startup-exclusion rationale and the
    "robust layer not promoted" reading must be re-checked.
