# Reader report — Teasley, "NASA's Rotating Detonation Rocket Engine Development" (2025)

Reviewer role: expert reader, convergence review. Metro di confronto: `reports/00_APPARATUS_BRIEF.md`
(program record state: (P)/T7, T-T3, T-T4, PB-2, EQ-v2, Λ-form/(G), Lemma B, O3.1, tier ladder, VI.1–VI.6 pipeline).

---

## 1. Citation (verified from the PDF itself)

Thomas Teasley, **"NASA's Rotating Detonation Rocket Engine Development"**, NASA Marshall Space Flight
Center, Huntsville, AL, 35808, United States. Footnote 1: "Liquid Propulsion Systems Development Engineer,
Engine Component Development and Technology Branch". 10 pages. Footer on every page: "This material is a
work of the U.S. Government and is not subject to copyright protection in the United States."

**Caveat of record on the citation:** the PDF carries **no printed venue, no paper number, no date, no DOI**.
The year 2025 is inferable only from internal evidence — references [1], [2], [7], [8] are *AIAA SciTech 2025*
papers; p. 9 states "Further investigation into reduced injector pressure loss operation will be conducted in
2025"; p. 9 states "Experimental activities conducted in FY24 have found…". The filename asserts 2025. Any
bibliography entry must therefore mark venue as **UNVERIFIED FROM SOURCE** (likely an AIAA/JANNAF-class
overview manuscript, but the PDF does not say so).

## 2. Read coverage

**10 / 10 pages read integrally, bibliography included** (single Read call, pages 1–20 requested, 10 returned;
the document ends on p. 10 with the 8-entry reference list). Nothing was skipped. Figures 5, 6, 7, 10, 11 were
read as images; Figs 5 and 6 are explicitly labelled "Representative" (Fig 5) / schematic curves with unlabeled
ordinate — i.e. **sketches, not data**, and are treated as such below. Fig 7 (thrust traces) and Fig 10
(PSD/spectrogram) carry real axes and are treated as data.

## 3. What the paper actually does

| Item | Content |
|---|---|
| **Problem** | Technology-maturation status report for the RDRE at NASA MSFC: reduce risk for industry adoption, identify "key design and operability requirements", set up a Technology Demonstration Mission (TDM) with a methane/oxygen single-shaft turbopump and a **10,000 lbf** thrust chamber assembly (abstract, p. 1; §II, p. 2). |
| **Formulation** | **No mathematical formulation whatsoever. The paper contains zero equations.** The organizing structure is a decomposition into four *critical technology elements* (CTEs, Fig 2, p. 3): CTE-1 thrust chamber/cooling, CTE-2 injector, **CTE-3 nozzle extension**, CTE-4 turbopump — plus a four-heading experimental matrix (p. 5): (1) thrust class & scalability; (2) propellant & conditioning; (3) annulus geometry (wall contouring, gap width, area contraction, L\*/L′); (4) injection parameters. |
| **Unknowns** | Empirical, not mathematical: wave mode count vs. pressure/propellant, wall heat flux, Isp, scaling relations to higher thrust class, manufacturability limits. |
| **Constraints** | Manufacturing and materials dominate: L-PBF build-box capacity, DED as fallback "should the nozzle extension exceed a specific build capacity" (p. 4), alloys GRCop-42 / GRX-810 / NASA HR-1 / Inconel 625, chemical-mechanical polishing (CMP) of coolant channels, abrasive polishing of hot walls, thermal survivability, vibratory loads, cost/schedule/TRL. |
| **Flow model** | None written down. Detonative combustion in an annular chamber, described qualitatively. Diagnostics: microphone PSD (peaks at 8.25 kHz and 16.665 kHz, Fig 10), spectrogram, high-speed video, load cells, calorimeters (refs [7], [8]). |
| **Solver** | None. "Computational approaches" are invoked twice in the abstract and §II with no method, code, discretization, or turbulence/chemistry model named. |
| **Verification** | Hot-fire testing on two platforms — MARLEN subscale and SWORDFISH full-scale 10K lbf (Fig 4, p. 5). No code verification, no grid study, no uncertainty quantification. Figs 5 and 6 (scaling uncertainty, manufacturability confidence vs. thrust class) are declaredly representative sketches. |

