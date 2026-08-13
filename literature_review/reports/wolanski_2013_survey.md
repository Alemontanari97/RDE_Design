# Expert read — Wolański 2013, "Detonative propulsion" (PCI 34)

Reader role: convergence review, one-to-one against the program apparatus of record.
Date of read: 2026-08-13.

## Citation (verified from the PDF itself)

Piotr Wolański, *Detonative propulsion*, Proceedings of the Combustion Institute **34** (2013)
125–158. Institute of Heat Engineering, Warsaw University of Technology, Nowowiejska 21/25,
00-665 Warsaw, Poland. Available online 27 November 2012.
DOI printed on p. 125: `http://dx.doi.org/10.1016/j.proci.2012.10.005`. ISSN line: 1540-7489/$.
© 2012 Published by Elsevier Inc. on behalf of The Combustion Institute.
Keywords (p. 125): Detonation; Propulsion; Pulse detonation engine; Rotating detonation engine.

## Read coverage

34 / 34 pages read integrally (journal pp. 125–158 = PDF pp. 1–34), in two Read calls
(pp. 1–20, pp. 21–34). The reference list (176 entries, journal pp. 154–158) was read
entry by entry. Nothing was skipped. Figures were read as rendered page images; the numeric
content of raster plots (e.g. Fig. 2, Fig. 53 contour maps) is not machine-extractable and no
number was taken from them.

## What the paper actually is

- **Problem.** None in the mathematical sense. It is an invited PCI topical review of
  propulsion based on chemical detonation: history, cycle thermodynamics, and a laboratory-by-
  laboratory survey of Standing Detonation Wave Engines, Ram Accelerators (RAMAC), Pulse
  Detonation Engines (PDE) incl. PDE+turbine and PDE rocket, Rotating Detonation Engines (RDE),
  and a short note on non-chemical (nuclear/laser) detonative propulsion.
- **Formulation.** The entire mathematical content of the 34 pages is five numbered equations:
  Eq. (1) Brayton–Joule cycle efficiency, Eq. (2) Humphrey cycle efficiency, Eq. (3)
  Fickett–Jacobs cycle efficiency (all p. 126–127), and Eq. (4) `W = t_r / t_mf` with its
  reduced form Eq. (5) `W = 2 V_max / (l_cr h u_D)` defining the detonation **Wave Number**
  (p. 144). There is no functional, no variational principle, no Lagrange multiplier, no
  optimality condition, no shape derivative anywhere in the paper.
- **Unknowns.** In Eqs. (1)–(3): cycle efficiency η given pressure/volume/temperature ratios and
  γ. In Eqs. (4)–(5): the integer number of detonation heads sustainable in an annular chamber.
- **Constraints.** None posed as optimization constraints. Physical admissibility conditions are
  discussed verbally: sonic vs subsonic vs reverse injection regimes (Fig. 31, p. 141), critical
  refill volume/length `V_cr`, `l_cr` for wave survival (p. 144).
- **Flow model.** Where computation is surveyed (§3.4.2, pp. 145–148): "the two and three
  dimensional unsteady Euler equations, with an additional conservation equation for the
  reactants and a chemical source term, are used" and "transport properties such as the
  viscosity, thermal conduction, and mass diffusion are ignored in the calculations" (p. 145);
  one-step, two-step (modified Korobeinikov–Levin, p. 146) or detailed kinetics; the thin annulus
  is unrolled into 2-D with periodic boundary conditions (Fig. 43, p. 147).
- **Solver.** Not the author's own; the survey reports others' codes (commercial or "in-house",
  p. 141), grid 100–250 μm for fine structure (p. 146), GPU-accelerated runs cited [156].
- **Verification.** Qualitative: computed "soot prints" compared with compensation photographs
  (Figs. 33, 34, 44), pressure traces vs transducer records (Figs. 29, 38, 39, 51, 52, 56).
  No convergence study, no error bar, no certificate is reported by the survey itself.

## Hypotheses

Declared:
- Ideal cycle comparison at fixed initial compression ratio 5, three fuels (Table 1, p. 127).
- Inviscid, transport-free reacting Euler for CRD structure calculation (p. 145, quoted above).
- Thin-annulus periodicity for the 2-D unrolled CRD computations (Fig. 43, p. 147).
- Critical-refill argument behind the Wave Number (p. 144).

