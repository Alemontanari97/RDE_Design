# DOSSIER — Uno published paper FULL READ (44/44 pages)

**Agent**: UNO FULL-READ (S-FOUNDATIONS-C3, user-ordered integral reading, depth
concern of record). **Date**: 2026-08-20.
**Object**: `literature/uno_paper.pdf` = Vanaret & Leyffer, *Implementing a
unified solver for nonlinearly constrained optimization*, Mathematical
Programming Computation, DOI 10.1007/s12532-026-00310-9, published online
10 June 2026, Open Access CC-BY (Received 19 June 2024 / Accepted 22 February
2026). 44 pages, **no text layer**: every page rendered via pymupdf
(`page.get_pixmap(dpi=120)`) to PNG and read as image; renders cross-checked
against the searchable preprint
`literature/vanaret_leyffer_2026_uno_unified_solver_mpc_arxiv2406_13454.pdf`
(v2, 38 pp, text layer extracted to scratchpad).
**Local clone consulted READ-ONLY**: `Uno/` at v2.8.0-45-gbfb79936
(HEAD 2026-08-19), files `docs/presets.md`, `docs/options.md`.
**PDF metadata note**: embedded title = the DOI filename
(`s12532-026-00310-9.pdf`), embedded author = the local user (an artifact of
the download/print chain, not of the work) — citations must use the
bibliographic identity above, never the file metadata.

**DISCIPLINE**: this dossier INFORMS; it does not adjudicate. C31's verdict
stands as-is until [P-IPADJ]; the pinned A/B decides. No ledger/registry edits
ride this file.

---

## 1. INGREDIENT MAP — the unifying framework's building blocks

The paper's abstract claims **eight building blocks** (p.1). The §3 prose
(pp.4-5) lists SEVEN highlighted strategy ingredients organized in FOUR
layers; the eighth block is the **Subproblem** composite object itself
(Fig. 3 "Definition of a Subproblem", p.16; Fig. 5 UML, p.38 — exactly eight
abstract classes: GlobalizationMechanism, ConstraintRelaxationStrategy,
InequalityHandlingMethod, Subproblem, SubproblemSolver, HessianModel,
InertiaCorrectionStrategy, GlobalizationStrategy). Reading note of record:
"eight" is honest only on the UML/class count; the §3 bullet list alone shows
seven.

Layer/ingredient map, with realizing strategies as published and the NEEDS of
a certified design loop each answers (our program vocabulary where genuine):

**Reformulation layer**
- **(1) Constraint relaxation strategy** (§4.2, pp.9-10): guarantees
  well-defined, feasible subproblems. Strategies: **l1 relaxation** (Eq. (6):
  min rho*f + ||c||_1, inverse penalty rho, steering rules; exact under mild
  conditions, Thm 14.3.1 of [18] cited) and **feasibility restoration**
  (Eq. (7): min ||c(x)||; "any (local) solution x* with ||c(x*)|| > 0 is a
  certificate that (NLP) is (locally) infeasible", p.10). The wheel (Fig. 1,
  p.6) also lists "relaxation / augmented Lagrangian / proximal term" arcs at
  framework level. NEEDS answered: constraint-set handling under linearized
  inconsistency; **infeasible-outcome certificate semantics** — the engine can
  CLOSE an infeasibility verdict, not just fail (guard-alphabet input for
  F-C31-3, §3 below).
- **(2) Inequality handling method** (§4.3, pp.10-11): the combinatorics of
  inequalities. Strategies: **inequality-constrained** (SQP/IQP via active-set
  QP solver; SLP as H=0 special case; quadratic local convergence once the
  active set settles), **equality-constrained** (EQP two-phase, e.g. SLPEQP),
  **interior-point** (primal-dual IPM: x_i z_i = mu, fraction-to-the-boundary,
  mu -> 0; primal barrier variant). NEEDS: **active-set/multiplier crispness
  at boundary-active optima vs log-barrier smearing** — exactly the panel's
  W2 axis vocabulary.

