# STAGE A — DIFF JUDGEMENT SP6: GEOMETRY AS DESIGN VARIABLES (representation, admissibility certificates, tolerances, existence)

S-REVIEW 2026-09-05. Judge = record-aware (JPP referee on the decisive number + PM on the shortest credible path).
Inputs read integrally: the four trees `stageA_tree_{variational,hyperbolic,optimization,propulsion}.md`,
`PROBLEM_STATEMENT_agnostic.md`, `DERIVER_BRIEF_agnostic.md`, `INCUMBENT_pointers.md`, the prior de-novo trees
`sfoundations_raws_2026-08-13/phaseA_tree_*_CONDENSED.md` + `phaseB_tree_diff.md`, `st_scoping_number_run.log`.
Record anchors followed into the sources: `docs/choice_ledger.yaml` C1-C8 (:164-248), `docs/rde_nozzle_MASTER.md`
D-DOM :65-72, A_gen :291-330, cone/tip :2450-2476, class ladder :3487-3530, VI.5 :3173-3180, [X-TBAK] block
:3985-4035, F2-B0 block :4250-4299; `docs/claims_registry.yaml` X-AKNO :1290, X-TBAK :1360;
`docs/findings_registry.yaml` :1385 (basis-oscillation-axis-unadjudicated, critical), :1394 (shape-monitors-uncomputed,
critical), :1893 (c6-outcome-i-never-reached); `docs/rde_nozzle_pipeline_decision_map.md` Stage 6 :154-163;
`docs/rde_nozzle_problem_book.md` §5 :337-363; `docs/rde_nozzle_development_plan.md` :905-935 (S20 basis decision),
:214-232 (F3), :1159-1195 (F2.REPR / F3.TOURNAMENT); `validation/sfoundations_raws_2026-08-13/blocco3/PANEL_C1REP.md`
§4.1 and `VERDICT_wave2.md` §4.5-4.7; `validation/TWIN_PROTOCOL_preregistration_2026-08-31.md` §2-§6;
`docs/literature_registry.yaml` (masters_etal_2017 :1057, wanted_kulfan_cst_2008 :1158, wanted_hicks_henne_1978 :1164,
rubino_2018 :579; NO rows for de Boor 1978, Chenais 1975, Bucur-Buttazzo, Delfour-Zolesio, Allaire-Jouve-Toader 2004,
Shadrin/de Boor projector bound — measured grep this window).
Independence caveat of record (LOG-4b) applied: every convergence is weighed MODULO the memory-INDEX exposure; the index
line for the topology census names "cono su Omega/Chenais" and the F3 step is named "F3.TOURNAMENT", so "Chenais" and
"tournament" vocabulary in the trees is NOT counted as derivation unless an argument accompanies it. No memory file was read.

## 0. Incumbent of record (what the trees are judged against)

- Basis/chart: clamped-left (tan thB, C3 DECIDED constructional) / natural-right (C2) interpolating natural cubic spline,
  wall HEIGHTS as dofs; knots uniform in normalized xi re-anchored to live xB (C5) + goal-indicator insertion [X-AKNO]
  (C4 DECIDED survey; carrier FAILING of record, fail=2026-09-05 by construction: outcome II certifiability-limited
  REPRODUCED, crawl path recorder-bound — claims :1292-1294, M0 :4267-4271); insertion-only ratchet (C7), print-only
  dev_warm (C8), mesh-derived degeneracy guard (C6) — all MIXED with named F2 duties.
- C1 (:164) = MIXED, adjudicated-split by a Form-2 panel + refuter 2026-08-19 (PANEL_C1REP §4.1, refute_C1REP,
  VERDICT_wave2 §4.5): DIRECTION CONVERGED to the B-spline CONTROL-POLYGON chart of the SAME certified spline space
  (Bernstein-exact sufficient admissibility certificates); incumbent chart VERDICT-BEARING until F-C1a (mechanism twin on
  the S17 taper/steep-thB failing family), F-C1b (equivalence gate: record J + gradients through the constant chart
  Jacobian at the O3.1 floor on the S18/S24 walk designs), F-C1c (Bernstein certificates pass on record-certified optima
  at derived subdivision depth) pass. Duty F2-C1-CONTROL-CHART-MIGRATION items 0-6 + driver leg; findings :1385 critical.
- Admissible set: A_gen(c) = {S compact solid in E: uniform cone condition (h0, omega); attachment on Lambda; g_i <= c_i}
  with FINITE topology-sector decomposition, configurations = OUTPUTS, working class A_h = spline manifolds in uniform
  C^{1,1} per sector (D-DOM :65-72, :291-294). Existence road P7 = Chenais compactness + S1 continuity (problem book §5
  :355-358, SCHEMA); sector finiteness carries NO rigor class of record (M0 :311-319); cone-vs-sharp-tip DISSOLVED at pin
  level (Omega-side Chenais cone-carrier pin 2026-08-02), record proof pending the census-lemma session (M0 :2460-2476).
