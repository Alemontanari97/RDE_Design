# BLIND DERIVATION — Formalization of the interface datum for a rotating-detonation exhaust cut

Independent derivation from the brief `contract_blind_brief.md` ONLY.
Lens: propulsion test data, combustion-device characterization, and
uncertainty quantification — i.e., the datum is treated throughout as
an object that must eventually be DELIVERED by a rig or a CFD
campaign, audited, and transported into a design program with a
certificate. No repository material consulted.

Rigor-class tags used below:
- **[CP]** complete proof (self-contained here or reducible to a
  standard textbook argument cited by name),
- **[PS]** proof sketch (route stated, gaps named),
- **[MA]** modeling assertion (physical closure; falsifiable, not
  provable).
Every Definition/Claim carries a **Reject:** clause — a concrete test
whose failure falsifies the claim or rejects a delivered datum.

---

## 0. Standing objects and notation

**Def 0.1 (geometry).** Work in cylindrical coordinates
(x, r, θ), x the machine axis. The interface is a fixed annular
surface at an axial station:
S := { x = x_I } × A,  A := [r_i, r_o] × 𝕋,  𝕋 := ℝ/2πℤ.
S is FIXED: it does not move with any wave and does not deform with
the design.

**Def 0.2 (state space).** Downstream model: non-reacting mixture of
frozen composition, thermally perfect with temperature-dependent
caloric properties h = h(T), c_p = c_p(T) defined on a validity
window T ∈ [T⁻, T⁺] (table or fit domain). The pointwise state is
u := (ρ, v_x, v_r, v_θ, T) ∈ 𝒰,
𝒰 := { ρ > 0, T ∈ (T⁻, T⁺) } ⊂ ℝ⁵ (open).
Derived: p = ρ R T (R fixed by the frozen composition),
a² = γ(T) R T with γ(T) = c_p/(c_p − R), normal Mach
M_n := v_x / a on S (x is the surface normal).

**Def 0.3 (wave kinematics).** The combustor sustains N ≥ 1
detonation waves rotating at angular speed Ω (sign = chirality).
At a fixed azimuthal station the state is time-periodic with period
τ := 2π /(N |Ω|)
under the identical-waves hypothesis (H-ID below). 𝕋_τ := ℝ/τℤ.

**[MA 0.4] Regime assertion (inherited from the brief).** In the
operating regime of interest the efflux is periodic in the sense of
Def 2.2 below (pure rotating wave up to a declared residual). This is
an empirical property of the device, not a theorem.
**Reject:** the mode-purity audit A6 (§6) fails on delivered data.

---

## 1. WHERE — admissible placement of the interface

**Def 1.1 (admissible placement).** A station x_I is *admissible*
for a design family 𝒢 (the set of candidate nozzle geometries) if
all of (P1)–(P5) hold:

**(P1) Chemical frozenness.** The integrated heat-release rate
downstream of x_I is small against the mean total-enthalpy flux:
∫_{x>x_I} q̇‴ dV ≤ ε_q · ⟨ Φ_h ⟩,  Φ_h := ∫_S ρ v_x h_t dA,
with ε_q a declared tolerance (order 1% for a thrust target, since
thrust error scales ∼ ½ ε_q through exit velocity). Otherwise the
non-reacting downstream model is wrong *by construction*, not merely
inaccurate. **[MA]**
**Reject:** CFD provenance — integrate the heat-release field
downstream of x_I, compare to ε_q·⟨Φ_h⟩. Rig provenance — axial
chemiluminescence (OH*/CH*) decay: signal at x_I above the
calibrated floor rejects; secondary-combustion signature (pressure
rise without area change) downstream rejects.

**(P2) Geometric commonality.** S lies in the region of geometry
shared by ALL g ∈ 𝒢: min over 𝒢 of the design-variable support
starts strictly downstream of x_I. **[CP** — set inclusion, checked
by construction**]**
**Reject:** exhibit g ∈ 𝒢 whose wall parameterization is active at
x ≤ x_I.

**(P3) Character budget.** The subsonic-normal fraction of the
cycle–surface measure is within a declared budget β:
meas{ (t,y) ∈ 𝕋_τ×A : M_n(t,y) ≤ 1 } ≤ β · meas(𝕋_τ×A),
with β = 0 required for an *unconditionally causal* cut (Claim 5.1)
and β > 0 admissible only together with a closure declaration (§4)
and a contamination bound (§5). **[MA** for the chosen β**]**
**Reject:** audit A8 (sonic census) exceeds β.

**(P4) Established periodicity at station.** The two-sided
statistical tests of A6/A7 pass at x_I over the certification run:
the flow at x_I is (statistically) a settled rotating wave, not a
transient or a mode-hopping record. **[MA]**
**Reject:** A6/A7 fail.

**(P5) Deliverability.** The station is instrumentable (rig) or
grid-converged (CFD) at the bandwidth demanded by A10: temporal
content up to the shock-rise harmonic cutoff n_max·N|Ω|/2π and
azimuthal wavenumbers up to n_max·N are resolvable. **[MA]**
**Reject:** A9/A10 fail (aliasing or resolution).

