# Expert read — Miki, Paxson, Perkins, Yungster: "RDE Nozzle Computational Design Methodology Development and Application"

Reader: convergence-review expert reader. Date of read: 2026-08-13.
File: `literature_review/miki_2020_rde_nozzle_design_methodology.pdf`

---

## 1. Citation (verified FROM the PDF)

Kenji Miki (1), Daniel E. Paxson (2), H. Douglas Perkins (3) — NASA Glenn Research Center,
Cleveland, Ohio 44135; Shaye Yungster (4) — HX5, Fort Walton Beach, FL 32548.
"RDE Nozzle Computational Design Methodology Development and Application."

**Verification caveat of record:** the PDF carries **no venue string, no AIAA paper number, no
year, no DOI and no page range on any of its 16 pages**. The title block gives only title,
authors, affiliations and author footnotes (AIAA member grades, `kenji.miki@nasa.gov`).
Acknowledgments (p.15) state sponsorship by the "National Aeronautics and Space Administration
Space Technology Mission Directorate's Center Innovation Fund program and Game Changing
Development project", and computation on the NASA Advanced Supercomputing Pleiades cluster.
The newest reference in the list is [9] (March 2019) / [25] (July 2019), so a 2020 date is
*consistent* with the content but is **not printed in the document**; the "2020" in our filename
is not PDF-verified. Any bibliography entry we ship must either locate the venue externally or
carry the qualifier "NASA GRC manuscript, undated in the copy of record".

## 2. Read coverage

**16 / 16 pages read** (pp. 1–16, bibliography included: References [1]–[25] on pp. 15–16).
The Read tool returned 16 pages for a 1–20 request, so the document ends at p.16.
NOT read as numbers: the raster figures (Figs. 4, 5–8, 10–16) were read as rendered images —
axis ranges and qualitative shapes are reported, but no digitized values are claimed. All
numeric values quoted below come from Tables 1–4, from in-line text, or from figure axis labels.

## 3. What the paper actually does

**Level verdict: it is NOT a design method. It is a two-domain CFD workflow plus a
five-geometry parametric trade study.** The word "optimization" in the title/abstract denotes
*hand-picked candidate comparison*, not mathematical optimization. There is no design vector, no
objective functional written as such, no constraint set, no gradient, no optimizer, no optimality
condition, and no convergence criterion. The genuine contribution is the **decoupling protocol**
(reusable unsteady inflow BC) and the **experimental validation** against the NPS rig.

