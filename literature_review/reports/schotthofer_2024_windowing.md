# Expert read — Schotthöfer et al. 2024, "Windowing Regularization Techniques for Unsteady Aerodynamic Shape Optimization"

Reader: convergence-review expert reader. Date of read: 2026-08-13.
Metro di confronto: `reports/00_APPARATUS_BRIEF.md` (record state of the cycle-averaged variational nozzle program).

---

## 1. Citation (verified from the PDF itself)

Steffen Schotthöfer, Beckett Y. Zhou, Tim Albring, Nicolas R. Gauger,
**"Windowing Regularization Techniques for Unsteady Aerodynamic Shape Optimization"**,
Chair for Scientific Computing, TU Kaiserslautern, Bldg 34, Paul-Ehrlich-Strasse, 67663 Kaiserslautern.
arXiv:2412.00604v1 [math.NA], 30 Nov 2024. 23 pages, 16 figures, 1 table, 22 references.
(Author footnotes on p. 1: Schotthöfer = Student Researcher; Zhou = Research Scientist, Member AIAA; Albring = Ph.D Candidate; Gauger = Professor, Associate Fellow AIAA. No journal/venue imprint, no DOI printed on the PDF — arXiv preprint only. AIAA-style typesetting suggests a conference-paper origin, but **no AIAA paper number is printed**, so none is cited here.)

## 2. Read coverage

**23 / 23 pages read in full, bibliography included** (pages 1–20 in one Read call, pages 21–23 in a second).
Nothing was skipped. The only content not machine-readable in detail is the *numerical value* of individual plotted points inside Figs. 1–16 (raster plots); all numbers quoted below are taken from the running text, from Table 1 (p. 12), or from figure captions and slope annotations printed on the figures (Fig. 16: −0.962, −0.988). Table 1 was read in full.

## 3. What the paper actually does

**Problem.** Gradient-based aerodynamic shape optimization when the objective is a **time average of an unsteady output over a limit cycle oscillation (LCO)** whose **period length `T(σ)` itself depends on the design parameter `σ`**. Two test problems: (i) NACA0012 at 17° AoA, M = 0.3, Re = 10³ and 10⁶, massively separated / vortex-shedding flow (self-excited LCO, period ≈ 31 Δt, Fig. 1 caption); (ii) NACA64A010 forced-pitching airfoil (period set by the imposed 53.3491 rad/s pitching frequency, i.e. **design-independent** period, Sec. V, p. 20).

**Formulation.** Continuous objective Eq. (3): `J(σ) = (1/T(σ)) ∫_{t_tr}^{t_tr+T(σ)} g(t,σ) dt`. The core obstruction is Eq. (5):
`d/dσ [ (1/T(σ)) ∫_0^{T(σ)} g dt ] ≠ (1/T) ∫_0^{T(σ)} d/dσ g dt`
— "we cannot simply interchange differentiation and integration in Eq. (5) due to dependence of T on σ" (p. 3). Fixed-horizon average `J_M` (Eq. 4) is replaced by the **windowed time average** Eq. (7): `J_w(σ,M) = (1/M) ∫_0^M w(t/M) g(t,σ) dt`, with window admissibility Eq. (8): `w ∈ C^l`, `w(s)=0 for s ∉ (0,1)`, `∫_0^1 w ds = 1`. Because `w` does not depend on `σ`, the windowed sensitivity Eq. (9) *does* commute: `d/dσ J_w = (1/M)∫_0^M w(t/M) d/dσ g dt`.

**Central theoretical result (RECALLED, NOT PROVED HERE).** Theorem 1 (p. 3) is explicitly attributed to Krakos, Wang, Hall & Darmofal, *J. Comput. Phys.* 231(8):3228–3245 (2012) [ref. 13]: "We recall Krakos' Theorem 1 for the sake of completeness." With `k = ⌈M/T⌉` periods spanned:
- Eq. (11): `|J_w(σ,M) − J(σ)| ≤ ‖h‖_∞ O(k^{−p})`
- Eq. (12): `|d/dσ J_w − d/dσ J| ≤ ‖∂_σ h‖_∞ O(k^{−p}) + ‖(1/T) dT/dσ‖_1 ‖∂_s h‖_∞ O(k^{−(p−1)})`
- Eq. (13): `p = 1` for `l = −1`; `p = l+1` for `l ≥ 0` even; `p = l+2` for `l > 0` odd; exponential rate for `w ∈ C^∞`.

