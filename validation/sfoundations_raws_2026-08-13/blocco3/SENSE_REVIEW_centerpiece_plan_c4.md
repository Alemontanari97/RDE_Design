# SENSE REVIEW — R22-F CENTERPIECE PLAN / MACHINE DESIGN (C4)
# Agent: expert sense-review, injection (6)(d) 2026-08-20 (timing miss
# declared on record; catches consumed at judge delivery + any
# post-judge repair round + the v2 continuation launch).
# SCOPE: the PLAN and the MACHINE, not the draft content. The on-disk
# author drafts were LISTED (existence/timestamps) but NOT read.
# Inputs read IN FULL: BRIEF_blocco2_phaseD.md (as amended, 209 lines);
# BRIEF_blocco2_phaseD_addendum_c4.md; findings_registry.yaml
# :1459-1467 (mandate row, magnitude field in full); C4 live-state
# block of SESSION_STATE_checkpoint.md (lines 1-186, to the ARCHIVE
# marker); BRIEF_nozzle_rde_arrivals_study.md (resume order).
# Machine state at review time (measured, ls): author drafts on disk =
# phaseD_r22f_centerpiece.md + phaseD_minor_{ntf,objdom,deltacarrier,
# crosslowering}.md; minor refuters EXECUTED = objdom, crosslowering;
# minor refuters NOT run = ntf, deltacarrier; R22F lens rounds NEVER
# ran (quota kill after author slots); v2 continuation pending.

Severity classes: BLOCKING-AT-DELIVERY (no landing until the check
passes; failure => escalation/repair round) / CHECK-ITEM (orchestrator
runs the named check at judge delivery or v2 launch; failure =>
named disposition) / NOTE (style/risk observation, no gate).

All greps below are relative to BASE =
validation/sfoundations_raws_2026-08-13 unless a path is given.

---

## AXIS (i) — MANDATE COVERAGE

### SR-C4-1 — The FORCHETTA table has NO refuter lens scoped to it
AXIS: mandate coverage. SEVERITY: BLOCKING-AT-DELIVERY.
DEFECT: The three lens scope lists (brief :139-152) enumerate content
from parts (1)-(3) only (fiber bounds/J-variation/duality; quotient/
residual well-posedness/fronts; swirl scaling/M-RED bands/epsilon
orders). Deliverable (5) — the user-mandated centerpiece table, added
by post-close addendum f67b1a9 — is named in NO lens scope. Neither
are: the six channels as such, the per-cell columns
(bound-or-estimate + provenance + what-tightens-it), the
SCALING-ESTIMATE labeling rule, the "no cell above held evidence
class" rule, or the mandatory Paxson-Miki worst-direction marker
(58.1% -> ~71.5% at fixed area ratio). The declared deterministic
delivery check (checkpoint, MID-WINDOW RECONCILIATION) covers ONLY
channel (vi) + the T-RED gradient schema. Consequence: the loop can
go DRY (zero BREAKS at all three lenses) with the user-facing
deliverable of record incomplete or defective — the refuters are
attacking math soundness, not table completeness.
DELIVERY CHECK (run on the FINAL revised draft, not round-1):
  grep -c "SCALING-ESTIMATE" phaseD/phaseD_r22f_centerpiece.md   # >=1
  grep -E "58\.1|71\.5" phaseD/phaseD_r22f_centerpiece.md        # marker present
  grep -E "\((i{1,3}|iv|v|vi)\)" phaseD/phaseD_r22f_centerpiece.md  # then eyeball: all SIX channels have cells
  Manual line-check: every cell has provenance + what-tightens-it
  (T-DISC/T-RED/M-RED/R22-CFD order) + a rigor/evidence class.
FAILURE => post-judge repair round scoped to the table (not a full
lens round).

