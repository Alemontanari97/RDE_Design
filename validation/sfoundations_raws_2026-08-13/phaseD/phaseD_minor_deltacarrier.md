# PHASE D MINOR (c) — DELTA-CARRIER FIXED-EXIT-AREA RELAXATION LEMMA
Author slot, S-FOUNDATIONS-C4 Blocco 1 (Phase D remainder), 2026-08-20.
Brief: BRIEF_blocco2_phaseD.md MINORS (c). ID prefix: DC-<n>; F2 duties
[DC-F2-<n>]. One refuter round + auto-escalation applies.

## 0. Mandate, inputs of record, seams (all read IN FULL at cited anchors)

- Row `pipeline:delta-carrier-F2-entry` (docs/findings_registry.yaml:292-300):
  fixed-exit-area relaxation lemma to M0 with rigor class; delta semantics
  of record = "distance to the L-unconstrained fixed-eps ceiling"; trigger
  "sequenced with/after [OBJ-DOM]; ships only with the sliver banded or
  repaired". Sequence enforcement = the Blocco-2 judge (brief text).
- Row `bound-ladder:constraint-aware-rungs-missing`
  (docs/findings_registry.yaml:1669-1677): shipped rungs constraint-blind;
  delta = B − J[S*] valid a fortiori but conflates suboptimality with the
  PRICE OF THE CONSTRAINTS; named computable refinements = (1) B1^c
  per-phase classical constrained rung (Rao exact in the
  irrotational-homentropic subclass; Guderley-Armitage/Kraiko variants),
  T3 collapse = attainment of B1^c under pressure similarity; (2) KKT
  weak-duality rung from the engine's own multipliers.
- Row `variational-driver:objective-omits-throat-panel` ([OBJ-DOM],
  docs/findings_registry.yaml:204-213): gradient axis governs (5.8e2x);
  the coded J omits the throat panel — the delta carrier inherits the
  sliver unless fix-A/fix-B lands or the sliver is banded.
- Source authority (not re-litigated): ADVISORY_S25_pipeline_sense_
  CONVERGED_2026-08-12.md §3.2 (R2 ratified with refuter corrections 1-5:
  proof obligation = THIS lemma, not the truncation dF/dA argument; delta
  wording; ceiling qualifications, lip/eps residual 4.4938e-3 at the twin;
  sequencing; hypothesis list) and §6 row "Delta carrier".
- M0 context consumed: D2.6 (P) constraint vector c (rde_nozzle_MASTER.md:250-266);
  bound ladder in (iv) (:349-356); [T-EAP]/OP-0 sonic-cap sharpening block
  (:1255-1330); T7(c) cone form + fixed-eps bookkeeping regime 2
  (rde_nozzle_P1_sections_5_7.md:72-94).
- No VERDICT_wave3/wave2 seam is named for item (c) in the brief; the
  binding seams here are [OBJ-DOM] sequencing and the bound-ladder row.

LOAD-CLASS declaration (AG-1 valve, user-ratified 2026-08-20): DC-1/DC-2
are load-bearing — proven properly below. DC-3/DC-4 rung bookkeeping is
gap-accounting — strong trivially-checkable sufficient hypotheses,
sufficient-not-optimized, declared as such.

## 1. Setting and hypotheses (per phase xi; explicit list)

Class W of per-phase designs (the engine's S1 per-phase class, bell/TOC
exit topology), sharing:

- (H1) SHARED-SAUER DATA CONTRACT: same transonic data (Sauer IVL), same
  throat area A_t, same per-phase mass flow mdot, same per-phase
  stagnation state (h0, s0) with the flow irrotational-homentropic and
  shock-free (S1) downstream of the IVL; hence h = h0 − q^2/2 and the
  state lies on the (h0, s0) isentrope, and C_IVL (the momentum-flux +
  gauge-pressure integral over the IVL) is W-independent.
- (H2) FIXED EXIT AREA: exit disk = flat disk of area A_e = eps·A_t at
  the lip station, bounded by the wall lip; control volume boundary =
  {IVL, wall, axis, exit disk}, no other openings (bell topology;
  annular/plug exit NOT covered — declared scope limit).
- (H2b) mdot / A_e < rho* c* (rho*, c* = sonic state on the (h0, s0)
  isentrope). [For eps > 1 this holds up to the Sauer-vs-1D mdot
  correction; checkable per design.]
