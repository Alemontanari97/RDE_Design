# ADVERSARIAL REFUTATION ATTEMPT — [EULER-GSEP] verdict LEGITTIMA-DICHIARATA-MONITORATA

**Role:** adversarial refuter, S-FOUNDATIONS (R35) hypothesis audit. **Date:** 2026-08-17.
**Target:** `validation/sfoundations_raws_2026-08-13/hypaudit/confront_euler.md` (read in full).
**Sources:** IN-REPO ONLY. `ADVISORY_litreview_confrontation_2026-08-13.md` cited strictly as
**pending-ratification evidence (CAVA NON RATIFICATA)**, never as decided.

**OUTCOME: NOT REFUTED.** The verdict survives the citation-accuracy attack, the internal-logic
attack, and the absence attack. Four objections survive as monitor/residual amendments; none
flips LEGITTIMA-DICHIARATA-MONITORATA on Q1 or Q2. Detail below.

---

## 1. Citation-accuracy attack (spot-verification of every load-bearing quote): PASSED

Each evidence bullet was re-checked against the file where the read of record lives:

| Claim in assessment | Verified against | Result |
|---|---|---|
| Kraiko 2001: Euler core, viscosity only via empirical Eq. (4); "not more reliable" quote; x_e = 75/80/85/90 insensitivity instrument; A-1 adoption queued | `reports/kraiko_2001_plug.md` lines 33, 38, 52, 60-61, 140 | EXACT |
| Harroun 2021 F2: Eq. (9) residence-time mechanism; conservative direction "on this instance"; Strouhal admission audit + (f,t_res) reparameterization as the two named repairs; falsifier "an instance where quasi-steady g_sep is anti-conservative" | `reports/harroun_2021_jpp_nozzle_perf.md` lines 351-364, 475, 591-593 | EXACT |
| Harroun 2021: delayed separation asserted/computed, not experimentally confirmed ("not densely located enough downstream", p. 670) | same report, line 624-626 + `VERIFICATION_FABLE_2026-08-13.md` Stage 4 | EXACT |
| Miki 2020: ~12% Isp / ~17% gross-thrust validation error vs 3.2% claimed improvement; turbulence-model validity undischarged for "unsteady, shock-containing, separating" flow | `reports/miki_2020_nasa_methodology.md` Hyp. 12/15 (lines 80-83) + A-3 (lines 232-237) | EXACT |
| Teasley 2023: "off-design separation across the throttle band... T-T3 caps to the attached segment" | `reports/teasley_2023_nasa_state.md` line 165 (Net verdict #2) | EXACT |
| ADVISORY choking §4-bis: HONEST GAP verbatim; "never claimable from the inviscid tool" | `validation/ADVISORY_rde_choking_2026-08-11.md` lines 337-347 | EXACT |
| Inviscid-only-ours risk / evaluators informationally incomparable | `validation/ASSESSMENT_methodology_position_2026-08-13.md` §2; independently corroborated by `reports/REFUTE_B_harroun_requalification.md` Linea (4) (lines 154-172: "il rischio INVISCIDO — NOSTRO e NON condiviso... i due valutatori sono informationalmente INCOMPARABILI") | EXACT, and the assessment carries it (T4/M5/R-c) rather than hiding it |

No misquote, no direction-flip, no evidence-grade inflation found. Notably the assessment
already downgrades its own most favorable fact (separation delay) to
computed-not-measured-instance-only (M4, R-a) — the standard overclaim channel is closed.

## 2. Internal-logic attack: PASSED

- **Q1 tri-leg structure holds.** Precedent (Kraiko school) + alternative-not-certifiable
  (Miki Hyp. 15 is *load-bearing for the paper's own headline and never stated* — the RANS
  route currently ranks 3.2% deltas inside a 12-17% validation error) + prior internal
  adjudication (choking §4-bis) are three independent legs; killing any one leaves two.
- **Q2 argument is not circular.** The claim "modeling separated operation at certified rigor
  is unavailable" rests on the corpus's own statements (Harroun 2020 F2 "no way to create an
  analytical model predicting the base pressure", F7 sign-wrong classical closure, Harroun
  2021 p. 669 non-axisymmetric migrating separated region), and the optimizer-drift evidence
  (Fernandes Hyp. 10, Ornano constraints table) makes the constraint load-bearing, not
  decorative. Verified in the respective reports.
- **The verdict prices its own cost.** T3/R-b concede the attached-every-phase feasible set may
  be small or empty for sea-level record hardware and demand the scope cap be printed. A
  verdict that prints its cap is not overclaiming on the channel where the corpus is harshest.
