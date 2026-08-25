# LOT-B BRIEF — theory-core rebuild (s-27..s-33, S4)

**Confronto/record stage**: NARRATIVE_SPINE_v2.md blocks [27/C6], [29/C7-bis-pre],
[30/C7-bis], [31/C7-ter], [32/C8], [33/C8-bis] + specs_c12.py (current on-slide
text + notes with provenance anchors and RIGOR CLASSES) + deck_audit findings.
**Consumption arc**: proposals here → S4 orchestrator implements into specs_c12.py
(+ new home figures where specified) → assert-gated rebuild → exact-persona
convergence listener (CKP-S4-1) → user gate.

## PERSONA CARD (CKP-S4-1, binding — copy into every listener/judgment)
The listener/audience is the EXACT audience of record: an **ESA propulsion
panel** — senior rocket-propulsion engineers, expert in classical nozzle design
(Rao/MoC), CFD and test, plus programme decision-makers. They know NOTHING of
this project's internals (nothing-assumed), they judge credibility, and they
decide on three requests at the end. 60-minute briefing.

## CONVERGENCE CRITERIA (CKP-S4-1 — a slide passes only on ALL four)
1. CHIAREZZA: the panel can paraphrase the slide in one sentence.
2. COMPLETEZZA: no essential question left unanswered and unrouted (an explicit
   deferral to notes/backup counts as routed).
3. COMPRENSIONE: the paraphrase == the spine SENSE contract.
4. COLLOCAZIONE: the slide sits at the right point of the arc; each content
   piece at the right level (main / backup / speaker notes).

## SCOPE + PROTECTIONS
- Slides in scope: s-27 (C6 lineage), s-29 (C7-bis-pre ancestors), s-30
  (C7-bis two problems — PROTECTED FORM: keep the two-column fork + promoted
  theorem band; repairs are register/wording/definition only, do not flatten),
  s-31 (C7-ter — FAIL by both listeners, full rebuild allowed), s-32 (C8),
  s-33 (C8-bis).
- s-28 (C7 'approximately') is UNTOUCHABLE (passed cleanly, protected).
- HARD RULES of act_rework/BRIEF.md apply verbatim (forbidden meta/process
  words, word budgets, author-year, no internal ids on-slide, NO new claims or
  numbers — anchors bind, weakening allowed, strengthening forbidden).

## LOT-B SPECIFIC ORDERS (user, 2026-08-23, binding)
A. **The organizing question** (user order + atlas CH6 :440/:490/:712): the
   programme's decisive question is: *per-phase design vs the classical
   variational design built on cycle-mean p0/T0, identical constraints, swirl
   excluded — does the optimal contour move, and how much thrust does the
   difference carry?* s-31 is the natural carrier (it is exactly "where the
   difference is a theorem"): rebuild it AROUND this question, with the break
   result as its answer-in-form and the measured rung-1 shift (+44–87% argmax,
   3–10 s Isp — existing anchored numbers) as its answer-in-size-so-far.
   C17 card 2 already carries the measurement; s-31 must plant the question.
B. **Theorem-status single vocabulary** (defuses the panel's killer question
   "which of your 'proven' claims are theorems?"): derive from the specs'
   notes rigor classes ONE plain 3-level wording, e.g. "proven (hypotheses
   stated)" / "proven, perimeter declared" / "proof laid out, completion in
   progress" — and apply it CONSISTENTLY on s-30/s-31/s-32. Never upgrade a
   class; the notes' class is the ceiling. s-32's current box ("Proof
   structure declared; complete proof in progress") must say WHICH result it
   scopes, so it cannot be read against s-30's theorem.
C. **s-29**: the non-commuting-mean inequality becomes the visual centerpiece
   (an equation strip exists: eqs/eq_ratio_mean.png — specify size/position);
   the "never posed before" claim keeps its query-bounded form.
D. **s-27**: the procurement caveat ("1975 Russian precedent…") moves to
   speaker notes; timeline stays; "quotient/certificates" either defined in
   six words or replaced by plain words.
E. **s-33**: internal ledger vocabulary ("named campaign", "9 DOF driver",
   "owners and windows", bare "certified") → engineering words from the notes;
   the plug-vs-bell first verdict becomes the headline it deserves (existing
   claim, existing class — no strengthening).
F. Home figures: where a slide needs a NEW drawing (e.g. s-31 three
   configurations: annular area-ratio-only / full adapted plug / truncated
   plug with the break), SPECIFY it precisely (panels, labels, what each shows)
   — the orchestrator will draw it in the deck palette (matplotlib).

## FILES
- Audit findings: deck_audit/LISTENER_S23_35.md (+ LISTENER_FULL.md rows
  s-27..s-33; AUDIT_SYNTHESIS.md rows for these slides).
- Renders: deck_audit/s-27.png .. s-33.png.
- Specs + notes: specs_c12.py (ids C6, C7-bis-pre, C7-bis, C7-ter, C8, C8-bis).
- Spine: NARRATIVE_SPINE_v2.md (blocks as listed above).
- Register rules: act_rework/BRIEF.md HARD RULES.

## DELIVERABLE FORMAT (per slide)
TITLE / ON-SLIDE (exact final text) / VISUAL (buildable concept; for new
figures: precise drawing spec) / SCRIPT (6-12 plain sentences) / ANCHORS
(per statement, copied from current notes or spine).
