# Expert deep-read — Kaemming & Paxson, "Determining the Pressure Gain of Pressure Gain Combustion" (EAP)

Reviewer role: expert reader, convergence review. Metro di confronto: APPARATUS BRIEF (record state) of the
cycle-averaged variational nozzle program.
Date: 2026-08-13.

---

## 1. Citation (verified FROM THE PDF)

Kaemming, Thomas A. (Innovative Scientific Solutions, Inc., Dayton, Ohio, 45459) and Paxson, Daniel E.
(NASA Glenn Research Center, Cleveland, Ohio, 44130), **"Determining the Pressure Gain of Pressure Gain
Combustion"**. 15 pages, 11 numbered figures (Fig. 1–11), 1 table (Table 1), 13 numbered equations
(Eqs. (1)–(13)), 19 references. Acknowledgment to Dr. Doug Schwer (Naval Research Laboratories).

**CITATION CAVEAT OF RECORD.** The supplied PDF carries **no venue line, no paper number, no date** on the
title page, and the file has **no PDF metadata** (`/Title`, `/Author`, `/CreationDate` all absent). The
strings "AIAA 2018-4567" and "NTRS 20180006890" carried in `docs/rde_nozzle_MASTER.md` are therefore
**NOT verifiable from this file**. The only internal dating evidence is the reference list: the most recent
reference is [7] Paxson & Naples, AIAA-2017-1746, January 2017 — consistent with a 2018 paper, not proof of it.
Everything else in this report is page-anchored to the PDF.

## 2. Read coverage

**15 / 15 pages read in full, references included** (Nomenclature p.1; §II Introduction p.2; §III Challenges
p.2; §IV A Representative Pressure p.2–3; §V Ideal EAP Based on Computational Results p.3–8 incl. §V.A
Computational Methods, §V.B Example Calculations, §V.C Non-Axial Momentum, §V.D RDE Geometry Effects,
§V.E Effect of Heat Release; §VI EAP Based on Experimental RDE Results p.9–14 incl. §VI.A–§VI.H;
§VII Conclusions p.14; Acknowledgments p.14; References [1]–[19] pp.14–15).

**Not read / not readable:** nothing textual. Numerical values read off *plotted* figures (Fig. 3, 4, 7, 8, 9,
10, 11) are read to plot resolution and are so flagged wherever used below; where the same number is stated in
running text (e.g. 5.4%, 6%, 3%, 12%, 38%, 1.7–8.7%, ~15%) the **text** is the anchor, not the plot.

---

## 3. What the paper actually does

**Problem.** Not a design problem. It is a **metrology / performance-accounting** problem: PGC devices
(PDE, RDE, wave rotors) produce "dynamic, non-uniform gas flows which are difficult to characterize and
compare with more conventional forms of propulsion" (Abstract, p.1). Direct stagnation-pressure measurement is
"impractical with currently available instrumentation" (p.2) and "it is not obvious that a simple average of
exit total pressure is a meaningful measure of available total pressure" (p.2). The paper proposes a way to
deduce pressure gain from *measurable* quantities.

**Formulation.** Define **Equivalent Available Pressure (EAP)** = "flow stagnation pressure which is
representative of flow's ability to do work or provide thrust" (p.2, attributed to prior work [2]) — i.e. the
uniform steady total pressure that would deliver the same thrust (or turbine work) as the PGC device
"assuming the same mass flow and the same heat addition" (p.2). Two variants:

* **EAP_i** ("ideal", combustor-alone ceiling): flow ideally expanded to ambient P_0, "divorces the EAP from
  the downstream component performance and therefore represents the combustor performance alone" (p.2);
  "analogous to the ideal exit velocity in thrust calculations and ideal spouting velocity in turbine
  performance calculations" (p.2). Computed from full CFD field.
* **EAP** (from measured gross thrust): includes the downstream component's performance; computed from
  experimentally measurable F_g.

**Unknowns.** A single scalar per case: EAP_i (Eq. (8)) or EAP (Eq. (13)). No field unknowns, **no geometric
unknowns, no shape**. Pressure gain is reported as EAP_i/P_t3 − 1 (Fig. 3 label).

**Constraints / reference stations.** SAE / JANNAF guidance: "the PGC combustor must include all hardware
specific to the PGC combustor… any air inlet or air valving should be considered part of the PGC combustor";
the upstream reference is therefore P_t3, the air supplied to the combustor inlet (p.3). Stations: 3 feed
plenum, 3.1 inlet minimum area, 3.2 combustor entrance, 4 combustor exit, 8 nozzle throat (p.1–2).

**Chain of computation, EAP_i (p.3–4).** Stated program: (a) ideal stream thrust per flow segment, (b) sum to
total ideal stream thrust, (c) find the EAP_i that yields that thrust with a uniform flow. Executed as:

* Eq. (1): invert the isentropic function `P_8t,j/P_0 = [1 + ((γ−1)/2) M_ei,j²]^{γ/(γ−1)}` for the ideal exit
  Mach of each CFD exit-plane cell j.
* Eq. (2): `T_ei,j = T_8t,j · [1 + ((γ−2)/2) M_ei,j²]` **(as printed; the "γ−2" is almost certainly a
  typographical error for γ−1 — the isentropic relation requires (γ−1)/2, and Eq. (2) as printed is
  dimensionally fine but thermodynamically wrong. Reported as-printed per the no-invention rule.)**
* Eq. (3): `V_ei,j = M_ei,j · a_ei,j = M_ei,j √(γ g R_g T_ei,j)`.
* Eq. (4): `V_xei,j = √(V_ei,j² − V_8y,j²)` — "resolved into its axial component to derive axial force and
  conserve non-axial energy".
