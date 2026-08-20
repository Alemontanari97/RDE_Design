# SYNTHESIS — NOZZLE-RDE ARRIVALS CAMPAIGN (P-A..P-D)

Slot 5 of BRIEF_nozzle_rde_arrivals_study.md (S-FOUNDATIONS-C4,
2026-08-20). SHARED RULES accepted: env pinned (nothing installed); ONLY
this file written; page anchors carried from the four study files (each
anchor below names paper + printed page, carrier = the slot file);
evidence classes carried per statement ([REP] paper text/number, [FIG]
slot agent's visual figure reading, [INF] labeled inference, [ADV] =
everything from these papers is published-CFD ADVISORY evidence, never a
measurement of ours).

INPUTS READ THIS WINDOW (all [FULL]):
- NOZZLE_RDE_STUDY_pA_liu_wang_2022.md (P-A, 14/14 pp. read by slot 1)
- NOZZLE_RDE_STUDY_pB_li_xu_2023.md (P-B, 22/22 pp., slot 2)
- NOZZLE_RDE_STUDY_pC_li_xu_2025.md (P-C, 18/18 pp., slot 3)
- NOZZLE_RDE_STUDY_pD_jourdaine_2019.md (P-D, 9/9 pp., slot 4)
- Confrontation frame: BRIEF_blocco2_phaseD.md (CENTERPIECE + forchetta
  (i)-(vi)), BRIEF_blocco2_phaseD_addendum_c4.md ((b)/(c)/(a)/(e)),
  phaseD/phaseD_r22f_centerpiece.md (parts 1-5, all 696 lines),
  docs/rde_nozzle_PROGRESS.md BLOCCATO row 9 (:240-249).
- Dedup instrument (SR-12, measured this window):
  `grep -niE "fotia|goto|zhu|...|paxson" docs/literature_registry.yaml`
  + targeted reads of rows liu_2022 (:614-621), vander_veen_1974
  (:427-434), onofri_2002_plug_survey (:436-441), zucrow_hoffman_1977_
  vol2 (:467-473), stechmann_2019 (:317-319), kaemming_paxson_2018,
  harroun_2021/2020, miki_2020, paxson_miki_2022, ornano_2017.

==============================================================================
## (a) COMMONALITY / DIFFERENCE MATRIX

| Axis | P-A Liu 2022 (PKU) | P-B Li-Xu 2023 (NUAA) | P-C Li-Xu 2025 (NUAA) | P-D Jourdaine 2019 (KIT/AoyamaG) |
|---|---|---|---|---|
| Design method | Angelino approximate isentropic ramp at time-averaged inputs (gamma=1.26, NPR 24.9, M_e 2.69; pp. 4-5); 4-case discrete trade study, NO optimizer (prior F1) | Axisymmetric MoC (Zucrow-Hoffman units) + Rao/Vander-Veen shrouded-plug MAX-THRUST variational surfaces with averaged p_b corner (pp. 5-8) | None new: takes P-B's max-thrust MoC design as baseline; studies axial cowl/spike misalignment + dynamic actuation (pp. 2, 4) | NONE: fixed 50-deg conic spike, explicitly non-optimized (F-19, p. 3450); method content = performance-evaluation chain Eqs. (1)-(6) |
| Averaging stance | Design at TIME-AVERAGED values, justified a posteriori (Fig. 7 vs 9); mean plume clean axisymmetric | Time-averaged STAGNATION constraints "empirically recognized" (F-01, p. 5, citing P-D); paired steady-averaged vs transient runs | Paired transient vs steady-reference (mass-weighted averaged inflow, p. 8); time-avg wall p obeys steady area law (L16, p. 13) | THE source claim: "time-averaged exhaust flow is similar to a classic axis-symmetric steady exhaust flow... classic design method could be used" (F-22, p. 3450) |
| Truncation | Case D = C truncated (L_s 13.60 mm); cost 1.2% Isp / 2.21 N (p. 12); "first 40% of aerospike gives almost all F_ramp" (Fig. 15) | SWEEP DL_spike = 20-80% L_cowl (removed length / cowl length, p. 10); transient optimum 40% L_cowl (~retains 60% of spike [INF]); cliff -5.78% at 80% | One fixed truncated spike (hump 53 mm); no truncation sweep | None (full conic spike) |
| Choking | Constriction recommended (+4.4% thrust A->B; eta table p. 10); M_t = 1.0 asserted EVEN for throatless Case A (A-L6) | Geometric throat = design factor 1 (F-01); contraction ratio 1.1 | Throat area ratio drifts ~6% under actuation (L2); contraction 1.115 | THE topic: choked raises chamber time-avg static p +50%/+60% (F-14), Isp +4-7% (F-8); chamber goes SUBSONIC with upstream-running reflected shock (F-5) |
| Loss decomposition | NONE offered: 14.2% off-ideal undecomposed (p. 12) | THREE parts [REP p. 1]: sweeping shocks / viscous passage / base-recirculation dissipation; steady-vs-transient gap ~2.8% uniform <=60% trunc (F-11) | No formal decomposition; attribution to asymmetric moving shocks + viscous (L11); gap 0.2-1.5% both signs [FIG p. 11] | Model-form admission: trends match experiment, "absolute values are completely different" (F-24, p. 3451) |
| Deflection / swirl magnitudes | NEVER measured or mentioned (prior hyp. 11 re-verified) | Exit V_cir 327.5-383.4 m/s on V_x ~1910 (F-22, Fig. 24d; film-cooled configs ONLY, cooling-modulated — no uncooled baseline exists [REV-NRS-3]) => swirl angle ~9.7-11.4 deg [INF]; RMSD_theta 14.42-18.57 deg: P-B prints NO RMSD formula anywhere (nomenclature p. 2: "flow deflection angle" only) — definition UNDER-DETERMINED at held evidence; never booked against B5 in any direction [REV-NRS-2] | RMSD_theta 8.16-14.63 deg = deviation from AXIAL (eq. 20 conflates divergence + swirl — upper proxy only); rotating lateral force ~25-35% of axial thrust [INF from Fig. 21] | NONE reported (F-25) — absence is itself a datum |
| Pressure-gain accounting | State-averaged reconstructed P_c Eq. (14); PG A -7.4% -> C +13.2% (Table 5, p. 10) | EAP per Kaemming-Paxson (Eq. 33); PG -19..-21% no-cooling, -16.48% final config (Table 5, F-25) | PG not central; C_fx 0.9425-0.968; throat total p +3.89% via retraction (L10) | Pc = static time-averaged (F-13); "pressure gain" = CHAMBER PRESSURIZATION BY CHOKING (definitional, F-14); Cf = F/(At*Pi) ~1.0-1.2, NOT comparable to P-B/P-C axial C_fx ~0.94 (definitional seam) |

CROSS-PAPER COMMONALITIES (all [ADV]):
C-1. All four practice or endorse the average-then-classical-design bet;
  P-D is the cited origin (P-B F-01 cites P-D verbatim). The field's
  premise = our R26 open question, never tested at ranking level by any
  of them at per-phase grade.
