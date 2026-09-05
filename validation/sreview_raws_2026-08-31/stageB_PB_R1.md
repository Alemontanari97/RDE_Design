# STAGE B — ITEM PB — REFUTER ROUND R1 (two hats: base-free/cancellation lens; ledger C61 owner)

Refuter, round 1 of 2. Date 2026-09-05. Read in order: `stageB_items.json` id PB; `stageB_PB_A0.md` integrally;
`stageA_diff_SP-PB.md` integrally (§0-§11); `RED_TEAM_decisive_number.md` RT-1/A-2/A-5 rows (:30-79, :146-156);
`BASE_PRESSURE_HARVEST_c4.md` §1, §13, §14, §15, CONSOLIDATED (a)-(d); ledger C61 (:818-831); decision map Stage 8
(H20/C61/DUTY-10 rows, edges E10-E14); ADR :126-146; TWIN §2-§9 (A-1 amendment); problem book PB-2 :532-536;
M0 :1340-1347 channels (v)/(vi), :2316-2319 T-T4 sharpness; D6 :214-227; the four trees' SP-PB sections
(P :620-640, H :511-523, V :537-560, O :523-540); BRANCH_LEDGER row PB-11 (:89). Memory files not read.
PDFs re-opened on disk THIS window for every load-bearing claim (tier [IO]): Harroun-Heister-Ruf 2021
`literature_review/harroun_2021_computational_experimental_rdre_nozzle_performance.pdf` journal pp. 666-669
(PDF 7-10); Humphreys-Thompson-Hoffman 1971 `GENO/literature/design-of-maximum-thrust-plug-nozzles-for-fixed-
inlet-geometry.pdf` pp. 1582, 1586-1587 (PDF 2, 6-7); WG10 `GENO/literature/ADA455494.pdf` doc pp. 14-16
(PDF 15-17); NASA SP-8120 `GENO/literature/NASA_SP8120_liquid_rocket_nozzles.pdf` doc p. 20 (PDF 34).
Verification result: every page citation in A0 §2-§3 is CORRECT at the page (0.59/0.95 atm p. 666; Schwer
counter-datum + "approximately 1% different" p. 667; verdict sentence + Fig. 17 regimes p. 669; y_D 0.954 -> 2.34
in, slope -13.26 -> -3.08 deg, 32,881 -> 32,965 lbf pp. 1586-1587; "constant which is not known a priori ...
independent of the model" p. 1582; 5%-of-thrust p. 14, Eqs. (5.1)-(5.2) "failed" p. 15, Univ. Rome [+19%, -15%]
p. 16; SP-8120 p_b = 0 p. 20). No citation defect. My attack is on the STRUCTURE of the protocol, not its anchors.

--------------------------------------------------------------------------------------------------------------
## 1. FALSIFIER — AGREED WITH THREE AMENDMENTS (binding text for the judge)

I agree F-PB.1 / F-PB.3 / F-PB.4 as measurements and F-PB.2 as the advocate's own kill, with these amendments:

AM-1 (replaces the F-PB.2 threshold). Strike "r_pb <= band_R/3". The /3 is the O tree's "minor term" convention
(O :538 "b_TS/3"), not a derived tolerance (R5). The criterion is the invariance rule ITSELF: the branch of §6 read
at every member is the same branch. r_pb is printed, not thresholded.

AM-2 (kill-eligible members). The F-PB.4 kill of plug eligibility at case A fires only on a flip INSIDE the
physical bracket k in [0.62, 1.19] (the cold best-of-class endpoints + the only RDE datum, both directions).
The floor member k = 0 stays in the sweep as a PRINTED STRESS ROW and may trigger the re-design half, but a flip
caused by k = 0 ALONE does not kill the sector (reason: §3 objection O5 — the floor is physically excluded by the
record's only RDE base datum). The advocate must accept, or show that k = 0 is a physical state of a
truncated-plug base under any regime on disk.

AM-3 (regime precondition). F-PB is defined only once the pinned instance's wake regime is READ (NPR vs the
Harroun 6.7 datum / the Nasuti-Onofri classifier, A-9 (b)); the set S_pb of A0 §2 is the CLOSED-WAKE set. For an
open-wake instance the set is re-derived at F3.TWIN opening with an ambient-tracking upper family (§3 objection
O4); until then "derived from the harvest's own numbers" is a closed-wake statement.

