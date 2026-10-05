# TWIN PROTOCOL — PRE-REGISTRATION OF RECORD (F2-B0, 2026-09-05)

Deliverable of F2-B0 order 7 (carrier `ADVISORY_F2B0_prompt_2026-08-31.md`
§C.7). Consumer: the F3.TWIN executor + every intermediate step that must
not drift from the decisive comparison (F2.REPR pins the representation
field; F2.ENGINE builds what both arms run on). Registered as findings row
`twin-protocol:preregistration-2026-08-31` (path critical, owner F3.TWIN).
This document is BINDING: a TWIN run deviating from it without a DATED,
DECLARED amendment in this file is REJECTED by rejector R-TWIN-0.

## 1. The question (quoted discipline, not restated)

Does the per-phase cycle-averaged design method BEAT the classical
fixed-design at identical constraints, on the sector where the break
theorem lives — and by how much? Head-to-head, kill-or-validate, both
outcomes publishable (atlas CH6 :440/:490/:712; comparator of record =
ZERO computed instances exist anywhere in the literature).

## 2. Configuration (FIXED)

- **Sector: TRUNCATED PLUG** (the F3 GEOMETRY CLASSES sector, D6:214-227).
  This is NOT the bell/TOC sector of the F1b twin (+0.51%, cert-limited,
  current-sector only — advisory E). The break theorem's arena.
- Geometry class: plug spike with declared truncation fraction; truncation
  and base handled by the C61/N2 base-pressure closure (p_b model of
  record at the F3.PLUG window; the closure CHOICE is C61's — this
  protocol only requires it be THE SAME OBJECT in both arms).
- Flow model: axisymmetric, frozen thermally-perfect mixture (scope pin
  P1), tabulated thermo backend (DIR-THERMOTAB; Cantera = sole production
  generator), margin/certification stack as of the F2.ENGINE exit.

## 3. Data class (FIXED, with the declared flip clause)

- **Case A of D6 Annex B (:1142)**: specs only (propellant, phi, mean
  pressure, annulus geometry, Pa) → Cantera CJ/HP → S-H matching →
  exponential blowdown → (P0, T0, gamma)(xi), mu log-uniform. Interface
  I3. **Active channels N1, N2 (truncated plug / duty split), N4 — NOT
  N3.**
- DECLARED CONSEQUENCE (the S-ROADMAP lever, now discharged in the
  pre-registration): this protocol does NOT require case-B data, so the
  `non-critical` tags on the F2a contract rows for richer-than-case-A
  ingestion DO NOT flip. If a future amendment moves the TWIN to case B,
  those tags flip in the SAME amendment (their named falsifier).
