# RES-CAP-1 TARGETED REFUTATION — ROUND-4 DELTA, LENS L0
# (variational/optimization; ONE round, scope RESTRICTED to the
# [REV2-r4-*] delta held out by VERDICT_r22f §4/RES-CAP-1)

Session: S-FOUNDATIONS-C4 escalation window, 2026-08-20. Role: E-5
TARGETED REFUTER (VERDICT_blocco2.md §7 E-5, carried by reference from
VERDICT_r22f RES-CAP-1). Numbering: E5-L0-<n> (fresh series — this is
the held-out escalation pass, not round 5 of the loop; the loop's
R22F-L0 series ended at L0-22).

SCOPE OF ATTACK (exactly the unrefereed round-4 delta): [REV2-r4-1]
(mu functional identity + H-G6/L_H), [REV2-r4-2] (instance-checked
convexity narrowing), [REV2-r4-3] (eps_U sweep-sup licensing),
[REV2-r4-5] ((vi)-row cell edits), the §13 disposition table, plus the
[REV2-r4-4]/[REV2-r4-6] carrier blocks they cite. Out-of-scope
observations filed as NOTE only.

READ-DEPTH DECLARATIONS (this window):
- VERDICT_blocco2.md: §§0-1 + §2 preamble + E-5 mandate lines (:60-98,
  :222, :259) [SLICE].
- VERDICT_r22f.md: §1 [FULL], §4 [FULL], §5 [FULL], §2.1-2.3 [FULL],
  §3 [FULL] (the mandated sections plus the finding index needed for
  the §13 check).
- phaseD_r22f_centerpiece.md: all [REV2-r4-*] marker sites grep-located
  and read IN CONTEXT [SLICES :58-70, :590-964, :965-1060 (J-1 splice
  region + §2.3 content sweep), :1482 ((vi) row, full), :1495-1554
  ([REV2-r4-5]/[REV2-r3-6]), :1785-1842 (R-13..R-17 residue region),
  :1900-1935 ([REV2-r4-6]), :2055-2110 (§11 tail/§12), :2114-2175
  (§13, full)]. Targeted greps of record this window (SR-12):
  `grep -n "REV2-r4" | "L2-24" | "prox-regular" | "mu_eff" |
  "delta/mu" | "sweep sup is measured" | "## 2.3"` — anchors cited
  per finding.
- phaseD_r22f_refute_r4_l0.md [FULL] (413), phaseD_r22f_refute_r4_l2.md
  [FULL] (318), phaseD_r22f_refute_r4_l1.md [TAIL :140-223 — L1-17
  sweep + machine summary; DRY lens, no fix of mine touches it].
