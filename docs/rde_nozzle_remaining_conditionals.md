# The remaining conditionals — statements and proof architectures
# (D2.5-U, P4-Fredholm, Lemma-B mesh limit, second order)

Status: RIGOR ATTACK OF RECORD (2026-07-16, Sessione 8-rigore, final
pass; [F1/D25U + F1/P4F + F1/LBML + F1/SO]). ANCHOR: (P) of M0 D2.6.
These four items are the LAST named function-space gaps of the
theory; none admits a symbolic carrier (declared per the sufficiency
discipline) — the deliverable here is, for each, a PRISTINE statement
with its proof architecture, constant dependencies, and falsifier.
[Cost re-pricing of record, S14 (PAN-S14 F-D25USPLIT): "bounded work,
not research risk" is SUPERSEDED for the -c component of §1 — see the
component note there; it stands for the -a/-b components.]

------------------------------------------------------------------------------
## §1 LEMMA D2.5-U (the shared uniform-stability conditional)

This is THE single conditional inherited by T7-FS, P7-S1, P3, S1-U
and G12-S1 (R-T7.1 = R-P7.1 = R-U assembly = R-G12.1). Stating it
once, sharply, replaces five scattered references.

STATEMENT (target class THEOREM*; the proof is classical two-variable
hyperbolic analysis, steps below). Let D(delta, L_x, C_geo, C_dat) be
the certified set: wall in C^2 with norm <= C_geo; data on the inflow
segment with C^1 norm <= C_dat; axial spacelikeness margin
M_x - 1 >= delta; boundary-function margin >= delta; on shocked
references, Lax front-strength margins >= delta with transversal
wall/front angles >= delta.
[AMENDMENT OF RECORD, S15 2026-08-05 ([S-D25U-U1], discovered by
EXECUTING U1): the certified set is D(delta, L_x, C_geo, C_dat,
h_min) — the DUCT-WIDTH FLOOR w_+ - w_- >= h_min > 0 is a NAMED
constant. Without it the acoustic bounce count Lambda L_x / h_min is
unbounded and, with reflection factors > 1 (possible in converging
geometry), the uniform-constants claim below is FALSE as written.
Physically free (throat height > 0); every C-D25U-derived statement
carries the fifth constant from now on.] CLAIM: on D, for x-intervals of length
<= L_x, the S1 solution map
    (wall, data) -> (U, fronts)
is well-defined and LIPSCHITZ into piecewise-C^1 x C^1-graphs, and
C^1 (in the shift sense across fronts), with ALL constants depending
ONLY on (delta, L_x, C_geo, C_dat) — never on the individual
solution.

PROOF ARCHITECTURE (steps named; each classical, none yet written):
 [NAMESPACE NOTE, S14 2026-08-04 (PAN-S14 addendum, verified): these
 D2.5-U proof-architecture steps U1-U5 are DISTINCT from the theorem-
 ledger §10bis method-upgrade list U1-U5; cite qualified — "D2.5-U U*"
 vs "10bis U*".]
 U1 Smooth regions: characteristic-ODE reformulation of the
    x-evolution (G12-L1 structure); C^0 and C^1 bounds by Gronwall
    along the three characteristic families on x-intervals bounded by
    L_x; constants from the coefficient bounds (margins keep the
    characteristic slopes uniformly transversal and the ODEs
    uniformly Lipschitz). [Li-Yu semiglobal machinery of record,
    instantiated — the writing task is bookkeeping, not new
    mathematics.]
    [U1 STATUS, S15 2026-08-05: WRITTEN — docs/rde_nozzle_D25U_U1.md
    ([S-D25U-U1]): C^0 (§3), C^1 (§4), two-solution Lipschitz -a
    (§5, explicit LIP(delta, L_x, C_geo, C_dat, h_min)), -b smooth
    corollary (§6); wall reflection exercised at U1's level; cost
    claim CONFIRMED bounded, with the h_min discovery (amendment
    above). U2 standalone lemma, U3, U4 remain named.]
 U2 Slip-wall reflection: the wall is characteristic for the
    streamline family and reflecting for the acoustic families;
    uniform reflection estimates need the C^2 wall bound and the
    margin (no glancing: spacelikeness keeps the acoustic families
    uniformly transversal to the wall). [Standard; must be written.]
    [U2 BRICK STATUS, S15 2026-08-05 ([T-U2RG], carrier X-U2RG,
    suite (xiii), PASS 8/8): the algebraic core is machine-verified
    at abstract EOS — glancing at slip IMPOSSIBLE (no C_geo/C_dat
    input needed: hypothesis reduction), reflection-solve degeneracy
    exactly at total-sonic q = c (excluded by the axial margin
    alone), closed-form R with margin bound, slip necessity by
    counterexample. Residue: only the composed estimate bookkeeping
    inside U3/U4.]
 U3 Fronts: local straightening; the front ODE and downstream traces
    are Lipschitz in the upstream traces UNIFORMLY by the certified
    equilibrated s_min of the linearized RH (G12-L2 — the
    quantitative constant is ALREADY a measured, machine-certified
    number at the reference; uniformity over D follows from the
    strength margins). Iterate over the (uniformly finite) front
    count.
 U4 Composition: finitely many regions and fronts on [0, L_x];
    constants compose multiplicatively — total constant explicit in
    (delta, L_x, C_geo, C_dat). QED (architecture).
 [COMPONENT NOTE OF RECORD, S14 (PAN-S14 F-D25USPLIT): U1-U4 as named
 deliver the -a (estimates/Lipschitz) component only; -b
 (well-definedness/uniqueness) is discharged BY the S1-U assembly,
 which uses only -a; the -c component (shift-C^1 of the MAP:
 linearized well-posedness + quadratic remainder) has NO named
 discharger — U5 is hereby NAMED MISSING, lead Bressan-Guerra/Ulbrich
 (TO-VERIFY, R-G12.2 status). -a/-b = classical two-variable
 estimates; -c = research-grade.]
 [LEAD SYNC, 2026-08-05 (D8 §8 roads-atlas residue, second-lens): the
 on-point U5/-c lead is Breitkopf-Ulbrich arXiv:2509.22076 (2025) —
 C^1 control-to-state for the generalized Riemann problem — alongside
 Bressan-Guerra/Ulbrich; already of record in lit map b3, hypothesis
 ledger C-D25U row, and D25U_U1 §8; acquisition pending.]
