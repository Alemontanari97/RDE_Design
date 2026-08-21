# ESCALATION REFUTATION — R22F ROUND-4 DELTA, LENS L2 (asymptotics /
# measure-scaling) — E-5, S-FOUNDATIONS-C4 escalation window, 2026-08-20

ROLE + SCOPE OF RECORD: E-5 TARGETED REFUTER, ONE round, restricted to
the centerpiece round-4 delta per RES-CAP-1 (VERDICT_r22f §§4-5): the
[REV2-r4-1] mu functional-identity + H-G6/L_H structure, [REV2-r4-2]
instance-checked-convexity narrowing, [REV2-r4-3] eps_U sweep-sup
licensing, [REV2-r4-5] (vi)-row cell edits, and the §13 table edits.
Out-of-scope observations filed as NOTE only. Guidance labels
NON-ADOPTED; classifications here are my own adjudication at this lens.

READ-DEPTH DECLARATIONS (this window):
- phaseD_r22f_centerpiece.md: [TARGETED-FULL at the delta] — all
  [REV2-r4-*] marker sites grep-located and read with their host
  sections in full (§2.2-bis :540-956 incl. conditions (1)-(3), forms
  (T)/(C), (A)-(F), [REV2-r3-1/2/3], [REV2-r4-1/2/3]; the Part 5 (vi)
  row :1475-1546 incl. [REV2-r4-5](a)-(f) and [REV2-r3-6]; residues
  block :1770-1834 incl. [REV2-r4-4]; landing notes :1844-1928 incl.
  [REV2-r4-6]; §13 :2114-2175; [REV2-r4-0] header :58-80).
- VERDICT_r22f.md §§1 (header + labels intro), 4, 5 [FULL at those
  sections] (:1-57, :227-339).
- phaseD_r22f_refute_r4_l0.md [FULL at findings] (:94-405: L0-19,
  L0-20, L0-21, L0-22, machine summary).
- phaseD_r22f_refute_r4_l2.md [FULL at findings] (:1-100 header/L2-24
  region via grep + :99-278: L2-25, L2-26, L2-27, machine summary
  :303-304).
- phaseD_r22f_refute_r4_l1.md [SLICE via grep]: finding IDs + machine
  summary lines only (:13-14, :113-135, :209-222) — L1 was DRY, its
  NOTES are not in my scope except for §13-table row accounting.
- Probe terminal lines verified on disk: r22f_v2_probe_r4_l0_mu_
  identity_proxreg.py (:141, :237, :243 "ALL ASSERTS PASS"),
  r22f_v2_probe_r4_l2_proxreg_annulus.py (:206 "ALL ASSERTS PASS
  (parts A-G)"). Not re-run (none of my findings turns on re-running
  them).
- New probe THIS window (RUN, ALL ASSERTS PASS):
  esc_probe_r4delta_hg6_pointfloor.py (feeds E5-L2-2).
- No paper read this window (no finding needs one). PAPERS NEEDED:
  NONE.

HAND-VERIFICATION LEDGER (positive record, done before attacking):
(i) [REV2-r4-1](d) value-route J_red-side chain re-derived by hand:
x1 = argmax J_red, x2 = argmax J_true, segment feasible (H-G5),
mu_red floor on segment: J_red(x1) − J_red(x2) ≥ (mu_red/2)·shift²;
|J_true − J_red| ≤ eps_U on the basin gives J_true(x2) − J_true(x1) ≤
2·eps_U − (mu_red/2)·shift²; x2 optimal gives ≥ 0; hence shift ≤
2·sqrt(eps_U/mu_red). EXACT as printed. (ii) H-G6's Weyl-type
direction checked at cone level: for any cone K and unit d in K,
<d, (−H_true)d> ≥ <d, (−H_red)d> − ||H_true − H_red||_M ==> cone-floor
transfer is the right SHAPE (the defect is the point-vs-ball
instantiation, E5-L2-2, not the operator inequality). (iii)
Tietze–Nakajima usage checked: closed + connected + locally convex ⇒
convex in R^n — hypotheses correctly stated in the [REV2-r4-2](a)
replacement text. (iv) [REV2-r4-5](a)-(f): each superseded fragment
diffed against the printed (vi) row — all six replacements present and
faithful to their descriptions; nothing silently deleted. (v) §13
joint-resolution containment claim checked against both fix shapes:
[REV2-r4-3]'s clause contains L0-21's sustained-under-refinement
license verbatim-class AND adopts L2-26's strictly stronger
never-discharges rule — the containment claim is TRUE. (vi) The
annulus probe's violation scaling re-derived: shift Theta(1), bound
2·sqrt(6·eps/mu) ⇒ ratio Theta(eps^{-1/2}) — the printed 40.8x →
4082.5x ladder matches exactly.

