# STAGE A — DIFF JUDGEMENT, SP1 "TIME TREATMENT: how the inflow time-dependence enters design and evaluation" (S-REVIEW 2026-09-05)

Judge: NOT agnostic (record-aware). Persona: JPP referee of the decisive number + PM of the shortest credible path.
Inputs read integrally: the four de-novo trees `stageA_tree_{variational,hyperbolic,optimization,propulsion}.md`,
`PROBLEM_STATEMENT_agnostic.md`, `DERIVER_BRIEF_agnostic.md`, `INCUMBENT_pointers.md` and every SP1 anchor it cites
(M0 Part I :25-62, D-MU :95-110, D-P :286-408 incl. requirement (v) + BAR-CLASS NOTE, [T-T0] :512 ff. + [S-T0P]/[T-T0P],
[T-T3] :746 ff., [T-T4] :2294 ff., Part V ladder + [S-BLITE] :3008-3050, VI.4bis(i)(ii) :3140-3160, F2-B0 block :4250-4299;
D1 = `docs/rde_nozzle_problem_book.md` §8 :451-478 + §9 ledger rows D1/D2; D6 G2/G3 :779-786, F2a block :160-213,
F2.REPR addendum :1159-1195; `choice_ledger.yaml` C51 :706, C57 :771, C59 :795, C62 :832; `claims_registry.yaml` S-P4F :643,
X-STSC :2278; `docs/rde_nozzle_T3QS.md` §1 + B3/B4; `findings_registry.yaml` :892 (st-marginal-numbers-uncarried),
:1052 (quadrature bar), :2566 (tau_n definition unpinned), :2717 (pipeline:m-red-campaign); decision map rows PIN-WAVE/C51/C59/C62/OPTSHIFT;
`BRIEF_blocco2_phaseD_addendum_c4.md` §(e) (C59 evidence); TWIN protocol §1-§9; `st_scoping_number_run.log` (MEASURED St);
prior de-novo evidence 2026-08-17: `phaseA_tree_*_CONDENSED.md` (H FORK-1/2, P FORK-1/2/3, V FORK-3/4/5, O FORK-1/2) + `phaseB_tree_diff.md` §3.1.
Independence caveat of record (LOG-4b) applied: every convergence is graded DERIVED vs NAMED below. Memory files NOT read by this judge.

## 0. The decisive input: the MEASURED St and what each tree licenses at those values

`st_scoping_number_run.log` ([X-STSC] PASS, envfp e100f996): bell TOC (L = 4 y_t) St_n in [0.153, 0.679] over the envelope,
[0.347, 0.599] AT THE RECORD HEAD COUNT (n = 3/2); plug class (L_ideal(1-trunc), trunc 0.20-0.40) St_n in [0.268, 1.415], worst 1.41;
He up to 1.39. Convention: f in the log is the PASSAGE frequency (n x f_1), so St_n = f tau_n is exactly the trees' St = f tau_res
(V L0 notation, H "St = fL/u", O "St = f tau_res", P "Delta_phi = 2 pi f int dx/u_x" = 2 pi St_n).

Applying each tree's OWN licensing rule to these numbers (designer D / evaluator E):
- VARIATIONAL (SP1 :237-262): D = T.3 quasi-steady multipoint ONLY IF the measured |J(St) - J_qs| < Delta J_decisive (Omega_p-sweep);
  no a-priori St cut. At St 0.35-0.60 the rule is UNDECIDED until the sweep runs; E = T.4 rotating-frame steady 3-D ALWAYS.
- HYPERBOLIC (SP1 :280-292): D = (2) quasi-steady ensemble "if St < 0.3 measured, else (3) in its marching branch"; E = (3) always
  + (5) once. At St 0.35-0.60 (bell) and 1.41 (plug) the hyperbolic tree licenses the ROTATING-FRAME MARCHING engine for the DESIGN
  loop, not the frozen-time ensemble. (Its 0.3 is an UNDERIVED constant — a brief violation; not consumed, see §3.)
- OPTIMIZATION (SP1 :259-284): licensing is NOT on St at all but on the measured reduction error r_red = |J_RF3D - J_QS|/F on the two
  decisive designs: r_red <= b_TS/3 plain QS loop; b_TS/3 < r_red <= b_TS TR-corrected loop (S7); r_red > b_TS switch the loop to RF-3D.
  Thresholds DERIVED (three-way equal split of the band). E = RF-3D sector always, unsteady 3-D once.
- PROPULSION (SP1 :305-329): D = T.2 quasi-steady admissible iff c2 A^2 Delta_phi^2 < 0.1 band_TS with c2 MEASURED from two wave-frame
  solves (Omega, Omega/2). With Delta_phi = 2 pi St_n = 2.2-3.8 rad (bell) and up to 8.9 rad (plug) the criterion cannot hold unless
  c2 A^2 is < 1e-3 — the tree's own default becomes T.4 (phi-averaged axisymmetric with MEASURED closure from one 3-D solve) for D;
  E = T.3 rotating-frame steady 3-D always.
VERDICT ON THE NUMBER: at the measured St NO tree licenses the frozen-time rung ALONE for the designer, and NO tree licenses ANY reduced
rung as the EVALUATOR of the decisive number. 4/4 put the evaluator on the exact-on-pin wave-frame steady 3-D field (record [T-T0]),
with a time-accurate run once as pin monitor. This is exactly the X-STSC declared license rule of record ("MARGINAL: corrector MANDATORY;
wave-frame backstop" / plug "wave-frame / unsteady rung REQUIRED") for the DESIGNER — and it is STRONGER than the record for the EVALUATOR (§2, row A2).

## 1. Incumbent of record (SP1) and its adjudication class

Incumbent: frozen-time per-phase decomposition J[S] = Int F[S; s(xi)] dmu (D-MU :95-110; D-P objective :286 ff.) with the O(St) corrector
as THE bar: J_exact = J_avg + St J_1 + O(St^2) (D1 §8 :472-478, "MARGINAL", P4 mandatory, T0 as nonperturbative backstop); requirement (v)
bars "|J_exact - J[S*]| <= St|J_1| + D2 residual + DWR" with the BAR-CLASS NOTE (PAN-S14) that these are ESTIMATED/ASYMPTOTIC indicators, NOT
certified bounds; VI.4bis(ii): both corrector routes live (unsteady comparison O5 general; steady sweep-perturbation solve on the wave-frame
anchor when T0 applies); S-P4F (claims :643, THEOREM*): corrector solvability = Fredholm alternative on the cycle monodromy; [T-T3QS]: J_1 = 0
on T3 ray families (first-order sweep cancellation), first-order jump-localized residue on sawtooth cycles, "conjectural until measured" (B3);
G3 (D6 :783-786): trigger "St|J_1| large" NEVER derived (S14 duty, "the only gate whose kill threshold cannot reject"); C59 (:795, NEVER):
temporal form = cycle-average CANONICAL-INSIDE-THE-PIN (addendum-c4 §(e), binding scoping); C62 (:832, NEVER): phase quadrature uniform-trapezoid
practiced, never adjudicated; evaluator of the decisive number = TWIN §6 "cycle-averaged Isp (equivalently J_avg ...) per arm" with a
"representation-class term while A-REPR carries one" — i.e. the TWIN as pre-registered evaluates BOTH arms on the rung-2 functional plus bands,
the wave-frame field being a bar/backstop (Part V ladder row 1; [S-BLITE] "the cheap exact meter of the rung-2 sweep/D2 residual"), not the evaluator.

ADJUDICATION CLASS: NO-ROW for the SP1 question proper (designer-rung vs evaluator-rung at the measured St). The ledger carries C59 (temporal
FORM of the functional, NEVER, question declared EMPTY inside the pin) and C62 (quadrature, NEVER); the frozen-time + corrector architecture
itself is D1 §8 single-author text later PANEL-VERIFIED as a BAR CLASS (PAN-S14 bar-class note) — never adjudicated against the alternative
"exact wave-frame field as the evaluator of the decisive number". No genuine advocate row exists, so no 2026 delta-sweep was performable inline
(delta_sweep_done = false); the sweep of the adjacent field IS performed below (§4) as [KNOWLEDGE] census, never as evidence.
PANEL RECOMMENDATION: FULL-PANEL, scoped to the ROLE question (row A2) + the G3 threshold derivation (row A4); C59 itself is CONFIRM-by-diff
(row A6) and needs no panel; C62 stays with its F2-engine owner (row A7).

## 2. Approach table (schema columns: approach | lenses | classification | weight on Q0 | reason | credibility/cost effect | record anchor | tree anchor)

| # | Approach | Lenses | Class | Weight | Weight reason | Changes credibility or cost of answering Q0 | Record anchor | Tree anchor |
|---|---|---|---|---|---|---|---|---|
| A1 | Single-mode rotating data + fixed axisymmetric nozzle => lab-frame thrust CONSTANT in time; J_true = steady wave-frame 3-D functional; time mean needs no limit | V,H,O,P (4/4, each with a short proof) | CONFIRM-candidate (DERIVED) | medium | re-derives the program's discovery (1); raises credibility of the pin-scoped claim, changes no cost | credibility up: four blind proofs of T-T0(i)-(ii); the trees ALSO derive the falsifier (thrust-trace non-flatness / drift of a time-accurate run) = record N-T0' monitor | M0 :25-40 (1); [T-T0] :512 ff.; [S-T0P] stage 1; claims S-T0P :1900, T-T0P :2044 | V L0.1 :15-29; H L1/L2 :15-27; O L1 :14-24; P DL-1 :12-30 |
| A2 | EVALUATOR of the decisive number = exact-on-pin wave-frame steady 3-D field (sector 2pi/n); DESIGNER may be reduced; designer != evaluator BY CONSTRUCTION; reduction error = MEASURED |J_3D - J_red| on the two decisive designs | V,H,O,P (4/4, each argued: "a model cannot grade itself", "no adjoint needed for evaluation", "the only representation exact under the pins must be the evaluator") | DIVERGENT (DERIVED) | high | the record's TWIN evaluates both arms on J_avg + a bar; the trees say the comparison itself must run on J_exact — this is the referee's "why not X?" at St 0.35-0.60 | credibility: HIGH effect — a delta quoted from the reduced rung with an asymptotic (non-certified) St bar at St = 0.35-0.60 is exactly what a JPP referee rejects; cost: one exact evaluation per arm; the record already OWNS the cheap instrument ([S-BLITE] helical space-marching at marching cost under the L4 axial margin; C51 route-B where |w_rel| > c) so the cost delta is the promotion of an existing bar-meter to evaluator status, not a new solver | TWIN §6 :87-116 (metric = J_avg per arm + "representation-class term"); D-P (v) BAR-CLASS NOTE; Part V ladder row 1 :3010; [S-BLITE] :3027-3050; C51; M-RED findings :2717 | V S0.4 :103-117 + SP5 :383-390; H S11 :210-235 + SP5 :366-377; O L4 :45-52 + T.E1-E3 :277-279; P H-1 :245-274 + SP5 :456-462 |
| A3 | Quasi-steady multipoint (K frozen phases, time-fraction weights w_k = Delta phi_k / 2pi) as the DESIGN loop, with per-phase adjoints summed | V T.3, H (2), O T.2, P T.2 (4/4) | CONFIRM-candidate (DERIVED: weights = azimuthal measure THEOREM in V/H; K rule derived in all) | medium | re-derives rung 2 (D-MU) as the designer's object — but every tree licenses it CONDITIONALLY on a measured reduction error, never on St alone | credibility neutral-to-up (the rung is standard multipoint practice, said so by O C.5 and P C.5: "weighted averaging is NOT novel"); cost none | D-MU :95-110; D-P objective; VI.4 cycle layer; C62 | V :243-246; H :285-287; O :266-270; P :312 |
| A4 | G3 THRESHOLD DERIVED FROM THE BAND, not from St: the reduced designer is licensed iff the MEASURED reduction error on the decisive designs is below a declared fraction of the thrust-stand band (O: b_TS/3 and b_TS, three-way split; P: 0.1 band_TS; V: < Delta J_decisive; H: designer/evaluator disagreement > designer band rejects) | O,P,V,H (3/4 derive a fraction; V derives "< decisive difference") | NEW (no record home for the NUMBER) + repairs a declared record defect | high | D6 G3 :783-786 is "the only gate whose kill threshold cannot reject" (S14 duty open since 2026-07); the trees supply a derivation RULE that makes it a rejector at zero compute | credibility: HIGH (closes the un-rejectable gate); cost: zero beyond the A2 evaluation, which produces r_red for free | D6 G3 :783-786; D-P (v); TWIN §6 bands; findings :892 residue (i) | O :280-283; P :319-323; V :253-254, :261-262; H :291-292 |
| A5 | St-ladder / Omega-sweep at FIXED data (f is a parameter): measure J(St), its two limits (quasi-steady, homogenized) and the EXPONENT of the reduction error (rejector: exponent test) | V (Omega_p-sweep + both limits, L0.2), H (f, 2f, 4f exponent >= 1), P (c2 from Omega, Omega/2; optional 3-value sweep), O (St by scaling L) | CONFIRM-candidate (DERIVED) of the M-RED B-1 ">= 4-point St-ladder Richardson" | medium | the record has this as the M-RED campaign leg (F2 queue, critical); the trees make it the G3 decision instrument and the generalization axis of the claim ("the map, not the point") | credibility up (the exponent test can KILL the corrector expansion form); cost: already budgeted in M-RED | findings :2717 (B-1 St-ladder); D6 Phase A4 O5 predictions; T3QS B4(iii) | V L0.2(iii) :40-44, :259-262; H :118-124, :490-491; P :319-322, :613-615; O :514-515 |
| A6 | Harmonic-balance / time-spectral / windowed unsteady adjoint in the lab frame: REJECTED under the pin for a stated reason (HB in time == theta-Fourier of the rotating-frame steady problem; Gibbs at the data-borne shock => K ~ 1e2; dominated by A2); live only if the pin is weakened (two incommensurate modes) | V S0.7/T.5, H S5/(4), O S6/T.5, P S-5/T.5 (4/4) | CONFIRM-candidate (DERIVED) of C59 "canonical inside the pin" | low | C59's question is EMPTY inside the pin by binding scoping; four blind derivations of the same dominance argument add credibility but change nothing on Q0's road | credibility up on C59; cost none. NOTE: P S-5 rejects a DIFFERENT object (2-D+t at fixed theta dropping the azimuthal flux, O(1) error) — an additional argument, consistent | C59 :795; addendum-c4 §(e); C59 anchors rubino_2018 / zahr_persson_2016 / schotthofer_2024 (registry, READ-INTEGRAL) | V :137-143; H :142-151; O :129-137; P :132-144 |
| A7 | Phase quadrature: V uniform trapezoid on the circle, K = 2N_h + 1 from the retained-harmonic energy criterion, rejector "double K"; O trapezoid but GRADED nodes at the sharp front (algebraic convergence for shocked waveforms), K until |J_K - J_2K| <= b_TS/10; H Richardson-in-K to band/4 | V,O,H (3/4; P silent) | CONFIRM-candidate-NAMED for C62 alternatives 4 (declared canonicity) AND 2 (event-stratified) — the trees SPLIT between them, matching C62's own two live alternatives | low | quadrature error is a band term, never the decisive delta; but findings :1052 shows the record has quoted a quadrature-unbarred number once | credibility: low direct; cost: none. Consumed by the C62 owner (F2 engine numerics cluster), not by this panel | C62 :832; VI.4bis(i); findings :1052 | V :243-246; O :266-270; H :121-122 |
| A8 | Expansion ORDER in St of the reduction error: V CONJECTURE |J(St) - J_qs|/J = O(St eps^2) (FIRST order in St, cross term); P CONJECTURE J(Omega) = J_qs[1 + c2 A^2 Delta_phi^2 + O(Delta_phi^4)] (SECOND order, no linear term); H "O(St A)" (first order) | V,P,H (mutually INCONSISTENT) | DIVERGENT among trees; the record ([T-T3QS]) is SHARPER than any tree: J_1 = 0 on T3 ray families (P's quadratic law holds THERE), first-order jump-localized residue on sawtooth cycles (V/H's linear law holds THERE), B3 "conjectural until measured" | medium | the corrector's form is the bar the record ships; the trees' disagreement PROVES the exponent must be measured, not assumed — and M0's own rule already says so | credibility: the record survives the diff with a sharper statement, provided the exponent test (A5) is run on the decisive family (case-A sawtooth blowdown = the jump-localized branch, where J_1 != 0); cost none extra | T3QS §1, B3, B4(i); D1 §8 :474-476; S-P4F :643 | V :255-258; P :319-322, S-14 :238-243; H :117-118 |
| A9 | Choked-throat linear thrust law: with a choked throat and 1-D inflow F(t) is LINEAR in p0(t) so the classical C_F,vac optimum maximizes the time mean for ANY waveform — zero gain from unsteady-aware design in that class; residual Jensen gap via gamma(T) second-order < 0.1 % | P DL-2 (1/4, with proof under H1-H4) | CONFIRM-candidate (DERIVED) of [T-T3] collapse (fixed full-flowing wall, pressure-scaling similarity) — P's H4 gamma = const matches T3 H1 | medium (SP0/SP-OBJ weight; SP1 corollary: the corrector can only matter through the T3-violating channels) | independently re-derives discovery (2) and its consequence that the decisive instance MUST sit where T3 leaves room (supersonic interface / finite St / attachment / base) — the record's N1-N6 channel logic and the TWIN's "active channels N1, N2, N4" | credibility up on T3 and on the TWIN sector choice (truncated plug); cost none | [T-T3] :746 ff.; M0 :44-49; D1 §9 "T3 is a conservation law for research effort"; TWIN §3 | P DL-2 :32-50; O L2 :26-40 (Jensen-gap bound = the non-similarity generalization, SCREEN) |
| A10 | Jensen-gap SCREEN: |J_2 - J_1| <= (1/2) H Var_w(u) computable WITHOUT derivatives from K+1 steady solves; 2 max delta < b_TS => the O-a advantage of any quasi-steady-aware design is unresolvable — a negative answer BEFORE optimizing | O L2/S13 (1/4; V S0.11 and H S12/L4 give the ceiling-gap analogue) | NEW as a pre-optimization time-treatment screen (record has the bound LADDER and int-max, not this variance-form screen) | medium | cheap (1 session), can END the O-a road at the measured St before F2.ENGINE is built; its caveat (ii) (feasible-set first-order change through per-phase attachment) is the record's N1 channel | credibility up (a pre-registered negative branch with a THEOREM-grade screen); cost: 1 session, may SAVE the campaign | D-P (iv) bound ladder (int-max, sonic-capped J_ideal, B_EK); GB_ergodic upper wall; D1 §9 novelty channels | O :26-40, :212-218; V :168-176; H :210-224 |
| A11 | Rothalpy / Jensen LOSS as the unsteady-SPECIFIC pool: h0 redistribution between particles by the rotating pressure field is a pure loss ~ eps^2/8 ~ 0.15-0.5 % of thrust; with the data-shock entropy it is "the only two nozzle-side unsteady-specific loss terms" => Q0 at (O-a) is intrinsically MARGINAL and must be MEASURED with a difference-resolving protocol | H L3 (1/4) | NEW (no record home; nearest = EAP swirl-energy remark and the S-H remark, M0 Part III) | medium | quantifies WHAT the time treatment can buy at all (a Stage-0 gate at near-zero cost); if the pool < band the SP1 question is moot for O-a | credibility: HIGH if it survives a refuter (it is a Jensen argument on the Euler turbine identity — THEOREM-shaped, unverified here); cost: seconds from class-B data | M0 Part III EAP/S-H remarks (per pointers); D6 G2 :779-782 value gate | H L3 :28-37, L4 :38-49, S11 Stage 0 :220-224 |
| A12 | phi-AVERAGED steady axisymmetric DESIGN model with MEASURED closure (wave-correlation "unsteadiness stress" terms extracted from one 3-D wave-frame solve, frozen per closure update; abandon if closure not design-invariant) | P S-4/T.4 (1/4) | DIVERGENT from the per-phase family (a mean-state-plus-closure designer instead of a multipoint designer) | low | a closure-corrected mean model has NO asymptotic regime (O L4: "the mean-state model has no asymptotic regime in St") and its design derivative ignores d(closure)/dS by construction; P's own abandon rule fires exactly where the record's T-RED residual lives | credibility: neutral (the tree grants it is a direction-finder only, "the evaluator carries the claim"); cost: one 3-D solve per closure update | [T-RED] :1734 ff. (reduction residual, delta/L_H UNDERIVED); OPTSHIFT SCHEMA-only; C51 | P :120-131, :314-316, :324-328 |
| A13 | Multi-fidelity TRUST-REGION MODEL MANAGEMENT: QS-2D adjoint loop with RF-3D value corrections (first-order corrected TR, Alexandrov-Lewis class) when b_TS/3 < r_red <= b_TS; control-variate bands | O S7/G.2 (1/4) | NEW (no ledger row: C57 is the exploration tier, C49 the captured explorer; neither is model management) | medium | it is the one design-loop architecture that USES the measured reduction error instead of merely reporting it; at the measured St this is the branch O's rule most likely lands on | credibility up (KKT of the corrected model first-order consistent with the exact evaluator at the iterate); cost: one exact value per accepted step | none (C57/C49 adjacent, different axes); [S-BLITE] as the cheap corrector source | O :139-161, :351-352, :282 |
| A14 | tau_n MEASUREMENT: mass-flux-weighted mean streamline int dx/u_x from the first solve (H, O, P) vs MAX over interface streamlines int ds/|u| (V, conservative); plus M_rel = |u_theta - Omega r|/a map (H L5, P) and azimuthal-communication number C_theta (O L4) as second/third indicators | H,O,P (3/4 converge on the problem-book definition), V (max) | CONFIRM-candidate (DERIVED) of D1 Def. 8.1 (tau_n = int dx/u along the mean streamline) — settles findings :2566 in favour of the problem-book definition, with V's max-over-streamlines as the conservative reporting variant | low | pins the definition the G3 number inherits; no effect on the road | credibility up (definition ambiguity closed by 3/4 blind convergence + the S.22 variant demoted); cost none | D1 §8 :453-455; findings :2566, :892 residue (i); X-STSC caveats | H :281-283; O :260-263; P :306-309; V :251-254 |
| A15 | Pin monitor = ONE time-accurate 3-D run initialized on the wave-frame steady field; drift beyond discretization noise => not in the pinned class (data rejected, not the lemma); thrust trace must be constant | V S0.8, H S6/(5), O V.6/T.E2, P F.5/DL-1 (4/4) | CONFIRM-candidate (DERIVED: each derives it as the falsifier of A1's hypothesis (H3)) | low | the record's flatness monitor is already mandatory in every data contract (VI.4bis(v)); the trees add the 3-D-drift form as cross-code anchor | credibility up; cost: one affordable run (H prices "hours") | [T-T0] N-T0'; VI.4bis(v); O5 oracle VI.6; VI.7 wave-frame anchor | V :145-150; H :153-162; O :475-476; P :24-26, :346 |
| A16 | Linearized small-amplitude (frequency-domain) expansion about the MEAN as a design corrector: REJECTED at RDE eps ~ O(1); kept as O(eps^2) estimator / rejector of the sweep | V T.7, H (6), O T.6 (3/4) | ORCHESTRATOR-SEEDED clarification, not a diff: the record's corrector linearizes in the SWEEP parameter about the per-phase field (VI.4bis(ii) "steady sweep-perturbation solve"), NOT in amplitude about the mean; the trees reject a different object | zero | no tree attacks the record's actual corrector; the rejection of amplitude-linearization is consistent with D1 §8 (no such expansion is claimed) | none | VI.4bis(ii) :3150-3156; D1 §8 :474-476 | V :152-159; H :287-288; O :274-276 |

## 3. Reasons with anchors (prose)

3.1 A2 is the load-bearing divergence. The record's decisive comparison (TWIN §6) quotes delta from "cycle-averaged Isp (equivalently J_avg
normalized by the metered feed) per arm" with bands = Richardson + certificate-stack + "representation-class term while A-REPR carries one".
The (v) bar the record attaches to J_avg is, by its own BAR-CLASS NOTE (D-P :396-402), an ESTIMATED/ASYMPTOTIC indicator: "St|J_1| ... does
not by itself bound the remainder"; certified brackets exist only via the D2.2 fallback targets. At St_n = 0.35-0.60 (bell, record head count)
and 1.41 (plug, the TWIN sector) an asymptotic O(St) bar is an EXTRAPOLATION beyond its regime — the four trees, each from its own lens,
reach the same construction that dissolves the objection: evaluate BOTH arms on the exact-on-pin wave-frame steady field (which the record
proved exact at T-T0 and whose cheap instrument it built at [S-BLITE]) and quote the reduction error as a MEASURED number per design
(H L8: the residual r_theta of the slice inserted in the 3-D equations + one 3-D solve; O r_red; P |J_3D - J_axi|; V |J_R3(St) - J_R2|).
The record has every piece (T-T0, S-BLITE under the L4 axial margin, C51 route-B where |w_rel| > c, M-RED legs (A)-(E)) but assigns them the
ROLE of bar/backstop/meter; the trees assign them the role of EVALUATOR OF THE DECISIVE NUMBER. Cost delta is small because the instrument
exists; credibility delta is the whole referee objection. This is why the class is DIVERGENT-derived and the weight high.
Caveat of record the trees do not see: the A-REPR field of the TWIN (4-field axial / five-field / route-B / hybrid / 3-D-per-phase, D6 :1170-1178)
is exactly where this role decision lands — F2.REPR is the owner; this judgement is INPUT to it, not a verdict.

3.2 A4 closes an un-rejectable gate. D6 G3 :783-786 has carried since S14 the duty "the trigger 'large' must be a NUMBER with a derivation".
Three trees derive the number from the materiality class the record itself adopted (D6 :779-782 thrust-stand note): the reduced designer is
licensed iff its MEASURED reduction error on the decisive designs is below a fraction of b_TS (O: b_TS/3 plain, b_TS with corrections;
P: 0.1 band_TS "one decade below the accuracy class"); V states the same rule against the decisive difference itself. The fraction differs
(1/3 vs 1/10) — the derivations differ in how many band terms share b_TS (O: three; P: ten-term headroom convention). Either is a derived
rule; neither is a magic St cut. The hyperbolic tree's "St < 0.3" is an undeclared constant and is NOT consumed (its second criterion,
designer/evaluator disagreement > designer band, is the same rule as the others). The falsifier of §5 fixes the fraction by measurement.

3.3 A8 protects the record's corrector form but only through measurement. V (first order in St, cross term St eps^2), H (O(St A)) and P
(second order, no linear term) contradict each other on the exponent. The record's [T-T3QS] already contains BOTH regimes: J_1 = 0 on
T3 ray families (P's law), first-order jump-localized residue on sawtooth cycles (V/H's law), labelled "conjectural until measured" (B3).
Since the TWIN data class is case A = exponential blowdown (sawtooth), the decisive family sits in the jump-localized branch where J_1 != 0:
the exponent test of A5 (H: fit p on f, 2f, 4f; reject the reduction if p < 0.8) is therefore MANDATORY on the decisive family, not optional.
This is already in M-RED B-1 (findings :2717) — the diff converts it from a campaign leg into a gate condition of the TWIN.

3.4 A9/A10/A11 bound what the time treatment can buy. P DL-2 re-derives T3 (with the gamma(T) second-order residual < 0.1 %, consistent
with D3 §5.2 numbers cited in the pointers); O L2 generalizes it to a computable Jensen-gap screen; H L3 prices the unsteady-specific pool
at 0.15-0.5 % of thrust. All three say the same thing the record says at D1 §9 ("T3 is a conservation law for research effort"): the SP1
choice matters ONLY on T3-violating channels, and the TWIN's sector (truncated plug, N1/N2/N4) is the right arena. None of the three
quantities has a carrier in the record; A10 and A11 are cheap (values only) and are the trees' Stage-0 gate — the record's
G2 value gate has no such pre-optimization screen. Recommendation to the panel: adopt ONE of A10/A11 as the Stage-0 screen owned by
F2.ENGINE entry (ceiling J_ceil of H L4 is the same object as the record's sonic-capped J_ideal, so the loss BUDGET decomposition is
the increment).

3.5 A6/A7: the ledger NEVER rows. C59 is CONFIRMED by four independent dominance arguments (HB under the pin == theta-Fourier of the wave-frame
steady problem; Gibbs at the data shock; dominated by A2) — CONFIRM-by-diff, no panel needed; the trigger clause (weakened pin) stands.
C62: the trees split between uniform-trapezoid canonicity (V, spectrally accurate for smooth periodic data) and event-graded nodes (O, algebraic
convergence for shocked waveforms; H Richardson-in-K) — precisely C62's alternatives 4 and 2; consumed by the C62 owner (F2 engine numerics
cluster), weight low on Q0. The prior de-novo trees of 2026-08-17 said the same (V FORK-4 "xi-modulus", O FORK-2 "double N_xi", diff §2.10).

