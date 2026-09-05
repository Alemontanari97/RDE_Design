# ADJUDICATION v2 — NASA nozzle/inlet tools vs rde-nozzle-program (POST-REFUTATION)
(2026-08-31, exploration session. v2 supersedes ADJUDICATION_draft_v1.md. Authority chain: four digests -> four source refuters (REFUTE_NPAC / REFUTE_Rice2003 / REFUTE_repo / REFUTE_SUPIN [pending at time of writing, completeness-only impact]) -> record refuter (REFUTE_adjudication.md) -> completeness critic (CRITIC_completeness.md). Every weight below cites the deciding anchor. B/NB/PO = classification against the TWIN critical path of validation/ADVISORY_Sroadmap_prompt_2026-08-31.md :28-29 (F2-B0 -> M-RED -> TWIN -> CFD-2 -> P-1).)

## 0. Convergence status
- Reading coverage: complete (all pages, all computational cores) — CONFIRMED by refuters (NPAC 7/9 confirmed + 3 sub-claims refuted; Rice 10/12 confirmed, 0 refuted; repo 7/8 structural confirmed, fidelity class REFUTED).
- v1 STRONG tier: EMPTY after measurement against the record (REFUTE_adjudication §5).
- Net: the four sources serve exactly TWO named open duties of the record, confirm ONE registered finding, and otherwise inform horizon items. "Mostly landscape, little load-bearing" — now proven, not asserted.
- Residual open slot: SUPIN completeness audit (REFUTE_SUPIN.md) — cannot raise any weight (all SUPIN rows already LOW/HORIZON by record); can only add omissions.

## 1. Rows of record (weight | B/NB/PO | anchor | reason)

### Load-bearing (serve a NAMED open duty)
| Row | v2 weight | TWIN class | Deciding anchors | Content |
|---|---|---|---|---|
| L-1 G12-L1-3D symbolic cross-check | MEDIUM (new, UPGRADE) | NB | M0:3041-3042 (brick "symbolic carrier candidate", never executed); CH_REF F-2; Rice eqs. 9-11 (conoid rays), 15/29-33 (conoid compatibility) with REFUTE_Rice caveat: printed eq. 15/29 ψ-coefficient is a report typo (cosθ·sinθ vs required cosθ·sinδ) — use the code's `CompEqu` (3D_MOCGrid.cpp:2163-2180) or Armstrong, never the printed form | Third-party 3-D characteristic structure to check the axial-flux eigenstructure brick against, at zero cost. Only in-hand use touching a NAMED open duty. |
| L-2 Kliegel-Levine 1969 acquisition | PRIORITY 2 in D6 item 12 (new, UPGRADE) | NB (feeds F2-C12-STARTLINE-REJECTOR band term) | choice_ledger:281-291 (C12 requires KL 2nd-order mass-flow correction EVALUATED as band term); glossary:1271; findings:1162; literature_registry: ZERO hits "Kliegel"; CRITIC G4 (not on disk); REFUTE_repo item 4 (KLThroat transcription bugs shift interior start-line Mach by −8%/−14%; half the shipped IDL is the M≤1.5 clamp) | The formula's source paper is missing from the record while a wave-3-adjudicated protocol depends on it; the repo's implementation CANNOT substitute (corrupted). CRITIC G2-b: KL CD at γ=1.4, R=1 = 0.98950 vs shipped 0.984756 (0.48% gap) — the band term the host wants is exactly this number; new bug `1/96` at MOC_GridCalc_BDE.cpp:2946. |
| L-3 Third start-line lineage (repo KLThroat, post-repair) | MEDIUM conditional on repair (was LOW) | NB | CRITIC G6-a: GENO = Sauer-only (InitialValues_m.f90:55), no KL/Hall/3-D; host C12 incumbent = Sauer GENO-mirrored → host and GENO share ONE lineage; repo = only in-hand second lineage | Value exists only AFTER the 5+ transcription repairs and only as coefficient cross-check once the paper is on disk. |

