# HYPOTHESIS AUDIT [EULER-GSEP] — Euler core + declared viscous layer + attached-flow constraint

**Session:** S-FOUNDATIONS (R35), Phase C-adjacent hypothesis audit. **Date:** 2026-08-17.
**Hypothesis as posed:** COMPRESSIBLE EULER CORE with slip walls; viscous effects = declared
model layer; separation margin `g_sep` as a declared empirical criterion class (R2) keeping
every phase attached.
**Questions:** (Q1) Is Euler-with-declared-viscous-layer legitimate for certified thrust
claims? (Q2) Is an attached-flow state constraint the right form (vs. modeling separated
operation)?
**Sources:** IN-REPO ONLY. Papers cited as [Author Year] + file where the read of record
lives. `ADVISORY_litreview_confrontation_2026-08-13.md` is cited only as
**pending-ratification evidence (CAVA NON RATIFICATA)**, never as decided.

**VERDICT: LEGITTIMA-DICHIARATA-MONITORATA** (both Q1 and Q2), with named monitors and a
hard never-claim list. Reasoning below.

---

## 1. The precedent side: Euler + empirical separation closure IS the record method of the strongest school

**[Kraiko 2001]** (`literature_review/reports/kraiko_2001_plug.md`, §3 "Flow model" +
Hypotheses 6-7, 12-13) is the direct structural precedent for the hypothesis exactly as
posed:

- Flow model: "Steady, inviscid, supersonic, planar ... **Viscosity enters only in the
  off-design evaluation, through an empirical separation criterion**" (report §3).
- The criterion is a declared empirical class, not a viscous solve: Eq. (4)
  `p_cr/p = 1 + 0.2 k M² / (M² − 1)^{1/4}` (Abramovich lineage, Refs. 38-40), plus an
  experimental separation-distance correlation.
- The school's own defense of the class (report Hypothesis 6, quoted from the paper):
  *"Such closure equations, however, are actually not more reliable than formula (4) for
  separations caused by interaction of shocks with a turbulent boundary layer"* — i.e. the
  RANS alternative is asserted by the owning school to buy **no** additional reliability for
  this failure mode.
- Crucially, the paper ships the **instrument** that makes the empirical closure honest: an
  explicit separation-point **insensitivity study** (x_e = 75/80/85/90 vs x_o ≈ 92) with the
  verdict "the thrusts values R and R_Σ are practically independent from the separation
  zone's size" even though the pressure distribution depends on it strongly (report §3
  "Verification"). Our own report queues this as adoption A-1 ("empirical separation closure
  Eq. (4) plus a pre-registered separation-point insensitivity instrument", report §
  Adoptions, line ~95).
- The report also flags the honest residues we inherit with the precedent: Hypothesis 12
  (boundary-layer displacement outside the separated zone negligible for thrust — *asserted*,
  defended only via the insensitivity study) and Hypothesis 13 (Eq. (4) validity assumed over
  the encountered Mach range).

**[Hoffman 1987]** (`hoffman_1987_ctp.md`, H-u2): the CTP line is "full-flowing,
shock-free-at-exit, supersonic-exit ... no separation model" — the classical
compressed/truncated nozzle literature designs on the inviscid core and does not even carry
a criterion. **[Kraiko 2016]** (`kraiko_2016_two_sided.md`, Hypothesis 4): attached flow in
the design regime "asserted a posteriori for nozzle 5 only, not [checked in general]" — the
Euler-verification norm of the field is *weaker* than our hypothesis, which promotes
attachment to a per-phase state constraint.

