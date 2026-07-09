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
validation/         frozen validation reports (do not regenerate; data/ copies may)
examples/           the three quickstart scripts (each ends with an assertion)
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
