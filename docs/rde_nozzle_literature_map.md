# Literature map and gap analysis: the cycle-averaged RDE nozzle problem (D2)

Status: DELIVERABLE D2 of the 2026-07-16 session. Six survey strands
(b1-b6), each executed as an independent web-verified search with the
discipline: every reference verified at the stated level (DOI/venue
fetched where possible); UNVERIFIED items flagged; every negative verdict
is "NOT FOUND under the listed queries", never "does not exist". The full
query lists and per-strand unverified-item ledgers are preserved in the
session transcripts; this map keeps the load-bearing content.

Verdict legend: FOUND / PARTIAL / NOT-FOUND(q) — the (q) reminds the
reader the claim is query-bounded.

------------------------------------------------------------------------------
## 0. Executive gap summary (the one-table version)

| # | Candidate novelty (internal notes) | Verdict | Nearest prior art |
|---|---|---|---|
| G1 | Cycle/phase-averaged SHAPE-FUNCTIONAL variational formulation of the RDE nozzle (T1/T2 system) | NOT-FOUND(q) | Paxson et al. AIAA 2022-4107 (2-param CFD opt of shrouded plug); Gonzalez-Viana 2025, Ornano 2017 (evolutionary PDE-nozzle opt) |
| G2 | Collapse theorem T3 (fixed wall → Rao at ⟨Pc⟩) | NOT-FOUND(q) | Empirical echoes: Harroun 2021 "near-perfect time-averaged expansion"; Liu et al. 2021 design axiom; certainty-equivalence analogues in stochastic control |
| G3 | Plug-at-peak theorem T4 (simultaneous per-phase optimality) | NOT-FOUND(q) as theorem; the ideal-adaptation CLOSURE has precedent as a performance BOUND | Qualitative altitude-compensation rationale (Harroun 2019; Liu 2021/22); Kraiko-Egoryan 2018/2020 instantaneously-adapted nozzle bounds for detonation cycles |
| G4 | Truncated/shrouded plug as genuinely averaged shape problem (PB-2/PB-3) | PARTIAL | Paxson et al. 2022: cycle-aware but parametric (2 DOF), no functional/optimality system |
| G5 | MOC design against a phase-FAMILY of inflow states, one shared contour | NOT-FOUND(q) | All published MOC RDE designs average first, design second (Li-Xu-Huang 2022; Liu 2021) |
| G6 | Averaged-Rao optimality system (function-valued multiplier, averaged wall/corner conditions) | NOT-FOUND(q) — b2 LANDED: zero hits; Kraiko unsteady line characterized (bounds and 1-D processes, never shared-wall averaging) | Efremov-Kraiko 2004 (steady-equivalent bound); Levin-Manuilovich-Markov 2010 (PDE duct, direct search); Kraiko 1979 book TOC unverified (residual due-diligence item) |
| G7 | Shape adjoint of a rotating relative equilibrium, unknown Ω(Σ) | NOT-FOUND(q) | STRONG methodological precedents: spiral-wave response functions (Biktasheva 2009/2010); freezing method (Beyn-Thümmler 2004); HB adjoints w/ imposed frequency |
| G8 | HB adjoint applied to detonation engines / combustor shape design | NOT-FOUND(q) | Turbomachinery HB-adjoint SOTA (Duta-Giles 2002 → Thress 2022) |
| G9 | "Sensitivity well-posedness ⟷ spectral non-degeneracy" stated for wave design | NOT-FOUND(q) (corrected form P1a/P1b in D3 §7) | Ingredients standard (Evans function; shadowing-conditioning); no explicit theorem |
| G10 | O(St) mean-thrust expansion with transfer-function corrector (P4) | NOT-FOUND(q) | O(He) correctors exist for REFLECTION coefficients (Stow-Dowling-Hynes; Goh-Morgans); nonlinear COMPACT map exists (Huet-Giauque 2013) |
| G11 | Rigorous time-homogenization of Euler w/ oscillating inflow BC | NOT-FOUND(q) as O(1)-amplitude; PARTIAL scaffold | Weakly nonlinear geometric optics for oscillating BVP data (Coulombel-Guès-Williams 2011/14; Kilque 2022, incl. 2-D Euler) |
| G12 | Multi-D rigorous shape derivative for thrust functional with shocks | NOT-FOUND(q) | 1-D complete (Bressan-Marson; Ulbrich); quasi-1D design rigor (Cliff-Heinkenschloss-Shenoy 1997); 2-D practice (Baeza et al. 2009) |
| G13 | Optimization constrained by statistical/measure-valued Euler solutions | NOT-FOUND(q) | Forward theory only (Fjordholm et al.) |
| G14 | Rao = adjoint (P2) | PARTIAL — three banks published, no bridge: Hoffman 1967 multiplier FIELDS on characteristics (classical side, in-house corpus §b0); Giles-Pierce 2001 (quasi-1D analytic adjoint); Lozano-Ponsin 2025 (2-D analytic adjoint, no Rao/Kraiko mention) | P2 narrows to the explicit identification + reverse-AD = adjoint characteristic sweep |
| G15 | Trajectory-averaged (altitude) nozzle contour design as variational problem; "affine collapse" folklore | NOT-FOUND(q) as theorem | Dual-bell literature = parametric sweeps + trajectory codes (Frey-Hagemann 1999; Stark-Génin/Ariane5 2016); Sutton folklore; certainty equivalence (stochastic control) |
| G16 | Mode multistability via mode-measure/CVaR/DRO | NOT-FOUND(q) for RDE | CVaR-PDE (Kouri-Surowiec 2016); Wasserstein-DRO shape opt EXISTS (Dapogny et al. 2023; Chen-Gauger 2024) — method known, application new |
| G17 | Existence for shape opt of an integral over a μ-family of hyperbolic states, shared boundary (P7) | NOT-FOUND(q) | Elliptic-state analogues only (Conti et al. 2009; Dambrine et al. 2015) |

