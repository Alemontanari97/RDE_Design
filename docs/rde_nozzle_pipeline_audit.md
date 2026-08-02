# Pipeline audit of record: per-step triple verdict (SOTA / general / correct) (D7)

Status: DELIVERABLE D7 (2026-07-16, closing audit). Granular pass over
every step of the assembled pipeline (D5 scheme + D5-Annex-A stages +
rung-2 machinery), each step judged on three axes:
  SOTA?    — is the tool/formulation the 2026 state of the art;
  GENERAL? — is the generality maximal, or maximal-with-declared-boundary;
  CORRECT? — is anything known to be fundamentally wrong.
Evidence base: line-by-line proof verification (D3), six-strand
web-verified survey (D2), 16-agent adversarial panel with double
refutation per proposal (D5), GENO-corpus page-verified read (D2 §b0),
and the in-session error hunts (§3 below).

VERDICT FORMAT: PASS = SOTA + generality declared + no known error.
PASS/D = PASS with a DECLARED residue (registered in §2, instrumented).

------------------------------------------------------------------------------
## 1. Per-step audit table

| Step | Content | SOTA? | General? | Correct? | Verdict |
|---|---|---|---|---|---|
| 0 | Problem definition (A_gen, S1+weak-strong canonicity, μ, J; ledger) | measure-theoretic objective + configuration-free admissible set: at or beyond published practice | maximal: sectors = outputs; ergodic definition on top | verified (O1, O2, sector decomposition SCHEMA declared) | PASS |
| 1 | Mode census / tier assignment (or data admission if profile given) | SAMR/LES + Koopman-DMD classification; data contract (Crocco, characteristic completeness, spacelikeness per phase) | tier ladder covers RE/RPO/multistable/chaotic; census re-run per accepted step (tier-flip detection) | census is PRACTICE (declared); contract loud-rejects | PASS/D (R1,R4) |
| 2 | Wave-frame steadification (T0) where licensed | freezing (Beyn-Thümmler) + phase condition: SOTA of equivariant dynamics | applied ONLY in H-A1 class; licensed, monitored (thrust-trace flatness = distance from steadifiability); C1-C4 condition hierarchy explicit | T0 proof verified incl. swirl audit (N-SW lemma: u_x > c frame-invariant; CJ = type/firewall only, licenses no marching) | PASS |
| 3 | Per-phase forward solve (S1, fitted inherited sheet) | shock-FITTED MOC / implicit shock tracking: the adjoint-consistent SOTA (Giles-Ulbrich negative theorem avoided by construction) | S1 membership certified a posteriori (Sternin/Rao-Beck monitor); outside S1 declared | classical well-posedness in determinacy domains; 2-D fitted-shock rigor = G12 SCHEMA, declared | PASS/D (R6) |
| 4 | Per-phase gradient (closed-form adjoint / reverse-AD) | closed-form adjoint = Rao/Kraiko (P2 three published banks); AD with implicit rules: SOTA | any S1 per-phase physics incl. nonuniform vortical (Kraiko generality) | exactness INSTRUMENTED/certifiable (O3 dot-product, Hoffman E-residual) [wording superseded S14, see E9] | PASS |
| 5 | Averaged optimality system + solve (T2, (**'), λ₂(ξ); B1 TR-SQP + B2 collocation; switch-split quadrature; sector tournament) | TR-SQP + Steklov-Poincaré metrics + deflated continuation + collocation: all SOTA | μ arbitrary; topologies = tournament; constraints active-set with marginal values | (**') correction adopted (unweighted (**) was the found error, fixed); Leibniz-at-switches verified; P3 rigor = SCHEMA declared | PASS/D (R5,R7) |
| 6 | Certification stack (KKT, 2nd order, dual-route, oracles T3/T4, DWR, bound gap M1-M5) | DWR + dual-route + duality-gap globality: at or beyond published optimization practice | globality mechanism DECLARED per result (M1-M5), incl. honest "within δ of global" | oracles are theorems (verified); certificates computable | PASS |
| 7 | Error bars (O(St) corrector; wave-frame anchor for D2; contraction q of data loop) | transfer-function corrector extends published linear/compact results; anchor = implicit BVP | quasi-steady license PRICED, never assumed; q measured never assumed | P4 = CONJECTURE with falsifier O5, declared | PASS/D (R8) |
| 8 | Robust/multistable outer layer (branch table, CVaR, DD-DRO) | CVaR (Kouri-Surowiec) + decision-dependent DRO (Luo-Mehrotra): SOTA, application new | J set-valued/discontinuous at mode boundaries handled honestly | μ estimation = PRACTICE declared | PASS/D (R4) |
| 9 | Chaotic tier | — | covered by bounds + robust surrogate ONLY | NILSS/shadowing correctly REFUSED (hypotheses fail across shocks) | PASS (honest refusal) |

------------------------------------------------------------------------------
## 2. Registry of declared residues (the ONLY non-theorem content, each instrumented)

| # | Residue | Class | Instrument |
|---|---|---|---|
| R1 | mode census is data-driven (LES/experiment) | PRACTICE | tier-flip detection; census refresh per accepted step |
| R2 | separation criterion (Summerfield/Schmucker class) | EMPIRICAL closure (N1) | pluggable criterion + sensitivity report; no rigorous alternative exists anywhere |
| R3 | base-pressure closure p_b (truncated plug) | EMPIRICAL closure (N2) | own adjoint + bracketing closures + URANS anchor |
| R4 | mode measure μ estimation | PRACTICE | DRO ball radius tied to sampling error |
| R5 | multiplier regularity λ₂ ∈ L²(dμ) (P3) | SCHEMA (open) | phase-wise constraint qualification route named; no obstruction known |
| R6 | multi-D fitted-shock shape derivative (G12) | SCHEMA (open for the whole field) | downstream certificates (O3, dual-route); 1-D theorem anchor |
| R7 | existence P7 | SCHEMA (target) | S1-margin monitor = failure boundary; restricted-class route named |
| R8 | O(St) expansion / Γ-convergence (P4/P4') | CONJECTURE | falsifier O5; T0 backstop |
| R9 | E4: corner theory for γ(T) | OPEN validation | Scofield-Hoffman Table-2 known-answer oracle (gate) |
| R10 | cellular-substructure regularization (wave-frame anchor) | MODELING | hybrid fit/capture + capturing-error audit + post-hoc DNS |

Claiming ZERO residues would itself violate the discipline: R2/R3 are
empirical for everyone (no rigorous separation or base-pressure theory
exists in the literature — verified); R5-R8 are the program's own open
mathematics, declared as contributions.

------------------------------------------------------------------------------
## 3. Fundamental errors FOUND AND FIXED this session (evidence the audit detects)

| # | Error | Where found | Fix |
|---|---|---|---|
| E1 | unweighted averaged transversality (**) presented as general | line-by-line verification | (**') weighted form; (**) = T3-class only |
| E2 | P1 "sensitivity ⟺ stability" biconditional | verification | P1a/P1b (degeneracy at neutral modes; stability = physical license) |
| E3 | "Rao applies verbatim in 3-D" | verification | weakened; N6 open |
| E4 | T1 labeled a theorem | verification | definition + conjecture (P4) |
| E5 | §5.1b measured numbers without committed script | asset audit | re-derive or strike (A0.3) — CLOSED 2026-07-16: re-derived in-repo, γ confirmed, ε* shift corrected −1.9% → −0.56%, penalty −0.001% → −0.00028% (D3 §5.2) |
| E6 | relative-Mach/spacelikeness conflation ("the sweep helps" for interfaces) | user challenge + granular re-derivation | N-SW lemma: u_x > c frame-invariant; C1-C4 hierarchy explicit |
| E7 | "Mo, Huang" citation conflation; Rao 1960/1961 dates; Sternin scope | survey b1/b2 | corrected of record |
| E8 | S1 canonicity via weak-strong uniqueness overstated for shocked solutions (theorem requires Lipschitz strong solution) | citation verification of Brenier-De Lellis-Székelyhidi CMP 305 (2011) during the convergence pass | canonicity downgraded: exact shock-free, declared-conditional across fronts (D1 §6, M0 D2.5) |
| E9 | step-4 "Correct?" cell read as executed certification: at this audit's date (commit of 2026-07-16 11:30) NO O3 script existed — "certified" named the certifying INSTRUMENTS of the design, not work done | S14 convergence panel (PAN-S14 F-D7DATE, arbiter-confirmed) | wording superseded in the step-4 row ("instrumented/certifiable"); status of record: O3.1 discharged at brick level (S8-op, 3.4e-12) and march level (S11, X-A1IM, 2.7e-10); O3.2 (Hoffman E-residual) + O3.3 (component match) PENDING under T-LEMA-iv/C-O33 — falsifiers of the A1 engine |

No further known-wrong item remains at the time of this audit
[time-indexed statement; the found-and-fixed register CONTINUES in
later sessions — S13 Lemma-B locus, S14 E9a-E9j of PAN-S14]. The
statement "nothing non-SOTA, non-general, or fundamentally wrong" holds
in its only rigorous reading: every step is theorem-grade or SOTA-grade;
every generality boundary is declared with its tier; every non-theorem
residue is in §2 with its instrument; and the error-detection process
has demonstrated nonzero recall (§3) under three independent
adversarial passes (self-verification, six-strand survey, 16-agent
red-teamed panel).

Standing external gates (not errors, but obligations before print):
G5 Kraiko-1979/PMM human pass; O5/G2/G3 empirical gates as the program
runs. RESOLVED 2026-07-16: Brenier-De Lellis-Székelyhidi weak-strong
citation VERIFIED (CMP 305:351-361 (2011), doi:10.1007/s00220-011-1267-0)
— and the verification IMPROVED the documents: the theorem's Lipschitz
hypothesis forced the canonicity claim to be downgraded to "exact
shock-free, declared-conditional across fronts" (D1 §6, M0 D2.5) —
error E8 of the found-and-fixed register.

------------------------------------------------------------------------------
## 4. The decision matrix: total vision of the alternatives per layer

For every mathematical decision point: the full candidate set
(classical + modern), the adopted choice, and what was rejected WITH
CAUSE. This section is the auditable form of "complete command of the
available tools".

| Layer | Candidates (classical → modern) | Adopted | Rejected, with cause |
|---|---|---|---|
| Solution concept | classical smooth (Courant-Friedrichs) · piecewise-smooth S1 (Li Ta-tsien, Majda) · entropy weak (Lax; convex integration) · measure-valued/statistical (DiPerna; Fjordholm-Mishra) · viscous (Feireisl; Plotnikov-Sokolowski) | S1 + weak-strong canonicity; statistical as roof definition; viscous as declared layer | pure entropy-weak as constraint (non-uniqueness = ill-posed J); pure viscous (inviscid limit uncontrolled, no periodic shape calculus) |
| Objective | instantaneous · finite-window average · ergodic/invariant-measure statistic · risk measures | ergodic definition on top; tiered exact/averaged reductions; CVaR where multistable | naive finite-window (protocol-dependent under hysteresis — instrumented instead via initialization protocol) |
| Time treatment | wave-frame steadification (equivariant/freezing) · HB/time-spectral · space-time periodic BVP, unknown (Ω,T) · quasi-steady averaging + two-scale/geometric optics · shadowing (LSS/NILSS) · Koopman/transfer operator | T0 where licensed; periodic BVP for RPO (2-D+t); quasi-steady with P4 price for rung 2; Koopman for CENSUS only | shadowing for design (hypotheses fail across shocks — unanimous); Koopman adjoints for design (no shape-gradient theory); plain HB with imposed frequency (Ω is unknown → LCO-style needed) |
| Shape calculus | Hadamard/velocity method (Murat-Simon; Sokolowski-Zolésio; Delfour-Zolésio) · shift-differentiability (Bressan-Marson; Ulbrich) · topological derivative · level-set/phase-field topology optimization | Hadamard on sectors + 1-D shift-diff anchors; sector tournament for topology | topological derivative (infinitesimal body in supersonic stream = pure wave drag → misleading germ); level-set topology change (unneeded: finite sector set, cone condition) |
| Optimality conditions | Rao/Guderley control-surface (classical) · Kraiko Lagrange formalism · Hoffman multiplier FIELDS · modern adjoint Euler (Giles-Pierce; Lozano-Ponsin) · reduced KKT | unified via P2 bridge: closed-form adjoint where S1, continuous/discrete adjoint elsewhere; averaged system with (**') | none — the unification IS the contribution |
| State/adjoint discretization | shock-capturing FV/DG · entropy-stable capturing · shock-fitted MOC · implicit shock tracking (HOIST) | fitted MOC per phase; HOIST-class for the wave-frame anchor; capturing DNS only for census/consistency checks | capturing for GRADIENTS (Giles-Ulbrich theorem: wrong adjoint limits) |
| Optimizer | reduced TR-SQP · full-space one-shot (LNKS) · nonsmooth bundle · deflated continuation · DIRECT/branch-and-bound · moment-SOS | TR-SQP + Sobolev/Steklov-Poincaré metric; bundle safeguard; deflation; certified B&B at 2-4 DOF | one-shot LNKS now (two immature solvers composed — deferred, not dismissed); moment-SOS (non-polynomial data, SDP scale explosion) |
| Existence | Chenais cone compactness · Γ/epi-convergence · relaxation (Young measures) · convexification (Buttazzo-Kawohl tradition) | Chenais per sector (P7); Γ-convergence for the St bridge (P4'); relaxation for BOUNDS only | relaxed "generalized shapes" as deliverables (answer a different question); symmetry assumed a priori (Newton-problem warning → P5 pricing instead) |
| Global optimality | duality/bound gap · monotone/unimodal structure · exhaustive stationary enumeration · certified global search · SOS certificates | M1-M5 ladder with per-result declaration | SOS (as above); "global by multistart luck" (never claimed as proof) |
| Averaging/two-scale | BLP/Allaire homogenization · Sanders-Verhulst averaging · weakly nonlinear geometric optics (Joly-Métivier-Rauch; Coulombel-Guès-Williams; Kilque) · Marble-Candel/admittance correctors | GO scaffold + admittance corrector for P4; O(1) amplitude declared open (G11) | classical homogenization as-is (wrong setting: coefficient oscillations, parabolic) |
| Wave dynamics/stability | Erpenbeck/Lee-Stewart normal modes · Evans function (Zumbrun) · Majda front conditions · Floquet · spiral-wave response functions · Koch-Kutz reduced models | Majda as P1 hypothesis; Evans/Arnoldi as operability monitor; Floquet as diagnostic; RFs as P1 precedent; reduced models for census | Floquet as path CONSTRAINT (essential spectrum, dense instability, fold nonsmoothness) |
| UQ/robust | weighted multipoint (classical practice) · expectation over measure (Huyse-Lewis) · CVaR (Kouri-Surowiec) · Wasserstein DRO (Dapogny) · decision-dependent DRO (Luo-Mehrotra) · worst case | μ-expectation as base; CVaR for tails; DD-DRO for μ(Σ) circularity | worst-case alone (vacuous under mode multiplicity without a measure) |
| Physical closures | separation criteria (Summerfield/Schmucker/free-interaction) · base-pressure models · frozen/equilibrium/finite-rate thermochemistry · ideal-adaptation bound · feed admittance BC | declared closures with own adjoints/bracketing (registry §2); frozen-composition per Scofield-Hoffman; ideal adaptation as BOUND (Kraiko-Egoryan precedent) | any closure used silently — the ledger forbids it |

Reading rule: a tool absent from the "Adopted" column is either in
"Rejected with cause" or was never applicable; there is no third,
silent category. Together with §1-§3, this closes the audit: the
pipeline contains no undeclared choice, no known error, and no
alternative that was ignored rather than weighed.

------------------------------------------------------------------------------
## 5. Inverse (de-biasing) audit: re-deriving the pipeline from the bare
##    problem, history removed

Exercise (2026-07-16, closing): state the problem nakedly (D2.6: find
(S*, delta) in the envelope under constraints, thrust-mean objective,
certified globality gap) and ask what a 2026 team with NO inheritance
(no Rao lineage, no S-H, no GENO) would build. Option space swept:
end-to-end differentiable simulation (killed: shadowing invalid across
shocks + Giles-Ulbrich capturing-adjoint theorem); ML surrogates/BO
(accelerator only: no certificates, truth still needed); direct 3-D
HB/time-spectral adjoint (contingency C1, gate G4: unknown frequency →
LCO treatment, mode discontinuities); wave-frame steady 3-D + bordered
adjoint (IN THE CORE, rung 3a — see bias B1); level-set topology
optimization (killed: supersonic infinitesimal germ = pure wave drag;
cone condition ⇒ finite sector tournament); metaheuristics/RL
(dominated); moment-SOS (killed: scale). Every elimination is by
theorem or verified fact, never by heritage. Surviving "classical"
components re-derive from scratch: MOC is the optimal S1 algorithm for
steady 2-D supersonic flow AND its adjoint has closed form (P2) — a
fresh team discovering that closed form would use it; the T3/T4
oracles are PROPERTIES OF THE PROBLEM (exactly solvable limits), and
any serious team would adopt them as rejection tests upon discovery.

DECLARED RESIDUAL BIASES (the honest yield of the exercise):
 B1 SCHEDULING BIAS (asset-driven, declared, gated): rung-2-first vs
    wave-frame-first for the single-mode class. A history-free team
    might lead with the exact steady 3-D wave-frame solve (no O(St)
    bar, no D2 residual; 2026-feasible at sector scale). Non-historical
    justification for the factorized engine: (i) per-channel
    attribution (N1..N4 one switch at a time) exists ONLY in the
    factorized reading; (ii) topology tournament + phase diagram need
    thousands of cheap evaluations; (iii) the O(St) bar must be
    computed anyway to judge the field's quasi-steady practice (EAP
    included). Architecture already contains the de-biased branch:
    gate G4 PROMOTES the wave-frame solve to engine if the D2 error
    dominates. Bias of schedule, not of architecture.
 B2 PRESENTATION BIAS: per-phase optimality exposed Rao-first
    (control surface, f2, corner) rather than adjoint-first —
    mathematically equivalent by P2; the P-2 outline adopts the
    adjoint-first double exposition for the modern reader.
No other historical imprint found under this pass. VERDICT: the
pipeline re-derives from the bare problem with modern tools; the
treatment is maximal-rigor in the D2.6 sense, forward AND inverse.
