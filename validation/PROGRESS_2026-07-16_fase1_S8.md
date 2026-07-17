# SESSION LOG S8 — 2026-07-16 — Fase 1 closure (P-1 §2/§4) + F2-prep (G0 spike ext) + OP-0-gamma tail
# Total-order, append-only. One numbered row per step. (CLAUDE.md R3 + standing directive.)

Session: S8 (operational). Program: cycle-averaged variational nozzle.
Branch: rde-nozzle-program. HEAD at open: 315da28 (matches handoff).
Tasks (priority order): T1 [F1/P-1 §2+§4], T2 [F2-prep/G0 spike ext],
T3 [F1/OP-0-gamma tail], T4 [F1/P-2 polish, optional], T5 [LEADS, optional].

--- LOG (total order) ---

1. APERTURA R2 — memory read (research-cycle-averaged-rao,
   gamma-variable-generality, gate-pre-esecuzione, periodic-wave-data-scope,
   python-env-cantera); M0 read IN FULL (Prop. 7 with SHARPENING +
   GAMMA-PURGE INSTANCE, VI.4bis pins, D2.6, T7/(**')); PROGRESS read
   (ORA S7 / NEXT S8 / BLOCCATO); P-1 skeleton 6263c22 read in full
   (claim map C1-C26 + acceptance rules (a)-(e)). Git verified: branch
   rde-nozzle-program, HEAD 315da28 = expected, no foreign staged files
   (untracked only: GENO/, scratch_out.txt, scratch_err.txt,
   validation/ADR_panel_2026-07-16.md — all expected, none touched).
   RESTART DECLARATION: resuming from S7 close; plan phase = Fase 1
   closure (P-1 writing + OP-0-gamma tail) + F2-prep (G0 spike);
   session = S8, ONE session active (concurrency check at every commit
   per handoff mandate).

2. GATE PRE-ESECUZIONE (A/B/C) — VERDICT: PASS, no deltas found.
   (A) PLAN ADHERENCE: T1 = D6 Fase 1 / P-1 writing = PROGRESS NEXT 1;
   T2 = D6 Fase 2-prep / G0 = PROGRESS NEXT 2; T3 = D6 Fase 1 /
   OP-0-gamma residual = PROGRESS NEXT 3 (declared residual in M0
   Prop. 7 GAMMA-PURGE paragraph); T4 = PROGRESS NEXT 4; T5 = PROGRESS
   NEXT 5. No orphan task.
   (B) UPSTREAM RIGOR AUDIT (re-read this session): (i) ceiling CAPPED
   at the sonic state in subcritical — of record in M0 Prop. 7
   SHARPENING, now ALSO on the real route (bounds_gamma, cap by
   inverting w(P*) = h0) — any T3 diagram work must embed the cap on
   BOTH routes; (ii) (**') weighted transversality, naive average
   forbidden outside T3 class (M0 T7(c), D3 lines 162-169 verified
   verbatim today); (iii) D3 §10quater(5): phase-diagram winners rank
   CLOSURES, never hardware — P-1 §7 semantics-first discipline applies
   to any §4 cross-reference too; (iv) D2.6 problem of record (P) =
   pair (S*, delta) — §4 text must not promise more; (v) GAMMA QUESTION
   (strengthened directive): primary route of every NEW number in T3 =
   EOS-general (Cantera h(s,P)); gamma=const appears ONLY as declared
   oracle (known-answer) or demoted corollary; P-1 §2/§4 text must
   carry rule (e) per claim. All five anchors match the documents of
   record; no discrepancy discovered, nothing to back-propagate before
   execution.
   (C) VERDICT: gate pre-esecuzione PASS — execution of T1 may start.

3. T1 [F1/P-1] EXECUTED — full text of record for sections §2 and §4
   written: docs/rde_nozzle_P1_sections_2_4.md. Content: §2.1 Theorem
   2.1 (mean equality + single-mode constancy) with the verbatim
   storage-vs-O(St) two-object warning; §2.2 Eq. (2.3) as THE only
   approximation (SCHEMA, O5 falsifier declared as outlook); §2.3
   Prop. 2.2 (O1) with N-O1± failure channels; §2.4 O2 log-uniform +
   measure agnosticism; §2.5 interface contract I0-I4/R1-R3. §4.1
   Theorem 4.1 (T3) with per-lemma scope split (T3-A EOS-general
   across shocks / T3-B calorically-perfect = THE boundary / T3-C
   affinity) + THE AGREED PEDAGOGICAL LINE (fixed full-flowing wall:
   interior (M, theta) phase-invariant; ALL per-phase content in the
   boundary margin p_e(xi) vs Pa = Lemma T3-C in one line); §4.2
   altitude duality; §4.3 sharpness (two-gamma counterexample, numbers
   of record -0.56%/-0.00028%/-2.39% rejected, PLUS the S7 purge delta
   -4.4..-7.9% now citable with carrier group (xi)); §4.4 Theorem 4.2
   (T4) THEOREM* with K-E closure duty + PB-2 pointer; §4.5 dichotomy
   as explanation of practice + QUERY-BOUNDED priority paragraph with
   Kraiko-Osipov 34(6) 1970 CONTINGENCY EXPLICIT (wording conditional,
   D4 §3 armed). Naming guard Lemma T3-A/B/C vs P-2 Lemma A/B declared
   in header (collision preempted). Rules (a)-(e): audit line [Class |
   Falsifier | Carrier | Gamma status] closes EVERY subsection;
   claim-map cross-check table (C1-C4, C8-C11, C26 partial) at end;
   rule (e) enforced in the strengthened form (gamma=const only as
   declared oracle or demoted corollary).

4. T1 coherence pass (rule (c)) — grep on the new file: "hardware"
   appears ONLY in the discipline note (line 426); zero unweighted
   (**) occurrences; all four "naive" occurrences are correct usages
   (rejected forms). Skeleton header updated with DRAFT TEXT STATUS
   pointer to the new file. VERDICT: T1 coherence PASS.

5. ⚠️ CONCURRENCY DETECTED (FIFTH interleaving) + RECONCILIATION —
   the mandatory pre-commit check for T1 surfaced three untracked
   files NOT present at session open and NOT mine:
   docs/rde_nozzle_G12_S1.md, validation/PROGRESS_2026-07-16_rigore_G12.md,
   validation/g12_shock_linearization.py — a "rigore G12" session is
   ACTIVE IN PARALLEL on this tree (shock-linearization / mesh-limit
   work, G12 frontier). No foreign COMMITS and no foreign STAGED
   files; the T1 commit a4e4964 was already PATH-LIMITED to the three
   S8 files, so the index was not contaminated. MITIGATION ADOPTED for
   the rest of S8 (per handoff mandate): every commit stays
   path-limited to S8 files; the G12 files are NEVER added; status +
   log re-checked before every commit. DECLARED RISK: the G12 session
   may touch shared theory docs (M0/D3) — my T3 R4 edits will be
   hunk-checked against upstream changes before committing. TOPIC
   OVERLAP NOTE: T2's shock-point extension (spike, P-B1/O3.1
   discharge) is a DIFFERENT deliverable from G12's mesh-limit
   linearization; file sets are disjoint (g0_spike_* vs g12_*).
   T1 commit: a4e4964.

6. T2 [F2-prep/G0] EXECUTED — spike extension written as TWIN file
   validation/g0_spike_axisym_shock.py (S5 spike untouched, its 52/52
   record stands). BRICK A (axisymmetric source term): compatibility
   d(th-nu) = -S+ dx / d(th+nu) = +S- dx with S+- = sin(th)sin(al)/
   (y cos(th+-al)) DERIVED IN-HOUSE from the potential-equation
   characteristic system (left-eigenvector route; planar limit
   re-verified in the derivation); interior + inverse-wall axisym unit
   processes in custom_vjp implicit form; VERIFICATION DUAL-ROUTE
   against the independent Zucrow-Hoffman conservative (u,v)
   compatibility form with order-scaling rejector (route difference
   must scale ~h^3, structural band [4,16] per halving). Results:
   planar-reduction known-answer EXACT (0.0); gradients 36/36 + 16/16
   in derived tol (worst err/tol 6.3e-2); dual-route clean ratios
   4.20/5.82 IN BAND; NEGATIVE CONTROLS: source-sign flip -> ratios
   1.70/1.80 OUT of band, REJECTED; corrupted vjp 36/36 out, REJECTED.
   BRICK B (fitted shock point, RH implicit): z = [beta, M2] on
   theta-beta-M + RH normal-Mach; Newton residual 2.2e-16; gradient
   6/6 in derived tol; Lax certificate margins M1n-1 = +0.26,
   1-M2n = +0.20; O3.1 DOT-PRODUCT IDENTITY err 3.4e-12 vs derived tol
   1.2e-9 -> P-B1 DISCHARGED AT BRICK LEVEL; negative controls:
   corrupted vjp breaks O3.1 (REJECTED), defl = 1.02*delta_max not
   certified (REJECTED — Lax/Majda rejector); transversality collapse
   at the detachment FOLD verified with DERIVED exponent-1/2 scaling
   band (ratio 1.777 in [1.414, 2.828]). DEVIATION FOUND-AND-FIXED
   (declared): first version used an arbitrary 10x collapse factor —
   replaced by the fold-scaling law (sigma_min ~ sqrt(1 - defl/dmax)),
   which is the derived form; the 10x form FAILED honestly (4x
   measured at 0.999 dmax) and was WRONG-BY-CONSTRUCTION, not tuned
   into passing. BRICK C (GENO cross-code interop, READ-ONLY file
   exchange with CASES/tocnoz): throat min-y = yt exact at x = 0; eps
   from contour 29.9547 vs 30 (err 0.045 <= derived tol 0.134 from
   endpoint slope x last grid step); maxtheta recomputed from the
   contour 37.4113 deg vs GENO performance.dat 37.4117 deg (err 4e-4
   deg); negative control 5%-rescaled contour REJECTED. DECLARED
   LIMIT: full O3.4 flowfield cross-check requires the GENO binary
   (reference x/y/u/v/p.dat exist only as checksums; gfortran ABSENT
   on this host, verified) -> stays in NEXT for the G0 decision.
   GENO NOT touched, NOT staged. Overall VERDICT: PASS (exit 0).

7. T2 R4 (same session) — Lemma B PENDING register updated in
   docs/rde_nozzle_P2_lemmaB.md: P-B1 marked DISCHARGED AT BRICK LEVEL
   with numbers + rejectors + declared residual (full-march identity =
   A1 engine); P-B2 annotated with its first brick-level instance
   (dual-route order-scaling test). No class changed (THEOREM rows were
   self-contained; discipline preserved).

8. ⚠️ SECOND CONCURRENCY EVENT + RECONCILIATION — between commits
   a4e4964 (T1) and 001aecc (T2) the parallel rigor campaign COMMITTED
   THREE times (da4cc31 T7-FS/P7 function space + M0 delta; ff97778
   its closure incl. shared docs/rde_nozzle_PROGRESS.md; d94f033
   N6 five-field + remaining-conditionals). Verified: (a) my T2 commit
   diff on docs/rde_nozzle_P2_lemmaB.md contains ONLY my PENDING-
   register hunk (no foreign content swept in — path-limited discipline
   held); (b) file sets disjoint (their targets: M0 T0-caution/N6, M0
   T7, new G12/N6/T7-FS docs; mine: P-1 sections, spike twin, lemmaB
   register); (c) NAMING RECONCILED: their PROGRESS entry already
   declares "S8-rigore ... concorrente alla S8 operativa" — THIS
   session keeps the S8-OPERATIVA label, no renumbering needed
   (precedent S6/S7 pattern, applied by them). CONSEQUENCE for T3/
   closure: M0 and docs/rde_nozzle_PROGRESS.md must be RE-READ before
   my edits (their T0/T7 hunks landed after my session-open read; my
   T3 target = Prop. 7 GAMMA-PURGE paragraph, disjoint from their
   hunks — verified in the diff). T2 commit: 001aecc.

9. T3 [F1/OP-0-gamma tail] EXECUTED (session crossed midnight: steps
   9+ dated 2026-07-17) — src/thrust/phase_diagram_real.py: the
   OP-11-eps diagram RE-DERIVED ON THE PRIMARY EOS-GENERAL ROUTE
   (bounds_gamma reuse: Cantera h(s,P) frozen-CJ isentrope, sonic cap
   w(P*) = h0; ONE shared table re-anchored at the highest grid P0 —
   all cells share the anchor entropy s0), 90 cells, closed forms
   NOWHERE in the primary computations. NEW EXECUTABLE OBJECTS:
   (a) eps*_real from the weighted-transversality quasi-1D reduction
   <P_E(eps; xi)>_mu = Pa solved by bisection on the REAL area-ratio
   inversion — FIRST EOS-GENERAL CARRIER of T7's executable reduction
   (closed form NPR(eps*) = <Pc>/Pa demoted to its oracle);
   (b) knee_real = real adaptation area ratio of the peak phase.
   RESULTS OF RECORD (data/phase_diagram_real.{json,md}): eps* =
   3.494..3.519 across PR 1..90; knee_real 3.49..10.38 — BELOW the
   closed-form knee (~12.9 at PR = 90): the caloric idealization
   overestimates the envelope needed by the peak design; map structure
   CONFIRMED at gamma(T): PR = 1 column all tie, capped band, ZERO
   bell cells, M1 attainment on all 41 knee-fitting cells INCLUDING
   11 subcritical (EOS-general certification of the M1 extension);
   naive instrument never beats the cap, strict loss beyond bar at
   the deepest-spread cells (PR = 90: gap 1.88e-2 s vs bar 1.43e-2 s).
   EQUILIBRIUM BRACKET: shifting-equilibrium ceiling (SP-equilibrate,
   Gibbs solver — ChemEquil warned outside its 3000 K guess range and
   was REPLACED, deviation declared-and-fixed; eq sound speed from
   c^2 = dP/drho on the table) sits +6.34..+6.97% ABOVE the frozen
   ceiling on every PR, bars <= 0.003 s; constant-cp known-answer
   through the eq machinery rel 1.0e-8 vs tol 1.6e-5 PASS, corrupted
   route REJECTED. Executable fix found-and-declared during bring-up:
   table floor Pa/8 (ceiling-only margin) insufficient for the
   area-ratio inversion at PR >= 32 — extended to Pa/64 with derived
   rationale; the eps_star_real RuntimeError guard remains as the
   grid-outrun rejector. Two sub-bar honesty items: near-critical
   cells (PR 49.21/64) have naive-capped gaps GENUINELY below the
   derived bar — the per-cell invariant is two-level (never-beats
   everywhere + strictness at the deepest cells), bounds_gamma
   precedent, NOT a tolerance retune.

10. T3 tests + lint — NEW GROUP (xii) tests/test_phase_diagram_real.py
    (E1-E8: fresh invariants on 90 cells, declared live-recompute
    subset = blessed-PR block, T3/T4-M1 oracles, two-level naive
    metric, eq bracket + LIVE corrupted known-answer rejection, 6
    negative controls, cross-anchor to bounds_ladder_real within
    summed bars diff 6.0e-4 s vs 1.3e-2 s): 20/20 PASS. run_all.py
    registered (suite now 12 groups). Numeric lint (vii): 7 new
    literals classified in validation/numeric_allowlist.json
    (NUMERIC/SPEC with rationale), lint PASS 22 files / 0 unlisted.

11. T3 R4 (same session) — M0 Prop. 7: S7 residual marked DISCHARGED
    + new REAL-ROUTE DIAGRAM INSTANCE OF RECORD paragraph (eps*
    carrier, knee-below-oracle, EOS-general M1, two-level naive
    metric, equilibrium bracket THEOREM* with winner-semantics
    reaffirmation); D3 §8 purge item: residual discharged with the
    same content. Edits verified disjoint from the S8-rigore hunks
    (T0-caution/N6 and T7 areas untouched by me).

12. FULL SUITE GREEN — python tests/run_all.py: 13/13 groups PASS in
    201 s (the 12 expected fast groups (i)-(xii) + slow live
    examples). Group (xii) = 20/20 checks, E5 restructured to the
    two-level naive metric after the honest sub-bar finding (step 9),
    both negative-control paths verified firing.

13. T4 [F1/P-2 rifiniture] EXECUTED — (a) LEXICAL-TRAP FOOTNOTE
    inserted in docs/rde_nozzle_P2_lemmaA.md §3.0 (AIAA 94-3264
    "adjoint constraints" = ADJOINED isoperimetric constraints, not
    the adjoint PDE; NEXT-0 inherited from S6 rigore, now discharged);
    (b) CONTINUOUS ANCHORS cross-reference inserted in
    docs/rde_nozzle_P2_lemmaB.md after the Prop.-A1-twin remark:
    (B.6) transports Prop. A3's invariant, J_k^{-T} solvability uses
    Prop. A2's off-kernel nondegeneracy (explicit pointers to lemmaA
    §3.3-§3.4 + the dual-route carrier); (c) P-A script consolidation
    EVALUATED, decision DEFERRED with data: measured runtimes
    pa1_symbolic_lemmaA.py 5.4 s + p2_pA1_symbolic_adjoint.py 51.0 s
    (both PASS standalone today) -> a combined suite group (xiii)
    would add ~1 min and exceed the declared 12-group S8 target;
    proposal for NEXT: subprocess group '(xiii) P-A symbolic
    carriers' running both scripts, cost ~56 s.

14. ⚠️ THIRD CONCURRENCY EVENT + POST-COMMIT AUDIT — two further
    foreign commits (8e24060, 36de0a5, "[F1/SCAFFOLD]") landed before
    the T3 commit, and the shared tree carried foreign UNCOMMITTED
    modifications (data/q_mapping.{json,md}). Audit results: (a) my
    path-limited T3 add did NOT stage q_mapping.*; (b) the SCAFFOLD
    commits touched only their own files (no M0/D3); (c) my T3 commit
    contains exactly ONE hunk in M0 (line 434, Prop. 7) and ONE in D3
    (line 490) — both mine; no cross-contamination in either
    direction. T3 = 528e033, T4 = eab6cf5.

15. SESSION CLOSE (R3) — docs/rde_nozzle_PROGRESS.md updated on top
    of the S8-rigore-committed version: new ORA (S8-operativa closure,
    both concurrency events declared), NEXT rewritten for Sessione 9
    (G0 formal decision first, with the GENO-toolchain residual named;
    P-1 §5-§7; group (xiii) proposal; leads with the raw-HTML method
    pin; G5 user dispatch), BLOCCATO G0 entry updated (flowfield
    cross-code blocked on absent gfortran), LOG SESSIONI entry
    S8-operativa added above S8-rigore. Project memory updated
    (research state + gamma-generality purge completion). TASKS
    DELIVERED: T1, T2, T3, T4 (T5 declared not executed). Suite
    13/13. LOG DEFINITIVELY CLOSED at step 15.