**Cautionary counter-precedents (what happens without the constraint):**
**[Fernandes 2023]** (`fernandes_2023_moc_shapeopt.md`, Hypothesis 10 + line ~239):
separation-blind MoC optimization runs `p_e = 1 atm` contours against overexpanded ambients
with "No separation criterion" — our report classifies the route as "γ = const, planar,
shock-free, **separation-blind**" and treats that as a defect, not a convenience.
**[Ornano 2017]** (`ornano_2017_pde_shapeopt.md`, constraints table): "No aerodynamic/state
constraints ... no separation constraint", box bound ACTIVE at the reported optimum, and
"mild flow separation near the outlet" appears in their own Fig. 8 — an unconstrained
inviscid-ish optimizer drifts to the feasibility boundary. These two are the in-corpus
demonstration that the `g_sep` constraint is **load-bearing for the optimizer**, not
decoration: without it, thrust-maximization actively seeks the separated boundary.

**Conclusion of §1:** the hypothesis is not an internal preference; it is the method of
record of the strongest classical school (Kraiko line), *upgraded* by us from a-posteriori
evaluation to an in-design constraint. Q1 has a direct literature basis.

## 2. The threat side: what the RDE record says against the hypothesis

The threats are real, all already registered in the repo record, and none of them
overturns the form — they price it and bound its claims.

**T1 — `g_sep` is history-dependent, not pointwise-in-phase.** [Harroun 2021]
(`harroun_2021_jpp_nozzle_perf.md`, §3b + Finding F2, ALTA): Eq. (9)
δ_m = 2√(μ t_res/(ρπ)) (Stewartson/Rayleigh-layer argument, paper p. 670); waves reintroduce
high-momentum products every 72 μs, preventing boundary-layer thickening and "moving the
flow separation point downstream"; Fig. 20 shows the separation point migrating
upstream-then-downstream **within one cycle**. Our (P) writes `g_sep(S; s(ξ)) ≤ 0`
pointwise in phase — the physics says onset depends on (f, t_res), not on the instantaneous
phase state alone. The report names the two repairs (F2): (i) a **Strouhal/residence-time
admission audit** for the quasi-steady form, or (ii) reparameterize `g_sep` by (f, t_res).
And it records the sign: "unsteady forcing *delays* separation, so the pointwise
quasi-steady g_sep is **conservative** on this instance" — a defensible interim position
("conservative closure with a named, cited direction of error"), not a defect.

**T2 — The empirical closure is uncalibrated in the corpus's best attempt.** [Harroun 2020]
(`harroun_2020_validation.md`, Finding F6, ALTA): the purpose-built experiment for `g_sep`
and `p_b` "closes **neither**" — ramp ports at only 6 stations, "not enough resolution in
the experimental pressure port locations" to confirm the separation trend (paper p. 9,
Conclusion 2 p. 11). Verdict of record: "Any g_sep we ship is a **modelling choice with a
falsifier, not a validated closure**." The delayed-separation status is "computed result,
not measured" — CONFIRMED and sharpened at verification
(`reports/VERIFICATION_FABLE_2026-08-13.md`, Stage 4, line ~299).