FALSIFIER: a certified family in D with solution-map Lipschitz
constant blowing up while all margins stay >= delta (would contradict
U1-U4; executable once A1 computes solution sensitivities).
CONSEQUENCE: discharging D2.5-U simultaneously converts T7-FS, P7-S1,
P3 and (with its assembly) S1-U from THEOREM* to THEOREM in the
shock-free class, and sharpens the across-front conditional to the
single Majda-stability ingredient.

------------------------------------------------------------------------------
## §1bis C-XBVP (Cauchy->BVP transfer residuals; minted S15 2026-08-05)

Inherited by [T-XWS] (docs/rde_nozzle_cauchy_bvp_transfer.md — the
x-as-time weak-strong transfer that gives shock-free canonicity a
BVP-native proof skeleton). Stated ONCE here; two components:
 (a) S-XCONV DISCHARGE: strict convexity of the x-entropy
     eta = -rho u g(S) as a function of the x-flux vector m on the
     WHOLE certified compact K with axial margin u - c >= delta
     (currently instance-certified: 200/200 randomized margin-box
     states definite, subsonic rejector 60/60 indefinite, sonic
     pincer sharp — carrier X-XBVP). Natural discharger: interval
     arithmetic over the box (connects to the S15 global-maximum
     dossier toolbox); EOS-general statement, ideal-gas instance.
     [(a) DISCHARGED AT INSTANCE LEVEL, 2026-08-05 (S15 reopened
     segment): X-IVXC interval certificate — outward-rounded
     arithmetic, Krawczyk solve, mean-value form, interval LDL^T,
     43199 boxes, VERDICT PASS — certifies strict definiteness over
     the whole declared (M, V) box, and by the T-XRED scaling
     reduction for EVERY (rho, S): stronger than the declared
     target. Residue of (a): the abstract-EOS statement only
     (schema). The libm-1ulp assumption is DECLARED in the carrier.]
 (b) WEAK-SIDE TECHNICALITIES: x-slice normal traces and wall traces
     for the entropy-solution class of T-XWS (Dafermos-class
     bookkeeping; strong traces available in BV; the strong side is
     C^1 and free).
Neither component touches the algebraic content (T-XSON sonic
bijection, T-XWALL wall annihilation, pair identity) — those are
THEOREM at abstract EOS. FALSIFIER: see the T-XWS row of the
registry (two distinct entropy solutions on identical certified
inflow data inside K).

------------------------------------------------------------------------------
## §2 P4-FREDHOLM (reduction to a monodromy condition)