Kill-of-the-falsifier clause (A0 §1 last bullet) accepted, with §3 objection O8 on what the cap actually prints.

--------------------------------------------------------------------------------------------------------------
## 2. WHERE THE INCUMBENT IS WEAKER (I serve the truth, not TWIN §6 as written)

The incumbent is dead on F-PB.1 almost by construction and I do not defend it: with the truncation FRACTION pinned
and the base radius a design OUTPUT (advocate §3.2, correct reading of TWIN §5.3), the direct term
d(delta)/dp_b = (A_b,P - A_b,C)/F is generically non-zero, so SOME member of any honest set moves the printed
branch unless eps_A is small — and nothing in §6 prints eps_A. A §6 that can quote MATERIAL with this term unpriced
fails RT-1 at the first referee question; four trees + the red team + the diff judge converge on a ROW. Hat 1 also
concedes the row (H :520 "(4) always shipped"). So the live question is not "row vs no row"; it is the WEIGHT of
the alternative (re-design half, H-PB-MONO, cap, plug-kill trigger, set width) and whether the set brackets. My
objections below are all on that weight and on that set.

--------------------------------------------------------------------------------------------------------------
## 3. OBJECTIONS (numbered; NEW = not raised by the diff judge, the red team or A0)

O1 [NEW] — The Humphreys exhibit is misfiled: it IS the direct term, and under its own architecture the
"indirect term" at fixed base radius is identically zero. Humphreys 1971 optimizes at FIXED LENGTH (p. 1582
[IO]: isoperimetric constraint Eq. (5) with g = 1 = fixed length; p. 1586 [IO]: "a length from point T to point D
of 12.0 in.") with y_D FREE and p_b "a constant which is not known a priori ... recalculated in each iteration"
(p. 1582 [IO]). The x2.45 shift is a y_D shift at fixed axial truncation — exactly the TWIN's pinned instance
(truncation fraction fixed, base radius = output). It is therefore the (A_b,P - A_b,C) DIRECT channel of A0 §3.2,
not a separate "tip-slope/corner channel" (A0 §3.3 says "with c fixed the y_D channel is closed" — false: c fixes
x_D, not y_D; the flatter slope at D in Table 4 is the same contour ending higher). Conversely, under Humphreys'
architecture the base term Phi = (eta_D - delta'_D)^2 p_b/2 (Eq. (11) [IO]) is an ADDITIVE CONSTANT once y_D is
fixed and delta' = 0 (the record's inviscid pin), so the optimum contour is p_b-INDEPENDENT at fixed base radius
— the advocate's "unmeasured indirect term" is zero by construction there, to all orders, not "second order" (the
P tree :637) and not "unpriced". The indirect term exists ONLY under a contour-dependent closure (O2). The
advocate must choose an architecture before the re-design half means anything. (Nuance that helps him, noted
for honesty: Humphreys' re-design held the cowl lip radius and injection angle at their Eq.-(12) optima, p. 1587
[IO] "it is expected that the optimum cowl lip radius and injection angle will also be different" — the exhibit
is a LOWER bound on the direct-channel response, not an upper one.)

