# STAGE A — DIFF JUDGEMENT, SP3 "INFORMATION FOR THE OPTIMIZER" (S-REVIEW 2026-09-05)

Judge: non-agnostic diff judge (persona = JPP referee on the decisive number + PM on the shortest credible path).
Inputs read integrally: the four de-novo trees (`stageA_tree_{variational,hyperbolic,optimization,propulsion}.md`),
`PROBLEM_STATEMENT_agnostic.md`, `DERIVER_BRIEF_agnostic.md`, `INCUMBENT_pointers.md`, `st_scoping_number_run.log`
([X-STSC] PASS: bell St_n 0.347-0.599 at the record head count = MARGINAL; plug class up to 1.415 = wave-frame rung REQUIRED);
prior de-novo evidence 2026-08-17 (`sfoundations_raws_2026-08-13/phaseA_tree_*_CONDENSED.md` SP3 forks + `phaseB_tree_diff.md`
rows C31/C32/C44 + items 11/13/14). Record anchors followed into the sources: M0 VI.3 (`docs/rde_nozzle_MASTER.md:3117-3131`),
VI.4bis(iv) (:3136-3166), S-BLITE block (:3027-3050), F2-B0 block (:4250-4299); ledger C56 (`docs/choice_ledger.yaml:760`),
C58 (:783), C44 (:622), C31 (:481), C57, C59; claims X-O31CS (`docs/claims_registry.yaml:1941`), X-TOCV, X-G0, X-G0AX,
X-A1IM, X-O32, X-MGOV (R-GRAD :1357), T-LEMB (:485), S-BLITE (:1536); findings oracles:o31-common-mode-hole (:1597),
engine:cross-lowering-gradient-floor (:339), oracles:o34-gradient-leg-unconsumed (:2764), benches:o32-adjoint-negative-control-missing
(:738); `validation/f2b0_raws_2026-08-31/VERDICT_engine_cluster_2026-08-31.md` (V-C57/V-C58/V-C60/V-C31);
`VERDICT_wave2.md` §2.10 (C56 gradient role); decision map rows C56/C44/C48/CLG/C57; TWIN protocol §1-§5; D6 :200-245, :530-560, :755-770;
literature registry rows giles_pierce_2000/2001, giles_ulbrich_2010 I/II, lozano_2018/2019, ancourt_2023, lozano_ponsin_2025,
hicken_zingg_2014, rubino_2018, zahr_persson_2016, schotthofer_2024, janc_2025, thakur_nadarajah_2025, breitkopf_ulbrich_2025,
shi_xie_xuan_nocedal_2022, sun_nocedal_2023, wanted_nadarajah_jameson_2000. Memory files NOT read (per brief).
INDEPENDENCE CAVEAT (LOG-4b) applied: every convergence below is labelled DERIVES (argument/lemma/cost in the tree) or NAMES.

## 0. Incumbent of record and its adjudication class

Gradient of record = reverse-mode AD of the FITTED characteristic march with implicit-function custom rules on inner
iterations, never unrolled, differentiating the fitted front never a captured smear (M0 VI.3 :3123-3129; VI.4bis(iv) :3160-3166;
[T-LEMB] :485 "block-triangular march => reverse-AD IS the transposed adjoint sweep, fitted front an explicit unknown");
closed-form corner/f2 adjoint (Prop. A3, lambda2 = -f2, P3) = ORACLE/INITIALIZER only; certificates: O3.1 dot-product at
machine precision (D6:538 2.7e-10 vs tol 5.1e-8 over the ENTIRE march, [X-A1IM]; [X-G0AX] 3.4e-12 at the fitted shock brick);
[X-O31CS] complex-step PRIMAL-INDEPENDENT audit (double implementation, h = 1e-20, CS4 negative control demonstrating and
closing the O3.1 common-mode hole; COVERAGE = interior unit process only, wall/axis/legge/composition = registered residual);
[X-G0] 52/52 unit-process Jacobian vs central FD with derived tolerance; R-GRAD = AD MARGIN gradient vs two-step Richardson FD
with derived band + corrupted control ([X-MGOV], [X-DEFTW]) — NOTE: R-GRAD covers the KS-margin gradient, NOT dJ/dSigma of the
thrust objective on the assembled march; [X-TOCV] verifies dJ/dSigma "by O3.1" only; the whole-march cross-code gradient leg
(JAX adjoint vs GENO FD, protocol pre-registered, K_RICH band, corrupted-tangent control) is UNCONSUMED of record, gated by the
GENO thrust double-count fix (findings :2764). Steps: C44 fixed sqrt(eps)*scale / eps^(1/3)*scale (MIXED, More-Wild never weighed).
Lowering discipline: ONE lowering per gradient comparison (findings :339, ~1e-8 rel cross-lowering floor).

ADJUDICATION CLASS = **MIXED** (adjudicated-split with refuter of record, not a single DECIDED-with-advocate row): C56 gradient
role CLOSED-CONSUMED at wave-2 §2.10 (discrete AD-adjoint = realization; continuous characteristic-native line = frame + referee;
dual-consistent synthesis = the combination, F11d residue); C58 JAX-primary REAFFIRMED at F2-B0 on corrected support with the
9(e) delta contract (a)-(g) still owed; C57 adjoint-free axis = Form-2 genuine advocate at F2-B0 with the user-ratified pilot
pinned to F2.REPR; C44 SINGLE-AUTHOR-derived incumbent inside a MIXED row (duty F2-C44-FDSTEP). The 2026 DELTA-SWEEP was
performed INLINE in this judgement (§6): registry-bounded 2023-2025 rows re-read + three web queries (2026 arrivals listed as
[KNOWLEDGE] rows, never as evidence). Nothing found flips the incumbent.