**Windows used**, Eqs. (35)–(39), p. 9, with their orders `(p, p_s)` where `p_s` is the order for the *sensitivity*:
- Square `w_sq = 1_{(0,1)}` — `C^0`(as printed) ⇒ `p = 1`, `p_s = 0` (**no convergence of the sensitivity**);
- Hann `w_h = 1 − cos(2πs)` — `C^1` ⇒ `p = 3`, `p_s = 2`;
- Hann-Square `w_hsq = (2/3)(1 − cos(2πs))²` — `C^3` ⇒ `p = 5`, `p_s = 4`;
- Bump `w_bmp = (1/A) exp(−1/(s − s²))`, `A = ∫_0^1 exp(−1/(s−s²)) ds` — `C^∞` ⇒ exponential.

**Unknowns / design variables.** NACA0012: FFD-box control points, 242 design variables (`X_ad = [−0.05, 0.05]^242`, Eq. 40); a *single* FFD variable is used for the window-comparison study (p. 6). NACA64A010: 50 Hicks–Henne design variables.

**Constraints.** (i) The URANS solver itself as a PDE constraint in fixed-point form, Eq. (22b) `U^n(σ) = G^n(U^n, U^{n−1}, U^{n−2}, σ)`, arising from a second-order BDF discretization Eq. (14) converged by dual-time stepping Eqs. (16)–(20); (ii) a **windowed** inequality constraint on lift, Eq. (40): `C_w(σ, N − n_tr) = (1/(N−n_tr)) Σ w((n−n_tr)/(N−n_tr)) C_L(n,σ) ≥ 0.96` (0.76 in the Re = 10³ case); (iii) box bounds on the design.

**Flow model.** Compressible **URANS** with the Spalart–Allmaras one-equation turbulence model, finite volume on a vertex-based median-dual grid, JST convective scheme (Roe for the pitching case), scalar upwind for the SA transport equation. NACA0012 mesh: 27125 elements, 217 wall boundary elements, 217 farfield; Δt = 0.0005 s. NACA64A010 mesh: 12897 quadrilaterals + 23205 triangles, 250 wall elements, Δt = 0.001636 s (72 steps per pitching period). **Viscous, turbulent, dissipative, subsonic** (M = 0.3, 0.35). No shocks, no nozzle, no reacting flow.

**Solver / adjoint.** SU2 v7.0.1 "Blackbird", **discrete adjoint by algorithmic differentiation** (CoDiPack, ref. 20), so the turbulence model is differentiated too — "the frozen turbulence assumption, which is typically used in many URANS-based adjoint formulations, is eliminated" (p. 2). Lagrangian Eq. (25), KKT system Eqs. (26)–(28), adjoint recurrence Eq. (29) marching backwards in time with the **window entering only as a scalar seeding weight** `1_{n≥n_tr} (1/(N−n_tr)) w((n−n_tr)/(N−n_tr)) ∂_{U^n} J(U^n)`; explicitly remarked (p. 6): "since the window function `w` is only dependent on the current time step `n`, the adjustment to traditional adjoint state equations is marginal." Adjoint fixed-point iterator Eq. (30) with contraction norm Eq. (31) `‖∂_{Ū^n} N_U^n‖ = ‖(∂_{U^n} G^n)^T‖` — "convergence of the adjoint iterator therefore depends only on the convergence of the primal iterator" (p. 6). Design equation Eq. (32). Outer optimizer: **SLSQP** (Kraft 1988, ref. 21), gradients relaxed by a factor 0.1.

