# STAGE B — item PROOF — ADVOCATE A0 (genuine advocate of the ALTERNATIVE) — S-REVIEW 2026-09-05

Persona: the verification engineer of the trees (optimization lens: result = (code hash, checker hash, envfp); quotable iff
Delta >= sum of bands + b_repro) together with the record's SP8 judge. Alternative defended: the BAND-RELATIVE certification
threshold with a contraction guard (A11) + the MEASURED cross-triple amplification rho_meas (A9b) + the [CERT-STAB] requirement
text (SP8 §6) with the emendations of §6 below. Incumbent attacked: the roundoff-relative per-cell certificate (NTF*EPS*sc, C18
single-author) + the A-1 margin numeral 1/K_RICH (TWIN §9). Scope rule honoured: every argument below changes either the
QUOTABILITY of the decisive delta (credibility of Q0's answer) or the cost of reaching a quotable arm (cost of Q0's answer).

READ AT THE SOURCE (files, anchors): stageB_items.json "PROOF"; stageA_diff_SP8.md integral (§2 A9b/A11, §3.2-3.4, §5 F-1/F-2/
F-3, §6, §7, §13); LEVERS_F1-F6_draft.md §F4; M0 :3181-3188 (VI.6), :3425-3440 (S20 crawl, "certdiag 8/8"), :3654-3770 (NTF-1..
NTF-5), :4250-4299 (version binding + A-1); choice_ledger C17/C18/C19/C20/C21/C41/C42/C43; TWIN §9 A-1; PROGRESS_F2B0 LOG-7,
LOG-7bis, LOG-10 discoveries; PROGRESS_Scert verdict head; claims X-O32 :1262, X-AKNO, X-LOCD :1332, X-CDKAT; findings
record-path:cert-verdict-recorder-dependence (:319); f2b0_raws rerun_locus_diagnosis.log + _colexec0.log + rerun_o32.log
:277-330; s25bis_gap29_sweep.json; s22_rejected_designs.json / s22_certlim_base.json / s20_adaptive_design.json (present);
CODE: validation/a1_ideal_march_jax.py :195-201 (constants), :424 (TRIALS), :432-473 (Newton while-loop), :795-828 (certify),
a1_toc_variational_jax.py :1536-1566 (certdiag), certdiag_kat.py :1-60, :166-170, o32_mesh_convergence.py :51-60; tests/
test_claims_lint.py :34-40, :94-101; trees V :474-504, H :433-470, O :460-489, P :550-576. LITERATURE ON DISK: Deuflhard CSM 35
(registry deuflhard_2011_csm35, READ-PARTIAL) — VERIFIED at the page for this file: PDF pp. 62-63 = book pp. 51-52 (Theta_k :=
||dx^{k+1}||/||dx^k|| (2.11); restricted monitor Theta_k <= 1/2 (2.12) "otherwise we diagnose divergence"; termination (2.14)
||dx^k||/(1 - Theta^2_{k-1}) <= XTOL, XTOL "a user prescribed error tolerance") and PDF p. 158 = book p. 148 (Algorithm NLEQ-ERR:
"Set a required error accuracy eps sufficiently above the machine precision"; convergence test ||dx^k|| <= eps; regularity test
lambda_k < lambda_min = "convergence failure") — tier [IO]. Roache/Celik/ASME rows are WANTED (registry :918-:928, no path):
nothing below rests on them (tier [APERTO], no procurement needed for this position; see §7).

## 1. PROPOSED FALSIFIER (what both sides must agree on BEFORE any run; refines SP8 §5 F-2 where it is mis-posed)

