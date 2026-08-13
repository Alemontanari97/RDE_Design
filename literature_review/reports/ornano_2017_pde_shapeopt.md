# Expert read — Ornano, Braun, Saracoglu & Paniagua (2017), pulsed-detonation nozzle shape optimization

**Reader role:** convergence-review expert reader. Metro di confronto = APPARATUS BRIEF of the
cycle-averaged variational nozzle program (record state, 2026-08-13).

---

## 1. Citation (verified from the PDF itself)

Ornano F, Braun J, Saracoglu BH, Paniagua G. **"Multi-stage nozzle-shape optimization for pulsed
hydrogen–air detonation combustor."** *Advances in Mechanical Engineering*, 2017, Vol. 9(2), pp. 1–9.
DOI: **10.1177/1687814017690955**. SAGE (journals.sagepub.com/home/ade). Research Article.
Date received 8 July 2016; accepted 5 January 2017. Academic Editor: Bo Yu. Creative Commons CC-BY.

Affiliations as printed on p.1: (1) Osney Thermo-Fluids Laboratory, Dept. of Engineering Science,
University of Oxford, UK; (2) Zucrow Laboratories, School of Mechanical Engineering, Purdue
University, West Lafayette, IN, USA; (3) Aeronautics and Aerospace Dept., von Karman Institute for
Fluid Dynamics, Sint-Genesius-Rode, Belgium. Corresponding author: F. Ornano.
Funding: EU FP7, *Tangential Impulse Detonation Engines* (TIDE), grant agreement 335091.

## 2. Read coverage

**9 pages of 9 read in full** (single Read call, pages 1–20 requested; the PDF contains 9 pages).
This includes the abstract, all body sections, all figure captions (Figs 1–9), the Conclusion,
Acknowledgements, Declaration of conflicting interests, Funding, the **complete reference list
(refs 1–23)** and **Appendix 1 (Notation)**.
Nothing was left unread. Caveat of record: Figures 3, 5, 7, 8, 9 are raster plots; numerical values
taken from them are only those **printed as labels or in the body text** (e.g. "5.69 kN" annotated on
Fig. 3; "23 × 10³ N", "27 × 10³ N", "12 × 10³ N" quoted in the p.7 text for Fig. 9). No value has been
eyeballed off a curve.

## 3. What the paper actually does

