# DEDICATED REFUTER — S25 pipeline implementation-fidelity review (Form-2, round 1)

Date: 2026-08-12. Refuter axis: default-REFUTE the single-expert one-pass
review `validation/ADVISORY_S25_pipeline_impl_fidelity_2026-08-12.md`
(verdict 0 MISMATCH / 11 faithful / 2 faithful-with-caveat). READ-ONLY,
no execution; every identity below re-derived BY HAND at the current
working tree, independently of the advisory's derivations. DEDUP: the
math-review refuter examines the thrust-sliver object from the math side;
§C below states the object precisely so the judge can merge.

Verdict grammar: **REFUTED** / **SURVIVES** / **SURVIVES-WEAKENED**
(per attacked claim), with evidence lines from the current tree.

---

## A. Adversarial re-verification of the "faithful" verdicts

All 13 pieces were re-examined; 7 were re-derived symbol-for-symbol
(the ones where an error would be most consequential), the rest
source-verified. Depth declared per item.

### A1. custom_vjp implicit rule (a1_ideal_march_jax.py 475-518) — advisory §5
**SURVIVES (full independent derivation).** IFT: r(z(p),p)=0 ⟹ dz/dp =
−(∂r/∂z)⁻¹(∂r/∂p) ⟹ p̄ = −(∂r/∂p)ᵀ(∂r/∂z)⁻ᵀ z̄. Code (476-481):
`Jz = jacfwd(resid_fn, argnums=0)` = ∂r/∂z in JAX's rows-=-outputs
convention; `w = solve(Jz.T, zbar)` = (∂r/∂z)⁻ᵀz̄; `vjp_p(−w)` =
−(∂r/∂p)ᵀw. Sign and transpose EXACT — confirmed. `bwd` (512-515)
returns `(zeros_like(z), pbar, None)`: z0 cotangent zero is the correct
implicit-function idealization (converged solution seed-independent,
licensed by per-cell certification — certify() exists and runs in the
record paths, a1_ideal:750-788, a1_toc cell() 257-312); `ta → None` is
the structural-zero table cotangent, exactly as the advisory's NOTE-1
declares. Damped trials (424) = (1, 1/2, 1/4, 1/16, 1/64, 0): the t=0
member makes argmin-norm monotone non-increasing — holds by
construction; nonfinite dz ⇒ dz zeroed + metric forced +inf (462-469)
⇒ runs to cap and fails cert honestly — control flow verified.
solve_cert (490-502) is verbatim newton + the step_norm expression;
consumer wiring verified at BOTH cited ends: a1_march_scan:159-162
stores the raw 4-tuples, a1_toc:261 indexes `[3]` (fused), 267 `[:3]`
(legacy); `get_solver` docstring at a1_ideal:710 still says 3-tuple
(NOTE-5 real).

