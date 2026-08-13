# Expert read — Giles & Pierce 2000, "An Introduction to the Adjoint Approach to Design"

Reader: expert-reader agent, convergence review. Date: 2026-08-13.
Metro di confronto: APPARATUS BRIEF (record state) — M0 / D3 / P2_lemmaA / litmap 2026-08-12 + extension 2026-08-13.

---

## 1. Citation (verified from the PDF itself)

Michael B. Giles¹ and Niles A. Pierce², **"An Introduction to the Adjoint Approach to Design"**,
*Flow, Turbulence and Combustion* **65**: 393–415, 2000. © 2001 Kluwer Academic Publishers, Printed in the Netherlands.
Received 13 December 1999; accepted in revised form 2 February 2000.
¹ Computing Laboratory, Oxford University, Wolfson Building, Parks Road, Oxford OX1 3QD, U.K.
² Applied Mathematics, California Institute of Technology, Pasadena, CA 91125, U.S.A.
Key words (printed): computational fluid dynamics, adjoint p.d.e., design.
No DOI is printed on the article's pages. 46 references (pp. 413–415), 6 figures, 2 tables.

**RIGOR NOTE, binding for everything below: the equations in this paper are UNNUMBERED.**
Every citation below is therefore anchored by *page + section + verbatim quote or displayed-equation description*. No equation number is attributed to this paper anywhere in this report.

---

## 2. Read coverage

**23 / 23 pages read integrally (pp. 393–415), bibliography included** (2 Read calls: pages 1–20, then 21–23).
Nothing was skipped. Figures 2–6 are raster images (aircraft surface grids, wing sections, Cp traces); their *captions and the numeric content of Tables I and II* were read, the pixel content of the wing/Cp plots was inspected only as rendered images and is not load-bearing for any finding below.

---

## 3. What the paper actually does

- **Problem.** Didactic/expository review (not a new result paper): how to compute the gradient of a scalar aerodynamic objective with respect to many geometric design variables, at a cost independent of the number of design variables. Two application demos are *reproduced from other people's papers*, not produced here.
- **Formulation.** Given design variables α controlling geometry through grid coordinates X(α), and discrete flow variables U satisfying `N(U,α) ≡ N(U,X(α)) = 0` (§2.4, p. 396), minimise J(U,α). Linearising: `dJ/dα = ∂J/∂U · dU/dα + ∂J/∂α` subject to `∂N/∂U · dU/dα + ∂N/∂α = 0`; setting `u = dU/dα, A = ∂N/∂U, gᵀ = ∂J/∂U, f = −∂N/∂α` gives the canonical pair `Au = f` (direct/tangent) and `Aᵀv = g` (adjoint), with `dJ/dα = gᵀu + ∂J/∂α = vᵀf + ∂J/∂α`.
- **Unknowns.** Primal flow state U (or its sensitivity u), adjoint state v (equivalently multiplier λ), design vector α.
- **Constraints.** The discrete flow equations + b.c.'s, as an equality constraint. Geometric design constraints "easily incorporated by modifying the search direction" (§2.7.1, p. 398). Flow-dependent hard constraints require *one extra adjoint solve per constraint* (§2.7.1, p. 398); the soft-penalty alternative `J(U) + λ(J₂(U))²` is stated to worsen conditioning (p. 399).
- **Flow model.** Steady compressible Euler and Navier–Stokes on structured and unstructured grids; also a 1-D convection–diffusion toy operator for the continuous derivation (§3.2, p. 403). Shocks discussed but not the design driver.
- **Solver.** Time-marching to steady state `dU/dt + R(U) = 0`; the adjoint solved by the mirrored march `dv/dt + Lᵀv = g` (§2.8, p. 400), exploiting that "L and Lᵀ have the same eigenvalues" so the asymptotic convergence rate is identical. Edge-wise assembly `R ≡ Σₑ Rₑ(U)` gives `Lᵀv = Σₑ Lₑᵀ v` computed *without forming the matrix* (p. 401). Adjoint code obtained by hand, or by reverse-mode AD (Odyssée, ADIFOR/ADJIFOR; p. 401), with Griewank's guarantee that the flop count is "no more than three times that of the original nonlinear code" (p. 402, ref. [20]). Design march: steepest descent with *smoothed/preconditioned* gradients on partially converged solutions, or BFGS on fully converged ones (§2.6, p. 398).
- **Verification.** Two devices, both stated as used in practice by the authors: (i) the **complex-variable (complex-step) method**, `lim_{ε→0} I{R(U, α+iε)}/ε = ∂R/∂α`, evaluated at ε = 10⁻²⁰ with no subtractive cancellation (p. 402); (ii) the **dot-product/transposition identity**: "We have also used it to verify the correctness of our handcoded adjoint calculations by checking the identity `uᵀ(Lᵀv) = vᵀ(Lu)`, with the product Lᵀv being computed using the adjoint code, and the product `Lu = lim_{ε→0} I{R(U+iεu, α)}/ε` being computed using the complex variable method" (p. 402). Application-level "verification" is qualitative: Elliott–Peraire business-jet wing, objective reduced 75 % in two design iterations (p. 410); Reuther et al. multipoint drag reduction, Table II p. 413.

