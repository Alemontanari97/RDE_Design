# Expert read — Zahr, Persson & Wilkening, fully discrete time-periodicity-constrained adjoint

Reader: literature-review agent, convergence review, 2026-08-13.
Metro di confronto: `00_APPARATUS_BRIEF.md` (record state of the cycle-averaged variational nozzle program).

---

## 1. Citation (verified from the PDF itself)

M. J. Zahr (a,1,*), P.-O. Persson (b,2), J. Wilkening (b,2), **"A Fully Discrete Adjoint Method
for Optimization of Flow Problems on Deforming Domains with Time-Periodicity Constraints"**.
(a) Institute for Computational and Mathematical Engineering, Stanford University, Stanford,
CA 94305. (b) Department of Mathematics and Lawrence Berkeley National Laboratory, University
of California, Berkeley, CA 94720-3840.
arXiv stamp printed in the left margin of p. 1: **arXiv:1512.00616v2 [math.OC] 12 Aug 2016**.
Footer of p. 1: "Preprint submitted to Elsevier — July 25, 2018".
No journal name, volume, page range or DOI is printed anywhere in the document. 34 pages,
83 references, one appendix (Appendix A). Funding: DOE CSGF DE-FG02-97ER25308 (MZ);
DOE DE-AC02-05CH11231 (PP, JW), p. 29-30.

> Record caution: the venue is NOT printed on this artifact. Cite as the arXiv preprint
> unless the journal version is separately procured and page-verified.

## 2. Read coverage

**34 / 34 pages read in full** (pp. 1-29 body + Appendix A; pp. 30-34 references [1]-[83]).
Nothing was skipped. Figures 1-16 and Tables 1-2 were read as rendered images; numeric values
quoted below are read off Table 1 and Table 2 text, not off figure pixels. No supplementary
material is referenced or attached.

## 3. What the paper actually does

**Problem.** Compute *and optimize over* time-periodic (cyclic steady-state) solutions of
parametrized PDEs on deforming domains. Motivating application: the energetically optimal
flapping motion of a 2-D NACA0012 airfoil in compressible viscous flow, minimizing total work
subject to **zero time-averaged x-impulse** (a time-averaged thrust constraint).

**Formulation.** Semi-discretize (Eq. 3, p. 4) `M du/dt = r(u, mu, t)`, `u(0) = u(T)`; discretize
in time with an s-stage DIRK scheme (Eqs. 4-5, p. 4). Time periodicity becomes the **algebraic
constraint u^(0) = u^(N_t)** (Eq. 6, p. 4), which "turns the problem into a nonlinear two-point
boundary value problem, which eliminates the possibility of using traditional evolution methods
(since the initial conditions are unknown)" (p. 5). The QoI is the space-time integral (Eq. 2,
p. 3) discretized **solver-consistently**, i.e. the discrete functional depends on the RK stages,
`F(u^(0),...,u^(N_t), k_1^(1),...,k_s^(N_t))` (Eq. 7, p. 4).

The design problem (Eq. 40, p. 15) is the nested / Generalized-Reduced-Gradient form: strict
enforcement of the time-periodic discrete PDE lets the implicit function theorem define
`u^(n)(mu)`, `k_i^(n)(mu)`, reducing to `min_mu F(...)` s.t. `c(...) >= 0` (Eq. 39, p. 14).
The continuous statement of the application (Eq. 55, p. 23): `min_{U,mu} W(U,mu)` s.t.
`J_x(U,mu) = 0`, `U(x,0) = U(x,T)`, Euler/NS conservation law in `Omega(mu,t)`; fully discrete
counterpart Eq. (56), p. 23.

**Unknowns.** (i) The periodic initial condition `u_0 in R^{N_u}` (all spatial DOFs at t=0);
(ii) the design vector `mu`. In §4.1, `mu` is 8 sinusoid parameters (Eq. 53, p. 17, held fixed).
In §4.2, `mu` = **the knots of periodic cubic splines describing the heaving/pitching kinematics,
N_mu = 8** — with only 4 true DOFs each because the half-period mirror condition (Eq. 57, p. 23)
`h(mu,t) = -h(mu,t+T/2)`, `theta(mu,t) = -theta(mu,t+T/2)` prescribes one knot from the other
four (footnote 3, p. 25). **The airfoil geometry itself is never a design variable.**

