# literature_review — procurement index (sweep 1971→2026)

Source: `validation/ADVISORY_litmap_extension_2026-08-13.md` (4 adversarial auditors, 105 queries).
Legend: [OK] = PDF in this folder · [GET] = manual download needed · [HARD] = no online route found.
Links marked (unverified DOI) follow a standard publisher pattern but were NOT resolved by the sweep —
check before citing (GENO CLAUDE.md §1: never cite a reference you have not verified).

---
## STATO ACQUISIZIONE (aggiornato 2026-08-13, dopo la consegna utente)

**26 PDF in cartella** (ri-misurato 2026-08-20: +CF_ASO_Paper_PrePrint, arrivo 2026-08-14), etichettati `autore_anno_slug.pdf`, zero duplicati.
Duplicati rimossi: `aerospace-10-00797 (1).pdf` (md5 identico), `s12567-023-00511-1 (2).pdf` (md5
identico), e il preprint arXiv di Ancourt — **sostituito dalla versione pubblicata** Aerospace 2023,
10, 797 (peer-reviewed = citabile; il preprint era lo stesso lavoro).

ACQUISITI (26) — nomi ESATTI su disco, senza estensione:
`CF_ASO_Paper_PrePrint` (arrivo 2026-08-14, registrato nel literature
registry come unread_cf_aso_preprint; aggiunto qui 2026-08-20 alla
chiusura C3 — lint (ii)/(iii) riparato, conteggio ri-misurato) ·
`ancourt_2023_adjoint_direct_characteristic_equations` ·
`fernandes_2023_moc_shape_optimization_rocket_nozzles` ·
`giles_pierce_2000_intro_adjoint_design` · **`giles_pierce_2001_analytic_adjoint_quasi1d_euler`** ·
`harroun_2020_rde_nozzle_simulation_validation` ·
**`harroun_2021_computational_experimental_rdre_nozzle_performance`** ·
`hoffman_1987_compressed_truncated_perfect` · `janc_2025_differentiable_reacting_solver_adjoint` ·
**`kaemming_paxson_2018_equivalent_available_pressure`** ·
**`kraiko_2001_optimal_plug_nozzles_thrust_at_start`** ·
`kraiko_2016_two_sided_asymmetric_maxthrust_nozzles` · `kraiko_tillyaeva_2004_ideal_jet_thrust_augmentor` ·
**`kraiko_tillyaeva_2015_conjugate_problem_lagrange_multipliers`** ·
`liu_2022_aerospike_rde_ga_gradient_optimization` · `miki_2020_rde_nozzle_design_methodology` ·
`nasa_teasley_2025_rdre_development` · `ornano_2017_pulsed_detonation_nozzle_shapeopt` ·
**`paxson_miki_2022_rdre_nozzle_cfd_optimization`** ·
`rubino_2018_harmonic_balance_adjoint_periodic_shapeopt` ·
`schotthofer_2024_windowing_unsteady_shapeopt` · `sun_2019_rao_contour_thermally_perfect_large_area_ratio` ·
`teasley_2023_nasa_rdre_state` · **`wintenberger_shepherd_2004_thermo_detonation_cycles`** ·
**`wolanski_2013_detonative_propulsion_survey`** · `zahr_persson_2016_time_periodicity_constrained_adjoint`.

Grassetto = item marcati decisivi dal sweep o arrivati dopo la prima consegna. Il TIER-1
Kraiko-Tillyaeva 2015 è ARRIVATO; Giles-Pierce JFM 2001 (voce "verify, do not buy") è SU DISCO —
voce chiusa. **Consegna utente 2026-08-13 06:10, cinque file (ingeriti nel round di convergenza
2026-08-13):** harroun_2021 (JPP 37(5):660-671), paxson_miki_2022 (= AIAA 2022-4107),
kaemming_paxson_2018 (= AIAA 2018-4567), wintenberger_shepherd_2004 (= AIAA 2004-1033),
wolanski_2013 (Proc. Combust. Inst. 34:125-158).

ANCORA MANCANTI, per peso:
1. ISABE-2003-117 e Bogdanov 2002 (TIER 1, gli unici due che possono ancora ribaltare PB-2/D2-G3).
2. **Harroun, A. J., M.S. Thesis, Purdue, July 2019** (P0 di record, duty D-29). NB: dopo la lettura
   di harroun_2021 §III.C il P0 è **DECLASSATO a P1** — la costruzione di cycle-averaging e il suo
   esito sono ora citabili da fonti peer-reviewed su disco (vedi TIER 2). Resta necessaria solo per
   il dettaglio numerico della stima "+1% Isp flared" riportata di seconda mano in harroun_2020 p.10.
