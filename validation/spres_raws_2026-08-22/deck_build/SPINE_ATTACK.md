# SPINE_ATTACK — hostile review of NARRATIVE_SPINE_v2 + the 66-page render (2026-08-23)

Reviewer stance: senior ESA propulsion panelist + communication referee (Alley assertion-evidence,
Doumont signal-to-noise). Object: tmp_pages/deck_qa/s-01..s-66 (main s-01..s-45), NARRATIVE_SPINE_v2.md,
DECK_MANIFEST.md, BUILD_LOG CKP-S3-1..4, STORYBOARD_v3 content-of-record. Constraint respected
throughout: content frozen (storyboard assertions only); every repair below moves ONLY flow, form,
wording, or speech.

Severity: CRIT = would damage the briefing in the room or violates a binding user order;
MAJ = a hostile panelist scores against the group; MIN = polish, fix cheaply in the repair pass.

Verified in-window (not hearsay): banned-word grep on specs (`specs_c34.py`, `specs_c12.py`);
killed-content check on renders s-62 (C2 throat) and s-63 (C3-bis census) — BOTH PRESENT in backup,
so the spine's "verify at Block-2" worry on killed content is RESOLVED-POSITIVE.

==========================================================================
## CRITICAL

**F-1 [45/C19] Banned phrase on-slide — direct violation of CKP-S3-1.**
The right column bullet reads verbatim: "an incremental plan, already priced, with pre-registered
outcomes — and a declared honest-death criterion". CKP-S3-1 bans "honest death" ON-SLIDE by name
(notes are exempt; the note occurrence at specs_c34.py:494 is fine, the bullet at specs_c34.py:481
is not). This is the closing slide — the last thing the panel reads.
REPAIR: replace with "and a declared stop criterion" — the exact wording C17 (s-43) already uses
("measured gain below ~1% Isp → pivot to certification"), so the deck also gains consistency.

**F-2 [38/C13 vs 45/C19] The machine's anatomy contradicts itself on stage count and names.**
s-38 draws SIX stages (ENGINE DATA · FUNCTIONAL · FLOW SOLVE · ADJOINT · OPTIMIZER · CERTIFY); the
bullet directly beneath says "Eight stages, data contract → verdict"; s-45's miniature strip shows
EIGHT stages with DIFFERENT names (CONTRACT · REPRESENT · MARCH · CERTIFY · ESTIMATE · OPTIMIZE ·
AGGREGATE · VERDICT). A panelist counts six boxes while hearing "eight", then sees a different
eight-name machine on the summary slide. This is a live credibility bug in the section whose entire
message is "every choice on record".
REPAIR (form only): change the s-38 bullet to "Six stages here — the full eight-stage record, with
estimation and aggregation, is in backup"; OR redraw s-38 with the eight record stages under the six
spoken labels. Whichever is chosen, s-45's miniature must use the SAME naming as s-38.

**F-3 [backup s-60] The promised "honesty table, complete" is an empty placeholder.**
s-60 renders as a title plus the sentence "content assembled from the record at Q&A-map time
(Block 2)" — there is no table. The spine's C11 block claims "full table in backup (s-60)" and the
C11 speech will promise it. If a panelist asks "show me the full error table", the flip lands on a
stub that admits it was never built — worse than having no backup slide at all.
REPAIR: build the actual six-channel table with verbatim cells on s-60 before delivery (content
exists — it is C11's record), or strike every promise of it from C11's script and the spine.

**F-4 [44/C18] A fourth card is clipped at the right edge of the "Three asks" slide.**
Confirmed on the render: a fourth card enters the frame cut mid-word, contradicting the slide title
AND the A2 promise ("Three requests for the panel"). This is the payoff slide; a visible layout
overflow here reads as exactly the sloppiness the deck spends 40 slides disproving. The spine flags
it (MOVE-3) but under-weights it, and misses that the reliability-ladder mini-diagram bottom-right
is illegible at room distance (entry-gate caption unreadable).
REPAIR: exactly three cards; the overflow card's content to notes/backup; enlarge the ladder ~1.5x
or move it to backup and keep only the teal contract sentence.

**F-5 [23/C1] The C2-merge carrier bullet is destroyed by the footer collision.**
Bullet 3 ("Even the throat is unsteady, ~6:1 excursions — we design downstream of it") is overprinted
by the footer band and half-illegible. This bullet is the ONLY surviving on-slide trace of the C2
merge — as rendered, the merge silently loses its content, which is precisely the "killed content
must not vanish" failure mode. (s-62 in backup carries the full claim, so the record is safe; the
main-deck sense is not.)
REPAIR: shrink the figure row ~8%, keep three bullets clear of the footer.

