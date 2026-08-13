# Expert read — "Theory of an Ideal Jet Thrust Augmentor" (Efremov & Kraiko, 2004)

Read date: 2026-08-13. Reader role: convergence expert-reader, one-to-one comparison against the
programme apparatus brief (`reports/00_APPARATUS_BRIEF.md`).

---

## 0. Citation (verified from the PDF, p. 621 header/title block and p. 632 footer)

N. L. **Efremov** and A. N. **Kraiko**, "Theory of an Ideal Jet Thrust Augmentor",
*Fluid Dynamics*, **Vol. 39, No. 4** (2004), **pp. 621–632**.
Translated from *Izvestiya Rossiiskoi Akademii Nauk, Mekhanika Zhidkosti i Gaza*, No. 4, 2004,
pp. 130–142. Original Russian text © 2004 by Efremov and Kraiko.
Received December 23, 2003. Publisher line: 0015–4628/04/3904–0621, Springer Science+Business Media.
Corresponding e-mail printed on p. 632: `akraiko@ciam.ru`.
Funding printed p. 631: RFBR project No. 02-01-00422; State Program for Support of Leading
Scientific Schools, project No. NSh-2124-2003.1.
Acknowledgements p. 631: V. I. **Bogdanov** and M. M. Tskhovrebov (discussion), G. G. Chernyi (appraisal).

> **CORRECTION OF RECORD (bibliographic).** Our working filename and list entry call this
> "kraiko_tillyaeva_2004". **Tillyaeva is not an author.** The authors are Efremov and Kraiko.
> N. I. Tillyaeva appears only inside references [20] and [21]. The list entry must be re-keyed
> `efremov_kraiko_2004`.

---

## 1. Read coverage

**12 of 12 pages read (pp. 621–632), reference list [1]–[22] included, in a single Read call
(`pages: 1-20`, PDF returned 12 pages).** Nothing skipped.

Declared limitation of the extraction, not of the reading: the PDF text layer **drops most Greek and
script symbols** (ρ, λ, χ, γ, δ, τ, θ, ∞-subscript, Ω/∂Ω render as blanks, "|" or "∘"). Consequently:
- every equation **number** quoted below is printed and verified;
- equation **content** is reported descriptively or with the missing symbols named as reconstructions
  from context, and each such reconstruction is flagged. No symbol is asserted as printed when it was
  not legible.
- Figures 2–4 are line plots; their **captions** are legible and quoted; individual curve values are
  read only to the printed gridlines (1, 3, 5 on the ordinate; 0, 10, 20 on k), so no numeric datum is
  extracted from the curves.

---

## 2. What the paper actually does

### 2.1 Problem
Theory of the **ideal jet thrust augmentor** (ejector-type device): the thrust of a "primary"
high-pressure jet is augmented by entraining a "secondary" low-pressure stream from the flow around
the vehicle. The paper generalises Heiser's ideal augmentor theory (ref. [2], Heiser, Trans. ASME
Ser. A, J. Engng. Power **89**, 75, 1967) in four declared directions, listed verbatim on p. 621:

1. "from the outset we assume that the augmentor flow is **time-dependent and periodic**; the period
   τ is taken for the time scale (the steady augmentor is a particular case of the periodic augmentor
   with an arbitrary finite period)";
2. "the ideal augmentor is considered to be a device providing a **maximum period-average thrust R**
   at fixed values of the mass fluxes of the primary (mᵖ) and secondary (mˢ) gases and the total
   enthalpy at the device inlets during the period, as well as fixed inlet entropies";
3. exit pressures are **not assumed** constant nor equal to ambient — that is derived;
4. "the optimum exit parameters of both flows are determined as **necessary conditions** for maximum
   R from the solution of a variational problem with **four isoperimetric conditions**";
   plus the genuinely new physical ingredient, **heat transfer q** between the two streams (in [2]
   only work exchange w was allowed).

The primary source is explicitly allowed to be a **pulsed detonation rocket engine** (p. 622), which
is why the paper is in our list.

