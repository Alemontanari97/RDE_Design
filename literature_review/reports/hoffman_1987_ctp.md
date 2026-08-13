# Expert read — Hoffman 1987, "Design of Compressed Truncated Perfect Nozzles"

Reader: convergence-review expert reader. Date of read: 2026-08-13.
File: `literature_review/hoffman_1987_compressed_truncated_perfect.pdf`

## 1. Citation (verified from the PDF itself)

Joe D. Hoffman (Professor of Mechanical Engineering, Thermal Sciences and Propulsion Center,
Purdue University, West Lafayette, Indiana; Member AIAA), **"Design of Compressed Truncated
Perfect Nozzles"**, *Journal of Propulsion and Power*, Vol. 3, No. 2, March–April 1987,
pp. 150–156.
Footnote of record on p. 150: "Presented as Paper 85-1172 at the AIAA/SAE/ASME/ASEE 21st Joint
Propulsion Conference, Monterey, CA, July 8–10, 1985; received Nov. 13, 1985; revision received
April 25, 1986. This paper is declared a work of the U.S. Government and is not subject to
copyright protection in the United States."
No DOI printed on the scan. Sponsor (Acknowledgments, p. 156): Air Force Rocket Propulsion
Laboratory, Edwards AFB; initial impetus Dr. Daweel George; Program Manager Mr. Steve Brown.

## 2. Read coverage

**7 / 7 pages read in full (pp. 150–156), figures, all six tables, Acknowledgments and the
complete 8-item reference list included.** The article is 7 printed pages; there is no appendix,
no supplementary material, no nomenclature beyond the one on p. 150. Nothing was skipped.
Limitation of the source: it is a **greyscale page scan**, so numerical values were read off the
rendered page images. All numbers quoted below are from the *tables and body text* (crisp), never
from figure curves; where I refer to a figure I say "read from Fig. N" and treat it as
qualitative. Two typographic caveats are declared in §4 (Eq. (1) subscripts; Ref. 2 page range).

## 3. What the paper actually does

**Problem.** Given a *fixed nozzle envelope* — a prescribed length `L` and exit area ratio `ε`,
in practice the envelope of an existing Rao nozzle — produce a diverging contour with the highest
possible vacuum specific impulse, using a *non-variational* construction. The competitor question
is explicit: Gogish (Ref. 3) had suggested that compressed truncated perfect (CTP) nozzles could
*beat* Rao nozzles for very short envelopes; the paper's object is "to develop a method for
designing compressed truncated perfect nozzles and to develop a procedure for predicting the
performance of such nozzles" (p. 150, Introduction).

**Formulation.** *There is no variational formulation.* The whole paper contains four numbered
equations:

- Eq. (1): the compression factor `C`, a ratio of axial extents measured from the attachment
  point (see §4, caveat (i));
- Eq. (2): `F_SS = ∫_{y_t}^{y_e} (P − P_a) 2πy dy` — supersonic-contour thrust as the axial
  component of the wall pressure force, integrated numerically;
- Eq. (3): `F_N = F_IVL + F_SS` — total nozzle thrust = initial-value-line thrust + wall thrust;
- Eq. (4): `I_sp = F_N / ṁ`.

The design is a three-step *construction*, stated on p. 150 ("Compressed Nozzle Design"):
(1) design a **perfect nozzle** (shockless MOC contour giving uniform parallel exit flow) at some
area ratio `ε_perfect`; (2) **truncate** it at a smaller area ratio; (3) **linearly compress** the
truncated contour in the axial direction to the desired length. A slope discontinuity is created
at the attachment point A; it is removed by **shifting the compressed contour downstream by
`Δx_s`** until it is tangent to the circular-arc initial-expansion contour, which moves the
attachment point A → A′ with a *larger* attachment angle (p. 151, Fig. 3).

**Unknowns / design variables.** Effectively **one scalar**: the design area ratio `ε_perfect` of
the parent perfect nozzle (Tables 4 and 5), or, in the second study, the truncation area ratio
`ε_truncated` at fixed `ε_perfect = 600` (Table 6). The wall shape is *not* a free function: it is
determined by the construction. There are no shape degrees of freedom in the optimization sense.

**Constraints.** Hard geometric envelope: the compressed nozzle must have exactly the length and
area ratio of the reference Rao nozzle ("All of these nozzles have the same length and area ratio
as Rao Nozzle 1, namely, L = 60.189 in. and ε = 400", footnote a of Table 4). Throat geometry
fixed (`y_t = 1.0 in`, `ρ_tu = 1.0 in`, `ρ_td = 2.0 in`, Table 1). No other constraints.

**Flow model.** Steady axisymmetric inviscid flow of a **thermally *and* calorically perfect gas**:
"The flowing fluid is assumed to be a thermally and calorically perfect gas (i.e., constant
molecular weight and specific heats). The presence of condensed phases and chemical reactions is
neglected, and boundary layer effects are considered negligible. Consequently, the flowfield is
isentropic everywhere except across the oblique shock wave, which is described by the standard
oblique shock wave relationships." (p. 151). Uniform-stagnation-state reservoir upstream.
Transonic/throat region by the **Kliegel–Levine** perturbation solution (Ref. 5), which supplies
the initial-value line `TT′`, the mass flow rate `ṁ`, the discharge coefficient `C_D` and the
initial-value-line thrust `F_IVL`. Supersonic region by the **method of characteristics**.
When compression is strong enough, right-running compression waves **coalesce into a fitted
oblique shock** starting at a point S; downstream of it "the flowfield ... is rotational due to
the entropy gradient produced by the curved oblique shock wave" (p. 151).

