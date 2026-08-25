# ESA_FINAL_TEXT — dump testuale Presentazione_ESA.pptx (35 slide, salvata 2026-08-24; READ-ONLY probe per TRACE P1)


## slide 1
- Rotating Detonation Engine Activities – T(H)RUST
- Alessandro Montanari, Francesco Nasuti

## slide 2
- 2/22
- Research Roads
- Group Overview
- “Newborn” RDE activity
- About 2 years of active R&D on Rotating Detonation Engines
- Numerical focus
- URANS / low-order in-house modelling of RDEs, oriented to industrially-relevant challenges
- International network
- Joint RDE activities with Purdue University (Prof. Stephen Heister) BEFAST Lab (NC State, Prof. James Braun), RMIT (Quentin Michalski) and ISAE-ENSMA (Prof. Marc Bellenoue)
- HYPERDE
- A hybrid-dimensional CFD modelling framework that solves chamber, injector, plenum and expansion with a consistent low-order formulation
- Open research lines
- Study of hot topics for the RDE community: refill region, supersonic bladeless turbines, disk RDEs, nozzle design (→ dedicated section today), heat flux
- Long heritage on nozzle design
- Participation in ESA-ESTEC ELITE, ARPT, FLPP and different specific GSTP and TRP programs
  [NOTE: 486 ch]

## slide 3
- Detonation compresses by itself: pressure-gain combustion
- 3/22
- •  Near-constant-volume compression: total pressure rise (Pressure Gain) | •  Maximum ideal thermal efficiency, given a certain pre-combustion state
  [NOTE: 789 ch]

## slide 4
- The RDE: a "steady" detonation in a rotating frame
- 4/22
- Annular RDE: rotating front, continuous refill — group figure
- Unwrapped RDE flowfield — Shepherd & Kasahara, GALCIT FM2017.001 (2017)
- •  A detonation front rotates at kHz speed; continuous refill behind it | •  Axial, continuous exhaust — no valves
  [NOTE: 637 ch]

## slide 5
- 2021–2026: detonation leaves the laboratory
- Why RDEs matter today — flights, records, market
- 300 s
- longest continuous RDRE burn — Astrobotic @ NASA Marshall, Apr 2026
- 26 kN × 251 s
- NASA’s full-scale 3D-printed RDRE hot-fire, 2023
- 2021 → 2026
- first RDE in space → duration record, first US flight, 91 M$ raised — lab to industry in five years
- •  JAXA + Nagoya Univ. (Kasahara) → first detonation engine operated in space: 500 N RDE for 6 s (CH₄/O₂) on sounding rocket S-520-31 → Jul 2021; liquid-propellant repeat (ethanol/N₂O) flown Nov 2024. | •  Łukasiewicz–Inst. of Aviation + Warsaw UT (Wolański school) → first rocket flight on a liquid-propellant RDE (propane/N₂O, regeneratively cooled): 3.2 s burn, 450 m → Sep 2021. | •  NASA Marshall (RDRE) → full-scale 3D-printed engine (GRCop-42): 251 s hot-fire at >5,800 lbf (≈26 kN) → 2023 — toward lunar landers and deep-space burns. | •  Venus Aerospace → first US flight of a high-thrust RDRE (2,000 lbf), Spaceport America → May 2025 — then funded to scale: below. | •  Astrobotic + NASA MSFC → record 300 s continuous burn of the Chakram engine (8 hot-fires, >470 s cumulative, >4,000 lbf, hardware intact) → Apr 2026
- Programs & funding — agencies and private capital:   DARPA Gambit → RTX: missile-class air-breathing RDE, ground-test series completed 2025, free-jet flight-weight next  ·  NASA MSFC RDRE program: 2022 hot-fire (In Space/Purdue) → 251 s full-scale 2023 → the Astrobotic record ran on the same stand, 2026  ·  GE Aerospace: RDC dual-mode ramjet 2023, two RDC engines at 3× the airflow of earlier hypersonic demos 2025  ·  Venus Aerospace: 91 M$ Series B — Mercury Fund lead, Lockheed Martin Ventures (Jul 8, 2026).
- 5/22
  [NOTE: 3685 ch]

