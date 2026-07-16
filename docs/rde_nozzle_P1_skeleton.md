# P-1 SKELETON — Cycle-averaged variational nozzle design for rotating
# detonation engines: exact steadification, a collapse dichotomy, and
# certified bounds (paper skeleton of record)

Status: PAPER SKELETON OF RECORD (2026-07-16, [F1/P-1]). Target venue:
JPP class (Journal of Propulsion and Power) per D6 §3. SUBMISSION
GATED: milestone M1 (D6) + gate G5 (Kraiko-1979/PMM human pass) — the
writing is not. Sources of record: M0 (all theorem statements + proofs;
in conflict, M0 wins), D3 (rigor ledger, §10quater), D2 (citations,
§b0 corpus), D4 (novelty verdicts), D7 (declared biases B1/B2).

Rigor legend as in M0: THEOREM / THEOREM* (within a declared closure) /
SCHEMA / CONJECTURE / PRACTICE. Every claim in this paper carries a
class, a falsifier, and an EXECUTABLE IN-REPO CARRIER (test group of
tests/run_all.py and/or persisted data of record). Zero orphan claims:
the claim map (§CM below) is the acceptance checklist for every draft
iteration.

NON-NEGOTIABLE SCOPE DISCIPLINE (D3 §10quater(5) + M0 D2.6/Prop. 7
SCOPE — enforced by coherence grep at every draft pass): the phase
diagram of §7 ranks CLOSURES (value models) at equal eps_max, NEVER
hardware sectors of the constrained problem (P); the released capped
plug IS the per-phase relaxation, so its dominance prices the
ADAPTATION PREMIUM only; the topology of the optimum S*(c) is the
OUTPUT of the finite sector tournament at the true constraint vector;
bell-winning regions of (P) are EXPECTED at contour level;
premium_bound is the certified tournament device. No sentence of the
paper may read a diagram winner as a hardware verdict.

------------------------------------------------------------------------------
## 0. Paper metadata

- Working title: "Cycle-averaged variational nozzle design for rotating
  detonation engines: exact steadification, a collapse dichotomy, and
  certified performance bounds".
- Type: full paper (methodological formulation + first certified
  quasi-1D results). Companion relation: P-2 (bridge lemma) can precede
  and be cited as companion (D6 §3).
- One-sentence pitch: the field's universal practice — design the RDE
  nozzle on the time-averaged flow — is derived, priced, and bounded:
  exact where a theorem says so (T3), replaced by the peak design where
  another says so (T4), and certified everywhere else by an executable
  bound ladder.
- What the paper does NOT claim: no contour-level topology verdicts
  (OP-11 remains CONJECTURE); no 3-D swirl transfer of Rao machinery
  (open, N6); no unconditional global optimality (excluded by theorem —
  M0 Part IV); no finite-rate chemistry closed forms (Hoffman boundary).

