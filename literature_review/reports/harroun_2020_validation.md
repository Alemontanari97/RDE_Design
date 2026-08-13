# Expert read — Harroun, Heister & Ruf, "Experimental Validation of Nozzle Flow Simulations for Rotating Detonation Rocket Engines"

Reader: convergence-review expert reader. Date: 2026-08-13.
File: `literature_review/harroun_2020_rde_nozzle_simulation_validation.pdf`
Why on the list: **the counter-evidence of record to design-on-the-mean.**

---

## 0. Citation (verified from the PDF itself)

Harroun, A. J. (Purdue University, School of Aeronautics and Astronautics), Heister, S. D. (Purdue),
and Ruf, J. H. (NASA Marshall Space Flight Center, ER42 Fluid Dynamics Branch),
**"Experimental Validation of Nozzle Flow Simulations for Rotating Detonation Rocket Engines,"** 12 pp.

**Bibliographic caution of record.** The PDF carries **no AIAA paper number, no forum/journal name, no
DOI, and no printed date** on the title page or in any header/footer. Its embedded metadata reads
`/Company: AIAA`, `/Title: Preparation of Papers for AIAA Journals`, `/Keywords: TP Template 2017`,
`/Author: Harroun, Alexis Joy` (scan/Paper-Capture produced 2023-06-09). The paper is therefore an
AIAA-template conference/journal manuscript whose venue **cannot be established from the document**.
Internal dating evidence: it cites [9] Lim & Humble, *AIAA SciTech Forum, Orlando, FL, Jan. 2020*, so it
is **2020 or later**; and it describes the V1.4 campaign of spring 2019 as complete. The repo filename
`harroun_2020_...` is consistent but **is not corroborated by the PDF**. Do not add a paper number or
venue to the litmap without an external check.

**Do not conflate with** `harroun_2021_computational_experimental_rdre_nozzle_performance.pdf` (the
JPP-line paper, separate file in the same folder). Program memory attributes a misquote
("near-perfect time-averaged expansion") to "Harroun JPP 2021"; **that phrase has 0 occurrences in
THIS document** (verified by full-text search), so this PDF is clean of it and cannot be used either to
support or to repair that misquote finding.

---

## 1. Read coverage

**12 / 12 pages read in full**, including the complete reference list [1]–[16] on pp. 11–12.
Everything in the document was read: title/abstract/nomenclature (p.1), Introduction (p.2),
campaign descriptions + Table 1 (p.3), Methodology/computational model + Eqs. (1)–(2) + Fig. 3 (p.4),
domain/BCs Fig. 4 + experimental set-up (p.5), instrumentation Figs. 5–6 + Results start (p.6),
base-pressure results Fig. 7 (p.7), Figs. 8–9 open/closed wake (p.8), IE-aerospike Fig. 10 + Table 2 (p.9),
Fig. 11 paired comparison (p.10), Conclusions + References (pp. 11–12).

