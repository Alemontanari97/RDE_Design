# STAGE A — DE-NOVO TREE, LENS: ROCKET-PROPULSION TEST ENGINEER / JPP-CLASS REFEREE

Inputs read: PROBLEM_STATEMENT_agnostic.md, DERIVER_BRIEF_agnostic.md. Nothing else
(independence rule honoured). Knowledge tagged [KNOWLEDGE: author/year, depth].
Rigor classes: THEOREM / THEOREM-closure / SCHEMA / CONJECTURE / PRACTICE.
Notation: F = axial thrust, J = time-mean F, St = f*L/u (residence ratio), band_TS =
thrust-stand class (0.5-1 % of F, statement §8), eps = area ratio, p_b = base pressure.

--------------------------------------------------------------------------------
## PART 0 — WHAT THIS LENS BRINGS (four dry-level results that shape everything)

### DL-1 (rotating-frame equivalence) — class: THEOREM for smooth solutions, SCHEMA for weak
Hypotheses: (H1) axisymmetric solid S; (H2) interface data on Gamma_d of the form
q_d(r, theta - Omega t) with Omega = 2 pi f / n (pure single-mode rotating wave,
the §1 pin); (H3) the flow solution inherits the pattern symmetry (no symmetry
breaking, no mode hop). Then q(x,r,theta,t) = Q(x,r,theta - Omega t) and Q solves the
STEADY compressible Euler system in the frame rotating at Omega, with Coriolis and
centrifugal source terms (change of variables phi = theta - Omega t; d/dt -> -Omega d/dphi).
Corollary: J_true = azimuthal average over phi of the thrust flux of Q, i.e. a STEADY
integral. Time-mean thrust of the unsteady 3-D flow is EXACTLY a steady 3-D quantity
under the pin. The unsteadiness never has to be resolved in time.
Weak-solution caveat: existence/uniqueness of entropy weak solutions of multi-D Euler
is open [KNOWLEDGE: De Lellis & Szekelyhidi 2010, abstract]; the symmetric steady
solution is one admissible solution; (H3) is checkable a posteriori by one time-accurate
run started from the rotating-frame solution (falsifier of DL-1's applicability).
Precedent: RDE combustor simulation in the wave-fixed frame [KNOWLEDGE: Paxson 2014,
AIAA 2014-0284, abstract]; sector + phase-lag/rotating-frame practice in turbomachinery
[KNOWLEDGE: textbook].
Consequence: the "3-D rotating field" horizon of §7 is REACHABLE on a workstation as a
steady 3-D problem; every 2-D reduction is measured against it, not estimated.

### DL-2 (linear thrust law kills the quasi-steady Jensen gap for choked nozzles) — THEOREM under closure
Hypotheses: (H1) a throat exists downstream of Gamma_d and is choked at every instant;
(H2) quasi-steady limit St -> 0 (each instant a steady nozzle flow); (H3) 1-D inflow
(uniform over the section) with total state (p0(t), T0(t)); (H4) constant gamma.
Then F(t) = C_F,vac(eps, gamma) A_t p0(t) - p_a A_e, LINEAR in p0(t); hence
J = C_F,vac A_t <p0> - p_a A_e: the contour that maximizes C_F,vac (the CLASSICAL
steady optimum) maximizes the time-mean thrust for ANY waveform p0(t). Zero benefit
from any unsteady-aware contour design in this class. Relaxing (H4): C_F depends on
T0 only through gamma(T); over a cycle gamma swings ~ +-0.02 [KNOWLEDGE: textbook
thermochemistry, full], dC_F/dgamma ~ -0.5 at eps ~ 10 [KNOWLEDGE: Sutton & Biblarz
textbook, full] -> first-order term +-1 % is CAPTURED by the mean-state design (it is
linear); the residual Jensen gap is second order, ~ 0.5*|d2C_F/dT0^2|*Var(T0)/C_F,
estimated < 0.1 % << band_TS.
Consequence: the ONLY places an unsteady-aware nozzle design can buy anything above
band_TS are (a) a SUPERSONIC interface (no internal choke: C_F then depends nonlinearly
on the inflow Mach/angle/swirl distribution which sweeps the cycle), (b) finite St
(wave-nozzle interaction, sweeping oblique shocks in the divergent), (c) the per-instant
ATTACHMENT constraint becoming active, (d) unsteady base-pressure response. The decisive
instance MUST be posed there or the answer is "negative by lemma".

### DL-3 (swirl and radius) — THEOREM (axisymmetric inviscid, along streamlines)
r*u_theta = const along streamlines (axisymmetric Euler, no body torque). Swirl kinetic
energy per unit mass scales as r^-2. Moving streamlines OUTWARD (plug / expansion-
deflection / exit radius > annulus radius) converts swirl energy into pressure/axial
energy; moving them INWARD (bell collecting an annulus to the axis) concentrates swirl
(vortex core, low axis pressure, possible vortex breakdown). Materiality: swirl energy
fraction s = <u_theta^2>/<|u|^2>; with u_theta ~ 0.1-0.2 u (RDE exit swirl order
[KNOWLEDGE: Schwer & Kailasanath 2011, abstract]) s ~ 1-4 % -> ABOVE band_TS: swirl
recovery through the radial placement of the wetted contour is a first-order lever
of the design variable, larger than contour fine-tuning. Measured per instance from
the data (SP7 audit item).

### DL-4 (what a thrust stand can actually decide for an RDE) — PRACTICE, [KNOWLEDGE: full, own field]
Well-calibrated steady stands: 0.5-1 % of F. RDE stands: short runs (0.5-2 s for
uncooled hardware), kHz-order vibration, water-cooled feed lines (tare drift), thrust
drifting with wall heating; reported thrust uncertainties 1-3 %, mass flow (choked
venturis/sonic orifices) 1-2 %, hence Isp 2-4 % [KNOWLEDGE: Rankin et al. 2017 JPP,
abstract; Goto et al. 2019 JPP, abstract; Fotia et al. 2016 JPP, abstract]. Contour-
level differences (conical vs Rao at eps 5-10: 1-2 % [KNOWLEDGE: Rao 1958, full;
Hoffman 1987, abstract]) are at or below the RDE-stand resolution; configuration-level
differences (no nozzle vs divergent vs plug: 5-20 %) are resolvable. Consequence: for a
contour claim the decisive number is COMPUTED with derived bands and the experiment
ANCHORS THE EVALUATOR (validation datum), it does not resolve the difference; for a
configuration claim the experiment can be decisive.

--------------------------------------------------------------------------------
## LEVEL 0 — SP0 STRATEGIES (open enumeration; tuple = objective / time / space /
## solver+information / search+guarantee / decisive result)

### S-1 PRACTICE TODAY (comparator): steady classical design at a representative mean state
tuple: O-a implicit / time -> ONE representative mean state (mass-flux-weighted or
"equivalent available pressure" EAP [KNOWLEDGE: Kaemming & Paxson 2018 AIAA, abstract])
/ axisymmetric steady / rotational MoC (Rao bell, Angelino-Lee plug) [KNOWLEDGE: Rao
1958 full; Angelino 1964 full; Zucrow & Hoffman textbook full] / calculus-of-variations
optimum within the steady model, no unsteady guarantee, post-check with an unsteady
CFD run / decisive result: none (it is the baseline).
Question answered: narrowing "best steady nozzle for the mean state".
Cost: days of person-time; zero new theory. Generality: bell, plug (Angelino), all data
classes (needs only the mean state); truncated plug via empirical base.
Pins needed: none of §1 beyond a mean state; relaxes everything.
Falsifier: an unsteady-aware design beating it by > 2 x band on the same evaluator.
Time-to-number: 1 session. Rank: 0 (baseline, must be fielded at its STRONGEST, SP-CARM).
Abandon measurement: not applicable — it is the control.

### S-2 QUASI-STEADY WEIGHTED MULTIPOINT DESIGN
tuple: O-a / time -> St << 1, sum_k w_k F_k(S) over sampled instants (w = time fraction)
/ axisymmetric steady per instant / FV Euler or MoC + adjoint or FD / local KKT / decisive:
gain over S-1 on the quasi-steady evaluator at the same instants.
Question: Q0 narrowed to the St -> 0 class. Cost: low (N_k steady solves).
Generality: all configurations; classes B-F. Pins: single-mode (for the weights) and
St << 1 (measured). Falsifier: DL-2 (choked case: gain identically zero); for a supersonic
interface, a measured gain < band. Time-to-number: 2-3 sessions. Rank: 5.
Abandon: measured phase lag Delta_phi = 2 pi f * int dx/u_x > threshold of SP1 (then the
quasi-steady premise is false and this strategy answers nothing).

### S-3 ROTATING-FRAME STEADY 3-D DESIGN (exact under the pin, DL-1)
tuple: O-a + O-c per-azimuth constraint / time -> rotating frame, steady / 3-D annulus or
2 pi/n sector / steady 3-D FV Euler with Coriolis sources, discrete adjoint / local KKT,
multistart / decisive: Delta J vs S-1 with GCI bands.
Question: Q0 in full under the pin. Cost: HIGH compute (2-3 M cells, hours per steady
solve on a workstation, adjoint x2), moderate theory. Generality: all configurations,
classes B-G (G through a coupling loop). Pins: single mode + axisymmetric S; relaxes
nothing on gas. Falsifier: symmetry breaking in a time-accurate check; or the design loop
not converging within the session budget. Time-to-number: 8-10 sessions (at/over budget).
Rank: 3 (as a DESIGN loop); rank 1 as an EVALUATOR (see H-1).
Abandon: a time-accurate run seeded from the rotating-frame steady solution drifting
away (mode hop / symmetry breaking) at the design point -> the pin itself is false.

### S-4 AZIMUTHALLY AVERAGED (cycle-averaged) AXISYMMETRIC DESIGN WITH MEASURED CLOSURE
tuple: O-a + O-c / time -> averaged over phi in the rotating frame: steady axisymmetric
equations with wave-correlation ("unsteadiness stress") closure terms extracted from one
3-D rotating-frame solution / axisymmetric / FV Euler + discrete adjoint, MoC oracle /
local KKT + family-gap / decisive: Delta J evaluated on the 3-D evaluator.
Question: Q0 with a measured reduction error. Cost: low per design, one 3-D solve per
closure update. Generality: all configurations; B-G. Pins: single mode. Falsifier: the
closure terms changing between the two designs by more than the decisive difference
(closure not design-invariant). Time-to-number: 5-7 sessions. Rank: 2 alone, rank 1
inside H-1.
Abandon: |J_3D(S) - J_axi(S)| for the FINAL design larger than the claimed Delta J.

### S-5 FIXED-FRAME TIME-SPECTRAL / HARMONIC-BALANCE DESIGN IN A MERIDIONAL PLANE (2-D + t)
tuple: O-a / time -> Fourier in t at fixed theta, azimuthal fluxes dropped / 2-D(x,r)+t /
time-spectral Euler + time-spectral adjoint [KNOWLEDGE: Hall, Thomas & Clark 2002,
abstract; van der Weide et al. 2005, abstract; Nadarajah & Jameson 2007, abstract] /
local KKT / decisive: Delta J vs S-1.
Question: Q0 under an UNMEASURED approximation (d/dtheta = -(1/Omega) d/dt is dropped,
which is exactly the term DL-1 keeps). Cost: moderate. Generality: all configurations;
B-F. Pins: single mode. Falsifier: the dropped azimuthal flux measured from S-3 being of
the order of the decisive difference (expected: it is O(1) — the relative azimuthal Mach
number Omega r / a ~ 2-3 at r = 5 cm, f = 10 kHz, n = 1). Time-to-number: 4-5 sessions.
Rank: 8 (rejected FOR THE STATED REASON: under the pin S-3 is exact at similar cost,
S-5 approximates with an O(1) term).
Abandon: azimuthal-flux magnitude from the 3-D solution > 0.5 x band.

### S-6 TIME-ACCURATE 3-D (LES/URANS) DESIGN LOOP
tuple: O-a / time-accurate / 3-D / unsteady adjoint or gradient-free / best-effort /
decisive: as S-3. Question: Q0 at horizon fidelity. Cost: HPC-class (weeks per design
iteration); excluded by §8 for the decisive answer; priced as ~50-100x S-3. Generality:
full, classes A-G; relaxes the single-mode pin (can host mode hopping). Falsifier: n/a.
Rank: 10 (horizon oracle only; one run affordable as the DL-1 symmetry check if a
compiled solver exists in the pinned stack).
Abandon: unaffordable by construction.

### S-7 GRADIENT-FREE / SURROGATE SEARCH ON A LOW-DIMENSIONAL FAMILY WITH THE 3-D EVALUATOR
tuple: O-a + O-c / rotating-frame steady / 3-D / FV Euler, no derivatives / Bayesian
optimization or CMA-ES [KNOWLEDGE: Jones, Schonlau & Welch 1998, full; Hansen CMA-ES,
abstract] with a family-bounded gap / decisive: Delta J vs S-1.
Question: Q0 narrowed to a 3-6 parameter family (Rao theta_n, theta_e, L; plug
truncation, wall angle, exit radius). Cost: 30-100 3-D solves = beyond the 3 h/session
window unless the mesh is coarsened (band grows). Generality: full; B-G; robust to
non-smoothness (separation onset, base switching). Pins: single mode. Falsifier: the
surrogate's predicted optimum not reproduced by the evaluator within the band.
Time-to-number: 6-8 sessions. Rank: 4 (fallback if the adjoint fails its rejector across
discontinuities, SP3).
Abandon: two independent BO runs disagreeing on the optimum by more than the band.

### S-8 OBJECTIVE CHANGE: MISSION / ENVELOPE ROBUST DESIGN (O-b)
tuple: O-b (weighted over ambient-pressure profile and throttle) / any of S-2..S-4 per
point / axisymmetric / adjoint / local / decisive: mission-integrated Isp of the
optimized plug vs the classical mission-averaged bell.
Question: a DIFFERENT question (engine-on-mission), classical practice already does the
trajectory average [KNOWLEDGE: Hagemann, Immich, Nguyen & Dumnov 1998 JPP, full: plug
and dual-bell gains of a few % integrated Isp]. RDE-specific novelty: small (the RDE
enters only through the interface data). Cost: multiplies S-4 by the number of points.
Generality: D, E classes needed. Rank: 6 (second paper).
Abandon: mission gain of the RDE-aware design over the classical mission design < band.

### S-9 OPERABILITY-FIRST DESIGN (O-c as the lever, O-a as the objective)
tuple: max J s.t. per-instant attachment margin m(x, phi) >= mu and side-load proxy /
rotating-frame steady (per-azimuth = per-instant) / 3-D or averaged / adjoint on the
margin / local KKT with active-set multipliers / decisive: the per-instant separation map
of the classical design (violated) vs the certified design (not), verified by a
high-frequency wall-pressure measurement.
Question: Q0 on the axis a referee CAN verify experimentally (kHz separation transients
are measurable with PCB-class wall transducers and side-load strain gauges; thrust
differences are not, DL-4). Cost: as S-4 plus the criterion instrumentation. Generality:
all configurations; B-F (F essential: margin under data uncertainty). Pins: single mode;
quasi-steady boundary-layer response (derived: delta/u_e ~ 1e-3 m / 2e3 m/s ~ 0.5 us <<
period 30-1000 us -> SCHEMA, falsifier = hysteresis in measured wall pressure).
Falsifier: the classical design's minimum instantaneous wall pressure never crossing the
criterion at the design point (then the constraint is inactive and S-9 collapses into S-4).
Time-to-number: 4-5 sessions. Rank: 2 as a stand-alone; FOLDED into H-1 as the
constraint and as the SECOND decisive measurable.
Abandon: measured wall-pressure minima on an instrumented divergent staying above the
criterion by more than the criterion scatter for the classical design.

### S-10 DESIGN-VARIABLE CHANGE: CONFIGURATION / EXIT-RADIUS / THROAT AS VARIABLES, CHAMBER COUPLING
tuple: O-a of the ENGINE / rotating frame + reduced combustor response map (class G) /
3-D or averaged / evaluator + response map iteration / local / decisive: engine thrust
of the co-designed (throat restriction, exit radius, plug vs bell) vs the classical
sequence (combustor then nozzle).
Question: Q0 read as "the engine's lever": nozzle back-pressure changes fill, wave count
and pressure gain by 5-20 % [KNOWLEDGE: Fotia et al. 2016 JPP, abstract; Bach et al.
2020, abstract] — an order of magnitude above contour effects (DL-2/DL-4). Cost: needs a
credible response map (class G) = a combustor model; theory moderate. Generality: G only.
Pins: relaxes the causal-separation premise (it models the violation). Rank: 7 here
(needs class G, outside the certified nominal answer) but flagged as THE lever the
referee will ask about (SP-OBJ). Abandon: measured combustor response to the nozzle
change < band (then the sequential practice is fine).

### S-11 QUASI-1-D UNSTEADY SCREENING (area law + stratified inflow)
tuple: O-a / time-accurate 1-D / Q1D / explicit FV, FD gradients / screening, no
guarantee / decisive: none (ranking tool). Question: a screening surrogate for St
effects. Cost: trivial. Generality: bell only (area law), no base, no swirl. Rank: 9
(instrument for SP1's St threshold, never a solver step). Abandon: n/a.

### S-12 ANALYTICAL VARIATIONAL MoC EXTENDED TO THE WEIGHTED CYCLE ("cycle-averaged Rao")
tuple: O-a / quasi-steady weights or averaged closure / axisymmetric characteristics /
Lagrange multipliers along characteristics, closed-form optimality (Rao / Guderley /
Kraiko class) [KNOWLEDGE: Rao 1958 full; Guderley & Hantsch 1955 title; Kraiko
variational gas dynamics, title] / calculus-of-variations optimum within the model /
decisive: same as S-2/S-4 with the analytic KKT as a cross-check of the discrete adjoint.
Question: Q0 in the quasi-steady or averaged class with a theorem-grade first-order
condition. Cost: new theory (multipliers with rotational, variable-gamma, weighted
functional; attachment constraint as a state constraint on characteristics is hard).
Generality: bell and plug full-flowing; truncated base = closure; no finite St.
Rank: 5-bis (as an ORACLE for SP3, not as the road). Falsifier: DL-2 in the choked case;
disagreement with the discrete adjoint beyond the MoC discretization band.
Abandon: the analytic condition unable to host the per-instant attachment constraint.

### S-13 HARDWARE-IN-THE-LOOP EXPERIMENTAL OPTIMIZATION (printed nozzle sweep on a stand)
tuple: O-a measured / real time / real 3-D / thrust stand / design of experiments /
decisive: measured Isp ranking. Question: Q0 at configuration level only (DL-4).
Cost: hardware, test time; access not guaranteed (§8). Generality: any. Rank: 11 for the
decisive number, but the ONLY external anchor class (SP8/SP9). Abandon: n/a.

### S-14 ASYMPTOTIC IN St (small-St expansion around the quasi-steady limit)
tuple: O-a / J = J_qs + St^2 J_2 + ... / axisymmetric / perturbation solves / local /
decisive: the measured J_2 coefficient. Question: Q0 for St below a derived threshold.
Cost: theory moderate. Generality: bell/plug; B-F. Rank: 9-bis (instrument to derive the
SP1 threshold; the coefficient is MEASURED with two rotating-frame solves at Omega and
Omega/2). Abandon: the expansion not converging (J_2 St^2 not << J_qs).

### H-1 (TOP RANK) HYBRID: averaged axisymmetric DESIGN loop + rotating-frame 3-D EVALUATION + per-instant attachment
tuple: objective O-a (time-mean thrust at fixed interface data = Isp) subject to O-c
per-instant attachment as a state constraint with multiplier / time -> DL-1 rotating
frame; design in the phi-averaged steady axisymmetric model (S-4), evaluation in steady
3-D (S-3), St measured, quasi-steady branch (S-2) taken only when the SP1 threshold is
met / space -> axisymmetric (design), 3-D sector 2 pi/n (evaluation) / solver: FV Euler,
thermally perfect frozen gas, shock capturing with a-posteriori validity; discrete
adjoint (AD) for the design loop, Rao/MoC legacy code as oracle, FD rejector / search:
continuation from the classical design (S-1) + local KKT with multipliers + family-gap by
BO on a 3-5 parameter family / decisive: D = [J_3D(S_H1) - J_3D(S_CARM)] / J_3D(S_CARM)
on a supersonic-interface annular RDE with (case 1) a divergent bell and (case 2) a
truncated plug with FIXED base, class B(+F) data, plus the per-instant separation map of
S_CARM; bands = GCI + data sensitivity + base interval; kill criteria in SP9.
Question: Q0 as posed (methodology with certificates + one number + publishable either
way). Cost: 7-9 sessions, one 3-D evaluator, moderate theory (closure extraction, adjoint
through captured discontinuities). Generality: bell / plug / shrouded / E-D (configuration
as INPUT for the decisive instance, priced in SP6); classes B-F certified, A via a model
chain (uncertainty dominated), G declared out of the nominal answer.
Pins needed: single mode (DL-1), frozen thermally perfect gas (same gas for both designs:
affects absolute Isp by the frozen/equilibrium bracket, not the difference to first
order), axisymmetric S. Could relax: single phase trivially; mode count n > 1 via sector.
Falsifier: (i) D within the band -> negative result, publishable; (ii) closure not
design-invariant (S-4 abandon); (iii) DL-1 symmetry check fails.
Time-to-number: 7-9 sessions (decisive 3-D runs at the 3 h window edge — priced in SP2).
Rank: 1.
ABANDON MEASUREMENT: on the final pair of designs, |J_3D - J_axi| (the reduction error,
measured) exceeding |D|; or D < 1 % AND the classical design's per-instant margin never
active — then the honest answer is "classical mean-state design is optimal within the
thrust-stand class for this configuration and St" and the program pivots to S-10 (the
engine lever).

--------------------------------------------------------------------------------
## LEVEL 1 — SUB-PROBLEM TREES FOR H-1

### SP-OBJ — OBJECTIVE (LOAD-BEARING)
Options:
 OBJ.1 time-mean thrust at fixed interface data at one design point (= Isp since mdot is
       fixed by supersonic data); metric normalized as eta = J / F_ideal, F_ideal =
       stream-tube isentropic expansion of the same data to p_a, swirl removed.
 OBJ.2 vacuum time-mean thrust (drops the p_a term; cleaner for upper stages).
 OBJ.3 mission/envelope weighted Isp (O-b) — S-8.
 OBJ.4 operability as objective (max min-margin) — S-9 pure.
 OBJ.5 composite (Isp - lambda*mass - side-load penalty) — O-d proxies.
 OBJ.6 engine-level thrust with chamber coupling (class G) — S-10.
Recommendation: OBJ.1 with O-c as a hard per-instant constraint (multiplier reported)
and O-d only as bounds (length, exit radius, mass proxy). Grounds: it is the only
objective whose comparator (S-1) is unambiguous and whose evaluation the referee can
anchor (thrust-stand class); OBJ.3/OBJ.6 change the question. Lever honesty (mandatory
for the referee): combustor-side losses (incomplete mixing, parasitic deflagration,
injector recovery) are 5-15 % of ideal [KNOWLEDGE: Anand & Gutmark 2019 PECS,
abstract; Raman, Prakash & Gamba 2023 ARFM, abstract], nozzle configuration/area
ratio 5-20 %, swirl recovery 1-4 % (DL-3), contour fine-tuning 1-2 % (DL-4). The nozzle
CONTOUR is a second-order lever; the paper must say so up front and derive its
decisive claim where DL-2 leaves room.
Decision criterion: a referee in propulsion accepts "Isp at fixed inflow, attached at all
instants" as THE nozzle question; the objective is settled by DL-2/DL-4, not by taste.
Falsifier: if the interface can only be placed subsonic (SP7 audit fails) then OBJ.1 is
ill-posed without class G and OBJ.6 becomes mandatory.
Options: 6.

### SP1 — TIME (LOAD-BEARING)
Measurement of the residence ratio: not St = f L / u_mean (too crude) but the phase lag
Delta_phi = 2 pi f * int_0^L dx / u_x(x) along the mass-flux-weighted mean streamline
(computed from the steady mean solution; reported per instance), plus the relative
azimuthal Mach number map M_rel = |u_theta - Omega r| / a in the rotating frame.
Options:
 T.1 mean-state (S-1): requires nothing; loses the cycle entirely.
 T.2 quasi-steady weighted (S-2): requires Delta_phi below threshold (derived below).
 T.3 rotating-frame steady 3-D (DL-1): requires only the pin; exact.
 T.4 phi-averaged steady axisymmetric with measured closure (S-4): requires one T.3 solve
     per closure update; error = measured difference.
 T.5 fixed-frame time-spectral 2-D+t (S-5): drops an O(1) term; rejected (stated).
 T.6 time-accurate (S-6): horizon check only.
 T.7 small-St expansion (S-14): instrument to derive the T.2 threshold.
Derived threshold for T.2: write J(Omega) = J_qs [1 + c2 A^2 Delta_phi^2 + O(Delta_phi^4)],
A = relative amplitude of the interface state over the cycle (measured from the data),
c2 measured from two T.3 solves at Omega and Omega/2 (Richardson on the quadratic term).
T.2 is admissible iff c2 A^2 Delta_phi^2 < 0.1 x band_TS (so the quasi-steady error is
one decade below the accuracy class) — a derived, instance-specific criterion.
Design loop: T.4 (cheap, differentiable); T.2 only if the threshold holds (then T.4's
closure is zero and the two coincide). Evaluation: T.3 always.
Decision criterion: the measured closure magnitude and Delta_phi. Falsifier: closure not
design-invariant (|closure(S_H1) - closure(S_CARM)| effect on J > |D|); then design must
move to T.3 (S-3, priced 8-10 sessions).
Options: 7.

### SP2 — FLOW MODEL AND SOLVER (LOAD-BEARING)
Model: frozen thermally perfect mixture (pin), h(T), cp(T) tabulated from the composition;
Euler; viscous layer only in the attachment criterion (declared model layer).
Solver options:
 F.1 rotational, variable-gamma axisymmetric MoC (classical; the legacy Fortran oracle
     is this class): exact for smooth supersonic flow, cannot host captured shocks from
     the stratified inflow without shock fitting; oracle only.
 F.2 steady axisymmetric FV Euler, shock-capturing, entropy-stable flux, pseudo-time
     (design loop).
 F.3 steady 3-D rotating-frame FV Euler with Coriolis/centrifugal sources on a 2 pi/n
     sector with periodic BC (evaluator).
 F.4 space-marching in the rotating frame where M_rel > 1 in the marching direction
     (steady supersonic 3-D, PNS-like): 10-100x cheaper than F.3, valid only where the
     M_rel > 1 indicator holds everywhere on the marching front (near the axis of a plug
     it fails: Omega r -> 0). SCHEMA; use as accelerator with the indicator as gate.
 F.5 time-accurate FV (2-D or 3-D): DL-1 symmetry check only.
 F.6 Q1D unsteady: screening.
Embedded discontinuities: the RDE exhaust carries an oblique shock and a slip surface
(stratification) per wave [KNOWLEDGE: Schwer & Kailasanath 2011 CF/2013, abstract];
in the divergent the shock reflects from the wall. Treatment: capturing + a-posteriori
validity: (v1) global conservation of mass/momentum/energy over Omega(S) to a tolerance
derived from the discretization order (residual scaling as h^p with observed p); (v2)
discrete entropy inequality satisfied cell-wise (loud reject otherwise); (v3) detected
discontinuities satisfy Rankine-Hugoniot to within the captured-jump width band; (v4)
attachment margin evaluated. Non-uniqueness: the entropy-satisfying steady solution
reached by pseudo-time from two different initial states must coincide within the GCI
band (rejector for multiplicity); disagreement = declared multiplicity, design rejected
from the certified class.
Attachment criterion options:
 A.1 Summerfield p_w/p_a < 0.4 [KNOWLEDGE: textbook] — too crude (fixed ratio).
 A.2 Schmucker correlation [KNOWLEDGE: Schmucker 1973, abstract].
 A.3 Stark: p_sep/p_a = 1/(1.88 M_w - 1) [KNOWLEDGE: Stark 2005, abstract] — Mach-
     dependent, database scatter of order 10-15 % in p_sep (to be taken from the source
     when cited; the margin mu is that scatter plus the data-induced uncertainty of p_w).
 A.4 free-interaction / boundary-layer integral shock-interaction model [KNOWLEDGE:
     Chapman, Kuehn & Larson 1958, abstract] — physics-based, needs a BL integration
     along the wall in the rotating frame (steady per azimuth).
 A.5 RANS per azimuth — cost beyond budget for the loop; validation of A.3/A.4 only.
Recommendation: A.3 as the certified criterion with margin mu derived as above, A.4 as
the cross-check; per-instant = per-azimuth on the F.3 wall pressure (the rotating-frame
wall pressure at (x, phi) IS the time history at x). Quasi-steady BL response: delta/u_e
~ 0.5 us << period (S-9 derivation) -> steady criterion legitimate (SCHEMA; falsifier:
measured hysteresis). Side loads: the azimuthal asymmetry of the wall pressure in the
rotating frame gives a ROTATING side force directly (integral of p_w n_y over the wall in
the rotating frame); reported as a proxy with no extra model.
Compute pricing for F.3 (dry estimate, hypotheses stated): L = 0.15 m, R = 0.05 m, n = 1,
captured shock width target 1 mm -> ~150 x 50 x 300 = 2.25 M cells; pseudo-time to
convergence ~5e3 iterations -> 1e10 cell-updates; at 1e6 cell-updates/s (vectorized
Python) = 3 h = the session window; at 1e7 (compiled kernels in the pinned stack) =
20 min. GCI needs 3 meshes (1/8, 1/64 cost extra). n = 2 halves the sector. If only
1e6 cell-updates/s is available the road prices +2 sessions or accepts the coarse-mesh
band (declared, not hidden).
Decision criterion: the validity checks v1-v4 pass on every consumed solution; GCI
observed order within [p-0.5, p+0.5] of the nominal. Falsifier: any consumed solution
failing v1-v4 (then that number is not quotable).
Options: 6 solver + 5 attachment = 11.

### SP3 — INFORMATION FOR THE OPTIMIZER (LOAD-BEARING)
Options:
 G.1 finite differences on a low-dim family (N+1 solves per gradient): robust, costly,
     step-size sensitive; the natural REJECTOR for any other gradient.
 G.2 complex-step: exact to roundoff for smooth branches; fails across max/min/abs of
     limiters unless they are complex-safe.
 G.3 discrete adjoint by automatic differentiation of F.2 (design loop): one extra solve
     per gradient; differentiates through the captured discontinuity exactly as the
     discrete functional does.
 G.4 continuous adjoint of Euler with explicit shock/contact jump conditions [KNOWLEDGE:
     Giles & Pierce 2001, abstract]: theorem-grade in 1-D, PRACTICE in 2-D/3-D.
 G.5 Rao/MoC variational multipliers (S-12): analytic oracle in the smooth steady class.
 G.6 surrogate gradients (BO posterior): for S-7 only.
Behaviour across discontinuities: the discrete adjoint of a conservative capturing
scheme gives the derivative of the DISCRETE integral output; mesh convergence of that
derivative to the continuous sensitivity is established in 1-D and observed in multi-D
[KNOWLEDGE: Giles & Pierce 2001, abstract] -> PRACTICE class, hence a rejector is
mandatory. Non-differentiable points: separation onset (constraint activity), base
regime switching, shock-wall reflection point moving across cells: use the MARGIN
FUNCTION m(S) (smooth up to the criterion) as the constraint and check the gradient's
mesh convergence in addition to its FD consistency.
Rejector (derived tolerance): with FD error model e(h) = a h^p + c eps_mach/h, evaluate
g_FD at h, h/2, h/4; the AD-FD discrepancy must decrease at the observed rate p until the
roundoff floor floor = 2 c eps_mach / h_opt; REJECT if |g_AD - g_FD(h_opt)| > 10 x floor,
or if the observed rate departs from p by more than 0.5, or if the gradient changes under
mesh refinement by more than the GCI of the gradient itself. Reported for EVERY design
variable at the start, at the optimum, and at one interior iterate.
Recommendation: G.3 for the loop, G.5 (legacy MoC) as the smooth-branch oracle, G.1 as
rejector. Grounds: cost (one adjoint per gradient) and consistency with the discrete
objective. Falsifier: the rejector firing at the optimum -> fall back to S-7 (G.6).
Options: 6.

### SP4 — SEARCH STRATEGY AND GUARANTEE CLASS (local)
Options:
 X.1 gradient-based SQP / trust-region with the attachment margin as inequality,
     multipliers reported (marginal value of length, exit radius, attachment).
 X.2 multistart from perturbed classical designs.
 X.3 Bayesian optimization on a 3-5 parameter family (family-bounded gap: the GP's
     upper confidence bound at termination bounds the family regret, PRACTICE class).
 X.4 CMA-ES.
 X.5 branch-and-bound with Lipschitz constants measured from the gradient norm (bounded
     gap, feasible only for <= 3 parameters; gap = L_lip x cell diameter).
 X.6 continuation/homotopy from the classical design in the closure magnitude (0 -> 1)
     and in Omega (quasi-steady -> actual).
 X.7 one-shot (simultaneous state/design).
Handling of invalid states: a design whose flow fails v1-v4 (SP2) is INFEASIBLE, treated
through the margin functions (attachment) or rejected with a flag (conservation/entropy
failure) and the trust region shrunk; never silently evaluated.
Recommendation: X.6 + X.1 (local KKT with multipliers, verified second-order by the
Hessian in the family via FD of the gradient), then X.3 on the family to bound the gap.
Guarantee class to be declared: LOCAL optimum with verified KKT, FAMILY-bounded gap
(within the parametric family; the infinite-dimensional class has no global guarantee,
stated). Decision criterion: no BO iterate better than the KKT point by more than the
numerical band. Falsifier: BO finding a better design beyond the band -> the KKT point
was a poor local optimum; report the better one and its own KKT.
Options: 7.

### SP5 — SPATIAL REPRESENTATION (LOAD-BEARING)
Options:
 R.1 Q1D — screening only.
 R.2 axisymmetric steady at the mean state (S-1 class) — loses everything unsteady.
 R.3 axisymmetric steady with phi-averaged closure (design loop): loses the wave
     correlation terms beyond the closure.
 R.4 2-D + t at fixed theta (S-5): loses the azimuthal flux, O(1).
 R.5 3-D rotating-frame steady, full annulus.
 R.6 3-D rotating-frame steady, 2 pi/n sector with periodicity: exact for the pin at
     1/n of the cost; identical to R.5 for n = 1.
 R.7 3-D time-accurate: horizon.
Measurement of loss (not estimate): on the SAME design, J_R6 - J_R3 (the reduction error,
a number with its GCI band), the closure-term magnitudes extracted from R.6, and the
azimuthal-flux magnitude (what R.4 drops). Designer: R.3; evaluator: R.6. Different
representations for designer and evaluator are DELIBERATE: the design loop only needs
a good direction, the evaluator carries the claim.
Decision criterion: reduction error < band for the final designs. Falsifier: reduction
error > |D| (H-1 abandon measurement) -> design must move to R.6 (S-3).
Options: 7.

### SP6 — GEOMETRY AS DESIGN VARIABLES (local, with one load-bearing pin)
Representation options:
 P.1 Rao 3-parameter family (theta_n, theta_e, L) or parabolic approximation: minimal,
     classical, cannot express what the classical cannot.
 P.2 B-spline / NURBS wetted contour with control points; count derived from a
     resolution criterion: spacing = the smallest wall-pressure feature length measured
     on the mean solution (shock reflection footprint) divided by 2 (Nyquist), never a
     fixed number.
 P.3 CST (class-shape transformation).
 P.4 free-form level-set / topology (configuration as OUTPUT): prices at S-3 cost in 3-D
     with topological non-smoothness; out of budget — configuration declared INPUT for
     the decisive instance; what is lost: the possibility that the optimizer would have
     changed configuration (bounded by comparing the two configurations' optima, which
     the decisive instance does in cases 1 and 2).
 P.5 hybrid P.1 warm-start + P.2 refinement (recommended).
Admissibility certificates: B-spline convex-hull property gives SUFFICIENT conditions:
slope bounds from control-polygon slopes; curvature bounds from second differences /
spacing^2; attachment on Lambda by clamping the first control point; envelope by control-
point boxes; regularity class C^1 with Lipschitz slope (cubic B-spline gives C^2).
Existence of a maximizer: in the finite-dimensional compact parameter box with J
continuous, existence is Weierstrass; continuity of J fails only at separation onset,
which the closed constraint m(S) >= mu excludes from the feasible set (feasible set
closed -> existence holds). For the infinite-dimensional class: uniform-cone /
Lipschitz-domain compactness [KNOWLEDGE: Chenais 1975, abstract] — stated as the class,
not needed for the finite-dimensional certified answer.
As-built tolerance: machining +-0.05-0.1 mm, additive +-0.1-0.2 mm [KNOWLEDGE: own
practice, full]; certify |Delta J| <= ||grad J|| delta + 0.5 lambda_max delta^2 with the
family Hessian, and m(S) - mu >= ||grad m|| delta (margin survives perturbation); the
tolerance class delta is an INPUT of the constraint vector; a design whose margin is
consumed by delta leaves the certified class.
Decision criterion: the control-point count from the resolution criterion vs the
gradient's rejector cost. Falsifier: J changing by more than the band when the control-
point count is doubled at fixed optimum (under-resolved family).
Options: 5.

### SP7 — DATA (LOAD-BEARING through the audit)
Entry per class:
 D.A specs only -> a combustor model chain is required (2-D unrolled reactive simulation
     with reduced kinetics, days per point on a workstation, or reduced analytical wave
     models); the data uncertainty then DOMINATES: the decisive number is then a
     sensitivity study, not a claim.
 D.B wave-structure profiles (M, angle, entropy handle, swirl vs r and cycle time) on
     Gamma_d -> the certified nominal input of H-1.
 D.C partial experiment (f, n, CTAP, thrust) -> calibrate the model chain's f, n and mean
     pressure; thrust used for the EVALUATOR validation, never for the design.
 D.D mission profile -> S-8 weights. D.E throttle -> multipoint weights.
 D.F declared uncertainty -> interval / distributional propagation of D through the
     adjoint (first order) and through evaluations at the extremes (interval on D).
 D.G coupling map -> S-10; out of the certified nominal answer.
Audits (each with loud reject):
 AU.1 supersonic-through-interface: min over (r, phi) of the normal Mach on Gamma_d >
      1 + delta_M, delta_M = the data's own uncertainty in M (class F, or the model
      chain's validation scatter); reject -> the interface must move downstream or class
      G is mandatory. Physical note (test practice): RDE combustor exits are typically
      near-sonic on average and subsonic over part of the cycle; a straight annulus
      followed by the divergent gives a supersonic interface only after the exit
      expansion; the audit is expected to be TIGHT and must be shown, not asserted.
 AU.2 conservation consistency: cycle-integrated mass and energy flux through Gamma_d vs
      the specs (propellant flow, heat release) to within the flow-meter class (1-2 %).
 AU.3 mode purity: spectral peak at n f and harmonics vs everything else; threshold =
      the noise floor of the trace (measured) x a factor derived from the required
      weight accuracy (weight error propagates linearly to J via dJ/dw from the adjoint).
 AU.4 measurability: only wall pressures (CTAP mean, PCB high-frequency), f, n (camera)
      and thrust are measurable; interface data are ALWAYS model outputs; the audit
      compares the model's wall-pressure prediction with the measured CTAP/PCB.
 AU.5 causal separation: the design must not change the data; verified by evaluating
      the interface state under the two designs with a combustor response model of
      class G if available, else by AU.1 (supersonic interface = causally separated).
Pin magnitudes on the decisive result (provenance = computed in-house, same gas tables):
 PIN-1 pure periodic single mode: mode hop changes the mean interface state by a few %
       [KNOWLEDGE: Bykovskii, Zhdan & Vedernikov 2006 JPP, abstract; own practice] ->
       J shifts by the same order, ABOVE band; but it shifts BOTH designs; effect on D
       is second order and measured by re-evaluating D on a two-mode data set.
       Cost to relax: S-6 class or a two-family robust design (S-8 machinery).
 PIN-2 frozen thermally perfect: frozen vs equilibrium expansion bracket of 1-4 % in Isp
       for 3000 K products with short residence [KNOWLEDGE: textbook, full] -> affects
       absolute J, cancels to first order in D (same gas for both); measured by one
       equilibrium-vs-frozen pair on the final designs. Cost to relax: reacting tables
       (moderate) — not needed for D.
 PIN-3 single phase: no effect for gaseous propellants; for metallized/condensing
       products a two-phase lag loss of several % [KNOWLEDGE: textbook] — out of scope.
Decision criterion: AU.1-AU.5 pass on the decisive instance. Falsifier: AU.1 failing at
any azimuth -> the nominal problem is not causally separated; class G required.
Options: 7 classes + 5 audits = 12.

### SP8 — PROOF (LOAD-BEARING)
Options (layers, all used):
 PR.1 per-solve validity v1-v4 (SP2).
 PR.2 a-posteriori discretization error: GCI on 3 meshes with observed order [KNOWLEDGE:
      Roache 1997/1998, full; ASME V&V 20, abstract]; refinement ratio >= 1.3.
 PR.3 cross-code: legacy Fortran MoC on the mean steady state — agreement within the
      MoC's own characteristic-mesh band (derived by running the MoC at two mesh sizes);
      disagreement beyond it = one of the two is wrong, investigated, never averaged.
 PR.4 experiment anchor of the EVALUATOR: one published nozzle-equipped RDE thrust datum
      (class C) [KNOWLEDGE: Goto et al. 2019 JPP, abstract; Fotia et al. 2016 JPP,
      abstract] reproduced within band_TS(RDE stand) + GCI; miss -> the evaluator is
      not anchored, the number is not quotable.
 PR.5 rejectors for every derivative (SP3), estimator (GCI observed order in range) and
      audit (seeded corrupted data must be rejected).
 PR.6 validated numerics / interval arithmetic: not affordable at 3-D; declared absent.
Reproducibility across (code version, checking procedure, environment): every number
carries the triple's fingerprint; a result is QUOTABLE when its claimed difference exceeds
the sum of its bands PLUS the reproducibility scatter measured by re-running the
rejectors in a second environment (different BLAS/compiler flags) — that scatter is
measured, never assumed; a non-reproducing result is marked FAILING with the offending
component named and the number withdrawn until re-stamped with a cause; never re-stamped
silently.
Uncertainty budget (sum, as §6 demands): band_total = GCI(D) + |dD/dw| delta_w (weights)
+ |D(p_b,max) - D(p_b,min)| (base interval) + |D_frozen - D_eq| (gas pin) + reduction-
error residual on D.
Decision criterion: |D| > 2 x band_total AND > band_TS. Falsifier: any PR layer failing.
Options: 6.

### SP9 — THE DECISIVE RESULT (LOAD-BEARING; pre-registered BEFORE building)
 Configuration: annular RDE, straight annulus, SUPERSONIC interface after the exit
   expansion (AU.1 shown), (case 1) divergent bell attached at the outer lip, length L and
   exit radius fixed; (case 2) truncated plug attached at the inner lip with FIXED
   truncation fraction and base radius (base as input so p_b cancels to first order).
   St deliberately in the marginal range (Delta_phi ~ 0.5-2) where DL-2 leaves room;
   one design point.
 Data class: B + F (declared +-band on M, angle, swirl amplitude and on the weights).
 Comparator: SP-CARM (strongest classical, same L, same exit radius, same base, same
   attachment safety margin taken at the cycle MINIMUM wall pressure).
 Metric: D = [J_3D(S_H1) - J_3D(S_CARM)] / J_3D(S_CARM), both on the SAME R.6 evaluator,
   same meshes, same gas; secondary metric: the per-azimuth attachment margin map of
   S_CARM and S_H1 (minimum margin and violated azimuth fraction).
 Accuracy class: thrust-stand class (0.5-1 %) as the materiality threshold; RDE stand
   reality 2-4 % (DL-4) stated; band_total per SP8.
 Pre-registered outcomes:
   OUT-N (negative): |D| < max(band_TS, 2 x band_total) -> "for a supersonic-interface
     annular RDE at this St, the classical mean-state design is optimal within the
     thrust-stand class; the unsteady-aware road buys no resolvable Isp" — publishable;
     program pivots to S-9 (operability) if the margin map shows S_CARM violated, else to
     S-10 (engine lever).
   OUT-P (positive): D >= 2 x band_total and >= band_TS -> advantage claimed as COMPUTED,
     with the statement that it is at/above the experimental resolution and hence
     testable; generalization bounded to the (configuration, St, interface-Mach class).
   OUT-C (constraint-decisive): |D| small but S_CARM violates attachment at some azimuth
     while S_H1 does not -> the road's worth is operability, testable by PCB wall
     pressure (S-9 decisive).
   OUT-X (no claim): any rejector fires, PR.4 anchor misses, DL-1 symmetry check fails.
 Kill criteria: K1 OUT-N in both cases 1 and 2; K2 reduction error > |D| after one closure
   update; K3 PR.4 miss.
 Sensitivity: dD/dw (adjoint) and D at the weight extremes; D at p_b band extremes
   (case 2); D frozen vs equilibrium tables.
 External anchor: PR.3 (legacy MoC, MoC-mesh band), PR.4 (published RDE nozzle thrust
   datum, RDE-stand band), qualitative field structure vs published RDE-nozzle simulations
   [KNOWLEDGE: Schwer & Kailasanath, abstract].
 Scope of generalization: one design point, one St, two configurations; a 3-value St
   sweep (Omega/2, Omega, 2 Omega at fixed data shape) is the cheapest extension and is
   pre-registered as optional (+1 session).
 Load-bearing: yes. Falsifier of the pre-registration: the audits (SP7) failing on the
   chosen instance before any design is built — then the instance, not the road, changes.
Options: 4 outcomes + 3 kills (enumerated above).

### SP-PB — BASE REGION (local for the decisive instance, load-bearing for plug claims)
Options:
 B.1 constant p_b = k p_a (closed-wake regime) [KNOWLEDGE: Hagemann et al. 1998 JPP,
     full].
 B.2 regime-switching open/closed wake vs pressure ratio [KNOWLEDGE: Ito, Fujii &
     Hayashi 2002 JPP, abstract].
 B.3 base bleed (design option, changes the configuration).
 B.4 inviscid computed recirculation: NOT a base-pressure model (Euler base pressure is
     not physical); declared invalid as an absolute, kept as the flow-domain closure only.
 B.5 RANS base flow per azimuth: validation of B.1/B.2 only.
 B.6 unsteady base response: base cavity time constant tau_b ~ L_b / a ~ 0.02 m / 1000
     m/s = 20 us vs period 30-1000 us -> quasi-steady for f < ~5 kHz, marginal above
     (derived indicator tau_b f; reported per instance).
Materiality (derived): F_base = p_b A_b; with A_b/A_e ~ 0.2-0.4 and p_b ~ 0.3-0.7 p_a at
sea level, F_base ~ 1-5 % of F; a +-30 % uncertainty on p_b -> +-0.3-1.5 % of F = the
band_TS itself. Therefore: the ABSOLUTE plug thrust cannot be resolved better than band_TS
by any base model, but the DIFFERENCE D between two plugs with the same base (fixed
truncation, same p_b band) is resolved to second order: residual = |D(p_b,max) -
D(p_b,min)| entering band_total. Recommendation: B.1 with the interval [k_min, k_max]
from the cited correlation's scatter, base geometry as INPUT; B.6 indicator reported.
Falsifier: the interval width on D exceeding |D| (then case 2 delivers OUT-N by
construction and only case 1 carries the claim).
Options: 6.

### SP-CARM — THE STRONGEST COMPETING PRACTICE (LOAD-BEARING: a weak comparator = worthless number)
What a competent designer fields today:
 C.1 representative state = mass-flux-weighted cycle mean of (p0, T0, M, angle, swirl) on
     Gamma_d, or the EAP state (the steady chamber pressure giving the same ideal thrust)
     [KNOWLEDGE: Kaemming & Paxson 2018, abstract] — EAP is the stronger choice because
     it matches the thrust integral, not the state moments.
 C.2 contour = Rao (bell) / Angelino-Lee (plug) by ROTATIONAL, variable-gamma MoC with the
     mean swirl included [KNOWLEDGE: Zucrow & Hoffman textbook, full], length- and exit-
     radius-constrained (same L, same R_e as the new design: same-budget comparison).
 C.3 attachment: the designer ALREADY checks the worst instant — takes the minimum
     instantaneous wall pressure from the combustor simulation and applies a Stark/
     Schmucker margin, i.e. a truncated-ideal (TIC-like) conservative choice [KNOWLEDGE:
     Frey & Hagemann 1998, abstract; Hagemann et al. 1998, full]. The comparator must be
     given this check (not the naive mean-state check), otherwise OUT-C is an artefact.
 C.4 base: Hagemann-class correlation, same as SP-PB for both designs.
 C.5 duty averaging already practised: mission-averaged area ratio selection (launcher
     practice), EAP for RDEs (emerging), worst-instant attachment check; multipoint
     design at several throttle points (expander-cycle practice). Hence "weighted
     averaging" is NOT novel; the novelty claim of H-1 is bounded to: (i) the DL-1 exact
     rotating-frame evaluation, (ii) the measured closure in the design loop, (iii) the
     contour correction beyond the mean state at finite St, (iv) the certified per-
     instant margin with multiplier. Literature query bounding the novelty claim: "rotating
     detonation" AND ("nozzle design" OR "nozzle optimization") AND ("time-average" OR
     "cycle-average" OR "rotating frame"), 2010-2026, plus the classical variational
     nozzle corpus (Rao, Guderley, Kraiko) — to be run and reported with hit counts.
 C.6 what a designer would NOT accept as comparator: a conical nozzle, a constant-gamma
     Rao, a mean-state design with the mean-state attachment check — all weaker than C.1-
     C.4 and would inflate D.
