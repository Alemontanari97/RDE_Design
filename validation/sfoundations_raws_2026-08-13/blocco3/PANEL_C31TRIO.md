# PANEL — CLUSTER C31TRIO (C31-IP / C32 / C33)
S-FOUNDATIONS-C2, Blocco 3 wave 2, 2026-08-19. Panel of record per
BRIEF_wave2_panels.md §C31TRIO under §0 (wave-1 frame verbatim),
§0-bis (directive axes), §0-ter (world-class census protocol),
rewritten COMPLETE per BRIEF_wave2_reconcile.md (RECONCILE PANEL) —
see the RECONCILIATION DECLARATION at the end of this file.
BASE = validation/sfoundations_raws_2026-08-13.
WAVE-1 CONSUMED: VERDICT_wave1.md read IN FULL (C28 §2.1, C27 §2.2,
C9 §2.3, C11 §2.4, cross-cluster §3, deltas §4) PLUS the now-landed
ledger rows C9 (docs/choice_ledger.yaml:219-228), C11 (:240-250) and
C56 (:731-740) with VERDICT_C9C11_supplement.md §1/§4.3/§4.4/§5 — the
C56 gradient-role forecast is OWED TO THIS CLUSTER and is CONSUMED in
§3.1-bis below, explicitly.
CENSUS VALIDITY STAMP: all web queries run 2026-08-19 in THIS
reconcile window (query protocol table §2.0); all greps and source
reads re-measured in this window (SR-12).

WRITE-ORDER DECLARATION (§0-ter(b) honesty): §1 — questions and
decision criteria — was written to this file by the killed wave-2
panel BEFORE any web query of its window was launched; this
reconcile slot VERIFIED §1 against every cited source in its own
window BEFORE launching its own queries, then appended §2-§5.
Reconcile-window amendments to §1 are marked [AMENDED-AT-RECONCILE]
with reason inline; every other §1 sentence stands as found and
verified. The refuter attacks post-hoc rationalization against the
frozen criteria as written.

---

## 1. FROZEN FORMAL STATEMENT

### 1.0 Cluster shared sub-problem

Second-order infrastructure of the certified design loop. Operational
context (of record, cite-not-relitigate): certified marched
axisymmetric Euler solver with fitted fronts (S1 class); JAX
custom_vjp discrete adjoint stack, one-lowering discipline (findings
row engine:cross-lowering-gradient-floor); TR-SQP driver `run_trsqp`
segmented by RK-G decision-flip events, each segment = a FRESH scipy
`minimize(method='trust-constr')` call on the frozen-plan replay,
P4/P3(ii) binary certification gates outside the KKT system
(facet validation/sota_gapmap_raws_2026-08-12/s24_gap_driver-nonsmooth.md:4-21;
kickoff §4bis, docs/rde_nozzle_brick2_kickoff.md:346-366, 404-413);
production instance is SMALL-DENSE (n ~ 9-10 dofs today, [X-AKNO] may
enrich to m ~ 10-12), function evaluations expensive (post-M-chain
measured of record: record 5.58-8.30 s median, segment 14.9-20.1 s
pessimistic — memory s25bis-speed-complete; S24 frontier walks 19-21
segments, decisive rung 4560 s pre-M-chain — facet G4; speed-audit
numbers cited, NOT re-measured, per brief).

WAVE-1 INPUT CONSUMED (changes what the engine must close): C28
verdict = HYBRID priced-frontier representation ADOPTED-FOR-MEASUREMENT
— GAP-1 KS-max surrogate on traced per-cell certification ratios
enters the KKT system as an INEQUALITY constraint with multiplier
mu_c; P4/P3(ii) binary gates KEPT as absolute verifiers; pins F-1..F-4;
duty [P-CERTKS]+[P-BSTAT] with **[P-IPADJ] on the same critical path**
(VERDICT_wave1 §2.1); C28's F-2 falsifier escalates TO THIS CLUSTER
("escalate to the engine re-adjudication ([P-IPADJ]/C31, bundle
fallback named)"). C27 verdict = incumbent KS-min fence retained +
near-binding band block (explicit VECTOR margin rows, fixed arity
k_max, through the margin_factory slot) as the DERIVED escalation
route (VERDICT_wave1 §2.2). Consequence, of record already in the
findings row driver-nonsmooth:ip-path-unadjudicated:1236-1244: "GAP-1
adoption makes the IP (or replacement) engine PERMANENT" — the
constraint set the engine sees is now permanently inequality-bearing
(cert KS-max row + margin governor row + possibly C27's k_max band
rows), so the equality-only Byrd-Omojokun path of the S18 §4bis
adjudication is no longer the production path ANYWHERE it matters.
Scipy method switch verified of record: `n_ineq == 0 ->
equality_constrained_sqp else tr_interior_point`
(minimize_trustregion_constr.py:403-406, Probe C, facet :36-39;
re-verified by the wave-1 judge, VERDICT_wave1 §0.1).