F-2 as written by the SP8 judge contains a hidden tautology that would let the incumbent win by definition: clause (b) "every
S20 GENUINE rejection is still rejected". "GENUINE" is the certdiag label of a1_toc_variational_jax.py :1540-1565, and that label
means ONE thing only: cert_worst bit-identical under N_NEWTON 30 -> 300 with the floor untouched. By the loop of record
(a1_ideal_march_jax.py :445-448: cond = it < N_NEWTON AND step > NTF*EPS*sc) a cell that exits on the METRIC before trip 30 is
cap-invariant trivially; a cell whose damped map is stationary (TRIALS :424 contains t = 0.0 — the argmin can select the
unmoved iterate every trip) is cap-invariant trivially too. X-CDKAT KAT-2 (certdiag_kat.py :25-27, :166-170) shows that HEALTHY
converged cells are bit-identical under cap 300 — the SAME signature. So "GENUINE" = "not a trip-cap artifact", never "non-
convergent"; the record itself says so in the KAT's licence clause (certdiag_kat.py :45-48: "what PASS licenses, no more").
The falsifier must therefore be posed on the OBJECT, not on the label. Proposed, for agreement:

  F-2' (threshold scale, A11 vs the roundoff certificate). On the X-LOCD design set (5 S20 rejected designs, S22 cert-limited
  base, S18 W*, X-CDKAT baseline), both recorders (A1_COLEXEC=1/0), >= 2 lowerings (eager / jit), env e100f996, record PER CELL:
  the extra step s_c (as today), the LAST TWO step norms of the while-loop above the floor (Theta_c := |dx_{k+1}|/|dx_k|), the
  selected trial index history, and the non-finite flag; and PER DESIGN the two-level difference b_J := K_RICH*|J(r=1) - J(r=2)|
  (one r=2 re-march per design). Verdict rule of the alternative (A11'): HARD-REJECT if any cell is non-finite, or shows
  Theta_c > 1/2 on its last above-floor pair (Deuflhard (2.12), [IO]), or has a t = 0 stationary history without any above-floor
  contraction; else PASS iff sum_c s_c*A_c <= c_band * b_J with c_band = 1e-2 (DECLARED; verified by the order test on J, V C.1) —
  the per-cell z-band form is a derived duty (§6 (x)). Kill/survive, pre-registered:
   * A11' is KILLED if a PLANTED non-convergent cell passes it: seeds = (k1) a corrupted-Jacobian cell (sign flip of one Jacobian
     row) whose Newton step is small but non-contracting; (k2) a corrupted-residual cell (X-STSC-class corruption) at s_c <
     c_band*b_J; (k3) a starved solver (KAT-3 pattern, cap 0). If ANY of k1-k3 passes A11', the band-relative threshold is too
     lax and A-1/A9b on the roundoff metric is the fix (SP8 §5 F-2 kill honoured, on the right object).
   * A11' is KILLED if the cross-recorder / cross-lowering binary verdict still differs for ANY design of the set under A11'
     (the flips are then NOT floor-class and the alternative's central claim — "the flip lives in the floor" — is false).
   * A11' is KILLED if fewer than all of the 5 S20 rejected designs show, at their argmax cell, s_c inside the floor class
     (s_c <= 10*NTF*EPS*sc AND an above-floor contraction pair Theta <= 1/2): then the S20 rejections are not a floor phenomenon.
   * A11' SURVIVES iff none of the three kills fires AND the one-recorder / one-lowering roundoff verdict of record is REPRODUCED
     as the reporting scale (cert_worst printed, unchanged semantics) — i.e. the alternative loses no information.
  F-1 (margin rule) is accepted AS WRITTEN, with the note that its outcome is already decided by logs of record (§2.3): the run
  fixes the numeral, it cannot change the branch. F-3 (matched-ladder band on Delta) accepted as written.
  What makes the PROGRAM change choice: A11' survives F-2' -> the binary verdict adopts the band-relative hierarchy, C18/C19 are
  re-scoped to the reporting scale (no constant retired, one role moved), A-1's margin is re-expressed on the band-relative
  metric; A11' killed -> A-1 with rho := max(K_RICH, rho_meas) stands and the design loop must be re-run until margin is met.

## 2. THE ALTERNATIVE AT ITS BEST (anchors, numbers of record, no run)

2.1 Where the flips live, measured. The recorder flips of record sit at cert_worst 1.06-2.46 (S20 set; findings :319; LOG-7bis
(b)), 2.023 vs 0.308 on the S22 base (rerun_locus_diagnosis.log :45 vs _colexec0.log :36), 4.108 vs <= 1 on rej-3 (:30 vs
_colexec0 :25), 3.757 vs 0.585 at the first instance (findings :319). Every one of these is a step of 1-4 x 100*EPS*sc, i.e.
1e-14 to 4e-14 relative. The measured floor population of record (s25bis_gap29_sweep.json: base arm cert_worst 0.7011 = worst
extra step 70.1*EPS*sc; NTF-1 kappa_eff,worst in [51.7, 70.1], M0 :3690-3697) puts the healthy floor at 0.5-0.7 of the threshold.
A cell at 1.06-2.46 is therefore 1.5-3.5x the healthy floor — inside the per-trip fluctuation band that NTF-4 itself declares
(H5, m = 0.25 "sufficient-not-optimized", M0 :3730-3745) once kappa_eff(cell) exceeds NTF. The record's OWN theory (NTF-4, scene
D) says: a cell with kappa_eff > (1+m)*NTF "fails certification" AT A TRUE ROOT. The five S20 rejections and the base flip are
the predicted behaviour of a floor-class cell under the roundoff certificate — not evidence of non-convergence.
2.2 The argmax cell is not even the same cell across recorders: per-column base at (3.9077, 0.0512) design_col 29 (:45), per-cell
base at (4.2641, 0.1429) design_col 26 (_colexec0 :36). A population of cells near the floor, the worst of which depends on
evaluation order, is the floor picture; a single non-convergent cell would stay put.
2.3 The margin route is self-defeating on the record's own numbers. A-1 requires cert_worst <= 1/K_RICH = 0.25 under the pinned
recorder. Of record: X-CDKAT baseline 0.181 (passes), S22 base 0.308 per-cell / 2.023 per-column (fails), GAP-29 record march
0.701 (fails), KAT-3 base 0.232 (passes barely). rho_meas is already bounded below by logs of record: base 2.023/0.308 = 6.6,
first instance 3.757/0.585 = 6.4, rej-3 > 4.1 — so F-1's branch is decided (rho_meas > K_RICH) and the A9b requirement on the
roundoff metric reads cert_worst <= 1/6.6 = 0.15: NO design of record passes, X-CDKAT included. Under the incumbent's own margin
logic, both TWIN arms are "at most INTERMEDIATE" by rule ([CERT-STAB] (ii)+(viii)) before they are built — the decisive number
becomes unquotable by construction. The margin fights a noise floor with a numeral; the floor is kappa_eff-shaped (NTF-1) and
recorder-shaped (findings :319), and no numeral sits reliably between 0.7 (healthy floor) and 1.06 (first flip).
2.4 The floor is irrelevant to the quoted number by ten orders. rerun_o32.log :297-315 (TOC ladder, J of record): J(r=1..4) =
2.776168785e7, 2.776068095e7, 2.776047926e7, 2.776042109e7 -> two-level differences 1.0e3, 2.0e2, 5.8e1 on J; the accumulated
certification floor printed at the same levels (o32_mesh_convergence.py :53-57, worst-case NTF*eps*N_cells*scale) = 2.83e-7,
1.09e-6, 2.41e-6, 4.25e-6. A cell certified at 2.5x the threshold moves the accumulated floor to at most 7e-7 against a
two-level difference of 1.0e3: nine to ten orders. dp_noise on the J order is 4.5e-3 against dp_model 0.67 (:314). No consumer of
the decisive delta (band 0.5% abs, TWIN §6) can see the difference between a cell at 100*EPS*sc and one at 250*EPS*sc.
2.5 The record's own source prescribes the alternative. Deuflhard CSM 35 [IO, PDF p. 158 = book p. 148]: NLEQ-ERR begins "Set a
required error accuracy eps sufficiently above the machine precision"; convergence = ||dx^k|| <= eps; convergence FAILURE is
diagnosed by the regularity test (damping below lambda_min) and the monitor Theta_k >= 1 (p. 149), divergence by Theta_k > 1/2 in
the restricted monitor ((2.12), PDF p. 63 = book p. 52). The record cites this book for NTF-2's contraction semantics (M0 :3699-
3704) and then terminates at 100*EPS — the one regime the source tells the reader to stay above. The band-relative hierarchy is
Deuflhard's own architecture: eps from the consumer (here the discretization band), non-convergence from Theta and damping, not
from the ulp scale.
2.6 Recorder independence BY CONSTRUCTION, not by margin. The recorder and the lowering change the realized per-cell floor by
O(1) factors (6.6 measured, findings :319 "ulp seed differences amplified through the damped-trial selection"). A threshold 7-9
orders above the floor cannot flip under an O(1) factor; the only decisions that remain recorder-sensitive under A11' are the
non-finite and the Theta-guard cases — exactly the ones a certificate SHOULD be sensitive to (X-O32 negative control: cert_worst
= inf, claims :1262, is rejected by A11' as by the incumbent; KAT-1 2.3e5 and KAT-3 6.1e8 likewise). Nothing the record has
ever demonstrated as a rejection of a truly non-convergent lane lives in cert_worst in (1, 10]: the KATs plant starved solvers
(cap 0-3) and non-finite steps, never a small-step non-convergent cell — the X-CDKAT row says so (KAT-1 / KAT-2 / KAT-3 text).
2.7 A9b belongs on the band-relative metric. Keep the measurement (rho_meas over the pre-registered set, re-measured at every
triple change; K_RICH the floor until measured) but apply it where a margin is affordable: quotable iff sum s_c*A_c <= c_band*
b_J/rho — with rho = 6.6 and c_band = 1e-2 the requirement is still 7 orders below the band. The widened class of the findings
row (truncation float(z[0]) > L, wall_search revision, margin-floor raise, TWIN branch) keeps clause (ii) as written: those
decisions are not roundoff-scaled and rho_meas on them is the right rule.
2.8 F-3 rides for free. The X-O32 ladder already shows the two-level differences on J contracting 1.0e3 -> 2.0e2 -> 5.8e1 with
the same march; on matched ladders the difference of two arms shares the mesh law and the tables — H :455-457 and O V.2 give the
cancellation argument; F-3 measures it on the S24 F1b pair. No theory claim from me beyond "measure it".
2.9 Cost. Instrumentation: the while-loop carry (a1_ideal_march_jax.py :471-472) gains one element (previous step) and the
selected trial index — no extra residual or Jacobian evaluation; certify() (:795-828) prints s_c and Theta_c beside the ratio.
F-2' data: 8 designs x 2 recorders x 2 lowerings at r=1 plus 8 r=2 re-marches: at the O32 scale (r=1 rec 3.3 s, r=2 rec 16.5 s,
:297-:301) and the S22 class re-record scale (locus run of record: minutes) this is well under the 892 s X-AKNO cycle the item
names as the unit; the whole of F-2' fits the F2.ENGINE first act beside the X-O32 / X-LOCD re-forms and REUSES their runs
(the refuter's PM hat is answered: same design set, same recorders, one added print per cell).

## 3. GENERALITY

The hierarchy is engine-agnostic: any certified Newton lane (per-cell march, wave-frame BVP, H20 plume solve, the F3.PLUG C-
family mirror) carries a consumer band, a contraction history and a floor; the roundoff-relative certificate is the one that
does NOT generalize — its NTF is instance-measured (kappa_eff population of ONE march, M0 :3690) and env-blind (SP8 A9e, [CERT-
STAB] (vii)), so every new engine re-opens F2-NTF-FLOOR-POPULATION before it can certify anything. The band-relative rule
inherits its scale from the estimator campaign (C11/C43 interim regime) that the program must run anyway.

## 4. HOW THIS CHANGES THE CREDIBILITY OR THE COST OF ANSWERING Q0

Credibility: the referee's first question on VI.6 will be "your certificate decides at 1e-14 relative, flips with the thread
order, and your band is 1e-5 relative — why is the certificate the verdict?" A11' answers it with the source the record already
cites; A-1 answers it with a ninth K_RICH role (C42) and a margin that the record's own designs do not meet.
Cost: under A-1 + rho_meas every arm of record is non-quotable (§2.3) -> the TWIN closes INTERMEDIATE or the design loop is re-run
until a margin that the floor forbids; under A11' the arms of record are quotable today on the binary verdict, and the F2.ENGINE
first act spends ~0.25 session on instrumentation instead of a re-design campaign. This is a change in the COST of Q0's answer,
not a change of road.

## 5. CONCESSIONS (stated before the refuter asks)

(c1) c_band = 1e-2 is DECLARED, not derived: V's "verified by the order test" is a procedure, not a proof; until the order test on J
is run with cells deliberately certified at c_band*b_J and shows the Richardson estimate unmoved, the factor is single-author in
my own text. (c2) The per-cell band in z-units needs a definition (the r=1/r=2 field difference at the cell, through the march
topology — LB-c2 says refinement cannot hold the topology fixed, claims :1262); the F-2' instrument is therefore the J-level
accumulation, and the per-cell form is a derived duty. (c3) The Theta guard is not evaluable at a floor-stationary cell; it uses
the last above-floor pair; a cell that starts at the floor (replay seeds, C2-F2 seam) has no such pair and inherits the replay's
certificate — a declared gap, seeded as k3. (c4) rho_meas from a 6-8 design set is a lower bound of record, not a requirement
numeral — I agree with the refuter's hat (1) on that and it is WHY the margin is moved off the roundoff metric. (c5) A11' does not
rescue X-O32's negative control and must not. (c6) NO RUN here: every number above is a log of record; F-2' is the run.
(c7) I do not claim the S20 rejections ARE floor-class; I claim the record cannot distinguish (§1) and that A11' makes the
distinction measurable (Theta history + trial history) — the third kill of §1 is where I lose if they are not.

## 6. [CERT-STAB] — emendations to the SP8 §6 text (M0-ready; class PRACTICE measured, THEOREM* target for (ii) under H-rho)

(ii) MARGIN ON EVERY DECISION — unchanged for the non-roundoff class; for the per-cell certificate the decision object is the
BAND-RELATIVE metric of (x), and rho applies to it.
(x) CERTIFICATION THRESHOLD SCALE (new). A Newton lane is CERTIFIED iff (a) every step is finite, (b) its last above-floor pair
contracts, Theta <= 1/2 (Deuflhard (2.12), [IO]), (c) the accumulated extra step over the certified cells is <= c_band * b_site / rho,
b_site = the site's two-level Richardson band (K_RICH-safeguarded, C41 P-tag), c_band DECLARED = 1e-2 until the order-test
derivation lands; the roundoff ratio cert_worst is PRINTED as the reporting scale (C18/C19 keep their constants, role moved to
reporting + F2-NTF-FLOOR-POPULATION input). A lane whose (b) cannot be evaluated inherits the certificate of its seed's record and
prints "guard-vacuous". Seeded rejectors: k1/k2/k3 of §1 refused; a planted step at 0.5*b_site refused; doctored envfp / tree
hash refused; a Verdict without recorder + lowering key refused.
(vi) unchanged; a reproduced outcome class with a flipped BAND-RELATIVE verdict is a FAIL of (x) — the requirement's own
falsifier, owner F2.ENGINE.

## 7. [KNOWLEDGE] / procurement

Deuflhard CSM 35 pp. 51-52, 148-149: [IO] verified on disk for this file (pages named above). Yamamoto 1986 eq. (7): [REP] via
registry :1083 (not used load-bearing here). Roache/Celik/ASME: [APERTO], WANTED rows :918-:928 — NOT load-bearing for this
position (c_band is declared, not sourced); procurement remains the C11 estimator-campaign rider's. Higham (rounding-error
floor model) and More-Wild (noise floor): no registry rows; not cited, nothing rests on them.

## 8. Answers to the item's three questions

Q-a (is A-1 a sufficient margin?): NO — the record's own logs bound rho_meas >= 6.6 > K_RICH (F-1 decided), and no numeral on
the roundoff metric separates the healthy floor (0.70) from the first flip (1.06). Q-b (band-relative threshold?): YES, in the
hierarchy A11' of §1/§6 — provided F-2' is run on the OBJECT (planted non-convergent cells), not on the certdiag LABEL. Q-c
(matched-ladder band on Delta?): measure it (F-3), the X-O32 ladder makes it cheap. Protocol: §1 F-2' + SP8 §7 design set,
recorders, lowerings, seeds; owner F2.ENGINE first act; NO RUN in this session.
