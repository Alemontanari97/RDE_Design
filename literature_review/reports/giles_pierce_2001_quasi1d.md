# Expert read — Giles & Pierce, "Analytic adjoint solutions for the quasi-one-dimensional Euler equations" (JFM 2001)

Reader role: expert reader in a convergence review. Metro di confronto = APPARATUS BRIEF (record state, 2026-08-12/13).
Date of read: 2026-08-13.

---

## 1. Citation (verified from the PDF itself)

Michael B. Giles & Niles A. Pierce, *Analytic adjoint solutions for the quasi-one-dimensional Euler
equations*, **Journal of Fluid Mechanics (2001), vol. 426, pp. 327–345**. Cambridge University Press.
Received 11 June 1998 and in revised form 8 August 2000.
Affiliation printed: Oxford University Computing Laboratory, Oxford, OX1 3QD, UK; Pierce's present
address footnote: Applied Mathematics, California Institute of Technology, Pasadena, CA 91125, USA.
DOI printed in the sidebar watermark: `https://doi.org/10.1017/S0022112000002366`.
Funding line (p. 344): "This research was supported by EPSRC under grant GR/K91149."

## 2. Read coverage

**19 / 19 PDF pages read in full** (journal pp. 327–345), including the complete REFERENCES list on
pp. 344–345 and all four figures (pp. 341–344). Nothing was skipped. No supplementary material exists.
Page citations below are the **journal** page numbers printed on the page.

---

## 3. What the paper actually does

**Problem.** NOT a design problem. It is an *analysis* of the analytic properties of the **adjoint
solution** of the steady quasi-one-dimensional Euler equations in a converging–diverging duct of given
cross-section `h(x)` on `−1 ≤ x ≤ 1` (p. 329, §2). The duct shape is DATA, never an unknown. The paper's
two headline results are (i) at a shock the adjoint variables are **continuous, with zero gradient**, and
an **internal adjoint boundary condition** is required there; (ii) there is a **logarithmic singularity**
in the adjoint variables at a **sonic throat**.

**Formulation.** Continuous (differentiate-then-discretize) adjoint. Flow residual
`R(U,h) ≡ d(hF)/dx − (dh/dx) P = 0` with `U = (ρ, ρq, ρE)`, `F = (ρq, ρq²+p, ρqH)`, `P = (0, p, 0)`
(p. 330), closed by the ideal-gas relation `H = E + p/ρ = γ/(γ−1) p/ρ + ½q²` (p. 330). Linearization gives
`Lu − f = 0`, Eq. (2.1). The **objective is `J = ∫_{−1}^{1} p dx`** — the pressure integral — chosen
explicitly "since this mimics the lift integral which is of importance in aeronautical applications"
(p. 330). Its linearization Eq. (2.2) carries the shock-displacement term `− [p]_{x_s^-}^{x_s^+} δ`.
The augmented functional uses **continuous multipliers `v` on each side of the shock plus a separate
multiplier `v_s` enforcing the Rankine–Hugoniot conditions at the shock** (p. 330) — this explicit RH
multiplier is the paper's technical novelty relative to the standard Jameson-1995 formulation.

**Unknowns.** The three adjoint variables `v(x)`; the linearized shock displacement `δ` is eliminated,
not solved for. Adjoint operator (p. 331): `L*v ≡ −h Aᵀ dv/dx − (dh/dx) Bᵀ v`, adjoint o.d.e. `L*v − g = 0`
Eq. (2.4) with `g = (∂p/∂U)ᵀ`.

**Constraints / conditions derived.**
- Continuity at the shock: `v(x_s^−) = v_s = v(x_s^+)` (p. 331) — *proved*, not assumed.
- Internal adjoint boundary condition at the shock, Eq. **(2.5)**: `v₂(x_s) = − (dh/dx (x_s))^{−1}` (p. 331).
- Zero adjoint gradient at the shock: writing the adjoint system in non-conservative variables
  `U_p = (ρ,q,p)ᵀ`, Eq. (2.5) forces `dv/dx = 0` at the shock (p. 332).
- Boundary-condition counting rule (pp. 331–332): "At a boundary where the flow equations have `n`
  incoming characteristics, and hence `n` imposed boundary conditions, the adjoint equations will thus
  have `(3 − n)` boundary conditions corresponding to an equal number of incoming adjoint characteristics".