[AMENDED-AT-RECONCILE — reason: C56 landed at the C9/C11 landing
between the killed panel's write and this window] C56 INPUT CONSUMED:
the ledger row C56 (choice_ledger.yaml:731-740, "Adjoint REALIZATION
of record for the marched stack, per role") is MINTED and MIXED: the
DWR-weight role is CLOSED (C11 supplement, F11d pinned), the
indicator role closed by transitivity, and the GRADIENT role is
"OWED TO wave-2 C31TRIO (forecast, not consumed)". This panel
consumes that debt: the gradient-role adjoint realization is
adjudicated INSIDE the C31 engine question (§3.1-bis) because the
gradient realization is what the engine's W1 certificate-closure axis
consumes. C9's F9b gradient-consistency contract (O3.1 identity at
the same derived floor on adapted meshes) is inherited as a
constraint on every option below.

### 1.1 Row C31-IP — MAIN QUESTION

**Which optimizer engine CLOSES THE CERTIFICATE at a boundary-active
(cert-frontier-priced) optimum — delivers a KKT/B-stationarity
residual with source-adjudicated semantics, multipliers carrying the
(ii) marginal-value meaning, and per-segment termination/restart
compatible with RK-G segmentation and the P4 gate discipline — now
that C28 makes the inequality-capable engine permanent?**
[AMENDED-AT-RECONCILE — reason: C56 debt addressed to this cluster]
Sub-question, adjudicated as part of W1: which ADJOINT REALIZATION
supplies the gradient that certificate closure is claimed on (the
C56 gradient role).

Pre-registered decision criteria (what makes an option WIN; derived
from the question, frozen before search):
- **W1 certificate closure**: exposes accepted-iterate state,
  multipliers, and a KKT residual whose semantics on the INEQUALITY
  path are §4bis-grade source-adjudicable (open source, readable);
  supports clean callback termination + restart (RK-G segmentation is
  non-negotiable).
- **W2 active-set / multiplier crispness at boundary-active optima**:
  identifies the active certification constraint and returns crisp
  multipliers at finite tolerance. SQP-type active-set identification
  beats log-barrier smearing UNLESS the barrier engine's mu->0 ramp
  semantics are source-adjudicated and measured adequate (the S24
  res.v = +4.8582e4 at an INACTIVE constraint, adjudicated
  "barrier estimate, INFORMATION-ONLY", is the of-record symptom —
  facet G3:192-196).
- **W3 warm start across segments**: ~19-21 fresh minimize() calls
  per frontier walk are of record; cold barrier/slack restarts are a
  priced defect (facet G3:200-203); an engine that warm-starts
  multipliers/working set across segment restarts wins this axis.
- **W4 measured cost at n~10 dense**: large-scale sparsity machinery
  is worthless at this size (materiality valve); per-segment overhead
  beyond function evaluations is noise — W4 discriminates only
  through eval counts and restart churn.
- **W5 pinned-environment compatibility**: the env is PINNED (CLAUDE.md
  Preferenze; PyYAML incident of record): an engine requiring a new
  binary dependency (IPOPT/cyipopt, Uno) CANNOT be adopted in-window;
  it may only be named as an F2-measured alternative whose install is
  an O5-class session-boundary decision. This is a REAL asymmetry and
  is declared here, not hidden in the verdict.
- **WIN RULE**: an alternative wins the formal half if it beats the
  in-use tr_interior_point path on W2+W3 at non-worse W1/W4/W5; the
  incumbent IP path wins if [P-IPADJ] source adjudication certifies
  its optimality/multiplier semantics AND the measured barrier-restart
  overhead is inside existing derived bands. Engine flips are
  trajectory-changing (N5-class): the measured half is F2 by
  construction — the panel converges representation + protocol +
  primary candidate, never a flip-of-record.

### 1.2 Row C32 — MAIN QUESTION

**What curvature information does the TR model consume per RK-G
segment — fresh full FD Hessian at every segment base (incumbent),
SR1/quasi-Newton carry from certified accepted pairs, or HVP-based
truncated Newton (Steihaug-CG/Lanczos) — such that the model is
certificate-grade and rejector-guarded at the least measured cost,
preserving RK-G determinism and the P2 model-rebuild contract?**

Pre-registered decision criteria:
- **W1 determinism + P2**: any carried curvature must be a
  deterministic pure function of the certified walk history (replay =
  bit-identical matrix; facet G4:254-261 establishes this is
  achievable for accepted-pair-only quasi-Newton); stratum flips
  invalidate the flipped columns, not the world. An option that
  cannot state this loses outright.
- **W2 certificate separation**: the (iii) certificate at S* needs
  exact curvature (full spectrum or Lanczos with certified
  Kaniel-Paige brackets) REGARDLESS of the in-flight policy — the
  in-flight model only needs healthy TR rho-statistics. Options are
  judged as IN-FLIGHT policy; no option is allowed to degrade the S*
  certificate (it is out of scope by structure).
- **W3 measured cost of record**: incumbent = (n+1) gradient evals
  per segment base with ~one productive step per segment (facet
  G4:245-252; T2 FIRED on exactly this decomposition, :248-250). An
  alternative wins the cost axis only by removing O(n) evals/segment
  WITHOUT degrading acceptance rate — measured, never asserted.
- **W4 route facts (JAX/adjoint)**: fwd-over-rev HVP is BLOCKED as
  written — `solve` is `@jax.custom_vjp`+`defvjp` only
  (a1_ideal_march_jax.py:504-517; B-F11 verified at source,
  ADVISORY_S25bis_diff_convergence_2026-08-12.md:119); true price of
  exact HVP = implementing the implicit custom_jvp rule (speed audit
  N5: "adjudication-only, trajectory-changing"). Any HVP-based option
  must carry that build cost in its case; pretending jacfwd works is
  an inflation violation.
- **W5 rejector obligation**: whatever supplies curvature ships with
  a rejector (symmetry-defect band pre-symmetrization + directional
  second-difference Richardson — [P-HESSREJ] pattern, findings row
  driver-nonsmooth:hessian-no-rejector) because a wrong Hessian
  MASQUERADES as certifiability-limiting (the outcome-II attribution
  risk of record). A carry policy additionally needs the
  stale-symptom re-measure trigger (S18 status-2 xtol collapse
  detector, facet G4:268-271).
- **WIN RULE**: SR1-carry wins the in-flight axis iff the [P-QNCARRY]
  A/B on the recorded S18 walk shows eval-count reduction with
  identical certified outcomes and no rejector trips; fresh-FD stays
  if carry degrades acceptance or trips the rejector; HVP-truncated
  Newton becomes primary only after N5's custom_jvp lands AND the
  measured product cost beats the FD column cost (2-4 gradient-
  equivalents per product claimed by the tree, O-F21 item 6 — a
  number to MEASURE on this stack, not import).

### 1.3 Row C33 — MAIN QUESTION

**Where does the CONSTRAINT block's curvature in the Lagrangian
Hessian come from — scipy's silent identity-seeded BFGS per segment
(incumbent default), exact HVP (blocked as written), or
FD-of-exact-constraint-gradient measured per segment base (the R-3
policy extended to the constraint side) — given that at a cert/
margin-ACTIVE optimum the KS constraint curvature ~ rho/4 |grad m|^2
(rho up to 5.75e4 of record) can DOMINATE the measured objective
Hessian?**

Pre-registered decision criteria:
- **W1 policy symmetry**: constraint curvature policy must match the
  objective policy class (measured at segment base, frozen within
  segment) or state why not — the incumbent asymmetry (exact measured
  objective H + identity-seeded BFGS constraint H re-learned from
  scratch every segment) re-creates the exact S18 stale-model plateau
  mechanism on the constraint side (GAP-19 magnitude text, findings
  row constraints:margin-constraint-no-hess:1272-1280).
- **W2 route fact**: same as C32-W4 — fwd-over-rev blocked; the
  executable exact-ish option today is FD-of-exact-gradient applied
  to the constraint gradient (gm is one VJP — cheap vs record).
- **W3 materiality by activity**: margin INACTIVE at every recorded
  instance (declared boundary, zero recorded effect — GAP-19); C28's
  adoption makes the cert constraint ACTIVE at frontier instances, so
  the choice becomes material exactly when [P-CERTKS] lands. Honest
  outcome shape: converge the POLICY + pins now, measure at the first
  cert/margin-active rung (F2) — not before.
- **W4 structure exploitation (emergent option, named per §0-bis(a)(5))**:
  the KS aggregate has ANALYTIC Hessian structure — for
  KS_rho(r(W)) with softmax weights w_i:
  H_KS = sum_i w_i H_{r_i} + rho (sum_i w_i g_i g_i^T
  - (sum_i w_i g_i)(sum_i w_i g_i)^T), g_i = grad r_i —
  i.e. a Gauss-Newton-like rho-term computable EXACTLY from
  already-priced per-lane gradients plus a residual sum needing the
  per-lane curvature. A "KS-structured constraint Hessian" (exact
  rho-term + FD or omitted residual term) is a REAL alternative the
  ledger does not list. It is censused and adjudicated below; if it
  survives, it rides the same F2 duty as a protocol arm.
- **WIN RULE**: the option that delivers segment-frozen, measured (or
  exact-structured) constraint curvature with a rejector, at cost
  subordinate to the record, wins the policy half; scipy default BFGS
  survives only if the census shows identity-seeded per-segment BFGS
  is SOTA-defensible for few-iterate segments (it is not expected
  to — burden on the incumbent, which here is an UNDECLARED default,
  not a decided policy).

### 1.4 Per-row §0-bis AXIS BEARING (§0-ter(f), one sentence each)

- **Axis (1) optimizer query-level choice**: C31-IP IS this axis
  (fully adjudicated below); for C32/C33 it bears only through what
  Hessian interface the chosen engine accepts (scipy trust-constr
  accepts callable hess/HessianUpdateStrategy — both policies
  representable), closed by that stated reason.
- **Axis (2) discrete-vs-continuous adjoint + consistency**: bears on
  ALL THREE rows as the SOURCE of every gradient/HVP the engine and
  both curvature policies consume — [AMENDED-AT-RECONCILE, reason:
  the killed panel wrote "the choice itself has NO ledger row (grep
  verified this window)", which was true at its mtime and is FALSE
  now] the axis NOW HAS a ledger home: row C56 minted at the C9/C11
  landing (choice_ledger.yaml:731-740), weight+indicator roles
  closed, GRADIENT role owed to this cluster — consumed in §3.1-bis;
  no candidate row is proposed for this axis (dedup: C56 owns it).
- **Axis (3) moving-mesh / r-adaptive**: does NOT bear on C31/C32/C33
  operationally — the march mesh law is C9, adjudicated wave-1
  (uniform-per-run interim, AC2 column-insertion h-type primitive
  gated on F9a/F9b with the frozen-topology attribution test; the C9
  supplement closed the moving-mesh FAMILY at census grade and folded
  the r-arm — ledger :228); the only contact is F9b's
  gradient-consistency contract, which this cluster inherits as a
  constraint on ANY engine/curvature choice (O3.1 identity at the
  same derived floor on adapted meshes); no candidate row minted —
  C9 owns it.
- **Axis (4) adjoint-free routes**: bears on C31 as the
  quarantined-explorer tier (4/4 blind trees; adjudicated below at
  its modern best per §0-ter(d)); does not bear on C32/C33 (both
  presuppose the gradient/adjoint stack).
