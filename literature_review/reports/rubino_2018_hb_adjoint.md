# Expert read — Rubino et al. 2018, HB discrete adjoint for quasi-periodic shape optimization

**Reader role:** expert reader, convergence review. **Date:** 2026-08-13.
**File:** `literature_review/rubino_2018_harmonic_balance_adjoint_periodic_shapeopt.pdf`

---

## 1. Citation (verified from the PDF, p. 220 and running heads)

A. Rubino, M. Pini, P. Colonna (Propulsion & Power, TU Delft), T. Albring (Chair for Scientific
Computing, TU Kaiserslautern), S. Nimmagadda, J. Alonso (Aeronautics & Astronautics, Stanford),
T. Economon (Bosch Research and Technology Center, Sunnyvale),
**"Adjoint-based fluid dynamic design optimization in quasi-periodic unsteady flow problems using a
harmonic balance method"**, *Journal of Computational Physics* **372** (2018) 220–235.
Received 5 December 2017; revised 23 May 2018; accepted 6 June 2018; available online 15 June 2018.
DOI: `https://doi.org/10.1016/j.jcp.2018.06.023`. ISSN 0021-9991. Open access, CC BY.
Keywords (p. 220): Unsteady optimization; RANS adjoint; Harmonic balance; Quasi-periodic.

## 2. Read coverage

**16 of 16 pages read integrally** (journal pagination 220–235), bibliography included
(refs [1]–[29] on p. 234, refs [30]–[46] on p. 235). Nothing skipped. No supplementary material
is referenced by the paper. Figures were read as rendered images (Figs. 1–15); numerical values
quoted below are those printed in the body text, tables and captions, never read off a plot.

---

## 3. What the paper actually does

**Problem.** Shape optimization of a fixed geometry whose flow is *quasi-periodic* — driven by a
finite set of dominant frequencies that need **not** be integer multiples of a fundamental
(abstract, p. 220; intro p. 221). Objective = a **time-averaged** (period-averaged) aerodynamic
functional. Two cases: (i) NACA 64A010 pitching at two non-harmonically-related frequencies,
inviscid, transonic; (ii) T106D-EIZ axial turbine cascade, fully turbulent (SST), with unsteady
inlet conditions.

**Flow model.** Compressible Navier–Stokes in ALE form, semi-discrete Eq. (1)–(4) with viscous
stress Eq. (5); Boussinesq eddy-viscosity closure, `mu = mu_l + mu_t`, `kappa = kappa_l + kappa_t`
(p. 222). Turbulence: SST (Menter, ref. [43]) for the cascade; the airfoil case is inviscid.
Finite volume, second order: JST for the airfoil convective fluxes, Roe for the cascade, MUSCL
option, corrected average-of-gradients for viscous fluxes (p. 225, p. 228). Shocks are
**captured**, not fitted (Mach contours Fig. 5, "strong shocks", p. 227).

**Formulation (harmonic balance).** DFT/IDFT matrices `E`, `E^-1` Eq. (11)–(12); `N = 2K+1` odd
time instances (p. 222, "to prevent numerical instabilities [34]"); spectral time-derivative
operator `H = E^-1 D E` Eq. (20) with `D = diag(0, i w_1, …, i w_-1)` Eq. (19), so
`D_t(U~) = H U~` Eq. (21). **Key structural point (p. 222, text after Eq. (14)):** if the `f_k`
are not multiples of `f_1`, *"it is not possible to obtain an analytical expression for the
corresponding inverse matrix"* — `E` is therefore built by **Gaussian-elimination inversion of the
analytic `E^-1`** (p. 223, text after Eq. (20)). Time-domain HB per instance Eq. (22)–(26); a
**semi-implicit, segregated** solve Eq. (27)–(28) moves the off-diagonal spectral coupling
`H_{n,k}, k != n` to the right-hand side. "an unsteady flow problem characterized by K frequencies
requires that the solution of 2K+1 nonlinear systems of equations need to be computed" (p. 223).
Implemented in **SU2** [25,26].

**Unknowns.** Primal: the conservative states `U_n`, n = 0…N-1, at the N time instances (each a
full CFD field), plus the N deformed grids `X_n`. Dual: flow adjoints `lambda_n` and mesh adjoints
`mu_n`. Design: `alpha` — 50 Hicks–Henne bump amplitudes on upper and lower airfoil surfaces
(p. 227); 16 free-form-deformation parameters for the blade (p. 230).

