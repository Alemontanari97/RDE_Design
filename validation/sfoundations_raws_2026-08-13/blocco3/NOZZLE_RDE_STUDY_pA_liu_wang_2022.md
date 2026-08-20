# NOZZLE-RDE DEEP STUDY — P-A: Liu, Cheng, Zhang & Wang 2022 (PKU aerospike)

Session: S-FOUNDATIONS-C4, blocco 3 (arrivals campaign, BRIEF_nozzle_rde_
arrivals_study.md, slot 1). Date: 2026-08-20.
Paper: "Design and optimization of aerospike nozzle for rotating detonation
engine", Aerosp. Sci. Technol. 120 (2022) 107300, DOI 10.1016/j.ast.2021.107300.
File: literature_addition_nozzle_rde/1-s2.0-S1270963821008105-main.pdf (14 pp.).

READ DEPTH: **[FULL] 14/14 pages, ALL pages rendered VISUALLY** (Read tool,
two calls, pages 1-7 and 8-14 — every figure page read as image); reference
list additionally pinned by pypdf text extraction (pp. 13-14) for exact
identities (no package installed; pypdf already in the pinned env).
EVIDENCE CLASS CONVENTION (brief SHARED RULES): everything sourced from this
paper is **published-CFD / published-experiment ADVISORY evidence** — never a
measurement of ours; per-statement class labeled [ADV-CFD] (their simulation),
[ADV-TXT] (their textual claim), [ADV-FIG] (my visual reading of their figure).

## SPECIAL DUTY — DIFF vs THE STANDING READ (census-defect context)

P-A was ALREADY read integrally (lit-registry :614-621; report
`literature_review/reports/liu_2022_aerospike_rde.md`, 2026-08-13, findings
F1-F12). Both were read IN FULL this window BEFORE the PDF. Diff verdict:

**WHAT STANDS (not duplicated here — incorporated by reference):** the prior
report's §0 citation, §1 coverage, §2 method/design-equations/thrust-
bookkeeping/averaging-convention tables, §3 hypothesis census (declared 1-7 +
undeclared 8-14), findings F1 (no optimizer in the paper — verified again
visually this window: the "optimization" is a 4-case discrete trade study,
Table 4 p. 5), F2 (averaging justified a posteriori), F3 (T-T3 practiced
without hypotheses; 14.2% penalty named), F4 (zero-DOF containment), F5
(choking assumed, not certified), F6 (rhetorical threat δ=85.8%), F7 (Angelino
= degenerate Route-A corner, no transversality), F8 (below-ambient ramp tail:
Case B −5.54 N at z>0.72 cm, Case C −0.095 N at z>2.0 cm, p. 11), F9
(state-averaged stagnation reconstruction Eq. (14)), F10 (γ inconsistency),
F11 (empty algorithmic niche), F12 (16-segment ramp diagnostic + truncation
sharpness datum), and §5 bibliography inspection (Rao/Guderley/Kraiko ABSENT;
only nozzle-theory refs = Angelino [35], Hagemann [36]). All re-checked
against the rendered pages; **no contradiction found between the standing
report and this visual re-read.**

**DELTAS (new in this read — the prior read did not render the field figures
visually; the topology content below is the main addition):**
- Δ1 TOPOLOGY ATLAS of Figs. 7-13 (the plot-borne field topology; §3 below).
  The prior report used Fig. 15 and captions only.
- Δ2 Measured mean design-point miss: mass-weighted average exit Mach ≈ 2.58
  vs design M_e = 2.69 (~4% low), attributed by the authors to "the
  nonhomogeneous flow at nozzle throat, no exact Prandtl–Meyer expansion and
  so on" (p. 7, §4.2) [ADV-CFD]. Not in the prior report.
- Δ3 The paper NAMES the cause of the cross-case ṁ variation the prior report
  flagged as an uncontrolled comparison (its hyp. 13): "The upstream reflected
  shock waves caused by constriction throat will block the fuel intake.
  Therefore, ṁ_f in Case B/C/D is slightly lower than Case A" (p. 12)
  [ADV-TXT]. The prior report's criticism stands (still no matched-ṁ
  control), but the mechanism is declared, and it is a data-nozzle COUPLING
  channel (threat scan T2 below).
