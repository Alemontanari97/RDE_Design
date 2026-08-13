# INVENTORY — seg8-supplement (S-ORDINE Phase 1, S0b reader, 2026-08-13)

Reader: S0b supplementary-inventory. Segment = the 64 NEW files found by the fresh
S0 list (a parallel session landed them after Phase-1 seg1-seg7 closed). Schema
identical to Phase-1 (seg3/seg4 advisory schema; seg7 literature schema):
PATH | CLASS | ROLE | STATUS-AUTHORITY proposed | PLAN-ANCHOR | UNIQUE-AT-RISK
CONTENT | REFS in/out.

METHOD (declared). Read INTEGRALLY: the 7 new validation .md except the SORDINE
plan and the live session log (structure-only, this session owns them) —
`ADVISORY_litmap_extension_2026-08-13.md` (full), `ADVISORY_litreview_confrontation_
2026-08-13.md` (full, 1289 lines, read across 6 passes), `ADVISORY_moc_zucrow_
fidelity_2026-08-13.md` (full, 649 lines, 2 passes), `ADVISORY_sota_definition_
2026-08-13.md` (opening + SECTION 0 + DEFINITIONS + SOTA-1..9 in full detail +
SECTION 4 provenance + closing "Come si usa" + "Residui aperti" — SOTA-10..18 and
SEZIONE 2/3 antipattern/scarti tables read only via header/grep, **not** verbatim;
declared partial-integral, see file entry below), `ASSESSMENT_methodology_position_
2026-08-13.md` (full), `LEDGER_dubbi_moc_2026-08-13.md` (full),
`RAW_geno_audit_instrumentation_2026-08-13.patch` (full, it is a small diff).
Read INTEGRALLY in `literature_review/`: `INDEX.md`, `reports/00_APPARATUS_BRIEF.md`,
`reports/VERIFICATION_FABLE_2026-08-13.md`, and 3 declared sample per-paper reports
— `kraiko_tillyaeva_2015_conjugate.md` (highest-stakes paper for claim 1/P2-G14),
`harroun_2021_jpp_nozzle_perf.md` (tranche-2 anchor, RDE physics threat), and
`giles_pierce_2001_quasi1d.md` (core modern-adjoint reference) — chosen because the
confrontation advisory itself names these as the ones the fused judge personally
re-read against the PDFs (§0 of that advisory). The other 22 per-paper reports are
classified from INDEX.md rows + the confrontation advisory's paper-by-paper table
(§2) + report headers/citation blocks (declared reason: homogeneous per-paper
reading-report schema — Citation / Read coverage / What the paper does / Hypotheses
/ 3-level Findings / Bibliography — content anchors are root-D "where-read" +
table row, already summarized at need-level by the confrontation advisory which
this reader verified in full). PDFs: classify-without-read (identity from filename
+ INDEX.md row + confrontation-advisory table row).

---

## PART A — root literature/ (1 file)

### A1. `literature/aerospace-10-00797.pdf`
- CLASS: literature-pdf.
- ROLE: Ancourt, Peter & Atinault, "Adjoint and Direct Characteristic Equations for
  2-D Compressible Euler Flows", *Aerospace* **10**(9):797 (2023),
  doi:10.3390/aerospace10090797 — the peer-reviewed published version (identity per
  `ADVISORY_litreview_confrontation_2026-08-13.md` C3: "Aerospace 2023, 10, 797").
- STATUS-AUTHORITY proposed: **DUPLICATE-OF-RECORD** (not ORPHAN, not new content).
  **md5/content DUPLICATE of `literature_review/ancourt_2023_adjoint_direct_
  characteristic_equations.pdf`.** Direct corroborating evidence: `literature_
  review/lint_index_consistency.py:40` records that a sibling copy
  `"aerospace-10-00797 (1).pdf"` was found **md5-identical to ancourt_2023** and
  removed from `literature_review/` on 2026-08-13 as a duplicate. The file at this
  path (no `(1)` suffix, landed in repo-root `literature/`, NOT in
  `literature_review/`) is therefore extremely likely the **same PDF landed a
  second time in a second location** — a cross-root duplicate that seg7's Phase-1
  dedup summary (which found "no paper PDF duplicated across the three roots") did
  not and could not see, because this file did not exist yet.
- PLAN-ANCHOR: literature acquisition register (T2 `docs/literature_registry.yaml`
  deliverable); Ancourt is already a full-text-verified acquisition (litreview
  report `ancourt_2023_char_adjoint.md`, confrontation-advisory row #4: CONT+ADO+
  MIN+COR touching claims 1, 7, 8, O3.5, X-GENOXC). No independent plan need beyond
  "second copy of an already-acquired, already-analysed paper".
- UNIQUE-AT-RISK CONTENT: **none** — if genuinely a duplicate, the content is fully
  covered by `literature_review/ancourt_2023_adjoint_direct_characteristic_
  equations.pdf` + its report + advisory rows. **Residual risk to flag loudly**: the
  identity was inferred from filename + the lint script's note about a *different*
  file (`"(1)"` suffix), not verified by this reader with a direct md5 comparison of
  THIS specific file — T2 should run one `md5sum` before archiving/merging this row
  as CONSUMED-DUPLICATE.
- REFS: in — none (loose file, root A of seg7's literature partition, added after
  Phase-1 closed). out — corroborated by `literature_review/lint_index_
  consistency.py` (EXEMPT_ABSENT dict, line 40) and `literature_review/INDEX.md`
  line 89 (arXiv preprint superseded note, C3 in the confrontation advisory).

---

## PART B — `literature_review/` (54 files)

Deck of record: this is a NEW top-level directory (sibling of `literature/`), the
deliverable of the "litreview-confrontation" workflow (`wf_ab852ac5-8e6`) tasked
with sweeping 1971→2026 per `ADVISORY_litmap_extension_2026-08-13.md`. All content
here is downstream of, and explicitly dated 2026-08-13, i.e. it POST-DATES every
Phase-1 inventory segment (seg1-seg7) and is not covered anywhere in them.

### B1. `literature_review/INDEX.md`
- CLASS: doc-index / procurement register. **READ INTEGRALLY.**
- ROLE: acquisition ledger for the 25 downloaded PDFs (ACQUISITI list, exact
  on-disk slugs), TIER-1/2/3 procurement classification for everything NOT yet
  acquired (ISABE-2003-117, Bogdanov 2002, Kraiko-Tillyaeva 2015 reference list —
  the last is now moot, it WAS acquired), and duty D-14 (extended, three-channel
  filename↔disk lint spec, later implemented as B2).
