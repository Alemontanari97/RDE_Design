# Expert read — Sun, Luo & Feng 2019, "New Contour Design Method for Rocket Nozzle of Large Area Ratio"

**Reader role:** convergence review, one-to-one comparison against the record apparatus of the
cycle-averaged variational nozzle program (M0 / P2_lemmaA / D3 / generality litmap).
**Date of read:** 2026-08-13.

---

## 1. Citation (verified from the PDF itself)

Dechuan Sun, Tianyou Luo, Qiang Feng, "New Contour Design Method for Rocket Nozzle of Large Area
Ratio", *International Journal of Aerospace Engineering* (Hindawi), Volume 2019, Article ID
4926413, 8 pages. https://doi.org/10.1155/2019/4926413. Received 3 September 2019; Revised 13
November 2019; Accepted 2 December 2019; Published 20 December 2019. Academic Editor: Wen Bao.
Affiliations: (1) School of Aeronautics and Astronautics, Dalian University of Technology, Dalian
116024, China; (2) Key Laboratory of Advanced Technology for Aerospace Vehicles, Liaoning Province
116024, China. Corresponding author: Dechuan Sun, dechuans@dlut.edu.cn. Open access, CC-BY.

*(All the above is printed on p. 1 of the PDF. Page numbers below are the printed journal page
numbers, which coincide with the PDF page indices 1–8.)*

## 2. Read coverage

**8 of 8 pages read in full**, including Section 5 (Conclusions), Nomenclature, Data Availability,
Conflicts of Interest, Acknowledgments and the complete reference list [1]–[21] (pp. 7–8).
Nothing was skipped.

**What could NOT be read exactly:** the figures are raster plots without tabulated data. Values I
quote from Figures 4, 5, 6, 7, 9, 10, 11 are *read off the plot* and are flagged as approximate
wherever used. Everything quoted from Tables 1–5, from the equations, and from the running text is
exact. There is no supplementary material referenced (Data Availability states all data are in the
article).

## 3. What the paper actually does

