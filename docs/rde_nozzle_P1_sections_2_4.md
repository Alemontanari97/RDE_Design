# P-1 DRAFT SECTIONS §2 AND §4 — full text of record
# "Cycle-averaged variational nozzle design for rotating detonation
#  engines: exact steadification, a collapse dichotomy, and certified
#  performance bounds"

Status: DRAFT TEXT OF RECORD (2026-07-16, [F1/P-1], session S8) for
sections §2 and §4 of the skeleton of record
(docs/rde_nozzle_P1_skeleton.md, commit 6263c22). Sources: M0 (theorem
statements and proofs — in conflict, M0 wins), D3 (rigor classes), D2
(citations), D4 (novelty verdicts and contingencies). Acceptance rules
(a)-(e) of the skeleton applied PER SUBSECTION: each subsection closes
with an audit line [Class | Falsifier | Carrier | Gamma status]; the
claim-map cross-check is at the end of this file.

NAMING GUARD (collision declared once): the lemmas INSIDE Theorem T3's
proof are cited here as Lemma T3-A (pressure-scaling similarity),
Lemma T3-B (stagnation-temperature similarity) and Lemma T3-C
(affinity), following M0 Theorem 5. They are DISTINCT from the
companion paper's bridge lemmas, cited here as "P-2 Lemma A" (the
Rao ≡ closed-form-adjoint bridge, now THEOREM grade in the
irrotational homentropic scope via Props. A2/A3,
docs/rde_nozzle_P2_lemmaA.md) and "P-2 Lemma B" (the discrete-adjoint
march lemma, draft of record docs/rde_nozzle_P2_lemmaB.md). No
occurrence of "Lemma A/B" below is left unqualified.

SUBMISSION DISCIPLINE (rule (d)): submission remains gated by M1 + G5;
the novelty wording in §4.5 is CONTINGENT on the pending full-text
reading of Kraiko & Osipov, PMM 34(6) 1970 (gate G5 Item 2b; D4 §3
contingency ARMED). Query-bounded formulas are used throughout.

==============================================================================
## §2 The objective: from wall force to phase integral

### §2.1 Thrust of a periodic engine: definitions and the exact mean identity

The thrust of a rocket engine is a force on structure, and for an
engine whose internal state sweeps a periodic cycle at kilohertz rate
the definition deserves one paragraph of care before any optimization
is posed on it. Let W denote the wetted surfaces of the device
(injector face, annulus walls, nozzle surfaces), n the outward normal,
and Pa the constant ambient pressure. The mechanical thrust is

    F_wall(t) = Int_W (p - Pa) n_x dA,                          (2.1)

the constant-Pa gauge being legitimate because a constant integrates
to zero over any closed surface. Equation (2.1) — not any flux
surrogate — is the definition; everything else must be derived from
it. For any fixed control surface S enclosing the engine with the
control volume V between W and S, the unsteady momentum theorem gives
the exact identity

    F_wall(t) = Int_S [rho u_x (u.n) + (p - Pa) n_x] dA
                + (d/dt) Int_V rho u_x dV.                      (2.2)

Instantaneously the two right-hand terms are individually large: in a
rotating detonation engine the momentum-storage term d/dt Int rho u_x
dV oscillates at the wave-passage frequency and is not small in any
useful sense. The exact statement that survives averaging is:

THEOREM 2.1 (mean equality; M0 Theorem 0, proof reproduced in
Appendix A1). For T-periodic flow with bounded contained momentum,
<F_wall>_T = <F_S>_T for EVERY fixed control surface S. Moreover, for
a SINGLE rotating mode — fields of the form q(x, r, theta - W t) —
F_wall(t) is CONSTANT in time and the storage term vanishes
identically, not merely in the mean.