- Δ4 Nozzle-to-chamber feedback topology: reflected shock wave from the
  constriction throat (Case B, Fig. 8d p. 8) and from the cowl lip (Case C,
  Fig. 11a-b p. 9) travels BACK INTO the combustor; authors: "Fortunately, the
  reflected shock is very weak and does not disturb the stable propagation of
  rotating detonation wave" (p. 7) [ADV-CFD/ADV-FIG]. Not in the prior report.
- Δ5 Intro-carried corpus numbers not in the prior report: choked aerospike
  improved Isp by 4~7% (Jourdaine [26], p. 2); Fotia [30] max stagnation
  pressure increase 3~7% at ε = 80%; Bach [56] pressure gain improved by
  restricting ε = 100% → 50% (both p. 10); Betelin [29] center-body length
  study 6/9/9.75 cm, Isp max at 6 cm (p. 2) [ADV-TXT].
- Δ6 Thrust-composition narrative numbers (p. 11): A→C the constriction-only
  gain is +4.4% (144.11→150.49 N, A vs B); C vs A: F_exit DROPS 142.38→134.64 N
  (axial-momentum loss from inward turning at the cowl lip) but F_ramp jumps
  3.92→34.45 N; C vs B at same ε: +10.5% [ADV-CFD]. Prior report carried the
  totals; the exit-vs-ramp migration mechanism is the delta.
- Δ7 Sonic-injection inlet static state (4.42 atm, 884.96 K) for P_0 = 8 atm,
  T_0 = 1000 K, Eqs. (10)-(13) three-branch inlet (p. 7) — minor method pin.
- Δ8 Reference-list corrections to the prior report's §5: [26] is PCI 37(3)
  (prior wrote 37(2)); [27] Goto has TEN authors (incl. Nakata, Uchiumi,
  Higashino); [39] Zhu 2020 title says "rotating detonation CHAMBER" (prior
  wrote "engine"); [34] Kurita author list is Kurita, Jourdaine, Tsuboi,
  Ozawa, Hayashi, Kojima (no Ozawa/Hayashi order swap). Pinned by extraction.
**OMISSIONS of the standing report (named, minor):** no visual read of
Figs. 7-13 (repaired here); no Δ2/Δ4 numbers; ṁ-cause not credited (Δ3).
Nothing in the standing report is WRONG on re-read; F1's filename correction
duty remains open (file still named ..._ga_gradient_optimization.pdf).

---

## 1. IDENTITY + METHOD SUMMARY (with pages)

Stands in the prior report §0-§2 (citation p. 1; solver/chemistry/grid §2.1
pp. 3-4 and §3.2 p. 6; design method §3.1 pp. 4-5; validation §2.2 pp. 4-5).
One-paragraph digest for this campaign's synthesis: 3-D unsteady RANS (k-ω
SST) + PaSR, in-house rhoHLLCFoam (OpenFOAM), HLLC + 2nd-order CN; premixed
Jet-A(C12H23)/air, Ajmani 21-species/37-reaction mechanism (Table 1 p. 3),
NASA-poly thermo (Table 2 p. 4); annular chamber R_in = 12.6 mm, R_out =
14.6 mm, A_c = 170.90 mm², L_c = 40 mm (p. 5); ~12M cells, Δ_min 0.125 mm,
Δt 5e-9 s, 1500 μs run (p. 6); inlet P_0 = 8 atm, T_0 = 1000 K, three-branch
injection Eqs. (10)-(13) (p. 7); ambient P_a = 0.36 atm (Fig. 15, p. 11).
FOUR cases (Table 4, p. 5): A flat ramp ε=100%, B flat ramp ε=87.3%, C
Angelino isentropic ramp ε=87.3% (Eqs. (5)-(9), γ=1.26, NPR=24.9, M_e=2.69,
A_e=581.08 mm², R_lip=13.6 mm, ω_t=50.47°), D = C truncated to 40% (L_s =
13.60 mm, R_b = 4.11 mm). Design inputs = TIME-AVERAGED values (p. 5).

## 2. FINDINGS LEDGER (paper results + design-method steps, with pages)

