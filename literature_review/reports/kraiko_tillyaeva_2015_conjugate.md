# Expert read — Kraiko & Tillyaeva 2015, "Conjugate Problem for Lagrange Multipliers"

**Reader role:** convergence-review expert reader. **Date:** 2026-08-13.
**Verdict headline:** this paper is the single most dangerous document found so far for
**Claim A / P2/G14** as literally worded, and it forces a **CORRECTION** of the litmap line
that calls Kraiko–Tillyaeva 2015 "terminology only".

---

## 1. Citation (verified from the PDF)

A. N. Kraiko, N. I. Tillyaeva (Baranov Central Institute of Aviation Motors, 2 Aviamotornaya St.,
Moscow 111116, Russia), **"Conjugate problem for Lagrange multipliers and consequences for
partial differential equations of mixed type"**, *Journal of Mathematical Sciences*, **Vol. 208,
No. 2**, July 2015, **pp. 181–198**. DOI **10.1007/s10958-015-2436-z**. UDC 517.9.
Translated from *Problemy Matematicheskogo Analiza* **80**, April 2015, pp. 31–45.
ISSN line printed on p. 181: `1072-3374/15/2082-0181 © 2015 Springer Science+Business Media New York`.
Submitted 29 August 2014. Supported by RFBR project No. 11-01-00668-a.
Abstract states: "Bibliography: 8 titles. Illustrations: 8 figures." (both verified).

## 2. Read coverage

**18 / 18 pages read in full (pp. 181–198), references page included.** A probe request for
p. 19 returned only 1 page (p. 198), confirming 18 is the total. Nothing was skipped.
Not machine-checkable from this PDF: the Russian-language sources [1]–[3], [6]–[8] behind the
paper's repeated "acting in accordance with the rules in [2]" — the derivation of the Δχ formula
is **not self-contained** and defers to Kraiko, *Variational Problems of Gas Dynamics* (1979).
Figures 3(a), 4, 8 are grayscale field "palettes" read qualitatively only.

## 3. What the paper actually does