- Propellant pin: CH4/O2 (the engine's exercised table class of record).
- TWO-STAGE PRE-REGISTRATION, declared: the CLASS and every rule in this
  file are pinned NOW; the numeric instance (phi, mean Pc, annulus radii,
  eps, L, truncation fraction, Pa) is pinned at F3.TWIN opening by a
  measured command BEFORE any arm runs, in an amendment block appended
  here. No decision rule below depends on the instance values.

## 4. The two arms

- **Arm P (per-phase method)**: Sigma* = argmax of the cycle-averaged
  functional J_avg over the certified design class, driven by the
  F2.ENGINE gradient/certificate machinery, consuming the FULL per-phase
  family {(P0,T0,gamma)(xi), mu}.
- **Arm C (classical)**: the classical design of the SAME geometry class
  at the I4 interface (⟨Pc⟩, T0, gamma — mean conditions only): the
  literature's fixed design (Rao-class plug / peak design at mean point),
  built by the SAME engine and certified by the SAME stack (independent
  classical route as cross-check where available, GENO oracle class).
- **Evaluation**: BOTH arms evaluated on the SAME cycle measure mu
  (arm C is designed blind to the cycle, but evaluated on it — that is
  the honest comparison the record's theorems address).
- **Representation of BOTH arms: PLACEHOLDER — pinned by F2.REPR.**
  Declared per finding plan:representation-ladder-3d-counterpart-no-named-
  d6-step (trigger: "the TWIN protocol pre-registration (representation
  of both arms must be declared)"): the representation field of this
  protocol is the ONE open field; F2.REPR's dated verdict (4-field axial /
  five-field / route-B / hybrid) lands here as amendment A-REPR, IDENTICAL
  for both arms. Until then no arm may run (R-TWIN-5).

## 5. Identical constraints (the premise of the whole comparison)

Both arms run under the SAME constraint vector, enforced by rejector:
1. eps (area ratio) — same value, same feasibility tolerance (derived,
   not magic; the cross-unit tolerance repair of finding
   variational-driver:cross-unit-and-slack-tolerances lands BEFORE any
   TWIN run — its near-vacuous slack would void constraint identity).
2. L (length) — same cap.
3. Truncation fraction — same value.
4. p_b closure — same C61/N2 closure object, same parameters.
5. lip/regularity class + margin floors + certification floors — same.
6. Same thermo tables (same generator run, content-hashed), same mu
   (content-hashed), same representation (A-REPR).

## 6. Metric, bands, decision rule (PRE-REGISTERED)

- Metric: cycle-averaged Isp (equivalently J_avg normalized by the
  metered feed) per arm; **delta := (Isp_P − Isp_C)/Isp_C**.
- Bands: every delta quoted ONLY with its derived band stack (two-
  resolution Richardson K_RICH-safeguarded + certificate-stack terms +
  representation-class term while A-REPR carries one). No bare deltas.
- **Materiality threshold: ~1% Isp, with the declared band 0.5-1% =
  thrust-stand-class experimental accuracy** (external calibration
  anchor, D6:779-782 note of 2026-08-19 — note-class anchor, quoted as
  such). Pre-registered reading:
  - **MATERIAL** (delta − band_upper > 1%): the method PAYS on this
    sector at this data class → the program's value claim, gated D-44 +
    G5 before any public form.
  - **SMALL** (delta + band_upper < 0.5%): **the literature is right at
    this rank** — the classical fixed design is adequate at case-A data
    on this sector; publishable honest outcome; program pivots per the
    G2 wording (certification/operability/duty-split value).
  - **INTERMEDIATE** (delta in [0.5, 1]% or bands straddle a boundary):
    NOT decidable at the thrust-stand rank; pre-registered duty =
    refinement ladder (band-shrinking) OR declared stop with
    "indistinguishable at experimental rank" as the finding. Never a
    victory claim from this branch.
  - **NON-CONCLUSIVE** (|delta| ≤ band): quoted as such; refinement duty;
    no claim.
- STOP RULE: the campaign stops when the band is small enough to place
  delta in one branch (target: band ≤ 0.5% abs on delta), or when the
  certified refinement ladder is exhausted → the reached branch is THE
  result. Both outcomes were publishable before the first run: this
  paragraph is the pre-registration of that fact.

## 7. Rejectors (named at pre-registration; each must be able to FIRE)

- R-TWIN-0 protocol-drift: any run whose config/data/constraint hash
  set differs from this file (+ dated amendments) → arm result REJECTED.
- R-TWIN-1 constraint-identity: seeded test = perturb one arm's eps by
  2× its derived tolerance → the harness must REFUSE the pair.
- R-TWIN-2 wrong-design discriminator: the N3-class control (A1 brick-2
  lineage) must FIRE on a deliberately wrong design fed as either arm.
- R-TWIN-3 same-mu: mu content-hash printed in both arm Verdicts; hash
  mismatch → pair REJECTED (seeded test: re-draw mu for one arm).
- R-TWIN-4 certification parity: an arm ending certifiability-limited
  (outcome II, F1b precedent) → NO delta quoted; branch declared
  cert-limited with the FULL S24-class branch bookkeeping.
- R-TWIN-5 representation parity: A-REPR unset, or arms at different
  representations → runs refused.
- R-TWIN-6 objective-domain guard: [OBJ-DOM-IMPL] must be landed before
  the first Verdict consuming dJ/dthB feeds an arm (ship-gate E9,
  sequenced with DELTA-CARRIER; carrier order pinned at F2-B0 order 6).

## 8. Prerequisites (owners named; this file blocks none of them)

- F2.REPR verdict → amendment A-REPR (representation, both arms).
- F2.ENGINE exit (stratified march + certificates + extended margin).
- F3.RK1/B-RAOPLUG: RaoPlug S1/S2 fix landed in GENO OR single-oracle
  status declared (Rao-1961 spike Table-1: M_E = 2.4, theta_E = −8.25
  deg, gamma = 1.23 → eps = 3.81, X_D/R_E = 1.164, C_F = 1.58).
- F3.PLUG: H20 plume-boundary solve + C61 p_b closure + plug/C− mirror
  margin + vortex-sheet certification monitor (flipped-critical row).
- D-44 (adequacy-claim gate) + G5 (submission gate) on the claim side.

## 9. Amendment log (append-only, dated)

- **A-1 (2026-09-05, same window, evidence-driven)** — CERTIFICATION WITH
  MARGIN. Evidence: the F2-B0 closure-aware re-runs showed that the binary
  certification verdict of cert-MARGINAL designs (cert_worst within a factor
  K_RICH of the bound) flips with the active recorder and with the engine
  version (findings record-path:cert-verdict-recorder-dependence,
  cross-version instance; X-LOCD declared FAILING). Rule appended HERE (section 9) and
  binding as a tightening of R-TWIN-4; section 7 text is unchanged by the
  append-only discipline: an arm's final design is QUOTABLE only if it certifies
  with margin, cert_worst <= 1/K_RICH (K_RICH = the registered two-level
  safety constant of record, no new magic number) under the pinned recorder
  printed in the Verdict; a design in the band (1/K_RICH, 1] is CERT-MARGINAL
  and quotable only if BOTH recorders agree on PASS; any recorder/version
  change after an arm's run re-fires R-TWIN-0. Seeded test: a design at
  cert_worst 0.9 must be refused as quotable.
- **A-REPR (2026-09-30, F2.REPR, owner's decisions T1 and T2)** — REPRESENTATION, IDENTICAL FOR BOTH ARMS.
  DESIGN: each arm is designed on the per-phase, axisymmetric description WITHOUT swirl (the engine's four
  fields). This is the declared fallback of the F2.REPR step. CHECK: both final designs are re-evaluated with the
  free-vortex swirl per phase; a design whose low-pressure phases detach only with the swirl is reported as such.
  JUDGE: the difference delta of section 6 is read on ONE evaluator for both arms = the 3-D steady flow in the
  frame turning with the wave, by CFD (MOSE_open, rotating frame). Its value is a MEASURE, not certified by the
  engine's stack (declared). It becomes the evaluator of record when PILOT-WF has shown it reproduces the
  laboratory-frame thrust of one plug within one third of the thrust-stand band; until then no arm may be quoted
  (R-TWIN-5 stays armed on the evaluator). Re-owned with triggers: the five-field swirl engine and the wave-frame
  marching solver (F5b / F6).
- Instance pin at F3.TWIN opening. Amendments A-2..A-15 of the review are PROPOSED, not applied (owner).
- **A-INST (2026-10-05, F3.TWIN opened; owner's word "vai con il piano", 2026-10-05 ~15:20, on the plan "the decisive
  comparison on the plug: walks to convergence, bands at two resolutions, CFD 2-D and 3-D on both designs")** — THE
  INSTANCE, PINNED BEFORE THE ARMS' FINAL RUNS. Written while both arms are being resumed (2026-10-05 15:37) and before
  any of their new segments is read.
  REHEARSAL DECLARED: the SDT walks of 2026-09-30/10-01 (A 24 segments, B 24, the plug + cowl pairs) and their table
  (+1.43 against +1.09 percent over Rao at the mean state, tool only) are the REHEARSAL of this twin, not its result.
  INSTANCE (content hashes md5[:8]): data = CycleFamily v0 case A, CH4/O2 phi 1, Pcp 20 atm, Ti 200 K (Stechmann-
  Heister-Harroun matched cycle, 12 equal-time sectors of the blowdown; mean P0 20.5 atm, T0 3132 K, gamma 1.1935):
  `validation/_cycle_family/sdt_ch4_phi1_pcp20/family_K12.json` a310b43d (= mu, both arms evaluated on it),
  `gas_mean.json` 2ca9effc, `phases_cfd.json` 8302efd2 (the CFD's sector states). Hardware = THOR annulus exit, inlet
  M 1.556 between y 0.792 and 1.000, internal nozzle -10 deg, hub arc 6 mm, cowl to its lip at x 35.20 mm (r_lip
  65.80 mm), all FIXED and identical (TWOP_FIX of the start). Constraint vector of section 5: (1) eps = pi r_lip^2 / A*
  is fixed by the fixed lip (identical by construction; the plug's tip radius is free and becomes the base); (2) L =
  87 mm from the annulus exit; (3) truncation = the cut at L (the same cap TWOP_CAP 0.8 in both arms); (4) p_b closure =
  the open wake p_b = p_a in both arms (Sule-Mueller open-wake case), and the base is NOT judged by the 3-D evaluator
  (its far field drains the outside air: finding waveframe:far-field-406-drains-outside-air); (5) class = no fold in
  region R and the channel at the MEAN state (`validation/_rde_tournament/stech/class_nofold_2026-09-28.json` 4e505fba),
  Summerfield separation in class, the per-cell certificate (A1_NEWTON_RESCUE=1); (6) representation = A-REPR plus the
  wall basis `validation/_plug_contest/SDT/twin_inputs/basis_plug_only.json` f0a01aed (12 numbers: the plug radius at
  11 stations from 15.6 to 79.6 mm and at its tip), start for BOTH arms = the Rao graft
  `validation/_plug_contest/SDT/twin_inputs/start_rao_sdt.json` a7997732; ambient p_a/P0 = 0.024378 (0.5 atm).
  ARMS: P = the TR-SQP walk with the 12 phases in J (TWOP_MU = family_K12, class at the mean state); C = the SAME walk on
  the mean state (the classical side of record: the fixed-inlet variational optimum at the mean point, owner's rule of
  2026-09-28). Rao's plug at the mean state (GENO) is reported as the literature anchor, not as an arm.
  STOPPING RULE (identical): the walk's own stop (a trial rejected at the radius floor, no motion, or two sub-floor
  steps in a row) or 64 segments of 12 iterations, whichever comes first; a budget stop is declared as such and the
  arm's |grad| at the landing is printed against its measured gradient floor (stationarity is then NOT claimed).
  METRIC: same inlet hardware and same mu, so the metered mass flow is the same in both arms and the Isp ratio equals
  the C_F ratio: delta = C_F(P)/C_F(C) - 1, every C_F over the 12 phases of mu.
  BANDS: the tool at two resolutions (the record rung K 140 + 123 stations, N 31, and K 280, N 61; Richardson with
  K_RICH); 2-D Euler per phase at levels c and f; 3-D at the 2-degree grid with the 1-degree term of PILOT-WF declared.
  CERTIFICATION: A-1 applies (quotable only with cert_worst <= 1/K_RICH under the pinned recorder).
  EVALUATOR GATE (A-REPR): the 3-D wave-frame CFD becomes the evaluator of record only if the laboratory-frame twin of
  ONE plug reproduces its wall thrust within one third of the thrust-stand band (0.17 percent of C_F): run LAB-WF,
  2026-10-05, Rao's plug on this instance, MOSE_open dcc627d8, same mesh/scheme/far field, the inlet as BC 410 turning
  at 6364.5 Hz (`RDE/Nozzle/labframe_case.py`, job 304078, reader `RDE/handoff/plug_2026-09-29/compare_lab_wave.py`,
  pass line written in the reader before the run ended). If LAB-WF fails, the evaluator of record is the
  laboratory-frame run itself, for both arms.
  SWIRL CHECK (A-REPR): both final designs re-evaluated with the free-vortex swirl per phase.
  REJECTORS: R-TWIN-0/3 (the hashes above printed in both arms' verdicts), R-TWIN-4 + A-1, R-TWIN-5 (A-REPR + the gate);
  R-TWIN-6 does not apply (the plug arms do not consume dJ/dtheta_B, the bell kernel's angle; declared); R-TWIN-1
  (perturbed eps refused) and R-TWIN-2 (wrong-design discriminator) are OWED before the verdict is quoted.
- **A-INST erratum (2026-10-05, same day, before any arm result was read)** — the cowl's lip is at x 35.196 mm, r 66.533 mm
  (the tool's lip state: the design files' `lip` entry, and the cowl's last station traced by the carrier), not r 65.80 mm:
  that number was the mesh summary's `r_lip`, which is the channel's outer line at x = L, not the cowl's lip. The constraint
  is unchanged: the lip state is identical in both arms (R-TWIN-1 compares `fix` and `lip` to the last bit).
- **A-REPR gate RESULT (2026-10-05, recorded 2026-10-06)** — LAB-WF PASSED: the laboratory-frame run of Rao's methane plug
  reproduces the wave-frame wall thrust to -0.058 percent (line 0.167): the walls -0.0065 percent, the rest the inlet
  table's time sampling (-0.051, predicted -0.050 from the table alone). The 3-D wave-frame CFD is the evaluator of record
  of this twin. Carrier [X-LABWF] (`validation/labwf_check.py`, data `validation/_labwf/`), page
  `validation/LABWF_lab_vs_wave_frame_2026-10-05.md`. Not shown: the base and the plume (the base is not judged).
