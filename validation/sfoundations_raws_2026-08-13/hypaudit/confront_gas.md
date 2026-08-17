# HYPAUDIT [GAS-FROZEN] — Frozen thermally-perfect mixture pin vs the literature corpus

Session: S-FOUNDATIONS raws 2026-08-13 (audit executed 2026-08-17).
Hypothesis bundle audited: **FROZEN THERMALLY-PERFECT MIXTURE** — fixed composition
downstream of Gamma_d, gamma(T) variable, single phase, no condensables.
Question: is the frozen pin legitimate as a scope pin WITH a named model-form error bar,
and what bracket magnitudes does the corpus support? IN-REPO SOURCES ONLY.

**VERDICT: LEGITTIMA-DICHIARATA-MONITORATA** (legitimate as a declared + monitored
hypothesis; the monitor set already exists in-repo and is named in §5; the bracket
magnitude is instance-dependent and must be re-executed per propellant — §4).

---

## 1. What the pin actually is (record status)

- User pin of record 2026-08-11 (S-GAUNTLET closure, memory
  `scope-pins-frozen-thermally-perfect`): design-region expansion = FROZEN composition of
  a THERMALLY PERFECT gas mixture (p = rho R T with fixed R; e = e(T) free, so gamma(T)
  allowed); two-phase a declared exclusion, not a work item; real-gas EOS and finite-rate
  chemistry OUTSIDE by declaration, "priced where already priced ([T-EQBR]
  frozen/equilibrium bracket; N4 ladder)".
- The model-form error bar is not an IOU: it is the **executable** bracket [T-EQBR] of
  record (M0 `docs/rde_nozzle_MASTER.md` ll. 970-980): shifting-equilibrium ceiling
  (SP-equilibrate isentrope, Gibbs solver, eq sound speed c^2 = dP/drho along the table)
  sits **+6.3..+7.0% ABOVE the frozen ceiling on every PR** (bars <= 0.003 s;
  constant-cp known-answer PASS, corrupted route rejected) — THEOREM* within the caloric
  closure pair [C-IGMIX]. Hypothesis ledger (`docs/rde_nozzle_hypothesis_ledger.md` §2,
  row C-IGMIX): PRICED, "+6.34..+6.97% ceiling bracket with bars (group (xii));
  **falsifier = finite-rate leaving the bracket**".
- Note the sign discipline this forces: frozen is the LOWER rung of the ceiling pair;
  the physical (finite-rate) curve is expected INTERIOR to [frozen, equilibrium]
  (corroborated externally, §3.2). The frozen pin therefore UNDER-states the available
  ceiling by up to ~7% at the audited instance — a conservative direction for
  bound-statements, but a first-order model-form error for absolute Isp claims, which is
  exactly why the bracket, not the frozen number alone, is the quotable object.

## 2. SOTA practice check: the corpus DOES what the pin says

The strongest legitimacy evidence is that the frozen thermally-perfect closure is the
**standing nozzle-side model of the SOTA RDE nozzle literature itself**, not an internal
convenience:

- [Paxson-Miki 2022, `literature_review/reports/paxson_miki_2022_nasa_opt.md`]: 3D
  OpenNCC nozzle RANS with chemistry frozen (verbatim: "The fluid constituent species
  are 'frozen' throughout the domain", p. 5), composition from a CEA equilibrium
  calculation at the time-averaged exit state. The report's F-finding states it plainly:
  their nozzle-side model "is *exactly* the P1 scope pin and exactly the validity window
  of Lemma A's thermal pin (p = rho R T with frozen composition), so Lemma A applies to
  the SOTA nozzle model as-is."
- [Harroun 2021, `reports/harroun_2021_jpp_nozzle_perf.md`]: frozen 2-species product
  mixture (60.5% H2O / 39.5% CO2), ideal-gas EOS with temperature-dependent c_p —
  verbatim classification in the report: "thermally perfect, calorically imperfect,
  frozen composition". Their justification "chemical reactions would be minimal when the
  flow has reached the nozzle" (p. 666) is a judgement, not a demonstration — but they
  quantify the composition-truncation half: Table 2 (p. 667), 9-species detonation
  composition reduced to 5/3/2 species with normalized THRUST error 0.58%/0.52%/0.28%.
- [Harroun 2020, `reports/harroun_2020_validation.md`]: H-D1 "Frozen product species;
  chemical kinetics ignored; composition from CEA for CH4/O2 detonation."
- [Miki 2020, `reports/miki_2020_nasa_methodology.md`]: declared hypothesis 3 —
  chemistry complete at combustor exit; nozzle expansion chemically **frozen** (p. 5);
  3-species thermally-perfect mixture (H2O, N2, O2).
- [Kaemming-Paxson 2018, `reports/kaemming_paxson_2018_eap.md`]: EAP containment
  hypotheses are even STRICTER than our pin (calorically perfect, one frozen gamma) —
  the industry metric lives inside a coarser closure than P1.
- [Janc 2025, `reports/janc_2025_differentiable.md`, finding T-4]: the state-of-the-art
  differentiable finite-rate solver itself, the moment an optimization loop is attached,
  falls back verbatim to "the specific heat ratio is fixed at 1.29, and the chemical
  reaction is modeled as a single-step hydrogen-air total combustion reaction" (p. 25).
  The report reads this as corroboration of the anti-overengineering pin P1. Their
  frozen-composition p = rho R T EOS with NASA-7 thermo "is also exactly our Lemma-A
  thermal pin".
- [Ornano 2017, `reports/ornano_2017_pde_shapeopt.md`]: temperature-dependent gas
  properties in the PDE nozzle URANS (gamma(T), not one frozen gamma) — i.e. the corpus
  member that breaks H1 (one gamma) still keeps composition effects out of the design
  layer; our pin (gamma(T) free, composition frozen) sits exactly at the corpus's own
  operating point.

Conclusion of §2: the pin is not weaker than SOTA practice — it IS SOTA practice, with
gamma(T) retained where several corpus members (Paxson-Miki Q2D side, Liu 2022 design
formulas, Kaemming-Paxson) degrade further to calorically perfect.

## 3. Adversarial side: what the corpus says the frozen choice COSTS

### 3.1 The thermo closure is a FIRST-order lever, not a detail

- [Paxson-Miki 2022, report F8 / confrontation §3bis-J]: the thermo remap at the
  Q2D-to-3D interface (R_g 60.12 -> 71.05 ft-lbf/lbm-R, from a CEA equilibrium
  calculation) shifts **mass flow by -15.6% and ideal thrust by -10.5% (589 lbf)** —
  roughly five times their entire optimization gain. The report calls this "a live
  instance of the [T-EQBR] frozen/equilibrium bracket being the dominant term." (The
  confrontation advisory carries the same reading in §3bis-J as "il dato più forte della
  tranche" — cited here as PENDING-RATIFICATION evidence, CAVA non ratificata.)
- [Wintenberger-Shepherd 2004, `reports/wintenberger_shepherd_2004_thermo.md`, F7]:
  p. 13 verbatim: "The results are significantly influenced by the variation of the
  specific heat capacity with temperature in the detonation products and the
  dissociation and recombination processes"; products at state 4 "are still in a
  partially dissociated state and a significant part of the energy released by the
  detonation is not available for work". The report's own gloss: "the same physics our
  [T-EQBR] bracket prices", and it is priced as FIRST-order, not second-order.
  Honest asymmetry carried from the report: this is magnitude corroboration in a
  ZERO-DIMENSIONAL cycle, not evidence about our nozzle-flow numbers.

### 3.2 Ordering corroboration: kinetics sits INSIDE [frozen, equilibrium]

- [Sun 2019, `reports/sun_2019_gamma_var_rao.md`, T4]: Fig. 5 (p. 4) plots gamma vs
  area ratio for **frozen, kinetics and equilibrium** closures of the same NTO/MMH
  mixture: the kinetics curve lies **strictly between** frozen (upper) and equilibrium
  (lower) over the whole range; read off at AR ~ 200: frozen ~1.385, kinetics ~1.35,
  equilibrium ~1.26 (approximate, raster figure). The report registers this as "an
  independent, published corroboration of the *ordering* that our [T-EQBR] bracket
  assumes", naming the physical curve as an interior point of the bracket. This is the
  key structural fact making the frozen pin + bracket a legitimate MODEL BRACKET rather
  than a hope: the corpus supports interiority of the true (finite-rate) answer.
- Magnitudes at the design-functional level from the same paper: gamma(T) vs
  constant-gamma buys ~+0.92 s on ~321 s vacuum Isp at AR 280:1 (Tables 2-3) — i.e. the
  caloric-imperfection half our pin RETAINS is worth ~0.3% in Isp at large AR, while
  the whole constant-gamma family spans only ~0.9 s. This separates cleanly the part we
  keep (gamma(T)) from the part we freeze (composition), whose ceiling-level price is
  the +6.3..+7.0% bracket.

### 3.3 H2-air vs hydrocarbon / fuel-oxygen: the spread is propellant-dependent

- [Wintenberger-Shepherd 2004, F7]: STANJAN equilibrium computations cover H2, C2H4,
  C3H8 and JP10 with O2 AND air (Figs. 17-20, 24). The dissociation/recombination
  physics **reverses an ordering near stoichiometry: fuel-air beats fuel-oxygen**
  (Fig. 19) — because fuel-oxygen products are hotter and more dissociated, so more of
  the release is locked in dissociated species. Consequence for the pin: the frozen
  model-form error is SMALLEST for diluted (air-breathing / fuel-lean) products and
  LARGEST for hot stoichiometric fuel-oxygen products. The corpus supports the
  direction; it does NOT supply transferable per-propellant frozen-vs-shifting Isp
  percentages beyond our own executable instance.
- Also from the same report (H-n): Wintenberger-Shepherd themselves run "two mutually
  inconsistent chemistry closures... interchangeably" (frozen constant-gamma analytic
  vs STANJAN shifting equilibrium with partial recombination, p. 13) without stating
  they bound different objects — a corpus-side warning that frozen and equilibrium
  numbers must never be quoted as the same object. Our bracket semantics (pair quoted
  together, THEOREM* within [C-IGMIX]) is exactly the repair of that defect.
