# PHASE D MINOR (d) — CROSS-LOWERING GRADIENT FLOOR: FORMAL
# DERIVATION OF THE CHAIN AMPLIFICATION FACTOR (derivable part)
# S-FOUNDATIONS-C4 Blocco 1, 2026-08-20. Author slot per
# BRIEF_blocco2_phaseD.md MINORS (d). ONE refuter round + escalation.
# ID prefix: CLG-. Status: ESCALATION ROUND 3 APPLIED [ESC-r3-0]
# (was: ROUND 2 APPLIED [ESC-r2-0], ROUND 1 APPLIED [ESC-r1-0],
# DRAFT): all 8 sustained findings of refute_minor_crosslowering +
# VERDICT_blocco2 §2.4 repaired in place, markers [ESC-r1-<n>]; then
# all 4 findings of esc_refute_crosslowering_r1.md (1 REPAIR + 2
# AMENDMENT + 1 NOTE) repaired in place, markers [ESC-r2-<n>]; then
# all 3 findings of esc_refute_crosslowering_r2.md (1 REPAIR + 1
# AMENDMENT + 1 NOTE) repaired in place, markers [ESC-r3-<n>];
# disposition tables at EOF.
# Probe: esc_probe_crosslowering_decades.py (ALL PASS, r1 window;
# unchanged by r2/r3 — those repairs are textual/logical, no new
# arithmetic).

## 0. MANDATE AND INPUTS OF RECORD

Mandate row: `docs/findings_registry.yaml` id
`engine:cross-lowering-gradient-floor` (:328-336, read IN FULL).
Scope of this minor = the THEORY HALF ONLY: the formal derivation of
the chain amplification factor — how a per-operation roundoff of
size u ≈ 1.1e-16 becomes a ~1e-8 relative cross-lowering floor on
the adjoint gradient through ~250 implicit 4x4 solves, and how FD
consumers amplify that floor ~7 further orders into H. The three
named scaling experiments (N-ladder, margin-proximity, float32
contrast) are the MEASURED half = F2 duty, named in §8 [ESC-r1-6].
The B-SHAPE
clause of record (convergence review B-F10, row :335) is consumed as
an INPUT (it defines the lowering index), never re-derived and never
presented as a conclusion of this derivation.

Numeric inputs of record (committed carriers; no new measured
numbers are produced by this minor):

| quantity | value | carrier |
|---|---|---|
| cross-lowering gradient floor (rel) | ~1e-8 (sequential eager-vs-jit 2.9e-2 abs on g-scale 2.0e6 = 1.45e-8 rel; vmap B=1 2.2e-2; B-dependent 6.0e-2) | findings_registry.yaml :331; PROGRESS_2026-08-12_S25bis_speed.md STEP 13 (:365-379) |
| value agreement across lowerings (rel) | ~1e-15 | findings :331 |
| chain length | ~250 implicit 4x4 solves | findings :322, :331 |
| FD amplification into H | ~7 orders; mixed-lowering form dH 18% (gate-rejected); corrected same-lowering form dH 4.9e-2 rel, INSIDE the derived bound K_RICH x max(scheme asyms) = 4.9e6 | findings :322; STEP 13 (:381-399) |
| same-lowering determinism witness | lane-permutation control BITWISE | findings :322; STEP 13 (:387-389) |
| B-SHAPE clause (input) | one lowering = one compiled executable AND one batch shape; measured B=1 vs B=9 divergence 6.0e-2 | findings :335 |

Adjacent authorities consumed (not re-litigated): VERDICT_wave2 §
(RC31T-2 block, :47-60 and :200-223) — same-lowering pinning is
standing discipline; cross-lowering pairs REJECTED as validation
comparisons. VERDICT_wave3 :612-620 (C44 adjudication) — FD
step-size ownership sits with F2-C44-FDSTEP; N-W §8.1 [FULL] folded
there. Boundary with both is named in §6 (C44/FD-step) and §8
(RC31T-2 object-of-study clause) [ESC-r1-6: pointer completed —
same systematic slip class as MIN-CROSSLOWERING-6].

## 1. SETUP AND HYPOTHESIS LIST

The replay objective is computed as a chain: states s_k in R^4,
k = 1..N (N ≈ 250), each defined implicitly by the cell relation
R_k(s_k; s_{k-1}, W) = 0 (4x4, Newton-solved to its tolerance
floor), and J = Phi(s_1, ..., s_N; W). The gradient g = dJ/dW is
produced by the exact adjoint (custom_vjp): a single linear reverse
sweep — lambda_{k-1} = T_k^T lambda_k + phi_k with per-stage
transition T_k built from the implicit-function VJP, i.e. one
transposed 4x4 linear solve with matrix A_k = dR_k/ds_k per stage,
plus accumulation g = sum_k (dR_k/dW)^T A_k^{-T} (adjoint weights).

A "lowering" L is one equivalence class of floating-point
executables of this real-arithmetic algorithm: per the B-SHAPE
clause of record (INPUT, findings :335), L = (compiled executable,
batch shape B). Two lowerings differ only by reassociation, fusion
(FMA), reduction order, and lane layout of the SAME real-arithmetic
computation.

Hypotheses (AG-1 valve applied: strong, trivially checkable,
sufficient-not-optimized, declared as such):

- **H1** (arithmetic): IEEE-754 binary64 throughout; standard model
  fl(a op b) = (a op b)(1+delta), |delta| <= u = 2^-53 ≈ 1.11e-16;
  no subnormals/overflow encountered in the chain. Checkable by a
  range monitor on recorded marches.
