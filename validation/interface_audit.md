> **STATUS — CONSUMED (2026-08-13, S-ORDINE) -> src/common/ (the refactor this pre-refactor snapshot gated, landed lecture-era; blessed numbers invariant by construction).** AS-IS snapshot of git a986717, kept as provenance. Full text preserved (R4).

# Interface & convention audit — pre-refactor snapshot (2026-07-10)

*Mandate: extreme coherence across the package's models. This document freezes
the AS-IS state (git a986717) before introducing `src/common/`; every claim is
from direct code reading, with file:line references. Blessed numbers are
invariant by construction: the refactor below routes existing call chains
through one shared core without changing a single numeric input.*

## 1. Where the CJ state is computed (four code paths)

| # | path | algorithm | equilibrium sound speed | tolerances | used by |
|---|---|---|---|---|---|
| 1 | `sdtoolbox.postshock.CJspeed` + `PostShock_eq` (vendored ≡ official Apr-2026 release, see `validation/sdt_official_audit.md`) | 21-point density-ratio sweep + LSQ parabola, repeat to R²≥0.99999; `shk_eq_calc` Newton with ERRFT=ERRFV=1e-4 | `sdtoolbox.thermo.soundspeed_eq` (TP method, App. G2) | ERRFT/ERRFV 1e-4; sonic residual ≈1.2–1.6e-3 | `src/thrust/sk_models.cj_calc` (l.127-130), `src/cycles/cycles.three_cycles` (l.415-420), `src/detonation/znd_profiles`, `src/detonation/cj_sweeps` |
| 2 | `src/detonation/cj_states.CJ_state` | own solver: `minimize_scalar` (bounded r∈[1.35,2.4], xatol 1e-6) over Rayleigh speed, `brentq` on the eq-Hugoniot residual (xtol 1e-6) | own `soundspeed_eq` (SV method, one-sided 1e-4) | see left | standalone demo/table (`__main__`); **deliberately independent** cross-check of path 1 (README l.126) |
| 3 | `src/thrust/st_core._hug_point` + `stechmann_nozzle.det_state` | own solver: secant on T along the eq-Hugoniot (residual < 2e2 J/kg ≈ 0.005%), fixed-point on P (2e-4), 3-level parabolic refinement of min U over x | `sdtoolbox.thermo.soundspeed_eq` | resid 2e2 J/kg; recorded `sonic_resid` ~1e-3 | Stechmann matched-cycle pipeline (18/18 Table-1 validation; live in design-study step f) |
| 4 | (consumer) `src/cycles/q_mapping` | no CJ solve: reads `data/cycles_ws.json` (produced by path 1) and re-derives M_CJ = U_CJ/a1 as a consistency check (max dev printed, 0.00%) | — | — | q̃ tables |

**Finding CJ-1.** Paths 1–3 are three *independent implementations* of the same
physics. 2 and 3 exist on purpose (2: pedagogical standalone solver validated
against Caltech DB; 3: verbatim replication of the Stechmann-paper pipeline
whose 18/18 row validation and design-study numbers are blessed). The
incoherence to fix is not their existence but that **path 1 is instantiated
twice with different composition inputs** (Finding MIX-2) and that nothing in
the repo *asserts* 1≡2≡3 within stated tolerances.

**Finding CJ-2.** `soundspeed_eq` exists in three flavours: official TP method
(`sdtoolbox/thermo.py`), SV method (`cj_states.py` l.38-53), and the
`sk_models.aeq` wrapper (SDT first, SP fallback). Numerically concordant to
4 decimals on γ_e (audited), but only path 1's is canonical.

## 2. Mixture registry duplicated four times