Undeclared but necessary:
- Eqs. (1)–(3) require a calorically perfect gas with a single constant γ and a closed
  thermodynamic cycle with complete heat rejection; no composition change is accounted for.
- The claim that a rotating detonation gives a usable propulsion cycle presupposes a quasi-steady
  periodic limit cycle in the chamber (implicitly assumed whenever "stable CRD" is invoked).
- The RDE nozzle statements (see below) presuppose full flowing, attached, ideally adapted
  expansion; neither ambient pressure, nor separation, nor off-design operation is modelled.
- The "very little loss ... for the rotational component" statement (p. 147) presupposes that a
  qualitative velocity-vector plot at one operating point generalizes across chamber depths and
  mixtures.

## Answers to the two questions this paper was put on the list for

**(i) Did a nozzle-design methodology for RDE exist in 2013 that our sweep missed?**
No. In 34 pages and 176 references the nozzle is never a design object. It appears only as a
hardware noun: "aerospike nozzle", "plug nozzle", "conical nozzle". The strongest statement in
the paper is a *dispensation from* nozzle design: p. 148, §3.4.3 — "Since the products from the
detonation chamber are flowing out with supersonic velocity, there is no need to apply a
converging–diverging nozzle and the aerospike nozzle can be attached directly to the detonation
chamber." The conclusions (p. 153) repeat the framing: "most effort has been focused on studies
of the application of that system to rocket propulsion, since it offers the greatest advantage of
continuous rotating detonation when coupled to an aerospike nozzle." Where nozzle quality is
implicated in measured performance it is named without method: p. 150, "The smaller values of
specific impulse are related to: very low pressure in the chamber, non-optimum design and heat
losses". The single nozzle-titled entry in the whole bibliography is [81] S. Stuessy, D.R. Wilson,
*Influence of Nozzle Geometry on Pulse Detonation Engine Performance*, AIAA Paper 97-2745, 1997 —
a PDE parametric-geometry study, not a variational contour method (unread; logged as a lead, not
as a threat).

**(ii) Does it attribute a variational/adjoint formulation to anyone?**
No — to no one, in no school. The words variational, adjoint, optimal control, Lagrange
multiplier, method of characteristics contour design do not occur. The only occurrences of
"optimization" are parametric-by-forward-simulation: p. 148, numerical CRD calculations "allow
for optimizing the geometry and fuel and oxidizer feed parameters for future propulsion systems
based on CRD"; p. 152, "Research on optimization of the chamber for different operating
conditions is now underway"; p. 134, "optimization of the volumes and dimension of the system".

## Findings

### TEORICO

**F1 — GAP-CONFIRMS (ALTA). Touches: D2-G3, empty-niche claim (claim 8), P2/G14 (claim 1).**
The 2013 state-of-the-art review of the *entire* detonative-propulsion field contains no nozzle
design methodology of any kind, and explicitly argues the nozzle away. Evidence: p. 148 §3.4.3,
"there is no need to apply a converging–diverging nozzle and the aerospike nozzle can be attached
directly to the detonation chamber"; conclusions p. 153; the bibliography note below. This is
negative evidence of the strongest available kind for a survey: the RDE community as it stood in
2012–2013 had no contour-design object at all, so our claim that the averaged-shape niche is
unoccupied is not contradicted by the field's own canonical stocktaking.

**F2 — GAP-CONFIRMS (ALTA). Touches: T-T4, PB-2, topology sectors as outputs.**
The survey documents that the field's *de facto* RDE nozzle is the plug/aerospike, chosen by
argument-from-supersonic-exit rather than by design: Fig. 50 (p. 149) shows "(a) RDRE with
aerospike nozzle (P&W), (b) RDRE with plug nozzle (MBDA)"; p. 150 records the WUT rocket where
"the cylindrical detonation chamber was directly connected to the aerospike nozzle, but in the
next test model, the CRD was initiated and run directly in the conical nozzle". This confirms
that the plug branch (T-T4 ideal-adaptation nesting, PB-2 length-capped truncation) is the
practically load-bearing branch of our program, and that nobody in this corpus poses the plug
contour — let alone the truncated plug under a length cap — as an optimization problem.