**Objective and constraints.** `J` is the **spectral average over the resolved time instances**,
Eq. (32) `J = f(J(U_1,X_1), …, J(U_N,X_N))`, evaluated through the spectral interpolation
Eq. (42) `Gamma* = E*^-1 (E Gamma)`.
Airfoil, Eq. (44): minimize `c_d` s.t. `c_l = c_l0`, `delta_max = delta_max0`, plus the N HB state
equations `U_n = G_n` and the N mesh equations `X_n = M_n`.
Cascade, Eq. (47): minimize the time-averaged total-pressure-loss coefficient `zeta_P` (defined by
Eq. (45) with mixed-out boundary averages [44]) s.t. `alpha_out < alpha_out0 + 4 deg`,
`delta_t = delta_t0`, plus the same state/mesh equations.

**Adjoint derivation (§2.4, p. 224).** The HB solve is recast as a **fixed-point iteration**
`U_n^{q+1} = G_n(U^q)` Eq. (29), contractive by assumption, with the converged state characterized
by Eq. (30). The design problem Eq. (31) is Lagrangian-augmented Eq. (33); the differential
Eq. (35) yields the two stationarity conditions: the **flow adjoint** Eq. (36)
`(dJ/dU_n)^T + sum_k lambda_k (dG_k/dU_n)^T = lambda_n`, and the **mesh adjoint** Eq. (37)
`(dJ/dX_n)^T + lambda_n (dG_n/dX_n)^T = mu_n`. Eq. (36) is itself iterated as a fixed point,
Eq. (38) `lambda_n^{q+1} = dN/dU_n (U_n*, lambda^q, X_n)`, with the **shifted Lagrangian**
`N = J + sum_n lambda_n G_n^T` Eq. (39). **Duality preservation** is the claim of Eq. (40):
`|| d/dlambda_n (dN/dU_n) || = || (dG_n/dU_n)^T || = || dG_n/dU_n || < 1`, hence
*"(38) will converge at the same rate as the primal flow solver"* (p. 225). Final gradient
Eq. (41): `dL^T/dalpha = dJ^T/dalpha = mu_n dM_n^T(alpha)/dalpha`.

**Solver / tooling.** Right-hand side of Eq. (38) is produced by **algorithmic differentiation of
the source code**, AD tool **CoDiPack** [29,39], reverse mode, *"Jacobi taping method in
combination with the Expression Templates feature of C++, leading only to a small runtime
overhead"* (p. 225). Optimizer: **SLSQP**, *"a modified version of the nonlinear least-squares
method"*, Kraft's DLR package [38] (p. 225). Mesh deformation `M_n(alpha)` is a declared
differentiable function (p. 224).

**Verification.** (a) HB primal vs second-order dual-time-stepping time-accurate URANS: Fig. 2
(airfoil `c_l`, `c_d` vs number of instances; RMSE of `c_l` = 0.00275 with 2 input frequencies;
time-averaged `c_d` = 0.0027 for 5 instances vs 0.0028 for 9/11/13 and 0.0028 time-accurate,
p. 226), Fig. 8a and Fig. 13a (cascade `zeta_P`; RMSE 0.010 with 5 instances, p. 229; Table 4:
RMSE 0.041 with 5 instances and 0.019 with 7 for OptC2). (b) Steady CFD vs experiment [42],
Fig. 7, good agreement except near `x/l = 0.75` (p. 229). (c) **Gradient verification: adjoint AD
vs second-order central finite differences** — Fig. 3a over 8 Hicks–Henne bumps (airfoil),
Fig. 9a/9b for the cascade with *"RMSE = 2 · 10^-5"* (p. 230, p. 233). (d) Adjoint convergence
histories Figs. 3b, 8b, 13b showing the adjoint residual tracking the primal.

**Headline results.** Airfoil: ~50% time-averaged drag reduction at constant `c_l` and thickness
within 1% (p. 227); the *steady*-optimized airfoil, when subjected to the same pitching, gives only
44% (p. 228). Adjoint/primal cost ratio ≈ 1.3, 0.28 s per primal iteration on 4 cores Xeon E5-1620
(p. 227). Cascade OptC1 (wake-resolving, spatially non-uniform unsteady inlet): peak `zeta_P`
reduced 44%, signal amplitude 54%; adjoint/primal cost ratio ≈ 1.7, 1.41 s per primal iteration
(p. 230–231). Cascade OptC2 (spatially uniform, time-fluctuating inlet total pressure Eq. (48),
two non-commensurate frequencies): ~14% reduction of average `zeta_P`, amplitude −44%, peak −29%
(p. 233). HB with 5 instances ≈ **9× faster** than the time-accurate run over five periods
(p. 229–230).

