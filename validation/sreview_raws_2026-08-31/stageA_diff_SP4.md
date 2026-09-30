# STAGE A — DIFF JUDGEMENT, SP4: SEARCH STRATEGY, GUARANTEE CLASS, HANDLING OF THE CERTIFICATION BOUNDARY (S-REVIEW 2026-09-05)

Judge: SP4 diff judge (NOT agnostic; persona = JPP referee on the decisive number + PM on the shortest credible path).
Inputs read integrally: the four de-novo trees `stageA_tree_{variational,hyperbolic,optimization,propulsion}.md`
(614/587/599/709 lines), `PROBLEM_STATEMENT_agnostic.md`, `DERIVER_BRIEF_agnostic.md`, `INCUMBENT_pointers.md`
(every SP4 anchor followed into `docs/choice_ledger.yaml`, `docs/rde_nozzle_MASTER.md`,
`docs/rde_nozzle_pipeline_decision_map.md`, `validation/f2b0_raws_2026-08-31/VERDICT_engine_cluster_2026-08-31.md`,
`validation/TWIN_PROTOCOL_preregistration_2026-08-31.md`, `docs/rde_nozzle_development_plan.md` G2, the three
obstruction logs, `docs/findings_registry.yaml`, `docs/literature_registry.yaml`), the prior de-novo evidence
(`sfoundations_raws_2026-08-13/phaseA_tree_*_CONDENSED.md` SP4 forks + `phaseB_tree_diff.md`), the measured
scoping number `st_scoping_number_run.log`, and the same-window `RED_TEAM_decisive_number.md` RT-8 / `LEVERS_F1-F6_draft.md` F2-M3.
Memory files: NOT read (LOG-4b). Tree locations are cited as `<lens>:<line>` of the tree files.

INDEPENDENCE CAVEAT applied (LOG-4b): every convergence below is independent MODULO the memory-index exposure.
One exposure is material for THIS sub-problem: the index carries the token `F3.TOURNAMENT` on the derived critical
path; the hyperbolic tree names "SECTOR TOURNAMENT" verbatim (hyp:254) and the optimization tree "topology by
TOURNAMENT" (opt:201, :401). Both trees DERIVE the construct (level-set derivative undefined across a topology
change → enumerate a finite catalogue; hyp:252-255, opt:198-201, :401-402), so the convergence is a genuine
CONFIRM-candidate, but the word choice is flagged as exposure-suspect and the row is weighted as derived-with-caveat.

## 1. THE INCUMBENT OF RECORD (SP4), with adjudication class per axis

| axis | incumbent of record | ledger status | adjudication class |
|---|---|---|---|
| closer | segmented TR-Newton at measured curvature; engine scipy trust-constr IP path (C31 :481); TR-SQP on spline dofs, Riesz metric, active set, multipliers as marginal values (M0 VI.5 in :3052-3200) | C31 MIXED | DECIDED-genuine-advocate (wave-2 PANEL_C31TRIO; F2-B0 V-C31 spec emended) |
| architecture | NAND reduced-space; STRUCTURAL reason = block-triangular march Jacobian, certificates defined on converged states (M0 :4250-4299; V-C60 :58-100) | C60 MIXED | DECIDED-genuine-advocate (Form-2 advocate+refuter, 2026-08-31/09-05) |
| exploration | local-only (every recorded walk = continuation/warm start); M4 deflated continuation + sector tournament = DECLARED apparatus, never executed (C57 :771; V-C57 :101-123; M0 :2994-3005 M1-M5) | C57 MIXED | DECIDED-genuine-advocate on the closer; the PARADIGM (certificate-first vs exploration-first) = DECLARED-AXIOLOGY by the row's own words, with a user-ratified pilot decided at F2.REPR (REF-13) |
| certification boundary | ledger: binary outside gates (C28 :450 incumbent); M0: tier ladder + KKT with the margin multiplier, KS-max hybrid (M0 :3487-3560; C28 note wave-1) | C28 MIXED, C27 MIXED | panel-adjudicated representation; MEASURED half open — and never binding to date (see §4) |
| record-failure policy | full record then P4 gate = certify-then-accept (C23 :399) | C23 DECIDED | constructional |
| outcome-II declaration | ratchet exhaustion + raw KKT-open number (C38 :557) | C38 NEVER | NEVER |
| tolerances | TR floor/caps, xtol literal 1e-10 (C34 :516, C35 :526) | MIXED | derivation duties open |

Overall incumbent class for the schema: MIXED (DECIDED-with-advocate on closer/NAND/local-closer; DECLARED-AXIOLOGY
on the boundary paradigm; NEVER on C38). Obstruction history of record, verified in the logs: S20 boundary crawl
(certdiag 8/8 genuine stalls, K_disc bridge = CONJECTURE, S20 :77-78); S22 campaign 1/2 = certifiability-limited-
under-constraint, margin INACTIVE, 0 active lanes, mu = 0 identically on the ladder, branch (c) unanimous, K_disc ~
A_0 bridge FALSIFIED (S22 :77-80); S24 F1b twin = F4 fired, margin INACTIVE (min DE val 33x above the floor), third
instance of the class-construction mechanism, +0.51% in-class datum with band caveat (S24 :109-110). No certified
outcome-I optimum exists on any sector; the binary cert verdicts of cert-marginal designs are recorder/version-bound
(M0 :4254-4271; findings :319; TWIN A-1 :150-162).

