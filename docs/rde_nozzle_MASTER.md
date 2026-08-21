# MASTER REFERENCE — The cycle-averaged variational nozzle problem for RDEs
# Idea, formalization, proofs, global optimality, implementation (M0)

Status: MASTER DOCUMENT OF RECORD (2026-07-16). Self-contained,
thesis-grade reference for all program phases. In case of conflict with
any other document, THIS + the D-deliverables win over the historical
notes. Depth per topic lives in the deliverables (map in Part VII);
the proofs of the core theorems are IN FULL here.

Rigor legend: THEOREM (proof here, verified line-by-line this session);
THEOREM* (proof within a declared model closure); SCHEMA (correct formal
structure, rigor gap named); CONJECTURE (precise + falsifier);
PRACTICE (no theorem, instrumented).
[Legend extension of record, S14 (PAN-S14 F-CLASSES, dated
supersession per the S9 convention): THEOREM* = proof complete modulo
the conditional-entry IDs in the registry `inherits` field — declared
model closures (C-HT4/C-IGMIX/C-O33), numeric residuals, or the named
ANALYTIC conditionals (C-D25U/C-MAJDA); the closure-conditional vs
analysis-conditional distinction lives in the L4 ledger
(docs/rde_nozzle_conditionals.md). "THEOREM* at statement level" is
sanctioned usage when the remaining analysis is itself a registered
conditional (instance: S-P4F with C-P4RZ).]

==============================================================================
PART I — THE IDEA (and why it is new)

A rotating detonation engine feeds its nozzle with a PERIODIC family of
states: at each azimuthal station the products' state (P, T, M, flow
angle, composition) sweeps a cycle as the wave passes. The nozzle is ONE
and FIXED. Classical nozzle optimization (Rao 1958; Guderley-Armitage;
the Kraiko school) designs for ONE steady inflow state; RDE practice
either averages the flow first and designs classically, or sweeps
parameters with CFD. The idea: define the total thrust functional as the
integral of per-state (per-phase) thrust functionals over the cycle
measure,

    J[Sigma] = Int_Xi F[Sigma; s(xi)] dmu(xi),

and derive Rao-type stationarity for the SHARED contour: per-phase
classical conditions coupled by mu-averaged wall and endpoint conditions.
Three structural discoveries organize everything:
 (1) STEADIFICATION IS EXACT for a single rotating mode (T0): the
     averaged functional is a genuine steady 3-D thrust functional in
     the wave frame — indeed the instantaneous thrust is CONSTANT.
 (2) A COLLAPSE DICHOTOMY: for fixed full-flowing walls under pressure-
     scaling similarity the averaged problem collapses EXACTLY to the
     classical design at the mean pressure (T3) — explaining why the
     field's "design on the averaged flow" works; for free boundaries
     the ideal plug is optimal at the PEAK pressure (T4); the first
     genuinely averaged problems are the truncated plug and the
     shroud/plug duty split.
 (3) THE MEASURE SELECTS THE TOPOLOGY (OP-11): in the configuration-free
     formulation the optimal nozzle TYPE (bell / plug / shrouded) is an
     output — a phase diagram over (constraints) x (spread of mu), whose
     limits are theorems (T3, T4, the geometry-free bound).
Novelty: verified query-bounded by three independent adversarial passes
(six-strand web survey; 16-agent red-teamed panel; page-level read of
the classical corpus). Every component is prior art in isolation; the
constructive certificate-bearing composition is unpublished. Residual
due diligence: Kraiko-1979/PMM human pass (gate G5) before submission.

==============================================================================
PART II — FORMAL DEFINITIONS

[D-DOM] D2.1 (Domain and constraint). Reactive compressible Euler (viscous
closure = declared model layer) in Omega(S) = E \ S, E an envelope
cylinder downstream of the annulus, S the SOLID SET (design variable)
with attachment at the chamber lip(s) and uniform cone condition.
Configurations (bell / plug / shrouded / E-D / ...) are the topology
sectors of S — outputs, not inputs. Working class A: spline manifolds
in uniform C^{1,1} per sector.