- (H3) PER-CELL AXIAL SUPERSONICITY on the exit disk: u_x − c > 0 at
  every point (the in-class license; certified a posteriori per design
  by the S1 margin machinery).
- (H4) Constant ambient Pa > 0; objective = per-phase wall gauge thrust
  J[W] = Int_wall (p − Pa) n_x dA ([T-TH0] definition restricted per
  phase), steady per-phase Euler.
- (H5) EOS: smooth strictly-decreasing isentrope maps q -> (p, rho, c)
  via dh = −q dq, dp = rho dh, drho = (rho/c^2) dh; and
- (H5b) gamma_s := rho c^2 / p >= 1 along the isentrope (true for
  thermally-perfect frozen mixtures; trivially table-checkable).
- (H6) OBJECTIVE-DOMAIN SEAM (binding, [OBJ-DOM]): the delta carrier
  evaluates ceiling and J[S*] on the SAME objective domain — it ships
  only after the [OBJ-DOM] fix lands (fix-A or fix-B) or with the
  throat-panel sliver banded into the carrier (row trigger verbatim).

Define lambda = q_e(eps) as the unique supersonic root of
rho(lambda)·lambda = mdot/A_e on the (h0, s0) isentrope (exists and is
unique under (H2b) since d(rho q)/dq = rho(1 − M^2) < 0 on the
supersonic branch, rho q decreasing from rho* c* to 0); M_e(eps) =
lambda/c(lambda) > 1 is the ideal march's uniform exit Mach. Define
J_ideal(eps) := C_exit^id − C_IVL with C_exit^id = A_e[rho(lambda)
lambda^2 + p(lambda) − Pa] the uniform, axially-aligned exit state.

## 2. DC-1 — FIXED-EXIT-AREA RELAXATION LEMMA [rigor: THEOREM*]

STATEMENT. Under (H1)-(H5b), for every design W in the class:
J[W] <= J_ideal(eps), with equality for the uniform axially-aligned
exit at M_e(eps). Consequently J_ideal(eps) is the L-UNCONSTRAINED
FIXED-EPS CEILING: it binds every class member regardless of length or
any other c-slot.

PROOF.
(i) Momentum-theorem decomposition. Steady per-phase momentum theorem on
the control volume of (H2), with the axis contributing nothing
(symmetry) and constant Pa integrating to zero over the closed surface:
J[W] = C_exit[W] − C_IVL, where
C_exit[W] = Int_{A_e} [rho u_x^2 + (p − Pa)] dA. By (H1), C_IVL is
common to the class, so it suffices to bound C_exit.

(ii) Pointwise Lagrangian bound. For the multiplier lambda of §1 and any
exit field satisfying the mass constraint Int_{A_e} rho u_x dA = mdot
(steady continuity + shared mdot, (H1)):
C_exit[W] − lambda·mdot = Int_{A_e} Phi dA,
Phi := rho u_x^2 + p − Pa − lambda rho u_x,
with the local state on the (h0, s0) isentrope (H1), parametrized by
speed q and axial component u := u_x in (c(q), q] (H3 forces q > c(q),
i.e., only supersonic-branch q are admissible). Write
G(q, u) := rho(q) u^2 − lambda rho(q) u + p(q), so Phi = G − Pa.

CLAIM: sup over admissible states of G = p(lambda), attained at
(q, u) = (lambda, lambda) (aligned, theta = 0, q = lambda).

(ii.a) G is convex in u (rho > 0), so its max over u in the closed
interval [c(q), q] is at an endpoint: u = q (aligned) or u = c(q)
(axially-sonic closure boundary; sup over the open class interval is
bounded by the closed one).

(ii.b) Aligned endpoint. A(q) := G(q, q) = rho(q^2 − lambda q) + p.
Using (H5): dp/dq = −rho q, drho/dq = −rho q/c^2, one computes
A'(q) = rho (q − lambda)(1 − M^2). On the supersonic branch
(1 − M^2) < 0, so A increases for q < lambda, decreases for q > lambda:
global branch max A(lambda) = p(lambda). (Endpoints: A(c*) below by
monotonicity; A -> 0 <= p(lambda) as q -> q_max = sqrt(2 h0).)

(ii.c) Axially-sonic endpoint. B(q) := G(q, c(q)) = rho c^2 −
lambda rho c + p. Two cases, exhaustive:
- Case q + c(q) >= lambda: B(q) − A(q) = rho (c − q)(c + q − lambda)
  <= 0 (c − q < 0, second factor >= 0), so B(q) <= A(q) <= p(lambda).
