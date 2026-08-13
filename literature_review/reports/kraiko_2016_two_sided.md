# Expert read — Kraiko, Pyankov & Tillyaeva (2016), *Contouring Two-Sided Asymmetric Plane Maximum-Thrust Nozzles*

Reader: convergence-review expert reader. Date of read: 2026-08-13.
File: `literature_review/kraiko_2016_two_sided_asymmetric_maxthrust_nozzles.pdf`

---

## 1. Citation (verified from the PDF header/footer)

A. A. Kraiko, K. S. Pyankov, N. I. Tillyaeva, "Contouring Two-Sided Asymmetric Plane
Maximum-Thrust Nozzles," **Fluid Dynamics**, 2016, Vol. 51, No. 1, pp. 120–125.
Pleiades Publishing, Ltd., 2016. ISSN 0015-4628. **DOI: 10.1134/S0015462816010142**.
Original Russian text © A. A. Kraiko, K. S. Pyankov, N. I. Tillyaeva, 2016, published in
*Izvestiya Rossiiskoi Akademii Nauk, Mekhanika Zhidkosti i Gaza*, 2016, Vol. 51, No. 1,
pp. 115–120. Affiliation: Baranov Central Institute of Aviation Motors (CIAM), ul.
Aviamotornaya 2, Moscow, 111116 Russia. Received June 1, 2015.
Funding: Russian Foundation for Basic Research, project No. 14-08-31211 (p. 124).

## 2. Read coverage

**6 / 6 pages read integrally (pp. 120–125), bibliography included** (12 references, pp. 124–125).
The paper carries **no numbered equations at all** — the entire content is prose, 5 figures
(Figs. 1–5) and one Table (p. 124). All quantitative anchors below are therefore given as
*page + figure/table + verbatim quotation*, never as an equation number (there are none to cite).
Nothing was unreadable. Not read (out of scope, not on disk): the original Russian MZhG version
and the 12 cited works.

## 3. What the paper actually does

**Problem (p. 120, opening paragraph).** "We consider the problem of contouring a plane nozzle
producing a maximum thrust *R* and its horizontal direction at the given values of the gas flow
rate *G*, the nozzle pressure ratio π_c (the ratio of the total pressure at the nozzle entry to
the external static pressure), and an asymmetric domain of the permissible arrangement of a
nozzle, *X* in length, with the greatest possible transverse dimension *Y*."
Planar (2-D) geometry, **not** axisymmetric. Design regime π_c = 300, γ = 4/3 (p. 121).

**Formulation. This is NOT a variational/exact-theory paper.** From the abstract (p. 120):
"The investigation is based on the numerical integration of the Reynolds-averaged Navier–Stokes
equations and **direct optimization methods using genetic algorithms** and the representation of
the optimized contours in the form of the **Bernstein–Bézier curves**." Keywords: "asymmetric
nozzles, direct optimization methods, genetic algorithms."
The exact variational theory enters **only as the generator of the two reference nozzles**:
"The symmetric supersonic section of the nozzle, as well as the one-sided nozzle, are designed
using the method of characteristics realizing the exact solution of the corresponding variational
problem within the framework of the Euler equations for perfect gas flows [6]" (p. 121; ref. [6]
= A. N. Kraiko, *Variational Problems of Gasdynamics*, Nauka, 1979).

**Unknowns.** Nine "arbitrarinesses" (p. 122): "In contouring asymmetric two-sided plane nozzles
the number of the varied parameters (arbitrarinesses) was taken to be nine." They parametrise
both walls of the supersonic part, the throat position/height *h*, and the shape downstream of
the bend; "The order of the splines is determined by the number of arbitrarinesses admitted by
the chosen approximation" (p. 122). The subsonic arm is **not** optimised — "designed by hand to
ensure a more uniform flow at the exit at separationless flow inside the arm. Its length in the
axial direction is chosen to be 2.5" (p. 121).

