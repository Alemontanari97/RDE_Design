# ADVERSARIAL REFUTATION — [SEED-B] verdict LEGITTIMA-ESATTA

**Role:** adversarial refuter, S-FOUNDATIONS (R35) hypothesis audit. **Date:** 2026-08-17.
**Hypothesis under audit:** "for a single steadily rotating wave (fixed wave count, constant
speed), the flow is steady in the co-rotating frame and the time-averaged axial thrust equals
the wave-frame steady thrust (axial momentum flux is invariant under the frame rotation)."
**Assessed verdict:** LEGITTIMA-ESATTA.
**Sources:** IN-REPO ONLY per brief. `ADVISORY_litreview_confrontation_2026-08-13.md` cited
strictly as **pending-ratification evidence (CAVA NON RATIFICATA)**, never as decided.

**OUTCOME: REFUTED AS GRADED.** The bundle is LEGITTIMA throughout — no in-repo source
falsifies any conjunct physically — but **ESATTA does not survive for the bundle as worded**.
The bundle fuses two legs of different rigor class of record: the identity legs
(time-average = wave-frame thrust; axial-flux frame invariance) are theorem-exact
*conditional on the rotating-pattern field ansatz*; the leg that gets the flow INTO that
ansatz from the stated observables ("fixed wave count, constant speed") is of record a
**SCHEMA + declared monitored model hypothesis**, with a named monitor-blind counterexample
channel inside the antecedent. Grading the fused bundle ESATTA contradicts the repo's own
of-record classification and the standing monitoring apparatus that exists precisely because
this leg is *not* exact. The correct surviving form is a split grade (below).

---

## 1. Decomposition and in-corpus status of each conjunct

The bundle asserts three things:

- **(A)** given a single steadily rotating wave *(operationalized in the parenthetical as:
  fixed wave count, constant speed)*, the flow is steady in the co-rotating frame;
- **(B)** the time-averaged axial thrust equals the wave-frame steady thrust;
- **(C)** the mechanism: the axial momentum flux is invariant under the frame rotation.

| Conjunct | In-corpus carrier | Rigor class of record | Result |
|---|---|---|---|
| (B)+(C) *conditional on the rotating-pattern field* | T-T0 claims (i)-(iii), quoted at print in `literature_review/reports/REFUTE_A_symmetry_reduction.md` Linea (1) (M0 r.442-453: constant thrust, wave-frame equality, axial closure — Coriolis −2W e_x×w ⊥ e_x, centrifugal W²r radial) | THEOREM | EXACT, conditional |
| (B)+(C) — external confrontation | `ADVISORY_litreview_confrontation_2026-08-13.md` §3.13 (Claim 14): **CONFERMATO, con CLAUSOLA DI DISAMBIGUAZIONE OBBLIGATORIA** *(pending ratification)* | confirmed-with-mandatory-clause | survives, never clause-free |
| (A) from the stated observables | `REFUTE_A_symmetry_reduction.md` Linea (1): the data⇒field / observables⇒pattern step is a **PROPAGATION claim T-T0 does not contain**; "l'attribuzione a 'T-T0 exactness' da sola è una citazione eccessiva" (VERDETTO (1): INDEBOLITO) | SCHEMA + declared class hypothesis + monitor | **NOT exact of record** |
| (A) — current M0 status | `[S-T0P]` PROPAGATION LEMMA, "SCHEMA — written of record 2026-08-13", proof route *named* (SO(2)/helical equivariance + certified-S1 uniqueness + L4 finite domain of dependence), falsifier named, **full proof write-up owner = F2 theory window**; and M0's own honest boundary: "the pin (pure rotating wave, T0-flatness monitor) is a **MODEL HYPOTHESIS with no certified hardware provenance** (R20)" | SCHEMA | **NOT exact of record** |

External corroborations of the identity legs, from the reports (these support LEGITTIMA, not
ESATTA-of-the-bundle):

- **[Kaemming-Paxson 2018]** (`reports/kaemming_paxson_2018_eap.md` §4.2-2 and F1 clause (iv)):
  the paper *asserts without proof* "a simple area weighted average (equivalent to a
  time-average in this frame of reference)" (p.5) — exactly conjunct (B), used by the field as
  an obvious fact; the report's finding: "our T0(i) used tacitly as a fact, proved here
  [by us] as a theorem", with the precision that the assertion "requires a single pure
  rotating mode". The corpus needs the theorem; it does not already contain a proof.
- **[Ornano 2017]** (`reports/ornano_2017_pde_shapeopt.md` F-2, quote p.3): exit force chosen
  over thrust "to obtain a solution that would be independent of the phase delay between inlet
  and outlet" — the published articulation of the problem conjunct (B) solves.
