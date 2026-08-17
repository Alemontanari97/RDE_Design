# ADVERSARIAL REFUTATION — SWIRL-2D formalization, ROUND 3, lens l1
# (hyperbolic-PDE structure: characteristics, admissibility, front
#  conditions, symmetry/group action, physics of the reduction)

TARGET: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
AT REVISION r2 (1413 lines — read in full, both pages). This is the
FIRST refutation round to attack the r2 text.

ORCHESTRATION STATE NOTE (measured in-window, SR-12; not inherited
from the launch brief). The brief said "Round 2 ... write to
refute_SWIRL-2D_r2_l1.md". That instruction is STALE against the
on-disk state, measured this window:

  refute_SWIRL-2D_r1_l0.md  (O1–O12)    ABSORBED by target r1, §6-bis
  refute_SWIRL-2D_r1_l1.md  (O-1..O-9)  ABSORBED by target r1, §6-bis
  refute_SWIRL-2D_r2_l0.md  (N1–N9)     ON FILE, **NOT ABSORBED** —
                                        §6-ter does not cite it
  refute_SWIRL-2D_r2_l1.md  (N-1..N-6)  ABSORBED by target r2, §6-ter
  refute_SWIRL-2D_r3_l0.md  (R3-1..R3-7b) ABSORBED by target r2, §6-ter

Overwriting `refute_SWIRL-2D_r2_l1.md` would destroy the of-record
source of the target's own §6-ter disposition ledger — provenance
corruption, prohibited by the repo anti-entropy discipline. Both
prior agents hit the same stale-brief condition and filed at the
round-correct name with a note; this deliverable follows that
of-record precedent and is filed as ROUND 3, lens l1.

DEDUP GROUND RULE OF THIS ROUND (stricter than the brief): no
objection below repeats (a) the brief's dedup list R3-1..R3-7b,
N-1..N-6 (absorbed), (b) the r1 lists O1–O12 / O-1..O-9 (absorbed),
OR (c) the PENDING, unabsorbed r2_l0 list N1–N9 — the brief's dedup
list omits (c), but repeating a pending on-file objection adds
nothing and double-books the ledger. Consequence declared honestly:
two of this round's strongest planned attacks were found ALREADY
RAISED in the pending N-list — the D.20 rothalpy front clause being
false across wave-frame contacts (= pending N3) and the D.4/D.13(c)
spacelikeness-audit geometry hole (= pending N2). They are NOT
re-raised; but see the ORCHESTRATION FINDING at the end: §6-ter's
"All thirteen objections ... APPLIED IN PLACE" is true of the list
it names while NINE on-file objections from r2_l0 remain
undispositioned — an open absorption debt the until-dry loop must
not lose.

EVIDENCE MEASURED THIS WINDOW (pinned env, nothing installed, no
carrier edits):
- The G_fund closed form of the r2 H-CVX discharge INDEPENDENTLY
  re-derived by hand from scratch (route: along an isentrope of the
  thermally perfect closure ds = c_v dT/T − R_g dρ/ρ = 0 gives
  dT/dρ|_s = (γ−1)T/ρ; then G_fund = 1 + (ρ/2c²)(dc²/dT)(dT/dρ|_s)
  = 1 + (γ−1)(γ+Tγ′)/(2γ) exactly). This EXECUTES the "independent
  recomputation" falsifier D.2(r2) queued for the G-f window:
  result AGREES — the closed form survives its own falsifier at pen
  grade (carrier-grade execution still owed to G-f).
- D.18's second iff re-proved from scratch under H-NC + H-WR,
  including the closure of the density/continuity extension over
  the UNION of the two loci (each closed with empty interior in a
  smooth region ⟹ union nowhere dense ⟹ complement dense; ∂_φρ
  continuous ⟹ extends) — SOUND as repaired.
- All six K rows re-derived independently from unsteady cylindrical
  Euler under ∂_t → −Ω∂_φ (mass, x-mom, r-mom, Γ-row incl. the
  ∂_φp torque, s, h0 incl. the (Ω/ρ)∂_φp work term) — AGREE. (This
  is a pen-grade partial of the G-f independent re-derivation; the
  common-mode caveat of D.18's verification-status paragraph still
  applies to the carrier, not to this hand check.)
