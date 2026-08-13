# Expert read — Paxson, Miki, Perkins & Yungster (2022), "CFD Optimization of an Experimental RDRE Nozzle"

Reader: convergence-review expert reader. Date of read: 2026-08-13.
File: `literature_review/paxson_miki_2022_rdre_nozzle_cfd_optimization.pdf`

---

## 0. Citation (verified from the PDF)

Paxson, D. E.¹, Miki, K.¹, Perkins, H. D.¹ (NASA Glenn Research Center, Cleveland, Ohio 44135, USA),
and Yungster, S.² (HX5, LLC, Cleveland, Ohio 44142, USA),
**"Computational Fluid Dynamic Optimization of an Experimental Rotating Detonation Rocket Engine Nozzle."**
12 pages, 12 figures, 2 numbered equations, 16 references.

**Rigor note on the citation.** The paper number **AIAA 2022-4107 is NOT printed anywhere on the
pages of this PDF** — there is no AIAA running header, no conference name, no date line, no DOI on
p. 1 or in the footer of any page. The number comes from the reading list, not from the document.
Internal dating evidence consistent with 2022: Ref. [8] is AIAA-2022-1879 (January 2022) and the
text states "Initial RDRE testing is planned for the 2022 calendar year" (p. 3). Author footnotes
give all four as Aerospace Research Engineers, Research and Engineering Directorate (AIAA Associate
Fellow / Senior Members).

---

## 1. Read coverage

**12 of 12 pages read in full, including the complete reference list (p. 12).** Nothing skipped.
Figures were read as rendered images; quantitative values taken from figures (Figs. 3, 8, 10) are
declared below as *figure-read* and are approximate. All numbers quoted with page anchors come from
the body text unless marked figure-read.

---

## 2. What the paper actually does

**Problem.** Choose the nozzle geometry of a specific ~5,000 lbf laboratory RDRE (methane/LOX,
ER = 1.3, nominal 17.7 lbm/s, sea-level exhaust to 14.7 psia, annulus with no physical throat,
2 detonation waves) to maximize **nozzle thrust at a single operating point**. The baseline is a
**shrouded truncated plug** with a straight 30° plug cone (Fig. 1).

**Objective functional.** Cycle-time-averaged exit-plane thrust, p. 6 **Eq. (1)**:

    F = (1/t_cycle) [ ∬ ρ_e v_e,axial² dA_e dt + ∬ (p_e − p_amb) dA_e dt ]

with `t_cycle` = the time for one of the two waves to traverse the circumference. Nozzle thrust is
isolated by difference, p. 7 **Eq. (2)**: `F_n = F − F_no_nozzle`.

