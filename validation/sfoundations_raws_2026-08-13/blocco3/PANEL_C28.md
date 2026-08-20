# PANEL_C28 — CERT-FRONTIER REPRESENTATION (Blocco 3, wave 1, solo panel)
S-FOUNDATIONS-C2, 2026-08-19. Cluster: C28 (docs/choice_ledger.yaml:419-427).
Brief: validation/sfoundations_raws_2026-08-13/blocco3/BRIEF_wave1_panels.md §0 + §C28.
Method: formalize-first → SOTA census → tree advocacy (cite-not-regenerate) →
per-row adjudication → dedup (navigation-first). No file outside blocco3/ edited.

---

## 1. FROZEN FORMAL STATEMENT

**Objects.** Design vector W ∈ R^n (spline wall dofs, class C_m(ξ)); objective
J(W) (cycle-averaged thrust-class functional) computed by a CERTIFIED marched
axisymmetric Euler solve (RK-G segmented march, fitted fronts, per-cell Newton
unit processes); equality constraints g(W)=0 (ε, L); JAX/adjoint stack (traced,
AD-differentiable replay fields); scipy trust-constr driver (TR-SQP class;
IP path unadjudicated — findings row `driver-nonsmooth:ip-path-unadjudicated`,
docs/findings_registry.yaml:1236-1244). Verdict discipline: derived constants
only, rejectors must be able to fire, binary record gates are the truth.

**The two admissibility families (the decomposition the S22 measurement forces
— they are DISTINCT objects of record, M0 S22 block (v), docs/rde_nozzle_MASTER.md:2318-2327):**

- **(i) PHYSICAL margins** m_phys(W) ≥ μ₀: fold margin (Sternin/Eq.(4)
  boundary via the (G)/Λ-form val field), causality margin u_x − c, g_sep.
  Quantifiable, AD-differentiable, with THEOREM-level KS machinery already of
  record ([X-MGOV], M0:2336-2353; KS-min bounds + derived ρ = K_RICH ln(N)/μ₀).
- **(ii) NUMERICAL certification frontier**: the certifiable set
  K = {W : the adaptive record passes every gate} — per-cell while-Newton
  certification ratio r_i(W) = ||one extra Newton step||/(NEWTON_TOL_FACTOR·ε·scale) ≤ 1,
  axial-margin gate, trip cap N_NEWTON (K = K_phys ∩ K_budget; M0:1990-2011).
  Solver-defined, piecewise-smooth per RK-G stratum (plan P frozen), MEASURED
  BINDING at three campaign instances (S20/S22/S24, F4-branch class) at HEALTHY
  physical margins (val 0.61-0.86 vs fold threshold 0.172; M0:2294-2327).
  The registered quantifier bridge K_disc ~ A₀ is FALSIFIED by its named
  falsifier (S22 (v)): bd(K) is a NUMERICAL-CLASS boundary, bd(A₀) a physical
  one; the margin governor "CANNOT capture the S20-instance certifiability
  frontier" (S22 (vi), M0:2328-2335). Pipeline-sense R1 of record: "no
  successor quantifier exists" (ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md §3.1).

**Frozen question (per-row, C28).** How is frontier (ii) — and its composition
with (i) — REPRESENTED in the production optimization loop
max J s.t. g=0, W ∈ C_m ∩ K:

- **(a) Binary outside gates only** (INCUMBENT of the ledger row): P4 gate at
  segment base + P3(ii) at accepted iterates (validation/a1_toc_variational_jax.py:935-938,
  :1158-1161), reject-and-ratchet-shrink, outcome-II declaration on exhaustion
  at TR_FLOOR.
