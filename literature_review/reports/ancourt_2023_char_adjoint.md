# Expert read — Ancourt, Peter & Atinault (2023), *Adjoint and Direct Characteristic Equations for Two-Dimensional Compressible Euler Flows*

Reader: convergence-review expert reader. Date: 2026-08-13.
Metro di confronto: `reports/00_APPARATUS_BRIEF.md` (record state of the cycle-averaged variational nozzle program).

---

## 1. Citation (verified from the PDF itself)

Ancourt, K.; Peter, J.; Atinault, O. **"Adjoint and Direct Characteristic Equations for Two-Dimensional
Compressible Euler Flows."** *Aerospace* **2023**, *10*(9), 797. MDPI, Basel. DOI
`10.3390/aerospace10090797`. Received 20 July 2023; Revised 8 September 2023; Accepted 10 September
2023; Published 12 September 2023. Pages 1–21 (article number 797, "1 of 21" … "21 of 21").
Affiliations: (1,2) ONERA / DAAA, Université Paris Saclay, Châtillon 92322 and Meudon 92190, France.
Correspondence: jacques.peter@onera.fr. Academic Editor: Carlos Lozano. Open access CC-BY 4.0.
Funding: EU H2020 SENECA (grant 101006742) + SONICE (French DGAC).

**Correction to our INDEX.md**: our entry records the *arXiv preprint* (arXiv:2305.03499) with
"**47 refs**". The peer-reviewed version of record has **45 references** (numbered 1–45; refs 1–27 on
p. 20, refs 28–45 on p. 21). The citable object is the *Aerospace* version, already on disk.

---

## 2. Read coverage

**21 pages of 21 read in full**, including Sections 1–5, Appendix A (the full `K^l_{jx}`, `K^l_{jy}`
coefficient tables, pp. 16–17), Appendix B (equivalence proof (14)⇔(42), p. 18), Appendix C (thrust
shape-optimization assessment, pp. 18–20), and the complete bibliography (pp. 20–21).
Not read (not part of the PDF): the **Supplementary Materials** — "three Python files checking the
formulas of `K^l_{mx}, K^l_{my}, K̃^l_{mx}, K̃^l_{my}`. Two Maple files checking the rank of the
differential forms along the S and C+ curves" (p. 16), hosted at
`https://www.mdpi.com/article/10.3390/aerospace10090797/s1`. Figures were read as rendered images;
numerical values quoted below are those printed in the body text, never read off a plot.

---

## 3. What the paper actually does

**Problem.** *Not* a nozzle-design paper. Two objectives, both stated in the Abstract (p. 1):
(i) "present a linear algebra analysis that greatly simplifies the discussion of the number of
independent characteristic equations satisfied along a family of characteristic curves. This method
may be applied for both the direct and the adjoint problem"; (ii) "to directly derive **in
conservative variables** the characteristic equations of 2D compressible inviscid flows". Then
"the theoretical results are assessed for a nozzle flow with a classical scheme and its dual
consistent discrete adjoint." The declared purpose of the whole construction is **code verification**
of adjoint modules (Conclusions, p. 16; verification framing cited to Oberkampf & Trucano [33]).

**Formulation.** Steady 2D Euler in conservative variables `W = (ρ, ρu, ρv, ρE)`, Eq. (1)–(3), with
flux Jacobians `A`, `B` written out explicitly on p. 2. The Cauchy problem for the *derivatives* of
`W` at a point, using a first-order Taylor expansion between neighbouring points `a`, `b` with
`(dx, dy) = ab⃗`, `t = dy/dx`, `κ = ut − v`, is the **8×8 linear system Eq. (4)**. Its adjoint
counterpart, **Eq. (5)**, is the identical system with `(A, B)` replaced by `(−Aᵀ, −Bᵀ)`. Both are
then abstracted into one **generic system with matrix `K`** built from generic `(A, B)` standing for
either pair (p. 3) — this is the paper's central device.

**Unknowns.** The eight first derivatives `(∂ζ_j/∂x, ∂ζ_j/∂y)`, `j = 1..4`, where `ζ` is either the
conservative state `W` or the adjoint vector `ψ = (ψ₁, ψ₂, ψ₃, ψ₄)`.

