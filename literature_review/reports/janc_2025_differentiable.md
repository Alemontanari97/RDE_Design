# Expert read — JANC (Wen, Luo, Xu, Wang; Tsinghua, 2025 preprint)

**File**: `literature_review/janc_2025_differentiable_reacting_solver_adjoint.pdf`
**Reader**: convergence-review expert reader, 2026-08-13
**Why on the list**: nominated THREAT VECTOR — differentiable JAX reacting solver with an adjoint demo on an RDC.

---

## 1. Citation (verified from the PDF only)

Haocheng Wen¹, Faxuan Luo¹, Sheng Xu, Bing Wang (¹equal contribution; corresponding: HC Wen,
haochengwenson@126.com; B Wang, wbing@mail.tsinghua.edu.cn), *"JANC: A cost-effective,
differentiable compressible reacting flow solver featured with JAX-based adaptive mesh
refinement"*, Tsinghua University, School of Aerospace Engineering, Beijing, China, 100084.
30 pages, 12 figures, 3 tables, 34 references. Code MIT-licensed at
`https://github.com/JA4S/JAX-AMR` and `https://github.com/JA4S/JANC`.

**Citation caveat of record**: the document carries **NO printed venue, volume, DOI, arXiv
identifier or date** on any of its 30 pages (no journal header, no submission stamp, no
copyright line). It is a manuscript/preprint. The year 2025 is *inferred*, not printed: the
most recent reference access dates inside the bibliography are "accessed April 13, 2025" and
"accessed April 14, 2025" (refs [10], [15], [16], [22], [29]), and ref [25] (Cantera) carries
a 2024 Zenodo DOI. **Do not cite this with a venue until the venue is independently
established.**

## 2. Read coverage

**30 / 30 pages read in full**, bibliography included (pp. 28–30, refs [1]–[34]).
Nothing was skipped. Not read (does not exist in the PDF): any appendix, any supplementary
material, and the GitHub source code — the paper repeatedly defers implementation detail to
"the documentation, source code, and comments on GitHub" (p. 13) and to "the relevant example
on GitHub" (p. 25), so any claim about the *code* is out of scope of this read.

## 3. What the paper actually does

**Problem.** Not a design problem. Two software-engineering objectives: (i) build the first
JIT-compatible block-structured AMR framework in JAX (JAX-AMR); (ii) build on it a
fully-differentiable GPU solver for 2-D compressible **reacting** Euler flow (JANC), and
demonstrate end-to-end gradients through the full time trajectory. The single optimization
demonstration (§6.2) is an **inverse problem**: infer the injection equivalence ratio φ of an
RDC from two flow-field snapshots.

**Formulation.**
- Governing: 2-D compressible reactive Euler in Cartesian (x, y), **Eq. (4.1)**,
  `U = [ρ, ρu, ρv, E, ρY₁ … ρY_{Ns−1}]ᵀ`, source `S = [0,0,0,0, ω̇₁ … ω̇_{Ns−1}]ᵀ`.
  Explicit statement, p. 10: *"The effects of viscosity and transport properties of the
  working fluid are neglected."*
- EOS: **thermally perfect gas**, **Eq. (4.2)** `p = ρRT`, `E = ρh − p + ½ρ(u²+v²)`,
  `h = Σ Y_k h_k`; species properties from **NASA-7 polynomials, Eqs. (4.3)–(4.5)**
  (quartic c_p ⇒ quintic h ⇒ log+quartic s), coefficients "retrieved from the open-source
  thermodynamic library Cantera [25]" (p. 11).
- Chemistry: finite-rate elementary mechanism, **Eqs. (4.6)–(4.9)** (Arrhenius forward rate,
  backward via equilibrium constant `K_i^eq`), Chemkin-format input [26].
- Optimization (§6): **Eq. (6.1)** `∂U/∂t = N(U;θ)`; **Eq. (6.2)** trajectory integral;
  **Eq. (6.3)** `θ* = argmin_θ L(U(t;θ))`; **Eq. (6.4)** Adam update; **Eq. (6.5)** the
  **continuous ODE adjoint** (Neural-ODE, ref [24] Chen et al.):
  `∂a/∂t = N*(a)`, `a(t₀) = ∫_{t₀}^{t} N*(a(τ))dτ + ∂L/∂U(t)`,
  `∂L/∂θ = a(t₀)ᵀ ∂N/∂θ`.