* Eq. (5): `V̄_xei = Σ ρ_j A_x,j V_x,j V_xei,j / Σ ρ_j A_x,j V_x,j` — **mass-flux-averaged** ideal axial exit
  velocity, "directly related to the ideal specific thrust of the device… corresponds to the ideal spouting
  velocity".
* Eq. (6): `T̄_8t = Σ ρ_8j A_8xj V_8xj T_8t,j / Σ ρ_8j A_8xj V_8xj` — mass-flux-averaged total temperature.
* Eq. (7): `T̃_ei = T̄_8t − ½ V̄_xei²/c_p` (baseline: only the AXIAL kinetic energy is credited).
* Eq. (8): `EAP_i = P̄_8ti = P_0 · [T̄_8t / T̃_ei]^{γ/(γ−1)}`.
* Eq. (9) (variant, §V.C): `T̃_ei = T̄_t − ½ V̄_ei²/c_p`, crediting the non-axial energy too.

**Chain of computation, experimental EAP (p.10).**
* Eq. (10): `F_g = P_8 A_8 (1 + γ M_8x²) − P_0 A_8` (the classical stream-thrust form).
* Eq. (11): `P̃_8 = (F_g/A_8 + P_0)/(1 + γ M_8x²)`.
* Eq. (12): same with **M_8x ≡ 1** assumed.
* Eq. (13): `EAP = P̃_t8 = P̃_8 ((γ+1)/2)^{γ/(γ−1)}`.

**Flow model.** Quasi-two-dimensional, **single-species, calorically perfect, premixed** reactive Euler
equations with source terms, integrated in the **detonation frame of reference** so that a time-invariant
(steady-in-frame) solution exists (p.4–5). Source sub-models: two-constant reaction rate (one for detonation,
one for deflagration, calibrated so "approximately 6% of the premixed RDE throughflow reacts" deflagratively,
"the remaining 94% detonates"), skin-friction momentum loss, wall heat transfer (p.4–5). Gas properties of
record: `R_g = 73.92 ft-lb_f/lb_m/R`, `γ = 1.264` (p.4). Baseline case: stoichiometric hydrogen/air, feed
plenum 4 atm, exit 1 atm, feed plenum temperature 540 °R, detonation velocity 6000 ft/sec (p.2, p.5).

**Solver.** Explicit, second-order, two-step Runge–Kutta in time; flux differences with **Roe approximate
Riemann solver** at cell faces; second-order space away from discontinuities via **MUSCL** with slope limiting
(p.5). Grid **200 × 80 uniform**, "deliberately… a course grid (i.e. is diffusive) in order to eliminate the
highest frequency unsteadiness (e.g. detonation cells, Kelvin–Helmholtz phenomena)" (p.4). BCs: periodic in y;
constant-pressure outflow with characteristic equations, imposed pressure disregarded if sonic/supersonic,
extrapolation if supersonic, normal-shock possibility accommodated; partially-open inflow with an
orifice-area (A_3.1/A_3.2) total-pressure-loss model; V_y = 0 prescribed in the lab frame (implemented as
−V_det in the moving frame — "it is here that a reference frame change is implemented"); notional
**check-valve** (solid wall) BC where backflow would occur (p.5).

**Verification.** No grid-convergence study, no formal V&V section. Verification is **cross-methodology
consistency**: (i) EAP-from-F_g vs EAP_i correlation over 28 CFD cases, "typically within 10%" and always
lower (Fig. 9, p.12; §VI.H p.14 gives 1.7% to 8.7% below EAP_i for 25 of 28 cases, "roughly 15% below" for the
remaining low-pressure-ratio cases); (ii) the M_8x = 1 error study (Fig. 7, p.11, "less than 5.4%" over the
typical range); (iii) a comparison of six averaging conventions on one case (Fig. 11, p.13). Sub-models are
said to be "adapted from validated one-dimensional sub-models" [11–13] and calibrated "based on past
validation efforts with experiments [10,14]" (p.4–5). One CFD point (A_3.1/A_3.2 = 0.6, A_8/A_3.2 = 0.6) is
reported **non-converged** — "the mass fluxes and pressures continue to oscillate… It is not known if this is
a CFD numerical issue or an indication of some true RDE flow instabilities" (p.8).

**Headline numbers (text-anchored).** Baseline case: V̄_xei = 5157 ft/sec (1572 m/s); T̄_8t = 3744 °R (2080 K);
T̃_ei = 2577 °R (1432 K); **EAP_i = 87.9 psia (6.0 atm) = +49% pressure gain over the air feed plenum** (p.5).
Table 1 (p.6): P_t3.2/P_t3 max/min/avg 0.85 / 0.64 / 0.74 (29% spread); P_t8/P_t3 4.07 / 0.67 / 1.43 (237%);
T_t8/T_t3 8.07 / 5.37 / 6.57 (41%); **M_8x 1.33 / 0.86 / 0.99 (48%)**. Fig. 2 (p.6): burned-gas total pressure
at station 3.2 spreads up to **93 atm** at the detonation spike, down to ≲16 atm at station 4. Non-axial energy
inclusion: **+6% on EAP_i** (p.7), **+3% on experimental EAP** (p.11). Base drag "nearly 12% of the gross
thrust"; ignoring it "could reduce the EAP pressure-gain… by as much as 38%" (p.9). Fig. 11 (p.13,
plot-resolution): EAP_i ≈ 5.96 atm, EAP-from-F_g ≈ 5.5, area(time)-avg P_t ≈ 5.75, **mass-flux-avg P_t ≈ 7.97,
momentum-flux-avg P_t ≈ 8.63**, CTAP & A/A* ≈ 3.55.