- **The grade is the middle one.** The assessment explicitly rejects LEGITTIMA-ESATTA and
  argues why not CONDIZIONATA/DA-RISCOPARE. On this corpus that adjudication is correct:
  no in-repo source contradicts Euler-with-declared-viscous-layer *as a design core*; every
  hostile fact attacks either the closure's calibration or the claim perimeter, both of which
  are fenced (R2 wording, T3-CONTROL, M1-M6).

## 3. Absence attack (the assigned hunt): what the assessment did NOT consider

Systematic sweep of the 15 corpus items absent from the assessment's source table
(ancourt 2023, giles-pierce 2000/2001, janc 2025, kaemming-paxson 2018, kraiko-tillyaeva
2004/2015, liu 2022, paxson-miki 2022, rubino 2018, schotthofer 2024, sun 2019, teasley 2025,
wintenberger-shepherd 2004, zahr-persson, + REFUTE_A/C/D, 00_APPARATUS_BRIEF,
ADVISORY_mean_swirl) via separation/viscous/attachment/base-pressure grep + targeted reads.
Findings, graded by whether they could flip the verdict:

**AB-1 (does NOT flip; enriches M6) — In-corpus quantified base-drag anchors ignored.**
[Paxson-Miki 2022] (`reports/paxson_miki_2022_nasa_opt.md`, F9, ALTA): measured base drag of a
**truncated plug under genuine RDE cycle flow** = **−9.5% of nozzle thrust (−1.4% of total)**,
p. 10 — "the exact object PB-2 studies", with the report's own note that the paper "offers no
base-pressure model... simply measures the drag and accepts it". [Liu 2022]
(`reports/liu_2022_aerospike_rde.md`, F12, ALTA): base pressure ≈ 0.16 atm vs P_a = 0.36 atm
(44% of ambient), base drag ≈ 0.65% of total thrust at 40% truncation. [Kaemming-Paxson 2018]
(pending-ratification confrontation A31): base-force subtraction protocol; the 12%/38% figures
are an undocumented order-of-magnitude warning, not a band. The pending-ratification C28 row
mandates keeping the three magnitudes in **separate geometric classes**, never summed or
substituted. Why it does not refute: magnitudes are not a predictive model — Harroun 2020 F2's
"no base-pressure model exists" stands (verified verbatim in the report), and these anchors
*strengthen* the declared-band route (M6) rather than the model-the-separated-state route.
But M6's MODEL-CONST 0.20 [0.20-0.40] currently ships without its two in-corpus calibration
anchors and without the class-separation discipline. **Surviving objection SO-1.**

**AB-2 (does NOT flip; enlarges R-d) — The named calibration carrier for g_sep itself.**
[Sun 2019] (`reports/sun_2019_gamma_var_rao.md`, references section, line ~348-349): Östlund &
Muhammad-Klingmann, *Applied Mechanics Reviews* 58(3):143-177, 2005 — flagged in-repo as "the
standard separation review; **relevant to our g_sep state constraint**". Unprocured. The
assessment's R-d names only the Harroun thesis and the Mueller NASA reports as the absent
calibration base; the standard steady separation review — the natural calibration corpus for
the *criterion class itself* (Kraiko's Eq. (4) is the Abramovich lineage of exactly this
literature) — is a named in-repo pointer left out of the residual list. It also softens the
rhetorical edge of "no dataset to calibrate against" (Harroun 2020 F6 is about the *RDE line*;
the steady criterion class has a classical calibration literature, named on file). Why it does
not refute: an unread review cannot flip a verdict; it can only extend the procurement
residual. **Surviving objection SO-2.**

**AB-3 (does NOT flip; sharpens M6) — The skin-friction debit is missing from the declared
band list.** The hypothesis says "viscous effects = declared model layer", and M6 names BL
*displacement* and base/truncation — but the corpus quantifies a third viscous-layer term the
assessment never mentions: wall shear / friction drag. [Sun 2019] Table 5 (report §3): D_w ≈
36.97-37.71 N against F_v ≈ 742 N — **≈5% of vacuum thrust** on a large-area-ratio nozzle,
larger than the 3.2% design deltas the certified tool is meant to resolve. [Miki 2020] Hyp. 16:
"pressure-only thrust accounting on a viscous field" is a named defect in the NASA route (wall
shear computed and plotted, never budgeted). A declared viscous layer whose band list omits
its potentially largest attached-flow term is an incomplete M6, though the *architecture*
(bands outside the certificate) is unchanged. **Surviving objection SO-3.**