## slide 6
- 6/29
- 6/22
- Code Development and Capabilities
- HYPERDE  (HYbrid-dimensional PERformance-predictive numerical framework for Rotating Detonation Engines)
- Chamber
- 3D  /  Q2D (unwrapped)
- Fully 3D or “unwrapped” Q2D URANS/Eulerian solver for the annular chamber | 3D Code: https://github.com/open-hydra/MOSE | Q2D Code: https://github.com/open-hydra/Q2D
- Plenum
- 3D  /  Q2D
- Fully 3D (2D for unwrapped) solver for the upstream feed plenum
- Injectors
- 3D  /  Q2D  /  Eulerian quasi-1D
- Quasi-1D solver captures the longitudinal transient response in strongly injector-coupled cases
- Expansion System
- 3D URANS  /  Q2D chamber coupling
- 3D URANS solver coupled with the chamber 3D/Q2D exhaust (choked and unchoked outflows)
- Rationale: each engine subsystem is solved at its most informative dimensionality
  [NOTE: 355 ch]

## slide 7
- 7/29
- 7/22
- Code Development and Capabilities
- General features of the solvers’ suite
- •  Finite volume method
- •  II order in space, up to III order in time
- •  Several turbulence models (easily extendable; strong modularity)
- •  Tabulated thermo properties, thermally perfect gas
- •  Flexible pre-processing tool, full integration with .yaml chemical datasets
- •  Strong CPU and GPU parallelization (OpenMP + MPI, CUDA)
- •  Lots of degrees of freedom on numerics: Riemann solvers, integrated quantities, stiff chemical ODE solver, …
- +
- •  Interface with other in-house solvers (solid, multiphase, real-fluid)
  [NOTE: 341 ch]

## slide 8
- 8/29
- 8/22
- Code Development and Capabilities
- Q2D solver — innovation w.r.t. recent literature |  | •  Rigorous treatment of diffusive fluxes and generic RANS equations | •  General derivation with z = z(x,y) — valid for generic width variations | •  Adaptation to CFD of the non-isentropic BFS boundary condition [1]
- [1]  Fievisohn & Yu, “Steady-state analysis of RDE flowfields with the method of characteristics,” J. Propulsion and Power 33(1), 89–99, 2017.
  [NOTE: 522 ch]

## slide 9
- 9/29
- 9/22
- Code Development and Capabilities
- V&V |  | •  Extensive assessment of HYPERDE features (Q2D source terms, Q1D injectors-chamber, Q2D-3D connection)
  [NOTE: 175 ch]

## slide 10
- 10/29
- 9/22
- Code Development and Capabilities
- V&V |  | •  Extensive assessment of HYPERDE features (Q2D source terms, Q1D injectors-chamber, Q2D-3D connection)
  [NOTE: 175 ch]

## slide 11
- 11/29
- 10/22
- Characterization of Refill Region Dynamics (with RMIT and NCSU)
- How does the geometry affect the refill region expansion process? | What happens if/when expansion yields supersonic Mach number in the layer? | Can the process be modelled? | How does the overall phenomenology impact the stagnation pressure losses?
- Understanding physics of RDE refill regions with diverging inlets | Introduced to mitigate separation losses associated with backward-facing steps | Experimental and numerical evidence instead reports degraded overall performance
  [NOTE: 478 ch]

## slide 12
- 12/29
- 11/22
- Characterization of Refill Region Dynamics
- Inlet line
  [NOTE: 287 ch]

## slide 13
- 13/29
- 12/22
- Characterization of Refill Region Dynamics
  [NOTE: 164 ch]

## slide 14
- 14/29
- 13/22
- Nozzle Design for RDEs
- •  Fully non-isentropic three-waves 2D / 2D-axisymmetric MoC solver developed as an in-house API | •  Primary application: nozzle design for ideal, TIC and optimized configurations | •  Implemented families: ideal (bell, plug, shrouded plug), Rao (optimal bell and plug) and Veen (optimal shrouded plug) |  |  |  |  |  | Open questions (and possible research paths) | •  How does an RDE expansion compare to its steady “equivalent” [2]? | •  Separation dynamics/topology in plug / shrouded plug (effect of rotating oblique shock on incipient separation [3]) | •  Does an “optimal” profile exist for an RDE exhaust?
- Optimized shrouded plug
- [2]  D. P. Stechmann, S. D. Heister, A. J. Harroun, “Rotating detonation engine performance model for rocket applications,” J. Spacecraft and Rockets 56(3), 887–898, 2019. | [3]  A. J. Harroun, S. D. Heister, J. H. Ruf, “Computational and experimental study of nozzle performance for rotating detonation rocket engines,” J. Propulsion and Power 37(5), 660–673, 2021.
- The stakes are real:  +4–7% Isp (choked interface) · 58.1→71.5% of ideal (shroud)
  [NOTE: 1570 ch]