**Verification.** Three layers, all *numerical*:
1. **Tangent-vs-adjoint consistency**, Table 1 (p. 12): `dC_D/dσ` for one FFD variable, forward AD vs adjoint AD, 8 rows. Max relative difference **1.8878 %** (Hann, Re = 10⁶); minimum **0.0318 %** (Hann-Square, Re = 10⁶); Square Re = 10⁶ 0.0731 %; the Re = 10³ rows cluster at 0.38–1.34 %.
2. **Theorem-1 rate validation**: Fig. 16 measures the Square-window decay slopes **−0.962** (time average) and **−0.988** (sensitivity) against `k`, i.e. the predicted `O(k^{−1})`; text (p. 10) states the Re = 10³ results "completely validate Theorem 1", and that the Re = 10⁶ case is **outside** it — "Theorem 1 does not give clear convergence properties in this case … since the exponential growth of the amplitude of the sensitivity implies exponential growth of `‖d/dσ C_D‖_∞`".
3. **Window-shift robustness of surface sensitivities** (Sec. IV.C, p. 13): shifting the end of the averaging window by **9 iterations ≈ 29 % of a period** changes the Square-windowed 217-point surface-sensitivity vector by **9.1 %** in Euclidean norm with **sign changes at 5 surface points**, versus **0.84 %** for the Bump window; Bump-vs-Square disagreement at fixed end time is **9.2 %**, with pointwise deviations of **5–20 %** in the 20 %-chord region.
4. **Optimization outcome** (Sec. IV.D, Figs. 11–13): with the Square window the SLSQP run oscillates, repeatedly oversteps the lift constraint to `C_w ≈ 0.94`, and never settles; with Hann / Hann-Square / Bump the run drives windowed drag to **≈ 30 % of the baseline** and stays feasible after ≤ 4 iterations. Fig. 11 records the qualitative outcome that the Hann-Square-optimized design has a *steady* (non-shedding) flow field while the Square-optimized one is still unsteady.

## 4. Hypotheses

### Declared
- H-D1. The unsteady system reaches a **limit cycle oscillation** after a transient of duration `t_tr` / `n_tr`; the LCO exists and is unique for each design (p. 4: "We further assume that the system exhibits a limit cycle oscillation after n_tr").
- H-D2. The period `T(σ)` depends on the design parameter (self-excited case), and is *not known a priori* — this is the motivation for long-time windowing (p. 4).
- H-D3. Window admissibility Eq. (8): compact support in `(0,1)`, unit mass, differentiability class `l`.
- H-D4. `h(s,σ) = g(t,σ)` under `s = t/T` (Eq. 10) has period one, and the norms `‖h‖_∞`, `‖∂_σ h‖_∞`, `‖∂_s h‖_∞`, `‖(1/T) dT/dσ‖_1` in Eqs. (11)–(12) are **finite** — this is where Theorem 1 silently fails at Re = 10⁶ and the authors say so (p. 10).
- H-D5. Differentiability of the Lagrangian `L` w.r.t. `σ, U^n, Ū^n` for all `n` (stated explicitly before Eq. (26), p. 5).
- H-D6. The dual-time primal iterator `G^n` is a contraction near convergence, `‖(∂_{U^n}G^n)^T‖ < 1` "in a suitable norm, if the direct (pseudo time) iteration is near convergence" (p. 6).
- H-D7. `n_tr` is chosen large enough; the authors flag that the transient duration may itself depend on `σ` (p. 4: "it should be stressed, that the duration of the transient phase may be dependent on the design parameter σ and the value of n_tr should be chosen big enough") — declared but **not enforced by any test**.

### Necessary but NOT declared
- H-U1. **The limit-cycle attractor is unique and the design homotopy does not cross a bifurcation.** Fig. 11c shows the optimized design has a *steady* flow — i.e. the optimizer walked the design across the Hopf boundary out of the LCO regime. The whole `T(σ)`, `k = ⌈M/T⌉` bookkeeping is undefined there. The paper never addresses what `J` means when the LCO ceases to exist mid-optimization.
- H-U2. **The design map σ ↦ (LCO) is smooth enough for `dT/dσ` to exist.** Eq. (12) uses `‖(1/T) dT/dσ‖_1` without ever establishing differentiability of the period, and `T` is never measured as a function of `σ` anywhere in the paper.
- H-U3. **Ergodicity / stationarity of the long-time average**: Fig. 5 shows the period mean "shifts upwards … stops at approximately n = 4500", and p. 10 concedes "in this example there exists an additional trend, i.e. the function is not exactly periodic." So the object being averaged is *not* the periodic `h` that Theorem 1 assumes; the theorem is applied outside its own hypothesis and this is admitted only in passing.
- H-U4. **The AD-differentiated SA turbulence model is a meaningful derivative of the physics**, not merely of the discretization. The paper argues AD is "accurate to machine precision by construction" (p. 2) — that is a statement about the *discrete* map, not about the modelled physics.
- H-U5. **The window does not change the optimum.** Since all admissible windows share the same `M→∞` limit `J(σ)`, the authors treat window choice as a pure regularizer. At finite `M` the optimizer is minimizing *different functionals* for different windows; that the resulting designs (Figs. 12b–d) are comparable is an empirical observation, not a proof.
- H-U6. Single-objective smoothness for SLSQP; no non-smoothness handling despite the LCO phase-shift mechanism cited from Wilkins et al. [22].
- H-U7. Mesh/time-step convergence of *sensitivities* is assumed — only one mesh and one Δt per test case; no grid or Δt refinement study appears anywhere.