### A2. Quintic Hermite basis + derivatives (thermotab_c1_jax.py 134-158) — advisory §1
**SURVIVES (all 36 conditions re-verified by hand, none delegated).**
Convention (136): H = f0B0+f1B1+D(d0B2+d1B3)+D²(s0B4+s1B5), so the
required basis conditions in t-units are B2'(0)=1, B3'(1)=1, B4''(0)=1,
B5''(1)=1, all others (value/'/'' at 0,1) zero except B0(0)=B1(1)=1.
My full check of the code polynomials (139-144):
B0: (1,0;0,0;0,0) with B0''=−60t+180t²−120t³ ⟹ B0''(1)=0 ✓;
B1 = 1−B0 pattern ✓; B2 = t−6t³+8t⁴−3t⁵: B2'(0)=1, B2'(1)=1−18+32−15=0,
B2''(0)=0, B2''(1)=−36+96−60=0 ✓; B3 = −4t³+7t⁴−3t⁵: B3'(1)=−12+28−15=1,
B3''(1)=−24+84−60=0 ✓; B4 = ½t²−1.5t³+1.5t⁴−½t⁵: B4''=1−9t+18t²−10t³ ⟹
B4''(0)=1, B4''(1)=0, B4'(1)=1−4.5+6−2.5=0 ✓; B5 = ½t³−t⁴+½t⁵:
B5''=3t−12t²+10t³ ⟹ B5''(0)=0, B5''(1)=1 ✓. All six closed forms in the
advisory's table expand to the code monomials (I expanded each). The six
dB polynomials (152-157) are the exact term-wise derivatives. Chain rule
in eval_fp (196-201): dH/dT = (f·dB)/D + d·dB + D·s·dB — correct
(1/D per t-derivative, one D absorbed per data factor). eval_f_fp
(203-220) verbatim-fused ✓.

### A3. spline_coeffs / spline_eval (a1_toc 133-167) — advisory §6
**SURVIVES (rows re-derived from the M-form).** From S(x) = a·y_i +
b·y_{i+1} + [(a³−a)M_i+(b³−b)M_{i+1}]h²/6: S'(x_i⁺) = Δy_i/h_i −
h_i(2M_i+M_{i+1})/6 and S'(x_{i+1}⁻) = Δy_i/h_i + h_i(M_i+2M_{i+1})/6.
C¹ continuity at interior node i ⟹ (h_{i−1}/6)M_{i−1} +
((h_{i−1}+h_i)/3)M_i + (h_i/6)M_{i+1} = Δy_i/h_i − Δy_{i−1}/h_{i−1} —
exactly rows 145-149. Clamped-left S'(x0)=slope0 ⟹ (h0/3)M0+(h0/6)M1 =
Δy0/h0 − slope0 — exactly rows 142-143. Natural right M_{n−1}=0
(150-151) ✓. spline_eval slope (164-166) = the exact derivative
(da/dx=−1/h, db/dx=1/h; S'' = aM_i+bM_{i+1} consistent) ✓.
wall_geometry: circle center (0, yt+rtd), tangent tanθ, clamp tan(thB),
last knot ξ=1 ⟹ x=L ✓ (170-184).

### A4. KS aggregate + (G) field + C5 identity (margin_governor 155-201, def_twin 533-651, 837-864) — advisory §8-§9
**SURVIVES (bounds and identities re-derived; M0 match checked
independently).**
* KS (175-201): argmin lane contributes exp(0)=1 ⟹ 1 ≤ Σe ≤ n_fin ⟹
  v_min − ln(n_fin)/ρ ≤ KS ≤ v_min. m ≥ 0 ⟹ ks_part ≥ μ0 + pen ≥ μ0 ⟹
  v_min ≥ μ0 over the finite lanes — conservativeness confirmed, and it
  survives the frac_bad surrogate (pen ≥ 0) and is ρ-independent.
  Masked lanes: +inf in the min (193), 0 in the sum (195-197), inner
  where at vmin_s = the correct JAX double-where (no cotangent
  poisoning). Σe ≥ 1 on live paths ⟹ 1e-300 clamp inert. No-survivor
  fallback −K_RICH·m_ref, plus frac_bad=1 ⟹ total −2K_RICH·m_ref−μ0,
  finite; at frac_bad = 0 the penalty is exactly 0 (integer-exact) —
  bit-for-bit KS recovery confirmed. m_np/gm_np fallbacks (240-251):
  −2K_RICH·m_ref and zeroed+counted ✓. ρ = K_RICH·ln(N)/ladder[-1]
  (derive:304) pins gap ln(N)/ρ = μ0_min/K_RICH ✓; the baseline-N
  anchoring note (NOTE-3) is as stated.
* (G) formula: M0 registration block read directly
  (docs/rde_nozzle_MASTER.md:1683-1688): val = [Λ·B·(A+B) −
  (A−B)]/[1+Λ·(A+B)], A = tan(θ−α), B = tan(α), Λ = V dα/dV, plus
  BOUND (b) "den reported, not guarded". Code sites re-read: MG
  margin_W 187-189, def_twin val_of_pts 541-544 (den returned),
  make_margin_fn_cs 635-637, baseline_val_stats 278-281 (den in the
  dict), def_twin derive artifact den_min_cs 872-873. EXACT match at
  all four; den never guarded — BOUND (b) honored. Λ = q·dα/dq by AD
  (162-163), α = arcsin(min(1, c/q)) ✓.
* DE bucket (cs_stats 584-603): bucket = strictly-lipward suffix after
  the LAST val ≤ 0 node (de[idx[:j_last+1]]=False), degenerating to the
  whole registered surface with no crossing, empty-bucket case → N=0 —
  matches the M0 S24 block (MASTER:1943-1951) including the mild-instance
  reconciliation and the [C9] empty-bucket clause. Node-resolution
  reading of "strictly lipward of the crossing" is the correct
  discretization.
* C5 (837-845): m_traced + μ0 = KS_masked (pen = 0 at a healthy derive
  point); m_ref = concrete chain min. KS two-sided bound ⟹ gap ∈
  [0, ln(n_fin)/ρ] ⊆ [0, ln(N)/ρ] (n_fin ≤ mask.sum() ≤ N); the ±1e-12/
  1e-10 floats are slack, and BOTH firing modes the advisory names
  (mapping error; argmin on an unmapped node ⟹ gap < 0) are real —
  genuine rejector, confirmed.
* R-GRAD (852-864): gm_bad·dv = gm·dv + 2tol_g (dv normalized at 828) ⟹
  |gm_bad·dv − d2| ≥ 2tol_g − |gm·dv − d2| > tol_g when the primary
  passes strictly — the advisory's construction is exact.
* _mvg (MG 224-236, def_twin 671-683): verbatim pattern, no first-hit
  control — consistent with F6 (see §D).

### A5. derived_newton_trips (thermotab 248-275 + invert_h 308-321) — advisory §2
**SURVIVES (seed error, pairing question, and conservativeness resolved
independently; one unflagged half-nit).**
* Seed: invert_h seeds with `jnp.interp(ht, hg, Tg)` (314) — linear
  interp of the (h_i, T_i) node data, as claimed. Remainder needs
  T''(h): T'=1/cp, T'' = d(1/cp)/dT · dT/dh = −cp'/cp³ — formula
  CORRECT. Per-interval bound (Δh_i)²/8·sup|T''| with Δh_i = ∫cp dT ≈
  cp_i·dT.
* **The pointwise-pairing question (the assigned attack): legitimate
  here, with the honest label the code/advisory already carry.** The
  code maxes the NODE-SAMPLED product g(T_i), g(T) = dT²|cp'(T)|/(8cp(T)),
  where the true bound needs max over INTERVALS of (Δh_i² · interval-sup
  of |T''|). Two undershoot channels: (a) Δh_i vs cp_i·dT — relative
  O(cp'·dT/cp) ≈ 1e-4 on this table; (b) node-max of g vs sup g —
  relative O(Lip(g)·dT/g) ≈ 1e-4 (quartic cp, dT = 0.348 K). Both are
  RELATIVE perturbations of e0; the trip count is log-log-insensitive:
  with M·e0 ≈ 1.5e-9 (M ≈ 2e-4 1/K, e0 ≈ 7.6e-6 K, both re-estimated
  from NASA-scale magnitudes), moving K by one boundary requires an e0
  error factor ≈ (M·e0)^{−1/2} ≈ 3·10⁴. A 1e-4 relative sampling
  undershoot is 8 orders short of consuming even the +1 margin trip.
  Conservatism of the iteration itself: x ↦ Mx² is monotone, so the
  bound sequence dominates the true sequence given e0_bound ≥ e0_true;
  M uses GLOBAL table extremes (max|cp'|/2·min cp), which dominates
  every interval-local constant — conservative in that factor
  unconditionally. So: conservative in the repo's declared
  data-derived-bound sense (grid-sampled sups + margin trip), not a
  theorem-grade interval bound — which is exactly how both the
  docstring and the advisory label it. The two independent rejectors
  are real and can fire: carrier bound 1 ≤ K ≤ N_NEWT_INV+2 (504-506;
  the 64-cap ⟹ K=65 ⟹ fires) and the C6 roundtrip (471-477; an
  undercounted K leaves rerr ≈ cp·e_{K−1} > tol_rt ≈ 8.9e-8 J/kg since
  cp·floor ≈ 1.7e-7 > tol_rt — the rejector has resolving power at
  exactly the margin in question). Units chain [K],[1/K] ✓; refusal
  guard M·max(e0,floor) ≥ 1 = the contraction certificate ✓; K=2 at
  this table reproduced by my numbers ✓.
* Unflagged half-nit (no advisory claim contradicted): invert_h line
  315 falls back to the retired literal via `c1.get("K_NEWT",
  N_NEWT_INV)` — a hand-built pack lacking K_NEWT would silently run 8
  trips, slightly against the module docstring's "kept ONLY as the
  R4/M3 negative-control reference and the derived-K sanity ceiling"
  (110-113). Dead code for every build_c1 pack; half-line fence.

### A6. grid_uniformity_reject + R6 sizing (thermotab 228-245, 657-675) — advisory §3
**SURVIVES-WEAKENED — the one genuine refutation of this review.**
The rejector itself: band = C_OPS·eps·max|T| ≈ 8.7e-11 K, band < 0.5·D
with ~9 orders slack, loud refusal — all confirmed; R5 fires on a
0.25·dT displaced node.
**REFUTED as stated: the advisory's endorsement "the R6 corruption
sizing (664-675) is the exact per-probe detectability formula: scaling
D by (1+ε) flips probe k iff ε > fr_k/(i_k+fr_k) — re-derived,
correct".** Exact algebra: probe at x = i+fr (interval units) under
corrupted spacing D(1+ε) maps to floor(x/(1+ε)); the index flips iff
x/(1+ε) < i ⟺ i+fr < i(1+ε) ⟺ **ε > fr_k/i_k** (and the i=0 probe
NEVER flips — x/(1+ε) stays in [0,1) — where the claimed formula gives
a finite threshold 1). Counterexample killing "exact": i=1, fr=0.5;
claimed threshold 0.333, but ε=0.4 gives 1.5/1.4 = 1.071 → floor 1, NO
flip; the true threshold is 0.5. The code formula is the small-ε,
i≫fr first-order approximation (equating the approximate shift
ε·(i+fr) to fr). **Verdict impact: nil at this probe geometry** — the
minimizing probe is k = 8190 (fr = 0.79), where fr/(i+fr) and fr/i
differ by 1 part in 10⁴, both argmins coincide, and epsD = 2·min(sens)
still exceeds the true threshold with margin 2·i/(i+fr) ≈ 1.9998
(≈ the intended 2×); the far probes shift ~1.6 intervals, so n_dis6 > 0
robustly. But the claim of EXACTNESS is wrong twice over — in the code
comment (660-663 "exact per-probe formula") and in the advisory's
endorsement, which specifically says "re-derived" — and this reviewer
demonstrably did not push the algebra to the exact form. Repair: 1-line
comment correction (fr/i exact; fr/(i+fr) = first-order, conservative
argmin unchanged) + amend the advisory sentence.

### A7. Remaining pieces (source-verified, not re-derived in full)
M4 engine (§7): kkf laws (629-632) match record/scan station laws
(367-376, 541-549) EXACTLY — verified; ekey carries M_NODES + KNOT_XI
bytes (929-933) with the M4-F1 repair comment — landed; per-make dummy
cert (727-745) executes BEFORE the engine-cache lookup (934) ⟹ runs on
every make — verified. One-body/two-bindings equivalence (920 legacy
closure vs 947 args) is by construction as claimed. M1/M2 (§7): fresh
pre-call at BOTH sites (1198, 1456); my per-episode re-derivation of
sum(ON fresh+cached+failmemo) == OFF fresh for cert-type, march-type
(the pre-call increment survives the internal raise — the load-bearing
point), and cached episodes: identity holds; the gate check exists
verbatim (engine_speed_bench:336-338). Slots one-shot (1159/1164),
vg_slot per segment (1339), n_vg_exec on execution only (1350), hits
separate (1345) — all verified. T2 (§7): lhs_T2 = n_eval·t_grad (1973),
legacy figure printed (1981) — matches the pre-adjudicated convention;
F8 confirmed at source (see §D). C-A oracle constants (§4): h exactly
quintic with a6 constant (a1_ideal:287-288); T_TAB_LO = 1050 > 1000
asserted common (196, 271-272); a1_up = c_up[0] = a_bl[0,0] (282);
s0⁽⁶⁾ = −120·Rg·a1/T⁶ re-derived (dⁿ(1/T)/dTⁿ = (−1)ⁿn!/T^{n+1});
46080 = 6!·64 with max|(x−x0)³(x−x1)³| = (D/2)⁶ re-derived; Rg chain
311/317 verified. Advisory §4 minor notes re-derived and confirmed:
max|dB1| = 30t²(1−t)² at t=½ = 30/16 = 1.875 with monomial intermediate
60; C4 envelope ratio (120·8/46080)(D/T)⁴ = 0.0208·(D/T)⁴ — the
advisory's 0.021 is exact.

---

## B. The C-A edge-stencil caveat (CAV-1) — attacked and independently sized

**SURVIVES (confirmed real, correctly sized; one phrasing refinement).**
* Premise verified at source: d_dT_table (120-127) is 4th-order central
  at nodes 2..n−3 (error ∝ dT⁴f⁽⁵⁾ = 0 on quartic cp) but 2nd-order at
  nodes 0, 1, n−2, n−1 (errors ∝ dT²cp'''/3, dT²cp'''/6; cp''' =
  Rg(6a4+24a5T), linear and NONZERO on the NASA quartic). The h-quintic
  s-data on intervals 0, 1, n−3, n−2 therefore carry those errors — the
  "exact on quartics ⟹ roundoff floor" claim block (68-75, 527-532) is
  overbroad at the edges exactly as the advisory says.
* Probe-set refinement: T_orc = linspace(Tg0+0.37dT, TgN−0.37dT, 2003)
  has spacing ≈ 4.09·dT, so the probe SET lands in edge intervals 0 and
  n−2 ONLY (probes 1 and 2003); intervals 1 and n−3 are in-window but
  unsampled. Immaterial to the caveat's substance: interval 0 exercises
  fp[0] AND fp[1], interval n−2 exercises fp[-2] AND fp[-1] — all four
  inexact node data enter the compared values. The advisory's "the
  probe window INCLUDES the four edge intervals" is true of the window,
  loose about the sampling; the operative claim stands.
* Independent sizing (hand, order-of-magnitude): perturbing the s-data
  by δ shifts h by D²(δ0B4+δ1B5); max B4 = max B5 = t²(1−t)³/2 at
  t = 2/5 → 0.01728 (advisory's 0.017 ✓). Worst combined |Δh| ≤
  0.0173·dT⁴·|cp'''|·(1/3+1/6) = 0.00865·dT⁴·|cp'''|. At dT = 2850/8191
  = 0.348 K and cp''' ~ 4e-7..1.2e-6 J/(kg·K⁴) (NASA-7 upper-branch
  CH4/O2-product magnitudes, Rg ~ 400): |Δh| ~ 5e-11..1.5e-10 J/kg vs
  tol_h_o ≈ 8.9e-8 J/kg → **2.8-3.3 orders below the band at the
  aggressive end of cp''', more at the soft end** — consistent with the
  advisory's "3-5 orders" (its range reaches 5 for the cp/s0 channels,
  whose bands are far larger: my cp check gives ≈ 4.6 orders against
  tol_cp_o ≈ 1.5e-5). Band-breaking threshold: 0.00865·dT⁴·cp''' =
  tol_h_o ⟹ dT ≈ 9.6-13 K ⟹ N_TAB ≈ 220-300 — the advisory's
  "dT ≳ 5-10 K (N_TAB ≲ ~500)" is the right ballpark, mildly
  conservative on N_TAB.
* Direction claim sharpened, and it HOLDS: the oracle takes a max over
  2003 probes of which ~2001 sit on interior intervals with exact data;
  an unmodeled edge term can only ADD deviation at the two edge probes
  (spurious-FAIL direction) and cannot mask an interior defect (which
  the clean interior probes expose independently). A defect confined to
  the edge-data handling itself would enter at O(dT²·cp')-scale ≫ band
  and still fire. "Conservative, never a false PASS" is right.
* s0 channel: the s0-quintic s-data ((cp'T−cp)/T²) also inherit the
  edge cp' error → extra edge term ~ 0.0173·dT²·(dT²cp'''/3)/T ~ 3e-14,
  4 orders under the s0 roundoff term ≈ 2.2e-10 — the advisory's
  parenthetical covers it. Verdict on CAV-1 and on both repair options
  (1 doc line, or 4th-order one-sided edge stencils — 5-point one-sided
  IS exact on quartics): confirmed.

---

## C. The thrust-panel caveat (CAV-2) — the θ1 = θB/n_B domain

**SURVIVES, with the object made precise for the judge merge.**

Source facts (all verified): arc stations start at k=1 → θ1 = θB/n_B
(a1_toc 367-371; scan twin 541-545); n_B = ceil(θB/da) (233) ⟹ θ1 ≤ da;
the wall array's first row IS arc station 1, no θ=0 throat point exists
anywhere in wall_pts (386-415, 468); thrust_J (953-960) is the signed
trapezoid 2π·Σ½(py_{i+1}+py_i)(y_{i+1}−y_i) over consecutive wall rows —
so the implemented domain is [θ1, θB] + contour, while the docstring
(23-27) documents "(0, theta_B]". All four call sites (1326 objective,
1789/1802 O3.1 probes, 1921 J_star) consume the same station wall.

(i) **The missing piece is exactly the [0, θB/n_B] arc sliver** —
CONFIRMED. ΔJ_sliver = 2π ∫₀^{θ1} p(θ)·y(θ)·rtd·sinθ dθ with
y(θ) = yt + rtd(1−cosθ).

(ii) **O(da²), not O(da)** — CONFIRMED with the reason made explicit:
the panel's θ-width is O(da) but the integrand carries dy/dθ =
rtd·sinθ = O(θ), which vanishes at the throat; equivalently the y-span
of the sliver is rtd(1−cosθ1) = O(θ1²). Exact leading term: ΔJ ≈
π·p_t·yt·rtd·θ1² (1+O(θ1²)). At da = 0.5°, yt = 1, rtd = 0.45:
ΔJ ≈ 1.07e-4·p_t — the advisory's "≈ 2π·p_throat·yt·rtd·(1−cosθ1)",
"O(da²) ≈ 1e-4·p_t·(scale)" is the same expression and number.

(iii) **The θB-derivative is deterministic — the impl side CONFIRMS the
math review's [NEW] claim, with the mechanism:** on the sliver, p(θ) is
kernel/fan flow on the FIXED arc circle — W-independent by construction
(the fan bucket is W-independent; the arc geometry depends only on rtd,
yt) — so ΔJ depends on the design ONLY through the upper limit
θ1 = θB/n_B, which is traced within a frozen plan. Hence
  dΔJ/dθB = 2π·p(θ1)·y(θ1)·rtd·sin(θ1)·(1/n_B)
          ≈ 2π·p_t·yt·rtd·θ1/n_B  > 0,
i.e. the implemented dJ/dθB UNDERSTATES the documented-domain dJ/dθB by
this deterministic, sign-definite amount (O(da²/θB) after θ1 = θB/n_B ≈
da), and the implemented optimizer's θB-stationarity is biased by the
same term relative to the documented functional. ACROSS plan re-records
n_B = ceil(θB/da) jumps, so ΔJ(θB) is piecewise smooth with O(da³)
jumps — the advisory's "varies smoothly with θB inside a frozen plan"
carries exactly the right qualifier. **OBJECT FOR THE JUDGE MERGE:
ΔJ_sliver(θB) = 2π∫₀^{θB/n_B} p·y·rtd·sinθ dθ, p = kernel flow;
both reviews must be speaking of this integral and its 1/n_B-scaled
θB-derivative.** The advisory's own (ii) (ambient term) re-derived:
thrust with ambient = J_vac − Pa·π(y_lip² − y_start²); implemented
y_start = y(θ1) is θB-dependent ⟹ d/dθB of the ambient term =
2π·Pa·y(θ1)·rtd·sinθ1/n_B — matches the advisory's
"O(Pa·yt·rtd·θ1·dθ1/dθB)"; and "moot in code" is verified (no Pa term
exists in thrust_J or anywhere in the objective).

(iv) **S18 oracle/GENO: unaffected — CONFIRMED.** O2 is a CONTOUR
oracle: our optimum wall vs the GENO type-2 wall inside GENO's OWN
two-resolution Richardson band (docstring 54-57; implementation ~2000-
2010: band = GENO's two-resolution wall delta, K_RICH-safetied;
out-of-band count at 1762). thrust_J never enters O2, and no cross-code
CF/thrust-value comparison exists in the carrier — the sliver cannot
touch the cross-code verdict. What IS affected: the recorded J values
(J0, J_star) and any future absolute-CF comparison — adding the θ=0
station shifts J by the constant-ish ΔJ ≈ 1e-4·p_t·(π·yt·rtd) and
re-baselines them, which is why the advisory's cheaper doc-scoping
repair is correctly ranked. One addition the advisory leaves implicit:
if the doc-scoping repair is chosen, the M0/doc statement should scope
BOTH the J value AND the "Pa drops out"/gradient statement to the
implemented [θ1, θB] domain (the sliver's θB-derivative is the
math-side [NEW] object; scoping only the value would leave the
gradient statement dangling).

---

## D. The "4 micro-repairs ≤ 3 lines each" list — each verified at source

| Item | Real? | Still open? (current-tree evidence) | Honestly sized? |
|---|---|---|---|
| m12-F3 scoping line | YES | OPEN: the " [replayed callback record failure, M1 memo]" suffix is live (a1_toc 1160-1161); the bit-transparency claim is still unscoped ("never WHAT", 1040; "only decide WHO", 1090); no numeric-outputs-only scoping line exists (grep: no hit) | YES: 1 registration line |
| m12-F6 M2 control / registered supersession | YES | OPEN: `_vg` (1341-1353), MG `_mvg` (224-236), def_twin `_mvg` (671-683) carry no first-hit control; no supersession-by-m12gate registration line anywhere (grep "supersed" hits none in the M2 blocks); side gap inside F6 also still true: engine_speed_bench:26 promises bit-identical "(W, J, n_segments, wall)" but 321-328 compares W/J/n_segments only, no wall row | QUALIFIED: "≤3 lines" holds ONLY for the registration-line option; the mirror-control option (fresh recompute + bitwise compare + nextafter miss) is realistically 5-10 lines. The advisory's "one-to-three-line repairs" is honest under the registration reading it plainly intends, but the judge should record which option is meant |
| m12-F11 assert strip-proof | YES | OPEN: both controls are bare `assert` (1177-1180, 1183-1184) and the probe counters increment AFTER them (1185-1186) — under `python -O` the counters would over-claim, exactly as stated | YES: 2-4 lines (two if-not-raise rewrites) |
| m12-F8 t_grad band | YES | OPEN: t_grad times `jax.jit(jax.grad(scalar_J))` (1863-1867) while the walk executes `jax.jit(jax.value_and_grad(scalar_J))` (1327); the T2 comment (1969-1970) asserts "t_grad IS the measured whole value_and_grad wall" — an identification, not a measurement, in a measured-bands repo | YES: 2-line val_grad timing |

Completeness cross-check of the advisory's not-landed list: the other
m12 caveats ARE landed at source — F1/F2 as code (1194-1198, 1453-1456;
_mkey 1105-1114 re-reading M_NODES/KNOT_XI/N_NEWTON at request time;
record_ctx_tag 994-997), F4 as the DECLARED probe-tax clause
(docstring 1051-1055) and F5 as the declared once-per-walk V12 reading
(1097). One hair on F4: the landing is declaration-only — no campaign
entry sets A1_MEMO_PROBE=0 (grep: only the definition site and the
docstring) — which is within the refuter's offered repair options
("declare the tax"), so the advisory's silence is defensible; the judge
may want the def_twin campaign entry to consume the declared permission.

---

## E. Judge-quality audit (were the cited lines actually opened?)

**PASS with two blemishes.** Over 30 cited line references were
spot-verified against the current tree and ALL resolve exactly
(thermotab 123/124-127/134-158/248-275/261-263/265/274/504-506/469-477
[C6 body 471-477]/524-574/550; a1_ideal 278-303/311/317/424/429/
462-469/475-481/485-488/490-502/515/710; a1_toc 23-27/133-152/155-167/
170-184/261/267/367-371/629-632/727-745/929-933/953-960/1105-1114/
1159/1164/1198/1339/1345/1350/1456/1964-1998/1973; MG 155-163/175-201/
186-189/240-251/278-281[baseline]/304; def_twin 541-544/562-603/
608-611/635-637/662-698/837-845/852-864; bench 336-338; M0 1683-1695/
1943-1951). Decisive provenance signal: the advisory cites POST-repair
line numbers that differ from the m12/m4 refuter files' pre-repair
numbers (e.g. fresh sites 1198/1456 vs the refuter's 1077-1122/
1365-1404; T2 at 1973 vs 1880) — the reviewer demonstrably re-opened
the live tree rather than transcribing the refuters. Blemish 1
(cosmetic): the summary's self-pointers are wrong — "repair-
completeness ledger (§8)" lives in §7 and "7 minor notes (§9)" is the
§10 ranked list (§8 = margin_governor, §9 = def_twin). Blemish 2
(substantive): the §3 R6 "exact ... re-derived, correct" endorsement is
the A6 refutation above — the single place where claimed re-derivation
does not withstand the exact algebra.

---

## CONVERGENCE TABLE

| # | Claim (advisory) | Refuter verdict | Status | Precise disagreement (if any) |
|---|---|---|---|---|
| 1 | Quintic basis + dB faithful (36 conditions) | SURVIVES | settled | none — independently reproduced 36/36 |
| 2 | derived_newton_trips faithful (T''=−cp'/cp³, M, +1 trip honest) | SURVIVES | settled | none; pointwise pairing = grid sampling, 8 orders of headroom vs one trip boundary, rejector-covered; peripheral half-nit: invert_h `.get(K_NEWT, N_NEWT_INV)` silent fallback vs the "kept ONLY as reference/ceiling" docstring — half-line fence, not an advisory error |
| 3 | grid_uniformity faithful + R6 sizing formula "exact … re-derived, correct" | SURVIVES-WEAKENED | settled (correction required, no judge dispute — 3-line algebra) | exact flip condition is ε > fr_k/i_k (i=0 never flips), NOT fr_k/(i_k+fr_k) (= first-order approx). Control still fires (deciding probes i≈8190, discrepancy 1e-4; margin 1.9998×). Repair: 1-line code-comment fix (660-663) + amend the advisory sentence |
| 4 | C-A caveat CAV-1 (edge-stencil overclaim, 3-5 orders below band, conservative) | SURVIVES | settled | refinement only: probe SET samples 2 of the 4 edge intervals (0, n−2) — which exercise all four inexact node data; my sizing 2.8-3.3 orders (h channel, aggressive cp''') to 4.6 (cp channel); threshold N_TAB ≈ 220-300 vs advisory's "≲500" |
| 5 | custom_vjp rule faithful (sign/transpose; z0 zeros; ta None) | SURVIVES | settled | none |
| 6 | damped Newton + cert metric + solve_cert faithful | SURVIVES | settled | none (consumer indexing verified both ends; NOTE-5 stale docstring confirmed at 710) |
| 7 | spline_coeffs/eval/wall_geometry faithful | SURVIVES | settled | none — rows re-derived exactly |
| 8 | thrust_J caveat CAV-2 (domain [θ1,θB], O(da²), Pa-statement scoping) | SURVIVES | **needs-judge (merge only)** | no impl-side disagreement; judge must merge with the math review on the SAME object: ΔJ_sliver(θB) = 2π∫₀^{θB/n_B} p·y·rtd·sinθ dθ, dΔJ/dθB = 2π·p(θ1)y(θ1)rtd·sinθ1/n_B > 0, deterministic per frozen plan, piecewise across re-records; O2 (contour oracle) untouched; doc-scoping repair should cover value AND gradient statements |
| 9 | M4 equivalence by construction + M4-F1 landed + kkf exact | SURVIVES | settled | none |
| 10 | M1/M2 repairs complete (F1 both sites, F2 request-time key); counters truthful | SURVIVES | settled | reconciliation identity independently re-derived for all three episode types; gate check verified verbatim |
| 11 | T2 repricing faithful; F8 concurred | SURVIVES | settled | none; F8 confirmed at source (jit(grad) 1863-1867 vs jit(value_and_grad) 1327) |
| 12 | MG KS + G1 surrogate + (G) EXACT vs M0 | SURVIVES | settled | none — M0 block read independently, symbol-for-symbol match at all four code sites; BOUND (b) honored (den reported, never guarded) |
| 13 | def_twin masked KS + DE bucket + C5 + R-GRAD | SURVIVES | settled | none — bucket matches M0 S24 block incl. degenerate and empty cases; C5/R-GRAD algebra exact |
| 14 | NOTE-2 "four micro-repairs, each ≤3 lines" | SURVIVES-WEAKENED | settled (record the reading) | all four real and open (evidence above); F6's "≤3 lines" true only for the registration option — the mirror-control option is 5-10 lines; F4 landed by declaration only (no campaign entry consumes A1_MEMO_PROBE=0) |
| 15 | Overall 0-MISMATCH / 11 faithful / 2 caveat | SURVIVES | settled | my independent pass also found NO math-to-code MISMATCH; the two review-text defects (row 3 endorsement; §8/§9 self-pointers) are in the ADVISORY, not the code, and flip no verdict |

**Needs-judge: row 8 only** (cross-review object merge; both refuters
appear to agree on the object — the judge should confirm the math side
names the same integral and the same 1/n_B scaling and then merge the
repair wording). Rows 3 and 14 need only be RECORDED (correction +
option-reading), not adjudicated — the algebra is 3 lines and checkable.

*Label: dedicated refuter, round 1, source-only, no execution; sized
numbers in §B-§C are hand estimates from table/case parameters
(N_TAB = 8192, [1050, 3900] K, da = 0.5°, yt = 1, rtd = 0.45).*
