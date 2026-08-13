# Expert read — Teasley et al., "Current State of NASA Continuously Rotating Detonation Cycle Engine Development"

Reader: convergence-review expert reader. Date: 2026-08-13.
File: `literature_review/teasley_2023_nasa_rdre_state.pdf`
Why on the list: NASA RDRE program state. **Hunt for ANY disclosure of contour (boundary) methodology; test our claim that no published one exists.**

---

## 1. Citation (verified from the PDF)

Thomas Teasley¹, Tessa Fedotowsky², Paul Gradl³ (NASA Marshall Space Flight Center, Huntsville, AL, 35808, United States); Benjamin Austin⁴, Stephen Heister⁵ (IN Space, LLC, West Lafayette, IN, 47906 / Purdue University, West Lafayette, IN, 47906), *"Current State of NASA Continuously Rotating Detonation Cycle Engine Development"*, 24 pp., 9 references.

**CITATION HYGIENE WARNING (of record).** The title page carries **no venue string, no paper number, no date**. Author footnotes give job titles only (¹ Combustion Devices Engineer, Engine Component Development and Technology Branch; ³ Principle Engineer, Associate Fellow AIAA; ⁵ Raisbeck Professor, Purdue). Internal dating evidence: hot fire campaign "during the summer of 2022" (p.2, p.23); "follow on work funded by NASAs Space Technology Mission Directorate (STMD) during FY23-24" (p.23); newest reference is 2021. So the year is **plausibly 2023 but NOT printed in the document**. Our litmap key `teasley_2023` is a filename convention, not a verified year/venue. The venue must be completed by hand (AIAA SciTech 2023 / JANNAF are the candidates) before any citation ships. Do not cite a number we have not seen.

---

## 2. Read coverage

**24 / 24 pages read in full, bibliography included** (Read tool, `pages 1-20` then `pages 21-40` → returned 4 pages, total 24; page 24 is the reference list). Nothing unread. Limitation of the medium: the paper is heavily figure-based (31 figures, mostly photographs, IR frames and high-speed stills); figure *pixels* were read as rendered images, so quantitative reads off Fig 22, 25, 29, 30 scatter plots are approximate and are reported as such below. All numbers quoted here are from **printed text or printed tables**, never digitized off a plot.

---

## 3. What the paper actually does

| Slot | Content |
|---|---|
| **Problem** | Not a design problem. Demonstrate that an additively-manufactured (L-PBF GRCop-42/GRCop-84) 7 klbf-class annular rotating detonation rocket engine (RDRE) thrust chamber survives long-duration cryogenic hot fire and sustains continuous detonation modes; raise TRL from ~3 toward 5. |
| **Formulation** | None mathematical. **The paper contains zero equations.** It is a hardware + test-campaign status report. |
| **Unknowns** | Experimental observables: hot-fire duration, wall heat flux, combustion completeness (C\*), wave mode/count/velocity/frequency, plume structure, hardware survival. No design variables, no shape, no field unknowns. |
| **Constraints** | Facility and manufacturing constraints only (TS115 stand limits; GH2 supply ≤ ~1 lbm/s at ≤ 2700 psi, p.15; 2500 psig proof; AM minimum wall thickness / powder removal). Geometry is **fixed and given**, not constrained-optimized. |
| **Flow model** | None. No CFD, no MoC, no 1-D model, no analytical nozzle model. Plume behaviour is described qualitatively from IR imagery. |
| **Solver** | None. |
| **Verification** | Experimental instrumentation only: 100 samples/s standard channels, 100 kHz high-speed channels; four high-speed pressure ports "printed directly into the injector face" for mean chamber pressure, unsteady transducers on fuel/ox manifolds "connected to 3-foot-long sense-lines" (p.19); high-speed cameras at 150,000 fps (p.9); dual FLIR A655 + FOL89 7° lens IR videography (p.9). No code-to-data validation, no uncertainty quantification, no error bars. |

### The nozzle disclosure — the whole of it

