# INCUMBENT POINTERS — the record rows each Stage-A DIFF judge reads (S-REVIEW 2026-09-05)

Purpose: the diff judges (NOT agnostic by design) compare the de-novo trees
(`stageA_tree_<lens>.md`, four lenses) with the program's road and choices
OF RECORD. This file is a navigation index only (cite-only, zero
adjudication): every judge reads the cited anchors in the sources, never
this summary. Authority order: M0 (`docs/rde_nozzle_MASTER.md`) > D1-D7 >
registries > advisories. Prior de-novo evidence to reuse (2026-08-17,
formulation-level, 141 forks): `validation/sfoundations_raws_2026-08-13/
phaseA_tree_{variational,hyperbolic,optimization,propulsion}_CONDENSED.md`
+ their diff `phaseB_tree_diff.md` (48 ledger rows classified).

Common to every judge: `docs/choice_ledger.yaml` (62 rows; status enum
DECIDED / MIXED / SINGLE-AUTHOR / NEVER; `alternatives` + `evidence` +
`owner` fields); `docs/rde_nozzle_pipeline_decision_map.md` (stages 1-8,
§9 edges); `docs/rde_nozzle_MASTER.md` Part VI (:3052-3200 core; :4250-4299
F2-B0 block); `validation/TWIN_PROTOCOL_preregistration_2026-08-31.md`;
`validation/st_scoping_number.py` + `sreview_raws_2026-08-31/
st_scoping_number_run.log` (MEASURED St_n of record: bell 0.35-0.60 at the
record head count; plug class up to 1.41).

## SP0 — THE ROAD (level 0; judge answers the three §G.3 questions)
- The idea and its sharpening: M0 Part I :25-62 (three structural
  discoveries: T0 steadification exact for a single rotating mode; collapse
  dichotomy T3/T4; the measure selects the topology); D-MU :95-110; D-P
  :286-408 (the problem of record, requirement (v) bars).
- Time treatment of record: D1 §8 :451-478 (St := tau_n/t_c, "MARGINAL",
  P4 corrector mandatory, T0 backstop); M0 VI.4bis(ii) :150-160 of Part VI
  (both routes live: unsteady comparison O5 + steady sweep-perturbation
  corrector); D6 G3 :783 ("St|J1| large" threshold NEVER derived — S14 duty);
  [T-T0] Theorem 3 M0 :512 ff. (wave-frame exactness); [T-T3] :746 ff.
  (collapse, fixed wall); [T-T4] :2294 ff. (plug simultaneous
  optimizability).
- Wave-frame road of record: M0 Part V :3008-3050 incl. the [S-BLITE]
  block :3027-3050 (3-D helical space-marching at marching cost, adjoint
  lifts by Lemma B); ledger C51 (implicit BVP vs azimuthal marching, NEVER;
  route-B); claims S-BLITE (`docs/claims_registry.yaml:1536`), S-T0P
  (:1900), T-T0P (:2044).
- Reduction/adequacy chain of record: [T-DISC] M0 :977 ff.; [T-RED] :1734
  ff. (delta and L_H UNDERIVED); [R22F-FORCHETTA] :1283 ff. (bracket, not
  adequacy; worst-direction marker); M-RED campaign row in
  `docs/findings_registry.yaml` (`pipeline:m-red-campaign`); decision map
  Stage 7 (OPTSHIFT: argmax-shift routes SCHEMA-only).
- U3' choking premise OPEN: D6 F2a block :160-213 (U3 stays PREMISE-OPEN
  until U3' closes); `validation/ADVISORY_rde_choking_2026-08-11.md`.
- Decisive experiment of record: TWIN protocol §1-§4 (question, truncated
  plug, case A, two arms P vs C at the mean state); D6 G2 :779-782 (value
  gate ~1% Isp, thrust-stand anchor); F1b twin precedent (D6 F1b status
  block: +0.51% in-class, cert-limited).
