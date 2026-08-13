# Expert read — Wintenberger & Shepherd 2004, AIAA 2004-1033

**Reader role:** convergence expert review, one-to-one against the record apparatus
(`00_APPARATUS_BRIEF.md`).
**Date of read:** 2026-08-13.

---

## 1. Citation (verified from the PDF itself)

E. Wintenberger and J. E. Shepherd, "Thermodynamic Analysis of Combustion Processes for
Propulsion Systems," **AIAA Paper 2004-1033**, 42nd AIAA Aerospace Sciences Meeting and
Exhibit, January 5–8, 2004, Reno, NV. Graduate Aeronautical Laboratories, California
Institute of Technology, Pasadena, CA 91125. Copyright © 2004 by California Institute of
Technology, published by AIAA with permission. 18 pages (paginated "N OF 18").
Acknowledgment: Stanford University Contract PY-1905 under Dept. of Navy Grant
N00014-02-1-0589, "Pulse Detonation Engines: Initiation, Propagation, and Performance."
No DOI printed on the paper.

## 2. Read coverage

**18 / 18 pages read in full, references page included** (single Read call, pages 1–20
requested, 18 returned = the whole document). Nothing skipped. The only content I cannot
report on is what is *inside* the cited references (e.g. Wintenberger & Shepherd refs 5 and
12, both "submitted" in 2003) and the fine numerical values that live only inside the
plotted figures (Figs. 3–5, 7, 9–12, 16–27): I read the figure captions and the axis
labels shown, and I quote only the numbers the text or captions state in words.

---

## 3. What the paper actually does

**Problem.** Adjudicate, on purely thermodynamic grounds, whether detonative combustion is
superior to deflagrative (constant-pressure, CP) or constant-volume (CV) combustion for
propulsion, in two distinct settings: (i) *steady*-flow engines, (ii) *unsteady* /
intermittent (pulsed) engines. It is a **combustion-mode adjudication paper**, not a
component-design paper.

**Formulation.**
- Closed-cycle framing: an arbitrary adiabatic process 1→4 closed by a constant-pressure
  process 4→5→1 (Fig. 1), with η_th = w/q_c (Eq. 1), w = q_in − q_out = h1 − h4 (Eq. 4),
  η_th = (h1 − h4)/q_c (Eq. 5). For a perfect gas the efficiency is written purely in terms
  of the entropy rise, η_th = 1 − (C_p T1/q_c)[exp((s4 − s1)/C_p) − 1] (Eq. 11).
- Steady branch: standard 1-D control volume across the combustion wave (Fig. 2),
  Eqs. 12–14 (mass, momentum, energy), Hugoniot Eq. 15, Rayleigh line Eq. 16, perfect-gas
  forms Eqs. 19–21, entropy rise Eq. 22. Then the paper's own construct: the split
  **s2 − s1 = Δs_min + Δs_irr** (Eq. 23), with Δs_min defined by an ideal zero-velocity
  constant-pressure combustion at the *stagnation* state (Eqs. 27–28), giving for a perfect
  gas Δs_min = C_p ln(T_t2/T_t1) (Eq. 31) and Δs_irr = −R ln(P_t2/P_t1) (Eq. 32). The
  resulting efficiency, Eq. 38, depends on the combustion mode **only through Δs_irr**, so
  the ceiling is Δs_irr = 0 → η_th < 1 − T0/T_t1, the ideal Brayton value (Eq. 39).
- The **stagnation Hugoniot** (Eqs. 40–42): the locus of solutions at fixed upstream
  *stagnation* state instead of fixed static state. Detonation solutions exist only for
  q_c/(C_p T_t1) < 1/(γ² − 1) (Eq. 42).
- Unsteady branch: the **Fickett–Jacobs (FJ) cycle** — a closed piston/cylinder system
  (Figs. 13–14), steps a–f, work terms Eqs. 43–46, net work w_net = h1 − h4 (Eqs. 48 and
  55), efficiency η_FJ = w_net/q_c (Eq. 56), one-γ closed form Eq. 57. Variant with
  isentropic precompression π_c = P_1'/P_1 (Eq. 58). Comparison against ideal Brayton
  (Eq. 59) and Humphrey (Eq. 60).

**Unknowns.** Post-wave state 2 (P2, ρ2, T2, M2) on the Hugoniot / stagnation Hugoniot; the
cycle work terms; the efficiencies η_th, η_FJ. **There is no field unknown and no geometric
unknown anywhere in the paper.**

