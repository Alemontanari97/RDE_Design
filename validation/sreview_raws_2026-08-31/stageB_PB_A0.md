# STAGE B — ITEM PB — ADVOCATE ROUND A0 (alternative = the p_b BAND PROTOCOL)

Persona: the base-flow experimentalist who wrote the record's base-pressure harvest
(`validation/sfoundations_raws_2026-08-13/blocco3/BASE_PRESSURE_HARVEST_c4.md`) and the red team's RT-1 / A-2
(`validation/sreview_raws_2026-08-31/RED_TEAM_decisive_number.md`). Date 2026-09-05. Item definition read from
`stageB_items.json` id PB; every pointer opened (SP-PB diff integrally; RT-1/RT-2/RT-9 + A-2/A-3/A-5/A-9 rows; harvest
§1, §13, §14, §15, CONSOLIDATED; ledger C61 :818-831; decision map Stage 8 :176-185 + E10-E14; ADR :126-146; TWIN §2-§9;
problem book :522-575; M0 :1340-1347 channels (v)/(vi), :2314-2319 T-T4 sharpness; D6 :214-227 F3 block; the four trees'
SP-PB sections; PROGRESS_2026-08-31_Sreview.md LOG-2 dominance criterion + scope rule).
PDFs opened on disk for every load-bearing [KNOWLEDGE] claim below (tier [IO] = read at the page this window):
Harroun-Heister-Ruf 2021 `literature_review/harroun_2021_computational_experimental_rdre_nozzle_performance.pdf`
journal pp. 666-669 (PDF 7-10); Humphreys-Thompson-Hoffman 1971 `GENO/literature/design-of-maximum-thrust-plug-
nozzles-for-fixed-inlet-geometry.pdf` pp. 1582, 1586-1587 (PDF 2, 6-7); Onofri et al. WG10 `GENO/literature/
ADA455494.pdf` doc pp. 14-16 (PDF 15-17); NASA SP-8120 `GENO/literature/NASA_SP8120_liquid_rocket_nozzles.pdf` doc
p. 20 (PDF 34). Nothing UNREAD is leaned on; §10 lists what stays UNVERIFIED with a procurement ask.

--------------------------------------------------------------------------------------------------------------
## 0. WHAT I ARGUE AND WHAT I REFUSE TO ARGUE