## 1. Table of approaches (every SP3 approach the four trees propose)

| # | approach | lenses (tree location) | class | derives/names | record anchor | weight on Q0 | changes credibility / cost |
|---|---|---|---|---|---|---|---|
| R1a | discrete AD-adjoint (reverse mode, adjoint of the residual / implicit rules, not of the iteration) as the gradient of record | V G.2 (:312-315), H SP3(1) (:326), O I.3 (:321-322), P G.3 (:394-396) | CONFIRM-candidate | 4/4 DERIVE (exactness for the discrete J + one adjoint per gradient; H adds the block-triangular backward-march argument) | C56 gradient role (`choice_ledger.yaml:760`; VERDICT_wave2 §2.10); VI.3/VI.4bis(iv); [T-LEMB]; X-A1IM/X-TOCV | medium | credibility UP (8/8 across two de-novo windows: prior FORK-20/29/25/14); cost unchanged |
| R1b | ...of a CAPTURED FV solver with smooth limiter (object differentiated) | V F.2+G.2 (:274-277, :322-328), O I.3 + discontinuity para (:327-331), P G.3 (:401-405) | DIVERGENT (3/4) vs H CONFIRM (fitted, :332-337) | V/O derive an optimistic reading (integral-functional gradient converges under refinement, SCHEMA); H derives the fitted case exactly | C49 (MIXED, SP2); giles_ulbrich_2010 II (lit :129-135: fixed-stencil discrete adjoint converges to a WRONG value across shocks, page-verified); lozano_2019; D6 F4b entry (:236-240) | high | credibility: the record's answer to "why not captured AD" is a page-verified theorem the trees do not cite; the divergent trees' own falsifiers (V :342-343 -> fit the plume; P M-3 :704 -> DFO) route back to the incumbent. Cost unchanged (C49 explorer tier already MIXED) |
| R2 | continuous adjoint (Hadamard / characteristic-native with jump conditions) as CROSS-CHECK / REFEREE only | V G.1 (:308-311, :340 "dual proof on a shock-free phase"), H (2) (:327-328, :338), O I.4 (:323-325 "discrepancy = discretization-error indicator"), P G.4 (:397-399) | CONFIRM-candidate | V/O DERIVE (finite-mesh inconsistency; discrepancy-as-indicator = the F11d logic), H/P NAME | C56 "continuous line = FORMULATION FRAME + REFEREE only" (wave-2 §2.10); ancourt_2023, lozano_ponsin_2025; F11d (Hicken-Zingg Def. 1) | low | none new — referee role already owned (F2-C11-ESTIMATOR-CAMPAIGN / F11d) |
| R3 | closed-form Rao/characteristic multiplier conditions = ORACLE/INITIALIZER only (never the multipoint gradient) | V L0.4 (:58-65) + G.5 (:318); P S-12 (:218-230, "ORACLE for SP3", falsifier = disagreement beyond MoC band) + G.5 (:399); H S9 (:189-199 initializer) | CONFIRM-candidate | V DERIVES (lemma: no common control surface for phase-dependent Mach); P DERIVES the oracle role with falsifier; H names | VI.4bis(iv) "Prop. A3 ORACLE/INITIALIZER only; lambda2(xi) = -f2 initializer (P3)"; VI.6 O1; M0:3319 "AD directional derivative vs Rao residual" | medium | credibility UP: the referee's "why not a cycle-averaged Rao?" gets an independent one-paragraph obstruction lemma (L0.4) convergent with the record's oracle-only role; cost 0 |
| R4 | dot-product / duality certificate with DERIVED tolerance | V V.1 (:332-333, c = O(N_ops)), H T-a (:339-340, measured N_ops), O (ii) (:337-338, c = 10 chosen) | CONFIRM-candidate | V/H DERIVE the tolerance law; O names with an undeclared constant (c = 10 = a magic number by the statement's own rule) | O3 (VI.3/VI.6); D6:538-540; X-A1IM/X-G0AX; findings :1597 (common-mode hole DEMONSTRATED) | low | none — executable of record; the record additionally KNOWS its blind spot (common-mode hole), which none of the trees states |
| R5a | primal-independent gradient check: complex-step | V G.3 (:316), H T-b (:341-342), O I.2 (:319-320 analyticity caveat: tables/min-max), P G.2 (:392-393 "complex-safe") | CONFIRM-candidate | O/P DERIVE the analyticity precondition; all 4 NAME CS; NONE derives the primal-INDEPENDENT double-implementation that closes the common-mode hole | [X-O31CS] (:1941: own quintic-Hermite twin, h = 1e-20, CS1/CS3/CS4/CS5, coverage interior-only); prior diff C44 note "CS interacts with custom_vjp route, option-with-precondition" | medium | credibility: record STRONGER than the trees' bar at unit level (negative control), WEAKER at whole-march level (coverage residual owner F2) |
| R5b | primal-independent gradient check: FD / Taylor-remainder with a NOISE-DERIVED step and slope check | V V.2 (:334-337, h* = (3 eps_J/M3)^(1/3), slope 2), O (i) (:333-336, h_min from roundoff floor, slope in [1.8,2.2]), P rejector (:409-414, e(h) = a h^p + c eps/h fitted at h,h/2,h/4; "10 x floor" undeclared) | DIVERGENT on C44 (noise-aware step vs incumbent fixed step); CONFIRM on the test itself | V/O/P DERIVE the step from measured noise (More-Wild philosophy re-derived); convergent with prior O-F22/V-F29 (diff :212-216) and with ON-DISK shi_xie_xuan_nocedal_2022 / sun_nocedal_2023 | C44 (:622, MIXED, incumbent "fixed sqrt(eps)*scale", More-Wild [TITLE] procurement row); [X-O31CS] honest catch (1e6x magic multiplier fired falsely) | medium | credibility of R-v rejectors: a mis-derived step = a rejector that cannot fire (S-CERT P0 class). Four independent derivations across two windows now challenge the C44 incumbent; owner F2-C44-FDSTEP stands, priority UP. Cost: small |
| R6 | WHOLE-MARCH cross-code / primal-independent gradient oracle (legacy MoC FD vs adjoint on the same state, tolerance = sum of both bands) | O (iii) (:339-341), P PR.3 + G.1 (:390-391, :555-557), V SP8 cross-code (:489-491, values), H (values via oracle) | CONFIRM-candidate | O DERIVES the tolerance; P derives the FD error model | findings oracles:o34-gradient-leg-unconsumed (:2764: <dJ/dW,dW/dp>_JAX vs FD_GENO(J)(p), K_RICH band, corrupted-tangent control) — UNCONSUMED, gated by oracles:geno-tocnoz-wall-thrust-double-count (critical) | high | credibility: the ONE gradient check the trees make MANDATORY (O decision criterion :344-345) that the record has NOT executed at the decisive scale; the objective gradient dJ/dSigma of [X-TOCV] is certified by O3.1 self-consistency + interior CS only. Cost: a GENO-side fix (critical finding) + one session |
| R7 | gradient mesh-convergence rejector (gradient order >= 1 under refinement; drop to 0 at a captured discontinuity rejects) | H T-d (:344-345), V V.3 (:338-339), P (:412-413 "GCI of the gradient itself"), O (:328-329 grid study) | CONFIRM-candidate-NAMED (fixed-topology FV assumption) | trees name a fixed-mesh-family rejector; none derives it for a FITTED march whose topology changes under refinement | [X-O32] (:1262 FAILING 2026-09-05 env-induced; statement: "ADJOINT rows NOT USABLE on a refinement ladder — refinement cannot hold the march topology fixed, clause LB-c2"); F11d order bookkeeping (hicken_zingg_2014); benches:o32-adjoint-negative-control-missing (:738) | medium | credibility: the trees' bar is UNMET of record on the fitted march for a STRUCTURAL reason (LB-c2) the record has named; the referee will ask — the record must either execute F11d at estimator sites (owned) or state LB-c2 + dual-pairing exponent + X-O31CS as the substitute. Cost: X-O32 re-stamp under TWIN A-1 |
| R8 | discontinuity-DISPLACEMENT Taylor test (perturb design so the FITTED front moves by delta; Delta J vs adjoint prediction; residual O(delta^2), measured exponent >= 1.8) | H T-c (:342-344) | NEW | H DERIVES (exponent criterion) | no record home as a primal-independent instrument: D6 F4b exit "jump-condition dot-product test" (:240) is self-consistency; X-G0AX fold-exponent is a different object; prior H-F29 front-terms designed-in (diff :288-291) | medium | credibility: targets EXACTLY the VI.3 claim "differentiate the fitted front, never a captured smear"; cheap (one perturbed march). Owner proposal: F2.ENGINE oracle block (G1 chain), executed on the X-G0AX fitted-shock instance before F4b |
| R9 | in-loop descent-direction rejector (Armijo fraction; 3 consecutive failures => gradient REJECTED, run halted) | O (iv) (:342-343) | NEW | O derives the rule | record has TR rho acceptance + C23 certify-then-accept P4 gate + REQ-NONSTALL zeroed-gradient fallback ([X-MGOV]); no rule promotes repeated step failure into a gradient rejection with halt | low | trivial cost; closes a silent-failure mode (cf. findings :655 NaN leak reduced res.optimality into a spurious PASS). Owner: [P-IPADJ] driver touch |
| R10 | second-order information: quasi-Newton (BFGS) in-flight + terminal FD-of-gradient reduced Hessian on the active null space | V G.6 (:319-321), O G.1 (:350-351, :366-367), H SP4 (:350-351), P X.1 (:436-437) | DIVERGENT (4/4) from C32 incumbent "fresh full FD Hessian per segment" | V/O DERIVE (n_design small; reduced Hessian only where (R-ii) needs it) | C32/C33 (MIXED, [P-QNCARRY]/[P-HESSREJ], win-asymmetry declared V-C32/C37); prior O-F17/23 HVP, V-F24 Lanczos (diff :168-173); C58 history: T2 FIRED at S18 with curvature measurement = the structural cost | medium (cost) | cost: the trees would remove the exact cost class that fired T2 (curvature + re-record); credibility: [P-QNCARRY] cannot WIN until the C28 frontier instance exists. Cross-reference SP4 judge; no new adjudication owed here |
| R11 | adjoint-free / DFO / BO as the gradient SUBSTITUTE | V G.4 (:317, > 5 params prohibitive, no KKT), H S7 (:164-173, equal-budget two-sided falsifier), O S8 + G.4 (:163-172, :356, :372), P S-7 + X.3 (:155-166, :425, :437-442) | CONFIRM-candidate (C57: exploration / cross-check / fallback, never the certificate-bearing channel) | H/V DERIVE (cost + certificate arguments; H's head-to-head falsifier both ways); O/P derive the family-bounded-gap role | C57 (MIXED; V-C57: user-ratified one-shot rival-paradigm pilot decided at F2.REPR; "adjoint-free at genuine best" = user directive axis 4); C58 9(e)(b) | medium | credibility of the user's "was there something better?" answer: 4/4 de-novo NO for the certificate-bearing channel, and 3/4 independently re-derive the MEASURED arm the record already owns (the pilot). Cost: unchanged (pilot already pinned) |
| R12 | surrogate gradients (GP/PCE posterior) | O I.5 (:325), P G.6 (:400) | PRUNED by the trees themselves (S8/S-7 only) | — | C57 alt | zero | not eligible for Stage B |
| R13 | "otherwise" information: exact-evaluator VALUES as first-order trust-region corrections of the reduced-model gradient (multi-fidelity model management) | O S7 + G.2 (:139-161, :351-352; Alexandrov et al. [abstract]), thresholds r_red <= b_TS/3 / b_TS (:280-282) | NEW (as a loop mechanism) | O DERIVES the license thresholds from the band budget | record: B-lite = exact METER of the rung-2 residual (S-BLITE :1536), P4 corrector = a BAR (VI.4bis(ii)), OPTSHIFT routes SCHEMA-only (decision map :174); no value-corrected loop | medium | cost/credibility via SP1/SP5: converts the reduction error from a bar into an in-loop correction; [X-STSC] says bell = MARGINAL (corrector mandatory) and plug (TWIN sector) NOT DEFENSIBLE alone -> DEFERRED to F2.REPR (A-REPR), owner SP1/SP5 judge |
| R14 | wave-frame 3-D MARCHING adjoint = backward marching (x-marching where u_x > a; theta-marching where \|u_theta - Omega r\| > a; near-axis r < r* not hyperbolic) | H L5 (:50-58) + S4 (:126-140) + SP2 (4)/(5) (:298-303); V S0.6 note (:133-135) | CONFIRM-candidate (S-BLITE Lemma-B lift) + DIVERGENT detail (theta-marching = C51 azimuthal-marching alternative, NEVER) | H DERIVES (type indicators, r* formula, cost N_x N_r N_theta); V names | M0 S-BLITE :3027-3050 ("adjoint lifts verbatim by Lemma B"; axial margin u_x - c >= delta; near-axis/subsonic pockets = FULL anchor); claims S-BLITE :1536; C51 (route-B, NEVER) | high (cost) | the biggest SP3 cost lever: [X-STSC] forces the wave-frame rung on the plug sector; H's independent result that an ANNULAR solid with r_min > r* is fully theta-hyperbolic makes the TWIN sector the CHEAP case for an exact marching adjoint. theta-marching adjoint = period-map fixed-point adjoint (NOT block-triangular) -> C60 SAND trigger (ii) territory. Owner: SP0/SP5 judge + F2.REPR |
| R15 | harmonic-balance / time-spectral ADJOINT inside the pin | V S0.7 (:137-143), H S5 (:142-151 Gibbs O(1/K) at the data shock), O S6 (:129-137), P S-5 (:132-144, dropped O(1) term) | CONFIRM-candidate (C59: cycle-average canonical inside the pin; HB/TS live only in weakened-pin regimes) | 4/4 DERIVE (equivalence to the theta-Fourier rotating-frame steady problem; Gibbs cost) | C59 (NEVER by binding scoping); rubino_2018, zahr_persson_2016, schotthofer_2024 | low (SP3) | none for SP3 (the adjoint form follows the time treatment); credibility of C59's binding scoping UP |
| R16 | data-sensitivity dJ/d(data), dJ/dw_k from the SAME adjoint (free) | H SP7 F (:412-413), O L3 (:42-43) + SP7 (:443-444), V D.F (:440-443) | CONFIRM-candidate-NAMED | O derives dJ/dw_k = F_k (trivial theorem); others name | prior diff item 11 (H-DATA adjoint-based data-sensitivity carrier, candidate row); TWIN §sensitivity; findings flatness-monitor | low | owner SP7 judge; no SP3 change |

## 2. Prose reasons (anchored)

**R1a/R1b — the core.** All four 2026-08-31 trees and all four 2026-08-17 trees put the discrete AD-adjoint as the
certificate-bearing gradient; none proposes the continuous adjoint as primary and none proposes an adjoint-free gradient
for the certified loop. That is eight independent derivations MODULO the LOG-4b exposure (the hyperbolic tree declared the
injection and its non-use; the others carry no repo ids). The split is on the OBJECT: the hyperbolic lens derives the incumbent
exactly — "with FITTED discontinuities in the marching engine the displacement is an explicit variable and (1) is exact; with
CAPTURED ones ... an O(h^0) spurious term possible at the shock" (:332-336) — which is [T-LEMB] + Giles-Pierce 2001 restated;
V/O/P differentiate a captured FV solver. The record holds a page-verified theorem against them (giles_ulbrich_2010 Part 2:
"fixed-stencil discrete adjoint converges to a WRONG value across shocks (pp.907, 910) — the trap is a theorem"), which NO tree
cites; the O tree's "integral functionals converge under refinement (SCHEMA)" (:327-329) is exactly the trap. The divergence is
C49's (SP2 judge); for SP3 it is DIVERGENT-and-record-refuted, and the divergent trees' own falsifiers hand the plume/shock back
to fitting. Weight high because the decisive TWIN sector (truncated plug, D6:214-227) carries the fitted oblique sheet + contact +
free plume — precisely the arena where a captured-AD gradient imports an O(1) front-term error.

**R3 — the user's "why not a cycle-averaged Rao".** The variational lens supplies L0.4 (:58-65): Rao's isoperimetric
reduction needs ONE control surface (the last left-running characteristic through the lip); phase-dependent inflow Mach numbers
give different last characteristics per phase, so no common control surface exists and the reduction fails except when all
phases share the characteristic net. This is an independent negative complement of the record's [T-T3] collapse dichotomy and
of VI.4bis(iv)'s "closed form = oracle/initializer only". The propulsion lens reaches the same role from the other side (S-12
"cycle-averaged Rao ... ORACLE for SP3, not the road", with the exact falsifier the record uses: disagreement with the discrete
adjoint beyond the MoC discretization band). CONFIRM with two DERIVING lenses.

**R4-R7 — the verification stack: where the record is stronger and where it is weaker than the de-novo bar.** Stronger:
the record knows and has demonstrated the O3.1 common-mode hole (transpose-consistent-but-wrong pairs pass the duality check at
machine zero) and closes it at unit level with a primal-INDEPENDENT twin ([X-O31CS] CS4); no tree derives the double-implementation
requirement — they all test complex-step/FD against the SAME code, which is enough for a wrong ADJOINT but not for a wrong
Jacobian shared by tangent and adjoint. Weaker, at the whole-march scale the referee will judge: (i) the thrust objective's
dJ/dSigma on the assembled march ([X-TOCV]) is certified by O3.1 only; the primal-independent AD-vs-FD band of record (R-GRAD)
covers the KS MARGIN gradient ([X-MGOV] :328-352, [X-DEFTW] :907-921), and the pre-registered cross-code gradient leg is
UNCONSUMED (findings :2764, gated by the GENO thrust double-count). All four trees make a whole-J Taylor/FD test mandatory
(V V.2 :334-337; H T-b; O (i) :333-336 + decision criterion :344-345; P :409-414). (ii) The gradient-order-under-refinement
rejector (H T-d, V V.3, P) is structurally obstructed on the fitted march (clause LB-c2 in [X-O32]: refinement cannot hold the
march topology fixed) and [X-O32] is FAILING of record (env-induced, 2026-09-05); the trees assume fixed-topology FV meshes. The
honest referee answer is: the dual-pairing exponent (S-LBML) + F11d at estimator sites + [X-O31CS] REPLACE the gradient-order
test, and the record must say so in one line. (iii) Steps: V/O/P all DERIVE the FD step from measured noise; the C44 incumbent
is a fixed sqrt(eps)*scale. With prior O-F22/V-F29 this is four independent derivations against a single-author incumbent, and
the two on-disk Nocedal rows (shi_xie_xuan_nocedal_2022, sun_nocedal_2023) already carry the method; F2-C44-FDSTEP's priority
rises, no new adjudication is needed. Both sides owe a derivation for their "10x" constants (P :412; O c = 10 :337) — the trees
are not cleaner than the record here.

**R8/R9 — NEW, cheap, eligible.** The front-displacement Taylor test (H T-c) is the primal-independent instrument for the
VI.3 claim itself and has no record home (the F4b "jump-condition dot-product" is a duality check). The Armijo-based
gradient-rejection rule (O (iv)) has no record home either; findings :655 (NaN leak reducing res.optimality into a spurious PASS)
is the failure mode it would have caught. Both are half-session-class duties, not panel questions.

**R10 — curvature.** 4/4 converge on quasi-Newton in-flight + terminal FD-of-gradient reduced Hessian, against the record's
fresh full FD Hessian per segment (C32). Record history matters: the C58 loop-speed falsifier FIRED at S18 with
"curvature measurement + re-record" as the structural cost (V-C58 item 1). The trees' posture removes that cost class. The
record's own [P-QNCARRY] is the measured arm but "cannot WIN today" (V-C32 REF-21). Cross-referenced to the SP4 judge; no new
row — the existing MIXED row with its win-asymmetry is the right home, and this diff is one more independent challenger.

**R11 — the user's named question, answered.** "Was there something better than the adjoint with a gradient-based optimizer?"
De-novo: no lens found a better CERTIFICATE-bearing channel; every lens quarantines DFO/BO to exploration, fallback, or a
global cross-check — and three of them independently prescribe the head-to-head as the decision instrument (H :169-172 two-sided
equal-budget falsifier; O G.4 :372; P X.3 :437-442 family-bounded gap). The record already owns that instrument (C57 pilot,
user-ratified, decided at F2.REPR jointly with S-5F/C49). The genuinely DIFFERENT information channels the trees add are R13
(evaluator values as in-loop corrections) and R14 (marching adjoint on the wave-frame rung), both representation-conditional.

**R13/R14 — the cost lever for the decisive sector.** [X-STSC] (measured 2026-09-05) puts the plug class at St_n up to 1.415:
"wave-frame / unsteady rung REQUIRED". So the SP3 question for the TWIN is not "which adjoint" but "what does the gradient cost on
the wave-frame rung". The record's answer is S-BLITE (Lemma B lifts to the helical x-march under the axial margin u_x - c >= delta;
the FULL anchor with Newton-Krylov + doubly bordered adjoint only where the camera enters). The hyperbolic lens independently
derives the same legality structure (L5: x-hyperbolic where u_x > a, theta-hyperbolic where |u_theta - Omega r| > a, near-axis
r < r* = (a + |u_theta|)/Omega never time-like) AND adds a fact the record does not state: an annular solid with r_min > r* is
FULLY theta-hyperbolic, so the truncated plug — the decisive sector — is the cheap marching case, while the full bell always
contains a non-hyperbolic core. theta-marching itself is the C51 "azimuthal marching" alternative (NEVER adjudicated, route-B):
its adjoint is a period-map fixed-point adjoint, not a transposed sweep — which lands in C60's SAND trigger (ii). This is the
one SP3 item that changes COST at the decisive number and it is DEFERRED to F2.REPR (A-REPR) with the SP0/SP5 judges as owners.

