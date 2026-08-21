# ESCALATED REFUTATION — MINOR (a) NTF, ROUND 1 (full form, single fused lens)
# S-FOUNDATIONS-C4 escalation E-1, 2026-08-20. Slot per VERDICT_blocco2
# §3 E-1 (escalation form of record: author-revision + refutation).
# Target: revised phaseD_minor_ntf.md (all [ESC-r1-*] markers + §9
# dispositions). Inputs read IN FULL: phaseD_minor_ntf.md (revised),
# refute_minor_ntf.md, VERDICT_blocco2 §2.1 + §3 E-1 (+ §4 sequencing
# lines relevant to E-1: none binding — E-1 is independent).
# Probe of this round (written+executed this window, exit 0):
#   esc_probe_ntf_r1_envelope_lower_bound.py (scenes C+D)
# Probes of record RE-RUN this window (both exit 0):
#   esc_probe_ntf_repaired_bound_window.py (16/16 checks)
#   r22f_v2_probe_minor_ntf_pass_bound_and_termination.py (scenes A+B)

## 0. Read-depth declarations (this refuter's own reads)

[FULL] phaseD_minor_ntf.md (revised, incl. §9 dispositions);
refute_minor_ntf.md; both probes of record (source);
s25bis_gap29_sweep.json (committed carrier, whole file).
[SECT] VERDICT_blocco2.md §2.1 (whole table + labels), §3 (E-1..E-5),
§2 preamble (:95-98 adoption rule), §4 head (E-1 independence).
[LINES] validation/a1_ideal_march_jax.py :160-204 (EPS :168, NTF :200,
N_NEWTON :201), :427-473 (termination cond :444-448, metric :469),
:790-828 (certify, threshold :813), :1442-1450 (replay band :1448);
validation/s25bis_gap29_sweep.py :55-109 (k_newt :66, o31 :98-103);
docs/findings_registry.yaml :214-222 (engine-core:F5-underived-factors),
:328-336 (engine:cross-lowering-gradient-floor);
docs/choice_ledger.yaml :324-333 (row C18).
[PAGES] Deuflhard CSM 35: book pp. 51-52 (PDF 62-63) — (2.11)-(2.16)
verified at source; Nocedal-Wright 2ed: book pp. 614-615 (PDF 633-634)
— (A.30)/(A.31) verified at source; Yamamoto 1986: pp. 91-92 (PDF 1-2,
rendered — no text layer, confirming both prior declarations) — Thm 2
eq. (6)-(7) verified at source.
NOT READ (declared, with reason): Deuflhard pp. 96-98/130-131/147-148
and the four aux carriers ([ADV] SYNTHESIS/FIELD_ATLAS/BASE_PRESSURE/
addendum) — the round-0 refuter verified the NLEQ-RES/NLEQ-ERR quotes
verbatim at source and no [ESC-r1-*] repair touches them; this item
touches no nozzle-paper content (CT-6 trivially respected, re-checked:
the revised file still contains no number from the four nozzle papers).

## 1. Repair-verification record (what was attacked and VERIFIED SOUND)

Every [ESC-r1-*] repair was re-checked independently this window; the
following are VERIFIED — cited so the closure judge sees coverage, per
zero-inflation these are NOT findings:

1. MIN-NTF-1 repair (PASS constant 2*(T+floor)): the composition is
   re-derived sound — PASS gives ||dz_hat|| <= T, H3 noise can cancel,
   so ||dz_exact|| <= T + floor; geometric-series estimator (factor
   <= 2 at Theta <= 1/2, supplied by H2) gives err <= 2*(T+floor) =
   2*(NTF+kappa_eff)*EPS*sc <= 2*NTF*(1+1/eta)*EPS*sc under LB.
   Probe scene A re-run: PASS at ratio 0.990, err 3.401*T > 2*T (old
   constant rejected), err/repaired-bound = 0.945. Propagation into
   NTF-2 falsifier, NTF-3 UB (2*(1+1/eta)*NTF*EPS*sc*A_c <= tol_c),
   window condition (2*(eta+1)*kappa*EPS*sc*A_c <= tol_c — the
   substitution NTF = eta*kappa checked exact), eta decade argument
   (2*(eta+1) <= 7 < 10 at eta = 2.5), §8: ALL PRESENT and correct.
