# ESCALATED REFUTATION r2 — PHASE D MINOR (d) CROSS-LOWERING
# S-FOUNDATIONS-C4 Blocco 2 escalation window, 2026-08-20. Escalated
# refuter slot per VERDICT_blocco2 §3 E-4, round 2 (single fused
# lens: math structure + carrier/bookkeeping contracts). Target = the
# r2-revised phaseD_minor_crosslowering.md (markers [ESC-r2-0..4])
# + both disposition tables + esc_probe_crosslowering_decades.py.
# ID prefix: ESC-CROSSLOWERING-r2-<n>. Zero inflation.

## VERIFICATION RECORD (what was checked, at what depth, this window)

- Revised phaseD_minor_crosslowering.md — [FULL] (597 lines), all
  [ESC-r2-*] markers located in text (:108-114, :118-127, :135-144,
  :463-479, :489-493) and cross-checked one-to-one against the r2
  disposition table (:578-584). No finding dropped, none weakened.
- esc_refute_crosslowering_r1.md — [FULL]. All 4 r1 findings traced
  to their applied repairs: r1-1 → h-scaled H8 (:132-135) FIXED;
  r1-2 → Lipschitz clause in H7 (:106-108) + step-(iv) wiring
  (:218-219) FIXED (residual defect below, r2-1); r1-3 → §9 top
  bullet rewritten in place (:463-471) FIXED (residual defect below,
  r2-2); r1-4 → "hypothesis behind the q = 1 side" (:116-117) FIXED
  at its anchor (same-class instances elsewhere, r2-2).
- refute_minor_crosslowering.md — [FULL]; original 8 repairs
  spot-re-verified: no live "seven decades" (grep: only repair-record
  mentions), N-W range unified 194-197 everywhere, H2 anchor =
  a1_ideal_march_jax.py (grep custom_vjp/defvjp re-run this window:
  hits :18, :413, :440, :496, :504, :517 — matches [ESC-r1-5]
  exactly), experiment pointers resolve to §8.
- VERDICT_blocco2.md §2.4 (:199-234) + §3 E-4 (:256-258) — [FULL] at
  lines. Escalation form honored (author-revision + refutation
  rounds until-dry); guidance labels correctly re-derived, not
  imported.
- docs/findings_registry.yaml :316-339 — [FULL] at lines. §0 table
  quotes verbatim-faithful (floor 2.9e-2 abs / g_sc 2.0e6 = 1.45e-8
  rel; values 1e-15; ~250 solves :322; B-SHAPE + three experiments
  :335; dH 18% / 4.9e-2 / K_RICH x max(asyms) = 4.9e6 :322).
- validation/PROGRESS_2026-08-12_S25bis_speed.md STEP 13 (:362-399)
  — [FULL] at lines. 2.2e-2/8.2e-2/6.0e-2/2.9e-2 abs; dH 2.06e6 vs
  asym 1.23e6 = 4.9e-2 rel; batched self-asym 7.6e5 vs sequential
  1.2e6; BITWISE lane-permutation — all as consumed.
- esc_probe_crosslowering_decades.py — RE-RUN this window: ALL PASS
  (separation 4.36 decades; A_FD pair-matched [10^6.64, 10^7.21];
  max shift 2.83x). Output IDENTICAL to the r1 refuter's recorded
  values — consistent with the header's "unchanged by r2" claim
  (file is untracked, so no git history check is possible; content
  consistency is the available evidence).
- Dimensional check of the r2-1 repair (H8, h-scaled form): b_L is
  gradient-scale, h is W-scale, scheme asymmetry is Hessian-scale
  (= gradient/W); h · asym is gradient-scale — the corrected
  inequality is unit-coherent, and ||delta b_L||/h <= asym <=
  K_RICH · max(asyms) (K_RICH = 4.9e6/1.23e6 ≈ 4 >= 1) delivers the
  band membership and the D5 cancellation leg (delta b_L/h ≈ 1.2e6
  abs ≈ 2.9e-2 rel on the H-scale of record — inside the measured
  in-band regime). The r1-1 objection is genuinely discharged.