Standing rows (prior report): design-map steps Eqs. (5)-(9) pp. 4-5; CJ
validation Table 3 p. 5 (errors < 1.49%); grid independence Fig. 6 p. 6;
P_c reconstruction Eq. (14) + η Eq. (15) p. 9; pressure gain Table 5 p. 10
(A −7.4% / B +8.9% / C +13.2% / D +13.1%); thrust bookkeeping Eqs. (16)-(19)
pp. 10-11; component split Table 6 p. 12 (C: 134.64/34.45/0/−2.73 N; D:
F_base = −1.07 N); performance Table 7 p. 12 (Isp 2384.5/2536.1/2826.2/
2792.8 s; C_F 1.139/1.158/1.231/1.216; δ 81.3/81.2/85.8/84.8%); ramp-tail
drags p. 11; 16-segment F_ramp decomposition Fig. 15c-d p. 11 ("almost all of
the F_ramp is provided by the first 40% of the aerospike"); base pressure
~0.16 atm vs P_a 0.36 atm p. 12; truncation cost 1.2% Isp / 2.21 N p. 12.

NEW rows (this read):
| ID | Finding | Page | Class |
|---|---|---|---|
| A-L1 | Mass-weighted average exit Mach ≈ 2.58 vs design 2.69 (~4% low); causes named: nonhomogeneous throat flow, no exact PM expansion | 7 | ADV-CFD |
| A-L2 | Reflected shock from constriction throat (B) / cowl lip (C) propagates upstream into combustor; "very weak, does not disturb" the RD wave | 7, 8 (Fig. 8d), 9 (Fig. 11) | ADV-CFD |
| A-L3 | Reflected shock blocks fuel intake → ṁ_f drops A→D 6.17→6.00 g/s (cause declared for the unmatched-ṁ comparison) | 12, Table 7 | ADV-TXT |
| A-L4 | Constriction-only thrust gain +4.4% (A→B); ramp-shape gain +10.5% (B→C, same ε); mechanism = F_exit −7.7 N vs F_ramp +30.5 N migration | 11 | ADV-CFD |
| A-L5 | Corpus numbers carried: choked nozzle +4~7% Isp [26]; Fotia 3~7% stagnation-pressure max at ε=80% [30]; Bach ε 100→50% [56]; Betelin center-body 6/9/9.75 cm [29] | 2, 10 | ADV-TXT (second-hand) |
| A-L6 | Case A (ε=100%, NO geometric throat) also reported congested with M_t = 1.0 — choking claim extends to the unconstricted case | 7, 9 | ADV-TXT (F5 sharpener) |
| A-L7 | Averaged plume of C: NO Mach disks, only weak recompression waves; A/B averaged plume: expansion fan + Mach disk + free-jet boundary | 7-9 (Figs. 9, 12) | ADV-FIG |
| A-L8 | Case D adds lip shocks + trailing shocks + enclosed subsonic recirculation at base; inner combustor field unaffected by truncation (Fig. 11 caption) | 7, 9 | ADV-FIG |

## 3. TOPOLOGY ATLAS (per field figure; visual reads; all [ADV-FIG])

Channel key = forchetta channels (i)-(vi) of BRIEF_blocco2_phaseD.md
CENTERPIECE (5); T-RED terms per phaseD_r22f_centerpiece.md §2.1-2.3.

**Fig. 7 (p. 7) — instantaneous 3-D field, Cases A/B** (T on symmetry plane,
p on inner wall/ramp): plume is manifestly NON-axisymmetric and time-varying;
hot lobed structure downstream, labeled Mach disk inside the plume; wall-
pressure footprint on the ramp is azimuthally banded (the rotating wave's
footprint). → Informs channel (i)/(ii): the instantaneous field is the 3-D
unsteady truth the reduction drops; the banded ramp footprint is the
sweep-advective K family (K_u, K_v rows) made visible on a plug wall.
Same phenomenon class as the exhibit of record (Harroun 2021 Fig. 18,
centerpiece §2.3) at ADVISORY grade — a SECOND published instance.

**Fig. 8 (p. 8) — unrolled r-θ combustor field, Cases A/B** (T and ||∇ρ||):
textbook RD cell topology labeled by the authors: detonation front, oblique
shock, slip line, deflagration surface, wedge-shaped fresh-gas layer; Case B
(d) additionally shows a REFLECTED SHOCK WAVE from the constriction throat
crossing the chamber diagonally back upstream. → This is the azimuthal-
structure content par excellence: detonation front + oblique shock + slip
line = the front-atom content of K ((J) channel, centerpiece §2.2); the
reflected shock = an azimuthally-structured wave family GENERATED BY THE
NOZZLE, i.e. a nozzle→interface feedback path (threat T2). Informs channel
(ii) WORST cell (azimuthally-fed segments) and the seam declaration that
interface data are nozzle-independent (see §5).

**Fig. 9 (p. 8) — time-averaged plume, Cases A/B** (p and Ma, meridional):
averaged field is cleanly axisymmetric under-expanded-jet topology: expansion
fan at chamber exit, Mach disk on axis (~z=5 cm), free-jet boundary, second
weaker cell downstream; supersonic annular jet merging on axis. → Channel
(iv) BEST-side qualitative datum: the average IS a classical jet (their
abstract claim verified on the plot); also the (i) seam: instantaneous
asymmetry (Fig. 7) vs axisymmetric mean (Fig. 9) is the paper's own
demonstration that the mean is well-defined — VALUE-level only, nothing about
optimum location (channel (vi) untouched by it).

**Fig. 10 (p. 9) — instantaneous 3-D field, Cases C/D**: with the inward-bend
cowl lip the lateral expansion is visibly confined; plume hugs the spike;
banded azimuthal structure persists on the ramp. → Same consumption as
Fig. 7; additionally shows the cowl lip suppressing the divergence loss
mechanism (their design rationale) at instantaneous level.

**Fig. 11 (p. 9) — unrolled r-θ combustor field, Case C** (T, ||∇ρ||):
same RD cell topology as Fig. 8 PLUS a labeled reflected shock wave from the
cowl lip propagating upstream; caption states the truncated spike (D) does
not affect the inner field (not shown for D). → Channel (ii) + threat T2
(cowl-lip reflection exists even without a flat constriction wall); the
"truncation does not affect inner field" claim is an ADV-CFD datum that the
BLOCCATO-9 truncation decision can cite (truncation decouples from chamber).

**Fig. 12 (p. 9) — time-averaged plume, Cases C/D** (p, Ma): Case C: NO Mach
disk — expansion fan at lip + weak recompression waves only, smooth
supersonic ramp flow; the authors read this as near-isentropic expansion
(minimum loss). Case D: lip shocks + trailing shocks + enclosed subsonic
recirculation bubble at the truncated base (blue wedge on axis, ~z=1-2 cm).
Mass-weighted exit Mach ≈ 2.58 vs design 2.69 (text, p. 7). → Channel (iv):
the 2.58-vs-2.69 pair is a QUANTIFIED mean-design-point miss (~4% Mach,
value-level) attributable to exactly the non-uniformity our reduction terms
carry; channel (v): the D-case base bubble is the base-pressure model-form
regime (R8 two-regime closure; base ~0.16 atm = 44% of ambient, p. 12 —
prior F12b stands, now with its flow topology seen).

**Fig. 13 (p. 10) — streamlines, Cases B/C/D** (overall + ramp closeups):
B: streamlines diverge outward after the parallel shroud (divergence loss
visible); C: streamlines turn at the lip and leave PARALLEL to the axis
(their design closure ω_t = ω(M_e) visibly achieved in the mean); D:
basically parallel with the recirculation bubble closing on the blunt base.
→ Channel (vi) context: the exit-parallelism is a KINEMATIC closure achieved
in the mean field — not a stationarity condition (prior F7 stands); the
visual parallelism is the mean-field face of their design bet.

**Fig. 15 (p. 11) — P_w(z) + 16-segment F_ramp bars, Cases B/C**: P_w decays
monotonically from ~3 atm (C) crossing BELOW the dashed P_a = 0.36 atm line
(B at z>0.72 cm, C at z>2.0 cm); bar charts show first-segment dominance
(C: ~19-20 N in segment 1) and small NEGATIVE bars beyond the crossing. →
The measured non-stationarity of their contour (prior F8 stands); the
segmented-density diagnostic (prior F12a) seen; informs channel (vi): a
design whose tail produces drag is not at a thrust argmax — the visible
signature our transversality/corner machinery is built to remove.

(Figs. 1-2, 5, 6 = validation/mesh plots; topology content nil for our
channels — declared, not skipped silently. Fig. 3 = geometry schematics,
Fig. 4 = case schematics, Fig. 14 = thrust-surface schematic: definitional.)

## 4. CONFRONTATION vs THE CENTERPIECE DRAFT (phaseD_r22f_centerpiece.md)

Per part; verdict + one bearing sentence + draft anchor.

**Part 1 [T-DISC] (fiber separation, p-only conviction)** — SUPPORTS
(indirect). The paper's design map consumes only (⟨p⟩, ⟨M⟩, γ, NPR) — a
projection-class pipeline in the sense of D1.2 (§1.0) — and its measured
δ-shortfall (14.2% of ideal, p. 12) is attributed by the authors to time-
slice non-uniformity the projection cannot see, which is external ADVISORY
evidence that fiber content matters; the paper never measures swirl (prior
hyp. 11), so it can neither test nor threaten [T-DISC-1/2] (§1.1-1.2), and
its evidence does not decompose into the E_theta debit.

**Part 2 [T-RED] (reduction-residual operator)** — SUPPORTS. Figs. 8/11
display the exact front-atom + sweep-advective phenomenon class of K (§2.1,
§2.3 disposition table), giving a SECOND published exhibit beside Harroun
Fig. 18; the reflected-shock feedback (A-L2) adds an azimuthal wave family
that originates at the NOZZLE — a mechanism adjacent to the data-anchored-
shadow pin (§2.3(b)): it is chamber-interior structure fed from downstream,
inherently outside a march anchored on interface data alone. DIFFERS (scope):
their fields are viscous-reactive RANS — the separation/deflagration content
is boundary-priced in our frame (§2.3(c)), so figure readings are consumed at
mechanism level only, never as magnitudes of K terms.

**Part 3 [M-RED] (measurement spec)** — SUPPORTS (as external anchor, not as
data). The paper supplies corpus-scale anchors the spec's families cannot
generate (δ = 81-86%, mean exit-Mach miss 2.58 vs 2.69, base ~0.16 atm) and
the 16-segment ramp-density diagnostic already adopted (prior F12a); none of
its numbers can enter B-1..B-4 bands (uncertified, viscous, reactive — §3.3
families are in-house by construction). No conflict.

**Part 4 [R22-CFD re-scope]** — SUPPORTS both halves. CFD-1 cost-class: this
is a ~12M-cell, 3e5-step coupled unsteady computation per case (p. 6) —
consistent with the "largest single compute item" pricing (§4.3); and the
paper is a published instance of what CFD-1-adjacent evidence looks like
WITHOUT certification (no error bars on any headline number). Crucially it
does NOT change the addendum (c) no-external-referee fact: its C_F/δ are
built from time-averaged thrust and a state-averaged reconstructed P_c
(Eq. (14), p. 9; Eqs. (20)-(23), p. 12) — **no unsteady c_F, and no
2D-per-phase-vs-3D-unsteady discrimination anywhere** (checked honestly:
the paper contains no per-phase or 2D reduced computation at all; it
compares 3-D unsteady cases to each other only).

**Part 5 forchetta cells** —
- (i) time-coupling: SUPPORTS BEST-cell reading qualitatively (Fig. 7 vs 9:
  the mean exists and is clean); adds no number; the class-exit WORST side
  untouched (their wave is single-mode stable by construction, p. 7-8).
- (ii) azimuthal reduction: SUPPORTS WORST-cell mechanism list (Fig. 8/11
  topology; A-L2 feedback); the paper's UNDECOMPOSED total loss (14.2% off
  ideal, incl. viscous + shocks) is CONSISTENT with "single-digit % plausible,
  >10% not excluded" and cannot tighten it (no decomposition offered).
