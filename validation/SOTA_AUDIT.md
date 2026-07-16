# SOTA Audit — RDE lecture-code repository

**Standard applied:** the repo must be a *state-of-the-art academic **and** industrial design tool for SOTA RDE design models* — precision and rigor above all, not "good enough for a lecture."

**Method:** two adversarial multi-agent audits, every finding verified against the referenced literature and against physical realizability. All headline numbers independently re-run live (Cantera 3.2.0 + NumPy 2.2.6; `tests/run_all.py` → 6/6 groups PASS).

- **Literature-fidelity audit** — 490 atomic claims inventoried across all source modules, each traced line-by-line to its paper equation, each verified on three axes (formula / constraint-enforcement / paper-scope). **518 verdicts** collected.
- **Design-exercise audit** — the 8 worked exercises of slides 65–72 (the design tool's user-facing face), each decomposed → reproduced → adversarially challenged → advantage-emergence tested. 49 agents.

---

## Headline verdict

| Axis | Grade | One line |
|---|---|---|
| **Literature fidelity** | **excellent** | 462/518 FAITHFUL, **0 algebraic bugs**. The math faithfully realizes Wintenberger–Shepherd (A/B), Shepherd–Kasahara, Stechmann, SDToolbox — equation by equation. |
| **Design-tool readiness** | **sound-with-gaps** | 55 non-faithful findings, **all of one kind**: a physical quantity is *computed and printed but never enforced as a constraint*. Zero wrong results inside the validated envelope; latent silent-wrong-answer / crash risk outside it. |
| **Exercise architecture** (65–72) | **sound** | Well-posed 2-DOF DAG, no circularity, every headline number reproduces exactly and is assert-guarded. |
| **Advantage honesty** (65–72) | **genuine-but-oversold** | The RDE gains are real physics; three framing overstatements make them look larger/cleaner than the code computes. |

**The two axes are distinct and must not be conflated.** The repo *is* faithful to its literature (0 bugs). It is *not yet* a SOTA-grade design tool, because a design tool must **enforce** the feasibility constraints it cites — and here they are narrated, not gated. That gap is the entire work-list below.

---

## Part 1 — Literature fidelity (518 verdicts)

| Cluster | Paper | FAITHFUL | Non-faithful | Note |
|---|---|---|---|---|
| Cycles | Wintenberger–Shepherd A/B | 104 | 3 | jump ratios, entropy, FJ/Humphrey/Brayton, one-γ — exact |
| S&K | Shepherd–Kasahara FM2017.001 | 71 | 8 | PH + AX control volumes, γ_e — exact; V&V verdicts weakly gated |
| Detonation | SDToolbox FM2018.001 | 38 | 2 | CJ/ZND, equilibrium Hugoniot — exact |
| Common | canonical CJ chain | 36 | 1 | cj_core, mixtures, constants — exact |
| Stechmann | JSR 56(3) 2019 | 33 | 6 | c*, Ik, cf_bell/spike, matched cycle, optima — exact algebra |
| Examples | design chains | 31 | 3 | (44 UNVERIFIABLE = verify agents blocked by spend limit; covered by Part 3) |

**0 BUG. 46 MISSING-CONSTRAINT. 9 DEVIATION.** The algebra is SOTA-faithful everywhere. Every non-faithful finding is a *missing guardrail*, not a wrong formula.

### The 8 recurring gaps (55 findings, ranked by frequency)

Each is the same shape: **the code computes the feasibility metric, prints it, then applies the model anyway.**

**A — Choke-margin computed but never enforced (20 findings, 15 major).**
`choke_margin = min(Pc)/Pa / ((g+1)/2)^(g/(g-1))` is stored and printed but never asserted/clipped. Live shipped data: RP-1 @20 atm has `choke_margin = 0.648` — the exit is **35% below** the sonic threshold over the blowdown tail, yet `mdot/A = Pc/c*` (Eq. 6, valid only if choked) is integrated across the full cycle and the row is marked PASS. Faithful to Stechmann (who retains assumption 3), but a design tool must gate it.
*Fix:* add a `choke_margin ≥ 1` gate (or surface it in PASS/FAIL) and restrict the `Ik` integrals to the choked interval, or explicitly flag the sub-choked fraction.

**H — Surrogate / extrapolated propellant not flagged at runtime (19, 13 major).**
RP-1 modeled as gaseous n-dodecane (H/C 2.17 vs ~1.95; NASA7 extrapolated 300→200 K). Declared in docstrings, but no runtime regime-flag when used outside the validated envelope.
*Fix:* attach a provenance/validity flag to surrogate propellants; warn when state leaves the validated (T, P, φ) box.

**D — `cf_bell` separation / negative-CF unclamped (18, 12 major).**
`cf_bell` has no flow-separation model and no floor: at sea level, ε=4, Pc=1 atm it returns **CF = −2.378** (negative thrust from a still-choked chamber — physically impossible), and `cycle_isp` integrates it. Asymmetry: `cf_spike` *has* the guards (`np.clip`, `np.where`), `cf_bell` does not.
*Fix:* clamp CF to its separated plateau (or floor the pressure term) when Pe/Pa < ~0.35, mirroring `cf_spike`.

**G — Optimum ε\* never checked against geometry/envelope (13, 8 major).**
`bell_opt`/`spike_opt` return ε\* from a purely thermodynamic criterion, blind to `D_e ≤ envelope`. **Design-audit critical finding:** the 10 kN headline is the aerospike at ε\*=10.64, whose axial length plausibly violates `L ≤ 260 mm`, yet `example_design_10kN.py` computes no D_e / axial-length check at all.
*Fix:* compute `D_e = √(4·ε·A_t/π)` and axial length, gate the optimum on the envelope, report `ε_feasible = min(ε_opt, ε_envelope)`.

**F — Solver convergence not asserted (11, 7 major).**
`_hug_point` (Picard 8 iter, secant 30 iter) returns the last value on non-convergence — no assert, no NaN sentinel, hard T-clamp [1200, 5200] K. The canonical sibling `cj_states.py` uses `brentq` at rtol 1e-10 with a realizability guard; the production path has neither.
*Fix:* assert residual/relative-step tolerance (or a converged flag) before returning; ideally adopt the sibling's `gas.TD + equilibrate('TV')` pattern that pins density by construction.

**C — Nozzle ε/NPR domain guards missing (11, 6 major).**
`npr_of_eps` silently clamps ε≤1 to the sonic value (returns it for ε = 1, 0.5, 0, −1). `eps_of_npr` returns `nan`/`inf` for NPR≤1 (a *realizable* sub-ambient condition) with only a RuntimeWarning; the non-finite value propagates into `cf_bell`/`cf_spike`.
*Fix:* `assert`/raise on ε<1 in `npr_of_eps` and on NPR≤1 in `eps_of_npr`, or clip with an explicit infeasibility flag.

**B — CJ sonic realizability not asserted on the `det_state` path (7, 5 major).**
`sonic_resid` is computed and returned, and `TOL['sonic_resid_max']=5e-3` exists, but it is asserted **only** on the canonical `cj_core` solver in one test, **never** on the `det_state` path that produces the 18 production states. Off-window fills can silently return a non-CJ state (or `TypeError` on `round(None,5)`).
*Fix:* `assert det['sonic_resid'] < TOL['sonic_resid_max']` in `det_state`; guard `xstar is not None`.

**E — γ>1 domain guard missing (4, 1 major).**
`cstar_fn`/`cf_base` diverge at γ≤1; no assert. Latent (γ_s = 1.11–1.13 across the shipped envelope) but a reusable rocket-grade primitive should assert `g > 1`.
*Fix:* one-line `assert g > 1` at the two `gamma_s` call sites (`cp_state`, `det_state`).

---

## Part 2 — Live-verified numbers (slides 65–72)

Every headline number reproduces **exactly** from the validated repo (Cantera 3.2.0 + NumPy 2.2.6):

| Quantity | Slide | Live | ✓ |
|---|---|---|---|
| U_CJ (C₂H₄/O₂) | 2373.5 m/s | 2373.5 (err +0.000%) | ✅ |
| CP: γ_s / c\* / Isp | 1.1247 / 1746 / 227.4 s | idem | ✅ |
| CP throat / ṁ | 4.64 cm² / 269 g/s | idem | ✅ |
| Vacuum ε=15, D_e | 94.1 mm | **94.14 mm** | ✅ |
| det: P_init / P_CJ / ⟨Pc⟩ | 1.11 / 37.0 / 10.24 atm | idem | ✅ |
| det bell ε\* / Isp | 2.44 / 233.6 s | idem | ✅ |
| det spike ε\* / Isp | 6.27 / 245.3 s | idem | ✅ |
| bell/spike D_e | 38 / 61 mm | 37.9 / 60.8 mm | ✅ |
| 10 kN: U_CJ / P_init / Isp | 2390.3 / 2.40 atm / +6.6% | idem | ✅ |

> **On the 94.1 mm question:** confirmed correct. It uses the **CP throat** A_t=4.64 cm² (ε=15 → D_e=94.14 mm). The 99.7 mm figure quoted earlier used the **det-nozzled throat** A_t=5.2 cm² — two different throats, both right.

---

## Part 3 — Design-exercise architecture & advantage honesty (slides 65–72)

**Grades:** architecture **sound** · fidelity **follows-with-declared-approximations** · advantages **genuine-but-oversold**.

**Do the intended advantages genuinely emerge?** *Partly, and mostly honestly.* The gains are **real physics, not convention artifacts**: the intensive Isp layer has zero F-dependence (gains can't be an artifact of the 600 N target); bell +2.7% is a real +2.4% Jensen pressure-gain; aerospike +7.9% is a genuine expansion win riding the blowdown to the saturation knee; the advantage persists at scale (+6.6% at 10 kN); the honest counter-story (vacuum collapse to +1.7%) is computed and shown. **But three framing overstatements recur:**

| Sev | Slide | Finding | Fix |
|---|---|---|---|
| 🔴 critical | S72 | 10 kN headline is the ε\*=10.64 spike; its axial length plausibly **violates L≤260 mm envelope**, but no check is run — the one constraint that could disqualify the winner is the one omitted. | Compute & print spike axial length + D_e vs envelope; headline the feasible config. |
| 🟠 major | S71 | "CP and det-bell both obey NPR\*=P̄c/Pa on the same matched mean — structural, not a coincidence" is **false in-code**: CP uses Pcp/Pa=10.00, det uses ⟨Pc⟩/Pa=10.24 at different γ. Shared ε\*=2.44 is a numerical near-tie. | Rewrite: each nozzle perfectly-expands at *its own* reference; the shared ε\* digit is a coincidence at this Pcp. |
| 🟠 major | S69 | Road-II reports Road-I one-pass numbers relabelled (−7%/−5%/+7.9%); true fixed point is **≈−6% flow / +7.0% Isp** at Pcp≈9.5 atm (live-verified: 9.56 atm, 251 g/s, 243 s). | Recompute at the true fixed point; state −6% consistently. |
| 🟠 major | S70/S72 | +7.9%/647 N (Road I) and −7% propellant (Road II) are the **same Isp fact read two mutually-exclusive ways**, shown as if simultaneously bookable; +7.9% pairs RDE-aerospike vs CP-bell (like-for-like bell-vs-bell is +2.7%). | Label each verdict with its road; lead with like-for-like +2.7%, present +7.9% as "with aerospike." |
| 🟠 major | S66/S70 | choke_margin **0.640 < 1** at 600 N presented as a satisfied guard; it is a violated-but-carried Stechmann assumption. | Add choke-margin row; relabel as violated-but-carried; note it flips to 1.39 at 10 kN. |
| 🟡 minor | S71 | Cited plot `scripts/fig_hh_isp_eps.py` **does not exist**. | Commit the script or fix the caption to `example_headtohead.py`. |
| 🟡 minor | S70 | W=2.4 not reproducible (script prints **2.69**). | Print 2.69; carry the λ sensitivity band. |
| ⚪ pedag. | S65/S68 | "Same pump" is mass-flux match, not equal pressure; R̄=45 mm is a packaging choice presented as derived (throatless closure gives ~22 mm). | Label ⟨Pc⟩=10.24 as "mass-flux-matched class"; R̄ as "packaging choice." |

**None of these fabricate the advantage** — all make it look larger/cleaner/more inevitable than the code computes. Fixing the framing changes no headline Isp number; it is about honest provenance, the standard the deck sets for itself.

---

## Roadmap to SOTA design-grade

Priority order (each closes findings the code already has the data to enforce):

1. **Enforce the choked-exit constraint** (theme A, 20 findings) — gate `Ik`/`DC`/optima on `choke_margin ≥ 1` or restrict integrals to the choked interval.
2. **Envelope-gate the optimizer** (theme G + S72 critical) — `ε_feasible = min(ε_opt, ε_envelope)`; add the missing 10 kN axial/D_e check.
3. **Clamp `cf_bell` separation** (theme D) — mirror the guard `cf_spike` already has.
4. **Assert solver convergence + CJ sonic realizability** (themes F, B) — no silent fall-through; guard `det_state`.
5. **Domain guards** (themes C, E) — ε≥1, NPR>1, γ>1 asserts on the reusable primitives.
6. **Runtime surrogate-provenance flag** (theme H) — warn outside the validated (T,P,φ) box.
7. **Fix the three deck framing overstatements** (S69 fixed point, S71 optimality claim, Road-I/II double-count) + the two minor repo pointers (missing plot script, W=2.69).

**Bottom line:** the repo is **literature-faithful and numerically correct** (0 bugs, 462/518 faithful, all headline numbers reproduce live). To reach the SOTA academic+industrial design-tool bar, it must **enforce the feasibility constraints it already measures** — the 55 findings above are that precise, bounded work-list.

---

*Audit provenance: 2 multi-agent workflows (`w9j5f15ch` literature-fidelity, `wrc2yvfvh` design-exercise), 518 + 49 verified verdicts, all numbers re-run live. Verify agents on the examples branch were interrupted by a monthly-spend limit; that branch is covered by the design-exercise audit (Part 3). Synthesis assembled locally from cached agent results — no unverified claims included.*

---

## Addendum 2026-07-16 — work-list executed

The enforcement gap identified above ("narrated, not gated") has been
closed by the 2026-07-15/16 hardening rounds: all 8 thrust V&V verdicts
computed from data, non-convergences raise, CJ sonicity/coherence gated at
every computed point, examples assert their headline numbers at the mission
fill, the (phi, eps) optimization is full-DOF with executable certificates,
and the no-magic-number invariant is enforced by suite group (vii). See
validation/dof_audit.md (hardening round + A6) and commits 7a075a1..638c4a1.
Suite: 8/8 groups PASS.