- Characteristic count at the shock (p. 332): "at the shock, there are three outgoing characteristics on
  the upstream side and one outgoing characteristic on the downstream side. Continuity of the adjoint
  variables across the shock provides three conditions and the additional shock boundary condition
  provides a fourth."

**Flow model.** Steady, inviscid, quasi-1D Euler; **perfect gas with constant γ**; at most one normal
shock, treated as a **fitted discontinuity** with exact RH jump `[F]_{x_s^-}^{x_s^+} = 0` (p. 330). No
viscosity, no chemistry, no unsteadiness, no multi-dimensionality.

**Solver.** No numerical optimizer. A **Green's-function construction** (§3, p. 332): solve
`L u_j(x,ξ) = f_j(ξ) δ(x−ξ)`, Eq. (3.1); then Eq. (3.2)
`vᵀ(ξ) = (I₁(ξ)|I₂(ξ)|I₃(ξ)) · (f₁(ξ)|f₂(ξ)|f₃(ξ))^{−1}`.
The key device is choosing the three source vectors as the derivatives of `F` with respect to the three
**quasi-1D flow invariants** — mass flux `mh ≡ ρqh`, stagnation enthalpy `H`, stagnation pressure `p₀`
(p. 333): `f₁ = ∂F/∂m|_{H,p₀}`, `f₂ = h ∂F/∂H|_{p₀,M}`, `f₃ = h ∂F/∂p₀|_{H,M}`, with jump relations (3.3)
on p. 334. Closed-form adjoint solutions are then obtained regime by regime: **supersonic (§4),
subsonic (§5), isentropic transonic (§6), shocked transonic (§7)**, the shocked case requiring the shock
displacement from the normal-shock relations and Eq. (7.1) (p. 337).

**Key derived singularity (§6.1, p. 336).** Because `∂p/∂m|_{H,p₀} = −q/(1−M²)` and `M` varies
approximately linearly through a choked throat, `∂p/∂m ~ 1/x` as `x → 0`, hence
`I₁(ξ) ~ log(ξ)` as `ξ → 0`, "so there is a logarithmic singularity in the adjoint variables at a sonic
throat."

**Verification.** Two independent legs. (a) Internal consistency: the closed-form solutions of §§4–7
reproduce the properties proved in §2. (b) Numerical: "The analytic results have been verified using
numerical solutions obtained by discretizing the adjoint equation (2.4) directly (Giles & Pierce 1998)"
(p. 342). Sample cases (§8, p. 341) use the explicit duct
`h(x) = 2` on `[−1,−½]`, `1 + sin²(πx)` on `(−½,½)`, `2` on `[½,1]`, with figure conditions
Fig. 1 supersonic `M_in = 3, H_in = 4, p₀_in = 2`; Fig. 2 subsonic `H_in = 4, p₀_in = 2, p_ex = 1.98`;
Fig. 3 isentropic transonic `H_in = 4, p₀_in = 2`; Fig. 4 shocked `H_in = 4, p₀_in = 2, p_ex = 1.6`.

**Explicit corrections of prior literature (p. 332).** Iollo, Salas & Ta'asan (1993) suggested imposing
`v = 0` at the shock: "this over-constrains the adjoint problem, in addition to contradicting (2.5)."
Cliff, Heinkenschloss & Shenoy (1996, 1998) concluded there is a "shock" in the adjoint variables:
"as this change of sign is entirely due to the non-standard coordinate system they employ … the
conclusion that the adjoint variables are discontinuous at the shock is misleading."

**Two-dimensional outlook (p. 343, ASSERTED / preliminary, not proved).** Adjoint again continuous at a
shock; an adjoint boundary condition is required *along the length* of the shock; current transonic
airfoil adjoint codes do not enforce it and "it remains an open question as to whether there is a
consistency error in the limit of increasing grid resolution". In 2-D, "numerical evidence suggests that
there is no longer a singularity at a sonic line if (as is usually the case) it is not orthogonal to the
flow". At stagnation points "the analysis indicates an inverse square-root singularity along the incoming
stagnation streamline, but further numerical experiments are required to confirm this behaviour".

---

## 4. Hypotheses