C-2. All four display the SAME instantaneous/mean dichotomy: rotating
  oblique-shock azimuthal structure at the instant (P-A Figs. 7/8/10/11;
  P-B Fig. 14-right; P-C Fig. 10-left; P-D Fig. 9) vs clean axisymmetric
  time-mean (P-A Figs. 9/12; P-B Fig. 14-left class; P-C Fig. 10-right;
  P-D Fig. 4). Four independent published instances of the K-operator
  phenomenon class (centerpiece §2.3) beside Harroun Fig. 18.
C-3. All four exhibit chamber-nozzle COUPLING: reflected shocks into the
  combustor + mdot shift -2.8% (P-A A-L2/A-L3); exit-BC feedback on
  p0/T0 (P-B Fig. 16); +3.89% throat total p under actuation (P-C L10);
  +50-60% Pc and subsonic chamber under choking (P-D F-14/F-5).
C-4. All favor constriction/choking for chamber pressure; magnitude
  ladder small->huge: P-A +4.4% thrust, P-C ~4% p0, P-D +50-60% Pc.
C-5. NONE is a per-phase reduction; the "steady" companion where it
  exists (P-B/P-C) is a GLOBAL averaged-inflow axisymmetric run — a
  cruder reduction than ours. None certifies class membership; none
  carries error bars; no optimizer appears anywhere in the four papers.
DIFFERENCES THAT MATTER: only P-B/P-C carry any swirl-adjacent numbers;
only P-B sweeps truncation; only P-D isolates choking; only P-A gives a
quantified mean-design-point miss (exit Mach 2.58 vs design 2.69, ~4%,
A-L1, p. 7); C_f definitions differ across P-D vs P-B/P-C (seam above).

==============================================================================
## (b) CONSOLIDATED THREAT LEDGER

Slot threats T-A1..4 (P-A), TH-1..4 (P-B), T-C1..4 (P-C), T-1..4 (P-D)
consolidated to 8 deduped items. Held evidence for every item = [ADV]
(published CFD, P-D self-graded "absolute values completely different").
Dispositions: FIRES / DOES-NOT-FIRE / NEEDS-F2(or CFD)-MEASUREMENT.

CT-1 DATA-NOZZLE COUPLING / design-dependent interface data
  (= T-A2 + P-B Fig.16 + T-C2 + P-D T-1; the sharpest consolidated threat).
  Evidence ladder: mdot -2.8% via reflected shock (P-A pp. 7-12); p0/T0
  drift with truncation (P-B Fig. 16 p. 10); +3.89% throat total p at
  fixed operating point (P-C p. 11); +50-60% Pc, subsonic chamber,
  upstream shock transit under choking (P-D pp. 3446-3449).
  ROW/THEOREM HIT: standing scope pin "interface data = pure periodic
  rotating wave, given" (memory periodic-wave-data-scope; M0 VI.4bis;
  centerpiece D1.1 pins H3/H9) + fixed-interface premise behind the
  delta-carrier frame (brief minor (c)) + R22-CFD-1 (centerpiece §4.1).
  FALSIFIER PROTOCOL OF RECORD: T0-flatness monitor + f_cycle contract
  field (A32, registry :1925); class-membership decider = CFD-1.
  DISPOSITION: DOES NOT FIRE — scope boundary, not theorem breaker:
  every centerpiece statement is conditional on the data class, and
  choking-scale moves are outside it. BUT the project-level fact stands:
  the largest published performance lever (choked +4-7% Isp) lives
  OUTSIDE the fixed-interface design class. NEEDS CFD-1 (scheduling
  input strengthened; joins §4.3 dossier). Carry: P-C is a working
  paired-run template; P-D is a CAUTIONARY spec input (micro-scale,
  idealized — poor reference-configuration candidate).

CT-2 OPTIMUM BLINDNESS along real design directions
  (= TH-1 + T-C1 + P-A drag-tail/4%-miss context).
  Evidence: P-B Fig. 15 (p. 10): steady C_fx ~flat 0.965-0.971 where
  transient has optimum at 40% (+0.52%) and cliff at 80% (-5.78%);
  P-C Fig. 13 (p. 11): mid-ranking flip between steady and transient
  orderings at gap 0.2-1.5% vs config spread ~2.5 pts, argmax HELD;
  P-A Fig. 15b + A-L1: best contour carries a drag tail + 4% mean miss.
  ROW HIT: forchetta channel (vi) + channel (iv) WORST / R26 ranking
  threshold (registry :2147). FALSIFIER OF RECORD: the (vi) cell's
  |argmax shift| <= delta/mu schema (mu = measured engine curvature);
  deciders M-RED gradient measurement + R22-CFD-2.
  DISPOSITION: DOES NOT FIRE — the cells already price exactly this
  mechanism; these are the SECOND and THIRD empirical markers beside the
  Paxson-Miki shroud line. Strengthens the priced threat; NEEDS
  F2-MEASUREMENT (M-RED) to convert [SE] to measured.