- (iii) swirl: NEUTRAL-SUPPORTS the program's differentiation: the leading
  published RDE-aerospike design paper never books, measures, or mentions
  swirl (prior hyp. 11 re-verified) — the channel's numbers stay swirl5f-only.
- (iv) averaging adequacy: SUPPORTS the sizing-level BEST cell with a new
  quantified datum (A-L1: exit-Mach miss ~4%, causes named); leaves the
  ranking threshold (R26) OPEN — their 4-case spread is CONFIGURATION-scale
  (tens of N), not in-class contour ranking.
- (v) model-form: SUPPORTS (γ=1.26 closed forms vs NASA-poly CFD, prior F10;
  base-regime topology seen, Fig. 12b/13f).
- (vi) optimum-shift: SUPPORTS the concern's premise at ADVISORY grade: their
  own best contour carries a drag tail (Fig. 15b) and a 4% design-point miss
  (A-L1) — value-adequate yet visibly non-stationary; no gradient-level
  number exists in the paper (consistent with addendum (b) expectations).

## 5. THREAT SCAN ("cosa potrebbe schiacciare il progetto")

T-A1 [value-proposition; = prior F6, re-affirmed at figure level] A
zero-effort 1-D mean design reaches δ = 85.8% (Table 7, p. 12). Row hit:
none (rhetoric only — program's motivation). Falsifier protocol already
in-paper: baseline is a straight cone (conical-vs-Angelino gap, not
Angelino-vs-optimal); Case C's own drag tail (Fig. 15b) + 2.58-vs-2.69 miss
show non-stationarity. Held class: ADV-CFD. **Does not fire.**

T-A2 [data-nozzle coupling — NEW] Reflected shocks from throat/cowl lip
propagate INTO the chamber and measurably shift ṁ_f (A-L2/A-L3, pp. 7-12):
the interface data are not strictly independent of the nozzle design. Row
hit: the standing scope pin "interface data given as pure periodic rotating
wave" (memory `periodic-wave-data-scope`; M0 VI.4bis; centerpiece D1.1
admissible class) and CFD-1's class-membership question (§4.1). Falsifier
protocol of the row: T0-flatness monitor + f_cycle contract field (A32) —
i.e., the coupling is DETECTED, not assumed away, by the class monitor; and
CFD-1 is the named decider for class membership on coupled fields. At held
evidence the effect is small (ṁ −2.8% A→D; "very weak... does not disturb",
p. 7 [ADV-CFD]) → **named, does not fire now; feeds CFD-1's case for a
coupled reference configuration.**

