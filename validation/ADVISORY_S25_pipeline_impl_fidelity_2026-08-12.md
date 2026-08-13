# ADVISORY — S25 PIPELINE IMPLEMENTATION FIDELITY (math-to-code)

Date: 2026-08-12. **Single-expert review, one pass.** Reviewer axis:
MATH-TO-CODE FIDELITY — does the implementation realize the declared
mathematics, and is each implemented algorithm correct SOTA practice
(not merely fast). READ-ONLY: no Python/jax executed; every identity
below was verified BY HAND from the source (current working tree,
post-refuter-repair state of 2026-08-12). This is NOT a diff review
(per-lever refuters of record:
`validation/sota_gapmap_raws_2026-08-12/s25_refute_m12.md`,
`s25_refute_m4.md` — read, cited, not duplicated) and NOT a SOTA-gap
census (`ADVISORY_S24_sota_gapmap_2026-08-12.md` — GAP-N cited where an
observation lands on an already-mapped gap).

Verdict grammar: **faithful** / **faithful-with-caveat** / **MISMATCH**
(with the exact line and the corrected math). Mismatches would be
ranked first; **none was found**.

---

## 0. SUMMARY

| Piece | Verdict |
|---|---|
| thermotab_c1_jax.py — quintic Hermite basis + derivatives | **faithful** (all 36 defining conditions verified) |
| thermotab_c1_jax.py — derived_newton_trips | **faithful** (T''(h) and the contraction constant re-derived, both correct; +1 trip honest) |
| thermotab_c1_jax.py — grid_uniformity_reject | **faithful** |
| thermotab_c1_jax.py — NASA-direct oracle (C-A) | **faithful-with-caveat** (edge-node estimator-order overclaim; sized immaterial at this table) |
| a1_ideal_march_jax.py — custom_vjp implicit rule | **faithful** (sign/transpose exact; one declared-scope note on `ta`) |
| a1_ideal_march_jax.py — damped Newton + cert metric + fused solve_cert | **faithful** (solve_cert expression verbatim; consumer indexing verified) |
| a1_toc_variational_jax.py — spline_coeffs / spline_eval / wall_geometry | **faithful** (tridiagonal rows re-derived exactly) |
| a1_toc_variational_jax.py — thrust_J | **faithful-with-caveat** (quadrature correct; integration domain starts at the first arc station, one O(da^2) panel short of the documented (0, theta_B]) |
| a1_toc_variational_jax.py — M4 plan_operands/engine | **faithful** (one body, two binding modes: equivalence by construction; refuter repair M4-F1 landed at source) |
| a1_toc_variational_jax.py — M1/M2 memo counters | **faithful** (repairs F1+F2 complete and correct — reconciliation identity re-derived for all three episode types; four low-severity refuter caveats knowingly not landed, listed) |
| a1_toc_variational_jax.py — T2 repricing line | **faithful** (matches the pre-adjudicated §7.1 repair; F8 identification caveat concurred, not duplicated) |
| margin_governor.py — KS aggregate + G1 surrogate | **faithful** (bounds, sign conventions, safe-where, fallbacks all correct) |
| margin_governor.py / def_twin_falsifier.py — make_alpha_lam / val field | **faithful** (EXACT match to the M0-registered (G) formula, S21/S24 blocks) |
| def_twin_falsifier.py — masked KS + DE bucket + C5 identity | **faithful** (bucket = M0 S24 definition; C5 identity is a correct consequence of the KS bounds) |

Counts: **0 MISMATCH · 2 faithful-with-caveat · 11 faithful**, plus a
repair-completeness ledger (§8) and 7 minor notes (§9).

---

## 1. thermotab_c1_jax.py — quintic Hermite basis (lines 134-158)

