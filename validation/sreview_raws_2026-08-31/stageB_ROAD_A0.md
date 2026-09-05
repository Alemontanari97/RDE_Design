# STAGE B — ROAD (LEVEL 0) — ADVOCATE A0: the HYBRID at its genuine best (S-REVIEW 2026-09-05)

Persona: union of the four de-novo derivers (variational + hyperbolic + optimization + propulsion lenses).
Role: GENUINE ADVOCATE of the alternative (hybrid tuple; second alternative = road (d) at marching cost).
Read integrally in this window: `stageB_items.json` id ROAD; `stageA_diff_SP0.md` (§0-§10); `stageA_diff_SP1.md`
(§0-§9); trees V S0.3/S0.4/S0.6/SP5, O S3/S4/S7 + order of battle + derived tolerances, P S-3/S-4/H-1 + "change road",
H L1-L8/S3/S4/S11/S12; `COVERAGE_CHECKLIST_roads.md`; `st_scoping_number_run.log`; `RED_TEAM_decisive_number.md` RT-6/RT-7/A-7/A-10;
M0 :25-62, :512-560, :1338-1348, :1734-1770, :2960-2985, :3008-3050, :3138-3162, :3276-3296, :4250-4299; D1 §8 :451-478;
D6 :160-230, :776-786, :1159-1213; TWIN §4-§9; ledger C51/C57/C59/C62; decision map OPTSHIFT :174; PROGRESS_Sreview LOG-2 (:114-:115, :179);
claims S-P4F :643, X-STSC :2278; findings :2717; roadmap :19-:32; G0_decision :160-190; PROBLEM_STATEMENT §8; registry rows rice_2003 :727,
rubino_2018 :580 (not load-bearing here); NASA ADJUDICATION_v2 L-1. No memory file consulted. Every number below carries its file anchor.

## 0. Scope rule applied

Only arguments that change the CREDIBILITY or the COST of answering Q0 by the road under review count, including the road's own decisive
experiment. I therefore do not re-argue [T-T0] (4/4 derived, SP0 §0) or the C59/C62 sub-axes: I argue (1) the EVALUATOR role, (2) the two
user COST FORKS, (3) the SP1 role split + a G3 derivation, (4) the LOG-2 dominance score honestly, and (5) what I concede.

## 1. PROPOSED AGREED FALSIFIER (both sides must sign it before arguing) — three legs, one measurement window

Owner/window: F2.ENGINE exit on the record contour ([X-AKNO]/S18 W*, the [X-STSC] instance) BEFORE any TWIN arm; C51 route-B/B-lite
adjudication = F2.REPR (D6 :1170-1178) supplies the march. Instrument of record already owed on the critical path: M-RED B-1 ">= 4-point
St-ladder Richardson" (findings :2717, roadmap :19 F2.M-RED critical) and [S-BLITE] "the cheap exact meter of the rung-2 sweep/D2 residual"
(M0 :3037-3038). Nothing new is built FOR the falsifier.

LEG A — evaluator role (kills or licenses the incumbent as CARRIER OF THE DECISIVE NUMBER; = SP0 §6 + SP1 §5 merged):
on the SAME design(s), SAME thermo tables, SAME mu, SAME p_b closure, compute (a) J_avg (rung 2, C62-audited K), (b) J_avg + St·J_1 where
J_1 is available (see §4: the ladder slope IS a J_1 estimate), (c) J_exact by the wave-frame march (B-lite where u_x − c >= delta; route-B on the
annular part where |w_rel| > c; O5 oracle where neither is legal) at Omega/2, Omega, 2·Omega with the data shape fixed. Report
r_red = |J_exact − J_avg|/J and r_corr = |J_exact − (J_avg + St J_1)|/J with two-level Richardson bands and the exponent p of r_red vs St.
  - Incumbent SURVIVES as carrier iff r_corr + band <= b_TS/3 at the record St AND p >= 0.8 on the case-A blowdown family.
  - Incumbent KILLED as carrier (A-EVAL adopted: TWIN §6 metric -> J_exact per arm) iff r_corr + band > b_TS/3 at the record St, OR on the final
    TWIN pair the branch (MATERIAL/SMALL/INTERMEDIATE) read on delta_wf differs from the branch read on delta_pp, OR delta_wf(St) crosses a
    branch boundary inside the [X-STSC] bracket [L/u_e, L/a*].
  - Hybrid's OWN kill (symmetric): if r_red + band <= b_TS/3 for BOTH arms AND the branch is invariant under the Omega-sweep, the wave-frame
    evaluator adds no information at this instance and the incumbent is CONFIRMED with a new reason (its number licensed a posteriori).
  - Rejector of the leg itself: the ladder must reproduce the quasi-steady limit as Omega -> 0 within band (V L0.2 both-direction test); failure = solver bug.