**AB-4 (does NOT flip; grades T5 finer) — The Harroun base-drag magnitude is contested;
the sign is not.** Pending-ratification confrontation C28/C29: the headline "8x base drag"
comes from the least grid-converged configuration of the study and is contested by Schwer et
al. (private communication of 2021-01-05 cited in the paper itself); what carries experimental
corroboration is the ejector-suction **sign/mechanism** (0.59 vs 0.95 atm, cross-campaign,
cross-fuel). The assessment's T5/F7 use ("Pb/Pa = 1 sign-wrong by measurement") relies only on
the sign — so the leg stands — but the evidence-grade split (sign corroborated / magnitude
contested) should be printed wherever T5 is quoted. **Surviving objection SO-4.**

**AB-5 (null results, reported for completeness).** Giles-Pierce 2000/2001, Ancourt 2023,
Janc 2025, Rubino 2018, Schotthöfer 2024, Zahr-Persson: adjoint/numerics papers, no
separation/attachment content bearing on the verdict (grep-verified). Kraiko-Tillyaeva
2004/2015: no separation content beyond the Kraiko-2001 lineage already carried.
Teasley 2025 (`reports/teasley_2025_rdre_dev.md` F-2/F-3): hardware nozzle sweeps run with
"g_sep absent and no attachment condition imposed analytically" — a further instance of the
field designing without the constraint, i.e. *supports* §1 of the assessment. Wolanski 2013:
as stated in the source table. ADVISORY_mean_swirl_panel: no separation-bearing rows (the
swirl-KE debit line is an objective-side issue, not a g_sep issue). REFUTE_A/C/D: symmetry,
cone form, slip *line* (shock-discontinuity class, R16) — unrelated to wall-BC slip/separation.
Ornano C16 (pending-ratification): the DE-optimum on viscous RANS and the Rao MoC contour
agree to ≈0.02% in mass-averaged exit force — if anything, in-corpus evidence *for* the
adequacy of inviscid design cores on attached flow.

**AB-6 (checked and rejected as an attack) — "The precedent is steady; the hypothesis is
cyclic."** True (Kraiko/Hoffman/Sun are all steady single-point), and it is the strongest
abstract objection to §1's precedent leg. But the assessment does not hide it: T1 states the
quasi-steady form is exactly what the RDE record attacks, and M1 (Strouhal/residence-time
admission audit, from Harroun 2021 F2's own named repairs) plus the pending-ratification A32
row (f_cycle as a mandatory CycleFamily field consumed by the g_sep hook — the physical period
is currently dimensionally cancelled by the normalized-μ contract) are the exact counter-
measures. The objection is already priced; citing A32 would strengthen M1's implementability,
but nothing here overturns.

## 4. Verdict of this refutation

**refuted = FALSE.** Every load-bearing citation is accurate; the tri-leg Q1 argument and the
Q2 constraint-form argument survive; the absence attack found only *supplementary* corpus
content (base-drag anchors, friction debit, the Östlund pointer, the sign/magnitude grade
split, the A32 f_cycle hook), all of which refines monitors M6/M1 and residual R-d without
touching the verdict class. No in-repo source asserts, shows, or prices Euler-core +
declared-viscous-layer + attached-flow-constraint as illegitimate for certified claims *within
the printed scope cap*; the corpus's harshest facts (record hardware outside H2'; evaluator
incomparability) are already carried inside the assessment as T3/T4 with monitors M3/M5.

**Surviving objections (amendments owed, not verdict changes):**
- **SO-1**: M6 must cite its in-corpus calibration anchors — Paxson-Miki 2022 F9 (−9.5%
  nozzle thrust, truncated plug, genuine RDE cycle) and Liu 2022 F12 (P_b/P_a ≈ 0.44, 0.65%
  of thrust) — with the C28-style (pending-ratification) three-class separation discipline
  (mechanism/anchor/protocol, never cross-class).
- **SO-2**: R-d must add Östlund & Muhammad-Klingmann 2005 (named in-repo at
  `reports/sun_2019_gamma_var_rao.md` refs as "relevant to our g_sep state constraint") to the
  unprocured calibration carriers; correspondingly soften "no dataset to calibrate against" to
  its true perimeter (no *RDE-line* dataset).
- **SO-3**: M6's band list must include the skin-friction/wall-shear debit (in-corpus anchors:
  Sun 2019 D_w ≈ 37 N ≈ 5% of F_v; Miki 2020 Hyp. 16 pressure-only accounting defect) — an
  attached-flow viscous term of magnitude above the 3.2% design deltas.
- **SO-4**: wherever T5/F7 is quoted, print the evidence-grade split: ejector-suction *sign*
  experimentally corroborated (cross-campaign, cross-fuel); the 8x *magnitude* from the least
  grid-converged configuration and externally contested (Schwer) — per pending-ratification
  C28/C29.

**Limits of this refutation:** grep-guided coverage of the 15 uncited corpus items plus
targeted full reads; pending-ratification confrontation rows used only as amendment evidence,
never as decided; no web sources (per brief).