O2 [NEW] — The advocate's own closure object contradicts the licence he cites for it. He chooses P_ref = WG10
Eq. (5.7) (doc p. 16 [IO]) whose exponent Phi is a function of phi = the plug exit-wall angle (definition per
harvest §14 :446/:486 [REP-in-record]; I did not re-verify the symbol definition at Eq. (5.7)'s page). phi is an
ARM OUTPUT: the "same object, same parameters" then yields DIFFERENT p_b in the two arms and enters each arm's
corner condition through dPhi/dphi. That is the contour-dependent architecture — the one in which Humphreys'
"the optimization procedure is independent of the model used" (p. 1582 [IO]) does NOT hold, because Humphreys'
independence rests on p_b being a constant in R. So A0 §3.3's "the k-sweep is a re-run of the same engine, no new
theory" is false for the chosen object: the corner condition acquires a dp_b/dphi source term that the
iterated-constant engine does not carry. This is precisely PB-11 (A11 "closure derivative in the gradient /
iterated constant"), DEFERRED to the F3.PLUG exit (BRANCH_LEDGER :89; diff §7 item 5). The protocol's re-design
half is therefore CONDITIONAL on an unadjudicated architecture choice and cannot be pre-registered as text today;
the honest pre-registration is a fork: (i) iterated-constant p_b -> indirect term = 0, re-design half DELETED,
protocol = closed-form direct row (O3); (ii) contour-dependent closure -> re-design half live, PB-11 must land
first (new adjoint source term + rejector).

O3 [NEW] — Under (i) the "8 forward evaluations" are ritual: the whole p_b dependence of delta is LINEAR in k
with a closed-form slope. With p_b = k P_ref and P_ref contour-independent (or read once at the final designs),
delta(k) = delta_0 + k P_ref (A_b,P - A_b,C)/F exactly in the inviscid model; the invariance question over ANY
set is interval arithmetic on two geometry numbers and one P_ref evaluation, zero solver cost — the advocate's
own §3.2 row already IS the sweep. The only legitimate use of forward evaluations at two k is a SEEDED REJECTOR
that the engine's base term is indeed the additive linear one (the solver reproduces the closed-form slope to its
tolerance); that is 2 evaluations per arm, not 8, and it is a regression test, not a measurement. Under (ii) the
evaluation-only sweep is still linear (the designs are frozen); what is non-linear is the re-design, which is
where the cost sits. Hat 1's verdict: as written the protocol carries the cost of (ii) and the theory of (i).

O4 [NEW] — S_pb is a CLOSED-WAKE set; in an open-wake instance it is not a bracket. Eq. (5.7) is a function of
M_e (and phi) only — regime-blind, closed-wake-type (base pressure set by the lip expansion). Harroun p. 669
Fig. 17 [IO]: open-wake P_b/P_c ~ 0.185 at NPR ~ 4.5 vs closed ~ 0.08 — the open-wake base is more than 2x the
closed one and tracks ambient (17-20% below it, M0 :1347). The set's upper member 1.19 P_ref is a fixed fraction
of p_e (order 0.5 p_e for M_e ~ 3 by Eq. (5.7)'s bracket [SE from the IO formula]; instance numbers are not
pinned, I quote none); an ambient-tracking open-wake base (~0.8 Pa) can lie ABOVE 1.19 P_ref whenever p_e is at
or below Pa, i.e. in the very regime where the wake is open. The advocate's R8 argument against V's bracket
("would EXCLUDE the observed region") cuts against his own set in that regime. A0 defers regime to a "printed
scope line"; insufficient — regime decides the set's FAMILY, not its label (AM-3). The record's PR spread (45-49
CJ-based, st log) suggests closed wake at an ADR-class instance, but "suggests" is not a pin; the pin is a
measured command at F3.TWIN opening (TWIN §3). Until then §2's "derived" is conditional.