**Not read / not readable:** nothing was skipped. Limitations are in the source, not in the reading:
(a) all quantitative results are delivered as **plots** (Figs. 7–11) — no data tables of pressures, so
values quoted below are read off figures or from the text; (b) the nozzle **geometries are not given
numerically** (only cross-section drawings, Figs. 1–2, 5–6, and station labels); (c) **thrust is never
tabulated for the V1.4 tests** (only Test #53 of V1.3, Table 1, 2.3 kN); (d) the key upstream carrier
[7] (Harroun M.S. Thesis, Purdue, July 2019) — which contains the cycle-averaged 1%-Isp result — is
**cited, not reproduced, and is UNREAD by this program**.

---

## 2. What the paper actually does

| Slot | Content |
|---|---|
| **Problem** | Forward analysis + experimental validation. Characterize the effect of downstream expansion geometry (nozzleless vs. two aerospikes) on an annular RDE, and validate a previous 3D transient CFD study against a new hot-fire campaign. **Not** a design problem, **not** an optimization problem. |
| **Formulation** | 3D unsteady RANS on a fixed geometry. No functional, no multipliers, no optimality condition, no adjoint (verified: 0 hits for "variational", "adjoint", "optimality" in full text). |
| **Unknowns** | The flow field only (URANS state) and the derived wall/base pressures. Geometry is **exogenous and fixed**: nozzleless; IE-aerospike designed by Stechmann at **NPR 13.7** [1]; flared aerospike designed with NASA **ADAPT** [10] at **design NPR 19.3**. Both are **single-design-point** contours. |
| **Constraints** | None in an optimization sense. Boundary conditions only: quiescent inlet P = 1 atm, M = 0.05 (entrainment); outlet P = 0.998 atm; far field; symmetry (Fig. 4). |
| **Flow model** | Compressible viscous turbulent; **Mentor baseline (BSL) two-equation model with the Sarkar\* compressibility correction** [14], chosen after a parametric turbulence-model study. **Frozen product species, chemical kinetics ignored**; product composition from NASA CEA [11]. Inflow: an *analytically prescribed* rotating pressure waveform, not a combustion computation — "it was decided not to model the full combustion physics of the rotating detonation wave" (p.4). Eq. (1): `P(t) = −630000 ln(t) − 5780000 [Pa]`; Eq. (2): `P(θ) = −630000 ln(θ/180 · 1/f) − 5780000 [Pa]`; bounds set by CTAP and the CEA detonation pressure ratio; two waves, f = 13800 Hz (Table 1). Waveform shown in Fig. 3 (sawtooth, capped near 30 atm, decaying to ~2 atm). |
| **Solver** | **Loci/CHEM** [13] (E. Luke, Mississippi State) — fully implicit dual-time, 2nd-order in space and time. Quadrilateral near-wall mesh + unstructured tetrahedral far field. |
| **Verification / validation** | *Verification:* "A mesh convergence study was conducted for all geometries by doubly refining an **axisymmetric** mesh" (p.5) — i.e. mesh convergence was established on the axisymmetric mesh, **not** on the 3D transient mesh whose results are the ones reported. *Validation:* 7 base pressure ports (nozzleless, radii R 0.8/1.4/1.9/2.5/3.0/3.6 cm + centerline, Fig. 5) and 6 plug-surface ports (aerospike, L 0.8/2.2/3.5/4.9/5.8/7.7 cm from throat, cowl exit at 2.5 cm, Fig. 6), against 23 nozzleless and 8 IE-aerospike hot-fire tests. Uncertainty is shown as error bars (transducers for stations 2–5 differ from 1–2/6–7, "resulting in higher uncertainties"). Cross-fluid caveat declared by the authors: computations are **methane**/O2, experiments **kerosene**/O2, justified only by "the ratio of specific heats ... is approximately the same" (p.5). |

### The four results the paper claims (Conclusions, p.11), with what is proved vs. asserted

1. **PROVED (measurement + matched-ṁ CFD control).** The RDE cycle **enhances base drag beyond constant-pressure estimation.** Fig. 7: at matched mass flow (1.24 kg/s), the *constant chamber pressure* computation gives base pressures ≈ 0.9–1.2 atm across the base radius, while the *detonation-wave* computation and all five experiments (Tests #54, 55, 65, 66, 79; ṁ 1.23–1.26 kg/s, ≤1% off the computation) collapse onto ≈ 0.55–0.65 atm. Text: "The surface-area averaged base pressures for the tests varied from **0.58 to 0.60** ..., a **1% difference from the computational result**" (p.7). Mechanism asserted (from [7], not measured here): "the changing pressure field exiting the combustor effectively acts as an **ejector**, enhancing the pumping action on the base region. This leads to increased suction force on the base region and thus **higher base drag for the RDE cycle versus constant pressure engines**" (p.7).
2. **NOT CONFIRMED (explicitly).** The computationally predicted **delay of flow separation** at the end of the ramp: "the detonation wave case showed a delay in flow separation at the end of the ramp. Similar to the ejection action seen in the nozzleless case, the constantly re-pressurizing flow of the RDE re-energized the boundary layer at the end of the ramp, which kept the flow from separating. **Unfortunately, there was not enough resolution in the experimental pressure port locations to be able to confirm this trend.**" (p.9). Conclusion 2 repeats it.
3. **ASSERTED (inference from wall pressure, not a thrust measurement).** At the tested conditions the **IE-aerospike** gives a more favourable pressure field than the flared. Fig. 11 (three paired tests, Table 2): the IE normalized surface pressures are higher over most of the ramp. The paper's own wording is inferential: "This trend **suggests** that for the pressure ratios tested, the IE-aerospike produces more pressure thrust" (p.10). **No thrust or Isp was measured for the paired tests.** The higher-NPR flared design could not be tested at its own regime "because of a significant increase in heat loading and hardware destruction" (p.10).
4. **ASSERTED.** The simplistic analytic inflow model "appears to produce results that agree well with the experiment."

### The sentence that puts this paper on our list (p.11, end of §IV.C)

> "However, previous work using **cycle-averaging of 2D axisymmetric constant pressure cases** for both the IE- and flared aerospike geometries estimated that the **flared aerospike geometry would produce 1% more specific impulse** at pressure ratios near the investigated mid-pressure ratio paired V1.4 test [7]. The discrepancy suggests that either the computation is not capturing all of the flow physics present in the experiment or that **the axisymmetric cycle-averaging is too simplistic of a method to estimating performance potential**."

and, in the closing paragraph:

> "Both the computational and experimental studies confirm that **previous aerospike literature for constant pressure engines is not sufficient for estimating the nozzle performance for RDEs**."

---

## 3. Hypotheses

**Declared:**
- H-D1 Frozen product species; chemical kinetics ignored; composition from CEA for CH4/O2 detonation.
- H-D2 The detonation is not simulated; an analytic, azimuthally rotating log-decay pressure waveform is imposed at the nozzle inlet plane (Eqs. 1–2, after Mikoshiba [12]).
- H-D3 Two-wave mode at 13.8 kHz, wave speed 88% of CJ (Table 1).
- H-D4 Methane-based computation validated with kerosene-based experiment, justified by approximately equal γ.
- H-D5 URANS closure = Mentor BSL + Sarkar\* compressibility correction, selected by parametric study.
- H-D6 Steady-state port pressures are attained within the sub-1-second hot-fire duration despite ~23 cm / ~30 cm port lengths.
- H-D7 Sea-level ambient (0.998 atm outlet), quiescent entrainment inlet.

**Necessary but NOT declared:**
- H-U1 **The inlet plane is a valid, one-way (non-reflecting-in-practice) boundary**: the imposed waveform is unaffected by the nozzle downstream. This is exactly the *upstream-influence* assumption our program handles with the L4 axially-supersonic-with-margin interface class and [T-NSW]; here it is imposed by fiat with no characteristic-completeness audit.
- H-U2 **The waveform's azimuthal profile is radially uniform and its velocity/temperature/composition companions are consistent with the pressure trace** — only P is specified in Eqs. (1)–(2); the remaining inflow state variables are never stated.
- H-U3 **Phase = azimuth**: the map t ↦ θ is a rigid rotation at constant f (Eq. 2 is Eq. 1 with t → θ/(180 f)), i.e. a pure single-mode rotating wave in the wave frame. This is our own periodic-wave data scope, adopted silently.
- H-U4 **Mesh convergence transfers from the axisymmetric mesh to the 3D transient mesh** (the study was done on the former, the results come from the latter).
- H-U5 **Port-averaged / discretized pressures are comparable to surface-area-averaged CFD** ("the base pressure ... is compared to the *discretized* pressure measurements", p.6) — the discretization/averaging rule is not given.
- H-U6 **Cross-campaign transfer**: V1.3 (methane, 2017) computations are compared to V1.4 (kerosene, 2019) experiments at 1–6% different mass flow, with the assumption that the differences are second-order.
- H-U7 **The 30-atm cap** in Fig. 3 (the log singularity at θ → 0 is truncated) is a modelling choice whose location is not stated in a formula; only "the CTAP and the detonation pressure ratio ... were used to determine the bounds".
- H-U8 **Base pressure is treated as a scalar operating-point function** (Figs. 8–9 plot a single area-averaged Pb vs. ṁ or Pa/Pc), i.e. no hysteresis / history dependence is entertained.

---

## 4. Derived numbers (MY arithmetic from their Eq. (2) — not stated in the paper)

Taking ξ = θ/180 uniform per wave (their own phase↔azimuth map) and capping at 30 atm as in Fig. 3:

| quantity | value |
|---|---|
| P(θ = 180°) | **2.22 atm** (matches Fig. 3) |
| P(θ = 90°) | 6.53 atm |
| P(θ = 45°) | 10.84 atm |
| cycle fraction with P < 5 atm | **36%** |
| cycle fraction with P < 8.6 atm (= CTAP) | **64%** |
| cycle fraction with P < 10 atm | 71% |
| cycle fraction with P > 25 atm | **2.6%** |
| ⟨P⟩ over the capped waveform, uniform in θ | **8.37 atm** vs. reported CTAP **8.6 atm** (−2.7%) |

Two consequences, both load-bearing for us:
- The last row is an **independent internal-consistency check of their waveform construction** that closes to 2.7% — good evidence the waveform is correctly transcribed in Eq. (2) and correctly read by me.
- The **measure is strongly low-pressure-weighted**: the arithmetic mean sits at the **64th percentile** of the phase distribution, while thrust weight sits in the top few percent. Inverting Eq. (2), with ξ uniform the induced pressure measure is `dμ_P ∝ exp(−(P + 5.78e6)/6.30e5) dP` — **exponential in pressure**, *not* the log-uniform `dμ_P = dPc/(Pc ln PR)` of our Lemma 2 (T-O2, exponential blowdown). This is a genuinely different, literature-anchored μ.

---

## 5. Findings

### TEORICO

**F1 — THREAT (bounded) on T-T3's applicability hypothesis H2' / on claim #4 (T-T3-MAP). Confidence ALTA.**
The paper delivers the cleanest published *controlled* comparison of "cycle physics" vs. "the same mean, steady": the constant-chamber-pressure computation is run **at the same mass flow (1.24 kg/s)** as the detonation-wave computation, i.e. it is literally the matched-ṁ steady surrogate our T-T3-MAP argues about. It **fails quantitatively** on the base: Fig. 7 constant-mass-flow curve sits at ≈ 0.9–1.2 atm while the detonation-wave curve and all five experiments sit at ≈ 0.55–0.65 atm — an error of roughly 0.35–0.5 atm, i.e. **50–100% of the measured base pressure**, and in the non-conservative direction (over-predicted Pb ⇒ under-predicted base drag). Conclusion 1, p.11: "Experiments confirmed the ejector action of the RDE cycle that enhances the base drag on the centerbody of an annular nozzleless RDE design **beyond that predicted by constant pressure estimations**."
*Scope discipline:* this does **not** falsify T-T3, which explicitly assumes **H2' (fixed wall, full-flowing, supersonic exit every phase, ambient-blind interior)** and constant Pa. A base region is by construction outside H2'. What it falsifies is any *unqualified* reading of "the cycle-optimal wall = the classical design at ⟨Pc⟩" for real RDE hardware, and it converts our T-T3-MAP breakers "Pa ≠ 0 at first order" and "subsonic patches" from adjudicated-on-paper to **measured**. **Program obligation:** every external presentation of T-T3 must ship with this counter-example named, and the H2' clause must be stated *before* the collapse statement, not after.

**F2 — GAP-CONFIRMS on T-T4 sharpness and on PB-2. Confidence ALTA.**
T-T4's declared sharpness is: "a length cap L < l(ξ_peak), **a base-pressure model**, or non-ideal adaptation break the nesting". This paper is the empirical statement of exactly that breaker, and it certifies the gap is **open in the corpus**: "Unfortunately, at present **there is no way to create an analytical model predicting the base pressure — and thus the base drag — with respect to the operating conditions**" (p.7). The one attempt in the literature (Stechmann's linear model, [8]) is shown *failing*: Fig. 8, the mid-ṁ cluster (~1.2–1.4 kg/s, Pb ≈ 0.58–0.60 atm) is on the line, but the high-ṁ points (~1.65–1.75 kg/s) measure Pb ≈ 0.60–0.76 atm against a model line falling toward ~0.4 atm — "at higher mass flow rates ... the physics in the base region changes drastically, limiting the applicability of the model."
**Consequence for PB-2:** the "first genuinely averaged shape problem" is *exactly* the problem whose closing datum (p_b in CSTR_PB) has **no accepted model in the RDE literature**. PB-2 must therefore ship its base-pressure closure as a declared conditional with a named owner and a monitor, in the same class as [C-HT4] — never as a plugged-in constant, and never as the classical constant-pressure-engine plug closure (see F7).

**F3 — THREAT (qualified) on the practical standing of J = ∫_Ξ F dμ as a design-ranking instrument. Confidence MEDIA.**
The paper reports (p.11) that *cycle-averaging of 2D axisymmetric constant-pressure cases* — structurally the same object as our J[S] = ∫_Ξ F[S; s(ξ)] dμ(ξ), evaluated by phase-wise steady solutions — predicted **flared > IE by 1% Isp** near the mid-pressure paired test, while the experiment's normalized wall pressures rank **IE > flared** over most of the ramp at all three paired conditions (Fig. 11a,b,c). The authors' own diagnosis names our method: "**the axisymmetric cycle-averaging is too simplistic of a method to estimating performance potential.**"
*Why only MEDIA, and the exact reason the threat is not decisive:* (i) the experiment **does not measure thrust or Isp** for the paired tests — the "IE produces more pressure thrust" is the authors' *inference* from surface pressure (their word: "suggests"), so no 1%-level Isp measurement exists to contradict the 1%-level computed difference; (ii) the paired tests are not at identical operating points (Table 2: CTAP 7.8 vs 7.4, 8.3 vs 8.5, 16.5 vs 15.7 atm; ṁ 1.32/1.32, 1.45/1.48, 2.77/2.79 kg/s) — a 1% Isp difference is inside that offset's plausible influence; (iii) the geometries differ in **cowl** only ("The plug geometry was shared between the IE- and flared aerospike configurations; only the cowl geometry was changed", p.6), so the disputed physics is cowl-region recompression and plume interaction, not the plug expansion our T3/T4 theory governs; (iv) the cycle-averaging in question is done over **constant-pressure axisymmetric** cases, which discards azimuthal nonuniformity entirely — a coarser surrogate than our (P), which carries per-phase interface states s(ξ) with M, θ, s profiles.
**Program obligation (binding):** this is the record instance for **PROTOCOL T3-CONTROL**. Any decisive cycle-averaged-vs-steady comparison we publish must (a) cite this discrepancy, (b) state that the rebuttal above is *our* argument and not the authors', and (c) not claim the cycle-averaged objective ranks *cowl-coupled, base-coupled, separated* configurations — that is outside its declared regime.

**F4 — ADOPT: a second literature-anchored cycle measure for the μ library. Confidence ALTA.**
Eqs. (1)–(2) with Table 1 (f = 13800 Hz, 2 waves, CTAP 8.6 atm, wave speed 88% CJ) constitute a complete, citable, reproducible cycle-family pressure law. Inverting it (§4 above) gives `dμ_P ∝ exp(−(P + 5.78e6)/6.30e5) dP` — **exponential in pressure**, structurally different from the log-uniform measure our Lemma 2 (T-O2) derives for exponential blowdown `Pc = P_CJ·PR^(−ξ)`.
**Where it plugs in:** (a) **D2.3 μ library** as measure #2 of record, with provenance "Harroun/Heister/Ruf Eq. (2), after Mikoshiba [12]" — non-synthetic, published, and used in a validated CFD study; (b) **T-T3-SI** (claim #3) gains a real second measure to run the measure-invariance falsifier against, instead of two synthetic ones; (c) the derived-number table in §4 gives the **Jensen/skew anchor** that our T-T3-MAP "Pa ≠ 0 ⇒ harmonic mean" breaker needs numerically: 64% of the cycle is below ⟨Pc⟩, only 2.6% above 25 atm. **Caveat to carry:** the 30-atm cap is a figure-read, not a formula in the paper (H-U7) — the adopted measure must declare the cap as our reconstruction.

**F5 — GAP-CONFIRMS: μ(Ξ_sub) > 0 is the generic RDE case, not a corner. Confidence ALTA.**
Our two-regime contract is declared "load-bearing" and J is declared UNDEFINED when μ(Ξ_sub) > 0. This paper supplies the physical proof that the condition bites for essentially every real RDE nozzle: instantaneous chamber pressure sweeps **≈2.2 → ≈30 atm within one cycle** (Fig. 3, Eq. 2) against a **fixed** sea-level ambient, while the tested contours are single-point designs at **NPR 13.7** (IE) and **NPR 19.3** (flared). By §4, **64% of the cycle sits below the CTAP**, i.e. the flared aerospike spends the majority of every cycle at NPR far below its 19.3 design point — deep overexpansion, with the wake and separation physics the paper measures. The measured **open-/closed-wake transition at Pa/Pc ≈ 0.15** (Fig. 9) is, in cycle terms, a **mode transition crossed within the cycle** — which our own D2.3 scope note routes *outside* the averaged theory ("a phase containing a MODE TRANSITION has no steady per-state F and is outside D2.3"). **This paper measures that our scope exclusion is triggered by ordinary RDE operation**, and therefore that the robust/CVaR layer is not optional decoration for the RDE application.

### FORMALE

**F6 — GAP-CONFIRMS: the empirical content of g_sep and CSTR_PB is unmeasured in the corpus's best attempt. Confidence ALTA.**
Our formal apparatus carries two objects whose closure we label *empirical*: the per-phase state constraint **g_sep(S; s(ξ)) ≤ 0** (separation margin, "empirical closure", holding μ-a.e.), and **p_b** in the plug corner transversality **CSTR_PB** (Rao 1961 Eq. (6) mirror). This paper is the purpose-built experiment for both, and it closes **neither**:
- separation: "the detonation wave case showed a **delay in flow separation** at the end of the ramp ... **there was not enough resolution in the experimental pressure port locations** to be able to confirm this trend" (p.9); Conclusion 2: "more resolution is required to confirm the delay of flow separation seen in the computational study" (p.11). With ramp ports only at L = 0.8/2.2/3.5/4.9/5.8/7.7 cm (Fig. 6), the separation location is not resolvable.
- base pressure: measured, but with no model (F2).
**Verdict:** our "empirical closure" honesty label on g_sep is *correct and currently irreducible* — there is no dataset in this line to calibrate it against. Any g_sep we ship is a modelling choice with a falsifier, not a validated closure.

**F7 — CORRECTION: the classical open-wake closure Pb/Pa = 1 is WRONG for RDE, by measurement. Confidence ALTA.**
The natural formal move for CSTR_PB is to import the classical truncated-plug base closure from the constant-pressure aerospike literature. This paper measures that import to be wrong in **sign**: "Literature of constant pressure aerospike engines has shown that the base pressure in open-wake mode will **directly adjust to the ambient pressure**, shown as the dotted **Pb/Pa = 1** line in Fig. 9 [15–16]. In the RDE experiments, however, we see evidence that **while the base pressure will adjust to the ambient pressure in open-wake mode, it will still be suctioned lower than the ambient pressure**, which is further evidence to support the ejection mechanism the RDE performs on the base region." (p.8). Fig. 9 shows all V1.4 points **below** the Pb/Pa = 1 dotted line, with the open-wake branch rising along a line strictly under it, and the closed-wake branch flat at Pb/Pc ≈ 0.075–0.085 for Pa/Pc ≲ 0.15.
**Action:** register in the litmap that `p_b = p_a` (and any classical constant-pressure-engine plug base closure) is **not admissible** in CSTR_PB for RDE, at either regime; the admissible structure is two-regime — *closed wake:* Pb/Pc ≈ const, ambient-independent; *open wake:* Pb increases with Pa but with Pb < Pa — with the transition at **Pa/Pc ≈ 0.15** (their number, declared by them as needing "more experiments ... to discretize this trend"). Sources [15] Mueller, Sule, Fanning, Giel & Galanga, NASA N-73-12282 (Sept. 1972) and [16] Mueller, Sule & Hall, NASA N-71-18990 (Jan.) are the classical carriers and should be procured before PB-2 is executed.

**F8 — GAP-CONFIRMS on claims #7 (gap G3) and #8 (empty niche), via the bibliography. Confidence ALTA.**
The paper contains **no functional, no Lagrangian, no multiplier, no optimality condition, no adjoint, no optimizer** (full-text search: 0 hits for "variational", "adjoint", "optimality", "Lagrang"; "optim" appears only in the informal senses "how their geometries could be optimized", p.2, and "at the optimal NPR", Fig. 2 caption). It is a pure forward-analysis + validation study on **exogenous, single-design-point** contours. It therefore **cannot** precede or occupy claims #1, #6, #7 or #8, and its bibliography (§6 below) shows the RDE-nozzle experimental line and the variational-nozzle line are **bibliographically disjoint** — the strongest kind of evidence for the empty-niche claim short of a citation-graph sweep.

### ALGORITMICO

**F9 — GAP-CONFIRMS: the CFD route cannot afford even a second geometry, let alone a design loop. Confidence ALTA.**
"It should be noted that the computational study did not investigate the flared aerospike geometry beyond **2D axisymmetric** cases because of the **long computation times associated with the full 3D transient boundary condition**." (p.10). And: only "the results of the full three-dimensional computations with the temporal and spatially evolving inflow boundary condition are considered" (p.5) — i.e. the expensive case is the *only* physically representative one, and it was affordable for exactly one geometry.
This is the price tag of the incumbent method, from a NASA-MSFC-co-authored study with a production implicit solver: **one 3D-transient geometry evaluation per study**. It (a) prices the empty niche of claim #8 — a shape-optimization loop is simply out of reach on this route; (b) independently justifies the program's MoC-per-phase + discrete-adjoint architecture and the S25/S25-bis speed program (segment record 100.84 s → 5.58 s); (c) explains *why* the field ranks geometries with the cheap surrogate whose failure F3 documents — the surrogate is not a preference, it is the only affordable instrument. **Use this citation whenever the "why not just CFD + adjoint" question is put to the program.**

**F10 — THREAT on the sufficiency of the per-phase axisymmetric evaluator. Confidence MEDIA.**
Abstract, final sentence: "This study showed both the **strength and the necessity for 3D transient computations** to better understand the RDE flow field with nozzle geometries." Conclusions, p.11: "performing full 3D transient studies modeling the combustion physics of the detonation wave would be useful to confirm the results from the more simplistic detonation wave pressure models."
This directly contests the adequacy of any per-phase axisymmetric evaluator, ours included.
*Assessment (ours, not theirs):* the assertion is **argued from the base/wake/cowl-recompression/turbulent-boundary-layer evidence** of this paper, none of which lives in the supersonic inviscid core our MoC march resolves; the paper offers no evidence that the *core expansion* requires 3D. Our own **T-T0** (single rotating mode ⇒ instantaneous thrust constant through every axisymmetric surface, with the flatness monitor as executable falsifier) is the formal answer *for the inviscid single-mode core*, and the L4 interface class with margin is where it is claimed. The threat is therefore **real but scoped**: it stands against extending the per-phase axisymmetric evaluator into base/wake/separated regions, exactly the regions F2/F5/F6 already fence off. **Obligation:** the program must never claim the per-phase evaluator settles base-region or cowl-recompression questions, and should cite this sentence when declaring that scope boundary.

**F11 — ADOPT: an EXTERNAL, non-GENO physical validation oracle for the per-phase evaluator. Confidence MEDIA.**
Our certificate stack (VI.6) oracles O1–O5 plus [X-GENOXC] are all **internal or code-to-code**: theory-to-implementation, or repo-to-GENO. This paper offers the raw material for the program's **first physical oracle**: a published rotating-wave inflow law (Eqs. 1–2, Table 1), a published station set on a real aerospike plug (L = 0.8/2.2/3.5/4.9/5.8/7.7 cm from throat; cowl exit at 2.5 cm, Fig. 10), and both the *detonation-wave* and *constant-mass-flow* CFD wall-pressure curves plotted against three hot-fire tests (#69, 70, 77). Digitizing Fig. 10 gives a wall-pressure target our per-phase MoC march can be asked to reproduce **on the supersonic, attached portion of the ramp** (roughly the L ≈ 0.8–3.5 cm stations, where the plotted pressures are ≈ 1.7–2.9 atm and the flow is far from the base).
**Where it plugs in:** VI.6, as a new *soft-band* oracle **O6-PHYS**, ranked below O1–O5 (which are exact-identity oracles) and shipped with its limitations in the Verdict.
**Limitations that must ride with it, non-negotiable:** the plug geometry is published only as a drawing (no coordinates) — the oracle is contour-uncertain; the data are viscous and turbulent while our march is inviscid; the CFD is methane and the tests kerosene; the tolerance band would have to be derived from the plotted error bars, which the authors themselves flag as heterogeneous ("the pressure transducers used for stations 2–5 were different than those for 1–2 and 6, resulting in higher uncertainty", p.9). This is an oracle for *gross* fidelity (tens of percent), never for the 1e-9-class agreements our internal oracles report.

**F12 — CORRECTION: three litmap hygiene items. Confidence ALTA.**
(i) **Unit inconsistency in the headline number.** The text on p.7 reads "The surface-area averaged base pressures for the tests varied from **0.58 to 0.60 psia**", but every figure axis is in **atm** (Fig. 7 "Surface Pressure [atm]", Fig. 8 "Base Pressure [atm]"), the plotted data lie at ≈ 0.58–0.60 on those axes, and the nomenclature (p.1) defines P, Pa, Pb, Pc all in **[atm]**. 0.58 psia ≈ 0.039 atm, which contradicts Figs. 7–8 by a factor ~15. The unit in that sentence is **a typo for atm**; the program must quote **"0.58–0.60 atm"** and never propagate "psia".
(ii) **Do not conflate the two Harroun papers.** This is the AIAA-template conference manuscript (12 pp., unnumbered — see §0); the JPP-line paper is the separate file `harroun_2021_...`. The program's misquote finding of record ("near-perfect time-averaged expansion") is attached to the 2021 paper; the phrase has **0 occurrences here**, so this document neither supports nor repairs it.
(iii) **New named blind spot for claim #20.** Reference **[7] Harroun, A. J., "Investigation of Nozzle Performance for Rotating Detonation Rocket Engines," M.S. Thesis, Purdue University, July 2019** is the actual carrier of the cycle-averaged 2D-axisymmetric constant-pressure comparison and of the 1%-Isp flared-vs-IE estimate that F3 turns on. We have only the one-sentence report of it. It is the nearest prior art to *cycle-averaged RDE nozzle evaluation* found so far and it is **UNREAD** — add to the blind-spot list beside ISABE-2003-117 / Bogdanov 2002. Also unread and worth procuring for PB-2: **[15] NASA N-73-12282** and **[16] NASA N-71-18990** (Mueller et al., truncated plug nozzle flow fields / separated flow regions in altitude-compensating nozzles) and **[2] Stechmann, Heister & Harroun, JSR** (the 0-D RDE rocket performance model quoted for the 2–5% generic-aerospike benefit).

---

## 6. Bibliography inspection (record datum)

References [1]–[16], read in full on pp. 11–12.

**Classical variational nozzle line — ABSENT, completely.**
No **Rao**, no **Guderley**, no **Hantsch**, no **Hoffman**, no **Kraiko**, no **Shmyglevskii**, no
Nikol'skii, no Sirazetdinov, no Scofield–Hoffman, no Rao–Beck. (Verified by full-text search: 0 hits for
each surname across all 12 pages, and by direct reading of the reference list.) The only nozzle-design
sources are **engineering/design-practice**, not variational:
- [3] Onofri, "Plug Nozzles: Summary of Flow Features and Engine Performance," AIAA 2002-584.
- [4] Hagemann, Immich & Terhardt, "Flow Phenomena in Advanced Rocket Nozzles – The Plug Nozzle," AIAA 1998-3522.
- [5] **Angelino**, "Approximate Method for Plug Nozzle Design," *AIAA Journal* Vol. 2, No. 10, 1964, pp. 1834–1835 — the *approximate simple-wave* plug method, i.e. the classical **non-variational** alternative to Rao's line.
- [10] Smith, "Final Report – Aerospike Design and Performance Tool (ADAPT)," Plumetech, 2001 — the tool that produced the flared contour.
- [15] Mueller, Sule, Fanning, Giel & Galanga, NASA N-73-12282, Sept. 1972; [16] Mueller, Sule & Hall, NASA N-71-18990 — truncated-plug flow fields and separated-flow regions.