## 3. The three questions (§G.3, SP3 reading)

- Q1 sharpening: "gradient of record = discrete AD-adjoint of the fitted march + O3.1 + complex-step audit" is the RIGHT
  sharpening of "how the optimizer gets what it needs" for the certificate-bearing channel (8/8 derivations, two windows). It
  UNDER-sharpens the "or otherwise" half: the trees put exact-evaluator VALUES (R13) and a DFO global check (R11) INSIDE the loop;
  the record keeps them as a bar (P4 corrector), a meter (B-lite) and a pilot (C57). Not wrong, but the referee will ask for the
  reduction error as a correction, not only as a band, on the MARGINAL bell and the NOT-DEFENSIBLE plug.
- Q2 answers Q0? For the derivative itself YES at the level of exactness and self-certification; NOT YET at the level the trees
  (and a JPP referee) demand: the whole-march primal-independent gradient test on the thrust objective is unconsumed of record
  (§2 R6) and the gradient-order rejector is structurally obstructed (LB-c2). The decisive number's derivative credibility today
  rests on O3.1 + interior-process CS + 52/52 unit FD + the MARGIN-gradient R-GRAD. That is a duty gap, not an adjudication gap.
- Q3 separate rungs designer/evaluator: 4/4 trees say the adjoint lives on the DESIGNER rung only; the evaluator is value-only
  (V S0.4 "no adjoint needed for evaluation" :107; O S7 "no adjoint mandatory" :150; P H-1; H S11). The record agrees (B-lite =
  meter; TWIN §4 evaluates both arms on the same cycle measure). SP3 consequence: the TWIN needs no evaluator adjoint; it needs the
  designer adjoint on whatever representation A-REPR pins — Lemma B on the helical march is the cost lever (R14), and the H tree's
  r* result says the plug sector is the cheap case.

