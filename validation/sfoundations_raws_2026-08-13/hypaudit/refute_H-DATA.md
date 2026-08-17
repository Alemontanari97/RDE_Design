# ADVERSARIAL REFUTATION — [H-DATA] verdict LEGITTIMA-DICHIARATA-MONITORATA

**Refuter:** subagent, 2026-08-17, S-FOUNDATIONS (R35) hypothesis-legitimacy audit.
**Target:** `validation/sfoundations_raws_2026-08-13/hypaudit/confront_hdata.md` (read in full).
**Corpus:** in-repo only (25-paper `literature_review/` + reports, validation advisories, M0,
PROGRESS). No web. Mandate: absence attack (what SOTA in-corpus evidence was ignored?) +
anchor verification + internal-consistency attack. Default refuted=true on overclaim.

**REFUTER VERDICT: NOT REFUTED** (refuted=false). The verdict category survives every attack
mounted. Four objections survive as non-flipping deficiencies (SO-1..SO-4 below); none moves
the verdict off LEGITTIMA-DICHIARATA-MONITORATA, and two of the ignored corpus items actually
STRENGTHEN the verdict beyond what the assessment claims.

---

## 1. Anchor verification (spot-checks at source — all load-bearing anchors HOLD)

| Bundle claim | Source check | Result |
|---|---|---|
| Wolanski F4: stable regular single-head + galloping/degeneration organized by W | `reports/wolanski_2013_survey.md:136-146` ("very regular and stable", Fig. 38 stable single-head; galloping Fig. 39, degeneration; Eqs. (4)-(5) p.144) | VERIFIED |
| Wolanski F8: W adopted as provenance label, NOT certificate | `wolanski_2013_survey.md:180-192` ("explicitly NOT as a certificate ... undefined critical volume V_cr ... no derivation") | VERIFIED |
| Teasley 2023 F3: mode zoo, >12 CW/CCW in 9 s, 3→2 transition | `reports/teasley_2023_nasa_state.md:91-93`, quotes verbatim at p.19/p.22 | VERIFIED |
| Teasley 2023 F11(i): no time-resolved measurement near nozzle interface; flatness certificate = only admission monitor | `teasley_2023_nasa_state.md:120-122` ("3-foot-long sense-lines", manifold transducers only) | VERIFIED |
| M0 VI.4bis(v): flatness monitor mandatory in every data contract; robust layer idle-not-absent | `docs/rde_nozzle_MASTER.md:1437-1441` verbatim | VERIFIED |
| Mean-swirl S1: counter-wave/unequal-count = NON-channels; aperiodic storage = H-AM1 violation | `ADVISORY_mean_swirl_panel_2026-08-11.md:23-27,73-75` + `ADVISORY_rde_choking_2026-08-11.md:198-200` (the adjudicated STRIKE of "wave-count asymmetries" and reclass under H-AM1 aperiodic storage) | VERIFIED |
| §3.22 pin-loses-hardware-provenance, cited pending-ratification | `ADVISORY_litreview_confrontation_2026-08-13.md:652-661` + registry row R20 line 1157 ("APERTO, owner F5") | VERIFIED, caveat correctly carried throughout |

No misquote, no inflated anchor, no pending-advisory item cited as decided. The
pending-ratification discipline (a common refutation lever) is clean: §3.22 is flagged
PENDING at every use, and residual R6 explicitly names the re-check obligation on ratification.

## 2. Absence attack — corpus items the assessment did NOT cite

Systematic sweep: grep for mode/transition/hysteresis/galloping/longitudinal/pulsation/
wave-count/slapping across all 29 report files + 4 validation advisories + PROGRESS POST notes.
Files with relevant content NOT cited by the assessment: `harroun_2021_jpp_nozzle_perf.md`,
`paxson_miki_2022_nasa_opt.md`, `kaemming_paxson_2018_eap.md`, `schotthofer_2024_windowing.md`,
`ornano_2017_pde_shapeopt.md`. Adjudication of each:

### 2.1 Ignored evidence that STRENGTHENS the verdict (absence attack FAILS in the refuting direction)

- **[Harroun 2021, `reports/harroun_2021_jpp_nozzle_perf.md:83-99,121-122`]** The JPP
  validation paper's inflow is Eq. (7), an analytic **pure two-wave rotating waveform**
  (13,800 Hz), no azimuthal-mode admixture, no transition, "the incoming flow was not rotating
  and had no vorticity" — and, decisively for the verdict's delta-claim: "**No grid-convergence
  index, no temporal-refinement study, no periodicity/limit-cycle residual certificate is
  reported**" (line 121-122). The field's premier validation study adopts H-DATA silently AND
  ships no monitor. The assessment claimed de-facto-scope status from Harroun 2020 alone; the
  corpus supports it 4×.
