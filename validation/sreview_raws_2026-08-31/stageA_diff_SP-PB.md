# STAGE A — DIFF JUDGEMENT, SP-PB: BASE REGION (truncated-base model and its uncertainty band vs the materiality threshold)

Judge: DIFF judge SP-PB (NOT agnostic; persona = JPP referee who judges the decisive number + PM). Date 2026-09-05.
Inputs read integrally: the four trees `stageA_tree_{variational,hyperbolic,optimization,propulsion}.md`;
`PROBLEM_STATEMENT_agnostic.md`; `DERIVER_BRIEF_agnostic.md`; `INCUMBENT_pointers.md` and every SP-PB anchor it
cites (ledger C61 `docs/choice_ledger.yaml:818-831`; decision map Stage 8 rows H20/C61/DUTY-10
`docs/rde_nozzle_pipeline_decision_map.md:181-186` + E11/E12 :217-218; `BASE_PRESSURE_HARVEST_c4.md` §1-§15 +
CONSOLIDATED; `ADR_panel_2026-07-16.md:126-146`; TWIN protocol §1-§9 (item §5.4); M0 channel (v)/(vi) row :1347
+ [ORCH-HARV-2]/[ORCH-HARV-3] :1430-1463 + T-T4 sharpness :2316-2319; problem book PB-2 :532-536 + sector (ii)
:347-348; D6 F3/F4b :214-251, G2 :776-782, DUTY-10 :435-439, Annex B :1142; findings rows
`litreview:residue-r8-r23-base-pressure-pb2-blocking` :2263 (path critical) and
`plume:free-boundary-solve-mechanics-missing` :2728 (path critical); lit registry rows humphreys_1971 :364,
vander_veen_1974 :428, onofri_2002 :436, harroun_2020 :633, harroun_2021 :273, wanted_chutkey_2014 :1308,
wanted_schwer_2018 :1332, wanted_hagemann_1998 :1374, rubino_2018 :579); prior de-novo trees 2026-08-17
(propulsion FORK-20 [L790], hyperbolic FORK-20/21 [L661]/[L683], variational FORK-11 [L522]; `phaseB_tree_diff.md`
par.2.9); `st_scoping_number_run.log` ([X-STSC] PASS: St_plug in [0.268, 1.415]); `RED_TEAM_decisive_number.md`
RT-1/RT-9/RT-10 + proposed A-2/A-5/A-9/A-11 (DA RATIFICARE, not of record). Memory files NOT read (LOG-4b).

Measured registry command for the [KNOWLEDGE] coverage claims below (SR-12, this window):
`grep -c -i <key> docs/literature_registry.yaml` -> korst 0 | ito/fujii 0 | nasuti 2 (Sapienza theses only, no
Nasuti-Onofri row) | fick 1 (Fickett-Jacobs, not Fick-Schmucker) | hagemann 2 (WANTED row only) |
lakshminarayana/denton/wang-he/turbomachin 0 | HB/time-spectral 9 (rubino_2018 + unrelated Nadarajah rows) |
mueller/sule 0 | stark/schmucker/summerfield 0 | lim/humble 0 | cumpsty/mixing-plane 0.

--------------------------------------------------------------------------------------------------------------
## 0. VERDICT IN ONE PARAGRAPH (the referee's first question at 1% Isp)