| Item | What the paper does |
|---|---|
| **Problem** | Evaluate and compare RDE aerospike exhaust-nozzle geometries; two stated goals (abstract, p.1): (i) validate the computational methodology against experimental data; (ii) "demonstrate how the validated prediction tool can be used to optimize the nozzle geometry". |
| **Formulation** | Domain split into (1) combustor and (2) throat-nozzle section. Q2D in-house reactive quasi-2-D Euler code computes the RDE limit cycle; its unsteady outflow at an axial station **just upstream of the physical throat** is recorded over one full wave transit and replayed as the inflow BC of the 3-D CFD code OpenNCC (Fig. 1, p.3; §III, p.5). No variational statement of any kind. |
| **Unknowns** | Flow fields only. The "design" enters as **six discrete drawn geometries**: NPS baseline (Fig. 2) plus Case 1–5 (Fig. 12, p.11). No parameterization, no DOFs. |
| **Constraints** | None formal. Geometries are fixed engineering drawings with dimensions in inches. Only physical BCs: `P_exit = 14.7 psia`, adiabatic wall. |
| **Flow model** | *Region 1 (Q2D)*: single species, premixed, **calorically perfect gas**, inviscid Euler, quasi-2-D, one-step finite-rate heat release with a reaction-temperature threshold; Roe approximate Riemann solver + MUSCL (2nd order space), explicit 2-step Runge-Kutta; RDE inlet loss models and wall heat transfer imposed via measured manifold conditions and an effective inlet area (p.5). *Region 2 (OpenNCC)*: 3-D unstructured cell-centered finite volume, **viscous, multi-species thermally perfect (H2O/N2/O2), non-reacting** ("chemistry part in OpenNCC is turned off", p.5), AUSM+-up 2nd order with minmod MUSCL, dual-time-stepping with 4-stage RK in pseudo-time, cubic nonlinear k-ε with wall function or LDKM subgrid model (p.5). |
| **Solver** | No optimizer whatsoever. Each case is time-marched to a limit cycle. "Optimization" = ranking six geometries by total thrust (Table 3, p.12). Best = Case 3, "~3.2% improvement over the NPS nozzle due to extending the outer body" (p.13). |
| **Verification** | Validation against NPS rig (Table 2, p.10): MFR 1.56 (exp) vs 1.65 kg/s (CFD); gross thrust 413 vs 483.7 lbf; Isp 120 vs 134 s ("the Isp's differ by about 12 %", p.9); nozzle-surface thrust −4 vs −7.6 lbf. Surface-pressure profile compared qualitatively (Fig. 11, p.10). **No grid-convergence study**: mesh ~600,000 elements, "it was concluded that this mesh is adequate for capturing the basic performance of the nozzle" (p.6) — asserted, not demonstrated. No uncertainty quantification, no error bars anywhere. |
| **Cost** | 240 processors (Xeon E5-2680v2) on Pleiades, "overall computational time is approximately 3 days" per case (p.6); coupled limit-cycle result "within 3-5 calendar days" (p.3). Six configurations + one high-pressure repeat. |

**Operating point** (Table 1, p.4): Pt_in = 131.7 psia, Tt_in = 510 R, P_exit = 14.7 psia,
phi = 0.972, air mass flow 1.51 kg/s. Interface data recorded at Δt = 9.2324E-9 s and Δθ-spacing
0.0008 m (p.5). High-pressure variant (§IV.C, p.13): inflow total pressure scaled ×3.9 with
velocity components and total temperature held fixed.

**What it PROVES vs what it ASSERTS.** It proves nothing in the mathematical sense; it
*measures* (in CFD) and *compares against experiment*. Everything methodological — choking
decoupling, mesh adequacy, chemistry completion at the combustor exit, radial uniformity of the
Q2D profile, the legitimacy of ranking designs whose spread is smaller than the validation error
— is **asserted**.

## 4. Hypotheses

### Declared in the paper
1. Flow is **choked at the throat**, hence nozzle-shape changes do not significantly affect the combustor (p.4, explicit).
2. The Q2D limit cycle has been reached during the recorded window (p.5).
3. Chemistry is **complete at the combustor exit**; the nozzle expansion is chemically **frozen** (p.5).
4. The Q2D single-species CPG state is convertible to a 3-species thermally-perfect mixture (H2O, N2, O2) preserving (P0, T0, u, v, w) (Fig. 1 "Data Conversion" box, p.3; p.5).
5. Detonation-frame → lab-frame conversion of the interface data (Fig. 1, p.3).
6. Adiabatic wall; ambient P_exit = 14.7 psia.
7. The meshed outer-body profile differs from the physical one, justified because "preliminary calculations indicated that the resulting flowfield was hardly changed" (p.4) — declared, unquantified.