## 5. Three-level comparison with the program apparatus

### 5.1 TEORICO

**F-T1 — [CONTAINED, ALTA] The paper's averaging layer is a restriction of our `J = ∫_Ξ F dμ`, under exactly two hypotheses.**
Their Eq. (3)/(7) is our objective with `Ξ = [0,1)` (one cycle), `dμ = w(s) ds`, `F[Σ; s(ξ)] = g(t,σ)`. The identification holds exactly under: (i) their `w` satisfies our μ-hypotheses (probability measure — their Eq. (8) `∫_0^1 w = 1` is literally our normalization), and (ii) their period is treated as fixed data. What is **not** contained is the constraint: their flow model is dissipative turbulent URANS with an SA closure, outside our S1 piecewise-smooth MOC-regular class, and Route A explicitly "dies for dissipative/reacting flow". So the containment is *measure-layer only*, and must be stated that way in the litmap. Evidence: Eqs. (3), (7), (8), p. 3; flow model description p. 6.

**F-T2 — [THREAT, ALTA] They exhibit, in closed form, the exact term that would break our "differentiation under the cycle integral is THEOREM\*" the moment μ becomes design-dependent.**
Eq. (5), p. 3: the Leibniz interchange is FALSE when the period depends on the design; the residual is quantified in Eq. (12) as `‖(1/T) dT/dσ‖_1 ‖∂_s h‖_∞ O(k^{−(p−1)})`. Our T7 upgrade of record ("differentiation under the cycle integral is THEOREM\*, dominated by audited margins") is silent on the *period* — it dominates the integrand, not the domain. **The theorem survives only because our μ is exogenous**: the interface contract (Γ_d, D, μ) is upstream data, the L4 default makes every patch axially supersonic with margin, and mean upstream influence is EXCLUDED BY THEOREM [T-NSW], so `dT/dΣ ≡ 0` structurally. This is a real threat in the sense that the theorem's proof, as recorded, does not *name* the exogeneity of μ as a hypothesis. Recommended repair: add to T7 the explicit hypothesis **"μ is exogenous to Σ (dμ/dΣ = 0), guaranteed by L4 + [T-NSW]"**, and register Eq. (5)/Eq. (12) as the named falsifier of that hypothesis. This becomes load-bearing at F5 (RDE coupled) and anywhere `μ(Ξ_sub) > 0`, where upstream influence returns.

**F-T3 — [GAP-CONFIRMS, ALTA] The paper's own failure mode confirms the class of the declared non-containment "endogenous measure weight".**
Containment claim 18 already declares Kraiko–Osipov's endogenous trajectory-adjoint weight as a structural non-containment of (P). Schotthöfer et al. are the modern, non-nozzle instance of exactly that class: an average whose *weight/domain* is a function of the design. Their whole paper is a workaround (freeze the weight `w` in a σ-independent normalized coordinate) rather than a derivation of the endogenous-measure stationarity system — they never write the `dT/dσ` term into the optimality system, they *bound* it away. Evidence: Eq. (9) is legitimate precisely because "the windowing function `w` is independent of `σ`" (p. 3). This confirms the gap is real and unfilled in the modern adjoint school too.

