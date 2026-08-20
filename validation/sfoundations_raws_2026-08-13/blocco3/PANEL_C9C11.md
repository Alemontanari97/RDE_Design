# PANEL — CLUSTER C9C11 (march mesh law + error estimator for J)
# S-FOUNDATIONS-C2, Blocco 3 wave 1, 2026-08-19.
# Brief of record: validation/sfoundations_raws_2026-08-13/blocco3/BRIEF_wave1_panels.md §0 + §C9C11.
# Rows: docs/choice_ledger.yaml:217-226 (C9), :238-248 (C11).
# Diff anchors: validation/sfoundations_raws_2026-08-13/phaseB_tree_diff.md:66-72 (C9), :76-81 (C11).
# Verdict class of this file: PANEL PROPOSAL (feeds the F2 build; ledger edits happen at landing, not here).

---

## 1. FROZEN FORMAL STATEMENT

### 1.1 Shared sub-problem (frozen before any census query was issued)

Let `J` be a scalar thrust-class functional (a Verdict headline or banded
quantity) computed from a per-phase MARCHED axisymmetric Euler solve:
characteristic space-marching with fitted fronts (Sauer IVL start with
mesh-independent Mach margin `M_IVL − 1 = 5e-6`, kernel, C+ control
surface to the lip), phase-averaged with weights `mu` over `Xi`. The
discrete run is parameterized by a MESH LAW `L: (accuracy request,
design, phase) -> point placement`, currently the four per-run integers
`NI / da / Nw / Ne` (streamwise columns + wall/exit refinement). The
exact discrete adjoint is available through the JAX implicit-unit-process
stack (O3.1 dot-product verified end-to-end; docs/claims_registry.yaml:814).
Certificate discipline binds every choice: bands DERIVED (no magic
constants), rejectors must be able to FIRE, verdicts carry bars, and the
production loop is a TR-SQP optimizer calling the march per phase per
iterate (cost and staleness chain priced by the S25/S25-bis record
program).

Two individuated per-row questions on this shared object:

- **C9 (the mesh LAW).** Choose `L`:
  (a) uniform-per-run `NI/da/Nw/Ne` — INCUMBENT;
  (b) column-local C- insertion at record time — the classical MoC
      policy, spec attached of record (gapmap AC2: RK-G P2-compatible
      AMR primitive, ADVISORY_S24_sota_gapmap_2026-08-12.md:855);
  (c) goal-oriented AMR (Venditti-Darmofal): placement driven by an
      adjoint-weighted (DWR) indicator;
  (d) the derived singularity-aware spacing law (cava A36): log-weighted
      DWR equidistribution near the sonic strip,
      `h ∝ [log(1/(M²−1))]^{−1/3}`, refinement-only, IVL never moved.

- **C11 (the ESTIMATOR).** Choose the carrier of the J-discretization
  bar:
  (i)   two-level Richardson with fixed safety constant `K_RICH = 4`
        and ASSUMED order p=2 — INCUMBENT
        (validation/a1_ideal_march_jax.py:198; reuse points e.g.
        validation/o33_bench.py:127, thermotab_c1_jax.py:108);
  (ii)  three-mesh observed-p GCI (Roache/Celik);
  (iii) DWR `η_J = Σ_K ⟨R(u_h), λ_h⟩_K` with measured effectivity
        (Becker-Rannacher; Venditti-Darmofal);
  (iv)  LSQ multi-grid fit (Eca-Hoekstra: least-squares Richardson over
        ≥4 grids; "multigrid" in the ledger row = multiple grids, not
        the solver).

### 1.2 Quantities being optimized/bounded

- **Bar honesty**: effectivity `θ = η_est / E_true` of the estimator,
  measured, with the safety factor DERIVED from the measured θ
  population (never assumed).
- **Cost per certified run**: unit-process evaluations at fixed bar
  width (the mesh law) and extra solves per banded quantity (the
  estimator: 2-level = +1 solve, 3-mesh GCI = +2, LSQ = +3..4, DWR = +0
  solves given the adjoint but + estimator assembly).
- **Loop compatibility**: fixed-shape JAX compilation (adaptive point
  counts change array shapes), gradient consistency across re-mesh
  events (TR acceptance must not see remeshing noise), staleness chain.

### 1.3 Operational constraints of record (cited, binding)

- **Sonic-strip validity domain**: the adjoint has a log singularity at
  the sonic throat (Giles-Pierce 2001 §6.1; literature row
  docs/literature_registry.yaml:491-498). Of record (cava §3.25,
  RATIFIED): bars are NOT uniform to the throat — the pre-registered
  norms exclude IVL/lip/axis neighborhoods
  (validation/o32_mesh_convergence.py:24-39, h-independent window);
  order O(h²) SAFE (margin `M_IVL−1` is mesh-independent), constant
  inflated ≈4× in the first strip [INF class], GRADIENT immune (zero
  design support in the singular strip). The sonic/IVL exclusion is the
  only pre-registered exclusion WITHOUT its probe — D-49
  (docs/findings_registry.yaml:1468-1476), trigger of record: "the
  first new DWR-bar claim of record".
- **Observed-order defect of record** (against the incumbent estimator):
  findings row `mesh-amr:observed-order-not-at-band-sites`
  (docs/findings_registry.yaml:1182-1190, CONFIRMED medium): every
  two-resolution band presumes h^p while the repo's own three-level twin
  measurement returned NON-CONCLUSIVE (p_fine=2.5347, dp_tot=0.6704 >
  0.5 cap) and a standing counterexample exists (f2 drift GROWS under
  refinement, 9.48e-03 → 1.42e-02); deployed K=4 bands protect the
  coarse member only for observed p ≥ log2(4/3) = 0.415.