| registry | file | entries | composition format | mechanism field |
|---|---|---|---|---|
| `MIXTURES` | `src/cycles/cycles.py` l.357-370 | 12 (`H2/air` … `kerosene/O2`) | exact stoich X string (`'H2:2,O2:1,N2:3.76'`) | `'gri30.yaml'` / abs path DODEQ |
| `MIX` | `src/cycles/q_mapping.py` l.64-79 | same 12 + `(x, y, n_fuel)` per fuel | same X strings (duplicated) | same (duplicated) |
| `CASES` | `src/thrust/sk_models.py` l.46-61 | same 12 as `C12H26/*` **(label differs from `kerosene/*`)** + 4 `SKREP:*` | `set_equivalence_ratio(1.0, fuel, ox)` then **q string re-rendered at %.6f** (`setup`, l.101) | GRI / DODEQ + K per oxidizer class |
| `PROPS` | `src/thrust/stechmann_nozzle.py` l.118-120 | 3 (H2, CH4, RP-1; +C2H4 injected by the design study) | `set_equivalence_ratio(phi, fuel, ox)` (φ from Table 1) | `data/gri30_CHO_eq.yaml` / dodecane (paper-specific reduced sets) |

**Finding MIX-1.** Same physical mixture, two label conventions
(`kerosene/air` in cycles/q_mapping vs `C12H26/air` in thrust).

**Finding MIX-2.** Same physical mixture, two numerically different
compositions: cycles feeds `CJspeed` the exact ratio string, sk_models feeds
the %.6f-rounded normalized mole fractions — a ~1e-7 relative composition
perturbation, i.e. U_CJ agreeing to ~1e-7 rel but **not bit-identical**.
Harmless at every displayed precision, but it silently defeats any
"same CJ from all paths" assertion stronger than ~1e-6.

**Finding MIX-3.** `PROPS` is *not* a duplicate of the other three: it is the
Stechmann-paper propellant set (fuel–O2 at paper φ, reduced CHO mechanisms for
speed). It stays a separate table, but should state that and share constants.

## 3. Units and reference states

Internal computation is SI everywhere (Pa, K, kg, J/kg). Edges:

| suite | fill/chamber reference | ambient | notes |
|---|---|---|---|
| thrust (`sk_models`, `tables`) | **P1 = 101325 Pa** (1 atm), T1 = 300 K; SKREP 0.15 MPa / 255 K (A6, re-bless 2026-07-16) | Pa = 101325 Pa | as SK Table 1 |
| cycles (`cycles`, `q_mapping`, `q_formal`) | **P1 = 1e5 Pa** (1 bar), T1 = 300 K | — (closed cycle) | as the W&S validation build |
| Stechmann nozzle | `Pcp_atm`, `Pinit` converted at boundary (`* ATM`); Ti = 200 K (Table 1) / user | Pa = 1 atm or vacuum | paper protocol |
| display | `P_CJ_bar` (cycles JSON, bar), `P0a/Pinita` (atm), MJ/kg for q | — | conversions only at print/JSON edges |

**Finding U-1.** The 1 atm vs 1 bar split between the thrust and cycle suites
is *intentional* (each replicates its source paper) but was stated nowhere
centrally. It must be documented, not "fixed": blessed numbers on both sides
depend on it (e.g. U_CJ H2/air = 1969.0 at 1 atm vs CH4/air 1802.8 at 1 bar).

**Finding U-2.** Constants duplicated: `G0 = 9.80665`, `ATM = 101325.0` defined
in `sk_models.py` l.38 and `st_core.py` l.38-40 (as `PA`); `T_ref = 298.15`
hard-wired inside `q_formal.py`; `tables.py` re-imports from `sk_models`.

## 4. Field-name drift for the same physical quantities

| quantity | cj_states | sk_models | cycles | stechmann |
|---|---|---|---|---|
| CJ speed | `UCJ` | `UCJ` | `U_CJ` | (implicit via PR) |
| eq. isentropic exponent ρ₂a_eq²/P₂ | `gamma_eq` | `gamma_e` | `gamma_e_CJ` | `gamma` |
| frozen cp/cv at CJ | `gamma_fr` | `gamma_fr` | `gamma_fr_CJ` | — |
| eq. sound speed at CJ | `a2_eq` | **`a_eq2`** | — | (via c*) |
| CJ pressure | `P2`, `p2p1` | `P2`, `p2p1` | `P_CJ_bar`, `pipk_FJ` | `PR` |
| CJ temperature | `T2` | `T2` | `T_CJ` | `TCJ` |