==============================================================================
# FINDINGS

### E5-L2-1 — REPAIR (§13 table edits): the round-4 disposition table
### omits the R22F-L2-24 NOTE row while its own COUNTS line says
### "NOTES 5" — the table prints 4 NOTE rows

ANCHORS: §13 table :2142-2152 — rows L0-19, L0-20, L0-21, L0-22,
L1-16, L1-17, L2-25, L2-26, L2-27 (NOTE rows present: L0-22, L1-16,
L1-17, L2-27 = FOUR); COUNTS line :2156 "NOTES 5 (no action owed)";
the L2 round-4 file's machine summary :303-304 "NOTES: 2 (L2-24,
L2-27)"; R22F-L2-24 itself at r4_l2 :59 ("NOTE (resolution ledger;
each disposition verified at ...)").
MEASURED THIS WINDOW: grep -o "R22F-L[012]-[0-9]*" over §13's row
block returns no L2-24; grep over phaseD_r22f_refute_r4_l2.md returns
L2-24 as a filed NOTE.
DEFECT: the count "5" is CORRECT (L0-22 + L1-16 + L1-17 + L2-24 +
L2-27) and the table is INCOMPLETE — an internal arithmetic
inconsistency in new round-4 text, and a violation of the file's own
declared inclusion rule: courtesy NOTE rows are retained in
disposition tables, a rule re-established by the loop itself when the
same omission class (the L2-12 NOTE row missing from §11) was found
and repaired ([REV2-r3-8]; r4_l2 :82 "adds the omitted L2-12 NOTE row,
and declares the inclusion rule (courtesy NOTE rows retained)"). A
reader cross-checking §13's counts against its rows fails; the
verdict's §2.1 "no refuter finding absent" duty leans on these tables.
WHY REPAIR (not BREAK, not AMENDMENT): mechanical completeness defect
in a table of record with a live internal contradiction (5 vs 4) —
same class as the repaired L2-12 omission; no theory content is wrong.
FIX SHAPE (append-only, one marker): add the row
"| R22F-L2-24 | NOTE | no action (resolution ledger; each round-3
disposition verified at its edited site) | — |" via an [ESC-*] marker
quoting this finding; no count change needed (the COUNTS line is
already right).

### E5-L2-2 — AMENDMENT ([REV2-r4-1](b), H-G6): the transfer
### inequality composes a POINT-measured mu_meas with a ball-sup L_H
### and omits the (E)-sustainment premise (and its band edge) — false
### as a freestanding hypothesis line even with L_H = 0 exactly

