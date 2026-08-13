# Expert read — Harroun, Heister & Ruf (JPP 2021), RDRE nozzle performance

**Reader role:** expert reader in a convergence review. Metric of comparison = the
programme apparatus brief (P, T7, T-T3/T-T3-MAP, T-T4, PB-2, EQ-v2, Route A/B, VI.1–VI.6).
**Date of read:** 2026-08-13.

---

## 0. Citation (verified from the PDF itself)

> Harroun, A. J., Heister, S. D., and Ruf, J. H., "Computational and Experimental Study of
> Nozzle Performance for Rotating Detonation Rocket Engines," *Journal of Propulsion and
> Power*, Vol. 37, No. 5, September–October 2021, pp. 660–673.
> https://doi.org/10.2514/1.B38244

Affiliations printed on p. 660: A. J. Harroun (Ph.D. student) and S. D. Heister (Raisbeck
Distinguished Professor, Fellow AIAA), School of Aeronautics and Astronautics, Purdue
University, West Lafayette, Indiana 47907; J. H. Ruf (Aerospace Engineer, ER42, Fluid
Dynamics Branch), NASA Marshall Space Flight Center, Huntsville, Alabama 35812.
Received 7 September 2020; revision received 8 January 2021; accepted for publication
9 February 2021; published online 17 May 2021. Associate Editor: V. Raman (p. 673).
Funding (Acknowledgments, p. 672): NASA Space Technology Research Grant 80NSSC17K0191
and AFOSR contract FA9550-14-1-0029.

## 1. Read coverage

**14 of 14 pages read (pp. 660–673), references [1]–[32] included** (pp. 672–673).
Read twice: once as rendered pages (figures inspected visually), once as extracted text
(full-text string search, used for the misquote adjudication in §5.F4 and the bibliography
census in §6).

Declared limits of the read:
- Numerical values taken off **Figs. 10, 13, 16, 17, 19, 21, 22** are **graphical reads**
  (no data tables are printed for those figures) and are marked as such below. Every number
  reported without that marker is printed as text or in Tables 1–3.
- Ref. [19] (Harroun's own M.S. thesis, Purdue 2019) carries "more details on the solver
  validation study, computational domains and meshes, and solver parameters ... in Chapter 2"
  (p. 665). That chapter is **not** in this PDF and was **not** read here; the solver-validation
  depth of this work is therefore only partly auditable from the paper.
- Ref. [9] (Stechmann Ph.D. dissertation) supplies Table 1's test conditions and Eq. (8)'s
  calibration; not read here.

---

## 2. What the paper actually does

**Problem.** *Not* a design-optimisation problem. It is an **analysis / attribution** problem:
quantify how the high-frequency, high-pressure-ratio unsteady exhaust of a rocket RDE changes
nozzle-and-base-region performance relative to a **constant-pressure engine passing the same
average product mass flow**, so that combustor performance can be isolated from nozzle effects.
Stated aim (p. 661): "The current work aimed to illuminate the flow physics specific to rocket
RDE combustor exit flows for various nozzle geometries."

**Geometries (three, all fixed hardware — no shape is a variable).** (i) A **nozzleless blunt
body** ("inherently unoptimized but ... commonly used in RDE hot-fire experiments", p. 661);
(ii) an **internal–external (IE) aerospike**, cowl + 22.57 deg conical plug, designed by the
**method of characteristics per Denton [18]** at optimal NPR **13.7** (p. 662); (iii) a **flared
aerospike**, same conical plug, cowl designed with the **NASA Aerospike Design and Performance
Tool** [20] for optimal NPR **19.3** (p. 662). Only the cowl differs between (ii) and (iii).

**Formulation (Sec. II.C).** Unsteady RANS, finite volume, NASA **Loci/CHEM**, fully implicit
dual-time, second-order in time and space. Eq. (1) is the integral conservation statement
d/dt ∫Q dV + ∮(F_i − F_v)·n dS = 0 on an arbitrary control volume Ω_c; Eq. (2) gives Q, F_i, F_v
for NS species; Eq. (3) the Newtonian stress tensor with turbulent viscosity μ_t; Eq. (4) the
heat flux q = (λ + μ_t c_p / Pr_t)∇T; Eq. (5) Fickian species diffusion with turbulent Schmidt
number; Eq. (6) the Sutherland form t_i = T^{3/2} F_{τ,i}/(T + G_{τ,i}). Turbulence: **Menter
k-ω BSL** with a **Sarkar\*** compressibility correction [24].

**Unknowns.** The flowfield only (ρ_s, u, e_0, k, ω). **There are no design variables, no
multipliers, no adjoint, no cost functional being differentiated.**

**Constraints.** None in an optimisation sense; only boundary conditions. Far field / quiescent
inlet at P = 1 atm, M = 0.05; outlet at P = 0.998 atm; adiabatic no-slip walls except a short
slip wall at the nozzle inlet; symmetry/centreline (Fig. 8, p. 665).

**Flow model.** **Nonreacting**, ideal-gas EOS, CHEMKIN temperature-dependent properties
(4th-order polynomial c_p; 4th-order fit for λ and μ above 1000 K, Sutherland below). Product
mixture reduced to **two species, 60.5 % H₂O + 39.5 % CO₂**, justified by the trade study of
**Table 2** (p. 667): full 9-species detonation composition vs 5/3/2-species models with
**normalized thrust errors 0.58 % / 0.52 % / 0.28 %** — the 2-species model has the *lowest*
error and was adopted.

**Inflow boundary condition — the cycle model.** Applied one engine diameter upstream of the
channel exit. Two inflows are run: (a) the **detonation-wave** case and (b) an equivalent
**constant-pressure** case "set to a constant pressure that produced the same mass flow as the
detonation-wave case" (p. 665). The detonation waveform is an analytic fit (from Mikoshiba [27],
curve-fitted to CTAP + a NASA CEA detonation calculation [28] at O:F 3.89, 300 K inlet),

  **Eq. (7):  P(θ) = −6.22 ln( (θ/180)·(1/f) ) − 57.04 [atm]**, two waves, f = **13,800 Hz**,

