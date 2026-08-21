# VERDICT — ESCALATION CLOSURE (E-1..E-5), S-FOUNDATIONS-C4,
# 2026-08-20. Role: ESCALATION CLOSURE JUDGE per the C4 escalation
# mandate (VERDICT_blocco2.md §§2-4: E-1..E-4 full-form escalations +
# E-5 = RES-CAP-1 targeted round-4-delta pass, carried by reference
# from VERDICT_r22f §4). This file is the ONLY file this slot writes.
# Label authority: per the mandate, the guidance labels of
# VERDICT_blocco2 §2 (explicitly NON-ADOPTED there) are adjudicated
# HERE; §5 of this verdict is the label list of record for the four
# minors. CT-6 respected throughout (no nozzle-paper number in any
# bound, band, or cell; re-checked at every file read).

## 0. READ-DEPTH DECLARATIONS (this judge window)

[FULL] the four escalated minors as revised: phaseD_minor_ntf.md
(537 lines, [ESC-r1-*]/[ESC-r2-*] + §§9-10 dispositions);
phaseD_minor_objdom.md (609 lines, through [ESC-r3-*] + §§6-8);
phaseD_minor_deltacarrier.md (913 lines, through [ESC-r3-*] +
§§11-13); phaseD_minor_crosslowering.md (667 lines, through
[ESC-r3-*] + three EOF disposition tables).
[FULL] ALL ELEVEN minor-escalation refutation files:
esc_refute_ntf_r{1,2}.md; esc_refute_objdom_r{1,2,3}.md;
esc_refute_deltacarrier_r{1,2,3}.md; esc_refute_crosslowering_r{1,2,3}
.md — every finding, verification record, and machine summary read
at source (tallies below are MY recount, not the summaries').
[FULL] the three E-5 files esc_refute_r4delta_l{0,1,2}.md + the
centerpiece E-5 disposition table phaseD_r22f_centerpiece.md §14
(:2208-2262) + every [ESC-E5-*] site read at-site (:570-575,
:784-790, :1806-1812, :1847-1851, :2179).
[SECT] VERDICT_blocco2.md §§2-4 + §7 LB-6..LB-14 (mandate + deferred
homes); VERDICT_r22f.md §§4-5 (RES-CAP-1..6) + §7 (landing list, the
RES-CAP-1-conditioned items L-B and registry row (2)) + §1/§8.
MEASURED THIS WINDOW (SR-12; commands run, outputs reproduced):
- marker censuses (grep -c "\[ESC-rN-"): objdom 30/18/6/0 (r1/r2/r3/
  r4); ntf 38/14/0; deltacarrier 69/30/44/0 (the two "[ESC-r4-"
  string hits at :90/:857 are QUOTED census text of minor (b), not
  markers — read at-site); crosslowering 45/15/10/0.
- ls esc_refute_*.md: exactly 14 files — r1/r2 for ntf, r1/r2/r3 for
  objdom/deltacarrier/crosslowering, l0/l1/l2 for r4delta. NO further
  round file exists for any item.
- mtime chain (stat, all 2026-08-20 −0400): consistent with every
  ordering claim in the round files; phaseD_minor_objdom.md 19:16:17
  is the LAST write to (b) — unchanged since before the (c) rounds,
  so the consumed (H6')/ship-gate block is bit-identical to what
  rounds 0-3 verified.
- ship-gate text: "[OBJ-DOM-IMPL] landed and used on both sides, OR
  the net-panel band included" present in BOTH minors (objdom :327,
  deltacarrier :611) — character-consistent; row-:300 license quotes
  verified by three refuter rounds and not re-litigated.
- [ESC-E5-*] sites: 14 marker-string hits; the three edits present
  at their claimed sites with content matching the refuters' fix
  shapes (verified at-site, §4 below). grep '^## 2.3' centerpiece =
  0 hits (J-1 repair still owed at landing, as of record).
Probes: NONE re-run this window — every probe carries an of-record
exit-0/ALL-PASS run in its author's window PLUS at least one
independent re-run by a later refuter in ITS window (ntf: 4 probes
re-run at r2; objdom: both probes re-run by r2 AND r3 refuters;
deltacarrier: probe re-run at r1, r2, r3; crosslowering: probe re-run
at r1, r2, r3; E-5: r4 probes re-run by L0, new probes run by their
authors). No adjudication below needs a further run.
Arithmetic re-verified by hand (sample): 2·(1+1/1.25) = 3.6;
70.11026×1.25 = 87.6378 (so "<= 87.6" rounds an upper bound DOWN —
ESC-NTF-r2-3 correct); log10(7.8/3.36e-4) = 4.37 decades; 1/4 − 1/5
= 1/20 (objdom r3 coefficient); cos15°·2 = 1.93 > 1.

==============================================================================
# 1. PER-ITEM DRY VERDICTS (recounted from files, duty i)

DRY criterion of record (centerpiece §13 tail, ratified by
VERDICT_r22f §3 and applied uniformly here): a round is DRY iff ZERO
BREAK and ZERO REPAIR findings are sustained in it; AMENDMENT/NOTE
findings do not block dryness but are adjudicated (§§2-4) and never
silently dropped.

| Item | Rounds run | Final-round recount | DRY verdict |
|---|---|---|---|
| E-1 NTF | rev-r1 → ref-r1 (0B/1R/0A/2N) → rev-r2 → ref-r2 (0B/0R/1A/3N) | 0 BREAK, 0 REPAIR | **DRY at round 2** (1 amendment + 3 notes adjudicated §2.1) |
| E-2 OBJ-DOM | rev-r1 → ref-r1 (1B/1R/1A/1N) → rev-r2 → ref-r2 (1B/0R/0A/1N) → rev-r3 → ref-r3 (0B/0R/0A/1N) | 0/0/0/1 | **DRY at round 3** (explicit "dry: TRUE" of record, recount confirms) |
| E-3 DELTA-CARRIER | rev-r1 → ref-r1 (0B/1R/1A/2N) → rev-r2 → ref-r2 (0B/1R/1A/1N) → rev-r3 → ref-r3 (0B/0R/0A/1N) | 0/0/0/1 | **DRY at round 3** (recount confirms) |
| E-4 CROSS-LOWERING | rev-r1 → ref-r1 (0B/1R/2A/1N) → rev-r2 → ref-r2 (0B/1R/1A/1N) → rev-r3 → ref-r3 (0B/0R/2A/1N) | 0 BREAK, 0 REPAIR | **DRY at round 3** (2 amendments + 1 note adjudicated §2.4) |
| E-5 RES-CAP-1 pass | ONE round by mandate, three lenses: L0 0B/0R/4A/1N; L1 0B/2R/3A/2N; L2 0B/1R/4A/4N; + reviser pass §14 | 0 BREAK unanimous; 3 REPAIRs found AND applied ([ESC-E5-1/2/3]) | **NOT-DRY-IN-ITS-SINGLE-ROUND** (repairs found); content verdict on the delta = unanimous SOUND; disposition §4 |

Escalation-finding grand total (my recount): 7 (E-1) + 7 (E-2) + 8
(E-3) + 10 (E-4) + 21 (E-5) = 53 findings across 14 files; every one
adjudicated below; 53 SUSTAINED, 0 OVERRULED.

==============================================================================
# 2. PER-FINDING ADJUDICATION, E-1..E-4 (duty i continued)

Rule applied: a finding is SUSTAINED when its defect was verified at
source/probe (by the next round's refuter or by this judge) and its
repair, where applied, was verified sound; OVERRULED requires the
objection itself to be wrong. Findings already FIXED in a later
revision and re-verified by a later refuter are SUSTAINED-AND-
RESOLVED (no action left). Findings from the final round of an item
(unapplied at cap) receive an explicit JUDGE DISPOSITION.

## 2.1 E-1 NTF (7 findings)

| Finding | Class | Verdict | Reason / disposition |
|---|---|---|---|
| ESC-NTF-r1-1 | REPAIR | SUSTAINED-AND-RESOLVED | probe scene C (kappa=2·NTF, 200/200 terminations, 87/200 PASSes) proves H1-H4 never imply the deterministic-envelope bullet; H5 adopted verbatim at [ESC-r2-1], scene D confirms the conditioned claim; r2 refuter re-verified |
| ESC-NTF-r1-2 | NOTE | SUSTAINED-AND-RESOLVED | attribution residues real (source-verified); fixed at [ESC-r2-2] by span-narrowing + "equivalently" retirement; r2 refuter verified (with the r2-2 nuance below) |
| ESC-NTF-r1-3 | NOTE | SUSTAINED-AND-RESOLVED | envelope-vs-realized dual role real; operational pin placed in F2-NTF-FLOOR-POPULATION at [ESC-r2-3]; conversion direction re-derived by r2 refuter |
| ESC-NTF-r2-1 | AMENDMENT | SUSTAINED | probe scene E is an executable counterexample AT the included boundary kappa_eff = (1+m)·NTF (H5's closed band admits step == T, which terminates at trip 1 AND passes cert at ratio 1.0 — engine semantics a1:444-448/:813 verified at source by the refuter); scene F verifies the strict-scoped form against the WORST H5-admissible realization (deterministic ⇒ valid for all). JUDGE DISPOSITION: repair ORDERED AT LANDING (LA-2, §6): strict regime kappa_eff > (1+m)·NTF; near-threshold band NTF < kappa_eff <= (1+m)·NTF; parenthetical "> T(z)"; §8 NTF-4 line — applied to the minor via append-only marker [ESC-J1-NTF] quoting this verdict BEFORE M0 transcription. One-character-class, probe-verified; the falsifier's closed ">=" selection clause stays (conservative, per the refuter) |
| ESC-NTF-r2-2 | NOTE | SUSTAINED | source nuance real ((2.10) numbered display on p. 50; content-restated on p. 51); repair substance stands; OPTIONAL clarifying parenthetical at LA-2 (refuter's own grading: optional) |
| ESC-NTF-r2-3 | NOTE | SUSTAINED | "<= 87.6" rounds an upper bound DOWN (derivable 87.6378; arithmetic re-verified this window) — R5 outward-rounding defect. JUDGE DISPOSITION: ORDERED AT LANDING (LA-2): "<= 87.64" |
| ESC-NTF-r2-4 | NOTE | SUSTAINED | §10 blanket sentence contradicted by the file's own §9 row; in-file bookkeeping only, does NOT land in M0. Disposition: one-word reword ("REVERTS or WEAKENS") applied with the [ESC-J1-NTF] pass; no landing impact |

## 2.2 E-2 OBJ-DOM (7 findings)

| Finding | Class | Verdict | Reason / disposition |
|---|---|---|---|
| ESC-OBJDOM-r1-1 | BREAK | SUSTAINED-AND-RESOLVED | (a.2) O(th1^6) false generically (sqrt cusp; probe slope 3.0000 vs claimed 6); fixed at [ESC-r2-1] (generic −(pi/6)·rtd·p'(0)·yt·th1^3), re-derived independently by BOTH the r2 and r3 refuters via two routes (series + cusp) — resolved in full including its own r2 residue |
| ESC-OBJDOM-r1-2 | REPAIR | SUSTAINED-AND-RESOLVED | kernel branch spurious-fire real (every kernel-sampled panel is a quadrature; probe rejector [3] slope 1.001); three-branch F-1 + P-1(2) declaration adopted at [ESC-r2-2]; branch-coverage attacked r2 (endpoint-p × trapezoid-in-y degeneracy proven ≡ branch (ii)) and re-proven analytically r3 — no uncovered combination |
| ESC-OBJDOM-r1-3 | AMENDMENT | SUSTAINED-AND-RESOLVED | "already landed" false per SR-12 (registry :209 drifted anchors persist — re-measured in three successive refuter windows); ordered-not-yet-applied sentence in place at [ESC-r2-3] and still true at the r3 read |
| ESC-OBJDOM-r1-4 | NOTE | SUSTAINED (verified-sound record; nothing owed) | coverage record accurate |
| ESC-OBJDOM-r2-1 | BREAK | SUSTAINED-AND-RESOLVED | "O(th1^6) IFF p'(0)=0" false in sufficiency (p3·th^3 → O(th1^5), coefficient (pi/10)·rtd·p3·yt probe-checked ratio 1.0007); fixed at [ESC-r3-1] at all three anchor sites; r3 refuter verified the corrected biconditional in BOTH directions by independent monomial decomposition, including the revision's new beyond-named-repair O(th1^7) clause |
| ESC-OBJDOM-r2-2 | NOTE | SUSTAINED (verified-sound record; nothing owed) | coverage items 1-13 accurate |
| ESC-OBJDOM-r3-1 | NOTE | SUSTAINED (dry-round verified-sound record; nothing owed) | includes the marker-sweep proof that "nothing else touched" holds |

## 2.3 E-3 DELTA-CARRIER (8 findings)

| Finding | Class | Verdict | Reason / disposition |
|---|---|---|---|
| ESC-DELTACARRIER-r1-1 | REPAIR | SUSTAINED-AND-RESOLVED | B_fam unrestricted-symbol exposure real (MIN-DELTACARRIER-3 class one section downstream); restriction promoted into the DEFINITION at [ESC-r2-1]; legs (a)-(c) re-proved by the r2 AND r3 refuters |
| ESC-DELTACARRIER-r1-2 | AMENDMENT | SUSTAINED-AND-RESOLVED | consumption version clause false (mtime-proven); corrected at [ESC-r2-2] with the explicit closure re-verification duty — DISCHARGED BY THIS VERDICT, §3 below |
| ESC-DELTACARRIER-r1-3 | NOTE | SUSTAINED-AND-RESOLVED | dangling clause reflowed at [ESC-r2-3] |
| ESC-DELTACARRIER-r1-4 | NOTE | SUSTAINED-AND-RESOLVED | probe tol_A scale wrong-as-stated (R5); re-derived at the largest-intermediate scale IN the probe at [ESC-r2-4]; re-run PASS in three successive windows, digits reproduced |
| ESC-DELTACARRIER-r2-1 | REPAIR | SUSTAINED-AND-RESOLVED | "supersonic-exit by construction ⟹ in W_cert" invalid (probe half [B]: supersonic-SPEED cell breaks the bound; u_x ≠ q); certificate form (M cosθ > 1, a-posteriori, report-on-fail) adopted at [ESC-r3-1a..g] at all four sites + two history annotations; r3 refuter grep-swept "by construction" — no operative instance survives |
| ESC-DELTACARRIER-r2-2 | AMENDMENT | SUSTAINED-AND-RESOLVED | W_cert phase-quantifier pinned at [ESC-r3-2a/b] (mu-a.e.-all-phase; mixed reading excluded); both readings re-checked sound by the r3 refuter |
| ESC-DELTACARRIER-r2-3 | NOTE | SUSTAINED-AND-RESOLVED | Pa adjacency sentence added as mandatory landing-text item [ESC-r3-3]; premise verified at MASTER :251 at source |
| ESC-DELTACARRIER-r3-1 | NOTE | SUSTAINED | "equivalently, write W_cert(xi) inside the integral" overclaims set/value equivalence (strict inequality possible between the two pinnings' sups); the adjacent scoped claim is the true, load-bearing one; no displayed statement false, no B_fam value ever quoted. JUDGE DISPOSITION: the one-word repair is ORDERED INTO THE LANDING CUT (LA-3, §6): "— alternatively, write W_cert(xi) inside the integral (either pinning closes every proof; both readings agree for every named consumer)" — folded wherever [T-DCRX] extracts [ESC-r3-2a] |

## 2.4 E-4 CROSS-LOWERING (10 findings)

| Finding | Class | Verdict | Reason / disposition |
|---|---|---|---|
| ESC-CROSSLOWERING-r1-1 | REPAIR | SUSTAINED-AND-RESOLVED | H8 printed inequality unit-incoherent (H-scale RHS bounding g-scale variation) and too weak for its consequent; h-scaled form adopted at [ESC-r2-1]; dimensional coherence re-derived by the r2 refuter |
| ESC-CROSSLOWERING-r1-2 | AMENDMENT | SUSTAINED-AND-RESOLVED | coefficient-sensitivity Lipschitz clause undeclared; added to H7 at [ESC-r2-2], step (iv) wired to it |
| ESC-CROSSLOWERING-r1-3 | AMENDMENT | SUSTAINED-AND-RESOLVED | §9 machine-harvest bullet carried stale pre-repair labels; rewritten in place at [ESC-r2-3], [ESC-r1-9] kept as consumed derivation record |
| ESC-CROSSLOWERING-r1-4 | NOTE | SUSTAINED-AND-RESOLVED | "EXACTLY the q = 1 side" → sufficiency form at [ESC-r2-4] |
| ESC-CROSSLOWERING-r2-1 | REPAIR | SUSTAINED-AND-RESOLVED | "c depending ONLY on kernel shape" false once step (iv) absorbs C_s + Lipschitz constants (RES-CAP-1 class: refuter-prescribed "(constant absorbed in c)" adopted without reconciling the statement); dependence restated at [ESC-r3-1] |
| ESC-CROSSLOWERING-r2-2 | AMENDMENT | SUSTAINED-AND-RESOLVED | freshly-printed "q = 1 = H7" + un-swept §3 instance; both one-phrase edits at [ESC-r3-2]; r3 refuter's wider grep confirms live text clean |
| ESC-CROSSLOWERING-r2-3 | NOTE | SUSTAINED-AND-RESOLVED | "i.e." → "hence a fortiori" at [ESC-r3-3] (contingent condition fired) |
| ESC-CROSSLOWERING-r3-1 | AMENDMENT | SUSTAINED | CLG-D3 is the RMS refinement of D2's law and never received the r1 H7/q=1 conditioning — a live un-conditioned u-linear expected law, concept-level instance the phrase-level sweeps could not catch. JUDGE DISPOSITION: ORDERED AT LANDING (LA-4, §6), refuter's named text: "Under the CLG-D2 hypotheses (H1-H4, H6, H7) with H5, ..." (or the equivalent appended clause); SCHEMA grade and E1 falsifier unchanged |
| ESC-CROSSLOWERING-r3-2 | AMENDMENT | SUSTAINED | magnitude bounds (sup_k ||dR_k/dW||, ||phi_k||, operand-scale ratios) that step (iii)'s "bounded factor" and c's finiteness lean on are declared by no hypothesis. JUDGE DISPOSITION: ORDERED AT LANDING (LA-4): extend H7's coefficient clause "uniformly Lipschitz AND uniformly bounded on the march tube (magnitude bounds sup_k ||dR_k/dW||, sup_k ||phi_k|| absorbed in c)" + extend the statement parenthetical "(C_s, the coefficient-map Lipschitz bounds, and the coefficient magnitude bounds)". AG-1 declaration, no label move |
| ESC-CROSSLOWERING-r3-3 | NOTE | SUSTAINED | kappa_eff·G_rms factorization presents rms of a product as product of rms (decorrelation silently assumed, plausibly violated in the E2 direction). Its contingent condition ("if ever edited") FIRES because r3-1's edit is ordered. JUDGE DISPOSITION: ORDERED AT LANDING (LA-4): "with kappa_eff·G_rms := rms_k(kappa_k G_k), the quadratic mean of the per-stage product" |

==============================================================================
# 3. SEQUENCING GATE (H6' + re-pinned ship-gate) — VERDICT: **SATISFIED**

Stated explicitly (SR-C4-9; silence forbidden):
(1) The (c) closure re-verification duty ([ESC-r1-0]/[ESC-r2-2] of
phaseD_minor_deltacarrier.md — "the judge RE-VERIFIES the consumed
(H6')/ship-gate block against (b)'s CLOSED text") is DISCHARGED THIS
WINDOW: minor (b) is CLOSED BY THIS VERDICT at its r3 state (DRY;
no finding of any round amended its OBJDOM-5/(H6')/ship-gate block
:290-330, which carries only [ESC-r1-3]); mtime 19:16:17 unchanged
since before every (c) round (measured this window) ⇒ the consumed
block IS (b)'s closed text, bit-identical. The adoption does NOT
re-open.
(2) The two minors as closed are CONSISTENT: one shared (H6')
two-branch form ((H6'-A) fix-A-panel-inclusive both sides OR (H6'-B)
both-coded + explicit net-two-wall-panel band, anti-conservative
sign declared, folded into DC-5(a)) and ONE ship-gate text, verified
character-consistent in both files this window and against
VERDICT_blocco2 §4(2) by three refuter rounds: "no (value, delta)
row ships unless '[OBJ-DOM-IMPL] landed and used on both sides, OR
the net-panel band included'" — the row-:300 banded-or-repaired
license correctly read.
(3) SEQUENCE HONORED: (b) reached DRY (19:22:33) before (c)'s first
escalated revision was written (19:29:27) and (c) consumed (b)'s
escalated OBJDOM-5 output as input of record; both are now closed in
this single verdict, (b) logically first.
(4) SCOPE OF SATISFACTION, stated so no one over-reads it: the gate
is satisfied AS A SEQUENCING/LANDING CONDITION — the [T-DCRX] and
OBJ-DOM landings may proceed (§6). The ship-gate itself remains a
LIVE, ARMED F2 gate on every future (value, delta) Verdict row:
nothing about this closure ships a row. [OBJ-DOM-IMPL] is still an
F2 duty; until it lands and is used on both sides, only the
(H6'-B) net-panel-band branch can ship a row.

==============================================================================
# 4. E-5 — RES-CAP-1 ADJUDICATION (duty iii)

Per-finding adjudication (21 findings; classes as filed by the three
lenses; each verified against the centerpiece text and the §14
disposition table this window):

- E5-L1-1 (REPAIR, identity-carriage at :571 + :782): SUSTAINED —
  APPLIED as [ESC-E5-1] (both sites verified at-site this window;
  bracket text carries mu = J_TRUE floor + H-G6 instantiation gate,
  matching the fix shape). JUDGE-VERIFIED AS FIXED.
- E5-L1-5 (REPAIR, R-17/R-14 decider re-licensing exposure; probe
  part C: the printed clause PASSES on the annulus of record with
  form-(T) bound 0 vs shift 2): SUSTAINED — APPLIED as [ESC-E5-2]
  (R-17 scope clause: effective-curvature horn only, segment-
  feasibility clause required, annulus = standing refuter, GLOBAL
  coverage un-claimable; mirrored at the R-14 decider; both sites
  verified at-site this window). JUDGE-VERIFIED AS FIXED.
- E5-L2-1 (REPAIR) = E5-L0-4 (AMENDMENT), joint (missing R22F-L2-24
  NOTE row vs the correct NOTES-5 count): SUSTAINED — APPLIED as
  [ESC-E5-3] (row present at :2179, verified this window; COUNTS
  line correctly unchanged). JUDGE-VERIFIED AS FIXED.
- E5-L0-3 limb (a): SUSTAINED — DISCHARGED by [ESC-E5-1](ii) (same
  site, same bracket), verified.
- The EIGHT deferred AMENDMENT inputs — E5-L0-1 (= E5-L2-4, H-G5
  "equivalently" gloss is star-shapedness, not equivalence; probe of
  record), E5-L0-2 (mu_eff symbol collision H-G6 vs R-17), E5-L0-3(b)
  (= E5-L2-5, SAMPLED-SUP at-site brackets at (F) and [REV2-r3-3](b)),
  E5-L1-2 (leg-(3) SAMPLED-DIRECTIONAL (estimate) class clause; probe
  parts A-B), E5-L1-3 (H-G6 existence/typing/positivity guards),
  E5-L1-4 (landing rename split mu_curv vs mu_red), E5-L2-2 (H-G6
  read on the (E)-certified ball at the band-lower-edge sustained
  floor mu_meas − b_E, never the bare point measurement; probe of
  record), E5-L2-3 (cross-channel bilinear blocks at second order not
  excluded): ALL SUSTAINED — each is probe-witnessed or verified at
  source by its lens, none was contested, and the reviser's
  DEFERRED-TO-LANDING routing follows the E-1..E-4 named-repairs-are-
  inputs rule correctly. JUDGE DISPOSITION: MANDATORY AT LANDING —
  see LA-5 (§6). They are landing-facing hypothesis/licensing text;
  the L-B edit that transcribes §2.2-bis and the (vi) row MUST carry
  them (fix shapes verbatim from the three refuter files, as indexed
  by the §14 table rows).
- The SEVEN NOTEs (E5-L0-5, E5-L1-6, E5-L1-7, E5-L2-6..L2-9):
  SUSTAINED as filed (positive-verification/hygiene records). The two
  named optional touches (E5-L1-6 R-14 parenthetical hygiene;
  E5-L2-8 estimate-class check-pass sharpening) are RECOMMENDED at
  LA-5, not mandatory. E5-L1-7(g)(i) (M-RED value-deriver sampling
  blindness) is minted as residue R-ESC-3 (§7). E5-L1-7(g)(ii)
  (VERDICT_blocco2 :62-64 dry-parenthetical omits L0's amendment) is
  RECORDED here as its correction of record: harmless, dry=false and
  census 66 unaffected; no edit to a closed verdict.

**RES-CAP-1: DISCHARGED.** The owed targeted one-round three-lens
refutation pass HAS RUN (files of record above); the content verdict
on the [REV2-r4-*] delta is unanimous SOUND / ZERO BREAK at all
three lenses; the three REPAIRs are applied in-file ([ESC-E5-1/2/3])
and judge-verified at-site this window. Consequently, at the L-B
landing of §2.2-bis and the (vi) row, the "round-4 delta unrefereed"
DECLARED LINE IS RETIRED and REPLACED by: "round-4 delta refereed
(E-5 targeted pass of record, esc_refute_r4delta_l{0,1,2}.md, 0
BREAK; [ESC-E5-1/2/3] applied; deferred inputs executed at this
edit per VERDICT_escalation_c4 LA-5)". The deferred-inputs
obligation is RENAMED as residue **RES-E5-LAND** (§7): owed IN the
same [REV2-J1] editorial pass; any input NOT applied there must
carry a declared named-residue line at the landing site — silent
drop forbidden. The E-5 pass's own applied repairs are carriage/
scope/bookkeeping brackets verified directly by this judge (the
RES-CAP-1 exposure class does not recur at bracket-insertion grade);
no new refutation round is owed for them.

==============================================================================
# 5. FINAL RIGOR LABELS FOR THE MINORS' ADOPTED STATEMENTS (label
#    authority of record; guidance labels of VERDICT_blocco2 §2 now
#    ADOPTED-AS-ADJUSTED below)

## 5.1 NTF (minor a) — statements land per LA-2
- NTF-1 (roundoff-floor model): **SCHEMA** (H1-H4; measured instance
  kappa_eff,worst ∈ [51.7, 70.1], carrier cited).
- NTF-2 (two-sided certificate semantics, PASS ⇒ err <= 2·(T+floor)
  = 2·NTF·(1+1/eta)·EPS·sc): **THEOREM\*** on the repaired constant;
  star discharges at the F2 floor measurement.
- NTF-3 (window inequality, per-consumer A_c): **THEOREM\***
  conditional-on-declared-A_c; derived form NTF = eta·kappa_q:
  **SCHEMA**; incumbent NTF = 100: PRACTICE-validated valid instance
  (headroom 1.426; /2 flip = model prediction, witness 51.665 > 50).
- NTF-4 (termination coupling): **SCHEMA**, conditioned on explicit
  H5, with the STRICT regime scoping (kappa_eff > (1+m)·NTF) per
  ESC-NTF-r2-1 as ordered at LA-2.
- NTF-5 (seam; threshold object T vs certified-error object):
  **PRACTICE** (C34/C35 consumption unchanged).

## 5.2 OBJ-DOM (minor b) — adjudication and text land per LA-1
- OBJDOM-1 as restated: (a.1) discrete identity + (b) + (c):
  **THEOREM**; (a.2) truncation-order ladder (generic O(th1^3) with
  coefficient −(pi/6)·rtd·p'(0)·yt; O(th1^6) ⇔ p'(0)=0 AND p'''(0)=0;
  O(th1^5) branch with coefficient (pi/10)·rtd·(p'''(0)/6)·yt):
  **THEOREM** (verified both directions, two independent routes,
  probe-controlled).
- OBJDOM-2 (absorption branch dead, >= 96x): **THEOREM\***.
- OBJDOM-3 (Pa-anchor): **THEOREM**.
- OBJDOM-4 (fix-A objective-of-record at F2 entry; fix-B scoping
  clause interim): **ADOPTED AS THE DECISION OF RECORD** (PRACTICE-
  class adjudication; survived all three rounds untouched). The §4
  landing text's PROPOSED status is lifted: it LANDS (LA-1).
- OBJDOM-5 ((H6') composition + re-pinned ship-gate): **SCHEMA**
  (proof obligation transferred to (c), discharged there).
- F-1 (three-branch) / F-2 (both paths): pinned falsifiers of
  record, F2 duties as named.

## 5.3 DELTA-CARRIER (minor c) — lands per LA-3 at [T-DCRX]
- DC-1 (fixed-exit-area relaxation lemma, Pa >= 0): **THEOREM\***
  under declared conditionals (a) (H3) a-posteriori certification,
  (b) bell-only topology, (c) S1 piecewise-C1 shock-free fields;
  mu-integrated form with the explicit a.e.-xi clause.
- DC-2 (delta semantics): **THEOREM\*** under the W_cert restriction
  (phase-quantified pin [ESC-r3-2a], with the LA-3 one-word repair);
  semantic rule ("distance to the L-unconstrained fixed-eps ceiling")
  = of record.
- DC-3 (rung-family composition, restricted B_fam, certificate-form
  membership): **THEOREM under V1-V2**.
- DC-4 (KKT weak-duality rung): inequality **THEOREM**; regime
  clause **SCHEMA**; DORMANT until (P)-as-posed unilateral-regime
  capped runs exist ([DC-F2-3] contingent).
- DC-5 (carrier practice rules incl. (H6') branch disposition, Pa
  convention, (H2b) check): **PRACTICE**.
- DC-6 (T3-collapse consistency, certificate-conditional
  attainment): **SCHEMA**.

## 5.4 CROSS-LOWERING (minor d) — lands per LA-4
- CLG-D2 (chain floor law): **THEOREM\*** under H1-H4 + H6 + H7
  (H7 with the Lipschitz clause AND, per LA-4, the magnitude-bounds
  clause); u-linear form CONDITIONAL on q = 1 (H7 sufficient, E3-
  adjudicated); c depends on kernel shape AND the H7 regularity
  constants.
- CLG-D3 (RMS refinement): **SCHEMA**, conditional on the CLG-D2
  hypotheses + H5 (LA-4 edit), with the joint rms_k(kappa_k G_k)
  definition.
- CLG-D5 (FD amplification law): **THEOREM\*** on the cross-lowering
  branch; same-lowering cancellation leg **SCHEMA conditional on
  H8** (h-scaled form).
- CLG-D6 (pinning discipline corollary): **SCHEMA conditional on
  H8**.
- CLG-D1 / D4 / D7: **SCHEMA**; CLG-D4-ALT: **CONJECTURE**.
- E3 discriminator at ~4.4 decades = the F2-CLG-SCALE duty spec of
  record.

## 5.5 Centerpiece (E-5)
NO label of VERDICT_r22f §1 moves — the E-5 pass found zero BREAKs
and its repairs/amendments are carriage/scope/class-label
completions; VERDICT_r22f §1 remains the single centerpiece label
authority (one authority per statement, unchanged).

==============================================================================
# 6. CONSOLIDATED LANDING ADDENDUM (duty iv — merged with, never
#    duplicating, VERDICT_r22f §7 [executed via LB-1] and
#    VERDICT_blocco2 §7 [LB-1..LB-14 stand as ordered there];
#    verbatim-applicable; orchestrator executes)

LA-1 — OBJ-DOM LANDING (concretizes the LB-6 deferred home).
(i) M0 site: the objective-declaration vicinity in
docs/rde_nozzle_MASTER.md (where the design functional/objective of
(P) is declared, D2.6 context). LAND VERBATIM the §4 text of
phaseD_minor_objdom.md (:461-470), which begins "OBJECTIVE DOMAIN
[OBJ-DOM adjudicated, Phase D 2026-08-20]: the functional of record
at F2 entry is the panel-inclusive J_A ..." — its PROPOSED status is
lifted by this verdict; the interim fix-B scoping regime (value +
gradient + Pa statements scoped, all three axes) lands WITH it.
(ii) Registry row variational-driver:objective-omits-throat-panel:
the LB-6(a) code-anchor refresh and LB-6(b) note append stand AS
ORDERED (execute if not yet applied — still pending at the last
SR-12 measurement of record); ADDITIONALLY append to the owner field
(verbatim):
  "; ESCALATION E-2 CLOSED 2026-08-20 (VERDICT_escalation_c4: DRY at
  round 3, 2 BREAKs found in-loop and fixed): ADJUDICATED fix-A
  objective-of-record at F2 entry, interim = fix-B scoping (landed);
  OBJDOM-1 THEOREM as restated (truncation ladder O(th1^3) generic /
  O(th1^5) / O(th1^6) iff p'(0)=0 AND p'''(0)=0), OBJDOM-2 THEOREM*,
  OBJDOM-3 THEOREM; F-1 three-branch + F-2 two-path falsifiers
  pinned; duties [OBJ-DOM-IMPL]/[OBJ-DOM-AB]/[OBJ-DOM-REBASE]"

LA-2 — NTF LANDING (concretizes the LB-7 deferred home).
(i) PRE-STEP (judge-ordered edits, append-only marker [ESC-J1-NTF]
quoting this verdict, applied to phaseD_minor_ntf.md BEFORE
transcription): (a) §4 + §8: deterministic-envelope regime made
STRICT — "kappa_eff(cell) > (1+m)*NTF"; near-threshold band "NTF <
kappa_eff(cell) <= (1+m)*NTF"; in-bullet parenthetical "realized
step >= floor_z/(1+m) > T(z)"; §8 line "unreachability only at
kappa_eff > (1+m)*NTF UNDER H5" (ESC-NTF-r2-1; probe scene F =
executable witness of record). (b) §5: "<= 87.6" → "<= 87.64"
(ESC-NTF-r2-3, R5 outward rounding). (c) §10: "rewrites" →
"REVERTS or WEAKENS" (ESC-NTF-r2-4; in-file bookkeeping). (d)
OPTIONAL: the ESC-NTF-r2-2 clarifying parenthetical on (2.10).
(ii) M0 site: engine-discipline / certificate block beside the C20
kappa-band program (one-window C18/C20-Tier-1 seam preserved). LAND
NTF-1..NTF-5 with the §5.1 labels; the threshold-object vs
certified-error-object disambiguation sentence lands verbatim; F2
duties F2-NTF-FLOOR-POPULATION (rides F2-C20-CERTQUAL-CAMPAIGN
Tier-1) and F2-NTF-TERMCOUPLE-TRIPCOUNT named at the M0 site.
(iii) Registry row engine-core:F5-underived-factors, owner APPEND
(verbatim):
  "; ESCALATION E-1 CLOSED 2026-08-20 (VERDICT_escalation_c4: DRY at
  round 2; boundary-strictness edit judge-ordered at landing,
  probe-verified): derivation LANDED — NTF-2 THEOREM* (repaired
  constant 2(T+floor)), NTF-3 window THEOREM* conditional on
  declared A_c + derived form SCHEMA (NTF = eta*kappa_q), NTF-1/
  NTF-4 SCHEMA (H5 explicit, strict regime kappa_eff > (1+m)*NTF),
  incumbent 100 = valid instance (headroom 1.426); measured halves =
  F2-NTF-FLOOR-POPULATION + F2-NTF-TERMCOUPLE-TRIPCOUNT"
(iv) Lit promotions LB-3/LB-4/LB-5: already ordered by
VERDICT_blocco2 — NOT restated (no duplication).

LA-3 — DELTA-CARRIER LANDING (concretizes the LB-8 deferred home;
gate satisfied per §3, so the landing is UNGATED).
(i) M0 site: Part III, new block [T-DCRX] adjacent [T-EAP]/OP-0
(after the sonic-cap sharpening, ~:1255-1330; site ratified twice).
LAND per phaseD_minor_deltacarrier.md §9 as revised through
[ESC-r3-*], which pins: DC-1 (THEOREM*, Pa >= 0, conditionals
(a)-(c)) + DC-2 WITH the W_cert restriction and phase-quantifier pin
+ pointer to the rung family (DC-3/DC-4 incl. dormancy clause;
B_fam DEFINED over A_phase(C) ∩ W_cert, membership = a-posteriori
certificate M cosθ > 1 — the retracted "by construction" inference
does NOT land) + DC-5 practice rules as extended ((H6') branch
disposition, Pa convention, (H2b) check) + DC-6 one-liner at the
T3/T4 attainment site + the MANDATORY Pa-adjacency sentence
[ESC-r3-3] + the G-12 scope sentence (verbatim in §9, [ADV],
CT-6-clean). LANDING-CUT EDIT (judge-ordered, ESC-DELTACARRIER-r3-1):
wherever the [ESC-r3-2a] pin is extracted, print "— alternatively,
write W_cert(xi) inside the integral (either pinning closes every
proof; both readings agree for every named consumer)" in place of
the bare "equivalently" clause.
(ii) Registry rows: LB-8 and LB-9 appends stand AS ORDERED;
ADDITIONALLY append to row pipeline:delta-carrier-F2-entry owner
(verbatim):
  "; ESCALATION E-3 CLOSED 2026-08-20 (VERDICT_escalation_c4: DRY at
  round 3; sequencing gate §4(3) SATISFIED — (b) closed first, (H6')/
  ship-gate block bit-identical across all rounds): lemma LANDED at
  [T-DCRX] — DC-1 THEOREM* (Pa >= 0), DC-2 THEOREM* under W_cert
  (phase-quantified), DC-3 THEOREM under V1-V2, DC-4 THEOREM
  (inequality; regime clause SCHEMA, DORMANT), DC-5 PRACTICE, DC-6
  SCHEMA; ship-gate remains ARMED for every (value, delta) row:
  [OBJ-DOM-IMPL] both sides OR net-panel band included; duties
  [DC-F2-1..5] incl. certificate-on-entry + (H2b) report-on-fail"

LA-4 — CROSS-LOWERING LANDING (concretizes the LB-10 deferred home).
(i) PRE-STEP (judge-ordered edits, append-only marker [ESC-J1-CLG]
quoting this verdict, applied to phaseD_minor_crosslowering.md
BEFORE transcription — the three r3-refuter named repairs, verbatim):
(a) §4 CLG-D3 statement: "Under the CLG-D2 hypotheses (H1-H4, H6,
H7) with H5, the expected floor scales as ..." (r3-1). (b) §1 H7
coefficient clause extended: "uniformly Lipschitz AND uniformly
bounded on the march tube (magnitude bounds sup_k ||dR_k/dW||,
sup_k ||phi_k|| absorbed in c)"; §3 statement parenthetical: "(C_s,
the coefficient-map Lipschitz bounds, and the coefficient magnitude
bounds)" (r3-2). (c) §4: "with kappa_eff · G_rms := rms_k(kappa_k
G_k), the quadratic mean of the per-stage product" (r3-3).
(ii) M0 site: engine-discipline block adjacent the same-lowering
standing rule. LAND CLG-D1..D7 + D4-ALT with the §5.4 labels; the
F2-CLG-SCALE identification design (E1/E2/E3, P1/P2/P3 at ~4.4
decades) lands as the duty spec; seam declarations (NTF minor owns
eps_N; F2-C44-FDSTEP owns step choice) land verbatim.
(iii) Registry row engine:cross-lowering-gradient-floor, owner
APPEND (verbatim):
  "; ESCALATION E-4 CLOSED 2026-08-20 (VERDICT_escalation_c4: DRY at
  round 3; D3-conditioning + H7-magnitude + rms-product edits
  judge-ordered at landing): derivation LANDED — CLG-D2 THEOREM*
  under H1-H4+H6+H7 (u-linear conditional on q = 1, H7 sufficient,
  E3-adjudicated), CLG-D5 THEOREM* cross-branch / SCHEMA-cond-H8
  same-branch, CLG-D6 SCHEMA-cond-H8, D1/D3/D4/D7 SCHEMA, D4-ALT
  CONJECTURE; F2-CLG-SCALE = E1/E2/E3 with H7/H8 cheap adjunct
  checks; Higham 2ed = conditional THEOREM-upgrade path only"

LA-5 — E-5 CENTERPIECE DELTA at the L-B landing (amends, does not
restate, VERDICT_r22f §7 L-B):
(i) Execute the [REV2-J1] "## 2.3" header repair pre-step (RES-CAP-6)
    — unchanged.
(ii) RETIRE the "round-4 delta unrefereed" declared line on §2.2-bis
    and the (vi) row; REPLACE with the refereed line quoted in §4
    above.
(iii) MANDATORY in the same editorial pass: execute the EIGHT
    deferred amendment fix shapes, verbatim from their refuter
    files as indexed by centerpiece §14 (E5-L0-1/L2-4 star-
    shapedness wording at both H-G5 printings; E5-L0-2 mu_eff
    rename + composition sentence at R-17; E5-L0-3(b)/L2-5
    SAMPLED-SUP at-site brackets at (F) and [REV2-r3-3](b);
    E5-L1-2 leg-(3) SAMPLED-DIRECTIONAL (estimate) class clause +
    R-15/R-16 carriage; E5-L1-3 H-G6 existence/M-operator-typing/
    mu_eff>0 guards; E5-L1-4 two-symbol landing split; E5-L2-2
    H-G6 read on the (E)-certified ball at mu_meas − b_E; E5-L2-3
    cross-channel bilinear clause). Any input NOT applied must
    carry a declared named-residue line at the landing site
    (RES-E5-LAND rule, §7).
(iv) The E5-L1-4 split AMENDS the L-B rename instruction: the
    landing assigns mu_curv (gradient route, J_TRUE floor,
    H-G6-gated) AND mu_red (value route, measured J_red floor);
    the (vi) cell's two formulas land with their own symbols.
(v) RECOMMENDED (optional): E5-L1-6 R-14 parenthetical hygiene;
    E5-L2-8 "a check-pass at estimate class is itself
    estimate-class" sharpening.

LA-6 — PROGRESS closure edit (amends LB-11): the queue entry becomes
"Blocco-2 escalations CLOSED (VERDICT_escalation_c4, 2026-08-20):
E-1/E-2/E-3/E-4 DRY, E-5/RES-CAP-1 DISCHARGED; sequencing gate
SATISFIED; landings LA-1..LA-5 owed at the M0/registry landing
window; ship-gate remains armed for F2 (value, delta) rows."

LA-7 — PAPERS NEEDED (aggregated from all 14 escalation files +
reviser passes): ALL DECLARED EMPTY; nothing new. The Higham ASNA
2ed conditional entry and the VERDICT_blocco2 §8 aggregate stand
unchanged — no duplication, no new procurement.

NO-DUPLICATION DECLARATION: LB-1..LB-14 (VERDICT_blocco2 §7) and
VERDICT_r22f §7 L-A..L-F + rows (1)-(4) + §7.3 stand exactly as
ordered there; this addendum only (a) lifts the PROPOSED status of
the minors' landing texts, (b) concretizes the deferred minor homes,
(c) adds the five escalation-closed registry appends, and (d) amends
the L-B edit with the E-5 dispositions. Nothing is restated.

==============================================================================
# 7. NAMED RESIDUES (duty v — none label-inflated; every §5 label
#    stands independent of these)

- R-ESC-1 — JUDGE-ORDERED UNREFEREED EDIT TEXTS: the LA-2(i),
  LA-3(i) landing-cut, and LA-4(i) edits are refuter-named repair
  texts adopted by judge order WITHOUT a further refutation round
  (cap reached; loop precedent acknowledged). Exposure priced:
  each is a one-clause/one-character-class edit, deterministic, and
  probe-verified where a probe applies (NTF scene F; CLG probe
  unchanged — textual edits only; DC one word). Declared at their
  [ESC-J1-*] markers; any future refuter may attack them as marked
  text.
- R-ESC-2 = RES-E5-LAND — the eight deferred E-5 amendment inputs,
  owed in the L-B/[REV2-J1] editorial pass (LA-5(iii)); un-applied
  inputs carry declared residue lines at the landing site.
- R-ESC-3 — M-RED VALUE-DERIVER SAMPLING BLINDNESS (from E5-L1-7(g)
  (i), probe esc_probe_r4delta_lh_leg3_blindness.py part B: sampled
  delta = 0 at two refinement levels with macroscopic true shift):
  the delta deriver leg (3) shares the directional/sub-sample-width
  blindness limbs. Owner: the M-RED §3.6 gradient-measurement rider
  / R-15 extension (F2, row theory:r22f-optimum-shift-gradient-route
  trigger already covers it); the E5-L1-2 clause carries the class
  label at the L_H side.
- R-ESC-4 — F2 MEASURED HALVES (carried, not new; listed for the
  sweep): F2-NTF-FLOOR-POPULATION + F2-NTF-TERMCOUPLE-TRIPCOUNT
  (H5 band ratification); F2-CLG-SCALE (E1/E2/E3 + H7 state-diff +
  H8 self-asymmetry cheap adjuncts); [DC-F2-1..5] (incl.
  certificate-on-entry [ESC-r3-1d] + (H2b) report-on-fail);
  [OBJ-DOM-IMPL]/[OBJ-DOM-AB]/[OBJ-DOM-REBASE]; [DC-F2-3] contingent
  (dormant until unilateral-regime runs exist).
- R-ESC-5 — CENTERPIECE CAP RESIDUES RES-CAP-2..5 (R-16 L_H
  underived; R-14 KS-margin convexity OPEN; R-15 eps_U sampled-sup
  ladder; R-17 prox-regular refinement — now scope-clamped by
  [ESC-E5-2]) CARRY UNCHANGED per VERDICT_r22f §4; RES-CAP-6/J-1
  executes at LA-5(i).
- RECORD-SIDE NOTE (no action): VERDICT_blocco2 §1's dry-status
  parenthetical "L0: 1 BREAK + 1 REPAIR" omits L0's round-4
  amendment (E5-L1-7(g)(ii)); harmless — dry=false and the census
  66 stand; recorded here as the correction of record.

==============================================================================
# 8. MACHINE SUMMARY (duty vi)

verdict: ALL FOUR MINOR ESCALATIONS CLOSED — E-1 DRY(r2), E-2
  DRY(r3), E-3 DRY(r3), E-4 DRY(r3) under the zero-BREAK/REPAIR
  criterion; E-5 executed (one round, three lenses, 0 BREAK
  unanimous, 3 REPAIRs applied [ESC-E5-1/2/3] judge-verified);
  RES-CAP-1 DISCHARGED with the deferred inputs renamed RES-E5-LAND
findings_adjudicated: 53/53 SUSTAINED (E-1: 7, E-2: 7, E-3: 8,
  E-4: 10, E-5: 21), 0 OVERRULED; cap-unapplied findings receive
  judge dispositions (ordered-at-landing via [ESC-J1-*] markers:
  NTF strict-boundary + outward-rounding; CLG D3-conditioning +
  H7-magnitude + rms-product; DC landing-cut one-word)
final_labels: §5 of record — NTF-2/NTF-3 THEOREM* (repaired
  constant; conditional on declared A_c) + NTF-1/4 SCHEMA + NTF-5
  PRACTICE; OBJDOM-1/3 THEOREM + OBJDOM-2 THEOREM* + OBJDOM-4
  adjudication ADOPTED (fix-A of record, fix-B scoping interim,
  landing text lands) + OBJDOM-5 SCHEMA; DC-1/DC-2 THEOREM* + DC-3
  THEOREM (V1-V2) + DC-4 THEOREM/SCHEMA-dormant + DC-5 PRACTICE +
  DC-6 SCHEMA; CLG-D2 THEOREM* (H1-H4+H6+H7) + CLG-D5 THEOREM*/
  SCHEMA-cond-H8 + CLG-D6 SCHEMA-cond-H8 + D1/D3/D4/D7 SCHEMA +
  D4-ALT CONJECTURE; centerpiece labels UNCHANGED (VERDICT_r22f §1
  sole authority)
sequencing_gate: SATISFIED (§3) — (b) closed DRY first, (H6')/
  ship-gate block bit-identical across all rounds (mtime + at-site
  verification this window), (c) closure re-verification duty
  DISCHARGED; ship-gate remains ARMED for F2 (value, delta) rows
rescap1: DISCHARGED (§4) — unrefereed line retired at the L-B
  landing, replaced by the refereed line; residue renamed
  RES-E5-LAND (8 deferred inputs owed in the [REV2-J1] pass, silent
  drop forbidden)
landing_addendum: 7 items LA-1..LA-7 (§6), merged with LB-1..LB-14
  and VERDICT_r22f §7 without duplication; five escalation-closed
  registry appends verbatim; two [ESC-J1-*] pre-step edit sets
residues: [R-ESC-1 judge-ordered unrefereed edits (declared,
  probe-backed), RES-E5-LAND, R-ESC-3 M-RED deriver sampling
  blindness (owner M-RED rider/R-15), R-ESC-4 F2 measured halves
  (carried), R-ESC-5 RES-CAP-2..5 carried + J-1 executes at landing]
papers_needed: NONE new (all 14 escalation files declared empty;
  Higham ASNA 2ed conditional entry unchanged per VERDICT_blocco2
  §8)
ct6: clean (no nozzle-paper number in this verdict or in any
  escalation file, re-checked)