- **[Kaemming-Paxson 2018, `reports/kaemming_paxson_2018_eap.md:163,405`]** EAP is defined on a
  "single pure rotating mode" with frame steadiness "playing the role of our T-T0 wave-frame
  exactness" — the field's performance METRIC itself presumes H-DATA.
- **[Paxson-Miki 2022, `reports/paxson_miki_2022_nasa_opt.md:368`]** The SOTA optimization CFD
  case is "a clean two-wave uniformly-spaced mode (p. 4)". Third silent adopter; also an
  in-corpus instance that the family's fixed n need not be 1 (n=2 of record in SOTA practice),
  consistent with H-DATA's "fixed wave count n" phrasing.

A refutation on "the assessment ignored SOTA evidence" therefore lands on evidence that makes
the verdict MORE secure, not less. The under-citation is a completeness defect (SO-4), not a
refutation.

### 2.2 Ignored evidence that pressures the verdict — adjudicated, does NOT flip it

- **SO-1 — [Schotthöfer 2024, `reports/schotthofer_2024_windowing.md:68,159` (H-U3, F-A1/A2/A3)]
  IGNORED, and it prices the assessment's own admission pipeline.** The assessment's chain is:
  no hardware interface data (Teasley F11i) ⇒ every admissible CycleFamily is
  simulation-sourced ⇒ the monitor is the only gate. The corpus contains a MEASURED
  demonstration of how that extraction step fails: "9 % vector error and sign flips from a
  29 %-of-a-period shift in the averaging horizon (F-A1, F-A2), and a regime (chaotic /
  high-Re / mode-competing) where no window works at all (F-A3)" — stated in the report's own
  conclusions for "any cycle family extracted from an unsteady simulation" — plus H-U3: the
  period mean "shifts upwards", "the function is not exactly periodic", i.e. the averaging
  theorem applied outside its own hypothesis by the source paper itself. None of M1-M7 names a
  window-convergence / extraction audit, and nothing in the arming list specifies that M1
  (flatness) and M4 (stationarity) must run on the **multi-period source trace**, not on the
  extracted single-period family — a single-period family is internally flat by construction
  and blind to period-mean drift. **Why it does not flip the verdict:** it is an arming-spec
  gap inside the "MONITORATA" clause, not a legitimacy defect of the hypothesis; a correctly
  specified M1+M4 (multi-period horizon + drift detector) generically fires on exactly the
  Schotthöfer failure, so the failure class does not escape the monitor architecture — it
  escapes the assessment's *specification* of it. Required repair: add **M8 (window-convergence
  / source-trace audit)** or fold the multi-period-source requirement + a window-shift
  invariance check into M1/M4, anchored to Schotthöfer F-A1/A2/A3 as the in-corpus calibration
  datum.
