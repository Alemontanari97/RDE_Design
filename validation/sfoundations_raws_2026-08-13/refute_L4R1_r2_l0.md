# ROUND-2 ADVERSARIAL REFUTATION — `phaseD_L4_implies_R1.md` (r1)

**Lens**: hyperbolic-systems rigor (eigenstructure, symmetrizer, energy estimate,
boundary-condition count). **Target**: the r1 revision in full (1171 lines), including every r1
repair, every label, and every falsifier. **Ground rule of this round**: only NEW objections
count; the round-1 list (O-1..O-12, N-list, O1..O11 P1-P3) is taken as consumed by r1 and is not
re-litigated except where an r1 repair itself opens a NEW hole. Absence attacks included.

**Method declaration**: every r1-critical computation was re-derived by hand before attacking
(list in Section B); every objection below carries (i) the exact claim attacked with anchor,
(ii) the defect with named spaces/hypotheses, (iii) the rigor class of MY objection
(complete proof / sketch / modeling assertion), (iv) severity, (v) repair path, (vi) a REJECTING
TEST for the objection itself (what would kill it).

---

## A. NEW OBJECTIONS

---

### R2-O1 (P1, CONSUMPTION/LABEL) — The composite "L4 => R1 BY THEOREM for the steady per-phase class" consumes a VOLUME hypothesis (H2.2) that the L4 SURFACE certificate does not supply; no monitor covers it

**Claim attacked.** Section 5 composite (lines ~1079-1103): "On the L4 default ... causal
separation R1 holds BY THEOREM for ... (ii) the steady per-phase class (Theorem 2(a)-(b) ...)";
and 3.4(3)(a): the certificate delivers "the HYPOTHESES of Theorems 1-2".

**Defect (hypothesis-strength mismatch).** The L4-DEFAULT of record ([D-CONTRACT], quoted at
lines 74-83) is a certificate ON THE SURFACE Gamma_d: "every patch of Gamma_d ... supersonic with
margin", u.n_I - c >= delta a.e. on Gamma_d. Theorem 2's hypothesis (H2.2) (line ~569) is a
VOLUME condition: u-bar_x - c-bar >= delta on the whole duct segment
Omega_{[x_0, x_I]} = Omega intersect {x_0 < x < x_I} — the document itself stresses "(not only on
the slab)". A trace condition on a codimension-1 surface does not imply, and cannot imply, an
L^infinity lower bound on an open 3-D subdomain: the implication
{u.n_I - c >= delta on Gamma_d} => {u_x - c >= delta on Omega_{[x_0,x_I]}} is FALSE as a
statement about W^{1,infinity} fields.

*Counterexample shape (complete at the level needed).* Take a per-phase base state, (G3)-box
valued, W^{1,infinity}, with u_x - c >= delta on the slab S_h and on Gamma_d, but with an embedded
pocket P subset Omega_{(x_0, x_I)} \ S_h where 0 < u_x < c (a locally over-expanded/recompressed
region; nothing in the L4 certificate forbids it). Then: (M-a) is green (margin on Gamma_d holds);
(M-b) is green (no front anywhere); (M-c) as scoped in 3.4(3) is green (the SLAB is regular —
(M-c) monitors "slab data-class purity ... across the slab", lines ~899-903). Yet Theorem 2 is
INAPPLICABLE (S_x = S A_1 fails positivity on P; x is not time-like there), and the failure is not
merely of the method: inside P, Lemma 2.2(c)'s own third bullet supplies elliptic-in-x directions
(complex xi_x for eta with u_perp.eta = 0), i.e., a genuine steady upstream-downstream coupling
channel through the pocket — the document's own mechanism (used in Corollary 4) defeats the
document's own composite. So "L4 => R1 [steady per-phase] BY THEOREM" is false as written: the
true statement is "L4 + (H2.2) => R1 by Theorem 2", and (H2.2) is a SEPARATE certificate that no
monitored condition (M-a/M-b/M-c) tracks. Note the asymmetry with Theorem 1, which is honest here:
its (H1.3) needs the margin only ON Gamma_I, so composite clause (i) is correctly conditioned —
clause (ii) is not.

**Rigor class of objection**: complete (quantifier accounting + counterexample construction; the
pocket state is elementary to write down as an explicit smooth field — e.g., a mollified axial
Mach profile M_x(x) dipping from 1 + delta/c to 1/2 and back, constant T).

**Severity**: P1 — this is the headline composite of the document, and its consumption route
(certificate ledger of 3.4(3)) is exactly what F2 will read.