---

## 4. Hypotheses

### Declared
- H-a. Cell volumes `Omega` and boundaries move without deforming; `v = u_Omega` on `dOmega`
  (Eq. (2), p. 221) — rigid-body ALE.
- H-b. Flow is **quasi-periodic**: representable by a finite set of `K` dominant frequencies,
  known a priori (abstract; selected here by spectral analysis of the time-accurate solution,
  Fig. 1b, Table 2, Table 4).
- H-c. `N = 2K+1` odd (p. 222).
- H-d. Boussinesq hypothesis for turbulence (p. 222); fully-turbulent computation, transition not
  modelled — *"since the present work aims to assess the methodology for design optimization only,
  the computations are performed assuming fully-turbulent conditions"* (p. 229).
- H-e. `G_n` is a **contraction**, `||dG_n/dU_n|| < 1` (p. 224, before Eq. (30); reused in Eq. (40)).
- H-f. `M_n(alpha)` is a differentiable mesh-deformation map (p. 224).
- H-g. Perfect-gas-like closure implied by SU2's default thermodynamics (never stated; the group's
  non-ideal-gas variant is ref. [30], not used here).
- H-h. A "pseudo-period" `T` exists and a uniform sampling within it is admissible; the optimal
  `T_opt/T_0` is selected by the algorithm of ref. [40] (p. 226, Table 2).

### Undeclared but necessary
- U-1. **The contraction assumption is never verified**, in either test case. Eq. (40) is a
  *conditional* statement whose antecedent is asserted, not measured. The whole "duality-preserving"
  rate claim rests on it.
- U-2. **Exact primal convergence**: Eq. (38) uses `U_n*`, the exact fixed point. The gradient is
  the gradient of the *converged* problem; the effect of a finite primal residual on gradient
  accuracy is not analysed (only shown to be small by the FD comparison).
- U-3. **Differentiability of `J` in `U`** — but `c_d` and `zeta_P` are evaluated on a flow field
  containing **captured shocks** and, in the cascade, a separation region (p. 230). Differentiability
  of the *discrete* objective holds; differentiability/convergence of the *continuous* shape
  derivative across captured shocks is neither claimed nor examined.
- U-4. **Invertibility and conditioning of `E`** for non-commensurate frequencies. The paper needs
  `E` numerically (Gaussian elimination, p. 223) and imports an "optimal time period" algorithm
  [40] precisely to make this robust (p. 226), but no condition number is reported.
- U-5. **The frequency set is exogenous and design-independent.** Both test cases prescribe the
  frequencies from outside (imposed pitching Eq. (43); blade-passing Eq. (46); imposed inlet
  fluctuation Eq. (48)). Nothing in the formulation handles a frequency that *moves with the
  design*; the design is only checked a posteriori for not introducing new frequencies (p. 231,
  p. 233).
- U-6. **Convergence of the semi-implicit segregated iteration** Eq. (27)–(28): the off-diagonal
  spectral coupling is lagged (Jacobi-style). Stability of this decoupling at high reduced
  frequency is not discussed.
- U-7. The **shape parameterization is the regularizer**: 50 Hicks–Henne bumps / 16 FFD boxes. No
  Sobolev/Riesz representation, no mesh-independence statement, no smoothness constraint on the
  shape beyond what the parameterization enforces.
- U-8. **Existence of a minimizer, uniqueness, and any globality statement are absent.** SLSQP
  returns a local point; Fig. 10a even shows the outlet-angle constraint violated mid-history and
  recovered.

---

## 5. Findings — three-level comparison against the program apparatus

### TEORICO

