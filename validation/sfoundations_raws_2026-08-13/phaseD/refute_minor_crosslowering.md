# REFUTATION — PHASE D MINOR (d) CROSS-LOWERING derivable part
# S-FOUNDATIONS-C4 Blocco 1, 2026-08-20. Refuter slot per
# BRIEF_blocco2_phaseD.md MINORS (d): ONE round, complete, zero
# inflation. Target = phaseD_minor_crosslowering.md (DRAFT).
# ID prefix: MIN-CROSSLOWERING-<n>. Adjudication = Blocco-2 judge.

## VERIFICATION RECORD (what was checked, at what depth)

- Author file phaseD_minor_crosslowering.md — [FULL].
- BRIEF_blocco2_phaseD.md MINORS (d) + SHARED FRAME — [FULL].
- docs/findings_registry.yaml :310-350 (rows
  engine:vmap-hessian-adjoint-divergence :319-327 and
  engine:cross-lowering-gradient-floor :328-336) — [FULL] at lines.
  All row quotes in the author's §0 table VERIFIED verbatim-faithful
  (floor ~1e-8 rel; 2.9e-2 abs on g-scale 2.0e6; vmap B=1 2.2e-2;
  B-dependent 6.0e-2; values 1e-15; ~250 implicit 4x4 solves at
  :322; dH 18% gate-rejected; corrected 4.9e-2 rel inside K_RICH x
  max(asyms) = 4.9e6; lane-permutation BITWISE; B-SHAPE clause
  B-F10 at :335; three named experiments at :335).
- validation/PROGRESS_2026-08-12_S25bis_speed.md STEP 13 :362-399 —
  [FULL] at lines. Matches the author's use.
- blocco3/VERDICT_wave2.md :40-64, :198-223 — [FULL] at lines.
  RC31T-2 same-lowering pin + cross-lowering-pairs-REJECTED-at-
  update-time text confirmed (:207-220).
- blocco3/VERDICT_wave3.md :600-620 — [FULL] at lines. F2-C44-FDSTEP
  ownership of FD step + N-W §8.1 fold confirmed (:612-615).
- literature/nocedal_wright_2006_numerical_optimization_2ed.pdf —
  [FULL] book pp. 194-197 (PDF 213-216), rendered pages. Eq. (8.5)
  total-error form (L/2)e + 2uL_f/e at book p. 196; u "about
  1.1e-16" at p. 196. The author's (8.5)-class adaptation
  (truncation (L_H/2)h + noise 2*eta/h with eta = absolute gradient
  noise) is a faithful class transplant and the transplant IS
  declared (R-4). Spot-verify PASS.
- validation/a1_toc_variational_jax.py :1690-1724 — [FULL] at lines
  (anchor check, see finding 5); grep for custom_vjp/defvjp in
  validation/a1_ideal_march_jax.py (hits :18, :413, :440, :496,
  :504, :517).

Arithmetic re-derived independently: 2.9e-2/2.0e6 = 1.45e-8;
1.45e-8/1.11e-16 = 1.31e8; 1.3e8/250 = 5.2e5; sqrt(250) = 15.8;
1.3e8/15.8 = 8.2e6; sqrt(1.11e-16) = 1.05e-8 (sqrt(u)-class claim
for 1.45e-8: PASS); 2^-24 = 5.96e-8; 2^29 = 5.4e8; 1.3e8 * 5.96e-8
= 7.7; 2^14.5 = 2.3e4; 1.45e-8 * 2.3e4 = 3.3e-4; 0.18/1.45e-8 =
1.24e7 = 10^7.09. All PASS except the "seven decades" claim
(finding 3).

## FINDINGS

### MIN-CROSSLOWERING-1 — CONTENT-OBJECTION
**Anchor:** CLG-D2 (§3), statement + proof sketch steps (i)-(ii);
hypothesis list §1 (H1-H4, H6); cross-refs CLG-D4 (§5), CLG-D4-ALT,
CLG-D7 (§8).
**Objection:** The THEOREM* bound ||g-hat_L − g-hat_L'||/g_sc <=
c·u·kappa-bar·G·N (first order in u, "for any two lowerings") is
not delivered by the stated hypotheses, because the proof sketch
counts ONLY discrepancies injected inside the adjoint sweep. Step
(ii)'s closure claim — "Inputs to stage k themselves differ across
lowerings, but that difference is exactly the accumulated
discrepancy from stages > k, already counted" — is true of the
lambda_k inputs only. The adjoint coefficients A_k = dR_k/ds_k,
dR_k/dW and phi_k are evaluated at the FORWARD states s-hat_k,
which per the file's own CLG-D4 agree across lowerings only to "a
floating-point neighborhood" of the common fixed point — a
neighborhood whose size is the Newton tolerance floor eps_N, which
per the file's own CLG-D4-ALT is plausibly sqrt(u)-class, NOT O(u).
A first-order coefficient perturbation delta A_k ~ O(eps_N) injects
a gradient discrepancy ~ kappa·G per stage that is NOT first order
in u whenever eps_N >> u. The file itself declares the u-exponent q
in {1, 1/2} UNIDENTIFIED on the current record (CLG-D7, §8) — i.e.
the record cannot exclude that the measured 1.45e-8 floor is
dominated by the very channel the stated bound omits. A bound
graded THEOREM* whose stated hypotheses do not exclude a named,
plausibly dominant violation channel is a derivation gap, not a
constant-tracking gap (the declared THEOREM*-not-THEOREM caveat
covers Higham-grade constants and H3/H4 uniformity — not this).
**Repair path (cheap, AG-1 valve):** add an explicit hypothesis H7
(cross-lowering converged-state agreement ||s-hat_L,k −
s-hat_L',k|| = O(u)·scale, strong sufficient-not-optimized,
checkable on recorded marches), OR restate the bound with the extra
term + C'·kappa-bar·G·N·eps_N-class and mark D2's u-linear form
explicitly CONDITIONAL on q = 1 pending E3. Either way the
D2/D4-ALT relation becomes exclusive-hypotheses instead of a
theorem coexisting with its own counterexample channel.
**Why CONTENT:** changes the scope and the hypothesis list of the
minor's central deliverable (the chain amplification law).