CT-3 UNSTEADY-c_F EXISTENCE vs addendum (c) wording (= TH-2 + T-C3).
  Evidence: unsteady/steady C_fx pairs EXIST at CFD class in P-B
  (Fig. 15, 2.8% gap) and P-C (Fig. 13 + time-resolved C_fx Fig. 20b);
  ABSENT in P-A (cycle/state-averaged only) and P-D (cycle-averaged
  only) — the brief's honest check, executed in (e).6 below.
  ROW HIT: addendum (c) structural fact (forchetta-table header
  delivery-check item). DISPOSITION [REV-NRS-1]: **FIRES AS
  ENRICHMENT-AMENDMENT (narrative completeness), the campaign's only
  firing item**. The addendum-(c) sentence of record is STRICTLY TRUE
  as written: its restrictive clause ("...THAT DISCRIMINATES the
  2D-per-phase-averaged prediction against 3D-unsteady truth") is part
  of the sentence — no freestanding "the literature carries NO unsteady
  c_F datum" phrasing exists anywhere in the record — and the P-B/P-C
  pairs discriminate only a GLOBALLY averaged steady companion at
  same-solver URANS. The record sentence needs no defensive rewrite.
  What fires is an ENRICHMENT of the nearest-referee inventory: the
  landing note names P-B Fig. 15 / P-C Figs. 13+20b as the nearest
  referee-shaped same-solver pairs, each disqualified by the two stated
  reasons (companion GLOBALLY averaged, not per-phase; truth
  same-family URANS, not external/experimental). Enrichment text at
  (e).6.

CT-4 TRUNCATION 40%-OPTIMUM vs default 0.20 (= TH-3; definitions in (e).2).
  ROW HIT: BLOCCATO row 9 ("default troncamento RESTA 0.20, banda
  0.20-0.40 stampata; esecuzione gated ADR-D4", PROGRESS :240-249).
  DECIDER OF THE ROW: the ADR-D4 implementation-window re-evaluation.
  DISPOSITION: DOES NOT FIRE NOW — definitions are NOT commensurable
  without mapping (P-B's ratio = length REMOVED / L_cowl; ours = plug
  retention convention), their ambient (6141 Pa) and base-flow class
  differ, and evidence is [ADV] + [INF] figure geometry. CARRY (duty):
  definition-mapping rider note MUST ride the ADR-D4 dossier; P-B's
  transient band argues against the deep-truncation end ON THEIR CONFIG.

CT-5 SINGLE-MODE PIN REALISM (= P-D T-2). Solver locks to one wave
  "in contrary with experiments" (P-D F-1, p. 3446); internal conflict
  on mode-count sensitivity (F-2 no-difference vs Tsuboi 2017 -10% Isp)
  => NO insensitivity claim consumable. ROW HIT: pin H3/H-A1 class
  membership (already priced: R20 residue, registry :2147; H-AM1 exit
  M0:1040-1044). FALSIFIER: T0-flatness + f_cycle (A32); decider CFD-1.
  DISPOSITION: DOES NOT FIRE (already priced); mitigant-free carry.
  Realization instance (CFD class only) [REV-NRS-8]: P-C Figs. 15/16
  show clean single-mode periodicity at all stations, all five configs
  [FIG pp. 12-13] — evidences CFD-realizability of the pure-periodic
  pin class (G-02's phrasing), NOT hardware realism, which is CT-5's
  actual concern (R20 residue).

CT-6 ABSOLUTE-VALUE UNRELIABILITY of published RDE-nozzle CFD
  (= P-D T-3 + T-C4 + P-A prior F10 gamma inconsistency). ROW HIT: none
  — a threat to OVER-CONSUMPTION, not to a row. DISPOSITION: DOES NOT
  FIRE; becomes the STANDING CONSUMPTION RULE of this campaign: no
  P-A..P-D number enters any band, bar, or referee position; mechanism/
  topology and gap-SCALE readings only, always [ADV]-labeled.

CT-7 VALUE-PROPOSITION RHETORIC (= T-A1 + TH-4): zero-effort 1-D mean
  design reaches delta = 85.8% (P-A Table 7); the field premise is
  "empirically recognized" (P-B F-01). ROW HIT: none (program
  motivation). DISPOSITION: DOES NOT FIRE — the same papers carry the
  counter-evidence (14.2% unexplained loss, drag tail, 4% miss, ranking
  flip); if the premise were wrong at ranking level, the per-phase
  program is the fix, not the victim.

CT-8 CONVERGENCE-SECTION RECOMMENDATION (= T-A3): "convergence section
  with throat should be adopted" (P-A abstract). ROW HIT: none directly
  — constriction is a design-class choice; the eta numbers inherit the
  un-certified M_t = 1.0 closure incl. the throatless case (A-L6).
  DISPOSITION: DOES NOT FIRE; consumed as context for minor (c) and as
  the weak sibling of CT-1's choking ladder; choking-advisory discipline
  (F5 row; L4 margin rule) already covers it.

TALLY: 8 consolidated threats; 0 BREAK; 1 ENRICHMENT-AMENDMENT fires
(CT-3, narrative completeness — record sentence true as written
[REV-NRS-1]); 1 rider duty (CT-4 -> ADR-D4); 6 do-not-fire (of which CT-1,
CT-2 strengthen already-priced threats and name their F2/CFD deciders).
No THEOREM/THEOREM* row of record is contradicted by any of the four
papers — each slot states this explicitly; re-verified here against the
centerpiece part list ([T-DISC-1/2], K-bar=0, [T-T0P], flux nullity,
delta-carrier, choking two-regime: all untouched).

==============================================================================
## (c) GRAFT LIST (consumption arcs consolidated; ONE landing each; deduped)

G-01 Exhibit-family graft -> centerpiece §2.3 (T-RED physical exhibit):
  add the four published instances beside Harroun Fig. 18, one line each
  with pages: P-A Figs. 7/8/10/11 (banded ramp footprint + reflected
  shocks); P-B Fig. 14-right (sweeping oblique wave in the diverging
  section); P-C Fig. 10 (one-sided internal shock + deformed base, the
  cleanest side-by-side with its own axisymmetrized steady twin);
  P-D Fig. 9 (rotating front + oblique shock + triple point; choked
  panel: azimuthal wave content reaching UPSTREAM). All [ADV-FIG].
  ATLAS RIDER [REV-NRS-5]: the P-A figure set and the P-D Fig. 9
  reading are ALSO candidate rows for FIELD_ATLAS_targeted_c4.md
  (blocco3, the addendum-(a) in-flight carrier) — restores the P-A/P-D
  slot atlas landing targets dropped undeclared in v1.
G-02 Forchetta (i) cell note: P-C Figs. 15/16 clean periodicity =
  published realization of the pure-periodic pin class; P-D choked
  subsonic chamber = boundary-text support (coupling received from
  outside the class). No number moves.
G-03 Forchetta (ii) BEST provenance: P-B 2.8% uniform steady-vs-transient
  C_fx gap (<=60% trunc) + P-C 0.2-1.5% both-signs gap = two external
  single-digit-% instances [ADV] (cruder-than-per-phase reduction — each
  an UPPER-class analog, stated). WORST note: P-B 80% divergence
  (-5.78%, "flow swirling induces the trailing shock wave in advance")
  = configuration-dependent growth mechanism.
G-04 Forchetta (iii) cell: P-B exit V_cir 327-383 m/s => eps_theta
  ~0.17-0.20, swirl angle ~9.7-11.4 deg [INF] — independent external
  datum: eps_theta INSIDE the DISPATCH §9 band (0.15-0.20); swirl
  angle OVERLAPPING B5's (10-14 deg) LOW EDGE, not inside it (9.7 sits
  below the floor) [REV-NRS-3]. FILM-COOLING CAVEAT (rides the cell
  note) [REV-NRS-3]: every P-B V_cir value is measured on FILM-COOLED
  configs (Fig. 24 = the cooling matrix); no uncooled-baseline exit
  V_cir exists anywhere in P-B, and the cooling system itself MODULATES
  the swirl — the datum remains a valid magnitude-class existence datum
  [ADV], scoped "film-cooled configs, cooling-modulated, no clean
  baseline". P-C RMSD_theta 8.16-14.63 deg = upper-proxy consistency
  only. DEFINITIONAL GUARD (mandatory, rides the cell note; STRONGER
  form [REV-NRS-2]): P-C eq. 20 (p. 8) = mass-weighted total-flow-angle
  RMS deviation from axial — upper-proxy reading defensible [VER-class];
  P-B prints NO RMSD formula anywhere in the paper (nomenclature p. 2:
  "flow deflection angle" only) — its meridional-vs-total status is
  UNDER-DETERMINED at held evidence. Operative rule, unconditional:
  RMSD_theta from EITHER paper is NEVER booked against B5 in ANY
  direction (neither as swirl value nor as certified upper bound); the
  only swirl datum is V_cir (see (e).4).
  Swirl-breaker family notes: P-B flat-jet suppression (F-24/F-25,
  actuated instance) + swirl-induced early trailing shock (F-11 tail),
  beside the registered Paxson-Miki candidate.
G-05 Forchetta (iv) BEST provenance: P-D F-6/F-22 (mean efflux = classic
  plume; the source claim) + P-A Figs. 9/12 (axisymmetric mean, no Mach
  disk in Case C) + A-L1 (exit Mach 2.58 vs 2.69: the ONE quantified
  external mean-design-point miss, ~4%) + P-C L16 (time-avg wall p obeys
  steady area law) + P-B F-11 (the steady design still selects a
  NEAR-OPTIMAL in-band truncation — coincidence of in-band argmax is
  at/below Fig. 15 resolution [REV-NRS-9]).
  WORST provenance: P-C ranking flip (L11) + P-B transient-only +0.52%
  invisible on the flat steady curve — the in-class delta scale
  (compare our +0.51%, advisory :828-832). Both cells [ADV].
  LANDING RIDER [REV-NRS-5]: P-B F-01 (time-averaged stagnation
  constraints "empirically recognized", citing P-D) = candidate
  cross-cite in M0 T-T3-MAP context at the landing — restores the P-B
  slot F-01 arc dropped undeclared in v1.
G-06 Forchetta (v) notes: P-A base ~0.16 atm bubble topology (Fig. 12b)
  + P-C base-zone transient-vs-steady deformation (L8) = base model-form
  UNPRICED stands; P-B Chutkey cold-rig base dataset (Figs. 4-5) =
  R8-adjacent context that does NOT retire the nozzleless->plug ANALOGY
  label (cold annular rig, not an RDE); P-B exit gamma 1.2500-1.2515 =
  weak frozen-gamma datum (one-step chemistry: does NOT test [T-EQBR]);
  P-D F-12/F-24 = the live instance of model-form bars dominating
  absolute values.
G-07 Forchetta (vi) provenance list: P-B Fig. 15 (flat-vs-peaked) =
  second empirical marker; P-C Fig. 13 (argmax holds, mid-ranking flips)
  = brush instance; P-A Fig. 15b drag tail + 4% miss = value-adequate
  yet visibly non-stationary design. All [ADV]; no number enters the
  delta/mu schema.
G-08 M-RED (Part 3) external-anchor note: P-B/P-C are the field's crude
  cousins of leg (A) (averaged-input vs unsteady, same code) landing at
  percent scale with BOTH signs (P-C) — leg-(A) expectation context,
  NEVER band inputs (uncertified, viscous/one-step, coarser averaging).
G-09 R22-CFD dossier (§4.1/§4.3): CT-1 evidence ladder verbatim (P-A
  reflected shocks / P-C +3.89% / P-D +50-60%); P-C paired-run mechanics
  = CFD-2 template; P-B shows the confrontation is readable at ~0.5%
  resolution; P-D = cautionary reference-config counter-candidate;
  P-A ~12M-cell cost instance confirms CFD-1 cost class.
G-10 Addendum (c) enrichment note (CT-3) [REV-NRS-1] -> forchetta table
  header note at the landing (record sentence itself unchanged — it is
  true as written); exact enrichment text in (e).6.
G-11 BLOCCATO 9 / ADR-D4 dossier rider (CT-4): definition mapping +
  P-A "truncation does not affect inner field" (Fig. 11 caption) +
  1.2% Isp truncation cost + P-B transient band. Single rider note.
G-12 Delta-carrier minor (c) context note: constriction/exit-area moves
  (P-A recommendation; P-D choked +50-60%; P-C area-law bookkeeping
  Fig. 8/9) live OUTSIDE the fixed-interface class — scope context for
  the lemma's delta semantics, no statement change.
G-13 Choking advisory (F5 row / L4 margin): A-L6 (M_t = 1.0 asserted for
  the throatless case) = the sharpest uncertified-choking instance;
  A-L5 corpus numbers (choked +4-7% Isp; Fotia 3-7%; Bach eps sweep).
G-14 Rao-baseline choice-ledger context row: P-B implements
  Vander-Veen-Gentry-Hoffman; P-C's approving citation (L12) must NOT
  upgrade the Veen constants (unreliability of record, registry :441
  via onofri_2002_plug_survey, stands).
G-15 Registry mechanics (landing, orchestrator): liu_2022 row gets PATH
  NOTE only (no new row, census-defect order) + prior-report errata note
  (P-A Δ8); THREE new READ-INTEGRAL rows minted for P-B/P-C/P-D
  (where_read = the three study files); prior P-A report filename-
  correction duty (F1) remains open. ERRATUM QUARANTINE (rides the P-B
  row mint) [REV-NRS-6]: P-B slot F-22 attributes min V_cir 327.5 m/s
  to hole type "(1.5/1.0, 150)"; the paper reads "corresponding to
  a/b = 1.0/1.5 and V_sec = 150 m/s" (p. 18) — the slot attribution is
  a transcription erratum; the registry-row note must carry the correct
  attribution so the wrong one never re-enters downstream (the
  synthesis itself carries only the range, which is correct).
G-16 Topology consolidation (section (d) below) -> the R22F in-flight
  loop as citable ADVISORY input (this file is the carrier).
G-17 P-B film-cooling body (F-16..F-21, F-23): out of program scope —
  archival in the slot file, declared non-orphan there; no further
  landing (this line closes it).
G-18 MISSED-CLUSTER WANTED list (section (f)) -> procurement queue.
ORPHAN CHECK [REV-NRS-5]: every consumption-arc row of the four slot
files maps to a G row or an in-file section ((a)/(e)); two landing
targets initially dropped WITHOUT declaration are RESTORED this
revision: (i) the P-B F-01 arc's "M0 T-T3-MAP cross-cite" target (now
the G-05 landing rider); (ii) the P-A/P-D arcs' FIELD_ATLAS_targeted_
c4.md candidate-row target (now the G-01 atlas rider). With these
restorations, no slot arc is unconsumed.

==============================================================================
## (d) TOPOLOGY CONSOLIDATION — citable ADVISORY input for the in-flight
##     R22F loop (revisers/refuters: cite as [ADV], with the page anchors)

D-1 THE DICHOTOMY, four times over: instantaneous fields are manifestly
  non-axisymmetric (rotating oblique shock, banded wall footprints);
  time-averaged fields are clean classical axisymmetric plumes. Anchors:
  P-A Fig. 7 vs Fig. 9 (pp. 7-8); P-B Fig. 14 right vs left (pp. 9-10);
  P-C Fig. 10 left vs right (pp. 9-10); P-D Fig. 9 vs Fig. 4 (pp. 3449,
  3447). This is the paper-borne face of [T-T0P]-steadified structure
  vs what K drops — the loop may cite it as the corpus-consistent
  phenomenology; it licenses NO magnitude.
D-2 K-PHENOMENON INSTANCES (advective-helix ray family, §2.3(a)):
  sweeping oblique wave descending the diverging section with azimuthal
  temperature banding (P-B Fig. 14, p. 9-10); one-sided internal shock
  whose ORIGINATION SWITCHES spike<->cowl with geometry (P-C L5, p. 8);
  helical/banded wall-temperature streaks (P-C Figs. 18-19, pp. 15-16;
  P-B Figs. 17-18 cold-film streaks bent toward the induced-shock side).
D-3 K-BAR = 0 PHENOMENOLOGY: P-C's rotating lateral force, ~25-35% of
  instantaneous axial thrust [INF], direction sweeping 0-360 deg per
  cycle (Fig. 21 sawtooth, pp. 16-17) — large per-phase azimuthal
  content, near-cancelling mean: the cleanest published face of the
  mean-nullity + (J)/(H) fluctuation-channel structure (§2.2(i)).
D-4 NOZZLE->CHAMBER FEEDBACK TOPOLOGY: reflected shock from constriction
  throat / cowl lip traveling back INTO the combustor (P-A Fig. 8d p. 8,
  Fig. 11 p. 9); upstream-running reflected shock through a subsonic
  chamber in the choked config (P-D Fig. 9 bottom, p. 3449; compression
  zone in Fig. 8, p. 3449). Azimuthally-structured wave families
  GENERATED BY THE NOZZLE — chamber-side, upstream of the interface:
  bears on CFD-1 coupling, NOT on the march (do not misfile as K terms).
D-5 BASE-ZONE TOPOLOGY: truncation bubble = enclosed subsonic
  recirculation (P-A Fig. 12b p. 9, base ~0.16 atm = 44% ambient p. 12);
  recirculation grows and turns irregular with truncation, extra
  trailing shocks at 80% (P-B Fig. 14a-d, p. 9-10); transient base zone
  DEFORMED vs the steady closed torus, direction depending on config
  (P-C L8, p. 11). Reinforces: base-pressure model-form UNPRICED on
  truncated plug (forchetta (v) WORST); R8 analogy label stands.
D-6 PERFORMANCE-FIGURE TOPOLOGY (the two figures the loop must see):
  P-B Fig. 15 (p. 10) — steady flat ~0.969 vs transient peaked (0.9456
  at 40%, ~0.89 at 80%): vertical offset = reduction gap, SHAPE
  difference = optimum-visibility statement; P-C Fig. 13 (p. 11) —
  transient-vs-steady C_fx bars with BOTH signs and one mid-ranking
  flip, argmax stable. Together: the (iv)/(vi) cells' empirical markers.
D-7 MEAN-FIELD QUALITY DATA: mean exit Mach 2.58 vs design 2.69 (P-A
  p. 7); no Mach disk on the well-designed contour, weak recompression
  only (P-A Fig. 12, Case C); streamlines leave PARALLEL after the lip
  turn (P-A Fig. 13); max average exit Mach 3.03 on the MoC profile
  (P-C L12, p. 11); Mach_ave peaks >3.2 under actuation (P-C L20).
D-8 EVIDENCE CEILING (binding on every citation above): P-D's verbatim
  self-grading "the absolute values are completely different" (p. 3451)
  + one-step/RANS stacks in P-B/P-C + P-A's unmatched-mdot comparison:
  ALL of D-1..D-7 is mechanism/topology evidence at [ADV]; no magnitude
  from these papers may enter a bound, band, or cell value.

==============================================================================
## (e) BEARING ON DECISIONS OF RECORD (the brief's explicit list)

(e).1 THE AVERAGING BET (T-DISC/R22) vs P-A's averaged-plume claim.
  The claim ("reasonable to use the time-averaged value... for nozzle
  design", P-A abstract; P-D F-22 is its cited origin) is CONFIRMING
  EVIDENCE at sizing level and carries its own counter-evidence at
  ranking level, in the same four papers: 14.2% unexplained shortfall
  attributed to time-slice non-uniformity (P-A p. 12), 4% mean
  design-point miss (A-L1), transient-only +0.52% invisible to the flat
  steady curve (P-B), mid-ranking flip (P-C). VERDICT: the bet of record
  ("adequate for sizing, unpriced at ranking" — R26 OPEN) is SHARPENED,
  not moved; centerpiece Part 1's conviction of the p-only projection
  and exoneration of the full-state average are untouched (none of the
  four papers poses the projection question; P-B's stagnation-parameter
  constraints are h0-bearing, consistent with §1.4(b)).

(e).2 TRUNCATION DEFAULT 0.20 (BLOCCATO 9) vs P-B's "40% optimum" —
  DEFINITIONS FIRST (brief order):
  - P-B's quantity: DL_spike/L_cowl = length REMOVED from the full MoC
    spike, normalized by the COWL diverging-section length (80 mm)
    [REP p. 10]. Their full spike ~ 1.0 L_cowl [INF, Fig. 14 tip
    positions] => optimum "40%" RETAINS ~60% of the spike; their 20%
    case retains ~80%; their worst 80% case (-5.78%) retains ~20%.
  - Our 0.20 (BLOCCATO 9, PROGRESS :240-249): the program's truncation
    default with printed band 0.20-0.40, execution gated ADR-D4. Under
    the classical plug-retention convention (the Chutkey rig P-B
    verifies against: "only retains 20% of the total length", P-B p. 4),
    0.20 = RETAIN 20% — i.e., nominally the neighborhood of P-B's WORST
    transient case ON THEIR CONFIGURATION.
  - RECONCILIATION VERDICT: the two numbers are NOT commensurable
    without the explicit mapping (removed-fraction-of-cowl vs
    retained-fraction-of-plug; different reference lengths, different
    ambient 6141 Pa vs our design point, different base-flow class);
    the apparent 0.20-vs-40% clash partly DISSOLVES (their optimum is
    mild truncation, not zero truncation) and partly points AGAINST the
    deep-truncation end at [ADV]+[INF] evidence. DECISION OF RECORD
    STANDS (default 0.20, band 0.20-0.40); DUTY: the definition-mapping
    note + P-B band evidence MUST ride the ADR-D4 dossier (CT-4/G-11)
    so the gated re-evaluation confronts it explicitly. P-A adds: 1.2%
    Isp cost at their truncation + "truncation does not affect inner
    field" (decoupling datum, Fig. 11 caption).

(e).3 FIXED-EXIT-AREA / DELTA-CARRIER LEMMA vs P-A convergence
  recommendation + P-D choked +50-60%. The lemma (minor (c); delta =
  distance to the L-unconstrained fixed-eps ceiling) is a statement
  INSIDE the fixed-interface data class; P-A's constriction
  recommendation and P-D's choking lever are CLASS-CHANGING moves (they
  rewrite the chamber state, CT-1). No confrontation exists at theorem
  level; the papers supply the honest scope sentence: the largest
  published performance lever lives outside the class the lemma prices,
  and pricing it is exactly CFD-1's irreducible core (centerpiece §4.1).
  Landing: scope-context note on the minor (c) draft + CT-1 evidence
  ladder into the §4.3 scheduling dossier.

(e).4 FORCHETTA CHANNEL (iii) SWIRL VALUES vs "P-B 14.42 deg RMS +
  P-C RMSD 9-11 deg" — DEFINITIONS FIRST [REV-NRS-2]: P-C's RMSD_theta
  (eq. 20, p. 8) is the mass-weighted RMS deviation of the EXIT FLOW
  ANGLE FROM AXIAL — for P-C it conflates meridional divergence with
  azimuthal swirl and is an UPPER PROXY, not a swirl angle. P-B prints
  NO RMSD formula anywhere in the paper (nomenclature p. 2 gives only
  "theta — flow deflection angle"), so P-B's meridional-vs-total status
  is UNDER-DETERMINED at held evidence (same-group eq.-20-type form is
  plausible [INF], not evidence). Operative rule, unconditional and
  STRONGER than v1: RMSD_theta from EITHER paper is NEVER booked
  against B5 in ANY direction (neither as swirl value nor as certified
  upper bound). The brief's own P-B abstract line ("RMS flow deflection
  angle 14.42 deg") must NOT be consumed as channel-(iii) swirl. The
  genuine swirl datum is P-B's exit V_cir = 327.5-383.4 m/s on V_x
  ~1910 m/s (Fig. 24d) => eps_theta ~0.17-0.20 and swirl angle
  ~9.7-11.4 deg [INF] — SCOPED [REV-NRS-3]: measured on FILM-COOLED
  configs ONLY (Fig. 24 = the cooling matrix; no uncooled baseline
  exists in P-B; the cooling system itself modulates the swirl) — a
  magnitude-class existence datum [ADV]; eps_theta INSIDE the DISPATCH
  §9 sweep band (0.15-0.20); swirl angle OVERLAPPING the LOW EDGE of
  the B5 band (10-14 deg), NOT inside it (9.7 sits below the floor).
  VERDICT: channel (iii) cell values STAND and gain their first
  non-corpus external consistency datum [ADV], film-cooled-scoped;
  the definitional guard (G-04) rides the cell note. Bonus mechanism
  rows: swirl-induced early trailing shock (P-B F-11) and actuated
  swirl suppression by flat jets (P-B F-24/F-25) join the swirl-breaker
  candidate family. P-D contributes nothing (absence declared).

(e).5 CHANNEL (v) MODEL-FORM vs the papers' loss decompositions.
  P-B's three-part transient decomposition maps cleanly onto the record
  structure: sweeping shocks -> channel (ii); viscous passage ->
  boundary-priced (outside the inviscid class, §2.3(c)); base
  recirculation -> channel (v) base row. P-A offers NO decomposition
  (14.2% bundled); P-C attributes without separating; P-D's admission
  (F-24) caps everything at [ADV]. VERDICT: the channel-(v) bars cannot
  be tightened by any of the four papers; the R8 nozzleless->plug
  ANALOGY label STANDS (P-B's Chutkey and P-C's Verma validations are
  cold rigs — R8 still lacks the truncated-plug RDE base MEASUREMENT;
  centerpiece R-8 residue unchanged, procurement class).

(e).6 NO-EXTERNAL-REFEREE FACT (addendum (c)) — HONESTLY RE-TESTED
  against the four papers' unsteady-c_F content:
  - P-A: NO unsteady c_F; C_F/delta built from time-averaged thrust +
    state-averaged reconstructed P_c (Eqs. (14), (20)-(23)); no
    per-phase or 2D companion anywhere. Fact STANDS.
  - P-B: unsteady c_F PRESENT (transient C_fx per truncation, Fig. 15)
    WITH a steady averaged-input companion — fails the discriminator on
    both qualifiers: companion is GLOBALLY averaged (not per-phase) and
    truth is same-family URANS (not external/experimental).
  - P-C: unsteady c_F PRESENT (time-resolved Fig. 20b; paired bars
    Fig. 13) — fails for the same two reasons.
  - P-D: NO unsteady c_F (cycle-averaged only, Eq. (4)). Fact STANDS.
  CONSOLIDATED VERDICT [REV-NRS-1]: the addendum-(c) sentence of record
  is STRICTLY TRUE as written — its restrictive clause ("...THAT
  DISCRIMINATES the 2D-per-phase-averaged prediction against
  3D-unsteady truth") is part of the sentence, no freestanding "the
  literature carries NO unsteady c_F datum" phrasing exists anywhere in
  the record, and the P-B/P-C pairs discriminate only a GLOBALLY
  averaged steady companion at same-solver URANS. The sentence needs no
  defensive rewrite; CT-3 fires as ENRICHMENT-AMENDMENT (narrative
  completeness of the nearest-referee inventory). ENRICHMENT TEXT
  (delivery-check landing): the forchetta header note gains the
  inventory line — nearest existing referees = P-B Fig. 15 /
  P-C Figs. 13+20b (same-solver URANS pairs at GLOBAL averaging —
  named, disqualified for the two stated reasons: companion not
  per-phase-averaged; truth not external/experimental). The bracket
  still CLOSES only via our own R22-CFD or dedicated procurement —
  that consequence is unchanged.

==============================================================================
## (f) MISSED-CLUSTER WANTED CANDIDATE LIST (consolidated, deduped)

Dedup basis (SR-12): grep of docs/literature_registry.yaml executed this
window (command in header) + row reads. ALREADY OF RECORD (NO new row):
stechmann_2019 (:317 — dedups P-B CORE#2), vander_veen_1974 (:427),
zucrow_hoffman_1977_vol2 (:467), kaemming_paxson_2018 (:236),
harroun_2021 (:273), harroun_2020 (:632), miki_2020 (:641),
paxson_miki_2022 (:249), ornano_2017 (:623 — NOTE: distinct from Braun
2017 JPP, same group), liu_2022 (:614 = P-A, path note only),
browne_shepherd_sdtoolbox_2018 (:299). CAMPAIGN-INTERNAL (rows minted at
landing): P-B, P-C, P-D. The brief's three named expectations all
RESOLVED: "Ma hot-fire" = P-C[12]; "Goto vacuum aerospike" = P-C[15] =
P-A[27] = P-B[26]; "Zhou conical" = P-C[13] (absence in P-A/P-B/P-D
lists search-proven by the slots).

TIER 1 (procure first — brief-named or multi-paper-cited or lineage):
W-01 Fotia, Schauer, Kaemming, Hoke 2016, "Experimental study of the
  performance of a rotating detonation engine with nozzle", JPP 32(3):
  674-681. [cited by ALL FOUR: P-A[30], P-B[21], P-C[14], P-D[23]
  garbled; the 3-7%-stagnation-pressure-at-eps-80% experiment]
W-02 Goto, Nishimura, Kawasaki, Matsuoka, Kasahara, Matsuo, Funaki,
  Nakata, Uchiumi, Higashino 2019, "Propulsive performance and heating
  environment of RDE with various nozzles", JPP 35(1):213-223.
  [P-A[27], P-B[26], P-C[15]; vacuum-chamber aerospike]
W-03 J.Z. Ma, Bao, Wang 2023, "Experimental research of the performance
  and pressure gain in continuous detonation engines with aerospike
  nozzles", AST 140:108464. [P-C[12]; the Ma hot-fire]
W-04 Zhu, Wang, Wang, Zhao, Jiao, Wang, Fan 2020, "Study on the
  performance of a rotating detonation chamber with different aerospike
  nozzles", AST 107:106338. [P-A[39], P-B[20], P-C[17]; EARLIEST
  average-then-design precedent per P-A p. 2]
W-05 R. Li, J. Xu, S. Huang 2022, "Nozzle design method for rotating
  detonation engine", JPP 38(5):849-865. [P-B[34], P-C[22]; the
  design-method PARENT of P-B/P-C — highest method-lineage bearing]
W-06 S. Zhou, Ma, Liu, Hu 2023, "Experimental investigation on pulse
  operation characteristics of rotating detonation rocket engine",
  Fuel 354:129408. [P-C[13]; the Zhou conical item]
W-07 Fotia, Kaemming, Codoni, Hoke, Schauer 2019, "Experimental thrust
  sensitivity of an RDE to various aerospike plug-nozzle
  configurations", AIAA SciTech 2019. [P-A[25]]
W-08 Chutkey, Vasudevan, Balakrishnan 2014, "Analysis of annular plug
  nozzle flowfield", JSR 51(2):478-490. [P-B[37]; truncated-plug base-
  pressure dataset — R8-ADJACENT (cold), candidate CFD-2-style reuse]