**Proved vs. asserted.** The paper *shows data* for: single-wave vs. 2-wave thrust traces (Fig 7), detonation at
1250 psia with two strong modes in PSD and high-speed video (Figs 9, 10), hardware damage under single-wave
operation (Fig 8). Everything else is **asserted**: "many staggering performance advantages demonstrated to
date over the state-of-the-art" (abstract) — no SOA comparison appears in the paper; "~80+% of the theoretical
performance potential" (p. 2) — "theoretical performance potential" is never defined; "Reduced length nozzles
were tested with no noticeable reduction in overall performance" (p. 10) — **no Isp number, no uncertainty
band, no test-point list** accompanies this sentence.

## 4. Hypotheses (declared and undeclared-but-necessary)

Declared: essentially none — the paper states no hypothesis set.

Undeclared but load-bearing:

1. **Nozzle/chamber separability**: the nozzle extension is a *downstream subcomponent* whose design is
   fully parameterized by four scalars (length, exit half angle, inlet half angle, exit diameter, p. 9);
   the detonation-wave structure upstream is not part of the nozzle design problem.
2. **Manufacturing precedence**: build-box, alloy and post-processing constraints are treated as binding and
   prior to gas-dynamic optimality (CTE-3, pp. 3–4; CTE-2 orifice pre-undersizing so CMP "opens up" the area).
3. **Ground load-cell force is a valid thrust proxy**, including in strongly unsteady single-wave operation.
4. **Test-point mode definiteness**: an operating point has a well-defined wave mode (1-wave, 2-wave), stable
   enough over a 30 s burn to be labelled — Fig 7's traces are labelled by mode over the whole run.
5. **Smooth, monotone scalability** of the validated relations between the 100 lbf and 10,000 lbf classes to
   25,000 and 500,000 lbf (Figs 5, 6) — asserted via sketched confidence bands.
6. **A well-defined ideal ceiling exists** against which "80+% of theoretical performance potential" is measured
   (p. 2); the ceiling model is never named.
7. **Near-adaptation of the nozzle-extension inflow**, implicit in the claim that truncation costs nothing
   measurable.

## 5. Findings, three levels

Legend: tags CONTAINED / GAP-CONFIRMS / THREAT / ADOPT / CORRECTION / IRRELEVANT.

### T-1 — TEORICO — GAP-CONFIRMS — claim 8 (nicchia vuota) + D2 gap G3 — confidence ALTA
NASA's own 2025 program-of-record overview contains **no nozzle-design theory of any kind**: no functional, no
optimality condition, no measure over operating states, no characteristic surface. The nozzle appears twice: as
CTE-3, a manufacturing subcomponent, and as a set of hardware specimens swept empirically.
*Evidence:* Fig 2, p. 3 (CTE map); p. 9: "These nozzles, and several others, have been investigated for variance
of length, exit half angle, inlet half angle, and exit diameter." A four-scalar hardware sweep is the entire
design methodology exhibited. Nothing here occupies the niche "variational MoC formulation + modern optimizer",
and nothing here derives optimality conditions for a shape shared across a measure-weighted family of inflow
states.

### T-2 — TEORICO — GAP-CONFIRMS — the litmap claim "nozzle = sottocomponente di manufacturing" — confidence ALTA
The claim is **verified verbatim and at the highest institutional level**. CTE-3, p. 3: *"The nozzle extension
subcomponent is comprised of a monolithic L-PBF or directed energy deposition (DED) printed hot wall and coupled
conventionally machined inlet and/ or exit manifolds. The manufacturing process will depend on the thrust class
which ultimately determines the scale of the nozzle extension."* And p. 4: *"Should the nozzle extension exceed
a specific build capacity, then DED will be the only viable production method if rapid development is desired…
GRX-810 will be a desired material for thrust classes lower than 30,000 lbf. This is predominantly driven by
build box limitations in existing L-PBF print platforms."* The **only** sizing/selection logic given for the
nozzle in the whole document is printer build volume, alloy availability, and coolant routing. The contour is
never mentioned as a designed object at CTE-3; "wall contouring" appears only under item 3a *Annulus Geometry*
(p. 5), i.e. for the chamber annulus, and again with no method.