The proof is one line deep on each claim: the storage term is the
time derivative of a bounded periodic function, so its period integral
is Q(T) - Q(0) = 0 exactly; and the theta-integral of any function of
theta - W t over a full turn is shift-invariant, so on an axisymmetric
wall each annular strip contributes a time-independent amount. Two
distinct "unsteady" objects must never be conflated — this is the
standard confusion in the pressure-gain literature and we state the
distinction verbatim from the reference document: (1) the STORAGE term
in (2.2) is pure bookkeeping — momentum borrowed and returned each
cycle — exactly zero in the mean by periodicity and identically zero
for a single rotating mode; it introduces NO approximation. (2) the
O(St) QUASI-STEADY error of §2.2 is a genuine modeling error that
lives in the per-phase steady factorization of the (exact) mean flux,
NOT in the momentum balance. "Storage averages to zero" does not imply
the quasi-steady step is exact, and "kHz unsteadiness" does not imply
the mean thrust needs unsteady corrections at the balance level.

The mission objective adopted for the rest of the paper is the mean
<F_wall>. This is a DECLARED CHOICE, justified by scale separation
(the vehicle responds to impulse at timescales far above the cycle),
not a theorem; thrust fluctuations leave the objective and re-enter as
constraints (side loads, fatigue) in the robust layer, which this
paper does not exercise.

[Class: THEOREM (exact identity; declared choice flagged as such) |
Falsifier: none needed — hypotheses (bounded periodic momentum)
declared; the single-mode strengthening carries the thrust-trace
flatness diagnostic of §3 as its executable purity monitor | Carrier:
Appendix A1 proof; quasi-1D identity tests, run_all group (ii) |
Gamma status: EOS-GENERAL — (2.1)-(2.2) and Theorem 2.1 use no
equation of state at all (claim C1, rule (e) primary form).]

### §2.2 The only approximation in the chain

The averaged objective is then represented as a phase integral of
steady per-state thrusts,

    <F_wall> = Int_Xi F[Sigma; s(xi)] dmu(xi) + O(St),          (2.3)

where s(xi) is the state family delivered at the design interface
(§2.5), mu the operating measure (§2.4), and F the steady thrust
functional of classical nozzle theory. Equation (2.3) — the
quasi-steady, per-phase factorization — is THE ONLY approximation in
the entire definition chain from (2.1) to the variational problem:
exact as the cycle Strouhal number St -> 0, with the error priced (not
merely bounded in order) by a corrector developed in a later phase of
this program, and with the exact steadification theorem of §3 as the
nonperturbative backstop for the single-mode regime. All approximate
content of the formulation lives in this one link; every other step is
an identity or a declared choice.

[Class: SCHEMA with declared bar (the O(St) statement); the paper
claims the ORDER, not the constant | Falsifier: the O5 unsteady-sim
oracle (unsteady simulation vs J_avg + St·J1, program Fase 4 —
declared as outlook, not used by any result below) | Carrier: run_all
group (ii) as the St -> 0 instance (blowdown-to-steady identity) |
Gamma status: EOS-GENERAL — the factorization statement is independent
of the equation of state (claim C2).]

### §2.3 Objective equivalence: thrust integral vs specific impulse (O1)

Practitioners optimize Isp; the variational machinery below optimizes
J = Int F dmu. The two are the same problem under hypotheses that
deserve explicit display, because their failure channels are physical.

PROPOSITION 2.2 (O1; M0 Proposition 1). Assume (i) the cycle family,
period and throat area A_t are independent of the nozzle contour Sigma
(frozen family, H-F1), and (ii) choked feed, mdot(t) = Pc(t) A_t /
c*(t). Then the Isp numerator equals Int F dt identically and
argmax_Sigma Isp = argmax_Sigma J.

The proof pivots on mdot c* = Pc A_t, which holds for ANY c*(t) law —
in particular for any equation of state and any caloric behavior of
the products; the denominator g0 Int mdot dt is Sigma-independent by
(i)+(ii). The failure channels are declared, not hidden: bilevel
coupling (the contour talking back to the chamber) breaks (i), and
then thrust-max and Isp-max are genuinely DIFFERENT problems; unchoked
tails of deep-blowdown cycles break (ii); axially subsonic interface
patches can make mdot contour-dependent. With a fully axially
supersonic interface (§2.5, Lemma N-SW of §3) the hypotheses hold
exactly without invoking upstream choking.