---

## 4. Hypotheses

### Declared
- Discrete flow equations and b.c.'s exactly satisfied at each design iteration (§2.4, p. 396).
- `R(U,α)` complex-analytic, for the complex-step device (p. 402, stated verbatim).
- Homogeneous b.c.'s in the first continuous derivation, relaxed later in §3.4 (p. 405).
- Gradient-based, local optimisation; §2.7.3 (p. 400) declares the limitation for integer design variables and multiple minima.
- Shocks (analytic formulation): treated as discontinuities with Rankine–Hugoniot enforced (§3.6, p. 407).

### Undeclared but necessary
- **Steady state throughout.** `N(U,α)=0` is a steady residual; there is no unsteady, periodic, or time-averaged objective anywhere in the paper. Time dependence appears only as the causality-reversal remark under Table I (p. 404).
- **Invertibility of A = ∂N/∂U** (and hence of Aᵀ) — required for both `Au=f` and `Aᵀv=g` to be well posed; never stated.
- **Local uniqueness / implicit-function differentiability of U(α)** — required for `dU/dα` to exist; never stated.
- **Differentiability of N and J in U and α** — the shock discussion is the admitted violation, handled separately and left open.
- **Smooth, differentiable mesh deformation X(α)** with `∂X/∂α` well defined at interior *and* surface nodes (asserted "usually non-zero", p. 396) — the mesh-motion operator's regularity is assumed, never analysed.
- **Fixed grid topology / fixed domain topology** across the design march.
- **Sufficient regularity for the integrations by parts** defining L* and the boundary operators B*, C* (§3.2, §3.4).
- **Single scalar objective**; no measure, no family of operating states in the theory (the multipoint case appears only in the reproduced application, §5).
- **Convergent time-marching** for the adjoint, argued from spectral identity of L and Lᵀ but with no statement about the transient / non-normality.

---

## 5. Findings (three levels)

Legend: level / tag / claim touched / evidence / confidence.

---

### TEORICO

**F1 — THREAT (ALTA) — touches P2/G14 (Rao = adjoint bridge).**
Giles & Pierce state explicitly, in §2.5 "Alternative Lagrange viewpoint" (p. 397), that the Lagrange-multiplier formulation `I(U,α) = J(U,α) − λᵀN(U,α)` with adjoint equation `(∂N/∂U)ᵀλ = (∂J/∂U)ᵀ` yields *the same object* as the duality formulation: **"The final equations are exactly the same as those derived by considering duality; it is really only the description of the mathematics which differs."** They add that "most people follow Jameson in adopting the Lagrange multiplier viewpoint … because of its connection to constrained optimisation and optimal control theory."
**Consequence for us:** the *generic* identification "adjoint variable ≡ Lagrange multiplier of the flow constraint" is textbook and pre-2000. A hostile referee can therefore attack P2/G14 as "trivially known" if we phrase it as a mathematical discovery. P2/G14 must be stated strictly as its query-bounded form already says: *no published work performs the identification **for the classical variational nozzle multiplier fields** (Route B: Hoffman 1967, Kraiko, Shmyglevskii, HTH) and exploits it.* Recommend an explicit sentence in M0/D3 that concedes the generic equivalence (citing this page) and localises the novelty to the corpus.
**Confidence: ALTA** (verbatim quote, unambiguous).