| Item | Content (as printed) |
|---|---|
| **Problem** | Shape-optimize the divergent nozzle bolted to a **pulsed** hydrogen–air detonation tube, single-cycle / low-frequency (**below 1 Hz**, p.2), so as to maximize the force at the nozzle exit surface. Explicitly scoped away from high frequency: "according to Ma et al.,¹⁰ at frequencies above 100 Hz, the nozzle performance may be substantially altered; hence, we invite the readers to test the present approach … at higher frequencies" (p.2). |
| **Formulation** | **Black-box design optimization.** No variational formulation, no Lagrangian, no multipliers, no adjoint, no derived optimality condition anywhere in the paper. Three stages (Fig. 1): (a) steady RANS optimization, 4th-order Bézier, **5 control points**; (b) unsteady URANS optimization on the narrowed design space, **4 control points**; (c) **evaluation only** (no optimization) of the resulting geometries with a 3D reacting DDT solver. |
| **Objective** | p.3: "The optimization aimed to maximize the nozzle exit force: **F = ṁ u_exit + p_exit A_exit**, where u_exit and p_exit are the mass-averaged exit velocity and pressure." Rationale, verbatim: "This objective was preferred, instead of the thrust, to obtain a solution that would be **independent of the phase delay between inlet and outlet**." Averaging: "The time-averaged results were obtained by **adding all the instantaneous forces and then dividing by the total time**." Notation appendix (p.9) defines F̄ = "time-averaged force acting at the nozzle exit surface (N)". **No ambient-pressure term p_a appears in F.** |
| **Unknowns** | Coordinates of the Bézier control points (5 in stage 1, 4 in stage 2). Inlet angle **fixed at 0°** (p.4). Nozzle length **fixed** l = 0.150 m; inlet radius R_inlet = 0.015 m (p.4). |
| **Constraints** | Box bounds on control-point coordinates only ("allowed to vary within wide bounds", p.4). The box bound was **ACTIVE at the reported optimum**: "The optimal design was found to be a divergent nozzle with an exit radius corresponding to **the maximum allowed by the design space** (R_exit = 0.0375 m)" (p.4). No aerodynamic/state constraints, no curvature/angle bounds, no separation constraint. |
| **Flow model** | Stages 1–2: 2D **axisymmetric URANS**, density-based, commercial **CFD++** (Metacomp), **HLLC**, multidimensional TVD polynomial interpolation, dual time-stepping with an automatic CFL adjustment procedure (ACAP), **k-ω SST**; "the **ideal gas** formulation with gas properties dependent on the flow temperature was used in the steady and unsteady optimization stages" (p.3). Grid ≈ **50,000 cells**, y⁺ < 1, first cell ≈ 10⁻⁶ m, growth 1.2, no wall functions; plenum appended at exit for the unsteady runs (p.3). Stage 3: **OpenFOAM DDTFoam** (Ettner, ref 17), density-based reactive URANS, HLLC + multidimensional slope limiters, **O'Conaire H₂ mechanism** (ref 19), Chemkin properties via **look-up tables** (ref 20), Sutherland transport (ref 21), Weller deflagration model + auto-ignition-delay detonation model; 3D **quarter** domain, no-slip walls, symmetry planes, supersonic extrapolating outlet, CFL < 0.5; **no chemical reactions inside the nozzle** — "the shaped nozzle, where only gas products expanded" (p.6). |
| **Solver / optimizer** | **CADO** (von Karman Institute in-house, Verstraete, ref 12), population-based **differential evolution**. "A CFD simulation was performed for each design selected by the optimizer. **No surrogate models were used** during the optimization, allowing convergence in fewer iterations" (p.3). Steady stage: **88 direct CFD evaluations** (Fig. 3), stopped "once the force did not improve any further within **0.02%**" (p.4). Unsteady stage: stopped when "the difference in time-averaged force between two consecutive populations was less than **1.2%**" (p.5). |
| **Verification / validation** | Validation exists **only for the stage-3 DDT solver**: flame position vs. time against the Ettner experiment in a 5.4 m obstacle-laden tube, "maximum difference of **2% in the Chapman–Jouguet velocity**" (p.7); predicted detonation cell width **30 mm** "in agreement with Giurao et al.²³" (p.7); CFL-sensitivity study, solution unaffected below CFL 0.5 (p.6); 1 mm tube mesh justified by citation to Ettner (ref 22). **No grid-convergence study for the 50k-cell optimization mesh; no discretization bar; no uncertainty on any reported delta; no optimality certificate of any kind.** |
| **Headline results** | Steady stage: F = **5.690 kN** vs **5.689 kN** for the Rao/MOC baseline — "proving the validity of Rao's method for steady-flow optimizations" (p.4). Unsteady stage: **F̄ = 607 N**, **+7.8%** over the optimizer's starting geometry (p.5). Stage 3 (reacting, time-averaged exit force): shaped nozzle vs straight duct **up to +80%**; MOC nozzle **+1.5%** over the steady-optimized nozzle; unsteady-optimized nozzle **≈ +2%** over the MOC nozzle (p.7). Peak transient exit force: MOC and unsteady-optimized ≈ 23 × 10³ N over ≈ 0.3 ms; steady-optimized **27 × 10³ N** but narrower pulse; straight duct 12 × 10³ N (p.7) — i.e. the **peak-favouring shape loses on the average**. |

### Internal inconsistency worth recording
The abstract (p.1) says the optimized nozzle delivers "about 2% more than the optimized results
assuming steady-flow operation", and the Conclusion (p.8) says "increased thrust by 2% compared to
the steady design"; the body (p.7) attributes the 2% to the comparison **against the MOC nozzle**,
with the MOC nozzle itself already 1.5% above the steady-optimized one. Under the body's numbers the
unsteady-vs-steady gap would be ≈ 3.5%, not 2%. Cite the **body** numbers, never the abstract's.

## 4. Hypotheses

### Declared
1. Ideal gas with temperature-dependent properties in the optimization stages; real-gas effects only
   in stage 3 (p.3).