### 2.2 Formulation
- Control volume Ω bounded by ∂Ω with two inlets and two exits (Fig. 1, p. 622); the two gases do
  **not mix**, separated by a "weightless, impermeable, and, in general, deformable (on the interval
  *ab* in Fig. 1), that is, time-dependent surface" (p. 622).
- Integral mass and energy conservation for each stream, Eqs. **(1.1)** (p. 623), with source terms
  ∓2(w+q): w the power of an ideal (lossless) turbine/compressor, q the heat transferred from primary
  to secondary.
- Periodicity + scaling on τ ⇒ period-integrated forms Eqs. **(1.2)**, **(1.3)** (p. 623), defining
  the constants mᵖ·ˢ, Cᵖ·ˢ = 2mᵖ·ˢ⟨H_iᵖ·ˢ⟩, W = period work, Q = period heat.
- Exit planes normal to x, flow there **uniform and parallel to x** (p. 624). Then the constraints
  become the four **isoperimetric** conditions **(1.4)** (mass) and **(1.5)** (energy), one per stream.
- x-momentum integral **(1.6)** and, after dropping fixed inlet-momentum and drag terms "correct to
  constant summands inessential for our purposes", the objective **(1.7)**:
  R = ∫₀¹ [ (p_eᵖ − p_a + ρ_e V_e^{p2}) F_eᵖ + (p_eˢ − p_a + ρ_e V_e^{s2}) F_eˢ ] dt − mˢ V_∞
  (Greek/subscript symbols reconstructed; the structure (p_e − p_a) + ρV² per stream, minus mˢV_∞, is
  legible).
- EOS in the general two-function form **(1.8)** ρ = ρ(p,s), h = h(p,s), with the thermodynamic
  identities **(1.9)** h_p = 1/ρ, h_s = T, ρ_p = 1/a². **No perfect-gas assumption at this stage.**

### 2.3 Unknowns
Stated on p. 625: "the states of the primary and secondary flows in their exit sections and, hence,
the optimized parameter R are determined by the values of **eight parameters Fᵖ·ˢ, Vᵖ·ˢ, pᵖ·ˢ, and
sᵖ·ˢ**. These are, generally, **time-dependent functions**" — plus the two scalars **W and Q**,
"unknown beforehand". So: 8 scalar functions of t on [0,1] + 2 scalars. **No shape, no contour, no
field.**

### 2.4 Constraints
Four isoperimetric integral conditions (1.4)–(1.5) (mass and energy, per stream), the EOS (1.8), and
a **second-law side condition**, stated but not formalised: "As for the entropy variations δsᵖ and
δsˢ, these cannot be regarded as independent, if only because in the absence of heat exchange between
the thrust augmentor and the surroundings, the total entropy flux across the exit sections cannot be
less than that across the inlet sections" (p. 625).

### 2.5 Flow model
Integral (control-volume) conservation only. Gases "ideal (inviscid and non-heat-conducting)" except
for the admitted inter-stream heat exchange (p. 623). **No differential equations of motion are ever
written.** Inlet flows may be non-uniform in every parameter except entropy and (secondary) total
enthalpy. Exit flows uniform, axial. Shocks appear only rhetorically: p. 628, "the entropy is no
longer able to increase in the weak shock waves which are almost inevitable in unsteady flows".

### 2.6 Solver
Purely analytical. Lagrange functional (p. 625)
J = R + λ₁ᵖL₁ᵖ + λ₁ˢL₁ˢ + λ₂ᵖL₂ᵖ + λ₂ˢL₂ˢ, with "**constant** Lagrange multipliers λ^{p,s}_{1,2} …
as yet undetermined". First variation **(2.1)** with coefficient blocks A_F, A_V, A_p, A_s given in
closed EOS-general form. Setting the coefficients of δFᵖ, δVᵖ, δpᵖ to zero gives **(2.2)–(2.4)**;
eliminating λ₁ᵖ gives **(2.5)**, hence