- Case q + c(q) < lambda: then c − lambda < −q, so
  rho c (c − lambda) < −rho c q, hence
  B(q) < p − rho c q < p − rho c^2 = p(1 − gamma_s) <= 0 < p(lambda),
  using q > c (H3) and gamma_s >= 1 (H5b).
In all cases G <= p(lambda) on the admissible set, proving the CLAIM;
the aligned state at q = lambda attains it.

(iii) Assembly (exact weak duality). C_exit[W] <= lambda·mdot +
A_e (p(lambda) − Pa). The uniform aligned exit at M_e(eps) satisfies
the mass constraint by the definition of lambda and attains equality:
C_exit^id = lambda·mdot + A_e (p(lambda) − Pa). Hence
C_exit[W] <= C_exit^id and J[W] <= J_ideal(eps). QED.

MU-INTEGRATED FORM (immediate): with phase-indexed data (mdot, h0, s0)
= s(xi) and phase-shared eps, J_cycle[W] = Int_Xi J[W; s(xi)] dmu <=
Int_Xi J_ideal(eps; s(xi)) dmu =: J_ideal_cycle(eps), by pointwise
domination; measurability of xi -> J_ideal(eps; s(xi)) from continuity
of the monotone root lambda(xi) in the data (R3 measurability chain).

WHY THEOREM* AND NOT THEOREM (declared conditionals): (a) (H3) is an
a-posteriori per-design certification (S1 margin), so the lemma binds
design-by-design conditional on that certificate; (b) bell-only exit
topology (H2) — the annular/plug variant is not derived here; (c) the
momentum-theorem step assumes the class's piecewise-C1 shock-free
fields (S1). Within (H1)-(H5b) the proof is complete; no gap is known.
This discharges advisory §3.2 correction 1: the truncation dF/dA
argument is NOT used anywhere above; the bound covers non-uniform-exit
TOC designs directly.

FALSIFIER (DC-1): (numerical) any certified class member with
(H1)-(H5b) verified and computed J[W] > J_ideal(eps) + ceiling band
kills the lemma — executable at the twin (TOC run vs ideal march, same
eps, same tables, same Sauer IVL); (analytic) any admissible exit state
(q, u) with G(q, u) > p(lambda) kills step (ii). A rejector that
artificially violates (H3) (subsonic-axial cells) must be ABLE to break
the bound — if it cannot, the hypothesis list is not load-bearing as
claimed and the lemma statement is suspect.

## 3. DC-2 — DELTA SEMANTICS OF RECORD [rigor: THEOREM* (inherits DC-1)]

Let A(c) be the admissible class of (P) (full constraint vector c =
(L, eps_max, L_p, curvature/angle, symmetry), M0 D2.6) and A(eps) the
same class with every c-slot except the exit-area/eps slot (and the
class-defining regularity) removed. Then A(c) ⊆ A(eps) and, by DC-1,
    sup_{A(c)} J <= sup_{A(eps)} J <= J_ideal(eps).
Hence for any certified J[S*]:
    delta := J_ideal(eps) − J[S*]  >=  sup_{A(c)} J − J[S*]  >= 0,
and delta admits the exact (definitional) decomposition
    delta = Pi_c + delta_true,
    Pi_c := J_ideal(eps) − sup_{A(c)} J >= 0   (constraint price),
    delta_true := sup_{A(c)} J − J[S*] >= 0    (true suboptimality),
with the split NOT separately computable today (that is exactly the
bound-ladder row's gap). SEMANTIC RULE (of record, advisory §3.2.2
verbatim): every (value, delta) Verdict row says "distance to the
L-unconstrained fixed-eps ceiling" — NEVER "distance to global at
(eps, L)". Under tight L/eps_max, delta can be dominated by Pi_c and go
uselessly loose while the design is near-optimal (the user catch
2026-08-17): the number stays TRUE, only the loose direction is
declared.

FALSIFIER (DC-2): exhibit S in A(c) with J[S] > J_ideal(eps) (breaks
the inclusion chain, hence DC-1); or a shipped Verdict row wording
"distance to global at (eps, L)" (semantic violation, grep-detectable).