### Undeclared but necessary
8. **One-way coupling / zero acoustic feedback.** The interface is placed *upstream of the physical throat*, i.e. in **subsonic** flow (Fig. 1: "Output at axial location just upstream of physical throat"). Choking at the throat does not by itself justify a Dirichlet interface in the subsonic region ahead of it: the full-state BC there numerically *suppresses* the very upstream influence whose absence is being assumed.
9. **Characteristic well-posedness of the interface BC.** Imposing (Pt, Tt, u, v, w, y_i) at a 3-D subsonic inflow boundary over-specifies the incoming characteristics (5 characteristic conditions available, more imposed). Not discussed.
10. **Radial uniformity**: a quasi-2-D (axial×azimuthal) profile is imposed across a genuinely 3-D annular inlet.
11. **Adequacy of the temporal/azimuthal resolution of the replayed BC** (Δt, Δθ above) and of its interpolation onto the OpenNCC boundary — no sensitivity study.
12. **Turbulence-model validity** for an unsteady, shock-containing, separating, wake-dominated flow with wall functions.
13. **Time-periodicity of the nozzle response** to the periodic BC ("Each case was run to a limit cycle", p.8).
14. **Search-space adequacy**: that comparing six drawn geometries identifies "the optimized nozzle" (abstract). No local optimality, no neighbourhood.
15. **Error-hierarchy assumption**: that a validation error of ~12% in Isp / ~17% in gross thrust does not invalidate the ranking of designs separated by 3.2% (468.2 → 499.3 lbf, i.e. a 6.6% total spread). Never stated, and load-bearing for the paper's headline conclusion.
16. **Pressure-only thrust accounting on a viscous field**: the thrust budget (p.8) contains no friction term although wall shear is computed and plotted (Fig. 6(b), p.7).

## 5. Findings — three-level comparison with the apparatus of record

### TEORICO

**T-1 — GAP-CONFIRMS — claim 7 (D2 gap G3: no averaged shape theorem in the corpus). Confidence ALTA.**
NASA states our problem and offers no variational answer. p.2, verbatim: *"The design of a nozzle
for an RDE combustor is somewhat problematic due to the spatially and temporally varying nozzle
inlet flow. **There is no single design pressure ratio for an RDE nozzle that can be used to
determine appropriate area ratios.**"* Their answer (§IV.B, p.10-13) is six drawn geometries
ranked by CFD thrust. There is no measure, no phase family, no stationarity condition, no shared
wall condition, no transversality. This is the *NASA methodology of record* and it contains no
averaged shape theorem — the strongest single piece of GAP evidence in the read corpus for G3.

**T-2 — GAP-CONFIRMS — claim 8 (empty niche) + claim 1 (P2/G14 Rao=adjoint bridge). Confidence ALTA.**
Bibliography [1]–[25] (pp.15-16) contains **zero** entries from the classical variational nozzle
line (no Rao, Guderley, Hantsch, Shmyglevskii, Hoffman, Kraiko, Scofield, Tillyaeva) and **zero**
from the modern adjoint line (no Lions, Pironneau, Jameson, Giles, Lozano). The only
classical-adjacent entry is [6] Hagemann, Immich, Nguyen, Dumnov, "Advanced Rocket Nozzles",
*J. Propulsion and Power* 14, 1998, 620-634 — a review, cited for nozzle *types*, not for
optimality theory; plus [7] Geron et al. (AIAA 2005-5408) and [8] Nasuti & Onofri (ESA SP-487,
2002) on aerospike open/closed wake. Neither the variational formulation nor the adjoint gradient
appears anywhere in the paper. The niche is unoccupied here.

