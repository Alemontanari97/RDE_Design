# PANEL C27 — CONSTRAINT AGGREGATION (Blocco 3, wave 1)

S-FOUNDATIONS-C2, 2026-08-19. Solo panel per BRIEF_wave1_panels.md §0+§C27.
Row: docs/choice_ledger.yaml:407-417 (id C27, status SINGLE-AUTHOR, owner
"F2 (with GAP-1)"). Diff anchor: BASE/phaseB_tree_diff.md:133-142
(DIVERGENT HIGH, 3/4 — H-tree silent). Seed layer: certified both
directions for the current pool (SEED_PROTOCOL_v3 PASS 2026-08-19,
docs/seed_outcome_registry.md); pool unchanged, no re-seed run.
Verdicts of record cited, not re-litigated (BASE/r2pass/*).

---

## 1. FROZEN FORMAL STATEMENT

**Objects.** Design vector W (spline dofs, n ~ tens). A constraint family
`g_i(W) <= 0` (equivalently margin lanes `v_i(W) >= mu_0`) indexed by a
set I that appears in two instantiations of record:

- **(inst-L, live today)** the finite lane family of the marched solve:
  every W-dependent cell of the certified marched axisymmetric Euler
  solver with fitted fronts (val_diag replay; measured of record
  N = 3498 design-wall bucket lanes, m_ref = 6.810298e-01 —
  docs/rde_nozzle_MASTER.md:2341-2343, carrier [X-MGOV],
  docs/claims_registry.yaml:1346-1358).
- **(inst-XI, arrives with the F2 cycle problem)** the semi-infinite
  per-phase family `g_sep(W; s(xi)) <= 0` for mu-a.e. xi on the 1-D
  periodic phase set Xi (periodic-wave data scope of record); today the
  per-phase problem is quadrature-frozen, so inst-XI is the declared
  future carrier, not a live constraint.

**Operational context (binding).** Gradients exact by JAX AD/adjoint
(one reverse pass ~ one march replay; forward JVPs available, n small);
optimizer TR-SQP-class (ledger C31) entering through the
`margin_factory` slot (scipy NonlinearConstraint; the GAP-1 spec note of
record: one slot -> vector-valued constraint avoids driver surgery,
ADVISORY_S24_sota_gapmap_2026-08-12.md:101-103); certificate discipline:
derived tolerances, rejectors must fire, conservativeness must be a
theorem, enforcement floor ladder mu_0_k = m_ref/2^k, k=1..4
pre-registered (M0:2340).

**The choice being adjudicated.** The aggregation operator
`A: {v_i}_{i in I} -> m` (scalar or small-vector constraint block handed
to the KKT system), judged on four frozen axes:

- **(A1) exactness / certificate semantics** — enforcing `A >= mu_0`
  must imply the true statement `inf_I v_i >= mu_0 - (declared,
  derived resolution)`; for inst-XI additionally the between-node
  question: a certificate issued at finitely many phases must cover
  mu-a.e. xi.
- **(A2) CONDITIONING** — the never-adjudicated axis of record (ledger
  C27 note: "conditioning axis NEVER"; the frozen gap): gradient
  support and curvature of A as the enforcement floor deepens, and its
  interaction with TR-SQP model acceptance at lane-argmin ties.
- **(A3) multiplier semantics** — the multiplier(s) of A must carry the
  (ii) marginal-value meaning of the theory (mu-averaged: the
  continuous-SIP dual object is a measure on the binding index set;
  dJ/dc = -Int lambda dxi(binding measure)).
- **(A4) cost in the JAX/adjoint stack** — constraint-gradient passes
  per iterate (VJP count), scan cost over the already-computed val
  field, wall time per rung (the AC12 monitor).

**Candidate operators (the alternative set).**
(a) incumbent: KS-min over ALL of I at fixed derived
rho = K_RICH ln(N)/mu_0 ([X-MGOV]); (b) adaptive-KS (Poon-Martins);
(c) induced-exponential/power aggregates (Kennedy-Hicken), incl. plain
p-norm; (d) two-constant rule (gap AND curvature budget on the same KS);
(e) exchange/working-set on the true inner problem, aggregate only
within the working set (O-F18/V-F23 hybrid), with Lipschitz covering +
post-hoc sweep for inst-XI (P-F16); (f) MPCC argmax-tracking;
(g) probabilistic relaxations (CVaR / scenario); (h) exact-penalty NCP
of the a.e. constraint; (i) interval/Taylor enclosure over xi-cells;
(j) no aggregation at all — all-local constraints under augmented
Lagrangian (census-found modern line); (k) discretize-all-only (all
quadrature nodes as constraints, no covering).

The literature query derives from this statement: smooth aggregation of
large/semi-infinite constraint families for gradient-based (adjoint)
optimization — conservativeness bounds, curvature/conditioning of the
aggregate, adaptive parameter rules, exchange/adaptive-discretization
SIP methods and their multiplier semantics, and aggregation-free
treatments at scale.

**Interplay NAMED, not decided here (per brief):** the constant K_RICH
enters both incumbent rho and every derived threshold below — its
one-numeral-8-roles audit is ledger C42 (docs/choice_ledger.yaml:571-579,
wave 3). GAP-1/C28: the cert-frontier KS-max surrogate REUSES this
aggregation and "inherits the defect if underived" (gapmap GAP-27
owner note, ADVISORY_S24_sota_gapmap_2026-08-12.md:748-749) — C27's
verdict is upstream input to the C28 build in this same wave; no
circularity (C28 decides the representation, C27 the operator).

---

## 2. SOTA CENSUS

### 2.1 Query trail (WebSearch, 2026-08-19; queries derived from §1)

1. "Kreisselmeier-Steinhauser constraint aggregation conditioning
   adaptive parameter aerostructural optimization review"
2. "semi-infinite programming adaptive discretization exchange method
   algorithm review 2021 2022 2023"
3. "Kennedy Hicken 'Improved constraint-aggregation methods' 2015"
4. "log-sum-exp smoothing max function Hessian curvature
   ill-conditioning bound optimization smooth approximation"
5. "semi-infinite programming duality measure-valued multiplier
   discretization convergence exchange working set atoms"
6. "constraint aggregation adjoint PDE-constrained aerodynamic shape
   optimization 2023 2024 2025 KS function differentiable"
7. (page fetch) optimization-online.org LSE near-optimality page —
   exact theorem statement pinned (only page-verified web item below).

### 2.2 Corpus recency

Span **1976-2026**. Histogram (items actually consumed below):
1976-1993: 3 (Blankenship-Falk; Kreisselmeier-Steinhauser; Hettich-
Kortanek). 2005-2009: 4 (Poon-Martins x2; Lopez-Still; Shapiro).
2015-2018: 4 (Kennedy-Hicken; IP-adaptive C&S 2015; Lambe-Kennedy-
Martins; wing-surrogate adaptive-KS 2018). 2021-2023: 4 (APJOR
exchange; Djelassi-Mitsos unbounded-SIP; quadratic-rate adaptive
discretization; convex-SIP inexact oracles). 2024-2026: 4+ (stress-TO
aggregation items 2024-2025; AL comparative IJNME 2025;
**Samakhoana-Grimmer LSE near-optimality, Dec 2025 upd. Jul 2026** =
newest). Modern refined literature REACHED: the 2021-2026 tranche is
methods-active (SIP algorithmics, aggregation-vs-AL comparatives, and a
new smoothing-optimality theorem), not classics re-cited.

### 2.3 Per-source one-liners (evidence level marked)

Smooth-aggregate family:
- **Kreisselmeier-Steinhauser 1979** — the KS function; classic origin
  (named via the M0 adopt-or-declare corpus and census hits; not
  re-read). [classic, corpus-anchor]
- **Poon-Martins, "An adaptive approach to constraint aggregation using
  adjoint sensitivity analysis", SMO 2007 (+ CASI 2005 conf.)** —
  adaptive rho update from constraint sensitivities; motive = accuracy
  recovery when many constraints are active at budget rho.
  [abstract-level] https://link.springer.com/article/10.1007/s00158-006-0061-7
- **Kennedy-Hicken, "Improved constraint-aggregation methods", CMAME
  289:332-354, 2015, DOI 10.1016/j.cma.2015.02.017** — induced
  exponential/power aggregates; addresses estimate accuracy and MESH
  DEPENDENCE of discrete aggregates (functional/continuous forms).
  [abstract-level] https://www.sciencedirect.com/science/article/pii/S0045782515000663
- **"Strategies for adaptive optimization with aggregation constraints
  using interior-point methods", Computers & Structures 2015** — the
  M0-named "interior-point adaptive aggregation 2015"; notes that very
  large local curvature of the aggregate yields ill-conditioned
  Hessians. [abstract-level] https://www.sciencedirect.com/science/article/abs/pii/S0045794915000620
- **Lambe-Kennedy-Martins, "An evaluation of constraint aggregation
  strategies for wing box mass minimization", SMO 2017** — modern
  comparative evaluation of aggregation strategies under adjoints.
  [title+context-level] https://link.springer.com/article/10.1007/s00158-016-1495-1
- **"Constraint aggregation for large number of constraints in wing
  surrogate-based optimization", SMO 2018** — adaptive-KS variant in
  surrogate context (the M0 adopt-or-declare block names "SAKS 2018" in
  this slot). [abstract-level] https://link.springer.com/article/10.1007/s00158-018-2074-4
- **Samakhoana-Grimmer, "An Elementary Proof of the Near Optimality of
  LogSumExp Smoothing", Optimization Online, 2025-12-11 (upd.
  2026-07-12)** — PAGE-VERIFIED: LSE smoothing of max over d terms has
  gap <= ln(d), and EVERY overestimating smoothing must have gap >=
  ~0.8145 ln(d) (LSE within ~1.23x of optimal; exactly-optimal
  constructions exist only in small d). The gap-vs-smoothness tradeoff
  of the KS class is STRUCTURAL, not an implementation defect.
  [page-verified] https://optimization-online.org/2025/12/an-elementary-proof-of-the-near-optimality-of-logsumexp-smoothing/
- **LSE conditioning corpus (topic pages + LSEMINK line)** — standard
  LSE Hessian rho(Diag(s) - s s^T) (softmax covariance): curvature
  scales with rho, softmax concentration = rank-deficient/one-hot
  regime; Newton-type fixes (LSEMINK) exist for LSE OBJECTIVES —
  recognition that LSE ill-conditioning is a named problem.
  [topic-page level] https://www.emergentmind.com/topics/log-sum-exp-objective

SIP / exchange family:
- **Blankenship-Falk 1976** — the exchange (cutting) method; finite
  convergence under mild assumptions (named in O-F18 advocacy;
  classic). [classic, corpus-anchor]
- **Hettich-Kortanek, "Semi-Infinite Programming: Theory, Methods, and
  Applications", SIAM Review 1993** — canonical SIP survey (named in
  P-F16 advocacy). [classic] https://epubs.siam.org/doi/10.1137/1035089
- **Lopez-Still, "Semi-infinite programming", EJOR 2007** — survey;
  exchange methods generally more efficient than pure discretization.
  [abstract-level] https://www.sciencedirect.com/science/article/abs/pii/S0377221706008782
- **Shapiro, "Semi-infinite programming, duality, discretization and
  optimality conditions", 2008/2009** — SIP duality: dual variables are
  MEASURES on the index set; no-gap duality <-> convergent
  discretizations; the formal home of the measure-valued multiplier
  semantics in axis (A3). [abstract-level]
  https://optimization-online.org/2008/07/2028/
- **"On Exchange Methods for Nonlinear Semi-Infinite Programs", APJOR
  2021** — active algorithmic line on exchange for nonlinear SIP.
  [title-level] https://www.worldscientific.com/doi/10.1142/S0217595921500433
- **Djelassi-Mitsos(-Stein) 2021 line, incl. "Adaptive
  discretization-based algorithms for SIP with unbounded variables"** —
  modern adaptive-discretization SIP with convergence guarantees.
  [abstract-level] https://optimization-online.org/2021/11/8666/
- **"An adaptive discretization method solving semi-infinite
  optimization problems with quadratic rate of convergence",
  Optimization 71(8), 2022** — adaptive SIP discretization with
  quadratic rate. [abstract-level]
  https://www.tandfonline.com/doi/full/10.1080/02331934.2020.1804566
- **"Convex semi-infinite programming algorithms with inexact
  separation oracles", 2023** — exchange with inexact inner solves —
  directly the regime of a numerically-solved inner problem.
  [title+abstract-level] https://arxiv.org/pdf/2307.14181

Aggregation-free modern line:
- **Silva et al., "Stress-Constrained Topology Optimization With the
  Augmented Lagrangian Method: A Comparative Study of Subproblem
  Solvers", IJNME 2025** (+ the 2020-2025 AL stress-TO line it heads) —
  AL handles ALL local constraints without aggregation at scale;
  comparative claims that AL is more consistent than aggregation are
  TO-domain evidence. [abstract-level]
  https://onlinelibrary.wiley.com/doi/10.1002/nme.70066
- **Stress-TO aggregation items 2024-2025** (multi-material P-norm SAE
  2024; two-scale aggregation for AM, 2025) — aggregation is still live
  production practice at scale; adaptive scaling/interpolation on top
  of P-norm. [abstract-level]
  https://saemobilus.sae.org/articles/stress-constrained-multi-material-topology-optimization-2024-01-2458 ;
  https://www.tandfonline.com/doi/full/10.1080/17452759.2025.2450276

### 2.4 Ratified cava rows consumed (per-row, IDs of the cava)

- **Cava C30** (ADVISORY_litreview_confrontation_2026-08-13.md:1117,
  overview :83): the record contribution formula NAMES "l'aggregazione
  KS a rho derivato" as OURS — the C27 operator is paper-visible
  contribution surface, so the conditioning axis cannot stay
  never-adjudicated without touching the P-1 claims. Consumed as
  stakes-raiser for this panel.
- **Namespace collision declared:** the cava's own row "C27" (:1115) is
  the Wintenberger-Shepherd litmap correction — UNRELATED to ledger
  C27 (the cava C-numbering is its own). Cited only to prevent
  cross-reference confusion.
- **Absence, search-proven:** grep of the cava for
  `C27|Poon|Kennedy|Kreisselmeier|aggregat|semi-infinite|exchange`
  (case-insensitive) hits only D-40 (:1230, Wintenberger row rewrite),
  the C27-collision row (:1115), and the C30/:83 "KS a rho derivato"
  mentions — the cava contains NO row on aggregation conditioning or on
  the C27 alternatives. The confrontation corpus (25 papers) did not
  touch this choice; the census above is the first modern sweep of the
  conditioning axis for this row.

### 2.5 Dedup (navigation-first; greps stated)

- docs/choice_ledger.yaml — C27 :407-417 (this row); C42 :571-579
  (K_RICH reuse, wave 3, named-not-decided); C28 :419-427 (consumer of
  this verdict).
- docs/findings_registry.yaml — grep
  `Poon|Kennedy|Kreisselmeier|adaptive-KS|semi-infinite|Blankenship|exchange`:
  NO rows (absence search-proven). Grep `GAP-27|argmin|chatter|aggregation`:
  header mapping :84-89 (GAP-27 and GAP-1 MAPPED to row
  `margin-governor:G1-three-jump-channels`, no re-mint allowed) and the
  carrier row itself :232-240 (owner: "F2, GAP-27/GAP-1 window"). This
  panel CITES that row as the registry carrier; it mints nothing.
- docs/claims_registry.yaml — [X-MGOV] :1346-1358 (incumbent carrier
  claim + falsifiers R-KS/R-GRAD/R-G1/R-FD; scope field records the
  adopt-or-declare: "Poon-Martins/SAKS NOT adopted, reason stated");
  [X-TBAK] :1360-1372 (adjacent ship-time backoff, untouched here).
- docs/literature_registry.yaml — grep
  `Poon|Kennedy|Kreisselmeier|adaptive-KS|semi-infinite|Blankenship|exchange|aggregation`:
  NO rows (absence search-proven). The aggregation corpus lives only in
  M0's adopt-or-declare block and the gapmap; §4 proposes registry rows
  (proposal only — this panel edits nothing outside blocco3/).
- Ledger-internal seeded row: the "TR-SQP-with-P4-gate vs
  nonsmooth/MPCC handling of the certifiability frontier" seeded
  question named in brief §C28 belongs to the C28 panel (its
  adjudication half); NOT consumed here — only the MPCC OPERATOR option
  (f) is closed below on C27's axes.

---

## 3. ADJUDICATION

### 3.0 The incumbent's genuine case (represented, not strawmanned)

[X-MGOV] of record (M0:2336-2375; claims_registry.yaml:1346-1358):
KS-min in shifted overflow-free form with the log-sum-exp bounds
`v_min - ln(N)/rho <= KS <= v_min` [THEOREM, standard]; rho DERIVED
= K_RICH ln(N)/mu_0_min, pinning the enforcement gap at
mu_0_min/K_RICH by construction — measured instance of record
m_ref = 6.810298e-01, N = 3498, rho = 766.83, gap = 1.0641e-02
(M0:2341-2343). Enforcement direction is conservative-CORRECT: KS <=
v_min, so `KS >= mu_0` implies the true min-lane margin >= mu_0; the
gap only shrinks the feasible region, and the shrinkage is pinned below
the enforcement resolution. G1 finite-negative surrogate
[PRACTICE, rejector-proven], AD gradient verified against two-step
Richardson FD (3.29e-06 vs band 5.92e-05, M0:2351-2353). ADOPT-OR-
DECLARE of record (SOTA search 2026-08-11, M0:2369-2375): adaptive-rho
variants (Poon-Martins SMO 2007; IP-adaptive 2015; SAKS 2018) NOT
adopted — "their motive (accuracy recovery under tuned budget rho with
many active constraints) is void here where rho is derived to pin the
gap below the enforcement resolution and gradients are exact AD."
Cost (A4): ONE VJP per iterate for the whole family — optimal.
The blind O-tree re-derived the incumbent's own bound unprompted
(P3 dry proof, phaseA_tree_optimization.md:1046-1049: rho = ln(m)/eta_KS
is DERIVED — "decides the 'is rho magic' objection"): the derived-rho
half of the incumbent is INDEPENDENTLY CONFIRMED, not merely defended.

This is a genuinely strong case on axes (A1) and (A4). The ledger
status is honest about where it stops: "survey answered accuracy axis;
conditioning axis NEVER" (choice_ledger.yaml:417).

### 3.1 The measured defect on the frozen axis (A2)

GAP-27 [CONFIRMED, measured P1 reproduced]
(ADVISORY_S24_sota_gapmap_2026-08-12.md:728-750): "the KS rho
derivation controls conservativeness only: at rho = 5.75e4 the 'smooth'
aggregate is a hard min to machine precision (one-hot gradient,
curvature ~rho/4), and this instance sensitivity is declared nowhere in
the derivation." Mild S22 gets a genuine aggregate (~20 weighted
lanes); deep-DEF gets a hard min (1/45 lanes above 1e-12 —
model-inferred, Q10 caveat carried). Panel-named symptom AC12
(gapmap:865): argmin-tie chatter at rho = 5.75e4 — gradient swap at
lane ties reads as TR model error. Exposure: deeper ladder / smaller
m_ref drives rho ~ 1e7 (gapmap:742). Registry carrier:
findings_registry.yaml:232-240 (`margin-governor:G1-three-jump-channels`,
severity medium, owner "F2, GAP-27/GAP-1 window"). Panel observation
(formula-level, no new number): rho = K_RICH ln(N)/mu_0 also GROWS
with mesh refinement at fixed mu_0 (N is the lane count) — log-mild,
but the direction is toward the defect, and it makes the discrete
aggregate mesh-dependent in exactly the sense Kennedy-Hicken 2015
names.

Census verdict on (A2)'s structure — the decisive modern item: the
gap-vs-smoothness tradeoff is a THEOREM-BACKED WALL, not a KS
implementation artifact. Samakhoana-Grimmer (2025-12, page-verified):
every overestimating smoothing of a d-term max must carry gap
>= ~0.8145 ln(d); LSE achieves ln(d). Translated to the incumbent's
normalization: ANY smooth aggregate that pins the gap at mu_0/K_RICH
must carry sharpness (curvature scale) within a constant (~1.23x) of
the incumbent's rho. Consequence: **no member of the smooth-aggregate
class — adaptive-KS, induced-exp/power, p-norm, or any future
variant — can hold the incumbent's gap pin at deep floors without the
incumbent's conditioning.** The only escapes are structural: shrink
the EFFECTIVE d the smoothing must cover (working set), or leave the
smooth class for the true polyhedral structure (explicit near-binding
constraints / exchange / AL).

### 3.2 Alternative-by-alternative (tree advocacy + census; stated-reason outcomes)

**(b) adaptive-KS (Poon-Martins 2007; + SMO 2018 surrogate variant).**
Advocacy: none of the trees advocates it (0/4). Census: motive =
accuracy recovery under budget rho with many active constraints.
Incumbent's adopt-or-declare (M0:2369-2375) already voided that motive
(rho derived, exact AD gradients); this panel ADDS the (A2) reason: the
adaptive update RAISES effective rho where constraints cluster — it
walks INTO the one-hot regime, aggravating GAP-27, and the 2025
near-optimality theorem denies it any gap-at-lower-curvature miracle.
**CLOSED (stated reasons: motive void on (A1) of record; direction
wrong on (A2); no tree advocacy).**

**(c) induced-exp/power aggregates (Kennedy-Hicken CMAME 2015) + plain
p-norm.** Advocacy: NEGATIVE from the blind O-tree — option 3 REJECTED
with stated reason "worse conditioning at high p; KS's error bound is
additive and explicit" (phaseA_tree_optimization.md:1012-1014). Census:
induced aggregates improve ESTIMATE accuracy and fix mesh dependence
via functional (measure-weighted) forms [abstract-level]; they remain
smooth aggregates, so the §3.1 wall applies to them unchanged.
**CLOSED as primary (stated reasons: subject to the same
gap-curvature theorem; blind-tree conditioning rejection; incumbent's
additive-explicit bound is the better certificate instrument).
ABSORBED as refinement: the measure-weighted (functional) form is the
natural cure for the ln(N)-mesh-dependence observation of §3.1 —
carried into the F2 duty as an optional variant of the in-set
aggregate, evidence level abstract-only.**

**(d) two-constant rule (gap AND curvature/weight-support budget;
gapmap GAP-27 SOTA column :738-741, rigor note :750 "keeps the
conservativeness theorem intact").** Attribution honesty: this is a
repo-derived rule (gapmap-named repair), not an external method — no
literature item of that name surfaced in the census; its two
ingredients are exactly the two sides of the census tradeoff (gap
bound ln(N)/rho of record; curvature ~rho of record + LSE Hessian
form). Adjudication: ADOPT as the DERIVATION REPAIR wherever a smooth
aggregate is used — rho := min(rho_gap, rho_curv), both constants
derived, with the beyond-budget regime DECLARED. By §3.1 the two
budgets MUST conflict at sufficient depth (the theorem says so) — so
the rule cannot dissolve the wall; its honest role is the **ex-ante
ESCALATION TRIGGER**: rho_gap > rho_curv at a rung fires BEFORE any
walk, declaring the smooth-only operator infeasible-by-derivation at
that rung. **ADOPTED with re-scoped role (trigger + declaration, not
cure).**

**(e) exchange/working-set hybrid — the 3/4 tree challenge.**
- O-F18 (phaseA_tree_optimization.md:996-1049; recommendation
  :1031-1037): "4 wrapped around 2" — exchange on the true 1-D inner
  problem for exactness, KS only WITHIN the working set for
  smoothness, inter-node certification via option 1's measured
  Lipschitz margin (:1002-1006); multiplier semantics: exchange
  multipliers at convergence approximate the measure-valued SIP
  multiplier — "precisely the multipliers carrying marginal-value
  meaning of (ii): dJ/dc_sep = -Int lambda(xi) d(binding measure)"
  (:1034-1037). Falsifier :1039-1044: a binding ARC (working set grows
  without saturation) -> switch to binding-arc free-boundary
  parametrization.
- V-F23 (phaseA_tree_variational.md:1036-1070; recommendation
  :1063-1066): O1+O2 combined — exchange finds binding phases,
  modulus-of-continuity covering certifies between them, margin
  m >= L_xi*Delta_xi/2 a DERIVED safety factor; inner 1-D search
  certifiable by Piyavskii-Shubert with the same measured L_xi
  (:1047-1051). Falsifier :1067-1070: refined-grid violation beyond
  covering margin falsifies the modulus protocol.
- P-F16 (phaseA_tree_propulsion.md:614-633; recommendation :628-633):
  KS in-loop + adaptive phase refinement near convergence "so the
  certificate is issued against the TRUE semi-infinite constraint, not
  the smoothed one"; MANDATORY post-hoc fine-phase sweep — a violating
  phase between nodes VOIDS the certificate.
Census support: the exchange/adaptive-discretization line is the
active modern SIP algorithmics (Lopez-Still 2007 efficiency claim;
APJOR 2021; Djelassi-Mitsos 2021; quadratic-rate 2022; inexact-oracle
2023); multiplier semantics grounded in SIP duality (Shapiro
2008/2009: duals are measures; exchange multipliers = atoms).
Transposition to inst-L (panel content): for the finite lane family the
"inner problem" is an exact argmin scan over the already-computed val
field (free); "exchange" = a working set/near-binding BAND
B(W) = {i : v_i <= v_min + w} handed to the optimizer as an explicit
vector constraint block (the margin_factory slot already admits
vector values — gapmap:101-103), with the complement fenced by the
incumbent KS at two-constant-derived rho (fence inactive => zero
conditioning cost). Ties then live in the SQP active set — the
polyhedral treatment SQP is built for: at a two-lane tie the active
set holds two rows with two multipliers, no kink is smoothed, and the
per-lane prices are exactly the atoms of (A3). Under-resolution risk
(w too small) is falsifiable (F-C27-3 below). Cost (A4): |B| extra
VJP rows (or one batched vmap-VJP) per iterate, |B| ~ tens at worst;
the scan is free.
**ADOPTED AS STRUCTURE, measurement-gated on (A2) (the build+measure
half is the F2 duty — §4).** Burden note: 3/4 blind convergence is
evidence, not a verdict (brief §0.4); the adoption below rests on the
census theorem (§3.1) + the measured defect (GAP-27) + the exactness
semantics, with the incumbent RETAINED inside the hybrid (fence + G1
surrogate + sole operator wherever the two-constant check passes).

**(f) MPCC argmax-tracking (P-F16 O5, :623-625).** Advocacy: its own
tree labels it "sharp but fragile". Census: MPCC
smoothing (Scholtes; Fischer-Burmeister) is named in the GAP-1 SOTA
column for the C28 representation question (gapmap:84-85), where it
belongs. **CLOSED here (stated reasons: fragility named by its own
advocate; unnecessary — the inner problem is an exact scan (inst-L) or
cheap certifiable 1-D search (inst-XI); the seeded MPCC-vs-TR-SQP
ledger question is C28's, dedup respected).**

**(g) CVaR/chance (O-F18 opt.5 :1021-1025) and scenario approach
(V-F23 O3 :1052-1056).** Both trees close their own options with
stated reasons: intermittent separation changes the ENGINEERING
meaning (unsteady side loads); "mu-a.e." is a hard certified-class
constraint, not a chance constraint. **CLOSED (tree-stated reasons
carried; retained as diagnostic reporting only — CVaR profile of
margins tells WHERE the cycle binds).**

**(h) exact-penalty/NCP of the a.e. constraint (O-F18 opt.6
:1026-1029).** **CLOSED (tree-stated reason carried: degenerate
multipliers at solutions destroy the (A3) marginal-value
interpretation).**

**(i) interval/Taylor-model enclosure over xi-cells (V-F23 O4
:1057-1059).** **CLOSED (tree-stated reason carried: requires
arithmetic-level solver access — disproportionate).**

**(j) aggregation-free AL with all local constraints (census-found,
Silva et al. IJNME 2025 + 2020-2025 stress-TO AL line).** No tree
advocates it (0/4 — the trees never priced it). Census: at TO scale it
is a live alternative with comparative claims against aggregation
[abstract-level, TO-domain]. Against the frozen context: the AL outer
loop multiplies march counts (each subproblem re-walks), the evidence
is domain-transplanted (TO elasticity, not marched-Euler certificates),
and it buys nothing on (A1) that exchange+covering does not already
give exactly. **CLOSED as primary (stated reasons above); NAMED
FALLBACK of record if the working-set road is falsified (F-C27-3
repeated-escape branch): it is the no-smoothing exact treatment with
honest per-lane multipliers.**

**(k) discretize-all-only (O-F18 opt.1 :1002-1006 used ALONE; also
inst-XI all-nodes).** For inst-L this is the AL/vector route without
its multiplier management; for inst-XI it leaves the between-node gap
open unless the Lipschitz margin is added — at which point it IS the
covering half of (e). **CLOSED as standalone (stated reason:
subsumed — its exactness ingredient (measured Lipschitz inter-node
margin) is absorbed into the adopted covering; its all-N cost buys
nothing extra).**

**(l) LSE Hessian-shift Newton machinery (LSEMINK line, census).**
**CLOSED — not applicable (stated reason: designed for LSE OBJECTIVES
in Newton solvers, not for constraint blocks in TR-SQP; cited only as
recognition that LSE concentration ill-conditioning is a named
problem).**

### 3.3 Axis synthesis

- (A1) exactness: incumbent theorem intact and blind-re-derived; the
  hybrid does not touch it (fence keeps the same bound; explicit band
  rows are exact). inst-XI needs covering + mandatory post-hoc sweep —
  the incumbent has NO between-node answer today; adopted from
  V-F23/P-F16 as certificate semantics (no measurement needed to adopt
  the OBLIGATION; the measured object is L_xi itself).
- (A2) conditioning: smooth class is walled (census theorem);
  two-constant rule = trigger; hybrid = the structural fix; measured
  half gated (F2 duty).
- (A3) multipliers: hybrid strictly better at ties (atoms vs one-hot
  chatter); KS softmax weights remain the smooth price distribution
  where the aggregate is genuine (healthy regime of record,
  rho = 766.83, ~20 weighted lanes).
- (A4) cost: incumbent optimal (1 VJP); hybrid bounded (+|B| rows,
  free scan); adaptive-KS/induced neutral; AL worst (outer-loop march
  multiplication). No option is closed on cost alone.

---

## 4. PROPOSED VERDICTS + DUTIES

### 4.1 Proposed ledger outcome for C27 (one row)

**Measurement-gated SPLIT** (brief §0.4 vocabulary), with the converged
half stated now:

CONVERGED-panel (structure + protocol):
1. **Operator structure adopted:** working-set/exchange hybrid —
   explicit near-binding band B(W) as a vector constraint block through
   the existing margin_factory slot; complement fenced by the incumbent
   KS-min; the incumbent REMAINS the sole operator at every instance
   where the two-constant check passes (mild regime of record), and
   remains the G1 survive-and-report surrogate everywhere (REQ-NONSTALL
   needs the globally-finite scalar; the band block does not provide
   it).
2. **Two-constant rule adopted as derivation repair + ex-ante trigger:**
   rho := min(rho_gap, rho_curv), both derived; rho_gap > rho_curv at a
   rung DECLARES smooth-only infeasible at that rung and mandates the
   band block (no experiment needed to fire — the census theorem
   guarantees the conflict occurs at depth).
3. **inst-XI certificate semantics adopted (obligation, conditional on
   the cycle-problem instantiation window):** measured-L_xi covering
   margin m >= L_xi*Delta_xi/2 between certified phases + MANDATORY
   post-hoc fine-phase sweep; a violating phase between nodes VOIDS the
   certificate (refine and re-issue). Inner 1-D search certifiable by
   Lipschitz global optimization with the same measured L_xi.
4. **Multiplier reporting adopted:** wherever the band block is active,
   report per-lane multipliers (atoms) as the (ii) marginal-value
   carriers; where only KS is active, report the softmax weight
   distribution + effective support count n_eff.

MEASURED HALF (binding F2 duty — the gate): pure-KS-at-depth vs hybrid
on the recorded instances; protocol and falsifiers pinned NOW (§4.2).
Proposed status transition: SINGLE-AUTHOR -> ADJUDICATED-SPLIT
(structure CONVERGED-panel 2026-08-19; conditioning axis = measured
duty open, owner F2).

### 4.2 Protocol + falsifier pins (exact, derived, refutation-directional)

**Duty name: F2-DUTY-C27-AGGCOND** — "aggregation conditioning
microbenchmark + working-set hybrid pilot". Window: the GAP-27/GAP-1 F2
window already named by findings_registry.yaml:239 (cite, no re-mint).
SUBSUMES the gapmap named-for-S25 probe "[R3] argmin-swap census along
the recorded S24 walk" (gapmap:746-747, :961) — same experiment family,
one execution.

Instances (all committed of record): the S22 mild instance
(rho = 766.83 regime) and the S24 deep-DEF recorded walk
(rho = 5.75e4 regime), on the pre-registered floor ladder
mu_0_k = m_ref/2^k, k = 1..4.

Arms: **A** = incumbent pure KS-min derived-rho (of record, untouched).
**B** = hybrid: band B(W) = {i : v_i <= v_min + w} as vector
constraints + KS fence on the complement at two-constant rho.

Derived quantities (formulas pinned now; numbers come from the
measured run — R5):
- band width w = K_RICH * (max over the recorded walk of the
  per-accepted-step change in v_min and in any band-adjacent lane) —
  the band must contain every lane reachable as argmin within one
  accepted step; measured on the committed walk artifacts.
- rho_curv = the largest rho whose tie-direction curvature (~rho/4 of
  record, GAP-27) keeps the constraint-model error within the TR
  acceptance band at the walk's recorded radii — every input of record
  on the walk.
- chatter red-line: rejected-step rate in swap-adjacent iterations
  vs K_RICH x the off-swap baseline rate (both measured on the same
  walk). Wall-time budget: the AC12 monitor (per-rung wall time inside
  the [P4] cap) — reused, not re-derived.
- K_RICH's role in all three = a NAMED C42 dependency (wave 3); if C42
  replaces the numeral per-role, these formulas inherit the per-role
  constants without structural change.

Falsifiers (what refutes what):
- **F-C27-1 (kills pure-KS-at-depth):** at any rung with
  rho_gap > rho_curv, arm A shows swap-adjacent rejected-step rate
  above the red-line while arm B stays in band => incumbent CLOSED as
  sole operator at depth; hybrid adopted there.
- **F-C27-2 (kills the hybrid's necessity):** arm A within band at ALL
  rungs k=1..4 on BOTH instances AND no two-constant conflict fires =>
  hybrid shelved as escalation-only; incumbent re-labeled
  CONVERGED-measured with the two-constant declaration added to
  [X-MGOV].
- **F-C27-3 (kills the band construction):** a lane outside B becoming
  argmin within one accepted step (band-escape) => w-derivation
  falsified, re-derive (per-lane step-Lipschitz bound); REPEATED escape
  => working-set road CLOSED, fall back to the named AL route (§3.2 j).
- **F-C27-4 (inst-XI limb, fires at cycle instantiation):** post-hoc
  fine-phase sweep finds a violating phase between nodes => certificate
  VOID (refine, re-issue); refined-grid violation exceeding the
  covering margin => L_xi modulus protocol falsified, tighten
  (V-F23:1067-1070 recalibrated). Working set growing without
  saturation (binding ARC) => switch to binding-arc parametrization
  (O-F18:1039-1044 recalibrated).
- **F-C27-5 (multiplier semantics, reporting):** at converged optima,
  compare band-block multipliers and KS-distributed prices against
  dJ/dc from a perturbed-c re-solve; disagreement beyond the derived
  band ON THE KS SIDE at one-hot instances makes the (A3) defect a
  number. Non-blocking; feeds the (ii) theory carriers.

Certificate-equivalence guard (both arms, every run): identical
accept/reject on every rung at the declared resolution; ANY enforcement
divergence between arms = protocol red (the hybrid must change
conditioning, never semantics).

### 4.3 Proposed registry deltas (PROPOSALS ONLY — this panel edits nothing outside blocco3/)

- choice_ledger C27: outcome per §4.1; evidence += this file; the
  in-row note should cite findings row
  `margin-governor:G1-three-jump-channels` and name F2-DUTY-C27-AGGCOND.
- literature_registry: add rows for Poon-Martins 2007, Kennedy-Hicken
  2015, Lambe-Kennedy-Martins 2017, Shapiro 2009, Lopez-Still 2007,
  Samakhoana-Grimmer 2025 (grep-proven absent today, §2.5) — tier per
  litreview protocol (all currently [APERTO]-level except the
  page-verified Samakhoana-Grimmer statement).
- No new findings row (GAP-27 carrier exists; dedup clause of record).
- C28-panel handoff (same wave): the C28 surrogate's aggregation
  constants inherit §4.1(2) (two-constant rule) — dependency named,
  direction C27 -> C28.

### 4.4 Orchestration weight (SR-9, this panel)

Solo panel, 1 agent, single pass; 7 web queries + 1 page fetch; ~14
repo reads/greps; no subagents; no re-seed (pool unchanged).

---

## 5. MACHINE SUMMARY

```json
{
  "cluster": "C27",
  "rows": {
    "C27": {
      "proposed": "MEASUREMENT-GATED SPLIT: structure CONVERGED (working-set/exchange hybrid via vector-valued margin_factory band + incumbent KS retained as fence/G1 and as sole operator where the two-constant check passes; two-constant rule adopted as derivation repair + ex-ante escalation trigger; inst-XI covering + mandatory post-hoc sweep adopted as certificate semantics; per-lane multiplier atoms = (ii) semantics). Conditioning axis measured half = F2 duty on recorded S22/S24 instances, falsifiers F-C27-1..5 pinned. Alternatives adaptive-KS, induced/p-norm(primary), MPCC, CVaR/chance, scenario, exact-penalty-NCP, interval-enclosure, AL-all-local(primary, named fallback), discretize-all-only, LSE-Hessian-shift all CLOSED by stated reason.",
      "gated": true,
      "duty": "F2-DUTY-C27-AGGCOND (subsumes gapmap [R3] argmin-swap census; window = GAP-27/GAP-1 F2 window of findings row margin-governor:G1-three-jump-channels; inst-XI limb conditional on cycle-problem instantiation)"
    }
  },
  "census_recency": "1976-2026; histogram 1976-1993:3, 2005-2009:4, 2015-2018:4, 2021-2023:4, 2024-2026:4+; newest = Samakhoana-Grimmer LSE near-optimality (2025-12, upd. 2026-07, page-verified), Silva et al. IJNME AL comparative (2025), convex-SIP inexact oracles (2023)",
  "alternatives_closed": 10,
  "inflation_check": "done"
}
```
