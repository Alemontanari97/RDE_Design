# ADVERSARIAL REFUTATION — [SEED-A]

**Hypothesis under audit:** "the ratio of specific heats gamma may be taken CONSTANT across the
whole RDE cycle and expansion for certified thrust claims, with no error bar needed."
**Assessment verdict under audit:** LEGITTIMA-ESATTA.
**Refuter verdict: REFUTED.** The verdict does not survive on any of its three load-bearing
clauses ("constant", "certified", "no error bar needed"). In-repo sources only; no web.

Date: 2026-08-17. Corpus: `literature_review/` (25 papers + reports), `validation/` advisories
named in the brief, `docs/rde_nozzle_PROGRESS.md` POST notes.
Caveat honored: `validation/ADVISORY_litreview_confrontation_2026-08-13.md` is CAVA NON
RATIFICATA — cited below only as pending-ratification evidence, never as decided.

---

## 1. The "no error bar needed" clause is falsified by measured in-repo numbers

**(a) Which constant value of gamma you pick already moves certified-grade thrust numbers by
~3.6–4%.** `validation/gamma_audit.md` (audit a convergenza, 2026-07-08) is dispositive:

- Frozen vs equilibrium gamma of the SAME detonation products at the SAME CJ state:
  gamma_e = 1.1634 vs gamma_fr = 1.2420 for H2/air @ 1 atm/300 K (§2, line 82) — a 6.8% spread
  in gamma itself, and the two are NOT interchangeable: "Con γ frozen, Eq. 19–22 di
  Shepherd–Kasahara non riproducono la loro Table 1" (§4, line 129).
- Measured Isp_f decomposition (§3 table, lines 95–102): swapping gamma frozen → gamma_e in
  SK Eq. 20 alone shifts Isp_f 3203 → 3319 s (**+3.6%**). Fig. 6a checkpoint: 928 m/s with
  gamma_e vs 896 m/s with frozen gamma — the paper's own figure is consistent only with one
  of the two choices (§1.1, line 30).
- A historical in-repo incident proves the risk is real, not academic: the old deck's
  `results_main.json` field *named* `gamma_eq` actually contained the frozen value 1.2420
  (mislabeled; §2, line 82) and propagated wrong thrust numbers into slides (§3.5, lines
  105–111). A hypothesis graded "ESATTA, no error bar" is exactly the epistemic posture that
  produced that defect.

**(b) The frozen/equilibrium caloric-closure spread on the expansion is priced in-repo as a
first-order bracket, not zero.** `literature_review/reports/wintenberger_shepherd_2004_thermo.md`,
finding F7 (lines 276–291): "Independent corroboration that the frozen/equilibrium and γ-choice
sensitivities we price are **first-order, not second-order, effects**", citing the in-repo
[T-EQBR] frozen/equilibrium bracket **+6.3..+7.0%** (line 278), and quoting the paper (p. 15):
"the value chosen for the specific heat ratio has a **strong influence** on the results obtained
for the thermal efficiency in the one-γ model" — Heiser & Pratt's γ = 1.4 vs 1.1–1.2 changes the
numbers materially at identical formulae, and the chemistry effect even *reverses an ordering*
(fuel-air vs fuel-oxygen near stoichiometry, Fig. 19). The report's stated conclusion: "Both
support **our refusal to let γ = const be load-bearing** and our insistence that the frozen
ceiling be **bracketed rather than quoted**." An assessment that says "no error bar needed"
contradicts the repo's own registered pricing of that error bar.

**(c) gamma = const vs gamma(T) moves the OPTIMAL DESIGN, not just the number.**
`literature_review/reports/sun_2019_gamma_var_rao.md` (Sun, Luo & Feng 2019, PDF read in
`literature_review/sun_2019_rao_contour_thermally_perfect_large_area_ratio.pdf`): the whole
constant-γ family (6-value sweep, Table 2) spans only 320.19–321.08 s while the γ(T) closure
reaches 322.00 s at the SAME length with a materially different geometry — β 36.8°→36.1°,
θ_e 8.5°→**12.2°**, area ratio **280:1 → 256:1** (lines 114–120) — and wins at every off-design
point (Table 4, lines 121–123). Report's own synthesis (line 315): "the whole point of the paper
is that **the γ model materially moves the optimum**"; and (line 272) "the risk our E4 flags is
**not academic**." For a certified *thrust-optimal* claim (this program's deliverable), a
gamma-model error is a design-point error, which no post-hoc scalar error bar on thrust can
absorb — a fortiori "no error bar" fails.

## 2. The "constant across the whole cycle AND expansion" clause is not even what the
   permissive literature does

`validation/gamma_audit.md` shows the two thrust-model papers most favorable to the hypothesis
do NOT support "constant across the cycle, exact":