**Constraints.** The time-periodicity constraint (Eq. 6); the discrete PDE; and one nonlinear
output constraint, `J_x = 0` (time-averaged x-impulse identically zero).

**Flow model.** Compressible Navier-Stokes (Eqs. 41-44, p. 15) with **the isentropic assumption**
`s = p/rho^gamma` constant (Eq. 46, p. 15), which "explicitly relates the pressure and density of
the flow, rendering the energy equation redundant" (p. 16), reducing the system from `n_sd+2` to
`n_sd+1` equations. `gamma = 1.4`, `Pr = 0.72`, constant `mu`. ALE form on a fixed reference
domain via a mapping G (Eqs. 47-50, pp. 16), GCL-satisfying. Numerics: nodal DG, **polynomial
degree 3 on 978 triangles**, compact DG viscous fluxes, `Re = 1000`, `M = 0.2`, third-order DIRK
with **100 equally spaced steps per period**, `T = 5` (pp. 17-18). All partial derivatives
`dr/du, dr/dmu, df_h/du, df_h/dmu` are obtained by **automatic symbolic differentiation at the
element level with MAPLE** plus assembly (p. 16).

**Solvers.**
- Primal: matrix-free **Newton-Krylov shooting** (Algorithm 2, p. 8) on `R(u_0) = u^(N_t)(u_0) - u_0 = 0`
  (Eq. 14), Jacobian-vector products `J(u_0)v = du^(N_t)/du_0 v - v` (Eq. 17) obtained from *one*
  linear directional-sensitivity evolution (Eq. 18, p. 7). Compared against fixed-point iteration
  (Algorithm 1, p. 5) and against unconstrained optimization of `j(u_0) = ½||u^(N_t)-u_0||²`
  (Eqs. 10-13, p. 6) with steepest descent / L-BFGS.
- **Nonlinear preconditioning**: m fixed-point cycle iterations as warm start (m = 0, 1, 5).
- Dual: the fully discrete periodic adjoint (Eq. 30, p. 11) is a **linear two-point BVP**, solved
  by matrix-free **GMRES** (Algorithm 3, p. 13) on `A x = b`, `A = d lambda^(0)/d lambda_{N_t} - I`
  (Eq. 34, p. 11), matvecs from the adjoint sensitivity equations (Eq. 37, p. 12).
- Outer optimizer: **SNOPT** (ref. [79]), nested/GRG, two periodic adjoint solves per iteration
  (one per QoI), primal tolerance `||u^(0) - u^(N_t)||_2 <= 1e-10` (Eq. 58, p. 25), Newton-Krylov
  linear tolerance `1e-3`, adjoint GMRES tolerance `1e-4`, warm-started from m = 5 (p. 25).

**Verification.**
1. **Stability of the periodic orbit** (§2.3, Eqs. 19-22, pp. 8-9): eigenvalues of `du^(N_t)/du_0`
   at the periodic solution must have modulus < 1. Figure 9 (p. 23): "First 200 eigenvalues ...
   with largest magnitude. All eigenvalues lie in unit circle, thus the periodic orbit is stable."
2. **Existence and uniqueness of the periodic adjoint** — PROVEN in Appendix A (pp. 28-29) via
   the transposition identity Eq. (A.7): `d lambda^(0)/d lambda_{N_t} = (du^(N_t)/du_0)^T`, so
   nonsingularity of the primal periodic Jacobian `du^(N_t)/du_0 - I` implies nonsingularity of
   `d lambda^(0)/d lambda_{N_t} - I`.
3. **Gradient verification against 2nd-order centered FD** on the *manifold of periodic solutions*
   (i.e. re-converging the periodic problem at each perturbed mu). Table 2, p. 22, e.g.
   `dW/dA_h`: adjoint **-2.3091901647e+01** vs FD **-2.3091901345e+01**; `dJ_x/dA_theta`: adjoint
   **6.7297082256e+00** vs FD **6.7297089105e+00**. Figure 11 caption (p. 24): "match the finite
   difference approximation to nearly 7 digits before round-off errors degrade the accuracy."
   "To realize the sub-1e-6 finite difference errors in the time-periodic gradient, **tolerances
   of 1e-12 were used for the primal and dual time-periodic solves**" (p. 22).