**Claim 1.2 (placement trade-off; invalidators).** Moving x_I
downstream improves (P1) and (P3) (expansion accelerates the flow,
kills residual reactions) but violates (P2) sooner and — decisive
from the test-data lens — degrades TRANSPORTABILITY: a datum
harvested on a rig that had *some* downstream hardware is
contaminated by that hardware wherever (P3) fails (upstream-running
characteristics; §5). Moving x_I upstream gains commonality but
breaks (P1) and admits injector/recirculation structures across S.
A placement is INVALIDATED (not merely degraded) by: (i) deflagrative
afterburning across S at O(1) of Φ_h; (ii) a change of wave count N
or direction during the record; (iii) any candidate design touching
x ≤ x_I; (iv) subsonic corridors connecting the design domain to the
combustor when β was declared 0. **[MA]**
**Reject:** each invalidator is detected respectively by (i) the P1
test, (ii) audit A6 spectrogram stationarity, (iii) the P2 set
check, (iv) the causality monitor C-ii of §5.

---

## 2. WHAT — the datum, mathematically

**Def 2.1 (datum, lab-frame form).** The interface datum is a map
q : 𝕋_τ × A → 𝒰,  q ∈ L^∞(𝕋_τ × A; 𝒰) ∩ BV(𝕋_τ × A; ℝ⁵),
i.e., bounded, realizable pointwise (values in 𝒰 with a uniform
compact margin: ess-range(q) ⋐ 𝒰), and of bounded variation. BV is
the correct regularity class: the efflux of a detonation carries
rotating shock and contact remnants — codimension-1 jump sets — and
must NOT be assumed continuous; but it must have well-defined
one-sided traces on its jump set J_q (BV structure theorem, Vol'pert
— **[CP** by citation**]**) so that internal jump conditions (A3)
are testable. Smoother subclasses (piecewise C¹ with finitely many
shock sheets per cycle) may be declared, never assumed.
**Reject (membership):** delivered data with unbounded total
variation under mesh/probe refinement (variation grows without bound
as resolution increases beyond the physical shock thickness scale)
reject BV membership; values escaping 𝒰 (T outside the caloric
window, ρ ≤ 0) reject realizability — audit A5.

**Def 2.2 (rotating-wave structure).** Hypotheses:
- **(H-ID)** the N waves are identical and equispaced;
- **(H-RW)** the field is a pure rotating wave: there exists
  Q : 𝕋 × [r_i,r_o] → 𝒰, Q ∈ BV, with
  q(t, r, θ) = Q(φ, r),  φ := θ − Ω t  (phase),
  and Q(φ + 2π/N, r) = Q(φ, r) under (H-ID).
Then the datum is equivalently the STEADY profile Q on the phase
annulus 𝕋 × [r_i,r_o], plus the scalars (N, Ω, sign Ω). **[CP** —
change of variables; the equivalence is exact given (H-RW)**]**
**Reject (of H-RW on data):** mode-purity audit A6: the relative
residual
e_RW := ‖ q(t,r,θ) − Q̂(θ−Ωt, r) ‖_{L²(𝕋_τ×A)} / ‖ Q̂ ‖_{L²},
with Q̂ the best phase-locked average, exceeds a declared ε_RW; or
off-comb spectral energy fraction exceeds tolerance.

**Def 2.3 (three representations of the cycle and their ranking).**
The cycle can enter the formalism as:
(a) *time-dependence*: q on 𝕋_τ × A (Def 2.1);
(b) *phase parameter*: Q on 𝕋 × [r_i,r_o] (Def 2.2) — a
one-parameter family of steady radial profiles q_φ(r) := Q(φ,r);
(c) *measure*: the phase-marginal (Young) measure
μ_{(r,θ)} := (1/τ) ∫_{𝕋_τ} δ_{q(t,r,θ)} dt ∈ 𝒫(𝒰),
equivalently, under (H-RW), the pushforward of the uniform phase
measure by φ ↦ Q(φ,r).

**Claim 2.4 (information ordering).** (a) ⇔ (b) exactly under
(H-RW); (b) ⇒ (c) with strict information loss in general: μ
retains, at each point of A, the one-point statistics (hence every
time-averaged pointwise observable ⟨g(q)⟩ = ∫ g dμ), but discards
the phase CORRELATION between distinct points of A. Since the
downstream Euler operator couples neighboring points, (c) is
sufficient only for diagnostics and UQ bookkeeping, NOT as input to
the downstream solve; the design program must consume (a)/(b).
**[CP** — construct two distinct profiles Q₁ ≠ Q₂ with identical
one-point marginals (e.g., shift the phase of the r-dependence:
Q₂(φ,r) := Q₁(φ + χ(r), r) for nonconstant χ); they yield different
downstream solutions but identical μ**]**
**Reject:** exhibiting a design functional that distinguishes Q₁,Q₂
above at fixed μ confirms the claim; failure to exhibit any (over a
dense family of functionals) would refute the *relevance* (not the
mathematics) of the distinction.