**Repair path.** Either (a) restate composite clause (ii) as conditional on a named SEGMENT-MARGIN
certificate "(M-d): u_x - c >= delta on Omega_{[x_0,x_I]}", noting that the certified per-phase
supersonic march (engine X-TOCV class) in fact produces and can log exactly this quantity
station-by-station — so the repair is a cheap ledger addition, not new theory; or (b) restrict
clause (ii) to the maximal sub-segment upstream of Gamma_d on which the certified march itself
maintained the margin. In both cases add (M-d) to the monitored-conditions list and to register
row 3d's hypothesis column.

**Rejecting test (kills this objection).** Exhibit either (i) a line in [D-CONTRACT]/M0 making the
L4 default a VOLUME certificate over the duct segment (I found none in the quoted block; the
quoted wording is "every patch of Gamma_d"), or (ii) a proof that margin on Gamma_d plus the
per-phase class I2 forces margin on the segment (impossible without extra structure: the
counterexample above is in the class).

---

### R2-O2 (P1/P2, APPLICABILITY + ABSENCE) — Theorem 1's (H1.1) demands a W^{1,infinity} base on ALL of Omega_up x [0,T_f]; the RDE upstream domain contains the rotating wave complex BY DESIGN, so composite clause (i) is vacuous for the device data class; the rescuing collar-localization statement is absent

**Claim attacked.** Section 5 composite clause (i): "R1 holds BY THEOREM for ... the linearized
unsteady dynamics about any W^{1,infinity} base state carrying the margin (Theorem 1 ...)";
3.4(3)'s claim that the monitor set (M-a/M-b/M-c) + bridge (H-RW) certifies "the HYPOTHESES of
Theorems 1-2".

**Defect (two-part).**

*(1) Applicability collapse.* (H1.1) requires W-bar in W^{1,infinity}(Omega x [0,T_f]) — in the
energy identity (EI) the constant C_0 consumes d_j(S A_j) on the WHOLE upstream domain Omega_up,
not just the slab. But [D-CONTRACT] places Gamma_d "downstream of all heat release": the
detonation front, its oblique-shock tails and slip lines — the S1-class piecewise-smooth wave
complex that defines the device — live INSIDE Omega_up. So for the physical per-phase data class
(S1, piecewise smooth with fronts), (H1.1) fails ALWAYS, not exceptionally: there is no admissible
device base state to which Theorem 1 applies on Omega_up as stated. Round-1's O-11 attacked the
monitor for missing fronts CROSSING the slab; this is different and worse: even with a pristine
slab and all three r1 monitors green, an interior slip line at, say, mid-combustor (which is the
generic state of affairs, not a fault) voids the theorem's hypothesis on Omega_up. Composite
clause (i)'s "about any W^{1,infinity} base state carrying the margin" is formally true and
materially empty for the class the contract serves.

