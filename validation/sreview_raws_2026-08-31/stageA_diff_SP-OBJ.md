# STAGE A — DIFF JUDGEMENT, SP-OBJ (objective definition: what is optimized, what constrained, over which operating set)

S-REVIEW 2026-09-05. Judge = JPP referee ("why not X?") + PM ("shortest credible path"). NOT agnostic: the record was read
integrally at the anchors below. Trees read integrally: `stageA_tree_{variational,hyperbolic,optimization,propulsion}.md`
(V/H/O/P), the statement + brief, `INCUMBENT_pointers.md`, the 2026-08-17 condensed trees + `phaseB_tree_diff.md`,
`st_scoping_number_run.log`. Independence caveat LOG-4b applied: every convergence below is labelled DERIVED (argument /
lemma / cost estimate present in the tree) or NAMED (option listed without derivation); NAMED convergences weigh less.
No memory file was read.

## 0. Incumbent of record (SP-OBJ) — what is being judged

- **Objective form.** [D-JEX] M0:74-94: J_exact = lim_T (1/T)∫F_S dt on any enclosing axisymmetric surface, Pa constant;
  liminf/limsup fallback targets with the [S-GBE] upper wall (J_exact^+ ≤ F_env under bounded storage + axially-sonic
  exhaust, `rde_nozzle_GB_ergodic.md`); scope discharge inside the periodic pin ("no Birkhoff limits"). [D-MU] M0:95-110:
  rung-2 J[Σ] = ∫F[Σ; s(ξ)]dμ(ξ), μ = pushforward of cycle time; scope = pure periodic single mode; mode transitions
  routed to the robust layer (PB-5), never averaged.
- **Constraints.** [D-P] M0:260-286 + :286-408: c-slots L / L_p / eps_max as declared PROXIES for heat/mass (no flux-level
  thermal c-slot; upgrade path named); side load = declared SECONDARY OUTPUT, zero by theorem for n ≥ 2 ([T-SLRW]);
  per-phase STATE constraint g_sep(S; s(ξ)) ≤ 0 μ-a.e. ([D-GSEP], criterion class R2 declared empirical closure, active-set
  multiplier = marginal value of attachment; separated designs exit the certified class); (v) bars St|J1| + D2 + DWR are
  ESTIMATED indicators, not certified bounds (BAR-CLASS NOTE); (iv) globality via computed delta against the bound ladder
  (int-max, sonic-capped J_ideal, B_EK).
- **Objective domain.** [OBJ-DOM] adjudicated fix-A (panel-inclusive J_A from θ = 0), IMPL open; findings
  `variational-driver:objective-omits-throat-panel` (path critical, severity medium; gradient axis governs, 5.36e3 vs 9.3);
  decision map Stage 7 row; ship-gate armed for every (value, delta) row.
- **Operating set.** P_amb SLOT OF RECORD (problem book :553-575): default P_amb = {Pa0}; F affine in Pa on the
  ambient-blind class (H-T3.2) so ν-mean aggregation collapses to a point evaluation; envelope binds only through
  admissibility (g_sep, wake fence). Ledger C55 (aggregation form ν-mean / minimax / CVaR) = NEVER, owner "first multi-point
  instantiation" (adjudication owed at instantiation, not before). C59 (temporal form) = NEVER, scoped EMPTY inside the pin
  (cycle-average canonical). C62 (phase quadrature) = NEVER (uniform trapezoid practiced).
- **Where the lever lives, of record.** [T-T3] M0:746 ff.: fixed full-flowing wall under pressure-scaling similarity + phase-
  independent nondimensional inflow shape ⇒ J[Σ] = F[Σ; ⟨Pc⟩_μ] POINTWISE (cycle-optimal bell = classical contour at the
  mean pressure); [T-T4] plug optimal at peak; PB-2 truncated plug = first genuinely averaged optimum (problem book :529-534).
  D6 G2 (:776-778): "bound-ladder gap per channel; gap < ~1% Isp on all of N1-N4 → pivot to certification/operability/duty-
  split value proposition (honest death)"; calibration anchor = thrust-stand class 0.5-1% (note only). M0 EAP remark
  (:2526-2540): the bound gap J_ideal − J(Σ*) is the honest discount on advertised pressure gain; M0:2742-2747: the largest
  published performance lever is class-changing (constriction/choking/exit-area), outside what delta prices (CFD-1 core).
  F1b twin precedent (D6:152): +0.51% in-class on the bell, cert-limited. TWIN protocol §1-§6: truncated plug, case A, arms
  P vs C (I4 mean conditions), same μ, metric = cycle-averaged Isp, outcomes MATERIAL / SMALL / INTERMEDIATE /
  NON-CONCLUSIVE; no attachment-map output, no constraint-decisive outcome (grep attach|separat|g_sep = 0 hits).