[D-JEX] D2.2 (Exact objective). J_exact[S] = lim_{T->inf} (1/T) Int_0^T F_S(t)dt,
F_S(t) = Int_S [rho u_x (u.n) + (p - Pa) n_x] dA on any enclosing
axisymmetric control surface; requires an attractor with invariant
measure (statistical stationarity — the weakest standing hypothesis)
and a solution concept (D2.5). Pa constant.
[S14 additions (PAN-S14 addendum, 2026-08-04; ME-1 + a-Jexact-fallback,
both team/arbiter-confirmed): (1) FALLBACK TARGET (definition): if no
invariant measure exists, the declared objects are J_exact^-/J_exact^+
[S] := liminf/limsup_{T->inf} (1/T) Int_0^T F_S(t)dt (always defined);
"only bounds ship" means certified brackets of [J_exact^-, J_exact^+],
collapsing to J_exact under the standing hypothesis. (2) SCOPE
DISCHARGE: within the declared periodic scope the hypothesis
discharges exactly (D3 remark (1), "no Birkhoff limits"); outside it
the OBSERVABLE failure channel is running-average non-convergence /
realization dependence — not the non-existence of an invariant
measure, which is non-exhibitable (Krylov-Bogolyubov where "attractor"
is well-posed). The D-JEX falsifier is re-pointed accordingly.
(3) WORDING NOTE, dated 2026-08-05 (PAN-S14 §8 residue PP-3,
second-lens verified): 'attractor with invariant measure' =>
realized-orbit stationarity additionally presumes the invariant
measure is the PHYSICAL (SRB-type) one for the observed data — a
DECLARED hypothesis, not a theorem; 'weakest standing hypothesis'
reads 'weakest DECLARED hypothesis', operationally subsumed by the
running-average monitor of (2).
(4) UPPER WALL, dated 2026-08-06 (S16, [S-GBE]): the fallback targets
now carry a certified geometry-free upper wall — J_exact^+ <=
F_env(mean interface fluxes) under bounded storage + axially-sonic
exhaust + admissibility (docs/rde_nozzle_GB_ergodic.md): the "only
bounds ship" clause has its bound.]

[D-MU] D2.3 (Operating measure and averaged objective). mu = pushforward of
normalized cycle time under t -> xi; averaged (rung-2) objective
J[Sigma] = Int F[Sigma; s(xi)] dmu(xi), with F the steady per-state
thrust (wall form or Rao control-surface form; equal by the momentum
theorem in the S1 class).
[Scope note, dated 2026-08-05 (PAN-S14 §8 residue ME-2, second-lens
verified): mu and the rung-2 integrand are declared WITHIN the
standing pure-periodic single-mode scope (fixed wave count n;
monitor = T0 flatness, VI.4bis): a phase containing a MODE
TRANSITION (n changes) has no steady per-state F and is OUTSIDE
this definition — it violates H-A1 (D1 §9) and is routed to the
robust layer (VI.4bis(v), A6/PB-5), never silently averaged.]

[D-CONTRACT] D2.4 (Design interface Gamma_d). A fixed axisymmetric surface
downstream of all heat release carrying the data family s(xi); the
CONTRACT is (Gamma_d, data class, validity): R1 causal separation;
R2 well-posed data (full state only on axially supersonic patches —
see L4; subsonic patches: incoming invariants + impedance closure or
choking closure, decision tree in D1 §4.3bis); R3 measurability.
Idealization ladder: I0 coupled bilevel / I1 wave-frame steady field /
I2 per-phase meridional profiles / I3 sonic family (P0,T0)(xi) /
I4 single mean state.
[L4-DEFAULT OF RECORD, dated 2026-08-06 (S16 [RIGOR/B], ledger pass 2
[PAP-D9HL] §4 items 1-2): the certified interface DEFAULT is the L4
class — every patch of Gamma_d axially supersonic with margin. On
the default: mdot-independence is EXACT ([T-TH0] L4 note, no choking
assumption) and mean upstream influence is EXCLUDED BY THEOREM
([T-NSW]) — the former hypotheses H2/H-I2 are DISCHARGED there.
Subsonic patches remain admissible as a DECLARED CASE-CLASS (D1
§4.3bis options O1-O4) whose closures carry H2/H-I2 as class
assumptions with the existing monitors (choking margin, R2
characteristic-direction audit) and the documented Verdict
downgrades. This names the class the certified apparatus already
lives on (the u_x - c >= delta margin was the standing certificate
AS WRITTEN — planar-only; the certificate of record is now the
L4-CERT split + normal form below); no theorem's scope changes.]
[L4-CERT — SPLIT CERTIFICATE + NORMAL (CURVED-Gamma_d) FORM OF
RECORD (landed 2026-08-19, S-FOUNDATIONS-C Blocco 2; sources:
phaseD_meanswirl_formalization.md §7 item 6 / D.4 curved clause
(CONFIRMED THEOREM) + VERDICT_contract_and_L4R1.md B.4 condition C-1
(NG-8 retro-propagation, BLOCKING); provenance: VERDICT_r2pass §3 +
VERDICT_escalation §4):
 (i) NORMAL FORM (planar-only repair, REQUIRED): the margin
 certificate of record is the MERIDIONAL-NORMAL form
     m_n := u . n_m - c >= delta   (criterion M_n > 1),
 with n_m the meridional unit normal field of Gamma_d —
 frame-invariant (same mechanism as [T-NSW]), reducing EXACTLY to
 the historical axial form m_x = u_x - c when Gamma_d is planar.
 The bare "u_x - c" form is PLANAR-ONLY: on a curved/tilted Gamma_d
 it can license an ill-posed march (tilted-element counterexample =
 the audit-wiring rejector, D.4 r3). Every "u_x - c" occurrence
 elsewhere in this document reads through this block (one-line
 annotations at the sites).
 (ii) SPLIT CERTIFICATE (C-1 retro-propagation): the L4-DEFAULT
 certificate is TWO distinct certified objects, never silently
 interchangeable —
   (M-a)  NORMAL-ON-SURFACE: m_n >= delta on every patch of Gamma_d
          (the interface-admission certificate = form (i));
   (M-a') AXIAL-ON-SEGMENT + BOX: u_x - c >= delta along the marched
          segment/volume PLUS certified box membership of the states
          (the volume certificate the causality theorems consume).
 Every Theorem-2/3 consumption of the L4=>R1 record cites (M-a')
 EXPLICITLY; (M-a) alone never licenses them. The normal-direction
 form (i) is the repair of BOTH halves on curved patches.
 (iii) R1 VALIDITY WINDOW (hypothesis-legitimacy audit, R1-CAUSAL
 verdict CERTIFIED): R1 is of record CONDIZIONATA on the window
 W1-W4 — W1 every patch axially supersonic with MEASURED margin;
 W2 the design vector strictly downstream of the CERTIFIED interface
 as GEOMETRY-INVARIANCE (throat-area invariance is necessary, NOT
 sufficient — Liu 2022 B-vs-C); W3 operating-point exogeneity;
 W4 subsonic patches routed to the declared closure (O1-O4).
 Monitors A1-A6: SPECIFIED, not armed (no run artifacts exist;
 every "monitored" claim reads monitor-SPECIFIED).
 (iv) NO-COFLOW DECLARATION: external coflow is explicitly OUT OF
 SCOPE for this contract; Pa constant per D-DOM/D-JEX.]
[H3-cl (D-CONTRACT vocabulary addition, S-GAUNTLET 2026-08-11):
"certified phase-independent closure patch pattern" — the named
sub-hypothesis of the O1-O4 subsonic case-class under which
collapse-in-form survives on the subsonic sector (see T-T3-MAP
clause (d)); expected to FAIL on migrating patch patterns (K-P
Fig. 6); its audit is CARRIER-D D2 of the advisory record.]

[D-S1] D2.5 (Solution classes). S1: piecewise-smooth MOC-regular (finitely
many transversal fronts, no wall-shock formation): classically
well-posed (Li Ta-tsien semi-global framework), membership checkable a
posteriori (Sternin/Rao-Beck boundary function). CANONICITY (corrected,
precision pass 2026-07-16): in SHOCK-FREE (locally Lipschitz) regions
and regimes, weak-strong uniqueness (Dafermos relative entropy;
measure-valued version Brenier-De Lellis-Székelyhidi, Comm. Math.
Phys. 305:351-361 (2011), doi:10.1007/s00220-011-1267-0 — VERIFIED)
makes the classical solution THE solution of every admissible concept.
ACROSS transversal shocks the strong comparison solution is not
Lipschitz and the general multi-D weak-strong property is OPEN;
partial support: 1-D uniqueness of BV/piecewise-smooth solutions
(Bressan school) and shift/a-contraction shock stability (Vasseur-
Krupa line, essentially 1-D). S1 canonicity WITH shocks is therefore a
DECLARED conditional (backed by Majda stability of the fitted fronts [C-MAJDA]),
not a theorem — ledger-grade honesty, consistent with the panel's
refutation of relative-entropy certificates for shocked orbits.
[BVP-NATIVE UPGRADE, dated 2026-08-05 (S15 [RIGOR/A], [T-XWS]
docs/rde_nozzle_cauchy_bvp_transfer.md, carrier X-XBVP): the
shock-free weak-strong citation above is TIME-formulation (its Cauchy
datum = the whole field at t = 0, which presupposes the solution);
the transfer to the steady BVP is now WRITTEN — relative entropy in
x-as-time with the pair (-rho u g(S), -rho v g(S)): sonic bijection
[T-XSON] (THEOREM, abstract EOS), slip-wall relative-entropy flux
annihilation [T-XWALL] (THEOREM, abstract EOS, every g: the slip flux
perturbation is isentropic at constant mass flux), convexity from the
AXIAL margin [S-XCONV] (SCHEMA, instance-certified; sonic line =
exact definiteness boundary), assembling to weak-strong uniqueness on
the BVP [T-XWS] (THEOREM* inheriting [C-XBVP](a,b), ledger §1bis;
retro-annotation 2026-08-20: leg (a) also admits the sufficient
hull/segment form (a') of the G8 grant — own claims row
C-XBVP-aprime, falsifiers stop_proof §13 (f1)-(f5); line landed per
confirm catch CR-W3-R10-1, closing the doc1-landing claim of C2):
with a C^1 margin solution present, shocked alternatives on the same
inflow data are excluded BY THEOREM in the class. Canonicity across
fronts stays with C-MAJDA, now cleanly separated.]
[FRONT-CHAIN COMPLETION, dated 2026-08-06 (S16 [RIGOR/A],
[S-D25U-U34] docs/rde_nozzle_D25U_U3U4.md, carrier X-U3BD): the
C-D25U component -a estimate chain (U1 smooth + U2 wall + U3 front +
U4 composition) is now WRITTEN at whole-class level with the
Lipschitz constant explicit in the five-constant certificate; and
C-MAJDA is SHARPENED in-class to a single scalar condition (U3-H1:
the 1-D Lopatinskii-Schur scalar of the bordered front solve,
nonvanishing on the compact certified front set — instance-certified
s_L = 1.8685, uniformity by compactness once pointwise). Declared
inventory: same-front-topology stratum (cross-topology = census/RK-G
layer), wall-attachment reading (front count DERIVED from the
entropy budget), origination clause, genuine nonlinearity for the
entropy floor. Shift-C^1 of the map (-c/U5) untouched.]
[A-CONTRACTION ROUTE, dated 2026-08-06 (S16 T2, [S-ACFR] docs/
rde_nozzle_acontraction_attack.md, probe X-ACFR): the "shift/
a-contraction (Vasseur-Krupa line)" partial support named above is
now TRANSPLANTED to the x-as-time BVP frame as a named route:
extremal fronts only (structural), walls free by T-XWALL, shift =
the fitted-front dof, entropy family -rho u g(S) on the certified
convexity box (CONFINEMENT CLAUSE load-bearing). The front
obstruction reduces to a balance-set condition, INSTANCE-FEASIBLE at
the certified oracle with weight window r = a_-/a_+ ~ [3.2, 47]
(probe, not certificate; reversed front infeasible for every r —
the condition discriminates). Route ADOPTED-AS-NAMED, completion
gated on bricks B1-B3 (interval certification over K_delta;
assembly; g-scan). No C-MAJDA discharge claimed.] S2:
entropy weak — non-unique in multi-D (convex integration), never used
as a constraint. S3: statistical — roof definition only.

[D-P] D2.6 (THE PROBLEM OF RECORD (P) — canonical fusion of Part II + Part IV).
GIVEN: envelope E (axisymmetric, L_E, R_E), attachment set Λ, constant
Pa > 0; interface contract (Gamma_d, D, mu) with the stage-A admission
audits passed (characteristic completeness on axially supersonic
patches per Lemma 4; Crocco compatibility; per-phase spacelikeness
margin (m_n form on curved Gamma_d — D2.4 L4-CERT (i) / VI.1);
declared closure O1/O2/O3 on subsonic patches); constraint
vector c = (L, eps_max, L_p, curvature/angle bounds, symmetry class).
[PROXY NOTE, dated 2026-08-05 (PAN-S14 §8 residue PP-4, second-lens
verified): industrial heat-load and mass constraints enter (P) at
rung 2 ONLY through these geometric c-slots as declared PROXIES
(L/L_p/eps_max bound wetted length and size); no flux-level thermal
or mass model is a c-slot today — declared upgrade path: a dedicated
c-slot with its own multiplier, same pattern as the side-load CVaR
disposition below.]
[SIDE-LOAD DISPOSITION, dated 2026-08-05 (S15, [T-SLRW]): the rotating
side load is a DECLARED SECONDARY OUTPUT, not a c-slot — inside the
certified n >= 2 pure-periodic scope it is zero BY THEOREM (a slot
would carry a structurally-zero multiplier), and the m = 1 wall trace
lives in the D2 azimuthal residual channel that rung-2 states cannot
evaluate; data-level impurity metric rides the T0 flatness monitor's
m = 1 line; declared upgrade path to a CVaR c-slot at the A6 robust
layer (mode transitions) — full grounds in
docs/rde_nozzle_side_load.md §4.]
PER-PHASE STATE CONSTRAINT (addendum 2026-07-21, S12, [D-GSEP]):
the constraint set also carries the separation-margin state
constraint g_sep(S; s(xi)) <= 0 for mu-a.e. xi (criterion class R2,
declared empirical closure; runtime detector = the S1 boundary-
function monitor): certified optima keep EVERY phase attached, the
active-set multiplier is the marginal value of the attachment
margin, and the temporal dual-bell question (N1) becomes a decidable
active-set question at rung 2; deliberately separated designs exit
the certified class (separation reopens the subsonic feedback
channel and carries its own non-rotating dynamics — out of the
single-mode scope by physics, not only by declaration).
[Alignment note, dated 2026-08-05 (PAN-S14 §8 residue ME-4,
second-lens verified): the reading of record is mu-a.e. — 'every
phase' means every xi up to a mu-null set; the readings coincide on
the atomic/empirical measures and quadrature nodes actually audited
(mu-hypotheses of Lemma 2 / T-O2, ME-3), and the D-GSEP falsifier's
'any phase' is read on supp(mu) accordingly.]
ADMISSIBLE SET: A_gen(c) = {S ⊂ E compact solid: uniform cone condition
(h0, omega); attachment on Λ; g_i(S) <= c_i}, with its FINITE topology-
sector decomposition (configurations = outputs) and working spline
class A_h per sector.
[ATTACHMENT-QUANTIFIER PIN PENDING, dated 2026-08-05 (D8 §8 residue
s1, second lens): the clause 'attachment on Λ' (and D2.1's
'attachment at the chamber lip(s)') does not fix the quantifier over
connected components — permissive (only lip-touching components
constrained; detached D-family admissible) vs strict (every component
anchored) is undecidable from the present text: census advisory open
point O1, sibling carrier question O9
(validation/PANEL_topology_census_2026-07-22.md §7, ADVISORY). USER
PIN + census-lemma session required (PROGRESS NEXT: "decisioni A_gen
(utente)"); until pinned, no sector-count or D-family claim may
silently assume a reading.]
[PINS SINCE DECIDED — note added 2026-08-06: the census thread closed
with ALL pins decided 2026-08-02 (advisory §7pin + memory bridge
topology-census-pins): CEN-O1 = PERMISSIVE (bare annulus in;
detached members via anchor classes/strut bands/tournament filter).
The D2.1/D2.6 amendments the pins imply are QUEUED to the
census-lemma rigor session (after brick 2, census sequencing) — this
note is a state pointer, not the amendment.]
[SECTOR-FINITENESS STATUS, dated 2026-08-05 (D8 §8 residue s6,
second lens): "FINITE" here carries NO declared rigor class at this
site of record. Current grounds: problem book §5 sector decomposition
(SCHEMA) + the two-clause counting theorem of the census advisory
(THEOREM-sketch, conditional on O1/O2/O3/O9;
validation/PANEL_topology_census_2026-07-22.md §3 — ADVISORY, not of
record). Class label + proof owed to the census-lemma session
(global-maximum dossier Card 4; PROGRESS NEXT).]
[SINCE 2026-08-06: the counting theorem's pin-conditionals are now
DECIDED (census §7pin, 2026-08-02): O1 permissive, O10 NONBLOCK+,
O11 lip circles; the old O2/O9 are DISSOLVED by the Omega-side
Chenais cone-carrier pin. Headline of the advisory: the classical
taxonomy collapses to ONE clopen sector S0 + the detached family
D(m,n); P(h)/BR empty. Still ADVISORY until the census-lemma session
promotes it (ratification = user lock).]
STATE (mu-a.e. xi): the unique S1 solution U_xi of steady Euler in
E \ S with data s(xi), slip walls, supersonic outflow; S1 membership
certified a posteriori (boundary-function margin >= delta_S1 > 0
uniformly in xi); canonicity per D2.5 (exact shock-free, declared
conditional across fronts).
OBJECTIVE: J[S] = Int_Xi F[S; s(xi)] dmu(xi), legitimacy chain
Theorem 0 -> T0 -> P4.
[LAND-C4-LA1] OBJECTIVE DOMAIN [OBJ-DOM adjudicated, Phase D
2026-08-20] (landed per VERDICT_escalation_c4 LA-1(i) — escalation
E-2 CLOSED DRY at round 3; the §4 text's PROPOSED status lifted by
that verdict; text verbatim from phaseD_minor_objdom.md :461-470; the
interim fix-B scoping regime — value + gradient + Pa statements
scoped, all three axes — lands WITH it): the functional of
record at F2 entry is the panel-inclusive J_A (domain [0,theta_B]
+ contour; fix-A). Until [OBJ-DOM-IMPL] lands, the executed
carrier computes the coded J on [theta_1, theta_B] + contour:
value, gradient, and Pa-drop statements about the carrier are
scoped to that domain, and the Pa-drop claim holds under the
vacuum objective only. Discharge = analytic throat-panel A/B
(F2 duty [OBJ-DOM-AB]); tilt of record 5.36e3 J-units/rad vs
acceptance 9.3 (advisory §1.3). [Adjudicated statement labels per
VERDICT_escalation_c4 §5.2: OBJDOM-1 THEOREM as restated (discrete
identity + truncation-order ladder: generic O(th1^3) with coefficient
−(pi/6)·rtd·p'(0)·yt; O(th1^6) ⇔ p'(0)=0 AND p'''(0)=0; O(th1^5)
branch with coefficient (pi/10)·rtd·(p'''(0)/6)·yt); OBJDOM-2
(absorption branch dead, >= 96x) THEOREM*; OBJDOM-3 (Pa-anchor)
THEOREM; OBJDOM-4 = the DECISION OF RECORD (fix-A objective-of-record
at F2 entry; fix-B scoping interim); OBJDOM-5 ((H6') composition +
re-pinned ship-gate) SCHEMA, proof obligation discharged in the
delta-carrier escalation; falsifiers F-1 (three-branch) / F-2 (both
paths) pinned; duties [OBJ-DOM-IMPL]/[OBJ-DOM-AB]/[OBJ-DOM-REBASE]
(F2). Carrier of record: phaseD_minor_objdom.md through [ESC-r3-*].]
PROBLEM (P): find the PAIR (S*, delta) such that
 (i)   S* ∈ argmax_{A_h(c)} J (existence; P7 = function-class target
       with monitored failure boundary);
 (ii)  S* satisfies the averaged system T7: per-phase adjoint
       stationarity — CLOSED-FORM (Rao/Kraiko) conditions in the
       IRROTATIONAL-HOMENTROPIC per-phase subclass; FIELD-LEVEL
       adjoint conditions otherwise (rotational/stratified data:
       the closed form is oracle/initializer only, VI.4bis(iv);
       Hoffman four-field route — scope qualifier added S21 per
       audit C1: the T-A3 derivation layer is scoped strictly
       narrower than S1) + mu-averaged wall condition +
       WEIGHTED transversality (**') + active-constraint
       complementarity with multipliers = marginal values;
 (iii) reduced Hessian ⪯ 0 on the active tangent cone;
 (iv)  GLOBALITY, certified: a declared mechanism M1-M5 delivering
       J[S*] >= sup_{A_gen(c)} J - delta with delta COMPUTED
       (delta = B - J[S*], B = min of the bound ladder: int-max,
       sonic-capped J_ideal, B_EK), and delta = 0 PROVEN in the
       structured classes (M1 duality-gap zero: T4, numerically
       attained on the supercritical rows; M2 pointwise T3 transfer —
       valid for EVERY S in the sector, not only stationary ones;
       M3 unimodality: the 1-DOF theorems);
 (v)   declared bars: |J_exact - J[S*]| <= St|J1| + D2 residual + DWR.
[BAR-CLASS NOTE, dated 2026-08-05 (PAN-S14 §8 residue PP-5,
second-lens verified): the (v) bars are ESTIMATED/ASYMPTOTIC
indicators — St|J1| is the first-order [J-CT1] term (it does not by
itself bound the remainder, T3QS §3 B3) and DWR is an estimate —
NOT certified bounds; certified brackets ship only via the D2.2
fallback targets [J_exact^-, J_exact^+].]
"Search for the global optimum of the defined problem" = compute
(S*, delta) with the least available delta; "global optimum PROVEN"
<=> delta = 0.
MAXIMALITY (why this is the strongest truthful form): (a) no
admissible-set-free version exists (vacuum theorem: sup unattained —
the Pa -> 0 limiting instance, outside (P)'s Pa > 0 GIVEN; at Pa > 0
the class is needed for existence itself: uniform cone condition +
envelope compactness, the P7/Chenais route of Part IV [anchor
corrected S14, PAN-S14 addendum, arbiter-confirmed]);
(b) no solution-concept-free version exists (multi-D non-uniqueness);
(c) unconditional global optimality on nonconvex infinite-dimensional
shape sets with PDE constraints exists for NO ONE (J non-concave —
deflation can exhibit multiple stationary contours; no convexification
known; G13/G17 verified open) — the certified-(S*, delta) form is
maximal w.r.t. the provable state of the art, achieves delta = 0
exactly where structure exists (T3/T4/unimodal), and is designed to
absorb future progress on the named residues (R5-R8, G12) without
changing form.

==============================================================================
PART III — THEOREMS WITH PROOFS

------------------------------------------------------------------------------
[T-TH0] THEOREM 0 (the definition chain of RDE thrust — why the phase integral
is legitimate). THEOREM (exact links) + one declared choice + one
priced approximation.
DEFINITION (mechanical thrust): F_wall(t) = Int_W (p - Pa) n_x dA over
the wetted surfaces W (+ declared viscous layer); legitimate gauge
reference since constant Pa integrates to zero over a closed surface.
This — the force on the structure — is the definition; everything else
must be derived.
IDENTITY (unsteady momentum theorem, fixed control volume V bounded by
W and a fixed control surface S):
    F_wall(t) = Int_S [rho u_x (u.n) + (p - Pa) n_x] dA
                + d/dt Int_V rho u_x dV.
Instantaneously, wall force and flux DIFFER by the axial-momentum
STORAGE term — not small in an RDE at kHz.
CLAIM (mean equality — exact). For T-periodic flow with bounded
contained momentum: <F_wall>_T = <F_S>_T for EVERY fixed S.
PROOF: the storage term is the time derivative of a bounded periodic
function; its period integral is Q(T) - Q(0) = 0 exactly. Average the
identity. S-independence: apply between any two surfaces. QED.
(Quasi-periodic/chaotic: Birkhoff averaging, Q(T)/T -> 0 under bounded
momentum — same conclusion in the limit sense.)
STRENGTHENING (single rotating mode): the wall pressure on an
axisymmetric wall is p(x, r_w, theta - W t), whose theta-integral is
shift-invariant: F_wall(t) itself is CONSTANT and the storage term is
identically zero — in the nominal regime mechanical thrust ≡ flux ≡
steady wave-frame value with no averaging needed (consistent with, and
feeding, Theorem 3).
DECLARED CHOICE: the mission objective is the MEAN <F_wall> by scale
separation (kHz cycle vs vehicle dynamics: the vehicle responds to
impulse); fluctuations leave the OBJECTIVE and enter CONSTRAINTS
(side loads / fatigue — CVaR tail objectives of the robust layer).
Isp relation: Proposition 1 (O1).
THE ONLY APPROXIMATION in the chain: representing the exact mean as a
sum of STEADY per-phase thrusts,
    <F_wall> = Int_Xi F_steady[Sigma; s(xi)] dmu(xi) + O(St),
is the quasi-steady (rung-2) step — exact as St -> 0, priced by the P4
corrector, with Theorem 3 as the nonperturbative backstop. All
approximate content of the formulation lives in this one link (ledger
row D1).
DO NOT CONFLATE the two "unsteady" objects: (1) the STORAGE term
dQ/dt = d/dt Int_V rho u_x dV in the exact thrust identity — pure
bookkeeping (momentum borrowed and returned each cycle), instantly
large at kHz, EXACTLY zero in the mean by periodicity, identically zero
for a single rotating mode (volume integral of a function of
theta - W t is shift-invariant); it introduces NO approximation.
(2) the O(St) QUASI-STEADY error — a genuine modeling error living in
the per-phase steady factorization of the (exact) mean flux, NOT in the
momentum balance. "Storage averages to zero" does NOT imply the
quasi-steady step is exact, and "kHz unsteadiness" does NOT imply the
mean thrust needs unsteady corrections at the balance level.
T3-QS SWEEP-PROTECTION REMARK (2026-07-21, S12, [T-T3QS]; carrier
X-T3QS, suite group (xvi); full statement docs/rde_nozzle_T3QS.md):
within the P4 first-order framework, on a T3 RAY family (Pc-only
cycles; EOS-general) the first-order term of the quasi-steady error
VANISHES on the smooth part of the cycle — flux Jacobians and the
thrust-adjoint source are invariant along the conservative ray, so
the sweep acts as a pure phase shift and the mean is unchanged; the
entire first-order correction concentrates at the wave-passage jump
(the physics the fitted inherited sheet represents), and off-ray
cycles contribute a computable AREA (hysteresis) term. The collapse
class is thus SECOND-ORDER protected ON SMOOTH RAY CYCLES; on the
canonical blowdown sawtooth (T-O2) the first-order residue
<psi_hat, Z>[k]_jump is jump-localized, and its absorption by the
fitted inherited sheet is the pre-registered O5 prediction P-ii
(conjectural until measured) [status restatement S14, PAN-S14
F-T3QSHEAD] — the quantitative reason the
field's quasi-steady practice outperforms naive St estimates. This
remark does not weaken the paragraph above: the storage bookkeeping
is untouched; T3-QS refines the FLUX-factorization error only.

------------------------------------------------------------------------------
[T-O1] PROPOSITION 1 (O1 — objective equivalence at frozen choked feed). THEOREM.
Hypotheses: (i) the cycle family, period and A_t are Sigma-independent
(frozen family H-F1); (ii) mdot(t) = Pc(t) A_t / c*(t) (choked feed H2).
Claim: argmax_Sigma Isp_cycle = argmax_Sigma J, and the Isp numerator
equals Int F dt identically.
PROOF. mdot c* = Pc A_t for ANY c*(t) law, hence
Int mdot CF c* dt = Int Pc A_t · F/(Pc A_t) dt = Int F dt. The
denominator g0 Int mdot dt is Sigma-independent by (i)+(ii). QED.
Failure channels: bilevel coupling breaks (i) — then thrust-max and
Isp-max are DIFFERENT problems (N-O1±); unchoked tails break (ii);
axially subsonic interface patches can make mdot Sigma-dependent.
Note: with a fully axially supersonic data interface (L4), (i) and the
mdot-independence hold EXACTLY without invoking upstream choking.

------------------------------------------------------------------------------
[T-O2] LEMMA 2 (O2 — log-uniform measure). THEOREM.
For the exponential blowdown Pc(xi) = P_CJ · PR^(-xi), xi ~ U[0,1):
xi = -ln(Pc/P_CJ)/ln PR, so dmu_P = dPc/(Pc ln PR) on [P_CJ/PR, P_CJ]:
the engine's canonical operating measure is LOG-UNIFORM in pressure.
QED. (Any measured cycle simply replaces mu_P; the theory is
measure-agnostic WITHIN the declared mu-hypotheses [scope note S14,
PAN-S14 addendum ME-3]: mu a probability measure; the mu-a.e. audits;
switch phases mu-NULL (T7 standing hypothesis) — the last must be
RE-VERIFIED for every imported measure, trivially but obligatorily
for ATOMIC/empirical measures, which can charge a switch phase; for
atomic mu the cycle quadrature becomes the exact weighted sum, not
Gauss panels.)

------------------------------------------------------------------------------
[T-T0] THEOREM 3 (T0 — wave-frame exactness, strengthened). THEOREM.
Hypotheses: rotating-pattern flow q(x,r,theta,t) = q~(x,r,theta - W t)
(W := Omega_w; piecewise-smooth, transversal fronts); S fixed
axisymmetric; Pa constant.
Claims:
 (i)  F_S(t) is CONSTANT in time (not merely mean-equal): the single-
      mode RDE has steady thrust through every axisymmetric surface.
 (ii) F_S equals the identical integral of the wave-frame steady fields
      with relative velocity w = u - W e_x x r: on axisymmetric S,
      w_x = u_x and w.n = u.n.
 (iii) The rotating-frame steady momentum balance closes with zero
      axial frame forces.
PROOF. (i) At fixed (x,r) the integrand is g(theta - W t); its
theta-integral over [0,2pi) is shift-invariant, so each annular strip
contributes a t-independent amount. (ii) The rotation adds only an
azimuthal velocity component W r e_theta; axisymmetric S has n_theta=0,
so (W e_x x r).n = 0 and w.n = u.n; trivially w_x = u_x. (iii) Coriolis
-2 W e_x x w is orthogonal to e_x; centrifugal W^2 r e_r is radial. QED.
Consequences: J_exact = steady 3-D wave-frame shape functional with W
an EIGENVALUE-like unknown (freezing formulation + phase condition);
thrust-trace flatness = executable mode-purity diagnostic (N-T0').
[S-T0P] PROPAGATION LEMMA (SCHEMA — written of record 2026-08-13,
F-SERVICE, from REFUTE_A / ASSESSMENT §3.1; the R4 duty "lemma to
write"). T-T0 HYPOTHESIZES the rotating pattern on the field. The
missing stage-1 statement — "purely periodic rotating data on the
interface + axisymmetric domain, wall and ambient BC elsewhere =>
the certified solution is a steady co-rotating pattern" — is
PROVABLE on the L4 class and is registered here at SCHEMA with the
proof route NAMED: equivariance of the steady Euler operator under
the helical symmetry group + uniqueness of the certified S1
solution (the solution map commutes with the group action, so the
rotated solution solves the rotated problem = the same problem, and
uniqueness forces the pattern), with L4's axially supersonic margin
giving the finite domain of dependence that propagates the symmetry
from the interface data along the march. HONEST TWO-STAGE CLAIM OF
RECORD (REFUTE_A, replaces any "the correct object" tout court):
STAGE 1 (exact): the symmetry quotient justifies the steady 3-D
adjoint in the wave frame — for an autonomous rotating wave the
naive periodic-BVP adjoint as printed is DEGENERATE (the trivial
Floquet multiplier along the group orbit makes I - monodromy
singular), so the per-phase/wave-frame formulation is the CORRECT
symmetry-reduced object in the pinned class, not a poor surrogate
of the "true" periodic adjoint; the general machinery applied
naively would itself be ill-posed without the same quotient.
STAGE 2 (declared approximation): the 2-D per-phase marches discard
the theta-coupling — rung 2, "the only approximation in the chain"
(M0's own wording). The claim of record is always: per-phase =
exact quotient + declared rung 2. Honest boundaries, separately
priced: (i) the pin (pure rotating wave, T0-flatness monitor) is a
MODEL HYPOTHESIS with no certified hardware provenance (R20);
(ii) the O(St)/dimensional-reduction step is DISTINCT from
time-coupling and is where the Harroun threat lives (R22 decides);
(iii) out of pin the named route is Zahr-Persson / Rubino
(+ LSS/NILSS for the chaotic regime) — registered alternative.
Falsifier: an L4-certified pure-periodic-data instance whose
certified solution is NOT a steady co-rotating pattern (kills
stage 1); owner of the full proof write-up: F2 theory window.
[T-T0P PARTIAL LANDING OF RECORD (2026-08-19, S-FOUNDATIONS-C
Blocco 2; proof of record = validation/sfoundations_raws_2026-08-13/
phaseD/phaseD_stop_proof.md, revision 8; labels per
VERDICT_phaseD_proofs1 §3.1; provenance: VERDICT_r2pass §3 +
VERDICT_escalation §4). LANDED:
 (1) [T-T0P-E], the EQUIVARIANCE HALF — THEOREM. Function-space
 complete conditional assembly at ABSTRACT EOS; the hypothesis
 (S1-anchored uniqueness of the certified solution) is stated
 IN-STATEMENT, never assumed silently. Falsifier: the three-target
 battery (t1) kills [L-STD] (an invariant field not of the standard
 form), (t2) kills the theorem (a non-pattern S1 element in a class
 VERIFIED to have the uniqueness property — premise checked, not
 assumed), (t3) kills [L-EQV3] — genuine rejection power.
 (2) Supporting lemma family, all THEOREM: [L-EQV1]/[L-EQV2]/
 [L-EQV3]/[L-INV] (verbatim computations, full group);
 [L-STD] (countable-dense closure + no-topology pointwise argument,
 EOS-free); [L-SPACE] (re-scoped — determinacy in Remark only);
 [L-COMPAT]/[L-XSON3]/[L-XREC]/[L-XWALL3]/[L-XC3D] (pen proofs
 complete at abstract EOS; the [X-T0P] symbolic battery is the owed
 EXECUTABLE rejector layer, owner F2 — labels hold as
 complete-proof-here with the carrier duty named).
 (3) [L-INC] (S1 elements are legitimate H7' competitors):
 THEOREM on stratum (A) / SCHEMA-inherited on stratum (B) (rides
 G2/G9; no new gap minted).
 (4) [P-HB1] THEOREM; [P-HB2] THEOREM (linearity-of-homomorphism
 clause in place; the D(a,b) rejector has genuine firing power);
 [P-HB3](i') THEOREM (count(s|I) defined; data-space mollification
 proof).
 (5) CONSUMPTION SCOPING (Cor 5.1, mandatory caveat): [T-T0] and
 [T-SLRW] fire on every certified solution of the T-PERIODIC class
 ON cl(Omega_march) ONLY (surfaces/control volumes within the
 marched domain), and on SLIP-FREE instances only (G9 breadth
 pricing).
 (6) THE [T-T0P] MAIN STATEMENT (landed 2026-08-19, S-FOUNDATIONS-C2:
 doc1 revision 10 DRY of record, legs 3+5 CLOSED — authority
 VERDICT_doc1_rev10 §4; proof of record = phaseD_stop_proof.md §5,
 revision 10; the deferral formerly printed here is CONSUMED).
 [T-T0P] SPLIT-GAP-LIST THEOREM (propagation/steadification; SCHEMA
 on BOTH strata, §4-uniform-criterion labels). Assume H1-H10 and H3
 (pure periodic single-mode rotating data, speed OM, wave count n).
 Then (i) STEADIFICATION: every S1-class solution q in C(s) is a
 steady co-rotating pattern q(x, r, theta, t) =
 q_tilde(x, r, theta - OM t) a.e. on Omega_march x R, with q_tilde
 n-fold azimuthally symmetric; and (ii) CANONICITY: q is the UNIQUE
 element of the whole class C(s), weak competitors per H7'/H8'
 included. QUANTIFIER OF RECORD (l1-F2): until G5 is written, C(s)
 is the T-PERIODIC class — [T-T0P] proves the M0 sentence RESTRICTED
 to t-periodic class elements. DOMAIN + FRONT-TYPE (Cor 5.1, carried
 from the partial landing above): conclusions on cl(Omega_march)
 only; SLIP-FREE instances only (G9 breadth pricing — the excluded
 slip sheets are the physically generic RDE front type).
 SPLIT GAP LISTS of record: stratum (A) (shock-free) inherits
 G1 = [C-XBVP](a) + G2 = [C-XBVP](b) incl. the STRUCTURAL trace
 clauses (b1')/(b2') + G7 = [C-XINJ] (consumed at the §4 endgame
 only) + G8 = [C-XBVP](a') (hull/segment convexity — see the
 registry row and the G8 accounting below), under H8' (t-periodic
 class, BOTH sides; G5 = the named lift) and H9 (interface
 normalization; tilted-interface branch = G4, FOUR clauses
 g4-a..g4-d); stratum (B) (fitted fronts) additionally
 G3 = [C-MAJDA-3DT] + G11 = [C-WSF] + the G9 restriction.
 STATEMENT (i) DECOMPOSITION (G12, Remark 5.3 route declaration):
 (i) additionally carries a DECLARED minimal-load classical route
 whose conditional set avoids G2/G7/G8/H7' entirely — M0 must not
 (and does not) enshrine the over-conditioned inheritance for (i);
 (ii) carries the full stratum list. G8 ROUTE ACCOUNTING (corrected,
 r2b-F1 + revision 10): NO viable abstract-EOS G8 route is currently
 named; the granted half of route r2 stands on the STRONG SUFFICIENT
 CONDITION (H-G8-1)-(H-G8-4) — global joint convexity (strict on a
 hull neighborhood), slice-connected single-chart domain, hull
 in-chart, fiber regularity — SUFFICIENT-BUT-UNOPTIMIZED of record
 (gap accounting, not load-bearing theory; every granted item
 derived from the FULL set, revision-10 pen-grade (D1)-(D7));
 abstract-EOS status of the [T-T0P] chain (uniqueness half
 included) = OPEN AT THE ROUTE LEVEL. GAP-GRAPH EDGES (landed with this delta): G5 -> G8
 (the t-periodic lift is itself G8-dependent); G4 -> G8 (clause
 g4-d, conservation-form/foliation source, r2b-F5); G8-falsifier ->
 G7-instrument (r2b-F4: on the standing gamma(T) tabulated model the
 G8 instance routes additionally need certified table-interpolation
 enclosures — stated once in the G8 row for all three consumers).
 FALSIFIER: two-tier instance falsifier, BOTH tiers G10-gated
 (owner F2): tier 1 (kills the theorem) = a second solution with
 finitely-checkable class membership; tier 2 (kills the
 architecture's relevance) = any reproducible class-uncertified
 second K-valued entropy solution; the executable rejector layer =
 the [X-T0P] symbolic battery (reserved row, owner F2). The [S-T0P]
 SCHEMA block above remains the stage-1 statement of record; this
 main statement subsumes its propagation content on the certified
 class.]
CAUTION (verified weakening): T0 steadifies the PROBLEM; it does NOT
transfer Rao's 2-D closed-form machinery to 3-D swirl (N6). N6 STATUS
UPGRADE (2026-07-16, [F1/N6-S1], docs/rde_nozzle_N6_swirl.md +
machine-verified carrier): the boundary is now THEOREM-grade SHARP —
(i) the swirl STRUCTURE theorems hold (meridional Mach lines
unchanged, swirl = triple streamline transport, kernel laws
identical: N6-1 [T-N6-1], symbolic-sufficient); (ii) Rao's machinery DOES
extend verbatim to FREE-VORTEX swirl (uniform r·u_theta, h0, s) with
W = meridional speed (N6-2 [T-N6-2], THEOREM); (iii) beyond free vortex the
pointwise control-surface closure fails by an exact obstruction
identity (N6-3 [T-N6-3]) — field-level (five-field/AD) machinery NECESSARY;
the five-field optimality system is the named SCHEMA [S-5F].
TRANSVERSE COMPANION (added 2026-08-05, S15 [RIGOR/A], [T-SLRW]
docs/rde_nozzle_side_load.md, carrier X-SLRW in suite group (xiii)):
T0 classifies the AXIAL line (m = 0: constant in t); the rotating
side-load lemma classifies the TRANSVERSE lines — the transverse
force/moment resultants on any surface of revolution read ONLY the
m = 1 azimuthal harmonic of the trace (kinematic proof, no EOS, jumps
admitted), so n >= 2 identical equally-spaced co-rotating waves give
IDENTICALLY ZERO transverse load density (every station, every
instant: no side force, no shear, no bending), while n = 1 gives a
constant-modulus vector rotating rigidly at Omega (zero mean, but
undiminished magnitude — bearing duty, never "averages away");
pressure exerts NO axial torque on a surface of revolution (M_x == 0,
only shear can torque the wall). Together the two lemmas classify all
six rigid-load resultants of a rotating pattern. Breakage channels
(counter-rotating admixture, unequal waves, mode transitions) are the
T0-flatness impurity channels — a measured side load on a nominally
n >= 2 engine is a mode-impurity detector with a theorem behind it.

------------------------------------------------------------------------------
[T-NSW] LEMMA 4 (N-SW — spacelikeness is frame-invariant; the swirl audit). THEOREM.
In the wave frame w_theta ~ u_theta - W r ~ -D_CJ: streamlines are
strongly helical. Distinguish:
 (a) TYPE: the steady operator is hyperbolic where |w| > c (real Mach
     cones) — the sweep HELPS. The relative sonic locus |w| = c
     attached to the wave IS the Chapman-Jouguet surface: the causal
     firewall (no downstream signal climbs into the reaction zone
     through it in CJ operation) — grounding H-F1 and locating the
     coupling channels in the UNSHIELDED sectors (fill, deflagration,
     oblique-shock tail).
 (b) DATA SURFACES: a plane x = const is spacelike iff the Mach cone
     from each of its points lies on one side: angle(w,e_x) + alpha
     < pi/2 with alpha = arcsin(c/|w|), i.e. cos(angle) > sin(alpha),
     i.e. w_x > c. Since w_x = u_x and c is frame-invariant:
         AXIAL INTERFACE SPACELIKE  <=>  u_x > c,  IN EVERY FRAME
     (plane x = const, i.e. planar Gamma_d; on curved Gamma_d the
     statement reads in the normal form m_n — D2.4 L4-CERT (i)).
PROOF of (b): the chain of equivalences above; each step elementary. QED.
Consequences: CJ-sonicity licenses NO axial MOC (condition hierarchy
C1 hyperbolicity ⊅ C2 axial marching (u_x>c) ; C3 = any time-like
foliation, helical in the wave frame, never constructed = N6; C4 = CJ
type/firewall only). Rung-3a must be an implicit BVP (freezing +
Newton-Krylov), which marches nothing. The huge relative swirl never
enters rung 2: it IS the O(St) sweep term.

[L4=>R1] CAUSAL-SEPARATION COMPOSITE OF RECORD (landed 2026-08-19,
S-FOUNDATIONS-C Blocco 2; proof of record = validation/
sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md, r3.5; labels
per VERDICT_contract_and_L4R1.md B.3 as UPDATED by VERDICT_confirm
§3; provenance: VERDICT_r2pass §3 + VERDICT_escalation §4 +
VERDICT_confirm for legs 14/17). The composite is a CONDITIONAL
COMPOSITE (judge flag J-2): NO unitary THEOREM label exists; the
per-clause labels below are the ONLY quotable ones. BINDING
QUOTABLE FORM:
 (i) linearized causal separation on the monitored COLLAR of
     Gamma_d — THEOREM (Thm 1'), modulo the PRACTICE bridges (H-RW)
     and (M-c); the full-domain device-class form is THEOREM modulo
     (H-UP-fam) (Proposition 1'' per VERDICT_confirm §3, the ceiling
     granted at doc3 dry; NG-9 keeps the class instantiation).
     HONESTY CLAUSE (travels with every consumption): in the
     motivating class, Gamma_in uniform-noncharacteristicity is
     generically VIOLATED — there the Status-(a) H^1 leg carries the
     residual, not the discharge;
 (ii) steady per-phase causal separation — THEOREM, conditional on
     the SEGMENT certificate (M-a') (D2.4 L4-CERT split; never
     claimable off the segment certificate);
 (iii) finite-amplitude protection boundary priced for PLANAR NORMAL
     UPSTREAM-FACING fronts ONLY (Pi* threshold, in-box; oblique =
     NG-2, surrogate legs = NG-10), Euler+slip scope only (the
     viscous channel is NG-5).
"L4 => R1" WITHOUT these qualifiers is NOT a statement of record.
Monitors (M-a)/(M-a')/(M-b)/(M-c): SPECIFIED, not armed (J-4 — no
run artifacts; arming = implementing + running the harnesses with
the rejector-of-the-rejector legs, filed as carrier rows).
Amendments AM-4..AM-7 (VERDICT_confirm §4) are of record against
the source document's text at composition.

------------------------------------------------------------------------------
[T-T3] THEOREM 5 (T3 — the collapse, fixed wall). THEOREM.
Hypotheses: H1 one frozen gamma common to all phases; H2' fixed wall,
full-flowing, supersonic exit at every phase (ambient-blind interior);
H3 phase-independent nondimensional inflow shape (phases differ only
through (P0(xi), T0(xi))); H4 per-phase uniqueness in the class; Pa
constant; shared geometric constraints.
Claim: J[Sigma] = F[Sigma; <Pc>_mu] POINTWISE on shape space, where
<Pc>_mu = Int Pc dmu. Hence the cycle-optimal fixed wall is EXACTLY the
classical contour designed at the mean pressure.
PROOF.
Lemma A (pressure-scaling similarity; holds for gamma(T) and ACROSS
transversal shocks; THERMAL PIN of record, S-GAUNTLET 2026-08-11:
thermally-perfect ideal gas p = rho R T with FROZEN composition —
not relaxable even to rho = p f(T), which Gibbs compatibility with
e = e(T) collapses back to the ideal gas, f = C/T; the scaling FAILS
for co-volume/virial/tabulated real-gas EOS. USER SCOPE PIN
2026-08-11: the program's design-region thermo of record IS this
class — frozen composition, thermally perfect mixture). Fix Sigma, T0. If (u,T,p,rho) solves the steady
problem at stagnation (P0,T0), then (u,T,kp,krho) solves it at
(kP0,T0), k>0: continuity/energy are untouched at fixed (u,T); momentum
contains p only through grad(p)/rho, invariant; EOS rho = p/(RT)
preserved; entropy s shifts by the constant -R ln k so isentropes map
to isentropes; slip and Mach-type inflow BCs are scale-free; by H2' no
ambient datum enters. ACROSS SHOCKS: the Rankine-Hugoniot fluxes are
degree-1 homogeneous in (rho, rho u, rho E) at fixed (u,T) (rho e =
rho e(T) scales by k), and the entropy-jump and Lax/Majda transversality
conditions are k-invariant. Uniqueness (H4) makes the scaled solution
THE solution. Hence M(x), theta(x), T(x) are phase-independent and
p_xi(x) = Pc(xi) · PI(x; Sigma) for one fixed field PI.
Lemma B (stagnation-temperature similarity; REQUIRES calorically
perfect gas; named "T0-similarity" in earlier notes — renamed here to
avoid collision with Theorem 3/T0). At fixed P0, T0 -> T0' rescales u
by sqrt(T0'/T0) and leaves (M, theta, p, T/T0) invariant; the thrust
contains T0 nowhere (CF is T0-blind). Dies for gamma(T): no similarity
variable in T — this is exactly where the collapse's boundary sits.
Lemma C (affinity). Per phase F[Sigma; s(xi)] = a[Sigma]·Pc(xi)
- Pa·b[Sigma]: the wall integral Int (p - Pa) n_x dA = Pc Int PI n_x dA
- Pa (A_e - A_t), and the throat momentum flux scales with P0.
Assembly. J = Int (a Pc - Pa b) dmu = a <Pc> - Pa b = F[Sigma; <Pc>].
Identical functions on the identical feasible set: identical stationary
points and optima. QED.
Remarks (verified): (R1) per-phase optimal contours DO move with Pc —
the average of an affine family is again a member, that is all;
(R2) the averaged corner condition collapses coherently because in this
class the endpoint weight is phase-independent (see T7).
Corollaries: (C1) the repo's 1-DOF Theorem 1 is the rank-1 shadow;
(C2) Pa enters linearly too: trajectory-averaged fixed-bell design
collapses to <Pa> — cycle average and altitude average are one
mathematics (the dual-bell literature exists because SEPARATION breaks
the linearity) [PRECEDENT DUTY, 2026-07-22 S13: the trajectory-
averaged variational instance is Kraiko-Osipov PMM 34(6) 1970,
page-verified; see the T7 precedent note; mandatory citation]; (C3) oracle O1: any ensemble machinery run under
H1-H4 MUST return Rao-at-<Pc> with Delta-Isp = 0.
Sharpness [T-T3-CE]: two-phase two-gamma counterexample — J = (1/2)[a(g1)Pc1 +
a(g2)Pc2] - Pa b is not of the collapsed form; first-order closure
gamma_eff = <Pc gamma>/<Pc> (~ gamma_CJ under blowdown weighting: the
S-H freeze-at-CJ choice retro-justified); design penalty second order
(envelope theorem). For genuinely reacting gas the closed-form corner
DIES (Hoffman 1967 Eq. 78: multiplier-field condition E = 0 replaces
it) — the N4 ladder: frozen ⊂ gamma(T) (fails in principle, small in
practice, E4 oracle pending) ⊂ finite-rate (adjoint-level mandatory).
[E4 ATTRIBUTION of record, D-07 2026-08-13: the EOS-generality of the
Route-A first integrals is classical and from 1957 (Sternin, arbitrary
two-parametric gas, per the account of Kraiko et al. 2001 p.1348 — a
party to the priority dispute); our audit is a RE-DERIVATION, never
new generality; the unqualified phrase "first to do Rao with variable
gamma" is FORBIDDEN (Sun 2019 / Sun-Yu 2018 occupy the construction
move); full lineage in docs/rde_nozzle_P2_lemmaA.md §3.0.]

[T-T3-SI] PROPOSITION 5-bis (T3-SI — scale-invariance content of the
collapse: mass flow, Isp, every averaging convention). Tier 1
THEOREM; tier 2 THEOREM*. (S-GAUNTLET 2026-08-11, Form-2 panel +
Form-3 discharge on full artifacts; adjudication record =
validation/ADVISORY_Scollapse_verdict_2026-08-11.md.)
Hypotheses (tier 1): H1-T thermally-perfect ideal gas p = rho R T,
FROZEN composition, e = e(T) free (gamma(T) allowed) — EXACT and not
relaxable (Gibbs closure, see the Lemma A thermal pin above; fails
for real-gas EOS; the audit theory-core:F2 "rho = p f(T)" clause is
EMPTY and must not be imported); per the USER SCOPE PIN 2026-08-11
this is the program's design-region thermo of record. H2' as in
T-T3; H3-p p-only family P0(xi) = k(xi) P0,1 with k > 0, T0 and
nondimensional inflow shape frozen; H4 uniqueness; H-OBJ vacuum
objective Pa = 0; H-CON constraint class GEOMETRIC-ONLY (mixed or
performance constraints can reintroduce measure dependence — scope
clause of record); H-MEAS any admissible probability measure nu
(D-MU validity set; atomic per the T-O2 note) with 0 < Int k dnu <
inf.
Claim (tier 1): F(xi) = k(xi) F1[Sigma] AND mdot(xi) = k(xi)
mdot1[Sigma] (the mdot half is implicit in Lemma A, stated nowhere
in T-T3); hence Isp(xi) = F1/(g0 mdot1) is PHASE-CONSTANT and
Isp_cycle[nu] = F1/(g0 mdot1) for EVERY nu — ratio-of-means =
mean-of-ratios, every quasi-arithmetic aggregation coincides; the
shape optimum is nu-INDEPENDENT and coincides with the single-phase
steady optimum; matched-mdot degeneracy (matching the steady twin's
mass flow at ANY phase or at the mean yields the same Isp; there
matched-mdot == matched-<p>). No frozen-family hypothesis at tier 1
(pointwise-in-Sigma cancellation).
Claim (tier 2: (P0,T0)(xi) both vary; ADD H1-C calorically perfect,
per Lemma B; THEOREM* — CAP, judge-added and judge-noticed: Lemma B
carries no across-shocks clause; the RH/Mach-similarity check under
T0-rescale is the named promotion condition): F(xi) = k F1 (CF is
T0-blind); mdot(xi) = k tau^(-1/2) mdot1, tau = T0(xi)/T0,1;
Isp_cycle[nu] = R[Sigma] C(nu): C nu-dependent, Sigma-independent —
hence shape optimum nu-independent — ONLY UNDER H-F1 (T-O1(i));
bilevel coupling can make the tier-2 optimum nu-dependent.
Containment (both routes of record): at Pa = 0 the thrust-argmax
half is a corollary of T-T3 + Lemma C + the T-O2 measure-agnostic
note; the Isp-argmax coincidence with the classical argmax at
<Pc>_mu holds at ANY Pa by T-O1 composed with T-T3, under T-O1's own
hypotheses (i) frozen family H-F1 + (ii) choked feed H2, with the L4
fully-supersonic-interface discharge note. NEW here: explicit mdot
scaling; per-phase Isp constancy; every-nu VALUE equality;
matched-mdot degeneracy; tier-2 C(nu) factorization; the convention
detector.
Novelty delimiter (query-bounded): no cycle-averaged
scale-invariance / Isp-convention-equality statement found in the
read corpus (Stechmann, K-P, Paxson-Miki, Harroun, Gonzalez-Viana;
Kraiko-Osipov PMM 1970 is the trajectory-averaged AFFINE instance —
distinct object, already cited at C2); the G2 novelty bound stands
on its OLD queries (the S-GAUNTLET 4-query widening was
default-refuted); folklore risk declared: the tier-1 mechanism is
elementary — claim as PRECISAZIONE, never as discovery.
Detector (dual-proof evidence half; carrier NAMED, unbuilt — tag
X-T3SI-conv reserved, registry entry when the script lands, lint
truthfulness; owner F5a, corner dry-run executable in an idle
window): convention sweep {time, mass-flux, log-uniform, atomic
empirical}; the exact contrapositive is THEOREM (nonzero EXACT
convention-sensitivity of Isp_cycle implies violation of the
tier-1+vacuum set); the measured instrument is PRACTICE (DERIVED
tolerance + rejector, R5); T0(xi) variation trips it BY DESIGN (it
detects tier-1 departures, not T-T3 violations); KILL branch:
injected T0 variation must reopen the spread with the sqrt(T0) law.

[T-T3-MAP] (breaker map of record, S-GAUNTLET 2026-08-11; container
class SCHEMA with per-clause classes as marked; full adjudication,
killing carriers CARRIER-A..E and open items =
validation/ADVISORY_Scollapse_verdict_2026-08-11.md). T3-as-stated
is UNBROKEN by the five adjudicated breakers; the GENERAL claim
"cycle-averaged optimum == matched-mdot (Harroun-style) steady
optimum" is REFUTED as a general theorem and PROVED on the
tier-1+vacuum corner (T-T3-SI). Per breaker:
 (a) Pa != 0: fixed-wall J and ratio-of-averages Isp are protected
 [THEOREM via T-O1 o T-T3 under T-O1(i)+(ii) + L4 note; in-theorem
 failure channels: bilevel coupling, unchoked tails, axially
 subsonic patches]; average-of-ratios Isp collapses to the classical
 design at the HARMONIC mean <Pc^-1>^-1 < <Pc> strictly [identity
 THEOREM; argmax shift THEOREM* pending the design-map monotonicity
 lemma]; constraint activity is governed by ess-inf k, not <k>
 [structure THEOREM*, shift genericity SCHEMA]; a mu-positive
 SEPARATED phase kills H2' and the affinity — collapse dies even for
 J [SCHEMA — mechanism exact; class pinned by both parties:
 separation is viscous, the machinery inviscid; THEOREM* repair
 queued (hypothesis-exit lemma), rejector = the separated-phase
 monitor]. The naive "J depends on the k-distribution at first
 order" is FALSE and must never be claimed. Sea-level verdict of
 record: "coincides, at <Pc>_mu, weight now load-bearing, under the
 T-O1 list above" — NOT "no coincidence"; corrects the choking
 advisory 2-ter(a) "only the vacuum objective is protected" (too
 narrow).
 (b) outside H1/H3 the objective is the MIXTURE FORM J = a_eff <Pc>
 - Pa b, a_eff = <a Pc>/<Pc>, a = a[Sigma; T0(xi), gamma-law, m(xi),
 s(xi)] [THEOREM*, generalizes T-T3-CE]; single-state
 representability is SUFFICIENT for coincidence (the "iff" is
 struck of record); only the (p,p) Hessian diagonal
 vanishes — Cov(Pc,T0)/Cov(Pc,gamma) cross terms live in the
 pressure channel [THEOREM* under C2 regularity]; optimum-shift
 genericity CONJECTURE. The Pc-weighted closure is T-T3-CE's, and is
 DISTINCT from the TWIN-C fair twin — conflation prohibited.
 (c) swirl: Lemmas A AND B extend to the five-field swirl system
 [THEOREM* — assembled from two SINGLE-SOURCE pen legs (deriver:
 Lemma A; refuter: Lemma B REPAIR of the refuted-as-incomplete
 original); both-identities symbolic KAT in n6_swirl_kernel.py is
 the promotion condition]; calorically-perfect boundary inherited;
 first moment is a NON-breaker (mean-swirl panel P1, with the
 mandatory "IDEALIZED axial-injection class" qualifier); the real
 break is TWIN-FAIRNESS: the swirl-KE flux E_theta > 0 under
 through-flow rho u_x > 0 is unconstrained by flux nullity [THEOREM*
 under T0] and a zero-swirl twin (TWIN-A) misattributes it; recovery
 asymmetry (Gamma^2/(2 r^2) decays outward, concentrates inward)
 signs AGAINST the plug family [per-streamline THEOREM*, N6-2
 free-vortex class]. Expectations: +6% EAPi / +3% experimental EAP
 (K-P pp.7/11).
 (d) subsonic patches: the per-phase supersonic map is PARTIAL
 [THEOREM, via the T-NSW spacelikeness lemma]; mu(Xi_sub) > 0 is a
 generic-class EXPECTATION (one page-verified example, K-P Table
 1/Fig. 6); J as written is UNDEFINED when mu(Xi_sub) > 0 — the
 two-regime decomposition is load-bearing; collapse-in-form on
 Xi_sub holds ONLY under sub-hypothesis H3-cl (certified
 phase-independent closure patch pattern — EXPECTED to fail on
 migrating patterns) or the whole-interface I3 surrogate; else the
 subsonic sector joins (b)'s mixture form. Expectations: closure
 component < 5.4% typical (K-P Fig. 7); the 1.7-8.7% / ~15% figures are TOTAL
 envelopes, never a realized closure band; pressure-band -> Isp-band
 transfer OPEN/SCHEMA.
 (e) conventions/matching: invariance is THEOREM on the p-only
 scaling class ONLY (value + argmax; the refuter counterexample
 (2 P0, T0/4) kills full-H1-H4 VALUE invariance); the design-pressure
 wedge <Pc>_mdot - <Pc>_t = Var(Pc)/<Pc>_t is exact on the p-only
 class, sign clause CONJECTURE; the matched-pressure formula
 p_match = <p u_x/T>/<u_x/T> is THEOREM* ONLY for the twin DECLARED
 by u_s/T_s := <u_x/T> (the (T_s=<T>, u_s=<u>) twin differs at order
 (sigma/mu)^2 — the construction must be declared); the fair twin of
 record is TWIN-C flux-consistent; Harroun's averaging convention is
 UNDECLARED (choking advisory 3-bis) so comparisons are ill-posed
 until a convention is pinned; every collapse-adjacent theorem
 statement carries its convention and matching. The judge-added
 full-H1-H4 shape-argmax refinement is EXCLUDED from this record
 pending its own refuter pass.
 S18 clause of record: the S18 +0.04% twin agreement is a CORNER
 MEASUREMENT (choking advisory 2-ter(A)), NEVER citable as evidence
 of general RDE/steady coincidence; a five-line hypothesis audit of
 the S18 twin against the tier-1+vacuum set is the NAMED
 PRECONDITION for any stronger phrasing — AUDIT PERFORMED (S24
 2026-08-12, T2a; verdict INSIDE the corner with the H3-p-degenerate
 and H4-instance qualifiers carried; see the S24 registration
 block).
 Harroun clause of record: "Harroun-style" above is a tier-1 CORNER
 READING of the TWIN-A construction (zero-swirl comparison twin,
 Harroun p.666; pp.665-666 document a comparison construction, not
 an optimization) — NOT an identification of Harroun's methodology
 with the formal tier-1 lab; the TWIN-A misattribution caveats
 (swirl panel P4) apply outside the corner.

[LAND-C4-LD RIDER — T-T3-MAP-context candidate cross-cite, [ADV]]
(S-FOUNDATIONS-C4 landing 2026-08-20; executes VERDICT_r22f §7 L-D /
[GRAFT-G05] landing rider [REV-NRS-5]): P-B F-01 (time-averaged
stagnation constraints "empirically recognized", citing P-D) =
candidate cross-cite in this T-T3-MAP context; [ADV] provenance,
CT-6-clean, no number consumed.

------------------------------------------------------------------------------
[T-DISC] FIBER-SEPARATION THEOREM (Part III block, landed
S-FOUNDATIONS-C4 2026-08-20)

[LAND-C4-LA LANDING HEADER] Executes VERDICT_r22f §7 L-A at the
J-V2-corrected anchor (after the T-T3-MAP block, before PROTOCOL
T3-CONTROL — the fiber axis completes the breaker census with the
projection axis). Carrier of record: validation/sfoundations_raws_
2026-08-13/phaseD/phaseD_r22f_centerpiece.md Part 1 AT CLOSURE, with
grades per VERDICT_r22f §1 (single label authority; unchanged by the
E-5 pass, VERDICT_escalation_c4 §5.5) and ALL scopings ([REV2-r1-1..5],
[REV2-r2-1]). READING RULE (binding, [REV2-r1-21]/[REV2-r2-8](b)): the
corrected forms land, never the superseded sentences — fragments
quoted inside marker blocks below as superseded are historical record
and govern nothing. This block is round-3-refereed text (no round-4
delta): no unrefereed-delta line applies here.

DEFINITION D1.1 (admissible data class). A := the class of per-phase
interface data families xi |-> s(xi) of the program's standing scope:
pure periodic single-mode rotating wave (pin H3; monitor = T0 flatness,
M0 VI.4bis), frozen thermally-perfect mixture (pin P1), interface
normalization H9, mu = pushforward of the time measure (uniform under
rigid rotation; [MS-T-MEASURE] D.9(ii)).
Each s(xi) carries at least (p, h0, s, u_x, u_theta = Gamma/r) with the
h0-CONVENTION DECLARED (whether h0 includes u_theta^2/2 — the D.13
contract fact, swirl5f DISPATCH §4 B-2; consumed here as a hypothesis
switch, not resolved here).

DEFINITION D1.2 (p-only projection). pi: s(xi) |-> (P(xi), uniform),
the map that retains the per-phase pressure trace P(xi) and replaces
every other field by the phase-uniform default (the EAP-style /
pressure-only reading of the interface). The FIBER over a pressure trace
P is pi^{-1}(P) ∩ A.

[REV2-r1-1] PIN (fixes amendment R22F-L0-7, applied): the "phase-uniform
default" of D1.2 is PINNED = the family's OWN mu-means (each non-pressure
field replaced by its mu-average over the cycle). The fiber over P is
therefore the CALIBRATED-SCALARS fiber: it fixes P(xi) PLUS all field
mu-means, and the fiber coordinate is exactly the fluctuation + swirl
content that [T-DISC-1] sweeps and M-RED band B-2 measures. eps_fib
([T-DISC-3]) is read under this pin. The canonical-constant reading
(fiber = full preimage of the P trace, with O(1) h0/s trace variation)
is EXCLUDED — it would decouple eps_fib from every B-2 output and is not
the object of any statement in this block; the [T-DISC-4](a) scale
sentence is read under the same pin ([REV2-r1-5]).

The question of record (mandate row, part (1)): characterize the fibers
and LOWER-BOUND the J-variation within a fiber — "exonerates or convicts
THE AVERAGE with zero CFD (the (b) half of R22)". Objective J = the
cycle-averaged thrust functional of record (Part I; two-regime
decomposition where mu(Xi_sub) > 0, T-T3-MAP(d) — the statements below
are made on the supersonic-map sector; the subsonic sector joins the
mixture form and is out of this theorem's scope, declared).

[T-DISC-1] FIBER NON-DEGENERACY.
STATEMENT. THEOREM* (conditionals inherited and named below). For every
admissible pressure trace P(xi) whose fiber contains an element with
through-flow (rho u_x > 0 a.e. on the exit station), the fiber
pi^{-1}(P) ∩ A contains a one-parameter family {s_lambda} with identical
(P(xi), h0-trace, s-trace, mass-flux trace) and swirl-KE flux
E_theta[s_lambda] ranging from 0 to a strictly positive value at the
measured corpus scale, ALL satisfying every flux-nullity constraint of
record. In particular pi is non-injective on physically distinguishable
data and NO constraint of record pins E_theta given P(xi).
PROOF (by citation, zero new derivation — the inputs are of record):
(a) the cycle-averaged axial angular-momentum flux constraint is
[MS-T-FLUXNULL] (D.6) THEOREM*: in the idealized class (inviscid,
J_inj = 0) the area-integrated mass-flux-weighted cycle mean of Gamma
vanishes at every admissible station;
(b) [MS-T-SKE] (D.10) THEOREM: E_theta > 0 strictly under
through-flow with u_theta ≢ 0, and E_theta is NOT constrained by D.6
under ANY measure — the theta-halves-at-each-radius exhibit realizes
Gamma-flux cancellation r-fiberwise with E_theta arbitrary;
(c) K-bar = 0 fiberwise UNCONDITIONAL on periodic BV composites
(swirl5f, verifier-confirmed: judgeverify ITEM 3.3, sympy witness) —
adding the theta-halves swirl content to a periodic composite leaves
the azimuthal-flux mean identically zero, so the construction stays
inside the residual-mean constraint as well;
(d) the first moment is a NON-breaker with the mandatory "IDEALIZED
axial-injection class" qualifier (mean-swirl panel P1, cited at
T-T3-MAP(c) — the mean-swirl covariance block of record).
The family s_lambda := (theta-halves exhibit scaled by lambda) composed
with the fiber's base element satisfies (a)-(c) for every lambda by (b);
pressure, h0, s, mass-flux traces are untouched by construction of the
exhibit (it permutes u_theta sign content across theta-halves at each
radius and scales its magnitude, leaving p, h (hence s), and rho u_x
fixed; h0 fixed under the DROP convention verbatim, and under the FOLD
convention fixed provided the exhibit's E_theta budget is compensated in
the meridional KE at fixed h — the compensated variant is admissible on
any station with meridional KE headroom, hypothesis H1.3 below).
WHY THEOREM* (named conditionals): inherits D.6's (c1) assembled-balance
symbolic check QUEUED (gap G-a) and (c2) H-AM0 audited-per-dataset.
[LAND-C4 R-6 MINT NOTE: the carrier's conditional (c3) — "the K-bar = 0
leg carries ADVISORY provenance until the R4 landing window mints it
(proof is pen-complete + machine-witnessed; no physical conditional)" —
is RETIRED at this landing: the K-bar = 0 mint at record grade executed
at the D.18/[MS-DEF-KRES] site in this same edit (VERDICT_r22f §7 L-B,
R-6). Conditionals (c1)/(c2) remain.]
HYPOTHESES: H1.1 through-flow rho u_x > 0 a.e. at exit; H1.2 idealized
axial-injection class (J_inj = 0, H-AM0-H-AM5); H1.3 under the FOLD
h0-convention, meridional-KE headroom for the compensated exhibit
(trivially checkable per family; AG-1 valve: sufficient-not-optimized,
declared); H1.4 standing pins H3/P1/H9.
FALSIFIER: exhibit ONE constraint of record (theorem, certificate, or
contract row) that determines E_theta from (P(xi), h0, s, mdot) on A —
this collapses the fiber and kills the theorem. (D.10's own falsifier
battery, panel A4 with pin B-1, is the executable layer; the KE-vs-h0
normalization trap is priced there and must never fire the falsifier on
a unit mismatch.)

[T-DISC-2] J-SEPARATION LOWER BOUND WITHIN A FIBER.
STATEMENT. Split-grade, declared per leg:
(i) SIGN LEG — THEOREM* (SCOPED; BOOKING level under H2.2, on
PHYSICAL-h0-FIXED comparisons — [REV2-r1-2] below): within a fiber, at
fixed (P(xi), h0-trace, s-trace, exit geometry, exit static-pressure
trace), the momentum-flux thrust per streamline is strictly decreasing
in the swirl content Gamma^2: from the exact per-streamline relation
u_e^2 = 2(h0 − h(p_e, s)) − v_e^2 − Gamma^2/r_e^2 (algebra verified:
swirl5f judgeverify §5.3, re-derived and sympy-confirmed there),
at fixed (mdot, h0, s, p_e, v_e, r_e) each increment of Gamma^2
subtracts exactly Gamma^2/r_e^2 from u_e^2. The pressure-thrust term
∫(p − Pa) dA is FIXED within the comparison BY HYPOTHESIS H2.2
([REV2-r1-2](1): booking-level comparison, frozen exit conditions).
Hence J separates single-signedly AT THE BOOKING LEVEL on
physical-h0-fixed comparisons: J(s_lambda) strictly decreases in
lambda^2 on the supersonic-map sector ([REV2-r1-2](2) scope; the
uncompensated DROP branch is geometry-signed with the r_e = r_in
degenerate corner).
[REV2-r1-2] SCOPING REVISION (fixes R22F-L0-5, R22F-L0-6, R22F-L2-3;
the carrier's original justification "(same P trace)" and unqualified
"strictly decreases" are SUPERSEDED and never land — integrated above
per [REV2-r1-21]):
(1) PRESSURE-TERM FIXITY (L0-5): the thrust functional of record
evaluates momentum flux + (p − Pa) on the EXIT/enclosing surface,
not on the interface; the fiber's shared P trace is
the INTERFACE trace and does not fix the exit term. Within the theorem
the fixity holds BY HYPOTHESIS H2.2 (fixed exit geometry + exit
static-pressure trace) — leg (i) is therefore a BOOKING-LEVEL
comparison (frozen exit conditions), and is labeled as such.
(2) CONVENTION SCOPE (L0-6/L2-3, probes r22f_v2_probe_r1_l0_fiber_
sign_2eps.py PART C and r22f_v2_probe_r1_l2_drop_sign.py, both PASS):
the strict decrease holds for PHYSICAL-h0-FIXED fiber comparisons —
the FOLD convention, or the DROP family in the compensated-exhibit
variant (H1.3 headroom). On the UNCOMPENSATED DROP branch the booked
h0-trace is fixed while the physical total enthalpy grows with swirl,
h0_phys(lambda) = h0_data + lambda^2 Gamma_0^2/(2 r_in^2), and the same
exact algebra gives Delta u_e^2 = lambda^2 Gamma_0^2 (1/r_in^2 −
1/r_e^2): momentum thrust INCREASES for r_e > r_in and the family is
IDENTICALLY DEGENERATE (zero separation) at r_e = r_in. This is
geometry-signed and matches the record's own B2 drop-bias clause
(judgeverify §5.2, verifier R-B; ≈ 0 at r_e ≈ r_in). Leg (i)'s
THEOREM* is SCOPED accordingly; the uncompensated DROP branch is
routed to the geometry-signed formula (single-signed PER FAMILY, sign
set by r_e/r_in; the r_e = r_in degeneracy is named beside R-7).
(3) ACTUAL-PAIR STATUS (L0-5 deeper limb): for actual per-phase
solution pairs H2.2 is not free — at fixed (h0, s, mdot, A_e) the exit
pressure is an OUTPUT and moves with Gamma (the B1 radial-equilibrium
companion, 0.6-9% of p, is its physical face). The actual-pair
separation statement (booking debit COMPOSED with the B1 exit-pressure
shift, sign adjudicated) is NOT asserted here at any theorem grade: it
is the M-RED band B-2 measured question, named. (Refuter L0 probe
evidence, PART B: in the synthetic counter-model the actual Delta J
tracks the booking Delta J within ~0.2% and keeps its sign —
plausibility context only, not proof.)
(ii) MAGNITUDE LEG — SCALING-ESTIMATE (labeled; NOT a bound): the
separation scale at measured corpus swirl content is the B2 booking
class: 1.5-3% of thrust (FOLD variant, single-signed); under the DROP
variant the booking bias is |bias| ≤ delta_int^2/2 and ≤ the fold value
iff r_exit ≤ sqrt(2)·r_in (swirl5f §1 B2 REPAIRED form incl. verifier
edit R-B; ADVISORY provenance). The underlying measured inputs: corpus
tangential energy 3-6% KE-NORMALIZED (h0-normalized reading ~4x smaller,
0.3-2.5% — pin B-1; D.10 falsifier text), u_theta/(Omega r)
≈ 0.15-0.20 (DISPATCH §9 sweep, 26 PDFs), per-phase exit swirl angle
10-14 deg (B5 row). Additionally the radial-equilibrium fiber companion:
B1 pressure shift 0.6-9% of p (working 1.5-4%), single-signed, phase-
coherent, "survives EVERY mu-average" (swirl5f §1 B1; SCALING-ESTIMATE).
LOWER-BOUND READING (the mandate's ask, stated honestly): the theorem-
grade content is that the within-fiber J-variation is BOUNDED BELOW BY A
STRICTLY POSITIVE, SINGLE-SIGNED functional of the fiber coordinate
(the E_theta debit: leg (i)); its NUMERICAL floor at corpus swirl
content is estimate-class (leg (ii)) until M-RED measures it on certified
families (M-RED band B-2). No numeric lower bound is asserted at
THEOREM grade — asserting one would exceed the held evidence class.
[REV2-r1-3] PROPAGATION (fixes R22F-L0-5/L0-6/L2-3 at this reading):
the LOWER-BOUND READING above is SCOPED to the BOOKING level on
physical-h0-fixed comparisons (FOLD or compensated variant; H1.3):
"bounded below by a strictly positive, single-signed functional" holds
THERE. On the uncompensated DROP branch the within-fiber variation is
geometry-signed with the r_e = r_in degenerate corner (ZERO
separation) — no strictly-positive floor is asserted on that branch.
The actual-pair (free exit state) form is an M-RED/B-2 measured
question, not a theorem of this block. The same scoping applies to the
[R22F-FORCHETTA] (iii) rigor column ([REV2-r1-18]).
HYPOTHESES: H2.1 = H1.* ; H2.2 fixed exit geometry and exit static
pressure across the fiber comparison (no re-optimization inside the
comparison — re-optimization transfer is priced by [T-DISC-3]); H2.3
supersonic-map sector (per-phase map partial, T-T3-MAP(d)); H2.4
h0-convention declared per family (fold/drop switch). AG-1 valve applied:
H2.2/H2.3 are strong, trivially checkable, sufficient-not-optimized.
FALSIFIERS: sign leg — one admissible instance with
∂(mdot·u_e)/∂(Gamma^2) ≥ 0 at fixed (p_e, h0, s, v_e, r_e) (kills (i):
it contradicts the exact relation, so it can only fire via a hypothesis
exit — which is precisely what it would localize). Magnitude leg — a
certified interface family whose computed exit-swirl debit at corpus
E_theta scale falls below the M-RED derived bar B-2 (kills the 1.5-3%
class for that family; the class claim retreats to the families where it
is measured).

[T-DISC-3] OPTIMIZATION CONSEQUENCE (2-EPSILON TRANSFER).
STATEMENT (SCHEMA; landed in the [REV2-r1-4] corrected two-leg form
with the [REV2-r2-1] corrected parenthetical — the pre-round statement
and parenthetical are SUPERSEDED and never land, per [REV2-r1-21]/
[REV2-r2-8](b); executable counterexamples against the superseded form
are of record: r22f_v2_probe_r1_l0_fiber_sign_2eps.py PART A and
r22f_v2_probe_r1_l2_two_eps.py). Let eps_fib(P) := sup over the fiber
of |J(s) − J(s')| — the within-fiber separation, read under the D1.2
pin [REV2-r1-1]; eps_fib(P) > 0 by [T-DISC-1]+[T-DISC-2](i) wherever
the PHYSICAL-h0-FIXED variant is admissible (FOLD or compensated, H1.3
headroom; [REV2-r1-2] scope), while on the uncompensated DROP branch
the within-fiber variation is geometry-signed with the r_e = r_in
degenerate corner (ZERO separation, [REV2-r1-3]) — no strictly-positive
floor is asserted on that branch ([REV2-r2-1] corrected reading of
record; round-1 probes witness the degenerate corner). TWO sound legs,
each at its own grade:
(a) ADEQUACY / UPPER leg (per-surrogate; claim 10 read verbatim;
SCHEMA over the cited lemma): for a GIVEN surrogate G = g∘pi with
uniform value-error premise (U_G): sup_Sigma |J_exact[Sigma] −
G(Sigma)| ≤ eps_G, any legitimate argmax of G is at most 2·eps_G
suboptimal for J_exact (swirl5f claim 10, PROVEN in-panel D+R;
constant 2 sharp — two-point example; uniformity (U) OPEN twice over +
class-wide H-A1; record theorem target = S.22 shock-free sub-scope,
F2). The bound is PER-SURROGATE: eps_G — never eps_fib — enters it.
The F5a conditional-gain template binds to the surrogate actually
used: "gain net of 2·eps_G, eps_G = measured/assumed per family".
(b) IRREDUCIBILITY / LOWER leg (the conviction direction; SCHEMA with
the design-realizability premise NAMED): with eps_fib(P) read under
the D1.2 pin [REV2-r1-1], and premise (DR): there exist admissible
designs Sigma_1, Sigma_2 whose data s(Sigma_1), s(Sigma_2) lie in one
fiber with |J(s(Sigma_1)) − J(s(Sigma_2))| = osc > 0 ([T-DISC-1]
constructs same-fiber DATA pairs; their DESIGN realization is this
named premise, checked per family at M-RED time). Then EVERY
pi-factoring surrogate takes one value on the pair and has sup-error
≥ osc/2; the BEST pi-factoring surrogate (fiber midrange) attains
sup-error exactly sup_P eps_fib(P)/2 (L2 probe-verified); and by the
sharpness construction a legitimate argmax selection can be up to the
full oscillation suboptimal. NO refinement of p-only data reduces
THIS floor — the irreducibility sentence attaches to leg (b) ONLY,
never to leg (a)'s upper bound. Where (DR) is not yet checked, the
consequence is scoped to the data-class reading (fiber non-degeneracy
of the DATA, [T-DISC-1]) and says so.
INTER-FIBER ranking error of a p-only surrogate is UNBOUNDED by fiber
diameters (the L2 counterexample) — no statement of this block bounds
it; only (U_G)-type premises do.
HYPOTHESES: leg (a) = (U_G) per surrogate ((U) OPEN, named; on its
current status the consequence holds with eps read as the measured/
assumed value per family, not as a certified class constant) + H2.*;
leg (b) = (DR) + the D1.2 pin.
FALSIFIERS: claim 10's own (a two-point construction beating 2·eps_G);
any proof that (U) fails structurally on A (would re-scope the lemma
to sub-families); for (b): a proof that no admissible design pair
realizes any non-degenerate fiber pair (kills (DR) class-wide; the
conviction retreats to the data-class reading, declared).
Every G2-class gain certificate over a p-only pipeline is therefore
conditional: "gain net of 2·eps, eps = <measured/assumed>" (the F5a
template duty, DISPATCH §5).

[T-DISC-4] VERDICT SEMANTICS — WHAT IS CONVICTED, WHAT EXONERATED.
STATEMENT. SCHEMA (dichotomy assembly; binding reading of
[T-DISC-1..3]).
(a) CONVICTED: the P-ONLY REDUCTION pi. Its fibers are non-degenerate
([T-DISC-1], THEOREM*), J separates within them single-signedly
([T-DISC-2](i), THEOREM*), at a scale whose current estimate is the
1.5-3% thrust class plus the B1 0.6-9%-of-p companion (SCALING-ESTIMATE,
labeled), and the loss is not recoverable by optimization downstream of
pi ([T-DISC-3]). Pressure-only surrogates are therefore NOT adequate
for percent-level thrust ranking on swirl-bearing RDE data — with zero
CFD consumed. This is the (b) half of R22, discharged at the grades
printed here.
(b) NOT CONVICTED (exonerated at this axis): the per-phase FULL-STATE
average — the program's own J, which carries (p, h0, s, u_x, Gamma) per
phase. Nothing in the fiber argument touches it: its data do not factor
through pi. Its residual exposure is the REDUCTION axis ([T-RED], at
the D.18/[MS-DEF-KRES] site) and the adequacy axis ([R22F-FORCHETTA]
channels (i), (ii), (iv)), not the fiber axis.
(c) PROHIBITION carried forward: neither "the mean flow has no swirl"
nor "the time-mean interface carries net Gamma ≠ 0 at first order" may
be asserted (D.12 PRACTICE); T-DISC lives strictly at the
E_theta/second-moment level, which flux nullity leaves free.
[REV2-r1-5] PROPAGATION (fixes the downstream inheritance named by
R22F-L0-4 CONSEQUENCE + R22F-L0-5/L0-6/L0-7): in (a) above, "J
separates within them single-signedly" is read at the BOOKING level on
physical-h0-fixed comparisons ([REV2-r1-2] scope; uncompensated DROP
branch geometry-signed with the r_e = r_in degenerate corner); the
"1.5-3% class plus the B1 0.6-9%-of-p companion" scale sentence is
read under the D1.2 pin ([REV2-r1-1]: calibrated-scalars fiber — the
scale claim is exactly what B-2 measures; no O(1) trace-variation
reading); and "the loss is not recoverable by optimization downstream
of pi ([T-DISC-3])" cites [T-DISC-3] leg (b) of [REV2-r1-4] (the
irreducibility floor, premise (DR)) — NOT the superseded 2·eps_fib
upper form.
FALSIFIER (of the conviction's relevance, not its truth): an M-RED
measurement campaign returning eps_fib below the smallest design delta
the program ever certifies (then the conviction is real but priced
irrelevant for our class — an honest positive outcome, reported as
such).

------------------------------------------------------------------------------
[R22F-FORCHETTA] — Adequacy bracket of record (2D-per-phase-averaged
vs 3D-unsteady; user-facing)

[LAND-C4-LC LANDING HEADER] Executes VERDICT_r22f §7 L-C (site named
per SR-C4-17: immediately after the new [T-DISC] block, beside
T-T3-MAP and the breaker census its channels consume). Content
transcribed VERBATIM from validation/sfoundations_raws_2026-08-13/
phaseD/phaseD_r22f_centerpiece.md Part 5 AT CLOSURE (the [REV2-r1-15]
header declaration, the [GRAFT-G10] enrichment note, the CELL RULES
line, the six-channel table with the [REV2-r4-5] cell readings as
amended at this landing by the E-5 deferred inputs per
VERDICT_escalation_c4 LA-5 — two-symbol split mu_curv/mu_red
[E5-L1-4], sustained-ball-floor mu_eff reading [E5-L2-2] — the
[REV2-r1-17/18] reading notes, the notes blocks [GRAFT-G02..G07]
under their CT-6 ceiling banner, and §5.1 roll-up + headline with the
fitted-sheet qualifier). This table is the user-facing adequacy
bracket of record until M-RED/R22-CFD tighten it (post-close addendum
C3 mandate). Grades per VERDICT_r22f §1.
(vi)-ROW DELTA STATUS (executes LA-5(ii)): round-4 delta refereed
(E-5 targeted pass of record, esc_refute_r4delta_l{0,1,2}.md, 0
BREAK; [ESC-E5-1/2/3] applied; deferred inputs executed at this edit
per VERDICT_escalation_c4 LA-5).

CELL RULES (enforced): bound-or-estimate declared; rigor class per
bound; provenance per number; SCALING-ESTIMATE cells labeled [SE];
what-tightens-it named in program order (T-DISC → T-RED → M-RED →
R22-CFD); NO cell above its held evidence class.

[GRAFT-G10] HEADER ENRICHMENT NOTE (grafted per SYNTHESIS §(c) G-10 /
(e).6, CT-3 [REV-NRS-1]; the addendum-(c) record sentence itself is
UNCHANGED — it is TRUE as written): nearest existing referees for the
per-phase thrust error = P-B Fig. 15 / P-C Figs. 13+20b — same-solver
URANS unsteady-vs-steady pairs at GLOBAL averaging — named and
DISQUALIFIED for the two stated reasons (companion not
per-phase-averaged; truth not external/experimental). The bracket still
CLOSES only via our own R22-CFD or a dedicated data procurement — until
then every cell is bound/estimate-class, never externally refereed.
[ADV]

[REV2-r1-15] STRUCTURAL DECLARATION OF RECORD (addendum_c4 (c),
delivery-check item; table-header status: this paragraph IS
the table's header note): NO EXTERNAL PUBLISHED REFEREE EXISTS for the
per-phase thrust error: the literature carries NO unsteady c_F datum
that discriminates the 2D-per-phase-averaged prediction against
3D-unsteady truth (the Harroun 1.25-flat is quasi-cycle-averaged,
verified verbatim at source 2026-08-20 — it is the non-discrimination
datum, not a referee). CONSEQUENCE: the bracket CLOSES only via our
own R22-CFD or a dedicated data procurement; until then EVERY cell of
this table is bound/estimate-class, never externally refereed.
(Enrichment — nearest existing referees, named and disqualified — is
the [GRAFT-G10] note above.)

[ORCH-HARV-1] ORCHESTRATOR HEADER GUARD (declared orchestrator
addendum note — NOT judge text; provenance = validation/
sfoundations_raws_2026-08-13/blocco3/BASE_PRESSURE_HARVEST_c4.md;
[ADV]): best-of-sweep != argmax: no published work optimizes the true
3D-unsteady case; sweep/redesign evidence is ranking-signal only.

| Channel | BEST (situazione migliore) | WORST (situazione peggiore) | Rigor + provenance | What tightens it |
|---|---|---|---|---|
| (i) Time-coupling / unsteadiness | **0 (exact)** on the certified class: [T-T0P] steadifies — gap identically zero MODULO the split gap lists (stratum A: G1,G2,G7,G8; +G5 lift, G4 tilted-interface; stratum B: +G3,G11,G9) and Cor 5.1 scoping (cl(Omega_march), slip-free). BOUND class, conditional. | **CLASS EXIT, unbounded of record**: aperiodic storage / mode transitions are an H-AM1 exit, not a gap number; slip-sheet fronts (the physically generic RDE type) are EXCLUDED by G9; the steady-sweep corrector half is G3/corrector-owned (VI.4bis), unquantified of record. Guard = T0-flatness monitor + f_cycle contract field (A32, registry :1925). No number is asserted — asserting one would exceed evidence. | [T-T0P] SCHEMA on both strata; H-AM1 exit; boundary PRACTICE | R22-CFD-1 (class membership on a real coupled field); G5/G9 lifts (F2 theory); the corrector program (G3 owner) |
| (ii) Azimuthal-structure reduction (T-RED's own face) | **O(St_n^2) on-ray; single-digit % plausible** [SE]: K-bar=0 kills the mean channel (THEOREM*, [T-RED-2](i)); first-order scale Lambda = 0.59-1.11·St_n, work-term 0.007-0.09 = 0.7-9% [SE] (verifier-repaired, judgeverify ITEMs 1.1, §5.4); on-ray St^2 cancellation exists in-panel but is LICENSE-GATED (X-T3QS-5F, F2) — NOT bankable in this cell yet. Read WITH the good-fitted-sheet condition ([REV2-r1-7/18](a)). | **>10% NOT EXCLUDED off-ray** (claim 9 verbatim, C-T1 OPEN) [SE]; azimuthally-fed interior front segments UNREACHABLE by the march (row-13 pin) with E5 magnitude DISPUTED-OPEN; Harroun Fig. 18 (p.669, page-verified centerpiece §2.3) is the physical instance of the mechanism class. | structure THEOREM* (machine-witnessed; K-bar=0 MINTED at record grade at this landing, R-6); magnitudes [SE]; swirl5f claims 2/9/11/13 + judgeverify | T-RED (D.18/[MS-DEF-KRES] site, structure) → M-RED bands B-1/B-3 (measures eps, splits (J)/(H)) → X-T3QS-5F license (F2) → R22-CFD-1 |
| (iii) Swirl / tangential content | **B2 ≈ 0 + B1 at 0.6% of p** [SE]: drop-convention with r_exit ≈ r_in makes the booking bias ≈ 0 (geometry-signed, \|bias\| ≤ delta_int^2/2; ≤ fold iff r_exit ≤ sqrt(2)·r_in — verifier R-B repaired clause); B1 low end 0.6% of p; B3 low end 0.5% in T; B5 exit swirl 10 deg bookkeeping-only. | **B1 up to 9% of p + B2 3% of thrust (fold) + B5 14 deg** [SE], all single-signed/phase-coherent, "survives EVERY mu-average" (B1 row); **WORST-DIRECTION MARKER (mandatory): Paxson-Miki shroud finding — 58.1% → ~71.5% of the notional ideal at FIXED area ratio** (V7 = argmax ~71.5%; the recommended V5 = 70.0%; figures are percentage POINTS of ideal, C25 corrections at findings_registry.yaml:2026 per [REV2-r1-17]) — **larger than the entire area-ratio design line, declared unexplained by the authors, and the registered swirl-breaker candidate** (E_theta debit + recovery asymmetry AGAINST the plug; advisory :807-812): configuration-scale effects the 2D-per-phase average could be blind to. | all magnitudes [SE]: swirl5f §1 B1-B5 repaired forms + R-A/R-B edits; shroud = [REP] page-verified external datum; sign leg of the debit THEOREM* ([T-DISC-2](i)) under the [REV2-r1-2] scope (physical-h0-fixed / booking level; uncompensated DROP geometry-signed, r_e = r_in corner — [REV2-r1-18](b)) | T-DISC fiber bound (block above) → M-RED band B-2 (measures the debit) → F2a pre-registered shroud prediction → S-5F build decision (user, pending) |
| (iv) Averaging adequacy (sizing vs ranking) | **~1% at sizing level** [REP]: Paxson-Miki area-ratio agreement 6.54 vs ~6.5 (R26, registry :2147); Harroun 1.25-flat read at its verified limits = no measured contradiction of sizing adequacy. | **RANKING THRESHOLD OPEN (R26)**: adequacy NOT demonstrated for percent-level contour ranking; in-class contour deltas are FRACTIONS of a point (Hoffman scale 0.04-0.34%; our +0.51% in-class, 3bis-D advisory :828-832) vs configuration spreads of TENS of points — the average could be blind exactly at design-relevant scale. Harroun 1.25-flat is a NON-DISCRIMINATION datum at verified limits (no thrust measured; no 3-D unsteady flared; "2-D AND averaged" not isolated; no bar — advisory :800-805), NOT proof of blindness. | [REP] external data, page-verified in the confrontation; threshold OPEN of record (R26, "decided by R22") | M-RED (eps vs in-class deltas — the in-house threshold reading) → R22-CFD-2 (Harroun pair, field-facing) → R22-CFD-1 |
| (v) Model-form bars | **Few-% class, priced and monitored**: frozen-vs-equilibrium bracket at the low end of its class with per-champion re-execution (P-F14 duty, registry :1627; instrument = hypaudit GAS-FROZEN monitors); base pressure in closed-wake regime with declared two-regime closure (transition Pa/Pc ≈ 0.15, R8). | **[T-EQBR] +6.3..+7.0% on the internal instance** (can exceed claimed design deltas — the P-F14 row's own warning); **base-pressure model-form UNPRICED on truncated plug**: Pb/Pa = 1 inadmissible in BOTH regimes (base stays ~20% below ambient in open wake — Harroun p.8 via R8); NO truncated-plug RDE base measurement exists in the read corpus — the nozzleless→plug transfer is an **ANALOGY, declared** (R8, advisory :1136). | frozen bracket = measured internal instance ([T-EQBR]) + corpus class; R8 = [REP] + declared ANALOGY (R8 vacuum re-confirmed by the C4 base-pressure harvest — [ORCH-HARV-2] below); T-T4 sharpness physical hole open (advisory :855) | P-F14 per-champion re-execution (standing duty); R8 = external measurement (procurement class, not ours); R22-CFD-1 prices coupled model-form jointly |
| (vi) OPTIMUM-SHIFT (value-adequacy ≠ optimum-adequacy) [REV2-r1-16] | **\|argmax shift\| ≤ delta/mu_curv, A-POSTERIORI form** [SCHEMA] (two-symbol landing split per E5-L1-4: mu_curv = gradient route, J_TRUE floor; mu_red = value route, measured J_red floor): mu_curv = the curvature floor of J_TRUE ([REV2-r4-1](a)); the MEASURED engine curvature at S* (segmented TR-Newton curvature, Hessians of record — the measured CARRIER, a J_RED Hessian) instantiates it ONLY UNDER H-G6 (mu_eff = (mu_meas − b_E) − L_H, read on the (E)-certified ball at the sustained band-lower-edge floor, never the bare point measurement [E5-L2-2]; L_H = the curvature-level face of the reduction residual, UNDERIVED — [REV2-r4-1](b)(c)): until L_H lands the GRADIENT route licenses NO number even a-posteriori from the measured carrier alone; critical-cone identification O1-GATED at a margin-active S*, [T-RED-2G] [REV2-r2-3](D)/H-G4 — POINT-measured, so the cell licenses ONLY the a-posteriori form, valid IF delta/mu_curv ≤ the certified basin radius (check per condition (1), radius deriver named [REV2-r2-3](E); cone-pairing + licensed forms (T)/(C) per [REV2-r2-3](A) UNDER H-G5 ([REV2-r3-1] as narrowed by [REV2-r4-2]: feasible-set CONVEXITY declared and checked per instance — a prox-regularity certificate does NOT license the forms; KS-margin-set status at a margin-active S* OPEN, residue R-14); constrained/KKT form per condition (2) as repaired; metric + typing per condition (3)/[REV2-r2-3](B); delta evaluated at S*_red per [REV2-r3-2]); VALUE-ROUTE bound available a-posteriori [SCHEMA] — the ONLY route whose floor mu_red is legitimately the measured carrier as-is (J_red-side derivation, [REV2-r4-1](d)): \|argmax shift\| ≤ 2·sqrt(eps_U/mu_red) with eps_U = the UNIFORM value-error level on the explored basin — measured instantiation = the sweep-sup of the M-RED value legs (A)-(B) along the §3.6 design sweep at SAMPLED-SUP (estimate) class, licensed only when sustained under the declared sweep-refinement re-check ([REV2-r4-3]); a single-family eps does NOT discharge the premise; measurement instantiates the premise at declared class, it NEVER discharges it — certified closure stays with (U)/S.22, R-1 ([REV2-r2-3](F) as repaired by [REV2-r3-3] and [REV2-r4-3]); a-posteriori check for this route: 2·sqrt(eps_U/mu_red) ≤ the certified basin radius ([REV2-r2-3](E)/R-12; reduced argmax inside the basin) + sweep-sup coverage declared + H-G5 status declared (a check-pass at estimate class is itself estimate-class, defeasible under sweep refinement [E5-L2-8]) — note the sqrt rate: value-level adequacy confines the shift only to O(sqrt(eps)), and ONLY the gradient-route delta/mu_curv can tighten optimum coverage to the in-class delta scale ([REV2-r2-6](a); superseded clause quoted there). | **delta AND L_H UNDERIVED ([REV2-r4-1](c)) — NO argmax-shift number exists at any grade, and none from the measured carrier alone**: the design-gradient-level residual bound is SCHEMA + named derivers only, and the curvature-transfer residual L_H (H-G6) is likewise SCHEMA + named derivers ([T-RED-2G]; addendum_c4 (b) right-sized), so the helical shock structure can move the TRUE argmax along design directions the reduced functional does not see, and no bound of record excludes it; on a NONCONVEX feasible set — CONNECTED nonconvex included, where branch-wise coverage is undefined ([REV2-r4-2](d)) — global-argmax coverage is NOT claimed by ANY form of this schema — feasible-set geometry, not only delta's underivation ([REV2-r3-1](b), H-G5/R-14). EMPIRICAL MARKERS: the shroud thrust-migration finding = the registered worst-direction marker (channel (iii) WORST cell, Paxson-Miki 58.1% → ~71.5% of ideal at fixed area ratio); second markers grafted at [GRAFT-G07] (P-B flat-vs-peaked, P-C mid-ranking flips, P-A design-point miss (numeral confined to [GRAFT-G07]) — all [ADV], no number enters the schema). A value-level bound is NEVER passed off as optimum coverage (brief :126, binding). | delta/mu_curv = SCHEMA ([T-RED-2G] soundness conditions (1)-(3) + functional identity [REV2-r4-1](a)); mu carrier = MEASURED (J_red Hessians of record; instantiates the J_TRUE floor only UNDER H-G6); delta = UNDERIVED, L_H = UNDERIVED (named derivers only, [REV2-r4-1]); markers [ADV]/[REP] per their rows | [T-RED-2G] derivers in order: five-field content bound (X-T3QS-5F, F2) → C51-route-B → M-RED gradient-measurement rider (centerpiece §3.6, F2) → R22-CFD-1 |

[REV2-r1-17] ANCHOR-NAME NOTE (applied): the (iii) WORST cell's C25
carrier is docs/findings_registry.yaml:2026 (content and line verified
by the L2 refuter; no file named "corrections registry" exists — the
C25 correction text lives verbatim at that line of findings_registry).

[REV2-r1-18] CELL-READING PROPAGATIONS (of record): (a) the (ii) BEST
cell's "single-digit % plausible" is read WITH the good-fitted-sheet
condition restored ([REV2-r1-7] — load-bearing, tested by M-RED leg
(E)); (b) the (iii) rigor column's "sign leg of the debit THEOREM*
([T-DISC-2](i))" is read under the [REV2-r1-2] scope: physical-h0-fixed
/ booking level; the uncompensated DROP branch is geometry-signed with
the r_e = r_in degenerate corner — consistent with the (iii) BEST
cell's own drop-convention clause.

CELL NOTES (grafted per SYNTHESIS_nozzle_rde_arrivals.md §(c)
G-02..G-07, confirm-verified; ALL [ADV]; evidence ceiling D-8/CT-6
BINDING on every line below: mechanism/topology/gap-SCALE readings only
— NO number below enters any bound, band, or cell value of the table
above):

[GRAFT-G02] Channel (i) cell note: P-C Figs. 15/16 clean periodicity =
published realization of the pure-periodic pin class (realization
instance at CFD class ONLY [REV-NRS-8]: CFD-realizability of the pin
class, NOT hardware realism — which is CT-5's actual concern, R20
residue unchanged); P-D choked subsonic chamber = boundary-text support
(coupling received from outside the class). No number moves.

[GRAFT-G03] Channel (ii) provenance: BEST — P-B 2.8% uniform
steady-vs-transient C_fx gap (<=60% trunc) + P-C 0.2-1.5% both-signs
gap = two external single-digit-% instances [ADV]
(cruder-than-per-phase reduction — each an UPPER-class analog, stated).
WORST note: P-B 80% divergence (-5.78%, "flow swirling induces the
trailing shock wave in advance") = configuration-dependent growth
mechanism.

[GRAFT-G04] Channel (iii) cell note: P-B exit V_cir 327-383 m/s =>
eps_theta ~0.17-0.20, swirl angle ~9.7-11.4 deg [INF] — independent
external datum: eps_theta INSIDE the DISPATCH §9 band (0.15-0.20);
swirl angle OVERLAPPING B5's (10-14 deg) LOW EDGE, not inside it (9.7
sits below the floor) [REV-NRS-3]. FILM-COOLING CAVEAT (rides this cell
note) [REV-NRS-3]: every P-B V_cir value is measured on FILM-COOLED
configs (Fig. 24 = the cooling matrix); no uncooled-baseline exit V_cir
exists anywhere in P-B, and the cooling system itself MODULATES the
swirl — the datum remains a valid magnitude-class existence datum
[ADV], scoped "film-cooled configs, cooling-modulated, no clean
baseline". P-C RMSD_theta 8.16-14.63 deg = upper-proxy consistency
only. DEFINITIONAL GUARD (mandatory, STRONGER form [REV-NRS-2]): P-C
eq. 20 (p. 8) = mass-weighted total-flow-angle RMS deviation from axial
— upper-proxy reading defensible [VER-class]; P-B prints NO RMSD
formula anywhere in the paper (nomenclature p. 2: "flow deflection
angle" only) — its meridional-vs-total status is UNDER-DETERMINED at
held evidence. Operative rule, unconditional: RMSD_theta from EITHER
paper is NEVER booked against B5 in ANY direction (neither as swirl
value nor as certified upper bound); the only swirl datum is V_cir.
Swirl-breaker family notes: P-B flat-jet suppression (F-24/F-25,
actuated instance) + swirl-induced early trailing shock (F-11 tail),
beside the registered Paxson-Miki candidate.

[GRAFT-G05] Channel (iv) provenance: BEST — P-D F-6/F-22 (mean efflux =
classic plume; the source claim) + P-A Figs. 9/12 (axisymmetric mean,
no Mach disk in Case C) + A-L1 (exit Mach 2.58 vs 2.69: the ONE
quantified external mean-design-point miss, ~4%) + P-C L16 (time-avg
wall p obeys steady area law) + P-B F-11 (the steady design still
selects a NEAR-OPTIMAL in-band truncation — coincidence of in-band
argmax is at/below Fig. 15 resolution [REV-NRS-9]). WORST — P-C ranking
flip (L11) + P-B transient-only +0.52% invisible on the flat steady
curve — the in-class delta scale (compare our +0.51%, advisory
:828-832). Both cells [ADV]. LANDING RIDER [REV-NRS-5]: executed at
this landing — see the [LAND-C4-LD RIDER] line in the T-T3-MAP context
above.

[GRAFT-G06] Channel (v) notes: P-A base ~0.16 atm bubble topology
(Fig. 12b) + P-C base-zone transient-vs-steady deformation (L8) = base
model-form UNPRICED stands; P-B Chutkey cold-rig base dataset
(Figs. 4-5) = R8-adjacent context that does NOT retire the
nozzleless->plug ANALOGY label (cold annular rig, not an RDE); P-B exit
gamma 1.2500-1.2515 = weak frozen-gamma datum (one-step chemistry: does
NOT test [T-EQBR]); P-D F-12/F-24 = the live instance of model-form
bars dominating absolute values.

[ORCH-HARV-2] ORCHESTRATOR ADDENDUM NOTE, channel (v) cell note
(declared orchestrator addendum — NOT judge text; provenance =
validation/sfoundations_raws_2026-08-13/blocco3/
BASE_PRESSURE_HARVEST_c4.md; all [ADV], CT-6-clean, no number enters
any bound/band/cell): (a) Purdue V1.4 nozzleless CTAP datum — the ONLY
hot-fire RDE base-pressure MEASUREMENT in the read corpus: 5
radially-resolved tests ~0.59 atm at 1.24 kg/s (CTAP cycle-mean, 7
ports, transducer-accuracy error bars); open/closed transition
P_a/P_c ≈ 0.15 with the NPR 4.5-6.7 gap untested; closed-wake
P_b/P_c ≈ 0.08; open wake ~17-20% below ambient (RDE ejector suction).
(b) R8 VACUUM CONFIRMED by the targeted harvest: NO truncated-plug RDE
base-pressure measurement and NO RDE-specific base-pressure correlation
exists anywhere in the read corpus (both Harroun papers state the
negative result verbatim: 2021 p. 669 verdict sentence; 2020 p. 7 "no
way to create an analytical model"); the classical best-of-stack
pure-empirical p_b model carries a [+19%, −15%] error band on cold
measured data (WG10) — the classical model-form floor sitting UNDER
the RDE-specific unpriced bars of this channel.

[GRAFT-G07] Channel (vi) provenance list: P-B Fig. 15 (flat-vs-peaked)
= second empirical marker; P-C Fig. 13 (argmax holds, mid-ranking
flips) = brush instance; P-A Fig. 15b drag tail + 4% miss =
value-adequate yet visibly non-stationary design. All [ADV]; no number
enters the delta/mu schema.

[ORCH-HARV-3] ORCHESTRATOR ADDENDUM NOTE, channel (vi) note (declared
orchestrator addendum — NOT judge text; provenance = validation/
sfoundations_raws_2026-08-13/blocco3/BASE_PRESSURE_HARVEST_c4.md §13;
[ADV]): Humphreys-Thompson-Hoffman 1971 argmax-sensitivity exhibit
(AIAA J 9(8), pp. 1586-1587): swapping the base-pressure closure
Eq. (12) → Eq. (38) moved the optimum base height ×2.45 (0.954 → 2.34
in) and the tip wall slope −13.26° → −3.08° while moving thrust only
+0.26% — the p_b closure moves the ARGMAX at O(1) with the VALUE
nearly flat: a classical, design-level instance of exactly this
channel's mechanism.

BRACKET ROLL-UP (§5.1 of the carrier — honest aggregate; no fake
summation). The channels are NOT independent and are not summed. Seam
declarations: (iii) is a DATA-CONTENT fidelity channel (what the
per-phase functional books from given data) while (ii) is the
REDUCTION channel (what the 2D march drops from the true field) —
B2's booking legs and K's ∂_phi p legs are disjoint by construction
(booking lives in the functional at fixed data; K lives in the field
equations), but both consume the same physical swirl, so a joint
measurement (M-RED families F-c) is the only legitimate aggregator.
Channel (i) is conditional-zero, not zero.
[REV2-r1-19] (vi) SEAM: channel (vi) is an OPTIMUM-adequacy channel,
not a value channel — it is never summed with (i)-(v); it composes
with them only through the delta/mu schema ([T-RED-2G] at the
D.18/[MS-DEF-KRES] site), whose delta consumes the (ii)/(iii)
gradient-level content. The headline below is unchanged: no
argmax-shift number is asserted at any grade.
HEADLINE OF RECORD (the licensed phrasing, nothing stronger):
- BEST: on-ray, corpus-swirl, in-class geometry — the gap is plausibly
  SINGLE-DIGIT PERCENT (on ray-like cycles WITH A GOOD FITTED SHEET —
  M-RED leg (E) tests it; [REV2-r3-7]), with the mean channel exactly
  null (THEOREM*) and the booking debit at the 1.5-3%-of-thrust scale
  [SE].
- WORST: off-ray >10% NOT excluded [SE]; configuration-scale blindness
  is the documented worst DIRECTION — the Paxson-Miki shroud line
  (58.1% → ~71.5% of ideal at fixed area ratio) is bigger than the
  whole area-ratio design line and unexplained; class exits (mode
  transitions, slip sheets, separation) carry NO number of record.
- The bracket TIGHTENS in the program order T-DISC → T-RED → M-RED →
  R22-CFD; nothing else tightens it.

PROTOCOL T3-CONTROL (pre-registered control row of record; class
PRACTICE, rejector-gated per R5; carrier tag X-T3CTRL reserved,
registry entry when the executable lands; S-GAUNTLET 2026-08-11;
full protocol text in the advisory §5 and the T3/T4 synthesis of
record). MANDATORY alongside every future decisive cycle-averaged
optimization or RDE-vs-steady comparison campaign (F5a; F1/F2/F3
campaigns run the applicable subset); no result touching the
coincidence claim is citable without this row's output. DISCHARGE
CORRECTIONS BAKED IN (binding on every use of this protocol): the
row-(a) verdict sentence carries the T-O1 hypothesis list of
T-T3-MAP(a) verbatim; the W2 matched-pressure formula is used ONLY
with its declaring twin construction u_s/T_s := <u_x/T>; the
S18/Harroun sentences carry the corner-reading qualifications of
the T-T3-MAP block above. Registered
inputs, declared BEFORE the run, never after: (1) OBJECTIVE PAIR
J_vac AND J_app (application backpressure; vacuum-only campaigns
must say so and forfeit application claims); (2) THREE DECLARED
MATCHINGS on every steady twin — matched-mdot, matched-<p>, TWIN-C
flux-consistent (TWIN-B prohibited; TWIN-A admitted only as the
labeled zero-swirl reference); on tier-1 data the three MUST
degenerate — non-degeneracy is itself a rejection; (3) BOTH
WEIGHTINGS wherever scaling is broken: ratio-of-averages AND
average-of-ratios; time measure AND mass-flux measure; the
arithmetic-vs-harmonic design-pressure pair reported explicitly;
(4) SUBSONIC-PATCH CLOSURE DECLARED before the run (H3-cl audit
attached, or whole-interface I3 surrogate, or certified
mu(Xi_sub) = 0) — a run with mu(Xi_sub) > 0 and NO declared closure
is INVALID by rule, not "approximate"; (5) SWIRL ACCOUNTING: the
E_theta swirl-KE debit under the through-flow guard, reported beside
the TWIN-C twin. BARS b1-b4 DERIVED per campaign (certificate-stack
evaluation band; propagation through the aggregation formulas;
cov-measurement band from the data contract; priced closure band) —
never reused numeric constants; a corner KAT on a certified tier-1
family is armed BEFORE first decisive use (a row that cannot pass
its own corner KAT is not an instrument). REJECTOR, four limbs:
(i) convention spread beyond its derived bar => tier-1+vacuum set
violated (THEOREM by contraposition), coincidence claim downgraded
or killed per the localization evidence; (ii) matching
non-degeneracy on nominally tier-1 data => run INVALID;
(iii) migrating subsonic patch pattern (H3-cl audit fails) =>
collapse-in-form claims BLOCKED for the data class; (iv) E_theta
beyond scale at claimed twin-equivalence => TWIN-A comparisons
invalid, TWIN-C mandatory. OUTCOMES, both honest and pre-registered:
collapse CERTIFIED (data class and Pa named; never extrapolated —
the S18-corner rule applies forever) OR departure MEASURED
(magnitude +/- bar, attributed to its axis via the fired rejector) —
the second is a POSITIVE program result, reported with equal
prominence. Post-hoc bar widening, post-hoc convention choice, or
silently dropped subsonic phases = protocol violations, not results.

------------------------------------------------------------------------------
[MS] MEAN-SWIRL / FLUX-NULLITY RECORD (landed 2026-08-19,
S-FOUNDATIONS-C Blocco 2 — the §7-item-2 absorption; proof of
record = validation/sfoundations_raws_2026-08-13/phaseD/
phaseD_meanswirl_formalization.md at its r7 state; labels = the
judge labels of VERDICT_phaseD_proofs1 §3.2 with the r2-pass
adjudication applied; provenance: VERDICT_r2pass §3 +
VERDICT_escalation §4 (+ VERDICT_confirm for leg 6). Setting: the
UNSTEADY 3-D inviscid (or shear-declared) lab-frame flow in a
control volume CV bounded by wetted walls Σ_w, an injection/
faceplate boundary S_inj, and cross-sections S(x₁), S(x₂); axial
angular-momentum density ℓ := ρ r u_θ = ρ Γ. ORIENTATION
CONVENTIONS: n is the OUTWARD unit normal of ∂CV everywhere, S_inj
included; τ·n is the traction exerted ON THE FLUID, so
τ_w = ∮_{Σ_w} r (τ·n)_θ dA is the axial torque of the wall ON the
fluid; every signed flux below is stated in this convention.)

HYPOTHESIS BLOCK H-AM (operative clauses verbatim from the staging
doc §3; the r1-r3 revision-history parentheticals are NOT
transcribed — the staging text is of record):
 H-AM0 (unsteady regularity — the function-space hypothesis):
   the unsteady flow is piecewise C¹ on cl(CV) × [0, t_c] — fields
   in L∞, finitely many C¹ moving front hypersurfaces across which
   the unsteady RH conditions hold in the weak form, one-sided
   limits at fronts, and NO energy/momentum concentration on
   lower-dimensional sets (orifice lips, re-entrant CV corners,
   measure-valued fronts): all flux integrands have well-defined
   integrable boundary traces on ∂CV, and L(t) := ∫_CV ρΓ dV is
   finite, CONTINUOUS — absolutely continuous on [0, t_c], so the
   fundamental-theorem step ∫₀^{t_c} L′ dt = L(t_c) − L(0) holds —
   and piecewise C¹ in t (continuity of L is exactly what
   moving-front RH without surface angular-momentum concentration
   delivers, and it is part of the HYPOTHESIS, not folklore).
   AUDIT: H-AM0 is audited by CONCENTRATION tests —
    (i) SOLVER-RESOLUTION SEQUENCE: the flux/torque integrals
    recomputed on the dataset family at increasing SOLVER
    resolution (not quadrature refinement — quadrature refinement
    is a NON-REJECTOR on fixed-resolution data) must be Cauchy in
    the BALANCE residual; divergence ⟹ H-AM0 red;
    (ii) COLLAR SCALING at named suspects (orifice lips,
    re-entrant CV corners): integrals of |ρΓu| over shrinking
    collars must scale with the collar measure — an atom shows as
    scale-independence.
   Where NEITHER test is available (single-resolution data, no
   local refinement), H-AM0 is ASSUMED-PER-DATASET — declared,
   unaudited — and D.6's conditional (c2) must be reported as such.
 H-AM1 (exact T0 periodicity): every field is t_c-periodic at every
   fixed lab point; equivalently the interface/chamber data are in
   the standing pure-periodic scope (T0-flatness monitor green).
   Violation channel: aperiodic storage (mode transitions) — routed
   OUT of this block (an H-AM1 exit, not a torque).
 H-AM2 (inviscid or deviatoric-stress-declared): the deviatoric
   stress is either zero (inviscid model) or its FULL boundary
   angular-momentum moment is DECLARED — physical (molecular) +
   modeled (Reynolds/SGS) + NUMERICAL shear alike — as THREE typed
   budget entries, all in the §3 conventions (traction-on-fluid,
   n outward):
     τ_w      := ⟨∮_{Σ_w} r (τ·n)_θ dA⟩   (wall torque),
     T_S(x)   := ⟨∮_{S(x)} r (τ·n)_θ dA⟩  (cross-plane stress
                 moment, per audited station; integrand r τ_xθ),
     T_inj    := ⟨∮_{S_inj} r (τ·n)_θ dA⟩ (faceplate stress
                 moment).
   AVERAGING TYPE: every entry is the CYCLE MEAN ⟨·⟩ (under strict
   T0 the instantaneous integral is t-independent and the
   distinction vanishes). The RESOLVED fluctuation covariance is
   NOT part of this budget — it lives inside ⟨ρ u_x Γ⟩ itself.
 H-AM3 (axisymmetric wetted geometry): every wetted surface is a
   surface of revolution about the engine axis; non-axisymmetric
   faceplate features (discrete orifices, posts) are explicitly
   disposed of — either excluded via a flush CV at the orifice exit
   planes (admissible declared bookkeeping) or carried as the
   DISTINCT torque channel (1) of D.8 (the default listing of
   record: "purely axial injection" does NOT imply zero boundary
   Γ-flux, and silent folding hides the weakest hypothesis).
 H-AM4 (declared injection flux): the injected angular-momentum
   flux J_inj := −⟨∮_{S_inj} ρ Γ (u·n) dA + ∮_{S_inj} p r n_θ dA⟩
   (n OUTWARD; the minus sign makes J_inj the flux INTO the CV) is
   DECLARED, INCLUDING wave-induced backflow episodes (sign changes
   of u·n within the cycle); J_inj = 0 for the idealized
   axial-injection class with axisymmetric S_inj.
 H-AM5 (no body torque): no azimuthal body force (no MHD, no swirl
   vanes inside the CV).

[MS-T-FLUXNULL] (D.6 — flux nullity / J_inj accounting). THEOREM*.
Under H-AM0–H-AM5, the cycle-averaged axial angular-momentum flux
through every ADMISSIBLE cross-section equals the declared inputs:
  ⟨∮_{S(x)} ρ u_x Γ dA⟩ = J_inj + τ_w,decl(x) + T_S,decl(x)
                          + T_inj,decl
for a.e. station x (admissible = plane transversal to the front set
for a.e. t; at a parked-front station the balance is asserted for
the one-sided limits, which agree by RH normal-flux continuity of
ρΓ), with τ_w,decl(x) CUMULATIVE in x (station-independence is a
COROLLARY of the inviscid limb only). In the idealized class
(inviscid, J_inj = 0):  ⟨∮_{S(x)} ρ u_x Γ dA⟩ = 0 — the
area-integrated, MASS-FLUX-WEIGHTED cycle mean of Γ vanishes
exactly at every admissible station. WHY THEOREM* (named
conditionals): (c1) the ASSEMBLED-BALANCE symbolic check is QUEUED
(gap G-a) — the geometric kernel ([T-SLRW]) and the local
conservation identity are machine-verified, the assembled CV
balance is a pen derivation independently reproduced by all four
panel positions; (c2) H-AM0 — a MATHEMATICAL regularity hypothesis,
audited per dataset by the concentration tests, else
ASSUMED-PER-DATASET, never provable in the abstract. No physical
conditional beyond H-AM0–H-AM5 remains. Gamma status: EOS-FREE.
Falsifier (panel F1): on one periodic chamber-CFD dataset (≥2
stations), A1(x) = ⟨∮ ρ u_x Γ dA⟩ normalized by the gross flux
⟨∮ |ρ u_x Γ| dA⟩; refuted if |A1 − J_inj − τ_decl − T_S,decl −
T_inj,decl| exceeds a DERIVED tolerance.
 Rmk 3.1 (instantaneous form under strict T0). THEOREM. For a PURE
 rotating wave, L(t) = ∫_CV ρΓ dV is CONSTANT in t, so the balance
 holds at EVERY instant (J_inj read instantaneously; the two
 readings coincide under strict T0). EOS-FREE. Falsifier: a
 strict-T0 dataset on which L(t) varies beyond derived quadrature
 bars.
[D.7] (non-channels — the THEOREM-level negative). THEOREM* (same
conditionals as D.6, its contrapositive reading). Under H-AM0–H-AM5
no interior dynamics and no axisymmetric-surface mechanism can
source net axial angular momentum: unequal wave counts,
counter-rotating admixture, deflagrative asymmetries, throat
convergence are NON-channels. "Wave-count asymmetries" must never
be listed as a net-swirl mechanism. EOS-free. Falsifier: D.6's,
restricted to a dataset realizing the named mechanism with all
H-AM hypotheses audited green.
[D.8] (torque-channel census). DEFINITION + THEOREM*
exhaustiveness OVER {¬H-AM0..¬H-AM5}: (0) regularity breakdown
(¬H-AM0 — concentration; breaks the accounting itself);
(1) non-axisymmetric wetted geometry (¬H-AM3 — DISTINCT channel of
record, never folded into (3); generically NONZERO in real
hardware); (2) boundary deviatoric stress — wall torque AND
cross-plane/faceplate stress moments (¬H-AM2; any dissipative
dataset audits to its declared moment SUM, not to zero);
(3) swirled/non-axial injection and backflow Γ-exchange (¬H-AM4 —
the physically weakest hypothesis); (4) aperiodic storage (¬H-AM1
— an exit, not a torque). EOS-FREE. Falsifier (panel F4, channel
(1)): one wave passage over a discrete-orifice faceplate;
engine-axis pressure torque zero within derived tolerance REFUTES
the distinct channel.
[MS-T-MEASURE] (D.9 — measure identities). (i) THEOREM
(product-L¹ integrability class): ⟨u_θ⟩ = ⟨u_θ⟩_ṁ −
cov(ρ u_x, u_θ)/⟨ρ u_x⟩; with D.6 (J_inj = 0) the INTEGRATED
consequence ∮⟨ρu_x⟩⟨Γ⟩ dA = −∮ cov(ρu_x, Γ) dA — ONE scalar per
cross-section; the pointwise reading "nonzero wherever cov ≠ 0"
does NOT follow. (ii) THEOREM under strict T0: time mean at a
fixed point = phase mean (μ of D2.3) = frozen-t azimuthal mean
(the Z_n cell-sweep step: "n identical waves" means Z_n-invariance,
so the fundamental-cell mean equals the S¹ mean). (iii) DEFINITION/
discipline: the program's μ is a TIME measure, NOT the mass-flux
measure constrained by D.6 — every swirl statement NAMES its
measure (T3-CONTROL input (3)). EOS-free. Falsifier (panel F2):
⟨u_θ⟩ field + A2 ≈ −A3 within derived bars.
[MS-T-SKE] (D.10 — swirl-KE flux). THEOREM (positivity +
unconstrainedness): E_θ := ⟨∮_S ρ u_x u_θ²/2 dA⟩ > 0 strictly on
any station with through-flow ρ u_x > 0 a.e. and u_θ ≢ 0, and E_θ
is NOT constrained by D.6 under ANY measure (θ-halves-at-each-
radius exhibit: Γ-flux cancels r-fiberwise with E_θ arbitrary).
First-order weight = measured record (σ/μ ≈ 0.70 ⇒ (σ/μ)² ≈ 0.5).
PRACTICE twins (binding, T3-CONTROL inputs (2)/(5)): TWIN-A
(zero-swirl) fair at the net-flux level ONLY — misattributes the
E_θ debit (unrecoverable WITHIN the vaneless axisymmetric nozzle
class of record — scope statement, N6-2 note), the radial-
equilibrium pressure shift, the covariance wedge (D.9(i)), and the
closure/margin class (D.5(iii)); TWIN-B REFUTED as fair; TWIN-C
(flux-consistent) is the fair twin of record. EOS-free. Falsifier
(panel A4) WITH THE NORMALIZATION PINNED (pin B-1, VI.1): A4 is
the KE-NORMALIZED swirl-KE flux fraction; the corpus "3-6%" figure
is KE-normalized, the h0-normalized reading is ~4x smaller
(0.3-2.5%); the falsifier must NEVER fire on a unit mismatch
(discriminating test: only the KE reading gives Ωr ≈ D_CJ).
[LAND-C4-LF RECONCILE FLAG to the D.10 row owner (VERDICT_r22f §4
forwarded note L2-10 / §7 L-F, 2026-08-20): the row's "~4x smaller
(0.3-2.5%)" sits in internal tension with its own nominal arithmetic
— ~4x of 3-6% = 0.75-1.5%; judgeverify computed 0.45-2%. Record-side
blemish flagged for reconciliation by the row owner; no grade moves;
the R22F centerpiece cites this row faithfully as printed.]
[D.11] (covariance sign). CONJECTURE — lands at the lowest class:
on in-scope RDE chamber data cov(ρu_x, u_θ) > 0 wave-ward, hence
by D.9(i) the plain time-mean swirl is net COUNTER-wave. EOS-free.
Falsifier (panel F3): sign(A3) on the first dataset (awaits G-e).
[D.12] (prohibition). PRACTICE. The statement "the time-mean
interface state carries net Γ ≠ 0, a first-order omitted
mean-field term" is REFUTED of record at the flux level and must
NEVER be asserted by this program; the folk statement "the mean
flow has no swirl" is EQUALLY unavailable (no time-mean tangential
field is reported anywhere in the read corpus — empirical vacuum
of record; falsifier: exhibit one).
D.18 CROSS-REFERENCE (compact — DOC-2 GUARD: the
over-certification counter on D.18 material stands at FOUR of
record; nothing here states a strength above the in-line grades):
[MS-DEF-KRES] / [T-RED] REDUCTION-RESIDUAL OPERATOR — TRANSCRIBED OF
RECORD (S-FOUNDATIONS-C4 landing 2026-08-20).

[LAND-C4-LB LANDING HEADER] Executes VERDICT_r22f §7 L-B (+ the L-D
pointer) as amended by VERDICT_escalation_c4 LA-5. Carrier of record:
validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece
.md Part 2 + §2.2-bis AT CLOSURE (grades per VERDICT_r22f §1, single
label authority; centerpiece labels UNCHANGED by the E-5 pass,
VERDICT_escalation_c4 §5.5). REPLACEMENT DECLARED per the verdict's
explicit order: the previous compact pointer of this block —
superseded fragment, verbatim: "[MS-DEF-KRES] (the reduction-residual
/ commutator terms K) is OF RECORD in the staging doc at its r7
state, NOT transcribed here. Labels: DEFINITION (distributional form)
+ SCHEMA completeness (gap G-f) + BOTH iff clauses SCHEMA (judge
downgrades J-r2p-2/J-r2p-3; escalation E-3 CLOSED at these labels per
VERDICT_confirm leg-6, with amendments AM-1..AM-3 of record against
the staging text). Restoration of the iffs ONLY via the G-f battery
(owner: carrier upgrade window, commit-gated)." — is REPLACED by this
transcription; the G-f/iff-restoration rule and the DOC-2 guard
STAND unchanged (census completeness stays G-f SCHEMA; iff clauses
SCHEMA; restoration only via the G-f battery). READING RULE (binding,
[REV2-r1-21]/[REV2-r2-8]/[REV2-r3-10]/[REV2-r4-6]): superseded
fragments quoted inside marker blocks below are historical record and
govern nothing; the corrected forms are the sole text of record.
ROUND-4 DELTA STATUS (executes LA-5(ii); the RES-CAP-1
"round-4 delta unrefereed" declared line is RETIRED and REPLACED by):
round-4 delta refereed (E-5 targeted pass of record,
esc_refute_r4delta_l{0,1,2}.md, 0 BREAK; [ESC-E5-1/2/3] applied;
deferred inputs executed at this edit per VERDICT_escalation_c4 LA-5).
CROSS-POINTER (L-C): channels (ii)/(vi) quantified face: see
[R22F-FORCHETTA], Part III.
M-RED POINTER (L-D): Residual-functional measurement spec (M-RED,
bands B-1..B-4, F2 execution): centerpiece Part 3, of record. (F2
duty registered per VERDICT_r22f §7.2 row (3), registry-side.)
K-BAR = 0 MINT (R-6 — EXECUTES HERE): the K-bar = 0 mean-nullity leg
is MINTED AT RECORD GRADE at this landing (THEOREM*: pen proof +
machine witness; holds on full BV — a.c. + Cantor + atoms). The
ADVISORY-provenance conditional (c3) of [T-DISC-1] and the carrier
§2.2(i) provenance line ("ADVISORY provenance pending R4 landing")
are RETIRED in this same edit.
SYMBOL BINDING AT THIS SITE (executes the landing rename
[REV2-r2-3](C) as amended by [REV2-r4-1](a) and E5-L1-4 — two
symbols, never one): mu_curv := the schema's curvature floor of
J_TRUE (gradient route; the measured carrier instantiates it only
UNDER H-G6); mu_red := the measured J_RED curvature floor (value
route, carrier-as-is per [REV2-r4-1](d)). The S20 margin MULTIPLIER
mu (KKT-with-margin-multiplier block, Part VI) is a DISTINCT object
never referenced by this section. The renames are executed in the
text below at every printed bound; "mu" survives only inside quoted
superseded fragments and in the forms' own subscripted floors
mu_T/mu_C (both instances of mu_curv on their cones).

[T-RED-1] THE OPERATOR, EXPLICIT AND EXACT.
DEFINITION (grade DEFINITION; identities THEOREM* — pen algebra
independently verified with sympy witnesses; distributional form is
this [MS-DEF-KRES] of record). Let
U = (rho, rho u, rho v, rho Gamma, rho E) and let the lab azimuthal flux
be F_theta(U) = (rho w, rho u w, rho v w, rho w Gamma + r p, (rho E + p) w).
The wave-frame azimuthal flux is EXACTLY
  F_phi,rel(W) = F_theta(U) − Omega r · U
              = (rho w_rel, rho u w_rel, rho v w_rel,
                 rho w_rel Gamma + r p, rho w_rel h0 + Omega r p)
(row-for-row identity, energy row rho E w + p w − Omega r rho E =
rho h0 w_rel + Omega r p: judgeverify ITEM 3.1, sympy PASS). The
reduction-residual operator is
  K(x, r, phi) := (1/r) ∂_phi [ F_phi,rel( W(x, r, phi) ) ]
in the distributional sense, and the per-phase-2D
reduction solves the K-DROPPED system: the azimuthal-structure terms
dropped by the reduction are EXACTLY the six advective rows + front atoms
of K (residual census: swirl5f claim 2 — PROVEN-HERE at advective level
by 3 independent derivations, in-panel; RECORD STATUS: div-form
completeness remains gap G-f SCHEMA, iff clauses SCHEMA — grades
NOT inflated here; the sixth drift piece (w/r)∂_phi h0 included per
repaired census, judgeverify §5.1).
Equivalent-form identities of record (both exact, judgeverify §5.4):
r·R_theta^(B) + Omega r^2 · K_rho = R_Gamma^(A) and
R_E^(A) − Omega·R_Gamma^(A) = (1/r) ∂_phi (rho w_rel I), I = h0 − Omega Gamma.
HYPOTHESIS LIST (operator level): H-RED-1 post-[T-T0P] quotient valid
(inherits the FULL split gap lists: stratum (A) G1+G2+G7+G8 under H8'/H9
with G5 the named lift and G4 the tilted-interface branch; stratum (B)
additionally G3+G11+G9 — cited, owned there, not re-litigated); H-RED-2
W in the periodic BV composite class in phi (bounded S1 fields, finitely
many front crossings per period); H-RED-3 conventions: J1^K = St·J1^ledger
normalization chain pinned (judgeverify ITEM 3.2, exact convention-pin;
the F-5 hazard resolved by S_sweep := K/St); H-RED-4 (J)/(H) channel
values read under the a.c.-only/psi-bar-pairing pin (convention-dependent
split, necessity verified: judgeverify ITEM 3.3 tail).
[REV2-r1-6] H-RED-2 STRENGTHENED (fixes R22F-L2-5; AG-1 valve:
sufficient-not-optimized, trivially checkable on the intended class):
H-RED-2 now reads — W piecewise-a.c. in phi, i.e. SBV composites
(a.c. part + finitely many atoms, NO Cantor part). Rationale: BV
admits a nonzero Cantor part (bounded + finitely many jumps does not
imply SBV), which the two-channel census would leave unowned:
on a BV-with-Cantor field a THIRD first-order channel exists and
belongs to neither (J) nor (H). The intended piecewise-smooth-fields-
with-fronts class is SBV trivially. The "exactly TWO first-order
channels" claim and the rigor line are conditional on this SBV clause.

[T-RED-2] BOUND SCHEMA.
(i) MEAN NULLITY — THEOREM* (pen proof + machine witness; MINTED AT
RECORD GRADE at this landing, R-6 — the carrier's "ADVISORY provenance
pending R4 landing" line is retired): K-bar = 0 fiberwise
UNCONDITIONALLY on periodic BV composites — the distributional
phi-derivative of a periodic BV function has total signed mass zero
over a period, a.c. + Cantor + atoms included (judgeverify ITEM 3.3).
CONSEQUENCE: the reduction residual has NO mean-field first-order
channel; exactly TWO first-order channels survive in J:
  (J) the atom/jump pairing  <psi-bar, atom content>, and
  (H) the a.c. covariance/hysteresis channel  −Cov^{ac}(psi, K),
(swirl5f claim 9, mixed grade of record: channel structure verified,
BOUNDS OPEN — C-T1). Magnitude status of record, licensed phrasing
with the FITTED-SHEET condition restored ([REV2-r1-7], verbatim at
source): "single-digit-% total PLAUSIBLE on ray-like sawtooth cycles
WITH A GOOD FITTED SHEET; >10% NOT EXCLUDED" off-ray —
SCALING-ESTIMATE class; the fitted-sheet qualifier is load-bearing
(exactly what M-RED leg (E) tests).
[REV2-r2-2] SITE POINTER: the "exactly TWO first-order channels"
clause above is read under H-RED-2(SBV) per [REV2-r1-6] — on a
BV-with-Cantor field a third first-order channel would exist; the SBV
clause excludes it by hypothesis.
(ii) FIRST-ORDER SCALES (all SCALING-ESTIMATE, labeled; verifier-repaired
forms only): first-order coefficient scale Lambda = 0.59-1.11·St_n
(R-C corrected band); pressure-work term order a_p·St_n·beta_w with
beta_w = p/(rho h0) in [0.091, 0.160] envelope => 0.007-0.09 (judgeverify
ITEM 1.1); dimensionless spine chi = Omega Gamma / h0 = 0.06-0.20
(verifier-confirmed band), exact EOS-free closure chi·beta_tau = beta_w
(STRONGER than printed — definition-level identity, judgeverify ITEM 1.1);
spike-core band r_core/R_int ≳ sqrt(eps_theta·chi/2) ≈ 0.065-0.14 (R-A
corrected; the printed 0.10-0.19 REFUTED for the record class).
(iii) ON-RAY IMPROVEMENT — LICENSE-GATED (not usable): the St_n^2 on-ray
cancellation (claim 3, H3-w) is PROVEN in-panel but LICENSE GATED on the
committed X-T3QS 5F battery (F2 duty). Until it lands: the J1 bar is
COMPUTED on swirl data, never argued away (DISPATCH §3 row 3 gate,
binding here).
(iv) UNIFORMITY — OPEN twice over ((U) + class-wide H-A1), decided by
the S.22 shock-free sub-scope theorem (F2) + measured eps (M-RED/O5-lite).
RIGOR LINE ([REV2-r2-4] form of record): operator definition
DEFINITION (exact identities THEOREM*, machine-witnessed); census
completeness G-f SCHEMA; K-bar = 0 THEOREM* (minted at record grade,
R-6); two-channel reduction THEOREM* conditional on
H-RED-2(SBV)/H-RED-3/H-RED-4; all magnitudes SCALING-ESTIMATE,
labeled; uniformity OPEN ((U) + H-A1); time-coupling
G3/corrector-owned, boundary named (the [T-RED] seam is the
AZIMUTHAL-STRUCTURE half only; aperiodic/mode-transition content is
an H-AM1 class EXIT, not a K term).

PER-TERM DISPOSITION (of record; [REV2-r1-9/10] corrected readings):
| K term (census of record) | Mechanism (ray family) | Disposition |
|---|---|---|
| sweep-advective rows: K_u, K_v, K_s + sweep parts of K_rho, K_Gamma, K_h0 (incl. sixth drift (w/r)∂_phi h0) | phase-lag on advective helix | mean of TOTAL K null (joint; no per-row nullity claimed — [REV2-r1-9]); first-order J-effect via (J)/(H) — magnitude MEASURED by M-RED (bands B-1/B-2); on-ray St^2 improvement deferred to X-T3QS-5F license (F2) |
| pressure-torque/work legs: ∂_phi p in K_Gamma, K_h0 | amputated azimuthal aperture of the acoustic cone (swirl generation + wave work) | order-estimate (a_p·St_n·beta_w = 0.007-0.09, SCALING-ESTIMATE); structure deferred to C51-route-B / S-5F (route B treats helical sheets natively); magnitude MEASURED by M-RED |
| front atoms (fitted-sheet jump content) | (J) channel; azimuthally-fed segments unreachable by the march (row 13 pin) | mean channel dead only JOINTLY with the a.c. parts (K-bar = 0, THEOREM*, SBV class); the atoms' own signed mass books into (J) ([REV2-r1-9]); J-pairing <psi-bar, atoms> MEASURED by M-RED protocol leg (E) (fitted-sheet ON/OFF); E5 magnitude DISPUTED-OPEN (needs measured Delta x_s standoff modulation — named decider); native treatment deferred to C51-route-B |
| separation / viscous content of the exhibit | outside inviscid class | NOT a K term — boundary named (separated-phase monitor, T-T3-MAP(a)); no bound asserted |
[REV2-r1-10] PER-INSTANCE CARRIAGE + D-4 GUARD: the exhibit-family
CONNECTION ("this IS the phenomenon class K carries") is SCOPED to the
K-CARRIED SUBSET of the [GRAFT-G01] exhibit family (carrier §2.3, of
record; all [ADV], mechanism/topology only, CT-6/D-8 unchanged):
P-A banded ramp footprint -> advective-helix rows (D-2 class); P-A
REFLECTED shocks -> D-4 family: chamber-side, upstream of the
interface — NOT K terms (D-4 misfiling guard verbatim: "do not misfile
as K terms"); bears on CFD-1 coupling and must be declared in/out of
the interface hypothesis (H3 class membership) at M-RED/CFD-1 time;
P-B sweeping oblique wave -> advective-helix rows (D-2); P-C one-sided
internal shock -> front-atom row; P-C deformed base ->
separated/boundary row; P-D rotating front + oblique shock + triple
point -> front-atom row; P-D choked-panel UPSTREAM azimuthal content
-> D-4 family, NOT a K term (chamber-side coupling, CFD-1). The
physical exhibit of record (Harroun 2021 Fig. 18, printed p. 669,
page-verified) lives in carrier §2.3 as restored by [REV2-J1].
FALSIFIERS ([T-RED] block): (f1) a periodic BV composite with nonzero
fiberwise K-bar (kills (i) — machine witness exists against it); (f2)
O5-lite leg (D) exponent 1 on a smooth on-ray cycle (kills the carrier
assumptions of the two-channel frame); (f3) distributed O(1) mismatch in
leg (C) outside the jump window (kills (J)-localization); (f4) a computed
5F gradient contradicting the mechanism-to-ray map's sign structure on
the migration family (the claim-7 deciding instrument).

[T-RED-2G] DESIGN-GRADIENT-LEVEL BOUND SCHEMA (§2.2-bis of the
carrier, AS AMENDED THROUGH [REV2-r4-1/2/3] AND the E-5 deferred
inputs executed at this landing; grade SCHEMA; form per addendum_c4
(b): honest SCHEMA + named derivers, closed form NOT claimed and NOT
demanded).
OBJECT (grade SCHEMA). On the admissible profile manifold (design
space of record, segmented TR-Newton parameterization), let J_red be
the reduced (per-phase-2D) functional and J_true the post-quotient
wave-frame functional. The DESIGN-GRADIENT residual is
  delta(S) := || P_T(S) [ grad J_true(S) − grad J_red(S) ] ||_{M*}
with P_T = projection on the feasible directions (critical cone at the
active set) and ||·||_{M*} the DUAL norm of the design-space metric M
in which the engine curvature is an eigenvalue (metric NAMED —
condition (3) below) [ESC-E5-1: at-site identity bracket, applies
REPAIR E5-L1-1(i) (esc_refute_r4delta_l1.md) — mu_curv = the J_TRUE
floor, [REV2-r4-1](a); the engine (measured-carrier) curvature
instantiates it only UNDER H-G6, [REV2-r4-1](c); the metric-naming
function of this sentence is unchanged].
STRUCTURE (bound schema): by the adjoint representation the gradient
gap inherits the residual operator: grad J_true − grad J_red =
<psi_S, K(W_S)>-type pairings + front-sensitivity terms, so delta
decomposes along the SAME channels as the value level —
  (J)-gradient content: <∂_S psi-bar, atom content> + <psi-bar, ∂_S
  atoms> (front-atom design sensitivity — the g2b/contact-crossing
  calculus class, F2; the Breitkopf-Ulbrich reference-space template
  is the named candidate instrument, retained as a named F2 candidate,
  not consumed);
  (H)-gradient content: ∂_S Cov^{ac}(psi, K).
HYPOTHESES: H-G1 = H-RED-1..4 incl. the SBV clause ([REV2-r1-6]);
H-G2 adjoint field psi_S exists and is regular on the B-4 registered
window with the per-family DOMAIN-margin floor (marched-domain min
margin per [REV2-r2-5](a), not entry-only); H-G3
differentiable-front regime — no crossing events inside the
perturbation ball (else the g2b calculus owns the term; named exit,
not silent).
WHAT DERIVES delta (the three named derivers, brief order, verbatim
class): (1) five-field content bound (X-T3QS-5F battery, F2) — would
bound the (H)-gradient channel on-ray; (2) C51-route-B (native
helical-sheet treatment) — would bound the front-atom sensitivity
structurally; (3) M-RED GRADIENT MEASUREMENT — named F2 duty RIDER on
the carrier §3.6: gradient of legs (A)-(B) along the design sweep,
evaluated in the measured Hessian's own parameterization.
STATUS (honest): NO closed-form gradient bound is derivable at current
record (the value-level magnitudes are themselves [SE]); this schema +
the named derivers IS the deliverable at this rigor class (addendum_c4
(b): an acceptable dry outcome; label inflation forbidden both ways).
SOUNDNESS CONDITIONS (these BIND the [R22F-FORCHETTA] (vi) row):
(1) BASIN CLAUSE: the perturbation bound |argmax shift| ≤ delta/mu_curv
is the strongly-concave argmax-shift lemma; mu_curv must be a curvature
FLOOR (smallest reduced-Hessian eigenvalue) of J_TRUE — functional
identity declared, [REV2-r4-1](a) — holding UNIFORMLY on a
neighborhood containing the shift ball. The segmented TR-Newton
curvature of record is POINT-measured: it licenses only the
A-POSTERIORI form — valid IF delta/mu_curv ≤ the certified basin
radius, and the check is stated as part of any cell that uses it.
(2) CONSTRAINED FORM: at an active-set optimum, the floor = reduced
Hessian on the critical cone and delta = the PROJECTED design-gradient
residual norm (feasible directions only); multiplier/margin shifts
priced per the KKT-with-margin-multiplier formalization of record
(S20 ladder — read per [REV2-r2-3](D): naming the stationarity
STRUCTURE only, no perturbation/stability theorem). An
unconstrained-form cell at a constrained S* would overclaim.
(3) METRIC CONSISTENCY: delta is measured in the dual norm of the
SAME design-space metric in which the floor is an eigenvalue;
otherwise delta/mu_curv is not norm-invariant and any cell number is
meaningless. The metric is named wherever the ratio is quoted.
[REV2-r2-3] SOUNDNESS-CONDITION REPAIR + TYPING + CARRIER SPLIT +
VALUE-ROUTE LEMMA (of record):
(A) CONE-PAIRING RULE: the argmax-shift schema licenses
EXACTLY TWO forms, and in each the residual delta and the curvature
floor are taken on the SAME cone — never curvature on the small
(critical) cone with residual projected onto that same small cone
while the shift explores the large (tangent) one (probe
r22f_v2_probe_r2_l0_activeset_shift.py of record: 500x violation and
an unbounded-violation variant under exactly that pairing):
  (T) TANGENT-CONE FORM (unconditional on convex feasible sets):
  mu_T = the curvature floor of J_TRUE ([REV2-r4-1](a)) over the
  TANGENT (feasible-direction) cone on the certified ball; delta_T =
  the residual measured on the SAME cone (support-function form, (B)
  below). Strong monotonicity / the VI argument give |argmax shift| ≤
  delta_T/mu_T with NO active-set hypothesis. Cost: mu_T degrades
  to the smallest feasible-direction curvature.
  (C) CRITICAL-CONE FORM (sharper floor, license-gated): mu_C = the
  critical-cone reduced-Hessian floor of J_TRUE ([REV2-r4-1](a))
  and delta_C on the SAME critical cone are licensed ONLY under the
  MULTIPLIER-MARGIN CLAUSE: every active-constraint multiplier ≥ its
  NAMED margin against the perturbation (the Bonnans-Shapiro-class
  strict-complementarity active-set-stability regime) — the clause is
  part of the a-posteriori check list wherever this form is quoted,
  alongside condition (1)'s basin check.
(B) TYPING: the sound reading of the delta definition, DECLARED, is
via the M-Riesz map — identify the gradient gap g with M^{-1}g,
project M-orthogonally onto the cone, measure in ||·||_M —
equivalently, by the Moreau decomposition, the support-function form
  delta_cone := sup { <g, d> : d in cone, ||d||_M ≤ 1 },
which is the form the VI argument of (A) consumes directly and makes
the cone-pairing rule automatic (delta and the floor name the same
cone by construction).
(C) SYMBOL + SIGN HYGIENE (EXECUTED at this landing — see the SYMBOL
BINDING paragraph above): the schema's curvature symbol at this site
is mu_curv (gradient route, J_TRUE floor) with mu_red the value
route's measured J_red floor (E5-L1-4 split); the S20 margin
MULTIPLIER mu is a distinct object. Sign convention, declared: for
concave J the floor is the smallest eigenvalue of −H_reduced
(equivalently |largest eigenvalue of the negative-definite
H_reduced|) — strictly positive; "smallest reduced-Hessian
eigenvalue" is always read in this convention.
(D) SCHEMA OBJECT vs MEASURED CARRIER + O1 GATE: the SCHEMA object is
the curvature floor per (A) (form (T) or (C)); the MEASURED CARRIER
of record is the segmented TR-Newton curvature in the driver's
parameterization (S18/S24 lineage, Hessians of record). The carrier
instantiates the schema object UNDER H-G6 (mu_eff = (mu_meas − b_E) −
L_H, [REV2-r4-1](c) as completed by E5-L2-2) at an interior /
margin-inactive S* — never flatly; the engine's Hessians of record
are Hessians of the REDUCED (coded, per-phase-2D) functional, and the
engine has never computed J_true (the premise of R22 itself)
[superseded fragment, verbatim: "The carrier INSTANTIATES the schema
object at an interior / margin-inactive S* (the F1/S22-S24
margin-inactive instances are exactly this case)." — never lands
flat]. At a MARGIN-ACTIVE S* — the record's own measured-supported
hypothesis for the current engine optimum — the active multiplier,
hence the critical cone and the reduced Hessian ON it, are NOT yet
defined objects of record: OBLIGATIONS LEDGER O1 (Danskin/Clarke cusp
derivative; until discharged the margin-active KKT is B-stationarity
ONLY). The critical-cone identification of the measured carrier is
therefore O1-GATED. New hypothesis line:
  H-G4: at a margin-active S*, form (C) (and any critical-cone
  reading of the measured carrier) is available only AFTER O1
  discharges; until then only form (T) with the tangent-cone floor
  is licensed there — UNDER H-G5 ([REV2-r3-1]; the feasible-set
  hypothesis is carried at every licensing site, never flat: at the
  margin-active S* the H-G5 status of the KS-aggregated margin set
  is OPEN and declared, residue R-14).
(E) BASIN-RADIUS DERIVER NAMED: the a-posteriori check of condition
(1) needs a certified basin radius; its deriver is NAMED — a
curvature re-measure ladder on balls around S* in the engine's own
parameterization, run as a cheap extension of the M-RED
gradient-measurement rider (carrier §3.6, F2), with radius = the
largest ball on which the measured floor sustains its value within
its own band. Residue R-12 carries it.
(F) VALUE-ROUTE ARGMAX-SHIFT LEMMA (SCHEMA; probe
r22f_v2_probe_r2_l2_value_grad_gap.py of record — bound verified on
50 random + 4 adversarial families, rate shown TIGHT): under a
uniform VALUE-error premise on the certified basin (a (U_G)-type
premise; measured instantiation per [REV2-r3-3] [at [REV2-r4-3]
SAMPLED-SUP (estimate) class — E5-L0-3(b)/E5-L2-5 at-site bracket] —
the sweep-sup of the M-RED value legs (A)-(B) along the design sweep,
NEVER a single-family point eps), the feasible-set hypothesis H-G5
([REV2-r3-1]), and a curvature floor mu_red [for THIS route
legitimately the MEASURED carrier (a J_RED floor) as-is — the
J_red-side derivation, [REV2-r4-1](d)], |argmax shift| ≤
2·sqrt(eps_U/mu_red). The rate is Theta(sqrt(eps)): value-level
adequacy alone confines the shift only to O(sqrt(eps)) —
sqrt(single-digit-%) is NOT the in-class design-delta scale in
curvature-normalized units. ONLY the gradient-route delta/mu_curv
(this section's schema, derivers named) can tighten optimum coverage
to the in-class delta scale. This lemma is what the [R22F-FORCHETTA]
(vi) BEST cell quotes; it consumes only already-named quantities
(measured carrier per (D); eps_U per the [REV2-r3-3] sweep-sup
instantiation at [REV2-r4-3] class) and demands no gradient bound
(addendum_c4 (b) respected). The one-line derivation of record:
J_red(x1) − J_red(x2) ≥ (mu_red/2)·shift², then 0 ≤ J_true(x2) −
J_true(x1) ≤ 2·eps_U − (mu_red/2)·shift² — so (F)'s floor is
LEGITIMATELY the measured carrier as-is, making the value route the
ONLY route of this schema executable on the measured carrier today.
The two routes' floors (mu_curv vs mu_red) are DISTINCT objects and
are never treated as one.
[REV2-r3-1] FEASIBLE-SET HYPOTHESIS H-G5 + LICENSING CARRIAGE (probe
of record r22f_v2_probe_r3_l0_nonconvex_feasible.py: on a nonconvex
two-branch feasible set BOTH licensed routes fail unboundedly while
every other printed check PASSES; convex control tight; nonconvexity
isolated as the sole killer):
(a) HYPOTHESIS LINE (beside H-G1..H-G4; AG-1 valve: strong,
trivially checkable where checkable, sufficient-not-optimized):
  H-G5 ([REV2-r4-2](a) form of record, with the E5-L0-1/E5-L2-4
  star-shapedness wording executed at this landing): the feasible set
  intersected with the certified ball is CONVEX (sufficient, and the
  property the arguments consume: the segment between S*_red and
  every point of the shift ball feasible — star-shapedness about
  S*_red; convexity implies it, not conversely [superseded fragment,
  verbatim: "(equivalently: the segment between S*_red and every
  point of the shift ball feasible;" — the false "equivalently" never
  lands]; locally convex admissible via Tietze–Nakajima (for a closed
  connected set, locally convex ⇒ convex — classical)) — declared and
  checked per instance; trivially checkable for box/linear design
  constraints; the prox-regular disjunct is WITHDRAWN as a licensing
  branch (retained only as the named F2 curvature-corrected
  refinement, R-17); for the KS-aggregated fold-margin set at a
  margin-active S* its status is OPEN and says so (named beside
  O1/R-13; residue R-14).
RATIONALE: the VI/strong-monotonicity argument behind form (T) and
the strong-concavity argument behind the value route (F) each consume
segment feasibility between the two argmaxes. H-G5 is carried at
EVERY licensing site: (T)'s definition, H-G4, R-13, the (F)
hypothesis list, and the (vi) cell check list.
(b) CONSTRUCTIVE COVERAGE REMARK: global argmax migration across
feasible components / nonconvex lobes is a VALUE-comparison event,
not a gradient event — it IS coverable by branch-wise application of
the licensed forms plus a cross-branch value-dominance margin >
2·eps_U (M-RED's own measured quantity under the [REV2-r3-3]
instantiation). Absent that check, global-argmax coverage on a
nonconvex feasible set is NOT claimed by ANY form of this schema.
[TAIL, [REV2-r4-2](d): the branch-wise route is defined ONLY where a
component/branch decomposition exists (disconnected feasible sets —
there the 2·eps_U dominance constant is exact); on a CONNECTED
nonconvex set no lobe-decomposition rule is declared and branch-wise
coverage is UNDEFINED — no global-argmax coverage is claimed there by
any form.]
[REV2-r3-2] EVALUATION-POINT PIN: in the support-function form
delta_cone of (B), g AND the cone are evaluated at the COMPUTED
REDUCED OPTIMUM S*_red — the only computable choice, and exactly what
the form-(T) VI chain consumes; the bound then reads
||S*_true − S*_red|| ≤ delta(S*_red)/mu_curv [ESC-E5-1: at-site
identity bracket, applies REPAIR E5-L1-1(ii) (esc_refute_r4delta_l1
.md; also discharges AMENDMENT E5-L0-3 limb (a), same site) —
mu_curv = the J_TRUE floor, [REV2-r4-1](a); measured-carrier
instantiation only UNDER H-G6, [REV2-r4-1](c); this printed bound is
the gradient route and licenses NO number until L_H lands (R-16)]. A
future M-RED gradient-rider executor evaluates delta at S*_red and at
no other point.
[REV2-r3-3] eps_U INSTANTIATION OF RECORD (the withdrawn "=" identity
never lands): eps_U is the UNIFORM value-error level on the basin the
shift explores; its measured instantiation = the SUP over the M-RED
value legs (A)-(B) sampled ALONG THE DESIGN SWEEP of the §3.6
gradient-measurement rider (sweep coverage declared per family). A
single-family eps does NOT discharge the premise; until the sweep sup
is measured, the uniformity premise is OPEN and DECLARED [READ UNDER
[REV2-r4-3]: measurement instantiates at declared class, never
discharges — E5-L0-3(b)/E5-L2-5 at-site bracket]. A-POSTERIORI CHECK
LIST, VALUE ROUTE (carried into the (vi) cell): (1) 2·sqrt(eps_U/
mu_red) ≤ the certified basin radius (radius deriver = (E)/R-12; the
reduced argmax verified inside the basin in the same check); (2)
sweep-sup coverage declared per family; (3) H-G5 status declared.
[REV2-r4-1] CURVATURE FUNCTIONAL-IDENTITY + H-G6 (of record; probe
r22f_v2_probe_r4_l0_mu_identity_proxreg.py):
(a) FUNCTIONAL IDENTITY DECLARED at every curvature sentence: the
SCHEMA object in forms (T)/(C) and condition (1) is the curvature
floor of J_TRUE on the certified ball/cone — the VI chain behind the
licensed gradient-route forms consumes the strong-concavity modulus
of J_TRUE along the feasible segment; sign convention (C) unchanged;
the mu_curv rename at this landing carries this identity.
(b) HYPOTHESIS LINE (beside H-G1..H-G5; AG-1 valve: strong, declared,
sufficient-not-optimized):
  H-G6 (curvature transfer; as completed at this landing by the E-5
  deferred inputs): the measured carrier instantiates the J_TRUE
  floor only up to the CURVATURE-level residual — mu_true_floor ≥
  mu_meas − L_H, with L_H := the sup over the certified ball of the
  design-Hessian residual norm ||H_true − H_red||_M (the SECOND-ORDER
  face of the SAME reduction residual operator; by the adjoint
  representation it decomposes along the same (J)/(H) channels at
  second order PLUS cross-channel blocks bilinear in the first-order
  residuals (not excluded; each L_H deriver must price them or prove
  them absent) [E5-L2-3 executed]). H-G6 is read on the (E)-certified
  ball with mu_meas = the SUSTAINED ball floor of the measured
  carrier at its band-lower edge (the (E)/R-12 ladder object,
  mu_meas − b_E) — never the bare point measurement; mu_eff =
  (mu_meas − b_E) − L_H [E5-L2-2 executed; probe of record
  esc_probe_r4delta_hg6_pointfloor.py]. GUARDS [E5-L1-3 executed]:
  (existence) H_true is twice differentiable on the certified ball —
  the second-order strengthening of H-G3; a front-topology or grazing
  event inside the ball exits to the g2b calculus, named exit, and
  L_H is DECLARED UNDEFINED there (refusal, not a number); (typing)
  ||·||_M = the M-operator norm via the (B) Riesz identification;
  (guard) mu_eff > 0 required, else instantiation refused.
STATUS (honest, addendum_c4 (b) form): L_H is UNDERIVED of record —
SCHEMA + named derivers, the exact mirror of delta's own treatment
(R-9): (1) five-field content bound at Hessian level (X-T3QS-5F,
F2); (2) C51-route-B; (3) M-RED gradient-rider EXTENSION — divided
differences of the MEASURED gradient gaps along the §3.6 design
sweep = measured directional Hessian-gap (a cheap extension of the
same rider, beside the (E) curvature ladder). [E5-L1-2 executed:] the
leg-(3) measurement instantiates L_H at SAMPLED-DIRECTIONAL
(estimate) class ONLY — a finite-sample lower estimate along the
SWEPT directions alone; off-sweep curvature-gap content and
sub-sample-width structure are declared UN-EXCLUDED (probe of record
esc_probe_r4delta_lh_leg3_blindness.py parts A-B); a directional
estimate NEVER lands L_H by itself — landing requires deriver (1) or
(2) at norm level, or a declared direction-coverage certificate;
until then mu_eff licenses NO number (R-16 unchanged). New residue
R-16.
(c) CONSEQUENCE, carried into the [R22F-FORCHETTA] (vi) row: until
L_H lands, the GRADIENT-route cells license NO number even
a-posteriori from the measured carrier alone — the (vi) WORST cell's
honesty line reads "delta AND L_H underived".
(d) (F) IS MEASURED-CARRIER-SOUND (the asymmetry, stated): see (F)
above — the value route's floor is legitimately the measured carrier
as-is; the two routes' floors are DISTINCT objects.
[REV2-r4-2] H-G5 CONVEXITY-ONLY LICENSING (of record; probes
r22f_v2_probe_r4_l0_mu_identity_proxreg.py PART B and
r22f_v2_probe_r4_l2_proxreg_annulus.py parts A-F): the licensing
branch is CONVEXITY ONLY (H-G5 line above); the prox-regular disjunct
is WITHDRAWN as a licensing branch — it is retained ONLY as a NAMED
F2 REFINEMENT candidate carrying the curvature-corrected floor clause
(SCHEMA; residue R-17 below) — never a bare disjunct. R-14's decider
sentence carries the does-NOT-license clause (residue list below);
the connected-nonconvex no-coverage extension is in [REV2-r3-1](b)'s
tail and the (vi) WORST cell.
[REV2-r4-3] eps_U SAMPLED-SUP CLASS + REFINEMENT-STABILITY CLAUSE (of
record; probe r22f_v2_probe_r4_l2_proxreg_annulus.py part G): the
measured sweep-sup is a FINITE-SAMPLE LOWER estimate of the basin sup
and instantiates eps_U at SAMPLED-SUP (estimate) class ONLY — and
only when the sweep-sup is SUSTAINED under the declared
sweep-refinement re-check within its own band (refinement of the
sweep SAMPLING, a named part of the §3.6 rider / R-15; a sup that
grows under refinement = instantiation refused, declared);
sub-sample-width residual structure is declared UN-EXCLUDED at this
class. Measurement INSTANTIATES the (U_G)-type premise at declared
class — it NEVER discharges it: certified closure of the uniformity
premise remains with the (U)/S.22-class program (R-1).

RESIDUES CARRIED AT THIS SITE (deciders named; per VERDICT_r22f §4/§5
and VERDICT_escalation_c4 §7; F2 owners unchanged):
R-9: design-gradient residual bound delta — SCHEMA only; deciders in
order: X-T3QS-5F content bound, C51-route-B, M-RED
gradient-measurement rider (§3.6, F2). Never label-inflated to a
bound.
R-12: certified basin radius for the a-posteriori argmax-shift check
— deriver NAMED ((E)): curvature re-measure ladder on balls around
S*, extension of the M-RED rider (F2); radius = largest ball
sustaining the measured floor within its own band.
R-13: O1 gate (Danskin/Clarke cusp derivative, OBLIGATIONS LEDGER,
F4b theory WP — owner unchanged, cited not owned here): until it
discharges, form (C) and any critical-cone reading of the measured
carrier are unavailable at a margin-active S* (H-G4); every licensing
of form (T)/(F) carries H-G5.
R-14: H-G5 status of the KS-aggregated fold-margin feasible set at a
margin-active S* — OPEN (no convexity certificate (nor any other
licensing certificate) of record exists for the admissible profile
manifold ∩ {margin ≥ 0} [E5-L1-6 hygiene applied]); deciders
([REV2-r4-2](b) form of record): a CONVEXITY certificate for the
margin set (a prox-regularity certificate does NOT license the forms
— probes of record r22f_v2_probe_r4_l0_mu_identity_proxreg.py PART B
and r22f_v2_probe_r4_l2_proxreg_annulus.py), OR the F2
curvature-corrected prox-regular refinement (R-17) [ESC-E5-2:
decider-branch scope mirror, applies REPAIR E5-L1-5
(esc_refute_r4delta_l1.md) — this branch's discharge cannot be read
from the curvature formula alone: it is subject to the R-17 scope
clause below (effective-curvature horn only; a derived form
additionally requires the segment-feasibility clause; GLOBAL-argmax
coverage on prox-regular nonconvex sets remains un-claimable)], OR
branch-wise coverage via the cross-branch value-dominance check
([REV2-r3-1](b) — defined only where a component/branch decomposition
exists) with the measured sweep-sup eps_U (at [REV2-r4-3] class).
Until decided, form (T)/(F) licensing at a margin-active S* carries
the declared-OPEN H-G5 line, and nonconvex global-argmax coverage is
NOT claimed by any form of the schema.
R-15 (extended): eps_U sweep-sup measurement at SAMPLED-SUP class +
sweep-refinement stability re-check + the per-mesh floor-certificate
ladder re-check — named parts of the M-RED §3.6 rider / protocol run
(F2); the H-G6 deriver leg (3) (measured directional Hessian-gap, at
SAMPLED-DIRECTIONAL (estimate) class per E5-L1-2) rides the same
rider (M-RED value-deriver sampling blindness = residue R-ESC-3 of
VERDICT_escalation_c4, owner = this rider/R-15 extension).
R-16: curvature-transfer residual L_H (H-G6) — UNDERIVED of record;
SCHEMA + named derivers (mirror of R-9): (1) X-T3QS-5F at Hessian
level (F2); (2) C51-route-B; (3) M-RED gradient-rider extension.
Until L_H lands, the gradient route licenses NO number even
a-posteriori from the measured carrier alone ([REV2-r4-1](c)); an
acceptable dry outcome per addendum_c4 (b) — never label-inflated.
R-17: the F2 curvature-corrected prox-regular refinement of H-G5
(mu_prox = mu − |lambda*|·kappa_max, kappa_max = 1/r_prox; SCHEMA)
[E5-L0-2 executed: R-17's object RENAMED mu_prox — no symbol
collision with H-G6's mu_eff; its "mu" is the H-G6-transferred floor
where the carrier is measured (the two corrections compose additively
at SCHEMA class: (mu_meas − b_E) − L_H − |lambda*|·kappa_max);
underived until both legs land] — optional refinement, NOT a
licensing branch until derived; deciders beside the O1/R-13 block.
[ESC-E5-2 scope clause, applies REPAIR E5-L1-5 (probe of record
esc_probe_r4delta_lh_leg3_blindness.py part C): the
curvature-corrected clause prices the effective-curvature horn ONLY
and can license at most LOCAL-argmax tracking; any derived form
additionally requires a segment-feasibility clause (the segment
between S*_red and the candidate argmax feasible — the H-G5 rationale
property), absent which the annulus counter-model of record
(r22f_v2_probe_r4_l2_proxreg_annulus.py;
esc_probe_r4delta_lh_leg3_blindness.py part C) is the standing
refuter any derivation must refuse; GLOBAL-argmax coverage on
prox-regular nonconvex sets remains un-claimable by this refinement.]
(Standing residues R-1..R-8, R-10, R-11 of the carrier §6 are NAMED
there with deciders and carry unchanged; the ENTRY CONTRACT (U) —
S.22 sub-scope uniformity — remains OPEN, F2 theorem target.)

------------------------------------------------------------------------------
[T-T4] THEOREM 6 (T4 — plug simultaneous optimizability). THEOREM* (under the
ideal-adaptation closure [C-HT4]: wall pressure clamps to Pa downstream of each
phase's full-expansion point; upstream, T3-class scaling).
Claim: per phase, F[Sigma_l; s(xi)] is nondecreasing in plug extension l
and exactly constant for l >= l(xi), with l(xi) increasing in Pc(xi);
the per-phase argmax sets are nested half-lines [l(xi), inf); hence
    max_Sigma Int F dmu = Int max_Sigma F dmu,
attained by the PEAK-phase design: the untruncated plug at NPR =
P_CJ/Pa (capped by eps_max where binding).
PROOF. Monotonicity: on the exit-area-limited set the incremental
thrust of extension is (p_wall - Pa) dA_proj > 0; on the adapted set it
is zero by the closure. Constancy for l >= l(xi) likewise. l(xi)
increases in Pc because the full-expansion point moves downstream with
NPR (area-Mach monotonicity on the supersonic branch). Nesting: the
argmax set of phase xi is [l(xi), inf); the intersection over xi is
[l(xi_peak), inf), nonempty; on it every phase attains its max, so the
integral attains the integral of maxima, which is an upper bound by
monotonicity of the integral. Attainment/measurability: l(xi) is finite
for each xi (finite NPR), xi -> l(xi) is monotone in Pc(xi) hence
mu-measurable, and sup_xi l(xi) = l(xi_peak) is ATTAINED because Pc
attains its maximum on the (compact) cycle at the wave-passage phase.
QED.
Sharpness: a length cap L < l(xi_peak), a base-pressure model at a
truncation plane, or non-ideal adaptation break the nesting: then
max Int < Int max STRICTLY and the optimum satisfies the averaged
system (T7) with the mu-averaged plug corner condition.
PB-2 LOCKED FORMULATION OF RECORD (D-06, 2026-08-13 — never
abbreviate): "the first genuinely averaged and NON-COLLAPSING shape
problem of the program (a CYCLE instance)". Any phrase of the type
"the first averaged-thrust variational problem" is DEAD of record:
Efremov-Kraiko 2004 poses a period-averaged maximum-thrust
variational problem, Kraiko-signed, with measure Int_0^1 ... dt
(Eq. 1.7, p.624) [page-verified]. It does not touch PB-2 because it
has no wall contour (unknowns are time-functions of exit state plus
scalars W, Q), its measure is ENDOGENOUS time rather than an
exogenous measure on a given family, and its optimum COLLAPSES to
steady by the authors' own admission (Summary p.631).
Precedent caveat (page-verified, S14 PAN-S14 F-PB2FIRST):
Kraiko-Osipov PMM 34(6) 1970 already poses TIME-AVERAGED endpoint
conditions for a length-capped nozzle with base pressure on the end
face (their (1.4) and (3.2) cont., transl. pp. 1007-1008; (4.4),
p. 1011) — trajectory measure in place of the cycle measure; "first"
is program-internal wording: first CYCLE-averaged instance for the
RDE plug, not first averaged shape problem tout court; K-O 1970
mandatory citation here too (cross-ref the T7 precedent note).
EXTENDED CAVEAT LIST of record (D-06; carried whenever PB-2's
formulation is presented): Kraiko-Osipov PMM 34(6) 1970 (above);
ISABE-2003-117 + Bogdanov et al. 2002 (average-thrust descriptor is
UNVERIFIED inference, full text unread — P0 procurement);
Efremov-Kraiko 2004 (averaged but collapsing, not a shape problem);
Reuther et al., J. Aircraft 36(1):51-60 and 61-74 (1999) (shared
shape over a FINITE family, atomic measure, adjoint — aerodynamics,
not nozzles); Ornano et al. 2017 (time-averaged force objective on a
PDE nozzle, zero optimality conditions); Harroun M.S. Thesis 2019
(the closest prior art to cycle-averaged RDE nozzle evaluation, NOT
READ — P0); Levin & Manulovich CESW 46:418-425 (2010) and Billings
NASA MSFC TR (2000) (not read). Precedent
duty: the ideal-adaptation closure is published as a BOUND for
detonation cycles (Kraiko-Egoryan) — cite next to the closure.

------------------------------------------------------------------------------
[T-GB] PROPOSITION 7 (G-B — geometry-free upper bound) and COROLLARY (global
optimality over ALL topologies). THEOREM-grade / mechanism M1.
Claim: for ANY solid set S in ANY topology, under choked frozen feed:
    J[S] <= J_ideal = Int F_id(s(xi); Pa) dmu(xi),
F_id = thrust of complete isentropic per-streamtube expansion of phase
xi to Pa.
PROOF (sketch, rigorous). Hypotheses: adiabatic, inviscid, slip walls,
exhaust to quiescent ambient Pa. Fix a phase and a streamtube with data
(mdot, h0, s). Explicitly, F_id = mdot · V_id with
    V_id = sqrt( 2 [ h0 - h(s, Pa) ] )
(complete isentropic expansion to Pa, axially aligned). Any admissible
evolution can only increase entropy (shocks) and misalign momentum; at
given exit pressure Pa the axial momentum flux + pressure thrust is
maximized by the isentropic, axially aligned, fully expanded state:
entropy rise lowers exit velocity at fixed (h0, p_exit) since
dh/ds|_p = T > 0; misalignment loses the axial projection; incomplete/
over-expansion loses against full expansion by the classical
dF/dA_e = (P_e - Pa) sign argument on the supersonic branch. Integrate
over streamtubes and phases (measurability of xi -> F_id from R3).
QED (integral-flux relaxation: Efremov-Kraiko 2004, a weaker published
bound; axial-only energy variant = the EAP_i baseline, see Remark).
SHARPENING OF RECORD (2026-07-16, OP-0 ladder, src/thrust/bounds.py):
the dF/dA_e sign argument covers only the supersonic branch, so the
"complete expansion to Pa" form of F_id is the streamtube supremum only
for Pc/Pa >= ((g+1)/2)^(g/(g-1)). On subcritical phases
(1 < Pc/Pa < critical) the exit matching Pa is subsonic and the SONIC
exit strictly beats it (dF/dA_e = Pe - Pa < 0 along the subsonic branch
from the sonic point; jet matching Pe = Pa holds only at its endpoint):
executable counterexample g = 1.15, Pc/Pa = 1.3, dCF = +0.0070. F_id
must be CAPPED AT THE SONIC STATE; with the cap the bound is restored
and, at eps level, exactly attained by the per-phase relaxation
(int-max = ceiling, dual-route verified); the naive form is rejected by
tests/test_bounds.py on the four subcritical Table-1 rows
(choke_margin < 1). This proposition, the E-K comparison and the T4
closure (whose S-H spike form uses the naive branch on subcritical
tails) carry "min-cycle NPR >= critical" as an explicit hypothesis, or
the cap.
GAMMA-PURGE INSTANCE OF RECORD (2026-07-16, [F1/OP-0-gamma], session
S6; src/thrust/bounds_gamma.py + tests group (xi); strengthened
gamma directive). The ceiling's executable PRIMARY route is now
EOS-GENERAL: V_id = sqrt(2[h0 - h(s, Pa)]) and the sonic cap evaluated
on the Cantera frozen-CJ-products isentrope (frozen-composition
gamma(T) rung of the N4 ladder; cap located exactly by inverting the
monotone w(P) = h + c^2/2 at w(P*) = h0), with the closed forms of
this proposition DEMOTED to declared oracles. The cap criterion is
executably RE-VERIFIED at gamma(T): a scan of all admissible exits
never beats the capped formula (within measured table-noise bars),
and on the four subcritical Table-1 rows the naive uncapped form
strictly LOSES at the deepest subcritical phase — the g = 1.15
counterexample generalized beyond calorically perfect gas. Known-
answer rejector: a constant-cp synthetic gas through the same route
reproduces the closed forms to 4.7e-7 (derived tol 1e-6) and a
corrupted route is rejected. MEASURED PURGE DELTA of record: on the
12 finite-Pa rows the real gamma(T) ceiling sits 4.4-7.9% BELOW the
frozen-gamma_s closed-form oracle (bars ~0.002%, all significant) —
the price of the caloric idealization at ceiling level, now a number
with a rejector instead of a hypothesis. Vacuum rows: T-floor (200 K)
truncated LOWER-BOUND instruments, declared. Residual (declared S7):
DISCHARGED 2026-07-17 (session S8 operativa, [F1/OP-0-gamma tail]) by
the REAL-ROUTE DIAGRAM INSTANCE below and its equilibrium bracket.
REAL-ROUTE DIAGRAM INSTANCE OF RECORD (2026-07-17, [F1/OP-0-gamma
tail], session S8; src/thrust/phase_diagram_real.py + tests group
(xii) + data/phase_diagram_real.{json,md}). The OP-11-eps phase
diagram itself is now re-derived on the EOS-general primary route
(same 90-cell grid, same anchor; closed forms NOWHERE in the primary
computations): (i) the executable quasi-1D reduction of T7 (b)-(c)
acquires its first EOS-GENERAL carrier — eps* solves the weighted
condition <P_E(eps; xi)>_mu = Pa by inverting the REAL area-ratio map
per phase (the closed form NPR(eps*) = <Pc>/Pa is demoted to its
gamma = const oracle); real eps* = 3.49-3.52 across the grid vs the
oracle's value at gamma_s (numbers of record in the JSON); (ii) the
real adaptation knee sits BELOW the closed-form knee (10.38 vs ~12.9
at PR = 90 — the caloric idealization overestimates the envelope the
peak design needs, of record with bars); (iii) the map STRUCTURE is
CONFIRMED at gamma(T): tie column at PR = 1, capped band, no bell
cell, M1 attainment at eps_max >= knee_real on all 41 knee-fitting
cells INCLUDING the 11 subcritical ones — the M1 duality-gap-zero
extension is now certified EOS-GENERALLY, not only in closed forms;
(iv) the naive-adaptation instrument never beats the cap and loses
STRICTLY beyond the bar at the deepest-spread cells (two-level metric,
PR = 90 gap 1.9e-2 s vs bar 1.4e-2 s) — the subcritical artifact
generalized to the diagram level. EQUILIBRIUM BRACKET [T-EQBR] of record (same
instance): the shifting-equilibrium ceiling (SP-equilibrate isentrope,
Gibbs solver; eq sound speed from c^2 = dP/drho along the table)
sits +6.3..+7.0% ABOVE the frozen ceiling on every PR (bars <= 0.003
s; constant-cp known-answer through the eq machinery PASS, corrupted
route rejected): the pair [frozen, equilibrium] is the executable
MODEL BRACKET of the caloric closure at ceiling level (THEOREM*
within the ideal-gas mixture closure pair [C-IGMIX]; the frozen rung of the N4
ladder now carries its upper companion). Winner semantics UNCHANGED
(closures, never hardware — D3 §10quater(5) applies verbatim to the
real-route diagram).
COROLLARY (mechanism M1: duality-gap-zero globality). Under the T4
closure with generous envelope, the untruncated peak-designed plug
ATTAINS J_ideal ⇒ it is GLOBALLY optimal over all topologies. This is
the precise sense in which a "total optimum independent of the shape
category" exists; at finite constraints the total optimum is the winner
of the FINITE SECTOR TOURNAMENT (cone condition ⇒ finitely many
topology sectors; per-sector existence P7; cross-sector comparison
licensed by shared constraints + this bound). The phase-diagram
conjecture OP-11 ("the measure selects the topology") interpolates the
proven limits: spread->0 ⇒ sectors tie at the Rao value (T3);
generous envelope ⇒ free boundary attains the ceiling (T4/M1);
vacuum ⇒ no finite optimum; tight length + large spread ⇒ duty split
(C1, open).
[M1-WITNESS ADMISSIBILITY, dated 2026-08-05 (D8 §8 residue s5, second
lens): the untruncated peak-designed plug closes on the axis; whether
an axis-closing tip satisfies the uniform cone condition (h0, omega)
of A_gen is the unpinned census question O2
(validation/PANEL_topology_census_2026-07-22.md §5/§7, ADVISORY: full
spike in-class iff O2 resolves tip-admissible, else a
class-boundary/ceiling object). This corollary is hereby
O2-CONDITIONAL as an IN-CLASS attainment statement; as a bound
statement (ideal-as-bound discipline) it is unaffected. Pin owed to
the census-lemma session.]
[SINCE 2026-08-06: the O2 question is DISSOLVED at pin level — the
Omega-side Chenais cone-carrier pin (census §7pin, 2026-08-02)
places tangent tips / sharp TEs IN class: the full-spike M1 witness
is admissible under the pinned carrier. The in-record proof (cone
condition on the fluid side at an axis-closing tip) lands with the
census-lemma session; until then the attainment statement is
pin-decided, record-proof pending.]
[T-OP11e] EPS-LEVEL INSTANCE OF RECORD (2026-07-16, [F1/OP-11-eps];
src/thrust/phase_diagram.py + rejector tests + data/phase_diagram.json
+ figs/phase_diagram_op11.png; full statement D3 §10quater). The OP-11
interpolation is COMPUTED AND CERTIFIED at the eps rung (90-cell
eps_max x PR grid at fixed <Pc>, blessed CH4/O2 anchor, OP-0 ladder
embedded per cell). Two THEOREM-grade additions: (i) under the
SONIC-CAPPED adaptation closure (this proposition's cap applied to the
T4/H-T4 closure) the plug family weakly dominates the fixed bell
POINTWISE — no strict bell region exists at eps level; (ii) at
eps_max >= knee the capped plug coincides pointwise with the per-phase
argmax and ATTAINS the capped ceiling: M1 gap-zero on every Pa > 0
cycle INCLUDING subcritical ones — the supercritical hypothesis is
needed only by the NAIVE closure, which loses strictly on subcritical
tails and, at the sonic-annulus cap eps_max = 1, even inverts the
bell/plug ranking (executable artifact, test-rejected). Tie region
characterized: eps_max <= eps*(Pc_min) ⇒ the plug never releases and
equals the bell as a member (plus the PR = 1 column, T3, and the
vacuum no-optimum sweep, both asserted as oracles). Duty splitting is
not expressible with the single shared eps DOF: at contour level OP-11
remains CONJECTURE.
SCOPE (non-transfer to (P), D2.6 — remark of record, full form D3
§10quater(5)): the diagram's winners rank CLOSURES at equal eps_max,
not hardware sectors of the constrained problem; the released capped
plug IS the per-phase relaxation, so its dominance prices the
ADAPTATION PREMIUM and does not decide (P) — the topology of S*(c) is
the output of the finite sector tournament at the true constraint
vector c (not a priori {bell, plug, shrouded}), and bell-winning
regions of (P) are EXPECTED at contour level once truncation/base-
pressure/length losses bite. Each cell certifies toward (P) the
geometry-free PREMIUM_BOUND = Isp_ideal(capped) − Isp_bell (THEOREM,
up to the bell surrogate's C4 bar): any certified non-bell loss band
exceeding it closes that cell for the bell with delta-certificate per
D2.6(iv) — the tournament device that PB-2's empirical truncation
band will arm.
[LAND-C4-LA3 DC-6 ONE-LINER at the T3/T4 attainment site (SCHEMA,
labels per VERDICT_escalation_c4 §5.3; full statement in the [T-DCRX]
block below): T3's collapse is precisely attainment of the
constraint-aware rung B1^c under pressure similarity — in that class
the per-phase constrained optimum is phase-shared, so B_fam({eps, L})
is attained by one design UPON its per-cell axial-supersonicity
certificate (M cos(theta) > 1, the S1 margin check; the attainment
claim is certificate-conditional), Pi_L -> 0 and delta^c ->
delta_true: the [T-DCRX] decomposition degenerates exactly as the
record demands (delta = 0 proven where M1-M3 structure exists,
D2.6(iv)) — no contradiction between the lemma, the rung program, and
the T3/T4 attainment results. FALSIFIER: a pressure-similar cycle
with computed B1^c strictly above the T3-collapse optimum (beyond
bands) breaks either this schema or the T3 chain.]

REMARK (relation to EAP — verified against Kaemming-Paxson, AIAA
2018-4567, NTRS 20180006890, full text read 2026-07-16). The industry's
Equivalent Available Pressure EAP_i is, verbatim from its Eqs. 1-8, the
PRESSURE-COORDINATE of J_ideal: each exit segment expanded
isentropically to ambient SEPARATELY (expand-then-average, never
mixed-out-then-expand), mass-flux-weighted specific quantities
(algebraically identical to our time-integrated fluxes, O1), computed
in the detonation frame where "area average = time average" — i.e. our
T0(i) used tacitly as a fact, proved here as a theorem. Deltas:
(1) baseline EAP_i declares non-axial energy unavailable (V_x only),
its +6% variant includes it: two adjacent ladder rungs,
EAP_i(axial) <= J_ideal(total); (2) EAP carries the quasi-steady and
azimuthal-decoupling hypotheses (our D1+D2) UNSTATED and UNPRICED —
the P4 corrector is, among other things, EAP's missing error bar;
(3) EAP is the combustor-alone CEILING: the program's bound gap
J_ideal - J(Sigma*) is the honest discount factor on advertised
pressure gain (cf. Paxson 2022: real truncated plug at 58-70% of the
notional ideal). The formalization CONTAINS and COMPLETES the EAP
doctrine rather than competing with it — a citable bridge for P-1.

REMARK (relation to the Stechmann-Heister-Harroun model — verified
against the full-text-derived granular spec, JSR 56(3):887-898 (2019),
doi:10.2514/1.A34313; local page renders + text in
`../project_build/tmp_st`, spec in `../project_build/specs/
stechmann_spec.md`; model mechanics independently validated in-repo
18/18 on Table 1). Concordances:
 (1) their Eq. (4) cycle Isp = total impulse / cycle propellant mass
     ≡ Def. 3.2 + Prop. O1: their mass-flux weighting of the
     instantaneous Isp is algebraically our time integral of F
     (numerator A_t Int Pc·CF dt via mdot·c* = Pc·A_t — the same pivot
     as the in-repo proof);
 (2) their F(t) = mdot·CF·c* is the PURE rung-2/I3 quasi-steady proxy;
     no momentum-storage discussion anywhere: Theorem 0 supplies the
     missing license, P4 the missing error bar — and their own flagged
     open item ("two timescales... the community has substantial work
     to do") is precisely what P4 answers;
 (3) their assumption list maps 1:1 onto the hypothesis ledger:
     asm 2 (M, gamma frozen) = H-T3.1; asm 3 (choked at all times,
     exit plane = thermal throat) = H2; asm 1 (exponential blowdown,
     complete fill) = the O2 measure generator; Eq. (9) validity
     (full-flowing bell) = H-T3.2; Eqs. (10)-(12) (ideal spike,
     Pe = Pa below max expansion) = the H-T4 closure verbatim;
 (4) THEIR NUMERICAL FINDINGS ARE INSTANCES OF THE THEOREMS HERE:
     bell eps_opt unchanged det-vs-CP (their Fig. 9, dotted optimum at
     the same eps in both panels) = the T3 collapse (repo Theorem 1);
     det aerospike sized by the PEAK with monotone-saturating Isp(eps)
     (Figs. 10/12: eps_opt 9.2-12.2 vs CP 3.6-3.9) = the T4 knee/
     plateau (repo Theorem 2); vacuum area ratios reported as "maximum
     values used in the simulation", not optima (Table 1 note) = the
     vacuum no-finite-optimum theorem (repo Theorem 3);
 (5) their Conclusion-7 loss ledger maps onto the violation channels:
     oblique-shock loss -> N3, gamma variation -> N4, off-design/
     separated nozzle -> N1, transient swirl -> N6, finite-rate
     kinetics -> the Hoffman boundary (N4 finite-rate rung).
QUANTITATIVE CONVERGENCE CHECK (executed 2026-07-16, closed-form,
one line per prediction): T3 predicts the bell optimum at
eps(NPR = <Pc>/Pa); T4 predicts the spike knee at eps(NPR = Pmax/Pa).
Against their Table 1 (Pcp = 20 atm, Ti = 200 K, Pa = 1 atm; peaks
from their Fig. 4, gamma back-computed 1.14/1.16, <Pc> = Pcp(1+DC)):
  H2/O2 : predicted bell 4.01 vs their 3.8; predicted spike knee 10.5
          vs their 9.2 (ratio 2.62 vs 2.42);
  CH4/O2: predicted bell 3.90 vs their 4.0; predicted spike knee 10.7
          vs their 11.4 (ratio 2.75 vs 2.85).
Agreement 3-5% (bell) and 6-14% (spike) — exactly the level warranted,
since their per-column optima re-optimize phi (changing PR and gamma
between columns) while the closed-form check holds phi fixed. Their
CEA-swept optima are thus reproduced by two one-line theorem
evaluations: independent numerical corroboration (their computations
predate this theory; no circularity). The FULL-FIDELITY version of
this check, with phi re-optimized per column as they do, already
exists in-repo: the 18/18 Table-1 validation reproduces their JOINT
(phi, eps) optima via `phi_opt` (certified 0.01-lattice search with
strict-neighbor certificate and global unimodality scan — no closed
form exists in phi since Isp(phi) passes through Cantera equilibrium
states) × `bell_opt` (closed form). Formal placement of phi: an OUTER,
non-variational design parameter of the DATA GENERATOR — it moves the
family s(xi; phi) and the measure mu(phi), not Sigma; the joint problem
is NESTED, max_phi max_Sigma J, with T3/T4 valid at each fixed phi and
the outer loop certified by the lattice — not to be confused with the
bilevel PB-4 (shape-to-chamber feedback).
The formalization therefore EXPLAINS the paper's empirical
regularities (its three nozzle findings are corollaries, now checked
NUMERICALLY, not only structurally), CLOSES its two flagged gaps
(timescale license = Theorem 0 + P4; fair-metric question = the bound
ladder), and inherits its comparison protocol (equal cycle mass +
throat area) as the frozen-family normalization. Together with the EAP
remark above, this is the second citable bridge for paper P-1 (target
venue: JPP class).

------------------------------------------------------------------------------
[T-DCRX] FIXED-EXIT-AREA RELAXATION LEMMA AND DELTA CARRIER (Part III
block, landed S-FOUNDATIONS-C4 2026-08-21)

[LAND-C4-LA3 LANDING HEADER] Executes VERDICT_escalation_c4 LA-3(i)
(escalation E-3 CLOSED DRY at round 3; sequencing gate §3 SATISFIED —
minor (b) closed first, (H6')/ship-gate block bit-identical across
all rounds — so this landing is UNGATED). Carrier of record:
validation/sfoundations_raws_2026-08-13/phaseD/
phaseD_minor_deltacarrier.md as revised through [ESC-r3-*], landed per
its §9; statement labels per VERDICT_escalation_c4 §5.3 (DC-1/DC-2
THEOREM*, DC-3 THEOREM under V1-V2, DC-4 THEOREM inequality with
SCHEMA regime clause DORMANT, DC-5 PRACTICE, DC-6 SCHEMA — the DC-6
one-liner lands at the T3/T4 attainment site above, beside the
[T-OP11e] instance). Site: adjacent the [T-GB]/OP-0 ceiling block
(after the sonic-cap sharpening; site ratified twice). Conditional
entry of record: [C-DCRX-CERT]. The judge-ordered LANDING-CUT edit
(ESC-DELTACARRIER-r3-1) is executed at the phase-quantifier pin below.

SETTING (per phase xi). Class W of per-phase designs (the engine's S1
per-phase class, bell/TOC exit topology) sharing: (H1) shared-Sauer
data contract — same transonic data (Sauer IVL), same throat area A_t,
same per-phase mdot and stagnation state (h0, s0), flow irrotational-
homentropic and shock-free (S1) downstream of the IVL, so h = h0 −
q^2/2 on the (h0, s0) isentrope and C_IVL (momentum-flux +
gauge-pressure integral over the IVL) is W-independent; (H2) fixed
exit area: exit disk = flat disk of area A_e = eps·A_t at the lip,
control volume {IVL, wall, axis, exit disk} (bell topology;
annular/plug NOT covered — declared scope limit); (H2b) mdot/A_e <
rho* c* (sonic state on the same isentrope; checkable per design);
(H3) per-cell axial supersonicity u_x − c > 0 on the exit disk
(certified a posteriori by the S1 margin machinery); (H4) constant
ambient Pa >= 0, objective J[W] = Int_wall (p − Pa) n_x dA ([T-TH0]
restricted per phase), steady per-phase Euler; (H5) smooth strictly-
decreasing isentrope q -> (p, rho, c); (H5b) gamma_s := rho c^2/p >=
1 (thermally-perfect frozen mixtures; table-checkable).
Pa-ADJACENCY SENTENCE (mandatory, ESC-DELTACARRIER-r2-3): Pa >= 0
deliberately widens (P)'s Pa > 0 (D2.6) to cover the executed vacuum
objective — the [OBJ-DOM] Pa axis, already consumed by the DC-5(b)
same-Pa-convention line; the argmax is untouched, the offset is the
class-constant Pa·Int_wall n_x dA.
Define lambda = q_e(eps) as the unique supersonic root of
rho(lambda)·lambda = mdot/A_e on the (h0, s0) isentrope (exists and
is unique under (H2b): rho q strictly decreasing from rho* c* to 0 on
the supersonic branch); M_e(eps) = lambda/c(lambda) > 1; J_ideal(eps)
:= C_exit^id − C_IVL, C_exit^id = A_e[rho(lambda) lambda^2 +
p(lambda) − Pa].

DC-1 (FIXED-EXIT-AREA RELAXATION LEMMA) [THEOREM* under the declared
conditionals (a) (H3) a-posteriori certification, (b) bell-only exit
topology, (c) S1 piecewise-C1 shock-free fields — [C-DCRX-CERT]].
Under (H1)-(H5b), for every design W in the class: J[W] <=
J_ideal(eps), with equality attained by the uniform axially-aligned
exit STATE at M_e(eps) (the relaxation's maximizer; in-class
attainment NOT claimed — no finite-length class member need realize
it, and a ceiling needs no attainment). Consequently J_ideal(eps) is
the L-UNCONSTRAINED FIXED-EPS CEILING: it binds every class member
regardless of length or any other c-slot.
PROOF. (i) Momentum theorem on the (H2) control volume (axis
contributes nothing by symmetry; constant Pa integrates to zero over
the closed surface): J[W] = C_exit[W] − C_IVL with C_exit[W] =
Int_{A_e} [rho u_x^2 + (p − Pa)] dA; C_IVL class-common by (H1).
(ii) Pointwise Lagrangian bound: with the multiplier lambda and the
mass constraint Int_{A_e} rho u_x dA = mdot, C_exit[W] − lambda·mdot
= Int_{A_e} Phi dA, Phi = G − Pa, G(q, u) := rho(q) u^2 −
lambda rho(q) u + p(q), local state on the (h0, s0) isentrope,
u := u_x in (c(q), q] ((H3) forces the supersonic branch). CLAIM:
sup over admissible states of G = p(lambda), attained at (q, u) =
(lambda, lambda). (ii.a) G is convex in u (rho > 0), so its max over
u in [c(q), q] is at an endpoint. (ii.b) aligned endpoint A(q) :=
G(q, q) = rho(q^2 − lambda q) + p; by (H5) A'(q) = rho (q − lambda)
(1 − M^2), so on the supersonic branch (1 − M^2 < 0) the global
branch max is A(lambda) = p(lambda). (ii.c) axially-sonic endpoint
B(q) := G(q, c(q)): if q + c(q) >= lambda then B − A = rho (c − q)
(c + q − lambda) <= 0; else c − lambda < −q gives B < p − rho c q <
p(1 − gamma_s) <= 0 < p(lambda), using q > c (H3) and gamma_s >= 1
(H5b). (iii) Assembly (exact weak duality): C_exit[W] <= lambda·mdot
+ A_e (p(lambda) − Pa) = C_exit^id, attained by the uniform aligned
exit at M_e(eps), hence J[W] <= J_ideal(eps). QED.
MU-INTEGRATED FORM: with phase-indexed data s(xi) = (mdot, h0, s0),
phase-shared eps, and W satisfying (H1)-(H5b) at mu-a.e. xi,
J_cycle[W] <= Int_Xi J_ideal(eps; s(xi)) dmu =: J_ideal_cycle(eps)
(pointwise domination; measurability of xi -> J_ideal from continuity
of the monotone root lambda(xi) in the data, R3 chain).
FALSIFIER (DC-1): (numerical) any certified class member with
(H1)-(H5b) verified and computed J[W] > J_ideal(eps) + ceiling band —
executable at the twin (TOC run vs ideal march, same eps, tables,
Sauer IVL); (analytic) any admissible (q, u) with G(q, u) >
p(lambda). The (H3)-breakout rejector is DISCHARGED executable
(esc_probe_deltacarrier_h3breakout.py, two-sided, PASS of record:
half [A] verifies sup G <= p(lambda) with exact aligned attainment;
half [B] drops (H3) and breaks the bound macroscopically — the
hypothesis list IS load-bearing).

DC-2 (DELTA SEMANTICS OF RECORD) [THEOREM*, inherits DC-1;
[C-DCRX-CERT]]. Let A(c) be the admissible class of (P) (full
constraint vector c, D2.6) and A(eps) the same class with every
c-slot except the exit-area/eps slot (and the class-defining
regularity) removed; W_cert := the certified subclass satisfying
(H1)-(H5b) — in particular (H3), certified a posteriori (per-cell
M cos(theta) > 1, the S1 margin check). PHASE-QUANTIFIER PIN OF
RECORD ([ESC-r3-2a], with the judge-ordered landing-cut edit):
(H2b)/(H3) are PER-PHASE predicates, so W_cert membership is
evaluated at the phase data in play; in cycle-integrated displays
(the mu-integrated form of DC-1, the B_fam(C) definition, DC-3)
W_cert denotes the mu-a.e.-ALL-PHASE certified subclass —
alternatively, write W_cert(xi) inside the integral (either pinning
closes every proof; both readings agree for every named consumer).
The named consumers (the certified S*, the classical solves under
their a-posteriori certificates) are certified at every phase, so no
conclusion moves under either reading; a MIXED reading (S certified
at one phase only, read into a xi-independent symbol) is EXCLUDED.
Then A(c) ∩ W_cert ⊆ A(eps) ∩ W_cert and, by DC-1 applied
member-by-member on W_cert,
  sup_{A(c) ∩ W_cert} J <= sup_{A(eps) ∩ W_cert} J <= J_ideal(eps);
hence for any certified J[S*] (S* in A(c) ∩ W_cert by its own
certificate): delta := J_ideal(eps) − J[S*] >= 0, with the exact
(definitional) decomposition delta = Pi_c + delta_true, Pi_c :=
J_ideal(eps) − sup_{A(c) ∩ W_cert} J >= 0 (constraint price),
delta_true := sup_{A(c) ∩ W_cert} J − J[S*] >= 0 (true
suboptimality) — the decomposition holds over the certified subclass
and only there. The split (Pi_c vs delta_true) is NOT separately
computable today — exactly the bound-ladder row's gap. SEMANTIC RULE
(of record): every (value, delta) Verdict row says "distance to the
L-unconstrained fixed-eps ceiling" — NEVER "distance to global at
(eps, L)"; under tight L/eps_max delta can be Pi_c-dominated and go
uselessly loose while the design is near-optimal (the number stays
TRUE, only the loose direction is declared).
SCOPE [ADV, synthesis (e).3/G-12, CT-6-clean — lands verbatim]:
"J_ideal(eps) prices designs INSIDE the fixed-interface data class
(H1); constriction/choking/exit-area moves that rewrite the chamber
state are class-changing and outside what delta prices — the largest
published performance lever lives there; pricing it is CFD-1's
irreducible core."
FALSIFIER (DC-2): a certified S in A(c) ∩ W_cert with J[S] >
J_ideal(eps) (breaks the inclusion chain, hence DC-1; an uncertified
exhibit breaks nothing — exactly the probe's half [B]); or a shipped
Verdict row wording "distance to global at (eps, L)"
(grep-detectable).

RUNG-FAMILY POINTER (DC-3/DC-4; full statements + proofs in the
carrier §§4-5). The relaxation family is DEFINED over the certified
set: B_fam(C) := Int_Xi sup_{S' in A_phase(C) ∩ W_cert} F[S'; s(xi)]
dmu(xi) — the ∩ W_cert restriction lives in the DEFINITION itself,
phase-quantified per the pin above; membership of the named classical
instantiations (Rao/Guderley-Armitage/Kraiko per-phase constrained
solves, the B1^c rung) is an a-posteriori CERTIFICATE (per-cell exit
axial supersonicity, M cos(theta) > 1, the same S1 margin check as
every consumer; certificate-on-entry duty [DC-F2-2], report-on-fail)
— the retracted "supersonic-exit by construction" inference does NOT
land. DC-3 [THEOREM under V1 (A_phase(C) xi-independent) and V2
(mu-measurability of the per-phase sup)]: J_cycle[S] <= B_fam(C) for
any certified all-phase-feasible S; B_fam monotone non-increasing in
C; B_fam({eps}) <= J_ideal_cycle(eps); adding the B1^c rung to the
ladder min can only TIGHTEN delta — delta^c = min(B, B1^c) − J[S*]
carries the semantics "distance to the C-relaxed ceiling" with Pi_c
reduced by exactly the priced slots. DC-4 [THEOREM (the weak-duality
inequality); regime clause SCHEMA; DORMANT]: for (P) as posed
(unilateral caps) and ANY mu_i >= 0, sup_{A(c)} J <= sup_{A(eps)}
[J − Sum_i mu_i (g_i − c_i)]; the rung consumes multipliers of the
UNILATERAL regime only (T7(c) cone form) — the fixed-eps bookkeeping
regime 2 carries FREE-SIGN lambda components which are NOT admissible
weights, so the rung is DORMANT until (P)-as-posed capped runs exist
([DC-F2-3] contingent).

DC-5 (CARRIER PRACTICE RULES) [PRACTICE]. (a) ANTI-CONSERVATIVE
DIRECTION: an under-estimated ceiling under-states delta, so delta is
quoted against the UPPER band edge of J_ideal (two-resolution band +
eps-achievement correction; lip/eps residual 4.4938e-3 measured at
the twin); under branch (H6'-B) the upper edge is additionally
WORSENED by the net-two-wall-panel band. (b) HYPOTHESES IN THE
CARRIER: same eps, same thermo leaf/tables, same Sauer IVL/mdot —
printed in the Verdict row; PLUS which (H6') branch the row shipped
under ((H6'-A) fix-A panel-inclusive functional on BOTH sides of
delta, or (H6'-B) both sides on the coded functional AND the explicit
net-two-wall-panel band, anti-conservative sign declared); PLUS the
same Pa convention (gauge/vacuum) declared — a delta row mixing a
gauge ceiling against a vacuum J[S*] is wrong by exactly the
class-constant Pa·Int_wall n_x dA; PLUS the (H2b) check result
(mdot/A_e vs rho*·c* from the same tables). (c) SEQUENCING (binding):
no (value, delta) row ships unless "[OBJ-DOM-IMPL] landed and used on
both sides, OR the net-panel band included" — the ship-gate remains
ARMED for every future (value, delta) row. FALSIFIER: a shipped delta
row quoting the lower/central band edge, or missing the hypothesis
line, is a carrier violation (grep-detectable).

F2 DUTIES (measured halves, named): [DC-F2-1] (value, delta) Verdict
field at the engine rung (ships under (H6') + DC-5); [DC-F2-2] B1^c
rung executable WITH the certificate-on-entry rule; [DC-F2-3] KKT
weak-duality rung instantiation (contingent, dormant until
unilateral-regime runs exist); [DC-F2-4] ceiling band measurement at
production resolution (upper-edge rule DC-5a); [DC-F2-5] DC-1
rejector (twin J_TOC <= J_ideal check + the (H3)-violation breakout
test; analytic form discharged by the probe of record) + the (H2b)
check, report-on-fail, never proceed silently.

------------------------------------------------------------------------------
[T-T7FS] THEOREM-SCHEMA 8 (T7/T2 — the averaged stationarity system). SCHEMA.
Maximize J over Sigma in a restricted class, per-phase steady Euler
constraints (adjoint psi_xi per phase), per-phase mass flow fixed
(function-valued multiplier lambda2(xi) in the control-surface
formulation; intrinsic in the wall formulation), shared geometric
constraints (multipliers lambda_L, ...).
Stationarity structure (verified formally):
 (a) per a.e. xi: the per-phase adjoint Euler system; in the
     IRROTATIONAL-HOMENTROPIC subclass of S1 (scope qualifier added
     S21 per audit C1 — the closed form's derivation layer, T-A3,
     is scoped there; on rotational S1 members the identification
     survives only at the FIELD level, VI.4bis(iv)) it reduces to
     the classical closed form — optimal control surface = the
     phase's characteristic; first integral
     f2 = V cos(theta -/+ alpha)/cos(alpha) = -lambda2(xi).
 (b) shared wall: Int_Xi G_xi(x) dmu + lambda_L g_L(x) = 0 a.e. on the
     wall, G_xi the phase Hadamard density — no phase satisfies its own
     wall condition; the mu-average does.
 (c) shared endpoint — THE WEIGHTED TRANSVERSALITY (**'), CONE FORM
     OF RECORD (C31, user-ratified 2026-08-13; supersedes the plain
     equality, which is the free-endpoint special case below):
         D := Int_Xi (dF/ds_E)[Sigma; s(xi)] dmu(xi)  in  N_K(s_E*),
     i.e. <D, d> <= 0 for all d in T_K(s_E*), with K = the admissible
     set of the SHARED endpoint, DECLARED for every statement and
     every instrument (one VI-statement, not three theorems):
       - K locally unconstrained => N_K = {0} => D = 0 (Rao Eq. (14) /
         KT2015 (2.10) as equalities — the FORMER statement of
         record, now the free-endpoint case);
       - K = {point} (fixed-(eps, L) pinning) => condition VACUOUS,
         the lambda are the components of D with FREE sign — exactly
         the FIXED-EPS TRANSVERSALITY BOOKKEEPING lambda_e = dJ/dy_lip
         already of record (the regime in which ALL executed
         instances live: the committed driver pins the lip by
         EQUALITY, a1_toc_variational_jax.py:1748);
       - K with unilateral caps ((P) as posed, A_gen(c) with
         g_i(S) <= c_i; the production quasi-1D reduction with its
         eps clamp/cap branches) => sign + complementarity per
         component, direction DERIVED from the active side: the
         admissible cone {Dx <= 0} INTERSECT {Dy <= 0} has polar
         giving BOTH >= 0 signs of KT2015 (2.10).
     The per-phase MASS FLOW stays an EQUALITY and lives OUTSIDE the
     cone (function-valued lambda2(xi); KT2015 (2.13) is an equality
     for the same structural reason: the fixed flow rate makes the
     endpoint variation dependent). D factorizes R(xi)·w(xi) with R
     the classical corner residual and w > 0 a geometric-kinematic
     weight; w is phase-independent EXACTLY in the T3 class (there
     (**') reduces to the naive average — everywhere else the naive
     form is WRONG; every implementation must use (**')). BOXED
     WARNING TWIN: the weight does NOT deform the cone — weighting
     and unilaterality are INDEPENDENT corrections.
     CONE TRANSFER LEMMA [T-T7CN] [THEOREM, elementary; proof of record:
     N_K(s*) is an intersection of half-spaces through the origin
     indexed by K, and the mu-integral (mu >= 0, integrand in
     L^1(dmu) by the [C-D25U] domination) preserves each half-space
     separately — neither closedness nor convexity of N_K is
     invoked]: if (dF/ds_E)(xi) in N_K(s_E*) for mu-a.e. xi, then
     D in N_K(s_E*). The CONVERSE IS FALSE (two-phase counterexample
     of record: K = {y <= 0}, s* = 0, N_K = [0, inf),
     D(xi_1) = -1, D(xi_2) = +3, mean = +1 in N_K with phase 1 out).
     Consequence: an all-in-cone per-phase sign scan CERTIFIES the
     cycle condition with no averaging (sufficient, not necessary);
     any tool armed on it must ACCEPT a one-phase-out/mean-in family
     (the S3 rejector of record, A39).
     CONTENT SPLIT (axial-vacuous / radial-substantial): axially,
     rho v^2 tan(mu_Mach) >= 0 POINTWISE AND IDENTICALLY, so the
     axial cycle condition holds automatically by the lemma; its
     only content is binary — lambda_L > 0 <=> mu({xi : v_E(xi) !=
     0}) > 0 => length cap ACTIVE (strictly weaker in hypothesis
     than the per-phase statement; per-phase, KT2015 p.186 carries
     the "if exists" qualifier on the terminal face). Radially,
     R(xi) CHANGES SIGN along the cycle (over- and under-expanded
     phases): ALL the averaging content of the unilateral condition
     lives there.
     ROUTE-A GRAFT (zero cost): rho v^2 tan(alpha) = -lambda3/q by
     Rao Eq. (13), hence lambda_L = Int_Xi (-lambda3(xi)/q) dmu >= 0:
     the cycle length multiplier is the mu-average of the per-phase
     Route-A length multipliers — the exact length twin of
     lambda2(xi) = -f2(lip data) [T-P3]. Carrier already computed
     nodewise: f3* = 2 pi y rho W^2 sin^2(theta) tan(alpha)
     (validation/o33_bench.py:292). NOTE (REFUTE_C, honest limit):
     f3* >= 0 identically on physical fields, so a bare sign check
     on it can never fire (R5); the falsifiable content is the
     IDENTITY lambda_L = Int f3*/q dmu plus complementarity.
     CLAIM-16 COMPANION (C32 falsifier, regime-qualified): outside
     the T3 class, since w > 0 is phase-dependent and R(xi) changes
     sign, Int R dmu and Int R w dmu can have OPPOSITE SIGNS — in
     the unilateral regime with an active cap the naive form can
     certify as KKT-admissible a DUAL-INFEASIBLE point. Falsifier
     (cheap, two quadratures on already-marched fields, no
     re-optimization): compare the two signs; family-wide agreement
     on a sign-varying-R family falsifies the RELEVANCE of this
     failure mode on the executed class (the existential itself is a
     theorem — two-phase example of record). The dual-infeasibility
     reading has content ONLY at an active unilateral cap (regime
     qualifier of record; in the fixed-(eps,L) regime a sign flip
     only measures naive-vs-weighted divergence).
TRAJECTORY-AVERAGED PRECEDENT (page-verified 2026-07-22, S13):
Kraiko-Osipov PMM 34(6):1067-1075 (1970) derive, for the TRAJECTORY
instance of this structure (aircraft flight conditions in place of
the cycle), the time-integrated weighted wall condition (their
(3.2), weight = trajectory-adjoint W(t)), multiplier fields on the
flow characteristics with jump relations, and the collapse of the
averaged conditions to the classical single-state family with
time-averaged weight under invariant dimensionless inlet (their §§4-5:
§4 = the averaged-weight collapse under inlet similarity; §5, transl.
p. 1012, = the degenerate second case — plane "short" nozzle, uniform
supersonic inlet, straight generatrix — where the FIRST of their
conditions (3.2) holds at every instant: stationarity-level partial
ancestor of T4's simultaneous-optimality mechanism [S14, PAN-S14
F-KO5])
— the 1970 ancestor of (b), of the weighted structure of (c), and
of T3's averaged-family reading. Not present there: the cycle
measure, exactness (T0), the priced O(St) step, the sharpened
pointwise collapse with proven boundary, certificates, and the
adjoint identification of P-2. Mandatory citation.
Non-smoothness: topology-switch phases are mu-measure-zero with F
continuous across them: Leibniz survives moving switches (boundary
terms cancel); persistent kinks: Clarke subdifferentials.
Named rigor gaps: [T-P3] P3 (lambda2 in L^2(dmu)) — UPGRADED 2026-07-16:
THEOREM* [C-D25U] in the shock-free S1 class (lambda2(xi) = -f2(lip data),
unique by scalar CQ, measurable + L^inf by margins; proof of record
docs/rde_nozzle_P3_multipliers.md; residues R-P3.1/R-P3.2 named
there; across fitted shocks it inherits the D2.5 conditional [C-MAJDA]);
T7 ITSELF UPGRADED same day ([F1/T7-FS],
docs/rde_nozzle_T7_P7_functionspace.md §1): differentiation under the
cycle integral is now THEOREM* — per-phase derivatives exist
(classical + G12-S1), are measurable (P3 composition) and uniformly
dominated by the audited margins, so dJ = Int F' dmu and the wall
condition + (**') are genuine L^1(dmu) statements (conditionals
R-T7.1/2 named: the shared D2.5 uniform-estimate conditional [C-D25U]).
NAMED HYPOTHESIS ADDED OF RECORD (H-EXO, D-02 2026-08-13, from the
Rubino confrontation): the cycle measure and the interface state map
are EXOGENOUS to the design — dmu/dSigma = 0 and ds(xi)/dSigma = 0 —
guaranteed on the L4 class (every axially supersonic patch with
margin) by the upstream-influence exclusion [T-NSW]. The Rubino/
Krakos residue term ||(1/T) dT/dsigma||_1 ||d_s h||_inf O(k^-(p-1))
prices exactly the failure of this hypothesis on the DOMAIN side:
our THEOREM* upgrade of differentiation under the cycle integral
dominates the INTEGRAND, not the domain, and is honest only under
H-EXO. Refuter precision of record: for a NORMALIZED phase measure a
pure rescaling of the physical period is a null variation — the
object that must be design-independent is mu, not T (Rubino p.20
confirms the positive direction: the interchange holds when the
period is design-independent). Named falsifier: a MEASURED
dmu/dSigma /= 0. H-EXO becomes LOAD-BEARING at F5 (coupled RDE) and
wherever mu(Xi_sub) > 0.
[T-P7S1] P7 EXISTENCE attacked same day (same doc §2, THEOREM*): argmax exists
on every margin-certified level set A_h^delta (finite-dim compactness
+ closed margins + continuity via R-P7.1 [C-D25U]); the monitored failure
boundary of record IS the boundary of those level sets;
[T-G12S1] G12 (multi-D fitted-shock shape derivative: theorem only in 1-D
[Bressan-Marson; Ulbrich]; quasi-1D design rigor [Cliff-Heinkenschloss-
Shenoy]; 2-D practice [Baeza et al.]) — ATTACKED 2026-07-16
([F1/G12-S1], docs/rde_nozzle_G12_S1.md): within the S1 marching
class the gap REDUCES to the 1-D-in-time theory via the x-as-time
reading (Lemma G12-L1, eigenstructure machine-verified EOS-general:
det A_p ∝ u^2(u^2-c^2), pencil factorization, Mach-line roots) plus
the front brick (Lemma G12-L2, machine-verified with rejectors:
linearized RH nonsingular strictly inside Lax, degeneration EXACTLY
at characteristic fronts = the Prop. A2 kernel law); THEOREM G12-S1
(THEOREM*, residues R-G12.1..3 named: D2.5-inherited regularity
conditional [C-D25U], shift-differentiability citation TO-VERIFY, mesh limit
= Lemma B clause with target now stated). Carrier:
validation/g12_shock_linearization.py, PASS with derived equilibrated
tolerances.
[T-T7RED] Executable reduction (verified in-repo): quasi-1D, only exit-area DOF:
(b)-(c) degenerate to <p_e(xi)> = Pa, i.e. NPR(eps*) = <Pc>/Pa — the
repo's Theorem 1 with its wrong-averaging rejector test.

==============================================================================
PART IV — THE GLOBAL-OPTIMALITY CONTRACT

"Without hypotheses" is excluded by theorem: (i) without an admissible
class no maximizer exists (vacuum: Isp strictly increasing in eps);
(ii) without a solution concept J is undefined (multi-D non-uniqueness);
(iii) without a measure the average is undefined. HYPOTHESES ARE THE
PROBLEM'S DEFINITION; the ledger instruments every one.
The contract for every delivered optimum Sigma*: EXISTENCE (P7:
Chenais compactness + S1-continuity uniform in xi + dominated
convergence; failure boundary = loss of S1-regularity, MONITORED by the
boundary function) + NECESSARY (T7 with (**')) + SECOND-ORDER
(reduced-Hessian) + GLOBALITY by a DECLARED mechanism:
 M1 duality-gap zero vs the bound ladder (J_ideal, Int-max, integral-
    flux) — certified global (T4 is an instance);
 M2 collapse transfer (T3 pointwise equality inherits classical
    globality);
 M3 monotone/unimodal structure (repo 1-DOF theorems are instances;
    target: unimodality of the truncated-plug duty variable);
 M4 exhaustive stationary-point enumeration (deflated continuation) +
    bound gap, finite-dimensional;
 M5 certified deterministic global search (Lipschitz/branch-and-bound)
    at 2-4 DOF.
Every Verdict states its mechanism and strength ("global", "within
delta of global, certified", "local + enumerated competitors").

==============================================================================
PART V — GENERALITY LADDER AND LICENSING LOGIC

The flow — not the method — selects the reduction, per design point:
| Flow class (census) | Machinery | Deliverable / rigor |
|---|---|---|
| single/k-wave rotating mode | T0 steadification (exact); rung 2 averaged + O(St) bar; wave-frame implicit BVP anchor | Sigma* + full certificate; per-phase THEOREMS, bridge CONJECTURE-with-falsifier |
| modulated / counter-rotating (RPO) | periodic BVP, unknown (Omega,T), doubly bordered adjoint; 2-D+t demonstrator | PRACTICE (space-time tracking 3-D absent) |
| multistable mode set | per-branch optimization + CVaR/DD-DRO outer layer over the mode measure | robust Sigma*; SCHEMA/PRACTICE |
| chaotic / mode-hopping | bounds + robust surrogates ONLY (shadowing refused: hypotheses fail across shocks) | honest refusal of certificates [S14 note, arbiter-confirmed: the ladder's upper wall (Prop. G-B) is PROVEN in the steady per-streamtube setting only — its transfer to the ergodic average [J_exact^-, J_exact^+] (targets per D2.2) is a NAMED MISSING LEMMA (Birkhoff + bounded momentum route) or the bound de-rates to SCHEMA on this row; cf. D5 Step 5(f) quasi-steady-only labeling] [RESOLVED 2026-08-06 (S16 T4, [S-GBE] docs/rde_nozzle_GB_ergodic.md, carrier X-GBE): the lemma is WRITTEN — under declared hypotheses (bounded storage; axially-sonic exhaust surface; admissibility) J_exact^+ <= F_env(mean interface fluxes), with the OP-0 sonic cap re-derived as the exact constrained sup (the axial margin is what makes a pointwise ceiling exist) and NO Birkhoff needed (finite-T Cesàro + bounded storage suffice — the named route was stronger than necessary). The upper wall's quasi-steady-only label is LIFTED; lower rungs (attainability) stay steady-setting; the ergodic wall is Jensen-looser than the per-phase wall where phases exist (gap reportable).] |
Licensing instruments: thrust-trace flatness (distance from
steadifiability); census refresh per accepted optimizer step (tier-flip
detection); St_n and drift numbers from the data (D1 ⊃ D2: one Strouhal
governs); mixed-interface decision tree (O1 move / O2 impedance +
mandatory coupling loop with measured q / O3 choking surrogate /
O4 anchor-always). Upstream-response model: AC part = admittance/
impedance ladder (compact linear -> O(He) -> full-frequency ->
compact-nonlinear -> state-space time-domain), exact for GRADIENTS by
definition of linearization; DC part = differentiated matched-cycle
response map; degrades declaredly at mode transitions (robust layer).
RUNG 3a-LITE (B-lite) — addendum of record (2026-07-21, S12,
[S-BLITE]): on the NOZZLE-ONLY domain with certified axial margin
u_x - c >= delta > 0 (interface data class I1, Omega an INPUT from
the data; this is the (M-a') segment certificate — D2.4 L4-CERT
(ii); interface admission on curved Gamma_d reads in the normal
form m_n, L4-CERT (i)), Lemma 4's condition C2 is SATISFIED and the exact
wave-frame field is computable by 3-D helical SPACE-MARCHING (fitted
sheet as per-station unknown, Lax in the x-as-time reading = G12-L2)
at marching cost — no Newton-Krylov global solve, no camera, no
Omega eigenvalue; the adjoint lifts verbatim by Lemma B
(x-block-triangular march => reverse-AD = transposed sweep). B-lite
is the cheap exact meter of the rung-2 sweep/D2 residual; the FULL
anchor of this Part remains necessary exactly where the camera
enters (Omega as output, subsonic pockets, reaction, R10). Named
brick to verify first: the 3-D axial-flux eigenstructure
(G12-L1-3D, symbolic carrier candidate). "Marches nothing" (Lemma 4)
remains true for the camera-included anchor; B-lite is C2 exercised
in 3-D, not an exception to it.

==============================================================================
PART VI — IMPLEMENTATION FORMULATION (what the coder builds)

VI.1 CycleFamily (contract C1; the [vorticity] placeholder is
REPLACED of record by the D.13 [MS-DEF-CONTRACT] swirl row —
DEFINITION + recovery THEOREM, landed 2026-08-19 from
phaseD_meanswirl_formalization.md §4; provenance: VERDICT_r2pass §3
+ VERDICT_escalation §4): {P0, T0, thermo handle gamma(.;xi) |
M_in(y;xi) — MERIDIONAL Mach profile (declaration of record: M_in
is meridional, never total; D.5(iii)),
theta_in(y;xi) — meridional flow angle,
s(y;xi),
w(y;xi) — swirl velocity profile; equivalently Gamma(y;xi) :=
R(y)·w(y;xi), the transported invariant (D.2 [MS-T-TRANSPORT]); the
evaluator carries Gamma as its transport row (one more
unknown/equation per unit process, VI.4bis(iv) / N6 §4 note),
h0(y;xi) — stagnation-enthalpy PROFILE (promotion of record: under
the pre-swirl contract h0 was constant in y by construction, so any
Delta_h0 monitor would have been VACUOUS — rejector-incapable;
staging Rmk 4.1, THEOREM; scalar T0 retained as the phase-aggregate
handle)} + mu weights +
provenance + stage-A audit results (characteristic completeness; Crocco
residual; spacelikeness margin declared as m_n(xi) = ess inf_y
(M_n - 1), M_n = (u n_x + v n_r)/c with n_m the meridional normal
field of Gamma_d (D.4 curved clause / D2.4 L4-CERT (i); reduces to
min(M_x - 1) exactly on planar Gamma_d; TOTAL Mach PROHIBITED as
the audit quantity); H-I2/choking
margins; projection norm if applied; T0 flatness/harmonic-decay
certificate [S14 F-FLAT: carrier + derived threshold = plan item D6
§6.5-bis; field named here so the contract cannot ship without it]),
EXTENDED by: (a) the TRIPLE spread monitor of D.14 (G6 rejector;
LICENSING leg = the TWO-leg SCHEMA gap G-b1/G-b2 — sensitivity
functional + per-campaign derived constant; every licensing verdict
carries the G-b1 conditional explicitly; BLOCKING direction usable
now, conservative);
(b) the angular-momentum audit row of D.16 (PRACTICE); (c) the m_n
margin above. Data class: rows in BV ∩ L∞(y), piecewise C¹
sufficient; through-flow sign convention declared (D.14 guard).
STATE RECOVERY: UNIQUE under AUD-cp + AUD-c2T for ALL Mach numbers
(THEOREM, gamma(T)-EXACT — two-line F′(T) > 0 proof of record;
falsifier: a table instance with two distinct recovered states) and
EXISTS only under AUD-hRANGE (flag-never-extrapolate).
BLOCKING PINS before ANY first dataset ingestion (advisory
provenance: validation/swirl5f_panel_2026-08-19/DISPATCH_swirl5f.md
§4 — panel grades are NOT record grades):
 (B-1) A4 NORMALIZATION PINNED: the corpus "tangential energy
 fraction 3-6%" figure is KE-NORMALIZED; the h0-normalized reading
 is ~4x smaller (0.3-2.5%); discriminating test: only the KE
 reading gives Omega·r ≈ D_CJ; the D.10 falsifier must NEVER fire
 on a unit mismatch — the A4 convention is a declared field of the
 audit.
 (B-2) h0-CONVENTION PROVENANCE CLAUSE: whether the generator's
 h0(y;xi) includes u_theta²/2 is a REQUIRED declared field of the
 contract (it decides the B2 fold/drop variant); rejector: the D.20
 Delta-h0 = Omega·Delta-Gamma linkage fires on
 convention-inconsistent data.
Generators: matched-cycle (case
A, exists), wave-structure model (case B, the one new physics module),
calibrated/mission/DRO variants (cases C-F), file-based CFD.
GENERATED data passes the same audits as imported data.
VI.2 Per-phase evaluator: rotational MOC (Zucrow Ch.17 class; GENO
MoC_Gen semantics), gamma(T) backend, FITTED inherited sheet (RH on the
front), plug off-design free-boundary march, separation-criterion hook;
S1 monitor = closed-form boundary function
val = [Lam·B·(A+B) - (A-B)]/[1 + Lam·(A+B)], A = tan(theta-alpha),
B = tan(alpha), Lam = V dalpha/dV (gamma-free); unit processes O(h^2).
VI.3 Per-phase gradient: closed-form adjoint where smooth (= f2
invariant + corner residuals: shroud/bell CSTR_PA
p_a = p - (1/2) rho V^2 sin(2theta) tan(alpha); plug CSTR_PB with +
sign — the sign from the CHARACTERISTIC TYPE). CONE RE-STATEMENT OF
RECORD (C31, user-ratified 2026-08-13): at unilateral endpoint caps
CSTR_PA/CSTR_PB are INEQUALITY + COMPLEMENTARITY statements on the
admissible cone {Dx <= 0} INTERSECT {Dy <= 0} (direction derived
from the active side, KT2015 (2.10); the terminal face carries the
"if exists" qualifier) — equalities only in the free-endpoint or
pinned regimes; every printed (**') residual DECLARES ITS REGIME
(free / pinned / unilateral) in the Verdict; reverse-mode AD of the
fitted march elsewhere (implicit-function custom rules on inner
iterations, never unrolled; differentiate the fitted front, never a
captured smear). Certificates: dot-product to machine precision (O3);
Hoffman E-residual -> 0 along optimized contours.
VI.4 Cycle layer: locate switch phases xi*(Sigma) (separation onset,
adaptation, sheet-entry) by root-finding; SPLIT Gauss panels there
(else O(1/N) + noisy outer gradient — the practical convergence trap);
Leibniz terms cancel by continuity of F (verified).
VI.4bis Algorithmic consequences of the standing scopings (2026-07-16,
S5/S6 directives; AMENDED same day on user clarification: the
periodicity assumption describes the EXPECTED DATA and sets theory
priorities — it must NOT condition the algorithm, which stays FULLY
GENERAL; periodic structure is EXPLOITED AT RUNTIME when certified,
never assumed structurally. The skeleton of VI.1-VI.7 is UNCHANGED —
these pin down choices inside it):
 (i)  QUADRATURE IN xi: the GENERAL rule of VI.4 (Gauss panels +
      mandatory switch-splits at xi*(Sigma)) is the baseline for
      arbitrary mu; WHEN the data are certified periodic and smooth
      (T0 flatness certificate + harmonic-decay audit) the layer MAY
      switch opportunistically to trapezoid-on-the-circle (spectral
      accuracy), still composed with the switch-splits. Data-driven
      selection, never a structural assumption.
 (ii) O(St) CORRECTOR: BOTH routes live in the pipeline — the general
      route (unsteady comparison, O5) always available; the steady
      sweep-perturbation solve on the wave-frame anchor (one
      linearized solve, C-T1 periodic re-scoping D3 §3) engaged WHEN
      T0 applies (certified single/k-wave mode). The cheap route is a
      licensed specialization, not a replacement.
 (iii) GAMMA DIRECTIVE (unconditional): thermo backend EOS-general
      (Cantera h(s,P) class) mandatory; the gamma=const corner<->eps
      bijection is FORBIDDEN as a solver step (enforce f2 = const
      actively; E4/G2 oracle gates any closed-form shortcut).
 (iv) ROTATIONAL DATA (unconditional): per-phase adjoint at the FIELD
      level (reverse-AD of the fitted march = discrete adjoint sweep,
      Lemma B); the two-field closed form (Prop. A3) serves as
      ORACLE/INITIALIZER only; cheap per-phase certificates: f2-drift
      and Hoffman-E residual along each phase's terminal
      characteristic, lambda2(xi) = -f2(lip data) as the closed-form
      multiplier initializer (P3 theorem).
 (v)  ROBUST LAYER (CVaR/DRO over the mode measure): PART OF THE
      GENERAL ARCHITECTURE, engaged whenever the data warrant it
      (multistability declared, or the flatness monitor rejects mode
      purity); idle — not absent — on certified-periodic data. The
      flatness monitor itself is mandatory in every data contract.

VI.5 Optimizer: TR-SQP on spline DOFs; gradients Riesz-represented in
a Sobolev/Steklov-Poincare metric (mesh-independence); active-set
constraints {L, eps_max, lip, truncation} with multipliers reported as
MARGINAL VALUES; bundle safeguard near persistent kinks; deflated
continuation for stationary-point enumeration; sector tournament for
topology; seeds: Rao-at-<Pc> (bell), peak design (plug) — provably
near-optimal for weak violations (P6), never affecting the certified
result (a-posteriori certification).
VI.6 Certificate stack per Verdict: KKT + (**') residuals; reduced-
Hessian spectrum; dual-route agreement (B1 NLP vs B2 collocation of the
optimality system); ORACLES (O1: T3-family in ⇒ Rao-at-<Pc> out with
Delta-Isp = 0; O2: ideal plug ⇒ peak design; O3 dot-product; O4
freezing-adjoint dOmega/dSigma vs FD of continued waves; O5 unsteady
sim vs J_avg + St·J1); DWR discretization bars; bound-ladder gap +
globality mechanism; O(St) and D2 physical bars; data provenance +
margins. NOTHING SHIPS OUTSIDE A VERDICT.
VI.7 Tooling: JAX (custom_vjp + implicit rules) or Julia/Enzyme;
GENO-Fortran as independent reference (dual-code); Newton-Krylov +
Arnoldi for the anchor; implicit shock tracking (HOIST class) for
wave-frame solves; known GENO prerequisites: RaoPlug S1/S2 fix (mass
multiplier + 2nd DOF) gated by the Rao-1961 spike Table-1 oracle
(M_E = 2.4, theta_E = -8.25 deg, gamma = 1.23 -> eps = 3.81,
X_D/R_E = 1.164, C_F = 1.58).

G0 DECISION AND DUAL-CODE EXERCISE OF RECORD (2026-07-17, [F2/G0],
session S10; work-layer, registry [DIR-G0]; D6 gate G0 = DECIDED):
the tool choice above is now DECIDED — JAX primary (custom_vjp +
implicit rules), Julia+Enzyme declared alternate, GENO-Fortran the
independent dual-code reference. The dual-code interop that this
section asserts is now EXERCISED, not deferred: GENO was built
(WSL gfortran 11.4.0, CMake, Cantera/Sundials/Tecio OFF, LAPACK from
the host conda env — GENO never modified/committed) and the TOC case
tocnoz regenerated; the design contour reproduces the committed
reference to 1e-10 (printed precision, toolchain-invariant), while the
full-precision field dumps differ only by the documented toolchain md5
convention (N-36) — same physics. The FLOWFIELD cross-code oracle
[X-GENOXC] certifies that GENO's Fortran MoC nodes satisfy OUR
EOS-general second-order axisymmetric (u,v) unit process within the
derived per-cell truncation band (100% of the clean supersonic core;
two negative controls reject) — i.e. the differentiable engine's cell
map and the Fortran reference discretize the SAME continuum. Full
decision dossier: docs/rde_nozzle_G0_decision.md. Consequence: Phase
A1 (differentiable per-phase engine) OPENS, with [X-GENOXC] as its
standing cross-code regression.

A1 BRICK 1 OF RECORD (2026-07-20/21, [F2/A1], session S11;
work-layer; registry [X-A1IM], standing directive [DIR-THERMOTAB]):
the PROFILE-GENERATION MACHINERY exists and is certified. The
assembled differentiable MoC march (validation/a1_ideal_march_jax.py)
GENERATES the ideal-nozzle contour end-to-end — Sauer IVL ->
characteristic fan -> circular-arc throat expansion (inverse-wall unit
process with GENO's chord-foot search and void-row bookkeeping,
wall-angle refinement to axis M = Me) -> uniform-exit region with the
WALL AS THE BOUNDING MASS-FLOW STREAMLINE — as the twin of GENO
nozzle_type 0, with every cell an implicit custom_vjp unit process
(implicit-function rule, never unrolled), so reverse-mode AD of the
assembled march IS the Lemma-B discrete adjoint sweep, executably.
Verdict of record (reduced case NI = 21, da = 0.5 deg, Ne = 41,
eps = 4, CH4/O2 frozen): generated contour vs the GENO WSL run inside
the derived two-resolution Richardson band at 62/62 samples with
max |dy| = 7.6e-9 (band 4.5e-3; median err/band 0.000) — agreement at
GENO's own predictor-corrector tolerance, far below truncation;
achieved Me twin-identical to 8.4e-9; O3.1 dot-product over the
ENTIRE march |<w,Jv> - <J^T w,v>| = 2.7e-10 vs derived tolerance
5.1e-8 (replay fidelity 1.6e-13); per-cell UNIT-CONSISTENT Newton
certification in z-space (2756 cells, worst step/tol 1.4e-2);
negative controls reject (corrupted source cannot reproduce GENO,
corrupted whole-march vjp breaks O3.1, corrupted thermo table and
corrupted gamma rejected). THERMO BACKEND PIN of record (standing
user directive S11, [DIR-THERMOTAB], strengthening VI.4bis(iii)):
JAX engines READ TABLES (the GENO backend-1 / ATLAS-FLINT model) —
the march consumes interpolated (h, s0, cp)(T) tables with derived
table-density floors; CANTERA is the SOLE PRODUCTION table generator
(the GENO NASA-polynomial generator is confined to declared
cross-code oracle instances; gamma = const tables only as declared
known-answer oracles). Consequence: DIR-G0's honest scope guard ("no
JAX-generated contour exists yet") is DISCHARGED for the ideal
(direct-march) nozzle type; the VARIATIONAL TOC brick — thrust
objective + {eps, L, lip} constraints with the (**')/corner
transversality imposed through the dJ/dSigma gradient, never a
hard-coded outer loop — is the NEXT A1 brick; the G0 loop-speed
falsifier stays armed (production-scale march not re-adjudicated).

A1 BRICK 2 OF RECORD (2026-08-06, [F2/A1], sessions S17-S18;
work-layer; registry [X-TOCV], policy [DIR-RKG]; logs S17 steps 4-11
+ S18 steps 3-7): the VARIATIONAL TOC ROAD EXISTS END-TO-END and is
certified. The specified-wall TOC march (design vector W = attachment
angle theta_B + clamped-spline wall nodes; arc-kernel geometry rtu/
rtd as fixed inputs, GENO-twin contract) is recorded adaptively with
per-cell Newton certification AND the per-cell AXIAL-MARGIN rejector
(u_x - c > floor — the x-as-time causality the L-DoD truncation
lemma requires; an (M-a')-class segment certificate per D2.4
L4-CERT (ii); instance floor delta = min_margin(base)/K_RICH =
0.1202 m/s on the reduced twin case), replayed by the bucketed
whole-loop-jit production engine (bit-level equivalence to the
certified replay; O3.1 transpose identity = the Lemma-B guarantee,
executably), and optimized by scipy trust-constr under the RK-G
segmentation policy with measured Jacobi scaling + a measured full
Hessian at every segment base (freshly measured per stratum — no
curvature carry-over, DIR-RKG-conformant). VERDICT OF RECORD
(reduced twin case, C^1 quintic closure primary): from a 1.5%
PERTURBED start the optimizer RECOVERS AND EXCEEDS the
GENO-projected seed (J* = 2.7761688e+07, +1.06e+04) and reaches
in-stratum stationarity KKT = 7.745e-02 <= derived gtol 1.156e-01 —
the TRANSVERSALITY INSTANCE: the Rao optimality conditions REACHED
VIA THE GRADIENT, never imposed by an outer loop; the optimum
contour agrees with the INDEPENDENT classical route (GENO type-2
Mrao/eps bisection) at 91/91 samples inside the derived cross-code
band (GENO cross-resolution + spline-class representation +
reference-resampling terms, neighborhood-enveloped; max|dy| =
1.861e-03, median err/band 0.102), with the N3 wrong-design
discriminator firing. DECLARED GOVERNANCE RESIDUE: the T2
practicality falsifier FIRED on the twin case (121.6 s vs 35.9 s;
decomposition = curvature measurement + RK-G re-record cost, NOT
language throughput — T1 = 1.593 and T2a = 0.116 s vs 1.197 s both
PASS with margin) => G0 re-decision review queued per the D6 flip
clause; named levers for scale: second-order implicit rules (exact
Hessian-vector products), colored/sparse FD Hessians, benign-flip
refinement of DIR-RKG (each a declared future brick, none executed
silently). CONSEQUENCE: D6 item 9 CLOSES; **O3.3 IS UNLOCKED** (the
pre-registered bench protocol P2_outline §5, untouched, becomes
executable against this engine — P-2's numeric half).

O3.2/O3.3 CAMPAIGN OF RECORD (2026-08-06, [F1/P-2], session S19;
carriers [X-O32], [X-O33B]; full numbers and the honest residues in
P2_lemmaA §3.7 and the S19 log). Class of the campaign: PRACTICE
(measurement) — it discharges numeric conditionals, it does not by
itself move a rigor class.
 THE LOCUS, first, because the campaign got it wrong before it got it
right: Rao's control surface is the C+ through the lip traced BACK and
STOPPED AT THE KERNEL BOUNDARY (the last C- emitted by the fixed
throat arc), not the whole C+ down to the axis. Measured on the full
chain, f2 drifts 2.9e-01 and identification (ii) looks falsified;
measured on the classical surface it is constant to 9.5e-03. The wrong
number is recorded alongside the right one because it is the one a
reader repeating the experiment would otherwise reproduce.
 WHAT THE BENCH ESTABLISHED. (1) f2 = -lambda2 is constant along the
control surface for the S18 converged design (2665.38, drift 9.5e-03)
AND for GENO's own Rao contour marched by the same engine (2666.03,
drift 8.0e-03), the two Rao CONSTANTS agreeing to 2.4e-04 — an order
of magnitude inside either drift, so the residual is the instance's
discretization, common to both designs. (2) The adjoint compatibility
relation of the classical corpus cancels to 1.6e-04 (C+) and 2.3e-04
(C-) in the Prop. A3 gauge on our field, and saturates at exactly 1.0
with the wrong sign per family — the sharpest rejector in the bench.
(3) THE PRIMARY KILL CRITERION PASSED: on a feasible family around the
optimum the AD directional derivative and the classical Rao residual
vanish at the SAME design inside the derived bar. (4) The corner
identity of identification (iii), dJ/dy_lip = 2 pi y_E [p_E - (1/2)
rho W^2 sin(2 theta) tan(alpha)], holds to 6.6e-02 on the 8-node
design — MESH-INDEPENDENT — and to 2.0e-02 on a faithful Rao wall at
the same mesh, falling further under refinement there: an identity of
the CONTINUUM optimum, converging in both limits, NOT confirmed at a
Richardson band on a finite-dimensional instance. [C-O33] stays open
with its residual quantified and its dominant term identified as the
DESIGN CLASS.
 THE HONEST RESIDUES. (i) The adjoint's convergence EXPONENT is not
measurable on a refinement ladder: refinement cannot hold the march
topology fixed, which is exactly clause LB-c2 of [S-LBML]; a
fixed-topology experiment is owed. (ii) The ideal twin's rows are
capped IN PART by a mirrored GENO algorithmic constant (the
|M - Me| < 1e-5 exit test) acting as an accuracy FLOOR on the achieved
exit Mach — critical-list item 3, now measured rather than suspected.
Its PRE-DECLARED diagnostic ran (hypothesis and test committed before
any four-level rate existed): tightening the constant 100x collapses
|dMe| from 1.5e-05 to 1.1e-08 and makes it monotone, so the floor is
REAL; but the rows do NOT recover (primal dp_tot 2.12 -> 1.46, still
non-conclusive; adjoint still not usable), so the constant is
ATTRIBUTED as a floor and EXONERATED as the binding cause, leaving the
topology mechanism of (i) as the only candidate standing for the ideal
twin too. No band was amended in either direction. (iii) The
design class (8 uniformly spaced nodes, natural cubic spline) is
instance-tuned and is what limits the corner row; its discharge is an
adaptive error-driven knot construction, not more uniform nodes.
(iv) Two data defects of GENO's profile output, found while consuming
it: the exit wall point is emitted twice 3.8e-6 apart in x (poisons
any spline fit at the lip), and the ATTACHMENT angle is not the
maximum wall angle (16.90 deg vs a peak of 18.83 deg) — the S18 seed
recipe took the peak.

ADAPTIVE DESIGN CLASS — DISCHARGE ATTEMPT, STATE OF RECORD
(2026-08-07, [F1/P-2][F2/A1], session S20; carrier [X-AKNO]; survey
decision in D6 item 9; runs stopped by user order mid-campaign).
Class: PRACTICE (measurement + engine work). BOTTOM LINE: the
discharge procedure for residue (iii) above is BUILT and its first
obstruction is characterized to the extent the stopped runs license;
[C-O33] is NEITHER discharged NOR falsified — the pre-declared kill
test ([D1], S20 gate) was never reached.
 THE FORMAL PROBLEM, made explicit by this session (previously
implicit): the engine's optimization is
    max J(W)  s.t.  the eps equality,  W in C_m(xi),  AND  W in K,
where K is the CERTIFIABLE SET — the designs whose adaptive record
passes every record gate (per-cell while-Newton metric <= the
certification floor NEWTON_TOL_FACTOR*eps*scale; axial margin above
the floor). K never bound the S18 walk (8-node class), so its
existence was invisible; the enriched class made partial(K) reachable
inside the trust region. Two structurally different terminations
follow, and they license DIFFERENT measurements: (I) interior
stationarity — KKT closed at the S18 gate (status converged,
optimality <= 10*gtol, feasibility <= gtol) — licenses the corner-row
measurement, because identification (iii) is DERIVED FROM OPTIMALITY
and [X-O33B]'s own control says the identity must BREAK at a
non-optimal design; (II) boundary-limited — KKT open — licenses ONLY
the certified-objective report; feeding such a design to the corner
row would confound class error with non-stationarity, so [D1] is
DEFINED ONLY over outcome-(I) designs (validity condition fixed in
the S20 log step 7 BEFORE any decisive run). Further, K = K_phys
intersect K_budget, with K_budget the part cut by the while-Newton
TRIP CAP N_NEWTON = 30 — a compute budget, not a tolerance; the
armed (not yet run) certdiag separates the two by re-recording a
rejected design with the cap raised and the floor untouched. Only
K_budget may ever be enlarged; the certification floor is a
tolerance and does not move.
 WHAT IS MEASURED (carrier committed, numbers from the printed
attempt logs, reproduced identically across attempts 1 and 2):
 (1) THE RESIDUAL IS CONCENTRATED: the f2 (= -lambda2) drift per
control-surface segment, attributed to the emitting wall station
through the march topology, puts 41.8% of its mass in the FIRST knot
interval after the attachment, 18.9% in the second, 17.6% in the lip
interval, 2.3% in the flattest — max/mean concentration 3.34 on a
wall whose 8 nodes are uniform. First direct, spatially resolved
evidence for the S19 design-class diagnosis beyond the two-knob
ladder: the optimality residual lives where the wall turns, and
uniform nodes misallocate the dofs.
 (2) THE INDICATOR IS GOAL-ORIENTED BY CONSTRUCTION: f2 IS the
adjoint variable of Prop. A3, so its segment drift is an
adjoint-weighted optimality residual — the object DWR weighting
constructs — adjudicated over a plain data-misfit indicator in the
S20 survey.
 (3) THE ENRICHED CLASS BUYS OBJECTIVE, WITH THE NUMBERS SPLIT BY
CERTIFICATION STATUS (a distinction the first draft of this block
got wrong; corrected in the S20 log step 7 audit): two
Doerfler-marked knots (8 -> 10 dofs, inserted at x = 0.3146 and
0.7026 from an attachment at xB = 0.121) carried the walk from the
S18 J* = 2.7761688e+07 to J = 2.7775368e+07 at the LAST CERTIFIED
accepted design (+1.27e+04), KKT falling 1.726e+06 -> 5.056e+04
along the certified prefix. The optimizer's next Newton target,
J = 2.7775635e+07, is UNCERTIFIABLE (one cell's certification
metric at 2.458x its floor) and no J from it is claimed.
 (4) ONE UNCERTIFIABLE TARGET DESIGN IS MEASURED — NOT a boundary:
the defective shrink (defect 2 below) re-proposed the SAME design
bit-identically (J, KKT, cert_worst identical over segments 7-17),
so the walk never tested shorter steps. Whether a certifiable ascent
continues past J = 2.7775368e+07 (boundary further out), stalls
(genuine boundary), or the obstruction dissolves under a larger trip
cap (K_budget artefact) are the three OPEN hypotheses; the
discriminating measurements are pre-declared: the ratcheted-shrink
walk and the certdiag.
 (5) TWO DRIVER DEFECTS OF RECORD, both exposed by the enriched
class, both fixed policy-conformantly, fixes selftested but NOT yet
exercised on a decisive run (declared): (a) DIR-RKG P3(ii)
certification of ACCEPTED iterates was in the policy text but absent
from the code, and the record-failure recovery restarted from the
failed iterate itself; (b) the post-rejection shrink was undone by
the callback re-capturing scipy's regrown radius — the measured
livelock. The driver now certifies every accepted iterate, RATCHETS
the radius bound downward on rejection, and on exhaustion RETURNS
the last certified base flagged certifiability_limited with the KKT
reported OPEN (outcome II above) instead of raising mid-walk.
 ATTEMPT 3, THE DECISIVE RUN OF RECORD (fixes held; certdiag 8/8;
S20 log step 8): the ratcheted walk crawled ALONG the certifiability
frontier with certified progress — rejections at FIVE distinct
nearby designs (cert_worst 1.170, 2.458, 1.060, 1.455, 1.698, each
bit-identical under N_NEWTON 30 -> 300 with the floor untouched =
the trip-cap/K_budget hypothesis dead eight times over) while the
certified objective advanced to J = 2.7775702e+07 (+1.40e+04 over
the S18 8-node J*, own-plan P4-audited record) and the KKT fell
1.726e+06 -> 3.795e+02, still ~400x above gtol. The global min
axial margin stayed AT the baseline value 0.4809 m/s: causality-
margin erosion is EXCLUDED as the mechanism. Reading of record: an
ACTIVE-CONSTRAINT signature — the ascent direction leaves the
certifiable set from every certified base near the frontier — so
outcome II is the necessary end state of the UNCONSTRAINED-form
walk, [D1] stays untestable there, and [C-O33] is NEITHER
discharged NOR falsified by this campaign.
 THE CLASSICAL CONNECTION (page-verified 2026-08-07: Rao & Beck,
AIAA 94-3264, pp. 1-4 READ IN FULL; GENO Profile_m.f90 DEF branch
READ. CITATION STATUS — SUPERSEDED 2026-08-12 (S24 R4, executing
duty D-A of ADVISORY_generality_litmap_2026-08-12 / dispatch A1):
BOTH primaries are ON DISK and READ IN FULL, TWICE, page-verified
by the generality-review refuter — Sternin = literature/dan25254.pdf,
the RUSSIAN ORIGINAL, DAN SSSR 139(2):335-336 (1961) (the Rao-Beck
Ref. 3 "Sov. Phys. Dokl. 6(7), Jan 1962" is its translation);
Shmyglevskii = literature/0041-5553(80)90091-9.pdf, USSR CMMP
20(5):113-127 (journal issue 1980, (c) 1981 Pergamon —
translation-year discrepancy noted, reference verified exact). The
O3 hard gate therefore moves from ACQUIRE to ADJUDICATE; the O3
comparison set is TWO-SIDED of record (dispatch A2): the Rao-Beck
D'-jump (admissibility restoration ON the boundary) AND
Shmyglevskii's SECOND SCHEME (discontinuous SHOCKLESS solutions
from variational corner conditions, his Eq. (7), completeness map
Fig. 4 claiming THE optimum for all nozzle dimensions — a STRONGER
classical object; its CONTACT front needs a certificate class of
its own, F4b open item). Historical wording kept for the record:
until 2026-08-12 both were cited VIA the Rao-Beck reference list
only): the forbidden zone has a classical name — Sternin's
boundary — with Rao-Beck Eq. (4) (the 1994 paper's numbering, of
record per dispatch A4) as its closed form at the kernel/
control-surface junction, their Eq. (1) being literally our f2
invariant;
minimum-length optimum-thrust nozzles sit ON that boundary; the DEF
construction goes beyond it via an isentropic Prandtl-Meyer
compression coalescing EXACTLY AT the control-surface point (zero
interior shock extent, isentropic upstream, shocks only downstream
of the surface; Shmyglevskii 1981 for the variational treatment;
-22% length at -0.3% thrust, slight advantage at equal length), and
GENO implements it in production (type-2 flagdef, DE<->BD mass
equality as the design constraint). Coalescence-shock caveat of
record: envelope geometry does NOT determine an interior shock's
position/strength — Rao-Beck avoid the interior shock by
construction (inverse method); the general rigorous treatment makes
the front an UNKNOWN of a fitted solve.
 GENERAL FORMALIZATION OF RECORD (the most general the corpus
supports; classes declared per item). The design problem is posed
on a LADDER of certified solution classes:
   (P_t):  max J(Sigma)  s.t.  g(Sigma) = 0 (eps, L),
           Sigma in C_m INTERSECT A_t(mu_0),
 where A_t(mu_0) = { Sigma in C_geo : P(Sigma) has a solution in
tier t's class with margin vector m(Sigma) >= mu_0 > 0 }, the
margin vector collecting the FOLD margin (distance from same-family
characteristic coalescence; classically Eq. (4)/Sternin at the
junction), the CAUSALITY margin u_x - c (the (M-a') segment
reading, D2.4 L4-CERT (ii); m_n on curved Gamma_d), and the uniform constants
of the certified class D(delta, L_x, C_geo, C_dat, h_min). Tiers:
S_0 (shock-free, the current engine) SUBSET S_1 (finitely many
FITTED fronts under RH + entropy + Lax + Lopatinskii certificates —
the G12/F2 line; DEF = the zero-interior-extent limit) SUBSET ...;
the nesting is trivial and gives sup J monotone in t. First-order
optimality at a boundary-active optimum is the KKT WITH THE MARGIN
MULTIPLIER, grad J = lambda grad g + mu grad m, mu >= 0 — the term
the S18/S20 formulation lacked, which is why the unconstrained-form
KKT could not close; and the measured multiplier mu at a
margin-constrained optimum PRICES shock-freeness: it is the
quantitative criterion for opening tier 1.
 CLASSICAL ATTRIBUTION OF RECORD (C30, user-ratified 2026-08-13,
GATED — Shmyglevskii 1962 unread, WANTED row in the literature
registry; upgrade from "classical structure" to "classical system"
is gated on reading it, R28): the STRUCTURE "at inadmissibility of
the continuous construction the necessary conditions become
INEQUALITIES" is CLASSICAL (1961-62) — Sternin 1961 (boundary of
constructibility of the continuous field) + Shmyglevskii, PMM
26(1):110-125 (1962) (necessary conditions in inequality form),
according to the account of Kraiko et al. 2001 p.1348 col.2 (a
party to the priority dispute), with DIRECT page-verified
counterproof in KT2015 p.186 Eq. (2.10) (delta R <= 0 on admissible
variations => inequality + complementarity, slack on the "region of
boundary extremum"). OURS: the quantified margin m(Sigma) (fold
Eq. (4)/Sternin, causality u_x - c per D2.4 L4-CERT (ii), uniform
constants), the
MEASURED shadow price mu pricing shock-freeness, the certified
ladder with the nesting theorem, the KS aggregation at derived rho,
and the B-stationarity qualifier. DECLARED ASYMMETRY (carried with
every presentation of the ladder): the classical response to
inadmissibility is to CHANGE CLASS (construct the discontinuous
optimum = our tier 1); ours is to PRICE STAYING in tier 0 — in a
precise sense the corpus goes further: it constructs the object we
cannot yet certify (R16). Rigor classes: the
nesting and the constrained-KKT structure are THEOREM (standard);
the ladder and A_t definitions are SCHEMA; "the S20 instance
optimum is boundary-active" is a measured-supported HYPOTHESIS (the
crawl + 8/8 genuine); "the discrete certifiable set K approximates
A_0" is a CONJECTURE with a named falsifier — evaluate the
Eq. (4)/Sternin validity relation (translated across the
Rao-vs-Zucrow characteristic-naming inversion) along the walk: it
must approach its boundary where certification degrades, else the
bridge is dead. TAXONOMY ANCHOR (surveyed 2026-08-07, S20 log step 9: the
Le Digabel-Wild "Taxonomy of Constraints in Simulation-Based
Optimization", the canonical frame for constraints of this kind):
in that taxonomy the certifiability constraint is TODAY of class
Known-Unrelaxable-Simulation-NONQUANTIFIABLE — the optimizer learns
only pass/fail, after paying a march, and a failed record yields no
usable J; the taxonomy names this the worst tractable kind, and the
recognized remedy, WHEN the physics exposes one, is to QUANTIFY a
margin. The margin-constrained reformulation is exactly that move:
m(Sigma) makes the constraint quantifiable BEFORE violation, with
its gradient free through AD, aggregated by Kreisselmeier-
Steinhauser (the standard aggregation for min/max constraint fields
under adjoint sensitivities; conservative side correct; adaptive-
parameter variants exist and are the current refinement). Discharge
routes adjudicated for S21 (S20 log step 9d): tier-0
margin-CONSTRAINED re-optimization (KS-aggregated fold margin,
derived floor, AD gradient; Eq. (4) as classical cross-check
monitor); tier-1 fitted-front optimization as the general rigorous
method (captured-shock adjoints rejected per Giles-Ulbrich/Lozano;
the tier-1 method's own survey is QUEUED to the G12/F2 session, not
claimed done); the S19 fallback (publish with the two-knob numbers)
standing at every gate.

[S21 REGISTRATION BLOCK — EQ-v2, THE Lambda-FORM VALIDITY MARGIN,
AND THE OBLIGATIONS LEDGER] (2026-08-11, [F0/ORDER] of plan v3,
session S21; panel wf_706f7901-32d ABSORBED AT THE RED-TEAM-CORRECTED
FOOTING — ADVISORY_redteam_2026-08-11 applied BEFORE absorption, per
the dated user addendum; nothing below is promoted above the raw
panel positions).
 EQ-v2 OF RECORD (the DEF-equivalence statement; supersedes the
unqualified EQ, which is REFUTED and non-citable). SCOPE: fixed
(eps, L) in the DEF regime, bell single-wall, homentropic-
homoenergetic core, perfect gas for the classical side. SPLIT
STATEMENT: Direction A [CONJECTURE on SCHEMA footing] — the
classical Rao-Beck DEF construction (single PM jump landing on the
validity boundary at D', E by DE<->BD mass equality) is, in the
joint continuum limit (h -> 0, KS rho -> inf, mu_0 -> 0; limit
order = obligation O5), a margin-active KKT point of the direct
problem, its fold touching the domain only at D' (under H-int).
Direction B [CONJECTURE] — the converse holds ONLY under H1-H6 PLUS
H7-SEL (selection/global-max among margin-active KKT points — the
red-team-restored hypothesis covering KKT nonuniqueness; without it
"coincides" is ill-posed), and speaks of the classical DEF
CONSTRUCTION, not its optimality (the optimum wording awaits O2/O3
— a DECLARED weakening, not an oversight). COMPONENT S4 [THEOREM]:
the Lambda-form boundary (G) with the perfect-gas Lambda reduces
EXACTLY to Rao-Beck Eq. (4) (hand proof + independent judge
re-derivation + the [X-VMON] machine identity at the roundoff floor
over a 247-point grid, executed S21). S1 SPLIT VERDICT: limb-2
(fold-on-boundary + interior pointwise certification) HOLDS
[SCHEMA, under H-int]; limb-1 (closure membership of the DEF wall
in cl(K)) OPEN pending approximant existence. S20-STANDOFF READING
OF RECORD (RT-1): the fixed-floor standoff is CONSISTENT WITH a
DEF-sector optimum AND equally with an interior-binding tier-1
optimum until O4 localization runs (the 41.8% attachment
concentration itself suggests interior binding); the fixed-floor
exclusion of the exact DEF wall is the REFUTER'S argument, experts
consistent-with.
 THE (G)/Lambda-FORM VALIDITY MARGIN, both bounds ADOPTED [S4]:
   (G)  val = [Lam*B*(A+B) - (A-B)] / [1 + Lam*(A+B)],
        A = tan(theta - alpha), B = tan(alpha),
        Lam = V d(alpha)/dV on the isentrope (AD through the
        tabulated backend — [X-VMON], KAT'd vs the closed form at
        gamma = 1.4 to 2.7e-13 inside a derived two-resolution
        band),  val > 0 = valid side.
   BOUND (a): EOS-GENERAL but NOT DATA-GENERAL — homentropic-
   homoenergetic (single-isentrope alpha(V)) data only; the
   stratified (q; s, h0) extension is OWNED BY F2 (exit gate).
   BOUND (b): the GENO implementation magics (dV_pert = 1.0,
   |den| < 1e-10 fold guard, PM landing window) are PRACTICE,
   tracked, NOT adopted here (AD Lambda; den reported, not
   guarded); their derived bands are an F1-entry duty.
   Classes: (G) derivation = THEOREM-level algebra (proof advisory,
   ratified); the monitor = PRACTICE carrier; K_disc ~ A_0 bridge
   stays CONJECTURE with THIS monitor as its named falsifier.
 FIXED-EPS TRANSVERSALITY BOOKKEEPING (lambda_e): Rao's Eq. (14)
free-endpoint corner condition is REPLACED, at fixed (eps, L), by
the lip-constraint multiplier lambda_e = dJ/dy_lip — the measured
corner identity of [X-O33B] R3; the classical reading pa/p_E is NOT
required to vanish (it equals the constraint's shadow price;
measured cross-design agreement 2.803e-03 of record, S21 re-issue).
[C31 note of record, 2026-08-13: this bookkeeping IS the pinned
(K = {point}) regime of the T7(c) cone form — an embryonic regime
declaration already in place, now named; lambda_e sign is FREE
here, and the dual-feasibility (sign) content exists only in the
unilateral-cap regime — see Part III T7(c) cone form.]
 RAO-vs-ZUCROW CONVENTION TRANSLATION (of record wherever D' is
discussed): Rao 1958/Rao-Beck name the left-running characteristic
C+ where Zucrow-Hoffman/GENO name it C-; this repo follows GENO —
Rao's "left Mach line DE" IS our C+ chain traced back from the lip;
the plug/C- mirror of (G) is UNPROVEN (panel scope limit, F3 entry
duty).
 OBLIGATIONS LEDGER (each with phase OWNER; blocks claim promotion,
never work): O1 Danskin/Clarke cusp derivative (until discharged
the margin-active KKT is B-STATIONARITY ONLY — no multiplier mu is
defined) -> F4b theory WP. O2 Rao wall<->surface duality in the
certified class -> F4b theory WP. O3 classical jump-depth
optimality (Sternin 1962 + Shmyglevskii 1981 PAGE-VERIFY = hard
gate for ANY classical-optimality claim; interim wording capped at
direct-side surplus prediction) -> paper claim gate (F1b/F4b).
O4 localization logs (argmin-margin cell + active-cusp census on
every walk) -> F1 consumption; the F0 instrumentation is ARMED of
record: [X-TOCV] cert-argmax/argmin localization (env
A1_CERT_ARGMAX, additive default-off), rejected-design persistence
in the driver (result dict + env A1_REJ_SAVE), and the [X-VMON]
monitor. O5 h -> 0 vs mu_0 -> 0 limit order -> F1b named
conditional (optional floor-ladder discharge). G1 extended-value
margin surrogate at failed marches (finite negative, from the
partial march, REJECTOR-GATED) -> F1, elevated to the D6
TIER-INVARIANT clause (REQ-NONSTALL + G1 + transition duty = every
margin of every tier/class). RT-4 DEMOTION of record: the GENO
deeper-jump companion test is a SIGN TEST for Direction A — not
decisive for O3; magnitude claims blocked until the
dJ/d(depth) = -mu*dm/d(depth) derivation under H3 and the
mu-estimator band exist.]

[LAND-C4-LA2 NTF DERIVATION BLOCK — NEWTON_TOL_FACTOR THEORY HALF
(engine-discipline / certificate block, landed S-FOUNDATIONS-C4
2026-08-21). Executes VERDICT_escalation_c4 LA-2(ii) (escalation E-1
CLOSED DRY at round 2). Carrier of record: validation/
sfoundations_raws_2026-08-13/phaseD/phaseD_minor_ntf.md as revised
through [ESC-r2-*] + the [ESC-J1-NTF] judge-ordered pre-step; labels
per VERDICT_escalation_c4 §5.1. SITE DECLARATION: M0 prints no
literal "C20 kappa-band program" block — this landing sits beside its
M0 face, the certification-floor text of the block above (per-cell
while-Newton metric <= the certification floor
NEWTON_TOL_FACTOR*eps*scale; trip cap N_NEWTON = 30), and preserves
the ONE C18/C20-Tier-1 window seam: the per-cell floor MEASUREMENT
stays inside F2-C20-CERTQUAL-CAMPAIGN Tier-1 (window shared with C18,
VERDICT_wave2 §2.8); C34's TR floor, C35's xtol_u arithmetic, and the
Tier-1 kappa band itself are consumed as-is, never re-derived here.
 OBJECT UNDER DERIVATION: the Newton loop exits when the undamped
step satisfies step <= T(z) := NTF*EPS*sc(z), sc(z) = max(1, max|z|),
EPS = float64 machine epsilon, cap N_NEWTON = 30 (C17);
certification = one extra Newton step at the returned solution must
move it by less than T(z) (worst ratio <= 1 over the certified
population). NTF = 100.0 was the S-CERT P1 underived load-bearing
constant (GAP-29 of record: NTF/2 FLIPS cert_verdict); this block is
its derivation of record (theory half; measured halves = F2, below).
 NTF-1 (roundoff-floor model) [SCHEMA, hypotheses H1-H4 declared]: at
a true root the computed one-extra-step does NOT go to zero — it
stalls at a floor ||dz_extra|| <= kappa_eff * EPS * sc(z), kappa_eff
:= ||J^{-1}|| * gamma_R * S_R / sc (dimensionless per-cell
amplification combining residual-evaluation noise, H3 envelope —
measured-model route, not pure Higham: the residual mixes units
across rows and includes tabulated-thermo interpolation — and
Jacobian conditioning). kappa_eff is the certificate-side face of the
SAME measured-noise object as the Tier-1 kappa(J)-aware band (C20)
and the C44 FD-noise floor — one object, four riders. Measured
instance (committed carrier s25bis_gap29_sweep.json):
kappa_eff,worst in [51.7, 70.1] (base arm worst extra step
70.110*EPS*sc; ntf50 arm 51.665*EPS*sc — threshold halved, floor
moved only 1.357x: floor-dominated; worst-cell-may-differ caveat
declared).
 NTF-2 (two-sided certificate semantics) [THEOREM* on the repaired
constant; the star discharges at the F2 floor measurement]: in the
contraction regime (Theta <= 1/2, H2) the correction is a two-sided
error estimator (geometric-series upper bound, cf. Deuflhard CSM 35
(2.10)-(2.14); Gragg-Tapia/Yamamoto-1986-eq.(7) lower bound, c_L >=
1/2 valid-conservative); floor-bounded noise can CANCEL part of the
exact correction, so a PASS certifies ||z_hat − z*|| <= 2*(T(z) +
floor_z) = 2*(NTF + kappa_eff(cell))*EPS*sc(z) <=
2*NTF*(1 + 1/eta)*EPS*sc(z) (population-wide under NTF-3's LB), and
a FAIL at a cell with kappa_eff < NTF witnesses genuine
non-convergence. DISAMBIGUATION SENTENCE OF RECORD (lands verbatim;
phaseD_minor_ntf.md §2 [ESC-r1-9]): "Two DISTINCT objects, stated so
no downstream reader conflates them: the THRESHOLD object T(z) =
floor_W = NTF*EPS*sc is what C34/C35 consume (correct for C35's
premature-stop purpose, VERDICT_wave3 §1.2 — unchanged); the
CERTIFIED-ERROR object is the strictly larger 2*(T+floor_z) <=
2*T*(1+1/eta) above — consumers of a certified ERROR bound must take
the latter, never T itself."
 NTF-3 (window inequality + derived form) [window THEOREM*
conditional-on-declared-A_c; derived form NTF = eta*kappa_q: SCHEMA;
incumbent NTF = 100: PRACTICE-validated valid instance]: (LB,
non-vacuity) NTF >= eta * kappa_eff,max over the certified
population, headroom eta > 1 declared — no false-FAIL at a true
root; (UB, soundness) for EACH downstream consumer c:
2*(1+1/eta)*NTF*EPS*sc*A_c <= tol_c, A_c the DECLARED unit-transfer
factor (AG-1 sufficient-not-optimized; consumers that are
NTF-proportional re-price automatically and do not bind); (window
nonemptiness) 2*(eta+1)*kappa_eff,max*EPS*sc*A_c <= tol_c — on the
record case open by ~5 orders even at the worst A_c = 1e7 class
(>= 4 orders conservative; the old ">11 orders" headline = the
A_c = 1 special case, retired as headline). Derived form: NTF =
eta*kappa_q, kappa_q = a declared upper quantile of the measured
per-cell kappa_eff population; eta in [1.25, 2.5] declared,
TWO-SIDED headroom (never blanket-"conservative"). INCUMBENT
ADJUDICATION: NTF = 100 is a VALID INSTANCE of the derived form
(measured headroom 100/70.110 = 1.426, inside the bracket); the
GAP-29 /2 flip is the model's PREDICTION, not an anomaly
(self-contained witness: the ntf50 arm's own 51.665 > 50, 3.3%
margin) — one committed retro-validation instance of NTF-1.
 NTF-4 (termination coupling, C17 seam) [SCHEMA, conditioned on the
EXPLICIT hypothesis H5 (per-trip fluctuation band [floor_z/(1+m),
floor_z], m = 0.25 declared sufficient-not-optimized; measured half
= F2), STRICT regime scoping per ESC-NTF-r2-1 as ordered at LA-2]:
in the deterministic-envelope regime kappa_eff(cell) > (1+m)*NTF,
UNDER H5 (realized step >= floor_z/(1+m) > T(z)),
metric-termination is unreachable at that cell — the trip cap
becomes the de facto terminator (silent per-cell cost inflation) AND
the cell then fails certification (probe scene D of record); in the
near-threshold band NTF < kappa_eff(cell) <= (1+m)*NTF, early
termination and certification-FAIL probabilities are BOTH nonzero
(probe scene B). The LB of NTF-3 therefore protects BOTH contracts
at once; below the floor only C17's trip cap guards. Envelope
conversion: envelope <= realized*(1+m), so the measured worst 70.110
is a LOWER estimate of that cell's envelope kappa (<= 87.64 at
m = 0.25, outward-rounded).
 NTF-5 (seam) [PRACTICE]: this block is the THEORY HALF of the ONE
C18/C20-Tier-1 window; floor_W := NTF*EPS*sc consumed by C34/C35
unchanged (threshold object, NOT the certified-error object).
 F2 DUTIES NAMED AT THIS SITE (measured halves; nothing executed
here): F2-NTF-FLOOR-POPULATION — per-cell kappa_eff measurement
(converged-cell extra-step probes + ECNoise/More-Wild-class noise
floor + float32 precision contrast for the EPS*sc scale law) across
production marches, quantile + eta ratification; RIDES
F2-C20-CERTQUAL-CAMPAIGN Tier-1 (window shared with C18 — no new
window minted; four-rider/one-owner discipline preserved); the duty
pins ONE operational kappa_eff = the REALIZED per-cell extra-step
multiple (upper quantile = kappa_q), H5 converting realized ->
envelope wherever the NTF-4 scoping needs the envelope object.
F2-NTF-TERMCOUPLE-TRIPCOUNT — trip-count instrumentation under the
NTF sweep (falsifier as re-pinned: margin-scoped,
deterministic-envelope cells only, = a measured H5-band violation;
also records the per-trip fluctuation band that ratifies or
supersedes m = 0.25). Gate REFORM stays F2 (out of scope here); on
any NTF change, C34's TR floor, C35's xtol_u and the O3.1 replay
band re-price linearly. Falsifiers NTF-1..NTF-4 as printed in the
carrier §§1-4 (floor tracking the requested tolerance below
50*EPS*sc or a non-EPS*sc scale law; a planted-root PASS farther
than 2*(T + measured-floor); kappa_eff,q95 > 80, or dispersion no
declared eta covers; margin-scoped termination-with-margin at
envelope-regime cells).]

[LAND-C4-LA4 CLG CROSS-LOWERING GRADIENT-FLOOR DERIVATION BLOCK
(engine-discipline block, landed S-FOUNDATIONS-C4 2026-08-21).
Executes VERDICT_escalation_c4 LA-4(ii) (escalation E-4 CLOSED DRY
at round 3). Carrier of record: validation/
sfoundations_raws_2026-08-13/phaseD/phaseD_minor_crosslowering.md as
revised through [ESC-r3-*] + the [ESC-J1-CLG] judge-ordered
pre-step; labels per VERDICT_escalation_c4 §5.4. SITE DECLARATION:
M0 prints no literal "same-lowering standing rule" line — the rule
of record lives in findings row engine:cross-lowering-gradient-floor
("every gradient COMPARISON or FD stencil pins ONE lowering";
VERDICT_wave2 RC31T-2: cross-lowering pairs REJECTED as validation
comparisons), and this block is its adjacent M0 derivation home,
beside the [LAND-C4-LA2] NTF block whose eps_N object the D4-ALT
channel names (one derivation program, no collisions).
 SETTING: the replay objective J is computed through N ~ 250
implicit 4x4 Newton-solved cell relations; the gradient g = dJ/dW by
the exact adjoint (custom_vjp reverse sweep: per-stage transposed
4x4 solve + accumulation). A "lowering" L = (compiled executable,
batch shape B) — the B-SHAPE clause of record, consumed as INPUT.
Hypotheses (AG-1-declared, checkable on recorded marches): H1
IEEE-754 binary64, u = 2^-53; H2 per-stage kernel flop count <=
m-bar; H3 kappa(A_k) <= kappa-bar; H4 adjoint transport gain G <
inf; H5 (RMS refinement ONLY, PRACTICE) independent zero-mean
per-stage injections; H6 lowering equivalence; H7 cross-lowering
converged-state agreement at unit-roundoff grade with the
coefficient maps uniformly Lipschitz AND uniformly bounded on the
march tube (magnitude bounds sup_k ||dR_k/dW||, sup_k ||phi_k||
absorbed in c); H8 b_L structural stability over an FD step
(h-scaled form).
 CLG-D1 (decomposition + same-lowering determinism) [SCHEMA]:
g-hat_L(W) = g(W) + b_L(W) + eta_L(W) with b_L a DETERMINISTIC
function of (executable, batch shape, W) — bitwise lane-permutation
witness of record; the cross-lowering floor of record phi := max
over lowering pairs of ||b_L − b_L'||/g_sc ~ 1e-8.
 CLG-D2 (worst-case chain floor law — THE amplification factor)
[THEOREM* under H1-H4 + H6 + H7 (H7 with the Lipschitz clause AND
the magnitude-bounds clause); u-linear form CONDITIONAL on q = 1
(H7 sufficient, E3-adjudicated); c depends on kernel shape AND the
H7 regularity constants (C_s, the coefficient-map Lipschitz bounds,
and the coefficient magnitude bounds)]: to first order in u, for any
two lowerings, ||g-hat_L − g-hat_L'||/g_sc <= c*u*kappa-bar*G*N —
equivalently the CHAIN AMPLIFICATION FACTOR Phi_chain :=
(cross-lowering floor, rel)/u <= c*kappa-bar*G*N. WITHOUT H7 the
bound gains the additive c'*eps_N-class*kappa-bar*G*N term (the
D4-ALT channel; eps_N NTF-owned). Record consistency:
Phi_chain(measured) ~ 1.3e8; at N = 250 the linear reading needs
c*kappa-bar*G >= 5.2e5 — compatible (the kappa/G ranges are
UNANCHORED order-of-magnitude, PRACTICE class, pending F2).
 CLG-D3 (RMS refinement) [SCHEMA, conditional on the CLG-D2
hypotheses (H1-H4, H6, H7) with H5]: E||g-hat_L − g-hat_L'||/g_sc ~
c*u*kappa_eff*G_rms*sqrt(N), with kappa_eff*G_rms := rms_k(kappa_k
G_k), the quadratic mean of the per-stage product.
 CLG-D4 (value/gradient asymmetry) [SCHEMA]: the forward chain is
SELF-CORRECTING (Newton re-convergence absorbs cross-lowering
perturbations — J agrees at ~1e-15 = O(u)); the adjoint sweep has NO
fixed point and transports every per-stage rounding discrepancy to
the output un-repaired — the ~7-decade value-vs-gradient gap is
STRUCTURAL. CLG-D4-ALT [CONJECTURE, named alternative]: the floor is
the primal Newton-tolerance floor eps_N leaking into the adjoint
coefficients (sqrt(u)-class; NTF-owned — this block does NOT derive
eps_N); discriminated from D2/D3 by E3 below.
 CLG-D5 (FD amplification law into H) [THEOREM* on the
cross-lowering branch; same-lowering cancellation leg SCHEMA
conditional on H8]: for Hessian columns by forward differences of
the gradient with step h — CROSS-lowering pair: dH/H_sc ~ A_FD*phi,
A_FD := 2*g_sc/(h*H_sc); measured A_FD(implied) ~ 1.2e7 = the "~7
orders" of the mandate row (pair-matched 10^6.6-10^7.2, robust).
SAME-lowering pair: UNDER H8 the systematic component b_L is
common-mode and cancels to first order (the corrected in-batch-base
M6 form meets its derived K_RICH x max(scheme asyms) band, the
standing witness that H8 holds at the operating point of record).
The h-value and H_sc identification are OWNED by F2-C44-FDSTEP —
this block states the law, it does NOT adjudicate step choice.
 CLG-D6 (pinning-discipline corollary) [SCHEMA conditional on H8]:
at floor phi any gradient comparison or FD stencil across lowerings
incurs irreducible noise >= phi*g_sc, FD-amplified by A_FD; within
one lowering, under H8, the systematic part cancels to first order —
the standing discipline ("every gradient COMPARISON or FD stencil
pins ONE lowering") is hereby DERIVED, conditional on H8, as the
unique zero-cost mitigation. This corollary ADDS no policy.
 CLG-D7 (identification gap) [SCHEMA]: the current record (one N,
one precision, one design neighborhood) CANNOT identify the
N-exponent p in {1/2, 1}, the split of c*kappa-bar*G into
conditioning vs transport, the u-exponent q (u^1 per D2/D3 vs
sqrt(u)-class per D4-ALT), or the margin dependence of kappa-bar.
 F2 DUTY SPEC OF RECORD — F2-CLG-SCALE (the three-experiment
identification design; owner = F2 entry, alongside the NTF program;
the cross-lowering pairs it measures are the OBJECT OF STUDY — no
collision with the RC31T-2 rejection of such pairs as VALIDATION
instruments): (E1) chain-length N-ladder — prediction P1: log-log
slope p = 1/2 under H5 (D3), p = 1 worst-case (D2);
nearest-hypothesis adjudication with CI, no magic threshold. (E2)
margin-proximity — prediction P2: floor increases monotonically as
certification margin shrinks, tracking the recorded kappa(A_k) of
the worst cells; a flat response falsifies the kappa-bar leg of D2.
(E3) float32 contrast — prediction P3: under q = 1 the floor ratio
phi32/phi64 ~ 2^29 (f32 gradients O(1)-corrupted); under the
sqrt-class D4-ALT ~ 2^14.5 — ~4.4 decades of separation, an
unambiguous discriminator. Cheap adjuncts: H7 = recorded-march
state-diff check; H8 = same-lowering scheme self-asymmetry at the
consumer's h. All three run on recorded marches with the existing
engine — zero package changes (env pinned), zero CFD.
 SEAM DECLARATIONS (land verbatim, carrier §9): "NTF minor (a) owns
the Newton-floor derivation (D4-ALT only NAMES the channel);
F2-C44-FDSTEP owns FD step choice (D5 only states the law). One
derivation program, no collisions." Higham ASNA 2ed = conditional
THEOREM-upgrade path only (CLG-D2 stands at THEOREM* without it).
Falsifiers: D1 — any same-executable same-batch-shape repeat on
identical recorded inputs differing bitwise; D2/D3 — a measured
floor exceeding the law once kappa-bar/G are measured, or
super-linear N growth; D5 — measured dH outside the K_RICH band
around A_FD*phi; D7 — joint non-separation (p-hat CI covering both
1/2 and 1 AND E3 landing between the two predicted decades) => the
law must be re-derived with a finer error model (declared escalation
path).]

[S22 REGISTRATION BLOCK — O4 DISCHARGED FOR THE S20 INSTANCE
(BRANCH (c)), THE K_disc ~ A_0 BRIDGE FALSIFIED ON ITS NAMED TEST,
AND THE F1 GOVERNOR DERIVATIONS] (2026-08-11, [F1/GOVERNOR] of plan
v3, session S22; log validation/PROGRESS_2026-08-11_S22_governor.md;
carriers [X-LOCD], [X-MGOV] committed this session).
 O4 DISCHARGE OF RECORD (the C-1 three-way locus test, verdict form
adopted VERBATIM; class: MEASUREMENT on committed carriers). The S20
walk was regenerated DETERMINISTICALLY ([X-AKNO] attempt-3 path:
same knots 0.3146/0.7026, same certified prefix to J = 2.7775368e+07
/ KKT 5.056e+04, same returned base J = 2.7775702e+07, same
rejection signature {1.170, 2.458 x4, 1.060, 1.455, 1.698}, record
artifact bit-identical) with the O4 instrumentation armed; the five
distinct rejected designs and the returned base were re-recorded in
their persisted class with cert-argmax localization and the
(G)/Lambda-form val field: VERDICT = BRANCH (c) UNANIMOUS (5/5).
The val field is HEALTHY at every rejected design (min val 0.612 -
0.620 vs the healthy reference m_ref = 0.68837 and the fold
threshold m_ref/K_RICH = 0.172; val at the FAILING cells 0.651 -
0.857; argmin-val locus INTERIOR, never on the terminal C+; the
returned base: val_min/m_ref = 0.899, no depression at the
frontier). CONSEQUENCES, each of record:
 (i)   the C-1(a) DEF-signature reading of the S20 standoff is
       FALSIFIED for the instance;
 (ii)  the C-1(b) interior-caustic reading is EQUALLY falsified (no
       low-margin locus exists anywhere in the design region);
 (iii) the mechanism is CLASS CONSTRUCTION, not physics: damped
       Newton stalls at HEALTHY-margin cells. HONEST LOCALIZATION
       DATUM (beyond the S20 candidate list): the stalling cells sit
       in the NEAR-AXIS region of design columns 23-30 (x ~ 3.93 -
       4.25, y ~ 0.05 - 0.14 at y_t = 1) — NOT adjacent to the
       inserted wall knots; the S20 candidates (spline conditioning,
       knot/station mismatch) remain candidates, mechanism
       identification is OWNED BY F2 (engine rebuild), no
       driver/engine surgery in F1 (S20 pre-named boundary);
 (iv)  the RT-1 standoff wording is RESOLVED: O4 has run — the S20
       standoff is a class-construction artifact, consistent with
       NEITHER a DEF-sector optimum NOR an interior fold-binding
       tier-1 optimum for this instance;
 (v)   THE K_disc ~ A_0 BRIDGE CONJECTURE IS FALSIFIED BY ITS NAMED
       FALSIFIER ON THIS INSTANCE (the S20 block's own test: "val
       must approach its boundary where certification degrades,
       else the bridge is dead"): certification degrades at val
       0.61 - 0.86, nowhere near 0. On this instance the discrete
       certifiable set K is NOT an approximation of A_0: bd(K) is a
       NUMERICAL-CLASS boundary, bd(A_0) a physical one, and they
       are DISTINCT objects here. The conjecture as stated is dead;
       any future bridge claim must carry a per-instance monitor
       test (this is now the standing rule);
 (vi)  GOVERNOR RE-SCOPING of record: the margin governor retains
       its role as the EXCLUSION guard against genuinely
       fold-approaching designs (front taxonomy (c); REQ-NONSTALL
       steering with the G1 surrogate) — that duty is untouched —
       but it CANNOT capture the S20-instance certifiability
       frontier, and no claim that margin-constrained
       re-optimization dissolves THIS obstruction survives (the
       T4 campaign measures the corresponding branch).
 F1 GOVERNOR DERIVATIONS OF RECORD ([X-MGOV]; classes declared):
 KS-min aggregate in shifted form with the log-sum-exp bounds
 v_min - ln(N)/rho <= KS <= v_min [THEOREM, standard]; rho DERIVED
 = K_RICH ln(N)/mu_0_min (gap pinned at mu_0_min/K_RICH by
 construction); floor ladder mu_0_k = m_ref/2^k, k = 1..4,
 PRE-REGISTERED from the measured healthy reference (governor scope:
 the design-wall BUCKET lanes — every W-dependent cell; measured
 m_ref = 6.810298e-01, N = 3498, rho = 766.83, gap = 1.0641e-02;
 the [X-LOCD] diagnostic uses the design-wall REGION scope, m_ref =
 6.8837e-01 — both scopes declared, each carrier owns its own); G1
 SURROGATE [PRACTICE, rejector-PROVEN]: m = KS(finite lanes) -
 K_RICH m_ref frac_bad - mu_0, finite negative at every
 representable W (measured at a gross non-monotone wall:
 m = -3.96e+02 finite, gradient finite with the zeroed component
 COUNTED — REQ-NONSTALL survive+report), exact KS at zero failures;
 AD margin gradient verified against two-step-Richardson FD
 (3.29e-06 vs band 5.92e-05) with a firing corrupted-gradient
 control; [D1]-CONSTRAINED CORNER METRIC [COROLLARY of the
 registered constrained-KKT THEOREM]: at a margin-active
 constrained maximum the lip component reads dJ/dy_lip +
 mu dm/dy_lip = lambda_e = corner density, so rel_c = |gJ_lip +
 mu gm_lip - cd| / |cd|, reducing to the unconstrained [D1] at
 mu = 0; validity condition (outcome-I only) unchanged; mu under
 the B-stationarity qualifier until O1. GENO IMPLEMENTATION-MAGIC
 BANDS (Lambda-form bound (b) F1-entry duty, DISCHARGED;
 SOURCE-VERIFIED against GENO Rao_m.f90 boundaryfunction_solve:
 CENTRAL FD with dV_pert = 1.0 absolute on V, alpha = asin(1/M)
 with an M_FLOOR guard; at |den| < 1e-10 GENO RETURNS val = 0 "on
 boundary" where our monitor reports den instead — a semantic
 difference of record for the F1b cross-check): derived band =
 K_RICH |Lam_FD(1.0) - Lam_FD(0.5)| + 100 eps |Lam_AD| per grid
 point, GENO-recipe FD verified inside it on the baseline q-range;
 den-guard in-range statement measured; PM landing window = F1b
 consumption, declared. ADOPT-OR-DECLARE (KS survey, SOTA search
 2026-08-11): standard KS with derived rho ADOPTED; adaptive-rho
 variants (Poon-Martins SMO 2007; interior-point adaptive
 aggregation 2015; SAKS 2018) NOT adopted — their motive (accuracy
 recovery under tuned budget rho with many active constraints) is
 void here where rho is derived to pin the gap below the
 enforcement resolution and gradients are exact AD.]

[S23 REGISTRATION BLOCK — DUTY-6(i) TOLERANCE-BALL MARGIN BACKOFF
DISCHARGED AND F1 CLOSED] (2026-08-11, [F1/CLOSE] of plan v3, session
S23; log validation/PROGRESS_2026-08-11_S23_f1close.md; carrier
[X-TBAK] committed this session; duty = DUTY-6(i) of the S-GAUNTLET
ratified package, owner F1 derived-floor machinery; S23 user pin of
record: T0 decisions bind ONLY insofar as they preserve the
generality and SOTA modus operandi of the codebase).
 THE BACKOFF OF RECORD (gauntlet C028: a KKT-active optimum has zero
 margin by construction — its certificate certifies a MEASURE-ZERO
 design; the as-built ball must be priced). Classes declared:
 (i)   BALL MAPPING [THEOREM-level step]: an in-class as-built
       perturbation p with ||p||_inf <= delta has nodal values
       |dW_i| = |p(x_i)| <= delta (nodal evaluation is
       norm-nonexpansive), so the in-class ball maps INTO the dof box
       {||dW||_inf <= delta} and the box worst case is conservative;
       slope control (the W^{1,inf}/C^1 qualifier of the ratified
       duty) is automatic in-class through the fixed basis, and the
       margin's dof-gradient chain carries the full slope dependence;
       OUT-OF-CLASS waviness (AM texture below class resolution) is a
       DECLARED class-scope boundary (F2/F6 per the ratified split).
 (ii)  MEAN-VALUE BOUND [THEOREM, m C^1 on the box]:
       min_{||dW||_inf <= delta} m(W + dW) >= m(W) - L1_sup * delta,
       L1_sup = sup over the box of ||grad m||_1 (Hoelder l_inf/l_1).
 (iii) MEASURED-SUP SURROGATE [PRACTICE, the repo's two-point
       K_RICH-safeguarded pattern]: L_TB = K_RICH * max(||grad
       m(W)||_1, ||grad m at the first-order worst box vertex
       -delta_max sign(grad m)||_1); BACKOFF RULE Delta(delta) =
       L_TB * delta; SHIP GATE m(W) >= Delta(delta) at the DECLARED
       application tolerance delta. SCOPE: certification-time (ship)
       requirement on the nominal optimum ONLY — the search-time
       margin machinery ([X-MGOV], REQ-NONSTALL, G1 surrogate) is
       untouched.
 (iv)  GENERALITY (binding text): delta is a DECLARED application
       input, never tuned (reference list of the carrier = 0.1 mm on
       throat radii 1 m / 10 cm / 1 cm in y_t = 1 units,
       env-overridable); the deliverable of record is the PER-CLASS
       coefficient L_TB; every tier/geometry-class transition
       RE-DERIVES it (D6 tier-invariant transition duty).
 (v)   MEASURED OF RECORD ([X-TBAK] FULL PASS, exit 0, first run):
       L_TB = 4.321067e+01 per unit ball radius on the bell tier-0
       9-dof baseline-plan class (||grad m||_1 = 1.868067e+00 nominal,
       1.080267e+01 at the delta_max vertex — curvature engaged and
       covered: measured drop/delta 1.88 -> 5.58 over delta 1e-4 ->
       1e-2, all inside Delta); R-TB2 THE RATIFIED DUTY-6 FALSIFIER
       FIRES (synthetic margin-active nominal at floor mu_0* =
       measured KS(base) = 6.803943e-01: the delta = 1e-2 perturbed
       contour fails re-certification at margin -5.576e-02); R-TB3
       discriminates (active nominal rejected at every declared
       delta; healthy rung-1 configuration m = 3.398794e-01 accepted
       at delta <= 1e-3 with perturbed margin >= 0 measured; HONEST
       DATUM: at delta = 1e-2 — 0.1 mm on a 1 cm throat — the rung-1
       design is NOT shippable, Delta = 4.32e-01 > m: the backoff
       BINDS on small hardware; no-backoff control reproduces C028).
 (vi)  ADOPT-OR-DECLARE (SOTA survey of record): worst-case
       linearization over a tolerance ball = the standard
       robust-margin treatment (robust-LP lineage, tolerance
       allocation practice) ADOPTED at ship-gate level; full
       minimax/DRO robust re-optimization NOT adopted with reason —
       the robust/mode-measure layer has a ratified owner (DUTY-13,
       post-F5a re-adjudication) and P3 anti-divergence pins this
       duty to the derived-floor backoff.
 F1 CLOSE OF RECORD (user decision T0, 2026-08-11): F1 closed at
 campaign 1/2, session 2/3 — exit conditions measured at S22 (branch
 certifiability-limited-under-constraint, margin inactive, O4
 localization branch (c), bridge falsified), 2nd campaign measurably
 vacuous by monotonicity. P-2 freeze fired BY RULE dated 2026-08-11
 (content: S19 two-knob numbers, registered norm 9.4809e-03, derived
 band 1.8696e-02, o32 objective row NON-CONCLUSIVE); the C1
 P-2-freeze-blocker row adjudicated FREEZE-WITH-DECLARED-CONDITIONAL
 (the field-level rejector remains a NAMED conditional with owner F2,
 declared in the P-2 outline header — the named-conditional-with-owner
 pattern of record, generality preserved).]

[S24 REGISTRATION BLOCK — F1b DEF ADJUDICATION: THE MARGIN
BUCKET-SCOPE BOUNDARY, THE CONSTRUCTION-SURFACE READING OF val, THE
TWIN LEG-1 NUMBERS, AND THE COMPANION VERDICTS] (2026-08-12,
[F1b/TWIN] of plan v3, session S24; log
validation/PROGRESS_2026-08-12_S24_f1b.md; carrier [X-DEFTW]
committed this session; two mid-session adversarial panels of record:
ADVISORY_S24_DEbucket_panel_2026-08-12 (Form-2, campaign GO
conditioned, C1-C10) and ADVISORY_S24_thermo_closure_survey_2026-08-12
(adopt-or-declare, KEEP [X-THC1]); both judge-adjudicated in one
round, labeled per the standing rule).
 SCIPY res.v CONVENTION OF RECORD (S22 residual CLOSED; scipy 1.18
 source-read): res.v = one multiplier array PER CONSTRAINT in the
 order passed; defining identity lagrangian_grad = grad f +
 sum J_i^T v_i (f = the MINIMIZED objective, J_i = the USER
 constraint Jacobians); active LOWER-bound inequalities give v <= 0
 (user v = MINUS the positive canonical multiplier), equalities pass
 through at + sign. For run_trsqp (f = -J; cons = [lip equality,
 margin]): mu(M0) = -res.v[-1][0] >= 0 and lambda_e = +res.v[0][0],
 scale-invariant in the Jacobi parametrization. The S22 print
 -156.05 maps to mu = +1.5605e+02 (sign-consistent; the NUMBER stays
 information-only). mu wording remains B-STATIONARITY (O1 open).
 THE MARGIN BUCKET-SCOPE BOUNDARY [MEASUREMENT of record, both
 codes, panel-ratified]: at a deep-DEF instance (defnoz: eps = 30,
 L = 8) the (G)/Lambda-form val field is legitimately NEGATIVE on
 certified shock-free fields — val ~ -0.81 at the wall attachment
 (theta ~ 46 deg) and val < 0 on the terminal characteristic
 UPSTREAM of D' (both measured on GENO's own A4-verified defnoz
 field AND on our march of its class representative, same AD
 monitor) — so a constraint "val >= mu_0 > 0 over every W-dependent
 lane" (the S20-S22 whole-field bucket) or over the whole control
 surface has an EMPTY feasible set there for the entire class,
 including the classical DEF design itself. CONSTRUCTION-SURFACE
 READING [panel 4/4]: val is the criterion "can a Rao control
 surface advance through this state" (val = 0 is a POLE of the
 reduced DE-march ODE, dtheta/dR ~ 1/val — E1 sharpening); the
 classical corpus evaluates it ONLY at candidate D points and along
 DE; no field criterion exists. EQ-v2 DIRECTION-A CLAUSE CORRECTED
 AT CONSTANT CONTENT [C2]: the fold "touches the CONSTRUCTION
 SURFACE only at D'" (not "the computed domain"). THE BUCKET OF
 RECORD for margin carriers: the DE-SIDE bucket — registered
 terminal-C+ chain nodes strictly LIPWARD of the last val = 0
 crossing (the direct problem's self-consistent D'-analog; GENO's
 own jb/xstar/pmcompression dispatch mirrored, source-verified);
 at mild instances (no crossing; eps = 4 field all-positive, min
 val 0.68) it DEGENERATES to the whole control surface and is
 feasibility-equivalent to the [X-MGOV] whole-field bucket — the
 S22 record stands AT ITS OWN instance; the bucket definition is
 INSTANCE-CLASS-SENSITIVE and every margin carrier must declare its
 bucket against this boundary. INDEPENDENT CLASSICAL CORROBORATION
 (generality-review dispatch A5, page-verified on BOTH Rao-Beck
 papers): the classical discontinuity sits at D' on the chosen
 right Mach line — the KERNEL-side end of the control surface —
 with the PM compression coalescing AT D', the jump landing ON the
 boundary, and the optimality Eqs. (1)-(3) UNCHANGED from the
 post-jump state (isentropic upstream, induced shock only aft of
 D') — exactly the "DE-side chain lipward of the last val = 0
 crossing" construction. An empty DE bucket = the direct
 image of the classical existence limit [C9]. Branch-map
 declaration [C1]: kill criteria of the pre-registered falsifier
 unchanged; margin OBJECT re-scoped; two F5 limbs re-routed
 (axis-side -> the F2 position-vs-D' comparison; field-interior
 caustics -> march certification + the F4 margin-inactive branch);
 F2's on-characteristic half holds by construction (its content =
 position along the chain). Site labels are quotable only together
 with the F2 |argmin - D'| distance [C8]. F1/F4 are re-scoped to
 the LADDER direction; the joint mesh+knot refinement half is a
 NAMED conditional [C7] (discharge: the pre-authorized optional
 session, else F2 entry).
 TWIN LEG-1 OF RECORD ([X-DEFTW] leg1, two GENO resolutions, fresh
 scratch runs): DEF marker ACTIVE, Dtheta_comp = -9.9837/-9.9839
 deg; A4 identity on the DEF branch rel 4.163e-4/4.108e-4
 (independent reproduction of GENO fca273a); CF = 1.7285/1.7284;
 D' = (5.2015, 3.4073)/(5.1994, 3.4058), two-resolution agreement
 2.613e-3 inside the K_RICH cell band 1.2122e-2; q(D') = 3145 m/s,
 den(D') = 0.684 (the GENO |den| < 1e-10 guard cannot bite at D');
 derived D' bands: landing window (0,1e-6) + dthetapm/2 through
 measured gradients = 1.581e-4 position, grid cell 3.03e-3,
 K_RICH-safeguarded band 1.2122e-2; GENO two-resolution wall
 difference 1.5283e-4; lip constraint residual |ye - yt sqrt(eps)|
 = 4.4938e-3 (GENO's inner-bisection tolerance, measured). GENO
 N-74 blast radius extended of record: resolution-INDUCED
 infeasibility at a feasible (eps, L) (NI = 201 halving sends the
 outer TOC bisection to the Mrao ~ 80 non-physical bracket + inner
 hang) — return finding for the GENO repo.
 S18 FIVE-LINE HYPOTHESIS AUDIT [T-T3-MAP S18-clause NAMED
 PRECONDITION — PERFORMED, S24 T2a]: the S18 "+0.04%" twin
 configuration audited from the S18 record against the
 tier-1+vacuum set: H-OBJ satisfied by construction
 (vacuum-equivalent objective, Pa drops on the {eps, L} feasible
 set); H1-T satisfied (frozen CH4/O2 thermally-perfect table,
 gamma(T) free); H2' satisfied-MEASURED (per-phase supersonic
 march, P4 margin audit 0.4809 >= 0.1202 m/s); H3-p
 satisfied-DEGENERATE (single-phase instance — the family axis
 never exercised: exactly why it is a corner measurement); H4
 instance-corroborated only (N2 restart control; hypothesis
 retained). "Zero-by-theorem inside the corner" phrasings are now
 admissible WITH the H3-p-degenerate and H4-instance qualifiers;
 the +0.04% stays a corner measurement, never general
 RDE/steady-coincidence evidence.
 THERMO-CLOSURE SURVEY OF RECORD [KEEP [X-THC1]; adopt-or-declare]:
 (i) the ATLAS table dCp column is NOT analytic — measured over all
 4999 intervals of the defnoz table it is the 1-K BACKWARD
 DIFFERENCE of Cp (max dev 1.0e-6 vs FD; analytic would sit 30-60x
 away): generator-derivative ingest only behind an ANALYTICITY
 REJECTOR (survey condition C-B); (ii) FORMAL EXACTNESS: in the
 working window
 [1050, 3900] K the NASA fit has quartic cp => quintic h, which the
 quintic-Hermite closure reproduces IDENTICALLY (interpolation and
 FD errors ~ cp^(5) == 0) — in-window the closure is an exact
 re-representation, S11 generality costs zero accuracy; the
 no-joint-in-box hypothesis is DECLARED with a per-table joint
 census duty (survey condition C-C; 200/201 K clamp, 1000 K joint
 at 1.57% cp' kink named); (iii) FLINT (GENO backend-2, source-verified): sole
 interpolant is LINEAR-C0 on the 1-K grid with cp/h/s independent
 and dCp never consumed — the S14 defect class at source level on
 GENO's second backend (cross-code finding; defnoz/leg-1 runs
 backend 0, untouched); FLINT is GPLv3 (user flag, GENO-side);
 (iv) NASA9-direct: not adopted as closure, ADOPTED as an
 exactness ORACLE [C-A, owner F2/next X-THC1 touch]; box-edge
 silent-clamp rejector = C-D (owner F2). Lit-map hygiene of
 record: the "AIAA 2019-0197" citation was a PHANTOM (user-verified
 non-existent, removed) and the Harroun "near-perfect time-averaged
 expansion" misquote is corrected to the faithful "steady MOC
 design at fixed NPR 13.7/19.3 (p.662)" in all three carrying
 lines. ACQUISITIONS LANDED 2026-08-12: Sternin (Doklady AN SSSR
 139(2), 1961, p.335 — the Russian original of the 'Sov. Phys.
 Dokl. 6(7) 1962' translation) + Shmyglevskii (USSR CMMP
 20(5):113-127, 1981) + Moretti (C&F 31:719-723, 2002) — the O3
 gate moves from blocked-on-acquisition to blocked-on-page-verify;
 the generality-review dispatch A1 then upgraded this further: both
 primaries READ IN FULL TWICE by the review refuter, so O3 =
 blocked-on-ADJUDICATION with a TWO-SIDED comparison set (dispatch
 A2), see the corrected S20-block citation status.
 THE TWIN VERDICT OF RECORD (leg 2 = [X-DEFTW] campaign, two
 decisive runs, rung 1 attributable — C3 gate CLEAN on the repeat,
 crossing drift 1 node; external monotonicity stop after the
 tightest rung measured margin INACTIVE; branch adjudication in the
 S24 log steps 13-14): **EQ-v2 stays CONJECTURE with ONE NEW NAMED
 HYPOTHESIS ADDED of record — H-CLASS**: Direction A's joint limit
 (h -> 0, rho -> inf, mu_0 -> 0) is read WITH the hypothesis that
 the design class/mesh can approach the (G) boundary before losing
 certifiability. At the tier-0 9-dof class at the defnoz instance
 this hypothesis MEASURABLY FAILS: the margin never activates (min
 DE val 7.31e-2 = 33x the tightest pre-registered floor at the
 certifiability-limited stop, active-cusp census 0/0), the walk is
 stopped by march CERTIFICATION at healthy val — the THIRD measured
 instance of the class-construction mechanism (S20, S22 mild; S24
 deep-DEF) — so the mu_0 -> 0 limit set of margin-active KKT points
 is EMPTY along the executed ladder and the falsifier's decisive
 content is UNREACHED at this class (named owners: the C7
 refine/enriched-class conditional, S24+1 optional else F2 entry;
 the F2 near-axis + C1-rejector mandate). NO hypothesis-killing
 branch fired (F5/F6 clean; F2 non-adjudicable, subject absent).
 MEASURED IN-CLASS DATA of record: (i) the classical transversality
 content VERIFIED in-class on the leg-1 side (the GENO DEF
 representative passes its own instance-derived f2 bar, 1.4972e-2 <
 2.0137e-2; our non-stationary outcome-II design does not and need
 not — F3 fired-as-written with its KKT-closure precondition unmet,
 declared); (ii) **the in-class F7 surplus datum**: within the
 tier-0 certified class at (eps = 30, L = 8) the DEF-wall class
 representative is measurably NOT the J-argmax — a certified
 margin-inactive design exceeds its J by +2.0407e5 (+0.51%) vs the
 pre-registered band 5.38e3 (38x), with the DECLARED
 band-underinclusion caveat (class-representation error saturates
 M -> 2M and is under-covered by the M-vs-2M J-difference; crude
 systematic bound ~6e4). EVIDENCE GRADE (S-CERT audit 2026-08-13,
 P1 finding, three independent streams convergent): the +0.51%
 datum is RECORDED-CONSISTENT (the arithmetic reproduces from the
 committed scalars of s24_deftw_f3f7.json: J_last - J_def =
 2.0407e5 = 0.507%) but NOT RE-EXECUTABLE - the F7-side design
 vector behind J_last was never persisted (campaign artifact absent
 from disk and git history); regeneration = declared conditional,
 owner F2 (hour-scale ladder re-run, and it would still not restore
 the design OF RECORD). MOC-08 falsifier of the pair executed
 2026-08-13: PASS (delta-J IVL-insensitive, drift 3.5e-1 vs band
 5.4e3). CLAIM CAP of record: this is an IN-CLASS
 statement about the 9-dof representative, NEVER about the true DEF
 construction's optimality in its own boundary-built family (O3
 gated); it is the first in-class measured datum on the Viviano
 side of the A3 three-way tension, compatible with Rao-Beck-Booth's
 boundary-family margin-activity statement (a family this class
 never reaches). O5 (limit order): NOT dischargeable at this class
 (no boundary-active sequence exists to extrapolate) — NAMED
 CONDITIONAL carried, same owner as C7. RT-4 mu SIGN TEST: mu = 0
 identically on the ladder (monotonicity, the pre-registered
 [X-MGOV] wording); the res.v barrier estimate at the stop
 (+4.86e4) is information-only under B-stationarity; the GENO
 deeper-jump family half remains STRUCTURALLY GATED (needs a
 GENO-side jump-depth knob; owner = the GENO repo under its own
 protocol, trigger = its next dedicated session).]

==============================================================================
PART VII — DOCUMENT MAP, PHASES, THESIS

Deliverables of record (depth per topic):
 D1 `rde_nozzle_problem_book.md` — definitions, interface contract +
    sonic-start + mixed-interface decision tree, hypothesis ledger.
 D2 `rde_nozzle_literature_map.md` — 17-gap analysis, six strands +
    in-house classical corpus (b0), all citations verified/flagged.
 D3 `rde_nozzle_theorem_ledger.md` — per-claim rigor classes,
    corrections of record, method upgrades (bounds, Gamma-convergence,
    DWR, shock tracking), global-optimality program, configuration-free
    total optimum.
 D4 `rde_nozzle_claims_verdict.md` — what survived/fell/weakened;
    ranked open problems OP-0..OP-11; repo actions.
 D5 `rde_nozzle_general_scheme_panel.md` — 16-agent panel scheme for
    the general (non-steadifiable) problem + prescribed-profile
    convergent pipeline (Annex A).
 D6 `rde_nozzle_development_plan.md` — certainty model C1-C4, phases
    A0-A7, tool matrix, gates G0-G6, 90 days, input taxonomy (Annex B).
 D8 `rde_nozzle_panel_2026-07-22.md` — S14 convergence panel of record
    [PAN-S14]: 16 team verdicts (§5), workflow-1b addendum + R4-bis
    register + declared residue (§8). [row added 2026-08-05, S15,
    D8 §8 residue]
 D7 `rde_nozzle_pipeline_audit.md` — per-step triple verdict, declared
    residues R1-R10, errors found-and-fixed E1-E7, decision matrix.
Work phases (operational plan): Fase 0 consolidation -> Fase 1
quasi-1D foundations (bound ladder OP-0, phase diagram OP-11-eps, paper
P-1) -> Fase 2 differentiable engine (gate G0, milestone M1, RaoPlug
fix) -> Fase 3 cycle layer + first science (gates G1 ORACLES-FIRST and
G2 value-by-bound-gap; papers P-2 fast-track, P-3) -> Fase 4 O(St)
license (G3) + wave-frame anchor (G4; papers P-4, P-5) -> Fase 5
robust/coupled/tool. Thesis mapping: Ch.1-2 = Parts I-III; Ch.3 =
Fase 1; Ch.4 = Fasi 2-3; Ch.5 = Fase 4A; Ch.6 = Fase 4B; Ch.7 =
horizon (OP list). External standing gates: G5 (Kraiko/PMM pass before
any submission). RESOLVED 2026-07-16: the weak-strong measure-valued
citation is VERIFIED (Brenier-De Lellis-Székelyhidi, CMP 305:351-361
(2011), doi:10.1007/s00220-011-1267-0) — with the Lipschitz caveat now
incorporated in D2.5 (canonicity conditional across shocks).
Target venue of record for P-1/P-3 (methodological + first results):
JPP class (Journal of Propulsion and Power), with the mathematics
papers (P-4/P-5) aimed at applied-mathematics venues.