**Solver.** *No optimizer.* A **parametric enumeration**: a database of 24 perfect nozzles with
area ratios from 97.32 to 800 was generated and stored on disk (p. 152–153); each was truncated
and compressed into the target envelope and evaluated by MOC; the best of the family was reported.
Three reference envelopes were used (Rao Nozzles 1/2/3, Table 2). The Rao contour of Nozzle 1 was
**furnished by private communication** (Ref. 8, S. Brown, AFRPL, Sept. 1983); Nozzles 2 and 3 were
generated by an "in-house program" that "selects points from the right-running Mach line emanating
from the nozzle throat downstream circular arc contour as initial points, and solves the Rao¹
nozzle design equations to determine the exit left-running Mach line for the corresponding Rao
nozzle" (p. 153).

**Verification.** *None in the modern sense.* No grid-refinement study, no error bars, no
comparison to experiment or to an independent CFD code (VNAP2 is cited as Ref. 6 for complicated
throat sections but no cross-check is reported). Verification is implicit and internal: two
independent generators of Rao contours (Brown's contour and the in-house program), and the
consistency of the perfect-nozzle family. The paper's own scope disclaimer: "Although the
parametric study was of limited scope..." (Conclusions, p. 156).

**Headline results (all from the printed tables/text).**

| quantity | value | source |
|---|---|---|
| γ, R, P_t, T_t, **P_a** | 1.2155, 68.1753 ft-lbf/(lbm-R), 1500.00 lbf/in², 6131.25 R, **0.0** | Table 1, p. 151 |
| Rao Nozzle 1 | ε = 400, L = 60.189 in, y_e = 20.000 in, θ_a = 39.833°, ṁ = 26.672 lbm/s, F = 9297.8 lbf, **I_sp = 348.60** | Table 2 |
| Rao Nozzle 2 | ε = 190.43, L = 38.255 in, ṁ = 26.672, F = 9102.9, **I_sp = 341.29** | Table 2 |
| Rao Nozzle 3 | ε = 97.32, L = 24.567 in, ṁ = 26.672, F = 8893.4, **I_sp = 333.45** | Table 2 |
| perfect nozzle at ε = 400 (unconstrained length, L = 146.717 in) | **I_sp = 350.33** | Table 3 |
| best CTP in Rao-1 envelope (ε_perfect ≈ 650) | **348.02** = **−0.17 %** vs Rao | Table 4 + p. 153 |
| best truncated-perfect at Rao-1 length (ε_perfect ≈ 700) | **347.56** = **−0.30 %** vs Rao | Table 5 + p. 154 |
| conical fitted in Rao-1 envelope | **342.79** (−1.67 %) | p. 153 |
| 15-deg conical, same length | **342.43** (−1.77 %) | p. 153 |
| best CTP vs Rao Nozzle 2 | **−0.04 %** | p. 154 |
| best CTP vs Rao Nozzle 3 | **−0.34 %** | p. 155 |

Shock incidence (this is the load-bearing physical result): in Table 4 only the two most strongly
compressed designs shock (ε_perfect = 410 → 344.35 and 450 → 346.79, both "yes"), and they are the
two *worst* of the series; in Table 6 the shocked designs degrade monotonically
(484 → 347.42, 529 → 346.09, 576 → 343.23, 600 → 337.67, all "yes"). Hence p. 154: "This result
suggests that the presence of the shock wave is not beneficial to nozzle performance, which is
contrary to the principle behind the compressed truncated perfect nozzle concept proposed by
Gogish." And p. 154, on Table 6: "the best nozzle of this design series is the one truncated at
the area ratio of the reference Rao nozzle and compressed to the length of the reference Rao
nozzle. In other words, that nozzle fits exactly into the envelope of the reference Rao nozzle." —
i.e. **zero compression is optimal**; the whole CTP idea is self-defeating in its own family.

**The abstract's two sentences of record** (p. 150): "It was found that Rao nozzles always yield
higher performance than compressed truncated perfect nozzles. However, the performance differences
are quite small (0.04–0.34%), which shows that compressed truncated perfect nozzles are good
propulsive nozzles. For nozzle envelopes for which the Rao nozzle design concept fails, compressed
truncated perfect nozzles may yield very efficient nozzle designs."

**Proved vs asserted.** The paper *proves* nothing analytically — there is not a single theorem,
lemma or derivation. It *demonstrates numerically*, on 3 envelopes × (7–10) designs each, that the
best CTP loses to Rao by 0.04–0.34 %. It *asserts* universality: "thus suggesting that the Rao
nozzle design concept will always yield higher performing nozzles than the compressed nozzle
design concept" (p. 156) — an extrapolation from a study the paper itself calls "of limited
scope", at a single γ, a single throat geometry and **P_a = 0**.

## 4. Hypotheses

**Declared.**
H-d1. Steady, inviscid, axisymmetric flow.
H-d2. Thermally *and calorically* perfect gas — constant molecular weight and constant specific
heats (γ = 1.2155 fixed, Table 1).
H-d3. No condensed phases, no chemical reactions (frozen, single-species-equivalent).
H-d4. Boundary layer effects negligible.
H-d5. Isentropic everywhere except across the oblique shock; shock treated by standard oblique
shock relations (fitted, not captured).
H-d6. Uniform upstream flow region with constant stagnation pressure and temperature (p. 151).
H-d7. Kliegel–Levine perturbation valid in the throat region: "The flowfield in the throat region
of the nozzle is assumed to be completely specified by the perturbation analysis developed by
Kliegel and Levine, which depends only on the geometry of the nozzle throat" (p. 151).
H-d8. The shock-origin point S is *known*: "The flowfield model described above is based on the
assumption that the location of point S, the point where the oblique shock wave originates, is
known" (p. 151), and is predetermined by shock-free Mach-line coalescence detection.
H-d9. P_a = 0 (Table 1) — vacuum operation.

**Undeclared but necessary.**
H-u1. **Single operating point.** No family of inflow states, no measure, no trajectory. The
objective is a vacuum I_sp at one stagnation condition.
H-u2. **Full-flowing, shock-free-at-exit, supersonic-exit nozzle** — no separation model, no
over/under-expansion, no base pressure, no plug.
H-u3. **Existence and uniqueness of the MOC solution** on the constructed contour, including
across the fitted shock; no certificate (no Lax/entropy/Lopatinskii check) is discussed.
H-u4. **Single oblique shock**, right-running, that does not reflect off the axis or interact with
itself; the description "continued until the end of nozzle, point E″, is reached" (p. 151)
presumes no reflection reaches the wall in a way that invalidates the march.
H-u5. **The linear axial compression map preserves admissibility** — no monotonicity, convexity or
curvature check on the compressed wall; the C¹ defect at A is patched by the Δx_s shift, but the
resulting family is not claimed to be smooth in ε_perfect.
H-u6. **The 24-nozzle grid resolves the CTP optimum.** All reported "optimum CTP" values are grid
maxima over Δε_perfect = 50–100 (Table 4) — a discrete argmax, never a stationarity condition.
H-u7. **The reference Rao contours are correct.** Nozzle 1's contour is unpublished (Ref. 8,
private communication); Nozzles 2–3 come from an in-house implementation of Rao's equations, with
no cross-verification reported.
H-u8. **The evaluator's numerical error is far below the differences discussed.** The entire
discussion lives at 0.04–0.8 % in I_sp; no discretization error is quantified anywhere.
H-u9. **Thrust bookkeeping is complete** — F_IVL + wall integral, with the same C_D and the same
initial-value line for Rao and CTP designs, so that the comparison is apples-to-apples. Stated
implicitly by "The gas thermodynamic properties, nozzle operating conditions, and nozzle throat
contours were the same for all of the parametric studies" (p. 152).