T-A3 [convergence-section recommendation] "The convergence section with
nozzle throat should be adopted in RDE" (abstract p. 1; η table p. 10):
pressure-gain bookkeeping favors ε < 100%. Row hit: none directly — the
program's fixed-exit-area / delta-carrier lemma (brief minor (c)) concerns
exit-area relaxation semantics, and constriction enters as a design-class
choice, not a theorem. The η numbers inherit the assumed M_t = 1.0 closure
INCLUDING for the throatless Case A (A-L6, p. 7/9) — the choking-advisory
discipline (prior F5; L4 margin rule) is the row of record and its falsifier
(monitored choking margin) already covers this. **No theorem hit; consumed
as context for minor (c) and the P-D confrontation (choked +50-60%).**

T-A4 [averaged-plume-suffices reading] A hostile reading of the abstract
("reasonable to use the time-averaged value... for nozzle design") could be
cited AGAINST the program's premise that the reduction gap matters. Held
evidence says otherwise inside the same paper: 14.2% unexplained loss
attributed to time-slice non-uniformity (p. 12) + the 4% design-point miss
(A-L1). Row hit: T-DISC/R22 averaging bet — evidence is CONFIRMING of "design
at the mean works at sizing level, unpriced at ranking level" (exactly R26's
open threshold). **Does not fire; sharpens the sizing/ranking split.**