**T3 — Record sea-level RDE hardware sits OUTSIDE the attached regime.** [Harroun 2021]
(Finding F1: both experimental discriminators are "separated / recirculating /
ambient-coupled"; record test articles sit **outside H2'**) and [Harroun 2020] (Finding F5,
ALTA: chamber pressure sweeps ≈2.2→30 atm within one cycle against fixed sea-level ambient;
64% of the cycle below CTAP; open/closed-wake transition at Pa/Pc ≈ 0.15 crossed *within*
the cycle — "μ(Ξ_sub) > 0 is the generic RDE case, not a corner"). [Teasley 2023]
(`teasley_2023_nasa_state.md`, Net verdict #2): "off-design separation across the throttle
band (F4 → g_sep and the two-regime contract are load-bearing, **T-T3 caps to the attached
segment**)". So the attached-flow constraint, applied at sea level to record-class
hardware, restricts (P) to a regime that record hardware ordinarily violates — the
hypothesis buys certifiability at the price of a scope cap, and the cap must be printed.

**T4 — The inviscid-only-ours ranking risk.**
`validation/ASSESSMENT_methodology_position_2026-08-13.md` §2 (REFUTE_B requalification,
lines ~46-52): comparisons against the field's RANS evaluators carry "il rischio
**INVISCIDO solo nostro** (il loro valutatore vede la separazione, il nostro no)" —
rankings produced by our evaluator and by viscous ambient-coupled evaluators are
incomparable where separation is the discriminating physics. [Harroun 2020] Finding F3 +
the binding **PROTOCOL T3-CONTROL** (F1/F3, line ~140): we may "not claim the
cycle-averaged objective ranks *cowl-coupled, base-coupled, separated* configurations —
that is outside its declared regime."

**T5 — Separated operation has NO certifiable model to import.** [Harroun 2020] F2 (ALTA):
"there is no way to create an analytical model predicting the base pressure — and thus the
base drag — with respect to the operating conditions" (paper p. 7); Stechmann's linear model
shown failing at high ṁ. F7 (ALTA): the classical open-wake closure Pb/Pa = 1 is **wrong in
sign for RDE, by measurement** (ejector suction, Pb < Pa in open wake). [Harroun 2021]
p. 669: "The separated flow region for the RDE had a complex geometry, contrary to the
axisymmetric separated flow geometry expected" — separated RDE operation is 3-D, unsteady,
and modelless in the corpus. [Miki 2020] (`miki_2020_nasa_methodology.md`, Hypotheses
12/15): even the production RANS route carries undischarged turbulence-model validity for
"unsteady, shock-containing, separating" flow and a ~12-17% validation error against 3.2%
design separations — viscous CFD does not currently deliver *certified* thrust on separated
states either.

## 3. Adjudication

### Q1 — Euler core + declared viscous layer, for certified thrust claims: LEGITTIMA-DICHIARATA-MONITORATA

The literature record supports the hypothesis **in the declared-and-monitored form it is
already posed in**, on three legs:

1. **Precedent** (§1): the Kraiko school designs on Euler and closes separation empirically,
   with the school's own printed argument that RANS closures are not more reliable for
   shock/turbulent-BL separation [Kraiko 2001, Hyp. 6]; classical CTP/Rao lines carry no
   separation model at all [Hoffman 1987 H-u2].
2. **The alternative is not certifiable either** (§2 T5): viscous CFD on the separated RDE
   states carries 12-17% validation error [Miki 2020] and one-3D-transient-geometry-per-study
   cost [Harroun 2020 F9]; there is no base-pressure model in the corpus [Harroun 2020 F2].
   Moving the core from Euler to RANS would import an *uncertifiable* closure into the
   certified layer — strictly worse for R5-grade claims than a declared model layer outside
   the certificate.
3. **The record already adjudicated this internally, consistently with the literature**:
   `ADVISORY_rde_choking_2026-08-11.md` §4-bis declares it as the program's "**HONEST GAP —
   separation is viscous, the machinery is inviscid**; ... Declared scope limit of record;
   option = correlation-based separation-margin constraint at design level (CONSERVATIVE for
   RDE per Harroun's computed cycle-averaged-CFD delay; experimentally UNCONFIRMED at the
   separation location)". The hypothesis under audit is exactly this adjudicated option.

It is **not** LEGITTIMA-ESATTA: `g_sep` is an uncalibrated empirical closure (T2), its
pointwise-in-phase form is only *conservative-on-one-computed-instance* (T1), and the
viscous displacement correction to thrust is asserted-not-proved even in the precedent
[Kraiko 2001, Hyp. 12]. It is not CONDIZIONATA-only, because the conditioning (attached,
full-flowing, supersonic-exit-every-phase = H2') is **internal to the hypothesis itself**
via the `g_sep` constraint — the validity window is enforced by the formulation, not merely
assumed; what remains external is monitoring plus a never-claim list. It is not
DA-RISCOPARE: no in-repo source contradicts Euler-with-declared-viscous-layer *as a design
core*; the sources contradict only (a) unqualified extension of its claims to separated /
base-coupled regimes (fenced by T3-CONTROL) and (b) treating `g_sep` as validated (fenced by
the R2 "declared empirical criterion class" wording).

### Q2 — Attached-flow state constraint vs. modeling separated operation: the constraint is the right form

- **Modeling separated operation at certified rigor is not available in the corpus, by the
  corpus's own statement** (T5): no base-pressure model exists [Harroun 2020 F2], the
  classical closure is sign-wrong for RDE [F7], the separated region is non-axisymmetric
  and phase-migrating [Harroun 2021 pp. 669-670]. A "model the separated phase" branch
  would put an unfalsifiable closure inside the certificate — an R5 violation by
  construction.
- **The constraint form has the strongest precedent and is an upgrade on it**: Kraiko 2001
  constrains nothing and only *evaluates* off-design separation a-posteriori; Kraiko 2016
  asserts attachment a-posteriori for one nozzle; Fernandes/Ornano show what optimization
  without the constraint does (drives to the separated boundary). Putting `g_sep ≤ 0`
  μ-a.e. *in the design problem* is the only form in this corpus that makes
  "every phase attached" a checkable property of the optimum rather than a hope.
- **The cost is a scope cap, and it must be printed** (T3): for sea-level record-class
  hardware, the attached-every-phase feasible set may be small or empty (64% of cycle below
  CTAP; mode transition within the cycle). The two-regime contract + robust/mode-measure
  layer [Harroun 2020 F5, Teasley 2023 F3/F4] is where separated operation lives — as a
  declared out-of-(P) regime with monitors, not as a modeled state.
- **Favorable-direction note, usable but not bankable**: the RDE-specific physics
  (cycle-forced boundary layer) *delays* separation vs. the steady criterion [Harroun 2021
  §3b], so the quasi-steady `g_sep` constraint is conservative on the one computed instance
  — the constraint form errs on the safe side for RDE. The converse benefit (raising
  ε_max because of the delay) is "never claimable from the inviscid tool"
  (`ADVISORY_rde_choking` §4-bis, verbatim).

## 4. Monitors required (the "MONITORATA" content)

M1. **Strouhal/residence-time admission audit** for the quasi-steady `g_sep` form: check
    t_res vs 1/f per design instance; regimes failing the audit are declared outside (P)'s
    scope or `g_sep` is reparameterized by (f, t_res) [Harroun 2021 F2 repairs (i)/(ii)].
M2. **Separation-point insensitivity instrument** (pre-registered, Kraiko-2001-style A-1):
    thrust recomputed under perturbed separation location; certified thrust claims only
    where the Kraiko-type insensitivity verdict holds.
M3. **Per-phase H2' monitor**: supersonic-exit / full-flowing / positive `g_sep`-margin
    check at every phase of every candidate; any phase failure routes the design to the
    two-regime contract, out of the certified claim [Harroun 2020 F5; Teasley 2023 F4].
M4. **`g_sep` falsifier of record**: the closure ships as a modeling choice with a named
    falsifier and its calibration debt printed ("no dataset in this line to calibrate it
    against", Harroun 2020 F6) + conservative direction cited with its evidence grade
    (computed, methane CFD, experimentally unconfirmed at the separation location).
M5. **T3-CONTROL claim fence**: no ranking claim over separated / base-coupled /
    cowl-coupled configurations; the counter-example (Harroun) named in every external
    presentation [Harroun 2020 F1/F3 binding obligation].
M6. **Viscous model-layer band declared**: BL displacement thrust correction and
    base/truncation carried as declared MODEL-CONST bands (trunc 0.20 [0.20-0.40], ADR D4),
    never inside the certificate [Kraiko 2001 Hyp. 12; ADVISORY_rde_choking §4-bis].

## 5. Residual risks (named, not discharged by this audit)

R-a. `g_sep` conservatism is instance-proved only (one methane CFD computation,
     experimentally unconfirmed); a regime where cycle forcing *promotes* separation would
     flip the safe direction — no in-corpus evidence either way beyond Harroun.
R-b. Sea-level certified claims for record-class hardware may have a small/empty attached
     feasible set (64%-of-cycle overexpansion; in-cycle mode transition): the hypothesis
     caps the application, it does not serve it there.
R-c. Rankings against viscous evaluators are incomparable where separation discriminates
     (inviscid-only-ours risk, ASSESSMENT §2) — R22 (3D-unsteady vs 3D-averaged vs
     2D-averaged) is the deciding experiment and is ours to run.
R-d. Harroun M.S. thesis (Purdue 2019), the actual carrier of the cycle-averaged
     evaluation threat, is UNREAD (procurement P0, VERIFICATION Stage 4 R2); Mueller NASA
     reports [15][16] (classical separated-flow carriers) unprocured — the calibration base
     for `g_sep`/CSTR_PB could shift when read.
R-e. Pending-ratification note: `ADVISORY_litreview_confrontation_2026-08-13.md` (CAVA NON
     RATIFICATA) carries consistent supporting rows (e.g. inviscid-model sign-correctness
     bar at line ~1066; mean-designed-nozzle blindness framing) — nothing in it contradicts
     this verdict, but none of it is citable as decided until ratified.

## 6. Source table

| Source | File (where read) | Role here |
|---|---|---|
| [Kraiko 2001] | literature_review/reports/kraiko_2001_plug.md | Direct precedent: Euler + empirical separation Eq. (4) + insensitivity instrument |
| [Hoffman 1987] | reports/hoffman_1987_ctp.md | Classical line: full-flowing, no separation model (H-u2) |
| [Kraiko 2016] | reports/kraiko_2016_two_sided.md | Attachment asserted a-posteriori (Hyp. 4) — weaker than our constraint |
| [Fernandes 2023] | reports/fernandes_2023_moc_shapeopt.md | Separation-blind optimization = named defect (Hyp. 10) |
| [Ornano 2017] | reports/ornano_2017_pde_shapeopt.md | No separation constraint → optimizer at box boundary, separation in own figures |
| [Harroun 2020] | reports/harroun_2020_validation.md | F2/F5/F6/F7: no base model; μ(Ξ_sub)>0 generic; g_sep uncalibrated; Pb/Pa=1 sign-wrong; T3-CONTROL |
| [Harroun 2021] | reports/harroun_2021_jpp_nozzle_perf.md | F1/F2/F3: outside-H2' hardware; g_sep history-dependent, conservative direction; migrating separated region |
| [Miki 2020] | reports/miki_2020_nasa_methodology.md | RANS route: 12-17% validation error on separating flow (Hyp. 12/15) |
| [Teasley 2023] | reports/teasley_2023_nasa_state.md | Throttle-band separation priced; T-T3 caps to attached segment |
| [Wolanski 2013] | reports/wolanski_2013_survey.md | Survey presupposes attached/adapted; separation not modelled in RDE survey line |
| VERIFICATION | reports/VERIFICATION_FABLE_2026-08-13.md | Separation-delay = computed-not-measured, confirmed; thesis procurement P0 |
| ADVISORY choking | validation/ADVISORY_rde_choking_2026-08-11.md | §4-bis HONEST GAP adjudication of record; never-claim clause |
| ASSESSMENT | validation/ASSESSMENT_methodology_position_2026-08-13.md | Inviscid-only-ours risk; R22 as decider |
| ADVISORY litmap ext. | validation/ADVISORY_litmap_extension_2026-08-13.md | Mean-designed nozzle vs delayed-separation framing (lines 78-79) |
| ADVISORY confrontation | validation/ADVISORY_litreview_confrontation_2026-08-13.md | PENDING RATIFICATION — consistent, not decided |