Convention (line 136): H = f0·B0 + f1·B1 + D·d0·B2 + D·d1·B3 +
D²·s0·B4 + D²·s1·B5 with t = (T − T_i)/D. For H to interpolate value,
first and second T-derivative data at both ends, the basis must satisfy
(value, value', value'' at t=0 and t=1):

| basis | (0) | (1) | '(0) | '(1) | ''(0) | ''(1) | closed form |
|---|---|---|---|---|---|---|---|
| B0 = 1−10t³+15t⁴−6t⁵ | 1 | 0 | 0 | 0 | 0 | 0 | (1−t)³(1+3t+6t²) |
| B1 = 10t³−15t⁴+6t⁵ | 0 | 1 | 0 | 0 | 0 | 0 | 1−B0 |
| B2 = t−6t³+8t⁴−3t⁵ | 0 | 0 | 1 | 0 | 0 | 0 | t(1−t)³(1+3t) |
| B3 = −4t³+7t⁴−3t⁵ | 0 | 0 | 0 | 1 | 0 | 0 | −t³(1−t)(4−3t) |
| B4 = ½t²−1.5t³+1.5t⁴−½t⁵ | 0 | 0 | 0 | 0 | 1 | 0 | t²(1−t)³/2 |
| B5 = ½t³−t⁴+½t⁵ | 0 | 0 | 0 | 0 | 0 | 1 | t³(1−t)²/2 |

All 36 conditions verified by hand (e.g. B3' = −12t²+28t³−15t⁴ →
B3'(1) = −12+28−15 = 1; B4'' = 1−9t+18t²−10t³ → B4''(0) = 1, B4''(1) =
1−9+18−10 = 0). **This is the correct two-point C² quintic Hermite
basis.** `_quintic_dcoeffs` (148-158) are the exact term-by-term
derivative polynomials of B0-B5 (checked each). The chain-rule assembly
in `eval_f` / `eval_fp` (189-201) is correct: dH/dT = (f·dB)/D + d·dB +
D·s·dB, and at t=0 it returns exactly d_i and s_i. `eval_f_fp` (203-220)
is verbatim the same two expressions with a shared locate/gather —
fused semantics identical by inspection. Verdict: **faithful**.

## 2. thermotab_c1_jax.py — derived_newton_trips (lines 248-275)

* **Seed error.** Seed = linear interp of the (h_i, T_i) node data.
  Linear-interpolation remainder: |ΔT| ≤ (Δh)²/8 · max|T''(h)|.
  T'(h) = 1/cp; T''(h) = d(1/cp)/dh = (−cp'/cp²)·(dT/dh) = **−cp'/cp³ —
  the claimed formula is correct.** With Δh_i ≈ cp_i·dT the per-interval
  bound is (cp_i dT)²/8 · |cp'_i|/cp_i³ = dT²|cp'_i|/(8cp_i); the code
  maximizes the per-node product (261-262) — a grid sampling of the sup,
  consistent with the repo's declared data-derived-bound model, and
  guarded (below).