3.6 Prior independent evidence (2026-08-17) — consistency check. The prior condensed trees already carried: H FORK-1 "(b) the exactness anchor
... the ONLY bridge exact at marginal Strouhal; converts requirement (v) from an asymptotic apology into two measurable terms" and FORK-2
"the defect of (a) is the azimuthal-flux commutator, helix angle tan(alpha_h) = Omega r/u_x"; P FORK-2 "at marginal St a pure O1 claim is
indefensible ... O2 as default carrier of the (v) unsteadiness term"; O FORK-1 "HB is the only measuring instrument for the gap at marginal St
... K-ramp at S*". The 2026-09-05 trees are STRONGER on the same axis: the prior trees made the exact object the CARRIER OF THE BAR (= the
record's current role); the new trees, given the measured St, make it the EVALUATOR. Same direction, one rung further — a second independent
signal, not a reversal. (The prior diff §3.1 recorded the (v) decomposition as "DIRECT INPUT to T-DISC/T-RED/M-RED"; those landed; the
role question did not.)

3.7 Two record items the trees MISS (record ahead of the trees): (i) S-P4F (Fredholm alternative on the cycle monodromy; the P1a/P1b margin
as the solvability monitor of the corrector) — no tree derives a solvability condition for its correction step (O's TR corrections and P's
closure both assume the correction exists); (ii) [S-T0P] stage-1 honesty: the naive periodic-BVP adjoint is DEGENERATE along the group orbit
(trivial Floquet multiplier) — only H (S6 "periodic adjoint") brushes it; none derives the quotient necessity. Both are credits to the
record and stay of record.