- **(2.6)** p_eᵖ = p_a  (exit pressure equals ambient, at every instant)
- **(2.7)** 1 + 2λ₂ˢV_eˢ = 0 and p_eˢ = p_a
- **(2.8)** λ₂ˢ = λ₂ᵖ = λ₂
- **(2.9)** V_eˢ = V_eᵖ = V_e  (equal exit velocities of the two streams)
- **(2.10)** R (the residual first variation) = −∫₀¹ (ρᵖFᵖTᵖ δsᵖ + ρˢFˢTˢ δsˢ)_e dt
- **(2.11)** s_e = s_i per stream when Q = 0 (isentropy is *derived*, not assumed)
- **(2.13)** V_e = V_ai^p·√(1+k·ν)/√(1+k), k = mˢ/mᵖ (the symbol for ν is dropped by the text layer;
  it is defined in the same display as 2(H_iˢ − h_aiˢ)/V_ai^{p2})
- **(2.14)** the augmentation coefficient χ = √(1+k)·√(1+k·θ∞) − k·√θ∞, with the printed definition
  θ∞ = (V_∞/V_ai^p)² (Greek names reconstructed; the algebraic form and the definition are legible)
- with heat transfer: the optimality condition **(2.15)** T_eᵖ/T_qᵖ = T_eˢ/T_qˢ, its equal-temperature
  realisation **(2.16)**, and the re-derived set **(2.17)** giving the larger coefficient χ_q.

§3 (pp. 628–630) "PROCEDURE AND RESULTS OF THE CALCULATIONS" restricts to a **perfect gas** and
evaluates explicit sequential closed-form formulas; Figs. 2–4 are parameter sweeps in k.
Printed settings: γˢ = γᵖ = γ = 1.4, c = c_pˢ/c_pᵖ = 1; Fig. 2 caption "n = 5, 10, and 20 … M∞ = 0,
r = 0.5"; Fig. 3 caption "n = 5, r = 0.5; curves 1 to 4 relate to M∞ = 0, 0.5, 1.0, and 1.5";
Fig. 4 caption "r = 0.125, 0.25, 0.5, 1, and 2 … M∞ = 0, n = 5".