**T-3 — GAP-CONFIRMS — choking advisory (`ADVISORY_rde_choking_2026-08-11`), interface class L4, [T-NSW]. Confidence ALTA.**
p.4, verbatim: *"It is worth mentioning that this approach is based on the **assumption** that the
flow is chocked at the throat. As a result, the change of the nozzle shape should not
significantly affect the combustor characteristics upstream."* [sic, "chocked"]. This is the
advisory's thesis in one sentence, in a NASA-grade paper: choking is an **assumption**, never a
theorem, and it is what buys the reusable-BC architecture ("the unsteady inflow profile can be
repeatedly reused as the inflow boundary condition, when simulating Region 2 with different
nozzle designs", p.4). Our L4 default plus [T-NSW] *prove* under a named margin what NASA assumes
by fiat. Our program's contribution here is exactly the missing certificate.

**T-4 — CONTAINED — mean-swirl panel P1 (flux-nullity THEOREM* + pointwise-nonzero correction). Confidence ALTA.**
p.2, verbatim: *"While there is **no overall net swirl** in the combustor outlet flow, there is
typically a **local tangential component of velocity at each circumferential location**."*
Corroborated by Fig. 4(b), p.6: the v-velocity trace oscillates roughly ±300 m/s about
approximately zero over 0–360°, while Fig. 4(c) shows w ≈ 500–800 m/s. This is precisely our P1
conclusion (net/flux nullity) together with our S21-evening correction (pointwise means are NOT
zero, covariance matters) — **asserted here without proof**, therefore contained as a special
case of our theorem statement, and citable as independent NASA-side corroboration of the swirl
scoping we adopted.

**T-5 — THREAT (bounded, does not falsify) — claims 2/6/7 novelty wording (T-T3 "design at the mean", PB-2 "first genuinely averaged shape problem"). Confidence MEDIA.**
p.10, verbatim: *"Case 3 (Fig. 12(c)) does not have a plug nozzle but is **designed to let the flow
perfectly expand on an averaged basis**."* And Case 3 is the winner: *"Case 3 shows the best
performance with a ~3.2% improvement over the NPS nozzle"* (p.13), Table 3 total 499.3 lbf vs NPS
483.7. So the *phrase* "averaged-basis nozzle design" exists in the RDE literature, applied, and
it wins the trade study. **Why it does not falsify us:** (i) it is a scalar area-ratio sizing rule
from an averaged pressure ratio, not a shape-optimality condition — no measure μ, no phase family,
no functional, no stationarity, no transversality; (ii) it does not distinguish
average-of-optima from optimum-of-averages, which is the entire content of T-T3/T-T4; (iii) its
win is inside the paper's own validation error (see A-3). **Binding consequence for our wording:**
any novelty sentence of the form "designing at the averaged condition is new" is dead; the
defensible form is the one we already use — *no derivation of optimality conditions for a shape
shared across a measure-weighted family*. Add this paper to the named prior-art list beside
Kraiko-Osipov 1970 and ISABE-2003-117, as the *heuristic* averaged-design precedent.

**T-6 — GAP-CONFIRMS — claim 15 (T-GB / M1 geometry-free bound). Confidence MEDIA.**
p.11, verbatim (Case 3 rationale): *"More importantly, by examining only the nozzle interior, it
is possible to **baseline the maximum thrust that could ever be produced by this RDE exit flow**."*
That is an informal ceiling claim — the same *role* our bound ladder plays — but it is (a)
unproven, (b) geometry-dependent (it is one particular drawn geometry), and (c) not even
internally consistent as an upper bound: Table 3 gives Case 4 MOT = 529 lbf > Case 3 MOT = 500.3
lbf. So the corpus wants a ceiling and has none. Our sonic-capped ∫F_id dμ is the object nobody
in this line possesses.

### FORMALE

**F-1 — CONTAINED — claim 18 (containment of the corpus core); f1 thrust integrand. Confidence ALTA.**
p.8 gives the complete thrust bookkeeping explicitly:
`MFR = ∫_{S_exit} ρu ds`, `PRT = ∫_{S_exit} p ds`, `MOT = ∫_{S_exit} ρu² ds`,
`NZT = ∫_{S_n} p n ds`, `OBT = ∫_{S_o} p n ds`, with `n = (1,0,0)`, S_exit the exit area at the
edge of the outer body, S_n the nozzle surface, S_o the outer body. Pressure is gauge (Table 3
shows PRT = −16.5 lbf for Case 3; Fig. 13 column 4 is labelled "Pg"). This is a control-volume
decomposition of exactly our `f1 = [(p − pa) + ρW² sin(φ−θ)cosθ/sinφ] q` with pa absorbed as
gauge and the axisymmetric weight q replaced by the 3-D surface element. **Contained under:**
exit control surface taken as a plane at the outer-body lip rather than a terminal characteristic;
no mass or length integrand (f2, f3) because there is no constrained optimization. **Load-bearing
sub-observation:** although the computation is viscous and wall shear is computed and plotted
(Fig. 6(b), p.7), **no friction term appears in the thrust budget** — the SOTA viscous workflow
still evaluates an *inviscid-form* thrust functional. This strengthens claim 18's scoping
("inviscid-Euler exogenous-measure CORE") rather than threatening it.

**F-2 — THREAT — practical value of contour optimization; pressure on PB-2 / [C-HT4] (base-pressure exclusion). Confidence ALTA on the numbers, MEDIA on the inference.**
The quantity our whole variational machinery optimizes — the pressure integral on the *external*
nozzle contour, NZT — is small and sign-indefinite in a real RDE aerospike. Table 3 (p.12), NZT
[lbf] vs Total [lbf]: NPS −7.6/483.7; Case 1 −11.1/468.2; Case 2 −5.8/491.9; Case 3 +17.5/499.3;
Case 4 −46.5/478.1; Case 5 +35.9/473.7. Table 4 (p.13), high-pressure Case 3: NZT −26.9 of
2496.9 total (≈1.1%). Text, p.8: *"the nozzle shows a slightly negative impact on the thrust"*;
p.12: *"These nozzles deliver a negative net thrust. To minimize such a low-pressure region is
critical while designing a nozzle. it was found to be beneficial to extend an outer body ... to
reduce the low-pressure region"*; p.13: *"For Case 4, as expected, the low-pressure region in the
large wake results in a significant amount of drag (~10% of total thrust)."*
**Caveat that keeps this honest:** their control volume puts all *internal* expansion work into
MOT+PRT at the lip plane, so a small NZT does not mean the internal contour is irrelevant. But
for the **external** plug/spike surface — precisely the Rao/Rao-Beck plug object and precisely our
T-T4/PB-2 object — the measured lever is O(1–10%) of thrust and can be **negative**, while the
dominant, decisive lever in this study is the **base/wake low-pressure region and the outer-body
extension**. Consequence of record: (i) PB-2's base-pressure model is not a refinement but the
main term in this regime, and [C-HT4]'s exclusion of base pressure is a *severe* closure, not a
technicality; (ii) any claimed percentage gain from our contour optimization must be reported
against this measured baseline, or it will read as optimizing a 1% term.

**F-3 — GAP-CONFIRMS — the two-regime interface contract (subsonic-patch closure O1/O2/O3). Confidence ALTA.**
The interface is at "an axial location just upstream of physical throat" (Fig. 1, p.3), i.e. in
**subsonic** flow, and the imposed data is the full state: *"The data file is composed of total
pressure; total temperature; and velocity components and species concentration, at each time
step"* (p.5). Full-state Dirichlet at a subsonic 3-D inflow is characteristically over-determined
and mechanically suppresses upstream influence. This is exactly the case our contract flags as
`μ(Ξ_sub) > 0`, where J as written is UNDEFINED and a declared closure is mandatory. NASA's
resolution is a numerical fiat, not a closure. The gap our contract names is therefore real,
present, and unaddressed at the top of the field.

### ALGORITMICO

**A-1 — GAP-CONFIRMS — claim 8 (empty niche) + the speed programme's value proposition. Confidence ALTA.**
The full "design methodology" is: draw six geometries, run each to a limit cycle, tabulate thrust.
Cost: *"240 processors (Xeon E5-2680v2) of Pleiades ... The overall computational time is
approximately 3 days"* (p.6), plus *"a coupled simulation limit-cycle result could be obtained
within 3-5 calendar days"* (p.3) — order 1.7e4 CPU-hours per **gradient-free** function
evaluation, six evaluations. There is no design vector, no sensitivity, no KKT residual, no
stopping test. This is the structural reason CFD-in-the-loop cannot support certified
optimization at this scale, and it is the concrete SOTA baseline against which our differentiable
fitted march (segment record 5.58 s) and TR-SQP driver should be priced in the paper.

**A-2 — ADOPT — the reusable unsteady-inflow protocol and the measured s(ξ) traces. Confidence ALTA.**
Two adoptable items, both concrete.
(i) *Protocol*: record the combustor outflow over exactly one full wave transit and replay it
frozen across all candidate geometries — *"The duration of data collection is long enough for a
detonation wave to circumferentially travel the combustion chamber once"* (p.5). This is an
executable instance of our **CycleFamily contract (VI.1)** with a named variable list
(P0, T0, u, v, w, y_i) and named resolutions (Δt = 9.2324E-9 s; azimuthal Δ = 0.0008 m). *Where it
plugs*: VI.1 as the minimum interface-file schema for imported data, and VI.6 as the harness shape
for **oracle O5** (unsteady sim vs J_avg + St·J1) — their one-way Q2D→3D chain is the cheapest
existing template for an O5 rig.
(ii) *Data*: Fig. 4 (p.6) is a real, published azimuthal trace of the RDE interface state — P0
sweeping roughly 5e5 → 2e6 Pa, T0 roughly 1400 → 2200 K, w roughly 500 → 800 m/s, u ±400 m/s,
v ±300 m/s over one revolution, with a sharp front near 270°. **Two scoping consequences we must
record**: (a) T0 at this station is strongly non-flat, so a lab-frame azimuthal trace is *not* the
wave-frame T0-flatness test — the monitor must be stated in the wave frame or it will read as
failing on real data; (b) D2.3's log-uniform-in-pressure μ (Lemma 2, exponential blowdown) does
**not** apply to this airbreathing fixed-Pt_in rig — its μ is the (empirical, non-atomic)
pushforward of the Fig. 4 traces, and our measure-agnosticism clause ("switch phases μ-null must
be re-verified for every imported measure") is exactly what such data will exercise.

**A-3 — GAP-CONFIRMS — R5 bar discipline / "nothing ships outside a Verdict". Confidence ALTA.**
The paper's headline design conclusion is ranked **inside its own validation error**. Validation
(Table 2, p.10): gross thrust 413 (exp) vs 483.7 lbf (CFD) = 17% high; Isp 120 vs 134 s, stated as
*"the Isp's differ by about 12 %"* (p.9). Design spread being resolved (Table 3, p.12): 468.2 →
499.3 lbf = 6.6%; the claimed improvement is 3.2%. There is no grid-convergence study (mesh
adequacy is *asserted*: *"it was concluded that this mesh is adequate for capturing the basic
performance of the nozzle"*, p.6), no time-step study, no uncertainty band, and no error bar in
any table or figure. Mass flow itself oscillates ±1.5% (p.8). This is not a criticism we need for
its own sake — it is the calibration of the field's evidentiary bar, and it says our derived-bar /
rejector / Verdict discipline is *above* SOTA rather than merely equal to it. It also means a
future comparison of our optimum against this study must be made on ratios within a single code,
never on absolute thrust.

**A-4 — ADOPT — segmented wall-thrust distribution as a discrete Hadamard-density diagnostic. Confidence MEDIA.**
p.12: *"The domain is divided into twenty segments and the following integration is solved for the
i-th segment, `NZT_i = ∫_{S_n,i} p n ds`. The summation of these thrusts is the gross thrust of the
nozzle."* Rendered in Fig. 14 (p.13) as a per-segment bar chart along the axial coordinate against
the wall gauge-pressure map. This is a cheap, physically interpretable **spatial decomposition of
the wall thrust contribution**, directly comparable with our per-phase wall Hadamard density G_ξ
and with the μ-averaged wall condition T7(b). *Where it plugs*: VI.6 Verdict diagnostics — report
the segmented wall-thrust distribution alongside `∫_Ξ G_ξ dμ + λ_L g_L` so that the reader can see
*which part of the wall* the averaged stationarity condition is trading, and so that our result is
readable in the same picture the NASA community already uses. Low cost, high communication value,
zero rigor risk (it is a diagnostic, never a certificate).

## 6. Bibliography note (record datum)

References [1]–[25], pp. 15–16, inspected in full.

- **Classical variational nozzle line — ABSENT.** No Rao, no Guderley, no Hantsch, no
  Shmyglevskii, no Hoffman, no Kraiko, no Osipov, no Scofield, no Tillyaeva. Nothing on
  maximum-thrust contouring, characteristics-based optimal contours, or multiplier fields.
- **Modern adjoint line — ABSENT.** No Lions, no Pironneau, no Jameson, no Giles, no Ulbrich, no
  Lozano. No adjoint, no shape derivative, no sensitivity analysis of any kind in the reference
  list or the text.
- **Closest classical-adjacent entries**: [6] Hagemann, Immich, Nguyen, Dumnov, "Advanced Rocket
  Nozzles", *J. Propulsion and Power* 14, 1998, 620-634; [7] Geron, Paciorri, Nasuti, Filippo,
  Martelli, "Transition between open and closed wake in 3D linear aerospike nozzles", AIAA
  2005-5408; [8] Nasuti & Onofri, "Prediction of Open and Closed Wake in Plug Nozzles", ESA
  SP-487, 2002. All three are cited for *nozzle phenomenology* (nozzle types, wake closure), never
  for optimality theory.
- **The reference list is overwhelmingly RDE-CFD**: Paxson and co-workers [1]-[5], [15]; Pal [9];
  Tsuboi [10]; Mizener & Lu [11]; Schwer, Kelso, Brophy [12]; Yungster [13]; OpenNCC/NCC numerics
  and combustion [14], [16]-[24]; Lietz LES [25].
- **Transcription caution**: entry [11] is printed as "*Journal of Propulsion and Power*, Vol. 125,
  2017, pp. 1543-1554" — the volume number as printed is implausible for JPP in 2017. Reported as
  printed; do not propagate without checking.

**Record consequence.** The NASA methodology paper for RDE nozzle design cites neither of the two
lines our programme fuses. Combined with the absence of any variational content, this is
first-class evidence for claim 7 (G3), claim 8 (empty niche) and claim 1 (P2/G14): the bridge
Rao-multiplier ↔ continuous adjoint is not merely unstated here, both of its endpoints are
unknown to this literature.

## 7. Novelty vs the 1971 state of the art (HTH-1971 / Hoffman-1967)

**Formulation level: a regression.** Hoffman 1967 (Eq. (78) residual) and HTH-1971 possess a
rigorous variational statement, multiplier fields, adjoint equations sharing the flow
characteristics, derived transversality and an optimality residual. This paper possesses none of
these; it ranks six drawn geometries. Measured against 1971, its *design-method* content is
strictly weaker.

**Physics/verification level: a genuine advance, in directions orthogonal to ours.** It adds
(i) a real, unsteady, azimuthally non-uniform RDE interface state as the actual nozzle inflow —
the physical object our (P) idealizes as the cycle family; (ii) 3-D viscous multi-species
thermally-perfect simulation with separation, wake, shear layers and base drag; (iii) experimental
validation against the NPS rig; (iv) a workflow decoupling (reusable frozen inflow BC) that makes
multi-geometry studies affordable at all.

**Net.** The paper does not advance, contest, or even touch the variational theory. It supplies
the *phenomenology and the cost baseline* against which our programme must argue, and its most
uncomfortable message for us is F-2: in a real RDE aerospike at these conditions, the external
contour pressure integral is a 1–10% sign-indefinite term while base/wake pressure dominates.
That is a scoping obligation, not a refutation.