- **In-house DWR precedent**: the knot-adaptation carrier [X-AKNO]
  (docs/claims_registry.yaml:1290-1299, PRACTICE) already runs a
  DWR-conformant goal indicator on this stack — f2 = −λ2 (Prop. A3) drift
  per control-surface segment, attributed to the emitting wall station
  via the march topology (validation/adaptive_knot_optimize.py:16-27).
  It drives KNOT placement (design dof), not the march mesh; transfer to
  C9/C11 is a hypothesis, not a record.
- **K_RICH role reuse = C42** (docs/choice_ledger.yaml:571-579, wave 3):
  named dependency only — this panel does NOT decide C42, but its
  observed-p leg feeds the C42 audit (findings row owner "feeds the R25
  K_RICH audit", findings_registry.yaml:1189).
- **C10 refinement operator** (choice_ledger.yaml:228-236, per-direction
  GCI Eca-Hoekstra): adjacent row, NOT decided here; named where the
  LSQ census touches it.

### 1.4 Dedup (navigation-first, greps of this window)

- `grep 'DWR|Richardson|Venditti|Rannacher|GCI|effectivity'
  docs/literature_registry.yaml` → ONLY giles_pierce_2001 (:491-498).
  `grep 'Roache|Celik|Fidkowski|Hartmann|Loseille|Alauzet'` → NO MATCH.
  Search-proven absence: the DWR/GCI methodological canon
  (Becker-Rannacher 2001, Venditti-Darmofal 2002, Fidkowski-Darmofal
  2011, Roache/Celik, Eca-Hoekstra 2014, Lozano-Ponsin 2025) has NO
  literature-registry rows → registration duty named in §4, nothing
  re-minted.
- `grep 'richardson|DWR|K_RICH|effectivity|Venditti|Rannacher'
  docs/findings_registry.yaml` → rows :1182 (observed-order defect) and
  :1468 (D-49 probe) exist and are cited above; no new findings minted.
- `grep 'DWR|Richardson|effectivity|Venditti' docs/claims_registry.yaml`
  → [X-AKNO] :1290, march Richardson-band claim :814, twin falsifier
  :1397; cited, not re-minted.
- `grep 'C42|K_RICH' docs/choice_ledger.yaml` → C42 :571; C27 incumbent
  rho-formula :409 (wave-1 C27 panel's scope, not touched here).

---

## 2. SOTA CENSUS

### 2.1 Query trail (derived from §1, in execution order)

All searches run 2026-08-19 (WebSearch; one WebFetch chain: doi.org →
mdpi.com 403 → arXiv abstract page).

- Q1 "goal-oriented dual-weighted residual error estimation aerodynamic
  output functionals mesh adaptation review recent advances"
- Q2 "DWR error estimator effectivity index reliability safety factor
  compressible Euler output error"
- Q3 "Fidkowski output-based mesh adaptation 2023 2024 2025 machine
  learning goal-oriented anisotropic MOESS"
- Q4 "grid convergence index observed order least squares Eca Hoekstra
  numerical uncertainty estimation solution verification 2023"
- Q5 "Lozano adjoint Euler singularities sonic line trailing edge
  inviscid transonic 2019 2021 2023"
- Q6 "method of characteristics nozzle design characteristic insertion
  point spacing accuracy control supersonic marching"
- Q7 "mesh adaptation within aerodynamic shape optimization adjoint
  gradient consistency remeshing adaptive loop"
- Q8 "graded mesh a priori refinement near singularity equidistribution
  weighted error optimal grading hyperbolic"
- Q9 (absence probe) "dual weighted residual OR adjoint error estimation
  thrust functional supersonic nozzle method of characteristics space
  marching"
- F1 (fetch) arXiv:2503.13007 / Aerospace 12(6):494 abstract
  (Lozano-Ponsin 2025).

### 2.2 Corpus recency

Span **1997-2025**; newest items **2025**. Histogram (items actually
used below): pre-2000: 2 · 2000-2009: 5 · 2010-2019: 6 · 2020-2026: 12.
The modern refined layer is REACHED: ML-driven goal-oriented adaptation
(2020-2024), NN-guided DWR (2021-2022), multigoal DWR (2024-2025),
adjoint characteristic structure (2025), LSQ-GCI verification practice
(2014-2023, ASME JVVUQ). This census is breadth-first over titles +
result snippets + one abstract; only giles_pierce_2001 is READ-INTEGRAL
on disk — evidence levels stated per item, nothing cited above snippet
level.

### 2.3 Per-source one-liners

DWR / goal-oriented canon:
- **Becker & Rannacher 2001** (Acta Numerica): the DWR method —
  adjoint-weighted residual as functional-error estimate; the estimator
  class itself. [snippet + on-disk derivative knowledge via [X-AKNO]]
- **Venditti & Darmofal 2002** (JCP): output-based adaptation for
  aerodynamic functionals — the C9 ledger row's named alternative.
  [snippet]
- **Fidkowski & Darmofal 2011** (AIAA J 49(4), "Review of Output-Based
  Error Estimation and Mesh Adaptation in CFD"): the field's reference
  review; DWR = "goal/output-based", drives adaptation where the output
  cares. [snippet]
- **Yano-Darmofal MOESS line** (2012 JCP; extended to continuous FE
  2020, S0021999120303946): mesh optimization via error sampling and
  synthesis — the refined optimality layer above bulk marking. [snippet]
- **Fidkowski & Chen 2020-2021** (JCP 2021, "Metric-based, goal-oriented
  mesh adaptation using machine learning"): NN predicts MOESS anisotropy
  from primal/adjoint features — active modern line; also Ojha-Chen-
  Fidkowski 2022 (initial meshes by ML), Coppeans-Fidkowski-Martins 2024
  (anisotropic high-order). [snippets]
- **Roth et al. 2021-2022** (arXiv:2102.12450; Discover Applied
  Sciences 2022): neural-network-guided adjoint computations in DWR —
  modern line on cheapening the dual solve. [snippet]
- **Endtmayer/Wick school 2021-2025** (arXiv:2108.05654; arXiv:2404.01823;
  2025 journal version): multigoal-oriented DWR, two-side estimates
  (arXiv:1811.07586), balancing discretization vs iteration error.
  [snippets]
- **CMAM 2020** (doi 10.1515/cmam-2020-0036, arXiv:2003.08999):
  reliability/efficiency of DWR-type estimates with weight recovering —
  states the honest caveat: DWR reliability is conditional on dual
  approximation quality (effectivity ≈ 1 achievable but not free).
  [snippet]
- **arXiv:2305.15285 (2023)**: linearization errors in discrete
  goal-oriented estimation — modern refinement of DWR honesty. [snippet]
- **Anisotropic-estimator review 2021** (Computers & Fluids,
  S0045793021003601): review + comparison of estimators for anisotropic
  adaptation in flow simulation. [snippet]

Verification / observed-order canon:
- **Roache GCI** (1994/1997 line): grid convergence index; Fs=1.25 only
  with three grids + observed order, Fs=3 for two-grid studies —
  two-grid-with-assumed-order is the WEAKEST sanctioned form. [snippet
  + standard-practice knowledge; no stronger claim made]
- **Celik et al. 2008** (J. Fluids Eng. policy statement): codified
  three-mesh observed-p GCI procedure. [snippet]
- **Eca & Hoekstra 2014** (JCP 262:104-130): LSQ-GCI — least-squares fit
  of the power-series error model over ≥4 grids; safety factor a
  FUNCTION of observed order and fit standard deviation (derived, not
  magic); robust outside the asymptotic range. [snippet]
- **ASME JVVUQ 8(4):041001, 2023**: URANS solution-verification study
  comparing GCI vs LSQ procedures; finds the LS procedure most reliable
  for discretization uncertainty ON THAT CASE (single-study support,
  not inflated). [snippet]

Adjoint structure / validity domain:
- **Giles & Pierce 2001** (JFM 426:327-345; literature_registry:491-498,
  READ-INTEGRAL): analytic quasi-1D Euler adjoints; log singularity at
  the sonic throat; adopted of record as the first estimator-independent
  oracle. Drives cava §3.25/A36.
- **Lozano & Ponsin 2025** (Aerospace 12(6):494; arXiv:2503.13007):
  characteristic structure of the 2-D adjoint Euler equations —
  compatibility conditions ALONG characteristics, adjoint discontinuities
  across characteristics with jump conditions, analytic supersonic
  adjoints (piecewise constant, smooth across the fan, constant along
  each Mach wave). [abstract read] → the 2025 literature legitimation of
  the in-house "adjoint-invariant drift along the C+" indicator
  mechanism ([X-AKNO], f2 = −λ2).
- **Lozano-Ponsin wall/mesh-divergence line 2022-2023**
  (arXiv:2201.08129; Aerospace 10(5):392): inviscid adjoint singularities
  at walls/trailing edges for subcritical-transonic flows; singularities
  ABSENT and numerical adjoints mesh-converge in supersonic cases —
  supports DWR validity in our marched supersonic domain with the sonic
  strip as the named excluded locus (consistent with cava §3.25).
  [snippets]

Mesh law / marching / in-loop practice:
- **Classical MoC insertion** (Zucrow-Hoffman-era practice; DTIC
  ADA578559 MoC solver doc; ARC R&M 3440): insert/limit characteristic
  spacing during the march, smoothing of point spacing per step — the
  C9 alternative (b) is the field's classical policy; modern MoC nozzle
  papers (e.g. real-gas short nozzles, Appl. Thermal Eng. 2022) still
  march with step-size/spacing control, NOT goal-oriented. [snippets]
- **NASA adjoint-adaptation + optimization practice** (AIAA 2019-3488,
  Cart3D line): shape optimization WITH adjoint-based adapted meshes and
  output constraints — adaptation inside the design loop is modern
  production practice. [snippet]
- **Chen & Fidkowski 2017** ("Airfoil Shape Optimization Using
  Output-Based Adapted Meshes"): optimize on coarse, adapt as the
  optimization proceeds. [snippet]
- **Graded-mesh theory** (a-priori grading near singularities;
  equidistribution with a-priori monitor functions; arXiv:2505.10095
  (2025), IGA grading RICAM rep14-24): a DERIVED spacing law near a known
  singularity recovers smooth-case rates — the theory class behind the
  A36 middle road. [snippets]

### 2.4 Census absences (query-bounded, honest)

- **No DWR-for-space-marching literature found** (Q9): the DWR corpus is
  FE/FV/DG-centric; nearest hits = functional-based adaptation on
  quasi-1D nozzles (arXiv:1511.02188) and Lozano-Ponsin 2025 (theory of
  adjoints ON characteristics, not an estimator). Claim bounded by Q9's
  terms; consequence: the C11 DWR alternative requires an in-house
  FORMULATION step (the characteristic-native form), it is not an
  off-the-shelf adoption.
- **No goal-oriented mesh law for MoC nozzle design found** (Q6+Q9
  intersection): classical spacing control only. The C9 alternative (c)
  transfers doctrine from FE/FV AMR, with the transfer itself part of
  the F2 duty.

### 2.5 Cava rows consumed (RATIFIED corpus, cited per-row)

- **A36** (ADVISORY_litreview_confrontation_2026-08-13.md:1057): derived
  singularity-aware spacing/exclusion policy keyed to the LOCAL MACH
  MARGIN — `log(1/(M²−1))·h³ = const` ⇒ `h ∝ [log(1/(M²−1))]^{−1/3}`,
  ≈1.6× finer in the first strip [INF]; three binding clauses: (i)
  excluded locus restated in Mach-margin form, (ii) refinement-only —
  moving the IVL de-rates O(h²) (the policy's own rejector), (iii) the
  sonic-strip probe is the missing instrument (→ D-49). → C9 option (d)
  and C11's excluded-locus discipline.
- **§3.25** (:679-756): DWR bars re-scoped NOT-uniform-to-the-throat;
  order SAFE, constant ≈4× [INF], gradient IMMUNE (zero design support
  in the strip); the operative in-house indicator does not touch the
  locus (adaptive_knot_optimize.py:16-27 runs kernel→lip, strictly
  supersonic); "the threat is against a FUTURE bar" — i.e. against
  exactly the bar C11's DWR alternative would build. → C11 constraint.
- **R27** (:1154): whether the quasi-1D adjoint-weight growth rate
  transfers to axisymmetric rotational flow is OPEN, non-blocking;
  decided by the [X-GP01] transonic rung (in-house, cost M) or by
  procurement of Giles & Pierce 1997. → named as a C11-duty input, not
  a blocker.

---

## 3. ADJUDICATION (per row)

### 3.0 Shared evidence posture

Phase-B diff of record: C9 = DIVERGENT HIGH, 4/4 AGAINST the uniform
incumbent (phaseB_tree_diff.md:66-72); C11 = DIVERGENT HIGH, 4/4 for
DWR-primary with Richardson demoted to referee, burden of proof
INVERTED onto the incumbent (:76-81). 4/4 blind convergence is
evidence, not a verdict — adjudicated on content below.

Tree advocacy blocks (cited once, shared by both rows):
- **V-F28** phaseA_tree_variational.md:1246-1272 — DWR production +
  hp-tier keyed to the certification map; "O2 [Richardson] at
  checkpoints as the effectivity referee; every safety factor traced to
  the measured effectivity distribution (no magic 1.25)"; falsifier =
  observed effectivity below the derived floor at any checkpoint.
- **H-F26** phaseA_tree_hyperbolic.md:833-850 — DWR primary ("estimates
  the THRUST error directly — matches the certificate need; needs the
  adjoint (have it anyway)"); Richardson/GCI "order-assumption fragile
  at fronts, cheap cross-check with MEASURED observed order"; option (c)
  characteristic truncation-error transport = lens-native, "sharp in
  smooth marching regions, exotic machinery"; falsifier = DWR
  under-predicting true error on oracle problems outside its own stated
  band → disqualified, fall to (b) with budget penalty.
- **H-F27** phaseA_tree_hyperbolic.md:854-870 — mesh policy: (a)
  characteristic-net-native insertion (FF-A) "the classical MoC policy,
  automatically front-aligned"; (e) design-frozen meshes with morphing
  as the DESIGN-LOOP MESH CONTRACT (gradient consistency across design
  steps); falsifier = gradient-verification failures traced to remeshing
  events.
- **O-F24** phaseA_tree_optimization.md:1257-1289 — DWR primary (+
  anisotropic metric only in the capturing tier); "effectivity must be
  MEASURED on a mesh sequence (declared safety factor = measured worst
  effectivity × margin derived from its variance, not a magic 2)";
  Richardson/GCI as THE cross-check ("two independent estimators
  agreeing = the error bar's own certificate"); residual-based rejected
  with stated reason (thrust is a boundary functional); uniform ladders
  kept for the FINAL design; falsifier = effectivity drifting (dual not
  converging) → fitted-tier duals take over near discontinuities.
- **P-F31** phaseA_tree_propulsion.md:1144-1164 — O1 driving + O2
  certifying + O4 (uniform ladders) at champions; per-phase budgets
  μ-weighted into the (v) bar; "front-passage phases will stress it";
  falsifier = measured effectivity outside its band on ANY accepted
  solve voids that solve's bar (per-solve rejector, automated).

### 3.1 Row C9 — march mesh law

**Incumbent case (genuine, represented fully).**
1. *Loop compatibility is real money.* The JAX stack compiles per array
   shape; a mesh law that changes point counts per iterate triggers
   recompilation and breaks the S25/S25-bis record chain economics
   (memory s25/s25-bis of record: record 100.8→32.1 s, then 18×; the
   chain is priced FOR fixed shapes). The uniform-per-run law satisfies
   the H-F27(e) design-loop mesh contract TRIVIALLY: within a run the
   mesh law is frozen, so no remeshing noise ever enters TR acceptance.
2. *The march is already characteristic-aligned.* Columns ARE the C-
   characteristics emitted by wall stations; the "mesh" is not free-form
   placement, and the unit-process stencil radius (2 neighbor columns)
   is what the pre-registered window `d = 2 × coarsest spacing` is
   derived from (o32_mesh_convergence.py:24-39). A four-integer law is
   auditable; certificates of record were issued under it.
3. *The sonic-strip case for adaptation is quantitatively modest.* Cava
   A36's own derived law gives only ≈1.6× finer spacing in the first
   strip [INF] — "greatly increase the grid resolution" (Giles-Pierce
   p.343) is, on this configuration, a small correction, not a regime
   change (cava §3.25(c)).

**Alternatives' case.**
- (b) column-local C- insertion (H-F27(a) advocacy; spec = gapmap AC2,
  RK-G P2-compatible; classical census Q6: standard MoC practice is
  spacing control during the march). Front-aligned by construction, no
  foreign machinery.
- (c) goal-oriented adapted placement (V-F28/O-F24/P-F31 + H-F27(b);
  census Q1/Q3/Q7: output-based adaptation is the modern production
  policy in CFD, including INSIDE optimization loops — NASA AIAA
  2019-3488; Chen-Fidkowski 2017; ML lines 2020-2024). Pays resolution
  only where J cares; the diff's 4/4 challenge.
- (d) A36 derived spacing law: a STATIC, DERIVED, singularity-aware
  grading (census Q8: graded-mesh theory recovers smooth-case rates with
  a-priori monitor functions) — goal-oriented in the derived-weight
  sense WITHOUT feedback machinery; keyed to the local Mach margin,
  frozen within a run (constants depend only on (γ, rtu, yt) — cava
  §3.25(c)), so it also satisfies H-F27(e) trivially.

**Content adjudication.** The 4/4 challenge is SUSTAINED on the target:
"uniform-per-run forever" is indefensible against the census (the whole
modern output-based line exists because uniform refinement pays where
the output does not care) and against the trees' converged doctrine.
BUT the incumbent's production-loop case (shape stability, gradient
consistency, record-chain pricing) is not a strawman — it is exactly
H-F27(e), advocated by the same blind tree that advocates adaptation.
And no census item adjudicates goal-oriented adaptation FOR a
characteristic-marched solver (census absence §2.4) — the transfer is a
build+measure object, precisely the brief's expected shape. The A36
middle road is adoptable NOW because it is derived (R5-clean), static
(loop-safe), and already carries its own rejector (refinement-only,
never move the IVL).

**Stated-reason outcomes (C9):**
- Uniform-per-run: LOSES the target-production-law role (stated reason:
  cost-per-accuracy dominated by goal-oriented placement per census
  Q1/Q7 and 4/4 tree doctrine); RETAINED pro tempore as the
  verdict-bearing certificate law (stated reason: only law satisfying
  the H-F27(e) contract with priced record chain today; certificates of
  record bind to the o32 pre-registered window on uniform families).
- A36 derived spacing law: ADOPTED as a static arm of the current law
  (stated reason: derived not tuned, loop-safe, census-backed by
  graded-mesh theory; its rejector is pinned in the cava row itself).
- Column-local C- insertion: ADOPTED as the ADAPTATION PRIMITIVE for the
  F2 build (stated reason: front-aligned, spec attached AC2, classical
  census support; it is the mechanism by which (c) is realized on a
  marched solver).
- Goal-oriented adapted placement: TARGET production law, adoption
  MEASUREMENT-GATED (stated reason: no census precedent on marched
  solvers; effectivity and gradient-consistency must be measured, per
  all four trees' own falsifiers).

### 3.2 Row C11 — error estimator for J (burden INVERTED: the incumbent defends)

**Incumbent case (genuine, represented fully).**
1. Cheapest honest instrument historically available: +1 solve,
   model-free, applied uniformly across the record; K=4 protects the
   coarse member for any observed p ≥ log2(4/3) = 0.415 (recorded
   arithmetic, findings_registry.yaml:1185) — a 10× conservativeness
   reserve over p=2 asymptotics.
2. Estimator-independence: it needs NO adjoint and NO residual
   definition, so it cross-checks the entire adjoint stack rather than
   sharing failure modes with it (O-F24's "two independent estimators
   agreeing = the bar's own certificate" argument cuts BOTH ways: it
   needs Richardson alive).
3. The repo already upgraded its own weakest point once: [X-O32] exists
   (three-level derived rate estimator, known-answer tested,
   NON-CONCLUSIVE honesty, negative control; o32_mesh_convergence.py:41
   "RATE ESTIMATOR — DERIVED, NOT log2 OF TWO LEVELS") — but only for
   O3.2 norms, not at band sites (the SINGLE-AUTHOR status of record).

**The defense fails as PRIMARY.** The incumbent's own registry convicts
the assumed-order premise at band sites: findings row
`mesh-amr:observed-order-not-at-band-sites` (CONFIRMED, medium) — the
repo's own three-level measurement at the twin was NON-CONCLUSIVE, a
standing counterexample exists where the banded quantity's error GROWS
under refinement, and K_RICH is not conditioned on any observed p.
Census: two-grid-with-assumed-order is the weakest form the V&V canon
sanctions (Roache Fs=3 two-grid vs Fs=1.25 three-grid observed-p; Celik
2008; Eca-Hoekstra 2014 goes further and derives the safety factor from
observed order + fit quality). A fixed K=4 with assumed p=2 is exactly
the "magic constant" class the repo's own discipline (R5) forbids — its
honesty today rests on the 0.415 coverage arithmetic, i.e. on being
enormously conservative, which is paid in bar width.

**Alternatives' case.**
- (iii) DWR (all four trees PRIMARY; census: the entire output-based
  field Q1-Q3): estimates the error IN J directly with an adjoint the
  stack already computes exactly; localizes (thrust is a boundary
  functional — O-F24's stated reason for rejecting non-goal residual
  estimators); modern refined lines active (ML/NN 2020-2024, multigoal
  2024-2025). CONSTRAINTS of record: it is an ESTIMATE, not a bound
  (M0:353-357 already says so; CMAM 2020 states reliability is
  conditional on dual-approximation quality); its validity domain
  excludes the sonic strip (cava §3.25/A36; probe D-49 owed, trigger
  fires on the first DWR-bar claim); and NO census precedent exists on
  a marched MoC solver (§2.4) — the formulation must be built, with the
  in-house bridge already demonstrated ([X-AKNO]: f2 = −λ2 drift =
  adjoint-weighted optimality residual; Lozano-Ponsin 2025 provides the
  modern theory of adjoint compatibility ALONG characteristics that
  legitimates exactly this object).
- (ii) three-mesh observed-p GCI (H-F26(b), O-F24 option 2; census:
  Roache/Celik/ASME V&V 20): discharges the CONFIRMED assumed-order
  defect immediately; the instrument is ALREADY BUILT in-house ([X-O32])
  and its extension to band sites is ALREADY OWNED (GAP-9, findings row
  owner F2 engine window). Cheap-resolvable half.
- (iv) LSQ multi-grid (Eca-Hoekstra 2014; ASME JVVUQ 2023 single-study
  support): the robust rule precisely WHERE our defect lives — noisy /
  non-asymptotic observed order (our twin measurement was NON-CONCLUSIVE
  with dp_tot 0.67); safety factor derived from fit quality = the
  repo's tolerance discipline in published form. Cost ≥4 meshes → not
  an in-loop tool; a checkpoint/fallback tool. (Its per-direction
  variant belongs to C10 — named, not decided here.)

**Content adjudication.** The trees' architecture survives contact with
the census and with the record constraints, with one material
correction: DWR cannot be PRIMARY of record TODAY, because (a) the bar
it would replace must not be voided while D-49's probe is missing and
the effectivity population does not exist (all four trees make measured
effectivity the PRECONDITION of DWR's certificate role — by their own
doctrine DWR starts as candidate, not incumbent), and (b) the
marched-solver formulation is an in-house build (census absence). The
honest converged form is therefore a TWO-INSTRUMENT architecture with a
STAGED primary: observed-p Richardson/GCI carries the verdict-bearing
bands NOW (with the assumed-order premise replaced by measured premises
at band sites = GAP-9), DWR is built as the target primary and takes
the certificate role only on a PASSED effectivity campaign — with
Richardson/GCI permanently retained as the referee (O-F24's
independence argument, and P-F31's per-solve effectivity rejector).
This honors the inverted burden: the incumbent LOSES its unverified
premise immediately (not at F2's leisure), and DWR must EARN
primacy by measurement, not by convergence vote.

**Stated-reason outcomes (C11):**
- Two-level Richardson K=4 with assumed p: LOSES the standalone
  verdict-bearing role (stated reason: CONFIRMED registry defect +
  census — assumed-order two-grid is sub-canon; R5 forbids the magic
  constant once a derived alternative exists in-house). Survives ONLY
  as the in-loop cheap band on quantity-sites holding a MEASURED
  observed-p certificate from the referee ladder (coverage condition
  p_obs ≥ 0.415 of record, re-checked per site).
- Three-mesh observed-p GCI via [X-O32] extension: ADOPTED NOW as the
  interim verdict-bearing band + permanent referee (stated reason:
  discharges the confirmed defect at minimal cost with an instrument
  already built and tested; census-canonical).
- LSQ (Eca-Hoekstra): ADOPTED as the degraded-p rule at checkpoints
  (stated reason: the census-standard treatment of exactly our
  NON-CONCLUSIVE failure mode; not in-loop — cost).
- DWR: TARGET PRIMARY, adoption MEASUREMENT-GATED (stated reason:
  matches the certificate need — error in J itself, adjoint already
  exact; 4/4 tree convergence + modern census; gated by its own
  doctrine's precondition — measured effectivity, D-49 probe, excluded
  locus in Mach-margin form, marched-solver formulation to be built on
  the [X-AKNO]/Lozano-Ponsin mechanism).
- H-F26 option (c) (characteristic truncation-error transport): NOT
  adopted as a separate estimator (stated reason: "exotic machinery"
  per its own advocate; its content — error transported along
  characteristics to the thrust surface — is EXACTLY what the
  characteristic-native DWR form realizes with the adjoint as the
  transport weight, so it merges into the DWR build rather than
  competing with it).

---

## 4. PROPOSED VERDICTS + DUTIES

### 4.1 Row C9 — proposed ledger outcome

**Measurement-gated SPLIT (CONVERGED protocol + F2 measured half).**
Direction converged: goal-oriented, characteristic-native adapted
placement is the TARGET production mesh law (4/4 diff sustained on
content); the uniform-per-run incumbent is DEMOTED to interim
certificate law and is no longer the program's answer to C9.
Adopted now (protocol pins):
1. Uniform-per-run `NI/da/Nw/Ne` remains the verdict-bearing law until
   the F2 campaign passes — no verdict of record moves.
2. The A36 derived spacing law is adopted as a static arm on the first
   strip (refinement-only; constants from (γ, rtu, yt); the IVL is
   NEVER moved — the cava row's own rejector, cited not re-minted).
3. The adaptation primitive of the F2 build = column-local C- insertion
   per the attached AC2 spec (RK-G P2-compatible), driven by the
   characteristic-native goal indicator (f2 = −λ2 drift, owner-array
   attribution — the [X-AKNO] mechanism transferred from knots to march
   columns; the transfer is the hypothesis under test, 41.8%
   localization datum = knot-side prior, not a march-side claim).

**Falsifier pins (exact, what refutes what):**
- **F9a (adaptivity value).** Protocol: same design, same phase set,
  matched total column count (equal unit-process count, the march's own
  cost meter); measure `E_U = |J_uniform+A36 − J_ref|` and
  `E_A = |J_adapted − J_ref|`, `J_ref` from the [X-O32]-verified fine
  ladder with its own band. REFUTES ADAPTATION: `E_A ≥ E_U` (adapted
  fails to beat uniform at matched cost) outside the two bands' joint
  width, on the pre-registered twin sites → C9 CLOSES on
  uniform+A36 and the AMR line is dropped as production law.
  REFUTES THE INCUMBENT-INTERIM: `E_A ≤ E_U/2` twice in a row at
  matched cost (factor 2 = the smallest ratio distinguishable outside
  the joint band at the measured [X-O32] band widths on the twins; if
  the measured bands come in wider, the threshold RISES with them —
  derived, not magic) → adapted law promoted at the next session
  boundary.
- **F9b (gradient consistency = the H-F27(e) contract).** O3.1
  dot-product identity at the adapted mesh must pass at the SAME derived
  floor as on the uniform mesh, and TR acceptance across a re-mesh event
  must show no step rejection attributable to remeshing (H-F27 falsifier
  verbatim: gradient-verification failures traced to remeshing events).
  FIRES → adapted meshes frozen per trust region (fixed topology within
  each TR cycle) or the law stays uniform-per-run.
- **F9c (IVL immobility — cited from A36 clause (ii)).** Any
  implementation in which the mesh law moves the IVL is REJECTED a
  priori: the Mach margin becomes mesh-dependent and de-rates O(h²).

**F2 duty (binding, named): `F2-C9-MESHLAW-CAMPAIGN`** — build the AC2
column-insertion primitive + A36 static arm; run the F9a/F9b protocol
on the pre-registered twin sites; report the measured localization of
the march-side indicator (replacing the knot-side 41.8% prior).
Dependencies named: rides the same adjoint/indicator build as
F2-C11-ESTIMATOR-CAMPAIGN leg (b); feeds nothing into C42.

### 4.2 Row C11 — proposed ledger outcome

**Measurement-gated SPLIT (CONVERGED architecture + F2 measured half),
burden inversion honored.** Architecture converged (the 4/4 direction):
DWR = target primary estimator for the J-bar; Richardson-family =
permanent referee; the incumbent's ASSUMED-ORDER premise is retired
NOW, not at F2's leisure.
Adopted now (protocol pins):
1. Interim verdict-bearing bands at band sites = observed-p
   Richardson/GCI: [X-O32] extended per GAP-9 (third resolution in
   contour_compare, banded quantities covered, NON-CONCLUSIVE
   propagation rule with degraded-p coverage factor — the findings row's
   own owner text, now bound as the C11 measured half's first leg).
2. Two-level K=4 remains usable IN-LOOP only on quantity-sites carrying
   a measured observed-p certificate with `p_obs ≥ 0.415` (the recorded
   coverage bound); any site failing or lacking the certificate falls
   back to the three-mesh band or carries the degraded-p factor.
3. LSQ (Eca-Hoekstra) = the checkpoint rule whenever the observed order
   is NON-CONCLUSIVE (our recorded failure mode); its safety factor is
   taken as published (function of observed p + fit std) — no in-house
   magic replaces it. (Per-direction variant = C10's question — named,
   not decided.)
4. The DWR build = characteristic-native form: per-cell adjoint-weighted
   residual localized via the march topology (owner array), the
   [X-AKNO] f2 = −λ2 mechanism promoted from knot-driver candidate to
   J-bar candidate; census legitimation Lozano-Ponsin 2025 (adjoint
   compatibility conditions along characteristics); excluded locus
   carried in MACH-MARGIN form (A36 clause (i)), never spatial
   stations.
5. D-49 (sonic-strip probe) is a PRECONDITION inside the campaign: the
   findings-row trigger ("the first new DWR-bar claim of record") fires
   the moment the DWR bar exists — the probe must land in the same
   window. R27 (quasi-1D→axisymmetric transfer of the log-weight growth
   rate) stays open and non-blocking; the [X-GP01] transonic rung is the
   in-house resolution lever if the campaign needs the constant.

**Falsifier pins (exact, what refutes what):**
- **F11a (DWR effectivity — the promotion gate).** Protocol: mesh ladder
  (≥3 levels, the [X-O32] ladder) on (i) the Giles-Pierce quasi-1D
  analytic-adjoint oracle (E_true analytic; literature row :491-498
  "adopted as the first oracle") and (ii) the production twin sites
  (E_true from the verified fine-ladder extrapolation ± its band).
  Measure the effectivity population θ_i = η_DWR/E_true. PROMOTE DWR to
  verdict-bearing iff BOTH: θ settles under refinement (no monotone
  drift trend across the ladder — O-F24/P-F31 falsifier: drift = dual
  not converging), AND the derived safety factor
  `S = (min θ)^{-1} × (1 + variance-derived margin)` (the O-F24/V-F28
  formulation; the margin comes from the measured θ spread, no magic
  constant) yields `S × η_DWR` ≤ the matched-cost GCI band on the same
  sites. REFUTES DWR-PRIMARY: θ drifting, or any oracle site with η_DWR
  under-predicting E_true outside its own stated band (H-F26 falsifier
  verbatim) → DWR demoted to ADAPTATION DRIVER ONLY (feeds
  F2-C9-MESHLAW-CAMPAIGN; no certificate value), bands stay
  GCI/LSQ — this outcome still closes C11 (converged, not gated).
- **F11b (referee permanence — per-solve rejector).** After promotion,
  every accepted solve carries the P-F31 per-solve check: measured
  effectivity (DWR vs the referee band at checkpoints) outside its
  population band VOIDS that solve's bar automatically. Richardson/GCI
  is never retired (stated reason: estimator independence — it does not
  share the adjoint stack's failure modes).
- **F11c (excluded-locus honesty).** The DWR bar must DECLARE its
  Mach-margin excluded locus and the D-49 probe result; a DWR-bar claim
  issued without the probe is a live breach of the findings-row trigger
  → the bar is not of record (this pin cites the existing row, no new
  finding minted).

**F2 duty (binding, named): `F2-C11-ESTIMATOR-CAMPAIGN`** — leg (a) =
GAP-9 execution ([X-O32] to band sites + third resolution +
NON-CONCLUSIVE propagation rule; feeds the C42/K_RICH audit, wave 3);
leg (b) = characteristic-native DWR-J bar build + F11a effectivity
ladder + D-49 probe in-window; report the θ population and the derived
S of record. Registration duty riding the same landing (cheap,
navigation-first): literature-registry rows for Becker-Rannacher 2001,
Venditti-Darmofal 2002, Fidkowski-Darmofal 2011, Roache/Celik GCI,
Eca-Hoekstra 2014, Lozano-Ponsin 2025 (arXiv:2503.13007) — WANTED/READ
status per procurement discipline (search-proven absent today, §1.4).

### 4.3 Interplay declared (named, not decided)

- **C42 (K_RICH role reuse, wave 3):** leg (a) of the C11 duty produces
  the observed-p data the C42 audit consumes. No K_RICH role is
  adjudicated here.
- **C10 (refinement operator):** per-direction LSQ/GCI variants touch
  C10's question; this panel's LSQ adoption is scalar-quantity,
  checkpoint-scope only.
- **C27/C28 (wave-1 siblings):** no shared pins; the estimator's bands
  feed the optimizer's error-aware acceptance (V-F30 doctrine) but that
  choice is not this cluster's row.

---

## 5. MACHINE SUMMARY

```json
{
  "cluster": "C9C11",
  "rows": {
    "C9": {
      "proposed": "SPLIT-MEASUREMENT-GATED: 4/4 challenge sustained on content — goal-oriented characteristic-native adapted placement = target production mesh law; uniform-per-run demoted to interim certificate law; A36 derived spacing arm adopted now (refinement-only, IVL immobile); adoption of adapted law decided by pinned falsifiers F9a (matched-cost value, derived threshold), F9b (H-F27(e) gradient-consistency contract), F9c (IVL immobility, cited from A36)",
      "gated": true,
      "duty": "F2-C9-MESHLAW-CAMPAIGN (AC2 column-local C- insertion primitive + A36 arm + F9a/F9b protocol on twin sites; march-side localization datum replaces knot-side 41.8% prior)"
    },
    "C11": {
      "proposed": "SPLIT-MEASUREMENT-GATED, burden inversion honored: assumed-order two-level K=4 retired NOW as standalone verdict-bearing band (registry row mesh-amr:observed-order-not-at-band-sites + census sub-canon); interim bands = observed-p GCI via [X-O32] extension (GAP-9) with p_obs >= 0.415 coverage condition for any in-loop K=4 reuse + Eca-Hoekstra LSQ as degraded-p checkpoint rule; DWR = target primary (4/4), characteristic-native form ([X-AKNO] f2=-lambda2 mechanism, Lozano-Ponsin 2025 legitimation), promotion gated by F11a effectivity ladder (Giles-Pierce oracle + twins, derived safety factor) with D-49 probe precondition and Mach-margin excluded locus; Richardson/GCI referee permanent (F11b per-solve rejector); DWR failure path closes C11 as GCI/LSQ-primary with DWR driver-only",
      "gated": true,
      "duty": "F2-C11-ESTIMATOR-CAMPAIGN (leg a: GAP-9 observed-p at band sites, feeds C42 wave-3 audit; leg b: characteristic-native DWR-J bar + F11a effectivity campaign + D-49 in-window; plus literature-registry registration rows for the DWR/GCI canon)"
    }
  },
  "census_recency": "1997-2025, newest 2025 (Lozano-Ponsin Aerospace 12(6):494 / arXiv:2503.13007; arXiv:2505.10095; multigoal-DWR 2025); modern lines covered: ML goal-oriented adaptation 2020-2024, NN-guided DWR 2021-2022, multigoal DWR 2024-2025, LSQ-GCI V&V 2014-2023 (ASME JVVUQ 2023); histogram pre-2000:2 / 2000s:5 / 2010s:6 / 2020s:12",
  "alternatives_closed": 8,
  "inflation_check": "done"
}
```