### Declared
H-a. Steady, inviscid, quasi-one-dimensional Euler in a duct of given `h(x)`, `−1 ≤ x ≤ 1` (p. 329).
H-b. Ideal gas, `H = γ/(γ−1) p/ρ + ½q²` with **constant γ** (p. 330) — i.e. calorically perfect.
H-c. Single normal shock at `x_s`, RH conditions `[F] = 0` enforced exactly (p. 330); shock **fitted**.
H-d. Objective is the pressure integral `∫ p dx`; other objectives allowed "with only minor changes"
     (p. 330) — an ASSERTION, not demonstrated.
H-e. `h(x)` piecewise differentiable, so that `dM/dx` follows analytically from the area–Mach relation
     with `h* ≡ h_t` at the sonic throat (p. 337).
H-f. Throat is choked/sonic in §§6–7; all perturbations vanish upstream of the throat in the choked
     case (p. 338, §7.2.1).

### Undeclared but necessary
H-g. **`dh/dx(x_s) ≠ 0`.** Eq. (2.5), `v₂(x_s) = −(dh/dx(x_s))^{−1}`, is meaningless for a shock standing
     in a constant-area section. The sample duct has `dh/dx ≡ 0` on `|x| ≥ ½`, and the Fig. 4 shock sits
     inside the bump — the hypothesis is satisfied by construction but never stated.