LEG B — COST FORK (user question 11:16; separates road (d)-at-marching-cost from the hybrid):
measure, on the record instance and the pinned host (envfp printed, F2-B0 rule M0 :4267-4271):
  T_3D  := wall-clock of ONE certified B-lite helical march + its Lemma-B adjoint (reverse sweep of the x-block-triangular march, M0 :3036-3037),
  T_2D  := wall-clock of ONE per-phase value_and_grad execution of record (t_value_and_grad = 0.185 s clean host, G0_decision :167-169),
  K     := the C62-audited phase-node count at which |J_K − J_2K| <= b_TS/10 on the case-A family (C62 NEVER; the number is NOT of record —
           `grep -rn "n_xi\|N_xi\|nphase" validation/*.py docs/*.md` in this window returned no pinned K; it is printed by the audit).
  rho   := T_3D / (K · T_2D)    (forward-and-gradient cost ratio; gradient/solve ~1.6 both sides by T1 :168 and Lemma B).
  Flip rule (pre-registered): road (d) at marching cost REPLACES the per-phase designer iff rho <= 1 AND the march is legal on the whole decisive
  domain of the instance (axial margin certified up to the lip; base pocket closed by the same C61 object as the arms). Hybrid stands iff rho >= 10
  OR legality fails on the pocket. In between (1 < rho < 10) the 3-D adjoint enters as a trust-region CORRECTION (O S7 row 14, one exact
  gradient per accepted step), the per-phase adjoint stays the inner search — still the hybrid.
  Why K, not "an order of magnitude": the per-phase loop's gradient count of record is ~102-108 compiled executions per campaign (G0_decision
  :180-185, S25 truth repair); each execution is K per-phase marches; so the designer's total is N_eval · K · T_2D versus N_eval · T_3D for road (d).
  N_eval cancels (no basis to assume the exact gradient converges in fewer steps — that would be an argmax-shift claim OPTSHIFT forbids, decision map :174).
  The flipping quantity is therefore rho alone, and the "K that flips" is K_flip = T_3D / T_2D: if the audit's K is above K_flip, road (d) is cheaper.
  Honest prior: a helical march resolves the azimuth with N_theta stations ~ K (the same waveform resolution requirement drives both), so rho ~ O(1)
  is PLAUSIBLE if [S-BLITE]'s "marching cost" is literally true — and NEVER measured (C51 NEVER, :706). The fork is real, not rhetorical.

LEG C — tier separation (user question 11:19): the same measurement prints, per tier, the mesh-chain items that exist or not (§3 table);
tier (3) is EXCLUDED from Stage B unless LEG B fails legality on the pocket AND the program decides to design there (then it is priced, 10-20 sessions, V S0.6).

## 2. THE HYBRID AT ITS GENUINE BEST

Tuple (all four trees, SP0 §1 row 3; V S0.4, H S11, O S7, P H-1): objective O-a with per-phase attachment as state constraint; DESIGN loop =
the record's cycle-weighted frozen-time axisymmetric engine with its discrete AD adjoint (C56 of record — nothing new); EVALUATION of EVERY
competing design (arm P, arm C, the tuned classical C*, the ceiling arm) on the exact-on-pin wave-frame steady 3-D field ([T-T0] M0 :512-536),
values only, a few times; SCREEN first (J_ceil − J_C* loss budget, H L4 / O L2 Jensen / V L0.3); Omega-sweep at fixed data as the reduction
meter; the argmax half a CLAIM with falsifier ([T-RED] M0 :1734 ff.; OPTSHIFT). Decisive result = the TWIN sector row (truncated plug, case A)
read on delta_wf, embedded per RED_TEAM A-10 if ratified.