**Constraints (the point of interest for us).**
1. Given mass flow rate *G* (met only approximately; see Δ_G in the Table, −0.73 % … +0.42 %).
2. Given π_c = 300.
3. **Asymmetric geometric box**: Fig. 1, *X* = 14, *Y* = 9, combustor-exit transverse dimension
   y₀ = 1.5, the nozzle adjoining the combustor on the left. Throat transverse dimension
   *h* ≈ 1.01–1.03 (Table).
4. **Thrust-direction requirement**, handled as a *second optimisation criterion* rather than a
   hard constraint: "in the plane of the optimization criteria R_x and |tan α| … The quantity R_x
   is maximized, while the value of the second criterion is minimized" (p. 122, Fig. 3).
5. **Curvature / bend-count restriction as a particle-laden-flow surrogate**: "The possible
   presence of solid or liquid particles in the gas flow issuing from the nozzle is taken into
   account in the contouring process by introducing restrictions on the flow duct curvature as
   the total number of turns/bends" (p. 120); and "the optimization algorithm includes some
   restrictions on the greatest permissible angle of inclination of the subsonic section of the
   contoured nozzle" (pp. 121–122).
6. **Subsonic-arm inclination β fixed by scan**: three optimisation cycles at β = 0.1, 0.5, 0.9
   (p. 122). β = 0 is the one-sided limit; maximum β is the symmetric-supersonic-section nozzle 2.

**Flow model.** RANS: "based on the integration of the Reynolds-averaged Navier–Stokes equations
(RANS) closed by the ν_t-90 turbulence model using the Godunov–Kolgan difference scheme [10–12].
The Reynolds number based on the critical parameter and the height of the minimum nozzle
cross-section in this set of calculations Re = 5 × 10⁶" (p. 122). Perfect gas, γ = 4/3.
Viscous losses are therefore **inside the objective**: "The thrust losses were determined with
account for viscosity from the calculations of nozzle flows by means of integration of the
averaged Navier–Stokes equations closed with the ν_t-90 turbulence model [7]" (p. 121).

**Solver / optimiser.** Derivative-free genetic algorithm, multi-criterion: "The optimal
asymmetric two-sided nozzles is performed using the direct optimization method developed by the
authors on the basis of a genetic algorithm realized in the form of the original multi-criterion
optimization program complex [8, 9]" (p. 122). "The genetic optimization algorithm uses the main
mechanisms of the biological evolution in the form of mutations, that is, a casual variation in
the parameter vector determining the unknown contour shape, and the selection of parent specimens"
(p. 122). Result read off a **Pareto front** (Fig. 3): "Points 2 correspond to the best calculated
cases that form the so-called Pareto front… One of the points of the front with a permissible
value of |tan α| gives the solution of the problem under consideration for the given angle of
inclination of the subsonic section β" (p. 122). **No adjoint, no gradient, no optimality
conditions are written anywhere in the paper.**

**Verification.** One grid-doubling check only: "The parameters of the chosen variant were refined
on the computation grid with a double cell number in each direction. In these recalculations the
variation in the specific thrust loss was not greater than a few percent of the loss level"
(p. 122). Mass-flow mismatch repaired by normalisation: "To eliminate the inaccuracies due to the
difference in the flow rate in the compared nozzles, which is within the limits of 1 %, we analyze
the losses of the specific thrust, that is, the thrust divided by the flow rate through the
nozzle" (p. 121). Flow-field sanity check on nozzle 5 only: "We note the absence of appreciable
shocks and flow separation zones in the flowfield" (p. 124, with Fig. 5 Mach field).

**Numbers of record (Table, p. 124; ideal reference from p. 121: Y_id = 19.68, R_id = 2.4653).**

