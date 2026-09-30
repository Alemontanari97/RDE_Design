# RED TEAM — THE DECISIVE NUMBER, Q2 -> Q0 (S-REVIEW order 6; carrier §C.6 + §G.4; refuter PROMPT-45; 2026-09-05)

Persona: the skeptical JPP referee who will judge the decisive number, with an RDE test engineer at the
elbow. Object attacked: the EXPERIMENT and the QUESTION of `validation/TWIN_PROTOCOL_preregistration_2026-08-31.md`
(the TWIN), not the machinery. Consumer: the S-REVIEW orchestrator and the Stage-B road judge (§B dominance
criterion); downstream consumer of the amendment table = the F3.TWIN executor via the protocol's §9.
STATUS OF EVERYTHING BELOW: PROPOSED, DA RATIFICARE. Nothing was applied; no file other than this one was
written; no package installed; GENO/ untouched; git not run.

Read integrally, in the brief's order: TWIN protocol §1-§9; `PROBLEM_STATEMENT_agnostic.md` (§0-§9);
`st_scoping_number_run.log` ([X-STSC]); D6 :779-786, :1133-1157 (+ :214-227, :156-172, :1159-1201);
problem book :451-478, :522-575 (+ :337-363, :495-512); M0 :25-62, :746-760, :2294-2310, :4250-4299
(+ :1336-1352 forchetta, :2436-2456, :3140-3160, :498-512, :865-880); choice ledger C61/C57/C59; decision map
Stage 7-8; `BASE_PRESSURE_HARVEST_c4.md` (§1-§15 + CONSOLIDATED); ADR panel :126-146; S24 F1b log rows 14/16;
findings rows twin-protocol:preregistration-2026-08-31, record-path:cert-verdict-recorder-dependence,
variational-driver:objective-omits-throat-panel, claims:engine-level-staged-evidence-hierarchy-missing (+ the
R8 base-pressure and H20 rows); `REFUTER_prompt.md` PROMPT-12/13/14/45 and §B/§C/§D; `INCUMBENT_pointers.md`;
`docs/literature_registry.yaml` (status of every source quoted).

Conventions. Anchors are file:line of the record. [KNOWLEDGE] items carry author/year and the registry depth
marker (READ-INTEGRAL / READ-PARTIAL(triaged) / WANTED = snippet depth, identity only / UNVERIFIED = not in
the registry, quoted through the harvest). Evidence classes of the harvest are kept ([ADV-CFD] = context only,
never a band input, CT-6). "Referee arithmetic" = arithmetic done in this file for the argument, NOT of record.
Compatibility with the pre-registered §B: each amendment names the CRED question (q1 anchor / q2 opponent / q3
budget / q4 reproducibility / q5 generalization) it moves, so the Stage-B judge can score it; cost is given in
sessions or hours against ISS-4 (F2 4-6 sessions incl. B0 consumed, F3 3-4, 3 h decisive runs/session, max 2
decisive campaigns per instance; D6:160-171, :214-227) and the statement's §8 ceiling (7-10 sessions total).
SP-PB / SP-CARM / SP-VAL of PROMPT-12/13/14 are the sub-problems A-2 / A-3 / A-4 instantiate.

## RT-1 UNCERTAINTY BUDGET BEFORE ANY RUN

ASKS: "Before you run anything, show that 1% is resolvable above the SUM of the terms you cannot compute away."
RECORD TODAY (per term):
- p_b closure on the truncated plug: NO number ("base-pressure model-form UNPRICED on truncated plug", M0:1347;
  C61 NEVER; residue R-8: no truncated-plug RDE base measurement exists anywhere in the read corpus, harvest
  CONSOLIDATED (a)). Brackets that exist: best classical pure-empirical p_b model [+19%, -15%] on COLD data
  [Onofri 2002 WG10, READ-PARTIAL(triaged), harvest §14]; the practiced Veen 0.846 p/M^1.3 = a 1966 near-wake
  curve fit, FAILED per WG10 [Fick-Schmucker 1996, UNVERIFIED at primary, via harvest §14]; RDE-specific departure
  on the NOZZLELESS base 0.59 atm (detonation CFD, 5 hot-fire CTAP tests follow it) vs 0.95 atm constant-pressure,
  "eightfold base drag" [Harroun-Heister-Ruf 2021, READ-INTEGRAL, harvest §1.2, ADV-CFD + ADV-EXP-HOT]; counter-
  datum "no substantial change" on an airbreathing TRUNCATED aerospike [Schwer 2018, WANTED, snippet]; the only
  hot-fire source's verdict: neither classical model "appropriate for predicting base pressures with an RDE cycle"
  (Harroun 2021 p. 669, harvest §1.2). Base-force scale: ~5% of thrust at 20% truncation, high PR [Ito 1999 via
  WG10, UNVERIFIED at primary, ADV-CFD]; ~12% of gross thrust [Schwer-Kailasanath via Kaemming-Paxson 2018,
  READ-INTEGRAL, ADV-CFD]; -9.5% nozzle thrust [Paxson-Miki 2022, READ-INTEGRAL, ADV-CFD]. Design-level
  sensitivity: a closure swap moved the optimum base height x2.45 and the tip slope -13.26 -> -3.08 deg at +0.26%
  thrust [Humphreys-Thompson-Hoffman 1971, READ-INTEGRAL, harvest §13]. Referee arithmetic: base force 5-12% of
  thrust x closure band 15-19% = 0.75-2.3% of Isp on the ABSOLUTE value = the size of the materiality threshold
  itself, before any RDE factor (0.59/0.95 = 0.62 on the nozzleless base; transfer to the plug = declared ANALOGY).