- STATUS-AUTHORITY proposed: **OF-RECORD, WITH KNOWN ERRATA** — the confrontation
  advisory's §6 correction table (C3, C4, C5, C9, C21) documents concrete errors IN
  THIS FILE (wrong ref-count for Ancourt "47" vs true 45; wrong filename for
  Ancourt; false "only formal optimizer" tag on Liu 2022; 5 filename↔disk
  disallignments; several un-timbrato venues asserted as fact). None yet repaired
  in the file itself (duties D-13/D-14 in the confrontation advisory, unexecuted at
  this reader's pass).
- PLAN-ANCHOR: T2 `docs/literature_registry.yaml` deliverable (direct feeder,
  parallel to seg7's role for the older 137-file literature universe); census R32
  (S-ORDINE) / R31 (findings-as-code corpus seeding, F2 first duty).
  literature-map duties D-A..D-F (litmap_extension) route through here.
- UNIQUE-AT-RISK CONTENT: the exact on-disk ACQUISITI slug list (25 names, no
  extension) is the ONLY authoritative filename↔identity map for this folder; the
  TIER-1 procurement list (ISABE-2003-117 route options: ISABE/AIAA proceedings
  order, interlibrary loan, direct CIAM request; Bogdanov 2002 via eLibrary.ru with
  the exact Russian search string) lives only here.
- REFS: in — `ADVISORY_litmap_extension_2026-08-13.md` (source of the acquisition
  drive); out — `ADVISORY_litreview_confrontation_2026-08-13.md` §6 (corrections
  filed against this file, unexecuted), `lint_index_consistency.py` (the executable
  check of this file's internal consistency).

### B2. `literature_review/lint_index_consistency.py`
- CLASS: code (test/lint script, ~176 lines). Classified-without-full-read (code
  file; docstring + head 40 lines read, sufficient to establish role and to
  discover the aerospace-10-00797 duplicate corroboration used in Part A).
- ROLE: implements duty D-14-extended — three independent channels checking
  `INDEX.md` against the disk: (i) every filename cited in INDEX.md exists on disk,
  (ii) every PDF on disk appears in the ACQUISITI list, (iii)
  `count(*.pdf) == len(ACQUISITI) == declared number` (the channel that was MISSING
  when a 5-PDF delivery landed silently on 2026-08-13 06:10 and the declared count
  stayed at 20 against a real disk count of 25 — the motivating incident, named
  in-file). `--selftest` runs three seeded rejectors (R5 discipline: numbers that
  can't fail are not trustworthy).
- STATUS-AUTHORITY proposed: **OF-RECORD** (executable channel guard; standing per
  R5 "test must be able to reject").
- PLAN-ANCHOR: R5 (numbers discipline); R28 numeric-lint / validation-ratchet
  family (same lint-hygiene lineage as S25-bis's `tests/test_numeric_lint.py`), but
  scoped to `literature_review/` not `validation/`.
- UNIQUE-AT-RISK CONTENT: the `EXEMPT_ABSENT` dict (filenames cited in INDEX.md
  that are legitimately absent from disk, each with a reason) is the durable record
  of the two dedup events already resolved inside `literature_review/` (the
  `aerospace-10-00797 (1).pdf` md5-duplicate-of-ancourt removal, and the
  `s12567-023-00511-1 (2).pdf` duplicate removal, and the arXiv-preprint→
  published-version swap for Ancourt) — this is the ONLY place those three
  resolutions are machine-checkable, and it is the evidence this reader used to
  flag A1 above.
- REFS: in — `INDEX.md` (the file it lints); out — none observed (not yet wired
  into any CI/test-suite `run_all` group at S-ORDINE time, unlike the `validation/`
  numeric-lint family — a plausible T2 wiring gap, flag loudly).

### B3-B27. `literature_review/*.pdf` — 25 primary-source PDFs (all class
**literature-pdf**, classify-without-read per PDF rule; identities and
tranche-1/tranche-2 status from `INDEX.md`; content/verdict summary from the
confrontation-advisory paper-by-paper table §2). STATUS-AUTHORITY proposed for
all 25: **OF-RECORD** (primary sources; the ANALYSES of record live in the paired
report B28-B52 below + the confrontation advisory — none of these PDFs is
superseded/consumed as an object, though several individual TABLE VERDICTS on
them were corrected mid-review, see §6 of the confrontation advisory).
PLAN-ANCHOR for all 25: census R32/S-ORDINE literature-seeding duty; the D6
generality-litmap program; specific claim-rows named per-file below (from the
confrontation advisory's "Claim toccato" column). UNIQUE-AT-RISK for all 25: none
in the PDF itself (findings live in the paired report + advisory); risk is
entirely in the REPORT/ADVISORY layer, tracked under B28-B78 below.

| # | PATH | Identity (author, venue, year) | Claims touched (confrontation-advisory §2) | Cross-root dedup |
|---|---|---|---|---|
| B3 | `ancourt_2023_adjoint_direct_characteristic_equations.pdf` | Ancourt, Peter & Atinault, *Aerospace* 10(9):797 (2023) | 1, 7, 8, O3.5, X-GENOXC | **DUPLICATE of `literature/aerospace-10-00797.pdf` (Part A, A1)** |
| B4 | `fernandes_2023_moc_shape_optimization_rocket_nozzles.pdf` | Fernandes, Souza & Afonso, *CEAS Space J.* 15:867-879 (2023) | 8 (niche), 16, 7, 13, H-CLASS | none |
| B5 | `giles_pierce_2000_intro_adjoint_design.pdf` | Giles & Pierce, *Flow Turb. Combust.* 65:393-415 (2000) | 1, 13, 6, 7, VI.3 pin, globality (iv) | none |
| B6 | `giles_pierce_2001_analytic_adjoint_quasi1d_euler.pdf` | Giles & Pierce, *JFM* 426:327-345 (2001) | 13 (O3.1), F4b, DWR bars, 1, 8 | none — **sample-read, see B29** |
| B7 | `harroun_2020_rde_nozzle_simulation_validation.pdf` | Harroun, Heister & Ruf (2020, un-timbrato) | 2 (H2'), 4, 5, 6, g_sep, CSTR_PB, D2.3 | none |
| B8 | `harroun_2021_computational_experimental_rdre_nozzle_performance.pdf` | Harroun, Heister & Ruf, *JPP* 37(5):660-673 (2021) | 2 (H2'), 4, 5, 6, 7, 8, 13, g_sep, CSTR_PB, D2.3, VI.1 | **DUPLICATE of `PARENT/computational-and-experimental-study-of-nozzle-performance-for-rotating-detonation-rocket-engines (2).pdf`** (seg7 B7) — **sample-read, see B30** |
| B9 | `hoffman_1987_compressed_truncated_perfect.pdf` | Hoffman, *JPP* 3(2):150-156 (1987) | 19 (F7), 2, 5, 8, REQ-NONSTALL, G2 | none |
| B10 | `janc_2025_differentiable_reacting_solver_adjoint.pdf` | Wen, Luo, Xu & Wang (JANC, 2025, un-timbrato), arXiv:2504.13750 | 8, 1, 13, VI.4 vmap, speed ledger | none |
| B11 | `kaemming_paxson_2018_equivalent_available_pressure.pdf` | Kaemming & Paxson (EAP; M0 cites as AIAA 2018-4567; venue un-timbrato in the PDF metadata) | 15 (T-GB), 2, 4, 7, 8, 16, M0 EAP remark, L4, PB-2 | **DUPLICATE of `PARENT/20180006890.pdf`** (seg7 B2, NTRS 20180006890) |
| B12 | `kraiko_2001_optimal_plug_nozzles_thrust_at_start.pdf` | Kraiko, Tillyaeva & Baftalovskii, *JPP* 17(6):1347-1352 (2001) | 12 (E4), 5 (T-T4), 6, 7, 8, Route A lineage | none |
| B13 | `kraiko_2016_two_sided_asymmetric_maxthrust_nozzles.pdf` | Kraiko, Pyankov & Tillyaeva, *Fluid Dyn.* 51(1):120-125 (2016) | 18 (vector thrust), 7, 8, Route A limit, VI.6 | none |
| B14 | `kraiko_tillyaeva_2004_ideal_jet_thrust_augmentor.pdf` | **Efremov & Kraiko** (NOT Tillyaeva — filename/key is WRONG, correction C7 in the confrontation advisory: "Tillyaeva is not an author"), *Fluid Dyn.* 39(4):621-632 (2004) | 6 (PB-2), 4 (T-T3-MAP), 7, 15 | none |
| B15 | `kraiko_tillyaeva_2015_conjugate_problem_lagrange_multipliers.pdf` | Kraiko & Tillyaeva, *J. Math. Sci.* 208:181-198 (2015) | 1 (P2/G14), 18, 7, 8, CSTR_PA, F4b | none — **sample-read, see B28** |
| B16 | `liu_2022_aerospike_rde_ga_gradient_optimization.pdf` | Liu, Cheng, Zhang & Wang, *Aerosp. Sci. Tech.* 120:107300 (2022) | 8, 7, 2 (T-T3), 5, 16, 12, choking | none |
| B17 | `miki_2020_rde_nozzle_design_methodology.pdf` | Miki, Paxson, Perkins & Yungster (2020, un-timbrato, AIAA 2020-3872) | 7, 8, 15, 18, VI.1, swirl P1, choking | none |
| B18 | `nasa_teasley_2025_rdre_development.pdf` | Teasley (2025, un-timbrato, NTRS 20250000643) | 8, 7, 5, 6, 14, 15, D2.3, VI.1 | none |
| B19 | `ornano_2017_pulsed_detonation_nozzle_shapeopt.pdf` | Ornano, Braun, Saracoglu & Paniagua, *Adv. Mech. Eng.* 9(2):1-9 (2017) | 7, 8, 4, 14, VI.5, VI.6 | none |
| B20 | `paxson_miki_2022_rdre_nozzle_cfd_optimization.pdf` | Paxson, Miki, Perkins & Yungster, AIAA 2022-4107 | 7, 8, 2 (T-T3), 6 (PB-2), 15, 18, L4, choking, VI.1 | **DUPLICATE of `PARENT/Aviation_2022_final.pdf`** (seg7 B3) |
| B21 | `rubino_2018_harmonic_balance_adjoint_periodic_shapeopt.pdf` | Rubino et al., *JCP* 372:220-235 (2018) | 7, 8, T7 (H-EXO), 13, F4b, speed ledger | none |
| B22 | `schotthofer_2024_windowing_unsteady_shapeopt.pdf` | Schotthöfer, Zhou, Albring & Gauger, arXiv:2412.00604v1 (2024) | T7 (Leibniz/period), O5, 18, 13, 14 | none |
| B23 | `sun_2019_rao_contour_thermally_perfect_large_area_ratio.pdf` | Sun, Luo & Feng, *Int. J. Aerospace Eng.* 2019:4926413 | 12 (E4), pin P1/Lemma A, 8, 11 | none |
| B24 | `teasley_2023_nasa_rdre_state.pdf` | Teasley, Fedotowsky, Gradl, Austin & Heister (2023, un-timbrato, AIAA SciTech 2023-1873) | 1, 7, 8, 2 (H2'), D2.3, 6, 15 | none |
| B25 | `wintenberger_shepherd_2004_thermo_detonation_cycles.pdf` | Wintenberger & Shepherd, AIAA 2004-1033 | 15 (T-GB), 2, 4, 7, 8, VI.1, [T-EQBR] | **DUPLICATE of `PARENT/aiaa2004-1033.pdf`** (seg7 B6 — NOTE: distinct from seg7 B4 `PARENT/FickettJacobsCycle (1).pdf`, which is the OTHER Wintenberger-Shepherd paper, JPP 22(3):694-698 2006; the two are different papers by the same authors, not to be conflated) |
| B26 | `wolanski_2013_detonative_propulsion_survey.pdf` | Wolański, *Proc. Combust. Inst.* 34:125-158 (2013) | 7, 8, 1, 5, 6, D2.3, periodic-wave pin | **DUPLICATE of `PARENT/1-s2.0-S1540748912004014-main.pdf`** (seg7 B1) |
| B27 | `zahr_persson_2016_time_periodicity_constrained_adjoint.pdf` | Zahr, Persson & Wilkening, arXiv:1512.00616v2 (2016) | 7, 8, 18, 14 (T-T0), O4, Lemma-B | none |

### B28-B52. `literature_review/reports/*.md` — 25 per-paper reading reports
(class advisory-adjacent / literature-report; homogeneous internal schema:
Citation → Read coverage → What the paper does → Hypotheses (declared/undeclared)
→ Findings at TEORICO/FORMALE/ALGORITMICO levels with THREAT/CONT/ADOPT/GAP-CONFIRMS/
CORRECTION tags → Bibliography inspection). STATUS-AUTHORITY proposed for all 25:
**OF-RECORD-AS-FILED, corrigendum = `ADVISORY_litreview_confrontation_2026-08-13.md`**
(same relationship pattern as the S25 one-pass-review/CONVERGED-file pattern in
seg3: where report and confrontation-advisory diverge, the advisory governs — and
it DOES diverge on several points, see the confrontation advisory's own "errata
found by me" callouts for the 3 sample-read reports below). PLAN-ANCHOR for all 25:
directly feeds the confrontation-advisory's per-paper table (§2) and per-claim
sections (§3/§3bis); each report is the primary evidentiary FILE for its row.

Three reports read INTEGRALLY by this reader (sample, per task instruction):

- **B28. `kraiko_tillyaeva_2015_conjugate.md`** (paired PDF B15). UNIQUE-AT-RISK:
  the full equation-by-equation chain (2.2)→(2.9)→(2.10)→(2.11)→(2.12) with page
  numbers, the 8-title bibliography census (zero modern-adjoint / zero Rao-school
  cross-citation, VERIFIED — this is the datum that answers the litmap's own
  "if it cites Jameson/Giles-Pierce" test, NEGATIVE), the symbol-collision table
  (their λ₁,λ₂ fields vs our λ₂,λ₃ constants; their C₁=our −λ₂, C₂=our −λ₃), and
  five ADOPT/THREAT findings (A1 closed-form field-level adjoint oracle, A2 second
  wall residual, A3 inequality/complementarity corner form, A4 third jump-class for
  F4b, A4-second the two-bend-point optimum + procurement pointer to ref [8]). The
  report's OWN verdict ("this paper is the single most dangerous document found so
  far for Claim A") is confirmed, and REFINED (not overturned) by the confrontation
  advisory §4 verdict. Minor errata found by the judge on THIS report (date "1 June
  2015" vs paper's printed "29 August 2014"; author count on ref [8]) are of
  RECORD LOW risk, filed in §6 of the confrontation advisory.
- **B29. `giles_pierce_2001_quasi1d.md`** (paired PDF B6). UNIQUE-AT-RISK: the full
  four-regime closed-form adjoint construction (§§4-7), the 26-reference bibliography
  census (zero classical nozzle line, zero Lions/Pironneau — a SECOND independent
  zero-crossing confirmation after KT2015's), the sonic-throat logarithmic
  singularity derivation (§6.1, `I₁(ξ) ~ log(ξ)`), the internal shock adjoint BC
  Eq.(2.5) `v₂(x_s)=−(dh/dx)⁻¹`, and the explicit rejection-of-prior-literature
  quotes (Iollo v=0 "over-constrains"; Cliff et al. sign-change "misleading").
  Confrontation-advisory §3.25 (a full new section, "gap G-c" of the convergence
  round) is built almost entirely on re-reading THIS paper past what the report
  first flagged — the report's own "F3 — THREAT, CONFIDENCE MEDIA" became, after
  the convergence round, a fully quantified locus-excluded correction (A36) with a
  measured ≈4× constant inflation and an immune-gradient proof. The report is
  therefore accurate but SUPERSEDED IN DEPTH (not in fact) by §3.25 of the
  confrontation advisory.
- **B30. `harroun_2021_jpp_nozzle_perf.md`** (paired PDF B8). UNIQUE-AT-RISK: the
  full three-object taxonomy of "averaging" the paper uses (hardware CTAP
  measurement operator / post-hoc time-average of an unsteady solution / the
  quasi-cycle-averaged c_F=1.25 SURROGATE that is the programme's counter-evidence
  of record), the base-drag mechanism narrative (0.59 vs 0.95 atm, ejector
  entrainment, Schwer et al. contestation with the exact private-communication
  date 5 Jan 2021), the delayed-separation Rayleigh-layer argument (Eq. 9, 72 μs
  reinjection period), the per-surface signed thrust decomposition (Eq. 10,
  negative IE cowl c_F), and 13 named findings (F1-F13) spanning all three
  programme levels — including the "disentanglement experiment" ask (F1/§7.4) that
  the confrontation advisory later promotes to **R22, "the single highest-value
  item in the tranche"**. The report's own grade for the 0.59/0.95 atm delta
  ("measured") is the exact item the convergence round's gap G-d **downgrades** to
  "CFD-vs-CFD with partial experimental corroboration" — a live divergence between
  this report and the corrigendum-of-record, flagged in D-50 of the confrontation
  advisory as still needing propagation back INTO this report file.

Remaining 22 reports, classified from INDEX.md + confrontation-advisory table row
+ report headers (not sampled by this reader; homogeneous schema, content-level
claims already synthesized at need-level in the confrontation advisory's §2 table
and per-claim §3/§3bis sections cited above per PDF row B3-B27):
`giles_pierce_2000_intro.md`, `ancourt_2023_char_adjoint.md`, `harroun_2020_
validation.md`, `hoffman_1987_ctp.md`, `janc_2025_differentiable.md`,
`kaemming_paxson_2018_eap.md`, `kraiko_2001_plug.md`, `kraiko_2016_two_sided.md`,
`kraiko_tillyaeva_2004_augmentor.md` (NOTE: filename NOT re-keyed to
`efremov_kraiko_2004` despite duty C7/D-51 of the confrontation advisory declaring
the re-key mandatory — **duty UNEXECUTED, flag for T2**), `liu_2022_aerospike_
rde.md`, `miki_2020_nasa_methodology.md`, `ornano_2017_pde_shapeopt.md`,
`paxson_miki_2022_nasa_opt.md`, `rubino_2018_hb_adjoint.md`, `schotthofer_2024_
windowing.md`, `sun_2019_gamma_var_rao.md`, `teasley_2023_nasa_state.md`,
`teasley_2025_rdre_dev.md`, `wintenberger_shepherd_2004_thermo.md`, `wolanski_
2013_survey.md`. UNIQUE-AT-RISK for this block (collective): each report is the
sole home of its paper's full equation-level derivation chain, undeclared-hypothesis
list, and per-level (TEORICO/FORMALE/ALGORITMICO) finding IDs (F1, F2, … or T1, T2,
… per report) that the confrontation advisory cites by number but does not fully
reproduce — e.g. `kraiko_tillyaeva_2004_augmentor.md`'s full Eqq.(2.6)-(2.13)
derivation of the collapse-to-stationary result (used in confrontation-advisory
§3bis's Efremov-Kraiko discussion) lives only in that report.

### B53. `literature_review/reports/00_APPARATUS_BRIEF.md` — **READ INTEGRALLY.**
- CLASS: doc-theory (condensed apparatus brief, the litreview-confrontation
  workflow's OWN copy of the programme's theoretical/formal/algorithmic state,
  built explicitly so per-paper readers need not open M0/D-docs directly).
- ROLE: (A) theoretical level — problem (P), measure μ, T7 stationarity system,
  T-T3 collapse theorem + T-T3-SI/T-T3-MAP extensions, T-T4, PB-2, EQ-v2, declared
  rigor classes/pins; (B) formal level — Route A (control-surface, Rao/Rao-Beck)
  and Route B (multiplier-field, Hoffman/Kraiko) with exact equation numbers, the
  Λ-form validity margin (G), the tier ladder/margin-constrained KKT; (C)
  algorithmic level — data contract, per-phase evaluator/gradient, cycle layer,
  driver, certificate stack, thermo backend; (D) 20 attackable claims of record,
  each ONE falsifiable sentence.
- STATUS-AUTHORITY proposed: **OF-RECORD** (this is the literal target-under-test
  for the entire litreview-confrontation exercise; every report and the
  confrontation advisory work against exactly this snapshot). Note: it is a
  DERIVED condensation of M0/D-docs/PROGRESS as of 2026-08-12/13, not a new
  primary source — but it is the specific FROZEN VERSION the whole 25-paper
  confrontation was run against (SOTA-1's "freeze the object under test"
  discipline, see `ADVISORY_sota_definition_2026-08-13.md` SOTA-1), so any later
  drift between M0 and this brief is itself a finding.
- PLAN-ANCHOR: D6 plan spine (all phases F0-F6 named); M0 Parts I-VII condensation;
  the 20-claim list is the exact falsification target of `ADVISORY_litreview_
  confrontation_2026-08-13.md` §3 (claim-by-claim).
- UNIQUE-AT-RISK CONTENT: **HIGH** — this is the single frozen artifact that makes
  the whole confrontation exercise well-posed and REPRODUCIBLE-IN-INTENT; if T2
  archives/moves `literature_review/` without preserving this file as a dated
  snapshot, the confrontation-advisory's claim table loses its frozen referent
  (SOTA-1's freeze discipline would flag exactly this loss). Also: it is the most
  compact single-file restatement of the ENTIRE theory+formal+algorithmic stack
  currently in the repo, more compact than M0 itself — a candidate onboarding
  document, currently un-referenced from CLAUDE.md's canonical reading order.
- REFS: in — condenses `docs/rde_nozzle_MASTER.md`, `docs/rde_nozzle_P2_lemmaA.md`,
  `docs/rde_nozzle_theorem_ledger.md`, `ADVISORY_generality_litmap_2026-08-12.md`,
  `ADVISORY_litmap_extension_2026-08-13.md`, `docs/rde_nozzle_PROGRESS.md`. out —
  cited as the fixed metric by every one of the 25 per-paper reports and by
  `ADVISORY_litreview_confrontation_2026-08-13.md` throughout.

### B54. `literature_review/reports/VERIFICATION_FABLE_2026-08-13.md` — **READ INTEGRALLY.**
- CLASS: advisory (independent re-verification pass, in progress at time of
  filing — STAGES 0-1 complete, 2-5 declared in-progress with STAGE 2/3/4/5
  PARTIAL sections already landed).
- ROLE: user-mandated SECOND-PASS re-verification of the litreview-confrontation
  reports themselves, treating the Opus-era reports/verdict as an "UNRATIFIED
  QUARRY" — every load-bearing claim re-checked by direct PDF read AND against the
  programme's own record (M0 lines/docs/code), never against the apparatus brief
  alone (i.e. an independent SOTA-8-style adversarial channel against the reports,
  by a *different* reading agent — "Fable"). Delivers a calibration verdict on the
  report layer ("READER-ACCURATE" on every spot-checked item so far; errors found
  live only in DOWNSTREAM summaries — INDEX rows, orchestrator paraphrases).
- STATUS-AUTHORITY proposed: **OF-RECORD, PARTIAL/IN-PROGRESS** — explicitly
  self-declared "stages 0-1 complete; stages 2-5 in progress", with STAGE 2/3/4/5
  each individually marked FULL, PARTIAL or ADDENDUM in-file. This file is itself
  a corrigendum-in-progress to `ADVISORY_litreview_confrontation_2026-08-13.md`
  (its own errata are folded INTO that advisory's convergence round §0 "gap G-a/
  G-b/G-c/G-d", per that advisory's own text — the two files are tightly coupled
  and were converged together on 2026-08-13).
- PLAN-ANCHOR: the standing directive claim-dual-proof-standard (controprova
  teorica + caso implementato) and pipeline-sense-expert-review (R29) — this is
  that discipline applied to a LITERATURE-CONFRONTATION product instead of an
  algorithmic one, a new instance not previously seen in Phase-1.
- UNIQUE-AT-RISK CONTENT (HIGH):
  1. STAGE 0 table: 5 papers the Fable reader had ALREADY read in-conversation
     before this pass (HTH-1971, Hoffman-1967, Rao-Beck 1994, Hoffman-1987,
     Efremov-Kraiko 2004, Paxson-Miki-method) with independently-derived findings
     that do not live in the numbered per-paper reports at all (e.g. the "AUTHORS
     CORRECTED (not Kraiko-Tillyaeva)" finding for Efremov-Kraiko, which became
     confrontation-advisory correction C7).
  2. STAGE 1 (Kraiko-Tillyaeva 2015, independently re-verified pp.181-189+195-198,
     skipping only the Tricomi numerics 190-194): the calibration verdict
     "READER-ACCURATE" on the paired report, plus two named errata (submission
     date, ref-[8] author count).
  3. STAGE 2 (Giles-Pierce 2001, 19/19 pp re-read): the independent confirmation
     that Fig. 4's asymptote sits at the THROAT (x≈0), not the shock — the exact
     fact that seeds confrontation-advisory §3.25/gap-G-c.
  4. STAGE 3 + ADDENDUM (Zahr-Persson pp.1-8 + App. A p.28-29 personally read):
     the symmetry-reduction argument for why the wave-frame/per-phase formulation
     is the CORRECT object for an autonomous rotating wave (not a cheap surrogate
     of a "true" periodic adjoint) — a genuinely new theoretical argument, derived
     here, not merely reported, with an explicit "single-analyst, refuter-pending"
     caveat (NOT yet dual-proved per the standing directive).
  5. STAGE 4 PARTIAL (Harroun 2021 cross-check against the 2026-08-11 choking
     advisory): three REVISE items to the older choking advisory (T3-novelty
     clause STRUCK; "8x base drag" number loses record status; grade demotion
     G-d) — this is the FIRST WRITTEN LANDING of what the confrontation advisory
     later calls "gap G-d"; if this file is lost, the origin of that correction
     is lost even though its CONSEQUENCE survives in the confrontation advisory.
  6. STAGE 5 PARTIAL (Kraiko-Tillyaeva-Baftalovskii 2001, pp.1347-1348): the
     verbatim Sternin-1961/Shmyglevskii-1962 slip-line quote that becomes the
     confrontation advisory's R16/C30/gap-G-a chain.
  7. LOSS-PREVENTION LEDGER (closing section): explicit list of duties CO-SIGNED
     (ready for ratification, not yet ratified) and the THREE P0s of record (R1
     ISABE full text, R2 Harroun MS thesis, R22 disentanglement experiment) —
     same three P0s the confrontation advisory reaches independently, i.e. TWO
     independent processes converged on the same three top blockers.
- REFS: in — the 25 PDFs + reports it re-verifies; `ADVISORY_rde_choking_
  2026-08-11.md` (cross-checked against, Stage 4). out — its findings are FOLDED
  INTO `ADVISORY_litreview_confrontation_2026-08-13.md` REV3/convergence round
  (gaps G-a/G-b/G-c/G-d are traceable back to specific Fable stages), but the
  fold-in is partial: Stage 2's asymmetry sizing (A36's ≈4×/≈1.6× numbers) is NOT
  in this file, it was derived only in the confrontation advisory — the two files
  must be read TOGETHER, neither supersedes the other cleanly.

---

## PART C — `validation/` (9 files)

### C1. `validation/ADVISORY_SORDINE_plan_2026-08-13.md`
- CLASS: advisory (this session's — S-ORDINE's own — Phase-4 fused-judge CONVERGED
  PLAN OF RECORD). Structure-only row per task brief (this session owns it; not
  independently re-litigated by this reader).
- ROLE: the de-entropy execution plan itself — §0 counts reconciliation (436+37+137
  universe diagnosis, incl. the 37-file NEW delta this very inventory belongs to),
  §1 target tree structure, §2 status taxonomy, §3 lint-group map, §4 14-step T2
  execution plan, §5 standing rules, §6 open user decisions, §7 out-of-scope
  registrations, §8 per-question adjudication, §9 proposed new system finding, §10
  Phase-5 red-team repairs already applied in-document.
- STATUS-AUTHORITY proposed: **OF-RECORD, PENDING EXECUTION** (T2 not yet run at
  the time this reader was dispatched — this very S0b inventory is upstream input
  to that plan, feeding its §0 count reconciliation for the 64 new files).
- PLAN-ANCHOR: census R32 (S-ORDINE itself); direct successor of Phase-1 (seg1-
  seg7) + Phase-2 (positions P1-P3) + Phase-3 (refutation).
- UNIQUE-AT-RISK CONTENT: not assessed by this reader (out of brief for this pass;
  structure-only per task instruction — this session owns and will re-verify it).
- REFS: in — all seven Phase-1 inventories, `position_P1/P2/P3.md`, `refutation.md`,
  `docs/findings_registry.yaml`, `redteam_judge.md`. out — is itself the direct
  ancestor of this file (`inventory_seg8_supplement.md`), and of the eventual T2
  execution.

### C2. `validation/ADVISORY_litmap_extension_2026-08-13.md`
- CLASS: advisory (Form-1, 4 independent adversarial web auditors, query-bounded).
  **READ INTEGRALLY** (134 lines).
- ROLE: extends `ADVISORY_generality_litmap_2026-08-12.md` with a dedicated
  1971→2026 web sweep (105 distinct queries across 4 auditors) answering the user
  challenge "no evolution in later literature? verify rigorously to the present
  day." Both named claims (Rao=adjoint bridge; no cycle-averaged variational shape
  theory) SURVIVE within declared query bounds, with two named near-misses
  (Kraiko-Tillyaeva 2015's internal "conjugate problem" terminology; the
  ISABE-2003-117/Bogdanov-2002 pair). Also: a full evolution map of the classical
  Kraiko-school line 1971-2022, an RDE-nozzle-SOTA 2020-2026 three-tier census, and
  procurement/watch/wording duties (W1/W2, A1-A4).
- STATUS-AUTHORITY proposed: **OF-RECORD — PARTIALLY SUPERSEDED IN DEPTH by
  `literature_review/` + `ADVISORY_litreview_confrontation_2026-08-13.md`.** This
  advisory is the SPARK that triggered the entire literature_review acquisition +
  25-paper confrontation campaign (Part B above); several of its claims (the
  Kraiko-Tillyaeva 2015 near-miss for Claim A, the empty-niche verification) are
  now backed by full-text reads rather than web-search-tier evidence, and its own
  §5 "aggregated named blind spots" list has been partially closed (KT2015's
  reference list — blind spot #2 — is now READ, see B15/B28 above). It remains
  OF-RECORD for everything NOT re-verified: the RDE-nozzle-SOTA three-tier census
  (tier 1 parametric CFD, tier 2 average-then-classical, tier 3 surrogate/ML) and
  the full Kraiko-school evolution genealogy (Baftalovskii-Kraiko-Tillyaeva 1999,
  Fluid Dyn. 2000/2002/2007/2012, curvilinear sonic line 2012, two-sided asymmetric
  2016) are NOT covered by the 25-paper deep read.
- PLAN-ANCHOR: PB-2 novelty caveat (ISABE-2003 addition); D2 gap G3 qualification;
  generality niche claim; triggers `literature_review/` acquisition (Part B) and
  its own duties W1/W2/A1-A4 feed directly into `INDEX.md`'s TIER-1 list.
- UNIQUE-AT-RISK CONTENT:
  1. The 4-auditor query-count breakdown (27+33+23+22=105) and the explicit
     un-run instrument (Scopus/WoS forward citation-graph sweep of Rao 1958 /
     Hoffman 1967 / Guderley-Hantsch 1955 filtered by "adjoint") — lives only here.
  2. The full Kraiko-school evolution genealogy 1971-2022 (Tillyaeva 1975 swirling/
     nonuniform inflow — "closest classical antecedent to our data class"; the
     plug/spike sub-line; the 3-D retreat to direct optimization FD 49(1) 2014;
     the detonation-flank skeptical-audit line Egoryan-Kraiko 2016-2022) — this
     genealogy is NOT reproduced in the 25-paper confrontation and lives ONLY here.
  3. The RDE-nozzle 2020-2026 three-tier SOTA census with specific paper
     attributions (Li-Xu-Huang JPP 2022, AeST 107 2020, IJHE Feb 2026, Sastre HFF
     2025, IIT Madras plug 2022-23, KTH LES Jan 2026) — several of these are
     STILL NOT ACQUIRED (paywalled) and this is the only place their existence and
     relevance is recorded.
  4. 10 named blind spots (§5), most now partially addressed but not all (German/
     Japanese literature lines — items 9/10 — remain completely untouched by any
     later session).
- REFS: in — `ADVISORY_generality_litmap_2026-08-12.md` (extends). out — direct
  ancestor of `literature_review/` (Part B) and `ADVISORY_litreview_confrontation_
  2026-08-13.md`; cited in `ADVISORY_litreview_confrontation_2026-08-13.md` C1 as
  containing one FALSE half-sentence (the "no equivalence statement" clause) that
  the confrontation advisory orders corrected.

### C3. `validation/ADVISORY_litreview_confrontation_2026-08-13.md`
- CLASS: advisory (Form-2+ fused-judge verdict, 3 revisions — REV3 is a
  convergence round on 4 gaps raised against REV2; the largest single new file in
  this segment, 1289 lines). **READ INTEGRALLY** (6 passes, full coverage
  including all 25 per-paper table rows, all 25 per-claim §3/§3bis sections, the
  Kraiko-Tillyaeva-2015 dedicated §4 verdict, the 39-item adoption list §5, the
  33-row corrections table §6, the 29-row honest-residuals table §7, the 52-item
  duties list §8.1-8.6, and the closing §9).
- ROLE: THE verdict of record on the 25-paper literature confrontation. Headline:
  **0 theorems falsified**, **2 claims rewritten** (P2/G14 glossa cancelled and
  re-worded to a three-legged qualified form; claim 16 + T7(c) re-derived from an
  EQUALITY into a THREE-REGIME CONE form `D ∈ N_K(s_E*)` — a genuine repair to an
  internal M0 inconsistency, not just a literature response), **3 non-containments
  to declare** (elliptic-region mixed-type adjoint; endogenous-cycle family;
  vector-thrust/Pareto criterion), **33 corrections of record**, **39 adoptions**
  (10 rejected after attack), **29 named residuals** (3 P0, 1 G5-blocking). The
  REV3 convergence round resolved 4 gaps, 3 of which were the programme's OWN
  defects (T7(c)'s wrong-regime equality; a "measured" label on a CFD-vs-CFD
  delta; an un-attributed classical KKT structure) rather than literature gaps.
- STATUS-AUTHORITY proposed: **OF-RECORD** (explicitly self-declared "verdict of
  record"; the two one-pass-review-then-CONVERGED pattern from S25 recurs here at
  larger scale — this IS the CONVERGED file, there is no separate one-pass
  predecessor advisory in this segment, unlike S25's pattern where both layers
  were filed). Duties in §8 are UNEXECUTED as of this reader's pass (verified: the
  mandatory re-key `kraiko_tillyaeva_2004_augmentor.md`→`efremov_kraiko_2004` per
  C7/D-51 has NOT happened; the INDEX.md corrections C3/C4/C5/C9/C21 have NOT been
  applied to `literature_review/INDEX.md`).
- PLAN-ANCHOR: retro-propagation duty R4 (theory corrections same-session — NOT
  YET discharged into M0/D-docs, see D-01 through D-52 all still open); census
  R31 findings-as-code (this file, like S24's gap-map, is a MASSIVE unseeded
  corpus — 33 corrections + 39 adoptions + 29 residuals = ~101 objects with owners,
  none yet in `docs/findings_registry.yaml`); F2-entry rows named throughout
  (H-EXO hypothesis, the cone-form T7(c), R22 disentanglement experiment).
- UNIQUE-AT-RISK CONTENT (**HIGHEST in this segment — the largest unabsorbed
  corpus of the 64 new files**):
  1. The full 25-row paper-by-paper table (§2) with per-paper "what it does /
     level / verdict / claims touched" — the master cross-reference for Part B's
     25 PDFs and 25 reports.
  2. §3/§3bis: 25 claim-adjudication sections (claims 1-20 + T7 + 5 scope/pin
     items), each with the FORMULATION-OF-RECORD text block to be inserted
     verbatim into M0/D-docs — e.g. the exact replacement sentence for P2/G14
     (§3.1), the exact PB-2 blocked formulation (§3.6), the exact three-regime
     T7(c) cone form with its THEOREM-class transfer lemma (§3.15).
  3. §4: the dedicated Kraiko-Tillyaeva-2015 verdict with the record-substitution
     citation block and the symbol-collision warning (their λ₁,λ₂ vs our λ₂,λ₃).
  4. §5: 39 adoption rows (A1-A39) each with exact insertion point (VI.1-VI.6),
     cost tier, and binding clauses — e.g. A1 (Giles-Pierce quasi-1D analytic
     adjoint oracle, "the only oracle genuinely independent of GENO"), A17/A18/A19
     (Ancourt cross-code harness + O3.5 ACE residual + R1^ψ corroboration), A36
     (singularity-aware refinement policy derived from Giles-Pierce §6.1).
  5. §6: 33 correction rows (C1-C33, C29 renumbered out of sequence) fixing
     specific errors in `INDEX.md`, `ADVISORY_litmap_extension_2026-08-13.md`,
     `docs/rde_nozzle_MASTER.md` (three specific line numbers: l.844 EAP UNCAPPED
     qualifier, l.691 swirl V_y-frozen label, l.1234+l.1297 DWR locus-excluded
     clause), and `docs/rde_nozzle_P1_sections_5_7.md` §5.1(c).
  6. §7: 29 residual rows (R1-R29) with exact procurement targets — R1
     ISABE-2003-117 (P0), R2 Harroun MS thesis 2019 (P0), R22 the disentanglement
     experiment (P0, "single item of highest value"), R5 Kraiko-1979 (G5-blocking,
     KT2015 defers to it FOUR times).
  7. §8: 52 duties (D-01 through D-52) each with owner+trigger — **NONE verified
     executed** by this reader; this is therefore a SECOND large "corpus not yet
     seeded" item alongside the S24 gap-map (findings_registry.yaml still has only
     20 entries per the SORDINE plan header, none from this file).
- REFS: in — all 25 PDFs + reports (Part B), `ADVISORY_litmap_extension_2026-08-13.
  md`, `literature_review/reports/VERIFICATION_FABLE_2026-08-13.md` (the two files
  converged together for REV3), `INDEX.md`. out — targets `docs/rde_nozzle_MASTER.
  md`, `docs/rde_nozzle_P1_sections_5_7.md`, `ADVISORY_generality_litmap_2026-08-
  12.md §6`, `validation/o33_bench.py`, `validation/o32_mesh_convergence.py`,
  `validation/adaptive_knot_optimize.py`, `src/thrust/phase_diagram_real.py`,
  `src/cycles/cycles.py` — none of these edit targets show the corrections applied
  yet (unverified by direct diff in this pass, but no commit in the visible git log
  touches them post-2026-08-13 with this content).

### C4. `validation/ADVISORY_moc_zucrow_fidelity_2026-08-13.md`
- CLASS: advisory (GENO-side MoC/march/wall-BC fidelity campaign vs Zucrow &
  Hoffman Gas Dynamics Vol.2 Ch.16-17, find→verify-adversarial→adjudication, ~14
  agents + a find/verify/critic workflow). **READ INTEGRALLY** (649 lines, 2
  passes; Italian-language, GENO-side).
- ROLE: answers two user questions — (1) does the differentiable engine ("motore
  differenziale", i.e. `a1_toc_variational_jax.py`) always march on a fixed
  profile with no Goursat phases? CONFIRMED: specified-wall direct march, inverse
  wall (§16-3d), zero Goursat phases ever, per-cell causality rejector. (2) is
  GENO's MoC SOTA per the canonical Zucrow reference? Verdict: **formula-per-
  formula FAITHFUL** (11/11 book anchors confirmed on re-derivation, including a
  NEW proof that Zucrow Eqs. (16.43)/(16.44) are DEPENDENT — rank 2 of 3, EOS-
  general, no γ=const needed — so GENO not coding (16.44) loses nothing), but
  with a LONG list of GENO-side robustness/transparency/economy defects: **MOC-01
  through MOC-28** (P0/P1/P2 severities), including one **P0 measured on committed
  production output**: wall thrust DOUBLE-COUNTED on every overshoot column
  (+7.27e3 N / +2.33e4 N excess on tocnoz/defnoz, contaminating F/CF/Isp/spi/etaf/
  etai but NOT the contour/field/mass-flow/design decisions — a bookkeeping-only
  defect, "O2 (the differential-engine cross-code oracle) NOT contaminated").
- STATUS-AUTHORITY proposed: **OF-RECORD, PARTIALLY CLOSED (R-1/R-2 closed
  in-session, R-3 open pending an instrumented run, R-4 closed)**. Self-declared
  "CAMPAGNA PARZIALMENTE CHIUSA (7 flussi su 9 completi; 2 troncati dal limite di
  sessione)". This is a GENO-side finding file (owner = GENO, not the research
  program per se), but it lives in `validation/` (repo side) — a placement
  question analogous to Phase-1's cross-repo placement flags.
  **CRITICAL CROSS-REFERENCE**: GENO/ is declared read-only for this whole
  segment per the task brief and per CLAUDE.md standing directive ("GENO/ è un
  repo git indipendente: mai aggiungerlo ai commit di questo repo"), yet this
  advisory names 28 concrete GENO source-code defects with file:line precision
  and a companion PATCH FILE (C6 below) that is APPLIED to GENO's working tree —
  this is the sharpest read-only/write-adjacent tension found in this segment;
  T2 must decide the archival home explicitly (GENO's own MASTER_PLAN.md/
  CHANGELOG per this file's own §8 duty-1, not this repo's validation/).
- PLAN-ANCHOR: [X-A1IM]/[X-TOCV] engine-fidelity carriers; GENO invariants
  standing directive (moc-critical-independent-invariants memory); no D6 phase
  names this campaign directly — it is a spontaneous SOTA-fidelity audit
  triggered by a user question, closer to the S-SPEED/S-GAUNTLET pattern
  (dedicated parallel-session audit) than to a numbered D6 task. Flagged as
  ORPHAN-ADJACENT under the primary lens: its nameable need is "engine ↔ GENO ↔
  Zucrow triangulation", not a named D6/census row.
- UNIQUE-AT-RISK CONTENT (**HIGH — 28 typed findings + 2 proofs, zero seeded into
  any registry**):
  1. MOC-01 through MOC-09 (§4): the original 9 findings surviving the first
     attack wave, incl. MOC-01 (signed-RHS convergence test breaks for v≤0 —
     silent exhaustion, live in the annular/migdal lower family), MOC-03
     (throat-exit-loop silent-overwrite-of-Me on non-convergence, asymmetric vs
     the annular twin's `error stop`), MOC-04 (Ch.16 legacy no-mass-crossing path
     silently un-closes the wall, asymmetric vs Ch.17's `error stop` AND its own
     `wall_save` restore).
  2. §4.1: 5 KILLED claims (honest retraction record) — "signed-RHS near-axis"
     claim FALSE (real defect is the sign, not near-axis smallness); "1e-8
     absolute = machine-forcing" FALSE; "10x cost" inflated (real ~2.3x/7x);
     "sign-absorption in Ch.17 sources" REFUTED; "Smoothing_m unused" imprecise.
  3. §7.1: the FULL symbolic proof that Zucrow (16.43)/(16.44) are rank-2-of-3
     dependent (CAS + 2000 random probes at 1e-9), cross-validated against
     `Rao_m.f90:93-100` — a new [R4]-class theory item explicitly marked
     "retro-propagation, new, to carry into the theory docs" that (per this
     reader's check) does NOT yet appear in `boundary_equivalence_derivation.md`
     or any D-doc.
  4. §7.2: MOC-10, the P0 thrust-double-count, with exact measured numbers on
     committed baselines (tocnoz/defnoz) and the reconstruction methodology
     (Simpson-vs-Simpson, not Simpson-vs-trapezoid) — plus a documentary finding
     that `docs/audit_thrust_planar_axi.md §3` (a GENO doc) misattributes this
     exact residual to "quadrature order" when it is largely this bug.
  5. §9 (appendix, agnostic verification of the streamline-foot policy and
     fixed-point structure): MOC-16 through MOC-28, a SECOND wave of findings
     including MOC-24 ("the N-26 root cause is STILL LIVE in the fallback
     branch" — contradicts GENO's own registry claiming N-26 closed) and MOC-27
     (GENO's own MASTER_PLAN.md admits the cross-stream foot-reconstruction
     branch has NEVER been exercised — an epistemic P1).
  6. The full 12-procedure characterization table (§9.11: which of `inter_solve_
     gen`, `axis_solve_gen`, `throatExpansion_solve` etc. are well-posed-and-
     convergent (i) / well-posed-not-guaranteed (ii) / uncharacterized (iii)).
- REFS: in — `GENO/literature/Zucrow_Hoffman_Gas_Dynamics_Vol2.pdf` (page-mapped,
  book-page = PDF-page − 9), numerous GENO `.f90` source files by exact line
  number, `boundary_equivalence_derivation.md` (GENO doc, referenced but shown
  NOT to have absorbed the (16.43)/(16.44) proof). out — `LEDGER_dubbi_moc_
  2026-08-13.md` (C5 below, the companion doubt-tracking ledger for this exact
  campaign) and `RAW_geno_audit_instrumentation_2026-08-13.patch` (C6 below, the
  executable instrumentation this advisory's §D residuals depend on).

### C5. `validation/LEDGER_dubbi_moc_2026-08-13.md`
- CLASS: advisory (companion doubt-tracking ledger for the MoC/Zucrow campaign,
  standing-directive format: every doubt investigated to convergence, "cannot
  decide statically" is never terminal without a named experiment+falsifier).
  **READ INTEGRALLY** (~209 lines).
- ROLE: tracks every open doubt from the MoC-fidelity campaign (C4 above) across
  five buckets — A. CLOSED-WITH-PROOF (9 items, A1-A9, one-line doubt + one-line
  proof each, cross-referencing C4's findings), B. IN-VERIFICATION (11 items,
  B1-B11, campaigns still in flight — notably B1, a NEWLY-ADVANCED archaeology
  finding that the N-26 fix commit 704b8c1 changed TWO mechanisms at once and the
  causal attribution was never isolated, promoted to D13), C. STOPPED/re-queue (2
  items — C1 CLOSED with 7 sub-findings on thermo/T_mid discontinuity measured at
  3.7e-9 not ~1e-4, C2 open), D. EXECUTABLE-NOW-WITH-EXISTING-PATCH (13 items,
  D1-D13, each with experiment+falsifier, blocked only on shared-build
  coordination — one item, D3, already CLOSED without a new run because the proof
  was already on disk in a GENO doc), D-bis (red-team verdict on the 16 record
  findings: 2 seeded rejectors both killed by all 5 lenses, but the deflation lens
  itself mis-killed a TRUE finding F08 and over-weakened 14/16 — a methodology
  lesson about needing a false-negative canary, not just a false-positive one), D-
  ter (a "loop-until-dry" sweep whose OWN dryness/survivor counts are shown to be
  CONTAMINATED by session-limit agent failures being miscounted as "clean
  rounds" — a second methodology lesson, with 5+ new findings on previously
  un-audited modules), E. (empty, by design — the ledger's own acceptance rule),
  F. RETRACTIONS (2 items, F-R1/F-R2, claims withdrawn under user pressure after
  direct re-reading, plus a derived meta-rule about verifying which branch
  production actually executes before calling something a defect).
- STATUS-AUTHORITY proposed: **OF-RECORD, LIVE/PARTIAL** (self-declared open
  buckets B, D, and the empty-by-design E; this file is explicitly NOT closed).
- PLAN-ANCHOR: standing directive "mai posticipare il risolvibile" (never-postpone-
  resolvables) — this ledger IS an instance of that directive's discipline applied
  to the MoC campaign; same GENO-fidelity lineage as C4, no D6 phase names it
  directly (ORPHAN-ADJACENT, same flag as C4).
- UNIQUE-AT-RISK CONTENT (HIGH):
  1. The two explicit METHODOLOGY LESSONS (D-bis: "a canary measures only false
     positives; a second seed for false NEGATIVES is needed"; D-ter: "a dryness
     counter must distinguish 'empty list' from 'agent failed', or a quota limit
     disguises itself as exhaustion") — general red-team/loop-hygiene lessons not
     captured anywhere else in the repo's orchestration-form memories.
  2. D13's full bisection protocol design (TWIN-bisected build isolating
     `foot_state_from_invariants` alone vs bracket-search alone) for resolving
     which of two conflated mechanisms actually fixed the historical N-26 mass
     deficit — a concrete, ready-to-run experiment, unexecuted.
  3. The D-ter "new findings on never-audited modules" block: `Extension_m`'s
     `j2` intent(inout) monotonic-reduction bug (truncates ALL prior columns'
     output including the TOC kernel's, and can leave `j2=0` with silent exit
     code 0), the three-way-collapsed "EXT: converged" print masking target-
     reached/bound-collapse/budget-exhausted, a poisoned-point propagation path
     through 15 of 17 dispatch call-sites, and a dead-and-wrong `huge()` guard
     whose protecting branch itself uses the wrong point (`pt2` instead of a C−
     coefficient basis) — none of these appear in C4's numbered MOC-01..28 list,
     they are ADDITIONAL findings that live ONLY in this ledger.
  4. F-R1/F-R2 retractions: the exact corrected reading of `IO_m.f90:715-720`'s
     rotational-data-import branch (genuinely non-isentropic when p,rho are both
     present in the imported file) and of the 18 paired `thrust_solve` call-sites
     (Ch.17 always passes solver pressure, contra an earlier claim) — these
     retractions are LOAD-BEARING corrections to C4 that must travel WITH it; if
     C4 is archived without this ledger, two claims that C4's own reader
     originally believed (and later retracted here) could be re-asserted as true.
- REFS: in — `RAW_geno_audit_instrumentation_2026-08-13.patch` (C6, the mechanism
  for D1-D13's executable falsifiers), `ADVISORY_moc_zucrow_fidelity_2026-08-13.md`
  (C4, the finding source this ledger tracks). out — none observed yet (no
  downstream consumer has run the D-bucket experiments).

### C6. `validation/RAW_geno_audit_instrumentation_2026-08-13.patch`
- CLASS: RAW (a git-diff-format patch file, ~264 lines, applied to GENO's working
  tree — NOT this repo's tree). **READ INTEGRALLY** (small, fully diff-reviewable).
- ROLE: adds temporary `DIAG_*` counters (module-level `integer, public ::`
  accumulators) into `GENO/src/lib/MoC_Gen_m.f90` and `GENO/src/lib/Profile_m.f90`
  to instrument, at zero algorithmic change to the nominal path: chord-vs-column
  call counts, k_seg==0 events, foot-clamp events, chord-snap direction/rate,
  fraction-out-of-[0,1] events, per-column convergence deltas (position/wall-row/
  thermo), and a labeled AUDIT VARIANT B branch (an alternate bracket-surrogate
  stencil for the boundary-row lagged case) that the ledger (C5) explicitly warns
  MUST BE REMOVED before measuring nominal behaviour.
- STATUS-AUTHORITY proposed: **RAW / DERIVED-INSTRUMENT, LIVE (applied but not yet
  exercised for its intended measurement)**. This is the literal mechanism behind
  LEDGER_dubbi_moc's entire "bucket D — EXECUTABLE-NOW" list (13 doubts, blocked
  only on shared-build coordination for one instrumented run on GENO's `s3` build).
- PLAN-ANCHOR: same MoC-fidelity campaign lineage as C4/C5 (GENO invariants
  standing directive; ORPHAN-ADJACENT under the primary D6 lens, same as C4/C5).
  **Explicit cross-repo boundary tension, flagged loudly**: this patch is a diff
  AGAINST GENO's source tree, stored as a raw artifact IN this repo's `validation/`
  — GENO is declared read-only for this segment and CLAUDE.md forbids ever
  committing GENO content into this repo's commits, yet the audit's WORK PRODUCT
  (the patch) legitimately needs to live somewhere citable. T2 must decide: this
  file documents a change made TO GENO, and should probably be paired with (or
  migrated toward) GENO's OWN change-tracking (MASTER_PLAN.md/CHANGELOG, per C4's
  §8 duty-1), not treated as a permanent artifact of THIS repo's `validation/`.
- UNIQUE-AT-RISK CONTENT: the entire diff IS the at-risk content — it is the only
  record of exactly which counters/instrumentation exist in GENO's (uncommitted,
  presumably) working tree at S-ORDINE time; if GENO's working tree is reset
  without this patch being re-applied or archived, the D-bucket experiments in
  LEDGER_dubbi_moc become unexecutable exactly as specified (D1-D13 all cite
  specific `DIAG_*` names introduced only here). Also contains the AUDIT VARIANT
  B branch, which if left in place would silently ALTER GENO's algorithmic
  behaviour for the lagged lower lagged case — a live footgun the ledger names
  explicitly ("da rimuovere prima di misurare il comportamento nominale").
- REFS: in — targets `GENO/src/lib/MoC_Gen_m.f90`, `GENO/src/lib/Profile_m.f90`
  (both outside this repo's jurisdiction, read-only per session rules). out —
  every D-bucket row of `LEDGER_dubbi_moc_2026-08-13.md` depends on exactly the
  counter names this patch introduces (`DIAG_CHORD_CALL`, `DIAG_COL_KSEG0`,
  `DIAG_SNAP_PT5`/`DIAG_SNAP_PB`, `DIAG_FASE2`, `DIAG_BOOT_CLAMP`, etc.).

### C7. `validation/ADVISORY_sota_definition_2026-08-13.md`
- CLASS: advisory (methodology-definition document — defines the SOTA standard
  FOR the task class "verified corpus×programme confrontation", i.e. it is a
  RUBRIC, not a literature verdict; version 2, post refuter-attack repair round).
  **READ SUBSTANTIALLY BUT NOT FULLY VERBATIM** (opening + §0 attack-disposition
  table + cross-cutting definitions D0-D5 + criteria SOTA-1 through SOTA-9 read in
  full paragraph detail [~430 of 1197 lines]; criteria SOTA-10 through SOTA-18,
  SECTION 2 "antipatterns" and SECTION 3 "scarti" read only via header/structure
  grep, NOT verbatim; SECTION 4 "provenienza per lente" and the closing "come si
  usa questo set" + "residui aperti" sections read in full). Declared honestly as
  **READ-PARTIAL-INTEGRAL** — this is the one file in the "read integrally" list
  this reader did not fully complete verbatim, given the 1197-line length and the
  effort budget for a 64-file segment; T2 or a dedicated re-pass should complete
  SOTA-10 through SOTA-18 and Sections 2-3 before this file is cited as
  fully-verified-by-inventory.
- ROLE: a from-scratch SOTA definition for "what makes a corpus×programme
  confrontation of record", synthesized from FIVE independent blind proposals
  (lenses `evidence-synthesis`/`llm-agent-systems`/`verification-qa`/
  `metascience-audit`/`comparison-methodology`, 12 criteria each = 60 proposed),
  then ATTACKED by a default-REFUTE refuter (round 1: 11/18 criteria found
  TEST-NON-MISURABILE, i.e. unfalsifiable-as-written, and repaired; 5 REGGE
  unchanged; 1 removed as redundant; 1 new criterion born entirely from the
  attack itself — SOTA-18, seed-hygiene, proposed by 0/5 lenses). Result: an
  18-criterion set (15 NECESSARIO / 3 FORTE / 0 DESIDERABILE) over a `paper ×
  layer` cell unit (25×3=75 cells, D0), with a noise baseline `b` (D1), a
  validated gold standard (D2), a unified seed registry (D3), and a frozen
  snapshot discipline (D4/D5).
- STATUS-AUTHORITY proposed: **ADVISORY, EXPLICITLY NOT-YET-RATIFIED, NOT
  CONVERGED** — the file's own header states "Stato: ADVISORY — non è ancora di
  record finché non ratificato e ancorato a una fase del piano (R1)" AND
  "Convergenza: NON CONVERSO (il refuter ha chiuso il round 1 con
  `converged: false`)". This is therefore a **PENDING-CONTRACT-class** document
  (same status family as `ADVISORY_Scert_prompt_2026-08-12.md` in seg3), not
  OF-RECORD in the sense the other 8 validation files in this segment are.
- PLAN-ANCHOR: **NO D6 phase names this rubric directly** — flagged LOUDLY as
  ORPHAN under the primary lens. It is methodologically closest to the standing
  directives claim-dual-proof-standard and agnostic-milestone-review, and it is
  the evident METHODOLOGICAL BASIS the litreview-confrontation campaign (Part B +
  C3 above) actually RAN ON (the 75-cell grid, the paper×layer taxonomy, the
  default-REFUTE channel, the gold/witness-set language all appear operationally
  in `ADVISORY_litreview_confrontation_2026-08-13.md`) — but C3 never CITES this
  file, and this file was never explicitly ratified before C3 executed against
  it. This is a genuine plan-adherence gap: **the campaign appears to have been
  run against an unratified, self-declared-non-converged draft standard**, which
  is itself a finding for the primary lens (R1/R2 discipline).
- UNIQUE-AT-RISK CONTENT (HIGH):
  1. The full 18-criterion catalogue (SOTA-1 freeze+deviation-ledger, SOTA-2
     falsifier-shootability, SOTA-3 stratified mutant bank w/ witness-set
     discipline, SOTA-4 gold+decoys w/ derived sample-size formula
     `M=⌈ln α/ln(1−FPR_max)⌉`, SOTA-5 non-LLM verbatim matcher + assertion-VOICE +
     hop-count, SOTA-6 source-admission tiering w/ dual-OCR-engine quality
     measurement, SOTA-7 paired blind double-reading w/ noise-subtracted flip
     test, SOTA-8 default-REFUTE w/ measured attack SYMMETRY, SOTA-9 cartesian
     coverage w/ vacuity check, SOTA-10 corpus-adequacy, SOTA-11 typed hypothesis
     correspondence, SOTA-12 executed-witness reduction, SOTA-13 layer discipline,
     SOTA-14 asymmetric evidence bar, SOTA-15 invariance/independence, SOTA-16
     provenance+staleness+PAIRED NOISE BASELINE, SOTA-17 orchestration-weight
     justified by flips, SOTA-18 unified seed registry) — of these, only SOTA-1
     through SOTA-9 were read by this reader in full paragraph detail; SOTA-10
     through SOTA-18's exact test specifications are UNVERIFIED by this pass and
     are entirely at-risk if this file is not re-read before T2 archival.
  2. §0's full 18-row attack-disposition table (which criteria REGGE'd unchanged
     vs were repaired vs removed) — a compact map of exactly what the refuter
     found broken, unique to this file.
  3. The five per-lens "provenienza" blocks (§ SEZIONE 4): full bibliography per
     lens (PRISMA 2020, GRADE, Cochrane Handbook, Knight & Leveson 1986's "27
     versions, coincident failures" as the sharpest argument against consensus-
     as-evidence, ASME V&V 20-2009, ACM Artifact Review v1.1, etc.) with each
     lens's declared UNVERIFIED-by-itself citations — a methodology bibliography
     that exists nowhere else in the repo.
  4. The closing "Residui aperti" (5 items): span-voice verification still partly
     a text-judgment (no non-LLM test exists yet to distinguish "asserted" from
     "criticized"); several un-derived thresholds (0.80 recall, 0.90 agreement);
     gold-standard statistical power (`m≥20` called "weak in a statistical sense"
     by the document's own authors); unfixed token budgets; and an unresolved
     interaction between the freeze discipline and mid-window known-item
     discovery — none of these are addressed anywhere else.
- REFS: in — none observed as a source (it is a from-scratch methodology
  synthesis, the five lenses are agent roles not files). out — operationally
  consumed (uncredited) by `ADVISORY_litreview_confrontation_2026-08-13.md`'s
  entire structure (75-cell grid, [PDF]/[INF] tagging = a lightweight version of
  SOTA-5's voice+hop-count discipline, the default-REFUTE per-finding pattern of
  SOTA-8); no other file in the repo cites `ADVISORY_sota_definition_2026-08-13.md`
  by name.

### C8. `validation/ASSESSMENT_methodology_position_2026-08-13.md`
- CLASS: advisory (single-analyst rigorous assessment of methodology / idea /
  problem-importance / SOTA-ness, with a declared 3-tier evidence system [IO]
  personally-verified-this-session / [REP] sampled-accurate-from-reports /
  [APERTO] undecided-with-named-deciding-act). **READ INTEGRALLY** (132 lines).
- ROLE: directly answers the user mandate "assessment rigoroso di metodologia,
  idea, importanza, SOTA-ness — in particolare la legittimità dell'adjoint PER
  FASI contro l'adjoint transitorio/periodico". Five sections: (1) the idea is
  ORIGINAL IN QUALIFIED FORM, containment verified on equations (T7(b) restricted
  to a Dirac measure reproduces KT2015's B^x literally); "first genuinely averaged
  thrust problem" is DEAD (Efremov-Kraiko 2004 predates it), the defensible form
  is "first NON-COLLAPSING form-genuinely-averaged problem, cycle instance". (2)
  problem importance is MAXIMAL and attested BY THE FIELD ITSELF (RDE corpus
  designs on averaged states with zero theory; the field's own internal debate —
  Paxson-Miki finds the average adequate for sizing, Harroun finds it blind to
  ranking — has NO ARBITER, and this programme IS that structural arbiter). (3)
  the per-phase-vs-periodic-adjoint methodology question is answered LEGITIMATE
  WITH STRONG THEORETICAL GROUNDING (a genuinely derived symmetry-reduction
  argument, matching VERIFICATION_FABLE's Stage-3 addendum) WITHIN the declared
  pin; the adjoint construction itself sits on the PROVEN side of a real
  controversy (Giles-Pierce 2001) but continuum-fidelity remains UNTESTED pending
  oracles A1-A3; MoC/classical-line containment is clean with ONE BLOCKING GAP
  (R16, the Shmyglevskii slip-line optimum the certified tier cannot certify). (4)
  the methodology IS SOTA in a specific, defensible sense: the P2/G14 bridge
  survives ONLY as articulation+operationalization (not mathematical content —
  KT2015 instantiates the glossed content already), the niche is verified
  unoccupied, and the certification regime (rejecting oracles, derived
  tolerances, falsifiers, Verdict format) has NO EQUIVALENT anywhere in the 25-
  paper corpus, "the most robust differentiator". (5) five gating residuals named
  with owners (R1 ISABE, R2 Harroun thesis, R22 disentanglement — all P0; R16
  slip-line certificate F4b-blocking; R28 Shmyglevskii 1962 full text).
- STATUS-AUTHORITY proposed: **OF-RECORD** — this is the closest thing in the
  segment to a synthesized EXECUTIVE VERDICT across the whole literature_review
  campaign, written from a position ABOVE the per-paper/per-claim detail (unlike
  C3, which is exhaustive; this file is a compact top-level position statement).
- PLAN-ANCHOR: directly answers a user mandate (methodology/idea/importance/SOTA-
  ness assessment) that maps onto P-1 paper framing material (JPP venue) more than
  onto a specific D6 phase/census row — closest anchor is P-1 (paper deliverable)
  and the G5 human-pass gate (since it repeatedly invokes G5-blocking items).
  Flagged as **PARTIALLY ORPHAN under the primary D6-phase lens** (no phase/task
  tag names it) though its CONTENT is clearly P-1-framing-material of high value.
- UNIQUE-AT-RISK CONTENT (HIGH):
  1. The T7(b)-to-Kraiko-Tillyaeva-Baftalovskii-(2.9)-under-Dirac-measure
     containment demonstration and the Efremov-Kraiko-2004-precedent-with-named-
     collapse-cause (§1) — a compact, citable containment proof not spelled out
     this precisely anywhere else (C3 has the pieces scattered across §3.6/§3bis).
  2. §2's crisp two-sentence statement of the field's own unresolved internal
     debate (Paxson-Miki adequate-for-sizing vs Harroun blind-for-ranking) as THE
     justification for problem importance — a rhetorical/framing asset for P-1's
     introduction, unique in this compact form.
  3. §3.1's symmetry-reduction argument for per-phase-vs-periodic adjoint
     legitimacy, PRESENTED AS A METHODOLOGY VERDICT (co-signed from structure, not
     just cited from VERIFICATION_FABLE) — this is the most citable single
     statement of that argument in the whole segment.
  4. §4's explicit "what we CANNOT say" list (4 items: the bridge's mathematical
     content is not ours; the inequality-at-inadmissibility structure is not ours
     [Shmyglevskii 1962]; averaging-suffices-for-ranking is OPEN; adjoint-fidelity-
     to-continuum is OPEN pending A1/A2/A3) — a compact liability list useful for
     G5/pre-submission review, not assembled this concisely elsewhere.
  5. §6's coverage-and-tier accounting (which papers were [IO] personally verified
     by THIS assessment's author vs [REP] sampled from reports) — a second,
     INDEPENDENT sampling-accuracy claim alongside VERIFICATION_FABLE's, using
     an overlapping but not identical paper set.
- REFS: in — the same 25-paper corpus (Part B), `Zahr-Persson`, `Giles-Pierce
  2001`, `Efremov-Kraiko 2004`, `M0:1071-1130`. out — none observed citing this
  file specifically (it appears to be a leaf synthesis document, not yet
  referenced by `ADVISORY_litreview_confrontation_2026-08-13.md` or any other
  file in this segment — a possible loose end for T2's cross-reference pass).

### C9. `validation/PROGRESS_2026-08-13_Sordine.md`
- CLASS: session-log (live, mid-session continuity guard — explicitly written as
  a restart map in case of a session-limit death, per R3). Structure-only row per
  task brief (this session owns it).
- ROLE: S-ORDINE session log to date — STEP 1 opening (HEAD verified a021fdd),
  STEP 2 fresh diagnosis (436-file tree, authoritative partition into 7 segments
  matching seg1-seg7 exactly, scarto 0), STEP 3 T1 planning workflow (7 inventory
  readers → 3 positions → refuter → fused judge → red-team, `wf_1b94cb5c-166`),
  a RESTART MAP, and STEP 3-bis documenting one session-limit interruption and a
  successful resume-not-relaunch (readers replayed from cache at 0 cost).
- STATUS-AUTHORITY proposed: **RAW/LIVE** (self-declared "IN PROGRESS", the exact
  session this S0b reader operates within).
- PLAN-ANCHOR: R3 (session closure/continuity discipline) — this file IS a live
  instance of that rule; census R32 (S-ORDINE itself).
- UNIQUE-AT-RISK CONTENT: the exact workflow-run-id (`wf_1b94cb5c-166`) and the
  resume/session-limit incident record (which position/refuter/judge stages died
  vs completed, and the exact resume mechanism used) — durable orchestration-
  process evidence not reproduced elsewhere; relevant to the standing
  orchestration-weight-sota directive as a real data point on resume-cost.
- REFS: in — the 7 Phase-1 inventories + `docs/findings_registry.yaml` (20
  entries, read at session open). out — will be superseded by this session's
  final PROGRESS update per R3 at S-ORDINE closure; this S0b inventory
  (`inventory_seg8_supplement.md`) is itself downstream of STEP 2's diagnosis.

---

## CROSS-ROOT / CROSS-SEGMENT DEDUP SUMMARY (new to this segment)

1. **`literature/aerospace-10-00797.pdf`** (Part A) duplicates
   **`literature_review/ancourt_2023_adjoint_direct_characteristic_equations.pdf`**
   (Part B, B3) — same paper (Ancourt, Peter & Atinault, Aerospace 10:797, 2023),
   landed in TWO locations across this one delta. Corroborated by
   `literature_review/lint_index_consistency.py`'s own record of a THIRD copy
   (`"aerospace-10-00797 (1).pdf"`, md5-identical to ancourt_2023) having already
   been found and removed inside `literature_review/` on the same date.
2. **Five of the 25 `literature_review/` PDFs duplicate pre-existing Root-B
   (`PARENT/`) files already inventoried in `inventory_seg7_literature.md`**:
   `wolanski_2013...pdf` ≡ seg7 B1; `kaemming_paxson_2018...pdf` ≡ seg7 B2;
   `paxson_miki_2022...pdf` ≡ seg7 B3; `wintenberger_shepherd_2004...pdf` ≡ seg7
   B6 (NOT B4 — B4 is a DIFFERENT Wintenberger-Shepherd paper, JPP 2006, easy to
   conflate); `harroun_2021...pdf` ≡ seg7 B7. **This breaks seg7's own closing
   claim** ("no paper PDF is duplicated across the three roots") — that claim was
   true only as of Phase-1's 137-file universe; the 25-file literature_review
   acquisition reintroduced 5 of those exact papers into a FOURTH location
   without checking against the already-inventoried Root B.
3. Net new-content PDFs in this 64-file delta (i.e. NOT duplicating anything
   already in the repo/parent/GENO universe): 20 of the 25 `literature_review`
   PDFs (all except the 5 dedup rows above) — these ARE genuinely new
   acquisitions (Kraiko-Tillyaeva 2015, both Giles-Pierce papers, Ancourt is a
   dup so excluded, Kraiko 2001/2016, Efremov-Kraiko 2004, Sun 2019, Hoffman
   1987, Fernandes 2023, Rubino 2018, Zahr-Persson 2016, Schotthöfer 2024, JANC
   2025, Liu 2022, Ornano 2017, Harroun 2020, Miki 2020, both Teasley papers) —
   19 truly new, not 20 (Ancourt/aerospace-10-00797 is itself a within-delta
   duplicate, already counted in item 1).

## AT-RISK LEDGER — TOP ROWS OF THIS SEGMENT (feeds the nothing-lost ledger)

1. **~101 typed objects (corrections/adoptions/residuals/duties) in
   `ADVISORY_litreview_confrontation_2026-08-13.md`, ZERO seeded into
   `docs/findings_registry.yaml`** (still 20 entries per the SORDINE plan
   header) — the single largest unabsorbed corpus in this 64-file delta,
   comparable in scale to the S24 gap-map that R31 was created to seed.
2. **28 typed MOC-01..28 findings + 2 new theorems in `ADVISORY_moc_zucrow_
   fidelity_2026-08-13.md`, PLUS ~13 additional findings in `LEDGER_dubbi_
   moc_2026-08-13.md`'s D-ter block** — all GENO-owned, none registered in
   GENO's own MASTER_PLAN.md/CHANGELOG per this reader's spot-check of the
   advisory's own §8 duty-1 ("not yet executed"); a genuine cross-repo dedup/
   registration gap.
3. **`ADVISORY_sota_definition_2026-08-13.md` is EXPLICITLY non-ratified,
   non-converged (refuter closed round 1 with `converged: false`), yet its
   methodology (75-cell grid, [PDF]/[INF] voice tags, default-REFUTE-per-
   finding) is operationally the exact shape `ADVISORY_litreview_confrontation_
   2026-08-13.md` used** — an un-cited, un-ratified standard was run against
   in practice. Flag for R1/R2 (plan-adherence, session-opening discipline).
4. **`kraiko_tillyaeva_2004_augmentor.md` filename NOT re-keyed** to
   `efremov_kraiko_2004` despite the confrontation advisory's own C7/D-51
   declaring the re-key mandatory (wrong author attributed — Tillyaeva is not
   an author of this 2004 paper) — a concrete, cheap, unexecuted duty.
5. **`RAW_geno_audit_instrumentation_2026-08-13.patch` sits in this repo's
   `validation/` but patches GENO's independent tree**, including a live
   AUDIT-VARIANT-B branch the companion ledger warns must be removed before
   any nominal-behaviour measurement — a real footgun if forgotten.
6. **Cross-root PDF re-duplication** (dedup summary items 1-2 above): 6 of the
   25+1 new PDFs in this delta are byte-identical-in-substance to files already
   inventoried in seg7 — a nothing-lost risk is LOW here (content is doubly
   preserved) but a HOUSEKEEPING/T2-lint gap is real (no cross-root dedup lint
   exists; `lint_index_consistency.py` only checks INSIDE `literature_review/`).

## CODENAME TOKEN COLLECTION (new tokens/instances seen in this segment,
feeding the T2-bis glossary; tokens already catalogued in seg3/seg7 are not
re-listed unless a NEW meaning/instance appears here)

| Token | Where seen (this segment) | Meaning / new instance |
|---|---|---|
| P2/G14 | throughout Part B/C3 | Rao=adjoint bridge claim — QUALIFIED (glossa cancelled) per this segment's convergence |
| D2-G3 | C2, C3 | no-averaged-shape-theorem gap — CONFIRMED, reformulated stronger ("everyone averages, nobody derives optimality of the average") |
| PB-2 | C2, C3 §3.6 | truncated-plug averaged problem — BLOCKED FORMULATION now mandatory: "first FORM genuinely averaged and non-collapsing, cycle instance" |
| T-T3 / T-T3-MAP / T-T3-SI | C3 §3.2-3.4 | collapse theorem family — theorem intact; new externally-measured breaker "cycle/base-wake ejector coupling" (grade demoted G-d) |
| T-T4 | C3 §3.5 | plug nesting theorem — sharpness clause now externally corroborated (Harroun: no analytic base-pressure model exists) |
| T7(c) / (\*\*') | C3 §3.15 | weighted transversality — REWRITTEN in three-regime cone form `D ∈ N_K(s_E*)`, new THEOREM-class transfer lemma |
| EQ-v2 | C3 §3.9 | DEF-equivalence conjecture — CONTACT (not touch) found: classical inequality-KKT structure at inadmissibility (Sternin 1961/Shmyglevskii 1962) |
| H-EXO | C3 §3.20, D-02 | new hypothesis to add to T7 (exogenous cycle measure/interface map), falsifier `dμ/dΣ≠0` |
| H2' | C3, B30 | fixed-wall/ambient-blind hypothesis — Harroun 2021 named as the empirical demonstration of hardware OUTSIDE it |
| X-GP01 | C3 A1 | new named oracle: Giles-Pierce quasi-1D analytic adjoint, GENO-independent |
| O3.5 | C3 A18 | new named oracle: Ancourt ACE residual, per-phase, complementary to O3.1 |
| O6 | C3 A3 | proposed new field-level closed-form adjoint oracle (KT2015 (2.11)) |
| [X-GENOXC] | C3 A17 | cross-code metric harness, solver-agnostic, Ancourt-derived |
| C1-C33 | C3 §6 | new correction-of-record rows (this segment's own numbering, distinct from S24's C1-C45 choice ledger) |
| A1-A39 | C3 §5 | new adoption rows (this segment's own numbering) |
| R1-R29 | C3 §7 | new residual rows (R1/R2/R22 = the three P0s of this segment) |
| D-01..D-52 | C3 §8.1-8.6 | new duty rows |
| G-a/G-b/G-c/G-d | C3 REV3 header, VERIFICATION_FABLE | the four convergence-round gap labels (attribution/cone-form/sonic-singularity/evidence-grade) |
| gap G-d | C3, B30 | "measured" → "CFD-vs-CFD with partial experimental corroboration" downgrade rule |
| R16 | C3 §7, C8 | slip-line certificate gap — now BLOCKING with a named acceptance test (certify the Shmyglevskii discontinuous plug benchmark) |
| C30 | C3 §6 | attribution correction: inequality-at-inadmissibility structure is CLASSICAL (1961-62), not ours |
| C31/C32 | C3 §6 | T7(c) cone-form + its economical sign-based falsifier |
| S1-S3 | C3 A37-A39 | three new zero-cost Verdict rejectors (dual feasibility on λ_e, axial λ_L row, per-phase sign-scan) |
| MOC-01..MOC-28 | C4 | GENO MoC fidelity findings (this segment's own numbering, GENO-owned) |
| A1-A9 (ledger) | C5 | closed-with-proof doubts (LEDGER's own numbering, distinct from C3's A1-A39) |
| B1-B11 (ledger) | C5 | in-verification doubts |
| D1-D13 (ledger) | C5 | executable-now doubts, tied to the DIAG_* patch (C6) |
| DIAG_* | C6, C5 | instrumentation counter family (CHORD_CALL, COL_KSEG0, SNAP_PT5/PB, FASE2, BOOT_CLAMP, LAG_CLAMP, FRACRAW_MIN/MAX, …) |
| AUDIT VARIANT B | C6 | temporary alternate stencil branch, must-remove-before-nominal-measurement flag |
| N-26 | C4 §7.1, C5 B1/D13 | historical foot-reconstruction mass-deficit fix — root cause re-opened (MOC-24, D13) as never causally isolated |
| SOTA-1..SOTA-18 | C7 | the new 18-criterion confrontation-methodology rubric (unratified) |
| D0-D5 (sota-def) | C7 | cross-cutting definitions: CELL, noise baseline `b`, GOLD, seed registry, snapshot_id, temporal anchor |
| [IO]/[REP]/[APERTO] | C8 | the assessment's own 3-tier evidence marking (personally-verified / sampled-accurate / undecided) |
| [PDF]/[INF] | C3 | the confrontation advisory's verbatim-vs-inference tagging convention (parallels SOTA-5's voice discipline) |

---

## COUNT ACCOUNTING

**Files accounted: 64/64.**

Breakdown:
- **Part A (root `literature/`)**: 1 file — classified-without-read (PDF rule).
- **Part B (`literature_review/`)**: 54 files —
  - Read-integral: **5** (`INDEX.md`, `reports/00_APPARATUS_BRIEF.md`,
    `reports/VERIFICATION_FABLE_2026-08-13.md`, and the 3 declared sample
    per-paper reports `kraiko_tillyaeva_2015_conjugate.md`,
    `harroun_2021_jpp_nozzle_perf.md`, `giles_pierce_2001_quasi1d.md` — wait,
    that is 3 reports + INDEX + brief + fable = **6** read-integral; see exact
    count below).
  - Classified-without-full-read: **48** (25 PDFs, classify-per-PDF-rule; 22
    remaining per-paper reports, classified from INDEX+table+headers; 1 code
    file `lint_index_consistency.py`, docstring+head read, classified as code).
  - **Exact Part B split: 6 read-integral (INDEX.md, 00_APPARATUS_BRIEF.md,
    VERIFICATION_FABLE_2026-08-13.md, kraiko_tillyaeva_2015_conjugate.md,
    harroun_2021_jpp_nozzle_perf.md, giles_pierce_2001_quasi1d.md) + 48
    classified (25 PDF + 22 report + 1 code) = 54.**
- **Part C (`validation/`)**: 9 files —
  - Read-integral: **6** (`ADVISORY_litmap_extension_2026-08-13.md`,
    `ADVISORY_litreview_confrontation_2026-08-13.md`,
    `ADVISORY_moc_zucrow_fidelity_2026-08-13.md`, `LEDGER_dubbi_moc_2026-08-13.
    md`, `RAW_geno_audit_instrumentation_2026-08-13.patch`,
    `ASSESSMENT_methodology_position_2026-08-13.md`).
  - Structure-only (this session owns, per task brief): **2**
    (`ADVISORY_SORDINE_plan_2026-08-13.md`, `PROGRESS_2026-08-13_Sordine.md`).
  - Read-partial-integral, honestly declared incomplete: **1**
    (`ADVISORY_sota_definition_2026-08-13.md` — ~40% verbatim coverage: opening,
    §0, D0-D5, SOTA-1..9 in full; SOTA-10..18 and SECTIONS 2-3 header/grep only).

**TOTALS.**
- **1 (Part A) + 54 (Part B) + 9 (Part C) = 64 = the declared list total,
  discrepancy 0.**
- **Read-integral (unqualified): 6 (Part B) + 6 (Part C) = 12.**
- **Read-partial-integral (honestly declared, not fully verbatim): 1**
  (`ADVISORY_sota_definition_2026-08-13.md`).
- **Structure-only (this session's own artifacts, per task brief): 2**
  (SORDINE plan, live log).
- **Classified-without-read/without-full-read: 1 (Part A) + 48 (Part B) = 49**
  (25 literature PDFs, 22 per-paper reports classified from index+table+headers,
  1 code file classified from docstring+head, 1 duplicate root PDF classified
  from filename+cross-reference).
- **12 + 1 + 2 + 49 = 64.** ✓ Reconciled.

**At-risk count (rows flagged UNIQUE-AT-RISK CONTENT with HIGH or explicit
loud-flag severity, this segment): 9** — B53 (00_APPARATUS_BRIEF, frozen-object
loss risk), B54 (VERIFICATION_FABLE, in-progress corrigendum), C3
(litreview-confrontation, ~101 unseeded objects), C4 (moc-zucrow-fidelity, 28
GENO findings + 2 theorems unseeded), C5 (LEDGER_dubbi_moc, methodology lessons
+ ~13 new findings), C6 (GENO patch, cross-repo footgun), C7 (sota-definition,
unratified-yet-operationally-used rubric), C8 (methodology assessment,
un-cross-referenced synthesis), and the dedup finding A1/B3 (aerospace-10-00797
cross-root duplicate, LOW content risk but real housekeeping risk). Plus the two
segment-level cross-cutting risks in the AT-RISK LEDGER section above
(findings-registry seeding backlog; unratified-methodology-in-practical-use).

*End of segment-8 supplementary inventory. Reader: S0b. Coverage: 64/64
accounted, 12 read-integral (unqualified) + 1 read-partial-integral (declared)
+ 2 structure-only (session-owned) + 49 classified-without-full-read.*
