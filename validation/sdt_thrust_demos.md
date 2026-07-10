# SDToolbox official demos vs the course thrust models — census & numeric comparison

*2026-07-10. Official reference: `SDToolbox.zip` release "Updated April 2026"
(49 Python demos ≡ MATLAB set). Complements `validation/sdt_official_audit.md`
(code/mechanism/γ audit): this report closes the specific question **"does the
official SDT ship an RDE thrust model, and how do its impulse demos compare
with ours?"** — including one refinement of the previous audit's §3.1, which
filed all `demo_PrandtlMeyer*` under "wave phenomena not used by the deck".*

## 1. Census

Word-boundary search `\b(impulse|thrust|isp|rocket|rotating detonation|rde)\b`
over all 49 Python demos (and the MATLAB mirror — same 4 hits; a naive
substring grep false-positives on `display` etc.):

| demo | what it computes | thrust/impulse content |
|---|---|---|
| `demo_rocket_impulse` | steady rocket: HP-equilibrium chamber (H₂/O₂ + He sweep, **100 bar / 300 K**), quasi-1D isentropic expansion, Isp = (u + (P−Pa)/(uρ))/9.81 with **Pa = 0**, exit ≈ 1 bar | YES — steady chamber Isp, **equilibrium vs frozen** bracket |
| `demo_quasi1d_eq` | same machinery at 10 bar chamber (H₂/O₂/He), exit-pressure specified; sonic throat where M_eq = u/a_eq = 1 | YES — steady Isp eq + frozen |
| `demo_PrandtlMeyerDetn` | PM fan + shock polar from the CJ state **and the RDE "ideal axial flow model"**: uₑ = √(2(h₁−h)) on the equilibrium isentrope through CJ, sonic axial state Mₑ = uₑ/a_eq = 1, **specific thrust T/ṁ = uₑ + (P−Pa)/(ρuₑ)** (sonic point, matched sweep, vacuum limit) | **YES — the one RDE thrust model in the official demos** |
| `demo_PrandtlMeyerLayer` | two-layer shock/PM polar matching (RDE upstream expansion geometry) | no (wave dynamics only, no T/ṁ) |

No other demo touches thrust or impulse. In particular the official demo set
contains **no PDE single-cycle impulse model** (Wintenberger's impulse-model
line of work is not demoed), **no pressure-history model** (SK K·ΔP_CJ), and
**no blowdown/mass-weighted chamber model** (Stechmann).

**Verdict (census).** The expected answer "no RDE thrust demo" is *almost*
right but needs one correction: `demo_PrandtlMeyerDetn` embeds exactly one —
the Shepherd–Kasahara **ideal axial flow** model (FM2017.001 Sec. 4), i.e. the
same "AX" model our `src/thrust/sk_models.axial_calc` implements. Everything
else in our thrust stack (PH pressure-history, Stechmann blowdown, PDE bridge)
has **no demo counterpart** and enters the course from the papers directly.

## 2. demo_PrandtlMeyerDetn (RDE axial model) vs `sk_models.axial_calc` — numeric

Method: the demo's exact algorithm (march in specific volume v ∈ [v_CJ, 50
v_CJ], 1000 `SV`-equilibrate steps, a_eq per step, sonic point interpolated on
Mₑ = 1 — the demo pchips over sorted arrays, we pchip the same monotone branch
— ambient = 1 atm) re-run inside our stack at matched condition and mechanism
(gri30), against our `axial_calc` (log-P march + exact bisection at w = a_eq).
Same physics, two independent numerical treatments:

| case | demo algorithm T/ṁ [m/s] | ours (`axial_calc` sonic) [m/s] | Δ |
|---|---|---|---|
| CH₄/air, 1 bar / 300 K (the demo's default condition) | 1250.4244 | 1250.4247 | **+2.6e-5 %** |
| H₂/air, 1 atm / 300 K (our standard; vs the *shipped* record) | 1353.0971 | 1353.0971 (shipped `FovM_sonic`) | **+4.5e-6 %** |

U_CJ agreed to ≤1.3e-6 % in both cases (same CJspeed). The previous audit's
cross-run of the `demo_quasi1d_eq` sonic core on the H₂/air CJ (P* = 2.0621e5
Pa, w* = 951.9 m/s, T/ṁ = 1353.1) found 0.005 % (`sdt_official_audit.md`
§3.2.4); the sharper 1e-6-grade agreement here uses the demo's own
interpolation refined on the monotone branch.

**Verdict: COERENTE (identical model).** The official RDE performance demo and
our AX model are the same computation; residuals are grid/interpolation noise.
Scope note: the demo *additionally* computes the PM fan, the oblique-shock
polar interaction and the bounding-layer matching (wave dynamics outside the
deck's thrust scope, knowingly not replicated — audit §3.3), and tabulates the
T/ṁ(P_exit) sweep and vacuum limit; our module tabulates the same sonic point
plus the pressure-matched exit, and adds the frozen lower bound
(`chem='frozen'`) that this demo does not carry (its sibling
`demo_rocket_impulse` does).

## 3. demo_rocket_impulse vs our Stechmann constant-pressure limit — numeric

The demo is a *steady* (constant-chamber) rocket: the comparable object in our
stack is the **CP collapse of the Stechmann blowdown model** (PR → 1), which
is already the model's internal consistency check (tables V&V check 5). On the
demo's own undiluted case (H₂:1.001/O₂:0.5, chamber HP at 100 bar / 300 K →
T_t = 3734.8 K, γ_e = 1.1321, exit at 0.989 bar, ambient Pa = 0, g = 9.81):

| quantity | value | note |
|---|---|---|
| demo Isp, shifting equilibrium | **415.26 s** (uₑ = 3760 m/s) | full recombination recovery |
| demo Isp, frozen | **387.14 s** (−6.77 %) | the demo's own bracket |
| our one-γ steady model at the same chamber & NPR = 101.1 (γ_e frozen at the chamber value — Stechmann assumption 2, `st_core` closures, ε = 14.0 from the area–Mach relation) | **392.79 s** (−5.41 % vs eq) | falls **inside the demo's bracket**, 1.4 pts above frozen |
| Stechmann PR → 1 collapse vs steady CF·c*/g₀ identity (re-verified live at these chamber conditions, ε = 1, sea level) | rel. err. **2.5e-11** | model-internal identity |

Why the differences — three structural mismatches, all understood:

1. **Chamber conditions.** The demo runs a 100-bar HP-combustion chamber (its
   He-dilution "warm gas thruster" study); our Stechmann cases build the
   chamber from a **detonation of a 1-atm fill** (P_CJ ≈ 18.6 atm for H₂/O₂) —
   so absolute Isp values are not comparable case-to-case; the comparison
   above is model-level at *matched* chamber state and NPR.
2. **Nozzle.** The demo has no discrete nozzle: it expands to the end of its
   isentrope table (~1 bar exit) and quotes vacuum-ambient Isp
   (u + P/(ρu), Pa = 0). Our closures replicate that as an ideal ε = 14 bell
   perfectly expanded at 1 bar in vacuum; our standard tables instead quote
   ε = 1 / ideal-aerospike / optimized-bell at Pa = 1 atm.
3. **Chemistry along the expansion.** The demo carries shifting equilibrium
   (and the frozen bracket); Stechmann's assumption 2 freezes γ = γ_e(chamber)
   in space and time. At the deep NPR = 101 of this case the one-γ
   linearization gives up 5.4 % of the equilibrium value (it loses part of the
   recombination heat release along the isentrope) while staying above the
   frozen floor — consistent with, and extending, the ±2 %-of-equilibrium
   figure measured at the Stechmann-regime PR ≈ 19
   (`validation/gamma_phase_audit.md` §4 row 9: the one-γ variant is "adjacent
   to equilibrium, never close to frozen"; the gap grows with expansion depth).
4. Edge conventions: the demo uses g = 9.81 (we used it for the comparison;
   package standard is G0 = 9.80665) and Pa = 0 with a finite exit pressure.

**Verdict: COERENTE nel limite comune, COMPLEMENTARE nel resto.** The demo
validates precisely the steady-CP limit our blowdown model collapses to
(identity at 2.5e-11), and its eq/frozen bracket brackets our one-γ treatment
as the γ-phase audit predicts. The blowdown dynamics, mass-weighting and
nozzle optimization of Stechmann have no SDT-demo counterpart.

## 4. PDE impulse models

No official demo implements a PDE single-cycle impulse model, so the course's
PDE→RDE bridge (SK FM2017.001 Sec. 6, Eqs. 63–64: impulse coefficient
K_PDE ≈ 4.3 vs the RDE effective K ≈ 1.5 — lecture-deck material, not a repo
module) has **nothing to be compared against in SDT: verdetto ASSENTE** on
both sides at code level. The deck's K = 1.02/1.54 pressure-history
parametrization is SK's own fit of the S&K (2013) CFD traces, already
validated against SK Tables 1–2 in `validation/vv_thrust.md`.

## 5. Summary table (demo → ours)

| SDT demo | our equivalent | comparison | verdict |
|---|---|---|---|
| `demo_PrandtlMeyerDetn` (RDE ideal axial flow, specific thrust) | `sk_models.axial_calc` (SK Eqs. 44–45) | 1250.42 vs 1250.42 m/s (CH₄/air 1 bar); 1353.0971 vs 1353.0971 m/s (H₂/air 1 atm) | **coerente** (≤2.6e-5 %) |
| `demo_quasi1d_eq` (steady eq nozzle, sonic throat M_eq=1) | same `axial_calc` machinery (+ `chem='frozen'` bracket) | 0.005 % on P*, w*, T/ṁ (audit §3.2.4) | **coerente** |
| `demo_rocket_impulse` (steady chamber, eq vs frozen Isp) | Stechmann CP collapse (`stech_calc` PR→1) + one-γ closures | identity 2.5e-11; one-γ inside the demo's eq/frozen bracket (−5.4 % / −6.8 %) | **coerente nel limite CP; complementare** (no blowdown/nozzle-opt in SDT) |
| `demo_PrandtlMeyerLayer` | — (wave-dynamics scope, no T/ṁ) | — | **assente** (declared out of deck scope, audit §3.3) |
| PDE impulse (any) | — (deck-level SK Eqs. 63–64 bridge) | no demo exists | **assente** |
| SK pressure-history (K·ΔP_CJ), Stechmann blowdown/nozzle | `ph_calc`, `stech_calc`, `stechmann_nozzle` | no demo exists; validated against the papers (`vv_thrust.md`, `st_opt_validation.md`) | **complementare** |

*Repro notes: comparisons executed with the repo's vendored sdtoolbox (proven
line-identical to the official release in `sdt_official_audit.md`) on Cantera
3.2.0 / gri30; demo algorithms re-run verbatim (SV march, pchip sonic
interpolation, demo ambient/g conventions) at matched conditions. The
independent SV-march bound is now a permanent regression test:
`tests/test_axial_bound.py`.*
