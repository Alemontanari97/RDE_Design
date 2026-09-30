# STAGE B — ITEM EXP — REFUTER R1 (round 1 of at most 2; S-REVIEW 2026-09-05)

Seat: REFUTER, two hats — (1) the TWIN protocol author (F2-B0 order 7) defending pre-registration discipline and
constraint identity; (2) the variational/record advocate reading [T-T3] (M0 :746-800) and [T-T4] (M0 :2294-2316).
Consumer: judge J2 + the advocate (A0). Scope rule honoured: every objection below is scored on whether it changes
the credibility or the cost of answering Q0 by the TWIN road, including the road's own decisive experiment.

Read in full or at the cited anchors (no summaries): stageB_items.json (EXP); stageB_EXP_A0.md (integral);
stageA_diff_SP-CARM.md §0-§7 (integral); stageA_diff_SP9.md §0-§6 (integral); stageA_diff_SP4.md §6 (rider A7);
RED_TEAM_decisive_number.md RT-1..RT-10 + amendment table; TWIN_amendments_PROPOSED.md; TWIN protocol §1-§9
(integral); M0 :25-62, :740-800, :944-952, :1334-1352, :1506-1522, :2290-2330, :2436-2460, :2560-2575, :3173-3188;
problem book :522-575; D6 :137-172, :214-227, :770-790, :1178-1201; src/thrust/stechmann_nozzle.py docstring
Step 4-5 + bell_opt/spike_opt :411-434; PROGRESS_2026-08-12_S24_f1b.md steps 12-16; ADR_panel_2026-07-16.md :126-146;
choice_ledger C61 :818-831; st_scoping_number_run.log; findings row twin-protocol:preregistration-2026-08-31
(:2873-2882); literature_registry.yaml rows paxson_miki_2022 :249-257, harroun_2021 :273-282, stechmann_2019
:318-326, humphreys_thompson_hoffman_1971 :364-370. PDFs opened at the page this window (tier [IO]):
Humphreys-Thompson-Hoffman 1971 pp. 1581-1587 (GENO/literature/design-of-maximum-thrust-plug-nozzles-for-fixed-
inlet-geometry.pdf, read-only); Paxson-Miki-Perkins-Yungster 2022 pp. 1-5; Harroun-Heister-Ruf 2021 pp. 669-673;
Stechmann-Heister-Harroun 2019 pp. 892-896 (../stechmann-et-al-2018-...(1).pdf = registry path PARENT/, ON DISK).
No memory file read.

## 1. THE FALSIFIER — AGREED WITH FOUR BINDING AMENDMENTS (the text below is the agreed text for the judge)

I ACCEPT F-EXP-1/2/3 and readings R1-R4 as the falsifier of the item, with these amendments, each repairing a
defect argued in §2 (the amendment text is what the judge reads; A0 §1 text stands where not touched):

 (F-EXP-1a, constraint pin for the sweep members) "same truncation fraction, same eps, L" is replaced by: eps :=
   the value fixed by the pinned annulus/throat of the instance (§3 two-stage pin) — printed, not chosen per member;
   ABSOLUTE plug length L_p := one value for every member (the §5.2 cap); the truncation FRACTION of each member is
   a printed OUTPUT (L_p / l_ideal(xi_d)), never an input. Rationale: l(xi) increases in Pc(xi) ([T-T4] proof), so
   "same fraction" and "same L" cannot both hold across design states — §5.2 and §5.3 are simultaneously
   satisfiable only at one member. Each member also prints its nondimensional contour distance to C_mean
   (sup-norm of theta(x)) so that a Lemma-A degeneracy (§2.1) is DETECTED, not inferred.
 (F-EXP-1b, the spread rule R1 read net of the member band and of the closure) R1 fires iff
   spread_C − max_member(band_RICH) > band AND the ordering C* > C_mean survives the closure endpoint sweep of
   A-2 (the WG10 bracket [+19%, −15%] on the C61 object, evaluation-only, on C*, C_mean and C_peak). Otherwise
   R1 is declared NOT-DECIDABLE and §4 stands with C_mean + C_peak as the two theorem-named context arms (the PB-2
   pair, :532-536). Rationale: the argmax of K noisy members is biased upward by O(band·sqrt(2 ln K)) (~2×band
   at K = 10 if member errors were independent; correlated in practice, hence MEASURED by the paired two-resolution
   band, never assumed) — the record's own header M0 :1338 "best-of-sweep != argmax ... ranking-signal only" applies
   to C* exactly as to the field's sweeps.
 (F-EXP-2a, the screen R3 is THEOREM-gated) R3 (campaign pivot WITHOUT arm P) fires ONLY on delta_ideal ≤ 0.5%
   ([T-GB], THEOREM, M0 :2446-2452) or on delta_class ≤ 0.5% computed from per-phase optima carrying a GLOBALITY
   certificate (M1 duality-gap-zero mechanism or bound-ladder closure, M0 :2446-2449; VI.6 "bound-ladder gap +
   globality mechanism"). KKT closure of a per-phase design is NOT sufficient (C57 MIXED: the optimizer is
   local-only of record; a local per-phase witness UNDER-estimates B_class and the screen would then cancel the
   arm-P campaign on a number that is not a bound). delta_class from KKT-closed local witnesses is a Verdict ROW
   (SMALL co-report, A-9), never a gate.
 (F-EXP-4, cost pin, pre-registered grid-reduction rule) the sweep is priced by the MEASURED certified plug
   construction cost at F3.PLUG exit (H20 solve + C61 closure + A-1 certification under the pinned recorder);
   if K × cost > 1 h of the F3.PLUG-exit session, the grid reduces BY RULE to the three theorem-named states
   {<Pc>_mu (T3 state), thrust-consistent u* (Opt C.4, one root find), P_CJ (T4 state)} + the T0-extremes of the
   family (T_CJ / T0_end, st log) — never to a judgement call in-session.