## 4. Pin table per road (SP3 roads)

| road | pins NEEDED | pins RELAXED / not needed |
|---|---|---|
| (a) discrete AD-adjoint of the fitted march [incumbent] | fitted class C49 (front as explicit unknown, Lax/Majda solvability); ONE lowering per comparison (C48/CLG floor ~1e-8 rel); converged-state certificates (C60 NAND); EOS-general tables (DIR-THERMOTAB); complex-safe twin for X-O31CS | gamma = const NOT needed (EOS-general); periodicity NOT needed for the gradient (only for the quotient functional) |
| (b) discrete AD of a captured FV solver (V/O/P) | smooth limiter; Giles-Ulbrich interior-smearing repair eps = h^alpha or adjoint kept continuous at the shock; contact-preserving flux; fixed-topology mesh family for the order rejector | relaxes the fitted-front machinery; relaxes nothing physical |
| (c) continuous / characteristic-native adjoint as referee | analytic frame (Ancourt 2023 / Lozano-Ponsin 2025 rows); dual-consistency criterion (Hicken-Zingg Def. 1) | never a realization; cannot referee itself |
| (d) DFO / BO gradient substitute | low-dimensional family (d <= ~10); an exact cheap evaluator; NO KKT certificate | relaxes differentiability across fronts / separation onset / base switching |
| (e) wave-frame marching adjoint (B-lite / theta-march) | axial margin u_x - c >= delta (x-march) OR r_min > r* (theta-march, C51 alt); single-mode pin (T0); 3-D axial-flux eigenstructure brick (G12-L1-3D) | Omega eigenvalue, camera, Newton-Krylov NOT needed on the marching branch |
| (f) evaluator-value-corrected reduced-model loop (R13) | an exact evaluator with GCI band < b_TS/3; first-order-consistent correction at the iterate | relaxes the need for an evaluator ADJOINT |