**F2 — GAP-CONFIRMS (ALTA) — touches P2/G14, D2-G3, the empty-niche claim.**
The canonical didactic origin story of the modern adjoint lineage, as told here (§1, p. 393), is: **optimal control [31] = Lions 1971 → "In fluid dynamics, the first use of adjoint equations for design was by Pironneau [37]" (JFM 64 (1974) 97–110) → Jameson [24–26] → Reuther/Elliott/Anderson/Mohammadi.** The **entire classical nozzle variational school is absent from the 46-item reference list** (pp. 413–415): no Rao, no Guderley, no Hantsch, no Hoffman, no Kraiko, no Shmyglevskii, no Sirazetdinov, no Nikol'skii, no Scofield, no Johnson–Thompson–Hoffman. Yet Hoffman 1967 and HTH-1971 had *already* adjoined the flow PDEs pointwise with multiplier fields and derived adjoint systems with the same characteristics as the flow, more than a decade before Jameson [24] (1988).
This is direct, primary-source, record-grade evidence that **the two schools never met**: the reference didactic account of adjoint design is written as if the nozzle school did not exist. It supports P2/G14 (nobody made the identification), G3 (no averaged shape theorem imported from there), and the empty-niche claim (nobody kept the variational-MoC formulation and swapped in a modern optimizer — the modern school did not even know the formulation).
**Confidence: ALTA** (exhaustive inspection of the printed reference list).

**F3 — THREAT (ALTA) — touches PB-2 ("first genuinely averaged shape problem") and D2-G3.**
§5 (p. 411) reports Reuther and co-authors [42] performing "a transonic multipoint wing design for a business jet configuration … the objective is to minimize drag for several flight conditions simultaneously", with 18 Hicks–Henne bumps at five span stations, 30 constraints, NPSOL, five design iterations; Table II (p. 413) gives the three design points (M = 0.81/0.82/0.83, C_L = 0.35/0.30/0.25) with drag going from 1.00257/1.00000/1.08731 to 0.85413/0.77915/0.76836 (normalised).
**Structurally this is a shared shape optimised against a finite family of operating states — i.e. J = Σᵢ wᵢ F[Σ; sᵢ], our J = ∫ F dμ with μ atomic.** It does *not* falsify D2-G3 as qualified (2026-08-13): it is not a nozzle formulation, there is no derivation of optimality conditions for the averaged problem (only computed numbers), no free-boundary/T4 counterpart, no measure theory, no traveling-wave inflow, and the family is over far-field flight conditions, not over a spatially nonuniform inflow. It does **not** falsify PB-2 either (no length-capped plug, no base pressure). **But it must be carried as named prior art for the "shared shape over a family of states" STRUCTURE**, alongside Kraiko–Osipov 1970 (trajectory measure) and ISABE-2003-117. Recommended litmap row: `Reuther, Jameson, Alonso, Rimlinger, Saunders, "Constrained multipoint aerodynamic shape optimisation using an adjoint formulation and parallel computers, Part 2", J. Aircraft 36(1) (1999) 61–74` — the adjoint-school ancestor of the atomic-measure case.
**Confidence: ALTA.**