## 2. TABLE OF APPROACHES (every SP4 approach proposed by any tree)

| id | approach | from lenses (tree location) | derives or names | classification | weight on Q0 | changes credibility / cost | record anchor |
|---|---|---|---|---|---|---|---|
| A1 | Local gradient-based TR-SQP / quasi-Newton closer, KKT with multipliers reported as marginal values | var:347-349 X.1; hyp:350-351 (1); opt:350 G.1; prop:422-423 X.1 | DERIVES (stopping tolerances derived from gradient band; multiplier semantics stated) | CONFIRM-candidate | medium | credibility: the (R-ii) form the referee checks; cost: none new | M0 VI.5; C31 :481; decision map Stage 6 :132-136 |
| A2 | Reduced-space (NAND) search; one-shot listed, never argued | all four implicitly ("BFGS on the reduced space" opt:350; adjoint-gradient loops); prop:432 X.7 one-shot listed without argument | NAMES only (no tree gives the block-triangularity argument) | CONFIRM-candidate-NAMED | low | none | C60 :807; M0 :4250-4299; V-C60 :58-100 |
| A3 | Guarantee class = local KKT + COMPUTED GAP to an ideal (thermodynamic) upper bound; honest "no global guarantee for anyone" | var:46-56 L0.3 + :360-362 X.6; hyp:38-49 L4 + :353-354 (4); opt:365-369 + L2 screen :26-40; prop:436-440 family-bounded gap | DERIVES (L0.3 proof sketch; L4 pointwise lemma with H1-H5; L2 Jensen bound) | CONFIRM-candidate | high | credibility: (R-i) class with evidence, the bound is also a solver-bug rejector (hyp:498, var:528); cost: post-processing | M0 VI.6 bound-ladder gap; M0 :2994-3005 M1-M5; D6 G2 :775-778; prior diff FORK-25/28/37 |
| A4 | Multistart over configuration seeds + sector TOURNAMENT over the catalogue (bell/plug/shrouded/ED), dispersion statistic reported | var:350-352 X.2; hyp:352 (2) + :249-255 S14; opt:353-355 G.3 + :401 P.6; prop:424 X.2 | DERIVES (topology change breaks the design derivative → finite enumeration; hyp:252-255, opt:198-201) — EXPOSURE FLAG on the word "tournament" | CONFIRM-candidate | medium | credibility: answers RT-8 gap (c) "a local argmax from one start is a property of the start" (red team :256-262, A-8 iii); cost: x(seeds) | M0 VI.5 "sector tournament"; C57 :771 (M4 line, declared never executed); A-8(iii) |
| A5 | Continuation / HOMOTOPY in the inflow modulation amplitude eps (or closure magnitude / Omega) from the mean-state (classical) optimum to the full cycle; yields dS*/d(unsteadiness) | var:353-355 X.3; hyp:355-356 (5); opt:360-361 G.7; prop:430-431 X.6 | DERIVES (4/4; var: "cheap, publishable diagnostic"; opt: "checks L2 numerically") | NEW | medium | credibility: arm C of TWIN §4 becomes the eps=0 endpoint of arm P's path — the delta gets a structural bridge, not two unrelated argmaxes; cost: low (scaled data, same engine) | grep homotopy / continuation-in-amplitude over M0, ledger, D6 = 0 hits (measured this window); nearest: P6 seeds (M0 VI.5), warm starts (C57 incumbent) |
| A6 | Derivative-free / BO / CMA-ES QUARANTINED to exploration: seeds, global cross-check, FALLBACK if adjoint rejectors fire | var:359 X.5 + :161-166 S0.10; hyp:164-173 S7 + :352 (3); opt:163-172 S8 + :356 G.4; prop:155-166 S-7 + :425-427 X.3/X.4 | DERIVES (cost estimates: 10^2-10^3 evals hyp:167; O(10d)-O(50d), d<=~10 opt:167; 30-100 3-D solves prop:159) | CONFIRM-candidate | high | credibility+cost: this IS the record's own named remedy (C57 alternative 1, user-ratified pilot) — 4/4 independent lenses place it exactly where the record does (never the certificate closer) | C57 :771 + V-C57 :101-123; prior diff C31 "quarantined to exploration" |
| A7 | DFO/BO TUNING of the classical comparator's 1-3 free parameters ON THE CYCLE/EXACT evaluator ("tuned practice" = ceiling arm) | var:188-196 S0.13 + :572 K.5; hyp:164-173 S7 role + :529-531 SP-CARM (3); opt:550-554 C.4 (1-D root-find of a thrust-consistent average) | DERIVES (hyp: "removes the objection: the gain is the evaluator's, not the method's") | DIVERGENT | high | credibility: the referee's "why not X" — TWIN §4 arm C is designed blind to the cycle and NOT tuned on it; a competent designer with the evaluator tunes his two knobs; cost: O(10) evaluator runs | TWIN §4 :51-72 (arm C = classical design at mean conditions); M0 :3394/:3558 two-knob test (applied to the design class, not to the comparator) |
| A8 | Global-certificate roads (SDP / moment-SOS / branch-and-bound) REJECTED for a stated reason; B&B only at <=3 params with Lipschitz gap | var:202-204 S0.15; opt:357-358 G.5 ("certifies the wrong object"); hyp:353-354 (4); prop:428-429 X.5 | DERIVES (3/4 reject; prop derives the <=3-DOF limit) | CONFIRM-candidate | low | credibility: confirms SDP-CAND-8 retirement; keeps D7/M5 "certified B&B at 2-4 DOF" as the only global mechanism, declared | M0 :4296-4298 (SDP retired); M0 :3002-3003 M5; V-C57 item 1 |
| A9 | INVALID / UNCERTIFIABLE states inside the search: filter-type feasibility restoration, TR shrink, NEVER a surrogate value, rejection count reported, 3 consecutive failures → point declared non-evaluable and excluded (logged) | var:363-365; hyp:358-362; opt:362-364; prop:433-435 | DERIVES (4/4 same mechanism; no tree derives a QUANTIFIED certifiability margin — the margin they price is the SEPARATION margin) | CONFIRM-candidate of C23 certify-then-accept and of the C28 LEDGER incumbent (binary outside gates); DIVERGENT from the M0 ladder's priced certifiability margin | high | cost: see §4 — this is the posture that produced three exits; credibility: the reported rejection COUNT + non-evaluable declaration are the outcome-II semantics C38 lacks | C23 :399; C28 :450; M0 :3487-3560; C38 :557; C31 arm-B filter (Fletcher-Leyffer / Uno filtersqp) |
| A10 | Multi-fidelity TRUST-REGION MODEL MANAGEMENT: first-order-corrected reduced (per-phase) model with exact-evaluator value corrections, ratio test | opt:351-352 G.2 + :139-161 S7 [KNOWLEDGE Alexandrov et al. 1998-2001, abstract] | DERIVES (thresholds b_TS/3, b_TS derived from a three-way band split, opt:280-282) | NEW | medium | credibility: the reduction error is controlled INSIDE the search rather than measured after (M-RED); cost: an evaluator in the loop — at plug St up to 1.41 (log) the evaluator is wave-frame class ([S-BLITE]), so the cost is road-(h)-conditional | no ledger row; nearest = M-RED campaign row (findings `pipeline:m-red-campaign`), road (h) |
| A11 | DERIVED stopping / KKT tolerance from the gradient band or the thrust-stand band | var:348-349 tau_g from V.2/V.3; hyp:362-363 eta*band/step; opt:370-371 tol_KKT = (b_TS/10)F/scale | DERIVES (3/4) | CONFIRM-candidate of the C34/C35 DERIVATION duties; DIVERGENT from the literal incumbents | low | credibility: a literal 1e-10 is a referee point, not decisive | C34 :516, C35 :526; prior diff C35 CONVERGENT-with-duty |
| A12 | Second-order: reduced-Hessian eigenvalues on the active null space (BFGS / FD-of-gradient at S*) | var:319-321 G.6 + :366-367; hyp:361-362; opt:367-368; prop:437 | NAMES the object; the curvature POLICY (BFGS carry) is C32 territory | CONFIRM-candidate-NAMED | low | none on Q0; touches [P-QNCARRY] | M0 VI.6 reduced-Hessian spectrum; C32 :495 |
| A13 | Outcome semantics for a search that cannot deliver a valid state: "(I) invalid: no number is quoted, the failure is the result" | hyp:493 SP9 (I); opt:363-364; var:365 | NAMES (no B-stationarity / degenerate-cone statement in the 2026 trees, unlike the 2026-08 trees) | CONFIRM-candidate-NAMED of the C38 declaration policy | medium | credibility: the shipped design's class must be declared — to date every record exit is outcome II | C38 :557 NEVER; prior diff C38 CONVERGENT with B-stationarity |
| A14 | Bayesian stopping rule for multistart ("probability of an unfound better basin") | opt:354-355 G.3 [KNOWLEDGE Boender & Rinnooy Kan 1987, abstract] | NAMES (declared PRACTICE by the tree itself) | NEW | low | credibility: gives A-8(iii) ">= 2 starts" a stopping semantics; cost: nil | red team RT-8 A-8(iii) :259-262 |