**Claim 2.5 (symmetries inherited and not).** Under (H-ID)+(H-RW)
the datum inherits EXACTLY:
- (S1) helical symmetry q(t+s, r, θ) = q(t, r, θ − Ωs) ∀s (this is
  the defining symmetry; periodicity S2 is its corollary on the
  discrete subgroup);
- (S2) time-periodicity with τ = 2π/(N|Ω|) at fixed (r,θ);
- (S3) discrete azimuthal symmetry ℤ_N at fixed t.
It does NOT inherit:
- (N1) continuous axisymmetry — broken by the wave; only the
  cycle-mean ⟨q⟩ is axisymmetric (and ⟨q⟩ is NOT a solution trace,
  see Claim 3.5);
- (N2) reflection θ ↦ −θ — broken by chirality (sign Ω); a datum and
  its mirror are physically distinct and must not be identified;
- (N3) time-reversal — broken by shocks (entropy production);
- (N4) phase-shift gauge is a symmetry of the FAMILY, not of a
  DELIVERED datum: two deliveries differing by a global phase are
  equivalent, so every audit and every downstream functional must be
  phase-gauge invariant. **[CP** for the group statements given the
  ansatz; **[MA]** for (H-ID) itself on a real device**]**
**Reject:** (S3): compare the N phase-translates of a delivered Q —
excess ℤ_N-residual beyond the noise floor rejects (H-ID)
(wave-to-wave asymmetry, a documented RDE behavior). (N4): any audit
statistic that changes under a global phase shift of Q is itself
rejected as ill-formed.

