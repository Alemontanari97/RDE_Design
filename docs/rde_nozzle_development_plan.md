# Development plan: from formalized idea to a formally optimal, certified methodology (D6)

Status: DELIVERABLE D6 (2026-07-16; STATUS DELTA-PASS 2026-07-17, S9
[F1/SCAFFOLD-M] — states/gates/90-days refreshed against the real
tree, plan substance unchanged). Integrates and AMENDS
`docs/roadmap_geno_rde.md` (WP0-WP8, gates G0-G4) with everything this
session established: D1-D5, the corrected optimality system ((**')),
the bound ladder, the panel scheme and its refutations, the
prescribed-profile convergent pipeline (D5 Annex A), and the literature
gates. Where this plan and the old roadmap differ, THIS plan wins.
WORK-PLAN LAYER NOTE (2026-07-17): the theory corpus now has its typed
INDEX — docs/claims_registry.yaml + suite group (xv) lint (SCAFFOLD
migration M-1..M-5 executed, S9); this plan remains the WORK index
(phases/gates/90-days); a maintainer opens SCAFFOLD §1 (L0), the
registry, then THIS plan + PROGRESS.

------------------------------------------------------------------------------
## 0. What "formally optimal methodology" means here (the certainty model)

Full certainty is NOT one big theorem; it is a LATTICE with four rungs,
all mandatory for every shipped result:

  C1 THEOREMS where the mathematics allows (T0, T3, T4, O1, O2; targets
     P2', P3, P4', P7) — proofs in-repo, hypotheses in the ledger.
  C2 CERTIFICATES everywhere else: KKT + weighted transversality (**')
     residuals; dual-route B1/B2 agreement; dot-product O3 at machine
     precision; Hoffman E-residual; second-order reduced-Hessian check;
     S1 membership monitor; DWR discretization bars.
  C3 BRACKETS: every reported optimum Sigma* ships with the bound-ladder
     upper bound B (shared-wall relaxation, ideal-adaptation bounds) and
     the CERTIFIED GAP B - J(Sigma*). This is the strongest available
     statement of "optimal": not faith in a local optimizer, but a
     bracketed value with a theorem-grade upper wall.
  C4 DECLARED ERROR BARS: O(St) physical bar (P4), D2 azimuthal residual
     (WP5 anchor), model-form rows of the ledger.

Rule of the shop (unchanged, enforced): no number without a committed
script + test; no novelty claim without a query list; no "Fixed" without
a passed gate. The one standing counterexample (the missing
gamma_cycle_probe.py) was Action A0.3 below — CLOSED 2026-07-16
(examples/gamma_cycle_probe.py + tests/test_gamma_probe.py; numbers of
record in D3 §5.2: gamma confirmed, eps* shift corrected to -0.56%,
penalty corrected to -0.00028%).

------------------------------------------------------------------------------
## 1. Critical path (revised)

The old roadmap's spine (rung 2 first, oracles first) SURVIVES the panel
review — with these amendments baked in:
  (i)    (**') everywhere; (**) only as the T3-class special case.
  (ii)   Switch-split quadrature in xi (D5 Annex A stage D): locate
         xi*(Sigma) by root-finding, split Gauss panels there, include
         the Leibniz terms (they cancel by continuity of F — verified).
         Non-negotiable: unsplit quadrature degrades to O(1/N) AND
         poisons the outer gradient.
  (iii)  Bound ladder FIRST (OP-0): eps-level Proposition B1 in week 1;
         contour-level bounds as soon as WP1 marches. The G2 value gate
         becomes theorem-grade (kill by bound gap, not by failed run).
  (iv)   RaoPlug S1/S2 fix is ON the critical path (blocks OP-2, the
         first genuinely averaged optimum).
  (v)    Data contract of D5 Annex A stage A (Crocco compatibility,
         characteristic completeness, loud reject) is part of the
         CycleFamily interface C1, not an afterthought.

------------------------------------------------------------------------------
## 2. Phases, with SOTA tool bindings

### Phase A0 — Consolidation (weeks 0-6, mechanical, no research risk)
[STATUS 2026-07-17: PHASE CLOSED (formally, session S2 2026-07-16).
A0.1-A0.4 done (see items); A0.5 partially discharged in-house (see
item); OP-0/OP-11-eps closed INCLUDING the EOS-general real-thermo
route (suite groups (xi)/(xii): real ceiling + real-route diagram +
equilibrium bracket, S7/S8).]
A0.1 Propagate D4 §6 fixes (Mo/Huang → Mo 2015 + Li-Xu-Huang 2022; S-H
     title; Rao 1960/1961 split; Sternin→Pirumov-Roslyakov caveat).
A0.2 Freeze D1 as the problem book of record; map every ledger row to a
     CI check where executable.
A0.3 Re-derive the gamma-channel numbers with a COMMITTED probe script +
     test, or strike them from all docs. [DONE 2026-07-16: examples/
     gamma_cycle_probe.py + tests/test_gamma_probe.py; D3 §5.2 corrected]
A0.4 OP-0: bound ladder at eps-level on the Table-1 states (S-H closed
     forms + ideal-adaptation bound + shared-wall relaxation). One
     module, one test, immediate value calibration of N1-N4.
     [DONE 2026-07-16: src/thrust/bounds.py + tests/test_bounds.py +
     data/bounds_ladder.{json,md}; chain verified 18/18; DISCOVERY: the
     naive G-B rung needs the sonic (choking) cap — M0 Prop. 7 and D3
     Prop. G-B sharpened; M1 gap-zero attainment confirmed on the 8
     supercritical sea-level rows]
A0.5 Human due diligence kickoff: Kraiko 1979 monograph TOC + PMM pass
     (library access); required before any submission (D4 §3).
     [STATUS 2026-07-17: Item 2a (PMM TOC sweep) DONE IN-HOUSE, S7:
     204/204 issues 1957-90, raw-HTML method of record — G14/P-2
     novelty HOLDS; TOP FLAG Kraiko-Osipov PMM 34(6) 1970 declared
     (P-1 §4.5/G6 wording CONTINGENT on its full text, D4 §3 armed).
     Item 1 (Kraiko 1979 TOC) + Item 2b (ranked reading list, ready in
     validation/G5_pmm_toc_sweep_1957-1990.md): dispatch package
     COMPLETE (validation/G5_dispatch_email.md, recipient verified);
     RESIDUAL = the user's send. See gate G5.]

### Phase A1 — Differentiable per-phase engine (months 1-6) [= WP1 amended]
[STATUS 2026-07-21 (S11): BRICK 1 DONE — profile-generation machinery
of record ([X-A1IM], validation/a1_ideal_march_jax.py, VERDICT PASS):
assembled differentiable MoC march (ideal-nozzle twin of GENO
nozzle_type 0) generating the contour end-to-end from the Sauer IVL to
the bounding-streamline wall; GENO cross-code contour agreement 7.6e-9
(62/62 inside the derived Richardson band) on the reduced case; O3.1
dot-product over the ENTIRE march 2.7e-10 vs tol 5.1e-8 (= Lemma B
adjoint executably); tabulated thermo backend per [DIR-THERMOTAB]
(Cantera SOLE production table generator; GENO NASA-poly generator
confined to cross-code oracle instances). NEXT bricks: variational TOC
((**')/corner transversality via dJ/dSigma with TR-SQP — never a
hard-coded outer loop), fitted single transversal sheet, plug
free-boundary march; G0 loop-speed falsifier stays armed.]
[STATUS 2026-07-17 (S10): OPEN — gate G0 DECIDED (JAX primary; dossier
docs/rde_nozzle_G0_decision.md, registry [DIR-G0]). Stack fixed, GENO
dual-code interop exercised (cross-code oracle X-GENOXC PASS). First A1
brick = gamma(T) backend unit process with X-GENOXC as standing
cross-code regression; then fitted single transversal sheet + plug
free-boundary march (content below). Prior spike record retained:]
[STATUS 2026-07-17: STARTED EARLY at spike level — S5 planar spike
(interior + inverse-wall, implicit custom_vjp, 52/52) and S8 twin
(axisymmetric source DUAL-ROUTE, fitted shock point on RH with O3.1
dot-product => P-B1 discharged at brick level, Lax/Majda executable,
first GENO read-only interop brick). G0 decision dossier COMPLETE on
the spike side; residual named under gate G0 (Fortran toolchain).
Rigor bricks of the phase's shape calculus already THEOREM-grade:
G12-S1, N6-1/2/3, five-field structure (registry IDs, carriers in
suite groups (xiii)/(xiv)).]
Stack decision (gate G0): default JAX (custom_vjp/custom_jvp per unit
process; implicit-function rules for iterative inner solves — never
unrolled; jaxopt-style implicit diff), Julia+Enzyme as alternate;
GENO-Fortran stays the independent verification reference (dual-code
discipline). Fallback: Tapenade on GENO.
Content: analysis-mode MOC (planar/axisym, rotational Ch.17 class,
gamma(T) backend, nonuniform IVL ingestion honoring the stage-A data
contract), FITTED single transversal sheet (inherited oblique shock),
plug off-design free-boundary march (RK1: front-load months 1-3,
Angelino limits as oracle), separation-criterion hook.
Certificates at M1: O3 dot-product at machine precision on every unit
process; GENO regression set reproduced; Hoffman E-residual ~ 0 on one
TOC case (this simultaneously seeds the P2 paper).

### Phase A2 — Cycle layer + first science (months 4-12) [= WP2 amended]
Quadrature with switch splitting; TR-SQP on spline space with
Sobolev/Steklov-Poincare Riesz gradients (mesh-independence check);
bundle safeguard near switches; constraints {L, eps_max, lip,
truncation} with active-set multipliers reported as marginal values.
GATE G1 (oracle gate, unchanged and absolute): O1 (T3 collapse), O2 (T4
peak plug), O3 pass — else no science downstream.
First science (each number = ledger row + oracle record + BOUND GAP):
N1 separated bell (temporal dual-bell question); N2 truncated plug vs
Paxson AIAA 2022-4107 benchmark (needs RaoPlug S1/S2 fixed + Rao
1961-spike Table-1 oracle passed); N3 per-phase inlet nonuniformity
(GENO IVL chain); N4 gamma(T) contour-level (expected null → publish as
bound; Scofield-Hoffman Table-2 frozen-thrust 2290 lbf as the only
known-answer var-gamma oracle).
[NEW BENCHMARK 2026-07-21 (S12): GONZALEZ-VIANA REPRODUCTION —
Aerospace 12:502 (2025) full-text read, PDF in literature/. Their
single-cycle PDE multi-objective optimization finds optimum
divergent nozzles of SMALL area ratio (A9/A8 = 1.13-1.31 with up to
15 available) with time-averaged exit pressure 1.4-2.1 bar >> Pa —
"steady criteria invalid". Three-way attribution of record:
(a) constraint effects (their length bound ACTIVE at all
performance optima — classical); (b) MEASURE effects — rung-2
predicts their qualitative result (tail-dominated mu + sonic cap +
weighted (**') => small eps*, mean-underexpanded optimum): the
eps-level reproduction with THEIR blowdown measure is a days-scale
task on existing machinery and arms P-1 sections 7-8 against the
"steady-theory-invalid" objection; (c) genuinely unsteady residue
(start-stop transit, air-filled nozzle) = the O5 anchor content —
maximal in single-cycle PDE, structurally absent in continuous-
rotation RDE (T3-QS explains the severity ranking). Their dataset
is "available on request" — an external-validation contact worth
making.]
[BENCHMARK ROW, 2026-08-05 (D8 §8 roads-atlas residue, second-lens):
Levin-Manuilovich-Markov 2010 (Combust. Expl. Shock Waves
46(4):418-425, doi:10.1007/s10573-010-0056-y; lit map b2 MANDATORY
CITATION, closest artifact to PB-1/PB-2 — cycle-averaged impulse of a
PDE duct by DIRECT parametric search) is recorded as a third external
anchor candidate alongside Paxson AIAA 2022-4107 and Gonzalez-Viana;
reproduction/comparison VERDICT-gated at A2, adoption not implied.]

### Phase A3 — Dual-route certification (months 8-14) [= WP3 amended]
B2: direct collocation of the averaged optimality system — per-phase
Rao/Kraiko conditions + averaged wall + (**') + lambda2(xi) samples —
one Newton BVP (pseudospectral collocation); DEFLATED continuation
(Farrell-style) to enumerate stationary contours (uniqueness never
assumed). Agreement B1↔B2 to tolerance = the stationarity certificate;
disagreement = bug detector.

### Phase A4 — The O(St) license (months 10-16) [= WP4 + OP-3/OP-3']
Numerical transfer functions on per-phase base flows (Marble-Candel
class; nonlinear compact zeroth order = Huet-Giauque, cite as prior
art); corrector J1; theory target P4' (Gamma-convergence on the P7
compact class so MAXIMIZERS converge); validation O5 vs direct unsteady
quasi-1D/2-D simulation; anchor against the PDE-literature unsteady vs
quasi-steady competition data (Cooper-Shepherd). Gate G3: if St|J1| =
O(several %), elevate WP5 to correction loop (design rung 2, correct
rung 3, iterate).
[STRENGTHENED 2026-07-21 (S12, [T-T3QS]): the license test is now a
PRE-REGISTERED falsification experiment, not a blind measurement.
O5-LITE (quasi-1D unsteady solver, Morris/Gonzalez-Viana class,
days-scale build) tests the three declared T3-QS predictions BEFORE
any tuning: (P-i) smooth ray cycle => |J_unsteady - J_rung2| =
O(St^2), NOT O(St); (P-ii) blowdown sawtooth => first-order residue
proportional to [k]_jump and LOCALIZED in the wave-passage transit
window; (P-iii) two-parameter cycle => residue scales with the
data-loop area. Each prediction ships with its rejector; failure of
any is a discovery, not a calibration. Anchors: Cooper-Shepherd
(identification J. Propulsion Power 24(1):81-87 (2008), TO
PAGE-VERIFY on acquisition) + Owens-Hanson JPP 23(2):325-337 (2007)
+ the Gonzalez-Viana benchmark of the Phase-A2 science note.]

### Phase A5 — Wave-frame anchor (months 12-22, parallel) [= WP5 + OP-5]
[FIRST ITEM 2026-07-21 (S12, [S-BLITE]): B-LITE DEMONSTRATOR before
the full anchor — (a) verify the 3-D axial-flux eigenstructure brick
(G12-L1-3D, symbolic carrier, days); (b) 3-D helical space-marching
of the NOZZLE-ONLY wave-frame field (u_x - c >= delta certified, I1
data, Omega input, fitted sheet per station, adjoint = Lemma B
lifted) — the exact rung-2 sweep/D2 residual at MARCHING cost. The
full camera-included anchor below stays the tier for Omega-output,
subsonic pockets and reaction; B-lite de-risks it and delivers the
license meter years earlier.]
2-D unrolled-annulus reactive Euler in the co-rotating frame; freezing
(phase condition, unknown Omega_w); Newton-Krylov (matrix-free,
PETSc-SNES/KrylovKit class) + Arnoldi spectra (SLEPc/ARPACK); HYBRID
implicit shock tracking (fit primary front, capture cellular residue —
panel-vetted); BORDERED adjoint delivering dJ/dSigma AND dOmega_w/dSigma
together. Certificates: O4 (adjoint vs FD of continued waves);
dynamic-consistency re-simulation at Sigma* (panel element, demoted
from Floquet gating to post-hoc DNS). Deliverables: D2-error
quantification on 2-3 Phase-A2 designs; the P1a/P1b paper's numerics;
optional U4 (computer-assisted existence of the wave on the reduced
model).

### Phase A6 — Robust/coupled layer (months 16-24) [= WP6 amended]
Finite branch table from operability data; CVaR_beta (Rockafellar-
Uryasev reformulation) over the mode measure; decision-dependent DRO
(Luo-Mehrotra finite-dim theory; PDE application new — cite) with
trust-region census↔gradient alternation (panel element 6); reduced
differentiable chamber response map Sigma -> (PR, Omega_w, fill) from
the matched-cycle machinery; the D5 Annex-A stage-G fixed point with
MEASURED contraction constant q (q >~ 1 → declare genuine bilevel,
PB-4 frontier).

### Phase A7 — Productization [= WP7, unchanged in shape]
CLI/API on the C1-C3 contracts; Verdict = contour + performance +
certificate stack (C1-C4 of §0) + oracle record. Nothing leaves the
tool outside a Verdict.

------------------------------------------------------------------------------
## 3. Theory/publication stream (updated, with the time-sensitive item)

P-1 (submit after M1; TARGET VENUE: JPP class): Formulation + collapse
    dichotomy. T0 (strengthened: instantaneous constancy),
    T1-as-definition + P4 statement, T2 with (**'), T3/T4 with verified
    proofs, oracles, altitude-duality corollary, N1-N6, the measure
    lemma. Prior-art citations per D4 (mandatory list) + the two
    concordance bridges (EAP and S-H remarks in M0 Part III: the
    field's own metric and model are contained and completed — their
    numerical findings become corollaries of T3/T4/vacuum theorems).
    This paper EXPLAINS the field's time-averaged design practice —
    the citable clarification.
    [STATUS 2026-07-17: SKELETON OF RECORD written (S5,
    docs/rde_nozzle_P1_skeleton.md, claim map C1-C26, acceptance rules
    (a)-(e)); FULL TEXT §2 + §4 of record written (S8,
    docs/rde_nozzle_P1_sections_2_4.md; §4.5 novelty wording
    CONTINGENT on Kraiko-Osipov PMM 34(6) 1970 full text — D4 §3
    armed). Registry note: paper claims now cite registry IDs
    (SCAFFOLD §5 — papers assemble by query). Remaining: §5-§7 text
    (now citable: eps*_real carrier group (xii) + equilibrium
    bracket), then §1/§3/§8/§9.]
P-2 (TIME-SENSITIVE, can precede or accompany P-1): the P2' bridge
    lemma — Rao/Kraiko conditions ≡ closed-form adjoint characteristics;
    three published banks (Hoffman 1967; Giles-Pierce 2001;
    Lozano-Ponsin 2025) and no bridge; Lozano-Ponsin built the 2-D bank
    in 2025, so the identification is at risk of being scooped. Cheap:
    mostly assembly + the reverse-AD = adjoint-sweep statement + O3/E
    numerics from M1. [OUTLINE OF RECORD 2026-07-16, [F1/P-2]:
    docs/rde_nozzle_P2_outline.md — statement (Lemmas A/B with rigor
    classes and falsifiers), banks, O3 oracle plan, declared risks.
    VENUE DECIDED 2026-07-16 (delegated, evidence-based): AIAA Journal
    primary + arXiv preprint at (G5 pass ∧ draft ready); Aerospace
    fallback with declared triggers; JOTA tertiary — outline §7.]
    [STATUS 2026-07-17: BOTH LEMMA DRAFTS OF RECORD WRITTEN — Lemma A
    (S5, docs/rde_nozzle_P2_lemmaA.md; S6 rigor upgrades: (ii) THEOREM
    via Prop. A2 + A3, P-A1/P-A1'/P-A2 discharged, carrier X-PA1 19/19
    in suite group (xiii)) and Lemma B (S7,
    docs/rde_nozzle_P2_lemmaB.md; P-B1 discharged at brick level S8,
    dual-route conservative carrier X-P2A1 in suite group (xiv)).
    The arXiv trigger is HALF-ARMED (draft ready; G5 pass pending).
    Residual numeric half: O3.2/O3.3 on the A1 engine (P-A3).]
P-3 (after M3): first certified cycle-averaged optima (N1/N2 numbers
    with dual-route certificates and bound gaps; truncated plug vs
    peak/mean baselines and vs Paxson parametric benchmark).
P-4 (after G3 data): the O(St) thrust corrector + Gamma-convergence
    license (P4'), validated (O5).
P-5 (after M5): P1a/P1b — freezing-adjoint sensitivity of a rotating
    detonation relative equilibrium with dOmega/dSigma; sensitivity
    degeneracy exactly at neutral modes; spiral-wave RF + Beyn-Thuemmler
    prior art.
Gating: A0.5 (Kraiko human pass) before ANY of P-1/P-2/P-3 submits.

------------------------------------------------------------------------------
## 4. SOTA tool matrix (what the team must actually know)

| Layer | Tools/knowledge | Used in |
|---|---|---|
| AD | JAX custom_vjp/jvp, implicit-diff rules; Enzyme/Julia; Tapenade fallback | A1-A3 |
| MOC/fronts | GENO unit processes; shock-FITTED marching; HOIST-class implicit shock tracking (Zahr-Persson) for A5 | A1, A5 |
| Optimization | TR-SQP; Steklov-Poincare/Sobolev shape metrics; proximal-bundle (nonsmooth); deflated continuation; pseudospectral collocation (B2) | A2-A3 |
| Dynamics | freezing/phase conditions; Newton-Krylov matrix-free; Arnoldi/SLEPc; Floquet as diagnostic; unknown-period LCO adjoints (Krakos windowing) | A5 |
| Error control | dot-product tests; DWR goal-oriented estimates; Richardson/dual-mesh checks | all |
| UQ/robust | CVaR reformulation; Wasserstein-DRO (entropic/Sinkhorn); decision-dependent DRO | A6 |
| Thermo | Cantera/CEA chains (repo); gamma(T) tables; Scofield-Hoffman oracle setup | A1-A2 |
| V&V culture | oracle-first CI; hypothesis-ledger rows as tests; md5/regression discipline (GENO) | all |

------------------------------------------------------------------------------
## 5. Gates and kill criteria (updated)

G0 (wk 4)   stack decision — criteria: gradient fidelity, loop speed,
            AND (user decision of record, S5) GENO interop: GENO stays
            Fortran provided the whole pipeline stays functional —
            file exchange + O3.4 cross-code oracle are explicit G0
            criteria (dual-code M0 VI.7).
            [STATUS 2026-07-17: DECIDED (S10; registry [DIR-G0]; dossier
            docs/rde_nozzle_G0_decision.md). Verdict: JAX primary
            (custom_vjp + implicit rules), Julia+Enzyme declared
            alternate, GENO-Fortran independent dual-code reference.
            Criteria met: (i) gradient fidelity — spikes 52/52 + O3.1
            machine precision (X-G0/X-G0AX); (ii) loop speed MEASURED
            STANDALONE — solve ~322 us, solve+adjoint ~327 us (grad/solve
            ratio ~1.01, host-invariant; absolute us host-caveated per S9);
            (iii) GENO interop NAMED RESIDUAL now CLOSED — GENO BUILT
            (WSL gfortran 11.4.0, CMake, Cantera/Sundials/Tecio OFF,
            LAPACK from host conda env; GENO never modified/committed),
            tocnoz regenerated, contour reproduced to 1e-10, md5 field
            convention N-36 confirmed, and the FLOWFIELD cross-code oracle
            [X-GENOXC] PASS (100% of the clean supersonic core inside the
            derived per-cell truncation band; both negative controls
            reject). Loop-speed falsifier kept: if the assembled A1 loop
            is impractical on JAX at production mesh, flip to Julia+Enzyme.]
G1 (M1+)    ORACLE GATE (absolute): O1/O2/O3 or no science.
G2 (M2)     VALUE GATE, now theorem-grade: bound-ladder gap per channel;
            gap < ~1% Isp on all of N1-N4 → pivot to certification/
            operability/duty-split value proposition (honest death).
G3 (M4)     UNSTEADINESS GATE: St|J1| large → rung-3 correction loop.
            [S14 duty (PAN-S14, PM lens): the trigger "large" must be
            a NUMBER with a derivation before A4 starts — currently
            the only gate whose kill threshold cannot reject.]
G4 (M5)     DECOUPLING GATE: D2 error dominates → wave-frame objective.
G5 (new)    LITERATURE GATE: A0.5 pass before any submission.
            [STATUS 2026-07-17: Item 2a DONE in-house (S7 PMM digital
            sweep 204/204; G14 holds; TOP FLAG Kraiko-Osipov PMM 34(6)
            1970 — multi-regime cousin). Dispatch package READY (email
            + verified recipient + Item 2b ranked list); RESIDUAL =
            user send from institutional account, then the full-text
            read. Blocks SUBMISSIONS only, never the work.]
            [STATUS S14: K-O 1970 contingency ADJUDICATED 2026-07-22
            (containment, in-repo full text) — the 2b list SHRINKS by
            its top item. SCOPE EXTENSIONS of record (PAN-S14, Kraiko
            lens + teams): (a) PMM/Fluid Dyn./MZhG title sweep
            1991-2010 (school active through 2007); (b) K-O 1970
            bibliography back-chase (refs [1],[2],[8],[9],[11] —
            Kraiko 1963 Trudy VTs now a register row, TITLE-VERIFIED);
            (c) Kraiko 2010 "Teoreticheskaya gazovaya dinamika" TOC
            alongside the 1979 monograph; (d) NEW content row 2.2(f):
            swirling-flow control-surface contouring — Tillyaeva Izv.
            AN MZhG 1975 no. 3 full-text check against T-N6-2's
            free-vortex closure. GOVERNANCE (PM lens, opinion-class):
            time-box the user send + declare a fallback channel.]
G6 (new)    DATA-CONTRACT GATE: any CycleFamily failing stage-A audits
            (Crocco, completeness, H-I2) is rejected loud — no design on
            inconsistent data.

------------------------------------------------------------------------------
## 6. First 90 days (concrete, amended; STATUS REFRESH 2026-07-17)

1. A0.1-A0.4 (fix docs; bound ladder eps-level; probe script).   (wk 1-3)
   [DONE — S1/S2; ladder extended to the real-thermo route S7/S8.]
2. G0 spike: ONE unit process (interior + inverse-wall) in JAX with
   custom implicit rule; gradient vs central differences AND vs GENO
   on one TOC case.                                              (wk 2-5)
   [DONE AND EXCEEDED — S5 planar 52/52 + S8 axisym/shock/interop
   twin; GENO comparison = file-exchange brick done; O3.4 flowfield
   leg CLOSED S10 ([X-GENOXC] PASS, see gate G0 — stale "blocked"
   clause corrected S14, W2 of PAN-S14); the gradient leg of O3.4
   lands with the A1 engine.]
3. RaoPlug S1/S2 fix in GENO + Rao 1961-spike Table-1 oracle
   (M_E=2.4, theta_E=-8.25 deg, gamma=1.23 -> eps=3.81,
   X_D/R_E=1.164, C_F=1.58).                                     (wk 3-8)
   [NOT STARTED — prerequisite of OP-2/PB-2.]
4. Plug off-design jet-boundary march prototype (RK1 front-load). (wk 4-10)
   [NOT STARTED.]
5. CycleFamily v0 with the stage-A data contract + loud rejects;
   generators: matched-cycle (exists) + file-based.              (wk 4-8)
   [NOT STARTED as a module; contract pins of record in M0 VI.1/VI.4bis.]
   5-bis (S14, PAN-S14 F-FLAT arbiter): T0 FLATNESS MONITOR carrier —
   committed script + threshold DERIVED from the pattern-rotation
   tolerance / harmonic-decay audit (R5, no magic numbers) + rejector
   that fails on impure-mode data; X-carrier ID registered and
   T-T0/DIR-PERIODIC carrier fields pointed at it WHEN the script
   lands (not before — lint truthfulness). Experimental mode
   identification enters via case-C inputs only (piezo-census numbers
   = PRACTICE, external citation required).
6. Oracle harness: O1/O2 as executable tests BEFORE the optimizer
   exists (test-first).                                          (wk 6-10)
   [PARTIAL — T3/T4 oracles executable in suite groups (vi)/(x)/(xii);
   O3.1 dot-product executable at brick level (spikes); full O1/O2
   harness lands with the A1 engine.]
7. P-2 bridge-lemma draft (time-sensitive) + P-1 outline.        (wk 6-12)
   [DONE AND EXCEEDED — P-2 Lemma A/B drafts of record; P-1 skeleton
   + §2/§4 full text (see §3 stream).]
8. Kraiko 1979/PMM library pass commissioned.                    (wk 1-12)
   [PMM 2a done in-house; dispatch package ready, user send pending.]
[ADDED 2026-07-21 (S12) — the strengthening sequence of record:]
9.  Variational TOC brick (A1 brick 2: dJ/dSigma + TR-SQP + (**')/
    corner on the assembled march) — UNLOCKS O3.3 = P-2's numeric
    half; then P-2 submission-ready (modulo G5).
    [NEXT-1 since S11; THREE user-ordered deferrals declared
    (S12/S13/S14) — tag corrected S14 (W1 of PAN-S14): PROTECTED
    NEXT-1 for S15, no fourth deferral short of a gate failure.
    WAIVER EXERCISED 2026-08-04 (S15 log step 2): deferral #4 by
    explicit user order (deep-foundations campaign, axes A-D), RK-A
    cited; compensating controls declared (O3.3 protocol stays
    pre-registered; preprint decision stays armed with the user;
    re-adjudication at campaign end). The kickoff duties below are
    UNCHANGED and waiting.
    RE-ADJUDICATED 2026-08-06 (S17 log step 3, campaign end reached —
    S15+S16 [RIGOR/A] queue exhausted; compensating controls i-iii
    verified held): VERDICT = deferral #4 EXPIRED, BRICK 2 STARTED in
    S17 with the kickoff duties below binding BEFORE optimization,
    plus the S16 addition to the THERMOTAB duty (EOS G > 0 audit on
    the state box — ledger c4 channel). RK-A re-weighed at the same
    step (risk grew during the waiver; mitigation resumes with the
    brick; preprint decision re-presented to the user, lock
    unchanged). Any further deferral would need a NEW explicit user
    order with RK-A re-weighed.
    Honest both ways: the deferred brick lands RICHER (corrected
    O3.3 bench (30)/(31)+f2, pre-registered norms P2_outline §5,
    RK-G topology policy, X1 capturing control design). KICKOFF
    DUTIES bundled: quantified loop-speed falsifier threshold
    (clean-host protocol, S9 lesson) + scan/vmap column architecture
    (the restructure IS brick-2's architecture, not a retrofit) +
    RK-G trust-region/re-record policy + THERMOTAB C^1 duty (S14
    addendum, two-lens confirmed: the pin declares accuracy floors
    only, but C-D25U wants C^1 coefficients and the live carrier
    interpolates cp INDEPENDENTLY of h with piecewise-linear
    jnp.interp — cp != dh/dT between knots, Jacobian jumps at knots;
    fix at kickoff: C^1/Hermite-monotone interpolant class +
    consistency invariants (cp = dh/dT, s0' = cp/T) within derived
    floors + rejector; node crossings under the RK-G one-sided
    policy).]
10. Gonzalez-Viana rung-2 reproduction (Phase-A2 note) + O5-LITE
    build with the three PRE-REGISTERED T3-QS predictions (Phase-A4
    note).                                              [days-scale]
    [S14 notes: implementation basis of record = Morris JPP 21(3)
    p. 531 exit-BC (Poinsott-Lele MOC; choked/supersonic interior-
    determined, subsonic Pa, reverse-flow inflow) + unstart check
    (W3 of PAN-S14). Interim anchors relabeled of record: "PDE
    SINGLE-CYCLE falsification bench" (O-H/Morris/C-S/GV — zero RDE
    data; the bench licenses the corrector STRUCTURE, never hardware
    numbers: the bench's own model class is 20-28% off absolute Isp,
    O-H p. 335). Measurement-projection annex duty: P-ii is the only
    hardware-falsifiable prediction at realistic instrumentation;
    P-i/P-iii in-silico-only at +-3-4% stand accuracy.]
11. B-lite: G12-L1-3D symbolic brick, then the 3-D helical march
    demonstrator (Phase-A5 note).                       [after 9]
12. LITERATURE ACQUISITIONS (user upload to literature/, then a
    page-verify session): PRIORITY 1 Kraiko-Osipov PMM 34(6) 1970
    (P-1 wording contingency); PRIORITY 2 Giles-Ulbrich SINUM
    48:882-904 and 48:905-921 (2010) + Lozano "Watch Your Adjoints!"
    AIAA J 57(9) 2019 (P-2 cites, incl. the "near the shock" locus
    check); PRIORITY 3 Cooper-Shepherd JPP 24(1):81-87 (2008, year
    TO-VERIFY vs D2) + Owens-Hanson JPP 23(2):325-337 (2007) +
    Morris JPP 21(3):527-538 (2005). Optional: Ma-Choi-Yang JPP
    21(3):512-526 (2005); Kailasanath AIAA J 41(2):145-159 (2003);
    Ransom/Hoffman/Thompson 3-D MOC (to locate; B-lite).
13. EXPERIMENTAL ANCHOR line (ESA-review finding): name and acquire
    at least one PUBLIC RDE dataset (thrust/Isp/frequency with
    nozzle) as the case-C calibration target — the program currently
    validates against models (S-H 18/18) and code (GENO), never yet
    against test data; declared industrial gap #1.
14. COMPUTE PLAN note (ESA-review finding): census LES (Step 1) and
    the full A5 anchor need HPC access not currently evidenced;
    until secured, A4/A5 scope = O5-lite + B-lite (laptop-scale),
    DECLARED; industrial gap #2.
15. MU-INSTRUMENTS BUNDLE (S14, PAN-S14 addendum ME-5, two-lens
    confirmed; single session, BEFORE any case-C Verdict): (a)
    per-phase F(xi) profile + derived TV/W1 sensitivity bar in every
    Verdict (J is LINEAR in mu — the sensitivity report is free:
    |J(mu')-J(mu)| <= osc_xi(F)·||mu'-mu||_TV, or Lip_xi(F)·W1 on the
    smooth part + jump term); (b) empirical-vs-log-uniform drift
    metric (W1/KS in ln Pc) with threshold derived from the same bar
    — closes the T-O2 falsifier; (c) running-average convergence
    monitor for case-C data — closes the D-JEX falsifier; register
    the three carriers so the falsifier fields become true. Natural
    hook: the GV Table-8 mu-testbed already in A2.
16. LINT GROUP (xvii) — AUDIT-GREP CARRIERS (status: PROPOSED;
    PAN-S14 §8 residue item, two-lens verified 2026-08-05; dedicated
    session required for the mechanization itself): mechanize the
    registry's declared hand-run grep falsifiers (census at kickoff;
    today at least DIR-GAMMA "lint/audit grep", carrier: [], and
    DIR-THERMOTAB "audit grep") as an executable suite group (xvii),
    then point the corresponding carrier/falsifier fields at it so
    those rejectors can fire in CI — same closure pattern as item 15
    (ME-5).

------------------------------------------------------------------------------
## 7. Risk register deltas (vs roadmap)

RK-A (new): P2' scoop risk — Lozano-Ponsin 2025 built the 2-D adjoint
  bank; mitigate by fast-tracking P-2.
  [S14 annotation (W1 of PAN-S14, two-lens verified): PARTIALLY
  REALIZED — the declared mitigation was contradicted in fact by
  three consecutive user-ordered preemptions of item 9 (the brick
  that unlocks P-2's numeric half); deferral count now carried on
  item 9, which is PROTECTED for S15. The characteristic-
  compatibility bank (Peter-Desideri 2022, Ancourt 2023, L-P 2023)
  is now MANDATORY-CITE, sharpening the same risk.]
RK-B (new): quadrature-switch neglect — silent O(1/N) degradation +
  noisy outer gradients; mitigate: switch localization is a REQUIRED
  feature of the cycle layer, with a test that detects an unsplit run.
RK-C (new): data-contract violations from URANS/experimental profiles
  (Crocco inconsistency); mitigate: projection-to-manifold with declared
  norm, or reject.
RK-D (carried): plug off-design march (RK1), autodiff-through-iteration
  (RK2), multi-D shock calculus boundary (RK3, declared), mode-measure
  scarcity (RK4), bus factor (RK5), URANS scope creep (RK6).
RK-E (new, S12): NO experimental anchor yet — all validation is
  model/code-level; mitigate via 90-days item 13 (public dataset as
  case-C target) before any industrial claim.
RK-F (new, S12): compute for census/A5 unfunded — mitigate via the
  B-lite/O5-lite laptop-scale scope (items 10-11) and a declared HPC
  plan before A4/A5 full scale (item 14).
RK-G (new, S14; PAN-S14 F-TOPO, two-lens convergent): MARCH-TOPOLOGY
  NON-DIFFERENTIABILITY — the march DAG (cell counts, void rows,
  shock-cell identity, chord-foot branches) depends on the design;
  AD gives one-sided gradients at DAG re-record boundaries (fixed-
  march-topology hypothesis now NAMED in Lemma B §4.1; instance =
  [X-A1IM] frozen Sched replay). Brick-2 policy: fixed topology
  within a trust region + re-record on step acceptance + kink
  detection (reject when predicted-vs-actual reduction degrades
  across a re-record). Distinct from RK-B (xi-quadrature switches)
  and RK-D/RK2 (AD-through-iteration); cross-links the existing
  Clarke/proximal-bundle machinery (tool matrix; general_scheme row E
  "between topology events").

------------------------------------------------------------------------------
## ANNEX B — Input taxonomy for the CFD-free design tool (rde-lecture-code
##            as the predictive front end)

Every admissible input maps to a DECLARED CycleFamily generator with its
rigor class; the downstream machinery is identical (the measure
formulation's payoff). Cases, by input richness:

| Case | Input | Generator | Interface | Active channels | Verdict class |
|---|---|---|---|---|---|
| A | specs only (propellant, φ, mean pressure, annulus geometry, Pa) | Cantera CJ/HP → S-H matching → exponential blowdown → (P0,T0,γ)(ξ), μ log-uniform | I3 | N1, N2, N4 (NOT N3) | fully predictive; fixed full-flowing bell = Rao-at-⟨Pc⟩ BY THEOREM (H-T3.3 holds by construction at I3) — the tool states it, does not rediscover it; added value = N1 (temporal dual-bell), N2 (truncated plug/duty split), γ_eff |
| B | A + wave-structure model (non-CFD) | per-phase profile generator: Fievisohn-Yu-class shock-fitted combustor MOC, or CJ + Taylor fan + oblique-shock chain → M_in(y;ξ), θ_in(y;ξ), s(y;ξ) | I2 | + N3 (first-order breaker) | the full CFD-free tool; profile generator = the ONE new physics module, validated once against reference data, then standalone |
| C | A/B + partial experiment (pressure traces, thrust, f, n) | calibration: PR, Ω_w, n; measured waveform → EMPIRICAL μ | I3/I2 calibrated | as A/B with true μ | sensitivity-to-μ reported (exponential vs measured) |
| D | + mission profile Pa(t) | product measure μ_cycle ⊗ μ_trajectory (T3 Corollary-2 duality: Pa and Pc enter alike) | ×mission | + altitude dual-bell channel | full-flowing bell collapses to design at (⟨Pc⟩,⟨Pa⟩) by theorem; separation breaks both averages jointly |
| E | + throttle envelope | mixture measure Σ w_i μ_cycle(point_i) | nested | all, wider μ | one contour over the operating envelope, weights declared |
| F | + declared uncertainty (waveform, PR, mode count) | Wasserstein-DRO ball around nominal μ; mode measure π from operability maps | robust | + PB-5 | robust Σ* (E_π/CVaR); the honest formulation under mode-hopping |
| G | + chamber-coupling request | differentiated reduced response map Σ → (PR, fill, Ω_w) from the matched-cycle chain; stage-G loop, q measured (cheap: chain is analytic) | weak-I0 | + coupling | q in the Verdict; choked annulus ⇒ q ≈ 0 except unchoked tails (margins 0.97/0.65 documented) |

Invariants across all cases: stage-A audits apply to GENERATED data too
(a generator emitting off-manifold data is a generator bug); T3/T4
oracles always on; bound ladder computable from any family at any level
(J_ideal is post-processing); O(St) bar from the family's own harmonics.
Build status: case A = assembly of existing validated pieces (Cantera
chain + Table-1 + closed forms; RaoPlug S1/S2 fix prerequisite for plug
cases); case B = the one new module; C-G = light wiring on the measure
formulation.
