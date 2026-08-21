# ESCALATED REFUTATION r1 — PHASE D MINOR (d) CROSS-LOWERING
# S-FOUNDATIONS-C4 Blocco 2 escalation window, 2026-08-20. Escalated
# refuter slot per VERDICT_blocco2 §3 E-4 (single fused lens,
# orchestrator right-sized: math structure + carrier/bookkeeping
# contracts in one pass). Target = the REVISED
# phaseD_minor_crosslowering.md (markers [ESC-r1-0..9]) + its
# disposition table + esc_probe_crosslowering_decades.py.
# ID prefix: ESC-CROSSLOWERING-r1-<n>. Zero inflation.

## VERIFICATION RECORD (what was checked, at what depth, this window)

- Revised phaseD_minor_crosslowering.md — [FULL], all [ESC-r1-*]
  markers and the EOF disposition table.
- refute_minor_crosslowering.md — [FULL] (the 8 findings vs the 8
  disposition rows: one-to-one, none dropped, none weakened in the
  mapping; both repair options of MIN-CROSSLOWERING-1 adopted, the
  -2 repair adopted in the stronger declared-AND-regraded form).
- VERDICT_blocco2.md §2.4 (:199-234), §3 E-4 (:256-258), LB-5
  (:491-500) — [FULL] at lines. The revised file's label state
  matches the §2.4 guidance non-adoption rule (labels re-derived in
  file, not imported).
- docs/findings_registry.yaml :316-339 — [FULL] at lines. Rows
  :319-327 and :328-336 reproduce exactly as quoted in the revised
  §0 table (floor numbers, B-SHAPE clause, three named experiments,
  ~250 solves at :322).
- validation/PROGRESS_2026-08-12_S25bis_speed.md :360-401 (STEP 13)
  — [FULL] at lines. 2.2e-2 / 8.2e-2 / 6.0e-2 / 2.9e-2 abs, dH 18%
  vs corrected 4.9e-2 rel (2.06e6 vs asym 1.23e6), K_RICH band
  4.9e6, batched self-asym 7.6e5 vs sequential 1.2e6, BITWISE
  lane-permutation control — all as consumed by the revision.
- validation/a1_ideal_march_jax.py — grep custom_vjp/defvjp
  re-run this window: hits :18, :413, :440, :496, :504, :517 —
  EXACTLY the [ESC-r1-5] corrected anchor set. Repair SOUND.
- literature/nocedal_wright_2006_numerical_optimization_2ed.pdf —
  PDF pp. 215-216 (book 196-197) re-rendered at source: eq. (8.5)
  total error (L/2)e + 2uL_f/e at book p. 196; u "about 1.1e-16"
  p. 196; page-numbering map book 194-197 = PDF 213-216 CONFIRMED
  (PDF 215 renders book p. 196). The unified 194-197 range
  [ESC-r1-7] matches LB-5's "narrower range is the verified one".
- esc_probe_crosslowering_decades.py — RE-RUN this window:
  ALL PASS (separation 4.36 decades; A_FD pair-matched
  [10^6.64, 10^7.21]; max shift 2.83x). Stdlib-only, pinned-env
  safe, rejecting asserts genuinely kill the seven-decade claim
  (assert not 6.5 < sep < 7.5) — a real rejector, not a confirmer.
- Cross-reference sweep [ESC-r1-6]: grep "§6|§8" over the revised
  file — every experiment pointer (E1-E3/P1-P3/F2-CLG-SCALE) now
  resolves to §8/CLG-D7; the two surviving content uses of "§6"
  (line 44 boundary clause — the C44/FD-step boundary IS stated in
  §6 — and the §9 N-W where_read anchor — the read IS consumed in
  §6) are both CORRECT. Repair COMPLETE, including the two
  additional in-window instances claimed (§0 :21, §1 H5 :92).
- Arithmetic re-derived independently: 2.9e-2/2.0e6 = 1.45e-8;
  1.45e-8/2^-53 = 1.31e8; 1.31e8 * 2^-24 = 7.8; sqrt(2^29) =
  2^14.5 = 2.317e4; 1.45e-8 * 2^14.5 = 3.36e-4; log10(7.8/3.36e-4)
  = 4.37; 0.18/1.1e-8 = 1.64e7 = 10^7.21; 0.18/4.1e-8 = 4.39e6 =
  10^6.64; 1.24e7/4.39e6 = 2.83. All match the revised text.

