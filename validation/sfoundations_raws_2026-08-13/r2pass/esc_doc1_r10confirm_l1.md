# ESCALATION — DOC-1 REVISION-10 CONFIRMING ROUND, LENS L1

Date: 2026-08-19 (S-FOUNDATIONS-C2 window). Role: confirming refuter,
lens L1, over the REVISION 10 delta (delta = CONTENT) of
`validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md`.
Mandate: `r2pass/BRIEF_rev10_confirm.md`; consumption audited against
`r2pass/VERDICT_doc1_closure.md` (§1 R9-A/B/C adopted specs, §4
RES-DOC1-1/2, §5 falsifiers) and the ratified strategy
(`validation/ADVISORY_SfoundationsC2_prompt_2026-08-19.md` § PRIMA
AZIONE PARALLELA, sufficient-but-unoptimized grant). Inputs read IN
FULL this window: the verdict, the strategy paragraph, the §13
REVISION 10 block (l.4687-4917), every declared edit site with
surrounding consumers (header l.1-140; condition of record + members +
(D1)-(D7) l.2140-2420; sufficiency attributions, momentum block,
assembly splice, AUD-cp note, falsifier consequent, grant head, honest
status l.2420-2709; §9 gamma-table carrier l.2860-2914; §13 rev-9
annotations l.4370-4600). Independence: the other lens's file NOT
read. Paths relative to repo root; line numbers = on-disk this window.

==============================================================================
## A. SUFFICIENCY AT PEN GRADE (duty a) — VERDICT: DELIVERS

I re-derived every load-bearing step of the (D1)-(D7) chain myself
from the printed members (H-G8-1)-(H-G8-4) (l.2187-2267):

(D1) theta = e_S > 0 at EVERY point of dom e ((H-G8-2)) makes
e(v, .) strictly increasing on each S-slice PROVIDED the slice is an
interval — monotonicity from a positive derivative does NOT cross
slice gaps, so the interval half ((H-G8-2), implied by (H-G8-1):
slices of a convex set are convex) is genuinely load-bearing and is
correctly named. At most one root per slice. SOUND.

(D2) (H-G8-3) totality + (D1): exactly one root at every hull point;
single-valued chart; "each per-segment continuation lands on the DATA
root" is a tautology under a single chart. SOUND.