[Class: THEOREM with explicit hypotheses H-F1 + H2 | Falsifier:
bilevel coupling / unchoked tails (failure channels N-O1±, declared) |
Carrier: the mdot·c* = Pc·A_t pivot is exercised by the in-repo
Stechmann-Heister-Harroun Table-1 validation (18/18) and by run_all
group (ii) | Gamma status: EOS-GENERAL — the pivot holds for any
c*(t); no caloric assumption enters (claim C3).]

### §2.4 The operating measure: blowdown is log-uniform in pressure (O2)

The cycle measure mu is the pushforward of normalized cycle time under
the phase map t -> xi. For the canonical exponential blowdown between
wave passages, Pc(xi) = P_CJ · PR^(-xi) with xi ~ U[0,1), a change of
variables gives

    dmu_P = dPc / (Pc ln PR)   on [P_CJ/PR, P_CJ]:              (2.4)

the RDE's canonical operating measure is LOG-UNIFORM in chamber
pressure. Nothing downstream depends on this closed form: any measured
cycle simply replaces mu, and every theorem of §§3-7 is
measure-agnostic. We display (2.4) because it is the measure used by
the executable results of §§6-7 and because it makes quantitative
sense of a field habit: log-uniform weighting is why the high-pressure
part of the cycle dominates averaged design less than a naive
arithmetic intuition suggests.

[Class: THEOREM (one-line change of variables) | Falsifier: none —
measure-agnosticism is the point; a measured cycle replaces mu without
touching any proof | Carrier: measure generator in
src/thrust/st_core.py (blessed cycles data), run_all group (v) golden
numbers | Gamma status: EOS-FREE — the statement involves no
thermodynamics beyond the declared blowdown law (claim C4).]

### §2.5 The design interface contract

All theorems below consume the cycle through a DESIGN INTERFACE
Gamma_d: a fixed axisymmetric surface downstream of all heat release
carrying the data family s(xi) and the measure mu. The contract has
three audited clauses: R1 causal separation (Gamma_d downstream of the
reaction zone's causal firewall, §3.3); R2 well-posed data (full state
prescribed only on axially supersonic patches — the frame-invariant
spacelikeness criterion u_x > c of §3.3; subsonic patches take
incoming invariants plus a declared closure); R3 measurability of
xi -> s(xi). An idealization ladder I0-I4 (coupled bilevel / wave-frame
steady field / per-phase meridional profiles / sonic family
(P0,T0)(xi) / single mean state) grades how much of the cycle a given
computation consumes; the quasi-1D results of §§6-7 sit at I3 and say
so. Data audits (characteristic completeness, Crocco compatibility,
spacelikeness margin) are PRACTICE: instrumented, not proven.

[Class: definition + PRACTICE audits (declared) | Falsifier: audit
fields reject non-conforming data at ingestion | Carrier: stage-A
audit fields in the data of record | Gamma status: EOS-GENERAL — the
contract constrains data structure, not thermodynamics.]

==============================================================================
## §4 The collapse dichotomy (core of the paper)

### §4.1 Fixed wall: the averaged problem collapses exactly (T3)

The first horn of the dichotomy explains the field's universal habit.

THEOREM 4.1 (T3, the collapse; M0 Theorem 5, proof in Appendix A3).
Assume H1 (one frozen gamma common to all phases), H2' (fixed wall,
full-flowing, supersonic exit at every phase — an ambient-blind
interior), H3 (phase-independent nondimensional inflow shape: phases
differ only through (P0(xi), T0(xi))), H4 (per-phase uniqueness in the
solution class), constant Pa, shared geometric constraints. Then

    J[Sigma] = F[Sigma; <Pc>_mu]   POINTWISE on shape space,     (4.1)

with <Pc>_mu = Int Pc dmu: the cycle-optimal fixed wall is EXACTLY the
classical contour designed at the mean pressure.