- Probes: r22f_v2_probe_r4_l0_mu_identity_proxreg.py and
  r22f_v2_probe_r4_l2_proxreg_annulus.py RE-RUN this window — BOTH
  terminate ALL-ASSERTS-PASS (independent re-verification; the loop
  record had them run only in the refuters' windows).
- git: single centerpiece commit 904f950 (2175 lines = closure state;
  working tree clean for the file) — no rev-3 snapshot exists, so the
  J-1 splice-extent check below is content-census-based, declared.
- Aux carriers [ADV]: none needed; no nozzle-paper number consumed
  anywhere below (CT-6 clean).

EXECUTABLE PROBE (standing preference honored): validation/
sfoundations_raws_2026-08-13/phaseD/esc_probe_r4delta_hg5_equivalence.py
— WRITTEN and RUN this window, ALL ASSERTS PASS (feeds E5-L0-1);
synthetic 2-D counter-models only, tolerances derived from grid
resolution, pinned-env numpy only.

==============================================================================
## VERDICT IN ONE LINE

The round-4 delta is SOUND AT CONTENT LEVEL — no BREAK, no REPAIR: the
H-G6 transfer inequality, the J_red-side value-route derivation, the
convexity-only narrowing, the sampled-sup licensing clause, and the
(vi)-row cell carriage all survive attack (several re-derived by hand
and probe-checked below). Four AMENDMENT-class defects of wording /
carriage / bookkeeping in the delta text are filed, each with a
one-to-two-line fix; none licenses anything unsound and none blocks
the M0 landing of §2.2-bis and the (vi) row — they should ride the
same landing edit that executes J-1.

==============================================================================
## FINDINGS

### E5-L0-1 — AMENDMENT (probe RUN): the [REV2-r4-2](a) parenthetical
### "(equivalently: the segment between S*_red and every point of the
### shift ball feasible)" is NOT an equivalence — it is a strictly
### weaker sufficient condition under its executable reading, and
### vacuous-at-boundary under its literal reading

ANCHORS: H-G5 line of record :738-741 ("CONVEX (equivalently: the
segment between S*_red and every point of the shift ball feasible;
locally convex admissible via Tietze–Nakajima)"); the [REV2-r4-2](a)
replacement text :901-905 (same parenthetical, slightly different
nesting of the Tietze–Nakajima clause — the two printings of the same
line differ cosmetically, noted).

DEFECT: convexity of C ∩ certified-ball and the segment condition are
not equivalent in ANY reading:
- Reading A (executable: segments to every FEASIBLE point of the shift
  ball = star-shapedness about S*_red): strictly WEAKER than convexity.
  Probe DIRECTION 1 (esc_probe_r4delta_hg5_equivalence.py, RUN):
  radial-graph star domain R(theta) = 1 + 0.4·cos(3·theta), interior
  S*_red — convexity check FAILS (witness midpoint infeasible), reading
  A HOLDS, and BOTH licensed bounds hold (form (T) tight: shift 0.4932
  vs bound 0.4950; value route holds) — the two sides of "equivalently"
  return DIFFERENT license verdicts on the same instance.
- Reading B (literal: EVERY point of the shift ball, feasible or not):
  fails at every margin-active boundary S* even when C ∩ ball is
  CONVEX (probe DIRECTION 2: half-disk, convexity HOLDS, literal
  reading FAILS) — the exact vacuity-at-boundary pattern R22F-L2-25
  itself criticized in the round-3 line's reading dichotomy.
WHY AMENDMENT, NOT BREAK/REPAIR (zero inflation): reading A is
genuinely SUFFICIENT for both licensed routes — I re-derived the
form-(T) VI chain under star-shapedness alone this window (VI at x1
along x2−x1 and at x2 along x1−x2 both consume only the ONE segment
[S*_red, x2], which star-shapedness about S*_red supplies for any x2
in the shift ball; the value route consumes the same segment) — so no
reading creates a false license; reading B only over-refuses
(conservative). A wording defect in unrefereed round-4 text, third
instance of the loop's refuter-prescribed-text pattern: the
parenthetical compresses the refuters' own fix-shape language (r4_l0
L0-20 fix (a) / r4_l2 L2-25 fix (a): "segment feasibility is the
consumed property; ... the only a-priori-checkable sufficient form is
convexity") into a false "equivalently".
FIX SHAPE (one wording touch at both printings, :738-741 and
:901-905): replace "(equivalently:" with "(the consumed property — a
weaker sufficient form:" or the refuters' verbatim clause; optionally
harmonize the two printings' parenthesis nesting in the same touch.
The (vi) cell needs NO edit ([REV2-r4-5](b) already carries
convexity-only with no parenthetical gloss).

### E5-L0-2 — AMENDMENT: round-4 symbol collision — "mu_eff" is given
### TWO distinct definitions by the same pass, in a file whose own
### precedent treats symbol collision as a landing defect

ANCHORS: mu_eff = mu_meas − L_H (H-G6 transfer): :857 ([REV2-r4-1](c))
and the (vi) BEST cell :1482; mu_eff = mu − |lambda*|·kappa_max
(prox-regular curvature-corrected F2 refinement): :908
([REV2-r4-2](a)) and :1832 (R-17). All four sites are round-4 text;
both objects land ([REV2-r4-6](a) carries §2.2-bis as amended; (c)
sends R-16/R-17 to the residue list).
DEFECT: two different corrections to the curvature floor share one
symbol with no cross-reference and no composition rule. An executor at
a margin-active S* on a prox-regular set with a measured carrier —
exactly the scenario R-14+R-17 name — meets both "mu_eff" lines at
once; whether the corrections compose (mu_meas − L_H − |lambda*|·
kappa_max) or the R-17 "mu" is already the transferred floor is
nowhere stated (R-17's own "mu" is ambient-ambiguous: J_TRUE floor or
measured carrier). The file's own precedent (R22F-L0-14(b), the
mu → mu_curv landing rename for the S20 multiplier collision;
VERDICT_r22f §2.2 CARRIED) sets this class at AMENDMENT with a landing
rename duty.
WHY AMENDMENT: both formulas are individually sound at their declared
SCHEMA class; nothing false is asserted — the defect is symbol hygiene
in landing-facing text.
FIX SHAPE (rename + one sentence): rename R-17's object (e.g.
mu_prox, or mu_eff^kappa) at :908 and :1832, and add one sentence at
R-17: "its 'mu' is the H-G6-transferred floor where the carrier is
measured (the two corrections compose additively at SCHEMA class:
mu_meas − L_H − |lambda*|·kappa_max); underived until both legs land."
NOTE LIMB (no action beyond the existing landing duty): the two
ROUTES' mu (gradient route = J_TRUE floor, value route = measured
J_red floor) also share the bare symbol "mu" inside the single (vi)
cell — but both cell sites carry their inline identity flags
([REV2-r4-1](a) and (d)), so this is covered by the mu_curv rename
discipline at landing rather than a new edit; flagged for the landing
editor to keep the two subscripts distinct there.

