# The final scheme: certified shape optimization of the RDE exhaust for generic transient periodic flow (D5 — expert-panel synthesis)

Status: DELIVERABLE D5 (2026-07-16). Output of a 16-agent adversarial
panel workflow (5 disciplinary proposal lenses: PDE analysis, dynamical
systems, adjoint/optimization, gasdynamics, original-formulations
maverick; 2 refutation referees per proposal — mathematical rigor and
2026 computational feasibility; 1 synthesis judge), each with web access
and the full-literature mandate (classical Rao/Guderley/Kraiko/Hoffman +
SOTA), on top of the D1-D4 deliverables. Problem as posed: the flow is a
GENERIC transient periodic/quasi-periodic/multistable/mode-hopping 3-D
reacting flow (steadifiability NOT assumed); required output = the
constrained optimal shape Sigma* with active multipliers and
certificates. Citations marked VERIFIED were web-checked during the run.

------------------------------------------------------------------------------

# FINAL SCHEME — Certified Shape Optimization of the RDE Exhaust (Synthesis)

**Verification run (this session, 3 searches):** (a) no adjoint-based RDE nozzle shape optimization exists — 2022–2026 literature is parametric/CFD-in-the-loop only ([NASA Paxson CFD optimization](https://ntrs.nasa.gov/api/citations/20220006164/downloads/Aviation_2022_final.pdf), [JPP nozzle design](https://arc.aiaa.org/doi/10.2514/1.B38539), [PDE-nozzle MOO 2025](https://doi.org/10.3390/aerospace12060502)) — novelty of the assembled scheme CONFIRMED; (b) closest tracked-adjoint prior art remains steady goal-oriented ISHT ([arXiv:2405.00904](https://arxiv.org/pdf/2405.00904)) — unknown-(Ω,T) periodic coupling still unpublished; (c) decision-dependent DRO exists in finite dimensions ([Luo–Mehrotra, arXiv:1806.09215](https://arxiv.org/abs/1806.09215)) — the μ(Σ) objection is answerable by prior art, upgrading Step 7 below.

## 1. FINAL SCHEME

**Step 0 — Modeling ledger (all closures declared up front).** Reactive Euler backbone + declared viscous layer; **ZND/CJ jump closure for the tracked primary front, cellular substructure explicitly regularized** (gasdynamics-refutation demand); base-pressure model for truncated plugs *with its own adjoint*; **Σ-dependent feed admittance BC** (Marble–Candel; maverick-refutation flaw 5); **initialization protocol** making J[Σ] well-defined under hysteresis (rigor-refutation of gasdynamics, flaw 5). A = spline contours, attachment/L/ε_max/truncation/κ bounds; compactness via uniform cone/curvature (Henrot–Pierre, MEMORY); existence of Σ* stated as **conditional hypothesis**, with Γ-convergence phrasing retained for the quasi-steady bridge. Rigor: SCHEMA. Cost: nil. Falsifier: audit that no undeclared closure enters downstream.

**Step 1 — Mode census & tier assignment** *(dynamics, gasdynamics)*. Capturing LES/SAMR runs at Σ₀ over the envelope; Poincaré sections + Koopman atoms classify: RE (k co-rotating waves) / RPO (modulated, counter-rotating) / quasi-periodic / chaotic-hopping; hysteresis map under the declared protocol. Exact Z_k symmetry of k-wave modes is **checked, not assumed** (rigor refutation: unequal spacings generic). Rigor: PRACTICE. Tool: SAMR solvers + DMD ([Koch–Kutz, arXiv:1908.03116](https://arxiv.org/abs/1908.03116), VERIFIED by lens). Cost: the hidden dominant item — O(10) LES runs, 10⁵–10⁶ CPU-h each; amortized once, re-run only per accepted trust-region step (Step 7). Falsifier: tier flip mid-optimization → restart at new tier.

**Step 2 — Tier RE production engine: freezing + tracked bordered adjoint** *(all lenses converge here; this is the deliverable path)*. Wave-frame steadification (T0; Z_k sector conditional on verified symmetry — SCHEMA, not theorem). Axisymmetric wall default. Discretize with steady implicit shock tracking (Zahr–Persson line, VERIFIED), **hybrid: fit the primary detonation/oblique-shock surfaces, capture cellular fine structure** (gasdynamics-feasibility salvage) — Giles–Ulbrich pathology removed for the fitted set, residual capturing error audited by finite differences. Bordered system: unknowns (U, mesh, Ω) + phase condition; bordered adjoint gives the shape gradient including Ω-sensitivity (dynamics lens; BVP-level prior art Ahsan–Dankowicz–Sieber, VERIFIED by lens). Hypotheses: attracting RE exists; S1-class piecewise-smooth flow; fixed fitted-front topology per SQP step. Rigor: per-phase Rao/Kraiko/Hoffman conditions THEOREM (2-D/axisym, S1 class); multi-D shape derivative SCHEMA (theorem only 1-D Ulbrich); tracking convergence PRACTICE. Cost: runnable today at 10⁵–10⁶ DOF sector solves; ~10⁶ CPU-h per converged design loop. Falsifier: **T3/T4 oracles reproduced to tolerance before any general run** (background theorems; all lenses).

**Step 3 — KKT solve → Σ*.** Reduced-space active-set SQP (full-space LNKS deferred — two immature solvers composed, adjoint-opt feasibility refutation) on (Σ, multipliers): averaged Hadamard wall residual, weighted endpoint transversality, corner conditions, complementary slackness on L/ε_max/truncation/κ. Topology events of the fitted front treated as **trust-region boundaries with re-seeding**, not differentiated through (concedes rigor-refutation flaw: gradient exact only between events). Output: **Σ\* with active multipliers λ_L, λ_ε, λ_trunc = marginal constraint values**, cross-validated by Danskin finite differences and constraint continuation. Rigor: finite-dim KKT sensitivity THEOREM (discretized problem only — honest label per refutation); function-space SCHEMA.

**Step 4 — Tier RPO demonstrator (2-D+t unrolled annulus)** *(maverick element B, surviving both refutations at reduced scope)*. Space-time ISHT on the periodically identified slab ([Naudet–Zahr, arXiv:2308.04065](https://arxiv.org/abs/2308.04065), VERIFIED) posed as periodic BVP with **unknown (Ω, T), two phase conditions, doubly bordered adjoint**. Feasible only 2-D space + time (no 4-D simplex tooling exists — unanimous feasibility verdict); 3-D RPO deferred to research program. Rigor: PRACTICE-WITHOUT-THEOREM (continuous-limit correctness = the open O(1) homogenization). Falsifier: reproduce imposed-frequency HB adjoint (Krakos) in the locked limit.

**Step 5 — Certificate stack** *(adjoint-opt assembly format + dynamics 6(c), post-refutation labels)*. (a) Stationarity: KKT/phase-adjoint residuals. (b) S1 membership: Sternin/Rao–Beck boundary function — **declared 2-D/axisym-only instrument**. (c) DWR error bars on J and gradient — labeled PRACTICE (shocked-adjoint delta-sheets). (d) Second-order: reduced-Hessian spectrum; Floquet demoted from gate to **monitored diagnostic** (essential-spectrum objection, Texier–Zumbrun — VERIFIED by lens). (e) **Dynamic-consistency certificate: post-hoc capturing DNS at Σ\*** confirming branch existence, wave count, and J within error bar (dynamics 6(c), demoted per feasibility refutation from Floquet gating to re-simulation). (f) Global bracket: Efremov–Kraiko/shared-wall relaxation gap δ — **valid only under quasi-steady hypotheses, labeled diagnostic in tiers RPO+** (rigor refutation accepted). Rigor: residual computability THEOREM; interpretation conditional on S1.

**Step 6 — Non-axisymmetry pricing rule** *(adjoint-opt element 4, survived)*. Non-axisym Σ destroys SO(2)-equivariance: no RE exists; wave-locked states exist only inside Arnold tongues, else quasi-periodic (rigor refutation accepted and incorporated). Price: freezing forfeited, one full tier jump to Step 4 machinery (2-D+t only today) — non-axisymmetric designs admissible but currently affordable only as perturbative studies. Rigor: SCHEMA (triage logic), CONJECTURE (torus case).

**Step 7 — Multistability outer layer** *(gasdynamics S5 + pde-analyst Step 6, rebuilt per refutations)*. **Finite enumerated branch table** (not continuation families): each stable mode from Step 1 optimized per-branch via Steps 2–4. Outer objective: CVaR_β over mode measure μ with **decision-dependent DRO** ambiguity (finite-dim theory exists — Luo–Mehrotra, VERIFIED this run; PDE application new): μ frozen within a trust region, **census re-run after each accepted step** (gasdynamics alternation), ball radius tied to census sampling error. Bifurcation-variety localization retained as heuristic budget allocator with global-bifurcation caveat (dynamics element ii, post-refutation). Rigor: SCHEMA (outer program), PRACTICE (μ estimation), CONJECTURE (μ locally constant). Cost: ×N_modes × census.

**Step 8 — Chaotic/mode-hopping death certificate.** NILSS/NILSAS rejected (shocks void shadowing; CLV count prohibitive — unanimous). Deliverable degrades to: robust surrogate optimization on the branch table + bound-ladder bracket; **no stationarity certificate**. Statistical-solution-constrained optimization: OPEN. Rigor: honest refusal. [S14 note (PAN-S14 addendum PP-2, arbiter-confirmed): the bracket's upper wall (Prop. G-B) is proven steady-per-streamtube only; its transfer to the ergodic targets [J_exact^-, J_exact^+] (M0 D2.2) is a named missing lemma — until then the bracket on THIS row carries Step 5(f)'s quasi-steady-only label.]

## 2. GENERALITY LADDER

| Flow class | Deliverable | Rigor of chain |
|---|---|---|
| Single/k-wave RE, axisym wall, S1-regular | Σ* + multipliers + full certificate (a–f) | Per-phase conditions THEOREM; shape derivative SCHEMA; runnable 2026 |
| RPO (modulated/counter-rotating), 2-D annulus model | Σ* + certificate (a,c,d,e) | PRACTICE-WITHOUT-THEOREM; demonstrator scale |
| RPO/torus, full 3-D; non-axisym Σ | scheme defined, not executable (4-D tracking absent) | SCHEMA on paper; CONJECTURE (torus) |
| Finite multistable mode set | robust Σ* (CVaR/DD-DRO over branch table) + per-branch certificates | SCHEMA outer / CONJECTURE on μ |
| Chaotic / mode-hopping / measure-valued | bounds + robust surrogate only; no certificate | OPEN |

## 3. ORIGINAL ELEMENTS

**Survived vetting:**
1. **Freezing + implicit-shock-tracking bordered shape adjoint for the RE class** (dynamics; gasdynamics) — survived both feasibility refutations as *the* runnable core; absence of prior art re-confirmed this run.
2. **Unknown-(Ω,T) periodic-BVP tracked adjoint** (maverick B; pde-analyst 2; adjoint-opt 1) — survived at 2-D demonstrator scope; 3-D killed by tooling.
3. **Non-axisymmetry pricing rule** (adjoint-opt) — survived, corrected by the Arnold-tongue objection.
4. **Dynamic-consistency certificate** (dynamics iii) — survived, demoted from Floquet gating to post-hoc DNS re-simulation.
5. **Hybrid fit-primary/capture-cellular tracking** (gasdynamics-feasibility salvage) — survived the cellular-instability objection by construction.
6. **Trust-region census↔gradient alternation with decision-dependent DRO** (gasdynamics d + this synthesis) — the circularity objection (μ depends on Σ) answered by existing finite-dim DD-DRO theory; PDE application new.
7. **Bifurcation-variety localization of nonsmoothness** (dynamics ii) — survived as heuristic only.

**Killed:**
- Relative-entropy a-posteriori certificate + convex-integration alarm (pde-analyst 1, 3): Gronwall e^{CT} vacuous; Lipschitz comparison hypothesis violated by the shocked orbit itself.
- Unsteady Rao–Hoffman space-time control hypersurface (maverick A): rotating shock sweeps it generically — domain empty.
- Shape-simultaneous moment-SOS bound (maverick D): non-polynomial data, SDP explosion beyond scalar 1-D.
- Floquet-margin path constraint as gate (adjoint-opt 2): essential spectrum, dense instability, nonsmooth at folds.
- NILSS/NILSAS chaotic gradients (all lenses): shadowing hypotheses fail across shocks.
- Torus time-spectral adjoint (adjoint-opt 3): cited prior art assumes known frequencies; small divisors untouched.

## 4. THREE HARDEST OPEN POINTS

1. **Multi-D shape calculus through shock topology events.** Differentiability of J in Σ for shocked multi-D (reactive) Euler is proven only in 1-D (Ulbrich/Bressan–Marson); triple-point birth/merger recurs every period and every design step. Everything above operates *between* events by fiat.
2. **The transient→orbit bridge.** No existence/selection theory for time-periodic 3-D reacting Euler solutions (Temple–Young is shock-free small-amplitude), and O(1) time-homogenization of the long-time average onto a mode measure is a physical ansatz — every rigor label downstream of Step 1 is conditioned on it.
3. **μ(Σ) and attractor certification.** The mode measure is hysteretic, history- and protocol-dependent; no theory ties basin weights to geometry, and no instrument certifies that the optimized invariant solution is the physical attractor (essential spectrum blocks Floquet; statistical-solution optimization has no theory).

## 5. VERDICT

Genuinely new as posed. Every load-bearing component is prior art in isolation — Kraiko-school per-phase design, freezing with eigenvalue Ω, implicit shock tracking, unknown-period LCO adjoints, CVaR/DRO — but their composition into a *constructive, certificate-bearing* pipeline for shape design constrained by symmetry-reduced shocked invariant solutions of reacting Euler has no publication: this run re-confirmed that RDE nozzle optimization literature is entirely parametric CFD, and that no periodic-BVP shock-tracking adjoint with unknown (Ω,T) exists. The problem is not a routine transfer because the three open points above are *structural*, not incremental: the field lacks the shocked multi-D shape-derivative theorem, the periodic-solution existence theory, and the decision-dependent attractor-selection theory that the full generality of the posed question requires. What is new-and-solvable in 2026 is the RE-class production engine (Steps 2–3) and the 2-D RPO demonstrator (Step 4); what is new-and-open is precisely the rest.

Sources: [arXiv:2405.00904](https://arxiv.org/pdf/2405.00904) · [NASA Paxson](https://ntrs.nasa.gov/api/citations/20220006164/downloads/Aviation_2022_final.pdf) · [JPP B38539](https://arc.aiaa.org/doi/10.2514/1.B38539) · [Aerospace 12(6):502](https://doi.org/10.3390/aerospace12060502) · [arXiv:1806.09215](https://arxiv.org/abs/1806.09215) · [arXiv:2308.04065](https://arxiv.org/abs/2308.04065) · [arXiv:1908.03116](https://arxiv.org/abs/1908.03116)

------------------------------------------------------------------------------
## ANNEX A — The prescribed-profile convergent pipeline (detonation profile GIVEN as data)

Setting: the detonation/chamber side is prescribed on the design
interface Gamma_d — either a phase family s(xi) (I2) or a wave-frame
steady 3-D field (I1). Cutting the domain moves the detonation from
STATE to DATA: cellular substructure and triple points live upstream of
the cut, inside the data generator. Price (ledger rows): H-I2 (no mean
upstream influence — auditable), H-F1 (frozen family — recovered by
Stage G), R1-R3 (data contract). Shocks REMAINING in the design region:
(1) the inherited oblique sheet entering with the data — single,
transversal, FITTED per phase (adjoint-consistent by construction, no
Giles-Ulbrich pathology, no cellular birth since chemistry is frozen);
(2) wall coalescence — the S1 boundary, MONITORED (Sternin/Rao-Beck
boundary function), not suffered; (3) the plug free jet boundary
(dedicated unit process, Angelino limits as oracle).

| Stage | Object | Well-posedness | Convergence (rate) | Monitor/falsifier |
|---|---|---|---|---|
| A | data admission | admissible-data manifold: characteristic-complete supersonic data; Crocco compatibility of (s, h0, vorticity); single transversal jump; xi-measurability | — (a contract, loud-reject off-manifold data) | Crocco/BV/choking/H-I2 audits |
| B | per-phase forward (MOC, fitted sheet) | classical in S1 domains of determinacy (Li Ta-tsien / Courant-Friedrichs) — THEOREM for C1 data; fitted jump under Majda transversality — SCHEMA (G12 declared) | O(h^2) unit processes | boundary function val>0; dual-backend equivalence |
| C | per-phase gradient | closed-form adjoint (Rao/Kraiko) or reverse-AD of the fitted march (implicit rules on inner solves) | exact to machine precision | dot-product O3; Hoffman E-residual ~ 0 |
| D | xi-quadrature over mu | integrand piecewise-C^k in xi, finitely many switches (separation onset, plug adaptation, sheet entry) | SPECTRAL iff split at located switches xi*(Sigma); O(1/N) if not — and the outer gradient degrades with it | switch localization + Leibniz boundary-term cancellation (F continuous at switches) |
| E | outer shape loop | TR-SQP on spline space, Sobolev/Steklov-Poincare Riesz gradient | global convergence to KKT of the DISCRETIZED problem between topology events; Clarke+bundle at events; mesh-independent | KKT + weighted transversality (**') residuals |
| F | certification | — | — | dual-route B1/B2 agreement; T3/T4 oracles; DWR bar; relaxation-gap bracket |
| G | data-shape outer loop (weak bilevel) | fixed point s -> Sigma*(s) -> s(Sigma*) | LINEAR iff composite Lipschitz constant q < 1; q ESTIMATED (two response-map evaluations), never assumed | q report; q >~ 1 => genuine bilevel (PB-4), out of this pipeline |

Rigor balance: with the profile given and S1 certified, stages A-F are
theorem-or-certificate except the multi-D fitted-shock shape-derivative
theorem (G12, operated as SCHEMA with downstream certificates) and P7
existence (restricted classes). NOT removed by giving the data: the
quasi-steady license — an I2 family carries the O(St) obligation (P4
bar); an I1 single-mode field makes the average exact (T0) but makes the
per-phase 2-D reading an approximation of the 3-D swirling problem (D2
residual). One chooses which error to carry, and measures it.
[Currency note 2026-08-05 (S15, D8 §8 residue, two-lens): the two
named exceptions have since been narrowed of record — within the S1
marching class the multi-D fitted-shock shape-derivative gap is
THEOREM* T-G12S1 (docs/rde_nozzle_G12_S1.md §3 Assembly; residues
R-G12.1..3 named; the general multi-D theorem stays SCHEMA, cf.
Stage B row), and existence holds as THEOREM* T-P7S1 on
margin-certified level sets (docs/rde_nozzle_T7_P7_functionspace.md
§2). Registry classes govern current status; the 2026-07-16 labels
above are the panel's historical record.]