**Subproblem layer**
- **(3) Hessian model** (§4.4, p.11): exact / quasi-Newton (BFGS, SR1,
  limited-memory) / identity / zero, plus structured curvature (barrier or
  proximal diagonal terms) injected by the reformulations. CLAIM-BOUND: in
  Uno **2.2.0 quasi-Newton is NOT implemented** (§5.3.5 p.17: exact-declared
  but matrix-absent degrades to "zero" WITH a printed warning; §8 p.38:
  L-BFGS/SR1 = future work). NEEDS: curvature-policy interface (our C32
  adjacency; certificate-grade curvature stays OUR duty — nothing here
  supplies S* spectra).
- **(4) Inertia correction strategy** (§4.5, p.12): none / primal (H + delta*I)
  / primal-dual (delta_w, delta_c on the augmented matrix, Eq. (9)); target
  inertia (n, m, 0) via factorization codes (MA57). NEEDS: descent-direction
  guarantee for line search — a globalization-guarantee precondition, and the
  declared mechanism by which the KKT system is made factorizable (relevant to
  multiplier quality: dual regularization delta_c perturbs the multiplier
  system, a fact any multiplier-provenance audit must carry).

**Subproblem solver layer**
- **(5) Subproblem solver** (§5.3.1 p.15): QP/LP/linear-system solvers as
  interfaced components: **BQPD** (null-space active-set for NONCONVEX QPs;
  **accepts Hessian-vector products / a Hessian linear operator instead of an
  explicit matrix**), MA57/MA27/MUMPS (sparse symmetric indefinite), HiGHS
  (LP; QP not yet supported through Uno). Planned: GALAHAD TRS. NEEDS:
  the concrete consumption point for curvature products (bears on C32/C33
  challenger shapes, note-only).

**Globalization layer**
- **(6) Globalization strategy** (§4.1, pp.6-9): accepts/rejects trial
  iterates. Three progress measures monitored throughout (p.7):
  infeasibility eta, objective omega_pi (parameterized by the FJ objective
  multiplier pi >= 0), auxiliary xi (barrier/proximal terms), with predicted
  reductions linked to the subproblem (§5.3.3 — "as much as possible, a given
  combination of strategies is meaningful", sufficient-decrease/Cauchy
  fraction assumption stated p.16). Strategies described: **merit functions**
  (§4.1.1, Armijo condition Eq. (4)) and **filter methods** (§4.1.2,
  envelope conditions with beta/gamma, switching condition, Armijo on the
  decrease function phi, upper bound U; filter flushed when mu updates,
  p.20). **The funnel method appears ONLY as a label in the wheel (Fig. 1,
  p.6)** — no subsection, no semantics, no experiment anywhere in the 44
  pages (verified against the preprint: same). NEEDS: globalization
  guarantees (global convergence to stationary points/feasible limits, cited
  to [19,22,47,48], not re-proven here).
- **(7) Globalization mechanism** (§4.6, pp.12-13): line search (backtracking,
  descent-direction requirement) / trust region (radius management, active-TR
  radius increase rule, negative curvature bounded) / proximal term (wheel
  arc). NEEDS: recourse action semantics — including IEEE-exception recovery
  (§5.3.8 p.18: radius reduction / step-length reduction on FP exceptions),
  which is a robustness fact our integrator-backed evaluations care about.