**F-T4 — [GAP-CONFIRMS, ALTA] Their measure is a numerical regularizer over the time axis of ONE trajectory, not a shared shape across a measure-weighted FAMILY of inflow states — D2 gap G3 / claim 7 stands, sharpened.**
There is one flow state family here (the LCO of a single configuration), one wall, no free endpoint, no corner condition, no counterpart of our T4 free-boundary nesting result. The only "shared-across-the-measure" object they produce is the design equation Eq. (32), which is a *gradient* condition, never analyzed as a stationarity system with transversality. Evidence: Eqs. (26)–(28) list exactly three conditions (state, adjoint, design) — no endpoint/transversality condition exists anywhere in the paper. Claim 7 is **not** falsified by this paper; if anything the qualification added 2026-08-13 ("spatially nonuniform traveling/rotating-wave inflow") is not even needed to exclude it.

### 5.2 FORMALE

**F-F1 — [ADOPT, ALTA] Krakos Theorem 1 (Eqs. 11–13) is the missing *derived tolerance* for our cycle-quadrature bar, and it prices the window/period-uncertainty error separately from the quadrature error.**
Our cycle layer (VI.4) currently carries a *practice*: split Gauss panels at switch phases, use "trapezoid-on-the-circle only opportunistically when the T0 flatness + harmonic-decay certificates pass". The unstated justification for trapezoid-on-the-circle is spectral accuracy for smooth exactly-periodic integrands over an **exactly known integer number of periods**. Theorem 1 is precisely the statement of what happens when that last clause fails: the square window (= plain trapezoid over an arbitrary horizon) degrades to `p = 1` for the value and `p_s = 0` — **no convergence at all** for the sensitivity, "at most `‖(1/T)dT/dσ‖ O(1)` … very slow convergence or none at all" (p. 4). Innesto: add to the VI.6 certificate stack a **cycle-quadrature bar with two branches** — (a) period-certified branch (T0 flatness + harmonic-decay pass, integer-period trapezoid, spectral), (b) period-uncertain branch, where the bar is Eq. (11)/(12) with the window's `p, p_s` from Eq. (13). Register the reference verbatim as Krakos, Wang, Hall & Darmofal, *JCP* 231(8):3228–3245 (2012), since Schotthöfer et al. **recall** the theorem rather than prove it (p. 3, "We recall Krakos' Theorem 1 for the sake of completeness") — the theorem must be cited to Krakos, never to this paper.

**F-F2 — [CONTAINED, ALTA] Their discrete design equation Eq. (32) is the discrete-time image of our T7(b) shared-wall condition, with the window playing the role of μ.**
Eq. (32): `∂_σ L = Σ_n [ 1_{n≥n_tr} (1/(N−n_tr)) w((n−n_tr)/(N−n_tr)) ∂_σ J(U^n) + (Ū^n)^T ∂_σ G^n ]`. Setting this to zero is exactly "the μ-weighted sum of per-phase design sensitivities vanishes", i.e. our T7(b) `∫_Ξ G_ξ(x) dμ + λ_L g_L(x) = 0` with the length multiplier absent (they have no geometric constraint of that type). Our reading of record — **"no phase satisfies its own wall condition; the μ-average does"** — is *structurally identical* to their statement, and their numerics are an independent demonstration that the weighted-average condition is the operative one. Under hypotheses: single wall, no free endpoint, weight independent of design, discrete time in place of `Ξ`. **Naming caution to record:** their `w` (window over normalized time) and our `w(ξ)` in the weighted transversality (\*\*') (geometric-kinematic weight `R(ξ)·w(ξ)`) are **different objects sharing a symbol**. The (\*\*') weight is a property of the corner geometry, not a user-chosen regularizer; do not let the two collide in the paper text.

**F-F3 — [ADOPT, MEDIA] The `‖∂_s h‖_∞` factor in Eq. (12) tells us WHY our T0-flatness certificate is worth more than we currently claim for it.**
Eq. (12)'s second term — the only one carrying the `dT/dσ` pathology — is multiplied by `‖∂_s h‖_∞`, the sup of the *within-cycle derivative* of the output. Our T-T0 (wave-frame exactness, THEOREM) says that for a single rotating mode the instantaneous thrust through every axisymmetric surface is **constant, not merely mean-equal**; i.e. `∂_s h ≡ 0`. Therefore **on certified single-mode data the entire period-dependence term of Krakos' bound vanishes identically, regardless of `dT/dσ`**. This upgrades the T0 flatness monitor from a data-quality audit to a *formal enabler* of the Leibniz interchange in T7. Innesto: state it as a corollary in M0 next to T-T0 and reference it from the T7 differentiation-under-the-integral THEOREM\*. Confidence MEDIA only because the identification `h ↔ our F` requires the flatness certificate to hold on the *objective integrand*, not merely on the thrust trace through the interface surface — that step must be written out.

