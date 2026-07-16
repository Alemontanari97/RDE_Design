# Problem book: the cycle-averaged variational nozzle problem for RDEs (D1)

Status: PROBLEM BOOK (formalization deliverable D1 of the 2026-07-16 session).
Frozen definitions, objective functional with its operating measure, the
design-interface ("RDE throat") formalization, and the hypothesis ledger.
Companion deliverables: `docs/rde_nozzle_theorem_ledger.md` (D3: formal
statements with verified proofs / counterexamples / open status),
`docs/rde_nozzle_literature_map.md` (D2), `docs/rde_nozzle_claims_verdict.md`
(D4). This document SUPERSEDES the informal definitions of
`docs/cycle_averaged_variational_nozzle.md` §1 and
`docs/mathematical_foundations_rde_nozzle.md` §1-2 where they differ; the
differences are listed in D4.

Discipline: every assertion carries its hypotheses; TEOREMA / CONGETTURA /
EURISTICA are separated; anything executable is flagged with its oracle.

------------------------------------------------------------------------------
## 1. Notation (frozen)

| Symbol | Meaning | Units |
|---|---|---|
| x, r, θ | axial, radial, azimuthal cylindrical coordinates | m, m, rad |
| e_x | engine axis unit vector | — |
| Σ | nozzle contour (design variable); A = admissible class | — |
| Ω(Σ) ⊂ ℝ³ | fluid domain bounded by chamber, walls Γ_w(Σ), interface(s) | — |
| Γ_d | design interface (Def. 4.2) | — |
| U = (ρ, ρu, ρE, ρY_k) | conservative state | SI |
| p, T, M, s | pressure, temperature, Mach, specific entropy | SI |
| Pa | ambient pressure (constant in time unless stated) | Pa |
| Ω_w | wave angular speed (unknown of the solution) | rad/s |
| t_c = 2π/(n Ω_w) | cycle period, n = wave count | s |
| ξ ∈ Ξ = [0,1) | cycle phase | — |
| μ | operating measure on Ξ (Def. 3.4) | — |
| s(ξ) | inflow-data family on Γ_d (Def. 4.3) | — |
| F[Σ; s] | per-state (steady) axial thrust functional | N |
| J[Σ] | cycle objective (Def. 3.1 exact; Def. 3.5 averaged) | N |
| ṁ | mass flow rate | kg/s |
| c* | characteristic velocity Pc·A_t/ṁ | m/s |
| St | Strouhal / two-scale parameter (Def. 8.1) | — |
| δ | 0 planar / 1 axisymmetric (GENO convention) | — |

Wave-frame variables carry a tilde: q̃(x, r, θ′) with θ′ = θ − Ω_w t.
Relative velocity w = u − Ω_w e_x × x (so w_θ = u_θ − Ω_w r, w_x = u_x).

Naming note. Ω_w (wave speed) vs Ω(Σ) (domain): context disambiguates; where
both occur we write Ω_w explicitly.

------------------------------------------------------------------------------
## 2. The exact problem (rung 3): what is honestly being optimized

The physical constraint is reactive compressible flow (Euler backbone;
viscous closure as a declared modeling layer) in Ω(Σ):

    ∂U/∂t + div F(U) = S(U)  in Ω(Σ),                       (PDE)

with injection-face boundary data on Γ_in (injector/feed model), slip on
Γ_w(Σ), supersonic outflow a.e. on Γ_out. For fixed Σ, after transients the
flow settles onto an attractor with (assumed) physical invariant measure
ν_Σ; the honest objective is the ergodic average

    J_exact[Σ] = lim_{T→∞} (1/T) ∫_0^T F_S(t) dt,           (Def. 3.1)
    F_S(t)     = ∫_S [ρ u_x (u·n) + (p − Pa) n_x] dA,

S any fixed control surface enclosing the engine (S-independence by steady
momentum balance in the mean). Well-definedness of J_exact presupposes a
solution concept and an ergodicity assumption; both are catalogued in §6
(this is not a footnote: multi-D entropy solutions are non-unique, §6/S2).

The nominal operating regime is a SINGLE steadily rotating wave (or an
n-fold symmetric set): the attractor is a relative equilibrium of the SO(2)
symmetry, the flow is exactly a rotating pattern, and Theorem T0 (D3 §2)
applies: F_S(t) is then CONSTANT in time and equals the steady wave-frame
thrust. Everything below is organized so that each idealization away from
Def. 3.1 is a ledger row (§9) with a named violation channel.

