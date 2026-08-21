# ESCALATED REFUTATION r3 — PHASE D MINOR (d) CROSS-LOWERING
# S-FOUNDATIONS-C4 Blocco 2 escalation window, 2026-08-20. Escalated
# refuter slot per VERDICT_blocco2 §3 E-4, round 3 (single fused
# lens: math structure + carrier/bookkeeping contracts). Target = the
# r3-revised phaseD_minor_crosslowering.md (markers [ESC-r3-0..3])
# + all three disposition tables + esc_probe_crosslowering_decades.py.
# ID prefix: ESC-CROSSLOWERING-r3-<n>. Zero inflation.

## VERIFICATION RECORD (what was checked, at what depth, this window)

- Revised phaseD_minor_crosslowering.md — [FULL] (666 lines), all
  [ESC-r3-*] markers located in text ([ESC-r3-1] §3 :197-206;
  [ESC-r3-2] §3 :251-254 and §9 :492-495; [ESC-r3-3] §1 H8 :140-141)
  and cross-checked one-to-one against the r3 disposition table
  (:645-649). No finding dropped, none weakened.
- esc_refute_crosslowering_r2.md — [FULL]. All 3 r2 findings traced
  to their applied repairs: r2-1 → c-dependence restatement ("kernel
  shape AND the H7 regularity constants (C_s and the coefficient-map
  Lipschitz bounds); its kernel-shape part <= small multiple of
  m-bar via gamma_m") adopted verbatim-class at :195-197, FIXED;
  r2-2 → both one-phrase edits adopted as prescribed (§3 "for which
  H7 is the sufficient hypothesis" :251-252; §9 "(sufficient
  hypothesis: H7)" :492), FIXED; r2-3 → contingent "hence a
  fortiori" edit adopted at :141 with adoption justified (the note's
  "if ever edited" condition fired: the file WAS edited this round),
  FIXED.
- esc_refute_crosslowering_r1.md — [FULL]; all 4 r1 repairs
  spot-re-verified still in place (h-scaled H8 :137-142; H7
  Lipschitz clause :112-118; §9 rewritten-in-place labels :489-506;
  §1 sufficiency phrasing :120-127). No regression.
- refute_minor_crosslowering.md + VERDICT_blocco2.md §2.4 (:199-234)
  + §3 E-4 (:256-268) — [FULL]. Original 8 repairs still standing;
  escalation form honored.
- Residual-class sweep, WIDER pattern than the author's (grep
  "q = 1 = H7|i.e. on H7|EXACTLY the q|depending only|seven decades"
  over the r3 file): every hit is inside a repair marker's "was ..."
  quotation (:121, :198, :251, :467, :492), the exempt [ESC-r1-9]
  consumed derivation record (:522), or the append-only disposition
  tables (:574, :610, :647-648). Live-text: CLEAN. The author's
  claimed post-repair state is confirmed by an independent, broader
  sweep.
- docs/findings_registry.yaml :316-339 — [FULL] at lines. §0 table
  quotes verbatim-faithful (2.9e-2 abs / g_sc 2.0e6; ~250 solves
  :322; B-SHAPE + three experiments :335; dH 18% / 4.9e-2 rel /
  K_RICH x max(asyms) = 4.9e6 :322; H2-anchor context :324 vs :333).
- validation/PROGRESS_2026-08-12_S25bis_speed.md STEP 13 (:362-399)
  — [FULL] at lines. 2.2e-2/8.2e-2/6.0e-2/2.9e-2 abs; dH 2.06e6 vs
  asym 1.23e6 = 4.9e-2 rel; K_RICH = 4.9e6/1.23e6 ≈ 3.98 ≈ 4 (the
  [ESC-r3-3] marker's "K_RICH ≈ 4" re-derived, correct); BITWISE
  lane-permutation — all as consumed.
- validation/a1_ideal_march_jax.py — grep custom_vjp/defvjp re-run
  this window: hits :18, :413, :440, :496, :504, :517 — matches the
  [ESC-r1-5] anchor set exactly. No drift.
- esc_probe_crosslowering_decades.py — read [FULL] (rejecting
  asserts confirmed present: seven-decade claim killed by
  `assert not (6.5 < sep < 7.5)`) and RE-RUN this window: ALL PASS
  (separation 4.36 decades; A_FD pair-matched [10^6.64, 10^7.21];
  max shift 2.83x). Output IDENTICAL to the r1 and r2 recorded
  values — consistent with the header's "unchanged by r2/r3" claim.
- Arithmetic spot re-derivations this window: 2.9e-2/2.0e6 =
  1.45e-8; 1.45e-8/2^-53 = 1.31e8; 1.3e8/250 = 5.2e5; 1.3e8/15.8 =
  8.2e6; 4.9e6/1.23e6 = 3.98. All match the revised text.
- Logical check of [ESC-r3-3]: ||delta b_L||/h <= max(asyms) <=
  K_RICH·max(asyms) — the a-fortiori direction is correct (the
  stronger hypothesis delivers band membership); the repair is
  sound.
- Logical check of [ESC-r3-2]: the §3 relative clause "which is
  exactly what E3 ... adjudicates" now attaches to "q = 1" (the
  mechanism dichotomy), not to H7 — consistent with the r1-4/r2-4
  division of labor (E3 adjudicates q; the recorded-march state-diff
  check verifies H7). Sound.

