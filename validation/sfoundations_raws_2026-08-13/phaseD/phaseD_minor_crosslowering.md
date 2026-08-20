# PHASE D MINOR (d) — CROSS-LOWERING GRADIENT FLOOR: FORMAL
# DERIVATION OF THE CHAIN AMPLIFICATION FACTOR (derivable part)
# S-FOUNDATIONS-C4 Blocco 1, 2026-08-20. Author slot per
# BRIEF_blocco2_phaseD.md MINORS (d). ONE refuter round + escalation.
# ID prefix: CLG-. Status: DRAFT (pre-refutation).

## 0. MANDATE AND INPUTS OF RECORD

Mandate row: `docs/findings_registry.yaml` id
`engine:cross-lowering-gradient-floor` (:328-336, read IN FULL).
Scope of this minor = the THEORY HALF ONLY: the formal derivation of
the chain amplification factor — how a per-operation roundoff of
size u ≈ 1.1e-16 becomes a ~1e-8 relative cross-lowering floor on
the adjoint gradient through ~250 implicit 4x4 solves, and how FD
consumers amplify that floor ~7 further orders into H. The three
named scaling experiments (N-ladder, margin-proximity, float32
contrast) are the MEASURED half = F2 duty, named in §6. The B-SHAPE
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
there. Boundary with both is named in §6 (no collisions clause).

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
  Checkable by inspection of the VJP code
  (validation/a1_toc_variational_jax.py:1697-1720 and the
  a1_ideal_march_jax defvjp).
- **H3** (conditioning): the linearized systems are uniformly
  invertible on the admissible design set: kappa(A_k) <= kappa-bar
  < inf. Checkable per design from recorded Jacobians.
- **H4** (transport): the adjoint transport is uniformly bounded:
  G := max_k ||T_N T_{N-1} ... T_{k+1}|| < inf (no exponential
  blowup along the chain). Checkable from recorded lambda growth
  along one sweep.
- **H5** (RMS refinement ONLY; declared PRACTICE, not proved):
  cross-lowering per-stage rounding-difference injections behave as
  independent, zero-mean across k. The N-ladder experiment (§6)
  decides it; nothing below except CLG-D3 uses it.
- **H6** (lowering equivalence): both lowerings compute the same
  real-arithmetic function; they differ only within the B-SHAPE
  equivalence classes. INPUT of record (findings :335).

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

**Statement (THEOREM*).** Under H1-H4, H6, there is a constant c
depending only on the per-stage kernel shape (c <= a small multiple
of m-bar via the standard gamma_m = m·u/(1−m·u) reassociation
bound) such that, to first order in u, for any two lowerings L, L':

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
QED (sketch).

**Why THEOREM\* and not THEOREM:** the constants are not tracked at
Higham grade (per-op inventory of the actual compiled kernels, FMA
contraction cases, reduction-tree shapes); H3/H4 are assumed
uniform rather than derived from the march equations. Upgrading to
THEOREM needs the constant-grade rounding analysis reference (see
PAPERS NEEDED) plus measured kappa-bar and G — the latter are
exactly two of the F2 identification targets (§6).

**Consistency with record (derived arithmetic from carried
numbers, shown):** Phi_chain(measured) = 1.45e-8 / 1.11e-16 ≈
1.3e8. With N = 250: the bound requires c · kappa-bar · G >=
1.3e8 / 250 ≈ 5.2e5 at the linear-in-N reading. Near-sonic /
marginal-cell 4x4 conditioning of order 1e3-1e5 times transport of
order 1e1-1e3 covers this range without strain — the law is
CONSISTENT with the measured floor, but the current record CANNOT
separate kappa-bar from G from the N-exponent (see CLG-D7).

**Falsifier:** once kappa-bar and G are measured (F2, §6), a
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
N-ladder decides between D2-linear and D3-sqrt (see §6, prediction
P1).

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
float32 contrast (§6, prediction P3) discriminates D2/D3 (q = 1 in
u^q) from D4-ALT (q ≈ 1/2 through the sqrt(u)-class Newton floor)
— this is exactly why the float32 experiment is load-bearing.

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
- SAME-lowering pair (one executable, one batch shape, per B-SHAPE):
  the systematic component b_L is common-mode and cancels to first
  order in the difference (CLG-D1 decomposition), leaving the
  sub-leading eta_L residue — the mechanism by which the sequential
  FD Hessian works and the corrected in-batch-base M6 form meets its
  derived bound K_RICH x max(scheme asyms) (findings :322, of
  record; that bound formulation is the acceptance authority, not
  re-derived here).