Overall: the DIAGONAL claim of the internal notes — that the intersection
"averaged variational nozzle theory × RDE" is unpopulated — SURVIVES on
five strands, with G6 (Kraiko school, b2) still pending and flagged by
two independent strands (b2 interrupted-then-resumed; b5 explicitly named
Kraiko "the highest-risk blind spot for C1... check before claiming
novelty in print"). No novelty claim should be published before the b2
verdict lands; see D4 §3.

------------------------------------------------------------------------------
## b1 — RDE performance models and RDE/PDE nozzle design

State of the art. 0-D/reduced-order performance models: Stechmann-
Heister-Harroun, "Rotating Detonation Engine Performance Model for Rocket
Applications", JSR 56(3):887-898 (2019), doi:10.2514/1.A34313 [VERIFIED at
title/venue level; equation-level content paywalled — the repo's own 18/18
Table-1 reproduction is the strongest available verification of the
internal mechanics]; Kaemming-Fotia-Hoke-Schauer JPP 33:1170 (2017)
reduced-order thermodynamic model + EAP pressure-gain metric; Paxson-
Perkins AIAA 2021-0192 sizing model; Fievisohn-Yu JPP 33:89 (2017)
MOC combustor flowfield; Shepherd-Kasahara GALCIT FM2017.001 control-
volume thrust models. Experiments: Fotia et al. JPP 32:674 (2016); the
Nagoya/Keio/JAXA line (Goto, Kawasaki, Kasahara) through the S-520-31
flight demonstration (JSR, doi:10.2514/1.A35401, aerospike RDE, Isp
290±18 s); multi-facility RDRE standardization (Bennewitz et al., Sci.
Rep. 2023, doi:10.1038/s41598-023-40156-y).

Nozzle design/optimization: Harroun-Heister-Ruf JPP 37(5) (2021),
doi:10.2514/1.B38244 (aerospikes + blunt body; performance driver =
near-perfect TIME-AVERAGED expansion) + AIAA 2019-0197; Paxson-Miki-
Perkins-Yungster AIAA 2022-4107 (shrouded TRUNCATED plug, 2-parameter CFD
optimization, 58.1%→70.0% of a "notional ideal shape-shifting nozzle"
bound; notes the choked chamber exit decouples cycle from nozzle);
Li-Xu-Huang JPP 38(5):849-865 (2022), doi:10.2514/1.B38539 (MOC +
maximum-thrust theory on a time-averaged exit state; +11.3%/27.6% axial
thrust/Isp vs partial nozzles); Liu-Cheng-Zhang-Wang AST 120:107300
(2022) (aerospike design for annular RDE; states the field's design
axiom verbatim: time-averaged quantities are "reasonable" for design).
BIBLIOGRAPHIC CORRECTION to the internal notes: "Mo, Huang" conflates
two distinct NUAA items — Mo-Xu-Quan-Yu-Lv, Acta Astronautica 108:92
(2015) is nonuniform-inflow MOC for a SCRAMJET; the RDE nozzle paper is
Li-Xu-Huang above.