**(8) Subproblem** (composite; §5.3.2 p.15, Fig. 3 p.16): reformulated
problem + current primal-dual iterate + Hessian model + inertia correction +
possible TR radius; auto-defines progress measures, correct-inertia matrix,
admissible solvers. NEEDS: the automatic-composition guarantee ("no
programming effort" combination) — the feature that makes an
options-composed variant (arm-B funnel rider) a FIRST-CLASS object rather
than a code fork.

Framework-level unification evidence: Table 6 (p.40) characterizes 15 SOTA
solvers (ALGLIB, CONOPT, FICO XSLP, filterSQP, IPOPT, KNITRO-ASM/-IPM,
LANCELOT, LOQO, MINOS, NAG, NLPQL, SLSQP, SNOPT, SQuID, WORHP) by the same
ingredients; FICO XSLP flagged as the only one with no proper globalization
strategy (§4.7 p.13).

---

## 2. PRESET/CONFIG TABLE of record

### 2.1 Presets as PUBLISHED (§5.2, p.14 — Uno 2.2.0)

Presets "automatically connect the eight ingredients and set hyperparameter
values from the solvers' documentations". **Exactly TWO presets exist in the
published paper**:

| Preset | Mimics | Composition (published words) | Declared NON-implemented vs the original |
|---|---|---|---|
| `filtersqp` | filterSQP [19,20] | trust-region restoration filter SQP | second-order correction steps |
| `ipopt` | IPOPT [49] | line-search restoration filter interior-point | SOC steps, scaling, least-square multipliers, iterative refinement, iterative bound relaxations, non-monotone techniques, soft feasibility restoration |

**There is NO funnel preset in the published paper.** Additional published
constraint (p.14): Uno 2.2.0 **prohibits interior-point + trust-region**
combinations ("resolved in later Uno versions"). Automatic instantiation
rules (§5.3.5 p.17): QP vs LP solver picked by subproblem curvature;
unconstrained reformulation => NoRelaxation + l1MeritFunction + BoxLPSolver;
exact-Hessian-without-matrix => "zero" + warning.

### 2.2 Presets at the LOCAL CLONE (Uno v2.8.0-45-gbfb79936, docs/presets.md, READ-ONLY)

Still exactly two named presets + a default chooser: `filtersqp`, `ipopt`,
and **`auto`** (default; oracle: if n+m >= 2000 or nnz(grad c)+nnz(Hess L) >=
50000 pick `ipopt`, else `filtersqp`). Values from `uno/options/Presets.cpp`:

`filtersqp` preset (v2.8.0): constraint_relaxation_strategy =
feasibility_restoration; inequality_handling_method =
inequality_constrained; hessian_model = exact; inertia_correction_strategy =
none; globalization_mechanism = TR; globalization_strategy =
fletcher_filter_method; filter_type = standard; progress_norm = L1;
residual_norm = L2; TR_radius = 10; l1_constraint_violation_coefficient = 1;
**primal_tolerance = 1e-6; dual_tolerance = 1e-6**;
switch_to_optimality_requires_linearized_feasibility = true;
protect_actual_reduction_against_roundoff = false. QP solver auto-chosen
among available (BQPD/HiGHS).

`ipopt` preset (v2.8.0): feasibility_restoration; interior_point;
barrier_function = log; hessian_model = exact; inertia_correction_strategy =
primal_dual; globalization_mechanism = LS; globalization_strategy =
waechter_filter_method; filter_type = standard; filter_beta = 0.99999;
filter_gamma = 1e-8; switching_delta = 1; filter_ubd = 1e4; filter_fact =
1e4; filter_switching_infeasibility_exponent = 1.1;
armijo_decrease_fraction = 1e-8; LS_backtracking_ratio = 0.5;
LS_min_step_length = 5e-7; barrier_tau_min = 0.99; barrier_damping_factor =
1e-5; l1_constraint_violation_coefficient = 1000; progress_norm = L1;
residual_norm = INF; **primal_tolerance = 1e-8; dual_tolerance = 1e-8;
loose_primal_tolerance = 1e-6; loose_dual_tolerance = 1e-6;
loose_tolerance_iteration_threshold = 15**;
switch_to_optimality_requires_linearized_feasibility = false;
LS_scale_duals_with_step_length = true;
protect_actual_reduction_against_roundoff = true. Linear solver auto-chosen
(MA57/MA27/MA86/MUMPS/SSIDS).

### 2.3 The funnel-variant composition (arm-B candidate rider of C31)

Confirmed at source: **funnel is an options-selected globalization strategy,
NOT a preset**, exactly as the C31 ledger rider states. At v2.8.0
(docs/options.md): `globalization_strategy` admits `merit_function`,
`fletcher_filter_method`, `waechter_filter_method`, **`funnel_method`**. A
funnel variant is therefore composed as:

    preset=filtersqp  (or explicit ingredient options)
    globalization_strategy=funnel_method
    + the seven funnel options (defaults from DefaultOptions.cpp):
      funnel_kappa = 0.5           (convex-combination coefficient, funnel update)
      funnel_beta = 0.9999         (infeasibility sufficient-reduction fraction)
      funnel_gamma = 0.001         (objective sufficient-reduction slope)
      funnel_ubd = 1.0             (min initial infeasibility upper bound)
      funnel_fact = 1.5            (initial-infeasibility multiple for the bound)
      funnel_update_strategy = 1   (update rule 1, 2, or 3)
      funnel_require_acceptance_wrt_current_iterate = false

**Version pin of record**: the PAPER (2.2.0) contains no funnel content at
all; the funnel options above are v2.8.0-docs facts. Any armed funnel variant
must be version-stamped and re-verified against the INSTALLED Uno (and its
semantics source-adjudicated from Uno code + the funnel literature — the
paper cannot serve as its source).

Other option families relevant to composing/pinning a configuration
(options.md): ingredients table (constraint_relaxation_strategy =
feasibility_restoration only, at v2.8.0 docs; hessian_model gains `LBFGS`,
`LSR1` vs the paper; inertia_correction_strategy primal/primal_dual/none;
globalization_mechanism TR/LS), termination family (primal/dual tolerance,
loose pair + iteration threshold, max_iterations = 2000, time_limit,
unbounded_objective_threshold = -1e20), switching family (switching_delta =
0.999, switching_infeasibility_exponent = 2), merit
(sufficient_infeasibility_decrease_ratio = 0.9), filter family (beta 0.999,
gamma 0.001, ubd 1e2, fact 1.25, capacity 50, reset thresholds), Armijo
(armijo_decrease_fraction = 1e-4, armijo_tolerance = 1e-9), progress_norm /
residual_norm, residual_scaling_threshold = 100.

---

## 3. ARM-B SPEC INPUTS (for the pinned A/B; VERDICT_wave2 §1.1 falsifiers read first)

Context of record: F-C31-1 ([P-IPADJ] incumbent-semantics leg or
barrier-restart overhead out of band => A/B MANDATORY), F-C31-2 (arm B beats
arm A on W2+W3 at non-worse W1/W4 => flip; arm A wins => IP path CERTIFIED;
falsifier-two certification CONDITIONED on falsifier-one semantics leg
passing — ledger rider), F-C31-3 (identical-certified-outcomes guard
violation => protocol red). Inputs the 44 pages actually provide:

1. **Termination-status alphabet (§5.3.7, pp.17-18)** — Uno terminates at
   (x*, y*, z*, pi*) in one of DECLARED classes: (a) **feasible KKT point**
   (CQ holds, pi* > 0); (b) **feasible FJ point** (CQ fails, pi* = 0); (c)
   **infeasible stationary point** (local min of constraint violation, with a
   complementarity condition on violated constraints, norm-dependent); (d)
   primal feasibility + TR radius ~ machine epsilon (non-differentiable /
   erroneous gradients / SLP class); (e) **loose-tolerance termination**:
   strict eps unattainable but 100*eps held for e.g. 15 consecutive
   iterations (preset values: 1e-8 strict / 1e-6 loose @ 15). The paper's own
   framing: "we check for termination, rather than for optimality". THIS is
   the guard vocabulary for F-C31-3: identical-certified-outcomes must
   compare TERMINATION CLASS, not objective values alone; class (e) and (d)
   exits are not the same certified outcome as class (a).
2. **Multiplier availability/quality at solution** — full primal-dual iterate
   returned; scaled Lagrangian/FJ formulation (§2.1) makes the CQ status
   EXPLICIT via pi* (KKT recoverable by scaling Eq. (2a) by 1/pi* when
   pi* > 0). Stationarity residual computed via EvaluationSpace
   Jacobian-transposed-vector products (§5.3.6). Caveat carried: 2.2.0
   implements NO least-square multiplier refinement (declared unimplemented
   IPOPT feature, §5.2), and dual inertia regularization (delta_c) perturbs
   the multiplier system (§4.5) — multiplier PROVENANCE on the arm-B side is
   "as-computed by the globalized iteration", to be consumed under the same
   INFORMATION-ONLY discipline until measured.
3. **Warm-start/restart** — the paper documents NO warm-start interface: the
   abstract algorithm starts from a given (x0, y0, z0) (initial point only);
   the ipopt-preset filter is FLUSHED whenever mu updates (p.20); §8's
   future-work list (quasi-Newton, MINRES, SLP-EQP, SQuID, parallel line
   search, more subproblem-solver interfaces) contains no warm-start item.
   ARM-B PIN: no warm-start API is to be ASSUMED; W3 must be measured as
   total evals + restart churn across the RK-G segment walk on both arms
   (BQPD's active-set estimate lives inside one solve; nothing is claimed
   across solves).
4. **Constraint-set handling for the matched-set requirement** — the general
   form (1) l <= {c(x); Ax; x} <= u (p.2) natively separates nonlinear /
   linear / bound classes with two-sided bounds and unbounded entries; the IP
   path converts inequalities to slacks internally (§6.2 p.19). Our
   constraint classes map 1:1 without reformulation on our side — the
   matched-constraint-set discipline (RC28-1 class) is realizable at the
   interface level.
5. **Hessian provisioning pin (A/B validity)** — §5.3.5: in 2.2.0, declaring
   an exact Hessian while providing neither an explicit matrix nor a linear
   operator silently degrades the model to "zero" (with only a printed
   warning). An arm-B run that fails to wire OUR per-segment Hessian through
   the interface would run a zero-curvature method while arm A runs exact —
   an invalid A/B that could still "terminate". The spec must assert the
   Hessian path (explicit matrix or BQPD linear operator) and REJECT runs
   whose logs show the degrade warning.
6. **Preset-fidelity bound** — the ipopt preset is NOT IPOPT: 12 CUTE
   instances (core1, csfi2, discs, growth, hs085, hs093, hs114, launch,
   meyer3, polak6, spanhyd, vanderm4) solved by IPOPT but not by the preset,
   attributed to the unimplemented features (p.26). For the A/B this cuts
   BOTH ways: arm-B results are Uno-filtersqp results, not filterSQP results;
   no transfer claims across the mimicry boundary.
7. **Benchmark scope vs our class** — evaluation is 429 SMALL CUTE problems
   (Table 1 pp.21-24: n up to ~96, m up to ~91), AMPL-translated, metric =
   OBJECTIVE EVALUATION COUNTS (performance profiles Fig. 4 p.25; shifted
   geometric means Table 2 p.26: filtersqp 18.08 / filterSQP 18.73 / ipopt
   preset 48.45 / IPOPT 34.63; failures priced at 1e6), no wall-clock, no
   large-scale, logs public (nonlinear_optimization_solver_benchmark repo).
   Transfer statement: the size class is actually NEAR our n~10 dense
   per-segment NLPs, and eval-count economics is the RIGHT axis for our
   expensive integrator-backed evaluations (panel W4 vocabulary) — but the
   CUTE evaluations are cheap closed-form, so no timing conclusion transfers;
   only the eval-count/robustness pattern does, and only as candidate-order
   evidence.
8. **Infeasibility certificate** — restoration convergence with residual > 0
   = local-infeasibility certificate (§4.2.2): gives the A/B a DECLARED
   outcome class for infeasible-subproblem episodes instead of an undefined
   failure (guard alphabet, again).
9. **Robustness facts usable as falsifier instrumentation** — IEEE-exception
   recovery via globalization mechanism (§5.3.8); TR-radius-active
   enlargement rule and restoration switching (§6.1); filter-flush-on-mu
   semantics (§6.2). These are the mechanisms whose LOGS an A/B protocol can
   record to explain eval-count differences (churn attribution).
10. **Version stamp duty** — paper = 2.2.0; local clone docs = v2.8.0 (auto
    preset, LBFGS/LSR1, funnel options present). The A/B spec and any
    [P-IPADJ]-grade source adjudication of arm B must pin the INSTALLED
    version and re-verify presets/options at that version; install remains an
    O5-class session-boundary decision (W5 asymmetry unchanged).

---

## 4. CLAIM-BOUNDS — what the paper does NOT establish (its own declared limits)

1. **No convergence theory of its own.** Global-convergence properties are
   cited (filter SQP [19,22], line-search filter [47,48], etc.), never
   re-proven; explicitly: "While all combinations do not lead to convergent
   methods, some of them result in efficient solvers that may not exist as
   software implementations" (p.2, §5.2 p.14). Never cite this paper as
   PROOF that a given composed variant converges.
2. **Funnel: label only.** "Funnel method" exists solely as a wheel arc
   (Fig. 1). No definition, no update rule, no theory, no preset, no
   experiment. Any sentence of the form "Uno's funnel method per the MPC
   paper ..." is above content. Funnel semantics must be sourced from Uno
   code/docs (v-stamped) + the funnel literature.
3. **Quasi-Newton absent from the evaluated artifact.** §4.4 describes
   BFGS/SR1 at FRAMEWORK level; Uno 2.2.0 implements none (§5.3.5 warning
   path; §8 future work). The published numbers are exact-Hessian only.
4. **Preset mimicry is bounded, and measured so.** filtersqp preset: no SOC;
   ipopt preset: seven named IPOPT features missing, 12 named instances lost
   (p.26). "Closely mimic" (§7) is the paper's claim — equivalence is not.
5. **Evaluation scope.** Small CUTE only; eval counts only; "preliminary
   numerical results" (§1 p.3, self-description); no wall time, no memory, no
   large-scale, no real-world classes; MPCC/robust optimization named as
   TARGET areas (§1, §8), zero experiments there. IP+TR combination
   prohibited in 2.2.0 (p.14).
6. **No warm-start capability is claimed anywhere** (see §3 item 3).
7. **Termination ≠ certified optimality.** §5.3.7's own framing plus the
   loose-tolerance and TR-collapse exit classes mean "solved" in Tables 2-5
   is per those status classes at the solvers' own defaults; the paper does
   not claim certified optima, and neither may anyone citing it.
8. **Solver-comparison numbers are configuration-bound.** Competitors run at
   fixed published versions (filterSQP 20010817, IPOPT 3.14.20, SNOPT
   7.5-1.2, MINOS 5.51, LANCELOT, LOQO 7.03, CONOPT 3.17A) with AMPL
   translations and failure-pricing conventions (1e6); IPOPT "too few degrees
   of freedom" exits counted as failures (p.20). Rankings do not transfer
   outside that harness.

---

## 5. [DELTA] ITEMS — published vs preprint (and vs local clone)

Published-vs-preprint (arXiv 2406.13454 v2):
- **[DELTA-1] Layout only**: 38 pp (preprint) -> 44 pp (Springer typeset).
  Section structure verified IDENTICAL by heading-by-heading comparison
  (§1..§8 including all §4.x/§5.3.x/§6.x subsections); same Uno version
  (2.2.0), same two presets, same experiments/tables/figures, same
  Argonot/ISMP-2018 footnote.
- **[DELTA-2] No substantive content delta found** at the resolution of this
  read (funnel-only-in-wheel is common to both — preprint grep: exactly one
  "funnel" hit, the Fig. 1 label; presets/features/limits sentences
  identical in wording wherever cross-checked).

Paper-vs-LOCAL-CLONE (v2.8.0-45-gbfb79936; declared for version hygiene, not
paper deltas):
- **[DELTA-3]** `auto` default preset with a size/nnz oracle (not in the
  paper).
- **[DELTA-4]** hessian_model admits `LBFGS`/`LSR1` at v2.8.0 docs (2.2.0:
  not implemented).
- **[DELTA-5]** funnel_method + seven funnel_* options documented at v2.8.0
  (2.2.0 paper: label only). Also MA86/SSIDS linear solvers, HSL runtime
  loading, filter_capacity/reset machinery — none of it citable to the
  paper.

---

## 6. CONFRONT — full read vs the C31 convergence analysis of record

**Method**: non-relitigation. Anchors: PANEL_C31TRIO.md §1.1 MAIN QUESTION
(:88-99) + criteria W1 (:103-107), W2 (:108-115), W3 (:116-119), W4
(:120-123), W5 (:124-129), WIN RULE (:130-137); VERDICT_wave2.md §1.1
falsifier definitions (:180-197), §2.1 row verdict (:483-520), §4.1 ledger
delta (:926-938); docs/choice_ledger.yaml C31 row as landed (:461-473,
including the E2/arm-B preset rider and the confirm-lens conditioning).
Each substantive dossier finding gets ONE verdict: CONSISTENT / TENSION /
ENRICHMENT. The row's own protocol governs throughout; nothing here
re-adjudicates.

| # | Finding (dossier anchor) | Verdict | One-line disposition |
|---|---|---|---|
| 1 | Uno = open-source C++/MIT, MPC-published, ingredient semantics documented (§1) | **CONSISTENT** | Supports the W1 source-adjudicability requirement for the FLIP CANDIDATE exactly as the verdict ordered it (:502); moves nothing on the incumbent gate. |
| 2 | Published presets = filtersqp/ipopt ONLY; funnel = options-selected `globalization_strategy=funnel_method`, confirmed at paper p.14 AND at v2.8.0 presets.md/options.md (§2.1-2.3) | **CONSISTENT** | Source-proves the ledger's arm-B wording rider verbatim (ledger :473 "presets = filtersqp/ipopt only ... DECLARED options-selected variant"); the verdict's shorthand "(filterSQP/funnel preset)" at :502 was already repaired by that rider — this read closes the loop at source. |
| 3 | Termination-status alphabet incl. FJ/KKT pi* distinction, infeasible-stationary certificate, loose-tolerance and TR-collapse exits (§3.1, §3.8) | **ENRICHMENT** | Proposed one-line delta for the A/B spec (landing/C4 window): "the F-C31-3 identical-certified-outcomes guard compares TERMINATION CLASS {feasible-KKT, feasible-FJ, infeasible-stationary, TR-collapse, loose-tolerance} at matched tolerances; any class divergence at the declared resolution = protocol red, regardless of objective agreement." |
| 4 | Matched tolerances are preset-asymmetric (filtersqp 1e-6/1e-6 vs ipopt 1e-8+loose; §2.2) | **ENRICHMENT** | A/B spec pin: "arm-B primal/dual tolerances set to the incumbent's certified band, loose-tolerance exits declared NON-equivalent outcomes" — prevents a tolerance-artifact win on either arm. |
| 5 | No warm-start interface documented; filter flushed on mu updates; future-work list has no warm-start (§3.3) | **CONSISTENT** | Panel W3 (:116-119) prices cold restarts as the defect and the WIN RULE demands a W3 win — but no landed premise asserts Uno warm-starts (RC31T-3's warm-start clause concerns the INCUMBENT's implementation and [P-IPADJ]); the A/B measures restart economics either way. Spec note ride-along: W3 measured as total evals + restart churn, no warm-start API assumed on arm B. |
| 6 | filtersqp preset = TR restoration filter SQP over BQPD active-set QPs (§2.1, §6.1 of paper) | **CONSISTENT** | Realizes the panel's W2 mechanism ("SQP-type active-set identification beats log-barrier smearing", :108-115) in the exact arm-B configuration the ledger pins — supports the pinned arm-B choice, decides nothing. |
| 7 | Uno filtersqp gmean 18.08 vs filterSQP 18.73 and field (Table 2; §3.7) | **CONSISTENT** | Candidate-order evidence at the paper's own scope (small CUTE, eval counts); the WIN RULE's measured half stays F2 by construction — no number here can move it. |
| 8 | Hessian silent-degrade-to-zero path (§3.5) | **ENRICHMENT** | A/B validity pin: "arm-B runs must assert the wired Hessian path and REJECT any run whose log shows the §5.3.5 degrade warning" — protects F-C31-2's metrics from a false-arm-B artifact. |
| 9 | Multiplier provenance: FJ pi* explicit; no least-square refinement in 2.2.0; delta_c dual regularization perturbs the system (§3.2) | **ENRICHMENT** | [P-IPADJ]/A/B duty note: "arm-B multipliers consumed INFORMATION-ONLY (same discipline as incumbent) until the A/B's W2 crispness measurement lands; record inertia-correction (delta_w, delta_c) activity per accepted iterate as multiplier-quality covariates." |
| 10 | Funnel semantics ABSENT from the paper; funnel options exist only at v2.8.0 (§2.3, §4.2) | **ENRICHMENT** | Arm-B rider completion: "IF the funnel variant is ever armed, it requires its own source adjudication (Uno code at the installed version + funnel literature) BEFORE its numbers are verdict-bearing; composition = preset filtersqp + globalization_strategy=funnel_method + funnel_* defaults pinned + version stamp." |
| 11 | Version skew paper 2.2.0 vs clone v2.8.0 (§5 DELTA-3..5) | **ENRICHMENT** | A/B spec pin: "installed-version stamp + re-verification of presets/options at that version is a precondition of the A/B run" (extends the O5 install decision with a verification duty; W5 asymmetry itself unchanged). |
| 12 | Benchmark scope small-CUTE/eval-counts (§3.7, §4.5) | **CONSISTENT** | Aligns with panel W4 materiality (n~10 dense; eval counts discriminate); simultaneously BOUNDS the paper's evidence to candidate-order weight — exactly the tier the verdict already assigned ([ABS]/[TITLE]-marked census claims, :513-516). |
| 13 | ipopt-preset fidelity gap, 12 named instances (§3.6, §4.4) | **CONSISTENT** | No landed premise equates Uno-ipopt with IPOPT; guards against a FUTURE inflation (citing preset numbers as IPOPT numbers) — claim-bound noted, nothing moves. |
| 14 | IP+TR prohibited in Uno 2.2.0 (§2.1) | **CONSISTENT** | The incumbent's TR-IP shape is NOT reproducible inside Uno 2.2.0 — irrelevant to the pinned A/B (arm B = TR-SQP filtersqp), relevant only against an unpinned "mimic the incumbent inside Uno" idea nobody registered. |
| 15 | No convergence theory for composed variants (§4.1) | **CONSISTENT** | The verdict never leaned on composed-variant theory; reinforces that any variant beyond the presets (incl. funnel) carries its own guarantee burden (item 10). |

**Counts**: confront_items = 15; CONSISTENT = 9; TENSION = 0; ENRICHMENT = 6.

**Closing question** — does the full read CHANGE the answer to the frozen
question "which engine closes the certificate at the boundary-active
optimum"?

**ANSWER CLASS: NO-CHANGE-experiment-still-decides.** The read found no
finding that fires a named falsifier or contradicts a landed premise: the
engine of record remains scipy trust-constr AS-IS under INFORMATION-ONLY
multiplier discipline until [P-IPADJ]; the flip candidate remains Uno
(filtersqp preset, funnel = declared options-selected variant — now
source-proven); F-C31-1/2/3 remain exactly decidable, and the six
enrichments above sharpen the A/B's guard alphabet, tolerance matching,
Hessian-path validity, multiplier discipline, funnel rider, and version
hygiene WITHOUT touching any frozen criterion. No criterion of the panel is
shown ill-posed by the paper (the W3 warm-start channel narrows to measured
restart economics, which the frozen text already prices).

---

## MACHINE SUMMARY

```yaml
pages_read: 44/44            # published PDF, all rendered pymupdf dpi=120, all read; none failed
render_failures: 0
preprint_cross_check: heading-structure diff + targeted greps (funnel, presets, version)
delta_items: 5               # DELTA-1/2 published-vs-preprint (layout-only; no substantive delta found);
                             # DELTA-3/4/5 paper-vs-local-clone v2.8.0 (auto preset; LBFGS/LSR1; funnel options)
arm_b_inputs_count: 10       # section 3 items: termination alphabet, multipliers, no-warm-start pin,
                             # constraint-set mapping, Hessian provisioning pin, preset-fidelity bound,
                             # benchmark-scope transfer bound, infeasibility certificate, robustness logs,
                             # version-stamp duty
claims_above_content_risks: 8  # section 4 items 1-8 (top: funnel-label-only; composed-variant convergence;
                               # quasi-Newton absent in 2.2.0; preset!=original solver; termination!=certified optimum)
confront_items: 15
confront_consistent: 9
confront_tensions: 0
confront_enrichments: 6
answer_class: NO-CHANGE-experiment-still-decides
discipline: informs-only; C31 verdict untouched; no ledger/registry edits; only this file written
```