3. Sotto-linea plug Kraiko: Fluid Dyn. 35(6) 2000, 37(5) 2002, 42(2) 2007, 47(2) 2012.
4. AIAA: Bigler 2019-0197, Fievisohn 2018-0881.
5. Li-Xu-Huang JPP 2022 (B38539), AeST 107 (2020), IJHE feb 2026, Sastre HFF 2025,
   Kraiko Thermophys. Aeromech. 29 (2022), Tillyaeva TsAGI 1975.

REVIEW: workflow `litreview-confrontation` (run wf_ab852ac5-8e6) ha letto i primi 20 e li ha
confrontati uno a uno con l'impianto (teorico/formale/algoritmico) a convergenza; il round di
convergenza 2026-08-13 ha ingerito i 5 restanti. Report per-paper in `reports/`, verdetto in
`validation/ADVISORY_litreview_confrontation_2026-08-13.md`.

**LINT DI COERENZA (duty D-14, esteso).** Il lint armato deve verificare TRE cose, non una:
(i) ogni filename citato in questo INDEX esiste su disco (il controllo originale, 5 disallineamenti
trovati a mano e qui riparati); (ii) ogni PDF su disco compare nella lista ACQUISITI;
(iii) **`count(*.pdf su disco) == count(lista ACQUISITI) == il numero dichiarato a inizio sezione`**
— è la clausola che avrebbe fatto sparare il lint sulla consegna delle 06:10, quando il conteggio
dichiarato (20) e il disco (25) hanno divergiuto senza che nessun filename fosse sbagliato.
Rejector seminabile per ciascuna delle tre: (i) rinominare un file, (ii) aggiungere un PDF non
listato, (iii) alterare il solo numero dichiarato lasciando la lista corretta.

---
## TIER 1 — blocking: can flip a verdict of record

- [HARD] **Kraiko, Pyankov, Tillyayeva, "Optimal nozzle design when time-changing its throat size and
  pressure ratio", ISABE-2003-117, 16th ISABE, Cleveland, 2003.**
  Near-miss for PB-2 / D2-G3: variational maximum-AVERAGE-thrust contouring. Must confirm it is
  quasi-steady + spatially uniform (currently inferred, not read).
  Routes: ISABE/AIAA proceedings order · interlibrary loan · direct request to CIAM authors.
  Search: https://www.google.com/search?q=ISABE-2003-117+Kraiko+optimal+nozzle+time-changing+throat
- [HARD] **Bogdanov, Kraiko, P'yankov, Tillyaeva, "Contouring an asymmetric nozzle with time-dependent
  stagnation parameters...", Aeromekhanika i Gazovaya Dinamika No. 3, 43 (2002)** (Russian original).
  Route: eLibrary.ru https://elibrary.ru/ (search "Крайко Тиллиаева сопло нестационарные параметры")
- [GET] **Kraiko & Tillyaeva, "Conjugate Problem for Lagrange Multipliers and Consequences for PDEs of
  Mixed Type", J. Math. Sci. 208:181-198 (2015).** The reference list alone decides Claim A: if it
  cites Jameson/Giles-Pierce, the Rao=adjoint bridge is no longer ours.
  https://link.springer.com/article/10.1007/s10958-015-2436-z

## TIER 2 — free (downloaded unless marked GET)

- [OK] `ancourt_2023_adjoint_direct_characteristic_equations.pdf` — Ancourt, Peter, Atinault,
  "Adjoint and direct characteristic equations for 2-D compressible Euler flows", arXiv:2305.03499
  (ONERA 2023). MoC applied to adjoint Euler, nozzle-validated; 47 refs, zero classical citations
  = the affirmative evidence for Claim A. https://arxiv.org/abs/2305.03499
- [OK] `janc_2025_differentiable_reacting_solver_adjoint.pdf` — JANC, arXiv:2504.13750 (Tsinghua, Bing Wang).
  Differentiable JAX reacting solver, adjoint demo on RDC = named threat vector 2026+.
  https://arxiv.org/abs/2504.13750
- [OK] `zahr_persson_2016_time_periodicity_constrained_adjoint.pdf` — Zahr & Persson, fully discrete adjoint with
  time-periodicity constraints, arXiv:1512.00616. https://arxiv.org/abs/1512.00616
- [OK] `schotthofer_2024_windowing_unsteady_shapeopt.pdf` — Schotthöfer et al., windowing
  regularization for unsteady shape optimization, arXiv:2412.00604. https://arxiv.org/abs/2412.00604
- [OK] `hoffman_1987_compressed_truncated_perfect.pdf` — Hoffman, JPP 3(2):150-156 (1987).
  Epitaph of the US line (CTP ≈ Rao in practice).
  http://ftp.demec.ufpr.br/CFD/bibliografia/propulsao/hoffman_1987.pdf