- **Axis (5) emergent sub-aspects**: three named — (i) KS-structured
  constraint Hessian (C33 W4, adjudicated here); (ii) interior-point
  warm-start-across-segments literature (C31, censused: it is the
  measured half of [P-IPADJ]'s A/B); (iii) engine-native MPCC/
  nonsmooth handling as the C28 F-2 fallback bundle (named,
  dedup: ledger C-row "TR-SQP-with-P4-gate vs nonsmooth/MPCC
  handling" seeded S24 belongs to C28's orbit — cite, don't re-mint).

### 1.5 Materiality estimates (§0-ter(c), frozen)

- **C31-IP**: MATERIAL at frontier instances (engine semantics decide
  whether outcome-II is representable and what res.v MEANS — the S24
  step-13d incident is of record); IMMATERIAL on mild equality-only
  walks (S18 path unchanged, bit-comparable claim scoped by RC28-1).
  Depth spent accordingly: full adjudication of the representation +
  primary-candidate order; flip = F2 measurement.
- **C32**: MATERIAL in measured cost (T2 FIRED on this decomposition;
  the dominant driver cost of record), IMMATERIAL in certified
  outcomes BY CONSTRUCTION (the A/B guard demands identical certified
  verdicts — any divergence is a protocol red, C27-guard pattern).
  Depth: protocol + falsifier pins; the measured half is the decision.
- **C33**: IMMATERIAL on every recorded instance (margin inactive,
  zero recorded effect — declared boundary of record); MATERIAL by
  arithmetic at the first cert-active rung (rho/4 ~ 1.44e4 at
  rho = 5.75e4 vs measured H scale — GAP-19). Depth: policy decided
  on consistency/cost grounds now (cheap, anti-over-engineering valve
  used honestly in BOTH directions: deciding it now is the CHEAP arm,
  building it is gated on the activity trigger).

---

## 2. SOTA CENSUS (dated 2026-08-19, this reconcile window)

### 2.0 Query protocol table (§0-ter(a))

Instrument: WebSearch (general US web index), surfacing arXiv,
Springer (Math. Programming / MPC / JOTA), SIAM (SIOPT), ScienceDirect,
AIAA ARC, Optimization Online, scipy.org documentation, GitHub,
Artelys/Knitro documentation, Semantic Scholar / ResearchGate records.
Russian classical school: DECLARED NOT-BEARING for this cluster's
territory (NLP engine internals / quasi-Newton policy are modern
numerical-optimization objects; the classical Russian contact —
Sternin 1961 / Shmyglevskii 1962 inequality-at-inadmissibility
structure — is C28/M0 territory, owned there via cava C30, cited in
§2.4). Counts = links returned / included in §2.1-2.3 one-liners.

| # | Query (VERBATIM) | Hits | Incl. |
|---|---|---|---|
| Q1 | interior point method warm start difficulty sequential NLP active-set SQP comparison | 8 | 4 |
| Q2 | Uno solver Vanaret Leyffer unified SQP interior-point framework 2024 nonlinear optimization | 10 | 5 |
| Q3 | MPCC B-stationarity active-set identification SQP multiplier estimates finite tolerance barrier smearing | 10 | 5 |
| Q4 | SR1 quasi-Newton trust region expensive function evaluations finite difference Hessian comparison accepted iterates | 10 | 3 |
| Q5 | forward-over-reverse Hessian-vector product cost gradient equivalents truncated Newton CG adjoint PDE optimization | 8 | 3 |
| Q6 | Kreisselmeier-Steinhauser aggregation second derivative Hessian Gauss-Newton structure constraint aggregation adjoint | 8 | 3 |
| Q7 | scipy trust-constr NonlinearConstraint hess BFGS default exact constraint Hessian practice | 8 | 3 |
| Q8 | discrete versus continuous adjoint gradient accuracy shape optimization exact derivative of discrete objective converged optimum | 9 | 4 |
| Q9 | derivative-free optimization expensive simulations 2024 2025 review CMA-ES Bayesian MADS convergence Clarke stationarity constrained | 9 | 3 |
| Q10 | proximal bundle method piecewise smooth nonconvex optimization 2024 2025 survey convergence | 9 | 3 |

CORPUS RECENCY: span 1979-2026. Newest items: arXiv:2604.18192
(SQP with complementarity constraints, local convergence, Apr 2026),
arXiv:2604.18726 (CCOpt open-source MPCC solver, 2026),
arXiv:2601.14680 (accelerated prox-level, piecewise-smooth, 2026),
Vanaret-Leyffer Uno paper in Math. Programming Computation
(s12532-026-00310-9, 2026), arXiv:2602.16005 (ODYN, 2026). Every
row's census axis reaches >= 2024; the canon layer (1979-2018) is
cited as canon, not as modernity. All web-layer entries are
[ABS]/[TITLE] depth (search-result snippets + abstracts); no claim
below exceeds that depth — anything needing full text is a
PROCUREMENT ASK. In-repo sources are [FULL].

### 2.1 C31-IP census (engine at boundary-active optima)

- [ABS] **Warm-start asymmetry (Q1)**: multiple independent sources
  (incl. "On Warm Starts for Interior Methods", Gould et al. lineage;
  a 2022 SQP-for-SOCP paper arXiv:2207.03082 whose selling point is
  warm-startability vs IP; MPC-solver literature) state the same two
  facts: (i) IP methods are "notoriously difficult to warm-start"
  (perturbed starts far from centrality, blocked directions,
  ill-conditioning); (ii) active-set SQP warm-starts naturally on
  sequences of closely related problems. Industrial confirmation
  [ABS]: Artelys Knitro manual recommends Active Set "when warm
  starting ... solving a sequence of closely related problems". This
  is exactly the RK-G segment structure (19-21 related solves) — W3
  is a REAL discriminating axis, not panel invention.
- [ABS] **Final-precision asymmetry (Q1)**: active-set SQP can close
  to higher precision; IP terminates at a small nonzero barrier value
  (typically 1e-6..1e-8) below which the linear systems are
  ill-conditioned — bears on W1 (what residual the certificate can
  claim) and matches the of-record res.v INFORMATION-ONLY incident.
- [ABS] **Uno (Q2)**: Vanaret-Leyffer, arXiv:2406.13454, now
  published Math. Programming Computation 2026 (s12532-026-00310-9);
  open C++ solver decomposing Lagrange-Newton methods into
  building blocks; presets stated to reproduce filterSQP and IPOPT.
  Companion: "A unified funnel restoration SQP algorithm", Math.
  Programming 2025 (s10107-025-02284-3). MODERN BEST of the
  SQP-class alternative family: ONE engine giving both semantics for
  a future A/B. Binary dependency => W5: F2-named, install =
  O5-class decision.
- [ABS] **MPCC/B-stationarity engines (Q3)**: active 2025-2026 line —
  arXiv:2501.13835 (globally convergent B-stationary MPEC method,
  2025), arXiv:2604.18192 (SQPCC local convergence + active-set
  identification after finitely many iterations, 2026),
  arXiv:2604.18726 (CCOpt solver, 2026), Fletcher-Leyffer-Ralph-
  Scholtes (SQP for MPECs, canon). Relevant ONLY if C28's F-1 fires
  (stratum contract violated => the ratio field must be treated as
  genuinely nonsmooth); until then the problem is smooth-NLP-within-
  stratum by construction. Cited as the C28 F-2 fallback bundle's
  modern layer — C28's orbit, not re-minted here.
- [ABS] **Bundle methods (Q10)**: alive and modern (SIOPT optimal
  rates 21m1428601; nonconvex constrained variants 2024 Wiley;
  accelerated prox-level for piecewise-smooth arXiv:2601.14680,
  2026). Steelman honored: the modern bundle line handles nonconvex
  constrained piecewise-smooth problems with convergence to
  approximate stationarity. Closed as PRIMARY by stated reason in
  §3.1 (fallback role kept).
- [ABS] **Adjoint-free at its best (Q9)**: "Direct-search methods in
  the year 2025" (arXiv:2403.05322) — Clarke-stationarity guarantees,
  explicit scaling limits; model-based DFO for convex constraints
  (SIOPT 21M1460971); CMA-ES dominant in ill-conditioned continuous
  landscapes; BO dominant for expensive moderate-dim global search.
  All certificate-blind (statistical or pattern guarantees, not
  KKT/B-residuals on the certified objective). Quarantine adjudicated
  in §3.1 at this modern best, per §0-ter(d).
- [FULL, in-repo] scipy method-switch + callback + state semantics:
  kickoff :346-366 (read-the-source findings (1)-(4)); facet Probe C
  :36-39; facet G3 whole block :181-234 (cold-restart mechanism,
  res.v incident, minimum bar for [P-IPADJ]).

### 2.2 C32 census (curvature policy)

- [ABS] **SR1/TR canon (Q4)**: SR1 is the TR-native update
  (indefiniteness tolerated — matches a maximization with saddle
  structure); "when SR1 and BFGS are both available, SR1 is typically
  more efficient" and "can give substantially better estimates of the
  Hessian" (survey-level). Modern refinements are mostly L-SR1 /
  stochastic lines for ML (OpenReview L-SR1; MDPI 2023; arXiv:
  2205.09121) — LARGE-SCALE machinery, immaterial at n~10 dense (W4
  valve). Nothing found that overturns "carry must be measured, not
  asserted": the A/B remains the decision instrument.
- [ABS] **HVP truncated Newton in design loops (Q5)**: the route is a
  real modern aero line — "Truncated-Newton Method with Adjoint-based
  Hessian-vector Product for Aerodynamic Shape Optimization"
  (AIAA 2020-1293) + meteorology/FWI second-order-adjoint TN canon.
  Confirms the tree option at its genuine best; on THIS stack it is
  N5-gated (custom_jvp build) — the census does not move the route
  fact (W4).
- [FULL, in-repo] Determinism-of-carry argument: facet G4:254-261
  (accepted-pair-only quasi-Newton = deterministic pure function of
  walk history; flipped columns localize invalidation — Dennis-Walker
  structured-secant lineage named there). Stale-symptom trigger
  :268-271. T2 FIRED decomposition :245-252.
- [ABS] **Inexactness-aware TR acceptance** (V-F30's error-aware
  frame): the adaptive-accuracy family was censused and CLOSED at
  wave-1 (RC28-3: tolerance half is a certificate and cannot move;
  budget half measured non-binding) — cited, not re-opened; what
  survives for C32 is only the acceptance-rule guard in the A/B
  (identical certified outcomes).

### 2.3 C33 census (constraint curvature)

- [FULL, docs-level] **scipy practice (Q7)**: SciPy 1.18 docs — 
  NonlinearConstraint hess default = BFGS() (HessianUpdateStrategy);
  exact callable hess accepted; FD-for-both-jac-and-hess in the same
  constraint is disallowed. Confirms (i) the incumbent is the DOCS'
  CONVENIENCE DEFAULT, not a decided policy; (ii) both repair arms
  (FD-of-exact-gradient callable, KS-structured callable) are
  representable in the existing engine interface — no engine flip
  needed for the C33 repair. Of-record leg: kickoff finding (3)
  ("default = a FRESH BFGS() instance per minimize() call") +
  findings :1272-1280 (identity-seeded, re-learned every segment).
- [ABS] **KS curvature at large rho (Q6)**: known phenomenon —
  "numerical difficulties ... local curvatures of the aggregated
  constraint become extremely large and then ill-conditioned Hessian"
  (constraint-aggregation literature; adaptive-aggregation-with-IP
  strategies, ScienceDirect 2015; Poon-Martins 2007 lineage). NO
  published exact-KS-Hessian recipe surfaced at this read depth =>
  the W4 "KS-structured constraint Hessian" stays labeled
  PANEL-DERIVED ARITHMETIC (elementary differentiation of the KS
  softmax form, verifiable on the page in §1.3-W4), carried as a
  protocol ARM — never cited as literature import. Zero inflation.
- [FULL, in-repo] GAP-19 magnitude + owner recipe: findings
  :1272-1280 ("exact Lagrangian Hessian via ... the existing
  FD-of-exact-gradient recipe applied to gm, measured-per-segment-base
  and frozen within segment — the R-3 policy extended, not changed").

### 2.4 Axis (2) census — adjoint realization, GRADIENT role (C56 debt)

- [ABS] **Discrete-vs-continuous canon + modern line (Q8)**:
  Nadarajah-Jameson AIAA-2000-0667 + Stanford thesis (canon
  comparison); arXiv:1811.00068 (discrete adjoints via AD, "exact
  gradients of the discrete objective", multiphysics); stellarator
  line arXiv:2005.07633. The load-bearing census fact, stated at
  [ABS] and carried by TWO legs: "the gradient obtained from the
  continuous approach may not be a descent direction of the
  DISCRETIZED problem near a local minimum", while the discrete
  adjoint's error depends only on solve tolerances. Internal
  of-record leg (independent): O3.1 dot-product identity and
  [X-A1IM] per-cell certification are bound to the DISCRETE
  realization; the cross-lowering floor row (findings :328-336) is
  the measured validity contract of that realization.
- [FULL, in-repo] C11 supplement weight-role closure (ledger :250):
  discrete AD-adjoint weight of record; continuous/characteristic-
  native (Ancourt 2023 + Lozano-Ponsin 2025) = formulation frame +
  REFEREE only; dual consistency = P2 Lemma B par.4.5 SCHEMA with
  F11d as estimator-site execution. Consumed as the role-split
  template for the gradient role (§3.1-bis).

### 2.5 Dedup + cava (navigation-first; all greps measured this window)

- **Cava** (ADVISORY_litreview_confrontation_2026-08-13.md, RATIFIED):
  `grep -inE "C31|C32|C33|interior[- ]point|punto interno|SQP|quasi-Newton|SR1|Hessian|hessian|curvatur"`
  -> hits {1113-1121 block, 1241, 1244}. ALL are the cava's OWN
  numbering family (numbering collision with the choice ledger, same
  class as wave-1 RC28-7): cava-C31 = T7(c)/claim-16 cone form,
  cava-C32 = claim-16 sign falsifier, cava-C33 = M0 excluded-locus;
  D-46/D-49 riders. The stem set includes bilingual forms
  ("curvatur" covers "curvatura"; "punto interno" ran empty).
  VERDICT: the ratified cava contributes NO row adjudicating engine,
  curvature policy, or constraint curvature. Declared
  inspected-adjacent: cava-C31/D-46 (active-set regime declaration on
  T7(c) — touches multiplier SEMANTICS, owned by F-SERVICE+F2) and
  D-47 (dual-feasibility rejector on lambda_e) — contact named, not
  consumed.
- **Choice ledger**: rows of this cluster C31 :452-464, C32 :466-474,
  C33 :476-485 (verbatim re-read this window); C48 :643-651
  (one-lowering batching, DECIDED — cited as gradient-validity
  contract); C56 :731-740 (consumed); C34/C35 (TR floor/xtol) =
  adjacent driver-constant rows, named not decided here.
  `grep -n "explorer|multistart|CMA|Bayesian|derivative-free|DFO"`
  -> only :654 (C49's "capturing explorer" — a REPRESENTATION clause,
  different object) => the exploration-TIER choice has NO ledger home
  => candidate row proposed in §4.5 per §0-bis(d).
- **Findings registry**: territory rows all cited in §1/§3:
  :1236-1244 (ip-path), :1245-1253 (hessian-no-rejector), :1254-1262
  (jacobi-scaling — adjacent, its [P-DVREFRESH] owner rides the same
  F2 window; named), :1263-1271 (flip-segmentation — N6-owned,
  cite-not-touch), :1272-1280 (margin-constraint-no-hess), :328-336
  (cross-lowering-gradient-floor), :319-327 (vmap-hessian-adjoint-
  divergence, C48 orbit).
- **Literature registry**:
  `grep -n "Nocedal|Conn.*Gould|SR1|interior-point|IPOPT|Byrd"` -> 0
  hits => the numerical-optimization canon is ABSENT from the
  registry; a literature rider is proposed in §4.4 (WANTED tier,
  procurement discipline).
- **Claims registry**: `grep -n "optimizer|trust-constr|interior"` ->
  :1253 ([X-TOCV] engine claim naming TR-SQP via scipy trust-constr
  in the RK-G driver) + unrelated hits (:476 Hoffman multipliers,
  :659 Lemma-B, :771 G0 spike) => no prior adjudication claim of this
  cluster's questions. Absence claims above are bounded by these
  exact greps.

---

## 3. ADJUDICATION (per row: incumbent case, alternatives at their
## best, stated-reason outcomes)

### 3.1 Row C31-IP — optimizer engine

**Incumbent's genuine case** (represented, per §0.3): scipy
trust-constr is the field's reference open TR-SQP/TR-IP hybrid with
years of production hardening (kickoff :414-417); its eq-path was
§4bis-adjudicated at source with zero disqualifying magic tolerances
(:346-366); its callback/state contract natively supports RK-G
segmentation (finding (2)); it is IN-ENV (W5 = perfect score); the
IP path is open source and READABLE, so the missing adjudication
([P-IPADJ]) is feasible at §4bis grade; on mild equality-only walks
the engine's record is certified of record (S18 KKT 7.7e-2 <= derived
gtol). The incumbent's defect is not a measured failure — it is an
ADJUDICATION LAPSE (findings :1236-1244) plus two priced structural
symptoms: cold barrier restarts per segment (facet G3:200-203) and
barrier-estimate multiplier semantics (res.v incident, G3:192-196).

**Blind-tree advocacy** (cite-not-regenerate; verified at tree source
this window): 4/4 converge on TR-SQP-class as the certificate closer
and NONE recommends IP as the closer (diff :159-167). At source:
O-F16 = phaseA_tree_optimization.md:900-960 (certificate tier "must
expose active sets, multipliers, exact curvature"; IP option :904-907
explicitly downgraded — "barrier smears activity identification;
multiplier meaning for (ii) less crisp until mu->0 ramp done
carefully" — the blind tree derived W2 verbatim); O-F17 :964-992
(TR-filter SQP; radius constants derived from the measured
rho-histogram :982-987); H-F36 = phaseA_tree_hyperbolic.md:1106-1140
(recommendation (a) "trust-region SQP, exact penalties for the few
nonsmooth constraint aggregates" :1135-1137; DFO (d)/(e) quarantined
:1117-1123); V-F30 = phaseA_tree_variational.md:1311-1342 (O1
reduced-space TR-SQP with error-aware acceptance; NUANCE of record:
"switching to O3 [IPOPT-class] when the active inequality set is
large" :1336-1339 — the one tree that conditionally admits IP, at a
regime our n~10 problem with 1-2 active rows does NOT occupy);
P-F27 = phaseA_tree_propulsion.md:989-1031 (O1 "SQP/interior-point"
bundled as one certificate-grade class :993-996; closer = O2/O1).
Honest reading: the 4/4 is TR-SQP-CLASS convergence; one tree
(V-F30) leaves IP a conditional niche; none prices the W5 env
asymmetry (blind trees owe no env) — the burden framing "incumbent
actively challenged" stands, softened from "4/4 reject IP" to "4/4
prefer SQP-class, 0/4 recommend IP as closer".

**Alternatives, each at its best, stated-reason dispositions:**
1. **tr_interior_point kept, adjudicated** (incumbent path): WINS
   W5+W1-feasibility today; W2/W3 carry priced defects; CANNOT be
   certified without [P-IPADJ]. => GATED (the WIN RULE's incumbent
   branch): [P-IPADJ] §4bis-grade source adjudication (barrier update
   law, what `optimality` measures on the IP path, status semantics,
   res.v sign/order, implementation warm-start capability) + measured
   barrier-restart overhead inside existing derived bands.
2. **Uno** (filterSQP/IPOPT presets, funnel restoration; 2024-2026):
   the MODERN BEST flip candidate — one open engine, both semantics,
   true-SQP inequality handling (no barrier to restart, W3) +
   active-set identification (W2). CLOSED-IN-WINDOW by W5 (new binary
   dep; install = O5-class session-boundary decision); NAMED PRIMARY
   FLIP CANDIDATE of record for the F2 A/B if the incumbent's gate
   fails. [ABS] depth; full-text ask in PAPERS NEEDED.
3. **IPOPT/cyipopt**: line-search interior point — same W2/W3 barrier
   class as the incumbent path PLUS a binary dep (W5) and weaker fit
   to RK-G radius semantics (kickoff :396-399 of record). CLOSED as
   flip candidate by stated reason (dominated by Uno's preset breadth
   for the A/B; it would re-buy the same barrier semantics being
   questioned).
4. **filterSQP / SLQP standalone** (Fletcher-Leyffer; Byrd-Gould-
   Nocedal-Waltz): the semantics the flip candidate needs, but no
   maintained open in-env implementation; CLOSED as separate
   adoptions — their content rides inside Uno's presets (stated
   reason: one dependency instead of three for the same A/B).
5. **SLSQP (in-env)**: the only other inequality-capable scipy
   engine. CLOSED by W1: line-search SQP with no trust-region
   semantics (RK-G excursion bound is non-negotiable, kickoff
   :414-415), no exposed multiplier/optimality state stream for
   certificate closure at accepted iterates.
6. **Knitro active-set/SQP**: industrial confirmation of the W3
   doctrine (its own manual recommends active-set for warm-started
   sequences) — CLOSED by W5 + closed-source (W1 source-adjudication
   impossible).
7. **Proximal-bundle** (D6:738; modern 2024-2026 lines censused
   §2.1): the honest fallback IF the smooth-per-stratum premise
   itself fails — i.e. C28's F-1 fires and the ratio field must be
   treated as genuinely nonsmooth. CLOSED as primary by stated
   reason: within a stratum the problem is smooth NLP by construction
   (traced, differentiable fields; the entire adjoint/certificate
   stack exists FOR that structure), and bundle methods consume only
   subgradients — discarding the exact curvature and multiplier
   structure the certificate needs. Fallback trigger NAMED (C28 F-1),
   riding C28's fallback bundle — cite, don't re-mint.
8. **MPCC-native engines** (SQPCC 2026, CCOpt 2026, B-stationary MPEC
   2025): same trigger as 7 but staying SQP-class; the modern layer
   exists and is cited; CLOSED here as C28-F-1-gated orbit (C28 owns
   the representation failure mode; this cluster owns only the engine
   consequence).
9. **ODYN / QP-class 2026 engines**: CLOSED — wrong problem class
   (QP, robotics/MPC target).
10. **Adjoint-free family as closer** (CMA-ES/BO/MADS at modern best,
    §2.1): CLOSED as certificate closer by stated reason —
    certificate-blind (no KKT/B-residual on the certified objective;
    guarantees are statistical or Clarke-pattern, and MADS — the one
    with Clarke theory — is gradient-starved at any dimension when
    gradients EXIST and are certified). 4/4 blind trees + census
    concur. Its LEGITIMATE role (exploration tier) has no ledger home
    => candidate row §4.5.

**Stated-reason outcome (per WIN RULE):** NO alternative can win the
formal half today (W5 blocks every out-of-env engine; SLSQP fails
W1), AND the incumbent cannot win it either (its gate — [P-IPADJ] +
in-band restart overhead — is exactly the unexecuted adjudication).
=> **measurement-gated SPLIT, converged on protocol + candidate
order**: (i) the engine of record REMAINS scipy trust-constr
tr_interior_point AS-IS, under the standing INFORMATION-ONLY
multiplier discipline, until [P-IPADJ] runs; (ii) [P-IPADJ] is the
FIRST F2 engine act (already on C28's critical path — VERDICT_wave1
§2.1); (iii) the A/B of record (matched constraint set, RC28-1
discipline): arm A = adjudicated tr_interior_point, arm B = Uno
filterSQP/funnel preset (install = O5-class decision AT the F2
session boundary, declared in advance); metrics = W2 (multiplier
crispness at the surrogate-active row vs its F-4 band; active-set
identification stability), W3 (restart churn; warm-start behavior),
W4 (eval counts), W1 (KKT/B-residual closure below the derived gtol
chain + [P-BSTAT] agreement); guard = identical certified outcomes
at the declared resolution (any divergence = protocol red); (iv)
engine flip only on the A/B verdict — trajectory-changing, never
in-window.

### 3.1-bis C56 GRADIENT ROLE — adjudicated here, explicitly

**This panel hereby CONSUMES the C56 gradient-role forecast owed by
the C9/C11 landing (ledger :739 "gradient role OWED TO wave-2
C31TRIO").** Question (from C56's choice text): which adjoint
realization is the GRADIENT of record for the marched stack —
discrete AD-adjoint (custom_vjp, one-lowering) vs separately
discretized continuous adjoint vs dual-consistent synthesis.

Adjudication (inside W1 — the engine's certificate closure is a
claim ON a gradient realization):
- **Discrete AD-adjoint (incumbent route fact) WINS the gradient
  role, adjudicated (no longer a route fact):** (1) the certificate
  the engine closes (KKT/B-residual, transversality O3) is defined on
  the DISCRETE certified objective; census [ABS] two-source +
  canon: a continuous-adjoint gradient near a local minimum "may not
  be a descent direction of the DISCRETIZED problem" — an engine
  closing a certificate on it would certify the wrong object; the
  discrete AD-adjoint is exact-to-solve-tolerance for the discrete J.
  (2) The verification infrastructure of record is realization-bound:
  O3.1 dot-product identity, [X-A1IM] per-cell certification, R-GRAD
  — all built FOR the discrete realization; C9's inherited F9b
  contract (O3.1 at the same derived floor on adapted meshes) is
  executable only there. (3) Blind advocacy: O-F21
  (phaseA_tree_optimization.md:1141-1183) option 1 + recommendation
  :1165-1167 — discrete adjoint as production, FD/complex-step as
  verification; the blind tree re-derived the role split. (4) Role
  consistency: the C11 supplement closed the WEIGHT role on the same
  realization (discrete weight, continuous line = referee); gradient
  and weight are the same object under one-lowering pinning — a split
  realization would break the F11d/O3.1 cross-checks.
- **Validity contract carried, not hidden:** the discrete realization
  is exact PER LOWERING — the cross-lowering floor (findings
  :328-336, ~1e-8 REL gradient variation across re-lowerings,
  amplified ~7 orders by FD consumers) and C48's B-shape clause are
  the CONTRACT under which "exact gradient" is claimed; every
  engine/curvature consumer in this cluster pins ONE lowering.
- **Continuous/characteristic-native line (Ancourt/Lozano-Ponsin) =
  referee + formulation frame for the gradient role too** (same
  split as the weight role): compatibility residuals usable as
  gradient cross-checks at band sites; NEVER the production gradient
  (a realization cannot referee itself — the C11 supplement's own
  clause, transferred).
- **Dual-consistent synthesis**: not a third production gradient —
  it is the CONSISTENCY CONDITION under which discrete and continuous
  agree in the limit; of record as P2 Lemma B par.4.5 SCHEMA with
  F11d as its estimator-site execution. A fired F11d re-opens C56
  (the row's own note), NOT C31 — carried verbatim.

**Proposed C56 delta (landing window applies):** owner field's
gradient-role clause "OWED TO wave-2 C31TRIO (forecast, not
consumed...)" -> "gradient role CLOSED-CONSUMED (PANEL_C31TRIO §3.1-bis,
2026-08-19 wave-2): discrete AD-adjoint = gradient realization of
record, adjudicated (census Q8 + O-F21 advocacy + O3.1/[X-A1IM]
binding + weight-role consistency); one-lowering/B-shape = validity
contract (C48, findings row engine:cross-lowering-gradient-floor);
continuous line = referee; dual-consistency residue unchanged (P2
Lemma B par.4.5 SCHEMA, F11d execution; fired F11d re-opens C56)."
Status MIXED -> all three roles closed => proposed
ADJUDICATED (2026-08-19, wave-1 weight/indicator + wave-2 gradient).

### 3.2 Row C32 — curvature policy

**Incumbent's genuine case:** fresh full FD-of-exact-gradient Hessian
per segment base is EXACT-to-FD-noise on the frozen stratum, needs no
carry-validity theory, is P2-literal (model rebuilt), and is the
policy under which every certified outcome of record was produced;
R-3 repaired the S18 plateau with exactly this policy. Its cost is
the measured dominant driver cost (T2 FIRED, facet :248-250) — the
incumbent loses only the COST axis, and only if a challenger matches
its certified outcomes.

**Blind-tree advocacy at source:** O-F17 :982-987 (CG-truncated
Newton with second-order adjoints in-flight) + O-F23 :1225-1246
(second-order-adjoint Lanczos with Kaniel-Paige brackets — the S*
certificate form); O-F21 item 6 :1162-1163 (fwd-over-rev, "cost ~ 2-4
gradient equivalents per product; needed by FORK-17/23"); V-F24 =
phaseA_tree_variational.md:1074-1105 (O1 Lanczos-on-HVP with DERIVED
tolerance "Lanczos residual + discretization error model" :1098-1100;
O3 directional second differences as independent cross-check — the
[P-HESSREJ] pattern blind-re-derived). The trees challenge the FRESH
FULL DENSE FD form, not the measured-curvature principle.

**Alternatives, stated-reason dispositions:**
1. **SR1-carry from certified accepted pairs** (ledger alternative):
   the live challenger. W1 PASS-by-construction is STATEABLE (facet
   G4:254-261: deterministic pure function of certified walk history;
   flip-localized invalidation via the structured-secant idea —
   Dennis-Walker lineage); W5 obligations named ([P-HESSREJ] +
   stale-symptom trigger). Census: SR1 = TR-native canon;
   modern large-scale variants immaterial at n~10. => GATED on
   [P-QNCARRY] A/B (protocol below) — never adopted by argument.
2. **HVP-truncated Newton (Steihaug-CG) in-flight**: real modern line
   (AIAA 2020-1293 [ABS]); BLOCKED AS WRITTEN on this stack (W4 route
   fact, custom_vjp only) — its true price INCLUDES the N5
   custom_jvp build (trajectory-changing, adjudication-only of
   record). => GATED SECOND: becomes primary only after N5 lands AND
   measured product cost < FD column cost on THIS stack (the 2-4
   gradient-equivalents is a tree number to MEASURE, cited not
   imported).
3. **L-SR1 / limited-memory / compact representations**: CLOSED —
   large-scale machinery at n~10 dense is the W4 materiality valve's
   textbook case (the full matrix is 10x10; memory is not a resource
   here).
4. **Stochastic quasi-Newton / ML lines** (Q4 hits): CLOSED — the
   objective is deterministic (fixed quadrature; RK-G replay);
   noise-model machinery answers a problem this stack does not have.
5. **ARC / cubic regularization** (O-F17 option 4): CLOSED as a
   separate adoption — same-class subproblem cost, and the TR radius
   constants are already the DERIVED kind (rho-histogram derivation,
   O-F17's own recommendation; C34's orbit for the floor) — switching
   regularizers buys no axis (the tree itself scored it "tie").
6. **Adaptive-accuracy/inexact TR family**: CLOSED at wave-1
   (RC28-3, both halves of K = K_phys ∩ K_budget) — cited, binding,
   not re-opened; only its acceptance-guard survives inside the A/B.

**S* certificate arm (W2, converged NOW, no measurement needed):**
the (iii) certificate at the returned base uses EXACT curvature —
Lanczos with certified Kaniel-Paige brackets on the tangent cone
(O-F23/V-F24 convergent, and V-F24's O3 cross-check = the
[P-HESSREJ] directional pattern). This does not touch the in-flight
policy (separation by structure, §1.2-W2) and no in-flight option
degrades it. Adopted as the certificate FORM at protocol level; its
build rides the same F2 window as [P-BSTAT] (both are properties of
the returned base).

**Stated-reason outcome (per WIN RULE):** **measurement-gated
SPLIT**: fresh-FD stays the INTERIM policy of record (incumbent
retained, zero verdicts move); SR1-carry = pinned challenger via
[P-QNCARRY]; HVP-TN = named second challenger, N5-gated;
[P-HESSREJ] = UNCONDITIONAL duty (ships regardless of winner — the
rejector hole is a standing findings row, not an option feature).
Protocol pins (the A/B of record): instance = the RECORDED S18 walk
replay (arms: A fresh-FD per segment; B SR1-carry from certified
accepted pairs + stale-symptom re-measure + [P-HESSREJ] armed);
guard = IDENTICAL certified outcomes at the declared resolution (any
divergence = protocol red, C27-guard pattern); metrics = total
gradient-eval count, segment count, acceptance rate, rejector trips;
determinism = two-run bit-compare of the carried matrix (W1
absolute). Falsifiers: **F-C32-1** carry degrades acceptance or
trips the rejector on either recorded instance => C32 CLOSES on
fresh-FD (converged, not re-gated); **F-C32-2** carry shows
eval-count reduction with identical certified outcomes and zero
trips on BOTH pre-registered instances (S18 mild + one frontier-class
walk) => carry promoted, fresh-FD demoted to the re-measure-on-
symptom role; **F-C32-3** carry bit-compare fails => carry REJECTED
outright (W1 is not tradeable); **F-C32-4** post-N5 measured HVP
product cost >= FD column equivalent on this stack => HVP-TN closed
by measurement.

### 3.3 Row C33 — constraint curvature

**Incumbent's genuine case (steelman of a default):** identity-seeded
BFGS per segment is free of extra evaluations, is what the reference
engine ships, and has ZERO recorded adverse effect — because the
margin has been INACTIVE at every recorded instance (declared
boundary of record). Its case is entirely the anti-over-engineering
valve. The census (§2.3) shows it is the docs' convenience default —
no source defends identity-seeded per-call BFGS as a POLICY for
few-iterate segments with known-steep constraint curvature; the
burden set in §1.3 is unmet.

**Blind-tree advocacy:** C33 diff block :174-175 — same HVP family,
O-F21 item 6 (the trees treat constraint and objective curvature as
one Lagrangian object; the asymmetry is OUR artifact).

**Alternatives, stated-reason dispositions:**
1. **FD-of-exact-constraint-gradient per segment base, frozen within
   segment** (the R-3 policy extended — findings :1279 owner recipe):
   ADOPTED as the DEFAULT ARM of the policy. W1 symmetry restored;
   W2 executable today (gm is one VJP per eval — cheap vs record);
   representable in the existing engine interface (hess= callable,
   §2.3) — no engine dependency.
2. **KS-structured constraint Hessian** (W4 emergent option,
   panel-derived arithmetic): exact rho-term from already-priced
   per-lane gradients (C27's vector rows) + FD-or-omitted residual
   term; at rho large the rho-term dominates (the same rho/4
   arithmetic that makes the row material). ADOPTED as PROTOCOL ARM
   (second arm of the same A/B): if the residual term is omitted, the
   omission ships with a derived band + its own rejector (rho-term vs
   FD-of-gm difference must sit inside the band). Labeled
   panel-derived; no literature import claimed (census found the
   ill-conditioning phenomenon, not the recipe).
3. **Exact HVP fwd-over-rev on the constraint block**: CLOSED AS
   WRITTEN (W2 route fact, custom_vjp only); re-enters ONLY behind
   N5's custom_jvp exactly like C32's second challenger — one route
   decision, cited once.
4. **Identity-seeded per-segment BFGS kept as decided policy**:
   SUPERSEDED AS POLICY by stated reason (W1: undeclared default
   re-creating the measured S18 plateau mechanism class on the
   constraint side; census confirms convenience-default status). It
   REMAINS the de-facto path until the activity trigger fires —
   honestly, because building before the trigger is the
   over-engineering arm (§1.5).
5. **No-hess / skip variants**: CLOSED — same undeclared-default
   class with strictly less information.

**Stated-reason outcome (per WIN RULE):** **CONVERGED-ON-POLICY +
measurement-gated adoption**: the policy of record = constraint
curvature MEASURED at segment base and frozen within segment
(policy symmetry with R-3), two representable arms (FD-of-gm default;
KS-structured protocol arm); the BUILD is GATED on the activity
trigger of the findings row (:1280 — "first margin-active rung of
record, or an argmin-lane swap mid-segment", extended by C28 to the
first cert-active rung); duty = **F2-C33-CONSTRHESS**, riding the
[P-CERTKS]/GAP-1 pilot window and the ledger's own [R2] hess= A/B
flag (owner alignment, no new window). Rejector obligation: the
[P-HESSREJ] pattern extended to the constraint block (symmetry-defect
+ directional Richardson on the KS row) — unconditional at build
time. Falsifiers: **F-C33-1** at the first active rung, the A/B
(default-BFGS vs measured-policy arms) shows NO plateau/churn
difference at matched cost => the policy verdict weakens to
cost-only and the row closes on simplicity (the incumbent's honest
comeback branch — pinned so the adjudication is falsifiable);
**F-C33-2** FD-of-gm cost exceeds its one-VJP-per-eval budget on the
real stack => cost premise false, re-price both arms; **F-C33-3**
KS-structured arm's omitted-residual band violated at any accepted
iterate => structured arm demoted to diagnostic (FD arm stands).

### 3.4 Cross-row consistency (cluster-internal)

One Lagrangian, one policy class: C32 (objective block) and C33
(constraint block) converge on the SAME policy statement — curvature
measured at segment base, frozen within segment, rejector-guarded —
so the Lagrangian Hessian the C31 engine consumes is uniformly
certificate-grade; the C33 activity trigger and the C32 A/B share
the [P-HESSREJ] instrument (built once). The engine A/B (C31) and
the curvature A/Bs are ORDERED: [P-IPADJ] first (it decides what
res.v/optimality MEAN — without it neither A/B can interpret its
own multiplier metrics), then [P-QNCARRY] on the adjudicated engine,
then F2-C33-CONSTRHESS at its activity trigger. Every multiplier
reported anywhere in this cluster carries the B-STATIONARITY
QUALIFIER until O1 is discharged (wave-1 cross-cluster rule,
VERDICT_wave1 §3 — inherited verbatim). K_RICH appears in this
cluster only through C27/C28-derived constants (rho) — flagged to
the C42 wave-3 audit by those rows already; this cluster adds NO new
K_RICH role.

---

## 4. PROPOSED VERDICTS + DUTIES (proposals only; ledger edits happen
## at the landing window)

### 4.1 C31 (docs/choice_ledger.yaml:452-464)
- status: MIXED -> "ADJUDICATED-SPLIT (engine protocol + candidate
  order converged 2026-08-19 wave-2; incumbent-IP certification vs
  flip gated on [P-IPADJ] + F2 A/B)"
- note appends: "Wave-2 verdict (PANEL_C31TRIO.md §3.1): engine of
  record remains scipy trust-constr tr_interior_point AS-IS under the
  standing INFORMATION-ONLY multiplier discipline until [P-IPADJ]
  (§4bis-grade source adjudication: barrier law, optimality
  semantics, status meanings, res.v sign/order, warm-start
  capability) — first F2 engine act, already on C28's critical path.
  Flip candidate of record = Uno (filterSQP/funnel preset;
  arXiv:2406.13454, MPC 2026), install = O5-class session-boundary
  decision; IPOPT closed (same barrier class + dep), SLSQP closed
  (no TR semantics/state), filterSQP/SLQP standalone closed (ride
  Uno presets), Knitro closed (W5+closed-source), bundle/MPCC-native
  = C28-F-1-gated fallback orbit, adjoint-free closed as closer
  (quarantine 4/4 + census 2025). A/B protocol pinned (matched
  constraint set per RC28-1; W1-W4 metrics; identical-certified-
  outcomes guard). Falsifiers F-C31-1/2/3 (see panel §4.3). Census
  1979-2026, newest 2026. GRADIENT-ROLE RIDER: C56's owed gradient
  role CONSUMED — discrete AD-adjoint adjudicated the gradient
  realization of record (§3.1-bis), one-lowering contract (C48)."
- owner: F2 [P-IPADJ] unchanged; adds F2-C31-ENGINE-AB (the A/B).

### 4.2 C32 (docs/choice_ledger.yaml:466-474)
- status: SINGLE-AUTHOR -> "ADJUDICATED-SPLIT (policy structure
  converged 2026-08-19 wave-2; carry-vs-fresh = measured F2 duty)"
- note appends: "Wave-2 verdict (PANEL_C31TRIO.md §3.2): fresh-FD =
  interim policy of record (incumbent retained, its genuine case
  represented); SR1-carry = pinned challenger ([P-QNCARRY] A/B on the
  recorded S18 walk + one frontier-class walk: identical-certified-
  outcomes guard, eval/segment/acceptance metrics, two-run
  bit-compare, [P-HESSREJ] armed); HVP-truncated-Newton = second
  challenger GATED on N5 custom_jvp + measured product cost (2-4
  grad-equivalents = tree number to MEASURE); L-SR1/stochastic/ARC/
  inexact-TR closed by stated reason (RC28-3 binding for the last).
  S* certificate form converged NOW: Lanczos + Kaniel-Paige brackets
  + directional cross-check (O-F23/V-F24), rides the [P-BSTAT]
  window. [P-HESSREJ] = UNCONDITIONAL duty. Falsifiers
  F-C32-1..4 (panel §3.2)."
- owner: G0/T2 review unchanged; F2 entry gains [P-QNCARRY] +
  [P-HESSREJ] (unconditional).

### 4.3 C33 (docs/choice_ledger.yaml:476-485)
- status: NEVER -> "ADJUDICATED-SPLIT (policy converged 2026-08-19
  wave-2; build gated on the activity trigger)"
- note appends: "Wave-2 verdict (PANEL_C31TRIO.md §3.3): policy of
  record = constraint curvature measured at segment base, frozen
  within segment (R-3 extended — policy symmetry); default arm =
  FD-of-exact-gradient on gm (one VJP); protocol arm = KS-structured
  Hessian (exact rho-term from priced per-lane gradients + banded
  residual; PANEL-DERIVED arithmetic, no literature import claimed);
  identity-seeded per-segment BFGS SUPERSEDED as policy (undeclared
  convenience default, census-confirmed; stays de-facto until
  trigger); exact fwd-over-rev closed-as-written (N5-gated, same
  route decision as C32). Duty F2-C33-CONSTRHESS rides the
  [P-CERTKS]/GAP-1 pilot window + the row's own [R2] hess= flag;
  [P-HESSREJ] pattern extended to the constraint block. Trigger
  unchanged (findings :1280 + first cert-active rung per C28).
  Falsifiers F-C33-1/2/3 incl. the incumbent's honest comeback
  branch."
- owner: "F2 (R2 pilot flag)" -> "F2 duty F2-C33-CONSTRHESS (rides
  [R2] + GAP-1 pilot window)".

### 4.4 C56 (docs/choice_ledger.yaml:731-740) — debt consumption
- owner field gradient-role clause -> CLOSED-CONSUMED per §3.1-bis
  (exact delta text there); status MIXED -> ADJUDICATED (all three
  roles closed; dual-consistency residue and F11d re-open semantics
  UNCHANGED — carried verbatim from the row's note).
- Literature rider (rides the landing, WANTED tier per procurement
  discipline; grep-proven absent §2.5): Vanaret-Leyffer 2024/2026
  (Uno, arXiv:2406.13454 + MPC s12532-026-00310-9); Byrd-Hribar-
  Nocedal 1999 (trust-constr IP lineage — the [P-IPADJ] source
  companion); Nocedal-Wright 2e (§6 SR1, §8.1 FD error model — the
  [P-HESSREJ]/carry derivation source); Conn-Gould-Toint Trust-Region
  Methods (§11 nonsmooth — [P-BSTAT] companion); Nadarajah-Jameson
  AIAA-2000-0667 (discrete-vs-continuous canon — C56 evidence leg).
  MPCC/bundle modern items (2501.13835, 2604.18192, 2604.18726)
  accompany F2 ONLY IF the C28-F-1 fallback fires (deferral kept —
  same pattern as wave-1 C28's KS/MPCC rider deferral).

### 4.5 CANDIDATE ROW (per §0-bis(d); dedup-proven §2.5; landing
### window decides whether to mint)
- choice: "Global exploration tier for the certified design loop:
  none/implicit multistart-from-seeds (incumbent de-facto) vs
  quarantined DFO explorer (CMA-ES / BO / MADS at explorer fidelity,
  outputs re-certified, never verdict-bearing) vs deferred-until-
  multimodality-demonstrated"
- advocacy: 4/4 blind trees assign DFO an explorer tier that the
  program has never designed or rejected (O-F16 options 5-8, H-F36
  (d)/(e), P-F27 O3/O4/O7, V-F30 O5); census modern best =
  arXiv:2403.05322 + model-based-DFO SIOPT line. Dedup: ledger grep
  (§2.5) -> no row; C49's "capturing explorer" is a representation
  clause, different object. NOT this cluster's question (C31 is the
  CLOSER); handed up unminted.

### 4.6 Machine-check note
alternatives_closed counting rule (RC27-8(vi) lesson): an option
counts when it receives a stated-reason non-adoption disposition in
§3 (closed now, or closed-as-default with named re-entry trigger);
adopted arms and gated challengers do not count. Count: C31 = 9
(IPOPT, filterSQP-standalone, SLQP-standalone, Knitro, SLSQP,
ODYN/QP-class, MPCC-native-here, bundle-as-primary,
adjoint-free-as-closer), C32 = 4 (L-SR1/limited-memory,
stochastic-QN, ARC, inexact-TR-family[wave-1-bound]), C33 = 3
(exact-HVP-as-written, default-BFGS-as-policy, no-hess variants)
=> **16**.

---

## PAPERS NEEDED (procurement channel §0-bis(c))

1. **Vanaret C., Leyffer S., "Implementing a unified solver for
   nonlinearly constrained optimization", Math. Programming
   Computation (2026), doi 10.1007/s12532-026-00310-9 (preprint
   arXiv:2406.13454)** — why: the named flip candidate's preset
   fidelity ("reproduces filterSQP and IPOPT") is asserted at [ABS];
   the F2 A/B design (arm B spec) needs the building-block/preset
   detail at full text BEFORE the O5-class install decision. Claim
   waiting: arm-B preset spec of F2-C31-ENGINE-AB.
2. **Nocedal J., Wright S., "Numerical Optimization" 2e, §6.2 (SR1)
   + §8.1 (FD error model)** — why: [P-HESSREJ]'s symmetry-defect
   band and [P-QNCARRY]'s carry conditions must be DERIVED from the
   stated error model, not asserted (R5); the facet cites the model
   by name without the constant forms. Claim waiting: the derived
   band constants of [P-HESSREJ] (both C32 and C33 legs).
3. **Byrd R., Hribar M.E., Nocedal J., "An interior point algorithm
   for large-scale nonlinear programming", SIOPT 9(4), 1999** — why:
   tr_interior_point's algorithmic parent; [P-IPADJ]'s source
   adjudication of the barrier update law and multiplier semantics
   should be checked against the published algorithm, not only the
   scipy implementation. Claim waiting: [P-IPADJ] item "what
   `optimality` measures on the IP path".

(MPCC/bundle full texts deliberately NOT asked now — they enter only
behind the C28-F-1 trigger; asking would be procurement inflation.)

---

## 5. MACHINE SUMMARY

```json
{
  "cluster": "C31TRIO",
  "rows": {
    "C31": {"proposed": "ADJUDICATED-SPLIT: engine stays scipy tr_interior_point AS-IS under INFORMATION-ONLY multiplier discipline until [P-IPADJ] (first F2 engine act, C28 critical path); flip candidate of record = Uno filterSQP/funnel preset (install = O5-class boundary decision); A/B pinned (matched constraint set per RC28-1, W1-W4 metrics, identical-certified-outcomes guard); 9 alternatives closed by stated reason; C56 gradient role consumed in-cluster", "gated": true, "duty": "[P-IPADJ] + F2-C31-ENGINE-AB"},
    "C32": {"proposed": "ADJUDICATED-SPLIT: fresh-FD = interim policy of record; SR1-carry = pinned challenger via [P-QNCARRY] A/B (identical-certified-outcomes guard, bit-compare determinism, rejector armed); HVP-TN second challenger N5-gated; S* certificate form (Lanczos + Kaniel-Paige + directional cross-check) converged now; [P-HESSREJ] unconditional", "gated": true, "duty": "[P-QNCARRY] + [P-HESSREJ] (unconditional)"},
    "C33": {"proposed": "CONVERGED-ON-POLICY + gated adoption: constraint curvature measured at segment base, frozen within segment (R-3 extended, policy symmetry); default arm FD-of-gm, protocol arm KS-structured (panel-derived, banded); identity-seeded BFGS superseded as policy, stays de-facto until activity trigger; build at first cert/margin-active rung", "gated": true, "duty": "F2-C33-CONSTRHESS (rides [R2] + GAP-1 pilot window)"},
    "C56-gradient-role": {"proposed": "CLOSED-CONSUMED (owed forecast executed): discrete AD-adjoint = gradient realization of record (census Q8 + O-F21 + O3.1/[X-A1IM] binding + weight-role consistency); one-lowering/B-shape validity contract; continuous line = referee; F11d re-opens C56 not C31", "gated": false, "duty": null}
  },
  "census_recency": "1979-2026; newest 2026 (arXiv:2604.18192, arXiv:2604.18726, arXiv:2601.14680, Uno MPC 2026); every axis >= 2024; web layer [ABS]/[TITLE], claims bounded",
  "alternatives_closed": 16,
  "inflation_check": "done"
}
```

---

## RECONCILIATION DECLARATION (per BRIEF_wave2_reconcile.md)

**What was on disk at read time** (mtime ~12:55-13:05, quota kill #5):
header + write-order declaration + §1 COMPLETE (§1.0-§1.5, ending at
the "---" separator, 264 lines). §2 (census), §3 (adjudication),
§4 (verdicts/duties), §5 (machine summary) and PAPERS NEEDED were
entirely ABSENT. No web query trail existed on disk.

**What verified clean (kept verbatim):** every §1 citation was
re-read at source in THIS window and verified: facet
s24_gap_driver-nonsmooth.md :4-21/:36-39/:192-196/:200-203/:245-252/
:248-250/:254-261/:268-271 (all quotes/numbers match); kickoff
:346-366/:404-413; a1_ideal_march_jax.py:504-517 (custom_vjp+defvjp
only); ADVISORY_S25bis_diff_convergence_2026-08-12.md:119 (B-F11);
findings rows :1236-1244/:1245-1253/:1272-1280/:328-336; ledger rows
C31 :452-464 / C32 :466-474 / C33 :476-485 (incl. the speed-audit
"OUT by policy"/N5 note text, re-verified at
ADVISORY_engine_speed_audit_2026-08-12.md:442 and :598-602);
VERDICT_wave1 §2.1/§2.2 consumption sentences; diff :159-175; the
KS-Hessian formula in §1.3-W4 (re-derived by hand this window:
softmax differentiation gives exactly the stated rho-term — correct);
GAP-19 arithmetic (rho/4 = 1.4375e4 at rho = 5.75e4 — matches
"~1.44e4"). The frozen questions, criteria, win rules, axis bearings
and materiality estimates are KEPT AS FOUND.

**What was repaired (each declared):**
- R1 (path precision): the partial cited the facet as bare
  "s24_gap_driver-nonsmooth.md"; the file lives at
  validation/sota_gapmap_raws_2026-08-12/ (glob-verified; the
  BASE/facets/ path does NOT contain it). First citation normalized;
  content claims were correct.
- R2 (stale forward claim): the header's "CENSUS VALIDITY STAMP:
  searched 2026-08-19 (all queries this window)" described a census
  that did not exist on disk — a forward claim orphaned by the kill.
  Replaced with this window's actual stamp; the real query protocol
  is §2.0 (10 queries, run in THIS reconcile window).
- R3 (superseded absence claim): §1.4 axis (2) claimed "the choice
  itself has NO ledger row (grep verified this window)" — true at
  the partial's mtime, FALSE now: C56 was minted at the C9/C11
  landing. Corrected in place with [AMENDED-AT-RECONCILE] marker;
  the §0-bis(d) hand-up for axis (2) is replaced by C56 consumption.
- R4 (owed-debt integration): §1.0 and §1.1 gained
  [AMENDED-AT-RECONCILE] blocks consuming the now-landed C9/C11/C56
  ledger rows and addressing the C56 gradient-role forecast to this
  panel explicitly (BRIEF_wave2_reconcile.md order + the row's own
  owner text). The write-order declaration was extended to describe
  the two-window history honestly.

**What was added (all new content):** §2 complete census with §0-ter(a)
query protocol table (10 verbatim queries, counts, recency, read-depth
markers, Russian-school bearing statement), §2.5 dedup incl. the
cava numbering-collision declaration (bilingual stems) and the four
registry greps; §3 full adjudication (C31 with 10 dispositions and
the softened-and-sourced tree-advocacy reading; §3.1-bis C56
gradient-role consumption; C32 with 6 dispositions + S* certificate
arm; C33 with 5 dispositions incl. the incumbent's comeback
falsifier; §3.4 cross-row consistency with duty ordering); §4
proposed deltas (C31/C32/C33/C56 + literature rider + candidate row
+ counting rule); PAPERS NEEDED (3 asks, deferral declared); §5
machine summary. The on-disk partial's UNVERIFIED status is hereby
DISCHARGED for this rewritten file.
