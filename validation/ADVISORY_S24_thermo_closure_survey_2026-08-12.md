# ADVISORY — Thermo-closure survey: [X-THC1] vs NASA9-direct / ATLAS-dCp / FLINT-style

- **Date**: 2026-08-12 (S24 window)
- **Workflow**: three independent investigators -> judge with refuter duty; **judge-adjudicated in one round** (no second pass; disputed points re-verified by the judge against the sources/artifacts directly)
- **Participants**: I1 (FLINT library + GENO backend-1 wiring), I2 (ATLAS/CEA table math, measured), I3 (closure requirements of record), Judge/refuter (this document)
- **Pattern**: untracked ADR (validation/ advisory series); adopt-or-declare per repo survey directive (curious in search, rigorous at adoption); judge-added points labeled **[JUDGE]**
- **Status**: advisory — registrable corrections listed in §8 for R4 retro-propagation when the owning session lands them; nothing in this file is a doc-of-record by itself

## 1. The question (user's, verbatim scope)

Is the [X-THC1] C1 quintic-table closure the right SOTA choice for OUR differentiable
engine versus:
(a) direct NASA9/CEA polynomial evaluation in JAX;
(b) an ATLAS-style dense-table pipeline consuming the EXACT `dCp` column;
(c) FLINT-style interpolation (whatever FLINT turned out to be)?

## 2. Net verdicts (one screen)

| Option | Verdict |
|---|---|
| **[X-THC1] quintic C1 table closure (standing)** | **KEEP** — confirmed at requirement level; in-window it is an EXACT re-representation of the NASA fit (machine precision), so no accuracy is being traded for the S11 generality it buys |
| **(a) NASA9/CEA-direct in JAX as engine closure** | **DECLARED-NOT-ADOPTED** (fires registry falsifier `claims_registry.yaml:1137` as written; re-narrows the interface; zero measurable gain in-window) — **HYBRID(named): ADOPT as exactness ORACLE** (condition C-A), which is the role DIR-THERMOTAB itself already assigns to NASA-poly evaluation |
| **(b) ATLAS dense-table pipeline** | split: table FORMAT as source = **ENDORSED (already the S11 model of record)**; consuming `dCp` as exact Hermite node data = **DECLARED-NOT-ADOPTED — premise FALSIFIED by measurement** (dCp is a 1-K backward difference, not an analytic derivative; §4 F2). Conditional re-open behind an analyticity rejector (condition C-B) |
| **(c) FLINT-style interpolation** | **DECLARED-NOT-ADOPTED** — FLINT is not an interpolation library (thermochem lib, GPLv3); its sole interpolant is piecewise-linear C0 on a hard-coded 1-K integer grid = the S14 defect class at source level; it never consumes the dCp it loads |

## 3. Judge verification protocol (what was re-checked, not taken on trust)

1. **Measured** `GENO/CASES/defnoz/INPUT/thermo.dat` (5000 rows) with an independent scan
   (scratchpad script, method restated in §4 F2 so it is one-liner reproducible).
2. **Read** `docs/claims_registry.yaml:1127-1138` (DIR-THERMOTAB + falsifier),
   `docs/rde_nozzle_MASTER.md:1349-1356` (M0 pin text),
   `docs/rde_nozzle_brick2_kickoff.md:79-85, 105-169, 312-323, 494-513`
   (RK-G knot discharge, quintic spec, SciPy survey rejection, two-track P3 numbers),
   `validation/thermotab_c1_jax.py:1-120` (class, FD order, invariants, rejectors),
   `validation/a1_ideal_march_jax.py:138-149, 218-269` (window, nasa_funcs twin),
   `validation/AUDIT_agnostic_2026-08-07.md:386-398` (box-edge silent clamp, open),
   `GENO/lib/FLINT/src/lib/Lib_ThermoTransport.f90:516-544` (linear interpolant),
   `GENO/CASES/defnoz/input.ini` (backend = 0).