- [OK] `giles_pierce_2000_intro_adjoint_design.pdf` — Giles & Pierce, "An Introduction to the Adjoint
  Approach to Design", Flow Turb. Combust. (2000).
  https://people.maths.ox.ac.uk/~gilesm/files/ftc00.pdf
- [OK] `nasa_teasley_2025_rdre_development.pdf` — Teasley, "NASA's RDRE Development", AAS G&C Feb 2025.
  https://ntrs.nasa.gov/citations/20250000643
- [OK] `harroun_2020_rde_nozzle_simulation_validation.pdf` — Experimental validation of nozzle flow
  simulations for RDREs. https://ntrs.nasa.gov/citations/20230009329
- [OK] `miki_2020_rde_nozzle_design_methodology.pdf` — Miki, Paxson et al., AIAA 2020-3872.
  https://ntrs.nasa.gov/citations/20205004461
- [OK] `teasley_2023_nasa_rdre_state.pdf` — AIAA SciTech 2023-1873.
  https://ntrs.nasa.gov/citations/20220018157
- [OK] `harroun_2021_computational_experimental_rdre_nozzle_performance.pdf` — Harroun, Heister, Ruf,
  JPP 37(5):660-671 (2021), DOI 10.2514/1.B38244. **Il derivato peer-reviewed della tesi Harroun
  2019**: §III.C p.671 porta la costruzione di cycle-averaging (media di calcoli assialsimmetrici
  a pressione costante sulle fasi del ciclo, C_F = 1.25 per ENTRAMBI gli aerospike) e il suo esito
  negativo; Eq. (7) p.666 è la legge di ciclo (decadimento logaritmico, 2 onde, 13.8 kHz).
- [OK] `kaemming_paxson_2018_equivalent_available_pressure.pdf` — Kaemming & Paxson, "Determining the
  Pressure Gain of Pressure Gain Combustion", AIAA 2018-4567. Definizione EAP/EAPi allineata
  SAE/JANNAF; Eqq. (1)-(8) = antenato pubblicato del rung int-max (NON sonic-capped); Eqq. (10)-(13)
  = antenato della convenzione "state-averaged reference-state reconstruction" col pin M=1.
- [OK] `paxson_miki_2022_rdre_nozzle_cfd_optimization.pdf` — Paxson, Miki, Perkins, Yungster,
  "Computational Fluid Dynamic Optimization of an Experimental Rotating Detonation Rocket Engine
  Nozzle", NASA GRC = **AIAA 2022-4107** (identità verificata sul frontespizio). Seguito di
  Miki 2020: sweep parametrico a 2 scalari su 8 geometrie CFD 3-D, nessun ottimizzatore.
- [OK] `wintenberger_shepherd_2004_thermo_detonation_cycles.pdf` — Wintenberger & Shepherd,
  "Thermodynamic Analysis of Combustion Processes for Propulsion Systems", AIAA 2004-1033.
  Ciclo Fickett-Jacobs; Eq. (48)/(56) = upper bound sul LAVORO per unità di massa di esplosivo,
  a monte dell'ugello — non traducibile in bound propulsivo per ammissione degli autori.
- [OK] `wolanski_2013_detonative_propulsion_survey.pdf` — Wolański, "Detonative propulsion",
  Proc. Combust. Inst. 34:125-158 (2013). Survey; peso basso; zero contenuto di ottimizzazione
  di forma o variazionale.
- [GET] **Sun et al., "New Contour Design Method for Rocket Nozzle of Large Area Ratio", Int. J.
  Aerospace Eng. 2019** — open access, Cloudflare-blocked to curl. Rao control surface re-derived for
  thermally perfect gamma(T); compare vs our E4/Lemma-B.
  https://onlinelibrary.wiley.com/doi/10.1155/2019/4926413
- [GET] **Ornano, Braun, Saracoglu, Paniagua, Adv. Mech. Eng. 9(2) (2017)** — open access, blocked to
  curl. Nozzle shape optimization for pulsed detonation combustor.
  https://journals.sagepub.com/doi/10.1177/1687814017690955

## TIER 3 — paywalled; verdicts currently rest on abstracts

Methodological neighbours
- **Rubino et al., J. Comput. Phys. 372:220 (2018)** — harmonic-balance adjoint, period-averaged
  objectives. Proves the gap is not technological.
  https://www.sciencedirect.com/science/article/pii/S0021999118304017
- **Fernandes, Souza, Afonso, CEAS Space Journal (2023)** — MoC-based shape optimization (FFD +
  NSGA-II): closest occupant of the niche we call empty.
  https://link.springer.com/article/10.1007/s12567-023-00511-1