**No further threats found** (stated explicitly): nothing in the paper
touches the quotient theorems ([T-T0P]), the fiber theorems, K-bar = 0, the
choking two-regime contract, or any M0 THEOREM/THEOREM* row; the paper
contains no optimizer, no adjoint, no per-phase computation, and no unsteady
c_F that could referee or contradict the forchetta table.

## 6. CONSUMPTION ARC (per finding — no orphan rows)

| Finding | Landing target |
|---|---|
| Atlas Figs. 7/8/10/11 readings | T-RED exhibit family: cite beside Harroun Fig. 18 at centerpiece §2.3 (ADVISORY, second instance); FIELD_ATLAS_targeted_c4.md candidate rows; forchetta (ii) WORST-cell mechanism footnote |
| Atlas Figs. 9/12 (averaged plume, no Mach disk in C) | forchetta (iv) BEST-cell footnote (external axisymmetric-mean datum); R22-CFD-2 context (what published averaged fields show) |
| A-L1 (2.58 vs 2.69, ~4% miss) | forchetta (iv) BEST cell: quantified external mean-design-point miss [ADV-CFD]; M-RED confrontation anchor (§3.4 B-1 external context, not band input) |
| A-L2/A-L3 (reflected-shock feedback, ṁ −2.8%) | threat T-A2 → periodic-wave-data-scope pin note + R22-CFD-1 dossier (§4.1 class-membership evidence); candidate registry threat item |
| A-L4 (+4.4% constriction / +10.5% shape; F_exit↔F_ramp migration) | synthesis commonality matrix (design-method column); forchetta (vi) context (thrust-migration phenomenology at configuration scale) |
| A-L5 (choked +4~7% Isp [26]; Fotia 3~7%; Bach ε sweep) | P-D confrontation seam (slot 4 + synthesis (e): choked +50-60% chamber-pressure claim); choking advisory context |
| A-L6 (M_t=1.0 asserted for ε=100%) | choking advisory (F5 row) sharpener — cite as the throatless-choking instance |
| A-L7/A-L8 (plume shock inventory; D base bubble) | forchetta (v) base-pressure cell (R8 two-regime) topology anchor; BLOCCATO row 9 (truncation 0.20) context: "truncation does not affect inner field" [ADV-CFD] + 1.2% Isp cost at 40% truncation (P-B seam) |
| Δ8 (reference corrections) | prior report errata note (ride the landing; no new registry row for P-A — existing row :614 gets path note per census-defect order) |
| §7 extraction list | synthesis MISSED-CLUSTER WANTED consolidation (dedup done below) |