**F-6 [37/C13-val] Internal programme jargon leaked into a main-deck figure.**
The plot titles/legends read: "Brick 2 of record (S18)", "reduced twin case NI=21, eps=4", "GENO
type-2 Rao contour (classical Mrao/eps loop)", "K_RICH x (GENO cross-res + class repr +
resampling)". "GENO", "S18", "Brick 2", "K_RICH" are internal identifiers with zero meaning to ESA
— on the one slide whose job is quiet credibility. The spine calls this slide "quietly devastating"
and never saw the labels: its VISUAL-SENSE was written from the storyboard, not the render.
REPAIR: re-render the figure with plain labels, data untouched — "classical construction (Rao)" vs
"variational route (adjoint gradient)"; band label "independent cross-code tolerance band"; strip
the internal case tag from the title.

**F-7 [15/A15] Title collision on a host-group slide (pre-existing, still present at 14:15).**
The teal subtitle "Λ sweep: stagnation-pressure losses grow with wave number" overprints the bold
in-body header "Pressure flow field comparison...". Host form is untouchable; a render defect is not
form. REPAIR: drop the in-body bold header line into clear space or suppress the teal subtitle —
one of the two must move; content untouched.

==========================================================================
## MAJOR

**F-8 [register, s-27/s-39/s-44] The tic "we say so" appears on three main slides.**
Verbatim: s-27 footline "A 1975 Russian precedent is still in procurement: we say so."; s-39 card
"the solver census is dated, and we say so"; s-44 band "(A contract prediction, not yet exercised
on real data; we say so.)" (+ s-66 backup "and we say so in the meantime"). Once is a stance; three
times on-slide is self-congratulatory honesty theater — exactly the LLM-process color CKP-S3-1
bans in spirit. The honesty is in the FACTS (procurement open, census dated, contract unexercised);
the phrase adds nothing a hostile reader will not discount.
REPAIR: delete the clause in all three; s-27 → "…is still in procurement — not yet read against the
original"; s-39 → end at "…the solver census is dated"; s-44 → end at "…not yet exercised on real
data".

**F-9 [register, s-31/s-33/s-38/s-43/s-44] Internal programme-management vocabulary on-slide.**
"the first campaign of the phase now opening" (s-31), "named owners and windows" (s-33), "declared,
with owner and window" (s-38), "phase just opened — September milestone" (s-43), "WHEN: within the
phase now opening" (s-44). Two failures: (a) "phase" collides head-on with ESA's own Phase-A/B/C
vocabulary — a panelist will momentarily parse it as an ESA programme phase; (b) "owner and window"
is internal tracking dialect, not propulsion English.
REPAIR (wording only, claims identical): "phase now opening" → "the campaign starting now" /
"first campaign, starting September"; "owner and window" → "with a named lead and date";
"named owners and windows" → "assigned, with dates".

**F-10 [30/C7-bis] The deciding theorem is typeset as a footnote on the deck's central slide.**
The spine says this is "the slide the panel should photograph", and its SENSE hangs on the theorem
("no single phase satisfies its own wall condition — the weighted mean does"). On the render that
sentence sits in the smallest type on the slide, in a pale pink band at the bottom, under two large
flow columns and two equation strips. The visual hierarchy tells the panel the columns are the
point and the theorem is a caption. The SENSE line is wishful as rendered.
REPAIR: enlarge the band type to bullet size and bold "the weighted mean does"; speech duty: stop
and read the band verbatim, then the second sentence ("optimal at no single operating point") as
the room's take-away.