Recommendation: comparator = C.1(EAP) + C.2 + C.3 + C.4, built with the legacy MoC oracle
(read-only) so that it is INDEPENDENT of the new machinery, then evaluated on R.6.
Decision criterion: the comparator's own KKT within the steady model verified by the
legacy code. Falsifier: a referee naming a stronger classical practice not in C.1-C.5
(e.g. a documented RDE-specific empirical contour correction) — then D is re-run against
it before any claim.
Options: 6.

--------------------------------------------------------------------------------
## ORDER OF BATTLE (dependency order, load-bearing first)
 1. SP-OBJ (fix the question: OBJ.1 + O-c constraint; lever honesty written down).
 2. SP1 with DL-1/DL-2 (decide WHERE the effect can live: supersonic interface, finite St;
    measure Delta_phi and the closure on a first instance).
 3. SP7 audits AU.1-AU.5 on the candidate instance (if AU.1 fails the instance changes).
 4. SP-CARM (build the comparator FIRST with the legacy oracle; freeze it).
 5. SP9 pre-registration (outcomes, kills, bands) — written before any design run.
 6. SP5 + SP2 (evaluator R.6/F.3 built and validated: PR.1-PR.4; pricing of the 3 h window).
 7. SP-PB (base interval fixed as input; B.6 indicator).
 8. SP3 (adjoint + rejector passing on the comparator geometry).
 9. SP6 (family and certificates).