## 5. Branch ledger

| branch | status | reason / trigger + owner |
|---|---|---|
| discrete AD-adjoint realization (R1a) | EXPANDED | 8/8 convergence; CONFIRM |
| captured-FV AD object (R1b) | EXPANDED | DIVERGENT, record-refuted by giles_ulbrich_2010 II; routed to C49/SP2 judge |
| continuous adjoint as primary | PRUNED | 0/4 recommend; C56 referee role of record |
| continuous adjoint as referee (R2) | EXPANDED | CONFIRM; owned by F11d |
| closed-form Rao/multiplier as gradient | PRUNED | V L0.4 obstruction + P oracle-only; VI.4bis(iv) |
| closed-form as oracle/initializer (R3) | EXPANDED | CONFIRM, two deriving lenses |
| dot-product certificate (R4) | EXPANDED | CONFIRM; record knows its blind spot |
| complex-step audit (R5a) | EXPANDED | CONFIRM; coverage residual (wall/axis/legge/composition) owner F2 |
| noise-derived FD step (R5b) | EXPANDED | DIVERGENT vs C44 incumbent; owner F2-C44-FDSTEP, priority UP |
| whole-march cross-code / Taylor gradient test (R6) | EXPANDED | CONFIRM of an UNCONSUMED record duty; = the proposed Stage-B falsifier; owner F2.ENGINE oracle block after the GENO double-count fix |
| gradient mesh-order rejector (R7) | EXPANDED | NAMED; obstructed by LB-c2 of record; owner F2-C11-ESTIMATOR-CAMPAIGN (F11d) + X-O32 re-stamp |
| front-displacement Taylor test (R8) | EXPANDED | NEW; owner proposal F2.ENGINE oracle block, before F4b |
| Armijo gradient-rejection rule (R9) | EXPANDED | NEW; owner [P-IPADJ] driver touch |
| quasi-Newton curvature (R10) | DEFERRED | trigger = C28 frontier instance (win-asymmetry V-C32 REF-21); owner SP4 judge / [P-QNCARRY] |
| DFO/BO as gradient substitute (R11) | EXPANDED | CONFIRM C57 posture; pilot at F2.REPR is the measured arm |
| surrogate gradients (R12) | PRUNED | pruned by the trees themselves; zero weight |
| evaluator-value-corrected loop (R13) | DEFERRED | trigger = A-REPR at F2.REPR + measured r_red > b_TS/3 (= the [X-STSC] MARGINAL license); owner SP1/SP5 judge |
| wave-frame marching adjoint, x-march (R14) | EXPANDED | CONFIRM S-BLITE Lemma-B lift |
| theta-marching / period-map adjoint (R14 detail) | DEFERRED | = C51 azimuthal-marching alternative (NEVER); trigger F2.REPR route-B; owner SP0/SP5 judge; adjoint class = fixed-point (C60 SAND trigger ii) |
| HB / time-spectral adjoint inside the pin (R15) | PRUNED | 4/4 derive dominance inside the pin; C59 binding scoping confirmed |
| checkpointed unsteady adjoint (revolve) | PRUNED | H S6 / O S5 / V S0.8 reject on budget; C59 windowed alternative lives only off-pin |
| adjoint-based data sensitivity (R16) | DEFERRED | owner SP7 judge; prior diff item 11 candidate row |
| Hadamard boundary formula / Riesz metric (V G.1 form) | DEFERRED | owner SP4/SP6 judge (VI.5 Riesz representation of record) |
| second-order adjoint (adjoint-of-adjoint, V G.6 option) | PRUNED | V itself prefers BFGS + FD-of-gradient; prior O-F17 HVP line already in the C32 alternatives |

