# REFUTATION — Round 1, Lens 1 (gas-dynamics physics)

**Target**: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md` (read in full, 814 lines).
**Lens**: shock kinematics, unstart phenomenology, the M_s > M_x derivation, gamma(T) validity.
**Refuter discipline**: every objection below states (a) the exact claim attacked, (b) the defect with
explicit hypotheses and named spaces, (c) the rigor class OF THE OBJECTION ITSELF (complete proof /
sketch / modeling assertion), (d) severity, (e) a repair path, and (f) a **rejecting test for the
objection** — an experiment or computation whose outcome would kill MY attack, per repo R5 (the
refuter's claims are claims too).

**Severity scale**: P1 = a stated THEOREM/THEOREM* is not proved under its stated hypotheses, or a
composite claim is false as worded; P2 = label/scope defect (true statement, wrong class or wrong
quantifier as applied); P3 = falsifier/editorial defect below the repo bar.

---

## 0. Verification log — what was checked and SURVIVED

Recomputed independently (complete recomputation, not trust):

1. **Lemma 0.1**: exactness of c_v(T) dT/T − R drho/rho; along ds = 0,
   dp = RT drho + rho R (RT/c_v)(drho/rho) = gamma(T) RT drho. CONFIRMED.
2. **Lemma 0.2**: direct substitution of r_∓ = (rho, ∓c n, rho c^2)^T into A(n) reproduces
   (u.n ∓ c) r_∓ row by row; Schur/rank-one determinant chain CONFIRMED; u.n semisimple with
   eigenvectors (1,0,0), (0,t_i,0) CONFIRMED.
3. **Lemma 1.1/1.2**: S A(n) symmetry, (BQ), and the S^{1/2}-conjugation argument CONFIRMED;
   spectrum {u.n − c, u.n (x3), u.n + c} ⊂ [delta, ∞) under the margin CONFIRMED
   (u.n ≥ delta + c ≥ delta, u.n + c ≥ delta + 2c).
4. **Theorem 1 energy chain**: volume-term bound needs only W^{1,∞} coefficients + (G); boundary
   decomposition (Gamma_in zero, wall zero by (BQ), interface ≤ −delta·energy) CONFIRMED; Gronwall
   closes. The C^1-core proof of Theorem 1 is, in my judgment, COMPLETE AS LABELED.
5. **Lemma 2.1**: the filled influence cone is {angle(d, u) ≤ alpha}, verified from
   |x − ut| ≤ ct ⟺ (u·x)^2 ≥ |x|^2(|u|^2 − c^2) & u·x > 0 ⟺ cos beta ≥ cos alpha; the
   theta + alpha < pi/2 ⟺ u_x > c chain CONFIRMED both directions. Frame-invariance of (u_x, c)
   under azimuthal frame change CONFIRMED.
6. **Lemma 2.2**: discriminant/4 = c^2[(u_perp.eta)^2 + (u_x^2 − c^2)|eta|^2] CONFIRMED; the 3-D
   counterexample u = (0.5c, 0.9c, 0), eta = (0,1) CONFIRMED complex. Theorem 2(a),(b): the
   symmetric-positive marching structure and the station-energy Gronwall (divergence theorem with
   the wall flux <S A(n)U,U> = 0 for ANY wall normal, n_x ≠ 0 included, by (BQ)) CONFIRMED — the
   sufficiency direction of Theorem 2 is sound.
7. **Lemma 3.1**: (dT/drho)_s = RT/(rho c_v); (d c^2/drho)_s = R^2 T (gamma + T gamma')/(rho c_v);
   Gamma_fund = (gamma+1)/2 + (gamma−1) T gamma'/(2 gamma) CONFIRMED exactly. The (G4) failure
   threshold T gamma' = −gamma(gamma+1)/(gamma−1) CONFIRMED.
8. **Theorem 3a**: U_s < 0 ⟺ M_s > M_x — trivially correct for the declared class (constant-speed
   NORMAL front; see O3 for what that scope excludes).
9. **Theorem 3b identities**: p_2 − p_1 = rho_1 v_1^2 (1 − rho_1/rho_2) from mass+momentum;
   M_s^2 = (Pi − 1)/[gamma_1 (1 − rho_1/rho_2)] ≥ (Pi − 1)/gamma_1 CONFIRMED; phi(T_1) < 0 and
   phi(∞) = +∞ CONFIRMED (but see O1, O2: domain and branch); gamma-const closed form and the
   anchor Pi*(2) = 1 + 2(1.4)(3)/2.4 = 4.5 CONFIRMED = the classical normal-shock pressure ratio
   at M = M_x (i.e., the threshold front is the standing normal shock — physically right).
10. **Corollary 4 flux algebra**: B_L = (rho_0/2)[(u_0+c_0)R_+^2 − (c_0−u_0)R_-^2] + u_0(·) ≥ 0
    under r^2 ≤ (u_0+c_0)/(c_0−u_0) CONFIRMED by direct substitution; inflow-face sign CONFIRMED
    good; arrival time (L−x)/(c_0−u_0) CONFIRMED. Quadrant (c) overdetermination argument
    CONFIRMED valid.

The core linear results (Theorem 1, Theorem 2(a)-(b), Corollary 4 claims (i)-(ii)) withstand this
round on their stated hypotheses. The defects found are concentrated in Section 3 (hypothesis
domain, branch selection, front-geometry scope), in the Assembly wording, and in three labels.

---

## O1 (P1) — Theorem 3b(i)-(iii)/3c: the Hugoniot leaves the hypothesized gas-model domain; "for every Pi > 1" is unproved under (G1)-(G4) as stated

**Claim attacked**: Thm 3b(i) "For every pre-state 1 in the (G3) box and every Pi > 1 there exists
a post-state 2 ... T_2 in (T_1, ∞)", labeled THEOREM (complete); 3b(iii) monotonicity under (G4),
labeled THEOREM*; 3c "U(delta) NONEMPTY for every delta" (register: strengths unbounded).

**Defect (complete proof of the objection).** Hypothesis (G2) posits e ∈ C^2 **on the working
temperature interval [T_min, T_max]** with c_v bounds there; (G3) boxes the states; (G4) is imposed
"on the working box". The proof of 3b(i) evaluates h(T_2) = e(T_2) + R T_2 along T_2 → ∞ (the IVT
endpoint estimate "phi(T_2) ≥ c_p,min(T_2 − T_1) − C − (R/2)(1 − 1/Pi) T_2 → +∞" uses c_p bounds on
ALL of (T_1, ∞)). Post-shock temperature is unbounded in Pi: from the Hugoniot,
T_2/T_1 → Pi (gamma−1)/(gamma+1)-type growth (gamma-const: T_2/T_1 ~ Pi (gamma−1)/(gamma+1) → ∞).
Hence for all Pi above a finite Pi_box(state 1), T_2 > T_max and the constructed state exits the
domain on which the gas model is even DEFINED by the standing hypotheses. Three consequences:

 (a) 3b(i) as quantified ("every Pi > 1") is not a theorem under (G1)-(G3): the function phi is not
     hypothesized to exist beyond T_max. The IVT chain is valid only after silently extending (G2)
     to [T_min, ∞) with global bounds — an UNSTATED hypothesis.
 (b) 3b(iii) invokes Bethe-Weyl/Menikoff-Plohr monotonicity, which requires Gamma_fund > 0 **along
     the Hugoniot curve through states possibly far outside the (G3)/(G4) box** — (G4) on the
     working box does not cover the curve. The THEOREM* citation is load-bearing on a domain where
     its hypothesis is not certified.
 (c) 3c ("strengths are unbounded", U(delta) nonempty for EVERY delta) inherits (a): for large
     margin (large Pi*(M_x)) the threshold-crossing states may already lie outside [T_min, T_max]
     — precisely where the tabulated backend (repo memory `thermo-tabulated-backend`) has no rows
     and where the frozen thermally-perfect pin physically fails (dissociation/vibrational
     nonequilibrium of combustion products at post-shock temperatures; the frozen-composition (G1)
     pin is a MODELING assertion there, not a theorem input).

**Rigor class of objection**: complete proof for (a) (a quantifier/domain mismatch is checkable by
reading); complete for (b) (the cited theorems' hypothesis is Gamma > 0 on the connecting curve);
modeling assertion for the physical clause of (c).

**Repair path**: either (R1a) extend (G2)/(G4) explicitly: e ∈ C^2([T_min, ∞)),
0 < c_v,min ≤ c_v ≤ c_v,max globally, Gamma_fund ≥ Gamma_min along all Hugoniots from box states —
declaring this an idealized extension of the table (and scoping the physical validity), or (R1b)
restrict the quantifier: "for every Pi with T_2(Pi) ≤ T_max", compute Pi_box from the tables, and
state U(delta) nonempty **whenever Pi*(M_x) < Pi_box** — with the honest remark that for
Pi* ≥ Pi_box the unstart claim leaves the certified gas model (which does NOT rescue R1: it means
the theory cannot certify what such a front does, strictly worse than a priced breach).

**Rejecting test for the objection**: exhibit in the document a line extending (G2)/(G4) beyond
[T_min, T_max] that I missed (there is none — Section 0 lines 50-64 are explicit), OR show
numerically from the pinned tables that for all margin states in the certified pipeline
T_2(Pi*(M_x)) ≤ T_max (this would demote (c) from P1 to a quantifier-wording fix while leaving
(a),(b) standing).

---

## O2 (P1) — Theorem 3b(i): the IVT root is not shown COMPRESSIVE; the chain (i) → (ii) → 3.3-admissibility has a named gap

**Claim attacked**: 3b(i) THEOREM (complete): existence of a post-state "T_2 in (T_1, ∞)";
3b(ii) opens "Any compressive RH solution (rho_2 > rho_1, as admissibility under (G4) requires)";
3.3 "let W_2 be the RH post-state of Theorem 3b(i) ... (admissible by (G4), Section 3.1)".

**Defect (complete proof).** (i) proves phi has A root in (T_1, ∞) and stops. Compressivity is
equivalent to rho_2 > rho_1 ⟺ p_2/(R T_2) > p_1/(R T_1) ⟺ **T_2 < Pi T_1**. Nothing in (i)
places the root below Pi T_1; a root with T_2 ≥ Pi T_1 has rho_2 ≤ rho_1, hence
1 − rho_1/rho_2 ≤ 0 and rho_1 v_1^2 = (p_2 − p_1)/(1 − rho_1/rho_2) < 0: no real front at all —
such a root is spurious for the construction, and (i)'s statement "T_2 in (T_1, ∞)" admits it.
(ii) then assumes compressivity as a hypothesis, and 3.3 asserts admissibility of "the" post-state
of (i) — consuming a property (i) never delivered. Under the document's own THEOREM standard
("complete proof in this document") this is a gap in a load-bearing chain: the unstart class 3c
rests on it.

**The missing step is one line (constructive refutation-repair):** evaluate phi at T_2 = Pi T_1:
rho_2 = p_2/(R Pi T_1) = rho_1, so
phi(Pi T_1) = h(Pi T_1) − h(T_1) − (p_2 − p_1)/rho_1 = Int_{T_1}^{Pi T_1} c_p(t) dt − R T_1(Pi − 1)
> R T_1 (Pi − 1) − R T_1 (Pi − 1) = 0, using c_p(t) > R ((G2): c_p = c_v + R > R). With
phi(T_1) < 0, IVT gives a root in (T_1, Pi T_1): compressive. (This also shows the compressive
root is the physical branch; uniqueness on that interval still needs monotonicity — (G4)-cited —
which is fine as THEOREM*.)

**Rigor class of objection**: complete proof (both the gap exhibition and the repair line).
**Severity**: P1 (a THEOREM-labeled statement whose stated conclusion does not support its
downstream consumption; repair trivial but mandatory).

**Repair path**: insert the phi(Pi T_1) > 0 evaluation into (i) and restate its conclusion as
"T_2 ∈ (T_1, Pi T_1), hence rho_2 > rho_1: compressive".

**Rejecting test**: show that some other line of the document already forces T_2 < Pi T_1 (I
searched: nothing does), or that the (i)-root consumed downstream is selected by an explicit branch
condition (none is stated).

---

## O3 (P1) — Normal-front scope overbreadth: the exclusion "fronts with Pi < Pi* cannot propagate upstream" is proved ONLY for planar NORMAL fronts, but Section 5 and 3.4(3)(b) state it unscoped; oblique-front kinematics is never adjudicated

**Claim attacked**: 3.2 positive re-statement "**every admissible front with strength Pi < Pi*(M_x)
cannot propagate upstream**"; 3.4(3)(b) "fronts below threshold excluded BY THEOREM"; Section 5
composite "an admissible front runs upstream iff M_s > M_x (Theorem 3a) ... prices the
excluded-front band Pi < Pi*".

**Defect.** Section 3.1 declares its class: "Normal front along x". Within that class the algebra
is correct (verified, item 8 above). But the monitor conclusion consumed by the program — downstream
overpressure below Pi* p_1 implies no finite-amplitude breach of the interface — quantifies over
ALL finite-amplitude disturbances, and the composite statement's wording ("an admissible front runs
upstream iff M_s > M_x") drops the normal-front qualifier. Oblique fronts have genuinely different
kinematics, and the threshold question for them is NOT settled by Theorem 3a:

*Complete computation (frozen uniform idealization, axial pre-state u = (u_1, 0, 0), M_x = u_1/c_1
> 1).* Let a planar front have unit normal n with n_x ∈ (0, 1) and normal-direction lab speed V.
Pre-state relative normal inflow v_1 = u·n − V, admissibility (Lax, (G4)) requires v_1 > c_1, i.e.
V = u_1 n_x − M_{s,n} c_1 with M_{s,n} > 1. The front's trace on a wall streamline (or any line
x_perp = const) moves axially at
    dx/dt = V / n_x = u_1 − M_{s,n} c_1 / n_x.
For any n_x < M_{s,n}/M_x — in particular for ANY admissible strength (M_{s,n} → 1+) once
n_x < 1/M_x — this is NEGATIVE: the trace of an arbitrarily WEAK admissible oblique front slides
upstream through an L4 state. The strength threshold Pi*(M_x) does not govern oblique traces.

*Why this does not immediately refute R1 (stated for fairness, and it is exactly the lemma the
document is missing):* a single planar oblique front's post-state occupies a half-space
{n·x > V t + const} which, for n oblique, was NEVER confined to {x > x_d} at t = 0 — so it is not a
member of the downstream-transient class. For downstream-CONFINED data the linear leading edge
moves along rays u ± c n with axial component u_1 ∓ c_1 n_x ≥ u_1 − c_1 ≥ delta > 0 for every unit
n: all rays advance downstream (this is Theorem 1's content and it survives). For the NONLINEAR
problem the analogous statement — the upstream-most point of the disturbed region's boundary,
where by smooth-minimum geometry the front normal is axial (n = e_1), advances at the NORMAL-front
rate, so Theorem 3a's threshold governs the apex — is the standard heuristic behind duct-unstart
phenomenology (inlet unstart proceeds by an upstream-running normal foot / Mach-stem leading a
shock train; the oblique members of the train ride behind the normal leading structure). **That
apex/leading-point lemma is nowhere stated, sketched, or even flagged as a gap.** As written, the
document proves normal-front sufficiency (3.3: genuine members of U(delta) exist — this stands)
but asserts EXCLUSION below Pi* in a generality it never establishes; between normal-front
exclusion and all-disturbance exclusion sits precisely the free-boundary geometry of multi-D shock
fronts (wall reflections, Mach stems, triple points), i.e., the physically operative unstart
mechanism.

**Rigor class of objection**: complete proof for the trace-speed computation and for the scope
mismatch (quantifier reading); sketch for the apex-lemma repair route; modeling assertion for the
shock-train phenomenology clause.
**Severity**: P1 for the composite/3.4(3)(b) wording (a claim consumed as a general exclusion is
proved only in a sub-class); the underlying mathematics of Section 3 is untouched.

**Repair path**: (R3a) scope every exclusion statement, including Section 5 and 3.4(3)(b), to
"planar NORMAL fronts", and add a named residue row for the multi-D front-geometry lemma
(owner + trigger, per the repo's structurally-gated rules); or (R3b) prove the leading-point lemma
in the piecewise-smooth class (at a C^1 minimum of the front-position function x = phi(x_perp, t),
grad_perp phi = 0 forces n = e_1, and d(min phi)/dt = V(e_1) = u_1 − M_s c_1, reducing the apex to
Theorem 3a; corner/wall-attachment cases need the reflection sub-lemma) — SCHEMA at minimum.

**Rejecting test**: (i) textual — exhibit a line scoping 3.4(3)(b)/Section 5 to normal fronts (the
phrase "Normal front along x" in 3.1 does not propagate: 3.4(3)(b) and Section 5 restate the claim
without it); (ii) physical — a 2-D duct Euler computation in which a downstream-confined
disturbance whose EVERY normal-strength stays below Pi*(M_x) drives the disturbed-region boundary
across x_I would refute my fairness caveat and make the objection STRONGER (upgrade to a
counterexample against the monitor itself); a computation showing the leading edge always pinned at
the normal-incidence rate supports repair (R3b) and still confirms the wording defect.

---

## O4 (P2) — The "iff"/"only then" narrative is false as applied to the document's OWN per-phase class (I2, axisymmetric meridional): there hyperbolicity-in-x holds iff the MERIDIONAL Mach exceeds 1, not iff u_x > c

**Claim attacked**: Theorem 2(a) narrative "Axial supersonicity with margin is EXACTLY ... the
promotion of x to a time direction"; Section 5 "x time-like via S A_1 ≥ delta S — equivalently,
and only then, the Mach cone points strictly downstream"; the pairing of Lemma 2.2(c)'s iff with
the per-phase class throughout Section 2.

**Defect (complete proof).** Lemma 2.2(c)'s iff is proved for the 3-D symbol, eta ∈ R^2, and is
TRUE there (verified). But Theorem 2's declared class is **I2: per-phase meridional profiles**
(document line ~23-24, M0 [D-CONTRACT]) — axisymmetric fields with swirl, derivatives in (x, r)
only. In that class the transverse frequency is ONE-dimensional (eta = xi_r e_r), and u_theta does
not enter the principal symbol at all (the theta-momentum equation is pure advection at the stream
speed; the azimuthal pressure gradient vanishes under d_theta = 0; swirl appears only in the 1/r
source terms). The Mach-factor discriminant of the meridional symbol is, by the document's own
formula with u_perp·eta = u_r xi_r:

    disc/4 = c^2 [ (u_r xi_r)^2 + (u_x^2 − c^2) xi_r^2 ] = c^2 xi_r^2 [ u_x^2 + u_r^2 − c^2 ].

Real roots for all xi_r ⟺ **q_m := sqrt(u_x^2 + u_r^2) ≥ c** — the MERIDIONAL Mach condition —
NOT u_x > c. So in the class Theorem 2 actually quantifies over, algebraic hyperbolicity-in-x holds
on a strictly larger set than the L4 margin set; "only then" is false there. This is exactly the
2-D degeneration the document itself records in Lemma 2.2(d) ("the counterexample direction below
needs dim(eta) ≥ 2 or ...") — but it never notices that its OWN consumed class is the degenerate
case. Classical confirmation: axisymmetric method-of-characteristics marching (Zucrow-Hoffman
class, the GENO MoC of this repo) is well-defined under meridional supersonic flow; u_x > c is not
its operating condition.

What u_x > c (with margin) IS equivalent to, in every dimension: positivity of S A_1 (Friedrichs
time-likeness of x; Lemma 1.2 — correct), spacelikeness of {x = const} for the UNSTEADY cone
(Lemma 2.1/[T-NSW] — correct), and the downstream-closing domain of dependence that carries R1.
The sufficiency direction of Theorem 2 is therefore intact; the defect is the biconditional
rhetoric ("EXACTLY", "equivalently, and only then") transplanted into the class where its
necessity half fails, plus a missed opportunity to state the true necessity content (causality /
energy-marching, not root-reality).

**Rigor class of objection**: complete proof (the discriminant computation above plus the
principal-symbol structure of axisymmetric Euler, both one-line verifiable).
**Severity**: P2 — no proved statement is false under its own hypotheses; the Assembly and 2(a)
wording claim a necessity that fails in the consumed class.

**Repair path**: state in Section 2 that for the I2 meridional symbol the root-reality condition
degenerates to q_m > c, and that the L4 condition u_x > c is retained because (i) it is the
UNSTEADY spacelikeness/causality condition (Theorem 1, the actual R1 carrier) and (ii) it is what
makes the Friedrichs energy marching and the downstream-closed domain of dependence work; delete
or scope "equivalently, and only then" in Section 5 to the 3-D unsteady reading.

**Rejecting test**: exhibit a principal-symbol coupling of u_theta in the axisymmetric system that
I have missed (write the cylindrical Euler system under d_theta = 0: there is none), or show the
document's Theorem 2 class is genuinely 3-D (line ~23-24 says I2 meridional).

---

## O5 (P2) — Remark 2.3's THEOREM* label rests on citations that do not cover the claimed class (characteristic wall boundary + axis singularity)

**Claim attacked**: Remark 2.3 "**Rigor: THEOREM***" for nonlinear per-phase local
existence-uniqueness by x-marching, citing Li Ta-tsien Ch. 1 and Courant-Friedrichs §V.

**Defect.** The document's own vocabulary (line 30-32) defines THEOREM* as "complete proof modulo
an explicitly cited standard result (citation load-bearing, named)". The named citations do not
carry the class: (a) Li Ta-tsien's semi-global classical theory is for quasilinear hyperbolic
systems in ONE space dimension with boundary conditions of prescribed characteristic-entering
structure on NON-characteristic boundaries; the per-phase problem is x-marching of the meridional
system on {(r): 0 ≤ r ≤ r_w(x)} whose wall boundary is a stream surface — i.e., a CHARACTERISTIC
boundary of constant multiplicity (the u·n = 0 wall sits exactly on the multiplicity-3 stream
eigenvalue): the characteristic-boundary IBVP is a distinct and harder theory (Secchi's
characteristic-boundary symmetric-hyperbolic results; Rauch's trace theory), not in Li Ch. 1.
(b) The axis r = 0 carries 1/r geometric sources; classical marching theory requires either
weighted spaces or a reflection/regularity argument at the axis — nowhere cited, and this repo has
an OPEN near-axis residue of record (O4 discharge: "non-fold, near-axis, owner F2"), so the gap is
live, not hypothetical. (c) Courant-Friedrichs §V is a constructive 2-D MOC exposition, not a
uniqueness/well-posedness theorem in the S1 class.

**Rigor class of objection**: complete for the citation-coverage mismatch (checkable against the
cited texts' hypotheses); sketch for what the correct citation set would be.
**Severity**: P2 (label inflation; the remark itself is plausibly true in content).

**Repair path**: relabel Remark 2.3 SCHEMA with the two gaps named (characteristic wall boundary;
axis weight), or upgrade the citation set to one that actually covers the class and check its
hypotheses (constant-rank characteristic boundary: yes for a slip wall of a nonvanishing base
flow; axis: needs the axisymmetric function-space lemma).

**Rejecting test**: produce chapter-and-theorem numbers from the cited works whose hypotheses
include a characteristic boundary and an axis-type coordinate singularity for quasilinear systems
(I claim none exist in Li Ch. 1 / C-F §V; a correct pinpoint citation kills this objection).

---

## O6 (P2) — Lemma 2.2(c): the claimed "codimension-1 eta-set of resonances" does not exist, and uniform diagonalizability is asserted, not proved

**Claim attacked**: "(indeed strictly, constant multiplicities 1, 3, 1 away from eta = 0 resonances
of the two factors, which occur only on a codimension-1 eta-set and remain semisimple ...)".

**Defect (complete proof).** The two factors NEVER resonate for eta ≠ 0: on the stream root
u·xi = 0 (xi ≠ 0), the Mach factor evaluates to (u·xi)^2 − c^2|xi|^2 = −c^2 |xi|^2 < 0, so no
common root exists; and under u_x > c the two Mach roots are distinct for every eta ≠ 0 (the
discriminant is ≥ c^2 (u_x^2 − c^2)|eta|^2 > 0 — the document's own display). Hence the
multiplicity pattern is constant (1, 3, 1) for ALL eta ≠ 0 with no exceptional set. Claiming a
nonexistent degeneracy set, and then waving it off by semisimplicity, is evidence the
diagonalizability clause was not actually executed. The clean and complete argument is available
one section earlier and goes unused: with S from Lemma 1.1, the x-pencil
xi_x (S A_1) + (S A(0, eta)) is a symmetric pencil with S A_1 ≻ 0 (Lemma 1.2, margin), hence all
xi_x real and the pencil diagonalizable with (delta, G)-uniform conditioning — which is the
"uniformly diagonalizable" the statement needs.

**Rigor class of objection**: complete proof.
**Severity**: P2 (the iff conclusion is true; a step inside a THEOREM-labeled proof asserts a false
intermediate and omits the needed uniformity argument).

**Repair path**: replace the parenthetical with the no-resonance computation + the
symmetric-definite pencil argument (three lines, all ingredients already in the document).

**Rejecting test**: exhibit a state in the (G3) box with u_x > c and an eta ≠ 0 at which two
factor-roots coincide or the x-symbol is defective (I claim the computation above excludes it;
a single numeric counterexample kills this objection).

---

## O7 (P2) — Theorem 3b(iii): a THEOREM(-*)-labeled block contains a placeholder display, and the general-gamma(T) threshold bound is asserted, not derived

**Claim attacked**: the display "Pi* − 1 ≥ gamma_min-normalized O(delta/c_1): Pi* − 1 ≥ (something
≥ 2 gamma_1 (2 delta/c_1 + delta^2/c_1^2)/(gamma_1+1) in the gamma-const form; in general
Pi* − 1 > 0 strictly ...)".

**Defect.** "(something ≥ ...)" is not a mathematical statement; "gamma_min-normalized
O(delta/c_1)" binds no constant to any hypothesis. Under the repo's own R5 (no numbers/claims
without derivation) a quantitative lower bound inside a proof-bearing block must be derived or
deleted; as written, only the qualitative clause "Pi* − 1 > 0 strictly" is actually proved
(monotonicity + M_s(1+) = 1 < M_x), and the quantitative content silently degrades to gamma-const.
The general-gamma bound the block gestures at is obtainable in one line from the document's own
(ii)-identity evaluated at the crossing M_s(Pi*) = M_x:

    Pi* − 1 = gamma_1 M_x^2 (1 − rho_1/rho_2(Pi*))  — exact, all gamma(T) —

which with the margin M_x ≥ 1 + delta/c_1 and any certified lower bound on the density jump at
threshold (e.g., from (G4)-monotonicity, 1 − rho_1/rho_2 ≥ (M_x^2 − 1)/(K M_x^2) with
K = K(gamma-bounds) from the Hugoniot slope bound) yields an explicit, hypothesis-bound
delta-dependent threshold floor.

**Rigor class of objection**: complete for the "not a statement" clause; sketch for the offered
replacement bound (the exact identity line is complete; the density-jump floor needs the (G4)
Hugoniot-slope bound written out).
**Severity**: P2.

**Repair path**: replace the placeholder with the exact identity above + a derived floor, or strip
the display to the proved qualitative statement and the gamma-const closed form (already labeled
as an anchor).

**Rejecting test**: none needed for the textual clause (the placeholder is verbatim, lines
564-566); for the replacement, a numeric Hugoniot sweep contradicting the exact identity
Pi* − 1 = gamma_1 M_x^2 (1 − rho_1/rho_2)|_{Pi*} would kill my repair (it follows from verified
(ii); it will not fail).

---

## O8 (P2) — "Measure-zero standing-front bifurcation" (3.4(2)) mischaracterizes duct unstart phenomenology; the claim is true only in the uniform frozen idealization and is not scoped to it

**Claim attacked**: 3.4(2) "... excluded on the margin state by Theorem 3a since M_s = M_x would
need Pi = Pi* exactly — the measure-zero standing-front bifurcation point, the classical unstart
threshold".

**Defect (modeling assertion, with classical evidence).** In the uniform frozen-coefficient
idealization, {Pi = Pi*} is indeed a single point. But "the classical unstart threshold" in a real
(nonuniform) duct is NOT a measure-zero phenomenon in the control parameter: with M_x(x) varying
along the duct, the family of steady solutions with a STANDING normal shock at station x_s spans a
whole BAND of back pressures (each back pressure in the band places the shock where the local
normal-shock relation is satisfied — the elementary quasi-1-D nozzle-flow shock-positioning
argument), and unstart onset proceeds by quasi-steady shock displacement through that band (and by
choking/accumulation paths of Kantrowitz type, where a modest blockage builds the overpressure up
to threshold over time). Calling the standing front "measure-zero" while attaching to it the label
"the classical unstart threshold" conflates the idealized bifurcation point with the physical
onset process; a reader consuming the monitor could conclude that near-threshold operation is
generically safe (measure-zero), which the duct phenomenology contradicts. Note the hypotheses
protect the formal statement: (H2.2) margin on the whole segment excludes interior standing shocks
from Theorem 2's class — the defect is the unscoped phenomenological gloss, not the theorem.

**Rigor class of objection**: modeling assertion (phenomenology), with the shock-positioning
argument complete at quasi-1-D level.
**Severity**: P2 (prose consumed by the monitor's operational reading).

**Repair path**: scope the sentence: "measure-zero IN THE UNIFORM IDEALIZATION'S strength
parameter; in a nonuniform duct the standing-shock family is robust in back-pressure and unstart
onset is quasi-steady displacement — the monitor must therefore alarm on APPROACH to Pi*, not on
crossing".

**Rejecting test**: show quasi-1-D steady nozzle flow admits standing normal shocks only at
isolated back pressures (contradicted by every compressible-flow text's overexpanded-nozzle /
supersonic-diffuser shock-positioning analysis; a derivation to the contrary kills this).

---

## O9 (P2, ABSENCE) — No inviscid-scope line: the boundary-layer upstream-influence channel makes "the protection boundary is exactly the finite-amplitude sector" (Section 5) true only within Euler + slip, and the margin monitor is blind to the physical bypass

**Claim attacked**: Section 5 "The protection boundary is EXACTLY the finite-amplitude sector";
3.4(3) monitor framing ("violation is DETECTED ... not prevented").

**Defect (absence; modeling assertion with classical basis).** Everything in the document lives in
compressible EULER with slip walls — correctly, since that is the certified model class. But the
composite claim of Section 5 asserts EXACTNESS of the protection boundary without naming the model
scope, and the operational monitor discussion never mentions the classical fact that in the
physical device upstream influence in nominally supersonic duct flow occurs at ARBITRARILY SMALL
overpressure through the subsonic near-wall layer: free-interaction/upstream-influence lengths of
shock-boundary-layer interaction, pseudo-shock/shock-train upstream creep — the standard
experimental unstart precursor is exactly this channel, active far below Pi*. Within Euler+slip
the document's boundary is (subject to O3) right; as the theory feeding a MONITOR on a real
nozzle certificate, omitting the one physically dominant sub-threshold upstream channel from even
a scope remark is a completeness defect under the repo's own claim-hygiene (every claim with
hypotheses explicit — the hypothesis "inviscid, slip walls" is stated for the theorems but the
Section 5 composite and the monitor role paragraph do not restate or inherit it where it bites).

**Rigor class of objection**: absence claim (checkable by grep: no occurrence of "viscous",
"boundary layer", "inviscid" as a scope word in the document); the physics clause is a modeling
assertion resting on classical SBLI phenomenology.
**Severity**: P2.

**Repair path**: one scope paragraph: "All statements are Euler + slip; the viscous near-wall
subsonic layer is a distinct upstream-influence channel outside this model, active below Pi*, and
is NOT monitored by the margin certificate — it belongs to the model-validity envelope (I-ladder),
not to R1"; optionally a monitor implication (wall-pressure creep sensor upstream of Gamma_d).

**Rejecting test**: exhibit the scope line in the document (a full-text search for
viscous/boundary-layer scope language returns nothing beyond "slip walls" as a hypothesis), or
argue the L4 contract already excludes wall layers BY DEFINITION at Gamma_d (it constrains data ON
Gamma_d, which does not remove the upstream wall-layer path in the physical duct).

---

## O10 (P3) — Falsifier defects (four)

 (a) **Theorem 3 falsifier under-specified.** "margin state M_x, downstream overpressure Pi; track
     the front" — a generic downstream pressurization (p raised, rho/u not RH-matched) resolves
     into a 3-wave fan whose UPSTREAM-running shock has strength Pi_left < Pi; testing arrival
     against Pi*(M_x) with the imposed Pi mis-anchors the pass/fail line (a harness could
     spuriously "refute" 3b(iii) with Pi slightly above Pi* but Pi_left below it). The harness
     must either initialize the exact RH pair of 3.3 or derive and use the fan map Pi ↦ Pi_left.
     *Rigor: complete (elementary Riemann-solver structure). Rejecting test: show the falsifier
     text pins the initialization to the 3.3 RH construction (it does not; it says "downstream
     overpressure Pi").*
 (b) **Register row 3d declares falsifier "n/a".** The document's own preamble promises "Every
     statement carries ... a rejecting falsifier (Section 6 table)", and repo R5 requires a
     falsifier per claim. 3d contains testable content: the amplitude-ball clause of 3.4(1)
     ("inside the amplitude ball of radius ~ (Pi* − 1) the linear conclusion is not contradicted")
     is directly testable — nonlinear vs linearized runs at Pi below/above Pi*, agreement scaling
     in the sub-threshold ball; the row should carry it. *Rigor: complete (textual + constructive).
     Rejecting test: an argument that 3d is genuinely non-empirical — but its amplitude-ball
     sub-claim is quantitative, so the row is not fully meta.*
 (c) **Theorem 2 falsifier control may be vacuous-by-unavailability.** The control requires "the
     same probe on a subsonic-patch closure run"; the certified pipeline (engine X-TOCV class) is
     a supersonic marching engine — if no subsonic-closure artifact exists, the control clause can
     never fire and the falsifier self-weakens to the bit-identity check (which tests code
     hygiene, not the theorem). Name the control artifact or substitute an executable control
     (e.g., the Corollary 4 impedance tube). *Rigor: sketch (depends on pipeline inventory).
     Rejecting test: point to an existing subsonic-closure run artifact in the repo.*
 (d) **Corollary 4 claim (i) label.** Existence for the dissipative-BC IBVP is invoked as
     "(linear symmetric hyperbolic with dissipative BCs) follow" with no citation, inside a
     THEOREM (complete) label; by the document's own vocabulary the existence clause is THEOREM*
     (Friedrichs/Lax-Phillips/Rauch dissipative boundary theory) — the energy estimate and
     uniqueness are complete, existence is cited-standard. *Rigor: complete (label semantics).
     Rejecting test: a self-contained existence proof present in the document (there is none —
     only the estimate is derived).*

---

## O11 (P3) — Theorem 1, hypothesis (ii) is stronger than the physically posed inflow condition; Remark 1.5.4's "solution operator" reading needs (and can have) the incoming-only version; plus one garbled proof sentence

**Claim attacked**: Theorem 1 hypothesis "(ii) U^(1) = U^(2) on the inflow face Gamma_in" (full
trace); Remark 1.5.4 "the upstream solution operator does not see (data, forcing, state) on
{x > x_I}"; Theorem 2(b) proof sentence "(the wall normal has n_x = 0 component handled
identically ...)".

**Defect.** (i) The physical IBVP prescribes only INCOMING characteristic data on Gamma_in; two
physical solutions with the same inflow data agree in incoming components there, but their full
traces need not be assumed equal — the outgoing part is determined by the interior. Theorem 1 as
stated is TRUE but its hypothesis (ii) does not match the problem whose "solution operator"
Remark 1.5.4 invokes; the mismatch is free to repair because the same proof works: S A(n) is
symmetric, so the boundary form diagonalizes in characteristic coordinates and at an inflow face
the difference's incoming components vanish, leaving −∫⟨S A(n)U,U⟩ ≤ 0 over the outgoing
subspace (nonneg-eigenvalue part... at inflow u·n < 0 the outgoing modes have lambda of the sign
that makes the flux term dissipative on the difference). State the incoming-only corollary or
weaken (ii). *Rigor: complete for the mismatch; sketch for the corollary proof (one paragraph of
sign bookkeeping).* (ii) The Theorem 2(b) parenthetical asserts "the wall normal has n_x = 0
component" — false for a duct with varying cross-section (the wall normal has n_x ≠ 0 wherever
r_w'(x) ≠ 0); the PROOF is unaffected because (BQ) kills the wall flux for ANY n with u·n = 0,
u'·n = 0 (verified, item 6), but the sentence as written is wrong and should say exactly that.
*Rigor: complete. Severity: P3 both.*

**Rejecting test**: for (i), show Remark 1.5.4 is consumed only in difference-of-solutions form
with full-trace-matched inflow everywhere downstream in the program (then the mismatch is
harmless-as-consumed and this drops to editorial); for (ii), textual.

---

## Verdict

**REPAIRABLE.**

The core of the deliverable is genuinely strong: Theorem 1's C^1 proof, Theorem 2(a)-(b), the
Lemma 0.1/0.2/1.1/1.2/2.1/3.1 algebra, the 3a/3b identities, and Corollary 4's exhibits all
survived full recomputation, and the honest three-layer architecture (linear theorem / steady
theorem / priced finite-amplitude boundary) is the right epistemology for the L4 monitor. But the
document is not sound AS LABELED: two THEOREM-labeled links in the Section 3 chain fail their own
standard (O1 quantifier/domain breach on the Hugoniot; O2 compressive-branch gap — both
constructively repairable in-window), the composite statement makes the finite-amplitude exclusion
in a generality proved only for normal fronts (O3 — the sharpest physics gap: the oblique-front /
leading-point question is the actual duct-unstart mechanism and is unadjudicated), the necessity
("only then") rhetoric fails in the document's own I2 meridional class (O4), one THEOREM* label
rests on non-covering citations (O5), and there are one phantom proof step (O6), one placeholder
display inside a theorem block (O7), a phenomenology mislabel (O8), a missing inviscid-scope line
(O9), and falsifier/hypothesis hygiene items (O10, O11). No objection kills L4 ⟹ R1 at the
linearized/steady level; every objection has a named, executable repair.
