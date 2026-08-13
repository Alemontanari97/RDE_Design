# Expert read — Fernandes, Souza & Afonso (2023), MoC-based shape design optimization

**Reader role:** convergence review, one-to-one against the record apparatus of the
cycle-averaged variational nozzle program.
**Read date:** 2026-08-13.
**Why it was on the list:** flagged as a DIRECT THREAT to the empty-niche claim
("variational MoC formulation + modern optimizer"). Verdict below: **near-miss, niche NOT
occupied** — but the niche wording must be pinned.

---

## 1. Citation (verified from the PDF)

Tiago Fernandes, Alain Souza, Frederico Afonso, *"A shape design optimization methodology
based on the method of characteristics for rocket nozzles"*, **CEAS Space Journal (2023)
15:867–879**, https://doi.org/10.1007/s12567-023-00511-1. ORIGINAL PAPER, Open Access
(CC BY 4.0). Received 10 November 2022 / Revised 24 April 2023 / Accepted 26 June 2023 /
Published online 8 July 2023. Affiliation: IDMEC, Instituto Superior Técnico, Universidade
de Lisboa, Av. Rovisco Pais, 1049-001 Lisbon, Portugal. 31 references.

## 2. Read coverage

**13 / 13 PDF pages read integrally** (journal pp. 867–879), including all figures/tables
(Figs. 1–9, Tables 1–2), footnote 1 on p. 876, the Declarations block, and the complete
31-item reference list on pp. 878–879. Nothing was skipped. No supplementary material is
referenced ("data available on request"); the MATLAB/SU2 source and the raw surrogate
training data are NOT in the PDF and were therefore NOT read.

---

## 3. What the paper actually does

| Slot | Content (as printed) |
|---|---|
| **Problem** | Preliminary-design shape optimization of a **2-D planar** supersonic rocket nozzle to maximize the thrust coefficient `C_T = F/(p_0 A_t)` (Eq. 22). Secondary objective in the NSGA-II runs: minimize nozzle height ("shows a direct proportionality to the drag forces", p. 873). Explicit aim, p. 869: "develop a low-fidelity model using a MoC capable of being integrated in an **optimization framework**". |
| **Formulation** | **Black-box parametric NLP.** The generic template is Eq. (13) (`min f(x)` s.t. `A·x ≤ b`, `A_eq·x = b_eq`, `lb ≤ x ≤ ub`, taken from Martins–Ning [23]); it is then explicitly **reduced to bound constraints only**, Eq. (23): `min_x f(x) such that lb ≤ x ≤ ub`, with the printed justification "when using an optimizer for the MoC, one has to take into consideration that the restriction to the optimizer is intrinsic to the method itself instead of being expressed separately" (p. 873). **No Lagrangian, no multipliers, no Euler–Lagrange system, no transversality, no adjoint.** |
| **Unknowns** | Free-form-deformation control-point displacements `x_FFD`, linked to Sederberg control points `P_ijk` (Eqs. 10–12). In the Table-1 campaign only ONE node is active ("the most upright node of the FFD box"), bounds −0.5 and 2; the Fig. 8 run activates multiple nodes on a [9×2] box. |
| **Constraints** | Box bounds on `x_FFD` only (Eq. 23). No length constraint, no area-ratio constraint, no curvature/angle bound, no separation criterion. Ambient pressure is a **swept parameter** (0, 0.25, 0.5, 0.75, 1 atm), one independent optimization per value. |
| **Flow model** | 2-D planar MoC ("a two-dimensional MoC produces a wedge-shaped nozzle with a rectangular outlet", p. 875; "unit breadth and unit throat height"), steady, supersonic, **constant entropy and constant total enthalpy** (stated p. 870), **calorically perfect gas** (γ enters Eqs. 2 and 5 as a constant), shock-free, sharp-corner throat with a centred Prandtl–Meyer fan. Base geometry = minimum-length nozzle at `M_e = 3`, `n_char = 50`, from `θ_w,max = ν(M_e)/2` (Eq. 14). The "arbitrary nozzle" marcher replaces the wave-cancellation condition Eq. (15) by the Euler wall BC `θ_wall = θ_contour` (Eq. 16). Thrust from the **quasi-1-D** relation Eq. (17) `F = ṁV_e + (p_e − p_amb)A_e`, with `V_n = V_e cos θ_e` (Eq. 18) and exit state obtained by a "centred Riemann sum" (Eqs. 19–20) plus linear interpolation onto a **"virtual" characteristic** imagined between the last two left-running characteristics (Eq. 21). High-fidelity cross-check: SU2 **Euler** solver, ROE scheme, structured mesh, ideal gas γ = 1.4, **R = 287 J/(kg·K) — "the default value for standard air"** (p. 874), adaptive CFL 0.5–100, 2-level multigrid. |
| **Solver** | MATLAB `fmincon` (gradient-based, local, deterministic) and **NSGA-II** (population-based, gradient-free, multi-objective) — both driving the MoC as a black box. Second route: **surrogate-based optimization (SBO)**, a polynomial fit (MATLAB + Excel) to SU2 `C_T` data, then the same two optimizers on the surrogate. **The gradient-supply mechanism for `fmincon` is never stated anywhere in the paper.** |
| **Verification** | (i) MoC contour vs analytic area–Mach Eq. (2): with `n_char = 10` the relative error is "already under 1%" (p. 875); with 100 characteristics the exit height differs from the analytic value by **0.18%** (p. 878). (ii) SU2 grid-convergence study on five structured meshes with **Richardson extrapolation**, Eqs. (24)–(26); the chosen [200×30] mesh has a **0.297%** relative error in `C_T,SSL` and runs in **3.4 s** vs **0.12 s** for one MoC evaluation (footnote 1: 64 GB RAM, Xeon E5-2620 v2 @ 2.10 GHz ×24). (iii) MoC-optimum vs SBO-optimum comparison, Table 2. |