*(2) The missing (and available) repair is absent.* The correct statement, standard in the
hyperbolic-IBVP toolkit, is COLLAR-LOCALIZED: let C_h = Omega intersect {x_I - h < x < x_I} (or a
transversal collar of Gamma_I) on which the base IS W^{1,infinity} (this is exactly what (M-c)'s
slab-regularity monitor checks); apply Theorem 1's estimate on C_h with the upstream collar face
Gamma_{in}^{coll} = Omega intersect {x = x_I - h} in the role of Gamma_in (hypothesis (ii) or
(ii') there); conclude: no downstream signal enters C_h through Gamma_I. Then causal separation
for the REST of Omega_up follows by domain decomposition: any influence path from downstream to
{x < x_I - h} must cross C_h (del Omega_up structure + finite speed, Remark 1.5.2), and inside C_h
the difference field is identically zero before any such crossing. This patched statement is
(a) stronger than needed, (b) provable with EXACTLY the tools already in the document
(Lemmas 1.1-1.3 + (EI) + 1.5.2's cone argument — the cone argument must then be upgraded from
SCHEMA to a proof, since it becomes load-bearing), and (c) is the version whose hypotheses the r1
monitor set ACTUALLY certifies ((M-c) checks the slab = the collar; nothing checks Omega_up). Its
absence means the document proves a theorem whose hypotheses its own monitors do not certify, and
monitors a hypothesis set for which no theorem is stated.

*(Adjacent ledger gap, same root)*: (G3)-box membership of the base on Omega_up (resp. the collar)
is likewise a consumed hypothesis of (EI)'s constants with no monitored condition; it should ride
whichever domain the repaired statement uses.

**Rigor class of objection**: part (1) complete (hypothesis accounting vs the contract's own
placement of Gamma_d; the wave complex being upstream is [D-CONTRACT] text, not physics I import);
part (2) sketch — the collar-patching argument is stated at SCHEMA level here (the finite-speed
ingredient is the document's own 1.5.2 SCHEMA; a full proof needs the frustum energy argument
written out).

**Severity**: P1 for the composite's consumption claim (clause (i) + 3.4(3)(a) as a certificate
ledger); P2 for the theorem itself (which is correct as a mathematical statement about smooth
bases).

**Repair path.** Add "Theorem 1' (collar form)": hypotheses (H1.1') W^{1,infinity} on
C_h x [0,T_f] only + (H1.3) on Gamma_I + (ii)/(ii') on the collar's upstream face; conclusion:
U^(1) = U^(2) on C_h, and (given finite speed on Omega_up, now proved, not SCHEMA) on all of
Omega_up for t up to the first arrival time from Gamma_{in}^{coll} differences. Rewire 3.4(3)(a)
and Section 5 clause (i) to consume Theorem 1' — whose hypotheses (M-c) + (M-a) actually monitor.
Promote 1.5.2 to THEOREM (the lens/frustum computation with the Section-1 symmetrizer is four
lines in this framework) since it becomes load-bearing.

**Rejecting test.** Exhibit (i) a reading of [D-CONTRACT] under which Omega_up excludes the wave
complex (e.g., Omega_up defined only as the slab-adjacent region — the document's own Geometry (D)
block defines Omega_up as everything upstream of Gamma_I, so this requires changing the document,
which IS the repair), or (ii) a proof that the I2 per-phase base class is W^{1,infinity} on all of
Omega_up (contradicts the S1 class definition and the physics of the contract).

---

### R2-O3 (P2, LABEL) — Corollary 4's truth-table row (a) asserts R2 (well-posedness, existence included) for the multi-D L4 patch via "Theorems 1-2", which prove NO existence; the Corollary's own rigor line silently omits row (a)

**Claim attacked.** Corollary 4 (line ~1018): "the truth table ... realizes: (a) R1 AND R2: any L4
patch (Theorems 1-2)"; register row 4; the R2 semantics fixed by the document itself (R2 =
"well-posed data", well-posedness = Hadamard: existence + uniqueness + continuous dependence —
the sense used everywhere else in Section 4, e.g., quadrant (c) fails R2 by EXISTENCE failure,
quadrant (d) by uniqueness failure).

**Defect.** Theorems 1 and 2 are uniqueness/a-priori-estimate statements in
C^1(closure(Omega_up) x [0,T_f]; R^5), extended by density to C([0,T_f]; H^1) intersect
C^1([0,T_f]; L^2). NOWHERE in the document is EXISTENCE proved or cited-as-consumed for the
multi-D upstream problem: the problem has a uniformly characteristic boundary portion Gamma_w
(kernel multiplicity 3), a positive-definite boundary portion Gamma_I (no BC), an inflow face with
a maximal-nonnegative BC, and wall-interface corner curves. Existence there is exactly the
Friedrichs 1954 / Lax-Phillips 1960 / Rauch 1985 theory PLUS corner compatibility — the document
cites Rauch 1985 for TRACES only (Remark 1.5.3, load-bearing for mollification), and its own NG-3
concedes the corner argument is "not written here". By the document's rigor vocabulary, row (a)'s
R2 clause is at best THEOREM* with three named citations and an NG-3 dependency — but the row sits
inside a Corollary labeled "THEOREM (by exhibition; quadrants (b), (c), (d) all complete)". Note
the tell: the rigor line itself lists only (b), (c), (d) — row (a) is asserted in the table and in
the prose ("any L4 patch") but is covered by NO rigor declaration at all, and register row 4's
hypothesis/rigor columns do not flag it. Round-1 O10(d) raised the existence gap for claim (i) in
the 1-D model (repaired by the explicit transport construction); the MULTI-D row (a) has no such
construction and was not attacked in round 1.

**Rigor class of objection**: complete (label semantics + inventory of what is proved; the
assertion "existence is genuinely not derivable from the document's estimates alone" is the
standard fact that a priori estimates yield existence only through a duality/viscosity/semigroup
argument, none of which appears).

**Severity**: P2 (the independence claim — the Corollary's actual point — survives on (b),(c),(d);
but row (a) is the row F2 will quote for the L4 default, and it is the unlabeled one).

**Repair path.** Three options, any sufficient: (i) restrict the truth table explicitly to the 1-D
normal-incidence model class (already done for (b),(d) via the r1 qualifier; then (a) follows from
the same explicit transport solves — two lines); (ii) label row (a)'s R2 clause THEOREM* citing
Friedrichs 1954 (existence via elliptic regularization for symmetric positive systems with
maximal nonnegative BCs), Rauch 1985 (characteristic boundary), + NG-3 for corners, and add the
citation to the load-bearing list; (iii) drop row (a) to "R1 by Theorem 1; R2 = NG-3-conditional"
in the table itself.

**Rejecting test.** Point to an existence proof or an existence-bearing citation consumed for the
multi-D patch problem anywhere in the document (the cited-standard-results block, lines
~1136-1149, load-bears Rauch 1985 only for "traces and mollification at the slip wall").

---

### R2-O4 (P2, CITATION-SCOPE) — The 3.3 uniqueness clause survives r1's citation swap in name only: wave-curve constructions give uniqueness among SELF-SIMILAR fans, not "in the piecewise-smooth 1-D class"

**Claim attacked.** Section 3.3 (lines ~833-836): "the one-front function IS the admissible
solution; uniqueness in the piecewise-smooth 1-D class by the convex-EOS wave-curve construction —
Menikoff & Plohr 1989 §V, THEOREM* for the uniqueness clause"; also consumed by register row 3c.

**Defect.** Round-1 O-9 demanded the citation move FROM Smoller's gamma-law chapters TO the
convex-EOS wave-curve construction, and r1 complied — but the wave-curve construction
(Menikoff-Plohr §V, and any construction of that type) proves existence and uniqueness of the
Riemann solution WITHIN the class of self-similar wave fans (functions of x/t composed of
constant states, simple waves, admissible discontinuities). The document claims uniqueness "in the
piecewise-smooth 1-D class" — a strictly larger class containing non-self-similar
piecewise-smooth entropy solutions. Uniqueness there is a genuinely different theorem: for large
data it is NOT settled by any cited result; the available tools are (α) weak-strong uniqueness via
Dafermos relative entropy (needs one of the two solutions Lipschitz — fails here: the reference
solution contains a shock), (β) stability/uniqueness theory for a single large extremal Lax shock
(a-contraction up to shifts, Kang-Vasseur, Invent. Math. 224 (2021) and sequels — covers extremal
shocks of the Euler system under convexity-type EOS conditions; whether the gamma(T) gas of (G)
satisfies its hypotheses is itself a check nobody has done here), (γ) short-time piecewise-smooth
uniqueness by the transmission/characteristics method (Li Ta-tsien style — local in time). None is
cited; the THEOREM* label therefore rests on a citation that does not cover the stated class. The
consequence is material for the counterexample's logical role: as written, 3.3 claims "the exact
entropy solution" breaches the interface; without class-correct uniqueness the honest claim is "AN
admissible entropy solution breaches" — which, note, is STILL fully sufficient for everything 3.3
is consumed for (defeating the naive nonlinear no-influence conjecture requires one admissible
solution violating it, since a nonlinear R1 theorem would have to hold for every admissible
solution).

**Rigor class of objection**: complete for the citation-scope claim (self-similar vs
piecewise-smooth is a definitional matter; MP §V's construction is self-similar by construction);
sketch for the (β) repair-path adequacy (the a-contraction hypotheses for gamma(T) EOS would need
verification).

**Severity**: P2 (label + one overreaching sentence; the theorem's role in the document is
unaffected under the weakened phrasing).

**Repair path.** Cheapest and fully sufficient: weaken to "the one-front function is AN admissible
entropy solution (Lax-admissible by (G4)/Bethe-Weyl, exactly RH-connected); within the
self-similar class it is THE Riemann solution (MP §V)" and change the 3.3 rigor tag for the
uniqueness clause from THEOREM* to "THEOREM* (self-similar class); piecewise-smooth-class
uniqueness = named residual". Alternatively cite (β) and verify its EOS hypotheses for (G) — a
theory task, overkill for the role.

**Rejecting test.** Produce a theorem in MP §V (or any cited work in the document) whose statement
quantifies over non-self-similar piecewise-smooth entropy solutions of the 1-D Euler system at the
relevant strengths. (Reading MP §V's construction: it parametrizes wave curves and composes
self-similar fans; no such statement exists there.)

---

### R2-O5 (P3, HYPOTHESIS UNDER-SPECIFICATION) — Remark 1.5.5's (ii') is stated without the regularity/multiplicity hypotheses that make "the same maximal nonnegative boundary condition" meaningful on a possibly characteristic Gamma_in

**Claim attacked.** Remark 1.5.5 (lines ~1403-416): hypothesis (ii') "same maximal nonnegative
(Friedrichs-dissipative) boundary condition on Gamma_in ... e.g., prescribed incoming
characteristic components, the physically posed injection condition"; labeled THEOREM.

**Defect (three clauses).** (a) The proof needs the homogeneous boundary subspace field
x |-> N(x) subset R^5 to be defined a.e. and MEASURABLE on Gamma_in with <S A(n) U, U> >= 0 on
N(x) a.e. — no measurability/definition hypothesis is stated; for the energy inequality this is
cheap but must be said, since N(x) enters an a.e. boundary integral. (b) The offered example
"prescribed incoming characteristic components" is not well-defined where Gamma_in is
CHARACTERISTIC for the base flow: at points with u-bar.n = -c (sonic inflow) or u-bar.n = 0
(grazing injection — generic on the rim of an injection face), the incoming count jumps
(4 -> 3 -> ...), the spectral projectors blow up in the glancing limit, and "the same BC" for two
solutions is ill-defined pointwise. Theorem 1 carefully hypothesized nothing about Gamma_in
because (ii) forced U = 0 there; (ii') re-opens the boundary and inherits none of the needed
structure (no non-characteristicity hypothesis, no constant-multiplicity hypothesis, no
uniform-subsonicity-of-inflow hypothesis). The ESTIMATE survives under (a) alone — the proof
really only uses pointwise nonnegativity on a measurable subspace field — but then the "e.g."
must be qualified: characteristic-variable prescription defines a valid N(x) only on the
non-characteristic part of Gamma_in, with constant multiplicity. (c) The Remark's purpose (per
round-1 O11) was to match "the physically posed injection condition"; the physically posed RDE
injection face IS partially characteristic (choked/grazing injector rim states), so the example
as stated does not cover the motivating case — the hypothesis that does is "N(x) maximal
nonnegative a.e., measurable", full stop.

**Rigor class of objection**: complete for (a),(b) (the glancing degeneracy of eigenprojectors is
Lemma 0.2 arithmetic: the acoustic projectors carry 1/c factors against (u.n -+ c) gaps); modeling
assertion for (c) (injector-face phenomenology).

**Severity**: P3 (the THEOREM label is repairable by adding one hypothesis sentence; no consumer
currently leans on (ii') at a characteristic inflow point).

**Repair path.** Restate (ii') as: "there is a measurable subspace field N(x) with
<S A(n) U, U> >= 0 on N(x) a.e. on Gamma_in, and U^(1) - U^(2)(t, x) in N(x) a.e."; demote the
characteristic-components example to the non-characteristic constant-multiplicity part of
Gamma_in; note the grazing-rim caveat in one line.

**Rejecting test.** A proof that the injection faces in the contract's data class are uniformly
non-characteristic with constant incoming count (then (b),(c) die and only the measurability
sentence (a) remains — a nano-repair).

---

### R2-O6 (P3, ASSERTED GEOMETRIC LEMMA) — (D')'s "Then Omega_up is a Lipschitz domain and boundary traces of H^1 functions exist" is itself an unproved, uncited geometric lemma inside a hypothesis block that feeds a THEOREM* label

**Claim attacked.** Geometry block (D') (lines ~201-207): "Gamma_w and Gamma_I meet transversally
with a uniform angle bound ... THEN Omega_up is a Lipschitz domain and boundary traces of H^1
functions exist in L^2(del Omega_up)."

**Defect.** The implication {two Lipschitz surfaces meeting along a corner curve at angles in
[theta_0, pi - theta_0]} => {the enclosed region is a Lipschitz domain} is a real lemma, not a
definition: near a corner-curve point one must produce a single Lipschitz graph direction for the
BENT boundary (union of two graphs with respect to different directions), and for Lipschitz (not
C^1) pieces with only an angle condition between (a.e.-defined) tangent planes this requires an
argument (local flattening of Gamma_I, then verifying the wall graph survives in the tilted
frame; uniform theta_0 makes it work, but nobody here has written it, and no citation — e.g.,
Grisvard, *Elliptic Problems in Nonsmooth Domains* §1.2 for the dihedral model case — is given).
As r1 stands, the chain is: (D') [asserted lemma] -> Omega_up Lipschitz -> L^2 traces ->
Remark 1.5.3's THEOREM* on smooth portions. A hypothesis block is the right place for
"Omega_up is Lipschitz"; it is the wrong place for a PROOF STEP ("Then ...") with no proof. The
r1 repair of O-7 thus moved the gap rather than closing it: the transversality hypothesis was
added (good), but the load-bearing implication from it was asserted (new gap).

**Rigor class of objection**: complete as a label/rigor-accounting claim; the mathematical content
(that the implication needs proof for Lipschitz pieces) is standard nonsmooth-domain theory.

**Severity**: P3 (the C^1 core of Theorem 1 is unconditional; only the H^1 extension chain is
touched, which already carries NG-3).

**Repair path.** Either restate (D') as the direct hypothesis "(D'') Omega_up is a Lipschitz
domain" (transversality then a REMARK about when to expect it), or keep (D') and add the
two-paragraph flattening proof or a citation covering Lipschitz-dihedral domains; fold the
residual into NG-3 (which already owns the corner arguments) so the register carries it.

**Rejecting test.** A citation whose stated theorem is exactly (D') => Lipschitz for Lipschitz
pieces (if produced, the objection reduces to "add the citation", a nano-repair).

---

### R2-O7 (P3, DEGENERATE-BAND QUANTIFIER) — Pi_T and Pi_box degenerate as T_1 -> T_max: 3b quantifies over a possibly EMPTY strength band, Pi_box = sup(empty set) is undefined, and the monitor's band edge min(Pi*, Pi_box) loses meaning — the case is never named

**Claim attacked.** Strength-band definitions (lines ~687-698): Pi_T := T_max/T_1;
Pi_box := sup{ Pi in (1, Pi_T] : ... }; 3b(i) "for every pre-state 1 in the (G3) box and every Pi
in (1, Pi_T]"; 3b(iii)'s two-case split; monitor (M-b) "below the priced band edge
min(Pi*, Pi_box) p_1".

**Defect.** For pre-states with T_1 = T_max (admissible: the (G3) box is closed), Pi_T = 1 and
(1, Pi_T] is EMPTY: 3b(i) is vacuously true, the set defining Pi_box is empty and its sup is
undefined (or -infinity), the two-case split of 3b(iii) presupposes M_s(Pi_box) exists, and
(M-b)'s band edge is undefined. For T_1 near T_max the band (1, Pi_T] is nonempty but collapses:
Pi* (which is bounded BELOW by the strictly-positive-threshold statement, Pi* - 1 > 0 pinned by
delta) eventually exceeds Pi_T, so the "band-edge saturation" state of 3b(iii) is the GENERIC
state for hot pre-states, and the monitor semantics there ("alarm on approach to min(Pi*, Pi_box)
-> 1^+") degenerate to a permanent alarm — operationally meaningful only if declared. The r1
repair of O-2/O1 introduced these caps correctly but never closed the quantifier at the hot end of
the box. This is the same defect class r1 itself fixed elsewhere ("the complementary case now
named, per O-2") — applied one level down.

**Rigor class of objection**: complete (quantifier arithmetic on the document's own definitions).

**Severity**: P3 (no false statement — a vacuous one plus an undefined sup; but (M-b) is a
monitor spec that F2 will implement, and sup(empty) is exactly the kind of edge a harness hits).

**Repair path.** One sentence in 3.1: "If Pi_T = 1 (pre-state at the hot box edge) set
Pi_box := 1 and declare the band EMPTY; the monitor state is then band-collapse (a reportable
state distinct from band-edge saturation), and all Pi-quantified statements of 3b/3c are vacuous
by convention." Plus the corresponding branch in the (M-b) spec and in the Theorem 3 falsifier
harness (which otherwise draws Pi from an empty interval).

**Rejecting test.** Show (G3) as consumed by the pipeline in fact bounds interface pre-state
temperatures strictly away from T_max with a margin that keeps Pi_T >= some Pi_min > 1 (then the
degenerate case is unreachable and the repair is a one-line remark citing that bound).

---

### R2-O8 (P3, MODELING STEP UNFLAGGED) — The Pi* pricing applies a pointwise 1-D uniform-pre-state theorem to a nonuniform interface patch: which scalar M_x feeds the monitor is unstated, and the transverse-averaging step is not named as a modeling assertion

**Claim attacked.** 3.4(3)(b) "a computable finite-amplitude admission price Pi*(M_x)"; (M-b)
"downstream overpressure below ... min(Pi*, Pi_box) p_1"; Section 5 "prices the excluded
normal-front band".

**Defect.** Theorem 3 is proved for a UNIFORM pre-state W_1 filling a 1-D duct (3.3: "constant
speed U_s", frozen-coefficient idealization — correctly declared there). The interface pre-state
of the contract is a per-phase PROFILE: M_x = M_x(patch point), p_1 = p_1(patch point), varying
across Gamma_d and with phase xi. The monitor spec (M-b) uses the symbols Pi*, p_1 as scalars
without stating the reduction: is the priced band computed from inf_patch M_x (conservative),
from the pointwise field with the alarm on the worst point (equivalent), or from some average
(wrong — a front can breach where the local threshold is lowest while the average looks safe)?
The safe choice is obvious (pointwise/inf), but it is a CHOICE, it is nowhere written, and the
step "a normal front over a transversely nonuniform pre-state breaches where the local 1-D
threshold is crossed" is itself a modeling assertion (the front is a connected surface; its
dynamics over a nonuniform state is not the 1-D theorem — this is NG-2-adjacent but distinct:
NG-2 owns obliqueness of the FRONT; this is nonuniformity of the STATE under a normal front).
Choice-adjudication discipline (memory `choice-adjudication-convergence`) applies: an algorithmic
choice point consumed by a monitor spec must be adjudicated on the record.

**Rigor class of objection**: complete for the under-specification claim (grep: no occurrence of
inf/min-over-patch language in (M-b) or 3.4(3)(b)); modeling assertion for the breach-locality
clause.

**Severity**: P3.

**Repair path.** One sentence in (M-b): "Pi* and p_1 are evaluated POINTWISE on the patch per
phase; the monitored band edge is inf over the patch of min(Pi*, Pi_box) p_1; the pointwise
reduction of the nonuniform-state normal-front problem is a PRACTICE-class assertion recorded
here, sharing NG-2's discharge path (leading-point analysis)."

**Rejecting test.** Exhibit an existing pin (M0 or choice ledger) fixing the patch reduction for
threshold monitors (navigation-first search of the choice ledger for a min-over-patch row; if a
row exists, the objection reduces to a cross-reference fix).

---

### R2-O9 (P3, CONSUMPTION POINTER MISSING) — Theorem 2(b)'s "response ... to ANY downstream modification (nozzle contour change, back-pressure representation, exit closure) is ZERO" invites the NONLINEAR design-space reading that is exactly NG-1-gated

**Claim attacked.** Theorem 2(b), closing sentence (lines ~588-590).

**Defect.** Within the linearized statement the sentence is true (downstream data/forcing do not
enter the upstream estimate). But its exemplars — "nozzle contour change", "exit closure" — are
DESIGN-SPACE modifications: the reading every design consumer will take is "the upstream
per-phase FIELD (the nonlinear base) is invariant under downstream redesign", which is the
NONLINEAR upstream-determination statement, i.e., precisely the Remark 2.3 content that r1 itself
downgraded to SCHEMA with the gap NG-1. The sentence carries no pointer; two paragraphs later the
document is scrupulous ("The per-phase rung-2 consumption of the NONLINEAR statement must cite
NG-1 until discharged"), but the quotable sound-bite sits inside a THEOREM-labeled block with
design-space language. This is a documentation-hygiene defect of exactly the kind the repo's R4/R5
discipline polices (a claim whose natural consumption exceeds its proof, one pointer away from
honest).

**Rigor class of objection**: complete (textual; the linear/nonlinear gap is the document's own
Remark 2.3).

**Severity**: P3.

**Repair path.** Append to the sentence: "(linearized statement; for the nonlinear design-space
reading cite NG-1, Remark 2.3)".

**Rejecting test.** None needed beyond the text itself; the objection dies only if the sentence
already carries the pointer (it does not).

---

### R2-N (minor list, N-severity)

 (N-a) **Corollary 4 falsifier, fourth leg**: "must remain STABLE at fixed resolution with bounded
       growth O(1 + |r|) per transit". In this BC pair there is exactly ONE reflection (R_- exits
       at x = 0 into prescribed-R_+ territory; no loop — the document's own Claim (i) proof).
       "Per transit" growth language describes a compounding process that cannot occur; as a PASS
       predicate it is loose in the dangerous direction (a scheme with spurious numerical
       re-reflection at x = 0 compounding |r| per transit could still pass at small |r| and fixed
       T). Repair: "total growth <= C(1 + |r|) uniformly in run time after the single reflection;
       any secular growth rejects the scheme's boundary implementation".
 (N-b) **Lemma 2.2(a)'s hedge** "up to the nonvanishing factor coming from the variable
       normalization" is unnecessary and slightly wrong in direction: the V -> U change
       (sigma = rho' - p'/c^2) is unipotent (triangular, unit diagonal), so det A^U(xi) =
       det A^V(xi) EXACTLY, no factor. One-word fix; as written it invites a reader to expect a
       state-dependent factor that does not exist.
 (N-c) **Corollary 4 rigor-line vs table**: the rigor line "THEOREM ... quadrants (b), (c), (d)"
       silently excludes (a) while the table asserts (a) — internal inconsistency; subsumed by
       R2-O3 but independently a lint-class defect (a rigor declaration that does not cover a
       displayed claim).
 (N-d) **(M-b) measurement point unstated**: "downstream overpressure" — measured where and in
       which frame (interface trace? plenum? peak over the phase?) is unspecified in the monitor
       spec; subsumed operationally by R2-O8's repair sentence.
 (N-e) **Register row 1 hypothesis column** lists "(D') for the extension" but not the collar
       issue of R2-O2; after the R2-O2 repair the row should cite Theorem 1' and (M-c)'s domain
       explicitly.

---

## B. ATTACKS ATTEMPTED AND FAILED (verification record — honest accounting)

Each item below was re-derived by hand in this round with intent to break it; all PASSED. These
are certificates FOR the r1 text, reported per the dual-proof standard.

 1. **3b(i) localization** (the r1 centerpiece): endpoint algebra re-derived — at T_2 = Pi T_1,
    R T_2/p_2 = 1/rho_1 exactly, bracket = 2/rho_1, phi(Pi T_1) = Int_{T_1}^{Pi T_1} c_v dt > 0;
    phi(T_1) < 0; compressivity equivalence T_2 < Pi T_1 <=> rho_2 > rho_1 checks; mass-flux
    reconstruction sign checks. Sound.
 2. **3b(ii) sharpening**: rho_1/rho_2 = T_2/(Pi T_1) > 1/Pi => 1 - rho_1/rho_2 < (Pi-1)/Pi =>
    M_s^2 > Pi/gamma_1. Sound.
 3. **Crossing identity + anchor**: Pi* - 1 = gamma_1 M_x^2 (1 - rho_1/rho_2)|_{Pi*}; upper band
    Pi* < gamma_1 M_x^2; gamma-const anchor Pi*(2) = 4.5 < 5.6. All re-derived. Sound.
 4. **(BQ) and the B_L characteristic-variable evaluation** (Cor 4): S A(n) symmetry, the
    2 p'(u'.n) cross term, and the R_± expansion rho_0(R_+^2 + R_-^2)/2, rho_0 c_0(R_+^2 -
    R_-^2)/2 — all re-computed. Sound.
 5. **No-resonance step** (Lemma 2.2(c)): u.xi = 0 forces Mach factor = -c^2|xi|^2 < 0. Sound,
    and indeed stronger than the retracted r0 hedge.
 6. **Pencil diagonalizability bound**: R^T (S A_1) R = I => cond(R) = sqrt(lambda_max/lambda_min
    (S A_1)) <= sqrt(s_max (u_x + c) / (s_min (u_x - c))), eta-uniform since S A_1 is
    eta-independent. Sound.
 7. **Corrected discriminant predicate** (Thm 2 falsifier (i)) incl. the counterexample draw
    u = (0.5c, 0.9c, 0), eta = (1,0): 0.81 c^2 > 0.75 c^2, real roots. Sound.
 8. **Lemma 2.1 extremality**: d(psi).e_1 = cos alpha cos theta + sin alpha sin theta cos psi,
    minimized at cos psi = -1; equivalence chain through cos(theta + alpha) > 0 valid on the full
    range (cos < 0 on (pi/2, 3pi/2) covers theta + alpha up to pi + pi/2). Sound.
 9. **Quadrant (d) witness**: R_- determined by data + r = 0 trace; R_+ un-pinned at inflow;
    infinite-dimensional affine solution family; ¬R1 via (ii)b. Sound. The r0 retraction is
    correct: every finite r is Hadamard well-posed in the 1-D model (one-reflection structure).
10. **Schur continuity remark** (Lemma 0.2), **wall annihilation** (Lemma 1.3), **(ii') sign
    argument** (good-sign boundary term), **Theorem 2(b) wall-term vanishing via (H2.3) without
    n_x = 0**: all check. Sound.
11. **Gruneisen one-liner**: G = R/c_v(T), positive and bounded by (G2). Sound.
12. **Meridional discriminant** (Remark 2.4): c^2 xi_r^2 (u_x^2 + u_r^2 - c^2). Sound, and the
    scoping of the iff is the correct fix of round-1 O4(P2).

---

## C. VERDICT

The r1 mathematics that was attacked in round 1 has been repaired competently: every load-bearing
computation re-derived this round is sound, and the r1 label discipline (SCHEMA downgrades, named
gaps NG-1..NG-8, capped quantifiers) is largely honest. The remaining NEW defects are
concentrated where the document TOTALIZES — the Section 5 composite and the Corollary 4 truth
table — and they are consumption/label defects with named, cheap repairs, plus one applicability
gap (R2-O2) whose repair (collar localization) strengthens the result using tools already in the
document. Nothing found this round breaks a core proof.

**VERDICT: REPAIRABLE** (not SOUND-AS-LABELED: the composite clause (ii) consumes an uncertified
volume hypothesis (R2-O1), clause (i) as worded is vacuous on the device data class absent the
collar form (R2-O2), and truth-table row (a) carries an existence clause under no rigor label
(R2-O3); not BROKEN: every defect has a stated repair that preserves the document's architecture
and conclusions).

*Deliverable authored 2026-08-17, round 2, lens = hyperbolic-systems rigor; raws directory keyed
by session date-of-record 2026-08-13 per the target document's own bookkeeping declaration.*