**Claim 2.6 (the datum is constrained, not free).** A delivered q
must satisfy, in addition to membership (Def 2.1):
(i) internal Rankine–Hugoniot consistency on its own jump set J_q
(one-sided traces satisfy moving-discontinuity jump relations with
the wave's trace speed);
(ii) entropy admissibility: the frozen-mixture entropy s(T,p) jumps
non-negatively across shocks in the wave-crossing direction; no
rarefaction shocks;
(iii) cycle-budget closure: cycle-mean mass flux equals the metered
feed, ⟨∫_S ρ v_x dA⟩ = ṁ_feed, and cycle-mean total-enthalpy flux
equals injected enthalpy plus heat release minus measured wall heat
loss, each to within combined uncertainty (these are properties any
trace of an actual upstream solution must have). **[PS** — (i),(ii)
follow from q being the trace of a weak entropy solution upstream
(Lax admissibility, standard); (iii) is control-volume bookkeeping
with declared loss terms**]**
**Reject:** audits A1–A4 (§6) are precisely the rejecting tests.

---

## 3. STRUCTURE — exact reductions of the periodic datum to steady data

**Claim 3.1 (wave-frame steadiness — the exact reduction).**
Hypotheses: (H-RW); downstream geometry AXISYMMETRIC; downstream
model = compressible inviscid flow with frozen composition (no
explicit t or θ dependence in the equations or walls). Then the
change of variables (t, r, θ, x) ↦ (φ = θ − Ωt, r, x) maps the
downstream time-periodic problem to a STEADY 3D problem in the
wave frame: the full unsteady solution is a rigidly rotating
pattern, and the datum entering it is the steady profile Q of
Def 2.2. Nothing is lost: this reduction is EXACT. Its price is
dimensional, not physical: the reduced problem is a steady
THREE-dimensional problem (all three velocity components, φ-gradients
retained), not a family of lower-dimensional ones. **[CP** — the
transformation is a diffeomorphism of the domain commuting with the
equations precisely when the geometry and coefficients are
θ- and t-invariant; the rotating-wave solution class is preserved
by uniqueness in the class, which is the only gap: uniqueness of the
downstream solution in the rotating-wave class is assumed, so
strictly **[PS]** at the level of the full nonlinear system**]**
**Reject:** downstream CFD initialized on the rotating-wave manifold
that drifts off it (growth of non-wave-locked energy beyond
numerical floor) rejects the class-closure hypothesis for that
configuration; a non-axisymmetric candidate nozzle rejects the
hypothesis set by inspection.

**Claim 3.2 (phase-family / quasi-steady reduction — approximate).**
The design-friendly reduction: for each φ, feed the steady radial
profile q_φ(r) = Q(φ,·) to a STEADY axisymmetric (or quasi-1D)
downstream solve 𝒮_st, then average the thrust:
T_QS := (1/2π) ∫_𝕋 T[𝒮_st(q_φ)] dφ.
Hypotheses for exactness: the downstream operator must DECOUPLE
phase slices, i.e., (i) unsteady terms negligible: reduced frequency
k := |Ω| L_noz / v̄_x ≪ 1 (equivalently Helmholtz number
He := |Ω| L_noz / ā ≪ 1 with the Mach factor absorbed), and
(ii) azimuthal fluxes negligible against axial: 
|∂_θ F_θ| ≪ |∂_x F_x| along the nozzle.
Then T_QS = ⟨T⟩ + O(k) + O(azimuthal-flux ratio). The reduction is
NOT exact at finite k: it discards inter-slice momentum/energy
exchange and unsteady storage. NUMERICAL WARNING from the lens: for
kHz-order waves (N|Ω|/2π ∼ 3–6 kHz), L_noz ∼ 0.1 m, ā ∼ 10³ m/s,
He ∼ O(1): the hypothesis is NOT automatically satisfied and must be
CHECKED per configuration, never assumed. **[PS** — linearize the
downstream operator about the slice solution; the first-order error
is the action of the discarded operators (Ω ∂_φ and tangential-flux
divergence) on the slice family, giving the stated orders; constants
not derived here**]**
**Reject:** (falsifier for a given configuration) run one wave-frame
exact solve (Claim 3.1) or one time-accurate downstream solve on the
same datum and compare ⟨T⟩ with T_QS: discrepancy above the declared
design tolerance rejects the reduction FOR THAT CONFIGURATION;
internally, k and the azimuthal/axial flux ratio measured above
declared thresholds reject the hypotheses directly.

**Claim 3.3 (what is lost, and how to carry it).** The loss of 3.2
is representable and boundable:
(a) *Carry as a corrector:* solve the linearized unsteady problem
about the slice family with forcing = the discarded terms; add the
resulting first-order thrust correction δT₁. Residual then O(k²).
(b) *Bound as a bracket:* |⟨T⟩ − T_QS| ≤ C·k·Var_φ(datum fluxes) +
C'·(tangential/axial flux ratio)·⟨|Φ_m|⟩, with C, C' calibrated once
per configuration class by the falsifier of 3.2 (a measured, not
assumed, constant — UQ practice: the bound's constants are estimated
with their own uncertainty and inflated by a coverage factor).
**[PS** for (a) (standard perturbation, well-posedness of the
linearized problem assumed); **[MA]** for the calibrated constants
in (b)**]**
**Reject:** a configuration where the measured discrepancy exceeds
the calibrated bound rejects the calibration class (constants must
be re-estimated; the bound as stated is falsified for that class).

**Claim 3.4 (averaging does not commute with the physics).** For any
nonlinear flux F, ⟨F(q)⟩ ≠ F(⟨q⟩) in general; concretely the mean
momentum flux ⟨ρ v_x²⟩ ≥ ⟨ρ⟩⟨v_x⟩²-type inequalities are strict
whenever the cycle variance is nonzero. Hence THREE inequivalent
objects must never be conflated:
(i) the true cycle-mean thrust ⟨T[q]⟩;
(ii) the phase-family average T_QS (Claim 3.2);
(iii) the "mean-flow" thrust T[𝒮_st(⟨q⟩)] from a single steady solve
of the averaged datum.
(iii) is NOT an admissible reduction: ⟨q⟩ is generally not a trace
of any admissible flow (it averages across shocks, violating its own
internal jump/entropy structure), and the committed error carries no
small parameter — it is O(cycle variance), not O(k). **[CP** — Jensen
/ direct counterexample: take ρ ≡ const, v_x square-wave in φ; then
⟨ρv_x²⟩ − ρ⟨v_x⟩² = ρ·Var(v_x) > 0**]**
**Reject:** the claim is refuted only by exhibiting a nonlinear
functional class for which the commutator vanishes on all admissible
data with nonzero variance (impossible for quadratic fluxes; the
test is the counterexample computation itself).

**Claim 3.5 (status of the mean datum).** ⟨q⟩ (or flux-consistent
averages of it) is admissible ONLY as (i) a diagnostic, (ii) a
reference for uncertainty normalization, or (iii) the zeroth term of
a declared expansion whose first-order term is carried (3.3a). A
design program consuming ⟨q⟩ alone must declare the O(Var) model
error as model-form uncertainty in its verdicts. **[MA]**
**Reject:** audit A11 — a delivered pipeline that quotes thrust from
⟨q⟩ without a variance-scaled error bar is rejected at review.

---

## 4. WELL-POSEDNESS — what may be prescribed where, and what must be closed

Setting: the per-state downstream problem — steady compressible
inviscid flow (frozen mixture, h(T) caloric closure) on the nozzle
domain, with S as the inflow boundary; states indexed by phase φ
(reduction 3.2) or the single wave-frame problem (3.1). The counting
below is the linearized (characteristic) well-posedness condition —
necessary for any well-posed nonlinear formulation, and the standard
of practice for boundary-condition design.

**Claim 4.1 (characteristic counting at S).** The normal flux
Jacobian of the 5-equation Euler system at a point of S with outflow
from the combustor v_x > 0 has eigenvalues
{ v_x, v_x, v_x, v_x + a, v_x − a }.
Incoming (into the design domain) characteristics number:
- **5** where M_n > 1 (supersonic normal inflow to the domain):
  the FULL state (ρ, v_x, v_r, v_θ, T) may — and must — be
  prescribed. No closure needed; the downstream problem is locally
  determined by the datum.
- **4** where 0 < M_n < 1 (subsonic inflow): exactly one
  characteristic (speed v_x − a < 0) runs upstream. Only FOUR
  independent combinations may be prescribed; the fifth is
  determined by the downstream solution. Prescribing all five
  overdetermines the problem (spurious reflected layers); standard
  admissible quadruples: {p_t, T_t (equiv. h_t), flow angles
  α_r, α_θ} or {s, h_t, v_r/v_x, v_θ/v_x}.
- Sonic points M_n = 1: degenerate (a characteristic tangent to S);
  admissible only on a measure-zero set with a declared limiting
  treatment.
**[CP** — eigenstructure of the Euler normal Jacobian is textbook
(e.g., Godunov/Toro-level); the count of prescribable data equals the
count of incoming characteristics by linearized well-posedness
(Kreiss-type condition), **[PS]** at full nonlinear rigor**]**
**Reject:** numerically, prescribing 5 quantities on a subsonic
patch produces a non-vanishing residual layer at S under grid
refinement (reflection that does not converge away) — a concrete
detector; prescribing 4 on a supersonic patch leaves a one-parameter
indeterminacy detectable as initialization dependence of the
converged solution.

**Def 4.2 (closure).** Wherever M_n < 1 on S (a set of positive
measure allowed only if the placement declared β > 0 in P3), the
datum is INTRINSICALLY INCOMPLETE for the per-state problem: the
missing fifth piece must be closed by a model. The options and their
prices:
- **(C1) Characteristic closure (downstream-coupled):** let the
  downstream solve return the outgoing invariant; prescribe the four
  incoming pieces from the datum. Price: the realized boundary state
  now DEPENDS on the design — the "datum" on the subsonic patch is
  not pure data (feeds §5); moreover the delivered rig/CFD values of
  the fifth quantity (e.g., static p) were set by the RIG's
  downstream hardware and must be discarded, not matched.
- **(C2) Non-reflecting / impedance closure:** impose zero (or a
  modeled) reflection coefficient for the upstream-running wave.
  Price: well-posed and design-independent, but physically wrong by
  exactly the neglected reflection; error O(|R|) with R the true
  reflection coefficient of the eventual design; the closure error
  must be logged as model-form uncertainty.
- **(C3) Full-state forcing (inadmissible):** prescribing all five
  on subsonic patches. Named only to be BANNED: it is
  overdetermined (Claim 4.1). **[CP** for the counting behind the
  ban; **[MA]** for the price estimates of C1/C2**]**
**Reject:** a delivered pipeline using C3 on a positive-measure
subsonic patch is rejected by the refinement test of 4.1; C2's
declared |R| bound is rejected if a coupled (C1) recomputation
shifts thrust beyond the C2-quoted uncertainty.

**Claim 4.3 (per-phase character map is part of the datum).** Since
the prescribability pattern depends on sign(M_n − 1) pointwise, the
datum must SHIP WITH its own character map
χ : 𝕋 × [r_i, r_o] → {sup, sub, sonic},  χ = sign(M_n − 1) ∘ Q,
and the partition's uncertainty (A8): near-sonic regions with
|M_n − 1| ≤ k·U(M_n) are classified UNKNOWN and force the
conservative branch (treated as subsonic, i.e., requiring closure).
**[MA** — the conservative-branch rule is a UQ policy, not a
theorem**]**
**Reject:** a delivered datum whose quoted χ flips on recomputation
within its own U(M_n) is rejected as under-resolved at the sonic
line.

---

## 5. CAUSALITY — when the cut is legitimate

**Claim 5.1 (sufficient condition for design-independence).** If
M_n(t, y) ≥ 1 + δ for a.e. (t,y) ∈ 𝕋_τ × A with margin
δ ≥ k_c · U(M_n) (coverage factor k_c ≥ 2 against the measured
uncertainty of M_n), then no downstream characteristic reaches S:
the domain of dependence of the upstream region excludes the design
domain, and the datum is EXACTLY independent of the design within
the inviscid model. The cut is then legitimate unconditionally over
the design family 𝒢. **[PS** — finite-speed-of-propagation /
domain-of-dependence argument for hyperbolic systems; complete at
the linearized level, standard for the nonlinear system away from
degeneracies; the margin-δ dressing is **[MA]** (UQ policy)**]**
**Reject:** the design-sweep test C-ii below detects any violation
in practice; analytically, a subsonic path from the design domain to
S refutes the hypothesis, not the claim.

**Claim 5.2 (mechanisms that break causality, ranked by severity).**
- **(B1) Continuous contamination:** subsonic patches (wall boundary
  layers' inviscid footprint, wave-wake deficits, near-sonic
  troughs of the cycle) admit upstream-running acoustics: the
  delivered fifth component on those patches encodes the RIG's
  hardware, and the design sees a datum that would differ on the
  real engine. Error: continuous in the reflection magnitude;
  handled by C1/C2 with logged uncertainty.
- **(B2) Operating-point shift:** downstream impedance changes the
  combustor's mean backpressure enough to shift (ṁ-split, wave
  speed Ω, peak states) continuously. The datum drifts with design:
  the cut fails QUANTITATIVELY. Detectable, partially correctable by
  re-parameterizing the datum against measured backpressure.