**F4 — GAP-CONFIRMS (MEDIA) — touches T-T3 (collapse) and T-T3-MAP.**
Closing §5 (p. 412): **"While a single point design would achieve lower drag at the specified cruise conditions, the multipoint design has the advantage of maintaining better off-design performance [42]."** This is *asserted*, with no characterisation of when the two coincide, no theorem, and no hypothesis class. The adjoint school therefore has the *question* our T-T3 answers (when does the averaged optimum equal the single-state optimum?) but not a theorem, not even a statement of the failure mechanism. This is corroborating evidence that a collapse theorem with a named hypothesis set (H1–H4 + H2' + constant Pa) and a breaker map (T-T3-MAP) is an open niche, and that our positioning ("the corpus has the practice, we supply the collapse boundary") is fair.
**Confidence: MEDIA** (it is an assertion in an expository paper, so it evidences the *state of discourse*, not a proved absence).

---

### FORMALE

**F5 — CONTAINED (ALTA) — touches T7(b) (shared-wall Hadamard density) and our thrust functional.**
§3.4 "Boundary terms" (p. 405) gives the general adjoint identity
`(V, LU)_Ω + (C*V, BU)_∂Ω = (L*V, U)_Ω + (B*V, CU)_∂Ω`
and then states the admissibility restriction: **"it reveals that on a solid surface, the boundary integral term in the objective function must be a weighted integral of the linear perturbation in the pressure when using the Euler equations."**
Our thrust integrand `f1 = [(p − pa) + ρW² sin(φ−θ)cos θ / sin φ] q`, whose *wall* contribution to the shape derivative is the pressure-perturbation density, is exactly of the admissible class Giles–Pierce name for the Euler adjoint. So the (P)-objective sits inside the admissible objective class of the modern continuous-adjoint framework, under exactly the hypotheses: Euler, solid wall, boundary integral term. Register as containment *of us inside their admissibility condition* (a consistency check, not a restriction of their result).
**Confidence: ALTA.**

**F6 — ADOPT (ALTA) — touches F4b (fitted-front adjoint jump conditions) and [C-MAJDA].**
§3.6 (p. 407), verbatim: **"When considering shocked Euler flows, then in the analytic formulation, the shocks need to be treated as discontinuities across which the Rankine–Hugoniot shock jump relations are enforced [16]. This treatment leads to the result that the adjoint variables are continuous across the shock and that an additional adjoint boundary condition must be imposed along the length of the shock."** Plus: "Quasi-1D results have demonstrated that the continuous implementation naturally leads to satisfaction of the adjoint boundary condition at the shock [16]."
This is a **precise, checkable formal target for F4b**, and it is *not* the same statement as Kraiko's discontinuous multipliers (which jump along characteristics, Kraiko–Osipov Eq. (3.8)). The two are compatible — jump along characteristics, continuity across the shock, plus one extra condition *along* the front — but our F4b must say so explicitly instead of inheriting only the Kraiko side.
**Innesto:** F4b specification in M0 (fitted-front adjoint jump conditions) and the tier-1 certificate list. Adopt three items: (i) the continuity-across-the-front statement as a *derived requirement* to be re-derived in our fitted MoC setting; (ii) the "additional adjoint b.c. along the front" as a **new machine check** (an executable residual on the fitted sheet, alongside the Hoffman-E residual); (iii) the quasi-1D case as the natural known-answer oracle for it. Note also this bears on the *open* F4b item "certificate class for linearly-degenerate (CONTACT) fronts": Giles & Pierce's statement is for shocks only and says nothing about contacts, so it does not close that hole.
**Confidence: ALTA** (verbatim; the derivation itself is in their ref. [16], not reproduced here — so we inherit it as a *cited* result, not a proved one, and must re-derive it in our setting).

**F7 — CORRECTION (MEDIA) — touches VI.3 "captured-shock adjoints rejected per Giles-Ulbrich/Lozano".**
Two passages weaken the absolute form of our wording. p. 407: "In practice, researchers using the continuous adjoint approach do not enforce this b.c., and their results indicate no difficulties as a consequence." p. 409: **"In 2D and 3D there is no proof of second-order accuracy for quantities such as lift and drag, and there is a discontinuity in the gradient of the adjoint variables at the location of the shock. Therefore it remains an open question as to whether either approach will give a consistent approximation to the gradient of the objective function in the limit of infinite grid resolution. However, practical results for applications with weak shocks suggest that any inconsistency must be small."**
Our record wording ("differentiate the fitted front, never a captured smear; captured-shock adjoints rejected") is *not misattributed* — we cite Giles–Ulbrich, not this paper — but the primary lineage record shows the rejection is **a certifiability choice, not a demonstrated large-error result at weak shocks**. Recommended correction: in VI.3 and in the litmap, price the choice ("fitted because the front carries certificates we need — RH/entropy/Lax/Lopatinskii — and because the gradient consistency of the captured route is an open question in 2D/3D [Giles & Pierce 2000, p. 409]; at weak shocks the measured inconsistency is reported small"). This *strengthens* the claim's defensibility by removing an over-claim.
**Confidence: MEDIA** (the passage is 2000-vintage and predates the sharper Giles–Ulbrich result; the correction is to our rhetoric, not to our engineering decision).

**F8 — CONTAINED (ALTA) — touches the dual-route architecture (Route A closed form vs the discrete march) and VI.6 dual-route agreement.**
Figure 1 (p. 408, caption "Alternative approaches to forming discrete adjoint equations") plus §4 give the exact nomenclature of what our pipeline does with two routes: the *fully-discrete* path (discretise → linearise → transpose) and the *continuous* path (linearise → form adjoint p.d.e. → discretise), with an intermediate path also named. The text (p. 408) states: **"In principle, if each of the steps is performed correctly, and all of the solutions are sufficiently smooth (e.g. no shocks) then in the limit of infinite grid resolution all three approaches should be consistent and converge to the correct analytic value for the gradient of the objective function. However, there are important conceptual differences between the different approaches, and for finite resolution grids there will be differences in the computed results."**
Mapping of record: **our Route A closed-form adjoint (f2 first integral, CSTR_PA/CSTR_PB corner residuals) is the continuous branch; our Lemma-B(ii) reverse-AD of the assembled fitted march is the fully-discrete branch.** Their statement is exactly why our two-route agreement at 91/91 samples inside a derived cross-code band (max|dy| = 1.861e-03) is a *non-trivial oracle* rather than an algebraic identity — the routes are only asymptotically equal, and only on smooth solutions. Also worth adopting verbatim as the nomenclature paragraph of D3/M0 when we describe the dual route.
**Confidence: ALTA.**

---

### ALGORITMICO

**F9 — ADOPT (ALTA) — touches O3.1 / Lemma-B guarantee (claim 13).**
p. 402, verbatim: **"We have found this complex variable method to be extremely effective. We have also used it to verify the correctness of our handcoded adjoint calculations by checking the identity `uᵀ(Lᵀv) = vᵀ(Lu)`, with the product Lᵀv being computed using the adjoint code, and the product `Lu = lim_{ε→0} I{R(U+iεu, α)}/ε` being computed using the complex variable method."** The complex-step evaluation is stated at ε = 10⁻²⁰ with the explicit rationale that "there is no subtraction of two quantities which are almost equal; therefore there is no unacceptable loss of accuracy due to machine rounding error."
**This is the named classical antecedent of our O3.1 transposition identity — and it is strictly stronger than what we currently run.** Our O3.1 measures |⟨w, Jv⟩ − ⟨Jᵀw, v⟩| = 2.7e-10 vs derived tolerance 5.1e-8, but **both sides come from the same JAX code path** (the JVP and the VJP of the same `custom_vjp` unit processes), which is blind to a common-mode error in the forward rule itself: a wrong-but-consistently-transposed unit process passes. Giles & Pierce's version computes the *primal* side by an independent mechanism (complex-step on the original residual code), so a common-mode error is caught.
**Innesto, exactly:** (a) VI.6 oracle O3 — add an **independent-primal variant O3.1-cs**, in which `Jv` is produced by a complex-step (or independently coded finite-difference-free) evaluation of the march residual rather than by the JAX JVP, and the identity re-measured against a derived tolerance; (b) the negative-control set — the existing seeded-corruption control should be extended with a corruption that is *transpose-consistent but physically wrong*, which current O3.1 provably cannot detect and O3.1-cs should. Caveat to declare at adoption: complex-step through an *implicit* unit process requires the implicit solve itself to be run in complex arithmetic (or the implicit-function rule to be re-derived in the complex plane); this is a real implementation cost and should be scoped as an F2/S-CERT instrument, not a same-window patch.
**Confidence: ALTA.**

**F10 — GAP-CONFIRMS (ALTA) — touches the globality apparatus (δ = B − J[S*], mechanisms M1–M5, deflated continuation, sector tournament) and the (P) maximality argument.**
§2.7.3 "Limitations of Gradient-Based Optimisation" (p. 400): **"if the objective function contains multiple minima, then the gradient approach will generally converge to the nearest local minimum without searching for lower minima elsewhere in the design space. If the objective function is known to have multiple local minima, and possibly discontinuities, then again a stochastic search method may be more appropriate."** There is **no globality certificate, no bound ladder, no gap measure anywhere in the paper** — the deliverable of the modern adjoint school is a *gradient*, full stop. Combined with §4 (p. 409, "it remains an open question as to whether either approach will give a consistent approximation to the gradient … in the limit of infinite grid resolution"), the state of the art shipped here has neither a globality certificate nor a proved gradient-consistency guarantee at shocks.
This confirms as real the hole that our certified-globality clause (iv) of (P) fills, and supports the (P) maximality argument's sentence "unconditional global optimality on nonconvex infinite-dimensional PDE-constrained shape sets exists for nobody" — here is the canonical didactic reference conceding exactly that, and offering only stochastic search as the alternative.
**Confidence: ALTA.**

**F11 — ADOPT (MEDIA) — touches VI.5 (Riesz/Sobolev–Steklov-Poincaré gradient) and the tier-ladder margin constraint m(Σ) ≥ μ₀.**
Two operative statements. (i) §2.6 (p. 398): steepest descent works with **"partially-converged flow and adjoint solutions … as long as these gradients are properly smoothed (preconditioned) prior to updating α [26]. As a result, the cost per design cycle is relatively low"**, whereas quasi-Newton/BFGS "requires more accurate flow and adjoint solutions, which must generally be converged fully during each design iteration. As a result, the cost of each design cycle is significantly increased." They then concede: "We have been unable to find any reference which presents a clear quantitative comparison of the two approaches, but the anecdotal evidence is that the partially-converged approach yields the lowest total computational time" — **explicitly anecdotal, not proved.**
(ii) §2.7.1 (pp. 398–399): a *hard flow-dependent* constraint J₂(U(α),α) requires **"a second adjoint calculation; the addition of more flow-based hard constraints would require even more adjoint calculations. This type of constraint therefore undermines the computational cost benefits of the adjoint approach."**
**Two adoptions.** First, (i) is the earliest didactic statement of the gradient-smoothing lever our Riesz/Steklov–Poincaré representation implements; but note we run TR-SQP/TR-Newton with a *full Hessian per segment base*, i.e. the fully-converged branch, so their cost argument bites against us — this belongs in the S25/S25-bis speed ledger as a **registered, un-taken alternative** (partially-converged flow+adjoint with smoothed gradients), with the honest note that their own comparison is anecdotal. Second, (ii) prices something our cost model should state explicitly: **our margin constraint `m(Σ) ≥ μ₀` in the tier-ladder KKT is a flow-dependent hard constraint**, so by their accounting it carries a second-adjoint price per design step. Budget it in the F2 general-engine cost model rather than discovering it.
**Confidence: MEDIA** (the cost claims are asserted/anecdotal in the source; the structural point about the second adjoint is exact).

**F12 — CONTAINED (ALTA) — touches VI.2 (per-cell implicit `custom_vjp` assembled march) and Lemma B (ii).**
§2.8 (pp. 400–401) gives the structural ancestor of our assembled-march adjoint: with `R ≡ Σₑ Rₑ(U)` and `Lu = Σₑ Lₑ u`, one has `Lᵀ v = Σₑ Lₑᵀ v`, and **"At the programming level, this product involves exactly the same loop over all of the edges as for the original nonlinear flow discretisation … it is more efficient to calculate the product directly without explicitly constructing the matrix … this memory overhead can be avoided while maintaining an operation count that is not substantially greater than that of the original nonlinear solver."** The Navier–Stokes case gives the transposition-ordering rule `Lᵀv ≡ Aᵀv + DᵀVᵀv`, "indicating that the adjoint gradient subroutine responsible for Dᵀ must be applied *after* the viscous subroutine responsible for Vᵀ." Reverse-mode AD is offered as the alternative, with the flop bound "no more than three times that of the original nonlinear code" (p. 402, Griewank [20]).
Our Lemma-B(ii) construction — reverse-mode AD of the assembled fitted march equals the transposed discrete sweep, assembled per-cell through implicit `custom_vjp` unit processes and never materialising the Jacobian — is exactly this pattern, restricted to a *block-triangular x-marching* discretisation instead of a globally coupled edge-based one. Their claim is that this is an *iterative* transposed solve; ours is a *direct* transposed sweep because the march is block-triangular. That specialisation is ours and is worth stating as such (it is why we get an exact, non-iterative discrete adjoint, and why the O3.1 identity holds at 2.7e-10 rather than at an iteration tolerance).
**Confidence: ALTA.**

---

## 6. Bibliography inspection (record datum)

Full inspection of the 46 printed references, pp. 413–415.

**Classical nozzle line — ABSENT, 0/6 (and 0 for the wider school).**
No Rao. No Guderley. No Hantsch. No Hoffman. No Kraiko. No Shmyglevskii. Also no Nikol'skii, no Sirazetdinov, no Scofield, no Johnson–Thompson–Hoffman, no Osipov, no Tillyaeva, no PMM/JOTA/AIAA-1960s nozzle citation of any kind. **Not one reference to the variational maximum-thrust nozzle corpus.** The closest thing to internal-flow design in the whole list is [6] Cabuk, Shung & Modi, "Adjoint operator approach to shape design for internal incompressible flow" (Proc. 3rd Int. Conf. Inverse Design and Optimization in Engineering Sciences, 1991) — incompressible, not a nozzle, not the variational school.

**Modern adjoint line — PRESENT, and it is the paper's entire genealogy.**
- **Lions** [31]: *Optimal Control of Systems Governed by Partial Differential Equations*, Springer-Verlag, Berlin (1971), transl. S.K. Mitter. Cited in the very first sentence.
- **Pironneau** [37]: "On optimum design in fluid mechanics", *J. Fluid Mech.* **64** (1974) 97–110 — cited as "the first use of adjoint equations for design" in fluid dynamics.
- **Jameson** [24] J. Sci. Comput. 3 (1988) 233–260; [25] AIAA95-1729-CP; [26] in *CFD Review* (1995) 495–528; [27] J. Aircraft 36(1) (1999) 36–50; [28] Jameson, Pierce & Martinelli, AIAA 97-0101 (1997).
- **Giles** (self) [14] Comput. Fluid Dynamics J. 5(2) (1996) 247–258; [15] Giles & Pierce AIAA 97-1850; [16] Giles & Pierce, "On the properties of solutions of the adjoint Euler equations", ICFD (1998) 1–16; [17] AIAA 99-3293; [35], [36] Pierce & Giles adjoint recovery of superconvergent functionals.
- **Lozano — ABSENT** (his shock-adjoint work post-dates this 2000 paper; its absence is chronological, not a gap in their coverage).
- Supporting modern lines: Reuther et al. [39–42], Elliott & Peraire [9–11], Anderson et al. [1–3], Nielsen & Anderson [34], Mohammadi [32,33], Ta'asan et al. [44], Baysal & Eleshaky [4], Korivi–Taylor–Hou [29], Lewis & Agarwal [30], Huffman et al. [22], Newman III et al. [23], Dadone & Grossman [8]; AD tooling Griewank [20], ADIFOR [5], Carle et al. [7], Faure [12], Gilbert–Le Vey–Masse [13]; optimisation Gill et al. [18] *Practical Optimization*, NPSOL [19]; geometry Hicks & Henne [21], Rausch–Batina–Yang "method of springs" [38], Thompson–Warsi–Mastin [45]; complex-step Squire & Trapp [43]; error estimation Venditti & Darmofal [46].

**Record conclusion of the bibliography check:** the canonical didactic account of adjoint design, written by two of the field's principals, traces its ancestry to control theory (Lions) and to Pironneau/Jameson, and **is entirely unaware of — or at least entirely silent about — the 1955–1980 nozzle multiplier-field school that had already built the same machinery for a different problem.** This is exactly the disjointness our program's P2/G14, D2-G3 and empty-niche claims assert, documented from the other side.

---

## 7. Novelty of this paper vs. HTH-1971 / Hoffman 1967

**At the level of the adjoint/multiplier structure itself: essentially nothing new.** Hoffman 1967 and HTH-1971 already adjoin the flow PDEs pointwise with multiplier fields, derive adjoint systems sharing the flow's characteristics, and convert a redundant boundary condition into an optimality residual (Hoffman 1967 Eq. (78), Scofield–Hoffman Eq. (43)); Kraiko already had discontinuous multipliers with derived jump conditions. Giles & Pierce's §2.5 Lagrange derivation is, mathematically, the discrete finite-dimensional shadow of that.

**What Giles & Pierce genuinely add, relative to the 1967–1971 nozzle state of the art:**
1. **The discrete adjoint as a first-class object** — the transpose of the discretised linearisation, distinct from the discretisation of the continuous adjoint, with the three-path taxonomy of Figure 1 (p. 408) and the statement that the paths agree only asymptotically and only for smooth solutions.
2. **The exactness argument for design:** the fully-discrete gradient is the *exact* gradient of the discrete objective, so "the optimisation process can converge fully" (p. 408), whereas the continuous route's inconsistency means "the optimisation process will fail to converge further once the solution is near a local minimum" (p. 407).
3. **The AD route to the adjoint code**, with Griewank's ≤ 3× flop guarantee (p. 402) — i.e. the adjoint stops being a hand-derivation exercise.
4. **Verification instruments**: the complex-step derivative (ε = 10⁻²⁰, cancellation-free) and the `uᵀ(Lᵀv) = vᵀ(Lu)` identity as a *correctness test* (p. 402).
5. **The scaling/cost argument** `m ≪ p` (§2.2, p. 395) — the reason adjoints, not tangents, are the design tool when design variables are many.
6. **Green's-function interpretation** of the adjoint variables (§2.3 p. 395, §3.3 p. 404).
7. **Geometry-to-source machinery**: design perturbations entering as a volume source term f and inhomogeneous boundary term f₂ via grid deformation or the mapping `x = ξ + α̃X(ξ,η), y = η + α̃Y(ξ,η)` (§3.5, pp. 405–406) — a *domain-transformation* shape derivative rather than the boundary-localised Hadamard form our T7(b) uses.
8. **The shocked-adjoint facts**: continuity of the adjoint across an RH-enforced shock plus an extra adjoint b.c. along the shock (§3.6, p. 407).
9. **Admissibility restrictions on objectives/b.c.'s** for the Euler adjoint (§3.4, p. 405).

**What they do *not* have, that the nozzle school does:** any use of the flow's characteristic structure to *reduce* the problem — no control surface, no algebraic Euler–Lagrange system, no first integrals, no free-endpoint transversality, no closed-form optimal contour. Their flow model is a general discretised Euler/NS operator, which is precisely why no first integral is available: generality is bought at the cost of every classical closed form. **That trade is the exact seam our program occupies.**

---

## 8. Net verdict for the program

- **Nomenclature is fixed** (the stated purpose of putting this paper in the list): continuous vs discrete adjoint per Figure 1 (p. 408); duality (`Aᵀv=g`) ≡ Lagrange multiplier (`(∂N/∂U)ᵀλ = (∂J/∂U)ᵀ`) per §2.5 (p. 397); "gradient" = `dJ/dα = vᵀf + ∂J/∂α`. Use these words verbatim in M0/D3 when describing our dual route.
- **Yes, the history they tell skips the nozzle school entirely** — and that is now a documented record datum (F2), not an inference.
- **Two real adoptions**: the independent-primal transposition test (F9, hardens O3.1 against common-mode error) and the shocked-adjoint continuity + along-front b.c. as an F4b target and a new machine check (F6).
- **One correction to our rhetoric** (F7): the captured-shock rejection is a certifiability choice, not a demonstrated-error result at weak shocks.
- **One novelty-framing threat** (F1) and **one prior-art row to add** (F3, Reuther et al. multipoint = atomic-measure shared-shape ancestor).
- Nothing in this paper contradicts any theorem of record. No THREAT here is fatal; all are framing/citation obligations.