H-h. **Linear variation of `M` through the throat**, `M − 1 ∝ x` (used verbatim on p. 336 as "M varies
     approximately linearly through a choked throat"). The `log` result is an *asymptotic* statement
     conditional on this local behaviour, i.e. on a non-degenerate throat (`d²h/dx² ≠ 0` at `x = 0`).
H-i. **Existence, uniqueness and smoothness of the nonlinear quasi-1D solution** on each side of the
     shock, and of the linearized solution; never proved.
H-j. **Invertibility of `(f₁|f₂|f₃)`** — Eq. (3.2) presumes the three source vectors are linearly
     independent everywhere, which fails wherever the map `(m,H,p₀) ↦ U` degenerates (in particular the
     `1/(1−M²)` factor at `M = 1`; this is the same degeneracy that produces the log singularity).
H-k. **Lax-admissible, genuinely nonlinear single shock**; no contact discontinuities, no shock/throat
     coincidence, no shock at a boundary.
H-l. **Non-vanishing determinant** in the §7.3 `2 × 2` system, asserted ("the determinant of this system
     is non-zero", p. 339) without proof, to conclude `a = c = 0`.
H-m. Formal exchange of limits / integration by parts across the delta sources and across the shock
     (p. 331) — the manipulations are formal, in the classical-solution sense, not distributional-rigorous.

---

## 5. Findings — three-level comparison with the programme apparatus

### LEVEL: TEORICO

**T1 — GAP-CONFIRMS (P2/G14, claim 8 "empty niche"). CONFIDENCE: ALTA.**
The bibliography verdict requested by the litmap is **CONFIRMED, not refuted**. The full reference list
(pp. 344–345, 26 entries) contains **NO Rao, NO Guderley, NO Hantsch, NO Hoffman, NO Kraiko, NO
Shmyglevskii, NO Sirazetdinov, NO Scofield, NO Beck** — no classical variational nozzle reference of any
kind. It also contains **no Lions and no Pironneau** (Jameson 1988/1995/1999 and Jameson–Pierce–Martinelli
1998 are present; Lozano post-dates this paper). This is the strongest possible form of the evidence for
P2/G14: the paper's flow configuration — a converging–diverging duct with a sonic throat, a fitted normal
shock and an integrated wall-pressure functional — is *the* quasi-1D shadow of Rao's problem, and the
modern adjoint school still never touches the classical multiplier-field corpus. The blindness is
symmetric and total. Record this as a page-verified data point.

**T2 — CONTAINED. CONFIDENCE: ALTA.**
The paper's whole formulation is a strict restriction of the programme's **Route B** limb of T7(a):
multiplier fields adjoined pointwise to every flow PDE, adjoint hyperbolic on the flow's own
characteristics, optimality/sensitivity read off boundary terms. Exact restricting hypotheses:
(i) quasi-1D area-law flow instead of the axisymmetric `δ`-geometry; (ii) **single phase** — a Dirac
measure `μ = δ_{ξ₀}`, so the entire cycle layer (T7(b),(c), the weighted transversality (\*\*')) is void;
(iii) objective `∫ p dx` rather than the thrust integrand `f₁`; (iv) geometry FIXED — no shape unknown,
no `λ₂` mass multiplier, no `λ₃` length multiplier, no free endpoint, hence no Rao-type corner condition;
(v) constant `γ`, whereas E4 requires EOS-generality. Evidence: p. 330 (residual + objective), p. 331
(`L*`, Eq. (2.4)), p. 332 (adjoint characteristics reversed). Nothing in the paper lies outside (P).

**T3 — GAP-CONFIRMS (F4b, "jump / discontinuity conditions, OPEN"). CONFIDENCE: ALTA.**
The programme's F4b entry states that fitted-front adjoint jump conditions are an open item and that the
tier-1 certificate list is shock-shaped. Giles & Pierce prove, in the *simplest possible setting* (1-D,
one shock, perfect gas), that an **internal adjoint boundary condition at the front is mathematically
mandatory** — without it the adjoint problem is under-determined (p. 332, characteristic count:
3 upstream + 1 downstream outgoing adjoint characteristics = 4 conditions needed; continuity supplies 3,
the shock BC the 4th). If the condition is unavoidable in 1-D, it is unavoidable in F4b. The gap is real
and now has a lower-bound witness.

### LEVEL: FORMALE

**F1 — ADOPT (characteristic-counting well-posedness audit). CONFIDENCE: ALTA.**
Adopt verbatim the rule on pp. 331–332: "At a boundary where the flow equations have `n` incoming
characteristics, and hence `n` imposed boundary conditions, the adjoint equations will thus have `(3 − n)`
boundary conditions corresponding to an equal number of incoming adjoint characteristics", together with
the shock count on p. 332. **Insertion point:** the F4b certificate list (currently RH + entropy + Lax +
Lopatinskii) gains a fifth, cheap, purely combinatorial member — an *adjoint BC-count audit* per boundary
and per fitted front. In the axisymmetric rotational MoC march the local characteristic set is
{streamline, C⁺, C⁻}, so the count is again 3 per node and the audit is directly transcribable. It also
sharpens the brief's Route B statement: the brief says the adjoint PDEs are "hyperbolic with the SAME
characteristics as the flow"; the missing half — *information travels along them in the opposite
direction* (p. 332) — is precisely what makes the count come out, and should be added to the Route B text.

**F2 — ADOPT (explicit internal condition + zero-gradient certificate). CONFIDENCE: ALTA.**
Two concrete, machine-checkable objects: Eq. **(2.5)** `v₂(x_s) = −(dh/dx(x_s))^{−1}` (p. 331), and its
corollary in non-conservative variables `dv/dx = 0` at the shock (p. 332). **Insertion point:** F4b, as
the quasi-1D specialization/known-answer form of the fitted-front adjoint jump conditions, and — more
immediately useful — as a **negative-control certificate**: on a fitted-front test case the discrete
adjoint gradient must vanish at the front, and a seeded corruption of the RH multiplier must break it.
This is exactly the shape of certificate the programme already uses for O3.1.

**F3 — THREAT (sonic-throat logarithmic singularity). CONFIDENCE: ALTA (that the singularity exists);
MEDIA (on the size of the threat to our bars).**
§6.1, p. 336: `∂p/∂m|_{H,p₀} = −q/(1−M²) ~ 1/x` at a choked throat, hence `I₁(ξ) ~ log(ξ)` and
"there is a logarithmic singularity in the adjoint variables at a sonic throat" — visible in Fig. 3
(p. 343) and Fig. 4 (p. 344). Consequences for the apparatus: (a) any statement of the form "the adjoint
field is bounded / `O(h²)` uniformly" is **false at the sonic line**, so per-cell truncation bands and DWR
bars (VI.6) cannot be uniform across a kernel/throat region; (b) the singularity is only *logarithmic*,
hence integrable, so functionals and the `f₂ = −λ₂` first integral along the *terminal* characteristic —
which lives strictly supersonic, downstream of the sonic line — are not directly hit; (c) the programme's
MoC march starts from an initial-value line near the throat, i.e. **exactly where the adjoint kernel is
unbounded**, so the initialization of the adjoint sweep is the exposed spot. Note the 2-D mitigation the
paper itself offers (p. 343): no singularity at a sonic *line* that is not orthogonal to the flow — but a
nozzle throat's sonic line is the canonical near-orthogonal case, so the mitigation does **not** apply to
us. Register this as a named limitation of the DWR/truncation-band discipline, not as a refutation.

**F4 — CORRECTION (scoped, to the F4b narrative, not to a numbered claim). CONFIDENCE: MEDIA.**
The brief says F4b "fitted-front adjoint jumps inherit the Kraiko discontinuous-multiplier structure".
Giles & Pierce prove the opposite-sounding statement in quasi-1D: with the RH conditions enforced by an
explicit multiplier `v_s`, the adjoint variables are **continuous** across the shock (p. 331), and they
explicitly label the contrary conclusion of Cliff *et al.* (1996, 1998) as "misleading", an artifact of a
non-standard coordinate system (p. 332); and they reject Iollo *et al.* (1993)'s `v = 0` at the shock as
over-constraining. These are not formally contradictory — Kraiko's multiplier discontinuities are jumps
*along characteristics*, with derived jump conditions, whereas Giles–Pierce concern continuity *across the
front* — but the current one-line F4b narrative invites the wrong inference. **Required repair:** state
in F4b that (i) across a fitted front, RH-enforced adjoint variables are expected CONTINUOUS (Giles–Pierce
quasi-1D result), (ii) the Kraiko structure supplies jumps along characteristic surfaces, a different
object, and (iii) the two must be reconciled explicitly before the F4b jump conditions are declared. Also
note for the litmap: this paper is *not* the authority for "captured-shock adjoints rejected" — that
citation belongs to Giles–Ulbrich/Lozano; what this paper supplies is the **fitted-front** side.

### LEVEL: ALGORITMICO

**A1 — ADOPT (external known-answer oracle for the adjoint machinery). CONFIDENCE: ALTA.**
This is the single highest-value item in the paper for the programme. §§4–7 deliver **closed-form adjoint
solutions in four flow regimes** (supersonic, subsonic, isentropic transonic, shocked transonic) on a
fully specified duct `h(x) = 2 / 1+sin²(πx) / 2` with fully specified boundary data (§8, p. 341, and the
captions of Figs. 1–4). The authors state the intent themselves: "it is hoped that the analytic solutions
will also serve as a useful set of test cases for researchers developing adjoint numerical methods"
(p. 329) and "this closed form solution should be very helpful as a test case for others developing
numerical methods for the adjoint equations" (p. 342, Conclusions). **Insertion point:** VI.6 certificate
stack, as a new oracle alongside O1–O5 — call it an *analytic quasi-1D adjoint oracle*: build a quasi-1D
`custom_vjp` march on this duct, run the reverse sweep, and compare against `v(ξ)` from Eq. (3.2) over the
four regimes, with a derived tolerance and a seeded-corruption rejector. It is cheap (1-D, closed form),
regime-complete (it exercises sonic and shock behaviour), and, crucially, **independent of GENO** — it
satisfies the standing "GENO-independent invariants" directive head-on.

**A2 — THREAT (O3.1 / Lemma-B guarantee is self-consistency, not fidelity). CONFIDENCE: MEDIA.**
Claim 13 as literally worded survives — it asserts a *discrete* transposition identity and measures it
(2.7e-10 vs 5.1e-8). The threat is against over-reading it as evidence that the discrete adjoint
approximates the *continuous* adjoint. A dot-product identity `⟨w,Jv⟩ = ⟨Jᵀw,v⟩` is satisfied exactly by
any consistently-assembled transpose, including the transpose of a discretization whose continuous limit
is the wrong adjoint problem — and the shock is precisely where this bites: Giles & Pierce observe that
some discretizations reproduce correct adjoint shock behaviour "without explicit enforcement of the
internal adjoint boundary condition" (p. 332), i.e. the discrete outcome is *discretization-dependent* and
can only be adjudicated against a reference solution. Combined with the 2-D open consistency question
(p. 343), the conclusion is: **O3.1 must be paired with A1's known-answer oracle before "the adjoint is
correct" is claimed anywhere near a fitted front or a sonic line.** Recommend recording this as a scope
qualifier on claim 13 rather than a defect.

**A3 — GAP-CONFIRMS (VI.3 pin "differentiate the fitted front, never a captured smear").
CONFIDENCE: ALTA.**
The programme's VI.3 pin gets independent structural support from the fitted side: the *only* way Giles &
Pierce obtain a well-posed, fully determined adjoint at the discontinuity is by enforcing RH explicitly
with its own multiplier `v_s` (p. 330), which then *derives* continuity, the internal condition (2.5) and
`dv/dx = 0`. Conversely, the paper flags that codes which do not enforce the internal condition face an
open consistency question in the grid-refinement limit (p. 343). Both halves point the same way as the pin.

**A4 — ADOPT (singularity-aware mesh policy). CONFIDENCE: MEDIA.**
pp. 343–344: "Where there are singularities in the adjoint variables it is desirable to greatly increase
the grid resolution so as to reduce the contribution of the local truncation error to the error in the
functional." **Insertion point:** the VI.4/VI.5 discretization policy already splits Gauss panels at switch
phases `ξ*(Σ)`; the spatial analogue is an adjoint-singularity-aware refinement near the sonic/kernel
region, derived from F3 rather than tuned. This is the same principle (refine where the dual is singular)
already implicit in the DWR bars, made explicit and located.

---

## 6. Bibliography inspection (record datum)

Full reference list read, pp. 344–345, 26 entries.

**Classical nozzle line — ABSENT, without exception.** No Rao (1958/1961), no Guderley, no Hantsch,
no Guderley–Hantsch, no Hoffman, no Scofield–Hoffman, no Kraiko, no Kraiko–Osipov, no Shmyglevskii, no
Sirazetdinov, no Nikol'skii, no Rao–Beck. No Russian-school reference of any kind. **The litmap's "NO" is
CONFIRMED.**

**Modern adjoint line — partially present.** Present: Jameson 1988, 1995, 1999; Jameson, Pierce &
Martinelli 1998; Reuther *et al.* 1996, 1999a, 1999b; Giles & Pierce 1997, 1998, 1999, 2001; Pierce &
Giles 1998, 2000; Elliott & Peraire 1997; Anderson & Bonhaus 1999; Newman *et al.* 1999; Iollo, Salas &
Ta'asan 1993; Iollo & Salas 1996; Cliff, Heinkenschloss & Shenoy 1996, 1998.
**Absent: Lions; Pironneau; Lozano** (the latter post-dates the paper). Error-estimation / adaptivity
strand present: Johnson, Rannacher & Boman 1995; Becker & Rannacher 1998; Paraschivoiu, Peraire & Patera
1997; Süli 1998; Venditti & Darmofal 1999.

Reading: the paper sits squarely and exclusively inside the Jameson–Giles adjoint-CFD lineage plus the
goal-oriented-error-estimation lineage. The classical variational-nozzle corpus is not merely uncited —
it is invisible to this community even when the geometry is a de Laval duct.

## 7. Novelty relative to HTH-1971 / Hoffman-1967

On the **design/optimality** side: **nothing.** The paper never poses an optimization problem, never
varies the geometry, has no free endpoint, no isoperimetric constraints, no transversality condition, and
no thrust functional. Hoffman-1967 Eq. (78) `E = y·h₁ − (u y′ − v)·h₃` is an *optimality residual* on the
designed wall; Giles–Pierce produce no such object.

What it adds is orthogonal and genuinely new relative to 1967/1971: (i) the **adjoint solution itself as
the object of study**, in closed form, for all Mach regimes; (ii) the proof that with RH enforced by a
dedicated multiplier the adjoint is **continuous with zero gradient at a shock** plus a **derived internal
adjoint boundary condition** — a structure the classical school (which used Kraiko's discontinuous
multipliers along characteristics) never wrote down in this form; (iii) the **logarithmic singularity at a
sonic throat**, a statement about the sensitivity kernel that has no classical counterpart; (iv) the link
to **goal-oriented error estimation and adaptive refinement** via `(g,u) = (v, R(U_h))` (p. 329). In short:
the classical corpus gives optimality conditions without adjoint regularity theory; this paper gives
adjoint regularity theory without optimality conditions. **The two never meet — which is exactly the
P2/G14 niche.**
