# ESC — DOC-1 REVISION-10 CONFIRMING ROUND, LENS L0

Date: 2026-08-19 (S-FOUNDATIONS-C2 window). Role: confirming refuter,
lens L0, over the REVISION 10 delta of `phaseD/phaseD_stop_proof.md`
(delta = CONTENT: every edited passage + its consumers). Mandate:
`r2pass/BRIEF_rev10_confirm.md`; adjudication context:
`r2pass/VERDICT_doc1_closure.md` (§1 R9-A/B/C adopted specs, §4
RES-DOC1-1/2, §5 falsifiers) + the ratified strategy paragraph of
`validation/ADVISORY_SfoundationsC2_prompt_2026-08-19.md` § PRIMA
AZIONE PARALLELA (sufficient-but-unoptimized grant). Inputs read IN
FULL: the closure verdict; the strategy paragraph; the §13 REVISION 10
block (l.4687-4917) + EVERY edit site it declares, each read with
surrounding context (header l.1-135; condition of record l.2140-2341;
sufficiency passage l.2344-2362; momentum block l.2384-2387; assembly
splice l.2391-2401; AUD-cp note l.2449-2496; falsifier consequent
l.2496-2574; grant head l.2578-2607; honest status line l.2646-2689;
§9 gamma-table carrier l.2860-2913; §13 rev-9 annotations l.4360-4450,
l.4481-4496, l.4550-4598). INDEPENDENCE: the other lens's file was not
read and was not consulted in any form. All line numbers below are
post-edit, measured this window.

==============================================================================
## §A DUTY (a) — SUFFICIENCY AT PEN GRADE: RE-DERIVED, DELIVERED

I re-derived every load-bearing step of (D1)-(D7) from the printed
strong set, independently of the document's prose:

(D1) per-slice uniqueness. (H-G8-2): theta = e_S > 0 at every point
of dom e; slices are INTERVALS ((H-G8-2) printed member, implied by
(H-G8-1)'s convex dom e — slices of a convex set are convex). A
strictly increasing function on an interval is injective: at most one
S-root per slice. VERIFIED. The interval clause is load-bearing here
(on a disconnected slice, per-branch monotone pieces can have
overlapping ranges — the ECL0-1 two-branch witness — so "strictly
increasing per component" does not give injectivity); rev-10 keeps it
printed exactly where it is consumed. The parity-bracketing retirement
sentence (l.2274-2277) is honest: uniqueness is monotonicity, and no
step below reads parity (measured: "parity" body hits are only the
retirement sentence l.2275-2276; all others are §13 history or the
unrelated §2/§3 wave-count usage, l.889/1025).

(D2) hull-wide chart. (H-G8-3) totality: at every hull point the root
exists; with (D1), exactly one; per-segment continuations land on the
data root because under a single chart there is only the data root.
VERIFIED.

(D3) root-map continuity + C^2 — the step R9-A broke at revision 9,
now re-derived in full: image point (v_0, S_0) of hull point W_0 lies
in int N ((H-G8-3): N is a compact R^2-neighborhood of the image, so
every image point is interior to N); a closed box B = [v_0 +- delta] x
[S_0 +- delta] subset int N subset dom e exists; theta >= theta_min > 0
on B (e_S continuous on compact B by (H-G8-1)'s C^2, positive by
(H-G8-2)); the vertical segments {v} x [S_0 - delta, S_0 + delta] lie
in B subset dom e, so e(v, S_0 +- delta) - e(v, S_0) has magnitude
>= theta_min*delta for every v in the box's v-range; W -> (v, eps) is
continuous on {rho >= rho_min} ((H-G8-3)); eps(W_0) = e(v_0, S_0), so
for hull W near W_0, |eps(W) - e(v(W), S_0)| < theta_min*delta, hence
e(v(W), S_0 - delta) < eps(W) < e(v(W), S_0 + delta); the slice at
v(W) is an INTERVAL containing S_0 +- delta and the root S(W)
(totality), and e(v(W), .) is strictly increasing on the whole
interval, which FORCES S(W) into (S_0 - delta, S_0 + delta).
Continuity delivered. C^2 upgrade: F(W, S) = e(v(W), S) - eps(W) is
C^2 on a neighborhood of (W_0, S_0) (e C^2 on the open int N; (v, eps)
smooth on rho >= rho_min), F_S = theta > 0, so the IFT gives a local
C^2 root branch, which coincides with S(W) wherever roots exist by
(D1) (theta > 0 holds on ALL of dom e, so off-hull roots near the hull
are unique too — the local IFT branches patch consistently).
VERIFIED COMPLETE. The interval clause and the interior-neighborhood
clause each carry named load; no unwritten hypothesis found. This is
where I hunted hardest for an in-class witness (the R9-A shape one
rung further out): the placement argument closes every route I tried —
(i) fiber-endpoint discontinuity needs the image to approach the
domain boundary, killed by N-interiority; (ii) root escape to a far
S-value needs a disconnected or non-monotone slice, killed by the
interval clause + theta > 0 on ALL of dom e (not just at roots — the
strong set's single-chart member is genuinely stronger than the
retired root-quantifier); (iii) degenerate dom e (a segment, empty
interior) kills (H-G8-3)'s N clause, hence OUT-OF-CLASS. No witness
IN the class exists: (D3) is a theorem of the printed members.

(D4) image compactness: continuous image ((D3)) of the compact hull
(hull compactness of record: segment hull of compact K = image of
K x K x [0,1] under an affine-in-parameter continuous map). VERIFIED.

(D5)-(D7) assembly: strict Legendre bridge consumes theta > 0
((H-G8-2)) and strict PD of Hess e at image points (image subset N,
(H-G8-1) strictness on N) — congruence unchanged from the rev-8 form
discharged CLEAN at both lenses of the confirming round; rest-state
block decomposition with momentum block 1/(rho*theta) > 0 ((H-G8-2)
theta read at image points, in dom e by (H-G8-3)); boost affinity
(boost is affine in W, E = -rho*S boost-invariant) transports PD to
all velocities; Hess_W E continuous near the compact hull ((D3) C^2 +
(H-G8-1) C^2) and PD at every hull point gives uniform
lambda_min > 0 on the compact hull (min of a continuous positive
function on a compact set; equivalently via (D4): lambda_min of
Hess e uniform on the compact image inside N, with congruence factors
continuous on the compact hull); Bregman identity
E(V|U) = int_0^1 (1-s) <D^2E(U+s*Delta) Delta, Delta> ds over segments
inside the hull gives item (i) with c = lambda_min/2 — the ORDER-TWO
lower bound, i.e. the granted item that failed at order one on the
rev-9 witness. VERIFIED. Item (ii) flux smoothness through the C^2
chart: p = -e_v is C^1 in W through (D3) — VERIFIED as stated.

WITNESS-USE AUDIT (per brief: an out-of-class witness proves
nothing): rev-10 does NOT misuse any. W-A is used only as (f2)'s
falsifier-class exhibit and is correctly shown OUT-OF-CLASS three
ways, each verified by me on the witness: two-strip domain
([0.5,1)x[0,1]) U ([1,1.5]x[10,11]) is non-convex (violates
(H-G8-1)); fibers jump [0,1] -> [10,11] at v = 1 (violates (H-G8-4));
the branch-1 hull image accumulates at (1,1), and (1,1) is not in
dom e (the v=1 slice is [10,11]), so no compact N subset dom e
contains the image (violates (H-G8-3)). The necessity chains
(m1)-(m3) are correctly framed at (f3) as OUT-of-class witnesses that
price individual members (each violates essentially only the member
it prices: (m1)/(m3) the strictness clause — (m3)'s box patch
satisfies domain convexity, chart, totality, constant fibers — (m2)
the PSD/concavity content): legitimate necessity role, no
sufficiency claim rests on them. The AUD-cp closure accounting is
ARITHMETICALLY VERIFIED: the (v,S)-image of the tabulated domain is
the R-ln-v-sheared strip; its lower boundary S = phi(T_min) + R ln v
is concave in v, chords between lower-boundary points fall below the
graph, i.e. exit the strip: NON-convex — (H-G8-1)'s domain half
genuinely fails there; and its only in-derivation loads (interval
slices for (D1), fiber structure for (H-G8-4)) are verified DIRECTLY
at the closure (interval fibers [phi(T_min)+R ln v, phi(T_max)+R ln v]
with v-continuous endpoints), so the granted items discharge through
the same chain — the honest sufficient-not-necessary display is
correct, and it does NOT violate (f4): the closure discharge is an
instance audit outside the strong class, declared as such, not an
abstract grant from a weaker member subset.

DUTY (a) VERDICT: the strong set DELIVERS every granted item —
root-map continuity on the compact hull, image compactness, the
lambda_min > 0 chain, and item (i) at c = lambda_min/2 — with no gap
found at pen grade. ZERO findings of class BREAKS-THE-LEG or
REPAIR-NEEDED from this duty.

==============================================================================
## §B DUTY (b) — MANDATE CONSUMPTION, CARRIER BY CARRIER

R9-A (RES-DOC1-1), the judge's ten named propagation sites, each
verified consumed on the page:
 1. condition clause re-scope: (H-G8-4) written l.2242-2267 with the
    adopted spec content (fiber endpoints continuous in v, closed
    interval fibers / hull image compact) + the judge's fallback
    branch kept verbatim-equivalent (l.2261-2267: imposed DIRECTLY,
    waives NO other member); the rev-9 "under which ... continuous"
    per-slice delivery is GONE from the body (zero body hits of
    "single-upcrossing": sole hit l.4381 = preserved history);
 2. assembly splice l.2391-2401: continuity/C^2 now cited from
    (D2)-(D3), compactness from (D4) "no longer a bare premise", the
    "three chart clauses" splice retired (sole body occurrence = the
    retirement sentence itself, line-wrapped at l.2396-2397);
 3. falsifier-consequent enumeration l.2528-2531: geometry bucket now
    (H-G8-3) + (H-G8-2)'s interval half + (H-G8-4) + (H-G8-1)'s
    domain half (jointly with R9-B, below);
 4. grant-head epithet l.2578-2607 (jointly with R9-C, below);
 5. header: status paragraph l.31-39 + audit line l.124-132 both
    carry the fiber member and the R9-A citation;
 6. §9 table l.2893-2906: RESTATED chain names fiber regularity
    (R9-A's member) + v-continuous endpoints at the closure;
 7. honest status line l.2656-2676: revision-10 form with fiber
    regularity + closure discharge with interval fibers;
 8. AUD-cp note l.2469-2476: the ONE clause the judge ordered
    ("(H-G8-4) is FREE there ... endpoints CONTINUOUS in v", citing
    VERDICT_doc1_closure §3(b));
 9. §13 ECL0-1 entry: delivery sentence re-scoped by annotation
    l.4384-4399 (prior text preserved) + the previously-missing
    continuity falsifier ADDED l.4419-4430 (moving-slice witness
    class; live form = full-class discontinuity exhibit, refuted by
    (D3)-(D4)) + the rev-9 uniqueness-only fallback RE-BASED
    l.4402-4406;
10. domain ladder l.4443-4450: outermost rung slice-FAMILY regularity
    appended, prior text preserved, judge's wording.
NO CARRIER MISSED. The ECL0-1 delivery re-scope and the fallback
re-base are faithful to §1 R9-A including the a-fortiori point.

R9-B (RES-DOC1-2(1)) at BOTH sites: body consequent l.2519-2542 —
root-quantifier content moved OUT of the geometry bucket into the
pin-delivered enumeration ("hull-image states and S-roots are domain
points the whole-domain reading covers, R9-B of record"), uniqueness
consequence kept with the interval member (l.2539-2542) — and §13
echo annotation l.4481-4496 (prior text preserved). The DECLARED
RECALIBRATION (geometry bucket enlarged by (H-G8-1)'s domain half, a
member the judge's rev-9-calibrated list could not name) is verified
SOUND at pen grade: no reading of the §1 pins constrains the SHAPE of
dom e (pins constrain derivatives where e is defined, never where it
is defined — the row's own a0-positive patch witness), so omitting
the domain half would have made the whole-domain consequent FALSE;
the declaration is printed at the R9-B entry (l.4757-4765) per the
R-4 binding rule. Adopted scoping present at both sites; the two
sites' geometry enumerations are IDENTICAL (four members), and (f5)'s
list matches them — three-way consistent.

R9-C (RES-DOC1-2(2)): route CHOSEN of the judge's two = retire the
staged epithets at every current-condition carrier (the harmonization
route, applied more radically than the minimal epithet-extension —
within the judge's stated alternatives). Verified at ALL variants by
MY OWN measured sweep (commands in the scope-sweep declaration): the
retired names survive ONLY in lineage recitals and §13 history/
annotation contexts — 18 grep lines, my classification matches the
block's line-for-line (115, 118, 2165, 2167, 2887, 2890, 4186, 4288,
4561, 4567, 4574, 4575, 4648, 4649, 4679, 4720, 4779, 4780); my WIDER
sweep over the epithet family the block's pattern omits
("DOMAIN-COMPLETED": hits 112, 2161, 2885, 3892, 4270; "STRICT +
hull-theta": hits 3977, 4288, 4552, 4560, 4574, 4648) finds ZERO
stale current-condition carriers either — all lineage/history. The
SIX current-condition carriers all print the (H-G8) taxonomy,
verified: header audit l.125, condition l.2180, grant head
l.2581-2582, honest status l.2661, §9 l.2895-2896, block label
summary l.4860; additional consistent recitals of the CURRENT name at
l.37, 4772-4773, 4836, 4913 (no stale token anywhere). The §13 ECR1-3
annotation is PRESENT l.4569-4580, names the grant head as the missed
sixth carrier, and preserves the benign-defined-term ruling.

DUTY (b) VERDICT: mandate FULLY consumed; zero ECR1-3-species carrier
misses in my window.

==============================================================================
## §C DUTY (c) — NEW-MINT HUNT (defects minted by the rev-10
## restatement itself): TWO FINDINGS, BOTH WORDING

### R10L0-1 — WORDING — (H-G8-4)'s "equivalently" gloss extended
### beyond the adopted spec, and beyond what the gloss can carry.
Site: l.2242-2248 ((H-G8-4) member text) + l.4725-4731 (§13 R9-A
entry's meta-claim). Mechanism: the judge's adopted spec reads
"(fiber endpoints continuous in v, fibers closed intervals —
equivalently the hull's (v, S)-image compact), under which
single-upcrossing DOES deliver root-map continuity ..."; the printed
member folds the CONSEQUENCE into the equivalence: "— equivalently
the hull's (v, S)-image is COMPACT and the root map W -> S(W) is
continuous on the compact hull." Even granting the in-context reading
(the forward direction holds given (D1), closed fibers and continuity
of e — the judge's own parenthetical mechanism), the REVERSE
direction is false as an equivalence of the member alone: image
compactness + root-map continuity constrain dom e's fibers only along
the image, not the fiber family (a dom e with wild fiber endpoints
away from a nice tube around the image satisfies the right side and
not the left). The same one-directionality already infects the
judge's narrower gloss (spec-seeded — standing disposition, not
re-opened); the rev-10 DELTA is the added conjunct. Zero derivational
load either way: the strong branch DERIVES both conclusions at
(D3)-(D4) ("THEOREMS under the strong set"), and the fallback imposes
BOTH directly ("the member's two conclusions ... members only in the
fallback branch" — the plural disambiguates the "/"). Consequently
the §13 R9-A entry's "WRITTEN as (H-G8-4) with the judge's adopted
spec text", which quotes the NARROWER gloss, is loose about the
extension. Repair (one clause, at the landing pass): either restore
the spec's split (equivalence for compactness, consequence clause for
continuity) or reword "equivalently" to "the working form imposed in
the fallback branch:". No witness, no consumer, no granted item
moves: WORDING.

### R10L0-2 — WORDING — the R9-C measured-sweep sentence: counting
### unit misnamed, and pattern narrower than the claim it certifies.
Site: l.4778-4794 (REVISION 10 block, R9-C entry). Mechanism, both
halves measured in MY window: (i) the block prints "18 token hits" for
its grep; 18 is the LINE count (grep -n semantics, which its own
quoted command uses); the TOKEN count under -o is 20, because the
pattern-quotation line l.4779 itself carries three matching tokens
(l.4780 the fourth). The number 18 is correct for the command as
quoted; the word "token" is not. (ii) The quoted pattern
(chart-complete|topology-complete|+past forms) under-covers the
staged-epithet family that the SAME sentence's claim quantifies over
("the staged epithets are RETIRED ... at EVERY current-condition
carrier"): the revision-6/7 stage names ("STRICT + hull-theta",
"DOMAIN-COMPLETED", the bare "STRICT form") are staged epithets the
pattern never sweeps. My wider sweep (commands + hits in the
declaration below) confirms the claim's SUBSTANCE — zero stale
current-condition carriers under the wider family too — so no
ECR1-3-species miss exists; the defect is that the cited evidence is
narrower than the certified claim (the overcert-guard species at its
mildest: claim true, cited sweep partial). Repair (ledger, one line):
"18 line hits (20 tokens)" + name the wider family as swept or sweep
it. WORDING.

Also hunted, NOT sustained: carrier-enumeration divergence (none —
the four geometry members are enumerated identically at the
consequent l.2528-2531, the §13 R9-B echo l.4490-4492, and (f5)
l.4848-4850); epithet drift (none — §B sweep); falsifier lists vs the
new members ((f1)-(f5) checked member-by-member: (f2)'s three
out-of-class showings each verified, (f3)'s necessity framing
verified, (f5)'s geometry list matches the modulo bucket, the ECL0-1
falsifier addition closes the judge-named hole); "under which"
scoping to less than the full set (my measured sweep: every
grant-scoping "under which" in the delta scopes to the full strong
set; the one other in-delta occurrence, l.2352, scopes a WITNESS
parameter regime inside the (m2)-family clause — not a granted-item
claim, so the strategy sentence's natural referent class is
unviolated; recorded here so the letter-vs-referent reading is on
file); the "18-line vs 20-token" arithmetic above is the only
measured-meta-claim discrepancy found — the leg-3 MD5 and the
edit-site line anchors all REPRODUCE (see §D and the anchor
spot-checks: (H-G8-1) l.2187, (H-G8-2) l.2202, (H-G8-3) l.2223,
(H-G8-4) l.2242, (D)-chain from l.2268, grant head from l.2578, §13
annotation sites 4384/4419/4443/4481/4569 — all exact).

==============================================================================
## §D DUTY (d) — ZERO-EDIT SCOPE, MEASURED

Leg-3 body: anchors measured this window — "## §4 The uniqueness
half" = l.1087, "## §5 The main theorem" = l.1440; span l.1087-1439 =
353 lines, matching the block's post-edit declaration exactly (and
the +16 shift from the pre-edit 1071-1423 is consistent with the
header's rev-10 growth: status-paragraph recital l.31-39 + audit-line
extension l.124-132). The recorded MD5 REPRODUCES on the current
file: `sed -n '1087,1439p' file | head -c -1 | md5sum` =
6ef096f238ef76bc0ea8965cd066ef96 — identical to the block's recorded
value (the recording's implicit convention is no-final-newline; raw
extraction gives 0a186e9d252fc01bedb657e83013bc58; noted for
reproducibility, no finding — the value regenerates once the
convention is found, and the file is LF throughout). Independent
marker check: ZERO hits of H-G8 / revision-10 / R9-* markers inside
l.1087-1439 (grep line-number lists below: nothing between 135 and
2159). LEG-3 CARRIES ZERO REVISION-10 EDITS: CONFIRMED.

Delta containment (edit-site list vs my own sweep): every "H-G8" hit
(89 lines) and every rev-10/R9 marker hit (59 lines) falls inside the
declared edit-site ranges — header 31-39/118-132, condition
2159-2341, sufficiency 2344-2350, momentum 2384-2387, splice
2391-2401, AUD-cp 2449-2496, consequent 2496-2574, grant head
2578-2607, honest status 2646-2685, §9 2880-2906, §13 annotations
4384-4450/4481-4496/4569-4580, block 4687-4917. No marker-bearing
passage outside the declared list; the two beyond-judge-list sites
(sufficiency attributions, momentum clause) are DECLARED in the
block's edit-site list and are strategy-covered member-attribution
recalibrations. NO NON-MANDATE PASSAGE MOVED, to the resolution this
window's instruments give (marker sweep + anchor arithmetic + span
hash; pre-image byte comparison is not available without git, which
the brief forbids).

==============================================================================
## §E DUTY (e) — LABEL/VERDICT MOTION: NONE

[T-T0P] main statement: SCHEMA of record, unmoved (header l.43-47
untouched in label content; block label summary l.4854-4855).
Route-level abstract-EOS verdict: OPEN, unmoved (l.2677-2681, l.4857).
gamma(T) closure conclusions: unmoved — granted items still
discharged IN FULL at the closure, now with the honest
dom-e-convexity accounting, and "table conclusions UNCHANGED"
(l.2906); the closure discharge mechanism matches the judge's §3(b)
reconciliation (l0's moving-interval fiber description adopted at the
AUD-cp clause). Quadruple-pinned grant, two-piece r2 residue: stand.
Held-out landings: correctly still BLOCKED pending this round's dry
adjudication (block residue (1) states the new mandate accurately
against the advisory text). All five §13 rev-9 annotation sites
preserve prior text ("prior text preserved" verified at each). No
orphan objection: the closure verdict's three findings are the only
open items of record against revision 9 and all three are consumed.

==============================================================================
## SCOPE-SWEEP DECLARATION (commands run in MY window, this file)

On `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md`
(4917 lines, 282293 bytes, LF endings):
 1. `grep -n -i -E "chart-complete|topology-complete"` -> 18 lines
    (115, 118, 2165, 2167, 2887, 2890, 4186, 4288, 4561, 4567, 4574,
    4575, 4648, 4649, 4679, 4720, 4779, 4780); with `-o` -> 20
    tokens. All lineage/history/annotation; zero current-condition
    carriers.
 2. `grep -n -i "DOMAIN-COMPLETED"` -> 112, 2161, 2885, 3892, 4270 —
    all lineage/history. `grep -n "STRICT + hull-theta"` -> 3977,
    4288, 4552, 4560, 4574, 4648 — all §13 history/annotations.
 3. `grep -n "H-G8"` -> 89 lines, all inside declared edit sites
    (min body hit 2187, max 2905; §13 hits 4396-4492; block
    4703-4913; header 37/125; none in 135-2158, none in leg-3).
 4. `grep -n -E "evision 10|EVISION 10|R9-A|R9-B|R9-C|RES-DOC1"` ->
    59 lines, same containment (none between 135 and 2158).
 5. `grep -n "under which"` -> 2352, 3569, 4136, 4377, 4500, 4537,
    4542, 4715, 4846, 4907; in-delta grant-scoping instances: none
    outside full-set scope; 2352 = witness-regime clause (see §C).
 6. `grep -n "single-upcrossing"` -> 4381 only (history).
    `grep -n "three chart clauses"` -> 0 line-hits (the phrase
    survives only line-wrapped inside its own retirement sentence
    l.2396-2397). `grep -n -i "parity"` -> body hits only the
    retirement sentence l.2275-2276 (+ unrelated §2/§3 usage
    889/1025; rest history).
 7. `grep -n "thermal-stability"` -> 19 hits; every current-status
    carrier (108, 2659, 2880, 4859, 4914) chains to the (H-G8) form;
    rest history.
 8. Condition-name carriers: `grep -n -E "FULL STRONG SUFFICIENT|
    STRONG SUFFICIENT CONDITION|\(H-G8-1\)-\(H-G8-4\)"` -> 15 hits =
    the six declared carriers (125, 2180, 2581-2582, 2661, 2895-2896,
    4860) + consistent recitals (37, 4772-4773, 4836, 4913) +
    annotations (4393, 4428).
 9. Leg-3: anchors 1087/1440; `sed -n '1087,1439p' | wc -l` -> 353;
    `sed -n '1087,1439p' | head -c -1 | md5sum` ->
    6ef096f238ef76bc0ea8965cd066ef96 (matches the recorded value;
    raw-with-final-newline variant 0a186e9d252fc01bedb657e83013bc58).

## DEDUP REGISTER (standing dispositions checked, NONE re-opened)

r2-batch (revision 4: L0-1/L1-1/L1-2/L0-2) — untouched; rounds 1-4
(revisions 5-8: EL0-3/ESC1-F2/EL0-4, E2L0-1/E2L0-2, E3L0-1/E3L0-2/
ER2L1-1, E4L0-1..4/ER3L1-1..3) — untouched, their clauses recalibrated
to (H-G8) names where member attributions moved, each recalibration
verified sound; confirming round (revision 9: ECL0-1..3, ECR1-1..4) —
annotations preserve prior text, dispositions stand; closure round
(R9-A/R9-B/R9-C + §3(a) recital slip + §3(b) fiber reconciliation +
§3(c) count ruling) — consumed/carried faithfully, not re-litigated.
My two findings attach to REV-10-MINTED text only (the extended
equivalence gloss; the sweep-sentence unit/coverage) — neither has an
antecedent in any standing disposition; no orphan objection from any
input file remains on disk against this revision.

## R-4 BINDING-RULE AUDIT

Count of record: ELEVEN declared instances (VERDICT_doc1_closure
§3(c) adopted at block residue (3); the absorbing "eight-plus" stays
true). I audited every rev-10 carried phrase against the
transplant-calibration-misfit species: the R9-B modulo list is
recalibrated to the enlarged taxonomy WITH declaration (l.4757-4765 +
l.4489-4494); the R9-A member text is re-anchored to (H-G8) names;
the judge's "under which single-upcrossing DOES deliver" clause was
correctly NOT transplanted (its mechanism is retired; its conclusion
is re-derived at (D3), a stronger route); the judge's rev-9-calibrated
line numbers were re-verified before editing per the block's
declaration, and my anchor spot-checks confirm the post-edit numbers.
The one candidate new instance — R10L0-1's equivalence-gloss
extension (spec text carried with an unrecalibrated scope widening) —
I do NOT sustain as an R-4 instance: it misfits no context (the
member's declared two-conclusion structure absorbs it; no false claim
becomes operative), so it stays a WORDING finding, not a
transplant-calibration misfit. NEW R-4 INSTANCES SUSTAINED AT THIS
LENS: ZERO — the count of record stays ELEVEN.

## MACHINE SUMMARY

{lens: l0, findings: [{id: R10L0-1, class: WORDING, site:
"(H-G8-4) member l.2242-2248 + §13 R9-A entry meta-claim
l.4725-4731"}, {id: R10L0-2, class: WORDING, site: "REVISION 10 block
R9-C measured-sweep sentence l.4778-4794"}], breaks: 0, repairs: 0,
amendments: 0, wording: 2, leg3_zero_edit: true,
carriers_consistent: true}