**Constraints.** Wave conservation Eqs. 12–14; CJ tangency to select the detonation branch;
fixed q_c; fixed initial state (or fixed upstream stagnation state); complete/pressure-matched
expansion back to P1; and the *comparison basis* — either equal pre-combustion pressure
(compression ratio π_c) or equal post-combustion pressure (π'_c = P2/P1).

**Flow model.** Steady branch: 1-D, steady, inviscid, constant-area, combustion wave as a
discontinuity. Unsteady branch: **no gas dynamics at all** — a thermostatic closed system
with spatially uniform states, explicitly chosen to avoid unsteady gas dynamics (p. 9:
"The advantage of the FJ cycle is that it provides a simple conceptual framework for
handling detonations in a purely thermodynamic fashion, avoiding the complexity of unsteady
gas dynamics of realistic pulse detonation or pulsejet engines.").

**Solver.** Closed-form algebra throughout (Eqs. 19–21, 38, 40–41, 57, 59, 60) plus
chemical-equilibrium computations with **STANJAN** (ref. 18) for H2, C2H4, C3H8 and JP10
with O2 and air (Figs. 17–20, 24). No PDE solve, no mesh, no iteration of consequence, no
optimizer, no sensitivity/gradient.

**Verification.** Three internal/external checks, all of them real:
1. *Dual derivation of the same quantity*: w_net obtained (a) from the closed-system First
   Law (Eq. 48) and (b) from the detonation jump conditions in the lab frame,
   Eqs. 49–51 → 52 → 53 → 54 → 55; p. 11: "Thus, we have verified that our two treatments
   give identical results. This gives us additional confidence that the FJ physical model of
   the detonation cycle is correct".
2. *Cross-method consistency*: p. 8, the stagnation-Hugoniot CJ efficiencies "are identical
   to those predicted by flow path analysis for ideal detonation ramjets" (their ref. 5).
3. *Cross-author consistency*: p. 15, "The result of Eq. 57 … is identical to the result
   obtained by Heiser and Pratt in their thermodynamic cycle analysis of pulse detonation
   engines," with the numerical difference traced to their γ choice (1.4 for reactants vs
   1.1–1.2 for products).

**Headline results (what is PROVEN vs what is ASSERTED).**
- *Proven within the model*: Eq. 38 (efficiency monotone in Δs_irr alone at fixed stagnation
  state and fixed q_c) — algebraic consequence of Eqs. 11, 36, 37. Eq. 42 (existence window
  for steady detonation at fixed stagnation state). Eqs. 48 = 55 (FJ net work, two routes).
  Eq. 57 (one-γ FJ efficiency).
- *Asserted / conjectured*: the identification of Δs_min with the ideal stagnation-state CP
  combustion is called a conjecture by the authors themselves — footnote, p. 5: "This
  conjecture is easy to demonstrate for a perfect gas with an effective heat addition model
  of combustion … We also demonstrate the correctness of this idea explicitly in subsequent
  computations". So it is demonstrated in-model and by example, not proven in general.
- *Bound claim* (the reason this paper is in our list), p. 11: "Since all processes other
  than the detonation are ideal, the work computed is an upper bound to what can be obtained
  by any cyclic process using a propagating detonation for the combustion step."
- *Basis-dependence of the verdict*: at equal pre-combustion pressure FJ > Humphrey >
  Brayton (Fig. 26); at equal post-combustion pressure the ordering **inverts**, Brayton >
  Humphrey > FJ (Fig. 27, and p. 17: "the trend is inverted and the Brayton cycle yields the
  highest efficiency").
- *Self-declared limitation on translating to thrust*, p. 2: "However, for unsteady flow,
  the thrust calculation with the cycle approach requires the explicit computation of
  efficiency for the unsteady cycle and the knowledge of another parameter, called the
  efficiency of non-uniformity by Foa." And p. 17: "We cannot use these efficiencies
  directly since performance estimates based on Eq. 8 are applicable only to steady
  propulsion systems."
- A genuine correction they make of the classic source, p. 10: "Fickett and Davis (p. 35–38)
  do not account for the work interaction during the process 4–1 in their definition of the
  net work," with the consequence (footnote ‡, p. 10) that their own earlier numbers in
  Cooper & Shepherd 2002 differ from those given here.

---

## 4. Hypotheses

### Declared
- H-a. Adiabatic combustion; ambient corresponds to the thermodynamic standard state (p. 2).
- H-b. s5 = s1, "approximately satisfied for real mixtures and exactly so for the simple
  model discussed later in this paper" (p. 3).
- H-c. Steady, 1-D, inviscid, constant-area control volume across the wave (p. 3, Eqs. 12–14).
- H-d. Perfect gas with **equal specific heat capacities for reactants and products**
  (p. 4, "We will assume equal specific heat capacities for reactants and products", Eq. 17)
  = the one-γ detonation model (ref. 17).
- H-e. CJ selection for the detonation branch; strong detonations only with an effective
  piston; weak detonations and strong deflagrations excluded (p. 4).
- H-f. FJ closed system: fixed mass, "All confining materials are assumed to be rigid,
  massless, and do not conduct heat" (p. 9); pistons independently movable.
- H-g. Detonation initiated *instantaneously* at the piston surface; the right piston
  *instantaneously* accelerates to u_p; the products behind the wave are in a **uniform
  state** (p. 9).
- H-h. Isentropic expansion 3→4 to the initial pressure P1; constant-pressure cooling 4→5;
  conversion of products back to reactants at constant T and P (step f).
- H-i. In the ideal-engine comparison, "Losses associated with shock waves, friction, mixing,
  or heat transfer are neglected, and the compression and expansion processes are assumed to
  be isentropic" (p. 8).
- H-j. Equilibrium thermochemistry (STANJAN) for the realistic-property results; "all
  chemical states involving combustion products are assumed to be in equilibrium" (p. 12).

### Not declared but necessary
- H-k. The detonation is a **zero-thickness discontinuity**: no reaction-zone structure, no
  front curvature, no cellular instability, no velocity deficit; U_CJ is constant over the
  whole tube length L (used implicitly in w12 = −P2 u_p (t2 − t1) A with t2 − t1 = L/U_CJ,
  p. 10).
- H-l. **Frictionless, massless pistons and no wall heat loss** — stated for the confinement
  but the piston work bookkeeping also requires no dissipation at the seals.
- H-m. Step f ("conversion of products back to reactants at constant T and P") is a
  **fictitious reversible chemical restoration** whose entire energy accounting is absorbed
  into q_c via a standard-state / Hess-law consistency assumption. Nothing in the paper
  bounds its irreversibility; it is a bookkeeping device, and the "upper bound" claim
  inherits it.
- H-n. **Two mutually inconsistent chemistry closures are used interchangeably**: the one-γ
  model (H-d) is a frozen, constant-γ closure, while the STANJAN results assume shifting
  equilibrium with partial recombination during 3→4 (discussed p. 13). The paper compares
  the two but never states that the analytic bound (Eq. 57) and the tabulated bound (Fig. 24)
  are bounds *of different objects*.
- H-o. Complete combustion to a well-defined product state (needed for "state 5 is fixed",
  p. 3).
- H-p. Pressure-matched, fully expanded exhaust with **no exit non-uniformity, no divergence
  loss, no swirl** — i.e. the nozzle is assumed perfect and is never modelled. This is the
  hypothesis that decides the entire relationship of this paper to our program.
- H-q. For Eq. 8 / Eq. 7 (thrust from efficiency) the mass and momentum contributions of the
  fuel are negligible (stated on p. 2 for the steady open/closed equivalence) — carried
  silently into all thrust talk.

---

## 5. Findings — three-level comparison with the record apparatus

### TEORICO

**F1 — GAP-CONFIRMS (ALTA). The FJ/thermodynamic bound is shape-blind, hence structurally
incapable of falsifying a shape-gain claim; the authors say so themselves.**
Touches: T-T3, T-T4, and the reason-for-listing question.
The FJ bound η_FJ = (h1 − h4)/q_c (Eq. 56) is a functional of the *thermodynamic path*
(1 → 2,3 → 4 → 5 → 1) only. No geometric variable appears in Eqs. 43–58; the expansion 3→4
is stipulated isentropic to P1 (H-h, H-p), which is the *perfect-nozzle* idealization. Its
first variation with respect to the contour Σ is therefore identically zero, so it cannot
enter, perturb, or contradict T7(a)/(b)/(c), T-T3's pointwise collapse
J[Σ] = F[Σ; ⟨Pc⟩_μ], or T-T4's nesting/peak-design argument — all of which are statements
about **argmax over Σ at fixed interface data**. Formally: a shape-independent scalar B can
falsify a claim of the form "J[Σ*] = X" when X > B, but never a claim of the form
"J[Σ_a] − J[Σ_b] = Δ > 0" when both lie under B.
The paper's own admission is the decisive evidence, and it is explicit twice: p. 2, "for
unsteady flow, the thrust calculation with the cycle approach requires the explicit
computation of efficiency for the unsteady cycle and the knowledge of another parameter,
called the efficiency of non-uniformity by Foa. These calculations require detailed
experimental measurements, unsteady analytical models, or numerical simulations."; and
p. 17, "We cannot use these efficiencies directly since performance estimates based on
Eq. 8 are applicable only to steady propulsion systems."
**Verdict on the listing question: compatible with T-T3/T-T4, and living at a strictly
different level. NO THREAT.**

**F2 — CORRECTION (ALTA). The litmap positioning "western cousin of the Kraiko–Egoryan
instantaneously-adapted bound" is wrong and should be re-worded.**
Touches: the bound ladder B = min(int-max, sonic-capped J_ideal, B_EK).
B_EK is a *flow/nozzle* bound: at a given chamber state it caps thrust by the
instantaneously-adapted expansion, i.e. it prices the **expansion**. FJ is a *closed-system
work* bound over the whole cycle that prices the **combustion mode** (its entire content is
the entropy generated at the wave, Eqs. 23, 32, 38) and then *assumes* a perfect expansion
(H-h/H-p). They are not the same rung and not competitors: FJ sits strictly upstream of
B_EK, and — unlike B_EK — it does not cap thrust at all without the Foa non-uniformity
conversion (p. 2, p. 17). Anyone reading the current one-liner would expect a rival
instantaneously-adapted thrust bound and would not find one in this paper.

**F3 — ADOPT (MEDIA). Candidate new rung B_FJ in the bound ladder, admissible only as a
declared non-tight upstream ceiling.**
Touches: T-GB/M1 and the δ = B − J[Σ*] globality gap.
Eq. 56/57 give a closed-form, geometry-free, *unsteady-legal* ceiling on the mechanical work
per unit mass extractable from a detonation, with the authors' bound statement on p. 11
("the work computed is an upper bound to what can be obtained by any cyclic process using a
propagating detonation for the combustion step"). Our current ladder rungs are all
steady-per-phase objects (int-max, sonic-capped J_ideal, B_EK); B_FJ is the only rung on
offer that is valid *across* the unsteady cycle without invoking the per-phase quasi-steady
reduction. Innesto: VI.6 bound ladder, as a **sanity rung**, with two mandatory tags —
(i) it is a work bound, not a thrust bound, and the conversion is UNDISCHARGED (Foa
non-uniformity, p. 2), so it may never be used to compute δ; (ii) it inherits H-m (the
fictitious reversible step f), so it is not a certified bound even for work. Expect it to be
very loose (their η_FJ ≈ 0.2–0.3 without precompression, Figs. 17–20).

**F4 — ADOPT (ALTA). The Fig. 26 / Fig. 27 inversion is a citable independent precedent for
the T-T3-MAP "conventions/matching" clause and for T3-CONTROL.**
Touches: T-T3-MAP (claim 4), PROTOCOL T3-CONTROL.
Same cycles, same thermochemistry, *opposite* ranking depending on whether the comparison is
made at equal pre-combustion pressure (Fig. 26: FJ > Humphrey > Brayton) or equal
post-combustion pressure (Fig. 27, p. 17: "the trend is inverted and the Brayton cycle
yields the highest efficiency"). This is exactly the structure of our matched-ṁ vs
matched-⟨p⟩ degeneracy, arrived at independently in the thermodynamic school. Innesto: cite
in the T-T3-MAP conventions clause and add to T3-CONTROL the requirement that **both**
matching bases be reported whenever a cycle-averaged-vs-steady comparison is decisive — with
this paper as the precedent showing that reporting only one basis can invert a published
verdict.

### FORMALE

**F5 — GAP-CONFIRMS (ALTA). Zero variational structure: no functional over a shape class, no
multiplier, no transversality, no free endpoint anywhere in 18 pages.**
Touches: D2-G3 (claim 7), empty-niche (claim 8), containment (claim 18).
The only "optimality" statement in the paper is proven **by construction** — all non-detonation
processes are stipulated ideal (p. 11) — not by a stationarity argument. There is no
admissible set, no first variation, no adjoint. Consequently: (a) this paper is *not* a
counterexample to the containment claim 18, because it is not a variational maximum-thrust
formulation at all; (b) it positively confirms G3 — the thermodynamic school that owns the
detonation-cycle bound never poses a shape problem, let alone a measure-weighted family of
inflow states; (c) it confirms the empty-niche claim at the level of "nobody in this school
is optimizing a contour."

**F6 — ADOPT (MEDIA). The Δs_min / Δs_irr decomposition at the stagnation state is a missing
audit in our interface contract — as a PRACTICE-grade diagnostic, matching the authors' own
rigor class.**
Touches: VI.1 stage-A audits (CycleFamily), and the bound ladder of F3.
Eq. 23 splits the measured entropy rise into a reversible part fixed by q_c and the
stagnation state (Eq. 31, Δs_min = C_p ln(T_t2/T_t1)) and an irreversible part read directly
off the total-pressure loss (Eq. 32, Δs_irr = −R ln(P_t2/P_t1)); Eq. 38 then makes the
attainable efficiency a monotone function of Δs_irr alone. Our CycleFamily contract audits
kinematics and compatibility (characteristic completeness, Crocco residual, spacelikeness,
T0 flatness) but carries **no entropy-budget audit** of the imported interface data. Adding
per-phase (Δs_min, Δs_irr)(ξ) computed from the provenance data would (i) flag interface
families whose irreversibility is inconsistent with their claimed q_c, and (ii) supply the
per-phase input needed for the B_FJ rung of F3.
Rigor cap, taken from the paper: the Δs_min prescription is called a **conjecture** by the
authors (footnote, p. 5) and is demonstrated only for a perfect gas with an effective
heat-addition model plus by example. So it enters our documents as PRACTICE, never as
THEOREM, and never as a certified bound.

**F7 — GAP-CONFIRMS (ALTA). Independent corroboration that the frozen/equilibrium and
γ-choice sensitivities we price are first-order, not second-order, effects.**
Touches: P1 scope pin + [T-EQBR] frozen/equilibrium bracket (+6.3..+7.0%); E4 / the standing
γ-variable directive.
Two anchored statements. (i) Chemistry: p. 13, "The results are significantly influenced by
the variation of the specific heat capacity with temperature in the detonation products and
the dissociation and recombination processes"; the mechanism given (products at state 4 "are
still in a partially dissociated state and a significant part of the energy released by the
detonation is not available for work") is the same physics our [T-EQBR] bracket prices, and
it *reverses* an ordering (fuel-air beats fuel-oxygen near stoichiometry, Fig. 19). (ii) γ:
p. 15, "the value chosen for the specific heat ratio has a strong influence on the results
obtained for the thermal efficiency in the one-γ model" — Heiser & Pratt's γ = 1.4 vs their
1.1–1.2 changes the numbers materially at identical formulae. Both support our refusal to
let γ = const be load-bearing and our insistence that the frozen ceiling be bracketed rather
than quoted. Note the honest asymmetry: this is corroboration of *magnitude*, in a
zero-dimensional cycle, not evidence about our nozzle-flow numbers.

### ALGORITMICO

**F8 — GAP-CONFIRMS (ALTA). The unsteady gas dynamics our per-phase evaluator resolves is
exactly what this paper deliberately deletes — so there is no algorithmic precedence and no
competing pipeline.**
Touches: VI.2 per-phase evaluator, D2-G3, empty-niche.
p. 9, explicit: the FJ cycle's stated *advantage* is "handling detonations in a purely
thermodynamic fashion, avoiding the complexity of unsteady gas dynamics of realistic pulse
detonation or pulsejet engines." Uniform post-wave states (p. 9), no spatial coordinate in
the unsteady analysis, no wave-frame, no characteristics. The paper is therefore silent on
every algorithmic object of our pipeline (MoC march, fitted fronts, adjoint sweep, cycle
quadrature with switch-phase panel splitting, driver). Their computational stack is STANJAN
equilibrium (ref. 18) plus closed-form algebra — superseded for us by the standing
Cantera-as-sole-table-generator pin; nothing there to adopt.

**F9 — ADOPT (MEDIA). Eq. 57 is a cheap, published, closed-form known-answer test, and the
Eq. 48 = Eq. 55 dual derivation is a literature instance of our dual-proof standard.**
Touches: VI.6 oracle stack, claim-dual-proof directive, and the B_FJ rung of F3.
(i) If B_FJ is admitted (F3), it must ship with a KAT: Eq. 57,
η_FJ = 1 − (C_p T1/q_c)[ (1/M_CJ²)((1 + γM_CJ²)/(1 + γ))^((γ+1)/γ) − 1 ], is a fully
specified one-γ closed form, reproducible to roundoff and *independently reproduced in the
literature* (Heiser & Pratt, p. 15) — an oracle of the same grade as our Scofield–Hoffman
Table 2 Case 1 rung. (ii) Method precedent: the same w_net obtained twice by structurally
different routes (closed-system First Law, Eq. 48, vs lab-frame jump conditions
Eqs. 49–55) and declared verified only on their agreement (p. 11). This is our B1/B2
dual-route discipline appearing in a 2004 thermodynamics paper; worth one citation in the
claim-dual-proof directive as evidence the standard is not idiosyncratic. Low weight: no
rejector, no tolerance, no seeded corruption — the agreement is exact-algebraic, so it is a
consistency proof, not a falsifiable numerical gate.

---

## 6. Bibliography inspection (data of record)

21 references, read in full on p. 18.

**Classical nozzle-contouring line — ENTIRELY ABSENT.** No Rao, no Guderley, no Hantsch, no
Hoffman, no Kraiko, no Shmyglevskii, no Nikol'skii, no Sternin, no Scofield, no Rao–Beck. No
Kraiko–Egoryan. The only Russian-language reference in the whole paper is Zel'dovich 1940
("On the Use of Detonative Combustion in Power Engineering," *J. Technical Physics* 10(17),
1453–1461, in Russian, ref. 15), cited for cycle priority over Jacobs, with the telling
remark on p. 9 that "until recently, there was no appreciation in the West of this work by
Zel'dovich."

**Modern adjoint / shape-optimization line — ENTIRELY ABSENT.** No Lions, no Pironneau, no
Jameson, no Giles, no Ulbrich, no Lozano, no Nadarajah. No optimization reference of any
kind.

**Only nozzle-adjacent reference:** ref. 16, Cooper, M. and Shepherd, J. E., "The Effect of
Nozzles and Extensions on Detonation Tube Performance," AIAA 2002-3628 — cited (footnote ‡,
p. 10) not for nozzle design but to flag that its FJ-availability convention differs from
this paper's.

**What the reference list *is*:** the detonation-thermodynamics / PDE-performance corpus —
Fickett & Davis (13), Jacobs NAVORD 4366 (14), Zel'dovich (15), Courant & Friedrichs (2),
Thompson (17), Reynolds/STANJAN (18) — plus the propulsion-cycle corpus — Foa (1, 9),
Oates (8), Heiser & Pratt (19), Wu–Ma–Yang (11), Bussing & Pappas (20), Talley & Coy (21),
Kailasanath (10), Clarke & Horlock (6), Riggins et al. (7) — plus the steady-detonation-ramjet
line Dunlap (3), Sargent & Gross (4) and the authors' own submitted papers (5, 12).

**Interpretation for our novelty bookkeeping:** this is a clean, high-quality *disjoint
corpus*. It shares no reference with the variational-nozzle corpus of our litmap. That
disjointness is itself the evidence for F5/F8: the thermodynamic-bound school and the
contouring school do not read each other, which is precisely the condition under which our
D2-G3 gap and the empty-niche claim survive. It is also a caution: the citation-graph sweep
named in claim 20 will not reach this paper from Rao 1958 or Hoffman 1967, so papers of this
class must be found by topic, not by forward citation.

---

## 7. Bottom line for the listing question

*Their bound is compatible with T-T3/T-T4, and it lives at a different level.* It is a
shape-independent, closed-system **work** ceiling that prices the combustion mode under a
stipulated perfect expansion; it has zero variation with respect to the contour and
therefore cannot falsify any claim of *shape* gain. It could, in principle, falsify an
absolute magnitude claim ("this cycle yields J = X") — but not even that today, because the
authors state twice (p. 2, p. 17) that their efficiencies do not translate into thrust
without Foa's non-uniformity efficiency, which they do not compute. The actionable residue
is three items: re-word the litmap positioning (F2), consider B_FJ as a declared non-tight
upstream rung with a KAT (F3 + F9), and add the Δs_min/Δs_irr entropy-budget audit as a
PRACTICE diagnostic on the interface contract (F6).