### E5-L0-3 — AMENDMENT: at-site carriage of the round-4 delta is
### incomplete at three sites — the file's own never-silent read-under
### protocol is applied asymmetrically

ANCHORS + LIMBS:
(a) [REV2-r4-1](a) claims the functional identity is declared "at
    every curvature sentence"; grep of record finds exactly 4 at-site
    pointers (:606 condition (1), :639 form (T), :647 form (C), :717
    (F)) plus the (D) bracket (:680) — but the [REV2-r3-2] printed
    bound "||S*_true − S*_red|| ≤ delta(S*_red)/mu" (:782) carries NO
    pointer: it is the one displayed inequality an M0 reader will
    quote, and its mu is identified only by remote inheritance from
    condition (1).
(b) [REV2-r4-3] declares its clause "read into (F)/[REV2-r3-3](b)" —
    but neither site carries an at-site bracket: (F)'s premise line
    (:713) still cites only "[REV2-r3-3] — the sweep-sup", and the
    superseded implication "until the sweep sup is measured, the
    uniformity premise is OPEN and DECLARED" stands unflagged at
    :807-809, 120 lines BEFORE the clause (:952-956) that withdraws
    its measured⇒discharged reading. Contrast the (D) protocol, where
    the same pass inserted an explicit at-site "[READ UNDER H-G6 ...]"
    bracket (:680-683) for exactly this situation.
WHY AMENDMENT: no content defect — the definitions upstream do carry
the identity, and the r4-3 clause is in the same section; but the
delta's own claim ("at every curvature sentence"; "read into") is
over-stated as printed, and a linear §2.2-bis reader meets the
superseded implication before its withdrawal. Same class as the
L1-9/L2-15 at-site-marking amendments (CARRIED precedent).
FIX SHAPE (three one-line bracket insertions): (a) append "[mu = the
J_TRUE floor, [REV2-r4-1](a)]" at :782; (b) append "[at SAMPLED-SUP
(estimate) class, read under [REV2-r4-3]]" at (F) :713-714 and at
[REV2-r3-3](b) :808.

### E5-L0-4 — AMENDMENT (measured this window, SR-12): the §13
### disposition table omits the R22F-L2-24 NOTE row while its own
### COUNTS line says "NOTES 5" — breaching the file's declared
### inclusion rule and its own arithmetic

ANCHORS: §13 table :2142-2152 — rows L0-19/20/21/22, L1-16/17,
L2-25/26/27 = 4 NOTE rows (L0-22, L1-16, L1-17, L2-27); COUNTS line
:2156 "NOTES 5 (no action owed)"; measured this window:
`grep -n "L2-24" phaseD_r22f_centerpiece.md` → ZERO hits (the ID
appears nowhere in the file); the declared inclusion rule :2063-2065
("courtesy NOTE rows are RETAINED", minted by [REV2-r3-8] to fix
exactly this defect class, R22F-L2-21) — and §12 honors it (all 4
round-3 NOTE rows present).
DEFECT: R22F-L2-24 (NOTE, the round-4 L2 prior-findings resolution
ledger — of record in phaseD_r22f_refute_r4_l2.md :59-94) has no §13
row. The count "5" is correct against the round files (VERDICT_r22f
§2.1: r4 = L0-22, L1-16, L1-17, L2-24, L2-27 = 5 NOTES) — the TABLE
is the incomplete side. The judge's index (§2.1) does list L2-24, so
no finding is absent from files+verdict (the absence rule holds at
verdict level); the defect is internal to the §13 table, which is
round-4 delta text in this pass's scope.
WHY AMENDMENT: bookkeeping only, zero dispositive content (a NOTE owes
no action); exact repeat of the L2-21 class, whose fix was CARRIED as
AMENDMENT.
FIX SHAPE (one row, append-only under the file's own protocol):
"| R22F-L2-24 | NOTE (round-3 resolution ledger; each disposition
verified at its edited site) | no action owed | — |" inserted before
the L2-25 row (or appended with a placement note).

### E5-L0-5 — NOTE: positive verification record of this pass (zero
### credit inflation; no action owed)

(a) BOTH round-4 probes RE-RUN this window: ALL-ASSERTS-PASS terminal
    lines reproduced (mu-identity 100x violation + transfer-form
    exactness; annulus parts A-G incl. the 0.425-shift sampled-sup=0
    leg). The loop record's probe claims are independently confirmed.