2. MIN-NTF-2 repair (declared A_c): arithmetic re-derived — certified
   error 2*(1+1/1.25)*100*EPS = 7.994e-14; at A_c = 1e7 vs o31_tol =
   7.646e-2 the margin is 10^4.98 (~5 orders, >= 4 conservative);
   ">11 orders" reproduced ONLY at A_c = 1 (10^11.98) — retirement
   correct. The eta = 1.25 form upper-bounds the measured incumbent
   case (2*(100+70.1)*EPS = 7.55e-14 < 7.994e-14): conservative
   direction correct. A_c = 1e7 class faithfully sourced at registry
   :328-336 ("FD consumers amplify this ~7 orders"), declared
   sufficient-not-optimized — AG-1-conformant; THEOREM* correctly
   stated conditional-on-declared-A_c.
3. MIN-NTF-3 repair: the falsifier RE-PIN (margin-scoped,
   deterministic-envelope cells only) is SOUND — the spurious-
   retraction hazard is disarmed; the near-threshold fluctuation-band
   text is sound and does explain ntf50's 1.033-yet-terminating. The
   REGIME-SPLIT CLAIM ITSELF is NOT fully repaired — see
   ESC-NTF-r1-1 (the one finding of this round that needs a repair).
4. MIN-NTF-4 repair: Deuflhard (2.13)/(2.14) verified AT SOURCE this
   window (PDF 62-63): (2.14) denominator is 1 - Theta^2_{k-1}
   exactly as the revision now states; the geometric-series
   re-attribution is true math (probe R1). Residue: ESC-NTF-r1-2.
5. MIN-NTF-5/-12 repairs: carrier numbers verified VERBATIM in
   s25bis_gap29_sweep.json — cert_worst 0.7011026275409529 (base) /
   1.033309604151919 (ntf50), o31_tol 0.07646234499018467 ->
   0.07960727353540988 (drift 4.11%), flip row = [ntf50,
   cert_verdict] only; witness 51.665 > 50 (3.33%), headroom
   100/70.110 = 1.4263 in [1.25, 2.5]. All correct.
6. MIN-NTF-6 repair: kappa_eff = ||J^{-1}||*gamma_R*S_R/sc checked
   dimensionally consistent with floor_z = ||J^{-1}||*gamma_R*EPS*S_R;
   EPS appears exactly once. Sound.
7. MIN-NTF-7 repair: (A.30) p. 614 storage / (A.31) p. 615
   per-operation, same bound u ~= 1.1e-16 = EPS/2 — verified AT
   SOURCE this window (PDF 633-634). Sound.
8. MIN-NTF-8 repair: rows["k_newt"] = int(c1["K_NEWT"]) verified at
   sweep script :66; json k_newt = 2 in all four arms; no per-cell
   trip field in the json. Sound.
9. MIN-NTF-9 repair: threshold object T vs certified-error object
   2*(T+floor) disambiguated in §2 and §8 NTF-5; C34/C35 consumption
   statement unchanged (seam intact). Sound.
10. MIN-NTF-10 repair: Yamamoto eq. (7) verified AT SOURCE (rendered
    p. 92): lower half 2||x_{n+1}-x_n||/(1+sqrt(1+4th^{2^n}/
    (1+th^{2^n})^2)); worst denominator 1+sqrt(2) at th -> 1, c_L =
    2/(1+sqrt(2)) = 0.8284 > 1/2. Sound (1/2 valid-conservative,
    1.66x tightening correctly flagged to F2).
11. MIN-NTF-11 repair: cert dict carries worst + n only (a1:793,
    :819-820); no per-cell Theta anywhere in the march or sweep —
    the honest H2 restatement is correct. Sound.
12. Bookkeeping: mandate row :214-222 quoted faithfully (owner,
    trigger, a1:195-205); C18 at ledger :324-333 (drift note still
    correct); seam text (one window, four riders) unchanged from the
    round-0 COMPLIANT verdict — no [ESC-r1-*] repair touched the seam.
    §9 dispositions table: 12/12 checked against the revised body —
    every "Where applied" anchor exists and says what the table
    claims; both declared deviations ((i) ~5-orders refinement keeping
    the >= 4 clause; (ii) m = 0.25 where the refuter left m free) are
    legitimate and declared. Probes: both re-run this window, exit 0,
    printed numbers match the document verbatim (16/16; scenes A+B).

## 2. FINDINGS