The proof runs through three lemmas whose individual scopes matter
more than the theorem's headline, because they locate the boundary of
the collapse. Lemma T3-A (pressure-scaling similarity) states that at
fixed contour and T0 the whole interior solution at stagnation
pressure k·P0 is (u, T, k·p, k·rho): pressure factors out of the
field. It is worth emphasizing — because it is where a referee will
probe — that Lemma T3-A holds for ARBITRARY frozen equation of state
(any gamma(T)) and ACROSS transversal shocks: the Rankine-Hugoniot
fluxes are degree-1 homogeneous in the conservative variables at fixed
(u, T), and the Lax/Majda transversality conditions are k-invariant.
Lemma T3-B (stagnation-temperature similarity) removes T0 from the
thrust coefficient and REQUIRES a calorically perfect gas: for
gamma(T) there is no similarity variable in T, and this — exactly and
only this — is where the collapse's validity boundary sits. Lemma
T3-C (affinity) assembles per-phase thrust as F = a[Sigma]·Pc(xi) -
Pa·b[Sigma], and the mu-average of an affine family is a member of the
family.

The pedagogical content of the three lemmas compresses to one line,
which we offer as the sentence to remember the theorem by: at a fixed
full-flowing wall the interior field (M, theta) is invariant phase by
phase — ALL of the per-phase content of the averaged problem lives in
the boundary pressure margin p_e(xi) versus Pa. That is Lemma T3-C in
one line: the interior is scaled, never reshaped, as the cycle sweeps;
only the exit-pressure mismatch keeps the phase label.

