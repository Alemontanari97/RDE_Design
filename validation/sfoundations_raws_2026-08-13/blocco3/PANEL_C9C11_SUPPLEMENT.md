# PANEL SUPPLEMENT — C9C11 directive-axis closure (wave 1)
# S-FOUNDATIONS-C2, Blocco 3, 2026-08-19. Census validity stamp: 2026-08-19.
# Brief of record: BASE/blocco3/BRIEF_wave1_C9C11_supplement.md (SUPPLEMENT AGENT).
# BASE = validation/sfoundations_raws_2026-08-13.
# Cause: the user directive of 2026-08-19 landed mid-wave-1; two named axes
# were not closed by PANEL_C9C11.md's census. This file closes them at census
# grade BEFORE the C9/C11 ledger deltas land. It does NOT re-open the wave-1
# verdict (VERDICT_wave1.md §2.3/§2.4): its outcome below is CONFIRM —
# both axes close consistently with the verdicts of record; zero conflicts.
# Verdict class: SUPPLEMENT PROPOSAL (ledger/registry edits happen at the
# landing window, not here; §4 carries exact proposed deltas).
# Protocol of record (BINDING, followed here): BRIEF_wave2_panels.md §0-bis
# (read-depth markers [FULL]/[ABS]/[TITLE], procurement channel, candidate
# rows) + §0-ter (query trail verbatim with counts, question-anchored
# pre-registered criteria, materiality both directions, steelman, dated
# census, per-row axis bearing).
# Env: pinned, untouched. GENO/: not read, not needed. No git commands run.

---

## 0. METHOD COMPLIANCE + DEDUP OF THIS WINDOW (navigation-first)

Read in full before any query: PANEL_C9C11.md §1/§2 (incl. §2.4)/§4;
VERDICT_wave1.md §0.1, §1.3, §2.3, §2.4, §3, §4.3-§4.7;
BRIEF_wave2_panels.md §0-bis + §0-ter. PANEL/VERDICT content is CITED by
section below, never re-derived.

Read-depth marker convention (§0-bis(b)) extended for in-repo holdings:
[FULL-R] = read-integral of record in this repo (registry row cited);
[PART-R] = READ-PARTIAL of record (page-verified summary cited);
[ABS] = abstract/snippet read this window; [TITLE] = existence only.
No claim below exceeds its marker.

Dedup greps run this window (verbatim, all on `docs/`):

