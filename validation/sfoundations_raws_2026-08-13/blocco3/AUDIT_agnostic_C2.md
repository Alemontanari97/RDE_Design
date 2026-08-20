# AUDIT — AGNOSTIC OVER-ENGINEERING / SOTA-DEPTH (S-FOUNDATIONS-C2)
Context-free auditor of record, 2026-08-19. Brief:
BASE/blocco3/BRIEF_agnostic_audit_C2.md. BASE =
validation/sfoundations_raws_2026-08-13. Read-only except this file.
No orchestrator self-assessment was read or sought; every verdict below
cites the artifacts themselves.

## 0. METHOD SPEC READ + SAMPLE COVERAGE (measured this window)

Read IN FULL: BRIEF_wave1_panels.md (205 l.), BRIEF_wave2_panels.md
(§0-bis/§0-ter, 251 l.), BRIEF_wave2_refuter_judge.md (74 l.),
BRIEF_wave2_reconcile.md (39 l.), BRIEF_wave1_C9C11_supplement.md
(75 l.), BRIEF_wave1_refuter.md, BRIEF_wave1_judge.md. Executed
instances read in full: PANEL_C28.md (576 l.), PANEL_C27.md (650 l.),
PANEL_C9C11.md (698 l.), PANEL_C9C11_SUPPLEMENT.md (694 l.),
refute_C28.md (308 l.), refute_C9C11.md (403 l.), VERDICT_wave1.md
(966 l.), r2pass/VERDICT_doc1_rev10.md (409 l.); sampled at need:
refute_C9C11_supplement.md (machine summary + posture),
VERDICT_C9C11_supplement.md (landed during this audit window, mtime
18:21 — read §0-§4). phaseD/phaseD_stop_proof.md: (H-G8) block
l.2159-2353 and §13 REVISION 10 block l.4687-4930 read; section map
measured (grep '^## §': proof body §0-§9 = l.149-2955; revision logs
§10-§13 = l.2956-4964 of a 4964-line file). Landed record verified at
source: docs/choice_ledger.yaml C28 :419-427, C27 :407-417, C43
:581-589, C42 note :579; docs/rde_nozzle_MASTER.md [T-T0P] Part-III
block (:573 "THE [T-T0P] MAIN STATEMENT" + surrounding);
docs/claims_registry.yaml C-XBVP-aprime :2087-2098 and [T-T0P] row
:2040-2050; docs/glossary.yaml header :1-40 + wave-1 entries
:1129-1148. State instrument: SESSION_STATE_checkpoint.md (443 l.,
SESSION C2 blocks l.9-141) read in full.

Cross-checks executed by me (not inherited): landed C28/C27/C43 note
texts diffed against VERDICT_wave1 §4.1/§4.2/§4.5 proposals (faithful,
no material divergence found on the three rows); grep "query-level"
across BASE (hits only in wave-2 partials, the supplement, and the
checkpoint — basis of AG-3); blocco3/ directory listing for wave-2
verdict/confirm artifacts (none exist yet — basis of AG-2's timing
claim); stop_proof section-line arithmetic (basis of AG-6).

---

## 1. FINDINGS