- **[Paxson-Miki 2022]** (`reports/paxson_miki_2022_nasa_opt.md` F12): contrast of record —
  "they require the *cycle-averaged* thrust to be constant in *iteration*; T-T0 asserts the
  *instantaneous* thrust is constant in *time* through every axisymmetric surface"; their
  clean 2-wave case is a T-T0 instance whose instantaneous-thrust flatness is **never
  plotted** — "an unexercised falsifier sitting in published NASA data".

## 2. The exactness attack on conjunct (A): why ESATTA falls

**2.1 The antecedent under-determines the field.** "Fixed wave count, constant speed" are
observables of the wave; "steady in the co-rotating frame" is a property of the ENTIRE field
(rotating-pattern ansatz q = q~(x, r, θ−Wt)). T-T0 *hypothesizes* the pattern on the field
(M0 r.442-445 via REFUTE_A Linea (1); restated verbatim in the [S-T0P] block: "T-T0
HYPOTHESIZES the rotating pattern on the field"). The step from data/observables to
field-pattern is the propagation lemma, and its in-repo rigor class is SCHEMA — registered
with a named proof route and a named falsifier ("an L4-certified pure-periodic-data instance
whose certified solution is NOT a steady co-rotating pattern"), full write-up owned by the F2
theory window. A conjunct whose carrier is SCHEMA-with-open-falsifier cannot be graded ESATTA.

**2.2 Concrete counterexample channel INSIDE the stated antecedent** (REFUTE_A Linea (4),
caveat da refuter). A lab-frame-fixed injector imprint (harmonic locked to the injector
count, a function of θ, not of θ−Wt) can coexist with a single wave of fixed count and
constant speed. The total field is then two-frequency, s(θ, θ−Wt) — **steady in NO frame** —
and conjunct (A) is false while the antecedent as parenthesized holds. Worse for the monitor
story: the purely lab-steady component *also produces constant thrust* (same shift-invariance
proof as T-T0(i) applied to a lab-steady field), so the **T0-flatness monitor is BLIND to
this channel**; the detector of record is the data-contract harmonic audit plus the
mean-swirl TRIPLE monitor — `ADVISORY_mean_swirl_panel_2026-08-11.md` rows [F-swirl-2]
(stage-A uniformity monitor on (Γ, h0, s), G6 rejector semantics) and the angular-momentum
balance-residual audit ("rejector semantics identical to T0-flatness"). An "esatta" grade
erases exactly the distinction (which detector guards which channel) that the corpus went to
the trouble of writing down.

**2.3 The repo's own apparatus contradicts ESATTA-as-a-bundle.** If (A) were exact, the
T0-flatness certificate, the harmonic-decay certificate, the Floquet/monodromia certificate
(confrontation A20, *modulo the symmetry group* — pending ratification), and the
limit-cycle certificate triple (Paxson-Miki F12 / confrontation A29 — pending ratification)
would all be idle. They are load-bearing, standing instruments. M0's [S-T0P] block states the
honest boundary in so many words: the pure-rotating-wave pin is "a MODEL HYPOTHESIS with no
certified hardware provenance (R20)".

**2.4 Audit-wave consistency.** The sibling assessment on the adjacent hypothesis
(`hypaudit/confront_axisym.md`, upheld by `hypaudit/refute_confront_axisym.md`) **refused
LEGITTIMA-ESATTA on precisely these grounds** ("currently over-cites T-T0 — propagation lemma
[full proof] unwritten, REFUTE_A duty R4") and the refuter found that refusal "not an
underclaim". Granting ESATTA to SEED-B, which contains the same slide, would put the audit in
contradiction with itself.

## 3. What survives exactly (and must not be given away)

Conditional on the rotating-pattern field with T-T0's printed hypotheses — **S a fixed
axisymmetric surface, axisymmetric wall, Pa constant, piecewise-smooth transversal fronts**
(M0 r.442-445 via REFUTE_A) — the identity legs are exact and are, if anything,
UNDER-claimed by the bundle:

- **(B) strengthens:** not merely "time-averaged thrust = wave-frame thrust" — the
  INSTANTANEOUS axial thrust is constant in time through *every* axisymmetric surface
  (T-T0(i); the Ornano phase-delay problem dissolves, report F-2). The time-average statement
  is the trivial corollary.
- **(C) is the right mechanism and is proved, not assumed:** rotation about the thrust axis
  leaves ρ, u_x, p pointwise unchanged; the fictitious forces have no axial component
  (Coriolis ⊥ e_x, centrifugal radial — T-T0(iii) via REFUTE_A Linea (5), "TIENE-come-
  prezzato"). No in-corpus source contests this.
- **Spurious refutation channel checked and rejected:** [Liu 2022]'s documented failure of
  "design at time-averaged parameters" (`reports/liu_2022_aerospike_rde.md`, e.g. the Jensen
  gap at line ~108, p.2 "proved" overclaim) does **not** touch (B): Liu averages the *state*
  and pushes it through nonlinear isentropic maps; (B) averages the *flux integral* itself,
  which is linear in the integrand. Different object; no contradiction.
- **Spurious physical refutation checked and rejected:** [Teasley 2025] Fig. 7 single-wave
  thrust-trace scatter (±1000-1500 lbf on ~4500-5000 lbf) and the p.9 quote "a single wave
  imparts a substantial vibratory environment on hardware, in some cases, an order of
  magnitude greater than the mean" (`reports/teasley_2025_rdre_dev.md` T-5) is a
  perception-level threat, not a counterexample: the load cell measures the mount reaction to
  a rotating TRANSVERSE unbalance, not the axial momentum flux through an axisymmetric
  surface. BUT — per §3.13 of the pending-ratification confrontation — this defense is "an
  hypothesis plausible, not an established fact" (the paper publishes neither sampling
  frequency, nor load-cell axis, nor filters), which is exactly why the disambiguation clause
  is MANDATORY, and why the 8.25 kHz peaks must not be attributed to the 1-wave trace
  (they are Fig. 10 = MARLEN HF021, 2-wave mode).

## 4. Verdict of this refutation

**refuted = TRUE (as graded).** The bundle is legitimate and its identity core is
theorem-exact, but LEGITTIMA-ESATTA for the fused statement does not survive the in-repo
record. The surviving formulation, which the assessment should be amended to:

> **Split grade.** (i) *LEGITTIMA-ESATTA, conditional:* GIVEN a rotating-pattern field
> (q = q~(x,r,θ−Wt)) on a fixed axisymmetric surface with axisymmetric wall and constant Pa,
> the instantaneous — a fortiori time-averaged — axial thrust equals the wave-frame steady
> thrust, and the axial momentum flux is invariant under the frame rotation (fictitious
> forces have no axial component). AXIAL COMPONENT ONLY: the transverse load is a rotating
> unbalance, unsteady in the lab frame, outside the statement.
> (ii) *LEGITTIMA-DICHIARATA-MONITORATA:* the step from the stated observables (single wave,
> fixed count, constant speed) to the rotating-pattern field is the propagation leg — of
> record [S-T0P] at SCHEMA (proof route named, falsifier open, full proof = F2 duty) and a
> declared MODEL HYPOTHESIS monitored by T0-flatness — with the printed caveat that flatness
> is blind to the lab-steady injector-harmonic channel, whose detector is the data-contract
> harmonic audit + the mean-swirl TRIPLE (Γ,h0,s) monitor.

**Surviving objections (owed amendments):**
- **SO-1 (grade-flipping):** conjunct (A) from "(fixed wave count, constant speed)" is
  SCHEMA + monitored model hypothesis of record ([S-T0P]; REFUTE_A Linea (1)), not exact;
  the bundle's grade must split as above.
- **SO-2 (grade-flipping, the counterexample channel):** the lab-frame-fixed injector
  harmonic satisfies the stated antecedent, defeats co-rotating steadiness (field steady in
  no frame), and is invisible to the T0-flatness monitor (it produces constant thrust
  itself); the clause naming the correct detector (harmonic/contract audit + mean-swirl
  TRIPLE) must ride with the hypothesis (REFUTE_A Linea (4); ADVISORY_mean_swirl rows).
- **SO-3:** the exactness perimeter must print T-T0's hypotheses — fixed axisymmetric S,
  axisymmetric wall, constant Pa, piecewise-smooth transversal fronts — and the axial-only
  restriction.
- **SO-4:** the MANDATORY disambiguation clause of pending-ratification §3.13 / Teasley T-5:
  measured stand force ≠ ∮ axial momentum flux; the single-wave vibratory environment is a
  transverse/structural load; the Teasley defense is plausible-not-established; no 8.25 kHz
  attribution to the 1-wave trace.
- **SO-5 (minor):** state the stronger true form (instantaneous constancy through every
  axisymmetric surface, Paxson-Miki F12 contrast) and record that the flatness falsifier is
  unexercised in published NASA data — the empirical leg is monitor-carried, not
  evidence-carried.

**Limits of this refutation:** in-repo sources only, per brief; the confrontation advisory
used exclusively as pending-ratification evidence; the [S-T0P]/M0 status cited as repo state
of record (rigor-class bookkeeping), with the adjudicating evidence drawn from the allowed
corpus (REFUTE_A, VERIFICATION_FABLE Stage 3 + Addendum, reports, named advisories); no web.
