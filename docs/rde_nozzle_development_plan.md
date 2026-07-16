# Development plan: from formalized idea to a formally optimal, certified methodology (D6)

Status: DELIVERABLE D6 (2026-07-16). Integrates and AMENDS
`docs/roadmap_geno_rde.md` (WP0-WP8, gates G0-G4) with everything this
session established: D1-D5, the corrected optimality system ((**')),
the bound ladder, the panel scheme and its refutations, the
prescribed-profile convergent pipeline (D5 Annex A), and the literature
gates. Where this plan and the old roadmap differ, THIS plan wins.

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
gamma_cycle_probe.py) is Action A0.3 below.

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
A0.1 Propagate D4 §6 fixes (Mo/Huang → Mo 2015 + Li-Xu-Huang 2022; S-H
     title; Rao 1960/1961 split; Sternin→Pirumov-Roslyakov caveat).
A0.2 Freeze D1 as the problem book of record; map every ledger row to a
     CI check where executable.
A0.3 Re-derive the gamma-channel numbers with a COMMITTED probe script +
     test, or strike them from all docs.
A0.4 OP-0: bound ladder at eps-level on the Table-1 states (S-H closed
     forms + ideal-adaptation bound + shared-wall relaxation). One
     module, one test, immediate value calibration of N1-N4.
A0.5 Human due diligence kickoff: Kraiko 1979 monograph TOC + PMM pass
     (library access); required before any submission (D4 §3).

### Phase A1 — Differentiable per-phase engine (months 1-6) [= WP1 amended]
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

### Phase A5 — Wave-frame anchor (months 12-22, parallel) [= WP5 + OP-5]
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
P-2 (TIME-SENSITIVE, can precede or accompany P-1): the P2' bridge
    lemma — Rao/Kraiko conditions ≡ closed-form adjoint characteristics;
    three published banks (Hoffman 1967; Giles-Pierce 2001;
    Lozano-Ponsin 2025) and no bridge; Lozano-Ponsin built the 2-D bank
    in 2025, so the identification is at risk of being scooped. Cheap:
    mostly assembly + the reverse-AD = adjoint-sweep statement + O3/E
    numerics from M1.
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

G0 (wk 4)   stack decision — criteria: gradient fidelity, loop speed.
G1 (M1+)    ORACLE GATE (absolute): O1/O2/O3 or no science.
G2 (M2)     VALUE GATE, now theorem-grade: bound-ladder gap per channel;
            gap < ~1% Isp on all of N1-N4 → pivot to certification/
            operability/duty-split value proposition (honest death).
G3 (M4)     UNSTEADINESS GATE: St|J1| large → rung-3 correction loop.
G4 (M5)     DECOUPLING GATE: D2 error dominates → wave-frame objective.
G5 (new)    LITERATURE GATE: A0.5 pass before any submission.
G6 (new)    DATA-CONTRACT GATE: any CycleFamily failing stage-A audits
            (Crocco, completeness, H-I2) is rejected loud — no design on
            inconsistent data.

------------------------------------------------------------------------------
## 6. First 90 days (concrete, amended)

1. A0.1-A0.4 (fix docs; bound ladder eps-level; probe script).   (wk 1-3)
2. G0 spike: ONE unit process (interior + inverse-wall) in JAX with
   custom implicit rule; gradient vs central differences AND vs GENO
   on one TOC case.                                              (wk 2-5)
3. RaoPlug S1/S2 fix in GENO + Rao 1961-spike Table-1 oracle
   (M_E=2.4, theta_E=-8.25 deg, gamma=1.23 -> eps=3.81,
   X_D/R_E=1.164, C_F=1.58).                                     (wk 3-8)
4. Plug off-design jet-boundary march prototype (RK1 front-load). (wk 4-10)
5. CycleFamily v0 with the stage-A data contract + loud rejects;
   generators: matched-cycle (exists) + file-based.              (wk 4-8)
6. Oracle harness: O1/O2 as executable tests BEFORE the optimizer
   exists (test-first).                                          (wk 6-10)
7. P-2 bridge-lemma draft (time-sensitive) + P-1 outline.        (wk 6-12)
8. Kraiko 1979/PMM library pass commissioned.                    (wk 1-12)

------------------------------------------------------------------------------
## 7. Risk register deltas (vs roadmap)

RK-A (new): P2' scoop risk — Lozano-Ponsin 2025 built the 2-D adjoint
  bank; mitigate by fast-tracking P-2.
RK-B (new): quadrature-switch neglect — silent O(1/N) degradation +
  noisy outer gradients; mitigate: switch localization is a REQUIRED
  feature of the cycle layer, with a test that detects an unsplit run.
RK-C (new): data-contract violations from URANS/experimental profiles
  (Crocco inconsistency); mitigate: projection-to-manifold with declared
  norm, or reject.
RK-D (carried): plug off-design march (RK1), autodiff-through-iteration
  (RK2), multi-D shock calculus boundary (RK3, declared), mode-measure
  scarcity (RK4), bus factor (RK5), URANS scope creep (RK6).

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
