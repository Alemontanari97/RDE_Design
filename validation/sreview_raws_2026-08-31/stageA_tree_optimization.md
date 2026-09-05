# STAGE A — INDEPENDENT DERIVATION TREE — lens: numerical optimization & uncertainty quantification

Inputs read: `PROBLEM_STATEMENT_agnostic.md`, `DERIVER_BRIEF_agnostic.md` (this directory) — nothing else.
Independence: no other file, directory, log, registry or source of the repository was opened.
Rigor tags: THEOREM / THEOREM(closure) / SCHEMA / CONJECTURE / PRACTICE. Knowledge tags: [KNOWLEDGE: author year] [full|abstract|title].
Notation: f = wave passage frequency at a fixed azimuth, n = wave count, T = 1/f, pattern angular speed W = 2*pi*f/n,
L = nozzle length, u = product axial speed, St = f*L/u (residence time / period), R = chamber radius,
eps = relative amplitude of the inflow variation over the cycle (measured, not assumed), b_TS = thrust-stand band (0.5-1 % of F).

--------------------------------------------------------------------------------------------------
## 0. DRY-LEVEL LEMMAS USED THROUGHOUT (each with hypotheses; each is a fork-decider)
--------------------------------------------------------------------------------------------------

L1  ROTATING-FRAME STEADINESS AND INSTANTANEOUS THRUST CONSTANCY — THEOREM under the wave pin.
    Hyp: pure periodic single-mode wave with n identical waves; ONE fixed axisymmetric nozzle; the flow
    solution in Omega(S) is the periodic response (exists, is the one selected by the declared solution class).
    Then the lab-frame field depends on (x, r, theta - W t) only, i.e. it is STEADY in the frame rotating at W,
    with azimuthal period 2*pi/n. Consequences: (a) on ANY axisymmetric control surface the thrust
    F_S(t) = integral over theta of a function of (theta - W t) is CONSTANT IN TIME: J_true = F_S(t) for every t,
    no limit, no liminf/limsup bracket needed; (b) J_true equals the thrust of the steady rotating-frame (RF)
    3D sector solution; (c) side loads are NOT constant (they rotate at W) — operability objective O-c is
    genuinely unsteady, O-a is not. Falsifier: a lab-frame time trace of thrust from a 3D unsteady solve of a
    pinned-family case that is not constant beyond discretization noise (measured, SP8) => the solution is not
    in the pinned class (mode content), and the audit must reject the data, not the lemma.

