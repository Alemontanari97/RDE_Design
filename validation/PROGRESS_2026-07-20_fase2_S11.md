# PROGRESS S11 — 2026-07-20 — FASE 2/A1 BRICK 1 (profile-generation machinery) + coda P-1

Total-order session log (user directive of record: one numbered row per
step / file / commit). Session S11, branch `rde-nozzle-program`.

1. APERTURA (R2 + S9 order). HEAD verified = ded6f56 (S10 closure) —
   no foreign commits, single session. Working tree: only GENO/
   (independent repo, never committed) and validation/ADR_panel_...
   (untracked, awaiting user ratification) — both expected, untouched.
   Read in order: project memory (research-cycle-averaged-rao,
   gate-pre-esecuzione, gamma-variable-generality, periodic-wave-data-
   scope, python-env-cantera, repo-sota-standard); L0 = SCAFFOLD §1;
   docs/claims_registry.yaml (schema + conventions header, definitions
   block); D6 Phase A1 (OPEN, G0 DECIDED [DIR-G0]); PROGRESS
   (ORA S10 / NEXT S11 / BLOCCATO). Depth reads:
   docs/rde_nozzle_G0_decision.md (§4 scope + falsifiers, full),
   M0 VI.1-VI.7 incl. VI.4bis(iii) (EOS-general backend mandatory;
   gamma=const corner<->eps bijection FORBIDDEN as a solver step),
   P-2 Lemma B statement set (march = block-triangular; reverse-AD =
   transposed sweep; implicit rules per cell, never unrolled),
   X-GENOXC carrier (validation/g0_geno_crosscode.py) and both G0
   spikes (validation/g0_spike_jax_moc.py, g0_spike_axisym_shock.py).
   Declaration: restart from PROGRESS NEXT S11 item 1 = [F2/A1 BRICK 1]
   (T1), then [F1/P-1] remaining sections (T2), optional [L6] T-NSW
   (T3). Priority T1 >> T2 (user prompt).

2. GENO RECONNAISSANCE for the ideal-nozzle twin (read-only source
   study; GENO never modified). Ch.16 type-0 pipeline identified line
   by line: Sauer IVL (InitialValues_m: alpha =
   sqrt((1+delta)/((gm+1) rtu yt)), eps-shift, u = as(1+alpha x+c2 y^2),
   v=0; Simpson mdot; as from secant M(as)=1.000005 on td%solve);
   leggeAree (Performance_m: Me from eps via mdot/(pi yt^2) =
   rho(Me) q(Me) eps, secant); initialExpansion fan (C- lines from IVL
   points to axis; interior + axis unit processes);
   throatExpansion_solve (CircularContour_m: wall on circular arc rtd,
   wall_angle = da*(i-NI); inverse-wall unit process with chord foot
   search + void-row (Nv) bookkeeping; interior sweep; axis append
   j2+1 per column; STOP when axis M reaches Me with linear wall_angle
   interpolation (flag=1) to |M-Me|<1e-5, then Me := achieved M);
   idealNozzleSub_solve (Profile_m: uniform-exit region; row j2
   marches ALONG THE EXIT MACH LINE from the focus K at slope
   1/sqrt(Me^2-1) with uniform state; columns = C- lines from the Mach
   line up to the wall; WALL = BOUNDING STREAMLINE placed where the
   cumulated massflow (Performance_m::massflow trapezoid) reaches
   mdot_ref, linear interpolation on the crossing segment; Ne-1
   columns to xe = x_K + ye sqrt(Me^2-1), ye from mdot). Unit
   processes (Interior_m/Axis_m/InverseWall_m): average-coefficient
   (u,v) compatibility qm u4 + rm v4 = tm with coefficients at
   MIDPOINT states, predictor-corrector to E1=E2=tol_conv=1e-8 — the
   PC fixed point is exactly an implicit nonlinear system (our Newton
   target). Thermo backend=0 (Types_thermo_sm case 0 + IO_m init):
   NASA-7 blended equivalent species (mole-fraction-weighted
   coefficient sums, break T = 1000 K for all 8 species), frozen
   composition = raptor.plt row 4 (throat, Bray), stagnation h0/s0/
   ts/ps = row 2 (x1000, x1000, K, x1e5), MixEntropy = Runi sum x ln x,
   Rg = Runi/mixM*1000, Runi = 8.31451; state closure q -> T (secant
   on h(T)+q^2/2 = h0) -> p = 1e5 exp((s0m(T)-s0)/Rg) -> rho, c^2 =
   gamma(T) Rg T. Defaults confirmed in IO_m: NI=401, NT=10001,
   Ne=2001, da=0.1 deg, icor=20, tol_conv=1e-8, pa=0. Ini keys
   confirmed: [GENO-nozzle] da (deg), eps, yt, rtu, rtd, thermoname,
   frozenname, backend; [GENO-solver] NI, NT, Ne, icor, tol_conv, pa.