**F-11 [41→45] The spine missed the deck's real terminal sag: five card/band slides in a row.**
s-41 (2 cards + bullets), s-42 (3 boxes + 3 stacked full-width bands), s-43 (4 cards + band + red
line), s-44 (3+1 cards + band + tiny ladder), s-45 (2 columns + band + tiny strip). Minutes ~48-58
contain no real image. The spine names only the host-corridor sag and the position-37 inversion;
this stretch is where a thousand-deck panelist actually checks their watch — same rhythm, same
geometry, all boxes.
REPAIR (no new content): (a) execute MOVE-2 — the C11 table landing after s-41 breaks the geometry
with a genuinely different visual form; (b) convert C17's four cards into one numbered left-to-right
arrow sequence (it is an ORDER — the form should show order, not a grid); (c) merge s-42's three
stacked bands into two (hypothesis+weak-point in one band, failure-condition in the second).

**F-12 [43/C17] "we already know what we will conclude in each case" invites the hostile reading.**
Verbatim bottom line: "Every outcome is pre-registered: we already know what we will conclude in
each case." A hostile panelist will read the second clause as "your conclusions are pre-decided" —
the opposite of the intended meaning — and someone in the room will say it aloud.
REPAIR (same claim): "Every outcome is pre-registered: the decision rule is fixed before the data
arrive."

**F-13 [41/C16-bis] The scope of "NOT CERTIFIABLE" is ambiguous on-slide — the deck's riskiest
ambiguity for this audience.** The verdict card says "not certifiable — two named defects" and the
third bullet says "defects moved from the object to the certifier: the floor rose" — too cryptic to
carry the scope. An ESA panelist can leave with "their tool is not certified" as the memory of the
slide, with no recollection that the defects hit the certification CHAIN, not the physics results,
and that one is already repaired.
REPAIR: card title → "Audit 2 — hostile, on the certification chain"; speech duty: state the scope
in the first sentence ("the audit judged our certifier, not the flow solutions — and it found the
certifier wanting"). Keep the starkness — it is the deck's credibility peak (the spine is right
about that). Also: "the floor rose" is a metaphor; "the standard got stricter" is plain.

**F-14 [33/C8-bis] Wall-of-text — the worst CKP-S3-1 violation left in the C section.**
109 net words (DECLARED-OVER); four bullets of 2-3 lines each; on-slide phrases that cannot be
parsed without the script: "closures at equal area ratio, never hardware", "an infinitesimal body
in supersonic flow pays only wave drag: sectors are compared whole". The declared card-mandate
tolerance does not cover ordinary bullets.
REPAIR: cut each bullet to its headline (≤12 words): "Configurations emerge as classes — not
presupposed" / "The global optimum is a tournament among sector optima" / "First verdict: plug
weakly dominates bell at certified closures" / "Certified splines per sector — no level-sets";
all qualifier prose to notes.

**F-15 [36→37 as-built + MOVE-1/MOVE-2 interaction] Endorsed, with one demand.**
The 36→37 bridge break is real (validation of a machine not yet introduced) and MOVE-1 heals it.
But the spine derives each MOVE's bridges in isolation and never walks the COMBINED order
35→38→39→37→40→41→36→42. I walked it: it holds, and it holds better than either move alone —
C11's bullet "Rao's classical scale: 0.04-0.34%" lands AFTER C13-val has introduced Rao's
benchmark, which the spine never noticed as a bonus weld.
REPAIR: adopt both moves; re-derive the seam bridges once against the combined order in the spine
before Block-2 audits consecutio, so the audit object is the real order, not two overlays.

==========================================================================
## MINOR

**F-16 [21/B1] The section's motor question is visually buried.** "Does an 'optimal' profile exist
for an RDE exhaust?" — the question the whole C section answers — is bullet 2 of the lower block,
same weight as its neighbors; the eye goes to the mesh and the stakes card. B1 is NOT in the
untouchable A7-A20 range. REPAIR: bold/color that one line, or speech duty: read it aloud as "the
question of the rest of this talk".

**F-17 [22/A6] The EAP formula strip is unexplained decoration as rendered.** Symbols F_g/A_8,
P_0, P_t3 are never glossed; the spine's claim that "the formula pre-loads the C-section" is
wishful for anyone who has not read Kaemming & Paxson. REPAIR: one caption line under the strip —
"the field's accepted average: a thrust-equivalent pressure — no error bar" — speech carries the rest.