plotted in Fig. 11 (peak ≈ 30 atm at the wave front, decaying to a few atm). Declared inflow
assumptions, verbatim (p. 666): "1) variation was not in the azimuthal direction, and thus the
properties in the radial direction were constant; 2) the gas chemistry was constant; and 3) the
temperature and velocities were constant, and only pressure changed with azimuthal direction and
temporally." (Clause 1 as printed is self-contradictory with clause 3 and with Fig. 11; from
context the intended meaning is *no radial variation*. Flagged as a printing/wording defect, not
re-interpreted silently.) Also stated: inflow temperature fixed at **3400 K** even though "the
unwrapped RDE result showed a complicated, nonuniform temperature profile post-detonation"; and
"**the incoming flow was not rotating and had no vorticity**" (p. 666).

**Solver parameters.** Δt = **0.1 μs**; limit cycle reached in **10–15 wave revolutions**; 3-D
meshes of **30–40 million cells**, y⁺ = 1, wall cell size 4.0E−4 cm; domain ≥ 50 diameters long,
10 wide; 2-D axisymmetric meshes revolved 360 deg with one-degree circumferential cells (p. 665).

**Experiment.** Two campaigns. Stechmann [9] (90 mm annular channel, 10–25 atm mean, CH₄/GOX)
is the *physical basis* of the computation; the **Humble and Lim** campaign [17] (RP-2/GOX, same
architecture, revised hardware with static pressure ports on the expansion surfaces) supplies the
*validation data*. Instrumentation: **CTAP (capillary tube average pressure)** ports — 7 on the
base (Fig. 5, ports ~23 cm, GE UNIK 5000s 0.04 % FS and Druck PMP 1260s 0.25 % FS) and 6 along
the plug (Fig. 6, ports ~30 cm). Kerosene-vs-methane mismatch reconciled by CEA showing γ and
speed of sound "below a 1 % difference" (p. 663).

**Verification / validation.** (i) **Mesh convergence by functional**: Fig. 10 plots relative
error in thrust vs cell count, acceptance criterion "the error in thrust is below 1 %"; the
nozzleless meshes are explicitly declared worse — "The nozzleless meshes had a larger error than
the others due to sensitivity of the mesh to local perturbations; the most resolved mesh was
deemed acceptable to capture these flow physics" (p. 665; graphical read of Fig. 10 puts the two
nozzleless points at ≈ 8–9 % thrust error, vs ≲ 0.5 % for the aerospikes). (ii) **Experimental
validation** of base pressure (Fig. 13, five nozzleless tests) and plug surface pressure
(Fig. 19, tests 69/70/77; Fig. 22, three paired tests, Table 3). (iii) Species-model trade
(Table 2). No grid-convergence index, no temporal-refinement study, no periodicity/limit-cycle
residual certificate is reported.

### 2bis. The cycle-averaging construction they use, and its outcome

This is the reason the paper is on the list, so it is isolated here.

**Three distinct averaging objects appear, and they must not be conflated:**

1. **Averaging as a measurement operator (hardware).** The CTAP configuration "was used to
   eliminate temporal variation in the surface pressure measurements, **such that the
   cycle-averaged surface pressures from the computational study could be directly compared to
   the empirical measurement**" (p. 663). Plus a **windowing protocol** (Fig. 7): the sampling
   region "was windowed to the steady-state operation of the RDE" and the window "excluded the
   transient startup and shutdown of the RDE operation" (p. 663).

2. **Averaging as post-processing of an unsteady solution.** The cycle-averaged surface pressure
   fields of Figs. 13 and 19 are time-averages *of the time-accurate URANS result*. This is a
   *posterior* average; the underlying physics is fully unsteady.

3. **Averaging as a surrogate design/performance model — the one that matters to us.** p. 671:
   "Using Eq. (7) for the detonation wave, a coefficient of thrust could be estimated from
   **averaging the discrete constant-pressure axisymmetric computations for each point in time of
   the cycle**. This **quasi-cycle-averaged** result estimated the coefficient of thrust for both
   the IE and flared aerospike to be **1.25**; thus, the performance with the detonation-wave
   cycle prescribed in Eq. (7) was estimated to be roughly the same for either design."

Object 3 **is our J[Σ] = ∫_Ξ F[Σ; s(ξ)] dμ(ξ)**, built exactly as (P) builds it: a family of
*steady* per-phase evaluations indexed by the cycle phase, integrated against the cycle-time
measure, on a *shared fixed* geometry, with c_F = F/(P_c A_t) (Eq. (10)) as the functional.

**Its outcome is the counter-evidence.** The quasi-cycle-averaged functional returns **the same
value (1.25) for both aerospike designs** — i.e. it is **discrimination-blind**. The paper itself
immediately caveats it: "As these simulations were two-dimensional and averaged, this result
obviously did not account for the difference that a fully three-dimensional detonation-wave
inflow would have on the nozzle performance" (p. 671). And the unsteady 3-D computations and the
**paired experiments do discriminate the two designs** (Fig. 22 and Table 3: three matched
low/mid/high-pressure pairs, cowl swapped between otherwise identical tests): "In all tests, the
IE aerospike's plug maintained a relatively high pressure before rapidly declining after exiting
the cowl (x = 2.5 cm)... Flow separation occurred on the flared aerospike by about x = 5 cm in
the low- and midpressure cases... The IE aerospike, with its smaller area ratio, may thus be the
better design for the chamber pressure (and mass flow rates) tested in the Humble and Lim RDE
campaign" (p. 671).

**The paper's own thesis sentence about averaged models** (Introduction, p. 661, on the prior
Stechmann performance correlations for bell / aerospike / no-nozzle):