- **Measured scoping number.** [X-STSC] PASS: bell St_n ∈ [0.347, 0.599] at the record head count (MARGINAL, corrector
  mandatory); plug class up to 1.415 (NOT defensible alone; wave-frame rung required).

**Adjudication class of the incumbent: MIXED.** The objective FORM (O-a mean thrust, single point, g_sep hard, O-d as
c-proxies) is DECIDED-constructional: panel-confirmed at S14 (D-JEX/D-MU "team/arbiter-confirmed" additions), re-derived
by the 2026-08-17 four trees (V FORK-3 "O1, robustness in the error-bar layer"; P FORK-4 "deterministic μ, separation hard"),
and now re-derived 4/4 by the 2026-09-05 trees (§1 row 1). The AXIS "is mean Isp at one operating point THE referee
question versus operability/robustness — and is the contour the engine's lever?" has NO ledger row: it is weighed OF RECORD
outside the ledger (G2 pivot clause, T3/T4/PB-2, EAP remark, M0:2742) at record grade — the C60/C61 pattern (weighed, no
C-row). C55 is NEVER by declared sequencing. Consequence for the panel recommendation: §4.

## 1. Table of approaches (every SP-OBJ branch of the four trees + the objective-changing level-0 roads)

| # | Approach (tree locations) | Lenses | Class | Weight on Q0 | Weight reason | Changes credibility / cost? | Record anchor |
|---|---|---|---|---|---|---|---|
| 1 | O-a time-mean thrust at ONE design point, g_sep per phase as HARD state constraint, O-d as geometric bounds, multipliers reported (V SP-OBJ rec + OBJ.1; H SP-OBJ (6) lexicographic; O OBJ.2; P OBJ.1) | V,H,O,P | CONFIRM-candidate (DERIVED 4/4: H "what a thrust stand measures"; O L5 feasible-set first-order + Euler blind to separation; P "only objective with an unambiguous comparator"; V referee scaling) | high | It IS the question Q1 sharpens; 4/4 independent re-derivation, each with grounds, after the 2026-08-17 4/4 | Credibility UP; cost 0 | D-JEX :74-94; D-MU :95-110; [D-GSEP] :270-286; c-proxies :260-265; D-P (ii) multipliers |
| 2 | Isp ≡ thrust when Γ_d is supersonic (ṁ is data); prefer thrust (no division by an audited quantity); if subsonic patches exist Isp must be used (V OBJ.2; H (2); O OBJ.5; P OBJ.1 parenthetical) | V,H,O,P | CONFIRM-candidate (DERIVED, one-line) | low | No change to the run; one increment: D-JEX does not say which of thrust/Isp is the objective on the subsonic case-class (D1 §4.3bis O1-O4) — TWIN §6 uses Isp normalized by metered feed | Credibility neutral; cost 0 | [T-TH0] L4 note M0:120-128 (ṁ-independence EXACT on the L4 default); TWIN §6 :89-90 |
| 3a | LEVER HONESTY + a VALUE GATE with a pre-registered negative and pivot (V S0.11 + OBJ decision criterion; H S12 / Stage-0 gate; O S13; P DL-2 + M-1) | V,H,O,P | CONFIRM-candidate (DERIVED 4/4, mechanisms differ) | high | The record's G2 pivot + bound ladder are re-derived independently; the trees insist the paper states the lever ordering UP FRONT (combustor 5-15% / configuration 5-20% / swirl 1-4% / contour 1-2%: [KNOWLEDGE] UNVERIFIED, no registry rows for Anand-Gutmark 2019, Sutton-Biblarz, Raman-Gamba 2023) | Credibility UP if the P-1 carries the lever table; cost 0 | D6 G2 :776-778; M0 EAP remark :2526-2540; M0 :2742-2747; D-P (iv) ladder |
| 3b | DIFFERENCE-SCREEN before building: a derivative-free bound on the maximal O-a advantage of ANY cycle-aware design over the mean-state design — O L2 Jensen gap 2·sup_A δ(S), δ = ½H(S)Var_w(u), K+1 steady solves; V δ_practice = (J_ideal − J_K.3)/J_ideal vs m; H unsteady-specific pool (Jensen + data-shock entropy) vs β_stand·F̄ | O (derived bound), V, H (derived screens on the absolute gap) | NEW for the DIFFERENCE bound (O L2); the absolute-gap screens are CONFIRM of the ladder | high | The record bounds the ABSOLUTE gap (ladder) and gives the difference EXACTLY ZERO on the bell (T3, H3); on the plug sector PB-2 gives only the SIGN ("max∫ < ∫max strictly"), not a size. A referee-checkable a-priori cap on the TWIN delta, at 0.116 s/solve × (K+1), converts "run and see" into "screen, then run". Caveat carried by O itself: L2 fails across events (shock-position jumps, separation onset) — exactly C62's event-stratification note and [D-GSEP]'s first-order feasible-set effect | Credibility UP (a-priori cap); cost DOWN (a dead TWIN is not run) | No record home for the difference bound; nearest: [T-T3] :746 ff. (zero case), PB-2 :529-534, C62 note, [R22F-FORCHETTA] (bracket on the 2D/3D gap, different axis) |
| 4a | O-c operability-primary as the PRE-REGISTERED PIVOT if O-a is unresolvable (V S0.12; H S8 "PRE-REGISTERED PIVOT"; O S10 / OBJ.3; P S-9) | V,H,O,P | CONFIRM-candidate (DERIVED: O L5 first-order feasible set; H L3 pool ~ band vs O(1) wall-pressure swing; P DL-2 + PCB-measurability) | medium | The record's G2 wording already names the pivot; the trees' ranking (never primary, always fallback, each with a reason) matches | Credibility UP; cost 0 | D6 G2 :778; [D-GSEP] N1 temporal dual-bell = active-set question; PB-5 |
| 4b | OUT-C CONSTRAINT-DECISIVE OUTCOME in the decisive pre-registration: |delta| small BUT arm C violates g_sep at some phase while arm P does not → the road's worth is operability, testable by kHz wall-pressure (P SP9 OUT-C; O SP9 "per-phase minimum attachment margin of both" as secondary metric; V S0.12 falsifier "practice design attached everywhere"; H S9 "(N) → pivot to S8") | P (derived), O, V, H | NEW | high | TWIN §6 has four outcomes (MATERIAL/SMALL/INTERMEDIATE/NON-CONCLUSIVE) on delta only; the attachment map of arm C on μ is NOT a registered output. Since g_sep is computed anyway ([D-GSEP] runtime detector), the outcome costs nothing and changes what the TWIN can PUBLISH either way; the P tree adds the artefact guard (arm C must be given the worst-instant attachment check, else OUT-C is rigged) | Credibility UP; cost ~0 | TWIN §6 :87-115 (absent); [D-GSEP] :270-286; findings twin-protocol:preregistration-2026-08-31 |
| 5 | O-b envelope-robust (mission Pa, throttle, mode weights) = SECOND paper, after the single-point verdict; classical practice already trajectory-averages (V OBJ.3/S0.12; H S10; O S9/OBJ.4; P S-8/OBJ.3) | V,H,O,P | CONFIRM-candidate (DERIVED by P: Hagemann 1998 mission practice → RDE-specific novelty small; O: needs D-F data; H: inherits the marginality of L3) | low | Matches C55's declared sequencing and the P_amb single-point default; F affine in Pa (record) makes the ν-mean collapse — no tree states the affinity, so the record is STRONGER here | Neutral; cost 0 | C55 (NEVER, owner = first instantiation); problem book :553-575; PB-5 |
| 6 | O-d cost / manufacturability as CONSTRAINTS not objective; Pareto front traced by the length multiplier (V OBJ.5/OBJ.6; O OBJ.2 bounds; P OBJ.5 composite rejected; H (5)) | V,H,O,P | CONFIRM-candidate (DERIVED by V: marginal thrust per unit length = (R-ii) multiplier) | low | Reporting device; record already has c-proxies + multipliers = marginal values | Neutral; cost 0 | D-P :260-265 (PROXIES), (ii) complementarity with multipliers |
| 7 | VACUUM objective (drop the Pa term) (P OBJ.2, named, not recommended) | P | CONFIRM-candidate-NAMED | zero | Not eligible for Stage B: record excludes Pa → 0 from (P) for existence (vacuum theorem, sup unattained, M0 :390-396); OBJ-DOM's Pa-drop claim is scoped to the vacuum objective only | — | D-P MAXIMALITY (a); [OBJ-DOM] :335-360 |
| 8 | ENGINE-LEVEL objective with chamber coupling (class G) named as THE lever the referee will ask about: back-pressure changes fill/wave count/pressure gain 5-20% (P S-10/OBJ.6 with [KNOWLEDGE] Fotia 2016, Bach 2020 — UNVERIFIED; O S12/OBJ.6; V S0.13(b)) | P,O,V | CONFIRM-candidate (DERIVED by P: magnitude ordering; O: coupling-derivative test) | medium | The record already says it (M0:2742-2747 class-changing lever; PB-4 bilevel; CFD-1 core) but the trees make it a MANDATORY sentence of the decisive claim ("the paper must say so up front"); P's numbers need [KNOWLEDGE] rows (Fotia 2016 = WANTED :1267, not read) | Credibility UP if stated; cost 0 | PB-4 problem book :540-545; M0 :2742-2747; D1 §4.3bis |
| 9a | CEILING as (R-i) gap certificate: H L4 J_ceil = ṁ√(2(⟨h0⟩_ṁ − h(s_min,Pa))) under H5 "axially-sonic exit surface"; V L0.3 per-stream-tube isentropic J_ideal | H,V | CONFIRM-candidate (DERIVED: H's H5 is the record's axially-sonic exhaust hypothesis; V's L0.3 is the per-tube J_ideal) | medium | Independent re-derivation of [S-GBE]/OP-0 sonic cap; H's wall is Jensen-looser than the per-phase wall exactly as M0:3016 states ("gap reportable") | Credibility UP; cost 0 | [S-GBE] M0:97-101, :3016; D-P (iv) ladder; `rde_nozzle_GB_ergodic.md` |
| 9b | TERM-BY-TERM LOSS BUDGET on the evaluated exit field (expansion p ≠ Pa / divergence / Jensen h0-spread / entropy s > s_min), exact decomposition of J_ceil − J[S]; V OBJ.7 exergy diagnostic "reported, not optimized" | H (derived), V | NEW (increment on 9a) | medium | The record reports the gap δ = B − J[S*], not WHERE the loss sits; the decomposition is the referee's "why not X" instrument and costs one pass over the exit surface | Credibility UP; cost ~0 | none (nearest: D-P (iv) delta; EAP remark) |
| 10 | UNSTEADY-SPECIFIC nozzle-side pool is band-order: H L3 rothalpy Jensen loss ≈ ε²/8 → 0.15-0.5% (scaling with ωr, Δu_θ, h0 numbers, CONJECTURE-grade); V "0.5-3% between competent contours"; P DL-4 "contour 1-2%" | H (derived scaling), V, P | NEW (no record NUMBER for the unsteady-specific pool; T3 gives zero on the bell; F1b +0.51% is the only measured datum) | medium | Sets the referee's prior that the decisive difference sits AT the band by construction — which is why the difference screen (3b) and the (v) budget must be first deliverables; numbers UNVERIFIED | Credibility UP (honest prior); cost 0 | [T-T3]; D6:152 F1b +0.51%; [X-STSC] |
| 11 | RDE THRUST-STAND REALITY: 1-3% thrust, 2-4% Isp (short hot runs, tare drift) ⇒ contour-level differences are NOT experimentally resolvable; the decisive number is COMPUTED with derived bands and the experiment ANCHORS THE EVALUATOR; configuration-level differences (5-20%) are resolvable (P DL-4, [KNOWLEDGE] Rankin 2017 / Goto 2019 / Fotia 2016 — abstract, UNVERIFIED: Goto/Fotia = WANTED rows, Rankin garble flag) | P | NEW (accuracy-class refinement) | high | TWIN §6 and D6 G2 pin "thrust-stand class 0.5-1%" as the materiality threshold AND as the external calibration anchor; if the RDE-stand reality is 2-4% Isp the CLAIM SHAPE changes ("computed, at/above experimental resolution, testable" — never "experimentally resolved") though the run does not. This is the referee's first question on the decisive number | Credibility: re-words the claim (protects it); cost 0 | TWIN §6 :94-96; D6 G2 note :779-782 |
| 12 | Side loads: only the first azimuthal harmonic contributes; zero for n ≥ 2 with n-fold symmetry; O-c "genuinely unsteady" while O-a is not (V L0.1 corollary; O L1(c); P SP2 rotating side force as proxy) | V,O,P | CONFIRM-candidate (DERIVED) | low | Re-derives [T-SLRW] side-load disposition (secondary output, zero by theorem for n ≥ 2); P's "reported as a proxy" matches the declared CVaR upgrade path | Neutral; cost 0 | M0 :266-275 [T-SLRW]; `rde_nozzle_side_load.md` §4 |
| 13 | Statistic of the cycle: deterministic μ with the weight sensitivity dJ/dw_k = F_k reported free (O L3 trivial theorem; V D.F; O SP9 sensitivity vector); robust μ only at the outer layer | O (derived), V | CONFIRM-candidate (DERIVED) | low | Record: D-MU deterministic μ + PB-5 routing; the dJ/dw Verdict line is a cheap increment (prior variational FORK-3 2026-08-17 already asked for it) | Credibility UP slightly; cost 0 | D-MU :95-110; PB-5; C62 alt. 4; findings :988 |
| 14 | LINEAR THRUST LAW kills the quasi-steady gain for choked, 1-D-inflow, constant-γ nozzles (P DL-2 THEOREM under closure); list of where the lever CAN live: supersonic interface / finite St / active attachment / unsteady base | P | CONFIRM-candidate (DERIVED; a strictly WEAKER special case of the record theorem) | high | Independent derivation of the collapse supports the record's choice of the PLUG sector for the TWIN; the record's [T-T3] is more general (frozen γ(T), transversal shocks, similarity + phase-independent inflow SHAPE), and P's "where it can live" list = record channels T4 / P4 corrector / N1 / N2 | Credibility UP; cost 0 | [T-T3] M0:746 ff.; [T-T4] :2294 ff.; PB-2; D1 §8 P4 |
| 15 | BELL-FIRST decisive configuration (no base band) with the plug CONDITIONAL on the base-band resolvability (V SP9; H SP9 "truncated plug EXCLUDED from the decisive run"; O SP9 DR.1 bell first; P both cases, plug with FIXED base) vs record TWIN = truncated plug | V,H,O (derived: base band ~ b_TS swamps the plug delta), P (fixed base cancels to first order) | DIVERGENT (3/4 on sector choice); CONFIRM on the mechanism (same closure object in both arms = TWIN §2) | high | The record is STRONGER by theorem on the sector (bell = T3 collapse ⇒ a bell-first decisive run is a pre-decided negative; F1b datum +0.51% in-class), which no tree has. But the trees' objection is REAL: the plug delta rides on C61 (base closure = NEVER, Veen WG10-FAILED, bracket [+19%, −15%], argmax moves ×2.45); TWIN §2 pins only "same object in both arms" (first-order cancellation), and the residual |D(p_b,+) − D(p_b,−)| over the C61 bracket is not in the pre-registered band stack | Credibility: conditional; cost: one extra band term (two re-evaluations) | TWIN §2; C61; PB-2; [T-T3]; SP-PB judge (deferred mechanism) |

Objective-level reading of the level-0 tuples (SP0 road families as they touch SP-OBJ): every top-ranked road (V S0.4,
H S11, O S7, P H-1) carries the SAME objective tuple entry — O-a exact under the pin, O-c per-phase constraint, O-d bounds —
and every tree ranks the objective-changing roads (O-c primary, O-b, class G) as fallback / second paper / referee-named
lever, each FOR A STATED REASON. That is a 4/4 DERIVED convergence on the incumbent's objective form and on the record's
pivot structure. The three genuinely new objective-level items are 3b (difference screen), 4b (OUT-C outcome) and 11
(accuracy-class reality); 15 is the one high-weight divergence and it is a sector/base question wearing objective clothes.

## 2. The three §G.3 questions, answered for SP-OBJ

**q1 — Is Q1 (the record's sharpening) the right sharpening of Q0 on the objective axis?** YES with two increments. The
sharpening "per-phase cycle-averaged design vs classical fixed design at identical constraints, on the truncated-plug
sector, mean Isp at one operating point, attached at every phase" is the objective every tree independently chose as THE
referee question (row 1, derived 4/4), and the record holds the theorem (T3) that tells WHY the bell cannot carry it and the
sign result (PB-2) that says the plug can. Increments the trees force: (i) the sharpening must be stated WITH the lever
ordering and the a-priori difference cap (rows 3a/3b) — a referee will not accept "mean Isp at one point" as THE question
unless the paper says up front that the contour is a second-order lever and shows the cap; (ii) the operability axis must
be a REGISTERED OUTCOME of the same run (row 4b), not only a gate wording. Neither increment changes the objective of
record; both change what ships with it.

**q2 — Does Q2 (the TWIN decisive number) answer Q0?** PARTIALLY, on the objective axis. Q2 answers Q0's (ii) on the
sector where the theorem leaves room — right by T3/T4/PB-2 — but three objective-level conditions are unmet in the
pre-registration as written: (a) no a-priori cap on delta (row 3b) — the referee can ask "could ANY cycle-aware design have
bought more than the band here?" and the record has only the sign; (b) no constraint-decisive outcome (row 4b) — the
SMALL branch (delta + band < 0.5%) currently ships as "the literature is right on this sector" even if arm C separates at
some phase, which would be the wrong headline; (c) the base-bracket residual (row 15) is not a named band term although the
sector was chosen precisely because of the base. Two further conditions belong to other judges but are flagged here because
they gate the OBJECTIVE comparison: the comparator arm C must be the STRONGEST classical practice (flux-consistent/EAP mean
state + worst-instant attachment check + tuned free parameters + a ceiling arm — all four SP-CARM trees; TWIN §4 has the I4
mean-conditions design only; SP9/SP-CARM judge) and the grader of both arms must be J_exact-class (wave-frame T0/S-BLITE)
or ship with the (v) bracket — TWIN §4 pins an IDENTICAL representation for both arms from F2.REPR, and 4/4 trees hold that
"a model cannot grade itself" (SP5/SP9 judge).

**q3 — Separate rungs for designer and evaluator?** On the objective axis: the objective of record is J_exact (D-JEX) with
J (D-MU) as the rung-2 working functional and (v) bars that are ESTIMATED, not certified. 4/4 trees make the evaluator a
different object from the designer BY CONSTRUCTION and make the reduction error a MEASURED per-design number — this is the
record's VI.4bis(ii) both-routes-live + [R22F-FORCHETTA] + M-RED + CFD-2 chain, so CONFIRM on the architecture; the
divergence is only whether the TWIN's decisive delta is evaluated on the reduced representation (identical for both arms)
or on the exact-on-pin evaluator. Objective-level verdict: a delta on the rung-2 functional is a statement about J, not
J_exact, unless the (v) bracket or the wave-frame evaluation is attached; the trees' demand is the record's own D-P (v)
taken seriously.

## 3. Weight on Q0 — the referee's and the PM's summary

Credibility: rows 1, 3a, 4a, 9a, 12, 14 CONFIRM the incumbent with derivations (4/4 or 3/4) — the objective of record
survives an independent attack from four lenses twice (2026-08-17, 2026-09-05). Rows 3b, 4b, 11 are NEW, cheap and
high-weight: they change what the decisive number can CLAIM and whether it is worth RUNNING, not how it is computed.
Row 15 is the only high-weight DIVERGENCE and the record wins on the sector by theorem, but owes the base-bracket band
term. Cost: the whole delta is ≤ 1 session — (K+1) per-phase solves at the record speed for the screen, the g_sep map
already computed, one band term from two re-evaluations, one paragraph of lever honesty. Shortest credible path = execute
the screen at TWIN opening (instance pin, two-stage pre-registration already allows an amendment block), add OUT-C and the
C61 residual to §6, re-word the accuracy-class sentence. No new theory, no new solver.

## 4. Panel recommendation and the 2026 DELTA-SWEEP (performed inline)

Recommendation: **DELTA-SWEEP-ONLY** (form of the objective = CONFIRM-BY-DIFF, done here; the lever/O-c axis has no ledger
row but is weighed of record outside the ledger at record grade AND is 4/4-converged by derivation in the trees, so a
FULL-PANEL on "O-a vs O-c primary" would be ritual — the four trees ARE that panel, with the O-c advocate argued and ranked
in every one of them). Mint the missing ledger row so the axis stops living outside the ledger: "objective-of-record:
O-a single-point s.t. g_sep hard (incumbent) vs O-c-primary vs O-b envelope vs engine-level class G; incumbent supports =
T3/T4/PB-2 + G2 + EAP remark + 2× four-tree de-novo convergence; falsifier = §5" (the C60/C61 no-row-class pattern, 8th
instance).

Delta-sweep 2026 (what the trees add beyond the 2026-08-17 record, objective axis): (Δ1) O L2 Jensen-gap difference screen,
derivative-free, with its event caveat — NEW; (Δ2) OUT-C constraint-decisive outcome + arm-C attachment map as registered
TWIN output, with the artefact guard (worst-instant check on arm C) — NEW; (Δ3) RDE-stand accuracy reality 2-4% Isp →
claim shape "computed, testable, not resolved" — NEW, [KNOWLEDGE] UNVERIFIED; (Δ4) term-by-term loss budget on the exit
field — NEW increment on the ladder; (Δ5) unsteady-specific pool estimate 0.15-0.5% — NEW prior, CONJECTURE-grade; (Δ6)
thrust vs Isp on the subsonic case-class — declaration gap; (Δ7) dJ/dw_k Verdict line — cheap increment already asked in
2026-08-17. Nothing in the sweep flips the objective of record; Δ1-Δ3 must be disposed of before F3.TWIN opens.

## 5. Proposed falsifier for Stage B (the one the parties must agree on)

STAGE-0 SCREEN ON THE PINNED TWIN INSTANCE (executable at TWIN opening, ≤ 1 session, record engine): compute (a) the
derivative-free difference cap 2·sup δ(S) (δ = ½H(S)Var_μ(u); K+1 per-phase solves at arm C and at its multistart
perturbations; H(S) from the phase-wise thrusts; event-stratified per C62), (b) arm C's per-phase g_sep map on supp(μ) with
the worst-instant check the P tree requires, (c) the width |D(p_b,+19%) − D(p_b,−15%)| of the TWIN delta over the C61
bracket with the same closure object in both arms. KILL of the incumbent objective/sector pairing: (a) < 1% of F AND (b)
≥ 0 everywhere ⇒ O-a on the plug has nothing resolvable and no operability lever either — the decisive question must be
re-posed (O-c primary or the pre-registered negative ships without a run); OR (c) > |D| ⇒ the plug cannot carry the
number at the Euler level (PB.3/C61 adjudication required first). SURVIVAL: (a) ≥ 1% of F, or (b) < 0 at some phase with
arm P attached (OUT-C live), with (c) < |D| − band. Rejectors: a corrupted-weight run must move (a) by the L3 identity
dJ/dw_k = F_k; a seeded separated phase must flip (b); swapping the closure between arms must break (c)'s cancellation.

## 6. BRANCH LEDGER (every branch seen; "not analysed" does not exist)

| Branch | Status | Reason / trigger + owner |
|---|---|---|
| V OBJ.1 / H (1) / O OBJ.2 / P OBJ.1 — O-a single point + g_sep hard | EXPANDED | row 1 (CONFIRM, derived 4/4) |
| V OBJ.2 / H (2) / O OBJ.5 — Isp vs thrust | EXPANDED | row 2; subsonic case-class declaration gap → F2a contract rows (SP7 judge) |
| V OBJ.3, S0.12(b) / H (3), S10 / O OBJ.4, S9 / P OBJ.3, S-8 — O-b envelope | EXPANDED | row 5; C55 NEVER by sequencing, no action before first multi-point instantiation |
| V OBJ.4, S0.12(a) / H (4), S8 / O OBJ.3, S10 / P OBJ.4, S-9 — O-c operability primary | EXPANDED | rows 4a/4b; pivot CONFIRM, OUT-C NEW → TWIN §6 amendment (owner F3.TWIN pre-registration; trigger = instance pin) |
| V OBJ.5, OBJ.6 / H (5) / O OBJ.2 bounds / P OBJ.5 — O-d as constraints, Pareto by multiplier | EXPANDED | row 6 (CONFIRM) |
| V OBJ.7 / H L4 budget — exergy / loss budget | EXPANDED | rows 9a/9b; 9b NEW increment → Verdict format (owner F2.ENGINE Verdict fields; trigger first (value, delta) row) |
| P OBJ.2 — vacuum objective | PRUNED | weight zero: excluded by the record's existence argument (Pa > 0 GIVEN); not a Stage-B item |
| P OBJ.6, S-10 / O OBJ.6, S12 / V S0.13(b) — engine-level class G | EXPANDED (objective statement) / DEFERRED (mechanism) | row 8; PB-4 + CFD-1 of record; trigger = class-G data or the P-1 lever paragraph; owner P-1 authoring (G5 window) |
| V S0.11 / H S12 / O S13 — bound-only negative-result road | EXPANDED | rows 3a/3b; the difference cap is NEW → §5 falsifier; owner F3.TWIN opening (Stage-0 screen) |
| O L2 (Jensen gap), O L3 (weight sensitivity), O L5 (feasible set) | EXPANDED | rows 3b/13/4a |
| H L3 (rothalpy Jensen pool) | EXPANDED | row 10 (NEW prior; measure at M-RED) |
| P DL-2 (linear thrust law), DL-4 (stand accuracy) | EXPANDED | rows 14/11 |
| P DL-3 (swirl recovery via radial placement, 1-4%) | DEFERRED | objective channel = swirl rows of the CycleFamily contract (VI.1 D.13/D.14/D.16, S-5F panel, B-1 convention pin); trigger F2.REPR five-field decision; owner SP5+SP6 / SP7 judges |
| V L0.4 (no cycle-averaged Rao: no common control surface) / P S-12 (cycle-averaged Rao as oracle) | DEFERRED | stationarity-system question, not objective: record T2 = per-phase closed form + μ-averaged coupling, closed form oracle-only for rotational data (VI.4bis(iv)); owner SP3/SP4 judges |
| V/H/O bell-first vs record plug (SP9 configuration) | EXPANDED (objective-sector pairing) / DEFERRED (base mechanism) | row 15; base-bracket band term → SP-PB/SP9 judges; trigger TWIN §6 amendment; owner F3.TWIN + C61 window |
| All four SP-CARM comparator strengthenings (flux-consistent/EAP mean, worst-instant check, tuned ceiling arm, thrust-consistent average refuter) | DEFERRED | gates the objective comparison but is SP-CARM/SP9's row; trigger = TWIN §4 arm-C build; owner SP9 judge; note: Kaemming-Paxson 2018 EAP row EXISTS (:236, read) — the EAP comparator is registry-covered |
| Designer ≠ evaluator; J_exact-class grader vs TWIN "identical representation for both arms" | DEFERRED | q3 answered at objective level; mechanism = SP5/SP9 judges; trigger F2.REPR verdict A-REPR |
| V L0.2 (two Strouhal limits, no sandwich) / H S3 St > 0.3 abandon vs [X-STSC] 0.35-0.60 | DEFERRED | SP1 judge; objective-relevant only through the (v) bar |
| Prior-tree FORK-3 (V 2026-08-17) / FORK-4 (P 2026-08-17) | EXPANDED | prior independent evidence for row 1 and row 13; both recommended O1 deterministic μ with sensitivity reported |

## 7. ADJACENT-FIELD PRIOR CHECK (mandatory) and [KNOWLEDGE] rows

Did the trees consider the SOTA of periodically unsteady flows and steady adjoint shape optimization? YES, all three items,
in all four trees, and each REJECTS the adjacent-field tool inside the pin for a DERIVED reason (the rotating-frame
steadiness lemma L0.1 / L1 / L1 / DL-1 makes harmonic balance the θ-Fourier discretization of the steady wave-frame
problem): (i) turbomachinery steady rotating frame + sector periodicity + mixing-plane averaging — O S4 [Lakshminarayana
1996; Wang & He 2010], H SP-CARM [Denton 1992], O SP-CARM [Cumpsty & Horlock 2006], P DL-1 [textbook]; (ii) harmonic-
balance / time-spectral with adjoints — V S0.7 [Hall-Thomas-Clark 2002 full; Nadarajah-Jameson], H S5 [Hall 2002;
McMullen-Jameson 2006], O S6 [Hall 2002; Gopinath-Jameson 2005], P S-5 [Hall 2002; van der Weide 2005; Nadarajah-Jameson
2007]; (iii) steady adjoint shape optimization — V/H/O/P [Jameson 1988; Giles-Pierce 2000/2001; Alexandrov TRMM; Drela 1998
multipoint]. This is a 4/4 DERIVED confirmation of C59's binding scoping ("cycle-average canonical inside the pin; HB/TS
live only in weakened-pin regimes"). Registry coverage: rubino_2018 (:579), zahr_persson_2016 (:588), schotthofer_2024
(:597), giles_pierce_2000/2001 (:507-521) EXIST. NOT covered (grep 0 hits): Hall-Thomas-Clark 2002; Lakshminarayana 1996;
Wang-He 2010; Denton 1992; Cumpsty-Horlock 2006; Drela 1998; Jameson 1988; Anand-Gutmark 2019; Raman-Prakash-Gamba 2023;
Sutton-Biblarz; Stark 2005 / Schmucker / Summerfield / Frey-Hagemann 1998; Rankin 2017 (garble flag); Goto 2019 and Fotia
2016 are WANTED rows (:1267, :1272), unread. Every number the trees quote from these is carried here as UNVERIFIED.

[KNOWLEDGE] rows (identity — why needed — procurement owner); NEVER evidence:
- K-1 Hall, Thomas & Clark 2002 (harmonic balance) + McMullen-Jameson 2006 / Gopinath-Jameson 2005 (time-spectral) — the
  4/4 rejection of HB inside the pin supports C59's scoping; a registry row is needed before C59's note can cite it — owner:
  C59 F2-entry census window / lit procurement W-queue.
- K-2 Turbomachinery rotating-frame steady practice + mixing-plane averaging (Lakshminarayana 1996; Denton 1992; Cumpsty &
  Horlock 2006; Wang & He 2010 rotating-frame adjoint) — precedent for the S-BLITE evaluator and for the flux-consistent
  comparator state (SP-CARM strength) — owner: F3.TWIN arm-C build + S-BLITE claim (claims_registry :1536) citation duty.
- K-3 Drela 1998 "Pros and cons of airfoil optimization" (multipoint design as standard practice) — bounds the novelty
  claim of the design loop (O C.5) exactly as M0 Part I already does ("every component is prior art in isolation") — owner:
  P-1 novelty query at G5.
- K-4 Anand & Gutmark 2019 review; Raman, Prakash & Gamba 2023 ARFM — combustor-side loss magnitudes 5-15% for the lever-
  honesty table (row 3a) — owner: P-1 introduction / lever paragraph; numbers UNVERIFIED until read.
- K-5 Sutton & Biblarz (contour losses 1-3%; frozen vs shifting-equilibrium 1-5%) — lever table + PIN-2 bracket duty —
  owner: P-1 + SP7 pin-magnitude duty.
- K-6 Rankin 2017 / Goto 2019 / Fotia 2016 RDE thrust-stand accuracies (1-3% thrust, 2-4% Isp) — decides the accuracy-class
  wording of TWIN §6 and D6 G2 (row 11) — owner: procurement queue W-01 (Fotia/Goto WANTED rows) + TWIN §6 amendment.
- K-7 Separation-criterion family (Summerfield 1954; Schmucker 1974/84; Stark 2005; Frey & Hagemann 1998) — the g_sep
  criterion class R2 of [D-GSEP] is "declared empirical closure"; the trees derive the margin as the criterion-family
  SPREAD (H, P) — a registry row is needed before the margin derivation can land — owner: D-GSEP closure adjudication
  (F2-DUTY-C27 window / SP2 judge).
- K-8 Hagemann, Immich, Nguyen & Dumnov 1998 (mission-averaged plug/dual-bell gains; base correlations) — WANTED row
  :1374 exists; needed for row 5 (O-b novelty bounding) and for C61 — owner: existing procurement queue.

## 8. Contradictions and honesty notes

- The trees quote the thrust-stand class 0.5-1% as the accuracy class AND (P only) the RDE-stand reality 2-4%; the record
  quotes only the former (TWIN §6, D6 G2). The record's wording is not wrong, it is incomplete for an RDE anchor.
- Three trees put the SCREEN first in the order of battle (sessions 1-3); the record's G2 sits at M2 after ENGINE/M-RED.
  With the engine already at 0.116 s/solve the sequencing cost is now small; the screen can ride the TWIN-opening amendment.
- No tree derives the affinity of F in Pa on the ambient-blind class (record C55 note); the record is stronger on O-b.
- No tree has the T3 collapse in its general form; P DL-2 is its choked/const-γ special case; the record is stronger on
  the sector choice. The trees are stronger on the DIFFERENCE cap (O L2) and on the OUT-C outcome.
- LOG-4b: the hyperbolic tree declared the memory injection and its non-use; every convergence above is graded DERIVED or
  NAMED on the tree's own text, never on the coincidence of names.