- Certified class = ladder A_t(mu_0) with margin floors on the STATE (fold, causality, uniform constants), KKT with the
  margin multiplier (M0 :3487-3506); NAND for a structural reason (M0 :4284-4290); certificates are properties of the
  triple (tree, recorder, env) (M0 :4254-4275).
- As-built tolerance: [X-TBAK] (:1360, PASS re-stamped 2026-09-05): in-class ball maps INTO the dof box because nodal
  evaluation is norm-nonexpansive (THEOREM-level, CHART-SPECIFIC to heights), mean-value bound m(W) - L1_sup*delta
  (THEOREM), measured-sup surrogate L_TB = K_RICH*max(two-point) (PRACTICE), ship gate m(W) >= L_TB*delta, delta a
  DECLARED input, per-class re-derivation mandatory at every tier/class transition (M0 :3996-4022). The record certifies
  the MARGIN under tolerance; it has NO objective-side (near-optimality) tolerance bound.
- Shape monitors (slope positivity, curvature bounds) are COMPUTED NOWHERE (findings :1394 critical, GAP-22): admissibility
  is discovered by paying a march; geometry rejections land as certifiability events.
- TWIN §5: identical constraint vector in both arms incl. truncation fraction (item 3, FIXED), p_b closure (item 4),
  lip/regularity class + margin floors + certification floors (item 5), representation (A-REPR, F2.REPR).

## 1. Table of approaches (schema columns)