### 2.7 Verification
No CFD, no experiment, no independent code. The checks that exist are:
(i) **reduction to the prior theory** — with Q = 0 the results collapse onto ref. [2] (Heiser 1967),
stated p. 626 ("If we assume, as in [2], that the primary and secondary flows do not exchange heat
(Q = 0) …");
(ii) **analytic limits** — the k → ∞ asymptotics for χ and χ_q printed on p. 631, and the take-off
limit χ → ½(√θ∞ + 1/√θ∞) as k → ∞ printed on p. 627 (symbol reconstructed);
(iii) **sign/operability bounds** — "χ > 1 only when 0 < k < …" (p. 627).
**Sufficiency is never examined**: the paper says "necessary conditions for an extremum" (pp. 621,
625). No second variation, no existence proof.

---

## 3. Hypotheses

### 3.1 Declared
H1. Periodic flow with a single period τ established throughout the augmentor; steady flow is the
    degenerate case (p. 621).
H2. mᵖ, mᵖ⟨H_iᵖ⟩, s_iᵖ preassigned and s_iᵖ time-independent (p. 622).
H3. mˢ, H_iˢ = H_∞, s_iˢ = s_∞ preassigned; requires "the absence of unsteady disturbances at the
    inlet of the 'ideal' low-pressure gas intake" if the flow is time-dependent and the oncoming flow
    subsonic (p. 622).
H4. **No mixing**, enforced by a weightless, impermeable, deformable, time-dependent separating
    surface (p. 622).
H5. Gases ideal (inviscid, non-heat-conducting) **except** for the admitted inter-stream heat
    exchange q (p. 623).
H6. Uniform, axial exit flow in plane sections normal to x (p. 624).
H7. Ideal (lossless) turbine and compressor; "the work done by the motion of their walls is assumed to
    be negligibly small" for the duct walls (p. 623).
H8. Secondary intake with **isentropic and isoenergetic** deceleration (p. 627).
H9. Primary inlet momentum flux constant and therefore droppable; secondary inlet momentum flux
    = mˢV_∞ in the "design inflow regime" (p. 624).
H10. Total exit entropy flux ≥ total inlet entropy flux (second law, invoked qualitatively, p. 625).
H11. §3 only: perfect gas, γ = 1.4, c = 1.

### 3.2 Undeclared but necessary
U1. **Realisability.** The variations δFᵖ·ˢ(t), δVᵖ·ˢ(t), δpᵖ·ˢ(t) are treated as free and mutually
    independent pointwise in t. Nothing guarantees that an admissible exit-state history is producible
    by *any* internal duct/nozzle flow. The whole theory is therefore an **upper-bound (ideal-limit)
    construction**, and the paper never says so in those words.
U2. Existence and attainment of the maximum; the multipliers are assumed to exist and be finite.
U3. Interchange of variation and time integration in passing from (1.7) to (2.1).
U4. The entropy-variation coupling is handled by *argument*, not by an explicit multiplier or an
    inequality-constrained KKT system — so (2.10)→(2.11) is an assertion supported by a monotonicity
    argument ("possible entropy increments … are positive with the result that … the thrust augmenter
    efficiency is reduced"), not a proof.
U5. Achievability of the equal-temperature heat-transfer limit: "ideally the temperature difference
    can be made as small as desired (for example, by steady acceleration of the hot gas)" (p. 628) —
    asserted, not demonstrated.
U6. Smoothness in t of the optimal histories; no switching/non-smooth phases are considered.
U7. Neglect of shock-generated entropy in the unsteady case is argued away, not bounded (p. 628).
U8. The dropped "constant summands" in (1.6)→(1.7) (drag, primary intake momentum) are assumed
    design-independent.

---

## 4. Three-level comparison with the programme apparatus

### 4.1 THEORETICAL

**F1 — THREAT (to the *unqualified* wording of PB-2 / D2-G3; ALTA).**
This is a **published, Kraiko-authored, cycle-averaged variational maximum-thrust problem**. Abstract
p. 621: "The conditions of optimal outflow … are obtained by **solving the variational problem of
maximum average thrust realization**"; intro p. 621: "a device providing a **maximum period-average
thrust R** at fixed values of the mass fluxes …"; objective Eq. (1.7) is literally ∫₀¹(…)dt with the
period scaled to 1, i.e. our μ = normalized cycle time (D2.3 default measure) *verbatim*. It appears
one year after ISABE-2003-117 and cites it. Consequence: any phrasing of PB-2 or of the programme
narrative that reads "the first averaged variational thrust problem" is **false**; the surviving,
defensible statement is the *shape* statement — "the first genuinely averaged **shape** problem" —
and it must never be shortened. Note also that ours is a **cycle** measure over a rotating-wave
interface; theirs is a period measure over device-level exit states.

**F2 — GAP-CONFIRMS (D2 gap G3, claim 7; ALTA).**
The same paper is the strongest available evidence that G3 is real: a maximum-*average*-thrust
variational problem written by the head of the Kraiko school contains **no shape, no contour, no
PDE constraint, no Hadamard derivative and no non-uniform measure**. The unknown list is printed
(p. 625): "eight parameters Fᵖ·ˢ, Vᵖ·ˢ, pᵖ·ˢ, and sᵖ·ˢ … time-dependent functions", plus W and Q. If
an averaged *shape* theorem existed in this school in 2004, this is the paper that would have cited
it; it does not exist here.

**F3 — CONTAINED (in the T7 skeleton, under named hypotheses; ALTA).**
Their whole optimality system is the **degenerate limb of T7 in which the shared design is empty**:
constraints purely isoperimetric ⇒ multipliers **constant** across the family ⇒ stationarity holds
**pointwise in the phase variable**. Exactly our T7(a)+(c) with T7(b) (the shared-wall averaged
condition) vacuous, because nothing is shared across phases except the scalars λ₁, λ₂, W, Q.
Exact hypotheses for the containment: design variables free per phase; constraints integral only;
μ = normalized time; objective affine in the per-phase state through (1.7).
Their collapse result — "**the stationary nature of the ideal augmentor flow is a result of the
formulation of the problem in which the flow rates of both active and passive gases are preassigned**"
(Summary, p. 631), supported by p. 627 "Since there are no additional constraints on the exit areas,
it is natural to make the areas Fᵖ·ˢ constant (time-independent) … The constancy of Fᵖ·ˢ renders it
unnecessary to use adjustable exhaust nozzles with deformable walls" and p. 628 "Since the solution
shows that the flows at the augmentor exit are steady, the moving surface should be abandoned in
favor of an ideal … turbine and a compressor" — is a **collapse theorem of the T-T3 family obtained
under a different hypothesis set** (period-integrated fluxes fixed; exit areas unconstrained). It
does **not** threaten T-T3, whose content is a *pointwise-on-shape-space* identity for a *fixed wall*
under H1–H4/H2′; it does supply an independent corpus precedent that "unsteady-periodic optimum ⇒
steady design" is a known phenomenon, which our novelty framing must acknowledge.

**F4 — ADOPT (T-T3-MAP: register a third corner; MEDIA).**
T-T3-MAP currently proves "cycle-averaged optimum = matched-ṁ steady optimum" only on the
tier-1 + **vacuum** corner, with p_a ≠ 0 listed as a breaker. This paper exhibits a corner where the
collapse survives **p_a ≠ 0 and V_∞ ≠ 0**: Eq. (1.7) carries (p_e − p_a) and −mˢV_∞ explicitly, and
the optimum satisfies Eq. (2.6) p_eᵖ = p_a, Eq. (2.7) p_eˢ = p_a, yet the optimal design is
time-independent. The reason is consistent with our own breaker statement and should be written into
T-T3-MAP as the discriminant: the p_a breaker bites on **average-of-ratios Isp**, not on **thrust at
preassigned period-integrated mass flux**. Recommended new named corner: *"free exit area +
preassigned period-integrated (ṁ, H₀) ⇒ collapse survives p_a ≠ 0, objective = thrust not Isp"*,
citing Efremov–Kraiko (2004) Eqs. (1.7), (2.6)–(2.9), Summary p. 631.

**F5 — THREAT, scope-conditional (claim 18, containment; BASSA).**
Claim 18 is bounded to "variational maximum-thrust **nozzle** formulations", and this is an
augmentor/ejector, so it is formally out of scope. But if the containment claim is ever widened to
"Kraiko's thrust-optimisation corpus", this paper is a **third structural non-containment**, on two
counts not expressible in (P): (i) the inter-stream **work and heat exchange** scalars W and Q enter
the functional as free optimisation variables (Eqs. (1.3), (1.5), (2.15)–(2.17)); (ii) the second-law
**inequality** on total exit entropy flux acts as a side constraint (p. 625). Action: state the scope
boundary explicitly in the litmap rather than leave it implicit.

### 4.2 FORMAL

**F6 — CONTAINED (Route A corner condition CSTR_PA at θ_E = 0; ALTA).**
Their Eq. **(2.6)** p_eᵖ = p_a and Eq. **(2.7)** p_eˢ = p_a are **exactly our CSTR_PA restricted to
zero exit flow angle**. Our transversality reads p_a = p − ½ρW² sin(2θ) tan α; their exit hypothesis
is printed on p. 624 — "the exit sections of both gases are planes normal to the x axis … and in
these sections the flows are **uniform and parallel to the x axis**" — i.e. θ_E = 0, whence
sin(2θ_E) = 0 and the condition degenerates to p = p_a. The classical Rao corner condition and the
Efremov–Kraiko ideal-adaptation condition are therefore the **same free-endpoint transversality**,
evaluated on a one-dimensional exit. This is a clean containment datum for Route A.

**F7 — CONTAINED (shared mass multiplier ↔ the f2 = −λ₂ first integral; MEDIA).**
Their structure is: one **constant** mass multiplier per stream on the isoperimetric mass condition,
Eq. (2.5b) 1 + 2λ₂ᵖV_eᵖ = 0 and Eq. (2.7) 1 + 2λ₂ˢV_eˢ = 0, then Eq. (2.8) λ₂ˢ = λ₂ᵖ = λ₂, hence
Eq. (2.9) V_eˢ = V_eᵖ = V_e. That is: **a single mass multiplier pins the exit velocity across the
whole family (both streams, all instants)** — the finite-dimensional shadow of our Route-A first
integral f2 := W cos(θ∓α)/cos α = −λ₂ held constant along the terminal characteristic, and of T7's
principle that the phases are coupled *only* through shared multipliers. Caveat of record: the
numerical factor 2 comes from their energy normalisation (2h + V²) in (1.3)/(1.5); the analogy is
structural, not a term-by-term identity.

**F8 — ADOPT (entropy-debit thrust identity as a new bound-ladder rung / certificate; ALTA).**
Equation **(2.10)** (p. 626) is, printed:
R = −∫₀¹ (ρᵖFᵖTᵖ δsᵖ + ρˢFˢTˢ δsˢ)_e dt
i.e. **the residual first variation of period-average thrust is the exit-plane entropy increment
weighted by ρ·F·T**. It is derived from the *general* EOS pair (1.8) with (1.9) h_s = T, h_p = 1/ρ —
therefore **EOS-general**, exactly the posture our E4 claim asserts for the stationarity system.
What to adopt and where:
- **M0 bound ladder (T-GB / mechanism M1)**: add an **entropy-debit rung**
  B_S = B_isentropic − ∫ ρ_e F_e T_e Δs_e dμ. It prices, in thrust units and at first order, every
  irreversibility the design admits (fitted or captured fronts, detonation-product entropy spread),
  and it is geometry-free, hence usable exactly like our sonic-capped J_ideal.
- **VI.6 certificate stack**: report Δs-debit alongside the Hoffman-E residual. The Hoffman-E residual
  certifies *stationarity*; the ρFT·Δs debit certifies *how much thrust the entropy budget is
  costing*, which is the quantity the RDE cycle actually spends.
- It also gives a principled statement of *why* a captured smear is penalised twice (adjoint
  inconsistency + priced entropy), reinforcing our Giles–Ulbrich/Lozano fitted-front pin.

**F9 — GAP-CONFIRMS (claim 1, P2/G14: Rao ≡ adjoint bridge; ALTA).**
Zero adjoint content. The only optimisation machinery is, verbatim p. 625, "we set up the **Lagrange
functional** J = R + λ₁ᵖL₁ᵖ + λ₁ˢL₁ˢ + λ₂ᵖL₂ᵖ + λ₂ˢL₂ˢ where the **constant** Lagrange multipliers
λ^{p,s}_{1,2} are as yet undetermined". No multiplier *field*, no adjoint PDE, no gradient, no
"conjugate/сопряжённая problem" terminology, no Hadamard derivative, no sensitivity. G14 is
un-threatened by this item, and the item is a positive data point that the school of 2004 was still
purely classical-variational.

### 4.3 ALGORITHMIC

**F10 — GAP-CONFIRMS (claim 8, empty niche "variational MoC + modern optimizer"; ALTA).**
There is **no algorithm at all**. §3 is titled "PROCEDURE AND RESULTS OF THE CALCULATIONS" (p. 628)
and its entire content is: "Restricting ourselves to the case of a perfect gas, we will describe the
procedure and results of the calculations …", followed by explicit sequential closed-form formulas
for h_aiᵖ, (V_aiᵖ)², θ∞, χ, and their heat-transfer counterparts (p. 629), evaluated to produce
Figs. 2–4. No discretisation, no MoC, no marching scheme, no iteration, no optimiser, no grid, no
convergence study, no error bar. The empty-niche claim is untouched, and the "no numerics" datum
extends the Kraiko-school evidence base to 2004.

**F11 — ADOPT (ideal-limit ceiling at matched period-integrated fluxes, as an executable oracle;
MEDIA).**
The paper's operational protocol is exactly our T-GB usage pattern and is worth importing verbatim as
a *reporting convention*. Summary, p. 631: "in these applications also, comparison of the achieved
augmentation coefficients with the values of χ_q and χ for the **ideal steady-state augmentor (at the
passive gas flow rate obtained)** will characterize the performance of the actual thrust augmentor."
Three transferable ingredients: (i) the ceiling is computed with the **preassigned period-integrated
fluxes** of the real device, not with idealised inputs — i.e. the ceiling is evaluated *at the
achieved operating point*; (ii) the ceiling is reported as a **ratio** (augmentation coefficient), so
it is dimensionless and comparable across designs; (iii) two ceilings are shipped (with and without
the extra physical freedom, here heat transfer), so the *value of the freedom* is priced. Innesto:
VI.6 Verdict — report J[S*]/B at the achieved (ṁ, H₀, μ), plus the ladder-rung spread, in place of a
bare gap δ.

### 4.4 Targeted hunt: everything this paper says about ISABE-2003-117 / Bogdanov 2002

**F12 — CORRECTION (caveat B descriptor and threat level; ALTA).**

*Complete harvest.* The pair is cited **exactly once in the body**, p. 622:

> "The primary, high-pressure gas flow can arrive at the augmentor either from the gas generator of a
> jet or rocket engine, whose exit flows are near-steady, or from a pulsed detonation rocket engine,
> **or from the combustion chamber with a rotating valve considered in [20, 21]**, or from some other
> 'primary' device."

That is the whole of it. There is no second mention, no description of their method, objective,
solver, or results. The reference entries (p. 632) read, verbatim:

> [20] V. I. Bogdanov, A. N. Kraiko, K. S. Pyankov, and N. I. Tillyaeva, "**Contouring an asymmetric
> nozzle for time-dependent stagnation parameters of the outflow and nozzle throat dimensions**",
> *Aeromekh. Gaz. Din.*, No. 3, 43 (2002).
>
> [21] A. N. Kraiko, K. S. Pyankov, and N. I. Tillyaeva, "**Optimal nozzle design when time-changing
> its throat size and pressure ratio**", 16th Intern. Symp. on Air Breathing Engines (ISABE
> Cleveland, Oh, USA 2003). ISABE-2003-117.

*What this establishes.*
1. **Not corroborated:** our advisory describes the pair as "variational maximum-**AVERAGE**-thrust
   contouring under time-dependent stagnation parameters". **Neither the in-text description nor
   either title contains "average", "mean", "period" or "thrust".** This citing source does **not**
   support the "maximum-average-thrust" descriptor. It must be down-graded to *unverified inference*
   until the ISABE text or Bogdanov 2002 is read, or until the descriptor's real source (plausibly
   Kraiko–Tillyaeva 2015) is re-checked.
