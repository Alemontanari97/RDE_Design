# BRICK 2 KICKOFF — binding duties of D6 item 9 (variational TOC)

Status: KICKOFF DOCUMENT OF RECORD (2026-08-06, S17, [F2/A1]).
Scope: the four kickoff duties D6 item 9 binds BEFORE any brick-2
optimization runs, plus the S16 addition (EOS G > 0 audit, ledger
channel c4). Each duty section states its NORMATIVE content and its
EXECUTED status (carrier + verdict, dated when it lands in the S17
log). Anchor: (P) of M0 D2.6 — everything here is machinery for the
pair (S*, delta); no hardware claims. Conflict rule: M0 + D1-D7 win;
this document binds the brick-2 implementation layer only.

Related record: D6 item 9 (the duty bundle + waiver/re-adjudication
annotations); [S-D25U-U34] discovery D2 (within-stratum scope, clause
c2); [S-LBML] clause LB-c2 (fixed march topology); [PAP-D9HL] §4.2
(c4 = genuine nonlinearity channel); DIR-THERMOTAB (M0 VI pin);
DIR-G0 + docs/rde_nozzle_G0_decision.md §4 (armed loop-speed
falsifier, unquantified until duty (a)); [X-A1IM] (the certified
march the brick differentiates).

------------------------------------------------------------------------------
## §1 Duty (c) — RK-G POLICY OF RECORD [DIR-RKG]
##    (fixed topology in trust region + re-record on acceptance +
##     kink detection)

The march engine records a SCHEDULE (branch decisions + cell
solutions: the wall-search indices, overshoot/interp retries, exit
tests, streamline-crossing rows — [X-A1IM] `Sched`). The frozen
schedule IS the march topology: the DAG of unit-process cells the
reverse-AD sweep transposes (Lemma B). Two record statements bound
what the gradient means: [S-D25U-U34] D2 — the stability estimate is
WITHIN-STRATUM (same front/cell topology; cross-topology comparison
is census/RK-G territory, not an estimate); [S-LBML] LB-c2 — the
mesh-limit statement holds at FIXED march topology, and re-record
events are the statement's boundaries. The policy below is the
operational consequence; it is BINDING for every brick-2 optimizer.

P1 (FIXED TOPOLOGY IN TRUST REGION). Within one TR-SQP iteration,
   the model gradient/Jacobian and every trial-point evaluation use
   the schedule RECORDED at the current accepted iterate (replay
   mode). All derivative information is therefore exact for the
   frozen DAG (T-LEMB transpose) and stratum-valid (D2/LB-c2). The
   trust radius is the excursion bound that keeps the quadratic
   model honest inside the stratum.

P2 (RE-RECORD ON ACCEPTANCE). On step acceptance the engine re-runs
   the ADAPTIVE march (record mode) at the accepted iterate; the new
   schedule replaces the old one. A decision-vector change vs the
   previous schedule = a RE-RECORD EVENT (topology moved): logged
   with iteration number and the first differing decision; the TR
   model is rebuilt from scratch (no curvature carry-over across a
   stratum boundary). Re-record events are exactly the LB-c2
   statement boundaries — convergence claims for the optimizer are
   per-stratum; a run's Verdict MUST report its re-record count.

