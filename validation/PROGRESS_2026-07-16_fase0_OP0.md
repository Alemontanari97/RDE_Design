# SESSION PROGRESS LOG — Fase 0-chiusura + OP-0 (2026-07-16)

Branch: `rde-nozzle-program`. Tasks of record: T1 (A0.3 gamma probe),
T2 (A0.1 inline biblio fixes), T3 (OP-0 eps-level bound ladder),
T4 (optional OP-11-eps scaffold). Priority order: T3, T1, T2, [T4].

DISCIPLINE: every step below is numbered in a TOTAL ORDER (column `#`);
every .md generated or modified by this session appears here with its
step number; every code artifact appears with its acceptance evidence.
This file is append-only during the session (entries are never rewritten,
corrections get a new entry referencing the old one).

## Step ledger (total order)

| # | When (step) | Action | Artifact(s) | Status / evidence |
|---|---|---|---|---|
| 1 | session open | Mandatory opening: read project memory `research-cycle-averaged-rao`, M0 (`docs/rde_nozzle_MASTER.md`), D3 §5.2, D4 §6, D6 A0/OP-0, python-env memory | — (reads only) | DONE. Branch verified = `rde-nozzle-program` |
| 2 | recon | Repo recon: Table-1 = 18-row `TABLE1` in `src/thrust/stechmann_nozzle.py`; states blessed in `data/st_nozzle_opt.json`; Theorem 1/2 proofs in `validation/bell_optimality_proof.md`; test convention = `run()` module registered in `tests/run_all.py`; numeric lint enforces allowlist on every `src/**` literal | — (reads only) | DONE |
| 3 | log open | THIS FILE created (user directive: total-order step accounting, one row per .md and per codebase work item) | `validation/PROGRESS_2026-07-16_fase0_OP0.md` [.md NEW] | OPEN (append-only) |
| 4 | T3 design | Pre-implementation analysis found a HOLE in the naive G-B rung: "complete expansion to Pa" is NOT the streamtube sup for 1 < Pc/Pa < NPR(1,g) — the sonic exit beats it (hand counterexample g=1.15, Pc/Pa=1.3: CF 0.4656 > 0.4587). Ladder designed with the CHOKING CAP; naive form kept for executable rejection | — (analysis) | DONE; magnitude later confirmed in code (dCF = +0.0070) |
| 5 | T3 code | `src/thrust/bounds.py`: chain C = Isp[eps_fix] <= int-max == ideal(capped) <= B_EK; int-max via explicit Theorem-1 eps*(xi) through Eq. 9; ideal via independent closed form; B_EK via Cauchy-Schwarz on the mdot measure; peak-plug M1 candidate; `check_chain` usable as rejector; tolerance derived: NQ*eps_mach (no magic numbers, lint PASS 19 files) | `src/thrust/bounds.py` [code NEW] | DONE. 18/18 rows chain-OK |
| 6 | T3 data | Ladder evaluated on the 18 Table-1 rows (blessed states + blessed incumbent eps): regimes = 8 supercritical sea-level (plug ATTAINS ceiling, M1 gap-zero), 4 subcritical (CH4/RP-1 20 atm: naive rung VIOLATED, gap 1.9e-7…7e-3 s), 6 vacuum (ceiling unattained at finite eps, Theorem 3) | `data/bounds_ladder.json` [data NEW], `data/bounds_ladder.md` [.md NEW] | DONE, persisted |
| 7 | T3 test | `tests/test_bounds.py` (B1 live==persisted; B2 chain re-run; B3 regime structure; B4 counterexample of record; B5 SEVEN negative controls incl. broken naive-ceiling implementation — the suite REJECTS violated orderings); registered as group (viii) in `tests/run_all.py`. Full fast suite 8/8 PASS in 58 s | `tests/test_bounds.py` [test NEW], `tests/run_all.py` [MOD] | DONE, acceptance of T3 met |
| 8 | T3 docs | Correction of record propagated: M0 Prop. 7 (G-B) + D3 §"Prop. G-B" get the SHARPENING paragraph (sonic cap; naive form valid only above critical NPR; T4/E-K inherit the hypothesis) | `docs/rde_nozzle_MASTER.md` [.md MOD], `docs/rde_nozzle_theorem_ledger.md` [.md MOD] | DONE |
| 9 | T3 commit | One commit for T3 on `rde-nozzle-program` | git | DONE: commit `1a4ff7b` |
| 10 | T1 probe | `examples/gamma_cycle_probe.py` on blessed det\|CH4\|20\|1.64: equilibrium SP family anchored at CJ (201 phases); measured: gamma_s 1.1537→1.2093 (interior min at xi≈0.1, depth 4e-4), gamma_fr 1.2223→1.2286, eps* 3.980→3.958 (shift −0.56%), Isp penalty −0.00028%, CF dev <0.3% early half / Pc-weighted 0.36% | `examples/gamma_cycle_probe.py` [code NEW], `data/gamma_cycle_probe.json` [data NEW] | DONE (~8 s runtime) |
| 11 | T1 verdict | D3 §5.2 claims adjudicated: "gamma_s 1.154→1.210" CONFIRMED to its own rounding (1.209); "eps* −1.9%" STRUCK → −0.56% (diagnosis: unweighted-mean closure gives −2.39%, the likely stale source; the D3 gamma_eff=⟨Pcγ⟩/⟨Pc⟩ closure gets first executable confirmation: −0.57% vs −0.56%); "Isp −0.001%" corrected in magnitude → −0.00028%, second-order structure penalty ≤ shift² now a test gate | — (analysis) | DONE |
| 12 | T1 test | `tests/test_gamma_probe.py` (G1 anchor; G2 valley+rise structure; G3 golden digits; G4 re-derivation from persisted arrays; G5 envelope inequality; G6 closure discrimination + reversed-array negative control — REJECTS wrong averaging and corrupted records); registered as group (ix). Full fast suite 9/9 PASS in 59 s | `tests/test_gamma_probe.py` [test NEW], `tests/run_all.py` [MOD] | DONE, acceptance of T1 met |
| 13 | T1 docs | Corrections propagated to ALL stale-number sites (grep-verified): D3 §5.2 + P6 [.md MOD]; D4 §1 row, §2 P6 row, §6.3 DONE [.md MOD]; historical note 5.1b corrected INLINE + banner updated [.md MOD]; mathematical_foundations P6 [.md MOD]; D6 shop-rule + A0.3/A0.4 DONE markers [.md MOD]; D7 E5 row CLOSED [.md MOD]; roadmap WP2 N4 number [.md MOD] | `rde_nozzle_theorem_ledger.md`, `rde_nozzle_claims_verdict.md`, `cycle_averaged_variational_nozzle.md`, `mathematical_foundations_rde_nozzle.md`, `rde_nozzle_development_plan.md`, `rde_nozzle_pipeline_audit.md`, `roadmap_geno_rde.md` | DONE |
| 14 | T1 commit | One commit for T1 on `rde-nozzle-program` | git | DONE: content in `f4cd429` + `9b2bcde` (checkpointed by the concurrent session from the shared working tree) + `e77f63b` (this log's T1 rows) |
| 15 | note | CONCURRENT SESSION detected on the same branch/working tree: commits `f4cd429`, `ae9f109` (CLAUDE.md rules R1-R6 + living `docs/rde_nozzle_PROGRESS.md`), `9b2bcde` are its checkpoints of the shared tree. No content conflict; governance files adopted from here on | — | RECONCILED |
| 16 | T2 fixes | Inline biblio corrections in the historical notes: (a) `cycle_averaged_variational_nozzle.md` §survey passage now carries the CORRECT split citations (Li-Xu-Huang JPP 38(5):849 (2022) RDE; Mo et al. Acta Astronautica 108:92 (2015) scramjet) with the conflation note; (b) `mathematical_foundations_rde_nozzle.md` Sternin now carries the two-phase caveat (general treatise = Pirumov-Roslyakov). Rao 1958/1960/1961 usage audited: already consistent everywhere; S-H title correct at every full citation | `cycle_averaged_variational_nozzle.md` [.md MOD], `mathematical_foundations_rde_nozzle.md` [.md MOD] | DONE |
| 17 | T2 gate | Control greps (A0.1 acceptance): (1) `Mo,\s*Huang` outside correction contexts → 0 hits; (2) `Performance Model` not preceded by exact title → only line-wrap false positives of correct citations; (3) `Rao 1961` without spike/review context → 0 hits; (4) Sternin caveat present at the one general-text citation site. GATE CLEAN | — (gate record here) | PASS |
| 18 | T2 commit | One commit for T2 | git | see hash below |

## Deliverable map (filled as work completes)

| Task | Code | Test | Data | Docs touched | Commit |
|---|---|---|---|---|---|
| T3 OP-0 | `src/thrust/bounds.py` | `tests/test_bounds.py` | `data/bounds_ladder.json` | (this log; ledger/verdict if needed) | pending |
| T1 A0.3 | `examples/gamma_cycle_probe.py` | `tests/test_gamma_probe.py` | `data/gamma_cycle_probe.json` | D3 §5.2, D4 §6.3 (reproduce-or-strike) | pending |
| T2 A0.1 | — | grep gate (recorded here) | — | historical notes (inline fixes) | pending |