- Objective in the demo: **Eq. (6.6)** `L = ‖Ū₁₀₀(φ=θ) − U₁₀₀(φ=1.0)‖ / ‖U₁₀₀(φ=1.0)‖`
  (relative snapshot mismatch after 100 TVD-RK3 steps).

**Unknowns.** Forward: the conserved vector U on a Cartesian grid. Inverse: a **single scalar**
θ = φ (equivalence ratio). Nothing geometric.

**Constraints.** *None* in the optimization sense. Unconstrained gradient descent (Adam,
learning rate 0.001). No KKT, no multipliers, no admissible set, no bounds. The PDE enters only
as the differentiable map (6.2).

**Flow model.** Inviscid, 2-D planar Cartesian, uniform spacing ("JANC uses uniformly spaced
grids", p. 12). No axisymmetry, no curved/immersed boundary, no geometry description at all.
RDC case: the annulus is **unfolded** into a rectangle L_x = 0.10 m (circumferential) ×
L_y = 0.04 m (axial), 1000 × 400 cells, periodic in x, **pressure outlet with backpressure
0.1 atm** at the top, premixed injection model [34] (Fievisohn & Yu) at the bottom with fixed
area ratio 0.2, p₀ = 10 atm, T₀ = 300 K (p. 25).

**Solver.** Conservative finite difference **Eq. (4.10)**; Lax–Friedrichs flux vector splitting
**Eq. (4.11)** with `α = max(|u|+c)`; **WENO5** reconstruction (6-point template, 3 ghost
layers at the physical boundary); Strang splitting of convection and chemistry; **TVD-RK3** for
convection; **first-order point-implicit** chemistry **Eqs. (4.12)–(4.13)**, with the Jacobian
`∂S*/∂U*` restricted to the species block ("only ρY₁, …, ρY_{Ns−1} are considered as the
variables for differentiation, while other conserved quantities are treated as constants",
p. 12); Newton–Raphson inversion of the quintic **Eq. (4.4)** for T from h, warm-started from
the previous time step. AMR: fixed-shape blocks, predeclared `N_{i,max}`, invalid/NaN padding
blocks, doubling/halving heuristic (**Algorithm 1**, p. 7), crossover vs synchronous advance
(**Figure 2**), piecewise-constant "one to four" refinement and arithmetic-mean "four to one"
coarsening (p. 6). Multi-GPU via `@jax.pmap` and `jax.lax.ppermute` halo exchange (pp. 15–16).
AD: `jax.custom_vjp` wrapper `make_diffeq` → `ode_solver` replaces default AD over the time
loop (p. 24).

**Verification.** (i) Sod shock tube vs the analytic Riemann solution, 400 cells, γ = 1.4,
CFL 0.2, Figure 4. (ii) Ignition delay in a 0-D constant-volume reactor vs **Cantera**, 9-species
19-reaction Jachimowski H₂–O₂ mechanism [29], Case 1 (20 atm, 1500 K) and Case 2 (9 temperatures
1200–2000 K), Figures 5–6; time-step study selects dt = 5e-9 s. (iii) Performance vs OpenFOAM
`detonationFOAM` [30] on a 2-D detonation tube, Figures 8–10, Table 3: CPMS 13.3 vs 1344.0 USD
(core solver, 1.0 %), 12.0 (synchronous) / 6.7 (crossover) vs 555.8 with AMR (2.1 % / 1.2 %).
Near-linear 1→4 GPU scaling, 5 → 20 steps/s (Figure 9b).

**What is NOT verified.** There is **no grid-convergence / order-of-accuracy study anywhere**;
**no verification of the gradient** (no dot-product/transposition test, no finite-difference
comparison, no adjoint consistency check); no experimental validation ("The consistency of the
results with experimental data is not discussed here", p. 19); no uncertainty/noise study on the
inverse problem.

**Result of the demo.** From four initial guesses θ₀ ∈ {0.70, 0.80, 1.20, 1.30}, Adam converges
to φ = 1.0 "within no more than 400 iterations" (Figure 12), 1.20 optimizer iterations/s on one
A100, 8–9 min per case. Default (unrolled) JAX AD fails outright:
*"XlaRuntimeError: RESOURCE_EXHAUSTED: Out of memory while trying to allocate 421565057912
bytes"* (p. 26) — i.e. ≈ 421 GB requested on a 40 GB card.

## 4. Hypotheses

**Declared.**
1. Inviscid; viscosity and all transport neglected (p. 10).
2. Thermally perfect gas mixture, NASA-7 caloric fits (Eqs. 4.2–4.5).
3. 2-D, Cartesian, **uniformly spaced** grid (p. 12).
4. Strang splitting validly decouples convection and chemical source.
5. Point-implicit Jacobian: only species variables differentiated; other conserved quantities
   frozen within the chemistry substep (p. 12).
6. AMR buffer sizing: "the number of buffer grids must be no less than the propagation distance
   of the disturbance in the unit AMR update step" (p. 5).
7. RDC demo only: **γ fixed at 1.29**, **single-step global H₂–air reaction**, unfolded planar
   annulus, area ratio 0.2, p₀ = 10 atm, T₀ = 300 K, p_back = 0.1 atm (p. 25).

**Undeclared but necessary.**
8. **Gradient consistency of the continuous adjoint.** Eq. (6.5) is the *continuous* ODE adjoint,
   integrated backward "using the same TVD-RK3 numerical integration method" (p. 24). That the
   result equals the derivative of the *discrete* forward map is assumed, never stated, never
   tested. It requires either exact reversibility of the RK3 sweep or negligible
   optimize-then-discretize inconsistency — neither is established. (Also: no checkpointing
   scheme is described, so backward reconstruction of intermediate states is left unspecified.)
9. **Differentiability through shock capturing.** The functional (6.6) is differentiated through
   WENO5 nonlinear weights and through `α = max(|u|+c)` across a *captured* detonation front.
   Smoothness of L in θ is assumed; the captured-shock adjoint problem is never mentioned.
10. **Time-step treatment in the adjoint.** `dt` is set by a CFL function of the state, hence of
    θ; whether the adjoint accounts for `dt(θ)` (or freezes it) is not stated.
11. **Identifiability** of φ from two snapshots 100 steps apart, and a basin assumption: all four
    starts lie within ±30 % of the truth; one ground-truth value only; no noise.
12. **Newton–Raphson convergence** for T(h) from a previous-step warm start within the assumed
    small number of iterations.
13. **NaN safety under AD.** Invalid blocks are filled with NaN and reductions must use
    `jnp.nanmax` (p. 6). NaN entries poison reverse-mode gradients through `where`/`nanmax`
    unless carefully masked. Never addressed — and never exercised, because the adjoint demo
    does not use AMR.
14. **Order preservation across AMR interfaces.** Refinement is piecewise-constant injection and
    coarsening is arithmetic averaging (p. 6) — first order — embedded in a WENO5 scheme; the
    resulting formal order is never measured.
15. Grid independence of every reported result.
16. Differentiability of the premixed injection model [34] with respect to φ.

## 5. Findings — three-level comparison against the programme apparatus

### TEORICO

**[T-1] GAP-CONFIRMS — the variational nozzle corpus and the adjoint-CFD corpus are both
absent.** *Claims touched: D2 gap G3, empty-niche claim (8), P2/G14.*
Evidence: complete reference list, pp. 28–30, 34 entries. **Rao, Guderley, Hantsch, Hoffman,
Kraiko, Shmyglevskii: none.** **Lions, Pironneau, Jameson, Giles, Lozano: none.** The word
"adjoint" in this paper is anchored to exactly one reference, [24] R.T.Q. Chen, Y. Rubanova,
J. Bettencourt, D. Duvenaud, *Neural Ordinary Differential Equations* (2019). The only method-of-
characteristics citation, [34] Fievisohn & Yu, *"Steady-State Analysis of Rotating Detonation
Engine Flowfields with the Method of Characteristics"*, JPP 33 (2017) 89–99, is used **only as an
injection boundary-condition model** (p. 25), never as an optimization instrument. A 2025
state-of-the-art differentiable reacting solver with an adjoint applied to an RDC therefore has
**zero contact** with the classical variational nozzle line — direct, dated corroboration that
gap G3 and the empty-niche claim describe a real vacancy. Confidence: ALTA.

**[T-2] THREAT (capability/timeline, not to any theorem) — the announced roadmap is exactly the
missing half of a brute-force competitor.** *Claims touched: T-T3 practical value, oracle O5,
F5/F6 phases.*
Evidence: §7, p. 27, four announced enhancements: *"Extending the current two-dimensional
framework to fully three-dimensional implementations; Integrating advanced physical models
including viscous flows, turbulence model, and particle phase model; Implementing parallel
computing for JAX-AMR; **Developing immersed boundary methods based on JAX-AMR for
complex-geometry computational domains**."* Plus MIT-licensed release. And their own
bibliography already contains the shape-side precedent in the same ecosystem: [13] Buhendwa,
Bezgin, Karnakov, Adams, Koumoutsakos, *"Shape inference in three-dimensional steady state
supersonic flows using ODIL and JAX-Fluids"* (2024), arXiv:2408.10094. Immersed boundary +
shape parameters + a thrust functional on top of JANC would be a *direct unsteady* attack on the
same physical problem. It threatens no theorem of record (T-T3 is a theorem under stated
hypotheses), but it shortens the horizon in which a purely computational unsteady result could
be published against which the cycle-averaged reduction must argue its value. ACTION: procure
arXiv:2408.10094 as a named litmap lead. Confidence: MEDIA.

**[T-3] CONTAINED — their optimization problem is the fully degenerate corner of (P).**
*Claims touched: (P) / D2.6, oracle O5.*
Evidence: Eqs. (6.3) and (6.6), p. 25. Their problem is `min_θ L(U(t;θ))` with **θ a single
scalar physical parameter**, no admissible set, no geometric design variable, no constraints
`g_i(S) ≤ c_i`, no measure μ, no state constraint, no shape derivative, no transversality, no
globality question. It is contained in (P) only in the vacuous sense of "fixed geometry,
zero-dimensional design space, snapshot-mismatch objective" — under those hypotheses it is
parameter identification, not design. This containment is nonetheless *useful*: their machinery
is precisely the machinery an **O5 oracle** (unsteady simulation vs `J_avg + St·J₁`) would need,
promoted from value-level to gradient-level comparison. Confidence: ALTA.

**[T-4] GAP-CONFIRMS — even the state-of-the-art finite-rate differentiable solver runs its
showcase at constant γ with a one-step reaction.** *Claims touched: P1 scope pin, E4 (γ-const
discipline), [T-EQBR] bracket.*
Evidence: p. 25, verbatim: *"For simplicity, the specific heat ratio is fixed at 1.29, and the
chemical reaction is modeled as a single-step hydrogen-air total combustion reaction."* This is
in the *same paper* whose §4.1 builds full NASA-7 + Chemkin finite-rate machinery (Eqs. 4.3–4.9)
and validates it against Cantera. Two consequences for us: (a) it corroborates the
anti-overengineering pin P1 — the field itself falls back to frozen/constant-γ the moment an
optimization loop is attached; (b) it corroborates why our E4 directive (γ = const admissible
only as a *declared oracle*, never load-bearing) is a real discriminator: here γ = 1.29 is
load-bearing in the only optimization result of the paper and is declared only as "for
simplicity". Confidence: MEDIA (interpretive step: from one instance to a field-wide habit).

### FORMALE

**[F-1] GAP-CONFIRMS — their adjoint is continuous-in-time (optimize-then-discretize) and
completely unverified; our discrete-adjoint certificate has no counterpart here.**
*Claims touched: Lemma B (discrete-adjoint reading), O3.1 transposition identity, claim (13).*
Evidence: Eq. (6.5), p. 24; and the sentence immediately after it: *"By solving equation (6.5)
using the same TVD-RK3 numerical integration method, the gradient of the cost function can be
computed …"*; and *"The specific form of the adjoint equation N* and ∂N/∂θ can be directly
obtained through JAX's built-in automatic differentiation, without the need for complicated
symbolic derivations."* This is the Neural-ODE continuous adjoint [24], **not** the transpose of
the discrete forward map. Nothing in §5 or §6 checks the gradient: no `|⟨w, Jv⟩ − ⟨Jᵀw, v⟩|`
identity, no finite-difference cross-check, no seeded-corruption negative control. Our O3.1
(2.7e-10 vs derived tolerance 5.1e-8 over the entire march, with a corrupted-vjp negative
control that fires) is strictly stronger *in kind*, not merely in number. The gap "modern
differentiable-CFD adjoints ship without a transposition certificate" is confirmed at the most
favourable possible sample point (a 2025 JAX solver whose whole selling point is
differentiability). Confidence: ALTA.

**[F-2] GAP-CONFIRMS — they differentiate a captured detonation, the exact object our VI.3 pin
rejects.** *Claims touched: VI.3 "differentiate the fitted front, never a captured smear";
F4b fitted-front adjoint jumps.*
Evidence: §4.2, p. 12 (LF flux splitting + WENO5 reconstruction, no fitting anywhere in the
paper); §6.2, pp. 25–26 (the adjoint of Eq. (6.5) is taken through the RDC field of Figure 11,
which contains the detonation front, the oblique shock and the contact surface as *captured*
structures). The Giles–Ulbrich / Lozano objection to captured-shock adjoints is never raised.
Their empirical success on a **scalar** parameter says nothing about a shape derivative through
the same smear — the sensitivity of a bulk L² snapshot norm to a scalar injection parameter is a
far more forgiving functional than a wall Hadamard density. Confirms our fitted-front pin is a
genuine, currently unoccupied discriminator rather than a preference. Confidence: ALTA.

**[F-3] ADOPT — the `make_diffeq` structure: a `custom_vjp`-wrapped time integrator carrying an
ODE adjoint, with the quantified memory argument.** *Claims touched: oracle O5, phase F5, VI.3.*
Evidence: p. 24 (*"JANC uses the `jax.custom_vjp` function to replace the default JAX automatic
differentiation, packaging the adjoint equation algorithm into a function called `make_diffeq`.
This function takes the right-hand side of the differential equation N … and outputs a function:
`ode_solver`, that can automatically solve the adjoint equation."*) and p. 26 (default AD:
`RESOURCE_EXHAUSTED … 421565057912 bytes` on a 40 GB A100; with the adjoint: 1.20 optimizer
iterations/s, 8–9 min per case, 400 000 grid points × 100 time steps).
**Where it grafts in our apparatus.** Our `custom_vjp` discipline is currently *spatial* (per-cell
implicit unit process, VI.2, giving the Lemma-B march transpose). Theirs is *temporal*. The two
are complementary and we do not yet have the temporal one. The graft points are exactly two:
(i) **oracle O5** in VI.6 — to compare an unsteady run against `J_avg + St·J₁` at gradient level
rather than only at value level, we need a differentiable time integrator over the RDC
trajectory, and this is the cheapest known structure for it; (ii) **phase F5 (RDE)**, where
interface data is generated rather than imported. **Adoption condition (binding)**: adopt the
*structure*, never their verification standard — any `make_diffeq`-style wrapper we write must
carry the O3.1 transposition identity against the discrete forward map plus a seeded-corruption
rejector before it is allowed to produce a number of record, precisely because Eq. (6.5) is
continuous-adjoint and its discrete consistency is unproven (see F-1). The 421 GB figure is also
directly citable in our S25 speed narrative as the quantified reason the naive unrolled-AD route
is not merely slow but infeasible. Confidence: ALTA.

**[F-4] ADOPT / CONTAINED — thermo backend: independent confirmation of DIR-THERMOTAB, plus one
concrete micro-technique.** *Claims touched: DIR-THERMOTAB, the quintic-Hermite closure survey,
P1 thermal pin.*
Evidence: Eqs. (4.3)–(4.5), pp. 10–11. Their `c_{p,k}/(R_u/M_k) = a₀ + a₁T + a₂T² + a₃T³ + a₄T⁴`
(quartic c_p) with `h_k/(R_u/M_k) = a₀T + a₁T²/2 + … + a₄T⁵/5 + a₅` (**quintic h**) is exactly
the structure recorded in our backend survey ("in the working window the NASA fit has quartic
c_p ⇒ quintic h, exactly reproduced by the quintic-Hermite closure"), reached independently.
Their EOS `p = ρRT` with frozen-composition mixture rules is also exactly our Lemma-A thermal pin
(thermally perfect ideal gas, no co-volume/virial/tabulated real-gas). And Cantera is their sole
coefficient source ([25], p. 11) — the same generator discipline as ours.
**Micro-technique worth taking**: p. 12, *"JANC uses the Newton-Raphson iteration method to solve
the quartic polynomial equation (4.4) for enthalpy and temperature. To accelerate the convergence
of the iteration, the initial temperature for each Newton-Raphson iteration is set as the
temperature from flow field of the previous time step."* Our table backend performs the same
h → T inversion per unit process; warm-starting from the upstream/previous node state is a free
iteration-count reduction and grafts directly into the thermo handle in VI.2. (Note the paper's
own wording slip: Eq. (4.4) is quintic in T, not quartic — a typographical inconsistency, not a
substantive error.) Confidence: ALTA (structure), MEDIA (size of the speed gain for us).

### ALGORITMICO

**[A-1] ADOPT — the JIT-static-shape padding pattern is the general solution to the obstruction
our own vectorization programme hit.** *Claims touched: VI.4 cycle layer, the S25/S25-bis vmap
work, generality-of-procedures directive.*
Evidence: §3.1, pp. 4–7. The whole design is a recipe for making a *dynamically sized* problem
JIT-compatible: (a) all blocks in a layer share one shape ("to ensure compatibility with JIT and
vectorized operations, all b_{i,j} within the same layer must have the same size and shape",
p. 4); (b) `N_{i,max}` predeclared as a compile-time constant, with valid blocks
`0 ≤ j ≤ N_{i,valid}−1` and reserved **invalid blocks** beyond, whose cost is accepted as the
price of avoiding re-JIT (p. 6); (c) a **NAN block** as the sentinel for ghost grids without a
neighbour, with the explicit consequence "if the solver involves computing global extrema,
averages, or similar operations, the influence of NAN values needs to be removed. For instance,
the function `jnp.nanmax` should be used instead of `jnp.max`" (p. 6); (d) **Algorithm 1**, p. 7,
the amortized doubling/halving of `N_{i,max}`: `if (N_valid+1) > N_max: N_max = 2·N_max;
elif (N_valid+1) < 2.5·N_max: N_max = N_max/2`.
**Where it grafts.** Our per-phase MoC marches over ξ have phase-dependent node counts (switch
phases, panel splitting at ξ*(Σ), plug free-boundary marches of differing length), and our
`vmap` over phases requires uniform shapes — the identical obstruction. The pattern to import is
(b)+(d): a predeclared padded node capacity with amortized doubling, plus masked reductions,
instead of per-phase re-tracing. **Two cautions on adoption**: their Algorithm 1 hysteresis is
written with a `<` where a shrink guard is expected and they themselves call it "only a simple
version" that "still incurs some redundant computational overhead" (p. 7) — re-derive the policy,
do not copy the constants; and **never use NaN as the pad sentinel in a differentiated region**
(see A-3). Confidence: ALTA.

**[A-2] ADOPT — `pmap` + `ppermute` halo exchange, with measured near-linear scaling and a
reporting unit.** *Claims touched: VI.4 cycle layer parallelism, S25 speed programme reporting.*
Evidence: pp. 15–16 (`split_grid`, `exchange_halo` "implemented using the `jax.lax.ppermute`
function", `parallel_rhs`, `parallel_advance_one_step` "with the `@jax.pmap` decorator added to
the function declaration"; *"By simply adding the `@jax.pmap` decorator, the program can
automatically implement parallelism without the need to separately write MPI files"*); Figure 9b,
p. 20 (1→4 A100: 5 → 20 steps/s, "increases almost linearly"), with the invariance claim "the
parallel computing results of JANC are identical to those obtained with a single GPU".
Our cycle layer is *embarrassingly* parallel over phases ξ — a strictly easier case than their
halo-coupled domain decomposition, since our phases need no halo exchange at all. `pmap` over
phases is the natural extension of the current `vmap` once phase count × march size exceeds one
device. Also worth importing as a reporting convention: their **CPMS** (cost per million steps,
USD) with the pricing stated openly (p. 20: ≈ 0.24 USD per A100-hour, 0.007 USD per EPYC-7452
core-hour; CPMS 13.3 vs 1344.0; Table 3, p. 27) is a cleaner, hardware-honest speed unit than
raw wall-clock and would strengthen our S25 record numbers. Confidence: ALTA (technique),
MEDIA (CPMS as a convention we actually need).

**[A-3] CORRECTION — the nomination "differentiable AMR reacting solver with adjoint on RDC"
overstates what is demonstrated: differentiability and AMR are never exercised together.**
*Claims touched: the threat-vector nomination for this paper in our reading list.*
Evidence: the abstract (p. 1) sells one artifact — *"a fully-differentiable solver for
compressible reacting flows"* with *"JAX-based adaptive mesh refinement"* — but the two features
are demonstrated on **disjoint** cases. The adjoint demo (§6.2, p. 25) runs on a **uniform**
1000 × 400 grid: *"the computational grid is set to 1000 and 400 cells along the x- and y-axes"*,
with no mention of AMR; the AMR performance case (§5.2.3, pp. 21–22) carries no gradients. And
there is a structural reason to expect they cannot simply be composed: the AMR framework fills
invalid blocks with **NaN** (p. 6) and requires NaN-aware reductions, while reverse-mode AD
propagates NaN through `nanmax`/`where` gradients unless every mask is written with explicit
gradient-safe guards; furthermore the refinement decision itself (`get_refinement_grid_mask`
thresholding a density gradient, p. 8) is a **discrete, non-differentiable** function of the
state, so the AMR topology would silently be treated as constant by any adjoint taken through it.
**Correction to record for our litmap**: this paper is a *differentiable uniform-grid* reacting
solver **and** a *non-differentiated* AMR framework, in one package. The threat level should be
re-priced downward accordingly, and any future ADOPT of A-1 into a differentiated region must
replace NaN padding with a finite sentinel plus an explicit mask. Confidence: ALTA.

**[A-4] GAP-CONFIRMS — the verification standard of the field, at its best current sample, is far
below the Verdict standard.** *Claims touched: VI.6 certificate stack / "nothing ships outside a
Verdict"; R5 numbers discipline.*
Evidence: §5.1 is the entire verification section, and it contains exactly two tests — Sod shock
tube against the analytic Riemann solution (p. 16, judged by eye: *"the results obtained by
JANC's solver closely match the analytical solution"* — **no error norm, no table, no rate**) and
ignition delay against Cantera (pp. 17–18, again judged by eye: *"in good agreement"*). There is
**no grid-convergence study, no measured order of accuracy, no error bar, no tolerance derived
from anything, and no test of the gradient at all**, in a paper whose central contribution is a
gradient. The comparison against OpenFOAM is explicitly disclaimed as not an accuracy comparison
(*"this section only compares the results and computational efficiency … under similar
configurations. The consistency of the results with experimental data is not discussed here"*,
p. 19). This is direct evidence that our certificate stack (derived tolerances, rejectors that
can fire, transposition identity, Hoffman-E residual, DWR bars, two-resolution Richardson bands,
cross-code oracles) is not over-engineering relative to the field — it is a genuine
differentiator at the implementation level, and the "three-level SOTA" claim of the programme
survives contact with this paper at the implementation level. Confidence: ALTA.

## 6. Bibliography note (data of record)

34 references, pp. 28–30, read in full.

- **Classical variational nozzle line — entirely ABSENT.** No Rao, no Guderley, no Hantsch, no
  Hoffman, no Kraiko, no Shmyglevskii, no Sirazetdinov, no Scofield, no Nikol'skii. Not one
  nozzle-contour-design reference of any school, classical or modern.
- **Modern adjoint / optimal-control-of-PDE line — entirely ABSENT.** No Lions, no Pironneau, no
  Jameson, no Giles, no Lozano, no Ulbrich, no Peter–Dwight. The single adjoint citation is
  **[24] Chen, Rubanova, Bettencourt, Duvenaud, *Neural Ordinary Differential Equations* (2019),
  arXiv:1806.07366** — i.e. the adjoint is imported from the machine-learning literature, not
  from the aerodynamic-design literature.
- **RDE line — thin and recent.** [33] Rankin, Fotia, Naples, Stevens, Hoke, Kaemming,
  Theuerkauf, Schauer, *"Overview of Performance, Application, and Analysis of Rotating Detonation
  Engine Technologies"*, JPP 33 (2017) 131–143; [34] Fievisohn & Yu, *"Steady-State Analysis of
  Rotating Detonation Engine Flowfields with the Method of Characteristics"*, JPP 33 (2017)
  89–99 — the sole MoC citation, used only for the injection boundary model.
- **Differentiable-CFD ecosystem — the actionable part.** [16] JAX; [17] JAX-MD; [18] JAX-FEM;
  [19] Bezgin, Buhendwa, Adams, *JAX-Fluids*, CPC 282 (2023) 108527; **[13] Buhendwa, Bezgin,
  Karnakov, Adams, Koumoutsakos, *"Shape inference in three-dimensional steady state supersonic
  flows using ODIL and JAX-Fluids"* (2024), arXiv:2408.10094** — the nearest shape-side artifact
  in the same ecosystem, **not currently in our litmap; procure it**. Also [21] AMReX, [22] AMROC,
  [23] OpenFOAM, [30] detonationFOAM, [25] Cantera, [26] Chemkin-II, [29] Jachimowski.

**Reading of this bibliography.** The absence is not an oversight of a minor citation: it is the
signature of a community that has arrived at "differentiable solver + adjoint + rotating
detonation" through the machine-learning route, with no awareness of the seventy-year variational
nozzle corpus and no awareness of thirty years of adjoint aerodynamic design. That is
simultaneously the strongest available corroboration of the empty-niche and G3 claims, and the
clearest statement of where the threat will come from if it comes: not from a competing theory,
but from an unaware, well-tooled, fast-moving software community.

## 7. Novelty relative to HTH-1971 / Hoffman-1967

**Orthogonal — the paper adds nothing to, and takes nothing from, the state of the art of 1971.**
Hoffman 1967 and Hoffman–Thompson–Hoffman-era work supply: a whole-region multiplier-field
formulation, adjoint PDEs sharing the flow characteristics, a derived exit-surface character, an
optimality residual on the boundary condition (Hoffman 1967 Eq. (78)), transversality, and
constraint multipliers. JANC supplies **none** of these objects. Its "adjoint" (Eq. 6.5) is the
parameter-gradient adjoint of an ODE system with respect to a scalar, carrying no transversality,
no endpoint condition, no boundary residual, no multiplier field on a shape, and no optimality
system. Conversely, 1971 supplies nothing JANC needed.

What JANC does add, relative to the *implementation* state of the art rather than the theory, is
real and citable: (i) the first JIT-compatible block-structured AMR in JAX (fixed-shape blocks +
predeclared block counts + amortized resizing, §3); (ii) the first JAX-based compressible
**reacting** flow solver with finite-rate chemistry and NASA-7 thermo (§4); (iii) a demonstrated
two-orders-of-magnitude cost reduction versus OpenFOAM on a detonation-tube benchmark (Table 3);
(iv) a working demonstration that whole-trajectory gradients through an RDC field are feasible at
400 000 cells × 100 steps on one GPU where naive AD needs 421 GB (p. 26). Items (i), (iii) and
(iv) are the parts that matter to us, and they matter as **tooling**, not as theory.

## 8. Bottom line for the programme

- **Threat to any claim of record: none.** No theorem is contradicted, no niche is occupied, no
  priority is challenged. Claim (8) (empty niche) and gap G3 come out *strengthened*.
- **Distance from being our falsifier: large, and enumerable.** They lack, all of them
  simultaneously: geometry representation, axisymmetry, wall boundary of any kind (immersed
  boundary is future work, p. 27), a shape derivative, a thrust functional, constraints, an
  optimizer beyond Adam, a cycle measure or any time-periodicity constraint, shock fitting, and
  any gradient verification. What they *do* have is the hardest engineering half: a fast,
  differentiable, GPU, reacting, open-source unsteady solver with a working trajectory adjoint.
- **The real value here is ADOPT, not defence**: F-3 (temporal `custom_vjp` ODE-adjoint wrapper
  for oracle O5), A-1 (static-shape padding for the phase `vmap`), A-2 (`pmap`/`ppermute` over
  phases + CPMS reporting), F-4 (warm-started h → T Newton inversion). Every one of them must
  enter under our own certificate discipline, because the paper's own verification of its
  gradient is empty (F-1, A-4).
- **One procurement action**: arXiv:2408.10094, *Shape inference in 3-D steady supersonic flows
  using ODIL and JAX-Fluids* — cited by this paper as [13], adjacent to our niche, not in our
  litmap.