2.1 Why the evaluator promotion is the whole credibility delta (referee q3, the uncertainty budget).
- The record's own contract: "Any hardware conclusion from rung 2 without an St error bar is out of contract" (D1 §8 :477-478); the bar the
  record ships is an ASYMPTOTIC indicator, not a bound (BAR-CLASS NOTE, cited SP1 §3.1 at D-P :396-402). MEASURED St ([X-STSC] log, PASS,
  envfp e100f996): bell 0.347-0.599 at the record head count; plug class 0.268-1.415, 1.09/0.95/0.82 (T_CJ) to 1.41/1.24/1.06 (end-of-cycle) at the
  10 kN n = 3 row. The record's OWN license rule printed by the carrier: "plug class worst -> NOT DEFENSIBLE alone: wave-frame / unsteady rung REQUIRED".
- No J_1 exists (D6 :783-786 "the only gate whose kill threshold cannot reject"; M0 :1343 channel (i) WORST "unquantified of record"). So today the
  incumbent's bar on the decisive sector is a symbol. The hybrid replaces the symbol with a MEASURED r_red per design — the only way any number at
  St ~ 1 gets an error bar a JPP referee accepts (SP1 §3.1). That is q3 going from 0 to 1 (RED_TEAM A-2/A-7 read CRED(TWIN as written) = 1/5).
- Structural point the refuter's hat (1) must answer: the record's CHEAP corrector route is "one linearized solve ON THE WAVE-FRAME ANCHOR"
  (VI.4bis(ii) M0 :3151-3156) and its solvability is a Fredholm alternative on the cycle monodromy (S-P4F :643, THEOREM*). The corrector
  PRESUPPOSES the wave-frame forward solve. A corrector-as-carrier road therefore costs the evaluator's forward solve PLUS a linearized solve and
  delivers an O(St) indicator out of regime at St >= 1; the hybrid costs the forward solve alone and delivers the exact-on-pin value. The general
  route (O5 unsteady comparison) is strictly more expensive. Dominance on both axes wherever St is not small — i.e. on the decisive sector.

2.2 Why the third arm and the screen are credibility, not cost (referee q2, q5).
- Arm C as pre-registered (TWIN §4: I4 mean state) is the weak comparator by 4/4 derivations (SP0 §3 q1 condition 1); T4 says the plug wants
  the PEAK (M0 :44-47), so the mean-state plug is what practice would NOT field. The tuned C* on the evaluator (O C.4 by continuity, 1-D root
  find; V S0.13(a)) costs O(10) forward marches — hours — and is the "why not X?" a referee asks first. Without it a MATERIAL branch is
  attributable to the average choice or the parametrization (V outcome (D)), not to cycle design.
- The screen (1 session, values only, O order-of-battle step 4; H S12 Stage 0): if the unsteady-specific pool is below b_TS on C*, the O-a answer
  is NEGATIVE before F2.ENGINE's adjoint is exercised for the TWIN — the shortest credible path to a publishable answer, and a re-use of the record's
  own G2 gate (D6 :776-778) one phase earlier. q5 comes from the Omega-sweep: the deliverable is a MAP J(St) at fixed data (SP0 §1 row 12), which turns
  "n = 1" into a curve with two theorem-limits as rejectors (V L0.2).

2.3 Why the hybrid is INVARIANT under the cost fork (the genuine-best argument).
Whatever LEG B returns, the hybrid's load-bearing content — wave-frame EVALUATOR, screen-first, tuned comparator, Omega-map, argmax-as-claim —
is unchanged; only the DESIGNER half is swapped (per-phase adjoint -> B-lite adjoint, or per-phase adjoint + 3-D TR corrections). The incumbent is
NOT invariant: a rho <= 1 outcome retires its search engine to oracle/initializer (VI.4bis(iv) already assigns that role to the closed form), and a
rho >= 10 outcome leaves it without a bar at St ~ 1. The hybrid is the road that survives the measurement in every branch; that is why 4/4 lenses
ranked it first without having seen the record (SP0 §0, DERIVED, not seeded).

