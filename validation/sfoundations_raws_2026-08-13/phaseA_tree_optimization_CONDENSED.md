# CONDENSED (mechanical slice; authority = phaseA_tree_optimization.md, line refs cited)

[L125] **FORK-1 — Relation of J_exact to the computable objective (the
      idealization ladder).**
  *Recommendation.* Optimize J (option 1) as the working objective;
  carry (v) via option 2 evaluated AT CANDIDATE OPTIMA (K-ramp at S*, few
  designs), with option 3 as a single confirmatory run at the final S*.
  Grounds: cost isolation — the expensive rungs price the *bar*, not every
  iterate; HB is the only measuring instrument for the gap at marginal St.
  Optionally, if the K-ramp shows the gap has a stable low-order-in-St
  structure across designs, switch late to option 4 with the measured
  coefficient (then the correction is calibrated, not assumed).

[L187] **FORK-2 — Discretization of the phase average (quadrature over Ξ).**
  *Recommendation.* Option 1, N_ξ chosen by a measured tail criterion:
  double N_ξ until |J_{2N} − J_N| < derived tolerance (FORK-25 chain);
  that difference IS the phase-quadrature carrier for (v). Freeze nodes
  during each outer optimization phase so the discrete objective is a
  FIXED smooth function (no adaptivity noise into the optimizer);
  re-audit nodes at trust-region resets.

[L251] **FORK-3 — Nominal vs robust treatment of μ and H-DATA.**
  *Recommendation.* Option 1 for the certified object, plus option 4's
  margin-hardening on g_sep (a deterministic margin η > 0 derived from the
  measured phase-interpolation error of s(ξ), not a probabilistic model).
  Monitor design (part of the problem per the brief): a cycle-spectral
  residual — project measured/asserted interface data on the single-mode
  rotating-wave ansatz s(θ − 2πft·n); H-DATA monitor statistic = relative
  L² residual + wave-count Fourier concentration; threshold derived from
  the sensitivity |∂J/∂s| (adjoint-based data sensitivity: the SAME
  adjoint fields give ∂J/∂(interface data) for free — use them to convert
  data-residual to objective-error, giving the H-DATA term of (v) an
  evaluable carrier).

[L298] **FORK-4 — Geometry representation family.**
  *Recommendation.* Option 1 (B-spline contours, sector-structured) as the
  certified carrier, with FORK-5 handling topology by enumeration+scout,
  and option 4 as the scout representation. Grounds: only explicit smooth
  contours give simultaneously exact slip-wall solves, provable
  admissibility (spline curvature/angle bounds are computable exactly on
  each polynomial segment — Bernstein-coefficient bounds give SUFFICIENT
  certificates: a Bernstein-form bound on κ(t) over a segment certifies
  the curvature constraint WITHOUT sampling), and a smooth reduced
  objective. This is also the representation with a provable existence
  link (FORK-30): spline classes with bounded control polygons are compact
  in the right topology, and cone conditions can be enforced by linear
  constraints on control points (offset conditions), giving A(c)-membership
  by construction.

[L375] **FORK-5 — Topology handling (sectors as outputs).**
  *Recommendation.* Option 1 as carrier + option 2 as scout. Order:
  scout first (cheap, discovers candidate sector list), then per-sector
  carrier runs. δ reported globally against B, not per sector.

[L422] **FORK-6 — Design-space dimension and adaptive refinement.**
  *Recommendation.* Option 2 driven by option 4's indicator, stopping when
  the indicator falls below the derived tolerance at which further class
  gain is smaller than the (v) error bars (no point refining the design
  space below the noise floor of the objective — see FORK-25 chain).
  Report final ‖(I−Π)G‖ as the "representation residual" carrier in the
  certificate.

[L472] **FORK-7 — Conditioning and regularity of the design map (gradient
      smoothing / metric choice).**
  *Recommendation.* Option 2 with smoothing order matched to a MEASURED
  Hessian symbol (probe the reduced Hessian's action on high-frequency
  shape modes via Hessian-vector products, FORK-23; fit the decay
  exponent; set the smoothing order to flatten it — a derived, not magic,
  smoothing parameter). Option 5's metric aligned with the same H^s.