**F-18 [29/C7-bis-pre] The punch card is the emptiest thing on the slide.** Three packed ancestor
cards, then "This programme: the variational optimum ON the family — never posed before" floating
in white space, plus a dead lower half. The layout makes the claim look thin exactly where it
should look strong. REPAIR: move the non-commuting formula INTO the fourth card (it is the reason
the ancestors fall short) and let the card carry visual weight.

**F-19 [26/C5] Bullet 3 is a non sequitur on-slide.** "Our design contract demands unimodality,
not flatness." — unmotivated internal vocabulary after two perfect evidence bullets; the
flatness→unimodality link is script material. REPAIR: move to notes; two bullets remain (the slide
gets leaner and the 1971 scan gains air).

**F-20 [31/C7-ter] Half the slide is an empty box.** The bottom band is two lines floating in a
container sized for eight; with three compact cards above, the slide reads as unfinished. REPAIR:
shrink the band to fit its text; optionally raise the cards' type one step.

**F-21 [40/C16 + 45/C19] "economic act(s)" — aphorism English, used twice.** "validation becomes
an economic act" / "validation campaigns as economic acts (minutes, not weeks)". The parenthesis
already says it better. REPAIR: "validation becomes affordable" on s-40's title band context;
s-45 keep "minutes, not weeks" and drop "as economic acts".

**F-22 [42/C17-pre + 29 + 38] ALL-CAPS chattiness recurs.** "which NOBODY has computed", "the
variational optimum ON the family", "MEASURABLE operator" (s-45), "SUBSTITUTE problem" (s-30).
One emphatic cap per deck is a choice; five is a voice. REPAIR: sentence case everywhere except at
most one deliberate instance (keep "SUBSTITUTE" on s-30 — it earns it).

**F-23 [45/C19] The miniature pipeline strip is illegible clutter.** The 8-stage reprise renders
~5 mm tall with an unreadable red annotation; as a "quiet reprise" it registers as noise, and its
naming conflicts with s-38 (see F-2). REPAIR: enlarge to legible height with s-38-consistent
labels, or cut it and let the two-column text close the deck.

**F-24 [spine/MOVE-5] The spine's bookkeeping premise is itself stale.** MOVE-5 declares
DECK_MANIFEST.md "STALE vs this render and must be regenerated" — but the manifest on disk already
describes the 66-page build (45 main + 21 backup, merges and cut-list logged, C2/C3-bis/C12/C15/
C17-bis at rows 62-66). The spine asserted staleness without re-measuring — the very SR-12 failure
it cites. REPAIR: strike MOVE-5's regeneration order; keep only the merge-deviation logging duty
and the killed-content check (which this attack has now verified PRESENT: s-62, s-63).

==========================================================================
## WHERE THE DECK WINS — do not flatten these in repair

1. **s-25 (C4) "Same hardware, two flowfields — and the optimum moves"** — the strongest
   quantitative slide: assertion title, published evidence left, three numbered claims right,
   ending on "no published work prices this error". Alley-perfect. Touch nothing.
2. **s-26 (C5) "A 1971 warning"** — the period-authentic scan is worth more than any redrawn
   figure; the fifty-year echo lands by itself. (Only F-19's third bullet moves.)
3. **s-28 (C7) "approximately applicable — with no error bar"** — quote card, SIZING/RANKING
   split, one thesis line. The leanest, sharpest slide in the deck; the thesis sentence is the
   talk. Protect its emptiness.
4. **s-30 (C7-bis) "Two different optimization problems"** — the two-column fork is the right
   central image and the panel WILL photograph it once F-10 promotes the theorem band.
5. **s-37 (C13-val) "the machine reproduces Rao"** — quietly devastating once F-6 strips the
   internal labels: overlay + log-deviation band needs no rhetoric at all.

(Honorable: s-22/A6 as the hinge — the retitle and move genuinely heal the old break; s-40/C16's
measured-vs-target table is the right form for the speed claim.)

==========================================================================
## TALLY
CRITICAL: 7 (F-1..F-7) · MAJOR: 8 (F-8..F-15) · MINOR: 9 (F-16..F-24)
Spine verdict: the arc holds and both reorders (MOVE-1/MOVE-2) are endorsed — but the spine was
written from the storyboard's intent more than from the renders (F-3, F-6, F-10, F-11, F-24 are
all visible-on-render facts the spine missed or asserted wrongly), and the deck still carries one
verbatim violation of a binding user order (F-1).