- **(B3) Mode bifurcation (catastrophic):** downstream feedback
  flips the wave COUNT N, direction, or triggers longitudinally
  pulsed operation. The datum changes discontinuously (different
  symmetry group S3, different τ): NO correction is possible; the
  entire datum object is void for that design. **[MA** — mechanism
  taxonomy from device phenomenology**]**
**Reject:** each is detected by the monitors of Claim 5.3; B3
additionally rejects itself via A6 (the delivered record's comb
structure changes).

**Claim 5.3 (audit/monitor suite for causality).** The cut is
accepted only with ALL of:
- **(C-i) Margin monitor:** cycle-and-surface minimum of M_n with
  uncertainty: report m := ess-inf M_n and U(m); require
  m − k_c·U(m) > 1 (else declare β > 0 and go through §4 closure).
- **(C-ii) Design-sweep falsifier:** evaluate the interface record
  under ≥ 2 deliberately different downstream geometries (in CFD; or
  rig with two aft-hardware variants): the datum must be invariant
  within its combined noise floor. THIS IS THE PRIMARY REJECTING
  TEST OF THE ENTIRE CUT: any statistically significant dependence
  of the delivered datum on downstream hardware rejects legitimacy.
- **(C-iii) Mode monitor:** wave count and frequency (N, Ω) from
  high-bandwidth pressure spectra, identical across the sweep of
  C-ii and across the certification window (guards B3).