2.4 Cost, honestly priced against the statement budget (7-10 sessions, workstation, no GPU, 3 h decisive-run windows; PROBLEM_STATEMENT §8 :221-231).
- Trees: hybrid 7-9 sessions (V S0.4, P H-1), 6-8 + 1 screen (O S7), 7-9 if a marching branch is legal (H S11). Record remaining: F2 cap 4-6
  (D6 :160-166, "DELIBERATE cap"), F3 3-4 (D6 :211-221) -> 7-10 to the TWIN. The trees' number was priced WITH a pseudo-time 3-D FV evaluator
  (V S0.4 "O(10^6) cells, pseudo-time, hours"; O S4 "O(1e2-1e3) s per steady solve") — a solver the record does not intend to build.
- Record-native pricing: the evaluator = [S-BLITE] helical space-marching (M0 :3027-3044), no Newton-Krylov, no camera, no Omega eigenvalue;
  its named first brick is the 3-D axial-flux eigenstructure G12-L1-3D, "symbolic carrier candidate, never executed" (NASA ADJUDICATION_v2 L-1,
  with the Rice eq. 15/29 typo caveat; registry rice_2003 :727 READ-INTEGRAL). MY ESTIMATE (declared, not measured): brick + 3-D march on the annulus
  = 1 session inside F2.REPR/F2.ENGINE (the 2-D fitted march of record is the template; the unit process is a per-station (r,theta) problem, H S4).
  Evaluations: 3 (ladder) + 2 arms + C* (~10) + ceiling = O(20) forward marches, hours. Net delta over the record roadmap: +1 session of build IF
  M-RED's meter were not already owed; M-RED (critical, roadmap :19, :32) needs a St-varying exact meter for B-1 — the SAME solve. Cost-neutral to +1.
- Session count for the LOG-2 criterion: COST(hybrid) = [7, 10] to the first credible number (screen included; A-10 embedding excluded as user-priced).

## 3. USER QUESTION 2 (11:19) — the three cost tiers, priced explicitly