2. **Newly established:** the physical driver is a **combustion chamber with a rotating valve** — not
   an RDE, not a detonation wave. Kraiko lists the pulsed detonation rocket engine as a *separate*
   primary device in the same sentence, so the 2002/2003 works are **not** detonation-wave work.
3. **Newly established:** the unknown in both is a **nozzle contour** ("Contouring…", "Optimal nozzle
   design…") — so, unlike the present 2004 paper, they *are* shape problems.
4. **Newly established and threat-raising:** what varies in time is the **throat size** *and* the
   pressure ratio *and* the stagnation parameters. A single contour designed while its own throat
   area sweeps a cycle is, structurally, **one shape shared across a family of operating states** —
   which is the D2-G3 shape. This raises, not lowers, caveat B's threat level.
5. **Newly established distinction in our favour:** their throat **moves**; our (P) has a **fixed**
   nozzle including a fixed throat, fed by a rotating-wave interface. And [20] is an **asymmetric**
   nozzle, i.e. plausibly plane/asymmetric rather than axisymmetric. These are genuine structural
   differences to state explicitly in the D2-G3 qualification.
6. **Inference, flagged as such (not evidence):** for "optimal nozzle design when time-changing its
   throat size" to be well posed with a *single* contour, some cycle-level objective (average, or
   worst-case) is logically required; and the same author's 2004 companion paper does formulate
   period-average thrust maximisation with the period scaled to ∫₀¹dt. Plausible, unproven.