4. **Solver comparison**, Table 1 (p. 20). At m = 0: fixed-point 90 primal solves to 8.10e-07;
   Newton-Krylov(1e-2) 9 primal + 128 sensitivity solves to 4.41e-08; steepest descent / L-BFGS
   "not included in the m = 0 study due to lack of convergence issues". At m = 5: steepest descent
   reaches only 4.65e-01 and L-BFGS 7.40e-02 after 125 primal + 125 adjoint solves, while
   Newton-Krylov(1e-2) reaches 3.50e-08 in 10 primal + 92 sensitivity solves.
5. Optimization result: "After 16 periodic optimization iterations, the first-order optimality
   conditions have been reduced by two orders of magnitude" (p. 25); heaving amplitude reduced by
   more than a factor of two, pitching amplitude increased to **18.7 deg**; total work "more than
   an order of magnitude smaller than at the initial guess"; abstract: "In less than 20
   optimization iterations, the flapping energy was reduced nearly an order of magnitude and the
   thrust constraint satisfied to 5 digits of accuracy" (p. 1).

**What is PROVEN vs ASSERTED.** Proven: Appendix A (existence/uniqueness of the discrete periodic
adjoint, conditional on nonsingularity of the primal periodic Jacobian). Everything else is
*derivation* (the adjoint equations Eqs. 26-31 are an exact algebraic consequence of Eq. 25 —
correct but not a theorem with hypotheses) plus *numerical assertion* (stability, convergence,
gradient accuracy, optimality of the flapping motion — all measured on one instance, no error
bound, no convergence-rate theorem). There is **no theorem** about the optimization problem
(no existence of an optimum, no second-order conditions, no globality statement).

## 4. Hypotheses