## 7. REFERENCE-LIST EXTRACTION (census-defect repair duty)

Bearing on RDE-nozzle design/efflux/experiments; identities pinned by
extraction (pp. 13-14). Registry dedup: grep of docs/literature_registry.yaml
this window — already held: [26]=P-D (on disk, this campaign), [28]
harroun_2021 (:273), [33] miki_2020 (:641), P-A itself (:614). NOT in
registry (candidate WANTED rows for the synthesis):

1. [25] M. Fotia, T.A. Kaemming, J.R. Codoni, J. Hoke, F. Schauer,
   "Experimental thrust sensitivity of a rotating detonation engine to various
   aerospike plug-nozzle configurations", AIAA SciTech 2019 Forum, 2019.
   (Fotia nozzle configs — named by the brief; thrust sensitive to internal
   expansion ratio, p. 2.)
2. [30] M.L. Fotia, F. Schauer, T. Kaemming, J. Hoke, "Experimental study of
   the performance of a rotating detonation engine with nozzle", J. Propuls.
   Power 32 (3) (2016) 674-681. (3~7% stagnation-pressure max at ε=80%, p. 10.)
3. [27] K. Goto, J. Nishimura, A. Kawasaki, K. Matsuoka, J. Kasahara,
   A. Matsuo, I. Funaki, D. Nakata, M. Uchiumi, K. Higashino, "Propulsive
   performance and heating environment of rotating detonation engine with
   various nozzles", J. Propuls. Power 35 (1) (2019) 213-223.
4. [39] Y. Zhu, K. Wang, Z. Wang, M. Zhao, Z. Jiao, Y. Wang, W. Fan, "Study on
   the performance of a rotating detonation chamber with different aerospike
   nozzles", Aerosp. Sci. Technol. 107 (2020) 106338. (EARLIEST
   design-at-time-averaged precedent per p. 2 — prior report's litmap
   candidate, still unprocured.)
5. [29] V. Betelin, V. Nikitin, E. Mikhalchenko, "3d numerical modeling of a
   cylindrical rde with an inner body extending out of the nozzle", Acta
   Astronaut. 176 (2020) 628-646. (Center-body length 6/9/9.75 cm study.)