2. Low frequency, **below 1 Hz**, single-cycle behaviour; higher frequencies explicitly out of scope (p.2).
3. k-ω SST is an adequate turbulence closure for this flow (p.3).
4. No chemistry inside the nozzle in stage 3; the nozzle is pre-filled with N₂/H₂O products (p.6).
5. Uniform initial conditions over the whole 3D domain; no-slip walls; symmetry on the quarter-domain
   side faces; supersonic outlet with extrapolated properties and "no boundary conditions … needed at
   the outlet" (p.6).
6. Under-resolved DDT is acceptable at the macroscopic scale — "not all microscopic scale phenomena
   are strictly significant for an accurate representation of the macroscopic features of the DDT.
   The accuracy of the under-resolved DDT simulations was proven by Thomas¹⁸" (p.5).
7. CFL < 0.5 and 1 mm tube mesh are sufficient (pp.5–6).
8. 2D axisymmetric geometry for both optimization stages; 0° inlet flow angle (pp.3–4).

### Undeclared but necessary (reader's list)
9. **Stage transfer**: that a shape optimal for the 2D axisymmetric non-reacting URANS problem remains
   the ranking-preserving choice under the 3D reacting DDT problem. Stage 3 performs **no**
   re-optimization; the transfer is assumed, never argued.
10. **Stage nesting**: that the topology class selected under *steady* flow (divergent) and the
    reduction 5 → 4 control points remain valid for the *unsteady* objective. This is precisely a
    nesting/monotonicity assumption — the kind our T-T4 has to prove, here taken for free.
11. **Box adequacy**: that the design-space box contains the optimum. Factually refuted in the paper's
    own text — the steady optimum sits **on** the R_exit bound (p.4), so the reported "optimum" is a
    boundary optimum of an arbitrary box, not a physical stationary point.
12. **Mass-averaged 1D reduction validity**: that ṁu_exit + p_exit A_exit built from mass-averaged
    quantities on a **plane** exit surface is a faithful thrust surrogate under strongly non-uniform,
    strongly transient exit profiles. Asserted, never checked (and the exit plane is not a
    characteristic surface).
13. **Grid independence** of the 50k-cell optimization mesh (only y⁺ and near-wall spacing are given).
14. **Global convergence of DE** in 88 evaluations, single run, no restart/seed study, no repeatability.
15. **Single pulse representative of a periodic cycle**: the averaging window is one pulse; refill,
    purge and inter-pulse dead time never enter F̄, although refilling frequency is invoked as a
    physical concern on p.2.
16. **p_a irrelevance to the objective**: back pressure acts in the flow (plenum) but is deliberately
    absent from F; the design is therefore implicitly a vacuum-thrust design.
17. **Fair-comparison basis of the MOC nozzle**: same l, R_inlet, area ratio 6.25 and inlet conditions
    are stated, but the design exit Mach / design ambient pressure of the Rao contour is never given,
    nor is it stated that the Rao contour was designed for **this** length constraint as a
    length-constrained optimum rather than an ideal one.

## 5. Three-level comparison with the program apparatus

### 5.1 TEORICO