- D.20's wave-steady front algebra re-derived from the UNSTEADY
  lab-frame RH with front normal speed σ = Ω r n_θ: energy row
  [ρu_rel,n h0 + Ωr n_θ p] = 0 minus Ωr × θ-row
  [ρu_rel,n w + p n_θ] = 0 gives [ρ u_rel,n I] = 0 — confirming
  both the mass-crossing clause AND (independently of this round)
  the pending N3 repair shape (contacts: [I] free).
- D.6's CV assembly re-checked under the r2 orientation conventions
  (n outward everywhere, J_inj = inflow with the explicit minus
  sign): the sign bookkeeping now CLOSES, including the S_inj
  rearrangement and the S(x_i) plane terms.
- D.5(ii) chain rule, D.9(i) covariance algebra, D.9(ii) fundamental
  cell + Z_n step, D.3(a)/(b) determinant degree and λ-quadratic
  discriminant (real Mach lines ⟺ W > c), D.15 cancellation-family
  algebra, OBS dimensional consistency, parked-front one-sided flux
  agreement ([ρu_xΓ] = 0 from the θ-row RH with σ = 0, n_θ = 0):
  all recomputed — sound.

------------------------------------------------------------------------------
## V-1 [MED — D.2, the r2 H-CVX repair itself; hypothesis completeness
## of a THEOREM clause + front-condition conventions]
## H-CVX as minted quantifies G_fund > 0 "on the states crossed" —
## endpoint evaluation; the Bethe–Weyl entropy-monotonicity package
## needs convexity along the CONNECTING HUGONIOT ARC, and the
## Menikoff–Plohr anomalous phenomena are arc-local. The clause's own
## falsifier can be satisfied by an in-hypothesis instance.

STATEMENT ATTACKED: D.2 front clause (r2 text): "s jumps upward
across a compressive Lax front UNDER (H-CVX, r2) Bethe–Weyl
convexity of the EOS: fundamental derivative G_fund := 1 +
ρ(∂c/∂ρ)_s/c > 0 **on the states crossed**." Class THEOREM; gamma
status "EOS-general only GIVEN H-CVX". Falsifier: "an
H-CVX-satisfying EOS instance with a Lax front carrying [s] < 0
(would refute the s-monotonicity clause under its stated
hypothesis)."

THE DEFECT (quantifier). "On the states crossed" reads, and can
only read, as evaluation at the two END STATES of the jump (the
one-sided limits — that is what a front "crosses"). But the theorem
being consumed (Bethe 1942 / Weyl 1949; Menikoff–Plohr RMP 61
(1989) — the very citation the r2 repair placed in the statement)
establishes entropy monotonicity ALONG THE HUGONIOT: its convexity
hypothesis is G_fund > 0 on the Hugoniot locus connecting upstream
to downstream, i.e. on the ARC of states the shock adiabat passes
through — states the front does NOT "cross" and the minted
hypothesis does NOT constrain. An EOS that is convex at both
endpoints with an anomalous pocket (G_fund < 0) on the arc between
them makes s(p) non-monotone along the Hugoniot; on such arcs
compressive fronts satisfying the Lax inequalities with [s] < 0
relative to upstream are exactly the Menikoff–Plohr anomalous-wave
phenomenology (where Lax admissibility and the entropy criterion
decouple, and Oleinik/Liu conditions — never named in this
document — replace Lax as the admissibility standard). Such an
instance SATISFIES H-CVX as written (endpoints convex) and
realizes the falsifier's "[s] < 0" — i.e. by the document's own
falsifier semantics the clause as stated is refutable at the
stated hypothesis, which is the definition of an under-hypothesized
THEOREM label. Burden note (house rules): I do not exhibit a closed
Hugoniot computation here; but a THEOREM label carries the burden
of EXCLUDING the arc case, and nothing in the r2 text does — the
r2 repair moved the defect from "no convexity hypothesis" to
"convexity hypothesized at the wrong set", a strictly smaller but
nonzero gap, on the exact axis this round was told the previous
repair closed.

