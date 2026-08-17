# ADVERSARIAL REFUTATION ATTEMPT — [CONTRACT-MU] verdict LEGITTIMA-DICHIARATA-MONITORATA

Refuter: S-FOUNDATIONS hypaudit adversarial refuter. Date: 2026-08-17.
Target: `validation/sfoundations_raws_2026-08-13/hypaudit/confront_contract.md` (read in full).
Method: (1) absence attack — enumerate the in-repo corpus the assessment did NOT cite and read
it; (2) anchor spot-checks — verify the assessment's citations against the per-paper reader
reports; (3) aggregation attack — test whether the bundle verdict overclaims relative to its
own element scores. IN-REPO SOURCES ONLY. The confrontation advisory
`validation/ADVISORY_litreview_confrontation_2026-08-13.md` is cited strictly as
PENDING-RATIFICATION evidence, never as decided.

## FINAL RESULT: NOT REFUTED (refuted = false), with 5 surviving objections

The verdict survives. Every source the assessment ignored, once read, CORROBORATES the
assessment's direction (all findings in those reports are GAP-CONFIRMS / ADOPT / bounded-THREAT
grade; none reverses an element verdict); the assessment's anchors spot-check as accurate; and
the two candidate overclaim routes (bundle-level aggregation above the CONDIZIONATA element;
unconditioned E2) are already carried inside the assessment as the E3 element verdict, monitor 3
(causal-separation certificate), and residual risks R2/R3, with the sharpening stated in the
bundle paragraph itself ("'default' must never be read distributionally … certificates must
PROVE L4 per instance, never presume it"). What survives are monitor-specification and
completeness objections, none verdict-flipping.

---

## 1. Absence attack — what the assessment ignored, and what it actually contains

The assessment cites only Harroun 2020/2021, Paxson-Miki 2022, Kaemming-Paxson 2018, Teasley
2023/2025, Wolanski 2013, Stechmann (via the choking advisory). Ignored corpus members with
bearing on the bundle, now read in full:

### 1.1 Miki 2020 [reports/miki_2020_nasa_methodology.md] — STRONGEST OMISSION; corroborates

- **F-3 / hypothesis 8-9**: the NASA methodology-of-record interface is placed "at an axial
  location just upstream of physical throat" — i.e. **in SUBSONIC flow** — with a **full-state
  Dirichlet** BC (P0, T0, u, v, w, y_i), characteristically over-determined, which "mechanically
  suppresses upstream influence. … NASA's resolution is a numerical fiat, not a closure." This
  is a third, and the strongest, in-corpus instance of BC-imposed decoupling (the assessment
  anchored that claim on Paxson-Miki alone). Direction: strengthens E3 CONDIZIONATA and
  residuals R2/R3; does not reverse anything.
- **T-3**: choking-as-assumption verbatim ("this approach is based on the assumption that the
  flow is chocked at the throat", p.4) — corroborates the choking-advisory pattern the
  assessment already uses.
- **Hypothesis 3 (declared)**: "Chemistry is complete at the combustor exit; the nozzle
  expansion is chemically frozen" — a fourth frozen-downstream-by-convention instance;
  corroborates E1's "corpus-wide unverified convention" grading.
- **A-2(a)**: the published lab-frame interface traces have **T0 strongly non-flat**
  (1400→2200 K over one revolution); "a lab-frame azimuthal trace is NOT the wave-frame
  T0-flatness test — the monitor must be stated in the wave frame or it will read as failing on
  real data." → surviving objection SO2 against the assessment's monitor 4 as written.
- **A-2(b)**: the airbreathing fixed-Pt_in rig's μ "is the (empirical, non-atomic) pushforward
  of the Fig. 4 traces" — NOT log-uniform blowdown and NOT Harroun's exponential-in-P: a
  **third structural measure class in the corpus**, absent from the assessment's E2-b
  measure-invariance falsifier set. → surviving objection SO3.

### 1.2 Schotthöfer 2024 [reports/schotthofer_2024_windowing.md] — corroborates; names the E2↔E3 coupling

- **F-T2**: the Leibniz interchange under the cycle integral FAILS when the measure/period is
  design-dependent (Eq. 5; residual priced by Krakos Eq. 12). Exogeneity of μ
  (`dμ/dΣ = 0`) is exactly the unnamed hypothesis, "guaranteed on the L4 class" — i.e.
  **E2's data-status premise is conditioned on the SAME window E3 is graded CONDIZIONATA on**.
  The corpus registers this as H-EXO with falsifier `dμ/dΣ ≠ 0` and activation note
  "F5 / μ(Ξ_sub)>0" [confrontation advisory line ~630 and decision row D-02 —
  PENDING-RATIFICATION]. The assessment grades E2 unconditionally and never names the channel;
  it is, however, operationally covered by its monitor 3 (all-characteristics-outgoing causal
  separation ⇒ no upstream influence ⇒ structural exogeneity), so this does not flip the
  verdict. → surviving objection SO1.
- **F-F3**: on T-T0-certified single-mode data the entire period-dependence term of the Krakos
  bound vanishes (`∂_s h ≡ 0`) — upgrades the value of the assessment's monitor 4, consistent
  with its direction.
- **F-A2**: any μ/cycle family EXTRACTED from an unsteady simulation is itself a
  windowed-averaging problem (measured: 29%-of-period window shift ⇒ 9.1% sensitivity error
  with sign flips; mean drift on a healthy LCO) — the monitor list lacks "declared window +
  declared k + period-shift rejector" on μ provenance. → part of SO5.
- **F-A3**: in the chaotic/mode-competing regime NO window works (sensitivity diverges for
  every window at Re 1e6) — consistent with the assessment's routing of mode transitions out
  of μ (monitor 4), and with E4's windowed-stationarity grading.

### 1.3 Ornano 2017 [reports/ornano_2017_pde_shapeopt.md] — corroborates

Uniform-in-time averaging over a single pulse; "the measure never becomes an object: it is
never named, never normalized, never varied" (F-3); objective deliberately re-defined to dodge
phase-dependence of thrust (F-2: "independent of the phase delay between inlet and outlet") —
published practitioner-level attestation of exactly the problem the bundle's μ formalization
and T-T0 solve. Supports the assessment's E2 adjudication ("formalization of what the field
does tacitly") verbatim.

### 1.4 Liu 2022 [reports/liu_2022_aerospike_rde.md] — corroborates

- **F5**: choking asserted from observation and folded into the reduction — including for
  Case A with ε = 100%, no geometric constriction at all. Strengthens E3's "assumed, never
  certified" line.
- **F9**: a THIRD undeclared averaging convention in the corpus — the state-averaged stagnation
  reconstruction `P_c := f(⟨p⟩, ⟨M⟩)` (Eq. 14), Jensen gap never bounded, propagating into
  every headline number. The assessment's monitor E2-c names only matched-ṁ / matched-⟨p⟩ /
  mass-flux; this corpus convention is missing from the declared list. → part of SO3.
- **F12b**: base pressure 0.16 atm vs Pa = 0.36 atm (44% of ambient) — a third external base
  datum consistent with E5's mandatory scope fence. Note also: Liu's constant Pa is 0.36 atm,
  NOT sea level — the assessment's E5 evidence line ("matches every record test environment"
  citing three sea-level environments) is incomplete as stated but unharmed in substance
  (constant-Pa is what E5 pins, and Liu is constant).

### 1.5 Wintenberger-Shepherd 2004 [reports/wintenberger_shepherd_2004_thermo.md] — corroborates

- **F4**: the Fig. 26/27 basis-inversion (equal pre- vs post-combustion pressure flips the
  cycle ranking) is an independent thermodynamic-school precedent for E2-c's
  convention-declaration monitor — supports it, from a school the assessment never touched.
- **F6**: a Δs_min/Δs_irr entropy-budget audit on imported interface data is named as a missing
  contract audit (PRACTICE grade, the split itself a conjecture per the authors) — absent from
  the assessment's monitor list. → part of SO5.
- **F1**: the FJ bound is shape-blind and cannot bear on the bundle — correctly ignorable; its
  omission by the assessment is harmless.

### 1.6 Findings omitted from a paper the assessment DID cite — Harroun 2020 F3/F10

[reports/harroun_2020_validation.md F3]: the corpus's ONLY direct published indictment of
cycle-averaged evaluation — the authors' own diagnosis "**the axisymmetric cycle-averaging is
too simplistic of a method to estimating performance potential**" (p.11), with the computed
flared>IE 1%-Isp ranking contradicted by measured wall-pressure ranking IE>flared. The
assessment never mentions it. Why it does not flip the verdict: the reader report itself bounds
it to MEDIA with four named mitigations (no thrust/Isp measurement exists for the paired tests;
operating points not matched; **cowl-only** geometry difference, i.e. the disputed physics is
cowl recompression/plume interaction outside the bundle's H2' fence; the criticized surrogate
discards azimuthal nonuniformity, coarser than the contract's s(ξ) family). Same for F10 (3D
transient necessity: "real but scoped" to base/wake/separated regions the bundle's E5 fence
already excludes). But PROTOCOL T3-CONTROL's binding obligation — "any decisive
cycle-averaged-vs-steady comparison must cite this discrepancy" — is a corpus-anchored
monitor-class obligation missing from the assessment's consolidated monitor list. → surviving
objection SO4.

## 2. Anchor spot-checks — the assessment's citations are accurate

- K-P Table 1 M_8x 1.33/0.86/0.99 + §VI.H "M_8x ~ 0.5" — verified at
  reports/kaemming_paxson_2018_eap.md lines 122, 227-230, 406-412; F11's "μ(Ξ_sub) > 0
  page-verified" as quoted.
- Harroun 2020 base data 0.58–0.60 atm, matched-ṁ twin 50–100% error non-conservative, open-wake
  Pb < Pa in sign, "no way to create an analytical model predicting the base pressure" — all
  verified at reports/harroun_2020_validation.md F1/F2/F7 (including the psia→atm typo hygiene
  the report itself flags; the assessment quotes atm, correctly).
- Exponential-in-P measure dμ_P ∝ exp(−(P+5.78e6)/6.30e5) dP, MODEL-DERIVED label, 64%-below-CTAP
  weighting — verified at report §4/F4, lines 121, 143-144.
- Choking advisory C1 "NO GENERIC SUPERSONIC SURFACE … TWO-REGIME BY CONSTRUCTION", closure
  branch "promoted from corner-case to LOAD-BEARING" — verified at
  ADVISORY_rde_choking_2026-08-11.md lines 66-72.
- Confrontation §3bis-G / D-36 L4 citation prohibition + "μ(Ξ_sub)>0 generic case
  page-verified" — verified (D-36 row), correctly handled as PENDING-RATIFICATION with
  reader-report primary anchors.
- Reader-report reliability premise — VERIFICATION_FABLE_2026-08-13.md header as quoted.

No misquote, no inflated number, no mishandled ratification status found.

## 3. Aggregation attack — does the bundle verdict overclaim above its elements?

Candidate argument for refuted=true: element E3 is CONDIZIONATA with a possibly-EMPTY validity
window (assessment's own R2: "no in-corpus dataset certifies M_axial > 1 anywhere"), the
subsonic branch is load-bearing generically, and — via SO1 — E2's exogeneity is conditioned on
the same window; a weakest-link aggregation would give the BUNDLE verdict CONDIZIONATA, so
LEGITTIMA-DICHIARATA-MONITORATA overclaims.

Why the argument fails on the record:
1. The assessment does not hide the conditionality — it is stated three times (E3 verdict; the
   bundle paragraph's adversarial sharpening; R2), and the bundle grade is explicitly argued:
   the bundle AS POSED carries the subsonic case-class as a declared closure branch, which is
   "exactly what the literature demands" (choking advisory C1 says two-regime-by-construction,
   not never-pose-L4). A declared two-regime contract with an armed per-instance audit is the
   literature-compliant object; grading it CONDIZIONATA at bundle level would punish the bundle
   for the very declaration the ratified-era advisory mandates.
2. The E2 conditioning (SO1) lands on an already-declared monitor: the causal-separation
   certificate (monitor 3) is precisely the per-instance discharge of exogeneity — all normal
   characteristics outgoing ⇒ no design→data back-reaction ⇒ dμ/dΣ = 0 structurally. The
   channel is unnamed, not unguarded.
3. Every ignored source reads in the SAME direction as the assessment (§1); an absence attack
   refutes only if the absent evidence points the other way. Here it uniformly deepens the
   assessment's own case (more BC-imposed decoupling instances, more assumed choking, more
   undeclared conventions) — all of which the declared monitors are shaped to catch.
4. No DA-RISCOPARE evidence exists anywhere in the corpus: no source measures a contract
   element to be FALSE as posed (with its declarations); the failures found are all failures of
   the SOTA's undeclared versions of the same idealizations, which is the assessment's thesis.

## 4. Surviving objections (verdict-preserving; owed to the monitor spec)

- **SO1 (E2↔E3 coupling unnamed).** Measure/data exogeneity (`dμ/dΣ = 0`, `ds(ξ)/dΣ = 0`) is
  guaranteed only on the L4 class [Schotthöfer report F-T2; confrontation line ~630 + D-02,
  PENDING-RATIFICATION]; outside the audit-passed window, E2's premise that (s(ξ), μ) is
  design-independent DATA is conditioned by the same window as E3. The assessment grades E2
  unconditionally and never names H-EXO; monitor 3 covers it operationally but the bundle text
  should carry the hypothesis by name with its falsifier (`dμ/dΣ ≠ 0` measured).
- **SO2 (monitor 4 frame mis-specification).** T0-flatness must be stated IN THE WAVE FRAME; on
  Miki 2020's published lab-frame traces (T0 1400→2200 K over one revolution) the monitor as
  written falsely fires on real, healthy data [Miki report A-2(a)].
- **SO3 (measure/convention library incomplete).** The corpus holds a third structural measure
  class — Miki 2020's empirical non-atomic pushforward from a fixed-Pt_in airbreathing rig
  (neither log-uniform blowdown nor exponential-in-P) [Miki A-2(b)] — and a third undeclared
  averaging convention — Liu 2022 Eq. (14) state-averaged stagnation reconstruction
  `f(⟨p⟩,⟨M⟩)` [Liu F9]. Neither is in the E2-b invariance-falsifier set or the E2-c declared
  convention list.
- **SO4 (omitted adverse datum).** Harroun 2020 F3 — the field's only direct published
  indictment of cycle-averaged ranking ("too simplistic", 1%-Isp ranking contradicted by
  measured wall pressures) — and F10 (3D-transient necessity) are absent from the assessment;
  both are bounded and outside the bundle's H2' fence, but PROTOCOL T3-CONTROL's citation
  obligation belongs in the consolidated monitor list.
- **SO5 (monitor-list completions).** (a) declared window + declared k + period-shift rejector
  on any μ/cycle family extracted from an unsteady simulation [Schotthöfer F-A2]; (b)
  per-phase Δs_min/Δs_irr entropy-budget audit on imported interface data, PRACTICE grade
  [W-S 2004 F6].

## 5. Verdict of this refutation attempt

**refuted = false.** The assessment's verdict LEGITTIMA-DICHIARATA-MONITORATA for [CONTRACT-MU]
survives adversarial confrontation with the full in-repo corpus, including five sources and two
findings it did not cite. All ignored evidence corroborates its direction; its anchors are
accurate; its one genuinely conditional element (E3) is disclosed, monitored, and correctly
carried into the bundle statement. The surviving objections SO1–SO5 are monitor-specification
and completeness repairs, owed at F2 consumption of the bundle, not verdict changes.