POSITIVE RECORD RATIFIED FIRST: all 3 r2 findings are repaired at
their anchors with honest markers (r2-1/r2-2 verbatim-class, r2-3
via its own contingent phrasing with the firing condition correctly
invoked); the r3 disposition table is faithful; no prior-round
repair regressed; the live §1/§3/§9 texts now state ONE logical
relation between H7 and q = 1 (sufficiency); the c-dependence
statement is now coherent with what steps (i)-(iv) absorb from H7;
the probe re-runs PASS with rejecting asserts; label state unchanged
as the r2 refuter predicted. The findings below attack residual
defects the three completed rounds have not reached — both are
instances of repair-propagation stopping at the attacked anchor
while a sibling statement carries the same defect class.

## FINDINGS

### ESC-CROSSLOWERING-r3-1 — AMENDMENT
**Anchor:** §4 CLG-D3 statement (:291-296): "**Statement (SCHEMA,
conditional on H5).** Under H1-H6 with H5, the expected floor scales
as E ||g-hat_L − g-hat_L'|| / g_sc ~ c · u · kappa_eff · G_rms ·
sqrt(N)"; cross-ref §3 CLG-D2 (repaired form: "Under H1-H4, H6, and
H7"; u-linear form conditional on q = 1, H7 sufficient).
**Objection (the r1-1 repair's conditioning was never propagated to
the sibling statement):** CLG-D3 is the RMS refinement OF CLG-D2's
law — same per-stage injections, same adjoint coefficients evaluated
at the forward states. The MIN-CROSSLOWERING-1 channel applies to it
verbatim: without H7 (or an explicit conditional-on-q = 1 scoping),
the EXPECTED floor also carries the additive eps_N-class coefficient
term (D4-ALT), and the printed u-LINEAR expected law
"~ c·u·kappa_eff·G_rms·sqrt(N)" under "H1-H6 with H5" is exactly the
pre-r1 defect class: a u-linear statement whose hypothesis list does
not exclude the named, plausibly dominant eps_N channel. The r1
repair conditioned D2; the file's own sweep discipline — invoked
twice, [ESC-r1-6] ("a slip class gets swept file-wide") and
[ESC-r3-2] (same precedent) — was applied at PHRASE level (grep
"q = 1 = H7" etc.) but not at CONCEPT level: D3 is a live instance
of the un-conditioned u-linear law that no phrase-level grep can
catch. Note the §8 E1/P1 text is consistent with the repair
("slope p = 1/2 under H5 (D3)") and needs no change; only D3's
hypothesis list does.
**Repair (one token-level edit):** §4 statement: "Under the CLG-D2
hypotheses (H1-H4, H6, H7) with H5, the expected floor scales as
..." — or equivalently keep "H1-H6 with H5" and append "and H7; the
u-linear form inherits D2's conditionality on q = 1 (H7 sufficient,
E3-adjudicated)". D3's SCHEMA grade and its falsifier are unchanged.
**Why AMENDMENT, not BREAK:** D3 is SCHEMA-grade, explicitly
heuristic ("~", conditional on H5), and its adjudication route (E1
N-ladder) is unaffected; the defect is an incoherent hypothesis
list between sibling statements, repaired by one clause — the same
species the loop has graded AMENDMENT since r1-2.

### ESC-CROSSLOWERING-r3-2 — AMENDMENT
**Anchor:** §3 CLG-D2, proof sketch step (iii) (:229-231): "the
(dR_k/dW)^T accumulation contributes one more bounded factor
absorbed in c"; step (i) (:219-221): "differ by <= c1 · u ·
kappa(A_k) · ||input||"; vs the [ESC-r3-1]-repaired statement
(:195-197): "a constant c depending on the per-stage kernel shape
AND the H7 regularity constants (C_s and the coefficient-map
Lipschitz bounds)".
**Objection (residual in the freshly repaired sentence — the
enumeration of what c absorbs is still incomplete, and the
boundedness it leans on is undeclared):** the proof asserts
boundedness of march-scale magnitudes that NO hypothesis delivers:
(a) step (iii)'s "bounded factor" is a uniform magnitude bound
sup_k ||dR_k/dW|| over the admissible design set — H3 bounds
kappa(A_k) (invertibility), H4 bounds transport products, and H7's
Lipschitz clause bounds the s-VARIATION of the coefficient maps, not
their magnitude; uniform Lipschitz on the march tube implies
boundedness only if the tube is bounded, which is also nowhere
declared; (b) since the bound is stated RELATIVE to g_sc, c also
absorbs operand-scale ratios (stage operand scale / g_sc, including
phi_k magnitudes feeding ||input|| in step (i)) — likewise
march-equation properties on the tube, not kernel-shape and not
among "C_s and the coefficient-map Lipschitz bounds". The r3-1
repair removed the false "only" and the global m-bar claim, so the
sentence is no longer false as printed (unlike the r2-1 target); but
the dependence it now enumerates presents itself as the
characterization of c, and the hypothesis list still contains no
clause for the magnitude bounds the finiteness of c requires —
exactly the r1-2 species ("the regularity clause the proof leans on
must be declared, not implied"), one rung smaller.
**Repair (one clause, AG-1 valve):** extend H7's coefficient clause
to "uniformly Lipschitz AND uniformly bounded on the march tube
(magnitude bounds sup_k ||dR_k/dW||, sup_k ||phi_k|| absorbed in
c)" — strong, trivially checkable from the same recorded Jacobians
the existing H7 check reads — and (optionally, half a clause) let
the statement's parenthetical read "(C_s, the coefficient-map
Lipschitz bounds, and the coefficient magnitude bounds)". No label
move: "Why THEOREM*" already disclaims Higham-grade constant
tracking, and the new clause is declaration, not derivation.
**Why AMENDMENT, not BREAK:** on any recorded finite march the
bounds are trivially finite and checkable; the bound's form, the H7
architecture, and all grades survive; only the declaration is owed.