3. **Grep** `dcpi` over all of GENO/: loaded at `Load_ThermoTransport.f90:72,78,84`,
   otherwise only test `deallocate` lines — never consumed. Confirms I1 V3 / I2 V5 / I3 §3.3.

## 4. Adjudicated facts of record

- **F1 (window)**: engine table = 8192 points on [1050, 3900] K
  (`a1_ideal_march_jax.py:142-143`); all NASA-7 species share the single breakpoint
  1000 K (asserted at `a1_ideal_march_jax.py:218-219`) => **no fit joint inside the
  working window** (this is a hypothesis to declare, not a law — condition C-C).
- **F2 (the decisive measurement — dCp is NOT an analytic derivative)**: over all 4999
  intervals of the defnoz ATLAS table, max |dCp(T_i) − (Cp(T_i) − Cp(T_{i−1}))| =
  1.0e-6 = the print precision (6 decimals). An analytic derivative column would sit
  ~cp''/2 ≈ 3.4e-5…6.4e-5 away from the backward difference (typical measured row-to-row
  |ΔdCp| = 6.75e-5 median above 1100 K, 1.28e-4 median 300-900 K) — i.e. 30-60x print
  precision — and it does not, anywhere. Forward-diff and central-diff hypotheses fail
  outright (max dev 0.42 / 0.21). First nonzero dCp at T=201 K with
  dCp(201) = 0.424474 = Cp(201) − Cp(200) exactly. **The ATLAS `dCp` column is the 1-K
  backward difference of the Cp column: first-order accurate, error ~cp''·ΔT/2 ≈
  3-7e-5 J/kg/K² (~1.5e-4 relative).** I2 V1 UPHELD; I1 V8 premise and I3 "Finding A"
  CORRECTED. (Provenance honesty: the ATLAS source on the cluster was unreachable to
  all participants; this classification is measured from the artifact, which is the
  thing the engine would consume.)
- **F3 (values ARE analytic)**: h(2997) − h(2996) − trapezoid(Cp) = +5.50e-6, matching
  the exact-integral correction −cp''·ΔT³/12; clamp rows are thermodynamically
  consistent (h(2)−h(1) = cp exactly; s(2)−s(1) = cp·ln 2 to 5e-7). I2 V2 CONFIRMED:
  Cp/H/S columns are analytic evaluations; only the derivative column is FD.
- **F4 (genuine 1000 K kink in the data)**: dCp jumps 0.447473 -> 0.440447 across
  1000 -> 1001 K = −7.026e-3 (−1.57% relative), vs smooth step −1.41e-4 (50x) =>
  genuine cp' discontinuity at the NASA breakpoint while Cp is continuous. This is the
  NASA/CEA fitting contract (value continuity constrained, derivative continuity never).
  I2 V3 CONFIRMED. Consequence: even "exact polynomial evaluation" is only
  C1-in-h / C0-in-cp globally.