**Modern adjoint / shape-optimization line — ABSENT, completely.**
No **Lions**, no **Pironneau**, no **Jameson**, no **Giles**, no **Lozano**, no Ulbrich, no Reuther, no
Nadarajah. Zero optimization references of any kind; zero shape-derivative references; zero
sensitivity-analysis references. The only numerics references are the solver and its verification:
[13] Luke et al., Loci/CHEM 2 user guide; [14] Roy et al., "Verification of RANS Turbulence Models in
Loci-CHEM using the Method of Manufactured Solutions," AIAA CFD 2007.

**RDE line — present and current:** [1] Lu & Braun JPP 2014 survey; [2] Stechmann, Heister & Harroun
(JSR, "not yet published" at the time); [6] Ishihara et al., AIAA 2015-0630 (conical tail, the 6–10%
thrust-over-no-nozzle datum); [7] Harroun M.S. thesis 2019; [8] Stechmann Ph.D. 2017; [9] Lim & Humble
AIAA SciTech 2020; [11] CEA; [12] Mikoshiba, Sardeshmukh & Heister, AIAA 2019-0477 (the source of the
log-decay waveform).

**Reading of record.** The RDE-nozzle *experimental/CFD* community and the *variational maximum-thrust
nozzle* corpus have **disjoint bibliographies**: the community that has the RDE data does not cite the
theory, and (from our corpus sweeps) the theory does not cite the RDE data. This is strong, independent,
bibliography-level support for **claim #7 (gap G3)** and **claim #8 (empty niche)** — the niche is not
merely unoccupied, the two literatures do not know about each other. It is also the sharpest statement of
what the program is for: it is the only artifact that would have to cite *both* lists.