Rows not proposed by any tree but present in the record (branch ledger only, §8): deflated continuation (M4),
the priced certifiability margin as an ACTIVE constraint (M0 ladder), the F2-C60-HYBRID terminal one-shot polish.

## 3. REASONS PER ROW (anchors)

A1/A2. All four lenses land on the same closer family as the record (TR-SQP / quasi-Newton on the reduced space with
adjoint gradients) and none proposes SAND; the prior 2026-08 trees did the same (phaseB diff :159-164). The
structural NAND argument of record (M0 :4250-4299) is stronger than anything in the trees, which only NAME the
reduced space; hence A2 is NAMED. Two lenses name FILTER-type globalization for invalid steps (var:364 "filter
method"; opt:362 "FILTER-type globalization"): as in the prior diff, this is a challenge to the interior-point half
of C31 (an IP barrier has no native semantics for a failed evaluation) and lands on the already-pinned [P-IPADJ] A/B
arm B (Uno filtersqp preset, C31 note). No new adjudication is owed; the delta-sweep records "no flip on the closer,
IP-vs-filter challenge persists 2/4".

A3. The guarantee class the trees would ship — "local KKT, within computed gap delta of an ideal bound" — is the
record's M0 VI.6 "bound-ladder gap + globality mechanism" and D6 G2's value gate. The trees DERIVE their bound
(var L0.3 via entropy monotonicity + full axial expansion; hyp L4 with a pointwise lemma under H1-H5 and an EXACT
decomposition of J_ceil − J into expansion/divergence/Jensen/entropy defects on the exit surface). The hyp
decomposition (hyp:47-49) is an enrichment: the record's bound ladder (J_ideal, Int-max, integral-flux; M0 :2994-2996)
reports a gap, not a term-by-term loss budget. Weight HIGH on credibility: the referee's (R-i) question is answered by
this row, and the negative answer to Q0 is a one-liner if the practice's gap is below the band (var:55-56, hyp:220-224).

A4. Multistart + catalogue tournament is 4/4 and derived, with the exposure caveat stated above. The record has the
apparatus DECLARED (M0 VI.5; C57 "never executable evidence", REF-12) and the same-window red team already proposes
">= 2 starts for arm P with the spread of J_P as the optimizer-basin row" (RT-8 A-8 iii). The trees add the
dispersion statistic as a REPORTED quantity with no theorem (opt:368-369) — the honest form.

A5 (NEW). No record object is a homotopy in the DATA amplitude: the record's continuation is along the dof ratchet
(warm starts) and P6 seeds (measured grep this window: 0 hits for homotopy / continuation-in-amplitude in M0, the
ledger, D6). The construct matters for the decisive number: arm C (mean-state design) is the eps = 0 endpoint, arm P
the eps = 1 endpoint; the path S*(eps) gives dS*/d eps and turns the twin delta into the integral of a measured
sensitivity rather than the difference of two independent argmaxes. It is cheap (scale the cycle family, re-use the
engine) and it is a rejector of the Jensen-gap screen (opt L2). Weight medium; a Stage-B candidate row for C57/C62's
neighbourhood, owner F3.TWIN opening (instance pin) — it also gives the search a physics-informed start on the plug
sector where no P6-class seed exists (LEVERS F2-M3: plug sensitivity machinery does not exist).

A6. The strongest CONFIRM of this sub-problem: four independent lenses quarantine DFO/BO/evolutionary to exploration,
seeding, global cross-check and FALLBACK-if-the-adjoint-fails, never the certificate closer — precisely the C57
posture (local closer of record + pilot arm). The trees' cost estimates are consistent with the record's post-S25
solve cost (0.116 s, V-C57 item 3): a 10^2-10^3-evaluation DFO run on the cheap tier is minutes, which kills the old
expense objection twice over. Hyp:170-172 and prop:441-442 give the operational falsifier pair that Stage B needs:
"DFO finds J higher than the KKT point by > band → the local optimum is exposed as poor; the KKT design beats DFO's
best at equal budget → DFO is dominated".

A7 (DIVERGENT, high). TWIN §4 arm C = "classical design of the SAME geometry class at the I4 interface (mean
conditions only), built by the SAME engine ... evaluated on the same cycle measure". Three lenses say the strongest
opponent is that design with its 1-3 classical knobs TUNED on the exact/cycle evaluator (hyp:479-484: "this removes
the objection 'the gain is the evaluator's, not the method's'"; var:188-196, :572-577; opt:550-554 thrust-consistent
average by root-find). The search element is SP4's: a derivative-free search over the comparator FAMILY on the
objective of record. The record's precedent is the S19/S20 "two-knob test" (M0 :3394, :3558) — applied to the
program's own design class, not to the comparator. If a 2-3-knob tune of arm C on mu moves Isp_C by more than half
the band, arm C as written is not the strongest opponent and the twin's MATERIAL branch is rigged in the referee's
eyes. Handed to the SP-CARM/SP9 judges with the mechanism; the SP4 falsifier (§6) carries it as a rider.