### SR-C4-2 — Addendum (b)/(c) are invisible to the frozen round machine
AXIS: mandate coverage + dry-gaming + right-sizing. SEVERITY:
BLOCKING-AT-DELIVERY (discharged by the v2 design IF verified).
DEFECT: BRIEF_blocco2_phaseD.md contains no reference to
BRIEF_blocco2_phaseD_addendum_c4.md (read in full: absent; a grep for
"addendum_c4" across blocco3 at review time matched no file). The
addendum's own capture claim ("round agents that read it apply it
directly") is conditional on prompts pointing at it — the frozen v1
prompts predate it. Two concrete failure modes:
 (1) Item (c) (no-external-referee declaration) never enters the
     table: no lens will demand it, the author may not know it.
 (2) Item (b) (right-sizing: gradient-level bound = SCHEMA + named
     duty is an ACCEPTABLE dry outcome) never reaches L0/L2: a
     refuter can sustain a BREAK "gradient bound not closed-form"
     and burn rounds toward cap-4 against the expectation of record
     — simultaneously an over-spend and a false not-dry.
The v2 continuation order (refuter prompts explicitly point at
auxiliary carriers) is the correct fix; it must be VERIFIED, not
assumed.
DELIVERY CHECK (at v2 launch, before any round fires):
  grep -l "addendum_c4" <every v2 round/judge prompt file>  # all hit
  At judge delivery:
  grep -iE "referee|external.*(datum|c_F)" phaseD/phaseD_r22f_centerpiece.md
    # declaration (c) present in table header/notes
  VERDICT_r22f.md must cite addendum (b) wherever a gradient-level
  SCHEMA outcome is adjudicated dry.

### SR-C4-3 — Per-term Fig.18 disposition and its cross-row citations have no owner
AXIS: mandate coverage. SEVERITY: CHECK-ITEM.
DEFECT: The T-RED mandate (brief :75-86) requires, per residual term:
BOUNDED here / deferred to C51-route-B/S-5F (citing their rows) /
measured by M-RED, plus the explicit connection Fig.18 <->
data-anchored-shadow pin (swirl5f dispatch §3 row 13). This is
disposition BOOKKEEPING, not math structure: L1 owns residual
well-posedness but no lens is scoped to verify the disposition table
is total (every term dispatched) or that the cited rows resolve.
DELIVERY CHECK:
  grep -E "Fig\.? ?18" phaseD/phaseD_r22f_centerpiece.md   # exhibit present
  grep -E "C51|route-B|S-5F|row 13|shadow" phaseD/phaseD_r22f_centerpiece.md
  Manual: every T-RED residual term appears in the disposition with
  exactly one of the three fates; cited rows exist at their anchors.

### SR-C4-4 — Channel (vi): the measured mu needs a carrier and a hypothesis list the brief does not spell out
AXIS: mandate coverage + R5. SEVERITY: CHECK-ITEM.
DEFECT: The brief pins mu = "the MEASURED engine curvature at S*
(segmented TR-Newton curvature, Hessians of record)" — a NUMBER. R5:
no number without committed carrier. The plan nowhere names WHICH
committed carrier holds the curvature of record, and the |argmax
shift| <= delta/mu bound is only valid under hypotheses the brief
does not enumerate: (a) mu must be a LOWER bound on the curvature of
the reduced/projected Hessian over admissible design directions (the
optima of record are cert-limited/margin-inactive class — active-set
/ boundary-of-certifiability handling at S* must be stated, else the
unconstrained perturbation bound is vacuous there); (b) curvature
uniformity over a basin of radius >= delta/mu (not just at the
point); (c) delta measured in the norm DUAL to the one mu is measured
in. L0 plausibly attacks (a)-(c) once drafted, but the carrier
citation is provenance (no owner, cf. SR-C4-8). Also, per the
generality directive, a single measured mu is per-design: the cell
must state the bound is evaluated per certified design of record,
not as a class constant.
DELIVERY CHECK:
  grep -iE "delta/mu|argmax" phaseD/phaseD_r22f_centerpiece.md
  Manual: the (vi) cell cites a committed carrier path for mu (or
  declares mu-extraction a named F2 duty and says the cell is
  schema-only); hypothesis list covers projected-Hessian/basin/dual-
  norm/active-constraint points or defers each by name.