| Nozzle | h | β | Y | μ | Δ_G, % | tan α | R_x | ΔR_x, % |
|---|---|---|---|---|---|---|---|---|
| 1 (one-sided) | 1.01 | 0 | 0.646 | 0.984 | −0.63 | −0.001 | 2.3592 | 4.30 |
| 2 (two-sided, symm. supersonic) | 1.03 | — | 9 | 0.969 | −0.25 | −0.006 | 2.4050 | 2.45 |
| 3 | 1.02 | 0.1 | 7.778 | 0.985 | 0.42 | 0.009 | 2.3745 | 3.68 |
| 4 | 1.01 | 0.5 | 8.025 | 0.983 | −0.73 | 0.004 | 2.3895 | 3.08 |
| 5 | 1.02 | 0.9 | 8.876 | 0.979 | −0.73 | 0.006 | 2.3937 | 2.90 |

Internal-consistency check performed by this reader (not by the paper):
R_id·(1 − ΔR_x) reproduces every R_x to ±1 in the 4th decimal (e.g. 2.4653·0.9710 = 2.3938 vs
2.3937). The Table is arithmetically self-consistent.

**Headline result (p. 124).** "the contouring of the lower wall and the throat position of plane
asymmetric nozzles makes it possible to reduce the thrust losses in the design regime, as compared
with the standard contouring of plane nozzles, by 0.6 % under the rigid constraint β = 0.1 … to
1.4 % at β = 0.9 in nozzle 5" (these are percentage-*points* of loss: 4.30 − 3.68 = 0.62 and
4.30 − 2.90 = 1.40). Nozzle 2 (symmetric supersonic section, not achievable with a constrained
subsonic arm) bounds the family at 2.45 %, i.e. "1.85 % as compared with the one-sided nozzle"
(p. 121). Also p. 121: relative to the ideal nozzle of the greatest permissible expansion degree
(Y = 9) all quoted losses drop by a further 1.52 %.

**Off-design (p. 124, last technical paragraph).** "The nozzles realizing the least and greatest
values of the specific thrust in the design regime (one-sided nozzle 1 and two-sided nozzle 2 with
a symmetric supersonic section, respectively) were also compared in off-design regimes. The
advantage of the two-sided nozzle in the specific thrust is conserved up to the fivefold increase
in the external pressure relative to the nominal one. **With further increase in the external
pressure the characteristics of the one-sided nozzle are better.**"

## 4. Hypotheses

