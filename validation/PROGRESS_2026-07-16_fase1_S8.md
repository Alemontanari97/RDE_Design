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
