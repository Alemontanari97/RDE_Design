# REFUTATION ATTEMPT — [GAS-FROZEN] verdict LEGITTIMA-DICHIARATA-MONITORATA

Role: adversarial refuter (S-FOUNDATIONS hypaudit, executed 2026-08-17).
Target: `validation/sfoundations_raws_2026-08-13/hypaudit/confront_gas.md` (READ IN FULL).
Corpus: IN-REPO ONLY — all 30 report files in `literature_review/reports/` enumerated and
keyword-swept (frozen/equilibrium/finite-rate/dissociat/recombin/afterburn/species/chemistry/
deflagrat/unburned), plus `validation/ADVISORY_litreview_confrontation_2026-08-13.md`
(PENDING-RATIFICATION, cited as evidence only), `ADVISORY_litmap_extension_2026-08-13.md`
(zero gas-closure hits — measured), `ADVISORY_rde_choking_2026-08-11.md`,
`ADVISORY_mean_swirl_panel_2026-08-11.md`, `ASSESSMENT_methodology_position_2026-08-13.md`
(zero frozen/equilibrium/IGMIX/EQBR hits — measured), M0 `docs/rde_nozzle_MASTER.md`
(T-EQBR block ~ll.970-980 re-read), `docs/rde_nozzle_hypothesis_ledger.md` (H-R1 l.56,
C-IGMIX l.66 re-read), `literature_review/reports/VERIFICATION_FABLE_2026-08-13.md`.

**RESULT: NOT REFUTED.** The verdict category survives every attack I could mount.
Three objections SURVIVE as evidence-quality defects (one mis-binning, two absences) that
must be absorbed, but none flips LEGITTIMA-DICHIARATA-MONITORATA to any alternative
(DA-RISCOPARE / CONDIZIONATA / LEGITTIMA-ESATTA all remain wrong for the reasons the
assessment gives, which I could not break).

---

## 1. Verification of the assessment's load-bearing anchors (all PASS)

| Claim in assessment | Check | Outcome |
|---|---|---|
| [T-EQBR] +6.3..+7.0% above frozen on every PR, bars <= 0.003 s, THEOREM* in [C-IGMIX] | M0 read at the block (~ll.968-982) | VERBATIM MATCH ("+6.3..+7.0% ABOVE the frozen ceiling on every PR (bars <= 0.003 s ...) THEOREM* within ... [C-IGMIX]") |
| C-IGMIX PRICED row + falsifier "finite-rate leaving the bracket" | hypothesis ledger §2 l.66 | MATCH |
| H-R1 executable rejector (total-enthalpy-flux across Gamma_d, afterburning channel) | hypothesis ledger §1 l.56 | MATCH ("Executable rejector minted S14 (PP-6)") |
| Paxson-Miki -15.6% mdot / -10.5% (589 lbf) ideal thrust from the remap; 5x the +120 lbf gain | report `paxson_miki_2022_nasa_opt.md` ll.88-94, 282-297 | ARITHMETIC AND QUOTES MATCH |
| Harroun 2021 Table 2: 9->5/3/2 species = 0.58/0.52/0.28% normalized thrust error; "reactions minimal" = judgement | report `harroun_2021_jpp_nozzle_perf.md` ll.78-81, 276-281, F11 | MATCH (incl. non-monotone-cancellation caveat) |
| Sun 2019 Fig.5 kinetics strictly interior, 1.385/1.35/1.26 at AR~200; T5/C13 inadmissibility as P1 instance | report `sun_2019_gamma_var_rao.md` T4 ll.203-215; confrontation advisory l.1101 (C13, pending-ratification) | MATCH, caveats carried |
| Miki 2020 declared H3 chemistry complete at combustor exit / frozen expansion | report `miki_2020_nasa_methodology.md` l.69 | MATCH |
| Hoffman 1987 H-d3 no condensed phases / frozen | report `hoffman_1987_ctp.md` ll.141-143 | MATCH |
| Confrontation-advisory items flagged pending-ratification | §3bis-J l.894, C13 l.1101 | Assessment's CAVA discipline correctly applied |

The Fable primary-source verification pass (`VERIFICATION_FABLE_2026-08-13.md`, header) found
that in every spot-check the per-paper READER reports were accurate and the demonstrated errors
lived in downstream summaries. The assessment cites reader reports and M0/ledger directly, i.e.
sits on the verified layer. No fabricated or drifted number found.

## 2. Attack 1 — evidence mis-binning in §3.1 / evidence item 1 (SURVIVES as objection, does not flip)

The Paxson-Miki remap is **CPG (gamma=1.182, R_g=60.12) -> frozen thermally-perfect CEA
mixture (R_g=71.05)** (report ll.63-68, H-U2 ll.122-124). **Both endpoints are frozen-composition
closures**: the CEA *equilibrium* calculation is used only to SET the frozen composition at the
time-averaged exit state. The -15.6% mdot / -10.5% ideal-thrust delta therefore prices the
**caloric-model + gas-constant bookkeeping gap (CPG vs TPG, unrepaired interface)** — NOT the
frozen-vs-shifting-equilibrium composition gap that [T-EQBR] brackets. The sentence "a live
instance of the [T-EQBR] frozen/equilibrium bracket being the dominant term" originates in the
reader report itself (F8, l.296-297) and is inherited by confront_gas §3.1 and by the verdict's
evidence line. That attribution is a category slip: as a T-EQBR instance the number proves
nothing (no equilibrium-composition leg is ever computed on the nozzle side).