STATEMENT (reduction — class THEOREM* at statement level). Under the
periodic scoping, the linearized decoupled operator L = DN_0(U_0)
acts phase-wise: (L U_1)(xi) = L_xi U_1(xi) with L_xi the linearized
PER-PHASE marching operator (invertible on each phase by G12-L1 +
D2.5-U: a linear hyperbolic evolution with certified margins). The
sweep source couples phases through d_theta' = (1/Omega_w) d_xi.
Hence solvability of L U_1 = -S_sweep(U_0) on the periodic class
REDUCES to the invertibility of a PERIOD MAP: writing the
xi-coupling as a linear evolution in xi with phase-wise-solvable
coefficients, the Fredholm alternative on the circle holds iff
    1 is not in spec( Pi ),
Pi = the monodromy operator of the linearized phase-transport over
one cycle. THE SPECTRAL HYPOTHESIS IS THEREBY IDENTIFIED with the
P1a/P1b neutral-mode margin OF RECORD: a neutral rotating-mode
perturbation is exactly a fixed point of Pi. Remaining analysis
(named): compactness/Riesz theory for Pi on the appropriate C^1
class (to convert "1 not eigenvalue" into bounded invertibility) and
the quantitative IFT remainder — MINTED as registered conditional
[C-P4RZ] (S14, PAN-S14 F-CLASSES + X2 exchange: Pi is the monodromy
of a linear hyperbolic transport, generically non-smoothing, hence
non-compact — the Riesz step is genuine analysis; until discharged,
the computed eigenvalue margin is a MONITORED SURROGATE of the full
spectral condition). FALSIFIER: O5 — the computed
J_1 = -<psi_J, S_sweep(U_0)> against unsteady simulation; divergence
beyond bars at certified spectral margin kills the reduction.

------------------------------------------------------------------------------
## §3 LEMMA-B MESH LIMIT (consistency of the fitted-AD gradient)

STATEMENT (target THEOREM*). On smooth regions, the MOC unit process
is a one-step method of order h^2 for the x-evolution of G12-L1; at
fronts, the implicit-rule differentiation is a consistent
discretization of the linearized RH (G12-L2). CLAIM: the discrete
tangent (hence, by the exact transpose identity of Lemma B, the
discrete adjoint/gradient) converges at order h^2 to the continuum
shift-derivative of THEOREM G12-S1 on certified references.
PROOF ARCHITECTURE: (i) CONSISTENCY: Taylor expansion of the unit
process against the exact characteristic ODEs — order h^2 by
construction (the O3.2 order check is its executable falsifier);
(ii) STABILITY of the linearized march: discrete Gronwall along the
discrete characteristics, uniform by the D2.5-U margins (the same
constants); (iii) Lax-equivalence argument (consistency + stability
=> convergence) applied to the TANGENT system; (iv) the gradient is
the transpose of a convergent stable linear solve — convergence in
the dual norm is inherited (finite-dimensional transpose, exact);
(v) fronts: the implicit rule solves the discretized linearized RH
whose continuum limit is nonsingular (certified s_min) — front-shift
convergence at the same order. FALSIFIERS: O3.2 (order), O3.3 (term
match), F2 of G12-S1 (FD-vs-AD at fitted shocks).

------------------------------------------------------------------------------
## §4 SECOND-ORDER (one honest paragraph)

With T7-FS proven, the SECOND shape derivative of J exists under one
more degree of the same conditional (D2.5-U at second order — named,
not claimed), and the reduced-Hessian negativity check of (P)(iii)
tests a well-defined object. No second-order THEORY (sufficient
conditions, quadratic growth) is claimed anywhere in the program;
the Verdict reports the computed spectrum. Falsifier: none needed
(the check is itself the instrument); upgrading to sufficient
conditions is OUT OF SCOPE of the current phases and declared such.

------------------------------------------------------------------------------
## §5 Register

| Item | Class now | Symbolic suffices? | Discharge cost |
|---|---|---|---|
| D2.5-U statement + architecture | THEOREM* target; U1 WRITTEN S15 ([S-D25U-U1], h_min amendment); U2 exercised, U3/U4 named | NO (function space) | bounded: classical 2-variable bookkeeping — CONFIRMED by execution (U1 one session) |
| C-XBVP (transfer residuals, S15) | conditional; algebraic bricks T-XSON/T-XWALL are THEOREM | (a) interval-proof candidate; (b) NO (function space) | (a) bounded: interval arithmetic over the certified box; (b) bounded: Dafermos-class trace bookkeeping |
| P4-Fredholm reduction to monodromy | THEOREM* (statement) | NO | Riesz theory + quantitative IFT |
| Lemma-B mesh limit | THEOREM* target; steps (i)-(v) named | NO (numerical analysis; O3 oracles as falsifiers) | bounded: Lax-equivalence instantiation |
| Second order | declared instrument, no theory claimed | — | out of scope, declared |
