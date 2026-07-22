# Verdict on the internal notes, and the ordered open-problem list (D4)

Status: DELIVERABLE D4 of the 2026-07-16 session. Inputs: line-by-line
mathematical re-verification of the internal notes (D3), code/asset audit
of every internal reference, and the six-strand web-verified survey (D2).
Rule of the session: prefer a counterexample to a weak confirmation;
separate THEOREM / CONJECTURE / HEURISTIC; never promote "not found" to
"does not exist".

b2 GATE — RESOLVED (b2 report landed within the session). All formerly
[b2-GATED] verdicts are now final at query-bounded confidence: b2 found
ZERO hits for family-averaged classical contouring (C1), averaged
Rao-type wall/corner conditions (C2), and the Rao=adjoint identification
(C3); the Kraiko unsteady line is characterized (C4 PARTIAL: variational
bounds — Efremov-Kraiko 2004; instantaneously-adapted nozzle limits —
Kraiko-Egoryan 2018/2020; 1-D piston/expansion processes — 1979 book;
plus Levin-Manuilovich-Markov 2010 PDE duct optimization by DIRECT
search). Residual due diligence before print (downgraded from gate):
human pass on Kraiko 1979 book (TOC unverified) and PMM archives.
Bibliographic corrections delivered by b2, to propagate: Rao's TOP paper
is ARS J. 30(6):561 (1960), not 1961; "Rao 1961" = the SPIKE paper,
Planet. Space Sci. 4:92-101; the "Eq. 14" label is UNVERIFIED against
the 1958 original (structure confirmed via NASA TM-103175; cite the
condition, not the equation number — GENO CLAUDE.md reference-honesty
rule applies); Sternin's books are two-phase nozzle gasdynamics — the
general Russian nozzle textbook is Pirumov-Roslyakov (1990); λ₃ is the
LENGTH multiplier (f₃ = cot φ).

------------------------------------------------------------------------------
## 1. Claim-by-claim verdict on `docs/cycle_averaged_variational_nozzle.md`