**F3 — THREAT (BASSA). Touches: T-T3-MAP swirl breaker, mean-swirl panel record (E_θ debit 3–6 %).**
The survey asserts the opposite of our swirl debit, unquantified. p. 147: "It is very important to
recognize that, although the detonation is rotational, flow of the products from the CRD chamber
is basically axial, so in RDE there will be very little loss of energy for the rotational
component of the flow." And, on the 3-D result of Fig. 47 [153]: "detonation products in the
nozzle is axial, similarly as for the 2-D calculation. This proves that despite the complicated
structure of the 3-D CRD, there will be very little loss due to the radial velocity component."
Assessment: this is an **assertion, not a demonstration** — "this proves" rests on a qualitative
3-D Schlieren/velocity visualization at one condition, with no energy accounting, no number, and
a slippage between "rotational" and "radial" within two sentences. It does not falsify our swirl
breaker, but it is a citable prior claim in a high-visibility venue that a referee may raise
against our E_θ debit. Recommended record action: carry it in the litmap as the corpus's default
belief on swirl recovery, and make sure the swirl-KE accounting of F2a is stated against it
explicitly (the burden it imposes is rhetorical, not mathematical).

**F4 — GAP-CONFIRMS (ALTA). Touches: periodic-wave data scope pin, μ/D2.3 mode-transition scope note.**
Both halves of our standing data pin are corroborated empirically. Regularity: p. 141–142, on the
compensation photographs of Fig. 33 — "It can be seen that, for the mixture parameters tested, the
structure of the rotating detonation is very regular and stable"; Fig. 38 (p. 144) is a stable
single-head trace. Mode transitions: p. 143–145 documents the "galloping rotational detonation"
regime (Fig. 39, C₂H₂–air, 75/95 mm, p₀ = 0.7 bar) with velocity fluctuating above and below C–J,
and degeneration to deflagration for further reduced parameters, organized by the Wave Number
criterion (Eqs. (4)–(5), p. 144). This is direct experimental support that D2.3's exclusion of
mode-transition phases from the averaged model addresses a **real** operating regime rather than a
hypothetical one, and that the pure-periodic-wave interface assumption is a regime restriction
that must be certified per dataset, exactly as our stage-A audits require.

### FORMALE

**F5 — GAP-CONFIRMS (ALTA). Touches: claim 1 (P2/G14), claim 8 (empty niche), claim 20 (novelty bound).**
Negative attribution datum of record: the paper's complete formal content is Eqs. (1)–(5)
(cycle efficiencies p. 126–127; Wave Number p. 144), and it attributes a variational, adjoint,
optimal-control or multiplier-field formulation to **no author, in no school**, anywhere in 34
pages of survey or 176 references. Combined with the bibliography note below (zero overlap with
either the classical variational-nozzle line or the modern adjoint line), this is a clean,
independent, high-visibility confirmation that the Rao ↔ adjoint identification is not part of the
detonative-propulsion literature's inherited toolkit as of 2012. It raises the query bound of
claims 1 and 8 by one authoritative survey; it does not make them absolute.

**F6 — IRRELEVANT (ALTA). Touches: Route A / Route B objects, T7, EQ-v2, S4/Λ-form.**
No formal object of our apparatus is engaged by this paper: no control surface, no characteristic
condition, no first integral, no transversality, no multiplier field, no tier ladder, no KKT
system. Evidence: exhaustive equation inventory above (five equations, all algebraic
thermodynamic or kinematic-bookkeeping). Recorded so that no future reader mistakes silence for
agreement.

### ALGORITMICO

**F7 — GAP-CONFIRMS (ALTA). Touches: claim 8 (empty niche), VI.5 driver, VI.3 gradient.**
The only optimization algorithm implied in the whole survey is parametric search by repeated
forward simulation: p. 148, the numerical CRD calculations "allow for optimizing the geometry and
fuel and oxidizer feed parameters for future propulsion systems based on CRD"; p. 152, "Research
on optimization of the chamber for different operating conditions is now underway"; p. 134,
"optimization of the volumes and dimension of the system to allow it to operate". No gradient, no
sensitivity, no adjoint, no shape derivative appears in any of the ~40 numerical-simulation
references (§3.4.2). The niche "keep the variational MoC formulation and swap in a modern
optimizer" is, in this corpus, not merely unoccupied — the gradient-based paradigm itself is
absent from the RDE-side computational practice being surveyed.

