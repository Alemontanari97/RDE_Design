# RDE Lecture Code — Detonation Thermodynamics and Rotating Detonation Engines

Validated companion code for the university lecture *Presentazione_CVA* on
detonation physics and RDE performance. Every model in the slides is backed by
a script in this repo, every script is validated against the source papers, and
every number in `data/` was produced by the code you are reading.

**Validation badges** (frozen reports in [`validation/`](validation/)):

| suite | result | report |
|---|---|---|
| Wintenberger–Shepherd cycles (analytic + equilibrium chemistry) | **99 / 99 PASS** | `validation/cycles_validation.md` |
| Stechmann Table-1 nozzle optimization (row-by-row) | **18 / 18 PASS** | `validation/st_opt_validation.md` |
| Thrust models V&V (literature + internal + cross-model) | **8 / 8 PASS** (one PASS\* with a documented literature anomaly) | `validation/vv_thrust.md` |

Cross-cutting audits: `validation/VALIDATION.md` (three-pillar summary, 33+22
checks), `validation/gamma_audit.md` + `gamma_phase_audit.md` (γ bookkeeping),
`validation/q_formal.md` (heat-release definition).

## Installation

Python ≥ 3.10, then:

```bash
pip install cantera scipy matplotlib
```

(NumPy comes with SciPy/Cantera. Validated with Python 3.10, Cantera 3.2.0,
NumPy 2.2, SciPy 1.15 — see `requirements.txt`.) No further setup: the Shock &
Detonation Toolbox is vendored in [`sdtoolbox/`](sdtoolbox/) and every script
resolves its paths relative to its own location.

## Quickstart — three worked examples

```bash
python examples/example_cj.py        # ~1-2 min (full CJ search)
python examples/example_cycles.py    # instant
python examples/example_thrust.py    # seconds
```

Expected key outputs:

1. **`example_cj.py`** — CJ detonation of stoichiometric H₂/air at 1 atm, 300 K:
   `U_CJ = 1969 m/s` (Caltech DB/CEA: 1971 m/s, err −0.10 %), `p2/p1 = 15.5`,
   `T2 = 2944 K`, checked live against the shipped validated state.
2. **`example_cycles.py`** — Fickett–Jacobs efficiency table for 12
   stoichiometric mixtures (full equilibrium chemistry):
   `eta_FJ(CH4/air) = 0.300`, fuel–air band 0.28–0.31, fuel–O₂ 0.18–0.23
   (dissociation penalty), plus the one-γ anchor `M_CJ(γ=1.4, q̃=4) = 4.599`.
3. **`example_thrust.py`** — specific-thrust table (Shepherd–Kasahara
   pressure-history and axial-flow models): H₂/air `F/Ṁ = 1194 / 1353 m/s`,
   `Isp_f = 4268 / 4838 s`; plus a live Stechmann mass-weighted cycle Isp for
   H₂/O₂ (`237.1 s`) matching the shipped value to <0.05 s.

## Repository layout

```
sdtoolbox/          vendored Shock & Detonation Toolbox (Caltech, GALCIT FM2018.001)
src/detonation/     CJ & von Neumann states, ZND profiles, CJ parameter sweeps
src/cycles/         Wintenberger–Shepherd cycle analysis, heat-release mapping (q, q̃, q°)
src/thrust/         Shepherd–Kasahara + Stechmann thrust models, tables & V&V generator
data/               validated results (JSON) + mechanism files + provenance README
validation/         frozen validation reports + audits (see validation/README.md)
examples/           quickstart scripts + end-to-end design study (all self-checking)
figs/               output directory for the optional plot stages (created on demand)
```

## Theory → code → paper map

