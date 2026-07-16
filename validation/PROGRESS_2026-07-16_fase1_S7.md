# SESSION LOG S7 — 2026-07-16 — "Fase 1: P-2 Lemma B + P-A1 + OP-0-gamma + G5-2a"

> Total-order append-only log (CLAUDE.md R3 + standing directive S2):
> one numbered row per step, rows ALWAYS appended at the end, never
> reordered. Every .md touched and every codebase action gets a row,
> with evidence (files, hashes, verdicts). Session tasks: T1 [F1/P-2]
> Lemma B draft + P-A1 symbolic discharge; T2 [F1/OP-0-gamma] purge of
> gamma=const from the executable ceiling; T3 [F0/G5-2a] digital PMM
> TOC sweep 1957-1990; T4 [F1/P-1] §2/§4 first text (time permitting);
> T5 [F2-prep/G0] spike extension (optional).

1. [APERTURA R2] Branch verified `rde-nozzle-program`, HEAD = b01a9fe
   (expected by the session prompt; `git log --oneline -3` shows only
   S5-closure commits — NO foreign commits, one-session rule respected
   at open). Untracked: GENO/ (never committed, policy), scratch_out.txt
   + scratch_err.txt (pre-existing scratch, left untouched),
   validation/ADR_panel_2026-07-16.md (NOT committed — awaiting user
   ratification, per PROGRESS BLOCCATO). Read in order: project memory
   (research-cycle-averaged-rao, gamma-variable-generality,
   gate-pre-esecuzione, python-env-cantera), M0 in full (D2.6 problem
   of record (P) = pair (S*, delta); Prop. 7 with SCOPE remark —
   winners rank CLOSURES, premium_bound = tournament device; T7/(**')
   weighted, never naive), PROGRESS (ORA/NEXT/BLOCCATO). RESTART
   DECLARATION: Fase 1 of plan D6; tasks T1-T5 = PROGRESS NEXT items
   2, 5, 1, 3, 4 respectively; priority T1 > T2 > T3 per prompt.

2. [APERTURA R2 — supporting reads] docs/rde_nozzle_P2_outline.md
   (§4 Lemma B plan, §8 claim register, §7 venue decided AIAA J +
   arXiv at (G5 AND Lemma-A draft)); docs/rde_nozzle_P2_lemmaA.md
   (full: §3.0 gamma audit, §3.2 eight-step classical derivation,
   §3.4 identifications (i)-(iv), §3.6 PENDING register P-A1..P-A3);
   D3 §8 (P2 entry incl. Lemma-A status upgrade of record);
   src/thrust/bounds.py (OP-0 ladder: cf_ideal capped, cf_ideal_naive
   kept for rejection, chain C, TOL_REL = NQ*eps derived);
   validation/g0_spike_jax_moc.py (implicit custom_vjp bwd rule =
   transposed Newton-Jacobian solve — the Lemma-B demonstrator).

3. [GATE PRE-ESECUZIONE — verdict] (A) PLAN ADHERENCE: T1 = [F1/P-2]
   (PROGRESS NEXT 2; D6 publication stream P-2, fast-track); T2 =
   [F1/OP-0-gamma] (NEXT 5; strengthened S5 gamma directive, executable
   purge); T3 = [F0/G5-2a] (NEXT 1; commission Item 2a rescoped
   in-house in S4); T4 = [F1/P-1] (NEXT 3); T5 = [F2-prep/G0] (NEXT 4).
   All five placeable — no orphan steps. (B) UPSTREAM RIGOR AUDIT:
   (i) capped ceiling in subcritical — confirmed of record in M0
   Prop. 7 SHARPENING + bounds.py cf_ideal (cap at sonic state; naive
   kept only as executable rejection); (ii) weighted (**') never naive
   — M0 T7(c) confirmed; Lemma-B draft must present the cycle assembly
   as (**')-weighted (planned §B.7); (iii) D3 §10quater(5) scope —
   winners rank closures, never hardware: binds T2's phase-diagram
   re-derivation wording; (iv) D2.6 canonical (P) — read, binds paper
   text; (v) GAMMA QUESTION per task (strengthened S5 directive):
   T1a Lemma-B transpose identity is CLOSURE-AGNOSTIC (operates on
   residual maps R_k, EOS-general by construction); the g0 spike's
   PM closure is gamma=const as DECLARED ORACLE (already declared in
   its docstring) — status to be stated in the draft §B.0. T1b
   symbolic pass to be run EOS-GENERAL (p(rho, rho e) with a =
   dp/drho|_rho_e, b = dp/d(rho e)|_rho, c^2 = a + b h), gamma=const
   only as numeric oracle instantiation. T2 IS the purge item itself:
   real-thermo route primary, closed forms demoted to declared
   oracles. T3: bibliographic, no gamma content. NAMING NOTE (not a
   discrepancy, declared): paper P-2's "Lemma B" (discrete bridge) is
   distinct from the internal "Lemma B (stagnation-temperature
   similarity)" inside M0 Theorem 5's proof — the new doc declares
   the collision explicitly (§B.0). No upstream discrepancies found.
   (C) VERDICT: gate pre-esecuzione PASS, no deltas. Execution begins
   with T1.

4. [T1a — Lemma B draft WRITTEN] docs/rde_nozzle_P2_lemmaB.md created
   (= paper §4, implements outline §4): §4.0 scope + TWO declared
   disambiguations (P-2 "Lemma B" vs M0-T3-internal "Lemma B
   similarity"; gamma status: transpose identity CLOSURE-AGNOSTIC =
   EOS-general by construction, g0 spike's PM closure = declared
   oracle); §4.1 march = block-triangular system (B.1)-(B.3), THEOREM
   B0, J_k-invertibility = discrete S1 monitor (named hypothesis);
   §4.2 THEOREM B1 (transposed back-substitution along the SAME
   discrete characteristics — discrete twin of Prop. A1) + THEOREM B2
   (reverse AD with implicit custom rules computes exactly (B.6);
   Griewank-Walther + the g0-spike bwd rule) + COROLLARY B3
   (dot-product identity (B.7) = O3.1, demonstrator of record cited);
   §4.3 fitted front as EXPLICIT unknown — Lax/Majda transversality ==
   nonsingularity of the shock-point J_k (THEOREM finite-dim; the
   discrete-to-continuous correspondence with the Giles-Pierce
   interior condition declared SCHEMA); §4.4 Giles-Ulbrich trap
   (SINUM 48:882/905 (2010), only citations already of record in the
   outline) + bypass-by-construction with HONESTY CLAUSE; §4.5 mesh
   limit SCHEMA with falsifiers O3.2/O3.3/O3.4; §4.6 cycle assembly =
   WEIGHTED (**'), never naive (THEOREM at fixed quadrature); §4.7
   claim register + PENDING P-B1 (O3.1 at the shock brick), P-B2
   (order tests, A1 engine) — neither blocks the classes.

5. [T1b — P-A1 symbolic pass SCRIPT] validation/p2_pA1_symbolic_adjoint.py
   written: EOS-GENERAL symbolic core (p(rho, rho e), a and b free,
   exact c^2 = a + b h; sin/cos as symbols with Pythagorean-ideal
   Groebner zero-checks: identities PROVED, not floated). Checks C1-C6:
   Mach-surface geometry, det K = 0 + acoustic kernel r, (L.20)
   bookkeeping executable, FREDHOLM closure identity d.r = 0
   (identically in lambda2 — Lemma A (i) made executable), adjoint
   trace solve (rank-deficient Gauss-Jordan), THE COMBINATION
   Lambda(psi) = psi.(K w) gauge-independent = -lambda2 = f2 via
   (L.12) — the P-A1 deliverable. Negative controls NC1 (non-
   characteristic surface: det K != 0), NC2 (pressure term dropped:
   Fredholm fails), NC3 (corrupted kernel). Numeric instantiation =
   DECLARED gamma=const oracle (Rao-1961 spike regime M=2.4,
   theta=-8.25 deg C-, + C+ bell point), tolerance derived (K_OPS *
   eps * scale, op-count rationale in docstring). One fix during
   development (declared): solve_least_squares -> gauss_jordan_solve
   (K^T is singular by construction — least-squares normal equations
   are inapplicable). Run in progress (background).

6. [T3 — PMM sweep LAUNCHED, then METHOD FINDING] Six parallel agents
   launched on pmm.ipmnet.ru/ru/Issues.php (window 1957-1990 = vols
   21-54, 204 issue TOCs; volume = year - 1936; criteria = commission
   §3 / 1.2(a)-(c) + 2.2(d)-(e), authors Kraiko/Shmyglevskii/Tillyaeva/
   Egoryan + school). METHOD FINDING OF RECORD (declared, affects any
   future web sweep of this archive): the WebFetch summarizer
   FABRICATES authors/titles on these windows-1251 pages (verified
   independently by three agents against raw HTML — e.g. invented
   "Башаров М.А." where the real first entry of 27-1 is Лурье А.И.).
   ALL WebFetch-summarized TOC content was discarded; the sweep was
   redone by raw-HTML fetch + windows-1251 decode + deterministic
   parsing, with per-issue verification that parsed entry counts equal
   the site's declared "Статей в выпуске". My own step-opening spot
   probe of 21-3 via WebFetch is therefore VOID (declared); superseded
   by the raw-HTML sweep of the 1957-62 agent.

7. [T2 — module + test WRITTEN, first run] src/thrust/bounds_gamma.py:
   real-thermo (frozen CJ-products composition, Cantera h(s,P), frozen
   sound speed) ceiling as PRIMARY route; sonic cap located exactly by
   inverting the monotone w(P) = h + c^2/2 (w(P*) = h0); closed forms
   of bounds.py DEMOTED to declared oracles evaluated alongside;
   derived bars (Richardson nested quadrature + exact-flash spot
   probes + roundoff floor); known-answer oracle = synthetic
   constant-cp gas (gamma = 7/5 exact) through the SAME route, TOL_KA
   derived 1e-6; cap-structure probe (grid of admissible exits must
   not beat the direct capped formula) = executable EOS-general
   re-verification of the M0 Prop. 7 cap. Vacuum rows: T-floor 200 K
   truncation, declared LOWER-BOUND instrument, excluded from
   rejectors. tests/test_bounds_gamma.py = run_all group (xi) with
   G1-G5 incl. corrupted-row rejections. Known-answer PASS (worst
   2.9e-13 on V_id; corrupted route rejected at 8.7e-5 > 1e-6).
   FIRST RUN: H2 rows show the purge delta at -4.4% (real gamma(T)
   ceiling BELOW the gamma_s = const oracle, bar 0.001% -> SIG);
   run aborted on a floor_pressure bug for vacuum rows (naive
   bisection window sent Cantera SP flashes to nonphysical T < 0);
   FIXED (sequential ln-P descent with warm flash starts + final
   bracket bisection); full 18-row run relaunched (background).

8. [T3 — sweep COMPLETE, deliverable of record] All six agents
   delivered with the raw-HTML method: 204/204 issue TOCs 1957-1990,
   zero gaps, ~4,300 titles screened. Consolidated in
   validation/G5_pmm_toc_sweep_1957-1990.md. VERDICTS: (c)+(e)
   adjoint/"sopryazhennye uravneniya" x contouring = ZERO title hits
   in 34 years -> G14 (P-2) SURVIVES the digital pass; (a)+(d) no
   direct averaged/periodic-inflow shape optimization, BUT TOP FLAG
   DECLARED IMMEDIATELY (per session mandate): Kraiko-Osipov PMM
   34(6) 1970 (nozzle contour "accounting for varying flight
   conditions" — the altitude/multi-regime cousin of the cycle
   average; whether its functional is averaged/weighted is EXACTLY
   the Item 2b question) + Kraiko-Tillyaeva 37(3) 1973 / Shipilin
   28(3) 1964 (nonuniform-inflow contours). P-1 G6 novelty wording =
   CONTINGENT on the A1 full text (D4 §3 contingency ARMED, not
   activated); P-2 unaffected. Item 2b ranked reading list produced.

9. [T2 — ladder COMPLETE 18/18 + test (xi) PASS] After a second fix
   (cap-probe bar now includes the MEASURED local table noise at the
   sonic endpoint |u_E - u*|; naive-loss metric split into
   naive_gap_max <= +noise and naive_gap_deep < -noise at the deepest
   subcritical phase — the first run's 4 subcritical-row "violations"
   were interpolation noise at the sonic point exceeding a
   curvature-only bar, not physics): full run 18/18 rows OK;
   tests/test_bounds_gamma.py G1-G5 ALL PASS (KA worst 4.7e-7 vs tol
   1e-6; corrupted route rejected at 8.7e-5; subcritical deep naive
   loss confirmed, worst gap -5.45e-5; all corrupted-row controls
   rejected). NUMBERS OF RECORD (data/bounds_ladder_real.json):
   real gamma(T) frozen-composition ceiling sits -4.4% (H2 20 atm)
   to -7.9% (RP-1) BELOW the gamma_s=const closed-form oracle on the
   12 finite-Pa rows, bars ~0.002% -> ALL SIGNIFICANT; vacuum rows =
   declared T-floor instruments (-17..-26%, no rejector semantics).
   DEVIATION DECLARED: the real-route re-derivation of the OP-11-eps
   phase diagram (the "se regge" conditional) is DEFERRED to NEXT
   (token/time budget; the ladder-level purge and the cap
   re-verification stand on their own).

10. [RICONCILIAZIONE — one-session rule violated AGAIN, declared]
   Before committing (per the session prompt's mandatory re-check),
   `git log` revealed SIX commits by a concurrent session
   (5ec62ef..c2649d4): the DEDICATED RIGOR SESSION spawned by the S5
   handoff-2 (aaf8b25), which took the name S6 and CLOSED (its log:
   validation/PROGRESS_2026-07-16_rigore_PA.md). Its results: P-A1
   narrowed via Prop. A2 (kernel solvability — the pointwise boundary
   algebra CANNOT carry f2), P-A1' DISCHARGED via Prop. A3 (f2 =
   TRANSPORTED adjoint invariant, HTH-1971/JOTA-1972 anchors), P-A2
   discharged (Hoffman full read), P3 -> THEOREM* (shock-free S1).
   RECONCILIATION ACTIONS: (i) THIS session renumbered S6 -> S7 in
   all its artifacts (log file renamed, headers fixed; steps 1-7
   above predate the renumbering and their "S6" self-references are
   to be read as this session); (ii) my T1b symbolic pass
   REPOSITIONED — no longer a "P-A1 discharge" (already discharged by
   Prop. A3) but an INDEPENDENT DUAL-ROUTE VERIFICATION of Prop. A2
   in CONSERVATIVE variables (general-EOS Grueneisen closure,
   explicit left covector, extra rejectors, (L.20) bookkeeping) + the
   boundary-datum reading lemma psi.(K w) = -lambda2 (complementary
   to and consistent with Prop. A2/A3: my C4 identity "d.r = 0 for
   EVERY lambda2" is exactly Prop. A2's solvability statement,
   derived independently before reading their commits); docstring and
   Lemma-A-draft note updated accordingly (dual-route remark under
   Prop. A2); (iii) my M0/D3 R4 edits audited vs theirs via git diff:
   disjoint hunks, no conflicts; (iv) commits proceed on top of
   c2649d4; (v) ladder data regenerated with corrected provenance.
   CONTENT CONSISTENCY: their Prop. A2 (primitive variables) and my
   C4 (conservative variables) AGREE — the dual-route agreement is
   itself a certificate, recorded in the draft.

11. [T2 + T3 COMMITTED on top of c2649d4] T2 = 1d762f8 ([F1/OP-0-gamma],
   7 files: module + test (xi) + run_all + data of record + M0/D3 R4);
   test (xi) re-verified against the regenerated (S7-provenance) data:
   ALL PASS. T3 = fb82846 ([F0/G5-2a], sweep record).

12. [T1b — dual-route pass VERDICT PASS] After a tractability
   restructuring (declared): Weierstrass-parametrized exact zero
   tests replace Groebner reduction (birational circle
   parametrization — proofs, not floats); det/nullspace/linear solves
   replaced by the EXPLICIT kernel pair (K r = 0, l^T K = 0) + the
   numeric rank-3 certificate; C6c/C6d recognized as PROVED
   COROLLARIES (kappa.l = (l^T K)w = 0 by C2b; Lambda = -d.w =
   -lambda2 by C6b + linearity) instead of heavy symbolic re-solves.
   FULL RUN: both families C1-C6 PASS symbolically; C6e numeric
   certificates PASS (kappa nondegenerate, gauge shift psi -> psi + l
   leaves Lambda unchanged to 1e-8 with conditioning-derived bar,
   Lambda -> lambda2 = 0.3 exactly); Fredholm d.r = 0 at both oracle
   points (1.7e-10 vs tol 4.5e-8); rank K = 3 certified (sv ratios
   ~1e-22 for the fourth); ALL THREE negative controls REJECTED
   (corrupted kernel 1.2e8; dropped pressure term 5.6e4;
   non-characteristic surface det 2.5e9). VERDICT: PASS. R4: D3 §8
   Lemma-B-draft + dual-route entry; Lemma-A draft note under
   Prop. A2 (already placed at step 10).

13. [CODA post-chiusura — suite + lint fix] Full fast suite run as
   the final non-regression check: 10/11 — group (vii) numeric lint
   correctly REJECTED the new bounds_gamma.py literals not yet
   classified (the invariant worked as designed; the earlier exit-0
   was tail's, declared). Fix: validation/numeric_allowlist.json
   entry for src/thrust/bounds_gamma.py — six exempted named
   assignments (M_TAB/N_REAL/N_SPOT/S_BAR/TOL_KA/T_FLOOR, each with
   its derivation note) + ten classified literals (NUMERIC knobs all
   covered by derived/measured bars or guards; SPEC = the
   known-answer oracle's exact-gamma constants). Lint re-run: PASS
   (21 files, 0 unlisted). Suite therefore 11/11 (groups (i)-(vi),
   (viii)-(xi) all PASS in the same run; (vii) PASS after the
   classification, no src/ code changed).