| # | approach (tree locations) | from lenses | classification | weight on Q0 | derived or named? | record anchor |
|---|---|---|---|---|---|---|
| A1 | B-spline CONTROL-POLYGON wall r_w(x), control points in a box; slope/curvature by convex-hull / divided-difference bounds (H SP6 (1) :381-393; O P.1 :394-395 + certificates :405-407; P P.2/P.5 :469-472,:479-483; V P.1 listed :394) | H, O, P (V lists, does not recommend) | DIVERGENT vs the verdict-bearing incumbent chart (heights, interpolating); CONFIRM of the record's converged DIRECTION (C1 migration) | medium (cost of the road: the migration campaign is already a binding F2 duty; credibility: certificate exactness enters TWIN §5 item 5) | DERIVED at lemma level (convex-hull property of B-spline derivatives; H, P; O states the control-polygon bound and MEASURES its conservatism); none reaches the record's Bernstein-subdivision exactness gate F-C1c | ledger C1 :164-166; PANEL_C1REP §4.1; VERDICT_wave2 §4.5; findings :1385 |
| A2 | angle-arclength chart theta_w(s), Lipschitz slope; curvature/slope bounds = BOX constraints; derived basis degree (V P.2 :395-398, recommendation :422-424) | V | NEW (no ledger alternative names it; C1 alternatives = B-spline / CST / Hicks-Henne) | low (V itself: "local for the number"); NEGATIVE on cost: nonlinear chart, x(s),y(s) = integrals of cos/sin theta -> length, exit radius, attachment become nonlinear integral equality constraints (V omits this); the march owner-array / station mapping and the chart-invariance argument of the migration are lost | DERIVED (argument present: C^{1,1} by construction, linear certificates for kappa and theta) but the constraint-side cost is not priced | no row; D6 :915-926 rejection axis (conditioning + revalidation) applies with full force |
| A3 | CST / Kulfan class-shape (V P.3 :399; H (2) :382; O P.2 :396 "poorer for plug + free lip"; P P.3 :473) | 4/4 list, 0/4 recommend | CONFIRM-candidate-NAMED of the record's NON-adoption | zero | named only (O gives one stated reason) | C1 alternatives; lit wanted_kulfan_cst_2008 :1158 |
| A4 | Hicks-Henne bumps on a Rao baseline (V P.3 homotopy seeds; H (3) :383; O P.3 :397 REJECTED as primary: "entangled with the comparator (bias)") | V, H, O | CONFIRM-candidate-NAMED of non-adoption; O's comparator-entanglement reason is a NEW stated reason | zero | O: derived (bias argument); others named | C1 alternatives; lit wanted_hicks_henne_1978 :1164 |
| A5 | Level set / topology as OUTPUT (V P.5/X.4 :356-358,:401; H (5)/S14 :249-255 "derivative through a topology change undefined in the piecewise-smooth class"; O P.4/S11 :192-201; P P.4 :474-478) | 4/4 reject for stated reasons | CONFIRM-candidate of the record's FINITE SECTOR TOURNAMENT device + problem-book caution (topological derivative unreliable) | low (F3.TOURNAMENT sits AFTER the decisive TWIN) | DERIVED (H: no design derivative across sector change in class S1 — the problem book :361-363 caution re-derived; O: existence needs perimeter regularization = SCHEMA; V: cut-cell adjoint regularity); "tournament"/"sector" vocabulary NOT counted (index exposure) | M0 :2450-2456; problem book :355-363; M0 VI.5 :3176; D6 :1185-1195 |
| A6 | Configuration as INPUT / enumerated catalogue {bell, plug, shrouded, ED} = hypothesis of the globality claim, price declared (V :420-421; H (6) :385-387; O P.6 :401-402; P P.4 :476-478) | 4/4 | CONFIRM-candidate-NAMED of the record's tournament (the record claims finiteness FROM the cone condition, SCHEMA/no rigor class :311-319; the trees make the catalogue a DECLARED hypothesis — the more honest rung, matching prior diff V-F14) | low | named (finite max over a catalogue is trivial); the enriching increment = "catalogue as declared hypothesis" | M0 :311-319; D6 F3.TOURNAMENT fallback :1193-1195 |
| A7 | Multi-body plug + shroud as two contours, attachment on Lambda, truncation fraction as PARAMETER (O P.5 :399-400; H (6) "truncation fraction as a variable" :386) vs truncation FIXED so the base band drops out at first order (O PB.4 :532-535, P SP9 case 2 :581-584, P SP-PB :636-639) | O, H (variable); O, P (fixed for the decisive run) | CONFIRM-candidate (fixed truncation in the decisive comparison, WITH the derivation dDelta/dp_b = (A_b7 - A_b2)/F); truncation-as-dof = DIVERGENT-minor vs TWIN §5 item 3 (deferred to F3.TOURNAMENT) | medium (touches constraint identity of the decisive experiment and the C61 base band) | DERIVED (O writes the first-order cancellation; P prices A_b/A_e * dp_b -> band_TS) | TWIN §5 items 3-4; ledger C61 (NEVER); problem book §5 (ii) L_p declared; D6 F3 :214-232 |
| A8 | Dof COUNT derived by uniform refinement-to-band: increase d/N/degree until |dJ*| < b_TS/10*F or band (O :403-404, falsifier :416-417; H "Richardson-in-N" :391-393; V degree rejector :397-398; P doubling test :496-497) | 4/4 | DIVERGENT-in-mechanism vs C4 (uniform + GOAL-indicator insertion, Doerfler marking, measured K_RICH stop) — the trees refine GLOBALLY; the record MEASURED that uniform nodes misallocate dofs (41.8% indicator mass in the first interval, M0 :3390-3396) | low (local for the number); positive on credibility of the R-i class: the "design-space refinement study reported like a grid study" (O) is a Verdict row the record lacks; O's "declare best-effort if J still moving at the largest affordable d" = the C38 outcome-II declaration duty (NEVER) with a named trigger | DERIVED (rejector form + band split b_TS/10 derived from the ten-term budget) | ledger C4 :195-204, C7 :227-237, C38; M0 :3344-3346, :3390-3405; X-AKNO :1292 |
| A9 | Physics-derived dof FLOOR: N lower-bounded by the characteristic-reflection scale L/dx_char (H :392-393) / control-point spacing = half the smallest wall-pressure feature length on the mean solution (Nyquist; P :470-472) | H, P | NEW (no row; C4/C6 have no physics floor, only a mesh-derived degeneracy guard) | low | DERIVED (scale argument, no proof) | ledger C6 :217-226 (guard object flip pending); [X-AKNO] insertion at residual-mass median |
| A10 | Existence, DISCRETE half: compact parameter box + continuity of the discrete map on the CLOSED valid set (validity filters are <=-inequalities; margin constraint m(S) >= mu closes the set at separation onset) -> Weierstrass, THEOREM (V :406-409; H :397-399; O :411-413 with the rider "provided the solver converges on the whole box — which it does NOT, non-evaluable points exist"; P :484-487) | 4/4 | CONFIRM-candidate of the record's certified class A_t(mu_0) (closed by margin floors) AND of the certifiability-frontier obstruction (O's rider = the S20/S22/S24 outcome-II history) | low (R-i declaration only; O: "the decisive number does not depend on it") | DERIVED (closedness argument written by V and P; O names the non-evaluable set) | M0 :3487-3506 (ladder, margin multiplier); X-AKNO outcome II; findings :1893; F2-B0 block :4254-4275 (referee rider: the "closed valid set" is recorder-bound near the bound — the discrete existence certificate is a property of the triple) |
| A11 | Existence, CONTINUUM half: uniform-cone / C^{1,1} compactness (Chenais 1975; Arzela-Ascoli), usc of J requires continuous dependence of multi-D Euler entropy solutions on the domain = OPEN, so SCHEMA/CONJECTURE, "the discrete theorem is what ships" (V :410-413; H :399-401; O :413-415; P :487-489) | 4/4 (3/4 name Chenais; O gives Arzela-Ascoli without the name) | CONFIRM-candidate-NAMED of the P7 road (index exposure: "cono su Omega/Chenais" is in the injected index; the compactness half IS argued by V via Arzela-Ascoli, the continuity gap is named identically to the record's S1-continuity requirement) | zero on Q0 | named + partial derivation (compactness); no tree touches the cone-vs-sharp-tip question or sector finiteness | M0 :291-294, :2460-2476; problem book :355-358; prior diff §3.4, §4.8 |
| A12 | As-built tolerance, MARGIN half: attachment/admissibility margin must exceed Lip(g)*delta or ||grad m||_1 delta; a design whose margin is consumed by delta leaves the certified class; delta = declared INPUT of c (V (i) :414-416; H :395-396; P :490-494; O certificate (ii) sampled) | 4/4 | CONFIRM-candidate of [X-TBAK] (mean-value/Hoelder bound, ship gate, delta declared) | low (deliverable (i), not the decisive number) | DERIVED (V, H write the Lipschitz mean-value bound; P adds machining/AM delta priors [KNOWLEDGE: own practice, full] UNVERIFIED) | X-TBAK :1360-1372; M0 :3996-4022 |
| A13 | As-built tolerance, OBJECTIVE half: near-optimality |J(S*+d) - J(S*)| <= ||grad J|| delta + 1/2 ||H|| delta^2 with ||grad J|| <= tau_g at KKT and ||H|| from the reduced Hessian / gradient differences at +-delta; O's linearized worst case |grad J| t_mach <= b_TS/10 F + sampled complement N = 20 (derived 0.88 coverage of the 90th percentile) (V (ii) :416-419; H :394-395; O (i)-(ii) :407-410; P :491-492) | 4/4 | NEW (the record's ship gate is margin-only; no J-side tolerance sensitivity is reported in any Verdict) | low on the decisive number (both TWIN arms are nominal computed designs; the statement's R-iii list has no tolerance term); medium on deliverable (i) "certified design" and on R-i (a KKT point with ||grad J|| <= tau_g is the hypothesis) | DERIVED (second-order Taylor bound; O derives N from the coverage identity 1 - 0.9^20; the 0.88 coverage is weak and the sample is a rejector complement, not a certificate) | none; nearest = X-TBAK (iii) two-point K_RICH pattern; ledger C42 (K_RICH roles) |
| A14 | REFEREE POINT (this judge, from A1 x A12): the tolerance ball placed "in the control points" (O :407-408) is a CHART-DEPENDENT object. [X-TBAK] step (i) maps the physical in-class ball into the dof box by nodal nonexpansiveness — true for HEIGHTS; in the control-polygon chart the forward map c -> p is nonexpansive (partition of unity) but the INVERSE map p -> c carries the sup-norm of the inverse spline collocation/projection operator (a chart constant K_chart >= 1; bounded independently of the knots for the L_inf spline projector [KNOWLEDGE: de Boor's conjecture, proved by Shadrin 2001, abstract] UNVERIFIED — no registry row). Hence L_TB must be re-derived WITH K_chart on migration, or the ball must be declared in physical sup-norm and the box worst case re-proved | judge (NEW) | NEW | medium on the CREDIBILITY of the certified class under the migration (the exact failure mode the brief names: certifiability floors on dofs); zero on the TWIN delta | derived here (one-line argument); the record already MANDATES per-class re-derivation of L_TB (X-TBAK (iv)) but does not name the chart constant | M0 :3996-4005 (step (i)), :4018-4022 (iv); PANEL_C1REP §4.1 item (4) constraint re-map |
| A15 | Admissibility certificates COMPUTED as constraints INSIDE the SQP (attachment exact by interpolation/clamping; envelope by bounds; slope/curvature by control-polygon bounds; conservatism measured) — assumed by 4/4 (V :398; H :388-391; O :405-407; P :480-483) | 4/4 | CONFIRM-candidate of the GAP-22 duty (findings :1394 critical: monitors computed NOWHERE today) — the trees' unanimity makes the duty LOAD-BEARING before the TWIN: §5 item 5 (identical lip/regularity class in both arms) is unverifiable without computed monitors | medium (credibility of the decisive experiment's constraint identity; cost = microseconds per check per GAP-22) | DERIVED (H/P: convex-hull sufficiency; O: conservatism measured by actual extremes) | findings :1394-1403; TWIN §5 item 5; PANEL_C1REP §4.1 items (0),(3),(4) |
| A16 | Left-end attachment by clamping the first control point / interpolation constraint (H :390; O :405; P :482) | 3/4 | CONFIRM-candidate-NAMED of C3 (constructional) | zero | named | ledger C3 :187-193 |
| A17 | Right-end condition: SILENT in all trees (no interpolating spline -> the end-condition dof dissolves) | — | CONFIRM-candidate-NAMED of C2 branch A ("dissolves by structure under migration"); silence is not evidence | zero | not derived | ledger C2 :176-186; VERDICT_wave2 §4.6 |
| A18 | Regularity class C^{1,1} per wetted piece, corners only at the lip and at the plug truncation edge (V :403-405; H "C^2 -> Lipschitz slope" :381; P :483) | V, H, P | CONFIRM-candidate-NAMED of D-DOM working class A_h | zero | named (V adds the design-choice status of the slope bound) | M0 :70-71; problem book :344-345 (dual-bell = same sector, kinked wall) |
| A19 | Seeds: Rao 3-parameter family as warm start + B-spline refinement (P P.1/P.5 :467,:479); Rao 2-parameter family as COMPARATOR/ceiling arm only (V P.6 :402, S0.13) | P, V | CONFIRM-candidate-NAMED of the seed policy (Rao-at-<Pc> bell / peak design plug, "never affecting the certified result") | zero for SP6 (the ceiling arm is SP-CARM's) | named | M0 VI.5 :3177-3180 |
| A20 | MoC-native design variable (exit-characteristic distribution, wall = streamline; H (4)/S9 :189-199) as bell-sector INITIALIZER only; V L0.4 :58-65 proves no common control surface exists across phases (the isoperimetric reduction fails for a multipoint objective) | H (initializer), V (obstruction lemma) | CONFIRM-candidate of the record's choice of wall dofs over the classical control-surface dof (T3/T4 collapse dichotomy; Rao/DEF construction = oracle/tier-1 object, not the design variable) | low | DERIVED (V L0.4 is a short lemma with hypotheses) | M0 :746 ff. [T-T3], :2294 ff. [T-T4]; VI.6 oracle O1; C-EQV2 :1387 |
| A21 | Knot anchoring across thB updates, insertion degeneracy guard, insertion-only ratchet, warm-start deviation (C5-C8) | — | SILENT (below the trees' granularity; the trees refine globally, so no knot mechanics) | zero | — | ledger C5-C8 :205-248 |
| A22 | NURBS (rational weights) named beside B-spline (V P.1, H (1) "B-spline / NURBS", P P.2) | V, H, P | NEW-in-name only; no argument for rational weights (conic exactness is irrelevant to a nozzle wall) | zero | not derived | none |

## 2. Prose reasons with anchors

### 2.1 The basis question (A1, A2): the trees do not rewrite the interface the record fears — except one
The brief's SP6-specific failure mode is that a parametrization flip rewrites the optimizer/adjoint interface and the
certifiability of the design class. Three of four trees (H, O, P) recommend exactly the chart the record's own wave-2
panel converged on (control polygon of a cubic spline space; PANEL_C1REP §4.1). For that chart the record's
CHART-INVARIANCE argument holds: same spline space, conversion = one linear solve, gradients map through a constant
Jacobian (F-C1b), knot insertion is chart-invariant (C4/[X-AKNO] unaffected, §4.1 cross-refs), and the margin floors of
the certified class A_t(mu_0) live on the STATE (fold/causality/per-cell Newton, M0 :3487-3496), not on the dofs. So on the
brief's question the answer is: the majority representation changes NEITHER the adjoint interface (beyond a constant
matrix) NOR the certifiability floors. Two objects ARE chart-dependent and the trees expose both: (a) the admissibility
monitors (A15) — sufficient linear conditions in the control-polygon chart, affine-in-dofs at fixed thB in the heights
chart (GAP-22 :1397-1398) — cheap in both charts but COMPUTED IN NEITHER today; (b) the tolerance-ball dof-box mapping
(A14) — nonexpansive only in the heights chart. The one tree representation that WOULD rewrite the interface is V's
theta_w(s) chart (A2): a nonlinear chart whose wall is an integral of the dofs, which breaks the station mapping the
march's owner array relies on ([X-AKNO] :1294 "attributed to the emitting wall station via the march topology") and turns
L, R_E and attachment into nonlinear integral constraints — V's claim "admissibility certificates become linear" is true
only for kappa and theta and silent on the equality constraints. Classification NEW, weight low, PRUNED for Stage B and
DEFERRED as a C1 rider (trigger: F-C1c exactness gate fails, i.e. Bernstein certificates keep rejecting record-certified
optima at derived depth — then the chart where the curvature bound is EXACTLY a box becomes the fallback of interest).

### 2.2 Delta sweep 2026-09-05 vs the wave-2 panel and the 2026-08-17 trees (done inline; MIXED with a genuine advocate)
C1's adjudication class is MIXED with a Form-2 panel + refuter of 2026-08-19 (a genuine advocate on both sides: D6 :915-926
single-author rejection axis vs the O-F4 Bernstein axis). The inline delta of today's trees against that panel and the
prior trees: (i) the variational lens RETREATED from its 2026-08-17 two-tier level-set discovery tier (V-F13) to "level set
not in budget" (V P.5) — the prior diff's only pro-level-set voice is gone; (ii) O-F4's Bernstein-subdivision exactness
(prior) is WEAKER today (O P.1 says "exact via control-polygon bounds" and then "sufficient, slightly conservative" — an
internal contradiction; the record's F-C1c gate is sharper than any tree); (iii) NEW relative to both: the theta(s) chart
(A2), the physics-derived dof floor (A9), the objective-side tolerance bound (A13), the sampled tolerance complement (A13),
and the fixed-truncation first-order cancellation written out (A7); (iv) P-F19's "analytic Rao spine as cross-check" and
H-F34's sector-structured explicit contour recur unchanged (A19, A6). Nothing in the delta contradicts the migration
direction or its pinned falsifiers; the delta is absorbable as riders to the F2-C1 duty and to X-TBAK's per-class
re-derivation. Consequence: DELTA-SWEEP-ONLY; no Stage-B panel is warranted for SP6.

### 2.3 Dof count and the outcome-II honesty (A8, A9)
All four trees derive the dof count by GLOBAL refinement to a band; the record measured (M0 :3390-3396) that uniform
allocation misplaces dofs (41.8% of the goal indicator in the first interval) and adopted goal-indicator insertion (C4).
On mechanism the trees are the weaker choice; on REPORTING they add something the record lacks: a "design-space
refinement study reported like a grid study" as a Verdict row, with the pre-registered declaration "parametrization-
limited, best-effort" if J still moves at the largest affordable d (O :416-417). The record's actual history is that
refinement hits the CERTIFIABILITY frontier before the parametrization limit (X-AKNO outcome II reproduced 2026-09-05,
:1294; findings :1893 no outcome-I ever reached), so the honest Verdict row today reads "certifiability-limited, not
parametrization-limited" — a distinction the trees do not make and the record's C38 (outcome-II declaration, NEVER)
should carry. Weight low on Q0: the TWIN compares two designs at identical constraints; a shared parametrization limit
cancels to first order in delta but NOT in the R-i class of each arm.

### 2.4 Truncation as dof vs fixed (A7): the trees confirm TWIN §5 with a derivation the record lacks in words
O's PB.4 and P's SP9 case 2 fix the truncation fraction and base radius so that dDelta/dp_b = (A_b,P - A_b,C)/F vanishes at
first order — exactly TWIN §5 items 3-4 — and P prices the alternative: A_b/A_e ~ 0.2-0.4, dp_b ~ +-30% -> +-0.3-1.5% of F =
band_TS itself (P :633-637 [KNOWLEDGE: Hagemann 1998, full] UNVERIFIED-as-number; registry row exists for the paper but the
numbers were not page-verified this window). This is the strongest SP6-side confirmation of the decisive protocol and it
is DERIVED, not named. Truncation as a free dof (H (6), O P.5) belongs to F3.TOURNAMENT, after the TWIN — DEFERRED.

### 2.5 Existence (A10, A11) and the referee rider on "closed valid set"
The discrete existence theorem all four trees ship (compact box x continuous discrete map on a CLOSED valid set) is the
record's A_t(mu_0) class with margin floors, re-derived (P :485-487 closes the set by m(S) >= mu; V :409 by the <=-form of
every filter). O's rider that the solver does not converge on the whole box is the record's certifiability-frontier fact.
The referee rider this judge adds: the record measured (M0 :4254-4275) that binary certification verdicts NEAR THE BOUND
are recorder-bound — so the "closed valid set" of the discrete theorem is itself a property of the triple (tree, recorder,
env); the discrete existence certificate must be quoted WITH the A-1 margin rule (cert_worst <= 1/K_RICH under the pinned
recorder) or it is not a theorem about a fixed set. The continuum half (Chenais/Arzela-Ascoli + the named continuity gap)
is the P7 road named by 3/4; classified NAMED because of index exposure and because no tree goes beyond the citation; the
cone-vs-sharp-tip tension (prior diff §4.8; M0 :2460-2476 pin-decided, proof pending) is untouched by every tree —
DEFERRED to the census-lemma session (R5c, F2-exit).

### 2.6 Tolerances (A12, A13, A14)
Margin half: 4/4 re-derive the Lipschitz/mean-value backoff of [X-TBAK]; CONFIRM with derivation. Objective half: NEW —
the record certifies that the MARGIN survives the ball, not that J does; the trees' second-order bound with ||grad J|| <=
tau_g at a KKT point is cheap (reduced Hessian already required for R-ii) and would give the "certified design" of
deliverable (i) its tolerance sensitivity. Weight on the decisive number is zero (nominal designs on both arms; R-iii
has no tolerance term), medium on deliverable (i). The chart-constant point (A14) is the one SP6 item where a
parametrization flip genuinely touches certifiability: X-TBAK (i) is proved for heights; under the migration L_TB must
carry K_chart (or the ball must be re-declared in physical sup-norm). The record already mandates per-class re-derivation
(X-TBAK (iv)); this judge names the missing constant and asks that item (4) of the migration duty include it.

### 2.7 Adjacent-field prior check (mandatory)
- Turbomachinery steady rotating frame: considered by 4/4 as the time treatment (V L0.1/S0.6; H L1/S4; O L1/S4 [KNOWLEDGE:
  Lakshminarayana 1996; Wang & He 2010, abstract]; P DL-1 [KNOWLEDGE: Paxson 2014; textbook]) — SP0/SP1/SP5 territory;
  for SP6 the relevant adjacent practice is rotating-frame BLADE shape optimization with adjoints (Wang & He 2010 names it):
  no tree carries a blade-parametrization precedent into SP6; no registry row (grep this window) -> [KNOWLEDGE] row K7.
- Harmonic balance / time spectral with adjoints: considered and rejected/dominated by 4/4 (V S0.7; H S5 Gibbs argument;
  O S6; P S-5); registry row rubino_2018 :579 covers the HB-adjoint existence claim; the trees' [KNOWLEDGE: Hall, Thomas &
  Clark 2002; Nadarajah & Jameson; McMullen & Jameson; Gopinath & Jameson; van der Weide 2005] have NO registry rows
  -> UNVERIFIED, entered as K8 (owner SP0/SP1 judges, not SP6).
- Steady adjoint-based shape optimization parametrization practice: Masters 2017 comparison (row :1057, PARTIAL read) is
  the record's dof-budget prior; Kulfan 2008 and Hicks-Henne 1978 are WANTED rows (:1158, :1164); de Boor 1978 (H
  [full]), Chenais 1975 (V/H/P [abstract]), Bucur-Buttazzo, Delfour-Zolesio, Sokolowski-Zolesio (V [full]), Allaire-Jouve-
  Toader 2004 (V [full], O [abstract]) have NO rows -> UNVERIFIED, rows K1-K6 below. Every [KNOWLEDGE] item is a
  procurement row, never evidence.