Kill of the falsifier itself: as declared by A0 (peak member not certifiable under A-1) — AGREED, with the
addition that a Lemma-A degeneracy detected by F-EXP-1a (all members within the band of each other in contour
distance AND in J_avg) reads as R2 BY STRUCTURE (the record's theorem class, §2.1), not as a measured refutation
of anything; clause (i) then never enters §4.
What would change MY position (both hats): R1 firing under F-EXP-1b (spread net of band and closure-robust) —
then the mean-state arm C is refuted as the strongest member and I sign the §4 amendment; F-EXP-2a's globality
certificate landing on the record instance — then the screen is a legitimate gate and I withdraw §2.4.

## 2. ATTACKS ON THE POSITION (each new; none pre-empted by A0 §7)

2.1 THE "BY ELIMINATION" ARGUMENT OVERSTATES THE CLASSICAL FREEDOM AT FIXED eps (hat 2; A0 §2.2, SP-CARM §2.2).
For a plug, the expansion ratio IS the design state: the field's own plug design knob is eps (= design NPR), not a
pressure label — [IO] Stechmann 2019 p. 895: "the optimum area ratio with an aerospike will be significantly
larger in a detonation engine ... as the nozzle design works to capture the potential of the highest pressure and
highest mass flow portion of the cycle"; Table 1 p. 896 CH4/O2 20 atm aerospike: det eps 11.4 vs CP 3.9; the 0-D
model has no contour, its whole "design" is eps (spike_opt :425-434, NPR(eps*) = Pmax/Pa). TWIN §5.1 pins eps for
BOTH arms (and at case A the annulus/throat specs pin it physically). At fixed eps and fixed T0, [T-T3] Lemma A
(pressure-scaling similarity, holds for gamma(T) and across shocks, frozen composition — M0 :752-771) makes the
interior wall field Pc-INDEPENDENT: the classical contour designed at Dirac(Pc_d) differs across Pc_d ONLY through
(a) the Pa-weighted terms of Lemma C (projected area / base term, O(Pa/Pc) ~ 1/45 at the family's PR, st log),
(b) the overexpanded phases where the C-HT4 clamp is active (closure-owned, §2.3), and (c) gamma(T0(xi_d)) —
T0 3712 → 2201 K over the cycle (st log), the one genuinely non-degenerate axis, and it is a THERMO axis, not a
"cycle-vs-mean" axis. So the design-state family at fixed eps is NEAR-degenerate by the record's own lemma; the
expected outcome of F-EXP-1 is R2, and the advocate's headline clause (i) is, a priori, a pre-registered NULL.
The comparator-strength axis a JPP referee actually means (A0 §2.4's own Paxson-Miki quote: "parameters varied
are the overall nozzle area expansion ratio and the fraction of the expansion area that is provided by the
shroud", p. 1 [IO]) is eps and shroud/truncation geometry — A5 in SP-CARM's table, which the judge himself says
COLLAPSES under §5. Hence: the amendment answers the referee's "why not X?" with a sweep along the wrong axis, and
the axis that matters (the eps / L_p / truncation pin of §3, "by measured command", NO strength or favourability
rule, RT-10 / SP9 A17) is where BOTH the incumbent and the alternative are silent. INCUMBENT WEAKER HERE TOO: §3's
instance pin decides the comparator's strength and carries no rule — a defect neither party has repaired.

2.2 INTERNAL INCONSISTENCY OF THE SWEEP DEFINITION (hat 1). F-EXP-1 demands "same truncation fraction, same eps,
L" across design states; [T-T4]'s own proof has l(xi) increasing in Pc(xi), so a fixed FRACTION gives a different
L_p per member and violates §5.2, while a fixed L_p gives different fractions and violates §5.3. As written the
members are not at identical constraints and spread_C partly measures LENGTH, not design state. Repaired by
F-EXP-1a (absolute L_p; fraction printed). Not a kill; a defect the advocate must accept in the falsifier text.

2.3 spread_C INHERITS THE UNPRICED CLOSURE MODEL-FORM (both hats). The members differ, at fixed eps, mainly
through the overexpanded phases (C-HT4 clamp) and the base term — exactly the two closures the record prices at
NOTHING: H20 free-boundary solve "no home in the record" (findings row, path critical; TWIN §8 prerequisite), C61
NEVER with the WG10 bracket [+19%, −15%] (:822), Harroun 2021 p. 669 [IO]: "Neither the analytical model in
Eq. (8) nor the previous theory for the closed-wake regime ... are appropriate for predicting base pressures with
an RDE cycle". A0 §3.3 prices the closure on Delta_Ab (the P-vs-C* difference) but NOT on spread_C itself: R1 as
written can "refute §4 by measurement" on a closure artefact. Repaired by F-EXP-1b (closure endpoint sweep on
the ordering). Cost of the repair: evaluation-only, 3 members × 2 endpoints.

2.4 R3 ON delta_class IS NOT THEOREM-GRADE EVEN WITH KKT CLOSURE (hat 2; A0 §3.2). The inequality J_avg[Sigma] ≤
∫ max_Sigma F dmu is a THEOREM only with the GLOBAL per-phase maximum; a KKT-closed per-phase design is a local
witness (C57 MIXED, local-only of record; three certifiability-limited exits S20/S22/S24 at healthy margin, D6
:143-146), so the measured B_class can sit BELOW the true bound and delta_class ≤ 0.5% would then cancel 3-4
sessions of arm P on a non-bound. A0 conflates "closed to KKT" with "attained". This is the ONLY clause of the
amendment with a session-scale cost lever, and as written it is unsound; with F-EXP-2a it is sound but — by A0's
own concession on delta_ideal ("will typically NOT fire on the TWIN sector", ADR :126 KEY FINDING 4 ~7% truncation
cost) — likely dead weight on the record instance. The honest status of clause (ii): a Verdict row (A-9), not a
gate. G2 as written (D6 :776-778, bound-ladder gap, THEOREM-grade) already owns the gate; the amendment adds a
sequencing that only the LOOSE bound can legitimately execute.

2.5 LITERATURE DEPTH: THE "FIELD'S PRACTICE" EVIDENCE SUPPORTS A5, NOT A4 (hat 1, binding rule of the session).
[IO] Paxson-Miki 2022 p. 1: "Optimization is performed for a single operating point. Parameters varied are the
overall nozzle area expansion ratio and the fraction of the expansion area that is provided by the shroud";
p. 3: "The baseline design is then perturbed by altering two of its geometric parameters" — a GEOMETRY sweep on a
3-D unsteady RANS evaluator (p. 5) at one operating point: the tuned-practice comparator (A5, eps free), forbidden
to both arms by §5.1. [IO] Humphreys 1971 p. 1584 Table 1 (32,699-32,881 lbf, +0.56%, verified) and p. 1586 sweep
cowl-lip radius and injection angle — INLET-geometry scalars that the case-A annulus spec FIXES; again A5-class,
and the variational contour there is designed at ONE steady state (500 psia, p. 1586). NO source on disk or in the
registry fields a design-STATE sweep of classical constructions selected on a cycle evaluator: A4 is a program
construct (a legitimate one), and "the field's practice is a cycle-evaluated sweep [of design states]" (A0 §2.4
closing line, §2.3 "the literature's fixed design of a plug is a PEAK design") is a claim above the depth held —
Stechmann's "peak design" is eps sizing at the peak (p. 895 [IO]), which §5.1 removes from arm C's hands. The
referee-proof version of A0's argument is therefore: "under §5.1 the referee's comparator (A5) is excluded by
construction for BOTH arms; declare it in §1 as the scope boundary and keep the free-eps companion (SP-CARM
branch ledger, DEFERRED) as the named follow-up". That sentence costs nothing and is missing from both parties.

2.6 PATH CLAIM FALSE (hat 1, navigation-first): A0 §8 declares the Stechmann 2019 registry path "NOT present on
disk in this window: PATH-REPAIR / PROCUREMENT ASK". The registry header (:39) defines PARENT/ = "../"; the file
../stechmann-et-al-2018-rotating-detonation-engine-performance-model-for-rocket-applications (1).pdf EXISTS and
was read at pp. 892-896 this window (Figs 9/10/12 + Table 1 verified [IO]). The absence claim was not
search-proven; the procurement ask is withdrawn by measurement. Minor, but it is the class of defect the session
rule names.

2.7 THE QUESTION CHANGES, NOT ONLY THE COMPARATOR (hat 2; A0 §4 "same road, same tuple"). §1 asks whether the
method beats "the classical FIXED design"; §4 says arm C "is designed blind to the cycle, but evaluated on it —
that is the honest comparison the record's theorems address" (:62-64): the theorem-addressed comparator IS the
Dirac design at a theorem-named state (T3: mean; T4: peak). C* is a cycle-SELECTED classical design — both arms
then consume mu, and delta* measures "per-phase coupling in the contour (T7 averaged wall/corner conditions)
beyond design-state selection", which is a different and sharper question. I AGREE it is the better question
for the METHOD claim (A0 §2.5 substance stands: delta vs C_mean does not isolate the method), but the amendment
must then touch §1 and the "blind to the cycle" sentence of §4, and the paper wording per branch (A-9). Calling
C* the isolator of "METHOD vs DATA" is loose — both C* and P have seen the data; the honest labels are "value of
the cycle information" (delta vs C_mean) and "value of per-phase coupling" (delta*). Not a kill; a wording duty.

2.8 R4 IS A CLASS CHANGE FOR ARM P (hat 1). "Base radius becomes a §5 pin" constrains arm P's admissible class
(the base radius is a contour output of the per-phase optimum); §2 "argmax over the certified design class" then
changes meaning. Cheap, but it must be declared as a §2 class amendment, not slipped in as a §5 constraint row;
the propulsion tree's device (SP9 A15) says the same. Alternative (the band-term route, A15) leaves the class
untouched — I prefer it and ask the advocate to pre-register the band-term route as the DEFAULT, the pin as the
exception when Delta_Ab > band.

2.9 THE "SAME c" BELL ROW NEEDS A RULE (hat 1; A0 §3.4). A bell at the plug's eps under the plug's L cap may be
infeasible: ADR :126 KEY FINDING 3 — the Rao-80% bell at eps* = 4.04 already violates the 260 mm envelope on the
10 kN example; at the plug's larger eps (Stechmann Table 1: 11.4 vs 3.9-4.0) a "bell at <Pc> at the same c" is
either length-infeasible or at a different eps, i.e. NOT at the same c. The row is post-processing only if a rule
says which constraint yields (eps at the same L, or L at the same eps) — pre-register it or the row is not
comparable across sectors (this is F3.TOURNAMENT's own device, D6 :1187-1201, priced 1-2 sessions, not zero).

2.10 COST CLAIM ABOVE ITS DEPTH (hat 1; A0 §4 "none of it costs a decisive session" vs "the PLUG forward solve
is UNPRICED"). A0 is honest that the plug cost is unpriced, then prices the sweep at "2-3 h of NON-decisive
wall-clock" and "zero" for the screen and the attribution arm. Under A-1 every member needs certification under
the pinned recorder (and both recorders under A-8(ii)); F3's budget (3-4 sessions, D6 :214-227) already carries
F3.PLUG (H20 + C61 + mirror margin + vortex-sheet monitor), F3.TWIN and F3.TOURNAMENT; "non-decisive wall-clock" is
still session wall-clock. Repaired by F-EXP-4 (measured cost + grid-reduction rule). Not new in kind (A0 declares
the unpricing) — new in that the "zero/none" wording contradicts the declaration; counted as a sharpening, not
as a new objection.

## 3. WHERE THE INCUMBENT IS WEAKER THAN THE ALTERNATIVE (conceded from the refuter's chair)

- §4 "Rao-class plug / peak design at mean point" is not an executable specification (SP-CARM §2.3, RT-2 (b));
  the PB-2 pair "peak- AND mean-designed baselines" (:532-536) is the record's own earlier and better wording.
  The two theorem-named arms (C_mean, C_peak) should be in §4 REGARDLESS of the sweep's outcome — at zero
  marginal cost (they are members of the grid). CONCEDED to the alternative.
- Attribution: §4 mixes the same-engine Dirac design with the literature's fixed design; the F1b F7 datum (+0.51%
  in-class, S24 log step 14, band caveat) sits inside the INTERMEDIATE band — the two-arm attribution (A7) is the
  minimal repair and costs one design, or zero by "unanchored" declaration (A-4). CONCEDED. Humphreys 1971 p. 1586
  [IO] is the classical exhibit of the same hazard: Rao's method vs the parametric-study formulation differ by
  34,253 vs 32,881 lbf (~4%) on the SAME problem until the start line is matched (34,373 vs 34,375, p. 1586-1587)
  — an "independent classical route" is a cross-check only after start-line/interface identity is proven.
- Value stack + operability rows (A-6) and SMALL co-report (A-9): post-processing, zero cost, and without them
  SMALL is an argument from silence (RT-9). CONCEDED, with the §2.9 rule for the bell row.
- §3 instance pin has no strength/favourability rule (§2.1 above) — a defect of the incumbent that the
  alternative does not repair either; flagged for the judge as OPEN on both sides.

## 4. VERDICT OF THIS ROUND

Kill: NO. The position is not refuted on the agreed falsifier (it has not run, and its expected outcome R2 is a
datum A0 already committed to accept, §6(a)); no defect is unrepairable: §2.2/§2.3/§2.4/§2.8/§2.9 are repaired
by the four amendments of §1, §2.5-§2.7 are wording/depth duties, §2.1 re-frames the amendment's value (clause (i)
expected NULL by Lemma A; the comparator-strength axis is the §3 pin, open on both sides). What survives of
A-CARM at full strength: the attribution arm, the value stack, the two theorem-named context arms, Delta_Ab as a
band term, and the sweep AS A MEASUREMENT of [T-T4] sharpness on the record instance. What does not survive as
written: clause (i) as "the strongest opponent by elimination", clause (ii) as a campaign-cancelling gate on
delta_class, and the "field's practice" framing.

New objections this round (not in A0 §7 or earlier rounds; the judge counts): 9 — §2.1, §2.2, §2.3, §2.4, §2.5,
§2.6, §2.7, §2.8, §2.9 (§2.10 = sharpening of A0's own declaration, not counted).

## 5. LITERATURE DEPTH DECLARATION (binding rule)

[IO] this window: Humphreys-Thompson-Hoffman 1971 AIAA J 9(8) — p. 1582 (base pressure as iterated constant,
"independent of the model", Eq. 12), p. 1584 (Table 1: 21 runs, 32,699-32,881 lbf), p. 1586 (Rao 34,253 lbf vs
32,881; start-line match 34,373 vs 34,375), p. 1587 (Eq. 38: y_D 0.954 -> 2.34 in., slope -13.26 -> -3.08 deg,
32,965 lbf); Paxson-Miki-Perkins-Yungster 2022 AIAA 2022-4107 — p. 1 (abstract: single operating point; eps and
shroud fraction varied; 58.1% -> 70.0%), p. 2 ("pressure ratio, and throat Mach number ill-defined"), p. 3 (two
geometric parameters perturbed), p. 5 (limit cycle: cycle-averaged thrust constant; 3-D OpenNCC, frozen species);
Harroun-Heister-Ruf 2021 JPP 37(5) — p. 669 (closure verdict; Fig. 17 open/closed at NPR ~ 6.7), p. 671 (C_F 1.25
for both aerospikes from the quasi-cycle-averaged 2-D result; "obviously did not account for" the 3-D inflow;
paired tests Table 3 / Fig. 22, surface pressures only); Stechmann-Heister-Harroun 2019 JSR 56(3) — pp. 894-896
(Figs 9/10/12, Table 1: det aerospike eps 11.4 vs CP 3.9 CH4/O2 20 atm; p. 895 "optimum area ratio ... significantly
larger in a detonation engine"). [IO] on in-repo carriers: stechmann_nozzle.py :411-434; st log; S24 log step 14.
[REP]: none load-bearing. UNVERIFIED / not used load-bearing: RDE thrust-stand accuracy (Goto 2019 / Fotia 2016 /
Rankin — WANTED rows; the SP-CARM judge's procurement ask stands); Onofri 2002 WG10 bracket (READ-PARTIAL via the
C61 row — used only as the record's own C61 number, not re-read here).

POSITION IN ONE LINE: agree to run the sweep — as a MEASUREMENT with the constraint pin, the band-net spread rule,
the theorem-gated screen and the priced grid — but not to its headline: at fixed eps the classical design state is
near-degenerate by the record's own Lemma A, the referee's comparator (eps-tuned practice) is excluded by §5.1
for both arms and must be declared as such, and the campaign-cancelling screen is sound only on the loose bound;
the incumbent's real hole is the rule-less §3 pin, which neither party has repaired.