> "The performance correlations for these different nozzle designs were based on classical
> constant-pressure ratio models, where the mean specific impulse was found by **mass-averaging
> over the range of pressure ratios in the cycle**; based on the work in the following study,
> **the applicability of these models will be thrown into question**."

**Measure note (numerically load-bearing).** Eq. (7) makes P **linear in ln ξ** (ξ ∝ azimuth/time).
Our Lemma 2 (T-O2) assumes exponential blowdown, P_c(ξ) = P_CJ·PR^{−ξ}, i.e. **ln P linear in ξ**,
whence the log-uniform-in-pressure operating measure dμ_P = dP_c/(P_c ln PR). The two forms are
functional inverses of each other. Inverting Eq. (7) with ξ uniform gives, up to normalisation,
**dμ_P ∝ exp(−P/6.22) dP** — an *exponential-in-pressure* measure, not a log-uniform one. This is
not a contradiction of T-O2 (which is a theorem *given* its blowdown form) but it is a hard datum
that the record empirical RDE waveform does not satisfy T-O2's hypothesis.

## 3. Physics of record extracted

### 3a. Base suction on the nozzleless (blunt-body) configuration

- **Result.** "The surface-area-averaged base pressure for the detonation-wave inflow condition
  was **0.59 atm**, an approximately **eightfold increase in base drag** relative to the base
  pressure of **0.95 atm** of the constant-pressure inflow computation" (pp. 666–667). Confirmed
  by experiment: "Five nozzleless tests of the Humble and Lim RDE campaign that had mass flow
  rates approximately 1 % different from that of the computation had significantly reduced base
  pressures compared to the constant mass flow computation" (p. 667, Fig. 13).
- **Mechanism (ejector / entrainment).** "The high-frequency replenishing of high-momentum gases
  into the plume acted to **continuously entrain fluid out of the base region beyond that seen in
  an equivalent constant-pressure engine**. The period of the detonation-induced pressure wave
  was **faster than the time necessary for the establishment of a steady-state condition in the
  base region**, preventing the base region from adjusting to the ambient condition" (p. 667).
- **Shock structure.** Cyclic oblique→normal shock formation/reformation in the plume over the
  cycle (Fig. 14, t₀ / +25 μs / +50 μs), "unique to the detonation-wave cycle", whereas the
  constant-pressure plume "maintained only a barrel shock that was not replenished with
  high-momentum products like the plume was for the RDE cycle" (Fig. 15) with a lower-frequency
  ≈ 7400 Hz oscillation (p. 667).
- **Analytical model and its failure.** Stechmann's control-volume base-pressure model,
  **Eq. (8): P_b = P_a − ṁ v_t (1 − cos α) / (π r_b²)** (p. 668), "provided adequate predictive
  capability in the midrange of mass flow rates tested; however, for the relatively low or high
  mass flow rates, the base pressures significantly deviated from the model" (Fig. 16, p. 669).
- **Wake-mode transition.** Fig. 17 normalises base pressure by chamber pressure vs NPR:
  "**Open- to closed-wake transition occurs at approximately NPR = 6.7**" (Fig. 17 caption,
  p. 669). In the open-wake regime the RDE base pressures are "significantly lower than ambient
  pressures; thus, the trend of the normalized base pressure in the open-wake regime was below
  the expected one-to-one ratio of a constant-pressure engine" (p. 669). Verdict of record:
  "**Neither the analytical model in Eq. (8) nor the previous theory for the closed-wake regime
  for constant-pressure engine aerospike nozzles are appropriate for predicting base pressures
  with an RDE cycle**" (p. 669).
- **Magnitude of the bookkeeping.** "The base drag must be calibrated out of the thrust
  measurement for accurate evaluation of the combustor contribution, as the typical annular
  topology of RDE chambers makes this correction about a **10 % reduction in thrust**" (p. 661).
- **Contested in the literature.** The result "disagreed with prior CFD simulations by Schwer
  et al. [15] of the base pressure of an airbreathing RDE with a truncated nozzle. These authors
  found that the base pressures did not vary substantially between steady-flow and RDE
  conditions." Reconciliation attributed in a footnote (private communication with Dr. Douglas
  Schwer, NRL, 5 Jan 2021) to "differences in operating conditions and geometries" — lower nozzle
  feed pressure, weaker airbreathing waves, much larger plug surface — "Clearly this is an area
  demanding a more focused study" (p. 667).

### 3b. Delayed separation on the expansion surface

- **Result.** "Around an axial location of **7.0 cm**, the pressure increased in the
  constant-pressure inflow condition due to flow separation. For the detonation-wave case,
  however, the cycle-averaged pressure indicated **the flow was attached until further down the
  plug**" (p. 670, Fig. 19). Not experimentally confirmed: "the pressure measurements in the
  Humble and Lim RDE hardware were not densely located enough downstream to confirm this
  behavior" (p. 670).
- **Mechanism (boundary-layer history / residence time).** Rayleigh-layer argument from
  Stewartson [31]: "For flow impulsively started over a semi-infinite flat plate, the Rayleigh
  layer thickness, a measure of the boundary layer thickness, is proportional to the residence
  time of the flow", **Eq. (9): δ_m = 2 √(μ t_res / (ρ π))** (p. 670). Then: "The high-pressure
  waves reintroduced higher-momentum products into the exhaust plume **every 72 μs**. These
  higher-momentum gases constantly disrupted the normal formation of the boundary layer by
  periodically increasing the shear stress on the viscous sublayer. **The constant reintroduction
  of high-momentum gases by the high-pressure detonation wave thus prevented the boundary layer
  from thickening to a steady-state condition, moving the flow separation point downstream on the
  nozzle**" (p. 670).