------------------------------------------------------------------------------
## 3. The objective functional and its measure

### 3.1 Two candidate objectives

Def. 3.1 (mean thrust): J_exact above; nominal-case form J[Σ] = F̃[Σ]
(steady wave-frame thrust).

Def. 3.2 (cycle specific impulse): for periodic operation with period t_c,

    Isp_cycle[Σ] = ∫_0^{t_c} F(t) dt / ( g0 ∫_0^{t_c} ṁ(t) dt ).

### 3.2 When the two coincide (and when not)

PROPOSITION O1 (equivalence at frozen, choked feed — proof in D3 §1).
Assume (i) the cycle family of chamber states and the period are UNCHANGED
by the divergent-section shape Σ (frozen-family assumption, = weak-coupling
rung of §7 of the roadmap); (ii) the feed is choked at a fixed minimal
section A_t all cycle, ṁ(t) = Pc(t) A_t / c*(t) independent of Σ. Then
∫ṁ dt is Σ-independent and argmax_Σ Isp_cycle = argmax_Σ J. Moreover with
CF := F/(Pc A_t) and ṁc* = Pc A_t, the Isp numerator is ∫F dt identically:
no mass-weighting ambiguity survives at the shape level.

Failure channels (ledger rows): (a) chamber–nozzle coupling — if Σ moves
the fill height, PR, Ω_w or the mode count, both objectives change and they
are NO LONGER equivalent (the bilevel problem PB-4, §10); (b) unchoked
tails — the 20-atm hydrocarbon cycles' documented choking margins 0.97/0.65;
(c) throat-area redesign — if A_t is itself a DOF, Isp and F diverge and the
mission decides the objective. Within this problem book the objective is
J = ∫F dμ; Isp statements are corollaries via O1.

### 3.3 The operating measure

Def. 3.4 (operating measure). μ = pushforward of normalized time
Lebesgue measure on one cycle under t ↦ ξ = t/t_c, and, derived from it,
the pushforward μ_P on the chamber-state space under ξ ↦ s(ξ).

LEMMA O2 (log-uniform pressure measure — proof one line, D3 §1). For the
exponential blowdown Pc(ξ) = P_CJ · PR^{−ξ}, the pushforward of dξ onto
pressure is dμ_P(Pc) = dPc / (Pc ln PR) on [P_CJ/PR, P_CJ]: LOG-UNIFORM.
"Design an RDE nozzle" = "design one contour optimal in mean over a
log-uniform NPR ensemble". The engine fixes physically the measure that
multipoint aerodynamic design must posit; the whole theory below holds for
ANY probability measure μ on Ξ (measured cycles, URANS slices, robustified
Wasserstein balls around the nominal — PB-5).

### 3.5 The averaged objective (rung 2)

    J[Σ] = ∫_Ξ F[Σ; s(ξ)] dμ(ξ),                            (AVG)

with F[Σ; s] the STEADY thrust of the per-state problem (Def. 4.4). The
legitimacy of (AVG) as an approximation of Def. 3.1 is NOT assumed: it is
the content of T0 (exact, wave-frame reading) and of the O(St) bridge
(P4), each with declared hypotheses.

Equivalent forms of F (used interchangeably under S1-regularity):
wall form F = F_throat + ∫_Σ (p − Pa) n_x dA; control-surface (Rao) form
F = ∫_CS [(p − Pa) + ρV² sin(φ−θ)cos(θ)/sin(φ)] (2πy)^δ dy on any
permeable surface φ(y). The two coincide by the steady momentum theorem;
the control-surface form is where per-streamline structure is explicit.

------------------------------------------------------------------------------
## 4. The design interface: what "the RDE throat" is

### 4.1 The four difficulties, stated

(a) NO GEOMETRIC THROAT in general: many RDEs exhaust the annulus directly
    into the divergent (or into ambient); there is no minimal section to
    anchor classical nozzle theory.
(b) THE SONIC SET IS UNSTEADY AND STRUCTURED: in the lab frame the M = 1
    locus moves with the wave; behind the wave the flow leaves the chamber
    subsonic, elsewhere supersonic — the sonic surface is azimuthally
    non-planar (in the wave frame: steady but θ′-structured, possibly
    non-existent as a graph over the annulus in some sectors).