## 4. Adjacent-field prior check (mandatory; every item = [KNOWLEDGE], never evidence)

| Item | Considered by trees? | Where | Registry row? | Status |
|---|---|---|---|---|
| Turbomachinery steady rotating-frame / sector-periodic practice (mixing plane, phase-lag) | YES (O S4 "[KNOWLEDGE: Lakshminarayana 1996, abstract]"; H SP-CARM (2) "[KNOWLEDGE: Denton 1992 mixing-plane, abstract]"; P DL-1 "textbook") | O :104-107; H :527-529; P :27-28 | NONE (grep lakshminarayana/denton/turbomach = 0) | UNVERIFIED [KNOWLEDGE]; census rows proposed §6 |
| Rotating-frame discrete adjoint (turbomachinery) | YES (O S4 "[KNOWLEDGE: Wang & He 2010, abstract]") | O :106-107 | NONE | UNVERIFIED [KNOWLEDGE] |
| Wave-fixed-frame RDE simulation precedent | YES (P DL-1 "[KNOWLEDGE: Paxson 2014, AIAA 2014-0284, abstract]") | P :26-27 | NONE (registry has paxson_miki_2022, kaemming_paxson_2018 only) | UNVERIFIED [KNOWLEDGE] |
| Harmonic balance / time-spectral with adjoint | YES 4/4, rejected for stated reason (V "[Hall, Thomas & Clark 2002, full; Nadarajah & Jameson ~2007, abstract]"; H "[Hall 2002 full; McMullen & Jameson 2006 abstract]"; O "[Hall 2002; Gopinath & Jameson 2005, abstract]"; P "[Hall 2002; van der Weide 2005; Nadarajah & Jameson 2007, abstract]") | V :138-139; H :143-144; O :130-131; P :134-136 | rubino_2018 :580 READ-INTEGRAL (covers the HB-adjoint MACHINERY claim); Hall-Thomas-Clark 2002 / McMullen-Jameson / Gopinath-Jameson: NONE | rubino covered; the HB canon itself UNVERIFIED [KNOWLEDGE] |
| Steady adjoint-based shape optimization (Jameson 1988; Giles & Pierce 2000/2001) | YES 4/4 | V :308-315; H :326-328; O :323-324; P :397-405 | giles_pierce_2000 :516, giles_pierce_2001 :507 (registry rows exist); Jameson 1988: NONE (only wanted_nadarajah_jameson_2000) | Giles-Pierce covered; Jameson 1988 UNVERIFIED |
| Space-time / unsteady output-based DWR (Fidkowski line) | NO — every tree uses STEADY DWR/Richardson on the wave-frame or per-phase solves | — | wanted_fidkowski_luo_2011 :937 ff. (WANTED) | not needed if A2 holds (steady evaluator); the record's wanted rows stay owned by f2-c11 |
| Linearized harmonic / transfer-function corrector (Hall & Crawley 1989; Marble & Candel — cited by D1 §8 itself) | YES as estimator-only (O T.6); the record's D1 §8 :475 invokes "Marble-Candel-type transfer functions" | O :274-276; D1 :475 | NONE for either (grep marble/candel/crawley = 0) | RECORD-SIDE GAP: D1 §8 cites Marble-Candel with no registry row; UNVERIFIED [KNOWLEDGE] |
| Multi-fidelity TR model management (Alexandrov-Lewis 1998-2001; Peherstorfer-Willcox-Gunzburger 2018) | YES (O S7) | O :143-146 | NONE | UNVERIFIED [KNOWLEDGE] |
| RDE unsteady-specific loss accounting (Anand & Gutmark 2019 review; Kaemming-Paxson EAP) | YES (H SP-OBJ; P SP-OBJ; V SP7 D.A) | H :274-275; P :294-296 | kaemming_paxson_2018 :236 READ-INTEGRAL; Anand-Gutmark: NONE | EAP covered; review UNVERIFIED |

