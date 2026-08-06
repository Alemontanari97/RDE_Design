# The ergodic G-B lemma — transfer of the geometry-free ceiling to
# the exact (time-averaged) objective (the PP-2 missing lemma, written)

Status: RIGOR ATTACK OF RECORD (2026-08-06, S16 deep-foundations
campaign second tranche, T4 [RIGOR/A]). Target: the S14 panel finding
PP-2 (arbiter-confirmed, M0 Parte V chaotic-tier row + D5 Step 8
note): the ladder's upper wall (Prop. G-B, [T-GB]) was proven in the
STEADY per-streamtube setting only; its transfer to the ergodic
targets [J_exact^-, J_exact^+] (D2.2) was a NAMED MISSING LEMMA
("Birkhoff + bounded momentum route") — else the chaotic-tier bracket
de-rates to SCHEMA. THIS DOCUMENT WRITES THE LEMMA. Registry:
[S-GBE]; carrier [X-GBE] validation/gbe_ergodic_envelope.py (suite
group (xiii), 2.1 s).

Audit line: [Class: SCHEMA overall (function-space averaging with
DECLARED hypotheses E1-E5; the pointwise flux lemma §2 and the
envelope identity are THEOREM-grade with carrier; composite-envelope
concavity = symbolic per branch + numeric on the scanned box) |
Falsifier: carrier rejectors R1/R2 + any dataset with bounded storage
and axially-sonic exhaust whose measured J̄ exceeds the §4 ceiling
beyond bars | Carrier: X-GBE | Gamma: EOS-general skeleton (h(s,p)
convexity in s is EOS-general: d2h/ds2|_p = T/cp > 0); the sonic-
branch closed forms and the carrier = declared perfect-gas instance
(abstract-EOS residue = schema, same pattern as S-XCONV)].

VERDICT UP FRONT: the transfer HOLDS — no de-rate needed. Under
declared hypotheses (bounded storage, axially-sonic exhaust surface,
admissibility) the ceiling transfers to J_exact^+ with the ceiling
evaluated at the MEAN interface fluxes. Two structural findings:
 (F1) the OP-0 SONIC CAP is not a patch on the ideal — it is EXACTLY
      the constrained supremum of the effective exhaust velocity over
      the axially-sonic-or-faster state set (§2): the cap discovered
      numerically at OP-0 re-derives as the sup boundary;
 (F2) NO BIRKHOFF NEEDED: the named route (invariant measure +
      Birkhoff) is sufficient but STRONGER than necessary — finite-T
      Cesàro averages + bounded storage close the argument at the
      liminf/limsup level, exactly matching the D2.2 fallback targets.
      Hypothesis minimization applied to our own named route.

------------------------------------------------------------------------------
## §1 Setting and hypotheses (all declared, each with its monitor)

Fixed solid S (ANY topology — the lemma is geometry-free like [T-GB],
and fully 3-D: nothing below uses axisymmetry); unsteady adiabatic
inviscid flow, slip walls, ambient Pa; control surface = interface
Gamma_d (inflow) + far lateral boundary (at pressure Pa) + exhaust
disk A_e (normal x̂, far enough downstream). F_S(t) per D2.2 on this
surface; J_exact^± the liminf/limsup Cesàro targets.

 E1 ADMISSIBILITY: weak solution with entropy production >= 0
    (physical specific entropy s), fluxes locally integrable so the
    control-volume balances hold distributionally. [Standard class;
    trace bookkeeping at the Dafermos level — same grade as
    C-XBVP(b), declared.]
 E2 BOUNDED STORAGE: sup_t | Int_V (rho, rho u_x, rho E, rho s) dV |
    < infinity. [The "bounded momentum" of the named route; physical:
    finite volume + bounded states; monitor: running storage
    estimate on any dataset.]
 E3 EXHAUST MARGIN: on A_e, u_x >= c a.e. (t, x) (axially sonic or
    faster — the program's own margin class extended to the exhaust
    surface), and p = Pa on the far lateral boundary. [Monitor: the
    same axial-margin audit the S1 class already runs; a subsonic
    exhaust plume = move the surface downstream or DECLARE the
    de-rate — the lemma does not silently cover it. u_x >= c > 0
    excludes backflow automatically.]
 E4 EOS: h(s, p) with T = dh/ds|_p > 0 and d2h/ds2|_p = T/cp > 0
    (EOS-general facts), fundamental thermodynamic consistency on
    the state box.
 E5 MEAN FLUXES: the finite-T inequality (§4) needs nothing; the
    closed form needs Cesàro limits of the interface fluxes (mass
    M̄, energy Ē, entropy Σ̄_in) — else the statement brackets over
    the limit set of mean-flux triples (declared).