### ESC-CROSSLOWERING-r3-3 — NOTE
**Anchor:** §4 CLG-D3 (:294-296): "c · u · kappa_eff · G_rms ·
sqrt(N), with kappa_eff, G_rms the quadratic means of the per-stage
factors".
**Reason (precision remark, no repair required at SCHEMA grade):**
the RMS accumulation under H5 gives E-floor ~ u · sqrt(sum_k
(kappa_k · G_k · c_k)^2) = u · sqrt(N) · rms_k(kappa_k G_k c_k) —
the quadratic mean of the per-stage PRODUCT. The printed factorized
form kappa_eff · G_rms (product of separate quadratic means) equals
it only under cross-stage decorrelation of conditioning and
transport factors; in general rms(kappa·G) can exceed
rms(kappa)·rms(G) (squares positively correlated — plausible here,
since marginal cells raise kappa AND sit where transport is
strongest, the E2 mechanism). D3 is SCHEMA, "~"-scaling, H5 already
declared PRACTICE, and the §4 consistency arithmetic (8.2e6) is a
product-level number unaffected by the split — so this is precision
only. If ever edited (e.g. under r3-1's repair), define the pair
jointly: "with kappa_eff · G_rms := rms_k(kappa_k G_k), the
quadratic mean of the per-stage product" — one phrase.

## VERDICT SUMMARY (machine-read)

- BREAK: 0. The r3 revision STANDS: all 3 r2 findings repaired at
  anchor as specified (contingent r2-3 edit correctly fired), no
  prior-round regression, dispositions faithful, probe re-runnable
  and rejecting (ALL PASS this window, output identical to r1/r2
  records), carriers verified at source (registry :316-339, STEP 13
  :362-399, VJP grep), live-text residual-class sweep clean under a
  broader pattern than the author's.
- REPAIR: 0.
- AMENDMENT: 2 (r3-1: CLG-D3's hypothesis list never received the
  r1 H7/q = 1 conditioning — the sibling statement still prints the
  un-conditioned u-linear expected law, a concept-level instance the
  phrase-level sweeps could not catch; r3-2: the magnitude bounds
  (sup_k ||dR_k/dW||, ||phi_k||, operand-scale ratios) that step
  (iii)'s "bounded factor" and the finiteness of c lean on are
  declared by no hypothesis and absent from the freshly restated
  c-dependence enumeration; both = one-clause AG-1 declarations).
- NOTE: 1 (r3-3: D3's kappa_eff · G_rms factorization presents the
  quadratic mean of a product as a product of quadratic means —
  decorrelation silently assumed, plausibly violated in the E2
  direction; SCHEMA grade makes it precision-only).
- Label state impact if r3-1/r3-2 are applied: NONE — CLG-D2
  THEOREM* under H1-H4+H6+H7 (H7 gaining the magnitude clause;
  u-linear conditional on q = 1, H7 sufficient, E3-adjudicated);
  CLG-D3 SCHEMA now explicitly conditioned on the D2 hypotheses +
  H5; CLG-D5 THEOREM* cross-branch / SCHEMA-conditional-H8
  same-branch; CLG-D6 SCHEMA conditional on H8; CLG-D1/D4/D7
  SCHEMA; CLG-D4-ALT CONJECTURE. No grade moves; the hypothesis
  lists become coherent across sibling statements.

## PAPERS NEEDED

(empty — both amendments and the note stand on the file's own text
and repo carriers verified at source; Higham 2ed remains relevant
only to the author's declared THEOREM*->THEOREM upgrade path,
unchanged.)

## PAPERS CONSULTED (read-depth honesty)

- No literature consulted this round: the r3 delta is textual/
  logical with no new citations; the N-W 194-197 read was
  source-verified by the r1 refuter (spot-verify PASS, LB-5) and
  re-ratified by r2; not re-litigated. All reads this window are
  repo carriers, listed with line ranges and depths in the
  VERIFICATION RECORD above.
