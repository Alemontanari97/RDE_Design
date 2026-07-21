# T3-QS — Quasi-steady protection of the collapse class
# (first-order sweep cancellation on ray families; the jump-localized
#  residue; the off-ray area term)

Status: RESULT OF RECORD (2026-07-21, S12, [F4-prep/T3QS]; discovered
and machine-verified in the 2026-07-20/21 review conversation, R4
back-propagated here). Registry: theorem [T-T3QS], carrier [X-T3QS]
(validation/t3qs_sweep_protection.py, VERDICT PASS: P1-P6 + rejectors
R1-R3; suite group (xvi)). ANCHOR: (P) of M0 D2.6; lives INSIDE the
P4 first-order framework [J-CT1] — it is a statement about the
first-order corrector J1 of D3 §3, not an independent expansion.

------------------------------------------------------------------------------
## §1 Setting and statement

Rung 2 (method A) deletes from the exact wave-frame system the
azimuthal coupling operator

    D(W) = (1/r) d_theta' [ F_theta(W) - Omega r W ],

which is the lab-frame time derivative transformed by theta' =
theta - Omega t (the unsteadiness of the lab frame turned into
azimuthal structure; M0 Theorem 0 "the only approximation" + M0
Lemma 4 sweep term). The first-order thrust error is
J_1 = -Int <psi_J(xi), D(W_A(.;xi))> dxi  (D3 §3, [J-CT1] frame).

THEOREM T-T3QS (algebraic core symbolic-sufficient, EOS-general:
ideal gas with ARBITRARY caloric e(T); carrier X-T3QS). On a T3 RAY
family — phases differing only by the pressure scale k(xi) = Pc(xi)/
Pc_ref at fixed (u, T) fields (H3 + Pc-only cycle; Lemma T3-A in
conservative form) —
 (P1) the scaling is LINEAR in conservative variables: W -> kW;
 (P2) Euler fluxes (any direction), the axisymmetric geometric
      source, and the Rankine-Hugoniot relations are degree-1
      homogeneous along the ray (the fitted-sheet position is
      k-invariant);
 (P3) hence (Euler's theorem) ALL flux Jacobians are invariant along
      the ray: the per-phase linearized operator is ONE operator;
 (P4) the thrust-objective W-gradient is invariant along the ray
      (degree-1 homogeneous part minus the constant Pa n_x): the
      adjoint SOURCE is phase-independent; with the T3-class BC
      structure (H3: geometry and (M, theta) fields phase-invariant)
      the per-phase adjoint is ONE fixed field psi_hat (uniqueness of
      the linear adjoint solve, S1 apparatus);
 (P5) the sweep term factorizes: D(W_A) = k'(xi) · Z with Z a fixed
      field;
 (P6) therefore J_1 = -<psi_hat, Z> · Int k'(xi) dxi:
      = 0 EXACTLY on smooth periodic cycles;
      = <psi_hat, Z> · [k]_jump on the blowdown sawtooth — the ENTIRE
      first-order sweep correction concentrates at the wave-passage
      jump.

REJECTORS (in the carrier, each fires): R1 non-ray direction (T
scaled too) breaks P3; R2 H3 violation (theta-dependent What) breaks
P5; R3 non-affine objective breaks P4.

------------------------------------------------------------------------------
## §2 Physical reading (of record — the anatomy of the neglected term)

D(W) at swirl-free data splits into exactly two mechanisms:
 (a) SWEEP TRANSPORT -Omega d_theta' W: each parcel transits the
     nozzle in tau_res while the pattern rotates over it — it samples
     a phase interval Delta xi = St, not one phase; equivalently the
     interior LAGS the inlet phase by the local transit time. Rung 2
     sets the lag to zero (each meridional slice is a closed
     universe: a player-piano roll where reality is a glissando).
 (b) AZIMUTHAL PRESSURE COUPLING (1/r) d_theta' p (the only content
     of F_theta at u_theta = 0): hot post-wave sectors push sideways
     on cold pre-wave sectors — inter-phase momentum exchange and
     SWIRL GENERATION from swirl-free data (the N6 boundary's
     entry point: generated swirl is generically non-free-vortex).

WHY THE MEAN IS PROTECTED (the cancellation mechanism): on the ray,
the thrust correction at phase xi is c·k'(xi) with ONE exchange rate
c for every phase (P3+P4). During blowdown decay each parcel carries
slightly STALE high-pressure benefit (surplus vs quasi-steady);
during the rise the mirror deficit; same rate => exact cancellation
over the period: at first order the lag acts as a PURE PHASE SHIFT
of the response, and a phase shift does not change a mean
(<f(t - tau)> = <f(t)>). The mean feels the sweep only where
 (i) the signal JUMPS (parcels whose transit STRADDLES the wave
     passage see genuinely different physics, not a delayed copy) —
     a xi-window of width ~St, precisely the physics the fitted
     inherited sheet already represents steadily; or
 (ii) the exchange rate itself varies around the cycle (OFF-RAY:
     (P0, T0) both varying at gamma(T), phase-dependent profile
     shapes, cap-binding subcritical phases): the integrand becomes
     a generically non-exact 1-form and J_1 equals the AREA integral
     of its exterior derivative over the data loop — quasi-steady
     HYSTERESIS, the exact analogue of net work from a
     thermodynamic cycle enclosing area.

------------------------------------------------------------------------------
## §3 Boundary and consequences (declared)

 B1 SCOPE: ray cycles (Pc-only) — EOS-general. Two-parameter cycles
    ((P0, T0)(xi), calorically imperfect) leave the ray: first-order
    residue = the area term (computable; a natural O5-lite target).
 B2 CAP-BINDING PHASES are off-ray by construction (the sonic cap
    changes the family structure) — consistent with the independent
    physical finding that subcritical phases carry the internal-shock
    ACOUSTIC LAG (tau_ac ~ L_div/(c-u) ~ 0.1-0.3 ms vs T ~ 0.2-1 ms:
    ratio O(0.1-1)); the choked throat is the dam (no upstream
    influence past it); route B's steady helical shock surface
    embodies this lag exactly, rung 2 misses it — an A-vs-B channel.
 B3 INTERPRETATION FRAME: the J_1 = 0 conclusion is a statement about
    the FIRST-ORDER term of the [J-CT1] expansion; it does not by
    itself bound the remainder (the expansion degrades exactly in the
    jump window, where fitting takes over).
 B4 CONSEQUENCES: (i) explains why the field's quasi-steady practice
    (S-H, EAP) outperforms naive St ~ 0.1-0.3 estimates — the
    collapse class is SECOND-ORDER protected; (ii) explains the
    severity of the single-cycle PDE case (start-stop = maximal jump
    + maximal data-loop area; Gonzalez-Viana 2025, Cooper-Shepherd);
    (iii) TARGETS the O5 measurements: the wave-passage window and
    two-parameter cycles are where the license number lives —
    pre-registered predictions in D6 Phase A4.