P3 (KINK DETECTION — the monitors that catch an invalid or
   seam-adjacent frozen replay). All four are rejector-grade:
   (i)   replay-fidelity: |replay - record| at the accepted iterate
         beyond the Newton floor (X-A1IM S6 metric) => the frozen
         schedule does not reproduce its own record — hard stop.
   (ii)  per-cell Newton certification on trial points: a trial
         replay whose worst cell exceeds the unit-consistent
         certification bound is REJECTED as an evaluation (the step
         is treated as a failed trial, TR shrinks) — a cell that
         cannot re-certify under the frozen seeds is the numerical
         signature of a decision that wants to flip.
   (iii) decision-flip probe: at an ACCEPTED step, P2's re-record
         reveals flips a posteriori; when the TR loop stalls
         (repeated rejections at shrinking radius), the engine runs
         one concrete record march at the rejected trial point and
         compares decision vectors — a flip localizes the stratum
         seam; the optimizer then either accepts-with-re-record
         (crossing the seam deliberately, new stratum) or bisects
         the radius below the flip. No silent crossing.
   (iv)  model/actual kink: |actual - predicted| reduction ratio
         outside the standard TR acceptance window at SMALL radius
         (where the within-stratum model must be good by U1-grade
         smoothness) signals a nonsmooth seam the decisions did not
         flag; treated as (iii).
   THERMOTAB note: under duty (d) the tabulated closure is C^1, so
   TABLE-KNOT crossings are NOT topology events and MUST NOT fire
   the monitors (the D6 "node crossings under the RK-G one-sided
   policy" clause is DISCHARGED INTO C^1 REGULARITY by duty (d) —
   with a C^1 interpolant there is no one-sided bookkeeping left at
   knots; kinks reachable by the state are only the declared
   decision seams). This is why duty (d) precedes any optimization.

P4 (CERTIFICATION GATE ON ACCEPTANCE). A step may be accepted ONLY
   if the record march at the new iterate certifies (all cells
   within the unit-consistent Newton bound) AND monitor (i) passes
   for its own replay. An optimizer output whose final iterate is
   uncertified is NOT a result (G1 discipline at the brick level).

Falsifier (DIR-RKG): a brick-2 optimizer run that (a) mixes
gradients across a re-record event, (b) reports a Verdict without
the re-record count, or (c) accepts a step failing P4, is
NONCONFORMING; the monitors (i)/(ii) are machine rejectors inside
the brick carrier, (iii)/(iv) are logged events auditable from the
run record. Status: policy of record from S17; carrier = the brick-2
TR-SQP carrier when it lands (lint truthfulness: the registry
carrier field stays empty until then).

------------------------------------------------------------------------------
## §2 Duty (d) — THERMOTAB C^1 [X-THC1] + EOS G > 0 AUDIT (c4)

DEFECT OF RECORD (S14 two-lens, D6 item 9 text): the live closure
interpolates cp INDEPENDENTLY of h with piecewise-linear jnp.interp
=> cp != dh/dT between knots and the state Jacobian jumps at knots —
against the C^1 coefficients C-D25U's machinery assumes, and a
gratuitous source of RK-G false kinks.