- **(C-iv) Upstream-wave detector:** two-station cross-correlation
  (or axial two-plane CFD probes) around x_I: coherent structures
  with upstream group velocity above the noise floor reveal active
  contamination paths (guards B1 even when C-i passes marginally).
**[MA** — monitor design; each is itself falsifiable by injecting a
synthetic violation and checking detection**]**
**Reject:** the suite is validated by seeded-fault tests: a
deliberately subsonic-patched synthetic datum or a forced
backpressure change must trip C-i/C-ii/C-iv respectively; a monitor
that misses its seeded fault is rejected and redesigned.

---

## 6. ADMISSIBILITY AUDITS — the acceptance gauntlet

A delivered datum 𝒟 = (Q̂, N, Ω, χ, U, W) (nominal profile, wave
count, speed, character map, uncertainty, validity window — see §7)
is accepted only if ALL audits pass. Each audit states its rejecting
test; tolerances are DERIVED (from uncertainties or resolution),
never bare numbers. All audit statistics must be phase-gauge
invariant (Claim 2.5 N4).

- **A1 Mass-budget consistency.** |⟨∫_S ρ̂ v̂_x dA⟩ − ṁ_feed| ≤
  k_c·U_comb, U_comb combining flow-meter and datum-integration
  uncertainties. **Reject:** outside the band — the datum is not the
  trace of the metered device. **[MA]**
- **A2 Energy-budget consistency.** Cycle-mean total-enthalpy flux
  vs injected (chemical + sensible) enthalpy minus measured wall
  heat loss, within combined uncertainty. **Reject:** outside band
  (missing physics upstream or bad calorics at the cut). **[MA]**
- **A3 Internal jump consistency.** On the delivered jump set J_Q:
  one-sided traces satisfy the moving-shock Rankine–Hugoniot
  relations at the wave trace speed, to a tolerance derived from the
  delivery resolution (shock smeared over n cells/probe spacings ⇒
  tolerance propagated accordingly). **Reject:** a jump violating RH
  beyond resolution tolerance — the "shock" is an artifact or the
  fields are mutually inconsistent (e.g., interpolated
  independently). **[PS** for the tolerance propagation**]**
- **A4 Entropy admissibility.** s(T,p) non-decreasing across each
  shock in crossing direction; no expansion shocks; pointwise
  s ≥ s_min(feed) − k_c·U(s). **Reject:** any entropy-decreasing
  jump above uncertainty. **[CP** criterion; **[MA]** tolerance**]**
- **A5 Realizability & window.** ess-range(Q̂) ⋐ 𝒰 with margin:
  ρ > 0, p > 0, T ∈ [T⁻ + ΔT_guard, T⁺ − ΔT_guard] (caloric-table
  window with guard band ≥ k_c·U(T)). **Reject:** any excursion —
  the downstream caloric model is undefined there. **[CP** set
  check; **[MA]** guard**]**
- **A6 Mode purity / periodicity.** (i) e_RW ≤ ε_RW (Def 2.2);
  (ii) spectral comb test: energy off the wave-locked comb
  { n·N|Ω|/2π } below declared fraction; (iii) spectrogram
  stationarity: instantaneous frequency variance over the record
  below tolerance (guards mode-hopping WITHIN the record);
  (iv) ℤ_N residual (Claim 2.5) below tolerance (guards
  wave-to-wave asymmetry against (H-ID)). **Reject:** any of the
  four. **[MA]**
- **A7 Statistical convergence.** The phase-locked average Q̂ built
  from M cycles: split-half comparison (first M/2 vs second M/2)
  within the standard error; standard error of cycle-mean
  functionals (thrust-relevant fluxes) below a declared fraction of
  design tolerance; record-level stationarity (e.g., reverse
  arrangements test on cycle-wise functionals). **Reject:** split
  halves differing beyond k_c × SE, or SE above budget ⇒ record too
  short. **[MA** — standard test-data statistics**]**