### MIN-CROSSLOWERING-2 — CONTENT-OBJECTION
**Anchor:** CLG-D5 (§6) same-lowering bullet ("the systematic
component b_L is common-mode and cancels to first order in the
difference"); CLG-D6 (§7) which promotes this to "derived ... the
unique zero-cost mitigation"; CLG-D1 (§2) decomposition.
**Objection:** First-order cancellation of b_L in an FD difference
g-hat_L(W+he_i) − g-hat_L(W) presumes b_L(·) varies smoothly (or
negligibly) over the step h. That is an UNSTATED hypothesis: b_L is
a rounding-bias function, deterministic (bitwise witness) but in
general only piecewise-continuous in W — per-op rounding
coefficients flip discontinuously as intermediates cross rounding
boundaries, so b_L(W+he) − b_L(W) is not generically O(h·db/dW);
worst case it is O(||b_L||) itself. The bitwise lane-permutation
witness of record covers determinism at FIXED inputs, not stability
of b_L across NEIGHBORING inputs — it cannot carry the cancellation
step alone. The measured fact that same-lowering FD meets its
K_RICH bound is evidence that the structural (slowly-varying) part
of b_L dominates, but D5 is graded THEOREM* and D6 claims the
mitigation is "derived", so the load-bearing smoothness/structural-
stability assumption must be declared as a hypothesis (AG-1: strong,
declared, checkable — e.g. b_L variation over the FD step bounded by
the measured same-lowering scheme self-asymmetry, carrier :322/STEP
13), or the cancellation leg demoted to measured-witness-supported
SCHEMA.
**Why CONTENT:** the cancellation step is what separates the
same-lowering from the cross-lowering branch of D5 and is the
entire derivational content of D6; its unstated hypothesis changes
what D5/D6 actually prove.

### MIN-CROSSLOWERING-3 — CONTENT-OBJECTION
**Anchor:** CLG-D7 (§8), experiment (E3), last clause: "seven
decades of separation between the two predictions: an unambiguous
discriminator".
**Objection:** the derived number is wrong. The two predictions are
phi32 ≈ O(1-10) (q = 1; 1.3e8·5.96e-8 = 7.7, file's own arithmetic)
vs phi32 ≈ 3e-4 (sqrt-class; 1.45e-8·2^14.5 = 3.3e-4, file's own
arithmetic). Separation = log10(7.7/3.3e-4) ≈ 4.4 decades
(equivalently, ratio-of-ratios 2^29/2^14.5 = 2^14.5 ≈ 2.3e4). No
reading of the file's own numbers yields seven decades (O(10) vs
3e-4 gives at most ~4.5). Likely contamination from the separate
"~7 orders FD amplification" figure. The qualitative conclusion
(E3 is a clean discriminator) SURVIVES at ~4.4 decades — stated
here explicitly to avoid inflation — but a wrong derived number in
a record-bound deliverable is an R5 defect, and the corrected
separation belongs in the landing text (prediction P3).
**Repair:** replace "seven decades" with "~4.4 decades (2^14.5 ≈
2.3e4x)".

### MIN-CROSSLOWERING-4 — WORDING
**Anchor:** CLG-D2 (§3), consistency paragraph: "Near-sonic /
marginal-cell 4x4 conditioning of order 1e3-1e5 times transport of
order 1e1-1e3 covers this range without strain".
**Reason:** the kappa and G ranges carry NO carrier and no declared
class — they are plausibility estimates, in a file whose §0
declares "no new measured numbers are produced by this minor". R5
hygiene requires labeling them as unanchored order-of-magnitude
estimates (PRACTICE class) pending the F2 measurements (E2 + the
lambda-growth check of H4), and softening "covers this range
without strain" to "is compatible". The consistency conclusion
itself is correctly framed as necessary-condition arithmetic and is
not contested.