## 3. Proposed falsifier for Stage B (if the orchestrator opens SP6 despite the DELTA-SWEEP-ONLY recommendation)
The parties must agree on ONE measurement that kills the incumbent chart or the migration: on the recorded S18/S24 walk
designs and the S17 taper/steep-thB failing family, (a) the converted control-polygon chart reproduces record J and maps
gradients through the constant chart Jacobian at the O3.1 derived floor (F-C1b) AND the alternating-curvature statistic of
the failing family sits below the certificate layer's derived floor (F-C1a) AND Bernstein sufficient certificates PASS on
record-certified optima at the derived subdivision depth with the conservatism ratio reported (F-C1c); (b) NEW, from this
judge: the tolerance ship gate re-derived in the new chart (L_TB^cp including the chart constant K_chart) accepts and
rejects the SAME designs as the heights-chart gate at every declared delta of the X-TBAK reference list. (a) firing on
any leg -> incumbent chart stands, migration DEAD on that axis (GAP-21 re-opens); (b) firing -> the certified design class
is chart-dependent and the flip DOES rewrite certifiability (the brief's failure mode confirmed; migration gated on a
re-proof of X-TBAK step (i) in the new chart). Neither outcome moves the TWIN delta; both move deliverable (i).

## 4. Branch ledger rows (every branch seen)
| id | branch | status | reason / trigger + owner |
|---|---|---|---|
| SP6-B1 | B-spline control-polygon chart (A1) | EXPANDED | DIVERGENT vs incumbent chart, CONFIRM of the converged direction; already a binding F2 duty with pinned falsifiers |
| SP6-B2 | angle-arclength theta(s) chart (A2) | DEFERRED | rider to ledger C1 alternatives; trigger = F-C1c exactness gate fails; owner F2-C1-CONTROL-CHART-MIGRATION |
| SP6-B3 | CST / Kulfan (A3) | PRUNED | 0/4 recommend; plug + free lip poorer (O); wanted lit row exists |
| SP6-B4 | Hicks-Henne on Rao baseline (A4) | PRUNED | comparator entanglement (O :397); seeds only |
| SP6-B5 | free-form mesh deformation (V P.4) | PRUNED | poor admissibility certificates (V :400); no tree recommends |
| SP6-B6 | level set / topology as output (A5) | PRUNED | 4/4 stated reasons (no derivative across sector change in class S1; budget); record = finite sector tournament F3.TOURNAMENT |
| SP6-B7 | catalogue as declared hypothesis vs finiteness from the cone condition (A6) | DEFERRED | trigger = census-lemma session R5c (sector finiteness rigor class); owner F2-exit census-lemma |
| SP6-B8 | truncation fraction as dof (A7 variable branch) | DEFERRED | TWIN §5 item 3 pins it FIXED for the decisive run; trigger = F3.TOURNAMENT entry; owner F3 |
| SP6-B9 | truncation FIXED so the base band cancels at first order (A7 fixed branch) | EXPANDED | CONFIRM of TWIN §5 items 3-4 with the derivation dDelta/dp_b written out; cross-link to C61/SP-PB |
| SP6-B10 | dof count by global refinement-to-band (A8) | EXPANDED | DIVERGENT-in-mechanism vs C4; the "design-space refinement Verdict row" + outcome declaration is the enriching increment (C38) |
| SP6-B11 | physics-derived dof floor (A9) | DEFERRED | rider to C6 guard-object edit / next [X-AKNO] touch; owner F2-C6-GUARD-EDIT |
| SP6-B12 | discrete existence on the closed certified set (A10) | EXPANDED | CONFIRM; referee rider on recorder-boundness of the set (A-1 rule) |
| SP6-B13 | continuum existence, Chenais road (A11) | PRUNED | named only, zero weight on Q0; record P7 unchanged |
| SP6-B14 | cone condition vs sharp tip / sharp lip | DEFERRED | untouched by every tree; trigger = census-lemma session (F2-exit, user pin); owner R5c |
| SP6-B15 | tolerance margin backoff (A12) | EXPANDED | CONFIRM of X-TBAK with derivation |
| SP6-B16 | objective-side tolerance bound + sampled complement (A13) | DEFERRED | NEW; rider to X-TBAK next touch (reduced Hessian already required by R-ii); owner F2 certificate stack (VI.6) |
| SP6-B17 | chart constant of the tolerance ball under migration (A14) | EXPANDED | NEW referee point; enters the migration duty item (4) and X-TBAK (iv) per-class re-derivation |
| SP6-B18 | admissibility monitors as SQP constraints (A15) | EXPANDED | CONFIRM of the GAP-22 duty; makes it load-bearing before the TWIN (§5 item 5) |
| SP6-B19 | left-end clamped attachment (A16) | PRUNED | C3 constructional, 3/4 name it |
| SP6-B20 | right-end condition (A17) | PRUNED | dissolves under migration (C2 branch A); trees silent |
| SP6-B21 | regularity class C^{1,1} with corners at lip/truncation (A18) | PRUNED | matches D-DOM A_h; no delta |
| SP6-B22 | Rao-family warm start / ceiling arm (A19) | PRUNED | seed policy of record (VI.5); the ceiling arm is SP-CARM's row |
| SP6-B23 | MoC-native exit-characteristic dof (A20) | PRUNED | V L0.4 obstruction (no common control surface across phases) = T3/T4; initializer role only |
| SP6-B24 | knot anchoring / degeneracy guard / ratchet / dev_warm (C5-C8) (A21) | PRUNED | below the trees' granularity; F2 duties of record unchanged |
| SP6-B25 | NURBS rational weights (A22) | PRUNED | no argument given; irrelevant to a nozzle wall |