A8. SDP/moment/B&B: 3/4 reject with reasons that match the F2-B0 retirement of SDP-CAND-8 (M0 :4296-4298); opt:357-358
gives the sharpest reason ("certifies the wrong object: the surrogate"). Prop X.5 keeps Lipschitz B&B at <= 3
parameters = D7/M5 "certified B&B at 2-4 DOF" (M0 :3002-3003). No change.

A9 — the certification boundary. See §4; classification is double-edged by construction: the trees CONFIRM the
ledger incumbent (binary outside gates, C28 :450) and the C23 certify-then-accept policy, and DIVERGE from the M0
ladder by never deriving a quantified certifiability margin. What they add and the record lacks: (i) the REJECTION
COUNT as a reported certificate row (var:365); (ii) the "three consecutive failures at the same point → non-evaluable,
excluded, logged" termination rule (opt:363-364) — an outcome-II declaration semantics C38 (NEVER) does not have.

A10 (NEW). First-order-corrected trust-region model management (opt G.2/S7) is the mechanism by which a reduced
designer rung can be TRUSTED inside the search with the evaluator's corrections, instead of only measured afterwards
(M-RED). No ledger row; the nearest record object is the road-(h) hybrid and the M-RED campaign. Its cost is
conditional on the evaluator's class: with the measured plug St_n up to 1.41 (st_scoping_number_run.log, PLUG CLASS
envelope [0.268, 1.415]; license line "wave-frame / unsteady rung REQUIRED") the evaluator is wave-frame, so A10's
in-loop corrections cost [S-BLITE] marches. Weight medium; Stage-B row only if the ROAD judge selects (h).