- **(b) Priced constraint inside KKT** (the ledger's listed alternative):
  a surrogate of max_i r_i enters the constraint set — candidate surrogate
  forms: KS-max / graded-violation aggregate / exact penalty — with multiplier
  μ_c = marginal price of certifiability; gates kept.
- **(c) A-priori solvability regions** (O-F20): provable inner approximation
  of the certifiable set derived per sector; optimize inside; the hidden
  constraint vanishes there.
- **(d) Hybrid gate+price tier ladder** (M0's S20 formalization of record,
  M0:2111-2185): ladder (P_t) over certified classes A_t(μ₀); first-order
  optimality at boundary-active optima = KKT WITH THE MARGIN MULTIPLIER
  ∇J = λ∇g + μ∇m, μ ≥ 0 (M0:2126-2132, THEOREM-level structure); gates stay
  verifiers of record; the measured μ prices tier opening.

**Quantity bounded/optimized.** Certified J, with the verdict requirement that
a returned base carries either KKT closure or an honest stationarity
certificate; today the outcome-II "KKT OPEN" number is the residual of the
problem WITHOUT the certification constraint — it measures nothing about
optimality at a frontier-pinned point (GAP-2, ADVISORY_S24_sota_gapmap_2026-08-12.md:107-139;
findings row `driver-nonsmooth:no-B-stationarity-certificate`,
docs/findings_registry.yaml:1136-1144).

**Hypotheses.** Pure-periodic interface data (standing scope pin); frozen
thermally-perfect mixture; RK-G determinism; stratum-local smoothness of r_i
(replay objects on the frozen plan); O1 obligation OPEN (Danskin/Clarke cusp
derivative — until discharged, margin-active KKT statements carry the
B-stationarity qualifier and no μ is defined; M0:2256-2259).

---

## 2. SOTA CENSUS

**Query trail (7 WebSearch queries, derived from §1, run 2026-08-19):**
1. "Kreisselmeier-Steinhauser constraint aggregation adaptive Poon Martins
   Kennedy Hicken conservativeness review aerodynamic optimization"
2. "hidden constraints unrelaxable simulation-based optimization taxonomy
   Le Digabel Wild progressive barrier"
3. "MPCC mathematical program complementarity constraints B-stationarity
   Scholtes regularization relaxation schemes survey recent"
4. "manifold sampling nonsmooth composite optimization Larson Menickelly Wild
   gradient sampling Clarke stationarity certificate"
5. "optimization design loop constraint on solver convergence failure crash
   constraint / solver failure, gradient-based, penalize non-convergence,
   differentiable"
6. "exact penalty function SQP filter methods Fletcher Leyffer elastic mode
   SNOPT infeasibility handling nonlinear programming production solvers"
   (+ paired query on implicit differentiation through Newton solvers, JAX)
7. "semi-infinite programming adaptive discretization exchange method review
   Djelassi Mitsos Stein vanishing constraints MPVC optimization"

**Corpus recency (explicit span + newest).** 1979-2026. Newest items reached:
arXiv:2605.29757 (2026, disjunctive MPCC regularizations), arXiv:2607.24959
(2026, implicit contact differentiation), Comput. Phys. Commun. article
S0010465526000846 (2026, implicit diff with second-order derivatives in
differentiable physics), arXiv:2601.16510 (2026, learning-to-optimize by
differentiable programming). 2025 layer: arXiv:2501.07383 (Scholtes-regularization
stability), COAP 10.1007/s10589-025-00710-y (bounding-focused SIP
discretization), RSC Digital Discovery 10.1039/D5DD00018A ("Anubis" BO with
unknown feasibility constraints), arXiv:2504.08721 (surrogate optimization
under hidden constraints), arXiv:2512.05392 (OpenSQP), arXiv:2512.01565
(Deep FlexQP), arXiv:2511.18998 (TR funnel for gray-box). 2023-2024:
Optim. Eng. 10.1007/s11081-023-09839-3 (taxonomy, journal version), Math.
Prog. Comp. 10.1007/s12532-023-00245-5 (structure-aware nonsmooth composite
DFO), CEAS Space J. 10.1007/s12567-023-00511-1 (MoC-based nozzle shape
optimization). Every census axis reaches ≥ 2023; the modern-refined-literature
requirement is met, not merely the classics.

**Per-source one-liners, by census axis.**

*Axis 1 — surrogate exactness/conservativeness (aggregation family):*
- Kreisselmeier–Steinhauser 1979 (via the S24 record + census hits): the
  standard conservative aggregate; conservative side correct; ρ trades
  conservatism vs domination/oscillation.
- Poon–Martins (SMO 2007; adaptive-KS): ρ updated from constraint
  sensitivities; accuracy gain without added cost when many constraints are
  active — the accuracy axis, already the C27 alternative set (INTERPLAY named
  in §4, not decided here).
- Kennedy–Hicken (induced exponential/power aggregation): tighter induced
  aggregates, same lineage.
- Parallel adaptive kriging with constraint aggregation (AIAA J.,
  10.2514/1.j059915) + wing surrogate aggregation (SMO 10.1007/s00158-018-2074-4):
  aggregation as production practice at large N — cost axis support.

*Axis 2 — the constraint CLASS and graded violation (hidden/unrelaxable):*
- Le Digabel–Wild taxonomy (arXiv:1505.07881; journal Optim. Eng. 2024,
  10.1007/s11081-023-09839-3): certification-type constraints =
  Nonquantifiable-Unrelaxable-Simulation(-Hidden), "the worst kind"; the
  recognized remedy WHEN the physics exposes one is to QUANTIFY a margin.
  This is the anchor M0 already registered (M0:2164-2177) — census confirms
  it is still the canonical frame, now in journal form.
- Audet–Dennis progressive barrier (via taxonomy corpus): graded violation
  aggregate h(S) treated with values, not booleans — the derivative-free
  realization of "price the frontier"; extreme barrier = the unrelaxable
  fallback, native to MADS, not to smooth TR-SQP stacks.
- Hidden-constraint surrogate classification (Basudhar et al. 2012 lineage;
  arXiv:2504.08721, 2025; "Anubis" 10.1039/D5DD00018A, 2025): classifier
  proposes, never disposes — explorer-tier only; modern BO line confirms the
  epistemic fence the trees drew independently.

*Axis 3 — nonsmooth/MPCC treatment and stationarity semantics:*
- Scheel–Scholtes 2000 (B/C/M-stationarity), Scholtes 2001 global relaxation
  (SIOPT 10.1137/070705490 lineage): the stationarity taxonomy for
  complementarity-structured frontiers; convergence to C-/M-/B-stationary
  points under MPCC-LICQ + conditions.
- arXiv:2501.07383 (2025): stability of Scholtes regularization —
  nondegenerate C-stationary ↔ KKT of the regularization, topological type
  preserved; the lineage is alive and refining.
- arXiv:2605.29757 (2026): disjunctive regularizations outperform
  Kanzow–Schwartz and Scholtes at high accuracy — the modern refinement edge.
- Vietnam J. Math. 10.1007/s10013-024-00704-z (2024): MPCC machinery applied
  to nonsmooth optimal control — transfer precedent to control-shaped problems.
- Burke–Lewis–Overton gradient sampling; Larson–Menickelly–Wild manifold
  sampling (SIOPT 2018; OSTI 1839939 compositions; MPC
  10.1007/s12532-023-00245-5, 2023): Clarke-stationarity certificates for
  piecewise-smooth objectives/constraints — the certificate technology behind
  [P-BSTAT]'s convex-hull test (0 ∈ conv{stratum gradients} + normals).
- Conn–Gould–Toint, Trust-Region Methods §11 (via S24 record): Clarke tests in
  nonsmooth TR frameworks.

*Axis 4 — production-loop cost and infeasibility mechanics:*
- SNOPT (SIAM Rev. 10.1137/S0036144504446096) elastic mode; Fletcher–Leyffer
  filter SQP (Math. Prog. 2002): production infeasibility handling = relax and
  price (ℓ1 elastic) or filter — NOT verdict-bearing certificate pricing; the
  distinction matters and is kept in §3.
- OpenSQP arXiv:2512.05392, Deep FlexQP arXiv:2512.01565, TR funnel
  arXiv:2511.18998 (all 2025): the modern open SQP/funnel generation — none
  prices a solver-certification field; they price constraint violation.
- JAXopt implicit differentiation (arXiv:2105.15183 + docs); CPC
  S0010465526000846 (2026): differentiating THROUGH Newton solves via IFT on
  the residual — the technology that makes r_i(W) a traced, differentiable
  replay field (the repo already has this; census confirms the stack choice is
  the modern mainline, not an in-house eccentricity).
- CEAS Space J. 10.1007/s12567-023-00511-1 (2023): modern MoC-in-loop nozzle
  shape optimization — MoC feasibility handled by construction/filtering; no
  pricing of certifiability found in this line.

*Axis 5 — semi-infinite treatment (named for completeness; the C28 family is
finite per stratum):* Djelassi–Mitsos–Stein 2021 review (EURO J. Comp. Opt.);
adaptive discretization arXiv:1910.13798; bounding-focused SIP COAP 2025
(10.1007/s10589-025-00710-y); inexact separation oracles arXiv:2307.14181.
The per-cell ratio family is finite-but-large per stratum (N = 3498-scale
lanes measured for the governor scope, M0:2341-2343), so SIP machinery is not
required for C28; it IS the C27 axis (exchange methods) — dependency named in
§4, not decided here.

**Census-bounded absence (zero inflation, query-bounded).** No source in this
census — across all 7 queries — was found that prices a MARCHED solver's
per-cell Newton-certification ratio as an in-KKT constraint in a production
design loop. The composition (traced certification field + KS-max pricing +
binary gates kept as absolute verifiers) is, as far as this census reaches,
the program's own; it composes standard, census-supported parts. This is an
absence claim bounded by the 7 queries above, not a novelty theorem.

**RATIFIED litreview cava, cited per-row as mandated.** Greps run on
validation/ADVISORY_litreview_confrontation_2026-08-13.md: `C28` → 3 hits
(lines 36, 854, 1231); `GAP-1` → 0 hits; `certifiab` → 0 hits. All three
`C28` hits are the cava's OWN correction-item numbering — a numbering
collision with the choice ledger: cava-C28 = the Harroun Fig. 7 epistemic
downgrade ("misurato" → "CFD-vs-CFD con corroborazione sperimentale parziale",
line 36), the base-drag measurement-protocol adjudication (§5/A31, §6/C28,
line 854), and dispatch row D-41 (line 1231). None bears on cert-frontier
representation. VERDICT: the ratified cava contributes NO row to this cluster
(search-proven; greps stated above).

**Dedup greps (navigation-first, §0.5).**
- docs/choice_ledger.yaml: `certifiab|P4-gate|frontier` → only C28:420;
  `TR-SQP|MPCC|nonsmooth` → 0 rows. The brief's seeded question
  "TR-SQP-with-P4-gate vs nonsmooth/MPCC handling of the certifiability
  frontier" (S24) is NOT a ledger row under that phrase; it lives of record as
  the S24 facet analysis validation/sota_gapmap_raws_2026-08-12/s24_gap_driver-nonsmooth.md
  (drop-item 2, :492-494: MPCC reformulation FOLDED into G1 as alternative
  lineage + G3 engine choice), gapmap GAP-1/GAP-2
  (ADVISORY_S24_sota_gapmap_2026-08-12.md:65-139), findings rows
  `driver-nonsmooth:*` (docs/findings_registry.yaml:1136-1271), and the S24
  seeded open-rows list (validation/sordine_raws_2026-08-13/inventory_seg6_memory.md:157,
  "MPCC" named). §3.4 below is that seeded question's adjudication half —
  cited, not re-minted.
- docs/findings_registry.yaml: `P-CERTKS|P-BSTAT|KSmax|KS-max` → [P-BSTAT] at
  :1143 (owner F2, GAP-1 window). [P-CERTKS] exists in validation/ (gapmap +
  raws + S25bis prompt), NOT yet as a docs/ registry row — carried as part of
  the duty in §4, not re-minted (the gapmap registration is the record).
- docs/literature_registry.yaml: `Kreisselmeier|Poon|Scholtes|MPCC|Audet|bundle|manifold sampling|Burke`
  → 0 rows. The aggregation/MPCC/nonsmooth-certificate lineage has NO
  literature-registry rows yet; any F2 adoption must mint them (folded into
  the §4 duty; none minted here).
- docs/claims_registry.yaml: `certifiab|KKT|frontier` → the [X-TBAK] KKT-active
  backoff claim (:1365) and the EQ-v2 margin-active-KKT claim (:1391-1397)
  presuppose the constrained-KKT frame — consistent, no collision.
- "census row 10 (C1 field-level rejector, owner F2)" — the C28 ledger owner
  pointer — is a REJECTOR, not an in-KKT surrogate (GAP-1's own gloss,
  ADVISORY_S24_sota_gapmap_2026-08-12.md:77-78); no dedup conflict with the
  proposed representation.

Sources: [Poon–Martins adaptive KS](https://link.springer.com/article/10.1007/s00158-006-0061-7) · [taxonomy arXiv](https://arxiv.org/pdf/1505.07881) · [taxonomy journal](https://link.springer.com/article/10.1007/s11081-023-09839-3) · [Anubis 2025](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00018a) · [hidden-constraints 2025](https://arxiv.org/html/2504.08721v1) · [Scholtes stability 2025](https://arxiv.org/abs/2501.07383) · [disjunctive MPCC 2026](https://arxiv.org/html/2605.29757) · [Scholtes-scheme SIOPT](https://epubs.siam.org/doi/10.1137/070705490) · [MPCC optimal control 2024](https://link.springer.com/article/10.1007/s10013-024-00704-z) · [manifold sampling SIOPT](https://epubs.siam.org/doi/10.1137/15M1042097) · [manifold sampling compositions](https://arxiv.org/pdf/2011.01283) · [structure-aware nonsmooth DFO 2023](https://link.springer.com/article/10.1007/s12532-023-00245-5) · [SNOPT SIAM Rev.](https://epubs.siam.org/doi/10.1137/S0036144504446096) · [NLP solvers survey](https://wiki.mcs.anl.gov/leyffer/images/7/75/NLP-Solvers.pdf) · [OpenSQP 2025](https://arxiv.org/pdf/2512.05392) · [Deep FlexQP 2025](https://arxiv.org/html/2512.01565) · [TR funnel 2025](https://arxiv.org/pdf/2511.18998) · [implicit diff](https://arxiv.org/pdf/2105.15183) · [JAXopt implicit diff](https://jaxopt.github.io/stable/implicit_diff.html) · [FE implicit diff 2026](https://www.sciencedirect.com/science/article/abs/pii/S0010465526000846) · [MoC nozzle optimization 2023](https://link.springer.com/article/10.1007/s12567-023-00511-1) · [SIP bounding 2025](https://link.springer.com/article/10.1007/s10589-025-00710-y) · [SIP adaptive discretization](https://arxiv.org/pdf/1910.13798) · [SIP inexact oracles](https://arxiv.org/pdf/2307.14181) · [aggregation kriging](https://doi.org/10.2514/1.j059915) · [wing aggregation](https://link.springer.com/article/10.1007/s00158-018-2074-4)

---

## 3. ADJUDICATION (row C28)

Diff anchor of record: BASE/phaseB_tree_diff.md:143-155 (CONVERGENT-WITH-M0 /
DIVERGENT-WITH-LEDGER, HIGHEST SIGNAL, 4/4) + §3.7 :347-350 ("the strongest
single methodological validation in the diff"). Per §0.4 the 4/4 convergence
puts the burden of proof on the incumbent; it is treated as evidence, and the
adjudication below is on content.

### 3.1 Incumbent (a) — binary outside gates only: the genuine case, then the record

GENUINE CASE (not strawmanned): (1) record-mode certification is the truth and
is non-negotiable; a binary gate cannot be fooled by surrogate conservatism
gaps or stratum drift; (2) after the K_disc~A₀ falsification (S22 (v),
M0:2318-2327) the honest state was "no proven quantifier for frontier (ii)" —
pricing the WRONG field (val) would have been inflation, and the incumbent's
refusal to price anything was epistemically correct AT THE TIME; (3) zero added
machinery; at mild instances (S18) the frontier is never met and the incumbent
costs nothing; (4) S22 (vi) stands: no claim that margin-constrained
re-optimization dissolves the S20-class obstruction survives — a priced
constraint is NOT being adopted on a dissolution claim.

THE MEASURED RECORD AGAINST IT AS SOLE REPRESENTATION: three outcome-II
records (S20/S22/S24, F4-branch class) where the KKT system is STRUCTURALLY
incapable of closing at frontier-pinned points (GAP-1,
ADVISORY_S24_sota_gapmap_2026-08-12.md:66-81); the reported "KKT OPEN" number
(S24: 1.417e6) is the residual of the problem WITHOUT the certification
constraint (GAP-2, :109-115); Probe B Arm 1 (committed, analytic toy,
:93-96): the binary-gate architecture exits at the radius floor reporting
optimality 1.0 at distance 7.1e-2 from the true constrained optimum whose true
KKT residual is 0. Deep-DEF S24: 19-21 segments fencing the frontier with
trial cert_worst 1e1..1e7 visible to no model (:89-90) — record-scale cost per
productive step. P-F33's blind verdict names the mechanism: a formulation that
cannot take gradients of its own certifiability "will grind or lie"
(phaseA_tree_propulsion.md:1206-1209); ours grinds (honestly — outcome-II is
"never a silent success", GAP-2 fairness note :117-120).

STATED-REASON OUTCOME: SUPERSEDED AS SOLE REPRESENTATION; RETAINED as the
absolute verifier layer (P4/P3(ii) stay adjudicators in every formulation —
s24_gap_driver-nonsmooth.md:21, and every tree keeps the gate as backstop:
V-F32 "O1 as the backstop", H-F24 "(a) as backstop", P-F33 "O1 as the outer
guard").

### 3.2 Alternative (b) — priced constraint inside KKT (ledger's listed alternative)

TREE ADVOCACY (cite-not-regenerate):
- V-F32 (phaseA_tree_variational.md:1373-1411): O2 margin-constraint
  internalization as doctrine — "the boundary becomes ordinary constraints
  with multipliers; the certificate then *prices* certification (marginal
  thrust cost of staying certifiable — decision-grade information)"; the fork
  that turns certified class "from a filter into a *priced constraint
  surface*" — "arguably the most distinctive structural choice of the whole
  formulation" (:1400-1406). Its falsifier: a margin whose zero level fails to
  coincide with actual certification failure is demoted to O1 filtering
  (:1407-1411) — adopted below as pin F-1.
- H-F24 (phaseA_tree_hyperbolic.md:774-795): (b) primary, (a) backstop; the
  certified-class boundary joins the ACTIVE SET; "its multiplier prices 'how
  much J is being held back by certifiability'" (:788-791); penalization
  REJECTED — "a certificate is not tradeable" (:782-783); falsifier = LICQ
  failure at the boundary forces the (a)/(d) fallback (:792-795).
- O-F20, C28-relevant half only (phaseA_tree_optimization.md:1095-1127; its
  per-sector solvability program is wave-2/C20 advocacy per the brief):
  option 2 progressive barrier / graded violation — "we HAVE one (residual
  stagnation level, monitor margins) ⇒ build h(S) = certification-violation
  aggregate; treat as a constraint with values, not a boolean" (:1099-1103);
  option 1 extreme barrier kills smooth TR methods (:1096-1098); option 3
  classification surrogate "never a certificate" (:1104-1107).
- P-F33 (phaseA_tree_propulsion.md:1192-1212): O2 primary — certifiability
  margins "become explicit constraints with their own gradients; the boundary
  becomes navigable instead of a wall" (:1198-1201); grounds: "optima live ON
  boundaries" (:1207-1208).

RECORD SUPPORT: this is the M0 S20 formalization the ledger lags (the crux the
brief names): KKT-with-margin-multiplier at boundary-active optima, THEOREM
(standard) for the nesting/constrained-KKT structure (M0:2126-2132, 2155-2157);
the taxonomy remedy "quantify a margin" (M0:2164-2177). For frontier (ii)
specifically, the successor spec ALREADY EXISTS of record: GAP-1
(ADVISORY_S24_sota_gapmap_2026-08-12.md:82-105; long form
s24_gap_driver-nonsmooth.md:63-98) — KS-max over the TRACED per-cell
certification ratios, KSmax_ρ(r) ≤ 1 − ln(N)/ρ with THEOREM-level bounds and
proven sufficiency for per-cell certification, ρ DERIVED (K_RICH ln(N)/s_min,
governor discipline, no tuned constant), stratum-local by construction,
wired via the existing margin_factory slot (a1_toc_variational_jax.py:1179-1182),
gates absolute. Probe B Arm 2 (committed): KKT closes to 4.6e-11 with
μ_c = 0.709 > 0, lands 2.9e-3 from the true optimum inside the KS conservatism
offset, and the binary gate never fires on any accepted iterate. Everyday
cost: at mild S18 the surrogate is strictly inactive, μ_c = 0, walk
bit-comparable — zero cost far from the frontier (GAP-1 exposure :89-92).

CENSUS SUPPORT: axis 1 (KS lineage standard, conservativeness controlled,
adaptive refinements exist); axis 2 (the taxonomy's canonical remedy IS
quantification; graded violation = Audet–Dennis progressive-barrier doctrine
in its gradient-based form); axis 4 (the traced-ratio differentiability rests
on the same IFT-through-Newton technology the modern differentiable-physics
mainline uses). Census-bounded absence stated in §2: the specific composition
is unprecedented as far as this census reaches — so its repo-scale behavior is
a MEASUREMENT question, not a literature question. That is exactly what gates
this verdict (§4).

WHY THE CRITICAL DIFFERENCE FROM THE FALSIFIED BRIDGE HOLDS: the falsified
object was a SET-LEVEL PHYSICAL claim (K_disc approximates A₀ — val proxies
certification). The KS-max surrogate makes NO physical claim: it aggregates
the very ratios r_i the gate itself checks — surrogate and gate see the SAME
field, and the conservative-side inequality max r_i ≤ KSmax is a THEOREM at
fixed stratum, not a bridge conjecture. The S22 standing rule ("any future
bridge claim must carry a per-instance monitor test", M0:2325-2327) is honored
by pin F-1 (§4): surrogate-vs-gate agreement is monitored per instance, and a
disagreement fires a rejector instead of silently lying.

HONEST RISKS (each carried into §4): (1) stratum seams — r_i is
piecewise-smooth per plan; plan flips give the frontier MPCC/nonsmooth
structure at seams, where the honest optimality language is B-stationarity
(Scheel–Scholtes; census axis 3) and the honest instrument is [P-BSTAT]'s
convex-hull test (GAP-2 :124-127); μ_c stays under the B-stationarity
qualifier until O1 is discharged (M0:2256-2259). (2) Conservatism: KS-max
over-approximates — it can refuse designs the gate would pass (never the
reverse); the derived-ρ discipline bounds the gap at ln(N)/ρ = s_min/K_RICH.
(3) Conditioning at large ρ (shifted form mandatory, gradient mass
concentrates on the argmax lane — s24_gap_driver-nonsmooth.md:106-109); the
governor's derived-ρ discipline transfers. (4) Engine: any inequality
constraint makes scipy's tr_interior_point path PERMANENT — [P-IPADJ]
re-adjudication moves onto the same critical path (findings
:1236-1244; ledger C31, not decided here).

STATED-REASON OUTCOME: ADOPTED as the in-KKT half of the representation,
measurement-gated (§4). Surrogate form adjudicated WITHIN (b): KS-max — over
graded-violation-without-multipliers (loses the multiplier semantics the (ii)
theory requires; census axis 2 keeps it as the DFO realization) and over
exact-penalty/elastic forms (production infeasibility tools — SNOPT elastic,
filter — that RELAX violated constraints; a certificate is not tradeable,
H-F24 :782-783; multiplier meaning polluted, V-F32 O3 :1391-1392).

### 3.3 Alternative (c) — a-priori solvability regions (O-F20's 5-first doctrine)

GENUINE CASE: a PROVABLE inner approximation of the certifiable set (classical
characteristics argument: monotone expansion, PM margin, coalescence bound —
phaseA_tree_optimization.md:1111-1118) makes the hidden constraint VANISH
inside; cleanest certificates; the classical corpus (Sternin boundary,
Eq. (4)) supports exactly this on the physical side, and the (G)/Λ-form val
monitor is its implemented descendant ([X-VMON], M0:2222-2238).

AGAINST AS THE C28 ANSWER (stated reason, from the record): the S22 O4
measurement (branch (c) unanimous 5/5, M0:2285-2327) shows the BINDING
frontier of record is a NUMERICAL-CLASS boundary — damped-Newton stalls at
HEALTHY-margin cells (val 0.61-0.86 vs threshold 0.172), near-axis, columns
23-30 — which no physically-derived solvability region can see: the bridge
falsification IS the proof that physical-region reasoning does not capture K
on this instance. O-F20's own falsifier concedes the escalation: "inner-region
optimum presses the provable boundary with positive multiplier ⇒ ... the
graded-barrier campaign (2) across the true boundary is REQUIRED"
(:1129-1133) — and the measured record (three campaigns pinned ON the true
frontier) is already past that trigger. Census: no modern production line
found doing a-priori certified-region optimization for marching solvers (the
CEAS 2023 MoC line filters, it does not price).

STATED-REASON OUTCOME: RE-SCOPED, not adopted for frontier (ii): solvability
regions remain live for the PHYSICAL family (i) and for the tier-opening
criteria of the M0 ladder, where they are the classical road; the per-sector
derivation program is O-F20's other half = wave-2 advocacy (per brief §C28,
cited only in its C28-relevant half here). No wave-2 row is decided here.

### 3.4 Alternative (d) — hybrid gate+price tier ladder (M0), and the seeded MPCC question

CONTENT: (d) is not a rival of (b) — it is (b) COMPOSED WITH the gates and the
ladder. Every tree's recommendation is itself a hybrid (V-F32: O2 doctrine +
O1 backstop + O4 discovery tier; H-F24: (b)+(a); O-F20: regions + graded
violation + TR backtracking; P-F33: O2 + O3 fidelity escalation + O1 outer
guard). M0's formalization of record IS this hybrid (ladder + margins +
KKT-with-multiplier + gates as verifiers). The Phase-B diff already read the
4/4 as CONVERGENT-WITH-M0 (BASE/phaseB_tree_diff.md:143-155). The adjudicated
representation is therefore (d) with (b) as its in-KKT instantiation for
frontier (ii) — per family: PHYSICAL margins priced via the existing [X-MGOV]
KS machinery (built, rejector-proven); NUMERICAL frontier priced via the
GAP-1 KS-max-on-r_i spec (to be measured); binary gates kept absolute
everywhere; discovery/explorer tiers stay outside the verdict loop.

THE SEEDED S24 QUESTION ("TR-SQP-with-P4-gate vs nonsmooth/MPCC handling of
the certifiability frontier") — adjudication half, deduped per §2: MPCC
machinery enters NOT as a reformulation of the whole loop (the S24 facet
already folded that: drop-item 2, s24_gap_driver-nonsmooth.md:492-494) but as
the STATIONARITY LANGUAGE at stratum seams: (1) within a stratum the priced
system is smooth NLP and scipy optimality IS the surrogate B-residual (GAP-2
executable form (i), :124-125); (2) at seams and at returned outcome-II bases
the honest certificate is B-stationarity via the convex-hull test on persisted
stratum gradients ([P-BSTAT], findings :1143); (3) Scholtes-type
regularization and its 2025-2026 refinements (census axis 3) are the named
fallback lineage IF the ratio field must ever stay nondifferentiable at lane
activation (GAP-1 SOTA line, s24_gap_driver-nonsmooth.md:94-98) — not adopted
now, for the stated reason that the traced r_i is differentiable per stratum
by construction. TR-SQP-with-P4-gate (the incumbent driver shape) is kept as
the OUTER mechanics; the frontier handling changes from gate-only to
gate+price. This consumes the seeded question's C28 half; its engine half
(which SQP/IP implementation) is C31/[P-IPADJ], named, not decided here.

### 3.5 Sub-alternatives closed (stated reasons; none by omission)

1. Penalty/relaxation of certification (V-F32 O3; H-F24 (c)) — CLOSED:
   pollutes multiplier semantics; a certificate is not tradeable.
2. Exact-penalty/elastic-mode forms (SNOPT lineage) as the verdict loop —
   CLOSED for verdict-bearing use (same reason as 1; census axis 4 shows they
   are infeasibility mechanics, not certificate pricing); available as inner
   QP mechanics only, under C31.
3. Extreme barrier as the loop mechanic (O-F20 opt 1) — CLOSED: kills smooth
   TR methods (gradient undefined at the wall); native to MADS, not to this
   gradient/adjoint stack; it is the incumbent's mechanism seen from
   DFO-land and it measurably grinds (§3.1).
4. Classification surrogate of K (O-F20 opt 3; P-F33 O4; census: Basudhar
   2012, Anubis 2025, arXiv:2504.08721) — CLOSED as verdict-bearing
   representation: proposes-never-disposes; admissible later as explorer-tier
   economics, outside this row.
5. MPCC/complementarity reformulation as PRIMARY form — CLOSED as primary
   (r_i differentiable per stratum; already folded by the S24 facet);
   RETAINED as stationarity language at seams + fallback lineage (§3.4).
6. Proximal-bundle replacement engine (D6:738, never built; Kiwiel) — CLOSED
   as primary for this row: the additive constraintification spec exists and
   preserves the adjudicated TR-SQP shape; bundle remains the named fallback
   if pin F-2 fires (engine escalation).
7. Solvability regions as the frontier-(ii) representation — CLOSED-RESCOPED
   (§3.3): cannot see the measured numerical-class boundary.
8. Binary-only incumbent as SOLE representation — SUPERSEDED (§3.1);
   retained as the absolute verifier layer in (d).

---

## 4. PROPOSED VERDICTS + DUTIES (row C28)

**PROPOSED LEDGER OUTCOME (C28).** CONVERGED-panel WITH measurement-gated
SPLIT (per §0.4):

- **Direction + adopted choice (formal half, converged now):** representation
  = HYBRID PRICED-FRONTIER (option (d)) — the M0 tier-ladder /
  KKT-with-margin-multiplier formalization of record (M0:2111-2185) — with the
  ledger's listed alternative (b) instantiated for the NUMERICAL certification
  frontier by the GAP-1 spec: KS-max surrogate on the traced per-cell
  certification ratios r_i(W), enforced as KSmax_ρ(r) ≤ 1 − ln(N)/ρ with
  DERIVED ρ = K_RICH ln(N)/s_min, stratum-local, wired through the existing
  margin_factory slot; P4/P3(ii) binary gates KEPT as absolute adjudicators
  (surrogate steers, gates verify — the [X-MGOV] precedent, GAP-1 rigor note);
  physical margins stay priced by the existing governor; solvability regions
  re-scoped to the physical family (wave-2). The incumbent "binary outside
  gates ONLY" is SUPERSEDED as sole representation. The ledger row should also
  stop reading "no successor": GAP-1 is the named successor spec of record —
  the row lagged M0 and the S24 gapmap, as the brief's crux anticipated.
- **Measured half (BINDING F2 duty, the gate on adoption-of-record):** the
  repo-scale behavior of the priced frontier — effectivity, closure, cost —
  is unmeasured (Probe B is an analytic toy, committed; census gives no
  precedent to lean on). Until the duty below reports, the choice is
  ADOPTED-FOR-MEASUREMENT, not adopted-of-record; nothing blocks F2 (this
  wave's mandate: an F2-consumed choice left NEVER blocks F2 — C28 leaves
  this panel NOT-NEVER).

**F2 DUTY (named precisely, riding registered instruments — nothing re-minted):**
**[P-CERTKS] + [P-BSTAT], the GAP-1/GAP-2 window, with [P-IPADJ] on the same
critical path** (registrations: ADVISORY_S24_sota_gapmap_2026-08-12.md:96-98,
:133-135; findings docs/findings_registry.yaml:1136-1144, :1236-1244; the S25
window these probes were first named for was consumed by the speed program —
carried, not lapsed). Content:
1. Build the KS-max ratio constraint at the small TCASE instance (ε=4, NI=21,
   Nw=60, cert_diag lanes); combined cert/val diag mode (GAP-1 implementation
   caveat); R-GRAD spot on d(KSmax)/dW vs two-step-Richardson FD band (the
   [X-MGOV] pattern, M0:2350-2353).
2. One short constrained walk vs the recorded S18 mild walk (bit-comparability
   check far from the frontier) + one frontier-class walk (S20 knot-insertion
   instance and/or S24 deep-DEF) vs the recorded outcome-II.
3. [P-BSTAT] convex-hull B-stationarity certificate assembled from the
   persisted rejected designs (s22_rejected_designs.json + S24 artifacts);
   with the surrogate active, scipy optimality doubles as the surrogate
   B-residual.

**PROTOCOL/FALSIFIER PINS (pinned NOW, thresholds derived):**
- **F-1 (surrogate-lies rejector; V-F32's falsifier recalibrated to this
  field):** any iterate ACCEPTED by the model (KSmax ≤ 1 − ln(N)/ρ) that FAILS
  record P4/P3(ii) certification ⇒ the stratum contract was violated in
  flight; the surrogate is DEMOTED to diagnostic, incumbent (a) stands, row
  re-opens. (At fixed stratum with exact ratios this is impossible by the
  THEOREM bound — a firing therefore localizes a real contract violation;
  that is what rejectors are for.)
- **F-2 (pricing-fails falsifier):** on the frontier-class walk, if the
  AUGMENTED KKT residual does not close below the existing derived gtol chain
  at the returned base AND the [P-BSTAT] certificate also refuses
  B-stationarity, then the priced representation did NOT upgrade the verdict
  (the mechanism is not a representable priced frontier); outcome: escalate to
  the engine re-adjudication ([P-IPADJ]/C31, bundle fallback named in §3.5.6)
  BEFORE any further C28 claim. What refutes what: F-2 firing refutes the
  ADOPTION, not the M0 formalization (which is THEOREM-structure + SCHEMA and
  stands on its own classes).
- **F-3 (cost falsifier):** on the mild S18 instance the surrogate must be
  strictly inactive (μ_c = 0) and the walk bit-comparable to the record; any
  drift kills the zero-cost-far-from-frontier claim and re-prices the choice
  against the S25-bis budget standard before adoption.
- **Reporting pins:** μ_c reported ONLY under the B-stationarity qualifier
  until O1 (Danskin/Clarke) is discharged (M0:2256-2259); KKT residuals
  reported normalized alongside raw (GAP-2 scale-conflation exposure, E3);
  every number in the eventual Verdict ships with its committed script + band
  (R5).

**INTERPLAY ROWS — NAMED, NOT DECIDED HERE:** C27 (aggregation family +
conditioning axis; shares the derived-ρ discipline and KS lineage — this
wave's other solo panel); C42 (K_RICH role reuse, wave 3 — the ρ derivation
reuses K_RICH; dependency named); C31/[P-IPADJ] (engine; permanent-IP
consequence of any inequality constraint); C38 (outcome-II stationarity
declaration — [P-BSTAT] is also its alternative's instrument; C38's own
adjudication stays open); C20 + O-F20's solvability-region half (wave 2);
O1 obligation (F4b theory WP). Literature-registry rows for the
KS/MPCC/nonsmooth-certificate lineage: NONE exist (grep stated in §2) —
minting them accompanies F2 adoption, not this panel.

**Inflation check (§0.2 zero-inflation, executed):** no alternative described
stronger than its literature support (each census one-liner is what the
source shows); the KS-max adoption claim is capped at ADOPTED-FOR-MEASUREMENT
with the toy-probe evidence labeled as such; the census-bounded absence claim
is query-bounded (7 queries listed); 4/4 tree convergence used as evidence
under content adjudication, not as the verdict; every number carries its
committed anchor.

---

## 5. MACHINE SUMMARY

```json
{
  "cluster": "C28",
  "rows": {
    "C28": {
      "proposed": "CONVERGED-panel: hybrid priced-frontier representation (M0 tier-ladder KKT-with-margin-multiplier, of record) with the numerical certification frontier priced via the GAP-1 KS-max surrogate on traced per-cell certification ratios (derived rho, stratum-local, margin_factory slot); P4/P3(ii) binary gates KEPT as absolute verifiers; incumbent binary-only SUPERSEDED as sole representation; solvability regions re-scoped to physical margins (wave-2); adoption-of-record gated on the measured half",
      "gated": true,
      "duty": "F2: [P-CERTKS] pilot + [P-BSTAT] B-stationarity certificate (GAP-1/GAP-2 window), [P-IPADJ] on the same critical path; falsifier pins F-1 (surrogate-lies rejector), F-2 (pricing-fails escalation to C31), F-3 (mild-instance bit-comparability cost gate)"
    }
  },
  "census_recency": "1979-2026 span; newest items 2026 (arXiv:2605.29757, 2607.24959, CPC S0010465526000846, 2601.16510) + seven 2025 items; every axis reaches >= 2023; 7 queries",
  "alternatives_closed": 8,
  "inflation_check": "done"
}
```