------------------------------------------------------------------------------
## §2 The pointwise flux lemma and the envelope identity (F1)

Effective thrust-flux density on A_e at a point/instant with state
(rho, u, v, w, p): f = rho u_x^2 + (p - Pa); mass flux m = rho u_x;
energy flux e = rho u_x H (H = h + |u|^2/2); entropy flux
sigma = rho u_x s.

LEMMA GBE-L1 (pointwise bound; THEOREM-grade). Under E3-E4, at every
point of A_e:   f <= m * V_env(e/m, sigma/m),
where V_env(h0, s) is THE RECORD'S CAPPED ENVELOPE (Prop. G-B with
the OP-0 sonic cap): complete isentropic expansion to Pa where the
supersonic branch reaches it (P0(h0,s)/Pa >= NPR(1,g)), the sonic
exit otherwise.
PROOF. The actual state contributes, per unit mass flux,
c_eff = u_x + (p - Pa)/(rho u_x), with data (h0, s) := (H, s) — note
|u| >= u_x costs nothing extra here: only u_x enters, and the actual
pair (p, u_x) satisfies u_x >= c(s, p) (E3) and
u_x <= sqrt(2(h0 - h(s, p))) (energy). Hence c_eff <= the SUPREMUM of
u' + (p' - Pa)/(rho(s,p') u') over the constrained set
{ (p', u') : c(s,p') <= u' <= sqrt(2(h0 - h(s,p'))) }. THE IDENTITY
(F1): this constrained supremum equals V_env(h0, s) — stationarity in
u' picks u' = sqrt((p'-Pa)/rho') only outside the constraints; on the
admissible set the maximum sits either at the jet-matched supersonic
endpoint (p' = Pa, u' = V_id: the supercritical branch) or at the
SONIC VERTEX u' = c (the cap): the same dichotomy the OP-0 ladder
found by the dF/dA sign argument, now read as a constrained-sup
boundary. WITHOUT the u' >= c constraint the sup is infinite (slow
overpressed states: u' -> 0 with p' > Pa) — the axial margin E3 is
exactly what makes a pointwise ceiling exist; the cap is its sonic
boundary. Machine confirmation: the envelope equals the INDEPENDENT
OP-0 ladder closed forms (cf_ideal/cf_sonic, tested 18/18) at six
NPRs including the critical seam, worst rel. dev. 3.4e-16 [X-GBE S4];
the corrupted (uncapped) rule is rejected at subcritical [R2]. QED.

------------------------------------------------------------------------------
## §3 Concavity of the envelope (the Jensen engine)

V_env is CONCAVE in (h0, s) and DECREASING in s:
 - supercritical branch V = sqrt(2(h0 - K e^{s/cp})): SYMBOLIC
   identities of record [X-GBE S1]: V_h0h0 = -W^{-3/2} < 0 and
   det Hess = (K e^{s/cp}/cp^2) W^{-2} > 0 — strictly concave;
   V_s < 0 (h(s,Pa) increasing in s, E4);
 - sonic branch c* + (p* - Pa)/(rho* c*): SYMBOLIC structure [X-GBE
   S2]: the Pa = 0 part is s-free and concave in h0 (~ sqrt(h0)); the
   Pa-part is (minus) a LOG-CONVEX function (log = affine in s,
   convex in ln h0) hence minus-convex = concave contribution;
 - COMPOSITE across the branch seam: numerically concave at 400/400
   scanned (m, e, sigma) points spanning both branches incl. the
   seam, max scaled Hessian eigenvalue 8.7e-06 vs derived FD floor
   1.5e-05 [X-GBE S3] (the zero ray-eigenvalue of the degree-1
   homogeneous perspective sits at the FD floor by construction);
   the corrupted-envelope rejector fires at 400/400 [R1]. HONESTY:
   composite concavity is carrier-verified ON THE SCANNED BOX;
   off-box (and at abstract EOS) the lemma survives with V_env
   replaced by its CONCAVE HULL — the ceiling only loosens, never
   breaks (declared de-rate map, §6).
Consequently the perspective F_env(m, e, sigma) := m V_env(e/m,
sigma/m) is concave and positively homogeneous of degree 1.

------------------------------------------------------------------------------
## §4 The transfer (averaging + Jensen)

Finite-T averages (no limits needed): integrate the conservation
laws over V x [0, T]:
 (i)  storage terms: |(1/T) Int d/dt(...)| <= 2 sup_t |storage| / T
      -> 0 by E2 (this is ALL the "Birkhoff" the argument needs —
      finding F2);
 (ii) the far lateral boundary contributes 0 to thrust (p = Pa) and
      0 <= mass/energy leakage handled by taking A_e to close the
      surface (declared bookkeeping);
 (iii) entropy: mean outflow flux >= mean interface flux - o(1)
      (production >= 0 + bounded entropy storage).
Then, per finite T, with the time-area mean fluxes on A_e:
    F̄_T  <=  mean of F_env(m, e, sigma)            [GBE-L1]
          <=  F_env(M̄_T, Ē_T, Σ̄_out,T)             [Jensen, §3;
                                                     homogeneity
                                                     absorbs the
                                                     normalization]
          <=  F_env(M̄_T, Ē_T, Σ̄_in,T) + o(1)       [(iii) + V_s < 0]
          =   ceiling at the MEAN INTERFACE FLUXES.
Taking limsup: J_exact^+ <= limsup_T F_env(M̄_T, Ē_T, Σ̄_in,T); under
E5 (Cesàro limits) the right side is the closed form
F_env(M̄, Ē, Σ̄_in); otherwise bracket over the limit set. QED.

JENSEN-GAP HONESTY (the price of genericity): on the PERIODIC scope,
where per-phase data exist, concavity gives
F_env(mean fluxes) >= Int F_id dmu = J_ideal — the ergodic ceiling is
WEAKER (looser) than the per-phase ceiling, as Jensen demands. The
per-phase wall stays the sharp instrument where phases exist; the
ergodic wall covers the chaotic/mode-hopping tier where NO phase
decomposition is available. Both are computable from data; the gap
between them is a REPORTABLE number per dataset.

------------------------------------------------------------------------------
## §5 What this changes in the corpus (R4 map, executed this session)

 - M0 Parte V chaotic-tier row: "named missing lemma or de-rate" ->
   RESOLVED: the bracket's upper wall now holds for the ergodic
   targets under E1-E5 ([S-GBE]); the quasi-steady-only label of D5
   Step 5(f) is LIFTED FOR THE UPPER WALL (the lower rungs —
   attainability constructions — remain steady-setting, unchanged).
 - D5 Step 8: same dated annotation (the robust-surrogate deliverable
   of the chaotic tier now ships with a theorem-shaped unsteady
   ceiling instead of a quasi-steady-labeled diagnostic).
 - D2.2/[D-JEX]: the fallback targets [J_exact^-, J_exact^+] now have
   a certified upper wall — the "only bounds ship" clause has its
   bound.

------------------------------------------------------------------------------
## §6 Residue (named, honest)

 - Composite concavity: symbolic per branch, numeric-on-box for the
   seam; a global symbolic proof (or interval certificate — the
   shared substrate again) is a SMALL named brick; off-box, the
   concave-hull de-rate applies automatically (ceiling loosens,
   lemma survives).
 - Abstract EOS: the skeleton (E4, perspective, Jensen, storage) is
   EOS-general; the sonic-branch closed forms + carrier are the
   declared perfect-gas instance — schema residue, S-XCONV pattern.
 - E3 subsonic-plume caveat: exhaust surfaces crossing subsonic jet
   regions are NOT covered (move the surface or de-rate) — the
   margin is load-bearing (GBE-L1 fails without it: the sup is
   infinite; this is a NECESSARY-hypothesis exhibit, ledger-grade).
 - E1 trace bookkeeping: Dafermos-class, shared pricing with
   C-XBVP(b).
 - Attainability (lower rungs of the bracket) in the unsteady
   setting: NOT touched — the wall is one-sided by design.