- **F5 (in-window exactness of [X-THC1])**: inside one NASA-7 branch cp is a true
  quartic and h a true quintic; the two-point quintic Hermite (6 dof) with node data
  (h, cp, cp'-by-4th-order-FD) reproduces h IDENTICALLY because the FD error term
  ∝ cp⁽⁵⁾ ≡ 0. The closure over [1050, 3900] K is an exact re-representation of the
  fit with cp ≡ dh/dT held structurally (machine-verified invariant,
  `thermotab_c1_jax.py:18-19,37-40`). I2 §4 CONFIRMED, with one **[JUDGE]** precision:
  the two edge nodes use 2nd-order one-sided FD (`thermotab_c1_jax.py:97-100`), exact
  only to degree 2, leaving ~1e-7 relative cp' deviation at the two outermost nodes —
  beneath every budget (physical fit floor ~1e-4), noted for honesty, not a defect.
- **F6 (FLINT identity and class)**: FLINT = "Fortran Library for INtegrated
  Thermochemistry" (Marco Grossi, GPLv3, CEA lineage) — not an interpolation library.
  Sole interpolant: `f_tabT_expr` linear blend on `idint(T)` 1-K integer grid
  (`Lib_ThermoTransport.f90:516-542`, judge-read); cp/h/s interpolated independently;
  no derivative API; `dcpi_tab` loaded and never consumed (§3.3). Delivered class on
  the 1-K ATLAS grid: values ~1e-8 relative, cp-vs-dh/dT consistency ~1.5e-4, state
  Jacobians jump at every integer kelvin — the S14 defect class, verbatim, at
  production-pattern level. I1 V1-V5 / I3 §3 CONFIRMED.
- **F7 (registry + directive text)**: DIR-THERMOTAB (`claims_registry.yaml:1127-1138`,
  M0:1349-1356): "JAX thermo backends READ TABLES… Cantera is the SOLE PRODUCTION
  table generator; **the GENO NASA-poly generator is confined to declared cross-code
  oracle instances**"; falsifier (line 1137): "closed-form or non-tabulated thermo
  found in a solver step of any A1+ engine module (audit grep)". A NASA-direct engine
  closure fires this as written; a NASA-direct declared ORACLE is inside the directive.
- **F8 (S11 confirmed at ARTIFACT level, not just by directive)**: the ATLAS chain
  exports one "CEA-mixture" pseudo-species (MW 22.854601) as a dense mass table with
  NO polynomial coefficients anywhere local; FLINT's own embedded CEA solver consumes
  the same tables; GENO's production backend is the table one; an equilibrium-path
  h(T) is not polynomial in T at all. Only tables cross the interface. I1 V6 / I2 V4
  CONFIRMED.
- **F9 (context facts)**: `defnoz` (the S23/S24 DEF regression case) runs `backend = 0`
  (judge-read `input.ini:11`) — the DEF-branch A4 identity was measured on the NASA
  backend (footnote for F1b instrumentation). Two-track gate of record: quintic
  primary vs 'nasa' linear twin, max|u_c1 − u_lin| = 1.0e-07 vs the 5.7e-01 Richardson
  band (kickoff §5bis P3, judge-read). Cost: I3's microbenchmark (quintic 4.7x/eval,
  ~70% of a cell-trip's flops, but ~10x T2a headroom and latency-bound scan) is a
  DECLARED NON-RECORD scratchpad estimate — carried as such; the 343x S17->S18 speedup
  came from dispatch/jit with the closure unchanged (committed record).

## 5. Dispute ledger (no manufactured unanimity)

| # | Dispute | Positions | Judge adjudication |
|---|---|---|---|
| D1 | Is ATLAS `dCp` the exact analytic Cp derivative? | I1 V8: yes ("EXACT"); I3 Finding A: yes ("the gift"); I2 V1: no — backward difference (measured) | **I2 UPHELD by independent re-measurement (F2). I1+I3 corrected of record.** The panel majority was wrong on the decisive fact; the measurement, not the vote, decides |
| D2 | Where does dCp become nonzero? | I1: "~300 K"; I2: clamp ends at 200 K | I2 upheld: first nonzero at T=201 K (F2). Minor I1 error |
| D3 | In-branch exactness of the quintic re-representation | I2: exact (machine); not contested | Upheld with the **[JUDGE]** edge-node precision (F5) |
| D4 | Everything else load-bearing (FLINT class, dcpi dead, registry text, window, kink at 1000 K, defnoz backend) | I1/I2/I3 concordant | All CONFIRMED by direct reads/greps/measurement (§3, §4) |

## 6. Per-alternative adjudication

### Standing choice — [X-THC1] quintic C1 table closure: **KEEP**

- **What it buys**: (i) structural cp ≡ dh/dT at roundoff (machine-verified, rejector-
  gated) — the S14 defect eliminated at CLASS level, per-generator; (ii) C1 cp => C1
  coefficient fields (c, gamma, M) => continuous cell Jacobians and custom_vjp
  transposes (C-D25U machinery), table knots invisible to RK-G (kink monitors
  discharged by regularity, kickoff §1 P3); (iii) the c4 G(T) > 0 audit exists only in
  this class (needs cp'); (iv) S11 interface generality: same closure for
  Cantera/CEA/ATLAS/equilibrium tables — swap data, not code; (v) in-window EXACTNESS
  w.r.t. the generating fit (F5): the generality is currently FREE of accuracy cost.
- **What it costs**: ~4.7x per closure eval (non-record estimate) — measured
  second-order to the march (10x T2a headroom; scan latency-bound); ~40-line evaluator
  + invariant/rejector machinery (already built, PASS 14/14 of record); a genuine data
  kink would be mollified over ~4ΔT instead of exposed raw (adjudicated not-a-defect,
  §7 A3, provided C-C census runs).
- **SOTA status**: on the surveyed ladder (linear C0 < PCHIP/cubic-Hermite C1-h/C0-cp
  < cubic spline < quintic Hermite (f,f',f'') ≈ NASA-direct-in-branch < constrained
  TTSE-style tabulations), [X-THC1] sits at the top of what the requirement set (R1-R8,
  I3 §5) admits; the open-library survey was applied at design time and SciPy's
  offerings rejected with declared reasons (kickoff:312-323). No investigator produced
  a library or class that dominates it under R1-R8.

### (a) Direct NASA9/CEA polynomial evaluation in JAX — **DECLARED-NOT-ADOPTED as closure; ADOPT as named exactness oracle (HYBRID, condition C-A)**

- **Buys**: exact fit values (already had in-window to machine precision — F5); ~50
  lines; no table build; bit-fidelity to GENO backend 0 (already owned by `nasa_funcs`,
  `a1_ideal_march_jax.py:225-250`, the exact backend-0 twin used as table
  generator/oracle).
- **Costs**: fires the DIR-THERMOTAB falsifier as written (F7) — adopting it is a
  user-owned directive amendment, not an engineering choice; re-narrows the engine
  interface to frozen thermally-perfect fit-gases against what the toolchain actually
  emits (F8); carries the genuine 1.6% cp' kink at 1000 K raw into solver Jacobians the
  moment any case leaves the current lucky box (F4); re-opens certified machinery
  ([X-A1IM] regression, C5 dual-route band, X-SCANM equivalence) for zero measurable
  in-window gain.
- **Verdict**: DECLARED-NOT-ADOPTED as engine closure. **ADOPTED in its
  directive-sanctioned role**: a declared cross-code exactness ORACLE asserting
  |state_q_c1 − state_q_poly| ≤ derived machine floor over the window — the sharpest
  cheap rejector for [X-THC1] (I2's recommendation, judge-endorsed; C-A below). No
  directive change needed for the oracle (F7 wording).

### (b) ATLAS-style dense-table pipeline consuming the "EXACT dCp column" — **premise FALSIFIED; format ENDORSED, dCp-as-nodes DECLARED-NOT-ADOPTED (conditional C-B)**

- **Buys (claimed)**: generator-exact node derivatives, drop the FD step and its
  verification burden, zero new I/O.
- **What measurement says (F2)**: `dCp` is the 1-K backward difference — first-order,
  ~1.5e-4 relative error on cp'. [X-THC1]'s 4th-order FD on the dense Cp column is
  in-branch EXACT (F5). **Consuming dCp as node data would DEGRADE cp' fidelity by
  ~3-4 orders and destroy the in-window exactness property.** The "fidelity hole"
  runs in the opposite direction from the briefing premise.
- **Also carries (Finding B, confirmed)**: the full ATLAS box [1, 5000] K contains two
  genuine data joints (clamp edge at 200/201 K; 1.6% cp' jump at 1000 K) — any closure
  built on the full box must census and declare them (C-C).
- **Verdict**: the ATLAS dense-table FORMAT as a table SOURCE is ENDORSED and is
  literally the S11 model of record (F8) — nothing to adopt, it is the standing
  interface. The dCp-ingest lever is DECLARED-NOT-ADOPTED on the false-premise ground,
  and survives only in corrected conditional form (C-B): generator-provided derivatives
  may enter as Hermite node data ONLY behind an analyticity rejector; today's legitimate
  instance is Cantera exporting analytic cp' from NasaPoly2 coefficients, not ATLAS's
  current column (usable as a QA cross-check at its measured first-order accuracy).

### (c) FLINT-style interpolation — **DECLARED-NOT-ADOPTED**

- **Identity correction of record**: FLINT is a thermochemistry library (tables +
  transport + kinetics + a ported CEA equilibrium solver), author Marco Grossi, GPLv3;
  the panel-question framing of FLINT as an interpolation library with
  orders/continuity options is factually void — it has exactly one interpolant:
  piecewise-linear C0 on a hard-coded 1-K integer grid (F6).
- **Buys**: O(1) integer-index lookup (legitimate industrial brute-force pattern for
  value-only forward CFD — errors ~1e-8 in values); GENO backend-1 fidelity (not
  needed: the twin bit-contract runs on backend 0 via the 'nasa' linear track, and
  defnoz itself runs backend 0 — F9).
- **Costs**: cp ≠ dh/dT ~1.5e-4 between knots; state Jacobians jump at EVERY integer
  kelvin; no derivative exists for the G-audit — the S14 measured defect class at
  source level. Adopting its evaluation semantics would machine-verifiably reintroduce
  the finding [X-THC1] exists to fix. GENO can afford it (never differentiates the
  march); we cannot — that asymmetry is the whole story.
- **Flags carried (no action in this repo)**: FLINT is GPLv3 (GENO links it — a
  distribution/licensing decision point owned by the user, GENO-side); latent T∈[0,1) K
  garbage row (h(0):=0 vs h(1)=−9.17e6 — unreachable in practice, GENO-side);
  backend-0 mole-fraction vs backend-1 mass-fraction asymmetry (documented in GENO).

## 7. Refuter attacks on the standing choice (duty discharged)

- **A1 — "S11 is not load-bearing under the frozen thermally-perfect pin; drop it and
  go NASA-direct."** REJECTED, with the true kernel conceded: under the pin and on the
  current box, NASA-direct satisfies the local math (R1-R4) — all three investigators
  state this honestly (I1 V7, I2 §5, I3 §4 honest statement). Rejection grounds:
  (i) S11 is confirmed at ARTIFACT level (F8) — only tables cross the real toolchain's
  interface, so a polynomial interface would make the engine LESS faithful to what
  GENO/ATLAS actually do, not more; (ii) the registry falsifier is as-written (F7) —
  the change would be a user-owned directive amendment; (iii) it buys nothing
  measurable: in-window the closure IS the fit at machine precision (F5) and closure
  cost is off the critical path (F9); (iv) the 2026-08-11 scope pin narrows PHYSICS,
  not the interface — under S11 the pin lifts by swapping data, under NASA-direct by
  rewriting code. **Registrable residue of the attack**: the no-joint-in-window fact
  is a HYPOTHESIS, to be declared wherever an isentrope could approach 1000 K (C-C).
- **A2 — "The FD-reconstructed cp' is a fidelity hole given ATLAS exports dCp
  exactly."** FALSIFIED BY MEASUREMENT (F2): the export is first-order; the FD
  reconstruction is in-branch exact (F5). The fidelity ordering is the reverse of the
  attack's premise. This also retires I1's V8 lever and I3's Finding A in their stated
  form (C-B is the corrected survivor).
- **A3 [JUDGE] — "The quintic closure mollifies genuine data kinks (1.6% cp' at
  1000 K) instead of exposing them — smoothing the truth."** NOT-A-DEFECT: the kink is
  a FIT artifact (NASA/CEA constrains value continuity only — F4), not physics; the
  closure declares-and-mollifies over ~4ΔT with the per-table probe audit as the
  instrument, while a direct backend would pass the kink raw and un-audited into
  Jacobians. Moot on the current box; C-C keeps it honest off the box.
- **A4 [JUDGE] — "Quintic + 8192-point table is over-engineering (anti-overengineering
  pin)."** REJECTED: every smoothness order traces to a named requirement (cubic fails
  C1-cp — kickoff:111-128); the evaluator is ~40 lines; the surveyed open libraries
  were rejected for named inadequacies, not taste; cost is measured second-order. No
  gratuitous rigor found.

## 8. Named conditions, owners, registrables

- **C-A (adopt, cheap)**: wire the existing `nasa_funcs` analytic route as a declared
  exactness ORACLE/rejector for [X-THC1]: assert max over the window of
  |state_q_c1 − state_q_poly| ≤ derived machine floor (in-branch identity, F5), plus a
  negative control (perturbed node must be detected). Owner: F2 engine window / next
  [X-THC1] touch. Within DIR-THERMOTAB's oracle role — no directive change.
- **C-B (conditional, gated)**: generator-derivative ingest into Hermite nodes is
  permitted ONLY behind an ANALYTICITY REJECTOR: if a table's derivative column equals
  backward-diff(Cp) at print precision (the F2 fingerprint), classify it FD-export and
  refuse node-data use (QA cross-check only). Legitimate near-term instance: Cantera
  analytic cp' from NasaPoly2. Owner: whoever lands the first ATLAS-table ingest into
  the JAX engine (F1b/F2 window); trigger: first ATLAS table consumed.
- **C-C (hypothesis + census)**: declare "no fit joint inside the state box" as a
  hypothesis of the closure certificate; at every table ingest run the joint census
  (clamp edges, range breakpoints — the defnoz instances are 200/201 K and 1000 K
  @1.6% cp') with the existing [X-THC1] probe machinery; a box crossing a joint must
  state the mollification (~4ΔT) explicitly in the certificate. Owner: same ingest
  path; already instrumentable.
- **C-D (pre-existing open residual, re-affirmed)**: any closure work lands the traced
  box-exit rejector for the silent clamp at T_TAB_LO/HI with dT/dq = 0
  (`AUDIT_agnostic_2026-08-07.md:388-398`) rather than reproducing the silence. Owner:
  F2 (already a declared residual; restated here because two options above touch the
  same code path).
- **Registrable corrections of record (R4 duty for the owning session, when landed)**:
  (1) "ATLAS exports the exact Cp derivative" is FALSE — dCp = 1-K backward difference
  (measured, F2); any doc/memory line implying otherwise must not propagate;
  (2) FLINT identity (thermochem lib, linear-only, dCp dead weight) — F6;
  (3) the 1000 K cp' jump is genuine and quantified (−1.57%) — F4;
  (4) defnoz DEF regression runs backend 0 — F9 footnote for F1b.
- **Flag ledger (no action this repo)**: FLINT GPLv3 (user-owned, GENO distribution
  question); FLINT T<1 K garbage row (GENO-side latent trap).

## 9. Honest limits

- ATLAS source code unreachable to all participants (cluster-side); the dCp
  classification is measured from the exported artifact — which is exactly the object
  any consumer would ingest — but the generator's internals remain inferred.
- I3's closure-cost microbenchmark is a declared NON-RECORD scratchpad estimate; only
  the committed T2a/two-track numbers (F9) carry record weight.
- This advisory adjudicates the CLOSURE question only; it does not touch the twin
  bit-contract (R6: 'nasa' linear track untouched) nor any GENO-side code.