- **A8 Character census.** Fraction of 𝕋 × [r_i,r_o] with
  M_n ≤ 1 + k_c·U(M_n) compared against the declared β of P3;
  sonic-line stability under recomputation (Claim 4.3).
  **Reject:** budget exceeded, or χ unstable within U. **[MA]**
- **A9 Numerical provenance (CFD).** Grid/time-step convergence of
  the DELIVERED FUNCTIONALS (fluxes, e_RW, χ-census — not just
  global residuals): observed order within the scheme's theoretical
  band, GCI below budget; iterative and statistical-sampling errors
  separated and quoted. **Reject:** erratic observed order or GCI
  above budget — the datum is discretization-contaminated. **[MA**
  — ASME V&V-20-style practice**]**
- **A10 Measurement provenance (rig).** (i) temporal bandwidth:
  sensor + acquisition chain flat (within calib. tolerance) up to
  n_max·N|Ω|/2π, with declared n_max set by the shock rise time;
  anti-aliasing verified; (ii) SPATIAL aliasing: probe count per
  annulus > 2·n_max·N (Nyquist in wavenumber) or a declared model-
  based reconstruction with its own uncertainty; (iii) calibration
  traceability and install effects (recess, line-cavity resonance)
  characterized IN BAND; (iv) probe intrusiveness bounded (blockage
  ratio, bow-shock standoff vs measurement volume). **Reject:** any
  chain element failing in-band verification voids the affected
  field components. **[MA]**
- **A11 Reduction-loss disclosure.** If the phase-family reduction
  (3.2) is used downstream: measured k, azimuthal/axial flux ratio,
  and the 3.3b bound evaluated and below the design tolerance; if
  the mean datum appears anywhere in the pipeline, its O(Var) error
  declared (3.5). **Reject:** undisclosed or over-budget loss.
  **[MA]**
- **A12 Identity & chirality declaration.** (N, sign Ω, Ω with
  uncertainty) declared; consistency between declared Ω and the
  comb of A6; chirality consistent with the sign conventions of the
  swirl field v_θ. **Reject:** mismatch (a mirrored or mislabeled
  datum silently flips the swirl seen by the design). **[CP** —
  consistency check**]**

**Claim 6.1 (gauntlet completeness relative to derivation).** A1–A12
cover exactly the failure modes surfaced by §§1–5: placement (P1–P5
↔ A1,A2,A5,A8,A9,A10), structure (H-ID/H-RW ↔ A6), statistics
(A7), constraint structure (Claim 2.6 ↔ A1–A4), reduction (A11),
character/closure (A8 ↔ §4), identity (A12), with causality carried
by the separate live monitors C-i..C-iv (§5, run at acceptance AND
during any design campaign). No claim of absolute completeness is
made: the list is falsifiable as a list. **[MA]**
**Reject:** exhibit a datum passing all of A1–A12 + C-i..C-iv that
still yields a downstream-verified thrust error beyond quoted
uncertainty; the exhibited failure mode then names the missing
audit.

---

## 7. UNCERTAINTY — the datum as a delivered, uncertain object

**Def 7.1 (the certified datum).** What the design program may
consume is never a bare field but the tuple
𝒟 := ( Q̂, (N, Ω), χ, U, W, 𝒫 )
with:
- Q̂ the nominal phase profile (Def 2.2), delivered in a declared
  discretization with its reconstruction operator;
- (N, Ω) the mode identity with uncertainties;
- χ the character map with its UNKNOWN band (Claim 4.3);
- U the uncertainty specification (Def 7.2);
- W the validity window (Def 7.3);
- 𝒫 the provenance dossier: which of A1–A12 ran, with numbers, plus
  the raw-record retention pointer (re-audit must be possible).
**[MA** — a data-product definition**]**
**Reject:** a delivery missing any component is rejected
administratively — the audits of §6 cannot even be re-run.

**Def 7.2 (uncertainty specification U — three admissible grades).**
Ordered by strength; the grade must be declared:
- **(U-a) Norm-ball / band:** Q ∈ Q̂ + B_ε in a DECLARED norm pair:
  L^∞(𝕋 × [r_i,r_o]) for realizability-critical components (A5
  guards live here) AND a flux-weighted L² norm
  ‖δQ‖_*² := ∫ |G(φ,r) · δQ|² dφ dr, where G is the Gâteaux
  derivative (sensitivity) of the thrust functional composed with
  the downstream solve, evaluated at Q̂ — i.e., the metric is
  CALIBRATED TO THE DESIGN TARGET, so that ‖δQ‖_* directly bounds
  first-order thrust error. Cheapest; supports worst-case
  (robust) design only.
- **(U-b) Parametric covariance:** uncertainty carried on a
  finite modal parameterization of Q̂ (Fourier in φ ⊗ radial modes,
  or POD of the delivered cycles), with covariance Σ estimated from
  cycle-to-cycle scatter and provenance budgets (A9/A10 terms
  entered as independent components). Supports linearized UQ
  propagation (adjoint/sensitivity × Σ).
- **(U-c) Measure-valued:** a probability law on the datum space
  (samples = bootstrap over cycles + provenance perturbations),
  pushforward through the design map for full thrust UQ. Most
  expensive; required only when the design verdict is
  distribution-sensitive. **[MA** — UQ architecture; the
  norm-calibration statement in U-a is **[PS]** (first-order
  functional calculus)**]**