- Ledger rows at level 0 (none exist as level-0 rows — the judge proposes
  them): C59 (temporal form of the functional, NEVER, "canonical inside
  the pin"), C57 (global exploration tier, MIXED), C62 (phase quadrature).
- Adjacent-field prior check (§H.3): harmonic-balance / time-spectral
  adjoints (`docs/literature_registry.yaml:580` Rubino 2018 exists); space-
  time DWR line (:937-952 wanted rows); turbomachinery rotating-frame
  practice: NO row found by grep (candidate [KNOWLEDGE] census rows).

## SP1 — TIME TREATMENT
D-MU + scope note; D1 §8; VI.4bis(i)(ii); C59; C62; [T-T0]; P4 corrector
(D1 §8 + M0 D-P (v)); S-P4F (`claims_registry.yaml:643`); [X-STSC] numbers.

## SP2 — FLOW-FIELD SOLVER CLASS
M0 VI.2 (rotational characteristic march, Zucrow Ch.17 class); D-S1 :141-
285 (solution class S1, canonicity, fitted fronts [T-XWS], C-MAJDA, U3/U4
front chain); ledger C49 (fitted-front marching vs adjoint-consistent
capturing vs two-tier, MIXED); C9-C14, C22 (march laws); D6 F2a contact/
slip default (:160-213); decision map Stage 3; GENO = read-only oracle
(START_HERE); `docs/rde_nozzle_G0_decision.md` §4.

## SP3 — SENSITIVITY INFORMATION
M0 VI.3 (closed-form adjoint where smooth; reverse-AD of the fitted march
with implicit rules; O3 dot-product certificate); VI.4bis(iv); ledger C56
(adjoint realization per role, MIXED), C58 (differentiable-stack
foundation, MIXED), C44 (FD steps); claims X-O31CS (complex-step primal-
independent audit; grep `id: X-O31CS`); memory directive point 8 (discrete
vs continuous adjoint / adjoint-free axes — recorded in
`choice_ledger.yaml` C31 alternatives + `VERDICT_engine_cluster_2026-08-31.md`).

## SP4 — OPTIMIZER
M0 VI.5 (TR-SQP on spline dofs, Riesz metric, active set, bundle, deflated
continuation, sector tournament); M0 Part VI ladder + margin-multiplier KKT
(grep `LADDER` / `margin multiplier` in Part VI); ledger C31 (engine,
MIXED; [P-IPADJ] A/B), C57 (global tier, MIXED — F2-B0 verdict V-C57 in
`validation/f2b0_raws_2026-08-31/VERDICT_engine_cluster_2026-08-31.md`),
C60 (NAND vs SAND, MIXED — NAND structural reason in M0 :4250-4299), C27
(KS aggregation), C28 (cert-frontier representation), C38 (outcome-II
declaration), C23 (record-failure policy = certify-then-accept P4 gate),
C32-C37; decision map Stage 6 + surface A; obstruction history: memory
s20-adaptive-obstruction / s22-f1-governor-o4 (class-construction
mechanism, margin INACTIVE, K_disc~A_0 bridge FALSIFIED) — log files
`validation/PROGRESS_2026-08-07_S20_adaptive.md`,
`validation/PROGRESS_2026-08-11_S22_governor.md`.

## SP5+SP6 — REPRESENTATION FRAME + PARAMETRIZATION
D-DOM :65-72 (spline manifolds per sector, configurations = outputs); M0
VI.1 CycleFamily contract (4-field + swirl rows D.13/D.14/D.16); D6
addendum F2.REPR :1159-1195 (ladder: 4-field axial / five-field / route-B
azimuthal / hybrids / 3-D-per-phase); claims S-5F (:617), S-N6SO (:630);
ROUTE-B (decision map Stage 2); R22-CFD scheduling (Stage 2/8); ledger
C1-C8 (basis class, BCs, knots, dof policy), C4 + [X-AKNO]
(`claims_registry.yaml:1290`, FAILING of record); `validation/
swirl5f_panel_2026-08-19/DISPATCH_swirl5f.md`; F2.REPR carrier
`validation/ADVISORY_F2REPR_prompt_2026-08-31.md`.

## SP7 — DATA INGESTION + PHYSICAL PINS
D-CONTRACT + L4-CERT :111-140; D1 §4 + §4.3bis (mixed interface decision
tree) + §9 hypothesis ledger :481-520; D6 Annex B :1133-1157 (cases A-G,
generators); M0 VI.1 generators + BLOCKING PINS B-1/B-2; ledger C50, C52,
C53, C54, C55; gate G6 (D6 :800-816); scope pins (memory files:
periodic-wave-data-scope, scope-pins-frozen-thermally-perfect —
recorded in M0 D-MU scope note + VI.4bis header + TWIN §2-§3); TWIN §3
(case A pinned for the decisive test, flip clause).

## SP8 — CERTIFICATION PHILOSOPHY + STABILITY
M0 VI.6 (certificate stack, NOTHING SHIPS OUTSIDE A VERDICT); F2-B0 block
:4250-4299 (certificate = property of (tree, recorder, env), PRACTICE on
three instances; A-1 margin rule); ledger C11 (DWR target vs Richardson
referee), C19, C20, C21, C41, C42 (K_RICH roles), C43, C18/C17 (NTF
block M0 :3654 ff.); TWIN §9 A-1; S-CERT verdict of record
(`validation/PROGRESS_2026-08-13_Scert.md`, NON-CERTIFICABILE 2 P0);
closure-aware staleness gate `tests/test_claims_lint.py` (envfp, fail=
grammar); FAILING carriers X-O32 (:1262), X-LOCD (:1332), X-AKNO (:1290)
in `claims_registry.yaml`; findings rows `record-path:cert-verdict-
recorder-dependence` (grep).

## SP9 — THE DECISIVE EXPERIMENT
TWIN protocol §1-§9 integral; D6 G2 :779-782; PB-2 (D1 §10 :522-575);
ledger C61 (base-pressure closure, NEVER), H20 (free plume boundary, no
home), D-44 gate, P34 staged-evidence hierarchy (decision map Stage 8);
F1b twin (D6 F1b block; `validation/PROGRESS_2026-08-12_S24_f1b.md`);
[X-STSC] St numbers on the plug class; findings `twin-protocol:
preregistration-2026-08-31`.
