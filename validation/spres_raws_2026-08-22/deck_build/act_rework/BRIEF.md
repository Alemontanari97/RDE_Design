# ACT-REWORK BRIEF — final act rebuild (S4 lot 3, user-ordered workflow)

**Confronto/record stage**: NARRATIVE_SPINE_v2.md blocks [41/C11], [42/C17-pre],
[43/C17], [44/C18], [45/C19] (SENSE contracts of record) + specs_c34.py (current
on-slide text + notes with provenance anchors).
**Consumption arc**: proposals in this folder → S4 orchestrator implements them
into specs_c34.py → assert-gated rebuild → user gate. Nothing here is of record
until implemented and rebuilt.

## USER VERDICT (verbatim, binding)
"le slide da 41 a 46 non le capisco, non capisco che messaggio vogliono
comunicare, non sono assolutamente sota, sono ancora chiaramente AI flavor."
(In the current 69-slide build the act is positions 42-46: C11, C17-pre, C17,
C18, C19. C16-bis has been MOVED to backup already — do not resurrect it.)

## DIAGNOSIS TO BEAT
These slides narrate PROCESS and META (error accounting, gap taxonomy,
pre-registration, asks bureaucracy) instead of ENGINEERING CONTENT. The fix is
not polish: each slide must be rebuilt around ONE concrete engineering
statement a first-time listener can repeat, with a visual that shows the thing
itself (numbers, physical channels, an ordered plan with physical quantities).

## HARD RULES (binding, from CKP-S3-1 + S4 orders)
1. Per slide: title-assertion ≤ ~10 words; ≤3 short bullets (≤15 words each)
   or ≤4 cards; ~35 net words target, cap 60 (cards 100); prose lives in the
   speaker notes, never on-slide.
2. FORBIDDEN on-slide (meta/process/AI-flavor register): audit, hostile,
   pre-registered, honest/honesty, declared, contract (as self-praise),
   "of record", owner, window, phase, roadmap, "we say so", "decision rule",
   bracket, channel (as bureaucratic tally), aphorisms, ALL-CAPS (except one
   kept SUBSTITUTE on C7-bis, untouched here). Honesty is SHOWN by numbers
   and falsifiable statements, never narrated.
3. Author-year for any literature reference. No internal ids (M-RED, CFD-1/2,
   PB-2, S-*, C-numbers) on-slide — they live in notes only.
4. NO NEW CLAIMS AND NO NEW NUMBERS: every rewritten statement must be
   traceable to the current slide's notes [PROVENANCE] block or the spine
   block SENSE. If a statement cannot be anchored, drop it. Class discipline:
   a rewritten claim may WEAKEN, never strengthen, the anchored claim.
5. The SENSE contract of each spine block must survive: the listener must end
   the slide thinking THAT thought, expressed in engineering words.
6. Keep the deck's visual grammar (cards/bands/figs of the existing layouts);
   a new visual concept is allowed per slide if it is buildable with the
   existing layout library (cards, bands, arrows, tables, matplotlib home
   figure) and shows content, not decoration.

## FILES (absolute paths)
- Renders of current act + context: act_rework/ctx-34.png … ctx-46.png
  (34=C9, 35=C2, 36=C10, 37=C-ADJ, 38=C13, 39=C14, 40=C13-val, 41=C16,
  42=C11, 43=C17-pre, 44=C17, 45=C18, 46=C19) in
  validation/spres_raws_2026-08-22/deck_build/act_rework/
- Spine contracts: validation/spres_raws_2026-08-22/deck_build/NARRATIVE_SPINE_v2.md
- Current specs + notes: validation/spres_raws_2026-08-22/deck_build/specs_c34.py
  (ids C11 in specs_c12.py — check both; C11 may live in specs_c12.py)
- Register rules of record: BUILD_LOG.md sections CKP-S3-1 and CKP-S3-5.

## DELIVERABLE FORMAT (per slide, for the rewriter)
For each of C11, C17-pre, C17, C18, C19:
- TITLE: (assertion, ≤10 words)
- ON-SLIDE: exact bullets/cards/bands text (final wording)
- VISUAL: concept in one paragraph, buildable with existing layouts
- SCRIPT: 6-12 spoken sentences (plain engineering, first-encounter)
- ANCHORS: per statement, the provenance pointer copied from current notes