- `grep -inE 'MMPDE|moving.mesh|r-adaptiv|equidistribution|monitor.function' docs/`
  → EXACTLY 2 hits: choice_ledger.yaml:226 (C9 note, the A36
  "log-weighted DWR equidistribution" phrase) and claims_registry.yaml:1294
  ([X-AKNO] "insertion at the residual-mass median station
  (equidistribution ...)"). Search-proven absence: the moving-mesh /
  r-adaptive canon (Huang-Russell, MMPDE, Budd, velocity-based, ML
  mesh-movement) has NO registry rows anywhere.
- `grep -inE 'Hicken|dual.consist|Hartmann|Zahr|HOIST|shock.tracking'
  docs/literature_registry.yaml` → only zahr_persson_2016 (:572-577, the
  periodicity-adjoint paper — not shock tracking, not dual consistency).
  Search-proven absence: the dual-consistency canon has no registry rows.
- `grep -in 'adjoint' docs/choice_ledger.yaml` → hits ONLY in C48's note
  (:649) and C49's text (:652/:655/:661). CONFIRMS §0-bis(a)(2)'s
  verification of record: NO ledger row adjudicates the
  discrete-vs-continuous adjoint realization (candidate row proposed in
  §4.3, per §0-bis(d) — proposal only, not minted).
- `grep -inE 'Thakur|Nadarajah|Huang|Budd|UM2N|Venditti|Fidkowski' docs/`
  → Venditti only as the C9 alternative label (choice_ledger.yaml:222);
  all 'Huang' hits are Li-Xu-Huang (propulsion corpus, unrelated); no
  moving-mesh or output-adaptation canon rows. Nothing re-minted below.
- Rows verified verbatim this window (SR-12): choice_ledger.yaml C9
  :217-226, C10 :228-236, C11 :238-248, C48 note :649 (the ONE-LOWERING
  discipline of record: "CORRECTED FORM (base in-batch, one lowering;
  lane-permutation control bitwise)"; defect root = "mixed-lowering
  formulation"), C49 :651-661 (fitted-front class of record; note names
  "adjoint front-motion term = the load-bearing argument, Giles-Pierce
  class"); claims_registry.yaml [X-A1IM] :809-821 ("every cell an
  implicit custom_vjp unit process (never unrolled); ... O3.1
  dot-product over the ENTIRE march"), [X-AKNO] :1290-1301 (f2 = -lambda2
  IS the adjoint variable, Prop. A3), PAP-P2LB :1480-1491 (falsifier =
  "the honesty clause (mesh limit stays SCHEMA) weakened anywhere");
  literature_registry.yaml giles_ulbrich_2010_part2 :114-120 ("the trap
  is a theorem", fixed-stencil discrete adjoint converges to a WRONG
  value across shocks), lozano_ponsin_2025 :122-128 (EXISTS, READ-PARTIAL,
  PDF on disk literature/aerospace-12-00494-v2 (1).pdf; summary: "adjoint
  compatibility Eqs. (30)/(31) = O3.3 bench rows (F-O33BENCH)"),
  ancourt_peter_atinault_2023 :199-208 (READ-INTEGRAL, two roots);
  docs/rde_nozzle_P2_lemmaB.md §4.3-§4.5 (:205-307) and §4.7 claim table
  :329-341; docs/rde_nozzle_P2_outline.md §5 :229-252 (S14 norm
  pre-registration: O3.3 oracle coordinates = L-P 2025 Eqs. (30)/(31)
  compatibility residuals + Prop. A3 f2 drift; S-LBML limit target
  includes the shock-foot adjoint condition and the characteristic-borne
  adjoint discontinuities of L-P 2025, "which the characteristic-ALIGNED
  fitted march can represent natively").

Other §0-bis axes, bearing on THIS supplement (§0-ter(f), one line each):
axis (1) optimizer query-level — does not bear (wave-2 C31TRIO scope);
axis (4) adjoint-free routes — does not bear (no C9/C11 alternative is
adjoint-free; wave-2 scope); axis (5) emergent sub-aspects — one emerged
and is closed in-line: the DWR ENRICHMENT-SPACE choice (§B.5 pin (iii)).

---

## A. AXIS A — MOVING-MESH / R-ADAPTIVE FAMILY vs THE C9 MESH LAW

### A.1 The single main question (question-anchored, frozen first)

Should the C9 mesh law ever MOVE existing resolution (redistribute nodes
at fixed count, the r-adaptive family) rather than only INSERT it (the
adopted refinement-only policy: A36 static arm + AC2 insertion primitive,
uniform interim — VERDICT §2.3), to lower J-error per unit-process under
the certificate discipline of record?

### A.2 Pre-registered decision criteria (frozen BEFORE the queries ran)

Derived from A.1 + the operational constraints of record (PANEL §1.2/§1.3),
declared before any search result was seen; no mid-census amendment was
needed:

- MOTION (r-family) ADOPTED only if ALL of: (i) census shows output-error
  gains at matched cost on marched/hyperbolic problems; (ii) motion
  respects the anti-motion facts of record (A36 clause (ii): IVL never
  moved → F9c); (iii) motion passes the H-F27(e) gradient-consistency
  contract (F9b); (iv) the marched characteristic structure leaves motion
  a genuine free dof not already consumed by the stack.
- REJECTED only if the family's transferable content is FULLY subsumed by
  record objects (fitted fronts + A36 equidistribution), leaving no
  material residual freedom.
- FOLDED as a named F2 arm if a genuine residual dof exists but has no
  census precedent on characteristic marching (build+measure, the
  campaign's expected shape), with its falsifier pinned.
- Tie-break at J-immateriality: cost/simplicity decides (§0-ter(c)).

### A.3 Query protocol table (§0-ter(a); engine = WebSearch, all run 2026-08-19)

| # | Query (verbatim) | Returned | Screened | Included |
|---|---|---|---|---|
| QA1 | "moving mesh method MMPDE equidistribution monitor function r-adaptivity review Huang Russell hyperbolic conservation laws" | 9 | 9 | 3 |
| QA2 | "adjoint-based r-adaptation node movement goal-oriented output error mesh redistribution optimization" | 6 | 6 | 4 |
| QA3 | "mesh movement network machine learning r-adaptivity M2N UM2N universal mesh movement 2024 2025" | 10 | 10 | 3 |
| QA4 | "moving mesh r-adaptive method of characteristics space marching supersonic nozzle characteristic net redistribution" | 8 | 8 | 4 |
| QA5 | "\"Space-Marching Method for Calculating Steady Supersonic Flows on a Grid Adapted to the Solution\" Journal of Computational Physics 1998" | 9 | 9 | 3 |
| FA1 | WebFetch arxiv.org/abs/2405.00904 (abstract) | 1 | 1 | 1 |

Databases/communities reached: arXiv, ScienceDirect/JCP/CPC listings,
AIAA ARC, NeurIPS/GitHub (ML mesh-movement community), SAGE, Springer,
NASA NTRS. Russian classical school (§0-ter(a), this territory is
classical-adjacent): reached at [TITLE] depth through QA4/QA5 — the
space-marching-on-adapted-grids line (JCP 1998 variational grid
adaptation; Utyuzhnikov-Rudenko 2008) is the visible modern end of the
Russian grid-generation ancestry (Godunov-Prokopov / Ivanenko
adaptive-harmonic mappings); no claim is made beyond existence and the
snippet facts stated below. Corpus recency: 1994-2025, newest 2025
(AMBER, arXiv:2505.23663 [TITLE]). Completeness is falsifiable against
this table.

### A.4 Census (per-source one-liners, depth-marked)

Family canon:
- **Huang-Ren-Russell 1994** (MMPDE line) [TITLE]: moving-mesh PDEs from
  the equidistribution principle — the family's definitional object.
- **Budd-Huang-Russell 2009**, "Adaptivity with moving grids", Acta
  Numerica [ABS]: the family review; r-adaptivity = fixed node count +
  fixed connectivity, nodes moved by a monitor-driven law (equidistributed
  monitor = the central principle); MMPDE decoupled/alternating solution
  practice for hyperbolic systems.
- **Velocity-based / GCL forms** [ABS via QA1 snippets]: monitor-driven
  mesh velocity; the moving-mesh FV line for 1-D hyperbolic conservation
  laws (JCP 2006 MHD item) marches the mesh with the solution.

Adjoint-in-moving-mesh (the axis's named modern best):
- **Fidkowski 2023**, "Output-Based Mesh Optimization Using
  Metric-Conforming Node Movement" [TITLE+ABS]: goal-oriented NODE
  MOVEMENT conforming to a MOESS-derived metric — the output-based school
  itself now carries an r-arm; motion driven by adjoint-weighted error
  sampling.
- **Thakur & Nadarajah 2024**, arXiv:2405.00904, "Adjoint-based
  goal-oriented implicit shock tracking using full space mesh
  optimization" [ABS, fetched]: LNKS full-space optimizer MOVES mesh
  faces to align with the shock, objective = MINIMIZE the
  adjoint-weighted residual (DWR) indicator, goal-oriented tracking of
  only the functional-relevant shock segment. The family's sharpest 2024
  instance — and its entire objective is to RECOVER, by optimization on a
  captured mesh, the front alignment our fitted march has BY CONSTRUCTION
  (exact RH front as explicit unknown, Lemma B §4.3 [FULL-R]).
- **ONERA finite-volume goal-oriented line** ("functional derivative with
  respect to nodal coordinates") [TITLE]: dJ/dX nodal-coordinate
  derivatives as the r-adaptation driver — the adjoint-in-moving-mesh
  mechanism in FV production form.

Modern ML layer (genuine best, cited to steelman not to adopt):
- **M2N (Song et al. 2022/2024)** and **UM2N (NeurIPS 2024 Spotlight,
  arXiv:2407.00382)** [ABS]: neural mesh-movement operators
  (GT encoder + GAT decoder), zero-shot across PDE types, replacing
  Monge-Ampere movers, effective "in scenarios where the conventional
  method fails"; **AMBER 2025** (arXiv:2505.23663) [TITLE]. The line
  optimizes the SAME r-objective (monitor equidistribution) at lower
  mover cost — it does not change what motion can buy.

Marching + adaptation (the transfer target):
- **JCP 1998**, "Space-Marching Method for Calculating Steady Supersonic
  Flows on a Grid Adapted to the Solution" (S0021999198960739) [TITLE]:
  noniterative implicit SPACE-MARCHING Euler on a solution-adapted grid;
  variational grid adaptation (smoothness/orthogonality/cell-volume),
  lines accumulated at strong gradients; demonstrated on nozzles and
  jets. Authorship not verified through the paywalled listing — no
  author claim made.
- **Utyuzhnikov-Rudenko 2008** [TITLE]: adaptive MOVING mesh for
  non-stationary hypersonic flows.
- **Semi-adapted space marching, JCP 2023** (S0021999123002656) [TITLE]:
  the marching+adaptation line is alive in 2023 (sonic-boom prediction).
- **r-adaptive Flux Reconstruction for supersonic flows, CPC 2022**
  (S0010465522000923) [ABS]: node re-positioning with FROZEN count and
  connectivity (spring analogy) for supersonic flows — the loop-relevant
  fact: r-adaptation is prized there precisely because it "maintains
  computational cost" at fixed mesh size.

### A.4-bis Census absences (query-bounded, honest)

- NO r-adaptive / moving-mesh law for CHARACTERISTIC (MoC) marching found
  (QA4∩QA5 terms): the marching+adaptation line above lives on
  shock-CAPTURING space-marching grids; classical and modern MoC practice
  controls SPACING and INSERTION only (PANEL §2.3 census, cited). This
  narrows but confirms PANEL §2.4's absence: the transfer of ANY adaptive
  placement doctrine to a marched characteristic solver is a
  build+measure object.
- NO adjoint-driven r-adaptation on a marched solver found (QA2∩QA4).

### A.5 Family relation to the record (the facts the brief orders weighed)

1. **A36 IS an equidistribution law — family relation named.** The
  adopted static arm `h ∝ [log(1/(M²−1))]^{−1/3}` (PANEL §2.5, cava A36,
  cited) is exactly de Boor equidistribution `h·M = const` with the
  DERIVED monitor `M(x) = [log(1/(M²−1))]^{1/3}` on the strip coordinate.
  The C9 verdict therefore ALREADY adopts the moving-mesh family's
  central principle (the monitor + equidistribution pair) in a-priori,
  derived, static form — what the family adds beyond A36 is only the
  MECHANISM (dynamic motion) and the FEEDBACK (solution-dependent
  monitor), not the principle.
2. **A36 clause (ii) is one-locus anti-motion, not family closure.** "
  moving the IVL de-rates O(h²)" (PANEL §2.5, cited) forbids motion of
  ONE point family (the IVL, where the mesh-independent Mach margin
  lives). It says nothing about redistributing wall-station seeds
  downstream of the IVL. The family stayed genuinely OPEN until this
  supplement; F9c (VERDICT §2.3) is the correct generalization: a pin,
  not a family verdict.
3. **Front-fitting IS mesh motion — the family's best instance is already
  consumed.** The fitted-front class of record (C49 incumbent :653;
  Lemma B §4.3 [FULL-R]: front = explicit unknown constrained by exact
  RH, its adjoint block deposited on the interface) is Lagrangian
  r-adaptation at the one locus where motion is worth the most. The 2024
  modern best of the adjoint-in-moving-mesh family (Thakur-Nadarajah,
  [ABS]) spends a full-space LNKS optimizer to APPROXIMATE this
  alignment on captured meshes. The family's highest-value content is
  therefore not merely compatible with the stack — the stack already
  owns its exact form.
4. **Columns are not a fixed grid — what "motion" can even mean here.**
  Interior nodes of the march are INTERSECTIONS of characteristics: they
  cannot be repositioned independently of the solution (moving an
  interior node = tracking a different characteristic). The only free
  placement dofs of the marched structure are (a) the seed line — wall
  stations / initial-line discretization launching the C- columns — and
  (b) insertion/deletion during the march (the AC2 primitive). MMPDE
  continuous-map motion `x(ξ,t)` does NOT transfer literally. The
  family's residual transferable dof is exactly (a): **fixed-count SEED
  REDISTRIBUTION** — moving column launch stations per the same derived
  monitor/indicator at frozen NI/da/Nw/Ne.
5. **The loop-compatibility asymmetry the panel never weighed (honest,
  pro-motion).** PANEL §1.2: adaptive point COUNTS change array shapes
  and trigger XLA recompilation; the S25/S25-bis record chain is priced
  for fixed shapes. Insertion (AC2) changes counts; fixed-count seed
  redistribution does NOT — an r-arm is fixed-shape by construction, so
  it rides the compiled record chain with zero recompile cost. On the
  COST axis the r-family strictly dominates insertion; this is the
  steelman fact that forbids closing the family by omission.

### A.6 Materiality (§0-ter(c), both directions)

- **J-error direction: NOT material above the campaign's bands.** Both
  mechanisms (insert vs move) place resolution per the SAME monitor
  family; the placement question itself is what F9a measures. The
  singular-strip correction the derived monitor buys is ≈1.6× spacing in
  the first strip [INF] (PANEL §3.1.3, cited) — a small correction, and
  the family's big lever (front alignment) is already exact of record
  (point 3 above). Node MOTION vs INSERTION is therefore not plausibly a
  band-crossing J-error effect on this configuration. Answer to the
  brief's materiality question: **NO** (material: false).
- **Cost direction: MATERIAL.** Fixed-shape motion avoids the recompile
  penalty insertion pays (point 5) — first-order in the priced record
  economics. Per §0-ter(c), an immaterial-in-J fork is decided on
  cost/simplicity: cost argues for CARRYING the r-arm into the
  measurement, not for adopting it unmeasured (no census precedent on
  marched solvers, A.4-bis).

### A.7 Steelman + closure

Steelman (best modern instances, rejected-for-adoption with stated
reasons): MMPDE/velocity movers (Budd-Huang-Russell [ABS]) — their
continuous-map mechanism has no object to act on here (A.5.4); ML movers
(UM2N [ABS]) — same objective, cheaper mover: inherits the same
non-transfer; goal-oriented node movement (Fidkowski 2023 [TITLE+ABS],
Thakur-Nadarajah 2024 [ABS]) — its alignment content is consumed by the
fitted class (A.5.3) and its smooth-region content is the monitor
principle consumed by A36 (A.5.1); none has census standing on a marched
characteristic solver (A.4-bis).

**CLOSURE (axis A): FOLD — one named arm into F2-C9-MESHLAW-CAMPAIGN;
family otherwise closed by stated reason at census grade.**

- The moving-mesh family is NOT adopted as a production law (no
  precedent on marched solvers; motion's alignment content already exact
  of record; J-materiality below bands) and is NOT rejected outright
  (the fixed-shape cost dominance and the residual seed dof are genuine).
- **Named arm (new, folded): F9a arm R — fixed-count seed
  redistribution.** Same design, same phase set, frozen NI/da/Nw/Ne
  (matched TOTAL unit-process count AUTOMATIC by construction — the
  repaired F9a meter, VERDICT §2.3, satisfied identically); wall-station
  seeds redistributed by equidistributing the SAME derived monitor/
  indicator the campaign already carries (A36 arm statically; the
  [X-AKNO]-mechanism march-side indicator when leg (b)'s build lands);
  IVL seed PINNED (F9c binds verbatim — clause (ii) cited, the first
  seed never moves); F9b applies to seed motion identically (a TR
  rejection is attributed by re-running on the frozen pre-motion seed
  set).
- **Falsifier pin (F9a-R):** the r-arm is DROPPED if it fails to beat
  uniform+A36 outside the joint bands on the pre-registered twin sites
  under the same F9a threshold discipline (derivation published before
  first use — VERDICT §2.3, RC911-3 repair, inherited verbatim); it is
  PROMOTED only under the same E_A ≤ E_U/2 rule as the insertion arm.
  Symmetrically: if the r-arm matches the insertion arm's error at
  matched unit-process count, the COST tiebreak (A.6) selects the r-arm
  as the production mechanism and the insertion primitive falls back to
  the between-runs role — this outcome still closes C9 (converged, not
  re-gated).
- Consistency with the verdict of record: VERDICT §2.3 is UNCHANGED —
  uniform interim, A36 arm, AC2 primitive, F9a/F9b/F9c all stand; the
  supplement ADDS one arm to the pinned campaign. CONFIRM.

---

## B. AXIS B — DISCRETE vs CONTINUOUS ADJOINT AS THE C11 DWR WEIGHT

### B.1 The single main question (question-anchored, frozen first)

THE question the C11 DWR weight answers: which adjoint REALIZATION
makes the DWR estimate `η_J = Σ ⟨R, λ⟩` an honest carrier of the
J-discretization bar the duty certifies — effectivity measured against
E_true (θ = η_est/E_true, measured; PANEL §1.1 C11 + §1.2, cited). The
fork frozen: (I) DISCRETE AD-adjoint of the marched scheme (the stack
of record: JAX custom_vjp, exact transpose, O3.1-verified — [X-A1IM]
:814), under which the weight is the sensitivity of the DISCRETE
functional to discrete-residual perturbations at band sites; (II)
CONTINUOUS/characteristic adjoint, separately discretized (the
Ancourt-Peter-Atinault 2023 ACE line [FULL-R :199-208]; Lozano-Ponsin
2025 as its extension [PART-R :122-128]); (III) a declared combination.
[RS911-2 correction of record, 2026-08-19: the question as first frozen
wrote branch (I)'s definition into itself (the discrete-sensitivity
clause) — reworded to the judge's neutral truth-referenced
certification question and the clause moved into branch (I)'s
description, per VERDICT_C9C11_supplement.md §1 (RS911-2 SUSTAINED)
and §4.4. No conclusion changed.]

### B.2 Pre-registered decision criteria (frozen BEFORE the queries ran)

- (I) DISCRETE wins the WEIGHT role only if ALL of: exactness at the
  computed J is of record (no dual-solve approximation added); the
  known discrete-adjoint pathology at fronts (the trap) is bypassed or
  controlled ON OUR CLASS by record objects; a census-standing estimator
  FORM exists that consumes a discrete weight (the same-level pairing
  `⟨R_h(u_h), λ_h⟩` is identically zero at a solved system — an
  enrichment space is mandatory and must be named); the continuous
  structure remains armed as an executable referee.
- (II) CONTINUOUS wins only if census/record shows the discrete adjoint
  of OUR march is dual-inconsistent at band sites in a way that biases
  η_J, or the continuous field is available at the sites at lower cost
  than the AD sweep.
- (III) A combination must assign ONE role per object (no double-count):
  weight vs structure/referee.
- Route facts binding whatever wins (brief, verified §0): custom_vjp
  everywhere ([X-A1IM] :814 "never unrolled"), ONE-LOWERING discipline
  (C48 note :649 — mixed lowering was the measured defect class).

### B.3 The record already carries the fork's skeleton (cited, not re-derived)

- **P2 Lemma B [FULL-R]:** reverse-AD of the fitted march IS the discrete
  adjoint characteristic sweep (THEOREM, finite-dim; PAP-P2LB :1484);
  §4.4: the Giles-Ulbrich trap (fixed-stencil discrete adjoint converges
  to a WRONG value across CAPTURED shocks — "the trap is a theorem",
  lit row :120 [PART-R]) is BYPASSED BY CONSTRUCTION on the fitted class
  (no smear to differentiate; front adjoint block = discrete twin of the
  Giles-Pierce interior condition); §4.5: discrete→continuous adjoint
  mesh-limit consistency at O(h²) is SCHEMA — the G12 frontier — with
  pre-registered executable falsifiers O3.2 (Hoffman E-residual order)
  and O3.3 (gradient vs Rao residual; oracle coordinates = L-P 2025
  Eqs. (30)/(31) compatibility residuals, P2_outline §5 :237-238).
- **The continuous/characteristic-native line is ALREADY the referee of
  record:** lozano_ponsin_2025 row summary [PART-R]: "adjoint
  compatibility Eqs. (30)/(31) = O3.3 bench rows (F-O33BENCH)"; the S14
  norm pre-registration adds the characteristic-borne adjoint
  discontinuities of L-P 2025 to the S-LBML limit target, "which the
  characteristic-ALIGNED fitted march can represent natively"
  (P2_outline §5 :246-250).
- **The in-house DWR precedent uses the DISCRETE adjoint variable:**
  [X-AKNO] f2 = −λ2 (Prop. A3) — the indicator the C11/C9 duties promote
  (VERDICT §2.3/§2.4) is a discrete-adjoint object already.
- So the fork was never adjudicated AS A CHOICE (dedup §0: no ledger
  row), but the record contains a proven bridge: the discrete weight and
  the continuous structure are the SAME object up to the §4.5 SCHEMA,
  whose falsifiers exist, are pre-registered, and are executable on the
  A1 engine.

### B.4 Query protocol table (§0-ter(a); engine = WebSearch, run 2026-08-19)

| # | Query (verbatim) | Returned | Screened | Included |
|---|---|---|---|---|
| QB1 | "discrete versus continuous adjoint goal-oriented error estimation comparison dual weighted residual which adjoint" | 8 | 8 | 3 |
| QB2 | "dual consistency discrete adjoint functional superconvergence Hicken Zingg Lu Darmofal adjoint consistent discretization" | 8 | 8 | 4 |
| QB3 | "adjoint error estimation shocks output functional captured versus fitted shock adjoint weight validity transonic Euler" | 8 | 8 | 3 |

(Plus PANEL §2.1 Q1-Q5/Q9 and F1, cited not re-run — this table extends,
does not replace, the panel's trail.) Databases/communities: arXiv,
ScienceDirect/JCP/CMAME, AIAA ARC, Springer, UTIAS (Hicken-Zingg PDF
host), deal.II/Hannover DWR school. Russian classical school: bears on
axis A, not on this axis (the DWR/dual-consistency corpus is
Anglo-European; the classical Kraiko school enters C11 through the
Giles-Pierce/Kraiko bank already registered — no separate query owed).
Corpus recency: 2000-2025, newest 2025 (VEM-DWR, S0045782525003068
[TITLE]); the modern layer (multigoal/NN-DWR 2021-2025) is already in
PANEL §2.3, cited.

### B.5 Census (per-source one-liners, depth-marked) + adjudication

Census additions beyond PANEL §2.3:

- **Hicken & Zingg 2014**, "Dual consistency and functional accuracy: a
  finite-difference perspective", JCP [ABS]: dual-consistent
  discretizations = "a synthesis of the so-called discrete-adjoint and
  continuous-adjoint approaches"; dual consistency delivers functional
  superconvergence AND accurate functional error estimates — the fork's
  modern resolution IS the synthesis, not a winner-take-all.
- **"The Role of Dual Consistency in Functional Accuracy: Error
  Estimation and Superconvergence"** [TITLE] + **quasi-1D Euler
  dual-consistency note (cell-centered vs cell-vertex)** [TITLE]: the
  dual-consistency question is posed and answered scheme-by-scheme —
  exactly the status our march holds as the §4.5 SCHEMA.
- **Venditti & Darmofal 2000** (quasi-1D, JCP) [TITLE] + field practice
  [ABS, QB1 snippets]: the production DWR estimator is the TWO-LEVEL
  DISCRETE form — coarse-level discrete adjoint (or fine-level adjoint
  of the injected state) weighting the FINE-SPACE residual of the
  injected coarse solution; "discrete adjoint approaches dominate modern
  implementations".
- **arXiv:2305.15285 (2023)** [ABS, already in PANEL §2.3]: linearization
  errors in DISCRETE goal-oriented estimation — the discrete line's own
  modern honesty literature.
- **Giles, "Discrete Adjoint Approximations with Shocks"** (Springer
  chapter) [TITLE] + **Peter, Renac & Labbé, FV discrete-adjoint
  analysis, arXiv:2009.07096** [TITLE] (same ONERA school as the
  consumed Ancourt anchor): the Giles-Pierce lineage itself carries
  the discrete-adjoint-at-shocks question; its negative results live on
  CAPTURED representations (lit row :120 [PART-R]) — the class our
  stack does not use (C49 incumbent, cited). [RS911-3 correction of
  record, 2026-08-19: arXiv:2009.07096 re-attributed "Lozano-Ponsin" →
  Peter, Renac & Labbé, judge-fetched at source
  (VERDICT_C9C11_supplement.md §0); [TITLE] depth kept.]
- **CMAM 2020** [ABS, already in PANEL §2.3]: DWR reliability is
  conditional on dual-approximation quality — for a discrete AD weight
  this caveat lands on the ENRICHMENT operator (the weight itself is
  exact at machine roundoff, O3.1), not on a dual PDE solve.

Adjudication against B.2 (criteria applied in order):

- (I).exactness: HELD of record — O3.1 dot-product over the ENTIRE march
  at machine roundoff ([X-A1IM] :814). A separately discretized
  continuous adjoint would ADD a second solver with its own mesh law,
  its own front interior conditions (Giles-Pierce BC + L-P
  characteristic-borne discontinuities) and its own discretization error
  — strictly more machinery, and the census shows no accuracy gain for
  it on fitted/aligned representations.
- (I).trap: BYPASSED on our class by construction (Lemma B §4.4
  [FULL-R]); the pathology literature (Giles-Ulbrich; Lozano
  mesh-divergence) lives on captured smears and wall/trailing-edge
  singular loci — the latter already norm-excluded of record
  (P2_outline §5 :229-235).
- (I).form: the two-level discrete form (Venditti-Darmofal) is the
  census-standing estimator that consumes a discrete weight; it composes
  with the [X-O32] ladder the duty already orders (leg (a) before leg
  (b), VERDICT §2.4). The same-level pairing is identically zero at a
  solved system — so the ENRICHMENT SPACE is a mandatory named pin, not
  an implementation detail (emergent sub-aspect per §0-bis(a)(5), closed
  here as pin (iii) below).
- (I).referee-armed: the continuous/characteristic structure is ALREADY
  the executable referee (O3.2/O3.3 + F-O33BENCH rows + Giles-Pierce
  analytic oracle in F11a — VERDICT §2.4, cited).
- (II): NOT triggered — no census or record evidence of dual-
  inconsistency of the FITTED march's discrete adjoint at band sites;
  the open remainder is exactly the §4.5 SCHEMA, which has named
  falsifiers rather than adverse evidence. The continuous field is
  analytic only on the Giles-Pierce oracle — where it serves as E_true
  (referee), which is precisely not the weight role.
- (III): the combination is therefore forced with one role per object.

**CLOSURE (axis B): the C11 DWR weight of record = the DISCRETE
AD-adjoint of the marched scheme (custom_vjp, one-lowering); the
continuous/characteristic-native structure = the FORMULATION FRAME and
the REFEREE, never the weight.** Stated reason: the weight must answer
for the COMPUTED J (B.1) — the discrete adjoint is that object exactly
and at machine roundoff of record; the trap that would disqualify it is
bypassed by the fitted class of record; the continuous line's entire
verifiable content (compatibility residuals, characteristic-borne
discontinuities, analytic oracle) is already armed as falsifiers/referee
— promoting it to the weight would duplicate machinery and DISARM the
referee (a weight cannot referee itself; O-F24's independence argument,
PANEL §3.0, applies inside the DWR build too).

Pins (exact, riding the existing duty — no new duty minted):

- (i) **Weight realization**: leg (b)'s "characteristic-native DWR" is
  BUILT on the discrete AD-adjoint λ of the march (the [X-AKNO]
  f2 = −λ2 mechanism promoted per VERDICT §2.4), lowered ONCE per the
  C48 discipline (:649) — the "characteristic-native" qualifier names
  the LOCALIZATION (march topology / owner array) and the REFEREE
  STRUCTURE (ACE/L-P compatibility along characteristics), not a
  separately discretized continuous dual.
- (ii) **Referee structure**: Ancourt 2023 (CONSUMED input, VERDICT
  §2.4) + L-P 2025 enter as the compatibility-residual referee (the
  F-O33BENCH rows of record) and as the smoothing constraint in (iii).
- (iii) **Enrichment pin (the emergent sub-aspect, closed)**: the
  fine-space residual of the two-level form is evaluated on the
  [X-O32] ladder's next-finer member (the ladder leg (a) already
  builds); any reconstruction/smoothing operator used to enrich the
  weight MUST NOT smooth across characteristics or fronts where the
  adjoint is discontinuous of record (L-P 2025 characteristic-borne
  discontinuities, P2_outline §5 — the fitted march represents them
  natively; an enrichment that smears them would re-import the captured
  pathology through the back door).
- (iv) **Falsifier pin F11d (weight-realization honesty — completes
  F11a/b/c; uses only existing machinery, no magic constants)**: on the
  Giles-Pierce quasi-1D analytic oracle (F11a site (i)), the discrete
  AD-adjoint weight restricted to the oracle's sites must converge to
  the analytic continuous adjoint at the PRE-REGISTERED O3.2/O3.3
  order/norms (Lemma B §4.5 falsifiers EXECUTED at the estimator's own
  sites, in the same window as the F11a ladder). FIRES (wrong order,
  nonvanishing residual, or compatibility-residual blow-up at a band
  site) ⇒ the fitted march's dual consistency is refuted AT BAND SITES:
  the weight realization is re-adjudicated (dual-consistency repair or
  continuous-adjoint discretization) BEFORE any DWR promotion — F11a
  cannot promote past a fired F11d. This is the falsifier that would
  select branch (II); its firing re-opens the WEIGHT realization only,
  never the C11 architecture (DWR-target + referee permanence stand —
  VERDICT §2.4).

### B.6 Materiality (§0-ter(c), both directions)

The fork is MATERIAL in general: on captured representations the
discrete adjoint converges to a WRONG value across shocks (theorem of
record, lit row :120) — a wrong weight biases η_J and the derived safety
factor S, i.e. the bar itself. On OUR stack the material branch is
neutralized by the class choice (fitted fronts, C49 + Lemma B §4.4), and
the residual exposure — dual consistency of the fitted march at band
sites — is exactly what F11d executes. The IMMATERIAL residual is the
cost delta: the discrete weight is a by-product of the gradient sweep
already priced (+0 solves, PANEL §1.2), a separately discretized
continuous dual would be a new solver. Depth follows stakes: closed at
census grade with the executable pin, no over-build.

Consistency with the verdict of record: VERDICT §2.4 is UNCHANGED — DWR
target primary, GCI referee permanence, leg ordering, D-49 both-branches,
Ancourt/L-P consumption all stand; the supplement names the WEIGHT the
verdict left unnamed and adds F11d. CONFIRM.

---

## C. VERDICT-CONSISTENCY CHECK (the supplement's mandate)

- Axis A closure vs VERDICT §2.3: CONSISTENT — adds arm R + F9a-R to the
  pinned campaign; no adopted/demoted status moves. CONFIRM.
- Axis B closure vs VERDICT §2.4: CONSISTENT — names the weight inside
  the adopted architecture; F11d strengthens the promotion gate in the
  incumbent-protective direction (DWR cannot be promoted on an
  unverified dual consistency). CONFIRM.
- **verdict_conflict: NULL.** One RIDER CORRECTION (not a conflict — it
  strengthens the verdict): VERDICT §4.7 lists "Lozano-Ponsin 2025"
  among proposed NEW literature rows "all grep-proven absent today" —
  false for that one item: row `lozano_ponsin_2025` EXISTS
  (literature_registry.yaml:122-128, READ-PARTIAL, PDF on disk in
  literature/). The panels' estimator-token greps (PANEL §1.4) could not
  see it (no token overlap) — same navigation-first failure mode as
  RC911-5, caught here by a family-token grep. Consequence carried in
  §4.4 below; the panel's census depth for L-P 2025 was UNDER-stated
  ("[abstract read]" — the repo holds page-verified content).

---

## 4. PROPOSED DELTAS (§4-style; proposals only — landing window applies)

### 4.1 C9 note delta (appends to the VERDICT §4.3 note text, verbatim)

"Supplement of record (BASE/blocco3/PANEL_C9C11_SUPPLEMENT.md, axis A):
the moving-mesh/r-adaptive family is CLOSED at census grade — A36 IS the
family's equidistribution principle in derived static form; clause (ii)
generalizes to F9c (one-locus anti-motion, not family closure);
front-fitting = the family's alignment content, already exact of record
(C49/Lemma B §4.3); MMPDE map-motion does not transfer (columns =
characteristic intersections; free dofs = seeds + insertion). FOLDED:
F9a arm R = fixed-count seed redistribution (frozen NI/da/Nw/Ne, matched
unit-process count by construction, fixed-shape/no-recompile; IVL seed
pinned per F9c; F9b applies via frozen pre-motion seed set). Falsifier
F9a-R: dropped if not beating uniform+A36 outside joint bands on the
twin sites (same threshold discipline); at error-parity with the
insertion arm, the cost tiebreak selects the r-arm as production
mechanism (fixed shapes). J-materiality of motion-vs-insertion declared
BELOW bands; cost materiality (recompile) declared FOR the r-arm."

### 4.2 C11 note delta (appends to the VERDICT §4.4 note text, verbatim)

"Supplement of record (BASE/blocco3/PANEL_C9C11_SUPPLEMENT.md, axis B):
the DWR WEIGHT fork is CLOSED — weight of record = the DISCRETE
AD-adjoint of the marched scheme (custom_vjp, one-lowering per C48;
exact at computed J, O3.1 [X-A1IM]; trap bypassed on the fitted class,
P2 Lemma B §4.4); the continuous/characteristic-native line
(Ancourt 2023 + Lozano-Ponsin 2025) = formulation frame + REFEREE only
(compatibility residuals = F-O33BENCH rows; never the weight — a weight
cannot referee itself). Estimator form = two-level fine-space residual
(Venditti-Darmofal class) on the [X-O32] ladder; enrichment operator
must not smooth across characteristic-borne adjoint discontinuities
(L-P 2025, P2_outline §5). New pin F11d: on the Giles-Pierce oracle the
AD weight must converge to the analytic adjoint at the pre-registered
O3.2/O3.3 order AT BAND SITES; F11d fired blocks F11a promotion and
re-opens the weight realization only (architecture stands). Dual
consistency of the march = P2 Lemma B §4.5 SCHEMA — F11d is its
execution at estimator sites."

### 4.3 Candidate NEW ledger row (per §0-bis(d); dedup-verified §0 — NOT minted here)

- proposed id: C52 (next free; landing window re-verifies numbering by
  measured command per SR-12)
- choice: "Adjoint REALIZATION of record for the marched stack, per
  role (gradient / DWR weight / adaptation indicator): discrete
  AD-adjoint (custom_vjp, one-lowering) vs separately discretized
  continuous adjoint vs dual-consistent synthesis"
- incumbent: "discrete AD-adjoint everywhere (route fact since S8/S18;
  never adjudicated as a choice — §0-bis(a)(2) verification 2026-08-19)"
- status: NEVER → proposed ADJUDICATED-FOR-C11-SCOPE by this supplement
  (weight role closed; gradient role = wave-2 C31TRIO consumption;
  indicator role = closed by transitivity, f2 = −λ2 is the same object)
- evidence: "BASE/blocco3/PANEL_C9C11_SUPPLEMENT.md §B; P2 Lemma B
  §4.4/§4.5; [X-A1IM]; C48 note"
- note: "The dual-consistency residue is the §4.5 SCHEMA with F11d as
  its estimator-site execution; a fired F11d re-opens this row, not C11."

### 4.4 Registration-rider corrections (to VERDICT §4.7, verbatim deltas)

- STRIKE "Lozano-Ponsin 2025" from the proposed NEW rows list: row
  `lozano_ponsin_2025` exists (literature_registry.yaml:122-128,
  READ-PARTIAL, on disk). Replace with: "lozano_ponsin_2025 row EXISTS —
  the C11 duty consumes it as a HELD anchor (READ-PARTIAL; upgrade to
  READ-INTEGRAL rides leg (b) if the build needs Eqs. (30)/(31) beyond
  the page-verified summary)."
- ADD (WANTED tier, consumed by this supplement's closures): Hicken &
  Zingg 2014 JCP 256:161-182, doi 10.1016/j.jcp.2013.08.014,
  dual-consistency/functional-accuracy (axis-B synthesis anchor)
  [RS911-4 correction of record, 2026-08-19: cite fixed from the
  erroneous "JCP 250:161-180" — of record J. Comput. Phys. 256:161-182
  (2014), judge-verified at doi, VERDICT_C9C11_supplement.md §0/§4.4;
  fix applied BEFORE the WANTED row mints]; Thakur & Nadarajah 2024 arXiv:2405.00904
  goal-oriented implicit shock tracking (axis-A modern-best steelman;
  also feeds C49's Phase-C advocate); Budd-Huang-Russell 2009 Acta
  Numerica "Adaptivity with moving grids" (family review, TITLE-tier
  registration for the axis-A closure's citability).
- Venditti-Darmofal 2000 (quasi-1D) added alongside the already-ridered
  2002 row IF the F2 build adopts the quasi-1D oracle form (leg (b)
  discretion; see PAPERS NEEDED).

Counting rule (stated): proposed_note_deltas = 4 = {C9 note delta,
C11 note delta, candidate row C52, rider-correction block}.

---

## PAPERS NEEDED (mandatory section; §0-bis(c))

No CLOSURE in this supplement waits on a full text: both axes close on
in-repo verified objects ([FULL-R]/[PART-R] rows + P2 lemmas) plus census
at the stated [ABS]/[TITLE] depths. Two full texts are asked for the F2
campaign legs (build-time inputs, not closure-blocking):

1. **Venditti & Darmofal 2000**, "Adjoint error estimation and grid
   adaptation for functional outputs: application to quasi-1D flow",
   J. Comput. Phys. 164(1):204-227. WHY: the two-level discrete-weight
   estimator form pinned in §B.5(iii) at its origin, ON quasi-1D — the
   same configuration as the Giles-Pierce oracle F11a uses. WHAT WAITS:
   leg (b)'s exact two-level algebra (injection operator + which-level
   adjoint variant); until then the pin stands at census grade.
2. **Hicken & Zingg 2014**, "Dual consistency and functional accuracy:
   a finite-difference perspective", J. Comput. Phys. 256:161-182,
   doi 10.1016/j.jcp.2013.08.014 [RS911-4 correction of record,
   2026-08-19: cite fixed from the erroneous "JCP 250:161-180" —
   judge-verified at doi, VERDICT_C9C11_supplement.md §0] (PDF
   publicly hosted at UTIAS — procurement may be a download, not an
   upload). WHY: the dual-consistency criteria in checkable form for a
   non-Galerkin scheme. WHAT WAITS: the F11d execution's
   order-of-convergence bookkeeping against a published criterion set;
   until then F11d stands on the in-repo §4.5 pre-registration alone
   (sufficient, falsifiable).

---

## MACHINE SUMMARY

```json
{
  "axes": {
    "moving_mesh": {
      "closure": "FOLDED-AS-NAMED-ARM: family closed at census grade (A36 = its equidistribution principle in derived static form; front-fitting = its alignment content, already exact of record; MMPDE map-motion non-transferable to characteristic intersections); one genuine residual dof folded into F2-C9-MESHLAW-CAMPAIGN as F9a arm R = fixed-count seed redistribution (fixed-shape/no-recompile, IVL seed pinned per F9c, F9b via frozen pre-motion seed set), falsifier F9a-R pinned (dropped if not beating uniform+A36 outside joint bands; cost tiebreak at error-parity selects it as production mechanism)",
      "reason": "no census precedent on marched characteristic solvers (absence narrowed and confirmed: adaptation lives on capturing space-marching grids); motion's high-value content (front alignment) already consumed exactly by the fitted class (C49/LemmaB 4.3, vs Thakur-Nadarajah 2024 recovering it by optimization); A36 clause (ii) is one-locus anti-motion, generalized as pin F9c, not family closure; fixed-shape cost dominance of motion over insertion is real and material -> measure, not adopt or reject",
      "material": false
    },
    "adjoint_choice": {
      "closure": "CLOSED-COMBINATION with one role per object: C11 DWR weight of record = DISCRETE AD-adjoint of the marched scheme (custom_vjp, one-lowering per C48); continuous/characteristic-native line (Ancourt 2023 + Lozano-Ponsin 2025) = formulation frame + referee ONLY (compatibility residuals = F-O33BENCH rows); estimator form = two-level fine-space residual (Venditti-Darmofal class) on the [X-O32] ladder with enrichment forbidden to smooth across characteristic-borne adjoint discontinuities; new pin F11d = LemmaB 4.5 SCHEMA falsifiers executed at band sites on the Giles-Pierce oracle, firing blocks F11a promotion and re-opens the weight realization only; candidate row C52 proposed for the stack-wide realization axis",
      "reason": "the weight must answer for the COMPUTED J: the discrete adjoint is that object exactly (O3.1 machine-roundoff of record, +0 solves); the disqualifying trap is a theorem only on captured smears and is bypassed by the fitted class of record (LemmaB 4.4); dual consistency (the census synthesis, Hicken-Zingg) is exactly the in-repo 4.5 SCHEMA with pre-registered falsifiers; promoting the continuous line to weight would duplicate machinery and disarm the referee"
    }
  },
  "verdict_conflict": null,
  "papers_needed": 2,
  "proposed_note_deltas": 4
}
```