This is the load-bearing extraction for the task. **Everything the paper says about how the nozzle contour was arrived at:**

- p.3: *"Typical rocket performance parameters were assumed to apply in the initial design phase."* — that is the complete methodology statement.
- p.4: the section promised as *"The following sections give an overview of hardware geometry and design strategy"* opens as **"A. Chamber and Injector Hardware"** and delivers only alloy chemistry, AM vendors and dimensions. "Design strategy" = *manufacturing* strategy.
- p.4, **Table 1 "Summary of Chamber Geometry"** — the entire published geometry: overall length 8.218 in; L' (injector face to throat) 2.736 in; volume to throat 17.8 in³; L\* 2.9 in; inner body diameter 5.59 in; annulus gap width G_c 0.33 in; **expansion ratio A_e/A_t = 5.0**.
- p.4-5: V1 = "an outer body, inner body, outer body nozzle, and inner body plug nozzle"; V2 = *"an inner body with coupled contoured plug nozzle and an outer body with a coupled bell type outer nozzle."* The words "contoured" and "bell type" appear with **no construction rule attached**.
- Tables 3 and 4 (pp.9-10) name the V1 plug part **"MER05419 Aerospike 30 Cone"** — i.e. the V1 spike is a **30° cone**, not a contoured spike.
- p.17: *"The throat cross sectional area is 6.137 in^2 while the exit plane at the cowl is 8.607 in^2 allowing for a slight expansion of the flow along the plug and cowl before contacting atmosphere."*
- p.4, Fig 3: the design driver is **length**: *"chamber and nozzle geometries that are approximately 40-50% shorter than the current state of art (SOA)"*, annotated "40% Length Reduction" against the NASA CP WHALE engine at identical A/A\* = 25.

There is **no contour equation, no contour table, no coordinate set, no reference to any contouring method, and no reference to any nozzle-design literature other than [9]** (Miki-Paxson-Perkins-Yungster 2020), which is cited once, for a *plume observation*, not for design (p.17: *"This has also been reported to be the case in studies such as [9] with a similar nozzle geometry."*).

### Results of record (printed numbers)

- 802 s total hot-fire duration, 18 starts; longest single burn 133 s (p.2, p.10, p.23).
- Phase 1 (LOX/GH2): 357 s at 8 starts, **no wave modes imaged** (p.10). Phase 2 (LOX/CH4, gas and liquid): 445 s at 10 starts, 193 s of that in direct liquid/liquid injection with waves imaged (p.10).
- Peak point: **622 psia mean chamber pressure, ~4171 lbf measured thrust**, V2/LOX-GCH4 (p.2, p.12); claimed *"highest operating pressure with confirmed wave modes in an RDRE based on the available literature"* (p.12).
- Wave velocities 4000-5000 ft/s across LOX/GCH4 cases (p.20); 2-5 waves; per-wave frequency ~2600-3200 Hz (Fig 30).
- Combustion completeness "90+ percentage" with L\* and L' "an order of magnitude smaller" than CP (p.2, p.23 concl. 3).
- V2 inner body burn-through at test 012 caused by **powder-clogged coolant channels**, plus substantial Alloy 718 injector-face erosion (p.11).
- Tests 026-028 (liquid/liquid): **chamber pressure ports frozen, "mean chamber pressure was not obtained"** (p.14); the 330 psia in Fig 21 and the 127/186/330 psia in Fig 24 are therefore **estimated/assumed**, as the captions state.

---

## 4. Hypotheses

### Declared
1. "Typical rocket performance parameters were assumed to apply in the initial design phase." (p.3) — the *only* declared design hypothesis.
2. Mean chamber pressure measured at the injector face is the correct total-pressure comparator against constant-pressure chambers: *"Mean chamber pressure was measured at the injector face via sense-line. This way the total pressure could be captured and directly compared to constant pressure thrust chambers"* (p.15).
3. Cycle count is an estimate: "approximately 1.5-2.5 million cycles each" (p.10).
4. Throttle points in Figs 21 and 24 are estimated/assumed after the Pc ports froze (p.14, Fig 24 caption).

