# FORK LEDGER — the 141 Phase-A de-novo forks, fork-side accounting
# S-FOUNDATIONS-C4 Blocco 2 item (1). Mechanical extraction (Sonnet
# MECHANICAL-EXTRACTION slot). Zero judgment: dispositions below are
# derived purely from tag-matching greps of the three input records
# (phaseB_tree_diff.md, docs/choice_ledger.yaml,
# docs/findings_registry.yaml) against each fork's V-F<n>/H-F<n>/
# O-F<n>/P-F<n> tag. Any case requiring a judgment call is marked
# AMBIGUOUS-FOR-FABLE with candidate anchors listed, never decided.
#
# Method (mechanical, reproducible): `grep -o "[VHOP]-F[0-9]+"` over
# each of the three input files gives every explicit fork citation
# with its line number. Compressed forms in the source text
# (`H-F26/27`, `O-F16/17`, `P-F19/26`) are expanded by hand into their
# two constituent tags (both halves share the same tree-letter
# prefix in every observed instance — a mechanical, not interpretive,
# expansion). COVERED = fork tag found in >=1 of the three files, at
# a location that names/weighs the fork's own recommendation (diff
# §1 ledger-row verdict, diff §2/§3/§4 novel/theory/ambiguity item,
# choice-ledger row note, or findings-registry row magnitude).
# NOT-COVERED = fork tag has 0 hits across all three files.
# AMBIGUOUS-FOR-FABLE = the tag IS found, but the finding itself
# conflicts with another source (see H13).
#
# Disposition legend actually exercised below: COVERED, NOT-COVERED,
# AMBIGUOUS-FOR-FABLE. PARTIAL was NOT assigned to any of the 141
# forks: no source-text instance was found where a FORK's own
# question (as opposed to a ledger ROW's question) is explicitly
# stated as half-covered with a named owner+trigger; ledger-row-level
# PARTIAL verdicts (diff C7/C10/C14/C19/C26/C29) all cite forks whose
# OWN recommendation was fully weighed elsewhere (COVERED), so the
# partiality is a property of the ledger row, not of the fork. This
# is reported as a deviation-worth-flagging in the final report, not
# silently normalized.

## TREE V — variational (34 forks; phaseA_tree_variational_CONDENSED.md)