## 6. Adjacent-field prior check + delta sweep (registry-bounded + 3 web queries, 2026-09-05)

Considered by the trees: turbomachinery steady rotating-frame adjoint practice (O S4 tuple: Lakshminarayana 1996, Wang & He 2010
[abstract]; P DL-1 "sector + phase-lag/rotating-frame practice [textbook]"; H SP-CARM Denton 1992 mixing-plane) — YES, as the
evaluator/design frame; NO literature-registry row exists (consistent with INCUMBENT_pointers §H.3 grep). Harmonic-balance /
time-spectral adjoints (Hall-Thomas-Clark 2002 [full/abstract] in all four; McMullen-Jameson 2006, Gopinath-Jameson 2005,
Nadarajah-Jameson ~2007, van der Weide 2005) — YES, rejected inside the pin with derivation; registry covers the line only through
rubino_2018 (READ-INTEGRAL) + zahr_persson_2016 + schotthofer_2024. Steady adjoint-based shape optimization SOTA (Jameson 1988
[full] V/H; Giles-Pierce 2000/2001 all; Ulbrich 2002/03, Bardos-Pironneau 2003, Bressan-Marson 1995 for 1-D shock sensitivity in
V/H) — YES; the trees' newest SP3 citation is 2001-2003, whereas the record's SP3 corpus is 2023-2025 (ancourt_2023,
lozano_ponsin_2025, thakur_nadarajah_2025, breitkopf_ulbrich_2025, janc_2025). NOT considered by any tree: giles_ulbrich_2010,
hicken_zingg_2014 (dual consistency), the JANC-class differentiable-solver threat vector.
Delta sweep result: web queries (2026 discrete adjoint / shock-fitting / MoC; 2026 JAX differentiable compressible + RDE; 2025-26
HB/TS adjoint rotating frame) surfaced JAX-Shock (arXiv 2601.04400), JAX-FVM (arXiv 2607.07385), discrete-adjoint gas-kinetic
schemes (arXiv 2604.14567, 2606.14112), JANC (2025, registry :607), and the 2018-2021 HB-adjoint turbomachinery line
(Rubino-class; AIAA J 10.2514/1.J060175 overset HB-adjoint rotor planform). ALL are captured-scheme AD or HB-adjoint = the
paradigm the record already classifies (C49 explorer tier / C59 off-pin); none is a fitted-front / characteristic adjoint. The
incumbent is NOT flipped by anything on disk or found in 2026. These enter ONLY as [KNOWLEDGE] rows below.