- **SO-2 — [Harroun 2021 F6, `harroun_2021_jpp_nozzle_perf.md:205-210,407-418,596-598`]
  IGNORED: an in-corpus mode-transition mechanism missing from the violating-regime census.**
  "Open- to closed-wake transition occurs at approximately NPR = 6.7" (Fig. 17 caption); a
  plug/E-D configuration operating across it "**crosses the wake-mode boundary every cycle**";
  and the report's own caveat: the wake-mode transition "may be a mode transition proper (no
  steady per-state F on either side of it), in which case D2.3 routes it to the robust layer".
  The assessment's census (transitions, counter-rotation, slapping, galloping, degeneration,
  feed-coupled pulsation) omits this channel entirely, and M1-M7 all watch interface-mode
  identity — a family could pass all seven while containing an intra-cycle wake-mode switch.
  **Why it does not flip the verdict:** H-DATA governs the admitted *interface data family*
  (annulus-exit periodicity and mode purity); the wake mode is a downstream aerodynamic state
  of the per-state map F, so this datum pressures D2.3/T-T4/PB-2 (where the Harroun 2021 report
  itself files it, F5/F6), not the data hypothesis under audit. It survives as an
  incompleteness of the census sentence "the violating regimes ... are documented" and as a
  cross-reference the monitor list should carry (the switch-phase-vs-mode-transition
  adjudication is queued in that report's open items, line 596-598).
- **SO-3 — [Ornano 2017, `reports/ornano_2017_pde_shapeopt.md:86`] wording overclaim in the
  named absence.** The assessment states "The corpus contains no dedicated longitudinal-mode
  (LP) study." Ornano 2017 is a dedicated *pulsed*-detonation (axially-pulsating) nozzle
  shape-optimization study, read in-corpus, with its own single-pulse-representative-of-a-cycle
  hypothesis (line 86). True, it is a PDE, not an RDE longitudinal mode, and it contains no
  RDE LP data — so the escalation-lever conclusion (HB/ZP) stands — but the sentence as
  written is contestable by any reader holding the corpus index. Repair: scope the absence
  claim to "no RDE longitudinal/feed-coupled-mode study".

### 2.3 Remaining uncited files — swept, nothing relevant withheld

`wintenberger_shepherd_2004_thermo.md`, `liu_2022_aerospike_rde.md`,
`miki_2020_nasa_methodology.md`, `janc_2025_differentiable.md`: zero wave-mode/transition/
hysteresis content bearing on H-DATA (grep-proven, patterns above; hits are generic
"model"/"wave" usages). `ADVISORY_litmap_extension_2026-08-13.md`: classical-nozzle-line
content only; its 9 pattern hits are "modern/model" tokens — nothing on operating modes
(grep-proven). `ASSESSMENT_methodology_position_2026-08-13.md:85` carries the same R20
model-hypothesis reading the assessment already uses. PROGRESS POST notes: the only "mode" hit
is X-O31CS common-mode (unrelated). The bistability absence claim was re-checked: hysteresis
in-corpus appears only at `harroun_2020_validation.md:100` (H-U8, a silence) and an unrelated
line-search context in Janc — the assessment's "named absence" and its quarantine of the
Anand & Gutmark 2019 tree-only citation are both correct and honest.

## 3. Internal-consistency attacks on the verdict category

1. **"MONITORATA while nothing is armed" = overclaim?** No: the assessment states the unarmed
   state is itself a breach of M0 VI.4bis(v) (verified at `rde_nozzle_MASTER.md:1441`), makes
   the verdict explicitly conditional on arming (R1, owner F2), and rejects LEGITTIMA-ESATTA on
   precisely this ground. The condition is declared, not hidden.
2. **CONDIZIONATA-rejection sound?** Yes: the argument (no a-priori validity window nameable in
   operating-parameter space; mode identity propellant/Pc-dependent per Teasley 2025 p.9,
   corpus silent on hysteresis maps ⇒ the window IS the per-dataset monitor verdict) is
   corroborated at source and is exactly the DECLARED+MONITORED form. No in-corpus datum
   supplies the a-priori window that would make CONDIZIONATA the tighter verdict.
3. **Wolanski-vs-§3.22 tension (stable single-head trace vs "no hardware provenance")?**
   Resolvable and resolved in substance: Wolanski's Fig. 38 regularity is a lab-chamber
   observation over the photographed interval for "the mixture parameters tested"
   (`wolanski_2013_survey.md:138`), not a certified persistent single mode in thermal steady
   state on flight-class hardware — which is what §3.22 (pending) denies exists. The
   assessment holds both correctly (existence of the regime ≠ certified persistence); an
   explicit sentence distinguishing them would harden §1.1 against this attack, but no
   contradiction obtains.
4. **DA-RISCOPARE rejection sound?** Yes: H-DATA is per-family scope over admitted data, the
   machinery is general with periodic structure exploited only when certified (M0 VI.4bis(ii)
   verified: the cheap route is "a licensed specialization, not a replacement"), and the
   Teasley 2025 multi-mode-design pressure is correctly routed to the registered-not-adopted
   ν-extension (R5) rather than to a problem-statement re-scope. Nothing found in-corpus
   forces the re-scope.

## 4. Surviving objections (none verdict-flipping)

- **SO-1** [medium]: monitor suite incomplete/under-specified against Schotthöfer 2024's
  measured extraction-fragility of simulation-sourced families — the ONLY admissible source
  class per the assessment's own chain. Add M8 (window-convergence/source-trace audit; M1/M4
  run on multi-period source trace) before "MONITORATA" is claimed operative.
- **SO-2** [low-medium]: violating-regime census omits the Harroun 2021 wake-mode transition
  (NPR≈6.7, crossed every cycle; possibly a mode transition proper) — invisible to M1-M7;
  belongs as a cross-reference to the D2.3 switch-vs-transition adjudication already queued.
- **SO-3** [low]: "no dedicated longitudinal-mode (LP) study" should be scoped to RDE
  (Ornano 2017 is an in-corpus dedicated pulsed-detonation optimization study).
- **SO-4** [low]: de-facto-scope claim under-cited (Harroun 2021 Eq. (7) two-wave + no
  periodicity certificate; K-P 2018 single-pure-mode EAP; Paxson-Miki 2022 two-wave) and the
  R20 registry row (APERTO, owner F5) + D-12 ν-gating in the pending advisory are not carried
  into R2/R5, where they supply the named owner and decision lever.

## 5. Refuter conclusion

refuted = **false**. Every load-bearing anchor verifies at source; the pending-ratification
discipline is clean; the absence attack surfaces four omissions, of which the two that bear on
the verdict's direction STRENGTHEN it and the two that pressure it (SO-1, SO-2) are repairable
inside the DECLARED+MONITORED form without moving the category. The verdict does not
overclaim: its strongest self-limitation (no steady-state hardware provenance; monitor unarmed
= standing breach; per-dataset certification only) is stated in the assessment itself. The
monitor arming list must absorb SO-1 (M8/window-convergence) and cross-reference SO-2 before
any H-DATA-scoped production claim.
