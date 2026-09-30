# STAGE B — ITEM EXP — ADVOCATE A0 (the alternative A-CARM, argued at its genuine best; S-REVIEW 2026-09-05)

Seat: GENUINE ADVOCATE of the alternative (stageB_items.json id "EXP"). Persona: the propulsion-journal referee
who has designed and fired aerospikes (the trees' propulsion lens) together with the record's SP-CARM judge.
Consumer: judge J2 (associate editor: quotability, strongest comparator, base-pressure reality) and the refuter
(TWIN author hat + variational/record hat). Scope rule honoured: every argument below is scored by whether it
changes the CREDIBILITY or the COST of answering Q0 by the road under review (the TWIN as the decisive
experiment), incumbent = TWIN §4-§6 as written, alternative = A-CARM (i)-(iv).

Read integrally in this window: stageB_items.json (EXP entry); stageA_diff_SP-CARM.md §0-§7; stageA_diff_SP9.md
§0-§6; stageA_diff_SP4.md §6 (rider A7); RED_TEAM_decisive_number.md RT-1..RT-10 + amendment table;
TWIN_PROTOCOL_preregistration_2026-08-31.md §1-§9; TWIN_amendments_PROPOSED.md; M0 :25-62, :746-765, :944-952,
:1334-1350, :1506-1522, :2294-2325, :2440-2460, :2560-2575, :3173-3188; problem book :522-575; D6 :770-786,
:1140-1157, :1178-1201, :137-159, :214-227, :160-172; src/thrust/stechmann_nozzle.py (docstring Step 5 +
bell_opt/spike_opt :411-434); PROGRESS_2026-08-12_S24_f1b.md steps 14-16; the four trees' SP9 / SP-CARM sections;
ADR_panel_2026-07-16.md :126-146; choice_ledger C57, C61; st_scoping_number_run.log; PROGRESS_2026-08-31_Sreview.md
LOG-2 (dominance criterion). PDFs opened on disk at the page (tier [IO]): Harroun-Heister-Ruf 2021 pp. 668-671;
Paxson-Miki-Perkins-Yungster 2022 pp. 1-5; Humphreys-Thompson-Hoffman 1971 pp. 1581-1587. Registry path for
Stechmann 2019 (PARENT/...) is NOT on disk in this window: that paper is used only through the in-repo validated
script (18/18 Table-1 fidelity, [IO] on the script) and M0 :2565-2572 ([REP]). No memory file read.

## 1. THE FALSIFIER I PROPOSE (both sides must agree on it before arguing)

Object: the F2.ENGINE arm-C builder (required by TWIN §4 anyway) on the pinned truncated-plug instance and the §5
constraint vector; values only; NO adjoint; run and READ before any arm-P optimisation starts.

 F-EXP-1 (design-state sweep, the RT-2 / SP-CARM §4 object). Build the classical truncated plug Sigma_C(xi_d) of
   the SAME engine at Dirac-mu(xi_d) for xi_d on a grid that contains <Pc>_mu (TWIN §4 as written), the
   mass-flux-weighted and thrust-consistent states (Opt C.4 root-find, one contour), and the cycle PEAK P_CJ
   (the T4 object / Stechmann knee). Same tables, same C61 closure object, same truncation fraction, same eps, L.
   Certify every member under A-1 (cert_worst <= 1/K_RICH under the pinned recorder). Evaluate every member on
   the SAME mu and representation as arm P. Report spread_C := max - min of J_avg over the certified members,
   and arm C* := argmax.
 F-EXP-2 (screen). Report two gap numbers on C*: (a) delta_ideal := (J_ideal - J_avg(C*))/J_ideal with J_ideal
   the geometry-free bound ([T-GB], M0 :2446-2452, post-processing per Annex B :1153); (b) delta_class :=
   (B_class - J_avg(C*))/B_class with B_class := Int_Xi max_{Sigma in class} F[Sigma; s(xi)] dmu(xi), the
   int-max bound of the T4 proof's own inequality (M0 :2304-2308: "the integral of maxima is an upper bound by
   monotonicity of the integral") — computed from the per-phase Dirac-mu optima at the quadrature nodes, i.e.
   from the SAME sweep family. B_class >= J_avg(arm P) for every arm P in the class, so delta_class bounds the
   reachable MATERIAL gain sharply; J_ideal bounds it loosely (see §3.5 for the grade of each).
 F-EXP-3 (base-area term). Print A_b of every member and of arm P; Delta_Ab := |A_b,P - A_b,C*| x Dp_b,band / F
   with Dp_b,band = the WG10 bracket [+19%, -15%] of the closure object (C61 :822).
Pre-registered readings (each side commits NOW to what it does if the number lands on the other side):
 R1  spread_C > band (0.5% abs on delta, TWIN §6 stop band)  =>  TWIN §4 "mean conditions only" is REFUTED as
     the strongest classical design; amendment A-CARM pins arm C := C* and adds the literature's fixed design
     (GENO RaoPlug / Rao-1961 spike class) as the ATTRIBUTION arm; delta of §6 is read on delta* =
     (Isp_P - Isp_C*)/Isp_C*; delta vs C_mean and vs C_peak are context rows.
 R2  spread_C <= band  =>  the comparator identity is IMMATERIAL on this instance; §4 stands with any member;
     the sweep is filed as the record datum on [T-T4] sharpness (PB-2's own "vs peak- and mean-designed
     baselines", problem book :532-536) and I WITHDRAW clause (i) of the amendment to a reporting row.
 R3  delta_class <= 0.5% (or delta_ideal <= 0.5%)  =>  the MATERIAL branch is unreachable by the class bound; the
     campaign pivots per the G2 wording (D6 :777-778) WITHOUT running arm P; SMALL is reached "by bound" (RT-9).
 R4  Delta_Ab > band/3  =>  base radius becomes a §5 pin (propulsion tree device) or the term enters the §6 stack.
Kill of the falsifier itself (declared): an engine that cannot certify a Dirac-mu classical plug at the peak
phase within the floors — then "peak-designed" is not a certifiable member; the sweep reports its certified
sub-range with the cause, and spread_C is read on that sub-range with the peak member printed "cert-limited".
What would make the PROGRAM change choice: R1 fires -> the comparator changes before any arm-P run (the
pre-registration mechanism working as designed); R2 fires -> the incumbent's comparator is confirmed with a
MEASURED reason instead of a fiat; R3 fires -> 3-4 sessions of F3 are not spent on an experiment decided by a
bound. Every outcome is a datum; none is a victory claim.

## 2. WHY "CLASSICAL AT THE MEAN STATE ONLY" IS A STRAW MAN ON THE TRUNCATED PLUG — the argument by elimination

2.1 The record's own theorems split the question by sector. Bell: [T-T3] (M0 :746-765) makes the classical
contour at the TIME-mean <Pc>_mu EXACT under H1-H4 at case A — Lemma C (affine in Pc) — with an executable rejector
that REJECTS the mass-weighted mean (tests/test_bell_optimality.py T1c; bell_optimality_proof :64-70, :98-101).
Free plug: [T-T4] (M0 :2294-2312) makes the PEAK-phase design optimal. Truncated plug — the TWIN sector (§2) —
is exactly where "a length cap L < l(xi_peak), a base-pressure model at a truncation plane ... break the nesting:
max Int < Int max STRICTLY" (M0 :2313-2316). No theorem of record selects mean vs peak vs flux-consistent there.
A comparator fixed "at the mean conditions only" on THIS sector is therefore a choice by fiat, not by theorem;
the very text of §4 betrays it ("Rao-class plug / peak design at mean point": a peak design is, by definition,
not at the mean point).

2.2 Under constraint identity (§5: eps, L, truncation fraction, closure object, floors, tables, mu, representation
all pinned) the ONLY freedom left to a classical single-state design is its DESIGN STATE. So the strongest
classical opponent is the argmax over the design-state family BY ELIMINATION (SP-CARM §2.2): no other classical
knob exists once §5 holds. This is also why the SP4 §6 rider A7 ("a 2-3-knob DFO tune of arm C on the cycle
measure moving Isp_C by > 0.5 x band falsifies arm C = strongest opponent") is not a separate object: under §5 the
tunable knobs collapse to the design state (SP-CARM A5 -> A4), so the rider IS F-EXP-1.

2.3 The field's practitioner baseline for a PLUG is the peak, not the mean — in-repo and page-verified. The
Stechmann-Heister-Harroun aerospike optimum is the saturation knee NPR(eps*) = Pmax/Pa with Pmax = P_CJ
(src/thrust/stechmann_nozzle.py docstring Step 5(c) and spike_opt :425-434: "saturation knee NPR(eps*) =
Pmax/Pa; verify plateau on sweep") — the bell optimum is at mean_t(Pc) (bell_opt :411-422). M0 :2565-2572 reads
their Figs. 10/12 as the T4 knee. Hence the literature's "fixed design" of a plug is a PEAK design, and TWIN §4's
"mean conditions only" is neither the literature's design nor the T4 object: it is the weakest member of the
family the record itself named as the pair of baselines (PB-2 :532-536; roadmap N2 per SP-CARM §0).

2.4 What a competent designer actually fields is a cycle-aware SWEEP, not a single state:
 - [IO] Paxson-Miki-Perkins-Yungster 2022, p. 1 (abstract): "Optimization is performed for a single operating
   point. Parameters varied are the overall nozzle area expansion ratio and the fraction of the expansion area
   that is provided by the shroud"; p. 3: "The baseline design is then perturbed by altering two of its geometric
   parameters ... Several perturbations are shown"; result 58.1% -> 70.0% of the notional ideal; p. 5: the
   limit-cycle criterion is "the cycle averaged thrust remained constant" (the objective is cycle-averaged).
   p. 2: "the unsteady and spatially non-uniform flow field ... renders common nozzle parameters such as pressure
   ratio, and throat Mach number ill-defined" — i.e. the field does NOT design at a mean state because it cannot
   even define one; it sweeps under the cycle objective. (The "7 designs on two OFAT lines" count is [REP] from
   the registry summary :257; the pages I read establish two parameters perturbed from a baseline.)
 - [IO] Humphreys-Thompson-Hoffman 1971, p. 1584 Table 1 + p. 1586: the CLASSICAL plug designer, at fixed length
   and mass flow, runs a 21-point parametric study over injection angle and cowl-lip radius; the thrust spread in
   Table 1 is 32,699 -> 32,881 lbf = 0.55% — the size of the TWIN §6 band. Classical practice = variational
   contour + parametric sweep of the free scalars, and the sweep moves the value by a band.
 - [IO] on the script: Stechmann Step 5 sweeps eps UNDER the cycle-averaged Isp (241-point grid + golden section).
So the strongest classical opponent is what the field does: a sweep evaluated on the cycle. TWIN §4 fields less
than the literature; a JPP referee will say so in the first paragraph of the review (RT-2).

2.5 METHOD vs DATA is NOT separable without the sweep. Arm P consumes the whole family {(P0,T0,gamma)(xi), mu};
arm C (as written) consumes one moment of it. A MATERIAL delta vs C_mean can be (a) the per-phase METHOD, or
(b) simply the DATA a mean-state design never saw. Only delta* against C* — a classical design that has SEEN the
family through the cycle evaluator but cannot USE it in the contour — isolates (a). The RT-2 falsifier is exact:
delta* < band while delta > 1% => the gain was data, publishable as such, but not as the method's value claim.
This is the credibility axis q2 of the pre-registered criterion (LOG-2), and the record scores 0 on it today
(RED_TEAM §B reading: CRED(TWIN as written) = 1/5).

2.6 Attribution arm (A7 of SP-CARM). The F1b bell twin measured a same-engine direct optimum EXCEEDING the GENO
DEF class representative by +0.51% at ONE state, both certified, with the band-under-inclusion caveat (S24 log
step 14, [X-DEFTW]; D6 :148-150). +0.51% sits INSIDE the §6 INTERMEDIATE band [0.5, 1]%. If arm C is "the
literature's fixed design" built by an independent route, that surplus contaminates delta; if it is the
same-engine Dirac-mu design, it is removed. §4 says both in one sentence. Two classical arms are therefore
required, one per attribution — same-engine C* for the METHOD delta, literature fixed design for the referee's
"why not X?". Cost: one extra design.

## 3. THE SCREEN, THE BASE TERM, THE TUPLE — with rigor classes

3.1 Bound screen (F-EXP-2). Three de-novo lenses blind-converge on "compute the gap of the practice design before
optimising" (Var S0.11/L0.3, Hyp S12/L4, Opt S13/L2 — SP-CARM A14 DERIVED 3/4); the record owns the object
([T-GB]; M1 corollary M0 :2446-2452) and its gate (G2, D6 :776-778: "gap < ~1% Isp -> pivot") but schedules the
gate AFTER the engine at M2. Sequencing it BEFORE arm P is the cheapest cost lever in the whole item: if the
reachable gain is below the band by bound, the arm-P campaign (F3 cap 3-4 sessions, 2 decisive campaigns per
instance, D6 :214-227) is not run. This is a Q0 cost change of up to 3-4 sessions for a post-processing number.

3.2 Honest grade of the two bounds (my own refinement of SP-CARM §4, which used J_ideal only):
 - delta_ideal (J_ideal, geometry-free): THEOREM as a bound, but LOOSE on a truncated plug — J_ideal is attained by
   the UNTRUNCATED peak plug (M1, M0 :2447-2449), and the truncation itself costs whole points (ADR :126 KEY
   FINDING 4: at 30% truncation the eps cap gives 259.6 s vs 278.4 s on the 10 kN example, ~7%). So the ideal
   screen will typically NOT fire on the TWIN sector; used alone, clause (ii) of A-CARM would be dead weight.
   I concede this to the refuter before he raises it.
 - delta_class (B_class = Int max_in-class F dmu): the inequality J_avg[Sigma] <= B_class for every Sigma in the
   class is THEOREM (it is the T4 proof's own step, M0 :2304-2308, and needs no closure hypothesis); the NUMBER is
   a bound only if each per-phase in-class maximum is ATTAINED and certified (KKT closure). The record's pattern is
   certifiability-limited exits with the margin inactive (S20/S22/S24; D6 :143-146) — so the measured B_class may
   be a WITNESS value, not a bound, and delta_class is then CONJECTURE-graded. Rule: the screen fires (R3) only on
   delta_class computed from per-phase designs that closed to KKT; otherwise both numbers are printed and the
   screen is declared NOT-DECIDABLE, arm P runs. This keeps clause (ii) alive where it can bite and prevents the
   bound from being passed off as coverage (the M0 :1349 warning, "a value-level bound is never passed off as
   optimum coverage", applies verbatim).

3.3 Base-area term (F-EXP-3 / A9 of SP-CARM, A15 of SP9). §5.3 pins the truncation FRACTION, §5.4 the closure
OBJECT; neither pins the base AREA, which is a contour output at the truncation station. All four trees derive
dDelta/dp_b = (A_b,P - A_b,C)/F (SP9 A15, 4/4 DERIVED). Magnitude anchors, page-verified: [IO] Humphreys 1971
p. 1587: swapping the base-pressure model from Eq. (12) (p_b = 0.846 p/M^1.3, from Ref. 9) to Eq. (38) moved the
optimum base height y_D from 0.954 in. to 2.34 in. (x2.45) and the wall slope at D from -13.26 deg to -3.08 deg,
thrust 32,881 -> 32,965 lbf (+0.26%); p. 1582: the optimisation "is independent of the model used to calculate
the base pressure" — the closure is an iterated constant, i.e. the design MOVES with it while the value barely
does. [IO] Harroun-Heister-Ruf 2021 p. 669: "Neither the analytical model in Eq. (8) nor the previous theory for
the closed-wake regime for constant-pressure engine aerospike nozzles are appropriate for predicting base
pressures with an RDE cycle" (Fig. 17: open/closed-wake transition at NPR ~ 6.7, Humble-Lim nozzleless tests).
With C61 NEVER (:818-831) the closure band is threshold-sized on the ABSOLUTE value (RT-1 arithmetic); on the
DIFFERENCE it survives at first order through A_b. Printing A_b costs nothing; R4 makes it a pin or a band row.
This is the part of A-CARM that the PB item owns at the closure level; here it is only the comparator-side
consequence (two arms of the same fraction can differ in A_b).

3.4 The decisive-result TUPLE (SP9 / RT-6, RT-9). At case A the bell is classical BY THEOREM (T3; Annex B row A
"the tool states it, does not rediscover it"), so a bell-first decisive run is delta = 0 by construction — the
trees' bell-first ordering (V/H/O) is a class-B ordering, not a case-A one; I do NOT ask for it. What I ask for is
the VALUE STACK in the TWIN Verdict: delta* (vs C*); each arm vs the bell designed at <Pc> at the SAME c (one
[X-TOCV]-class bell design, post-processing); the bound gap per arm (delta_ideal and delta_class); per-arm
operability rows (g_sep per phase; side-load proxy). Rule: MATERIAL on Isp with a worse operability margin than
C* = CONDITIONAL. Without the stack, SMALL is an argument from silence (RT-9) and MATERIAL is a number relative to
nothing a designer builds. The two-sector EMBEDDING (A-10: the TWIN as the plug row of the F3.TOURNAMENT fallback
table, D6 :1187-1201) is a USER-priced option (+1-2 sessions, 7-11 vs the 7-10 ceiling) — I recommend it, I do not
make it a precondition. The bell-at-<Pc> row of the value stack already delivers most of its information at
case A for one design.

3.5 The evaluator caveat I accept up front (SP1/SP5 territory, not mine). The sweep's reading (spread_C) is only
as good as the evaluator both arms are scored on. [IO] Harroun 2021 p. 671: the quasi-cycle-averaged 2-D CFD
"estimated the coefficient of thrust for both the IE and flared aerospike to be 1.25; thus, the performance ...
was estimated to be roughly the same for either design", while the paired Humble-Lim tests (Table 3, Fig. 22)
separate the two designs by surface pressure — averaged 2-D evaluation was BLIND at contour-ranking level. And
[X-STSC] puts plug St_n in [0.27, 1.41] with the record's own rule "frozen-time rung alone NOT defensible" on the
plug class (st log). If A-REPR lands on the 4-field axial fallback (D6 :1184-1186), spread_C <= band (R2) is a
rung-2 reading and must be quoted as such ("comparator identity immaterial at rung 2, St_n = x"). I do not claim
more than the evaluator licenses; I claim that WHATEVER evaluator is pinned, arm C must be the argmax on it.

## 4. COST, priced against the F3.TWIN window

- Sweep: O(10) Dirac-mu classical constructions + O(10) cycle evaluations + O(10) A-1 certifications, values only,
  no adjoint. The arm-C builder is required by §4 anyway; the sweep is 10-20x arm C's own forward cost. Bell-class
  solve of record 0.116 s (C57 note); the PLUG forward solve is UNPRICED until F3.PLUG lands H20 (findings row,
  path critical) — so I do NOT promise "inside the 3 h decisive window": I place F-EXP-1 at the F3.PLUG EXIT / arm-C
  build step (before F3.TWIN opens), where a sweep of 10-20 forward plug constructions is the natural exit test of
  the plug builder itself. If a certified plug construction costs ~10 min, the sweep is ~2-3 h of NON-decisive
  wall-clock, outside the decisive-run cap. If it costs O(1 min), it fits in the opening hour of the TWIN window.
- Screen: J_ideal post-processing (zero); B_class = the per-phase optima at the quadrature nodes = the same family
  as the sweep (zero extra if the sweep grid is the quadrature grid; otherwise K extra Dirac-mu designs).
- Base term: print A_b (zero). Value stack: one bell design ([X-TOCV] class, minutes) + post-processing.
- Attribution arm: one extra design if GENO RaoPlug S1/S2 are fixed, else declared "unanchored" (A-4 of the red
  team) at zero cost.
- Downside on the cost axis: NONE on the arm-P campaign (untouched); UPSIDE: R3 can cancel it (3-4 sessions).
Net on the pre-registered criterion: CRED q2 0 -> 1 (strongest opponent named and measured), q3 partially (Delta_Ab
row), q5 unchanged; COST_hi unchanged or lower. This is CONFIRM-with-repairs territory for the road, not a new
road: the amendment does not dominate the incumbent under LOG-2 (same road, same tuple), it repairs the field the
red team and two Stage-A judges independently found single-author and NO-ROW (SP-CARM §0 measured grep: 0 hits on
"comparator|arm C|peak" in choice_ledger.yaml; SP9 §0).

## 5. GENERALITY

The decision rules are written on SPREADS and GAPS, not on instance values (TWIN §3 two-stage pin honoured: "no
decision rule depends on the instance values"). They transfer unchanged to: the second instance of A-5 (truncation
0.40 / PR-halved family), the case-B flip (§3 clause — the sweep family then includes profile-shape states), the
F3.TOURNAMENT plug row, and any sector where a collapse theorem does NOT select the design state (shrouded/duty
split, PB-3). On the bell at case A the sweep is provably degenerate (T3 Lemma C: every member collapses to the
same contour up to the affine scaling) — the sweep would return spread_C = 0 and R2 fires by theorem: the rule is
consistent with the record where the record has a theorem, and measures where it does not.

## 6. WHICH OF THE DECISION RULES WOULD MAKE ME ABANDON THE AMENDMENT

 (a) R2 on the record instance — spread_C <= band over a certified sub-range that INCLUDES the peak member: the
     comparator identity is immaterial; I withdraw clause (i) (arm C := argmax) to a reporting row and keep only
     the sweep datum on T4 sharpness. If additionally the peak member is cert-limited, I withdraw (i) only with
     the caveat "spread read on the certified sub-range".
 (b) Clause (ii) (screen): if on the pinned instance delta_class cannot be computed at THEOREM grade (per-phase
     problems do not close to KKT — the S20/S22/S24 pattern) AND delta_ideal > 0.5% (the loose bound does not
     fire), the screen is NOT-DECIDABLE and I withdraw it from the gate position to a Verdict row; arm P runs.
 (c) Clause (iii) (base term): if the engine's parametrisation pins the truncation-station radius by (eps,
     truncation fraction) so that A_b,P = A_b,C identically, Delta_Ab = 0 by construction and the rule is
     withdrawn (printing A_b once proves it).
 (d) Clause (iv) (tuple): the value-stack rows I do not withdraw (post-processing, zero-cost, RT-9 makes SMALL
     unpublishable without them); the two-sector EMBEDDING I abandon the moment the user declines the +1-2
     sessions — it was never a precondition.

## 7. PRE-EMPTED ATTACKS (the refuter's two hats)

- "Change of the pre-registered comparator after the fact": the amendment is dated, appended to §9 BEFORE any arm
  runs, on a §4 field the judges classify SINGLE-AUTHOR / NO-ROW; correcting a single-author field before the
  experiment IS the pre-registration mechanism (R-TWIN-0 forbids undeclared drift, not declared amendment).
- "Constraint identity breaks": every sweep member satisfies §5 identically; the design state is not a §5 item.
  A-1 applies to every member; cert-limited members are printed, not quoted.
- "Scope creep / cost the F3 budget does not carry": values only, no adjoint, placed at the plug-builder exit;
  the only campaign the amendment can change is one it CANCELS (R3).
- "At the mean state the bell is classical by theorem": granted for the bell, and irrelevant on the plug (T4
  sharpness :2313-2316); the sweep degenerates on the bell by that same theorem (§5 above).
- "The sweep changes the DATA claim, not the METHOD claim": inverted — without C* the METHOD claim is not
  separable from the DATA claim at all (§2.5); with it the two are read on two rows (delta*, delta vs C_mean).
- "A sweep member that is not a certifiable design": excluded by A-1 per member; the kill of the falsifier is
  declared (§1) and produces a datum (the certified sub-range), not a silent narrowing.

## 8. LITERATURE DEPTH DECLARATION (binding rule of the session)

[IO] page-verified this window: Harroun-Heister-Ruf 2021 JPP 37(5) — p. 669 (closure verdict, Fig. 17 open/closed
wake), p. 671 (C_F = 1.25 for both aerospikes from the quasi-cycle-averaged 2-D CFD; paired tests Table 3,
Fig. 22); Paxson-Miki-Perkins-Yungster 2022 AIAA 2022-4107 — pp. 1, 2, 3, 5 (two parameters perturbed at one
operating point; 58.1 -> 70.0%; "pressure ratio and throat Mach number ill-defined"; cycle-averaged thrust as the
limit-cycle criterion); Humphreys-Thompson-Hoffman 1971 AIAA J 9(8) — p. 1582 (base pressure as iterated constant,
Eq. 12), p. 1584 (Table 1 parametric study, 32,699-32,881 lbf), p. 1587 (Eq. 38 swap: y_D 0.954 -> 2.34 in.,
slope -13.26 -> -3.08 deg, thrust 32,965 lbf).
[IO] on the in-repo carrier: src/thrust/stechmann_nozzle.py bell_opt/spike_opt (:411-434) + Step 5 docstring;
S24 log step 14 (+0.51% F7); st_scoping_number_run.log ([X-STSC]).
[REP]: Stechmann 2019 Figs. 9/10/12 read through M0 :2565-2572 and the registry summary :318-326 — the registry
path PARENT/stechmann-...pdf is NOT present on disk in this window: PATH-REPAIR / PROCUREMENT ASK (the paper is
READ-INTEGRAL of record; only its on-disk path needs restoring; nothing in this file depends on a page of it
beyond what the validated script carries). "7 designs on two OFAT lines" (Paxson-Miki) [REP] via registry :257.
NOT used load-bearing (UNVERIFIED, no PDF or WANTED): Hagemann-Immich-Nguyen-Dumnov 1998 (WANTED :1374);
Kaemming-Paxson 2018 EAP (READ-INTEGRAL of record, but not needed here); RDE thrust-stand accuracy 1-3% / 2-4% Isp
(Goto 2019 / Fotia 2016 / Rankin — WANTED rows; if true it matters for the §6 band anchor, which is SP9's, not
this seat's — PROCUREMENT ASK stands as filed by the SP-CARM judge §2.8).

POSITION IN ONE LINE: on the truncated plug no theorem selects the classical design state, the field's practice
is a cycle-evaluated sweep, and a MATERIAL delta against a mean-state plug does not separate method from data —
so arm C must be the certified design-state-sweep argmax (with the literature's fixed design as the attribution
arm), the class-bound screen must be read before arm P, and the Verdict must carry the value stack; every clause
carries the measurement that would retire it (§6), and none of it costs a decisive session.