------------------------------------------------------------------------------
## §1 Introduction (class: expository; every historical claim cited per D2)

 1.1 The problem: an RDE feeds ONE fixed nozzle with a periodic family
     of states; classical variational contouring (Rao 1958; Guderley-
     Armitage; Kraiko school 1982-2007) assumes ONE steady state.
     Current practice: average-then-design, or CFD sweeps.
 1.2 Prior art to be contained, not competed with: the EAP metric
     (Kaemming-Paxson AIAA 2018-4567) and the Stechmann-Heister-Harroun
     performance model (JSR 56(3):887-898, 2019) — both are shown in
     §8 to be instances/coordinates of the present formalization.
     Mandatory citation list per D4/D2 (Efremov-Kraiko 2004,
     Kraiko-Egoryan 2020, Li-Xu-Huang JPP 38:849 2022, Paxson AIAA
     2022-4107, Giles-Pierce JFM 2001, Lozano-Ponsin 2025, ...).
 1.3 Contributions (each pointing to its section + claim-map row):
     (a) the thrust definition chain for periodic engines (Theorem 0);
     (b) exact steadification of the single rotating mode (T0);
     (c) the collapse dichotomy (T3 fixed wall / T4 free boundary) with
         full proofs and sharpness;
     (d) the weighted averaged optimality system (**');
     (e) a geometry-free, topology-free certified ceiling with the
         SONIC-CAP correction to naive complete expansion;
     (f) the executable eps-level phase diagram with closure semantics
         and the premium_bound tournament device;
     (g) an executable certificate culture: every claim ships with a
         falsifier and an in-repo carrier (rejector tests).
 1.4 Novelty statement, QUERY-BOUNDED (class: QUERY-BOUNDED; falsifier:
     any surfaced prior statement, incl. the pending G5 PMM/Kraiko-1979
     human pass — declared in the paper as residual due diligence).
     Wording per D4: every component is prior art in isolation; the
     constructive certificate-bearing composition is unpublished as of
     the 2026-07-16 six-strand query set (D2).

------------------------------------------------------------------------------
## §2 The objective: from wall force to phase integral (Theorem 0 + O1/O2)

 2.1 Definitions: F_wall, control-surface flux, storage term; the
     mean-equality claim <F_wall> = <F_S> for every fixed S.
     Class THEOREM (proof = M0 Theorem 0, reproduced in appendix A1).
     Falsifier: none needed (exact identity under bounded periodic
     momentum); the DECLARED CHOICE (mean as mission objective) and
     the two-unsteadiness distinction (storage vs O(St)) stated
     verbatim from M0 to preempt the standard confusion.
 2.2 The ONLY approximation: the quasi-steady per-phase factorization,
     O(St), priced by the P4 corrector (stated as outlook; class of
     the O(St) statement: SCHEMA with declared bar; falsifier: O5
     unsteady-sim oracle, Fase 4). Carrier today: quasi-1D identity
     tests (run_all group (ii)).
 2.3 O1 objective equivalence (Isp vs J at frozen choked feed):
     class THEOREM; hypotheses H-F1 + H2 explicit; failure channels
     N-O1± declared. Falsifier: bilevel coupling / unchoked tails.
     Carrier: the mdot·c* = Pc·A_t pivot is exercised by the in-repo
     S-H Table-1 validation (18/18) and group (ii).
 2.4 O2 log-uniform measure for exponential blowdown: class THEOREM;
     measure-agnosticism remark (any measured cycle replaces mu).
     Carrier: measure generator in src/thrust/st_core.py (blessed
     cycles data), group (v) golden numbers.
 2.5 Design interface contract Gamma_d (I0-I4 ladder, R1-R3): stated
     as the paper's data contract (class: definition + PRACTICE
     audits; carrier: stage-A audit fields in data of record).

------------------------------------------------------------------------------
## §3 Exact steadification (T0 strengthened) and its limits (N-SW)

 3.1 T0(i)-(iii): instantaneous thrust CONSTANCY for a single rotating
     mode; wave-frame equality; frame-force closure. Class THEOREM
     (proof = M0 Theorem 3, appendix A2). Falsifier/diagnostic:
     thrust-trace flatness = executable mode-purity monitor (N-T0';
     class PRACTICE, carrier pending Fase 4/5 data — declared).
 3.2 The CAUTION of record: T0 steadifies the PROBLEM, it does NOT
     transfer Rao's 2-D closed-form machinery to 3-D swirl (N6 open).
     Class: declared negative scope (prevents over-claim).
 3.3 N-SW lemma: axial spacelikeness u_x > c frame-invariant; CJ
     surface = causal firewall; consequence: rung-3a is an implicit
     BVP, no axial MOC. Class THEOREM (proof = M0 Lemma 4).
     Falsifier: none (elementary chain); role: licenses the data
     interface and locates coupling channels.