**Declared.**
- H-D1. Temporally first-order PDE, or recast as such (p. 3).
- H-D2. DIRK time discretization (stated as convenient, not fundamental: "this is not a
  fundamental restriction of this work", p. 4).
- H-D3. Fixed mass matrix M (the ALE reference-domain formulation "leads to a constant mass
  matrix. Therefore, attention will be restricted to the case of a fixed mass matrix", p. 4).
- H-D4. Isentropic flow, `s = p/rho^gamma` constant, energy equation dropped (Eqs. 45-46, p. 15).
- H-D5. Ideal gas, `gamma = 1.4`, constant `Pr = 0.72`, constant viscosity (p. 15).
- H-D6. Nonsingularity of `du^(N_t)/du_0 - I` at the periodic solution ("which is assumed
  non-singular at a time-periodic solution", p. 28).
- H-D7. Stability of the periodic orbit for the fixed-point / Newton-Krylov machinery to work
  ("fixed point iteration relies on transient modes being damped by the evolution equations, i.e.
  on the periodic solution being stable and attracting", p. 8).
- H-D8. Geometric Conservation Law enforced by the ALE modifications (p. 16, refs [72,73]).

**Undeclared but necessary.**
- H-U1. **The period T is known a priori and externally imposed by the forcing.** T = 5 throughout
  (p. 17, p. 25); the kinematics *is* the forcing. There is **no phase condition and no unknown
  period** — autonomous / self-sustained periodic orbits (where the period is an eigenvalue of the
  problem) are silently outside the framework. This is the single most consequential unstated
  restriction for any RDE application.
- H-U2. **Uniform (Lebesgue) time measure.** The averaged QoI is `int_0^T ... dt` (Eqs. 2, 51);
  no weighting, no pushforward, no measure-theoretic hypotheses. Any non-uniform cycle measure
  would have to enter the discretization by hand.
- H-U3. **Smoothness / differentiability of the discrete state map and of F in every argument**,
  hence no shocks, no state-dependent switching, no free boundaries. The instance is viscous,
  subsonic (M = 0.2), Re = 1000, shock-free. Non-smooth cases are never mentioned.
- H-U4. **The domain deformation mapping G is prescribed analytically as a function of mu**
  (rigid-body motion, Eq. 54, p. 17), so `dr/dmu` is exact by symbolic differentiation. Genuine
  *shape* design (a mesh-deformation chain rule and a geometry parametrization) is delegated to
  ref [54] and is NOT exercised here.
- H-U5. **The periodic orbit is locally unique / isolated** at the given mu, and remains so along
  the entire optimization path — otherwise `u^(n)(mu)` in Eq. (39) is not a well-defined implicit
  function and the reduced gradient is meaningless. Verified a posteriori at one point (Fig. 9),
  never along the design path.
- H-U6. **Continuity of the periodic branch in mu** — required for the FD gradient check on the
  manifold (p. 22) and for SNOPT's line search; no continuation safeguard is described.
- H-U7. Low-Mach validity of the isentropic reduction (they cite the incompressible-limit results
  [69,70,71] for M -> 0, but M = 0.2 is asserted as "a good compromise", p. 17 — not proven).
- H-U8. The Krylov subspace dimension suffices without preconditioning ("economical, matrix-free
  preconditioners could result in non-trivial speedups", p. 28 — an admitted open item).

## 5. Novelty vs. the state of the art (as the paper itself frames it)

The paper's own novelty claim (abstract, p. 1; §1, p. 2; Conclusion, p. 28) is: **the derivation of
the fully discrete adjoint equations for a time-periodically constrained PDE**, showing they form a
*linear two-point boundary value problem* (not a backward evolution), proving that BVP solvable,
and using it to compute *exact* discrete gradients on the manifold of periodic solutions. Prior
art it explicitly positions against: (i) harmonic-balance / time-spectral / NLFD methods
([26] Hall-Thomas-Clark, [27] Gopinath-Jameson, [28] McMullen-Jameson-Alonso, [29]
Nadarajah-Jameson) — spectral in time but couple all time instances into a space-time tensor
product; (ii) shooting / Newton-Krylov periodic solvers ([17, 33-38, 40-48]) — no adjoint;
(iii) fully discrete unsteady adjoints ([51-54]) — no periodicity constraint, initialized from
steady state and run through transients; (iv) continuous unsteady adjoints ([55, 56]) — "may
result in inexact gradients and slow optimization convergence if the spatial discretization
employed is not adjoint consistent" (p. 2); (v) Stanford-Beran [57] — spectral time
discretization enforcing periodicity, but on a *dry* structure without fluid.

This is a **methods paper in the modern discrete-adjoint school**. It is not a nozzle paper, not a
variational-nozzle paper, and it makes no claim about optimal-thrust contouring. Relative to
HTH-1971 / Hoffman-1967 (our classical baseline) it is simply a different literature: it adds
nothing to, and takes nothing from, the classical maximum-thrust variational line — see §7.

## 6. Findings (three levels)

### TEORICO

**T-1 — GAP-CONFIRMS — D2 gap G3 (no averaged shape theorem in the corpus). Confidence ALTA.**
This paper *does* optimize a cycle-averaged quantity with genuinely unsteady dynamics inside the
constraint (Eq. 55, p. 23: `min W` s.t. `J_x = 0`, `U(x,0)=U(x,T)`, conservation law in
`Omega(mu,t)`) — and it is the closest thing in the read corpus to our averaged design problem.
But it is **not** a counterexample to G3, on four independent counts, each anchored:
(i) the averaged object is the time history of **one single periodic orbit**, not a shape shared
across a *family* of mutually independent inflow states — there is no `Xi`, no `mu(xi)`, no
per-phase state;
(ii) the measure is uniform Lebesgue on [0,T] (Eqs. 2, 51), with no measure-theoretic apparatus;
(iii) **the geometry is fixed**: the design vector is the 8 spline knots of the *kinematics*
("The vector of parameters, mu — used as optimization parameters — are the knots of the cubic
splines. This leads to N_mu = 8 parameters", p. 25), the airfoil is a NACA0012 throughout;
(iv) there is no free-boundary / T4-type counterpart of any kind.
G3 as qualified on 2026-08-13 ("spatially nonuniform traveling/rotating-wave inflow with genuinely
unsteady dynamics in the constraint") survives intact — and this paper sharpens *why* the
qualification is the right one: the unsteady-adjoint school averages over a trajectory, never over
an exogenous measure-indexed family.

**T-2 — GAP-CONFIRMS — periodic-wave-data-scope / T-T0 (wave-frame exactness). Confidence ALTA.**
Their entire periodicity mechanism presupposes a **known, externally imposed period**: "corresponds
to the motion in Figure 2 with period T = 5" (p. 17); "where t is time and T = 5 is the fixed
period of the flapping motion" (p. 25). The cycle is *forced* by the prescribed kinematics
(Eqs. 52, 57). There is no phase condition and no unknown-period formulation anywhere in the paper.
In an RDE the cycle period is an **output** (set by the detonation wave speed), so this machinery
does not transfer to RDE data without an added phase condition and an augmented Newton system.
This is direct external support for our scope pin and for T-T0: the wave-frame reduction converts
an unknown-period time-periodic BVP into a steady problem with an unknown wave speed — exactly the
object our "Newton-Krylov + Arnoldi wave-frame anchor" is built for. Record it as evidence that the
wave-frame route is not merely convenient but *avoids a structural hole* in the periodic-shooting
route.

**T-3 — GAP-CONFIRMS — robust CVaR/DRO layer ("idle, not absent"). Confidence ALTA.**
Their own Conclusion names our exact failure mode as an open problem: "One extension of this work
is the development of robust solvers for determining **nearly** time-periodic solutions of problems
where a time-periodic solution does not exist, but exhibits **quasi-cyclic behavior**. An example
of such a problem is the 3D turbulent flow around periodically driven bodies such as helicopter and
windmill blades" (p. 28). An RDE with mode competition / wave-number drift is precisely such a
problem. This is independent, third-party confirmation that when our **T0-flatness monitor fails**,
the state of the art has *no* method — i.e. the robust layer in our architecture is load-bearing,
not decorative, and it is the right architectural place for the failure to be routed.

**T-4 — THREAT (bounded) — nicchia-vuota / D2-G3 barrier-to-entry. Confidence MEDIA.**
Our niche claims are query-bounded statements about what *has been done*, but this paper shows the
missing ingredient is one composition away. The companion work is cited as ref [54]:
"M. J. Zahr and P.-O. Persson, *Fully-discrete, time-dependent adjoint method for high-order
discontinuous galerkin discretizations on deforming domains: Application to pde-constrained
optimization*, Journal of Computational Physics, 2016" — and p. 16 states: "Additional details
regarding computation of the partial derivatives with respect to mu in the case of a
**parametrized, deforming domain** are provided in [54]." So shape/deforming-domain design and
periodicity-constrained adjoints already exist in the *same* codebase from the *same* authors.
Anyone who composes [54] + this paper on a nozzle geometry with a periodic inflow enters the G3
neighbourhood. This does **not** touch claim #8 (the empty niche is "keep the variational MoC
formulation and swap in a modern optimizer" — there is no MoC, no characteristic surface, no
classical variational formulation anywhere in this paper), and it does not touch T-T3 / T-T4 /
PB-2. But the "no one has done it" defence should be paired, in the paper, with "and here is why
the naive composition does not solve our problem" — the answers being T-2 (unknown period), the
exogenous measure (T-1(ii)), and the supersonic/inviscid/shock-fitted regime (H-U3).

### FORMALE

**F-1 — ADOPT — Appendix A, Eq. (A.7): the monodromy transposition identity, with an existence
proof. Confidence ALTA. Innesto: oracle O3 family + Lemma-B (reading ii) + F5 (RDE).**
Appendix A proves `d lambda^(0)/d lambda_{N_t} = (du^(N_t)/du_0)^T` (Eq. A.7, p. 29) by taking
`F = v^T u^(N_t)` and observing the resulting adjoint recursion (Eq. A.4) is *identical* to the
adjoint sensitivity recursion (Eq. 32), hence `(du^(N_t)/du_0)^T v = (d lambda^(0)/d lambda_{N_t}) v`
for all v (Eq. A.6). Two things we should take:
(a) **the identity itself is our O3.1 / Lemma-B transposition identity closed over a full cycle**
rather than over one march — the correct generalization if F5 ever computes a time-periodic field
instead of a family of quasi-steady phases;
(b) **it is used as an existence-and-uniqueness theorem**, not merely as a numerical check: the
transpose of a nonsingular operator is nonsingular, therefore the adjoint two-point BVP is uniquely
solvable. Our Lemma-B (reading ii) currently has a *machine witness* (2.7e-10 vs derived tolerance
5.1e-8) and existence only by block-triangularity of the march. The Appendix-A pattern — derive the
adjoint operator, prove it is the transpose of the (assumed-nonsingular) forward operator, conclude
solvability — is the argument shape to reuse if we ever close a loop (periodicity, or a
free-boundary fixed-point) in the march.

**F-2 — ADOPT — solver-consistent discretization of the quantity of interest. Confidence ALTA.
Innesto: cycle layer VI.4 (mu-quadrature) and the DWR bar in VI.6.**
"While any numerical quadrature formula can be used to perform the discretization of the space-time
integral, this may lead to a truncation error of different orders for the governing equations and
the quantity of interest. This implies there is wasted effort since the largest order will
dominate. A solver-consistent discretization of the quantities of interest [54] — where the spatial
and temporal discretization of the partial differential equation are also used for the quantity of
interest — can be used to circumvent this wasted effort" (pp. 4-5). Consequently their discrete
functional depends on the RK **stages** (Eq. 7, p. 4), and p. 5 warns: "A standard numerical
quadrature, such as midpoint rule or Simpson's rule, would *not* use the stages, which are only
low-order solutions of (3)". Our VI.4 splits Gauss panels at switch phases for a *different*
reason (non-smoothness / O(1/N)); the order-matching principle is complementary and currently
unwritten: the mu-quadrature order should be *derived from* the per-phase MoC unit-process order
(O(h²)) and the DWR bar, not chosen independently. Register as a rule in VI.4 with its own
falsifier (a refinement study where tightening only the mu-quadrature does not move J beyond the
D2 bar proves the quadrature was not the binding error).

**F-3 — THREAT (bounded, structural) — containment claim (#18). Confidence ALTA.**
The time-periodicity constraint `u^(0) = u^(N_t)` (Eq. 6, p. 4; adjoined as the residual
`r_tilde^(0)(u^(0), u^(N_t)) = u^(0) - u^(N_t) = 0` in Eq. 23, p. 9) is a **state-space coupling
across the cycle** that (P) structurally cannot express: our phases are mutually independent
quasi-steady S1 states indexed by an exogenous mu, so there is no object in (P) that couples
phase `xi = 0` to phase `xi = 1`. Its formal signature is exactly one term: the periodic adjoint
terminal condition is `lambda^(N_t) = lambda^(0) + (dF/du^(N_t))^T` (Eq. 30, first line, p. 11)
instead of the march adjoint's `lambda^(N_t) = (dF/du^(N_t))^T` — the extra `lambda^(0)` is the
multiplier of the periodicity residual, and setting it to zero recovers the ordinary
(non-periodic) discrete adjoint.
Claim #18 is *literally* untouched — it is bounded to "the inviscid-Euler exogenous-measure CORE of
every variational maximum-thrust nozzle formulation in the read corpus", and this is neither a
nozzle nor a variational max-thrust formulation. But if the corpus is ever widened to unsteady
design, this is a **third declared structural non-containment**, alongside Kraiko-Osipov's
endogenous trajectory-adjoint weight (§6(g)) and boundary-layer-terms-in-the-functional (§6(c)).
Declaring it pre-emptively is cheaper than being handed it by a referee.

### ALGORITMICO

**A-1 — ADOPT — Floquet / monodromy-spectrum certificate for the cycle. Confidence ALTA.
Innesto: stage-A audits of CycleFamily (VI.1), next to the T0-flatness certificate.**
§2.3 (Eqs. 19-22, pp. 8-9) defines orbit stability as `|eig(du^(N_t)/du_0)| < 1` and Figure 9
(p. 23) reports "First 200 eigenvalues ... with largest magnitude. All eigenvalues lie in unit
circle, thus the periodic orbit is stable." Our certificate stack has **no analogue**: the
T0-flatness / harmonic-decay certificate attests that the *data* is a single rotating mode; it says
nothing about whether the underlying orbit is stable and isolated. For imported RDE data this
distinction matters — a marginally stable or bifurcating orbit is exactly where H-U5/H-U6 fail and
where "the same nozzle serves all phases" stops being a well-posed premise. Add a monodromy /
dominant-Floquet-multiplier estimate (Arnoldi on the existing wave-frame anchor gives it nearly
free) as a **declared coverage item** of the CycleFamily contract, with an explicit
NOT-COMPUTED-FOR-IMPORTED-DATA disclosure until it is.

**A-2 — ADOPT — the gradient-verification protocol and its tolerance discipline. Confidence ALTA.
Innesto: oracle O4 (freezing-adjoint dOmega/dSigma vs FD of continued waves) tolerance derivation.**
Their FD check is done **on the manifold**: "The finite difference approximation to gradients on
the aforementioned manifold requires finding the *time-periodic* solution of the governing
equations *at perturbations* about the nominal parameter configuration" (p. 22) — i.e. the periodic
problem is re-converged at each perturbed mu, which is precisely O4's design. The quantitative
discipline is the part we do not yet have written down: "To realize the sub-1e-6 finite difference
errors in the time-periodic gradient, **tolerances of 1e-12 were used for the primal and dual
time-periodic solves**" (p. 22) — a six-order gap between inner solve tolerance and target gradient
accuracy — plus a **tau sweep** (Fig. 11, p. 24, tau from 1e-8 to 1e-2) exhibiting the
truncation/round-off minimum rather than a single tau. Achieved agreement: Table 2, p. 22, e.g.
`dW/dA_h` adjoint -2.3091901647e+01 vs FD -2.3091901345e+01 (agreement to ~9 significant figures on
that entry; the caption of Fig. 11 states "nearly 7 digits" for the relative vector norms).
Our O4 should carry the same three elements: re-convergence at perturbed design, a derived inner
tolerance (not an inherited default), and a tau sweep with the minimum reported — otherwise an O4
"pass" may be measuring solver noise.

**A-3 — ADOPT / CONTAINED-aligned — Newton-Krylov shooting beats optimization-based shooting,
measured. Confidence ALTA. Innesto: the wave-frame anchor (Newton-Krylov + Arnoldi) already in
our tooling — this is the evidence that it must NOT be built as an optimization-based shooting.**
Table 1 (p. 20) is a clean, pre-registered-style comparison at three levels of nonlinear
preconditioning. At m = 0: fixed-point 90 primal solves reaching 8.10e-07; Newton-Krylov(1e-2)
9 primal + 128 sensitivity solves reaching 4.41e-08; steepest descent and L-BFGS excluded "due to
lack of convergence issues" (caption Fig. 5, p. 20). At m = 5: steepest descent stalls at 4.65e-01
and L-BFGS at 7.40e-02 after 125 primal + 125 adjoint solves, while Newton-Krylov(1e-2) reaches
3.50e-08 in 10 primal + 92 sensitivity solves. Two transferable facts: (i) minimizing
`½||u^(N_t)-u_0||²` is a *decisively inferior* route to a cyclic steady state versus solving
`R(u_0)=0` by Newton-Krylov — relevant the moment F5 needs a wave-frame anchor; (ii) their cost
model, "the linearized equations (sensitivity and adjoint) are about 2x less expensive to solve
than the nonlinear, primal equations" (p. 18; same ratio derived on p. 7), is the right shape of
accounting for our own S25 speed ledger — count *linear* solves separately from nonlinear ones,
because nonlinear preconditioning trades the former for the latter ("this does not save many
primal solvers — since the nonlinear preconditioning requires primal solves — but requires far
fewer linear system iterations", p. 18).

**A-4 — ADOPT (minor) — QoI-independent adjoint operator enables multi-RHS Krylov.
Confidence MEDIA. Innesto: VI.6 certificate stack when several constraints/oracles share the
transposed march.**
"The adjoint sensitivity equations in (37) are *independent* of the quantity of interest, F. If
there are multiple quantities of interest, fast multiple right-hand side solvers [66, 67, 68] could
be used to solve `Ax = b` as the matrix A will be fixed and only the right-hand side varied.
Furthermore, the adjoint sensitivity equations in (37) and the adjoint equations in (32) are
identical, with the exception of the terms `dF/du^(n-1)` and `dF/dk_i^(n)`. Therefore, the adjoint
sensitivities are less expensive to compute than the adjoint states" (p. 12). In our reduced-space
driver, the active-set constraints {L, eps_max, lip, truncation} and the O3-family oracles all
consume the *same* transposed march operator with different seeds; the structural observation
(fixed A, varying b) is the justification for batching those transposed sweeps rather than
re-deriving each.

## 7. Bibliography inspection (record datum)

References [1]-[83], pp. 30-34, read in full.

**Classical variational nozzle line: ENTIRELY ABSENT.** No Rao. No Guderley. No Hantsch. No
Hoffman (the "Jones and Yamaleev" in [53] and "Nielsen, Diskin, Yamaleev" in [51] are unrelated).
No Kraiko. No Shmyglevskii. No Sirazetdinov, no Nikol'skii, no Scofield. No Russian-school entry of
any kind. Not one nozzle paper appears in 83 references.

**Modern adjoint line: PARTIALLY present, Jameson-branch only.**
- Jameson branch present: [27] Gopinath & Jameson (time spectral); [28] McMullen, Jameson & Alonso
  (nonlinear frequency domain); [29] Nadarajah & Jameson (unsteady 3-D shape design, J. Aircraft
  44(5) 1513-1527, 2007); [50] Culbreth, Allaneau & Jameson (high-fidelity flapping optimization);
  [55] Nadarajah & Jameson (continuous and discrete unsteady adjoint, AIAA J. 45:1478-1491);
  [56] Economon, Palacios & Alonso (unsteady continuous adjoint on dynamic meshes, AIAA J. 53(9)).
- Discrete unsteady adjoint: [51] Nielsen, Diskin & Yamaleev; [52] van Schrojenstein Lantman &
  Fidkowski; [53] Jones & Yamaleev; [54] Zahr & Persson (JCP 2016, self-citation, the load-bearing
  companion).
- Control/optimization background: [64] Gunzburger, *Perspectives in flow control and optimization*,
  SIAM 2003; [61] Gill, Murray & Wright; [63] Nocedal & Wright; [79] SNOPT (Gill, Murray & Saunders).
- **ABSENT: Giles. ABSENT: Pironneau. ABSENT: Lozano. ABSENT: J.-L. Lions.**
  Record caution against a plausible mis-reading: reference [70] is
  "B. Desjardins, E. Grenier, **P.-L. Lions** and N. Masmoudi, *Incompressible limit for solutions of
  the isentropic navier-stokes equations with dirichlet boundary conditions*, J. Math. Pures Appl.
  78(5):461-471, 1999" — that is **Pierre-Louis** Lions on the incompressible limit, cited for the
  isentropic reduction, **not** Jacques-Louis Lions on optimal control of PDEs. The adjoint-control
  founding line is not cited.

**Interpretation for claim P2/G14 (Rao = adjoint bridge).** This is a strong, clean data point for
the record: a 2016 methods paper written at the technical centre of the modern discrete-adjoint
school, on periodic-flow optimization with an averaged thrust constraint, cites **zero** works from
the classical variational nozzle line. The two literatures do not touch, in this direction either.
It does not *prove* P2/G14 (novelty claims stay query-bounded, claim #20), but it is exactly the
kind of negative evidence the claim rests on, and it is now page-verified.

## 8. Summary verdict for the program

- **No claim of record is falsified or weakened by this paper.**
- Three gaps we declare are independently confirmed (T-1 on G3, T-2 on the wave-frame scope pin,
  T-3 on the robust layer).
- One bounded threat to register (T-4): the composition [54] + this paper is the cheapest route
  for someone else into the G3 neighbourhood; the paper should pre-empt it by naming the three
  obstructions (unknown period, exogenous measure, supersonic/shock-fitted regime).
- One bounded structural non-containment to declare pre-emptively (F-3).
- **Five concrete ADOPTs**, in descending value: A-2 (O4 tolerance discipline — cheapest, highest
  immediate rigor return), F-1 (Appendix-A existence-by-transposition argument shape), A-1
  (Floquet/monodromy certificate for CycleFamily), F-2 (solver-consistent QoI quadrature order),
  A-3 (Newton-Krylov over optimization-based shooting for the wave-frame anchor) — plus A-4 minor.