**Problem.** Contour design of the supersonic expansion section of a **large-area-ratio apogee
rocket nozzle**, single steady operating point, vacuum. Concrete case: a 750 N NTO/MMH engine
(O/F = 1.65, identical to China's 490 N / S400 class), chamber pressure p_c = 0.85 MPa, measured hot-fire
vacuum specific impulse I_sv = 320.4 s (p. 3). Baseline geometry (Fig. 3, p. 3): R_t = 12.25 mm,
R_u/R_t = 1.633, R_d/R_t = 0.816, β = 36.5°, an 80 %-length bell at area ratio 210 : 1. Target: area
ratio 330 : 1 at **80 % of the length of a 15° conical nozzle of the same area ratio**, x_e/R_t ≈ 51.5
(p. 4).

**Formulation.** Not a variational formulation. It is the **classical Rao/TOC *construction***
(Route A, mass-balance form), taken from Arrington, Reed & Rivera [9]: initial-value line by
Kliegel's method; kernel region by MOC from the initial line and the throat-downstream wall defined
by (R_d, β); last (terminal) characteristic *BD*; contour points E_i obtained by imposing **mass-flow
equality between BD_1 and D_1E_1** for sequentially chosen points D_i on BD; "finally, according to
the criteria of the exit point, the whole expansion contour can be obtained" (§2.3, p. 2). The
exit-point criterion is *never written down*.

**The actual modification (§2.4, pp. 2–3).** In Rao's method the thermodynamic state is obtained
from velocity with a *calorically perfect* closure, Eqs. (6a)–(6d):

    T = T_s − V²/(2 c_p),  c = √(γRT),  M = |V|/c,  p = p_s (T/T_s)^{γ/(γ−1)},  ρ = p/(RT).

Sun et al. replace this by a **thermally perfect** closure, Eq. (7):

    T = p/(ρR),  c = √(γRT),  M = |V|/c,

"where the heat capacity ratio is calculated by" Eq. (8): **γ = c_p/(c_p − R)**, with c_p a quartic
polynomial fit in temperature, Eq. (9):

    c_p = a0 + a1 T + a2 T² + a3 T³ + a4 T⁴

with printed coefficients: for T ≥ 1000 K, a0 = 1188.27296, a1 = 0.74502, a2 = −2.15067E−4,
a3 = 2.61593E−8, a4 = −7.06741E−13; for T < 1000 K, a0 = 1476.10931, a1 = −0.14838, a2 = 7.94836E−4,
a3 = −4.60444E−7, a4 = 8.11403E−11 (p. 4). Explicit caveat by the authors: "although the expression
of this c_p is identical with that of JANNAF database [21], the composition of the gas varies"
(p. 4). Viscosity is also fitted, Eq. (10): μ = 5.65752E−6 + 3.71243E−8 T − 5.00581E−12 T² +
4.3062E−16 T³.

**Design procedure (Fig. 1, p. 2).** ODE code (1-D chemical equilibrium) → Rao's method at constant
γ → *original contour* → ODK code (1-D non-equilibrium kinetics) on that contour → c_p(T) fit →
**modified Rao** → *new contour* → CFD evaluation → *add extension*. The kinetics freeze is one-shot
and explicitly justified by an unmeasured assumption: "we used the initial nozzle contour to
calculate the chemical reaction flow in the nozzle **under the assumption that the nozzle contour has
little change**" (p. 4).

**Unknowns.** The wall coordinates of the expansion section downstream of the kernel (points E_i),
plus, in the extension study, the choice among four hand-drawn extension curves L1–L4. Design
"parameters" swept: the constant γ value (6 values), and the extension curve (4 curves).

**Constraints.** Fixed nozzle length (80 % of a 15° conical at AR 330 : 1; the extension study raises
it to 85 %); fixed throat geometry and initial expansion arc (R_u, R_d, β from Fig. 3 for the
baseline; β and θ_e come *out* of the construction for the redesigns). Exit area ratio is an
**output**, not a constraint — this is stated in the Conclusions ("the exit area ratio of the nozzle
designed by this method not only reduces significantly from 330 : 1 to 256 : 1", p. 7).

**Flow model.** (i) *For design*: steady, axisymmetric, inviscid, isentropic MOC. Compatibility
equations, §2.2, p. 2: Eq. (1) ρV dV + dp = 0; Eq. (2) dp + c² dρ = 0; Eq. (3)
(√(M²−1)/(ρV²)) dp ± dθ + [sin θ / (yM cos(θ ± α))] = 0; Eq. (4) dy/dx = tan θ along the streamline;
Eq. (5) dy/dx = tan(θ ± α) along the Mach lines. (The paper calls this "the rotational axisymmetric
flow", but Eqs. (1)+(2) with a single stagnation state are the homentropic/irrotational set;
Eq. (3) as printed is **dimensionally inconsistent** — the third bracket carries no differential;
the standard axisymmetric term is (sin θ/(yM cos(θ±α))) dσ along the Mach line. Treat this as a
typesetting defect and do not transcribe it.) (ii) *For evaluation*: Fluent, 2-D axisymmetric
Navier–Stokes, implicit 2nd-order Roe-FDS, RNG k-ε turbulence with enhanced wall function (§2.5,
p. 3). The gas model used inside the CFD is not stated.

**Solver / "optimizer".** There is none in the modern sense. The design is a *construction*
(MOC + mass balance + an unstated exit criterion). The two "optimizations" are **manual enumerations**:
a 6-point sweep over constant γ ∈ {1.2, 1.238, 1.25, 1.275, 1.3, 1.32} (Fig. 6, Table 2, pp. 4–5) and a
4-curve sweep over extension shapes L1–L4 (Fig. 10, Table 5, p. 6). No gradients, no adjoint, no
optimality residual, no convergence criterion, no certificate.

**Verification.** Grid convergence, Table 1, p. 4: 288×60/80/100/120 → F_v = 735.897 / 735.895 /
735.901 / 735.926 N, F_m = 715.096 / 715.092 / 715.108 / 715.133 N, F_p = 20.801 / 20.803 / 20.793 /
20.793 N; grid 288×80 selected. Validation against hot fire: computed I_sv = F_v/ṁ =
735.895/0.235 = 3131.468 N·s/kg = 319.3 s vs. measured 320.4 s, **deviation −0.34 %** (p. 4). This is
the only external validation in the paper; the redesigned contours themselves are *not* tested.

**Headline results.**
- Constant-γ sweep (Table 2, p. 5): best at γ = 1.275, I_sv = 321.08 s; the whole constant-γ family
  spans only 320.19–321.08 s. "Rao's method with constant γ can only increase I_sv by 1.78 s
  (321.08−319.3)" (p. 5).
- Variable γ (Table 3, p. 5): I_sv = 322.00 s (F_v = 742.07, F_m = 723.57, F_p = 18.50 N); with
  boundary-layer displacement added, "Var.+dis.", I_sv = 322.09 s (F_v = 742.28, F_m = 724.08,
  F_p = 18.20 N). Geometry shift (Fig. 7, p. 5): constant γ = 1.275 gives β = 36.8°, θ_e = 8.5°,
  AR 280 : 1; **variable γ gives β = 36.1°, θ_e = 12.2°, AR 256 : 1**.
- Off-design (Table 4, p. 6), mass flow −20 %/−10 %/nominal/+10 %/+20 %: constant γ = 1.275 →
  I_sv = 320.55 / 320.97 / 321.08 / 321.10 / 321.38 s; variable γ → 321.22 / 321.65 / 322.00 / 321.83 /
  322.04 s. Variable γ wins at every point, "the highest increase of I_sv is on the design point".
- Extension (Table 5, p. 6), at 85 % length: Var.+dis. 322.09 s; L1 (straight) 322.42 s; L2 323.32 s;
  **L3 323.71 s (best)**; L4 323.64 s. Wall viscous drag D_w ≈ 36.97–37.71 N throughout.
  Mechanism given: "The expansion wave (in the case of L2, L3, and L4) originating from the curve
  accelerates the main flow to increase F_m and F_r. If the expansion angle is too large, the axial
  thrust will decrease (L4)" (p. 6).

## 4. Hypotheses

### Declared
1. Inviscid, isentropic flow for the design construction (acknowledged as a limitation, p. 2:
   "the assumption of inviscid isentropic flow makes it deviate from the real flow").
2. Steady, axisymmetric flow.
3. Thermally perfect gas: p = ρRT with c_p = c_p(T), Eqs. (7)–(9).
4. c_p(T) obtained from a **one-shot** 1-D kinetics (ODK) run on the *initial* contour, under the
   declared assumption "that the nozzle contour has little change" (p. 4).
5. Kliegel's method for the transonic initial-value line, justified by agreement with Back et al.
   via [9] (p. 2).
6. Contour points from mass-flow conservation across the terminal characteristic (§2.3).
7. RNG k-ε with enhanced wall function for the evaluation CFD (§2.5).

### Undeclared but necessary
8. **Constant gas constant R.** Eq. (8) γ = c_p/(c_p − R) and Eq. (7) T = p/(ρR) both hold R fixed,
   while the authors state that "the composition of the gas varies" (p. 4). A varying composition
   implies a varying mixture molecular weight and hence a varying R. Their thermo is therefore a
   **hybrid that is not thermodynamically self-consistent**: composition change is absorbed into
   c_p(T) while its effect on R (and on the frozen sound speed) is silently dropped.
9. **The energy integral is enforced only implicitly.** Eq. (6a), the calorically perfect energy
   integral, is dropped and *not replaced* by h(T) + V²/2 = h(T_s); T is recovered from the EOS
   instead. This is consistent only because Eqs. (1)+(2) with dh = dp/ρ reproduce the energy integral
   for a thermally perfect gas — the paper never states this and never verifies it (no energy-residual
   monitor).
10. **Single isentrope / homentropic, homoenergetic core.** Required for Eq. (2) plus a single
    (p_s, T_s) to close the state; asserted only by calling the set "rotational".
11. **Vacuum, p_a = 0.** Only vacuum thrust and I_sv are ever reported; the unstated "criteria of the
    exit point" must therefore be the p_a = 0 form of the classical corner condition. Never written.
12. **The optimality/exit-point criterion is unchanged from the constant-γ Rao construction.** The
    paper modifies only the *state evaluation* and is silent on whether the endpoint condition (which
    in the classical implementations is where the γ = const corner↔ε bijection lives) was re-derived.
13. **Frozen-composition sound speed.** c = √(γRT) with γ = c_p/(c_p − R) is the *frozen* thermally
    perfect sound speed; using it with a composition-varying c_p is inconsistent (see 8).
14. **The CFD gas model is unstated** — yet the entire contour ranking (Tables 2, 3, 5) rests on it.
15. **The boundary layer enters only as a post-hoc displacement thickness added to the inviscid wall**
    ("Var.+dis.", Table 3) — a correction map applied after the design, not a term in the objective.

## 5. Three-level comparison with the record apparatus

### TEORICO

**T1 — CONTAINED (ALTA).** The paper's design problem is a **Dirac-measure single-phase instance of
(P)**: μ = δ_{ξ0}, topology fixed a priori to *bell* (never an output), constraint vector c = (L fixed
at 80 % of the 15° conical at AR 330 : 1, x_e/R_t ≈ 51.5) with ε *free* and appearing as an output,
p_a = 0, solution class S_0 (shock-free homentropic MOC), thermally perfect frozen-composition EOS,
objective F = vacuum thrust. Under those exact hypotheses everything the paper does at design level
is a restriction of (P): the terminal-characteristic mass-balance construction is exactly the Route-A
control-surface object of our formal layer, and their Fig. 2(b) mass-equality step
("the mass flow through BD_1 is equal to the mass flow through D_1E_1", p. 2) is the discrete form of
the f2^i mass integrand along the terminal characteristic. Their extension study (L1–L4) is a
1-parameter subfamily inside our sector/continuation machinery, not a new object.

**T2 — GAP-CONFIRMS, D2 gap G3 (ALTA).** Section 4.3 (p. 5, Table 4) evaluates **two fixed contours
across a family of five inflow states** (mass flow −20 % … +20 %) and observes that the variable-γ
contour wins at all of them. That is the closest this paper comes to our object — and it stops
exactly where our gap begins: there is **no measure, no weighted objective, no averaged stationarity
condition, no shared-contour optimality**. The comparison is purely a posteriori between two designs
each obtained at the nominal point. Verbatim: "we compared the performance of the nozzles designed
by Rao's method and modified Rao's method" (p. 5). Nothing here derives optimality conditions for a
shape shared across a weighted family. **G3 stands, and this paper is a documented near-miss inside
it: the off-design family is *evaluated*, never *designed for*.**

**T3 — THREAT (MEDIA), against loose novelty phrasing on "variable γ".** This is a published,
CFD-verified, hot-fire-anchored instance of *γ(T) inside a Rao-type contour construction* with
quantified magnitudes (Tables 2, 3; Fig. 7). Any program sentence of the form "we are the first to
run Rao with variable γ" is **occupied** by Sun 2019 (and by its Chinese-language predecessor
Sun & Yu 2018, ref. [20]). Mitigation, and the exact place our claim must sit: our E4 claim is about
the **stationarity system** being EOS-general in primitive variables and about the **Λ-form/(G)
boundary** (claims 11–12) — neither object exists anywhere in this paper. Novelty must always be
stated at that level, never at the "we used γ(T)" level. Recommend registering this explicitly in
the litmap so the phrasing never drifts.

**T4 — ADOPT (ALTA), the kinetics-informed frozen c_p(T) freeze, and an external corroboration of
[T-EQBR].** Figure 5 (p. 4) plots γ vs area ratio for **frozen, kinetics and equilibrium** closures
of the same NTO/MMH mixture: the kinetics curve lies **strictly between** the frozen (upper) and
equilibrium (lower) curves over the whole range, with the three separating rapidly past the throat
(read off the plot at AR ≈ 200: frozen ≈ 1.385, kinetics ≈ 1.35, equilibrium ≈ 1.26 — approximate,
raster figure). This is an independent, published corroboration of the *ordering* that our
[T-EQBR] frozen/equilibrium bracket (+6.3 … +7.0 % above the frozen ceiling) assumes, and it names the
physical curve as an interior point of that bracket. **What to adopt:** the *procedure* — run 1-D
kinetics (ODK class) once on a seed contour, fit c_p(T) as a low-order polynomial, and use that
kinetics-informed frozen table inside the design march (Eqs. (8)–(9)). This is a cheap
bracket-**narrowing** PRACTICE that fits our P1 pin exactly (frozen thermally perfect, finite-rate
chemistry structurally contained but not instantiated). **Point of insertion:** DIR-THERMOTAB /
VI.2 table generation, as a second table generator alongside the Cantera equilibrium/frozen pair, and
in the D3 / M0 statement of [T-EQBR] as an external anchor. Note the functional class matches our
own survey: their c_p is **quartic in T** (Eq. (9)), the same order as the NASA fit whose quintic-h
closure we already reproduce exactly in the window.

**T5 — CORRECTION (ALTA), about how this paper may be cited.** Sun 2019 must **not** be cited as a
"frozen thermally perfect" reference compatible with our P1 pin. Their own text (p. 4) says the c_p
fit absorbs a **varying composition** while Eqs. (7)–(8) keep **R constant**. Under our P1 pin
(frozen thermally-perfect mixture, p = ρRT with fixed composition) their closure is *not*
admissible: it is a composition-varying c_p glued onto a fixed-R state equation and a frozen sound
speed. Consequence for us: (i) if their contour is ever used as an oracle, the discrepancy in R must
be priced first; (ii) our Lemma A thermal pin of record ("thermally-perfect ideal gas p = ρRT with
FROZEN composition, not relaxable") is *stricter* than what Sun 2019 does — their model sits outside
Lemma A's hypotheses, so their results carry no evidence for or against Lemma A. Register this in
the litmap row.

### FORMALE

**F1 — CORRECTION (ALTA), against our own reading-list rationale.** The list entry for this paper
says "Rao ri-derivato a gas termicamente perfetto γ(T)". **That is wrong and must be corrected.**
The paper contains **no re-derivation of anything variational**. It never writes Rao's
Euler–Lagrange system, never introduces the augmented density or the multipliers λ2, λ3, never states
the first integral f2 = W cos(θ∓α)/cos α = −λ2, never states q ρW² sin²θ tan α = −λ3, and never
states the corner/transversality condition (p_a = p − ½ρW² sin 2θ tan α). The only reference to the
endpoint is the phrase "according to the criteria of the exit point, the whole expansion contour can
be obtained" (§2.3, p. 2). What is actually modified is Eqs. (6a)–(6d) → Eqs. (7)–(9), i.e. the
**thermodynamic state evaluation inside the MOC march**, nothing else. Corrected one-line
characterisation for the litmap: *"Rao's TOC **construction** with the state closure re-based on a
thermally perfect γ(T); the variational conditions are neither restated nor re-derived."*

**F2 — CONTAINED (ALTA), and an external corroboration of E4's direction (a).** The structural move
in Eq. (7) — abandon the calorically perfect closed form T = T_s − V²/(2c_p) and
p = p_s(T/T_s)^{γ/(γ−1)} (Eqs. (6a), (6c)), and instead recover T from the **state equation in
primitive variables**, T = p/(ρR), with the marched (p, ρ) — is *precisely* the move our E4 audit makes
when it states that the stationarity system is EOS-general **in primitive variables** and that the
γ = const closed forms are the removable part. Sun et al. reach the same structural conclusion
empirically, at implementation level only, for the state evaluation. This is CONTAINED under: single
isentrope, frozen R, c_p(T), shock-free, steady, axisymmetric. It is *evidence in favour of* E4's
feasibility direction; it is **not** a proof of E4 and does **not** touch (L.6)–(L.16).

**F3 — GAP-CONFIRMS (ALTA), the Λ-form / (G) boundary is entirely absent.** The paper carries **no
validity-boundary object of any kind**: no Sternin/Rao–Beck boundary, no
val = [Λ·B·(A+B) − (A−B)]/[1 + Λ·(A+B)] monitor, no fold guard, no DEF construction, no PM-jump
landing. The bibliography confirms the vintage: it cites **Rao 1958** [11] and the Zucrow–Hoffman
textbook [12], but **not Rao 1961, not Rao–Beck 1994**; the construction is taken from Arrington,
Reed & Rivera 1996 [9]. Our S4 [THEOREM] (the Λ-form reduces exactly to Rao–Beck Eq. (4)) and the
whole margin/tier ladder are therefore strictly beyond this paper, and this paper cannot threaten
claims 9–11. It also confirms that the (G)-boundary apparatus is *not* standard equipment in the
applied-design literature — a data point for the generality litmap.

**F4 — GAP-CONFIRMS (ALTA), the E4 risk site (a) is load-bearing and now externally priced.** At
**fixed length**, moving from the best constant γ to the γ(T) closure moves the *design endpoint*
substantially: β 36.8° → 36.1°, **θ_e 8.5° → 12.2° (+3.7°, +44 %)**, exit area ratio 280 : 1 → 256 : 1
(§4.2 and Fig. 7, p. 5); relative to the original design the exit AR drops 330 : 1 → 256 : 1
(Conclusions, p. 7). Our E4 names the corner↔ε **bijection** as the surviving γ = const dependence in
implementations, and our pipeline pins it as FORBIDDEN as a solver step (VI.4bis). These printed
numbers are the external, independent measurement that the endpoint/exit-angle is **strongly**
sensitive to the γ model — i.e. the risk our E4 flags is not academic. *Caveat on what is
demonstrated vs asserted:* the paper **reports** the geometry shift; it does **not** attribute it to
the endpoint condition (it never discusses the endpoint condition at all). The attribution is our
inference; the magnitudes are theirs.

### ALGORITMICO

**A1 — GAP-CONFIRMS (ALTA), the empty-niche claim (claim 8) is reinforced, with a verbatim statement
of the schism.** There is no optimizer in this paper. "Optimization" = a 6-point manual sweep over
constant γ (Table 2, p. 5) and a 4-curve manual sweep over extension shapes (Table 5, p. 6). More
usefully, the authors state the two-camp view explicitly and choose the classical camp: after citing
CFD-based direct optimization [15]–[18] (Yumusak & Eyi; Ezertas et al.; Ogawa & Boyce, surrogate-assisted
evolutionary; Tanimizu et al.), they write — "These methods take into account the viscosity and
chemical kinetics in the real flow and show better performance in applications. However, these
methods not only are much more complicated than Rao's method but also have **little increase in
specific impulse of the nozzle of large area ratio**. For this reason, we restudied the nozzle design
process" (p. 2). That is a 2019, peer-reviewed articulation of exactly the gap our claim 8 asserts:
one either keeps the classical MOC/Rao construction (and then has no optimizer) or one goes to
black-box CFD optimization (and then abandons the variational formulation). **Nobody in this paper's
frame of reference keeps the variational MOC formulation and swaps in a modern optimizer.**

**A2 — ADOPT (ALTA), the thrust decomposition as a standing Verdict column.** Every performance table
in this paper reports **F_v = F_m + F_p** separately — momentum thrust and pressure thrust — and
Table 5 adds **D_w**, the wall viscous drag. This is diagnostically sharp and we currently do not
report it. Concretely, Table 3 (p. 5) shows that the variable-γ redesign **gains F_m (720.34 → 723.57 N,
+3.23 N) while losing F_p (19.55 → 18.50 N, −1.05 N)**; with the displacement correction, F_m 724.08 N,
F_p 18.20 N. Two designs with similar J can have entirely different mechanisms, and the split names
the mechanism for free. Why it matters structurally for us: Lemma C's affinity F = a[Σ]·P_c − p_a·b[Σ]
is precisely a momentum-vs-pressure decomposition, and the **p_a ≠ 0 breaker** in T-T3-MAP acts on
exactly the pressure term. **Point of insertion:** the VI.6 Verdict schema — add (F_momentum,
F_pressure, and, when a viscous debit is in play, D_wall) as required reported quantities beside
KKT/Hessian/oracles; and use the split as the executable read-out of the Lemma-C structure in the
T3-CONTROL protocol. Also worth adopting: their grid-convergence table reports **all three components
separately** (Table 1, p. 4), which is a stricter mesh-convergence statement than converging the
scalar thrust alone.

**A3 — ADOPT with a named repair (MEDIA), the thermo-freeze outer loop needs a residual monitor.**
Figure 1 (p. 2) is a **one-shot outer iteration on the thermodynamic closure**:
contour_0 → kinetics on contour_0 → c_p(T) table → contour_1. This is a sound structure and maps
directly onto our table-based thermo backend. What is missing — and what we must supply if we adopt
it — is any measurement of the fixed point: the authors declare the assumption "that the nozzle
contour has little change" (p. 4) and never re-run the kinetics on the redesigned contour, even
though their own result is that the contour changes a lot (AR 330 : 1 → 256 : 1, θ_e 8.5° → 12.2°,
§4.2 / Conclusions). Since the whole point of the paper is that the γ model materially moves the
contour, the un-iterated freeze is self-undermining at exactly the magnitude they report.
**Point of insertion:** DIR-THERMOTAB / VI.2 — adopt the loop, but as a *fixed point with a declared
residual monitor* (‖c_p^{(k+1)} − c_p^{(k)}‖ on the working window, plus a contour-move norm), with a
rejector that fires when the freeze residual exceeds a derived bar. This turns a PRACTICE with an
undeclared error into an instrumented one.

## 6. Bibliography inspection (record datum)

21 references, listed on pp. 7–8. Inspected in full.

**Classical variational nozzle line — almost entirely ABSENT:**
- **Rao 1958** — PRESENT: [11] G. V. R. Rao, "Exhaust nozzle contour for optimum thrust", *Journal of
  Jet Propulsion*, vol. 28, no. 6, pp. 377–382, 1958.
- **Zucrow & Hoffman** — PRESENT but as the *textbook only*: [12] M. J. Zucrow and J. D. Hoffman,
  *Gas Dynamics*, Wiley, New York, 1976.
- **ABSENT:** Guderley; Hantsch; Guderley–Hantsch 1955; **Hoffman 1967** (the variational
  multiplier-field paper); Scofield–Hoffman 1971; Hoffman–Thompson–Hoffman 1971; Johnson–Thompson–Hoffman;
  **Kraiko** (any); Kraiko–Osipov; Kraiko–Tillyaeva; **Shmyglevskii**; Sirazetdinov; Nikol'skii;
  **Rao 1961** (plug); **Rao–Beck 1994**; Miele / JOTA 1972; Sternin.
  There is **no Route-B (multiplier-field) reference of any kind** in this paper.

**Modern adjoint line — COMPLETELY ABSENT:** no Lions, no Pironneau, no Jameson, no Giles, no
Ulbrich, no Lozano, no adjoint reference whatsoever. The word "adjoint" does not appear in the paper.
The optimization references are all black-box / gradient-free or generic CFD optimization:
[15] Yumusak & Eyi, *Computers & Fluids* 65:25–34, 2012; [16] Ezertas, Yumusak & Eyi, 46th AIAA/ASME/SAE/ASEE
JPC, 2010; [17] Ogawa & Boyce, *JPP* 28(6):1324–1338, 2012 (surrogate-assisted evolutionary);
[18] Tanimizu, Mee, Stalker & Jacobs, *JPP* 27(1):40–49, 2011.

**Other references of interest to us:**
- [9] Arrington, Reed & Rivera Jr., 32nd Joint Propulsion Conference, 1996 — this is the paper from
  which the Rao procedure of §2.3 is taken; worth pulling if we want the exact form of the
  "criteria of the exit point" used here.
- [10] Östlund & Muhammad-Klingmann, *Applied Mechanics Reviews* 58(3):143–177, 2005 — the standard
  separation review; relevant to our g_sep state constraint.
- [20] **D. Sun and Z. Yu, "A nozzle contour optimization method considering the change in fuel gas
  properties", *Acta Armamentarii* (Chinese), vol. 39, no. 11, pp. 2145–2152, 2018** — the
  Chinese-language predecessor of this work. **This is a live instance of our declared blind spot
  "Chinese-language journals" (claim 20).** It should be named in the blind-spot list, not left
  generic: if a γ(T) *contour optimization* method exists there, it is the nearest prior art to T3
  and to the E4 discussion and it is unread.
- [21] Nickerson, Coats & Bartz, TDK (two-dimensional kinetic) reference program, NASA-CR-152999,
  1973 — the classical MOC+kinetics tool; relevant background for our P1 pin.

**Record conclusion on the bibliography:** this is an *applied engine-design* paper whose classical
anchor is Rao 1958 and a 1996 procedural paper, with zero contact with either the Route-B variational
school or the modern adjoint school. It therefore cannot threaten claim 1 (Rao = adjoint bridge) or
claim 18 (containment), and it positively reinforces claim 8 (empty niche).

## 7. Novelty relative to HTH-1971 / Hoffman-1967

At the **formal/variational level, this paper adds nothing and is behind the 1967–1971 state of the
art.** Hoffman 1967 and the Scofield–Hoffman 1971 line already treat variable-γ / frozen and reacting
flows *inside* the multiplier-field formulation, with the full transversality apparatus and the
optimality residual (our record: Hoffman 1967 Eq. (78) E = y·h1 − (u y' − v)·h3; Scofield–Hoffman
Eq. (43) the wall form; Scofield–Hoffman 1971 Table 2 Case 1, frozen thrust 2290 lbf, is our own G2
oracle for exactly this frozen-γ(T) class). Sun 2019 instead stays inside Rao 1958's Route-A
*construction* and replaces the state-evaluation closure. Its genuine contributions are engineering
contributions, and they are real ones: (i) a concrete, reproducible kinetics-informed c_p(T)
closure for an NTO/MMH apogee engine, with printed coefficients (Eq. (9)); (ii) **quantified
magnitudes at large area ratio** — the constant-γ family spans only ~0.9 s (Table 2), whereas the
γ(T) closure buys ~+0.92 s at the same length while *reducing* the exit area ratio 280 : 1 → 256 : 1
(Table 3, Fig. 7), i.e. the same performance at markedly lower nozzle weight, which is the
practically interesting claim of the paper; (iii) an outward-bending extension heuristic (L1–L4)
worth a further ~+1.6 s (Table 5); (iv) a hot-fire anchor for the evaluation chain (−0.34 %). All of
(ii)–(iv) are ASSERTED from CFD and one hot-fire point, not proved; and the redesigned contours were
never themselves tested.

## 8. Verdict for the program

- **Nothing here threatens a theorem.** T-T3, T-T4, T-T3-SI, T-T3-MAP, S4, O3.1, T-T0 are all
  untouched: there is no measure, no averaged objective, no validity boundary, no adjoint.
- **One real threat, to phrasing only** (T3): "variable γ inside a Rao construction" is occupied
  published territory; our novelty must always be stated at the stationarity-system / Λ-form level.
- **Two gaps confirmed with printed evidence**: G3 (family evaluated, never designed for — Table 4)
  and the empty niche (A1, with a verbatim two-camp statement on p. 2).
- **One correction to our own litmap** (F1): this is *not* a re-derivation of Rao at γ(T).
- **One correction to how we may cite it** (T5): their thermo is not frozen-consistent (varying
  composition, constant R) and sits outside Lemma A's thermal pin.
- **Three things to adopt**: the kinetics-informed c_p(T) freeze as a bracket-narrowing table
  generator (T4), the F_m/F_p/D_w thrust decomposition as a standing Verdict column and Lemma-C
  read-out (A2), and the thermo-freeze outer loop *with* a residual monitor and rejector we must add
  ourselves (A3).
- **One new named blind spot**: ref. [20], Sun & Yu, *Acta Armamentarii* 39(11):2145–2152, 2018
  (Chinese) — a *contour optimization* method accounting for changing gas properties, unread.
