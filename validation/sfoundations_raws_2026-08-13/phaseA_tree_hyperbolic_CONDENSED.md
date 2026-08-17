# CONDENSED (mechanical slice; authority = phaseA_tree_hyperbolic.md, line refs cited)

[L102] FORK-1: How is J_exact related to computable steady objects?
  - Recommendation: (b) as the exactness anchor, with (c) as its falsifier
    rung and (d) as last-resort bracket. Grounds: it is the ONLY bridge that
    is exact at marginal Strouhal; it converts requirement (v) from an
    asymptotic apology into two measurable terms (FORK-39).

[L145] FORK-2: What IS the per-phase steady problem of the surrogate?
  - Recommendation: (a), with the (a)-vs-(c) commutator measured, not assumed
    (FORK-39): the defect of (a) is the azimuthal-flux commutator — the
    axisymmetric ensemble deletes the d/dtheta transport of axial momentum by
    cycle fluctuations, whose magnitude is set by the helix angle
    tan(alpha_h) = Omega*r/u_x (the geometric face of the marginal Strouhal).

[L175] FORK-3: Existence of the time average; bracket policy when the exact flow
      does not settle to the rotating wave.
  - Recommendation: (b) primary. Key lens fact: the plume free boundary is a
    vortex sheet against quiescent ambient; 2D compressible vortex sheets are
    linearly stable for relative convective Mach > 2*sqrt(2) (Miles 1958;
    Fejer–Miles 1963) and KH-unstable below; axisymmetric/finite-thickness
    corrections via convective Mach number Mc (Papamoschou–Roshko 1988). The
    certificate must therefore CHECK Mc phase-by-phase rather than assert
    stability. Downstream shear-layer instability need not destroy J-existence
    (it may only unsteady the far plume, outside the thrust domain of
    influence — FORK-21), so couple this fork to the control-surface fork.

[L209] FORK-4: Solution class for the per-phase state (THE state-model fork).
  - Recommendation: (b) as the CERTIFIED class, (c) as the exploration/fallback
    class with an explicit downgrade flag. Certified optima must have states
    IN (b), certified by FORK-23 monitors. Non-uniqueness policy: work where
    uniqueness is a theorem or a checked monitor, never rely on scheme
    selection (FORK-5).

[L251] FORK-5: Admissibility and uniqueness selection inside the weak class.
  - Recommendation: enforce (a)+(c) at every fitted front, with (d) as the
    declared selection principle; dry note: in the piecewise-smooth class on a
    domain of determinacy, local uniqueness follows from characteristic energy
    estimates (Li–Yu theory) + Majda front stability — the wild-solution
    pathology lives in the unconstrained weak class, not in (b) with Lax
    fronts. The certificate line is exactly: "state is in class (b) with all
    fronts Lax-admissible and uniformly stable"; uniqueness claims are scoped
    to that.

[L275] FORK-6: Thermally-perfect gas structure: characteristic thermodynamics.
  - Recommendation: (b) realized as (c). Mandatory audits: monotonicity of
    h(T); a^2 = (dp/drho)_S > 0; fundamental derivative Gamma_fund =
    1 + (rho/a)(da/drho)_S > 0 over the reachable (T,p) set (cheap quadrature
    over the table range) — this single audit underwrites FORK-5's use of Lax
    conditions and Majda's stability hypotheses.

[L305] FORK-7: Swirl in the per-phase state model.
  - Recommendation: (b), unconditionally (the cost delta is one ODE invariant).

[L328] FORK-8: PDE formulation for computation (per phase).
  - Recommendation: (a) as the certifying instrument with (b) as its
    conservation-exact twin oracle (disagreement beyond derived bands rejects
    a run — agreement is NOT truth, only non-rejection); (c) for uncertifiable
    or sonic-pocket states and as sector-agnostic explorer.

[L364] FORK-9: Front inventory and per-type fit-vs-capture policy.
  - Recommendation: (c)/(d): fit the lip system and any wall-incident shock;
    fit contacts that carry entropy-layer thrust bias; capture the rest in the
    FF-B twin. Front-strength threshold DERIVED: fit any front whose
    contribution to the DWR error estimate exceeds the assigned budget line.

[L396] FORK-10: Fitting technology.
  - Recommendation: (b) within FF-A marching for the primary lip/wall shock
    families (one front family per marching strip); (d) as the modern upgrade
    path if front-interaction complexity grows; (c) reserved for the FF-C 3D
    reference if fitted fronts are wanted there. Grounds: (b) gives the RH
    Jacobians in closed form for the adjoint (FORK-29).

[L423] FORK-11: Spontaneous shock formation and front-topology change.
  - Recommendation: (b) inside the FF-A march (it is cheap: the characteristic
    net is already there) + (c) as the independent cross-check per certified
    design. Every insertion/removal event is LOGGED as a stratification
    boundary in (S, xi) space — these are exactly the loci where J loses
    classical differentiability (see FORK-33/29).