### AG-1 — OVERENGINEERED — proof-loop generality unpriced by load
class: the (H-G8) granted half burned five until-dry rounds on a row
the record itself classes as non-load-bearing.
**Evidence:** phaseD_stop_proof.md:4706-4725 — the revision-10 strategy
declaration prints, verbatim, "the row is gap ACCOUNTING for the
abstract-EOS route — which stays OPEN at route level — not load-bearing
theory. Over-generality bought five rounds; this revision stops
buying." Round count verified: REVISION 5-10 entries at :3482, :3634,
:3790, :4022, :4342, :4693, each a full two-lens+judge cycle
(r2pass/esc_doc1_* file series). The fix (sufficient-but-unoptimized
strong condition, (H-G8-1)-(H-G8-4) at :2187-2264 with (D1)-(D7)
derived at pen grade) was available at any round: it required no new
mathematics, only a scoping decision — and it came from the
orchestrator/user strategy note (SESSION_STATE_checkpoint.md:267-272),
not from the loop itself. The method HAS a depth-vs-stakes valve, but
only at the census tier (BRIEF_wave2_panels.md §0-ter(c) "materiality
... depth follows stakes — this is the anti-over-engineering valve");
no analogous valve governs proof-revision depth: the until-dry tier
(checkpoint :406-410) is reserved by TOPIC (centerpiece theorems), and
once a row escalates there, nothing prices generality against its
declared load.
**Named cut (policy, zero rigor loss):** extend the materiality valve
to the proof tier — at until-dry entry, the brief DECLARES the row's
load class (load-bearing theory vs gap accounting/bookkeeping);
gap-accounting rows OPEN at the strong-sufficient-unoptimized form
(the rev-10 strategy as default first move), and generality is
escalated only on a NAMED consumer that needs the weaker hypothesis
set. Rigor is untouched: sufficiency is still proven at pen grade and
still adversarially confirmed; only the number of generality-driven
refutation rounds falls.
**Materiality:** HIGH. Rounds 5-9 on this row are the single largest
avoidable spend in the sampled record (four two-lens rounds + judges
of the r2pass/esc_doc1 series); the failure mode recurs at every
future gap-accounting row absent the rule.

### AG-2 — UNDERRIGOROUS — repaired text lands of record before any
adversarial pass over the repairs; the scheduled retroactive pass is
conditioned on an unrelated event.
**Evidence:** (a) VERDICT_wave1.md:440-445 — 11 REPAIR-NEEDED + 18
AMENDMENT texts adjudicated and "CARRIED to the landing window", zero
escalations; SESSION_STATE_checkpoint.md:10-14 — wave-1 LANDED
(C28/C27 in choice_ledger + C43 aligned + C42 notified) in the same
window. The landed rows are of record now (choice_ledger.yaml:419-427,
:407-417, :581-589). (b) The confirm-on-repairs stage was adopted
AFTER that landing (BRIEF_wave2_refuter_judge.md:60-74, mtime 18:12 vs
the landing recorded at checkpoint :10) — adopted, correctly, on the
measured evidence that "repaired text is the record's most
defect-prone class — R9-B/R9-C minted by rev-9's own restatement,
R10-1/-3 by rev-10's" (:61-62). (c) Its retroactive coverage of the 11
wave-1 repaired clauses is CONDITIONAL: "If the wave judge sustains
REPAIRS > 0, ONE dedicated confirming lens runs after the judge ...
PLUS — retroactively, first instance only — the 11 wave-1 repaired
clauses" (:63-68). If the wave-2 judge sustains zero repairs, the
wave-1 repaired clauses — already landed — never receive their confirm
pass. (d) Same class: the 8 doc1 landing edits (checkpoint :21-24,
applied per VERDICT_doc1_rev10 §4 "applied at the landing window
without further rounds", :330-332) are post-verdict restatements with
no confirming lens scheduled at all — exactly the operation that
minted R10-1/R10-3 out of rev-10's own restatement (VERDICT_doc1_rev10
:51-139). Mitigations noted honestly: each wave-1 repair text was
authored by a refuter and independently verified/re-derived by the
judge (VERDICT_wave1 §0.1), and my own spot-diff of the three landed
ledger notes against the §4 proposals found no divergence — the
finding is the missing GUARANTEE on the composed landed text, at a
measured restatement-defect base rate of 2 rounds out of 2 (rev-9,
rev-10).
**Named repair:** (i) uncondition the retroactive clause — the
confirm-on-repairs lens over the 11 wave-1 repaired clauses AS LANDED
(ledger note text, not only verdict text) + the 8 doc1 landing edits
runs regardless of the wave-2 judge's repair count; (ii) standing
sequencing rule: adjudicated repairs become of-record only after
their confirm lens (or land flagged PENDING-CONFIRM, so a later defect
finding re-opens a flagged row, never silently corrects a clean one).
**Materiality:** MEDIUM-HIGH. The 29 carried texts include falsifier
protocols (F-3, F-C27-1..5+αβγ, F9a/F11a pins) that will govern F2
experiments; a restatement defect there mis-pins an experiment, and
the class's measured mint rate is not small.

### AG-3 — UNDERRIGOROUS — a BINDING landing gate passed two rows with
no on-file verdict.
**Evidence:** the wave-1 landing gate is declared binding at
SESSION_STATE_checkpoint.md:105-112: "before any wave-1 ledger delta
lands, orchestrator checks the panels' census against the directive
axes — C9/C11 must have closed moving-mesh/r-adaptivity +
discrete-vs-continuous adjoint + adjoint-free estimation; C27/C28 the
query-level axis; any miss = census supplement round for that row
BEFORE its delta lands." The C9/C11 MISS produced a full documented
chain (supplement + refuter + judge, now on file). The C27/C28 PASS
exists only as the implication of the landing having happened: grep
"query-level" across the repo hits only the wave-2 partials, the
supplement, and the checkpoint itself — no artifact carries the
per-axis reasoning for C27/C28 (whether the axis closed, or a ruled
does-not-bear per the §0-ter(f) form). The panels themselves defer the
engine question to C31 by name (PANEL_C28.md:434-435 "its engine half
... is C31/[P-IPADJ], named, not decided here"), which is a plausible
does-not-bear ruling — but plausible-by-implication is below this
record's own standard (SR-12: gate verdicts cite the measured check in
their own window; the C9/C11 half of the SAME gate got a documented
verdict).
**Named repair:** one written gate-verdict paragraph in the landing
log (or checkpoint) before session close: per-axis, per-row (C27,
C28), either the panel file:line where the census closes the
query-level axis or the explicit does-not-bear ruling with its reason.
Cost: a paragraph.
**Materiality:** LOW-MEDIUM. The substantive risk is small (the axis
almost certainly lands in C31's wave-2 scope, and C28 risk (4) +
PANEL_C28 §3.5.2/6 already route engine consequences there by name);
the process risk is the precedent — a binding gate whose pass leg is
undocumented is unfalsifiable, and this record's entire value
proposition is falsifiable gates.

### AG-4 — UNDERRIGOROUS — single-model verification pool: the seed
calibration proves detection power, not absence of common-cause blind
spots; and the seeds are authored by the same model they calibrate.
**Evidence:** model pin of record — Fable everywhere; Sonnet
mechanical-only; Opus zero slots (checkpoint :337-339, user-pinned).
Every panel, refuter, lens, and judge in the sample is therefore the
same model. The compensating layer is real and executed: dual-seed
protocol PASS both directions (checkpoint :176-183: canary BROKEN on
content at source, known-true SOUND; SEED_PROTOCOL_v3), independence
declarations + per-lens ID prefixes (VERDICT_doc1_rev10:28-33). But
the seeds are in-workflow, model-authored artifacts — the record
itself logs a "judge-adjudicated SEED-AUTHORING defect (3 genuine
route elisions)" (checkpoint :154-157) — so the calibration axis
cannot, in principle, exhibit a defect class the authoring model
cannot conceive. A shared-blind-spot failure passes every layer:
author, both lenses, judge, and seed-designer share it.
**Named repair (compatible with the user's model pin):** (i) draw a
fraction of canary defects from MODEL-EXTERNAL corpora — published
errata, known-wrong classical claims, defect taxonomies from the
V&V/proof-checking literature — so the calibration axis is
model-independent even when the graders are not; (ii) mint a standing
findings-registry row naming the residual common-cause risk of the
single-model pool, so the model-pin decision is priced at every future
user touchpoint instead of living only in a memory file.
**Materiality:** MEDIUM. Unquantifiable by construction (that is the
point); the record's stakes (certified-engine theory) justify pricing
it visibly rather than assuming the seed layer covers it.

### AG-5 — OVERENGINEERED — the live checkpoint carries ~160 lines of
superseded session-C history in the every-session opening path.
**Evidence:** SESSION_STATE_checkpoint.md:142-299 — SESSION C blocks
(Blocco 0-2, quota kills #1-#4, close) all marked CLOSED/EXECUTED and
duplicated of record in the committed session log
(validation/PROGRESS_2026-08-19_SfoundationsC.md, cited at :285-286)
and the R35 census row; the file's own authority note ranks it below
registries (:300-302). The C2 opening reads this file integrally
(header :6-7), so the dead blocks are paid at every opening.
**Named cut:** at the C2 close, archive blocks :142-299 to the session
log / PROGRESS_ARCHIVE (the SR-10 pattern already used for ORA/NEXT),
keeping the purpose header + live-session block only. Zero rigor loss:
nothing in :142-299 is the current authority for anything.
**Materiality:** LOW (recurring opening-context cost only; but it is
the exact entropy class R7/SR-10 exists to sweep).

### AG-6 — OVERENGINEERED — 40% of the proof carrier is process ledger:
§10-§13 revision logs = ~2000 of 4964 lines of phaseD_stop_proof.md.
**Evidence:** measured section map — proof body §0-§9 ends l.2955;
§10-§13 span l.2956-4964; §13 alone l.3356-4964 (~1600 lines, six
REVISION entries each embedding authority recitals, per-residue
mechanisms, edit-site inventories with line anchors, hash proofs,
falsifier lists, label summaries: e.g. REVISION 10 at :4693-4930).
The apparatus is genuinely load-bearing for the confirm rounds (the
rev-10 lenses audited containment against the §13 anchor lists and
leg-3 hashes — VERDICT_doc1_rev10 §2(d)), so none of its CONTENT can
be cut. Its LOCATION can: R4 makes theory docs the paper source; every
future lens/reader pays the full 283KB file, and the in-file log
grows per round by construction.
**Named cut (mechanical, zero rigor loss):** at the next session
boundary, split §10-§13 to a sidecar
(phaseD_stop_proof_REVLOG.md, append-only, ADVISORY_INDEX row, same
in-place-annotation rule), leaving in the proof document the current
condition, the label summary, and a pointer. The audit mechanics
transfer intact: edit-site lists and containment sweeps run on both
files; the leg-hash discipline gets STRONGER (the proof body file
changes only when proof content changes). One-time cost: anchor-range
re-measurement + index/lint updates — the record already performs
exactly this class of migration (SR-10 archives).
**Materiality:** MEDIUM. Every confirm lens reads this file in full;
the log's share grows monotonically; at the measured trajectory the
process ledger passes the proof itself within ~2 more rounds.

### AG-7 — AT-BAR — candidate "measured halves deferred to F2 while
verdicts read as 'converged'" REJECTED: the labels are honest at every
carrier sampled.
**Evidence:** VERDICT_wave1 headlines are "measurement-gated
CONVERGED-ON-PROTOCOL" with gated:true per row (:453, :533, :600,
:650, machine summary :938-958); the landed ledger statuses are MIXED
with in-note gating ("adoption-of-record gated on F2 measured half",
choice_ledger.yaml:419-427; same structure at :407-417); the C28
adoption is explicitly capped "ADOPTED-FOR-MEASUREMENT, not
adopted-of-record" (VERDICT_wave1:488-489) and the evidence-status
inflation that DID exist ("Probe B ... committed", three sites) was
caught by the refuter (refute_C28.md:68-91), carried as a repair, and
the landed note now prints the honest form ("scratchpad-run toy ...
NOT a committed carrier", choice_ledger.yaml:427).
**Named consequence:** no cut, no repair — candidate closed. The one
residual is covered by AG-2 (the honest labels are repair-carried
text, which is the class needing the confirm pass).
**Materiality of the finding:** LOW (it removes a suspected defect
from the audit space).

### AG-8 — AT-BAR — candidate "verification layers per claim class /
per-wave stage count incl. confirm-on-repairs" REJECTED at the
panel/wave tier: depth is governed by a declared, escalation-guarded
policy, and the new stage is evidence-priced and narrowly scoped.
**Evidence:** the right-sizing policy of record enumerates depth per
class with the auto-escalation valve as its conservativeness proof
(checkpoint :388-422: trees-as-advocates not regenerated, cluster
panels, single-pass for convergent rows, protocol-only convergence for
measurement-gated rows, until-dry reserved for centerpieces, "~20-25
agents vs ~90+ naive"; escalation rule (g)). Executed instances match
the policy: wave-1 = 3 panels + 3 fused refuters + 1 judge for 4 rows;
zero ritual rounds observed (every round in the sample produced
sustained findings: 33/33 in wave 1; even the marginal rev-10 confirm
round minted R10-1/-3 — defects created by the revision under check,
i.e., exactly what the round exists to catch). The confirm-on-repairs
stage is scoped "to ONLY the judge-repaired clauses"
(BRIEF_wave2_refuter_judge:64-65) — one lens, not a wave re-run.
**Named consequence:** no cut at this tier. The genuine layer-count
defect lives at the proof tier and is AG-1; the stage's trigger defect
is AG-2(i).
**Materiality:** LOW-MEDIUM (validates the sampled economy; directs
the cut where the evidence is).

### AG-9 — AT-BAR (with one cheap repair) — census read-depth
discipline: the two live under-depth instances in the sample were both
caught by the system's own layers; wave-1 censuses remain formally
below the §0-bis(b) standard they predate.
**Evidence:** caught instance 1 — PANEL_C27's decisive census item
(Samakhoana-Grimmer LSE near-optimality) is a page-verified PREPRINT
statement carrying the §3.1 "theorem-backed WALL"; the refuter flagged
the transfer as underived and the judge carried the weakening with the
verdict surviving on two independent legs (VERDICT_wave1:265-279).
Caught instance 2 — PANEL_C9C11 cited Lozano-Ponsin 2025 at
"[abstract read]" while the repo HOLDS the PDF with a READ-PARTIAL
registry row; the supplement's family-token grep caught it and the
supplement judge verified it at source (PANEL_C9C11_SUPPLEMENT:556-565;
VERDICT_C9C11_supplement:26-29). Residual: PANEL_C28 §2's per-source
one-liners carry no explicit depth markers (C27's do, ad hoc:
[abstract-level]/[page-verified]/[classic] at PANEL_C27:127-217);
wave-1 panels predate §0-bis(b) and were gated for AXES, not
retrofitted for depth markers.
**Named repair:** one rider line in the wave-1 landing annotations
declaring the two wave-1 censuses pre-§0-bis (grandfathered; evidence
levels ad hoc per item; verdicts lean on in-repo record objects, which
this audit confirms for C28 — the adoption rests on GAP-1/M0/probe
evidence, census as context). No retro-editing of frozen panel
artifacts.
**Materiality:** LOW (the load-bearing exposures were already
consumed; the rider prevents a future reader from holding wave-1
censuses to a standard they were never run under, or trusting them to
one they don't meet).

### AG-10 — UNDERRIGOROUS (process placement) — SR-12-class defects
recur at authoring time and are caught only at refuter/judge cost:
three instances in one wave.
**Evidence:** (1) PANEL_C28 §2 cava grep count wrong (3 vs measured 5
— refute_C28.md:165-174); (2) VERDICT_wave1 §4.7 "all grep-proven
absent today" false for lozano_ponsin_2025 (row exists on disk —
PANEL_C9C11_SUPPLEMENT §C, judge-verified); (3) the supplement's own
"candidate id C52 (next free)" inherited-not-measured while C52-C55
already existed — the refuter classed it REPAIR-NEEDED and its being
sustained FIRED A FULL JUDGE SLOT (VERDICT_C9C11_supplement:2-4, :68:
"the exact SR-12 failure mode of record"). The catching layer works
(all three consumed); the enforcement point is misplaced — each catch
costs a downstream agent pass, and instance (3) cost a whole
escalation slot for a one-command defect.
**Named repair:** make the two recurring claim shapes mechanically
verifiable at authoring time — panel/supplement brief schemas require
a verbatim MEASURED-OUTPUT block (command + raw output) for (a) any
"next free id" claim and (b) any registry-absence claim; a missing
block is a lint-class failure the refuter checks first. This is the
record's own SR-12 rule moved from duty to schema.
**Materiality:** MEDIUM-LOW per instance (tens of k tokens per
downstream catch; measured recurrence 3 in one wave), compounding at
Blocco-4/5 scale.

### AG-11 — AT-BAR — candidate "glossary/token ratchet discipline"
REJECTED: the glossary already implements the anti-bloat rule the
candidate suspects is missing.
**Evidence:** docs/glossary.yaml:17-38 — namespace-qualified entries;
PREFIX-FAMILY RULE ("any token family that resolves to a REGISTRY ROW
gets ONE family entry ... NOT one row per member"; "a navigable file,
NOT a 700-row dump"); honest-scope clause disclaiming anti-re-mint
authority (:9-15). Wave-1 minted exactly 5 duty tokens + 1 session
token + a family row (checkpoint :12-13), each a 5-line resolver
pointer, no content restatement (:1129-1148). Lint automated (0
violations at 164 entries).
**Named consequence:** no cut. **Materiality:** LOW.

### AG-12 — ABOVE-BAR — brief economy and consumption: the candidate
"brief length vs what agents actually consume" resolves in the
method's favor.
**Evidence:** wave-2 briefs bind wave-1 §0 BY REFERENCE instead of
restating it (BRIEF_wave2_panels.md:7-12; BRIEF_wave2_refuter_judge:
3-5 "applies VERBATIM with these substitutions"); the reconcile brief
is 39 lines for a three-slot salvage with a verified-partial doctrine
(BRIEF_wave2_reconcile.md:19-30); consumption is demonstrable — every
§0/§0-bis/§0-ter obligation appears as an executed section in the
sampled outputs (e.g. PANEL_C9C11_SUPPLEMENT §A.2/A.3/B.2/B.4 query
tables, pre-registered criteria, depth markers, PAPERS NEEDED), and
the §0-ter protocol itself records what it deliberately did NOT adopt
("NOT adopted (ritual here): PRISMA flow diagrams, database quotas,
inter-rater stats" — checkpoint :125-126).
**Named consequence:** none — preserve the by-reference pattern as the
template. **Materiality:** LOW.

---

## 2. Q3 — SOTA GRADES (per dimension, with the comparison practice)

| Dimension | Grade | Basis (specific practice compared) |
|---|---|---|
| (i) Systematic review / meta-research | **ABOVE** | Compared to PRISMA-2020-class search documentation + Cochrane-style pre-registration + GRADE-style evidence levels: §0-ter mandates verbatim query strings with hits/screened/included counts, per-row decision criteria FROZEN BEFORE search with declared mid-census amendments, dated censuses, read-depth markers [FULL]/[ABS]/[TITLE] with claims capped at depth, steelman-at-best-instance, materiality valve, and a procurement channel instead of silent approximate reading (BRIEF_wave2_panels:55-82); an independent enforcement duty exists (refuter g2, BRIEF_wave2_refuter_judge:17-26) and FIRED in practice (RS911-2 post-hoc-question smuggle; RS911-3 over-depth authorship claim — both sustained, VERDICT_C9C11_supplement §1). Ritual PRISMA elements were examined and declined by name (checkpoint :125-126). Published engineering-design SOTA surveys carry almost none of this. Honest caveats: wave-1 grandfathered (handled via landing gate + supplement; residual = AG-9's rider), and coverage is WebSearch-bounded with absence claims correctly query-bounded (PANEL_C28:192-198). |
| (ii) Formal verification / safety-case | **ABOVE** | Compared to GSN/assurance-case practice with defeaters, DO-178C-style traceability, and mutation-testing calibration: per-claim rigor classes with named falsifiers INCLUDING falsifiers for the verdicts themselves (VERDICT_wave1 §5; VERDICT_doc1_rev10 §5); adversarial dual-lens review with declared independence and per-lens ID namespaces; judge re-derivation at pen grade with own-window re-measurement of every witness (VERDICT_wave1 §0.1 — a 90-line measured-witness ledger; judge re-derived band arithmetic, coverage bounds, falsifier partitions); byte-range hash proofs that untouched proof legs are untouched (stop_proof :4836-4846, command pinned); and — rare even in safety-critical practice — CALIBRATION OF THE REVIEW LAYER ITSELF in both directions via seeded canary (must fire) + known-true (must survive), with a seed-authoring defect itself caught and adjudicated (checkpoint :154-157, :176-183). The two named holes are AG-2 (repairs land before their confirm pass) and AG-4 (single-model common-cause), both with repairs proposed; neither lowers the comparative grade — the compared practices do not reach this floor. |
| (iii) Agentic-pipeline engineering | **AT** | Above bar: cache-resume vs relaunch doctrine with the never-resume-with-edit rule (checkpoint :241-243), the reconcile pattern for post-kill partial files ("verify + complete, never duplicate, never trust" — BRIEF_wave2_reconcile:5-7), null=failure accounting everywhere, structured machine summaries as inter-agent contracts, per-workflow token/shape reporting (SR-9), and briefs-by-reference. Below bar: capacity/admission control — FIVE quota kills in one campaign, with kill #5's root cause self-declared as "orchestrator launched 7+3 agents concurrently without budget weighing" (checkpoint :52-55) against a KNOWN session limit; ~552k tokens sunk on wave-2 panels alone (:40-41), the fix (usage-aware launch sequencing) minted only after the fifth kill. Production-grade pipeline practice treats quota admission as a first-class scheduler constraint, not a post-mortem lesson. Recovery discipline is exemplary; the scheduling that necessitates it is not. Net: AT. |

---

## 3. VERDICT SHAPE (one paragraph)

The sampled method is not performing rigor — the layers demonstrably
kill real defects at every tier (33/33 sustained wave-1 findings, all
witness-backed; a misfiring falsifier pin, a false provenance label,
and a missing representation family caught before landing; a
restatement-defect class discovered, measured, and answered with a
targeted stage), and its economy instruments (right-sizing with an
escalation valve, materiality clause, family-row glossary,
briefs-by-reference) are genuine and used. The over-engineering that
exists is concentrated and specific: generality unpriced by load class
at the proof tier (AG-1, the expensive one), and process mass
accreting inside carrier files (AG-5, AG-6). The under-rigor that
exists is also specific and mostly sequencing-shaped: repaired text
becomes record before its confirm pass (AG-2), one gate leg
undocumented (AG-3), a structural common-cause residue priced nowhere
(AG-4), and SR-12 enforcement placed downstream of authorship (AG-10).
All six carry named cuts/repairs above; none breaks a landed verdict
sampled by this audit.

---

## 4. MACHINE SUMMARY

```json
{
  "findings": [
    {"id": "AG-1", "class": "OVERENGINEERED", "target": "proof-tier depth policy: (H-G8) gap-accounting row consumed 5 until-dry rounds before the sufficient-but-unoptimized restatement; no load-class valve exists at the proof tier (stop_proof:4706-4725)"},
    {"id": "AG-2", "class": "UNDERRIGOROUS", "target": "repair-landing sequencing: 29 wave-1 repair/amendment texts + 8 doc1 landing edits of record before any confirm pass; retroactive confirm-on-repairs conditional on wave-2 sustaining repairs>0 (BRIEF_wave2_refuter_judge:60-74; checkpoint:10-24)"},
    {"id": "AG-3", "class": "UNDERRIGOROUS", "target": "wave-1 landing gate: C27/C28 query-level-axis pass has no on-file verdict (checkpoint:105-116; grep-proven absent elsewhere)"},
    {"id": "AG-4", "class": "UNDERRIGOROUS", "target": "single-model (Fable) verification pool: seed calibration is model-authored, common-cause blind-spot risk unpriced in any registry (checkpoint:154-157,176-183,337-339)"},
    {"id": "AG-5", "class": "OVERENGINEERED", "target": "SESSION_STATE_checkpoint.md:142-299 superseded session-C history in the live opening path"},
    {"id": "AG-6", "class": "OVERENGINEERED", "target": "phaseD_stop_proof.md revision logs = ~2000/4964 lines (40%) inside the paper-source proof carrier"},
    {"id": "AG-7", "class": "AT-BAR", "target": "measurement-gated verdict labeling: 'converged-while-deferred' candidate refuted — MIXED/gated labels honest at verdict, ledger, and M0 carriers"},
    {"id": "AG-8", "class": "AT-BAR", "target": "per-wave stage count and layer policy: right-sizing + escalation valve governs depth; confirm-on-repairs evidence-priced and clause-scoped; the layer defect is AG-1's tier, not this one"},
    {"id": "AG-9", "class": "AT-BAR", "target": "census read-depth: both live under-depth instances self-caught (RC27-4 preprint wall; L-P 2025 held-on-disk); wave-1 censuses need a grandfathering rider, not retro-editing"},
    {"id": "AG-10", "class": "UNDERRIGOROUS", "target": "SR-12 enforcement placement: 3 inherited/unmeasured claims in one wave each caught only at downstream agent cost (incl. one full judge slot for the C52 id collision)"},
    {"id": "AG-11", "class": "AT-BAR", "target": "glossary ratchet: anti-bloat family rule + honest-scope clause already implemented (glossary.yaml:17-38)"},
    {"id": "AG-12", "class": "ABOVE-BAR", "target": "brief economy: binding-by-reference composition, demonstrable full consumption, declared non-adoption of ritual protocol elements"}
  ],
  "cuts_proposed": 3,
  "repairs_proposed": 5,
  "grades": {
    "review": "ABOVE",
    "verification": "ABOVE",
    "pipeline": "AT"
  }
}
```