**F-F4 — [GAP-CONFIRMS, ALTA] Bibliography: zero contact with the classical nozzle line; partial contact with the modern adjoint line. This is a record datum for claims 1 and 8.**
Exhaustive inspection of the 22 references (pp. 22–23):
- **Classical variational nozzle line — Rao, Guderley, Hantsch, Hoffman, Kraiko, Shmyglevskii, Sirazetdinov, Nikol'skii: ZERO citations. None. Not one.**
- **Modern adjoint line:** Jameson 1988 "Aerodynamic design via control theory", *J. Sci. Comput.* 3:233–260 [6] — **YES**. Pironneau 1974, *JFM* 64(1):97–110 [7] — **YES**. **Lions — NO. Giles — NO. Lozano — NO.**
- Unsteady-adjoint line present: Nadarajah & Jameson, *AIAA J.* 45(7):1478–1491 (2007) [1]; Nielsen, Diskin & Yamaleev, *AIAA J.* 48(6):1195–1206 (2010) [2]; Thomas, Hall & Dowell, *AIAA J.* 43(9):1931–1936 (2005) [5]; Zhou et al. 2015 [3]; Albring et al. 2016 [4], 2019 [8].
- Chaotic-sensitivity line: Wang/Hu/Blonigan LSS *JCP* 267:210–224 (2014) [11]; Ni & Wang NILSS *JCP* 347:56–77 (2017) [12]; Ni et al. FD-NILSS *JCP* 394:615–631 (2019) [10]; Krakos et al. *JCP* 231(8):3228–3245 (2012) [13]; Wilkins, Tidor, White & Barton, *SIAM J. Sci. Comput.* 31(4):2706–2732 (2009) [22].
- Tooling: SU2 [14][15], CoDiPack [20], SLSQP/Kraft [21], JST [16], Roe [17], AUSM [18], Spalart–Allmaras [19], Shur et al. DES [9].
This is a 2024 paper at the centre of the discrete-adjoint unsteady-shape-optimization school, citing Jameson and Pironneau by name, that has **no awareness whatsoever of the variational nozzle corpus**. It is direct supporting evidence (not proof) for claim 1 (P2/G14) and claim 8 (empty niche): the two literatures do not touch, in the direction "modern adjoint school → classical nozzle school", as of Nov 2024.

### 5.3 ALGORITMICO

**F-A1 — [ADOPT, ALTA] Oracle O5 must be re-specified with a high-order window; as currently written it is exposed to a measured ~9 % sensitivity error and sign flips.**
O5 of record is "unsteady sim vs `J_avg + St·J1`". If the unsteady-simulation side of that comparison uses a plain time average over an arbitrarily chosen horizon — which is the natural reading of the current spec — then the paper's Sec. IV.C measurement applies directly: moving the window end by **9 iterations, i.e. 29 % of one period**, changed the Square-windowed surface-sensitivity vector by **9.1 % in Euclidean norm with sign changes at 5 of 217 surface points**, whereas the Bump window moved **0.84 %** (p. 13). Concrete innesto, three lines in VI.6: (i) the O5 unsteady-side average is computed with the **Bump window Eq. (38)**, `w_bmp(s) = (1/A) exp(−1/(s − s²))`, `A = ∫_0^1 exp(−1/(s−s²)) ds`, or Hann-Square Eq. (37) `(2/3)(1 − cos 2πs)²` if `C^∞` support is inconvenient; (ii) O5 declares its window and its `k` (number of periods spanned) in the Verdict; (iii) a **rejector**: recompute O5 with the window shifted by a quarter period — if the O5 residual moves by more than its own bar, the O5 firing is void. This is the direct, positive answer to the question that put this paper on the list.