Why it does not flip the verdict: the role the number plays in the verdict is "the thermo
closure is FIRST-order, hence the pin cannot be LEGITTIMA-ESATTA" — and that weaker reading is
exactly what report F8 also states ("the thermodynamic-closure uncertainty is roughly five times
the optimization gain") and what the assessment's own evidence line says ("closure is
first-order"). Strike the T-EQBR attribution entirely and first-orderness still stands on two
independent legs: the internal executable +6.3..+7.0% instance (M0, THEOREM* with bars) and
Wintenberger-Shepherd F7 ("significantly influenced", dissociated-products energy lock-up, with
the 0-D honesty rider the assessment already carries). LEGITTIMA-ESATTA stays excluded;
DICHIARATA stays required. **Required repair: re-label the -15.6%/-10.5% datum as
"thermo-closure/interface-bookkeeping dominance (CPG->TPG-frozen remap)", never as a
frozen-vs-equilibrium instance.**

## 3. Attack 2 — absence hunt: what the assessment never cites (two real absences, neither fatal)

Systematic sweep of all corpus members NOT cited by the assessment: Liu 2022, Wolanski 2013,
Teasley 2023, Teasley 2025, Hoffman 1987 (cited only via H-d3), Fernandes 2023 (gamma=1.4 air,
irrelevant), Kraiko family / Giles-Pierce / Rubino / Schotthofer / Zahr-Persson / Ancourt
(adjoint/variational layer, no gas-closure content — keyword counts 0-1 each), REFUTE_A/C/D
(no gas content), REFUTE_B (gamma-frozen H1 discussion only, T-T3 side).

### 3a. Liu 2022 — the one finite-rate-through-nozzle corpus member (ABSENCE, MEDIUM)
`reports/liu_2022_aerospike_rde.md`: the evaluation CFD is **reactive with reduced 21-species /
37-reaction Jet-A/air kinetics through the full domain including the aerospike nozzle**
(declared-adequate §2.2, l.98; 12M cells, l.42-43). This is the strongest available
counterexample-shaped fact against §2's flourish that the frozen closure "IS SOTA practice" for
the nozzle side — the corpus DOES contain a finite-rate RDE nozzle-flow simulation. The attack
fails to flip, for three reasons found in the same report: (i) Liu's **design layer** (the layer
our pin governs) is a single frozen gamma=1.26 imposed by fiat (F4 l.191, Angelino closed forms);
(ii) Liu publishes **no frozen-vs-finite-rate delta** (no frozen twin is run), so the
assessment's residual-risk sentence "the corpus contains no published finite-rate vs frozen
nozzle-flow delta for an RDE nozzle" remains literally TRUE — I verified there is no such delta
anywhere in the corpus; (iii) Liu's F10 (ll.263-271: variable-c_p NASA-polynomial CFD vs frozen
gamma=1.26 closed forms, never reconciled, "never states which gamma it means") is additional
corpus-side support for monitors 5-6 (gamma-status line, citation discipline). Ornano's reacting
stage-3 evaluator likewise keeps "no chemistry inside the nozzle ... pre-filled with N2/H2O
products" (`ornano_2017_pde_shapeopt.md` l.60) — supporting the pin, not breaking it. Sun 2019's
authors even state the field's own cost-benefit: CFD methods with chemical kinetics show "little
increase in specific impulse of the nozzle of large area ratio" (report ll.282-287).
**Required repair: the §2 census should name Liu 2022 as the finite-rate-evaluation member and
harvest F10 — its omission is an absence, though a verdict-preserving one.**

### 3b. Teasley 2023 + Kaemming-Paxson 2018 — corpus magnitudes for the PLACEMENT clause (ABSENCE, MEDIUM)
The assessment's §3.4 handles "fixed composition downstream of Gamma_d" with the H-R1 monitor
and no corpus magnitude. The corpus is not empty there:
- `reports/teasley_2023_nasa_state.md` l.55: **combustion completeness "90+ percentage"** with
  L* and L' an order of magnitude smaller than CP engines (paper p.2, p.23 concl. 3) — the NASA
  RDRE hardware family (the SAME family whose CFD papers Miki 2020 / Paxson-Miki assume
  "chemistry complete at combustor exit") measures a C*-efficiency leaving up to a ~10%-class
  energy/completeness deficit at the chamber, part of which is available for release downstream
  of any Gamma_d placed near the chamber exit. Caveat honestly carried: the report's
  undeclared-hypothesis 7 (l.72) shows the "90+%" depends on an unnamed CEA-class reference and
  unnamed MR/Pc, and a C* deficit conflates mixing losses, heat loss and incomplete combustion —
  it is a HOOK, not a priced afterburning fraction.