- frozen vs equilibrium: [T-EQBR] equilibrium ceiling +6.3..+7.0% above frozen on the internal instance, bars
  <= 0.003 s (M0:2436-2445); per-champion re-execution = standing duty P-F14 (M0:1347); both arms frozen (pin P1).
- mu shape: log-uniform is THEOREM for the exponential blowdown ([T-O2] M0:498-503) but the blowdown is the
  case-A generator's MODEL (Annex B :1142); J is linear in mu, so |J(mu')-J(mu)| <= osc(F)*||mu'-mu||_TV
  (D6:1043-1048, item 15, PROPOSED, "BEFORE any case-C Verdict"); the convention sweep {time, mass-flux,
  log-uniform, atomic empirical} is named with its carrier UNBUILT (M0:868-876). No number for the TWIN family.
  The family's spread is CJ-based (PR 49.2 at phi 1.66 / 45.1 at phi 1.00, st log) while a nozzle interface sees
  a smoother field (interface std dev ~70% of means, throat total Mach 1.05-1.65 [Paxson-Miki 2022, READ-INTEGRAL];
  throat axial Mach 0.86-1.33 [Kaemming-Paxson 2018, READ-INTEGRAL]).
- discretization: two-level Richardson x K_RICH = 4 (M0:3265); F1b: pre-registered band 5.38e3 vs +2.04e5 excess
  (38x) WITH the measured under-inclusion caveat — the class-representation error SATURATES M -> 2M (5.679e-3 ->
  5.595e-3), crude systematic ~6e4 = excess/3 (S24 log :110). The plug adds the H20 free-boundary solve with no
  discretization precedent (findings plume:free-boundary-solve-mechanics-missing, path critical).