A11/A12/A13/A14: low-weight confirmations and one low-weight NEW (A14); anchors in the table.

## 4. THE CERTIFICATION BOUNDARY: TREES vs THE OBSTRUCTION HISTORY (the load-bearing finding of this diff)

1. What the record measured three times (S20 :77-78, S22 :77-80, S24 :109-110): the walk stops at the boundary of
   the DISCRETE certifiable set K of the fitted-march class (non-fold, near-axis class-construction frontier,
   branch (c) unanimous), with the priced margin INACTIVE — mu = 0 identically on every ladder rung, 0 active lanes,
   min val 33x above the tightest floor at S24. The K_disc ~ A_0 bridge that would have made the frontier a
   quantifiable margin is FALSIFIED (S22). The binary verdict at cert-marginal designs is recorder/version-bound
   (M0 :4254-4271). Consequence: the M0 ladder's "price staying in tier 0" has never bound; what binds is exactly
   the Le Digabel-Wild "Known-Unrelaxable-Simulation-NONQUANTIFIABLE" constraint the ladder block itself names
   (M0 :3535-3545) — the optimizer learns pass/fail after paying a march.
2. What the trees do with such a state (A9): reject the step, restore feasibility, shrink the trust region, count
   and log — i.e. what the record's driver does (rejected_designs). Their SP4 alone would produce the same three
   exits. They do NOT solve the obstruction at SP4; they AVOID it by two moves outside SP4 that map onto record rows:
   (a) SP2: a capturing pseudo-time FV design solver has no march-certifiability frontier (its failure modes are
   non-convergence / entropy violation / positivity — different, generally softer boundaries) = the C49 captured
   explorer tier (MIXED); (b) SP4/A6: exploration-first with certification deferred to termination = the C57 pilot
   (user-ratified, execution decided at F2.REPR). The trees are therefore an independent 4/4 re-derivation of the
   record's C49+C57 two-tier remedy, and of nothing beyond it.
3. Why this weighs HIGH on Q0 through the TWIN: the decisive sector is the truncated plug (TWIN §2), whose state
   solve includes the H20 free-plume boundary — named by V-C60 as "the FIRST genuinely iterative outer state solve in
   the program" — and the C61 base closure. The class-construction risk is therefore HIGHER than on the bell, and a
   fourth certifiability-limited exit on arm P would cap the twin at INTERMEDIATE / NON-CONCLUSIVE by construction
   (RT-8: "SMALL can be a class-construction artifact", red team :277-278). The MVE row M3 (LEVERS F2) already makes
   "the search strategy Stage B selects (derivative-free / hybrid)" an alternative deliverable to plug sensitivities.
4. What the trees add that the record should take now, cost ~0: the rejection COUNT and the non-evaluable
   declaration as certificate rows (A9), and the multistart dispersion row (A4 = A-8 iii). Both are reporting
   changes, not engine changes, and both are what C38's outcome-II declaration lacks.
5. The priced-margin representation (C28 hybrid, M0 ladder) is NOT refuted by the trees' silence — but the record's
   own evidence (mu = 0 x3) says it is dead weight at tier 0 unless a design is ever found with the margin ACTIVE.
   The falsifier of §6 makes this a pre-registered outcome instead of an open question.

## 5. 2026 DELTA-SWEEP (performed inline now, for the DECIDED-with-genuine-advocate axes)