I argue: the TWIN §6 band list AS WRITTEN (no p_b row, "same closure object in both arms" only) cannot quote ANY
branch of the decisive plug delta at case A, because the closure slot is NEVER-class (C61) and its error is
threshold-sized on the absolute value; the p_b BAND PROTOCOL (declared set + evaluation-only sweep + invariance rule
+ re-design-on-flip inside the F3 cap + "no producer -> INTERMEDIATE by rule") is a PRECONDITION of quotability,
costs hours where cancellation holds and one in-cap campaign where it does not, and is the only device that TESTS
the trees' cancellation claim instead of assuming it.
I refuse to argue "which closure is right for the RDE" (R-8: no truncated-plug RDE base measurement exists in the
corpus, harvest CONSOLIDATED (a); Harroun 2021 p. 669 [IO], verbatim: "Neither the analytical model in Eq. (8) nor
the previous theory for the closed-wake regime for constant-pressure engine aerospike nozzles are appropriate for
predicting base pressures with an RDE cycle"). The set below chooses no closure; it brackets. Any member of it
labelled "the RDE closure" is a protocol violation and a seeded rejector (§9).

--------------------------------------------------------------------------------------------------------------
## 1. THE FALSIFIER I PROPOSE FOR AGREEMENT (F-PB, sharpened from the SP-PB diff §6)

Measurement: at the pinned F3.TWIN instance (truncation fraction c, eps, L, mu hash, representation A-REPR, one
closure OBJECT), take the two FINAL designs (arm P, arm C) and evaluate BOTH under every member of the declared set
S_pb of §2 (values only, no re-design). Print the §6 branch (MATERIAL / SMALL / INTERMEDIATE / NON-CONCLUSIVE) at
every member, the zero-cost base-area row of §3.2, and the paired residual r_pb := max over members of
|delta(k) - delta(k_ref)|.

- F-PB.1 (kills the INCUMBENT): the branch differs between any two members of S_pb -> TWIN §6 as written is
  KILLED (it would have quoted a branch that the closure alone moves). The protocol's row, rule and cap become
  binding text of §6.
- F-PB.2 (kills the ALTERNATIVE'S WEIGHT — my own kill): the branch is invariant over S_pb AND r_pb <= band_R/3
  (band_R = the two-level Richardson band on delta, K_RICH-safeguarded) AND the base-area row is below band_R/3 —
  at BOTH truncations {0.20, 0.40} (A-5's second instance). Then the re-design half never fires, the cancellation
  claim is MEASURED TRUE at this class, and I concede the protocol reduces to one reporting row + one evaluation
  sweep (still mandatory: the row is what makes the invariance checkable, RT-1). "Precondition of quotability"
  survives only in that reduced form. I abandon the re-design rule and the INTERMEDIATE cap for this instance.
- F-PB.3 (the trees' cancellation claim): after re-design at the adversarial endpoint (§5), |delta(p_b,hi) -
  delta(p_b,lo)| > band_R -> the "cancels to first/second order on the difference" claim (P/V/O trees) is KILLED as
  a THEOREM-shaped statement and demoted to an instance-measured residual row.
- F-PB.4 (plug eligibility at case A): no truncation in {0.20, 0.40} yields a branch invariant over S_pb after the
  in-cap re-design -> the truncated plug is NOT the decisive sector at case A; the class-B flip (TWIN §3 clause) is
  the road. This is the outcome that changes the PROGRAM'S ROAD on the data-class axis — the measurement the task
  asks me to name.
- Kill of the falsifier itself: the plug forward solve (H20, F3.PLUG prerequisite, TWIN §8) is not landed at
  F3.TWIN opening -> F-PB cannot run; the ONLY honest output is "no producer -> INTERMEDIATE by rule" — which is
  the alternative's cap, not the incumbent's silence. If the refuter rejects that cap he must say what §6 prints
  for the p_b term when nothing can produce it.

Which outcome makes ME change: F-PB.2 at both truncations. Which outcome makes the PROGRAM change: F-PB.4.

--------------------------------------------------------------------------------------------------------------
## 2. THE SET S_pb, DERIVED FROM THE HARVEST'S OWN NUMBERS (every member page-verified)

One closure OBJECT for both arms (TWIN §5.4 kept verbatim): p_b = k * P_ref(M_e, gamma, phi), with P_ref the WG10
best pure-empirical model (Univ. Rome Eq. (5.7), ADA455494 doc p. 16 [IO]) and k a SCALAR parameter of the object.
"Same object, same parameters" holds member-by-member; the set is the parameter list:

| k | provenance (page-verified) | validity label printed in the Verdict |
|---|---|---|
| 0.85 / 1.19 | WG10 doc p. 16 [IO]: the Univ. Rome model "gives the smallest percentage of error [+19%,-15%] relatively to measured data" (cold, clustered/annular rigs, Fig. 5.4) | [MODEL-UNREL, best-of-class, COLD] — the classical model-form floor, before any RDE effect |
| 0.62 | Harroun 2021 p. 666 [IO]: surface-area-averaged base pressure 0.59 atm (detonation-wave inflow) vs 0.95 atm (constant-pressure), "an approximately eightfold increase in base drag"; p. 667 [IO]: "confirmed by experiment. Five nozzleless tests of the Humble and Lim RDE campaign ... approximately 1% different ... had significantly reduced base pressures" (Fig. 13) | [ANALOGY, LABELLED] — nozzleless annular base -> truncated plug; sign is CONFIGURATION-DEPENDENT: p. 667 [IO] Schwer et al. found base pressures "did not vary substantially between steady-flow and RDE conditions" on an airbreathing truncated aerospike, Harroun: "an area demanding more focused study". The member WIDENS the set; it predicts nothing |
| 0 | NASA SP-8120 doc p. 20 [IO], verbatim: "The bell-nozzle optimization procedure can be applied to plug nozzles, but to obtain a solution it is necessary to assume that the base pressure is zero ... truncated ideal nozzles ... produce higher overall nozzle (base included) efficiency than the optimum nozzles with zero base pressure" | [PRACTICE floor] — the only closure under which a variational plug optimum was ever posed in the handbook; the SMALL-branch stress member |
| REFUSED: p_b = Pa "lower bound" | Harroun 2021 p. 669 [IO]: "the Humble and Lim RDE in the open-wake regime had base pressures significantly lower than ambient pressures" (Fig. 17, dotted P_b = P_a line above the RDE points) | inadmissible in BOTH regimes (M0 :1347 R8) — a set built on V's bracket [min(Pa, p_lip), p_lip] would EXCLUDE the observed region |
| NOT a member: Veen 0.846 p/M^1.3 | WG10 doc p. 15 [IO]: Eqs. (5.1)/(5.2) "failed to produce reliable results" (Fick et al. evaluation); Eq. (5.1) = Humphreys 1971 Eq. (12) p. 1582 [IO], "a curve fit of the data presented in Ref. 9" (Rom 1966, near-wake) | the GENO RaoPlug oracle's closure of record (C61 incumbent field) -> §5.4 rider: the oracle cross-check runs at the swept k or with base thrust excluded, else §5.4 is violated at the oracle level |

Regime scope (printed, not a member): Harroun 2021 p. 669 Fig. 17 [IO]: open wake at NPR 4.5-6.7, transition at
NPR ~ 6.7, closed-wake P_b/P_c ~ 0.08 flat to NPR ~ 17 (in-source caveat: "Additional tests with NPRs between 4.5
and 6.7 are required"). The pinned instance's NPR (F3.TWIN opening amendment) is read against 6.7 and the regime
printed as A-9 (b) scope; the closed-wake absolute ~0.08 P_c is a sanity anchor on P_ref's magnitude, not a member.

--------------------------------------------------------------------------------------------------------------
## 3. THE ARITHMETIC — WHY THE ROW IS A PRECONDITION, NOT DECORATION

3.1 Absolute value. Base force fraction f_b = p_b A_b / F: 5% for a 20%-truncated plug at high PR (WG10 doc p. 14
[IO]: Navier-Stokes computations, "base drag should represent only 5% of the total thrust (inner nozzle, plug and
base) at high nozzle pressure ratio", cold); up to ~12% of gross thrust on an RDE (Schwer-Kailasanath via
Kaemming-Paxson, harvest §4 [REP], CFD context-only per CT-6). Multiply by the set's spread: WG10 endpoints (34% span
of p_b) -> 1.7-4.1% of thrust between endpoints, 0.75-2.3% each side; suction member (-38%) -> 1.9-4.6%; floor
-> 5-12%. Every member moves the ABSOLUTE plug Isp by more than the 0.5-1% thrust-stand band (TWIN §6). All four
trees derived the same conclusion blind (V "derived materiality tolerance", H "~3% >> 1%", O "the base band alone
can be ~ b_TS", P "+-0.3-1.5% of F = the band_TS itself"). No party disputes this; it is why the difference is the
only quotable object.

3.2 The DIRECT term on the difference — cancels only if the base areas match (zero-cost row). With both arms under
the same k, d(delta)/dp_b = (A_b,P - A_b,C)/F (optimization tree PB.4, derived). TWIN §5 item 3 pins the truncation
FRACTION, not the base radius: the plug radius at the truncation plane is a design OUTPUT of each arm, so
|Delta A_b|/A_b =: eps_A is not zero by construction. Direct-term band = eps_A x f_b x (span of k). To hold it below
band_R/3 ~ 0.17%: WG10 endpoints -> eps_A < 10% (f_b = 5%) / < 4% (f_b = 12%); floor member -> eps_A < 3.4% / 1.4%.
This row is computed from the two final geometries BEFORE any sweep, at zero solver cost. It either (a) pins the base
radius as a §5 constraint (the EXP item's alternative (iii) reaches the same pin from the comparator side — cross-item
consistency) or (b) prices itself as a named band row. The incumbent has neither.

3.3 The INDIRECT term — the design's response to the closure, unmeasured. Humphreys-Thompson-Hoffman 1971
pp. 1586-1587 [IO]: swapping the base model Eq. (12) for Eq. (38) moved the optimum base height y_D 0.954 -> 2.34 in
(x2.45), the wall slope at D -13.26 -> -3.08 deg, and the thrust 32,881 -> 32,965 lbf (+0.26%); verbatim "the base
pressure model significantly influences the shape of the optimum contour". With c fixed the y_D channel is closed;
the tip-slope/corner channel (mu-averaged plug corner condition, M0 :2316-2319: a base-pressure model at the
truncation plane is exactly what breaks T4's nesting) stays open in BOTH arms, and nobody has measured its effect on
delta. That is the whole reason a re-design half exists — and it fires ONLY on a flip. Note the classical
architecture is already the one the protocol needs: p. 1582 [IO], the base pressure "must be treated in the
variational problem as a constant which is not known a priori ... recalculated in each iteration ... The optimization
procedure is independent of the model used" — an iterated constant, i.e. the k-sweep is a re-run of the same
engine, no new theory.

3.4 Consequence: "the closure error cancels on the difference" is TWO claims — the direct term cancels iff eps_A is
small (checkable at zero cost), the indirect term is an unpriced residual (checkable at one in-cap campaign). A
protocol that prints both is not weight; it is the only path from an absolute band of 0.75-12% to a paired band a
referee can read against 0.5-1%.

--------------------------------------------------------------------------------------------------------------
## 4. THE REFUTER'S TWO HATS, ANSWERED IN ADVANCE

Hat 1 (base-free preference; "cancellation holds -> ritual weight"; "test it, don't assume it"). Conceded: the
direct term cancels under matched A_b; conceded: if F-PB.2 fires, the re-design half is dead weight at this
instance. But the hat's own demand — test the cancellation — IS the evaluation sweep: 2 arms x 4 members = 8 forward
evaluations plus a geometry row. A device with a pre-registered kill for itself (F-PB.2) is not ritual. The base-free
alternative (bell at case A) is not available to this hat: [T-T3]/[T-T4] collapse the full-flowing bell and the
full-length plug to single-state designs at case A (M0 :2316-2319 sharpness; Annex B "Rao-at-<Pc> BY THEOREM"), so
the plug with a base is the ONLY non-degenerate case-A sector — the trees, ignorant of T3/T4, would have run a bell
that returns zero by theorem. Base-free at class B is a different item (DATA), and F-PB.4 is precisely the trigger
that hands the road to it.
Hat 2 (C61 owner; "no closure is right; do not drift into which"). Agreed, and enforced: the set carries validity
LABELS, not a winner; the C61 trigger "first truncated-plug (value, delta) row entering the record" fires at the
TWIN, and a NEVER-class slot licenses exactly one thing — set-valued treatment with the slot left open. The
protocol does not close C61; it makes the decisive number survive C61 being open. Drift guard = seeded rejector §9
(iii).

--------------------------------------------------------------------------------------------------------------
## 5. COST, PRICED AGAINST THE F3 BUDGET OF RECORD (D6 :214-227: 3-4 sessions, 3 h decisive runs/session, max 2
decisive optimization campaigns per instance)

| item | cost | anchor |
|---|---|---|
| Set S_pb as a k-parameter of one closure object + labels | < 1 h coding; closed-form P_ref | WG10 Eq. (5.7) doc p. 16 [IO] |
| Base-area row eps_A | zero solver cost (two geometries) | §3.2 |
| Evaluation sweep, 8 forward plug evaluations | bell solve of record 0.116 s (ledger C57 note); plug forward solve UNPRICED until H20 lands (TWIN §8). Rule: sweep <= 8 x t_plug; if t_plug <= 10 min the sweep is <= 80 min inside one 3 h window; if t_plug > 20 min the sweep is a session and the user decides — printed, never silent | C57 note; TWIN §8 |
| Regime + truncation scope line | closed-form (NPR vs 6.7) | Harroun Fig. 17 p. 669 [IO] |
| Re-design on a flip — arm C | 2 classical forward constructions (iterated-constant architecture, Humphreys p. 1582 [IO]); hours | RT-2/A-3 pricing ("hours, 10-20 forward constructions") |
| Re-design on a flip — arm P | ONE optimization campaign at the ADVERSARIAL endpoint (the member whose evaluation-only reading moved the branch against the central verdict) = the instance's SECOND decisive campaign, inside the cap. Invariance is then declared under a printed one-sided monotonicity hypothesis H-PB-MONO (the other endpoint was already favourable evaluation-only). BOTH endpoints = a third campaign = a cap breach = user decision by rule, never silent | D6 :224-226 cap |
| Second flip after the in-cap re-design | INTERMEDIATE by rule (the diff judge's "a THIRD flip means the instance is not quotable", made precise) | SP-PB diff §7 item 2 |
| Truncation window {0.20, 0.40} | +0 sessions from this protocol: it rides A-5's second instance (already priced +1 session inside the F3 cap by the red team) and adds the sweep to it | RED_TEAM A-5 row |

Total incremental cost of the protocol: hours at F3.TWIN opening; +0 campaigns if no flip; +1 in-cap campaign on a
flip; the cap breach is the only path to a session, and it is a user decision. Against the LOG-2 criterion this
leaves COST(road (b)/(h)) unchanged in sessions and raises CRED on q3 (uncertainty budget below the threshold)
0 -> 1 for the base term and on q5 (scope: regime + truncation printed). Without the protocol a MATERIAL plug branch
at case A is referee-dead at the first question (RT-1) — a CRED loss on the only non-degenerate case-A sector.

--------------------------------------------------------------------------------------------------------------
## 6. GENERALITY

(i) Closure-agnostic: any future N2 closure or a measured CTAP datum enters as the central member and SHRINKS the
set (the hyperbolic tree's falsifier — a class-C measurement narrowing the band below band/4 — is the same protocol
with a smaller set); nothing is re-derived. (ii) Sector-general: every sector with a closure slot (shrouded plug
PB-3, E-D, base-bleed variants) inherits the row unchanged. (iii) Rung-independent: no evaluator rung computes p_b
(SP-PB diff §5 Q3: the wave-frame evaluator and the per-phase march share the base model-form error), so the
protocol is invariant under A-REPR and under the ROAD item's outcome — the hybrid's exact evaluator adds nothing to
the base band and needs this row too. (iv) Cycle-mean by construction: the set is a cycle-mean object, which is the
only class licensed at the record head count (St_plug 0.27-1.41, st log PLUG CLASS line; CTAP is cycle-mean only,
Harroun p. 663 via harvest §1.1 [REP]) — I do not make the tau_b f indicator (A10) load-bearing here; it is a cheap
separate add. (v) The cap "no producer -> INTERMEDIATE by rule" is the general anti-silent-scope rule of RT-1 and
transfers to every band row (thermo, mu, St).

--------------------------------------------------------------------------------------------------------------
## 7. HOW IT CHANGES THE ANSWER TO Q0 (scope rule)

Q0 = "how does one optimize an RDE nozzle". The record's road answers it through a decisive number on the truncated
plug at case A. The protocol changes (a) the CREDIBILITY of that number: from "1% with a 0.5-1% band and an unpriced
threshold-sized term" to "branch invariant over a declared, labelled bracket, with the direct and indirect closure
terms separated and measured"; (b) the COST: hours, +1 in-cap campaign at worst; (c) the ROAD, via F-PB.4: if no
truncation in {0.20, 0.40} gives an invariant branch, the plug is not quotable at case A and the program flips the
decisive data class — a road decision taken by measurement, not by preference. An argument that only chose a closure
would be out of scope (R-8); this one changes whether the decisive experiment can be quoted at all.

--------------------------------------------------------------------------------------------------------------
## 8. CONCEDED UP FRONT (so the exchange spends its rounds on what is open)

C1. The direct term cancels under matched base areas — trivially, and the trees are right to say so.
C2. The protocol BRACKETS; it certifies nothing against the world (P34 light instantiation). The closer is external:
    a V1.4-class CTAP measurement on a truncated plug under rocket-condition RDE across NPR ~4-20 (harvest (c));
    procurement, not a Stage-B falsifier.
C3. The set's width is literature-class (cold data, +-15-19%) and the 0.62 member is an ANALOGY whose sign is
    configuration-dependent (Schwer counter-datum, Harroun p. 667 [IO]); the set widens, it does not predict.
C4. If F-PB.2 fires at both truncations, the re-design rule and the INTERMEDIATE cap are dead weight for THIS
    instance and I withdraw them for it; the row + sweep remain (they are what made F-PB.2 readable).
C5. The re-design at BOTH endpoints exceeds the F3 campaign cap; I do not ask for it silently (§5).

--------------------------------------------------------------------------------------------------------------
## 9. SEEDED REJECTORS (each must be able to FIRE before the first arm runs)

(i) a Verdict with an empty p_b row -> REFUSED; (ii) a member p_b = Pa labelled "lower bound" -> REFUSED (R8);
(iii) any member labelled "the RDE closure" or "closure of record" -> REFUSED (R-8 drift guard); (iv) a Verdict
quoting MATERIAL/SMALL with a flipped member and no re-design record -> REFUSED; (v) the base-area row missing when
eps_A exceeds the §3.2 threshold for the widest member -> REFUSED; (vi) a re-design at both endpoints without a
logged user cap decision -> REFUSED; (vii) arm C's GENO-oracle cross-check run at the Veen closure with base thrust
included -> REFUSED (§5.4 at the oracle level).

--------------------------------------------------------------------------------------------------------------
## 10. WHAT STAYS UNVERIFIED — PROCUREMENT ASKS (none load-bearing above)

| identity | why it would matter | status (registry, measured grep this window) |
|---|---|---|
| Hagemann, Immich, Nguyen & Dumnov 1998 JPP 14(5) | the correlation ALL FOUR trees cite; would give a second central value for P_ref | WANTED :1374, unread |
| Fick & Schmucker 1996 JSR 33(4) | primary of the WG10 verdict on Eqs. (5.1)/(5.2); I cite the verdict at WG10 doc p. 15 [IO], not the primary | no row |
| Ito, Fujii & Hayashi AIAA 99-3211 | primary of the 5%-of-thrust base drag; cited at WG10 doc p. 14 [IO] as "Navier-Stokes computations" | no row |
| Schwer & Kailasanath AIAA 2012-3943 | primary of the ~12% figure ([REP] via Kaemming-Paxson, harvest §4) | no row |
| Lim, Humble & Heister AIAA 2020-0195 | primary of the only hot-fire RDE base dataset (Fig. 17 of Harroun 2021) | no row |
| Chutkey et al. 2014 JSR 51(2); Schwer, Kelso & Brophy AIAA 2018-4968 | nearest truncated-plug p_b(NPR) data (cold) and the RDE counter-datum's own numbers | WANTED :1308 / :1332 |

--------------------------------------------------------------------------------------------------------------
## 11. ONE-PARAGRAPH POSITION FOR THE JUDGE

The incumbent pins "same closure object" and lists no p_b row; at case A the truncated plug is the only sector the
record's theorems leave non-degenerate, and its closure slot is NEVER-class with an absolute error of 0.75-12% of
thrust across the labelled bracket the harvest itself supplies (WG10 +19/-15% [IO]; Purdue 0.59/0.95 [IO], analogy;
SP-8120 p_b = 0 [IO]). "Cancels on the difference" is two claims: the direct term cancels iff the base areas match
(a zero-cost row the incumbent lacks); the indirect term is the Humphreys channel (x2.45 argmax at +0.26% value,
[IO]) and is unmeasured. The band protocol prints both, is cheap where cancellation holds (hours), buys one in-cap
campaign where it does not, carries its own kill (F-PB.2) and the program's road trigger (F-PB.4), and chooses no
closure. I ask the refuter to agree F-PB.1-F-PB.4 as the falsifier and to attack the cost table of §5 and the
threshold arithmetic of §3.2, not the closure question the record cannot converge on.