### SR-C4-5 — Part (4) R22-CFD re-scope has no lens owner
AXIS: mandate coverage. SEVERITY: CHECK-ITEM.
DEFECT: Part (4) is presentational (scheduling-decision INPUT,
"present, do not decide" per the row's owner field) and no lens is
scoped to it. Low math risk; the failure mode is scope creep
(deciding) or absence.
DELIVERY CHECK:
  grep -iE "schedul" blocco3/VERDICT_blocco2.md  # dossier present
  Manual: part (4) text presents options without a decision verb of
  record; the user touchpoint owns the decision.

### SR-C4-6 — Declaration (c) must be re-tested against the four new arrivals before it lands verbatim
AXIS: mandate coverage + arrivals seam. SEVERITY: CHECK-ITEM.
DEFECT: Addendum (c) asserts NO unsteady c_F discriminating datum
exists in the literature (verified at source for Harroun). Four
nozzle-RDE papers arrived AFTER that verification; the arrivals
campaign brief slot 5(e) explicitly orders the check "unsteady c_F
present or absent — check honestly" (P-B carries transient loss
decomposition and RMS deflection; P-C carries time-average bands).
If any of P-A..P-D provides a discriminating unsteady c_F datum,
declaration (c) is FALSE as written and must be amended, not
asserted. The plan currently has no wiring from the synthesis
outcome to the (c) delivery check.
DELIVERY CHECK (judge delivery, if SYNTHESIS_nozzle_rde_arrivals.md
is on disk — else the check blocks on the campaign landing):
  grep -iE "c_F|referee" blocco3/SYNTHESIS_nozzle_rde_arrivals.md
  Cross-check: the (c) declaration in the table cites the synthesis
  outcome (confirmed-absent OR amended) with the campaign as anchor.

---

## AXIS (ii) — SEED-DESIGN / STRUCTURAL BLIND SPOTS

