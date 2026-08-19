# ESCALATION REFUTATION — DOC-3 r3.3 repair text, until-dry ROUND 3, lens l0

Lens: hyperbolic-systems / functional-analytic rigor. Date: 2026-08-19.
Target: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md`,
ATTACK SCOPE STRICTLY = the NEWEST revision-log entry's edited passages —
the r3.3 (until-dry ROUND 2 continuation, 2026-08-19) repairs to the E-4
leg-14 text: the face-dependent "why this does not prove too much"
paragraph + its superseding annotation (ESC2-1/ESC2-2), the corrected
"Which (H-UP) form" straddling parenthetical (ESC2-3), the rederived
falsifier window arithmetic + register-row-1' mirror (ESC2-4), the Status
(a) scoping (ESC2-5), and the r3.3 revision-log/reconciliation block —
plus the mandated re-verification of the leg-17 amendment A-2 chain
(Remark 1.5.5; r3.3 did not touch it, standing r3.2 text re-verified).
Machine sweep of scope: `grep -n "r3\.3"` on the target = lines 14, 154,
163, 192-198 (log), 693 (ESC2-3), 826/848 (ESC2-1/2), 882 (ESC2-5),
922 (ESC2-4), 1814 (register row 1'); all examined below.

**FILENAME/ROUND DEVIATION, DECLARED.** The launching brief named "until-dry
ROUND 2" and output file `esc_doc3_r2_l0.md`. On disk, that round is already
consumed: `esc_doc3_r2_l0.md` (ESC2-1..5, 2026-08-19) exists and is cited
IN FULL — with its exact objection counts — by the target's r3.3
revision-log entry, the very repair text this brief mandates attacking
("the newest revision-log entries name the edited passages"; the newest
entry is r3.3, which consumes ESC2-1..5). Overwriting the cited of-record
round-2 carrier would falsify the audit chain (SR-6/SR-10 class violation;
identical precedent: the round-2 slot received a brief naming "ROUND 1" and
deviated the same way, declared in its own header). This refutation is
therefore the ROUND-3 lens-l0 output, written to `esc_doc3_r3_l0.md`;
nothing else in the brief is deviated from. Note of record: round 2 ran
lens l0 only (no `esc_doc3_r2_l1.md` exists); this round likewise covers
the l0 lens.

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 (L0-7/L1-7
SUSTAINED-BREAKS, L1-8 SUSTAINED-AMENDMENT), §3 (A-2), §4(c) (E-4), §5
(falsifiers incl. the proves-too-much test). Full objection texts consumed:
`refute_r2batch_l0.md` L0-7, `refute_r2batch_l1.md` L1-7/L1-8;
prior escalation rounds `esc_doc3_r1_l0.md` (ESC-L0-1..7),
`esc_doc3_r1_l1.md` (F-1..F-6), `esc_doc3_r2_l0.md` (ESC2-1..5) — the
round whose r3.3 dispositions this round verifies.

DEDUP DECLARATION: no dispositioned objection is re-raised at its own
content. L0-7/L1-7/L1-8, ESC-L0-1..7, F-1..F-6, and ESC2-1..5 are engaged
ONLY through discharge verification (§1); no disposition is attacked as
failed this round — all five r3.3 dispositions are ADEQUATE (first round
of this escalation with zero inadequate dispositions). Every objection
below targets r3.3-NEW text with zero prior adversarial coverage.

==============================================================================
## §1 DISCHARGE VERIFICATION (r3.3 repairs vs the objections they answer,
## chained back to the sustained originals)

**ESC2-1 (proves-too-much wrong face) — DISCHARGED.** The rewritten
paragraph is now face-correct and face-dependent, verified at pen grade:
(i) geometry re-derived — Omega_int^{h/2} := Omega_up \ closure(C_{h/2})
and Gamma_in^coll = {x = x_I - h} lies strictly upstream of Gamma_mid
(x_I - h/2), so Gamma_in^coll IS interior to (H-UP-fam)'s domain
Omega_int^{h/2}, exactly as bullet 1 now states (and consistent with the
ESC-L0-3 log row it re-closes); (ii) the quantifier claim is now TRUE:
(H-UP-fam)'s states at depth h/2 solve the interior problem on
Omega_int^{h/2} ∋ Gamma_in^coll, hence across THAT face; (iii) the repair
excludes ESC-L0-3's strengthened bare-coupling instance by the correct
mechanism (a bare interior-side hypothesis lives on Omega_int^h, stopping
AT Gamma_in^coll, inapplicable on the enlarged domain), and I verified the
exclusion is ROBUST over the F-2-restricted family: for EVERY admissible
depth s < h, Omega_int^s contains Gamma_in^coll in its interior — the
would-be prover cannot dodge by re-choosing the mid-face (s = h is dropped
of record, d_0(h) = 0); (iv) the r3.2 paragraph is retained verbatim in
the annotation with its three recorded defects, matching ESC2-1's three
prongs word-for-substance. Strongest attack tried: hunt for a coupling
face the new two-bullet taxonomy leaves unexcluded — found one class
(faces already interior to Omega_int^h), which does NOT re-open ESC2-1
(the conclusion and both printed mechanisms stay correct on their faces):
ESC3-1 below. CHECK.

**ESC2-2 (false universal "never Step 1") — DISCHARGED.** The universal is
replaced by the face-dependent statement; bullet 2 now carries the
Gamma_mid bare coupling with STEP 1 as the operative exclusion (frusta
straddle the face, no single C^1 solution of the homogeneous system to act
on, (MID-TRACE) never available) and the parenthetical closes the
STEP-3-route escape exactly as ESC2-2 demanded (the interior-side member
is (H-UP-fam)-admissible — it solves across Gamma_in^coll, interior to its
domain). Re-derived: for such a coupling STEP 1 fails FIRST and STEP 3's
inputs never materialize. The superseded clause is recorded in the same
annotation. CHECK.

**ESC2-3 ("nothing straddles any face") — DISCHARGED.** The corrected
block now reads "nothing straddles a DATA-CARRYING face (Gamma_in^coll or
Gamma_I)" with the frusta's Gamma_mid-straddling stated as STEP 1's
mechanism and Gamma_mid's trace identified as STEP 1's OUTPUT — ESC2-3's
demanded wording, verbatim in content. Strongest attacks tried: (α) do the
frusta touch Gamma_I or Gamma_in — no (R < d_0 keeps them clear of both
collar data faces; Gamma_in is unreachable from inside C_h); (β) is
Gamma_in a "data-carrying face" missing from the parenthetical's
enumeration — immaterial: the enumeration is scoped to C_h's faces, the
only ones a frustum inside C_h could straddle. CHECK.

**ESC2-4 (window arithmetic) — DISCHARGED as to both prongs, one NEW
narrow defect in the repair's own contaminant labeling (ESC3-3).**
Prong (i) (collar constant applied to the exterior): the rederivation
routes through the TERMINAL COLLAR SEGMENT and I verified the path bound
at pen grade — any influence path from Gamma_in^coll ∪ Gamma_I to
Gamma_mid, after its LAST crossing of Gamma_in^coll ∪ Gamma_I, stays in
closure(C_h) (∂C_h consists of those two faces plus wall portions, and
walls cannot be crossed), and that terminal segment has length
≥ dist(Gamma_mid, Gamma_in^coll ∪ Gamma_I) = d_0 where lambda_max is
theorem-grade (Lemma 1.4, collar base unroughened) — arrival
≥ t_p + d_0/lambda_max = t_p + 2× the probed window d_0/(2 lambda_max),
regardless of exterior speeds. Non-circularity checked: Gamma_I is treated
as a possible entry face (Theorem 1' is NOT assumed). Prong (ii) (vacuous
t_p case): the repair now reasons from post-t_p contamination — but its
labeling of the downstream contaminant is wrong in a way prong (ii)'s fix
should have caught: ESC3-3 below. The register row 1' falsifier cell
(line 1814) mirrors the terminal-collar-segment derivation verbatim in
condensed form — the r3.3 disposition's mirror claim is TRUE. The
superseded r3.2 sentence is retained with both defects named. CHECK
(modulo ESC3-3, a defect of the new sentence, not of the repair's
mechanism).

**ESC2-5 (Status (a) unscoped class) — DISCHARGED as to the class
scoping.** Case (a) now quantifies over (H1.4)-grade (C^1) pairs of the
delegated class, with H^1 members via 1.5.3 (THEOREM* modulo NG-3, corner
inventory extended to the Gamma_mid ∩ Gamma_w curves — exactly ESC2-5's
named repair, new-corner clause included); the r3.2 unconditional
quantification is retired by annotation. Strongest attacks tried: (α)
characteristic-transition loci ON Gamma_mid (points where u-bar·n crosses
{0, ±c-bar}) as a residual 1.5.3 never inventoried — fails to bite at the
scoped grades: for C([0,T_f]; H^1) members the L^2 boundary trace on the
Lipschitz face exists by the trace theorem independently of A(n)'s
characteristicity there, and the (EI) boundary pairing passes to the
mollification limit by trace continuity (Rauch 1985 is needed only for the
uniformly characteristic WALL portions, unchanged from 1.5.3's own
inventory); (β) does the (EI) run on Omega_int^s consume the wall
structure on INTERIOR walls (Gamma_w ∩ ∂Omega_int^s) that Prop 1''s
Claim never hypothesizes ((H1.2) is assumed on Gamma_w ∩ ∂C_h only) —
fails to bite: (H-UP-fam)'s interior problem is DEFINED with "slip walls"
(its own enumeration line), so the wall-term kill via (BQ)
(u-bar·n = 0 kills the advective part, u'·n = 0 kills 2p'(u'·n)) is part
of the problem definition case (a) proves uniqueness FOR. One enumeration
defect survives in the same edited sentence — the base-state BOX clause:
ESC3-2 below. CHECK (modulo ESC3-2).

**Chain to the sustained originals — re-verified this round.** L0-7(a)
(quantifier order): eps_1 = d_0/(2 lambda_max) is a (D-coll)+collar
constant, eps_1' = min(eps_1, T_f − t*) > 0 keeps the window in-domain,
and STEP 1's R-choice survives (lambda_max·eps_1' ≤ d_0/2 < d_0) — still
DISCHARGED. L0-7(b) (trace on the source face): the only concluded trace
is on Gamma_mid at distance ≥ d_0 from both uncontrolled-data faces —
still DISCHARGED. L1-8/A-2 (leg 17): r3.3 did not touch Remark 1.5.5;
the standing r3.2 text re-verified by direct spectrum computation
(u·n = 0: {−c, 0(×3), +c}; u·n = −c: {−2c, −c(×3), 0}; adjacent distinct
gaps = c-bar, all pairwise separations ≥ c-bar, extreme pair 2c-bar;
multiplicity pattern (1,3,1) constant, projectors regular; the flipping
object is the mode-CLASS at the zero crossing of one regular eigenvalue)
— A-2 remains fully landed. CHECK.

**r3.3 reconciliation block (log lines 163-198) — verified.** The
state-integrity outcomes match the live text at every spot-checked anchor:
(cl-C)/(cl-F) in the Claim, eps_1' threading, STEP-2 checklist with
"(H1.4) on C_{h/2} by restriction", (D-coll) Lipschitz clause, F-2
restricted quantifier with s = h dropped, F-4 corrected attribution block,
F-6 adjacent-gaps wording, register row 1' mirrors. The header's counts
("ESC2-1..5 = 0 BREAKS + 1 REPAIR-NEEDED + 4 AMENDMENT") match the round-2
file; "NO step of the two-face proof moved this round" is TRUE (the proof
body carries r3.2 markers only — STEPs 1-3, UNION, Claim, (H-UP-fam)
unchanged since round 2's C-block confirmed them). CHECK.

**Residue:** the two-face proof (STEPs 1-3 + UNION with
(cl-C)/(cl-F)/eps_1') again survives this lens's strongest attacks — no
proof step moved and no new attack on the unchanged steps succeeded (§3).
The three surviving defects live in the honesty paragraph's case coverage,
the falsifier sentence's contaminant labeling, and one hypothesis clause
of the Status-(a) premise — none touches a proof step; the
SCHEMA-per-J-r2p-1 label discipline is intact.

==============================================================================
## §2 OBJECTIONS (r3.3 text; verbatim quote + attack + class)

------------------------------------------------------------------------------
**ESC3-1 — class AMENDMENT. The face-dependent taxonomy's two bullets do
not exhaust the bare-coupling faces the paragraph's universal test ranges
over: couplings across faces ALREADY interior to Omega_int^h fall under
neither bullet, and bullet 1's stated mechanism (the enlargement) is not
the operative exclusion there.**

Quote (Section 1.6, "Why this does not prove too much", r3.3):
> "The exclusion is FACE-DEPENDENT: every face of the two-face
> decomposition is crossed by a certified structure, and a bare coupling's
> face is crossed by nothing.
> - *Coupling across Gamma_in^coll (the r2 configuration; ESC-L0-3's
>   strengthened bare-coupling instance):* the operative exclusion is
>   STEP 3's DOMAIN ENLARGEMENT. [...]
> - *Coupling across a face interior to C_h (e.g. Gamma_mid itself):* the
>   operative exclusion is STEP 1's requirement of certified TWO-SIDED
>   regularity across the face [...]"

Attack (derivation level). The judge's §5 test quantifies over ANY
"transmission coupling with no transmission condition" (retraction-grounds
text, same section). Take the coupling face Gamma'' strictly UPSTREAM of
Gamma_in^coll, interior to Omega_int^h (e.g. planar {x = x_I − 2h}, two
subdomains joined there, no transmission condition). This face is neither
Gamma_in^coll (bullet 1) nor interior to C_h (bullet 2). Run the proof on
a glued pair: STEP 1 runs (the pair is a single C^1 solution on all of
C_h — the coupling face is outside C_h); STEP 2 runs; STEP 3 fails —
but NOT by the enlargement mechanism bullet 1 states: Gamma'' was interior
to Omega_int^h ALREADY, no enlargement needed; the exclusion is
(H-UP-fam)'s bare class quantification (its states solve the interior
problem on all of Omega_int^{h/2}, hence across Gamma''; the glued
restriction does not, and the bare coupling supplies only piecewise
uniqueness on the two pieces with the Gamma'' trace-feed uncontrolled —
the r2 circularity reproduced INSIDE the interior domain). So the
paragraph's case analysis, as the carrier of the judge's universal test,
is incomplete by one (easy) case, and an adjudicator running the test on
this instance finds neither bullet's mechanism applicable as printed.
Fix (one clause, rides the existing bullets): "for a coupling across a
face already interior to Omega_int^h, no enlargement is needed — the
exclusion is (H-UP-fam)'s class quantification itself (its states solve
the PDE across every face interior to its domain)". Not REPAIR: no proof
step consumes the paragraph, both printed bullets are correct ON THEIR
faces, and the conclusion (the derivation does not prove too much) is
TRUE — I verified it on the missing case through exactly the clause
above. AMENDMENT.

------------------------------------------------------------------------------
**ESC3-2 — class AMENDMENT. Status (a)'s premise drops the (G3)-box half
of the global-regularity hypothesis: "W^{1,infinity} on all of Omega_up"
alone does not deliver the symmetrizer bounds the (EI)/Gronwall run
consumes.**

Quote (Section 1.6, Status of (H-UP-fam), case (a), r3.3-edited sentence):
> "(a) If W-bar is W^{1,infinity} on all of Omega_up, (H-UP-fam) IS a
> theorem of this document at every depth with a given (D-coll)-class
> split, FOR PAIRS OF (H1.4)-GRADE (C^1) MEMBERS of its delegated
> solution class [...]"

Attack (hypothesis accounting; the sentence is the r3.3-rewritten unit).
The document's own convention states regularity and box membership as
SEPARATE conjuncts everywhere: (H1.1) is "W^{1,infinity}(...) , values in
the (G3) box"; (H1.1') is "W^{1,infinity}(C_h x [0,T_f]) with (G3)-box
values ON C_h ONLY". Case (a)'s premise carries only the W^{1,infinity}
half. The (EI) run it sketches on Omega_int^s needs the symmetrizer
S(W-bar) uniformly positive-definite and bounded (coercivity of the energy,
Gronwall constants) — that is BOX membership (rho, p, c^2 bounded away
from the vacuum/degenerate boundary), not Lipschitz regularity: a
W^{1,infinity} base state drifting to c-bar^2 -> 0 or rho-bar -> 0 in the
far interior satisfies the printed premise while (EI) loses coercivity
there and no theorem of this document delivers the uniqueness. The
Claim's inherited hypotheses supply the box on the COLLAR only ((H1.1')),
so nothing closes the gap on Omega_int^s \ C_h. Same defect class the
round-1 loop sustained at STEP 2 (ESC-L0-6: consumed-but-unlisted
hypothesis) and the round-2 loop sustained at this very sentence (ESC2-5:
over-wide quantification). Fix (three words): "If W-bar is
W^{1,infinity} on all of Omega_up WITH (G3)-BOX VALUES, ...". Load-bearing
only for the smooth-base sanity reduction (case (b)/NG-9 untouched);
AMENDMENT.

------------------------------------------------------------------------------
**ESC3-3 — class AMENDMENT. The rederived window arithmetic labels the
downstream contaminant "POST-t_p growth in the deliberately ROUGHENED
exterior" — but downstream of Gamma_I the pinned trigger constrains
NOTHING: the injected pulse is a PRE-EXISTING above-bound contaminant AT
t_p, and it is the pulse, not the roughening, that lives there.**

Quote (Section 1.6, falsifier, r3.3):
> "under the pinned trigger the field is at the bound on ALL of Omega_up
> at t_p, so the operative contaminant is POST-t_p growth in the
> deliberately ROUGHENED exterior (downstream of Gamma_I or upstream of
> Gamma_in^coll), where NO speed bound is hypothesized or monitored"

Attack (executor level — the falsifier-correctness discipline of R5, the
class ESC2-4 itself occupied). The trigger is pinned to Omega_up ("the
field on ALL of Omega_up — collar C_h INCLUDED"). The region downstream of
Gamma_I is OUTSIDE Omega_up, and in this very run it carries the injected
downstream pulse — above the scheme bound AT t_p, deliberately and
legitimately (it is the falsifier's probe signal). Two mislabels in one
parenthetical: (1) for the downstream half, the operative contaminant is
NOT "post-t_p growth" — it pre-exists t_p; the inference "the field is at
the bound on ALL of Omega_up at t_p, SO the operative contaminant is
post-t_p growth" is valid only for the upstream exterior (which IS in
Omega_up); (2) "the deliberately ROUGHENED exterior" — the roughening of
record is of the base state in Omega_up outside the collar ("a steep
interior layer mimicking a slip line"); downstream of Gamma_I is the
PULSE region, not the roughened region. An executor reading the sentence
literally would wait for exterior "growth" and could ignore the standing
pulse as an already-present contaminant when timing the window. The
ARITHMETIC is unaffected — I re-derived it for the pre-existing pulse:
above-bound influence cannot be inside closure(C_h) at t_p (trigger), so
its collar entry still occurs at time ≥ t_p and the terminal-collar-
segment bound gives arrival ≥ t_p + d_0/lambda_max unchanged. Fix (one
clause): "the operative contaminant is the standing downstream pulse
(above bound at t_p OUTSIDE Omega_up, which the trigger does not
constrain) and any post-t_p growth in the roughened upstream exterior".
Mirror check: register row 1''s condensed cell says only "post-t_p
contaminant arrival >= ..." — compatible with the fix (no separate row
repair needed if "post-t_p" is read as arrival-time, but the body
sentence must change). AMENDMENT.

==============================================================================
## §3 CONFIRMED passages (strongest attack tried, each)

**C3-1 — Bullet 1 (Gamma_in^coll exclusion by enlargement): CONFIRMED.**
Attacks tried: (α) geometry — is Gamma_in^coll really interior to
Omega_int^{h/2} (yes: strictly upstream of Gamma_mid, outside
closure(C_{h/2})); (β) can the would-be prover of the bare-coupling
"uniqueness" evade by choosing a different depth so the coupling face is
NOT internalized — no: every admissible depth s < h internalizes
Gamma_in^coll, and s = h is dropped of record (F-2, d_0(h) = 0); (γ) does
the new text repeat ESC2-1's false quantifier claim — no: "the states
(H-UP-fam) quantifies over solve the PDE ACROSS Gamma_in^coll" is true at
depth h/2 (their domain contains the face); (δ) the distance clause "the
only trace the proof consumes is on Gamma_mid, at distance >= d_0 from it"
— exact per (D-coll)'s definition of d_0.

**C3-2 — Bullet 2 (Gamma_mid exclusion by STEP 1) + its parenthetical:
CONFIRMED.** Attacks tried: (α) does STEP 1 really fail for the Gamma_mid
bare coupling (yes: the glued difference is not a C^1 solution of the
homogeneous system on the frusta, which straddle the face); (β) is the
parenthetical's admissibility claim right (yes: the interior-side member
solves the interior problem on Omega_int^{h/2}, across Gamma_in^coll,
interior to its domain) — and does it contradict the log row's "is
(H-UP-fam)-admissible" ("can be" body vs "is" row: the row speaks of the
specific witness instance; consistent); (γ) tension with ESC2-2's
falsifier — none: the exclusion IS derived through Step 1's failure.

**C3-3 — r3.3 superseding annotation (lines 848-871): CONFIRMED.**
Attacks tried: quote fidelity of the retained r3.2 paragraph against
`esc_doc3_r2_l0.md`'s verbatim quote (matches); the three recorded defects
against ESC2-1's three prongs (match in substance, none weakened in
transcription); the closing sentence's claim that the conclusion "was true
in all three printings" (true — verified independently each round); the
statement that the r3 annotation retiring "Step 1 is unavailable" stands
(consistent: that sentence did fail on the Gamma_in^coll instance).

**C3-4 — corrected "Which (H-UP) form" parenthetical (ESC2-3 repair):
CONFIRMED.** Strongest attack tried: hunt for a data-carrying face a
frustum could still straddle — none (R < d_0 clears Gamma_in^coll and
Gamma_I; Gamma_in unreachable from C_h; walls are frustum-admissible
boundary, not straddled); the OUTPUT/input characterization of Gamma_mid's
trace is exactly STEP 1's logical role.

**C3-5 — terminal-collar-segment window bound (ESC2-4 repair, mechanism):
CONFIRMED.** Attacks tried: (α) can an influence path shortcut outside
closure(C_h) after last touching Gamma_in^coll ∪ Gamma_I — no (∂C_h =
those faces + walls; walls impassable); (β) is lambda_max still
theorem-grade in the roughened run — yes (roughening is outside the
collar; lambda_max is a collar sup over the unroughened base); (γ)
circularity via Gamma_I (assuming Theorem 1' to bound entry) — absent:
Gamma_I is treated as an entry face; (δ) arithmetic — d_0/lambda_max =
2 × d_0/(2 lambda_max), exact; (ε) pre-t_p entry — covered: above-bound
presence in the collar at t_p is excluded by the pinned trigger itself.

**C3-6 — register row 1' falsifier cell (r3.3 mirror): CONFIRMED.** Read
against the body: the cell carries the pinned Omega_up-inclusive trigger,
the fixed d_0/(2 lambda_max) window, and the terminal-collar-segment
derivation with "collar-only speed bound, exterior speeds unconstrained
(r3.3, ESC2-4)" — a faithful condensation; hypotheses/rigor cells carry
(cl-F)/(cl-C) and SCHEMA-per-J-r2p-1 unchanged.

**C3-7 — Status (a) class scoping + 1.5.3 extension clause (ESC2-5
repair): CONFIRMED** modulo ESC3-2 (a different clause of the same
sentence). Strongest attacks tried: (α) characteristic-transition loci on
Gamma_mid as an uninventoried mollification residual — fails at the scoped
C^1/H^1 grades (L^2 traces on a Lipschitz face exist by the trace theorem
independently of A(n)'s characteristicity; Rauch 1985 is consumed only for
the wall portions, as in 1.5.3); (β) interior-wall structure unhypothesized
— fails: "slip walls" is part of (H-UP-fam)'s own interior-problem
definition, so (BQ) kills the wall terms within the problem class; (γ)
the new corner clause (Gamma_mid ∩ Gamma_w added to NG-3's inventory) —
present and correctly attributed.

**C3-8 — leg-17 Remark 1.5.5 (A-2 chain; r3.3-untouched, re-verified per
brief): CONFIRMED.** Strongest attack: direct spectrum recomputation at
both loci (adjacent distinct gaps c-bar; pairwise separations c, c, 2c;
multiplicities (1,3,1) constant; projectors regular; the discontinuous
object is the incoming-modes subspace map — one regular eigenvalue's sign
crossing flips a fixed mode's class). No consumer cites the retired
"mutual = c-bar" phrase unannotated.

**C3-9 — r3.3 revision-log entry + reconciliation block: CONFIRMED.**
Re-counted: 5 IDs = 1 REPAIR + 4 AMENDMENT, matching the round-2 file's
summary table; the 13 round-1 re-verification outcomes match the live
text at every anchor spot-checked (§1); "NO step of the two-face proof
moved this round" is true (no r3.3 marker inside the proof body); the
described interruption/resume protocol (null=failure, three checks per ID)
is internally consistent with what the text shows.

**C3-10 — the two-face proof core at r3.3 state: CONFIRMED (unchanged
text; no new attack found).** The proof body (Claim with (cl-F)/(cl-C),
(D-coll), (H-UP-fam) restricted quantifier, eps_1', STEPs 1-3, UNION)
is byte-level r3.2 text already confirmed by round 2's C-block; this
round's attacks on the surrounding commentary produced no new angle on
the steps themselves (ESC3-1/2/3 live outside the proof). Label of record
SCHEMA per J-r2p-1, correctly carried at every consumer site re-checked
(Section 1.6 rigor block, register row 1', the r3.3 log).

==============================================================================
## §4 Summary table

| ID | Passage (r3.3 text) | Class |
|---|---|---|
| ESC3-1 | proves-too-much taxonomy: faces interior to Omega_int^h fall under neither bullet; enlargement not the mechanism there | AMENDMENT |
| ESC3-2 | Status (a) premise omits the (G3)-box clause; W^{1,infinity} alone does not give (EI) symmetrizer coercivity off the collar | AMENDMENT |
| ESC3-3 | falsifier arithmetic labels the standing downstream pulse "POST-t_p growth in the ROUGHENED exterior"; trigger constrains Omega_up only | AMENDMENT |

Totals: 3 objections = 0 BREAKS-THE-LEG + 0 REPAIR-NEEDED + 3 AMENDMENT.
Discharge verdicts (§1): ESC2-1, ESC2-2, ESC2-3 DISCHARGED clean; ESC2-4
DISCHARGED (mechanism + mirror) modulo ESC3-3's new-sentence labeling;
ESC2-5 DISCHARGED (class scoping) modulo ESC3-2's box clause in the same
sentence; L0-7(a)/(b), L1-7(i)/(ii) remain DISCHARGED; L1-8/A-2 remains
fully landed. First round of this escalation with ZERO inadequate
dispositions and ZERO REPAIR-grade findings: the residue is three
one-clause wording amendments in commentary/falsifier/status text — a
plausible dryness signal for lens l0, subject to the seed-protocol gate
(LG-1/E-5), which this refutation does not and cannot discharge. No
finding touches a step of the two-face proof; no label motion is proposed.

==============================================================================
## §5 Self-falsifiers (what kills each finding)

- ESC3-1 dies if a bare coupling across a face interior to Omega_int^h is
  shown to fall under a printed bullet as written — i.e. if bullet 1's
  enlargement mechanism is shown operative for a face that was already
  interior to Omega_int^h (it is not: the enlargement internalizes exactly
  Gamma_in^coll), or if such couplings are shown outside the judge's §5
  test class "ANY transmission coupling with NO transmission condition".
- ESC3-2 dies if (G3)-box membership on Omega_up is derived from
  "W-bar in W^{1,infinity}(Omega_up x [0,T_f])" alone (it cannot be —
  box membership is a pointwise range condition, not a regularity
  condition), or if the (EI) run on Omega_int^s is shown not to consume
  uniform S-bounds off the collar, or if a document clause already in
  force at case (a) is exhibited that supplies the box on
  Omega_int^s \ C_h (the Claim's (H1.1') supplies it ON C_h ONLY).
- ESC3-3 dies if the downstream pulse is shown to be inside Omega_up
  (it is injected "downstream of Gamma_I", outside Omega_up by
  definition), or shown constrained at t_p by the pinned trigger, or if
  the falsifier's roughening is shown to be applied downstream of
  Gamma_I rather than to the upstream exterior of the collar.

END — machine summary: {objections: 3, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc3_r3_l0.md}
