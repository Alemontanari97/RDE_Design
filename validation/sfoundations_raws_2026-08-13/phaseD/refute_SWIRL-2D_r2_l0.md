# ADVERSARIAL REFUTATION — SWIRL-2D formalization, ROUND 2, lens 0
# (functional-analytic rigor: spaces, operators, compactness, traces,
#  every quantifier)

TARGET: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
(revision r1, 2026-08-17, 1173 lines — read in full).
CARRIER INSPECTED: `phaseD_meanswirl_symcheck.py` (read in full, 164
lines; EXECUTED this window in the pinned env, nothing installed:
OVERALL PASS reproduced, R1 residual = 2·v·w·w_rel/r — used below).
M0 ANCHORS CHECKED: [D-CONTRACT] D2.4 (M0 ~116–137), L4-DEFAULT
("axially supersonic with margin", "u_x − c ≥ delta margin is the
standing certificate").

GROUND RULE OF THIS ROUND: the 21 round-1 objections (O1–O12,
O-1..O-9) are NOT repeated. Every objection below is NEW: it attacks
either (a) content the r1 repairs did not touch, (b) the r1 repairs
themselves (repair adequacy / repair propagation), or (c) claims
whose defect only becomes visible against the carrier source or the
M0 contract. Verdict at the end.

------------------------------------------------------------------------------
## N1 [HIGH] — D.18 second-iff THEOREM: the proof consumes w_rel ≠ 0,
## which is NOT in the hypothesis list; the co-rotation locus
## w_rel = 0 carries a FOUR-parameter kernel, larger than the r1
## CJ-locus kernel

STATEMENT ATTACKED: D.18 EQUIVALENCE CLAUSE, "under (H-NC) …
K ≡ 0 iff ∂_φ(fields) ≡ 0", classed "THEOREM under H-NC
(proof above, r1-supplied)".

THE DEFECT. The proof's first move is: "with w_rel ≠ 0 (standing
scope), K_u = K_v = K_s = 0 force ∂_φu = ∂_φv = ∂_φs = 0." The
hypothesis w_rel ≠ 0 appears ONLY in this parenthetical; the
theorem's stated hypothesis is H-NC alone, which excludes open
patches of |w_rel| = c and says NOTHING about w_rel = 0. This is
exactly the defect class the r1 pass repaired in D.5(ii) (u > 0
used, unstated) and in the original second iff (sonic locus): an
assumption load-bearing in the proof and absent from the statement.

THE KERNEL IS WORSE THAN THE SONIC ONE. At a point with w_rel = 0:
K_u = ρ(w_rel/r)∂_φu ≡ 0, K_v ≡ 0, K_s ≡ 0 IDENTICALLY, regardless
of ∂_φu, ∂_φv, ∂_φs. The remaining equations force only:
  K_Γ = 0 ⟹ ∂_φp = 0  (since the sweep term carries w_rel);
  K_ρ = 0 ⟹ ρ∂_φw + w_rel∂_φρ = ρ∂_φw = 0 ⟹ ∂_φw = 0;
  K_h0 = 0 automatic (every term carries w_rel or ∂_φp).
So ∂_φρ, ∂_φu, ∂_φv, ∂_φs are ALL free: a FOUR-parameter pointwise
kernel, strictly larger than the one-parameter CJ-locus kernel the
r1 objection O-1 exhibited and the r1 repair excluded. If the
co-rotation locus {w = Ωr} has nonempty interior, the iff is FALSE
under the stated hypotheses; if it has empty interior the same
continuity argument used for H-NC closes it, but that argument is
NOT in the proof and its hypothesis is NOT in the statement.

WHY "standing scope" DOES NOT DISCHARGE IT: [T-NSW] gives
w_rel ≈ −D_CJ AT THE INTERFACE; the theorem quantifies over the
whole wave-frame domain, where w − Ωr is a field difference with no
recorded sign certificate. The doc itself insists (D.14
PRECONDITION pattern) that scope facts used pointwise must be
hypotheses with guards, not narrative.