## slide 15
- The RDE exhaust is "periodic" — the literature designs on its time-average
- 14/22
- Nonuniform RDE exhaust — Kaemming & Paxson, AIAA 2018-1101 (Equivalent Available Pressure)
- the literature's accepted average: one equivalent pressure for the whole cycle
- •  The real exhaust rotates at kHz: every flow quantity swings within each cycle. | •  Every published nozzle-design route replaces it with a steady average before designing — the authors of the average themselves caution that naive averaging mis-states performance.
  [NOTE: 1311 ch]

## slide 16
- Rotating Detonation Engine nozzle flowfield
- 15/22
- Transient (left) vs reference steady state (right) — Li, Xu, Lv, Yu, Zhou, Aerosp. Sci. Technol. 158:109878 (2025), Fig. 10
- Instantaneous internal flow — Jourdaine et al., PCI 37 (2019), Fig. 9
- •  Instantaneous: a rotating oblique shock. Time-averaged: a clean axisymmetric plume (but different from the one obtained from the steady-state equivalent stagnation conditions) | •  Fundamental (unexplored) questions: how much the nozzle shape and topology impact the RDE Isp?
- Time-averaged exhaust — Jourdaine et al., PCI 37 (2019), Fig. 4
  [NOTE: 1425 ch]

## slide 17
- Not just pressure — the whole "throat" state varies
- 16/22
- Corrugated sonic line — Kaemming & Paxson, AIAA 2018-1101, Fig. 6
- Every quantity, not just pressure — ibid., Table 1
- •  Across one cycle: total pressure ~4:1, total temperature ~40%, Mach 0.85–1.33 (from literature) | •  The sonic surface is corrugated: subsonic and supersonic bands can coexist (depending on the feed total pressure)
  [NOTE: 2309 ch]

## slide 18
- How RDE nozzles are designed today
- 17/22
- Angelino-type plug on averaged flow — Liu et al. 2022
- Liu et al., Aerosp. Sci. Technol. 120:107300 (2022)
- Classical max-thrust MoC on averaged inflow — Li et al. 2023
- Li, Xu et al., Aerosp. Sci. Technol. 136:108221 (2023)
- Non-optimized conical spike — Jourdaine et al. 2019
- Jourdaine et al., Proc. Combust. Inst. 37:3443 (2019)
- Manual CFD-guided redesign — Paxson & Miki 2022 (NASA)
- Paxson & Miki, AIAA (2022)
- Best of a parametric sweep is not an optimum — and in a systematic literature review, no published work formulates the optimum problem on the real RDE exhaust
  [NOTE: 951 ch]

## slide 19
- Designing on the average solves a different problem
- 18/22
- Literature: average FIRST
- the cycle
- collapse to ONE mean field
- apply steady optimality (Rao / Veen)
- the optimum of a SUBSTITUTE problem
- the error on the argmax (the difference of this optimum and the true optimum)
- Us: formulate the PERIODIC optimum
- the cycle
- per-phase 2D expansion
- cycle-averaged thrust functional
- ITS optimality conditions: averaged transversality & corner
- conditions never written before
- No single phase satisfies its own wall condition — the weighted mean does. The cycle-optimal nozzle is optimal at no single operating point.
  [NOTE: 1595 ch]

## slide 20
- From unsteady periodic to steady per-phase axial MoC expansion
- 19/22
- •  In the declared class (pure rotating wave) the flow is steady in the wave frame | •  The global time average mixes the phases in an exact way |  | Approximation (to be measured): each phase is axially | expanded by a generalized 2D steady MoC
  [NOTE: 1128 ch]

## slide 21
- The per-phase + axial expansion has some recent precedents
- 20/22
- Stechmann et al. 2019 [2]
- Q1D ideal nozzle expansion per phase, averaged thrust — on fixed nozzle families
- Harroun et al. 2021 [3]
- 2D steady axi CFD at cycle pressure ratios, then averaged thrust coefficients — but just as an “evaluation” tool, no optimization
- This project
- the variational optimum on the family — never posed before
- [2]  D. P. Stechmann, S. D. Heister, A. J. Harroun, “Rotating detonation engine performance model for rocket applications,” J. Spacecraft and Rockets 56(3), 887–898, 2019. | [3]  A. J. Harroun, S. D. Heister, J. H. Ruf, “Computational and experimental study of nozzle performance for rotating detonation rocket engines,” J. Propulsion and Power 37(5), 660–673, 2021.
  [NOTE: 1496 ch]