### Fixtures / confirmations (no new duty; band-less)
| Row | v2 weight | TWIN class | Anchors | Content |
|---|---|---|---|---|
| F-1 Control-surface thrust identity (NPAC Eq.11 vs Eq.12) | SUPPORT | NB | findings:1589-1597 (owner F2 engine rebuild, trigger = first Verdict shipping both thrust forms); REFUTE_NPAC: Eq.57 ≠ identity unless λ=1 (λ is a model correction) | Independent-lineage citation + bookkeeping layout for an ALREADY registered finding. Exact oracle = Eq.11-vs-Eq.12 closure only. |
| F-2 Table-4 KAT (3-D on M4 perfect wall) | LOW as R5 oracle; DATA-VERIFIED as "must-beat" floor | NB (F6 horizon) | CRITIC G3: 36-div column REPRODUCED from shipped full_mesh.plt (mean M 4.0510, 3σ 0.0322, 181 pts); actual inflow M=1.1 (z=0.out), NOT 1.15181 (report Table 3 is the inconsistent party); azimuthal Mach std floor ≈1.4e-3 (M4Perfect), 1.3e-3 (cone10), 2.2e-3 (M4RAO); REFUTE_Rice: use mean-Mach row only (% row undefined); bias-attribution is author conjecture; REFUTE_repo: real mechanism likely the start-line clamp artefact | Quotable floor for the F6 demonstrator on axisymmetric input; cannot REJECT under R5 (bias grows with refinement, no derived band). Geometry shipped (M4perfect.geo 162 planes, 6 s.f.); the 2-D parent field of the M4 cases is NOT shipped. |
| F-3 M3.5Perf 2-D fixture | IDL-CONDITIONAL only, class ≥7.5e-3 for integrals (was "~1e-3, high") | NB | CRITIC G2: summary.out:506 mass defect 0.7537%, wall |ΔṀ| max 0.806%, eps 6.73651 vs A/A*(3.5)=6.78990 → implied CD 0.99214 vs printed 0.984756; REFUTE_repo item 4 (IDL corrupted) | Usable ONLY as "given the printed 101-point TT' line as IVL, march and compare" — i.e. experiment E-1 below. Do NOT use eps/CD from this case as tolerance source. |
| F-4 Rao exit condition (Rice eq.6 / code eq.14) + M4RAO/rao.dat | FIXTURE, band-less, same lineage as GENO | NB | P2_lemmaA:238-242 (L.15), M0:3113-3114, :3316-3319 (measured 6.6e-02/2.0e-02); CRITIC G6-a (GENO Rao 1958 lineage identical) | Already of record and measured; repo = second implementation of the SAME lineage, downstream of a corrupted IDL. |
| F-5 NR-license / clean-room constraint | UPHELD | — | digest_repo §5; REFUTE_repo S4 (NR by idiom, no notice) + undeclared third-party Chart*.cpp | Never port; shipped outputs only; nothing buildable anyway (CRITIC G1: zero project files for MOC_Grid_BDE/3D_MOC; STT2001.dsw → missing .dsp). |

### Witnesses / citations (paper-side)
| Row | v2 weight | TWIN class | Anchors | Content |
|---|---|---|---|---|
| W-1 Rao-only discontinuous exit-pressure profile (Rice §5.2) vs DE-side bucket | LOW-MEDIUM, ADJUDICATE (cheap) | NB | D6:154-155 (MARGIN-BUCKET SCOPE BOUNDARY, DE-side bucket, panel 4/4); REFUTE_adjudication M-5 | Possible third-party witness of the same mechanism; undecided. |
| W-2 SUPIN NURBS-refit breaks shock cancellation (pp.157, 267) | LOW witness | PO | choice_ledger:164-174 (C1: MoC solved ON the spline wall, never refit) | Cautionary datum for the paper; no open ledger row. |
| W-3 Repo = NASA GRC PDE-sponsored irrotational MoC tooling (2001-03) | LOW citation | PO | literature_registry:1281 (Fievisohn = closer cousin); R5 novelty bound | Strengthens the novelty bound in P-1 landscape. |
| W-4 "Set End Point exists only between Rao and perfect lengths" (Rice) | KEEP OUT | — | REFUTE_adjudication M-6 | Practitioner observation, no proof/shock criterion — never cite vs Sternin boundary (D6:1024-1033). |