**Declared.**
- Perfect gas, constant γ = 4/3 (p. 120: "The gas is assumed to be perfect, with a given adiabatic
  exponent γ"; p. 121: γ = 4/3).
- Plane (2-D) geometry; single design regime π_c = 300.
- RANS closure by the ν_t-90 one-equation turbulence model [7]; Godunov–Kolgan scheme [10–12];
  Re = 5 × 10⁶ on throat height.
- Geometric box X = 14, Y = 9, y₀ = 1.5; subsonic-arm axial length fixed at 2.5, hand-designed.
- Nine shape parameters, Bernstein–Bézier splines.
- Particles are represented **only** by curvature/bend-count restrictions (they are not modelled).
- Ideal-nozzle reference Y_id = 19.68, R_id = 2.4653 (used to normalise all losses).

**Undeclared but necessary.**
1. Steady flow; single-point (Dirac) operating condition — no operating measure, despite the
   authors' own remark on start-vs-cruise weighting (p. 120).
2. Infinite span / no end-wall effects: a *plane* nozzle used to draw conclusions about real
   hardware requires the 2-D idealisation to be non-degenerate.
3. Fully turbulent boundary layer from the throat; no transition model; wall thermal condition
   (adiabatic vs isothermal) never stated, although viscous loss is the discriminating quantity.
4. Attached flow in the design regime — asserted a posteriori for nozzle 5 only (p. 124), not
   verified for nozzles 3, 4, nor at the off-design conditions where the ranking crossover is
   claimed.
5. GA global convergence: the Pareto front (Fig. 3) is asserted to be the front; no convergence
   criterion, population size, generation count, or repeat-seed test is reported.
6. Class adequacy: the 9-parameter Bernstein–Bézier family is assumed rich enough to contain a
   near-optimal contour; no class-refinement study.
7. Discretisation adequacy across the *comparison*: one grid doubling on "the chosen variant"
   only; the bar is never propagated to the inter-nozzle differences that carry the conclusion.
8. Constraint satisfaction by normalisation: G is violated by up to 0.73 % and repaired by
   dividing thrust by the realised flow rate — i.e. the comparison is *matched-ṁ by convention*,
   not by constraint.
9. Constant external static pressure, uniform; thrust direction evaluated on a fixed exit station.
10. The reference R_id = 2.4653 is an ideal (inviscid, unconstrained-expansion) value; its basis is
    not derived in the text, so all ΔR_x values inherit an unstated reference convention.

## 5. Findings — three-level comparison against the programme apparatus

### TEORICO

**F1 — CORRECTION (ALTA). The reason-for-listing is wrong: this is not an extension of the exact
theory.** Our list entry describes this paper as "l'ultima estensione vera della teoria esatta
(piani asimmetrici a due lati, vincoli geometrici + forza)". The paper is a **direct
RANS + genetic-algorithm + Bézier** study. Evidence: abstract, p. 120 ("direct optimization methods
using genetic algorithms"); keywords; p. 122 (GA mechanics, RANS/ν_t-90/Godunov–Kolgan). The exact
variational theory appears exactly once and only as the *generator of the two reference nozzles*
(p. 121: "designed using the method of characteristics realizing the exact solution of the
corresponding variational problem … [6]"). There are **no equations, no functional, no multipliers
and no optimality conditions** in the paper. The litmap line must be re-worded: *the last
extension is by the Russian school's own migration AWAY from the exact theory*.
Touches: litmap entry / claim 18 corpus classification.

**F2 — GAP-CONFIRMS (ALTA). D2 gap G3 and claim 7 are confirmed, and the paper contains the
sharpest verbal near-miss found so far.** Two anchors.
(i) p. 120: "the solution of the problem of the choice of an optimal plane nozzle configuration is
far from unique and **depends, in particular, on the ratio of the losses at the start and in the
cruise flight**." That is a measure over operating conditions *named in words* — and then never
formalised: the optimisation is executed at the single design point π_c = 300 only.
(ii) p. 124: the off-design comparison is a **post-hoc ranking crossover** — the two-sided nozzle's
advantage "is conserved up to the fivefold increase in the external pressure … With further
increase in the external pressure the characteristics of the one-sided nozzle are better."
So the corpus (a) knows the objective *should* be a weighted average over regimes, (b) observes
that the design-point argmax loses its rank off-design, and (c) still never writes the averaged
functional nor derives averaged optimality conditions. This is exactly gap G3 and exactly the
niche of (P). Recommended wording upgrade (analogous to the ISABE-2003-117 caveat): the G3 claim
should now carry "verbal recognition of a start/cruise loss weighting exists in the corpus
(Kraiko–Pyankov–Tillyaeva 2016, p. 120) without any formulation."

**F3 — GAP-CONFIRMS (ALTA). Claim 8 (empty niche) and claim 1 (Rao = adjoint bridge) survive, and
this paper is now the strongest positive evidence for both.** Faced with constraints that Route A
cannot carry (asymmetric box, bend count, subsonic-arm inclination, thrust direction), the *Kraiko
school itself* does not extend the variational formulation — it **abandons** it for a
derivative-free GA on RANS (p. 122). The bibliography contains **zero** adjoint-method references
(see §6). Nobody in this lineage "keeps the variational MoC formulation and swaps in a modern
optimizer": they keep neither MoC nor the functional, and the optimiser they swap in is
gradient-free. Reinforcing external datum from their own reference list: refs [2] (Kraiko &
Pyankov, *Fluid Dynamics* 49(1), 120, 2014, "Contouring Optimal Three-Dimensional Nozzles") and
[5] (Isakova, Kraiko & Pyankov, ZhVMMF 52, 1976, 2012, "Direct Method of Contouring Optimal
Three-Dimensional Aerodynamic Shapes") show the same migration in 3-D — consistent with our
recorded Route A limit "no check surface exists in 3-D".

**F4 — CONTAINED (ALTA), with the containment boundary named.** The *inviscid core* of the design
problem is a restriction of (P) under: μ = Dirac at a single phase (π_c = 300), δ = 0 (plane
instead of axisymmetric, i.e. q = 2πy^δ with δ = 0), γ = const = 4/3, geometry-only constraints
plus the mass constraint (our λ₂) and the length/box constraint (our λ₃ / ε_max, here X ≤ 14 and
Y ≤ 9 of Fig. 1), and the symmetry-class element of our c set to "asymmetric". Their "one-sided vs
two-sided" distinction is a **topology-sector** choice in our sense, and their own result — that
which sector wins depends on the constraint values *and* on the ambient pressure (p. 124) —
directly supports our design pin "configurations are outputs, not inputs" and the sector
tournament. **The containment stops at the objective**: their functional contains viscous losses
(p. 121, "The thrust losses were determined with account for viscosity"), which is our already
DECLARED structural non-containment §6(c) "boundary-layer-terms-in-the-functional". No new
non-containment at this level; the declared one is confirmed with a concrete instance.

**F5 — GAP-CONFIRMS (MEDIA→ALTA). Independent empirical support for the Pa ≠ 0 breaker in
T-T3-MAP.** T-T3-MAP names "Pa ≠ 0" as a breaker of the general "cycle-averaged optimum =
matched-single-point optimum" claim. Here, at fixed geometry class and fixed feed, raising the
ambient pressure past ≈ 5× nominal **reverses the ranking of two designs** (p. 124). Under our
H2' (ambient-blind interior, full-flowing supersonic exit) such a reversal cannot occur through the
interior solution — it can only come through the pa-linear term or through H2' failing (over-
expansion / separation at high pa). Either way the datum is on the breaker's side, not T3's:
T-T3-as-stated is not touched (H2' is violated in their high-pa regime), but the *general* claim
is again refuted empirically. Caveat: the paper gives no numbers for this comparison, only the
sentence — evidence strength is an assertion, not a table.

### FORMALE

**F6 — THREAT (MEDIA). A third structural non-containment candidate: the thrust-VECTOR criterion.**
Our (P) has a scalar objective J. This paper optimises the **pair** (R_x, |tan α|) and selects on a
Pareto front (p. 122: "in the plane of the optimization criteria (R_x, |tan α|) … The quantity R_x
is maximized, while the value of the second criterion is minimized"; Fig. 3; Table column tan α
with values 0.009 … −0.001). Our declared non-containment list has exactly two entries
(Kraiko–Osipov's endogenous trajectory-adjoint weight §6(g); boundary-layer terms §6(c)); a
**vector-valued objective / thrust-direction criterion** is not among them, and (P) as written
cannot express it — Pareto selection is not a restriction of scalar argmax. Two honest defences,
both requiring a decision: (a) scalarise — direction as a hard constraint g_dir(S) ≤ c_dir with its
own multiplier, in which case it IS an element of our c and the non-containment dissolves; (b)
concede a third declared non-containment. Note the paper does not prove it needs a Pareto front:
it in fact uses direction as a threshold ("one of the points of the front **with a permissible
value of |tan α|**", p. 122), i.e. defence (a) is what they operationally do. Recommended: add
"thrust-direction / vector-thrust constraint" explicitly to c in A_gen(c) and record the
adjudication, rather than let a red-teamer find it first.

**F7 — GAP-CONFIRMS (ALTA). The declared limit of Route A ("cannot carry constraints not
expressible on the check contour") is confirmed by an instance from the school that owns Route A.**
The three constraints that force this paper off the exact theory are precisely non-check-contour
constraints: the **bend/curvature count** ("restrictions on the flow duct curvature as the total
number of turns/bends", p. 120), the **subsonic-arm inclination angle** ("restrictions on the
greatest permissible angle of inclination of the subsonic section", pp. 121–122; β = 0.1, 0.5,
0.9), and the **asymmetric arrangement domain relative to the combustor exit** (Fig. 1, y₀ = 1.5
off-centre, stated in the abstract as "One of the constraints is due to the asymmetric arrangement
of the unknown nozzles relative to the combustion chamber exit"). None of these is a functional of
the terminal control surface; all three are geometry-of-the-whole-duct constraints. This is exactly
our recorded Shmyglevskii-1980 limitation, instantiated. It also confirms that our A_gen(c) entry
"curvature/angle bounds" is not an invented decoration — it is the constraint class that killed
Route A for its own authors.

**F8 — ADOPT (MEDIA). Constraint-violation reporting + realised-flow normalisation as a Verdict
field.** The paper reports, per design, the flow-rate coefficient μ and the *signed* constraint
violation Δ_G in percent (Table: −0.73, −0.25, +0.42, −0.73, −0.63) and then compares **specific**
thrust because "the difference in the flow rate in the compared nozzles … is within the limits of
1 %" (p. 121). We should adopt this as a hard rule in the Verdict format (VI.6): whenever a design
comparison is made under an approximately-enforced constraint, print (i) the per-design signed
constraint residual, and (ii) the normalisation convention used to repair it. This is directly the
"conventions/matching" breaker of T-T3-MAP made into a reporting obligation, and it is cheap. It
also exposes a weakness in *their* result that we would catch with the rule: nozzle 4 and nozzle 5
carry the same Δ_G = −0.73 % but nozzle 3 carries +0.42 %, a 1.15-point spread across the very
designs whose loss differences (3.68 vs 3.08 vs 2.90) carry the conclusion.

### ALGORITMICO

**F9 — GAP-CONFIRMS (ALTA). The corpus has no derived-tolerance discipline: their Pareto front is
resolved ~4–6× BELOW their own stated verification bar.** Their bar (p. 122): "In these
recalculations the variation in the specific thrust loss was not greater than a few percent of the
loss level." With loss levels of 2.45–4.30 % (Table) and R_id = 2.4653, "a few percent of the loss
level" is ≈ 0.06–0.15 percentage points of loss ≈ 1.5·10⁻³ – 3.7·10⁻³ in R_x (this reader's
arithmetic from their printed numbers, 1 pp of ΔR_x = 0.0247 in R_x). The Fig. 3 Pareto plot
resolves R_x over the axis range **2.3853 → 2.3859**, i.e. a total span of 6·10⁻⁴ in R_x — smaller
than the bar by a factor of ≈ 3–6. The GA therefore selects among candidates that are
indistinguishable at the stated discretisation accuracy. Their *headline* conclusions survive
(0.62 and 1.40 pp of loss = 1.5·10⁻² and 3.5·10⁻² in R_x, i.e. ~10× the bar), but the front's fine
structure — and therefore the specific optimal contour shipped — does not. This is precisely the
gap our VI.6 stack ("nothing ships outside a Verdict"; derived, not magic, tolerances; rejectors)
is claimed to close, and it is a clean, citable instance of its absence in the SOTA of this school.
Caveat on honesty: "a few percent" is vague; the interval above is my reading of "few" ∈ [2, 5].

**F10 — ADOPT (MEDIA). Report the discretisation bar relative to the DIFFERENCE, not to the total.**
Independently of F9's negative verdict, the *form* of their statement is right and better than the
usual practice: the bar is quoted as a fraction of the **loss level** (the small quantity being
compared), not of the thrust (the big number). Innesto: our DWR / two-resolution Richardson bars
in the Verdict should be printed twice — absolute, and as a fraction of the design-to-design
difference being adjudicated — so that any comparison whose effect size falls below its own bar is
auto-flagged. This is a one-line addition to the Verdict formatter and would have caught F9
automatically.

**F11 — CONTAINED / comparability datum (MEDIA). Same design-class dimension, opposite method
economics.** Their design class is "nine … varied parameters (arbitrarinesses)" on Bernstein–Bézier
splines (p. 122) — the same dof count as our tier-0 9-dof class, which makes the two directly
comparable as *classes*. The cost asymmetry is the point: Fig. 3 shows a scatter of several
thousand GA-evaluated RANS designs to resolve one β value, and the procedure must be repeated per
β (three cycles, p. 122); our route reaches a certified KKT point with gradients (record: in-stratum
KKT 7.745·10⁻² ≤ derived gtol 1.156·10⁻¹) plus a transposition certificate. There is no threat here
— rather, this is the concrete measured baseline against which the "swap in a modern optimizer"
niche is worth occupying. Note also that their class is *richer* than ours in one respect worth
importing at F3/F4b: **the throat position and both walls are design variables, and the optimum
places a bend at the minimum cross-section** ("in nozzle 4 with β = 0.5 both walls have bends in the
minimum cross-section, and in nozzle 5 with maximum β = 0.9 the upper wall is smooth in the throat
region but the lower wall suffers a bend", p. 123). A wall-kink at the throat is an admissible
optimum in their class; our A_h spline classes should state explicitly whether they admit it (our
Clarke-subdifferential / bundle-safeguard machinery exists precisely for such kinks).

**F12 — ADOPT (BASSA/MEDIA). The β-scan as an explicit "price of the constraint" curve.** Rather
than optimising over the subsonic-arm inclination, they run three separate optimisation cycles at
β = 0.1, 0.5, 0.9 and read off the loss as a function of the constraint level (Table: 3.68, 3.08,
2.90 against the unconstrained-arm bound 2.45 and the one-sided 4.30), then state the *range*
"0.6 % … 1.4 %" as the deliverable (p. 124). This is a clean way to present a constraint whose
level is a stakeholder decision: report the objective as a function of the constraint level and
let the multiplier be read as a finite difference. Innesto: our multipliers are already "reported
as MARGINAL VALUES" (VI.5); adding a coarse constraint-level scan for the *one* constraint the
user actually negotiates (here β; for us L or ε_max) turns a local shadow price into a validated
price curve, and is a cheap non-local check on the multiplier itself. They observe a genuinely
non-monotone structural response worth noting — "The supersonic region length varies
nonmonotonically in β. It is nozzle 4 corresponding to the intermediate value β = 0.5 that has the
shortest supersonic section" (p. 123) — a reminder that the price curve need not be smooth in the
geometry even where the objective is monotone.

## 6. Bibliography inspection (record datum)

Twelve references, pp. 124–125. **Composition: 12/12 Russian-school works; 11/12 in Russian or
Russian journals; the single non-Russian-venue item (ref. [4], J. Propulsion Power) is also by the
same authors.** There is not one citation to a non-Soviet/non-Russian author anywhere in the paper.

**Classical nozzle line.**
- **Kraiko: YES** — [6] A. N. Kraiko, *Variational Problems of Gasdynamics* [in Russian], Nauka,
  Moscow (1979). This is our G5 human-pass gate item; it is cited here as *the* source of the exact
  MoC/variational construction used for the reference nozzles.
- Also present, adjacent classical: [1] V. N. Zudov, *Album of Two-Dimensional Nozzles, Parts 1 and
  2* [in Russian], Siberian Division of the USSR Academy of Sciences, Inst. of Theoretical and
  Applied Mechanics, Report No. 1239 (1981) — cited as "the conventional technique of designing
  supersonic plane optimal-in-thrust nozzles" (p. 120).
- **Rao: NO. Guderley: NO. Hantsch: NO. Hoffman: NO. Shmyglevskii: NO.** None appears.
  Notably the paper's core object (a plane maximum-thrust contour) is cited to Zudov and Kraiko
  only — the Western Route A lineage is absent even where it is the direct antecedent.

**Modern adjoint line.**
- **Lions: NO. Pironneau: NO. Jameson: NO. Giles: NO. Lozano: NO.** No adjoint, continuous or
  discrete, is cited or mentioned anywhere in the text. The word "adjoint" does not occur.

**Plug-nozzle line (relevant to T-T4 / PB-2 / T-T3-SI, procurement leads).**
- [3] S. V. Baftalovskii, A. N. Kraiko, N. I. Tillyaeva, "Contouring Self-Adjustable Plug Nozzles,
  Optimal when Operating in a Vacuum, and Determining their Thrust at Start from the Earth," in:
  *Selected Works of XXII Scientific Lectures on Cosmonautics* [in Russian], Voina i Mir, Moscow
  (1999), p. 116. — **vacuum objective + start-thrust evaluation**: this is squarely the
  tier-1 + vacuum corner of T-T3-SI and the two-regime (start vs vacuum) structure of PB-2.
  Not on disk; worth procuring.
- [4] A. N. Kraiko, N. I. Tillyaeva, S. V. Baftalovskii, "Optimal Design of Plug Nozzles and Their
  Thrust Determination at Start," *J. Propulsion Power* **17**, 1347 (2001). — English-language,
  obtainable, same subject; also worth procuring for the T-T4 / PB-2 dossier.
- Both are invoked on p. 120 for "the self-adjustment property when operating in the high-pressure
  regimes in the case of a beveled nozzle [3, 4]".

**Direct-method / 3-D line (evidence for the school's migration).**
[2] Kraiko & Pyankov, *Fluid Dynamics* **49**(1), 120 (2014), "Contouring Optimal Three-Dimensional
Nozzles"; [5] Isakova, Kraiko & Pyankov, ZhVychisl. Mat. Mat. Fiz. **52**, 1976 (2012), "Direct
Method of Contouring Optimal Three-Dimensional Aerodynamic Shapes"; [8] Pyankov & Tillyaeva (2010,
GA on a fan impeller blade); [9] Kraiko, Pyankov, Tillyaeva & Toporkov (2014, GA on a birotative
fan). **Numerics:** [7] Gulyaev, Kozlov & Sekundov, *Fluid Dynamics* **28**(4), 485 (1993) — the
ν_t-90 model; [10] Godunov, Zabrodin, Ivanov, Kraiko & Prokopov, *Numerical Solution of
Multidimensional Problems of Gasdynamics*, Nauka (1976); [11] Kolgan, Uch. Zap. TsAGI **3**(6), 68
(1972); [12] Tillyaeva, Uch. Zap. TsAGI **17**(2), 18 (1986).

## 7. Novelty of this paper vs the HTH-1971 / Hoffman-1967 state of the art

**What it adds.** (i) A constraint set that the exact theory cannot express — asymmetric
arrangement box relative to the combustor exit, duct-curvature/bend-count limits standing in for
particle-laden flow, and a bound on the subsonic-arm inclination. (ii) Viscous (RANS, ν_t-90)
evaluation *inside* the optimisation loop, so the optimised object is the viscous thrust, not the
inviscid one. (iii) A vector-thrust treatment: thrust direction as a second criterion with Pareto
selection. (iv) Contouring of **both** walls with a free throat position for a plane asymmetric
nozzle, and the quantified answer: 0.6 pp (β = 0.1) to 1.4 pp (β = 0.9) of loss recovered versus
the standard one-sided contouring, against a family bound of 1.85 pp set by the symmetric
supersonic section. (v) A method statement: GA over Bernstein–Bézier parametrisations as the
school's replacement for the variational construction in constrained/3-D settings.

**What it does NOT add.** Nothing to the exact theory: no functional, no multipliers, no optimality
conditions, no transversality, no new characteristic-surface result, no theorem, and no equations
at all. Relative to HTH-1971/Hoffman-1967 the *mathematical* content is strictly less; the advance
is entirely in problem scope (constraints, viscosity) and in computational method (direct GA).
For our programme this makes the paper a **scope-and-method datum, not a theory competitor**: it
neither precedes nor contradicts (P), T7, T-T3, T-T4, PB-2, EQ-v2 or the tier ladder, and it does
not occupy the empty niche of claim 8 — it documents the corpus walking away from that niche.