---

## 4. Hypotheses

### 4.1 Declared
1. Thermally and calorically perfect gas, single species, premixed; γ = 1.264, R_g = 73.92 ft-lb_f/lb_m/R
   ("In this example, we use the CFD analysis assumption of a thermally and calorically perfect gas", p.3;
   properties p.4).
2. Quasi-2-D reactive Euler + source terms; detonation frame; converged solution time-invariant in that frame
   (p.4).
3. Grid deliberately coarse/diffusive to suppress detonation cells and KH (p.4).
4. Reaction-rate calibration: ~6% deflagrates, 94% detonates (p.5).
5. **No backflow** — check-valve BC; "these results assume no backflow. For real inlets, the effects of
   backflow may limit the practical extent of A_3.2/A_3.1" (p.5, p.8).
6. Each exit-plane segment expanded **isentropically to ambient P_0** (p.3).
7. Baseline: **non-axial energy is unavailable** — "Because this momentum is not easily recovered, the proposed
   definition of EAP provided here assumes that the non-axial energy is not available" (p.7).
8. Experimental method: **M_8x = 1** (Eq. (12)), justified by Fig. 7.
9. Combustor tested with nozzle convergence but **without divergence**; base forces to be subtracted from the
   balance by direct static-pressure measurement (p.9, Fig. 5).
10. Combustor boundary per SAE/JANNAF: inlet/valving belong to the combustor; upstream reference is P_t3 (p.3).
11. Heat-release study models effective heat release by scaling the fuel heating value, "reflect[ing] only
    global fuel heat release and… not address[ing] mixing or detonation/deflagration percentages" (p.8).
12. Scope caveat: "this proposed method has only been examined for RDE and therefore further study is required
    for additional forms of PGC" (p.9).

### 4.2 Undeclared but necessary
1. **Quasi-steady, streamtube-decoupled expansion.** Eqs. (1)–(4) treat each exit cell as an isolated steady
   1-D streamtube expanding to P_0. No unsteady momentum/energy storage term, no inter-streamtube work, no
   mixing or shear during the expansion, no entropy generation between segments. Nowhere stated, nowhere
   priced.
2. **Exit-plane spatial average in the detonation frame = cycle time average.** Asserted once,
   parenthetically, for the Table-1 "Avg" column — "a simple area weighted average (equivalent to a
   time-average in this frame of reference)" (p.5) — and then relied on throughout. Never proved; requires a
   single pure rotating mode.
3. **Frozen circumferential velocity through the ideal expansion.** Eq. (4) subtracts `V_8y,j` — the *station-8*
   circumferential velocity — from the *fully expanded* total velocity. This silently assumes the swirl
   velocity is unchanged by the expansion. It is **not** an angular-momentum (free-vortex, Γ = rV_θ) model and
   not a radius-aware model. Undeclared.
4. **No sonic cap.** Eq. (1) is inverted for arbitrary P_8t,j/P_0, including sub-critical segments, and full
   expansion to P_0 is taken as the ideal for every segment. That complete expansion to ambient is
   thrust-optimal for a sub-critical streamtube is assumed, not argued.
5. **A single γ, c_p from ~2080 K products down to ambient.** The isentropic chain Eqs. (1)–(3), (7)–(8),
   (13) uses the one CFD γ = 1.264 for the whole expansion. No γ(T) or composition-shift channel exists.
6. **The "equivalent" state is under-determined and only two matches are imposed.** p.2 advertises the
   comparison as "assuming the same mass flow and the same heat addition", but the EAP_i construction matches
   exactly two mass-flux-weighted quantities — ⟨T_t⟩_ṁ (Eq. (6)) and F_ideal/ṁ = V̄_xei (Eq. (5)) — and never
   closes an area–mass-flow relation at the equivalent state. Existence/uniqueness of the equivalent uniform
   state is never discussed.
7. **The mass-flux weights are the actual (unsteady) fluxes.** Eq. (5) weights with ρ_j A_x,j V_x,j; Eq. (6)
   with ρ_8j A_8xj V_8xj. That this is *the* right weight — rather than area, momentum flux, or time — is
   argued only a posteriori by Fig. 11, never derived.