[L450] FORK-12: Contacts, slip lines, entropy layers.
  - Recommendation: (a) in FF-A always (zero extra cost, exact transport of
    the three streamline invariants by construction); in FF-B accept smearing
    but charge it: the entropy-layer smearing bias on thrust is a named (v)
    carrier, measured by the FF-A/FF-B twin diff.

[L467] FORK-13: Front stability certification.
  - Recommendation: all three as standing monitors in the certification list
    (FORK-23). Note the honest scope: (b) instability of the FAR plume shear
    layer does not void the thrust certificate if the control surface
    decouples it (FORK-21); it voids the FF-C exactness claim unless FORK-3(b)
    passes upstream of the control surface.

[L500] FORK-14: Subsonic patches on Gamma_d: policy + causal-separation audit.
  - Recommendation: (a) as the certified default with the margin monitor as a
    standing audit; (b) as the declared closure for data families that need
    it. Grounds: every other option imports an unauditable hypothesis or
    breaks the data contract.

[L544] FORK-15: Sonic surface / embedded transonic region treatment.
  - Recommendation: (a) where its audit passes, (b) as fallback; either way
    the sonic region OUTPUT is only consumed through FORK-16's start surface.

[L577] FORK-16: Start-surface placement: the limiting-characteristic rule.
  - Recommendation: (a) for supersonic phases; (b) for choked closures, with
    the limiting-characteristic location COMPUTED (trace the C- family from
    the sonic-bubble edge), never assumed at the geometric throat.

[L602] FORK-17: Spacelike certification, including the swirl margin.
  - Recommendation: (b) implemented, (c) as its generality audit. The margin
    epsilon_sl is DERIVED: the smallest margin for which the truncation-error
    and front-position error bounds hold uniformly (the error constants blow
    up as (u·n/a - 1)^{-1/2} near sonic — the derivation names this constant).

[L622] FORK-18: Lip/corner treatment at attachment set Lambda.
  - Recommendation: (a): insert the exact centered solution as internal data;
    it is simultaneously the lip-shock generator on overexpanded phases (fan
    of compression -> immediate coalescence => fitted lip shock per FORK-11(b)
    detector at the corner itself).

[L640] FORK-19: Axis r = 0 treatment.
  - Recommendation: (a)+(b): axis unit process with a one-term parity-correct
    series; enforce Gamma_circ = O(r^2)... audit: swirling data families
    CANNOT reach the axis with nonzero circulation — a vortex-core structure
    or an on-axis solid (plug) is REQUIRED; make this an explicit sector
    certificate (a bell sector with swirling flow through the axis region
    must show the computed vortex-core resolution or be rejected).

[L661] FORK-20: Free plume boundary (p = Pa) treatment.
  - Recommendation: (a) in FF-A (the free boundary is one more characteristic
    interface — cheap in marching); (b) in FF-B. The free-boundary position
    is part of the state vector for the adjoint (its linearization is the
    free-boundary shape derivative — FORK-29 must carry it).

[L683] FORK-21: Control-surface placement and the plume-decoupling certificate.
  - Recommendation: (a) with per-sector fallback (b); the decoupling
    certificate (pointwise spacelike check on Sigma_e + geometry check) is a
    standing monitor. This is what makes strongly-overexpanded phases with
    Mach disks CERTIFIABLE for bell sectors: the disk lives downstream of
    Sigma_e; the state upstream remains in class FORK-4(b).

[L713] FORK-22: Per-phase BVP well-posedness framework.
  - Recommendation: (a)+(b) as the theorem shelf with explicitly LOCAL scope,
    monitors (FORK-23) covering the gap to global claims; (d) enforced at the
    discrete level (GKS/SBP-SAT-style boundary implementations in FF-B).

[L748] FORK-23: Solution-class membership certification (the monitor list).
  - Recommendation: certificate = conjunction m1–m10, emitted as a machine-
    checkable record per (S, xi). NO state consumed by the optimizer or the
    averaging quadrature without its record (FORK-24).

[L774] FORK-24: The certification boundary inside the optimization loop.
  - Recommendation: (b) primary with (a) as backstop for monitor classes
    without usable margins; the certified-class boundary becomes part of the
    active set in the KKT system (its multiplier prices "how much J is being
    held back by certifiability" — decision-relevant information the brief's
    (ii) explicitly wants multipliers to carry).

[L801] FORK-25: Primary discretization + oracle pairing (concretizing FORK-8).
  - Recommendation: FF-A = (a) upgraded toward (c) for conservation aud its;
    FF-B = (d) (entropy-stable FV, smooth limiters) with (e) as the
    high-order upgrade path; (h)/(i) tracked as modern options, adopted only
    after oracle-suite qualification. Oracles for both: exact gamma(T)
    quadrature solutions (quasi-1D, Prandtl–Meyer, source/conical rotational
    flows integrated by ODE), plus manufactured solutions (MMS, Roache) for
    the axisymmetric-with-swirl operator including axis terms.