| module | equations implemented | reference |
|---|---|---|
| `sdtoolbox/postshock.py` | CJ speed (density-ratio sweep + LSQ parabola on the equilibrium Hugoniot); frozen/equilibrium post-shock states (Reynolds' iteration) | Shepherd, *SD Toolbox*, GALCIT FM2018.001 (rev. 2021) |
| `sdtoolbox/znd.py` | ZND ODE system driven by thermicity σ̇ through η = 1 − M²; induction/exothermic lengths | FM2018.001 §2.4 |
| `src/detonation/cj_states.py` | equilibrium Hugoniot h₂−h₁ = (p₂−p₁)(v₁+v₂)/2; Rayleigh speed U = v₁√((p₂−p₁)/(v₁−v₂)); CJ = min U; frozen vN jump | FM2018.001 §2; validated vs S&K FM2017.001 Table 2 |
| `src/detonation/znd_profiles.py` | full ZND pipeline CJspeed → PostShock_fr → zndsolve, 4 mixtures | FM2018.001 §2.4 |
| `src/detonation/cj_sweeps.py` | U_CJ, p_CJ, T_CJ vs φ, N₂ dilution, p₁, T₁ | FM2018.001 (method); lecture §2 |
| `src/cycles/cycles.py` | jump ratios & entropy (A19–A22); Δs partition (A31–A32); stagnation Hugoniot, weak-det asymptote, existence limit (A40–A42); steady-engine η (A38–A39); FJ one-γ (B3 = A57, B2); Brayton (A59); Humphrey (A60); real-chemistry FJ/Humphrey/Brayton with η = (h₁−h₅)/q_c (B1) | Wintenberger & Shepherd, AIAA 2004-1033 (**A**); JPP 22(3):694-698, 2006 (**B**) |
| `src/cycles/q_mapping.py` | q̃ = q_c/(c_p T₁); q̃_t = q_c/(c_p T_t1); exact inverse H = (M²−1)²/4M² of B2; q_eff at the physical M_CJ | A18, A21, A40–42, Fig. A16/A22; B2–B3 |
| `src/cycles/q_formal.py` | q° = Σᵢ(Y_i,1−Y_i,2)Δh°f,i(298.15 K); identity q_c(T₁) = q° + ∫Δc_p dT; CJ-plane release fraction | B Eq. 1 + standard-state anchoring (validation/q_formal.md) |
| `src/thrust/sk_models.py` | PH: F_I/Ṁ = K·ΔP_CJ/(ρ₁U_CJ) (Eqs. 6, 15–18), headline K·U_CJ/(γ_e+1) (Eqs. 19–20); AX: w = √(2(h₁−h(P,s₂))) on the equilibrium isentrope, T/Ṁ = w + (P−P_a)/(ρw) (Eqs. 44–45); ST mass-weighted blowdown Isp (Eqs. 4–15) | Shepherd & Kasahara, GALCIT FM2017.001 (2017); Stechmann et al., JSR 56(3) 2019 |
| `src/thrust/st_core.py` + `stechmann_nozzle.py` | c\* (Eq. 1/7); choked ṁ (Eq. 6); C_F bell/aerospike (Eqs. 8–12); blowdown P_c(t), T_c(t) (Eqs. 13–15); mass-weighted Isp (Eqs. 4–5); optima NPR(ε\*) = ⟨P_c⟩/P_a (bell, exact) and = P_max/P_a (spike knee) | Stechmann, Heister & Harroun, JSR 56(3) 2019, doi:10.2514/1.A34313 |
| `src/thrust/tables.py` | regenerates the thrust tables and the 8 V&V verdicts | S&K Tables 1–2; Schwer & Kailasanath 2013 CFD anchors |


## Use as a design tool

`examples/example_design_study.py` walks a complete first-cut RDE design on
stoichiometric C2H4/O2 (fill 1 atm / 300 K; annulus R̄ = 45 mm, gap 5 mm,
L = 80 mm, ṁ = 0.30 kg/s; nozzle trade at P_cp = 10 atm) using the modules
as a library:

```bash
python examples/example_design_study.py    # ~15-60 s, everything computed live
```

| step | expected output |
|---|---|
| (a) CJ state (`sk_models.cj_calc`) | U_CJ = 2373.5 m/s, p_CJ/p₁ = 33.2, γ_e = 1.139 (γ_fr = 1.236) |
| (b) fill height & Wolański wave number (PCI 34 Eqs. 4–5) | l_fill = 20.1 mm/rev, W = 2.69 (band 1.9–4.6) → nominally 2–3 co-rotating heads |
| (c) specific thrust (`ph_calc`, `axial_calc`) | PH 1979 m/s (term II = 300) / AX-sonic 1905 m/s; Isp_f = 892 / 859 s; F = 594 / 571 N |
| (d) frozen bound (`axial_calc(chem='frozen')`) | 1715 m/s, −10.0 % vs shifting equilibrium (Bray freeze lands in between) |
| (e) η_FJ (`cycles.three_cycles`, live) | 0.2042 = shipped value (fuel–O₂ dissociation penalty) |
| (f) Stechmann nozzle at P_cp = 10 atm (`stechmann_nozzle.matched` + `bell_opt`/`spike_opt`) | bell ε* = 2.44 → 233.6 s; aerospike ε* = 6.27 → 245.3 s (+5.0 %) |

Every step cross-checks itself against the shipped validated JSONs and the
script ends with `OK`. To redesign, edit the `KEY / MDOT / RBAR / GAP / LCH /
PCP_ATM` block: any propellant key of `sk_models.CASES` works, and new
propellants enter the nozzle step with one line
(`stn.PROPS['C2H4'] = ('data/gri30_CHO_eq.yaml', 'C2H4', 'O2')`, as done for
C2H4). The wave-number step is deliberately order-of-magnitude (cell size
λ ≈ 29 Δ_i from the shipped ZND induction lengths, Bykovskii l_cr =
(12 ± 5) λ): it reports its uncertainty band, not a false single number.

Library entry points (repo root on `sys.path`; importing never writes files):

| call | returns |
|---|---|
| `src.thrust.sk_models.cj_calc(key)` | CJ record: U_CJ, p₂/p₁, T₂, ρ₂, s₂, γ_e, γ_fr, sonic residual |
| `src.thrust.sk_models.ph_calc(cj, K)` | S&K pressure-history F/Ṁ (terms I+II), Isp_f |
| `src.thrust.sk_models.axial_calc(cj, fuel, ox, chem='eq'\|'frozen')` | S&K axial flow at sonic / matched exit; frozen lower bound |
| `src.thrust.sk_models.stech_calc(γ_e, R, PR, P₁, T_CJ)` | Stechmann mass-weighted blowdown Isp (ε=1 / spike / vacuum) |
| `src.thrust.stechmann_nozzle.matched(prop, φ, T_i, P_cp)` | CP-matched detonation cycle (P_CJ, PR, DC shift, choke margin) |
| `src.thrust.stechmann_nozzle.bell_opt / spike_opt` | optimum area ratio + mass-weighted cycle Isp |
| `src.cycles.cycles.three_cycles(label, X, mech, …)` | FJ (+ Humphrey/Brayton) efficiencies, full equilibrium chemistry |
| `src.cycles.cycles.cj_mach(q̃, γ)`, `eta_fj_1g(q̃, γ, π_c)` | one-γ analytic model (Paper B Eqs. 2–3 / A57) |
| `src.detonation.cj_states.CJ_state / vN_state` | standalone CJ + von Neumann solver (independent of SDT) |

## Two conventions you must not mix

**γ: equilibrium vs frozen.** Every CJ state carries two exponents, and they
are *not* interchangeable:
`gamma_e = ρ₂ a_eq²/P₂` (equilibrium/shifting isentropic exponent, ≈1.13–1.17)
is the "γ_e" of Shepherd–Kasahara Eqs. 19–22 and of the Stechmann model, and
the CJ point is sonic w.r.t. the *equilibrium* sound speed (w₂/a_eq = 1, while
w₂/a_fr ≈ 0.96–0.97); `gamma_fr = c_p/c_v` at frozen composition (≈1.22–1.27)
governs the frozen leading shock (ZND spike). Using γ_fr where γ_e belongs
understated the deck's specific thrust by ~25 % before release — the fix is
documented in `validation/gamma_audit.md` and `validation/vv_thrust.md` (A5).

**q°: the standard-state heat release.** The formal heat release is anchored at
T_ref = 298.15 K: q° = Σᵢ(Y_i,1−Y_i,2)Δh°f,i(T_ref). The project-wide working
definition q_c = h₁(T₁,P₁) − h₆(T₁,P₁) (equilibrium products, Paper B Eq. 1)
obeys exactly q_c(T₁) = q° + ∫_{T_ref}^{T₁}(c_p,react−c_p,prod)dT: at T₁ = 300 K
the shift is <0.01 % (so the shipped tables are unaffected), but it grows to
percent grade at preheated T₁ (700 K: +1.6 %/−0.3 % for H₂/CH₄–air). Details
and Cantera verification: `validation/q_formal.md`, `src/cycles/q_formal.py`.


## Model assumptions map (equilibrium vs frozen — where and why)

Condensed from the 12-row per-usage audit in
`validation/gamma_phase_audit.md` §4 (third-pass audit with the quantified
expansion bounds):

| where | assumption | why (one line) | if you flip it |
|---|---|---|---|
| CJ state, U_CJ | equilibrium Hugoniot, sonic w.r.t. **a_eq** | Rayleigh–Hugoniot tangency ⇒ ds = 0 ⇒ w₂ = a_eq (M₂,eq → 1 verified to 2·10⁻⁶) | frozen sound speed gives M₂,fr ≈ 0.96–0.97 — a category error, not a bound |
| von Neumann state | **frozen** post-shock | the shock is chemically inert on its own scale (ZND ansatz) | equilibrium post-shock is the CJ state itself, not a vN bound |
| ZND interior | frozen sound speed in η = 1 − M²; shifting chemistry only through thermicity σ̇ | composition is a kinetic variable: (∂P/∂ρ)_{s,Y} = a_fr² | a_eq inside ZND double-counts the shifting contribution |
| product expansion (cycle legs 3/4→5, SK axial flow) | **shifting equilibrium** isentrope | τ_flow ≫ τ_chem downstream of the CJ plane | frozen = lower bound (Isp_f −7…−13 %); Bray sudden-freeze at the throat: −0.2…−2 % |
| reactant compression (0→2, ram legs) | frozen **reactant** isentrope (γ₁ ≈ 1.36–1.40) | no reaction below ignition | product-γ on the fresh-gas leg = the one-γ bias: η_FJ −0.10…−0.14 |
| SK Eqs. 19–22 and Stechmann γ | **γ_e = ρ₂a_eq²/P₂** at CJ, then frozen in space/time | the only reading that reproduces SK Table 1 / Fig. 6a | γ_fr ≈ 1.24 understates Eq. 20 by ~3.6 % (the pre-release −25 % thrust bug) |
| M_CJ in the tables | a₁ = frozen **reactant** sound speed | upstream consistency (definition) | one-γ implicit a₁ = √(γ_e R T₁) inflates q_eff/q_c to 1.18–1.30 |

One-line synthesis (the lecture slide): **equilibrium for end states and for
the product expansion (CJ, isentropes, γ_e, Stechmann); frozen for whatever
is faster than chemistry (shock/vN, ZND interior, reactant sound speed and
compression).** The frozen lower bound is live in the code
(`axial_calc(…, chem='frozen')`: H₂/air −6.8 %, C₂H₄/O₂ −10.0 % on sonic
T/Ṁ, matching the audit); the Bray sudden-freeze sits between the two and
would need nozzle-timescale kinetics, deliberately out of scope.

## Regenerating results

Shipped JSONs in `data/` are the validated build artifacts; every one can be
reproduced by the module that owns it (module → artifact ownership in
`data/README.md`). The heavier pipelines are staged and resumable, e.g.:

```bash
python src/cycles/cycles.py all            # one-γ anchors, 12-mixture FJ, sweeps,
                                           # 99-check validation report, 7 figures
python src/thrust/sk_models.py all "H2/air"   # CJ + PH + AX (+ ST for fuel-O2)
python src/thrust/stechmann_nozzle.py validate # 18-row Table-1 verdicts
python src/thrust/tables.py                # thrust tables + 8 V&V verdicts
```

Regenerated reports land in `data/` (they carry run dates); the reviewed,
frozen copies live in `validation/` and should not be overwritten.

## Citing

See `CITATION.md` for the source papers (Wintenberger–Shepherd, Shepherd–
Kasahara, Stechmann–Heister–Harroun) and the SD Toolbox / Cantera / GRI-Mech
citations.