*Action of record.* Keep caveat B; **re-word** it to "shape/contouring optimisation for a nozzle whose
throat size, pressure ratio and stagnation parameters vary in time (rotating-valve chamber); the
cycle objective is **not yet verified**"; and promote procurement of ISABE-2003-117 and
Bogdanov et al., *Aeromekhanika i Gazovaya Dinamika* No. 3 (2002) p. 43 to a **named P0 blocker** of
the D2-G3 / PB-2 novelty claims — this is now the single highest-value unread item in the litmap.

---

## 5. Bibliography inspection (required record datum)

22 references, p. 631–632, read in full.

**Classical optimal-nozzle line — ABSENT.** No Rao. No Guderley. No Hantsch. No Hoffman. No
Shmyglevskii. No Nikol'skii. No Kraiko–Osipov. Kraiko's own work appears only as [20] and [21], the
time-dependent-nozzle pair. Chernyi, *Gas Dynamics* [22] and Abramovich, *Applied Gasdynamics* [1]
are the only Russian gas-dynamics monographs cited.

**Modern adjoint / shape-optimisation line — ABSENT.** No Lions, Pironneau, Jameson, Giles, Ulbrich,
Lozano. No CFD-optimisation reference of any kind.

**What the list *is*.** An ejector/thrust-augmentor bibliography:
[2] Heiser 1967 (the base theory), [3] Parkhomov 1968, [4] Shlyakhtenko & Sosunov, *Theory of Bypass
Engines* 1979; the steady-ejector block [5]–[12] (Bogolyubov 1958, Mikhalev 1958, Kozyukov 1958,
Pearson–Holliday–Smith 1958, Quinn 1973, Cheng–Wang–Chisel 1973, Alperin & Wu 1983 Parts I and II);
the **pulsed-ejector block [13]–[19]** (Kudrin 1958, Ovsyannikov & Kudrin 1958, Bremhorst & Watson
1981, Favre-Marinet et al. 1981, Parikh & Moffat 1982, **[18] Munipalli, Shankar, Wilson, Kim, Lu,
Liston, "Performance assessment of ejector augmented pulsed detonation rockets", AIAA Paper
2001-0830**, **[19] Paxson, Wilson, Dougherty, "Unsteady ejector performance: an experimental
investigation using a pulsejet driver", NASA TM 211711, 2002**); then [20], [21], [22].

**Programme-relevant note.** [18] and [19] are detonation/pulse-jet ejector items already adjacent to
our RDE lit-map; [19] Paxson is the same author as the Paxson–Miki 2022-4107 item already read in the
choking census. Neither is cited here for anything variational.

---

## 6. What the paper proves vs. asserts (record separation)

**Proves (within its own integral model):** Eqs. (2.2)–(2.9) as **necessary** first-order conditions —
p_e = p_a for both streams, equality of exit velocities, equality of the two mass multipliers;
Eq. (2.10) as the residual first variation; Eq. (2.15) as the necessary heat-transfer condition;
the closed-form χ, χ_q of (2.14)/(2.17) and their k → ∞ limits (p. 631) as algebraic consequences.

**Asserts:** that entropy conservation (2.11) is optimal when Q = 0 (monotonicity argument, no formal
inequality-constrained treatment); that the equal-temperature heat-exchange limit is attainable; that
constant exit areas are the right selection among the many histories satisfying ∫F dt = const ("it is
natural to make the areas Fᵖ·ˢ constant", p. 627 — a **selection**, not a derivation, since the
objective is indifferent among them); that the optimum exists and is a maximum (no second-order
condition anywhere); that neglecting unsteady weak-shock entropy is legitimate.

This last point deserves emphasis for our purposes: the celebrated "the ideal periodic augmentor is
steady" conclusion is, strictly, **"the optimum is *indifferent* to the time history of F, and steady
is the natural representative"** — the collapse in F is a *non-uniqueness*, whereas the collapse in
(p_e, V_e) is genuine. Our T-T3 is stronger in exactly that respect: it is a pointwise identity on
shape space, not a selection among indifferent optima.
