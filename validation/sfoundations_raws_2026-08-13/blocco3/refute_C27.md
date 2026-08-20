# REFUTE C27 — wave-1 refuter over PANEL_C27.md (Blocco 3)

S-FOUNDATIONS-C2, 2026-08-19. Role per BRIEF_wave1_refuter.md (cluster
C27, single ledger row). Inputs read IN FULL: PANEL_C27.md;
BRIEF_wave1_panels.md §0+§C27; anchors at source (ledger C27/C28/C42,
phaseB_tree_diff.md:133-142, M0:2330-2375, claims_registry [X-MGOV]
:1346-1358 / [X-TBAK] :1360-1372, gapmap :82-104/:726-752/:863-867/
:959-963, findings_registry :82-92/:230-242, the three tree advocacy
blocks, cava :81-85/:1113-1119/:1228-1232, seed_outcome_registry.md).
Web verification: Samakhoana-Grimmer page fetched (statement,
preprint status, norm setting); one census probe for missing lines.
Env untouched; only this file written.

VERDICT UP FRONT: the proposed row outcome (measurement-gated SPLIT,
duty F2-DUTY-C27-AGGCOND) SURVIVES. No BREAKS-VERDICT finding. Three
REPAIR-NEEDED findings (alternative-set omission; protocol
under-specification; falsifier outcome-space holes) must land before
the duty is binding and the "all alternatives closed by stated
reason" claim is true. Four AMENDMENTS, one NOTE.

---

## FINDINGS (row C27 — the cluster's only row)

### RC27-1 — REPAIR-NEEDED — alternative-set omission: block/regional/adaptive-domain (grouped) aggregation