RDE / detonation (tier-2 "average-then-classical" corpus we would subsume)
- **Li, Xu, Huang, "Nozzle Design for RDE", JPP 38 (2022)** — NB: "area-variational source term" =
  area variation, NOT calculus of variations. https://arc.aiaa.org/doi/10.2514/1.B38539
- **Liu, Cheng, Zhang, Wang, Aerosp. Sci. Tech. 120:107300 (2022)** — parabolic spike + GA/gradient,
  5 objectives; only formal optimizer in the corpus.
  https://www.sciencedirect.com/science/article/abs/pii/S1270963821008105
- **"Performance of a rotating detonation chamber with different aerospike nozzles", Aerosp. Sci.
  Tech. 107 (2020)** — design from time-averaged outlet (author list not pinned).
  https://www.sciencedirect.com/science/article/abs/pii/S1270963820310208
- **Int. J. Hydrogen Energy, Feb 2026** — most explicit a-posteriori defence of designing on the mean.
  https://www.sciencedirect.com/science/article/pii/S0360319926004568
- ~~**Paxson, Miki et al., AIAA 2022-4107**~~ — **ACQUISITO 2026-08-13, spostato in TIER 2**
  (`paxson_miki_2022_rdre_nozzle_cfd_optimization.pdf`). Il verdetto non riposa più su un abstract.
  https://arc.aiaa.org/doi/10.2514/6.2022-4107
- **Bigler, Bennewitz, Schumaker, Danczyk, Hargus, AIAA 2019-0197** — open since S21.
  https://arc.aiaa.org/doi/10.2514/6.2019-0197 (unverified DOI, standard AIAA pattern)
- **Fievisohn, Hoke, Schauer, "Quasi-2D Simulations of Nozzled RDEs with the MoC", AIAA 2018-0881** —
  only MoC-native unsteady RDE+nozzle lineage, never extended to design.
  https://arc.aiaa.org/doi/10.2514/6.2018-0881 (unverified DOI, standard AIAA pattern)
- **Sastre et al., Int. J. Num. Meth. Heat & Fluid Flow (2025)** https://doi.org/10.1108/HFF-11-2024-0855

Kraiko school — steady line, plug sub-branch is closest to our F-domain
(Springer DOIs below verified only where a link is given; others: search
https://link.springer.com/journal/10697 "Fluid Dynamics" by volume/page)
- Kraiko & Tillyaeva, "Optimal Profiling of the Supersonic Part of a Plug Nozzle Contour",
  Fluid Dyn. 35(6) (2000). [DOI not pinned]
- Kraiko, Tillyaeva, Baftalovskii, "Optimal Design of Plug Nozzles and Their Thrust Determination at
  Start", J. Propulsion & Power 17(6):1347 (2001). [DOI not pinned — search arc.aiaa.org]
- Kraiko, Pyankov, Tillyaeva, "Profiling the Supersonic Part of a Plug Nozzle with a Nonuniform
  Transonic Flow", Fluid Dyn. 37(5) (2002). [DOI not pinned]
- Kraiko & Tillyaeva, "Contouring spike nozzles and determining the optimal direction of their primary
  flows", Fluid Dyn. 42(2) (2007). [DOI not pinned]
- Kraiko & Tillyaeva, curvilinear sonic line, Fluid Dyn. 47(2) (2012). [DOI not pinned]
- Kraiko, Pyankov, Tillyaeva, two-sided asymmetric planar max-thrust nozzles, Fluid Dyn. 51(1) (2016).
  https://link.springer.com/article/10.1134/S0015462816010142
- Kraiko & Tillyaeva, "Theory of an Ideal Jet Thrust Augmentor", Fluid Dyn. 39 (2004) — cites the
  2002/2003 unsteady pair. https://link.springer.com/article/10.1023/B:FLUI.0000045678.92653.98
- Kraiko et al., skeptical audit of claimed RDE gains, Thermophys. & Aeromech. 29 (2022). [DOI not pinned]
- Tillyaeva, profiling for nonuniform AND swirling inflow, TsAGI 1975 (Russian) — closest classical
  antecedent to our data class. [HARD]

## Verify, do not buy
- **Giles & Pierce, JFM 426:327-345 (2001)** — cited as a verified bank in the 2026-08-12 litmap but
  NOT found in `literature/` or `GENO/literature/`. Locate it; if absent, procure (central to P2/G14).
  Cambridge Core: https://www.cambridge.org/core/journals/journal-of-fluid-mechanics
- **Already on disk, do not re-procure**: `literature/aerospace-12-00502.pdf` = UPM, "Multi-Objective
  Optimization of Rocket-Type Pulse Detonation Engine Nozzles", Aerospace 12(6):502 (2025).