| fork-id | fork statement | disposition | anchor(s) |
|---|---|---|---|
| V1 | How is J_exact related to the computable objective? | NOT-COVERED | none (grep "V-F1\b" over diff+ledger+registry: 0 hits) |
| V2 | Thrust bookkeeping — which control surface, and how does Pa enter? | COVERED | phaseB_tree_diff.md:229 (§2.1, discrete control-surface-invariance rejector); docs/findings_registry.yaml:1591 (carriers:control-surface-invariance-rejector-missing) |
| V3 | Which statistic of the cycle is optimized? | NOT-COVERED | none (0 hits) |
| V4 | Discretization of the phase space (Ξ, μ). | COVERED | phaseB_tree_diff.md:269,364 (§2.10, phase-quadrature stratification) |
| V5 | The idealization ladder for the state model. | COVERED | phaseB_tree_diff.md:257 (§2.8, swirl first-order mandate — V-F5 "R1s") |
| V6 | Solution concept for the per-phase multi-D Euler state. (HW-2 lives here.) | COVERED | docs/choice_ledger.yaml:672 (C49 note, "V-F6/F27") |
| V7 | Per-phase non-uniqueness of the flow configuration (hysteresis) and the selection principle. | COVERED | phaseB_tree_diff.md:62 (C8, ENRICHING); phaseB_tree_diff.md:114 (C21, ENRICHING); phaseB_tree_diff.md:236 (§2.2); docs/findings_registry.yaml:1600 (engine:flow-branch-selection-unpinned) |
| V8 | Closure where the axial inflow on Γ_d is subsonic. | NOT-COVERED | none (0 hits) |
| V9 | Thermally-perfect γ(T) thermodynamics — exact treatment vs surrogates. | COVERED | phaseB_tree_diff.md:118 (C24, CONVERGENT+ENRICHING); phaseB_tree_diff.md:345 (§3.6, thermo road) |
| V10 | Sonic set / throat treatment. | NOT-COVERED | none (0 hits) |
| V11 | Plume / free-jet boundary ("ambient pressure on free portions"). | NOT-COVERED | none (0 hits) |
| V12 | Separation margin g_sep — which detection model? | COVERED | phaseB_tree_diff.md:300 (§2.15, g_sep = integral-BL margin) |
| V13 | Representation of the solid set S. | COVERED | phaseB_tree_diff.md:28 (C1, DIVERGENT-ENRICHING); phaseB_tree_diff.md:57 (C7, PARTIAL) |
| V14 | Topology sectors — enumerate, or let the representation discover them? | NOT-COVERED | none (0 hits) |
| V15 | Existence framework and its monitored failure boundary. (HW-1 lives here.) | COVERED | phaseB_tree_diff.md:284 (§2.12, existence discrete-shadow split); phaseB_tree_diff.md:337 (§3.4, existence road P7/Chenais) |
| V16 | Encoding the constraint vector c (curvature, angle, envelope, wetted length). | NOT-COVERED | none (0 hits) |
| V17 | Optimize-then-discretize (OtD) vs discretize-then-optimize (DtO). | NOT-COVERED | none (0 hits) |
| V18 | Form of the shape derivative. | NOT-COVERED | none (0 hits) |
| V19 | Differentiability across embedded discontinuities. (HW-3, part 1.) | NOT-COVERED | none (0 hits) |
| V20 | Adjoint construction and the averaged optimality system. | NOT-COVERED | none (0 hits) |
| V21 | Transversality / endpoint conditions. | NOT-COVERED | none (0 hits) |
| V22 | Machinery for the attachment state constraint. (HW-3, part 2.) | NOT-COVERED | none (0 hits) |
| V23 | Aggregation over phases — certifying "μ-a.e." from finitely many phases. | COVERED | phaseB_tree_diff.md:138 (C27, DIVERGENT) |
| V24 | Second-order conditions and their verification. | COVERED | phaseB_tree_diff.md:171 (C32, DIVERGENT); phaseB_tree_diff.md:192 (C38, B-stationarity alternative) |
| V25 | The certified upper-bound mechanism for δ. | COVERED | phaseB_tree_diff.md:339 (§3.5, delta-mechanism/bound ladder) |
| V26 | The global search layer (candidate generation). | COVERED | phaseB_tree_diff.md:60 (C8, ENRICHING) |
| V27 | Discretization of the per-phase state. | COVERED | docs/choice_ledger.yaml:672 (C49 note, "V-F6/F27") |
| V28 | Mesh/refinement policy and error estimation. | COVERED | phaseB_tree_diff.md:69 (C9, DIVERGENT); phaseB_tree_diff.md:78 (C11, DIVERGENT); phaseB_tree_diff.md:206 (C42, CONVERGENT-AGAINST-INCUMBENT) |
| V29 | Derivative computation and its verification battery. | COVERED | phaseB_tree_diff.md:213 (C44, ENRICHING) |
| V30 | Optimizer class and globalization. | COVERED | phaseB_tree_diff.md:163 (C31, CONVERGENT on family) |
| V31 | Stopping criteria and tolerance derivation. | COVERED | phaseB_tree_diff.md:98,101 (C17/C18, CONVERGENT ON THE DUTY) |
| V32 | Handling the certification boundary in the loop. (HW-3, part 3.) | COVERED | phaseB_tree_diff.md:144 (C28, CONVERGENT-WITH-M0/DIVERGENT-WITH-LEDGER, 4/4) |
| V33 | Structure of the unsteady correction bound (requirement (v), HW-4). | NOT-COVERED | none (0 hits) |
| V34 | H-DATA monitoring and the data-admissibility audit. | NOT-COVERED | none (0 hits) |