Two remarks of record. First, per-phase OPTIMAL contours do move with
Pc(xi); the theorem says the average of that affine family is again a
member — no more. Second, the averaged endpoint (corner) condition
collapses coherently because in this class the endpoint weight is
phase-independent; outside this class the weighted form (**') of §5 is
mandatory and the naive average is wrong.

[Class: THEOREM | Falsifiers (executable): the O1 oracle — any
ensemble machinery run under H1-H4 MUST return Rao-at-<Pc> with
Delta-Isp = 0; the wrong-averaging rejector (naive averaging of optima
vs optimum of the average) | Carriers: run_all groups (vi) (averaging
discrimination) and (ii) (blowdown -> steady identity) | Gamma status,
rule (e) — split by lemma: Lemma T3-A EOS-GENERAL (holds for gamma(T),
across transversal shocks); Lemma T3-B CALORICALLY-PERFECT-ONLY and is
THE declared boundary of the collapse; the theorem as stated is
therefore the calorically-perfect corollary rung of the general
weighted system (**'), of which it is the degenerate instance — the
general form is primary, per the standing generality discipline
(claim C8).]

### §4.2 Altitude duality: the same mathematics collapses trajectory averages

Pa enters the per-phase thrust affinely too (Lemma T3-C), so the
identical algebra collapses a TRAJECTORY-averaged fixed-bell design to
the classical design at <Pa>: cycle average and altitude average are
one mathematics. The dual-bell literature exists precisely because
flow SEPARATION breaks the affinity (a separated bell is not
full-flowing, violating H2'), which is why altitude adaptation is a
real design problem while cycle adaptation of a full-flowing fixed
bell is not. We state this as a corollary because it prices an entire
literature's worth of intuition at zero marginal proof cost.

[Class: THEOREM (corollary of Lemma T3-C) | Falsifier: separation
breaks affinity — declared boundary, same H2' | Carrier: the affinity
algebra exercised by run_all group (vi) | Gamma status: inherits §4.1
— affinity in Pa is EOS-general (it needs only the wall-pressure
gauge), the closed-form collapse point <Pa> inherits Lemma T3-B's
calorically-perfect boundary (claim C9).]

### §4.3 Sharpness: the two-gamma counterexample and the price of the caloric idealization

The collapse is sharp, and the sharpness is executable. Take two
phases with different frozen gammas: J = (1/2)[a(g1)·Pc1 + a(g2)·Pc2]
- Pa·b is not of the collapsed form (4.1) — the coefficient a depends
on the phase through gamma, and no single equivalent pressure
reproduces it. This closed-form counterexample is why NO reformulation
can rescue the exact collapse for gamma(T): the failure is structural
(Lemma T3-B), not technical.

What survives for reacting products is a first-order closure with a
certified second-order penalty. Define gamma_eff = <Pc gamma>/<Pc>
(under blowdown weighting this sits near gamma_CJ, retro-justifying
the freeze-at-CJ habit of the performance-model literature). The
numbers of record on the CH4/O2 anchor cycle: the cycle-consistent
sonic gamma rises 1.1537 -> 1.2093 against the naive chamber value;
the optimal-area shift is -0.56% (an earlier -1.9% figure in our own
working notes originated from an UNWEIGHTED mean — that class of
estimate is now test-rejected at -2.39%); the Isp design penalty of
optimizing at gamma_eff instead of per-phase is -0.00028%, second
order in the shift as the envelope theorem predicts. Separately, at
the CEILING level (§6), purging the caloric idealization altogether is
now executable: evaluating the geometry-free bound on the real frozen
CJ-products isentrope (Cantera h(s,P) route, sonic cap included)
places the true gamma(T) ceiling 4.4-7.9% BELOW the gamma_s = const
closed-form oracle across the finite-Pa rows of record (derived bars
~0.002%) — the price of "one gamma" is a measured number with a
rejector, not a hypothesis.

[Class: counterexample THEOREM + numbers of record | Falsifiers: the
gamma-probe rejector (the unweighted-mean class IS rejected by test);
the constant-cp known-answer rejector on the real-isentrope route
(closed forms reproduced to 4.7e-7, corrupted route rejected) |
Carriers: run_all groups (ix) (gamma probe,
data/gamma_cycle_probe.json) and (xi) (real-route ladder,
src/thrust/bounds_gamma.py, data/bounds_ladder_real.json) | Gamma
status: this subsection IS the gamma audit of the dichotomy — the
counterexample is exact; gamma_eff is the declared first-order repair;
the EOS-general route is primary and the closed forms appear only as
declared oracles (claim C10; rule (e) enforced in the strengthened
form).]

### §4.4 Free boundary: the peak phase wins (T4)

The second horn replaces averaging by a maximum principle.

THEOREM 4.2 (T4; M0 Theorem 6, proof in Appendix A5; stated within the
ideal-adaptation closure, DECLARED). Under the closure in which wall
pressure clamps to Pa downstream of each phase's full-expansion point
(upstream, Lemma T3-A scaling), the per-phase thrust of a plug of
extension l is nondecreasing in l and exactly constant for l >= l(xi),
with l(xi) increasing in Pc(xi). The per-phase argmax sets are NESTED
half-lines [l(xi), inf), so

    max_Sigma Int F dmu = Int max_Sigma F dmu,                  (4.2)

attained by the PEAK-phase design: the untruncated plug laid out at
NPR = P_CJ/Pa (capped by eps_max where binding).

Where T3 says "average, then design", T4 says "design for the peak and
let adaptation do the averaging": the free boundary re-optimizes
itself phase by phase, so the shared-contour coupling that forces
compromise at a fixed wall simply never binds. The closure under which
this is a theorem is not ours: ideal adaptation is published as a
BOUND for detonation cycles (Kraiko-Egoryan 2020, following
Efremov-Kraiko 2004), and we cite it in that duty — the closure's
sonic-cap correction on subcritical tails is part of this paper's §6
contribution and applies verbatim here. Sharpness: a binding length
cap L < l(xi_peak), a base-pressure model at a truncation plane, or
non-ideal adaptation each break the nesting, max Int < Int max
STRICTLY, and the optimum then satisfies the genuinely averaged
optimality system of §5 with the mu-averaged plug corner condition.
The TRUNCATED plug is thus the first genuinely averaged shape problem
of the program — the outlook problem PB-2, deliberately not solved
here.

[Class: THEOREM* (within the declared ideal-adaptation closure, cited
as the Kraiko-Egoryan bound precedent) | Falsifier: a binding cap
makes (4.2) strict — executable | Carriers: run_all groups (vi)
(knee/plateau) and (x) (phase diagram checks) | Gamma status: the
nesting argument is EOS-GENERAL (monotonicity of expansion in l and
area-Mach monotonicity on the supersonic branch need no caloric
hypothesis; the sonic cap is evaluated EOS-generally on the real
route, group (xi)); only the CLOSED-FORM sizing of l(xi) at the eps
rung uses gamma = const, as a declared oracle instance (claim C11).]

### §4.5 The dichotomy read as an explanation of practice

Sections 4.1-4.4 together derive, rather than assume, the two habits
of RDE nozzle practice. Average-then-design is EXACT for fixed
full-flowing walls in the T3 class: the field's habit is a theorem,
not an approximation — and its hypotheses (one frozen gamma,
full-flowing, shape-invariant inflow profile) are precisely the fine
print practitioners should check before trusting it. Peak design is
the theorem for free boundaries within a closure the Kraiko school
already legitimized as a bound. Between the horns — truncated plugs,
base flows, binding length constraints, per-phase gamma variation —
lies the genuinely averaged territory that the rest of this paper
instruments with certified bounds (§6) and an executable phase
diagram over closures (§7), and that the companion paper's adjoint
machinery (P-2 Lemma A, now theorem-grade in the irrotational
homentropic scope; P-2 Lemma B for the discrete march) is built to
optimize in.

On priority: to our knowledge — query-bounded to the six-strand survey
of record (D2, 2026-07-16) and to a 204/204-issue title sweep of PMM
1957-1990 — no published variational nozzle treatment couples a cycle
MEASURE to a single shared contour with the collapse/peak dichotomy
stated, proved, and bounded. The closest published relative surfaced
by the sweep is Kraiko & Osipov, PMM 34(6) 1970 — nozzle contouring
for VARYING FLIGHT CONDITIONS, a multi-regime cousin of the cycle
average. Its full text is pending acquisition (gate G5, reading-list
item 2b); the priority wording of this paragraph is CONTINGENT on that
reading and will be weakened to a containment statement if the 1970
paper's variational structure overlaps (contingency plan D4 §3,
armed). No stronger novelty claim is made anywhere in this paper.

[Class: expository synthesis + QUERY-BOUNDED novelty statement |
Falsifier: any surfaced prior statement — explicitly including the
pending Kraiko-Osipov 1970 full text and the G5 human pass | Carrier:
D2 query record; validation/G5_pmm_toc_sweep_1957-1990.md (204/204
issues, raw-HTML method of record) | Gamma status: inherits the split
declared in §§4.1-4.4; no new claim.]

==============================================================================
## Claim-map cross-check (rule (b) — zero orphan claims)

| Skeleton claim | Where realized above | Class as written | Notes |
|---|---|---|---|
| C1 (§2.1) | Theorem 2.1 + storage/O(St) distinction | THEOREM | verbatim two-object warning kept |
| C2 (§2.2) | Eq. (2.3) paragraph | SCHEMA (priced) | O5 declared as outlook |
| C3 (§2.3) | Proposition 2.2 | THEOREM | failure channels N-O1± in text |
| C4 (§2.4) | Eq. (2.4) paragraph | THEOREM | measure-agnosticism explicit |
| C8 (§4.1) | Theorem 4.1 + three-lemma scope + one-line Lemma T3-C reading | THEOREM | gamma boundary = Lemma T3-B, named |
| C9 (§4.2) | altitude-duality corollary | THEOREM | dual-bell positioning kept |
| C10 (§4.3) | two-gamma counterexample + gamma_eff + purge delta | THEOREM + numbers of record | adds the S7 ladder-level purge delta (-4.4..-7.9%, group (xi)) to the skeleton's list — carrier exists, no new orphan |
| C11 (§4.4) | Theorem 4.2 + sharpness + PB-2 pointer | THEOREM* | closure cited as K-E bound |
| C26 (§1.4, partial) | §4.5 priority paragraph | QUERY-BOUNDED | CONDITIONAL wording (Kraiko-Osipov 2b) as mandated |

Rule (c) coherence: no sentence above reads a §7 winner as a hardware
verdict (§4.4/§4.5 point to §7 as a diagram over CLOSURES only).
Rule (d): submission gates M1 + G5 restated in the header.
Rule (e): gamma status declared in every audit line; gamma = const
appears only as declared oracle (C11 sizing, C10 closed-form oracles)
or demoted corollary (T3 collapse as the calorically-perfect rung).