## 4. DC-3 — COMPOSITION WITH THE CONSTRAINT-AWARE RUNG FAMILY
[rigor: THEOREM under valve hypotheses V1-V2; bookkeeping = gap-accounting, AG-1 valve applied, sufficient-not-optimized]

Define the relaxation family, for a constraint subset C of the c-slots
(always containing the eps slot and the class regularity):
    B_fam(C) := Int_Xi  sup_{S' in A_phase(C)} F[S'; s(xi)]  dmu(xi),
the per-phase-relaxed ceiling at constraint set C.

(V1) [trivially-checkable sufficient hypothesis] The per-phase
constraint set A_phase(C) is xi-independent (true: one shape serves all
phases; c is geometric and phase-shared).
(V2) [sufficient, declared] xi -> sup_{A_phase(C)} F[·; s(xi)] is
mu-measurable (satisfied when the per-phase sup is attained by a solve
continuous in the data — Rao/ideal-march solves are; declared
sufficient-not-optimized).

THEOREM (under V1-V2). (a) For any single S feasible for all phases,
F[S; s(xi)] <= sup_{S' in A_phase(C)} F[S'; s(xi)] pointwise; integrating,
J_cycle[S] <= B_fam(C) — NO sup/integral interchange theorem is needed
(each phase is bounded by its own sup). (b) B_fam is monotone
non-increasing in C under inclusion (sup over a smaller set). (c) The
DC-1 ceiling is the C = {eps} member: J_ideal_cycle(eps) = B_fam({eps})
restricted to the uniform-exit relaxation; the B1^c rung of the
bound-ladder row is the C = {eps, L} member (per-phase CLASSICAL
CONSTRAINED solves: Rao exact length/exit-area-constrained optimum in
the irrotational-homentropic subclass; Guderley-Armitage/Kraiko
variants for other combos). Hence B1^c <= J_ideal(eps): adding the
B1^c rung to the ladder min can only TIGHTEN delta, and the tightened
delta^c = min(B, B1^c) − J[S*] carries the semantics "distance to the
C-relaxed ceiling" with Pi_c reduced by exactly the priced slots. The
lemma and the rungs program are one monotone family — CONSISTENT by
construction, as the brief requires.

Derivable now: (a)-(c) above (derived). F2 rungs (NOT derived here,
named duties §8): the B1^c executable rung and its ladder wiring.

FALSIFIER (DC-3): a computed B1^c > J_ideal(eps) at shared (eps, data,
tables) = monotonicity violation => implementation bug or hypothesis
breach (V1/V2), the composition claim dies with it; a phase family
breaking (V2) measurability voids the integral bound and must be
declared at the carrier.

## 5. DC-4 — KKT WEAK-DUALITY RUNG (derivable-now half)
[rigor: THEOREM (the inequality); instantiation = F2 duty; regime clause = SCHEMA]

For (P) as posed (unilateral caps g_i(S) <= c_i) and ANY multiplier
vector mu_i >= 0:
    sup_{A(c)} J <= sup_{S in A(eps)} [ J[S] − Sum_i mu_i (g_i(S) − c_i) ],
(one-line weak duality: on A(c) each penalty term is >= 0). With mu =
the engine's KKT multipliers (constraints priced at marginal values,
registry row text) this is the second named rung. REGIME CLAUSE
(consistency with T7(c) cone form, P1_sections_5_7.md:72-94): the rung
consumes multipliers of the UNILATERAL regime (K with caps: sign +
complementarity per KT2015 (2.10)); the fixed-eps bookkeeping regime 2
(K = {point}) carries FREE-SIGN lambda components which are NOT
admissible weights here — a sign-blind import of regime-2 bookkeeping
values into the rung is an ERROR, and the carrier must gate on
multiplier regime. Computable evaluation of the right-hand sup (needs
the perturbed ceiling map, e.g. eps- and L-perturbation of J_ideal) is
NOT derived here: F2 duty [DC-F2-3].

FALSIFIER (DC-4): a toy constrained instance where the multiplier-
priced bound falls below the true constrained sup => sign/regime error
(e.g. free-sign regime-2 import); the regime clause is falsified if a
correctly-signed unilateral-regime instance still violates the bound.

## 6. DC-5 — CARRIER PRACTICE RULES [rigor: PRACTICE]