3. GATE PRE-ESECUZIONE (standing directive, logged BEFORE execution).
   (A) PLAN ADHERENCE: T1 = D6 Phase A1 first brick == PROGRESS NEXT
   S11 item 1 (explicit S10 user expectation; G0 dossier §4 names
   profile-generation machinery = A1, this session); T2 = F1/P-1
   remaining sections == NEXT item 2; T3 (optional) = L6 == NEXT
   item 4. No orphan step. Pending user decisions (G5 dispatch, ADR
   ratification, G0 out-of-criteria ratification) NOT forced — remain
   in BLOCCATO.
   (B) UPSTREAM RIGOR AUDIT (anchors re-read this session):
   - Weighted (**') / capped ceiling / winner-never-hardware / D2.6:
     NOT touched by brick 1 (the ideal-nozzle target is a DIRECT march
     with no thrust objective and no averaging; the variational TOC
     brick with (**')/corner via dJ/dSigma is NOT attempted this
     session unless time allows — if absent it is declared NEXT, per
     the task contract).
   - GAMMA QUESTION (VI.4bis(iii) + DIR-GAMMA): twin march primary
     route = tabulated frozen-mixture isentrope (h(T), s0(T), gamma(T)
     tables; Cantera as PRIMARY table source; GENO's NASA file as the
     declared file-exchange interop source; both EOS-general in
     structure), (u,v) compatibility with local c — NO Prandtl-Meyer
     closed form and NO gamma=const bijection anywhere in the primary
     path; gamma=const appears ONLY as a synthetic known-answer oracle
     backend with rejector.
   - Lemma B pins: every unit process = implicit residual in
     jax.custom_vjp with the implicit-function rule (never unrolled);
     march assembled as the block-triangular system; O3.1 dot-product
     identity on the ENTIRE march with derived tolerance.
   - X-GENOXC stays the standing cell-level regression (untouched).
   No discrepancies found in the anchors; no R4 pre-fix needed.
   (C) VERDICT: gate pre-esecuzione PASS. Execution order: T1 (a-e)
   -> registry entries BEFORE citation -> R4 (M0 VI.7 addendum / D6 A1
   state) -> commit [F2/A1]; then T2 -> commit [F1/P-1]; R3 closure.
   DECLARED DEVIATION (in advance, honest): the end-to-end GENO
   comparison runs on a REDUCED-RESOLUTION twin case (own input.ini in
   an untracked scratch case dir, GENO binary re-run read-only in WSL;
   NI/Ne/da scaled down) because the default-resolution march
   (NI=401, Ne=2001) is intractable for whole-march reverse-mode
   tracing in one session; production-scale loop speed remains the
   ARMED G0 loop-speed falsifier (G0 dossier §4), not re-adjudicated
   here.

4. T1 REFERENCE CASE (file exchange, GENO never modified). Reduced
   twin case created in the session scratchpad (input.ini:
   nozzle_type=0 axisymmetric, yt=1, rtu=1.5, rtd=0.45, da=0.5 deg,
   eps=4, backend=0, NI=21, Ne=41; thermo files copied beside it —
   the FiNeR ini parser rejects paths with spaces, found empirically)
   and run with the WSL bin/GENO (ct-env LD_LIBRARY_PATH): exit 0,
   86 columns x 64 rows, achieved Me 2.6139377, eps 4.000001,
   maxtheta 16.265 deg, Cd 0.9820. Outputs untracked (scratch).

5. T1 CARRIER WRITTEN (validation/a1_ideal_march_jax.py, ~1250
   lines): assembled march (Sauer IVL -> fan -> arc throat expansion
   with inverse-wall + chord-foot search + void rows + wall-angle
   interpolation -> uniform-exit region with wall = bounding
   mass-flow streamline), unit processes as implicit custom_vjp
   Newton systems in GENO's exact corrector fixed-point form
   (midpoint-state coefficients); record/replay schedule (frozen
   topology) for whole-march differentiation; TABULATED thermo
   backend (user directive of the day, memory
   thermo-tabulated-backend: interface = tables, GENO backend-1
   model; generators: Cantera PRIMARY / GENO NASA-poly interop
   instance / gconst declared oracle). First evidence: twin Sauer IVL
   vs GENO column 1 max|dx| = 1.1e-16, max|du| = 8.6e-8 (GENO's
   as-secant tolerance, below truncation); leggeAree twin Me
   2.613938 vs GENO 2.6139377.

6. T1 DEBUG TRAIL (honest, in order). (a) First marches NaN from the
   first fan cell: the near-sonic fan cells are razor-thin
   (alpha -> 90 deg) and a generic z0 leaves the M > 1 domain ->
   FIX: GENO's own PREDICTOR (foot-state coefficients) as Newton
   seed + damped NaN-safe Newton (trial steps incl. t=0, residual
   monotone; a stalled cell fails certification instead of poisoning
   the march). (b) XLA compile explosion (30 unrolled damped
   iterations) -> lax.fori_loop (one compiled body). (c) March still
   frozen sonic at the axis: cell-by-cell PROBE vs the GENO grid
   showed fan == GENO to 3.5e-4 and the first arc column == GENO to
   1e-6 (axis u 1672.767 identical) -> the predictor wiring had
   applied to ONE site only (whitespace-mismatched replace);
   asserted-count rewiring of all five z0 sites. (d) Certification
   metric artifact: max|R| vs |z|-scale mixes units (compat rows
   ~ u^3) -> worst 7.8e3 at machine-converged cells; REDEFINED
   unit-consistently in z-space (one extra Newton step must move the
   solution < 100 eps scale(z)); jitted per solver.

7. T1 BASE MARCH OF RECORD (NI=21, da=0.5, Ne=41, NASA tables):
   194 s, 2756 cells ALL certified (worst step/tol 1.4e-2), 23 arc +
   40 streamline wall points; Me_achieved 2.6139377 = GENO to 7
   digits; exit (7.3408, 2.0000003), eps_out 4.000001046 = GENO;
   quick full-contour comparison: max|dy| = 7.6e-9 (median 6.5e-10)
   over 62 overlap samples; max wall angle recomputed 16.265 deg =
   GENO maxtheta (the peak lives in the streamline region — the arc
   ends at 11.44 deg in BOTH codes, 25 arc columns each).

8. T1 CANTERA PRIMARY ROUTE. ct.Species thermo attach + NasaPoly2
   coefficient order determined EMPIRICALLY (hi-first matches the
   hand evaluation at 500/2000 K; lo-first REJECTED by cp);
   entropy sampled at 1 atm (the NASA7 data reference — GENO's
   s0(T) convention); Thigh extended to the table top (H stops at
   3500 K: GENO extrapolates the blended polynomial implicitly, the
   Cantera instance mirrors it, declared). Residual dual-route delta
   is a GENUINE physical-constants difference (engine R, plt mole
   fractions sum 0.99997 used unnormalized by GENO, file-vs-element
   molar masses) -> check reframed with the DERIVED constants budget
   (|dR/R| + |1-sum x| + max|dM/M| = 2.5e-4): rescaled relative
   deltas h/s0/cp = 5.3e-6 <= K*budget = 9.9e-4 PASS; corrupted-table
   rejector at 1e-3 (above budget). Machine-level validation of the
   GENO-convention route = the S4 end-to-end contour (7.6e-9).

9. T1 FULL CARRIER RUN 1: VERDICT PASS on every counted check
   (S1 dual-route + gconst oracle with rejectors; S2 base certified;
   S3 refined certified, dMe 5.2e-6; S4 contour 62/62 in band, max
   err 7.589e-9, band 4.5e-3, Me delta 8.4e-9; S5 cantera contour
   max|dy| 2.0e-7 within constants-budget bound; S6 replay fidelity
   1.6e-13, O3.1 = 2.714e-10 vs tol 5.094e-8, corrupted vjp
   rejected). DEFECT FOUND AND DECLARED: the N1 corrupted-source
   control CRASHED (corrupted march cannot place the wall — the
   broken mass balance never crosses mdot: a physically meaningful
   REFUSAL) and the S4 exception handler swallowed it as
   "GENO reference unavailable -> SKIP", so the control was not
   counted. FIX: exception structure split (reference acquisition
   vs negative control); a corrupted-march RuntimeError now counts
   as rejection-by-refusal (attribution: the clean march completed
   on the identical code path in S2). Carrier RELAUNCHED for the
   clean verdict of record.

10. R4 SAME SESSION (theory/registry back-propagation). M0 Part VI:
    "A1 BRICK 1 OF RECORD" addendum (machinery + verdict numbers +
    [DIR-THERMOTAB] pin strengthening VI.4bis(iii): tables-only
    backend, Cantera sole production generator) after the G0
    addendum. D6 Phase A1: STATUS S11 BRICK 1 DONE + next bricks
    (variational TOC via dJ/dSigma, fitted sheet, plug free
    boundary). Registry: [X-A1IM] carrier entry, [DIR-THERMOTAB]
    directive, [PAP-P1S1389] paper record, [PAP-P1S57]
    FOUND-AND-ALIGNED (the S10 session omitted the sections_5_7
    paper record; precedent PAP-P1S24 — added structure-only,
    declared); T-LEMB carriers += X-A1IM. P-2 Lemma B §4.7 register:
    march-level O3.1 instance of record (shock-free half; fitted-
    sheet march + P-B2 order tests declared still open). Claims lint
    standalone: PASS, 89 entries, triple rejector proven.

11. T1 CLEAN VERDICT OF RECORD (carrier run 2, 2026-07-21): VERDICT
    PASS with ALL 14 checks counted — dual-route budget + rejector;
    gconst known-answer + rejector; base/refined/cantera cells
    Newton-certified; end-to-end contour inside the derived band
    (62/62, max err 7.589e-9); N1 corrupted march rejected BY REFUSAL
    ("straightening column 191: no wall crossing" — the flipped
    source breaks the mass balance; clean march completed on the
    identical path); primary-route contour consistent; replay
    fidelity; O3.1 whole-march 2.714e-10 vs tol 5.094e-8; corrupted
    whole-march vjp rejected. A1 BRICK 1 = DONE.

12. T2 [F1/P-1] SECTIONS §1, §3, §8, §9 FULL TEXT OF RECORD
    (docs/rde_nozzle_P1_sections_1_3_8_9.md): §1 with the var-gamma
    genealogy and the MANDATORY Rao 1958 IAC Amsterdam citation
    (abstract-verified ONLY, attribution bounded to the abstract,
    Springer DOI of record); §1.4 novelty query-bounded + contingent
    on Kraiko-Osipov PMM 34(6) 1970; §3 steadification [T-T0] +
    sharp N6 boundary ([T-N6-2]/[T-N6-3], class refresh vs skeleton
    DECLARED) + N-SW [T-NSW]; §8 EAP/S-H containment bridges (term
    maps, three findings as theorem instances, 3-5%/6-14% check,
    phi placement); §9 limits/outlook (single conditional spine,
    ladder, biases B1/B2). Audit line [Class | Falsifier | Carrier |
    Gamma status] per subsection; claims by registry ID (21 IDs, all
    resolving). Coherence grep PASS (zero winner-as-hardware
    readings, zero unqualified attribution). Skeleton DRAFT TEXT
    STATUS updated: BODY TEXT COMPLETE, remaining appendices +
    assembly.

13. COMMITS (protocol: git log -3 + status before each; path-limited;
    post-commit hunk audit). Pre-commit check: HEAD ded6f56, no
    foreign commits, single session; untracked `literature/` = user
    material, NOT touched/committed (declared); ADR panel untracked
    per discipline. T1 = 8fc815e ([F2/A1], 5 files, 1376 insertions;
    hunk audit: M0 pure insertion, D6 13 insertions, registry's only
    deletions = the declared T-LEMB carrier-line update; no foreign
    content). T2 = c0065af ([F1/P-1], 2 files, 391 insertions).

14. R3 CLOSURE. FULL SUITE: 16/16 groups PASS exit 0 in 232 s
    (healthy host; incl. (xv) claims lint on the 89-entry registry
    and (xiv) rigor tier 36.5 s). data/q_mapping.{json,md} datestamps
    regenerated by the live examples (diff = 2 datestamp lines,
    content identical) — RESTORED, declared (standing lesson).
    PROGRESS updated (ORA S11 / NEXT S12 with the variational-TOC
    brick as NEXT 1 / BLOCCATO unchanged / LOG S11 entry); INDEX row
    added; project memory updated (research state S11 + the
    thermo-tabulated-backend directive strengthened with the
    Cantera-sole-generator decision and the S11 technical pins;
    operational lessons: detached processes survive harness restarts
    — kill stale python3.13 by PID; stdout block-buffering on
    redirected files — progress to stderr; FiNeR ini parser rejects
    paths with spaces). Total-order log CLOSED at step 14. Session
    S12 restarts from memoria + L0 + registro + PROGRESS (+ D6) only.