## 5. Proposed falsifier (what the Stage-B parties must agree on)

FALSIFIER-SP1 (measurement, executable at F2.ENGINE exit on the record contour [X-AKNO]/S18 W* at the record head count, before any TWIN arm runs):
compute, on the SAME design and the SAME thermo tables, (a) J_avg (rung 2, uniform trapezoid at the C62-audited K), (b) J_avg + St J_1
(the record's O(St) corrector via the steady sweep-perturbation solve, VI.4bis(ii)), and (c) J_exact from the wave-frame field by
[S-BLITE] helical space-marching under the certified L4 axial margin (or the C51 route-B march where legal), at THREE pattern speeds
Omega/2, Omega, 2 Omega with the data shape fixed (M-RED B-1 ladder). Report r_red := |J_exact - J_avg|/J and r_corr := |J_exact - (J_avg + St J_1)|/J
with two-level Richardson bands, and the fitted exponent p of r_red vs St.
- The INCUMBENT (frozen-time + corrector = the bar) SURVIVES iff r_corr + band <= b_TS/3 (the stricter of the trees' derived fractions,
  O's three-way split) at the record St AND p >= 0.8 (H's exponent rejector) on the case-A blowdown family.
- The incumbent is KILLED as the evaluator of the decisive number (A2 adopted for the TWIN) iff r_corr + band > b_TS/3 at the record St —
  then the TWIN metric of §6 must be amended to J_exact per arm (A-REPR is the amendment site) and the corrector stays a DESIGNER-side bar only.
- The incumbent is KILLED as a designer license iff r_red > b_TS on the record contour (O's third branch: the loop moves to the wave-frame
  engine, S-BLITE/route-B), which at St_plug = 1.41 the X-STSC license rule already anticipates.
- Rejector of the falsifier itself: the ladder must reproduce the quasi-steady limit as Omega -> 0 within band (V L0.2 both-direction test);
  a ladder that does not is a solver bug, not a verdict.
Fixed cost: 3 wave-frame marches + 3 corrector solves + K per-phase marches on one contour; zero new theory; the instrument is of record.

## 6. Knowledge rows to procure (identity | why needed | owner) — [KNOWLEDGE], never evidence

1. Hall, Thomas & Clark 2002 (AIAA J.) harmonic-balance canon — the trees' 4/4 rejection of HB under the pin cites it; C59's trigger clause needs the source when the pin weakens | F2-entry census window (C59 owner)
2. Lakshminarayana 1996 (turbomachinery rotating-frame steady practice) + Denton 1992 (mixing-plane averaging) — the adjacent-field practice the A2 evaluator and the SP-CARM "mixed-out state" comparator descend from; no row exists | F2.REPR (representation ladder, route-B/3-D rows)
3. Wang & He 2010 (rotating-frame turbomachinery adjoint) — the only cited precedent of an adjoint in a rotating steady frame; the S-BLITE Lemma-B lift claim should be bounded against it | F2.REPR / C51 route-B window
4. Paxson 2014, AIAA 2014-0284 (wave-fixed-frame RDE simulation) — the RDE-side precedent of the wave-frame steadification (T-T0's novelty bound must cite it) | P-1 claim gate (novelty query) + T-T0P write-up owner (F2 theory window)
5. Marble & Candel 1977 (compact-nozzle transfer functions) — cited by D1 §8 :475 as the corrector's cell-problem class with NO registry row; the record cites it, so the row is owed regardless of the diff | D1 owner at the next R4 batch (record hygiene, lint (xix))
6. Alexandrov, Lewis et al. 1998-2001 (first-order corrected TR model management) — A13 is NEW and cheap; if the panel adopts an r_red-driven corrected loop this is its canon | F2.ENGINE optimizer cluster (C31/C57 adjacent)
7. Anand & Gutmark 2019 (PECS review, combustor-side loss magnitudes) — the "is the nozzle the lever" honesty line 3/4 trees demand up front; the paper's lever-honesty paragraph needs a cited magnitude | P-1 claim gate
8. Jameson 1988 (continuous adjoint canon) — cited by 4/4 for the continuous-adjoint cross-check; wanted_nadarajah_jameson_2000 covers the discrete/continuous axis, not the 1988 source | f2 SP3 cluster (C31/C56 owner), low priority

## 7. Branch ledger (every branch seen; EXPANDED / PRUNED with reason / DEFERRED with trigger + owner)

| Branch | Status | Reason / trigger + owner |
|---|---|---|
| V T.1 / H (1) / O T.1 / P T.1 single mean state as designer | PRUNED | 4/4 keep it as COMPARATOR only (SP-CARM); no error term; record S0.1/arm C — not an SP1 candidate |
| V T.2 flux-consistent (homogenized, St->inf) equivalent state | EXPANDED (as diagnostic + comparator K.3) | the second limit of A5's ladder; SP-CARM's strongest single-state arm; no design role at measured St |
| V T.3 / H (2) / O T.2 / P T.2 quasi-steady multipoint designer | EXPANDED (A3, A4) | licensed conditionally on measured r_red (A4), never on St alone |
| V T.4 / H (3) / O T.3 / P T.3 wave-frame steady 3-D as evaluator | EXPANDED (A2) | the divergence of record; falsifier §5 |
| V T.4 / H (3)-marching / O T.3 as DESIGNER (S0.6 / S4 / S4) | DEFERRED | trigger: r_red > b_TS on the record contour (falsifier §5 third bullet) or St_plug worst case at F3.TWIN instance pin; owner F2.REPR (route-B/S-BLITE rows) |
| V T.5 / H (4) / O T.5 / P T.5 harmonic balance, time-spectral | PRUNED (A6) | dominated under the pin by 4 derivations; C59 trigger (weakened pin) stays with its owner |
| V T.6 / H (5) / O T.4 / P T.6 time-accurate 3-D as designer | PRUNED | HPC-class, out of §8 budget by 4/4; retained ONLY as pin monitor (A15, EXPANDED) |
| V T.7 / H (6) / O T.6 amplitude-linearized corrector about the mean | PRUNED (A16) | invalid at RDE eps ~ O(1) by 3/4; not the record's corrector object |
| P T.4 phi-averaged model + measured closure designer | DEFERRED (A12) | trigger: A13/route-B both fail the session cap at F2.ENGINE; owner F2.REPR hybrid row; its abandon rule = T-RED residual |
| P T.7 / S-14 small-St expansion instrument (c2 from two solves) | EXPANDED (A8) | subsumed by the exponent test of the §5 ladder; sharper statement of record = T-T3QS |
| V scaling CONJECTURE O(St eps^2) | EXPANDED (A8) | contradicts P's quadratic law; measured by §5; the record already carries both regimes |
| V Omega_p-sweep both-limit convergence test / H f-2f-4f exponent test / P 3-value St sweep / O St-by-L sweep | EXPANDED (A5) | = M-RED B-1; O's "scale L" variant PRUNED as a St instrument (changes the nozzle, confounds the exponent) |
| O r_red thresholds b_TS/3, b_TS / P 0.1 band_TS / V < Delta J_decisive | EXPANDED (A4) | fraction fixed by §5 measurement; owner = D6 G3 (S14 duty) |
| H "St < 0.3" cut | PRUNED | undeclared constant (brief §0 violation); H's own second criterion is A4 |
| O C_theta azimuthal-communication number (1/M_x)(L/ell_theta) / H M_Omega map + r* = (a+|u_theta|)/omega / P M_rel map | EXPANDED (A14 indicators; SP5/C51 relevance) | H L5's r* is the C51 route-B legality locus (swirl5f claim 6 of record); consumed by F2.REPR, not by SP1 |
| V tau_res = max over streamlines / H,O,P mass-weighted mean streamline | EXPANDED (A14) | pins findings :2566 to the problem-book definition; V's max reported as the conservative variant |
| O L2 Jensen-gap screen (S13) / H L4 ceiling + loss budget (S12) / V L0.3 ideal bound (S0.11) | EXPANDED (A10, A11) | Stage-0 negative-branch gate; owner proposed F2.ENGINE entry; record has the ladder, not the screen |
| H L3 rothalpy Jensen loss eps^2/8 | EXPANDED (A11) | NEW dry lemma; needs a refuter before any consumption |
| P DL-2 linear thrust law (choked) | EXPANDED (A9) | = T-T3 re-derived; consequence for SP1 = corrector matters only on N-channels |
| O S7 TR model management with RF-3D corrections | EXPANDED (A13) | NEW; candidate branch of the A4 rule at b_TS/3 < r_red <= b_TS |
| H L8 slice-defect residual r_theta + <lambda_3D, r_theta> predictor with measured effectivity | EXPANDED | = record T-RED reduction residual re-derived with an adjoint-weighted predictor; consumed by M-RED (E_theta debit B-2) |
| V/O/H uniform trapezoid K rule vs O graded nodes at the front vs H Richardson-in-K | EXPANDED (A7) | C62 alternatives 4 vs 2; owner F2 engine numerics cluster |
| P B.6 base-cavity time constant tau_b f (quasi-steady base for f < ~5 kHz, marginal above) | DEFERRED | SP-PB axis; trigger: F3.PLUG C61 closure window (the base's OWN Strouhal is a second time-treatment number the record does not carry); owner C61/N2 |
| P S-11 quasi-1-D unsteady screening | PRUNED | bell-only, no swirl/base; the record's quasi-1D is the X-STSC estimate with bracket, already superseded by the certified-march tau_n duty (findings :892) |
| V S0.9 / O T.6 linearized as O(eps^2) ESTIMATOR and sweep rejector | DEFERRED | trigger: the §5 ladder shows an eps^2 regime at scaled amplitude; owner M-RED (amplitude leg) |
| Record-side: VI.4bis(ii) unsteady-comparison route O5 | EXPANDED | remains the general route; the trees' A15 run IS an O5 instance |
| Record-side: S-P4F Fredholm solvability of the corrector | EXPANDED (3.7) | record ahead of trees; unchanged |
| Record-side: [S-T0P] quotient degeneracy of the naive periodic adjoint | EXPANDED (3.7) | record ahead of trees; unchanged |

## 8. Three questions (SP1-scoped reading of §G.3)

Q1 (is SP1 the right sharpening?): YES — 4/4 trees mark SP1 LOAD-BEARING and put its decision BEFORE the solver build (order of battle step 2 in H/P, step 4 in V, step 7 gate in O); the sharpening the trees add is that the question is two questions (designer rung / evaluator rung) with SEPARATE licenses.
Q2 (does answering SP1 answer Q0?): NO on its own — the trees are unanimous that the time treatment can only buy on T3-violating channels (A9) and that the pool is band-sized (A11); SP1 decides the CREDIBILITY of the decisive number, not its sign.
Q3 (separate rungs designer/evaluator?): YES, 4/4 derived — the record already separates them as "rung 2 + bar/backstop"; the diff moves the evaluator rung from bar to metric of the decisive comparison (A2), to be settled by the §5 measurement at F2.ENGINE exit and landed in A-REPR.

## 9. Pin table per road (SP1 roads)

| Road | Pins needed | Pins relaxable |
|---|---|---|
| Frozen-time per-phase + O(St) corrector (incumbent designer) | pure periodic single mode ONLY through the measure mu and the corrector's T0 anchor (VI.4bis(ii)); frozen thermally-perfect (solver); single phase | mode-mixture weights at zero structural cost (O L3, S3); corrector falls back to the O5 route when T0 fails |
| Wave-frame steady 3-D evaluator (A2; S-BLITE / route-B / pseudo-time) | pure periodic single mode STRICTLY (L1 void for counter-rotating pairs, H :135-136); axisymmetric S; frozen gas | nothing on the mode; n > 1 via 2pi/n sector |
| HB / time-spectral (C59 alternatives) | periodicity (single f); relaxes to two incommensurate frequencies at multi-frequency HB cost | the single-mode pin (that is its only reason to exist) |
| Time-accurate 3-D (pin monitor only) | none beyond frozen gas | all wave pins |
| phi-averaged + measured closure designer (P T.4) | single mode (closure extracted from one wave-frame solve) | none |

END OF SP1 DIFF JUDGEMENT.