- `reports/kaemming_paxson_2018_eap.md` ll.94, 140: the EAP model itself calibrates
  **~6% of throughflow reacting deflagratively** (94% detonative) — a corpus-side scale for the
  non-detonative-release channel (in-chamber in their model, but the only quantified
  deflagrative fraction in the corpus).
These two numbers are exactly the kind of corpus evidence §3.4's placement discussion should
carry, and the assessment ignored both. The attack does not flip the verdict because the clause
is guarded by an EXECUTABLE rejector, not by the corpus: H-R1 (ledger §1 l.56, minted S14,
violation channel = afterburning) is monitor 3 of the verdict, and a monitored placement clause
with a named executable rejector is precisely the "MONITORATA" semantics. But the residual-risks
section should list the ~10%-class completeness deficit explicitly rather than implying corpus
silence on placement. **Required repair: add Teasley-2023 90+% completeness (with its H7 caveat)
and the K-P ~6% deflagrative calibration to §3.4/§6 as placement-channel magnitude hooks.**

### 3c. Exhausted absences (no further material)
Wolanski 2013: zero frozen/equilibrium/species content (measured grep; the survey argues the
nozzle OUT of the problem). Teasley 2025: manufacturing/test status, "no turbulence/chemistry
model named" (l.39). Litmap-extension advisory: zero gas-closure hits (measured). Choking
advisory "frozen T,u" (ll.172, 223) is Harroun's p-only inflow BC (azimuthally frozen T and u),
not chemistry — irrelevant to this bundle. Mean-swirl advisory: deflagrative asymmetries appear
only as PROVEN NON-channels for angular momentum — not composition evidence. No corpus paper
contradicts bracket interiority; no corpus paper supplies a per-propellant frozen-vs-shifting
table the assessment failed to use.

## 4. Attack 3 — internal-logic probes (all fail)

- **Gamma-interiority vs functional-interiority**: Sun Fig.5 shows interiority in gamma(AR)
  space (1-D, NTO/MMH, non-RDE); the bracket lives on the ceiling FUNCTIONAL. Interiority of
  gamma does not logically entail interiority of the functional value. The assessment however
  claims only "corroboration of the ORDERING ... the bracket assumes" and carries all three
  caveats (raster read-off, non-RDE, T5/C13 inadmissibility as P1 instance); the actual guard is
  the falsifier (finite-rate leaving the bracket), which is executable and registered. Probe fails.
- **Single-instance bracket generalization**: the assessment nowhere quotes +6.3..+7.0% as
  transferable; §4's honest summary explicitly forbids cross-propellant quoting without
  re-execution, and monitor 1 makes re-execution the rule. The fuel-oxygen worst-case direction
  (Wintenberger Fig.19) is carried in residual risks. Probe fails.
- **Verdict-category boundaries**: DA-RISCOPARE would need a corpus source contradicting the
  pin — none exists (measured sweep, §3c). CONDIZIONATA would need a validity window the
  monitors cannot express — but the error bar is two-sided, executable, falsifier-named; the
  only unpriced windows (condensables, hot fuel-oxygen re-execution) are declared exclusions or
  named residuals, which is the D-M semantics. LEGITTIMA-ESATTA is killed by first-orderness
  (surviving even after the Attack-1 strike, §2). The four-way partition is stable.
- **Monitor existence**: all six monitors verified in-repo (§1 table; gamma-status directive =
  memory `gamma-variable-generality`; species rung = Harroun F11 ADOPT). No monitor is an IOU.

## 5. Verdict on the verdict

**NOT REFUTED.** LEGITTIMA-DICHIARATA-MONITORATA stands. Surviving objections (evidence-quality,
to be absorbed at ratification):

1. **[MIS-BINNING]** The Paxson-Miki -15.6%/-10.5% datum is a CPG->TPG-frozen interface-remap
   price, not a [T-EQBR] frozen/equilibrium instance (both endpoints frozen; CEA used only to set
   the frozen composition). Quote it as thermo-closure/interface dominance; the mis-attribution
   originates in report F8 l.296-297 and propagates into the assessment's §3.1 and verdict
   evidence line. First-orderness survives on the internal T-EQBR instance + Wintenberger alone.
2. **[ABSENCE]** Teasley 2023 combustion completeness "90+%" (with its unnamed-reference caveat)
   and Kaemming-Paxson's calibrated ~6% deflagrative fraction are ignored corpus magnitudes for
   the "fixed composition downstream of Gamma_d" placement clause; §3.4/§6 should carry them as
   hooks feeding the H-R1 monitor threshold.
3. **[ABSENCE]** Liu 2022 is missing from the §2 SOTA-practice census: it is the corpus's only
   finite-rate-through-nozzle RDE evaluation (design layer still frozen gamma=1.26 by fiat), and
   its F10 gamma-inconsistency is additional external support for monitors 5-6.

None of the three changes the verdict category; all three change what the assessment may cite
verbatim at absorption time.
