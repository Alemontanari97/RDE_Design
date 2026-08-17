# BLIND DERIVATION — The interface datum for a rotating-detonation exhaust cut
## Lens: hyperbolic PDE theory and trace/boundary-value structure

Independent derivation from the blind brief only. No repository material
consulted. Rigor classes per claim: **[PROOF]** = complete proof given or
one-line-checkable; **[SKETCH]** = proof sketch, gaps named; **[MODEL]** =
modeling assertion, not a theorem. Every numbered item carries a test
`TEST:` that could reject it.

---

## §0 Standing model, notation, hypotheses

**Geometry.** Cylindrical coordinates $(r,\theta,z)$, annulus
$A = [r_i, r_o] \times S^1_\theta$, $0 < r_i < r_o$. The candidate interface is
$\Sigma_c = A \times \{z = z_I\}$, unit normal $\nu = e_z$ pointing into the
downstream (design) domain $D \subset \{z > z_I\}$. $D$ is bounded by $\Sigma_c$,
solid walls $\Gamma_w$ (design variable), and an outlet $\Gamma_{out}$.

**State space.** Conservative state $U = (\rho, \rho u, \rho E) \in \mathbb{R}^5$,
primitive $V = (\rho, u, T)$, $u = (u_r, u_\theta, u_z)$,
$E = e(T) + \tfrac12 |u|^2$. Admissible set
$\mathcal{K} = \{ \rho \in [\rho_-, \rho_+],\ T \in [T_-, T_+],\ |u| \le u_+ \}$,
a fixed compact subset of $\{\rho > 0, T > 0\}$.

**(H-th) Thermodynamic hypotheses** [MODEL, standard]. Frozen composition:
mass-fraction vector $Y$ constant on $\overline{D}$ (see (P1), §1). Thermally
perfect mixture: $p = \rho \bar R T$, $\bar R = R_u \sum_k Y_k / W_k$;
$e(T) = \sum_k Y_k e_k(T)$ with $c_v(T) = e'(T) > 0$,
$c_p(T) = c_v(T) + \bar R$; sound speed $a(T)^2 = \gamma(T)\bar R T$,
$\gamma = c_p/c_v \in (1, 5/3]$ on $[T_-,T_+]$. Specific entropy
$s(T,p) = \int^T c_p(\tau)\,d\tau/\tau - \bar R \ln p$. These give a strictly
convex mathematical entropy $\eta(U) = -\rho s$ with flux $q = -\rho s u$, and a
genuinely-nonlinear/linearly-degenerate characteristic structure identical in
type to the polytropic case (Weyl-type gas).
`TEST:` tabulate $c_p(T)$ on $[T_-,T_+]$; any $T$ with $c_v \le 0$ or
$\partial^2(\rho e)/\partial(\cdot)^2$ losing convexity rejects (H-th) and with
it every claim below that invokes strict hyperbolicity or entropy convexity.

**Equations on $D$.** Non-reacting compressible Euler,
$\partial_t U + \nabla \cdot F(U) = 0$, with normal flux map
$$ F_\nu(U) = \big(\rho u_\nu,\ \rho u\, u_\nu + p\,\nu,\ (\rho E + p) u_\nu\big),
\qquad u_\nu = u \cdot \nu . $$
Normal Jacobian $A_\nu(U) = DF_\nu$ has eigenvalues
$$ \lambda_1 = u_\nu - a, \quad \lambda_{2,3,4} = u_\nu \ (\text{entropy + 2 shear}),
\quad \lambda_5 = u_\nu + a. \tag{0.1} $$
[PROOF] — direct computation, standard for any $p = p(\rho, e)$ with
$p_\rho + p\,p_e/\rho^2 = a^2 > 0$.
`TEST:` symbolic/numeric eigendecomposition of $A_\nu$ at sampled
$\mathcal{K}$-states; any eigenvalue off (0.1) beyond roundoff rejects.

**Kinematics of the cycle.** The combustor sustains $m \ge 1$ waves rotating at
pattern angular velocity $\Omega \ne 0$ (sign = chirality). Period at a fixed
azimuthal station: $T_{per} = 2\pi/(m|\Omega|)$ if the $m$ waves are identical,
$2\pi/|\Omega|$ otherwise.

---

## §1 WHERE: placement of the interface

**D1.1 (Interface surface).** An interface placement is a choice of $z_I$ (more
generally a Lipschitz surface $\Sigma$ transverse to $e_z$; we take the flat
annulus, and record below where flatness is used: only in the convenience of
$\nu = e_z$; all claims hold for a fixed Lipschitz $\Sigma$ with a.e. normal).

**D1.2 (Admissible placement).** $\Sigma$ is *admissible for the cut* if all of
(P1)–(P6) hold, each uniformly over the cycle and over the intended operating
window:

- **(P1) Chemical frozenness** [MODEL]. On $\{z \ge z_I\}$ the reaction source
  $\dot\omega(\rho,T,Y)$ satisfies
  $\tau_{res}\,\|\dot\omega\|/\|Y\| \le \varepsilon_{chem}$, with $\tau_{res}$ the
  downstream residence time. Equivalently a Damköhler smallness condition.
  `TEST:` evaluate a full kinetic mechanism at the delivered datum states; if
  predicted composition drift over $\tau_{res}$ exceeds $\varepsilon_{chem}$, the
  placement (not the datum) is rejected — move $\Sigma$ downstream.
- **(P2) Uniform outflow** [MODEL as a fact about the flow; checkable].
  $\operatorname*{ess\,inf}_{\Sigma \times \text{cycle}} u_\nu \ge \delta_0 > 0$: no
  backflow at any phase.
  `TEST:` scan the datum; any cell/phase with $u_\nu \le \delta_0$ rejects.