TIER 2 (design/efflux CORE, single- or double-cited):
W-09 Fievisohn, Hoke, Schauer 2018, "Quasi-2D simulations of nozzled
  RDEs with the method of characteristics", AIAA 2018-0881. [P-B[24];
  closest published cousin of our reduced-MoC class — elevated bearing]
W-10 Huang, Xia, Chen, Luan, You 2021, AST 117:106969 (aerospike shock
  dynamics + RDC interaction). [P-B[25], P-C[23]]
W-11 J. Braun, Saracoglu, Paniagua 2017, "Unsteady performance of RDEs
  with different exhaust nozzles", JPP 33(1):121-130. [P-B[18], P-C[20]]
W-12 Schwer, Kelso, Brophy 2018, "Pressure characteristics of an
  aerospike nozzle in an RDE", AIAA 2018-4968. [P-B[19]]
W-13 Bach, Stathopoulos, Paschereit, Bohon 2020, Combust. Flame 217:
  21-36 (stagnation-pressure PG, eps 100->50%). [P-A[56]]
W-14 Betelin, Nikitin, Mikhalchenko 2020, Acta Astronaut. 176:628-646
  (center-body length study). [P-A[29]]
W-15 Kurita, Jourdaine, Tsuboi, Ozawa, Hayashi, Kojima 2020, AIAA
  2020-0688 (P-D's own geometry follow-on). [P-A[34]]
W-16 Verma 2009, JPP 25(3):783-791 (annular conical aerospike,
  freestream). [P-A[58], P-C[44]; P-C's validation experiment]
W-17 He, Qin, Liu 2015, Chin. J. Aeronaut. 28(4):983-1002 (overexpanded
  aerospike separation). [P-C[43]]
W-18 Angelino 1964, "Approximate method for plug nozzle design", AIAA J
  2(10):1834-1835. [P-A[35], P-B[38]; THE design-method source; caveat
  of record rides onofri row :441 but NO dedicated row exists]
W-19 Hagemann, Immich, Nguyen, Dumnov 1998, "Advanced rocket nozzles",
  JPP 14(5):620-634. [P-A[36]]
W-20 Tsuboi, Eto, Hayashi, Kojima 2017, JPP 33(1):100-111 (wave-number
  effect, -10% Isp at 2 waves — CT-5's conflict partner). [P-D[27]]
W-21 Sun, Zhou, Liu, Lin, Lin 2018, "Plume flowfield and propulsive
  performance analysis of an RDE", AST 81:383-393. [P-B[23]]
W-22 Zhu, Wang, Zhao, Wang, Fan 2022, Acta Astronaut. 200:388-399
  (outlet configs vs wave propagation). [P-C[18]]
W-23 Zhao, Wang, Zhu et al. 2022, Acta Astronaut. 193:35-43 (exit
  convergent ratio, liquid kerosene). [P-C[19]]
W-24 C. Sun, Zheng, Zhao, Li, Zhu 2021, IJHE 46:18644-18660 (outlet
  nozzles + outlet load). [P-C[21]]
W-25 Rankin, [Hoke, Schauer — garble flag], AIAA 2014-1015 (CD-nozzle
  RDE experiment). [P-D[21]; verify identities at procurement]
W-26 Ruf, McConaughey 1997, AIAA 97-3218 (aerospike altitude
  compensation plume physics). [P-A[57]]
W-27 Tsuboi, Watanabe, Kojima, Hayashi 2015, PCI 35:2005-2013 (P-D's
  direct predecessor). [P-D[20]]
W-28 Shao, Liu, Wang 2010, CST 182(11-12):1586-1597 + Shao, Meng, Wang
  2010, CJA 23:647-652 (earliest nozzle-effect CFD pair — two DISTINCT
  entries). [P-D[14]; P-B[17]]
W-29 Yi, Lou, Turangan, Choi, Wolanski 2011, JPP 27(1):171-181 (+ the
  2010 AIAA precursor). [P-B[33], P-D[10]/[22]]
W-30 Kaemming, Fotia, Hoke, Schauer 2017, "Thermodynamic modeling of an
  RDE through a reduced-order approach", JPP 33(5):1170-1178. [P-B[15]]

TIER 3 (context/marginal — register as WANTED only if the cluster map
wants completeness; identities in the slot files): Braun-Lu-Wilson-
Camberos 2013 (P-B[13]=P-D[6]); Davidenko 2011 (P-B[16]); Deng-Ma-Liu-
Zhou 2019 (P-B[42]); Sun injector-width pair 2017/2019 (P-B[46]/[35-Sun]
= P-C[42]); Tang-Wang-Shao 2015 hollow RDC (P-C[47], injection-BC model
source); Yokoo et al. 2020 (P-A[55]); Frolov et al. 2018 (P-A[51]);
Stechmann PhD thesis 2017 (P-A[50] — DISTINCT from stechmann_2019);
Zhou-Wang 2012 particle paths (P-D[15]); DeBarmore et al. 2013 vanes
(P-D[7]); Zhdan-Bykovskii-Vedernikov 2007 (P-D[4]=[8]); Adamson-Olson
1967 (P-D[3]); Li-Yao-Fan 2016 LES jets (P-A[54]); He-2015-adjacent
cooling SEC cluster P-B[27]-[32]; Huang-Lin 2023 ramjet (P-C[26]);
S. Yao, J. Wang 2016, "Multiple ignitions and the stability of
rotating detonation waves", Appl. Therm. Eng. 108:927-936 (P-B[47],
wave stability); F.K. Lu, E.M. Braun 2014, JPP 30(5):1125-1142
(P-B[12], CTX-grade review, kept for the cluster map) — these last two
RESTORED from the P-B slot §8 extraction (silently dropped in v1;
registry grep re-executed this revision window: neither is
registry-held) [REV-NRS-4].

COUNT: 30 tiered WANTED candidates (8 Tier-1, 22 Tier-2) + 17 Tier-3
context items (15 + 2 restored [REV-NRS-4]); 11 registry-held
identities deduped out; 3 campaign-
internal. Procurement order proposal: W-01..W-08 first (brief-named
cluster + all-four-cited + lineage parents), then W-09 (method cousin).

## PAPERS NEEDED (this deliverable)
None blocking. The list above IS the procurement output.

==============================================================================
## (g) MACHINE SUMMARY

campaign: BRIEF_nozzle_rde_arrivals_study.md slot 5 (synthesis)
inputs: 4/4 study files [FULL] + confrontation frame (2 briefs + centerpiece 696 lines + BLOCCATO 9) + registry grep (dedup, SR-12)
matrix: (a) 7 axes x 4 papers [REV-NRS-7] + 5 commonalities C-1..C-5 + named seams (C_f definitions; RMSD_theta definition)
threat_ledger: 8 consolidated (CT-1..CT-8) from 16 slot threats; 0 BREAK; 1 FIRES-as-ENRICHMENT-AMENDMENT (CT-3 narrative completeness — record sentence true as written; enrichment text at (e).6) [REV-NRS-1]; 1 rider duty (CT-4 -> ADR-D4 definition mapping); 6 do-not-fire (CT-1/CT-2 strengthen priced threats; deciders named: CFD-1, M-RED, T0-flatness/A32); 0 THEOREM/THEOREM* rows contradicted
graft_list: 18 landings (G-01..G-18), consolidated from 4 slot consumption-arc tables, deduped; orphan-check PASS after [REV-NRS-5] restorations (M0 T-T3-MAP cross-cite rider on G-05; FIELD_ATLAS rider on G-01)
topology_consolidation: D-1..D-8 (citable ADVISORY input for the R22F loop; D-8 = evidence ceiling binding every citation)
decisions_of_record: 6 bearings delivered ((e).1-(e).6): averaging bet SHARPENED not moved (R26 stays open); truncation 0.20 STANDS with mandatory ADR-D4 mapping rider (P-B optimum retains ~60% of spike [INF] — not commensurable with 0.20 without mapping); delta-carrier lemma untouched (choking = class-changing move, CFD-1's case strengthened); channel (iii) values STAND + first external swirl datum (P-B V_cir, FILM-COOLED configs only, cooling-modulated => swirl angle ~9.7-11.4 deg OVERLAPPING B5's low edge, eps_theta 0.17-0.20 inside DISPATCH band [INF]) [REV-NRS-3] + RMSD_theta definitional guard in STRONGER form (P-B formula unprinted; never booked against B5 in any direction) [REV-NRS-2]; channel (v) bars unchanged, R8 analogy stands; no-external-referee fact SURVIVES — record sentence TRUE as written, CT-3 = enrichment note at landing naming P-B/P-C nearest referees + disqualifiers (unsteady c_F PRESENT in P-B/P-C at CFD class, ABSENT in P-A/P-D) [REV-NRS-1]
missed_cluster: 30 WANTED candidates (8 Tier-1 + 22 Tier-2) + 17 Tier-3 (2 restored [REV-NRS-4]); 11 registry dedups; brief's 3 named items all resolved (Ma=P-C[12], Goto=P-C[15], Zhou=P-C[13])
output_file: validation/sfoundations_raws_2026-08-13/blocco3/SYNTHESIS_nozzle_rde_arrivals.md

==============================================================================
## (h) REVISION DISPOSITION TABLE [REV-NRS] (appended 2026-08-20,
##     convergence close; orchestrator adjudication: ALL refuter
##     findings SUSTAINED; source = REFUTE_nozzle_rde_synthesis.md)

| Finding | Class | Disposition applied in this file | Sites |
|---|---|---|---|
| NRS-1 | REPAIR | CT-3 re-grounded: the addendum-(c) record sentence is TRUE as written (restrictive clause is part of it); "FALSE-READING" / else-read-as-false framing STRUCK; CT-3 regraded FIRES-AS-ENRICHMENT-AMENDMENT (narrative completeness — nearest-referee pairs P-B Fig. 15 / P-C Figs. 13+20b named with their two disqualifiers); (e).6 landing text kept AS the enrichment; record sentence needs no rewrite | (b) CT-3, TALLY, G-10, (e).6, machine summary |
| NRS-2 | REPAIR | RMSD_theta guard harmonized to ONE consistent statement: P-C eq. 20 (p. 8) = total-flow-angle RMS deviation from axial, upper-proxy defensible; P-B prints NO RMSD formula (wrong "eq. 30-class" anchor removed; "MERIDIONAL ... NOT swirl" over-assertion removed) — definition UNDER-DETERMINED; guard lands in its STRONGER unconditional form: RMSD_theta from either paper NEVER booked against B5 in ANY direction | (a) P-B cell, G-04, (e).4, machine summary |
| NRS-3 | AMENDMENT | P-B V_cir 327.5-383.4 datum scoped FILM-COOLED-CONFIGS-ONLY (cooling-modulated, no uncooled baseline exists); swirl angle 9.7-11.4 deg restated as OVERLAPPING B5's low edge (9.7 below the 10-14 floor), not inside; eps_theta 0.17-0.20 remains inside DISPATCH §9 band | (a) P-B cell, G-04, (e).4, machine summary |
| NRS-4 | AMENDMENT | Two silently-dropped P-B WANTED entries RESTORED to Tier-3: [47] Yao-Wang 2016 (ATE 108:927-936) + [12] Lu-Braun 2014 (JPP 30(5):1125-1142); dedup re-checked by registry grep this revision window (neither held; only distinct Ornano-Braun 2017 row matches "braun"); Tier-3 count 15 -> 17 | (f) Tier-3, COUNT, machine summary |
| NRS-5 | AMENDMENT | Orphan-check repaired by RESTORING both dropped targets: M0 T-T3-MAP cross-cite arc (P-B F-01) = landing rider on G-05; FIELD_ATLAS_targeted_c4.md candidate rows (P-A figures + P-D Fig. 9) = atlas rider on G-01; ORPHAN CHECK sentence rewritten to name the restorations | G-01, G-05, ORPHAN CHECK, machine summary |
| NRS-6 | NOTE | Min-V_cir slot erratum (F-22 hole-type "(1.5/1.0, 150)" vs paper's a/b = 1.0/1.5, V_sec = 150 m/s, p. 18) QUARANTINED: correction note attached to the G-15 P-B registry-row mint; synthesis body needed no numeric change (carries only the correct range) | G-15 |
| NRS-7 | NOTE | Machine-summary axis count corrected: "8 axes" -> 7 (matches the printed matrix and the brief's seven-item list) | machine summary |
| NRS-8 | NOTE | CT-5 last sentence re-scoped: "counter-datum FOR the pin" dropped; P-C Figs. 15/16 = realization instance at CFD class only (CFD-realizability of the pure-periodic class, not hardware realism), aligned with G-02's phrasing | (b) CT-5 |
| NRS-9 | NOTE | G-05 P-B F-11 line softened: "uniform offset preserves in-band ranking" -> "steady design still selects a NEAR-OPTIMAL in-band truncation" (in-band argmax coincidence at/below Fig. 15 resolution) | G-05 |

Deviations from the ordered repairs: NONE. All nine findings applied;
no other content touched. Revision markers [REV-NRS-1..9] tag every
edited passage in place; this table is append-only.