### Undeclared but necessary
5. **Steady + mean-based equivalence.** The whole comparison to CP engines (C\*, Isp-adjacent statements, "completion of combustion") assumes the unsteady annulus can be characterized by a single mean Pc at the injector face. The 3-ft sense lines (p.19) low-pass and resonate at the ~3 kHz wave frequency; no transfer-function correction is described.
6. **Sea-level ambient**, un-stated, for all thrust/plume statements (MSFC TS115 open stand).
7. **C\* formula and area used** (throat area 6.137 in², total measured ṁ) are never written; the "90+%" C\* efficiency depends on an unnamed CEA-class reference and an unnamed reference MR/Pc.
8. **The 30° cone and the "contoured" plug are treated as adequate**, i.e. nozzle losses are assumed second-order relative to the hardware/durability objectives; the paper's own p.17 caveat contradicts this ("would theoretically reduce the measured Isp").
9. **Water contamination is assumed non-invalidating**: tests 026-028 leaked water into the annulus ("substantial water leak", Fig 20; plume colour changed blue → red/orange, p.15) and the wave data from those tests are nonetheless reported and interpreted (p.22).
10. **Two different area ratios coexist unreconciled**: Table 1 gives A_e/A_t = 5.0 while p.17 gives 8.607/6.137 = **1.40** (derived arithmetic, mine) for the cowl exit plane. Which surface defines ε = 5.0 (the plug tip? a virtual exit?) is never stated. The geometry is therefore **not reconstructible from the paper**.

---

## 5. Three-level comparison against the apparatus

Legend for tags as instructed: CONTAINED / GAP-CONFIRMS / THREAT / ADOPT / CORRECTION / IRRELEVANT.

### 5.1 THEORETICAL level

**F1 — GAP-CONFIRMS (ALTA) — claims 1 (P2/G14), 7 (D2-G3), 8 (empty niche).**
The NASA program-of-record paper for the flagship US RDRE effort discloses **no contour methodology whatsoever**. Evidence chain, all printed: p.3 *"Typical rocket performance parameters were assumed to apply in the initial design phase."*; the section headed as covering "design strategy" (p.4) contains only alloys, vendors and Table 1; the V1 spike is named **"Aerospike 30 Cone"** in Tables 3 and 4 (pp.9-10); the V2 plug is called *"contoured"* (p.5) with no construction rule. This is the strongest available *positive* instance of the negative claim: not a paper that omits its method for brevity, but a 24-page state-of-the-program paper whose complete geometric disclosure is a 7-row table. Our niche is confirmed occupied by nobody, in the very place where it would hurt most if it were occupied.

**F2 — GAP-CONFIRMS (ALTA) — claim 7 (D2-G3), program motivation.**
The paper **names our gap in its own words, twice**. p.17: *"These observations underline the need for a direct study on the design for detonation cycle engine nozzles."* p.23, Future Work item 4: *"Nozzle design for annular geometries in addition to the detonation cycle will need to be experimentally and computationally investigated to produce the highest possible performances and minimize losses."* This is a NASA-authored, quotable statement of need for exactly the object (P) constructs. It should become the lead external citation for the program's motivation paragraph (P-1 introduction), replacing any softer wording.

