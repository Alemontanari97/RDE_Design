# PROBLEM BRIEF — frozen formal statement (self-contained)

You are given a mathematical design-optimization problem. Everything you
need is in this brief. Do not consult any repository files, prior
documents, or external write-ups about this problem: your value lies in
an INDEPENDENT attack. Work from this statement alone (open literature
knowledge is welcome; any project-specific document is off-limits).

## 1. Physical setting

A rotating detonation engine (RDE) exhausts through a single, FIXED
axisymmetric nozzle. Because a detonation wave rotates in the annular
combustor at frequency f (kilohertz order; treat f and all timescales
as PARAMETERS, not asserted values), the nozzle inflow is not steady:
at each azimuthal station the product-gas state sweeps a CYCLE as the
wave passes. The design task: choose the one fixed nozzle shape that is
optimal for the whole cycle of inflow states.

## 2. Given data

- An envelope cylinder E (axisymmetric; length L_E, radius R_E)
  downstream of the annular combustor exit; a constant ambient
  pressure Pa > 0; an attachment set Λ (the chamber lip circle(s))
  where solid surfaces may be anchored.
- A fixed axisymmetric interface surface Γ_d, downstream of all heat
  release, carrying the inflow data: a family of gas states
  s(ξ) = (P, T, M, flow angle, ...) indexed by the cycle phase
  ξ ∈ Ξ, together with a probability measure μ on Ξ (the pushforward
  of normalized cycle time). HYPOTHESIS H-DATA (declared, monitorable,
  not guaranteed): the data family is a PURE PERIODIC ROTATING WAVE of
  a single mode (fixed wave count n; no mode transitions inside the
  family). How to detect/monitor violations of H-DATA is itself a
  design question you may address.
- Admissibility premises on the data (to be AUDITED, not assumed
  silently — the audit design is part of the problem): causal
  separation (no upstream influence of the design on the data through
  the interface), well-posedness of the per-state boundary data
  (complete data only where the axial flow is supersonic; where it is
  subsonic, an explicit closure must be declared), measurability in ξ.
- A constraint vector c: overall length bound L, maximum radius /
  envelope bound, wetted-length / size proxies, curvature and angle
  bounds, symmetry class. (Heat-load and mass limits enter only
  through these geometric proxies at this level of modelling.)
- Gas model (scope pin of the problem): the products are a FROZEN
  (chemically non-reacting downstream of Γ_d), THERMALLY PERFECT gas
  mixture — fixed composition, temperature-dependent caloric
  properties h(T), cp(T) (so γ = γ(T) is NOT constant); single phase
  (no condensed phase). Viscous effects are a declared model layer,
  the core state model is compressible Euler.

## 3. Design variable and admissible set

The design variable is the SOLID SET S ⊂ E (a compact axisymmetric
solid): the flow domain is Ω(S) = E \ S. Nozzle "configurations"
(bell, plug/aerospike, shrouded plug, expansion-deflection, ...) are
TOPOLOGY SECTORS of S — outputs of the optimization, not inputs.
Admissible set:
  A(c) = { S ⊂ E compact solid : uniform cone condition (h0, ω);
           attachment on Λ; g_i(S) <= c_i for the constraint vector c }.
How to parametrize S for computation (which function class, which
discretization, which regularity) is YOUR choice to derive and defend.

## 4. State model

For μ-a.e. phase ξ: the steady compressible Euler equations in
Ω(S) with inflow data s(ξ) on Γ_d, slip condition on the wetted solid
boundary, supersonic outflow (where achieved), ambient pressure Pa on
free portions of the control boundary. The gas is the frozen
thermally-perfect mixture above. What solution class to work in
(smooth / piecewise-smooth with fitted fronts / weak), how to certify
membership, and what to do about non-uniqueness of multi-dimensional
weak solutions are YOUR calls to derive and defend.

An additional per-phase STATE CONSTRAINT: certified optima must keep
the flow ATTACHED on every phase (a separation margin g_sep(S; s(ξ))
<= 0 for μ-a.e. ξ, with an explicit detection criterion); designs that
separate exit the certified class.

## 5. Objective

The ultimate target is the EXACT time-averaged axial thrust of the
unsteady flow:
  J_exact[S] = lim_{T→∞} (1/T) ∫_0^T F_S(t) dt,
  F_S(t) = ∫ [ρ u_x (u·n) + (p − Pa) n_x] dA