**Typographic caveats declared.** (i) Eq. (1) is printed as a ratio of two axial differences
anchored on the attachment point / origin; the subscripts on the exit-station symbols
(x_e, x_e′, x_e″, x_a, x_o of Fig. 2) are not fully resolvable in this scan, so I do not quote the
subscript pattern as certain — the *meaning* (linear axial compression ratio of the truncated
contour into the target length) is unambiguous from the surrounding text. (ii) Ref. 2 (Ahlberg
et al.) is printed "ARS Journal, May 1961, pp. 614–620" without a volume number.

## 5. Independent arithmetic checks I performed (not in the paper)

These are *my* computations from the paper's Table 1/2/3 inputs, reported as such:

- **Mass flow.** 1-D isentropic choked flow with γ = 1.2155, R = 68.1753 ft-lbf/(lbm-R),
  P_t = 1500 lbf/in², T_t = 6131.25 R, A\* = π(1.0)² in² gives ṁ_1D ≈ **26.93 lbm/s**. The paper's
  ṁ = 26.672 lbm/s (Table 2, identical for all three nozzles) implies a discharge coefficient
  **C_D ≈ 0.990**, which is exactly the value Kliegel–Levine predicts for ρ_td/y_t = 2.0. The
  paper's throat model is therefore internally consistent and *externally checkable*.
