# ADVERSARIAL REFUTATION — SWIRL-2D formalization, ROUND 4 on disk
# (orchestrator round label: "Round 2"), lens l0
# (functional-analytic rigor: spaces, operators, compactness, traces,
#  every quantifier)

TARGET: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
AT REVISION r2 (2026-08-17 10:22, 1413 lines — read in full).

ORCHESTRATION STATE NOTE (measured in-window, SR-12; not inherited).
The launch brief said "Round 2 ... write to refute_SWIRL-2D_r2_l0.md".
That instruction is STALE against the on-disk state, measured this
window (Get-ChildItem, sorted by mtime):
  refute_SWIRL-2D_r1_l0.md  08:09  (O1–O12, absorbed at r1, cited §6-bis)
  refute_SWIRL-2D_r1_l1.md  08:13  (O-1..O-9, absorbed at r1, cited)
  refute_SWIRL-2D_r2_l0.md  08:37  (N1–N9 vs r1 — ON FILE, see R4-0)
  refute_SWIRL-2D_r2_l1.md  10:13  (N-1..N-6 vs r1 — absorbed at r2)
  refute_SWIRL-2D_r3_l0.md  10:13  (R3-1..R3-7b vs r1 — absorbed at r2)
  target revised to r2      10:22
Overwriting `r2_l0` would destroy an of-record refutation that no
ledger has yet consumed (provenance corruption, prohibited); `r3_l0`
is likewise taken. This deliverable is therefore filed as ROUND 4,
lens l0, per the precedent set inside this same loop by the state
notes of `r2_l1` and `r3_l0`.

GROUND RULES OF THIS ROUND. (1) The thirteen absorbed objections
(R3-1..R3-7b, N-1..N-6) are not repeated; every attack below targets
either the r2 repairs themselves or axes untouched by any prior
round. (2) The nine PENDING objections of `r2_l0` (N1–N9, raised
against r1, only partially coincident with the absorbed list) are
also not repeated: one candidate finding of this round (D.20's front
clause false on wave-frame contacts) was independently re-derived
here and then found to DUPLICATE pending N3 — it is dropped from the
new list and noted only inside R4-0. (3) Every objection states the
attacked label, the defect, a counterexample or failure scenario in
the declared class, and the minimal repair.

------------------------------------------------------------------------------
## R4-0 [MED — audit-integrity / nothing-lost, not a theorem defect]
## The r2 revision header and §6-ter coexist with an on-file,
## uncited, unabsorbed nine-objection refutation (`r2_l0`, N1–N9);
## the doc's own ledgers never mention the file