### Downgraded to LOW / HORIZON / DROP (with the record anchor that closes them)
- 3D_MOC as "the" B-lite analogue → MEDIUM only as class member: B-lite is a formulation-agnostic hyperbolic x-as-time space-march with fitted sheet + Lemma-B adjoint (M0:3033-3037; G12_S1:30-50), NOT a committed 3-D MoC; docs/ zero hits "bicharacteristic"/"reference-plane". Armstrong ≠ Ransom/Hoffman/Thompson → D6:1023 stays OPEN (check Zucrow-Hoffman Vol. 2 on disk, registry:469-470, before procuring). Armstrong acquisition = optional F6 horizon.
- IVS-from-axisymmetric-solution caution → LOW: B-lite marches FROM interface data on Γ_d in normal form m_n (M0:3028-3032, L4-CERT); no such step to price. Residual: 2-D and 3-D demonstrator legs must ingest the SAME interface data (test-design remark).
- Uniform-field-preservation rejector → LOW one-line F6 test seed (scattered-stencil-specific).
- Reflected-wave validity bound after trimming → LOW/horizon: principle of record (Lemma B :91, M0:544-545, R-6 kickoff:472-485); practice (stream-surface lofting) absent from the plan (zero hits "loft/trimm/stream-surface").
- SUPIN choked outflow-nozzle CFD device → LOW/horizon: solves an inlet problem; every plan CFD has supersonic outflow or U3 extraction surface already axially supersonic (D6:263-267).
- NPAC C_FG/C_d/C_V bookkeeping → LOW nomenclature crosswalk: cycle-averaged conventions are theorems with detector ([T-T3-SI] M0:833-859, :887-893); ideal denominator = bound ladder (D6:1150-1153).
- NPAC friction/heat-transfer layer → DROP or MINT: plan has ZERO viscous duty (CRITIC G5-b; MASTER :737 "viscous channel is NG-5"); only hook = F2b DUTY-4(i) δ* band (D6:413-414) where NPAC's second pass could serve as δ*-estimator comparator. DECISION PENDING (user): mint a loss-accounting row (owner F5, empirical comparator class) or drop.
- NPAC mass-addition contract → HORIZON/DROP: interface fluxes already exact in normal form (L4-CERT (i)); no lateral mass addition in scope (scope pins).
- Berton two-angle λ → LOW: F3 oracle is exact MoC (Rao 1961 spike, D6:218/832); λ cannot reject (R5). Acquisition optional.
- DTHETAB / R_down heuristics → CITATION-ONLY (C9 census note: practitioner class, not adjudicable).
- SUPIN productization pattern → LOW A7 horizon: 3/6 items conflict with "nothing leaves the tool outside a Verdict" (D6:678-681); 2/6 already practice; only input write-back survives as a nicety.
- SUPIN App. B MoC cross-check → DROP: GENO + Zucrow-Hoffman already serve; software US-persons-only (no executable twin).
- SUPIN Taylor-Maccoll vs ANNEX B case B → IRRELEVANT: "Taylor fan" = Taylor-Zel'dovich unsteady rarefaction, not Taylor-Maccoll (REFUTE_adjudication M-4; CRITIC G5-a). Side finding: "Taylor fan" is UNGLOSSED in the record (zero hits "Zel'dovich") — a one-line gloss in D6:1143/glossary closes an ambiguity. SUPIN's closed-form θ-β-M + shock-point unit process (B-18) = citable prior art for the oblique-shock-chain leg; SUPIN's rotationality drop behind curved shocks = named ANTI-PATTERN for the case-B generator (s(y;ξ) is the payload).
- Item 13 experimental anchor (RK-E) → NONE of the sources helps (TP 3576 = steady O2/H2 rocket test, not RDE). Declared explicitly. TP 3576 could be a SEPARATE steady-limit experimental thrust anchor for case A (collapse theorem makes steady test data relevant) — not proposed before; LOW-MEDIUM, user decision.
- Inlet-side system context → HORIZON by scope pin.