**F-A2 — [ADOPT, MEDIA] The same window discipline belongs in the stage-A data-generation audit of the CycleFamily, not only in O5.**
Our data contract VI.1 requires a "T0 flatness / harmonic-decay certificate" and states that generated data passes the same audits as imported data. But the *extraction* of `(P0, T0)(ξ)` and the μ weights from an unsteady RDE simulation is itself a windowed-averaging problem with an imperfectly known period; the paper documents (Fig. 5 and p. 10) that even a well-behaved LCO carries a slow mean drift — "the shift in the mean value stops at n = 4500", "the function is not exactly periodic". Innesto: stage-A audit gains an item — **declared window + declared `k` + a period-shift rejector** on any cycle-family generated from an unsteady simulation. Confidence MEDIA: our standing scope pin is that interface data is a *pure periodic rotating wave* with T0 flatness as the monitor, so on certified data this audit is expected to pass trivially; it earns its place as the falsifier that the pin actually holds on real generated data.

**F-A3 — [THREAT, MEDIA] At high Reynolds number the paper measures DIVERGENCE of the windowed sensitivity for EVERY window — a warning that O5's gradient limb may be unfirable on realistic RDE data.**
Fig. 9b and p. 10: "We can observe a divergent behavior for all windows as time increases … Theorem 1 does not give clear convergence properties in this case … since the exponential growth of the amplitude of the sensitivity implies exponential growth of `‖d/dσ C_D‖_∞`". Fig. 2c–d show the instantaneous `dC_D/dσ` amplitude growing exponentially at Re = 10⁶ (to `O(10²–10³)`) versus linearly at Re = 10³. The lesson transfers: on a real RDE field with mode competition / chaotic content, **no choice of window rescues the averaged sensitivity**; only the *value* comparison survives. Our D2.3 scope note already routes mode transitions out of the averaged theory and to the robust layer, which protects the value limb — but O5 is a gradient-adjacent oracle and our idle CVaR/DRO layer is the declared home for this regime. Recommended: annotate O5 with a **precondition** ("certified single-mode, flatness-passing data only") and name Least-Squares-Shadowing / NILSS (refs. [10]–[12]) as the registered alternative route should the precondition ever fail, so the route is *registered as beaten-or-declared* per the choice-adjudication directive rather than discovered late.

**F-A4 — [CONTAINED, ALTA] Their adjoint architecture is a strictly weaker instance of ours; nothing in the algorithmic core is new to us.**
(i) Discrete adjoint by reverse-mode AD of the assembled solver (CoDiPack) — our JAX march with per-cell `custom_vjp` implicit unit processes is the same principle with an implicit-function rule instead of unrolling, and our Lemma-B / O3.1 transposition identity (measured 2.7e-10 vs derived tolerance 5.1e-8 over the entire march) is a **strictly stronger certificate** than their tangent-vs-adjoint agreement, which is only **1.8878 % at worst and 0.0318 % at best** (Table 1, p. 12). Their check is a consistency comparison at percent level; ours is a machine-precision bilinear identity with a seeded negative control. (ii) Their Eq. (31) result — adjoint iterator contraction inherits from the primal — is the fixed-point-solver analogue of our Lemma-B block-triangular statement. (iii) Their outer driver is SLSQP with a hand-tuned 0.1 gradient relaxation factor (p. 13); ours is TR-SQP with Riesz representation in a Sobolev/Steklov–Poincaré metric and derived trust-region segmentation — again strictly stronger. **Nothing to adopt at this level.** The one honest asymmetry: they differentiate through a turbulence model without the frozen-turbulence assumption, a capability our inviscid formulation does not need.