- **Perfect-nozzle I_sp.** A perfect nozzle has uniform parallel exit flow, so its thrust is
  exactly ṁV_e + p_eA_e. At ε = 400 the 1-D isentropic solution (M_e ≈ 6.138) gives a vacuum
  I_sp ≈ **350.4 s** against the paper's Table 3 value **350.33 s** — agreement to ≈ 0.02 %.
  Table 3 is thus a *reproducible* artifact independent of the unpublished Rao contour.
- **Reframing of the margin.** Using the paper's own numbers at the Rao-1 envelope, deficits
  against the length-unconstrained perfect nozzle (350.33) are: Rao 1.73 s (0.494 %),
  best CTP 2.31 s (0.659 %), best truncated-perfect 2.77 s (0.791 %), conical-in-envelope 7.54 s
  (2.15 %). The variational design therefore recovers **25 % of the length-constraint deficit
  relative to CTP**, **37 % relative to truncated-perfect**, and **77 % relative to conical**.

## 6. Findings — three-level comparison against the programme

### TEORICO

**T1 — THREAT (touches: F7 in-class +0.51 %, campagne O3.2/O3.3; also the programme's practical
motivation).** The paper *quantifies* the practical prize of the whole variational apparatus in
its own class and it is small: 0.04 % (Rao Nozzle 2), 0.17 % (Nozzle 1), 0.34 % (Nozzle 3) of I_sp
against a purely constructive competitor. Since ṁ = 26.672 lbm/s is identical for all designs
(Table 2, same throat and stagnation state), ΔI_sp % = ΔF % exactly, so these numbers are directly
commensurable with our thrust-based J. Our F7 in-class surplus (+0.51 % at ε = 30, L = 8) is the
same order of magnitude as Hoffman's entire Rao-vs-heuristic gap — meaning: (a) our measured
surplus is *not* implausibly large, it sits just above the classical scale; (b) our claim of
practical significance must be stated at that scale, not inflated. Three bounded defences, all
anchored in the paper: (i) **P_a = 0** (Table 1) — the study is vacuum-only, precisely the corner
where our own T-T3-MAP says the problem degenerates and the Pa≠0 first-order breaker is switched
off; (ii) the gaps are grid maxima (see A3), hence *upper* bounds on the true gap — the threat is
if anything harsher than printed; (iii) the same tables give the counter-scale: Rao beats
conical-in-envelope by 1.67 % (348.60 vs 342.79, p. 153) and recovers 25–37 % of the
length-constraint deficit (§5). **Evidence:** abstract p. 150; Table 1 (P_a = 0.0); Table 2;
Table 4; p. 153 "0.17% less"; p. 154 "(0.04%)"; p. 155 "(0.34%)". **Confidence: ALTA.**

**T2 — CONTAINED (touches: (P), T-T3, claim 18 containment).** Hoffman 1987 is a *degenerate
member of (P)*: measure μ = a single Dirac atom (H-u1); one frozen γ = 1.2155, calorically perfect
(H-d2) ⇒ H1 and Lemma B_T3 of T-T3 hold exactly; fixed wall, full-flowing, supersonic exit ⇒ H2′;
per-phase uniqueness assumed ⇒ H4; P_a constant (= 0). All five T3 hypotheses are satisfied, so
J[Σ] = F[Σ; P_c] holds trivially and the cycle layer is empty. The admissible set, however, is
*not* A_gen(c) nor even A_h: it is a **one-parameter constructed family** {CTP(ε_perfect)}, a
measure-zero curve inside our shape space. Consequence of record, and it is the sharp one:
**within the T3 collapse class the practical prize of our apparatus is capped near Hoffman's
number.** The programme's practical value must therefore be argued from *outside* T3 — the named
breakers (P_a ≠ 0 and the harmonic-mean I_sp collapse, multi-γ mixture form, swirl debit, subsonic
patches, the length-capped plug PB-2) — not from the steady bell at vacuum. **Evidence:** Table 1;
p. 151 "thermally and calorically perfect gas"; p. 152 "The perfect nozzle contours were stored on
disk and used as needed"; Table 3 (the 24-member family). **Confidence: ALTA.**