**T-1 — GAP-CONFIRMS (D2 gap G3, claim 7; ALTA).**
The paper time-averages an objective over a genuinely unsteady operating cycle and optimizes a shape
against that average — and derives **no optimality condition of any kind**. There is no stationarity
system, no transversality, no measure, no adjoint; the entire "theory" content is the algebraic
definition F = ṁu_exit + p_exit A_exit (p.3). Better still, the authors state the void themselves:
"the previous literature on supersonic nozzle design relies fundamentally on steady-flow
assumptions" (p.2) and "This article addresses the void of optimization tools for nozzles exposed to
transient supersonic flows" (Conclusion, p.8). This is independent, published, dated (2017)
attestation that **the averaged shape problem has no derived optimality theory in the corpus** — our
G3 exactly. Two consequences: (i) G3 survives this paper untouched; (ii) our novelty wording must
never claim we *noticed* the void first — Ornano stated it in 2017 and should be cited as the
attesting source, our claim being about *deriving* the conditions (T7, (\*\*'), T3, T4), which they do not.

**T-2 — GAP-CONFIRMS (empty-niche claim 8; ALTA).**
This paper puts **both** ingredients of our "empty niche" on the same table and does not combine them.
The classical variational MoC line is present as a *baseline geometry*: "Rao¹¹ developed an analytical
method based on the MOC to optimize a nozzle shape for maximum thrust … The geometry designed with the
MOC was approximated by a second-order quadratic polynomial as recommended by Rao¹³" (p.4). A modern
optimizer is present: differential evolution inside CADO (p.3). The MoC/variational formulation is used
**only** to generate a fixed contour to compare against; the optimizer runs on a black-box RANS solver.
Nobody here keeps the variational formulation and swaps in a modern optimizer. Claim 8 unfalsified,
and now with a strong positive instance of *how close the corpus gets without doing it*.

**T-3 — ADOPT (T-T3 / T-T3-MAP external calibration; MEDIA).**
Their unsteady stage is, by construction, an **H3 instance**: the inlet family is a spatially uniform
step/blowdown in (p₀, T₀)(t) only — "A step in pressure and temperature was imposed at the nozzle
inlet" (p.4), inlet angle fixed at 0°, no spatial profile. The objective omits p_a, so it also sits in
the vacuum corner where our Lemma C affinity degenerates. Simultaneously, **three T3 hypotheses are
broken and named**: H1 fails (temperature-dependent gas properties, p.3, hence γ(T) not one frozen γ);
H2' fails (mild flow separation near the outlet at the end of the pulse, Fig. 8(a) t = 0.38 ms, p.7);
H4 fails (the constraint is genuinely time-resolved URANS, not a family of steady per-phase solutions).
Under exactly this hypothesis-breaking, the measured departure of the cycle-averaged optimum from the
steady/Rao-designed contour is **≈ 2%** (p.7). That is an external, published, order-of-magnitude
calibration for the T3 sharpness statement ("design penalty is second order — envelope theorem") in a
setting far harsher than the theorem's. **Where it grafts:** M0 T-T3-CE / T-T3-MAP sharpness discussion
and the T3-CONTROL protocol register, as the corpus's only measured averaged-vs-steady design gap for a
detonation-fed nozzle. Cite with its caveats (T-11): no bar, single instance, deltas near the
optimizer's own tolerance.

**T-4 — THREAT (value proposition of the whole averaged program; MEDIA).**
The paper's own decomposition of the payoff is uncomfortable for us and must be answered explicitly:
"The performance of the detonation tube was enhanced by **up to 80%** in terms of time-averaged force
by just **adding a shaped nozzle** with respect to the straight duct application. The MOC nozzle showed
**1.5%** increase … compared to the optimized nozzle for steady flow. Interestingly, the optimized
nozzle for unsteady flow delivered about **2%** more time-averaged force than the MOC nozzle" (p.7).
Read adversarially: essentially all the value is in *having* a contoured nozzle; the entire
shape-optimization enterprise — steady, averaged, variational or otherwise — lives inside the last
couple of percent, of the same order as our own in-class datum (claim 19, +0.51%). A reviewer can and
will ask what the cycle-averaged machinery buys.
**Counters of record** (all sourced in this paper): (i) their 2% and 1.5% are **at or below their own
declared unsteady convergence tolerance of 1.2%** (p.5) and carry no error bar and no grid-convergence
study; (ii) their objective drops p_a entirely, and our T-T3-MAP names p_a ≠ 0 as a *first-order*
breaker (Isp average-of-ratios collapsing at the harmonic mean), so their configuration is precisely
the one in which the gap is expected to be smallest; (iii) their regime is < 1 Hz single-pulse, and
they themselves warn that above 100 Hz "nozzle performance may be substantially altered" (p.2), which
is where the RDE lives. The threat is real but is a **framing** threat, not a technical refutation.

**T-5 — ADOPT (bibliographic lead against the declared Russian-corpus blind spot, claim 20; ALTA as a lead).**
Reference 8: **Levin V and Manulovich I, "Optimization of the thrust performance of a pulse detonation
engine", *Combustion, Explosion and Shock Waves* 2010; 46: 418–425**, described on p.2 as: "Levin and
Manulovich⁸ performed a nozzle-shape optimization of conical and parabolic nozzle shapes **using
analytical expressions based on infinitely thin detonation waves**." An analytic thrust-optimization of a
detonation-fed nozzle from the Russian gas-dynamics school is exactly the kind of item our claim-20
blind-spot list warns about (eLibrary/Math-Net/TsAGI-CIAM). **Action:** procure and read before any
G3/PB-2 novelty statement is submitted. Note the description is second-hand (shape *family* fitting on
conics/parabolas, not a free contour), so the prior a-priori threat level is moderate, but it must be
read, not inferred.

### 5.2 FORMALE

**F-1 — CONTAINED, with an explicitly declared non-containment (ALTA).**
Their objective functional is a strict reduction of ours. Our thrust integrand is
f1 = [(p − p_a) + ρW² sin(φ−θ)cos θ / sin φ]·q on a control surface; theirs is
F = ṁ u_exit + p_exit A_exit (p.3). It is our f1 under **three simultaneous restrictions**:
(i) **p_a = 0** (the ambient term is simply absent from their F — a vacuum objective, our Lemma C with
b·P_a dropped); (ii) the control surface is the **flat exit plane** (φ = π/2, θ = 0 on the surface),
*not* the terminal characteristic that Route A **derives** (tan²ψ = 1/(M²−1) ⇒ φ = θ ± α, Rao Eq. (11));
(iii) a **1D mass-averaged reduction** of the surface integral rather than the integral itself.
And the cycle layer is our J = ∫_Ξ F dμ with μ = normalized uniform time — "adding all the instantaneous
forces and then dividing by the total time" (p.3).
**Declared non-containment:** their *constraint* is viscous turbulent (k-ω SST) and, in stage 3, reacting
— outside our S1 inviscid class. This is not a surprise but a confirmation of our own declared Route-A
boundary (Shmyglevskii 1980: the check-surface machinery "dies for dissipative/reacting flow"). So:
objective contained, constraint not; and the paper carries no formal object that could bridge the two.

**F-2 — GAP-CONFIRMS (T-T0, claim 14; ALTA on the quote, MEDIA on the inference).**
Verbatim, p.3: the exit force was preferred over thrust "**to obtain a solution that would be
independent of the phase delay between inlet and outlet**." This is an explicit, published,
practitioner-level recognition that under transient operation the instantaneous thrust **depends on the
surface/phase at which you evaluate it**, and their remedy is to *change the objective* until the
dependence goes away — an engineering workaround, unproven, with no statement of when it is legitimate.
Our T-T0 is exactly the theorem the corpus is missing here: for a single rotating mode the instantaneous
thrust through **every** axisymmetric surface is constant, with the T0-flatness monitor as executable
falsifier. **Use:** cite Ornano p.3 in the paper as the corpus's articulation of the problem T-T0 solves.

**F-3 — CONTAINED at the measure level, non-contained at the reduction level (MEDIA).**
Their loading spectrum is a blowdown: initial nozzle state 0.63 × 10⁶ Pa / 507 K, inlet pulse peaking at
**4.20 × 10⁶ Pa** total pressure and **3700 K** total temperature, purged over **0.054 ms** (pp.4–5),
with the decaying p₀(t), T₀(t) traces of Fig. 5(a),(b). That is the same physical family our D2.3
**Lemma 2 (T-O2)** formalizes — exponential blowdown P_c(ξ) = P_CJ·PR^(−ξ) with ξ ~ U[0,1), giving the
**log-uniform-in-pressure** operating measure. Ornano *imposes* this spectrum as a boundary condition and
averages uniformly in time; **the measure never becomes an object**: it is never named, never
normalized, never varied, no measure-agnosticism is claimed or tested, and there is no reduction to a
phase family of steady states (their evaluator is time-resolved throughout). So: our μ contains their
weighting as the uniform-time special case of a blowdown spectrum, while their *problem* is not a
restriction of (P) because it never admits the per-phase quasi-steady decomposition (P) is built on.

### 5.3 ALGORITMICO

**A-1 — ADOPT / CONTAINED (multi-fidelity staging; ALTA).**
The three-level ladder of Fig. 1 — (a) steady, cheap 2D RANS DoE over a **wide** design space with 5
control points to select the *topology class* ("This step suggested that a divergent shape was
preferable", p.8); (b) unsteady URANS refinement on a **narrowed** population with 4 control points;
(c) high-fidelity 3D reacting **assessment only** — is the practitioner's version of our
seed-then-refine + sector-tournament policy (VI.5: seeds Rao-at-⟨P_c⟩ for the bell, peak design for the
plug, sector tournament for topology). Two things to take and one to fix:
- **Adopt as external precedent** for the D6/VI.5 staging narrative: an independent group, on the same
  physical class, converged on "steady screen first, unsteady refine second, high fidelity last".
- **Adopt the explicit DOF ladder** (5 → 4 control points as fidelity rises) as an argument in the
  choice ledger for our own screening tier.
- **What we supply that they do not**: their stage-1 → stage-2 transfer is an *undeclared* nesting
  assumption (hypothesis 10 above). Our **T-T3** is precisely the theorem that says when a steady design
  is the cycle-averaged answer (and **T-T3-MAP** says when it is not); our **T-T4** is the nesting
  theorem for the plug. No certificate whatsoever is transported between their stages.

**A-2 — GAP-CONFIRMS (empty niche / adjoint gap at the algorithmic level, claims 1 & 8; ALTA).**
Method of record: "A wide design space was explored via a **differential evolution** algorithm. A CFD
simulation was performed for each design selected by the optimizer. **No surrogate models were used**
during the optimization" (p.3), with **88 direct CFD evaluations** in the steady stage (Fig. 3) over
**5** design variables (p.4), dropped to **4** for the unsteady stage (p.2). This is derivative-free
optimization at its natural ceiling: 4–5 DOFs is what an 88-evaluation population budget buys against a
50k-cell URANS. It is direct support for our choice-ledger position that adjoint/AD differentiability is
what unlocks the spline-DOF count (our design vector: attachment angle θ_B plus clamped spline wall
nodes, driven by TR-SQP with Riesz-represented gradients). No adjoint, no shape derivative, no Hadamard
density appears anywhere in the paper.

**A-3 — GAP-CONFIRMS (Verdict discipline, VI.6; supports our bars/multiplier reporting; ALTA).**
The certificate content of the paper is empty and, in one place, self-contradicting:
- Steady stage terminated because "the force did not improve any further within **0.02%**" (p.4) —
  stagnation, not optimality; no KKT residual, no Hessian, no multiplier.
- The reported steady optimum sits **on the box bound**: "an exit radius corresponding to **the maximum
  allowed by the design space** (R_exit = 0.0375 m)" (p.4). The binding constraint's shadow price is
  never reported, so the reader cannot tell how much of the "optimum" is physics and how much is the box.
  This is exactly the pathology our VI.5 rule ("multipliers reported as MARGINAL VALUES") exists to kill.
- Unsteady stage terminated at a **1.2%** inter-population difference (p.5), while the *headline
  scientific deltas* the paper then reports are **1.5%** and **≈2%** (p.7). The claimed effects are of
  the same size as the declared convergence tolerance, with no bar and no grid-convergence study for the
  optimization mesh.
This is the clean external justification for "nothing ships outside a Verdict" — and it is also the
principal reason the T-4 threat above should not be conceded on the numbers.

## 6. Corrections / citation hygiene

**C-1 — CORRECTION (pre-emptive, for our litmap; ALTA).**
p.4 states: "the MOC-based design and the steady-optimized configuration delivered the same
mass-averaged exit force (**5.689 kN** for the MOC and **5.690 kN** for the steady optimization),
**proving the validity of Rao's method for steady-flow optimizations**." This sentence is an
**assertion**, not a proof, and if it ever enters our lit-map as "external validation that the Rao
contour is optimal" it must carry three qualifiers, all sourced in the same paragraph:
1. The compared geometry is **not** an MoC-exact Rao contour but "a **second-order quadratic
   polynomial** as recommended by Rao¹³" (i.e. the ARS-1958 chart/approximation route, ref 13).
2. The equality is of the **objective at two geometries** on one instance; the paper itself notes the
   fields differ — "we observe that the **MOC actually has a less uniform flow field**" (p.4) — and no
   error bar is attached to a 0.02%-level agreement produced by a 50k-cell RANS whose grid convergence
   was never demonstrated.
3. The evaluation is **viscous turbulent RANS**, while Rao's construction is inviscid; a coincidence of
   objective values across a model mismatch cannot "prove validity" of an inviscid variational method.
Correct usage: "Ornano et al. (2017) report that a viscous-RANS DE optimum and a Rao-approximation
contour of the same length and area ratio deliver mass-averaged exit forces agreeing to ≈0.02% on a
single H₂-air detonation-tube case."

**C-2 — CORRECTION (internal to the paper, to be quoted correctly).** See §3: the "2%" is attributed to
different baselines in the abstract/conclusion (vs steady design) and in the body (vs MOC nozzle). Only
the body's chain (straight duct → steady-opt → +1.5% MOC → +2% unsteady-opt) may be cited.

## 7. Bibliography inspection (record datum)

References 1–23, plus Appendix 1 (Notation). Full list scanned.

**Classical variational-nozzle line:**
- **Rao — CITED, twice.** Ref 11: Rao GVR, "Exhaust nozzle contour for optimum thrust", *J Jet Propul*
  1958; **28**: 377–382. Ref 13: Rao GVR, "Approximation of optimum thrust nozzle contour", *ARS J*
  1958; **28**: 561.
- **Guderley — ABSENT. Hantsch — ABSENT. Hoffman — ABSENT. Kraiko — ABSENT. Shmyglevskii — ABSENT.**
  Also absent: Zucrow–Hoffman, Sirazetdinov, Nikol'skii, Rao–Beck, Scofield–Hoffman, Kraiko–Osipov.
  The classical line is represented **only** by Rao, and only as a contour-generating recipe.

**Modern adjoint / shape-optimization line:**
- **Lions — ABSENT. Pironneau — ABSENT. Jameson — ABSENT. Giles — ABSENT. Lozano — ABSENT.**
  No adjoint, continuous or discrete; no shape derivative; no Hadamard formula; no sensitivity analysis
  of any kind. The only optimization-methodology reference is ref 12, Verstraete T, "CADO: a computer
  aided design and optimization tool for turbomachinery applications", EngOpt 2010 — a derivative-free
  evolutionary framework.

**Adjacent detonation/nozzle line present:** Cambier (ref 3, JPP 1998), Daniau et al. (ref 4), Ruhul
Amin et al. (ref 5), Kailasanath (ref 6), Falempin et al. (ref 7, AIAA 2003-3815), **Levin & Manulovich
(ref 8, CESW 2010 — see finding T-5)**, Billings (ref 9, NASA MSFC technical report, "PDE nozzle
optimization using a genetic algorithm"), Ma, Choi & Yang (ref 10, JPP 2005), Driscoll et al. (ref 1,
RDE injection), Frolov et al. (ref 2). Numerics/chemistry: Ettner (refs 17, 22), Thomas (ref 18),
O'Conaire (ref 19), Chemkin (ref 20), Stewart & Lightfoot (ref 21), Giurao et al. (ref 23),
Gaathaug (14), Heidari & Wen (15), Wang et al. (16).

**Record statement:** this paper sits entirely in the *detonation-propulsion + evolutionary-CFD-optimization*
literature. It touches the classical variational line at exactly one point (Rao, as a baseline contour)
and the modern adjoint line at **zero** points. It is therefore a clean confirmation that the two
literatures our program joins are, in this corner of the field, still unjoined.

## 8. Bottom line for the program

- **No claim of ours is refuted by this paper.** G3, PB-2, claims 1, 4, 5, 8, 14 all survive; nothing
  here derives an optimality condition, and the MoC/variational formulation is never optimized.
- **Two claims gain positive external support**: G3/claim 7 (the authors state the void themselves,
  p.2 and p.8) and claim 8 (both ingredients present, never combined).
- **One real threat, of framing not of substance** (T-4): +80% from having a nozzle vs ≈+2% from
  optimizing its shape. Answer it in the paper explicitly, with their own p_a-free, <1 Hz, tolerance-
  sized-delta caveats on the table.
- **Three concrete actions**: (i) procure and read Levin & Manulovich, CESW 2010; 46: 418–425 (T-5);
  (ii) register Ornano's ≈2% as the external calibration datum in the T-T3 sharpness / T3-CONTROL
  register (T-3); (iii) add the citation-hygiene note C-1 to the lit-map before any use of the
  5.689/5.690 kN coincidence.