[L516] **FORK-8 — Imposition of geometric admissibility A(c).**
  *Recommendation.* Hybrid: attachment, symmetry, envelope, length by
  construction (option 1: linear); curvature/angle by option 2 with
  Bernstein sufficient certificates and exchange refinement where the
  sufficient check is too conservative (subdivide the Bernstein form —
  converges to sharp by de Casteljau subdivision, a certified branch-and-
  bound on the constraint itself). Cone condition: enforce via a linear
  sufficient condition on control-point offsets (uniform cone with axis
  data fixed per sector); dry check: a C¹ contour with slope bounded by
  tan ω and minimal feature size ≥ h0 satisfies the (h0, ω) cone condition
  — provable per segment from Bernstein slope bounds.

[L566] **FORK-9 — Solution concept and embedded-discontinuity treatment
      (decides differentiability of everything downstream).**
  *Recommendation.* Two-tier: option 1 (adjoint-consistent capturing,
  option 5 flavor) as the EXPLORATION-tier solver (robust on arbitrary
  intermediate designs), option 2/3 composite as the CERTIFICATION-tier
  solver on candidate optima and final KKT/Hessian verification. The two
  tiers cross-validate (independent-oracle principle): |J_capture −
  J_fitted| at same design is itself a measured model-residual carrier
  for (v).

[L643] **FORK-10 — Per-phase solver architecture and state certification.**
  *Recommendation.* 1 with 3's phase-continuation as the default; 2 as the
  fast path when its validity monitor passes (many nozzle phases will be
  fully supersonic); certification = the declared list in 5.

