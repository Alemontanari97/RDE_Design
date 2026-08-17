# ADVERSARIAL REFUTATION — Round 1, lens 0 (hyperbolic-systems rigor)

**Target**: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md` (Phase D, L4 => R1 composite).
**Lens**: eigenstructure / symmetrizer / energy estimate / boundary-condition count, plus ABSENCE attacks.
**Refuter discipline**: every objection below carries (i) the exact target line/claim, (ii) a refutation
class (PROOF-GAP / FALSE-STATEMENT / CITATION-MISMATCH / SCOPE-GAP / FALSIFIER-DEFECT / LABEL-VIOLATION /
ABSENCE), (iii) the rigor class of MY demonstration (complete proof / sketch / audit assertion), and
(iv) a **rejecting test for the objection itself** — the concrete evidence that would kill MY attack.
Function spaces named where load-bearing. Notation follows the target document.

**Round-1 verdict (summary)**: the linear/steady core — Lemmas 0.1-0.2, 1.1-1.3, the (EI) energy
identity, Theorem 1's Gronwall argument, Lemma 2.1-2.2's algebra, Theorem 2(a)-(b), Theorem 3a, the
Gamma_fund formula, Corollary 4 quadrants (b)-(c) — SURVIVES direct attack (see Section S, verified-
algebra log). But the document is NOT sound as labeled: I find **one demonstrated proof gap in a claim
labeled "THEOREM (complete)"** (O-1), **one hypothesis-domain inconsistency that falsifies the labels
of 3b/3c as stated** (O-2), **one load-bearing citation that does not cover the claimed statement**
(O-3), **one SCHEMA sketch whose conclusion is provably false in its own model class** (O-4), **one
self-contradictory falsifier that rejects correct implementations** (O-5), and **one scope gap between
the consumed L4 statement (Gamma_d = axisymmetric SURFACE, verified in M0 [D-CONTRACT] lines 116-117)
and the proved statement (planar interface)** (O-6), plus six lower-severity objections and a nit
list. All repairs are named and cheap. Overall: **REPAIRABLE**, not SOUND-AS-LABELED, not BROKEN.

---

## O-1. Theorem 3b(i) "RH solvability for every strength" — PROOF-GAP in a claim labeled THEOREM (complete): the IVT root need not be a realizable front

**Target**: Section 3.2, Theorem 3b(i), lines ~536-542.
**Refutation class**: PROOF-GAP. **My demonstration: complete proof.** **Severity: HIGH** (the
statement is true, but the written proof does not prove it; the label "THEOREM (complete)" fails).

The proof defines phi(T_2) := h(T_2) - h(T_1) - (1/2)(p_2 - p_1)(1/rho_1 + R T_2/p_2), shows
phi(T_1) < 0 and phi(+infinity) = +infinity, and concludes by IVT that a root T_2 in (T_1, infinity)
exists, calling the result "a post-state 2 solving (RH)".

**The gap.** A root of the Hugoniot equation alone is NOT an RH solution. Reconstructing the front
requires a real mass flux: from mass+momentum (the document's own eliminated relation),

    rho_1 v_1^2 = (p_2 - p_1) / (1 - rho_1/rho_2),

which demands rho_2 > rho_1 when p_2 > p_1 (else v_1^2 <= 0 and no real v_1 exists). With
rho_2 = p_2/(R T_2), the condition rho_2 > rho_1 is **T_2 < Pi T_1**. The IVT as written locates a
root somewhere in (T_1, infinity); a root in [Pi T_1, infinity) would satisfy the Hugoniot equation
and reconstruct **no front at all**. The proof never excludes this; as written it is not a proof of
(i). (The subsequent parts lean on (i): (ii) assumes a compressive RH solution, (iii) parametrizes
the family produced by (i), and 3.3 consumes the constructed W_2. So the gap sits upstream of the
whole finite-amplitude section.)

**The repair (I supply it; two lines).** Evaluate phi at the endpoint T_2 = Pi T_1, where
rho_2 = rho_1 and 1/rho_1 + R T_2/p_2 = 2/rho_1:

    phi(Pi T_1) = Int_{T_1}^{Pi T_1} c_p(t) dt - (p_2 - p_1)/rho_1
                = Int_{T_1}^{Pi T_1} c_p(t) dt - R T_1 (Pi - 1)
                = Int_{T_1}^{Pi T_1} [c_p(t) - R] dt = Int_{T_1}^{Pi T_1} c_v(t) dt
                >= c_v,min T_1 (Pi - 1) > 0.

With phi(T_1) < 0, IVT on the COMPACT interval (T_1, Pi T_1) gives a root there, hence
rho_2 > rho_1 automatically (compressivity for free — this also strengthens (ii), whose compressive
hypothesis becomes a conclusion). The theorem is true; the of-record proof must contain this endpoint
evaluation to earn "THEOREM (complete)".

**Rejecting test for O-1**: exhibit the line of Section 3.2 that bounds the IVT root below Pi T_1 or
otherwise establishes rho_2 > rho_1 within part (i). (I searched; the words "rho_2 > rho_1" occur
only as an assumption in (ii), flagged "as admissibility under (G4) requires" — admissibility of a
front presupposes the front exists, which is what (i) was supposed to deliver.)

---

## O-2. Theorem 3b / 3c hypothesis-domain inconsistency — LABEL-VIOLATION: (G2)/(G3)/(G4) live on a compact box, the proofs run T_2 -> infinity

**Target**: Section 0 (G2), (G3), (G4); Theorem 3b(i) tail estimate, 3b(ii) "-> infinity as
Pi -> infinity", 3b(iii) monotonicity "on (1, infinity)"; Section 3.3 "U(delta) NONEMPTY for every
delta"; register rows 3b/3c.
**Refutation class**: LABEL-VIOLATION + SCOPE-GAP. **My demonstration: audit assertion with the
contradiction exhibited.** **Severity: HIGH** (labels), MEDIUM (mathematical content — repairable by
restating hypotheses).

(G2) declares e in C^2 **on the working temperature interval [T_min, T_max]**, with c_v bounds on
that interval; (G3) is a compact state box; (G4) demands Gamma_fund >= Gamma_min "on the working
box". But:

1. 3b(i)'s tail estimate "as T_2 -> infinity, phi(T_2) >= c_p,min (T_2 - T_1) - C - ..." uses
   c_p,min on an UNBOUNDED interval. Under (G2) as written, h(T_2) is not even defined for
   T_2 > T_max. The claim "for every Pi > 1 there exists a post-state" is, under the stated
   hypotheses, not a theorem: for Pi large enough the root T_2 (which the O-1 repair localizes in
   (T_1, Pi T_1), still unbounded in Pi) exits [T_min, T_max].
2. 3b(iii)'s strict monotonicity of M_s over Pi in (1, infinity) invokes Bethe-Weyl/Menikoff-Plohr
   along the ENTIRE Hugoniot — which leaves the (G4) box for large Pi, where Gamma_fund is not
   hypothesized at all.
3. 3c ("U(delta) nonempty for EVERY delta"; "strengths are unbounded") inherits both. As labeled
   (THEOREM / THEOREM* under (G1)-(G4)), these statements quantify over states on which their own
   hypotheses are silent.
4. Operational corollary the document should own: the tabulated backend (repo standing directive,
   `thermo-tabulated-backend`) covers a finite T range; for a large margin M_x the threshold
   Pi*(M_x) grows like M_x^2, and the "priced exclusion band Pi < Pi*" can exit the certified EOS
   validity range — at which point the monitor's price is a number the model of record cannot
   certify. The falsifier for Theorem 3 (1-D run at given Pi) cannot be executed there either.

**Repair (either one suffices; declare which):**
- (G2') strengthen: e in C^2 on [T_min, infinity) with 0 < c_v,min <= c_v(T) <= c_v,max globally
  and (G4) global — then all of 3b/3c go through verbatim (with O-1's endpoint repair). Honest cost:
  (G2') is a MODELING ASSERTION about the gas beyond the tabulated range and must be classed
  PRACTICE, downgrading 3b(iii)/3c from THEOREM*/THEOREM to "THEOREM under (G2'), PRACTICE at the
  table boundary"; or
- Cap the quantifier: restate 3b/3c for Pi in (1, Pi_max(T_max)] with Pi_max defined by
  T_2(Pi_max) = T_max, and restate 3c as "U(delta) nonempty whenever Pi*(M_x) < Pi_max" — with the
  complementary case (margin so large that every in-model front is excluded) NAMED as a scope
  boundary, not silently absorbed.

**Rejecting test for O-2**: exhibit the clause extending (G2)/(G4) beyond [T_min, T_max]. There is
none: line 53 says "on the working temperature interval", line 59 says "on the working box", and
lines 540-541 use c_p,min at T_2 -> infinity.

---

## O-3. Remark 2.3 (nonlinear per-phase class) — CITATION-MISMATCH: the load-bearing citation is one-dimensional; the claimed problem is multi-D with a characteristic boundary

**Target**: Remark 2.3, lines ~452-461; register row 2b ("nonlinear class THEOREM* (Li/C-F cited)");
Section 5 assembly ("(ii) the steady per-phase class").
**Refutation class**: CITATION-MISMATCH. **My demonstration: audit assertion (checkable against the
cited texts' tables of contents/theorem statements).** **Severity: HIGH for the THEOREM* label**,
because the remark itself declares "cited semiglobal theory is load-bearing", and this is "the
statement consumed per-phase by the rung-2 objective" — i.e., a consumed brick.

Li Ta-tsien, *Global Classical Solutions for Quasilinear Hyperbolic Systems*, Ch. 1 develops
semi-global classical solutions for quasilinear hyperbolic systems in **one space dimension**
(u_t + A(u) u_x = F, boundary/Goursat problems on a strip in the (t, x) plane). The problem Remark
2.3 claims — steady 3-D Euler x-marching in a duct Omega_{[x_0,x_I]}, i.e., a QUASILINEAR symmetric
hyperbolic system with x time-like and **two** transverse space dimensions, with a **characteristic
boundary** (slip wall: u.n = 0 makes the boundary matrix A(n) singular, kernel dimension 3) — is not
in that theory. Courant-Friedrichs §V (MOC) is 2-D/axisymmetric-by-symmetry, constructive, and not a
well-posedness theorem in the stated class either. The correct theory for the claim is the
characteristic-boundary quasilinear IBVP literature (Rauch-Massey CPAM 1974 for linear/semilinear
tame estimates; Gues, Comm. PDE 1990; Secchi, Arch. Rational Mech. Anal. 1996, "Well-posedness of
characteristic symmetric hyperbolic systems"), which requires (and here HAS — see below) a
constant-rank boundary matrix, imposes compatibility conditions on the data at omega(x_0) ∩ wall,
and delivers solutions in anisotropic spaces (normal-derivative loss: H^m_tan-type spaces, not plain
H^m). None of this is cited or acknowledged; "transfers verbatim" (uniqueness in the class + finite
domain of dependence) additionally sweeps the piecewise-smooth S1 sub-class (fronts!) into a smooth-
solutions citation — linearized energy arguments do not cross base-state discontinuities without
RH-transmission terms.

**What survives**: the INPUTS the remark says it contributes (symmetrizer, direction count) are
indeed complete; and the slip wall does satisfy Secchi's constant-rank condition (A(n) at the wall
has eigenvalues {-c, 0 x3, +c}, rank 2 constant along Gamma_w) — so the repair is a citation swap
plus a class restriction, not a retraction:

**Repair**: re-cite (Rauch-Massey / Gues / Secchi + compatibility conditions) for the smooth
sub-class; restrict the claim to the smooth-in-x-slab sub-class of S1 or add a separate front-
tracking/transmission clause for piecewise-smooth members; keep THEOREM* only after the swap.
Downgrade to SCHEMA until then.

**Rejecting test for O-3**: produce a theorem statement in Li Ch. 1 (or C-F §V) covering quasilinear
symmetric hyperbolic systems in 1+2 dimensions with characteristic boundary of constant multiplicity.
(Li Ch. 1's standing assumption is one space variable; this test fails on the book's own setup.)

---

## O-4. Corollary 4 quadrant (d) — FALSE-STATEMENT inside a SCHEMA: the proposed ¬R1 ∧ ¬R2 witness is in fact well-posed for every finite r

**Target**: Corollary 4(d), lines ~727-732.
**Refutation class**: FALSE-STATEMENT (of the sketch's conclusion, in the document's own model
class). **My demonstration: complete proof (explicit solution).** **Severity: MEDIUM** — declared
"not load-bearing for the corollary" (the independence needs only (b), (c), which stand), but an
of-record truth table with a false quadrant entry is a defect, and the SCHEMA label does not shield
a refutable claim: SCHEMA = gap in the proof, not falsity of the statement.

The claim: an active termination with r^2 > (u_0 + c_0)/(c_0 - u_0) yields ¬R2 ("no uniform energy
estimate of Claim (i)'s form; a genuinely active Z"). The hedge admits full Hadamard ill-posedness
"needs a normal-mode/Kreiss argument, standard but not spelled out" — implying it would succeed.
It would not: **the problem is Hadamard well-posed for EVERY finite r.**

*Proof.* The model is the constant-coefficient decoupled pair
(d_t + (u_0 + c_0) d_x) R_+ = 0, (d_t + (u_0 - c_0) d_x) R_- = 0 on (0, L), plus advected sigma
(and shear), with incoming data prescribed at x = 0 (R_+, sigma) and the closure
R_-(L, t) = r R_+(L, t) at x = L. Solve by characteristics: R_+ is determined on all of
(0, L) x (0, T) by its initial and x = 0 data alone (it never meets the closure as an unknown);
then R_-(L, t) is explicitly determined; then R_- is determined everywhere by rightward-in-time
transport from x = L and its initial data, exiting at x = 0 where it is outgoing (no condition —
correct count). There is **no reflection loop**: the inflow condition prescribes R_+ independently
of R_-. Existence and uniqueness are constructive; continuous dependence holds with
||U(t)||_{L^2(0,L)} <= C(1 + |r|) ( ||U(0)||_{L^2} + ||data||_{L^2(0,t)} ) for all t <= T — a
Hadamard estimate for every finite r, growth constant polynomial in |r|, no exponential blow-up in
the data map. Equivalently: the boundary condition is of the form "incoming = r x outgoing" at each
end, which satisfies the (1-D, noncharacteristic) uniform Kreiss-Lopatinskii condition for every r;
the Kreiss argument the sketch defers to would PROVE well-posedness, not refute it. QED.

What actually fails for |r| large is only the SPECIFIC maximal-dissipative estimate of Claim (i)
(B_L >= 0 with THIS symmetrizer). Failure of one energy method is not ¬R2, and the document's own
definition of R2 in the corollary is well-posedness of the patch problem, not dissipativity.

**Repair (witness that works, same model class):** keep the subsonic base (¬R1 by Claim (ii)(b))
and take a MISCOUNTED closure: prescribe the outgoing invariant R_-(0, t) = b(t) at the inflow while
leaving R_+ unprescribed there. Then R_+ is undetermined on the triangle
{x < (u_0 + c_0) t}: uniqueness fails (any incoming profile is a solution) — genuine ¬R2 by
direction-count violation, and ¬R1 persists. Alternatively prescribe both R_+ and R_- at x = 0:
existence fails generically (over-determination), same conclusion. Either fills quadrant (d) with a
complete proof and no Kreiss machinery.

**Rejecting test for O-4**: exhibit initial/boundary data for the document's active-r closure with
no solution, two solutions, or a sequence violating continuous dependence at fixed T. The explicit
construction above shows none exists.

---

## O-5. Theorem 2 falsifier (i) — FALSIFIER-DEFECT: the stated PASS predicate rejects correct implementations (R5 violation: the rejector rejects truth)

**Target**: Section 2 falsifier, lines ~462-465; register row 2a last column.
**Refutation class**: FALSIFIER-DEFECT. **My demonstration: complete proof (counterexample draw).**
**Severity: HIGH under repo R5** — this is an of-record rejecting test whose PASS criterion is
mathematically wrong; if implemented as written it would either misfire on correct code or be
silently "fixed" ad hoc at implementation time, both R5 failures.

The text states two incompatible criteria in one sentence: "PASS iff complex roots occur exactly
when u_x < c and u_perp.eta small" and "(classification must match the predicate u_x > c on every
draw; a single mismatch rejects)".

The correct classification, from the document's OWN discriminant (line ~372-373):

    complex roots  <=>  (u_perp.eta)^2 + (u_x^2 - c^2)|eta|^2 < 0
                   <=>  u_x < c  AND  (u_perp.eta)^2 < (c^2 - u_x^2)|eta|^2.

**Counterexample draw**: u = (0.5 c, 0.9 c, 0), eta = (1, 0) (aligned with u_perp). Then
discriminant/4 = c^2 [ (0.9 c)^2 + (0.25 - 1) c^2 (1) ] = c^2 (0.81 - 0.75) c^2 > 0: roots REAL
with u_x < c. A correct implementation returns "real" on this draw; the stated predicate
("match u_x > c on every draw") declares a mismatch and REJECTS the correct code. Conversely the
first clause's "u_perp.eta small" is unquantified — not a predicate at all. A falsifier whose PASS
condition is false cannot reject the theorem; it can only reject implementations of the theorem's
truth.

**Repair**: the per-draw predicate is the sign of the discriminant expression itself —
"complex iff (u_perp.eta)^2 < (c^2 - u_x^2)|eta|^2 with u_x < c" — and the AGGREGATE check
"some eta with complex roots exists iff u_x < c" (verified by drawing eta from the orthogonal
complement of u_perp, per the proof of 2.2(c)). Both are exact, drawable, and rejecting.

**Rejecting test for O-5**: show the draw above is excluded by the falsifier's sampling rule. It is
not — "random states and eta directions" includes it with positive probability.

---

## O-6. Planar interface vs Gamma_d as axisymmetric surface — SCOPE-GAP between the consumed L4 statement and every proved theorem

**Target**: Geometry (D) (lines ~123-127); Theorem 1 statement; Section 5 composite (lines ~758-774);
the document's own [D-CONTRACT] quote (lines 16-22).
**Refutation class**: SCOPE-GAP / ABSENCE. **My demonstration: audit assertion, verified against M0.**
**Severity: MEDIUM-HIGH** (composite-level overstatement; cheap repair).

Verified at source: M0 [D-CONTRACT] D2.4 (lines 116-117 of `docs/rde_nozzle_MASTER.md`) defines
Gamma_d as "a fixed axisymmetric surface downstream of all heat release" — NOT a plane; the
L4-DEFAULT block (M0 lines 125-137) says "every patch of Gamma_d axially supersonic with margin"
with the u_x - c >= delta certificate. The document proves every theorem for the PLANE {x = x_I}
(Geometry (D): "interface station x_I"; every boundary integral uses n = e_1).

For a curved axisymmetric patch with unit normal n != e_1 (n = (n_x, n_r), n_x < 1), the causal-
separation/pure-outflow property of the surface requires the NORMAL margin u.n - c >= delta'
(Lemma 1.2 is already stated for general n — the document's own machinery says so). The axial
certificate does NOT imply it: u.n = u_x n_x + u_r n_r can be < c with u_x - c >= delta whenever
the patch is tilted and the meridional velocity misaligned (e.g., u = (c(1 + delta/c), 0, 0),
n = (cos 40°, sin 40°, 0): u.n = 1.0 delta-ish x 0.766 c < c). Hence the Section 5 composite —
"On the L4 default (every patch of Gamma_d axially supersonic with margin ...), causal separation R1
holds BY THEOREM" — is proved only for the planar-Gamma_d sub-case, and the document nowhere says
so. This is exactly the kind of silent quantifier narrowing the Phase D batch exists to catch.

**Repair (pick one, one paragraph):**
1. Cite a planarity pin if one exists in M0/D-docs (I did not find one in [D-CONTRACT]; the burden
   is on the document to anchor it); or
2. Restate the consumed hypothesis as the NORMAL margin u.n - c >= delta on each patch — every
   Section 1 proof then goes through verbatim with n in place of e_1 (Lemmas 1.1-1.3 are already
   general-n), Theorem 2's x-marching keeps the axial form on the planar stations it actually uses;
   plus a remark that for planar patches normal margin = axial margin, and that for curved patches
   the axial certificate must be strengthened or the tilt bounded (u.n - c >= u_x n_x + u_r n_r - c,
   an explicit checkable lower bound given the surface geometry).

**Rejecting test for O-6**: an M0/D-doc anchor declaring Gamma_d planar of record (or the data-class
declaring the certificate as normal-margin). Absent that, the objection stands as stated.

---

## O-7. Remark 1.5.3 rough-solution extension — THEOREM* whose citation does not reach the actual geometry (characteristic wall + corners); Omega_up Lipschitz-ness unhypothesized

**Target**: Remark 1.5.3; (H1.4); Geometry (D).
**Refutation class**: CITATION-MISMATCH (mild) + ABSENCE. **My demonstration: sketch.**
**Severity: LOW-MEDIUM** (the C^1 core is complete and honestly separated; only the extension label
is over-credited).

Two gaps in the extension clause "by mollification in (x, t) tangentially to the boundary ...
(Friedrichs mollifier lemma, cited)":
1. Gamma_w is a CHARACTERISTIC boundary (u-bar.n = 0 => A(n) singular on the wall). The Friedrichs
   commutator/mollifier argument for passing (EI) to the H^1 class is stated in the classical
   sources for noncharacteristic (or boundaryless) settings; near a characteristic wall the correct
   statement needs the tangential-mollification argument of the characteristic-IBVP literature
   (Rauch 1985, Trans. AMS 291, symmetric positive systems with characteristic boundary of constant
   multiplicity — which the slip wall satisfies, rank 2 constant). The repair is a citation swap,
   but as cited the load-bearing lemma does not cover the wall.
2. The energy identity on Omega_up integrates by parts over a domain whose boundary is
   Gamma_in ∪ Gamma_w ∪ {x = x_I} with CORNERS (wall ∩ interface plane). For the divergence theorem
   with L^2 traces, Omega_up must itself be Lipschitz: this requires transversality of Gamma_w and
   {x = x_I}, which is generic for a duct but is a geometric HYPOTHESIS, nowhere stated (a wall
   tangent to the interface plane produces a cusp and the trace/divergence package degrades).

**Repair**: add "(D+): Gamma_w meets {x = x_I} transversally (uniformly Lipschitz Omega_up)" and
re-cite Rauch 1985 for the characteristic-wall mollification. Keep THEOREM* after that.

**Rejecting test for O-7**: a statement of the Friedrichs mollifier lemma covering Lipschitz domains
with characteristic boundary portions and corners, as cited (Friedrichs 1954 / B-G&S Ch. 1-2). The
cited forms are interior/noncharacteristic; the test fails.

---

## O-8. Register row 3d falsifier = "n/a" — LABEL-VIOLATION of the document's own header claim and repo R5

**Target**: header line ~10-11 ("Every statement carries hypotheses, rigor class, gamma(T) status,
and a rejecting falsifier (Section 6 table)"); register row 3d.
**Refutation class**: LABEL-VIOLATION. **My demonstration: audit assertion (direct contradiction).**
**Severity: LOW-MEDIUM** (discipline, not mathematics — but it is the document's own bar).

Row 3d declares "n/a (meta-statement)". The header quantifies over ALL statements. Moreover 3d is
NOT untestable: its content ("outside linearization by amplitude >= Pi* - 1; weak fronts covered by
the linear picture") admits an executable rejecting test — an amplitude scan: 1-D margin base,
downstream pulses of increasing strength Pi; PASS iff the upstream response stays within the
linear-theory band (Theorem 1's discretization bound) for Pi < Pi*(M_x) and departs from it at an
O(1) rate for Pi > Pi*, with the crossover localized at Pi* within a refinement-shrinking band.
This simultaneously tests 3d's two scope claims and the 3b threshold (complementing the existing
Theorem 3 falsifier, which tests trajectory, not linear-band exit).

**Repair**: put the amplitude-scan test in row 3d, or weaken the header sentence.
**Rejecting test for O-8**: none needed beyond reading the two lines; the contradiction is literal.

---

## O-9. The "classical package" (Bethe-Weyl / Menikoff-Plohr / Smoller) — cited scope under-specified: (G4) alone is presented as the sufficient condition

**Target**: Section 3.1 last paragraph; 3b(iii); 3.3 uniqueness clause; register rows 3b/3c;
Cited-results block.
**Refutation class**: CITATION-MISMATCH (under-specification). **My demonstration: audit assertion.**
**Severity: LOW-MEDIUM** (the package almost certainly holds for THIS gas class, but not by the
stated hypothesis alone; the missing verifications are one-liners that must be of record).

1. Menikoff-Plohr's global Hugoniot results (monotone parametrization, Lax admissibility,
   compressivity) use convexity Gamma_fund > 0 TOGETHER WITH auxiliary "weak" EOS conditions —
   notably Gruneisen coefficient G := v (dp/de)_v > 0 (and bounded) — not Gamma_fund > 0 alone.
   For the thermally-perfect frozen gas G = R/c_v(T) in [R/c_v,max, R/c_v,min], positive and
   bounded by (G2): the check COSTS one line, but that line is absent, and (G4) is advertised as
   the sufficient condition ("Under (G4), the gas is of Bethe-Weyl convex type: ...").
2. Smoller Ch. 17-18's uniqueness discussion is developed for gamma-law gas dynamics / p-systems;
   the single-front Riemann uniqueness for the gamma(T) gas at ARBITRARY strength should be anchored
   to the convex-EOS wave-curve construction (Menikoff-Plohr §V under Gamma > 0, G > 0) rather than
   to the gamma-law chapters. Same fix.
3. Note the interaction with O-2: both citations are being applied along Hugoniot arcs that exit
   the (G) box; the auxiliary conditions must be hypothesized wherever the arc lives.

**Repair**: add "Lemma 3.0: G = R/c_v in [R/c_v,max, R/c_v,min] > 0 under (G1)-(G2)" and re-scope
the citation sentence to "under (G4) + Lemma 3.0 (+ (G2') per O-2)".
**Rejecting test for O-9**: a theorem in the cited sources deriving the full admissibility/
monotonicity package from Gamma > 0 alone, with no Gruneisen-type condition, for a general EOS.

---

## O-10. Lemma 2.2(c) — three rigor defects in one parenthetical: "strictly" is false, the resonance hedge is vacuous, uniform diagonalizability is asserted not proved

**Target**: Lemma 2.2(c), lines ~375-380.
**Refutation class**: FALSE-STATEMENT (terminology) + PROOF-GAP (minor). **My demonstration:
complete proof for the first two items; sketch for the third.** **Severity: LOW** (nothing
downstream consumes the defective clauses), but this is the lens's home turf and an of-record
eigenstructure statement should be exact.

1. **"indeed strictly"**: strict hyperbolicity = all characteristic roots simple. The stream root
   has multiplicity 3 (the document says so in the same sentence: "constant multiplicities 1, 3, 1").
   The system is constant-multiplicity (nonstrictly) hyperbolic in x; "strictly" is false as a
   technical term.
2. **The hedge "away from eta = 0 resonances of the two factors, which occur only on a
   codimension-1 eta-set"** is vacuous: the two factors can NEVER share a root for real eta != 0.
   *Proof*: a common root has u.xi = 0 (stream) and (u.xi)^2 = c^2 |xi|^2 (Mach), forcing
   |xi|^2 = 0, i.e., xi = 0, i.e., (xi_x, eta) = 0 — contradiction with eta != 0 (xi_x is then
   determined and the pair is nonzero). So multiplicities are EXACTLY (1, 3, 1) for every real
   eta != 0: the correct statement is stronger and simpler than the hedged one. A hedge that
   guards an impossible case signals the case analysis was not done.
3. **"uniformly diagonalizable symbol"** appears in the definition of hyperbolicity-in-x used by
   the iff, but the proof establishes only: real roots, distinctness of the Mach pair, and
   semisimplicity of the stream root. Uniformity (eigenprojector bounds uniform over |eta| = 1 and
   over the (G3)-box margin states) follows from root separation >= 2 c delta' |eta| / sqrt(...)
   plus homogeneity — two lines, currently absent. Without them the iff's forward direction proves
   a weaker property than the one defined.

**Repair**: delete "indeed strictly"; replace the hedge with the impossibility argument of item 2;
add the two-line uniformity bound.
**Rejecting test for O-10**: (1) a definition of strict hyperbolicity admitting multiplicity 3;
(2) a real eta != 0 with a shared root (impossible, shown above); (3) the uniformity bound already
present in the text (it is not).

---

## O-11. ABSENCE — the exclusion-monitor list (3.4(3)) omits the base-regularity hypothesis, which the L4 certificate does not certify

**Target**: Section 3.4(3) ("margin persistence + downstream overpressure staying below Pi* p_1 are
checkable running conditions"); (H1.1); Section 5 composite.
**Refutation class**: ABSENCE. **My demonstration: audit assertion.** **Severity: MEDIUM.**

Theorem 1's protection is conditional on (H1.1): base state W-bar in W^{1,infinity} on (a
neighborhood of) the slab. The L4 certificate (u_x - c >= delta per patch) does not certify
smoothness; and the physically expected interface field of an RDE — the rotating-wave state carrying
oblique-shock tails, slip lines (contact discontinuities in u_perp and s) — generically transports
DISCONTINUITIES across Gamma_d even "downstream of all heat release". Linearization about a
discontinuous base is outside every theorem in the document (the energy identity needs Lipschitz
S A_j; a base front introduces transmission terms at the front). Consequence: both listed monitors
(margin, overpressure) can be green while the (H1.1) hypothesis — hence R1-by-theorem — is void.

The repo's standing data-class scope (pure periodic rotating wave; monitor = T0 flatness, M0 VI.4bis
per the [D-CONTRACT] block and memory `periodic-wave-data-scope`) PARTIALLY covers this: but (a) the
document never names it as the third monitored hypothesis, and (b) T0 flatness monitors periodicity/
mode purity, not slab smoothness of the instantaneous field. There is also a small unnamed bridge:
(H1.3) is an INSTANTANEOUS unsteady margin on the slab x [0, T_f], while the certificate is checked
per phase on Gamma_d — equality of the two is exactly the rotating-wave ansatz, which should be
cited as the bridge assumption where Theorem 1 is claimed to be "the theorem behind" the
certificate.

**Repair**: extend 3.4(3)'s monitored-condition list to (i) margin persistence, (ii) overpressure
< Pi* p_1, (iii) base-state regularity across the slab (named monitor: data-class purity/T0
flatness + a slab smoothness proxy, e.g., bounded measured gradients), with the rotating-wave
bridge named where per-phase certificates are converted to (H1.3). Rigor class of (iii): PRACTICE.
**Rejecting test for O-11**: a contract clause making slab W^{1,infinity}-regularity part of the L4
certificate itself. [D-CONTRACT] as quoted contains none (verified in M0 lines 116-137: R1/R2/R3 +
margin; no regularity clause).

---

## O-12. ABSENCE — Corollary 4(i) well-posedness is normal-incidence 1-D; consumption for the contract's multi-D subsonic patches would overreach (impedance BCs are Kreiss-delicate in multi-D)

**Target**: Corollary 4 model (lines ~660-673) and claim (i); register row 4; Section 5's last
sentence ("subsonic patches must carry causal-separation as a named extra hypothesis").
**Refutation class**: ABSENCE (consumption risk; the corollary itself is honest about its class).
**My demonstration: audit assertion.** **Severity: LOW** for this document, MEDIUM if row 4 is later
consumed as "R2 holds for passive impedance closures" at contract level.

The model suppresses transverse dependence (all statements are exact 1-D transport identities). For
a genuine multi-D subsonic patch with impedance closure p' = Z u'.n, well-posedness is a uniform
Kreiss-Lopatinskii question in (tau, eta): impedance-type conditions for linearized Euler can admit
neutral surface modes / WR-class instabilities for ranges of Z, and "passive" (Re Z >= 0, frequency-
dependent) does not by itself deliver maximal dissipativity in multi-D. The corollary's quadrant
logic is unaffected (exhibition in a declared model class suffices for the truth table), but the
register row's hypothesis column ("uniform subsonic base; passive r") does not carry the "1-D
normal-incidence model" qualifier that the proof requires — and the [D-CONTRACT] R2 clause this
grounds ("incoming invariants + impedance") is a multi-D clause.

**Repair**: add "1-D normal-incidence model class" to row 4's hypothesis column and one sentence in
Corollary 4 flagging that the multi-D passive-impedance R2 statement is NOT proved here (open,
Kreiss-type analysis required — candidate future falsifier: 2-D patch run with transverse
wavenumber sweep).
**Rejecting test for O-12**: a multi-D dissipativity proof for p' = Z u'.n with the Section-1
symmetrizer (would need the boundary form sign for all eta, which the document does not attempt).

---

## Minor nits (N-list; each independently checkable, none load-bearing)

- **N1 (of-record text incomplete)**: the 3b(iii) margin-price display literally contains the
  placeholder "(something >= 2 gamma_1 (...))" (lines ~564-566). An of-record THEOREM display
  containing "something" fails the document's own bar; state the gamma-const bound and the general
  strict-positivity claim as two separate sentences. (The gamma-const bound itself checks out:
  M_x >= 1 + delta/c_1 => Pi* - 1 >= 2 gamma_1 (2 delta/c_1 + delta^2/c_1^2)/(gamma_1 + 1).)
- **N2 (hypothesis bookkeeping)**: Theorem 2's proof of (b) invokes "(H2.1)+(H1.2)" for the wall
  stream-surface property; (H1.2) is a Theorem-1 hypothesis about the UNSTEADY problem's
  perturbations. The per-phase slip conditions (base and perturbation) should be their own (H2.3).
- **N3 (asserted extremality)**: Lemma 2.1's "minimal axial component ... attained in the plane
  span{u, e_1}" is the spherical triangle inequality angle(ray, e_1) <= angle(ray, u) +
  angle(u, e_1) with equality in the common plane — true, but asserted; one line to cite/prove.
  Also the degenerate case u parallel to e_1 (theta = 0) and theta + alpha >= pi/2 wrap-around
  deserve a half-line.
- **N4 (Schur step)**: Lemma 0.2's determinant via Schur complement divides by (u.n - lambda);
  the identity extends to lambda = u.n by polynomial continuity — standard, but the of-record proof
  should say so (both sides polynomials in lambda agreeing off a finite set).
- **N5 (Theorem 1 hypothesis strength)**: hypothesis (ii) demands FULL-trace equality on Gamma_in.
  For the physical upstream domain the inflow (injection face) is subsonic: two runs sharing the
  same physical inflow BC (incoming invariants + closure) do not a priori share full traces, so
  Theorem 1 as stated does not directly apply to "same physical inflow BC" pairs. Repair: replace
  (ii) by "U^(1), U^(2) satisfy the same maximal nonnegative boundary condition on Gamma_in"
  (the boundary term for the difference is then <= 0 and the proof is unchanged). As stated the
  theorem is correct but weaker than its R1 gloss suggests.
- **N6 (cosmetic)**: Lemma 0.2 labels lambda_- "incoming-side" with no orientation defined at that
  point; orientation only appears in Section 1. Delete or define.
- **N7 (bookkeeping)**: header says "authored 2026-08-17" inside `sfoundations_raws_2026-08-13/`;
  fine if the raws directory is the session anchor, but the of-record status line should say which
  date governs (SR-12-adjacent hygiene).
- **N8 (register row 2a hypotheses column)**: omits the orientation hypothesis u_x > 0 that 2.2(c)
  carries in-line.

---

## S. Verified-algebra log (attacked and SURVIVED — for round-2 economy)

Each item was recomputed independently, not pattern-matched:

1. Lemma 0.1: exactness of c_v dT/T - R drho/rho; c^2 = gamma(T) R T along isentropes. HOLDS.
2. Lemma 0.2: A(n) entries vs the primitive system; det = (u.n - lambda)^3 [(u.n - lambda)^2 - c^2];
   eigenvectors r_∓ = (rho, ∓c n, rho c^2), r_s, r_{t_i} verified by substitution; kernel of
   A - (u.n) I has dim 3 (rank 2). HOLDS (modulo N4).
3. p-equation derivation from energy: c_v DT/Dt = -RT div u => Dp/Dt = -gamma p div u. HOLDS.
4. Linearization bookkeeping g_rho, g_u, g_p and the sigma-transformation (div u' cancellation;
   zeroth-order remainder includes the time-derivative of 1/c-bar^2, covered by (H1.1) in t). HOLDS.
5. Lemma 1.1: S A(n) symmetry and (BQ) = (u.n)<SU,U> + 2 p'(u'.n). HOLDS.
6. Lemma 1.2: symmetric similarity N = S^{1/2} A S^{-1/2}, spectrum shift => S A(n) >= delta S.
   HOLDS.
7. (EI): signs of d_t S, d_j(S A_j), sym(S B), boundary term; Gronwall closure; s_min comparison.
   HOLDS (C^1 class).
8. Lemma 2.1 chain cos theta > sin alpha <=> u_x > c, alpha in (0, pi/2). HOLDS (modulo N3).
9. Lemma 2.2: discriminant/4 = c^2 [(u_perp.eta)^2 + (u_x^2 - c^2)|eta|^2]; the u_x < c complex-root
   construction (eta perp u_perp); the u = (0.5c, 0.9c, 0) example; the 2-D contrast (eta in R^1:
   complex iff |u| < c, so 2-D x-hyperbolicity iff q > c) — all re-derived. HOLD.
10. Theorem 2(a)-(b): S_x = S A_1 >= delta S; wall term vanishing for n with n_x != 0 (BQ needs
    only u-bar.n = 0, u'.n = 0 — verified, the varying-cross-section wall is handled correctly);
    x-Gronwall with 1/delta degradation. HOLDS.
11. Theorem 3a: U_s < 0 <=> M_s > M_x, pure algebra. HOLDS.
12. Lemma 3.1: Gamma_fund = (gamma+1)/2 + (gamma-1) T gamma'(T)/(2 gamma), via
    (dT/drho)_s = RT/(rho c_v); the (G4)-failure threshold T gamma' <= -gamma(gamma+1)/(gamma-1).
    HOLDS.
13. gamma-const anchors: M_s^2 = 1 + (gamma+1)(Pi-1)/(2 gamma); Pi*(2) = 4.5 at gamma = 1.4. HOLD.
14. 3b(ii) identity M_s^2 = (Pi - 1)/[gamma_1 (1 - rho_1/rho_2)] and the >= (Pi-1)/gamma_1 bound
    (GIVEN compressivity — see O-1 for who must supply it). HOLDS conditionally.
15. Corollary 4: B_L in characteristic variables (axial-acoustic split rho_0 (R_+^2 + R_-^2)/2 and
    rho_0 c_0 (R_+^2 - R_-^2)/2); dissipativity bound r^2 <= (u_0 + c_0)/(c_0 - u_0) > 1;
    quadrant (b) explicit reflection solution and arrival time (L - x)/(c_0 - u_0); quadrant (c)
    over-determination argument. ALL HOLD.
16. Section 3.4(1): U_s not in spec A(e_1; W_1) (all eigenvalues >= delta > 0 > U_s). HOLDS.
17. Compressivity direction: for p_2 > p_1, mass+momentum FORCE rho_2 > rho_1 for any realizable
    front (v_1^2 > 0) — used in O-1's repair. HOLDS.

---

## Round-1 verdict

**REPAIRABLE.** No objection breaks the composite's spine: Theorem 1, Theorem 2(a)-(b), Theorem 3a,
Lemma 3.1, and Corollary 4 quadrants (b)-(c) stand as proved (with the O-6 planar qualifier), and
the finite-amplitude boundary story (Section 3) is TRUE but not yet proved-as-labeled: O-1 (proof
gap, repair supplied), O-2 (hypothesis-domain, repair named), O-9 (citation scope). The labels that
must change pending repair: 3b(i) THEOREM(complete) -> THEOREM after O-1's endpoint line; 3b(iii)/3c
labels conditioned on (G2') or the capped quantifier (O-2); Remark 2.3 THEOREM* -> SCHEMA until the
citation swap (O-3); Corollary 4(d) sketch withdrawn and replaced by the miscounted-closure witness
(O-4); Theorem 2 falsifier (i) rewritten (O-5); Section 5 composite either planar-qualified or
normal-margin restated (O-6). None of these is expensive; all are in-window class repairs.
