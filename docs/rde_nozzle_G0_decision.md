# G0 DECISION — differentiable per-phase engine stack (gate G0 of D6)

Status: DECISION OF RECORD (2026-07-17, [F2/G0], session S10). Gate G0
of `rde_nozzle_development_plan.md` (D6 §5). This document records the
formal G0 stack decision on the D6 criteria — gradient fidelity, loop
speed, and (user decision of record S5) GENO interop — with the GENO
cross-code criterion NOW EXERCISED (previously the named residual). The
outcome opens Phase A1 (differentiable per-phase engine).

Registry: this decision is indexed as `DIR-G0`; the new cross-code
carrier is `X-GENOXC` (claims_registry.yaml). Conflict rule: M0 + D1-D7
win; this is a work-layer decision (D6), not a theory statement.

------------------------------------------------------------------------------
## 1. The decision

**G0 = DECIDED. Primary stack: JAX** (custom_vjp / custom_jvp per unit
process; implicit-function rules for the Newton inner solves — never
unrolled). **Alternate: Julia + Enzyme** (declared fallback, not
benchmarked on this host — see §4). **GENO-Fortran stays the independent
verification reference** (dual-code discipline, M0 VI.7); its interop
criterion (user decision S5) is now MET, not deferred.

Consequence for the plan: gate G0 moves from INSTRUCTED to DECIDED;
Phase **A1 OPENS** (D6 §Phase-A1). The first A1 item is the item this
session already seeded: the gamma(T) backend unit process with the GENO
cross-code oracle as a standing regression (`X-GENOXC`).

------------------------------------------------------------------------------
## 2. Criteria, evidence, verdict

### (i) Gradient fidelity — JAX: PASS (executable)
- Planar spike (S5, `validation/g0_spike_jax_moc.py`, carrier X-G0):
  interior + inverse-wall unit processes as Newton-implicit systems in
  `jax.custom_vjp` with the implicit-function rule; full Jacobian vs
  central FD with DERIVED tolerance (two-step Richardson + roundoff
  floor): 52/52 entries in tolerance, Newton residuals ~1e-16, negative
  control (corrupted vjp) rejected.
- Axisym + shock twin (S8, `validation/g0_spike_axisym_shock.py`,
  carrier X-G0AX): axisymmetric source dual-route; fitted shock point on
  RH with the O3.1 dot-product identity at 3.4e-12 vs tol 1.2e-9 (P-B1
  discharged at brick level); Lax/Majda == J_k nonsingular executable.
- VERDICT: the reverse-mode adjoint through implicit unit processes is
  correct to machine precision. Fidelity is the decisive criterion and
  JAX meets it with a committed rejector.

### (ii) Loop speed — MEASURED STANDALONE (host caveat declared)
Standalone microbenchmark of the axisym interior unit process
(`make_implicit_solver(make_resid_interior_axi)`, jit, 2000 calls,
float64, this host):
- solve (primal Newton): ~322 us/call
- solve + reverse-mode gradient (custom_vjp adjoint): ~327 us/call
- **adjoint overhead ~1.5%** — the implicit-function rule delivers the
  per-unit-process gradient at the cost of the primal solve.
CAVEAT OF RECORD (S9 host lesson): absolute us figures are host- and
load-dependent and do NOT constitute a record timing; the DECISION-
RELEVANT number is the grad/solve RATIO (~1.01), which is host-invariant
and confirms the "adjoint is free" property that motivates the stack.
The A1 loop-speed at engine scale is a G0 falsifier (see §4).