[L685] **FORK-11 — Non-uniqueness of the per-phase weak solution.**
  *Recommendation.* 1+2 always-on (cheap monitors); 3 at candidate optima
  (rides FORK-1's runs for free); 4 as an early one-off probe and again
  at the final design. If multiplicity found: worst-case-over-branches
  objective for the certificate (declared), option 3's dynamic selection
  for the reported value.

[L728] **FORK-12 — Sonic set / choking treatment.**
  *Recommendation.* 1 for exploration; 2 within certification tier; 3's
  closure declaration mandatory in the data audit regardless.

[L764] **FORK-13 — The separation criterion g_sep: functional form for
      optimization.**
  *Recommendation.* g_sep from option 3 (integral BL margin) as the
  certified criterion — it is the least-magic option whose coefficient
  is a model, not a tuned constant — with option 1 as the cheap in-loop
  proxy during exploration (both computed; proxy calibrated against BL
  margin on the fly: measured offset+slope, giving the proxy a derived
  tolerance). Option 4 at final designs.

[L816] **FORK-14 — Optimize-then-discretize (OD) vs discretize-then-optimize
      (DO) vs dual-consistent both.**
  *Recommendation.* Option 3. Where the certification-tier solver
  (shock-fitted composite) lacks an off-the-shelf dual-consistent
  discretization, enforce dual consistency at the interface conditions
  (R–H internal boundary adjoint conditions derived by hand — the fitted
  analog of adjoint consistency; the continuous derivation of (ii) then
  doubles as the implementation spec). LOAD-BEARING: this fork fixes the
  meaning of every downstream tolerance.

[L863] **FORK-15 — Reduced-space (NAND) vs full-space (SAND / one-shot).**
  *Recommendation.* 1 as backbone, 3's terminal polish adopted if the
  terminal KKT residual (FORK-26) proves expensive to reach by NAND alone.

[L896] **FORK-16 — Optimizer class (the full menu, per the breadth
      requirement).**
  *Recommendation.* Certificate tier: SQP (1) with TR-Newton-CG (3) as
  the terminal phase (multiplier clarity + curvature certificate in one).
  Explorer tier: 8 (≤20-dim sector coarse spaces) seeding 5 (full shape
  space at low fidelity), with 6 as the wrapper wherever hidden
  constraints are dense. All explorer results are SEEDS, never claims.

[L964] **FORK-17 — Globalization and curvature policy.**
  *Recommendation.* 2 + 3 (TR-filter SQP): trust region in the derived
  shape metric, filter instead of penalties, CG-truncated Newton with
  second-order adjoints; radius-update constants DERIVED from the
  measured actual/predicted-reduction statistics (accept thresholds set
  where the measured ρ-histogram separates model-valid from model-broken
  steps — a data-derived, declared constant).

[L996] **FORK-18 — Aggregation of the per-phase separation constraint
      (semi-infinite structure).**
  *Recommendation.* 4 wrapped around 2: exchange method on the true 1-D
  inner problem for exactness, KS within the working set for smoothness;
  inter-node certification via option 1's measured Lipschitz margin.
  Multipliers: the exchange multipliers at convergence approximate the
  measure-valued multiplier of the continuous SIP (the density of the
  binding-phase measure) — this is precisely the "multipliers carrying
  marginal-value meaning" of (ii): dJ/dc_sep = −∫ λ(ξ) d(binding measure).

[L1053] **FORK-19 — Nonsmooth events of the reduced map (activity changes,
      sector boundaries, shock birth).**
  *Recommendation.* 2 as the doctrine (regime cells = certified classes;
  matches FORK-9's fitted-topology bookkeeping), 1 in the explorer.

[L1088] **FORK-20 — Certification boundary as hidden constraint (designs whose
      state cannot be certified).**
  *Recommendation.* 5-first doctrine: derive per-sector sufficient
  solvability conditions (dry-level: for a monotonically expanding
  supersonic sector with wall angles below the Prandtl–Meyer margin to
  vacuum and above the compression-coalescence bound, the marching
  solution exists and is smooth — classical characteristics argument);
  optimize inside; if the optimum is interior, hidden constraints never
  fired and the certificate is clean. Outside the provable region:
  smooth tier with 2's graded violation + 4; explorer with 1/3.

[L1141] **FORK-21 — Derivative computation.**
  *Recommendation.* 1 (with dual-consistent pairing per FORK-14) as
  production; 5 on the fitted tier and 4-with-derived-step on the
  capturing tier as verification; 3 for ξ-tangents; 6 for curvature.

[L1187] **FORK-22 — Derivative verification protocol (the rejector battery).**
  [NO-REC-MARKER]

[L1222] **FORK-23 — Second-order machinery for certificate (iii).**
  *Recommendation.* 1 for in-flight and the certificate; 2 once at S*
  if n permits (also feeds FORK-28's local-globality radius). Active
  tangent cone assembled from the SQP active set with multiplier
  sign-checks (strict complementarity verified numerically; if
  degenerate multipliers appear, report the weak-(iii) form on the
  critical cone — declared).

[L1257] **FORK-24 — Mesh/estimator policy for objective error bars.**
  *Recommendation.* 1 (+5 in capturing tier), cross-checked by 2 at
  candidate optima and by 4 at the final S*. Per-phase bars combined into
  the J-bar by the quadrature weights (plus FORK-2's phase-truncation
  term) — the (v) "discretization error" carrier is the weighted sum
  with measured effectivity band.

[L1293] **FORK-25 — The tolerance chain (every tolerance derived).**
  [NO-REC-MARKER]

[L1332] **FORK-26 — Outer stopping and the KKT certificate number.**
  [NO-REC-MARKER]

[L1345] **FORK-27 — Assembly of the (v) error bar (named carriers).**
  [NO-REC-MARKER]

[L1368] **FORK-28 — The globality mechanism: computing δ (requirement (iv)).**
  *Recommendation.* Option 1 with refinements (a),(b): δ = B_refined −
  J[S*], each term carrying its own (v)-style bar. Report option 5's
  evidence separately. Where structure permits δ = 0 (the brief's ask):
  only in degenerate sub-cases (e.g. if the envelope permits full ideal
  expansion at every phase and the cone condition admits the ideal
  contour — then S* achieving B within bars proves δ ≤ bars); state
  this as the δ→0 mechanism and its (rare) trigger condition.

[L1470] **FORK-29 — Global exploration layer (evidence generation).**
  [NO-REC-MARKER]

[L1488] **FORK-30 — Existence structure (i) and its discrete shadow.**
  *Recommendation.* 1(b) NOW (finite-dimensional certificate,
  unconditional) + 1(a) as the theory target, with the FORK-6 indicator
  quantifying what the subclass certificate leaves on the table.

[L1527] **FORK-31 — Surrogates and multifidelity management (in-loop use).**
  [NO-REC-MARKER]

[L1549] **FORK-32 — Warm starts, continuation, and the outer loop schedule.**
  [NO-REC-MARKER]