NORMATIVE FIX (this duty). KICKOFF DISCOVERY (S17, declared): the
naive reading — cubic Hermite on h with node derivatives cp_i —
delivers cp = dh/dT structurally but leaves cp = h' only C^0
(piecewise quadratic with slope jumps at knots): the MoC
COEFFICIENT fields (c, gamma, mu enter through cp) would still be
merely continuous, against the C^1-coefficients requirement the
duty exists to serve (D6: "C-D25U wants C^1 coefficients"). The
interpolant class of record is therefore QUINTIC HERMITE (still the
Hermite class D6 names, one smoothness order up):
    h:  node data (h_i, cp_i, cp'_i)         => h in C^2
    s0: node data (s0_i, cp_i/T_i, (cp'T - cp)_i/T_i^2) => s0 in C^2
with cp'_i estimated from the dense cp table by 4th-order central
differences (2nd-order one-sided at the two edges; estimator error
O(dT^4), far below the physical-constants budget). The interpolated
cp(T) := d/dT [h-interpolant](T) — the EXACT derivative polynomial,
so cp = dh/dT is STRUCTURAL (roundoff-exact, machine-verified
against AD) and cp is C^1: coefficient fields c, gamma, M are C^1
in the state, table knots are invisible to RK-G (§1 note).
s0' = cp/T: exact at nodes by construction, inter-node within a
DERIVED Hermite-remainder floor (table-spacing power bound, no
magic). Monotonicity: h' = cp interpolant VERIFIED positive on a
dense probe with derived margin (monotone-verified class: the
carrier proves it for the data rather than clamping — clamping
would break the invariant); the inverse T(h) then exists and is
computed by Newton on the quintic (seeded by linear interp,
fixed-trip loop), roundtrip-certified at the derived floor.
REJECTORS: (R1) corrupted cp row breaks the structural invariant /
dual-route budget; (R2) non-monotone doctored h detected; (R3)
BZT-doctored table breaks the G-floor (below); (R4) corrupted
inverse breaks the roundtrip certification.
Accuracy: the C^1 closure must agree with the certified linear
closure of [X-A1IM] within the DERIVED interpolation-class band
(spacing^2 curvature bound) — the twin-contour regression stays
inside its existing Richardson band (no re-certification of X-A1IM;
the brick engine uses X-THC1, the record carrier stays untouched).

EOS G > 0 AUDIT (S16 addition, ledger §4.2 channel c4): the entropy
floor of U4's counting lemma and the a-contraction convexity budget
assume GENUINE NONLINEARITY (fundamental derivative G > 0). For the
tabulated ideal-gas frozen mixture (derived in-carrier from
G = 1 + (rho/c)(dc/drho)_s with the ideal-gas isentrope
(dT/drho)_s = (gamma-1) T/rho):
    G(T) = (gamma+1)/2 + (gamma-1) T gamma'(T) / (2 gamma),
which reduces to the classical (gamma+1)/2 at gamma' = 0 (the
carrier verifies that reduction as a known-answer); the audit
evaluates G on the DECLARED state box (the table's full T range,
which contains every march-realized state) via AD of the C^1
closure (gamma' needs cp' — defined BECAUSE the closure is C^1:
the audit is only possible in this interpolant class) and CERTIFIES
G >= floor > 0 with the floor derived from the audit grid spacing
and the closure's Lipschitz bound on the box. REJECTOR: a doctored
BZT-like table (locally concave isentrope) is DETECTED. Scope
honesty: grid-certified audit on the box (dense grid + derived
Lipschitz safety), not an interval certificate; the interval upgrade
rides the [PAP-GMAX] substrate if c4 is ever load-bearing at class
level.

Status: EXECUTED S17 (carrier validation/thermotab_c1_jax.py
[X-THC1], VERDICT PASS 14/14 incl. 4 negative controls; numbers of
record in the registry scope field and the S17 log, step 5).

------------------------------------------------------------------------------
## §3 Duty (b) — SCAN COLUMN ARCHITECTURE (the brick engine)

D6 item 9: "the restructure IS brick-2's architecture, not a
retrofit". The [X-A1IM] record path drives every cell through a
Python-level dispatch (one custom_vjp call-site per cell): correct,
certified, and fine for record/certification — but the OPTIMIZER
inner loop (replay + gradient, called O(10^2-10^3) times) must not
pay Python dispatch per cell, and the graph must not grow with cell
count.

ARCHITECTURE OF RECORD (brick engine, module a1_march_scan):
 (i)   RECORD mode stays the adaptive Python march (topology
       decisions are concrete by construction — this is where RK-G
       P2 lives). Record emits the schedule as ARRAYS: per-column
       cell counts, per-column decision tuples, stacked cell seeds.
 (ii)  REPLAY mode = the differentiable engine: each COLUMN's
       interior sweep is one jax.lax.scan over its cells (the chain
       G[(j,i)] <- G[(j-1,i)], G[(j,i-1)] is sequential by MoC data
       dependence — scan, not vmap, is the correct primitive along
       a column; vmap remains available across INDEPENDENT solves,
       e.g. batched trial points at fixed schedule). The scan body
       contains the SAME implicit-solve custom_vjp cell (Newton
       inside, implicit rule for the transpose) — the Lemma B
       correspondence is untouched, cells are just driven by scan
       instead of Python.
 (iii) Columns of equal cell count share ONE compiled scan (bucketed
       by length; the fan/straightening regions are
       constant-length-per-phase by construction, the arc region
       buckets by its recorded Nv/j2 progression), so compile time
       is bounded by the number of DISTINCT column shapes, runtime
       by the cell count with no Python in the loop.
 (iv)  EQUIVALENCE REGRESSION (rejector-grade): on the reduced twin
       case the scan replay must reproduce the [X-A1IM] Python
       replay to the Newton floor (same schedule, same cells — the
       restructure may not move a single number beyond roundoff),
       and O3.1 must hold on the scan path with the same derived
       tolerance. A scan engine that only "roughly" matches is
       REJECTED — it would silently change the certified machinery.
Status: EXECUTED S17 (module validation/a1_march_scan.py, carrier
id X-SCANM; verdict in the S17 log, step 6).

------------------------------------------------------------------------------
## §4 Duty (a) — DERIVED LOOP-SPEED THRESHOLD (G0 falsifier
##    quantified; clean-host protocol)

DEBT OF RECORD: DIR-G0's loop-speed falsifier is ARMED but
UNQUANTIFIED ("impractical" undefined — S15 T2 fix d1); the S9
lesson binds the measurement discipline (clean host: no concurrent
suites, standalone timings, tasklist check; wall-clock under
contention is NOT record-grade).

DERIVATION OF RECORD (no magic constants — every factor is either a
cited theorem constant or a measured quantity):
 (1) The cheap-gradient bound: reverse-mode AD evaluates the
     gradient at <= omega_rev x the primal cost with omega_rev in
     [3, 4] (Baur-Strassen / Griewank-Walther bound, cited in P-2
     Lemma B context). MEASURED grad/solve above 4 therefore
     indicts the IMPLEMENTATION, not the method — first threshold:
         T1: grad/solve <= 4          (theory constant, not tuned).
 (2) The practicality anchor is GENO ITSELF (the cross-code
     reference is the only non-arbitrary cost scale in the room):
     one TR-SQP optimization must not cost more than the
     COST-EQUIVALENT of the classical outer loop it replaces. The
     GENO type-2 outer loop evaluates O(N_outer) forward marches
     (Mrao/eps bisection at production resolution); our loop pays
     N_TR x (solve + grad) <= N_TR x (1 + omega_rev) x solve_JAX.
     The falsifier fires when the WHOLE brick-2 optimization at the
     declared case exceeds
         T2: N_TR x (solve_JAX + grad_JAX)
             > K_prac x N_outer x solve_GENO
     with N_TR = the measured TR-SQP iteration count of the brick
     run itself, N_outer = the measured GENO type-2 iteration count
     on the twin case, solve_GENO = the measured clean-host GENO
     forward time, and K_prac = 4 (the SAME two-level safety
     constant the repo already uses for Richardson bands — reused,
     not invented; rationale: a differentiable loop that costs more
     than 4x the classical loop it replaces has lost its practical
     case even if asymptotically superior).
 (3) FLIP CLAUSE (D6): if T1 or T2 fails on the clean host after
     the duty-(b) architecture (i.e. the failure is structural, not
     dispatch overhead), the declared alternative is the
     Julia/Enzyme route — a G0 re-decision session, not a silent
     acceptance.
Both thresholds are ARMED as machine checks in the loop-speed
carrier; the measured numbers and the verdict live with the carrier
(R5: no numbers in prose without the committed script).
Status: EXECUTED S17 (carrier validation/a1_loopspeed_bench.py, id
X-LSG0; measured numbers + verdict in the S17 log, step 7; DIR-G0
falsifier field updated; G0_decision.md §4 mirror note).

------------------------------------------------------------------------------
## §5 Registry deltas (S17 kickoff)

 [DIR-RKG]  directive, PRACTICE — the §1 policy P1-P4; falsifier as
            §1; carrier: brick-2 TR-SQP carrier when it lands.
 [X-THC1]   carrier — §2 (thermotab C^1 + invariants + G>0 audit);
            MINTED S17 with the artifact, PASS.
 X-SCANM    carrier — §3 (scan engine equivalence + O3.1).
 X-LSG0     carrier — §4 (loop-speed thresholds T1/T2).
Each entry lands in claims_registry.yaml IN THE SAME COMMIT as the
artifact it indexes (lint truthfulness).