POSITIVE RECORD RATIFIED FIRST: all 4 r1 findings are repaired at
their anchors with honest markers; the r2 disposition table is
faithful; the h-scaled H8 is now unit-coherent and strong enough for
the D5/D6 cancellation leg; the H7 Lipschitz clause closes the
coefficient-sensitivity gap in step (iv); the §9 adoptable bullet
now carries post-r1 conditional labels in place with [ESC-r1-9]
honestly kept as consumed derivation record; label state unchanged
as the r1 refuter predicted. The findings below attack residual
defects IN the r2 repairs, not the architecture.

## FINDINGS

### ESC-CROSSLOWERING-r2-1 — REPAIR
**Anchor:** §3 CLG-D2 statement (:184-188): "there is a constant c
depending only on the per-stage kernel shape (c <= a small multiple
of m-bar via the standard gamma_m ... reassociation bound)"; vs §1
H7 [ESC-r2-2] "(constant absorbed in c)" (:108) and step (iv)
"absorbed into c to first order in u" (:221-222).
**Objection (the r2-2 repair contradicts the theorem statement's
characterization of c):** the statement still declares c a function
of the per-stage KERNEL SHAPE ONLY, bounded by a small multiple of
m-bar via gamma_m. But step (iv) — since r1, and now explicitly via
the [ESC-r2-2] clause — absorbs into c the H7 state-agreement
constant C_s AND the coefficient-map Lipschitz constants (bounds on
dA_k/ds i.e. second derivatives of R_k, and on the s-sensitivity of
dR_k/dW, phi_k). These are properties of the MARCH EQUATIONS on the
march tube (physics/design regularity), not of the compiled kernel's
flop count; nothing in the gamma_m mechanism prices them, so both
the "depending only on the per-stage kernel shape" clause and the
"c <= a small multiple of m-bar" parenthetical are false as printed
for the c the proof actually constructs. The defect originates in
the r1 refuter's own prescribed phrase "(constant absorbed in c)"
(RES-CAP-1 class: refuter-prescribed text breaking under later
attack) adopted verbatim without reconciling the statement.
**Repair (one clause):** restate the constant's dependence: "a
constant c depending on the per-stage kernel shape AND the H7
regularity constants (C_s and the coefficient-map Lipschitz bounds);
its kernel-shape part is <= a small multiple of m-bar via the
standard gamma_m bound". "Why THEOREM*" already disclaims
Higham-grade constant tracking, so no label move follows.
**Why REPAIR, not BREAK:** the bound's form, the H7 conditioning,
and the exclusive-hypotheses architecture all survive; only the
printed characterization of c must match what the proof absorbs into
it — same defect class as r1-1 (printed clause incoherent with the
repair's own bookkeeping, intent clearly correct).

### ESC-CROSSLOWERING-r2-2 — AMENDMENT
**Anchor:** §9 top bullet [ESC-r2-3] (:468): "u-linear form
conditional on q = 1 = H7, E3-adjudicated"; and §3 step-(iv) closing
(:231-233): "the u-LINEAR form of the law is CONDITIONAL on q = 1 —
i.e. on H7 holding — which is exactly what E3 ... adjudicates".
**Objection (a repair re-imported the defect a sibling repair
removed):** the r2-4 repair made §1 H7 exact — H7 is SUFFICIENT for
q = 1, not equivalent; E3 adjudicates D2's mechanism conclusion
while the recorded-march state-diff check verifies H7 itself. But
the r2-3 rewrite of the adoptable-statements bullet — the file's
machine-harvest line, the exact hazard class this item has now
repaired twice (MIN-CROSSLOWERING-6, ESC-r1-3) — freshly prints
"q = 1 = H7" (an equality sign between the empirical exponent and
the hypothesis) plus "E3-adjudicated" attached to that equation; and
§3's "on q = 1 — i.e. on H7 holding" is a pre-existing instance of
the same equivalence class left un-swept (the r1-4 fix was applied
at its §1 anchor only — the file's own [ESC-r1-6] precedent is that
a slip class gets swept file-wide, not anchor-only). Result: the
live §1 text and the live §9/§3 texts now state different logical
relations between H7 and q = 1. ([ESC-r1-9]'s "q = 1 = H7" (:495) is
exempt: annotated as consumed derivation record.)
**Repair (two one-phrase edits):** §9: "u-linear form conditional on
q = 1 (sufficient hypothesis: H7), E3-adjudicated"; §3: "CONDITIONAL
on q = 1 — for which H7 is the sufficient hypothesis — which is
exactly what E3 adjudicates". No label change.

### ESC-CROSSLOWERING-r2-3 — NOTE
**Anchor:** §1 H8 [ESC-r2-1] (:132-135): "||b_L(W + h e_i) −
b_L(W)|| <= h · (the scheme-asymmetry scale of record), i.e. its
FD-mapped contribution ||delta b_L|| / h to dH stays inside the
K_RICH x max(scheme asyms) acceptance band".
**Reason (precision remark, no repair required):** the "i.e." joins
the h-scaled inequality to a strictly WEAKER consequence — the
inequality gives ||delta b_L||/h <= max(asyms), the band admits up
to K_RICH · max(asyms) (K_RICH ≈ 4 on the record numbers) — so the
two readings differ by the K_RICH factor and are an implication, not
a restatement. The direction is SAFE (the printed hypothesis
delivers the band membership a fortiori), the declared check is
unaffected, and the phrasing is the r1 refuter's own prescribed
text adopted verbatim; recorded so a later consumer does not flag
the K_RICH slack as an inconsistency. If ever edited, "i.e." →
"hence a fortiori".

## VERDICT SUMMARY (machine-read)

- BREAK: 0. The r2 revision STANDS architecturally: all 4 r1
  findings repaired at anchor, dispositions faithful, probe
  re-runnable (ALL PASS this window, output identical to r1 record),
  carriers verified at source (registry :316-339, STEP 13 :362-399,
  VJP grep), H8 now unit-coherent and sufficient for its consequent.
- REPAIR: 1 (r2-1: CLG-D2's "constant c depending only on the
  per-stage kernel shape (c <= small multiple of m-bar)" is false as
  printed once step (iv)/H7 absorb C_s and the coefficient-map
  Lipschitz constants into c; one-clause dependence restatement;
  refuter-prescribed-text origin, RES-CAP-1 class).
- AMENDMENT: 1 (r2-2: "q = 1 = H7" freshly printed by the r2-3
  rewrite in the adoptable-statements line + the un-swept §3 "i.e.
  on H7 holding" contradict the r2-4-repaired §1 sufficiency form;
  two one-phrase edits).
- NOTE: 1 (r2-3: H8's "i.e." presents an a-fortiori implication as a
  restatement — K_RICH-factor slack, safe direction, no repair
  required).
- Label state impact if r2-1/r2-2 are applied: NONE — CLG-D2
  THEOREM* under H1-H4+H6+H7 (u-linear conditional on q = 1, H7
  sufficient, E3-adjudicated); CLG-D5 THEOREM* cross-branch /
  SCHEMA-conditional-H8 same-branch; CLG-D6 SCHEMA conditional on
  H8; CLG-D1/D3/D4/D7 SCHEMA; CLG-D4-ALT CONJECTURE. The statements
  become self-consistent; no grade moves.

## PAPERS NEEDED

(empty — all objections stand on repo carriers already verified at
source; Higham 2ed remains relevant only to the author's declared
THEOREM*->THEOREM upgrade path, unchanged.)

## PAPERS CONSULTED (read-depth honesty)

- No literature consulted this round: the r2 delta is textual/
  logical with no new citations; the N-W 194-197 read was
  source-verified by the r1 refuter (spot-verify PASS, LB-5) and is
  not re-litigated. All reads this window are repo carriers, listed
  with line ranges and depths in the VERIFICATION RECORD above.