**Headline results.** Table 1 (gradient-based, single active FFD node): at `p_amb = 0`,
`C_T` = 1.61217 / 1.60647 / 1.59609 / 1.58533 for FFD boxes 2×2 / 3×2 / 5×2 / 9×2.
Multi-variable [9×2] run in vacuum: `C_T,vac` improves from **1.56784 to 1.61612**,
i.e. **+3.08%** (p. 878). Base nozzle: `p_0 = 3 723 300 Pa`, `T_0 = 3000 K`, exit pressure
exactly 1 atm. Conclusion of record, p. 878: "The resulting **thrust-optimized contour
(TOC)** demonstrated being able to be **contoured accurately by a parabola**."

---

## 4. Hypotheses

### Declared
1. Steady, supersonic, inviscid (Euler) flow; no turbulence/viscosity model (p. 874).
2. Constant entropy **and** constant total enthalpy — i.e. homentropic AND homoenergetic,
   hence irrotational (p. 870, sentence introducing Eq. 6).
3. Ideal gas with constant ratio of specific heats (γ appears as a constant in Eqs. 2, 5);
   SU2 side pinned to γ = 1.4, R = 287 J/(kg·K) (p. 874).
4. Two-dimensional planar geometry, unit breadth, unit throat height (p. 875).
5. Shock-free isentropic design intent ("MoC provides a technique for properly designing the
   contour of a supersonic nozzle for shock-free, isentropic flow", p. 871).
6. Sharp-corner (minimum-length) throat with a centred PM fan; supersonic Dirichlet inflow
   at the throat in SU2 (p. 874).
7. Ambient pressure constant within a run; quasi-1-D thrust bookkeeping (Eq. 17).

### Undeclared but necessary
8. **Caloric perfection** is never named as a restriction, even though `T_0 = 3000 K` is used
   on the MoC side. Worse, the SU2 validation runs **air** (R = 287) — so the "rocket nozzle"
   working fluid is effectively air in both routes; no combustion-gas thermodynamics anywhere.
   The program's γ-variable standing directive (E4) has no counterpart here.
9. **No shock forms on any deformed FFD contour.** Never checked. The paper itself concedes
   the mechanism can break: "for too fine a grid the characteristic line might collapse when
   experiencing slight compression… the whole characteristic grid might break down" (p. 878).
10. **No flow separation** at over-expanded conditions (p_amb = 0.5, 0.75, 1 atm), although
    contours designed for `p_e = 1 atm` are run against those ambients. No separation criterion
    exists in the method.
11. **Exit flow uniform enough for Eq. (17) to be a faithful thrust.** The paper documents that
    it is not: "the MoC has… its exit conditions not being coincident with the real nozzle exit.
    This leads to error when the flowfield is not uniform leaving the last characteristic line,
    since part of the flow is not simulated" (p. 877).
12. **Objective smoothness for `fmincon`.** Asserted only generically ("in practice, however,
    they can tolerate discontinuities as long as they are not near the optimum", p. 871) and
    never verified for a marching scheme whose characteristic-mesh node count and topology
    change with the design vector.
13. **Gradients exist and are computable** — the supply mechanism (analytic? complex-step?
    forward finite differences, the MATLAB default?) is nowhere stated. This is the single
    largest undeclared hypothesis of the paper.
14. The FFD box is fixed and contains the deformed geometry at all iterates; the throat and
    the kernel region are frozen (only downstream control nodes move).
15. The "virtual characteristic" linear interpolation (Eq. 21) is an admissible exit-state
    reconstruction; the Riemann sum (Eq. 19) is applied on a **non-uniformly spaced** set —
    conceded on p. 877 ("the distance between the 'virtual' exit characteristic and its
    adjacent ones is not constant").
16. Richardson extrapolation (Eqs. 24–26) presumes the three grids lie in the asymptotic range
    and share a constant refinement ratio; only a single observed order `p` is reported, with
    no asymptotic-range check.
17. Polynomial surrogate adequacy — partly self-refuted on p. 877 ("overfitting"; the SU2
    framework "only outputs the `C_T` with four decimal places"; "inability to work with more
    than one design variable at a time without the curve fitting process becoming too complex").

---

## 5. Findings (three-level comparison)

Anchors are journal page numbers as printed (867–879 = PDF pages 1–13).

### TEORICO

**T-1 — THREAT (niche wording) / verdict: claim 8 SURVIVES. Confidence ALTA.**
*Claim touched: nicchia-vuota (claim 8), P2/G14.*
This is the closest published artifact to the sentence "keep the MoC and swap in a modern
optimizer", and a hostile reader could call the niche occupied. **It is not.** What is kept is
the MoC as a **flow simulator**; what is discarded is the entire variational content. Rao is
cited exactly once, historically: "Rao [8] developed in 1958 a method by using the calculus of
variations to design the wall contour of the optimum thrust nozzle by using a simple parabolic
approximation" (p. 868) — and never used again. The optimization statement is Eq. (23),
`min_x f(x) s.t. lb ≤ x ≤ ub`, solved by `fmincon`/NSGA-II. **Action of record:** the niche
must henceforth be worded as *"retains the classical **variational optimality conditions**
(Rao Eqs. 11–14 / Hoffman-E residual) as the object being solved, and swaps in a modern
gradient-based optimizer"* — never as "MoC + modern optimizer", which Fernandes 2023 already
does in the black-box sense.

**T-2 — GAP-CONFIRMS. Confidence ALTA.**
*Claim touched: D2 gap G3 (no averaged shape theorem), and the T-T3 framing.*
Ambient pressure is treated as a **swept parameter producing four independent optima**, not as
a measure-weighted family sharing one contour: Table 1 (p. 876) lists a *different* optimal
`x_FFD` for each of `p_amb` = 0, 0.25, 0.5, 0.75 atm (1.1167 / 0.7721 / 0.4773 / 0.2225 on the
2×2 box). There is no measure μ, no weighting, no shared-shape-across-states functional, and no
unsteadiness anywhere in the paper. G3 is confirmed real by a 2023 paper written specifically
about MoC-based nozzle shape optimization.

**T-3 — CONTAINED. Confidence ALTA.**
*Claim touched: containment claim (18), (P)/T7.*
Their problem is (P) restricted by: μ = a single Dirac atom (one operating state); H1 with
γ = const; planar geometry, i.e. the δ = 0 branch of `q := 2π y^δ`; `P_a` constant; irrotational,
homentropic **and** homoenergetic core (their own p. 870 wording), i.e. the S1 shock-free
sub-tier S₀; constraint vector empty apart from box bounds. Under exactly those hypotheses
T7(b) degenerates to the single-phase Hadamard wall condition and T7(c) to Rao's Eq. (14)
free-endpoint condition — **neither of which they write down**. Containment is therefore
strict: their formulation is a proper restriction of the record apparatus, with the optimality
system deleted rather than solved.

**T-4 — GAP-CONFIRMS. Confidence ALTA.**
*Claim touched: (\*\*') weighted transversality (claim 16), CSTR_PA, P2/G14.*
The only optimality condition invoked in the entire paper is the **quasi-1-D** one:
"the condition of optimality states that `p_e = p_amb`" (p. 876), repeated as
"a total optimal condition (`p_e = p_amb`) cannot be achieved because the flow may not be
expanded too extensively". This is precisely the θ_E → 0 degeneration of the record corner
condition `p_a = p − ½ρW² sin(2θ) tan α` (CSTR_PA). A 2023 MoC-optimization paper using the
degenerate scalar condition instead of Rao's transversality is direct evidence that the correct
endpoint condition has left modern low-fidelity practice.

### FORMALE

**F-1 — GAP-CONFIRMS. Confidence ALTA.**
*Claim touched: P2/G14 (Rao = adjoint bridge), claim 1.*
Across 13 pages there is **no Lagrange multiplier, no adjoint variable, no Euler–Lagrange
equation, no transversality condition, and no first integral**. Section 2.5–2.7 present only
the generic NLP template Eq. (13) and a gradient-free/gradient-based taxonomy. The bridge claim
is untouched — indeed, the paper cannot even state it. Corroborating bibliography evidence in
§6 below: neither the classical variational line (Guderley, Hantsch, Hoffman, Kraiko,
Shmyglevskii) nor the modern adjoint line (Lions, Pironneau, Jameson, Giles, Lozano) appears in
the 31 references.

**F-2 — CONTAINED. Confidence MEDIA.**
*Claim touched: Route A thrust integrand f1.*
Their thrust functional is the **uniform-exit-plane degeneration** of the record control-surface
integrand `f1 = [(p − p_a) + ρW² sin(φ−θ) cos θ / sin φ] q`. Concretely: Eq. (17)
`F = ṁV_e + (p_e − p_amb)A_e`, Eq. (18) `V_n = V_e cos θ_e`, and a centred Riemann sum
(Eqs. 19–20) with linear interpolation onto a "virtual" characteristic (Eq. 21). Containment
holds under: exit surface taken as a plane normal to the axis, small exit flow angle, and a
state uniform enough that the θ-weighted momentum flux equals the plane-averaged one. The paper
itself measures the cost of that degeneration — the MoC `C_T` is **systematically higher** than
SU2's in every row of Table 2 (p. 877; e.g. 1.61217 vs 1.58895, 1.51788 vs 1.49927) and the text
attributes it to exactly this ("the MoC seems to overestimate the coefficient of thrust", p. 877).

**F-3 — CORRECTION (citation hygiene for our litmap). Confidence ALTA.**
*Claim touched: any future litmap citation of Fernandes 2023's validation.*
The Conclusions state (p. 878): "The maximal deviation of the design variable `Δx_FFD` between
both methods showed **not to exceed a 20% absolute variation**." Their own **Table 2 (p. 877)
contradicts this**, listing `Δ(%)` = 24.9, 55.0 and **60.1** for `p_amb = 0.5 atm` on the 3×2,
5×2 and 9×2 boxes (and the body text on p. 877 even says "finer FFD grids are the ones dealing
with overshooting issues (`Δx_FFD ≈ 60%`)"). **Record instruction:** do not cite this paper as
evidence of MoC-optimizer fidelity, and if it is cited in the litmap, cite Table 2 (up to 60.1%
design-variable disagreement, ~1.2–1.5% `C_T` disagreement) and explicitly NOT the ≤20% sentence.

### ALGORITMICO

**A-1 — ADOPT (structure only, with a named caveat). Confidence MEDIA.**
*Claim touched: VI.5 driver design vector; H-CLASS (S24).*
Adoptable object: **free-form deformation** as a topology-agnostic parameterization laid over a
base contour (Sederberg's scheme, Eqs. 10–12, ref. [22]), together with an explicit
**parameterization-refinement ladder** (FFD boxes 2×2 / 3×2 / 5×2 / 9×2, Fig. 6, Table 1) whose
effect on both the optimal design variable and the objective is tabulated. Innesto point: the
VI.5 driver's design vector (currently attachment angle θ_B + clamped spline wall nodes) and,
more pointedly, the **H-CLASS dof ladder** — S24 recorded that the tier-0 9-dof class
*measurably* fails H-CLASS (min DE val 7.31e-2 = 33× the tightest pre-registered floor), which
is exactly a "the class is too poor" diagnosis calling for a certified refinement ladder.
FFD also composes naturally with the sector tournament, since it deforms a base geometry
without committing to a wall-node topology.
**Caveat of record (do not import their execution):** their ladder is **confounded** — in
Table 1 only one control node is active regardless of the FFD grid size, so a finer box means a
*less influential* single variable, and `C_T` at `p_amb = 0` **decreases** monotonically
(1.61217 → 1.60647 → 1.59609 → 1.58533) with refinement. That is a parameterization artifact,
not a convergence study. Note further that going from 1 active variable on a 2×2 box (1.61217)
to a multi-variable [9×2] run (1.61612) buys only ≈0.24%.

**A-2 — GAP-CONFIRMS. Confidence ALTA.**
*Claim touched: O3.1 / Lemma-B guarantee (claim 13); nicchia-vuota (claim 8).*
The paper is a documented case of the **non-differentiable MoC-in-the-loop** problem that the
record pipeline's implicit `custom_vjp` unit-process design exists to remove. Two anchors:
(i) the gradient-supply mechanism for `fmincon` is **never stated** in 13 pages; (ii) the
mesh-topology fragility is admitted verbatim — "for too fine a grid the characteristic line
might collapse when experiencing slight compression. This outcome is strictly undesired, since
the whole characteristic grid might break down introducing far worse errors than the ones trying
to be avoided" (p. 878). No transposition/dot-product identity, no discrete adjoint, no
verification of any derivative. Claim 13 and the differentiable-march route are unchallenged.

**A-3 — GAP-CONFIRMS (strongest single datum). Confidence ALTA.**
*Claim touched: nicchia-vuota (claim 8), P2/G14.*
The adjoint was **in their hands and declined**. Section 3.8, p. 874: "Although SU2 provides a
feature to perform shape design optimization, the computational budget available for this work
would not sustain such complex simulations. Furthermore, to use this design capability in SU2,
one has to adapt the source code such that the nozzle design with the aforementioned features is
enabled (e.g., nozzle outputs and flow post-processing), which is outside the scope of this
document." They then built a **polynomial surrogate** instead. A 2023 team working on nozzle
shape optimization, holding an adjoint-capable open-source framework, chose a polynomial fit.
The niche is empty by practice, not by ignorance of the tools.

**A-4 — THREAT (presentational, not technical). Confidence MEDIA.**
*Claim touched: programme value proposition; T-T3 / Rao-at-⟨Pc⟩ narrative.*
Their black-box loop **empirically rediscovers the classical answer**: "The resulting
thrust-optimized contour (TOC) demonstrated being able to be contoured accurately by a parabola"
(p. 878), for +3.08% `C_T,vac` at 0.12 s per evaluation vs 3.4 s for CFD (p. 876 + footnote 1).
A reviewer can ask why a certified variational machine is needed when FFD + `fmincon`
reproduces Rao's parabolic contour in seconds. **Rebuttal of record:** the recovery is
uncertified (no KKT residual, no bound ladder, no globality mechanism), single-state (no μ),
γ = const, planar, shock-free, separation-blind, with an exit-plane thrust that overestimates
`C_T` in every validated row (Table 2), a design variable disagreeing with the high-fidelity
route by up to 60.1%, and a mesh admitted to break down under "slight compression". It also
recovers the *shape family*, never the *optimality conditions* — Rao's parabola was already
known in 1960. This is a threat to a careless framing, not to any claim of record.

---

## 6. Bibliography inspection (record datum)

31 references, pp. 878–879.

**Classical variational nozzle line — almost entirely ABSENT.**
- **Rao: PRESENT** — [8] Rao, G.V.R.: *Exhaust nozzle contour for optimum thrust.*
  J. Jet Propuls. **28**(6), 377–382 (1958). Cited once, historically (p. 868), never used.
  Note the mis-characterization: the sentence conflates the 1958 exact variational construction
  with the later parabolic approximation ("by using a simple parabolic approximation").
- **Guderley: ABSENT. Hantsch: ABSENT. Hoffman: ABSENT. Kraiko: ABSENT.
  Shmyglevskii: ABSENT. Sirazetdinov: ABSENT. Rao–Beck: ABSENT. Scofield–Hoffman: ABSENT.**
- MoC textbook line present: [20] Anderson, *Fundamentals of Aerodynamics*, 6th edn (2017);
  [21] Ferri, A.G., *The Method of Characteristics*, Princeton UP (2015); [24] Kulkarni, NPTEL
  Lecture 34 in Gas Dynamics. Zucrow–Hoffman is **absent**.
- Nozzle-design context present: [3] Sutton & Biblarz; [7] Frey et al., *tictop* nozzle,
  CEAS Space J. 9(2) 175–181 (2017); [9] Hagemann et al., AIAA 1998-3522; [10] Khare & Saha,
  *Rocket nozzles: 75 years of research and development*, Sādhanā 46:76 (2021);
  [14] Sun, Luo & Feng, *New contour design method for rocket nozzle of large area ratio*,
  Int. J. Aerosp. Eng. (2019) — already in our corpus as `sun_2019_rao_contour_...`;
  [15] Cai et al., Aerosp. Sci. Technol. 11(2) 155–162 (2007); [11] Afridi & Khan (2022);
  [17] Asha et al. (2019); [18] Khan et al. (2013); [19] Matsunaga et al., Aerosp. Sci. Technol.
  130:107879 (2022); [31] Murnaghan, MSc thesis, UPC (2019).
- Likely citation slip worth recording: p. 868 reads "Classical optimization procedures began
  with an inviscid design, such as **Rao's method [14]**" — but [14] is Sun et al. 2019, not
  Rao [8]. Low importance; noted for accuracy only.

**Modern adjoint / PDE-constrained optimization line — ENTIRELY ABSENT.**
- **Lions: ABSENT. Pironneau: ABSENT. Jameson: ABSENT. Giles: ABSENT. Lozano: ABSENT.**
  No adjoint reference of any kind.
- Optimization references are generic: [23] Martins & Ning, *Engineering Design Optimization*,
  CUP (2021); [25] Seshadri, NSGA-II MATLAB File Exchange; [26] Deb et al., NSGA-II,
  IEEE Trans. Evol. Comput. 6(2) 182–197 (2002); [16] Colonno, Van der Weide & Alonso,
  AIAA 2008-911 (multi-fidelity).
- CFD side: [27] Cummings et al.; [28] Economon, Palacios, Copeland, Lukaczyk & Alonso,
  *SU2: an open-source suite for multiphysics simulation and design*, AIAA J. 54(3) 828–846
  (2016); [29] Wesseling; [30] NASA Glenn spatial-convergence tutorial.
- Parameterization: [22] Sederberg & Parry, *Free-form deformation of solid geometric models*,
  ACM SIGGRAPH Comput. Gr. 20(4) 151–160 (1986).

**Reading of the bibliography.** The reference list is a clean cross-section of the "modern
low-fidelity nozzle optimization" community, and it contains **exactly one** point of contact
with the classical variational corpus (Rao 1958, used decoratively) and **zero** points of
contact with adjoint-based shape optimization — while citing SU2, whose adjoint they explicitly
declined to use. This is a strong, quotable data point for the empty-niche claim and for the
D2/G3 gap.

---

## 7. Novelty vs the 1971 state of the art (HTH-1971 / Hoffman 1967)

**At the variational level: none — the paper is strictly weaker.** Hoffman 1967 and
Hoffman–Thompson–Hoffman 1971 solve the *axisymmetric, rotational, constrained
(length/area-ratio) maximum-thrust* problem with multiplier **fields**, adjoint PDEs sharing the
flow characteristics, a derived exit-surface Mach-line character, and an optimality **residual**
on the boundary condition (Hoffman 1967 Eq. (78) `E = y·h1 − (u y' − v)·h3`; Scofield–Hoffman
Eq. (43) for the wall). Fernandes 2023 solves a 2-D planar, perfect-gas, irrotational,
homentropic, homoenergetic, unconstrained-except-bounds parametric `C_T` maximization with an
off-the-shelf optimizer and **no optimality conditions at all**, on air (R = 287). It also
recovers empirically (the "parabolic TOC", p. 878) a shape family that Rao derived in 1958–60.

**What it does add over 1971 — and it is not nothing, but it is all engineering practice:**
1. A reusable **software pattern**: geometry-agnostic FFD parameterization (Eqs. 10–12) layered
   on a base contour, driven by standard optimizers, so the design space is not tied to the
   variational construction's own degrees of freedom.
2. **Multi-objective** treatment (thrust vs nozzle height/drag) via NSGA-II — a constraint class
   the classical Route A provably cannot carry, matching Shmyglevskii's declared limit that the
   check-contour method "cannot carry constraints not expressible on the check contour".
3. An explicit **multi-fidelity verification ladder**: low-fidelity MoC vs SU2 Euler with a
   documented grid-convergence study and Richardson extrapolation (Eqs. 24–26, 0.297% relative
   error), plus a quantified cost ratio (0.12 s vs 3.4 s) that prices the fidelity trade.
4. An honest, itemized **limitations section** (§4.6) naming the exit-surface non-coincidence,
   the coarsening characteristic grid downstream, the interpolation/Riemann-sum error and the
   characteristic-grid collapse under compression — useful as a catalogue of MoC-in-the-loop
   failure modes.

None of (1)–(4) touches the mathematics. The classical 1967/1971 machinery remains, on every
axis of rigor (flow model, constraint handling, optimality conditions, gas model, dimensionality
of the state), ahead of this 2023 paper.

---

## 8. Bottom line for the programme

- **The niche is NOT occupied.** MoC is used as a *simulator inside a black-box optimizer*
  (`fmincon` / NSGA-II on Eq. 23, bound constraints only). The variational optimality condition
  is neither used nor mentioned beyond a historical nod to Rao [8].
- **Claim 8 survives**, but its wording must be pinned to "retains the variational optimality
  conditions" (see T-1), otherwise Fernandes 2023 is a defensible counter-example to a loose
  reading.
- **Claims 1 (P2/G14), 7 (D2-G3), 13 (O3.1/Lemma-B) and 16 ((\*\*')) are all confirmed as real
  gaps** by this paper, several of them with quotable text.
- **One thing to adopt** (FFD + a parameterization-refinement ladder, into VI.5 / H-CLASS), with
  the confound in their own ladder named so it is not imported.
- **One citation-hygiene correction**: their ≤20% agreement sentence contradicts their Table 2
  (up to 60.1%); never cite the sentence.