(D3) Box argument, re-derived in full: (v_0, S_0) in int N
((H-G8-3)); closed box B ⊂ int N ⊂ dom e; theta >= theta_min > 0 on
compact B (C^2 of (H-G8-1) gives continuity of e_S; positivity
pointwise from (H-G8-2)); the two displacement inequalities
e(v, S_0 ± delta) vs e(v, S_0) need {v} x [S_0-delta, S_0+delta] ⊂
dom e — inside B, granted; W -> (v(W), eps(W)) continuous on
{rho >= rho_min} (v = 1/rho, eps = E/rho - |m|^2/(2 rho^2)); with
eps(W_0) = e(v_0, S_0) (root identity) the sandwich
e(v(W), S_0-delta) < eps(W) < e(v(W), S_0+delta) follows for W near
W_0; strict monotonicity on the WHOLE slice — an interval containing
both [S_0-delta, S_0+delta] and S(W) — places THE root in
(S_0-delta, S_0+delta). Continuity DERIVED. C^2 upgrade: IFT on
F(W, S) = e(v(W), S) - eps(W), F_S = theta > 0 at (W_0, S_0) in the
open int N; the IFT branch coincides with the root map at hull points
by (D1) uniqueness. SOUND. Fiber endpoints are never read
((H-G8-3)'s positive distance from the boundary), so the
(H-G8-4)-noted boundary caveat is correctly discharged.

(D4) Compact image = continuous image of the compact hull. SOUND
(hull compactness is standing framework of record, used identically
by the closure judge's own spec — see dedup register).

(D5)-(D7) assembly: strict Legendre bridge (confirmed clean in the
rev-9 round, unchanged in mechanism, splice re-scoped); momentum
block 1/(rho theta) > 0 with theta read at hull-image points, which
lie in dom e by (H-G8-3) — attribution correct (l.2384-2386); boost
affinity (standing); uniform lambda_min > 0 from continuity of
Hess_W E ((H-G8-1) C^2 through (D3)'s C^2 chart) + strict PD of
Hess e at image points inside N ((H-G8-1) strictness clause; min of a
continuous positive function on the compact N is positive) + (D4)
compactness; Bregman double integral: E(V|U) =
int_0^1 (1-s) DW^T Hess_W E(W_s) DW ds >= (lambda_min/2)|DW|^2, all
segment points hull points by definition. Item (i) at ORDER ONE with
c = lambda_min/2: DELIVERED. Item (ii) flux smoothness: (H-G8-1)'s
C^2 through the C^2 chart: DELIVERED.

WITNESS HUNT INSIDE THE CLASS: none constructible — (D3)'s box
argument closes every route a moving-slice witness could take (the
witness would need a fiber-family jump, which forces either a
non-convex dom e, a fiber discontinuity, or image accumulation on
the boundary — each violating a printed member). The rev-10 text does
NOT misuse out-of-class-ness anywhere: W-A's exclusion (l.4394-4399,
f2 l.4826-4837) is stated as exclusion, never as proof of
sufficiency — sufficiency is carried by (D1)-(D7) alone
("FALLBACK MEMBERS IMPOSED: NONE", l.4742-4745). I verified W-A's
three member-violations independently: two disjoint strips are not
convex ((H-G8-1)); fibers [0,1] -> [10,11] jump at v = 1 ((H-G8-4));
branch-1 image accumulates at (1,1), and (1,1) is in NO strip
(v = 1 slice is [10,11], S = 1 not in it), so no compact N ⊂ dom e
contains the image ((H-G8-3)). All three CORRECT. The necessity
chains (m1)-(m3) each violate a strong member as claimed (e_SS <= 0
or det < 0 breaks PSD; rank-1 breaks strictness on N): the f3
sentence is TRUE. lambda_min > 0 chain: closed. Item-(i) order-one
bound: closed.

==============================================================================
## B. MANDATE CONSUMPTION (duty b) — VERDICT: CONSUMED AT EVERY CARRIER

R9-A (adopted spec, VERDICT §1) — carrier-by-carrier, each read this
window: member written as (H-G8-4) with the judge's spec text +
fallback branch incl. "the fallback waives NO other member"
(l.2242-2267); rev-9 "under which ... continuous" clause superseded
by the full restatement (continuity now DERIVED at (D3), the
strategy-ratified stronger move — subsumes the judge's re-scope);
assembly splice re-scoped, "by the three chart clauses" RETIRED
(l.2391-2401); falsifier-consequent enumeration carries (H-G8-4) in
the geometry bucket (l.2528-2531, jointly with R9-B); grant head
(l.2578-2607, jointly with R9-C); header audit line (l.124-132); §9
gamma-table carrier (l.2893-2906); honest status line (l.2656-2676);
AUD-cp note fiber clause — l0's description adopted per VERDICT
§3(b): closed-interval fibers [phi(T_min)+R ln v, phi(T_max)+R ln v],
v-continuous endpoints (l.2469-2476); §13 ECL0-1 delivery re-scope
(l.4384-4399) + falsifier addition closing the continuity sub-claim
hole with the moving-slice witness class (l.4419-4430); domain ladder
outermost rung slice-FAMILY regularity (l.4443-4450); rev-9
uniqueness-only fallback RE-BASED by annotation (l.4402-4406). ALL
judge-named carriers hit. Measured epithet/member greps: §D below.

R9-B — BOTH sites with the adopted scoping: body consequent
(l.2520-2542): root-quantifier content moved INTO the pin-delivered
enumeration ("hull-image states and S-roots are domain points the
whole-domain reading covers, R9-B of record"), modulo bucket =
geometry members only, uniqueness consequence kept with the interval
member (l.2539-2542); §13 rev-8 echo annotated (l.4481-4496), prior
text preserved. The bucket ENLARGEMENT by (H-G8-1)'s domain half is a
DECLARED recalibration (l.4757-4765) with the correct argument: the
judge's "ONLY" list was calibrated to the rev-9 + R9-A member list; a
member R9-B could not name cannot be excluded by it, and dom-e
convexity is domain geometry no pins-reading delivers (same witness
class). Leaving it out would have made the consequent FALSE —
the recalibration is mandatory, not optional. CONSUMED AS DEMANDED.

R9-C — route (a) of the judge's two, applied at ALL variants: the six
current-condition carriers all print the (H-G8-1)-(H-G8-4) form
(header audit line l.124-132; condition of record l.2180-2186; grant
head l.2581-2582; honest status l.2660-2661; §9 carrier l.2895-2896;
rev-10 label summary l.4860-4861); staged names survive only in
lineage/history contexts (my own extended sweep, §D — including
patterns the block's own grep did NOT cover: "hull-theta",
"DOMAIN-COMPLETED", "STRICT +", "strict condition of record": ZERO
stale current-condition naming found). §13 ECR1-3 annotation present,
naming the grant head as the missed sixth carrier (l.4569-4580).
CONSUMED.

Strategy conformance: the grant head declares NON-OPTIMIZATION and
gap-accounting status verbatim per the ratified strategy
(l.2587-2593); the four-member strong set matches the brief's own
enumeration (fiber-regularity included per R9-A); every granted item
claimed from the FULL set only. CONFORMAL. (One citation imperfection:
finding R10L1-4.)

==============================================================================
## C. FINDINGS (new-mint hunt, duty c; zero-edit, duty d; per-lens IDs)

### R10L1-1 — EDIT-SITE INVENTORY INCOMPLETE (class: AMENDMENT)
Site: §13 REVISION 10 block, EDIT-SITE LIST l.4796-4811.
Mechanism: the list is the block's complete-inventory instrument (it
closes with "NO OTHER BYTE TOUCHED"), and two revision-10 byte-ranges
fall outside it: (w1) the third ECL0-1 in-entry annotation
"[FALLBACK RE-BASED in revision 10 per R9-A: ... imposes root-map
continuity / image compactness DIRECTLY;]" at l.4402-4406 — the list
enumerates only "ECL0-1 delivery re-scope l.4384, ECL0-1 falsifier
addition l.4419" for that entry; (w2) the header recital range
"l.31-38" excludes the recital's final tokens on l.39 ("conclusions
again UNCHANGED — 2026-08-19)."). Witnesses: my marker sweep (§D,
command H) hits at 4402-4405 map to NO declared anchor; l.39 read
verbatim this window. Mitigation (why AMENDMENT, not REPAIR): the
fallback re-base edit is mandate-conformal and separately DECLARED in
the same block's R9-A mechanism entry ("the revision-9 uniqueness-only
fallback re-based, annotation at the ECL0-1 entry", l.4731-4733) —
the benign reading (one logical ECL0-1 re-scope, three brackets)
exists, the ECR1-3-style rescue; and the species is the ledger class
(ECL0-3/ECR1-4 precedent = AMENDMENT). No content defect: both edits
are exactly the mandated repairs. Repair spec: add the l.4402 anchor
to the list and correct the header range to l.31-39.