(b) H-G6 transfer inequality re-derived: mu_true_floor ≥ mu_meas − L_H
    follows from the Weyl/operator-norm bound |d'(H_true − H_red)d| ≤
    ||H_true − H_red||_M for ||d||_M = 1, uniformly on the ball and on
    any cone — direction correct (lower bound on the J_TRUE floor),
    honest refusal when L_H ≥ mu_meas. Sound at SCHEMA class.
(c) (F) J_red-side one-line derivation re-derived symbol-by-symbol:
    J_red(x1) − J_red(x2) ≥ (mu_red/2)·shift² (x1's VI + strong
    concavity along the H-G5 segment), then 0 ≤ J_true(x2) − J_true(x1)
    ≤ 2·eps_U − (mu_red/2)·shift² ⇒ shift ≤ 2·sqrt(eps_U/mu_red) —
    exact; the asymmetry claim (value route measured-carrier-sound,
    gradient route not) is CORRECT.
(d) [REV2-r4-3] containment claim verified: the adopted L2-26 form
    (instantiates-never-discharges) strictly contains L0-21's
    discharge-only-if-sustained clause (discharge never occurs ⇒ the
    conditional is preserved a fortiori; the stability clause is
    retained as the estimate-class license condition). The §13
    joint-adjudication note and VERDICT_r22f §2.2 ratification stand.
(e) [REV2-r4-2] scrub verified complete: every surviving
    "prox-regular" site (:743, :880-914 probe/defect narrative, :1791
    descriptive no-certificate-exists line, :1795 does-NOT-license
    clause, :1798/:1831 R-17 refinement, :1913 never-lands line,
    :2145) is either withdrawn-branch narrative, superseded-fragment
    quotation, or the F2 refinement — NO residual licensing use.
    Tietze–Nakajima as cited (closed connected locally convex ⇒
    convex) is classical-correct.
(f) [REV2-r4-5](a)-(f) all six cell edits verified present in the
    printed (vi) row (:1482) exactly as described; the cell's
    "licenses NO number even a-posteriori ... licenses ONLY the
    a-posteriori form" juxtaposition is surface tension only
    (form-type restriction vs current-instantiation restriction —
    disambiguated in-cell; no edit owed).
(g) J-1 (RES-CAP-6) extent check, as far as reconstructible: no rev-3
    snapshot exists in git (single centerpiece commit 904f950 already
    at the 2175-line closure state), so a diff is impossible —
    content-census instead: exhibit paragraph (:956-965), [GRAFT-G01]
    family (:967), ATLAS RIDER (:981), CONNECTION block (:985),
    per-term disposition reference (:1029), retained-verbatim line
    (:1047), and the §2.4 header (:1058) are ALL present; only the
    "## 2.3" header + lead-in words are missing, exactly as the judge
    found. The [REV2-J1] landing repair is confirmed sufficient.
(h) [REV2-r4-6](d) is a correct and necessary guard (the L0-18(d)
    conservative-floor half-sentence bridges cones of the SAME
    functional and must not be used against H-G6) — verified sound.

==============================================================================
## PAPERS NEEDED

NONE. (Every finding closes on the delta text, the round files, and
synthetic probes; no procurement would change any classification.)

## MACHINE SUMMARY (RES-CAP-1 pass, lens L0)

breaks = 0
repairs = 0
amendments = 4 (E5-L0-1 H-G5 "equivalently" gloss; E5-L0-2 mu_eff
  symbol collision; E5-L0-3 at-site carriage incompleteness, 3 limbs;
  E5-L0-4 §13 missing L2-24 NOTE row vs its own NOTES-5 count)
notes = 1 (E5-L0-5 positive verification record, limbs (a)-(h))
probe: esc_probe_r4delta_hg5_equivalence.py — RUN, ALL ASSERTS PASS
  (non-equivalence witnessed in both directions; no unsound license
  from any reading — supports AMENDMENT classification of E5-L0-1);
  r22f_v2_probe_r4_l0_mu_identity_proxreg.py and
  r22f_v2_probe_r4_l2_proxreg_annulus.py re-run, both PASS.
content_verdict_on_the_delta: SOUND — no BREAK/REPAIR; the four
  amendments are wording/carriage/bookkeeping and can ride the same
  landing edit that executes J-1 ([REV2-J1] + these four touches =
  one editorial pass); the RES-CAP-1 condition ("round-4 delta
  unrefereed" declared line) is DISCHARGEABLE once these amendments
  are adjudicated — the M0 landing of §2.2-bis and the (vi) row is
  NOT content-blocked by anything found in this pass.