- SK axial-flow model (§1.2): expansion computed on the **equilibrium isentrope** anchored at CJ
  ("the flow is to a reasonable approximation in chemical equilibrium and so that h = h(P,s)
  only") — "Nessun γ costante è coinvolto nel modello numerico" (line 44). The in-repo replica
  reproduces Table 1 within ±0.2% only on the equilibrium isentrope; a frozen expansion "would
  miss by several percent."
- SK one-γ closed form (§1.3): the paper itself grades it "reasonable agreement (**within
  10%**)" against detailed thermochemistry (line 50) — i.e. the source of the constant-γ move
  attaches a ~10% error bar to it. LEGITTIMA-ESATTA claims tighter than the primary source does.
- Stechmann–Heister (§1.4): holds γ constant as **declared assumption 2** ("negligible" —
  an approximation claim, not an exactness claim), with the *value* taken from CEA equilibrium.

So the strongest pro-constant-γ practice in the corpus is: constant-VALUE-of-equilibrium-γ,
declared as an approximation, with the value itself state-dependent (1.13–1.17 across
propellants, gamma_audit §4 table) — never "exact, no error bar."

## 3. The "certified" clause collides with the program's registered epistemic status of γ=const

- `literature_review/reports/VERIFICATION_FABLE_2026-08-13.md` line 154: γ=const appears in the
  program as a "**declared slot**" of a closed-form **fidelity oracle** (GP2001 quasi-1D twin,
  J=∫p dx) — i.e. an oracle/test instance, not a load-bearing hypothesis of certified claims.
- `validation/ASSESSMENT_methodology_position_2026-08-13.md` lines 97–102: the A1 oracle is
  listed as "γ=const" precisely as an adjudicated *instrument*; certified-fidelity claims are
  explicitly flagged as still hypotheses with named falsifiers. Nothing in the assessment
  licenses γ=const as a certified-thrust hypothesis.
- Pending-ratification corroboration (cite as such, NOT decided):
  `validation/ADVISORY_litreview_confrontation_2026-08-13.md` §3.11 (claim 12 / E4, lines
  384–398) records the γ-variable boundary audit as CONFERMATO (EOS-general stationarity is the
  primary object; γ=const is "una scelta di espressione"), and its proposed row D-16 (line 1191)
  would forbid loose γ phrasing at text level. Same direction, weaker tier.
- `validation/ADVISORY_litmap_extension_2026-08-13.md` lines 53–58: Sun 2019 registered as
  "const-gamma contours **systematically off** (~1% Isp at large area ratio)" — the litmap of
  record already carries the anti-hypothesis.

## 4. Steel-manning the assessment — what WOULD survive

The defensible kernel is real and the corpus supports it: a **one-γ model with the equilibrium
products value (1.1–1.15) is a legitimate, literature-standard approximation** for RDE thrust
estimates, good to ~3–10% (SK §1.3; Stechmann §1.4; Eq. 57 KAT in wintenberger report F9). Had
the verdict been "LEGITTIMA-APPROSSIMATA, with declared value choice (equilibrium, not frozen)
and a derived error bar of order 3–10% (bracketed frozen/equilibrium)", it would be confirmable
from this corpus. But the verdict as issued asserts EXACTNESS and NO ERROR BAR — both clauses
are contradicted by measured in-repo numbers (+3.6% γ-swap; +6.3..+7.0% bracket; ~10% the
source's own grade; design-point migration in Sun 2019). No reading of the corpus rescues
"ESATTA".

## 5. Verdict

**REFUTED.** Surviving objections, ranked:

1. Measured first-order sensitivity: γ-choice (frozen vs equilibrium at CJ) shifts Isp_f +3.6%
   and the frozen/equilibrium expansion bracket is +6.3..+7.0% — incompatible with "no error
   bar needed" (`validation/gamma_audit.md` §2–§3; wintenberger report F7).
2. The primary sources themselves grade constant-γ as an approximation: SK one-γ "within 10%";
   Stechmann assumption 2 "negligible" (declared, not proven exact); SK's actual numerical model
   uses an equilibrium isentrope with NO constant γ (`validation/gamma_audit.md` §1.2–1.4).
3. γ=const vs γ(T) moves the thrust-OPTIMAL contour itself (AR 280:1→256:1, θ_e 8.5°→12.2°,
   off-design ordering) — a scalar error bar cannot certify a design claim, and "no error bar"
   a fortiori cannot (sun_2019 report lines 114–123, 266–272, 315; litmap_extension lines
   53–57).
4. In-repo precedent of harm: the mislabeled `gamma_eq`-is-actually-frozen field propagated
   ~3.5%-low thrust curves into the deck — the exact failure mode "ESATTA, no error bar"
   invites (`validation/gamma_audit.md` §2 line 82, §3.5).
5. Program status of record: γ=const is registered ONLY as declared-oracle/demoted-corollary
   material (VERIFICATION_FABLE line 154; ASSESSMENT lines 97–102), never as a load-bearing
   hypothesis of a certified number; pending-ratification confrontation §3.11/D-16 points the
   same way.

**Repair path for the bundle:** restate SEED-A as "one-γ (equilibrium products value) is a
DEMOTED COROLLARY / oracle-grade closure with bracketed error [frozen, equilibrium] = derived
bar; primary route stays EOS-general γ(T)" — that restatement is confirmable from this corpus.