SECONDARY DEFECT (front-condition conventions, same clause): "s
jumps UPWARD across a COMPRESSIVE Lax front" leaves both the
crossing direction and "compressive" undefined. The monotonicity
statement is directional: s increases ALONG THE PARTICLE PATH
(i.e. on the downstream side of the mass flux, sign(u_n) fixed by
the crossing mass), and "compressive" means [p] > 0 in that same
mass-flux direction. Neither convention is declared in §0 or in
D.2; the falsifier "[s] < 0" inherits the ambiguity (an instance
with s decreasing in the +x direction across a front whose mass
flux runs in −x would spuriously "refute"). One sentence fixes it.

IN-SCOPE IMPACT: NONE — the γ(T)-exact discharge is GLOBAL (the
closed form G_fund = 1 + (γ−1)(γ+Tγ′)/(2γ) > 1 holds at every
table state under AUD-c2T + AUD-cp, hence on every arc), so the
pinned-closure limb of the status line is untouched. The defect
lives purely in the EOS-GENERAL-GIVEN-H-CVX limb — the clause's
claimed generality beyond the pinned gas.

REPAIR (three lines): restate H-CVX as "G_fund > 0 on the Hugoniot
arcs connecting the states crossed (equivalently, on the EOS
region spanned by the front's shock adiabat)"; add the
crossing-direction sentence (s monotone along the mass flux;
compressive = [p] > 0 same direction); note in the falsifier that
endpoint-convex/arc-anomalous instances are IN-hypothesis for the
old wording and OUT for the new — that asymmetry is the test that
the repair changed content, not words.

FALSIFIER OF THIS OBJECTION: produce a proof that endpoint
convexity of an otherwise-free Gibbs EOS implies convexity (or at
least s-monotonicity) along the whole connecting Hugoniot — any
such theorem would kill V-1 and restore the r2 wording.

------------------------------------------------------------------------------
## V-2 [LOW-MED — D.2, the r2 contact-union repair itself; proof-step
## justification]
## The ψ-continuity argument "ρ, u, v ∈ L∞ makes ψ Lipschitz on
## cl(D)" is a non sequitur as printed: it consumes existence and
## path-independence of ψ (weak-form (E1) INCLUDING the mass-RH row
## across fronts, plus simple connectivity) and chord-arc
## (quasiconvexity) of the Lipschitz domain — both true in-class,
## neither cited by the step.

STATEMENT ATTACKED: D.2, r2 insertion (a): "ψ IS CONTINUOUS ACROSS
C, and across every front: dψ = ρ u r dr − ρ v r dx with
ρ, u, v ∈ L∞ (§0) makes ψ Lipschitz on cl(D), hence continuous
across any curve."

THE DEFECT. Boundedness of a 1-form does not make its potential
Lipschitz; it makes it Lipschitz ONLY IF the potential exists —
i.e. only if the 1-form is closed in the weak sense so that the
path integral is path-independent. Closedness of ρur dr − ρvr dx
is exactly the CONTINUITY EQUATION (E1) — in smooth regions from
the PDE, and ACROSS FRONTS from the mass Rankine–Hugoniot row
([ρu_n] = 0), which is precisely a §0 T-front/C-front class
property. A field satisfying (E1) in smooth regions but violating
mass-RH on one curve has a ψ that JUMPS across that curve while
every coefficient stays in L∞ — the printed inference fails on it.
So the load-bearing legs of the step are (i) weak-(E1)-with-RH and
(ii) simple connectivity of G (declared, but not cited here), and
additionally (iii) the Lipschitz-in-space conclusion on cl(D) uses
that a bounded Lipschitz domain is quasiconvex (internal path
metric comparable to Euclidean distance) — a real property of the
declared geometry class, silently consumed. The r2 repair thus
proves the right statement from insufficient stated premises — the
same "consumed unstated" defect class the repair itself was
prosecuting (its disposition row reads "ψ-continuity across fronts
PROVED (Lipschitz from L∞ fields)", an over-claim of the proof's
own completeness).

REPAIR (two lines): "...with ρ, u, v ∈ L∞ AND (E1) holding weakly
across fronts (mass RH, §0 class), the 1-form is closed and
bounded on the simply connected G, so ψ exists and is Lipschitz
w.r.t. the path metric of D, hence (Lipschitz domain ⟹
quasiconvex) Lipschitz on cl(D)." No label change: the clause
remains THEOREM once the premises are stated — they are all
in-class.

FALSIFIER: exhibit an in-class field (all L∞ bounds, (E1) smooth
regions) violating mass-RH on one admitted curve whose ψ is
continuous anyway for every choice of base point — would show the
RH leg is not load-bearing and V-2 over-reaches.

------------------------------------------------------------------------------
## V-3 [LOW-MED — D.16; rejector calibration under the block's own
## admitted backflow]
## The audit's normalizer ⟨∮ ρ u_x |Γ| dA⟩ is SIGNED in u_x: on
## wave-induced backflow episodes — explicitly admitted by H-AM4 —
## cancellation can deflate the denominator toward ε_gross while
## gross angular-momentum transport is O(1), inflating R_AM into a
## spurious FAIL; the signed arming test cannot see it.

STATEMENT ATTACKED: D.16 [MS-DEF-AMAUDIT]:
"R_AM(x) := |⟨∮ ρ u_x Γ dA⟩ − J_inj^decl − τ_decl(x)| /
max(⟨∮ ρ u_x |Γ| dA⟩, ε_gross)", with "ε_gross = derived floor
guarding the degenerate zero-swirl case."

THE DEFECT. The denominator takes |·| on Γ but NOT on u_x. H-AM4
(r1 refuter extension, kept at r2) declares "wave-induced backflow
episodes (sign changes of u·n within the cycle)" IN scope; at a
station swept by the wave's recompression, ρu_x reverses over part
of the cycle, and the time average ⟨ρ u_x |Γ|⟩ subtracts the
backflow transport from the through-flow transport. On data with
strong backflow fraction the denominator is the small DIFFERENCE
of two O(1) gross transports — it no longer measures "gross flux"
(its declared role) but net through-transport, and can sit at the
ε_gross floor on datasets that are nowhere near the degenerate
zero-swirl case the floor was derived for. Consequence: R_AM is
inflated by an uncontrolled cancellation factor and the row FAILS
spuriously — a false-reject. False-reject is the conservative
direction, but a rejector whose firing threshold is modulated by a
cancellation the tolerance derivation does not model violates the
R5 derived-tolerance discipline as directly as a false-pass would
(tol_AM's stated inputs — periodicity residual, torque budget,
quadrature error — do not include backflow cancellation). The r2
SIGNED ARMING CLAUSE does not catch this: it injects a known
torque and checks the residual's polarity and magnitude — a
numerator-side test, structurally blind to a denominator
pathology.

REPAIR (one character class): normalize by the genuinely gross
⟨∮ |ρ u_x Γ| dA⟩ (absolute value on the whole integrand), which
bounds the current denominator from above, coincides with it on
through-flow-only data (so no recalibration on clean cases), and
is cancellation-free by construction; keep ε_gross for the true
zero-swirl degeneracy. Extend the arming spec with one
backflow-bearing synthetic (sign-reversing u_x, known torque):
R_AM must still move by the known amount within bars.

FALSIFIER OF THIS OBJECTION: a proof that on the H-AM class the
backflow contribution to ⟨ρu_x|Γ|⟩ is bounded by the terms already
inside tol_AM's derivation — then the current form is calibrated
and V-3 collapses to a documentation note.

------------------------------------------------------------------------------
## V-4 [LOW — D.6 / H-AM2; averaging bookkeeping on the torque leg]
## The balance equates a CYCLE-AVERAGED flux to τ_w,decl, but H-AM2
## defines τ_w as an INSTANTANEOUS surface integral; the object the
## balance consumes is ⟨τ_w⟩, nowhere stated.

STATEMENT ATTACKED: D.6 display "⟨∮_{S(x)} ρ u_x Γ dA⟩ = J_inj +
τ_w,decl(x)" together with H-AM2's definition "τ_w := ∮_{Σ_w} r
(τ·n)_θ dA" (r2 text: conventions added, no time average added).

THE DEFECT. J_inj carries its cycle average inside its H-AM4
definition (⟨·⟩ explicit); τ_w does not. The proof's chain is
instantaneous balance → cycle-average → storage cancels; after
that step the wall term is ⟨τ_w⟩, and on any dissipative unsteady
dataset the instantaneous τ_w(t) oscillates O(1) about its mean
(the wave sweeps the wetted wall), so the distinction is not
pedantic: a declared budget read instantaneously is ill-defined
(at WHICH t?) and read as the mean is correct but unstated. The
same untyped symbol then flows into D.16's τ_decl(x) per-station
budgets. This is the exact defect class of the PENDING r2_l0
objection N9(f) (which prosecuted the J_inj leg inside Remark 3.1)
— raised here for the τ_w leg of the MAIN balance, which N9(f)
does not touch; adjacency declared, content disjoint.

REPAIR (one line in H-AM2): "τ_w denotes the CYCLE MEAN
⟨∮_{Σ_w} r (τ·n)_θ dA⟩ wherever it enters a cycle-averaged
balance; under strict T0 the instantaneous integral is
t-independent (same one-line argument as Remark 3.1) and the
distinction vanishes."

------------------------------------------------------------------------------
## V-5 [LOW — self-containedness / navigation cluster; each item
## violates a rule the document itself declares]

(a) DANGLING ANCHOR IN A REPAIRED PROOF: D.9(ii)'s r2 proof asserts
    "over one cycle t_c = 2π/(nΩ) (§0)". Measured this window
    (grep): §0 defines only "t_c = cycle period" — the formula
    2π/(nΩ) appears NOWHERE in §0; its only occurrences are
    D.9(ii)'s citation of §0 and §6-ter's ledger row. The r2 repair
    of the traversal count (N-5) thus rests on a citation to a
    statement that does not exist — ironic, since N-5 was ABOUT the
    period. Under the navigation-first discipline (structure beats
    recollection) this is a real defect, not a typo: a reader
    auditing D.9(ii) against §0 finds no period pin, and for n
    UNEQUAL waves the true period at a fixed point is 2π/Ω, so the
    pin carries content (it encodes the Z_n hypothesis). Fix: add
    "t_c = 2π/(nΩ) for n identical waves (Z_n scope)" to §0's
    notation block.
(b) GARBLED FRAGMENT INSIDE A THEOREM PROOF: D.2 proof (i) opens
    "(E4) ⟹ (u∂_x + v∂_r)(rw) = r·(E4)/ρ + w·(u∂_x+v∂_r)r − …
    computed directly:" — the "− …" is a dangling, unfinished
    clause (the correct computation follows it). Two rounds of
    lens audits have certified this proof's ALGEBRA while the
    printed sentence remains ungrammatical mathematics; in a
    document whose standard is "every step justified", a proof
    line that does not parse is a defect of record. Delete the
    fragment.
(c) REGISTER-KEY COLLISION: the §6 register keys Remark 3.1 as
    "R3.1" while §6-ter's absorbed objection namespace is
    "R3-1..R3-7b" — "R3.1" and "R3-1" now denote a THEOREM and an
    OBJECTION in the same document, one hyphen apart. At absorption
    (token minting, lint (xxiii)) this is a glossary hazard. Cheap
    fix: key the register row "Rmk 3.1" (and "Rmk 4.1" for
    symmetry).
(d) UNTYPED SCOPE WORD: D.6's r2 admissibility clause ends "All
    but finitely many stations PER PHASE are admissible" — but §3
    is the UNSTEADY LAB-FRAME setting; "phase" (ξ, a §1/§0 notion
    for the per-phase family) has no declared meaning for the
    unsteady flow's front set. Intended reading: per dataset/per
    cycle. One word.

------------------------------------------------------------------------------
## Attacks run to destruction that produced NO objection (reported
## per house discipline so the round is auditable — including one
## the refuter KILLED ITSELF)

- PLANNED ATTACK, WITHDRAWN AS INVALID (reported per the doubts-to-
  convergence rule): "the x-march is ill-posed on the r1-admitted
  C-front data because compressible vortex sheets below the
  Miles/Coulombel–Secchi threshold are Kelvin–Helmholtz unstable,
  and no per-contact stability audit exists." VERIFICATION KILLED
  IT: in the STEADY marching problem (x time-like, u > c both
  sides), the slip line is a characteristic of the linearly
  degenerate triple family — the analog of a 1-D contact, across
  which the march is well-posed; the KH instability is a TEMPORAL
  phenomenon of the unsteady problem, and its exclusion is already
  carried by the standing strict-T0/H-AM1 periodicity scope pin
  (the flow is hypothesized periodic, hence not transitioning).
  The genuine contact obstructions are the COMPARISON-side one
  (S.22 g2b, of record) and the D.20 front clause (pending N3).
  No new objection stands here.
- D.18 second iff (r2 form): full independent re-proof under
  H-NC + H-WR including both kernel families and the
  nowhere-dense-union extension — SOUND; the r2 repair is
  complete. The extended two-kernel G-f rejector spec is the
  right spec.
- K-row list: independent hand re-derivation of all six rows from
  cylindrical unsteady Euler under ∂_t → −Ω∂_φ — agrees, including
  both non-obvious terms (∂_φp in K_Γ; (Ω/ρ)∂_φp in K_h0).
- G_fund closed form: independent hand derivation agrees (route in
  the evidence block) — the queued independent-recomputation
  falsifier, executed at pen grade, CONFIRMS.
- D.20 mass-crossing rothalpy jump: re-derived from lab-frame RH
  with σ = Ωr n_θ; [ρu_rel,n I] = 0 confirmed (and confirms that
  u_rel,n ≠ 0 is the load-bearing division — pending N3's point,
  not re-raised).
- D.6 r2 sign closure: full orientation bookkeeping re-run under
  the declared conventions (outward n, inflow J_inj, traction-on-
  fluid τ) — closes; the r2 N-2 repair is complete.
- D.9(i) product-L¹ class, D.9(ii) cell/Z_n argument (given (a)
  above), D.3(a)/(b) determinants and discriminant, D.5(ii)
  derivative chain and sign discipline, D.13 recovery monotonicity
  under AUD-c2T + AUD-hRANGE, D.14 OBS dimensions and
  TV-vs-spread inequality, D.15 cancellation family, parked-front
  one-sided flux agreement: all recomputed — no finding.
- Gamma-status sweep of every r2-touched statement (H-CVX split,
  R4.1, D.8 body, D.18 second iff EOS-general via free c²):
  consistent, EXCEPT the arc-quantifier limb prosecuted in V-1.
  (The undefined "EOS-FREE" token is pending r2_l0 N9(a), not
  re-raised.)

------------------------------------------------------------------------------
## ORCHESTRATION FINDING (not an objection against the mathematics;
## a nothing-lost finding against the loop state)

§6-ter opens "the ROUND-2 objection list (R3-1..R3-7b, N-1..N-6) is
APPLIED IN PLACE ... All thirteen objections were fixable". True of
the named list — but `refute_SWIRL-2D_r2_l0.md` (N1–N9, on file
since before the r2 revision, per r3_l0's own state note) has NO
disposition ledger anywhere in the target. Overlap is partial (N1 ≈
absorbed N-1; N9(b)/(d) ≈ absorbed N-6) but N2 (curved-Γ_d
spacelikeness audit), N3 (D.20 contact front clause), N4 (g2a
weak-vs-weak), N5 (D.14 licensing functional), N6 (H-AM0 audit
non-rejector), N7 (H-FIB bridges), N8 (K_h0 printed prefactor),
N9(a,c,e,f) are PENDING with no owner row. Until a §6-quater
dispositions them, the target's "no objection dropped" claims are
scoped to the absorbed lists only. This must ride the next revision
window.

------------------------------------------------------------------------------
## VERDICT

REPAIRABLE. The r2 revision is genuinely strong on this lens: the
H-WR/H-NC completion of the second iff survives a from-scratch
re-proof, the K list survives an independent re-derivation, the
orientation bookkeeping now closes, and the G_fund closed form
survives its own falsifier executed at pen grade. This round's new
findings are one MED (V-1: the H-CVX repair quantifies convexity at
the endpoints where the consumed Bethe–Weyl package needs it along
the Hugoniot arc — the clause's own falsifier is satisfiable
in-hypothesis; in-scope γ(T) discharge unaffected) and four
LOW/LOW-MED precision defects (V-2 the ψ-Lipschitz step's unstated
premises; V-3 the D.16 normalizer's backflow cancellation; V-4 the
τ_w averaging type; V-5 the self-containedness cluster, including a
dangling §0 anchor inside an r2-repaired proof). Nothing found this
round breaks a load-bearing result; every repair is 1–3 lines. The
lens is APPROACHING DRY on the absorbed text — but the loop is NOT
dry: the pending r2_l0 N1–N9 absorption debt (see ORCHESTRATION
FINDING) contains two MED-HIGH-class items (N2, N3) that remain
open against the current revision.