**Unknowns (design variables).** Exactly **two scalars**: the overall expansion area ratio
`A_e/A_ch` and the shroud fraction of the expansion area `A_sh/A_e` (p. 7). The plug portion and
the overall length are **held fixed** ("The plug portion of each nozzle and the overall length do
not change", p. 7). The shroud wall is a heuristic: *"The serpentine shape of the shroud inner wall
is not based on theory. It is simply a smooth fit that transitions from the inner to the outer
diameter with zero rate of change at the beginning and end"* (p. 7).

**Constraints.** None imposed formally. Fixed length, fixed plug cone, and (implicitly, at the
recommendation stage) diameter/mass/cooling preferences that are *not* in the functional.

**Flow model.** Two codes, **one-way coupled** (methodology of Ref. [5], Miki et al. AIAA-2020-3872):
- Upstream annulus: in-house **Q2D** unwrapped-annulus solver, two-species reactive **Euler** with
  source terms (reaction rate, skin friction, wall heat transfer at 1460 R walls), explicit
  2nd-order two-step Runge–Kutta, Roe approximate Riemann solver, piecewise-linear MUSCL with slope
  limiting, 400 × 65 cells, deliberately coarse/diffusive to suppress detonation cells and K-H
  (p. 3–4). Working fluid **calorically perfect** (CPG), γ = 1.182, R_g = 60.12 ft·lbf/lbm·R,
  manifold P_m = 320 psia, T_m = 540 R. Result = a time-invariant limit cycle in the wave frame.
- Nozzle: 3D **OpenNCC** unsteady multi-species **RANS** (viscous), ~4 M cells, chemistry **frozen**
  ("No reactions are utilized for this work. The fluid constituent species are 'frozen' throughout
  the domain", p. 5), composition from a **CEA** equilibrium calculation at the time-averaged exit
  state (H₂, H₂O, CO₂, CO), giving R_g = 71.05 ft·lbf/lbm·R (p. 4).
- The rotating Q2D exit-plane distribution (Fig. 3) is imposed as an **unsteady but periodic inlet
  BC**, assumed **radially uniform** (p. 5). ~15 wave revolutions to limit cycle.

**Solver / "optimization".** **Parametric one-factor-at-a-time sweep of 7 CFD designs** (V1–V7,
V1 = baseline shared by both lines): four points varying `A_e/A_ch` at drifting `A_sh/A_e`
(Figs. 7–8), four points varying `A_sh/A_e` at `A_e/A_ch` = 5.0 (Figs. 9–10), each line fitted with
a **second-order polynomial** "to indicate trends" (p. 8), plus **one** off-line combination check
(`A_e/A_ch` = 5.7, `A_sh/A_e` = 18%). No gradient, no optimality condition, no convergence
criterion, no error bars, no design-of-experiments. Cost: ~1.5 days on 360 cores per design (p. 5).

**Verification.** (i) Code validation by citation only ([6–9] for Q2D, [5,15] for OpenNCC).
(ii) Limit-cycle convergence certificate triple: exit-plane mass-flow limit cycle reached, *cycle-
averaged thrust constant*, and *cycle-averaged mass flow into and out of the nozzle matched* (p. 5).
(iii) BC-placement check: the nozzle domain includes 0.6 in of annulus, and the states there differ
from the Fig. 3 mapping plane "by less than 6% as measured by ratios of their standard deviations"
(p. 5). (iv) **A single grid check, not a study**: V5 rerun at ~7.7 M cells (30 days on 480 cores),
total thrust matching to within **0.4%**; the paper states plainly "Due to time and resource
restraints, a full grid refinement study was not possible" (p. 10).

**Headline numbers (all reproduce arithmetically — checked).**
CPG estimate ṁ = 19.1 lbm/s, F_i = 5592 lbf → after the CEA thermally-perfect remap
ṁ = 16.13 lbm/s, **F_i = 5003 lbf**; chamber-alone thrust **F_no_nozzle = 3993 lbf**; notional ideal
nozzle thrust **F_ni = F_i − F_no_nozzle = 1010 lbf** (p. 4, p. 8). Baseline total = **4580 lbf** =
91.5% of ideal (8.5% below); baseline nozzle thrust = 4580 − 3993 = 587 lbf = **58.1%** of 1010 ✔.
Optimized 70.0% → 707 lbf → total 4700 lbf = **94%** of ideal ✔. **The optimization gain is
+120 lbf ≈ +2.4% of total engine thrust.**

**The "notional ideal".** *"the ideal thrust is found by isentropically expanding (i.e. accelerating)
each element of mass in the exit plane to its velocity at atmospheric pressure. The axial components
of the ideal velocities are then mass flux averaged to obtain an ideal specific thrust which is then
multiplied by the computed flow rate to get ideal thrust [12]. Note that this ideal is notional only
since it would require a nozzle with variable exit area in both time and space."* (p. 4)

---

## 3. Hypotheses

### Declared
H-D1. Choked/supersonic annulus exit ⇒ chamber cycle unaffected by nozzle design (abstract, p. 1).
H-D2. Single operating point; result explicitly **not generalizable** (p. 11, §IV: "the nozzle design
and parameterization cannot be generalized").
H-D3. Two uniformly spaced detonation waves; unclear what happens otherwise (p. 4, p. 11).
H-D4. Q2D annulus: calorically perfect single gas, γ = 1.182 (p. 3).
H-D5. Nozzle: frozen composition, thermally perfect multi-species mixture from CEA (p. 4–5).
H-D6. Idealized inflow BC at the injector face (manifold at fixed P, T; check-valve model
      preventing backflow) since injector details were unknown (p. 4).
H-D7. Nozzle inlet flow **radially uniform** (p. 5).
H-D8. Ambient p_amb = 14.7 psia constant on all external surfaces (p. 5).
H-D9. Coarse/diffusive Q2D grid deliberately suppresses cell-scale unsteadiness (p. 3).

### Undeclared but necessary
H-U1. **One-way coupling is exact**: no acoustic/entropic feedback from the nozzle into the annulus.
      This is *enforced by the Q2D outflow BC construction*, not verified (see Finding 3).
H-U2. The Q2D exit-plane state, computed under a **CPG with R_g = 60.12**, remains a valid inflow
      state after being re-interpreted as a **mixture with R_g = 71.05** in the 3D code. No
      conservative re-mapping is described; ṁ and F_i are simply re-derived (p. 4).
H-U3. **Axial** Mach ≥ 1 at the interface. The paper reports only the Mach "comprised of both axial
      and circumferential velocity components" (Fig. 3 caption / p. 5); the axial component is never
      shown, while "significant local tangential velocity components" are asserted (p. 2).
H-U4. The 2-parameter family contains a design close to the true optimum of the (much larger)
      shrouded-plug shape space — the plug cone angle, truncation station and length are frozen.
H-U5. Second-order polynomial fits through 4 scattered points are an adequate response surface;
      and the two parameters are separable enough for OFAT — **contradicted by the paper itself**
      (p. 10: "the parameters A_e/A_ch and A_sh/A_e are not independent").
H-U6. Turbulence/wall modelling (RANS closure, wall functions, wall temperature) does not bias the
      *ranking* of designs — never tested; only a 0.4% total-thrust grid check exists.
H-U7. The notional ideal is a legitimate normalizer, i.e. the per-element isentropic expansion is an
      upper bound for every design considered (no sonic capping, no attainability argument).

---

## 4. Verification requested: is the abstract's choking/decoupling claim proven or assumed?

**Claim under test (abstract, p. 1):** *"The fluid in the RDRE chamber leading to the nozzle is
choked at its exit so that its cyclic behavior is unaffected by any changes to the nozzle design."*

Evidence chain, in order of appearance:

| # | Page | Text | Status |
|---|------|------|--------|
| 1 | 2 | "The exit plane boundary condition for the combustor region **ensures** that the flow is sonic or supersonic at all times." | **Imposed by BC** |
| 2 | 3 | "The annulus does not have a physical throat. **However, the fluid mechanics of the RDRE still yields** sonic or supersonic flow in the annulus exit plane." | Asserted as a computed outcome |
| 3 | 4 | "At the exit plane, constant pressure outflow is imposed along with characteristic equations… **If the resulting flow is sonic, or supersonic, then the imposed pressure is disregarded.** If, in addition, the upstream flow is supersonic, then pressure, density, and axial velocity are extrapolated from the interior." | The code *switches off* downstream influence |
| 4 | 5, Fig. 3 | Exit-plane Mach ≈ 1.15–1.45 (figure-read) — but explicitly "comprised of both axial and circumferential velocity components" | Total-velocity Mach, not axial |
| 5 | 2, 5 | Architecture is two domains, one-way mapped (Ref. [5]) | No two-way coupling exists |
| 6 | 5 | Interface-placement check: states 0.6 in upstream differ from the mapping plane "by less than 6% as measured by ratios of their standard deviations" | Consistency of the mapping, **not** a back-influence test |

**Verdict: ASSUMED, not demonstrated — a modeling hypothesis with partial internal support.**
It is (a) built into the Q2D outflow boundary condition, (b) structurally guaranteed by the one-way
two-code architecture (the annulus solution is computed *once*, before any nozzle exists, and is
reused unchanged for all seven nozzles), and (c) supported only by the *total-velocity* Mach field
of the Q2D solution. **No back-pressure sensitivity run, no two-way coupled run, and no axial-Mach
margin are reported anywhere in the paper.** The 6% check on p. 5 is often mistaken for such a test;
it is not — it compares two stations of the *same* Q2D solution against the 3D mapping, i.e. it
tests where the interface was placed, not whether the nozzle can talk back.

Consequence for our programme: this is the SOTA instance of exactly the pattern registered in
`validation/ADVISORY_rde_choking_2026-08-11.md` — choking is an *assumption or an integral of the
model*, never a certified property. It must be classified as **hypothesis** in our lit-map and
**must not** be cited as independent physical validation of the L4 default (see Finding 4).

---

## 5. Findings (three-level comparison)

### TEORICO

**F1 — CONTAINED (ALTA).** *Claim touched: (P) / D2.3 measure μ / T7.*
Their objective, p. 6 Eq. (1), **is** a cycle-time-averaged thrust functional over the limit cycle:
`F = (1/t_cycle)[∬ρ_e v²_axial dA_e dt + ∬(p_e − p_amb) dA_e dt]`. This is our J = ∫_Ξ F[S; s(ξ)] dμ
with μ = normalized cycle time — the D2.3 default measure, uniform, no atoms — evaluated on an
exit-plane control surface rather than on the wall. It sits inside (P) under: fixed shared wall
across all phases; single operating point (no trajectory/operating measure); Pa constant (14.7 psia,
p. 5); frozen composition (P1 pin); design set reduced to a 2-dimensional scalar family inside one
topology sector (shrouded truncated plug) rather than A_gen(c) with sector tournament. **They
evaluate J; they never differentiate it.** No T7(a) adjoint, no T7(b) shared-wall condition ("no
phase satisfies its own wall condition; the μ-average does"), no (\*\*') transversality. This is the
strongest available confirmation that our functional is the *physically right* object at the SOTA
frontier — the same integral, computed at 13,000 core-hours per point.

**F2 — GAP-CONFIRMS (ALTA).** *Claims touched: D2 gap G3 (claim 7), empty-niche claim (claim 8),
P2/G14 (claim 1).*
The record NASA study shares one wall across the entire rotating-wave family and **derives no
averaged optimality condition of any kind**. The wall is admittedly untheorized: *"The serpentine
shape of the shroud inner wall is not based on theory. It is simply a smooth fit…"* (p. 7); the plug
is a straight 30° cone (Fig. 1), fixed. The bibliography (p. 12, 16 refs) contains **no Rao, no
Guderley, no Hantsch, no Hoffman, no Kraiko, no Shmyglevskii, no Sternin** — the only classical
nozzle-design references are [3] Angelino (approximate plug design, AIAA J. 1964) and [4] Onofri
(plug nozzle survey, AIAA 2002-0584), neither variational — and **no adjoint/shape-optimization
reference at all**: no Lions, no Pironneau, no Jameson, no Giles, no Lozano, no optimization theory
of any kind. Gap G3 and the empty-niche claim are confirmed by the strongest possible witness: the
paper that *would* have cited that literature if it were in use.

**F3 — GAP-CONFIRMS (ALTA).** *Claim touched: two-regime choking contract (ADVISORY_rde_choking),
L4 interface default, T-NSW.*
See §4 above for the full chain. The decoupling claim is **imposed by the outflow BC** ("the exit
plane boundary condition … **ensures** that the flow is sonic or supersonic at all times", p. 2;
"If the resulting flow is sonic, or supersonic, then the imposed pressure is disregarded", p. 4) and
**structurally guaranteed by one-way coupling**, never tested against a back-pressure perturbation.
This confirms verbatim the advisory finding that choking is an assumption/integral of the model
throughout the literature. Its direct consequence for us: our audit list (stage-A H-I2/choking
margin) is doing work that the SOTA does not do, and our two-regime contract is not redundant.

**F4 — CORRECTION (MEDIA-ALTA).** *Claims touched: L4 default class, T-NSW, citation discipline.*
Our L4 default requires **every patch axially supersonic with margin**, min(M_x − 1) > 0, and
T-NSW excludes mean upstream influence *by theorem* on that class. Paxson et al. report only the
Mach number **"comprised of both axial and circumferential velocity components"** (Fig. 3 caption,
p. 5, and text p. 5), with values ≈ 1.15–1.45 (figure-read), while simultaneously stating that
"there are significant local tangential velocity components" (p. 2). Since M_axial < M_total
whenever swirl is present, **their data does not establish M_x > 1 anywhere**, and at the low end of
their range a modest tangential fraction drives M_x below 1. **Correction to be applied to our
lit-map:** this paper may be cited as evidence that the SOTA *assumes* an axially-supersonic
interface, and never as evidence that RDE exit data *is* L4-admissible. Any of our sentences citing
NASA RDRE exit-plane Mach numbers in support of L4 must be re-qualified to "total-velocity Mach,
axial component not reported".

**F5 — CONTAINED (MEDIA).** *Claim touched: T-T3 (collapse), E4.*
p. 7 reports a *steady, γ = const, one-dimensional* sizing at the **mean** condition: ideal exhaust
Mach 2.94 from the ideal specific thrust and exhausted total enthalpy, then "Standard compressible
flow equations … (assuming that the throat Mach number is 1.0) [16]. **For γ = 1.182, the value is
A_e/A_ch = 6.54**". p. 8 then reports the *cycle-averaged 3D unsteady* sweep result: "Approximately
7% improvement in the thrust is obtained if A_e/A_ch is increased from 5 to 6.5. This appears to
coincide with near perfect expansion of the flow on a time averaged basis." **6.54 predicted at the
mean vs ≈ 6.5 measured cycle-optimal**: an independent, high-fidelity, empirical instance of the
T-T3 pattern (cycle-optimal design = classical design at the mean state), obtained by a group with
no knowledge of the theorem. Caveats binding the confidence to MEDIA and the tag to CONTAINED rather
than a validation: (i) the coincidence lives on a **one-parameter slice**, and the shroud-fraction
parameter — shown on p. 9 to matter *more* — was drifting along that slice; (ii) their flow is
viscous, swirling and radially non-uniform, so H1/H3 of T3 are not satisfied; (iii) the matching is
at the mean *exit* condition, not at ⟨Pc⟩_μ. Note also that the *object* they use is exactly the
γ = const closed-form ε↔M bijection that E4 forbids as a solver step and permits only as
oracle/initializer — and they use it in precisely that demoted way, calling it "based on steady flow
arguments; however, it still proved useful as a preliminary design tool" (p. 7). Our E4 discipline
is corroborated as the right practice.

**F6 — GAP-CONFIRMS (MEDIA).** *Claims touched: T-T3-MAP swirl breaker, mean-swirl panel
(recovery asymmetry against the plug), F2a swirl deltas.*
p. 9: *"thrust production improves as it is shifted away from being produced on the plug surface,
and toward being produced on the shroud inner surface. **An observation is not an explanation
however, and more study is needed to understand this result.**"* The measured effect is large — the
shroud-fraction line spans 58.1% → ≈71.5% of ideal (Fig. 10, figure-read) at *fixed* `A_e/A_ch`,
i.e. bigger than the whole area-ratio effect. Our registered swirl breaker in T-T3-MAP (swirl-KE
debit E_θ, with the recovery asymmetry **signing against the plug**) is a named, first-principles
candidate explanation for exactly this unexplained observation. Two consequences: (a) the swirl
breaker is confirmed to be physically live at record scale, not a theoretical nicety; (b) this is a
**pre-registrable prediction against published NASA data** — a genuine opportunity for the F2a swirl
deltas (swirl field + TRIPLE monitor (Γ, h₀, s) + balance-residual audit). Also on record from the
same paper: "while there is **no net swirl** in the RDRE exit flow, there are significant local
tangential velocity components" (p. 2) — an assertion (unproved) that is exactly the content of our
P1 flux-nullity THEOREM\* with pointwise-nonzero covariance.

### FORMALE

**F7 — ADOPT (ALTA).** *Claims touched: T-GB / M1 geometry-free bound (claim 15), T-T4, globality
gap δ.*
Their normalizer is our bound object minus the cap: *"the ideal thrust is found by isentropically
expanding … each element of mass in the exit plane to its velocity at atmospheric pressure. The
axial components of the ideal velocities are then mass flux averaged … Note that this ideal is
notional only since it would require **a nozzle with variable exit area in both time and space**"*
(p. 4; restated in the Conclusion p. 11 as "a notional ideal RDRE nozzle which can instantaneously
change shape to allow isentropic expansion of every fluid element"). Structurally this is
∫F_id dμ **uncapped** (no sonic cap, cf. our claim 15, where the uncapped form is already rejected
on four subcritical Table-1 rows), and the "instantaneously reshaping nozzle" is precisely our
T-T4 ideal-adaptation object used as a per-phase argmax.
**What to adopt, and where:** (i) report every Verdict headline **also** as "% of the Kaemming–Paxson
notional ideal" (Ref. [12], AIAA-2018-4567) beside our capped bound, so our results are directly
commensurable with the NASA/PGC literature — innesto: VI.6 Verdict template, bound-ladder row;
(ii) register the **capped-vs-uncapped delta** on any dataset where we compute both — it is the
quantitative price of our tighter bound and a free novelty datum; (iii) adopt their explicit
**axial-projection of the ideal velocity** as the convention against which our E_θ swirl-KE debit
is compared (they retain tangential KE through the expansion but count only axial momentum — a
different debit convention from TWIN-C; the difference must be named before any cross-comparison).

**F8 — GAP-CONFIRMS (ALTA).** *Claims touched: data contract VI.1 (stage-A provenance/thermo
audits), P1 pin, Lemma A thermal pin.*
The two codes run **different thermodynamics** and the interface crosses that boundary unrepaired:
Q2D is calorically perfect with γ = 1.182, R_g = 60.12 ft·lbf/lbm·R (p. 4); the 3D nozzle runs a
frozen thermally-perfect CEA mixture with **R_g = 71.05 ft·lbf/lbm·R** (p. 4). The paper is candid:
"This change lowers the density of flow leaving the annulus and thus reduces both the predicted mass
flow rate and ideal thrust. The values become 16.13 lbm/s and F_i = 5003 lbf respectively" — i.e.
**ṁ shifts by −15.6% and the ideal thrust by −10.5% (589 lbf) purely from the thermo remap**, while
the entire optimization campaign buys **+120 lbf**. *The thermodynamic-closure uncertainty is roughly
five times the optimization gain.* Two record consequences: (a) our stage-A data-contract audits
(thermo handle γ(·;ξ) with declared provenance, EOS-general backend, consistent state across the
interface) would reject this hand-off — the contract is not bureaucracy, it guards a first-order
error; (b) their nozzle-side model — **frozen composition, thermally perfect, multi-species** — is
*exactly* the P1 scope pin and exactly the validity window of Lemma A's thermal pin (p = ρRT with
frozen composition), so Lemma A applies to the SOTA nozzle model as-is. This is also a live
instance of the [T-EQBR] frozen/equilibrium bracket being the dominant term.

**F9 — GAP-CONFIRMS (ALTA).** *Claims touched: PB-2 (truncated plug under length cap), T-T4
sharpness (base-pressure model breaks the nesting), CSTR_PB corner condition with p_b.*
p. 10: *"The bluff body region of the Version 5 nozzle (i.e., the truncated portion of the plug)
generated a **drag force equivalent to −9.5% of the nozzle thrust (−1.4% of total thrust)**. It is
possible that this small drag force could be eliminated by extending the plug to a point. However,
this also adds material that must be actively cooled, and it adds mass."* This is a **measured base-
drag magnitude for a truncated plug under genuine RDE cycle flow** — the exact object PB-2 studies
and the exact term that appears in our plug-side endpoint condition CSTR_PB (the '+'-sign mirror of
Rao Eq. (14) with base pressure p_b). Three consequences: (i) T-T4's declared sharpness clause ("a
base-pressure model … breaks the nesting; then max∫ < ∫max STRICTLY") is confirmed *physically live*
at −9.5% of nozzle thrust, not a formal caveat; (ii) the sentence "could be eliminated by extending
the plug to a point. However … adds mass" is precisely the length/mass cap that makes PB-2 a genuine
averaged problem rather than a T-T4 collapse; (iii) we now have a literature-anchored order of
magnitude (≈ 9.5% of nozzle thrust ≈ 56 lbf on this engine) to calibrate the base-pressure model in
PB-2 instead of inventing one. Note the paper offers **no base-pressure model** and no averaged
corner condition — it simply measures the drag and accepts it.

### ALGORITMICO

**F10 — GAP-CONFIRMS (ALTA).** *Claims touched: empty-niche claim (claim 8), driver VI.5, S25 speed
programme.*
The real methodological level is a **one-factor-at-a-time parametric sweep of 7 CFD designs**, not a
formal optimization. There is: no gradient, no adjoint, no optimality residual, no KKT check, no
stopping criterion, no uncertainty quantification, no error bar on any thrust value, and no
design-of-experiments. The only "surrogate" is a second-order polynomial through 4 scattered points
"to indicate trends" (p. 8). Cost per design: ~1.5 days on 360 cores ≈ 1.3 × 10⁴ core-hours (p. 5);
the single grid check cost 30 days on 480 cores ≈ 3.5 × 10⁵ core-hours (p. 10), and even so "a full
grid refinement study was not possible". **This is the economic proof of our niche:** at ~10⁴ core-
hours per function evaluation, a gradient-free search of a 2-parameter space is the *most* that can
be afforded, and shape optimization over a spline wall (our design vector: attachment angle θ_B +
clamped spline nodes) is unreachable. Our differentiable fitted MoC march (S25/S25-bis record:
segment 100.84 s → 5.58 s, 18×, on one machine) is 6–7 orders of magnitude cheaper per evaluation
and returns a gradient. The complementarity is the honest framing: their 3D URANS is the *validator*
we cannot replace; our march is the *searcher* they do not have.

**F11 — CORRECTION (ALTA).** *Claim touched: lit-map framing "OTTIMIZZAZIONE NASA DI RECORD /
58.1% → 70.0%".*
Three corrections to how this result must be stated in our documents:
1. **The 70.0% design is not the argmax.** p. 9: "The highest performing nozzle of all those tested
   was Version 7 with a 13.4% thrust improvement over the baseline. However, it also had the largest
   value of A_sh/A_e. This implies a larger diameter nozzle with greater mass." p. 10: "Since the
   Version 5 nozzle was notably smaller in diameter, but just 1.5% lower in terms of nozzle thrust
   relative to ideal, it was selected as the recommended one for experimental testing." So the
   reported 70.0% is **V5**, chosen under an *unstated multi-objective* (diameter, mass, cooling,
   manufacturability) that is nowhere in Eq. (1). The declared objective and the applied objective
   differ.
2. **"13.4% improvement" is 13.4 percentage points of ideal**, not a 13.4% relative gain:
   58.1 + 13.4 = 71.5 (V7, matching Fig. 10 figure-read), and 71.5 − 1.5 = 70.0 (V5) — the arithmetic
   only closes under the percentage-point reading. In relative terms V7 is +23%, V5 is +20.5%.
   Quote the number, never the word "improvement", without this qualifier.
3. **The 2-D landscape was never searched.** p. 10: a combination at `A_e/A_ch` = 5.7,
   `A_sh/A_e` = 18% — i.e. near the *apparent* optimum of the first sweep — "was actually 1.4% lower
   than the Version 5 nozzle… This result suggests that the parameters A_e/A_ch and A_sh/A_e are not
   independent." The two quadratic fits therefore do **not** locate a joint optimum, and the OFAT
   design is invalid on the authors' own evidence. Correct wording for our lit-map: *"best-of-seven
   CFD designs on two one-at-a-time parameter lines, recommended point selected under undeclared
   secondary criteria"* — not "NASA optimization of record".

**F12 — ADOPT (MEDIA).** *Claims touched: VI.1 stage-A audits, VI.4bis T0-flatness monitor, F2a
balance-residual audit.*
Two cheap, transferable instruments:
(i) **Limit-cycle certificate triple** (p. 5): the run is declared converged only when the exit-plane
mass flow reaches a limit cycle, **the cycle-averaged thrust is constant**, *and* **the cycle-averaged
mass flow into the nozzle equals that out of it**. The third is a conservation residual over the
cycle — the same object as the balance-residual audit already mandated as an F2a delta by the
mean-swirl panel. Adopt as an explicit *named* audit in the VI.1 stage-A list (currently our
flatness/harmonic-decay certificate covers T0 but no in/out cycle-integrated mass and momentum
balance). Note the contrast with T-T0: they require the *cycle-averaged* thrust to be constant in
*iteration*; T-T0 asserts the *instantaneous* thrust is constant in *time* through every axisymmetric
surface for a single rotating mode. Their case is a clean two-wave uniformly-spaced mode (p. 4) —
i.e. a T-T0 instance — and the flatness of their instantaneous thrust trace is **never plotted**.
That is an unexercised falsifier sitting in published NASA data.
(ii) **Interface-placement sensitivity** (p. 5): they deliberately place the mapping plane 0.6 in
inside the combustor and quantify the resulting discrepancy ("less than 6% as measured by ratios of
their standard deviations"). Our Γ_d contract audits characteristic completeness *at* the chosen
station but never measures sensitivity *to the station's axial location*. Adopt as a stage-A
robustness audit: recompute the admission audits at two stations and report the drift.

---

## 6. Bibliography inspection (record datum)

16 references, p. 12. Classified:

- **Classical variational nozzle line (Rao, Guderley, Hantsch, Shmyglevskii, Hoffman, Kraiko,
  Sternin, Scofield): ABSENT — zero citations.**
- **Modern adjoint / shape-optimization line (Lions, Pironneau, Jameson, Giles, Ulbrich, Lozano,
  Nadarajah, Peter–Dwight): ABSENT — zero citations.** No optimization-theory reference of any kind;
  no surrogate/DOE/response-surface methodology reference either.
- Only classical-adjacent nozzle-design entries:
  - [3] Angelino, G., "Approximate Method for Plug Nozzle Design," *AIAA Journal*, Vol. 2, No. 10,
    1964 — approximate (PM-based) plug design, **not** variational-optimal.
  - [4] Onofri, M., "Plug Nozzles: Summary of Flow Features and Engine Performance," AIAA 2002-0584 —
    a survey.
  - [16] Thompson, P. A., *Compressible Fluid Dynamics*, McGraw-Hill, 1988, pp. 281 — the source of
    the γ = const area-ratio relation used for the 6.54 sizing.
- The rest is the NASA/PGC in-house chain: [1] Lietz et al. 2020-0687; [2] Paxson 2014-0284;
  [5] **Miki, Paxson, Perkins, Yungster, "RDE Nozzle Computational Design Methodology Development and
  Application," AIAA-2020-3872** (the methodology this paper applies — already reviewed in
  `reports/miki_2020_nasa_methodology.md`); [6] Paxson et al. 2015-1101; [7] Rankin et al. 2015-0877;
  [8] Tobias et al. 2022-1879; [9] Theuerkauf et al. 2016-1200; [10] Stubbs & Liu 1997-3114 (NCC);
  [11] Teasley et al. 2021-3655; [12] **Kaemming & Paxson, "Determining the Pressure Gain of Pressure
  Gain Combustion," AIAA-2018-4567** (source of the notional-ideal thrust); [13] Paxson & Perkins
  2021-0192; [14] Gordon & McBride, CEA, NASA RP-1311, 1994; [15] Miki, Moder & Liu, *JPP* Vol. 34,
  2018, pp. 415–427 (OpenNCC).

**Record conclusion.** The paper defining the state of the art in RDRE nozzle "optimization" at NASA
is bibliographically disjoint from both the classical variational nozzle corpus and the modern
adjoint corpus. It cites no work that could have supplied an optimality condition. This is the
cleanest available evidence for claims 1 (P2/G14 bridge unoccupied), 7 (gap G3) and 8 (empty niche),
and it is *positive* evidence — a group with the motive, the budget and the platform to do
gradient-based averaged shape optimization did a 7-point sweep instead, because the formulation was
not available to them.

---

## 7. What the paper PROVES vs what it ASSERTS

| Statement | Status |
|---|---|
| Baseline shrouded truncated plug yields 58.1% of notional ideal nozzle thrust; V5 yields 70.0%; total 94% | **Computed** (single code chain, one grid check at 0.4%, no error bars) |
| Shroud fraction A_sh/A_e matters more than overall area ratio A_e/A_ch | **Computed**, on 4+4 points (Figs. 8, 10) |
| Thrust production shifting from plug surface to shroud inner surface improves performance | **Observed, explicitly unexplained** (p. 9) |
| Chamber is choked at exit ⇒ cycle behavior independent of nozzle design | **Assumed / BC-enforced** (see §4) |
| No net swirl in the RDRE exit flow | **Asserted** (p. 2), no supporting figure |
| The 6.54 ideal area ratio | **Derived** under steady 1-D γ = const — declared "steady flow arguments" |
| Notional ideal is an upper bound | **Asserted** (uncapped, attainability only heuristically argued) |
| Grid independence | **One check, 0.4%**, explicitly not a study (p. 10) |
| Result generalizes to other RDREs | **Explicitly denied by the authors** (p. 11) |

---

## 8. Net position for the programme

Nothing in this paper threatens a theorem, occupies the niche, or pre-empts a novelty claim. It
strengthens four of them (G3, empty niche, P2/G14, the choking two-regime contract), supplies one
empirical near-coincidence in the T-T3 direction (6.54 vs ≈ 6.5, MEDIA confidence, one-parameter
slice), hands us a quantitative base-drag anchor for PB-2 (−9.5% of nozzle thrust), and offers three
concrete adoptions (notional-ideal reporting axis, cycle-integrated in/out balance audit,
interface-placement sensitivity audit). It forces two corrections in our own documents: the lit-map
framing of "NASA optimization of record" (best-of-seven OFAT, recommended point ≠ argmax,
percentage-point arithmetic) and the prohibition on citing its exit-plane Mach numbers as evidence
of an axially-supersonic (L4) interface.