## 7. [KNOWLEDGE] rows (identity — why needed — procurement owner); all UNVERIFIED unless a registry row is cited

1. Wang & He 2010 (turbomachinery adjoint in rotating frames, [abstract] in O) + Lakshminarayana 1996 + Denton 1992 — needed to
   census the rotating-frame steady adjoint practice for A-REPR/route-B — owner: F2.REPR [KNOWLEDGE] census (pointers §H.3).
2. Hall, Thomas & Clark 2002; McMullen & Jameson 2006; Gopinath & Jameson 2005; van der Weide et al. 2005 — needed only if the pin
   is weakened (C59 trigger) — owner: C59 trigger window (no procurement before the trigger fires).
3. Ulbrich 2002/2003 shift-differentiability; Bressan & Marson 1995; Bardos & Pironneau 2003 — 1-D front-sensitivity theory behind
   R1b/R8 — owner: F4b entry census (rides the giles_ulbrich_2010 / lozano_2019 entry condition, D6:236); breitkopf_ulbrich_2025
   [PARTIAL] on disk is the nearest row.
4. Squire & Trapp 1998 / Martins, Sturdza & Alonso 2003 (complex-step canon) — needed to cite the h = 1e-20 instrument of [X-O31CS]
   and the analyticity precondition (O/P) — owner: F2-C44-FDSTEP (shares the step/stencil duty); giles_pierce_2000 row mentions
   the test only.