[L833] FORK-26: Error estimation for the state and for J.
  - Recommendation: (a) primary (it also drives adaptation, FORK-27, and
    supplies the derived tolerances of FORK-40); (b) as an independent
    cross-check with measured order; safety factors DERIVED from the ratio of
    estimated-to-realized error on the oracle suite (no magic 1.25).

[L854] FORK-27: Mesh / refinement policy.
  - Recommendation: (a) for FF-A, (b) for FF-B, (e) as the design-loop mesh
    contract, (c) as the verification harness.

[L874] FORK-28: Captured-fallback differentiability: limiter and flux class.
  - Recommendation: (c)+(b) for FF-B, with (d) on the theory shelf as the
    justification and as the analysis of what error the smoothing introduces;
    FF-A largely sidesteps the issue (fitted fronts => piecewise-smooth
    discrete map).

[L901] FORK-29: Fronts in the derivative/adjoint calculus (THE fidelity fork).
  - Recommendation: (a) in FF-A as the gradient of record, (d) as its
    continuous twin for consistency checks, (b) only for FF-B exploration
    gradients (flagged non-certified). The averaged gradient is the
    mu-integral of per-phase adjoint wall tractions + front terms (the
    "averaged wall condition" of requirement (ii) emerges here).

[L937] FORK-30: Optimize-then-discretize vs discretize-then-optimize.
  - Recommendation: (c) operationally: DtO gradient feeds the optimizer; OtD
    twin computed at audit points; their difference must contract under
    refinement at the verified order (a standing rejector).

[L960] FORK-31: Gradient mechanics and verification duties.
  - Recommendation: (a)+(c) for FF-A; (b)+(c) for FF-B; (d) demoted to
    smoke test.

[L980] FORK-32: Second-order machinery for requirement (iii).
  - Recommendation: (a) with (d) handled by the fitted linearization; (c) as
    cross-check when dim <= O(50).

[L1001] FORK-33: Phase quadrature and aggregation across xi.
  - Recommendation: (b)+(c): stratify at detected events, adapt within
    strata, quadrature error a NAMED (v) line; the gradient integral uses the
    same strata (dF/dS is discontinuous across events even where F is
    continuous). If mu arrives as data samples: (e) for the loop, (b) for the
    certificate.

[L1026] FORK-34: Design representation of the solid S.
  - Recommendation: (f) with (a) inside sectors ((b) as the mesh-motion
    carrier); (c) allowed ONLY in the FF-B exploration layer to DISCOVER
    sector candidates, whose output is re-instantiated as (f) before any
    certificate. Existence framing for (i): the class A(c) with uniform cone
    property is compact for Hausdorff-type convergence (Chenais 1975); J
    upper-semicontinuity along certified sequences is the part to prove/
    monitor (front-stable continuous dependence — FORK-13/22), with a
    declared failure boundary where certification is lost.

[L1069] FORK-35: Optimality framework: does the classical exit-characteristic
      reduction survive averaging?
  - Recommendation: (a), with (c) as initializer and the Dirac-mu Rao oracle
    as a standing rejector of the whole optimality implementation.

[L1106] FORK-36: Optimizer class and globalization (breadth fork).
  - Recommendation: (a) [trust-region SQP, exact penalties for the few
    nonsmooth constraint aggregates] + (c) for global coverage + (d)/(e)
    quarantined in FF-F for sector census; (b) as the scale-up path.

[L1144] FORK-37: The globality certificate (requirement (iv)).
  - Recommendation: report the CHAIN delta_a >= delta_b >= 0 with
    delta_b = B_var - J[S*] as the headline certificate, (d) closing the
    sector dimension, (f) proven on its strata; (c)/(e) explicitly declined
    with reasons.

[L1195] FORK-38: Separation/attachment constraint g_sep.
  - Recommendation: (c) as detector of record with (a) as its cheap bound
    and cross-check; (e) wired into the front logs; margin g_sep and its
    adjoint contribution enter the averaged KKT system (multiplier = price
    of attachment, requirement (ii) semantics).

[L1225] FORK-39: Error-bar architecture for requirement (v).
  - Recommendation: publish the budget as a table with measured values and
    derived bands per certified design; the budget PARTITION is itself
    derived (next fork).

[L1253] FORK-40: Tolerance and stopping derivation (no magic constants).
  - Recommendation: (a); every tolerance in the certificate record carries
    its derivation hash (which budget line, which measured curve).

[L1273] FORK-41: H-DATA monitor design.
  - Recommendation: all four are cheap; (b)+(d) run on every data delivery,
    (a) when signals exist, (c) as part of each FF-C rung audit. On ANY
    trip: t1 of FORK-39 switches from "zero (proved)" to the bracket branch,
    and the certificate downgrades explicitly — H-DATA is monitorable, so
    the certificate must MOVE when it fails, not die silently.