ANCHORS: H-G6 line :839-845 ("mu_true_floor ≥ mu_meas − L_H, with
L_H := the sup over the certified ball of the design-Hessian residual
norm ||H_true − H_red||_M"); condition (1) :607-609 ("The segmented
TR-Newton curvature of record is POINT-measured"); the (E) ladder
:700-707 ("radius = the largest ball on which the measured floor
sustains its value within its own band"); the (vi) BEST cell :1482
("mu_eff = mu_meas − L_H").
DEFECT (measure-scaling): L_H prices the J_red→J_true curvature gap
UNIFORMLY on the ball, but mu_meas is a POINT value of J_red's
curvature at S*_red — the inequality silently prices J_red's OWN
intra-ball curvature decay at zero. With H_true ≡ H_red (L_H = 0
exactly, in every metric) and a J_red whose curvature decays off the
sustained region, mu_true_floor on the explored ball is MU_OUT while
mu_meas − L_H = MU_IN: the printed inequality is FALSE and the
composed bound delta/(mu_meas − L_H) is violated 17.5x, unbounded
along the MU_OUT → 0 ladder (same divergence shape as the r4_l0 A7
ladder). EXECUTABLE WITNESS (probe esc_probe_r4delta_hg6_pointfloor.py,
RUN this window, ALL ASSERTS PASS; synthetic 1-D, CT-6 clean, stdlib
only): PART A1 (freestanding inequality false, 0.01 vs 1.0 with
L_H = 0), A2 (violation 17.5x), A3 (the SCHEMA object with the TRUE
J_TRUE floor stays sound — the [REV2-r4-1](a) identity is NOT the
defect), B1 (the composed chain refuses: condition (1)'s a-posteriori
check 0.6 ≤ r_cert 0.5 FAILS via the (E)-certified radius), B2 (the
sustained-floor reading restores the transfer, bound tight).
WHY AMENDMENT (not BREAK/REPAIR): the full printed chain issues no
false certificate today — the gradient route licenses NO number until
L_H lands ([REV2-r4-1](c)), and when it does, condition (1)'s
(E)-radius check blocks the counter-model (probe PART B1). The defect
is ONE missing premise clause in landing-facing hypothesis text (the
same dormant-route class as L0-21/L2-26), plus the unpriced band-edge
term: the (E) ladder certifies sustainment only "within its own band",
so the licensed floor at the edge is mu_meas − b_E, not mu_meas.
CROSS-ORIGIN DECLARED (zero inflation both ways): the H-G6 wording is
verbatim from the L0 round-4 fix shape (b) (r4_l0 :204-217), adopted
faithfully by the reviser — a new defect in new text; the r4_l0 probe
could not catch it (its PART A uses CONSTANT Hessians, so point = ball
floor by construction and any (E) certificate passes).
FIX SHAPE (one clause at H-G6, read into the (vi) BEST cell's mu_eff
parenthesis; AG-1 valve, sufficient-not-optimized): "H-G6 is read on
the (E)-certified ball with mu_meas = the SUSTAINED ball floor of the
measured carrier at its band-lower edge (the (E)/R-12 ladder object,
mu_meas − b_E) — never the bare point measurement; mu_eff =
(mu_meas − b_E) − L_H." Probe PART B2 witnesses that this reading
restores exactness.

### E5-L2-3 — AMENDMENT ([REV2-r4-1](b), H-G6 tail): "by the adjoint
### representation it decomposes along the same (J)/(H) channels at
### second order" is flat-asserted; the second-order residual
### generically carries CROSS-channel bilinear terms

ANCHORS: H-G6 line :843-845 ("the SECOND-ORDER face of the SAME
reduction residual operator; by the adjoint representation it
decomposes along the same (J)/(H) channels at second order"); the
deriver list :846-853 (leg (1) = X-T3QS-5F content bound at Hessian
level "mirror of R-9").
DEFECT (structure/bookkeeping at second order): differentiating the
first-order adjoint gap representation twice in the design produces,
besides the second-order faces of the (J) and (H) channels, terms
BILINEAR in first-order quantities (first-order channel residuals
paired with first-order sensitivity/adjoint gaps). A deriver that
mirrors the first-order channel split without the cross blocks —
which is what "decomposes along the SAME channels" invites, and what
leg (1)'s "mirror of R-9" phrasing suggests — would systematically
UNDERCOUNT L_H, and an undercounted L_H enters mu_eff = mu_meas − L_H
in the unsafe direction (overstates the floor, understates the shift
bound). The claim is underived (the whole line is SCHEMA-status) yet
stated as fact.
WHY AMENDMENT: no number rests on the sentence today (L_H underived,
route dormant); the defect is one structural overstatement in
deriver-steering text. CROSS-ORIGIN DECLARED: wording verbatim from
the L0 round-4 fix shape (b) (r4_l0 :208-210), adopted faithfully —
new defect in new text.
FIX SHAPE (one wording touch): "... decomposes along the same (J)/(H)
channels at second order PLUS cross-channel blocks bilinear in the
first-order residuals (not excluded; each L_H deriver must price them
or prove them absent)."

### E5-L2-4 — AMENDMENT ([REV2-r4-2](a) replacement text): the
### parenthesis "(equivalently: the segment between S*_red and every
### point of the shift ball feasible)" is NOT an equivalence — it is
### star-shapedness about S*_red, strictly weaker than convexity

ANCHORS: H-G5 line of record :738-741 and its verbatim duplicate in
the [REV2-r4-2](a) block :901-905 ("C ∩ certified ball CONVEX
(equivalently: the segment between S*_red and every point of the
shift ball feasible)").
DEFECT: convexity of C ∩ ball implies the quoted segment property;
the converse is FALSE — a set star-shaped about S*_red (e.g. a
Pac-Man/star domain with S*_red at the kernel) satisfies "segment
between S*_red and every point of the shift ball feasible" while
C ∩ ball is nonconvex. So "equivalently" is a false mathematical
claim in the round-4 licensing sentence of record. DIRECTION IS
BENIGN, stated honestly: the segment property (star-shapedness
covering the shift ball) is exactly what the VI/strong-concavity
chains consume (segments from S*_red to the candidate argmax; the
directional first-order conditions at both endpoints run along that
segment), so an executor who checks the weaker form and licenses is
NOT unsound — the mislabel cannot issue a false certificate, it can
only misname the checked property. But the same word "equivalently"
also invites the reverse substitution (checking convexity and quoting
it as "the same as" the segment property is fine; quoting the segment
property as delivering CONVEXITY, e.g. to feed the Tietze–Nakajima
clause or a future consumer that genuinely needs convexity, is not).
WHY AMENDMENT: one-word-class wording defect in new licensing text;
no unsoundness reachable today.
FIX SHAPE: replace "(equivalently: ...)" with "(sufficient, and the
property the arguments consume: the segment between S*_red and every
point of the shift ball feasible — star-shapedness about S*_red;
convexity implies it, not conversely)" at both printings (:738-741
and the (a)-block quotation context).

### E5-L2-5 — AMENDMENT ([REV2-r4-3] completeness): the SAMPLED-SUP
### class label has NO at-site pointer at its two §2.2-bis consumption
### sites — the withdrawn measured⇒discharged implication survives
### unflagged exactly where it is printed

ANCHORS: (F)'s premise list :713 ("measured instantiation per
[REV2-r3-3] — the sweep-sup of the M-RED value legs (A)-(B) along the
design sweep, NEVER a single-family point eps") — no [REV2-r4-3]
pointer; [REV2-r3-3](b) :802-809 ("until the sweep sup is measured,
the uniformity premise is OPEN and DECLARED") — the exact sentence
whose invited implication [REV2-r4-3] :951-956 WITHDRAWS, carrying no
at-site read-under flag. CONTRAST, same round: [REV2-r4-1] inserted
FOUR at-site pointers (condition (1) :605-606, form (T) :639, form
(C) :647, (F) :716-717) precisely so no curvature sentence could be
read without its round-4 scoping; and the file already owns the
needed phrase — R-14's decider sentence :1802 reads "([REV2-r3-3] at
[REV2-r4-3] class)".
DEFECT: §2.2-bis is the L-2 landing source ("AS FURTHER AMENDED"
lands by instruction [REV2-r4-6](a), so no false landing is FORCED),
but the in-file reading rule is violated: a reader (or extraction
agent) consuming (F) or [REV2-r3-3](b) at-site — the normal grep
path — gets the round-3 sweep-sup form WITHOUT the estimate-class
label and WITH the withdrawn discharge implication. Round 4's own
protocol (at-site pointers for every re-scoped curvature sentence)
is applied asymmetrically to [REV2-r4-1] but not [REV2-r4-3].
WHY AMENDMENT: pointer-completeness defect; content of record is
correct and the landing instruction carries it.
FIX SHAPE (two bracket insertions, append-only style of the r4-1
pointers): at :713 "per [REV2-r3-3] [at [REV2-r4-3] SAMPLED-SUP
(estimate) class]"; at the end of [REV2-r3-3](b)'s discharge sentence
"[READ UNDER [REV2-r4-3]: measurement instantiates at declared class,
never discharges]".