**F1 — THREAT (partial, scope-narrowing) — touches D2-G3 / claim 7.**
This paper *does* solve, and *does* write down first-order optimality conditions for, "a shape
shared across a family of flow states weighted by a measure, with genuinely unsteady dynamics in
the constraint". The measure is the uniform atomic measure on the N time instances; the objective
is its average, Eq. (32) with Eq. (42); the state constraints Eq. (31) `U_n = G_n(U(alpha),
X_n(alpha))` are **not** N independent steady problems — the spectral operator `H` in Eq. (26)/(28)
couples every instance to every other, so the dynamics in the constraint are genuinely unsteady;
and the OptC1 configuration imposes a **spatially non-uniform, time-dependent inlet boundary
condition** reproducing the wakes of moving bars (p. 229, Eq. (46), Figs. 11a–c), i.e. a
traveling-wave inflow. The stationarity system is Eqs. (35)–(37).
*What survives.* Claim 7 as written says "**variational nozzle theory** … optimality conditions …
**with a T4-type free-boundary counterpart**". This paper is not nozzle theory, and it has **no
free boundary, no endpoint, no transversality condition, no existence result** — the shape lives in
a fixed finite-dimensional parameterization and the conditions are the KKT conditions of a
finite-dimensional NLP. So claim 7 is **not falsified**, but the 2026-08-13 qualification is now
load-bearing in a second way and should be re-worded to say explicitly *continuous* optimality
conditions *with free-boundary/transversality structure*: without that clause the sentence is
attackable by this paper. Confidence ALTA.
Evidence: p. 224 Eq. (31)–(37); p. 229 §3.2.1 and Eq. (46); p. 226 Eq. (42)/Table 2.

