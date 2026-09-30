# STAGE A — DIFF JUDGEMENT, SP-CARM "THE STRONGEST COMPETING PRACTICE" (S-REVIEW 2026-09-05)

Judge: NOT agnostic (record-aware). Persona: JPP referee asking "why not X?" + PM asking "shortest credible
path?". Inputs read integrally: the four Stage-A trees (`stageA_tree_{propulsion,variational,hyperbolic,
optimization}.md`), `PROBLEM_STATEMENT_agnostic.md`, `DERIVER_BRIEF_agnostic.md`, `INCUMBENT_pointers.md`
and every anchor it cites for this sub-problem (M0 [T-T3] :746-800, [T-T4] :2294-2320, EAP/Stechmann remarks
:2526-2600, VI.5-VI.6 :3173-3188; `docs/choice_ledger.yaml` C61 :818-830 + full id/status scan; TWIN protocol
§1-§9; D6 G2 :776-782, Annex B :1142, F3 :214-227, F1b :137-152; `src/thrust/stechmann_nozzle.py` :1-140;
`tests/test_bell_optimality.py`; `validation/bell_optimality_proof.md`; `docs/roadmap_geno_rde.md` :125-145;
`docs/rde_nozzle_problem_book.md` :532-536; hypothesis ledger H-CON :173-178; `st_scoping_number_run.log`;
prior trees 2026-08-17 + `phaseB_tree_diff.md`; literature registry rows named below). Memory files NOT read
(LOG-4b). Independence caveat applied: every convergence below is tagged DERIVED (argument/lemma/cost in the
tree) or NAMED (mentioned only).

## 0. Incumbent of record (what arm C actually is today)

- TWIN §4 arm C (:57-61): "the classical design of the SAME geometry class at the I4 interface (<Pc>, T0,
  gamma — mean conditions only): the literature's fixed design (Rao-class plug / peak design at mean point),
  built by the SAME engine and certified by the SAME stack (independent classical route as cross-check where
  available, GENO oracle class)". Sector = TRUNCATED PLUG (§2), case A data (§3), constraint identity §5
  (eps, L, truncation FRACTION, p_b closure object, floors, tables, mu, representation).
- Theorems that define the classical opponents: [T-T3] (M0 :746 ff.) — full-flowing fixed wall under
  pressure-similarity collapses EXACTLY to the classical contour at the TIME-mean <Pc>_mu (Lemma C: affine in
  Pc); [T-T4] (M0 :2294 ff.) — ideal plug optimal at the PEAK phase; sharpness (:2313-2316): a length cap
  L < l(xi_peak) or a base-pressure model at a truncation plane breaks the nesting, max Int < Int max STRICTLY.
- The field's own RDE practice in-repo: Stechmann-Heister-Harroun model (`stechmann_nozzle.py` Step 5, :66-90):
  bell optimum sits at the TIME-mean Pc (NPR(eps*) = mean_t(Pc)/Pa, proved in `bell_optimality_proof.md`
  :64-70), aerospike optimum = saturation knee at the PEAK (NPR = Pmax/Pa); the eps sweep is done UNDER the
  cycle-averaged Isp. Rejector `tests/test_bell_optimality.py` T1c (:13-15, :75-82) REJECTS the plausible
  mass-weighted mean as the bell design state. M0 :2565-2572 reads the paper's Figs 9/10/12 as instances of
  T3/T4.
- Historical record BEFORE the TWIN pre-registration fielded BOTH baselines explicitly: roadmap_geno_rde N2
  (:137-138) "TRUNCATED PLUG at fixed length — cycle-optimal vs PEAK-designed vs MEAN-designed"; problem book
  PB-2 (:532-536) "vs peak- and mean-designed baselines". The TWIN §4 wording "Rao-class plug / peak design at
  mean point" COLLAPSED the two baselines into one phrase that is internally inconsistent (a peak design is by
  definition NOT at the mean point).
- Base treatment: ledger C61 NEVER (Veen legacy-practiced, WG10 bracket [+19,-15]%, N2 slot declared, no
  program adoption); M0 :1347 channel (v): "base-pressure model-form UNPRICED on truncated plug"; C61 note:
  the closure moves the ARGMAX x2.45 (Humphreys) — foundation-grade.
- "Which mean" in the record: ADVISORY_rde_choking :231-240 (moot INSIDE the T3 hypotheses); hypothesis
  ledger H-CON :173-178 (moot only for GEOMETRIC-ONLY constraint classes — PRICED). No record text decides
  which mean for the TRUNCATED plug.
- Ledger status of the comparator-identity axis: NO ROW. Measured this window: grep -n -i on
  "comparator|arm C|peak" in docs/choice_ledger.yaml = 0 hits on this axis (the only "classical"/"peak" hits
  are C9 mesh-law text). The TWIN §4 text is SINGLE-AUTHOR (F2-B0 order 7; the F2-B0 refuter pass targeted
  the roadmap placements, not arm C's identity — findings row :2873-2882 is a guardian of protocol drift, not
  an adjudication among classical opponents). Prior de-novo evidence (2026-08-17): the formulation-level brief
  had no SP-CARM fork (grep -i comparator on phaseA_tree_*_CONDENSED.md = 0 hits); nearest = diff §2.16
  "averaged-system regression oracles" (Dirac-mu Rao regression) and §3.2 Rao-collapse re-derivation —
  oracles, not comparators.
- CLASS: NO-ROW (ledger) / SINGLE-AUTHOR (protocol text). DELTA-SWEEP inline NOT applicable (no DECIDED row
  with a genuine advocate exists); what I did instead is the record sweep above, which is the input a panel
  needs.

## 1. Table of approaches (every SP-CARM branch fielded by the trees + the orchestrator-seeded one)

| # | Approach | From lenses (tree loc.) | Class | DERIVED / NAMED | Record anchor | Weight on Q0 | Why (credibility / cost) |
|---|---|---|---|---|---|---|---|
| A1 | Classical contour at the ARITHMETIC TIME-MEAN state ("naive mean") | Var K.1 :563-564; Opt C.1 :545; Hyp (1) :527; Prop C.6 :669-671 (all: "weakest / straw man") | DIVERGENT (bell) / OPEN (plug) | NAMED as weakest (no lemma against it at case A) | TWIN §4 :57-61 (= the incumbent); [T-T3] :746-800; test_bell_optimality T1c; ADVISORY_rde_choking :231-240 | high | The trees rank it weakest because at class B (M, angle, swirl vary) an arithmetic mean of primitives is arbitrary. At case A / I3 only (P0,T0,gamma)(xi) vary and [T-T3] Lemma C makes <Pc>_mu the EXACT collapse point for the full-flowing bell — the record wins by theorem + executable rejector. For the TRUNCATED plug no theorem covers it ([T-T4] sharpness) — the trees' objection stands there. |
| A2 | Flux-consistent / mixed-out / mass-flux-weighted / EAP equivalent state + classical contour | Var K.2/K.3 :565-569 + L0.2(ii) :35-39 (DERIVED: homogenized St->inf limit, realizability check); Hyp (2) :528-529 (NAMED, Denton mixing-plane); Opt C.2 :546-548 + L2 caveat (i) :36-38 (DERIVED: O(eps) first-order term = "which average"); Prop C.1 :646-649 (DERIVED: EAP matches the thrust integral) | DIVERGENT (bell) / NEW arm (plug) | DERIVED 3/4 | M0 EAP remark :2526-2545 (EAP = pressure coordinate of J_ideal, a BOUND not a design state); bell_optimality_proof :98-101 (mass-weighted mean is the WRONG bell state, rejected by T1c); X-STSC plug St up to 1.41 (log :38) | medium (upper end; high as a member of A4) | For the bell the record REFUTES it with a rejector. For the plug at St ~ 0.3-1.4 the homogenized limit is not remote (Var L0.2(iii): no ordering holds), so a flux-consistent classical plug is a legitimate SECOND classical opponent. Cost: one extra Dirac-mu design + one cycle evaluation. |
| A3 | PEAK-designed plug (design at P_CJ/Pa, capped by eps_max) | NONE of the four trees fields it (Hyp (4) contains it implicitly as the peak member) | ORCHESTRATOR-SEEDED | — (tree gap: the trees do not know T-T4) | [T-T4] :2294-2320; Stechmann Step 5(c) :80-90 + M0 :2567-2570 (det aerospike sized by the PEAK); roadmap N2 :137-138; problem book PB-2 :532-536 | high | It IS the field's practitioner baseline for a plug (Stechmann Figs 10/12) and the record's own pre-TWIN baseline. TWIN §4 names it in the same breath as "mean point" — the protocol must pin ONE design phase or a SWEEP (A4). Cost: zero beyond A4. |
| A4 | DESIGN-PHASE SWEEP: classical contour built at Dirac-mu(xi) for xi from <Pc>_mu to the peak (through the A2/A6 states), each member evaluated on the same mu, arm C := argmax | Hyp (4) :530-531 "multi-phase Rao, pick the best on the exact evaluator" (DERIVED as a second control); Var K.5/S0.13 :572, :188-196 (DERIVED: ceiling arm, O(10) evaluator runs); Prop S-7 :155-166 (family BO) | NEW (as a TWIN arm) | DERIVED 3/4 | 0-D precedent in-repo: Stechmann Step 5 sweeps eps UNDER the cycle Isp; M0 VI.5 :3178 seeds Rao-at-<Pc> and peak design are SEEDS not arms; roadmap N2 is its 2-member subset | high | Under constraint identity §5 (eps, L, truncation fixed) the ONLY freedom left to a classical plug is the design state — so A4 IS the strongest classical opponent, by elimination. Directly measures [T-T4] sharpness on the record instance. Cost: O(10) single-state designs of the same engine + O(10) cycle evaluations = one session, before any arm-P run. |
| A5 | TUNED PRACTICE: classical family's 1-2 geometric parameters (design NPR / eps / length fraction / truncation) optimized on the exact evaluator | Hyp (3) :529-530 (THE comparator; DERIVED attribution argument :480-484); Var K.5 :572, S0.13 :188-196; Opt C.3 :549 manual area-ratio iteration | NEW, but COLLAPSES to A4 under §5 | DERIVED 3/4 | TWIN §5 :73-86 fixes eps/L/truncation; Stechmann Step 5 (0-D realization) | medium | Relevant only if constraint identity is relaxed (area ratio free — a different question, outcome (D) of Var SP9). Under §5 it adds nothing to A4. Keep as the DEFERRED "free-eps" companion. |
| A6 | THRUST-CONSISTENT average: single state u* with F(S;u*) = sum_k w_k F_k(S) at the baseline contour (1-D root find along the arithmetic->mixed-out family) | Opt C.4 :550-554 (DERIVED: existence by continuity; "refuter's comparator"; residual advantage O(eps^2) + feasible-set first-order) | CONFIRM-candidate (bell) / NEW arm (plug) | DERIVED 1/4 | [T-T3] Lemma C: F affine in Pc => u* = <Pc>_mu EXACTLY for the bell (the tree's construction, run at case A, RETURNS the record's choice — a derived convergence); for the truncated plug F is not affine => u* != <Pc>_mu | medium (upper end; high as a member of A4) | Cheapest way to make "mean conditions" well-defined for the plug: it is the member of A4 that matches the cycle thrust at the baseline. Cost: K+1 evaluations at one contour (values only). |
| A7 | SAME-ENGINE single-state control arm (attribution: parametrization freedom vs cycle weighting) + literature fixed design as a SEPARATE arm | Var S0.5 :119-124 (DERIVED: "if S0.5 beats S0.2 by the same margin as S0.3, the gain is the parametrization"), SP9 outcome (D) :525; Opt C.5 :555-558; Hyp (3) rationale :482-484 | CONFIRM-candidate (same-engine arm) + NEW (3-arm attribution) | DERIVED 3/4 | TWIN §4 "built by the SAME engine"; F1b F7 datum: direct optimum vs GENO DEF at ONE state = +0.51% (D6 :137-152; log :110) = the record's MEASURED parametrization surplus at one state | high | +0.51% is INSIDE the TWIN §6 INTERMEDIATE band [0.5,1]%: if arm C is the literature's Rao-class plug (GENO) the surplus contaminates delta; if it is the same-engine Dirac-mu optimum it is removed. §4 mixes both ("literature's fixed design ... built by the SAME engine ... independent route as cross-check"). Two classical arms are required, one per attribution. Cost: one extra design. |
| A8 | Worst-instant (per-phase) attachment check GIVEN to the comparator (TIC-like conservative choice) | Prop C.3 :653-657 (DERIVED: otherwise OUT-C is an artefact); Opt C.3/L5 :54-59, :549; Var K.3 "attachment checked over the cycle" :513; Hyp SP9 :480-484 | CONFIRM-candidate-NAMED (§5.5 floors) / DEFERRED | NAMED for the plug sector | TWIN §5.5 (margin/certification floors are solution-class margins, not separation margins); sector = plug (free boundary self-adapts); N1 separated-bell channel = different window; D-GSEP declared empirical closure (phaseB diff §2.15) | low (plug TWIN) | Moot on the truncated-plug sector; becomes HIGH if the TWIN sector flips to bell (F1b-class) or N1 opens. Trigger + owner in the branch ledger. |
| A9 | SAME base closure for both arms AND same base AREA (not only the same truncation FRACTION) | Opt PB.4 :532-540 (DERIVED: dDelta/dp_b = (A_b7 - A_b2)/F; fix truncation so base areas MATCH); Prop SP9 :581-582 "FIXED truncation fraction and base radius", SP-PB :633-641 (DERIVED materiality 0.3-1.5% F); Hyp SP-PB :518-522 (DERIVED: ~3% swamps unless same base — "they don't, A_b differs"); Var B.5 :547-553 (DERIVED bracket both sides) | CONFIRM-candidate (same closure) + DIVERGENT (sufficiency of §5.3) | DERIVED 4/4 | TWIN §5.3 truncation fraction same value, §5.4 same closure object; C61 NEVER (bracket [+19,-15]%); M0 :1347 (v) model-form UNPRICED on truncated plug | high | A plug's base RADIUS at the truncation station is contour-dependent: arm P and arm C can share the fraction and differ in A_b, re-introducing the C61 band at FIRST order — 1-5% F base thrust x 15-19% bracket = 0.2-1% F, straddling the 0.5-1% materiality band. Cost: zero (print A_b of both arms; add the (A_bP - A_bC)*Dp_b/F term to the band stack or pin the base radius). |
| A10 | Comparator built INDEPENDENTLY by the legacy MoC oracle (read-only), then evaluated on the common evaluator | Prop recommendation :672-673; Hyp SP9 :480-482; Opt V.5 :473-474 | CONFIRM-candidate-NAMED | NAMED | TWIN §4 "independent classical route as cross-check where available, GENO oracle class"; F3 entry gate (D6 :214-217) RaoPlug S1/S2 fix or single-oracle status (Rao 1961 spike Table 1); lit registry :434 (GENO S4/S5/S6 plug bugs of record) | medium | Credibility only; the record has it as a cross-check, conditional on RaoPlug repairs. Trees add nothing the record lacks except the ORDER (comparator built and frozen FIRST — Prop OoB step 4, Var step 1, Opt step 3): adopt as a sequencing pin. |
| A11 | "A competent designer already averages duty" + literature query bounding the novelty | Prop C.5 :659-668; Var :576-577; Hyp :534-537; Opt :559-560 | CONFIRM-candidate | NAMED 4/4 | M0 Part I :32-34 ("RDE practice either averages the flow first and designs classically"); lit registry liu_2022 :622 (average-then-classical corpus), zhu_2020 :1285 (earliest average-then-design), harroun_2021 :285 (cycle average BLIND at contour-ranking level), paxson_miki_2022 :257 (steady sizing misses ~31%); TWIN §1 "ZERO computed instances"; G5 | low | Changes claim wording, not the number; the record is already page-verified and query-bounded here. |
| A12 | Unsteady base-pressure response indicator tau_b*f reported per instance | Prop B.6 :630-632 (DERIVED order estimate) | NEW | DERIVED 1/4 | C61 alternatives (measured closure); litmap extension :78 (base suction differs under the cycle); harroun_2020 :640 (base drag enhanced by the cycle) | low | Report-only indicator; enters the C61/N2 window, not the comparator identity. |
| A13 | Weighted multipoint steady design is a KNOWN technique — novelty only in evaluator / bound / certificates | Opt C.5 :555-558; Prop C.5 (ii)-(iv) :662-665 | CONFIRM-candidate-NAMED | NAMED 2/4 | M0 Part I :58-61 ("every component is prior art in isolation; the constructive certificate-bearing composition is unpublished"); M0 :2333-2336 Reuther 1999 in the caveat list | low | Already the record's stance. |
| A14 | BOUND-SCREEN THE COMPARATOR FIRST: delta_practice = (J_ideal - J_C*)/J_ideal vs band; if <= band the MATERIAL branch is unreachable by theorem | Var S0.11 :168-176 + L0.3 :46-56 (DERIVED); Hyp S12 :237-242 + L4 :38-49 (DERIVED, evaluable in seconds from class-B data); Opt S13 :212-218 + L2 :26-40 (DERIVED Jensen bound, K+1 solves, no adjoint) | CONFIRM-candidate (record has the bound) + NEW sequencing | DERIVED 3/4 (independent blind convergence) | [T-GB] M0 :2323 ff. (J_ideal geometry-free bound); G2 value gate D6 :776-782 ("bound-ladder gap per channel; gap < ~1% Isp -> pivot"); Annex B invariants :1153 ("J_ideal is post-processing"); M1 corollary :2447-2452 | high | The record owns the theorem but schedules the gate at M2; three trees put it BEFORE building. For SP-CARM it upper-bounds ANY classical arm's deficit: if the best classical plug (A4 argmax) is already within 0.5% of J_ideal on the record instance, F3.TWIN is decided SMALL before its first arm-P run (saves 3-4 sessions). Cost: J_ideal post-processing + one evaluation. |

Weight legend: high = changes the identity or the readability of the decisive delta (TWIN §6 branch); medium =
changes attribution/credibility at fixed cost; low = wording or reporting; zero = none (no A-row is zero).

## 2. Reasons, with anchors

2.1 The trees CONVERGE (4/4) on the load-bearing statement "a weak comparator = worthless number" and on the
STRUCTURE of the strongest classical opponent: not the naive mean, but (i) a well-defined equivalent state,
(ii) the classical family's residual freedom exhausted under the SAME cycle evaluator, (iii) identical
constraints/base/tables, (iv) attribution controls. The record has (iii) (TWIN §5) and half of (iv) ("same
engine"); it does NOT have (i) or (ii) pinned for the truncated plug. Conversely the trees are BLIND to the
record's two theorems that make (i) trivial on the bell ([T-T3]) and non-trivial on the plug ([T-T4]
sharpness); none of them fields the peak-designed plug, which is the field's own practitioner baseline
(Stechmann, in-repo 18/18). Net: the record is stronger on the THEORY of the comparator; the trees are stronger
on its PROTOCOL.

2.2 On "which state" (mean / peak / duty-weighted), the answer is sector-conditional and the record already
proves the bell half:
- Bell / case A: <Pc>_mu (arithmetic TIME mean) is exact ([T-T3] Lemma C, M0 :787-791); mass-flux-weighted or
  EAP states are provably WORSE design states (bell_optimality_proof :98-101; T1c rejector). The trees'
  ranking K.1 < K.2 < K.3 is therefore INVERTED for the bell at case A — a DIVERGENT verdict where the record
  wins with a rejector. (Their ranking is defensible at class B, where M/angle/swirl vary — a different data
  class from the TWIN's.)
- Truncated plug (the TWIN sector): [T-T4] sharpness says the nesting breaks under a length cap or a base
  closure; no theorem selects mean vs peak vs flux-consistent; the in-repo 0-D model says PEAK for the ideal
  spike (Step 5(c)). Hence the strongest classical plug is NOT known a priori and must be the ARGMAX over the
  design-phase sweep (A4), which contains A1, A2, A3, A6 as members. Under §5 constraint identity the sweep
  is the only classical freedom (A5 collapses into it), so A4 is strongest BY ELIMINATION — a short argument
  the Stage-B parties can check without running anything.

2.3 TWIN §4 wording defect (record-side, referee-visible): "Rao-class plug / peak design at mean point" names
two incompatible designs; §4 also mixes the literature's fixed design (GENO classical route) with the
same-engine Dirac-mu optimum. With the F1b F7 datum (+0.51% at one state, D6 :146-150) sitting inside the
§6 INTERMEDIATE band, the attribution ambiguity is MATERIAL: a "gain" of 0.5-1% could be parametrization
surplus, not cycle weighting. The trees' 3-arm structure (literature fixed design / same-engine single-state /
per-phase) is the minimal repair (A7). It costs one extra design.

2.4 Constraint identity (TWIN §5) is NECESSARY but NOT SUFFICIENT for the base term: all four trees derive
that the p_b band cancels only to first order in (A_bP - A_bC), and §5.3 pins the truncation FRACTION, not the
base AREA. On a plug spike the radius at the truncation station is a contour output. With C61 NEVER and the
WG10 bracket [+19,-15]% (C61 :822), the residual is 0.2-1% F — the same order as the materiality threshold.
This is the single largest UNPRICED term the trees expose for SP-CARM (A9). Repair options (either is cheap):
(a) add the (A_bP - A_bC)*Dp_b,band/F term to the §6 band stack, or (b) pin the base radius as a §5 item. The
propulsion tree derives a second-order residual only under equal base area (SP-PB :636-638).

2.5 Bound-screen sequencing (A14): three lenses independently derive "compute the ideal-bound gap of the
practice design before optimizing" (Var L0.3/S0.11, Hyp L4/S12, Opt L2/S13). The record owns the object
([T-GB], G2) and even states it is post-processing (Annex B :1153) but gates on it AFTER the engine (M2). For
SP-CARM the consequence is direct: delta_practice(A4 argmax) <= band makes the TWIN's MATERIAL branch
unreachable by theorem, so the comparator build (already required for arm C) should ship its gap number
BEFORE arm P runs. The record's own X-STSC number (plug St up to 1.41) does not change this: J_ideal is
rung-independent (it is a per-phase isentropic bound).

2.6 Evaluator parity for the comparator (touches SP1/SP5, noted for their judges): all four trees insist that
the comparator be scored on an evaluator that is NOT the designer's own model (Opt T.E3 "a model cannot grade
itself", Var SP5 "designer != evaluator by construction", Hyp SP5, Prop SP5). TWIN §4 has same mu + same
representation (A-REPR placeholder). At plug St = 0.27-1.41 (X-STSC log :38-40, license rule: "wave-frame /
unsteady rung REQUIRED") scoring BOTH arms at the frozen-time rung would violate the record's own license.
This does not change the comparator's identity; it changes where its NUMBER is quotable — owner SP1/SP5.

2.7 Duty-weighted opponent and the "duty split" channel: the trees' "duty-weighted" state (A2/A6) is a
single-state object; the record's N2 "duty split" (D6 :1142, PB-3) is a two-body (shroud/plug) object —
different axes, no conflict. No tree proposes a shrouded-plug comparator; PRUNED here (sector not in the TWIN).

2.8 [KNOWLEDGE] claims of the trees I relied on, verification status against docs/literature_registry.yaml:
- Kaemming & Paxson 2018 EAP (Prop C.1, Var K.2): VERIFIED — row kaemming_paxson_2018 :236-247
  READ-INTEGRAL; M0 remark verified clause-by-clause.
- Stechmann-Heister-Harroun 2019 (not cited by any tree; used by me): VERIFIED — row stechmann_2019 :318-326,
  in-repo 18/18 validation.
- Cumpsty & Horlock 2006 "averaging nonuniform flows" (Opt C.2 [abstract]): UNVERIFIED — no registry row.
- Denton 1992 mixing-plane practice (Hyp (2) [abstract]): UNVERIFIED — no registry row.
- Hagemann, Immich, Nguyen & Dumnov 1998 (Prop C.4 [full], Var B.2, Hyp (3) base correlations): UNVERIFIED
  in-repo — row wanted_hagemann_1998_advanced_nozzles :1374 (WANTED, unread).
- Frey & Hagemann 1998 / Stark 2005 / Schmucker (Prop C.3, Opt SP2): UNVERIFIED — no rows (bell-sector only).
- "RDE nozzle studies design for time-averaged exit conditions" (Hyp :534-536, via Fotia 2016 [abstract]):
  the CLAIM is VERIFIED by rows liu_2022 :622 and zhu_2020 :1285; the Fotia 2016 SOURCE is WANTED :1266.
- Rankin 2017 / Goto 2019 / Fotia 2016 RDE thrust-stand uncertainty 1-3% thrust, 2-4% Isp (Prop DL-4 :64-75):
  UNVERIFIED — wanted rows :1266, :1272, :1410; if true it bears on SP9's band anchor (TWIN §6 quotes the
  steady thrust-stand class 0.5-1% as a NOTE-class anchor, D6 :779-782) — flagged to the SP9 judge.
- Reuther et al. 1999 multipoint (Opt/Prop novelty bound): VERIFIED as a caveat entry, M0 :2333-2336.

## 3. Three questions (SP-CARM seat only)

- Q1 (is Q1 the right sharpening of Q0?): "per-phase method vs classical fixed design at identical
  constraints on the truncated plug" is the right sharpening ONLY IF "classical fixed design" is the STRONGEST
  classical member (A4 argmax with A7 attribution), and only if A14 has not already decided it. As written
  (§4 ambiguity) the sharpening is under-specified, not wrong.
- Q2 (does the delta answer Q0?): yes for the truncated-plug sector at case A, provided the base-area term (A9)
  is inside the band stack; without it the INTERMEDIATE/SMALL boundary is not readable.
- Q3 (separate rungs for designer and evaluator?): 4/4 trees say yes; for the comparator this means arm C's
  score must come from the same evaluator as arm P AND that evaluator must satisfy the X-STSC license at plug
  St — an SP1/SP5 duty, noted here.

## 4. Proposed falsifier (what Stage-B parties must agree on) — the DESIGN-PHASE SWEEP + BOUND SCREEN

Object: the F2.ENGINE arm-C builder (required anyway) at the TWIN instance and constraint vector §5.
Procedure (one session, values only, before any arm-P run):
 1. Build classical truncated plugs Sigma_C(xi_d) at Dirac-mu(xi_d) for xi_d on a grid containing <Pc>_mu (A1),
    the mass-flux-weighted and thrust-consistent states (A2/A6), and the peak P_CJ (A3); same engine, same
    tables, same C61 closure object; print A_b of every member.
 2. Evaluate every member on the SAME mu and representation as arm P; arm C := argmax_xi_d J_avg(Sigma_C(xi_d)).
 3. Report spread_C := max - min over the sweep, delta_practice := (J_ideal - J_avg(arm C))/J_ideal, and
    Delta_Ab := (A_b,P - A_b,C)*Dp_b,band/F for the eventual pair.
Decision rules (pre-registered):
 - spread_C > band (0.5% abs on delta): TWIN §4 "mean conditions only" is REFUTED as the strongest classical
   design; amendment A-CARM pins arm C := the sweep argmax (+ the literature's GENO fixed design as the
   attribution arm A7) before any arm-P run.
 - spread_C <= band: the comparator identity is IMMATERIAL on this instance; §4 stands with any member, and the
   sweep result is the record datum on [T-T4] sharpness.
 - delta_practice <= 0.5%: the MATERIAL branch is unreachable by theorem ([T-GB]); the TWIN's value outcome is
   pre-decided SMALL and the campaign pivots per G2 wording without running arm P.
 - Delta_Ab > band/3: base radius becomes a §5 pin or the term enters the §6 stack; else declared minor.
Kill for the falsifier itself: an engine that cannot build a Dirac-mu classical plug at the peak phase within
the certification floors (A-1 margin rule) — then "peak-designed" is not a certifiable member and the sweep
reports its certified sub-range with the cause.
Cost: O(10) designs + O(10) evaluations; wall-clock inside one 3 h decisive window at F3.TWIN opening.

## 5. Branch ledger (every branch seen)

| Branch | Status | Reason / trigger + owner |
|---|---|---|
| Prop C.1 EAP / mass-flux-weighted state | EXPANDED | A2 |
| Prop C.2 Rao / Angelino-Lee rotational var-gamma MoC with mean swirl, same L / R_e | EXPANDED (partly) | same-constraint half = TWIN §5 (CONFIRM); mean-swirl half = case A has no swirl channel -> DEFERRED, trigger: TWIN flip to case B (§3 flip clause), owner F2.REPR/swirl5f |
| Prop C.3 worst-instant attachment for the comparator | DEFERRED | A8; trigger: sector flip to bell / N1 window opens; owner F3.TWIN amendment author |
| Prop C.4 Hagemann-class base for both | EXPANDED | A9 |
| Prop C.5 duty averaging practised + literature query | EXPANDED | A11/A13 |
| Prop C.6 rejected comparators (conical, const-gamma Rao, mean-state attachment) | PRUNED | agreed weaker; the record never fields them |
| Prop S-1 practice / S-7 family BO | EXPANDED | A1 / A4-A5 |
| Prop B.6 tau_b*f indicator | EXPANDED (low) | A12 -> C61/N2 window |
| Var K.1 naive mean | EXPANDED | A1 |
| Var K.2 mass-flux-weighted | EXPANDED | A2 |
| Var K.3 flux-consistent (L0.2(ii)) | EXPANDED | A2 |
| Var K.4 K.3 + a-posteriori multipoint check + manual tweak | PRUNED | dominated by K.5/A4 under §5 (no free parameter left to tweak) |
| Var K.5 Rao family under the exact evaluator | EXPANDED | A4/A5 |
| Var K.6 multipoint by hand | PRUNED | = the method under test (tree's own reason) |
| Var S0.5 adjoint freedom at one state | EXPANDED | A7 |
| Var S0.11 / Hyp S12 / Opt S13 bound-only screen | EXPANDED | A14 |
| Var S0.13(b) class-G co-design comparator | PRUNED | class G outside the TWIN nominal answer (§3); owner SP7 judge |
| Hyp (1) time-mean Rao | EXPANDED | A1 |
| Hyp (2) flux-averaged (mixing-plane) Rao | EXPANDED | A2 |
| Hyp (3) tuned practice | EXPANDED | A5 (collapses to A4 under §5) |
| Hyp (4) multi-phase Rao, best on evaluator | EXPANDED | A4 (core of the falsifier) |
| Hyp (5) conical / ideal-truncated equal length | PRUNED | second control only; the record's spike Table-1 oracle (F3 entry) is the plug-side classical control of record |
| Opt C.1 arithmetic mean | EXPANDED | A1 |
| Opt C.2 mixed-out average | EXPANDED | A2 |
| Opt C.3 C.2 + per-phase separation fix + manual eps/L iteration | EXPANDED / DEFERRED | eps/L half collapses under §5; separation half = A8 deferred |
| Opt C.4 thrust-consistent average | EXPANDED | A6 |
| Opt C.5 multipoint = known technique | EXPANDED (low) | A13 |
| Opt S2 tuned classical | EXPANDED | A5 |
| ORCH-seeded peak-designed plug | EXPANDED | A3 (record-side, tree gap) |
| ORCH-seeded duty split (shroud/plug, PB-3) | PRUNED for SP-CARM | sector not in the TWIN; owner F3.TOURNAMENT |
| Record TWIN §4 arm C as written | EXPANDED | incumbent; wording defect §2.3 |
| Var S0.13(a) / Prop S-7 with eps FREE | DEFERRED | trigger: any amendment relaxing §5.1; owner F3.TWIN |

## 6. Adjacent-field prior check (mandatory) — considered by the trees?

| Item | Considered by trees | Note |
|---|---|---|
| Turbomachinery steady rotating frame (sector + periodic BC; Coriolis sources) | YES (Prop DL-1 :12-30, Opt S4 :103-117 Lakshminarayana 1996 / Wang & He 2010, Hyp L1 :15-23, Var L0.1 :15-29) | For SP-CARM it is the EVALUATOR on which the comparator is scored, not the comparator; no registry row for the turbomachinery precedent (candidate census row, owner SP0/SP1 judge). |
| Harmonic-balance / time-spectral adjoints | YES, all four, rejected for a stated reason (dominated by the rotating frame under the pin; Gibbs at the data shock — Hyp S5 :142-151) | registry rubino_2018 :579-586 exists; Hall-Thomas-Clark 2002 not a row. Owner SP1 judge. |
| Steady adjoint shape optimization (Jameson; Giles-Pierce; discrete vs continuous) | YES (all four, SP3) | Out of SP-CARM scope; owner SP3 judge. |
| Averaging of non-uniform flows "for a purpose" (Cumpsty-Horlock 2006; Denton 1992 mixing plane) | YES (Opt C.2 :546-548, Hyp (2) :528-529) | DIRECTLY the SP-CARM question ("which mean"); UNVERIFIED — no rows. [KNOWLEDGE] rows below. |
| Multipoint design practice (Drela 1998; Reuther 1999) | YES (Opt S3 :92-93, C.5) | Reuther in M0 caveat list; Drela no row. Novelty-bound only. |
| EAP (Kaemming-Paxson) as the RDE field's own averaging doctrine | YES (Prop C.1, Var K.2) | VERIFIED row; the record's remark is stronger than the trees' use (EAP = bound coordinate, not a design state). |
| The RDE practitioner's own bell-vs-aerospike cycle-mean-Isp model (Stechmann 2019) | NO (no tree names it) | The trees' gap; in-repo of record (18/18), gives the PEAK-designed plug baseline the trees miss. |
| Mission-averaged area-ratio selection (Hagemann 1998) | YES (Prop C.5) | WANTED row unread; [T-T3] C2 already proves cycle- and altitude-averages are one mathematics for the full-flowing bell. |

## 7. Panel recommendation

FULL-PANEL (right-sized): the axis is NO-ROW in the ledger and single-author in the protocol; the fix is a
single dated amendment (A-CARM) to TWIN §4/§5 plus the §4 falsifier — a 3-party, 2-round panel (propulsion
referee, variational/record advocate, refuter) on the amendment text, not a fork-wide panel. Delta-sweep
inline: NOT DONE (not applicable — no DECIDED row with a genuine advocate); the record sweep of §0 is the panel
input. Deliverable of the panel: (i) arm C := design-phase-sweep argmax (A4) + literature fixed design as
attribution arm (A7); (ii) base-area term or base-radius pin (A9); (iii) delta_practice gate before arm P
(A14); (iv) a ledger row C63 "comparator identity" minted from the amendment (SR-12 dedup by the grep above).