O5 [NEW] — The floor member k = 0 is a historical artefact, not a physical endpoint, and it loads F-PB.4. SP-8120
p. 20 [IO] says p_b = 0 is what the 1976 bell procedure had to ASSUME to obtain a solution and that the resulting
designs LOSE to truncated-ideal practice — a statement about a method's limitation, not about a base state. The
only RDE base datum on disk (Fig. 17 [IO]) has closed-wake P_b/P_c ~ 0.08 and open-wake higher; no regime on disk
produces a vacuum base. With f_b = 5-12% of thrust, k from 0 to 1.19 sweeps the ENTIRE base force through delta:
any eps_A above ~3% (the advocate's own §3.2 arithmetic at f_b = 5%) flips a branch near a boundary. So with the
floor in the kill test F-PB.4 fires almost by construction and hands the road to the class-B flip on a member
nobody believes — the "widens, does not predict" concession (C3) becomes a trigger. AM-2 repairs it; without
AM-2 the alternative is a loaded die and I move to kill on it in R2.

O6 [NEW] — Pinning the base radius (A0 §3.2 option (a); EXP alternative (iii)) is not a free cross-item
consistency; it re-scopes PB-2. T-T4 sharpness (M0 :2316-2319): the non-collapsing optimum "satisfies the averaged
system (T7) with the mu-averaged plug corner condition" — that corner condition is the y_D transversality
(Humphreys Eq. (11) at D). Pinning y_D deletes the one averaged condition that distinguishes arm P from arm C at
the truncation plane; what remains is the averaged wall condition under the length cap (still non-collapsing, so
PB-2 survives, but with one of its two signatures removed). The x2.45 exhibit says two CLOSURES want very
different y_D; two ARMS may equally want different y_D — that difference is SIGNAL, and option (a) throws it away
to make the base band vanish. The protocol must declare (a) as a design-class restriction of PB-2 with its own
falsifier (pinned-y_D optimum vs free-y_D optimum of arm P at the central member, difference vs band_R), or take
(b) and live with the linear direct row of O3. It cannot present (a) as costless.

O7 [NEW] — Cost anchored on an unratified amendment and on one of its two branches. A0 §5 prices the {0.20, 0.40}
window at "+0 sessions: rides A-5's second instance". A-5 is DA RATIFICARE (RED_TEAM :148, header "not of
record") and its second instance is EITHER truncation 0.40 OR a PR-halved family (:151-153), chosen at the
instance pin. If the user ratifies A-5 as PR-halved (the spread driver), F-PB.4's window is a THIRD campaign pair
= +1 session on the protocol's own account, inside a 3-4 session F3 budget already carrying F3.RK1, F3.PLUG (H20
unpriced) and the TWIN. Price it honestly: +0 OR +1 session depending on a decision not yet taken; the LOG-2
"COST unchanged in sessions" claim (A0 §5 last paragraph) is conditional.

O8 [NEW] — "No producer -> INTERMEDIATE by rule" is vacuous for THIS row. TWIN §8 lists "C61 p_b closure" as an
F3.PLUG PREREQUISITE: if no closure object exists no arm runs at all (R-TWIN-0/§8), so the outcome is "no TWIN",
not INTERMEDIATE. If the object exists, the k-sweep of one object is always producible (evaluation-only). The cap
is RT-1's general rule for rows with genuinely absent producers (O(St) J_1, M-RED representation term); imported
into PB it is dead text that inflates the protocol's apparent content. Keep it in A-2, drop it from PB.

O9 [NEW] — F-PB.4's "road" mislabels what escapes the band. The class-B flip changes the DATA class; the base band
is closure model-form (diff §5 Q3: no evaluator rung computes p_b, case B included). What escapes the band in P's
DL-2 (a) is the SECTOR (a bell made non-degenerate by swept supersonic interface data), not the data class per
se. F-PB.4's consequence should read "the plug is not quotable at case A; the road is a base-free sector, which at
this record requires case-B data (TWIN §3 clause, F2a tags flip)". Wording — but it is the wording the PROGRAM
acts on; the item's question ("is the class-B flip the road") is answerable only with the sector named.

O10 (hat 2, drift guard; the diff judge §11 raised the principle, the two instances below are NEW) — (a) A0 §2
uses the nozzleless closed-wake P_b/P_c ~ 0.08 "as a sanity anchor on P_ref's magnitude": calibrating a
truncated-plug cold correlation's level against an annular nozzleless hot datum is exactly the transfer R8
forbids without the analogy label, and here it is used as a CHECK, i.e. as if it could reject P_ref; strike it or
demote it to a printed context row with no consequence. (b) When the only branch-flipping member is the 0.62
analogy member, a referee's first question is "is that member physical for a truncated plug?" — and the panel is
dragged into R-8 exactly when it matters. The protocol needs a TIER RULE on flips (AM-2 is the minimal one): a
flip by a [MODEL-UNREL, cold] endpoint = kill path; a flip ONLY by the [ANALOGY] member = "INTERMEDIATE-by-
analogy" printed, with the Schwer counter-datum (p. 667 [IO]) beside it; a flip only by the [PRACTICE floor] =
stress row. Without the tier rule the set's labels are decorative: every member kills equally.

O11 (minor, hat 1) — Seeded rejector (vii) (GENO oracle at Veen with base included) is PB-3's rider (diff §8,
PRUNED, owner F3.RK1/B-RAOPLUG) and SP-CARM's business; re-importing it into PB double-books a rejector. Also, an
oracle run "with base thrust excluded" no longer cross-checks the corner condition, which is where p_b acts —
the rejector as written buys less than it claims. Keep it where the ledger put it.