REPAIR (names itself): extend H-NC to
  (H-NC′) |w_rel| ∉ {0, c} on every open subset of the domain,
with the same continuity-off-fronts closing argument stated for
BOTH loci, and add the co-rotation kernel family to the G-f
kernel-instance rejector list (the queued rejector currently tests
only the sonic family — it would PASS on a broken proof of the
co-rotation case).

------------------------------------------------------------------------------
## N2 [HIGH] — D.4/D.13(c): the spacelikeness THEOREM is proved for
## planes x = const only, but the contract audit applies it to the
## general curved interface Γ_d (M0 [D-CONTRACT]: "a fixed
## axisymmetric surface" with radius R(y)) — hypothesis incompleteness
## that can LICENSE an ill-posed march

STATEMENT ATTACKED: D.4 [MS-T-SPACE] ("A surface x = const is a
spacelike (marchable) data surface … iff M_x > 1", THEOREM) together
with D.13(c) ("the spacelikeness margin declared as m_x(ξ) =
ess inf_y (M_x − 1) from meridional data (D.4/D.5)") and §0's
Γ_d = "a fixed axisymmetric surface with arc/radial coordinate y
and radius R(y)".

THE DEFECT. D.4 is true as stated — for PLANES. But the object the
margin row audits is Γ_d, which by its own definition (here and in
M0 [D-CONTRACT], checked at source) is a general axisymmetric
surface, generically NON-planar (R(y) a free profile: cones, bells).
For a curved initial surface, spacelikeness is a condition on the
MERIDIONAL NORMAL: with unit meridional normal n_m = (n_x, n_r),
the surface is spacelike iff the meridional velocity's normal
component exceeds c with the Mach-cone one-sidedness,
  u·n_m > c  (i.e. M_n := (u n_x + v n_r)/c > 1),
NOT iff u_x > c. Explicit counterexample inside the doc's own class:
take u = 1.2c, v = 0.9c (W ≈ 1.5c, meridionally supersonic,
M_x = 1.2 > 1, m_x-audit GREEN) and a surface element tilted with
n_m = (cos α, −sin α), α = 50°: u·n_m = c(1.2·0.643 − 0.9·0.766)
= 0.082c < c. Every point of that element is a characteristic-side
violation: the surface cuts INTO the Mach cone, data on it do not
determine a march, yet the D.13(c) audit row — total-Mach
prohibition and all — reports a healthy margin. The audit can
therefore license exactly the ill-posed march that D.5(iii) was
built to prevent, by a GEOMETRIC rather than kinematic route.

QUANTIFIER DIAGNOSIS: D.4's theorem quantifies over surfaces
x = const; D.13(c) silently instantiates it at Γ_d. Nothing in the
document (or in the L4-DEFAULT text of M0, which certifies
"u_x − c ≥ δ") records the planarity hypothesis that makes the
instantiation legal.

REPAIR: either (a) PIN Γ_d planar (x = const) as a stated contract
hypothesis of D.13 — cheap, probably true of the intended rig — or
(b) restate the margin as m_n(ξ) := ess inf_y (M_n(y;ξ) − 1) with
n_m the meridional normal of Γ_d, and re-derive D.4's frame-
invariance clause for M_n (it survives: rotation about the axis
leaves n_m and (u, v) unchanged). Either way D.4 needs a scope
sentence; as landed, the THEOREM label is correct but the AUDIT
that cites it is unsound on the declared data class.

------------------------------------------------------------------------------
## N3 [MED-HIGH] — D.20: the r1 front-type split was NOT propagated;
## the rothalpy front clause and corollary (a) are false across
## wave-frame contacts — and the fill/product interface IS one

STATEMENT ATTACKED: D.20 [MS-T-ROTH], front leg: "Across fronts
STEADY IN THE WAVE FRAME: [ρ u_rel,n] = 0 and the energy jump give
[I] = 0, so I is transported by the exact flow across its own wave
fronts" (THEOREM*), plus the structural sentence "the exact 3-D
flow … transports only the combination I", plus corollary (a)'s
diagnostic ("a measured VIOLATION of Δh0 ≈ Ω ΔΓ … localizes
non-Euler sources").

THE DEFECT (repair-propagation failure). Round 1 (O2, O-6) forced
the mass-crossing/contact split into §0, D.2 and D.13. D.20's front
clause was left in the pre-split state: it asserts [I] = 0 from
"[ρ u_rel,n] = 0 and the energy jump", an inference valid ONLY when
u_rel,n ≠ 0 (mass-crossing). On a wave-frame-STEADY CONTACT
(u_rel,n = 0 both sides — admitted by §0's own extended S1 class on
D × S¹_φ, "both types admitted", line ~95–97), RH forces [p] = 0
only; [h0], [Γ], hence [I] = [h0] − Ω[Γ], are FREE. The clause "I is
transported … across its own wave fronts" is false on C-fronts in
the doc's own class. And the case is not exotic: the burnt/fill
interface and triple-point shear layers — the §0 r1 text's OWN
examples of generic per-phase slip surfaces — are precisely
wave-frame-steady contacts under strict T0.

CONSEQUENT FALSE DIAGNOSTIC: corollary (a) claims a violation of
Δh0 = Ω ΔΓ on uniform-I injection data "localizes non-Euler sources
(friction, reaction)". A perfectly Euler-legal wave-frame contact
with [I] ≠ 0 violates the linkage with ZERO non-Euler physics: the
"free diagnostic row" mis-attributes a contact jump to
friction/reaction. As specified, the row cannot distinguish the two
— a rejector that fires for the wrong reason is an R5 defect.

REPAIR: split the front leg exactly as D.2 was split — [I] = 0
across mass-crossing wave-steady fronts (u_rel,n ≠ 0, THEOREM* as
now); across wave-frame contacts I jumps freely, so I is a
RELATIVE-STREAMLINE invariant per side, BV across the contact's
ψ-level (mirroring D.2's contact clause); corollary (a) restricted
to relative-streamline bundles NOT crossing a contact, and the
diagnostic row's verdict text amended to "non-Euler source OR
unbudgeted contact crossing", with the contact set reported by the
front census.

------------------------------------------------------------------------------
## N4 [MED-HIGH] — S.22 (g2a) is still mislabeled after the r1 split:
## the comparison is WEAK-vs-WEAK, not weak-strong — the per-phase
## REFERENCE itself carries shocks, so the named relative-entropy
## route fails even in a slip-line-free sub-scope

STATEMENT ATTACKED: S.22 (g2a): "SHOCKS — weak-strong beyond
Lipschitz, the standing D2.5 conditional, fair as stated."

THE DEFECT. Round 1's O-7 broke g2 on CONTACTS (Chiodaroli–De
Lellis–Kreml) and the repair split g2a/g2b, leaving g2a certified
"fair". It is not. Weak-strong/relative-entropy machinery (Dafermos–
DiPerna) compares a WEAK solution against a LIPSCHITZ (strong)
reference; "weak-strong beyond Lipschitz" names the extension where
the reference has a shock (e.g. Chen–Frid–Li-type results, specific
geometries). But S.22's target object is
d(V₃D(·,·,φ(ξ)), V(·;ξ)) where the REFERENCE side V(·;ξ) is a
per-phase S1 solution that GENERICALLY CARRIES T-FRONTS — §0 admits
them, D.2 has a whole clause for them, and the standing scope
(detonation-fed interface data) makes them expected, not
exceptional. So even after excising every slip line (g2b's
sub-scope), the comparison is between TWO front-carrying weak
solutions. Multi-D stability of weak-vs-weak compressible Euler
comparisons is not a "conditional" with a named route — no
Bressan-type L¹ well-posedness theory exists in multi-D, and
relative entropy degenerates when BOTH sides jump (the shock-shift
terms are not controlled by the relative entropy). The r1 lesson of
g2b applies verbatim to g2a: a known structural obstruction is
being booked as a routine named conditional.

WHAT SURVIVES: the route is genuinely fair when the PER-PHASE
reference is shock-free (smooth transonic-free nozzle march on L4
data with margin — plausibly the actual use case of T-RED), or when
fronts are FITTED on the reference side and the estimate is run
piecewise between fitted fronts (the same Majda/Coulombel–Secchi
toolset already named in g2b).

REPAIR: relabel (g2a) as: weak-strong valid for shock-free
per-phase references (sub-scope to be certified by the front census
of the marched solution — an auditable, per-dataset condition);
shock-carrying references route to fitted-front machinery WITH g2b.
The schema's class (SCHEMA) survives; its gap inventory is
currently incomplete, which for a schema is precisely the content.

------------------------------------------------------------------------------
## N5 [MEDIUM] — D.14: "the FORM is no longer the gap" over-claims;
## the adequacy of the INTEGRATED pairing is itself unproven, and the
## pointwise closure defect at interior W-extrema is unbounded — the
## gap is a sensitivity FUNCTIONAL, not a constant

STATEMENT ATTACKED: D.14 [MS-DEF-TRIPLE], r1-repaired class line:
"the per-campaign sensitivity CONSTANT is a NAMED GAP at SCHEMA
grade … the FORM is no longer the gap, G-b reformulated"; and the
rationale sentence "the obstruction enters INTEGRATED along the
surface/march, so the correct pairing is the ψ-integral of the
obstruction content … against the transport scale 1/W_ref²."

THE DEFECT. The r1 repair correctly made OBS finite on BV (TV
form). But the LICENSING claim (OBS ≤ tol ⟹ the N6-2 closed form
is within propagated tolerance of the field-level optimum) requires
a theorem of the form
  |objective error| ≤ S[data] · OBS(ξ),
i.e. that the DESIGN-LEVEL error depends on the closure defect only
through its ψ-INTEGRATED content. That is asserted by the word
"correct" and nowhere proved, routed, or even stated as the gap.
The gap inventory says the missing piece is a CONSTANT. It is not:
what is missing is the FUNCTIONAL FORM of the sensitivity S — the
claim that pointwise closure violations are only felt integrated.
And there is a concrete reason to doubt pointwise harmlessness: at
an interior extremum of W(y) (the r1 text's own "generic on real
data" case), dψ/dW → ∞, so the POINTWISE defect of the closure
p = p(W, y) — which N6-2 uses pointwise to build the contour — is
UNBOUNDED, while OBS stays small if TV is small. Whether an
unbounded pointwise defect concentrated at a W-extremum produces
only an integrated-size objective error depends on how the N6-2
construction consumes the closure (through quadratures or through
pointwise inversion at the extremum); no lemma in this document or
in N6 §5 decides it. Until that lemma exists, "the FORM is no
longer the gap" is an over-claim inside the very sentence that was
supposed to close O5 honestly.

REPAIR: restate G-b as TWO legs: (b1) the sensitivity FUNCTIONAL —
prove (or refute) |objective error| ≤ S·OBS with S depending on
(W_ref, geometry) only, on the BV class, with the W-extremum case
treated explicitly (route: the N6-2 contour map is a ψ-quadrature
of the closure — if true, integration-by-parts moves the defect
onto TV exactly; if the construction inverts W pointwise, the
monitor needs a W-extremum guard analogous to δ_tf); (b2) the
per-campaign constant, as now. The monitor's conservative/blocking
role (SAFETY NOTE) is unaffected — this attack is on the LICENSING
direction only, which is exactly the direction R5 cares about.

------------------------------------------------------------------------------
## N6 [MEDIUM] — H-AM0's "auditable, not merely assumed" is false as
## specified: quadrature convergence under refinement CANNOT reject
## the concentration channel on fixed-resolution data — channel (0)'s
## audit is a non-rejector

STATEMENT ATTACKED: H-AM0's audit sentence ("AUDIT (H-AM0 is
auditable, not merely assumed): quadrature convergence of the flux
integrals under grid refinement") and D.8 channel (0)'s "AUDIT:
H-AM0's own quadrature-convergence check under refinement";
downstream, D.6's conditional (c2) inherits it.

THE DEFECT (falsifier-power, the doc's own R5 lens). The datasets
this block will ever audit are chamber-CFD fields: FINITE-
RESOLUTION, piecewise-polynomial-representable objects. On such an
object, refining the QUADRATURE always converges — the integrand is
already tame at the data's own scale. The hypothesis H-AM0 is about
the underlying FLOW (vanishing-viscosity concentration, orifice-lip
singularity, measure-valued fronts): a flow violating H-AM0,
sampled on any fixed grid, yields a dataset on which the specified
audit PASSES. The audit as written can only ever fail on a
quadrature-vs-data mismatch, i.e. it audits the postprocessing, not
the hypothesis. A check that cannot fire on the violation it names
is a non-rejector — precisely the defect class (vacuous monitor)
that Remark 4.1 prosecutes elsewhere in the same document.

REPAIR (route exists and is standard): audit CONCENTRATION, not
convergence — e.g. (i) solver-resolution sequence (not quadrature
refinement): recompute the flux/torque integrals on the dataset
family at increasing SOLVER resolution and test Cauchy behavior of
the BALANCE residual, with divergence → H-AM0 red; (ii) local
scaling monitor at named suspects (orifice lips, CV corners):
integrals of |ρΓu| over shrinking collars must scale with collar
measure (an atom shows as scale-independence). Both are per-dataset
and honest; (i) matches how the numerical-shear budget of H-AM2 is
already priced. Until one is specified, H-AM0 must be labeled
ASSUMED-per-dataset (declared, unaudited), and D.6's (c2) sentence
"it is auditable per dataset" corrected accordingly.

------------------------------------------------------------------------------
## N7 [MEDIUM] — D.2/H-FIB: the r1 repair contains two unproven
## bridges — the "equivalently" clause and the "delivers H-FIB there"
## clause (interface monotonicity does NOT give domain fibration
## without a reachability hypothesis)

STATEMENT ATTACKED: D.2 hypothesis (H-FIB): "every level set of ψ
in G is CONNECTED — equivalently, G is a streamtube region fibered
by its streamlines over a single transversal arc (…); on the
interface, the D.14 through-flow guard makes ψ ↦ y strictly
monotone and delivers H-FIB there."

TWO DEFECTS, both inside the r1 repair:
(a) The "equivalently" is not an equivalence at the stated level of
    generality. Connected fibers ⟸ fibered-over-a-transversal is
    immediate; the CONVERSE (connected level sets ⟹ existence of a
    single C¹ arc transversal to ALL streamlines, trivializing the
    foliation) needs an argument: ∇ψ ≠ 0 plus connected fibers
    gives a foliation by arcs with interval leaf space, but a
    GLOBAL section of the leaf-space projection requires
    properness/completeness of the leaves (a non-proper leaf
    accumulating on the boundary admits no continuous global
    transversal). On the bounded Lipschitz D with fronts this is
    plausible but not free; an equivalence asserted inside a
    THEOREM's hypothesis is itself a claim and currently has no
    proof and no class. Cheapest repair: demote "equivalently" to
    "in particular, sufficient:" — nothing downstream uses the
    converse.
(b) "delivers H-FIB there" is a non sequitur as quantified. The
    through-flow guard gives strict monotonicity of ψ ON THE
    INTERFACE ARC — i.e. the interface is a transversal on which
    each ψ-value occurs once. H-FIB is a statement about level sets
    IN G. The bridge needs: EVERY streamline of G meets Γ_d (no
    streamline entering/leaving G solely through other boundary
    portions, no closed streamlines trapped between fronts —
    note the simple-connectivity exclusion of closed streamlines
    uses ∇ψ ≠ 0 on the enclosed disc, which fails if the disc
    meets a front, so fronts re-open the closed-leaf case that
    simple connectivity was supposed to kill). That reachability
    hypothesis (call it H-REACH: G is the streamtube OF Γ_d) is
    load-bearing and unstated; with it, (a)'s converse is also
    moot since Γ_d itself is the transversal.
REPAIR: state H-FIB as "G is the streamtube of Γ_d: every
streamline of G meets Γ_d exactly once" (this is what every
downstream consumer — D.14's ψ-parametrization, N6-3 — actually
uses), keep the counterexample remark, drop the unproven
equivalence. THEOREM label then stands.

------------------------------------------------------------------------------
## N8 [LOW-MED] — D.18 proof, printed algebra error: the K_h0
## elimination line has the wrong prefactor (Ω w_rel instead of
## w w_rel / r); the conclusion survives, the printed identity is
## false — and it is exactly the kind of pen line the doc's own
## carrier discipline exists to catch

STATEMENT ATTACKED: D.18 proof line: "K_h0 adds nothing new: with
ds = 0, K_h0 = Ω w_rel (∂_φw + w_rel ∂_φρ/ρ) = 0 automatically by
K_ρ."

THE COMPUTATION (all under the proof's context ∂_φu = ∂_φv =
∂_φs = 0, hence ∂_φh = ∂_φp/ρ, and K_Γ = 0 ⟹ ∂_φp = w_rel²∂_φρ):
  K_h0 = (w_rel/r)(∂_φp/ρ + w∂_φw) + (Ω/ρ)∂_φp
       = (w/(rρ))∂_φp + (w_rel w/r)∂_φw        [w_rel/r + Ω = w/r]
       = (w w_rel/r)·(∂_φw + w_rel ∂_φρ/ρ).
The correct prefactor is w w_rel/r = (Ω + w_rel/r)·w_rel, which
equals the printed Ω w_rel ONLY where w_rel = 0 (or r → ∞). The
final "= 0 by K_ρ" is right (the bracket vanishes), so the THEOREM
conclusion stands; the displayed identity is false as printed. In a
document whose §5 discipline is that pen algebra near the carrier
must be machine-checked or flagged, an incorrect printed elimination
inside the ONE clause r1 promoted to THEOREM is a rigor defect and
a cheap fix: correct the prefactor, and add this one-line
elimination to the queued G-f kernel-instance rejector (it is a
two-second sympy check).

------------------------------------------------------------------------------
## N9 [LOW] — label/consistency discipline cluster (each violates a
## rule this document itself declares)

(a) UNDEFINED STATUS TOKEN "EOS-FREE": §0's STATUS RULE defines
    exactly three gamma statuses (EOS-GENERAL, γ(T)-EXACT,
    γ=const-ONLY). Eight register rows and five statements carry
    "EOS-FREE", nowhere defined. Presumably "no thermodynamic
    closure enters at all" (stronger than EOS-GENERAL, which
    consumes Gibbs); by the doc's own navigation-first/label
    discipline an undeclared fourth status is a rule violation.
    Fix: one sentence in §0.
(b) "SEVEN ROWS" MISCOUNT: D.18 says "the residual vector is
    (carrier C4, seven rows, zero leftover)" and the header says
    "C4 ×7 rows" — the residual vector has SIX components
    (K_ρ, K_u, K_v, K_Γ, K_s, K_h0); the carrier's seventh C4 check
    (verified at source) is C4-gamrow-equiv, an EQUIVALENCE check,
    not a residual row. The claim-register row for D.18 says
    "6 rows". Three mutually inconsistent counts for the same
    object in one document. Fix: "six residual rows + one
    independence check".
(c) D.13's "State recovery on supersonic patches is UNIQUE under
    AUD-c2T" is an unlabeled THEOREM-grade assertion with no proof
    and no falsifier — the same defect pattern r1 prosecuted in
    D.18 (O-1). It happens to be TRUE and cheap: at fixed y the
    data (M, s, w, h0) determine T uniquely because
    F(T) := h(T) + M²c²(T)/2 has F′ = c_p + M²(dc²/dT)/2 > 0 under
    AUD-c2T, then p from (s, T); two lines. Write them (for ALL M,
    incidentally — the "supersonic" restriction is about
    marchability, not recovery) and give the clause a class.
(d) D.14's OBS uses y_min, never defined in the document (inferable
    as ess inf_y y ≥ r_min via H-ANN — but H-ANN bounds r on D, and
    y lives on Γ_d; one definition line needed).
(e) D.15 Clause 2: "solvable for any h0, y: Γ² = Γ₀² + 2∫y²h0′dψ"
    needs the qualifier Γ₀² > 2·sup of the running decrease (else
    Γ² < 0); on BV∩L∞ rows the sup is finite so a large Γ₀ always
    exists — say so, or the cancellation family's existence claim
    has a silent hypothesis.
(f) D.6/Remark 3.1 interplay: H-AM4 defines J_inj as a CYCLE MEAN;
    Remark 3.1 asserts an INSTANTANEOUS balance whose injection
    term is the instantaneous flux — the remark silently redefines
    J_inj(t). One clause ("with J_inj read instantaneously; under
    strict T0 it is t-constant by the same one-line argument")
    closes it.

------------------------------------------------------------------------------
## Checks run that produced NO objection (reported per house
## discipline, so the round is auditable)

- D.2 proof algebra (i)/(iii), contact ψ-level argument (u_n = 0 on
  both sides ⟹ front is a level curve of ψ, ψ continuous across):
  verified by hand — sound.
- D.3(b) pencil factorization and D.5(ii) chain rule (including the
  s-fixed/T-slaved consistency of the state derivative): recomputed
  by hand — correct, including the ∂M_x/∂Γ sign and the u > 0
  hypothesis as repaired.
- D.9(i) integrated statement and the SOMEWHERE inference (r1
  form): now a correct two-line argument; F2 matches it.
- D.9(ii)/D.17 traversal argument for n identical waves: correct
  (period at fixed point 2π/(nΩ); φ-average over 2π/n = full-circle
  average by periodicity).
- D.10 strict positivity of E_θ under ρu_x > 0 a.e. and u_θ ≢ 0:
  sound; (σ/μ)² arithmetic checked.
- Carrier executed in the pinned env: OVERALL PASS reproduced
  exactly as claimed in the header (no installation performed);
  R1's symbolic residual 2vw·w_rel/r is generically nonzero —
  legitimate symbolic rejector (it does vanish identically on
  v ≡ 0 or w ≡ 0 subfamilies, so it rejects on the generic field
  class, which is what a symbolic rejector must do).
- D.20 smooth-region leg (C3 = C2 − Ω·C1) and corollary (b): sound
  given N3's front-scope repair.
- §6-bis disposition ledger cross-checked against the r1 objection
  lists: no round-1 objection silently dropped (the two NAMED-GAP
  dispositions G-f, G-g are honestly carried).

------------------------------------------------------------------------------
## VERDICT

REPAIRABLE. The r1 revision genuinely raised the document's floor —
the honest-downgrade pattern (D.15 split, D.18 completeness SCHEMA,
D.19 bridge PRACTICE) is real rigor, and the central objects (flux
nullity, TRIPLE transport, rothalpy splitting, the monitor) survive
this round intact. But round 2 finds nine genuinely new defects, of
which four threaten labels as they stand: N1 (D.18's second-iff
THEOREM has an unlisted hypothesis and a larger unexcluded kernel),
N2 (the D.13(c) audit instantiates D.4 outside its proven scope —
the only objection in this round that can silently license an
ill-posed march), N3 (D.20's front THEOREM* is false on the class's
own C-fronts — an r1 repair-propagation failure), and N5 (D.14's
"form is no longer the gap" over-claims; the licensing-direction
sensitivity is a functional-form gap, not a constant). All nine
have named, cheap-to-moderate repairs (added hypotheses, scope
sentences, one relabel, two audit redesigns); none breaks a
load-bearing result irreparably.