**T3 — GAP-CONFIRMS (touches: REQ-NONSTALL / gate F1, fixed-ε transversality bookkeeping,
H-CLASS).** Two independent statements in the paper confirm that the *classical construction can
fail to deliver a design at a prescribed envelope* — the exact need that REQ-NONSTALL encodes:
(i) p. 153, on the in-house Rao generator: "if a specific length or area ratio is required, the
program must be run in an iterative manner. For that reason, an exact area ratio was not required.
Hence, Rao nozzles having area ratios close to the desired nominal area ratios of 200 and 100 were
selected for use in the parametric study" — the classical free-endpoint construction **cannot hit
a prescribed (ε, L)**; it can only shoot at it, and the authors gave up and accepted ε = 190.43
and 97.32 instead of 200 and 100 (Table 2, "Nominal area ratio" vs "Exact area ratio"). This is
exactly why our formulation replaces Rao's free-endpoint Eq. (14) with the lip-constraint
multiplier λ_e = dJ/dy_lip at fixed (ε, L). (ii) Abstract and Conclusions: "For nozzle envelopes
for which the Rao nozzle design concept fails, compressed truncated perfect nozzles may yield very
efficient nozzle designs" (pp. 150, 156) — the corpus itself records that the Rao construction has
*no design* for some envelopes, without characterising when or why. That is a published, citable
corroboration that REQ-NONSTALL addresses a real, classically acknowledged defect, and it is
adjacent to our H-CLASS failure (the design class losing certifiability before reaching the deep-DEF
region). **Evidence:** p. 153; abstract p. 150; Conclusions p. 156; Table 2 nominal-vs-exact ε.
**Confidence: ALTA.**

**T4 — CORRECTION (touches: the reading-list framing of this paper; litmap wording).** The list
entry frames this paper as "epitaffio della linea USA: CTP ≈ Rao in pratica". The magnitude is
right but the *sign of the paper's verdict is the opposite of an epitaph for the variational line*:
Hoffman concludes that **Rao always wins, in every case tested**, and that **shocks never help** —
he explicitly *refutes* Gogish's compression-beats-Rao thesis ("This result suggests that the
presence of the shock wave is not beneficial to nozzle performance, which is contrary to the
principle behind the compressed truncated perfect nozzle concept proposed by Gogish", p. 154), and
his Table 6 shows the best member of the compressed family is the one with **zero compression**
(p. 154). The paper is therefore an epitaph for *Gogish's* claim and a quantification of the
*small size* of the variational prize at P_a = 0, not a devaluation of variational design. Two
further corrections to any citation of it: (a) the universality ("always") is **asserted**, from a
study the paper itself calls "of limited scope" (p. 156) — 3 envelopes, one γ, one throat, one
ambient pressure; (b) the honest way to state the 0.17 % is as **25 % of the length-constraint
deficit** (§5), not as "a fifth of a percent". Our litmap line for this paper should carry all
three qualifications. **Evidence:** p. 154 (Gogish refutation and the zero-compression optimum);
p. 156 (Conclusions, "of limited scope ... will always yield"); Tables 4 and 6 shock columns.
**Confidence: ALTA.**

### FORMALE

**F1 — CONTAINED (touches: Route A f1/CSTR_PA, fixed-ε transversality bookkeeping, E4).** The
paper's objective, Eqs. (2)–(4), is exactly the **primal wall-integral form** of our thrust
functional: F_SS = ∫(P − P_a) 2πy dy is the wall-pressure dual of our control-surface integrand
f1 = [(p − p_a) + ρW² sin(φ−θ)cos θ/sin φ] q, with the initial-value-line term F_IVL playing the
role of the upstream closure — i.e. Hoffman evaluates the same J on the wall where we evaluate it
on the check contour. With **P_a = 0** (Table 1), our corner condition CSTR_PA
(p_a = p − ½ρW² sin 2θ tan α) collapses to p_E = ½ρW² sin(2θ_E) tan α at the lip; and the paper's
own description of the in-house Rao generator — initial points on the throat downstream arc,
"solves the Rao¹ nozzle design equations to determine the exit left-running Mach line", exit lip
point "cannot be specified a priori" (p. 153) — is precisely the operational signature of Rao's
Eq. (14) being a **free-endpoint transversality condition**. So the classical formal apparatus is
present in this paper only as a *black box that generates the reference contours*, exactly as our
Route A describes it, and its known operational weakness (unprescribable ε) is on record here.
Constant γ throughout (Table 1) puts the whole paper inside the γ = const corner our E4 claim
isolates. **Evidence:** Eqs. (2)–(4), p. 152; Table 1 P_a = 0.0; p. 153 (Rao Nozzle Designs
paragraph). **Confidence: ALTA.**

**F2 — GAP-CONFIRMS (touches: P2/G14 Rao-as-adjoint bridge; claim 8 empty niche; claim 20 novelty
bound).** This paper contains **zero variational mathematics**: no Euler–Lagrange system, no
Lagrange multipliers, no transversality, no adjoint, no gradient. Four equations total, all
bookkeeping. Most tellingly, **Hoffman does not cite his own Route-B work** — neither Hoffman 1967
(the multiplier-field formulation with the E-residual, our Eq. (78) of record) nor
Scofield–Hoffman 1971 (our G2 oracle) appears in the 8-item reference list, and neither do
Guderley, Hantsch, Kraiko or Shmyglevskii. The single classical citation is Rao 1958 (Ref. 1).
That the principal Western author of the multiplier-field formulation, writing in 1987 on a
length-constrained nozzle design problem, reaches for a *heuristic construction plus grid search*
rather than his own variational machinery is strong positive evidence for the empty-niche claim
and for P2/G14: the two lines never met, not even inside one author's own bibliography.
**Evidence:** the complete reference list, p. 156 (see §7); absence of any Euler–Lagrange or
multiplier statement anywhere in pp. 150–156. **Confidence: ALTA.**