------------------------------------------------------------------------------
## §4 The collapse dichotomy (the paper's core)

 4.1 T3 (fixed wall): J[Sigma] = F[Sigma; <Pc>_mu] POINTWISE under
     H1-H4; cycle-optimal fixed wall = classical contour at mean
     pressure. Class THEOREM (proof = M0 Theorem 5 with Lemmas A/B/C,
     appendix A3; Lemma A holds across transversal shocks and for
     gamma(T); Lemma B dies for gamma(T) — the collapse boundary).
     Falsifiers (executable): O1 oracle — any ensemble machinery run
     under H1-H4 MUST return Rao-at-<Pc> with Delta-Isp = 0; the
     wrong-averaging rejector (naive averaging of optima vs optimum of
     average). Carriers: run_all groups (vi) (averaging
     discrimination) and (ii) (blowdown -> steady CP identity).
 4.2 Altitude-duality corollary (Pa linear => trajectory-averaged
     design collapses to <Pa>): class THEOREM (corollary C2);
     positioning remark vs dual-bell literature (separation breaks
     linearity). Carrier: same affinity algebra as (vi).
 4.3 Sharpness of T3: two-gamma counterexample (closed form); the
     first-order gamma_eff = <Pc gamma>/<Pc> closure with SECOND-ORDER
     design penalty (envelope theorem). Class: counterexample THEOREM;
     closure numbers of record: gamma_s 1.1537->1.2093, eps* shift
     -0.56%, Isp penalty -0.00028% <= shift^2. Falsifier: the gamma
     probe rejector (the unweighted-mean class -2.39% IS test-rejected).
     Carrier: run_all group (ix), data/gamma_cycle_probe.json.
 4.4 T4 (free boundary): per-phase argmax sets nested half-lines;
     max Int = Int max attained by the PEAK-phase untruncated plug.
     Class THEOREM* (ideal-adaptation closure DECLARED; precedent duty:
     the closure is published as a BOUND for detonation cycles —
     Kraiko-Egoryan — cited next to it). Sharpness: length cap / base
     pressure / non-ideal adaptation break nesting STRICTLY => the
     truncated plug is the first genuinely averaged shape problem
     (PB-2, outlook). Falsifier: strict max Int < Int max under a
     binding cap. Carriers: run_all groups (vi) (knee/plateau) and (x).
 4.5 The dichotomy as explanation of practice: average-then-design is
     EXACT in the T3 class — the field's habit is a theorem, not an
     approximation; where it fails (free boundaries), the peak design
     replaces it — also a theorem (within its closure). This section
     is the paper's citable clarification (D6 §3).