5. More & Wild 2011/2012 (ECNoise) — needed by R5b — owner: already ONE deduplicated procurement row (C44 note, VERDICT_wave3 par.9);
   the on-disk shi_xie_xuan_nocedal_2022 and sun_nocedal_2023 rows carry the method today.
6. Alexandrov, Lewis et al. 1998-2001 (first-order corrected TR model management); Peherstorfer, Willcox & Gunzburger 2018 — needed
   by R13 — owner: F2.REPR agenda (SP1/SP5 judge), procure only if R13 is opened.
7. Christianson 1994 / Giles-Pierce 2000 fixed-point adjoint ("adjoint of the residual, not of the iteration") — the principle
   behind the custom_vjp implicit rules — owner: none needed (giles_pierce_2000 READ-INTEGRAL covers it).
8. 2026 arrivals: JAX-Shock (arXiv 2601.04400), JAX-FVM (arXiv 2607.07385), discrete-adjoint GKS (arXiv 2604.14567, 2606.14112) —
   needed to keep the JANC-class threat-vector line current (registry :607) — owner: litreview delta rider at F2.REPR; identity
   to be settled on the PDFs, no read claim.
9. Griewank & Walther 2000 (revolve) — named and rejected by H/O; no procurement (pruned branch).

## 8. Proposed Stage-B falsifier (the one the parties must agree on)

WHOLE-MARCH PRIMAL-INDEPENDENT GRADIENT TEST on the committed design of record ([X-TOCV] instance, ONE lowering pinned per
findings :339): (leg 1) Taylor remainder e(h) = |J(Sigma + h d) - J(Sigma) - h g.d| along >= 3 directions incl. one lip/corner dof,
step decade DERIVED from the measured objective noise eps_J (the accumulated Newton certification floor already reported by the
engine) via h* = (3 eps_J / M3)^(1/3) with M3 fitted from three steps; PASS iff the truncation-side slope lies in a band derived
from the measured curvature of e(h) (the trees' [1.8, 2.2] is a default, not a magic constant, and must be re-derived) and
|g_AD.d - g_FD(h*).d| lies inside the FD error band; NEGATIVE CONTROL: a corrupted tangent (2x band along one dof, the R-GRAD
pattern) must break the identity. (leg 2) the pre-registered cross-code leg <dJ/dW, dW/dp>_JAX vs FD_GENO(J)(p) (findings :2764)
once the GENO double-count fix lands. (leg 3, R8) the front-displacement test on the [X-G0AX] fitted-shock instance: measured
exponent of the residual vs delta >= a derived threshold.
KILL of the incumbent: leg 1 or leg 3 failing on any dof at any of three iterates (start / interior / optimum) while O3.1 passes —
that would prove the gradient of record wrong at the scale of the decisive number regardless of duality; leg 2 failing with the
control passing kills the cross-code oracle instead. PASS confirms the "why not X?" answer at whole-march level and leaves only
the C57 pilot (equal-budget head-to-head) as the remaining measured arm on the adjoint-free axis.

## 9. Panel recommendation

**CONFIRM-BY-DIFF** for the SP3 incumbent (discrete AD-adjoint of the fitted march + closed-form oracle + O3.1 + X-O31CS): eight
independent derivations across two de-novo windows; the only divergent axes (captured object -> C49/SP2; FD step -> C44 duty;
curvature -> C32/SP4) are already MIXED rows with named measured arms; the delta sweep (registry + 2026 web) finds no rival
paradigm. No Stage-B panel is owed for SP3; what is owed is EXECUTION of three duties the diff exposes as the credibility gap
at the decisive scale: the whole-march gradient test (§8), the LB-c2 statement + F11d at estimator sites, and F2-C44-FDSTEP with
its priority raised. The representation-conditional cost lever (R13/R14) is the SP0/SP5 judges' and F2.REPR's.