**Constraints / structure.** `|K| = |−dx B + dy A| = (−v dx + u dy)²(−v dx + u dy + c dl)
(−v dx + u dy − c dl)` (p. 4). The Cauchy problem is ill-posed iff `|K| = 0`, i.e. on
`S` streamtraces (Eq. 8, all Mach numbers, **double root**), `C⁻` (Eq. 9) and `C⁺` (Eq. 10)
(supersonic only). Where the derivatives are nevertheless bounded, the Cramer numerators must vanish
— that is the characteristic equation (CE).

**Flow model.** 2D **planar** steady Euler, inviscid, **thermally and calorically perfect gas**,
"a constant γ = 1.4 and a constant heat capacity at constant volume `c_v`" (p. 2). No assumption of
irrotationality, constant entropy or constant stagnation enthalpy is made for the general derivation
(explicitly stated p. 6: "without any assumptions of constant stagnation enthalpy, or constant
entropy or null vorticity"); those are added only to recover the classical reduced forms (15)–(17).

**Main theoretical results (things the paper *proves*).**
- §2.4, p. 5: for `t = t±` (a `C⁺` or `C⁻`), `rank(B − tA) = 3` from the eigenanalysis of the Euler
  flux Jacobians; via block-diagonal equivalence `rank K = 7`, so the adjugate has rank one and
  **all CEs along `C±` are proportional — exactly ONE independent CE**, for the direct *and* the
  adjoint problem alike.
- §2.5, p. 6: along `S` (`t = v/u`), `rank(B − tA) = 2`, all minors `K^i_{jx}`, `K^i_{jy}` vanish,
  `rank K = 6`; the CEs must be extracted from the reduced coefficients `K̃` obtained by removing the
  factor `(−v dx + u dy)`.
- §2.3, p. 5, Eq. (11) and following: `K^i_{jx} = −t K^i_{jy}` — the `x`- and `y`-derived CEs are
  proportional, so only one family need be studied.
- §3.2–3.4: the **direct CE in conservative variables, Cartesian frame**, is
  **Eq. (42)**: `γ₁(u + tv)E_c dρ − (γu(u + tv) − 2E_c)dρu − (γv(u + tv) − 2tE_c)dρv +
  γ₁(u + tv)dρE = 0`, with `t = t±` from Eq. (39)/(40) and the quadratic Eq. (41).
  Its equivalence with the classical primitive-variable DCE Eq. (14) is **proved in Appendix B**
  (proportionality factor `(u + t⁺v) tan β`, Eq. (A3)).
- §3.3, Eqs. (34)–(36): three differential forms along `S`; "the rank of the matrix was first
  calculated with the Maple software 2020.0 (Supplementary Materials) and, as expected, is two"
  (p. 10). Eq. (34) is shown to be exactly `ρ^γ d(p/ρ^γ) = 0` (Eq. 37) and `G×(34) + (36)` combined
  with `γ₁×(34)` gives `ρ dH = 0` (Eq. 38) — **`dS = 0` and `dH = 0` along streamlines are contained
  in the derived CEs**, not assumed.
- §4.4, Eq. (44)–(46): from the two streamtrace ACEs (Eq. 45) follows `dλ₁/ds − H dλ₄/ds = 0`, hence
  `λ₁ = Hλ₄ + λ*`; the paper argues `λ* = 0` here because "all trajectories, when traveled in the
  adjoint information propagation direction (that is, backwards) start in a zone where the adjoint
  vector is zero, so that (46) is true over the whole fluid domain, **although the nozzle thrust does
  not exclusively depend on the static pressure**" (p. 14) — i.e. it holds *beyond* the
  Giles–Pierce [41] hypothesis. This last point is **asserted with a supporting figure (Fig. 6), not
  proved**.

**Solver / numerics.** SENECA Mach-1.6 supersonic-transport nozzle (p. 10): the 2D geometry is the
symmetry-plane extraction of an axisymmetric engine contour — the paper flags the consequence
honestly: "**the mass flow rates are different**" and "the flows are also different along the midline
of the nozzle" (p. 11). Inlet `p_i,inl/p_i,∞ = 1.605`, `T_i,inl/T_i,∞ = 1.606`; `M = 1` at throat,
`M ≈ 1.9` at exit. Structured **eight-block mesh, 370,538 cells**; `elsA` finite-volume cell-centred
code [37], **Jameson–Schmidt–Turkel (JST)** scheme [38]. Functional: **Eq. (43)**
`Th = ∫_{Γw}(p − p_∞) ds_x + ∫_{Γinl}(ρu² + p) ds_x`. Adjoint: the **discrete** adjoint module of
`elsA` [39], **dual consistent for Euler on structured meshes except in the cells next to those
adjacent to a boundary** [40] — the paper does *not* apply the boundary fix and therefore
**discards all points inside the first two cells near any boundary** because "slight oscillations in
the adjoint field are observed near the boundaries" (p. 13). Characteristic curves are extracted
a-posteriori by integrating the tangent field `(1, t)` — `(1, v/u)` for `S`, `(1, t⁺)`, `(1, t⁻)` for
`C±` — from a shared seed point at `(615, 130)` mm.

**Verification (the measured numbers of record).**
- Flow accuracy: `L1` relative error on total enthalpy `2.3×10⁻³` (jet) and `2.5×10⁻³` (external
  flow), p. 12.
- Direct CE residual along the extracted characteristics, normalised by the max of its own four
  subparts: **`9.0×10⁻⁸` for `ΞC⁺`, `4.2×10⁻⁸` for `ΞC⁻`** (p. 15).
- Complementary: relative variation of `H` over the streamtrace `2.3×10⁻⁶`, of `S` up to the first
  shock `1.4×10⁻⁶` (p. 15).
- Adjoint CE (ACE) residuals, Eqs. (47)–(50): **`1.8×10⁻⁶` (`Ξ_adj S¹`), `2.6×10⁻⁶` (`Ξ_adj S²`),
  `2.0×10⁻⁶` (`Ξ_adj C⁺`), `9.5×10⁻⁹` (`Ξ_adj C⁻`)** (p. 15).
- Adjoint domain-of-dependence check (§4.3, p. 13): "The exact adjoint of the thrust is expected to be
  zero downstream of the backward `C⁺` characteristic … emanating from the rear of the nozzle, as no
  perturbation downstream of these lines can affect the flow on the support of `T` … This property is
  well satisfied by the discrete adjoint."
- Noted stiffness: "a lower accuracy would be observed for more upwind `C⁺` and `C⁻`. Our
  understanding of this stiffness is the sensitivity of the `c√(u²+v²−c²) = c²√(M²−1)` term in the
  slope of Equation (40) close to the boundary of the supersonic zone, `M = 1⁺`" (p. 16).

**Appendix C — the only optimization content.** Six shape parameters `α₁..α₆` multiplying bump
functions `D^l_y(x,y)` (p. 18, Eqs. (A4)–(A5)); **steepest descent** with a max wall displacement of
5% of throat height per step; `‖∇Th‖ = 12.5e3` at step 1, `12.3e3` at step 2; thrust **+3.1%** then
**+0.7%**; mass flow **+4.19%** then **+0.78%**. The physical reading given (p. 19–20): with a fixed
inlet stagnation state and `M_exit ≫ 1`, "we expect the thrust to be optimized only via an increase
of the mass flow", confirmed by Eq. (A6); the optimizer duly **enlarges the throat**.

---

## 4. Hypotheses

**Declared.**
1. Steady, 2D **planar Cartesian**, inviscid Euler; no body forces, no source terms.
2. **Thermally *and* calorically perfect gas**, `γ = 1.4` constant, `c_v` constant (p. 2). γ enters
   the Jacobians `A`, `B` and every coefficient of Appendix A.
3. `C⁺`/`C⁻` exist only in supersonic zones (Eqs. (9)–(10)); `S` exists at all Mach numbers.
4. `dx ≠ 0` — "For the sake of brevity, we shall not discuss the simple specific case where
   `dx = 0`" (p. 5); and `κ ≠ 0` to pass from Eq. (27) to Eq. (28).
5. Constant `H` for Eq. (15); additionally constant `S` (⇒ irrotational by Crocco) for Eqs. (16)–(17)
   and the Prandtl–Meyer integration.
6. For the numerical section: an inviscid flow fully defined by the two stagnation ratios and the
   far-field Mach number (p. 11).

**Undeclared but necessary.**
7. **Local `C¹` smoothness of both the flow and the adjoint field** along the extracted curves — the
   whole construction rests on first-order Taylor expansions between `a` and `b`. The CEs are
   therefore *invalid across shocks*; the paper implicitly respects this (it quotes `S` variation
   "up to the first shockwave", p. 15) but never states the restriction as a hypothesis. It also
   never engages its own citations [43] "Singular and discontinuous solutions of the adjoint Euler
   equations" and [44] "Watch your adjoints!".
8. **Regularity/mesh-convergence of the discrete adjoint** in the zone where the curves are sampled;
   guaranteed only by *fiat*, via the removal of the first two boundary cells.
9. **Dual consistency** of the JST discrete adjoint away from boundaries, imported from [40] and used
   as the premise that makes the discrete adjoint a legitimate proxy for the continuous one.
10. `λ* = 0` in `λ₁ = Hλ₄ + λ*` requires that **every** backward-traced trajectory originate in a
    zero-adjoint region — a property of *this* configuration and *this* functional support, asserted
    (p. 14) and shown graphically (Fig. 6), not proved in general.
11. **No axisymmetric source term**: the axisymmetric `δ`/`1/y` term of a real nozzle is absent; the
    2D object is a contour extraction, with the mass-flow discrepancy acknowledged but not corrected.
12. In Appendix C: **no mass-flow, area-ratio or length constraint** on the optimization — the design
    problem is unconstrained apart from a per-step displacement cap.

---

## 5. Three-level comparison with the program apparatus

### Level TEORICO

**T-1 — CONTAINED.** The paper's structural core — the adjoint linear system is the direct system with
`(A, B) → (−Aᵀ, −Bᵀ)` (Eq. 5), hence **the same determinant `|K|` and therefore the same
characteristic curves `S`, `C⁺`, `C⁻`** (§2.3, p. 4) — is precisely the Route-B statement carried in
our apparatus ("the first variation yields adjoint PDEs *hyperbolic with the SAME characteristics as
the flow* (streamlines + Mach lines)"), i.e. the field-level limb of **T7(a)** for a single phase.
Their setting is a strict restriction of ours in three named directions: (i) `μ` is a Dirac (one
operating point, no cycle); (ii) planar 2D, no axisymmetry; (iii) **calorically perfect γ = 1.4**,
versus our EOS-general-in-primitive-variables claim **E4**. It is *not* a restriction in one
direction: they keep entropy gradients and vorticity in the general derivation (p. 6), matching our
S1/rotational field-level scope rather than the irrotational–homentropic closed form.

**T-2 — GAP-CONFIRMS (strong, for P2/G14 and for the empty-niche claim).** This is the single most
favourable piece of negative evidence yet found for claim **P2/G14**. The paper is, by construction,
the intersection of the three ingredients of our bridge — *adjoint of the Euler equations* ×
*method of characteristics* × *nozzle thrust functional, including a thrust shape optimization
(Appendix C)* — written in 2023 by the ONERA discrete-adjoint group, with **Carlos Lozano as academic
editor**. And it contains **no trace whatsoever of the variational nozzle-design corpus**: no Rao, no
Guderley, no Hantsch, no Shmyglevskii, no Hoffman, no Kraiko, no Sirazetdinov, no Scofield. Its thrust
optimization (Appendix C) is a six-bump steepest descent on a finite-volume mesh; the MoC appears
*only as an analysis and verification instrument*, never as the state solver of the optimization and
never as the source of an optimality condition. The two literatures are, in this artifact, mutually
invisible. Claim 8 (empty niche: "keep the variational MoC formulation and swap in a modern
optimizer") is **not** occupied by this paper and is reinforced by it.

**T-3 — GAP-CONFIRMS (D2 gap G3).** No measure, no family of inflow states, no shared shape across
operating points, no free-boundary/plug counterpart, no `(**')`-type endpoint condition. The
functional Eq. (43) is a single steady thrust. Nothing here touches the averaged-shape gap.

### Level FORMALE

**F-1 — ADOPT (the highest-value item in the paper).** The **adjoint characteristic-equation residual
as a certificate**: Eqs. (47)–(50) define `Ξ_adj S¹, Ξ_adj S², Ξ_adj C⁺, Ξ_adj C⁻` as line integrals
of the ACE differential forms along independently extracted characteristic curves, and the pass
criterion is that the total be small **relative to the max modulus of its own subparts** — a
self-normalising, scale-free residual (defined for the direct case on p. 14, applied to the adjoint on
p. 15). Measured: `1.8e-6`, `2.6e-6`, `2.0e-6`, `9.5e-9`.
*Why we need it*: our VI.6 stack has **O3.1** (transposition identity `|⟨w,Jv⟩ − ⟨Jᵀw,v⟩| = 2.7e-10`
vs derived tol `5.1e-8`) and the **Hoffman-E residual** on the *direct/optimality* side, but **no
certificate that the adjoint field satisfies the continuous adjoint characteristic ODE**. O3.1 is a
*discrete self-consistency* check: it can pass perfectly while the discrete operator being transposed
is the wrong discretisation of the adjoint PDE. The ACE residual is a *continuous-vs-discrete*
check — strictly complementary, and it is exactly the certificate our stack is missing.
*Innesto*: VI.6, as a new per-phase adjoint oracle (proposed tag **O3.5 / ACE-residual**), evaluated
along each phase's `C±` and along a streamline of the fitted march, with the normalisation recipe
above supplying a *derived* tolerance in the R5 sense.
*Declared cost of adoption*: Eqs. (24)–(26), (42) and all of Appendix A are written for constant `γ`
and `c_v`. Under our thermo pin (`γ(T)` tables, DIR-THERMOTAB) the ACE coefficients must be
**re-derived for the variable-`γ` Jacobians** before the certificate can be armed — the `K`-minor
machinery of §2 is EOS-agnostic in *structure* (it only needs `A(W)`, `B(W)`), so the re-derivation
is mechanical, but it is real work and must be booked, not assumed.

**F-2 — ADOPT (cheap, closed-form).** The adjoint invariant **`dλ₁/ds − H dλ₄/ds = 0` (Eq. 44)** along
streamlines, and its integrated form **`λ₁ = Hλ₄` (Eq. 46)** when the backward trajectory starts in a
zero-adjoint region — verified discretely as `ψ₁ = Hψ₄` (Fig. 6, p. 14). This is an algebraic,
mesh-free, one-line oracle on the multiplier field, and the paper's own contribution beyond
Giles–Pierce [41] is precisely that it survives for a functional (thrust) that is *not* a
pure-static-pressure functional. *Innesto*: our Route-B field limb of T7(a), alongside the
Hoffman-E residual, as an initializer sanity check and a negative control on the reverse-AD adjoint.
*Obligation attached*: our march's adjoint variables are per-node MoC sensitivities, not multipliers
of the four conservative residuals; adopting F-2 requires an explicit declared map from the fitted
march's adjoint to the `(λ₁..λ₄)` conservative-residual multiplier field. Without that map the
identity is not testable on our objects, and this should be registered as the adoption precondition.

**F-3 — CONTAINED / structural refinement worth recording.** The exact **count of independent
compatibility relations** is settled here by a clean rank argument rather than by tradition:
`rank(B − tA) = 3` on `C±` ⇒ `rank K = 7` ⇒ adjugate rank one ⇒ **exactly one independent CE on each
of `C⁺`, `C⁻`** (§2.4, p. 5); on `S`, the double root of `|K|` gives `rank K = 6`, all minors vanish,
and after removing the `(−v dx + u dy)` factor the surviving forms (34)–(36) have **Maple-verified
rank two** (p. 10), equivalent to `dS = 0` and `dH = 0`. Total `1 + 1 + 2 = 4`, matching the four
equations. Our apparatus asserts the "streamlines + Mach lines" structure but does not carry this
multiplicity/count as a stated fact; it is the well-posedness argument underlying our MoC unit
process being neither under- nor over-determined, and it now holds *verbatim for the adjoint system
too*, by the same generic-`K` argument. Recommend recording in M0 Route B as a cited structural fact
(class: THEOREM in the paper's declared model closure — planar, calorically perfect).

**F-4 — CONTAINED, degenerate case, and it corroborates λ₂.** Appendix C's optimization is our
problem **(P) with the mass constraint deleted**: no `λ₂ f₂ⁱ` term, no `ε`, no `L`. The paper then
observes, and its own quasi-1D Eq. (A6) explains, that thrust can only be raised by raising mass
flow, so the descent enlarges the throat (`ṁ +4.19%`, `Th +3.1%`). This is an independent,
externally-published demonstration that the *unconstrained* thrust-maximisation shape problem is
degenerate — i.e. that the constant multiplier `λ₂` on the mass integrand in Route A is
load-bearing, not decorative. Useful as a citable illustration in the paper's Route-A motivation.

### Level ALGORITMICO

**A-1 — THREAT (bounded, but real, against any FV-discrete-adjoint cross-check of our wall
gradient).** §4.3, p. 13, states plainly that the `elsA` JST discrete adjoint is dual consistent
"**but in the cells next to those adjacent to a boundary**"; that "the change in the Jacobian to
obtain the dual consistency in the vicinity of the physical boundaries is complex to implement in an
industrial code. In this study, it is not used and slight oscillations in the adjoint field are
observed near the boundaries"; and that consequently "the points inside the first two cells in the
vicinity of a boundary are removed from the extracted characteristic curves". **The boundary is
exactly where our object lives**: our Hadamard density `G_ξ`, the `(**')` endpoint transversality and
the CSTR_PA/CSTR_PB corner residuals are all *wall* and *lip* quantities. A state-of-the-art
industrial FV discrete adjoint is here documented as *not dual consistent and visibly noisy precisely
at the wall*, and the authors' own remedy is to delete those points. Consequence for us: (i) any
future validation of our wall gradient against a finite-volume discrete adjoint twin must carry a
declared boundary-consistency caveat, or the comparison is worthless where it matters most; (ii) this
is a positive, citable argument for our architecture — the fitted-march + exact-transposed-sweep route
computes the wall sensitivity from the closed-form corner residual and an exactly transposed march,
so the failure mode reported here does not exist in our pipeline. Also supported by the Conclusions
(p. 16): "the assessment of numerical solutions with respect to exact continuous equations is also
linked to the difficult question of adjoint consistency, about which little has been proved today."

**A-2 — ADOPT (verification harness).** The a-posteriori **characteristic-curve extraction by
integration of the tangent field `(1, t)`** — `(1, v/u)` for `S`, `(1, t±)` with `t±` from Eq. (40)
for the Mach lines — from a single shared seed point (§4.3, p. 13), plus the *per-series normalised
error* definition (max `|Ξ|` divided by max over the four subparts, p. 15). This gives a
**solver-agnostic** verification harness: it can be run on our JAX fitted march, on GENO's Fortran
MoC output, and on any future FV twin, with a *derived* rather than magic tolerance. *Innesto*: the
cross-code oracle family (`[X-GENOXC]`), as an additional independent invariant that does not rely on
node-to-node correspondence between the two codes — which is exactly the weakness of a node-matching
cross-code comparison. Attach the paper's own caveat: accuracy degrades for characteristics traced
close to `M = 1⁺` because of the `c²√(M²−1)` term in Eq. (40) (p. 16) — i.e. this harness must not be
seeded near the sonic line, a constraint we should pre-register rather than rediscover.

**A-3 — THREAT, downgraded to non-threat after inspection (recorded because the brief flags this paper
as "il vicino più prossimo alla nostra Lemma-B/O3.1").** The two constructions do **not** overlap and
neither subsumes the other. *Theirs*: the state is solved on a finite-volume mesh; the adjoint is a
discrete adjoint of that FV scheme; the MoC/characteristics are used *afterwards*, as an analytical
yardstick, to verify the adjoint. *Ours*: the state solver **is** the fitted characteristic march, the
adjoint **is** the exactly transposed march obtained by reverse-mode AD through implicit `custom_vjp`
unit processes (Lemma B(ii)), and O3.1 measures the exactness of that transposition. The quantities
measured are different in kind: their `1.8e-6 … 9.5e-9` are *continuous-consistency* residuals of a
discrete adjoint; our `2.7e-10` vs derived `5.1e-8` is a *discrete transposition identity*. Therefore
the paper neither anticipates nor devalues claim 13; what it does is supply the complementary
certificate we lack (F-1) and confirm, at the continuous level, the propagation structure our discrete
Lemma-B exploits — stated in their Introduction, p. 1: for the adjoint problem "(a) information
travels along characteristics in the opposite direction to the flow, and (b) the right eigenvectors of
the local Jacobian replace the left eigenvectors in the equation definition". Our
`x`-block-triangular march reversed by AD is the discrete image of exactly that.

**A-4 — IRRELEVANT-to-us note on their driver, recorded for the SOTA ledger.** Steepest descent, six
bump DOFs, 5%-of-throat displacement cap, two steps, no convergence claim (Appendix C). This is a
functionality demonstration, not an optimization study, and it is far below our driver (TR-SQP,
Sobolev/Steklov–Poincaré Riesz representation, active-set multipliers as marginal values, RK-G
segmentation, deflated continuation, sector tournament). No algorithmic transfer in that direction.

---

## 6. Bibliography inspection (data of record)

**45 references** (refs 1–27 on p. 20, refs 28–45 on p. 21). Our INDEX.md figure of "47 refs" comes
from the arXiv preprint and should be corrected to **45** for the version of record.

**Classical variational nozzle-design line — COMPLETELY ABSENT.**
No **Rao**, no **Guderley**, no **Hantsch**, no **Shmyglevskii**, no **Hoffman (J.D.)**, no
**Kraiko**, no **Sirazetdinov**, no **Scofield**, no **Nikol'skii**, no **Miele**. Zero items from
the maximum-thrust nozzle corpus, in a paper whose only application is a nozzle and whose appendix
optimizes nozzle thrust. This is the affirmative evidence the sweep was looking for.

**Classical gasdynamics / MoC line — PRESENT (so "zero classical citations" needs qualifying).**
[1] **Ferri**, *Application of the Method of Characteristics to Supersonic Rotational Flow*, NASA TR
841, 1946; [2] **Shapiro** 1954; [3] Bonnet & Luneau 1989; [4] Délery 2008; [27] **Hirsch** 2007;
[31] **Meyer & Goldstein**, "The method of characteristics for problems of compressible flow
involving two independent variables: Part I", *Q. J. Mech. Appl. Math.* **1948**, 1, 196–219;
[32] Anderson, *Modern Compressible Flow*, 3rd ed.; [34] **Liepmann & Roshko** 1956; [35] Grossman
2000. So the classics they cite are the *analysis* classics, never the *design/variational* classics.

**Modern adjoint line — PRESENT AND STRONG.**
[5] **Jameson**, "Aerodynamic design via control theory", *J. Sci. Comput.* 1988;
[19] **Lions**, *Contrôle Optimal de Systèmes Gouvernés par des Équations aux Dérivées Partielles*,
1968; [13] **Giles**, Duta, Müller, Pierce (AIAA 2001-2596), [14] Giles et al. *AIAA J.* 2003,
[29] **Giles & Pierce**, "Analytic adjoint solutions for the quasi-one-dimensional Euler equations",
*JFM* 2001, 426, 327–345, [41] Giles & Pierce, AIAA 97-1850;
[42][43][44] **Lozano** (mesh sensitivities and boundary formulas, *JCP* 2017; "Singular and
discontinuous solutions of the adjoint Euler equations", *AIAA J.* 2018, 56, 4437–4451; "Watch your
adjoints! Lack of mesh convergence in inviscid adjoint solutions", *AIAA J.* 2019, 57, 3991–4006);
[28] Anderson & Venkatakrishnan 1999; [6][7] Brezillon et al.; [8] Peter & Dwight 2010;
[9] Schmidt, Ilic, Schulz, Gauger 2013; [10] Venditti & Darmofal 2002; [30] **Peter & Désidéri**,
"Ordinary differential equations for the adjoint Euler equations", *Phys. Fluids* 2022, 34, 086113
(the direct predecessor of this paper); [40] Peter, Renac, Labbé, *JCP* 2022, 449, 110811;
[33] Oberkampf & Trucano 2002 (V&V).
**Pironneau is ABSENT** — notable, given he is the other canonical name of the adjoint-shape line.

**Reading of record.** The reference list is a clean cross-section of the modern adjoint school with
a gasdynamics-analysis tail, and it is *hermetically sealed* from the variational nozzle-design
school. Two schools, one physical object, zero citations between them — in 2023, at ONERA, under a
Lozano editorship. This is the strongest single-artifact support the litmap has for P2/G14 and for
the empty-niche claim, and it also independently corroborates our existing Giles-Ulbrich/Lozano-based
pin ("differentiate the fitted front, never a captured smear"), since [43]/[44] are exactly the
singular-and-discontinuous-adjoint and lack-of-mesh-convergence papers that pin rests on.

---

## 7. What the paper proves vs. what it asserts (rigor separation)

| Statement | Status in the paper |
|---|---|
| Direct and adjoint systems share `|K|` and hence the same `S`, `C±` | **Proved** (§2.3, p. 4) |
| Exactly one independent CE along `C⁺` and along `C⁻` (both problems) | **Proved** by rank argument (§2.4, p. 5) |
| All minors vanish along `S`; reduced `K̃` needed | **Proved** (§2.5, p. 6) |
| DCE in conservative variables, Eq. (42) | **Derived**; equivalence with (14) **proved** in Appendix B |
| `dS = 0`, `dH = 0` contained in the derived CEs | **Proved** (Eqs. 37–38, p. 10) |
| Rank two of the `S` differential forms | **Machine-verified** (Maple, Supplementary Materials) — not a hand proof |
| `dλ₁/ds − H dλ₄/ds = 0` | **Derived** from the streamtrace ACEs (Eq. 45 ⇒ 44) |
| `λ₁ = Hλ₄` for the nozzle thrust (`λ* = 0`) | **Asserted** with a physical argument + graphical evidence (Fig. 6); not proved |
| Discrete adjoint satisfies the ACEs | **Measured** (`1.8e-6 … 9.5e-9`), on one case, one mesh — no mesh-refinement study of the residual is reported |
| Dual consistency of JST discrete adjoint | **Imported** from [40], and explicitly *not* holding near boundaries |
| Appendix C optimization | **Demonstration** (two steps, +3.1% / +0.7%); no convergence, no optimality certificate |

---

## 8. Actions proposed (for the parent to triage)

1. **CORRECTION to INDEX.md**: "47 refs" → **45 refs**, and qualify "zero classical citations" as
   "zero *variational nozzle-design* classics (Rao/Guderley/Hantsch/Shmyglevskii/Hoffman/Kraiko);
   the MoC-analysis classics Ferri 1946, Meyer–Goldstein 1948, Shapiro 1954, Liepmann–Roshko 1956
   *are* cited". Cite the *Aerospace* 2023, 10, 797 version, not the arXiv preprint.
2. **Register in the litmap as affirmative evidence for P2/G14 and for claim 8** (empty niche), with
   the "two sealed schools" reading and the Lozano-editorship detail.
3. **New certificate to book (F-1)**: adjoint characteristic-equation residual as a per-phase oracle
   in VI.6, complementary to O3.1, with the declared precondition that the ACE coefficients be
   re-derived for variable-`γ` Jacobians under DIR-THERMOTAB.
4. **New cheap oracle to book (F-2)**: `λ₁ = Hλ₄` / `dλ₁/ds = H dλ₄/ds`, with the declared
   precondition of an explicit map from the fitted-march adjoint to conservative-residual multipliers.
5. **Record the boundary dual-consistency threat (A-1)** in the cross-code / validation section: any
   FV-discrete-adjoint comparison of our wall Hadamard density inherits a documented, unfixed
   inconsistency exactly at the wall.
6. **Record the count fact (F-3)** in M0 Route B: 1 independent CE per Mach-line family, 2 along the
   streamline (double root), for the adjoint system as for the direct one.