### SR-C4-7 — Omission-blindness: the dry criterion cannot see what the author never wrote
AXIS: seed-design (the hypaudit precedent, elided-routes class).
SEVERITY: CHECK-ITEM (mitigated by SR-C4-1's checklist if adopted).
DEFECT: DRY = zero sustained BREAKS/REPAIRS at three CONTENT lenses.
All three attack what is on the page. A mandated element the author
omitted (a channel cell, a column, the G-c disposition, the M-RED
band derivations "published in the spec") generates no BREAK at any
lens — the machine structurally converges on a subset of the
mandate. The only declared completeness guard covers channel (vi)
alone. This is exactly the hypaudit failure class transposed from
seed authoring to draft authoring.
DELIVERY CHECK: the consolidated checklist at the end of this file,
run deterministically on the final draft against the brief-as-amended
deliverable list (1)-(5), each sub-element ticked by grep or line
citation in the orchestrator's delivery log.

### SR-C4-8 — No provenance/citation-fidelity lens exists
AXIS: seed-design. SEVERITY: CHECK-ITEM.
DEFECT: The brief orders "cite, never re-derive" for inputs of record
(P1 THEOREM*, swirl 3-6%, B1/B2/B5 numbers, Paxson-Miki numbers,
2-epsilon lemma and K-bar=0 "where the §8 verifier confirmed"). No
lens is scoped to verify a citation says what the draft claims it
says (L0/L1/L2 are structure lenses). A mis-transcribed number or a
panel-grade cited as record-grade (the swirl5f ADVISORY caveat is
explicit in the brief) survives all rounds.
DELIVERY CHECK (judge delivery, sampled): spot-verify at source the
load-bearing numeric cells — the swirl5f §8 verifier lines for the
2-epsilon lemma and K-bar=0, one of B1/B2/B5, and the Paxson-Miki
pair — read-then-quote in the delivery log. ADVISORY-provenance
labels present wherever swirl5f panel content is cited:
  grep -c "ADVISORY" phaseD/phaseD_r22f_centerpiece.md  # >=1

### SR-C4-9 — Minor (c) was authored in parallel with the [OBJ-DOM] adjudication it is sequenced against
AXIS: seed-design. SEVERITY: CHECK-ITEM.
DEFECT: Row pipeline:delta-carrier-F2-entry has trigger "sequenced
with/after [OBJ-DOM]"; the machine ran both authors in parallel
(both drafts on disk 10:14/10:20) and delegates sequencing to "the
judge enforces the sequence in its verdict text". Enforcement-by-
verdict-text cannot retroactively make the lemma consistent with
whichever OBJ-DOM fix (A: theta=0 station / B: declare coded J +
scope) is adjudicated: if the lemma's exit-area semantics depend on
the fix choice, a one-round minor refuter that ALSO ran blind to the
outcome cannot catch it. The deltacarrier refuter has NOT yet run —
the v2 continuation can repair this cheaply.
DELIVERY CHECK: v2 deltacarrier-refuter prompt points at
phaseD/refute_minor_objdom.md AND the judge's OBJ-DOM adjudication
order (refuter attacks consistency-with-both-fixes or the judge
adjudicates OBJ-DOM first). At delivery: VERDICT_blocco2 states the
lemma's consistency with the adjudicated fix EXPLICITLY; silence =
escalation of minor (c).

---

## AXIS (iii) — DRY-CRITERION GAMING

### SR-C4-10 — Amendment-downgrade laundering
AXIS: dry-gaming. SEVERITY: CHECK-ITEM.
DEFECT: AMENDMENTS carry to the closure judge "without extra rounds".
A lens (or the reviser characterizing a lens finding) can reach dry
by classing a real BREAK as an AMENDMENT. The plan gives the judge
adjudication over amendments but does not oblige it to audit the
classification itself.
DELIVERY CHECK: VERDICT_r22f.md must, per carried amendment, state
why it is not a BREAK (one line each); and every refuter finding the
reviser declined to repair must appear in the verdict as
sustained/overruled — a finding absent from both the final round
files and the verdict = delivery failure.
  grep -cE "AMENDMENT" blocco3/VERDICT_r22f.md  # count matches round files

### SR-C4-11 — Who computes DRY is unspecified
AXIS: dry-gaming. SEVERITY: CHECK-ITEM.
DEFECT: "Zero BREAKS/REPAIRS sustained at ALL THREE lenses in a
round" — the plan names no computer of this predicate. If the
reviser's round summary is the source, the agent with the strongest
dry-incentive adjudicates its own convergence.
DELIVERY CHECK (v2 codification): DRY is computed by the
ORCHESTRATOR, mechanically, from the three refuter round files of
the final round (zero findings classified BREAK or REPAIR in each
file), never from reviser text. The dry declaration in the delivery
log cites the three filenames + the per-file counts:
  grep -cE "^.*(BREAK|REPAIR)" phaseD/phaseD_r22f_refute_r<k>_l{0,1,2}.md

### SR-C4-12 — In-place revision can silently weaken mandated content across rounds
AXIS: dry-gaming. SEVERITY: NOTE.
Revisions are in place with append-only markers; a mandated statement
present at round 1 can be revised away by round k and no later lens
re-checks against the mandate. Covered IF the SR-C4-1/SR-C4-7
checklist runs on the FINAL draft (as specified there) — recorded
here so the delivery log says "final draft" explicitly.

---

## AXIS (iv) — RIGHT-SIZING

### SR-C4-13 — Over-spend guard on the gradient-level bound
AXIS: right-sizing. SEVERITY: CHECK-ITEM (same root as SR-C4-2(2)).
DEFECT: Without addendum (b) reaching L0/L2, cap-4 rounds can be
burned forcing a closed-form gradient bound against the expectation
of record. The valve direction is asymmetric and both sides bind:
SCHEMA + named duty = acceptable dry; label inflation (SCHEMA sold
as THEOREM) stays forbidden.
DELIVERY CHECK: any round-k refuter BREAK demanding a closed-form
gradient bound is adjudicated against addendum (b) BY THE
ORCHESTRATOR AT ROUND BOUNDARY (do not wait for the judge — rounds
are the resource being protected); the adjudication line lands in
the delivery log with the addendum cited.

### SR-C4-14 — Minor (c) load-class at one refuter round
AXIS: right-sizing. SEVERITY: NOTE.
The lemma is declared load-bearing ("prove properly") yet sits in the
one-round minor tier. Acceptable AS DESIGNED because the
auto-escalation rule is the protection — provided the judge applies
the load-bearing standard when deciding "surviving content
objection" for THIS minor (the LOAD-CLASS valve applies only to the
rung bookkeeping half, per the brief's own clause). No action beyond
judge awareness.

### SR-C4-15 — v2 continuation design checklist (resume order, folded in)
AXIS: right-sizing + machine design. SEVERITY: BLOCKING-AT-DELIVERY
(for the v2 LAUNCH, not the landing).
The v2 continuation workflow must verify, before the first round
fires:
 (a) NO re-run of on-disk author work: phaseD_r22f_centerpiece.md +
     the 4 phaseD_minor_*.md are inputs, not slots (verified on disk
     this review, 2026-08-20 10:14-10:22);
 (b) NO re-run of the two executed minor refuters
     (refute_minor_objdom.md, refute_minor_crosslowering.md on
     disk); the v2 minor slate = ntf + deltacarrier refuters ONLY
     (deltacarrier per SR-C4-9's amended prompt);
 (c) CIRCUIT-BREAKER: a round in which all three refuter slots die =
     VOID round — it does not consume the cap AND cannot contribute
     to dry (extends the declared null=failure single-slot rule to
     the full-dead case; a quota kill mid-round must not strand a
     half-attacked draft as "attacked");
 (d) AUXILIARY-CARRIER POINTERS in every round prompt (refuters,
     reviser, both judges): BRIEF_blocco2_phaseD_addendum_c4.md
     (binding), blocco3/FIELD_ATLAS_targeted_c4.md (cite-if-on-disk,
     absence blocks nothing), blocco3/SYNTHESIS_nozzle_rde_arrivals
     .md (cite-if-on-disk, ADVISORY; see SR-C4-16);
 (e) round file naming continues the of-record pattern
     phaseD_r22f_refute_r<k>_l<0|1|2>.md starting at r1 (no
     collision with the historical S-T0P/SWIRL-2D round files in
     phaseD/ — distinct prefixes, verified).
LAUNCH CHECK: the orchestrator's v2 launch log quotes (a)-(e) each
with its verification line; (d) by the grep of SR-C4-2.

---

## ARRIVALS SEAM (resume order item 2)

### SR-C4-16 — The nozzle-RDE campaign seam INTO the loop is half-defined: entry exists, adjudication wiring does not
AXIS: mandate coverage + machine design. SEVERITY: CHECK-ITEM.
WHAT IS DEFINED (campaign brief, read in full): confrontation stage
= the on-disk centerpiece draft parts 1-5 + forchetta channels;
slot 5(d) topology consolidation is declared "the citable ADVISORY
input" for R22F revisers/refuters; the campaign landing points its
outputs "at the Blocco-1 continuation prompts". Connectedness is
honored at the brief level.
WHAT IS NOT DEFINED (three holes):
 (1) TIMING/BARRIER: no rule says what happens when the synthesis
     lands after round k of the v2 loop — rounds already dried on a
     draft the threat ledger may contradict. Needed rule: the
     CONSOLIDATED THREAT LEDGER (slot 5(b)) and slot-6 refuter
     findings that bear on centerpiece statements are round INPUT if
     on disk before the final round, else a JUDGE-DELIVERY
     cross-check — VERDICT_r22f or VERDICT_blocco2 must record a
     disposition (fires / does not fire / F2 measurement) for every
     threat-ledger item naming a centerpiece statement or forchetta
     cell. A dry declared before the synthesis landed does NOT
     exempt the delivery from this cross-check.
 (2) JUDGE INPUT LIST: both judge briefs (frozen v1) enumerate their
     reads without the synthesis/threat ledger; the v2 judge prompts
     must add it (SR-C4-15(d) covers mechanically; recorded here
     because the JUDGES, not only refuters, are the consumers of the
     threat ledger's dispositions).
 (3) SPECIFIC CELL CONFRONTATIONS the seam must force (from the
     campaign brief's own 5(e) list, so the judge check is
     grep-able): channel (iii) swirl cells vs P-B 14.42 deg RMS /
     P-C RMSD 9-11 deg; channel (v) model-form vs the papers' loss
     decompositions; delta-carrier lemma vs P-A convergence-section
     + P-D choked +50-60%; declaration (c) vs unsteady-c_F check
     (SR-C4-6); T-DISC averaging bet vs P-A averaged-plume claim.
DELIVERY CHECK:
  grep -iE "14\.4|9-11|choked|averaged.plume|THREAT" \
    blocco3/VERDICT_blocco2.md   # dispositions present when synthesis on disk
  Absence of the synthesis on disk at delivery = the check converts
  to a NAMED PENDING item in the landing list (owner: arrivals
  campaign landing), never silently dropped.

---

## AXIS (v) — LANDING / R4 COMPLETENESS

### SR-C4-17 — The judge's landing-list duty under-specifies four obligations
AXIS: landing/R4. SEVERITY: CHECK-ITEM.
DEFECT: "Exact M0/D-doc sites + registry row texts" is generic; four
concrete obligations can fall through:
 (a) the MANDATE ROW ITSELF: docs/findings_registry.yaml
     theory:r22-formal-decomposition (:1459) needs its
     status/evidence updated by the landing — a landing list that
     only MINTS rows misses the row that ordered the work;
 (b) LIT-REGISTRY PROMOTIONS harvested from ALL slots (author +
     refuters + minors + judges), not only the author: every [FULL]
     read feeds UNREAD -> READ-* with where_read (brief :37-38);
     Giles-Pierce specifically rides with the G-c leg outcome;
 (c) the FORCHETTA TABLE'S OWN LANDING SITE is UNNAMED anywhere in
     the plan: the brief lands T-DISC/T-RED in M0 and M-RED as a
     spec, but the table — "the user-facing adequacy bracket of
     record until M-RED/R22-CFD tighten it" — has no named of-record
     site nor registry row. Per the artifact-connectedness rule this
     is an orphan-in-waiting; the judge's landing list must name the
     site + the bracket-of-record row text;
 (d) NO DUPLICATION with the arrivals campaign's own landing (4 lit
     rows + graft list are THAT landing's authority — one authority
     per statement, per the brief's own judge clause).
DELIVERY CHECK:
  grep -E "1459|r22-formal-decomposition" blocco3/VERDICT_blocco2.md
  grep -iE "READ-|where_read" blocco3/VERDICT_blocco2.md
  grep -iE "forchetta" blocco3/VERDICT_blocco2.md  # landing site named
  Manual: PAPERS NEEDED sections of all slot outputs aggregated into
  the landing list (may aggregate to empty — stated).

### SR-C4-18 — G-c leg outcome must be greppable in the verdict
AXIS: landing/R4. SEVERITY: CHECK-ITEM.
DEFECT: The Giles-Pierce leg (brief :62-71) ends in exactly one of
two states — DISCHARGED-with-citation or OPEN-declared — and the
registry update "rides the landing". If the verdict does not carry
the outcome explicitly, the landing cannot execute it.
DELIVERY CHECK:
  grep -E "G-c" blocco3/VERDICT_r22f.md blocco3/VERDICT_blocco2.md
  # outcome word (DISCHARGED|OPEN) on the same line or adjacent

### SR-C4-19 — Temporal-form row is NOT the judge's to mint
AXIS: landing/R4. SEVERITY: NOTE.
Addendum (e)'s refined temporal-form row (WEAKENED-PIN scoping) is a
coverage-gate mint with dedup, per the checkpoint's iniezione (4).
The Blocco-2 judge's landing list must not mint it — recorded so the
delivery check treats a judge-minted duplicate as a defect, not
diligence.

---

## MACHINE SUMMARY

COUNTS: 19 findings — BLOCKING-AT-DELIVERY: 3 (SR-C4-1, SR-C4-2,
SR-C4-15) / CHECK-ITEM: 13 (SR-C4-3, -4, -5, -6, -7, -8, -9, -10,
-11, -13, -16, -17, -18) / NOTE: 3 (SR-C4-12, -14, -19).

ROOT PATTERN (one sentence): the machine is sound on math-structure
attack but has NO owner for completeness-vs-mandate, provenance
fidelity, or the post-amendment deliverables (forchetta table,
addendum items) — everything the three content lenses structurally
cannot see must be caught by a deterministic orchestrator checklist,
which the plan gestures at (channel (vi) only) but does not enumerate.

CONSOLIDATED DELIVERY CHECKLIST (orchestrator; two gates):

GATE V2-LAUNCH (before the first v2 round fires):
 [ ] SR-C4-15(a): author drafts are inputs, no author slot in v2.
 [ ] SR-C4-15(b): minor refuter slate = ntf + deltacarrier only.
 [ ] SR-C4-15(c): full-dead-round circuit breaker in the workflow
     (void round: no cap consumption, no dry contribution).
 [ ] SR-C4-15(d)/SR-C4-2: grep -l "addendum_c4" over every v2
     prompt file = all hit; field-atlas + synthesis pointers
     present as cite-if-on-disk.
 [ ] SR-C4-9: deltacarrier refuter prompt carries the OBJ-DOM
     outcome pointer (or judge sequences OBJ-DOM first).
 [ ] SR-C4-11: dry predicate computed by orchestrator from the
     three refuter files, rule quoted in the launch log.
 [ ] SR-C4-13: round-boundary adjudication of closed-form-gradient
     BREAKs against addendum (b), rule quoted in the launch log.

GATE JUDGE-DELIVERY (before ANY landing):
 [ ] SR-C4-1: forchetta completeness greps (six channels, cell
     columns, SCALING-ESTIMATE, 58.1/71.5 marker) on FINAL draft.
 [ ] SR-C4-2: declaration (c) present (grep referee/c_F) + cited
     per SR-C4-6 against the arrivals synthesis (or NAMED PENDING).
 [ ] SR-C4-3: Fig.18 per-term disposition total; C51-route-B/S-5F/
     row-13 citations resolve.
 [ ] SR-C4-4: channel (vi) mu carrier cited or F2 duty named;
     hypothesis list (projected Hessian / basin / dual norm /
     active constraints) present or deferred by name; per-design
     scope stated.
 [ ] SR-C4-5: part (4) presents-not-decides; scheduling dossier in
     VERDICT_blocco2.
 [ ] SR-C4-7: deliverables (1)-(5) sub-element tick-list in the
     delivery log, each with grep or line cite.
 [ ] SR-C4-8: provenance spot-checks (swirl5f §8 lines, one of
     B1/B2/B5, Paxson-Miki) read-then-quote; ADVISORY labels
     present.
 [ ] SR-C4-9: OBJ-DOM/delta-carrier consistency stated in
     VERDICT_blocco2 (silence = escalate minor (c)).
 [ ] SR-C4-10: per-amendment not-a-BREAK line in VERDICT_r22f;
     no refuter finding absent from both round files and verdict.
 [ ] SR-C4-16: threat-ledger dispositions in the verdicts (or
     NAMED PENDING with owner) incl. the five named cell
     confrontations.
 [ ] SR-C4-17: landing list updates row :1459; harvests lit
     promotions from ALL slots; NAMES the forchetta landing site +
     row; no duplication with the arrivals landing; PAPERS NEEDED
     aggregated.
 [ ] SR-C4-18: G-c outcome greppable in the verdicts.
 [ ] SR-C4-19: no judge-minted temporal-form row.

FAILURE SEMANTICS: any BLOCKING gate line failing = post-judge repair
round (table-scoped where SR-C4-1) or escalation per the standing
rule; CHECK-ITEM failures = named disposition in the delivery log,
never silent.