* **Contraction constant.** For the root problem f(T) = h(T) − h_t:
  the classical Newton quadratic bound is e⁺ ≤ M e² with
  M = sup|f''|/(2 inf|f'|) = **max|cp'|/(2 min cp) — the code's M
  (line 263) is the correct Newton constant.** Units check: e0 [K],
  M [1/K], M e² [K] — consistent. The refusal guard `M·max(e0,floor) ≥ 1`
  (265) is exactly the contraction-certification condition.
* **Trip count.** The loop iterates the model e ← M e² until e ≤ floor
  (roundoff target C_OPS·eps·max|T|, the C6 scale), then **+1 margin
  trip (274) — an honest guard** for the grid-sampled sups; and the
  derived K is independently rejector-covered twice: the carrier bound
  `1 ≤ K_NEWT ≤ N_NEWT_INV+2` (504-506) and the C6 roundtrip
  certification (469-477), so an undercounted K cannot pass silently.
  Edge case noted: if the model needed >64 trips the loop caps and K
  would land at 65 → both rejectors fire; unreachable at real tables
  (M·e0 ~ 1e-9 ⇒ K = 2). Verdict: **faithful**. (The C_OPS = 100
  convention itself is the GAP-29 constants cluster — mapped, not
  re-raised.)

## 3. thermotab_c1_jax.py — grid_uniformity_reject (228-245)

Band = C_OPS·eps·max|T| ≈ 8.7e-11 K on this table; requires every node
on the uniform law within band AND band < 0.5·D (D ≈ 0.348 K, ~9 orders
of slack). The license is a necessary condition; the operative verifier
is the off-node floor-vs-searchsorted identity (511-522) plus the R5/R6
negative controls, which can fire. The R6 corruption sizing (664-675) is
the exact per-probe detectability formula: scaling D by (1+ε) flips
probe k iff ε > fr_k/(i_k+fr_k) — re-derived, correct — with the firing
corruption = 2× the most sensitive probe's floor. Verdict: **faithful**.

## 4. thermotab_c1_jax.py — NASA-direct oracle C-A (524-574)

Verified exact:
* **h exactly quintic**: from `A1.nasa_funcs` (a1_ideal_march:278-303),
  h/Runi = a1·T + a2T²/2 + a3T³/3 + a4T⁴/4 + a5T⁵/5 + **a6 (constant)**
  — degree-5 polynomial, the a6 claim is exactly right.
* **Joint-free window**: T_TAB_LO = 1050 > T_break = 1000 (asserted
  common in `blend_nasa`), so the whole table and all probes are on the
  upper branch; `a1_up = a_bl[0,0]` IS the upper-branch a1 (c_up[0]).
* **4th-order cp' exact on quartics**: the central 5-point formula
  (d_dT_table:123) has error ∝ f⁽⁵⁾ = 0 on the quartic cp — exact at
  INTERIOR nodes.
* **s0 remainder**: s0m = Rg(a1 ln T + quartic); d⁶(ln T)/dT⁶ = −120/T⁶
  ⇒ **s0⁽⁶⁾ = −120·Rg·a1/T⁶** (code 550, with Rg = Runi·1000/mixM
  matching build_tab_nasa:311,317) — correct, correctly maximized at
  Tg[0].
* **Remainder constant 46080**: two-point Hermite with 6 conditions has
  remainder f⁽⁶⁾(ξ)/6! · (x−x0)³(x−x1)³; max|(x−x0)³(x−x1)³| = (D/2)⁶ =
  D⁶/64 ⇒ constant = 6!·64 = **46080 — correct, and the derivative
  count (6th) is correct.**

**CAVEAT (the one real finding of this file).** The claim block (68-75,
527-532) states "the 4th-order cp' estimator is exact [on quartics] ⇒
h/cp match at the roundoff floor". `d_dT_table` uses the 4th-order
stencil ONLY at interior nodes 2..n−3; nodes 0, 1, n−2, n−1 use
2nd-order formulas (124-127) whose error ∝ dT²·cp''' ≠ 0 on a quartic —
and the oracle probe window [Tg0+0.37dT, TgN−0.37dT] INCLUDES the four
edge intervals, whose Hermite data carry those inexact cp' values. So
the exactness claim is overbroad at the edges: the true edge-interval h
deviation is O(B4max·dT²·δcp'·D²) = O(0.017·dT⁴·cp'''/3). SIZED IN
REVIEW (not executed): at dT = 2850/8191 ≈ 0.348 K and NASA-7
upper-branch magnitudes this sits 3-5 orders BELOW tol_h_o =
C_OPS·eps·max|h| (similarly for cp against its 60·hscale/dT-scaled band
and for s0's Rg-scaled band); it would become band-breaking only at
dT ≳ 5-10 K (N_TAB ≲ ~500). Direction of failure is conservative (a
spurious oracle FAIL, never a false PASS). **Repair (doc-level, 1
line): scope the claim to "interior stencil exact; edge-node 2nd-order
error O(dT⁴) sized below the band at N_TAB = 8192", or extend
d_dT_table with 4th-order one-sided edge stencils (5-point, exact on
quartics) — the cleaner fix.** Verdict: **faithful-with-caveat**.

Minor notes (no verdict impact): the C2 tolerance's 60-factor is
justified because dB1 is evaluated in monomial form (intermediate
magnitude ~60 before cancellation to |dB1| ≤ 1.875 = 30/16) — the
comment's "worst INTERMEDIATE magnitude" reasoning is right. The C4
gconst tol_p labels a linear-interp-scale envelope "the s0 remainder";
as an envelope it strictly dominates the true quintic remainder here
(ratio 0.021·(D/T)⁴ ≪ 1) — conservative, wording loose. Band
composition style at these sites is the GAP-10 subject.

## 5. a1_ideal_march_jax.py — implicit-solve machinery (417-518)

* **custom_vjp implicit rule (bwd_solve, 475-481).** For r(z,p) = 0:
  dz/dp = −(∂r/∂z)⁻¹(∂r/∂p), so the VJP is
  p̄ = −(∂r/∂p)ᵀ(∂r/∂z)⁻ᵀ z̄. Code: `Jz = jacfwd(resid, argnums=0)`
  (= ∂r/∂z, rows = residual components); `w = solve(Jz.T, zbar)`
  (= (∂r/∂z)⁻ᵀ z̄); `pbar = vjp_p(−w)` (= −(∂r/∂p)ᵀ w by linearity of
  the VJP). **Sign and transpose exactly correct.** `bwd` returns zero
  cotangent for z0 — correct by the implicit-function idealization (the
  converged solution is seed-independent; the per-cell certification is
  precisely the rejector licensing this). NOTE (declared-scope): the
  `ta` cotangent is `None` (515) — gradients w.r.t. the thermo tables
  are structurally zero through `solve`. Correct for the pipeline's
  W/P-differentiation scope; if a table-sensitivity study ever
  differentiates through `ta` it would get silent zeros — one docstring
  line would fence this permanently.
* **Damped candidate set (424, 444-469).** Trials (1, 1/2, 1/4, 1/16,
  1/64, 0): the t = 0 member guarantees the residual-norm argmin is
  monotone non-increasing (the current iterate is always a candidate) —
  the stated property holds by construction. Nonfinite dz ⇒ dz zeroed,
  metric forced to +inf ⇒ the loop runs to the cap and the cell FAILS
  certification honestly (the C2-F1 comment matches the actual control
  flow: with dz = 0 all candidates equal z, so the iterate freezes).
  NaN residual norms map to +inf (429) so argmin never selects a NaN
  point. Bare-argmin acceptance (no sufficient-decrease/measured
  contraction) is GAP-29 — mapped, not re-raised.
* **Certification metric (485-488).** step_norm = |J⁻¹r|_∞ at the
  solution = the length of one undamped Newton step — the standard
  a-posteriori Newton-floor certificate; the while-loop termination
  metric (469: max|dz| of the step just taken) is the SAME quantity one
  iterate earlier, so termination and certification are mutually
  consistent, and certify() re-checks post-hoc in all record paths.
* **Fused solve_cert (490-502).** Body = `newton` + verbatim the
  step_norm expression at its solution; jit-of-jit inlines the inner
  primal; the custom_vjp `solve` remains the only differentiable entry
  (solve_cert is host-consumed). **Identical semantics: yes.** Consumer
  wiring verified: `a1_march_scan.cached_solvers` stores the raw
  4-tuples (`mk = A1.make_implicit_solver`, a1_march_scan:159-162), and
  run_toc_record's fused path indexes `solvers[kind][3]` (a1_toc:261)
  = solve_cert, legacy path `[:3]` (267) — correct; `A1.get_solver`'s
  docstring still says "(solve, newton, step_norm)" (a1_ideal:710) —
  stale 3-tuple doc, trivial.

Verdict: **faithful**.

## 6. a1_toc_variational_jax.py — spline, geometry, objective

* **spline_coeffs (133-152).** M-form cubic spline. Interior rows:
  (h_{i−1}/6)M_{i−1} + ((h_{i−1}+h_i)/3)M_i + (h_i/6)M_{i+1} =
  Δy_i/h_i − Δy_{i−1}/h_{i−1} — the standard C² continuity equations,
  matched exactly (144-149). Clamped-left row: from S'(x0) =
  (y1−y0)/h0 − h0M0/3 − h0M1/6, the condition S'(x0) = slope0 gives
  **(h0/3)M0 + (h0/6)M1 = (y1−y0)/h0 − slope0** — exactly rows 142-143.
  Natural-right row: M_{n−1} = 0 (150-151). **The tridiagonal system
  implements exactly the declared clamped-left/natural-right spline.**
  (Dense solve of a 9×9 tridiagonal under AD: acceptable SOTA at this
  size; a Thomas solve would buy nothing under jit.)
* **spline_eval (155-167).** Value and slope re-derived from the M-form;
  the slope formula (y_{i+1}−y_i)/h + ((3b²−1)M_{i+1} − (3a²−1)M_i)h/6
  is the exact derivative (checked term by term, da/dx = −1/h,
  db/dx = 1/h). searchsorted-right minus 1 with clip: correct interval
  selection incl. both endpoints.
* **wall_geometry (170-184).** Arc point (rtd·sinθ, yt+rtd(1−cosθ)) and
  tangent tanθ re-derived from the circle center (0, yt+rtd) — correct;
  clamping the spline's left slope to tan(thB) makes the attachment C¹
  by construction; last knot at xi = 1 ⇒ x = L exactly ("L fixed by
  construction" holds).
* **thrust_J (953-960).** For an axisymmetric wall the axial-projected
  area element is dA_x = 2π y dy, so pressure thrust = 2π ∫ p y dy;
  the code's 2π·Σ ½(py_{i+1}+py_i)(y_{i+1}−y_i) is the exact
  trapezoidal quadrature of that integral on the (possibly nonuniform,
  signed) y-partition of the wall stations — **the correct axisymmetric
  pressure-thrust quadrature** for the declared vacuum objective, and
  it is a signed sum, so any locally non-monotone candidate wall is
  still integrated correctly.
  **CAVEAT (integration domain).** The wall-point list starts at the
  FIRST arc station θ1 = θB/n_B (a1_toc:367-371) — there is no θ = 0
  (throat) point — so the implemented J integrates over [θ1, θB] +
  contour, not the documented "(0, θ_B]" (docstring 23-27). The missing
  panel is ≈ 2π·p_throat·yt·rtd·(1−cosθ1) with θ1 ≤ da: O(da²) ≈
  1e-4·p_t·(scale) at da = 0.5°, and it varies smoothly with θB inside
  a frozen plan. Consequences: (i) the optimization is fully
  internally consistent (AD gives the EXACT gradient of the implemented
  J — clean discretize-then-optimize practice); (ii) the "Pa drops out"
  statement is exact for the documented full-wall domain (with {eps, L}
  fixed, Pa·π(y_lip²−yt²) is constant) but for the implemented domain
  the ambient term would carry an O(Pa·yt·rtd·θ1·dθ1/dθB) design
  dependence — moot in code (no Pa term exists anywhere; the objective
  is vacuum-equivalent) but the M0/doc statement should be scoped to
  the quadrature actually implemented, or the θ = 0 throat point added
  to the station list (1-line change, shifts J by a constant-ish
  O(da²) amount and re-baselines recorded J values — hence doc-scoping
  is the cheaper repair). Verdict: **faithful-with-caveat**.

## 7. a1_toc_variational_jax.py — M4 engine + M1/M2 memos + T2

* **M4 operand-vs-constant equivalence (589-947).** ONE traced body
  `run(W, ops)` serves both modes: legacy jits `lambda W: run(W, ops_j)`
  (ops closed over → jaxpr constants), M4 jits `run` and passes the
  same `ops_j` as arguments. Identical Python expression tree ⇒ the
  mathematics is identical **by construction**; any residual
  numerical difference is XLA optimization-level and is exactly what
  the m4gate Newton-floor row measures (measured bitwise per its
  print). The kkf mapping (plan_operands 629-632) re-derived: for arc
  columns kk = k+1 ∈ 1..n_B, kkf = kk/n_B; for contour kk = k+1−n_B ∈
  1..Nw, kkf = kk/Nw — matches the record's θ = θB·k/n_B and
  x = xB+(L−xB)·k/Nw station laws exactly (the fl(a·fl(k/n)) vs
  fl(fl(a·k)/n) association drift is refuter M4-F2, band-gated there;
  not duplicated). Refuter repair **M4-F1 landed at source**: ekey now
  carries `M_NODES` and `KNOT_XI` bytes (929-933) with the repair
  comment naming the finding; the per-make dummy-cell certification
  (727-745) still runs on every make (cache hit or not), preserving
  the eager rejector.
* **M1/M2 counters (1101-1567) — repairs verified complete.**
  - **F1 (s25_refute_m12, the REFUTED-THE-EDIT finding): repaired and
    correct.** `fresh` now counts the REQUEST pre-call at BOTH sites
    (loop top 1198, callback 1456). Reconciliation re-derived for all
    three episode types: cert-type failure (callback fresh 1 + loop-top
    failmemo 1 = OFF 2), march-type failure (same — the pre-call
    increment survives the internal raise), cached boundary (callback
    fresh 1 + loop-top cached 1 = OFF 2). The gate check
    (engine_speed_bench: `sum(ON fresh+cached+failmemo) == OFF fresh`)
    is exactly the identity that now holds — the false-FAIL channel is
    closed.
  - **F2: repaired.** `_mkey` (1105-1114) re-reads M_NODES / KNOT_XI /
    A1.N_NEWTON AT REQUEST TIME into the key (ctx hash stays
    walk-constant but now covers only genuinely stable content, and
    `record_ctx_tag` (976-998) additionally hashes the class knobs +
    N_NEWTON). Mid-walk class mutation can no longer alias a stale
    record.
  - `n_eval` = n_vg_exec increments only on actual compiled
    value_and_grad executions (1350); hits counted separately (1345);
    slots one-shot (cleared on consume 1159/1164; vg_slot fresh per
    segment 1339). Counters are truthful under the new semantics.
  - **Knowingly NOT landed** (low-severity refuter caveats, listed so
    the record is explicit): m12-F3 (failure-path message/artifact
    divergence still lacks its one scoping line; the " [replayed
    callback record failure, M1 memo]" suffix remains), m12-F6 (the
    M2 `_vg`/`_mvg` memos still carry no in-driver first-hit control —
    the m12gate A/B is the de facto superseding control, but that
    supersession is not registered), m12-F11 (the two first-hit
    controls are still `assert` — strip under `python -O`; the
    counters would then over-claim), m12-F8 (t_grad ≈ value_and_grad
    wall remains an asserted identification, no band). None blocks
    adoption; all four are one-to-three-line repairs.
* **T2 repricing (1964-1998).** `lhs_T2 = opt["n_eval"] * t_grad` with
  n_eval = honest compiled executions — implements exactly the
  pre-adjudicated §7.1 convention ("one value_and_grad per eval", not
  N×(t_solve+t_grad)); the legacy double-priced figure and dedup hits
  are printed alongside for ledger continuity. Faithful to the
  adjudication; the residual F8 identification (t_grad times
  jit(grad), a different compiled object from the walk's
  jit(value_and_grad)) is concurred as stated by the refuter — a
  2-line val_grad timing would close it. Per refuter F7, the normative
  T2 text in the kickoff/claims docs still awaits its R4 delta.

Verdict: **faithful** on all three sub-pieces (caveats above are
process/doc-level, none is a math error).

## 8. margin_governor.py — KS aggregate, G1 surrogate, (G) field

* **KS-min form (make_margin_fn 175-201).** KS_ρ(v) = v_min −
  ln(Σ exp(−ρ(v_i−v_min)))/ρ. Verified: the argmin lane contributes
  exp(0) = 1 ⇒ 1 ≤ Σ ≤ N ⇒ **v_min − ln(N)/ρ ≤ KS ≤ v_min** and KS is
  the conservative (lower) envelope of min — enforcing KS ≥ μ0 does
  guarantee min val ≥ μ0 over the finite lanes. Sign conventions all
  correct (masked lanes → +inf in the min, → 0 in the sum). The
  double-where (183-197) is the correct JAX safe-where pattern (masked
  lanes evaluate at the safe reference forward, contribute exactly 0,
  and poison no cotangent); Σe ≥ 1 whenever n_fin > 0 makes the 1e-300
  clamp inert on live paths. frac_bad penalty −K_RICH·m_ref·frac_bad
  only strengthens the constraint (m ≥ 0 ⇒ KS ≥ μ0 + penalty ≥ μ0), so
  the conservativeness theorem survives the surrogate. No-survivor
  fallback = −K_RICH·m_ref (finite negative, continuous at
  frac_bad = 0: exact KS recovered bit-for-bit — verified: the penalty
  term is exactly 0 there). m_np's nonfinite fallback −2·K_RICH·m_ref
  and gm_np's zeroed+counted gradient match the declared G1
  survive-and-report contract. ρ = K_RICH·ln(N)/μ0_min pins the gap by
  construction; the one-hot-gradient instance sensitivity of large ρ
  is **GAP-27** (mapped; the derivation here is as declared). Minor:
  the gap-tightness statement is anchored to the BASELINE lane count N
  — a later plan with more real lanes has gap ln(n_fin)/ρ marginally
  above μ0_min/K_RICH (log-scale; the conservative side is
  ρ-independent, so no guarantee is lost).
* **make_alpha_lam (155-163) vs the M0-registered formula.** M0 S21
  block (and re-affirmed in the S24 block):
  (G) val = [Λ·B·(A+B) − (A−B)] / [1 + Λ·(A+B)], A = tan(θ−α),
  B = tan(α), Λ = V·dα/dV on the isentrope, val > 0 = valid side.
  Code: α(q) = arcsin(min(1, c/q)) with c from the closure on the
  isentrope (= arcsin(1/M)); Λ = q·dα/dq by AD; val computed with
  exactly A = tan(th−al), B = tan(al), the numerator
  lam·B·(A+B) − (A−B) and the denominator 1 + lam·(A+B)
  (margin_governor:186-189, identically def_twin:541-544/635-637 and
  baseline_val_stats:278-281). **EXACT match, sign for sign.** den is
  reported and never guarded/read as val = 0 — the BOUND (b)
  declaration honored. Notes: the min(1, c/q) clamp (subsonic guard)
  gives α = π/2, Λ = 0 there — unreachable on real lanes (the
  axial-margin rejector enforces u_x > c upstream) and masked lanes
  evaluate at q_ref; `make_alpha_lam` calls state_fn(q, None), a
  c1-closure-only contract (a table-bound state_fn would crash loudly,
  never silently — acceptable, worth half a comment line).

Verdict: **faithful**.

## 9. def_twin_falsifier.py — masked KS, DE bucket, controls

* **val_of_pts / make_margin_fn_cs**: the (G) formula is verbatim the
  M0 form (see §8). The masked KS replica preserves the MG structure
  exactly, with the DECLARED variant frac_bad = (n_sel − n_fin)/n_sel
  over the masked lane count (docstring 608-611) — consistent.
* **DE bucket (cs_stats 562-603)**: registered chain nodes; the last
  node with val ≤ 0 is found and everything up to and INCLUDING it is
  excluded (de[idx[:j_last+1]] = False) ⇒ the bucket = the maximal
  strictly-lipward all-positive suffix — exactly the M0 S24 block's
  "registered terminal-C+ chain nodes strictly LIPWARD of the LAST
  val = 0 crossing", degenerating to the whole registered surface when
  no crossing exists (matching the mild-instance reconciliation
  clause).
* **C5 mapping-identity rejector (837-845)**: m_ref − (m_traced + μ0)
  ∈ [0, ln(N)/ρ] is precisely the KS two-sided bound restated
  (m_traced + μ0 = KS_masked ≤ v_min = m_ref and ≥ v_min − gap), with
  honest ±1e-12/1e-10 floats; it is a genuine rejector — a (k,i)→lane
  mapping error, or an argmin landing on an unmapped node, drives the
  gap negative or past ln(N)/ρ and fires.
* **R-GRAD floor-sized control (852-864)**: gm_bad = gm + 2·tol_g·dv ⇒
  |gm_bad·dv − d2| ≥ 2tol_g − |gm·dv − d2| > tol_g whenever the primary
  check passes strictly — fires by construction at exactly the declared
  detection floor (the S24 R-GRAD lesson, honored).
* **_mvg one-slot memo (662-698)**: verbatim the MG pattern (refuter
  m12-F9/F11 territory — HOLDS there, nothing new found).

Verdict: **faithful**.

---

## 10. RANKED FINDINGS (no MISMATCH; caveats and notes)

1. **[CAV-1, thermotab C-A]** Edge-node cp' estimator order overclaim
   (§4): "exact on quartics" holds only for the interior stencil; the
   four edge intervals carry O(dT⁴·cp''') data error inside the probed
   window. Sized 3-5 orders below every C-A band at N_TAB = 8192;
   failure direction conservative. Repair: 1 doc line, or 4th-order
   one-sided edge stencils.
2. **[CAV-2, thrust_J]** Quadrature domain starts at θ1 = θB/n_B, one
   O(da²) panel short of the documented (0, θB]; the Pa-free statement
   is exact for the documented domain, approximate at O(da²) for the
   implemented one (moot in code — vacuum objective). Repair: scope the
   doc, or add the θ = 0 throat station (re-baselines J).
3. **[NOTE-1, custom_vjp]** `ta` cotangent = None: table-parameter
   gradients are structurally zero through `solve` — correct today,
   silent-zero trap if the differentiation scope ever widens to thermo
   sensitivities. One fencing line.
4. **[NOTE-2, repairs not landed]** m12-F3 scoping line, m12-F6 M2
   in-driver control (or registered supersession by the A/B gate),
   m12-F11 strip-proof asserts, m12-F8 t_grad band — all still open at
   source (§7), each ≤ 3 lines.
5. **[NOTE-3, KS ρ]** Gap-tightness statement anchored to baseline N;
   conservativeness unaffected (§8). Instance sensitivity of large ρ =
   GAP-27 (already mapped).
6. **[NOTE-4, C4 gconst]** tol_p wording "s0 remainder" actually
   implements the linear-scale envelope (dominates the true quintic
   remainder by (T/D)⁴/0.021 — conservative). Wording only. Band
   composition policy at these sites = GAP-10.
7. **[NOTE-5, stale doc]** A1.get_solver docstring says 3-tuple; the
   factory returns 4 (solve, newton, step_norm, solve_cert).

Cross-map: constants conventions (NEWTON_TOL_FACTOR/C_OPS/N_NEWTON,
bare-argmin damping) = GAP-29; two-resolution band topology
conditioning at the bands this review touched = GAP-7; table-box
literals behind the thermotab hypothesis = GAP-11. None re-raised here.

## 11. WHAT WAS POSITIVELY RE-DERIVED (the checklist of record)

Quintic basis: 36/36 defining conditions. dB0-dB5: exact. T''(h) =
−cp'/cp³: derived. M = max|cp'|/2min cp: the classical constant.
46080 = 6!·64 with the (D/2)⁶ extremum: derived. s0⁽⁶⁾ = −120Rg a1/T⁶:
derived, right branch, right units chain (Runi·1000/mixM). Γ(T) =
(γ+1)/2 + (γ−1)Tγ'/2γ from Γ = 1 + (ρ/c)(∂c/∂ρ)_s with (dT/dρ)_s =
(γ−1)T/ρ: derived exactly (variable-γ form). Implicit-rule
sign/transpose: derived. Spline clamped/interior/natural rows: derived.
Spline slope formula: derived. Trapezoidal 2π∫p y dy = axial pressure
force: derived. kkf station laws: matched to record. Counter
reconciliation identity: re-derived for cert-type, march-type, cached
episodes against the gate check. KS bounds + conservative side + C5
identity: derived. (G) val formula: matched symbol-for-symbol to the
M0 S21/S24 registration blocks. R6/R-GRAD control sizings: formulas
re-derived.

*Label: single-expert review, one pass. Source-only; sized numbers in
§4/§6 are order-of-magnitude hand estimates from the table parameters
(N_TAB = 8192, [1050, 3900] K), not executed measurements.*