### ESC-NTF-r1-1 — REPAIR. The [ESC-r1-3] deterministic-envelope
regime claim is still not an implication of H1-H4: the MIN-NTF-3
defect (envelope != per-realization) was moved to the (1+m) boundary,
not removed. Executable counterexample, scene C.
Claim attacked (revised §4, first bullet): "DETERMINISTIC-ENVELOPE
regime, kappa_eff(cell) >= (1+m)*NTF: metric-termination is
unreachable at that cell — the loop exhausts N_NEWTON = 30 trips
(C17's cap becomes the de facto terminator ...) AND the cell then
fails certification." Reason: H3 bounds ||delta|| from ABOVE only —
the revision's own near-threshold text says exactly this ("it does
not pin each per-trip realization") — so NO lower bound on the
realized step exists at ANY kappa_eff/NTF ratio; the flat
"unreachable ... AND fails" in the scoped regime is asserted, not
derived, for every m. EXECUTABLE COUNTEREXAMPLE (probe scene C, exit
0 this window, SAME H3-consistent sampling class as the sustained
scene B, uniform(0, floor)): kappa_eff = 2*NTF (deep inside the
declared regime at m = 0.25), 200 cells — metric termination reached
at 200/200 cells (max 7 trips vs cap 30) and 87/200 cells PASS
certification: BOTH conjuncts fail. Note the escalation probe of
record verifies only that scene B sits INSIDE the near-threshold band
(check R4); no check of record tests the deterministic-regime claim —
consistent with it being untestable without the missing hypothesis.
Named repair (one sentence, amendment-sized in text but load-bearing
in logic): state the band hypothesis EXPLICITLY as a hypothesis —
e.g. "H5 (fluctuation band, measured half = F2): per-trip realized
steps at a converged cell lie within [floor_z/(1+m), floor_z]; m =
0.25 declared sufficient-not-optimized, ratified or superseded by
F2-NTF-TERMCOUPLE-TRIPCOUNT's measured band" — and condition the
deterministic-envelope bullet on H5 ("under H5, metric-termination is
unreachable ..."). Probe scene D verifies the conditioned claim HOLDS
at kappa_eff = 2*NTF under H5 (0/200 terminations, cap exhausted;
0/200 cert PASSes). What SURVIVES unchanged: the regime split itself,
the m = 0.25 declaration, the near-threshold fluctuation-band text,
the RE-PINNED falsifier (it already measures exactly the H5 band —
"steps consistently below T*(1-band)"), the F2 duty as extended, and
the SCHEMA label (honest once H5 is explicit). The LB-protects-both-
contracts sentence survives with H5 read into it.

### ESC-NTF-r1-2 — NOTE. Two secondary-attribution residues in
[ESC-r1-4] (precision only; the primary attribution now carries the
statement).
(i) The inline cite "(cf. Deuflhard CSM 35, (2.8)-(2.14), book pp.
51-52, read [PAGES])" opens the span at (2.8), which is NOT displayed
on the declared read pages (verified this window: pp. 51-52 display
(2.10)-(2.16); p. 52 only REFERENCES (2.8) — "In view of (2.8) and
with h_k -> [h_k] = 2*Theta^2_{k-1} ..."); §6 declares pp. 51-53
read, so (2.8) sits on an unread page. A "cf." span tolerates this;
in an item twice dinged for equation-level attribution precision,
either open the span at (2.10) or extend the declared read one page.
(ii) "equivalently, the Yamamoto eq. (7) upper half, already cited in
(b), is a two-sided source": at source the upper half bounds
||x* - x_n|| <= th^{2^n - 1} * ||x_n - x_{n-1}|| — the PREVIOUS
correction, not the current one; the current-correction form
err <= 2*||dz_k|| follows only via an index shift plus one triangle
step (||x*-x_n|| <= ||dz_n|| + ||x*-x_{n+1}||, then eq. (7) at n+1).
Eq. (7) IS two-sided as a display, so the sentence is literally true,
but "equivalently" overstates the directness. Suggested touch: "(cf.
also Yamamoto eq. (7), a two-sided display; its upper half yields the
current-correction form after an index shift + triangle step)". No
mathematical damage either way — the geometric-series attribution is
verified correct and suffices alone.

### ESC-NTF-r1-3 — NOTE. kappa_eff plays two roles that the F2 duty
window must reconcile explicitly (one definitional sentence at duty
time; nothing false today).
In §1 kappa_eff is defined as an ENVELOPE constant (via H3's bound);
in the measured instance, the bracket [51.7, 70.1], the incumbent
headroom 1.426, and the derived form's kappa_q ("upper quantile of
the measured per-cell kappa_eff population") all use REALIZED
extra-step multiples. Under the revision's own fluctuation-band
picture (and ESC-NTF-r1-1's H5), realized <= envelope with ratio down
to 1/(1+m): the measured 70.110 is then a LOWER estimate of the
envelope kappa at that cell (envelope <= 70.110*(1+m) = 87.6 at m =
0.25), and envelope-headroom is correspondingly smaller than the
realized-headroom 1.426. Internally the document stays consistent
because the NTF-3 falsifier and derived form are pinned to the
MEASURED population (same object both sides), and the F2 duty
measures the band; but the duty should pin ONE operational kappa_eff
(realized quantile, with the band converting to the envelope where
the deterministic-regime scoping needs it) so LB (measured-object)
and the NTF-4 regime split (envelope-object) do not silently use the
same symbol for two numbers up to (1+m) apart. Rides
F2-NTF-FLOOR-POPULATION + F2-NTF-TERMCOUPLE-TRIPCOUNT; no text is
wrong today (the worst-cell caveat and SCHEMA labels cover it).

## 3. Coverage statement (attacked and HELD, beyond §1)

- The repaired NTF-2 THEOREM* (constant 2*(T+floor)): attacked via
  independent re-derivation + probe re-run — HOLDS. The star's
  discharge condition (F2 floor measurement) is correctly stated.
- The repaired NTF-3 window (conditional on declared A_c): attacked
  via the incumbent-case arithmetic and the A_c sourcing — HOLDS;
  conservative direction of the eta = 1.25 form verified.
- Incumbent adjudication (100 valid instance, headroom 1.426; /2 flip
  = model prediction with the self-contained ntf50 witness): HOLDS.
- Seam position and consumption (§0): unchanged by the revision;
  round-0 COMPLIANT verdict stands — re-verified that no [ESC-r1-*]
  marker touched a seam-facing sentence except the [ESC-r1-9]
  disambiguation, which STRENGTHENS the C34/C35 contract.
- §9 dispositions: 12/12 faithful; deviations declared and legitimate;
  judge-guidance consistency paragraph accurate.
- Probes: all three (refuter scenes A+B; escalation 16/16; this
  round's scenes C+D) executed this window, exit 0, pinned-env deps
  only (numpy / stdlib math), re-runnable from the phaseD directory.

## 4. PAPERS NEEDED

None new. (The scene-C counterexample needed no source beyond disk;
Higham stays conditional as filed; More-Wild stays the deduplicated
wave-3 entry.)

## 5. Machine summary

item: minor (a) NTF — ESCALATED REFUTER round 1 (full form, single
  fused lens: math structure + carrier/bookkeeping contracts)
probe_this_round: esc_probe_ntf_r1_envelope_lower_bound.py (scenes
  C+D, exit 0 this window)
probes_of_record_rerun: [esc_probe_ntf_repaired_bound_window.py
  (16/16, exit 0), r22f_v2_probe_minor_ntf_pass_bound_and_termination
  .py (A+B stand, exit 0)]
findings:
  ESC-NTF-r1-1: REPAIR — [ESC-r1-3] deterministic-envelope claim not
    derivable from H1-H4 for any m (envelope bounds noise above only);
    probe scene C: kappa=2*NTF, 200/200 terminations (max 7 trips),
    87/200 cert PASSes — both conjuncts fail in an H3-consistent
    instance; named repair = explicit H5 fluctuation-band hypothesis
    conditioning the bullet (scene D verifies the conditioned claim);
    regime split, falsifier re-pin, F2 duty, SCHEMA label all survive.
  ESC-NTF-r1-2: NOTE — [ESC-r1-4] residues: (2.8) opens the cite span
    off the declared read pages; Yamamoto eq. (7) upper half is
    previous-correction at source (current-correction form needs index
    shift + triangle); primary geometric-series attribution verified
    correct and carries the statement.
  ESC-NTF-r1-3: NOTE — kappa_eff envelope-vs-realized dual role;
    measured 70.110 is a lower estimate of envelope kappa (<= 87.6 at
    m = 0.25); duty window must pin one operational definition (rides
    the two named F2 duties; nothing false today).
counts: {breaks: 0, repairs: 1, amendments: 0, notes: 2}
repair_verification: 11 of 12 [ESC-r1-*] repairs VERIFIED SOUND
  (independent re-derivation + source reads + probe re-runs, §1);
  the 12th ([ESC-r1-3]) sound in its falsifier re-pin but incomplete
  in the regime claim (ESC-NTF-r1-1).
citation_source_checks_this_window: Deuflhard (2.13)/(2.14) PDF 62-63;
  Nocedal-Wright (A.30)/(A.31) PDF 633-634; Yamamoto eq. (6)-(7)
  PDF 1-2 (rendered). All match the revision's statements.
papers_needed: none