------------------------------------------------------------------------------
## §5 The averaged optimality system (T7) and the weighted transversality (**')

 5.1 Stationarity structure (a) per-phase closed-form adjoint,
     (b) mu-averaged wall condition, (c) WEIGHTED endpoint
     transversality (**') = Int (dF/ds_E) dmu = 0 with factorization
     R(xi)·w(xi). Class SCHEMA (named gaps P3, G12 declared in the
     paper — honesty section). The naive unweighted average is WRONG
     outside the T3 class: stated as a boxed warning (this is the
     implementable form; D2 §b0 doctrinal point: ambient pressure
     enters ONLY through endpoint transversality).
 5.2 Executable reduction (quasi-1D, exit-area DOF): (b)-(c) degenerate
     to <p_e(xi)> = Pa, i.e. NPR(eps*) = <Pc>/Pa. Class THEOREM
     (in-repo Theorem 1). Falsifier: wrong-averaging rejector.
     Carrier: run_all group (vi).
 5.3 Pointer to P-2 (companion): per-phase closed-form adjoint = the
     bridge lemma (Rao/Kraiko ≡ closed-form adjoint characteristics);
     here only the assembly into (**') is used.

------------------------------------------------------------------------------
## §6 Certified bounds: the sonic-capped ceiling and the OP-0 ladder

 6.1 Prop. G-B: J[S] <= J_ideal for ANY solid set in ANY topology
     (choked frozen feed). Class THEOREM (proof = M0 Prop. 7,
     appendix A4). Comparison: Efremov-Kraiko 2004 integral-flux
     relaxation (weaker published bound, cited).
 6.2 THE SHARPENING OF RECORD (a paper contribution in itself): naive
     "complete expansion to Pa" is NOT a bound below the critical
     pressure ratio — the per-streamtube ceiling must be CAPPED AT THE
     SONIC STATE; executable counterexample gamma = 1.15, Pc/Pa = 1.3,
     dCF = +0.0070. Every statement in the paper carries the cap or
     the explicit "min-cycle NPR >= critical" hypothesis. Class
     THEOREM. Falsifier: the four subcritical Table-1 rows REJECT the
     naive form (choke_margin < 1). Carrier: run_all group (viii),
     src/thrust/bounds.py, data/bounds_ladder.json.
 6.3 The ladder: bell <= int-max == capped ideal <= B_EK; dual-route
     agreement <= NQ·eps_mach; M1 duality-gap-zero attainment on the
     supercritical rows (numbers of record, 18 rows). Class THEOREM
     (executable). Carrier: group (viii) + data/bounds_ladder.md.
 6.4 EAP positioning (forward pointer to §8): J_ideal is the total-
     energy rung; EAP_i(axial) <= J_ideal(total) — two adjacent rungs
     of the same ladder.

------------------------------------------------------------------------------
## §7 The eps-level phase diagram (OP-11-eps) — closures, not hardware

 FIGURE: figs/phase_diagram_op11.png (90 cells, eps_max x PR at fixed
 <Pc>, CH4/O2 20-atm anchor + vacuum sweep; generated by
 src/thrust/phase_diagram.py; record data/phase_diagram.{json,md}).

 7.1 SEMANTICS FIRST (the section OPENS with the scope statement, D3
     §10quater(5) verbatim): winners rank VALUE MODELS (closures) at
     equal eps_max, NOT hardware sectors of the constrained problem
     (P) (defined in §7.0 below as the pair-(S*, delta) problem of
     M0 D2.6, summarized). The released capped plug IS the per-phase
     relaxation: its dominance PRICES THE ADAPTATION PREMIUM and is
     silent on how much of it real hardware retains (truncation, base
     pressure, length are invisible at the eps rung). Bell-winning
     regions of (P) are EXPECTED at contour level.
 7.0 The constrained problem (P) in one block: admissible set at
     constraint vector c, finite topology-sector decomposition
     (configurations = OUTPUTS), optimum = pair (S*, delta) with
     certified globality mechanism M1-M5. Class: definition (canonical
     form M0 D2.6); the paper's global-optimality contract.
 7.2 Statement (1): under the SONIC-CAPPED adaptation closure the plug
     family weakly dominates the fixed bell POINTWISE — no strict bell
     cell at eps level. Class THEOREM (eps-level closed forms).
     Falsifier: any strict bell winner cell. Carrier: run_all group
     (x), 22 checks + 8 negative controls.
 7.3 Statement (2): at eps_max >= knee the capped plug ATTAINS the
     capped ceiling — M1 gap-zero on EVERY Pa > 0 cycle INCLUDING
     subcritical cells (extension beyond OP-0's 8 supercritical rows;
     the supercritical hypothesis belongs to the NAIVE closure only).
     Class THEOREM. Carrier: group (x); knee table of record
     (data/phase_diagram.md).
 7.4 Statement (3), artifact of record: the PUBLISHED S-H spike closure
     is strictly suboptimal on subcritical tails and at eps_max = 1
     INVERTS the bell/plug ranking (executable artifact, test-
     rejected). Presented as a warning to users of the published
     closure. Class: executable counterexample. Carrier: group (x)
     negative controls.
 7.5 Statement (4), map structure: tie region {PR=1} u {eps_max=1} u
     {eps_max <= eps*(Pc_min)}; capped-plug band (the genuinely
     averaged regime — PB-2's section); M1 region. Duty split NOT
     expressible at eps level: OP-11 at contour level remains
     CONJECTURE (stated in those words).
 7.6 The tournament device: premium_bound = Isp_ideal(capped) −
     Isp_bell per cell (class THEOREM up to the bell surrogate's C4
     bar; max 64.7 s at PR = 90, eps_max = 1 on the anchor): any
     certified non-bell sector loss band exceeding it closes that cell
     for the bell with a delta-certificate per D2.6(iv). This — not
     the winner colors — is what the diagram contributes to (P).
     Carrier: premium_bound field persisted in data/phase_diagram.json
     + its rejector in group (x).
 7.7 Proven limits framing the map: PR = 1 column = T3 tie; eps_max >=
     knee = T4/M1; vacuum sweep = no finite optimum (eps is a
     specification, not an optimum — vacuum area ratios in the S-H
     Table 1 are correctly reported by them as "maximum values used").

------------------------------------------------------------------------------
## §8 Bridges: the formalization contains the field's metric and model

 8.1 EAP (Kaemming-Paxson 2018, full text verified): EAP_i is the
     PRESSURE-COORDINATE of J_ideal (their Eqs. 1-8 mapped term by
     term); their "area average = time average" is T0(i) used tacitly,
     proved here; their unstated quasi-steady + decoupling hypotheses
     are D1+D2, priced by P4; the bound gap J_ideal − J(Sigma*) is the
     honest discount on advertised pressure gain (Paxson 2022: real
     truncated plug at 58-70% of notional ideal). Class: THEOREM-link
     identification (textual falsifier: their Eqs. 1-8; executable
     carrier: the axial-vs-total rung distinction lives in
     src/thrust/bounds.py ladder).
 8.2 S-H (JSR 2019, spec + in-repo 18/18 Table-1 validation): their
     Eq. (4) ≡ O1; their F(t) ≡ the rung-2 proxy (Theorem 0 = their
     missing license, P4 = their missing bar, answering their own
     flagged open item); their assumptions map 1:1 to the hypothesis
     ledger; THEIR THREE NUMERICAL FINDINGS ARE INSTANCES OF THE
     THEOREMS (Fig. 9 bell optimum unchanged = T3; Figs. 10/12 spike
     knee/plateau sized by the peak = T4; Table-1 vacuum note = the
     vacuum theorem). Quantitative convergence check of record:
     bell 3-5%, spike 6-14% at fixed phi (exactly the warranted level;
     the full-fidelity joint (phi, eps) reproduction is the in-repo
     18/18 validation via certified phi_opt lattice x closed-form
     bell_opt). Class: THEOREM-link + executable check. Falsifier:
     closed-form predictions vs their Table 1 beyond the phi-fixed
     tolerance. Carriers: groups (ii)/(v) + validation records
     (data/st_opt_validation.md).
 8.3 phi placement (preempts a referee objection): phi is an OUTER,
     non-variational parameter of the DATA GENERATOR — nested
     max_phi max_Sigma J, T3/T4 valid at each fixed phi; not the
     bilevel PB-4. Class: definition + certified lattice carrier
     (phi_opt strict-neighbor certificate).

------------------------------------------------------------------------------
## §9 Discussion, declared limits, outlook

 9.1 What is proven vs what is conjectured: OP-11 contour-level
     CONJECTURE (duty split needs more DOF than eps); P3/G12 rigor
     gaps named; S1 canonicity conditional across shocks (D2.5
     wording); finite-rate chemistry = Hoffman boundary (corner dies,
     E = 0 residual — pointer to P-2).
 9.2 Generality ladder (M0 Part V table, condensed): what each flow
     class licenses; honest refusal for chaotic regimes.
 9.3 Declared exposition biases (D7 §5): B1 (schedule) gated by G4;
     B2 (exposition) — the paper derives the pipeline from the bare
     problem, not from the repo's history.
 9.4 Outlook: PB-2 truncated plug (first genuinely averaged shape
     problem) armed by premium_bound + empirical truncation bands;
     P-2 companion (adjoint bridge); P4 corrector (the O(St) bar).

------------------------------------------------------------------------------
## Appendices

 A1 Theorem 0 proof (from M0). A2 T0 + N-SW proofs. A3 T3 proof
 (Lemmas A/B/C + sharpness). A4 G-B proof + sonic-cap sharpening +
 M1 corollary. A5 T4 proof. A6 (**') derivation sketch + quasi-1D
 reduction. A7 Reproducibility statement: every number in the paper
 maps to a committed script + rejector test (tests/run_all.py groups
 (i)-(x)); data of record listed with hashes at submission time.

------------------------------------------------------------------------------
## §CM — CLAIM MAP (acceptance checklist; zero orphan claims)

| # | Claim (paper §) | Class | Falsifier | Executable carrier (in-repo) |
|---|---|---|---|---|
| C1 | <F_wall> = <F_S>, storage exactly zero in mean (§2.1) | THEOREM | — (exact identity; hypotheses declared) | proof A1; quasi-1D identity group (ii) |
| C2 | Quasi-steady factorization error is O(St), the ONLY approximation (§2.2) | SCHEMA (priced) | O5 unsteady-sim oracle (Fase 4) | declared bar; group (ii) as St->0 instance |
| C3 | O1: argmax Isp = argmax J at frozen choked feed (§2.3) | THEOREM | bilevel coupling / unchoked tail (N-O1±) | pivot exercised by 18/18 S-H validation + group (ii) |
| C4 | O2: blowdown measure is log-uniform in Pc (§2.4) | THEOREM | measured cycle replaces mu (agnosticism) | src/thrust/st_core.py generator; group (v) |
| C5 | T0: instantaneous thrust constancy, wave-frame equality (§3.1) | THEOREM | thrust-trace flatness diagnostic (N-T0') | proof A2; diagnostic = PRACTICE (declared pending) |
| C6 | No Rao-machinery transfer to 3-D swirl (§3.2) | negative scope (open N6) | exhibiting the transfer | — (scope statement) |
| C7 | N-SW: axial spacelike <=> u_x > c, frame-invariant (§3.3) | THEOREM | — (elementary chain) | proof A2; stage-A margin audits |
| C8 | T3 collapse: J = F[.; <Pc>] pointwise (§4.1) | THEOREM | O1 oracle (Rao-at-<Pc>, DeltaIsp=0); wrong-averaging rejector | groups (vi) + (ii) |
| C9 | Altitude duality: fixed bell collapses to <Pa> (§4.2) | THEOREM | separation breaks linearity (declared) | affinity algebra in group (vi) |
| C10 | Two-gamma counterexample; gamma_eff closure, 2nd-order penalty (§4.3) | THEOREM + numbers of record | gamma-probe rejector (unweighted mean IS rejected) | group (ix); data/gamma_cycle_probe.json |
| C11 | T4: peak-designed untruncated plug attains Int max (§4.4) | THEOREM* (ideal-adaptation closure, cited as K-E bound) | binding length cap => strict inequality | groups (vi) + (x) |
| C12 | (**') weighted transversality; naive average wrong outside T3 (§5.1) | SCHEMA (P3, G12 declared) | naive-vs-weighted rejector | group (vi) |
| C13 | Quasi-1D reduction: NPR(eps*) = <Pc>/Pa (§5.2) | THEOREM | wrong-averaging rejector | group (vi) |
| C14 | G-B: J <= J_ideal any topology (§6.1) | THEOREM | — (proof A4); vs E-K bound comparison | group (viii) ladder |
| C15 | SONIC CAP: naive full expansion not a bound subcritically (§6.2) | THEOREM | naive form REJECTED on 4 subcritical rows | group (viii); data/bounds_ladder.json |
| C16 | Ladder: bell <= int-max == capped ideal <= B_EK; M1 gap-zero (§6.3) | THEOREM (executable) | dual-route disagreement > NQ·eps_mach | group (viii); data/bounds_ladder.md |
| C17 | Phase diagram stmt (1): capped plug closure dominates pointwise, no strict bell cell (§7.2) | THEOREM (eps-level; CLOSURE ranking only) | any strict bell winner cell | group (x); data/phase_diagram.json |
| C18 | Stmt (2): M1 attainment at eps_max >= knee incl. subcritical (§7.3) | THEOREM | gap > 0 at any eps_max >= knee cell | group (x) |
| C19 | Stmt (3): published S-H closure inverts ranking at eps_max = 1 (§7.4) | executable counterexample | — (it IS the rejected artifact) | group (x) negative controls |
| C20 | Stmt (4): tie region structure; duty split not expressible at eps (§7.5) | THEOREM (structure) + CONJECTURE (OP-11 contour) | sector tournament at true c (Fase 3+) | group (x); data/phase_diagram.md |
| C21 | premium_bound = certified tournament device for (P) (§7.6) | THEOREM (up to bell-surrogate C4 bar) | certified sector band <= premium_bound closing a cell | premium_bound in data/phase_diagram.json + group (x) rejector |
| C22 | Vacuum: no finite optimum, eps is a specification (§7.7) | THEOREM | — (repo Theorem 3) | vacuum sweep in group (x); data/phase_diagram.md |
| C23 | EAP_i = pressure-coordinate of J_ideal; axial <= total rungs (§8.1) | THEOREM-link (textual) | their Eqs. 1-8 term match | M0 Part III remark; bounds.py rung split |
| C24 | S-H findings = instances of T3/T4/vacuum; 3-5%/6-14% check (§8.2) | THEOREM-link + executable check | closed-form vs Table 1 beyond phi-fixed tolerance | 18/18 validation; groups (ii)/(v); data/st_opt_validation.md |
| C25 | phi = outer nested generator parameter (§8.3) | definition + certificate | phi_opt lattice strict-neighbor failure | phi_opt certificate (in-repo) |
| C26 | Novelty of the composition (§1.4) | QUERY-BOUNDED (2026-07-16) | any surfaced citation; G5 PMM pass | D2 query record; G5 gate declared |

Acceptance rule for every draft: (a) each section names its class +
falsifier + carrier inline; (b) every claim appears in this map; (c)
coherence grep vs M0/D3 passes — no sentence reads a §7 winner as a
hardware verdict; (d) submission blocked until M1 + G5 (declared in
the cover letter if asked); (e) GAMMA STATUS (standing user directive
2026-07-16, STRENGTHENED same day): every claim declares whether it
holds for variable gamma / general EOS or requires gamma = const, AND
gamma = const may appear ONLY as a declared oracle instance or a
demoted corollary of the general statement — never as a load-bearing
hypothesis of a paper claim (the general form is primary: T7/(**') at
the adjoint level, EOS-general per-phase stationarity, V_id in
h(s, Pa) form; the T3 collapse and gamma_eff closure are presented as
the calorically-perfect corollary rung, with the two-gamma
counterexample stating why no stronger form exists) — of the map
above:
EOS-general given frozen homentropic flow: C1, C3-C9, C14 (V_id via
h(s, Pa), EOS-general); calorically-perfect-only: T3's Lemma B inside
C8 (declared boundary), the S-H closed forms carrying C15-C22 at the
eps rung and the corner<->eps bijection (E4 risk, oracle S-H 1971
Table 2 = gate G2); first-order repair where gamma varies per phase:
C10 (gamma_eff closure with certified second-order penalty).