- [Sun 2019, T5 / confrontation C13 — pending-ratification for the C13 wording]: Sun
  2019 must NOT be cited as a physical frozen thermally-perfect instance compatible
  with P1 (composition-varying c_p glued onto constant R). The only corpus member that
  LOOKS like a variable-gamma frozen design paper is inadmissible as such — the pin's
  physical instances in the corpus are the NASA CFD papers (§2), not Sun.

### 3.4 The remaining bundle clauses

- **Single phase / no condensables**: user pin P2 (two-phase declared exclusion). The
  corpus is SILENT on condensables in RDE nozzle products: H2/CH4/RP products at
  3000-3400 K inflow (Harroun 2021 uniform 3400 K; Paxson-Miki CEA exit state) are far
  from condensation in every corpus case; no corpus paper models condensed phases in the
  expansion (Hoffman 1987 H-d3 explicitly "no condensed phases"). Silence is not
  evidence of smallness for metallized/soot-rich hydrocarbon operation — carried as a
  residual risk, correctly handled as declared exclusion rather than priced hypothesis.
- **Fixed composition downstream of Gamma_d specifically**: the causal-separation row
  H-R1 (hypothesis ledger §1) already carries the executable rejector minted S14 —
  total-enthalpy-flux residual across Gamma_d, violation channel = afterburning
  documented in RDEs. This is the monitor that guards the pin's PLACEMENT (composition
  frozen from Gamma_d on), distinct from the bracket that prices its CLOSURE.

## 4. Bracket magnitudes the corpus supports

| Object | Magnitude | Source / status |
|---|---|---|
| Equilibrium ceiling above frozen ceiling (repo instance, all PR) | **+6.34..+6.97%**, bars <= 0.003 s | [T-EQBR] M0 ll. 970-980, THEOREM* within [C-IGMIX]; executable, group (xii) |
| Thermo-closure remap at code interface (CPG -> frozen CEA mixture) | -15.6% mdot, -10.5% ideal thrust | Paxson-Miki 2022 p. 4, report F8 — dominance evidence, ~5x their optimization gain |
| Species truncation within frozen closure (9 -> 2 species) | 0.28-0.58% normalized thrust error | Harroun 2021 Table 2 p. 667 (non-monotone ordering suggests cancellation — rung must be pre-registered, report F11) |
| gamma(T) vs constant-gamma (the part the pin KEEPS) | ~+0.92 s on ~321 s (~0.3%) at AR 280:1; constant-gamma family spans ~0.9 s | Sun 2019 Tables 2-3 |
| Frozen/kinetics/equilibrium gamma at AR ~200 (NTO/MMH) | 1.385 / 1.35 / 1.26, kinetics strictly interior | Sun 2019 Fig. 5 (raster read-off), report T4 |
| Real gamma(T) ceiling vs frozen-gamma_s closed form (caloric idealization, different axis) | -4.4..-7.9% | M0 ll. 941-944 (purge delta of record) |
| Fuel-air vs fuel-oxygen ordering reversal near stoichiometry | sign reversal (no transferable %) | Wintenberger-Shepherd Fig. 19, report F7 |

