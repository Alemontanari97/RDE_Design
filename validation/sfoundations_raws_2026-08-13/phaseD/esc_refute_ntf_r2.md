# ESCALATED REFUTATION — MINOR (a) NTF, ROUND 2 (full form, single fused lens)
# S-FOUNDATIONS-C4 escalation E-1, 2026-08-20. Slot per VERDICT_blocco2
# §3 E-1 (escalation form of record: author-revision + refutation,
# until-dry with cap; single fused lens per orchestrator right-sizing).
# Target: revised phaseD_minor_ntf.md (all [ESC-r2-*] markers + §10
# dispositions). Inputs read IN FULL: phaseD_minor_ntf.md (r2 revision),
# esc_refute_ntf_r1.md, refute_minor_ntf.md, VERDICT_blocco2 §2.1 + §3
# E-1.
# Probe of this round (written+executed this window, exit 0):
#   esc_probe_ntf_r2_boundary_strictness.py (scenes E+F)
# Probes of record RE-RUN this window (all exit 0, printed numbers match
# the document verbatim):
#   esc_probe_ntf_r1_envelope_lower_bound.py (scenes C+D: 200/200 term,
#     max 7 trips, 87/200 PASS; 0/200, 0/200)
#   esc_probe_ntf_repaired_bound_window.py (16/16)
#   r22f_v2_probe_minor_ntf_pass_bound_and_termination.py (scenes A+B:
#     3.401*T > 2*T at ratio 0.990; 200/200 term max 3 trips, 6/200 FAIL)

## 0. Read-depth declarations (this refuter's own reads)

[FULL] phaseD_minor_ntf.md (r2 revision, incl. §9+§10 dispositions);
esc_refute_ntf_r1.md; refute_minor_ntf.md; all four probes (source).
[SECT] VERDICT_blocco2.md §2.1 (whole table + guidance labels), §3
(E-1..E-5 + escalation form of record :243-269), §2 preamble (:95-98
adoption rule).
[LINES] validation/a1_ideal_march_jax.py :166-202 (EPS :168, NTF :200,
N_NEWTON :201), :444-450 (loop exit = step <= T, continue while
step > T), :811-815 (cert ratio), :1446-1450 (replay band);
carrier s25bis_gap29_sweep.json: all four load-bearing numbers
re-grepped verbatim this window (cert_worst base/ntf50, o31_tol
base/ntf50 — script check, exact strings found).
[PAGES] Deuflhard CSM 35: book pp. 51-52 (PDF 62-63) re-read AT SOURCE
this window (the [ESC-r2-2] repair is a source claim — see
ESC-NTF-r2-2 for what the pages actually show).
NOT READ (declared, with reason): Yamamoto + Nocedal-Wright PDFs — no
[ESC-r2-*] marker changes what is claimed OF those sources beyond the
r1 refuter's index-shift reading of Yamamoto eq. (7), which the r2
revision adopts VERBATIM from the r1 finding (attribution-only, r1
verified it at source; nothing new to check); Deuflhard pp. 96-98/
130-131/147-148 and the four aux carriers [ADV] — untouched by round 2
(no [ESC-r2-*] marker in §0/§6/§7; CT-6 re-checked trivially: still no
nozzle-paper number in the file).

## 1. Repair-verification record (what was attacked and VERIFIED SOUND)

Per zero-inflation these are NOT findings; cited so the closure judge
sees coverage. Every [ESC-r2-*] repair was independently re-checked
this window:

1. ESC-NTF-r1-1 repair ([ESC-r2-1], H5): the refuter's named hypothesis
   is adopted VERBATIM in §4 (band [floor_z/(1+m), floor_z], m = 0.25
   sufficient-not-optimized, measured half = F2-NTF-TERMCOUPLE-
   TRIPCOUNT); the deterministic-envelope bullet is conditioned
   ("UNDER H5"); the scene-C counterexample is cited in-text as the
   reason H1-H4 alone never imply the bullet; the falsifier is tied to
   H5 ("= precisely a measured violation of H5's band" — checked: steps
   consistently below T*(1-band) at a cell with floor >= (1+m)*T do
   violate H5's lower edge, since floor/(1+m) >= T > T*(1-band));
   the falsifier's cell-selection clause "MEASURED kappa_eff >=
   (1+m)*NTF" is conservative in the right direction under the
   [ESC-r2-3] pin (realized <= envelope, so realized >= (1+m)*NTF
   implies the cell is genuinely in the envelope regime). §5 duty
   extended, §8 NTF-4 line updated, SCHEMA label kept. Scene D re-run
   confirms the conditioned claim in the strict interior (kappa =
   2*NTF: 0/200 terminations, 0/200 PASSes); scene C re-run confirms
   the unconditioned form stays rejected. SOUND in the interior — but
   the regime's closed BOUNDARY is a genuine residue: ESC-NTF-r2-1.
2. ESC-NTF-r1-2 repair ([ESC-r2-2]): (ii) "equivalently" retired,
   Yamamoto eq. (7) restated as previous-correction-at-source with the
   index-shift + triangle path named, geometric-series attribution
   declared primary — matches the r1 finding text exactly; SOUND.
   (i) span-narrowing to (2.10) — the source situation is subtler than
   the disposition table records: ESC-NTF-r2-2 (NOTE; the substance of
   the repair survives).
3. ESC-NTF-r1-3 repair ([ESC-r2-3]): the operational pin (kappa_eff =
   REALIZED per-cell extra-step multiple; kappa_q, LB, falsifier,
   bracket [51.7, 70.1] all ride the realized object; H5 converts
   realized -> envelope, envelope <= realized*(1+m)) is placed in the
   kappa-owning duty F2-NTF-FLOOR-POPULATION as the r1 note prescribed,
   with the trip-count duty riding via H5. Conversion direction
   re-derived: under H5, realized step >= floor_z/(1+m) implies
   kappa_env <= kappa_realized*(1+m) — correct. Internal consistency
   re-checked against §3 (falsifier + derived form pinned to the
   measured population): holds. Arithmetic: 70.11026...*1.25 = 87.6378
   — the disposition table's own verification cell prints 87.6375;
   the BODY's "<= 87.6" rounds an upper bound down: ESC-NTF-r2-3
   (NOTE). Otherwise SOUND.
4. §10 dispositions table: 3/3 checked against the r2 body — every
   "Where applied" anchor exists and does what the table claims; the
   declared deviations (span-narrowing option chosen; duty-sentence
   placement) are legitimate and match the r1 refuter's own options.
   One bookkeeping sentence is literally false as printed:
   ESC-NTF-r2-4 (NOTE).
5. Non-regression sweep: no [ESC-r2-*] marker in §0 (seam untouched —
   C34/C35 consumption text verbatim-unchanged from the round-0
   COMPLIANT state); §9's r1 dispositions untouched as append-only
   record; the r1 refuter's §1 verified-sound record (11/12 + the
   falsifier half of [ESC-r1-3]) spot-re-checked at the four corners
   most at risk from the r2 edits (NTF-2 composition text, NTF-3
   LB/UB/window, §8 machine lines, falsifier texts) — no regression.
   Code anchors re-verified at source this window: loop exit at
   step <= T (a1 :444-448, continue-while step > T), cert PASS iff
   ratio <= 1 (:813), NTF = 100.0 (:200), EPS (:168), replay band
   10*NTF*EPS*scale (:1448). Carrier numbers re-grepped verbatim.