- **H2** (structure): N stages; per-stage adjoint kernel (one 4x4
  transposed solve + products) has flop count <= m-bar, uniform in k.
  Checkable by inspection of the VJP code: the per-stage adjoint
  kernel lives in validation/a1_ideal_march_jax.py (implicit-solve
  machinery :413-517; @jax.custom_vjp :504; solve.defvjp(fwd, bwd)
  :517 — grep re-verified this window). [ESC-r1-5: previous anchor
  a1_toc_variational_jax.py:1697-1720 was the driver's FD-consumer
  stencil (the registry row's code-field context), not the VJP
  kernel; anchor corrected per MIN-CROSSLOWERING-5.]
- **H3** (conditioning): the linearized systems are uniformly
  invertible on the admissible design set: kappa(A_k) <= kappa-bar
  < inf. Checkable per design from recorded Jacobians.
- **H4** (transport): the adjoint transport is uniformly bounded:
  G := max_k ||T_N T_{N-1} ... T_{k+1}|| < inf (no exponential
  blowup along the chain). Checkable from recorded lambda growth
  along one sweep.
- **H5** (RMS refinement ONLY; declared PRACTICE, not proved):
  cross-lowering per-stage rounding-difference injections behave as
  independent, zero-mean across k. The N-ladder experiment (§8
  [ESC-r1-6: same slip class, instance found in-window beyond the
  refuter's four]) decides it; nothing below except CLG-D3 uses it.
- **H6** (lowering equivalence): both lowerings compute the same
  real-arithmetic function; they differ only within the B-SHAPE
  equivalence classes. INPUT of record (findings :335).
- **H7** (cross-lowering converged-state agreement) [ESC-r1-1]: the
  forward states the adjoint coefficients are evaluated at agree
  across lowerings at unit-roundoff grade,
  ||s-hat_L,k − s-hat_L',k|| <= C_s · u · ||s-hat_k|| for all k,
  with C_s moderate; and the coefficient maps
  s -> (A_k, dR_k/dW, phi_k) are uniformly Lipschitz on the march
  tube (constant absorbed in c) [ESC-r2-2: coefficient-sensitivity
  clause DECLARED — step (iv) of CLG-D2 converts the H7 state gap
  into O(u)-grade coefficient perturbations, which needs a Lipschitz
  bound on dA_k/ds (second derivatives of R_k) and likewise for
  dR_k/dW, phi_k; H3 bounds kappa(A_k), not this sensitivity. AG-1
  valve: strong, trivially checkable from recorded Jacobian
  variation along the march]. AG-1 valve: strong,
  sufficient-not-optimized, DECLARED as such; checkable on recorded
  marches (per-stage cross-lowering state diff vs u·scale). H7 is
  the hypothesis behind the q = 1 side of the u-exponent dichotomy
  of CLG-D7 [ESC-r2-4: was "EXACTLY the q = 1 side" — an implication
  printed as an equivalence; H7 is SUFFICIENT for q = 1 (given D2),
  not equivalent to it: a measured q = 1 floor can coexist with H7
  false if the coefficient channel is subdominant for another
  reason. E3 adjudicates the MECHANISM dichotomy (D2's conclusion);
  the direct verifier of H7 itself is the recorded-march state-diff
  check, the separate cheap adjunct of [ESC-r1-9]]: it EXCLUDES the
  D4-ALT channel (Newton-floor eps_N leakage into the coefficients,
  sqrt(u)-class) by hypothesis — D2-under-H7 and D4-ALT are
  exclusive hypotheses, adjudicated by E3 (§8, prediction P3).
- **H8** (b_L structural stability over an FD step) [ESC-r1-2]: the
  lowering-systematic bias b_L(W) of CLG-D1, restricted to one
  lowering, varies over an FD step h by no more than h times the
  measured same-lowering scheme self-asymmetry:
  ||b_L(W + h e_i) − b_L(W)|| <= h · (the scheme-asymmetry scale of
  record), hence a fortiori [ESC-r3-3: was "i.e." — the inequality
  gives ||delta b_L||/h <= max(asyms) while the band admits up to
  K_RICH · max(asyms) (K_RICH ≈ 4 on the record numbers): an
  implication in the safe direction, not a restatement; edit adopted
  from ESC-CROSSLOWERING-r2-3's contingent phrasing since the file
  is edited this round] its FD-mapped contribution
  ||delta b_L|| / h to dH
  stays inside the K_RICH x max(scheme asyms) acceptance band
  (findings :322; STEP 13 :381-399) [ESC-r2-1: h factor inserted /
  band membership restated — the r1 printed RHS was an H-scale
  absolute (~1e6) bounding a g-scale variation (b differences
  ~1e-2 abs on g_sc 2.0e6): unit-incoherent and, read literally,
  weak enough to permit ||delta b_L|| of order half the gradient,
  under which the D5 cancellation leg would not follow. The
  declared check below (scheme self-asymmetry at the consumer's h)
  already measures the FD-mapped quantity, so only the printed
  inequality changes; CLG-D5's "H8-bounded variation" clause and
  CLG-D6 inherit the corrected form without further text].
  Declared PRACTICE (not proved): b_L is
  deterministic (bitwise witness, fixed inputs) but in general only
  piecewise-continuous in W — per-op rounding coefficients can flip
  as intermediates cross rounding boundaries — so smoothness over a
  step is a HYPOTHESIS, carried by the measured same-lowering FD
  success (corrected M6 form inside its K_RICH band), not by the
  fixed-input bitwise witness. Checkable: repeat the same-lowering
  scheme self-asymmetry measurement at the consumer's h.

## 2. CLG-D1 — DECOMPOSITION AND SAME-LOWERING DETERMINISM

**Statement (SCHEMA).** The computed gradient in lowering L admits
the decomposition

  g-hat_L(W) = g(W) + b_L(W) + eta_L(W),

where b_L(W) is the lowering-systematic bias — a DETERMINISTIC
function of (executable, batch shape, W) — and eta_L collects
sub-leading terms. Determinism of the map (L, inputs) -> bits is the
measured witness of record: the lane-permutation control is BITWISE
invariant (findings :322; STEP 13 :387-389) — lane content fully
determines the result within one lowering. The cross-lowering floor
of record is then phi := max over lowering pairs of
||b_L - b_L'|| / g_sc ≈ 1e-8 (g_sc = gradient scale of record
2.0e6, findings :331).

**Why SCHEMA and not THEOREM:** the split b vs eta is a modeling
choice (leading reassociation-systematic part vs remainder); its
operational content is the determinism leg plus the common-mode
cancellation corollary CLG-D6, both carried by bitwise-grade
measured witnesses of record.

**Falsifier:** any same-executable, same-batch-shape repeat on
identical recorded inputs that differs bitwise kills the determinism
leg (and with it the common-mode cancellation logic). Current
evidence: bitwise PASS.

## 3. CLG-D2 — WORST-CASE CHAIN FLOOR LAW (the amplification factor)

**Statement (THEOREM*).** Under H1-H4, H6, **and H7** [ESC-r1-1],
there is a constant c depending on the per-stage kernel shape AND
the H7 regularity constants (C_s and the coefficient-map Lipschitz
bounds); its kernel-shape part is <= a small multiple of m-bar via
the standard gamma_m = m·u/(1−m·u) reassociation bound [ESC-r3-1:
was "depending only on the per-stage kernel shape (c <= a small
multiple of m-bar ...)" — false as printed, since step (iv) (per
[ESC-r1-1]/[ESC-r2-2]) absorbs into c the H7 state-agreement
constant C_s and the coefficient-map Lipschitz constants, which are
march-equation regularity properties on the march tube, not kernel
flop-count properties, and are NOT priced by the gamma_m mechanism;
only the kernel-shape part of c is. Per ESC-CROSSLOWERING-r2-1; no
label move — "Why THEOREM*" already disclaims Higham-grade constant
tracking]. Then, to first order in u,
for any two lowerings L, L':

  ||g-hat_L − g-hat_L'|| / g_sc  <=  c · u · kappa-bar · G · N.

Equivalently, the CHAIN AMPLIFICATION FACTOR

  Phi_chain := (cross-lowering floor, rel) / u  <=  c · kappa-bar · G · N.

**Proof sketch.** (i) Fix a stage k. Both lowerings apply the same
real-arithmetic kernel (H6) to (their own) inputs; by the standard
model (H1) and the reassociation bound for a kernel of <= m-bar
flops containing one 4x4 transposed solve, the computed outputs of
the two lowerings applied to a COMMON input differ by
<= c1 · u · kappa(A_k) · ||input|| to first order (the kappa factor
enters because the solve maps backward-stable per-op errors to
forward error at the conditioning of A_k; 4x4 direct solves are
normwise backward stable at this size). (ii) The adjoint recursion
is LINEAR in lambda: a discrepancy delta_k injected at stage k is
transported to the output through T_N ... T_{k+1}, hence with gain
<= G (H4). Inputs to stage k themselves differ across lowerings, but
that difference is exactly the accumulated discrepancy from stages
> k, already counted — linearity prevents double amplification to
first order in u. (iii) Triangle inequality over the N injection
points and the accumulation sum gives the bound; the (dR_k/dW)^T
accumulation contributes one more bounded factor absorbed in c.
(iv) [ESC-r1-1] COEFFICIENT CHANNEL, closed by H7: steps (i)-(iii)
count discrepancies injected inside the adjoint sweep; the adjoint
COEFFICIENTS A_k = dR_k/ds_k, dR_k/dW and phi_k are additionally
evaluated at the FORWARD states s-hat_k, which differ across
lowerings by the converged-state gap. Under H7 that gap is
C_s·u·scale, and by H7's coefficient-sensitivity Lipschitz clause
[ESC-r2-2] the induced coefficient perturbations are O(u)·scale in
norm, so they inject per-stage discrepancies of the same
O(u)·kappa·G grade already counted — absorbed into c to first
order in u. WITHOUT H7 this
channel is NOT priced by H1-H4/H6: if the forward states agree only
to the Newton tolerance floor eps_N (plausibly sqrt(u)-class, the
D4-ALT channel, NTF-owned), the bound gains an additive term and
reads

  ||g-hat_L − g-hat_L'|| / g_sc
    <=  c · u · kappa-bar · G · N  +  c' · eps_N-class · kappa-bar · G · N,

and the u-LINEAR form of the law is CONDITIONAL on q = 1 — for
which H7 is the sufficient hypothesis [ESC-r3-2: was "i.e. on H7
holding", an equivalence reading; H7 is SUFFICIENT for q = 1, not
equivalent to it, per the r2-4-repaired §1 form — pre-existing
same-class instance, swept file-wide per the [ESC-r1-6] precedent]
— which is exactly what E3 (§8, prediction P3)
adjudicates. D2-as-printed and CLG-D4-ALT are thereby EXCLUSIVE
hypotheses, not a theorem coexisting with its own counterexample
channel. QED (sketch).

**Why THEOREM\* and not THEOREM:** the constants are not tracked at
Higham grade (per-op inventory of the actual compiled kernels, FMA
contraction cases, reduction-tree shapes); H3/H4 are assumed
uniform rather than derived from the march equations; and H7 is an
assumed (checkable, unmeasured) state-agreement grade, not a proved
property of the Newton-converged march [ESC-r1-1]. Upgrading to
THEOREM needs the constant-grade rounding analysis reference (see
PAPERS NEEDED) plus measured kappa-bar and G — the latter are
exactly two of the F2 identification targets (§8 [ESC-r1-6]) — plus
the H7 state-diff check on recorded marches.

**Consistency with record (derived arithmetic from carried
numbers, shown):** Phi_chain(measured) = 1.45e-8 / 1.11e-16 ≈
1.3e8. With N = 250: the bound requires c · kappa-bar · G >=
1.3e8 / 250 ≈ 5.2e5 at the linear-in-N reading. Near-sonic /
marginal-cell 4x4 conditioning of order 1e3-1e5 times transport of
order 1e1-1e3 [ESC-r1-4: these two ranges are UNANCHORED
order-of-magnitude estimates, PRACTICE class, carrying NO carrier —
pending the F2 measurements (E2 for kappa, the H4 lambda-growth
check for G)] is compatible with this range — the law is
CONSISTENT with the measured floor, but the current record CANNOT
separate kappa-bar from G from the N-exponent (see CLG-D7).

**Falsifier:** once kappa-bar and G are measured (F2, §8
[ESC-r1-6]), a
measured floor exceeding c · u · kappa-bar · G · N falsifies the
law (missing mechanism); a measured super-linear growth in N
falsifies H2-H4 as stated (compounding mechanism present).

## 4. CLG-D3 — RMS REFINEMENT (sqrt-N scaling)

**Statement (SCHEMA, conditional on H5).** Under H1-H6 with H5, the
expected floor scales as

  E ||g-hat_L − g-hat_L'|| / g_sc  ~  c · u · kappa_eff · G_rms · sqrt(N),

with kappa_eff, G_rms the quadratic means of the per-stage factors.
At the sqrt-N reading, the record requires c · kappa_eff · G_rms ≈
1.3e8 / 15.8 ≈ 8.2e6 — also inside the plausible range; the
N-ladder decides between D2-linear and D3-sqrt (see §8, prediction
P1 [ESC-r1-6]).

**Falsifier:** N-ladder log-log slope p-hat closer to 1 than to 1/2
(nearest-hypothesis adjudication — no magic threshold: the
discriminator is |p-hat − 1/2| vs |p-hat − 1| with the regression
CI covering at most one of the two) kills D3 and keeps D2 as the
operative law; slope above ~1 (CI excluding 1) kills both as
stated (see CLG-D2 falsifier).

## 5. CLG-D4 — VALUE/GRADIENT ASYMMETRY (why J holds 1e-15 while g
## floors at 1e-8)

**Statement (SCHEMA).** The forward chain is SELF-CORRECTING: each
s_k is the limit of a Newton iteration converged to its tolerance
floor — cross-lowering perturbations of intermediate iterates are
re-absorbed by re-convergence to (a floating-point neighborhood of)
the same fixed point, so state discrepancies do not compound
multiplicatively along the chain and J agrees at ~1e-15 = O(u)
(measured, findings :331). The adjoint sweep has NO fixed point and
NO re-convergence: it is one linear pass in which every per-stage
rounding discrepancy is transported to the output un-repaired
(CLG-D2 (ii)). The ~7-decade gap between the value floor (1e-15)
and the gradient floor (1e-8) is therefore structural
(transport-without-repair, amplified by kappa-bar · G · N^p), not
incidental.

**Falsifier (named, not scheduled — it is NOT one of the three
mandated experiments):** per-stage iterative refinement of the
adjoint solves (re-converging each transposed 4x4 solve to residual
floor) must REDUCE the cross-lowering floor if
transport-of-unrepaired-roundoff is the mechanism; an unchanged
floor under adjoint iterative refinement falsifies D4's mechanism
attribution (and points at the D7-ALT channel below).

**CLG-D4-ALT (CONJECTURE, named alternative for the refuter):** the
observed floor 1.45e-8 sits at sqrt(u)-class, which is also the
class of a primal Newton-tolerance floor leaking into the adjoint
COEFFICIENTS (A_k evaluated at states carrying their own
convergence floor eps_N; NTF-owned, minor (a) of this brief — one
derivation program, no collisions: this minor does NOT derive
eps_N). Under D4-ALT the floor scales with the Newton floor (hence
with NTF and only indirectly with u), not linearly in u. The
float32 contrast (§8, prediction P3 [ESC-r1-6]) discriminates D2/D3 (q = 1 in
u^q) from D4-ALT (q ≈ 1/2 through the sqrt(u)-class Newton floor)
— this is exactly why the float32 experiment is load-bearing.
[ESC-r1-6: all experiment pointers (E1-E3/P1-P3/F2-CLG-SCALE) now
resolve to §8/CLG-D7; the §9 N-W where_read "§6" anchor is correct
and unchanged, per MIN-CROSSLOWERING-6.]

## 6. CLG-D5 — FD AMPLIFICATION LAW INTO H

**Statement (THEOREM*).** Let a consumer build Hessian columns by
forward differences of the adjoint gradient with step h. Adapting
the standard FD error model (Nocedal-Wright 2ed, §8.1, eq. (8.5)
class: total error <= truncation (L_H/2)·h + noise 2·eta/h, read
[FULL] at pp. 194-197), with eta = the ABSOLUTE gradient noise of
the pairing used:

- CROSS-lowering pair (the M6 first-form defect class): eta =
  phi · g_sc, hence the relative H-contamination is

    dH/H_sc  ~  A_FD · phi,   A_FD := 2 · g_sc / (h · H_sc),

  i.e. the floor is amplified by A_FD — the second amplification
  stage of the mandate ("FD amplifies ~7 orders").
- SAME-lowering pair (one executable, one batch shape, per B-SHAPE)
  [ESC-r1-2 — this leg is graded SCHEMA, conditional on H8; the
  cross-lowering leg above keeps THEOREM* grade]: UNDER H8 (b_L
  stable over the FD step, §1 — a declared hypothesis, since the
  bitwise witness covers determinism at FIXED inputs only, not
  stability across NEIGHBORING inputs), the systematic component
  b_L is common-mode and cancels to first order in the difference
  (CLG-D1 decomposition), leaving the sub-leading eta_L residue plus
  the H8-bounded variation — the mechanism by which the sequential
  FD Hessian works and the corrected in-batch-base M6 form meets its
  derived bound K_RICH x max(scheme asyms) (findings :322, of
  record; that bound formulation is the acceptance authority, not
  re-derived here; the measured in-band result is the standing
  witness that the slowly-varying part of b_L dominates, i.e. that
  H8 holds at the operating point of record).

**Consistency with record (derived arithmetic from carried numbers,
shown):** measured mixed-lowering contamination dH = 18% rel at
floor phi = 1.45e-8 rel gives A_FD(implied) = 0.18 / 1.45e-8 ≈
1.2e7 = 10^7.1 — i.e. "~7 orders" exactly as carried by the row
(findings :322). [ESC-r1-8: pair-choice declared — phi = 1.45e-8 is
the SEQUENTIAL eager-vs-jit floor, while the M6 18%-incident pair
was batched-rows-vs-separate-sequential-base (divergences 2.2e-2 to
8.2e-2 abs = 1.1e-8 to 4.1e-8 rel, STEP 13 :366-368); the
pair-matched phi moves A_FD(implied) by at most ~2.8x, to
10^6.6-10^7.2 (probe esc_probe_crosslowering_decades.py, PASS) —
the "~7 orders" reading is robust to the choice.] The h-value and
H_sc identification inside A_FD
are FD-step territory OWNED by F2-C44-FDSTEP (VERDICT_wave3
:612-620); this minor states the law and consumes the measured
consistency, it does NOT adjudicate step choice. No collision.

**Why THEOREM\*:** the bound form is textbook-grade (N-W §8.1 read
[FULL] at the cited pages) but transplanted onto a noise source
(cross-lowering bias) that is deterministic-systematic rather than
the i.i.d.-roundoff of the textbook model; the transplant step is
the un-hardened link (R-4 discipline: transplant DECLARED).
[ESC-r1-2: the THEOREM* grade attaches to the CROSS-lowering branch
only; the same-lowering cancellation branch is SCHEMA conditional
on H8, as marked in the bullet above.]

**Falsifier:** with phi measured on a lowering pair and (h, H_sc)
pinned by the consumer, a measured dH outside the K_RICH-band
around A_FD · phi falsifies the law (either a missing noise channel
or a wrong cancellation claim).

## 7. CLG-D6 — COROLLARY: PINNING DISCIPLINE IS THE ZERO-COST
## MITIGATION (consistency statement, not new policy)

**Statement (SCHEMA, corollary of D1+D5).** At floor phi, any
gradient COMPARISON or FD stencil across lowerings incurs
irreducible noise >= phi · g_sc (D1), FD-amplified by A_FD (D5);
within one lowering, UNDER H8, the systematic part cancels to first
order [ESC-r1-2]. Hence the standing discipline of record — "every
gradient COMPARISON or FD stencil pins ONE lowering" (findings :335;
VERDICT_wave2 RC31T-2 pin: cross-lowering pairs REJECTED at update
time) — is derived here, CONDITIONAL ON H8, as the unique zero-cost
mitigation [ESC-r1-2: "derived" inherits the D5 repair — the
cancellation leg rests on the declared b_L-stability hypothesis H8,
witnessed by the measured in-band same-lowering FD of record, not
on the fixed-input bitwise witness alone]. This corollary ADDS no
policy; it gives the registered discipline its formal footing.

**Falsifier:** inherits D1's (bitwise determinism) and D5's
(cancellation) falsifiers, plus H8's check (same-lowering scheme
self-asymmetry re-measured at the consumer's h) [ESC-r1-2].

## 8. CLG-D7 — IDENTIFICATION GAP + THE MEASURED HALF (F2 DUTY NAMED)

**Statement (SCHEMA).** The current record (one N, one precision,
one design neighborhood) CANNOT identify the four structural
unknowns of the law: the N-exponent p in {1/2, 1}, the split of
c · kappa-bar · G into conditioning vs transport, the u-exponent q
(u^1 per D2/D3 vs sqrt(u)-class per D4-ALT/NTF leak), and the
margin dependence of kappa-bar. The three experiments named by the
mandate row (:335) are exactly an identification design for these
unknowns:

**F2 DUTY NAMED: F2-CLG-SCALE** (measured half; owner = F2 entry,
alongside the NTF derivation program per the row text; the
cross-lowering pairs it measures are the OBJECT OF STUDY — this is
permitted and does not collide with the RC31T-2 rejection of
cross-lowering pairs as VALIDATION instruments):

- **(E1) chain-length N-ladder:** floor vs N on truncated/extended
  replay chains, log-log. Prediction P1: slope p = 1/2 under H5
  (D3), p = 1 worst-case (D2); adjudication = nearest-hypothesis
  with CI (no magic threshold), per CLG-D3's falsifier.
- **(E2) margin-proximity:** floor vs certification margin class of
  the design (marginal cells raise kappa(A_k)). Prediction P2:
  floor increases monotonically as margin shrinks, tracking the
  recorded kappa(A_k) of the worst cells; a flat response falsifies
  the kappa-bar leg of D2 (conditioning not the carrier — transport
  G dominant).
- **(E3) float32 contrast:** same pair of lowerings in binary32
  (u32 = 2^-24 ≈ 5.96e-8). Prediction P3: under q = 1 (D2/D3),
  floor ratio phi32/phi64 ≈ u32/u64 = 2^29 ≈ 5.4e8, i.e. f32
  gradients are O(1)-corrupted (predicted phi32 ≈ 1.3e8 · 6e-8 ≈
  O(1-10)); under the sqrt-class D4-ALT, ratio ≈ 2^14.5 ≈ 2.3e4,
  i.e. phi32 ≈ 3e-4 — ~4.4 decades of separation between the two
  predictions (ratio-of-ratios 2^29 / 2^14.5 = 2^14.5 ≈ 2.3e4x;
  probe esc_probe_crosslowering_decades.py, PASS): an unambiguous
  discriminator. [ESC-r1-3: the draft said "seven decades" — wrong
  derived number (contamination from the separate "~7 orders FD
  amplification" figure), corrected per MIN-CROSSLOWERING-3; the
  discriminator conclusion survives at ~4.4 decades.]

All three run on recorded marches with the existing engine — zero
package changes (env pinned), zero CFD. Numbers above marked
"prediction" are derived arithmetic from carried record numbers
with the arithmetic shown; none is asserted as measured.

**Falsifier for D7 itself:** if the three experiments jointly fail
to separate the hypotheses (e.g. p-hat CI covering both 1/2 and 1
AND E3 landing between the two predicted decades), the
identification claim is falsified and the law must be re-derived
with a finer error model (escalation path, declared).

## 9. LANDING NOTES (for the Blocco-2 judge / orchestrator; not
## self-executed)

- Adoptable statements [ESC-r2-3: bullet rewritten IN PLACE with
  the post-r1 labels — the pre-repair unconditional labels formerly
  printed here (D2 without H7, D5 without the branch split, D6
  without the H8 conditional) are VOID; [ESC-r1-9] below records the
  derivation of these labels]: CLG-D2 (THEOREM* under H1-H4+H6+H7,
  u-linear form conditional on q = 1 (sufficient hypothesis: H7),
  E3-adjudicated [ESC-r3-2: was "q = 1 = H7" — an equality sign
  between the empirical exponent and the hypothesis, freshly printed
  by the r2-3 rewrite in this machine-harvest line; corrected to the
  sufficiency form of the r2-4-repaired §1 H7]), CLG-D5
  (THEOREM* on the cross-lowering branch; same-lowering cancellation
  leg SCHEMA conditional on H8), CLG-D6 (SCHEMA conditional on H8),
  CLG-D1/D3/D4/D7 (SCHEMA), CLG-D4-ALT (CONJECTURE). Proposed
  M0 site: the engine-discipline block adjacent to the
  same-lowering standing rule; registry row
  `engine:cross-lowering-gradient-floor` owner field gains "formal
  derivation LANDED (chain law THEOREM* under H7, u-linear
  conditional on q = 1; FD law THEOREM* cross-lowering branch /
  SCHEMA-conditional-H8 same-lowering leg);
  F2-CLG-SCALE = the three-experiment identification design
  (E1/E2/E3 with predictions P1/P2/P3)".
- Lit-registry promotion: Nocedal-Wright 2ed §8.1 read [FULL] at
  book pp. 194-197 (PDF 213-216) — where_read anchor = this file
  §6. (Wave-3 had already folded a §8.1 [FULL] read into
  F2-C44-FDSTEP, VERDICT_wave3 :612-615; this read is the executed
  instance for the error-model equations.)
- Seam declarations: NTF minor (a) owns the Newton-floor
  derivation (D4-ALT only NAMES the channel); F2-C44-FDSTEP owns
  FD step choice (D5 only states the law). One derivation program,
  no collisions.
- [ESC-r1-9] ESCALATION-r1 LABEL CORRECTIONS to the adoptable list
  above (the bullet at the top of §9 is superseded on these points
  [ESC-r2-3: the supersession is now CONSUMED — the top bullet has
  been rewritten in place with these labels; this bullet remains as
  the derivation record]):
  CLG-D2 = THEOREM* under H1-H4, H6, H7 (u-linear form CONDITIONAL
  on q = 1 = H7, adjudicated by E3; without H7 the bound carries the
  additive eps_N-class term, §3 step (iv)); CLG-D5 = THEOREM* on the
  cross-lowering branch, same-lowering cancellation leg = SCHEMA
  conditional on H8; CLG-D6 "derived" = conditional on H8; E3
  prediction P3 separation = ~4.4 decades (2^14.5 ≈ 2.3e4x), not
  seven. Registry owner-field text (if adopted) should carry these
  conditional forms verbatim. New hypotheses H7/H8 are declared in
  §1 with checkability routes; both checks are cheap adjuncts of the
  F2-CLG-SCALE campaign (H7: recorded-march state diffs; H8: scheme
  self-asymmetry at the consumer's h).

## PAPERS NEEDED

- Higham, "Accuracy and Stability of Numerical Algorithms" 2ed
  (SIAM 2002) — NOT on disk. Needed ONLY for the THEOREM*->THEOREM
  upgrade of CLG-D2 (constant-grade gamma_m reassociation bounds and
  backward-stability constants for small direct solves). The minor
  stands at THEOREM* without it.

## PAPERS CONSULTED (read-depth honesty)

- literature/nocedal_wright_2006_numerical_optimization_2ed.pdf —
  [FULL] on §8.1 error-model portion, book pp. 194-197 (PDF
  213-216); used for eq. (8.5)-class bound and optimal-step
  structure in CLG-D5. [ESC-r1-7: draft declared two ranges
  (194-197 in §6 vs 194-199 here); unified to 194-197, the
  refuter-verified range (spot-verify PASS) and the one carried by
  the VERDICT lit promotion LB-5; pp. 198-199 are NOT claimed
  read.]
- literature/giles_pierce_1997_adjoint_equations_cfd_aiaa97_1850.pdf
  — NOT consulted (not needed for this minor; it is the R27/T-RED
  leg, other slot's duty).
- Registry/verdict carriers read [FULL] at cited lines:
  docs/findings_registry.yaml :319-336;
  validation/PROGRESS_2026-08-12_S25bis_speed.md STEP 13 (:362-399);
  VERDICT_wave2.md :40-64, :200-223; VERDICT_wave3.md :605-620.

## ESCALATION ROUND 1 — DISPOSITION TABLE [ESC-r1] (appended EOF,
## 2026-08-20; author-reviser slot per VERDICT_blocco2 §3 E-4)

Inputs of record read IN FULL this window: refute_minor_crosslowering.md;
VERDICT_blocco2.md §2.4 (:199-234) + §3 E-4 (:256-258) + LB-5 (:491-500).
Repair texts on the page were VERIFIED before adoption: code anchors
re-grepped in-window (a1_ideal_march_jax.py custom_vjp :18/:413/:440/
:496/:504, defvjp :517); arithmetic re-derived by executable probe
esc_probe_crosslowering_decades.py, ALL PASS in-window (separation
4.36 decades; A_FD pair-matched 10^6.64-10^7.21; max shift 2.83x).

| Finding | Class | Disposition | Marker(s) | What changed |
|---|---|---|---|---|
| MIN-CROSSLOWERING-1 | CONTENT SUSTAINED | REPAIRED (both named options adopted: H7 AND the conditional two-term form) | [ESC-r1-1] | New hypothesis H7 (cross-lowering converged-state agreement O(u), AG-1-declared, checkable on recorded marches) added in §1; CLG-D2 statement now "Under H1-H4, H6, and H7"; proof sketch gains step (iv) pricing the coefficient channel (A_k, dR_k/dW, phi_k at forward states): closed by H7, and WITHOUT H7 the bound carries the additive c'·eps_N-class·kappa-bar·G·N term with the u-linear form CONDITIONAL on q = 1, adjudicated by E3 — D2 and D4-ALT are now exclusive hypotheses; "Why THEOREM*" names H7 as assumed-not-proved |
| MIN-CROSSLOWERING-2 | CONTENT SUSTAINED | REPAIRED (hypothesis declared AND leg regraded — stronger than either single option) | [ESC-r1-2] | New hypothesis H8 (b_L structural stability over an FD step, bounded by the measured scheme self-asymmetry, findings :322 / STEP 13 :381-399; declared PRACTICE, checkable) added in §1; CLG-D5 same-lowering bullet regraded SCHEMA conditional on H8 (cross-lowering branch keeps THEOREM*), with the piecewise-continuity caveat and the fixed-input-only scope of the bitwise witness stated; CLG-D6 "derived" made CONDITIONAL ON H8, falsifier extended with the H8 check |
| MIN-CROSSLOWERING-3 | CONTENT SUSTAINED | REPAIRED (number corrected; probe added) | [ESC-r1-3] | "seven decades" replaced by "~4.4 decades (2^14.5 ≈ 2.3e4x)" in §8 E3/P3; contamination source named; discriminator conclusion retained at 4.4 decades; executable rejector probe esc_probe_crosslowering_decades.py commits the corrected arithmetic (asserts kill the seven-decade claim) |
| MIN-CROSSLOWERING-4 | WORDING SUSTAINED | REPAIRED | [ESC-r1-4] | kappa/G ranges in §3 consistency paragraph labeled UNANCHORED order-of-magnitude, PRACTICE class, no carrier, pending F2 (E2 + H4 lambda-growth check); "covers this range without strain" softened to "is compatible with this range" |
| MIN-CROSSLOWERING-5 | WORDING SUSTAINED | REPAIRED (anchor re-verified in-window before adoption) | [ESC-r1-5] | H2 anchor corrected to validation/a1_ideal_march_jax.py :413-517 (@jax.custom_vjp :504, solve.defvjp :517); wrong transplant of the registry code-field anchor (a1_toc_variational_jax.py:1697-1720 = driver FD-consumer stencil) named in place |
| MIN-CROSSLOWERING-6 | WORDING SUSTAINED | REPAIRED (4 named instances + 2 further instances of the same slip class found in-window: §0 boundary clause, §1 H5) | [ESC-r1-6] | All experiment pointers (E1-E3/P1-P3/F2-CLG-SCALE) now resolve to §8/CLG-D7: §0 (x2), §1 H5, §3 (x2: targets + falsifier), §4, §5; the §9 N-W where_read "§6" anchor confirmed correct and UNCHANGED per the finding |
| MIN-CROSSLOWERING-7 | NOTE SUSTAINED | REPAIRED | [ESC-r1-7] | Page range unified to book pp. 194-197 (PDF 213-216) — the refuter-verified range, matching VERDICT LB-5 ("narrower range is the verified one"); pp. 198-199 explicitly NOT claimed read |
| MIN-CROSSLOWERING-8 | NOTE SUSTAINED | REPAIRED | [ESC-r1-8] | Declaring clause added in §6 consistency paragraph: phi = sequential eager-vs-jit pair vs the batched-pair M6 incident (1.1e-8 to 4.1e-8 rel, STEP 13 :366-368); pair-matched A_FD(implied) = 10^6.6-10^7.2, max shift 2.83x (probe PASS); "~7 orders" robust |

Label state after r1 (supersedes the §9 top bullet where they differ,
per [ESC-r1-9]): CLG-D2 THEOREM* under H1-H4+H6+H7 (u-linear
conditional on q = 1, E3-adjudicated); CLG-D5 THEOREM*
(cross-lowering branch) / SCHEMA-conditional-H8 (same-lowering leg);
CLG-D6 SCHEMA conditional on H8; CLG-D1/D3/D4/D7 SCHEMA and
CLG-D4-ALT CONJECTURE unchanged. No measurement was produced; all
new numbers are derived arithmetic committed to the probe with
rejecting asserts. Files written this window: this file (in-place,
markers [ESC-r1-0..9]) + esc_probe_crosslowering_decades.py. Next:
refutation lens per E-4 form of record (until-dry with cap), closure
judge.

## ESCALATION ROUND 2 — DISPOSITION TABLE [ESC-r2] (appended EOF,
## 2026-08-20; author-reviser slot, escalation round 2)

Inputs of record read IN FULL this window:
esc_refute_crosslowering_r1.md (all 4 findings + verification record
+ verdict summary). The refuter's positive record is accepted as
standing (all 8 r1 repairs ratified; findings below attack residual
defects IN the repairs). No probe change needed: all 4 dispositions
are textual/logical repairs with no new arithmetic;
esc_probe_crosslowering_decades.py unchanged and its r1 PASS record
stands.

| Finding | Class | Disposition | Marker(s) | What changed |
|---|---|---|---|---|
| ESC-CROSSLOWERING-r1-1 | REPAIR | FIXED (h-scaled form AND band-membership restatement, both adopted) | [ESC-r2-1] | §1 H8 printed inequality corrected to ||b_L(W+h e_i) − b_L(W)|| <= h · (scheme-asymmetry scale of record), with the FD-mapped band-membership reading (||delta b_L||/h inside the K_RICH x max(scheme asyms) band) stated inline; the r1 unit-incoherence (H-scale RHS ~1e6 bounding a g-scale variation, too weak for the D5/D6 cancellation leg) named in the marker; the declared check (self-asymmetry at the consumer's h) was already coherent and is unchanged; CLG-D5 "H8-bounded variation" clause and CLG-D6 inherit the corrected form without further text, per the refuter's own repair spec |
| ESC-CROSSLOWERING-r1-2 | AMENDMENT | FIXED (H7 extended, step (iv) wired to it) | [ESC-r2-2] | §1 H7 gains the coefficient-sensitivity clause "the coefficient maps s -> (A_k, dR_k/dW, phi_k) are uniformly Lipschitz on the march tube (constant absorbed in c)", AG-1-declared (strong, trivially checkable from recorded Jacobian variation), with the gap named (H3 bounds kappa(A_k), not sensitivity of A_k to its evaluation point); CLG-D2 step (iv) now cites the clause explicitly when converting the state gap to O(u) coefficient perturbations |
| ESC-CROSSLOWERING-r1-3 | AMENDMENT | FIXED (in-place rewrite, the refuter's primary option) | [ESC-r2-3] | §9 top "Adoptable statements" bullet REWRITTEN IN PLACE with the post-r1 labels (D2 THEOREM* under H1-H4+H6+H7; D5 branch split; D6 conditional on H8) and an inline voiding of the formerly printed pre-repair labels; registry owner-field proposal text updated to carry the conditional forms verbatim per [ESC-r1-9]'s own instruction; [ESC-r1-9] annotated as CONSUMED (kept as derivation record) |
| ESC-CROSSLOWERING-r1-4 | NOTE | FIXED (soften applied + implication made exact) | [ESC-r2-4] | §1 H7: "is EXACTLY the q = 1 side" replaced by "is the hypothesis behind the q = 1 side", with the sufficiency-not-equivalence logic stated inline (measured q = 1 can coexist with H7 false via a subdominant coefficient channel; E3 adjudicates D2's conclusion, the recorded-march state-diff check verifies H7 itself — division of labor already printed in [ESC-r1-9], unchanged) |

CONTESTED: none — all 4 findings adopted as specified by the refuter.

Label state after r2: UNCHANGED from [ESC-r1-9]/r1 table as
predicted by the refuter's own impact line — CLG-D2 THEOREM* under
H1-H4+H6+H7 (H7 now carrying the Lipschitz clause; u-linear
conditional on q = 1, E3-adjudicated); CLG-D5 THEOREM*
(cross-lowering branch) / SCHEMA-conditional-H8 (same-lowering leg,
H8 now h-scaled and well-posed); CLG-D6 SCHEMA conditional on H8;
CLG-D1/D3/D4/D7 SCHEMA; CLG-D4-ALT CONJECTURE. No grade moves; the
conditions are now well-posed. No measurement produced; no new
arithmetic (probe unchanged). Files written this window: this file
only (in-place, markers [ESC-r2-0..4]). PAPERS NEEDED: unchanged
(Higham 2ed, THEOREM upgrade path only).

## ESCALATION ROUND 3 — DISPOSITION TABLE [ESC-r3] (appended EOF,
## 2026-08-20; author-reviser slot, escalation round 3)

Inputs of record read IN FULL this window:
esc_refute_crosslowering_r2.md (verification record + all 3 findings
+ verdict summary + papers sections). The r2 refuter's positive
record is accepted as standing (all 4 r1 repairs ratified at anchor;
probe re-run PASS with output identical to the r1 record; H8
dimensional check ratified; registry :316-339 and STEP 13 :362-399
re-verified at source). BREAK count in r2 = 0; the 3 findings below
are residual-defect repairs IN the r2 repairs, all textual/logical.
No probe change: esc_probe_crosslowering_decades.py unchanged, its
recorded ALL-PASS stands (no new arithmetic introduced by r3).
Pre-repair sweep re-run in-window (grep "q = 1|= H7" over this
file): live-text instances of the H7/q=1 equivalence class = §3 :231
and §9 :468 ONLY — exactly the two the refuter named; [ESC-r1-9]
(:495) exempt as annotated consumed derivation record; disposition
tables = append-only round history, not live claims, left unedited.

| Finding | Class | Disposition | Marker(s) | What changed |
|---|---|---|---|---|
| ESC-CROSSLOWERING-r2-1 | REPAIR | FIXED (dependence restatement adopted as specified) | [ESC-r3-1] | §3 CLG-D2 statement: "constant c depending only on the per-stage kernel shape (c <= a small multiple of m-bar via ... gamma_m ...)" corrected to "c depending on the per-stage kernel shape AND the H7 regularity constants (C_s and the coefficient-map Lipschitz bounds); its kernel-shape part is <= a small multiple of m-bar via the standard gamma_m bound"; the defect origin (step (iv)/[ESC-r2-2] absorbing march-equation regularity constants into c that the gamma_m mechanism does not price; RES-CAP-1 class, refuter-prescribed "(constant absorbed in c)" adopted without reconciling the statement) named in the marker; no label move, "Why THEOREM*" already disclaims Higham-grade constant tracking, per the refuter's own impact line |
| ESC-CROSSLOWERING-r2-2 | AMENDMENT | FIXED (both one-phrase edits adopted as specified) | [ESC-r3-2] (x2) | §9 adoptable-statements bullet: "conditional on q = 1 = H7, E3-adjudicated" corrected to "conditional on q = 1 (sufficient hypothesis: H7), E3-adjudicated" — the machine-harvest line no longer prints an equality between the empirical exponent and the hypothesis; §3 step-(iv) closing: "on q = 1 — i.e. on H7 holding —" corrected to "on q = 1 — for which H7 is the sufficient hypothesis —" (pre-existing same-class instance, now swept file-wide per the [ESC-r1-6] precedent the refuter invoked); live §1/§3/§9 texts now state the SAME logical relation (H7 sufficient for q = 1); [ESC-r1-9] :495 left as-is per the finding's explicit exemption |
| ESC-CROSSLOWERING-r2-3 | NOTE | FIXED (contingent edit adopted — file edited this round, so the note's "if ever edited" condition fired) | [ESC-r3-3] | §1 H8: "i.e." joining the h-scaled inequality to its K_RICH-slack consequence replaced by "hence a fortiori", with the implication-not-restatement logic (||delta b_L||/h <= max(asyms) implies band membership up to K_RICH ≈ 4 slack, safe direction) recorded inline so no later consumer flags the slack as an inconsistency; declared check unchanged |

CONTESTED: none — all 3 findings adopted as specified by the r2
refuter (r2-1 and r2-2 verbatim-class; r2-3 via its own contingent
phrasing, adoption justified by the marker).

Label state after r3: UNCHANGED, as the r2 refuter's impact line
predicted — CLG-D2 THEOREM* under H1-H4+H6+H7 (u-linear form
conditional on q = 1, H7 sufficient, E3-adjudicated; c's dependence
now printed coherently with what the proof absorbs); CLG-D5 THEOREM*
(cross-lowering branch) / SCHEMA-conditional-H8 (same-lowering leg);
CLG-D6 SCHEMA conditional on H8; CLG-D1/D3/D4/D7 SCHEMA; CLG-D4-ALT
CONJECTURE. No grade moves; statements now self-consistent. No
measurement produced; no new arithmetic (probe unchanged, recorded
ALL-PASS stands). Files written this window: this file only
(in-place, markers [ESC-r3-0..3]). PAPERS NEEDED: unchanged (Higham
2ed, THEOREM*->THEOREM upgrade path only; r2 refuter's PAPERS NEEDED
was empty).