(a) ANTI-CONSERVATIVE DIRECTION: delta = J_ideal − J[S*] with an
UNDER-estimated ceiling under-states delta (claims closer-to-optimal
than true). The carrier ships J_ideal with its qualifications (advisory
§3.2.3: two-resolution band + eps-achievement correction — the ideal
march stops at |M − M_e| < 1e-5 and re-targets; lip/eps residual
measured 4.4938e-3 at the twin) and delta is quoted against the UPPER
band edge of J_ideal. (b) HYPOTHESES IN THE CARRIER (advisory §3.2.5):
same eps, same thermo leaf/tables, same Sauer IVL/mdot — printed in
the Verdict row. (c) SEQUENCING (binding): (H6) — no (value, delta)
row ships before the [OBJ-DOM] resolution or sliver banding; the judge
enforces.
FALSIFIER: a shipped delta row quoting the lower/central band edge, or
missing the hypothesis line, is a carrier violation (grep-detectable).

## 7. DC-6 — T3-COLLAPSE CONSISTENCY [rigor: SCHEMA (consumes registry/M0, no re-derivation)]

Bound-ladder row text: T3's collapse is precisely attainment of B1^c
under pressure similarity. In that class the per-phase constrained
optimum is phase-shared, so B_fam({eps, L}) is attained by one design:
Pi_{L} -> 0 and delta^c -> delta_true. The DC-2 decomposition
degenerates exactly as the record demands (delta = 0 proven where M1-M3
structure exists, M0 D2.6(iv)) — no contradiction between the lemma,
the rung program, and the T3/T4 attainment results. FALSIFIER: a
pressure-similar cycle with computed B1^c strictly above the T3-collapse
optimum (beyond bands) breaks either this schema or the T3 chain.

## 8. F2 DUTIES (measured halves — NAMED, not executed here)

- [DC-F2-1] (value, delta) Verdict field at the engine rung (execution;
  owner = row pipeline:delta-carrier-F2-entry; ships under (H6) + DC-5).
- [DC-F2-2] B1^c rung executable: per-phase Rao/Kraiko constrained
  solves wired into the ladder min (owner = row
  bound-ladder:constraint-aware-rungs-missing, F2 ladder window).
- [DC-F2-3] KKT weak-duality rung computable instantiation
  (unilateral-regime multipliers only, per DC-4 regime clause).
- [DC-F2-4] Ceiling band measurement at production resolution
  (two-resolution + eps-achievement residual; upper-edge rule DC-5a).
- [DC-F2-5] Rejector for DC-1 (twin-based J_TOC <= J_ideal check + the
  H3-violation breakout test named in the DC-1 falsifier).

## 9. PROPOSED LANDING (for the judge's landing list; orchestrator executes)

- M0 site: Part III, new row [T-DCRX] adjacent to the [T-EAP]/OP-0
  ceiling block (after the sonic-cap sharpening, MASTER.md ~:1255-1330),
  containing DC-1 (THEOREM*) + DC-2 semantics + a pointer to the rung
  family (DC-3/DC-4) and the DC-5 practice rules; DC-6 as a one-line
  consistency remark at the T3/T4 attainment site.
- Registry: row pipeline:delta-carrier-F2-entry — owner field updated:
  lemma DERIVED (Phase D minor (c), [T-DCRX]); remaining owner = F2
  execution [DC-F2-1..5]. Row bound-ladder:constraint-aware-rungs-missing
  — note added: composition derived ([T-DCRX] DC-3/DC-4); rungs remain
  F2. Exact row texts to be fixed by the judge per standing format.

## 10. READ DEPTH + PAPERS

Repo documents read (not papers): BRIEF_blocco2_phaseD.md [FULL];
findings_registry.yaml rows 204-222, 285-309, 1660-1677 [FULL at cited
lines]; ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md §3.2-§3.4,
§6 [FULL at sections]; rde_nozzle_MASTER.md :248-270, :320-399,
:1255-1330 [targeted slices]; rde_nozzle_P1_sections_5_7.md :70-99
[targeted slice]. Papers consulted: NONE (the proof is self-contained
from the ratified proof obligation; no paper claim is load-bearing
here). Efremov-Kraiko 2004 is cited only through the existing M0
[T-EAP] block (its provenance, not re-read).

PAPERS NEEDED: none blocking. Optional (non-blocking, provenance only):
a Kraiko ideal-nozzle-comparison source to attach classical lineage to
DC-1 in the paper (P-1) bibliography; not required for the lemma's
rigor class.