- **(P3) Uniform characteristic signature** [MODEL]. Either
  (P3-S) $\operatorname*{ess\,inf} (u_\nu - a) \ge \delta_1 > 0$ (uniformly
  supersonic cut), or, if that is unattainable,
  (P3-s) $\operatorname*{ess\,sup} (u_\nu - a) \le -\delta_1 < 0$ (uniformly
  subsonic), with the signature *constant in phase and position*. Mixed or
  phase-crossing signature is inadmissible (the number of prescribable data
  would change with phase; the sonic set on $\Sigma$ is a free boundary of the
  prescription problem).
  `TEST:` compute $\operatorname{sign}(u_\nu - a)$ over $\Sigma \times$ cycle;
  nonconstant sign, or margin $< \delta_1$, rejects the placement class claimed.
- **(P4) Geometric fixity** [MODEL]. $\Sigma$ and everything upstream of it are
  identical for *every* member of the design family; the design variable acts
  only on $\Gamma_w \subset \{z > z_I\}$.
  `TEST:` inspection of the design parameterization; any design parameter whose
  support touches $\{z \le z_I\}$ rejects.
- **(P5) Model validity** [MODEL]. Inviscid-core adequacy at $\Sigma$:
  displacement thickness $\ll r_o - r_i$, no separation at the wall circles.
  `TEST:` boundary-layer estimate from upstream data; violation rejects.
- **(P6) Mode-locked stationarity** [MODEL]. Over the averaging record, $m$
  is constant and $\Omega$ drifts by less than $\varepsilon_\Omega$ relative.
  `TEST:` spectrogram of a probe signal; mode transition or drift beyond
  $\varepsilon_\Omega$ rejects.

**C1.1 (Placement = noncharacteristic boundary)** [PROOF]. Under (P2) and
(P3), $\Sigma$ is uniformly noncharacteristic for (0.1): no eigenvalue of
$A_\nu$ vanishes on the datum range, with a uniform gap
$\min(\delta_0, \delta_1)$. *Proof.* The eigenvalues are (0.1); $u_\nu \ge \delta_0$
kills $\lambda_{2,3,4} = 0$ and $\lambda_5 = 0$; $|u_\nu - a| \ge \delta_1$ kills
$\lambda_1 = 0$. $\square$ This is precisely the hypothesis under which
hyperbolic trace and IBVP theory (Kreiss–Sakamoto class, BV one-sided traces)
is available; i.e., **the placement conditions are exactly the hypotheses of
the boundary-value theory**, not extra physics.
`TEST:` inherited from (P2)/(P3) tests.

**C1.2 (Invalidation catalogue)** [MODEL]. A previously admissible placement is
invalidated by: (i) appearance of a subsonic pocket or backflow interval
(throttled operation, nozzle unstart) — violates (P2)/(P3); (ii) wave-mode
transition $m \to m'$ or chaotic/longitudinal-pulsed contamination — violates
(P6) and D2.2; (iii) afterburning reaching $\Sigma$ (equivalence-ratio change) —
violates (P1); (iv) a design excursion that moves geometry or its upstream
influence across $\Sigma$ — violates (P4) or §5; (v) an upstream-running shock
crossing $\Sigma$ (unstart) — violates (P2)/(P3) dynamically.
`TEST:` each maps to a monitor in §5–§6; firing monitor = invalidated placement.

**Remark 1.3 (placement band, honest tension).** (P1) pushes $\Sigma$
downstream; (P4) and the wish for a large design domain push it upstream; §3
will show the *phase-family* reduction also prefers downstream placement (decay
of azimuthal nonuniformity), while a strong "cycle" content requires upstream
placement. Admissibility is therefore a *band* $[z_I^-, z_I^+]$, possibly
empty; emptiness is a legitimate negative verdict on the whole cut strategy for
a given machine, and the tests above decide it.

---

## §2 WHAT: the datum, mathematically

**D2.1 (Datum as trace)** [definition + PROOF of existence under stated
regularity]. Let $U^{up}$ be the upstream flow on a neighborhood
$\mathcal{N} = A \times (z_I - h, z_I] \times \mathbb{R}_t$, an entropy solution of
the (possibly still weakly reacting, per (P1) approximately homogeneous) Euler
system, with $U^{up} \in L^\infty(\mathcal{N}; \mathcal{K})$.

- *Minimal (flux) trace.* Since each component of
  $(U^{up}, F(U^{up}))$ is a bounded divergence-measure field (the equations
  hold with bounded source), the **normal flux trace**
  $\mathcal{F} := F_\nu(U^{up})|_\Sigma \in L^\infty(\Sigma \times \mathbb{R}_t;
  \mathbb{R}^5)$ exists in the Chen–Frid (Gauss–Green) sense. [SKETCH — the
  Chen–Frid normal-trace theorem for $\mathcal{DM}^\infty$ fields over Lipschitz
  boundaries; sketch because the trace is a priori only a functional on
  boundary test functions, upgraded to an $L^\infty$ function on flat $\Sigma$.]
- *Strong (state) trace.* If moreover
  $U^{up} \in BV_{loc}(\mathcal{N})$, the one-sided **state trace**
  $U_\Sigma := U^{up}|_{\Sigma^-} \in BV(\Sigma \times (0,T_{per}))$ exists a.e.
  (Vol'pert one-sided traces of BV functions on a Lipschitz surface
  transverse to the jump set) and $\mathcal{F} = F_\nu(U_\Sigma)$ a.e. [PROOF for
  the BV statement, classical.]

The **datum** is $U_\Sigma$ when it exists (supersonic cut needs it, §4), else
$\mathcal{F}$ plus partial state information (subsonic cut, §4). Working
regularity class, justified by the physics (shock remnants sweep $\Sigma$):
$$ U_\Sigma \in BV \cap L^\infty(A \times S^1;\ \mathcal{K}),
\quad \text{piecewise } C^1 \text{ with finitely many Lipschitz jump curves.} $$
`TEST:` mesh/record-refinement Cauchy test — integrated fluxes and TV norms of
the delivered datum must stabilize under refinement; unbounded TV growth
rejects the BV class (and demotes the datum to flux-trace-only status).

