# INVENTORY — SEGMENT 5 "session logs + validation artifacts" (S-ORDINE Phase 1, reader seg5-logs-artifacts, 2026-08-13)

Authoritative list: `validation/sordine_raws_2026-08-13/seg5_sessionlogs_artifacts.txt` — 165 files, ALL accounted below.
Coverage discipline: of-record prose read at structure/header level (session logs per brief: headers + classification, steps NOT re-read integrally); .py classified from docstrings (full docstring read, not code review); .pyc / .log / .json classified-without-integral-read with declared reasons (compiled cache / derived run evidence whose record lives in session md / machine artifact consumed by a named gate). No unread file is summarized beyond its declared class.

Verdicts S14-S25bis are of record and are NOT re-litigated here.

---

## A. SESSION LOGS (27 files, class = session-log)

Common facts: append-only total-order logs mandated by CLAUDE.md R3; each is the LOG OF RECORD of its session (its steps/verdicts live ONLY here + commit messages — docs/rde_nozzle_PROGRESS.md carries only the ORA/NEXT/BLOCCATO/LOG summary). ALL 27 ARE UNTRACKED (single-copy, zero git history — the durability risk named in the S-ORDINE prompt §2(b), decision pending). STATUS-AUTHORITY: OF-RECORD for every row. UNIQUE-AT-RISK: yes for every row (the full step ledger with evidence/hashes/verdicts). Question for Phase 2 = index/archive/tracking status, not absorption. Indexed by `validation/INDEX.md`.

| PATH | ROLE (session) | PLAN-ANCHOR |
|---|---|---|
| validation/PROGRESS_2026-07-16_S4_G5venue.md | S4: G5 dispatch + P-2 venue decision of record (AIAA J primary, fallback triggers) | F0/G5 (A0.5) + F1/P-2 venue; R3 |
| validation/PROGRESS_2026-07-16_fase0_OP0.md | Fase-0 closure + OP-0 eps-ladder session | F0/A0.3, OP-0; R3 |
| validation/PROGRESS_2026-07-16_fase1_OP11.md | S3: OP-11-eps phase diagram + P-2 outline + G5 commissioning | F1/OP-11-eps, F1/P-2, F0/G5; R3 |
| validation/PROGRESS_2026-07-16_fase1_P1.md | S5: P-1 skeleton + P-2 Lemma A + G0 spike (renumbered S4->S5, concurrency declared) | F1/P-1, F1/P-2, F2-prep/G0; R3 |
| validation/PROGRESS_2026-07-16_fase1_S7.md | S7: Lemma B + P-A1 + OP-0-gamma + G5-2a TOC sweep | F1/P-2, F1/OP-0-gamma, F0/G5-2a; R3 |
| validation/PROGRESS_2026-07-16_fase1_S8.md | S8: P-1 §2/§4 + G0 spike axisym extension + OP-0-gamma tail | F1/P-1, F2-prep/G0; R3 |
| validation/PROGRESS_2026-07-16_rigore_G12.md | Rigor S8: G12-S1 fitted-shock x-as-time attack | F1/G12-S1; R3 |
| validation/PROGRESS_2026-07-16_rigore_PA.md | Rigor S6: P-A1/P-A2/P3 discharge | F1/P-2 (P-A1/P-A2), F1/P3; R3 |
| validation/PROGRESS_2026-07-17_S9_ordine.md | S9: SCAFFOLD migration M-1..M-5, claims_registry.yaml born (80 entries) | F1/SCAFFOLD-M, PIANO/D6; R3 |
| validation/PROGRESS_2026-07-17_fase2_S10.md | S10: G0 formal decision + GENO cross-code criterion + P-1 §5-§7 | F2/G0, F1/P-1; R3 |
| validation/PROGRESS_2026-07-20_fase2_S11.md | S11: A1 brick 1 (profile-generation machinery [X-A1IM]) | F2/A1 brick 1; R3 |
| validation/PROGRESS_2026-07-21_S12_rigoreR4.md | S12: R4 back-prop of the review conversation (T3-QS, D-GSEP, S-BLITE, GV row, plan M1-M7) | R4 rule itself; F4-prep/T3QS, F2-prep/A5, PIANO/D6 |
| validation/PROGRESS_2026-07-21_S13_leads.md | S13: literature page-verify; Kraiko-Osipov 1970 read in full, D4 contingency adjudicated (containment) | F0-coda/D2 leads, G6/G14, D4 §3; R3 |
| validation/PROGRESS_2026-07-22_S14_panel.md | S14: reading-queue completion + 16-persona convergent panel (D8 of record) | PIANO/panel (D7-class); memory s14-panel-verdict; R3 |
| validation/PROGRESS_2026-08-04_S15_fondazioni.md | S15: deep-foundations tranche 1 (T-SLRW/T-XWALL/T-XWS/U1/U2/X-IVXC, ledger p1, dossier) | RIGOR/A campaign (s15-foundations-campaign); R3 |
| validation/PROGRESS_2026-08-06_S16_fondazioni2.md | S16: foundations tranche 2 (U3+U4, S-ACFR, S-GBE, S-LBML, ledger p2) | RIGOR/A-B; C-D25U, C-MAJDA/U3-H1; R3 |
| validation/PROGRESS_2026-08-06_S17_brick2.md | S17: brick-2 re-adjudication + kickoff ([X-TOCV], DIR-RKG, X-SCANM, X-LSG0, X-THC1) | F2/A1 brick 2 (D6 item 9); R3 |
| validation/PROGRESS_2026-08-06_S18_brick2run.md | S18: production levers P1-P4 + end-to-end run — BRICK 2 CLOSED, O3.3 unlocked | F2/A1 brick 2 closure, T2a gate; R3 |
| validation/PROGRESS_2026-08-06_S19_o33.md | S19: campaign O3.2/O3.3 (P-2 numeric half; bench PASS, C-O33 quantified) | F1/P-2 oracles O3.2/O3.3; [C-O33]; R3 |
| validation/PROGRESS_2026-08-07_S20_adaptive.md | S20: adaptive knot class [X-AKNO], certifiability-boundary crawl, tier-ladder formalization | F1/P-2 + F2/A1 ([C-O33] discharge attempt); R3 |
| validation/PROGRESS_2026-08-11_S21_order.md | S21: F0 order+instrumentation of plan v3 (ratification, P0 rejectors, [X-CDKAT], [X-VMON] armed) | F0 of plan v3; R3 |
| validation/PROGRESS_2026-08-11_S22_governor.md | S22: F1 governor [X-MGOV] + [X-LOCD] retro-diagnosis + decisive campaign A' + O4 discharge | F1 of plan v3; R3 |
| validation/PROGRESS_2026-08-11_S23_f1close.md | S23: F1 early-close decision, P-2 dated freeze, [X-TBAK] DUTY-6(i), C1 conditional | F1 close; R3 |
| validation/PROGRESS_2026-08-11_Sgauntlet.md | S-GAUNTLET: parallel adversarial generality-ledger session (advisory-pattern, path-limited) | Standing directive claim-dual-proof; ADVISORY_Sgauntlet_prompt; R3 |
| validation/PROGRESS_2026-08-12_S24_f1b.md | S24: F1b DEF twin falsifier [X-DEFTW] executed, EQ-v2 adjudication, DE-bucket | F1b of plan v3; R3 |
| validation/PROGRESS_2026-08-12_S25_speed.md | S25: C4-first + engine speed M-CHAIN (M0-M5ab), [X-SPDB] | Census R30-prep / S-SPEED dispatch; F-SERVICE; R3 |
| validation/PROGRESS_2026-08-12_S25bis_speed.md | S25-bis: M5c/M6/H3/H4 + GAP-29 + notaknot twin + findings registry; STEP 15 = convergence map (named input of THIS S-ORDINE) | Census R30/R31; F-SERVICE; R3 |