### E5-L2-6 — NOTE (out-of-adjudication confirmation of J-1 /
### RES-CAP-6): the §2.3 header clobber is independently confirmed;
### the specified landing repair is sufficient

MEASURED THIS WINDOW: grep '^## 2.3' phaseD_r22f_centerpiece.md
returns 0 matches; at :956 the [REV2-r4-3] block's final sentence
("... with the estimate-class instantiation available for a-posteriori
checks that declare it).") runs directly into "Harroun 2021 Fig. 18,
printed p. 669". The r4-3 sentence is grammatically COMPLETE, and the
exhibit paragraph from "Harroun 2021 Fig. 18" onward matches the
judge's description of intact content — consistent with exactly two
fragments lost (the "## 2.3 ..." header line and the lead-in "PHYSICAL
EXHIBIT OF RECORD (page-verified this window):"), i.e. the [REV2-J1]
repair text specified at VERDICT §4 RES-CAP-6 restores everything
lost. No additional clobber found at any other r4 insertion site
(each [REV2-r4-*] block begins and ends at clean sentence boundaries
— checked at :817, :876, :927, :1500, :1810, :1907, :2115). No new
action.

### E5-L2-7 — NOTE (positive verification, [REV2-r4-1](d)): the
### value-route J_red-side derivation is EXACT as printed; its
### localization premise is carried at premise level

The one-line chain re-derived by hand (ledger item (i) above) is
correct, including constants. One reading obligation, already
premise-carried: the chain compares J_true at the two argmaxes, so it
presupposes the TRUE argmax lies in the region where the eps_U
uniformity premise and the mu_red floor hold — that is exactly (F)'s
own premise wording ("on the certified basin ... the basin the shift
explores") plus the cell's radius check with "reduced argmax inside
the basin". Nothing outside the basin is claimed excluded by these
premises alone; the text nowhere claims otherwise. No action owed;
recorded so the delta's soundest piece is positively attested rather
than silently passed.

### E5-L2-8 — NOTE ([REV2-r4-3] residual asymmetry, covered in
### substance): a check-PASS computed with a sampled-lower eps_U is
### itself estimate-class

The a-posteriori check "2·sqrt(eps_U/mu) ≤ certified basin radius"
is monotone in eps_U, so an under-estimated eps_U can PASS the check
where the true-sup check would FAIL (the part-G probe exhibits the
extreme: sampled bound 0, check trivially passes). The [REV2-r4-3]
clause covers this in substance — the instantiation carries
SAMPLED-SUP (estimate) class, sub-sample-width structure is declared
un-excluded, and checks must "declare it" — so the pass inherits the
class label by the printed rule. Optional one-clause sharpening for
the landing editor (not owed): "a check-pass at estimate class is
itself estimate-class (defeasible under sweep refinement)."

### E5-L2-9 — NOTE (verified-green ledger for the rest of the delta;
### zero credit inflation)

(a) [REV2-r4-2](a): prox-regular withdrawal is a STRICT narrowing;
Tietze–Nakajima hypotheses correctly stated; the F2 refinement clause
(mu_eff = mu − |lambda*|·kappa_max, kappa_max = 1/r_prox) is
correctly SCHEMA-labeled and never licenses — matches both refuters'
fix shapes (r4_l0 :306-323 option "withdraw + named F2 refinement";
r4_l2 :188-209 shapes (a)-(d) all present at their sites).
(b) [REV2-r4-2](d): the connected-nonconvex no-coverage tail :769-775
is consistent with the 2·eps_U dominance constant being EXACT only in
the branch-decomposable case (r4_l2 L2-27(a) re-derivation cited
correctly at :772).
(c) [REV2-r4-5](a)-(f): all six cell edits faithful (ledger item
(iv)); the WORST-cell headline "NO argmax-shift number exists at any
grade, and none from the measured carrier alone" is CONSISTENT with
the BEST cell's measured-carrier-sound value route: that route still
needs the eps_U sweep-sup, which is unmeasured (R-15 pending), so no
number exists today from any route — "alone" is doing correct work.
(d) [REV2-r4-3] joint-adjudication: the stronger-form containment
claim verified TRUE against both fix shapes (ledger item (v)).
(e) §13 header claims checked: "4 at-site functional-identity
pointers" = condition (1), (T), (C), (F) — count correct; "6 (vi)-row
cell edits" = (a)-(f) — correct; CONTESTED-BY-ADDENDUM-B = 0 —
consistent with both refuter files' right-sizing compliance blocks.
(f) The r4 probes' terminal ALL-ASSERTS-PASS lines verified on disk;
the annulus eps^{-1/2} violation scaling re-derived by hand (ledger
item (vi)).
(g) [REV2-r4-0]'s "L1 round 4 = DRY (0 findings; its two NOTES ...)"
uses "findings" loosely (the L1 file's own machine summary says
"findings: 2", both NOTES); the DRY claim itself is correct under the
brief's criterion (zero BREAKs/REPAIRs). Cosmetic; no action.

==============================================================================
# OVERALL ADJUDICATION OF THE DELTA (this lens)

The round-4 delta is SOUND IN SUBSTANCE and its fixes stand: the
functional-identity repair, the H-G6 structure, the convexity-only
narrowing, and the sampled-sup class label are each the right shape,
faithful to the refuters' prescriptions, and internally consistent
with the rest of the file at every site I checked. No BREAK. The loop
precedent (rounds 3-4 each finding defects in refuter-prescribed
text) recurs here in miniature: E5-L2-2/-3 are new defects in text
verbatim from the L0 round-4 fix shape, both AMENDMENT-class because
the gradient route is dormant until L_H lands and the composed check
chain blocks the exploit today. One mechanical REPAIR (§13 missing
L2-24 row). The "round-4 delta unrefereed" line owed at the two
landing items (VERDICT RES-CAP-1) is DISCHARGED by this pass at this
lens once the sibling-lens passes land, per the escalation form.

## MACHINE SUMMARY (E-5, lens L2, one round)

breaks = 0
repairs = 1 (E5-L2-1)
amendments = 4 (E5-L2-2, E5-L2-3, E5-L2-4, E5-L2-5)
notes = 4 (E5-L2-6, E5-L2-7, E5-L2-8, E5-L2-9)
probes_run_this_window = 1 (esc_probe_r4delta_hg6_pointfloor.py —
  ALL ASSERTS PASS)
papers_needed = NONE