### (iii) GENO interop / cross-code oracle — NOW EXERCISED: PASS
User decision of record (S5): GENO stays Fortran provided the whole
pipeline stays functional; file exchange + the O3.4 cross-code oracle
are explicit G0 criteria (dual-code M0 VI.7). Through S8 this was the
NAMED RESIDUAL of G0 ("the GENO binary is not buildable on this host;
gfortran absent; the reference x/y/u/v/p.dat exist only as checksums").
S10 CLOSED it:
- **Toolchain (declared, reversible):** GENO built in WSL Ubuntu 22.04
  (gfortran 11.4.0, CMake 3.23.3, `USE_TECIO=OFF USE_CANTERA=OFF
  USE_SUNDIALS=OFF`, LAPACK/BLAS from the host conda env `ct-env`
  libopenblas — `dgesv` is a genuine GENO dependency in `write_profile`).
  GENO is NEVER modified and NEVER committed; only the submodules needed
  for the OFF build were checked out; run outputs are gitignored (GENO
  tree stays pristine — verified `git status` clean).
- **tocnoz regenerated (T1b):** `bin/GENO` run on `CASES/tocnoz` (TOC,
  axisym CH4/O2 frozen, eps=30) exits 0; performance physically sane
  (Cd 0.9820, Cf 1.7759, Isp 338.86 s), profile 550 points monotone
  divergent, area-ratio consistent.
- **Checksum convention identified in-session (cite only what is read):**
  `reference/checksums.md5` header states "baselines are toolchain-
  dependent (-O level changes md5): regenerate with the CTest binary on
  toolchain change (N-36)". Empirically confirmed: printed-scalar / copied
  files (performance.dat, dimensions.dat, thermo.dat) md5-MATCH the s3
  gfortran-7.5.0 baseline; full-precision field dumps (x/y/u/v/p/rho/
  gamma.dat, output_fe.tec) md5-DIFFER by last-bit formatting. Same
  physics, different toolchain — NOT a regression. Hence the scientific
  cross-check must be VALUE-based, not md5.
- **Nozzle contour cross-check (design output):** the regenerated TOC
  contour `profile 30.0.dat` matches the committed reference
  `ch16_ref/profile 30.0.dat` to max |Delta| = 1e-10 (full printed
  precision, toolchain-invariant); independent TOC validation: throat
  yt=1.0 at x=0, exit eps=29.95, max wall angle 37.41 deg, monotone
  divergent. The GENO build reproduces the contour of record.
- **Flowfield cross-code oracle (T1c, carrier X-GENOXC,
  `validation/g0_geno_crosscode.py`):** OUR axisymmetric second-order
  (u,v) unit process (EOS-general: local a=sqrt(gamma p/rho), no
  gamma=const Prandtl-Meyer invariant — DIR-GAMMA / M0 VI.4bis(iii)) is
  SATISFIED by GENO's own structured-grid node values within a PER-CELL
  truncation band derived from the scheme order (|R_trap| <= 4*(|R_trap -
  R_end| + floor)); 100% of 218 clean supersonic-core triangles (M in
  [1.5,6], off-axis, feet on the characteristics) inside the band; median
  residual 2.2e-5 below median band 6.8e-5. Negative controls REJECT: a
  1%-corrupted child leaves the band (100% -> 0%); a wrong C+/C- pairing
  makes the slope residual 84x worse. VERDICT PASS.
- VERDICT: the interop criterion is MET at the level of the interior unit
  process (the A1 building block): our differentiable engine's cell map
  and GENO's Fortran MoC agree to the discretization truncation, and the
  design contour agrees to printed precision.

------------------------------------------------------------------------------
## 3. Why JAX over Julia/Enzyme (on the criteria, not preference)

- Fidelity: JAX's `custom_vjp` + implicit-function rule is exercised and
  rejector-backed here (52/52 + O3.1 machine precision). Enzyme would
  differentiate the Fortran/Julia march directly; equally valid in
  principle but UNexercised on this problem and this host.
- Speed: the adjoint-is-free property (grad/solve ~1.01) is already
  demonstrated for the JAX route; it is the property the cycle-layer
  TR-SQP needs (many gradient evaluations per outer step).
- Interop: JAX co-exists with the Fortran reference by FILE EXCHANGE
  (no in-process FFI), which the S10 cross-code oracle uses directly and
  which keeps GENO pristine — matching the S5 user decision exactly.
- Ecosystem fit: numpy/Cantera thermo backend (repo standard, gamma(T)
  tables) plugs into JAX via pure-callback / custom primitives without a
  language boundary; the A1 gamma(T) unit process (T4 brick) is a JAX
  custom primitive over the Cantera isentrope.

Julia+Enzyme remains the DECLARED ALTERNATE (D6): it is the fallback if
the A1 loop speed at engine scale regresses (§4), and an independent
third route (beyond GENO) if a differentiation cross-check is ever needed.

------------------------------------------------------------------------------
## 4. Falsifiers and residuals (honesty)

- LOOP-SPEED FALSIFIER: if the assembled A1 engine (full analysis-mode
  MoC + fitted shock + plug free boundary) shows the JAX route's
  wall-clock per optimizer step to be impractical at production mesh
  sizes, the decision flips to Julia+Enzyme (the alternate is kept warm
  for exactly this). The standalone unit-process timing does not bound the
  assembled loop — declared.
  [Dated note 2026-08-05, PAN-S14 §8 residue: 'impractical' carries no
  number here BY DESIGN of record — the quantified threshold (clean-host
  protocol) is a D6 §6 item-9 kickoff duty, pending brick-2 kickoff.]
  [Dated note 2026-08-06, S17 duty (a) EXECUTED — the falsifier is now
  QUANTIFIED and machine-rejectable (carrier X-LSG0, clean host):
  T1 = grad/solve <= 4 (cheap-gradient theorem constant; MEASURED
  3.004 on the scan engine — inside the [3,4] theory window, PASS);
  T2a = t_solve <= 4 x t_GENO at same case/resolution (measured
  39.8 s vs 4 x 0.286 s: FAIL-AS-IMPLEMENTED, root cause measured =
  per-evaluation Python re-trace over cached kernels; whole-march
  outer jit not compilable today — XLA module blowup, crash measured)
  => PRODUCTION GATE CLOSED: the named remediation (single-bucket-
  per-phase padded scans => 3 XLA modules, outer jit compilable,
  topology re-records stop generating new shapes) is BINDING before
  any production-mesh use, then T2a re-runs; T2 whole-loop bound
  armed with the measured constants for the brick-2 Verdict. FLIP
  CLAUSE adjudication: NOT triggered — the failure is dispatch-
  overhead class while the theorem-relevant T1 passes; the flip
  re-arms if T1 or post-remediation T2a fails on a clean host.]
  [Dated note 2026-08-06, S18 — REMEDIATION EXECUTED, T2a RE-RUN
  PASS, PRODUCTION GATE OPEN: the single-bucket-per-phase padded
  scans + whole-loop jit landed (make_run_scan_jit in the X-SCANM
  module; safe-where guard with a certification-verified recorded
  dummy cell; equivalence to the certified replay at 6.2e-15 =
  Newton-floor bit-level; O3.1 on the jit path 4.9e-11 = the
  NaN-leak detector, clean). Clean-host re-measurement (X-LSG0):
  t_solve 0.116 s (was 39.8 as-implemented), t_grad 0.185 s,
  grad/solve 1.593 <= 4 (T1 PASS), t_GENO 0.299 s, T2a 0.116 <=
  1.197 s PASS. The production gate CLOSED at the S17 note above is
  hereby OPEN of record; a future T2a failure on this path would be
  STRUCTURAL and triggers the flip clause directly.]
  [Dated note 2026-08-12, S25 — THE QUEUED G0/T2 REVIEW (S18 flip
  clause) CONSUMED, VERDICT OF RECORD: the S18 T2 firing was
  STRUCTURAL COST (records + curvature measurement), NOT language
  throughput — T1 1.593 and T2a 0.116 s both PASS with margin, so
  the flip clause does NOT trigger and the G0 language decision
  (JAX primary / Julia-Enzyme alternate kept warm) STANDS. LEDGER
  TRUTH REPAIR absorbed (S-SPEED advisory §1.3/§7.1, of record):
  the S18 "67 evals" line was untruthful — true compiled-eval count
  ~102-108 (g_np and the 18 preconditioning evals uncounted; the
  n_eval += n+1 line double-counted Hessian evals) AND the T2 lhs
  priced each eval at t_solve + t_grad while reality is ONE
  value_and_grad per execution; the [X-TOCV] T2 line is REPRICED of
  record (lhs = n_eval_actual x t_value_and_grad, legacy figure
  printed alongside; n_eval now counts actual compiled executions —
  the S25 M2 truth repair). The structural cost line is REPAIRED,
  not just re-adjudicated, by the S25 M-chain (clean-host
  [X-SPDB] baselines + gates of record): defnoz record 100.84 s ->
  25.49 s (derived-K fused C1 closure M3 x fused-dispatch M5a,
  bitwise-vs-legacy gated), duplicated fun/jac compiled executions
  DELETED (M2 memo, bit-transparent, counter-reconciled), duplicate
  segment-boundary records DELETED (M1 memo with failed-record
  replay), per-segment engine recompile DELETED (M4 plan-as-args
  engine cache, wall bitwise vs constants build). Julia/Enzyme
  remains NOT benchmarked on this host (unchanged honesty row);
  Python 3.14/3.14t stays DECLARE-NOT-ADOPT (advisory N7). The
  remaining record-cost tail (true-L5 compiled record M5c + vmapped
  Hessian M6) is a NAMED S25-bis item, not a G0 matter.]
- JULIA/ENZYME NOT BENCHMARKED on this host: the "JAX over Julia" verdict
  rests on JAX being EXERCISED and Julia not, plus interop/ecosystem fit —
  not on a head-to-head speed number. Stated plainly.
- CROSS-CODE SCOPE (stated plainly to prevent over-reading): X-GENOXC
  certifies agreement at the INTERIOR UNIT PROCESS (what GENO calls an
  interior process) in the clean supersonic core — the differentiable
  BUILDING BLOCK. It is NOT the profile-generation machinery. In
  particular this session did NOT generate any nozzle contour with the
  JAX route: the JAX artifacts (X-G0/X-G0AX) are unit-process ADJOINT
  fidelity checks, and X-GENOXC is a unit-process cross-code check
  consuming GENO's field. There is no assembled JAX MoC march, no
  JAX-produced wall, no JAX TOC contour yet. The oracle also does not
  cover the wall/corner unit processes, the fitted shock cell, or the
  near-axis / near-sonic regions (excluded as singular).
- PROFILE-GENERATION MACHINERY = PHASE A1 (not this session). Assembling
  the validated unit processes into a full analysis-mode MoC march (IVL
  -> interior/wall/corner/shock unit processes -> flowfield + wall
  streamline), and the reverse-AD of that march (= discrete adjoint,
  Lemma B), is the A1 engine. The NOZZLE TYPE is imposed at the
  FORMULATION level, not in the solver kernel: an IDEAL MoC nozzle
  expanded to a target exit Mach is a DIRECT march (inverse-wall unit
  process, wall = bounding streamline, no thrust optimality — GENO
  nozzle_type 0); a TOC (Rao thrust-optimized) contour is the CONSTRAINED
  optimization max thrust s.t. {eps, L, lip} whose optimality condition
  is the Rao control-surface transversality (the weighted (**') endpoint
  condition + corner CSTR_PA/PB = the adjoint closure surface of P-2
  Lemma A), driven by the differentiable dJ/dSigma gradient through
  TR-SQP (GENO nozzle_type 2, imposed there by the Mrao/eps outer loop;
  here by the objective+constraint set and the transversality condition).
  Truncated plug / free-boundary types add the length cap / plug closure
  (T4). The theory for all of this is already of record (M0 VI.1-VI.7,
  Lemma A/(**'), T4); A1 EXECUTES it.
- GAMMA: the oracle and the engine are EOS-general by construction; GENO's
  own reference is gamma(T) frozen Fortran MoC. The perfect-gas closed
  forms live only in the declared oracle spikes (X-G0/X-G0AX), never in
  X-GENOXC's primary path (DIR-GAMMA satisfied).

------------------------------------------------------------------------------
## 5. Plan impact (D6)

- Gate G0: INSTRUCTED -> DECIDED (JAX primary, Julia/Enzyme alternate,
  GENO dual-code reference; interop criterion met).
- Phase A1: OPENS. First brick = gamma(T) backend unit process with
  X-GENOXC as standing cross-code regression; then fitted single
  transversal sheet, plug off-design free boundary (D6 Phase-A1 content).
- Gates downstream unchanged: G1 (oracle gate, absolute) still governs
  the first science; G5 still blocks submissions only.
- User ratification (D6 §pending): G0 is decided within the D6 criteria;
  if the user judges a trade-off outside those criteria (e.g. a strategic
  preference for a single-language Julia pipeline), that is a standing
  pending-decision item — the technical criteria point to JAX.