| tier | what the shape sensitivity needs | volume mesh? | mesh-sensitivity chain dR/dX·dX/dalpha? | limiter/shock differentiability | status of record | sessions |
|---|---|---|---|---|---|---|
| (1) HYBRID: per-phase AD adjoint for the SEARCH + wave-frame evaluator ADJOINT-FREE (values only, O(20) times) | none new: the per-phase march's wall enters as data of the fitted march (C56 discrete AD, C49 fitted class) | NO for the evaluator: B-lite "the march generates its own grid from the data", shape enters through the wall BC (M0 :3031-3036) | NONE | none for the evaluator (no adjoint); the designer's fitted-front AD is the machinery of record (G12-S1, M0 :2963-2977) | designer EXISTS and is certified (X-TOCV, grad/solve 1.593 :3287); evaluator brick UNBUILT (G12-L1-3D) | +0..1 (§2.4) |
| (2) road (d) via B-lite: DESIGN on the 3-D helical march, adjoint by Lemma B (reverse sweep of the x-block-triangular march) | no volume mesh; wall = boundary of the march; adjoint = exact transpose of the march (M0 :3036-3037; the NAND structural fact M0 :4285-4288 is the same block-triangularity) | NO on the legal domain | NONE on the legal domain | fitted sheet as per-station unknown (Lax in x-as-time, G12-L2): differentiable by construction inside the Lax class, degenerate exactly at characteristic fronts (record's own boundary) | 3-D unit process UNBUILT; march ILLEGAL where the axial margin fails: near-axis core of a full bell (H L5 r*/R ~ 0.4-0.7 [SE], unverified) and the plug BASE POCKET — there a pseudo-time sector solve with a mesh re-enters | brick 1 + adjoint verification 1-2 (my estimate); LEG B decides whether it is the designer |
| (3) road (d) via 3-D FV/DG with adjoint | full chain: mesh deformation (elasticity/RBF/regeneration) + dR/dX·dX/dalpha + adjoint consistency under mesh motion (discrete AD of the whole chain or continuous surface form) + non-differentiable shock capturing + free plume and pocket inside the domain | YES | YES | captured shocks: limiter non-differentiability (the C49 captured-vs-fitted axis, record) | NEVER adjudicated in the ledger: SP0 §7 registry grep = 0 rows for rotating-frame adjoint (Wang & He 2010 cited by O S4 at abstract depth, UNVERIFIED [APERTO]); C56 covers adjoint REALIZATION, not mesh motion; C31 alternatives lacked the axis | 10-20 (V S0.6), 8-10 (P S-3), 6-8 + abandon at > 20 min/step (O S4) — over the §8 budget by 4/4 |

Answer to the user in one line: "CFD with adjoint" = tier (3) and is NOT what any tree recommends; the hybrid needs NO adjoint on the 3-D side
and NO mesh (tier 1); road (d) at marching cost needs an adjoint but NO mesh either (tier 2) — its price is the unbuilt 3-D unit process and the
pocket/near-axis legality, both printed by LEG B. The evaluator on the truncated plug is exact on cl(Omega_march) and CLOSURE-bound in the pocket
(same C61 object for all arms, TWIN §5 item 4); the base term cancels between arms only with matched base AREA (SP0 §3 q2 increment) — the hybrid
inherits this exactly as the incumbent does, and prints dDelta/dp_b as a row.

## 4. SP1 ROLE QUESTION + the G3 THRESHOLD, derived (the S14 duty, D6 :784-786)

Designer rung and evaluator rung are chosen SEPARATELY — 4/4 derived (V SP5 "designer != evaluator by construction"; H SP5; O SP5 "what makes
the reduction error a MEASURED number"; P SP5 "deliberate"). Protocol consequence: TWIN §4's single field A-REPR splits into A-REPR (design, both arms
identical) + A-EVAL (evaluation, both arms identical, wave-frame or O5), R-TWIN-5 parity read on each (SP0 §3 q3 (iii)). F2.REPR is the owner
(D6 :1170-1183); the fallback "current 4-field axial declared for the TWIN" (:1184-1186) is then legal for A-REPR but NOT for A-EVAL at St >= 1.

G3 threshold derivation (no magic St cut; H's "St < 0.3" is NOT consumed, SP1 §3.2):
 (i) Materiality class of record: b_TS = thrust-stand 0.5-1% (D6 :779-782 note; TWIN §6). On the decisive sector three band terms have no
     producer (reduction, discretization, data — RED_TEAM A-2); with no prior on their sizes the max-entropy allocation is the equal three-way split
     -> each term <= b_TS/3 (O derived tolerances; P's 1/10 is the ten-term-headroom variant; the falsifier's measurement fixes the fraction).
 (ii) J_1 without a corrector solve: on the pin f is a parameter at fixed data, so J_exact(St) is a curve; J_1 := dJ_exact/dSt at St -> 0 is the
     ladder's slope (Omega/2, Omega, 2·Omega + the quasi-steady limit as rejector). Three forward marches print St|J_1| with a Richardson band.
     [T-T3QS] already predicts which branch the case-A sawtooth family sits in (jump-localized, J_1 != 0; SP1 A8), so the exponent p is a rejector
     of the expansion form itself.
 (iii) G3 as a rejector: "St|J_1| large" := St|J_1|/J + band > b_TS/3 -> rung-3 (wave-frame) correction loop for the DESIGNER; independently, the
     EVALUATOR is wave-frame whenever r_red + band > b_TS/3 (LEG A). Two thresholds, one measurement, zero new theory. Until (ii) runs, every public
     wording carries "rung-2 delta at St_n = x" (RED_TEAM A-7 (iii)).

## 5. LOG-2 DOMINANCE SCORE (PROGRESS_Sreview :114), stated against myself

CRED(hybrid): q1 external anchor = the wave-frame FIELD is directly comparable to a 3-D CFD/experimental field (F2.CFD-2 prediction-first, D6 addendum;
Harroun IE aerospike fields Figg. 12-20 named at F2.REPR entry :1166-1168) — a per-phase AVERAGE field is not (SP0 §1 row 20: anchor class only);
q2 tuned C* on the evaluator (§2.2); q3 measured r_red (§2.1); q4 forward marches with the A-8 hash set + envfp; q5 the Omega-map. CRED = 5 reachable
with named deliverables inside the plan. CRED(incumbent as carrier) <= 3 by the record's own rule at St >= 1 (q3 fails; q2 fails as pre-registered; RED_TEAM
read 1/5 as written). COST(hybrid) = [7, 10]; COST(incumbent) = [7, 10] (F2 4-6 remaining 3-5 + F3 3-4 = 6-9 per RED_TEAM :337, +1 with A-5).
Criterion: DOMINATES iff COST_hi(R) <= COST_lo(I) − 1 -> 10 <= 6 is FALSE. The hybrid does NOT dominate under LOG-2; it wins on CRED at equal cost.
GO MAP consequence (:115), as the advocate reads it: "incumbent = PILOT-arm / design-loop half of a hybrid tuple -> GO-CON-PILOT", NEXT = F2.REPR with
the pilot's kill criterion = LEG A/LEG B above, window = F2.ENGINE exit, cost = 3 wave-frame marches + K per-phase marches + the G12-L1-3D brick.
This is a road CORRECTION (evaluator field + three protocol increments), not a RE-PLAN; I do not claim NO-GO.

## 6. CONCEDED (what the hybrid does not buy, and where the refuter is right in advance)

- Argmax half: the evaluator licenses NO argmax-shift number (OPTSHIFT SCHEMA-only; delta and L_H UNDERIVED, M0 :1348 (vi)); the trees' abandon
  test (|J_3D − J_red| on the final pair < |D|) is VALUE-level — the record is stricter (SP0 §4 half 2). Only road (d) at marching cost (rho <= 1)
  discharges it by construction; the hybrid's designer inherits it exactly as the incumbent does.
- Legality: B-lite/route-B fail near the axis of a full bell and in the plug pocket (§3); the annular plug is the FAVOURABLE case (H L5) but the
  pocket is closure-bound for every road. H20 free-plume solve mechanics are homeless of record (findings :2519 via SP0 §3 q2).
- The 3-D unit process is unbuilt and its "marching cost" unmeasured; my +1 session is an estimate, not a record number.
- Rothalpy-Jensen pool 0.15-0.5% (H L3) and r*/R 0.4-0.7 (H L5) are [SE] tree estimates, unverified; Wang & He 2010 / Alexandrov-Lewis /
  Lakshminarayana 1996 are [APERTO] — PROCUREMENT ASK: Wang & He 2010 (rotating-frame discrete adjoint; needed to bound the tier-(2) Lemma-B
  lift against the only published rotating-frame adjoint precedent) and Alexandrov-Lewis 1998-2001 (first-order corrected TR model management;
  needed only if LEG B lands in 1 < rho < 10). Neither is load-bearing for §1-§5.
- Certification version-binding (M0 :4250-4271): the wave-frame evaluator is a forward march under the same recorder/env discipline; it inherits the
  A-1 margin rule, it does not escape it.

## 7. Position in one paragraph

Design where gradients are cheap and certified (the record's per-phase engine, unless LEG B shows the helical march is as cheap); EVALUATE every
competitor where the objective is exact on the pin ([T-T0]) with an instrument the record already owns and already owes to M-RED; screen first;
field the strongest classical opponent; derive the G3 gate from the ladder's slope. At the MEASURED St of the decisive sector this is not a preference
but the record's own license rule executed; it costs +0..1 session, raises CRED from <= 3 to 5, and is the only road whose content survives every
branch of the user's cost fork. Agreed falsifier = §1 LEG A + LEG B, pre-registered, owner F2.REPR (C51) / F2.ENGINE first act.