**F2 — GAP-CONFIRMS — touches claim 8 (empty niche) and the "non-technological gap" framing.**
The paper is the cleanest available demonstration that the *machinery* for measure-averaged
adjoint shape optimization is mature and industrial (SU2, CoDiPack, SLSQP, turbulent RANS) — and,
at the same time, that **nobody in this line touches the variational nozzle formulation**. The
approach here is the exact opposite of the empty niche: they discard analytic optimality structure
entirely and differentiate a discretized solver. The niche "keep the variational MoC formulation
and swap in a modern optimizer" is *not* occupied by this paper; the paper instead confirms that
the technology which would make it possible exists off the shelf. Confidence ALTA.
Evidence: p. 220 abstract ("A fully-turbulent harmonic balance discrete adjoint formulation based
on a duality-preserving approach is proposed"); the entire bibliography, which contains zero
classical nozzle references (§6 below).

**F3 — CONTAINED (with an active caveat of ours) — touches D2.3 (measure) and VI.4bis (quadrature).**
Their `mu` is the **uniform atomic measure on N instances** — an admissible instance of our
measure-agnostic D2.3 framework, and precisely the case our own D2.3 flags as needing
re-verification ("switch phases mu-null … non-trivially for atomic/empirical ones"). Their own
data is direct evidence for our panel-splitting pin: with the same shape, the *lift* is captured
with 5 instances (RMSE 0.00275) while the *drag* — the objective — requires 9, *"due to the
dominant non-linearities in the flow (shocks). Hence more than five time instances are necessary
for the accurate determination of the drag coefficient"* (p. 226). Uniform sampling of an integrand
made non-smooth in phase by moving shocks converges slowly: exactly the "practical convergence
trap" our VI.4bis names, and their fix is brute-force N, not switch-phase-aware quadrature.
Confidence ALTA.
Evidence: p. 226, §3.1 paragraph beginning "Overall, the agreement of the lift coefficient…";
Fig. 2a vs Fig. 2b.

**F4 — CONTAINED (consistency datum, no threat) — touches T-T3 / claim 2.**
They report a measured non-collapse: the *steady*-optimized airfoil, put through the prescribed
pitching, achieves 44% time-averaged drag reduction whereas the *unsteady* (cycle-averaged)
optimization achieves 50% — *"This shows that the inclusion of unsteadiness is worthwhile in this
case"* (p. 228). This does **not** threaten T-T3: their case violates H1–H4/H2' comprehensively
(moving grid, viscous/turbulent-adjacent objective, shocks moving in phase, objective is drag not
thrust, no pressure-scaling family). It is a useful external corroboration that "cycle-averaged
optimum = steady optimum" fails generically and that T3's collapse really is bought with its
hypotheses, consistent with T-T3-MAP. Confidence ALTA.
Evidence: p. 228, first paragraph.

### FORMALE

**F5 — ADOPT (high value) — touches Lemma-B(ii)/O3.1 and the F2 general engine.**
The **duality-preserving fixed-point discrete adjoint** Eq. (36)/(38)/(39) with the contraction
inheritance Eq. (40) is the exact structural replacement for our Lemma-B(ii) *in the regime where
Lemma-B(ii) does not apply*. Our Lemma-B(ii) is stronger where it holds — the x-block-triangular
fitted march admits an **exact, non-iterative** transposed sweep — but triangularity is a property
of the supersonic marching regime. The moment F2 admits the declared subsonic patches (closures
O1/O2/O3), an elliptic/mixed region, or any iteratively-solved sub-block, the march loses its
triangular order and the exact-transpose argument dies. Rubino's route then gives: (i) an adjoint
that is the *transpose of the iteration*, converging at the primal rate; (ii) **constant memory** —
the iteration is not unrolled onto a tape, only the fixed-point map is differentiated, which is the
same philosophy as our `custom_vjp` implicit unit process but applied at solver level rather than
cell level; (iii) a clean place to hang the averaging operator, since `J` (Eq. (32), the measure
average) sits **inside** the Lagrangian Eq. (33) and is differentiated with everything else.
*Insertion point:* M0 VI.3 (per-phase gradient) as the declared fallback branch for non-marching
patches, and the F2 engine architecture; it also directly serves REQ-NONSTALL, since a fixed-point
adjoint does not require a well-posed march to exist. Confidence ALTA.
Evidence: p. 224 Eq. (36)–(39); p. 225 Eq. (40) and the sentence *"(38) will converge at the same
rate as the primal flow solver"*.

**F6 — CONTAINED (their certificate is strictly weaker than ours) — touches claim 13 / O3.1.**
Their only gradient certificate is **adjoint-AD vs second-order central finite differences**:
Fig. 3a (8 Hicks–Henne bumps, normalized `dc_d/dalpha`) and Fig. 9a/9b with *"RMSE = 2 · 10^-5"*
(p. 230, restated p. 233). There is **no transposition/dot-product identity**, no derived
tolerance, and no negative control. An FD comparison at RMSE 2e-5 on *normalized* gradients over 8
of 50 (resp. some of 16) design variables cannot separate a correct transpose from a
consistently-wrong one, and it inherits FD step-size error. Our O3.1 (`|<w,Jv> - <J^T w, v>| =
2.7e-10` vs derived tolerance 5.1e-8 over the entire march, with a seeded-corruption rejector) is
strictly stronger and covers the whole operator rather than a few directions. This is a defensible
SOTA-superiority datum for claim 13, and it should be recorded as such rather than assumed.
Confidence ALTA.
Evidence: p. 227 Fig. 3a and caption; p. 230 Fig. 9 and caption; p. 230 text "RMSE = 2 · 10^-5".

**F7 — THREAT-to-adoption / confirms our fitted-front pin — touches VI.3 (Giles–Ulbrich/Lozano rejection).**
The airfoil case is transonic with *"strong shocks"* (p. 227, Fig. 5) which **move in phase**, and
the gradients are obtained by AD through a **captured** JST discretization; the cascade uses Roe.
Nothing in the paper addresses whether the discrete gradient of a captured-shock functional
converges to the continuous shape derivative under refinement — the FD check only establishes
*discrete* consistency (it compares two evaluations of the same discretization). **Giles, Ulbrich
and Lozano are not cited anywhere** (§6). This is not an error in their own frame — the discrete
adjoint is exactly right for the discrete problem — but it means the *flow-side* of this paper
cannot be adopted into our pipeline without violating our standing rejection of captured-shock
adjoints. Adopt the adjoint architecture (F5), not the shock treatment. Confidence ALTA.
Evidence: p. 225 ("the JST scheme [32]"), p. 227 ("attenuation of the strong shocks"), Fig. 5;
reference list pp. 234–235.

**F8 — CORRECTION (to any optimistic reading of the "duality-preserving" guarantee).**
Eq. (40) is a **conditional theorem, with its hypothesis unverified in both test cases**. The chain
is: *if* `||dG_n/dU_n|| < 1`, *then* the adjoint fixed point Eq. (38) converges at the primal rate.
The paper never measures the contraction factor; the empirical support is the residual histories
(Figs. 3b, 8b, 13b) and the measured cost ratios 1.3 / 1.7, which are *observations*, not proof.
If we cite this work in our litmap as "duality preserved / rate inherited", we must carry the
conditional, exactly as we carry `[C-MAJDA]` and `[C-HT4]`. Additionally the derivation assumes the
primal fixed point is reached exactly (Eq. (38) uses `U_n*`); the sensitivity of the gradient to a
finite primal residual is never quantified. Confidence ALTA.
Evidence: p. 224 ("If `G_n` is contractive, i.e. `||dG_n/dU_n|| < 1`, according to the Banach
fixed-point theorem [35]"); p. 225 Eq. (40) and the "Therefore" that follows it.

### ALGORITMICO

**F9 — ADOPT (conditional, narrow) — non-commensurate-frequency machinery.**
Two concrete, transferable items. (i) The **optimal pseudo-period selection** of ref. [40]
(Nimmagadda, Economon, Alonso, Ilario da Silva, *Robust uniform time sampling approach for the
harmonic balance method*, AIAA 2016-3966): Table 2 reports `T_opt/T_0` = 1.13 / 1.00 / 1.41 / 1.38
for 5 / 7 / 9 / 11 instances, *"In order to ensure convergence for any set of frequencies"*
(p. 226). This exists because `E` must be inverted numerically when the `f_k` are not commensurate
(p. 222 after Eq. (14); p. 223 after Eq. (20)) and is otherwise ill-conditioned. (ii) Ref. [46]
Guédeney, Gomar, Gallard, Sicot, Dufour, Puigt, *Non-uniform time sampling for multiple-frequency
harmonic balance computations*, JCP 236 (2013) 317–345 — the literature hook for the *non-uniform*
sampling idea, i.e. the HB-side analogue of our switch-phase panel splitting.
*Insertion point:* **only** if the program ever admits a multi-mode RDE interface (two co- or
counter-rotating modes with incommensurate speeds, or a modulated mode), which today is outside the
standing periodic-wave scope pin. Recorded as a named lever, not adopted now. Confidence MEDIA
(value is contingent on entering the multi-mode case).
Evidence: p. 226 Table 2 and the paragraph above it; p. 235 refs [40], [46].

**F10 — IMPORTANT NEGATIVE / adoptability verdict on the flow model — touches T-T0 (claim 14).**
For our declared case the harmonic-balance *flow model* is **not adoptable, because it is
superseded**. HB buys quasi-periodicity by solving `2K+1` coupled pseudo-steady systems (p. 223).
For a **single rotating mode**, T-T0 gives the wave-frame reduction: the problem is exactly steady
in the rotating frame, one solve, and the instantaneous thrust through every axisymmetric surface
is constant — a strictly stronger statement than "the average is right". HB with K=1 would cost
3 coupled systems to recover, approximately, what one wave-frame solve gives exactly. HB therefore
earns its place for us **only** in cases T-T0 does not cover: incommensurate multi-mode operation,
longitudinal/feed-coupled pulsation, or genuinely non-wave-frame-reducible unsteadiness — and note
that D2.3 already routes **mode-transition phases outside the averaged theory entirely**, which is
the other candidate use. Verdict of record: **adopt the adjoint architecture (F5), do not adopt the
HB flow model.** Confidence ALTA.
Evidence: p. 223 ("the solution of 2K+1 nonlinear systems of equations need to be computed");
Eq. (20)–(21).

**F11 — ADOPT (benchmark datum) — touches the S25 / S25-bis engine-speed program.**
Hard external numbers for what an industrial-grade discrete adjoint costs relative to its primal,
useful as the SOTA bar in the speed ledger: **adjoint/primal cost ratio ≈ 1.3** for the inviscid
airfoil (0.28 s per primal iteration, 4-core Xeon E5-1620 with hyper-threading, ~11 000 grid
points, p. 227) and **≈ 1.7** for the fully-turbulent cascade (1.41 s per primal iteration, ~40 000
elements, p. 230; 1.98 s for OptC2, p. 233). Plus the reduced-order gain: HB with 5 instances is
*"about 9x faster than the time-accurate solution calculated over a total simulation time of five
periods"* (pp. 229–230). Optimization counts: convergence "nearly reached after only 7 evaluations"
for OptC1 (p. 230), ~14 for OptC2 (p. 233), ~15 for the airfoil (Fig. 4a).
The AD implementation detail worth copying in spirit: **Jacobi taping + C++ expression templates**
(CoDiPack), reported as *"leading only to a small runtime overhead"* (p. 225) — the analogue of
our per-cell `custom_vjp` implicit rule choice, and independent evidence that a well-structured
reverse-AD adjoint need not cost more than ~2× the primal. Confidence ALTA.
Evidence: p. 225, p. 227, p. 230, p. 233 as quoted.

**F12 — CONTAINED / named limitation of their pipeline — driver and parameterization.**
Their driver is **SLSQP** [38] on a fixed parameterization (50 Hicks–Henne bumps; 16 FFD
parameters), with the parameterization acting as the only regularizer: no Riesz/Sobolev
representation of the gradient, no mesh-independence statement, no trust region reported, no
reduced-Hessian or KKT-residual certificate, no bound ladder, no globality mechanism. Fig. 10a
shows the outlet-angle constraint driven into violation around evaluations 6–9 before recovery.
Our VI.5 (TR-SQP with Steklov–Poincaré-represented gradients, active-set multipliers reported as
marginal values, deflated continuation, sector tournament) and VI.6 (Verdict stack) are strictly
richer. Nothing to adopt on this axis; recorded so the litmap does not over-credit the paper's
optimizer. Confidence ALTA.
Evidence: p. 225 ("solved using a modified version of the nonlinear least-squares method (SLSQP)
[38]"); p. 227 ("50 Hicks–Henne bump function variables [41]"); p. 230 ("16 geometrical design
parameters `alpha` based on a free-form deformation (FFD) approach [45]"); Fig. 10a.

---

## 6. Bibliography inspection (record datum)

46 references, pp. 234–235. Inspected in full.

**Classical variational nozzle line — ENTIRELY ABSENT.**
- **Rao** — not cited. **Guderley** — not cited. **Hantsch** — not cited. **Hoffman** — not cited.
  **Kraiko** — not cited. **Shmyglevskii** — not cited. **Sirazetdinov, Scofield, Beck, Nikol'skii,
  Tillyaeva, Osipov** — none cited.
- There is **no nozzle reference of any kind** in the list, and no method-of-characteristics
  reference. The paper's application domain is airfoil/turbomachinery only.

**Modern adjoint line — partially present.**
- **Pironneau** — YES, ref. [6]: *On optimum design in fluid mechanics*, J. Fluid Mech. 64 (01)
  (1974) 97–110.
- **Jameson** — YES, and repeatedly: ref. [7] *Aerodynamic design via control theory*, J. Sci.
  Comput. 3 (1988) 233–260; also [15] (3-D unsteady multi-stage HB, with Gopinath/Van der Weide/
  Ekici/Hall), [17] Van der Weide–Gopinath–Jameson time-spectral, [21] Nadarajah–Jameson
  frequency-domain optimum shape design, [32] Jameson–Schmidt–Turkel (JST), [33] Jameson
  time-dependent multigrid, [34] Gopinath–Jameson time spectral for vortex shedding.
- **Lions** — NOT cited. **Giles** — NOT cited. **Ulbrich** — NOT cited. **Lozano** — NOT cited.
  (Consequence: the captured-shock adjoint consistency question of F7 is nowhere raised.)
- Discrete-adjoint / duality-preserving line, present and central: **Nielsen–Diskin–Park-style**
  ref. [27] Nielsen, Lu, Park, Darmofal, *An implicit, exact dual adjoint solution method for
  turbulent flows on unstructured grids*, Comput. Fluids 33 (9) (2004) 1131–1155; **Mavriplis**
  refs. [11] and [28]; **Albring–Sagebaum–Gauger** refs. [29], [36], [39] (CoDiPack).
- Harmonic-balance / time-spectral adjoint line: **Hall–Ekici–Thomas** [14], [16], [18], [19];
  **Choi–Lee–Copeland–Alonso** [20]-adjacent [18]; **Engels-Putzka & Frey** [22] (adjoint HB for
  forced response in turbomachinery); **Ma–Su–Yuan** [23]; **Lyu–Kenway–Furst–Martins** [24] AD of
  RANS adjoint with turbulence model.
- **SU2 stack**: [25] Palacios et al. 2013, [26] Economon et al. AIAA J. 54 (3) (2015) 828–846,
  [12] Economon–Palacios–Alonso unsteady continuous adjoint on dynamic meshes.
- **Real-gas sibling worth noting for our thermo pin**: [30] S. Vitale, T.A. Albring, M. Pini,
  N.R. Gauger, P. Colonna, *Fully turbulent discrete adjoint solver for non-ideal compressible flow
  applications*, J. Glob. Power Propuls. Soc. 1 (2017) 252–270 — the same group's EOS-general
  discrete adjoint; a candidate follow-up read for the EOS-general branch of E4.
- Other items of interest: [35] **Banach 1922** (the fixed-point theorem underwriting Eq. (30)/(40));
  [40] Nimmagadda et al. robust uniform time sampling; [46] **Guédeney et al.** non-uniform time
  sampling for multi-frequency HB, JCP 236 (2013) 317–345; [44] Prasad, mixed-out averaging;
  [42] Stadtmüller–Fottner, the T106D-EIZ experiment.

**Record conclusion:** this paper sits *entirely* inside the Jameson/Pironneau/SU2 discrete-adjoint
lineage and has **zero contact** with the classical variational nozzle corpus. It therefore cannot
be a prior-art threat to P2/G14 (the Rao-multiplier-field ↔ continuous-adjoint identification):
it never mentions Rao, never mentions a multiplier field of the classical type, and never discusses
optimality conditions of Euler–Lagrange/transversality type. It is, however, a strong exhibit for
the *"the gap is not technological"* argument.

---

## 7. Novelty relative to HTH-1971 / Hoffman-1967

The two literatures do not intersect; "novelty relative to 1971" is best stated as a trade.

**What Rubino et al. add that the 1967–1971 school cannot do.** (i) Unsteadiness in the constraint:
the optimized shape is shared across a coupled family of flow states, whereas HTH/Hoffman optimize
a single steady field. (ii) Turbulence and viscosity inside the differentiated model (SST, with the
turbulence model itself differentiated by AD — no frozen-turbulence approximation, explicitly
claimed on p. 220: *"without any approximation in the linearization of the turbulent viscosity"*).
(iii) Arbitrary geometry and arbitrary objective: no check-contour is required, so the method
survives in regimes where Shmyglevskii's classical limits kill Route A (2-D cascades with wakes and
separation here; and in principle 3-D, where "no check surface exists"). (iv) Arbitrary
parameterization and arbitrary number of design variables at O(1) gradient cost. (v) An engineering
toolchain: open-source solver, reverse AD, SQP, 7–15 design iterations to convergence.

**What is lost relative to 1967–1971.** (i) All analytic optimality structure: no derived control
surface, no first integrals, no transversality/corner condition, no statement that the optimal
surface *is* a characteristic. The 1971 school *derives* structure; this paper *searches*.
(ii) Any statement about the continuous problem — existence, uniqueness, or convergence of the
discrete optimum to a continuous one; the object optimized is the discretization.
(iii) Discontinuity handling: Kraiko's discontinuous multipliers with derived jump conditions have
no counterpart here; shocks are captured and smeared, and the adjoint is taken through the smear.
(iv) Certificates: the 1971 school ships the optimality residual (Hoffman Eq. (78)-type) as a
verifiable object; here the only certificate is an FD cross-check on a handful of directions.
In our own vocabulary: this paper is a *strong* ALGORITHMIC contribution, a *moderate* FORMAL one
(the duality-preserving fixed-point adjoint of an averaged objective is genuinely well-structured),
and a *null* THEORETICAL one — no theorem is proved anywhere in the paper.

---

## 8. Bottom line on adoptability (the question the review was asked)

**Adopt:** the duality-preserving fixed-point discrete adjoint (F5) as the declared non-marching
fallback for Lemma-B(ii), with the averaging operator differentiated inside the Lagrangian; the
cost-ratio benchmark and the constant-memory AD philosophy (F11); the non-commensurate-frequency
sampling machinery as a *named, unexercised* lever for a future multi-mode interface (F9).

**Do not adopt:** the harmonic-balance flow model itself — superseded for our single-rotating-mode
scope by T-T0's exact wave-frame reduction (F10); the captured-shock treatment, which violates our
fitted-front pin (F7); the FD-only gradient certificate, strictly weaker than O3.1 (F6); the
optimizer/parameterization layer (F12).

**Carry as conditional if cited:** the "duality preserved / rate inherited" claim, whose contraction
hypothesis is asserted and never measured (F8).

**Litmap action:** re-word claim 7 (D2 gap G3) to make *continuous* optimality conditions *with
free-boundary/transversality structure* explicit, otherwise this paper is a legitimate attack on the
sentence as written (F1).