No tree's base model can RESOLVE the decisive difference above the thrust-stand band by modelling alone, and all
four trees say so themselves: their independently derived materiality arithmetic (V: A_b Delta p_b / F vs m; H:
~3% crude; O: "the base band alone can be ~ b_TS"; P: +-0.3-1.5% of F "= the band_TS itself") lands on the
record's own number (red team RT-1: base force 5-12% of thrust x closure band 15-19% = 0.75-2.3% absolute; M0:1347
"base-pressure model-form UNPRICED on truncated plug"). The trees' unanimous answer is structural, not a model
choice: (i) p_b is a SET (interval/bracket), never a point model; (ii) the decisive delta is a PAIRED difference
under the SAME closure with the truncation fraction FIXED, so the direct base term cancels and only the closure
sensitivity of delta survives; (iii) that residual is shipped as a named band row; (iv) the plug is quotable only
if the branch is invariant over the set. The record has (ii) already (TWIN §5 items 3-4) but NOT (i), (iii), (iv):
TWIN §6 lists Richardson + certificate-stack + representation bands and no p_b row, so as written the protocol can
quote MATERIAL with the p_b term unpriced. Three of four trees additionally recommend a base-free decisive
configuration (bell first); this is DIVERGENT from TWIN §2 and, at the record's data class A, theorem-degenerate:
[T-T3]/[T-T4] make the full-flowing bell and the full-length plug collapse to single-state designs (Annex B :1142
"Rao-at-<Pc> BY THEOREM"; M0:2316-2319 sharpness: only a length cap or a base-pressure model breaks T4's nesting).
So the base region is FORCED into the decisive path by the record's own theorems, and the p_b band is the price of
having a non-degenerate experiment at case A. The incumbent C61 is NEVER-class (declared slot, no adoption);
FULL-PANEL recommended, scoped to the p_b BAND PROTOCOL of the TWIN (set + sweep + re-design rule + cap), not to
"which closure is right" (undecidable inside the record: residue R-8, no truncated-plug RDE base measurement
exists; the closer is procurement-class external).

--------------------------------------------------------------------------------------------------------------
## 1. TABLE OF APPROACHES (schema columns)

| # | approach (tree option) | from lenses | classification | weight on Q0 | weight reason | changes credibility / cost | record anchor (+ tree location) |
|---|---|---|---|---|---|---|---|
| A1 | p_b as an UNCERTAIN SET / interval, decisive delta reported as the extremum over the set, residual `|delta(p_b,hi)-delta(p_b,lo)|` as a NAMED band row; quotable only if the branch is invariant | O (PB.4, DERIVED: dDelta/dp_b = (A_b7-A_b2)/F, criterion < b_TS/3); P (SP8 budget row `|D(p_b,max)-D(p_b,min)|`, SP9 "D at p_b band extremes"); V (B.5 bracket as CERTIFICATE, dJ/dp_b = A_b explicit); H ((4) "always shipped", claim only if Delta > eps_base + eps_tot) | NEW vs TWIN §6 (no p_b band row; C61 alternative "WG10 empirical bracket" is a closure CHOICE, not a budget row) — converges 4/4 with the red team's proposed A-2 (ORCHESTRATOR-SEEDED, DA RATIFICARE) | high | decides whether MATERIAL is ever quotable on the decisive sector (R-iii checkability); without it the protocol is referee-dead on its first question | credibility: TWIN as written -> checkable budget; cost: hours evaluation-only if the plug forward solve is O(1 s); +1 campaign per endpoint only on a branch flip | TWIN §6; M0:1347 (v) WORST; RED_TEAM A-2 table row; trees: V SP-PB "Derived materiality tolerance", H SP-PB "Materiality (dry)", O SP-PB PB.4 + "Decision criterion", P SP-PB "Materiality (derived)" + SP8 budget |
| A2 | FIXED truncation fraction + base geometry as INPUT so the direct base-area term drops out of the paired delta | O (PB.4 "fix the truncation fraction in the tournament so that the base band drops out"; falsifier = optimizer wants a different truncation); P (SP9 case 2 "FIXED truncation fraction and base radius (base as input so p_b cancels to first order)") | CONFIRM-candidate (DERIVED by O: the explicit (A_b7-A_b2) term; by P: dimensional argument) of TWIN §5 item 3 (truncation same value) — but the trees' "cancels to first order" is WEAKER than the record: Humphreys 1971 exhibit (harvest §13, [ORCH-HARV-3] M0:1453-1463) shows the closure moves the ARGMAX x2.45 at value +0.26%, i.e. the INDIRECT term (design response to p_b through the corner condition, M0:2319 mu-averaged plug corner condition) does not vanish at fixed truncation | high | fixing truncation removes one channel only; the re-DESIGN sensitivity of both arms to p_b is the unpriced remainder — exactly channel (vi) | credibility: the cancellation claim must be demoted to "direct term cancels; indirect term measured"; cost: re-design sweep at closure endpoints only if evaluation sweep flips the branch (A-2 rule) | TWIN §5.3-5.4; C61 note "priced at the design-gradient level, not the value level"; harvest §13 pp. 1586-1587 |
| A3 | SAME closure object in both arms (comparator fielded with the identical base treatment) | V (SP-CARM "identical closure on both sides"); O (SP-CARM C.3 "same base treatment"); P (C.4 "same as SP-PB for both designs"); H (SP-CARM: comparator base = option (1) p_b = Pa with band — see A8) | CONFIRM-candidate-NAMED of TWIN §5 item 4 ("same C61/N2 closure object, same parameters") — 3/4 name it, none derives more than "identity is the premise of a paired comparison" | medium | already of record; the trees add nothing except the GENO warning below | credibility: unchanged; cost: zero. NOTE (referee): arm C's independent cross-check is the GENO RaoPlug oracle (TWIN §4/§8) whose closure of record is the FAILED Veen 0.846 p/M^1.3 (C61 incumbent field) -> the oracle comparison must be run at the swept p_b or with base thrust excluded (Veen 1974 practice, harvest §11), else §5.4 is violated at the oracle level | TWIN §5.4; C61 incumbent; harvest §11 |
| A4 | Empirical p_b correlation (Hagemann-class), band = source scatter, as the CENTRAL value | V (B.2, [abstract]); H ((3), [abstract]); O (PB.1, "tens of % of p_b", [abstract]); P (B.1 constant p_b = k p_a closed wake, Hagemann [full]) | CONFIRM-candidate-NAMED of C61 alternative 1 (WG10 bracket [+19%,-15%] = best pure-empirical model on COLD data, harvest §14 Eq. 5.7) — the record is SHARPER (Veen FAILED per WG10; open-wake RDE anomaly below ambient; Schwer counter-datum). All four cite Hagemann 1998 = registry WANTED (:1374), UNVERIFIED | medium | fixes the central value and the width of the set of A1; the width is what the referee reads | credibility: only with the RDE offset labelled as ANALOGY (R8); cost: zero (closed form) | C61 alternatives; harvest §14 (b).4; M0:1347 |
| A5 | Physics-based Korst/Chapman-Korst recompression closure (mixing-layer model), band from the mixing-constant scatter | V (B.3, Korst 1956 [abstract]); H ((2), [abstract]) | CONFIRM-candidate-NAMED of harvest §14 (b).1 (multi-component Korst-class, [MODEL-VAL] only for closed bubble + 2D + cold + exact incoming Mach line) — NOT in the C61 `alternatives` field although C61's own evidence file ranks it first: ledger-field gap to repair | medium | the only mechanistic candidate for the N2 slot; its validity envelope is exactly what the RDE open-wake/3D regime violates (harvest §14: "mostly wrong" for overexpanded truncated plugs) | credibility: as the N2 mechanistic leg it would upgrade the set from empirical to modelled; cost: new theory + cold validation, F4b/N2 window (2-3 sessions) | harvest §14 pp. 16-17; C61 alternatives (absent) |
| A6 | Regime classifier open/closed wake vs pressure ratio (transition PR), regime-dependent band | P (B.2 Ito-Fujii-Hayashi 2002 [abstract]); implicit in H's "low altitude" qualifier of (1) | CONFIRM-candidate-NAMED of C61 alternative 2 (Nasuti-Onofri transition-PR model, the only [MODEL-VAL] classical piece, ~5% cold) + R8 two-regime row (transition Pa/Pc ~ 0.15, Harroun 2020 Fig. 9) | medium-high | the regime decides which band applies and whether the P_amb slot (C55) touches the base; open wake at the record's PR spread (45-49 CJ-based, st log) vs sea-level Pa must be classified per instance | credibility: instance scope printed (A-9 (b)); cost: closed-form check | C61 alt 2; findings :2263; harvest §2 Fig. 9, §14 Eqs. 3.1-3.2 |
| A7 | Euler cannot close a base: the captured/inviscid recirculation is NOT a base-pressure model; the base is a declared model layer | O (PB.2 REJECTED for a stated reason — derived); P (B.4 "not physical", derived); H ((5) needs a recirculation closure); V (F.2 "base pocket by a closure") | CONFIRM-candidate (DERIVED, short dry argument in O/P) of the record's declared-slot architecture (problem book :348 "base-pressure closure p_b declared (N2)"; SP-8120 practice, harvest §15; H20 = inviscid plume solve DISTINCT from C61 closure, E12) | medium | protects the TWIN from the cheapest wrong shortcut (reading p_b off the march) | credibility: guards R-iv; cost: zero | decision map E12; problem book :348 |
| A8 | p_b = Pa as closure (or as the bracket's lower endpoint) | V (B.1 "conservative lower bound"; B.5 bracket p_b in [min(Pa,p_lip), p_lip]); H ((1) low altitude; SP-CARM comparator base = (1) with band) | DIVERGENT from R8 of record: "Pb/Pa = 1 INADMISSIBLE for RDE in both regimes (base ~17-20% below ambient even in open wake — Purdue V1.4 CTAP, hot-fire)" (M0:1347; findings :2263; harvest §1.2/§2); V's bracket ASSUMPTION "base pressure between ambient and lip pressure" is already broken by the record's only hot-fire datum (nozzleless, transfer = ANALOGY) and by P-A CFD P_b/P_a ~ 0.44 (context) | low as a closure (rejected), medium as a warning | if the set of A1 were built on V's endpoints it would EXCLUDE the physically observed region -> a branch declared invariant could be false | credibility: negative if adopted; cost: zero to widen the set (suction factor 0.62 as labelled analogy, A-2) | M0:1347; harvest CONSOLIDATED (a) |
| A9 | Derived MAXIMUM ADMISSIBLE TRUNCATION fraction: invert A_b Delta p_b,band / F < m - (other bands) into a constraint on c; if violated the plug ships CONDITIONAL and only the base-free result is decisive | V (SP-PB "Derived materiality tolerance ... INVERTS into a maximum admissible truncation fraction" — DERIVED) | NEW (no record home: ADR-D4 pins truncation 0.20 with a declared 20-40% band, PROGRESS B9; TWIN §3 pins the instance value by measured command; no band-derived rule exists) | high | gives the F3.TWIN instance pin a DERIVED truncation instead of a practice default; BUT it pulls toward small truncation where T4's break (delta) vanishes (M0:2316: full plug nests, max Int = Int max) while the red team notes the break GROWS with truncation depth (RT-9) -> the quotable window is delta(trunc) > band(trunc), unpriced by anyone | credibility: converts "why 20%?" into a derived answer or an honest "no window"; cost: a truncation sweep of (delta, band) = A-5's second instance at 0.40 + the 0.20 pin (+1 session inside F3 cap) | ADR :126-146; PROGRESS B9; TWIN §3; M0:2316-2319; RED_TEAM A-5/RT-9 |
| A10 | Unsteady base-response indicator tau_b f = f L_b / a: quasi-steady base only if << 1; per-phase base closures unlicensed otherwise -> cycle-mean effective closure | P (B.6, DERIVED order-of-magnitude 20 us vs period 30-1000 us; DL-2 (d) "unsteady base-pressure response" named as one of the four places an unsteady-aware design can buy) | CONFIRM-candidate (derived indicator) of DUTY-10(a) "base forced-response validity note" (D6 :435-437, slotted F5b) and of the Harroun mechanism (harvest §1.2: wave period faster than base adjustment -> ejector suction, base never steady) — the record has the physics and the duty slot, not the indicator | medium-high | with the record's f (2.8-9.1 kHz 10 kN; 8.6-28 kHz 600 N, st log) and a ~1000-1300 m/s the indicator spans O(0.05)-O(1) for L_b of centimetres: the base is MARGINAL exactly as St is -> V's "per phase" bracket and H's (5) per-phase base are physically unlicensed at the record head count; the closure must be a cycle-mean quantity entering the mu-averaged corner condition (M0:2319) — coherent with CTAP being cycle-mean only | credibility: names the error bar that DUTY-10(a) owes and moves it from F5b to the TWIN instance scope; cost: one printed number per instance (producer = X-STSC-class script extension) | D6:435-437; harvest §1.1-1.2; M0:2319; st log |
| A11 | Closure derivative in the gradient: explicit dp_b/d(geometry) in the adjoint source term, or bracket NOT differentiated with the gradient error bounded by the base band; iterated-constant architecture | V (SP3 "the base closure enters the gradient through its explicit derivative; B.5 has none — declared gradient error bounded by the base band" — DERIVED); O (SP3 extra rejector I.1 on a base-pressure functional) | CONFIRM-candidate (derived) of the C61 note's gradient-level pricing + Humphreys' architecture ("treated in the variational problem as a constant not known a priori; iterated to compatibility; procedure independent of the model", harvest §13) | medium-high | sets the N2 requirement at design level: a closure that is differentiable or an iterated constant whose sensitivity is reported; the O3 dot-product certificate must include the base term | credibility: closes a hole in the F3.PLUG exit (H20 carries the plume shape-adjoint, nothing carries dJ/dp_b of record); cost: one adjoint source term + one rejector | C61 note; harvest §13; TWIN §8 F3.PLUG line |
| A12 | Viscous/zonal RANS base computation as a ONE-OFF anchor for the band (not as a model) | V (B.4); O (PB.3 "oracle for the closure band"); P (B.5 "validation of B.1/B.2 only") | CONFIRM-candidate-NAMED of "R22-CFD-1 prices coupled model-form jointly" (M0:1347 what-tightens column) — with the record's CT-6 rule (literature CFD values context-only) unaffected because the anchor is in-house; R22-CFD scheduling = USER-DECISION PENDING (Stage 2/8) | medium | the only in-budget path to shrink the set below the WG10 width; priced in F2 (CFD-2) per red team A-4 | credibility: upgrades the set from literature-width to instance-width; cost: R22-CFD decision (user) | decision map Stage 8 R22-CFD row; M0:1347 |
| A13 | MEASURED base pressure (class C) narrowing the band; plug becomes decisive-eligible if the band < band/4 | H (falsifier of SP-PB, derived threshold band/4); P (D.C CTAP calibration) | CONFIRM-candidate-NAMED of C61 alternative 4 (V1.4-class CTAP on a truncated plug = "THE closer", harvest (c); residue R-8 procurement-class external) | high on credibility, zero on cost feasibility inside §8 (no experimental access) | the only evidence class that certifies rather than brackets; outside the program's budget by statement §8 | credibility: certification against the world; cost: external procurement, unpriced | C61 alt 4; harvest CONSOLIDATED (c); findings :2263 |
| A14 | Decisive run on a BASE-FREE configuration (bell first; full-length annular nozzle r_min > r*); truncated plug secondary/conditional, "typically it will not resolve — pre-registered" | V (SP9 "BELL first ... plug CONDITIONAL"); H (SP9 "TRUNCATED plug is excluded from the decisive run (SP-PB band)"); O (SP9 "BELL first (no base-region band)"); P runs BOTH cases with base as input | DIVERGENT from TWIN §2 (sector FIXED = truncated plug, "the break theorem's arena") — and theorem-DEGENERATE at the record's data class A: [T-T3] (M0:746 ff.) collapses the fixed full-flowing bell to Rao-at-<Pc> (Annex B :1142 "BY THEOREM"), [T-T4] (M0:2294 ff.) makes the full-length plug simultaneously optimizable (peak design); only a length cap / truncation + base closure breaks the nesting (M0:2316-2319). The trees could not know T3/T4; P's DL-2 (linear thrust law, choked case: "zero benefit ... the decisive instance MUST be posed where DL-2 leaves room") is the independent re-derivation of the SAME collapse and lists "(d) unsteady base-pressure response" among the places that leave room | high | the trees' reason (band swamps) and the record's reason (bell collapses) are BOTH valid: at case A the non-degenerate sector is the one with the threshold-sized band. Escape routes: case-B flip (TWIN §3 clause; P's DL-2 (a) supersonic interface with swept Mach/angle/swirl makes a bell non-degenerate) or accept the plug with A1/A2/A9 | credibility: a bell decisive at case A would be a zero by theorem (fatal); at case B it re-opens the F2a contract tags (TWIN §3 declared consequence); cost: case-B = richer data + contract flip | TWIN §2-§3; Annex B :1142; M0:746, :2294, :2316-2319; P DL-2 |
| A15 | Base bleed as a design option | P (B.3, "changes the configuration") | NEW (no C61 alternative; record has only harvest §14 §6 Hagemann-Immich ~1% bleed raises open-wake p_b [ADV-CFD] and the ADR O-c mention) | low | outside the pinned solid-set class (adds a mass-flow port); a sector for F3.TOURNAMENT, not for the TWIN | credibility: none for Q0's nominal answer; cost: new configuration class | harvest §14 §6; ADR :126 O-c |

--------------------------------------------------------------------------------------------------------------
## 2. THE INCUMBENT OF RECORD (what the judge compared against)

- Ledger C61 (:818-831): status NEVER; incumbent "INCUMBENT-DECLARED, no program adoption" — Veen 0.846 p/M^1.3
  practiced in the LEGACY chain only (GENO), traced to a 1966 near-wake curve fit (Rom, via Humphreys 1971 Eq. 12)
  and FAILED per WG10 (Fick-Schmucker 1996, UNVERIFIED at primary); the program's own p_b is a DECLARED SLOT (N2,
  problem book :348). Alternatives on the row: WG10 bracket [+19%,-15%]; Nasuti-Onofri transition model; derived
  N2 closure; measured (V1.4-class CTAP). Owner N2/F4b window; trigger = "first truncated-plug (value, delta) row
  entering the record, or F4b window entry" — the TWIN IS that trigger.
- TWIN protocol: §2 sector FIXED truncated plug, closure = "C61/N2 base-pressure closure ... THE SAME OBJECT in both
  arms"; §5 items 3-4 (same truncation, same closure + parameters, enforced by rejector); §6 bands = Richardson x
  K_RICH + certificate stack + representation term — NO p_b row; §8 prerequisite F3.PLUG = "H20 plume-boundary solve
  + C61 p_b closure + plug/C- mirror margin + vortex-sheet monitor".
- M0 forchetta channel (v) :1347: "base-pressure model-form UNPRICED on truncated plug"; channel (vi) + [ORCH-HARV-3]:
  Humphreys x2.45 argmax exhibit; T-T4 sharpness :2316-2319: a base-pressure model at a truncation plane is what
  breaks the nesting (the reason PB-2 exists, :532-536).
- H20 (decision map Stage 8 :183; findings :2728, path critical): the free plume boundary p = Pa SOLVE mechanics +
  shape-adjoint term has NO home; distinct by declaration from C61 (closure). Owner F4b window by registry, F3.PLUG
  by D6 precedence (findings :2813 declared override).
- ADR panel :126-146: truncation default alone flips the SIGN of the spike-vs-CP headline (20/25/30%: +6.4%/+3.4%/
  below CP); base-pressure loss/credit "~1% class at >= 20% with base bleed" DECLARED NOT MODELLED (O-c). PROGRESS
  B9: truncation 0.20 DECIDED, execution gated to the ADR-D4 window with the p_b rider on C61 + findings :2263.
- Prior de-novo evidence 2026-08-17: propulsion FORK-20 "the Euler-uncertifiable zone ... the one place this program
  could ship a certified number that a thrust stand would flatly contradict" (O2 = model with O4-grade calibration;
  O1 = base-free "whenever constraints admit it"); phaseB diff par.2.9: "certificate class must exclude or model the
  base region explicitly". The 2026-09-05 trees re-derive the same fork with sharper arithmetic (A1) and the same
  base-free preference (A14): 2-of-2 independent campaigns converge on "exclude or price"; the record chose
  "price" by fixing the plug sector, and has not yet priced.

--------------------------------------------------------------------------------------------------------------
## 3. DERIVES vs NAMES (independence modulo LOG-4b)

The four trees converge on A1-A3/A7 through arguments present IN the trees (materiality formulas with explicit
hypotheses; the (A_b7-A_b2) direct term; "Euler cannot set a base pressure" as a dry statement; the base-free
preference as a consequence of their own arithmetic). None of the trees uses any repo identifier, the closure
constants (0.846/1.3), the WG10 bracket, the Purdue datum, the Humphreys exhibit or the T3/T4 collapse: their
option spaces are textbook-shaped (Korst, Hagemann, p_b = Pa, RANS, interval). I therefore treat A1, A2, A7, A9,
A10, A11 as DERIVED convergences and A3-A6, A12, A13 as NAMED. The hyperbolic tree's explicit non-use declaration
(:585-587) and the lint (0 hits) support this; the exposure caveat is carried, not discharged.

Where the record is AHEAD of the trees (the trees' cancellation claims are too strong): Humphreys 1971 (harvest
§13) shows a closure swap moving the optimum base height x2.45 and the tip slope from -13.26 to -3.08 deg at +0.26%
thrust. With truncation FIXED (A2) the base-height channel is closed, but the tip-slope/contour channel through the
plug corner condition (Veen Eq. 8 / Li-Xu 2023 Eq. 26, harvest §7/§11; mu-averaged form M0:2319) stays open in
BOTH arms; its effect on delta is the quantity nobody has measured. Hence: direct term cancels (trees, correct);
"second order" (P) / "first order" (V) cancellation of the whole is UNPROVEN — the sweep must include re-design at
the endpoints whenever the evaluation-only sweep flips the branch (A-2 rule, adopted here as the falsifier).

Where the trees are AHEAD of the record: (a) the set-valued p_b as a BUDGET ROW with an invariance rule (A1) —
the record only has it as a proposed amendment; (b) the derived truncation bound (A9); (c) the base-response
indicator (A10) which downgrades every per-phase base closure at the record head count and makes the cycle-mean
closure the only licensed form — this also re-reads C61's "measured (CTAP)" alternative as the physically right
CLASS of closure (cycle-mean), not merely the best evidence class.

--------------------------------------------------------------------------------------------------------------
## 4. THE STRUCTURAL POINT THE REFEREE WILL PRESS (T3/T4 vs the band)

At case A / interface I3 the record's own theorems remove every base-free sector from the decisive path: the bell
collapses to Rao-at-<Pc> ([T-T3]; Annex B :1142 says the tool STATES it), the full plug collapses to the peak design
([T-T4]). The only non-degenerate cycle instance is the length-capped/truncated plug with a base closure
(M0:2316-2319; PB-2 :532-536). Therefore the decisive difference lives BY CONSTRUCTION on the sector whose closure
band is threshold-sized. The trees, ignorant of T3/T4, would have run a bell that returns zero by theorem — the
one outcome worse than an unresolvable plug. The consistent program-level reading is:

  delta(trunc, regime, p_b-set) must exceed band(trunc, regime, p_b-set) somewhere in the admissible truncation
  window; delta grows with truncation depth (break of T4's nesting), band grows with base area (A_b ~ trunc).
  Neither the trees nor the record has this curve. It is the sharp form of the referee's question, and it is
  computable inside the record at evaluation cost once the plug forward solve (H20) exists: two truncations
  (0.20 pinned, 0.40 = A-5's second instance) x the closure set of A1.

If no window exists, the honest Q0 answer at case A is "SMALL/INTERMEDIATE by base band on the only non-degenerate
sector" and the flip to case B (TWIN §3 clause; P's DL-2 (a): supersonic interface with swept Mach/angle/swirl makes
a bell non-degenerate WITHOUT a base) becomes the road, at the declared contract cost.

--------------------------------------------------------------------------------------------------------------
## 5. THE THREE QUESTIONS (§G.3), answered for SP-PB

- Q1 (is Q1 the right sharpening of Q0?): the sharpening to the truncated plug is FORCED (T3/T4) and therefore right
  at case A; but Q1 as written (TWIN §6) is UNDER-sharpened: "beats by how much" is not decidable without a p_b
  band row and an invariance rule. The trees' unanimous set-valued p_b (A1) is the missing clause. Q1 must read:
  "... at identical constraints and the SAME closure, with the branch INVARIANT over the declared p_b set".
- Q2 (does Q2 answer Q0?): conditionally. A MATERIAL branch with p_b unpriced does not answer Q0 (a referee rejects
  it at RT-1). With A1 + the re-design rule, Q2 answers Q0 at the "BRACKETED from inside the record" evidence stage
  (P34 light instantiation): the sign of delta is bracketed over the set, not certified against a measurement —
  the closer is R-8 procurement (A13). A SMALL branch answers Q0 only with the A-9 co-report (bound gap + instance
  scope incl. regime + truncation), otherwise it is an argument from silence on a flat objective (ADR :126 KEY
  FINDING 4).
- Q3 (separate designer/evaluator rungs?): for the base term the two rungs share the SAME model-form error: the
  wave-frame evaluator cannot compute p_b any more than the per-phase march can (A7); there is no higher rung for
  the base short of viscous unsteady CFD (R22-CFD-1, user decision) or measurement. So the designer/evaluator split
  helps every band EXCEPT the base band; the base band is controlled only by pairing (A2/A3) + sweep (A1). The
  indicator A10 says the closure must be cycle-mean in both rungs.

--------------------------------------------------------------------------------------------------------------
## 6. PROPOSED FALSIFIER (the one the Stage-B parties must agree on)

F-PB: At the pinned instance (fixed truncation, fixed base radius, same closure object in both arms), evaluate the
final designs of arm P and arm C under a declared p_b SET spanning at least {WG10 best model at its -15% and +19%
endpoints; the same model with the Purdue suction factor 0.62 applied as a LABELLED analogy offset; p_b = 0 as the
SP-8120 variational floor} and print the TWIN §6 branch at every member. If the branch differs between any two
members, BOTH arms are re-designed at the two extreme members and the branch re-read. The incumbent (TWIN §6 band
list without a p_b row) is KILLED if any member moves the branch — the protocol must carry the row and the cap
"no producer -> INTERMEDIATE by rule". The trees' cancellation claim (A2/A3 "cancels to first/second order") is
KILLED if |delta(p_b,hi) - delta(p_b,lo)| exceeds the Richardson band on delta after re-design. The plug sector's
eligibility as the decisive sector (A9/A14) is KILLED at case A if no truncation in {0.20, 0.40} yields a branch
invariant over the set — then the case-B flip is the road. Seeded rejectors: an arm Verdict with an empty p_b row
must be REFUSED; a run with p_b = Pa as a set member labelled "lower bound" must be REFUSED (R8). External closer
(not a Stage-B falsifier, procurement): a V1.4-class CTAP measurement on a truncated plug under a rocket-condition
RDE across NPR 4-20 (harvest (c)).

--------------------------------------------------------------------------------------------------------------
## 7. WHAT THE RECORD MUST ADD (ordered by value/cost; none applied here)

1. TWIN §6 p_b band row + invariance rule + no-producer cap (A1; = red-team A-2 p_b part). Cost: hours at F3.TWIN
   if the plug forward solve is O(1 s); the set is closed-form.
2. Re-design-at-endpoints rule (A2 residual; Humphreys channel). Cost: +1 campaign per endpoint only on a flip
   (inside the F3 cap of 2 campaigns/instance — a THIRD flip means the instance is not quotable).
3. Cycle-mean closure class + base-response indicator tau_b f printed per instance (A10); move DUTY-10(a) from an
   F5b note to a TWIN instance-scope field. Cost: one number from an X-STSC-class script extension (rejector: a
   deliberately per-phase closure must be refused when tau_b f > a declared fraction).
4. Truncation window curve delta(trunc) vs band(trunc) at {0.20, 0.40} (A9 + A-5). Cost: +1 session inside F3.
5. Closure derivative / iterated-constant sensitivity in the F3.PLUG exit and in the O3 dot-product certificate
   (A11). Cost: one adjoint source term + one rejector.
6. C61 ledger hygiene: add the Korst-class multi-component model (harvest §14 (b).1) to `alternatives` (its own
   evidence file ranks it first); record the GENO-oracle closure mismatch as a §5.4 rejector condition (A3 note).
   Cost: minutes.
7. Regime classification per instance (A6) as an A-9 (b) scope field. Cost: closed-form.
8. Procurement rows (see §9): Lim-Humble 2020-0195, Fick-Schmucker 1996, Nasuti-Onofri 1999 (harvest (d) 1/4/5),
   Hagemann 1998 (WANTED, cited by all four trees), Chutkey 2014 / Schwer 2018 (WANTED).

--------------------------------------------------------------------------------------------------------------
## 8. BRANCH LEDGER ROWS (every branch seen; candidate rows for the orchestrator's BRANCH_LEDGER.md)

| id | branch | status | reason / trigger + owner | source |
|---|---|---|---|---|
| PB-1 | p_b set-valued as a budget row with invariance rule (A1) | EXPANDED -> Stage B | high weight; converges 4/4 + red-team A-2; kills/keeps TWIN §6 as written | all four trees SP-PB; RED_TEAM A-2 |
| PB-2 | fixed truncation + base as input; direct term cancels (A2) | EXPANDED -> Stage B (as the residual channel) | of record in TWIN §5.3 but the indirect (argmax) channel unpriced (Humphreys) | O PB.4; P SP9 case 2; harvest §13 |
| PB-3 | same closure object both arms (A3) | PRUNED (already of record, TWIN §5.4); one rider: GENO-oracle closure mismatch -> §5.4 rejector condition, owner F3.RK1/B-RAOPLUG | V/O/P SP-CARM |
| PB-4 | Hagemann/WG10 empirical correlation as central value (A4) | EXPANDED at Stage A only; DEFERRED as a closure CHOICE to the N2/F4b window (C61 trigger fires at the TWIN) — enters Stage B only as a SET MEMBER | V B.2; H (3); O PB.1; P B.1 |
| PB-5 | Korst/Chapman-Korst mechanistic closure (A5) | DEFERRED: trigger = N2 closure work at the F4b/F3.PLUG window; owner N2/F4b; ledger hygiene now (C61 alternatives) | V B.3; H (2); harvest §14 |
| PB-6 | regime classifier open/closed (A6) | DEFERRED to the instance pin (F3.TWIN opening amendment): print regime by the Nasuti-Onofri classifier; owner F3.TWIN executor | P B.2; harvest §14 |
| PB-7 | Euler-captured recirculation as a base model (A7) | PRUNED: rejected by O/P with a dry argument; record architecture agrees (declared slot) | O PB.2; P B.4 |
| PB-8 | p_b = Pa closure / bracket endpoint (A8) | PRUNED: inadmissible for RDE in both regimes (R8, hot-fire datum); H's comparator base treatment REJECTED as a §5.4 violation | V B.1/B.5; H (1) + SP-CARM |
| PB-9 | derived maximum admissible truncation (A9) | EXPANDED -> Stage B as the truncation-window question (delta vs band curve) | V SP-PB derived tolerance |
| PB-10 | base-response indicator tau_b f, cycle-mean closure class (A10) | EXPANDED -> Stage B (cheap; changes which closures are licensed) | P B.6 / DL-2 (d); D6 DUTY-10(a) |
| PB-11 | closure derivative in the gradient / iterated constant (A11) | DEFERRED: trigger = F3.PLUG exit (first dJ/dthB Verdict consuming a plug with base); owner F3.PLUG | V SP3; harvest §13 |
| PB-12 | zonal viscous anchor for the set width (A12) | DEFERRED: trigger = R22-CFD scheduling decision (user, Stage 2/8); owner R22-CFD-1 | V B.4; O PB.3; P B.5 |
| PB-13 | measured CTAP closer (A13) | DEFERRED: procurement-class external (residue R-8); owner N2/F4b + procurement queue | H falsifier; P D.C |
| PB-14 | base-free decisive configuration at case A (A14) | PRUNED at case A (theorem-degenerate: T3/T4); DEFERRED as the case-B flip road: trigger = no invariant branch in the truncation window (PB-9); owner user decision + F2a contract tags (TWIN §3 clause) | V/H/O SP9 |
| PB-15 | full-length annular / shrouded r_min > r* base-free config (H SP9 second config) | PRUNED at case A: T4 collapse (peak design) + shrouded plug = PB-3 conjecture C1, not the decisive sector | H SP9 |
| PB-16 | per-phase base pressure from the evaluator with a recirculation closure (H (5)) | PRUNED: no model layer exists and tau_b f ~ O(1) at the record head count unlicenses per-phase closures | H (5); P B.6 |
| PB-17 | base bleed as a design option (A15) | DEFERRED: trigger = F3.TOURNAMENT sector enumeration; owner F3.TOURNAMENT | P B.3 |
| PB-18 | H20 free-plume solve + shape-adjoint as a TWIN prerequisite with a rejector (R-TWIN-7) | EXPANDED at Stage A only: not an SP-PB closure question (E12 distinct); the SP2/SP9 judges own it; noted here because the plug band arithmetic assumes the plume solve exists | findings :2728; RED_TEAM A-11 |

--------------------------------------------------------------------------------------------------------------
## 9. ADJACENT-FIELD PRIOR CHECK (mandatory) and [KNOWLEDGE] ROWS

Considered by the trees: (i) turbomachinery steady rotating frame — YES, all four (V L0.1, H L1, O S4 citing
Lakshminarayana 1996 + Wang & He 2010 [abstract], P DL-1 citing Paxson 2014 wave-fixed frame + sector/phase-lag
practice); (ii) harmonic-balance / time-spectral with adjoints — YES, all four (V S0.7, H S5, O S6, P S-5; Hall-
Thomas-Clark 2002, McMullen-Jameson 2006, Gopinath-Jameson 2005, Nadarajah-Jameson 2007), each REJECTED for a stated
reason (equivalent to the rotating-frame steady problem under the pin; Gibbs at the data-borne shock; O(1) dropped
azimuthal flux in the 2D+t variant); (iii) steady adjoint-based shape optimization — YES, all four (Jameson 1988,
Giles-Pierce 2000/2001, Sokolowski-Zolesio, Delfour-Zolesio, Allaire-Jouve-Toader 2004). (iv) Mixing-plane /
flux-averaging practice for the comparator state — H (Denton 1992) and O (Cumpsty-Horlock 2006). NOT considered by
any tree, relevant to SP-PB specifically: base pressure of bluff trailing edges under PERIODIC wake passing
(turbine cascade base-pressure correlations and their unsteady sensitivity) — the adjacent field's version of
"base region under a kHz forcing". Every item enters as [KNOWLEDGE], never as evidence.

| identity | why needed | procurement owner | registry status (measured grep, this window) |
|---|---|---|---|
| Hagemann, Immich, Nguyen & Dumnov 1998, JPP 14(5):620-634 | the correlation/review source ALL FOUR trees cite for p_b (P declares [full]); central value + width of the set A1 | procurement queue (existing WANTED row :1374) | WANTED, unread -> tree claims UNVERIFIED |
| Korst 1956, J. Appl. Mech. (base pressure theory) | mechanistic N2 candidate (A5); record knows it only via WG10 | N2/F4b window (harvest (d) item 9) | no row (korst 0) |
| Fick & Schmucker 1996, JSR 33(4):507-512 | primary of the WG10 verdict "Veen FAILED" — the incumbent's kill is second-hand | N2/F4b (harvest (d) item 5) | no row (fick = Fickett only) -> UNVERIFIED at primary |
| Nasuti & Onofri 1999, JPP 15(4):544-551 | the only [MODEL-VAL] regime classifier (A6); C61 alternative 2 | N2/F4b (harvest (d) item 4) | no row (nasuti = Sapienza theses only) |
| Ito, Fujii & Hayashi 2002 JPP / AIAA 99-3211 | P's regime-switching source; WG10's 5%-base-drag datum | N2/F4b | no row (ito/fujii 0) |
| Lim, Humble & Heister, AIAA 2020-0195 | primary of the ONLY hot-fire RDE base dataset (Purdue V1.4 CTAP) that fixes the suction analogy factor | procurement (harvest (d) item 1) | no row (humble 0) |
| Chutkey, Vasudevan & Balakrishnan 2014, JSR 51(2) | cold truncated-plug base dataset vs NPR (the closest measured p_b(NPR) curve for a truncated plug) | procurement queue W-08 (:1308) | WANTED |
| Schwer, Kelso & Brophy 2018, AIAA 2018-4968 | counter-datum: no substantial RDE-vs-steady base change on an airbreathing truncated aerospike (sign of the RDE offset is configuration-dependent) | procurement queue W-12 (:1332) | WANTED |
| Lakshminarayana 1996 (textbook); Wang & He 2010 (rotating-frame turbomachinery adjoint) | adjacent-field prior for the wave-frame road (O S4) — census row for the SP0/SP1 judges | S-REVIEW census (orchestrator) | no row (0) |
| Hall, Thomas & Clark 2002; McMullen & Jameson 2006; Gopinath & Jameson 2005; Nadarajah & Jameson 2007 | HB/time-spectral adjoint family the trees reject for a reason; rubino_2018 (:579) covers only the HB-adjoint existence | S-REVIEW census (SP0/SP1 judges) | rubino_2018 present; others no row |
| Turbine trailing-edge base pressure under periodic wake passing (Sieverding-class cascade correlations; title depth only, UNVERIFIED) | adjacent-field prior NOT considered by any tree: base region under kHz periodic forcing = the physics behind Harroun's ejector suction and the A10 indicator | DUTY-10(a) owner (F5b) / N2 window | no row |
| Stark 2005; Schmucker 1973/84; Summerfield 1954; Frey & Hagemann 1998 (separation criteria) | used by all trees for g_sep — SP2's business, listed for completeness | SP2 judge | no row (0) |

--------------------------------------------------------------------------------------------------------------
## 10. PIN TABLE PER ROAD (SP-PB view)

| road | pins needed for the base term | pins the road could relax |
|---|---|---|
| (a) practice: mean-state steady design + unsteady check | closed-wake regime + a correlation closure (Hagemann/WG10); truncation from practice (20%) | none; it inherits the full absolute p_b band |
| (b) program road: per-phase cycle-averaged design | fixed truncation; same closure object; cycle-mean closure entering the mu-averaged corner condition (A10); p_b set + invariance rule (A1) | per-phase base modelling (unlicensed anyway); the choice of closure (a set suffices) |
| (c) direct unsteady optimization | a viscous model layer + HPC to compute the base (Euler pin blocks it) | the closure itself (computed, not modelled) — at a cost outside §8 |
| (d) wave-frame steady 3-D | same as (b): no base rung exists in the wave frame either (A7) | nothing on the base |
| (e) ROM / surrogate + global search | inherits (b)'s closure; surrogate over the p_b set is cheap (values only) | nothing on the base |
| (f) robust over the envelope (P_amb set, C55) | regime fence across the ambient set (open/closed transition inside P_amb -> non-affine, outside the certified class, problem book P_amb slot) | the single-regime assumption of (b), at the cost of a regime classifier per member |
| (g) physical levers as primary object (base pressure, truncation) | a MEASURED closure (R-8 procurement) to be more than a bracket | the closure becomes a measured input; truncation becomes the design variable (A9's window curve) |
| (h) hybrid: design per-phase, evaluate both arms in the wave frame | same as (b) + (d): the evaluator adds nothing to the base band | nothing on the base |

--------------------------------------------------------------------------------------------------------------
## 11. PANEL RECOMMENDATION

Incumbent adjudication class: NEVER (C61: declared slot, legacy-practiced Veen FAILED, no program adoption; the
TWIN pins "same object" without choosing the object). No genuine advocate exists for the incumbent, so no 2026
DELTA-SWEEP was performed (delta_sweep_done = false). Recommendation: FULL-PANEL, scoped to the p_b BAND PROTOCOL
of the decisive experiment (set membership, invariance rule, re-design-on-flip, INTERMEDIATE cap, cycle-mean
closure class + tau_b f indicator, truncation window), with the parties: (advocate) the record's TWIN as
written + A-2; (refuter) the trees' base-free preference at case B; (judge) the T3/T4 collapse reading. The panel
must NOT be asked "which closure is right" — that is R-8 and cannot converge inside the record. Weight on Q0: high
(the first referee question; decides quotability of MATERIAL on the only non-degenerate case-A sector).