**Reject (per grade):** U-a: a validation perturbation δQ inside the
band that produces thrust change beyond the band's implied bound
rejects the calibration of G; U-b: cycle-resampled Σ failing a
split-half stability test rejects the covariance; U-c: pushforward
prediction interval failing empirical coverage on a hold-out
configuration rejects the law.

**Def 7.3 (validity window W).** The datum certifies an OPERATING
BOX, not a point: intervals for (ṁ_feed, equivalence ratio/mixture
spec upstream of the frozen cut, backpressure seen by the combustor,
ambient/installation states), plus the regime certificate (N, Ω
stable per A6, C-iii) over that box. Design evaluations are
admissible ONLY inside W; any excursion is EXTRAPOLATION and is
rejected, not error-barred (mode bifurcation B3 makes extrapolation
across regime boundaries meaningless — the map is discontinuous).
**[MA]**
**Reject:** a design verdict quoting 𝒟 outside W is rejected at
review; W itself is falsified if a within-window replication shows
regime change (then W was drawn too wide and must be re-certified).

**Claim 7.4 (robustness obligation on the consumer).** A design
program consuming 𝒟 must return, with any optimal design g*,
either (i) a worst-case certificate: bound on thrust degradation
over the declared U (grade U-a/b/c respectively by min-max,
sensitivity ellipsoid, or quantile), or (ii) at minimum the
directional sensitivities of the objective along the dominant
uncertainty modes, compared against the design margin. An optimum
whose claimed advantage over a competitor is smaller than the
U-propagated thrust uncertainty is REPORTED AS A TIE. **[MA** — UQ
decision policy**]**
**Reject:** re-optimization at perturbed data within U flipping the
ranking of designs quoted as distinct rejects the quoted verdict
(the concrete test: k_c-scaled datum perturbations along the top
covariance modes; ranking must be stable).

**Claim 7.5 (uncertainty–structure coupling).** U is not independent
of the structure of §§2–5: (i) the phase-gauge (N4) must be quotiented
before computing scatter (align cycles by cross-correlation phase
shift, THEN average — otherwise wave jitter masquerades as amplitude
uncertainty and inflates U near shocks by O(jitter × slope));
(ii) uncertainty near the sonic line feeds the χ UNKNOWN band
(Claim 4.3), coupling U to well-posedness; (iii) the causality
margin δ (Claim 5.1) consumes U(M_n): a larger measurement
uncertainty directly weakens the legitimacy certificate of the cut.
**[PS** for (i) (first-order error model of misaligned averaging);
**[MA]** for the policy couplings**]**
**Reject:** (i) is tested by synthetic resampling: impose known
jitter on a clean synthetic Q, verify the aligned estimator recovers
amplitude uncertainty within its stated bars while the naive one
fails; failure of the aligned estimator on synthetics rejects the
alignment procedure.

---

## 8. Contract summary (one screen)

1. **Cut placement:** fixed annular station; frozen chemistry,
   common geometry, declared subsonic budget β, established
   periodicity, deliverable bandwidth (P1–P5). Prefer the most
   upstream station with β = 0.
2. **Datum:** BV∩L^∞ realizable field on 𝕋_τ × A; equivalently, under
   (H-ID)+(H-RW), a steady phase profile Q on 𝕋 × [r_i,r_o] plus
   (N, Ω, chirality). Helical symmetry inherited; axisymmetry,
   mirror symmetry, time-reversal NOT. The Young-measure form is for
   diagnostics/UQ only — it drops inter-point phase correlation.
3. **Reduction:** wave-frame steadiness is EXACT (axisymmetric
   nozzle) but 3D; the per-phase steady family is approximate with
   error O(reduced frequency k) + O(azimuthal-flux ratio) — at
   kHz, CHECK, don't assume; carry the loss by linear corrector or
   calibrated bracket; never solve the averaged datum and call it
   the average (Jensen).
4. **Well-posedness:** prescribe 5 components where M_n > 1, only 4
   where M_n < 1 with a declared closure (characteristic-coupled or
   non-reflecting), never 5 on subsonic patches; the character map χ
   with its uncertainty band ships with the datum.
5. **Causality:** legitimate cut ⟺ uniformly supersonic normal
   outflow with a k_c·U(M_n) margin; monitors = margin census,
   design-sweep invariance (the primary falsifier), mode identity,
   upstream-wave detector; mode bifurcation voids the datum
   entirely.
6. **Acceptance:** gauntlet A1–A12 (budgets, internal jump/entropy
   consistency, realizability, mode purity, statistical
   convergence, character census, CFD/rig provenance, reduction
   disclosure, identity) — every audit with a derived tolerance and
   a rejecting outcome.
7. **Uncertainty:** the deliverable is (Q̂, (N,Ω), χ, U, W, 𝒫);
   U in a thrust-calibrated metric (plus L^∞ realizability guard) at
   a declared grade (band / covariance / law); validity window with
   extrapolation forbidden across regime boundaries; consumer owes a
   robustness certificate, ties reported as ties.