### MIN-CROSSLOWERING-5 — WORDING
**Anchor:** §1, H2: "Checkable by inspection of the VJP code
(validation/a1_toc_variational_jax.py:1697-1720 and the
a1_ideal_march_jax defvjp)".
**Reason:** mis-anchored. Lines 1697-1720 of a1_toc_variational_jax
are the Jacobi-preconditioner FD stencil block of the DRIVER (an FD
CONSUMER of the gradient — the M6 batched dispatch), verified
in-window; they contain no VJP kernel and cannot support the H2
flop-count/kernel-shape inspection. The registry row's code field
cites the same range for the row's FD-consumer context — the
transplant of that anchor to "the VJP code" is wrong. The actual
per-stage adjoint kernel lives in validation/a1_ideal_march_jax.py
(implicit-solve machinery ~:413-517; @jax.custom_vjp :504;
solve.defvjp(fwd, bwd) :517 — grep verified in-window). Correct the
anchor; H2's content is otherwise fine.

### MIN-CROSSLOWERING-6 — WORDING
**Anchor:** internal cross-references to "§6" for the three
scaling experiments: §0 ("named in §6"), CLG-D2 §3 ("two of the F2
identification targets (§6)"), CLG-D3 §4 ("see §6, prediction P1"),
CLG-D4-ALT §5 ("The float32 contrast (§6, prediction P3)").
**Reason:** the experiments (E1-E3, predictions P1-P3, F2-CLG-SCALE)
are defined in §8 (CLG-D7), not §6 (§6 = CLG-D5, the FD law) — a
systematic renumbering slip. Machine-read consumers and the judge's
landing text would mis-resolve these anchors. Note the §9 landing
anchor "where_read anchor = this file §6" for the N-W read IS
correct (the read is consumed in §6/CLG-D5) — only the
experiment-pointing instances are wrong.

### MIN-CROSSLOWERING-7 — NOTE
**Anchor:** §6 (CLG-D5) declares N-W read "[FULL] at pp. 194-197
(PDF 213-216)"; PAPERS CONSULTED declares "pp. 194-199 (PDF
213-218)".
**Reason:** internal inconsistency in the declared-pages record
(two ranges for the same read). The citation content is verified
correct at pp. 194-197 either way (spot-verify PASS, see
VERIFICATION RECORD); declare ONE range. If pp. 198-199 were
actually read (central-difference/(8.7)-class material continues
past p. 197), keep the wider range everywhere including §9.

### MIN-CROSSLOWERING-8 — NOTE
**Anchor:** CLG-D5 (§6), consistency paragraph: A_FD(implied) =
0.18 / 1.45e-8.
**Reason:** pair-choice mismatch, declared here for the record: phi
= 1.45e-8 is the sequential eager-vs-jit floor, while the M6
18%-incident pair was batched-rows-vs-separate-sequential-base
(measured divergences 2.2e-2 to 8.2e-2 abs = 1.1e-8 to 4.1e-8 rel,
STEP 13 :366-368). Using the pair-matched phi moves A_FD(implied)
by at most ~2.8x (10^6.6-10^7.2); the "~7 orders" reading is robust
to the choice. Worth one clause declaring which pair the implied
A_FD uses.

## SUMMARY FOR THE JUDGE

Verification: every registry/verdict/PROGRESS anchor the author
cites reproduces faithfully; all record numbers transcribe
correctly; the N-W §8.1 load-bearing citation spot-verifies at the
declared pages; the seam declarations (NTF minor (a), F2-C44-FDSTEP,
RC31T-2 object-of-study vs validation-instrument distinction) are
consistent with the cited authorities. The derivation program is
sound in architecture (decomposition + chain law + RMS refinement +
asymmetry mechanism + FD law + identification design) and the
falsifier discipline is genuinely good (nearest-hypothesis E1
adjudication, load-bearing E3 discriminator).

Three content objections, all repairable without new measurements:
(1) CLG-D2's u-linear chain bound omits the forward-state
coefficient channel that the file's own D4-ALT names as plausibly
dominant — one added hypothesis (or an eps_N term + conditional
scoping on q = 1) closes it; (2) the D5/D6 same-lowering
cancellation leg rests on an unstated smoothness/structural-
stability hypothesis on b_L that the bitwise fixed-input witness
cannot carry; (3) the E3 "seven decades" separation is
arithmetically ~4.4 decades (discriminator conclusion survives).
Escalation per standing rule is the judge's call; the refuter notes
that all three repairs fit inside the minor's existing frame (AG-1
hypotheses + one number), none requires the full-form escalation on
technical grounds.

## PAPERS NEEDED

(empty — the objections stand on the record carriers and the N-W
pages already on disk; Higham 2ed remains relevant only to the
author's own THEOREM*->THEOREM upgrade path, unchanged)

## PAPERS CONSULTED (read-depth honesty)

- literature/nocedal_wright_2006_numerical_optimization_2ed.pdf —
  [FULL] book pp. 194-197 (PDF 213-216, rendered), for the (8.5)
  spot-verify.
- All other reads are repo carriers, listed with line ranges and
  depths in VERIFICATION RECORD above.