### R10L1-2 — SWEEP UNIT MISLABEL "18 token hits" (class: WORDING)
Site: §13 REVISION 10 block, R9-C entry l.4778-4788.
Mechanism: the recited measured sweep says "18 token hits"; the
measured unit is LINES. My re-run of the block's own pattern (§D,
command A): 18 line hits carrying 20 token instances — l.4779 alone
carries 3 pattern tokens (it quotes the grep pattern). The number is
wrong under its own declared unit. No classification consequence: the
block's bucket list enumerates exactly the 18 lines I measure, all
correctly classified lineage/history/self-quote, and the 2 surplus
tokens sit on the self-quoted pattern line the block already
classifies. Repair: "18 line hits (20 token instances)".

### R10L1-3 — (H-G8-4) "EQUIVALENTLY" OVER-EXTENDED (class: WORDING)
Site: condition of record, (H-G8-4) member statement l.2242-2248.
Mechanism: the member prints "... fiber endpoints continuous in v,
fibers closed intervals — equivalently the hull's (v, S)-image is
COMPACT and the root map W -> S(W) is continuous on the compact
hull". The judge's adopted spec had ONLY image compactness inside the
equivalence and root-map continuity as a DELIVERED conclusion ("under
which single-upcrossing DOES deliver..."). As a bare biconditional
the printed form is not literal: fiber regularity is domain geometry;
root-map continuity additionally consumes (H-G8-2)/(H-G8-3) content.
Why WORDING (no consumer harm, checked at every reader): in-class
both sides are THEOREMS ((D3)-(D4)), so the equivalence carries no
derivational load; the fallback branch imposes both conclusions
DIRECTLY (l.2261-2267), never deriving one from the other; the AUD-cp
closure discharge runs through the (D1)-(D7) chain with directly
verified members (l.2485-2490), not through the equivalence. R-4
relevance: see §F — flagged as a CANDIDATE spec-mutation instance,
my recommendation below-threshold. Repair (optional): scope the
clause, e.g. "equivalently (within the condition) ...", or restore
the judge's two-part form.

### R10L1-4 — NON-OPTIMIZATION SECONDARY CITATION UNRESOLVED (class: WORDING)
Sites: grant head l.2590-2591 ("ratified strategy of record +
VERDICT_doc1_closure §4 orchestrator note"); strategy declaration
l.4710-4711 ("(VERDICT_doc1_closure §4 orchestrator note)").
Mechanism: VERDICT_doc1_closure §4, read in full this window,
contains NO note stating that weaker sufficient sets are possible and
not sought; its only orchestrator mentions are the RES-DOC1-1 owner
clause and "any re-opening is a NEW user/orchestrator decision" —
neither carries non-optimization content. The load-bearing authority
(the ratified strategy paragraph, "SUFFICIENTE-NON-OTTIMIZZATA ... la
riga è contabilità di gap, non teoria portante") is real, correctly
cited, and sufficient on its own. The surplus citation points at a
locus that does not resolve. Repair: drop the secondary citation or
re-anchor it to the actual carrier of the grant (the advisory
strategy paragraph; or the orchestrator's commissioning instruction
if that is the intended referent — then name THAT, not the verdict).

NO FURTHER FINDINGS. Hunted and NOT sustained (each checked to
convergence this window): carrier-enumeration divergence between the
six-carrier claim and my extended sweep (none — §D); epithet drift
(none); falsifier-list/member mismatch ((f1)-(f5) each audited
against the four members: (f2)'s three violation claims re-verified
independently, (f3)'s out-of-class claims re-verified for
(m1)/(m2)/(m3), (f5)'s two witnesses cover exactly the four geometry
members); "under which" scoping to less than the full set (the only
current-text instance outside the block, l.2352, scopes a WITNESS
regime clause, not a granted item — the f4 falsifier does not fire);
meta-claims without measured sweeps (the epithet sweep, the leg-3
hash, and the under-which audit are all cited and all REPRODUCED in
my window — §D; the leg-3 MD5 reproduces under the join-without-final-
newline convention, see §D command F2, which cost four probe variants
to identify: recommend the M0-landing pass pin the exact command).

==============================================================================
## D. SCOPE-SWEEP DECLARATION (measured in MY window, Git Bash, repo file
`validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md` = $F)

(A) Block's own epithet pattern, re-run:
`grep -n -i -E "chart-complete|topology-complete|chart-completed|topology-completed" "$F"`
= 18 line hits (115, 118, 2165, 2167, 2887, 2890, 4186, 4288, 4561,
4567, 4574, 4575, 4648, 4649, 4679, 4720, 4779, 4780) — the block's
classification buckets reproduce line-for-line;
`grep -o -i -E ... | wc -l` = 20 token instances (l.4779 carries 3).
Basis of R10L1-2.
(B) Extended staged-name residue hunt (patterns the block did not
sweep): `grep -n -i -E "hull-theta|DOMAIN-COMPLETED" "$F"` = 39 hits,
all in lineage recitals (115/2161/2211/2524/2560/2651/2885), §13
history blocks (3710-4680), or rev-10 annotations quoting retired
names (4753); `grep -n -E "STRICT \+" "$F"` = 6 hits, all
history/annotation-quoted; `grep -n "condition of record" "$F"` = 23
hits — the two current-text operative uses (2329 = rev-6/7 lineage
narrative inside the sufficiency parenthetical; 2378 = the defined
singular object, unqualified) carry no stale epithet.
`grep -n "thermal-stability" "$F"` = 18 hits: current-text sites
(108, 2659, 2880, 4859, 4914) all resolve to the (H-G8) form; the
rest are §13 history. ZERO stale current-condition naming =>
carriers_consistent.
(C) Carrier map: `grep -n "H-G8" "$F"` = 89 hits, bucketed: header
audit line, condition of record + (D1)-(D7), sufficiency
attributions, momentum block, assembly splice, AUD-cp, consequent,
grant head, honest status, §9 carrier, §13 rev-10 annotations, and
the REVISION 10 block. All six claimed current-condition carriers
print the taxonomy; no seventh naming carrier found.
(F2) Leg-3 zero-edit (duty d): anchors measured
(`grep -n "## §4 The uniqueness half\|## §5 The main theorem"` =
1087 / 1440); `sed -n '1087,1439p' "$F" | wc -l` = 353 lines (matches
the block); marker sweep INSIDE the span
(`sed -n '1087,1439p' | grep -n -E "H-G8|R9-|revision 10|VERDICT_doc1_closure|RES-DOC1|fiber"`)
= ZERO hits; MD5: raw-span md5sum = 0a186e9d252fc01bedb657e83013bc58,
and with the final newline stripped
(`sed -n '1087,1439p' "$F" | perl -0pe 's/\n\z//' | md5sum`) =
6ef096f238ef76bc0ea8965cd066ef96 — EXACTLY the block's printed hash:
the zero-edit proof REPRODUCES byte-for-byte under the
join-without-trailing-newline extraction convention.
leg3_zero_edit = TRUE.
(H) Whole-file rev-10 marker sweep (duty d, non-mandate motion):
`grep -n -E "R9-A|R9-B|R9-C|revision 10|REVISION 10|VERDICT_doc1_closure|RES-DOC1|fiber regularity|FIBER REGULARITY|fiber-regularity|H-G8|SUFFICIENT-BUT-UNOPTIMIZED|sufficient-but-unoptimized" "$F"`
= 160 hits; every hit maps into a declared edit site or the §13
REVISION 10 block EXCEPT l.4402-4405 (the R10L1-1 witness — itself a
mandated rev-10 edit, only its anchor is missing from the list). No
non-mandate passage moved by this sweep. Declared caveat: a
markerless edit would evade a marker sweep — coverage beyond markers
rests on (i) the leg-3 hash (byte-exact, reproduced), (ii) verbatim
re-reads of every declared site and its surround this window, (iii)
the §13 history blocks' prior text spot-checked against the judge's
rev-9-verified quotes (no drift found where quoted).
(I) Under-which audit: `grep -n "under which" "$F"` = 10 hits;
current-text: 2352 only (witness regime clause, not a grant);
4715/4846/4907 = the block's own meta-claims; the rest §13 history.
The f4 discipline claim HOLDS on the measured set.

==============================================================================
## E. DEDUP REGISTER (standing dispositions checked — NONE reopened,
no orphan objection)

- r2-batch (L0-1/L1-1 leg 3; L1-2/L0-2 leg 5): leg-3 body byte-identical
  (hash reproduced); L1-2/L0-2 consumption texts preserved inside the
  restated row. Not reopened.
- Rounds 1-4 (EL0-3/EL0-4; E2L0-1/E2L0-2; E3L0-1/E3L0-2/ER2L1-1;
  E4L0-1..4/ER3L1-1..3): strict form, hull-theta subsumption, totality,
  Legendre bridge (l.2365-2377), ECR1-2 determinant-regime clause
  (l.2350-2362), consequent lineage — all preserved under the lineage
  compression. Not reopened.
- Confirming round (ECL0-1..3, ECR1-1..4): entries annotated in place,
  prior text preserved (verified at 4384/4402/4419/4443/4481/4569);
  ECL0-3/ECR1-4 ledger corrections untouched. Not reopened.
- Closure round (R9-A/B/C = RES-DOC1-1/2): the audited delta — consumed,
  §B. Judge §3(a) recital slip (l1 S_U value): moot under the
  restatement (W-A carried as out-of-class exhibit only, values
  quoted correctly at l.4388-4391). Judge §3(b) fiber reconciliation:
  the AUD-cp clause adopts l0's (v, S)-image description as ruled.
- "the compact hull" premise in (D4)/(D5)-(D7): STANDING framework
  carried from rev <= 9 and used verbatim by the closure judge's own
  R9-A spec ("root-map continuity on the compact hull") — registered
  as standing, not attackable as rev-10 delta; noted that (H-G8-3)'s
  compact-neighborhood clause independently forces image
  boundedness.
- My four findings target artifacts MINTED by the revision-10
  restatement/block itself (inventory, sweep recital, member wording,
  citation) — none restates or reopens a prior lens's objection; ID
  space disjoint by prefix rule.

==============================================================================
## F. R-4 BINDING-RULE AUDIT

Count of record: ELEVEN declared instances (VERDICT_doc1_closure
§3(c), l1 enumeration adopted) — correctly transcribed at honest
residue (3) (l.4896-4901), absorbing form "eight-plus" intact. Hunt
over the rev-10 text for NEW transplant-calibration misfits: the
block's self-audit claims every carried phrase recalibrated, and the
two big recalibrations check out (R9-B modulo bucket enlarged WITH
declaration, l.4757-4765; judge's "under which" clauses subsumed by
the full-set restatement). ZERO new instances SUSTAINED by this lens.
ONE CANDIDATE flagged for the judge: R10L1-3 — the (H-G8-4)
"equivalently" fold extends the judge's spec-calibrated equivalence
(fiber regularity ~ image compactness) to swallow the delivered
conclusion (root-map continuity); it is the spec-mutation species
(the ECL0-2 lineage runs transplant-AND-INVERT; this is
transplant-AND-EXTEND) but with NO located consumer harm and with the
self-audit's "re-anchored to (H-G8) names" partially covering it. If
the judge sustains it as an instance it numbers TWELVE; my
recommendation: below threshold (WORDING repair suffices). The
next-round lesson stands: attack revision-10 text as
strategy-and-spec-derived text — which this lens did (all four
findings are restatement-minted artifacts, none mathematical).

==============================================================================
## MACHINE SUMMARY

{lens: l1, findings: [
 {id: R10L1-1, class: AMENDMENT, site: "S13 REVISION 10 EDIT-SITE LIST l.4796-4811 (omits l.4402-4406 FALLBACK-RE-BASED anchor; header range l.31-38 excludes l.39 tail)"},
 {id: R10L1-2, class: WORDING, site: "S13 REVISION 10 R9-C entry l.4778-4788 ('18 token hits' = 18 line hits / 20 tokens)"},
 {id: R10L1-3, class: WORDING, site: "condition of record (H-G8-4) l.2242-2248 ('equivalently' folds root-map continuity into the fiber-geometry equivalence)"},
 {id: R10L1-4, class: WORDING, site: "grant head l.2590-2591 + block l.4710-4711 ('VERDICT_doc1_closure §4 orchestrator note' citation does not resolve)"}
], breaks: 0, repairs: 0, amendments: 1, wording: 3,
leg3_zero_edit: true, carriers_consistent: true}

END — lens L1, revision-10 confirming round.