**F3 — ADOPT (touches: tier ladder margin vector m(Σ), F4b fitted-front initialisation, VI.2
evaluator / S1 boundary monitor).** The paper carries a clean, deterministic, cheap **tier-0 → tier-1
transition detector and fitted-front seeder**: "That point must be predetermined by first
constructing the network of left-running Mach lines without a shock wave and locating the point in
the characteristic network where right-running Mach lines coalesce. The coalescence of
right-running Mach lines indicates the formation of a right-running oblique shock wave." (p. 151).
That is: *run the shock-free march first; detect C-family coalescence; place the fitted front at
the coalescence point; re-run with the front.* We should adopt this in two places. (i) **VI.2
per-phase evaluator / margin vector**: the *distance to first coalescence* in the shock-free
characteristic net is an inexpensive, monotone, geometrically meaningful surrogate for a
"shock-onset margin", complementing our fold margin (Eq. (4)/Sternin) and causality margin
(u_x − c) — it detects the *compression-wave* route into tier 1, which the fold margin does not
see. (ii) **F4b front initialisation**: the coalescence point is the natural initial guess for the
fitted-front origin in the tier-1 march, replacing an arbitrary seed. Cost is one extra shock-free
march, which after the S25/S25-bis speed programme (segment 5.58 s) is affordable inside the
per-phase evaluator. **Evidence:** p. 151, "Flowfield Model" and the paragraph preceding it;
Fig. 4 (point S and the shock branch S–S′). **Confidence: ALTA.**

**F4 — ADOPT (touches: tier-ladder multiplier μ "prices shock-freeness"; claim 17).** Tables 4 and
6 constitute a **published, quantified price of shock-freeness** in a real design class, which our
tier ladder posits structurally but has so far measured only as an *inactive* margin (S20/S22, and
the F1 branch closed as "margin-inactive / cert-limited"). Table 4: the only two shocked designs
(ε_perfect = 410, 450) score 344.35 and 346.79 against 347.53–348.02 for every shock-free member —
a penalty of 1.2–3.7 s. Table 6 is stronger, because there truncation is swept monotonically and
the shock appears at ε_truncated = 484: 347.42 → 346.09 → 343.23 → 337.67 as the shock strengthens,
a 10 s collapse. Adoption: (i) record these as a **corpus prior** in the tier-ladder documentation —
in the compression direction the shock-freeness constraint is *strongly active* with a large
shadow price, which is qualitatively opposite to our two measured instances where μ came out
inactive, and that contrast is itself a diagnostic (our instances may simply not be pushing in the
compression direction); (ii) report a **"shock: yes/no" column** in every parametric Verdict sweep,
as Hoffman does — it is the cheapest possible tier-membership label and we currently do not print
it in sweep tables. Caveat on strength: this is one gas, one throat, P_a = 0, and it says nothing
about *plug* or *E-D* topologies where an internal front may be benign. **Evidence:** Table 4 with
its "Shock wave" column; Table 6 with its "Shock wave" column; p. 154 Gogish-refutation sentence.
**Confidence: MEDIA.**

### ALGORITMICO