Honest summary: the corpus supports a **several-percent (5-10% class) ceiling-level
frozen/equilibrium spread**, with our single executable instance at +6.3..+7.0%, the
physical answer interior (Sun ordering), the spread growing with area ratio (Sun Fig. 5
"separating rapidly past the throat") and with product temperature (fuel-oxygen worse
than fuel-air near stoichiometry). No corpus source licenses quoting +6.3..+7.0% for a
DIFFERENT propellant/PR window without re-executing the bracket — the bracket is cheap
and executable, so re-execution per instance is the monitor, not a gap.

## 5. Monitors required (all already exist in-repo; audit confirms sufficiency)

1. **[T-EQBR] bracket re-execution per propellant/instance** — the frozen number is
   quotable only as the pair [frozen, equilibrium] with bars (M0 winner semantics:
   closures, never hardware).
2. **[C-IGMIX] falsifier** — finite-rate result leaving the [frozen, equilibrium]
   bracket kills the pricing (hypothesis ledger §2); Sun 2019 T4's kinetics-informed
   c_p(T) freeze (ODK-class 1-D kinetics on a seed contour) is the registered
   bracket-NARROWING practice if the bracket ever becomes the dominant bar.
3. **H-R1 rejector across Gamma_d** — total-enthalpy-flux residual (afterburning
   channel): guards "fixed composition downstream of Gamma_d" as a placement claim.
4. **Species-reduction functional-error rung** (Harroun 2021 Table 2 pattern, report
   F11): pre-registered thrust-error acceptance in the Cantera table-generation step,
   guarding the "which frozen composition" choice inside the pin.
5. **gamma(T) status line per theory piece** (standing directive
   `gamma-variable-generality`, corroborated by Wintenberger p. 15 and Janc T-4):
   gamma = const only as declared oracle, never load-bearing.
6. **Citation discipline**: Sun 2019 never cited as a P1 instance (report T5); frozen
   and equilibrium numbers never quoted as the same object (Wintenberger H-n lesson).

## 6. Residual risks (named, not priced by the corpus)

- Bracket magnitude is a SINGLE internal executable instance; corpus gives ordering and
  dominance evidence but no independent per-propellant frozen-vs-shifting Isp table.
- Hot stoichiometric fuel-oxygen products (Wintenberger Fig. 19 direction): the frozen
  error bar is largest exactly where RDRE hardware runs; the +6.3..+7.0% figure may be
  optimistic there until re-executed.
- Condensables/soot for heavy-hydrocarbon or metallized operation: corpus silent;
  covered only by the P2 declared exclusion.
- Harroun's "reactions minimal in the nozzle" is a judgement, not a measurement, in the
  very paper our pin most resembles; the corpus contains no published finite-rate vs
  frozen nozzle-flow delta for an RDE nozzle (the interior-point evidence is 1-D,
  NTO/MMH, non-RDE).
- Confrontation-advisory confirmations (§3bis-J, §3.21, C13) are PENDING RATIFICATION
  (CAVA non ratificata) — cited here as evidence, never as decided record.

## 7. Verdict rationale

DA-RISCOPARE is excluded: no corpus source contradicts the pin as posed; the SOTA
nozzle papers USE it. LEGITTIMA-ESATTA is excluded: the corpus itself prices the frozen
closure as a first-order model-form choice (Paxson-Miki -10.5% ideal thrust across the
closure boundary; Wintenberger "significantly influenced"), so the pin cannot be exact
— it is legitimate only WITH its error bar attached. CONDIZIONATA is unnecessary: the
validity window does not need to be carved out because the error bar is already
executable and two-sided-bracketed with a named falsifier — that is precisely the
declared+monitored semantics. Hence **LEGITTIMA-DICHIARATA-MONITORATA**, with the six
monitors of §5 (all pre-existing in-repo; this audit adds no new machinery, per the
anti-overengineering pin).