**Consistency with record (derived arithmetic from carried numbers,
shown):** measured mixed-lowering contamination dH = 18% rel at
floor phi = 1.45e-8 rel gives A_FD(implied) = 0.18 / 1.45e-8 ≈
1.2e7 = 10^7.1 — i.e. "~7 orders" exactly as carried by the row
(findings :322). The h-value and H_sc identification inside A_FD
are FD-step territory OWNED by F2-C44-FDSTEP (VERDICT_wave3
:612-620); this minor states the law and consumes the measured
consistency, it does NOT adjudicate step choice. No collision.

**Why THEOREM\*:** the bound form is textbook-grade (N-W §8.1 read
[FULL] at the cited pages) but transplanted onto a noise source
(cross-lowering bias) that is deterministic-systematic rather than
the i.i.d.-roundoff of the textbook model; the transplant step is
the un-hardened link (R-4 discipline: transplant DECLARED).

**Falsifier:** with phi measured on a lowering pair and (h, H_sc)
pinned by the consumer, a measured dH outside the K_RICH-band
around A_FD · phi falsifies the law (either a missing noise channel
or a wrong cancellation claim).

## 7. CLG-D6 — COROLLARY: PINNING DISCIPLINE IS THE ZERO-COST
## MITIGATION (consistency statement, not new policy)

**Statement (SCHEMA, corollary of D1+D5).** At floor phi, any
gradient COMPARISON or FD stencil across lowerings incurs
irreducible noise >= phi · g_sc (D1), FD-amplified by A_FD (D5);
within one lowering the systematic part cancels to first order.
Hence the standing discipline of record — "every gradient
COMPARISON or FD stencil pins ONE lowering" (findings :335;
VERDICT_wave2 RC31T-2 pin: cross-lowering pairs REJECTED at update
time) — is derived here as the unique zero-cost mitigation, not
merely an empirical rule. This corollary ADDS no policy; it gives
the registered discipline its formal footing.

**Falsifier:** inherits D1's (bitwise determinism) and D5's
(cancellation) falsifiers.

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
  i.e. phi32 ≈ 3e-4 — seven decades of separation between the two
  predictions: an unambiguous discriminator.

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

- Adoptable statements: CLG-D2 (THEOREM*), CLG-D5 (THEOREM*),
  CLG-D1/D3/D4/D6/D7 (SCHEMA), CLG-D4-ALT (CONJECTURE). Proposed
  M0 site: the engine-discipline block adjacent to the
  same-lowering standing rule; registry row
  `engine:cross-lowering-gradient-floor` owner field gains "formal
  derivation LANDED (chain law THEOREM*, FD law THEOREM*);
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

## PAPERS NEEDED

- Higham, "Accuracy and Stability of Numerical Algorithms" 2ed
  (SIAM 2002) — NOT on disk. Needed ONLY for the THEOREM*->THEOREM
  upgrade of CLG-D2 (constant-grade gamma_m reassociation bounds and
  backward-stability constants for small direct solves). The minor
  stands at THEOREM* without it.

## PAPERS CONSULTED (read-depth honesty)

- literature/nocedal_wright_2006_numerical_optimization_2ed.pdf —
  [FULL] on §8.1 error-model portion, book pp. 194-199 (PDF
  213-218); used for eq. (8.5)-class bound and optimal-step
  structure in CLG-D5.
- literature/giles_pierce_1997_adjoint_equations_cfd_aiaa97_1850.pdf
  — NOT consulted (not needed for this minor; it is the R27/T-RED
  leg, other slot's duty).
- Registry/verdict carriers read [FULL] at cited lines:
  docs/findings_registry.yaml :319-336;
  validation/PROGRESS_2026-08-12_S25bis_speed.md STEP 13 (:362-399);
  VERDICT_wave2.md :40-64, :200-223; VERDICT_wave3.md :605-620.