**A1 — GAP-CONFIRMS (touches: claim 8 empty-niche; VI.5 driver).** The solver is a **1-D grid
enumeration**: build 24 perfect nozzles (ε from 97.32 to 800, Table 3), store them on disk,
truncate + compress each into the target envelope, evaluate by MOC, take the maximum. There is no
gradient, no constraint handling, no stationarity test, no convergence criterion. In the second
study (Table 6) the sweep is over ε_truncated at fixed ε_perfect = 600 — again enumeration. This
is the empty-niche claim made concrete from the *other* side: in the classical corpus, when a
constrained nozzle-shape optimum is wanted, either the closed-form Rao construction is invoked as
a black box or the design space is enumerated; **nobody keeps the variational/MOC formulation and
drives it with an optimizer.** Note the specific structural obstruction the paper displays without
naming it: the CTP construction produces a wall with a slope discontinuity at the attachment point,
patched by the ad-hoc Δx_s tangency shift (p. 151, Fig. 3), so the map ε_perfect ↦ contour is not
manifestly C¹ — a differentiable driver over this family would need exactly the kind of smooth
spline class A_h our formulation supplies. **Evidence:** p. 152–153 (24-nozzle database, "The
perfect nozzle contours were stored on disk and used as needed"); Tables 4, 5, 6 as grid sweeps;
p. 151 and Fig. 3 (Δx_s tangency repair). **Confidence: ALTA.**

**A2 — ADOPT (touches: VI.6 oracle stack; E4 / gate G2; DIR-THERMOTAB γ = const oracle policy).**
**Table 3 is a usable, fully specified, γ = const known-answer oracle for our MOC evaluator**, and
we should register it as such (proposed name [X-HOFF87]). All inputs are printed (Table 1:
γ = 1.2155, R = 68.1753 ft-lbf/(lbm-R), P_t = 1500 lbf/in², T_t = 6131.25 R, P_a = 0,
y_t = 1.0 in, ρ_tu = 1.0 in, ρ_td = 2.0 in) and Table 3 gives, for 24 area ratios from 97.32 to
800, the four outputs (θ_e, L, y_e, I_sp) of the *shockless perfect-nozzle* construction — a
deterministic MOC design with no free choices. Two immediate cross-checks I already ran (§5)
pass: the printed ṁ = 26.672 lbm/s implies C_D ≈ 0.990, exactly the Kliegel–Levine value for
ρ_td/y_t = 2, and Table 3's I_sp at ε = 400 (350.33) matches the 1-D isentropic vacuum I_sp I
compute (≈ 350.4) to 0.02 % — as it must, since a perfect nozzle has uniform parallel exit flow.
This makes Table 3 a **two-sided oracle**: the I_sp column is checkable analytically (1-D), while
the (θ_e, L, y_e) columns exercise the *characteristic net and the turning-region mass balance* —
precisely the part of our evaluator that no analytic check reaches. It sits naturally beside the
Scofield–Hoffman 1971 Table 2 Case 1 oracle (frozen thrust 2290 lbf) at gate G2, and it is a
*length* oracle, which S-H is not. **Explicit exclusion:** Table 2 (the three Rao nozzles) must
**not** be used as an oracle — Nozzle 1's contour is an unpublished private communication (Ref. 8)
and Nozzles 2–3 come from an unverified in-house code. **Evidence:** Table 1; Table 3; Table 2
ṁ = 26.672; Ref. 8, p. 156; §5 of this report for my arithmetic. **Confidence: ALTA.**

**A3 — CORRECTION (touches: any use of Hoffman 1987 numbers as ground truth; the F7 band
discipline).** Two defects bound how the paper's headline numbers may be cited. (i) **The reported
"optimum CTP" values are grid maxima**, not optima: Table 4 samples ε_perfect at
410, 450, 500, 550, 600, 650, 700, 750, 800 (Δε = 40–50), Table 5 at 300–800 (Δε = 50–100),
Table 6 at 256–600. The true best CTP is ≥ the grid best, so **0.04 %/0.17 %/0.34 % are *upper*
bounds on the true Rao-minus-CTP gap** — the threat in T1 is, if anything, understated by the
paper. The non-monotone ordering of the three gaps (0.17 % at ε = 400, 0.04 % at ε = 190, 0.34 %
at ε = 97) is itself consistent with grid noise rather than a physical trend, and the paper offers
no explanation for it. (ii) **No verification whatsoever is reported** — no grid-refinement study,
no error bar, no experimental or independent-code comparison — while the entire discussion lives
in the 0.04–0.8 % band. A discussion at 0.04 % resolution requires an evaluator whose
discretisation error is demonstrably ≪ 0.004 %, and nothing in the paper establishes that.
Corollary for us, and it is favourable: our own claims at this scale (F7 +0.51 % against a
pre-registered band of 5.38e3, with Richardson two-resolution bands of 4.5e-3 on the contour and
O3.1 transposition at 2.7e-10 vs tolerance 5.1e-8) are *better instrumented than the classical
result they are being compared against*, and that must be said explicitly whenever T1 is answered.
**Evidence:** the ε grids of Tables 4, 5, 6; absence of any convergence or uncertainty statement
in pp. 150–156; p. 156 "of limited scope". **Confidence: ALTA.**

**A4 — ADOPT (touches: VI.5 driver seeds; REQ-NONSTALL gate F1; H-CLASS).** The CTP construction
is a **universal feasibility generator**: unlike the Rao/DEF construction, it produces an
admissible contour for *any* prescribed (L, ε) envelope, by construction — truncate a perfect
nozzle at the required ε, compress to the required L — including envelopes where "the Rao nozzle
design concept fails" (abstract, p. 150) and including envelopes so short that the design carries
an internal fitted shock (Table 4, ε_perfect = 410, 450). We should adopt it as a **third driver
seed** beside the existing "Rao-at-⟨P_c⟩ (bell)" and "peak design (plug)": a *CTP-at-envelope*
seed, generated by the same three-step construction (perfect nozzle at a chosen parent ε →
truncate at the target ε → linear axial compression to the target L → Δx_s tangency repair at the
attachment point). Its virtues for us are exactly the two places we are currently stuck: (a) it
directly serves **REQ-NONSTALL** — the optimum search must never stall because the classical
construction has no solution or because a field with an internal shock cannot be computed; the CTP
seed is always defined, and Hoffman's own machinery shows the shocked member is evaluable with a
fitted front; (b) it reaches envelopes that the tier-0 9-dof class cannot reach, which is the
**H-CLASS** failure of record (min DE val 7.31e-2, 33× the tightest pre-registered floor) — a CTP
seed at a deep-DEF envelope gives the driver a feasible starting point in a region the DEF
construction does not cover. Seeds never affect the certified result, so the adoption cost is
bounded. **Evidence:** the three-step procedure, p. 150 "Compressed Nozzle Design" and p. 151;
Δx_s repair, p. 151 and Fig. 3; abstract/Conclusions escape clause, pp. 150 and 156; shocked
members evaluated in Table 4. **Confidence: ALTA.**

## 7. Bibliography inspection (record datum)

The reference list (p. 156) has **exactly 8 items**, transcribed:

1. Rao, G.V.R., "Exhaust Nozzle Contour for Maximum Thrust," *Jet Propulsion*, Vol. 28, June 1958,
   pp. 377–382.
2. Ahlberg, J.H., Hamilton, S., Migdal, D., and Nilson, E.N., "Truncated Perfect Nozzles in
   Optimum Nozzle Design," *ARS Journal*, May 1961, pp. 614–620.
3. Gogish, L.V., "Investigation of Short Supersonic Nozzles," *AN SSSR, Izvestiya, Mekhanika
   Zhidkosti i Gaza*, 1966, No. 2, pp. 175–180.
4. Zucrow, M.J. and Hoffman, J.D., *Gas Dynamics*, Vol. 2, John Wiley and Sons, New York, 1977,
   pp. 160–164.
5. Kliegel, J.R. and Levine, J.N., "Transonic Flow in Small Throat Radius of Curvature Nozzles,"
   *AIAA Journal*, Vol. 7, July 1969, pp. 1375–1378.
6. Cline, M.C., "VNAP2: A Computer Program for Computation of Two-Dimensional, Time-Dependent,
   Compressible, Turbulent Flow," Rept. LA-8872, Los Alamos National Laboratory, Los Alamos, NM,
   Aug. 1981.
7. Zucrow, M.J. and Hoffman, J.D., *Gas Dynamics*, Vols. I and II, John Wiley, New York, NY, 1977.
8. Brown, S., Private communication, Air Force Rocket Propulsion Laboratory, Edwards Air Force
   Base, CA, Sept. 1983.

**Classical nozzle line.** **Rao 1958: PRESENT** (Ref. 1, cited as the definition of the reference
design concept and as the source of "the Rao nozzle design equations", p. 153).
**Guderley: ABSENT. Hantsch: ABSENT. Kraiko: ABSENT. Shmyglevskii: ABSENT.**
**Hoffman's own Route-B papers (Hoffman 1967; Scofield–Hoffman 1971; Johnson–Thompson–Hoffman):
ABSENT** — the author cites only his own *textbook* (Refs. 4 and 7), never his own variational
work. The Russian school appears exactly once, via **Gogish 1966** (Izv. AN SSSR MZhG), and only
as the *originator of the concept being tested and refuted*, not as a variational source.

**Modern adjoint line.** **Lions: ABSENT. Pironneau: ABSENT. Jameson: ABSENT. Giles: ABSENT.
Lozano: ABSENT.** Zero adjoint references, zero optimization references of any kind (no
gradient-based method, no SQP, no design-of-experiments literature). Chronologically unsurprising
for a 1985/87 propulsion paper (Jameson's adjoint aerodynamic design is 1988), but Pironneau 1974
and Lions 1971 predate it, so the absence is a genuine datum and not merely a date effect.

**Net record datum.** A 1987 *Journal of Propulsion and Power* paper on constrained nozzle contour
design, by the principal Western author of the multiplier-field (Route B) formulation, cites the
variational nozzle line only through Rao 1958, cites none of its own author's variational work,
and cites nothing from the adjoint/shape-optimization literature. This is direct bibliographic
support for claim 8 (empty niche) and for P2/G14 (no Rao ↔ adjoint identification in the corpus),
and it should be entered in the litmap as such, query-bounded per claim 20.

## 8. One-line verdict

Hoffman 1987 is **not a variational paper at all**: it is a careful, honest, under-verified
numerical benchmark that measures how much a heuristic construction loses to Rao in a *single
vacuum operating point at constant γ* — 0.04–0.34 % of I_sp, equivalently 25–37 % of the
length-constraint deficit. It is a real THREAT to naive statements about the practical size of the
variational prize *inside the T3 collapse class*, it is CONTAINED in (P) as a one-atom-measure
instance, it CONFIRMS three of our declared gaps (no averaged formulation, no optimizer in the
niche, the Rao construction can fail on a prescribed envelope), and it yields two concrete
adoptions worth executing (the Table 3 γ = const length-and-I_sp oracle, and the CTP universal
feasibility seed for REQ-NONSTALL) plus one cheap instrument (coalescence-based shock-onset
detection as a tier-transition margin).
