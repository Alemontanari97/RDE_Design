# DOF & input audit — every model, every input, its provenance

Purpose: make the inputs of every implemented model explicit, so that any
"magic parameter" has nowhere to hide. Every quantity that enters any model
is classified as exactly one of:

| class | meaning |
|---|---|
| `COMPUTED` | derived live from equilibrium chemistry / the model's own equations |
| `SPEC` | a design/problem specification (declared given, not tunable physics) |
| `DOF` | a free variable the code actually optimizes |
| `ELIMINATED` | a variable removed by an exact constraint or identity (not free, not assumed) |
| `MODEL-CONST` | a constant that DEFINES the cited model (provenance = the paper's own derivation/fit; changing it means implementing a different model) |
| `EMPIRICAL` | a literature correlation, carried with its declared uncertainty band |
| `NUMERIC` | solver/grid knob with a documented convergence or cross-check |

Audit rule (enforced): nothing a model can compute is inherited from a paper
table. Paper tables are used ONLY as validation targets. After Step 7
(`optfull`), this includes the Table-1 optimum equivalence ratios, which the
code now rediscovers independently.

## 1. Stechmann-Heister-Harroun performance model
(`src/thrust/st_core.py`, `src/thrust/stechmann_nozzle.py`; JSR 56(3) 2019)

| input | class | how it is given |
|---|---|---|
| propellant, mechanism | SPEC | `PROPS` registry; RP-1 = gaseous n-dodecane surrogate (declared caveat) |
| Pcp (feed class, 20/200 atm) | SPEC | Table-1 configuration being validated |
| Pa (1 atm / vacuum) | SPEC | per row; default from `constants.P_ATM` |
| Ti = 200 K | SPEC | paper inlet condition; functions take Ti as an argument |
| eps_max = 15/150 (vacuum rows) | SPEC | geometric cap; no finite optimum exists at Pa = 0 |
| phi (equivalence ratio) | DOF | `optfull`: outer optimization on the 0.01 lattice, certified local max; paper phi* used only as target (rediscovered 18/18) |
| eps (area ratio) | DOF | inner optimization, closed form: bell NPR(eps*) = mean_t(Pc)/Pa (exact stationarity), spike knee NPR(eps*) = Pmax/Pa; certified by sweep + golden section |
| gamma | COMPUTED | equilibrium isentropic exponent rho*a_eq^2/P at chamber/CJ state (never an assumed number), then frozen (paper assumption 2) |
| T0, M, R, c* | COMPUTED | HP equilibrium (CP side) / equilibrium CJ point (det side) |
| P_CJ, PR | COMPUTED | equilibrium Hugoniot minimum-wave-speed solve |
| P_init | ELIMINATED | feed-equivalence fixed point (Sec. III matching), closed form via I(k) |
| tc (blowdown time) | ELIMINATED | cancels exactly in the mass-weighted Isp (quadrature in xi = t/tc) |
| Pe(t) | ELIMINATED | slaved to NPR(eps) (bell) or Pa (adapted spike) |
| exponential blowdown shape | MODEL-CONST | paper Eqs. 13-14; endpoints fixed by Pc(0)=P_CJ, Pc(tc)=P_init |
| no-flow-separation, choking kept (assumption 3) | MODEL-CONST | paper choices replicated; choke margin reported per case |
| NQ = 4001; XTOL; phi seed grids; secant/Hugoniot tolerances | NUMERIC | quadrature checked vs 16001 (<1e-5 s); golden vs analytic eps (<1e-3); phi seed grids auto-extend (argmax never accepted on an edge) |

Fitted constants: NONE.

## 2. Stechmann eps=1 / ideal-plug variant (`sk_models.stech_calc`)

| input | class | how it is given |
|---|---|---|
| gamma_e, R, PR, P_init, T_CJ | COMPUTED | from the canonical CJ record (`cj_core`) |
| fill P1 = 1 atm, T1 = 300 K | SPEC | Shepherd-Kasahara lab convention (constants.py, deliberate; the mission chain uses the matched P_init instead) |
| eps = 1 (sonic exit) / unbounded plug | SPEC | the two bounding nozzle closures of the thrust suite (no eps DOF by design) |
| n = 20001 | NUMERIC | quadrature grid |

Fitted constants: NONE.

## 3. Shepherd-Kasahara pressure-history model [PH]
(`sk_models.ph_calc`; GALCIT FM2017.001 Sec. 3)

| input | class | how it is given |
|---|---|---|
| CJ record (P_CJ, rho1, U_CJ, gamma_e, Yf) | COMPUTED | canonical CJ chain |
| K = 1.02 (fuel-air) / 1.54 (fuel-O2) | MODEL-CONST | K = 1/alpha from S&K's own tail fit psi(xi) = exp(-alpha*xi) (Eqs. 14, 16); part of the cited closure, not tuned here |
| u_c = 300 m/s | MODEL-CONST | S&K 2013 inlet axial speed (term II, Eq. 7) |
| Pa | SPEC | 1 atm (SK Table-1 convention) |

K and u_c are the only paper-sourced constants in the whole thrust suite.
They are definitional for the cited model; the repo does not treat them as
physics it can compute. Their independent first-principles check is model
[AX] below (no fitted constants), asserted by `tests/test_axial_bound.py`
(TOL 2e-3) — i.e. the fitted closure is VALIDATED against a fit-free model,
not trusted blindly.

## 4. Shepherd-Kasahara axial-flow model [AX] (`sk_models.axial_calc`)

| input | class | how it is given |
|---|---|---|
| CJ state (h1, s2, P2) | COMPUTED | canonical CJ chain |
| w = sqrt(2(h1-h)), T/Mdot at sonic point | COMPUTED | equilibrium isentrope march (Eqs. 44-45) |
| chem = 'eq' / 'frozen' | SPEC | declared upper/lower recombination bounds (Bray switch out of scope, documented) |
| nstep = 90, pfloor = 0.012, bisection 1e-6 | NUMERIC | sonic point re-solved by exact bisection, not grid interpolation |

Fitted constants: NONE.

## 5. Canonical CJ chain (`src/common/cj_core.py`)

Inputs: composition X, p1, T1, mechanism — all SPEC/COMPUTED. One canonical
path (CJspeed -> PostShock_eq -> soundspeed_eq); identity across callers
asserted at 1e-9 (test i); independent verbatim solvers within 2e-3.
Fitted constants: NONE.

## 6. Cycle suite (`src/cycles`: FJ/ZND/Brayton, q-mapping)

| input | class | how it is given |
|---|---|---|
| P1 = 1 bar, T1 = 300 K | SPEC | Wintenberger-Shepherd validation convention (constants.py) |
| q~, M_CJ | COMPUTED | from CJ states; round-trip inversion exact to 1e-6 (test iv) |
| gamma = 1.4, q~t = 0.8, M0 = 5 | SPEC | ONLY in the textbook stagnation-Hugoniot benchmark case (function defaults of `stagnation_benchmark`), not model constants |

Fitted constants: NONE.

## 7. Design examples (`examples/`)

| input | class | how it is given |
|---|---|---|
| mdot, Rbar, gap, L, Pcp, thrust target | SPEC | the design brief of each example |
| Wolanski wave number W = 2 Vdot/(l_cr h u_D) | COMPUTED | derived formula (PCI 34, 2013, Eqs. 4-5), no fit |
| l_cr, fill bands ((12+/-5) lambda class) | EMPIRICAL | cell-size-based literature correlations, carried WITH their uncertainty bands (never a bare point value) |
| P_init (mission chain) | ELIMINATED | output of the matched cycle (no 1-atm assumption; see commit 6d3e4a2) |

## Hardening round 2026-07-15 (multi-agent audit -> 41 findings, all closed)

A 10-model line-by-line audit (formula re-derivation + input classification +
magic-parameter hunt; adversarial verification) found 0 formula mismatches
and 41 findings, every one closed in-repo:

- Stechmann Step 7: certificate made STRICT; unimodality now an EXECUTABLE
  scan (n_local_max, grid persisted, PASS gate + test T3); nozzle/Pa input
  guards; `matched` raises on non-convergence; CJ sonicity asserted at every
  det_state (TOL ladder).
- tables.py: ALL 8 V&V verdicts now computed from data (check 2 was a frozen
  PASS string); 3c PASS* carve-out verifies the failure IS the documented
  anomaly; Pm/P2 band tied to the SK quote (0.215-0.255); empty-set guards;
  exit code reflects FAIL. Discovery A6: SK Table-1 fill is 0.15 MPa, not
  1.5 atm - our densities rescaled to 0.15 MPa reproduce all four quoted
  rho_c to 3 s.f. (offset +1.32%, cancels in U_CJ/gamma/Isp ratios).
- CJ coherence: U_CJ of the verbatim Stechmann Hugoniot solver now asserted
  vs the canonical chain (was computed and discarded); sonic residual gated
  at 4/4 computed CJ points; actionable single-species dispatch error.
- q-formalism: constants imported from constants.py (drift-proof); mdev
  consistency asserted at 1e-6; the gamma=1.2 family claim computed and
  asserted (<5%, live 3.8%); 700-K sensible-shift sign convention fixed;
  FAM half-width documented as half the label spacing.
- cycles: the tautological Brayton A59 row is labelled [algebraic identity]
  and two NEW independent cross-checks exercise the (previously dead)
  A21/A40 quadratics against the closed-form CJ Mach (tangency M2^2 -> 1,
  no real root below M_CJ); vN band aligned to the documented 1.6-2.0;
  pic < 1 rejected; plot-stage KeyErrors made actionable. Compression
  FROZEN / expansion EQUILIBRIUM verified as the correct hypothesis pair
  (metastable cold reactants; papers' B1 state-function definition).
- detonation suite: CJ minimiser validated (sentinel + bracket-edge);
  Hugoniot bracket sign pre-check; vN fixed point raises on
  non-convergence; ZND completeness asserted (exo > 0, thermicity tail
  < 1% of peak; shipped worst case 0.21%).
- axial/PH: rebuilt-entropy cross-assert vs the CJ record (+ phi guard);
  flatness-window literals named, documented and recorded in the output;
  edge guards (pfloor, empty supersonic window, Pa <= 0); actionable
  stage errors; aeq fallback no longer constructs from a phase name.
- examples: 10 kN fill hydraulics/detonability moved to the MISSION fill
  P_init = 2.40 atm with the cell size carried as a two-route band
  (DB 2.5+-0.4 | 29*Delta_i = 5.77 mm @ 1 atm, ~1/P): W is
  pressure-invariant (3.14, band 0.96-6.41 -> 1-6 heads, central ~3);
  throatless/nozzled closures computed LIVE and asserted in both examples
  (G* = 428, R_bar = 22.6 mm / 142.2 mm, A_t = 4.30 cm2); gap >= 2.4*lambda
  and D_bar >= 28*lambda asserted; both examples added to the test suite.

Deliberately NOT changed (declared): np.trapz in sk_models (numpy pinned
2.2.6 by repo policy; numpy >= 2.3 dies at st_core import first anyway).
A6 UPDATE 2026-07-16: the SKREP cases were re-blessed at the true SK fill
0.15 MPa / 255 K; check 3a now compares rho_c DIRECTLY and the former
+1.32% offset on P-linked quantities is gone.

## The invariant is now ENFORCED (2026-07-16)

This audit is no longer a snapshot: `tests/test_numeric_lint.py` (suite
group vii) scans every numeric literal in src/**/*.py via AST and FAILS
unless the literal is (a) trivially structural (|int| <= 12, algebra
fractions, percent/kilo scalers), (b) classified in
`validation/numeric_allowlist.json` with a class from THIS taxonomy and a
provenance note, or (c) inside a data-block/function exempted AS A
CLASSIFIED UNIT (paper tables, the mixture registry, literature-anchor
rows, plot code). Malformed entries (missing class/note) also fail. A new
number cannot enter the physics without arriving together with its class
and provenance; the failure message prints the exact JSON snippet to add.
Mutation-tested: an injected unlisted literal is caught with an actionable
message.

## Verdict

- The only paper-sourced constants anywhere in the implemented physics are
  the PH-model K (1.02/1.54) and u_c (300 m/s) — both MODEL-CONST of the
  cited S&K closure, both independently cross-validated against the fit-free
  axial model inside this repo.
- Every remaining number is computed, a declared specification, an
  eliminated variable, a banded literature correlation, or a numeric knob
  with a convergence/cross check.
- As of Step 7 (`optfull`), no optimum is inherited: the joint (phi, eps)
  optimization rediscovers all 18 Table-1 rows (phi* to the 0.01 lattice,
  26/36 exactly; superiority Isp(phi*_model) >= Isp(phi_paper) asserted
  per row). Verdict line in `data/st_opt_validation.md`:
  "18/18 rows FULL-OPT PASS."