## slide 22
- From theory to a design machine
- 21/22
- •  The objective is one number: J, the cycle-averaged thrust of the optimal wall. | •  The adjoint: one forward + one backward solve → the exact dJ/d(shape) for every wall parameter — trust-region Newton climbs it in seconds.
  [NOTE: 2299 ch]

## slide 23
- A thorough and innovative assessment of nozzle physics and design practice
- 22/22
- First per-phase variational design method for RDE nozzles
- Fast, quick and modern tool to explore the possible design space
- First hierarchical assessment of the error committed by common RDE design nozzle practice
- Our per-phase design vs the classical design at cycle-mean p₀/T₀ |  | Either results (big difference or small gap) could be of foremost importance for the RDE designers
- Strong and modular reducer order CFD infrastructure allowing for URANS assessments
- Possibility to extend it to other functionals (heat flux, pressure gain)
- Comparison with equivalent canonical (deflagrative) expansions |  | Is the real problem (and physics) properly captured by the optimizer?
- 3D exploration of different nozzle topologies and phenomena
  [NOTE: 3727 ch]

## slide 24
- Backup Slides
  [NOTE: 89 ch]

## slide 25
- What is an adjoint — the whole gradient for one extra solve
- •  The objective is one number: J, the cycle-averaged thrust of the optimal wall. | •  To improve a shape we need its slope dJ/d(shape) — for a number of wall parameters. | •  The adjoint: one flow solve + one backward solve → every derivative at once, exact — the gradient a trust-region Newton then climbs.
  [NOTE: 1312 ch]

## slide 26
- Before going where Rao cannot, the machine reproduces Rao
- Variational contour vs classical Rao contour, with deviation panel — in-house, two independent routes
- •  By a route independent of the classical construction, the machine recovers Rao's contour: max deviation ~2·10⁻³ of throat radius. | •  And it is fast: one design segment in 15–20 s; a full validation campaign in 10–14 minutes.
  [NOTE: 1191 ch]

## slide 27
- Code Development and Capabilities
- V&V |  | •  Validation against 1D ZND H2/Air detonation from SDT
  [NOTE: 203 ch]

## slide 28
- Code Development and Capabilities
- V&V |  | •  Validation against “unwrapped” literature test cases [2]
- [2]  D. Schwer and K. Kailasanath, “Feedback into mixture plenums in rotating detonation engines,” 50th AIAA Aerospace Sciences Meeting, 2012.
  [NOTE: 197 ch]

## slide 29
- Code Development and Capabilities
- V&V |  | •  Extensive assessment of HYPERDE features (Q2D source terms, Q1D injectors-chamber, Q2D-3D connection)
- AR = 0.4
  [NOTE: 516 ch]

## slide 30
- Code Development and Capabilities
- V&V |  | •  Extensive assessment of HYPERDE features (Q2D source terms, Q1D injectors-chamber, Q2D-3D connection)
  [NOTE: 254 ch]

## slide 31
- Supersonic Bladeless Turbines (with NCSU)
- CFD based design of NCSU supersonic wind tunnel | Capability up to Mach 4 for steady non-reactive flow | Swappable nozzle and second-throat diffuser system allowing for low feed pressure | Numerical analysis of phenomenology and working principle of bladeless turbines
  [NOTE: 214 ch]

## slide 32
- Supersonic Bladeless Turbines (with NCSU)
- CFD based design of NCSU supersonic wind tunnel | Capability up to Mach 4 for steady non-reactive flow | Swappable nozzle and second-throat diffuser system allowing for low feed pressure | Numerical analysis of phenomenology and working principle of bladeless turbines
- p0 = 3 bar
- p0 = 4 bar
  [NOTE: 148 ch]

## slide 33
- Supersonic Bladeless Turbines (with NCSU)
- Ongoing | Bladeless turbine shape optimization | CFD analysis and design of ejector-diffuser system for RDE testing
  [NOTE: 189 ch]

## slide 34
- Disk RDEs (with RMIT and ISAE-ENSMA)
- Collaboration with PPRIME lab  | CFD lead on design and analysis of disk RDEs operating with H2/Air
- 3D URANS (or Euler)
- Q2D URANS (or Euler)
  [NOTE: 158 ch]

## slide 35
- Real configuration study (with NCSU)
- Numerical rebuilding of the THOR test rig (Purdue University)
  [NOTE: 158 ch]