10. SP4 (continuation from the comparator, KKT, family gap).
11. SP8 (budget summed, reproducibility scatter measured in a second environment, quote
    or withdraw).
Session pricing: 1-2 (steps 1-5), 3-4 (step 6), 5 (steps 7-9), 6-7 (step 10 + decisive
runs), 8 (step 11 + optional St sweep), 9 (write-up). At the budget edge; the 3-D
evaluator throughput is the declared risk (SP2 pricing).

--------------------------------------------------------------------------------
## WHAT WOULD MAKE THIS LENS CHANGE ROAD (consolidated)
 M-1 Measured phase lag Delta_phi < the SP1 threshold AND choked interface -> DL-2 rules:
     the answer is negative by lemma; pivot to S-10 (engine lever) / S-9.
 M-2 Reduction error |J_3D - J_axi| on the final designs > |D| -> design loop to S-3.
 M-3 Adjoint rejector firing across the captured discontinuity at the optimum -> S-7.
 M-4 AU.1 failing at every admissible interface station -> class G mandatory, S-10.
 M-5 DL-1 symmetry check failing (time-accurate drift) -> the pin is false at the
     design point; robust layer first.
 M-6 Evaluator missing the published thrust datum beyond band -> no anchor, no claim
     until the evaluator is repaired.