**F8 — ADOPT (MEDIA, PRACTICE-grade, non-load-bearing). Touches: VI.1 data contract / stage-A
provenance, periodic-wave scope pin.**
Adopt the **Wave Number** `W = t_r / t_mf`, Eq. (4) p. 144, in reduced form Eq. (5)
`W = 2 V_max / (l_cr h u_D)`, as a *provenance label* on every imported or generated CycleFamily:
W ≈ integer ⇒ the n-head periodic rotating-wave hypothesis is physically plausible; W noticeably
below 1 ⇒ galloping/decaying regime, i.e. the dataset is outside the D2.3 averaged model and must
be routed to the robust layer. Insertion point: `VI.1 CycleFamily` provenance block, alongside the
T0-flatness / harmonic-decay certificate, as a *cheap upstream sanity label*, explicitly NOT as a
certificate (it is a refill-volume heuristic with an undefined critical volume `V_cr`, and the
survey gives it no derivation). Rationale for adopting at all despite the anti-overengineering
pin: it costs one arithmetic line from data we already carry, and it names, in the field's own
vocabulary, the regime boundary our scope pin depends on — which is worth having when a combustion
referee asks why we may assume a pure periodic wave.

## Bibliography note (record datum)

176 references, journal pp. 154–158, read entry by entry.

- **Classical variational-nozzle line — ABSENT.** No Rao, no Guderley, no Hantsch, no Hoffman
  (the "Hoffman"-adjacent hits are unrelated: [151] Hishida–Fujiwara–Wolanski; there is no
  J.D. Hoffman entry), no Kraiko, no Shmyglevskii, no Nikol'skii, no Sternin, no Scofield.
- **Modern adjoint / shape-optimization line — ABSENT.** No Lions, no Pironneau, no Jameson, no
  Giles, no Ulbrich, no Lozano, no Miele.
- **What is there instead**: the detonation-physics and detonative-propulsion communities —
  Zel'dovich [1,12], Nicholls [2,5,10,23,24,114], Adamson [3,4], Voitsekhovskii–Mitrofanov–
  Topchiyan [8,9], Oppenheim [52], Schelkin [53], Hertzberg/Bruckner/Knowlen (RAMAC) [31–33,41,42],
  Kailasanath [21,44–51,91,152,167,168,175,176], Eidelman [59–66,76,82], Bussing/Hinkey/Bratkovich
  [67,68,71–74,77,83–86], Bykovskii–Zhdan–Vedernikov [117,121–128,139,140,145,149,162,163],
  Falempin/Daniau/Davidenko/Gökalp (MBDA/ICARE) [134–138,146,159–161], Hayashi/Tsuboi/Yamada/
  Fujiwara [141,144,150,166,170,171], Schwer–Kailasanath (NRL) [152,158,167], Lu–Braun–Wilson
  (UTA) [97,164,165,168,169], and the Warsaw group [14,37,38,54,116,118–120,129–133,143,156].
- **Interpretation.** The citation graph of detonative propulsion and the citation graph of
  variational nozzle design are, as of this survey, **disjoint**. That disjointness is precisely
  the structural gap our program sits in, and it is also the reason the novelty bound must stay
  query-bounded: a survey of community A cannot certify absence in community B. What it does
  certify is that community A had, in 2013, no imported design methodology from community B.

## Rigor caveats on this report

- Every quotation above is verbatim from the rendered PDF pages and carries its journal page.
- Equation numbers (1)–(5) are the paper's own; there are no others in the document.
- "This proves" (F3) is the paper's wording, flagged as an assertion, not a demonstration.
- Reference [81] (Stuessy & Wilson, nozzle geometry, PDE) and reference [16] (Back, Dowler, Varsi,
  AIAA J. 21(10) 1983 1418–1427, title not printed in the list) are **unread**; neither is claimed
  here as containing or not containing a design method.