**F3 — THREAT (ALTA evidence / MEDIA impact) — D2.3 measure hypotheses, the periodic-wave scope pin, the robust layer.**
Our standing scope pin is "interface data always a pure periodic rotating wave", and D2.3 declares mode transitions **outside** the averaged theory (routed to the robust layer), with switch phases μ-null. The measured reality here is the opposite of rare: p.19 *"Several different wave modes were observed at startup ranging from 2-4 wave counter propagating modes, one through five wave co-rotating modes, and two wave slapping modes."*; p.22 *"There was a continuous transition between clockwise and counterclockwise throughout the duration of the test. Over the 9 seconds of recorded high-speed data, this transition occurred more than a dozen times."*; p.22 test 028: a 3-wave → 2-wave transition with velocity dropping 4230 → 3520 ft/s, and *"more chaotic modal transitions were occurring as more water was introduced"*. Also p.14: *"Throughout this test, 2-3 co-rotating waves were observed. There were some instances where counter propagation would occur but then transition to rotation in the opposite direction."*
Consequence for us, stated precisely: on real RDRE hardware, mode transition is a **first-order operating fact at O(1 Hz)**, not a μ-null event. This does not falsify T-T3 (which is a theorem under H1-H4 on a given cycle family), but it **caps the physical reach of any single-mode cycle family** and converts the CVaR/DRO robust layer from "idle, not absent" into a *required* layer for any hardware-facing claim. Recommended registration: a **mode-measure** ν over the mode set (n-wave co-rotating, counter-rotating, slapping) sitting above the phase measure μ, with J = ∫∫ F dμ_m dν(m); the T-T3 collapse then applies mode-by-mode and the cross-mode aggregation is a *new* averaged problem (a second, genuinely-averaged instance beside PB-2).