**D2.2 (Rotating-wave form; the datum triple)** [MODEL for the exactness of
the form; the brief's stated observation]. The pure-periodic hypothesis is:
$$ \textbf{(H-RW)} \qquad U_\Sigma(r, \theta, t) = \hat U(r, \theta - \Omega t),
\qquad \hat U : A \to \mathcal{K}, \ \hat U \in BV \cap L^\infty, $$
with $\mathbb{Z}_m$ refinement $\hat U(r, \theta + 2\pi/m) = \hat U(r,\theta)$ if
the $m$ waves are identical. Under (H-RW) the full datum is the finite object
$$ \boxed{\ \mathcal{D} = (\hat U,\ \Omega,\ m;\ Y,\ \text{thermo tables})\ } $$
— one BV annulus field, one frequency, one integer, plus the frozen mixture.
Time-dependence is not extra data; it is the group orbit of $\hat U$.
`TEST:` rotating-frame residual
$\rho_{RW} := \| U_\Sigma(\cdot,\cdot,t) - \hat U(\cdot, \cdot - \Omega t) \|_{L^2(A)}
/ \|\hat U\|_{L^2}$ over the record, with $\hat U$ fitted by phase-aligned
averaging; $\rho_{RW} > \varepsilon_{RW}$ rejects (H-RW) (see audit A3, §6).

**D2.3 (Three representations of the cycle, and their exact hierarchy).**

1. **(T)** Time-periodic boundary function
   $U_\Sigma \in L^\infty(\mathbb{R}_t; BV(A))$, $T_{per}$-periodic.
2. **(L)** A **loop of steady data**: $\phi \in S^1 \mapsto
   \hat U_\phi := \hat U(\cdot, \cdot - \phi) \in BV(A)$ — a continuous (in
   $L^1(A)$) closed curve in datum space. Under (H-RW), (T) $\equiv$ (L)
   *exactly*: $U_\Sigma(t) = \hat U_{\Omega t}$. [PROOF — substitution; the
   $L^1$-continuity of translation on $BV \subset L^1$ is standard.]
3. **(M)** The **one-point cycle measure**: for each $x \in A$, the
   push-forward $\mu_x := (\phi \mapsto \hat U(x_{-\phi}))_\# \mathrm{Haar}(S^1)
   \in \mathcal{P}(\mathcal{K})$ — a Young-measure-like statistical datum.

**C2.1 (What each representation supports)** [PROOF for the identities,
one-line each].
(i) (T)$\Rightarrow$(L) loses nothing under (H-RW); without (H-RW), (L) does
not exist and (T) is the only faithful form.
(ii) (L)$\Rightarrow$(M) is a strict loss: it forgets phase ordering and all
multi-point (in $x$ and $\phi$) correlations.
(iii) For any pointwise nonlinear observable $g$,
$$ \frac{1}{T_{per}} \int_0^{T_{per}} g(U_\Sigma(x,t))\, dt
 \;=\; \int_{\mathcal{K}} g \, d\mu_x
 \;=\; \frac{m}{2\pi} \int_{0}^{2\pi/m} g(\hat U(r, \alpha))\, d\alpha
 \tag{2.1} $$
(time average = cycle-measure average = wave-frame azimuthal average).
[PROOF — change of variables $\alpha = \theta - \Omega t$ and periodicity.]
Hence: **one-point averages at $\Sigma$ (including all cycle-averaged fluxes)
need only (M); downstream *propagation* through the nonlinear system needs (L)
(equivalently (T))**, because the Euler evolution does not factor through
one-point marginals.
`TEST:` for (2.1): numerically compare the three averages of $g = p$, $\rho u_z^2$,
$\rho u_z H$ on a delivered record; disagreement beyond quadrature error
rejects (H-RW) or the record's periodicity, not (2.1) itself (which is exact).

**C2.2 (Symmetries inherited and not)** [PROOF for the group statements given
(H-RW); MODEL for which symmetries the physics actually delivers].
Inherited by $\mathcal{D}$: (a) the **helical symmetry** — invariance under the
one-parameter group $g_s: (\theta, t) \mapsto (\theta + \Omega s, t + s)$; time
translation and azimuthal rotation are *not* separately inherited, only their
locked combination; (b) $\mathbb{Z}_m$ discrete rotation if the waves are
identical. **Not inherited**: (c) axisymmetry ($\hat U$ genuinely depends on
$\theta$ — otherwise the cycle is empty); (d) the reflection
$\theta \mapsto -\theta$ (chirality of the rotation direction: $O(2)$ is broken
to $SO(2)$-locked-with-time); (e) time reversal (entropy production in the
detonation); (f) steadiness.
`TEST:` (b): $\|\hat U(\cdot, \cdot + 2\pi/m) - \hat U\|_{L^1}$ beyond tolerance
rejects the $\mathbb{Z}_m$ claim (audit A9); (d): a delivered datum with
reflection symmetry to tolerance is *suspicious* (over-symmetrized synthetic
data) and triggers provenance review.

---

## §3 STRUCTURE: exact and approximate reductions to steady data

Three distinct reductions. Only the first two are exact; their hypotheses
differ and must not be conflated.

**C3.1 (R1: exact wave-frame steady reduction of the coupled problem)**
[SKETCH, conditional]. Hypotheses:
(H1) = (H-RW) exactly; (H2) $D$ axisymmetric (walls and outlet surfaces of
revolution); (H3) downstream boundary conditions rotation-invariant; (H4) the
downstream IBVP with datum $U_\Sigma$ has a unique solution in a class
$\mathcal{X}$ closed under the symmetry action; (H5) the long-time limit (the
attractor actually computed/designed for) is unique, independent of admissible
initial data, and stable.
*Claim.* The attractor has the rotating-wave form
$U(r,\theta,z,t) = \tilde U(r, \theta - \Omega t, z)$, and $\tilde U$ solves the
**steady** system in wave coordinates $\alpha = \theta - \Omega t$:
$$ \frac{1}{r}\partial_\alpha \big[ F_\theta(\tilde U) - \Omega r\, \tilde U \big]
 + \frac{1}{r}\partial_r \big[ r F_r(\tilde U) \big]
 + \partial_z F_z(\tilde U) = 0 \tag{3.1} $$
with boundary datum $\hat U$ on $\Sigma$.
*Sketch.* By (H2)–(H3) the solution operator commutes with $g_s$ of C2.2; by
(H1) the boundary datum is $g_s$-invariant; hence $g_s$ maps the attractor to
itself for every $s$; by uniqueness (H4)–(H5) the attractor is a fixed point of
the whole group, which is exactly the stated form; substitution
$\partial_t \to -\Omega \partial_\alpha$ gives (3.1). Gaps: (H4)–(H5) are unproven
for 3D Euler (no uniqueness theory in this class); symmetry of the attractor
can fail by spontaneous symmetry breaking even when (H1)–(H3) hold. Hence
conditional. **Nothing is lost by (R1) when its hypotheses hold** — it is a
change of variables, not an approximation.
`TEST:` run the unsteady downstream problem to its attractor with a
rotating-wave inlet in an axisymmetric nozzle; the symmetry defect
$\sup_s \|U(t+s) - g_s U(t)\|_{L^1(D)}$ failing to vanish (relative tolerance)
rejects (H5)-with-symmetry, and with it the applicability of (R1).

**C3.2 (Wave-frame azimuthal hyperbolicity)** [PROOF given (H-th)]. In (3.1)
the azimuthal direction is *timelike* wherever the wave-frame azimuthal speed
is supersonic: $|u_\theta - \Omega r| > a$. Since $|\Omega| r$ is of the order of
the detonation speed ($\gg a$ of the burned gas) while $|u_\theta| \lesssim a$,
this holds throughout $\mathcal{K}$ in the intended regime; then (3.1) is
symmetrizable-hyperbolic with $\alpha$ as evolution variable, and the steady
wave-frame problem can in principle be *marched in azimuth* — the periodic
orbit in $\alpha$ replacing time-periodicity. *Proof:* the $\alpha$-Jacobian is
$A_\theta(U)/r - \Omega\,\mathrm{Id}$ with eigenvalues
$(u_\theta - \Omega r \pm a)/r$, $(u_\theta - \Omega r)/r$; all of one sign iff
$|u_\theta - \Omega r| > a$. $\square$
`TEST:` evaluate $\min_{\mathcal{K}} (|u_\theta - \Omega r| - a)$ on the delivered
datum range; $\le 0$ anywhere rejects the marching structure (not (R1) itself).

**C3.3 (R2: exact azimuthal-average flux identity)** [PROOF]. Let
$\langle \cdot \rangle$ denote the average over $\alpha \in S^1$ at fixed $(r,z)$.
Averaging (3.1) kills the $\alpha$-divergence exactly (periodicity):
$$ \frac{1}{r} \partial_r \big[ r \langle F_r(\tilde U)\rangle \big]
 + \partial_z \langle F_z(\tilde U) \rangle = 0. \tag{3.2} $$
The **averaged fluxes** satisfy steady axisymmetric conservation exactly; but
(3.2) is *not closed*: $\langle F(\tilde U)\rangle \ne F(\langle \tilde U\rangle)$;
the defect is the flux covariance ("wave stress")
$ \mathcal{R} := \langle F(\tilde U)\rangle - F(\langle \tilde U \rangle) $,
the exact analogue of a Reynolds stress with the cycle playing the role of the
ensemble. By (2.1), the cycle-averaged fluxes *at $\Sigma$* are data:
$\langle \mathcal{F} \rangle$ is computable from $\mathcal{D}$ alone. $\square$
`TEST:` on any resolved unsteady solution, evaluate the residual of (3.2) with
measured averaged fluxes; nonzero beyond discretization error rejects the
computation (the identity is exact).

**D3.1 (Flux-equivalent steady datum) and C3.4 (two-branch inversion)**
[SKETCH]. Given the averaged normal-flux triple per point,
$(\bar m, \bar \Pi, \bar h) := \langle (\rho u_\nu,\ \rho u_\nu u + p\nu,\ \rho u_\nu H)\rangle$,
define the equivalent steady state $U^*$ by $F_\nu(U^*) = (\bar m, \bar\Pi, \bar h)$
(tangential momentum components give $u^*_t$ directly as $\bar\Pi_t/\bar m$).
*Claim.* For a thermally perfect gas with $c_p(T) > \bar R$ on $[T_-, T_+]$ and a
strictly admissible triple (positive mass flux, attainable impulse/enthalpy
pair), the normal 1D inversion has **exactly two** solutions, one with
$u^*_\nu < a^*$ and one with $u^*_\nu > a^*$ (the classical subsonic/supersonic
impulse pair), merging at the sonic point. *Sketch:* parameterize by Mach
number; the impulse function per unit mass flux,
$I(M) = (1 + \gamma(T) M^2)/ (M\,\Gamma(T))$ along the fixed-$(\bar m, \bar h)$
manifold, is strictly decreasing for $M<1$ and increasing for $M>1$ for any
$\gamma(T) \in (1, 5/3]$; variable $c_p(T)$ deforms but does not destroy the
monotonicity under (H-th) — the gap in the sketch is the uniformity of this
monotonicity for strongly varying $c_p$, checkable per table. **The branch must
be selected by the placement class (P3):** supersonic cut $\Rightarrow$
supersonic branch. Non-attainable triples (violating the sonic bound) admit
no $U^*$: the averaged data of a genuinely unsteady flow need not be
realizable by any steady state — this is a *feature* (rejection channel), not
a defect.
`TEST:` numeric inversion on the delivered $\langle \mathcal{F}\rangle$ with the
actual $c_p$ table; zero or $>2$ solutions, or branch mismatch with (P3),
rejects (respectively) attainability, the monotonicity sketch, or the
placement declaration.

**C3.5 (What (R2) preserves and loses)** [PROOF for the preservation; MODEL
for the loss estimate]. The design target is a time-averaged **flux**
functional (thrust = averaged momentum flux + pressure integrals). By (2.1),
$U^*$ of D3.1 reproduces *exactly* the cycle-averaged mass, momentum (all
components), and energy fluxes **through $\Sigma$**. What it does not
reproduce: the downstream *evolution* — the deviation field
$\tilde U - \langle\tilde U\rangle$ propagates nonlinearly and feeds back on the
mean through $\mathcal{R}$ of C3.3; the exit-plane averaged fluxes of the true
unsteady solution and of the steady solution fed by $U^*$ differ at second
order in the deviation amplitude $\epsilon := \|\hat U - \langle \hat U\rangle\|
/ \|\langle\hat U\rangle\|$ (quadratic flux covariance), with no sign
guarantee. Carrying the loss: either (i) bound it — $|\Delta QoI| \le
C \epsilon^2$ with $C$ from a computed linearized (adjoint) sensitivity plus a
measured $\mathcal{R}$ at $\Sigma$ [MODEL until the linearization is certified];
or (ii) close (3.2) with the measured $\mathcal{R}$ transported by a declared
model [MODEL, price: a new modeling layer with its own audit].
`TEST:` two-point Richardson-type check — run the (available) unsteady
downstream problem at two deviation amplitudes ($\hat U$ scaled toward its
mean); QoI error failing to scale $\sim \epsilon^2$ rejects the quadratic-loss
claim; any use of (R2) beyond $\Sigma$ without a declared $\mathcal{R}$ closure
rejects by audit (§6, A12).

**C3.6 (R3: phase-family quasi-steady reduction — approximation, with an
honest defect bound)** [PROOF for the defect identity; MODEL for smallness].
The common engineering reduction: for each phase $\phi \in S^1$, feed a
*steady* downstream solve with the frozen datum slice, and average the QoI
over $\phi$. In wave coordinates this is exactly the act of **dropping the
$\alpha$-divergence term in (3.1) pointwise** (not in average). The defect is
the measure
$$ \mathcal{R}_\phi = \frac1r \partial_\alpha\big[ F_\theta(\tilde U) - \Omega r \tilde U \big],
\qquad |\mathcal{R}_\phi|(A) \;\le\; \frac{1}{r_i}\,
 \sup_{\mathcal{K}} \big| A_\theta - \Omega r\,\mathrm{Id} \big| \; \mathrm{TV}_\alpha(\tilde U)
 \;\le\; \frac{(|u_\theta - \Omega r| + a)_{\max}}{r_i}\, \mathrm{TV}_\alpha(\tilde U).
 \tag{3.3} $$
[PROOF of (3.3) as a BV chain-rule bound.] The coefficient is
$O(|\Omega| r)$ — detonation-speed order, **large**. Therefore (R3) is *not*
justified by any smallness of $\Omega$; it is admissible only when
$\mathrm{TV}_\alpha(\hat U)$ itself is small at $\Sigma$ (azimuthal nonuniformity
already decayed — downstream placement), or for QoI components for which the
$\alpha$-divergence integrates away (the $\Sigma$-averaged fluxes, where (R3)
coincides with (R2)). Declared admissibility number:
$\delta_{qs} := (|u_\theta - \Omega r| + a)_{\max} \mathrm{TV}_\alpha(\hat U) \big/
\big( r_i \|\partial_z F_z\|_{est} \big) \ll 1$.
`TEST:` compute $\delta_{qs}$ from the delivered datum and a one-shot estimated
axial flux gradient; $\delta_{qs} \ge 1$ rejects (R3) for pointwise/downstream
use (it remains usable only in its (R2)-coincident averaged role). A stronger
rejector where affordable: compare (R3) against one resolved unsteady run;
per-phase field errors exceeding the (3.3)-propagated bound reject the bound's
constants.

**Summary of §3.** (R1) exact, conditional on symmetry+uniqueness hypotheses;
(R2) exact as a flux statement, not closed, preserves the QoI *at* $\Sigma$
verbatim; (R3) approximate with an explicitly large-coefficient defect (3.3),
legitimate only under measured azimuthal-decay smallness. Any pipeline claim
of "steady family, exactly" must name which of the three it means; conflation
of (R3) with (R1)/(R2) is the single most likely structural error and is
rejectable by the $\delta_{qs}$ test alone.

---

## §4 WELL-POSEDNESS: what may be prescribed where, and closures

**C4.1 (Characteristic counting at $\Sigma$)** [PROOF — linear algebra (0.1) +
classical hyperbolic IBVP counting]. Let $\nu$ point into $D$ (flow
direction). The number of scalar boundary conditions the downstream problem
accepts at a boundary point equals the number of positive eigenvalues of
$A_\nu$ (characteristics entering $D$):

| Regime at the point | $\lambda$ signs | # data prescribed | # returned upstream |
|---|---|---|---|
| supersonic inflow $u_\nu > a$ | all 5 $> 0$ | **5** (full state $U_\Sigma$) | 0 |
| subsonic inflow $0 < u_\nu < a$ | $\lambda_1 < 0$, rest $>0$ | **4** | 1 (upstream-running acoustic) |
| sonic / stagnant / backflow | degenerate or reversed | excluded by (P2)/(P3) | — |

Under (P3-S), the datum is the full state trace of D2.1 and nothing must be
modeled: the boundary operator is trivially maximally dissipative.
`TEST:` well-posedness rejector — perturb the full supersonic-inflow datum at
high wavenumber in a linearized solve; unbounded amplification (violating the
Kreiss bound $\|u\| \lesssim \|$data$\|$) rejects either the counting or the
signature declaration.

**C4.2 (Admissible prescribed sets in the subsonic case)** [SKETCH]. Under
(P3-s), exactly 4 scalar combinations are prescribed; the choice must satisfy
the uniform Kreiss–Lopatinskii condition (equivalently: the prescribed
4-dimensional subspace of datum perturbations must be transverse to the
outgoing eigendirection, uniformly on $\mathcal{K}$). Classical valid sets for
Euler inflow: $(s, h_0, u_{t_1}, u_{t_2})$ (entropy, total enthalpy, two flow
angles/tangential velocities), or the equivalent $(p_t, T_t, \text{2 angles})$
— for the thermally perfect gas, $h_0$ and $s$ are the natural invariants
along $\lambda_{2,3,4}$-characteristics and the set inherits KL-uniformity from
the polytropic computation under (H-th). Invalid sets exist (e.g., prescribing
$(\rho, u)$ entirely constrains the outgoing invariant and fails KL at finite
frequencies). Gap: the KL verification for strongly variable $c_p$ is by
continuity from the polytropic case within $\mathcal{K}$ — checkable, not
written here.
`TEST:` per candidate set, a frozen-coefficient normal-mode computation at
sampled $\mathcal{K}$-states: any root of the Lopatinskii determinant in the
closed unstable half-plane rejects that prescription set.

**C4.3 (Closure options in the subsonic case, with prices)** [MODEL]. The
returned characteristic carries downstream information into the combustor; the
5th scalar at $\Sigma$ is *not data*. Options:

1. **(C1) Re-placement** to a (P3-S) surface. Price: the design domain shrinks
   or no admissible band exists (Remark 1.3).
2. **(C2) Impedance closure**: prescribe a combustor reflection model
   $\widehat{\delta w^-} = Z(\omega)\, \widehat{\delta w^+}$ linking outgoing and
   incoming acoustic invariants at $\Sigma$. Price: a new *empirical* datum
   $Z$ with its own provenance, uncertainty and audits; the cut is no longer
   state-data-only.
   `TEST:` measured combustor reflection coefficient vs. $Z$; mismatch beyond
   its error bar rejects the closure.
3. **(C3) Anechoic closure** ($Z \equiv 0$, non-reflecting). Price: asserts the
   combustor absorbs all upstream-running waves at the relevant frequencies —
   generically false near resonances.
   `TEST:` same as (C2) with $Z = 0$; measured reflection magnitude above
   tolerance rejects.
4. **(C4) Abandon the cut** (couple the combustor into the design loop for
   this regime). Price: cost; the datum concept survives only as an initial
   iterate.

In the family/phase pictures of §3, the closure choice must be **the same for
every phase and every design candidate**, else the family members solve
different problems and their average is meaningless.
`TEST:` pipeline audit — grep of the solver configuration per phase/design;
any heterogeneity rejects the campaign.

---

## §5 CAUSALITY: when is the cut legitimate

**C5.1 (Supersonic cut $\Rightarrow$ exact causal independence)** [SKETCH for
entropy solutions; PROOF-grade for smooth solutions]. Hypotheses: (P2),
(P3-S) hold for the *coupled* solution on $\Sigma$ for all $t$ in the window;
finite speed of propagation holds for the solution class (true for classical
solutions by characteristic-cone energy estimates; for entropy solutions,
propagation speed bounded by $\max(|u| + a)$ on $\mathcal{K}$ [SKETCH — standard
in 1D/BV theory, asserted in multi-D $L^\infty$ via the same cone argument on
the entropy inequality]). *Claim.* The trace $U_\Sigma$ is invariant under any
modification of geometry, boundary conditions, or state in
$\{z > z_I\}$: every backward characteristic cone from a point of
$\overline{\{z \le z_I\}}$ remains in $\{z \le z_I\}$, because all
characteristic normal speeds at $\Sigma$ are $\ge \delta_1 > 0$ into $D$. Hence
the datum is a genuine *given* and the cut is legitimate.
Conversely, under (P3-s), legitimacy **fails structurally**: exactly one
characteristic family carries design information upstream; the datum is
design-independent only modulo the closure model of C4.3, and "independence"
is then a property of the closure, not of the physics.
`TEST:` (i) numerical rejector — two downstream designs differing only in
$\{z > z_I\}$, coupled to the same combustor model; any statistically
significant difference in the measured $U_\Sigma$ beyond discretization noise
rejects the claimed (P3-S) causality; (ii) analytic rejector — exhibit a point
of $\Sigma \times$ cycle with $u_\nu < a$ in the coupled solution: one point
suffices to void the theorem's hypothesis.

**C5.2 (Breakage mechanisms)** [MODEL]. Physical channels that break
independence, in decreasing order of violence: (i) **unstart / upstream shock
propagation** — a nozzle-borne shock crosses $\Sigma$ (destroys (P2)/(P3)
dynamically); (ii) **subsonic pockets** in phase or in space (near-wall
strips, wake of the wave) — continuous acoustic feedback; (iii)
**thermoacoustic coupling**: upstream-running waves (through a subsonic
pocket or through the closure) modulate the detonation, shifting
$(\hat U, \Omega, m)$ themselves — the datum drifts with the design; (iv)
**viscous channels** outside the model (boundary-layer upstream influence,
separation): invisible to the inviscid characteristic count — must be excluded
by (P5), not by C5.1.

**D5.1 (Monitors — the causality audit instruments).**
1. **Margin monitor**: $\mathcal{M}_1 := \operatorname*{ess\,inf}_{\Sigma \times
   \text{cycle}} (u_\nu - a)$; alarm at $\mathcal{M}_1 < \delta_1$; rejection at
   $\mathcal{M}_1 \le 0$ on any set of positive measure (report the measure of
   the sonic-violating set, not only the inf).
2. **Upstream-flux monitor**: the outgoing-invariant energy flux through
   $\Sigma$ computed from the *downstream* solution's trace; nonzero beyond
   tolerance under a (P3-S) declaration is a contradiction — reject.
3. **Datum-drift monitor**: re-estimate $(\hat U, \Omega, m)$ against design
   iterations; correlation of datum drift with design parameters beyond noise
   rejects independence (mechanism (iii)).
4. **Unstart detector**: pressure-ratio/shock-position sentinel in
   $z \in (z_I, z_I + h)$; a captured shock with upstream-directed motion
   rejects the window.

---

## §6 ADMISSIBILITY AUDITS — full list, each with a rejecting test

A delivered datum $\mathcal{D} = (\hat U, \Omega, m)$ is accepted only if ALL
pass. (Tolerances $\varepsilon_\bullet$ are part of the datum's contract, §7.)

- **A1 (Range/positivity).** $\hat U(x) \in \mathcal{K}$ a.e.
  `TEST:` pointwise scan; any excursion (vacuum, negative $T$, out-of-table
  $T$) rejects.
- **A2 (Frozen chemistry).** As (P1), evaluated on the datum itself.
  `TEST:` kinetic-mechanism evaluation at datum states; composition drift over
  $\tau_{res}$ beyond $\varepsilon_{chem}$ rejects.
- **A3 (Rotating-wave purity).** Two-sided $(k,\omega)$ spectrum of probe
  signals must concentrate on the dispersion lines $\omega = k\Omega$
  ($k \in m\mathbb{Z}$ under $\mathbb{Z}_m$).
  `TEST:` off-line energy fraction $> \varepsilon_{pure}$ rejects (H-RW) — the
  datum is then (T)-class only, and every §3 reduction is void; additionally
  the direct residual $\rho_{RW}$ of D2.2.
- **A4 (Global conservation compatibility).** Cycle-averaged mass and energy
  fluxes through $\Sigma$ must match the combustor's supply:
  $\langle \int_\Sigma \rho u_\nu \rangle = \dot m_{prop}$,
  $\langle \int_\Sigma \rho u_\nu H \rangle = \dot m_{prop} h_{0,in} + \dot Q$
  within provenance error bars.
  `TEST:` mismatch beyond bars rejects (the datum and the machine disagree).
- **A5 (Characteristic-signature audit).** Verify the declared (P3) class on
  the datum: sign pattern of (0.1) constant over $\Sigma \times$ cycle with
  margins $\delta_0, \delta_1$.
  `TEST:` any sign change or margin violation rejects the placement class (and
  reroutes to C4.3).
- **A6 (Jump admissibility / moving Rankine–Hugoniot).** Every jump curve of
  $\hat U$ (in $\alpha$) sweeping the annulus at speed $\Omega r$ must satisfy
  the RH conditions of the *upstream* system with Lax-admissible entropy
  production (no expansion shocks).
  `TEST:` extract jump strengths and normal speeds from the datum; RH residual
  or entropy-production sign violation beyond tolerance rejects (the datum is
  not the trace of any admissible flow — fabricated or corrupted data).
- **A7 (Trace attainability / refinement stability).** As D2.1's test:
  integrated fluxes and $\mathrm{TV}$ stable under record/mesh refinement.
  `TEST:` non-Cauchy behavior rejects the claimed BV class.
- **A8 (Periodicity and mode-lock).** $T_{per}$-return residual
  $\|U_\Sigma(\cdot, t + T_{per}) - U_\Sigma(\cdot, t)\|_{L^1(A)}$ small over the
  record; $\Omega$ drift $\le \varepsilon_\Omega$.
  `TEST:` violation rejects (P6)/the averaging window.
- **A9 ($\mathbb{Z}_m$ symmetry, if claimed).** D2.2 test.
  `TEST:` residual beyond tolerance demotes the datum to $m' = 1$ (period
  $2\pi/|\Omega|$) — all downstream uses must then use the long period; silent
  use of the short period rejects the pipeline.
- **A10 (Wall compatibility).** At the bounding circles $r = r_i, r_o$:
  tangency $u_r = 0$ in the trace sense if walls continue through $\Sigma$; the
  datum's corner traces must be compatible with the downstream wall condition
  to the order demanded by the solution class (for BV: no condition beyond
  bounded traces; for piecewise-$C^1$ design solves: first-order corner
  compatibility).
  `TEST:` corner-trace evaluation; incompatibility beyond the declared
  solution-class order rejects (spurious corner singularities would be
  design-domain artifacts, not physics).
- **A11 (Entropy-flux budget).** The datum's cycle-averaged entropy flux
  $\langle \int_\Sigma \rho s\, u_\nu \rangle$ must be $\ge$ the supply's entropy
  flux plus a nonnegative production consistent with the upstream entropy
  inequality [MODEL — multi-D boundary entropy inequalities for systems are
  not a complete theory; this audit is a necessary-condition check, not a
  characterization].
  `TEST:` negative implied upstream entropy production rejects.
- **A12 (Declared-reduction consistency).** The delivery must state which of
  (T)/(L)/(M) it provides and which reduction (R1)/(R2)/(R3) downstream
  consumption will apply; the §3 admissibility numbers ($\delta_{qs}$, the
  branch selection of C3.4, the $\mathcal{R}$-closure declaration of C3.5) must
  be computed and in range.
  `TEST:` missing declaration, or $\delta_{qs} \ge 1$ under an (R3) claim, or
  branch mismatch, rejects the *use*, independently of the datum's quality.
- **A13 (Provenance measurability).** Every field of $\hat U$ must be traceable
  to measured/simulated quantities with a declared estimator (e.g., $T$ from
  which diagnostic; $u_\theta$ from what). Derived-only fields (filled by
  assumption, e.g., "swirl set to zero") must be flagged as *modeled
  components* and enter §7's uncertainty with prior-width, not error-bar,
  status.
  `TEST:` an unflagged assumed component discovered by provenance review
  rejects the delivery as mislabeled.

---

## §7 UNCERTAINTY: empirical provenance in the formal structure

**D7.1 (The datum as a calibrated set, not a point).** The deliverable is
$$ \mathfrak{D} = \big( \mathcal{D}_0;\ d(\cdot,\cdot);\ \varepsilon;\ W \big) $$
where $\mathcal{D}_0 = (\hat U_0, \Omega_0, m)$ is the nominal triple; $d$ is a
declared metric on datum space; $\varepsilon$ the certified radius (from
measurement/simulation error analysis, per component:
$\varepsilon_{\hat U}$ in $d$, $\varepsilon_\Omega$ relative, $m$ exact-or-reject);
and $W$ the **validity window** — the set of operating conditions (mass flow,
equivalence ratio, backpressure range) over which the provenance holds.
Extrapolation outside $W$ is not "larger error bars": it is *no datum*.
`TEST:` any design-campaign evaluation at conditions outside $W$ rejects the
campaign (audit, not error bar).

**C7.1 (Metric choice)** [MODEL with a PROOF-grade constraint]. Requirements
on $d$: (a) the audits of §6 must be $d$-continuous (else acceptance is
unstable to noise); (b) the QoI map (datum $\mapsto$ cycle-averaged thrust
through the downstream solve) must be $d$-continuous on the admissible set.
Constraint (a) rules out $\mathrm{TV}$-metrics (jump positions are never
measured to $\mathrm{TV}$-accuracy); (b) rules out metrics weaker than
$L^1$-type (fluxes are $L^1$-continuous on $L^\infty \cap$-bounded sets [PROOF
— dominated convergence on $\mathcal{K}$]). Declared choice:
$d = \|\cdot\|_{L^1(A)}$ on $\hat U$ within the $L^\infty(\mathcal{K})$-bounded,
$\mathrm{TV}$-bounded class (bounds part of the contract, not of the metric).
Honest status of (b): $L^1$-stability of the *downstream solution* w.r.t.
boundary data is a theorem only in 1D small-BV (Lipschitz semigroup); in the
present multi-D setting it is a **modeling assertion to be verified by
sampling**, not assumed.
`TEST:` finite-difference sampling of the QoI over an $\varepsilon$-net of the
ball: QoI oscillation not $\to 0$ with $\varepsilon$ (at fixed numerics) rejects
$d$-continuity of the pipeline — and with it any pointwise-nominal design
claim.

**C7.2 (Robustness requirement on the consumer)** [MODEL]. The design program
must report, for every candidate design and every claimed optimum, not
$J(\mathcal{D}_0)$ alone but a certified interval:
either $[\min, \max]$ of $J$ over the $\varepsilon$-ball (sampled or
optimization-based), or the first-order bound
$|J(\mathcal{D}) - J(\mathcal{D}_0)| \le \|\Lambda\|_{L^\infty(A)} \,
\varepsilon_{\hat U} + |\partial_\Omega J| \, \varepsilon_\Omega$, with $\Lambda$ the
adjoint-state trace on $\Sigma$ (the exact first-order kernel of
datum-sensitivity — note this is again a *trace object*, of the adjoint
system, and its existence imposes the dual regularity of D2.1 on the adjoint).
Comparisons between designs are meaningful only when the intervals separate.
`TEST:` two designs declared distinct with overlapping certified intervals
reject the comparison claim; an adjoint bound violated by a direct
finite-difference probe (outside its own error bar) rejects the adjoint
implementation.

**C7.3 (Modeled components carry priors, not bars)** [MODEL]. Components
flagged under A13 (assumed, not measured) enter the interval of C7.2 through
declared prior ranges (e.g., swirl $u_\theta \in [0, u_\theta^{max}]$), i.e., a
worst-case over the prior, never a Gaussian bar.
`TEST:` sensitivity of $J$ to a flagged component exceeding the campaign's
distinguishability threshold, while that component remains unmeasured, rejects
"optimum" claims (verdict: measure it first).

---

## §8 Claim register (rigor summary)

| # | Claim | Class |
|---|---|---|
| 0.1 | Eigenstructure of $A_\nu$ under (H-th) | PROOF |
| C1.1 | Placement conditions = noncharacteristic-boundary hypotheses | PROOF |
| C1.2 | Invalidation catalogue | MODEL |
| D2.1 | Existence of flux trace ($\mathcal{DM}^\infty$) / state trace (BV) | SKETCH / PROOF |
| D2.2 | Rotating-wave datum triple $(\hat U, \Omega, m)$ | MODEL (physics) |
| C2.1 | (T)≡(L) under (H-RW); (M) sufficient for one-point averages only; identity (2.1) | PROOF |
| C2.2 | Helical + $\mathbb{Z}_m$ inherited; axisymmetry/reflection/time-reversal not | PROOF (group part) |
| C3.1 | (R1) exact wave-frame steady reduction | SKETCH, conditional (H4–H5 open) |
| C3.2 | Azimuthal timelike/hyperbolic structure in wave frame | PROOF |
| C3.3 | (R2) exact averaged-flux identity; wave-stress defect named | PROOF |
| C3.4 | Two-branch flux inversion (thermally perfect) | SKETCH |
| C3.5 | (R2) preserves $\Sigma$-fluxes exactly; downstream loss $O(\epsilon^2)$ | PROOF / MODEL |
| C3.6 | (R3) defect identity + bound (3.3); large coefficient; $\delta_{qs}$ criterion | PROOF (bound) / MODEL (use) |
| C4.1 | Characteristic counting: 5 vs 4 prescribed | PROOF |
| C4.2 | KL-admissible subsonic prescription sets | SKETCH |
| C4.3 | Closure options and prices | MODEL |
| C5.1 | Supersonic cut ⇒ causal independence; subsonic ⇒ closure-dependent | SKETCH (PROOF-grade smooth case) |
| C5.2 | Breakage mechanisms | MODEL |
| A1–A13 | Audit battery | each tagged in-line |
| C7.1–C7.3 | Metric, robustness, priors | MODEL with PROOF-grade constraints |

**Structural verdict of this derivation.** The entire cut strategy stands or
falls on three measurable numbers: the characteristic margin $\mathcal{M}_1$
(§5), the purity residual of A3, and the quasi-steady number $\delta_{qs}$
(C3.6). Everything exact in the construction — the trace existence, identity
(2.1), the averaged-flux law (3.2), the counting C4.1 — survives any regime;
everything regime-dependent is carried by those three numbers and by the
conditional hypotheses (H4)–(H5) of the wave-frame reduction, all of which
have named rejecting tests above.