## 5. [KNOWLEDGE] rows (identity — why needed — procurement owner); never evidence
- K1 de Boor 1978 "A Practical Guide to Splines" (H [full]): convex-hull / divided-difference bounds on B-spline
  derivatives = the sufficiency half of the admissibility certificates (A1, A15); no registry row — owner: F2-C1 migration
  landing rider (lit registry policy).
- K2 Chenais 1975 uniform-cone compactness (V/H/P [abstract]): P7 existence road; no row — owner: census-lemma session R5c.
- K3 Shadrin 2001 (de Boor's conjecture: L_inf-bounded spline projector, knot-independent constant) [abstract, this judge]:
  the chart constant K_chart of A14; no row — owner: F2-C1 migration item (4) + X-TBAK (iv).
- K4 Allaire, Jouve & Toader 2004 level-set shape optimization (V [full], O [abstract]): prices the declared-out discovery
  tier; no row — owner: F3.TOURNAMENT fallback note (low).
- K5 Bucur & Buttazzo; Delfour & Zolesio; Sokolowski & Zolesio (V [abstract]/[full]): continuum shape-calculus framing of
  A11; no rows — owner: census-lemma session (cite-only unless the continuum theorem is attempted).
- K6 Masters et al. 2017 (row :1057, PARTIAL), Kulfan 2008 (:1158 wanted), Hicks & Henne 1978 (:1164 wanted): COVERED at
  their recorded depth; consume as priors only.
- K7 rotating-frame blade shape optimization with adjoints (O: Wang & He 2010 [abstract]; Lakshminarayana 1996): the
  adjacent-field parametrization precedent for a rotating-frame designer; no row — owner: SP0/SP5 judges / F2.REPR census.
- K8 harmonic-balance / time-spectral adjoints (Hall, Thomas & Clark 2002; Nadarajah & Jameson; McMullen & Jameson 2006;
  Gopinath & Jameson 2005; van der Weide 2005) — only rubino_2018 :579 is on the registry; others UNVERIFIED — owner: SP1
  judge / literature landing.
- K9 P's machining/AM tolerance magnitudes (+-0.05-0.1 mm / +-0.1-0.2 mm) [KNOWLEDGE: own practice, full]: UNVERIFIED;
  X-TBAK's reference list (0.1 mm on throat radii 1 m / 10 cm / 1 cm) is the declared input of record — no procurement
  needed unless a tolerance class becomes a claim.

## 6. Verdict in one paragraph (PM + referee)
SP6 is local for the decisive number by every lens and by the record (TWIN compares nominal designs at identical
constraints). The trees do not move the road: three re-derive the record's own converged migration target, one proposes a
nonlinear chart that would cost the chart-invariance argument. The credible-shortest path is unchanged — F2-C1 migration
with its three pinned falsifiers, plus two cheap riders this diff earns: compute the admissibility monitors before the
TWIN (GAP-22 is load-bearing for §5 item 5) and re-derive the tolerance gate with the chart constant. No Stage-B panel.