6. [34] N. Kurita, N.H. Jourdaine, N. Tsuboi, K. Ozawa, K.A. Hayashi,
   T. Kojima, "Three-dimensional numerical simulation on hydrogen/air rotating
   detonation engine with aerospike nozzle: effects of nozzle geometries",
   AIAA SciTech 2020 Forum, p. 0688. (P-D's own follow-on.)
7. [35] G. Angelino, "Approximate method for plug nozzle design", AIAA J.
   2 (10) (1964) 1834-1835. (THE design-method source; planar-only caveat
   already of record at registry :441.)
8. [36] G. Hagemann, H. Immich, T.V. Nguyen, G.E. Dumnov, "Advanced rocket
   nozzles", J. Propuls. Power 14 (5) (1998) 620-634.
9. [56] E. Bach, P. Stathopoulos, C.O. Paschereit, M.D. Bohon, "Performance
   analysis of a rotating detonation combustor based on stagnation pressure
   measurements", Combust. Flame 217 (2020) 21-36. (ε = 100→50% pressure-gain
   restriction datum, p. 10.)
10. [57] J. Ruf, P. McConaughey, "The plume physics behind aerospike nozzle
    altitude compensation and slipstream effect", AIAA 97-3218, 33rd JPC, 1997.
11. [58] S.B. Verma, "Performance characteristics of an annular conical
    aerospike nozzle with freestream effect", J. Propuls. Power 25 (3) (2009)
    783-791.
12. [55] R. Yokoo, K. Goto, J. Kim, A. Kawasaki, K. Matsuoka, J. Kasahara,
    A. Matsuo, I. Funaki, "Propulsion performance of cylindrical rotating
    detonation engine", AIAA J. 58 (12) (2020) 5107-5116. (Efflux/performance;
    marginal-bearing.)
13. [51] S.M. Frolov, V.S. Aksenov, V.S. Ivanov, S.N. Medvedev, I.O. Shamshin,
    "Flow structure in rotating detonation engine with separate supply of fuel
    and oxidizer: experiment and cfd", in: Detonation Control for Propulsion,
    Springer, 2018, pp. 39-59. (Plume-structure source [49-51] set for the
    under-expanded-jet similarity claim, p. 4.)
14. [50] D.P. Stechmann, "Experimental study of high-pressure rotating
    detonation combustion in rocket environments", Ph.D. Thesis, 2017.
    (Registry holds stechmann_2019 JSR :317 — the thesis is DISTINCT.)
15. [54] X. Li, W. Yao, X. Fan, "Large-eddy simulation of time evolution and
    instability of highly underexpanded sonic jets", AIAA J. 54 (10) (2016)
    3191-3211. (Their steady-jet comparator class; marginal-bearing.)

NEGATIVE census (search-proven on the extracted text): the brief's named
items "Ma hot-fire", "Goto vacuum aerospike", "Zhou conical" do NOT appear in
P-A's reference list (H. Ma appears only as co-author of [7]/[24]
plane-radial ignition papers; Goto's only entries are [27]/[37]/[55]; Zhou
only as co-author of [7]/[20]/[21]/[24]) — those candidates must come from
P-B/P-C/P-D lists.

## 8. PAPERS NEEDED

None blocking for this deliverable. Procurement candidates = §7 rows 1-5
(Zhu [39] first: the earliest average-then-design precedent; then Fotia
[25]/[30], Goto [27], Betelin [29]) — consolidation owner = slot-5 synthesis.

## 9. MACHINE SUMMARY

- paper: liu_2022 (P-A), pages read 14/14, ALL rendered visually.
- standing-report diff: 12 prior findings STAND (0 contradicted), 8 deltas
  (Δ1-Δ8), 3 omissions repaired; NO new registry row (path note on :614 per
  census-defect order).
- new findings ledger rows: 8 (A-L1..A-L8); topology atlas: 8 figures read
  (Figs. 7, 8, 9, 10, 11, 12, 13, 15) + 6 non-topology figures declared.
- confrontation: Part 1 SUPPORTS (indirect), Part 2 SUPPORTS + scope DIFFERS,
  Part 3 SUPPORTS (anchor-only), Part 4 SUPPORTS (incl. addendum (c)
  no-unsteady-c_F check: CONFIRMED ABSENT), Part 5: (i)-(vi) all touched, 0
  cells contradicted.
- threats: 4 scanned (T-A1..T-A4), 0 fire at held evidence; T-A2
  (data-nozzle coupling) = the one NEW named threat, routed to CFD-1 +
  T0-flatness monitor.
- reference extraction: 15 bearing entries (11 registry-new candidates,
  3 marginal, 1 thesis-distinct), 3 named-candidate absences search-proven.
- consumption arcs: 10 rows, all with named landing targets; 0 orphans.