--------------------------------------------------------------------------------------------------------------
## 4. WHAT I CONCEDE

K1. The row is a precondition of quotability (2 of 2 campaigns + 4/4 trees + red team; the incumbent falls on
F-PB.1). K2. The set must contain the RDE suction datum in some form and must refuse p_b = Pa as a "lower bound"
(R8; Fig. 17 [IO] shows the RDE open-wake points below the P_b = P_a line). K3. Every page anchor in A0 is
[IO]-correct. K4. The falsifier is runnable once H20 + a closure object exist, and its outcome can change the
program's road — it passes the scope rule. K5. If architecture (ii) is what F3.PLUG lands, the re-design half is
real and the Humphreys exhibit is the right warning (as a direct-channel exhibit, O1).

--------------------------------------------------------------------------------------------------------------
## 5. WHAT THE ADVOCATE MUST DO IN A1 (or the WEIGHT is refuted, not the row)

1. Declare the closure ARCHITECTURE of the F3.PLUG object (iterated constant vs contour-dependent) or pre-register
   the fork of O2 with PB-11 as the gate of the re-design half.
2. Replace the 8-evaluation sweep by the closed-form direct row + the 2-evaluation linearity rejector (O3),
   keeping re-design evaluations only for architecture (ii).
3. Accept AM-1/AM-2/AM-3 or refute O4/O5 on disk.
4. Re-price §5 with O7's conditional.
5. Declare option (a) (pinned base radius) as a PB-2 design-class restriction with a falsifier, or drop it (O6).
6. Drop the cap from PB (O8) and rejector (vii) (O11).
7. Fix F-PB.4's road wording (O9).
8. Strike or demote the 0.08 sanity anchor (O10a); adopt a flip tier rule (O10b).

--------------------------------------------------------------------------------------------------------------
## 6. [KNOWLEDGE] / UNVERIFIED LEDGER FOR THIS ROUND

- Definition of phi in WG10 Eq. (5.7) = plug exit-wall angle: taken from harvest §14 (:446, :486); the symbol is
  defined at the page for Eq. (3.2) (doc pp. 10-11, rendered by the harvest, not re-opened by me) —
  [REP-in-record], load-bearing for O2 only through "phi is an arm output", which holds for any wall-angle
  reading of phi.
- "Open-wake base ~0.8 Pa can exceed 1.19 P_ref" (O4): an order-of-magnitude statement [SE] from Eq. (5.7)'s
  bracket at M_e ~ 3 [IO formula]; no instance number quoted; checkable only at the F3.TWIN instance pin.
- Everything else at tier [IO] as listed in the header. No procurement ask beyond A0 §10 (I add none; Fick &
  Schmucker 1996 remains the primary behind "Veen FAILED", cited at WG10 p. 15 [IO] second-hand).

--------------------------------------------------------------------------------------------------------------
## 7. VERDICT OF THIS ROUND

Not a kill. The position survives on its agreed falsifier (unrunnable today, correctly conceded) and its anchors
are clean. Its WEIGHT is refuted as written: the re-design half rests on an architecture the record has not chosen
(O1/O2), the evaluation sweep is closed-form under one branch of that choice (O3), the set is closed-wake-only
(O4) and its floor member loads the plug-kill trigger (O5), the base-radius pin is a hidden re-scoping of PB-2
(O6), and the cost is conditional on an unratified amendment (O7). All repairable in A1. If A1 keeps k = 0 as a
kill-eligible member or keeps the 8-evaluation re-design protocol without naming the architecture, I move to kill
the alternative's weight in R2 and the record keeps only: ROW + closed-form direct term + linearity rejector +
regime-conditional set + PB-11 gate on the re-design half.