6. Prior-round objections status: ESC-NTF-r1-1 RESOLVED (modulo the
   boundary residue below, which is NEW, not a persistence — scene C's
   defect was the missing hypothesis; the boundary defect is in the
   adopted hypothesis's closed-set arithmetic); ESC-NTF-r1-2 RESOLVED
   (modulo the source nuance below); ESC-NTF-r1-3 RESOLVED. No r1
   objection persists unaddressed.

## 2. FINDINGS

### ESC-NTF-r2-1 — AMENDMENT. The H5-conditioned deterministic-envelope
claim fails at the regime's included boundary point: the scoping needs
one strict inequality. Executable counterexample, probe scene E.
Claim attacked (r2 §4 bullet, [ESC-r2-1]): "DETERMINISTIC-ENVELOPE
regime, kappa_eff(cell) >= (1+m)*NTF: UNDER H5 (whose lower edge gives
realized step >= floor_z/(1+m) >= T(z) in this regime),
metric-termination is unreachable at that cell — the loop exhausts
N_NEWTON = 30 trips ... AND the cell then fails certification."
Reason: the regime is defined with >= and H5's band is CLOSED, so the
boundary point kappa_eff = (1+m)*NTF is IN the regime, where the band's
lower edge EQUALS T(z). H5 is a deterministic band hypothesis (no
distribution), so the adversary may realize step == floor_z/(1+m) == T
at every trip — the same adversarial-edge game scene A of record
already plays with the noise floor. Engine semantics verified at source
this window: the loop EXITS at step <= T (a1 :444-448 continues only
while step > T), and cert PASS iff ratio <= 1 (:813) — so step = T
terminates at trip 1 AND passes certification at ratio 1.0. EXECUTABLE
COUNTEREXAMPLE (probe scene E, exit 0 this window): kappa_eff =
(1+m)*NTF exactly, H5-admissible edge realization — 200/200 metric
terminations at trip 1 (claim predicts 0, cap 30) and 200/200 cert
PASSes (claim predicts 0): BOTH conjuncts fail under H5 at a point the
scoping includes. Named repair (one-character-class): define the
deterministic-envelope regime STRICT, kappa_eff(cell) > (1+m)*NTF, and
the near-threshold band as NTF < kappa_eff(cell) <= (1+m)*NTF;
propagate to the parenthetical "realized step >= floor_z/(1+m) >= T(z)"
(becomes > T(z)) and to §8's NTF-4 line ("unreachability only at
kappa_eff > (1+m)*NTF UNDER H5"). Probe scene F verifies the
strict-scoped claim HOLDS against the WORST H5-admissible realization
(band lower edge): 0/200 terminations (cap exhausted), 0/200 PASSes —
deterministic check, hence valid for all admissible realizations. What
SURVIVES unchanged: H5 itself (band and m = 0.25 as declared — the
repair moves the regime edge, not the band), scenes C/D (both taken at
kappa = 2*NTF, strict interior — their verdicts unaffected), the
near-threshold fluctuation text (the boundary point moves INTO the
fluctuation band, where the model claims nothing deterministic —
consistent), the re-pinned falsifier (its cell-selection ">= (1+m)*NTF"
may stay closed: for SELECTION it is conservative, and its firing
condition "steps consistently below T*(1-band)" already carries the
margin that excludes the edge case), the F2 duties, and the SCHEMA
label. Zero effect on NTF-1/2/3, the incumbent adjudication, or the
seam.

### ESC-NTF-r2-2 — NOTE. [ESC-r2-2](i) "span opened at (2.10), the
first display ON the declared read pages": true only under a
content-display reading, and it silently resolves a discrepancy inside
the r1 refuter's own record — one clarifying parenthetical would close
it cleanly.
Verified at source this window (book pp. 51-52 = PDF 62-63): the
NUMBERED display "(2.10)" does NOT appear on pp. 51-52 — it sits on
p. 50 (unread; same page-status as (2.8)). What p. 51 carries, as its
first display, is the UNNUMBERED restatement ||e_{k+1}|| <=
(1/2)*omega*||e_k||^2 immediately identified in-text as "which is just
(2.10)" (and (2.10) is referenced again two lines later, "Insertion
into (2.10)"). The first NUMBERED display on p. 51 is (2.11). So: the
revision's sentence is defensible — (2.10)'s CONTENT is displayed and
source-identified on the read page, which is a genuinely stronger
status than (2.8) on p. 52 (referenced by number only, content never
shown), so the distinction the repair draws is REAL and the repair's
substance stands. But the r1 refuter's own file says both "(2.11)-
(2.16) verified at source" (its §0 header) and "pp. 51-52 display
(2.10)-(2.16)" (its finding (i)) — the r2 disposition table cites the
latter as "the refuter's source verification of record" without
noting the former. In an item three times dinged for equation-level
attribution precision, the honest one-touch form is: "(2.10) —
restated unnumbered and identified in-text ('which is just (2.10)') on
p. 51; the numbered display sits on p. 50". Optional touch; zero
mathematical damage; the geometric-series attribution remains primary
and sound.

### ESC-NTF-r2-3 — NOTE. §5 [ESC-r2-3] rounds a stated upper bound
DOWN: "envelope kappa (<= 87.6 at m = 0.25)".
The derivable bound is 70.110 * 1.25 = 87.6375 (from the verbatim
carrier multiple 70.11026..., 87.6378) — the §10 verification cell
itself prints 87.6375 and glosses it "~87.6", but the BODY asserts
"<= 87.6", which is 0.04% TIGHTER than what H5 licenses. R5 number
discipline: bounds round OUTWARD. Fix: "<= 87.64" (or "< 87.7").
Immaterial to every conclusion (the number is a duty-time estimate
under declared m and appears nowhere else); recorded because a stated
"<=" with an unlicensed tightening is exactly the class this loop
exists to catch.

### ESC-NTF-r2-4 — NOTE. §10 bookkeeping sentence literally false as
printed: "no [ESC-r2-*] marker rewrites any [ESC-r1-*] repair text".
The [ESC-r2-2] touch DID rewrite text inside the [ESC-r1-4] repair:
the cite span "(2.8)-(2.14)" (recorded as the r1-applied text in §9's
MIN-NTF-4 row) became "(2.10)-(2.14)" in the body. The change is
exactly what the r1 refuter asked for, and the SAME §10 sentence goes
on to name "two attribution touches" — so the record self-clarifies
and no content is at risk; but the blanket clause contradicts the
file's own §9 row. One-word fix: "no [ESC-r2-*] marker REVERTS or
WEAKENS any [ESC-r1-*] repair". Same sentence: "(iii)'s duty sentence"
mislabels finding ESC-NTF-r1-3 with the residue-numbering style used
for r1-2's (i)/(ii) — cosmetic, worth aligning while touching the
line. Pure bookkeeping; §9 itself correctly stays append-only.

## 3. Coverage statement (attacked and HELD, beyond §1)

- The conditioned NTF-4 bullet in the STRICT INTERIOR of the regime:
  attacked via scene D re-run and the scene-F worst-case argument —
  HOLDS (the sole defect is the boundary point, ESC-NTF-r2-1).
- H5's compatibility with the rest of the document: checked that no
  OTHER statement silently consumes a lower noise bound (NTF-1's floor
  model, NTF-2's composition, NTF-3's LB/UB use only the H3 upper
  envelope; the [ESC-r2-3] realized->envelope conversion uses H5
  exactly where declared) — HOLDS.
- "LB protects BOTH contracts ([ESC-r2-1] the termination-side
  protection read under H5)": under LB with eta >= 1.25 = 1+m, the
  envelope of the H5 band sits at or below T for every cell (kappa_env
  <= (1+m)*kappa_q <= NTF at the bracket's lower edge), so realized
  steps <= floor <= T and termination is guaranteed — the sentence is
  in fact provable from H3 alone on the realized object; reading it
  under H5 is over-cautious but nowhere false. HOLDS.
- The kappa_q (quantile) vs kappa_eff,max (LB text) pairing in §3 is
  pre-existing round-0 text, explicitly declared (quantile chosen at
  duty time, falsifier pinned to q95), attacked by neither prior
  refuter and not touched by round 2 — re-read, still internally
  consistent as a SCHEMA with its measured half named. NOT REOPENED.
- §10 disposition fidelity (beyond the r2-4 sentence): 3/3 anchors and
  probe-number claims verified against my own re-runs — HOLDS.
- Seam (§0), C34/C35 threshold-object consumption, incumbent
  adjudication (100 valid instance, headroom 1.426; /2 flip = model
  prediction, ntf50's own 51.665 > 50 witness): all
  verbatim-unchanged by round 2; round-0 COMPLIANT verdict stands.
- All four probes: executed this window, exit 0, pinned-env deps only
  (numpy/stdlib), re-runnable from the phaseD directory; printed
  numbers match the document verbatim.

## 4. PAPERS NEEDED

None new. (The boundary counterexample needed only the engine source
and stdlib; Deuflhard re-read stayed within the already-arrived PDF;
Higham stays conditional as filed; More-Wild stays the deduplicated
wave-3 entry.)

## 5. Machine summary

item: minor (a) NTF — ESCALATED REFUTER round 2 (full form, single
  fused lens: math structure + carrier/bookkeeping contracts)
probe_this_round: esc_probe_ntf_r2_boundary_strictness.py (scenes E+F,
  exit 0 this window)
probes_of_record_rerun: [esc_probe_ntf_r1_envelope_lower_bound.py
  (C+D, exit 0), esc_probe_ntf_repaired_bound_window.py (16/16,
  exit 0), r22f_v2_probe_minor_ntf_pass_bound_and_termination.py
  (A+B, exit 0)]
findings:
  ESC-NTF-r2-1: AMENDMENT — H5-conditioned deterministic-envelope
    claim fails at the included boundary kappa_eff = (1+m)*NTF (H5's
    closed band admits step == T, which terminates at trip 1 AND
    passes cert at ratio 1.0, per a1 :444-448/:813 semantics); probe
    scene E: 200/200 terminations at trip 1, 200/200 PASSes; repair =
    strict regime kappa_eff > (1+m)*NTF (near-threshold band NTF <
    kappa <= (1+m)*NTF), propagated to the in-bullet parenthetical and
    §8; scene F verifies the strict form against the worst
    H5-admissible realization; H5, scenes C/D, falsifier, duties,
    SCHEMA label all survive.
  ESC-NTF-r2-2: NOTE — [ESC-r2-2](i) source nuance: numbered display
    (2.10) sits on p. 50; p. 51 carries its unnumbered restatement
    identified in-text ("which is just (2.10)") as the first display —
    claim true under the content reading (and strictly stronger status
    than (2.8), so the repair's substance stands), but the r1
    refuter's own header said "(2.11)-(2.16)"; one clarifying
    parenthetical closes it. Optional touch.
  ESC-NTF-r2-3: NOTE — §5 stated bound "<= 87.6" rounds an upper bound
    down (derivable: 87.6375/87.638); R5 outward-rounding fix
    "<= 87.64". Immaterial to conclusions.
  ESC-NTF-r2-4: NOTE — §10 sentence "no [ESC-r2-*] marker rewrites any
    [ESC-r1-*] repair text" contradicted by the file's own §9 MIN-NTF-4
    row ((2.8)->(2.10) span change); reword "reverts or weakens";
    "(iii)" labeling cosmetic. Bookkeeping only.
counts: {breaks: 0, repairs: 0, amendments: 1, notes: 3}
prior_round_objections: ESC-NTF-r1-1/-2/-3 all RESOLVED (r2-1 is a new
  boundary residue in the adopted H5 scoping, not a persistence; r2-2
  is a source-precision nuance on the adopted span, substance stands)
repair_verification: 3/3 [ESC-r2-*] repairs verified applied and sound
  in substance (§1); defects found are one strict-inequality scoping
  (amendment-sized, probe-verified repair named) and three
  precision/bookkeeping notes
citation_source_checks_this_window: Deuflhard book pp. 51-52 (PDF
  62-63) re-read — (2.11) first numbered display on p. 51; (2.10)
  content-restated and identified in-text; (2.12)-(2.16) on p. 52;
  (2.8) referenced by number only. Code anchors a1 :168/:200/:201/
  :444-448/:813/:1448 verified; carrier numbers re-grepped verbatim.
papers_needed: none