- **Separation point is a moving, phase-indexed object.** "From t = 0 μs to t = 25 μs, as the
  detonation wave exhausted over the plug and the incoming pressure decreased, the **flow
  separation point moved upstream** on the nozzle. By t = 50 μs, the next high-pressure peak of
  the detonation wave was exhausting over the plug, **pushing the flow separation point back
  downstream**" (p. 670, Fig. 20). Fig. 18 shows the instantaneous separated region with
  "gray volumes at the end of the plug show[ing] regions of reverse flow (negative axial
  velocity)" and notes "The separated flow region for the RDE had a complex geometry, contrary to
  the axisymmetric separated flow geometry expected for a constant-pressure case" (p. 669).
- **Design consequence claimed (asserted, not proved).** "An RDE nozzle may not be as limited in
  maximum area ratio due to this delay in flow separation, allowing for booster RDEs to have
  higher area ratios and potentially better mission-averaged specific impulse" (p. 672); and the
  trade is explicit — "While this eliminates the pressure thrust enhancement due to pressure
  recovery, eliminating potentially destructive flow-separation-induced structural instabilities
  may have a potential advantage for launch propulsion applications" (p. 670).

### 3c. Cowl / per-surface thrust decomposition

Eq. (10): **c_F = F / (P_c A_t)**, evaluated **separately for the plug and the cowl surfaces**
over the NPR range spanned by the cycle (Fig. 21, from a series of axisymmetric constant-pressure
runs). Graphical read of Fig. 21: the **IE cowl carries a negative c_F** (≈ −0.05 at NPR 9 down to
≈ −0.15 at NPR 30) while the IE plug rises to ≈ +0.32; the flared plug reaches ≈ +0.17 and the
flared cowl stays near ≈ +0.03. Text: "As expected, the cowl surface for the IE aerospike produced
a negative thrust coefficient because of its orientation; however, at the higher pressure ratios
in the cycle, the IE plug produced a much higher pressure thrust than the flared aerospike's plug
surface" (p. 671). Conclusion (p. 672): the flared design "shows to be favorable for future
analysis because of its potential to achieve area ratios beyond that prescribed by an annular
combustor geometry", yet "the flared aerospike was outperformed by the IE aerospike; however, the
engine testing conducted was at relatively low pressure ratios and high ambient pressures."

---

## 4. Hypotheses

**Declared.**
1. Nonreacting flow downstream of the inflow plane: "chemical reactions would be minimal when the
   flow has reached the nozzle" (p. 666) — stated as a judgement, not demonstrated.
2. Frozen 2-species product mixture (60.5 % H₂O / 39.5 % CO₂), justified by Table 2's 0.28 %
   normalized thrust error.
3. Ideal-gas EOS with temperature-dependent c_p, λ, μ (CHEMKIN) — i.e. **thermally perfect,
   calorically imperfect, frozen composition**.
4. Inflow: no radial variation, constant chemistry, constant T and velocity, **pressure only**
   varying azimuthally/temporally (p. 666, clause list quoted above).
5. Uniform inflow T = 3400 K despite an acknowledged nonuniform post-detonation profile (p. 666).
6. **Irrotational, non-rotating inflow**: "the incoming flow was not rotating and had no
   vorticity" (p. 666).
7. Adiabatic no-slip walls — self-flagged: "an adiabatic wall was a significant assumption,
   considering that many rocket RDEs tested thus far and indeed referenced by this study are
   heat-sink cooled; however, the current literature quantifying the heat flux generated by rocket
   RDEs is not mature enough for extrapolation by this study, and so heat loss was omitted for
   simplicity" (p. 665).
8. Analytic logarithmic waveform Eq. (7), two waves at 13,800 Hz, as a stand-in for the real
   detonation structure: "the fine details associated with the detonation wave are not preserved
   by the time the wave interacts with the nozzle and were thus not critical to determining the
   first-order effects on the nozzle" (p. 666) — asserted.
9. Menter BSL k-ω RANS closure with Sarkar\* compressibility correction.
10. Cross-propellant substitution (kerosene experiment vs methane simulation) valid because CEA
    γ and sound speed differ by < 1 % (p. 663).

**Undeclared but necessary.**
a. **That a RANS closure calibrated on statistically stationary flow responds correctly to
   13.8 kHz forcing.** The entire delayed-separation conclusion is a statement about the
   *transient* response of the turbulent boundary layer, made with a two-equation eddy-viscosity
   model and no LES/DNS or downstream experimental confirmation. This is the load-bearing
   unstated hypothesis of §3b.
b. **That grid convergence in integrated thrust certifies base pressure and separation location.**
   The acceptance metric is thrust (Fig. 10); the headline results are a base pressure and a
   separation abscissa. For the nozzleless case, on which the headline 0.59 atm rests, the thrust
   error itself is ≈ 8–9 % (graphical read).