**F-A5 — [CORRECTION, MEDIA] The litmap's one-line framing of this paper needs tightening.**
`INDEX.md` line 62 lists it as "windowing regularization for unsteady shape optimization" and the review brief frames its relevance as "the QUALITY of our cycle average … a window/convergence problem of the mean to be priced". That framing is imprecise in a way that matters: **windowing is not a quadrature-accuracy device for a known-period, exactly-periodic signal** — there, trapezoid over an integer number of periods is already spectrally accurate and a smooth window would *lose* accuracy by tapering. Windowing buys exactly two things, both visible in Eqs. (12)–(13): robustness to an **unknown or design-dependent period**, and robustness to a **non-integer number of periods in the horizon**. Correct litmap line: *"prices the cycle-average error when the period is unknown or design-dependent (Krakos bound); irrelevant on certified exactly-periodic known-period data, decisive on simulation-extracted data."* Filed as a CORRECTION because leaving the loose framing in place invites the wrong adoption — replacing our *physical* measure μ (log-uniform in pressure by T-O2, Lemma 2) with a smooth window would silently change the objective, not improve its estimate. The window belongs on the **estimator** side (O5, data generation), never on the definition of `J`.

## 6. Bibliography note (record datum)

Full inspection of all 22 references, pp. 22–23:

| Line | Present? | Detail |
|---|---|---|
| Rao | **NO** | — |
| Guderley | **NO** | — |
| Hantsch | **NO** | — |
| Hoffman (nozzle) | **NO** | — |
| Kraiko | **NO** | — |
| Shmyglevskii | **NO** | — |
| Lions | **NO** | — |
| Pironneau | **YES** | [7] *JFM* 64(1):97–110 (1974) |
| Jameson | **YES** | [6] *J. Sci. Comput.* 3:233–260 (1988); also [16] JST scheme 1981; also [1] with Nadarajah |
| Giles | **NO** | — |
| Lozano | **NO** | — |

Zero of six classical nozzle names; two of five modern adjoint names (Jameson, Pironneau). Supporting evidence for claims 1 and 8; not decisive on either, since absence of citation in one paper is not a survey.

## 7. What the paper PROVES vs what it ASSERTS

- **Proves (in the paper):** nothing new analytically. Every derivation in Sec. III is a construction (Lagrangian → KKT → adjoint recurrence → design equation) from standard discrete-adjoint machinery.
- **Recalls from Krakos et al. [13]:** Theorem 1, Eqs. (11)–(13). The paper is explicit: "We recall Krakos' Theorem 1 for the sake of completeness" (p. 3). No proof is reproduced.
- **Asserts + demonstrates numerically:** (a) the embedding of windowing into SU2's AD-based discrete adjoint is correct (Table 1, ≤ 1.89 % tangent-vs-adjoint); (b) higher-order windows converge and the square window does not (Figs. 6–9, slopes −0.962 / −0.988 in Fig. 16 matching `O(k^{−1})`); (c) higher-order windows make the *optimization* qualitatively better-behaved (Figs. 11–13); (d) at Re = 10⁶ all windows diverge and Theorem 1 does not apply (p. 10) — an honest negative result.
- **Novelty vs. the state of the art it builds on:** the theory is Krakos 2012; the contribution is (i) embedding long-time windowing in a *discrete AD adjoint* URANS solver with the window as a mere seeding weight (Eq. 29 remark), (ii) the observation that at higher Reynolds number the instantaneous sensitivity amplitude grows *exponentially*, defeating all windows, and (iii) the end-to-end shape-optimization demonstration with a windowed *constraint* as well as a windowed objective (Eq. 40).

## 8. Bottom line for the program

The question that put this paper on the list — *"is there a window/convergence problem in our cycle mean that we must price?"* — answers cleanly in two parts:

1. **On the objective `J = ∫_Ξ F dμ` itself: NO, and now for a named reason.** Our μ is exogenous (interface contract, L4 supersonic patches, mean upstream influence excluded by [T-NSW]), so `dT/dΣ = 0` and the pathological term of Eq. (12) is structurally absent; and on T-T0-certified single-mode data `∂_s h ≡ 0` kills it a second time. **Both of these are hypotheses our T7 differentiation-under-the-integral THEOREM\* currently leaves unnamed** — that is the one real repair this paper forces (F-T2, F-F3).
2. **On the estimators — O5 and any cycle family extracted from an unsteady simulation: YES, and the price is measured.** 9 % vector error and sign flips from a 29 %-of-a-period shift in the averaging horizon (F-A1, F-A2), and a regime (chaotic / high-Re / mode-competing) where no window works at all (F-A3).

No claim of record is falsified by this paper. No novelty claim is threatened. The niche remains empty in the direction this paper looks.