The four trees are a 2026-SOTA sweep by construction (open-literature knowledge, four lenses, brief §Level 1 "2026
option space at its genuine best"). Result per DECIDED axis:
- closer (C31 family): 4/4 TR-SQP/quasi-Newton with derived constants; 0/4 propose a different closer class →
  NO FLIP. IP-vs-filter: 2/4 name filter globalization for invalid steps (already the [P-IPADJ] arm B; no new row).
- NAND (C60): 0/4 argue SAND; 1/4 lists one-shot without argument → NO FLIP; the record's structural reason stands
  and its partition falsifier (block-triangularity exhibit) remains the first citation duty (V-C60 item 2).
- local-only closer + exploration quarantine (C57 closer half): 4/4 confirm → NO FLIP on the closer; the exploration
  arm is exactly the pinned pilot → the sweep CONFIRMS the pilot's design, not its result.
- KS aggregation with conservativeness-derived rho (C27): 3/4 derive KS with rho from ln(N)/tolerance (var:292-293
  beta from wall-pressure resolution; hyp:318-319 rho_KS >= ln(N_wall N_phi)/(m/4); opt:307-309) — on the SEPARATION
  margin, not the certification margin; the 2026-08 trees' exchange-method divergence (phaseB :133-141) is NOT
  repeated in 2026-09 → the C27 structure half is re-confirmed; the conditioning axis stays the F2 duty.
- SDP certificate solver: 3/4 reject → retirement confirmed.
delta_sweep_done = true for these axes. NOT swept (not DECIDED): the boundary PARADIGM (declared axiology) and C38.

## 6. PROPOSED FALSIFIER (the one the Stage-B parties must agree on)

PILOT-CB — the certification-boundary pilot, on the S22 certifiability-limited instance of record
(s22_certlim_base + the five rejected designs; both recorders; envfp pinned; equal march budget = the S22 campaign's
14-segment / 498 s budget, scaled by the measured post-S25 solve cost):
- Arm I (incumbent): the segmented TR-Newton certify-then-accept walk of record from the outcome-II base, re-run
  under the closure-aware gate, A-1 margin rule applied.
- Arm E (trees' posture): exploration-first — multistart (>= 2 starts, A-8 iii) + amplitude homotopy from the
  classical seed (A5) driven by a DFO/BO engine at its genuine best on the cheap tier (captured explorer if available,
  else the same march with certification DEFERRED to termination), then ONE terminal certification of the winner
  with margin (cert_worst <= 1/K_RICH under the pinned recorder) and, if it fails, ONE certified back-projection
  (feasibility restoration into K).
Pre-registered outcomes (each must be able to fire):
- K1: Arm E's terminal design certifies with margin AND J_E − J_I > K_RICH |J_M − J_2M| (the registered two-level
  band) → the in-loop certify-then-accept closer is FALSIFIED as the closer for this class (it loses J to a frontier
  it cannot price); the pilot posture becomes the arm-P recipe of TWIN §4 by amendment.
- K2: Arm E's winner fails terminal certification and its certified back-projection lands within the band of J_I →
  the trees' posture is REFUTED at this class; the frontier is class-intrinsic; the incumbent stands and C38 closes on
  this datum with the outcome-II declaration made explicit (rejection count + non-evaluable rule, A9).
- K3 / K3': Arm E's certified design has the margin ACTIVE (mu > 0 on the ladder) → the priced-margin representation
  (C28 hybrid) is vindicated for the first time; margin INACTIVE for a fourth time → the C28 priced hybrid is declared
  dead weight for the tier-0 class and the ladder's role is re-scoped to tier-1 entry only.
Rider (A7, for SP-CARM/SP9): a 2-3-knob DFO tune of arm C on the cycle measure moving Isp_C by > 0.5 x band falsifies
"arm C = strongest opponent" as written in TWIN §4.
Cost: <= 1 session. Scheduling constraint of record: V-C57 item 3 / REF-13 puts execution + priority in the F2.REPR
joint table (with S-5F and the C49 explorer) — Stage B may PRE-REGISTER this design, never execute it.

## 7. ADJACENT-FIELD PRIOR CHECK (mandatory) — [KNOWLEDGE] items, never evidence

| item | considered by the trees? | note |
|---|---|---|
| Turbomachinery steady rotating frame (sector + periodic BC, Coriolis/centrifugal sources) | YES, 4/4 (var L0.1 :15-29, S0.6 :126-135; hyp L1 :15-23, S4 :126-140; opt L1 :14-24, S4 :103-117 [Lakshminarayana 1996; Wang & He 2010, abstract]; prop DL-1 :12-30 [Paxson 2014, abstract]) | record: [T-T0]/[S-BLITE] (M0 :3027-3050), C51 NEVER; NO registry row for the turbomachinery precedents (grep: lakshminarayana/wang_he/denton = 0 hits; paxson rows on disk are 2018/2020/2022, not 2014) |
| Harmonic-balance / time-spectral with adjoints | YES, 4/4, each REJECTED under the pin for a stated reason (var S0.7 :137-143 dominated by rotating-frame steady; hyp S5 :142-151 Gibbs O(1/K) at the data shock; opt S6 :129-137 "= S4 in a Fourier basis"; prop S-5 :132-144 drops an O(1) azimuthal flux) | record: C59 canonical-inside-the-pin; rubino_2018 READ-INTEGRAL (:579), zahr_persson_2016, schotthofer_2024; the HB canon itself (Hall-Thomas-Clark 2002; McMullen/Gopinath-Jameson) has NO row |
| Steady adjoint-based shape optimization (continuous vs discrete adjoint; adjoint at shocks) | YES, 4/4 (var G.1/G.2 :308-315; hyp SP3 :325-338; opt I.3/I.4 :321-324; prop G.3/G.4 :394-398) | record: giles_pierce_2000/2001 READ-INTEGRAL (:507, :516), giles_ulbrich_2010 (:120, :129), nadarajah_jameson_2000 WANTED (:1134) — covered; SP3 judge's territory |
| Mixing-plane / flux-consistent averaging of non-uniform inflow as the competent designer's practice | YES, 2/4 (hyp SP-CARM (2) :528-529 [Denton 1992, abstract]; opt C.2 :546-548 [Cumpsty & Horlock 2006, abstract]; var L0.2(ii) derives it without citation) | record: EAP row kaemming_paxson_2018 (:236); NO Denton/Cumpsty row |
| Multi-fidelity trust-region model management / control variates | YES, 1/4 (opt G.2 :351-352, S7 :139-148 [Alexandrov et al.; Peherstorfer-Willcox-Gunzburger 2018, abstract]) | NO record row; A10 NEW |
| Hidden-constraint handling in simulation-based optimization (Le Digabel-Wild taxonomy) | PARTIALLY: the standard remedy (filter/restoration, non-evaluable point) is used 4/4 without naming the taxonomy | record already cites the taxonomy at M0 :3535-3545; no procurement needed |
| Deflation for distinct stationary points (Farrell-Birkisson-Funke 2015) | NO (0/4) | record: M4 declared apparatus; WANTED row :1229 |
| Filter SQP (Fletcher-Leyffer) as globalization | YES by mechanism, 2/4 (var:364, opt:362) | record: C31 alternative + Uno filtersqp arm B; no dedicated row (grep fletcher = 0) |

## 8. BRANCH LEDGER ROWS (every branch seen; "not analysed" does not exist)

| id | branch | status | reason / trigger + owner |
|---|---|---|---|
| SP4-B1 | local gradient TR-SQP / quasi-Newton closer with KKT + multipliers | EXPANDED | A1; 4/4 confirm; no flip |
| SP4-B2 | NAND vs SAND / one-shot | PRUNED | no tree argues SAND; structural reason of record (M0 :4250-4299); re-entry triggers named at V-C60 (C49/HOIST, RPO tier, H20 free plume at F3.PLUG) |
| SP4-B3 | guarantee class = local KKT + computed gap to an ideal bound | EXPANDED | A3; 4/4 derive; enrichment = hyp L4 loss decomposition |
| SP4-B4 | multistart over seeds + sector tournament + dispersion row | EXPANDED | A4; exposure-flagged word, derived construct; = A-8(iii) |
| SP4-B5 | deflated continuation (M4) | DEFERRED | no tree proposes it; record apparatus never executed; trigger = C57 pilot decision table at F2.REPR (REF-13), owner F2.REPR T3 |
| SP4-B6 | amplitude / closure homotopy from the classical optimum | EXPANDED | A5 NEW; candidate Stage-B row; owner F3.TWIN opening (instance pin) |
| SP4-B7 | DFO / BO / CMA-ES exploration tier, fallback if adjoint rejectors fire | EXPANDED | A6; = C57 pilot arm; PILOT-CB design in §6 |
| SP4-B8 | DFO tuning of the classical comparator's knobs on the cycle evaluator | EXPANDED | A7 DIVERGENT vs TWIN §4; handed to SP-CARM/SP9 with the §6 rider |
| SP4-B9 | SDP / moment-SOS / B&B global certificates | PRUNED | 3/4 reject with reason; SDP-CAND-8 retired of record; M5 B&B at 2-4 DOF stays declared |
| SP4-B10 | evolutionary / population methods as the closer | PRUNED | 4/4 reject (no certificate class); allowed for seeding only (opt:359) |
| SP4-B11 | level-set / topology optimization as the search | PRUNED | out of budget, design derivative undefined across topology change (hyp:252-255, opt:198-201); SP6 territory; replaced by B4 |
| SP4-B12 | invalid-state handling: filter / restoration / TR shrink / count / non-evaluable rule | EXPANDED | A9; the two reporting rows (count, non-evaluable) recommended for immediate landing at C38 |
| SP4-B13 | priced certifiability margin as an ACTIVE constraint (M0 ladder, C28 KS-max hybrid) | EXPANDED (record-only) | trees silent; record evidence mu = 0 x3; pre-registered outcome K3/K3' in §6 |
| SP4-B14 | multi-fidelity TR model management with evaluator corrections | EXPANDED | A10 NEW; conditional on the ROAD judge selecting hybrid (h); owner M-RED |
| SP4-B15 | derived stopping / KKT tolerance | EXPANDED | A11; = C34/C35 derivation duties; low weight |
| SP4-B16 | outcome-II / B-stationarity declaration (C38) | DEFERRED | trigger = PILOT-CB K2 datum or [P-BSTAT]; owner F2 [P-BSTAT]; interim landing of the two reporting rows (B12) recommended now |
| SP4-B17 | Bayesian multistart stopping rule | DEFERRED | A14 NEW, low; trigger = A-8(iii) landing; owner RT-8 amendment landing |
| SP4-B18 | F2-C60-HYBRID terminal full-space polish | DEFERRED | record lever only (V-C60 item 1); no tree; after [P-IPADJ] |
| SP4-B19 | robust / CVaR / epigraph outer search (var S0.12, opt S9) | PRUNED for SP4 | objective-axis road (f); owner SP-OBJ / ROAD judge |
| SP4-B20 | Lipschitz B&B on <= 3 parameters; GP-UCB "family-bounded gap" | PRUNED | subsumed by B9; the GP-UCB gap is PRACTICE class (prop:426), not a certificate — must never be printed as one |

## 9. [KNOWLEDGE] ROWS (identity, why needed, procurement owner) — all UNVERIFIED unless a registry row is cited

1. Hall, Thomas & Clark 2002 (harmonic balance, AIAA J.) + McMullen & Jameson 2006 / Gopinath & Jameson 2005 /
   Nadarajah & Jameson 2007 time-spectral (all [abstract]/[full] in the trees) — why: the trees' rejection of HB under
   the pin is an EQUIVALENCE argument (HB in lab time = rotating-frame steady in a Fourier basis) that should be
   checked against the canon before C59's trigger ever fires; owner: C59 weakened-pin trigger window / literature
   census at F2-entry. (rubino_2018 :579 covers the adjoint-HB machinery claim only.)
2. Alexandrov, Lewis et al. 1998-2001 (first-order corrected trust-region model management) — why: A10 NEW; needed
   only if the ROAD judge selects hybrid (h) with an evaluator in the loop; owner: M-RED campaign owner (F2.M-RED).
3. Peherstorfer, Willcox & Gunzburger 2018 (multi-fidelity survey; control variates) — why: band composition for the
   reduction term if A10 is adopted; owner: M-RED.
4. Jones, Schonlau & Welch 1998 (EGO) + Hansen CMA-ES — why: the C57 pilot's exploration engine "at its genuine
   modern best" must be named before the pilot is designed; owner: C57 pilot design at the F2.REPR joint table.
5. Boender & Rinnooy Kan 1987 (Bayesian stopping for multistart) — why: A-8(iii) ">= 2 starts" needs a stopping /
   dispersion semantics; owner: RT-8 A-8 landing.
6. Fletcher & Leyffer 2002 (filter SQP) — why: the trees' invalid-state handling is filter globalization; the C31 arm-B
   semantics; owner: [P-IPADJ] (no registry row; Uno rows :1089/:1099 cover the preset only).
7. Lakshminarayana 1996 (turbomachinery textbook) + Wang & He 2010 (rotating-frame adjoint) + Paxson 2014
   AIAA 2014-0284 (wave-fixed-frame RDE simulation) — why: adjacent-field precedents for road (d)/[S-BLITE]; owner:
   F2.REPR route-B census (distinct from the paxson rows on disk).
8. Denton 1992 / Cumpsty & Horlock 2006 (mixing-plane, averaging non-uniform flows) — why: the strongest classical
   arm's averaging state (A7); owner: F3.TWIN opening arm-C recipe, cross-listed to the SP-CARM judge.
9. Le Digabel & Wild taxonomy — already cited in the record (M0 :3535-3545); no row needed.
10. Farrell, Birkisson & Funke 2015 — WANTED row exists (:1229); no new row; note only.

## 10. PANEL RECOMMENDATION and the three questions from the SP4 angle

Recommendation: FULL-PANEL, narrowly scoped to ONE axis — the certification-boundary PARADIGM (certify-inside-the-
loop vs explore-then-certify), which the record itself labels DECLARED-AXIOLOGY (C57 note) and which the trees give a
genuine 4/4 rival posture with a cheap measured arm (PILOT-CB, §6). The panel's deliverable is the pre-registration of
PILOT-CB (outcomes K1-K3'), NOT its execution (REF-13 joint clause at F2.REPR). Every other SP4 axis is
DELTA-SWEEP-ONLY / CONFIRM (closer, NAND, gap class, KS structure, SDP retirement) and is discharged in §5. Two
zero-cost reporting rows (rejection count; non-evaluable declaration) and the multistart dispersion row (A-8 iii) can
land without a panel.

q1 (is Q1 the right sharpening of Q0?) — from SP4: Q1 ("design on the cycle family beats design on the mean") is only
meaningful if arm P reaches an outcome-I certified optimum with margin; to date the record has none on any sector
(S20/S22/S24), so the decisive test as posed currently measures the certification frontier of the search, not
"cycle vs mean" (RT-8). Q1 is the right sharpening CONDITIONAL on PILOT-CB K1 or K2 being settled first.
q2 (does Q2 answer Q0?) — Q2 (truncated plug, ~1% Isp) answers Q1 on channel N2 only, and only if SP4 delivers
outcome I with the A-1 margin on the plug sector, whose state solve (H20 free plume, C61 base) is the FIRST genuinely
coupled solve of the program (V-C60): a fourth cert-limited exit caps Q2 at INTERMEDIATE by construction. Otherwise
Q2 answers "the certified class is search-limited on this sector" — a valid, negative, publishable answer to Q0 only
if declared as such (C38).
q3 (separate rungs for designer and evaluator?) — YES from SP4, and with a third separation the trees make explicit:
the SEARCH runs on the cheap designer rung (4/4), the delta is an evaluator-rung property, and the CERTIFICATION of
the search's output is a designer-rung property printed with its own recorder/env triple (A-1) and its own
optimizer-basin row (A-8 iii, A4). Three rows, never one number.