c. **That the twin is fair.** The comparison basis is stated as matched mass flow ("set to a
   constant pressure that produced the same mass flow as the detonation-wave case", p. 665;
   "The average mass flow rates and speeds of sound were identical for both the detonation-wave
   and constant-pressure cases", p. 669), yet the Conclusions restate it as matched mean pressure
   ("a constant-pressure engine operating at the same mean pressure level", p. 672). The matching
   convention is therefore internally inconsistent in wording; the executed convention is
   **matched ṁ**.
d. **Well-posedness of the inflow BC** under a 30 atm wave peak into a nominally 8.6 atm chamber:
   no characteristic-admissibility or choking-margin statement is made anywhere.
e. **Limit-cycle convergence**: "The solution was found to reach limit cycle operation in 10 to
   15 wave revolutions" (p. 664) — no residual, no periodicity error, no sensitivity to that count.
f. **Phase quasi-steadiness + per-phase axisymmetry** for the c_F = 1.25 surrogate (p. 671): the
   per-phase members are 2-D axisymmetric steady solutions. The paper attributes the surrogate's
   failure to the 2-D-ness *and* the averaging in one breath and **does not disentangle the two**.
g. The Stechmann centreline base-pressure measurement "never reached a steady-state value during
   the short 0.9 s window of RDE operation" (p. 668), so Eq. (8) had to be calibrated on
   *preburner-only* warm-oxygen flow, not on RDE flow (p. 662, p. 668).

---

## 5. Three-level comparison with the programme apparatus

### TEORICO

**F1 — THREAT (ALTA) — the phase-average functional is measurably discrimination-blind on this
instance.** *Touches:* our objective J = ∫F[Σ;s(ξ)]dμ as the decision object; T-T3-MAP;
practical value of (P).
*Evidence:* p. 671, "averaging the discrete constant-pressure axisymmetric computations for each
point in time of the cycle. This quasi-cycle-averaged result estimated the coefficient of thrust
for both the IE and flared aerospike to be 1.25" — against Fig. 22 + Table 3, where three paired
experiments and the 3-D unsteady CFD separate the two designs decisively (separation on the flared
plug by x ≈ 5 cm; IE plug holds high pressure to the cowl exit; "the IE aerospike ... may thus be
the better design").
*Reading:* this is the sharpest published attack available on design-on-the-average, and it is
**not** a falsification of T-T3, because the discriminating physics violates **H2'** (fixed wall,
full-flowing, ambient-blind, supersonic exit *every phase*): both discriminators are separated /
recirculating / ambient-coupled. What it *does* threaten is the claim that (P) as posed is the
right decision object **for sea-level RDE hardware**. The programme must therefore carry Harroun
2021 in the T-T3 scope statement as the empirical demonstration that record RDE test articles sit
**outside H2'**, not as a counterexample inside it.

**F2 — THREAT / ADOPT (ALTA) — g_sep is history-dependent, not pointwise-in-phase.** *Touches:*
(P)'s per-phase state constraint "g_sep(S; s(ξ)) ≤ 0 μ-a.e."; D2.3's requirement of a well-defined
steady per-state F.
*Evidence:* Eq. (9) δ_m = 2√(μ t_res/(ρπ)) with the surrounding argument (p. 670): the waves
"reintroduced higher-momentum products into the exhaust plume every 72 μs ... thus prevented the
boundary layer from thickening to a steady-state condition, moving the flow separation point
downstream"; and Fig. 20's separation point migrating upstream then downstream within one cycle.
*Reading:* separation onset depends on the **cycle frequency and the boundary-layer history**, not
on the instantaneous phase state s(ξ). Our (P) writes it pointwise. Two clean repairs, to be
arbitrated: (i) admit a **Strouhal/residence-time admission audit** — quasi-steady g_sep is only
admissible when t_res ≫ 1/f fails to hold, and RDE regimes failing the audit are declared outside
(P)'s scope; or (ii) reparameterise g_sep by (f, t_res). Note the **sign is favourable**: unsteady
forcing *delays* separation, so the pointwise quasi-steady g_sep is **conservative** on this
instance. That gives a defensible interim position — "conservative closure with a named, cited
direction of error" — rather than a defect.

**F3 — GAP-CONFIRMS (ALTA) — the subsonic-patch breaker and the H3-cl failure mode are real, in
hardware.** *Touches:* T-T3-MAP breaker "subsonic patches: J as written is UNDEFINED when
μ(Ξ_sub) > 0"; the two-regime contract; the H3-cl clause ("certified phase-independent closure
patch pattern", expected to fail on migrating patterns).
*Evidence:* the nozzleless base region is subatmospheric and recirculating with cycle-averaged
0.59 atm (p. 667, Figs. 12–13); Fig. 18 shows reverse-flow volumes on the plug; and Fig. 20 /
p. 670 show the **patch boundary migrating within the cycle**. Our H3-cl was declared "expected to
fail on migrating patterns" — this paper exhibits exactly a migrating pattern, measured
computationally and consistent with the experiment.
*Reading:* the two-regime contract is not defensive over-engineering; it is required by the record
hardware. Cite Harroun 2021 as the empirical anchor for μ(Ξ_sub) > 0.

**F4 — CORRECTION (ALTA) — the misquote correction is VERIFIED, and can be strengthened.**
*Touches:* the litmap correction already at registry in
`validation/ADVISORY_rde_choking_2026-08-11.md` (§2-ter), three lit-map lines flagged.
*Evidence:* full-text search of the extracted PDF returns **0 occurrences** of "near-perfect",
"near perfect", "time-averaged expansion", "time averaged expansion" and "perfect expansion".
The phrase **"near-perfect time-averaged expansion" does not exist in this paper.**
*Strengthening:* the paper's actual position is the *opposite* of the misattributed one. Its
Introduction states that mass-averaged constant-pressure-ratio performance models will be "thrown
into question" (p. 661), and its Conclusions state that the base pressure of a nozzleless RDE "was
shown to be poorly predicted with either analytical models or previous empirical results for
constant-pressure engines" (p. 672). **Harroun 2021 must be cited as NEGATIVE evidence against
design-on-the-average, never as positive evidence for time-averaged expansion adequacy.** The
correction of record is confirmed; the registry entry should be upgraded from "phrase absent" to
"phrase absent AND the paper argues the contrary thesis".

**F5 — GAP-CONFIRMS (ALTA) — T-T4's base-pressure breaker is live, and PB-2 has no off-the-shelf
closure.** *Touches:* T-T4 sharpness ("a base-pressure model ... break[s] the nesting"); PB-2.
*Evidence:* Eq. (8) P_b = P_a − ṁ v_t(1 − cos α)/(π r_b²) is the record closed-form closure, and
it is shown inadequate (Fig. 16: deviation at low and high ṁ); Fig. 17's open→closed wake
transition at NPR ≈ 6.7; and the flat verdict on p. 669 that neither Eq. (8) nor the closed-wake
constant-pressure theory ([29] Mueller et al. 1972, [30] Mueller, Sule & Hall 1971) is appropriate
for an RDE cycle.
*Reading:* PB-2 (truncated plug, length cap, base pressure) is therefore **not** a matter of
plugging in a known p_b. Base pressure in the RDE cycle is an open modelling problem *by the
record source*. PB-2 must ship with p_b as a declared bracketed parameter (open-wake
ambient-coupled vs closed-wake chamber-coupled) plus a sensitivity, and must **not** claim a
predictive base-pressure closure.

**F6 — ADOPT (ALTA) — the wake-mode transition is a SWITCH PHASE in the D2.3 sense.**
*Touches:* VI.4/VI.4bis ("locate switch phases ξ*(Σ) ... and SPLIT the Gauss panels there");
D2.3 scope note on mode transitions.
*Evidence:* Fig. 17 caption, "Open- to closed-wake transition occurs at approximately NPR = 6.7",
with the text noting the base region's behaviour is qualitatively different on either side.
*Reading:* since the RDE cycle sweeps NPR from ≈ 2 to ≈ 30 within one period (Fig. 21's abscissa),
a plug/E-D configuration operating across NPR ≈ 6.7 **crosses the wake-mode boundary every cycle**.
That is a genuine ξ\*(Σ) whose location depends on the design. It is exactly the object our panel
splitter exists for, and it is the first *physically named, externally sourced* switch phase in
the programme. Insertion point: VI.4 switch-phase list (alongside separation onset, adaptation,
sheet entry) and the D2.3 μ-null audit — with the caveat that a wake-mode transition may be a mode
transition proper (no steady per-state F on either side of it), in which case D2.3 routes it to the
robust layer instead of averaging it.

### FORMALE

**F7 — GAP-CONFIRMS (ALTA) — zero formal overlap; a strong query-bounded datum for claims 1, 7, 8.**
*Touches:* P2/G14 (Rao = adjoint bridge), D2 gap G3 (no averaged shape theorem), the empty-niche
claim.
*Evidence:* full-text search over the whole paper returns **0** occurrences of "variational",
"adjoint", "Rao", "Guderley", "Hantsch", "Hoffman", "Kraiko", "Shmyglevskii", "Jameson",
"Pironneau", "Lions", "Giles", "Lozano". "Method of characteristics" occurs **exactly once**
(p. 662) and only as the provenance of the hardware contour: "designed using the method of
characteristics per Denton [18]". There is no Lagrangian, no multiplier, no stationarity
condition, no transversality, no free-endpoint condition, no gradient of any functional anywhere
in the paper.
*Reading:* a 2021 JPP paper by the leading rocket-RDE-nozzle group, co-authored with NASA MSFC,
whose entire subject is RDE nozzle design performance, contains **not one object from Route A or
Route B** and cites **not one paper from either the classical variational-nozzle line or the modern
adjoint line**. This does not prove our novelty claims, but it is precisely the kind of
query-bounded evidence they are stated in: the community that owns the application is not using
the machinery, and the machinery's owners are not in its bibliography. Record it against claims 1,
7 and 8 as corroboration, with the standing caveat (claim 20) that corroboration is not proof.

**F8 — ADOPT (MEDIA) — per-surface signed thrust decomposition as a Verdict field and a sector
tiebreaker.** *Touches:* VI.6 Verdict certificate stack; VI.5 sector tournament over topology
sectors (bell / plug / shrouded / E-D).
*Evidence:* Eq. (10) c_F = F/(P_c A_t), reported **separately for plug and cowl** across the cycle's
NPR range (Fig. 21), yielding a **negative cowl c_F** for the IE geometry vs a small positive one
for the flared — the single cleanest discriminator between the two topologies in the whole paper,
and the one the aggregate c_F = 1.25 destroyed by summation.
*Reading:* our Verdict reports J with bars, certificates and multipliers, but not a signed
per-surface decomposition of J. Adding it is nearly free (the Hadamard density G_ξ is already
computed per wall segment) and it is exactly the diagnostic that would have caught the
non-discrimination in F1. Insertion: a `thrust_by_surface` block in the Verdict, and a tiebreak
rule in the sector tournament when two sectors agree on J within the derived band.

**F9 — ADOPT / CORRECTION (MEDIA-ALTA) — an external, published instance of the T3-CONTROL twin,
with a matching-convention slip to avoid.** *Touches:* PROTOCOL T3-CONTROL (mandatory alongside any
decisive cycle-averaged-vs-steady comparison); T-T3-MAP breaker "Pa ≠ 0"; twin fairness.
*Evidence:* the executed convention is matched ṁ (p. 665, p. 669) but the Conclusions restate it as
matched mean pressure (p. 672). The comparison runs at **Pa = 1 atm** (Fig. 8), i.e. squarely in
our named Pa ≠ 0 breaker, and the entire measured discrepancy in the nozzleless case is a
Pa-coupled base term (0.59 vs 0.95 atm against a 1 atm ambient).
*Reading:* (i) this is the first external twin the programme can cite as an *instance* of
T3-CONTROL, and it demonstrates the protocol's necessity — a published paper slipped the matching
convention between its own Methods and its own Conclusions; (ii) our T3-CONTROL wording should
require the matching convention to be stated **in the same sentence as the verdict**, with
Harroun 2021 as the cited precedent for why. Also record: matched-ṁ and matched-⟨p⟩ degenerate
only on the tier-1 + vacuum corner (T-T3-SI); at Pa = 1 atm with a base region they emphatically
do not, which is consistent with, and empirically illustrates, T-T3-MAP's harmonic-mean breaker.

### ALGORITMICO

**F10 — GAP-CONFIRMS / ADOPT (ALTA) — the CycleFamily data contract is missing the cycle
frequency.** *Touches:* VI.1 data contract; VI.2's "separation-criterion hook"; (P)'s "separation
margin, empirical closure".
*Evidence:* Eq. (9) and the 72 μs / 13,800 Hz argument (p. 670) make the separation closure an
explicit function of the **wave frequency** and the flow residence time.
*Reading:* our CycleFamily carries {P0, T0, γ(·;ξ), M_in(y;ξ), θ_in(y;ξ), s(y;ξ), [vorticity]} +
μ weights + provenance + stage-A audits. It carries **no f**. Since the μ measure is a pushforward
of *normalized* cycle time, the physical period is dimensionally erased from the contract — yet the
one closure in (P) that is empirical (g_sep) provably needs it. Concrete change: add `f_cycle`
(and, derived, a Strouhal number against a stated reference length/velocity) to CycleFamily as a
**required** field, and make the separation hook consume it. This is a small, precise, externally
justified contract gap.

**F11 — ADOPT (MEDIA-ALTA) — functional-error species reduction as a table-fidelity rung.**
*Touches:* DIR-THERMOTAB (JAX engines read tables, Cantera as sole production generator, derived
table-density floors); the P1 frozen thermally-perfect pin.
*Evidence:* Table 2 (p. 667): full 9-species detonation composition reduced to 5 / 3 / 2 species
with **normalized error in thrust of 0.58 % / 0.52 % / 0.28 %**, and the 2-species model adopted
because it had the lowest error.
*Reading:* two things worth taking. (i) The **metric**: the error is measured in the *functional*
(thrust), not in a thermodynamic property. Our table-density floors are derived on property error;
a functional-error rung is strictly more relevant to J and is the natural companion to our DWR
bars. (ii) The **rung itself**: our P1 pin fixes a frozen mixture but the programme has no
species-reduction certificate for the table generator. Insertion: the Cantera table-generation
step gains a species-reduction ladder with a pre-registered functional-error acceptance, reported
in the Verdict's provenance block. Caveat to carry: their non-monotone ordering (2 species better
than 3 and 5) is unexplained in the paper and suggests error cancellation, so the rung must be
built with a *bracket*, not a single number.

**F12 — CORRECTION (ALTA) — a citation constraint on the "eightfold base drag" datum.**
*Touches:* how the programme is allowed to cite this paper's headline number.
*Evidence:* p. 665, "The nozzleless meshes had a larger error than the others due to sensitivity
of the mesh to local perturbations; the most resolved mesh was deemed acceptable to capture these
flow physics" (Fig. 10: nozzleless points at ≈ 8–9 % thrust error on a graphical read, vs a stated
< 1 % acceptance criterion met by the aerospikes). Add the contested status vs Schwer et al. [15]
(p. 667).
*Reading:* the 0.59 atm / eightfold figure comes from the *least* grid-converged configuration in
the study and is contradicted by another group on a different (airbreathing) configuration. What
is robustly supported is the **trend** — significantly reduced base pressure under RDE inflow —
because five nozzleless experiments at ~1 % matched mass flow confirm it (Fig. 13). Programme rule:
cite the **trend and the mechanism** as of-record; cite the **number** only with the grid-error and
contested-status caveats attached.