L2  JENSEN-GAP BOUND ON THE GAIN OF WEIGHTED-MULTIPOINT OVER MEAN-STATE DESIGN — THEOREM under hypotheses.
    Let F_k(S) = thrust of the steady axisymmetric solution with inflow state u_k, weights w_k >= 0, sum w_k = 1,
    J_2(S) = sum_k w_k F_k(S) (quasi-steady cycle average), J_1(S) = F(S; u_bar) with u_bar = sum_k w_k u_k
    (mean-state design), both on the same admissible set A. Hyp: u -> F(S;u) is C^2 on the convex hull of the
    data for every S in A with second derivative bounded by H(S). Then |J_2(S) - J_1(S)| <= (1/2) H(S) Var_w(u)
    =: delta(S) (the first-order term vanishes because u_bar is the w-mean). For maximizers S_1*, S_2*:
    0 <= J_2(S_2*) - J_2(S_1*) <= delta(S_2*) + delta(S_1*) <= 2 sup_A delta.
    The gap delta(S) is COMPUTABLE WITHOUT DERIVATIVES at any S by K+1 steady solves. Hence a SCREEN exists:
    if 2*max(delta over a few designs) < b_TS, the O-a advantage of any quasi-steady-aware shape design over the
    mean-state design is unresolvable at thrust-stand accuracy — a negative answer certified before optimizing.
    Caveats (stated, load-bearing): (i) if the competitor uses a different average (mixed-out), a first-order
    term sum_k w_k D_uF (u_k - u_bar') appears and is O(eps) — this is exactly "which average" (SP-CARM);
    (ii) the bound is on the OBJECTIVE; per-instant state constraints change the FEASIBLE SET and can produce
    first-order differences (SP-OBJ); (iii) RDE eps is not small (pressure swings of order unity) so delta may
    be large — the screen is a computation, not a prejudice.

L3  WEIGHT SENSITIVITY IS FREE — trivial THEOREM. In any weighted formulation dJ/dw_k = F_k(S): the sensitivity
    of the decisive difference to the data weights is obtained at zero cost from the values already computed.

L4  PLACEMENT OF THE REDUCED MODELS — SCHEMA. The locally-axisymmetric quasi-steady model (each azimuth = an
    independent axisymmetric nozzle with that phase's inflow) is justified only when (a) St << 1 (pattern rotates
    by 2*pi*St/n during transit) AND (b) azimuthal communication within the axial Mach cone is negligible:
    ell_theta / L >> 1/M_x with ell_theta the azimuthal scale of the inflow pattern. Detonation fronts are sharp
    (ell_theta << 2*pi*R/n), so (b) fails locally for any RDE data; the loss is a MEASURED quantity (SP5), never an
    asymptotic zero. The mean-state model has NO asymptotic regime in St; it is an averaging closure whose
    error is delta(S) of L2 plus the same 3D loss. Consequence: the RF-3D steady solution (L1) is the only
    representation that is exact under the pins, and it must be the EVALUATOR whatever the design loop uses.

L5  ATTACHMENT MAKES THE FEASIBLE SET PHASE-DEPENDENT — SCHEMA. With a wall-pressure separation criterion
    p_w >= p_crit(M_w) * Pa applied at every cycle phase, the binding phase is the lowest-pressure one; a
    mean-state design that is attached on average can be separated at that phase. A shape that satisfies the
    per-phase constraint typically has a smaller area ratio or a different terminal slope: this is a FIRST-ORDER
    change in S (not O(eps^2)), so the operability-constrained problem is where an unsteady-aware road can buy
    something at first order — and also where a competent designer already iterates by hand (SP-CARM).

--------------------------------------------------------------------------------------------------
## LEVEL 0 — SP0 STRATEGIES (tuple = objective; time treatment; spatial representation; solver & information;
## search & guarantee; decisive result). Open enumeration; nothing rejected by omission.
--------------------------------------------------------------------------------------------------

### S1  PRACTICE OF TODAY — mean-state classical design + a posteriori unsteady check  (rank 12 as a road; it is the baseline)
tuple: O-a proxy at design point | time: one representative mean inflow state (arithmetic or mixed-out average) |
axisymmetric steady | MoC / Rao-type variational contour, legacy code, information = none (closed form or 1-2 parameter sweep)
[KNOWLEDGE: Rao 1958 exhaust nozzle contour for optimum thrust] [abstract] | search: classical variational optimum for the
single state (local, exact for that model) | decisive result: none (it is the thing to beat).
question answered: a narrowing (design for a steady surrogate). cost: days; no new theory. generality: bell native; plug via
plug-MoC variants; classes A-B only (needs a mean state). pins needed: none beyond frozen gas. pins relaxed: wave pin irrelevant.
falsifier as a road: none (unfalsifiable by construction: it makes no claim about J_true). time-to-number: hours.
abandon measurement: not applicable — it is retained forever as the control arm.
decisive result: serves as CONTROL in every other strategy's decisive result.

### S2  TUNED CLASSICAL — mean-state design + per-phase separation check + designer's sweep of area ratio/length  (rank 11 as a road; THE comparator, see SP-CARM)
tuple: O-a with O-c checked | time: mean state for design, K phase states for the check | axisymmetric steady | steady Euler or
MoC per state; information = 1-2 scalar sweeps | search: manual/1-D line search over area ratio (local, best-effort) |
decisive: none. question: narrowing. cost: 1-2 sessions. generality: bell/plug; classes A-C. pins: frozen gas.
falsifier: none as road. time-to-number: 1 session. abandon: n/a. Reason it exists: L5 — a competent designer already fixes
the separated phase by shrinking area ratio; any new road must beat THIS, not S1.

### S3  WEIGHTED-MULTIPOINT QUASI-STEADY AXISYMMETRIC ADJOINT DESIGN (QS-2D)  (rank 4 stand-alone; rank 1 as the DESIGN LOOP of S7)
tuple: O-a (cycle mean via quadrature over the cycle) s.t. per-phase attachment (O-c as constraint) | time: quadrature nodes
u_k on the cycle with weights w_k (trapezoid on a periodic cycle: spectrally convergent for smooth data, K derived from the
tail of the quadrature error, SP1) | axisymmetric steady per node | steady axisymmetric Euler FV, thermally-perfect table;
discrete adjoint by AD; information = exact gradient of the discrete J and of the KS-aggregated constraint | search: SQP /
trust-region with adjoint gradients, multistart over configuration seeds; guarantee = KKT-certified local optimum of the
DISCRETE reduced model + multistart dispersion statistic | decisive: Delta_QS = J_RF3D(S_3*) - J_RF3D(S_2*) with bands.
question: Q0 narrowed to "St small enough that the reduced model's error term (measured by RF-3D) is below band".
cost: solver + adjoint + verification 3-4 sessions; theory: none new (weighted multipoint is standard aero practice
[KNOWLEDGE: multipoint airfoil/wing design, e.g. Drela 1998 "Pros and cons of airfoil optimization"] [abstract]).
generality: bell/plug/ED via parametrization + base closure; classes A-G (A needs a generator; D-E add nodes; F adds outer
weights; G adds a fixed point). pins needed: frozen thermally-perfect (solver table), wave pin (weights), single phase.
pins relaxed: could take mode-mixture weights (class F) at no structural cost (L3).
falsifier: RF-3D evaluation of S_3* shows |J_RF3D - J_QS| > b_TS on the design itself (reduction error above band) => the
reduced model is not a licensed design surrogate at this St. time-to-number: 4-5 sessions.
abandon measurement: measured reduction error |J_RF3D(S) - J_QS(S)| / F > b_TS at the design point AND the trust-region
correction of S7 fails to converge in the session budget.
decisive result: pre-registered Delta_QS vs S2 on a bell, class B, at measured St, with the three outcomes of SP9.

### S4  ROTATING-FRAME STEADY 3D SECTOR ADJOINT DESIGN (RF-3D)  (rank 2)
tuple: O-a exact under pin (L1) s.t. attachment at every azimuth (= every phase) | time: eliminated exactly by the frame
change (steady with Coriolis/centrifugal sources) [KNOWLEDGE: rotating-frame steady Euler/RANS in turbomachinery, textbook,
e.g. Lakshminarayana 1996] [abstract] | 3D sector 2*pi/n with periodic BC | 3D steady Euler FV, discrete adjoint by AD
[KNOWLEDGE: turbomachinery adjoint in rotating frames, e.g. Wang & He 2010] [abstract] | search: SQP/trust-region, local KKT |
decisive: Delta_RF = J_RF3D(S_4*) - J_RF3D(S_2*).
question: Q0 itself at the design point (no reduction error term; remaining terms: discretization, data, gas model).
cost: 3D solver+adjoint on a workstation: 1e6-cell sector, O(1e2-1e3) s per steady solve if the kernel is compiled/vectorized,
same for adjoint; 50-100 design iterations => 10-50 h — exceeds the 3 h/session decisive-run cap unless coarse grids are used in
the loop (=> multi-fidelity S7). theory: none new; exactness by L1. generality: all configurations; classes A-G.
pins needed: wave pin (essential: without single-mode periodicity there is no rotating frame), frozen gas. pins relaxed: none.
falsifier: (a) a pinned-family 3D unsteady time-marching solve of S_4* whose time-mean thrust differs from J_RF3D by more than the
discretization band (L1 broken by the solver, e.g. non-uniqueness); (b) cost exceeds session budget without a converged design.
time-to-number: 6-8 sessions. abandon: wall-clock of one converged RF-3D adjoint step > 20 min on the workstation (then 100 steps
do not fit 3 sessions of decisive runs). decisive result: as S3 but with no reduction-error term.

### S5  BRUTE FORCE — 3D unsteady time-marching + unsteady (checkpointed) adjoint  (rank 9)
tuple: O-a as a long-time average | time: resolved | 3D full annulus | unsteady Euler FV, unsteady adjoint with checkpointing
[KNOWLEDGE: Griewank & Walther 2000 revolve] [abstract] | search: gradient, local | decisive: same as S4.
question: Q0 without the wave pin (also covers mode hopping if data provide it). cost: HPC-class (memory of trajectories,
periodic-orbit sensitivity issues); person-time 10+ sessions. generality: maximal. pins needed: none (frozen gas only).
pins relaxed: wave pin. falsifier: sensitivities of long-time averages of chaotic/quasi-periodic flows do not converge
(known pathology; for strictly periodic pinned data it is benign). time-to-number: > budget. abandon: any run above the 3 h
cap for a single evaluation. decisive result: reserved as the EXTERNAL ANCHOR (one run per final design, SP9), never the loop.
Rejected as the road for a stated reason: budget (§8) and redundancy with S4 under the pin (L1).

### S6  HARMONIC BALANCE / TIME-SPECTRAL in the lab frame with azimuthal Fourier modes  (rank 6)
tuple: O-a | time: N harmonics of f | 3D via (x,r) x azimuthal modes | HB steady solver [KNOWLEDGE: Hall, Thomas & Clark 2002;
Gopinath & Jameson 2005 time-spectral] [abstract] with adjoint | local | decisive as S4.
question: Q0 at design point. cost: comparable to S4; more implementation (coupled harmonics). generality: as S4.
pins needed: wave pin (harmonic content of a single f). pins relaxed: could take 2 incommensurate frequencies (counter-rotating
pairs) at multi-frequency HB cost. falsifier: harmonic truncation error above band (measured by N-refinement).
time-to-number: 7+ sessions. abandon: N needed for band-level convergence > sector-grid azimuthal resolution equivalent
(then S4 is cheaper for the same accuracy). Reason not top: under the pin S6 is mathematically S4 in a Fourier basis, at
higher implementation cost; kept as the road if the wave pin is relaxed to two modes.

### S7  MULTI-FIDELITY HYBRID (TOP, rank 1): Jensen screen -> QS-2D adjoint design loop under trust-region model management
###     with RF-3D corrections -> RF-3D evaluator -> paired comparison with common closures and control-variate bands
tuple: O-a s.t. per-phase attachment; robustness (O-b) and tolerance (O-d) as declared outer layers | time: DESIGN loop = quadrature
over the cycle (S3); EVALUATION = exact rotating frame (L1) | DESIGN = axisymmetric steady per node; EVALUATION = RF-3D sector |
adjoint of the QS-2D model; RF-3D value (and optionally RF-3D gradient at low resolution) used as trust-region corrections
[KNOWLEDGE: Alexandrov, Lewis et al. 1998-2001 first-order corrected trust-region model management] [abstract]; multi-fidelity
control variates for the bands [KNOWLEDGE: Peherstorfer, Willcox & Gunzburger 2018 survey] [abstract] | search: SQP/TR with
corrected model; guarantee = KKT of the corrected model at the RF-3D-evaluated point (first-order consistent at the iterate),
multistart over configuration seeds, gap statement "local, multistart dispersion d, no global claim" | decisive: paired
Delta = J_RF3D(S_7*) - J_RF3D(S_2*) with the band budget of SP9, after the L2 screen.
question: Q0 at a design point + a MAP of when it pays (St, eps) via the screen, at workstation cost.
cost: S3 cost + one RF-3D solver (no adjoint mandatory) + verification: 6-8 sessions. theory: L1-L5 (all short).
generality: bell/plug/shrouded/ED via parametrized wetted contour + base closure; classes A-G. pins needed: wave, frozen gas,
single phase; the wave pin is needed by the evaluator; the design loop tolerates mode-mixture weights (L3).
pins relaxed: class F mode uncertainty enters as weights on the design side; the evaluator then reports per-mode RF-3D values.
falsifier: the corrected trust-region loop does not converge (the 2D model is not first-order-trustworthy: RF-3D corrections
oscillate); or the screen bound 2*delta < b_TS (then the O-a road is over BEFORE any optimization — a valid negative answer).
time-to-number: screen: 1 session; full: 7-8 sessions.
abandon measurement: (a) 2*max delta(S) < b_TS at the comparator design and its perturbations => abandon O-a shape road,
switch to S10 (operability) or publish the negative result; (b) measured reduction error of the QS-2D model on S_2* above
b_TS with TR corrections not converging in 2 sessions => switch the design loop to S4.
decisive result: pre-registered in SP9 (bell, class B, comparator S2, metric = cycle-mean thrust at fixed mass flow, exit radius,
length; accuracy class b_TS; outcomes (+), (0), (-)).

### S8  DERIVATIVE-FREE / BAYESIAN OPTIMIZATION over a low-dimensional shape space, any evaluator (RF-3D direct)  (rank 5)
tuple: O-a or O-b | time: whatever the evaluator does (RF-3D exact) | 3D | evaluator values only; GP surrogate + expected
improvement [KNOWLEDGE: Jones, Schonlau & Welch 1998 EGO] [full]; constraints via probability-of-feasibility | search: global
in the surrogate sense (no certificate; regret bounds need GP-hypothesis) | decisive as S4.
question: Q0 restricted to d <= ~10 design parameters. cost: RF-3D evaluations O(10 d) - O(50 d): for d = 8 and 5 min/solve,
~3-7 h (fits 2-3 sessions). generality: all configurations; needs no adjoint => the simplest way to get an RF-3D-exact design.
pins: wave (evaluator). falsifier: EI stagnation with GP posterior variance not decreasing (surrogate misspecified: shocks
make J non-smooth in some parameters). time-to-number: 3-4 sessions once the RF-3D solver exists.
abandon: d needed for a competitive contour (from the QS-2D loop's active parameter count) > 12. Role in S7: the GLOBAL
cross-check of the local KKT optimum in the reduced parameter space (SP4).

### S9  ROBUST DESIGN OVER AN ENVELOPE (O-b) — changes the objective  (rank 7; the class D-F extension of S7)
tuple: O-b (weighted envelope mean, or mean - k*std, or CVaR of thrust over D-F data) | time as S7 | as S7 | as S7 with
outer quadrature/PCE over envelope parameters [KNOWLEDGE: Xiu & Karniadakis 2002 gPC] [abstract] | search local |
decisive: envelope-integrated Delta vs S2 (S2 designed at the nominal point).
question: Q0 for a mission (needs classes D-F). cost: S7 x (number of outer nodes). generality: full. pins: as S7.
falsifier: the envelope optimum coincides with the nominal optimum within band (robustness is free) — then O-b adds nothing.
time-to-number: S7 + 2 sessions. abandon: outer-node count for band-level convergence > 8 with sparse grids (cost blows the
session cap). Reason not top: needs richer data than the certified nominal answer; ordered after the design-point verdict.

### S10 OPERABILITY-FIRST (O-c) — changes the objective: maximize separation margin s.t. thrust >= (1 - b_TS) F_ref  (rank 3)
tuple: O-c primary | time: per-phase (all phases bind) | QS-2D + RF-3D check | adjoint of the KS margin | local KKT |
decisive: margin gain at equal thrust, or thrust gain at equal margin (Pareto point).
question: Q0 with the referee's objection "thrust is not the lever" taken seriously (L5: first-order effects live here).
cost: as S7 (same machinery, swapped objective/constraint). generality: full. pins: as S7. falsifier: the Pareto front is
flat (margin costs nothing) => operability is not a design lever either. time-to-number: S7 + 1 session.
abandon: measured margin at S_2* already > the as-built tolerance-induced margin loss (nothing to gain).
Placement: the FALLBACK if the L2 screen kills O-a; also the second decisive number if budget allows.

### S11 TOPOLOGY AS OUTPUT — level-set / phase-field shape-topology optimization of S in E  (rank 10)
tuple: O-a | as S7 | axisymmetric (QS) or RF-3D | Euler adjoint with immersed/cut-cell solid representation
[KNOWLEDGE: Allaire, Jouve & Toader 2004 level-set shape optimization] [abstract] | local, mesh-dependent |
decisive: a topology not in the input catalogue that beats the best catalogue member above band.
question: Q0 with configuration as an output. cost: new solver infrastructure (cut cells + adjoint), 5+ sessions; theory:
existence needs perimeter/curvature regularization (SCHEMA). generality: by construction maximal. pins: as S7.
falsifier: every level-set optimum lands in the bell/plug/shrouded/ED catalogue (then a TOURNAMENT over the catalogue is
equivalent and cheaper). time-to-number: > budget. abandon: any cut-cell solve failing the a-posteriori validity checks
(SP8) at the shocks. Rejected for the decisive answer for a stated reason: budget; replaced by "topology by tournament"
(SP6 P.6) which is exact for a finite catalogue.

### S12 COUPLED CHAMBER-NOZZLE DESIGN (class G) — changes the design variables' effect  (rank 8)
tuple: O-a of the ENGINE (nozzle back-pressure changes chamber pressure, fill, wave speed via a reduced response map) |
time: as S7 with a fixed-point on the map | as S7 | S7 + fixed-point derivative (implicit function theorem) | local |
decisive: engine-level Delta.
question: Q0 at engine level. cost: S7 + the response map (class G data) + 1 session. generality: full. pins: wave pin
must survive the coupling (mode count fixed under back-pressure change — an AUDIT item). falsifier: the coupling derivative
d(chamber state)/d(back pressure) x nozzle sensitivity is below band => decoupled answer stands. time-to-number: S7 + 1-2.
abandon: measured coupling term below b_TS/10 at the design point (then it is a band term, not a design lever).

### S13 BOUND-ONLY / NEGATIVE-RESULT ROAD — compute the L2 screen and the L5 feasible-set difference, publish the bound  (rank 3-bis: mandatory first step of S7, and a complete answer on its own if it kills)
tuple: O-a | time: quadrature | axisymmetric | K+1 steady solves, no adjoint | no search | decisive: 2*sup delta vs b_TS.
question: "can any unsteady-aware shape design buy O-a above band at this St/eps?" — the referee's real first question.
cost: 1 session after the 2D solver exists. generality: all configurations, classes B+. pins: wave (weights), frozen gas.
falsifier: delta(S) varies by more than itself across perturbed designs (then sup_A delta is not estimable from a few points
and the bound is not certifiable — measured by evaluating delta on the multistart seeds). time-to-number: 1 session.
abandon: n/a (it is a computation). decisive result: the bound itself, with its provenance, if it is below band.

### S14 DATA-DRIVEN CALIBRATION ROAD (class C) — Bayesian calibration of the wave model, then any of S3/S4/S7  (rank 7-bis, a data layer)
tuple: as chosen road | time: as road | as road | + Bayesian calibration of wave-model parameters against pressure traces
and thrust [KNOWLEDGE: Kennedy & O'Hagan 2001] [abstract] | as road | decisive: posterior-predictive Delta with data band.
question: Q0 with measured data. cost: + 1-2 sessions; needs class C. pins: wave pin becomes a posterior over modes.
falsifier: posterior on eps/weights so wide that the band swallows Delta. time-to-number: road + 2. abandon: no class C data.

RANKING SUMMARY (recommendation): 1 S7 | 2 S4 | 3 S10 (fallback objective) and S13 (mandatory screen) | 4 S3 | 5 S8 |
6 S6 | 7 S9, S14 | 8 S12 | 9 S5 | 10 S11 | 11 S2 (comparator) | 12 S1 (baseline).
The ranking is DECIDED by two measured numbers, not by preference: the L2 screen value 2*delta/F versus b_TS, and the
QS-2D reduction error |J_RF3D - J_QS|/F on S_2* versus b_TS (SP1/SP5 decision criteria).

--------------------------------------------------------------------------------------------------
## LEVEL 1 — SUB-PROBLEM TREES for S7 (where S4/S10 differ it is said)
--------------------------------------------------------------------------------------------------

### SP-OBJ  OBJECTIVE  — LOAD-BEARING
Options:
 OBJ.1 O-a cycle-mean thrust at a design point, unconstrained by attachment. Cost min. Risk: separated designs win on paper
       (Euler cannot see separation) — referee kills it. Falsifier: winning design violates the per-phase criterion.
 OBJ.2 O-a s.t. per-phase attachment (g_sep <= 0 at every phase), fixed mass flow, length, exit radius; O-d as bounds.  [RECOMMENDED]
 OBJ.3 O-c primary, thrust as a constraint (S10). First-order lever per L5; referee may prefer it if the nozzle is not the
       engine's thrust lever.
 OBJ.4 O-b envelope robust objective (S9): needs classes D-F.
 OBJ.5 Specific impulse instead of thrust: identical under fixed mass flow (the data fix the mass flow through Gamma_d
       when the interface is supersonic) — degenerate with OBJ.2; if the interface is subsonic the closure changes the mass
       flow and Isp must be used (SP7 audit decides).
 OBJ.6 Engine-level objective (S12, class G).
Recommendation: OBJ.2 for the certified nominal answer; OBJ.3 pre-registered as the fallback that consumes the same machinery.
Is the nozzle the lever? Dry argument: thrust = m_dot * c* * C_F; the nozzle acts only through C_F. Nozzle contour effects at
fixed area ratio are of order 1 % of C_F for well-designed bells [KNOWLEDGE: textbook, Sutton & Biblarz, divergence/contour
losses ~1-2 %] [abstract]; combustor-side RDE losses (parasitic deflagration, incomplete mixing, mode effects) are reported at
several to tens of % [KNOWLEDGE: RDE reviews, e.g. Anand & Gutmark 2019] [abstract]. So the honest expectation is that the
O-a nozzle lever is of the ORDER OF THE BAND; that is precisely why the L2 screen and the band budget must be the first
deliverables, and why the referee will accept OBJ.2 only with the screen number attached ("the lever is X % at this St").
Decision criterion: (i) the screen 2*delta/F vs b_TS; (ii) whether S_2* violates per-phase attachment (then OBJ.2's feasible
set differs from S2's at first order and the road has something to buy). Falsifier of the recommendation: screen below band AND
S_2* attached at every phase => OBJ.2 has nothing resolvable; switch to OBJ.3.
Options count: 6.

### SP1  TIME  — LOAD-BEARING
Measurement of St: residence time tau_res = axial transit time of the mass-averaged streamline from Gamma_d to the exit in the
S_2* mean-state solution (computed, not L/u by hand); St = f * tau_res; also the pattern rotation during transit
dTheta = 2*pi*St/n, and the azimuthal-communication number C_theta = (1/M_x) * L / ell_theta with ell_theta measured as the
azimuthal half-width of the pressure peak on Gamma_d (L4).
Options for the DESIGN loop:
 T.1 Single mean state (S1/S2). Error: delta (L2) + 3D loss. No St requirement claimed; no justification.
 T.2 Weighted quadrature over the cycle (quasi-steady multipoint, S3/S7).  [RECOMMENDED for the loop]
     Node count K: trapezoid rule on the periodic cycle; K chosen by the measured decay of |J_K - J_2K| until
     |J_K - J_2K| <= b_TS/10 * F (a tenth of the band so the quadrature term is negligible in the budget — derived, SP9).
     For data with a sharp front, convergence is algebraic; a graded (non-uniform) node set on the front is derived from
     the pressure-trace derivative (nodes ~ arc-length in log p). Requirement: reduction error measured by RF-3D below band.
 T.3 Rotating-frame steady 3D (exact under pin, S4). Requirement: single-mode data (audit); cost.
 T.4 Time-resolved unsteady (S5). Requirement: none; cost > budget.
 T.5 Harmonic balance (S6): requirement: harmonic content converges.
 T.6 Frequency-domain LINEARIZED unsteady about the mean (small-eps perturbation) [KNOWLEDGE: linearized harmonic
     methods, Hall & Crawley 1989] [abstract]: gives the O(eps^2) term of L2 analytically; invalid at RDE eps ~ O(1).
     Falsifier: measured eps (pressure swing / mean) > 0.3.
Options for the EVALUATION of competing designs:
 T.E1 RF-3D steady sector (exact under pin) [RECOMMENDED]; T.E2 unsteady 3D anchor (once); T.E3 QS-2D itself (only as a
 self-consistency check; never as the evaluator: a model cannot grade itself).
Decision criterion: measured St, dTheta, C_theta, and DIRECTLY the reduction error r_red = |J_RF3D(S) - J_QS(S)|/F on S_2* and
on S_7*: if r_red <= b_TS/3 the QS loop is licensed without corrections; if b_TS/3 < r_red <= b_TS use TR corrections; if
r_red > b_TS switch the loop to T.3 (S4). The thresholds are derived from the band budget (three terms sharing b_TS equally).
Falsifier: r_red measured above band on either design => T.2 rejected for the loop at this instance.
Options count: 6 (+3 evaluation).

### SP2  FLOW MODEL AND SOLVER  — LOAD-BEARING
Options:
 F.1 Legacy MoC (steady, single state, characteristic): oracle only (constant-gamma or its own gas model: audit); cannot take
     captured shocks in the core, cannot do RF-3D. Role: cross-check of single-state values and of the S2 comparator.
 F.2 Steady axisymmetric Euler, finite-volume, shock-capturing (HLLC/Roe with entropy fix), 2nd-order MUSCL, pseudo-time
     implicit or multigrid; thermally-perfect gas via tabulated h(T), cp(T) with monotone interpolation; AD-differentiable
     implementation.  [RECOMMENDED for the loop]
 F.3 Same in 3D sector, rotating frame (Coriolis/centrifugal source terms; periodic BC on the sector faces).  [RECOMMENDED evaluator]
 F.4 Space-marching (steady supersonic, marching in x) where M_x > 1 everywhere: 10-100x cheaper than F.2/F.3; requires the
     axial Mach on Gamma_d > 1 pointwise (audit); fallback to F.2 upstream of the sonic line otherwise. Falsifier: any M_x <= 1
     cell inside the marched region.
 F.5 High-order DG with shock sensors: better convergence order, more code; not needed at band-level tolerance.
 F.6 Unsteady 3D FV (anchor).
Discontinuities: captured (weak solutions) in the loop; a posteriori checks: (a) Rankine-Hugoniot residual across detected
shock cells below the discretization band; (b) entropy inequality cellwise (reject expansion shocks); (c) contact/slip surface
carrying the stratification: check that entropy/composition handle is transported without spurious pressure jumps
(pressure continuity across contacts within band); (d) free plume boundary for plug solids: captured as a contact between
products and ambient at Pa with an ambient buffer region in E (the buffer's outer state = Pa, quiescent; audit that the buffer
does not choke the plume: outflow supersonic on the buffer exit).
Attachment constraint: Euler has no separation; use a wall-pressure criterion g_sep = max over wall stations and phases of
[p_crit(M_w)*Pa - p_w] with p_crit from a stated correlation [KNOWLEDGE: Stark 2005 separation criterion p_sep/Pa ~ 1/(1.88 M - 1);
Summerfield-type p_w/Pa ~ 0.35-0.4 rule, textbook] [abstract]; smoothed by Kreisselmeier-Steinhauser aggregation with
rho_KS derived so that the KS overestimate ln(N)/rho_KS <= b_TS/10 * (typical p_crit*Pa) (derived from the aggregation bound,
N = number of wall stations x phases). Separated designs are INFEASIBLE, not evaluated: the search never trusts an Euler solve
of a separated state (SP4). Base region: SP-PB.
Recommendation: F.2 (loop) + F.3 (evaluator) + F.1 (oracle) + F.4 as an accelerator when the audit permits.
Decision criterion: verification suite (SP8) passes on exact solutions; RH/entropy residuals below band on every used solve.
Falsifier: a used solve failing (a)-(d) is discarded and the design step rejected (search sees a failed evaluation).
Options count: 6.

### SP3  INFORMATION FOR THE OPTIMIZER  — LOAD-BEARING
Options:
 I.1 Finite differences: cost d+1 solves per gradient; noise floor from solver tolerance; used as REJECTOR, not as gradient.
 I.2 Complex-step: exact to roundoff for real-analytic code; tables and min/max limiters break analyticity (needs care); used as
     second rejector where applicable.
 I.3 Discrete adjoint by algorithmic differentiation of the FV solver (reverse mode, fixed-point adjoint of the pseudo-time
     iteration) — exact gradient of the DISCRETE J.  [RECOMMENDED]
 I.4 Continuous adjoint with shock/contact jump conditions [KNOWLEDGE: Giles & Pierce 2001, analytic adjoint with shocks]
     [abstract]: elegant, mesh-independent, more theory; discrepancy vs I.3 is itself a discretization-error indicator.
 I.5 Surrogate gradients (GP/PCE): for S8 only.
 I.6 Derivative-free (no information): S8.
Behaviour across discontinuities: the discrete adjoint of a shock-capturing scheme is consistent with the discrete J; for
INTEGRAL functionals (thrust) the discrete gradient converges under refinement (SCHEMA; verified by the grid study of SP8);
for pointwise functionals it need not. The attachment constraint uses wall pressure (pointwise!) => aggregate with KS and
verify its gradient convergence separately. Design derivatives of the free plume boundary pass through the captured contact:
the same discrete-consistency argument, with an extra rejector (I.1 on a base-pressure functional).
REJECTABLE tests (derived tolerances):
 (i) Taylor-remainder slope test: e(h) = |J(x+h d) - J(x) - h g.d|; fit slope on h in [h_min, h_max] with h_min derived from the
     roundoff floor h_min = (eps_mach * |J| / |g.d|)^(1/2) x 10 and h_max from the smallest active length scale of the
     parametrization; PASS iff slope in [1.8, 2.2]; a wrong gradient gives slope 1 (rejects); the interval width is set by the
     measured curvature of e(h) at the floor (reported).
 (ii) Dot-product (adjoint-consistency) test: |<lam, A v> - <A^T lam, v>| <= c * N * eps_mach * ||A|| ||v|| ||lam|| with c = 10;
     rejects a transposition bug at any level.
 (iii) Cross-oracle: single-state sensitivity of thrust to exit area from the legacy MoC (F.1) vs the FV adjoint on the same
     state: agreement within the sum of the two discretization bands (SP8), otherwise REJECT one of the two (adjudicate by grid
     refinement).
 (iv) Direction-of-descent check inside the optimizer: every accepted step must decrease the merit function by at least the
     Armijo fraction predicted by g; three consecutive failures = gradient rejected, run halted.
Recommendation: I.3 with I.1/I.2 as rejectors, I.4 as a cross-check if time allows. Decision criterion: tests (i)-(iv) pass on
the baseline, on a shocked case and on a plug case with plume. Falsifier: any test failing on the used configuration.
Options count: 6.

### SP4  SEARCH STRATEGY AND GUARANTEE  — LOAD-BEARING (for R-i/R-ii)
Options:
 G.1 SQP with quasi-Newton (BFGS on the reduced space) + adjoint gradients; KKT report with multipliers.  [RECOMMENDED core]
 G.2 Trust-region model management (first-order corrected QS-2D model, RF-3D value corrections; ratio test rho for
     acceptance) [KNOWLEDGE: Alexandrov et al.] [abstract].  [RECOMMENDED wrapper when r_red > b_TS/3]
 G.3 Multistart from configuration seeds (bell/plug/shrouded/ED x 2-3 area-ratio seeds); dispersion statistic; Bayesian
     stopping rule [KNOWLEDGE: Boender & Rinnooy Kan 1987] [abstract] as a "probability of an unfound better basin" heuristic
     (declared PRACTICE).  [RECOMMENDED]
 G.4 Global surrogate cross-check (S8: GP/EI over the active reduced parameters).  [RECOMMENDED as a check]
 G.5 Branch-and-bound / interval methods on a polynomial surrogate: gives a certified gap w.r.t. the SURROGATE only; the gap
     to the PDE optimum remains uncertified — rejected as a certificate for a stated reason (it certifies the wrong object).
 G.6 Evolutionary / population: no certificate, high cost; rejected for the decisive answer, allowed for seeding.
 G.7 Homotopy in the inflow amplitude eps (continue from the mean-state optimum): produces the O(eps) family and checks L2
     numerically; cheap, informative.  [RECOMMENDED as diagnostic]
Invalid states inside the search: a solve failing SP2 checks or the attachment constraint returns a "failed evaluation" to
a FILTER-type globalization (feasibility restoration step, never a fake value); the trust region shrinks; three consecutive
failures at the same point => the point is declared non-evaluable and excluded (logged).
Guarantee class delivered: KKT-certified LOCAL optimum of the corrected discrete model, first-order consistent with RF-3D at the
final iterate; multipliers of active constraints reported (marginal thrust per unit length, per unit separation margin);
second-order: reduced Hessian eigenvalues from the BFGS/finite-difference of adjoint gradients (positive => strict local);
global: multistart dispersion d = spread of J over converged starts and the G.4 surrogate's max EI at termination
(reported, no theorem). Honest statement: no global guarantee for anyone (statement §6 R-i).
Decision criterion: KKT residual below the derived tolerance tol_KKT = (b_TS/10) * F / (typical design-scale) (so that a
KKT violation cannot hide a band-level thrust gain); reduced Hessian positive; multistart converged to the same J within band.
Falsifier: G.4 finds a point with J higher by more than band => local optimum rejected as the answer.
Options count: 7.

### SP5  SPATIAL REPRESENTATION  — LOAD-BEARING
Options:
 R.1 Axisymmetric mean state (S1/S2). Loss: everything azimuthal + averaging closure.
 R.2 Locally-axisymmetric quasi-steady per phase (S3/S7 loop). Loss: azimuthal communication, Coriolis-type deflection
     in the rotating frame, transport of swirl; valid domain per L4.
 R.3 RF-3D steady sector (exact under pin).  [RECOMMENDED evaluator; loop if r_red > b_TS]
 R.4 Full-annulus unsteady 3D (anchor; exact without the pin).
 R.5 Azimuthal Fourier/HB (S6).
 R.6 Linearized azimuthal modes about R.1 (T.6): eps-limited.
Designer vs evaluator: DIFFERENT representations (R.2 loop, R.3 evaluator) — this is the core of S7 and is what makes the
reduction error a MEASURED number: r_red(S) = |J_R3(S) - J_R2(S)| / F, computed on S_2*, S_7*, and on 2-3 intermediate
iterates; plus the residual of the R.2 field inserted in the R.3 equations (azimuthal flux + source terms), which localizes
WHERE the loss occurs (front region vs wall). For S4 the loop is R.3 and the loss is only discretization.
Decision criterion: r_red thresholds of SP1. Falsifier of the recommendation: r_red > b_TS on S_2* and TR corrections
non-convergent => R.3 in the loop.
Options count: 6.

### SP6  GEOMETRY AS DESIGN VARIABLES  — local for the decisive number, LOAD-BEARING for existence/tolerance claims
Options:
 P.1 B-spline wetted contour r_w(x) with d control points (C^2 interior => C^{1,1} contour automatically); slope/curvature
     bounds as linear/quadratic constraints on control points (exact for splines via control-polygon bounds).  [RECOMMENDED]
 P.2 CST/Bernstein class-shape function: compact, good for bells; poorer for plug + free lip.
 P.3 Hicks-Henne bumps on a Rao baseline: entangled with the comparator (bias); rejected as primary for a stated reason.
 P.4 Level set (S11): topology output; over budget.
 P.5 Multi-body parametrization: plug body + shroud as two P.1 contours with an attachment on Lambda and a truncation
     fraction as a parameter (base region handled in SP-PB).  [RECOMMENDED for plug/shrouded/ED]
 P.6 Topology by TOURNAMENT over the catalogue {bell, plug (truncation fraction free), shrouded plug, ED}: each optimized with
     P.1/P.5, all evaluated by RF-3D under the same closures; exact selection for a finite catalogue.  [RECOMMENDED]
Number of control points d: derived, not chosen — increase d until the optimized J changes by less than b_TS/10 * F
(a design-space refinement study, reported like a grid study).
Admissibility certificates: attachment on Lambda (interpolation constraint, exact); envelope (bound constraints); slope and
curvature (spline control-polygon bounds — sufficient, slightly conservative — the conservatism is measured by the actual
extremes); length/exit radius (fixed parameters or bounds); as-built tolerance class: perturbation ball of radius t_mach
(a declared manufacturing tolerance) in the control points; certificate = (i) linearized worst case |grad J| * t_mach <= b_TS/10 * F
and (ii) sampled verification (N = 20 random perturbations, N derived so that the sample max estimates the 90th percentile
with probability 0.88 = 1 - 0.9^20) all admissible and attached.
Existence of a maximizer: in the FINITE-dimensional compact parameter box, existence follows from continuity of the discrete
map S -> J_h(S) (Weierstrass): THEOREM for the discrete problem provided the solver converges on the whole box (which it does
not — non-evaluable points exist, SP4). For the continuous problem: compactness of C^{1,1} contours with bounded curvature
(Arzela-Ascoli) is THEOREM; continuity of the Euler solution map in the domain for weak solutions is a rigor GAP => existence
declared SCHEMA; the decisive number does not depend on it (it compares two computed designs).
Decision criterion: design-space refinement study converged; certificates (i)-(ii) pass. Falsifier: J still moving with d
above b_TS/10 at the largest affordable d (then the "optimum" is parametrization-limited: declare best-effort).
Options count: 6.

### SP7  DATA  — LOAD-BEARING
Entry of each class:
 D.A specs only: generator = reduced RDE wave model (analytic ZND-type wave + expansion fan + fill model) producing (p,T,M,angle,
     swirl) vs (r, phase) on Gamma_d [KNOWLEDGE: reduced RDE flow-field models, e.g. Fievisohn & Yu 2017 MoC-based RDE model;
     Sousa et al. 2017 RDE cycle analysis] [abstract]. Predictive but uncalibrated: the decisive answer at class A carries a
     model band that must be declared (SP9); class A is NOT the class of the decisive answer.
 D.B wave-structure model given: DIRECT input to the quadrature nodes (T.2) and to the RF-3D inflow.  [class of the decisive answer]
 D.C partial experiment: Bayesian calibration of the generator's parameters (S14), or at minimum a consistency audit (mean
     pressure, thrust of S_2*, f, n) with loud reject if outside 2x band.
 D.D mission profile: outer nodes on Pa (S9); D.E throttle envelope: outer nodes on operating points; D.F declared
     uncertainty: outer weights / sets (worst case = min over the set of the paired Delta); D.G coupling: fixed-point on the
     response map (S12).
Audits (loud reject):
 A.1 Causal separation: normal velocity through Gamma_d supersonic at every point and phase (all characteristics outgoing
     from the chamber) => no upstream influence; if subsonic anywhere: declare the closure (imposed total state + tangential
     velocity, exit pressure from the nozzle) and MEASURE the influence by perturbing the nozzle and re-running the generator
     (class A/B) — if the data change above band, the interface is misplaced (move Gamma_d downstream) or class G is required.
 A.2 Well-posedness: number of imposed variables = number of incoming characteristics per point and phase (counted from the
     computed normal Mach) — an automatic count, reject on mismatch.
 A.3 Measurability/periodicity: the data must be a single-mode periodic function of (theta - W t): test = azimuthal Fourier
     spectrum of the interface pressure has its energy at multiples of n (>= 99 % of variance, threshold derived from the
     quadrature-term budget b_TS/10 through the sensitivity dJ/dw of L3) — otherwise the wave pin is violated: reject.
 A.4 Mass/energy flux consistency of the data with specs (class A/B vs C): within the generator's declared band.
Weights and their uncertainty: J is linear in w (L3) => uncertainty band from weights = sum_k |F_k(S_7*) - F_k(S_2*)| * dw_k
for a declared dw (from the class F set or from the calibration posterior) — exact, no sampling needed for the difference.
USER PIN magnitudes (with provenance and relaxation cost):
 PIN-wave (single mode): effect on Delta = weight band above; a mode change (n -> n') changes W and the RF sector — the evaluator
 must be re-run per mode; cost = one RF-3D solve per mode. Magnitude: unknown a priori, MEASURED by L3 (free).
 PIN-frozen thermally-perfect: effect on ABSOLUTE thrust can be several % for hot dissociated products (recombination in the
 nozzle) [KNOWLEDGE: textbook, frozen vs shifting-equilibrium Isp differences of ~1-8 % depending on propellant and
 chamber temperature] [abstract] — LARGER than the band; effect on the DIFFERENCE Delta partially cancels under a common gas
 model (paired comparison) but not certainly: MEASURE by re-evaluating both designs with a quasi-1D shifting-equilibrium
 oracle along the mean streamline and reporting the change of Delta; cost = 1/2 session. Relaxing the pin fully (finite-rate
 chemistry in 3D) is a new solver: out of budget, declared.
 PIN-single-phase: zero effect for gaseous propellants; for propellants with condensed products a two-phase lag loss of order
 % [KNOWLEDGE: textbook two-phase nozzle losses] [abstract] — out of scope, declared, would be a common loss to both designs.
Recommendation: decisive at class B; class A only as a predictive demonstration with band; audits A.1-A.4 automatic.
Decision criterion: audits pass; weight band below b_TS/3. Falsifier: A.3 rejects (spectral leakage) or weight band > b_TS/3.
Options count: 7 (classes) + 4 audits.

### SP8  PROOF  — LOAD-BEARING
Verification ladder (each rung a rejector):
 V.1 Exact/semi-exact solutions: thermally-perfect quasi-1D nozzle (tabulated h) — mass flow and exit state to 1e-8 relative;
     Prandtl-Meyer fan (variable gamma via integrating the exact ODE); rotating-frame free-vortex/solid-body checks for F.3
     (uniform rotating flow must remain uniform: rejects source-term errors). Method of manufactured solutions for the
     3D sector with periodic BC.
 V.2 Grid convergence: three grids, observed order p measured; GCI band [KNOWLEDGE: Roache 1994 grid convergence index] [abstract]
     with safety factor 1.25 for three-grid studies (Roache's derived factor for observed-order studies); the discretization band
     b_h = GCI on J and on Delta (Delta converges faster if both designs are on matched grids — measured, not assumed).
 V.3 A posteriori validity of every used solve: SP2 (a)-(d) residuals + conservation balance (mass, momentum, energy flux
     through the control surface vs through Gamma_d within b_h) + attachment criterion + iterative residual drop to the level
     where |dJ| < b_TS/100 * F (derived: iteration error must be negligible against the band).
 V.4 Adjoint tests SP3 (i)-(iv).
 V.5 Cross-code: legacy MoC on every single state of the comparator (values), and on the S_2* contour; an independent
     quasi-1D + 2D check of J_QS.
 V.6 External anchor: one unsteady full-annulus 3D solve per final design (S5) at the coarsest grid whose GCI is below band;
     thrust time trace must be constant (L1 test) and its mean must match J_RF3D within b_h.
 V.7 Experiment (class C only): thrust-stand value of a built design — the only rung at the reference accuracy class.
Bands and safety factors of derived origin: b_h from GCI; b_red from r_red (SP5); b_w from weights (SP7); b_gas from the
equilibrium oracle re-evaluation (SP7); b_iter from V.3; b_repro from run-to-run variability (below). Budget rule: worst-case
SUM (independence not proven), each term computed, none assumed zero without a stated reason.
Reproducibility across versions/environments: a result = (code hash, checker hash, environment fingerprint). Re-run policy:
on any change of the three, re-run the checker on the stored design; quotable iff Delta >= sum of bands + b_repro where b_repro
is the measured spread of J over N_rep = 7 repeated runs with permuted thread/order settings (N derived: relative error of a
sample std ~ 1/sqrt(2(N-1)) ~ 29 % at N = 7 — enough for a band, and cheap). A non-reproducing result is marked FAILED with the
environment delta named; it is never re-stamped: either the new environment reproduces the old within b_repro, or the
discrepancy becomes a new finding with its own owner (re-derivation from scratch, not a tolerance widening).
Recommendation: V.1-V.6 mandatory; V.7 if class C. Decision criterion: all rungs pass; band sum computed. Falsifier: any rung
rejecting on a used solve; any re-run outside b_repro.
Options count: 7 rungs.

### SP9  THE DECISIVE RESULT  — LOAD-BEARING (it IS the answer)
Pre-registration:
 Configuration: BELL first (no base-region band; the plug comes second, SP-PB), fixed length, fixed exit radius, fixed mass flow
 (supersonic interface, audit A.1), one design point, class B data with measured St, eps, n.
 Comparator: S2 (mean-state classical + per-phase attachment fix + designer's area-ratio/length sweep) with the SAME gas table,
 SAME solver family for the evaluation, SAME attachment criterion — the strongest a competent designer fields (SP-CARM).
 Metric: paired difference Delta = [J_RF3D(S_7*) - J_RF3D(S_2*)] / J_RF3D(S_2*) (RF-3D exact evaluator, L1), plus the per-phase
 minimum attachment margin of both.
 Accuracy class: thrust-stand b_TS = 1 % (the conservative end of 0.5-1 %) as the materiality threshold; the computed band budget
 B = b_h + b_red + b_w + b_gas + b_iter + b_repro must itself be < b_TS for the experiment to be decidable at all (pre-condition;
 if B >= b_TS the program's first result is "undecidable at this fidelity", published as such).
 Outcomes: (+) Delta > b_TS + B: the unsteady-aware road buys a resolvable gain at this (St, eps); program continues to plug
 tournament and envelope (S9). (0) |Delta| <= b_TS + B: NEGATIVE RESULT — classical practice with per-phase check is adequate
 for O-a at this instance; publish with the L2 screen as the explanation and the operability Pareto (S10) as the follow-up.
 (-) Delta < -(b_TS + B): the road is WRONG (its model or search is defective): KILL; audit before any further claim.
 Kill criterion for the whole O-a road: outcome (0) or (-) at the instance with the LARGEST measured eps and SMALLEST St the
 data family offers (the most favourable case for the road) — if it cannot win there, it cannot win.
 Sensitivity: dDelta/dw_k = F_k(S_7*) - F_k(S_2*) (L3), reported as a vector; sensitivity to the base model = 0 for the bell;
 for the plug: SP-PB.
 External anchor: V.6 unsteady 3D solve of both designs (own machinery but a different equation set and frame: rejects L1
 misuse and the RF solver), V.5 legacy MoC on the comparator (independent code), and — if class C exists — the measured thrust
 of the engine with its current nozzle as an absolute-level check (accuracy class thrust-stand).
 Generalization scope: from ONE design point the claim is "at (St, eps, n) = measured values, configuration bell, class B";
 the L2 screen evaluated over a sweep of eps (by scaling the data family) and of St (by scaling L) at negligible cost (values
 only) gives the MAP of where the gain could exceed band — the map is the honest generalization, the point is the proof.
Options for the decisive result (alternatives considered): DR.1 bell/class B/S2 comparator [RECOMMENDED]; DR.2 plug (higher
expected sensitivity to phase because of the free plume, but base band); DR.3 envelope-level Delta (needs D-E); DR.4 operability
Pareto (S10); DR.5 experiment (class C + build: out of budget).
Decision criterion: B < b_TS computed; audits pass. Falsifier: B >= b_TS (undecidable) — then the decisive result is the band
budget itself and the lever named for reducing it (grid, r_red).
Options count: 5.

### SP-PB  BASE REGION (truncated plug)  — LOAD-BEARING for plug configurations, irrelevant for the bell
Options:
 PB.1 Constant base pressure from a correlation p_b/Pa = c(M_lip, truncation) [KNOWLEDGE: plug/aerospike base-pressure
      correlations, reviewed in Hagemann, Immich, Nguyen & Dumnov 1998 advanced nozzle concepts] [abstract]: band of the
      correlation typically tens of % of p_b (declared from the source's scatter, not assumed).
 PB.2 Base pressure from the captured recirculation of the Euler solve: NOT a legitimate model (inviscid base flow is
      undefined); rejected for a stated reason (Euler cannot close a base).
 PB.3 Viscous layer model (RANS in the base region only, zonal): cost + turbulence-model band; out of the pinned Euler core
      (declared model layer), possible as an oracle for the closure band.
 PB.4 Closure as an UNCERTAIN PARAMETER: treat p_b as an interval [p_b_lo, p_b_hi] from PB.1 scatter; decisive Delta reported
      as the MIN over the interval of the paired difference (both designs under the same p_b), with dDelta/dp_b = (A_b7 - A_b2)/F
      reported (the difference cancels at first order if base areas match — a design choice: fix the truncation fraction in the
      tournament so that the base band drops out).  [RECOMMENDED]
Materiality: base thrust contribution = (p_b - Pa) A_b / F; with A_b/A_exit ~ 0.2-0.4 for typical truncations and p_b - Pa of
order 0.1-0.5 Pa, the base band alone can be ~ b_TS (derived per instance from the numbers) — hence the bell-first order of SP9.
Decision criterion: |A_b7 - A_b2| * (p_b_hi - p_b_lo) / F < b_TS/3 (the paired base band must be a minor term). Falsifier: the
optimizer wants a different truncation than the comparator (base areas differ) AND the resulting band exceeds b_TS/3 => the
plug decisive number is declared undecidable at the Euler level, PB.3 required.
Options count: 4.

### SP-CARM  THE STRONGEST COMPETING PRACTICE  — LOAD-BEARING (a weak comparator invalidates the decisive number)
Options:
 C.1 Rao/MoC bell at the arithmetic time-mean state (S1): weakest; beaten by choice of average alone.
 C.2 Rao/MoC or steady-Euler-optimized bell at the MIXED-OUT average (mass, momentum, energy flux-conserving equivalent
     uniform state) [KNOWLEDGE: averaging non-uniform flows, Cumpsty & Horlock 2006] [abstract]: the average a competent
     designer uses; removes most of the first-order term of L2.
 C.3 C.2 + per-phase separation check + manual iteration on area ratio/length (L5).  [RECOMMENDED comparator]
 C.4 C.3 + THRUST-CONSISTENT average: choose the mean state so that F(S;u_bar*) = sum w_k F_k(S) at the baseline contour
     (exists by continuity along a 1-parameter family of averages between arithmetic and mixed-out; found by 1-D root find):
     this competitor already captures the first-order gain; against it the road's residual advantage is O(eps^2) in the
     objective + first-order only through the feasible set (L2, L5). Declared as the "refuter's comparator": if S_7* does not beat
     C.4 above band the claim of novelty is bounded to certificates and evaluator, not to thrust.
 C.5 Weighted multipoint steady design by a designer with a modern optimizer (= S3 without certificates): the honest
     statement is that the ROAD's design loop is this known technique; novelty can only be claimed for (a) the exact RF evaluator
     and its measured reduction error, (b) the screen/bound L2, (c) the certificates; the literature query bounding the claim must
     be stated ("multipoint nozzle design under periodic inflow", "rotating-frame steady RDE nozzle").
Does a competent designer already average duty? Yes (C.2/C.3), and multipoint design is standard in aerodynamics; therefore
the comparator of record is C.3 with C.4 as a pre-registered refuter run (values only, cheap).
Decision criterion: comparator built with the same gas table, solver and criterion; its own per-phase attachment verified.
Falsifier: S_7* beats C.3 but not C.4 above band => outcome (0) for thrust, with the novelty claim re-bounded as above.
Options count: 5.

--------------------------------------------------------------------------------------------------
## ORDER OF BATTLE (dependency order; load-bearing first) with session budget (7-10 sessions, 3 h decisive-run cap)
--------------------------------------------------------------------------------------------------
 1. SP7 audits A.1-A.4 on the class-B data + measurement of St, eps, n, ell_theta, C_theta (session 1; values only).
 2. SP2 F.2 solver + SP8 V.1/V.2 verification on exact solutions and grids; thermally-perfect table (sessions 1-2).
 3. SP-CARM C.3 comparator built and verified (per-phase attached), C.4 refuter average found (session 2-3).
 4. SP-OBJ/S13 L2 SCREEN: delta(S) on S_2* and on perturbed contours; decision O-a vs O-c objective (session 3). GATE.
 5. SP3 adjoint + rejector tests (i)-(iv) (session 3-4).
 6. SP6 parametrization + design-space refinement; SP4 SQP/multistart loop on QS-2D (sessions 4-5).
 7. SP2 F.3 RF-3D sector solver + V.1 rotating-frame checks + GCI (session 5-6); SP5/SP1 r_red measured on S_2*, S_7*. GATE:
    r_red vs b_TS/3, b_TS thresholds => plain loop / TR-corrected loop / S4 loop.
 8. SP9 decisive paired Delta with full band budget B; V.5 cross-code; V.6 anchor solve (session 7).
 9. SP-PB + plug tournament (P.6) if outcome (+) or budget remains (sessions 8-9); S10 Pareto if outcome (0).
10. SP8 reproducibility re-runs (N_rep = 7), provenance, write-up (session 10).
Fork dependencies: 4 gates 6-8 (screen kills => skip to S10); 7 gates the loop representation; 3 gates 8 (no comparator, no number).

--------------------------------------------------------------------------------------------------
## DERIVED TOLERANCES (single table; none magic)
--------------------------------------------------------------------------------------------------
 b_TS = 1 % of F (conservative end of the stated 0.5-1 % thrust-stand class).
 quadrature term, KS overestimate, design-space refinement, tolerance certificate: each <= b_TS/10 (ten-term budget headroom).
 r_red thresholds b_TS/3, b_TS (three-way equal split of the band among reduction, discretization, data).
 iteration error b_TS/100 (must be negligible against every other term).
 Taylor slope window [1.8, 2.2], h_min from the roundoff floor formula; dot-product tolerance 10 * N * eps_mach * norms.
 GCI safety factor 1.25 (three-grid observed order). N_rep = 7 (29 % std-of-std). N_tol = 20 (0.88 coverage of the 90th percentile).
 A.3 spectral-purity threshold: derived from dJ/dw (L3) so that leaked energy cannot move J by more than b_TS/10.

--------------------------------------------------------------------------------------------------
## WHAT THIS LENS EXPECTS (pre-registered belief, to be falsified)
--------------------------------------------------------------------------------------------------
 CONJECTURE: for O-a on a bell against comparator C.3/C.4, |Delta| <= b_TS at St <= 0.3 (L2: O(eps^2) with a competent average),
 with the road's resolvable value living in (a) the per-phase feasible set (L5) and (b) the certificates/evaluator, not in thrust.
 Falsifier: outcome (+) of SP9 against C.4. Either way the answer to Q0 is publishable: "optimize with a weighted multipoint
 steady loop, certify with the exact rotating-frame evaluator and a computed band budget, and expect the thrust lever to be
 of the order of the band unless eps is large and St small — here is the map".