V tally: COVERED 19, NOT-COVERED 15, AMBIGUOUS-FOR-FABLE 0. 19+15+0=34.

## TREE H — hyperbolic (41 forks; phaseA_tree_hyperbolic_CONDENSED.md)

| fork-id | fork statement | disposition | anchor(s) |
|---|---|---|---|
| H1 | How is J_exact related to computable steady objects? | COVERED | phaseB_tree_diff.md:315 (§3.1, steadification exactness / T-T0 road) |
| H2 | What IS the per-phase steady problem of the surrogate? | COVERED | phaseB_tree_diff.md:319 (§3.1, azimuthal-flux commutator decomposition) |
| H3 | Existence of the time average; bracket policy when the exact flow does not settle to the rotating wave. | COVERED | phaseB_tree_diff.md:244 (§2.4, plume vortex-sheet stability); docs/findings_registry.yaml:1609 (plume:vortex-sheet-stability-unchecked) |
| H4 | Solution class for the per-phase state (THE state-model fork). | COVERED | docs/choice_ledger.yaml:672 (C49 note, "H-F4/F8/F9/F28") |
| H5 | Admissibility and uniqueness selection inside the weak class. | COVERED | phaseB_tree_diff.md:332 (§3.3, certified solution class D2.5/S1 road) |
| H6 | Thermally-perfect gas structure: characteristic thermodynamics. | COVERED | phaseB_tree_diff.md:120 (C24); phaseB_tree_diff.md:129 (C25); phaseB_tree_diff.md:251 (§2.6); docs/findings_registry.yaml:1618 (thermotab:fundamental-derivative-audit-missing) |
| H7 | Swirl in the per-phase state model. | COVERED | phaseB_tree_diff.md:256 (§2.8, swirl first-order mandate) |
| H8 | PDE formulation for computation (per phase). | COVERED | phaseB_tree_diff.md:295 (§2.14, two-instrument twin doctrine); docs/choice_ledger.yaml:672 (C49 note) |
| H9 | Front inventory and per-type fit-vs-capture policy. | COVERED | docs/choice_ledger.yaml:672 (C49 note, "H-F4/F8/F9/F28") |
| H10 | Fitting technology. | COVERED | phaseB_tree_diff.md:290 (§2.13, front-terms in the adjoint designed-in, "H-F10(b)") |
| H11 | Spontaneous shock formation and front-topology change. | COVERED | phaseB_tree_diff.md:189 (C37, ENRICHING) |
| H12 | Contacts, slip lines, entropy layers. | NOT-COVERED | none (grep "H-F12\b": 0 hits) |
| H13 | Front stability certification. | AMBIGUOUS-FOR-FABLE | docs/findings_registry.yaml:1609 (plume:vortex-sheet-stability-unchecked magnitude text explicitly names "H-F3/H-F13") VERSUS phaseB_tree_diff.md:244 (§2.4, the registry row's OWN declared source section, which names only H-F3 and H-F21 — not H13). Candidate readings: (a) H13 is a genuine second anchor (its own recommendation text discusses the same far-plume-decoupling scope as H21); (b) the registry row's citation of H13 is a drift/substitution for H21. Mechanical search cannot adjudicate which; not decided here. |
| H14 | Subsonic patches on Gamma_d: policy + causal-separation audit. | COVERED | phaseB_tree_diff.md:241 (§2.3, causal-separation escalation ladder) |
| H15 | Sonic surface / embedded transonic region treatment. | COVERED | phaseB_tree_diff.md:85 (C12, ENRICHING) |
| H16 | Start-surface placement: the limiting-characteristic rule. | COVERED | phaseB_tree_diff.md:83 (C12, ENRICHING) |
| H17 | Spacelike certification, including the swirl margin. | NOT-COVERED | none (0 hits) |
| H18 | Lip/corner treatment at attachment set Lambda. | COVERED | phaseB_tree_diff.md:41 (C3, CHALLENGED) |
| H19 | Axis r = 0 treatment. | COVERED | phaseB_tree_diff.md:87 (C13, ENRICHING); phaseB_tree_diff.md:375 (§4.7) |
| H20 | Free plume boundary (p = Pa) treatment. | NOT-COVERED | none (0 hits) |
| H21 | Control-surface placement and the plume-decoupling certificate. | COVERED | phaseB_tree_diff.md:230 (§2.1); docs/findings_registry.yaml:1591; phaseB_tree_diff.md:246 (§2.4) |
| H22 | Per-phase BVP well-posedness framework. | NOT-COVERED | none (0 hits) |
| H23 | Solution-class membership certification (the monitor list). | COVERED | phaseB_tree_diff.md:105 (C19, PARTIAL) |
| H24 | The certification boundary inside the optimization loop. | COVERED | phaseB_tree_diff.md:147 (C28, 4/4) |
| H25 | Primary discretization + oracle pairing (concretizing FORK-8). | NOT-COVERED | none (0 hits) |
| H26 | Error estimation for the state and for J. | COVERED | phaseB_tree_diff.md:69 (C9); phaseB_tree_diff.md:79 (C11); phaseB_tree_diff.md:207 (C42); phaseB_tree_diff.md:211 (C43, subpart "H-F26(b)") |
| H27 | Mesh / refinement policy. | COVERED | phaseB_tree_diff.md:69 (C9, compressed citation "H-F26/27") |
| H28 | Captured-fallback differentiability: limiter and flux class. | COVERED | docs/choice_ledger.yaml:672 (C49 note, "H-F4/F8/F9/F28") |
| H29 | Fronts in the derivative/adjoint calculus (THE fidelity fork). | COVERED | phaseB_tree_diff.md:288 (§2.13) |
| H30 | Optimize-then-discretize vs discretize-then-optimize. | NOT-COVERED | none (0 hits) |
| H31 | Gradient mechanics and verification duties. | NOT-COVERED | none (0 hits) |
| H32 | Second-order machinery for requirement (iii). | NOT-COVERED | none (0 hits) |
| H33 | Phase quadrature and aggregation across xi. | COVERED | phaseB_tree_diff.md:266 (§2.10) |
| H34 | Design representation of the solid S. | COVERED | phaseB_tree_diff.md:29 (C1); phaseB_tree_diff.md:336 (§3.4) |
| H35 | Optimality framework: does the classical exit-characteristic reduction survive averaging? | COVERED | phaseB_tree_diff.md:306 (§2.16); phaseB_tree_diff.md:325 (§3.2, Rao-collapse under averaging / T7 road) |
| H36 | Optimizer class and globalization (breadth fork). | COVERED | phaseB_tree_diff.md:162 (C31) |
| H37 | The globality certificate (requirement (iv)). | COVERED | phaseB_tree_diff.md:343 (§3.5); phaseB_tree_diff.md:384 (§4.9) |
| H38 | Separation/attachment constraint g_sep. | NOT-COVERED | none (0 hits) |
| H39 | Error-bar architecture for requirement (v). | COVERED | phaseB_tree_diff.md:201 (C41, CONVERGENT) |
| H40 | Tolerance and stopping derivation (no magic constants). | COVERED | phaseB_tree_diff.md:101 (C17/18); phaseB_tree_diff.md:180 (C35); phaseB_tree_diff.md:208 (C42) |
| H41 | H-DATA monitor design. | COVERED | phaseB_tree_diff.md:278 (§2.11, H-DATA monitor with adjoint-based data-sensitivity carrier) |

H tally: COVERED 31, NOT-COVERED 9, AMBIGUOUS-FOR-FABLE 1. 31+9+1=41.

## TREE O — optimization (32 forks; phaseA_tree_optimization_CONDENSED.md)

| fork-id | fork statement | disposition | anchor(s) |
|---|---|---|---|
| O1 | Relation of J_exact to the computable objective (the idealization ladder). | NOT-COVERED | none (grep "O-F1\b": 0 hits) |
| O2 | Discretization of the phase average (quadrature over Ξ). | COVERED | phaseB_tree_diff.md:268 (§2.10); phaseB_tree_diff.md:363 (§4.3, FFT probe) |
| O3 | Nominal vs robust treatment of μ and H-DATA. | COVERED | phaseB_tree_diff.md:274 (§2.11, H-DATA adjoint-based data-sensitivity carrier) |
| O4 | Geometry representation family. | COVERED | phaseB_tree_diff.md:23 (C1, DIVERGENT-ENRICHING); phaseB_tree_diff.md:36 (C2) |
| O5 | Topology handling (sectors as outputs). | NOT-COVERED | none (0 hits) |
| O6 | Design-space dimension and adaptive refinement. | COVERED | phaseB_tree_diff.md:46 (C4, ENRICHING); phaseB_tree_diff.md:56 (C7, PARTIAL) |
| O7 | Conditioning and regularity of the design map (gradient smoothing / metric choice). | COVERED | phaseB_tree_diff.md:181 (C36, ENRICHING) |
| O8 | Imposition of geometric admissibility A(c). | COVERED | phaseB_tree_diff.md:53 (C6, ENRICHING) |
| O9 | Solution concept and embedded-discontinuity treatment. | COVERED | phaseB_tree_diff.md:294 (§2.14, two-instrument twin doctrine); docs/choice_ledger.yaml:672 (C49 note) |
| O10 | Per-phase solver architecture and state certification. | NOT-COVERED | none (0 hits) |
| O11 | Non-uniqueness of the per-phase weak solution. | COVERED | phaseB_tree_diff.md:237 (§2.2, per-phase branch selection) |
| O12 | Sonic set / choking treatment. | NOT-COVERED | none (0 hits) |
| O13 | The separation criterion g_sep: functional form for optimization. | COVERED | phaseB_tree_diff.md:301 (§2.15) |
| O14 | Optimize-then-discretize (OD) vs discretize-then-optimize (DO) vs dual-consistent both. | NOT-COVERED | none (0 hits) |
| O15 | Reduced-space (NAND) vs full-space (SAND / one-shot). | NOT-COVERED | none (0 hits) |
| O16 | Optimizer class (the full menu, per the breadth requirement). | COVERED | phaseB_tree_diff.md:161 (C31, compressed citation "O-F16/17") |
| O17 | Globalization and curvature policy. | COVERED | phaseB_tree_diff.md:161 (C31, compressed "O-F16/17"); phaseB_tree_diff.md:168,177 (C32/C34) |
| O18 | Aggregation of the per-phase separation constraint (semi-infinite structure). | COVERED | phaseB_tree_diff.md:133 (C27); phaseB_tree_diff.md:196 (C39) |
| O19 | Nonsmooth events of the reduced map (activity changes, sector boundaries, shock birth). | COVERED | phaseB_tree_diff.md:156 (C29); phaseB_tree_diff.md:186 (C37) |
| O20 | Certification boundary as hidden constraint (designs whose state cannot be certified). | COVERED | phaseB_tree_diff.md:106 (C20, ENRICHING); phaseB_tree_diff.md:148 (C28) |
| O21 | Derivative computation. | COVERED | phaseB_tree_diff.md:175 (C33, ENRICHING, "O-F21 item 6") |
| O22 | Derivative verification protocol (the rejector battery). [NO-REC-MARKER in Phase A] | COVERED | phaseB_tree_diff.md:214 (C44, ENRICHING) |
| O23 | Second-order machinery for certificate (iii). | COVERED | phaseB_tree_diff.md:168 (C32); phaseB_tree_diff.md:192 (C38) |
| O24 | Mesh/estimator policy for objective error bars. | COVERED | phaseB_tree_diff.md:69 (C9); phaseB_tree_diff.md:79 (C11); phaseB_tree_diff.md:202 (C42) |
| O25 | The tolerance chain (every tolerance derived). [NO-REC-MARKER in Phase A] | COVERED | phaseB_tree_diff.md:97,100 (C17/18); phaseB_tree_diff.md:180 (C35) |
| O26 | Outer stopping and the KKT certificate number. [NO-REC-MARKER in Phase A] | NOT-COVERED | none (0 hits) |
| O27 | Assembly of the (v) error bar (named carriers). [NO-REC-MARKER in Phase A] | NOT-COVERED | none (0 hits) |
| O28 | The globality mechanism: computing δ (requirement (iv)). | NOT-COVERED | none (0 hits) |
| O29 | Global exploration layer (evidence generation). [NO-REC-MARKER in Phase A] | NOT-COVERED | none (0 hits) |
| O30 | Existence structure (i) and its discrete shadow. | COVERED | phaseB_tree_diff.md:28 (C1, existence-link parenthetical); phaseB_tree_diff.md:282 (§2.12) |
| O31 | Surrogates and multifidelity management (in-loop use). [NO-REC-MARKER in Phase A] | NOT-COVERED | none (0 hits) |
| O32 | Warm starts, continuation, and the outer loop schedule. [NO-REC-MARKER in Phase A] | COVERED | phaseB_tree_diff.md:64 (C8, ENRICHING, "full block") |

O tally: COVERED 21, NOT-COVERED 11, AMBIGUOUS-FOR-FABLE 0. 21+11+0=32.

## TREE P — propulsion (34 forks; phaseA_tree_propulsion_CONDENSED.md)

| fork-id | fork statement | disposition | anchor(s) |
|---|---|---|---|
| P1 | What exact object does the computable objective approximate? | NOT-COVERED | none (grep "P-F1\b": 0 hits) |
| P2 | Where does the quasi-steady per-phase model break at marginal St? | NOT-COVERED | none (0 hits) |
| P3 | Existence of the time-average limit and the liminf/limsup fallback. | NOT-COVERED | none (0 hits) |
| P4 | Objective robustness: deterministic μ vs uncertainty in the data family. | NOT-COVERED | none (0 hits) |
| P5 | Placement of Γ_d: where is "downstream of all heat release" real? | COVERED | phaseB_tree_diff.md:248 (§2.5, Gamma_d placement residual accounting) |
| P6 | Causal separation: nozzle→combustor back-reaction (the contract's weakest premise). | COVERED | phaseB_tree_diff.md:240 (§2.3, causal-separation escalation ladder) |
| P7 | Closure for subsonic-axial patches on Γ_d. | NOT-COVERED | none (0 hits) |
| P8 | Dimensional fidelity of s(ξ): full radial profiles + swirl vs reduced data. | NOT-COVERED | none (0 hits) |
| P9 | Swirl accounting (azimuthal momentum in an axisymmetric design). | COVERED | phaseB_tree_diff.md:256 (§2.8, swirl first-order mandate) |
| P10 | Phase discretization: quadrature over Ξ. | COVERED | phaseB_tree_diff.md:268 (§2.10) |
| P11 | H-DATA violation monitor (mode detection as part of the design). | COVERED | phaseB_tree_diff.md:276 (§2.11) |
| P12 | Per-phase solution class: smooth / fitted fronts / captured weak. | COVERED | phaseB_tree_diff.md:335 (§3.3, certified solution class); docs/choice_ledger.yaml:672 (C49 note) |
| P13 | Sonic region treatment (per phase). | NOT-COVERED | none (0 hits) |
| P14 | Gas model: frozen thermally-perfect γ(T) — where it matters, where it fails. | COVERED | phaseB_tree_diff.md:125 (C24); phaseB_tree_diff.md:253 (§2.7); docs/findings_registry.yaml:1627 (scope-pins:frozen-model-form-bar-at-champions) |
| P15 | Viscous layer and the separation criterion. | COVERED | phaseB_tree_diff.md:301 (§2.15) |
| P16 | Aggregation of the per-phase attachment constraint. | COVERED | phaseB_tree_diff.md:138 (C27) |
| P17 | Topology treatment: emergent vs enumerated sectors. | COVERED | phaseB_tree_diff.md:384 (§4.9, "H-F37/P-F17") |
| P18 | Configuration physics: who should win under cycle-varying inflow, and why. | NOT-COVERED | none (0 hits) |
| P19 | Contour parametrization within a sector. | COVERED | phaseB_tree_diff.md:30 (C1); phaseB_tree_diff.md:308 (§2.16, compressed "P-F19/26") |
| P20 | Plug truncation and base pressure (the Euler-uncertifiable zone). | COVERED | phaseB_tree_diff.md:262 (§2.9) |
| P21 | Lip and attachment treatment on Λ. | COVERED | phaseB_tree_diff.md:39 (C3, CHALLENGED) |
| P22 | Control surface, ambient term, and what counts as nozzle thrust. | COVERED | phaseB_tree_diff.md:93 (C14, PARTIAL); phaseB_tree_diff.md:229 (§2.1); docs/findings_registry.yaml:1591 |
| P23 | Phases outside the certified class inside the average. | NOT-COVERED | none (0 hits) |
| P24 | Optimize-then-discretize vs discretize-then-optimize. | NOT-COVERED | none (0 hits) |
| P25 | Derivative computation and its verification. | NOT-COVERED | none (0 hits) |
| P26 | Structure of the averaged stationarity system (the (ii) deliverable). | COVERED | phaseB_tree_diff.md:197 (C39); phaseB_tree_diff.md:308 (§2.16, compressed "P-F19/26") |
| P27 | Optimizer class and globalization (search mechanics). | COVERED | phaseB_tree_diff.md:163 (C31) |
| P28 | The globality certificate: how δ is actually COMPUTED. | COVERED | phaseB_tree_diff.md:342 (§3.5) |
| P29 | Second-order conditions (iii) in verifiable form. | NOT-COVERED | none (0 hits) |
| P30 | Per-phase discretization scheme. | NOT-COVERED | none (0 hits) |
| P31 | Mesh/refinement policy and error estimators. | COVERED | phaseB_tree_diff.md:69 (C9); phaseB_tree_diff.md:79 (C11) |
| P32 | Tolerance derivation, error budget, and stopping. | NOT-COVERED | none (0 hits) |
| P33 | Handling the certification boundary in the loop. | COVERED | phaseB_tree_diff.md:149 (C28) |
| P34 | Evidence hierarchy for a real engine. | NOT-COVERED | none (0 hits) |

P tally: COVERED 19, NOT-COVERED 15, AMBIGUOUS-FOR-FABLE 0. 19+15+0=34.

## MACHINE SUMMARY (measured this window)

Per-tree fork counts (measured from the condensed tables — highest
FORK-N per tree, cross-checked against title-line count):
- V (variational): 34 (FORK-1..FORK-34)
- H (hyperbolic): 41 (FORK-1..FORK-41)
- O (optimization): 32 (FORK-1..FORK-32; 7 of these carry
  [NO-REC-MARKER] in Phase A: O22, O25, O26, O27, O29, O31, O32 —
  still counted as forks per the brief's arithmetic)
- P (propulsion): 34 (FORK-1..FORK-34)
- TOTAL: 34+41+32+34 = 141. Matches the brief's prior measurement
  (34+41+32+34) exactly — no discrepancy to report.

Disposition tally per tree (|forks| == COVERED + PARTIAL +
NOT-COVERED + AMBIGUOUS-FOR-FABLE):
- V: COVERED 19, PARTIAL 0, NOT-COVERED 15, AMBIGUOUS-FOR-FABLE 0.
  19+0+15+0 = 34. OK.
- H: COVERED 31, PARTIAL 0, NOT-COVERED 9, AMBIGUOUS-FOR-FABLE 1.
  31+0+9+1 = 41. OK.
- O: COVERED 21, PARTIAL 0, NOT-COVERED 11, AMBIGUOUS-FOR-FABLE 0.
  21+0+11+0 = 32. OK.
- P: COVERED 19, PARTIAL 0, NOT-COVERED 15, AMBIGUOUS-FOR-FABLE 0.
  19+0+15+0 = 34. OK.

TOTAL: COVERED 90, PARTIAL 0, NOT-COVERED 50, AMBIGUOUS-FOR-FABLE 1.
90+0+50+1 = 141. Reconciled.

NOT-COVERED id list (50, no fork-tag citation found in any of the
three input files):
- V: V1, V3, V8, V10, V11, V14, V16, V17, V18, V19, V20, V21, V22,
  V33, V34 (15)
- H: H12, H17, H20, H22, H25, H30, H31, H32, H38 (9)
- O: O1, O5, O10, O12, O14, O15, O26, O27, O28, O29, O31 (11)
- P: P1, P2, P3, P4, P7, P8, P13, P18, P23, P24, P25, P29, P30, P32,
  P34 (15)

AMBIGUOUS-FOR-FABLE id list (1):
- H13 (Front stability certification) — findings_registry.yaml:1609
  names "H-F3/H-F13" as the covering evidence for
  plume:vortex-sheet-stability-unchecked, but that row's own declared
  source, phaseB_tree_diff.md §2.4 (line 244), names only H-F3 and
  H-F21, not H13. Candidate anchors: (a) docs/findings_registry.yaml:1609
  (treats H13 as covered — a genuine, content-consistent second
  anchor: H13's own recommendation text discusses the identical
  far-plume-decoupling scope as H21); (b) phaseB_tree_diff.md:244/246
  (§2.4 — names H3/H21 only; H13 may be a drift/substitution for H21
  introduced when the registry row was minted). Not adjudicated here.

## DEVIATIONS FROM THE BRIEF (declared)

1. PARTIAL was never assigned at the fork level (see legend note at
   top of file): the diff's own PARTIAL verdicts (C7, C10, C14, C19,
   C26, C29) are properties of LEDGER ROWS, not of the individual
   forks cited within them — every fork cited under a PARTIAL row
   (O6/V13 at C7; P-F22 at C14; H-F23 at C19; O-F19 at C29) has its
   own recommendation fully weighed elsewhere in the diff, so its
   fork-level disposition is COVERED. This is a measured fact of the
   source material, not an extraction choice: no fork's OWN question
   was found stated as half-covered with a named owner+trigger
   distinct from its ledger row's owner+trigger. Flagged per the
   brief's instruction to report, not force, any deviation.
2. One AMBIGUOUS-FOR-FABLE case (H13) was raised beyond a simple
   found/not-found binary, per the binding AMBIGUITY RULE — see
   above. This is the only fork where the mechanical search itself
   surfaced conflicting evidence about whether an anchor validly
   covers the fork.
3. Compressed multi-tag citations in the source prose
   ("H-F26/27", "O-F16/17", "P-F19/26") were expanded mechanically
   into both constituent tags (same tree-letter prefix carried across
   the slash, the only pattern observed in the corpus) rather than
   left as a single grep hit. Declared since grep alone (without this
   expansion) would under-count H27, O17 as NOT-COVERED.
4. Three tags (V6, V27, H4, H8[dup], H9, H28, O9[dup], P12[dup]) were
   found NOT in phaseB_tree_diff.md but in docs/choice_ledger.yaml's
   C49 note (line 672) instead — C49 is a ledger row minted directly
   at Phase B for the fit-vs-capture solution-representation choice,
   and its note independently lists the four trees' forks at their
   "genuine best" for that choice. This is a valid COVERED anchor
   under the brief's own anchor-type list ("choice-ledger row C<n>"),
   used here because the diff's own §1/§2/§3/§4 text does not
   separately cite these six tags for this content.