**Mechanism.** The frozen statement's operator signature explicitly
admits "scalar or small-vector constraint block" (§1), and the census
window includes stress-TO aggregation practice (§2.3 items 2024-2025).
The canonical small-vector instantiation in that literature —
PARTITIONED aggregation: one KS/p-norm per GROUP of constraints,
groups static (block) or adaptive (regional/interlacing, adaptive
domains + rho) — is absent from the candidate set (a)-(l), never
listed, never closed. Brief §0.2: "An option loses only by STATED
REASON, never by omission." The §3.1 escape taxonomy is also
falsified as stated ("The only escapes are structural: shrink the
EFFECTIVE d the smoothing must cover (working set), or leave the
smooth class") — grouping shrinks the effective d INSIDE the smooth
class with no working-set machinery.

**Witness (census, search-result/abstract level, probe 2026-08-19).**
(i) Paris-Navarrina-Colominas-Casteleiro, "Block aggregation of
stress constraints in topology optimization of structures", Advances
in Engineering Software (sciencedirect S0965997809000568);
(ii) "An enhanced aggregation method for topology optimization with
local stress constraints", CMAME (S0045782512003349) — interlacing
regional measures, p-norm + max-normalization;
(iii) "An improved adaptive constraint aggregation for integrated
layout and topology optimization", CMAME (S0045782515000717) —
adaptive aggregation DOMAINS and rho (domain adaptation is a
different mechanism from the rho-adaptation the panel closed in (b)).

**Why the outcome still stands after the repair (derivation
sketch, inherits RC27-4's norm caveat).** Per-group, the same
gap-smoothness tradeoff applies with d_g = group size: pinning every
group's gap at mu_0/K_RICH forces per-group curvature scale
~ K_RICH ln(d_g)/mu_0 — the 1/mu_0 depth blow-up is unchanged;
grouping buys only the constant factor ln(d_g)/ln(N) (e.g. groups of
~55 lanes from N = 3498: ln 55 / ln 3498 ~ 0.49). Argmin-tie chatter
persists WITHIN a group, and tied lanes are typically spatially
adjacent, hence co-grouped. So (m) cannot displace the band at depth.
It DOES have a real refinement role the panel must adjudicate: per-
group fences are better-conditioned than the single global fence at
the same pin (rho_gap,g = K_RICH ln(d_g)/mu_0 < rho_gap,global), at
zero extra VJP cost beyond the vector rows.

**Named repair.** Add option (m) grouped/regional aggregation to
§1's candidate set; close it as primary by the stated reason above;
adjudicate group-fencing as an optional fence refinement inside the
adopted structure; extend the §3.1 escape list ("shrink d" covers
grouping as well as working sets, with the constant-vs-structural
distinction stated); add the three items to the §4.3 proposed
literature rows.

### RC27-2 — REPAIR-NEEDED — F2 duty not yet binding: arm B under-specified, w-formula circular, guard wording ambiguous

**Mechanism (duty (e): the pin must be executable and reproducible).**
Three defects in §4.2 as written:
(i) **Arm B under-specification.** B(W) = {i : v_i <= v_min + w} is a
variable-cardinality, W-dependent set. The margin_factory slot
(scipy NonlinearConstraint) requires a FIXED output dimension, and
the JAX stack requires static shapes under jit. The pin never states
the band refresh policy (recompute per iterate vs freeze between
exchange-style outer steps) or the fixed-arity mechanism. Two
implementers can build materially different arm Bs; the F-C27-1/2
rejected-step-rate comparison is then not reproducible — the
falsifier cannot bind.
(ii) **w-derivation circularity.** w is defined via the per-step
change "in v_min and in any band-adjacent lane", but band-adjacency
presupposes w. As pinned, the formula is not well-founded.
(iii) **Guard wording.** "identical accept/reject on every rung" is
ambiguous between TR step accept/reject (trivially different between
arms — rejected-step RATE is the experiment's metric, so demanding
identity contradicts the design) and rung-level enforcement
verdicts. Only the second reading is coherent with "ANY enforcement
divergence between arms = protocol red".

**Witness.** PANEL_C27.md §4.2 (band definition, derived-quantities
block, certificate-equivalence guard); gapmap:101-103 (the slot is
vector-CAPABLE; nothing there fixes arity or cadence).

**Named repair.** Pin: band refresh cadence; fixed-arity mechanism
(e.g. k_max derived from the recorded walks' max near-binding count,
padded with provably-inactive rows — constants derived, R5); re-found
w as K_RICH x max over the recorded walk over ALL lanes of the
per-accepted-step |Delta v_i| (or declare a one-pass fixed-point
construction); rewrite the guard as "identical rung-level enforcement
verdicts at the declared resolution".

### RC27-3 — REPAIR-NEEDED — falsifier set does not partition the outcome space

**Mechanism (duty (e): every outcome must refute or confirm
something).** As pinned: F-C27-1 fires only on {conflict rung AND arm
A above red-line AND arm B in band}; F-C27-2 only on {arm A in band
at ALL rungs, BOTH instances, AND no conflict fires}; F-C27-3 only on
band-escape. Unassigned branches:
(alpha) conflict fires at a rung but arm A stays WITHIN the red-line
there — the §4.1(2) trigger has then mandated the band at a rung
where the measurement shows pure KS healthy: trigger calibration
(rho_curv derivation) is questioned in the conservative direction;
no named verdict.
(beta) arm A above red-line AND arm B also out of band (hybrid fails
to cure conditioning) — fires neither F-C27-1 nor F-C27-3 (no
band-escape needed for this failure); the AL fallback is reachable
only through F-C27-3's repeated-escape branch; no named verdict.
(gamma) arm A above red-line at a rung with NO two-constant conflict
(rho_gap <= rho_curv) — outside F-C27-1's predicate and incompatible
with F-C27-2; this outcome would show the conflict predicate MISSES a
real chatter regime, i.e. it refutes the two-constant rule's trigger
role itself; no named verdict.

**Witness.** PANEL_C27.md §4.2 falsifier block (predicates quoted
above are verbatim-faithful conditions of F-C27-1/2/3).

**Named repair.** Add the three residual branches with named
verdicts: (alpha) -> rho_curv re-derivation duty + trigger demoted to
declaration-only until re-derived; (beta) -> operator question
re-opens, escalation to the named AL fallback or the binding-arc
route WITHOUT requiring band-escape; (gamma) -> two-constant trigger
falsified as insufficient (its §4.1(2) role re-adjudicated), band
mandated by measurement at that rung.

### RC27-4 — AMENDMENT — evidence-level of the §3.1 "wall": preprint status, norm setting, and adaptive-scheme over-extension

**Mechanism (duty (b) inflation hunt).** Three over-statements around
the decisive census item, none of which moves the outcome:
(i) Samakhoana-Grimmer is an Optimization Online PREPRINT (posted
2025-12-11, updated 2026-07-12; page re-verified by this refuter).
"Page-verified" correctly covers the STATEMENT; §3.1's "THEOREM-
BACKED WALL" and §4.1(2)'s "the census theorem GUARANTEES the
conflict occurs at depth" consume it as an established guarantee with
the proof unchecked in-repo and no peer-review behind it.
(ii) The theorem is stated for overestimating smoothings of max on
R^d **in the infinity norm** (page: "smoothings of the
(coordinate-wise) max function in R^d in the infinity norm"). The
panel's quantitative translation — "must carry sharpness (curvature
scale) within a constant (~1.23x) of the incumbent's rho" — transfers
the constant to the incumbent's curvature-of-record normalization
(softmax-covariance spectral scale, ~rho/4 at ties, gapmap GAP-27)
without deriving the norm bridge; such transfers can pick up
dimension-dependent factors. The qualitative wall (gap x smoothness
bounded below ~ ln d, hence curvature ~ 1/gap at fixed d) is robust;
the 1.23x-in-rho figure is underived on file.
(iii) The theorem bounds FIXED smoothings; §3.2(b)'s "the 2025
near-optimality theorem denies it [adaptive-KS] any
gap-at-lower-curvature miracle" extends it to input-dependent
(adaptive) schemes without derivation. Adaptive-KS stays closed
anyway on its two independent legs (motive void of record,
M0:2369-2375; measured direction-wrong on (A2), GAP-27).

**Repair (text).** Carry "preprint, statement page-verified, proof
not checked" into §3.1 and §2.3; restate the wall qualitatively or
add the one-line norm-bridge derivation; replace "the census theorem
guarantees" in §4.1(2) with "the trigger is arithmetic on derived
constants; the preprint theorem predicts the conflict at depth" — the
gate design already survives both worlds (F-C27-2 covers the
no-conflict branch), which is why this is not REPAIR-NEEDED.

### RC27-5 — AMENDMENT — cava absence-proof defective as recorded (hit list wrong; English stems over an Italian corpus); conclusion survives inspection

**Mechanism (duty (b): absence claims must be search-proven — the
recorded proof must be true).** §2.4 states the grep
`C27|Poon|Kennedy|Kreisselmeier|aggregat|semi-infinite|exchange` (-i)
"hits only D-40 (:1230...), the C27-collision row (:1115), and the
C30/:83 'KS a rho derivato' mentions". Measured this window
(grep -inE, then byte-level python cross-check): the TRUE hit set is
EXACTLY {1115, 1230}. Lines :83 and :1117 contain NO token of the
pattern — "KS a rho derivato" matches nothing in it, and the Italian
"aggregazione" does not contain the English stem "aggregat"
(z, not t). The stated hit list is wrong, and the pattern is
language-blind on an Italian document: it cannot see "aggregazione"
(3 lines: 660, 1117, 1182), "scambio", or "semi-infinito".

**Inspection of the missed lines (this refuter).** :1117 = cava C30
(the panel consumed it by direct read — content use is correct even
though it was not a grep hit); :660 and :1182 = the D-12 cross-mode
measure aggregation line (J = double-integral over d mu_m d nu(m)) —
OBJECTIVE aggregation across operating modes, "classe non-collassante
gia registrata", not a constraint-aggregation-operator row. The
material absence conclusion (no cava row on aggregation conditioning
or C27 alternatives) SURVIVES.

**Repair (text + record).** Correct §2.4: state the measured hit set
{1115, 1230}; re-run with bilingual stems (e.g. add
`aggregazion|semi-infinit|scambio`) and record the result; declare
D-12 (:660/:1182) as inspected-adjacent, out of scope.

### RC27-6 — AMENDMENT — advocacy attribution: "3/4" backs the divergence, not the adopted structure; the inst-L design inverts O-F18 and is panel content

**Mechanism (duties (c)+(d); R-4).** Verified at source: P-F16's
recommendation is "O2 in-loop + O3-style adaptive phase refinement
near convergence" + mandatory post-hoc sweep
(phaseA_tree_propulsion.md:628-633) — i.e. KS KEPT in the loop; it
challenges on exactness only, not on the working-set structure. Tree
advocacy for exchange/working-set is therefore at most 2/4 (O-F18,
V-F23-O2); "3/4" is the DIFF's divergence call of record
(phaseB_tree_diff.md:133-142), which bundles the exactness challenge.
Separately, the adopted inst-L architecture (explicit band rows +
KS fence on the COMPLEMENT) INVERTS O-F18's "KS within the working
set" (:1031-1037) — no tree advocates the adopted inst-L structure;
the panel declares the transposition ("panel content") but headlines
it under "(e) ... the 3/4 tree challenge" and adopts it as
"structure CONVERGED". Finally, the CONVERGED label sits uneasily
with F-C27-2, which can shelve the hybrid: what actually converges
un-gated is {two-constant derivation repair + band as the DERIVED
escalation route + inst-XI covering/sweep semantics + multiplier
reporting}, with hybrid production adoption conditional on the
measured half. If F-C27-2 fires, the row as currently worded reads
as a flip-flop.

**Repair (text).** In §3.2(e)/§4.1/§5: attribute the working-set
challenge as 2/4 + diff-divergence 3/4; mark the inst-L
band+fence design explicitly as panel-designed structure (tree
advocacy covers the inst-XI exchange semantics); word the converged
half as the four items above rather than "operator structure adopted:
working-set/exchange hybrid" unconditionally.

### RC27-7 — AMENDMENT — frozen statement omits two load-bearing context elements later used in the verdict

**Mechanism (duty (a)).** (i) The G1/REQ-NONSTALL survive-and-report
duty (globally-finite scalar surrogate, [X-MGOV] of record) is absent
from §1's objects/axes yet decides part of the verdict (§4.1(1):
"the band block does not provide it"). An axis used to retain the
incumbent belongs in the frozen statement — alternatives (j)/(k)
were closed without being tested against it. (ii) The fixed-shape/jit
requirement of the JAX stack (which drives RC27-2's arm-B issue) is
likewise absent from the operational context. Outcome unmoved (the
incumbent is retained as G1 surrogate everywhere; (j)/(k) stay closed
on their stated reasons), so text-level: add both to §1.

### RC27-8 — NOTE — minor strengtheners and bookkeeping

(i) The near-binding band has census precedent the panel did not
attach: epsilon-active constraint selection is classical practice in
local-stress TO (active-set selection of constraints above a
threshold) — attaching it would convert the inst-L structure from
pure panel content to census-supported practice (strengthens, does
not weaken). (ii) §3.0's "the derived-rho half is INDEPENDENTLY
CONFIRMED" is form-level: O-F18's P3 derives rho = ln(m)/eta_KS
against the INTER-NODE margin target, not the incumbent's
mu_0/K_RICH enforcement target (phaseA_tree_optimization.md:1007-1011,
:1046-1049) — the derivation PATTERN is confirmed, the constant's
target differs. (iii) §2.3's LSE-conditioning support cites an
AI-aggregator topic page; the primary LSEMINK item (arXiv) should
replace it at the same evidence level. (iv) §4.2 adds new K_RICH
roles (band width w; chatter red-line multiplier) — the C42
dependency is declared, but the C42 row's "one numeral, 8 roles"
count grows; the wave-3 audit should receive the delta explicitly.
(v) §4.4 says "7 web queries + 1 page fetch" while §2.1 lists 6
queries + 1 page fetch — trivial SR-9 arithmetic mismatch. (vi)
"alternatives_closed": 10 in §5 is defensible only counting CVaR and
scenario (bundled as (g)) separately — state the counting rule.

---

## VERBATIM-QUOTE AUDIT DECLARATION

Spot-checked at source this window, all VERBATIM-FAITHFUL unless
noted: GAP-27 headline (gapmap:728-729) — exact; M0 adopt-or-declare
motive clause (M0:2369-2375) — exact; "keeps the conservativeness
theorem intact" (gapmap:750) — exact; "inherits the defect if
underived" (gapmap:748-749) — exact; margin_factory vector-slot note
(gapmap:101-103) — faithful paraphrase; O-F18 "4 wrapped around 2" +
multiplier clause + P3 "decides the 'is rho magic' objection"
(:1031-1037, :1046-1049) — exact; O-F18 opt.3 rejection (:1012-1014)
— exact; V-F23 m >= L_xi*Delta_xi/2, Piyavskii-Shubert, O3/O4
closures, falsifier (:1036-1070) — exact; P-F16 "sharp but fragile"
(:623-625), "issued against the TRUE semi-infinite constraint, not
the smoothed one" + mandatory sweep (:628-633) — exact; ledger C27
row fields incl. note (choice_ledger.yaml:407-417) — exact; C42
:571-579 and C28 :419-427 — exact; [X-MGOV]/[X-TBAK] fields
(claims_registry.yaml:1346-1372) — exact incl. falsifier names
R-KS/R-GRAD/R-G1/R-FD and the mu_0_min form; findings carrier row +
GAP-27/GAP-1 mapping (findings_registry.yaml:82-92, :232-241) —
exact; cava :83/:1115/:1117/:1230 — content exact (grep hit-list
mis-report = RC27-5); diff C27 block :133-142 — exact ("H-tree
silent" is a fair paraphrase of the 3/4 with O/V/P named); seed
registry v3 PASS both directions 2026-08-19 — exact;
Samakhoana-Grimmer numbers ln(d) / ~0.8145 ln(d) / ~1.23x — page
re-verified exact (norm setting and preprint status = RC27-4).
M0 measured numbers m_ref = 6.810298e-01, N = 3498, rho = 766.83,
gap = 1.0641e-02 (M0:2341-2343) and AD-vs-FD 3.29e-06 vs 5.92e-05
(M0:2351-2352) — exact. Mis-cites found: NONE beyond the RC27-5
grep-report defect.

## DEDUP REGISTER

This file mints nothing. RC27-1's three grouped-aggregation items are
absent from docs/literature_registry.yaml (panel's grep reproduced
this window: zero aggregation rows) — they are PROPOSED additions
riding the panel's §4.3 proposal, not mints. GAP-27's carrier row
`margin-governor:G1-three-jump-channels` cited, not touched. No
contradiction with verdicts of record found: the proposed SPLIT
preserves [X-MGOV]'s theorems, its adopt-or-declare (adaptive-KS
still not adopted), the G1/REQ-NONSTALL duty, and the C28 boundary
(MPCC operator-half closed here, representation-half left to C28,
consistent with gapmap:84-85). Findings RC27-1..8 are refutation
findings on BASE/blocco3/PANEL_C27.md only; registry deltas remain
the judge/orchestrator's to consume.

## MACHINE SUMMARY

```json
{
  "cluster": "C27",
  "findings": [
    {"id": "RC27-1", "class": "REPAIR-NEEDED", "row": "C27"},
    {"id": "RC27-2", "class": "REPAIR-NEEDED", "row": "C27"},
    {"id": "RC27-3", "class": "REPAIR-NEEDED", "row": "C27"},
    {"id": "RC27-4", "class": "AMENDMENT", "row": "C27"},
    {"id": "RC27-5", "class": "AMENDMENT", "row": "C27"},
    {"id": "RC27-6", "class": "AMENDMENT", "row": "C27"},
    {"id": "RC27-7", "class": "AMENDMENT", "row": "C27"},
    {"id": "RC27-8", "class": "NOTE", "row": "C27"}
  ],
  "breaks": 0,
  "repairs": 3,
  "amendments": 4,
  "notes": 1
}
```