## 2. Zero-cost twin experiments (CRITIC G6-b/c; not yet run — NB, ~1 h each on s3)
E-1. GENO `ivl_file` (IO_m.f90:254-256, read_ivl_from_file :620-776) ingests the shipped `TT'.out` (101 pts, x/R*, R/R*, M, θ + p0/T0/γ from summary.out) → GENO ideal bell to Me=3.5 → compare contour with wall.out/rao.dat and eps 6.73651 / L 12.5363. Separates start-line error from march error; prices F-3 honestly; exercises the host C12 displaced-IVL machinery on a foreign line. CAVEAT: GENO working tree carries a NON-inert instrumentation patch (memory s-genoaudit-parallel-incomplete) — run from HEAD or after revert.
E-2. GENO nozzle_type 3 (conical) + uniform M=1.1 IVL at r∈[0,1] + 10° wall = exact 2-D twin of 3D_MOC cone10 (exit z=12.93: mean M 4.036, 3σ 0.072 measured from shipped data) → quantified axisymmetric error of the reference-plane scheme = F6 "beat this" bar from data on disk.

## 3. Refuter-found defects in the digests (corrections of record)
- digest_NPAC: injected-stream energy term is c_p·T_a (STATIC) + ½V_a² (Eq. 43 p. 19), not c_p T_Ta; "Eq.11≡12≡57 exact" wrong (λ correction); App. III p0=1e-4 psf (strongly under-expanded), not 0; fully-coupled pass itself iterated to M8=1; Fig.1/4/5 geometry ≠ App. II geometry.
- digest_Rice: 1/(R_up+1) sentence is self-contradictory in the source; Fig. 22 value mapping inferred; per-axis print controls ARE functional (pp. 34-35); report typos eq. 15/29 (ψ coefficient) and eq. 38 (n₁→n₂) unflagged; "STT internals in Refs 1-2" is inference.
- digest_repo: default 3-D surface fit = global "All Point Spline" (3D_MOCDlg.cpp:86), not 8-neighbour TPS; "~1e-3 oracle" REFUTED (see F-3); B11 not a bug (failCounter caps insertions); 4 new defects ((y+6) for (G+6) :3148, missing *y :3158, silent-continue 3D_MOCGrid.cpp:152-157, clamp artefact); 1181/1881 comparison anchor wrong (conclusion right); B8 empirically confirmed in M3.5Perf_AvsX.out (stations jump 4.18→8.61, 27 duplicates).
- digest_SUPIN: pending REFUTE_SUPIN.

## 4. Process duties before any landing (R7)
- The three NTRS PDFs + digests have NO literature_registry / ADVISORY_INDEX rows (CRITIC G4/G7-d) → rows required if promoted to validation/.
- All rows here: NON-BLOCKING or PAPER-ONLY for TWIN; expected BLOCKING count contributed = 0.
- Precision floor of all shipped fixtures = 6 significant digits (~5e-6 rel) — must appear in any fixture contract.

## 5. Proposed landing (user decision; nothing executed)
(a) D6 item 12: + Kliegel & Levine AIAA J 7(7) 1969 PRIORITY 2 (C12 band-term source); + Armstrong AEDC-TR-78-68 OPTIONAL (F6 horizon); note D6:1023 still open (check Zucrow-Hoffman Vol. 2 first).
(b) M0 [S-BLITE] one line: G12-L1-3D cross-check source = Rice/Armstrong conoid algebra (with the eq. 15/29 typo caveat).
(c) D6:1143 / glossary: gloss "Taylor fan" = Taylor-Zel'dovich.
(d) DECISIONS: mint-or-drop viscous loss-accounting row (F5, δ*-band hook); TP 3576 as steady-limit anchor yes/no; run E-1/E-2 (2 h total) yes/no.
(e) Advisory in validation/ promoting digests + this v2 with registry rows, OR keep as consultation material with the memory pointer only.
