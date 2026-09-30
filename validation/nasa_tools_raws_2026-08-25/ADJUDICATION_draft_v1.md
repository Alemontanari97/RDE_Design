# ADJUDICATION DRAFT v1 — NASA nozzle/inlet tools vs rde-nozzle-program phases
(2026-08-31, exploration session; v1 = single-judge draft, UNDER REFUTATION. Sources: the four digests in this folder.)

## Program anchors used
- F6/B-lite: M0 [S-BLITE] lines 3027-3044 (3-D helical space-marching in the wave frame, fitted sheet per station, x-as-time Lax reading = G12-L2, adjoint by Lemma B; brick G12-L1-3D symbolic, never executed); D6:646-655 (Phase-A5 first item), D6:1012 (item 11), D6:1023 (Ransom/Hoffman/Thompson 3-D MOC "to locate").
- F2: D6:160-213 (three-family MoC, thermo on (q;s,h0), adjoint at machine precision, GENO twin + independent invariants).
- F3: D6:214-232 (plug/aerospike, Rao 1961 spike Table-1 oracle C_F=1.5804).
- F5: D6:252-274 (CFD-to-contract pipeline, U3 extraction-surface rule, U3' choking adjudication).
- ANNEX B D6:1133-1157 (input taxonomy, cases A-G).

## Registry facts found AFTER the v1 verbal adjudication (navigation-first repair)
- Rao exit condition sin2θ_E = (p−pa)cotα/(½ρW²) is ALREADY of record: P2_lemmaA L.15 (:238-242), M0:3114 & :3317 (measured 6.6e-02 on 8 nodes), P2_outline:291 (dJ/dy_lip identity). => Rice eq. 6 / code eq. 14 is NOT a new rejector; at most a third-party numeric fixture.
- Control-volume thrust identity (wall-form vs control-surface-form) is ALREADY a declared open finding: findings_registry:1592 ("FREE per-solve integral-identity audit that the engine does not compute"). => NPAC Eq.11≡12≡57 = independent-lineage confirmation + bookkeeping form for an EXISTING open finding, not a new oracle.
- Kliegel-Levine higher-order start line is ALREADY a registered alternative: choice_ledger:285-291; findings:1162 (F4b/F5 lever if the start-line invariance rejector fires); glossary:1271. => repo KLThroat = a concrete (transcription-corrupted) implementation of a known alternative.
- SEARCH-PROVEN ABSENT from docs/: Armstrong AEDC-TR-78-68, Berton TM 105176, NPAC/Barnhart, SUPIN/Slater, Rice 2003, "reference-plane"/"bicharacteristic", "outflow nozzle"/choked-outflow BC device. Domain-of-dependence IS present (L4, Lemma B, brick2_kickoff R-6 :472) — whether it already covers the F5 "reflected-wave validity bound after stream-surface trimming" is TO CHECK.

## Claimed connections (v1 weights, to be refuted)
C-F6-1 [STRONG]: repo 3D_MOC = operational Armstrong-lineage reference-plane inverse-march bicharacteristic scheme; locates the D6:1023 line operationally; Armstrong = acquisition target.
C-F6-2 [STRONG, caution]: 3D_MOC IVS = uniform M=1.1 disc; no axisym-solution hand-off exists; B-lite must price that interface as new work.
C-F6-3 [MEDIUM]: Rice Table 4 (M4 perfect: 4.027/4.051/4.067 mean, 3σ 0.067/0.032/0.019 at 18/36/72 divisions; bias grows with refinement) = quantified KAT for any future 3-D march.
C-F6-4 [MEDIUM]: uniform-field preservation as interpolation-operator rejector (from the documented 9-point TPS failure).
C-F6-5 [CONSTRAINT]: Numerical Recipes sources vendored in repo => never port; clean-room from Armstrong; shipped outputs (~1e-3) = oracle currency.
C-F2-1 [DOWNGRADED to SUPPORT]: NPAC CV identity supports findings:1592.
C-F2-2 [DOWNGRADED to FIXTURE]: Rao exit condition already of record; repo M4RAO/rao.dat + M3.5Perf (eps 6.73651, L/R* 12.5363, CD 0.984756, θB 15.2196°) = independent-lineage fixtures at ~1e-3 class.
C-F2-3 [LOW]: KLThroat as second KL implementation IF findings:1162 lever fires; needs transcription-bug repair first.
C-F2-4 [LOW]: DTHETAB insertion rule / R_down-dominates-convergence as choice-ledger prior art.
C-F5-1 [MEDIUM]: reflected-wave / domain-of-validity bound after stream-surface trimming (STT2001 FindMaxX approximate) = named F5 requirement — UNLESS already covered by L4/R-6.
C-F5-2 [MEDIUM]: SUPIN §13.5 choked outflow-nozzle sub-domain = transplantable CFD mass-flow/back-pressure BC device for F5 verification campaigns.
C-F5-3 [MEDIUM]: NPAC C_FG/C_d/C_V/C_e station bookkeeping = structure for the F5 performance layer; ideal denominators must be re-derived for stratified inflow (ties to Harroun C_F blindness datum, literature_registry:285).
C-F5-4 [LOW]: NPAC mass addition/loss contract (expand-to-local-p, δṁ≪ṁ) as lateral-surface bookkeeping template.
C-F3-1 [MEDIUM]: Berton two-angle divergence λ (TM 105176) as plug/cowl comparator; acquisition target.
C-ARCH-1 [STRONG, architectural]: SUPIN productization pattern (user-overridable closures, .new.in write-back, red-flagged non-functional options, unit-problem mode, sample cases as regression, scheduling not optimizer); NOT a rigor benchmark.
C-ARCH-2 [MEDIUM]: SUPIN NURBS-reparameterization-breaks-shock-cancellation = documented failure mode vindicating "carry the MoC contour itself".
C-HIST-1 [LOW]: repo sponsored as NASA GRC PDE work => citable prior detonation-engine nozzle tooling in P-1.
C-SYS-1 [HORIZON]: SUPIN inlet-side context (cane curve, unstart, isolator buffering) for air-breathing RDE framing; out of current scope.

## Anti-connections (v1)
All four sources: γ=const (SUPIN single-Θ thermally-perfect exists but unused in design), irrotational (SUPIN drops rotationality behind curved shocks; Ferri cited not implemented), no swirl, no adjoint/variational content, no shocks in the nozzle tools, no separation (NPAC). SUPIN empirical loss stack inlet-specific. STT2001 is not a tracer.
