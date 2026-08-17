# HYPOTHESIS AUDIT — [CONTRACT-MU] Interface-contract bundle vs the in-repo literature corpus

Auditor: S-FOUNDATIONS hypaudit subagent. Date: 2026-08-17.
Bundle under audit (from the frozen problem brief, `phaseA_problem_brief.md` §2/§4/§5):
(E1) fixed axisymmetric surface Γ_d downstream of ALL heat release; (E2) Γ_d carries s(ξ)
with probability measure μ = pushforward of normalized cycle time; (E3) L4 default (every
patch axially supersonic with margin), subsonic patches = declared closure case-class;
(E4) statistical stationarity for J_exact with liminf/limsup fallback; (E5) Pa constant,
quiescent ambient.

Sources: IN-REPO ONLY. Papers cited as [Author Year, file-where-read]. The confrontation
advisory `validation/ADVISORY_litreview_confrontation_2026-08-13.md` is cited throughout as
**PENDING-RATIFICATION evidence** (CAVA non ratificata), never as decided; where possible the
same datum is anchored on the per-paper reader report, whose accuracy the Fable verification
pass spot-checked positively (`literature_review/reports/VERIFICATION_FABLE_2026-08-13.md`,
header: "in every spot-check to date, the per-paper READER reports were accurate; the
demonstrated errors lived in DOWNSTREAM summaries").

Adversarial rule applied: literature data wins over internal preference. Verdict semantics
per the tasking (LEGITTIMA-ESATTA / LEGITTIMA-DICHIARATA-MONITORATA / CONDIZIONATA /
DA-RISCOPARE).

---

## 1. E1 — Γ_d "downstream of ALL heat release" (fixed, axisymmetric)

### What the corpus actually shows about where heat release ends

**No source in the corpus MEASURES a heat-release-free station.** The pin is everywhere an
*assumption of the models*, at three grades:

1. **Asserted judgment, undemonstrated** — [Harroun 2021, reports/harroun_2021_jpp_nozzle_perf.md
   §4 H-D1]: the nonreacting-downstream hypothesis is stated as *"chemical reactions would be
   minimal when the flow has reached the nozzle"* (p. 666) — the reader report explicitly grades
   it "stated as a judgement, not demonstrated". The same computation freezes inflow T at 3400 K
   *despite* acknowledging "a complicated, nonuniform temperature profile post-detonation"
   (p. 666).
2. **Imposed by construction** — [Paxson-Miki 2022, reports/paxson_miki_2022_nasa_opt.md §2]:
   nozzle-side chemistry is frozen by fiat: *"No reactions are utilized for this work. The fluid
   constituent species are 'frozen' throughout the domain"* (p. 5), composition from one CEA
   equilibrium call at the time-averaged exit state. [Harroun 2020,
   reports/harroun_2020_validation.md, H-D1]: "Frozen product species; chemical kinetics
   ignored."
3. **Quantified as NON-zero in the only model that carries it** — [Kaemming-Paxson 2018,
   reports/kaemming_paxson_2018_eap.md §3]: the Q2D source model is calibrated so that
   *"approximately 6% of the premixed RDE throughflow reacts" deflagratively* (p. 4–5). I.e.
   the community's own reference cycle model carries a parasitic-deflagration channel of order
   several percent of the throughflow — burning that does not complete at the detonation front
   and therefore releases heat *somewhere downstream of it*. Where it completes axially is not
   resolved by any in-corpus source.

Additional hard datum on heat-release-mode reality: [Teasley 2025,
reports/teasley_2025_rdre_dev.md, T-4 and §A-2]: for H2/O2, *"pure deflagration at higher
pressures exceeding 250 psia CTAP or so"* (p. 9) — the heat-release mode itself migrates with
operating point; and multi-mode operation at throttle is a stated *design requirement* (p. 7).
This is a chamber-side fact, but it warns that "all heat release" is an operating-point-dependent
spatial claim, not a geometric constant.

### Adjudication

The pin is **not contradicted** by any measurement in the corpus (nobody measured secondary
combustion in the expansion either way), but it is **nowhere verified**: the corpus's uniform
frozen-downstream practice is a modelling convention, and its one quantified in-model channel
(K-P's 6% deflagrative fraction) points against "ALL". Thrust is first-order sensitive to heat
addition at M > 1 (Rayleigh mechanism — the conversion factor already named in the program's own
Phase-A fork, `phaseA_tree_propulsion.md` FORK-5), so silent violation is not a second-order
defect. The program's ledger already owns this as C014
(`validation/ADVISORY_Sgauntlet_generality_ledger_2026-08-11.md`: "IN-NOZZLE HEAT RELEASE
(afterburning/parasitic deflagration) — R1 causal-separation clause of the interface contract +
H-R1 executable rejector (enthalpy-flux residual)").

**Element verdict: LEGITTIMA-DICHIARATA-MONITORATA** — legitimate as a declared idealization
matching SOTA practice, ONLY with the placement/settling audit armed:
- **Monitor E1-a (placement audit)**: cycle-resolved total-enthalpy-flux settling over a
  one-parameter family of candidate surfaces; Γ_d = first surface where d(enthalpy flux)/dx
  drops below a threshold DERIVED from the (v) thrust-error budget via the Rayleigh sensitivity
  (FORK-5 O2 of `phaseA_tree_propulsion.md`, recommendation O2+O3).
- **Monitor E1-b (always-on residual)**: declared source-term residual layer — heat addition
  downstream of Γ_d as a bounded model defect entering the (v) budget (FORK-5 O3 / C014 H-R1).
- **Named falsifier** (already in the tree): if enthalpy-flux settling never occurs inside the
  envelope E for a given engine, the frozen-downstream-of-Γ_d model class is REJECTED for that
  engine and the problem re-poses with a reacting layer (declared model-class change).

---

## 2. E2 — s(ξ) with μ = pushforward of normalized cycle time

### What the corpus shows about the cycle measure

The field USES cycle-time averaging but its weight convention is **partly undeclared and
internally inconsistent**:

- [Kaemming-Paxson 2018, reports/kaemming_paxson_2018_eap.md §4.2-2]: the identity "area
  average = time average in the detonation frame" is *asserted once, parenthetically, without
  proof* (p. 5) — it requires exactly the single-pure-rotating-mode hypothesis (our H-DATA);
  and the EAP_i chain itself then switches to mass-flux weights on the same plane.
- [Harroun 2021 via ADVISORY_rde_choking_2026-08-11 §3-bis(ii)]: the quasi-cycle-averaged
  C_F = 1.25 is built by "averaging ... for each point in time of the cycle" with **no formula
  or weight given** — "the averaging MEASURE is not merely inconsistent across the school — it
  is partly undeclared". Stechmann declares mass-weighting (Eq. 4); Harroun declares nothing.
- The corpus supplies a second, published, structurally different pressure measure: inverting
  Harroun's waveform Eq. (2) with ξ = θ/180 uniform gives dμ_P ∝ exp(−(P+5.78e6)/6.30e5) dP —
  **exponential in pressure**, not the log-uniform of the program's Lemma 2/T-O2 blowdown form
  [Harroun 2020, reports/harroun_2020_validation.md §4 and F4; same datum in Harroun 2021
  report §2bis "Measure note"]. Mandatory label per the pending-ratification confrontation
  (§3.3): **MODEL-DERIVED, not "measured"** (log-decay fit to a 2-D unwrapped CFD; the ~30 atm
  cap is a figure-read reconstruction).
- 64% of the cycle sits below the CTAP mean; only ~2.6% above 25 atm [Harroun 2020 report §4,
  reader arithmetic closing to −2.7% against the reported CTAP] — the measure is strongly
  low-pressure-weighted, which is exactly where the exit goes deeply overexpanded/subsonic.

### What the corpus shows about the H-DATA single-mode premise that μ rides on

μ = pushforward of cycle time is only well-defined per the brief under H-DATA (pure periodic
rotating wave, fixed wave count). The corpus shows the premise is PHYSICAL and can fail inside
real operating envelopes:
- [Teasley 2025, reports/teasley_2025_rdre_dev.md T-4]: wave mode is a function of chamber
  pressure and propellant; on a blowdown/throttle sweep "wave-count changes are expected to
  occur INSIDE the support of μ, not on a μ-null set", and detonation→deflagration (H2/O2,
  >250 psia CTAP) leaves the detonative model entirely.
- [Wolanski 2013 via confrontation §3bis-I, PENDING-RATIFICATION; reports/wolanski_2013_survey.md
  line 142]: galloping regimes and degeneration to deflagration, organized by the Wave Number
  W = t_r/t_mf — the D2.3 mode-transition exclusion "treats a PHYSICAL regime named in the
  field's vocabulary, not a convenience hypothesis".
- The one hardware protocol in the corpus IMPLEMENTS the exclusion: Harroun's CTAP + windowing
  "excluded the transient startup and shutdown of the RDE operation" [Harroun 2021 report
  §2bis-1 and F13] — the experimental realization of a μ carried only on windowed
  steady-state operation.

### Adjudication

The pushforward-of-cycle-time definition is the FORMALIZATION of what the field does tacitly
(and, in K-P's wave frame, asserts without proof). It is legitimate — indeed it is the
program's contribution that the weight becomes a theorem-level object instead of a habit
[choking advisory §3-bis(ii)]. But it is not "exact" against the literature in the
LEGITTIMA-ESATTA sense, because (a) the field's own record waveform induces a measure in a
different structural class than the program's blowdown lemma (a hard datum, not a
contradiction: T-O2 is a theorem *given* its blowdown form — Harroun 2021 report §2bis), and
(b) the single-mode premise it needs is violated inside real envelopes.

**Element verdict: LEGITTIMA-DICHIARATA-MONITORATA.**
- **Monitor E2-a**: H-DATA single-mode monitor (T0-flatness + wave-mode PSD / wave-count
  audit); mode-transition phases excluded from μ with the exclusion window declared in the
  measure's provenance (the CTAP-windowing precedent, Harroun 2021 F13).
- **Monitor E2-b**: measure-invariance falsifier run against a REAL second measure — Harroun
  Eq. (2) exponential-in-P (MODEL-DERIVED label mandatory), not only synthetic ones
  [Harroun 2020 report F4].
- **Monitor E2-c**: averaging-convention declaration in the same sentence as any J value
  (matched-ṁ vs matched-⟨p⟩ vs mass-flux weights); the corpus precedent for the slip is
  Harroun 2021's Methods-vs-Conclusions inconsistency [Harroun 2021 report §4-c, F9].
- **Content caveat on s(ξ)**: the interface data WILL carry swirl — "significant local
  tangential velocity components" [Paxson-Miki 2022 report F4, p. 2] — so the s(ξ) tuple and
  its audits must include the Γ = r·u_θ channel and the swirl-uniformity monitor
  (`validation/ADVISORY_rde_choking_2026-08-11.md` §4-bis F-swirl-1/F-swirl-2;
  `validation/ADVISORY_mean_swirl_panel_2026-08-11.md` for the adjudicated torque channels).
- Also load-bearing and cheap: the physical period f is dimensionally erased by the
  normalized pushforward, yet the one empirical closure (g_sep) provably needs it — `f_cycle`
  must ride in the data contract [Harroun 2021 report F10].

---

## 3. E3 — L4 default (every patch axially supersonic with margin); subsonic patches = declared closure case-class

### The exit-plane Mach data of record

This is the element where the literature bites hardest, and it must be stated adversarially:

- [Kaemming-Paxson 2018, reports/kaemming_paxson_2018_eap.md §3 + F11]: Table 1 (p. 6), the
  HEALTHY case: **M_8x max 1.33 / min 0.86 / avg 0.99** — the axial Mach at the throat plane is
  subsonic on part of EVERY cycle; Fig. 6 (p. 10) shows the dip covering roughly a third of the
  annulus in one case; §VI.H (p. 14): at low overall pressure ratio **M_8x ~ 0.5**. The reader
  report's F11 conclusion: "the spacelikeness margin min(M_x − 1) is therefore NEGATIVE on part
  of the interface … μ(Ξ_sub) > 0, page-verified."
- [Paxson-Miki 2022, reports/paxson_miki_2022_nasa_opt.md §4 + F4]: the published exit Mach
  1.15–1.45 is **total-velocity** Mach ("comprised of both axial and circumferential velocity
  components"), the axial component is NEVER shown, while "significant local tangential
  velocity components" are asserted (p. 2) — so "their data does not establish M_x > 1
  anywhere". The choking/decoupling claim is **assumed / BC-enforced** ("the exit plane
  boundary condition ... ensures that the flow is sonic or supersonic at all times", p. 2), and
  structurally guaranteed by one-way coupling — no back-pressure sensitivity run exists.
- [Stechmann 2019 via ADVISORY_rde_choking_2026-08-11 §1(a)]: exit-plane sonicity is a
  DECLARED ASSUMPTION ("It is thus assumed that the flow at the RDE exit plane is sonic at all
  points in the cycle to simplify the analysis"); no transonic analysis anywhere.
- [Kaemming-Paxson via choking advisory §1(b)]: the definition shift of record — choking is
  CYCLE-INTEGRAL ("any choking condition ... will have a range of axial Mach numbers... both
  subsonic and supersonic portions"); uniform M = 1 is an engineering surrogate priced at
  <5.4% by their own Fig. 7.
- Hardware corroboration that μ(Ξ_sub) > 0 is generic, not a corner: the cycle sweeps
  NPR ≈ 2→30 within one period against fixed sea-level ambient while the tested contours are
  single-point designs at NPR 13.7 / 19.3; 64% of the cycle sits below the CTAP → deep
  overexpansion for most of every cycle, with measured recirculating/reverse-flow regions
  and a wake-mode transition CROSSED within the cycle [Harroun 2020 report F5; Harroun 2021
  report F3, Fig. 18/20, NPR ≈ 6.7 transition].

The pending-ratification confrontation consolidates this into a citation PROHIBITION
(§3bis-G / D-36): neither source may be cited as evidence that RDE exit data is
L4-admissible — only that the SOTA *assumes or imposes* a sonic-or-supersonic interface; and
"μ(Ξ_sub) > 0 is the generic case, page-verified; the two-regime contract is load-bearing and
not defensive". The choking advisory (ratified-era, C1/C2) says the same in contract terms:
"NO GENERIC SUPERSONIC SURFACE ... the contract must be TWO-REGIME BY CONSTRUCTION"; the right
criterion is AXIAL, min_ξ(M_axial − 1) with margin, with the tangential component explicitly
separated.

### Adjudication

As POSED, the bundle already contains the saving clause: subsonic patches are a *declared
closure case-class*, not an afterthought. That is exactly what the literature demands. What the
literature REFUSES is any reading in which "default" means "generic": on the record data the
axially-supersonic-everywhere class is NOT the generic RDE case — a per-phase axially-subsonic
patch exists at the throat during part of every cycle even when the device is "effectively
choked" [choking advisory §1(b)], and no in-corpus dataset certifies L4 admissibility for any
real engine (the axial Mach is either sub-unity where reported, or unreported).

**Element verdict: CONDIZIONATA** — L4 is legitimate ONLY inside a named validity window:
instances where the stage-A audit measures min over Γ_d × Ξ of (M_axial − 1) > margin on the
actual data. Outside that window the declared subsonic closure branch is not a case-class but
the LOAD-BEARING branch. The named window and its instrument:
- **Monitor E3-a (decisive)**: per-phase axial-Mach margin audit min_ξ,patch (M_axial − 1),
  with swirl separated (total-Mach never accepted as a proxy) [choking advisory C2;
  Paxson-Miki report F4].
- **Monitor E3-b**: causal-separation certificate — "all normal characteristics outgoing at
  every phase on the extraction surface, else LOUD REJECT" — the certified version of the
  Paxson-Miki BC premise [choking advisory C3; Paxson-Miki report §4 verdict
  "ASSUMED, not demonstrated"].
- **Citation discipline**: the L4 citation prohibition (no published RDE exit Mach may be
  cited as L4 evidence) [confrontation §3bis-G/D-36, PENDING-RATIFICATION; independently
  supported by both reader reports].

---

## 4. E4 — Statistical stationarity for J_exact, liminf/limsup fallback

### What the corpus shows

- **CFD side**: limit cycles are reached and certified — Harroun: "limit cycle operation in
  10 to 15 wave revolutions" (p. 664, with the reader flagging: no residual, no periodicity
  error, no sensitivity to that count — undeclared-hypothesis (e)) [Harroun 2021 report §2,
  §4-e]. Paxson-Miki state the cleanest available stationarity certificate, the limit-cycle
  triple: exit-plane mass flow at limit cycle AND cycle-averaged thrust constant AND
  cycle-averaged mass in = mass out (p. 5) [Paxson-Miki 2022 report F12].
- **Hardware side**: stationarity holds only WINDOWED — the CTAP sampling "was windowed to the
  steady-state operation of the RDE" excluding startup/shutdown [Harroun 2021 report §2bis-1];
  tests are sub-second bursts, and at least one measurement chain "never reached a steady-state
  value during the short 0.9 s window of RDE operation" (Stechmann's centreline base pressure,
  p. 668) [Harroun 2021 report §4-g]. Mode stability is operating-point-dependent (single-wave
  vibratory environment "an order of magnitude greater than the mean", Teasley Fig. 7/p. 9;
  galloping regimes in Wolanski) [Teasley 2025 report T-5; confrontation §3bis-I].

### Adjudication

The literature supports statistical stationarity as an ACHIEVABLE, CERTIFIABLE property of
healthy single-mode operation (CFD limit cycles with certificates; windowed hardware
operation), and simultaneously shows it FAILS across mode transitions and transients — which
is precisely what the liminf/limsup fallback and the windowing exclusion are for. The brief's
formulation (declared objects = liminf/limsup brackets when the limit is not known to exist)
is the honest form; no source contradicts it; the field's own practice (windowing,
limit-cycle certificates) implements it informally.

**Element verdict: LEGITTIMA-DICHIARATA-MONITORATA.**
- **Monitor E4-a**: limit-cycle certificate triple adopted as a named stationarity audit
  (mass-flow limit cycle; cycle-averaged thrust constant; cycle-integrated in/out mass
  balance) [Paxson-Miki 2022 report F12].
- **Monitor E4-b**: declared observation window with startup/shutdown/mode-transition
  exclusion carried in the measure provenance (CTAP-window precedent) [Harroun 2021 report
  F13]; W = t_r/t_mf as a provenance label, grade PRACTICE, never certificate
  [confrontation §3bis-I, PENDING-RATIFICATION].
- **Monitor E4-c**: T-T0 flatness monitor stated WITH its measurable disambiguation (measured
  stand force ≠ axial momentum flux through an axisymmetric surface — the Teasley Fig. 7
  single-wave trace is structural response at 8.25 kHz, not a T-T0 falsifier)
  [Teasley 2025 report T-5].

---

## 5. E5 — Pa constant, quiescent ambient

### What the corpus shows

- Every in-corpus test and computation IS at constant sea-level ambient: Harroun far field
  quiescent P = 1 atm, M = 0.05, outlet 0.998 atm [Harroun 2021 report §2]; Paxson-Miki
  p_amb = 14.7 psia "constant on all external surfaces" (H-D8) [Paxson-Miki 2022 report §3];
  Teasley: "Sea-level ambient, un-stated, for all thrust/plume statements (MSFC TS115 open
  stand)" [Teasley 2023, reports/teasley_2023_nasa_state.md line 71]. As a description of the
  record test environment, Pa constant is EXACT.
- But the corpus also measures that the constant ambient COUPLES INTO THE FLOW at first order
  wherever a base/wake region exists, and does so through cycle-specific physics that no
  steady surrogate reproduces: measured base pressures 0.58–0.60 atm vs ~0.95 atm for the
  matched-ṁ constant-pressure twin against a 1 atm ambient — an error of 50–100% of the
  measured quantity, in the non-conservative direction [Harroun 2020 report F1, Fig. 7,
  five tests ≤1% matched ṁ]; the classical open-wake closure Pb/Pa = 1 is wrong in SIGN for RDE
  (Pb suctioned below ambient even in open wake) [Harroun 2020 report F7, p. 8]; base drag
  ≈ 12% of gross thrust with 38% sensitivity on reported pressure gain [Kaemming-Paxson 2018
  report F12, p. 9]; truncated-plug base drag −9.5% of nozzle thrust under genuine RDE cycle
  flow [Paxson-Miki 2022 report F9, p. 10].
- "Quiescent" is an idealization the record CFD itself perturbs deliberately (Harroun's
  M = 0.05 entrainment inlet): the ejector action of the cycle means near-nozzle fluid is NOT
  quiescent and base surfaces do NOT see Pa — "the period of the detonation-induced pressure
  wave was faster than the time necessary for the establishment of a steady-state condition in
  the base region, preventing the base region from adjusting to the ambient condition"
  [Harroun 2021 report §3a, p. 667].

### Adjudication

Pa constant quiescent is legitimate AS THE AMBIENT DATUM — it matches every test environment
in the corpus exactly. It is an idealization WITH NAMED BARS as soon as it is used as a
statement about the pressure actually seen by surfaces: (i) any wake/base/separated surface
sees a cycle-pumped pressure ≠ Pa (bar: 0.36–0.4 atm error on a ~0.6 atm quantity, the
measured ejector deficit); (ii) at sea level the cycle crosses the open/closed wake-mode
boundary (NPR ≈ 6.7) within every period — a switch/mode phase the averaged theory must
split or exclude [Harroun 2021 report F6]; (iii) the Pa ≠ 0 breaker kills
convention-independence of the collapse (harmonic-vs-arithmetic mean; tail-governed
constraint activity) even where the argmax survives [choking advisory §2-ter(B)(a)].

**Element verdict: LEGITTIMA-ESATTA within its scope (the ambient datum of the record test
environment) — with the scope boundary MANDATORY**: Γ_d-interior claims stay ambient-blind
only under H2' (full-flowing, supersonic exit every phase); the base region is
outside-by-construction and must never inherit the constant-Pa idealization silently
[Harroun 2020 report F1 scope discipline; Harroun 2021 report F1].

---

## 6. Bundle verdict

Element scores: E1 LEGITTIMA-DICHIARATA-MONITORATA; E2 LEGITTIMA-DICHIARATA-MONITORATA;
E3 CONDIZIONATA (named window = audit-passed instances; the subsonic branch is load-bearing
generically); E4 LEGITTIMA-DICHIARATA-MONITORATA; E5 LEGITTIMA-ESATTA within scope, with a
mandatory scope boundary.

**Bundle verdict: LEGITTIMA-DICHIARATA-MONITORATA** — the bundle AS POSED already carries its
own saving declarations (subsonic case-class; liminf/limsup fallback; H-DATA declared
monitorable), and no element is contradicted *as posed* by the corpus. The verdict is NOT
LEGITTIMA-ESATTA for the bundle because two elements are only conditionally exact and one
(E1) rests on a corpus-wide unverified convention; it is NOT DA-RISCOPARE because every
literature attack lands on an already-declared monitor or on the named validity window. The
single adversarial sharpening the record forces: the word "default" in E3 must never be read
distributionally — on the page-verified record, μ(Ξ_sub) > 0 is the generic case and the
declared-closure branch is load-bearing, so the bundle's certificates must PROVE L4 per
instance, never presume it.

### Consolidated monitors (required)

1. Γ_d placement audit: cycle-resolved enthalpy-flux settling with Rayleigh-derived
   threshold + always-on downstream heat-release residual in the (v) budget (E1-a/E1-b,
   C014/H-R1).
2. Stage-A axial-Mach margin audit min_{ξ,patch}(M_axial − 1) with swirl separated;
   total-Mach never accepted (E3-a).
3. Causal-separation certificate: all normal characteristics outgoing every phase, else loud
   reject (E3-b).
4. H-DATA single-mode monitor (T0 flatness + wave-count/PSD) with mode-transition exclusion
   window declared in μ provenance (E2-a/E4-b).
5. Limit-cycle stationarity triple: mass-flow limit cycle, cycle-averaged thrust constant,
   cycle-integrated in/out mass balance (E4-a).
6. Measure-invariance falsifier run against Harroun's exponential-in-P published measure
   (MODEL-DERIVED label) alongside the blowdown form (E2-b); averaging/matching convention
   declared in the same sentence as any J value (E2-c).
7. Swirl-uniformity monitor + Γ = r·u_θ channel in the s(ξ) contract; f_cycle as a required
   data-contract field (E2 caveats).
8. H2'/base-region scope fence: constant-Pa never applied to wake/base surfaces; wake-mode
   transition (NPR ≈ 6.7 class) treated as a switch/mode phase (E5).

### Residual risks (named, with bars where the corpus prices them)

- R1: In-nozzle heat release is unmeasured in the corpus; the only quantified in-model channel
  is ~6% deflagrative throughflow (K-P). If settling never occurs inside E, the model class is
  rejected (falsifier named; risk = late re-scope to a reacting layer).
- R2: L4 window may be empty on real engines: no in-corpus dataset certifies M_axial > 1
  anywhere; healthy-case throat axial Mach dips to 0.86 and low-PR to ~0.5 — the program may
  find the declared-closure branch carrying most of the certification weight.
- R3: The decoupling premise (no design→data back-reaction) is only ever BC-imposed in the
  SOTA; a genuine coupled falsification does not exist in the corpus — the causal-separation
  certificate can only be as good as the data source it audits.
- R4: Stationarity in hardware is windowed sub-second operation; some measurement chains never
  settle (0.9 s CTAP case). Cross-window/mode drift is a real bracket-widening term for
  J_exact.
- R5: The Pa ≠ 0 ambient couples at first order through the base region (0.36–0.4 atm on
  ~0.6 atm; 12% of gross thrust; −9.5% of nozzle thrust), with no accepted predictive closure
  in the corpus ("no way to create an analytical model predicting the base pressure",
  Harroun 2020 p. 7) — any configuration with a base carries this as a bracketed, not
  predicted, term.
- R6: The confrontation advisory consolidating several of these findings is
  PENDING-RATIFICATION; where this audit relies on it, the per-paper reader report is cited as
  the primary anchor, but final ratification could still adjust grades (not, on the evidence
  seen, directions).