| Claim | Verdict | Action |
|---|---|---|
| Weighting lemma (Isp ≡ J at choked matched feed) | SURVIVES (verified; = D3 O1) | add the coupling caveat: equivalence DIES in the bilevel setting (D3 N-O1±) |
| T0 (wave-frame exactness) | SURVIVES and STRENGTHENED: instantaneous thrust is CONSTANT, not merely mean-equal (D3 §2) | adopt strengthened statement; add mode-purity diagnostic |
| "Rao applies verbatim in 3-D" (T0 consequence) | FALLS as phrased — OVERCLAIM | weaken to: T0 steadifies the problem; 3-D swirling variational theory is open (N6) |
| T1 (factorization) labeled "Theorem" | WEAKENED: it is a DEFINITION + the P4 convergence CONJECTURE | relabel; adopt the sharpened D1 ⊃ D2 parameter structure (D1 §8) |
| T2 (averaged stationarity system) | SURVIVES as SCHEMA, with one CORRECTION: averaged transversality must be the weighted (**') not the unweighted (**) | any implementation (WP2/WP3, `raocore` modification) MUST implement (**'); (**) is exact only in the T3 class |
| T3 (collapse theorem) | SURVIVES — proof re-verified; SHARPENED (Lemma A holds across transversal shocks and for γ(T)) | none; T3 is the strongest single result of the notes |
| T3 novelty ("not published") | SURVIVES query-bounded (D2 G2: only empirical echoes + stochastic-control certainty equivalence; b2 confirms zero hits on averaged optimality conditions) | cite Dambrine-Dapogny-Harbrecht 2015 and certainty-equivalence as nearest relatives when publishing |
| §5.1b measured γ-channel numbers (1.154→1.210; ε* −1.9%; Isp −0.001%) | RESOLVED 2026-07-16 (A0.3): re-derived in-repo — `examples/gamma_cycle_probe.py` + `tests/test_gamma_probe.py` + `data/gamma_cycle_probe.json`. γ_s 1.1537→1.2093 CONFIRMED (to the stale note's own rounding); ε* shift CORRECTED to −0.56% (stale −1.9% STRUCK; unweighted-mean closure reproduces −2.39% — the likely wrong-averaging source, now rejected by test); Isp penalty CORRECTED to −0.00028% (second order confirmed: penalty ≤ shift²); γ_eff = ⟨Pcγ⟩/⟨Pc⟩ closure gets its first executable confirmation (−0.57% vs −0.56%) | numbers of record now in D3 §5.2; cite only those |
| T4 (plug at peak) | SURVIVES as THEOREM* (closure-conditional); nesting argument verified. b2 addendum: the ideal-adaptation CLOSURE has published precedent as a detonation-cycle performance BOUND (Kraiko-Egoryan 2018/2020) — the shape-level nested-argmax theorem remains unfound | cite Kraiko-Egoryan next to the closure; keep the caveat prominent; the off-design plug march is what retires it |
| N1-N6 channel taxonomy | SURVIVES with the D1§8 restructuring (D1 ⊃ D2; N5 governs) | update note |
| Measure remark (log-uniform) | SURVIVES (trivially verified, D3 O2) | none |
| Corollary 2 (altitude-averaging duality) | SURVIVES; survey adds: the altitude collapse is unpublished folklore (D2 G15) — the duality is itself publishable | fold into the T3 paper |
| Corollary 3 / oracle culture | SURVIVES; survey confirms adjoint-consistency trap is a theorem (Giles-Ulbrich 2010) | none |
| Claim map "Rung 3a NEW" | SURVIVES query-bounded, with mandatory prior-art citations: spiral-wave response functions (Biktasheva 2009/2010), freezing (Beyn-Thümmler) — precedent exists for the OBJECT, not the shape-design use | cite; phrase as "first application to shape design in gas dynamics" |
| Claim map "Rung 3b HB-adjoint on RDE NEW application" | SURVIVES (D2 G8 clean) | note frequency-imposed vs unknown-Ω distinction (b4): the RDE case needs the LCO-style unknown-period treatment, not plain forced-response HB |
| Claim map "Rung 2 all NEW" | SURVIVES query-bounded — b2 landed: the per-phase brick exists at full generality (Kraiko 1982/1994/2002/2007, all verified), the averaged wall/corner system does not; the closest artifacts are Efremov-Kraiko 2004 (bound, not shared wall) and Levin-Manuilovich-Markov 2010 (direct search, no optimality system) | mandatory citations: the four Kraiko papers, Efremov-Kraiko 2004, Levin et al. 2010 |
| Claim map "Bridge 2↔3 O(St) NEW" | SURVIVES sharpened (D2 G10): linear O(He) correctors exist for reflection coefficients; nonlinear COMPACT map exists (Huet-Giauque) — what is new is the corrector FOR THE THRUST FUNCTIONAL at finite amplitude | reframe P4 as the two-direction extension (D2 §b6 closing) |
| Claim map "Coupling (b) response map NEW" | SURVIVES query-bounded | none |
| "Mo, Huang" citation | FALLS — bibliographic conflation | replace with: Mo et al. Acta Astronautica 108:92 (2015) [scramjet, nonuniform-inflow MOC]; Li-Xu-Huang JPP 38:849 (2022) [RDE, MOC on time-averaged state] |
| S-H paper title as cited | MINOR FIX: actual title "Rotating Detonation Engine Performance Model for Rocket Applications", JSR 56(3):887-898 | fix in all docs |

## 2. Claim-by-claim verdict on `docs/mathematical_foundations_rde_nozzle.md`

| Claim | Verdict | Action |
|---|---|---|
| Solution-concept trichotomy S1/S2/S3, convex-integration non-uniqueness | SURVIVES; all key references verified (D2 §b3) | none |
| "Optimization constrained by statistical solutions = virgin territory" | SURVIVES (D2 G13) | none |
| Transonic-degeneracy confinement strategy | SURVIVES; supported by Giles-Pierce sonic-throat log singularity (published evidence the degeneracy is real in the adjoint) | cite JFM 426:327 |
| §2 "ergodic average over an attractor; intersection essentially unpopulated" | SURVIVES query-bounded | none |
| P1 statement (a)-(c) | SURVIVES as SCHEMA | none |
| P1 corollary "design sensitivity well-posed ⟺ spectrally robust" | FALLS as a biconditional — corrected to P1a/P1b (D3 §7): IFT needs only spectral NON-DEGENERACY at 0; instability does not destroy sensitivity, it destroys its physical license | rewrite; the corrected version is still novel (D2 G9) and still the organizing structural fact |
| P2 "folklore-adjacent, never written down" | WEAKENED and SHARPENED: quasi-1D adjoints PUBLISHED (Giles-Pierce JFM 2001); 2-D supersonic ANALYTIC adjoints with characteristic structure PUBLISHED (Lozano-Ponsin, Aerospace 12(6):494 (2025) — the resolved "MDPI 2025 hit"), with NO mention of Rao/Guderley/Kraiko: both banks of the bridge exist, the bridge does not | rewrite P2 as the identification lemma anchored on Giles-Pierce (1-D) and Lozano-Ponsin (2-D) |
| P3-P7 | SURVIVE as SCHEMA/targets; P7 confirmed novel even restricted (D2 G17); P6's "first measured instance" is now IN-REPO (A0.3 closed: shift −0.56%, penalty −0.00028% ≤ shift²) | P6: cite the D3 §5.2 numbers of record |
| §8 placement claim (six-field intersection, empty center) | SURVIVES query-bounded, now with a verified populated-edges map (D2 §7) | none |
| Newton-problem symmetry-breaking cautionary tale | SURVIVES, references verified (Brock-Ferone-Kawohl 1996; Lachand-Robert-Peletier 2001; Lachand-Robert-Oudet 2005) | none |
| Wasserstein-DRO as "SOTA frame" suggestion | SURVIVES with attribution duty: DRO shape optimization EXISTS (Dapogny et al. 2023; Chen-Gauger CMAME 2024) — method known, RDE application new | cite when used |

## 3. Verdict on `docs/roadmap_geno_rde.md`

The roadmap survives structurally (the rung-2 critical path, oracle-first
gating, the G2 value gate). Three amendments required:
 (i)   WP2c/WP3: implement the WEIGHTED transversality (**') — the
       unweighted average is only T3-class exact (D3 §4c). The §2bis
       "Level A" scope statement is CONFIRMED and now has its precise
       license: Level A = the class where w(ξ) is phase-independent.
 (ii)  WP0 problem book: DONE this session (D1); the hypothesis ledger
       supersedes the draft ledger sketch.
 (iii) WP8 Paper-1 scope: add the mandatory prior-art citations (spiral-
       wave RFs; freezing; Giles-Pierce; Huet-Giauque; Stow/Goh
       correctors; Dapogny/Chen DRO; certainty equivalence) and the b2
       publication gate below.

PUBLICATION GATE — RESOLVED to DUE DILIGENCE: (a) the b2 final report
LANDED (C1/C2/C3 zero hits; C4 characterized: bounds and 1-D processes,
never a shared-contour measure-averaged optimality system); (b) residual
item, downgraded from gate to pre-print due diligence: a human pass over
Kraiko's 1979 monograph (TOC unverified online) and the PMM archives.
Contingency unchanged: if that pass surfaces a shared-contour averaged
system, the program's novelty restates as the RDE instantiation + T0
exactness + the T3/T4 dichotomy + the O(St) bridge — still a paper,
smaller claim.

ADJUDICATION ADDENDUM (2026-07-22, S13): the Kraiko-Osipov PMM 34(6)
1970 contingency (armed via the S7 PMM sweep; wired into P-1 §4.5) is
RESOLVED in containment mode — full text read; trajectory-averaged
weighted variational contouring with characteristic multiplier fields
and an averaged-weight collapse case CONFIRMED; P-1 §4.5 reworded to
the pre-planned containment statement with mandatory citation; M0
T3-C2/T7 precedent notes added; P-2 novelty (adjoint bridge)
UNAFFECTED. Record: D2 adjudication row + S13 log.

## 3bis. Verdict on the GENO variational corpus (per-nozzle methods)

Read in full: `GENO/docs/theory_variational_understanding.md` (19-agent
page-verified synthesis vs the primary PDFs in `GENO/literature/`),
`theory_variational_optimization.md`, `toc_constraint_combinations.md`,
`variable_gamma_generalization.md`. Verdict and consequences for the
program (full inventory now in D2 §b0):

| Item | Verdict | Consequence |
|---|---|---|
| Rao 1958 "Eq. [14] p.379" corner label | VERIFIED in-house against `RAO.pdf` (page-level, multi-agent read) | closes the b2 UNVERIFIED item; equation numbers citable |
| Two-multiplier doctrine (λ₂ mass + λ₃ length; p_a/p_b ONLY via endpoint transversality) | VERIFIED against five primary sources | the averaged system (**') inherits exactly this structure; T3 remark (R2) doubly confirmed |
| TOC bell (type 2) per-phase brick | MATCH theory=code (2 DOF, 2 bisections, mass by curve termination) | rung-2 fixed-wall brick READY |
| TOP (4), conical (3), Angelino plug (5) | MATCH (non-variational or documented approximation) | usable as contour families / closures |
| RaoPlug (type 8) | STRUCTURAL BUGS S1/S2 confirmed: mass multiplier NOT enforced, 1 DOF of 2 | the free-boundary per-phase brick is INCOMPLETE — PB-2 (truncated plug, OP-2) is BLOCKED on the S1/S2 fix, as the roadmap already states; priority raised by this session's ranking |
| Veen (type 7) | PARTIAL (S4 mass over-imposed, S5 base-pressure loop dropped, S6 coupled modes) | PB-3 (duty split, OP-8) blocked on S4/S5 |
| Hoffman 1967 multiplier fields + E-residual (Eq. 78) | page-verified in-house | P2 gains its classical bank (D3 §8 updated); Level-C certificate has a 1967 ancestor; for finite-rate gas the closed-form corner is PROVEN dead → N4 ladder restructured (D3 §5.2) |
| Sternin 1962 / Rao-Beck 1994 valid-region boundary | verified; implemented γ-free as `boundaryfunction_solve` | P7's failure-boundary monitor already exists in code (D3 §9 updated) |
| E4 risk (corner bijection for γ(T): asserted, never validated on known answer) | OPEN, honestly documented in-house | new ledger row H-E4 (D1 §9); the only known-answer var-γ oracle is Scofield-Hoffman 1971 Table 2 (frozen 2290 lbf) = GENO gate G2 — ALSO the natural contour-level N4 oracle for rung 2 |
| Constraint-pair equivalence map (TOC) | formally derived + code-verified; only {eps,L} CTest-covered | the averaged designer should keep {eps,L} as canonical pair; MF-pairs/inner=none pathologies (C-B1/C-B2) must be gated before ensemble sweeps |

Net effect on the open-problem ranking (§5): OP-2's critical path now
explicitly includes the RaoPlug S1/S2 fix + Rao 1961-spike Table-1
oracle (M_E=2.4, θ_E=−8.25°, γ=1.23 → ε=3.81, X_D/R_E=1.164, C_F=1.58)
before any averaged-plug computation; OP-7 gains the Hoffman bank and
the E-residual falsifier.

## 4. Session's own negative results (things we tried to break and could not)

- T3 proof: attacked at the shock-jump level (RH homogeneity) and the
  γ(T) level — holds (indeed extends) at the first, dies exactly where
  claimed at the second. The dichotomy line is drawn correctly.
- T0: attacked via frame-change bookkeeping (w vs u in the flux) and
  Coriolis/centrifugal axial components — closes exactly; the proof is
  robust and elementary.
- Weighting lemma: attacked via c*(t) time dependence — the ṁc* = PcA_t
  cancellation is algebraic and law-independent. Holds.
- Leibniz across topology switches: attacked via Σ-dependent switch
  locations — continuity of F at the switch kills the boundary terms.
  Holds.

## 5. The ordered open-problem list (the scientific contribution, ranked)

Ranking criterion: (novelty confidence after D2) × (feasibility with
in-house tools) × (load-bearing-ness for the program).

1. OP-1 [T3/T4 papers-grade formalization + oracles]. The collapse
   dichotomy with the verified proofs (D3 §5-6), the altitude-duality
   corollary, and the executable oracles O1/O2. Novelty: G2/G3 clean
   (b2 confirmed). Feasibility: exists (this session + repo tests). The
   null-result explains the entire "design-on-time-averaged-flow"
   practice of b1 — a citable clarification the field lacks.
2. OP-2 [PB-2: the truncated plug]. First genuinely averaged optimum;
   direct benchmark exists (Paxson AIAA 2022-4107, parametric). Needs:
   plug off-design march (WP1c-i, the known numerics risk) + (**').
3. OP-3 [P4: the O(St) thrust corrector]. Two-direction extension of
   published results (Huet-Giauque amplitude-wise; Stow/Goh
   frequency-wise), for the thrust functional, validated on Cooper-
   Shepherd-type unsteady/quasi-steady competition data. Novelty G10
   clean. This is the program's LICENSE result (St = O(0.1-1)).
4. OP-4 [P3 + (**'): the averaged optimality system, rigorously]. The
   function-valued multiplier + weighted transversality on restricted
   classes; quasi-1D anchor: Cliff-Heinkenschloss-Shenoy; per-phase
   brick at full generality: Kraiko 1994/2002 (b2 verified).
5. OP-5 [P1a/P1b on the reduced model]. Freezing-adjoint sensitivity of
   a rotating detonation relative equilibrium with dΩ_w/dΣ, on the 2-D
   unrolled annulus; the corrected sensitivity/stability statement.
   Novelty G7/G9. Prior art to cite: Biktasheva RFs, Beyn-Thümmler.
6. OP-6 [P7 existence]. Measure-family existence in uniform
   C^{1,α} ∩ S1 classes; novel even restricted (G17); failure boundary =
   loss of MOC-regularity: a checkable mechanism.
7. OP-7 [P2 bridge lemma, 2-D]. Rao/Kraiko conditions = closed-form
   adjoint characteristics; anchored on Giles-Pierce (quasi-1D) and
   Lozano-Ponsin 2025 (2-D analytic adjoint, no Rao link — the bridge
   confirmed missing by b2). Partly expository, high unification value,
   now time-sensitive: the 2-D bank was built in 2025 by others.
8. OP-8 [PB-3: shrouded duty split]. The C1 conjecture as a tool mode;
   engineering payoff highest, dependent on OP-2 machinery.
9. OP-9 [PB-5: mode-measure robust design]. CVaR/DRO with existing
   method literature (cite Dapogny/Chen/Kouri-Surowiec), calibrated on
   operability maps; novelty is the application + the mode-discontinuity
   honesty (G16).
10. OP-10 [G11 hard mathematics]. O(1)-amplitude time-homogenization of
    Euler with oscillating inflow — the far frontier; keep as declared
    open problem feeding P4's hypotheses, not as a dependency.

Items 1-3 are self-contained and publishable from this repo's toolchain;
4-7 constitute the mathematics paper(s); 8-10 are the program's horizon.

Second-pass addenda (D3 §10bis, adversarial self-review of the method):
 OP-0  [Proposition B1: the bound ladder]. Upper bounds by relaxation
       (shared-wall relaxation ∫max; ideal-adaptation/integral-flux
       bounds à la Efremov-Kraiko) reported with every optimum; the
       relaxation gap = theorem-grade channel-value estimate, upgrading
       gate G2. Cheapest item on the whole list; do it FIRST.
 OP-3' [P4 as Γ-convergence]. The quasi-steady license restated so that
       MAXIMIZERS converge, not just values (epi-convergence on the P7
       compact class). Strictly stronger than OP-3's expansion.
 Level-C addition: DWR (dual-weighted residual) discretization error
       bars on J — adjoints already available, near-zero marginal cost.
 Optional mathematics: computer-assisted existence of the spinning wave
       on the reduced model (discharges P1's standing hypothesis).
 OP-11 [the phase diagram: "the measure selects the topology"] (D3
       §10quater). Configuration-free formulation over A_gen (solid set
       in an envelope; sectors = topologies; total optimum = finite
       tournament); geometry-free ceiling J_ideal (Prop. G-B) attained
       by the free-boundary family at generous constraints (Cor. G-T4 =
       global-over-topologies optimality, mechanism M1); the general
       design question becomes the map of the optimal topology over
       (constraints) × (spread of μ). PB-2/PB-3 reclassified as
       SECTIONS of this diagram. Quasi-1D diagram traceable NOW from
       the S-H closed forms on Table-1 states.
       [ε-LEVEL INSTANCE DONE 2026-07-16, [F1/OP-11-eps]:
       src/thrust/phase_diagram.py + tests/test_phase_diagram.py +
       data/phase_diagram.{json,md} + figs/phase_diagram_op11.png.
       Two THEOREM-grade additions of record (full statement D3
       §10quater): capped-closure plug dominance (no strict bell region
       at ε level) and M1 gap-zero attainment extended to SUBCRITICAL
       cycles via the sonic-capped closure; published S-H closure's
       naive branch inverts the ranking at ε_max = 1 (test-rejected
       artifact). Contour-level OP-11 (duty split) remains OPEN.]

## 6. Immediate repo actions (mechanical, this week)

1. Fix "Mo, Huang" → Mo et al. (2015) + Li-Xu-Huang (2022) in
   `cycle_averaged_variational_nozzle.md` (§b1 correction).
2. Fix the S-H title everywhere it is cited informally.
3. Re-derive or strike the §5.1b numbers; if re-derived, commit the
   probe script + a test (repo no-unverifiable-numbers culture).
   [DONE 2026-07-16: examples/gamma_cycle_probe.py, tests/test_gamma_probe.py,
   data/gamma_cycle_probe.json; γ confirmed, ε* shift corrected to −0.56%,
   penalty corrected to −0.00028%; see D3 §5.2 and §1 row above.]
4. Patch the notes: T1 relabel, (**)→(**'), P1 biconditional →
   P1a/P1b, "verbatim 3-D" weakening — or mark the two notes as
   superseded by D1/D3 (chosen route: supersession notice added at top
   of each, content kept as historical record).
5. Add the b2-gate marker to the roadmap WP8 (done in D4 §3; mirror it
   in `roadmap_geno_rde.md` when next edited).