POSITIVE RECORD RATIFIED FIRST: all 8 sustained findings are
genuinely repaired in place with honest markers; no repair silently
narrows the original objection; the disposition table is faithful;
the probe is re-runnable and rejecting; the H7/D4-ALT
exclusive-hypotheses restructuring of CLG-D2 is the RIGHT
architecture (theorem no longer coexists with its own counterexample
channel); label demotions ([ESC-r1-9]) are honest and match the
VERDICT's expected recovery path. The findings below attack residual
defects IN the repairs, not the repaired architecture.

## FINDINGS

### ESC-CROSSLOWERING-r1-1 — REPAIR
**Anchor:** §1 H8 [ESC-r1-2], the printed inequality
"||b_L(W + h e_i) − b_L(W)|| <= the scheme-asymmetry scale of
record (findings :322; STEP 13 :381-399, the K_RICH x max(scheme
asyms) acceptance band)"; inherited by CLG-D5 same-lowering leg
("the H8-bounded variation") and CLG-D6.
**Objection (the applied repair is dimensionally wrong as printed):**
b_L lives on the GRADIENT scale (g_sc = 2.0e6; cross-lowering b
differences 2.9e-2 abs), while the scheme-self-asymmetry numbers of
record are HESSIAN-scale absolutes (asym 1.23e6 / 7.6e5 against dH
2.06e6 = 4.9e-2 rel; the K_RICH band 4.9e6 bounds dH — STEP 13
:381-399, verified at source this window). An FD consumer maps b_L
variation into H as ||delta b_L|| / h, so the coherent form of the
hypothesis carries the step: ||b_L(W + h e_i) − b_L(W)|| <=
h · (scheme-asymmetry scale), equivalently "delta b_L's FD-mapped
contribution stays inside the K_RICH x max(asyms) band". Read
literally, the printed RHS (an H-scale number ~1e6 bounding a
g-scale variation) would permit ||delta b_L|| of order half the
gradient itself — under which the D5 cancellation conclusion that H8
exists to carry does NOT follow: the hypothesis as printed is both
unit-incoherent and too weak for its consequent. The declared CHECK
("repeat the same-lowering scheme self-asymmetry measurement at the
consumer's h", §1 and §7 falsifier) is coherent — it measures the
FD-mapped quantity — which shows the intent is the h-scaled form;
only the printed inequality is wrong.
**Repair (one clause):** insert the h factor or restate
membership-in-band: "||b_L(W+h e_i) − b_L(W)|| <= h · (the
scheme-asymmetry scale of record), i.e. its FD-mapped contribution
to dH stays inside the K_RICH x max(scheme asyms) band". D5's
"H8-bounded variation" clause and D6 inherit without further text.
**Why REPAIR, not BREAK:** the SCHEMA-conditional-on-H8 regrade,
the measured in-band witness, and the named check all survive; only
the hypothesis's printed inequality must be corrected for it to
deliver the cancellation leg it conditions.

### ESC-CROSSLOWERING-r1-2 — AMENDMENT
**Anchor:** §3 CLG-D2 proof sketch step (iv) [ESC-r1-1], "Under H7
that gap is C_s·u·scale, so the induced coefficient perturbations
inject per-stage discrepancies of the same O(u)·kappa·G grade";
hypothesis list §1.
**Objection:** converting the H7 state gap into an O(u)-grade
COEFFICIENT perturbation needs bounded coefficient sensitivity —
||delta A_k|| <= L_R · C_s · u · ||s-hat_k|| requires a Lipschitz
bound on dA_k/ds (i.e. on the second derivatives of R_k), and
likewise for dR_k/dW and phi_k. No hypothesis in §1 declares it: H3
bounds kappa(A_k), not the sensitivity of A_k to its evaluation
point. The step is standard and the bound is exactly the
AG-1-valve kind (strong, trivially checkable from recorded
Jacobian variation along the march), but at THEOREM* grade with a
freshly repaired coefficient channel, the regularity clause the
repair itself leans on must be declared, not implied.
**Repair (one clause):** extend H7 (or step (iv)) with "and the
coefficient maps s -> (A_k, dR_k/dW, phi_k) are uniformly Lipschitz
on the march tube (constant absorbed in c)" — AG-1-declared,
checkable.