**F13 — ADOPT (MEDIA) — CTAP + windowing as the hardware realisation of our μ, and of our
mode-transition exclusion.** *Touches:* D2.3 (μ = pushforward of normalized cycle time; mode
transitions outside D2.3, routed to the robust layer); oracle O5 (unsteady sim vs J_avg + St·J1).
*Evidence:* p. 663 — CTAP "used to eliminate temporal variation in the surface pressure
measurements, such that the cycle-averaged surface pressures from the computational study could be
directly compared to the empirical measurement"; and the windowing that "excluded the transient
startup and shutdown of the RDE operation" (Fig. 7).
*Reading:* the CTAP is a physical low-pass integrator that *implements* the cycle-average operator
on the wall pressure field, and the windowing *implements* our rule that mode-transition phases are
excluded from μ. This gives O5 an experimental limb it currently lacks: our O5 compares an unsteady
simulation to J_avg + St·J1; Harroun's protocol shows how to compare **hardware** to J_avg, with a
declared exclusion window. Insertion: D2.3's measure section (empirical validation protocol for μ)
and the O5 oracle definition (add an experimental variant with the exclusion window as an explicit
part of the measure's provenance).

---

## 6. Bibliography census (a datum of record)

**32 references, pp. 672–673. Read in full.**

**Classical variational nozzle line — ABSENT, completely.** No Rao, no Guderley, no Hantsch, no
Shmyglevskii, no Hoffman, no Scofield, no Kraiko, no Sirazetdinov, no Nikol'skii, no Rao–Beck.
Zero Russian-school references of any kind.

**Modern adjoint / shape-optimisation line — ABSENT, completely.** No Lions, no Pironneau, no
Jameson, no Giles, no Ulbrich, no Lozano, no Reuther, no Nadarajah. No optimisation reference of
any kind: no SQP, no trust region, no gradient method.

**The only nozzle-contour-design references present** are two grey-literature design tools:
- [18] Denton, B., "Design and Analysis of Rocket Nozzle Contours for Launching Pico-Satellites,"
  M.S. Thesis, Rochester Inst. of Technology, Rochester, NY, 2008 — the MoC source for the IE
  aerospike contour (optimal NPR 13.7).
- [20] Smith, S. D., "Final Report — Aerospike Design and Performance Tool," Plumetech
  PT-FR-01-01, Huntsville, AL, Aug. 2001 — the NASA Aerospike Design and Performance Tool used for
  the flared cowl (optimal NPR 19.3).

**Classical plug base-flow / separation line — PRESENT.** [29] Mueller, T. J., Sule, W. P.,
Fanning, A. E., Giel, T. V., and Galanga, F. L., "Analytical and Experimental Study of Axisymmetric
Truncated Plug Nozzle Flow Fields," NASA N-73-12282, Sept. 1972; [30] Mueller, T. J., Sule, W. P.,
and Hall, C. R., "Characteristics of Separated Flow Regions Within Altitude Compensating Nozzles,"
NASA N-71-18990, Jan. 1971; [31] Stewartson, K., "On the Impulsive Motion of a Flat Plate in a
Viscous Fluid," *QJMAM* 4(2), 1951, pp. 182–198; [32] Sutton & Biblarz, *Rocket Propulsion
Elements*, 7th ed., 2001, pp. 45–101.

**RDE nozzle corpus — dense.** [1]–[17] and [27]: Lu & Braun 2014 JPP; Kindracki et al. 2011 *Shock
Waves*; Stechmann, Heister & Harroun 2019 JSR; Chengwen et al. 2019 *Applied Sciences*; Wang et al.
2019 *Shock Waves*; Goto et al. 2019 JPP; Peng et al. 2018 *Acta Astronautica*; Zhang et al. 2017
IJHE; Stechmann Ph.D. 2019; Ishihara et al. AIAA 2015-0630; Jourdaine et al. 2019 *Proc. Comb.
Inst.*; Fotia et al. 2016 JPP; Fotia et al. AIAA 2019-1743; Braun, Saracoglu & Paniagua 2017 JPP;
Schwer, Kelso & Brophy AIAA 2018-4968; Miki, Paxson, Perkins & Yungster AIAA 2020-3872; Lim,
Humble, Heister AIAA 2020-0195; Mikoshiba Ph.D. 2020.

**Numerics / CFD-verification corpus.** [21]–[26]: Luke et al. (CHEM 2 user guide, and the
chemically reacting solver for generalized grids); Veluri (code verification, Ph.D. 2010); Roy
et al. AIAA 2007-4203 (RANS verification by MMS); Morris & Ruf AIAA 2010-6657 (supersonic film
cooling validation); Luke & Cinnella, *Computers & Fluids* 36(10), 2007 (upwind algorithms for
mixtures). [28] McBride & Gordon, CEA, NASA RP-1311, 1996.

**Interpretation.** The bibliography is a clean partition: applied RDE experiment/CFD plus
CFD-verification methodology, with the classical altitude-compensating-nozzle base-flow literature
retained and the *entire* optimal-contour-design literature — classical and modern alike —
absent. This is corroborating evidence for claims 1, 7 and 8, and it also explains F1: the paper
had no formal machinery with which to *pose* the averaged design question, so it posed and then
discarded a 2-D surrogate.

---

## 7. What the programme must arbitrate (the ask)

1. **Scope of H2', restated with an empirical anchor.** T-T3 is not falsified by this paper, but
   the record RDE test articles it describes are demonstrably **outside H2'** at sea level. Duty:
   the T-T3 scope note must name Harroun 2021 as the empirical demonstration, so the theorem is
   never read as a design licence for sea-level RDE hardware with a base region. *No repair, a
   honesty duty.*
2. **The status of g_sep.** Pointwise-in-phase (as written in (P)) vs history/frequency-dependent
   (as evidenced by Eq. (9) and Fig. 20). Recommended adjudication: keep the pointwise form,
   **declare it conservative** on the RDE instance with Harroun 2021 as the cited direction-of-error,
   and add a Strouhal/residence-time **admission audit** to stage A that fires when quasi-steadiness
   is not defensible. Falsifier: an instance where quasi-steady g_sep is *anti*-conservative.
3. **PB-2's base-pressure closure.** No valid closure exists per the record source (p. 669). PB-2
   must ship with a bracketed p_b and a sensitivity, and must not claim predictivity. Additionally,
   decide whether the open/closed wake transition (NPR ≈ 6.7) is a **switch phase** (splittable,
   μ-null, F continuous) or a **mode transition** (no steady per-state F, routed to the robust
   layer). These have different treatments in D2.3 and the answer is currently undetermined.
4. **The disentanglement experiment the paper did not run.** Harroun attributes the c_F = 1.25
   non-discrimination jointly to 2-D-ness and to averaging, without separating them. This is a
   cheap, decisive, and *externally motivated* controlled experiment for the programme:
   (a) 3-D unsteady, (b) 3-D per-phase steady averaged, (c) 2-D per-phase steady averaged. If (b)
   discriminates and (c) does not, the averaging is exonerated and the dimensional reduction is
   the culprit — which would materially strengthen (P). If (b) also fails to discriminate, the
   phase-average itself is the culprit on ambient-coupled configurations and the two-regime
   contract becomes load-bearing rather than defensive. **This is the single highest-value item
   in this read.**
5. **Litmap registry action (F4).** Upgrade the existing misquote correction from "phrase absent"
   to "phrase absent AND the paper argues the contrary thesis", and re-class Harroun 2021 in the
   litmap as **negative evidence against design-on-the-average**.
6. **Citation constraint (F12).** Record the grid-error and Schwer-contested caveats on the
   eightfold base-drag datum before it is used anywhere in P-1.
7. **Small contract/report changes (F8, F10, F11, F13).** `f_cycle` into CycleFamily;
   `thrust_by_surface` into the Verdict; a functional-error species-reduction rung in the table
   generator; an experimental limb (CTAP + exclusion window) on oracle O5.

## 8. Proved vs asserted (discipline note)

**Demonstrated by data in this paper:** reduced base pressure under RDE inflow (CFD + five
experiments, Fig. 13); the drastic influence of cowl geometry on plug surface pressure (three
paired experiments, Fig. 22 / Table 3); the inadequacy of Eq. (8) at low/high mass flow (Fig. 16);
the open→closed wake transition near NPR ≈ 6.7 (Fig. 17); the species-reduction thrust errors
(Table 2).
**Asserted, computationally suggested but not experimentally confirmed:** delayed flow separation
on the plug (explicitly unconfirmed — "the pressure measurements ... were not densely located
enough downstream to confirm this behavior", p. 670); the Rayleigh-layer/residence-time mechanism
(a scaling argument, Eq. (9), not a measurement); the higher-area-ratio booster implication
(p. 672); the c_F = 1.25 surrogate value (2-D, self-caveated).
**Neither proved nor asserted, simply absent:** any optimality statement, any shape derivative, any
adjoint, any variational formulation.