### T-3 — TEORICO — THREAT — PB-2 / T-T4 (practical relevance of the length-capped plug problem) — confidence MEDIA
p. 9: *"Length, or truncation was among the most important parameters of interest since a major feature of
interest for RDRE is the overall benefit in reduced length."* p. 10 (Summary): *"Reduced length nozzles were
tested with no noticeable reduction in overall performance."* Combined with the programmatic bar of §II, p. 2
(*"roughly ~80+% of the theoretical performance potential… not necessarily a hard target but rather a rule of
thumb"*), this is a live threat to the *practical* framing of PB-2 and of in-class surpluses at the +0.5% scale
(claim 19): the customer's declared tolerance band is ~20% of an undefined ideal, and their measurement resolves
nothing at the level our theory optimizes.
**Two mitigations, both real and both must be carried explicitly:** (i) the statement is **unquantified** — no
Isp, no bar, no test list, no truncation percentages, so it cannot be used as data against us either; (ii) in
*form* it is exactly what T-T4 predicts on the plateau branch (F constant for l ≥ l(ξ)), so it is weak
*corroboration* of the nesting/plateau structure, not a counterexample. What it kills is the rhetorical move
"truncation is where the money is" unless we state the pressure/NPR regime where l < l(ξ_peak) binds.

### T-4 — TEORICO — THREAT — D2.3 measure hypotheses (switch phases μ-null; mode transitions outside the averaged theory) — confidence MEDIA
Our D2.3 scope note routes any phase containing a **mode transition** outside the cycle-averaged theory, and
Lemma 2 (T-O2) builds the operating measure from a monotone blowdown Pc(ξ) = P_CJ·PR^(−ξ). Teasley's data says
the **wave mode is a function of chamber pressure and propellant**, and that mode multiplicity is a *design
requirement across throttle*: p. 9, *"Hydrogen, however, yields a vastly different number of wave at low
pressure, and pure deflagration at higher pressures exceeding 250 psia CTAP or so"*; p. 7, *"future designs must
implement strategies by which multi-mode operation is achieved even at throttled conditions."* Consequence: on a
blowdown/throttle sweep — precisely the μ of Lemma 2 — wave-count changes are expected to occur **inside** the
support of μ, not on a μ-null set, and one of them (detonation → deflagration for H2/O2) leaves the detonative
model entirely. This does not falsify T-T3 (whose hypotheses H1–H4 are about the interface family, not the
chamber), but it **raises the re-verification burden of the D2.3 "switch phases are μ-null" clause from
formality to a real audit** for any imported flight-relevant measure, and it strengthens the case that the
robust CVaR/DRO layer is load-bearing rather than idle.

### T-5 — TEORICO — THREAT — T-T0 (wave-frame thrust flatness), perception-level — confidence MEDIA
Fig 7, p. 7 shows a single-wave thrust trace whose raw scatter spans roughly ±1500 lbf about a ~4500 lbf moving
average, versus a visibly tight 2-wave trace; p. 9 (Summary): *"a single wave imparts a substantial vibratory
environment on hardware, in some cases, an order of magnitude greater than the mean."* T-T0 claims that for a
single rotating mode the instantaneous thrust through **every axisymmetric surface** is constant. These two
statements are not in contradiction — the load cell measures the *mount reaction* of a structure excited by a
rotating transverse unbalance at 8.25 kHz (Fig 10), not the axial momentum flux through a fixed axisymmetric
surface; the plotted 30–105 s traces are structural response, not resolved wave-period data. But the figure is
exactly the artifact a hostile reader will place next to T-T0. **Action:** T-T0 must ship with a named
disambiguation clause ("measured stand force ≠ ∮ axial momentum flux; the rotating single-mode unbalance is a
transverse load") and the T0 flatness monitor must state which measurable it is a monitor *of*.

### T-6 — TEORICO — THREAT — claim 15 (T-GB / M1 geometry-free bound: "under choked frozen feed") — confidence MEDIA
The bound's hypothesis of a **choked feed** is not generic in NASA hardware, by design. p. 9: *"reduced injector
pressure losses well below choked condition were demonstrated with wave activity observed in ranges 700 psia to
1250 psia. These pressure losses were anywhere from 100 psid to 415 psid. There were conditions in which
injector pressure losses were so low that waves were no longer observed, however chugg or other instabilities
were not experienced."* This is a measured, deliberately-pursued operating class in which the T-GB hypothesis
fails. The bound is not wrong; its **coverage** is narrower than "any RDRE", and the litmap should carry the
100–415 psid / 700–1250 psia band as the named external datum defining the unchoked-feed regime.

### F-1 — FORMALE — CONTAINED — A_gen(c) / A_h working class — confidence ALTA
The paper's entire nozzle design space is the four-parameter family {length, exit half angle, inlet half angle,
exit diameter} (p. 9, Fig 11 shows three C-103 specimens of the family). This is a strict finite-dimensional
restriction of our A_gen(c): fixed bell topology sector, exit diameter ≡ ε constraint, length ≡ L constraint,
the two half-angles being a two-knot conical/parabolic surrogate of the spline class A_h, with the per-phase
state constraint g_sep absent and no attachment condition on Λ imposed analytically. Containment holds under:
bell sector fixed a priori; wall class restricted to two-angle conic interpolation; no measure (single design
point); no stationarity requirement. **Their "optimization" is an exhaustive hardware sweep — no multiplier, no
first integral, no transversality, no gradient.** Contained trivially and completely.

### F-2 — FORMALE — GAP-CONFIRMS — claim 1 (P2/G14, Rao = adjoint bridge) and claim 20 (novelty bounding) — confidence ALTA
**Bibliography inspection (mandatory record datum).** The reference list has exactly **8 entries**, all AIAA
conference papers from the same NASA MSFC / Purdue circle, all experimental or heat-transfer:
[1] Petty–Teasley–Hernandez-McCloskey–Goldman, SciTech 2025 (heat load trends, subscale RDRE);
[2] Teasley–Petty–Hemming–Scarborough–Heister, SciTech 2025 (kerosene/oxygen heat transfer);
[3] Martinez–Cabot–Blong–Teasley–Heister, SciTech 2024, p. 2791 (GOX/RP-1 watercooled combustor);
[4] Teasley–Protz–Larkey–Williams–Gradl, Propulsion and Energy 2021, p. 3655 (review toward design optimization
of AM RDRE **injectors**);
[5] Teasley–Fedotowsky–Gradl–Austin–Heister, SciTech 2023, p. 1873 (current state of NASA CRD cycle engines);
[6] duplicate of [4] (same title/forum/page, listed twice — an editorial defect of record);
[7] Maybee et al., SciTech 2025 (average heat flux measurements);
[8] Hernandez-McCloskey–Teasley–Petty–Reutlinger–Pineda, SciTech 2025 (calorimeter heat flux trends).

- **Classical variational nozzle line — Rao, Guderley, Hantsch, Hoffman, Kraiko, Shmyglevskii: ZERO citations.**
- **Modern adjoint line — Lions, Pironneau, Jameson, Giles, Lozano: ZERO citations.**
- The word "optimization" appears in the corpus only in the *injector* review titles [4]/[6].

The 2025 NASA state-of-the-program document is therefore **disjoint from both lines we bridge**. This is
positive evidence (query-bounded, per claim 20) that claim 1 and claim 8 survive in the applied-RDRE literature,
and it is the sharpest available demonstration that the two literatures do not meet.

### F-3 — FORMALE — ADOPT — Λ (attachment set) and the constraint vector c — confidence MEDIA
Fig 2 (p. 3) and CTE-3 (pp. 3–4) show that in real hardware the nozzle is a **separately manufactured extension
joined at a conventionally machined inlet manifold** to a chamber that already contains an inner body
(centerbody, visible in Figs 2 and 3, and named in the "Inner Body Burn Through" damage panel of Fig 8). Two
things to adopt into (P)'s constraint vector and admissible set:
1. **The inlet half angle is a real, industry-varied DOF** (p. 9) *and* a manufacturing joint. Our Λ attachment
   set should carry an explicit "extension-inlet joint" element with an angle DOF and a continuity/step
   tolerance, rather than an idealized smooth attachment — that is the parameter the customer actually turns.
2. **A build-envelope constraint belongs in c.** "Should the nozzle extension exceed a specific build capacity,
   then DED will be the only viable production method" (p. 4) is a *hard* size constraint of exactly the type
   c = (L, ε_max, …) is meant to hold, and it is thrust-class dependent. Innesto: D2.6 constraint vector c and
   the use-case interface advisory.

### A-1 — ALGORITMICO — GAP-CONFIRMS — claim 8 (empty niche) at the pipeline level — confidence ALTA
There is **no algorithm** in the paper: no discretization, no MoC, no CFD code, no optimizer, no gradient, no
certificate, no convergence criterion. The only *quantitative algorithmic rule* stated in the whole document is
a manufacturing compensation loop, CTE-2, p. 3: *"the orifices will need to be undersized from their desired
effective flow area so that when the integrated coolant channels are polished using CMP they are opened up to
their final design effective flow area."* Against the VI.1–VI.6 pipeline (data contract with stage-A audits,
implicit-custom_vjp differentiable march, O3.1 transposition identity, TR-SQP with Riesz-represented gradients,
Verdict-gated shipping), the comparison is not one of degree: the design loop for the nozzle at NASA in 2025 is
build-and-test. This is the strongest single piece of evidence in the read corpus that the algorithmic niche is
unoccupied on the *applied* side.