### ESC-CROSSLOWERING-r1-3 — AMENDMENT
**Anchor:** §9 first bullet ("Adoptable statements: CLG-D2
(THEOREM*), CLG-D5 (THEOREM*), CLG-D1/D3/D4/D6/D7 (SCHEMA) ...")
vs [ESC-r1-9] four bullets later and the EOF label-state paragraph.
**Objection (bookkeeping contract):** the top §9 bullet still
prints the PRE-repair unconditional labels and carries NO inline
marker; the supersession is declared only downstream ([ESC-r1-9]
"the bullet at the top of §9 is superseded on these points"). A
machine-read consumer or judge harvesting the "Adoptable
statements" line — the exact mis-resolution hazard class this same
file repaired under MIN-CROSSLOWERING-6 — reads stale unconditional
labels (D2 without H7, D5 without the branch split, D6 without the
H8 conditional). Appending a supersession instead of editing in
place is the one spot where the revision's own repair-in-place
discipline was not applied to itself.
**Repair (one edit):** rewrite the §9 top bullet with the
[ESC-r1-9] labels directly (or prefix the bullet itself with
"[SUPERSEDED on labels — see ESC-r1-9]:").

### ESC-CROSSLOWERING-r1-4 — NOTE
**Anchor:** §1 H7 [ESC-r1-1], "H7 is EXACTLY the q = 1 side of the
u-exponent dichotomy of CLG-D7 ... adjudicated by E3".
**Reason (precision, no repair required beyond one word):** H7 is a
SUFFICIENT condition for q = 1 (given D2), not equivalent to it: a
measured q = 1 floor can coexist with H7 false, if the coefficient
channel is subdominant for another reason (small coefficient
sensitivity, cancellation). So E3 adjudicates the MECHANISM
dichotomy (u-linear law vs eps_N-leak dominance) — i.e. D2's
conclusion — while the direct verifier of H7 itself is the
recorded-march state-diff check, which the file correctly names as
a separate cheap adjunct in [ESC-r1-9]. "EXACTLY the q = 1 side"
overstates an implication into an equivalence. A one-word soften
("H7 is the hypothesis behind the q = 1 side") makes the logic
exact; the E3/state-diff division of labor already printed is
correct.

## VERDICT SUMMARY (machine-read)

- BREAK: 0. The escalated revision STANDS architecturally: all 8
  repairs applied, disposition faithful, probe re-runnable and
  rejecting, anchors verified at source (registry, STEP 13, VJP
  grep, N-W p. 196 re-rendered), cross-reference sweep clean.
- REPAIR: 1 (r1-1: H8's printed inequality is unit-incoherent and
  as printed too weak for the D5/D6 cancellation leg it conditions;
  one-clause fix, h-scaled form / band membership — intent already
  witnessed by the file's own declared check).
- AMENDMENT: 2 (r1-2: undeclared coefficient-sensitivity Lipschitz
  clause used by the step-(iv) repair; r1-3: §9 top bullet retains
  pre-repair labels with no inline supersession marker).
- NOTE: 1 (r1-4: "EXACTLY the q = 1 side" is an implication printed
  as an equivalence; E3 verifies D2's conclusion, the state-diff
  check verifies H7).
- Label state impact if r1-1/r1-2 are applied: unchanged from
  [ESC-r1-9] (CLG-D2 THEOREM* under H1-H4+H6+H7(+Lipschitz clause);
  CLG-D5 THEOREM* cross-branch / SCHEMA-conditional-H8 same-branch;
  CLG-D6 SCHEMA conditional on H8). No grade moves; the conditions
  become well-posed.

## PAPERS NEEDED

(empty — all objections stand on repo carriers and the on-disk N-W
pages; Higham 2ed remains relevant only to the author's declared
THEOREM*->THEOREM upgrade path, unchanged.)

## PAPERS CONSULTED (read-depth honesty)

- literature/nocedal_wright_2006_numerical_optimization_2ed.pdf —
  PDF pp. 215-216 (book 196-197), re-rendered this window for the
  (8.5) source re-verify and the page-map confirmation.
- All other reads are repo carriers, listed with line ranges and
  depths in the VERIFICATION RECORD above.