STATEMENT ATTACKED: REVISION r2 header ("the ROUND-2 objection list
(R3-1..R3-7b, N-1..N-6) ... APPLIED IN PLACE ... All thirteen
objections were fixable at full rigor in-document") and §6-ter's
closing line ("Unfixed residue this round: NONE new").

THE DEFECT. Both sentences are true RELATIVE TO their list, but the
list is not the round-2 record on disk: `refute_SWIRL-2D_r2_l0.md`
(08:37, targeting r1, nine objections N1–N9, four label-threatening
by its own verdict) is cited by NO disposition ledger in the target.
Cross-checking its content against the r2 text, measured this
window: N1 landed (coincides with absorbed N-1, H-WR), N9(b) and
N9(d) landed (coincide with absorbed N-6), but N2 (D.4/D.13(c)
curved-interface spacelikeness — the one objection able to LICENSE
an ill-posed march), N3 (D.20 rothalpy front clause false on
wave-frame contacts), N4 (S.22 g2a weak-vs-weak), N5 (D.14
licensing sensitivity is a functional, not a constant), N6 (H-AM0
quadrature audit is a non-rejector), N7 (H-FIB "equivalently" +
reachability), N8 (D.18 K_h0 printed prefactor Ω·w_rel — still on
the r2 text at the "K_h0 adds nothing new" line, correct prefactor
w·w_rel/r), and N9(a,c,e,f) are ALL still present in the r2 text,
unrepaired and unregistered. A reader of §6-bis + §6-ter alone
would conclude the refutation record is fully consumed — false.

REPAIR: add a §6-ter-bis ledger consuming N1–N9 (dispositions:
three "already-landed-via-coincidence" rows + the pending rows with
owner), or fold them into the next revision; the absorption pass
(§7) MUST NOT run before this file is consumed — the nothing-lost
gate would pass on a lie otherwise.

------------------------------------------------------------------------------
## R4-1 [MED-HIGH] — D.18: BOTH iffs of the equivalence clause lack a
## front clause and are FALSE on the declared class; K is read as a
## smooth-region object in D.18 and as a measure with front atoms in
## S.22 — the same symbol, two inequivalent readings in one document

STATEMENT ATTACKED: D.18 [MS-DEF-KRES] equivalence clause: first iff
"The per-phase family solves the exact 3-D wave-frame system iff
K ≡ 0 (bookkeeping)"; second iff "K ≡ 0 iff ∂_φ(fields) ≡ 0
(degenerate axisymmetric operation)", classed "THEOREM under
H-NC + H-WR"; and the definition's silent reading of K via classical
∂_φ in smooth regions.

THE DEFECT (quantifier/domain-of-definition). The six K rows are
built from classical ∂_φ derivatives, defined only on the open
complement of the front set; the r2-completed proof of the second
iff operates entirely there ("continuity of ∂_φρ off fronts").
But §0 declares the 3-D wave-frame class WITH fronts: "finitely
many C¹ hypersurfaces steady in φ (both types admitted)" — i.e.
fixed hypersurfaces in (x, r, φ)-space, generically with NONZERO
azimuthal normal component n_φ (the detonation front itself is the
in-scope instance; S.22's r2 text says so verbatim: "any front with
nonzero azimuthal normal component (the detonation front itself,
the in-scope object)"). On that class the smooth-region reading
makes BOTH iffs false, in both directions:

COUNTEREXAMPLE (piecewise-constant helical front; in-class). Take
two constant states V± satisfying the full 3-D RH conditions across
a C¹ wave-steady front hypersurface with normal n = (n_x, 0, n_φ),
n_φ ≠ 0 (an oblique front — locally realizable for mass-crossing
data; states constant on each side). Then:
 (a) All six K rows vanish IDENTICALLY in smooth regions (every
     ∂_φ of the fields is zero off the front). K ≡ 0 in D.18's
     reading.
 (b) The azimuthal sections V(·;ξ) := V₃D(·,·,φ(ξ)) do NOT solve
     the per-phase 2.5-D system of D.1: each section carries a
     meridional front curve whose 2.5-D RH conditions are the
     x/r-NORMAL jump relations, while the states jump by the
     OBLIQUE relations (which involve the ρ w_rel n_φ mass and
     momentum fluxes through the front). Generic oblique RH data
     violate the meridional RH. So "K ≡ 0" does not imply "the
     per-phase family solves" in any reading of the first iff —
     the bookkeeping identity exact = 2.5-D + K simply has NO
     front component, and the difference between the two systems
     at fronts is invisible to the K list.
 (c) Conversely, a per-phase family in which each section solves
     the 2.5-D system exactly (say a family of meridional normal
     shocks whose STANDOFF LOCATION x_s(ξ) varies with phase,
     constant states on both sides) has K ≡ 0 in smooth regions
     yet, read as a 3-D field via ξ ↔ φ, does NOT solve the exact
     3-D system: the front surface x = x_s(φ) has n_φ ≠ 0 and the
     3-D RH across it are violated by data that only satisfy the
     x-normal relations. First iff false in this direction too.
 (d) Second iff: in example (a)/(c), ∂_φ(fields) ≡ 0 in smooth
     regions, so the biconditional's two sides are formally both
     "true" — but the parenthetical conclusion "degenerate
     AXISYMMETRIC operation" is FALSE: the front is helical, the
     operation is genuinely three-dimensional and unsteady at
     every fixed lab point. The THEOREM as worded proves
     φ-independence of the fields OFF fronts, which on the
     declared front-carrying class does not imply axisymmetric
     operation. Under the alternative (distributional) reading,
     ∂_φ fields ≢ 0 (jump atoms on the front) while D.18's K, as
     defined, is still ≡ 0 — the iff is then false outright.

INTERNAL INCONSISTENCY (r2-created). S.22's r2 repair now treats K
as "a MEASURE with an atom on the front" (that was the whole
content of absorbed objection R3-2), while D.18 — the DEFINITION of
record for the same symbol — still defines K by classical ∂_φ off
fronts and proves its equivalence clause in that reading. One
symbol, two inequivalent objects: the document's §5 does not
type-check against its own §S.22.

REPAIR (moderate, names itself). Define K DISTRIBUTIONALLY on
D × S¹_φ: the six rows as distributions, whose absolutely
continuous part is the displayed smooth-region formulas and whose
singular part is supported on the front set with density
n_φ · (the 3-D RH residual of the meridional-RH-matched jump) —
exactly the atoms S.22 already prices in its split-norm candidate.
Then: first iff becomes TRUE as bookkeeping (the front atom IS the
front-level difference of the two systems — state and prove the
one-line jump computation); second iff: K ≡ 0 as a measure kills
both the smooth ∂_φ content AND φ-dependent front geometry, making
"degenerate axisymmetric operation" correct (the H-NC + H-WR proof
covers the a.c. part; add one paragraph for the atom part: zero
atom + n_φ ≠ 0 somewhere forces zero jump or meridional front).
Extend the G-f rejector spec with a FRONT instance: the
helical-normal-shock family of (c) must FAIL K ≡ 0 under the
distributional reading and PASSES under the current smooth-region
reading — a one-instance check that cleanly separates the two
readings and would have caught this objection at authoring.

------------------------------------------------------------------------------
## R4-2 [MED] — D.2 (r2 repair adequacy): H-CVX as minted — "G_fund > 0
## on the states crossed" — is insufficient for finite-amplitude Lax
## fronts; entropy monotonicity needs convexity along the CONNECTING
## HUGONIOT ARC (+ Hugoniot well-definedness), and the clause's own
## falsifier already fires on the as-minted reading

STATEMENT ATTACKED: D.2, r2-minted hypothesis "(H-CVX, r2)
Bethe–Weyl convexity of the EOS: fundamental derivative
G_fund := 1 + ρ(∂c/∂ρ)_s/c > 0 on the states crossed", supporting
the clause "s jumps upward across a compressive Lax front UNDER
H-CVX", gamma status "EOS-general GIVEN H-CVX".

THE DEFECT (hypothesis completeness inside the round-2 repair). "On
the states crossed" reads as: at the two end states of the jump (a
discontinuity has no intermediate states). That is NOT the
Bethe–Weyl hypothesis. The classical sufficient condition for
"compressive Lax front ⟹ [s] > 0" at finite amplitude is G_fund > 0
along the HUGONIOT LOCUS connecting the states (entropy varies
along the Hugoniot with sign controlled by G at the RUNNING state;
Bethe 1942 assumes convexity everywhere plus the subsidiary
Grüneisen condition Γ_G > −2 for global single-valuedness of the
Hugoniot; Menikoff–Plohr Rev. Mod. Phys. 61 (1989) is the of-record
treatment). With G > 0 at both END states but a non-convex arc in
between (the van der Waals / BZT configuration: end states in
convex regions straddling an anomalous G < 0 pocket), a single
discontinuity satisfying RH + the Lax inequalities can carry
[s] < 0 — this is precisely why Lax admissibility is superseded by
the Oleinik/Liu E-condition for non-genuinely-nonlinear fields: the
entropy-violating Lax front is the textbook object of that theory.
So under the endpoint reading, the clause "EOS-general GIVEN H-CVX"
remains an over-label — the SAME defect class R3-1 prosecuted, one
level deeper.

THE CLAUSE'S OWN FALSIFIER FIRES. D.2's r2 falsifier reads: "an
H-CVX-satisfying EOS instance with a Lax front carrying [s] < 0
(would refute the s-monotonicity clause under its stated
hypothesis)". Under the endpoint reading of H-CVX such an instance
EXISTS in the literature class above — the falsifier is not
hypothetical, it is discharged against the statement as worded.
(Falsifier power confirmed; statement wording refuted.)

WHAT SURVIVES UNTOUCHED. The γ(T)-EXACT discharge is UNAFFECTED and
actually completes the repair: the closed form
G_fund = 1 + (γ−1)(γ + Tγ′)/(2γ) > 1 holds under AUD-c2T + AUD-cp
at EVERY state of the table's range, hence on every Hugoniot arc
inside the operating range — the arc condition is free in-model.
Weak (small-amplitude) fronts are also fine EOS-generally with
endpoint G > 0 (the [s] ~ G·[v]³/T cubic law is local).

REPAIR (three lines): reword H-CVX to "G_fund > 0 on the Hugoniot
locus connecting the states (equivalently: the front's wave family
is genuinely nonlinear along the connecting arc), plus Hugoniot
well-definedness (Menikoff–Plohr weak conditions)"; note the
γ(T)-exact discharge covers the arc automatically; add to the
falsifier the BZT/composite-wave instance as the named
counterexample class for the endpoint misreading.

------------------------------------------------------------------------------
## R4-3 [MED] — H-AM2/D.6/D.8/D.16: the shear-declared limb budgets the
## WALL torque only; the cross-section (and S_inj) deviatoric-stress
## angular-momentum flux ∮_{S(x)} r τ_xθ dA is in NO hypothesis, no
## census channel, and no audit budget — the census exhaustiveness
## fails on interior-stress datasets with zero wall torque

STATEMENT ATTACKED: H-AM2 ("the wall stress is either zero ... or
its axial torque τ_w := ∮_{Σ_w} r (τ·n)_θ dA ... is DECLARED");
D.6's balance ⟨∮_{S(x)} ρ u_x Γ dA⟩ = J_inj + τ_w,decl(x) in the
shear-declared limb; D.8's exhaustiveness ("any breakage must
negate a hypothesis"); D.16's tol_AM derivation ("declared
shear/numerical torque budget bars (H-AM2)").

THE DEFECT (a boundary term dropped from the balance's own
divergence-theorem display). For a viscous (or turbulence-modeled,
or numerically diffusive) flow, the exact CV angular-momentum
balance carries the deviatoric-stress moment over ALL of ∂CV:
  ∮_{∂CV} r (τ·n)_θ dA = τ_w  +  ∮_{S(x₂)} r τ_xθ dA
                              −  ∮_{S(x₁)} r τ_xθ dA
                              +  (S_inj stress moment).
H-AM2 declares the Σ_w term ONLY. The station-plane terms
⟨∮_{S(x)} r τ_xθ dA⟩ — molecular, modeled-Reynolds/SGS, and
numerical-diffusion stress alike — are silently zero in D.6's
stated balance and in D.16's residual budget. FAILURE SCENARIO
(in-scope: D.16 exists precisely for dissipative chamber-CFD
ingestion): an LES/RANS dataset with free-slip or low-friction
walls (τ_w ≈ 0, correctly declared) but O(1) modeled τ_xθ on the
station planes — e.g. strong modeled shear between the swirling
core and outer flow — audits RED on R_AM with EVERY hypothesis
H-AM0..H-AM5 green as specified: the census exhaustiveness claim
("exhaustive over {¬H-AM0..¬H-AM5}") is false for this dataset —
the broken term negates no listed hypothesis, because no
hypothesis ever declared it. Conversely a dataset where the
plane-stress term partially cancels a wall torque can falsely PASS
against the wall-only budget: both rejector directions are
compromised at the tolerance edge. Note the resolved-fluctuation
covariance is NOT the issue (it lives inside ⟨ρ u_x Γ⟩ already);
this is strictly the modeled/molecular stress moment on the
non-wetted boundary portions, the piece the r1 "refuter extension"
(physical + turbulent + NUMERICAL shear) correctly flagged but
then booked under the WALL integral alone.

REPAIR (small and structural): extend H-AM2 to declare the FULL
deviatoric-stress angular-momentum flux through ∂CV — wall torque
τ_w plus per-station plane-stress moments T_S(x) :=
⟨∮_{S(x)} r τ_xθ dA⟩ and the S_inj moment; D.6's balance becomes
flux = J_inj + τ_w,decl(x) + [T_S(x) − T_S(inj-side)]; D.8 channel
(2) reworded "boundary deviatoric stress — wall AND cross-plane";
D.16's budget line adds the per-station declared plane-stress bar
(cheap: the ingested dataset's own stress field evaluated on the
plane). Inviscid limb untouched; EOS-FREE status untouched.

------------------------------------------------------------------------------
## R4-4 [LOW-MED] — D.2 r2 item (a): global single-valuedness of ψ on
## cl(D) is consumed, not proved — the Lipschitz argument bounds the
## GRADIENT but existence of a single-valued primitive needs (E1)
## weakly ACROSS fronts and vanishing periods on the holes of D
## (D is never assumed simply connected)

STATEMENT ATTACKED: D.2, r2-added clause "(a) ψ IS CONTINUOUS
ACROSS C, and across every front: dψ = ρ u r dr − ρ v r dx with
ρ, u, v ∈ L∞ (§0) makes ψ Lipschitz on cl(D), hence continuous
across any curve."

THE DEFECT (two consumed steps, one of them with a topological
hole). The argument establishes: IF a function ψ with the stated
a.e. differential exists on D, THEN it is Lipschitz (W^{1,∞} on a
bounded Lipschitz — hence quasiconvex — domain embeds in
C^{0,1}(cl(D)); the quasiconvexity step is silently used, fine).
It does NOT establish EXISTENCE of a single-valued ψ, which needs:
 (i) CLOSEDNESS ACROSS FRONTS: the 1-form ρur dr − ρvr dx must be
     closed DISTRIBUTIONALLY on D, i.e. (E1) must hold weakly
     across the front set. That is exactly the RH mass row — TRUE
     in-class, but nowhere invoked; without it, a mass-producing
     front would make ψ two-valued and the whole clause (a)
     collapses. One citation sentence fixes it.
 (ii) VANISHING PERIODS: §0 declares D only "bounded Lipschitz";
     simple connectivity is assumed for the THEOREM's region G but
     the r2 clause asserts ψ Lipschitz "on cl(D)". On a multiply
     connected D (a meridional section with an internal island —
     a strut or cooled-pylon cross-section is the realizable
     instance), a closed 1-form needs vanishing periods around
     each hole to admit a primitive: the period equals the net
     mass flux through any curve encircling the island, which
     vanishes BY wall impermeability (u·n = 0 on the island
     boundary) plus weak (E1) — again true in-class, again a
     one-line argument, again absent. As written, "makes ψ
     Lipschitz on cl(D)" is a non sequitur from the displayed
     differential alone.
REPAIR (three lines inside clause (a)): "single-valuedness of ψ on
cl(D): the form is closed distributionally by weak (E1) (RH mass
row across fronts), and its periods around any internal boundary
component vanish by impermeability + weak (E1); a primitive exists,
and W^{1,∞} on the quasiconvex Lipschitz domain gives the Lipschitz
bound." THEOREM label then stands.

------------------------------------------------------------------------------
## R4-5 [LOW] — discipline cluster (each item violates a rule the
## document itself declares; none threatens a core result)

(a) REMARK 3.1 still violates the preamble's every-statement rule
    IN BODY (the exact class N-4 fixed for R4.1 and D.8, missed
    here): it carries "Class: THEOREM" but NO gamma-status line and
    NO falsifier in the body; the register row's falsifier cell is
    "one-line proof" — a PROOF is not a falsifier (R5: tests must
    be able to REJECT). Fix: body lines "Gamma status: EOS-FREE.
    FALSIFIER: a strict-T0 dataset (T0-flatness green) on which
    L(t) = ∫_CV ρΓ dV varies beyond quadrature bars refutes the
    instantaneous form"; register cell updated to that test.
(b) D.6, idealized-class sentence: "the ... cycle mean of Γ
    vanishes exactly at EVERY station" — drops the a.e./admissible-
    station qualifier the r2 repair just installed two sentences
    upstream (at a parked-front station the assertion holds only
    for the one-sided limits). One word: "every admissible
    station".
(c) S.22, r2 candidate class: "PLUS a front term ... — or
    EQUIVALENTLY a measure/W^{−1,1}-grade norm on K with the
    LEFT-side distance weakened to match". The two candidates are
    NOT equivalent as norm topologies (a split strong-L¹-plus-atom
    functional vs a negative-order weak norm control different
    quantities even on the same K; the left-side weakening changes
    the THEOREM being targeted, not just the RHS). Inside a SCHEMA
    the pair is a legitimate fork of the design space, but
    "equivalently" asserts a false equivalence — write
    "alternatively", and note the fork is part of gap (g1). Also
    W^{−1,1} is a delicate space (measures do not embed in
    W^{−1,1} in general; they do in W^{−1,q} for q < d/(d−1)) —
    the schema should say "W^{−1,q}, q < d/(d−1), or a
    dual-Lipschitz/Kantorovich–Rubinstein norm" if it wants a
    named, well-defined target class.
(d) D.10, unconstrainedness exhibit: "u_θ = ±u₀ on EQUAL-MASS-FLUX
    halves — zero net Γ-flux". Equal mass flux (∫ρu_x dA matched)
    does NOT zero the Γ-flux ∮ρu_x r u_θ dA — the r-weighting
    differs (inner/outer annulus halves of equal mass flux give
    net Γ-flux ≠ 0). The exhibit works under the θ-halves reading
    with axisymmetric ρu_x (r-fiberwise cancellation). The
    THEOREM (existence) is true; the exhibit as stated does not
    deliver its claimed property on all in-class splits. Fix:
    "θ-halves at each radius (r-fiberwise equal mass flux)".

------------------------------------------------------------------------------
## Checks run that produced NO objection (reported so the round is
## auditable; all by hand this window)

- D.18 second-iff proof AS REPAIRED (H-NC empty-interior + H-WR):
  algebra re-derived from scratch — ∂_φp = w_rel²∂_φρ vs c²∂_φρ
  compatibility, density of the good set (finite union of closed
  empty-interior loci), continuity closure, K_h0 automatism (the
  CONCLUSION; the printed prefactor defect is pending N8, not
  repeated) — sound off fronts. R4-1 attacks the front scope, not
  this algebra.
- The w_rel = 0 kernel family as recorded (K_Γ = 0 ⟹ ∂_φp = 0
  only; ∂_φρ, ∂_φu, ∂_φv free, ∂_φs slaved to ∂_φρ at fixed p):
  verified; the r2 record is correct.
- D.6 r2 sign closure (n outward, J_inj inflow with explicit minus,
  S(x_i) flux terms ∓, S_inj contributing +J_inj): orientation
  bookkeeping re-run — closes; the N-2 repair is sound. D.16's
  signed arming clause states the right polarity test.
- D.9(ii) r2 Z_n step (fundamental cell 2π/n + Z_n invariance ⟹
  full-circle mean): correct; t_c consistency with §0 restored.
- D.9(i) product-L¹ class (r2): correct and sufficient (L∞ standing
  case covers it); identity re-expanded, signs right.
- AUD-cp / AUD-hRANGE (r2 mints): correctly placed; the
  flag-never-extrapolate semantics is the right rejector form.
- G_fund closed form: independently re-derived by hand this window
  from c² = γ(T)R_gT: ρ(∂c/∂ρ)_s/c = (T/c²)(dc²/dT)·(∂T/∂ρ)_s·(ρ/2T)
  chain with (∂T/∂ρ)_s = (γ−1)T/ρ gives
  G = 1 + (γ−1)(γ+Tγ′)/(2γ) — matches; γ=const specializes to
  (γ+1)/2. The queued independent sympy recomputation (G-f window)
  remains the falsifier of record; this hand check does not replace
  it.
- D.14 r2 y_min definition: well-placed (ess inf interface radius,
  > 0 by H-ANN — note H-ANN bounds r on cl(D) and Γ_d ⊂ cl(D), so
  the inheritance is legal).
- H-AM0 r2 "L ∈ AC" clause: exactly what the FTC step needs; the
  a.e.-transversal station clause in D.6 is well-quantified
  (finitely many bad stations per phase — consistent with finitely
  many C¹ moving fronts).
- Dimensional audit of OBS (TV form): dimensionless as claimed
  (h0, Γ²/y², T·s all ~ velocity²; W_ref² denominator).
- §6-ter ledger vs the absorbed thirteen: no absorbed objection
  silently dropped; every claimed edit located in the text at the
  marked spot. (The ledger GAP is R4-0 — a different file.)

------------------------------------------------------------------------------
## VERDICT

REPAIRABLE. The r2 revision is real work: all thirteen absorbed
objections landed where the ledger says they landed, and the two
heaviest r2 repairs (H-WR with the second kernel family; the D.6
orientation closure) survive independent re-derivation. But the
round is not dry. One finding is MED-HIGH and label-threatening:
R4-1 — D.18's equivalence clause (one limb THEOREM-classed) is
false in both directions on the declared front-carrying class via
an explicit piecewise-constant helical-front counterexample, and
the document now reads K as a smooth-region object in §5 and as a
measure with front atoms in S.22 — the distributional repair is
forced and also completes S.22's own r2 story. Two MED findings
attack r2 repair adequacy and hypothesis completeness (R4-2: H-CVX
must hold on the Hugoniot arc, not the endpoints — the clause's own
falsifier fires on the as-minted wording; R4-3: the cross-plane
deviatoric-stress AM flux is in no hypothesis and no budget — the
census exhaustiveness fails on free-slip interior-stress datasets).
One LOW-MED (R4-4: ψ single-valuedness consumed, not proved) and a
LOW cluster (R4-5) complete the list. Separately, R4-0: the
revision's "nothing dropped" frame coexists with an on-file,
unconsumed nine-objection refutation (`r2_l0` N1–N9, several still
live in the r2 text, including a printed-algebra error and the
curved-interface licensing hole) — the absorption pass must consume
that file before §7 runs, or the nothing-lost gate certifies a
false completeness claim.