### A-2 — ALGORITMICO — ADOPT — VI.1 data contract provenance / use-case interface — confidence ALTA
The paper supplies a **published, citable operating box** for our CycleFamily provenance field, which is
currently synthetic. Adoptable numbers, all page-anchored:
- thrust classes of record: 100 lbf and 10,000 lbf **validated**, 25,000 and 500,000 lbf **unvalidated**
  (Figs 5, 6, p. 6); SWORDFISH = "NASAs full scale 10K lbf platform" (Fig 4 caption, p. 5);
- chamber pressures: 750 psia (Fig 1 caption, p. 2), 1250 psia for 5 s with methane/oxygen, two strong
  detonations in PSD and high-speed video (p. 7 and Fig 9, p. 8);
- wave frequencies: 8.25 kHz fundamental, 16.665 kHz second peak (Fig 10, p. 8) — i.e. a directly usable cycle
  period for the μ construction and for the St (Strouhal) bar;
- injector pressure loss band 100–415 psid over 700–1250 psia (p. 9);
- propellants of record: CH4/O2, kerosene(RP-1)/O2, H2/O2, HTP (abstract, p. 1);
- H2/O2 deflagration threshold "exceeding 250 psia CTAP or so" (p. 9).
Innesto: VI.1 provenance block and the use-case interface advisory — anchor the demonstration instance to the
10K lbf CH4/O2 SWORDFISH class at 750–1250 psia with an 8.25 kHz fundamental, so the interface data has an
external, citable envelope instead of a synthetic one.