over any enclosing axisymmetric control surface. If the limit is not
known to exist, the declared objects are the liminf/limsup variants
(certified brackets). A natural computable surrogate is the
CYCLE-AVERAGED objective
  J[S] = ∫_Ξ F[S; s(ξ)] dμ(ξ),
with F the steady per-state thrust functional. Whether and when the
surrogate is exact, what corrections apply at finite wave frequency
(the unsteadiness/residence-time ratio — a Strouhal-type number — is
MARGINAL, neither ≪1 nor ≫1, in the regimes of interest; treat its
value as a parameter to be measured, not given), and how to BOUND
|J_exact − J| are part of the problem (requirement (v) below).

## 6. The problem (find, with certificates)

Find the PAIR (S*, δ) such that:
 (i)   EXISTENCE: S* ∈ argmax over the admissible class of J (state
       the function-class and compactness structure that makes the
       argmax exist, or the monitored failure boundary if existence
       can fail);
 (ii)  STATIONARITY: S* satisfies first-order optimality conditions
       for the averaged problem — derive them (per-phase adjoint /
       variational conditions coupled through the SHARED contour,
       averaged wall condition, endpoint/transversality conditions,
       active-constraint complementarity with multipliers carrying
       marginal-value meaning);
 (iii) CURVATURE: second-order condition (reduced Hessian ⪯ 0 on the
       active tangent cone) — verifiable form;
 (iv)  GLOBALITY, certified: a mechanism delivering
       J[S*] >= sup_{A(c)} J − δ with δ COMPUTED (e.g. via upper
       bounds B: δ = B − J[S*]), and δ = 0 PROVEN wherever structure
       permits;
 (v)   DECLARED ERROR BARS: |J_exact − J[S*]| bounded by named,
       evaluable terms (unsteadiness correction, model residuals,
       discretization error), each with an explicit carrier or a
       declared absence.
Every numerical tolerance must be DERIVED (no magic constants), every
claim must name its hypotheses and a falsifier: a test that could
REJECT it.

## 7. Your deliverable — an ATTACK TREE

Produce a complete attack tree for this problem from your lens:

- FORMULATION FAMILIES: the viable overall formulations you see
  (how to relate J_exact to computable objectives; which idealization
  ladder; which state model / solution concept; which design
  representation; which optimality framework; which globality
  mechanism; which error-control framework), with the criteria that
  select among them.
- FORKS: every substantive decision point as a numbered node:
  FORK-<k>: {question; options (each stated at its genuine best);
  decision criterion (what evidence/theorem/measurement decides it);
  your recommendation with grounds; what would falsify that
  recommendation}.
  BREADTH REQUIREMENT: at each fork, enumerate the FULL
  state-of-the-art option space the open literature offers for that
  specific sub-problem — including, wherever applicable, families
  outside the classical deterministic toolbox (evolutionary/genetic
  and other derivative-free global searches; design-of-experiments,
  surrogate and Bayesian-optimization approaches to geometry;
  level-set and topology-optimization representations; stochastic
  and robust formulations; machine-learned surrogates with
  verification). Do not prune to the obvious classics: an option may
  be rejected at its fork, but it must appear and be rejected FOR A
  STATED REASON, not by omission.
- DRY-LEVEL PROOFS: where a fork is decidable by a short argument
  (a lemma, a counterexample, a scaling estimate), give the argument
  at proof-sketch level with hypotheses explicit.
- ORDER OF BATTLE: the dependency order in which you would attack the
  forks, and which forks are load-bearing (a wrong early choice
  poisons everything) vs local.

Be exhaustive on forks: parametrization of the design, treatment of
the sonic region and of any embedded discontinuities, mesh/refinement
policy, error estimators and safety factors, optimality-system
discretization order (optimize-then-discretize vs
discretize-then-optimize), optimizer class and globalization,
handling of the certification boundary (designs whose state cannot be
certified), aggregation of per-phase constraints, derivative
computation (adjoint/AD/FD) and its verification, stopping and
tolerance derivation, and the unsteady-correction structure of (v).

FORMAT: write your tree as structured markdown with the FORK-<k>
schema above. Number every fork. Keep prose tight; the tree is the
deliverable, not an essay.