PDE (pulse-detonation) precedent — the periodic-inflow nozzle question is
OLDER than the RDE: Cambier-Tegnér JPP (doi:10.2514/2.5305) single- vs
multi-cycle nozzle optimization diverge; Morris JPP 21:527 (2005) MOC
without quasi-steady-nozzle assumption; Owens-Hanson JPP 23:325 (2007)
single-cycle unsteady nozzle phenomena; Cooper & Shepherd, "Single-Cycle
Impulse from Detonation Tubes with Nozzles", JPP 24(1):81-87 (2008),
doi:10.2514/1.30192 [PAGE-VERIFIED 2026-07-22, S13]: +72%/+43%
CONFIRMED verbatim (abstract) — both vs the plain-tube baseline for
the largest nozzle (12 deg, 0.6 m, area ratio 16.7): +72% at P0 =
100 kPa where UNSTEADY nozzle-air tamper effects dominate (Gurney/
partial-fill model — no unsteady CFD in the paper), +43% at 1.4 kPa
where the nozzle quasi-steadily expands from the AVERAGE upstream
pressure; nozzle-dependent transition pressure (5.2 kPa for the
largest); nozzle startup 6-12% of cycle time — directly relevant to
N5/P4 expectations.
KRAIKO-OSIPOV ADJUDICATION (2026-07-22, S13; full text READ,
literature/0021-8928(70)90164-4.pdf, JAMM pp. 1005-1013): the 1970
paper IS a trajectory-averaged variational contouring problem for a
single shared contour — time-integrated WEIGHTED wall condition
(their (3.2), weight W(t) = lambda2 k/m from the trajectory
adjoint), multiplier FIELDS on flow characteristics with transport
and jump relations ((3.6)-(3.10)), quasi-stationary approximation
declared (validity footnote, unpriced), and a §4 COLLAPSE CASE:
invariant dimensionless inlet (nozzle starting at its throat) =>
reduction to the CLASSICAL optimum family with time-AVERAGED weight
W-degree. CONTAINMENT (per the pre-armed plan): our formulation
contains K-O as the trajectory instance of the general measure (the
altitude-duality corollary T3-C2 is the bridge); beyond it: cycle
measure + exact steadification (T0), PRICED quasi-steady step (P4
answers their footnote), sharpened collapse with proven boundary,
RDE physics, EOS-general executables, bounds/(S*, delta), topology-
as-output, and the modern-adjoint bridge (P-2 unaffected; their
native multiplier fields are additional bank-B1 material).
MANDATORY CITATION in P-1/P-2. Lozano 2018 (AIAA J 56(11), singular/
discontinuous adjoint solutions) and Lozano-Ponsin Aerospace
12(6):494 (2025) now ALSO uploaded — page-verification queued (S13
continuation). Modern black-box shape
optimization under detonation pulses: Ornano-Braun-Saracoglu-Paniagua,
Adv. Mech. Eng. 2017 (doi:10.1177/1687814017690955); Gonzalez-Viana et
al., Aerospace 12(6):502 (2025) (doi:10.3390/aerospace12060502), which
states explicitly that classical steady nozzle-optimization criteria are
INVALID for detonation exhaust — the field knows the problem, and answers
it numerically, never variationally.
[FULL-TEXT READ 2026-07-21 (S12; PDF in
literature/aerospace-12-00502.pdf): Gonzalez-Viana-Sastre-Martin-
Velazquez, Aerospace 12:502 (2025), doi:10.3390/aerospace12060502 —
single-cycle H2-air PDE (tube 1 m + Con-Di), quasi-1D unsteady
reactive Euler (OpenFOAM rhoReactingCentralFoam variant, one-step
kinetics, CJ vs CEA 1.5-3%), 5 design variables, 13,860 cases +
HOSVD surrogate + GA/gradient, five objective mixes (I_SPF, I_T,
A_N). FINDINGS: optimum always divergent with SMALL ratio (A9/A8 =
1.13-1.31 of 15 available), length bound ACTIVE; time-averaged exit
pressure at optimum 1.4-2.1 bar >> Pa (their Fig. 8) — "the unsteady
character disallows conventional steady-state nozzle flow theory".
ATTRIBUTION OF RECORD (three-way, S12): constraint effects
(classical) + MEASURE effects (rung-2 reproduces the qualitative
optimum: tail-dominated mu + sonic cap + weighted (**') — benchmark
row in D6 Phase A2) + genuinely unsteady start-stop residue (O5
anchor; maximal in single-cycle PDE, absent in continuous-rotation
RDE — T3-QS explains the severity ranking). Their "steady invalid"
convicts the NAIVE reading that our T7/(**') already rejects by
theorem; the averaged theory survives and prices the rest.]
PENDING ACQUISITIONS REGISTER (S12; upload target literature/, then
page-verify): Kraiko-Osipov PMM 34(6) 1970 [PRIORITY 1 — P-1
contingency]; Giles-Ulbrich SINUM 48:882 and 905 (2010) and Lozano
AIAA J 57(9) 2019 [P-2 cites — verify the "near the shock"
divergence locus vs stagnation-streamline]; Cooper-Shepherd JPP
24(1):81-87 (2008) [year of this identification TO-VERIFY vs the
"JPP ~2008 UNVERIFIED" row above]; Owens-Hanson JPP 23(2):325-337
(2007); Morris JPP 21(3):527-538 (2005).

What b1 does NOT contain (all NOT-FOUND(q)): the shape-functional
formulation (G1); the collapse theorem (G2); peak-design optimality proof
for plugs (G3); MOC on a phase family (G5). PARTIAL: cycle-aware
parametric optimization of the truncated shrouded plug (G4: Paxson 2022 —
the closest single artifact to PB-2, and the natural benchmark for it).

------------------------------------------------------------------------------
## b2 — Classical variational nozzle theory (Rao, Guderley, Kraiko school)

VERDICT LANDED (full report in session transcript). All target
references verified; bibliographic corrections found; the critical
Kraiko-unsteady question resolved with a sharp distinction.

Canonical line (verified): Guderley-Hantsch, Z. Flugwiss. 3(9):305-313
(1955); Rao, Jet Propulsion 28(6):377-382 (1958), doi:10.2514/8.7324 —
two-multiplier control-surface structure CONFIRMED via NASA TM-103175
(Shyne-Keith, AIAA-90-2222): augmented functional ∫(f₁ + λ₂f₂ + λ₃f₃)dl,
λ₂ mass flow, λ₃ LENGTH (f₃ = cot φ), control surface = left-running
characteristic, multipliers fixed at the corner-adjacent point [the
specific "Eq. 14" label: UNVERIFIED, original paywalled];
CORRECTIONS: Rao's TOP approximation paper is ARS J. 30(6):561 (1960),
not 1961; "Rao 1961" is the SPIKE paper, Planet. Space Sci. 4:92-101
(1961), doi:10.1016/0032-0633(61)90125-8. Guderley-Armitage: Boeing
Symposium (1962) + Ch. 11 of Miele (ed.), Theory of Optimum Aerodynamic
Shapes (1965) — the "exact" full-contour variational problem.
Shmyglevskii: PMM 21 (1957), PMM 26(1) (1962), book VTs AN SSSR (1963).
Sternin CAVEAT: his books are TWO-PHASE nozzle gasdynamics
(Mashinostroenie 1974); the general Russian nozzle-theory textbook is
Pirumov-Roslyakov, "Gazovaya dinamika sopel" (1990) — fix internal
citations accordingly.

Kraiko school — ALL FOUR claimed papers CONFIRMED:
- Kraiko-Tillyaeva, Fluid Dyn. 17(1):156-159 (1982), doi:10.1007/BF01090716
  (nonuniform minimal-section inflow; Russian original Izv. MZhG 1981/1);
- Kraiko-Telyakovskii-Tillyaeva, ZhVMMF 34(10):1444-1460 (1994)
  (highly rotational/vortical supersonic nozzle profiling);
- Kraiko-P'yankov-Tillyayeva, Fluid Dyn. 37(4):637-648 (2002),
  doi:10.1023/A:1020653605889 (plug with NONUNIFORM TRANSONIC inflow;
  finding: ignoring transonic nonuniformity costs real thrust — direct
  support for the N3 channel's first-order status);
- Kraiko-Tillyayeva, Fluid Dyn. 42(2):321-329 (2007),
  doi:10.1134/S0015462807020172 (spike contouring + optimal primary-flow
  direction). Antecedent: Tillyaeva, Izv. MZhG 1975/3 (nonuniform and
  SWIRLING flows). Plug uniform-inflow predecessor: Fluid Dyn.
  35(6):945-955 (2000). Books: Variatsionnye zadachi gazovoi dinamiki
  (Nauka 1979, 448 pp; TOC UNVERIFIED); Teoreticheskaya gazovaya
  dinamika (TORUS PRESS 2010, 440 pp).
Scope map: the most general per-single-state result is optimal
bell/plug contouring, planar/axisymmetric, for ARBITRARY nonuniform,
vortical steady inflow, dimension/backpressure constraints, arbitrary
two-parameter EOS (1994 + 2002). Everything is per ONE steady inflow
state — exactly the "per-phase brick" of the T2 program, confirmed to
exist at the required generality.

The unsteady line (the C4 gate — RESOLVED with a distinction):
- Efremov-Kraiko, Fluid Dyn. 39(4):621-632 (2004),
  doi:10.1023/B:FLUI.0000045678.92653.98 — "ideal jet thrust augmentor":
  variational optimal-OUTFLOW conditions for max thrust given INTEGRAL
  inlet fluxes (mass/enthalpy/entropy/momentum), explicitly motivated by
  pulsed-detonation sources but formulated as a steady/ideal-limit BOUND
  — it sidesteps the shared-wall unsteady problem. MANDATORY CITATION.
- Kraiko-Egoryan, Fluid Dyn. 55(4) (2020), doi:10.1134/S0015462820020020
  (+ AIP Conf. Proc. 2027:020006 (2018)): detonation cycles evaluated
  with IDEAL (instantaneously adapted) nozzle bounds — i.e. the
  ideal-adaptation closure of T4 has published precedent AS A BOUND;
  T4's shape-level nested-argmax theorem remains unfound. MANDATORY
  CITATION next to T4.
- Levin-Manuilovich-Markov, Combust. Expl. Shock Waves 46(4):418-425
  (2010), doi:10.1007/s10573-010-0056-y: cycle-averaged impulse of a
  PULSE-detonation engine maximized over axisymmetric duct shapes — by
  DIRECT parametric/numerical search, no optimality/transversality
  conditions. The closest existing artifact to PB-1/PB-2 in spirit;
  MANDATORY CITATION.
- Kraiko's 1-D unsteady variational work (1979 book; piston/expansion
  impulse problems): 1-D process optimization, not 2-D wall contouring.

Adjoint bridge (G14): Giles-Pierce JFM 426:327-345 (2001) confirmed, no
Rao/Guderley connection anywhere in it; NEW ANCHOR FOUND: Lozano-Ponsin,
"On the characteristic structure of the adjoint Euler equations and the
analytic adjoint solution of supersonic inviscid flows", Aerospace
12(6):494 (2025) / arXiv:2503.13007 — 2-D supersonic ANALYTIC adjoints
with characteristic structure, and NO mention of Rao/Guderley/Kraiko:
the P2 bridge lemma now has both banks built (classical conditions on
one side, 2-D analytic adjoint on the other) and the bridge itself
confirmed missing.

Gap verdicts (b2): C1 (family-averaged classical contouring) NOT-FOUND(q);
C2 (averaged Rao-type wall/corner conditions) NOT-FOUND(q) — zero hits
under ensemble/phase-averaged-optimality queries; C3 (Rao = adjoint
identification) NOT-FOUND(q) — folklore-adjacent (multiplier field =
adjoint is textbook) but the specific published identification absent;
C4 PARTIAL as characterized above. Residual blind spot, declared: the
1979 book's table of contents is unverified — the human PMM/library pass
(D4 §3) remains recommended before print, now as due diligence rather
than as an open gate.

------------------------------------------------------------------------------
## b0 — The in-house classical corpus (GENO/literature) and the
##      per-nozzle variational method inventory

Source basis: primary PDFs in `GENO/literature/` (Rao 1958 `RAO.pdf`;
Rao 1961 spike + 1961 review; Veen 1974; Hoffman 1967; Humphreys-
Thompson-Hoffman 1971; Johnson-Thompson-Hoffman 1974 (Computers &
Fluids 2:173); Scofield-Hoffman 1971; Hoffman-Scofield-Thompson JOTA
10(3) 1972; Rao-Beck AIAA 94-3264; Rao-Beck-Booth AIAA 99-2584; Sternin
1962 Sov. Phys. Dokl.; Allman-Hoffman 1981; Zucrow-Hoffman Vol. 2;
Onofri NATO RTO-TR-AVT-007; NASA SP-8120; Viviano & Valeriani theses)
and the GENO variational dossier (`theory_variational_understanding.md`,
`theory_variational_optimization.md`, `toc_constraint_combinations.md`,
`variable_gamma_generalization.md`, `audit_rao_2constraint.md`), the
first of which was produced by a 19-agent workflow that read the primary
PDFs page-by-page.

RESOLUTION of a b2 UNVERIFIED item: Rao 1958's corner/transversality
condition IS "Eq. [14], p. 379" — verified in-house against `RAO.pdf`
(theory_variational_understanding §1.2, with per-equation page numbers
for Eqs [1]-[15]). The b2 web-side caveat is closed by the in-house
primary-source read; equation numbers may be cited.

### The common variational scheme (all GENO thrust-optimized types)

One scheme (Rao 1958; generalized Hoffman 1967): maximize
F = ∫_C^E [(p−p_a) + ρW² sin(φ−θ)cosθ/sinφ] 2πy^δ dy over the control
surface CE, subject to EXACTLY TWO isoperimetric constraints — mass
(multiplier λ₂) and length (λ₃, f₃ = cot φ); third multiplier h = 0
(Guderley-Hantsch). First variation delivers: (i) the optimal control
surface IS a characteristic (φ = θ+α shroud/bell; φ = θ−α plug/spike) —
a RESULT, not an assumption; (ii) first integrals f₂ = W cos(θ∓α)/cosα =
−λ₂ (mass) and f₁ = y^δ ρW² sin²θ tanα = −λ₃ (length; not independent —
a first integral of the system, used in GENO as a drift diagnostic);
(iii) endpoint transversality = corner conditions, sin(2θ_E) =
(p−p_a)cot α/(½ρW²) (C+ shroud, CSTR_PA) and sin(−2θ_G) = (p−p_b)cot α/
(½ρW²) (C− plug, CSTR_PB) — the ± from the CHARACTERISTIC TYPE, not from
the sign of θ. Doctrinal point (verified against five primary sources):
ambient/base pressure enters ONLY through endpoint transversality, never
as a third integral multiplier — exactly the structure the averaged
system (D3 §4) inherits, with (**') replacing the single-phase corner.

### Per-nozzle inventory (theory DOF vs GENO implementation)

| Type | Method | Variational DOF (theory) | GENO status | Rung-2 role |
|---|---|---|---|---|
| 2 TOC bell | Rao 1958, C+ surface | 2 {ε, L} ↔ (λ₂, λ₃); p_a via corner | MATCH (2 nested bisections; mass = curve termination `Rao_m.f90:417`) | the fixed-wall per-phase brick; T3 applies verbatim |
| 4 TOP | Rao kernel + parabola fit (Rao 1960) | kernel as TOC; parabola = documented geometric approximation | MATCH | cheap surrogate contour family for PB-1 scans |
| 0/1 ideal/TIC | non-variational (reference contours) | — | PROD | baselines/oracles |
| 3 conical | non-variational (Rao 1961 review reference) | 0 | MATCH | divergence-factor λ_d closure for Phase-B quasi-1D+ |
| 5 plug (Angelino) | non-variational construction | 0 (mass closure only) | MATCH | ideal-adaptation closure carrier (T4's H-T4) |
| 8 RaoPlug | Rao 1961 spike, C− surface | 2 {M_E, θ_E}; mass λ₂ PRIMARY (Rao 1961 Eq. (2)) | KNOWN STRUCTURAL BUGS S1/S2: mass NOT enforced, 1 DOF of 2 (curve ends on corner, never on mass match) | the free-boundary per-phase brick — MUST be fixed before PB-2 (roadmap prerequisite confirmed) |
| 7 Veen shrouded | Veen 1974 = Rao C+ shroud + Rao C− plug + kernel + p_b match | 2 per wall with PARTIAL masses; Eq. 9 base-pressure loop | PARTIAL: masses over-imposed (S4), Eq. 9 dropped (S5), coupled modes under-constrained (S6) | the PB-3 duty-split carrier; S4/S5 block quantitative use |
| 6 extension | PM-fan extension of TOC base | bisections on deviation | PROD | off-design/appendix |

Constraint-pair equivalence (TOC, verified formally + in code): the
2-DOF optimal family is reparametrizable by {ε,L} ↔ {p_a,L} ↔ {ε,p_a} ↔
{ε,θ₀} (bijective observable pairs); pairs involving MF are
quasi-degenerate, CF is the objective (not a constraint), inner=none is
under-determined. Direct support for D3 §4's treatment of the corner as
TRANSVERSALITY (bijective to ε) and for T3 remark (R2).

### What the in-house corpus adds to the gap analysis

1. HOFFMAN 1967 IS THE MISSING HALF OF G14/P2, published in 1967: for
   chemically reacting flow the optimality system is Lagrange-multiplier
   FIELDS λ₁..λ₄ (+λ₅ per species) satisfying PDEs along the SAME
   characteristics as the flow — a continuous adjoint avant la lettre,
   with an a-posteriori optimality residual E (Eq. 78) that is the
   classical ancestor of the Level-C stationarity certificate. The P2
   bridge lemma therefore has THREE banks: Hoffman 1967 (classical
   multiplier fields), Giles-Pierce 2001 (quasi-1D analytic adjoint),
   Lozano-Ponsin 2025 (2-D analytic adjoint) — none of which cites the
   others' side. P2's content narrows to the explicit identification +
   the reverse-AD = adjoint-characteristic-sweep statement.
2. HOFFMAN 1967 p.676 PROVES the corner bijection dies for reacting gas
   (E = 0 on multiplier fields replaces the algebraic corner): the
   closed-form per-phase brick is frozen-composition-only. This is
   classical, page-verified support for the N4 channel's structure and
   for the declared Level-A license boundary — and the reason the
   averaged system (**') must be formulated at the Hadamard/adjoint
   level, not only at the corner level, if finite-rate chemistry is in
   scope.
3. STERNIN 1962 (+ Rao-Beck 1994 Eq. 4 closed form) = the classical
   valid/invalid-region boundary for optimal-contour existence — the
   ancestor of P7's failure boundary (loss of MOC-regularity), ALREADY
   IMPLEMENTED as `boundaryfunction_solve` (Rao_m.f90:30-56, closed
   form, γ-free): the P7 "S1-regularity monitor" exists in code today.
4. E4 RISK (in-house, open): the corner↔ε bijection is DERIVED only for
   γ = const; for γ(T) frozen the equations are γ-agnostic in primitive
   variables and GENO enforces f₂ = const actively (correct approach),
   but NO known-answer validation exists — the only var-γ oracle with a
   published answer is Scofield-Hoffman 1971 Table 2 Case 1 (frozen
   thrust 2290 lbf; gate G2 of `variable_gamma_generalization.md`).
   Rung-2's per-phase brick for γ(ξ) families inherits E4: ledger row
   added (D1 §9).
5. Scofield-Hoffman's practical recommendation (design with FROZEN
   composition — closer to the finite-rate optimum than equilibrium) is
   the classical twin of T3's γ_eff-at-CJ closure (D3 §5.2): both say
   the early/locked state dominates the design.

------------------------------------------------------------------------------
## b3 — Shape/parameter calculus under hyperbolic constraints with shocks

State of the art (all VERIFIED, DOIs in the b3 session report). The
rigorous theory is 1-D: Bressan-Marson, Comm. PDE 20:1491 (1995)
(generalized tangent vectors); Bressan-Guerra DCDS 3:35 (1997); Ulbrich
SICON 41(3):740-797 (2002) + Systems & Control Letters 48:309 (2003)
(shift-differentiability, complete adjoint calculus for scalar laws with
sources); Giles-Ulbrich SINUM 48:882 & 905 (2010) (discrete adjoints
converge only with interior smearing conditions — the adjoint-consistency
trap is a theorem, not a rumor; practice-side confirmation: Lozano AIAA J
2018/2019 mesh-divergent inviscid adjoints). Frontier: Breitkopf-Ulbrich
arXiv:2509.22076 (2025), C¹ control-to-state for the generalized Riemann
problem (1-D systems, single shock, short time).

Euler adjoints with shocks: Giles-Pierce AIAA 97-1850 + JFM 426:327-345
(2001) — adjoint continuous across the shock, interior BC along it,
CLOSED-FORM quasi-1D adjoints, and the log-singularity at the sonic
throat (load-bearing for G14/P2 and for the transonic caveat of D1 §6).
The only rigorous design-with-shock theorem in the Euler setting is
quasi-1D: Cliff-Heinkenschloss-Shenoy JOTA 94(2):273-309 (1997) (fitted
shock as explicit unknown; existence + Fréchet differentiability +
multipliers) — the template P7/T2 should generalize, never extended to
2-D. 2-D practice: Baeza-Castro-Palacios-Zuazua AIAA J 47:552 (2009)
(adjoint Rankine-Hugoniot, alternating descent); Bardos-Pironneau
(2002/03, formal distributional calculus). Multi-D state theory that the
program leans on: Majda Mem. AMS 275 (1983) (uniform shock stability =
the front-linearization hypothesis of P1); Chen-Feldman JAMS 16:461
(2003) (transonic free-boundary); Li Ta-tsien school (semi-global
classical solutions; exact boundary controllability, SICON 2003) — the
S1 class's well-posedness language. Non-uniqueness: De Lellis-
Székelyhidi Ann. Math. 170:1417 (2009), ARMA 195:225 (2010);
Chiodaroli-De Lellis-Kreml CPAM 68:1157 (2015) — the reason S2 needs a
selection principle. Repairs: Fjordholm-Käppeli-Mishra-Tadmor FoCM
17:763 (2017); Fjordholm-Lanthaler-Mishra ARMA 226:809 (2017) +
M3AS 30:539 (2020) (statistical solutions, forward theory only).
Time-periodic quasilinear existence (relevant to rung 3 beyond relative
equilibria): Temple-Young (small divisors; arXiv:2406.00200 pure tones);
Fang-Qu-Yu arXiv:2306.09653 + Chin. Ann. Math. B (2024) — existence and
stabilization, NO optimal-design layer.

Gaps (b3): G12 multi-D thrust-functional shape derivative NOT-FOUND(q);
G13 optimization vs statistical solutions NOT-FOUND(q); design
sensitivity across a sonic line NOT-FOUND(q) (only the Giles-Pierce
singularity analysis — supports D1's decision to confine the degeneracy
inside the interface); optimal control of time-periodic quasilinear
systems NOT-FOUND(q) (existence yes, design no).

------------------------------------------------------------------------------
## b4 — Time-periodic flow optimization, periodic-orbit adjoints, detonation stability

State of the art (all VERIFIED, DOIs in the b4 session report).
HB machinery: Hall-Thomas-Clark AIAA J 40:879 (2002); first harmonic
adjoint Duta-Giles-Campobasso IJNMF 40:323 (2002); discrete HB adjoint
shape optimization Huang-Ekici AST 39:481 (2014); Thomas-Ekici AIAA J
52(6) (2014); DLR chain Engels-Putzka-Frey J. Turbomach. 141:031014
(2019); monolithic one-shot Thress-Kaminsky-Djeddi-Ekici AIAA J 60(6)
(2022). CRUCIAL STRUCTURAL FACT: in forced-response HB the frequency is
IMPOSED (blade passing); the unknown-period case lives in the LCO
literature — Krakos-Wang-Hall-Darmofal JCP 231:3228 (2012) — and in
dynamical-systems continuation (phase conditions: Sánchez-Net JCP 201:13
(2004); Tuckerman-Barkley 2000). Chaotic regimes: LSS Wang et al. JCP
267:210 (2014); NILSS JCP 347:56 (2017); NILSAS JCP 395:690 (2019);
Ruelle CMP 187:227 (1997). Relative equilibria: freezing, Beyn-Thümmler
SIADS 3:85-116 (2004), doi:10.1137/030600515. THE key precedent for P1:
spiral-wave RESPONSE FUNCTIONS — Biktasheva-Barkley-Biktashev-Bordyugov-
Foulkes PRE 79:056702 (2009); Biktasheva et al. PRE 81:066202 (2010) —
adjoint eigenfunctions at λ = 0, ±iω of a rigidly rotating wave with
unknown ω, used to predict drift/frequency response to perturbations:
the adjoint of a rotating relative equilibrium EXISTS as mathematics and
numerics, in excitable media, for drift — not for shape design, not in
gas dynamics. Detonation stability: Erpenbeck Phys. Fluids 5:604 (1962),
7:684 (1964); Lee-Stewart JFM 216:103 (1990); Texier-Zumbrun CMP 302:1
(2011) (galloping = Hopf, generic); Zumbrun ARMA 200 (2011); reduced
models Faria-Kasimov-Rosales JFM 784:163 (2015); RDE-as-pattern:
Koch-Kurosaka-Knowlen-Kutz PRE 101:013106 (2020) + PRE 104:024210
(2021); Koch-Kutz Phys. Fluids 33:091703 (2021). RDE mode multiplicity/
hysteresis documented (JPP doi:10.2514/1.B38801; AST 2022) —
descriptively only.

Gaps (b4): G7 NOT-FOUND(q) (strong precedent, unoccupied application);
G8 clean NOT-FOUND(q); G9 NOT-FOUND(q) as explicit statement — publish in
the corrected P1a/P1b form (D3 §7); G16-RDE NOT-FOUND(q).

------------------------------------------------------------------------------
## b5 — Shape-optimization theory, multipoint/robust design, dual-bell analogue

State of the art (all VERIFIED, DOIs in the b5 session report).
Existence/structure: Chenais JMAA 52:189 (1975) (uniform cone);
Murat-Simon (1976); Delfour-Zolésio 2nd ed. SIAM (2011); Sokolowski-
Zolésio (1992) (Hadamard structure). Newton's problem: Buttazzo-Kawohl
Math. Intell. 15(4):7 (1993); SYMMETRY BREAKING of the optimal body:
Brock-Ferone-Kawohl Calc. Var. 4:593 (1996); Lachand-Robert-Peletier
Math. Nachr. 226:153 (2001); Lachand-Robert-Oudet SIOPT 16:368 (2005) —
the rigorous reason D1 treats axisymmetry as a hypothesis with a
perturbative check (P5), not an assumption. Metrics: Schulz FoCM 14:483
(2014); Schulz-Siebenborn-Welker SIOPT 26:2800 (2016). Multipoint/OUU:
Drela (1998) single-point overfitting critique; Buckley-Zhou-Zingg
J. Aircraft 47:1707 (2010) (18-point); Huyse-Lewis ICASE 2001-1 +
Li-Huyse-Padula SMO 24:38 (2002) (expectation over a Mach DISTRIBUTION —
the continuous-measure idea exists in aero); Liem-Kenway-Martins AIAA J
53:104 (2015) (mission-data-derived measure — closest formulation
pattern to μ); CVaR: Rockafellar-Uryasev J. Risk 2(3):21 (2000);
Kouri-Surowiec SIOPT 26:365 (2016) (PDE-constrained CVaR, elliptic);
two-stage stochastic shape opt Conti-Held-Pach-Rumpf-Schultz SIOPT
19:1610 (2009); Dambrine-Dapogny-Harbrecht SICON 53:3081 (2015) (state
LINEAR in random input ⇒ moments suffice — the closest published
relative of the T3 affinity mechanism, in elliptic setting);
Wasserstein-DRO shape/topology optimization EXISTS: Dapogny-Iutzeler-
Meda-Thibert SMO (2023), doi:10.1007/s00158-023-03500-4; aerodynamic DRO:
Chen-Rottmayer-Kusch-Gauger-Ye CMAME (2024). Consequence for the notes:
PB-5's DRO framing must cite these as EXISTING method, new application.
Dual-bell: Foster-Cowles (1949) and Horn-Fisher (1994) [secondary-source
verified only]; Frey-Hagemann JPP 15:137 (1999), doi:10.2514/2.5402;
Hagemann-Immich-Nguyen-Dumnov JPP 14:620 (1998), doi:10.2514/2.5354;
DLR trajectory-coupled optimization: Stark-Génin et al. JSR (2016),
doi:10.2514/1.A33363 (Ariane 5, parametric sweeps + TOSCA trajectory
code, up to 490 kg GTO gain). Sutton folklore: boosters pick the area
ratio for "average performance" — mechanism implicit, never a stated
result.

Gaps (b5): G15 NOT-FOUND(q) (no variational trajectory-measure nozzle
problem; no published affine-collapse statement — nearest: certainty
equivalence in stochastic control, e.g. expectation of cost linear in
noise optimized by the mean problem, and Dambrine et al. 2015); G17
NOT-FOUND(q) (existence for hyperbolic families — elliptic only); G16
method-FOUND/application-NOT-FOUND. Explicit b5 caveat: Kraiko school
not web-covered — reinforces the b2 gate.

------------------------------------------------------------------------------
## b6 — Time-homogenization, nozzle admittances, quasi-steady validity

State of the art (all VERIFIED, DOIs in the b6 session report).
Linear transfer functions: Marble-Candel JSV 55:225-243 (1977),
doi:10.1016/0022-460X(77)90596-X (compact limit); Cumpsty-Marble Proc.
R. Soc. A 357:323 (1977); Stow-Dowling-Hynes JFM 467:215 (2002) and
Goh-Morgans JSV 330:5184 (2011): O(He) EFFECTIVE-LENGTH correctors to
the compact limit — the exact linear analogue of the P4 corrector, but
for reflection coefficients, not thrust; Duran-Moreau JFM 723:190 (2013)
(all-frequency quasi-1D via Magnus/invariants); Motheau-Nicoud-Poinsot
JFM 749:542 (2014). Admittance tradition: Crocco-Cheng AGARDograph 8
(1956); Crocco-Sirignano AGARDograph 117 (1967) [DTIC AD0672435];
Bell-Zinn NASA CR-121129 (1973). NONLINEAR compact transfer functions
EXIST: Huet-Giauque JFM 733:268-301 (2013), doi:10.1017/jfm.2013.442
(+ Huet JSV 2016) — i.e. the ZEROTH-ORDER (quasi-steady) nonlinear
nozzle map of the P4 expansion is published; Zinn-Crocco Astronautica
Acta 13:481 (1968) [secondary-verified]. Homogenization/averaging:
Allaire SIMA 23:1482 (1992); Bensoussan-Lions-Papanicolaou (1978);
Chechkin-Piatnitski-Shamaev AMS TMM 234 (2007); Sanders-Verhulst-Murdock
2nd ed. (2007) — all coefficient-oscillation or parabolic; the right
scaffold for oscillating BOUNDARY data on quasilinear systems is weakly
nonlinear geometric optics: Joly-Métivier-Rauch (Ann. ENS 28:51 (1995) +
program); Coulombel-Guès-Williams Comm. PDE 36(10) (2011), Anal. PDE
7:551 (2014); Kilque SIMA (2022), doi:10.1137/21M1413596 — leading
profiles for highly oscillating boundary forcing on quasilinear systems
INCLUDING 2-D isentropic Euler, but strictly at weakly nonlinear
amplitude O(ε); nothing at O(1) amplitude (where the RDE lives:
PR ≈ 50 pressure swings). Time-periodic Euler existence: Temple-Young
(small divisors); subsonic periodic solutions (2023-24). Quasi-steady
validity data: PDE thrust-augmentation frequency dependence;
Kaemming-Paxson EAP as steady-equivalent bookkeeping (AIAA 2018-4567);
turbocharger quasi-steady-map errors under pulsation; RDE unsteadiness
Isp deficits quoted only qualitatively ("a few percent", UNVERIFIED as a
standalone number).

Gaps (b6): G10 clean NOT-FOUND(q) — no J = J_qs + St·J₁ + O(St²) for
thrust anywhere; G11 NOT-FOUND(q) at O(1) amplitude with a rigorous
PARTIAL scaffold (Kilque/CGW) that a linearized-corrector theorem (P4
with small-oscillation hypothesis) could use AS-IS; error-bar data (C3)
PARTIAL — validation targets exist, no competing theory. Sharp framing
delivered by b6: the P4 program = "extend Huet-Giauque (nonlinear,
compact) in the St direction, or extend Stow-Dowling-Hynes/Goh-Morgans
(linear, O(He)) in the amplitude direction, for the THRUST functional" —
both extensions unoccupied.

------------------------------------------------------------------------------
## 7. Cross-strand synthesis: where the problem actually sits

1. The ENGINEERING strand (b1) knows the problem exists (Gonzalez-Viana
   2025 states steady criteria are invalid; Harroun observes time-
   averaged-perfect expansion) and answers it with black-box CFD
   optimization on parametric families. No functional, no optimality
   system, no theorem. The internal T3 explains WHY their time-averaged
   heuristic works as well as it does — and none of them states it.
2. The MATHEMATICAL strands (b3, b6) supply rigorous 1-D/weakly-nonlinear
   bricks (shift-differentiability; analytic quasi-1D adjoints;
   geometric-optics boundary layers) and STOP exactly at the joints the
   RDE problem needs: multi-D shape derivatives with shocks, O(1)
   time-homogenization, design through sonic degeneracy.
3. The DYNAMICS strand (b4) has the freezing/relative-equilibrium and
   response-function technology the wave-frame problem needs, unapplied
   to compressible reacting flow or shape design.
4. The DESIGN-THEORY strand (b5) has measures-over-conditions, CVaR, DRO
   — with the elliptic-state caveat — and the symmetry-breaking warning;
   its own folklore (mean-ambient-pressure boosters) is exactly T3's
   corollary 2, unproven in print.
5. The CLASSICAL strand (b2, LANDED) confirms: the per-phase brick
   exists at full generality (Kraiko 1994/2002: arbitrary nonuniform,
   vortical inflow, arbitrary EOS), the unsteady line went to bounds
   (Efremov-Kraiko 2004; Kraiko-Egoryan 2020) and 1-D processes, the
   PDE-duct cycle-averaged optimization exists only as direct search
   (Levin-Manuilovich-Markov 2010), and the averaged wall/corner system
   is nowhere. The 2025 Lozano-Ponsin 2-D analytic adjoint builds the
   second bank of the P2 bridge without noticing the first.

Bottom line, query-bounded: the internal notes' program occupies a real
hole whose edges are populated by strong, recent, verifiable work on
every side — which is simultaneously the best evidence that the hole is
real (people circle it) and the reason every claim stays query-bounded.
Residual due diligence before print: a human pass on Kraiko's 1979 book
(TOC unverified) and the PMM archives (D4 §3).