- **Problem.** Contour a d_− d_+ f of a Laval nozzle (Fig. 1, p. 182) giving **maximum thrust** for
  given total length X, given mass flow, given stagnation parameters, external pressure p⁺ acting
  on a possible end face f f°. The optimized region **includes the subsonic part**; the contracting
  (subsonic) section is taken as an **abrupt contraction** a d of zero length, suspected optimal.
  The paper's actual question: *is the vertical segment a d a region of boundary extremum under
  one-sided variations δx > 0?* — **and the paper does not answer it** (Sec. 5, p. 197: "In future
  … it will become possible to clarify whether an abrupt contraction is a region of end extremum").
  It builds the machinery.
- **Formulation (p. 183).** χ = (∫_a^{d_−} + ∫_{d_+}^f) y^{ν−1} p dy − (y_f^ν/ν) p⁺, ν = 1 planar,
  ν = 2 axisymmetric. Constraints adjoined pointwise:
  I = χ + (∫+∫) λ₀ L dy + ∬_Ω (λ₁L₁ + λ₂L₂) dx dy, with L₁ = continuity, L₂ = irrotationality (2.1),
  L ≡ y^{ν−1}ρ(u − x′v) = 0 the wall impermeability. **This is Route B verbatim.**
- **Unknowns.** Contour x = x(y) on a d (with x ≡ 0) and on d_+ f, plus the coordinates of the bend
  point d and the endpoint f; multiplier fields λ₁(x,y), λ₂(x,y) and the boundary multiplier λ₀(y).
- **Constraints.** Total length X; fixed mass flow; fixed stagnation parameters; p⁺ external;
  impermeability; one-sided permissible variations δx ≥ 0 on a d_− and Δx_d ≥ 0 — and the explicit
  observation (p. 187) that **δx and Δx_d are not independent** because Δy_d must adjust to hold
  mass flow fixed.
- **Flow model.** Ideal (inviscid, non-heat-conducting) gas; **uniform total enthalpy and entropy**
  ⇒ p, ρ, a functions of |V| only, dp/dV = −ρV, dρ/dV = −ρV/a²; steady; shock-free ("Δχ valid for
  shock-free flows", p. 184); one bend point d with an expansion fan; scales a_*, ρ_*, ρ_*a_*².
  From Sec. 3 on: **perfect gas with constant γ**, ε = (γ−1)/(γ+1).
- **Adjoint (conjugate) system (2.2), p. 184.** R^u = R^v = 0, linear first order in (λ₁, λ₂).
  "For V > a the characteristics of this system coincide with the C^± characteristics of the flow."
  Compatibility along characteristics (2.3): (y^{ν−1}ρ cot μ) dλ₁ ± dλ₂ = 0.
- **Discontinuous multipliers (2.4)–(2.6), pp. 184–185.** Jump lines admit nonzero solutions only
  for x′ = cot(θ ± μ), i.e. **only along characteristics**; [λ₂] ∓ [λ₁]y^{ν−1}ρ cot μ = 0, and
  [λ₂] = ±C √(y^{ν−1}ρ cot μ) with C constant.
- **Adjoint boundary conditions (2.7), (2.8), p. 185.** λ₀ = λ₁ and **λ₂ = −y^{ν−1}ρv on the wall**;
  λ₂ = 0 on the axis and on the horizontal wall i₊a; λ₂ = λ₁ = 0 in the exit section x = X;
  λ₁ ≡ λ₂ ≡ 0 to the right of the characteristic g f.
- **Shape gradient (2.9), p. 186.** Δχ = y_d^{ν−1}(A^y Δy + A^x Δx)_d
  + y_f^{ν−1}[(p − p⁺ − ρuv tan μ)Δy + ρv²(tan μ)Δx]_f + (∫_{d_+}^f − ∫_{d_−}^a) **B^x δx dy**,
  with **B^x = y^{ν−1}ρv(u − λ₁)′**.
- **Optimality conditions (2.10), p. 186.** On d_+f: **B^x = 0 ∝ λ₁ = u + C**;
  **(p − p⁺ − ρuv tan μ)_f ≥ 0**; v_f² ≥ 0. Equalities in the last two fix optimal y_f and x_f.
- **Closed-form adjoint (2.11), p. 186.** λ₁ = u + C, λ₂ = −y^{ν−1}ρv **reduce (2.2) to (2.1)** —
  the adjoint field on the optimal contour is an explicit algebraic function of the primal state,
  valid in the whole triangle h d_+ f h.
- **Recovery of the classical first integrals (2.12), p. 186.**
  **V cos(θ − μ)/cos μ = C₁** and **y^{ν−1}ρV² sin²θ tan μ = C₂ on hf.**
  Redundancy noted: "any of the conditions (2.12) is a consequence of the other and the
  compatibility condition for the C⁺-characteristic" (p. 187, citing [2]).
- **Boundary-extremum conditions (2.13), (2.14), p. 187** for the abrupt contraction a d_−.
- **Sections 3–4 (pp. 187–197), two-dimensional only (ν = 1).** In hodograph variables (V, θ) the
  adjoint reduces to (3.1) and to the second-order equation (3.3),
  (1−V²)²λ_{2θθ} + V²(1−V²)(1−εV²)λ_{2VV} + V[1+(1−2ε)(2−V²)V²]λ_{2V} = 0,
  **elliptic for V<1, hyperbolic for V>1** — a **generalized Tricomi problem**. Sonic-line condition
  λ_{2V} = 0 derived from (ρV)_V = ρ(1−M²) = 0 (p. 188). Eigensolutions λ_{2,n} = φ_n(V) sin(2nθ)
  via ODE (3.4) with singular points V = 0 and V = 1; series starts φ_n = V^{2n} − …; numerical
  integration matched to local expansions; Fourier expansion of the mismatch Δλ₂ in an orthonormal
  system Λ_k on the closing C⁻-characteristic od_o.
- **Key negative structural result (p. 189).** "introduction of discontinuities of Lagrange
  multipliers on the closing C⁻-characteristic od_o **does not delete the mismatch** of curves 1 and
  2; moreover, the tangent to curves 1 and 2 at the point o is horizontal, and to the dashed curve
  it is vertical. By (2.6), we have λ₂ ~ η^{1/4}". Eigensolutions vanish as η^{3/2}; the required
  partial solution behaves as η^{1/4}. Hence Sec. 4 builds a **singular partial solution**
  λ₂ = r^{1/4}λ(V,ϑ) obeying (4.3), fixed by (4.4)–(4.16).
- **Solver.** Direct problem: time-marching ("steading (or pseudosteading) per time") left to right,
  then MoC for the expansion fan and a Goursat problem (p. 182). Conjugate problem: **backward,
  right to left** (p. 182), MoC in the supersonic region, hodograph + separation of variables +
  numerical ODE integration + a numerical **Dirichlet problem** in the subsonic rectangle.
- **Verification.** Qualitative only: Fig. 8 (p. 196), λ(V,ϑ) on three grids (baseline, ×4 cells,
  ×16 cells) — "The results differ only by smoothness of 'isolines'." No error norms, no
  convergence rate, no falsifier. Numerical case of record (p. 189): γ = 1.4, y_a/y_d = 1.5,
  X/y_d = 10, p⁺/p_i = 0, V_i ≈ 0.39, nondimensional mass flow ≈ 0.870.

## 4. Hypotheses

**Declared.** Inviscid, non-heat-conducting ideal gas; **homentropic and homoenergetic**
(⇒ irrotational, hence the two-equation system (2.1)); steady; **shock-free** (stated as the
validity condition of Δχ, p. 184); exactly **one bend point d**, distinct from a and f, streamlined
with an expansion fan; fixed X, fixed mass flow, fixed stagnation parameters, constant p⁺;
zero-length abrupt contraction; **perfect gas, constant γ** from Sec. 3 on; **ν = 1 (planar) for the
whole Sec. 3–4 analysis** ("We restrict ourselves to the two-dimensional case", p. 188).

**Undeclared but necessary.**
1. Existence and uniqueness of the direct-problem solution for every admissible contour.
2. Differentiability of the control-to-state map (the flow response to contour variation) — the
   whole Δχ construction presumes it.
3. Topological stability of the flow structure under permissible variations (single smooth sonic
   line d_−…o; no new shocks appearing in varied flows; the fan structure preserved).
4. Legitimacy of exchanging variation and integration over Ω.
5. **Completeness** of the eigensystem {Λ_k} on od_o and **convergence** of the Fourier series:
   asserted, not proved — "The smoothness of Δλ₂(V) provides its uniform approximation by the
   Fourier series" (p. 191).
6. Solvability/uniqueness of the numerical Dirichlet problem for λ in the subsonic rectangle with
   the prescribed singular arcs at o and d_− (Fig. 6).
7. Well-posedness of the generalized Tricomi problem itself for (3.3) — the paper says it is "of
   intrinsic interest" (p. 197) rather than proving it.
8. Axisymmetric transfer: the ν = 2 case of the mixed-type analysis is **not** carried out; only the
   location of the multiplier discontinuity line is asserted for ν = 2 "Following [2], one can show
   that the same situation holds in the axisymmetric case" (pp. 185–186).

**Proved vs asserted.** *Derived in the paper:* (2.2)–(2.14), (3.1)–(3.4), (4.1)–(4.18) and the
numerical eigen/partial solutions. *Asserted on external authority:* the rules generating Δχ [2];
the redundancy of (2.12) [2]; the ν = 2 continuity statement [2]; the two-bend-point optimal
supersonic contour and its "hundredth fractions of per cent" margin [8]; the historical attribution
to Guderley–Armitage and Sirazetdinov [1],[2].

## 5. Findings

### TEORICO

**T1 — THREAT (ALTA) — hits P2/G14 / Claim A.**
The paper carries out, end to end and inside the classical Russian school, the *mathematical*
identification our claim says nobody publishes: multiplier field (2.2) → **shape-gradient
(Hadamard) formula (2.9) with wall density B^x = y^{ν−1}ρv(u−λ₁)′** → **optimality condition
B^x = 0 ⇔ λ₁ = u + C (2.10)** → **the classical control-contour first integrals (2.12)**. That chain
*is* "Rao's optimality residual = the vanishing of the adjoint-based shape gradient". A hostile
reviewer holding this paper can declare P2/G14 falsified **as literally worded**. What genuinely
survives is narrower and must be re-worded to it: (i) the identification is never stated in
modern-ASO language, (ii) it is never connected to discrete adjoints / reverse-mode AD, (iii) it is
never used to drive a modern gradient-based optimizer. **Evidence:** pp. 184–186, Eqs. (2.2), (2.9),
(2.10), (2.11), (2.12).

**T2 — CORRECTION (ALTA) — hits the litmap/claim-1 wording.**
Our record sentence describes Kraiko–Tillyaeva 2015 as "the Russian school's internal
'сопряжённая задача' terminology (…), which is terminology only". **That is factually wrong.**
The paper formulates, solves and numerically integrates the conjugate problem, and derives the
Route-A optimality conditions from it. The line must be rewritten to: *"a full Route-B→Route-A
derivation inside the classical school, with no contact whatsoever with the modern adjoint
literature."* **Evidence:** title and abstract p. 181 ("We formulate and solve the conjugate problem
for Lagrange multipliers connected with designing a Laval nozzle optimal contour"); Eqs. (2.12).

**T3 — CONTAINED (ALTA) — hits (P) / T7.**
Their problem is exactly (P) restricted to a **single Dirac phase** (|Ξ| = 1, μ = δ), with:
homentropic–homoenergetic irrotational S1 state; shock-free; frozen perfect gas (constant γ from
Sec. 3); ν ∈ {1,2}; constraints = {L = X fixed, ṁ fixed, stagnation parameters fixed}; Pa ≡ p⁺
constant. Under those hypotheses T7(a) collapses to (2.2)–(2.3), T7(b) collapses to **B^x = 0**
(their G-density *is* our G_ξ), and T7(c) collapses to (2.10)₂. Their homentropic–homoenergetic
premise is also **independent confirmation of the S21 audit C1 scoping** of T7(a): the classical
closed forms (2.11)–(2.12) are derived only in the irrotational–homentropic subclass, never for
rotational data. **Evidence:** functional I, p. 183; Eqs. (2.9), (2.10); "the flow of an ideal gas is
uniform with respect to the total enthalpy and entropy", p. 183.

**T4 — GAP-CONFIRMS (ALTA) — hits D2-G3 (claim 7) and the empty-niche claim (claim 8).**
Two independent confirmations. (i) There is **no measure, no family of inflow states, no averaging**
anywhere: χ is a single steady integral at fixed stagnation parameters (p. 183). Gap G3 stands.
(ii) The paper explains *why* the niche is empty, in its own words: "until now, only several such
problems have been solved by the method of Lagrange multipliers since **the direct methods turned
out to be more perspective**" (p. 182). The school itself abandoned the multiplier route for direct
methods — nobody kept the variational MoC formulation and swapped in a modern optimizer.
**Evidence:** p. 182, opening of Sec. 1 continuation; p. 183 functional.

**T5 — THREAT (MEDIA) — hits claim 18 (containment).**
Claim 18 asserts (P)+T7+tier-ladder contains the inviscid-Euler exogenous-measure **core** of every
corpus formulation, with exactly two declared structural non-containments. This paper supplies a
**third**: its design domain includes the **subsonic/transonic (elliptic) region**, so its adjoint is
a **mixed-type generalized Tricomi problem** (3.3), not an S1 MOC-regular object. Our (P) routes
subsonic patches to a *declared closure* O1/O2/O3 and defaults to the L4 interface class (every
patch axially supersonic), so this core is not a restriction of (P) as written. Remedy: declare
non-containment #3 ("design variable inside the elliptic region ⇒ mixed-type adjoint"), rather than
let claim 18 be falsified. **Evidence:** Eq. (3.3), p. 188; abstract p. 181 ("including its subsonic
part"); "leads to an interesting generalization of the Tricomi problem for mixed type equations",
p. 183.

### FORMALE

**F1 — CONTAINED (ALTA) — hits the Route-A first integrals and the f1/λ₃ naming caution.**
Eq. (2.12) is, term for term, our Route-A pair: **V cos(θ−μ)/cos μ = C₁** ≙ our f₂ = W cos(θ∓α)/cos α
= −λ₂ (upper sign, C⁺ family), and **y^{ν−1}ρV² sin²θ tan μ = C₂** ≙ our q ρW² sin²θ tan α = −λ₃ with
the 2π absorbed. This is an **independent classical confirmation of our declared convention note**
(the 2π lives in λ₃; the corpus "f1" label is the length integral, not the thrust integrand). Also
record a **symbol collision hazard for citation**: their λ₁, λ₂ are *multiplier fields* for
continuity and irrotationality, whereas our λ₂, λ₃ are the *constant* Route-A mass and length
multipliers; their C₁ ≙ our −λ₂, their C₂ ≙ our −λ₃. Any citation of this paper in M0 must state
that mapping explicitly. Also adoptable: their redundancy statement — one of (2.12) follows from
the other plus C⁺ compatibility. **Evidence:** Eq. (2.12), p. 186; redundancy remark, p. 187.

**F2 — ADOPT (ALTA) — hits VI.3 / VI.6 / O3.1 / Hoffman-E.**
Two adoptions, both cheap and both *external* truths rather than self-consistency checks.
(a) **Closed-form adjoint oracle.** On the optimal contour and throughout the triangle h d_+ f h,
λ₁ = u + C and λ₂ = −y^{ν−1}ρv, with C fixed by λ_{1f} = −v_f tan μ_f (p. 187). Our current
closed-form initializer is *lip-local* (λ₂(ξ) = −f₂(lip data)); this gives the **field-level**
known-answer over a whole region. Innesto: a new oracle in VI.6 alongside O3 — on a converged
tier-0 optimal bell, the continuous adjoint recovered from our fitted march must match
(u + C, −y^{ν−1}ρv) to a derived band. Unlike the O3.1 transpose identity (self-consistent by
construction), this can fail while the transpose identity passes.
(b) **A second wall residual.** B^x = y^{ν−1}ρv(u − λ₁)′ = 0 ⇔ (u − λ₁) constant along the wall is
the Russian-school counterpart of Hoffman-E; monitoring a single scalar's constancy along the wall
is cheaper than the E-residual and independent of it. Innesto: VI.3 certificate list.
**Evidence:** Eqs. (2.9)–(2.11), p. 186; C determination, p. 187.

**F3 — ADOPT (ALTA) — hits CSTR_PA / CSTR_PB and the transversality bookkeeping.**
Their endpoint condition is an **inequality with complementarity**, not an equality:
(p − p⁺ − ρuv tan μ)_f ≥ 0, becoming an equality only "If there are no restrictions on the
coordinates of the point f". Since ρuv = ½ρV² sin 2θ and tan μ = tan α, this is exactly our
CSTR_PA (p − pa) − ½ρW² sin(2θ) tan α with "= 0" replaced by "≥ 0", the slack being carried by the
end face f f° as a **region of boundary extremum**. Our documents state CSTR_PA as an equality and
handle the fixed-ε case by swapping in the multiplier λ_e; the general KKT-correct statement is the
inequality plus complementarity with the base/end-face area. Innesto: the Route-A formal block in
M0 Part II and the fixed-ε bookkeeping note — the plug base-pressure mirror (CSTR_PB) is the same
structure and should be re-stated the same way. **Evidence:** Eq. (2.10) and the paragraph following
it, p. 186.

**F4 — THREAT (ALTA) — hits F4b and the tier-1 certificate list.**
Our F4b frames adjoint jumps as *fitted-front* objects and its certificate list
(RH + entropy + Lax + Lopatinskii) is, by our own admission, "shock-shaped"; we already flag the
missing contact-discontinuity class. This paper shows a **third class we do not have at all**:
Lagrange-multiplier discontinuities arising on characteristics **while the flow parameters are
perfectly continuous**, caused by a **convex bend of the design contour with an expansion fan** —
"The discontinuities can arise on the characteristics of the Euler equations even if the flow
parameters are continuous [2]. One of the reasons of appearing discontinuous Lagrange multipliers
is the presence convex bends of contours in the flow with formation of expansion fans" (p. 182).
The jump conditions are geometric-only: nonzero jumps exist **only** for x′ = cot(θ ± μ), with
[λ₂] ∓ [λ₁]y^{ν−1}ρ cot μ = 0 and [λ₂] = ±C√(y^{ν−1}ρ cot μ). Consequence for us: any design class
admitting a wall corner (and the literature says the optimum *has* corners — see A4) produces an
adjoint discontinuity that our fitted-front certificate machinery will neither detect nor certify,
and a smooth-adjoint solver will silently smear. Severity is raised by their own negative result:
imposing this jump condition alone **does not** close the problem at the sonic point (p. 189).
**Evidence:** p. 182; Eqs. (2.4)–(2.6), pp. 184–185; mismatch result, p. 189.

### ALGORITMICO

**A1 — ADOPT (MEDIA) — hits the O1/O2/O3 subsonic closure and F2's general engine.**
The adjoint is solved in the **hodograph plane**: (2.2) becomes (3.1), ρVλ_{1V} + λ_{2θ} = 0,
ρ(M²−1)λ_{1θ} + Vλ_{2V} = 0, with a single second-order equation (3.3) whose coefficients depend on
V alone. Two properties worth importing for the subsonic/transonic closure: (i) the adjoint domain
becomes a **fixed quadrangle 0 ≤ V ≤ 1, −π/2 ≤ θ ≤ 0 that is independent of the contour**, so the
subsonic adjoint can be pre-solved once per (γ, boundary data) rather than per design iterate;
(ii) the **sonic-line adjoint condition λ_{2V} = 0**, derived from (ρV)_V = ρ(1−M²) = 0 at M = V = 1
(p. 188), is exactly the kind of derived interface condition our closures currently declare rather
than derive. Import with two declared limits: the hodograph route works only because y^{ν−1} = 1,
i.e. **planar ν = 1 only** — the axisymmetric case is not treated; and the adjoint has a
**fractional-power singularity at the sonic point** (λ₂ ~ η^{1/4}, vertical tangent) that the regular
eigensolutions (~η^{3/2}, horizontal tangent) cannot represent, so a naive collocation basis on the
sonic line will be wrong at first order. **Evidence:** Eqs. (3.1)–(3.3), p. 188; sonic-line remark,
p. 188; η^{1/4} vs η^{3/2}, p. 189 and Eq. (4.1), p. 192.

**A2 — GAP-CONFIRMS (ALTA) — hits the empty-niche claim (8) and our verification standard.**
No modern optimizer appears anywhere: there is no design loop at all, no gradient-descent, no
SQP/trust-region, no AD — the machinery stops at conditions and a forward/backward field solve.
Verification is qualitative only: three grids (baseline, ×4 cells, ×16 cells), "The results differ
only by smoothness of 'isolines'" (p. 196, Fig. 8) — no error norm, no observed order, no rejector,
and no independent cross-code. This confirms both that the niche "keep the variational MoC
formulation, swap in a modern optimizer" is unoccupied by the strongest possible incumbent, and
that our R5/Verdict standard is materially above the state of the art in this line. It also
reinforces the **G5 gate**: the derivation rules for Δχ are deferred to Kraiko 1979 [2] four separate
times, so the human pass on Kraiko-1979 is load-bearing and cannot be discharged from this paper.
**Evidence:** Fig. 8 caption and the paragraph above it, p. 196; deferrals to [2] on pp. 184, 187,
185–186.

**A4 — ADOPT (MEDIA) — hits A_gen / A_h spline class, the sector tournament, and claim 19's cap.**
Reported from [8] (p. 187): "in the presence of an abrupt contraction, the optimal contour of the
supersonic nozzle part consists of not one …, but **two sections**: a short section that contracts
after the lower bend point … and a long extending section adjacent to the first one **also with a
bend**", and "the smooth contours d_+f … are inferior in thrust to contours with two bend points
only by **hundredth fractions of per cent**". Two actions. (i) Our working class A_h is a clamped
smooth spline and **cannot represent an interior wall bend**; add a bend-enabled variant (a knot
with free slope, one per sector) to the sector tournament, so the class boundary is a *choice* and
not an unexamined restriction — this is exactly the H-CLASS axis. (ii) Record the quantitative
context for claim 19: the classical corner-vs-smooth penalty is O(0.0X%) in this configuration,
which is an order of magnitude below our measured in-class surplus (+0.51%) — the two are different
comparisons and must not be conflated, but the datum bounds what our smooth class can be losing to
corners. Also: **procure ref [8]** — A. A. Kraiko, A. N. Kraiko, K. S. P'yankov, N. I. Tillyaeva,
*Fluid Dynamics* **47**(2), 223–238 (2012) — it is the carrier of both numbers.
**Evidence:** p. 187, final paragraph of Sec. 2.

## 6. Bibliography inspection (record datum)

The reference list is **8 titles, all Russian-school or Russian PDE monographs**:

1. A. L. Gonor, A. N. Kraiko, in *Theory of Optimal Aerodynamic Shapes*, pp. 455–492, Mir, Moscow (1969).
2. A. N. Kraiko, *Variational Problems of Gas Dynamics*, Nauka, Moscow (1979).
3. A. N. Kraiko, N. I. Tillyaeva, S. A. Shcherbakov, *Izv. AN SSSR MZhG* No. 4, 129–137 (1986); transl. *Fluid Dyn.* **21**(4), 615–623 (1986).
4. A. V. Bitsadze, *Some Classes of Partial Differential Equations*, Nauka (1981); transl. Gordon & Breach (1988).
5. M. M. Smirnov, *Equations of Mixed Type*, Vysshaya Shkola (1985); transl. AMS (1977).
6. G. G. Chernyi, *Gas Dynamics*, Nauka (1988); transl. CRC Press (1994).
7. A. N. Kraiko, *Theoretical Gasdynamics. Classical and Topical*, Torus Press, Moscow (2010).
8. A. A. Kraiko, A. N. Kraiko, K. S. P'yankov, N. I. Tillyaeva, *Izv. RAN MZhG* **47**(2), 97–113 (2012); transl. *Fluid Dyn.* **47**(2), 223–238 (2012).

**Classical nozzle line.** Guderley and Armitage, and Sirazetdinov, are named **in the body text**
(p. 181, Sec. 1) as the originators of the multiplier method for optimal 2-D and axisymmetric
aerodynamic shapes, but are cited only indirectly, "cf. reviews in [1] and [2]" — **they do not
appear in the reference list**. **Rao, Hantsch, Hoffman, Shmyglevskii, Nikol'skii, Sternin and
Rao–Beck are cited nowhere, in text or list.** The recovery of Rao's first integrals in (2.12) is
presented with **no attribution to Rao at all** — it is framed purely as "the control contour
method [2]".

**Modern adjoint line.** **Completely absent.** No Lions, no Pironneau, no Jameson, no Giles, no
Pierce, no Giles–Ulbrich, no Lozano, no Nadarajah, no Anderson–Venkatakrishnan — no citation of any
kind to Western shape-optimization or adjoint CFD literature, and no use of the words "adjoint",
"shape optimization", "sensitivity" or "gradient" in the modern sense anywhere in the 18 pages.
The paper's own word is "conjugate problem" throughout.

**Consequence of record.** The two schools do not touch in this document. P2/G14 is therefore *not*
falsified in its intended sense (no one bridges the classical multiplier field to modern ASO), but
its **literal wording is falsified** by T1/T2 and must be rewritten before it can be defended.

## 7. Net assessment

- **Nothing here occupies our niche.** No measure, no family of inflow states, no averaged shape
  problem, no modern optimizer, no AD, no certified verification, and the paper's own question is
  left unanswered.
- **One claim is at genuine risk** (P2/G14, literal wording) and **one litmap line is wrong**
  ("terminology only"). Both are repairable by re-wording, not by retreat — but they must be
  repaired in-window.
- **One containment declaration must be added** (mixed-type adjoint with design inside the elliptic
  region).
- **Four concrete imports** are available at low cost: the closed-form adjoint oracle, the B^x wall
  residual, the inequality/complementarity form of the corner condition, and the hodograph
  fixed-domain subsonic adjoint with its derived sonic-line condition.
- **One design-class gap is exposed**: the classical optimum has wall bends; our spline class
  cannot represent them, and the corresponding adjoint discontinuity (in *continuous* flow) has no
  certificate class in our tier ladder.