- O(St): St_plug in [0.268, 1.415]; 0.73-1.41 at the record head count (st log ENVELOPE); no J_1 number exists
  (D6:783-786: G3's "large" never a number; M0:1343 channel (i) WORST "unquantified of record"). See RT-7.
GAP: four of five terms have no number on the decisive sector; the fifth carries a caveat that it under-covers
the representation systematic. TWIN §6 names only "Richardson + certificate-stack terms + representation-class
term": nothing forbids quoting MATERIAL with the p_b term unpriced, and the absolute p_b uncertainty alone is
threshold-sized. What matters is the closure-sensitivity of the DELTA (Humphreys: argmax O(1), value O(0.3%)) —
unmeasured.
PROPOSED A-2 (2026-09-05, DA RATIFICARE) — UNCERTAINTY BUDGET TABLE BEFORE ANY ARM RUN: rows p_b / thermo / mu /
discretization+representation / O(St) / optimizer basin (A-8). Producers, all EVALUATION-ONLY on the two final
designs: >= 3 closures spanning the WG10 bracket endpoints plus the 0.62 suction factor as a labeled analogy;
the equilibrium tables (P-F14) on both champions; the convention sweep + ONE PR-halved family; the M-RED-measured
representation term; St per A-7. Rule: a branch is quotable only if INVARIANT under every row's sweep; a row with
no producer caps the outcome at INTERMEDIATE by rule; the re-DESIGN sweep at the closure endpoints is owed only if
the evaluation sweep flips the branch. Seeded rejector: a Verdict whose p_b row is empty must be refused.
EFFECT: credibility — converts "1% with a 0.5-1% band" into a checkable budget (statement R-iii); q3 0 -> 1.
Cost — hours inside the TWIN session (S25 class 0.116 s/solve on the bell, ledger C57 note; plug forward solve
UNPRICED until F3.PLUG lands H20); +1 campaign per closure endpoint only on a branch flip (F3 cap: 2/instance).

## RT-2 THE STRONGEST OPPONENT

ASKS: "A competent aerospike designer designs for a design NPR, truncates to the envelope, and today ranks
candidates on cycle-averaged CFD. A mean-state plug is a straw man — and your own T4 says the plug wants the peak."
RECORD: TWIN §4 arm C = "classical design of the SAME geometry class at I4 (<Pc>, T0, gamma) ... (Rao-class plug /
peak design at mean point)" — one program-chosen opponent; the wording conflates peak and mean. PB-2 itself names
TWO baselines, "peak- and mean-designed" (PB :532-536). The field's actual practice is a crude cycle-aware sweep:
7 designs on two OFAT lines with cycle-averaged thrust as the objective, no optimizer [Paxson-Miki 2022,
READ-INTEGRAL, registry :249]; the record flags "best-of-sweep != argmax ... ranking-signal only" (M0:1338). The
classical plug optimum WITH base term treats p_b as an iterated constant, "independent of the model" [Humphreys
1971, READ-INTEGRAL, harvest §13]; truncated-ideal-plug practice with cold-flow scaling [NASA SP-8120 1976,
READ-PARTIAL(triaged), harvest §15]. Constraint identity (§5) fixes eps, L, truncation, closure, floors — but the
classical family's DESIGN STATE is not a constraint: the protocol fixes it at <Pc> by fiat. No duty-weighted
classical arm exists in the record (grep "duty-weighted|mean-designed": only PB-2's baselines).
GAP: (a) a MATERIAL delta vs the mean-state plug does not separate METHOD from DATA — arm P consumes the whole
family, arm C only its mean; a designer who picks the best design state on a cycle evaluator may close the gap;
(b) "peak design at mean point" is not an executable specification; (c) the referee's first counter-arm is absent.
PROPOSED A-3 — ARM C* (classical family best-on-mu): the SAME classical construction swept over its design state
P_d in [P_CJ/PR, P_CJ] (and its base-slope parameter where the family has one), each candidate EVALUATED on the
same mu, closure, truncation, eps, L; C* = argmax of the sweep (10-20 forward constructions). §6 decision rule read
on delta* = (Isp_P - Isp_C*)/Isp_C*; delta vs C (mean member) and vs C_peak reported as context rows. §4 repaired:
C = mean-state member, C_peak = peak member, C* = mu-best member of the classical family. Falsifier (PROMPT-13's):
delta* < band while delta > 1% => the gain was DATA, not METHOD — publishable as such.
EFFECT: credibility — q2 0 -> 1; the claim becomes "beats the competent designer's cheap cycle-aware practice",
the only version a JPP referee does not dismiss. Cost — hours (forward constructions; on the plug each needs the
H20 solve arm C needs anyway).

## RT-3 EXTERNAL ANCHOR

ASKS: "Both arms run in your engine with your certificates. What OUTSIDE your machinery tells me a 1% delta is
real — a second code, a high-fidelity computation, an experiment — and at what accuracy class?"
RECORD: cross-code = GENO read-only oracle; on the plug sector GENO RaoPlug carries the S1/S2 bugs (B-RAOPLUG,
critical, "APERTO, mai attaccato", PROGRESS BLOCCATO; F3 ENTRY D6:214-218); fallback = single-oracle status on the
spike Table-1 point M_E = 2.4, gamma = 1.23 -> eps 3.81, X_D/R_E 1.164, C_F 1.58 [Rao 1961, READ-INTEGRAL; TWIN §8]
— gamma = const, ONE point, no var-gamma oracle. High-fidelity = R22-CFD-2 (Li-Xu template paired demo, F2 tail,
critical) = an ADEQUACY check of the 2D-per-phase reduction, not a validation of Isp (M0:1346 channel (iv),
"R22-CFD-2 (Harroun pair, field-facing)"); CFD-1 (~12M cells) = user decision post-M-RED (B-CFD1 critical).
Experiment: none guaranteed (statement §8); thrust-stand class = NOTE, no row (D6:779-782). The only published
discrimination datum for an averaged method: cycle-averaged CFD gives C_F = 1.25 IDENTICAL for two aerospikes the
experiment separates [Harroun 2021, READ-INTEGRAL, registry :273] — at verified limits "no thrust measured"
(M0:1346): a FIELD-level datum, not a delta-level one. Thrust-measured multi-nozzle RDE data exist only as WANTED
rows [Goto et al. 2019 JPP 35(1), vacuum-chamber aerospikes; Fotia et al. 2016 JPP 32(3); snippet depth,
UNVERIFIED beyond identity]. P34 staged-evidence hierarchy: never adjudicated (findings :2740, path paper).
GAP: no delta-level external anchor exists or is planned inside the budget; arm C has no independent construction
on the plug beyond one gamma = const point; §6's MATERIAL wording ("the method PAYS") carries no evidence stage.
PROPOSED A-4 — EXTERNAL ANCHORS: (i) arm C independent construction: GENO RaoPlug S1/S2 fix landed OR single-
oracle status declared IN the protocol with the var-gamma gap named (arm C at var-gamma prints "cross-code:
unanchored"); (ii) F2.CFD-2 registered as the TWIN's FIELD-level anchor with a prediction-first clause: the reduced
per-phase prediction on the paired demo is written BEFORE the 3-D field is read; (iii) the thrust-level anchor
DECLARED ABSENT with its procurement path (Goto 2019 / Fotia 2016 as Annex-B case-C calibration data, B12 class)
and every public wording carries the P34 stage "in-model, field-anchored, thrust-unanchored".
EFFECT: credibility — q1 0 -> 1 at field level (named deliverable already on the critical path); the referee gets
the honest evidence stage instead of an implied one. Cost — (ii),(iii) zero beyond CFD-2 (priced in F2); (i)
external repo, unpriced, or zero by declaration.

## RT-4 GENERALIZATION FROM n = 1

ASKS: "One propellant, one chamber pressure, one annulus, one truncation. What does MATERIAL license? What does
SMALL license? Which second point would convince me it is a trend and not a coincidence?"
RECORD: TWIN §3 pins CH4/O2 (the exercised table class), numeric instance at F3.TWIN opening. The theory names the
DRIVERS of the cycle-vs-mean gap: spread of mu and constraint tightness — "spread -> 0 => sectors tie at the Rao
value (T3); generous envelope => free boundary attains the ceiling (T4/M1); tight length + large spread => duty
split" (M0:2450-2456); T4's nesting fails only under truncation (PB :532-536). The two families of record have PR
49.2 and 45.1 (st log) — the same spread; the 600 N annulus moves St and scale, not spread; St on the plug drops
~25% from 20% to 40% truncation (st log St_plug columns).
GAP: no second point, no generalization wording: MATERIAL as written ("the method PAYS on this sector at this data
class", §6) is a CLASS statement from one instance.
PROPOSED A-5 — SECOND INSTANCE WITH PREDICTED ORDERING: (i) wording: MATERIAL = EXISTENCE claim ("at least one
instance where the field's practice is measurably suboptimal at case A"); SMALL = instance-scoped (A-9); (ii) a
second point moving a theory-named driver, chosen at the instance pin: truncation 0.40 at the same family (cheapest:
same tables, same mu; moves T4-break depth and St together) or a PR-halved family (moves spread); (iii) PREDICTION
FIRST: the bound-ladder gap of both instances computed and the predicted ordering of delta written BEFORE the second
campaign (P34 light instantiation); a wrong ordering = the theory's own falsifier fired, reported as such.
EFFECT: credibility — q5 0 -> 1; two points with a pre-registered ordering is the minimum a referee accepts as a
trend. Cost — +1 campaign pair = +1 session inside F3 (cap 3-4; "2 campaigns per instance" is per instance).

## RT-5 IS NOZZLE Isp THE RDE LEVER AT ALL (Q0 objective axis)

ASKS (the engineer): "Your losses are elsewhere — base drag, swirl, sizing, backflow, mode hopping, separation.
Why should I care about 1% on a contour? Show me operability first."
RECORD: nozzle-side losses at CONFIGURATION scale are the largest numbers in the read corpus: a real truncated plug
at 58.1 -> ~71.5% of the notional ideal at FIXED area ratio, "larger than the entire area-ratio design line"
[Paxson-Miki 2022, READ-INTEGRAL; M0:1345 worst-direction marker; M0:2542 "honest discount on advertised pressure
gain"]; steady M = 1 sizing misses the optimal area ratio by ~31% (registry :249); base areas ~12% of gross thrust,
swirl energy +6% EAP_i CFD / +3% exp [Kaemming-Paxson 2018, READ-INTEGRAL]; 8x base drag on the nozzleless base
[Harroun 2021]; "+1% Isp flared", second-hand [Harroun 2020, READ-INTEGRAL]; 3-7% stagnation pressure at eps 80%
[Fotia 2016, WANTED, snippet]; NASA treats the nozzle as a manufacturing subcomponent with a 4-scalar sweep
[Teasley 2025, READ-INTEGRAL]. IN-CLASS contour deltas are fractions of a point: Hoffman scale 0.04-0.34%, ours
+0.51% (M0:1346 channel (iv)); the field's averaged evaluation is BLIND at that scale (Harroun C_F 1.25 flat).
Operability: attached flow at every phase is a state constraint of the certified class (statement §4; PB-5 robust
layer); side load = declared SECONDARY OUTPUT for n >= 2 (M0:265-273; side_load.md); backflow/combustor coupling
= H-AM4 declared exit (M0:1677), out of the nominal by pin.
GAP: the TWIN is an in-class comparison (same sector, truncation, eps, closure): it lives exactly at the scale where
the field's data say averaging is blind and thrust stands cannot see, while the lever the engineer recognizes sits
at tens of points. §6 relates the delta to nothing outside the pair and reports no operability per arm. A referee
accepts mean Isp as THE metric only with operability as a REPORTED constraint status, not an unstated one.
PROPOSED A-6 — VALUE STACK + OPERABILITY ROWS in the TWIN Verdict: (1) delta* in-sector (A-3); (2) each arm vs the
practice baseline = the bell designed at <Pc> at the same c (classical BY THEOREM at case A, T3, Annex B :1142;
ADR :126 KEY FINDING 4: the truncation default alone flips the spike-vs-CP sign at 30%); (3) the bound gap
J_ideal - J(arm) (post-processing, Annex B invariants; M1 duality-gap-zero M0:2446-2449); (4) per-phase separation
margin g_sep and the side-load proxy per arm. Rule: MATERIAL on Isp with a WORSE operability margin than C* =
"CONDITIONAL", never a clean win. O-b stays P_amb = {Pa0} by the P_amb slot (PB :551-573), declared, not first.
EFFECT: credibility — the engineer's first objection answered with the record's own configuration-scale numbers;
the 1% becomes legible ("small next to sizing/base/operability; here is where the method's value sits"). Cost —
rows (2)-(3) post-processing + one bell design of the [X-TOCV] class; row (4) reads existing certificate fields.

## RT-6 Q2 vs Q0

ASKS: "Does the head-to-head tell me HOW to optimize an RDE nozzle, or only that cycle design beats mean design on
one plug? If another experiment answers Q0 better at equal cost, which?"
RECORD: TWIN §1 = "does the per-phase method BEAT the classical fixed design ... on the sector where the break
theorem lives" = Q1 restricted to channel N2. Q0's deliverable (statement §0) = methodology + certificates + ONE
number + publishable either way. The road's Q0 answer of record is "the MEASURE SELECTS THE TOPOLOGY", configuration
as OUTPUT (OP-11, M0:47-52; PB :337-363 finite sector tournament, SCHEMA), whose executable step is F3.TOURNAMENT
(D6 addendum :1187-1201: fallback = two-sector bell vs plug, 1-2 sessions after F3.PLUG; roadmap path NON-critical).
At case A the bell sector is classical BY THEOREM (T3), so the tournament's information at case A is the sector
CHOICE plus the plug-sector gain — of which the TWIN is the plug-sector row.
GAP: the TWIN fixes configuration, data class and comparator: it answers Q1(N2). MATERIAL plus nothing does not say
what a designer should build; SMALL plus nothing says "Rao at <Pc> on bells (theorem) and the classical plug" —
which IS a Q0 answer at case A, but only with the bound gap (A-9) and the sector row.
PROPOSED A-10 — Q0 EMBEDDING, tuple: (configuration: OUTPUT of {bell, truncated plug} at the true c; data class: A
+ the A-2 sweeps; comparator: the competent designer's best classical choice across both sectors = max(bell at <Pc>,
C*), the strongest because it is what practice fields today; metric: cycle-averaged Isp + bound gap + operability
margin; accuracy: thrust-stand 0.5-1% + the priced model-form rows; outcomes: (a) S*(c) beats the designer's best by
> band -> Q0 answered positively at case A, gated D-44 + G5; (b) within band -> "two-sector classical practice is
adequate at case A; the road's value = certificates + the sector choice as a theorem"; (c) S*(c) loses -> kill).
The TWIN stays its plug-sector row; F3.TOURNAMENT(fallback two-sector) proposed as a critical-path override
(roadmap tool, user decision). REPLACE not warranted: the tournament CONTAINS the TWIN.
EFFECT: credibility — the number becomes Q0-shaped (what to build) instead of Q1-shaped (which method). Cost —
+1-2 sessions on top of the 6-9 remaining to the TWIN (F2 3-5 + F3 3-4) -> 7-11 vs the statement §8 ceiling 7-10:
AT THE CAP; the user prices it.

## RT-7 THE St NUMBER ON THE DECISIVE SECTOR

ASKS: "Your plug has St_n up to 1.4 at the head count your own examples predict. Your problem book says rung 2
without an St error bar is out of contract. What licenses a per-phase delta there?"
RECORD: [X-STSC] MEASURED 2026-09-05: plug class St_n in [0.268, 1.415]; at the record head count, 10 kN n = 3 ->
1.09/0.95/0.82 (T_CJ) to 1.41/1.24/1.06 (end-of-cycle T0) at 20/30/40% truncation; 600 N n = 2 -> 0.73/0.64/0.54
to 0.94/0.83/0.71; n = 1 -> 0.36-0.47 at 20% (st log). LICENSE RULE of record: St >= 1 -> "frozen-time rung alone
NOT defensible, wave-frame/unsteady rung REQUIRED"; 0.1 <= St < 1 -> corrector MANDATORY (st_scoping_number.py
docstring; PB :466-478 "Any hardware conclusion from rung 2 without an St error bar is out of contract"). No J_1
number exists (D6:783-786; M0:1343); routes exist on paper (M0:3150-3156 VI.4bis(ii): unsteady comparison O5, or
ONE linearized sweep-perturbation solve on the wave-frame anchor; S-P4F THEOREM* Fredholm reduction, falsifier O5);
the exact backstop is T0 (wave-frame steady 3-D, [S-BLITE] route-B; C51 NEVER, decided at F2.REPR). Caveats of the
St number itself: quasi-1D u (PRACTICE), wave speed U_CJ (a deficit LOWERS St), R_lip ~ R_bar, certified-march tau_n
= F2.ENGINE upgrade. Both arms sit on the SAME rung, so delta is a rung-2 delta; J_1 is a per-design cell problem and
acts on the two designs differently.
GAP: the decisive sector is the St-WORST sector of the program — the theorem's arena (truncation breaks T4) is the
arena where the reduction is least licensed. The protocol has no St field, no scope declaration, no corrector row
in §6, and its backstop depends on an A-REPR outcome the fallback (4-field axial, D6:1185) does not provide.
PROPOSED A-7 — St DISCIPLINE: (i) the instance pin (§3) prints St_n per arm from the certified march and the head
count with provenance; (ii) St_n < 0.5 -> rung-2 delta quotable with the corrector as a NAMED residual row of A-2
(owner F5b); 0.5 <= St_n < 1 -> the corrector term (one linearized solve per arm) MANDATORY in the band stack before
any branch is read; St_n >= 1 -> NO branch quotable from rung 2: either both FIXED designs are re-evaluated in the
wave frame (T0, forward solve only, route per A-REPR) or the instance is re-pinned to a head count/truncation with
St_n < 1 and the record head count is printed as the scope boundary; (iii) every public wording carries "rung-2
delta at St_n = x" until (ii) is met. Seeded rejector: an instance pinned at St_n = 1.2 without a wave-frame row is
refused.
EFFECT: credibility — without (ii) a referee who reads PB §8 rejects the number by the program's own rule; with it
the delta carries the missing error bar (q3). Cost — the linearized corrector is engine work not yet built (F5b):
UNPRICED; the wave-frame forward evaluation exists only if A-REPR pins route-B; the re-pin to n = 1 is free but
narrows the claim to a head count the record's own 10 kN example calls unlikely (W ~ 3.14, st log inputs).

## RT-8 REPRODUCIBILITY

ASKS: "You measured PASS/FAIL flipping with recorder and version near the bound. Is 'certify with margin under a
pinned recorder' enough? What must BOTH arms re-run, and is arm P's optimum a property of its start?"
RECORD: certificate = property of (code tree, active recorder, env fingerprint), MEASURED on three instances
(M0:4254-4271: X-CDKAT cert_worst -13.9% under env change, structure unchanged; X-LOCD binary flips on cert-marginal
designs cert_worst 1.06-2.46 between per-column and per-cell recorders; X-AKNO same outcome class, different
frontier; findings :319). A-1: cert_worst <= 1/K_RICH = 0.25 under the pinned recorder; (0.25, 1] cert-marginal,
quotable only if BOTH recorders PASS; seeded test at 0.9. envfp REQUIRED on every ondemand stamp, env change =
declared re-stamp duty (closure-aware staleness gate of F2-B0). F1b: both designs certified, band caveat declared.
The optimizer is local-only of record (C57 MIXED); three certifiability-limited exits at healthy margin
(S20/S22/S24, class-construction mechanism); the F1b start = perturbed feasible start, 1.5% sine bump (X-DEFTW).
GAP: (a) R-TWIN-0's hash set names config/data/constraint but not code tree, envfp, recorder, table hashes, start
recipe; (b) A-1 prints the second recorder only for marginal designs; (c) nothing addresses the optimizer basin:
a local argmax from one start is a property of the start; (d) arm C has no independent reproduction on the plug.
PROPOSED A-8 — REPRODUCIBILITY: (i) R-TWIN-0 hash set := {protocol + amendments, code tree hash, envfp, active
recorder, thermo table hash, mu hash, A-REPR, start recipe}; (ii) BOTH final designs re-certified under BOTH
recorders regardless of margin (4 cert_worst values printed; two cheap forward certifications); (iii) >= 2 starts
for arm P (multi-start on the existing branch machinery = C57 alternative 3) with the spread of J_P across starts as
the optimizer-basin row of A-2; spread > band caps the outcome at INTERMEDIATE; (iv) any envfp change after an arm
run re-fires R-TWIN-0 for BOTH arms; (v) arm C reproduced by A-4(i) or printed "unanchored".
EFFECT: credibility — q4 stays 1 but becomes referee-checkable (statement R-vi: a result is a property of the triple
and is OWNED when it does not reproduce). Cost — (ii) minutes; (iii) the second start IS the second campaign of the
F3 cap; (i),(iv),(v) zero.

## RT-9 NEGATIVE OUTCOME

ASKS: "If SMALL, what does the paper claim, and why should I believe the classical design is adequate rather than
that your optimizer, your class or your instance could not see the gain?"
RECORD: §6 SMALL = "the literature is right at this rank — the classical fixed design is adequate at case-A data on
this sector; publishable honest outcome; program pivots per the G2 wording". G2 = "bound-ladder gap per channel;
gap < ~1% Isp on all of N1-N4 -> pivot" (D6:777-778): the bound gap is the record's OWN adequacy instrument
(J_ideal = post-processing, Annex B invariants; M1 duality-gap-zero, M0:2446-2449). Isp_spike(eps) is plateau-flat
above the knee (ADR :126 KEY FINDING 4): a flat objective yields SMALL by insensitivity. Three certifiability-limited
exits at healthy margin (S20/S22/S24): SMALL can be a class-construction artifact. The T4 break grows with truncation
depth and with the base regime (open vs closed wake, transition Pa/Pc ~ 0.15 [Harroun 2021]; the Nasuti-Onofri
transition-PR model = the only validated classical regime classifier, ~5% on cold rigs [via WG10 harvest §14,
UNVERIFIED at primary]).
GAP: SMALL as written is an argument from silence: it asserts adequacy from the absence of a resolvable delta without
excluding (a) an unreached gain (bound gap >= 1%), (b) instance insensitivity (mild truncation, closed wake, flat
objective), (c) optimizer/class limitation. A referee asks for exactly these three.
PROPOSED A-9 — SMALL CO-REPORT: SMALL is quotable only with (a) the bound-ladder gap of both arms — SMALL and gap
< 1% = "adequacy by bound" (theorem-shaped negative, the G2 pivot); SMALL and gap >= 1% = "gain exists, unreached by
both arms" -> NOT "the literature is right": it triggers the C57 exploration pilot and the C7 class-enrichment leg
BEFORE any pivot; (b) the instance scope printed: truncation, base regime by the transition classifier, PR spread,
St_n; (c) the value stack of A-6; (d) the second point of A-5 whenever the first is SMALL (SMALL at 20% + closed wake
does not license SMALL at 40% + open wake). Paper wording pre-registered per branch (P34 light instantiation).
EFFECT: credibility — the negative result becomes a scoped, bound-backed statement; without (a) it is unpublishable.
Cost — (a)-(c) post-processing; (d) = A-5.

## RT-10 ANYTHING ELSE A REFEREE ASKS FIRST

ASKS (in reading order): (1) "Your case-A inflow is a MODEL — provenance, and how does its spread compare with an
engine's?" (2) "Where is the plume boundary solved and certified for the plug?" (3) "Is the annulus choked at all in
your data class?" (4) "How were the arms started?" (see RT-8) (5) "Is the near-vacuous constraint tolerance repaired?"
RECORD: (1) case A = Cantera CJ/HP -> S-H matching -> exponential blowdown (Annex B :1142); the 18/18 Table-1
fidelity is to a 0-D model [Stechmann-Heister-Harroun 2019, READ-INTEGRAL, registry :318], not to an engine; the
family's top state is P_CJ while a nozzle interface sees a smoothed field (RT-1); the protocol prints no provenance.
(2) H20 free-plume solve "no home in the record", genuine FORK-141 gap (findings row, path critical); TWIN §8 lists
it as an F3.PLUG prerequisite WITHOUT a rejector. (3) U3' RDE choking PREMISE-OPEN until F2a closes (D6:191-202,
:267) while S-H matching presumes a choked annulus. (5) TWIN §5 item 1 names the cross-unit tolerance repair as
pre-run — CONFIRM. Also CONFIRM as written: R-TWIN-1..6, the case-B flip clause of §3, the two-stage instance pin.
GAP: (1)-(3) are premises the protocol consumes silently.
PROPOSED A-11 — PREMISE ROWS: (i) a DATA PROVENANCE row in every arm Verdict: generator chain + hashes, PR spread,
choking status of the annulus (U3' verdict of record or "premise open"), with the PR-halved sensitivity of A-2 as
the spread's own falsifier; (ii) R-TWIN-7 plume-boundary certificate: no certified H20 solve (vortex-sheet monitor +
free-boundary adjoint term) on an arm -> runs refused; (iii) CONFIRM §5.1 and R-TWIN-1..6.
EFFECT: credibility — the three silent premises closed at zero cost. Cost — (i) zero; (ii) = F3.PLUG's own exit.

## PROPOSED AMENDMENTS TO THE TWIN PROTOCOL (DA RATIFICARE) — none applied; §9 append-only, dated on ratification

| id | amendment | evidence anchor | effect on credibility | effect on cost |
|---|---|---|---|---|
| A-2 | Uncertainty-budget table BEFORE any arm run (p_b closure sweep at WG10 endpoints + 0.62 suction analogy; P-F14 equilibrium re-evaluation; convention sweep + PR-halved family; M-RED representation term; St; optimizer basin); branch quotable only if INVARIANT; no-producer row caps at INTERMEDIATE; seeded rejector on an empty p_b row | M0:1347; harvest §13/§14/CONSOLIDATED; M0:2436-2445; D6:1043-1048; S24 log :110; st log; TWIN §6 | q3 0 -> 1; R-iii checkable; the threshold-sized absolute p_b band is confronted at delta level | hours (evaluation-only) if the plug forward solve is O(1 s); +1 campaign per closure endpoint only on a branch flip |
| A-3 | Arm C* = classical family best-on-mu (design-state sweep at identical constraints); §6 rule on delta*; C (mean) and C_peak as context rows; §4 wording repaired | TWIN §4; PB :532-536; M0:1338; registry :249 (Paxson-Miki); harvest §13 | q2 0 -> 1; METHOD separated from DATA | hours (10-20 forward constructions) |
| A-4 | Arm-C independent construction (GENO RaoPlug fix OR declared single-oracle with the var-gamma gap named); F2.CFD-2 as prediction-first FIELD anchor; thrust-level anchor declared ABSENT with procurement path; P34 stage on every wording | D6:214-218; TWIN §8; M0:1346; registry :273/:1266/:1272; findings :2740 | q1 0 -> 1 (field level); evidence stage honest | zero (CFD-2 priced in F2); GENO fix external/unpriced |
| A-5 | Second instance moving a theory-named driver (truncation 0.40 or PR-halved) with the bound-ladder ordering predicted BEFORE the run; MATERIAL = existence claim | M0:2450-2456; PB :532-536; st log St_plug; D6:214-227 | q5 0 -> 1 | +1 session inside F3 (cap 3-4) |
| A-6 | Value stack (delta*; each arm vs bell-at-<Pc> at the same c; bound gap) + per-arm operability rows (g_sep per phase, side-load proxy); MATERIAL with worse operability = CONDITIONAL | M0:1345-1346; M0:2542; ADR :126; Annex B :1142; M0:2446-2449; M0:265-273 | engineer's objection answered with record numbers; 1% made legible | hours (post-processing + one bell design) |
| A-7 | St discipline: St_n per arm from the certified march; corrector mandatory at 0.5-1; no rung-2 branch at St >= 1 without wave-frame forward evaluation of both fixed designs or a re-pin; "rung-2 delta at St_n = x" wording; seeded rejector | st log; PB :466-478; D6:783-786; M0:3150-3156; M0:1343; D6:1185 | the program's own license rule enforced; the missing error bar named | corrector UNPRICED (F5b); wave-frame A-REPR-conditional; re-pin free but narrows the claim |
| A-8 | R-TWIN-0 hash set extended (tree, envfp, recorder, tables, mu, A-REPR, start); both recorders printed for both arms; >= 2 starts with the J_P spread as a band row; env-change re-stamp for both arms | M0:4254-4271; findings :319; X-DEFTW; C57; TWIN §9 A-1 | q4 referee-checkable (R-vi) | minutes; second start = second campaign of the cap |
| A-9 | SMALL quotable only with bound gap (adequacy-by-bound vs unreached gain -> C57 pilot / C7 leg), instance scope (truncation, regime, PR, St), value stack, second point; per-branch wording pre-registered | D6:777-778; M0:2446-2449; ADR :126; S20/S22/S24 logs; harvest §14 | negative result publishable, not an argument from silence | post-processing (+ A-5) |
| A-10 | TWIN embedded as the plug-sector row of the two-sector tournament table at the true c (comparator = designer's best across sectors); F3.TOURNAMENT(fallback) proposed critical | D6:1187-1201; PB :337-363; M0:47-52; roadmap §2 | Q0-shaped deliverable (what to build) | +1-2 sessions: total 7-11 vs the §8 ceiling 7-10 (user decision) |
| A-11 | Data-provenance row (generator chain, PR spread, choking status U3'); R-TWIN-7 plume-boundary certificate; CONFIRM §5.1 + R-TWIN-1..6 + case-B flip clause + two-stage pin | Annex B :1142; registry :318; D6:191-202; findings H20 row; TWIN §5/§7/§8 | silent premises closed | zero (R-TWIN-7 = F3.PLUG's own exit) |

§B scoring, my reading (contestable by the refuter/verifier from the anchors above): CRED(TWIN as written) = 1/5
(q4 only: A-1 + envfp discipline); CRED(TWIN + A-2..A-9) = 5/5 with q1 at field level; COST(as written) = 6-9
sessions to the first number (F2 3-5 remaining + F3 3-4); COST(amended) = same + 1 session (A-5) + hours, +1-2 if
A-10 is ratified. Seeded check on the criterion itself: a fictitious road with CRED 1 and COST 8-10 must NOT
dominate the amended incumbent; a road with CRED 5 and COST_hi <= 5 would — none was found in the record.

VERDICT: AMEND — CONFIRM the tuple (truncated plug / case A / per-phase vs classical / cycle-averaged Isp /
thrust-stand band / both outcomes pre-registered): it is the sector where the break theorem lives, and no
alternative tuple dominates it under §B (the one candidate with higher CRED, the two-sector tournament, CONTAINS
the TWIN and is proposed as embedding A-10, not replacement). As written the number is NOT referee-proof: no
uncertainty budget on a sector whose base-pressure band alone is threshold-sized, a straw-man opponent, no external
anchor, St_n up to 1.4 on the decisive sector against the program's own license rule, n = 1, and an unpublishable
SMALL branch. The ONE question the record cannot answer today: WHAT IS THE BASE PRESSURE OF A TRUNCATED PLUG UNDER
A ROTATING-DETONATION CYCLE — no measurement exists anywhere in the read corpus (R-8), the only hot-fire source
judges every classical closure inappropriate for the RDE (Harroun 2021 p. 669), the RDE departure is configuration-
dependent even in sign (Schwer 2018), and the closure moves the ARGMAX by O(1) (Humphreys 1971): the sign of delta on
the decisive sector can be BRACKETED from inside the record (A-2) but not certified against it until a V1.4-class
CTAP measurement on a truncated plug exists (procurement class, external).