8. **Convexity is never invoked.** The direction of the bias between averaging conventions is documented
   numerically (Fig. 11) and cautioned about verbally ("simple averaging can produce significantly optimistic
   results", p.12), but no Jensen / concavity argument appears anywhere in the paper.
9. **Fig. 7's conservatism is asserted, not proved.** "by assuming Mach 1, the EAP will be smaller than the EAP
   if any other Mach number were assumed" (p.11) is read off a plotted curve for one perfect gas, then used as
   a general property.
10. Ambient P_0 constant and the exhaust quiescent; axial alignment of the reference thrust direction.

---

## 5. Findings — three-level comparison

### TEORICO

**F1 — CONTAINED (confidence ALTA). EAP_i is exactly the pressure coordinate of the axial-only, UNCAPPED
T-GB ceiling; the M0 EAP remark is FAITHFUL on all four of its clauses.**
Evidence. The paper's own program (p.3): "(a) compute the ideal stream thrust for each flow segment
(b) combine all of the flow segments to stream thrusts to obtain a total flow ideal stream thrust (c) compute
an EAPi which would provide the same total ideal stream thrust given a uniform flow", executed by expanding
"each exit-plane flow segment isentropically to ambient pressure, P_0" (p.3). Eq. (5) is literally
`V̄_xei = (Σ ṁ_j V_xei,j)/(Σ ṁ_j) = F_ideal,axial / ṁ`. That is our `J_ideal/ṁ` from [T-GB], with V_id
replaced by its axial projection (Eq. (4)) and with the pressure-thrust term absent because every segment is
fully expanded to P_0. Eq. (8) then re-coordinatizes that specific thrust as a pressure.
Verification of the M0 remark (`docs/rde_nozzle_MASTER.md` ll. 981–999), clause by clause:
(i) *"verbatim from its Eqs. 1-8"* — correct, the EAP_i chain is Eqs. (1)–(8);
(ii) *"each exit segment expanded isentropically to ambient SEPARATELY (expand-then-average, never
mixed-out-then-expand)"* — **CONFIRMED**, p.3 + Eqs. (1)–(4) precede the averages Eqs. (5)–(6);
(iii) *"mass-flux-weighted specific quantities"* — **CONFIRMED**, Eqs. (5), (6);
(iv) *"computed in the detonation frame where 'area average = time average' — i.e. our T0(i) used tacitly as
a fact, proved here as a theorem"* — **CONFIRMED with one precision**: the identity is stated *explicitly*
(p.5, "a simple area weighted average (equivalent to a time-average in this frame of reference)") but
*without proof*, so "tacitly" should read "asserted without proof"; and it is stated for the Table-1 simple
area average, while the EAP_i chain itself uses mass-flux weights over the same exit plane in the same frame;
(v) delta (1) *"+6% variant"* — **CONFIRMED**, §V.C p.7 (Eq. (9)) and §VI.F p.11 (+3% experimental);
(vi) delta (3) *"EAP is the combustor-alone CEILING"* — **CONFIRMED verbatim**, p.2 ("divorces the EAP from
the downstream component performance and therefore represents the combustor performance alone… analogous to
the ideal exit velocity… and ideal spouting velocity").
Containment hypotheses (exact): thermally+calorically perfect single-species gas with one frozen γ;
homentropic per-segment expansion to a constant P_0; segments decoupled; axial projection with frozen V_y;
mass-flux weights; no sonic cap.
Touches: **T-GB / M1**, M0 EAP remark, M0 l. 844.

**F2 — CORRECTION (confidence ALTA). Our own text must carry the "UNCAPPED" qualifier: EAP_i as published is
the naive complete-expansion form that [T-GB]'s own sharpening rejects on sub-critical segments.**
Evidence. Eq. (1) is inverted for arbitrary P_8t,j/P_0 with no branch condition and no cap; the words "sonic",
"critical pressure ratio" and "choked segment" never appear in the EAP_i derivation (p.3–4). Yet Table 1 (p.6)
gives P_t8/P_t3 **min 0.67** and M_8x **min 0.86**, and §VI.H (p.14) explicitly names the failure regime:
"there were CFD cases where EAP was roughly 15% below EAPi. In these cases, the RDE combustors were operating
with small overall pressure ratios (i.e. P_t3/P_0) and/or high loss inlets… which in turn resulted in
substantially subsonic exit Mach numbers (i.e. M_8x ~ 0.5)."
Our record already owns the defect: M0 ll. 845–860, "F_id must be CAPPED AT THE SONIC STATE… executable
counterexample g = 1.15, Pc/Pa = 1.3, dCF = +0.0070", with the naive form rejected by
`tests/test_bounds.py` on four sub-critical Table-1 rows. But M0 l. 844 identifies "axial-only energy variant
= the EAP_i baseline" as a rung of the bound ladder **without the cap qualifier**, and the EAP remark
(ll. 981–999) does not mention the cap at all.
Repair required (R4, same-session class): (a) M0 l. 844 → "axial-only energy variant = the EAP_i baseline,
**uncapped** — hence not a valid ceiling on sub-critical phases, see the sharpening below"; (b) add a delta
(4) to the EAP remark stating that EAP_i inherits the uncapped defect and that K-P's own §VI.H low-PR anomaly
is its empirical shadow. This is simultaneously a **correction we can offer the EAP doctrine**, with an
executable counterexample already in-repo.
Touches: **T-GB / M1**, M0 l. 844, M0 EAP remark.

**F3 — ADOPT (confidence ALTA for the theorem, MEDIA for the full explanation of Fig. 11). The program can
supply the Jensen theorem the paper is missing, and it predicts the sign of their Fig. 11 ordering.**
Evidence. The paper documents, on one case (Fig. 11, p.13, plot resolution): EAP_i ≈ 5.96 atm,
area(time)-avg P_t ≈ 5.75, **mass-flux-avg P_t ≈ 7.97, momentum-flux-avg P_t ≈ 8.63** — a 2.4× spread from
CTAP&A/A* (≈3.55) to momentum-flux average — and comments only that "The CFD mass-flux averaged total pressure
and the CFD momentum-flux average total pressure were significantly higher than EAPi" (p.13), with the general
caution "simple averaging can produce significantly optimistic results" attributed to [2] (p.12). **No
convexity or Jensen argument appears anywhere in the paper.**
The missing theorem, which our apparatus supplies in one line: at fixed T_t, the ideal expansion velocity
`V_id(P_t) = √(2 c_p T_t [1 − (P_0/P_t)^{(γ−1)/γ}])` is **strictly concave increasing in P_t** (with
k = (γ−1)/γ: `u(P_t) = 1 − (P_0/P_t)^k` has `u' = k P_0^k P_t^{−k−1} > 0`, `u'' = −k(k+1) P_0^k P_t^{−k−2} < 0`,
and √· is concave increasing, so the composition is concave). Hence by Jensen, under any fixed weighting,
`⟨V_id(P_t)⟩ ≤ V_id(⟨P_t⟩)`, and since EAP_i is by construction the P_t reproducing `⟨V_id⟩`, we get
**EAP_i ≤ ⟨P_t⟩ under the same weights** — the paper's empirical ordering, as a proved inequality, with the
hypotheses (fixed T_t, common weights) named. The extra spread T_t8/T_t3 = 5.37…8.07 (Table 1) is exactly the
term the fixed-T_t hypothesis excludes, and is where our mixture-form clause (b) `a_eff = ⟨aPc⟩/⟨Pc⟩` takes
over.
Insertion point: M0 EAP remark as a new delta (4) (Jensen direction + hypotheses), and the bound ladder as the
statement "the pressure coordinate of an averaged ideal velocity is a *lower* bound on the correspondingly
weighted mean total pressure". Cite K-P Fig. 11 as the published empirical instance.
Touches: **T-T3-MAP clause (e) conventions/matching**, M0 EAP remark, bound ladder.

**F4 — CONTAINED (confidence ALTA). On the T3 class, EAP's implicit thrust-equivalence definition collapses
EXACTLY onto our ⟨Pc⟩_μ — and T-T3 supplies by THEOREM the shape-independence that EAP_i has only by FIAT.**
Evidence. EAP is defined implicitly, by equating the thrust of a uniform steady flow to that of the device
(p.2, Eqs. (10)–(13) for the measured variant). Our Lemma C gives `F = a[Σ]·Pc − Pa·b[Σ]`, i.e. F **affine in
Pc** on the T3 class; therefore on that class the implicit thrust-equivalence and the arithmetic mean
coincide exactly, and EAP ≡ ⟨Pc⟩_μ with **no Jensen gap**. K-P's own case sits *off* that class: T_t8/T_t3
varies 5.37 → 8.07 (Table 1, p.6), i.e. the phases differ in T_0, violating H3-as-p-only; their EAP is
therefore an instance of the mixture form `J = a_eff⟨Pc⟩ − Pa b` with `a_eff = ⟨aPc⟩/⟨Pc⟩`, not of the
collapsed form.
Second half. EAP_i is nozzle-independent **by definition** — "The latter divorces the EAP from the downstream
component performance" (p.2) — a stipulation. T-T3 proves the corresponding statement: the collapse
`J[Σ] = F[Σ; ⟨Pc⟩_μ]` holds **pointwise on shape space**, so ⟨Pc⟩_μ is shape-independent as a *theorem*. The
paper's own contrast makes the point sharp: the *other* variant, EAP-from-thrust, "includes the performance of
the downstream component, either nozzle or turbine, and therefore does not solely represent the combustor
performance" (p.2) — i.e. it is design-dependent by construction. This is the cleanest available statement of
what our theorem adds to their doctrine, and belongs in P-1 §8.
Touches: **T-T3**, **T-T3-MAP clause (b)**, P-1 §8 EAP bridge.

**F5 — GAP-CONFIRMS (confidence ALTA). No shape problem exists anywhere in the paper; the nozzle contour is
deliberately REMOVED. Confirms D2-gap-G3 and the empty-niche claim on the strongest possible witness — a
2018-era NASA/industry RDE performance paper.**
Evidence. (i) The only "design" exploration is a **two-parameter parametric CFD sweep** of area ratios:
"the RDE inlet area and nozzle throat area were varied in the CFD" (§V.D, p.7, Fig. 3, discrete CFD points
joined by straight segments, one of which is flagged non-converged). No gradient, no optimizer, no
contour DOFs, no constraint qualification, no optimality condition. (ii) For the experimental protocol the
divergent section is *removed on purpose*: "to isolate the combustor performance from the nozzle performance,
the combustor should be tested with the nozzle convergence but without the nozzle divergence" (p.9). (iii) The
Conclusions (p.14) frame the contribution entirely as "A method has been proposed for demonstrating total
pressure gain in a Pressure Gain Combustion (PGC) device."
So the paper poses **the same question as ours** ("what steady equivalent describes this unsteady non-uniform
flow?") but answers it as a *post-processing metric*, and structurally excludes the object our (P) optimizes.
It cannot occupy the D2-G3 niche (no measure-weighted family of inflow states in a shape functional, no
free-boundary counterpart) nor the empty-niche claim (no variational MoC formulation, no optimizer at all).
Touches: **D2 gap G3**, **empty-niche claim**, PB-2.

**F6 — GAP-CONFIRMS (confidence ALTA). Bibliography of record: 19 references, ZERO classical nozzle line,
ZERO modern adjoint line, ZERO optimization references of any kind.**
Evidence, full inspection of [1]–[19] (pp.14–15). All 19 are PGC/RDE/wave-rotor community items, 14 of them
with Paxson as author or co-author: [1] Paxson & Hoke JANNAF 2012 / NASA TM 2013-217826; [2] Paxson &
Kaemming AIAA 2012-0770; [3] Paxson JPP 20(5) 2004 pp.945–947; [4] Paxson AIAA-2014-0284 / NASA TM
2014-216634; [5] Paxson, Fotia, Hoke, Schauer AIAA-2015-1101; [6] Rankin, Fotia, Paxson, Hoke, Schauer
AIAA 2015-0877; [7] Paxson & Naples AIAA-2017-1746; [8] Theuerkauf, Schauer, Anthony, Paxson, Stevens, Hoke
AIAA 2016-1200; [9] Paxson, Brophy, Bruening JANNAF J. Prop. & Energetics 3(1) 2010 pp.44–54; [10] Paxson,
Fotia, Hoke, Schauer AIAA-2015-1101; [11] Perkins et al. AIAA 2005-3831; [12] Paxson, Naples, Hoke, Schauer
AIAA-2011-584; [13] Paxson, Schauer, Hopper AIAA-2009-0502 / NASA TM 2012-217629; [14] Rankin, Fotia, Paxson,
Hoke, Schauer AIAA 2015-0877; [15] Paxson NASA TM 105740, 1992; [16] Paxson AIAA-93-0482; [17] Rankin, Hoke,
Schauer AIAA 2014-1015; [18] Paxson AIAA 2016-1647; [19] Schwer & Kailasanath AIAA 2012-3943.
**Absent: Rao, Guderley, Hantsch, Shmyglevskii, Hoffman, Kraiko, Sirazetdinov, Scofield-Hoffman.
Absent: Lions, Pironneau, Jameson, Giles, Ulbrich, Lozano, Nadarajah — indeed any adjoint or shape-optimization
reference whatsoever.** This is a record datum: the EAP doctrine, which is *the* industry-standard answer to
"what steady state is equivalent to this unsteady flow", was developed in complete bibliographic isolation
from the variational nozzle corpus. It strengthens P2/G14 (nobody in this community is near the
Rao↔adjoint identification) and the empty-niche claim, and it is the citation that makes those novelty bounds
credible to a JPP-class reviewer.
Touches: **P2/G14**, **empty-niche claim**, **novelty-bound discipline (claim 20)**.

### FORMALE

**F7 — CONTAINED (confidence ALTA). Their Eq. (10) is exactly our f1 thrust integrand evaluated on the
degenerate control surface; there is no variational apparatus of any kind in the paper.**
Evidence. Eq. (10), p.10: `F_g = P_8 A_8 (1 + γ M_8x²) − P_0 A_8`. Our Route-A thrust integrand is
`f1 = [(p − p_a) + ρW² sin(φ−θ) cos θ / sin φ] · q`. On a plane exit surface normal to the axis
(φ = π/2, θ = 0) the bracket is `(p − p_a) + ρV_x²`, and with `ρV_x² = γ p M_x²` the integral over the exit
area is `P_8 A_8 (1 + γ M_8x²) − P_0 A_8` — **identically Eq. (10)**. Their thrust functional is therefore the
degenerate, single-surface, flat-exit member of our objective.
What is absent, and must be stated as a record datum: **no Euler–Lagrange system, no augmented density, no
multipliers λ2/λ3, no first integrals, no free-endpoint transversality, no control surface / check contour, no
adjoint field, no Hoffman-E residual analogue**. The nearest structural neighbour of a transversality
condition — the fully-expanded exit condition P_e = P_0 — is imposed as a *definition of "ideal"* (p.3), not
derived as the vanishing of an augmented density at a free endpoint. Route A and Route B are both simply
absent.
Touches: **Route A formal level**, **P2/G14**, **empty-niche claim**.

**F8 — ADOPT (confidence ALTA). Their M_8x = 1 conservatism is a genuine, γ-independent minimality theorem —
they only plot it; we should prove it and adopt it as a certified-conservative reconstruction lemma.**
Evidence. §VI.C, p.10–11: Eq. (12) sets M_8x ≡ 1; Fig. 7 plots `EAP/EAP|M=1` vs assumed M_8x for "Perfect Gas
Uniform Flow Constant F_g/A", showing a minimum of 1.0 at M = 1 and "less than 5.4%" over the typical range
0.8–1.28; the text concludes "by assuming Mach 1, the EAP will be smaller than the EAP if any other Mach
number were assumed. Thus, assuming a uniform exit Mach number of 1 provides an engineering estimated EAP that
is conservative". This is **asserted from a plotted curve**, for one gas, and used as a general property.
It is in fact exactly true, and provable in three lines. With `C := F_g/A_8 + P_0` fixed (Eq. (11)),
`P̃_t(M) = C · (1 + ((γ−1)/2)M²)^{γ/(γ−1)} / (1 + γM²)`. Then
`d ln P̃_t / d(M²) = (γ/2)/(1 + ((γ−1)/2)M²) − γ/(1 + γM²)`, which vanishes iff
`½(1 + γM²) = 1 + ((γ−1)/2)M²`, i.e. iff `M² = 1`; the second-order sign makes it the unique **minimum**,
and the stationary point is **independent of γ** — which is precisely why Fig. 7 shows a single curve.
Adoption. This is a *certified-conservative inversion* device: when the exit Mach distribution is unknown, the
M = 1 reconstruction yields a rigorous lower bound on the equivalent pressure. Insertion points: (i) the
bound ladder in M0, as the experimental-interface rung (a lower bound to pair with the T-GB upper bound —
together they bracket); (ii) the [VI.6] certificate stack, as a reconstruction certificate for any campaign
that must infer a chamber-equivalent pressure from a thrust measurement; (iii) the two-regime contract, where
sub-critical/sonic-cap questions and this M = 1 minimality are the same algebra seen from two sides.
Touches: **bound ladder / M1**, **VI.6 certificate stack**, two-regime contract.

**F9 — CORRECTION (confidence ALTA). M0 l. 691 imports K-P's +6% / +3% as swirl expectations; the numbers are
page-correct but the underlying swirl bookkeeping is a frozen-V_y model, NOT the free-vortex N6-2 model, and
the label is missing.**
Evidence. M0 ll. 690–692 (swirl clause (c)) reads: "recovery asymmetry (Gamma^2/(2 r^2) decays outward,
concentrates inward) signs AGAINST the plug family [per-streamline THEOREM*, N6-2 free-vortex class].
Expectations: +6% EAPi / +3% experimental EAP (K-P pp.7/11)." The two numbers verify exactly — §V.C p.7,
"the inclusion of the non-axial energy in the EAPi calculation resulted in a 6% increase in EAPi"; §VI.F p.11,
"the inclusion of non-axial energy would result in a 3% increase in computed EAP". **But** their model of the
non-axial energy is Eq. (4), `V_xei,j = √(V_ei,j² − V_8y,j²)`, which carries the *station-8* circumferential
velocity unchanged through a full isentropic expansion, and Eq. (9), which credits `½V̄_ei²` in full. Neither
conserves `Γ = r V_θ`; neither is radius-aware; the paper's whole justification is the qualitative "Because
this momentum is not easily recovered" (p.7) plus "Further study is necessary to assess the effect of the
non-axial momentum on available turbine work". Consequently the +6% / +3% bracket is an **upper–lower pair
under a frozen-V_y bookkeeping**, and cannot be read as a free-vortex recovery estimate, which is what its
placement next to the N6-2 clause invites.
Repair required: M0 l. 691 → "Expectations: +6% EAPi / +3% experimental EAP (K-P pp.7/11) — **measured under
K-P's frozen-V_y bookkeeping (their Eqs. (4), (9)), NOT a free-vortex Γ = rV_θ recovery model; a model-mismatch
qualifier, not a transferable N6-2 number**." Also worth adding: the paper's *own* named uncertainty here
("Further study is necessary", p.7) is a GAP-CONFIRMS for our swirl channel being open in the literature too.
Touches: **T-T3-MAP clause (c) swirl**, M0 l. 691, mean-swirl panel.

**F10 — THREAT, mild (confidence MEDIA). EAP is the industry's matched-ṁ / matched-heat-addition steady twin,
stated as such in 2018 and traceable to 2012 [2] — our twin ledger must carry a TWIN-EAP row, and T-T3-MAP
claim 4 must cite it as the standing construction it is arguing about.**
Evidence. p.2: "EAP is directly comparable to uniform flow of a conventional combustor **assuming the same
mass flow and the same heat addition**." That is verbatim the matched-ṁ steady twin whose optimum-equivalence
T-T3-MAP declares FALSE as a general theorem. Two consequences.
(a) *Priority/framing:* the matched-ṁ twin is not a construction we introduce for the purposes of a
counterexample — it is the community's standard comparison basis, standardized under SAE/JANNAF station
guidance (p.3). Claim 4's phrasing must therefore attribute the construction, or a reviewer will read our
refutation as attacking a straw twin.
(b) *A defect in their twin that ours does not have:* despite the "same mass flow" wording, the EAP_i
construction matches only ⟨T_t⟩_ṁ (Eq. (6)) and F_ideal/ṁ (Eq. (5)); no area–mass-flow closure is imposed at
the equivalent state, and existence/uniqueness of that state is never addressed. Our **TWIN-C
flux-consistent** twin is strictly better specified. Recommended action: register **TWIN-EAP** as a named row
in the twin ledger (matched pair = ⟨T_t⟩_ṁ and F_id/ṁ; unmatched = ṁ closure), adjudicate it against TWIN-A
and TWIN-C, and cite it in T-T3-MAP clause (e). This is a THREAT only to *framing and completeness*, not to
the mathematics: nothing in the paper is an optimum-equivalence statement.
Touches: **T-T3-MAP (claim 4)**, TWIN-C / twin ledger, clause (e).

### ALGORITMICO

**F11 — GAP-CONFIRMS (confidence ALTA). Their exit-plane field is a legitimate CycleFamily instance that
FAILS our stage-A L4 admission audit — a page-verified witness that μ(Ξ_sub) > 0 is generic, and a
captured-shock solution our differentiability pin excludes.**
Evidence. (i) *Data-contract fit:* the CFD delivers, on the combustor exit plane, per-cell (P_8t,j, T_8t,j,
V_x,j, V_8y,j, ρ_j) over the full circumference, steady in the detonation frame (p.4–5) — structurally exactly
a `CycleFamily` datum in VI.1, with the frame steadiness playing the role of our T-T0 wave-frame exactness.
(ii) *Audit failure:* Table 1 (p.6) gives M_8x **min 0.86**, avg 0.99, max 1.33; Fig. 6 (p.10) shows the
circumferential M_x trace dipping to ≈0.86 over roughly a third of the annulus for the A_3.1/A_3.2 = 0.6,
A_8/A_3.2 = 0.8 case. The spacelikeness margin `min(M_x − 1)` is therefore **negative on part of the
interface**, so this instance violates the **L4 default class** (every patch axially supersonic with margin) —
`μ(Ξ_sub) > 0`, page-verified. This is the concrete citation supporting M0 ll. 693–704 (which already names
"K-P Table 1/Fig. 6"; **verified correct**) and it makes the two-regime contract load-bearing rather than
defensive. §VI.H (p.14) sharpens it further: at low overall pressure ratio, M_8x ~ 0.5.
(iii) *Differentiability pin:* the solver is Roe + MUSCL with slope limiting (p.5) — **shock capturing**, not
fitting, on a deliberately diffusive 200 × 80 grid. Under our VI.3 pin ("differentiate the fitted front, never
a captured smear", Giles-Ulbrich / Lozano), a solution of this class cannot supply an adjoint gradient in our
pipeline; it is admissible only as *data* (through the stage-A audits and the two-regime route), never as an
inner solve. Worth recording because the RDE community's standard field solvers are all of this class.
Touches: **VI.1 data contract / stage-A audits**, **T-T3-MAP clause (d) subsonic patches**, **VI.3 pin**, L4.

**F12 — ADOPT (confidence ALTA). Their base-force protocol and its measured magnitude are directly usable in
PB-2 and in the T-T4 sharpness clause.**
Evidence. §VI.A, p.9: "With the nozzle divergence removed, there remain significant base areas around the RDE
combustor exit that will contribute axial forces to the thrust balance. Indeed, a previous simulation of an
RDE with this geometry [19 = Schwer & Kailasanath, AIAA 2012-3943] indicated **sub-ambient base pressures**.
Although the integrated base drag results were not presented, it was later found that **the base drag was
nearly 12% of the gross thrust**. Failure to account for this drag when using the method to be described
**could reduce the EAP pressure-gain to be described by as much as 38%**. Therefore, it is recommended that
these base forces be subtracted from the balance readings by **direct measurement of the static pressure
forces acting on the base areas**" — with Fig. 5 showing the recommended annular static-pressure tap layout.
Why we should adopt it. (a) **PB-2** (the truncated plug under a length cap) is defined by exactly this
physics: a base region whose pressure model breaks T-T4's nesting. K-P supply an independent,
detonation-relevant magnitude — base drag ≈ 12% of F_g, sub-ambient base pressure — which is a far better
anchor for PB-2's empirical truncation band than a generic steady-nozzle base-pressure correlation. (b) The
38% sensitivity figure is a *published* demonstration that base-force accounting dominates the reported
performance number — direct support for the T-T4 sharpness clause ("a base-pressure model… break[s] the
nesting; then max∫ < ∫max STRICTLY"). (c) The measurement protocol itself (subtract base forces by direct
static-pressure integration over the base annulus) is the experimental counterpart of our CSTR_PB corner
condition and should be named in the F5/RDE validation plan as the required thrust-balance discipline.
Insertion: PB-2 empirical band + T-T4 sharpness clause in M0, and the F5 experimental protocol in D6.
Touches: **PB-2**, **T-T4 (claim 5)**, CSTR_PB, D6 phase F5.

---

## 6. Bibliography note (mandatory record datum)

19 references, pp.14–15, inspected individually (full list transcribed in F6).

* **Classical variational nozzle line — Rao, Guderley, Hantsch, Shmyglevskii, Hoffman, Kraiko,
  Scofield-Hoffman, Sirazetdinov: NOT CITED. Zero occurrences.**
* **Modern adjoint / shape-optimization line — Lions, Pironneau, Jameson, Giles, Ulbrich, Lozano, Nadarajah:
  NOT CITED. Zero occurrences.**
* No optimization, calculus-of-variations, or design-sensitivity reference of any kind appears.
* The list is a closed PGC/RDE community loop: 14 of 19 items have Paxson as author or co-author; the
  remaining five are Perkins et al. (PDE performance estimation), Rankin et al. ×2 (RDE experiment), Theuerkauf
  et al. (RDE heat flux), Schwer & Kailasanath (RDE exhaust modelling).
* Two self-references carry the doctrinal load: [2] Paxson & Kaemming, AIAA 2012-0770, "Foundational
  Performance Analyses of Pressure Gain Combustion Thermodynamic Benefits for Gas Turbines" — the source of the
  EAP *definition* (p.2) and of the "simple averaging can produce significantly optimistic results" caution
  (p.12); and [1] Paxson & Hoke, JANNAF 2012 / NASA TM 2013-217826, "Time Averaged Pressure Measurement in
  Fundamentally Unsteady Pressure Gain Combustion Systems" — the CTAP instrumentation basis (p.2). Both are
  **named blind spots to be added to our novelty-bound list**: the EAP doctrine's foundational statement is in
  [2], which we have not read, and any priority claim on "equivalent steady pressure" must be bounded against
  it, not against this 2018 paper.

---

## 7. Verdict

The M0 EAP remark (`docs/rde_nozzle_MASTER.md` ll. 981–999) is **FAITHFUL to the paper** on every clause it
makes (F1), as are the two other K-P citations in M0 — the +6%/+3% swirl numbers at l. 691 (pages 7/11
correct) and the sub-critical/closure numbers at ll. 693–704 (Table 1 / Fig. 6 / Fig. 7's 5.4% / §VI.H's
1.7–8.7% and ~15% envelopes, all correct and correctly qualified as *total* envelopes). Two **precision
repairs** are required, both R4 same-session class: the missing **UNCAPPED** qualifier on the EAP_i-as-ceiling
identification (F2) and the missing **frozen-V_y model label** on the swirl expectations (F9). One
**citation caveat** stands: the venue/paper-number string in M0 is not verifiable from the supplied file.

EAP is **not a rival to (P)** — it is a metric, defined by fiat where we prove, and it structurally excludes
the nozzle contour that (P) optimizes (F5). It is, however, the *pressure coordinate of our own ceiling* (F1)
and the community's standing matched-ṁ twin (F10), which makes it the single most important citable bridge in
P-1 §8. The program should take three things from it: the Jensen theorem it is missing and we can supply (F3),
the M = 1 minimality lemma it plots and we can prove (F8), and its base-force protocol and magnitudes for PB-2
(F12).