### A-3 — ALGORITMICO — ADOPT — validated/unvalidated scaling ledger as a template — confidence MEDIA
Figs 5 and 6 (p. 6) encode a discipline we already practise informally but do not display: every scaling
relation is tagged **validated** or **unvalidated** against the thrust classes at which it was actually
measured, and the confidence interval is drawn as *widening away from validated points* — with the further
observation that confidence in manufacturability is **non-monotone** (Fig 6 peaks between 10,000 and 25,000 lbf
and collapses toward 500,000). Two things to take: (i) the presentational device — a validated/unvalidated
tag per relation, plotted against the anchor variable — is a good shape for the generality ledger and for
S-CERT's coverage claims; (ii) the substantive warning that extrapolation confidence can be **non-monotone in
the scale parameter** is exactly the failure mode our tier-ladder margin story assumes away when it treats
class refinement as monotone improvement. Caveat binding this adoption: **both figures are sketches**, Fig 5 is
labelled "Representative", neither has a quantified ordinate — adopt the *structure*, never the curves.

---

## 6. Novelty relative to HTH-1971 / Hoffman-1967

**None at the theoretical or formal level — the paper is strictly below the 1955–1971 state of the art on the
nozzle-contour question.** Guderley–Hantsch 1955, Rao 1958, Hoffman 1967 and HTH 1971 all pose and solve a
constrained variational problem with derived optimality conditions; Teasley 2025 varies four geometric scalars
on printed hardware and reports that nothing noticeable happened. The paper's genuine novelty is entirely
experimental and industrial: additively manufactured GRCop-42/GRX-810 chamber and nozzle hardware, detonation
sustained at 1250 psia (against the prior expectation that deflagration would dominate at high pressure),
quantified hardware damage attributable to single-wave operation with the resulting design rule "multi-mode even
at throttle", operation below choked injector loss without chug, and a funded TDM path to a turbopump-fed
10,000 lbf RDRE. For our program its value is as a **customer/requirements document and a niche-emptiness
witness**, not as a technical competitor.

## 7. Bibliography note (record datum, per procedure item 6)

8 references, one of them a duplicate ([4] ≡ [6]). All in-house AIAA conference papers, 2021–2025, experimental.
**Classical nozzle line (Rao / Guderley / Hantsch / Hoffman / Kraiko / Shmyglevskii): not cited — zero.**
**Modern adjoint line (Lions / Pironneau / Jameson / Giles / Lozano): not cited — zero.**
No textbook, no archival journal article, no non-AIAA source of any kind appears.
