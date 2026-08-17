# ADVERSARIAL REFUTATION — Round 2, lens 1 (gas-dynamics physics)

**Target**: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md` (REVISED r1, 2026-08-17),
read in full (1171 lines).
**Lens**: shock kinematics, unstart phenomenology, the M_s > M_x derivation, gamma(T) validity.
**Round-2 discipline**: only objections NOT in the r1-consumed list (O-1..O-12, N-list, O1..O11
P1-P3) count. Every objection below is checked against that list and its dedup relation declared.
**Rigor of this document**: each objection states target, quoted claim, defect with rigor class of
the counter-claim (complete proof / sketch / modeling assertion), a rejecting test, and the
minimal repair.

---

## Part A — Verification audit trail (attacks attempted that FAILED; the r1 repairs that hold)

Declared per the doubts-to-convergence standard: these are branches I tried to kill and could not.
They are listed so the round-2 verdict is measured against real resistance, not selective attack.

- **3b(i) localization algebra (the r1 repair of O-1/O2)**: at T_2 = Pi T_1,
  R T_2/p_2 = R T_1/p_1 = 1/rho_1, so the bracket is 2/rho_1 and
  phi(Pi T_1) = Int_{T_1}^{Pi T_1} c_p dt − R T_1 (Pi−1) = Int_{T_1}^{Pi T_1} c_v dt
  ≥ c_v,min T_1 (Pi−1) > 0. Endpoint signs, IVT, compressivity T_2 < Pi T_1 ⇔ rho_2 > rho_1,
  and the reconstruction v_1 = +sqrt all check. **HOLDS.**
- **3b(ii) sharpening**: rho_1/rho_2 = T_2/(Pi T_1) > 1/Pi ⇒ 1 − rho_1/rho_2 < (Pi−1)/Pi ⇒
  M_s^2 = (Pi−1)/[gamma_1 (1 − rho_1/rho_2)] > Pi/gamma_1. **HOLDS.**
- **Lemma 3.1**: (dc^2/drho)_s = R^2 T (gamma + T gamma')/(rho c_v) via
  (dT/drho)_s = RT/(rho c_v); Gamma_fund = (gamma+1)/2 + (gamma−1) T gamma'/(2 gamma); the
  failure boundary T gamma' = −gamma(gamma+1)/(gamma−1). **Exact; HOLDS.**
- **Gamma-const anchor**: M_s^2 = 1 + (gamma+1)/(2 gamma)(Pi−1) inverts the standard
  Pi(M_s) relation; gamma = 1.4, M_x = 2 gives Pi* = 4.5 < gamma_1 M_x^2 = 5.6; at Pi* the
  identity returns M_s = 2. General band Pi* < gamma_1 M_x^2 follows from the sharpening at the
  crossing. **HOLDS.**
- **(BQ) and Lemma 1.2**: <S A(n)U,U> = (u.n)<SU,U> + 2 p'(u'.n) by direct block multiplication;
  the similarity/definiteness argument S A(n) ≥ delta S. **HOLDS.**
- **Lemma 2.2(c) r1 upgrades**: the no-resonance argument (u.xi = 0 forces the Mach factor to
  −c^2|xi|^2 < 0) and the symmetric-definite pencil (S A_eta) w = −xi_x (S A_1) w with
  S A_1 ≥ (u_x−c) s_min I > 0; discriminant identity
  c^2[(u_perp.eta)^2 + (u_x^2−c^2)|eta|^2] and its meridional restriction
  c^2 xi_r^2 (u_x^2+u_r^2−c^2) (Remark 2.4). **HOLD.**
- **Corollary 4 r1 rebuild**: the closure algebra p' = Z u'_x ⇔ R_- = r R_+ with
  r = (Z−rho_0 c_0)/(Z+rho_0 c_0) is exact WITH mean flow (the mean flow enters the transport
  speeds, not the ratio); the no-reflection-loop explicit construction for every finite r; the
  quadrant (d) non-uniqueness witness (R_+ family free at r = 0 under outgoing-invariant
  prescription). **HOLD.** The r0 retraction is correct.
- **3.3 admissibility/kinematics**: the constructed front is a Lax 1-family (upstream-facing)
  shock in the front frame (v_1 > c_1 entering, 0 < v_2 < c_2 leaving; all other characteristic
  speeds one-signed); with continuous tangential velocity the normal RH system is unaffected by
  swirl at the interface state. Upstream of a downstream-washing front the state stays exactly
  W_1 (no precursor in the inviscid uniform class). **HOLDS.**

---

## Part B — NEW objections (round 2)

### R2-1 (P1) HYPOTHESIS SUPPLY-CHAIN BREAK: the r1 normal-form certificate no longer feeds Theorem 2's (H2.2) or Theorem 3's M_x — and never fed the volumetric clause at all

**Target**: Section 5 composite ("causal separation R1 holds BY THEOREM for ... (ii) the steady
per-phase class"), 3.4(3)(a) ("the certificate delivers the HYPOTHESES of Theorems 1-2"),
monitor list (M-a), Theorem 2 (H2.2), Theorem 3 setup (M_x ≥ 1 + delta/c_1).
**Dedup**: NOT in the prior list. O-6/NG-8 attacked the axial-on-tilted-patch reading of
Theorem 1's (H1.3) and were repaired by moving the certificate to the NORMAL form. This objection
is the CONVERSE and the VOLUME direction: the repair broke the other two consumers.

**Defect (complete argument):**

1. *Normal vs axial, converse direction.* On a tilted patch (n_I not parallel to e_1), the r1
   certificate u.n_I − c ≥ delta does NOT imply u_x − c ≥ delta: write
   u_x = u.n_I n_{I,x} + (tangential contribution); for n_{I,x} < 1 there are states with
   u.n_I − c = delta and u_x < c (e.g., u exactly along n_I with |u| = c + delta and
   n_{I,x} ≤ c/(c+delta) gives u_x = (c+delta) n_{I,x} ≤ c). This is precisely O-6's tilt
   geometry run in reverse. Consequences:
   - Theorem 2's hypothesis (H2.2) is the AXIAL margin u_x − c ≥ delta; the composite's clause
     (ii) states it holds "on the L4 default read in the NORMAL form". As written the
     BY-THEOREM claim consumes a hypothesis the certificate no longer certifies.
   - Theorem 3's entire pricing is anchored on the AXIAL Mach M_x = u_1/c_1 of the pre-state
     ("L4 margin M_x ≥ 1 + delta/c_1"): under the normal-form certificate on a tilted patch,
     M_x ≥ 1 + delta/c_1 is unproved, so Pi*(M_x) in monitors (M-b) and register row 3d is
     priced off a quantity the standing certificate does not bound.
2. *Surface vs volume (present already in r0, never raised).* (H2.2) demands the margin on the
   VOLUME Omega_{[x_0, x_I]} ("not only on the slab", the document's own emphasis at line
   ~569). The certificate of record — (M-a), "u.n_I − c ≥ delta per phase ON Gamma_d" — is a
   SURFACE statement. No monitor in 3.4(3) checks the duct-segment margin, yet 3.4(3)(a) claims
   the certificate delivers "the HYPOTHESES of Theorems 1-2" and Section 5 claims steady
   per-phase R1 BY THEOREM. A per-phase field satisfying the interface-surface margin with an
   embedded subsonic pocket at x_0 < x < x_I (locally u_x < c away from Gamma_d — e.g., a
   residual hot spot; nothing in the L4-DEFAULT excludes it) satisfies every monitored condition
   while (H2.2) fails and Theorem 2(b)'s Gronwall-in-x argument dies (the document itself notes
   the argument "dies at delta = 0").

**Rigor class of the objection**: complete proof (the tilt counter-state is explicit; the
surface-vs-volume gap is a quantifier comparison between the certificate text and (H2.2)).

**Rejecting test (for the objection itself)**: exhibit either (i) a planarity + full-segment
margin pin in M0 [D-CONTRACT] making the three hypothesis forms equivalent on the certified
class (the document itself reports NO planarity pin was found — line ~80), or (ii) a proof that
u.n_I − c ≥ delta on Gamma_d implies u_x − c ≥ delta' > 0 on Omega_{[x_0,x_I]} for the
per-phase class. Either kills this objection; neither is in the document.

**Repair (minimal)**: split the certificate: (M-a) normal margin on Gamma_d (feeds Theorem 1);
new (M-a') axial margin u_x − c ≥ delta on the duct segment per phase (feeds Theorem 2 and
supplies M_x ≥ 1 + delta/c_1 at the interface for Theorem 3's pricing); Section 5 clause (ii)
and 3.4(3)(a) restated to consume (M-a') explicitly; NG-8 extended to carry BOTH wording deltas
to M0. On planar patches with a segment-wide certificate the two collapse and nothing changes —
the repair is scoping, not new mathematics.

---

### R2-2 (P2) MONITOR ANCHORING: (M-b) compares the wrong physical quantity, with unproven conservatism direction and undefined per-phase/pointwise anchoring

**Target**: 3.4(3) (M-b); Section 5 ("prices the excluded normal-front band Pi < min(Pi*,
Pi_box) with alarm-on-approach").
**Dedup**: O10(a) raised the 3-wave-fan mis-anchoring FOR THE FALSIFIER HARNESS and was repaired
there (exact RH-pair initialization / measure Pi_left). The OPERATIONAL MONITOR (M-b) — the
object actually consumed by the program — carries the same defect and was not repaired: new
target, new consequence.

**Defect:**

1. *Wrong quantity.* Theorem 3 prices the strength Pi = p_2/p_1 OF THE FRONT at the interface.
   (M-b) monitors "downstream overpressure below the priced band edge min(Pi*, Pi_box) p_1". A
   downstream overpressure event of ratio Pi_d resolves (the document's own O10(a) physics) into
   a wave fan whose upstream-running shock has strength Pi_left ≠ Pi_d, further modified by
   propagation through the NONUNIFORM downstream field (steady nozzle gradients strengthen or
   weaken a front between the measurement station and Gamma_d). The document proves no
   inequality Pi_left ≤ Pi_d for this configuration, so even the CONSERVATISM DIRECTION of the
   monitor is unestablished: a green (M-b) does not certify that no front of strength > Pi*
   reaches Gamma_d, and the composite's "prices the excluded normal-front band" overstates what
   the monitor checks. (Modeling assertion, one derivation short of a theorem: for the
   compression-fan resolution over a uniform state Pi_left < Pi_d is provable from wave-curve
   monotonicity under (G4) — but it is NOT in the document, and the nonuniform-propagation leg
   is genuinely open.)
2. *Undefined anchoring.* p_1, c_1, M_x, hence Pi*(M_x), Pi_T = T_max/T_1 and Pi_box are
   PER-PHASE, PER-PATCH fields on Gamma_d (the interface state of an RDE varies over the cycle
   by design — the document's own H-RW discussion). (M-b) uses the symbols as scalars. The
   honest monitor threshold is the pointwise-in-(patch, phase) minimum
   min_{xi, patch} [ min(Pi*(M_x), Pi_box) p_1 ]; unstated. Edge case also unstated: a patch
   with T_1 = T_max has Pi_T = 1, empty in-box band, and the monitor saturates at ZERO
   admissible overpressure — a reportable state distinct from band-edge saturation as defined.

**Rigor class**: sketch (item 1's missing inequality identified; item 2 is a
definition-completeness proof by inspection).
**Rejecting test**: produce the derivation Pi_arrival(Pi_d, downstream field) ≤ Pi_d (or a
priced correction factor) for the consumed configuration class, plus the per-phase minimum in
the monitor definition; that discharges the objection.
**Repair**: either monitor the front strength AT Gamma_d directly (measured Pi_left analog of
the r1 falsifier fix, promoted from harness to monitor), or add the missing one-sided
wave-curve inequality as a lemma (uniform-field class, THEOREM* under (G4)) plus a declared
PRACTICE clause for the nonuniform leg; state all thresholds as per-phase pointwise minima.

---

### R2-3 (P2) FAMILY/FACING OVERCLAIM in Theorem 3a's interpretation: "on a SUBSONIC stream every admissible front runs upstream" is false without the upstream-facing qualifier

**Target**: Section 3.2, interpretation paragraph after Theorem 3a.
**Dedup**: not in the prior list (O3(P1) is oblique geometry; this is wave-FAMILY scoping in the
1-D normal class itself).

**Defect (complete):** The claim chains "admissible fronts always have M_s > 1 (Lax)" into "on a
SUBSONIC stream (M_x < 1) every admissible front runs upstream". The Lax bound v_1 > c_1, i.e.
M_s := v_1/c_1 > 1, holds for fronts of the UPSTREAM-FACING acoustic family — those whose
pre-shock state is the stream state 1 with v_1 = u_1 − U_s > 0. The admissible-front class over
the same stream also contains the DOWNSTREAM-FACING family (pre-shock side downstream of the
front, v_1 < 0): e.g., a compression born upstream overtaking the flow — a blast front running
downstream into the subsonic stream at U_s = u_1 + M_s' c_1 > 0. For that family the document's
own definition gives M_s = (u_1 − U_s)/c_1 = −M_s' < −1, not "> 1", and the front runs
DOWNSTREAM on the subsonic stream. So the quoted sentence is false as stated; the whole of
Section 3 silently works in the upstream-facing family (correctly so — it is the only family
relevant to upstream invasion), but the restriction is never declared, and the class U(delta)
("downstream transients whose induced front strength exceeds Pi*") inherits it invisibly: a
downstream transient also induces downstream-facing and contact waves to which Pi* pricing does
not apply and need not.

**Rigor class**: complete proof (explicit counterexample family).
**Rejecting test**: a 1-D run with a downstream-running admissible blast front over a subsonic
stream — the front's lab speed is positive, refuting the sentence read literally.
**Repair**: one sentence — restrict the interpretation and the U(delta) definition to fronts of
the upstream-facing family (pre-state = the stream state), which is also the family Theorem
3b(i) constructs (v_1 = +sqrt chosen). No mathematics changes; the label "THEOREM (complete)"
on 3a is retained, the INTERPRETATION paragraph is the defect.

---

### R2-4 (P3) NG-7 INTERIM CONTROL IS MODE-MISMATCHED: an unsteady subsonic column does not exercise a steady marching stencil

**Target**: Theorem 2 falsifier (ii), r1 interim-control clause; NG-7 row.
**Dedup**: O10(c) raised vacuousness of the missing subsonic control; r1 answered with the
interim synthetic column. Attacking the ADEQUACY of that interim answer is new.

**Defect:** The falsifier's probe targets a specific failure mode of a STEADY x-marching code:
the marching stencil reading downstream memory (exit-plane array slots). The proposed interim
control — "a synthetic 1-D subsonic column per the explicit model of Corollary 4" — is an
UNSTEADY IBVP integrated in time: its upstream sensitivity to exit perturbations arises from the
physical upstream characteristic (u_0 − c_0 < 0) resolved by the time-stepper, not from any
x-marching stencil read. It therefore exercises a DIFFERENT code path and a different failure
mode; a marching implementation that silently reads downstream memory would not be flagged by
the column run, and the clause "which exercises the same stencil-reads-downstream failure mode"
is unsupported. The control is a placebo for the stated mode.
**Rigor class**: complete argument at the level of code-path analysis (modeling assertion about
the pipeline, checkable by inspection of the two harness designs).
**Rejecting test**: instrument a deliberately-broken steady marcher (stencil reads one
downstream slot); PASS of the objection iff the column control fails to flag it while the
steady-BVP control below does.
**Repair**: the honest interim control is a minimal STEADY subsonic 1-D duct BVP solve (the
steady limit of the Corollary 4 model with area variation; a two-point BVP in the pinned env),
whose steady solution genuinely depends on the exit closure — a marching probe on IT must show
O(1) sensitivity. Rewrite the NG-7 interim clause accordingly.

---

### R2-5 (P3, minor bundle — each independently checkable)

**Dedup**: none of these appear in the r1-consumed lists.

(a) *Undefined symbol in a THEOREM proof*: Theorem 2(b)'s comparison display uses lambda_A
    ("<S_x U, U> ≤ s_max lambda_A |U|^2") with lambda_A never defined (intended: an upper bound
    on spec A_1, i.e., u_x + c ≤ lambda_A from the (G3) box + base-state bound). One line.
    Rejecting test: grep for a definition of lambda_A — absent.
(b) *Asserted Kreiss clause inside a THEOREM block*: Corollary 4(i)'s "the incoming condition
    R_- = r R_+ satisfies the 1-D Kreiss condition uniformly for every finite r" is load-bearing
    for the Hadamard claim but is asserted, not computed (the one-line Lopatinskii determinant
    for the decoupled transport pair is trivial and should be displayed, or the clause dropped —
    the explicit-construction proof already suffices without invoking Kreiss).
(c) *Internal wording tension in 3.4(3)*: clause (a) says the certificate delivers "the
    HYPOTHESES of Theorems 1-2" while (M-c) two lines later says (H1.1) "the margin certificate
    does NOT certify". Section 5 carries the correct "MODULO (H-RW), (M-c)" hedge; 3.4(3)(a)
    must carry it too (and, post R2-1, also the (M-a') hedge).
(d) *gamma_1 undefined*: 3b(ii) and everything downstream use gamma_1 without defining
    gamma_1 := gamma(T_1) (the r1 register fixed u_x > 0 in row 2a but not this).
(e) *Empty-band edge case*: Pi_T = T_max/T_1 ≤ 1 when T_1 → T_max (hot interface phases): the
    in-box band (1, Pi_T] is empty and 3b(i) is vacuous there; the band-edge-saturation state of
    3b(iii) should name this degenerate sub-case (monitor semantics: zero certified overpressure
    headroom at such phases). Feeds R2-2's per-phase anchoring.

**Rigor class**: complete by inspection (each).
**Repair**: five one-liners plus the (e) monitor sub-state.

---

## Part C — Verdict (round 2, this lens)

The r1 revision genuinely consumed round 1: the repaired proofs (3b(i) localization, Lemma
2.2(c) pencil, Corollary 4 rebuild, falsifier predicates) survive direct re-derivation — Part A.
The core mathematics of Theorems 1, 2(a)-(b), 3a, 3b(i)-(ii) and Corollary 4 is sound as
labeled. What does NOT survive is the COMPOSITE as stated: the r1 normal-form repair of O-6
broke the certificate-to-hypothesis supply chain for Theorem 2 and Theorem 3's pricing (R2-1,
P1 — the single genuinely structural find), the operational monitor (M-b) still anchors on an
unpriced quantity (R2-2), and one interpretation sentence in Section 3.2 is false without a
family qualifier (R2-3). All are repairable by scoping, one new monitor clause, one lemma-or-
PRACTICE declaration, and one sentence — no theorem falls.

**VERDICT: REPAIRABLE** (composite overclaims in Section 5 / 3.4(3)(a) pending R2-1's split
certificate; no core statement broken).