(c) 0-D CLOSURES PRESCRIBE CHOKING, NOT GEOMETRY: Stechmann-Heister-Harroun
    assume thermal choking at the chamber exit plane, ṁ = Pc A / c* — an
    aggregate statement, not a pointwise sonic condition.
(d) THE TRUE INTERFACE STATE IS A DISTRIBUTION: (M, θ_flow, p0, T0, s)(y,
    θ′, t) with an oblique shock sector, a deflagrative contact region,
    and swirl — not a clean sonic line at time-varying stagnation state.

### 4.2 Definition (design interface)

Γ_d := a FIXED, axisymmetric surface (nominally the annulus exit plane
x = x_d, or any surface downstream of all heat release), on which inflow
data for the nozzle problem are prescribed, and downstream of which the
design region Ω_d(Σ) extends. The pair (Γ_d, data class) — not any sonic
condition — is the design interface. Requirements:

  R1 (causal separation): all combustion is upstream of Γ_d; the design
     region is chemically frozen or in declared local equilibrium (the
     thermo backend's γ-law is part of the data).
  R2 (well-posed data): the prescribed data must make the downstream
     problem well-posed in the declared solution class (§6). On supersonic
     patches: full state. On subsonic patches: incomplete data + the
     admissibility that the downstream solution not send information
     upstream of Γ_d in the mean — this is an ASSUMPTION (ledger row H-I2),
     violated by strong nozzle-generated compressions reaching Γ_d.
  R3 (measurability): ξ ↦ s(ξ) is μ-measurable with values in the data
     class; all per-phase constructions below use measurable selections.

The "RDE throat" is therefore NOT a location: it is the interface
CONTRACT (Γ_d, data class, validity conditions). What plays the throat's
classical role — fixing ṁ independently of the divergent — is hypothesis
H2 (choked feed), an upstream statement.

### 4.3 The idealization ladder of the interface data (taxonomy)

Each level names: data given on Γ_d / validity conditions / violation
channel it opens.

I0 (bilevel, no interface): no data given; chamber and nozzle solved as
   one coupled limit cycle; Σ feeds back on s and μ. The general problem
   (PB-4). Validity: always. Cost: differentiable-detonation frontier.
I1 (wave-frame exact data): steady 3-D data q̃(y, θ′) on Γ_d in the
   co-rotating frame, taken from a chamber solution at frozen Σ (or from
   URANS/experiment). Validity: single steadily rotating mode (else no
   wave frame); weak coupling. Opens: N6 only.
I2 (quasi-steady phase family): a μ-family s(ξ) of MERIDIONAL data,
   s(ξ) = {P0(ξ), T0(ξ), thermo handle γ(·;ξ), M_in(y;ξ), θ_in(y;ξ),
   [entropy/vorticity profiles]}, each feeding a steady 2-D (planar or
   axisymmetric) per-phase problem. Validity: St ≪ 1 (D1) and azimuthal
   decoupling (D2) — see §8 for the sharpened relation D1 ⊃ D2. Opens:
   N5 (finite St), N6 (3-D). This is rung 2's native interface, and GENO's:
   `read_ivl_from_file` (IO_m.f90:620) + annular inlet (InitialValues_m.f90:146).
I3 (S-H sonic family): s(ξ) = sonic line at stagnation (P0(ξ), T0(ξ)),
   frozen γ, uniform profiles. Validity: I2 conditions + clean-blowdown
   chamber abstraction + H-T3.3 (phase-independent nondimensional inflow
   shape). Opens: N3 (inlet nonuniformity), N4 (thermochemistry) on top of
   I2's. This is the interface of `src/thrust/st_core.py` and of Theorems
   T3/T4.
I4 (single mean state): one state (⟨Pc⟩, T0, γ); classical Rao/GENO design.
   Validity: exactly the T3 collapse class — and T3 (D3 §5) says that
   WITHIN I3's other hypotheses, I4 is not an approximation but EXACT.
   Opens: everything N1-N6 when its hypotheses fail.

### 4.3bis The sonic start (MOC initial data) in full generality

Classical fact: MOC needs a SPACELIKE (non-characteristic) supersonic
initial curve with characteristically complete data; the sonic line is
the parabolic-degeneracy locus and cannot itself carry the start. The
classical treatment solves the transonic throat separately (Sauer-type
local expansions; or a computed transonic solution) and hands MOC a
slightly supersonic IVL; Kraiko-P'yankov-Tillyaeva (2002) prove that
the NONUNIFORMITY of that transonic datum enters the optimum at first
order — IVL quality is an optimality ingredient, not a startup detail.

The choking firewall: under H2 the mass flow is independent of the
divergent section — information does not climb past the sonic set.
This DECOUPLES the design mathematically: the subsonic/transonic part
fixes (ṁ, IVL shape); the divergent fixes thrust at given data. This is
why divergent-only design with prescribed data is well-posed, and why
R2 confines the transonic degeneracy inside the data generator (shape
sensitivity THROUGH a sonic surface is open — gap b3-C3; the published
warning is Giles-Pierce's logarithmic adjoint singularity at the
throat).

RDE without a geometric throat — CORRECTED formulation (the swirl
audit). In the wave frame the relative velocity carries the sweep,
w_θ ≈ u_θ − Ω_w r ≈ −D_CJ at the annulus: wave-frame streamlines are
STRONGLY HELICAL. Two distinct sonic notions must not be conflated:
 (i)  PDE TYPE: the steady wave-frame operator is hyperbolic where
      |w| > c (real Mach cones) — the sweep HELPS here, making the
      problem hyperbolic almost everywhere. Physically, the relative
      sonic locus |w| = c attached to the wave IS the CHAPMAN-JOUGUET
      surface: in the wave frame it is the causal firewall (downstream
      information cannot climb into the reaction zone through it in CJ
      operation) — the physical grounding of H-F1, and the statement of
      WHERE chamber-nozzle coupling does pass: through the UNSHIELDED
      sectors (fresh fill, deflagrative region, oblique-shock sector).
 (ii) DATA SURFACES (spacelikeness lemma, frame-invariant): a plane
      x = const can carry full data iff the Mach cone lies on one side:
      angle(w, e_x) + α < π/2 ⟺ w_x/|w| > c/|w| ⟺ w_x > c. Since
      w_x = u_x and c is frame-invariant, an axial interface is
      spacelike IFF u_x > c — THE SAME condition as in the lab frame;
      the sweep does NOT help data prescription on axial planes (it
      tilts the cone azimuthally, leaving the axial projection intact).
Definitions of record: the AXIAL sonic surface u_x = c (steady in the
wave frame by T0) governs full-state prescription on axial interfaces;
the RELATIVE sonic surface |w| = c (= CJ locus at the wave) governs the
operator type. EXPLICITLY, to preclude any conflation: CJ-sonicity
licenses NO axial MOC — axial marching requires u_x > c pointwise on
the marching foliation, full stop; |w| > c only guarantees real Mach
cones, whose time-like directions in the wave frame are near-azimuthal
(helical), so no axial plane near the chamber is spacelike even where
the relative flow is supersonic. The condition hierarchy is:
C1 hyperbolicity (M > 1, frame-appropriate) ⊅ C2 axial marching
(u_x > c) ⊅ nothing; C3 non-axial marching (any time-like foliation,
e.g. streamline-aligned with flow-normal data — helical in the wave
frame, never constructed = N6); C4 CJ-sonic = type boundary + causal
firewall ONLY. In classical nozzle MOC C1 and C2 nearly coincide
(near-axial flow past the throat), which is why the distinction is
invisible there and maximal in the RDE. Γ_d with full-state I1/I2 data must lie downstream of
the axial sonic surface a.e.; on axially subsonic patches the data are
incomplete + H-I2-audited (R2), or carried by the thermal-choking
closure (ṁ = Pc A/c* — S-H assumption 3), with the H2 margin monitored.
Methodological consequences: the rung-3a wave-frame problem must be
solved as an IMPLICIT steady BVP (freezing + Newton-Krylov, as WP5
prescribes) — no marching, hence no spacelike-surface requirement; a
3-D "design MOC" would need helical time-like marching surfaces near
the chamber (never constructed — the precise content of N6). In the
quasi-steady per-phase reading the huge relative swirl never appears:
it IS the sweep term, i.e. the O(St) unsteadiness priced by P4.

Operational IVL sources (all inside the CycleFamily contract, all
subject to the stage-A audits, now including SPACELIKENESS per phase —
an IVL valid for the peak phase can be near-characteristic for the
tail phase): (i) Sauer-type per-phase throat expansion (γ = const
structural limit, GENO `InitialValues_m`); (ii) computed IVL import
(`read_ivl_from_file` semantics generalized to phase families);
(iii) prescribed annular supersonic inlet (M_i, θ_i);
(iv) choking closure for subsonic phases (modeling row H2, declared).
The IVL's provenance and accuracy order are part of the Verdict.

MIXED-INTERFACE DECISION TREE (data with axially subsonic patches —
the GENERIC case for raw chamber-exit data; the patches are exactly
the CJ-unshielded sectors: fresh fill, deflagrative zone, oblique-shock
tail). Stage A classifies each patch: (a) HYPERBOLIC-TIMELIKE (total
per-phase M > 1, M_x < 1): full-state prescription is OVERDETERMINED
and Σ₀-contaminated — inconsistent for Σ ≠ Σ₀; (b) ELLIPTIC (total
M < 1): mixed-type per-phase region, MOC dead by type. Options, all
declared in the Verdict, never silent:
 O1 MOVE Γ_d downstream of the axial-sonic crossing; the wall between
    the old and new interface is FROZEN (it generated the data):
    full rigor on a reduced design class. Mandatory for (b) patches
    (unless a transonic per-phase solver is accepted — PRACTICE,
    outside S1, not a default).
 O2 PARTIAL DATA + IMPEDANCE: prescribe only incoming invariants on
    timelike patches; close the returning family with an admittance/
    impedance BC (Marble-Candel class) or the reduced chamber response
    map; per-phase problem becomes a mixed characteristic BVP; the
    stage-G coupling loop becomes MANDATORY with measured q.
 O3 HYBRID CHOKING SURROGATE: replace subsonic patches by the thermal-
    choking closure (row H2 revived, margins monitored); default when
    σ_sub (μ⊗area fraction) is small and thrust-lean.
 O4 ANCHOR UNAFFECTED: the rung-3a implicit wave-frame BVP ingests the
    full field including subsonic patches (no marching, no spacelike
    requirement) — always available as the verification anchor.
DOWNGRADES that mixed data force (written into the Verdict): H-I2
violated on the patches (real upstream information flux); H-F1 from
THEOREM (q ≡ 0, fully supersonic interface) to hypothesis with MEASURED
q; Prop. O1 at risk (ṁ through subsonic sectors may depend on Σ →
thrust-max vs Isp-max may split, N-O1± activated: the objective must be
chosen); the J_ideal bound becomes CONDITIONAL on frozen inlet fluxes.
The mathematics loses its theorems exactly where the physics says the
chamber feels the nozzle — the formalization LOCALIZES the coupling
channel rather than hiding it.

### 4.4 Per-state problem (Def.)

Given Σ ∈ A and data s on Γ_d of class I2/I3: find the steady flow U_s in
Ω_d(Σ) (solution concept per §6) with inflow s, slip on Σ, supersonic
outflow; F[Σ; s] := its axial thrust (wall or control-surface form). In
the MOC-regular class this is a classical Goursat/characteristic problem
(GENO's world), well-posed in domains of determinacy.

------------------------------------------------------------------------------
## 5. Admissible shapes

GENERAL (configuration-free) formulation. The design variable is the
SOLID SET S inside an envelope E (cylinder of length L, radius R_max
downstream of the annulus), with attachment constraints at the chamber
lip(s) and a uniform cone/regularity condition; the fluid domain is
E∖S. Configurations are the TOPOLOGY CLASSES of S — outputs of the
optimization, not inputs:
  (i)   BELL: solid on the outer boundary only; Σ = graph y_w ∈ C^{1,1},
        y_w(0) = y_lip (dual-bell = same sector, kinked wall).
  (ii)  PLUG (aerospike): center body only — free-boundary configuration;
        truncation length L_p and base-pressure closure p_b declared (N2).
  (iii) SHROUDED PLUG (Veen class): both; causally separable
        F = F_shroud + F_plug + F_kernel (GENO Veen doctrine).
  (iv)  further sectors included in A_gen: expansion-deflection (center
        body downstream of the exit plane), multi-component/clustered,
        non-axisymmetric (priced by P5).
Sector decomposition (SCHEMA): the uniform cone condition forbids
degenerating components (no needles/laminae), so A_gen splits into
FINITELY many topology sectors; per-sector existence via Chenais
compactness + S1 continuity (P7); the TOTAL optimum over A_gen = winner
of a finite tournament of sector optima (upper semicontinuity across
sector degenerations suffices). Cross-sector comparison is licensed by
the shared constraints and the geometry-free bound (D3 §10quater).
CAUTION: topological-derivative exploration is unreliable here — an
infinitesimal body in a supersonic stream produces only wave drag; the
center body pays only at finite size. Compare whole sectors.

Working class A: finite-dimensional spline manifolds inside the uniform
C^{1,1}/cone classes per sector (existence trivial, P7 gives the
function-class version); axisymmetry is an ASSUMPTION here, licensed
perturbatively by P5 (symmetry trichotomy), not by habit.

------------------------------------------------------------------------------
## 6. Solution concepts and well-definedness of J

(S1) MOC-REGULAR piecewise-smooth: steady supersonic per-state flows,
     piecewise C¹, finitely many transversal shocks/contacts, no wall
     shock formation. Classical well-posedness (Li Ta-tsien semi-global
     theory as framework); F and its shape sensitivity classical between
     switch events. ALL closed-form results (T2-T4, Rao/Kraiko conditions)
     live here. Membership is CHECKABLE along any computed solution
     (transversality + regularity monitors; the Sternin/Rao-Beck boundary
     function is the in-code instance) — S1 is an a-posteriori
     certificate class, not a wish.
     CANONICITY (why S1 is not a convenience restriction): by WEAK-STRONG
     UNIQUENESS (Dafermos relative-entropy argument; measure-valued
     version Brenier-De Lellis-Székelyhidi, CMP 2011 — citation to be
     re-verified at print), wherever an S1 solution exists, EVERY
     admissible weak or measure-valued solution coincides with it. Inside
     S1 the solution-concept ambiguity of (S2) is closed: the MOC
     solution is THE solution of every concept. The S2 minefield lives
     strictly outside S1 — which is exactly what the regularity monitors
     detect.
(S2) ENTROPY WEAK (multi-D): non-uniqueness by convex integration
     (De Lellis-Székelyhidi; Chiodaroli-De Lellis-Kreml) makes
     "J[Σ] = thrust of THE solution" ILL-DEFINED without selection.
     Repairs, in order of preference: retreat to S1 when certified;
     statistical/measure-valued solutions (Fjordholm-Käppeli-Mishra-
     Tadmor) — J becomes a double average ∫∫ F dν_sol dμ, composing
     cleanly with μ; declared dissipative surrogate (RANS/LES) with
     model-error ledger row. Optimization constrained by statistical
     solutions: open frontier, NOT a dependency of the program (D2 §b3).
(S3) THE WAVE (chamber side): ZND-type reacting shock with sonic locus;
     existence/spectrum in the Erpenbeck / Lee-Stewart / Evans-function
     (Zumbrun) language. Enters the nozzle problem only through (i) the
     data family s(ξ), (ii) the bilevel coupling, (iii) P1's structural
     link between design sensitivity and the stability operator.

Transonic degeneracy: the sonic set is where the steady operator changes
type. Adopted position (declared): all shape calculus happens strictly
downstream of prescribed regular data on Γ_d (R2); sensitivity THROUGH
the degeneracy is confined inside the chamber response map (bilevel), and
is an open analytical problem (D2 §b3 gap C3), not silently assumed.

------------------------------------------------------------------------------
## 7. Periodicity, the wave frame, and modes

Single steadily rotating wave (nominal): rotating pattern q(x,r,θ,t) =
q̃(x,r,θ−Ω_w t). T0 (D3 §2, proof verified): for ANY fixed axisymmetric
control surface the instantaneous thrust is time-CONSTANT and equals the
steady wave-frame momentum-flux integral; Coriolis/centrifugal forces are
exactly axial-component-free; w_x = u_x and w·n = u·n on axisymmetric
surfaces make the lab and rotating expressions of the functional
identical. Consequently: J_exact = steady 3-D shape functional in the
wave frame, with Ω_w an EIGENVALUE-like unknown (freezing formulation
with phase condition), and dΩ_w/dΣ a well-defined sensitivity object (P1).
CAUTION (weakened from the internal notes): this steadifies the PROBLEM;
it does NOT hand over Rao's closed-form machinery, which is 2-D — the 3-D
swirling variational theory is open (N6).

Failure modes of the nominal case, with the correct machinery for each:
counter-rotating pairs / modulated waves → relative periodic orbits,
harmonic-balance representation (3b); mode-hopping/chaotic → shadowing/
linear response (3c); MULTISTABILITY of wave count n (documented in RDEs,
with hysteresis) → J is SET-VALUED in Σ; well-posed reformulations:
expectation over a mode measure π(Σ), worst case, or CVaR (PB-5). The map
Σ ↦ n is piecewise constant: J can be DISCONTINUOUS across mode
boundaries — no smooth formulation can hide this; the robust formulation
is the honest one.

Symmetry trichotomy (P5): axisymmetric wall ⇒ relative-equilibrium
structure survives (steady problem); non-axisymmetric wall breaks SO(2) ⇒
modulated/periodic response, Floquet/HB machinery, one rung costlier;
discrete C_m wall symmetry ⇒ m|n resonance selection rules. "Axisymmetric
design" is thus a theorem-shaped boundary of the cheap problem class, and
leaving it has a computable perturbative price tag (P5).

------------------------------------------------------------------------------
## 8. Quasi-steadiness: the two-scale structure, sharpened

Def. 8.1. St := τ_n / t_c with τ_n the nozzle CONVECTIVE residence time
(τ_n = ∫ dx/u along the mean streamline; the acoustic time L/c enters the
Marble-Candel compactness criterion separately and is shorter).

Sharpened structure (correction to the internal notes, which listed D1
and D2 as independent). In the wave frame the steady transport operator
splits as w_θ ∂_θ′ + (meridional part); w_θ = u_θ − Ω_w r. The SWEEP part
−Ω_w r ∂_θ′ is what the lab frame calls ∂_t: neglecting it during one
nozzle transit is EXACTLY the quasi-steady hypothesis, with parameter
Δθ_sweep/(2π/n) = n Ω_w τ_n/2π = St_n (per-wave Strouhal). The residual
azimuthal coupling is the LAB-frame azimuthal drift u_θ τ_n / r ÷ (2π/n),
generically SMALLER than St_n (|u_θ| ≪ Ω_w r for detonation products).
Hence:

    D1 (quasi-steady, St_n → 0)  ⟹  most of D2 (meridional decoupling);
    D2 additionally requires weak azimuthal pressure-gradient smoothing
    of the inflow family (an O(u_θ/Ω_w r) + profile-mixing statement).

Honest numbers (rocket RDEs): f = 3-30 kHz, t_c = 33-330 μs, τ_n = 20-150
μs ⇒ St = O(0.1-1): MARGINAL. Therefore the averaged theory (rung 2) is
NOT self-licensing: it needs the O(St) corrector (P4: two-scale expansion
J_exact = J_avg + St·J_1 + O(St²), with J_1 a cell problem = per-phase
linearized nozzle response, i.e. Marble-Candel-type transfer functions
driven by the blowdown's pressure/entropy content) — and T0 as the exact
nonperturbative backstop. Any hardware conclusion from rung 2 without an
St error bar is out of contract in this program.

------------------------------------------------------------------------------
## 9. Hypothesis ledger

Columns: ID / statement / where it is used / violation channel / oracle
or falsifier (executable where possible).

| ID | Hypothesis | Used in | Violated by → channel | Oracle/falsifier |
|---|---|---|---|---|
| H-A1 | single steadily rotating wave (n-fold symmetric), exact periodicity | T0, wave frame, P1 | mode-hop, counter-rotation, modulation → robust formulation (PB-5) | spectrum monitor (P1); operability maps |
| H-A2 | axisymmetric wall and control surfaces | T0, §7 | non-axisym. wall → Floquet/HB (P5) | P5 perturbative sign test |
| H-F1 | frozen family: s(·), μ, Ω_w independent of Σ | O1, all of rung 2 | back-pressure feedback → bilevel PB-4 | chamber response map ΔPR(Σ), Δfill(Σ) |
| H2 | choked feed all cycle, fixed A_t: ṁ = Pc A_t/c* | O1, T3 assembly | unchoked low-Pc tail (margins 0.97/0.65 documented) | choking-margin monitor per row |
| H-I2 | no mean upstream influence through Γ_d | Def. 4.2 R2 | nozzle compression reaching Γ_d | characteristic-direction audit at Γ_d |
| D1 | St_n → 0 (quasi-steady) | T1/(AVG), all per-phase machinery | St = O(0.1-1) real engines → N5 | P4 corrector J_1; oracle O5 (unsteady sim) |
| D2 | azimuthal decoupling (residual, §8) | T1 factorization | strong swirl/sector mixing → N6 | wave-frame anchor solve (WP5) |
| D3 | per-phase MOC-regularity (S1), uniqueness | T2-T4, Rao/Kraiko conditions | wall shock formation, secondary shocks → adjoint-Euler fallback | S1 monitors; P7 failure boundary |
| H-T3.1 | one frozen γ common to all phases | T3 Lemma B | γ(ξ), γ(T) → N4 (measured small; §D4) | two-γ counterexample (D3 §5.2, executable) |
| H-T3.2 | fixed wall, full-flowing, supersonic exit every phase | T3 Lemma A (ambient-blindness) | separation → N1 (first-order breaker) | Summerfield/Schmucker criterion hook |
| H-T3.3 | phase-independent nondimensional inflow shape | T3 Lemma A | per-phase (M,θ)(y;ξ) profiles → N3 (first-order breaker) | GENO IVL ensemble runs |
| H-T4 | ideal-adaptation closure of the free boundary | T4 | truncation, base pressure, real adaptation → N2 (THE open problem) | plug off-design march (WP1c-i) |
| H-P1 | spectral non-degeneracy at 0 (beyond group mode), transversal fronts (Majda) | P1 IFT | neutral modes at mode boundaries → set-valued J | Evans/Arnoldi monitor |
| H-μ | μ known (nominal blowdown log-uniform) | (AVG) | waveform misspecification → DRO ball (PB-5) | sensitivity-to-μ report |
| H-E4 | per-phase Rao/corner theory valid for γ(T) frozen (form γ-agnostic; justification derived only for γ = const; finite-rate PROVEN to break it — Hoffman 1967 Eq. 78) | rung-2 per-phase brick with γ(ξ) families | strong γ(T) variation, finite-rate chemistry → adjoint-level formulation | Scofield-Hoffman 1971 Table-2 frozen-thrust oracle (GENO gate G2); Hoffman E-residual along optimized contour |
| H-Pa | Pa constant over the cycle | T0, T3 affinity | altitude transients (slow: OK); plume feedback | — (declared) |

Every ledger row is also a NOVELTY CHANNEL (N1-N6 of the engineering
note): T3 is a conservation law for research effort — genuine gains over
"Rao at ⟨Pc⟩ / plug at peak" enter ONLY through a violated row.

------------------------------------------------------------------------------
## 10. The problem statements (precise)

PB-1 (averaged variational problem, rung 2 — the program's core).
Given interface class I2/I3 with family s(·) and measure μ, admissible
class A (§5), solution class S1: maximize J[Σ] = ∫F[Σ; s(ξ)]dμ(ξ).
Deliverables: stationarity system (T2: per-phase Rao/Kraiko conditions +
μ-averaged wall condition + μ-averaged ENDPOINT-DERIVATIVE transversality
— the weighted form, D3 §4), existence in restricted classes (P7),
multiplier regularity (P3).

PB-2 (truncated plug / first genuinely averaged optimum). PB-1 for
configuration (ii) with L_p < l(ξ_peak) and a base-pressure closure:
T4's nesting fails, max∫ < ∫max strictly; compute the cycle-optimal
truncated plug vs peak- and mean-designed baselines (Table-1 states).
This is the first concrete problem NOT solved by any single-phase design.

PB-3 (shrouded duty split — conjecture C1). PB-1 for configuration (iii):
optimal division of expansion duty between fixed shroud (collapse-prone,
wants ⟨Pc⟩) and free plug (peak-seeking) under length/heat constraints;
mixed averaged corner conditions (CSTR_PA averaged at shroud lip, plug
corner averaged at truncation).

PB-4 (bilevel/coupled). max_Σ J[Σ; s(·;Σ), μ(Σ)] with the chamber limit
cycle as lower level; tractable middle rung: differentiable reduced
response map Σ ↦ (PR, Ω_w, fill) from the matched-cycle machinery; full
reacting adjoint = declared frontier.

PB-5 (robust). Mode multistability and μ-misspecification: maximize
E_π[J] or CVaR_β, π calibrated on operability maps; Wasserstein-DRO ball
around nominal μ. The formulation of record whenever H-A1 fails.

Ladder bridges (rigor obligations, not slogans): rung1(=I4/T3,T4 oracles)
⊂ rung2(PB-1..3) —O(St) bridge P4→ rung3(T0/freezing, HB, shadowing) —
coupling→ PB-4/PB-5.