## 5. Resolution (implemented by this refactor — minimal, adapter-based)

1. **`src/common/constants.py`** — single home for G0, P_ATM, P_REF_BAR,
   T_STD, T_REF and the standard tolerance ladder. Existing modules keep
   their local names (`ATM`, `G0`, `PA`) as aliases imported from common.
2. **`src/common/mixtures.py`** — the 12-mixture registry (one entry = Cantera
   X string + mechanism + display names + fuel/ox + SK K-factor + CxHy info),
   with the `kerosene/* ↔ C12H26/*` alias map. `cycles.MIXTURES`,
   `q_mapping.MIX`, `sk_models.CASES` become thin views of it.
   `stechmann_nozzle.PROPS` stays (paper-specific set) with a docstring
   cross-reference.
3. **`src/common/cj_core.py`** — ONE function `cj_state(mix, p1, T1, …)`
   wrapping the canonical SDT chain (CJspeed → PostShock_eq → soundspeed_eq)
   and returning the canonical record (U_CJ, p2, T2, gamma_e, gamma_fr, a_eq,
   a_fr, s2, h1, + derived). `sk_models.cj_calc` and `cycles.three_cycles`
   route through it via thin adapters (schema-preserving). q_mapping consumes
   its output store. `cj_states.CJ_state` (path 2) and
   `stechmann_nozzle.det_state` (path 3) remain **independent by design** —
   their agreement with `cj_core` becomes an *asserted* test
   (`tests/test_cj_coherence.py`) at the documented cross-solver tolerance,
   instead of an unchecked hope.
4. **Composition unification** — the registry X string (exact ratios) becomes
   the single composition input for path 1 in all modules, removing the %.6f
   rounding (Finding MIX-2). Measured effect on sk_models records: ≤2e-6
   relative on U_CJ/γ_e (verified in `tests/`), far below every display digit
   and every validation tolerance; cycles inputs are unchanged (they already
   used the exact strings).
5. **Blessed-number invariance policy** — `stechmann_nozzle.det_state` keeps
   its own Hugoniot solver because the 18/18 Table-1 states are cached and the
   design-study step (f) recomputes `matched()` live at print precision 0.1 s
   (`245.3`); swapping the solver would move the third decimal and risk the
   displayed digit for zero physical gain. Decision re-evaluated empirically
   in `tests/test_cj_coherence.py` (det_state vs cj_core deviation is printed
   on every run).

Everything else (physics, stage logic, JSON schemas, validation reports) is
untouched.


## 6. Post-refactor outcome (measured, 2026-07-10)

* Canonical identity (test i): `cj_core` vs `sk_models.cj_calc` vs
  `cycles.three_cycles` — **0.0 relative deviation (bit-identical)** on U_CJ,
  gamma_e, p2, T2, s2, h1 (H2/air, C2H4/O2 at 1 atm; CH4/air at 1 bar).
* Finding MIX-2 composition unification: sk_models records moved by
  **1.33e-8 rel** on U_CJ vs the shipped JSON (H2/air) — invisible at every
  display digit (1969.0225 -> 1969.0225).
* Independent solvers vs cj_core: `cj_states.CJ_state` **7.2e-8** (U_CJ) /
  1.3e-5 (gamma_e); `stechmann_nozzle.det_state` **8.3e-4** (PR) / 7.1e-5
  (T_CJ) / 6.9e-6 (gamma) — the ~1e-3 PR deviation empirically confirms §5:
  swapping det_state onto cj_core would have moved the blowdown inputs at the
  same order and endangered the 0.1-s-precision design-study digits (245.3
  reproduced exactly with the solver kept in place).
* Cycle-side regeneration: `q_mapping` rerun under the shared registry
  reproduced data/q_mapping.{json,md} **byte-identical except the run date**.
* Full ledger: tests/run_all.py (suite i-v + live examples & design study).