## B. VALIDATION INDEX + PRE-PROGRAM V&V DOCS (21 other .md)

The 2026-07-08..10 block (rows marked LECTURE-ERA) predates the nozzle program: it is the V&V corpus of the RDE *lecture-code tool itself*, anchored to the standing `repo-sota-standard` memory (SOTA academic+industrial tool bar) and to the top-level README badges — NOT to D6 phases. That is a nameable need (tool credibility layer under which the program runs, G1 "no science from an uncertified machine" inherits from it), so NOT orphan; but Phase 2 should give this layer an explicit typed archive banner separating it from the program docs.

| PATH | CLASS | ROLE | STATUS | PLAN-ANCHOR | UNIQUE-AT-RISK | REFS |
|---|---|---|---|---|---|---|
| validation/INDEX.md | doc-index | one-line index of all session logs (audit trail, "never normative") | OF-RECORD (living) | R3 audit trail; S-ORDINE R32 direct input | the concurrency/renumbering reconciliation map of 2026-07-16 | inbound: R3 practice; outbound: every PROGRESS_* log |
| validation/README.md | doc-index | frozen-reports contract for lecture-era validation (regenerate into data/, never overwrite here) | OF-RECORD (LECTURE-ERA) | repo-sota-standard; top-level README badges | the freeze rule + report->regenerator mapping table | top-level README |
| validation/VALIDATION.md | doc-validation | lecture-era 3-pillar validation report (33 CJ checks vs Caltech DB/CEA) | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | pillar-1/2/3 numeric verdicts | validate.py, data/ |
| validation/REPO_VV.md | doc-validation | adversarial V&V of repo as teaching/design tool (2026-07-10, verdict PROMOSSA) | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | student-viewpoint findings + verdict | commit 863c836/9b10e58 |
| validation/SOTA_AUDIT.md | doc-audit | two adversarial multi-agent audits: 490 claims/518 verdicts + 8 design exercises | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | per-claim literature-fidelity verdicts | tests/run_all.py; source modules |
| validation/cycles_validation.md | doc-validation | W-S cycles V&V, 99/99 PASS | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | 99-check table | scripts/cycles_ws.py, data/cycles_ws.json |
| validation/vv_thrust.md | doc-validation | analytical thrust models V&V (PH/axial/Stechmann, 16 cases) | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | cross-check verdicts | scripts/thrust_models.py |
| validation/gamma_audit.md | doc-audit | gamma frozen-vs-equilibrium audit of SK/Stechmann thrust models | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | the "frozen never appears in the papers" grep finding + gamma_e adjudication | tmp_sk/tmp_st fulltexts, specs/ |
| validation/gamma_phase_audit.md | doc-audit | per-phase gamma audit of W-S cycles (2nd round, complements gamma_audit) | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | per-phase gamma verdicts | specs/thermo_spec.md, cycles_ws.py |
| validation/dof_audit.md | doc-audit | DOF/input provenance audit ("no magic parameter hides") | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard (ancestor of R5 numeric discipline) | per-input provenance classification | all model scripts |
| validation/interface_audit.md | doc-audit | pre-refactor AS-IS interface/convention snapshot (git a986717) | CONSUMED (refactor executed; kept as frozen snapshot) | repo-sota-standard | file:line AS-IS map at a986717 | src/common/ |
| validation/q_formal.md | doc-theory | formal definition/verification of q (standard-state anchored) | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | q° vs calorimetric relation + numbers | scripts/q_formal.py, data/q_mapping.md |
| validation/sdt_official_audit.md | doc-audit | official Caltech SDToolbox zip vs vendored stack audit | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | official-vs-vendored diff verdicts | sdtoolbox/, ShockDetonation.pdf |
| validation/sdt_thrust_demos.md | doc-audit | SDT official impulse demos vs course thrust models census | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | "no official RDE thrust model" finding | sdt_official_audit.md |
| validation/st_opt_validation.md | doc-validation | Stechmann Table-1 nozzle-optimization validation | OF-RECORD (LECTURE-ERA, frozen) | repo-sota-standard | sweep+golden-section reproduction numbers | scripts/st_nozzle_opt.py |
| validation/bell_optimality_proof.md | doc-theory | formal optimality theorems for area-ratio in Stechmann model | OF-RECORD (LECTURE-ERA; ancestor of program's bell claims) | repo-sota-standard; cited context for M0 "bell≈0 in-hypothesis" correction | proofs + executable-verification pointer | tests/test_bell_optimality.py |
| validation/G5_dispatch_email.md | doc-plan (dispatch) | ready-to-send Italian ILL email for Kraiko 1979 + PMM DD | OF-RECORD (awaiting user send — BLOCCATO-side) | F0/G5 (A0.5) | the exact dispatch text + recipient verification | G5_kraiko_pmm_commission.md §6 |
| validation/G5_kraiko_pmm_commission.md | doc-plan (commission) | G5 human library-pass commissioning text of record (+§6 dispatch scoping) | OF-RECORD | F0/G5; D4 §3; D6 gate G5 | commission checklist mapped to G6/G14 kill paths | D2 §b2/§G6/§G14, S4 log |
| validation/G5_pmm_toc_sweep_1957-1990.md | doc-record | G5 Item 2a digital PMM TOC sweep -> Item 2b reading list | CONSUMED (Item 2a discharged; reading list feeds Item 2b, still open human task) | F0/G5-2a | the query-bounded TOC hit list 1957-1990 | commission §3; S7 log |
| validation/s25bis_refute_diff.md | raw-agent-output | S25-bis dedicated adversarial refutation of commits 1806ae2/18b4e0f | RAW (verdicts absorbed in S25bis log + commit of record) | R30; claim-dual-proof directive; pipeline-sense R29 | refuter's per-claim attack detail beyond the absorbed verdicts | S25bis log; commits 1806ae2, 18b4e0f |
| validation/s25bis_sense_perimeter.md | raw-agent-output | S25-bis perimeter sense-review (R29 expert adjudication of each choice) | RAW (verdicts absorbed in S25bis log/registry) | Standing directive pipeline-sense-expert-review (R29); choice-adjudication-convergence | per-choice SOTA-alternative argumentation detail | S25bis log; choice ledger |

## C. SOTA GAPMAP RAWS (17 files, dir sota_gapmap_raws_2026-08-12/, class = raw-agent-output)

All 17: RAW backing files of the judged advisories `ADVISORY_S24_sota_gapmap_2026-08-12.md` (finder/verifier pairs, 6 facets) and the S25 pipeline-sense/red-team layer. STATUS: RAW — the judged/absorbed verdicts live in the advisories (segment of another reader); the UNIQUE-AT-RISK content is the line-level finder evidence and adversarial reasoning NOT copied upward (legitimate raw layer, keep archived, never normative). PLAN-ANCHOR: census R26 (gap-map) / R29 (pipeline-sense reviews) / GAP-<n> rows of docs/findings_registry.yaml. Classified from headers (raw layer; record content lives in the advisories).

| PATH | ROLE |
|---|---|
| validation/sota_gapmap_raws_2026-08-12/s24_gap_cell-cert.md | Finder position, facet 2 (cell solver + certification) |
| validation/sota_gapmap_raws_2026-08-12/s24_gap_constraints.md | Finder position, facet 5 (constraint machinery) |
| validation/sota_gapmap_raws_2026-08-12/s24_gap_driver-nonsmooth.md | Finder position, facet 4 (TR-SQP driver at nonsmooth frontier) |
| validation/sota_gapmap_raws_2026-08-12/s24_gap_mesh-amr.md | Finder position, facet 1 (mesh/error control, DWR/AMR) |
| validation/sota_gapmap_raws_2026-08-12/s24_gap_parametrization.md | Finder position, facet 3 (design parametrization vs SOTA) |
| validation/sota_gapmap_raws_2026-08-12/s24_gap_thermo-bands.md | Finder position, facet 6 (thermo closure + tolerance culture) |
| validation/sota_gapmap_raws_2026-08-12/s24_gapv_cell-cert.md | Adversarial verifier, facet 2 |
| validation/sota_gapmap_raws_2026-08-12/s24_gapv_constraints.md | Adversarial verifier, facet 5 |
| validation/sota_gapmap_raws_2026-08-12/s24_gapv_driver-nonsmooth.md | Adversarial verifier, facet 4 (supersedes its own interrupted draft at same path — declared in-file) |
| validation/sota_gapmap_raws_2026-08-12/s24_gapv_mesh-amr.md | Adversarial verifier, facet 1 (probes re-run bit-for-bit) |
| validation/sota_gapmap_raws_2026-08-12/s24_gapv_parametrization.md | Adversarial verifier, facet 3 |
| validation/sota_gapmap_raws_2026-08-12/s24_gapv_thermo-bands.md | Adversarial verifier, facet 6 |
| validation/sota_gapmap_raws_2026-08-12/s25_redteam_gapmap_judge.md | Form-3 red-team of the gap-map JUDGE layer (verdict ABSORB-WITH-REPAIRS; repairs applied [S25-REPAIR]) |
| validation/sota_gapmap_raws_2026-08-12/s25_refute_m12.md | Refuter of S25 M1+M2 memo/counter claims |
| validation/sota_gapmap_raws_2026-08-12/s25_refute_m4.md | Refuter of S25 M4 plan-as-args engine |
| validation/sota_gapmap_raws_2026-08-12/s25_refute_pipeline_impl.md | Form-2 refuter of the impl-fidelity review advisory |
| validation/sota_gapmap_raws_2026-08-12/s25_refute_pipeline_math.md | Form-2 refuter of the math-structure review advisory |

## D. PYTHON CARRIERS / PROBES (33 .py)

Classification from docstrings (all 33 docstrings read). CARRIER-OF-RECORD = anchored by docs/claims_registry.yaml (registry ID in docstring) and/or docs/findings_registry.yaml — MOVING THESE FILES BREAKS ANCHORS (registry doc/carrier paths + advisory citations). STATUS OF-RECORD unless noted. UNIQUE-AT-RISK for carriers = the executable proof itself (verdict numbers live in logs/registry; code path is the anchor target).

| PATH | CLASS | REGISTRY ID / ROLE | PLAN-ANCHOR | ANCHOR-TARGET? |
|---|---|---|---|---|
| validation/a1_ideal_march_jax.py | carrier-py | [X-A1IM] A1 brick-1 differentiable MoC march (ideal nozzle twin of GENO type 0) | F2/A1 brick 1 (S11) | YES |
| validation/a1_loopspeed_bench.py | carrier-py | [X-LSG0] derived loop-speed threshold, clean-host protocol (T2a production gate) | F2/A1 kickoff duty (a); DIR-G0 falsifier | YES |
| validation/a1_march_scan.py | carrier-py | [X-SCANM] scan-column replay engine | F2/A1 kickoff duty (b) | YES |
| validation/a1_toc_variational_jax.py | carrier-py | [X-TOCV] variational TOC engine, TR-SQP driver run_trsqp — THE engine of record | F2/A1 brick 2 (S17-S18); gap-map facets cite it by line | YES (heavily) |
| validation/acontraction_front_probe.py | probe-py (declared "NOT a certificate") | [X-ACFR] a-contraction front sampling probe | RIGOR/A S16 T2; C-MAJDA/U3-H1 | YES |
| validation/adaptive_knot_optimize.py | carrier-py | [X-AKNO] adaptive error-indicator knot construction | F1/P-2 + F2/A1 (S20, [C-O33] residual) | YES |
| validation/certdiag_kat.py | carrier-py | [X-CDKAT] certdiag known-answer test + S20 retro-validation | F0 P0 audit seed A1 (S21) | YES |
| validation/def_twin_falsifier.py | carrier-py | [X-DEFTW] F1b DEF twin falsifier (branches F1-F7, verbatim pre-registration) | F1b (S24); def-equivalence panel | YES |
| validation/engine_speed_bench.py | carrier-py | [X-SPDB] engine speed bench, M0..M-E checkpoints + gates | S25/S25bis speed program (R30); S-SPEED dispatch | YES |
| validation/g0_geno_crosscode.py | carrier-py | [X-GENOXC] G0 cross-code flowfield oracle (O3.4) vs GENO tocnoz | F2/G0 (S10) | YES |
| validation/g0_spike_axisym_shock.py | carrier-py | [X-G0AX] axisym source + fitted shock point spike | F2-prep/G0 (S8); T-LEMB carrier list | YES |
| validation/g0_spike_jax_moc.py | carrier-py | [X-G0] first differentiable MoC unit-process spike (52/52 record stands) | F2-prep/G0 (S5); gate G0 decision | YES |
| validation/g12_shock_linearization.py | carrier-py | G12-S1 attack carrier (symbolic + numeric bricks) | F1/G12-S1 (rigor S8) | YES |
| validation/gbe_ergodic_envelope.py | carrier-py | [X-GBE] ergodic G-B envelope bricks | RIGOR/A S16 T4; [S-GBE] | YES |
| validation/ivxc_interval_certificate.py | carrier-py | [X-IVXC] interval convexity certificate over margin box (global-max dossier Card 1) | RIGOR/A+C S15; C-XBVP(a) | YES |
| validation/locus_diagnosis.py | carrier-py | [X-LOCD] S20 three-way locus retro-diagnosis | F1 entry row (S22); O4 | YES |
| validation/margin_governor.py | carrier-py | [X-MGOV] margin governor: KS aggregation, G1 surrogate, decisive-campaign driver | F1 (S22); REQ-NONSTALL/G1 | YES |
| validation/margin_tolerance_backoff.py | carrier-py | [X-TBAK] tolerance-ball margin backoff (gauntlet C028, DUTY-6(i)) | F1 close (S23); S-GAUNTLET duty package | YES |
| validation/n6_fivefield_adjoint.py | carrier-py | five-field swirl adjoint structure, EOS-general | F1/N6-5F (rigor S8) | YES |
| validation/n6_swirl_kernel.py | carrier-py | N6 swirl structure lemmas | F1/N6-S1 | YES |
| validation/o32_mesh_convergence.py | carrier-py | [X-O32] O3.2 mesh convergence of primal/adjoint pair | F1/P-2 (S19); S-LBML clause LB-c1 | YES |
| validation/o33_bench.py | carrier-py | [X-O33B] O3.3 pre-registered term-match bench (primary kill criterion of Lemma A i/iii) | F1/P-2 (S19); [C-O33] | YES |
| validation/p2_pA1_symbolic_adjoint.py | carrier-py | [X-P2A1] dual-route verification of Prop. A2 (conservative variables) | F1/P-2 (S7) | YES |
| validation/pa1_symbolic_lemmaA.py | carrier-py | P-A1 symbolic Lemma-A verification + kernel solvability lemma | F1/P-2 (rigor S6) | YES |
| validation/s25bis_gap29_sweep.py | probe-py (one-shot sweep, of record) | GAP-29/AUDIT:426 halved-constants sensitivity sweep (found the NTF flip) | findings_registry GAP-29; choice ledger C17/C18; S25bis | YES (findings registry) |
| validation/s25bis_notaknot_twin.py | probe-py (one-shot twin, of record) | GAP-5 notaknot BC twin (-82% corner mismatch; BC bias datum) | findings_registry GAP-5; choice ledger C2; S25bis | YES (findings registry) |
| validation/side_load_rotating_lemma.py | carrier-py | [X-SLRW] rotating side-load lemma carrier [T-SLRW] | RIGOR/A S15 | YES |
| validation/t3qs_sweep_protection.py | carrier-py | [X-T3QS] quasi-steady protection of the collapse class (suite group xvi) | F4-prep/T3QS (S12 R4) | YES |
| validation/thermotab_c1_jax.py | carrier-py | [X-THC1] C^1 tabulated thermo closure + EOS GNL audit | F2/A1 kickoff duty (d); thermo-tabulated-backend directive | YES |
| validation/u2_reflection_glancing.py | carrier-py | [X-U2RG] slip-wall reflection brick [T-U2RG] (U2) | RIGOR/A S15; C-D25U | YES |
| validation/u3_bordered_front_solve.py | carrier-py | [X-U3BD] U3 bordered front-solve structure | RIGOR/A S16; [S-D25U-U34]/U3-H1 | YES |
| validation/validity_monitor.py | carrier-py | [X-VMON] (G)/Lambda-form validity monitor + gamma=1.4 KAT vs Rao-Beck Eq.(4) | F0 exit gate (S21); Eq.(4)/Sternin monitor | YES |
| validation/xbvp_entropy_transfer.py | carrier-py | [X-XBVP] Cauchy->steady-BVP transfer bricks | RIGOR/A S15; shock-free canonicity | YES |

## E. JSON MACHINE ARTIFACTS (25 .json) — classified-without-integral-read (machine artifacts; each consumed by the named gate/test)

| PATH | CONSUMER / ROLE | STATUS | PLAN-ANCHOR |
|---|---|---|---|
| validation/numeric_allowlist.json | tests/test_numeric_lint.py — allowlisted literals | OF-RECORD (living config) | R5 numeric discipline; R28 |
| validation/numeric_lint_baseline_validation.json | tests/test_numeric_lint.py ratchet tier — frozen per-file literal-debt baseline (33 files / 622 literals) | OF-RECORD (ratchet baseline; baseline==reality invariant) | R28; commit 18b4e0f |
| validation/s20_adaptive_design.json | [X-AKNO]/S20 adaptive-design artifact (consumed by S20/S22 analyses, [X-LOCD]) | OF-RECORD artifact | S20 [C-O33] |
| validation/s22_certlim_base.json | S22 campaign A' cert-limited base design record | OF-RECORD artifact | F1 (S22) |
| validation/s22_rejected_designs.json | A1_REJ_SAVE rejected-design persistence (O4 instrumentation) | OF-RECORD artifact | F1/O4 (S21 armed, S22 consumed) |
| validation/s24_deftw_derive.json | [X-DEFTW] derive-mode artifact (H4 re-derive reproduces it, f2 vs bar numbers) | OF-RECORD artifact (H4 gate consumer) | F1b (S24); H4 |
| validation/s24_deftw_f3f7.json | [X-DEFTW] F3/F7 branch records (pre-registered refs of the H4 derive artifact) | OF-RECORD artifact | F1b; H4 |
| validation/s24_deftw_leg1.json | [X-DEFTW] leg-1 (GENO flagdef) record | OF-RECORD artifact | F1b |
| validation/s25_spdb_h3.json | [X-SPDB] h3gate memo | OF-RECORD gate memo | R30; H3 |
| validation/s25_spdb_m0.json | [X-SPDB] M0 clean-host re-baseline | OF-RECORD gate memo | R30 |
| validation/s25_spdb_m12.json | [X-SPDB] m12gate (M1+M2 memos/counters) | OF-RECORD gate memo | R30 |
| validation/s25_spdb_m4.json | [X-SPDB] m4gate (plan-as-args engine) | OF-RECORD gate memo | R30 |
| validation/s25_spdb_m5.json | [X-SPDB] m5gate (M5ab) | OF-RECORD gate memo | R30 |
| validation/s25_spdb_m5c.json | [X-SPDB] m5cgate (per-column compiled executor) | OF-RECORD gate memo | R30; M5c |
| validation/s25_spdb_m6.json | [X-SPDB] m6gate — the M6 REJECTION verdict of record | OF-RECORD gate memo (rejection is the verdict) | R30; M6 adoption row (F2) |
| validation/s25_spdb_mbwalk.json | [X-SPDB] M-B walk checkpoint | OF-RECORD gate memo | R30 |
| validation/s25_spdb_mc.json | [X-SPDB] M-C checkpoint | OF-RECORD gate memo | R30 |
| validation/s25_spdb_md.json | [X-SPDB] M-D segment stop-check (14.9 s vs <=30) | OF-RECORD gate memo | R30 speed counter of record |
| validation/s25_spdb_me.json | [X-SPDB] M-E stop-check (20.1 s pessimistic) | OF-RECORD gate memo | R30 |
| validation/s25bis_gap29_base.json | GAP-29 sweep arm: base constants | OF-RECORD artifact (sweep input to registry GAP-29 row) | GAP-29 |
| validation/s25bis_gap29_cfloor4.json | GAP-29 arm: C_FLOOR/2 | OF-RECORD artifact | GAP-29 |
| validation/s25bis_gap29_cops50.json | GAP-29 arm: C_OPS/2 | OF-RECORD artifact | GAP-29 |
| validation/s25bis_gap29_ntf50.json | GAP-29 arm: NEWTON_TOL_FACTOR/2 — the FLIP arm (NTF load-bearing) | OF-RECORD artifact (the flip datum) | GAP-29 -> NTF derivation duty (F2, registry) |
| validation/s25bis_gap29_sweep.json | GAP-29 consolidated sweep result | OF-RECORD artifact | GAP-29 |
| validation/s25bis_notaknot_twin.json | GAP-5 notaknot twin result (-82% corner mismatch, cd shift 8.2%) | OF-RECORD artifact | GAP-5 adjudication (F2, registry) |

## F. RUN LOGS (24 .log) — classified-without-integral-read (derived run evidence; record content lives in PROGRESS_2026-08-12_S25bis_speed.md and the gate memos of section E)

All: class run-log, STATUS DERIVED (re-runnable evidence; verdicts of record absorbed in S25bis session log + spdb/gap json memos), PLAN-ANCHOR = R30 (S25/S25bis speed program) or the named gate. UNIQUE-AT-RISK: none of record (raw stdout; timings/diagnostics duplicable), EXCEPT noted rows.

| PATH | EVIDENCE OF |
|---|---|
| validation/s25bis_closing_suite.log | closing FULL suite 20/20 PASS run 1 |
| validation/s25bis_closing_suite2.log | closing suite re-run (282 s SUITE_EXIT=0 of record) |
| validation/s25bis_derive_h4_run1.log | H4 tail-to-derive re-run (reproduces S24 tail exactly) |
| validation/s25bis_derive_restamp.log | H4 code-identity restamp run |
| validation/s25bis_gap29_run1.log | GAP-29 4-arm sweep execution |
| validation/s25bis_h3gate_final.log | h3gate final PASS |
| validation/s25bis_h3gate_postrepair.log | h3gate after repair |
| validation/s25bis_h3gate_run1.log | h3gate first run |
| validation/s25bis_m12gate_final.log | m12gate final (post default-flip re-chain) |
| validation/s25bis_m12gate_postrepair.log | m12gate post-repair |
| validation/s25bis_m12gate_rerun.log | m12gate rerun 1 |
| validation/s25bis_m12gate_rerun2.log | m12gate rerun 2 |
| validation/s25bis_m4gate_rerun.log | m4gate frozen-code re-chain |
| validation/s25bis_m5cgate_run1.log | m5cgate first-pass acceptance (defnoz-mild) |
| validation/s25bis_m5cgate_run2.log | m5cgate full acceptance |
| validation/s25bis_m5gate_rerun.log | m5gate re-chain |
| validation/s25bis_m6diag.log | M6 consumer diagnostic (batched adjoint 5.6e-8 divergence) — mechanism-isolation evidence; cited in the M6 convergence-map row |
| validation/s25bis_m6fix.log | M6 corrected-form (one-lowering) run — cross-lowering-floor finding evidence |
| validation/s25bis_m6gate_run1.log | m6gate REJECTION run of record |
| validation/s25bis_m6locus.log | M6 locus probe (eager-vs-jit 2.9e-2) — root-cause probe evidence |
| validation/s25bis_md_run1.log | M-D segment measurement |
| validation/s25bis_me_run1.log | M-E measurement |
| validation/s25bis_notaknot_run1.log | GAP-5 twin run 1 (incl. the refuted-then-reformed rejector event) |
| validation/s25bis_notaknot_run2.log | GAP-5 twin run 2 (delta-stability rejector) |

NOTE: the three M6 probe logs (m6diag/m6fix/m6locus) carry mechanism-isolation detail (the three convergent probes of the cross-lowering-gradient-floor finding) summarized but not fully transcribed in the session log — borderline at-risk; findings_registry row cross-lowering-gradient-floor is the absorbing anchor. Flag for Phase 2: confirm the registry row's evidence field points at these logs before any archive move.

## G. DERIVED CACHE (18 .pyc, validation/__pycache__/) — classified-without-read (compiled bytecode, fully regenerable)

All: class derived-cache, STATUS DERIVED, PLAN-ANCHOR n/a (build byproduct), UNIQUE-AT-RISK none, candidate for gitignore hygiene (garbage-candidate as tracked content, but R4-safe: regenerable by construction).

validation/__pycache__/a1_ideal_march_jax.cpython-313.pyc; validation/__pycache__/a1_loopspeed_bench.cpython-313.pyc; validation/__pycache__/a1_march_scan.cpython-313.pyc; validation/__pycache__/a1_toc_variational_jax.cpython-313.pyc; validation/__pycache__/adaptive_knot_optimize.cpython-313.pyc; validation/__pycache__/certdiag_kat.cpython-313.pyc; validation/__pycache__/def_twin_falsifier.cpython-313.pyc; validation/__pycache__/engine_speed_bench.cpython-313.pyc; validation/__pycache__/g0_spike_axisym_shock.cpython-313.pyc; validation/__pycache__/ivxc_interval_certificate.cpython-313.pyc; validation/__pycache__/locus_diagnosis.cpython-313.pyc; validation/__pycache__/margin_governor.cpython-313.pyc; validation/__pycache__/o32_mesh_convergence.cpython-313.pyc; validation/__pycache__/o33_bench.cpython-313.pyc; validation/__pycache__/s25bis_gap29_sweep.cpython-313.pyc; validation/__pycache__/s25bis_notaknot_twin.cpython-313.pyc; validation/__pycache__/thermotab_c1_jax.cpython-313.pyc; validation/__pycache__/validity_monitor.cpython-313.pyc — 18 files.

## H. ORPHAN FINDINGS

NONE in this segment: every file maps to a nameable plan need (D6 phase, census row, registry row, gate, or the pre-program repo-sota-standard V&V layer). Two near-orphan observations flagged, not orphans:
1. The LECTURE-ERA block (17 md) answers the tool-credibility need, not a D6 phase — Phase 2 should type it as a distinct archived layer with banner so the plan-lens navigation does not mix it with program artifacts.
2. validation/interface_audit.md is CONSUMED (its refactor happened); keep as frozen snapshot with supersession note.

## I. RECONCILIATION

27 session-log + 21 other-md (B: 21 rows) + 17 gapmap raws + 33 .py + 25 .json + 24 .log + 18 .pyc = 165. MATCHES the authoritative list.

## J. CODENAME TOKENS COLLECTED (token | where seen | meaning if evident)

X-A1IM | a1_ideal_march_jax.py | A1 brick-1 differentiable MoC march carrier
X-LSG0 | a1_loopspeed_bench.py | loop-speed threshold / T2a production gate
X-SCANM | a1_march_scan.py | scan-column replay engine
X-TOCV | a1_toc_variational_jax.py | variational TOC engine of record
X-ACFR | acontraction_front_probe.py | a-contraction front probe
X-AKNO | adaptive_knot_optimize.py | adaptive knot design class
X-CDKAT | certdiag_kat.py | certdiag known-answer test
X-DEFTW | def_twin_falsifier.py | F1b DEF twin falsifier
X-SPDB | engine_speed_bench.py | engine speed bench + gates
X-GENOXC | g0_geno_crosscode.py | G0 cross-code oracle (O3.4)
X-G0 / X-G0AX | g0 spike files | MoC unit-process spikes (planar / axisym+shock)
X-GBE | gbe_ergodic_envelope.py | ergodic G-B envelope carrier
X-IVXC | ivxc_interval_certificate.py | interval convexity certificate
X-LOCD | locus_diagnosis.py | S20 three-way locus diagnosis
X-MGOV | margin_governor.py | margin governor
X-TBAK | margin_tolerance_backoff.py | tolerance-ball backoff (gauntlet C028)
X-O32 / X-O33B | o32_mesh_convergence.py / o33_bench.py | oracles O3.2 / O3.3
X-P2A1 | p2_pA1_symbolic_adjoint.py | Prop. A2 dual-route carrier
X-SLRW | side_load_rotating_lemma.py | rotating side-load carrier
X-T3QS | t3qs_sweep_protection.py | quasi-steady protection carrier
X-THC1 | thermotab_c1_jax.py | C^1 tabulated thermo class
X-U2RG / X-U3BD | u2/u3 carriers | D2.5-U steps U2 / U3
X-VMON | validity_monitor.py | Lambda-form validity monitor
X-XBVP | xbvp_entropy_transfer.py | Cauchy->BVP transfer carrier
X-GRP01..12, X-GRP16 | S9/S12 logs | run_all suite groups as registry carriers
GAP-5 | s25bis_notaknot_twin.py/json | spline natural-BC bias gap (registry row, F2 owner)
GAP-29 | s25bis_gap29_sweep.py/json | halved-constants sensitivity gap / AUDIT:426
GAP-18 | S25 repair notes (context) | gap re-owned to N6
R1-R6 | CLAUDE.md via logs | plan-adherence rules
R25/R26/R28/R29/R30/R31/R32/R33 | S24/S25/S25bis logs, S-ORDINE prompt | census rows (ledger, gap-map, numeric-lint ratchet, pipeline-sense, S25bis, findings-as-code, S-ORDINE)
C-O33 / C-D25U / C-MAJDA / C-HT4 / C-IGMIX / C-XBVP | S9/S19 logs, carriers | declared conditionals (adjoint residual / class uniqueness / stability / closures)
C1 | S22/S23 logs | F1 blocker conditional (GENO), landed
C2, C17, C18, C028 | probe docstrings | choice-ledger rows / gauntlet finding
M0-M6, M-A..M-E | engine_speed_bench, S25/S25bis logs | speed-chain levers and measure checkpoints (M0 also = MASTER doc, context-dependent)
H3 / H4 / H6 | S25bis logs, spdb json | rung-boundary dedup / tail-to-derive+code-identity / cache unification
H1-H6 (EQ-v2) | POST-S20 advisory context | EQ-v2 hypotheses
T-SLRW, T-U2RG, T-LEMA-i/ii/iii, T-T3QS, T-EQBR, T-T7RED, T-NSW, T-XWALL, T-XWS | logs/carriers | registry theorems
T0-T5 | session mandates | per-session task numbering
T2a | a1_loopspeed_bench/S18 | clean-host production gate
O3.1-O3.4, O4, O5 | logs/carriers | oracles (gradient cert / mesh conv / term-match / cross-code; O4 localization; O5 env decision)
P-1 / P-2 | logs | paper records (JPP paper / adjoint lemma paper)
P-A1 / P-A1' / P-A2 / P3 / P4 | rigor logs | Lemma-A propositions / quasi-steady layer
P0-P2 | S21 log | audit triage priorities
S-LBML / S-GBE / S-BLITE / S-XCONV / S-ACFR / S-D25U-U34 / S-H | logs/carriers | registry schemas/statements
A1_REJ_SAVE / A1_COLEXEC / A1_VMAP_HESS | locus_diagnosis, commits | engine env-flag switches (rejected-design persistence / column executor / batched Hessian opt-in)
EQ-v2 | S24 log | equivalence conjecture (CONJECTURE + H-CLASS)
REQ-NONSTALL | S21 log, margin_governor | tier-invariant no-stall requirement
KAT / KAT_BFUN | validity_monitor, S24 log | known-answer tests (GENO B-function KAT) |
G0-G6, G12, G14 | logs, G5 docs | plan gates (G5 = human Kraiko/PMM pass; G12/G14 = rigor/no-bridge claims)
D-GSEP / D-DOM / D-JEX / D-MU | S9/S12 logs | registry definitions
DIR-G0 / DIR-RKG / DIR-ANCHOR | carriers, S14 log | ratified directives (stack decision / segmentation policy / anchor-(P))
NTF (NEWTON_TOL_FACTOR), C_FLOOR, C_OPS | gap29 arms | asserted tolerance factors under sweep (NTF = load-bearing flip)
U1-U4, U3-H1 | S15/S16 logs, u3 carrier | D2.5-U proof steps and condition
LB-c1 / LB-c2 | o32 docstring, S19 | S-LBML clauses
RK-A / RK-G | S17 log | declared risks (scoop / segmentation)
F1b, F-SERVICE, F0-F6 | logs/commits | plan-v3 phases
OBJ-DOM, G1-DISC, P-FLIPMAT, P-TRFLOOR, PAP-RIM, PAP-D9HL | memory/S25 context in logs | registry/ledger row ids seen in passing
X-BVP? none; X-WALL variants T-XWALL/T-XWS only.

(Distinct token families collected: 78.)