---

## 7. Bottom line — exactly what our program must explain or arbitrate

1. **Explain the base-suction result, or fence it off explicitly.** The ejector/base-drag enhancement (F1)
   is a first-order, measured, cycle-specific effect that the matched-ṁ steady surrogate gets wrong by
   50–100% of the measured quantity. T-T3 survives *because* H2' excludes it. The program must state H2'
   in front of every collapse claim and cite this paper as the physical boundary marker.
2. **Arbitrate PB-2's base-pressure closure as a declared conditional.** No analytical Pb model exists
   (F2); the classical Pb/Pa = 1 open-wake import is measured wrong for RDE (F7); the admissible structure
   is two-regime with a transition near Pa/Pc ≈ 0.15 (their number, their caveat).
3. **Arbitrate the cycle-averaging ranking discrepancy (F3) before publishing any cycle-vs-steady claim.**
   The authors themselves name "axisymmetric cycle-averaging" as a candidate culprit. Our rebuttal exists
   (no thrust measured; cowl-only geometry difference; unmatched operating points; coarser surrogate) but
   it is *our* argument and must be labelled as such under PROTOCOL T3-CONTROL.
4. **Adopt the measure (F4) and the physical oracle (F11); adopt neither without their caveats.**
5. **Register the bibliographic disjointness (§6) as record evidence for claims #7 and #8, and the
   3D-transient cost datum (F9) as the price of the incumbent route.**
6. **Add [7] Harroun M.S. Thesis 2019 to the blind-spot list (F12-iii)** — it is the nearest prior art to
   cycle-averaged RDE nozzle evaluation currently known to the program, and it is unread.