**F4 — THREAT / scope-cap (ALTA) — claim 2 (T-T3, hypothesis H2'), g_sep, two-regime contract.**
H2' requires fixed wall, **full-flowing, supersonic exit every phase**. On this hardware that fails over part of the operating band: p.18 *"while the flow was separated from the outer nozzle the wave rotation attached to the inner body plug nozzle could clearly be seen in the high speed. ... Once the flow attaches to the outer body nozzle, the oblique shock rotation in the plume is substantially diminished"*. Additionally, p.16 documents the shock structure migrating with mean Pc across the throttle band (test 007 at 108 / 205 / 247 psia, Fig 23), with the shock anchoring on the nozzle tip at ~150-170 psia and moving off past the tip near ~260 psia. **Caution of record:** the p.16 passage labels the low-Pc regime "under expanded" and the high-Pc regime "over expanded", which is inverted relative to standard NPR usage; the qualitative fact (shock position sweeps across the tip as Pc sweeps) is robust, the over/under labels in that paragraph should **not** be quoted by us. Net: g_sep (per-phase separation constraint, empirical closure) and the two-regime (sub/supersonic-patch) contract are **empirically load-bearing, not defensive**, and T-T3 applies only on the attached-flow segment of the throttle band.

**F5 — GAP-CONFIRMS (ALTA) — claims 5 (T-T4) and 6 (PB-2).**
T-T4's ideal-adaptation nesting is explicitly *not* the regime of this hardware, and the paper states the reason in physical terms: p.17 *"It is expected that since no cowl is intentionally redirecting the flow down the plug nozzle, there may be regions of appreciably low pressure along the nozzle. This is particularly a concern for high thrust cases and would theoretically reduce the measured Isp of the thrust chamber."* Coupled with the hard length driver (p.4, "40-50% shorter than the current state of art") and with observed tip damage (p.11, *"some burning, and pitting found at the tip of the plug nozzle after test 007"*), the physically binding instance is exactly **PB-2: a length-capped, base-pressure-carrying truncated plug**. This is external, independent confirmation that PB-2 is the *right* object of study rather than a mathematical curiosity — and that T-T4's clean result is the idealized bookend, as our own sharpness clause already says.

**F6 — GAP-CONFIRMS (MEDIA) — claim 2 (T-T3) context, not support.**
The practitioners assert an empirical decoupling: p.21 *"There also appears to be no correlation between thrust chamber performance parameters and wave performance parameters. Thus, control over wave mode operation may not be necessary or useful from a design standpoint."*, and p.23 conclusion 4: *"All wave parameters were found to be independent of mean chamber stagnation pressure and mixture ratio."* **This must not be read as evidence for T-T3.** It is an assertion on a handful of imaged points (Figs 29-30 show ~8 points), and the authors themselves qualify statistical weakness elsewhere (p.20, on V1-vs-V2 velocity: *"may not be statistically significant given the number of data points presented"*). What it *does* establish is a field fact useful to us: the community currently designs and reasons **at the mean chamber pressure with no theory linking wave structure to nozzle performance** — precisely the vacuum that (P) + T-T3 fills with a statement that has hypotheses and a falsifier.

### 5.2 FORMAL level

**F7 — GAP-CONFIRMS (ALTA) — claims 1 (P2/G14), 7 (D2-G3), 12 (E4), 16 ((\*\*')).**
The paper contains **zero equations**. There is no functional, no multiplier, no characteristic surface, no transversality condition, no measure, no adjoint — nothing that could be compared clause-by-clause with Route A (f1/f2/f3, Rao Eqs. (11)-(14)) or Route B (Hoffman 1967 Eq. (78), Kraiko's discontinuous multipliers). At the formal level the intersection with our apparatus is **empty**, and that emptiness is itself the record datum: the flagship hardware program operates entirely outside the variational nozzle formalism. Our formal claims are untouched by it and cannot be threatened by it.

**F8 — GAP-CONFIRMS with an actionable caveat (ALTA) — validation-case availability, claim 20 (novelty-bound discipline).**
Even at the level of a *geometry*, the paper is not usable: no contour coordinates, no plug half-angle beyond the part name "30 Cone", no cowl profile, and two mutually unreconciled area ratios — Table 1 gives A_e/A_t = 5.0 while p.17 gives throat 6.137 in² and cowl exit 8.607 in², i.e. **1.40** (derived arithmetic, mine, from the paper's two printed areas). Consequence to register: **this paper cannot serve as a validation case for our tool**, and the general finding is that the RDRE hardware corpus does not publish reconstructible nozzle geometry. Any "we match the state of the art" claim we might be tempted to make against NASA hardware is unavailable by construction — the litmap should carry this as an explicit *unavailability*, not as an unexplored option.

**F9 — ADOPT (MEDIA) — claim 15 (T-GB / M1 geometry-free bound): one free external sanity anchor.**
The paper prints a closed set of numbers that permits a single, coarse, *independent* test of the geometry-free bound at system level: throat area 6.137 in² (p.17), peak Pc 622 psia at the injector face and measured thrust ~4171 lbf (p.12), MR 3.74 LOX/GCH4 (Fig 1 caption; Fig 29 shows the 622 psia point near MR 3.7), sea-level ambient. Derived (my arithmetic, clearly labelled): **C_F = F/(P_c A_t) = 4171 / (622 × 6.137) = 1.093**. T-GB asserts J[S] ≤ ∫F_id dμ with F_id capped at the sonic state; a real engine at 1.09 sea-level C_F must sit strictly below the capped ideal ceiling for LOX/CH4 at ε≈5. **Where it plugs in:** the bound-ladder regression suite (VI.6, B = min of int-max / sonic-capped J_ideal / B_EK) gains one row of *hardware* provenance rather than simulation provenance — the first such row in the ladder. Caveats that must ride with it: injector-face Pc is not a nozzle-inlet stagnation pressure; the thrust is a chamber-assembly thrust including cowl and base; ε is ambiguous per F8; no uncertainty is published. It is a **loose non-violation check** (a rejector that would fire only on a gross error), and must be labelled as such — never as a validation.

### 5.3 ALGORITHMIC level

**F10 — GAP-CONFIRMS (ALTA) — claim 8 (empty-niche), claim 1 (P2/G14).**
There is no solver, no CFD, no optimizer, no gradient, no design loop anywhere in the 24 pages. The **entire 9-item bibliography** (p.24) contains exactly one computational-design item — [9] K. Miki, D. E. Paxson, D. Perkins, S. Yungster, *"RDE Nozzle Computational Design Methodology Development and Application"*, AIAA Propulsion and Energy 2020 Forum, 2020, p. 3872 — and it is cited **once, for a plume/low-pressure observation, not for design** (p.17). So even the single design-methodology paper in NASA's own reference set is used as an observational corroboration, not as a design authority. The niche "keep the variational MoC formulation and swap in a modern optimizer" is untouched; so is the weaker niche "use *any* systematic contouring method on an RDRE nozzle".

**F11 — ADOPT (MEDIA-ALTA) — CycleFamily data contract (VI.1), oracle O5, T0-flatness monitor.**
Two adoptable items, one positive and one negative.
(i) *Negative, and more important:* **no time-resolved measurement exists anywhere near the nozzle interface.** High-speed pressure transducers are on the fuel and oxygen **manifolds** through *"3-foot-long sense-lines"*, and the mean-Pc transducers are on *"4 evenly spaced ports printed directly into the injector face"* (p.19). Nothing is instrumented at the nozzle entrance. Registration for the data contract: an experimentally-sourced CycleFamily is **not obtainable from the published hardware corpus**; imported cycle families are simulation-sourced by necessity, and the T0-flatness / harmonic-decay certificate remains the only available admission monitor. This closes off, with evidence, a "just use measured interface data" alternative that a reviewer will otherwise propose.
(ii) *Positive:* the IR plume-structure sequence versus mean Pc (Fig 23: test 007 at 108, 205, 247 psia; Fig 24: test 028 at 127, 186, 330 psia; Fig 26 ignition-to-full-power sequence) is a cheap **qualitative** O5-adjacent target for the off-design plug march: our free-boundary plug solver should reproduce the *ordering* of tip-shock position with Pc across a throttle sweep. Rejector shape: a march that puts the tip shock on the wrong side of the plug tip across the whole sweep is wrong. This is a qualitative rejector only — no quantitative band is derivable from published data (see F8).

**F12 — ADOPT (ALTA) — claim 6 (PB-2), constraint priority in (P).**
The stated value proposition of the RDRE, in NASA's own framing, is **length**, not thrust: p.4 *"chamber and nozzle geometries that are approximately 40-50% shorter than the current state of art (SOA)"* with Fig 3 annotating "40% Length Reduction" at identical A/A\* = 25, and p.23 conclusion 3 *"Combustion performance, or rather completion of combustion, was found to be equivalent to a constant pressure operating thrust chamber but with L\* and L' an order of magnitude smaller."* Where it plugs in: in (P)'s constraint vector c = (L, ε_max, L_p, …), the **length constraint L (and plug length L_p) should be declared the PRIMARY, always-active constraint** for the RDE application, with an external, quotable justification, rather than one constraint among several. That, in turn, promotes **PB-2 (length-capped truncated plug) from "an interesting averaged instance" to "the application-defining instance"**, and it makes the length-multiplier λ_L a *reportable engineering marginal value* (in⁻¹ of thrust) rather than an internal bookkeeping quantity.

### Nothing tagged CONTAINED
Deliberate. The paper contains no formulation, so there is nothing whose core could be a restriction of (P). Tagging it CONTAINED would be a category error: containment (claim 18) is a statement about *formulations*, and this paper has none. Nothing tagged CORRECTION at the technical level either — the only correction the paper forces on us is bibliographic (see §1, and the `novelty_vs_1971` note below).

---

## 6. Bibliography inspection (record datum)

The reference list is on p.24 and has **exactly 9 entries**:

1. Teasley, Gradl, Garcia, Williams, Protz — "Extreme Environment Hot Fire Durability of Post Processed Additively Manufactured GRCop-Alloy Combustion Chambers", AIAA Propulsion and Energy 2021 Forum, 2021, p. 3233.
2. Teasley, Gradl, Garcia, Williams, Protz — "Hot Fire Test Durability of Post Process Polished Additively Manufactured GRCop-Alloy Combustion Chambers in LOX/Methane and LOX/Hydrogen", JANNAF, no. 0001BN, 2021.
3. Greene — Test Summary Report PJ030 (MSFC, 2020).
4. Teasley — Test Summary Report PJ062 (MSFC, 2021).
5. Teasley, Gradl — PJ116 Test Summary Report, COMET (MSFC, 2021).
6. Teasley — Test Summary Report PK129, LLAMA (MSFC, 2021).
7. Teasley — Test Summary Report PK058 & PK129, LLAMA (MSFC, 2021).
8. Unruh, Spaulding, Lineberry, Xu, Frederick — "Development of an Optically Accessible Racetrack-Type Rotating Detonation Rocket Engine", AIAA Propulsion and Energy 2020 Forum, 2020, p. 3868.
9. Miki, Paxson, Perkins, Yungster — "RDE Nozzle Computational Design Methodology Development and Application", AIAA Propulsion and Energy 2020 Forum, 2020, p. 3872.

**Classical nozzle-optimization line (Rao, Guderley, Hantsch, Hoffman, Kraiko, Shmyglevskii): ABSENT — zero citations.**
**Modern adjoint line (Lions, Pironneau, Jameson, Giles, Lozano): ABSENT — zero citations.**

Composition: 7 of 9 are the authors' own NASA/AIAA/JANNAF hardware-durability or test-summary reports; [8] is RDRE hardware; [9] is the sole nozzle-design-methodology citation in the entire document and is used for an observation, not a method. There is no citation to any detonation-cycle *thermodynamics* work either (no Wintenberger-Shepherd, no Kaemming-Paxson), no CFD, no optimization of any kind. This is a purely hardware-and-test citation graph.

---

## 7. Novelty vs the 1971 state of the art (HTH-1971 / Hoffman-1967)

**At the level of nozzle theory or contouring method: nothing. Strictly negative.** Measured against Hoffman 1967 / Scofield-Hoffman 1971 / Hoffman-Thompson-Hoffman, this 2022-2023 NASA paper contributes no formulation, no optimality condition, no numerical method, and no contour. On the contrary, the flight-relevant hardware it reports is **behind** the 1958 Rao state of the art at the geometric level: the V1 spike is a **30° cone** ("MER05419 Aerospike 30 Cone", Tables 3-4), and the V2 plug is described only as "contoured" with no method. The paper's own Future Work (item 4, p.23) requests the study that the 1958-1971 corpus would already partially answer for the steady problem, and that our (P) answers for the cycle-averaged one.

**What it does add, and it is real:** the experimental state of the art. First AM GRCop-alloy RDRE at 7 klbf class; 802 s / 18 starts; 133 s single burn; 622 psia with confirmed wave modes at ~4171 lbf; first liquid/liquid LOX/LCH4 direct-injection RDRE with clear wave activity *"the first experiment of this nature based on published available literature"* (p.8); internal multi-point CASI ignition without pre-detonator or external backlighting; direct heat-flux profiles for deflagrative and detonative modes. For our program this is **boundary-condition and motivation material** (operating envelope, throttle range, mode statistics, length driver), not competing method.

---

## 8. Net verdict for the program

1. **Our negative claim survives, strengthened.** The single most authoritative place a published RDRE contour methodology could hide — NASA MSFC's own state-of-the-program paper — has none, and asks for one twice in print. Record this as the anchor citation for D2-G3 and for the empty-niche claim.
2. **Two scope pressures, both already structurally anticipated but now empirically priced:** frequent mode transitions (F3 → mode-measure ν, robust layer required) and off-design separation across the throttle band (F4 → g_sep and the two-regime contract are load-bearing, T-T3 caps to the attached segment).
3. **One constraint-priority change (F12):** length becomes the declared primary constraint for the RDE application, promoting PB-2 to the application-defining instance, with a NASA-quotable justification.
4. **One cheap instrument addition (F9)** and **one closed-off alternative (F11i)**.
5. **One citation-hygiene defect on our side (§1):** `teasley_2023` has no printed year or venue. Fix before any citation ships; this is a G5-class human-pass item.
