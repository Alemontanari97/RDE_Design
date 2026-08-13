# INVENTORY — Segment 6: persistent memory directory (S-ORDINE Phase 1, reader "seg6-memory")

Date: 2026-08-13. Reader: seg6-memory. Authoritative list:
`validation/sordine_raws_2026-08-13/seg6_memory_files.txt` (37 files).
Segment root: `C:/Users/amont/.claude/projects/c--Users-amont-Claude-Projects-Presentazione-RDE-CVA-rde-lecture-code/memory/`
(all PATHs below are relative to this root).

Coverage: **37/37 accounted, 37 read integrally, 0 classified-without-read.**
All files are markdown; none exceeded a single read.

Legend for STATUS: OF-RECORD / SUPERSEDED-BY-x / CONSUMED / RAW / DERIVED.
Memory-specific status refinement used below:
- **CURRENT-STANDING** = OF-RECORD standing directive/preference, still binding.
- **CURRENT-BRIDGE** = OF-RECORD continuity bridge (points to untracked/of-record artifacts the opening protocol would not surface).
- **HISTORICAL-SESSION** = session memory whose NEXT/routing half is superseded by the following session memory, but whose verdict half is still the compact of-record summary; NOT marked superseded in-file (the named entropy source).

---

## 0. Segment-level findings (the answers the brief asks for)

**F1 — MEMORY.md index integrity: 36/36 files have an index line; 2 inline-only entries; 1 STALE index line.**
- Every one of the 36 memory files has exactly one matching index line in MEMORY.md.
- MEMORY.md additionally carries TWO entries with NO backing file (inline-only memory):
  - line 26 "POST-S20 (2026-08-07 …)" — the inter-session window record (6 advisories landed, REQ-NONSTALL verbatim user requirement).
  - line 29 "POST-S21 SERA (2026-08-11 …)" — choking/collapse/swirl census record (5 papers read, Harroun misquote, 2 session prompts ready, Giles-Ulbrich on disk).
  These are UNIQUE-AT-RISK: index-only prose, not typed, not in any memory file; content partially mirrored in the advisories they cite but the *status/ingestion framing* lives only here.
- STALE INDEX LINE: MEMORY.md line 1 says "numpy must be pinned to 2.2.6" but `python-env-cantera.md` itself contains a dated **[SUPERSEDED 2026-08-06 S17]** block: pin DISCHARGED, numpy>=2.0, env on 2.5.1. The index contradicts its own file. (Open user decision O5 = numpy 2.5.2 adoption, per PROGRESS — so the stale line is actively misleading.)

**F2 — The known entropy source, enumerated: old session memories NOT marked superseded.**
Session memories form a chain s14 → s15(+16) → s17 → s18 → s19 → s20 → s21 → s22 → s23 → s24 → s25 → s25bis. Each one's "Why / next session opens here" routing half is superseded by the next memory in the chain, but only TWO carry any supersession marking:
- `s17-brick2-kickoff.md` — index line only: "[NEXT-1 superseded: vedi s18-brick2-closed]" (file body unmarked).
- `s23-f1-closed.md` — in-file dated "SUPERSEDING UPDATE (2026-08-12)" block (S24=F1b not F2), exemplary practice.
UNMARKED (routing half stale, no banner): **s14, s15-foundations-campaign, s18, s19, s20, s21, s22, s24, s25** (s25bis is the live head). Also partially superseded content inside standing files: `s14-panel-verdict-canonical-loop` loop-shape half extended by `agentic-orchestration-forms` (Forms 1-3 + full-text rule); `roads-insertion-matrix-directive` sequencing pin "[PAP-RIM] after brick 2" is stale (brick 2 closed S18; never-postpone-resolvables flags PAP-RIM/census-lemma as the twice-migrated smell); `s15` "How to apply" (brick-2 re-adjudication) consumed by S17. Proposed T2(v) sweep action: dated supersession banner on the routing half of each HISTORICAL-SESSION memory, verdict half untouched (R4).

**F3 — Link integrity ([[name]] targets): 3 broken/non-resolving.**
- `generality-litmap-review.md` → `[[s24-deftw]]` — target does not exist; the actual file is `s24-f1b-def-twin.md` (the litmap memory was written "if created by the carrier session" before the name existed; never repaired).
- `sspeed-engine-speed-audit.md` → `[[s24-*]]` — wildcard, not a resolvable target (intent = s24-f1b-def-twin).
- `scope-pins-frozen-thermally-perfect.md` → `[[s-gauntlet absorption in PROGRESS log]]` — prose pseudo-link, no such memory.
All other [[targets]] (~60 occurrences checked across the 36 files) resolve to existing memory files.

**F4 — Structural observation for the target design**: `research-cycle-averaged-rao.md` is a dual-role file (project overview + accreted S1–S13 session-history log, ~509 lines) — it is the memory-side mirror of the PROGRESS.md monotone-growth entropy pattern; its per-session content largely duplicates the committed `validation/PROGRESS_2026-07-*` logs and doc deltas. Candidate for the same slim+archive treatment as PROGRESS (T2(iv) pattern), keeping the overview/opening-protocol/corrections-of-record head.

**F5 — Orphans: none.** Every memory file answers a nameable plan need (R2 opening protocol, a standing R1–R6 rule extension, or the census/phase continuity chain). 0 orphan candidates.

---

## 1. Per-file inventory

### MEMORY.md
- CLASS: memory (index)
- ROLE: auto-memory index; one line per memory file + 2 inline-only entries (POST-S20, POST-S21 SERA); injected at every session open.
- STATUS: OF-RECORD (live index) — with 1 STALE line (python-env numpy pin, see F1) and 2 untyped inline entries.
- PLAN-ANCHOR: CLAUDE.md R2 (session-opening mandatory read); S-ORDINE R32 target object (T2(v) memory sweep).
- UNIQUE-AT-RISK: the two inline entries POST-S20 / POST-S21 SERA (window records: 6-advisory ingestion order for S21; 5-paper choking census status, Harroun-misquote flag, Scollapse/Sgauntlet prompt readiness, Giles-Ulbrich ×2 on-disk / AIAA 2019-0197 wanted) — no backing file, no registry row.
- REFS: out → all 36 files; in ← system context injection every session.

### Standing directives / preferences (type = feedback unless noted; ALL CURRENT-STANDING OF-RECORD)

Common UNIQUE-AT-RISK property of this whole block: each carries the **verbatim (Italian) user order with date and session of issue** — the authoritative wording exists nowhere in the repo (CLAUDE.md/advisories carry English paraphrases). Losing these files loses the primary-source form of the standing rules.

#### gate-pre-esecuzione.md
- ROLE: pre-execution gate (plan adherence + upstream rigor audit + logged verdict) before any task.
- STATUS: OF-RECORD. PLAN-ANCHOR: extends CLAUDE.md R1/R2; consumed by every session log "gate pre-esecuzione PASS" step; S-ORDINE prompt §(1) mandates it.
- UNIQUE-AT-RISK: verbatim order + the two historical drift incidents motivating it (phase-diagram winners misread; optimum-is-for-constraints challenge).
- REFS: out → research-cycle-averaged-rao, repo-sota-standard; in ← ~8 other memories.

#### repo-sota-standard.md (type: project)
- ROLE: the bar — SOTA academic+industrial RDE design tool; PRISTINE WRITING + verification-sufficiency declarations + anchor to (P) of M0 D2.6.
- STATUS: OF-RECORD. PLAN-ANCHOR: overarching program standard (D6 preamble; R5 discipline).
- UNIQUE-AT-RISK: the 2026-07-16 standing additions block (pristine writing / sufficiency declarations) in this exact form.
- REFS: out → python-env-cantera; in ← most directive memories.

#### gamma-variable-generality.md
- ROLE: variable-gamma generality directive + full gamma-purge record (strengthened form, architecture inversion, ladder+diagram purge completion with measured deltas).
- STATUS: OF-RECORD (purge record itself closed/CONSUMED into M0 Prop.7 + D3; directive live).
- PLAN-ANCHOR: R4 back-propagation; M0 Prop.7 GAMMA-PURGE INSTANCE; P-1 acceptance rule (e).
- UNIQUE-AT-RISK: verbatim strengthened order; the consolidated purge narrative (numbers 4.4-7.9% below oracle, +6.3..+7.0% eq bracket, knee 10.38 vs ~12.9) is mirrored in M0/D3 — memory-only part = the order's wording and the S7/S8 commit trail as one narrative.
- REFS: out → gate-pre-esecuzione, research-cycle-averaged-rao; in ← scope-pins, thermo-tabulated, topology-census.

#### periodic-wave-data-scope.md (type: project)
- ROLE: standing modeling assumption (pure periodic rotating wave; T0 flatness monitor; algorithm stays fully general; pins in M0 VI.4bis).
- STATUS: OF-RECORD. PLAN-ANCHOR: M0 VI.4bis; D3 §3 C-T1; F5 data contract (G6).
- UNIQUE-AT-RISK: verbatim clarification "algoritmo sempre pienamente generale"; consequences (1)-(4) list — mirrored in D3/M0.
- REFS: out → research-cycle-averaged-rao, gamma-variable-generality.

#### thermo-tabulated-backend.md
- ROLE: [DIR-THERMOTAB] — JAX thermo = table reading; Cantera sole production generator; technical pins (NasaPoly2 coeff order, s0 at 1 atm, derived dual-route budget 2.5e-4).
- STATUS: OF-RECORD. PLAN-ANCHOR: registry [DIR-THERMOTAB]; A1/F2 engine architecture; S24 thermo survey (KEEP quintica) rests on it.
- UNIQUE-AT-RISK: the empirically-determined coeff-order pin and the "budget not machine floor" rationale in narrative form (also in [DIR-THERMOTAB] registry row / S11 log).
- REFS: out → gamma-variable-generality, research-cycle-averaged-rao; in ← s24-f1b-def-twin.

#### moc-critical-independent-invariants.md
- ROLE: never assume GENO bug-free; GENO-independent invariant list; critical list of deliberately mirrored GENO quirks (NASA-poly Thigh extrapolation, y2==0 guard, |M-Me|<1e-5, gammamedio Sauer).
- STATUS: OF-RECORD. PLAN-ANCHOR: G1/oracle discipline (R6); O3.x bench design; F2 engine work.
- UNIQUE-AT-RISK: the consolidated mirrored-quirk critical list as a single checklist (individual items scattered in carrier docstrings/logs).
- REFS: out → sota-library-survey, general-vision, repo-sota-standard; in ← generality-litmap, s17.

#### general-vision-nondivergence.md
- ROLE: never diverge into rabbit holes; decide forks from the program picture; honest state + named lever when abandoning a local fight.
- STATUS: OF-RECORD. PLAN-ANCHOR: R1 discipline at mid-session forks; census "leva nominata" convention.
- UNIQUE-AT-RISK: verbatim order + the S17 mega-jit origin story.
- REFS: in ← ~7 memories.

#### sota-library-survey-directive.md
- ROLE: survey open SOTA libraries before implementing complex numerics; TOOLCHAIN-CURRENCY half (never version-limited); READ-THE-SOURCE half (adoption ≠ trust).
- STATUS: OF-RECORD (its numpy-pin example paragraph is historically dated — pin since discharged — but framed as "as of 2026-08-06", acceptable).
- PLAN-ANCHOR: choice-adjudication precursor; D6 tool matrix; S-SPEED env verdict rests on the currency half.
- UNIQUE-AT-RISK: three verbatim orders (survey / currency / read-the-source) — the tripartite structure only here.
- REFS: out → repo-sota-standard, gate-pre-esecuzione; in ← choice-adjudication, s17, sspeed.

#### generality-nonhardcoded-procedures.md
- ROLE: every procedure general + SOTA + economical, never case-tuned (nodes, basis, iterations); economy is part of correctness.
- STATUS: OF-RECORD. PLAN-ANCHOR: [C-O33] design-class attribution (S19-S20); adaptive-class work; choice ledger.
- UNIQUE-AT-RISK: verbatim order; the S19 6.63%→2.0% class-not-physics motivating datum (also in S19 log/memory).
- REFS: in ← s19, s20, orchestration-weight, sspeed.

#### agnostic-milestone-review-directive.md
- ROLE: agnostic audits (committed+uncommitted, milestone-anchored, rabbit-hole boundary pre-named, one alternative frame per obstruction).
- STATUS: OF-RECORD. PLAN-ANCHOR: AUDIT_agnostic pattern; S-CERT (R33) is this directive's next instance.
- UNIQUE-AT-RISK: verbatim order + the S20 step-7 audit scope-failure rationale.
- REFS: out → general-vision, gate-pre-esecuzione, repo-sota-standard; in ← s20, s21, claim-dual-proof.

#### self-improvement-at-convergence.md
- ROLE: on proven method convergence, self-improve immediately and register it (memory/form/CLAUDE.md delta), unasked.
- STATUS: OF-RECORD. PLAN-ANCHOR: the mechanism behind every "standing rules extended" block (e.g. s25bis tail); S-ORDINE T3 education deliverable is its instance.
- UNIQUE-AT-RISK: verbatim order.
- REFS: out → agentic-orchestration-forms, agnostic-milestone, general-vision.

#### claim-dual-proof-standard.md
- ROLE: THE working standard — every claim = converged theory half + rejector-bearing implemented case; CAUTO-MA-SOTA addendum (curious in search, rigorous at adoption).
- STATUS: OF-RECORD. PLAN-ANCHOR: extends R5; claims-to-code table (ADVISORY_claims_to_code); triple-proof extension in pipeline-sense-expert-review.
- UNIQUE-AT-RISK: verbatim order + the refined "non essere troppo cauto…" addendum wording.
- REFS: out → 4 memories; in ← choice-adjudication, pipeline-sense, s21-s24.

#### roads-insertion-matrix-directive.md
- ROLE: no over-math (depth = slot contract) + [PAP-RIM] roads×insertions matrix census (I1-I11 axes, verdict vocabulary, I10 formal-certification-ladder pre-pinned content).
- STATUS: OF-RECORD directive; **sequencing pin STALE** ("after brick 2" — brick 2 closed S18; PAP-RIM still unexecuted = the never-postpone twice-migrated smell; needs a live owner row).
- PLAN-ANCHOR: DIR-SUFF; D8 §6 roads register extension; census queue row [PAP-RIM].
- UNIQUE-AT-RISK: the I10 pre-pinned four-row certification-ladder content (user-approved in chat 2026-08-06) — the fullest statement lives ONLY here; verdict vocabulary {ADOPTED, ADOPTED-AS-NAMED, PROPOSER-ONLY, KILLED, OPEN}.
- REFS: out → s15-foundations, repo-sota-standard, gate-pre-esecuzione; in ← general-vision, scope-pins.

#### scope-pins-frozen-thermally-perfect.md
- ROLE: user scope pins P1 (frozen thermally-perfect mixture, gamma(T) free = H1-T class) + P2 (two-phase excluded) + anti-overengineering order.
- STATUS: OF-RECORD. PLAN-ANCHOR: M0/ledger S-GAUNTLET absorption; every duty/phase adjudication filter.
- UNIQUE-AT-RISK: verbatim pins; (registered in M0/ledger per the file, so content recoverable — wording unique).
- REFS: out → general-vision, roads-insertion, gamma-variable + 1 broken pseudo-link (F3).

#### never-postpone-resolvables.md
- ROLE: postponement legitimate only if structurally gated (owner+trigger); twice-migrated = mislabeled, execute; R3 queue sweep.
- STATUS: OF-RECORD. PLAN-ANCHOR: R3 closure checklist; census conditional discipline; findings_registry OPEN⇒owner+trigger schema is its machine form.
- UNIQUE-AT-RISK: verbatim order + the GENO-flagdef 4-day-debt case study; the C4/census-lemma/PAP-RIM migration smell list.
- REFS: out → general-vision, gate-pre-esecuzione, s23-f1-closed; in ← s24, s25, s25bis.

#### choice-adjudication-convergence.md
- ROLE: every algorithmic choice adjudicated to convergence vs SOTA alternatives, no incumbent bias; CHOICE LEDGER artifact; commit-time row declaration (R5 extended to choices).
- STATUS: OF-RECORD. PLAN-ANCHOR: census R25 (choice ledger carrier); S-ORDINE T2(ii) = docs/choice_ledger.yaml extraction.
- UNIQUE-AT-RISK: verbatim order; the S24 seeded open-rows list (spline vs control points; AMR/DWR; MPCC; differentiable mask; K_RICH=4) — also in the gap-map annex.
- REFS: out → 4 memories; in ← orchestration-weight, s24, s25.

#### pipeline-sense-expert-review.md
- ROLE: two-level expert sense-review of every algorithmic piece (whole-pipeline + per-step), cadence = every algorithmic touch; 3-bis convergence-mandatory clause; triple proof gate+refuter+sense-review.
- STATUS: OF-RECORD. PLAN-ANCHOR: census R29; the S25/S25-bis pipeline-sense advisories are its instances.
- UNIQUE-AT-RISK: verbatim order + 3-bis convergence-mandatory verbatim.
- REFS: out → 5 memories; in ← orchestration-weight, s25, s25bis.

#### orchestration-weight-sota.md
- ROLE: orchestration weight optimized like an algorithmic choice: right-size pre-launch, merge, pointed briefs, resume-not-relaunch, no ritual rounds, weight reported.
- STATUS: OF-RECORD. PLAN-ANCHOR: standing census row (S25 close); S-ORDINE T2-bis(c) = its education deliverable.
- UNIQUE-AT-RISK: verbatim order + the measured motivating data (~270k tokens/review, stalled red-team).
- REFS: out → 4 memories.

#### agentic-orchestration-forms.md (type: project)
- ROLE: canonical multi-agent forms — Form 1 find→verify, Form 2 panel-to-convergence, Form 3 red-team-before-absorption (with the measured S21 judge-layer failure modes) + 7 session-management rules incl. FULL-TEXT adjudication (S-GAUNTLET sliced-judge failure).
- STATUS: OF-RECORD; extends (partially supersedes the loop-shape half of) s14-panel-verdict-canonical-loop.
- PLAN-ANCHOR: every workflow of record since 2026-08-07; S-ORDINE T1 phases 2-5 are built on Forms 1/2/3.
- UNIQUE-AT-RISK: the enumerated measured judge-failure modes (RT-1/RT-2/RT-3, manufactured unanimity, silent weakenings) and the S-GAUNTLET slice evidence as one operational doctrine — advisories carry the instances, only this file carries the doctrine.
- REFS: out → s14, agnostic-milestone, s20; in ← ~8 memories.

#### python-env-cantera.md (type: project)
- ROLE: how to run examples/tests live (MS-Store Python 3.13 path, pip --user, suite timing); numpy-pin SUPERSEDED block; cp1252 console caveat.
- STATUS: OF-RECORD with in-file dated supersession (good practice); **MEMORY.md index line STALE** (F1).
- PLAN-ANCHOR: R2 env prerequisite for every suite/gate run; O5 (numpy 2.5.2) user decision context.
- UNIQUE-AT-RISK: HIGH — env-run instructions, interpreter path, cp1252 UnicodeEncodeError workaround, np.trapz history: recoverable nowhere in the repo (requirements.txt gives versions, not procedure).
- REFS: in ← repo-sota-standard, s17.

### Continuity-bridge project memories

#### research-cycle-averaged-rao.md (type: project)
- CLASS: memory (project overview + accreted session history S1-S13, ~509 lines)
- ROLE: research-goal statement, D1-D6 deliverable map, corrections of record (Mo/Huang conflation, S-H/Rao bibliographic fixes, gamma-probe numbers), opening protocol S10+, and per-session closure blocks S1-S13.
- STATUS: split — overview/protocol/corrections head OF-RECORD; the S1-S13 session blocks are HISTORICAL, largely CONSUMED into the committed PROGRESS_2026-07-* logs, M0/D-docs and claims registry (F4: memory-side PROGRESS-entropy mirror; slim+archive candidate).
- PLAN-ANCHOR: R2 opening protocol; phases A0-A2 history; D1-D7 map.
- UNIQUE-AT-RISK: MEDIUM — most numbers/verdicts are mirrored in committed docs; unique = the cross-session narrative glue (concurrency violations count, "ONE SESSION AT A TIME" enforcement history, WebFetch-fabricates-PMM method finding — the latter also in the S7 log).
- REFS: out → repo-sota-standard, python-env-cantera; in ← ~6 memories.

#### topology-census-pins.md (type: project)
- ROLE: continuity bridge to the UNTRACKED PANEL_topology_census_2026-07-22.md + all 4 user pins of 2026-08-02 (Omega cone carrier, permissive attachment, NONBLOCK+, Lambda=lip circles) + queued census-lemma session duties.
- STATUS: OF-RECORD / CURRENT-BRIDGE (census-lemma session STILL unexecuted — live queue row; the "after brick 2" sequencing is stale per never-postpone).
- PLAN-ANCHOR: D2.1 amendment duties; sector/topology gate ("read the doc before touching topology"); census queue row (census-lemma).
- UNIQUE-AT-RISK: the file says pins are recorded in the panel doc §7pin — but the panel doc is UNTRACKED single-copy; this memory is the only second copy of the pin summary + the only pointer that surfaces it at session open. Effectively at-risk pair.
- REFS: out → research-cycle-averaged-rao, s14, gamma-variable; in ← MEMORY.md warning line.

#### generality-litmap-review.md (type: project)
- ROLE: 2026-08-12 parallel litmap session record: 24-PDF generality map advisory + DISPATCH to S24; O3 sources found on disk (Sternin dan25254.pdf, Shmyglevskii 0041-5553…pdf); Rao 1961 Eq.(8)/(9) label swap; ingestion-pending flag.
- STATUS: OF-RECORD; the DISPATCH-pending-ingestion clause is now CONSUMED (S24 ingested O3 adjudication per s24 memory) but NOT marked here — minor staleness.
- PLAN-ANCHOR: F1b/O3 gate (ACQUIRE→ADJUDICATE); literature registry T2(vi) (identity of the opaque-named PDFs is load-bearing for seg7).
- UNIQUE-AT-RISK: the opaque-filename↔bibliographic-identity mapping (dan25254.pdf = Sternin DAN 139(2) 1961; 0041-5553%2880%2990091-9.pdf = Shmyglevskii CMMP 20(5)) — also in the advisory; the [[s24-deftw]] BROKEN LINK (F3).
- REFS: out → BROKEN [[s24-deftw]], research-cycle-averaged-rao, moc-critical; cites both validation advisories.

#### sspeed-engine-speed-audit.md (type: project)
- ROLE: S-SPEED parallel session record: plan of record pointer (ADVISORY_engine_speed_audit + DISPATCH), 5 verdicts-not-to-relitigate, M0-M6 mandatory set framing.
- STATUS: OF-RECORD; execution half CONSUMED by S25/S25-bis (targets met) — routing stale, verdict list still the compact of-record summary.
- PLAN-ANCHOR: census R22/R30 chain; S25 dispatch ingestion.
- UNIQUE-AT-RISK: low — advisory/dispatch files carry the substance; the [[s24-*]] wildcard link (F3).
- REFS: out → [[s24-*]] (broken), agentic-orchestration-forms, sota-library-survey, generality-nonhardcoded.

### Session-memory chain (all CLASS: memory, type: project; all HISTORICAL-SESSION except s25bis = live head)

Common pattern: verdict half = compact of-record summary duplicating the committed session log + commit messages; routing/"Why next session" half = superseded by the next memory, unmarked (F2). PLAN-ANCHOR per file = the phase it closes + its census rows. Bulk rows, with per-file unique-at-risk:

| PATH | ROLE (phase closed) | STATUS | PLAN-ANCHOR | UNIQUE-AT-RISK |
|---|---|---|---|---|
| s14-panel-verdict-canonical-loop.md | D8 panel of record + canonical loop shape | OF-RECORD verdicts; loop-shape half extended by agentic-orchestration-forms (unmarked) | D8 [PAN-S14]; brick-2 protection | cache/sorted-keys/journal loop mechanics (partially re-stated in orch-forms); "D8 §8 residue not settled" guard |
| s15-foundations-campaign.md | S15+S16 foundations tranches | HISTORICAL-SESSION (re-adjudication clause CONSUMED by S17) | [RIGOR/A] queue; U1-U4, ledger p1/p2 | named rigor-bench leftovers list (B1 interval s_L, C-XBVP(b), GBE concavity, g-scan B3) — the queue's only consolidated statement outside PROGRESS |
| s17-brick2-kickoff.md | brick-2 kickoff, 4 duties, X-TOCV staged | HISTORICAL-SESSION (index-marked NEXT-1 superseded) | D6 item 9; A1 brick 2 | GENO Interior_m no-margin-guard finding; axial-margin rejector rationale (also kickoff doc §5bis) |
| s18-brick2-closed.md | BRICK 2 CLOSED, O3.3 unlocked, T2 fired | HISTORICAL-SESSION | D6 item 9 close; G0/T2 flip clause | run-of-record numbers (KKT 7.745e-02, J* 2.7761688e+07, 343x T2a) — mirrored in log/G0 doc |
| s19-o33-campaign.md | O3.2/O3.3 campaign | HISTORICAL-SESSION | P-2 numeric half; [X-O32]/[X-O33B] | Rao control-surface LOCUS ERROR warning ("do not repeat"); 2 GENO data defects (double exit point, attachment≠max angle) |
| s20-adaptive-obstruction.md | C-O33 obstruction, formulation gap | HISTORICAL-SESSION | [X-AKNO]; M0 tier ladder | Sternin/Rao-Beck adjudication narrative; Rao-vs-Zucrow naming-inversion warning (also M0) |
| s21-f0-order-instrumentation.md | F0 complete, plan v3 ratified | HISTORICAL-SESSION | D6 §0-pre; F0 | red-team correction wording (RT-1..RT-4) as applied; armed-not-consumed env flags list (A1_CERT_ARGMAX, A1_REJ_SAVE) |
| s22-f1-governor-o4.md | F1 s.1: O4 discharged, bridge falsified, X-MGOV | HISTORICAL-SESSION | F1; [X-LOCD]/[X-MGOV] | process lessons (git-bash kill -0 MSYS pids; WindowsApps alias; res.v unverified) — partially only here |
| s23-f1-closed.md | F1 CLOSED, P-2 freeze, GENO conditional landed | HISTORICAL-SESSION w/ exemplary in-file superseding update | F1 close; ISS-5 | GENO fca273a return findings (tocnoz was MILD-DEF; N-74) — cross-repo, also in GENO docs |
| s24-f1b-def-twin.md | F1b closed: construction-surface discovery, H-CLASS | HISTORICAL-SESSION | F1b; [X-DEFTW]; census R1-R27 consolidation | AIAA 2019-0197 = PHANTOM verdict; process lessons (pre-scan constraint field, docstring-promise rule, tail -f, grep -c) |
| s25-engine-speed.md | C4 closed + M-chain M0-M5ab | HISTORICAL-SESSION | census R22/R25/R28-30; [X-SPDB] | refuter-found defect narratives (class-key engine cache; _mkey knobs); frozen-code re-chain rule origin |
| s25bis-speed-complete.md | speed targets MET; M6 convergence; R31/R28; session chain ratified | OF-RECORD — LIVE HEAD (routing = S-ORDINE→S-CERT→F2, current) | census R30 consumed, R31/R32/R33; F2-entry row list | the ratified session-chain order + F2-entry row list ([OBJ-DOM], delta-carrier, GAP-1/2, NTF, GAP-5, [G1-DISC], M6, lint classification) — also in PROGRESS/commit msg |

---

## 2. Codename tokens collected (feeds T2-bis glossary)

token | where seen (memory file) | meaning if evident
- R1..R6 | CLAUDE.md via all | codebase protocol rules (orphan-step ban … gates)
- R7c,R22,R25,R26,R28,R29,R30,R31,R32,R33 | s25*, MEMORY.md | PROGRESS census rows (R28 numeric-lint ratchet; R29 pipeline-sense; R30 S25-bis; R31 findings-as-code; R32 S-ORDINE; R33 S-CERT)
- A0-A7, F0-F6, F1b, F2a, F4b, F5 | plan memories | D6 phases (historical / v3 work index)
- G0..G6, G12, G14, G17, G1-surrogate | several | plan gates; G12 = multi-D shape-derivative gap; G1 = oracle gate
- T0..T7 | research-c-a-rao, periodic-wave | theorem ladder (T0 thrust flatness; T3 collapse; T7 averaged system)
- (P), (**), (**'), (G)/Lambda-form, EQ-v2, H-CLASS, H1-H6, H1-T, H7-SEL | s21/s24/scope-pins | problem of record; weighted transversality; equivalence conjecture + hypotheses
- REQ-NONSTALL | MEMORY.md POST-S20, s21 | user req: optimum search never stalls on internal-shock fields
- KAT, KAT_BFUN | s23, gamma | known-answer test
- [X-*] carriers: X-TOCV, X-SCANM, X-LSG0, X-THC1, X-IVXC, X-U3BD, X-GBE, X-ACFR, X-CDKAT, X-VMON, X-MGOV, X-LOCD, X-TBAK, X-DEFTW, X-A1IM, X-GENOXC, X-O32, X-O33B, X-AKNO, X-SPDB, X-T3SI-conv, X-TRED(X-XRED) | session memories | registry carrier IDs
- [T-*]/[S-*]/[C-*]/[D-*] registry rows: T-SLRW, T-XWALL, T-XWS, T-XSON, T-U2RG, T-LFEQ4, T-T3QS, T-T3-SI, T-EQBR, S-XCONV, S-D25U-U34, S-ACFR, S-GBE, S-LBML, S-BLITE, C-D25U, C-MAJDA, C-XBVP, C-O33, C-EQV2, C-T1, C-HT4, C-IGMIX, C-P4RZ, C-A..C-D, D-P, D-GSEP, DIR-RKG, DIR-G0, DIR-THERMOTAB, DIR-SUFF | s15/s16/s21+ | claims-registry typed rows
- U1..U5, U3-H1, U3' | s15/s21 | foundations lemmas / use-case duties; U3-H1 = Lopatinskii scalar
- O1..O5 | s21 ledger | obligations (O3 = classical-corpus adjudication; O5 = unsteady route / ALSO numpy-2.5.2 user decision id in BLOCCATO — collision to flag for glossary)
- O3.1/O3.2/O3.3/O3.4 | many | adjoint/oracle benches
- M0..M6, M5a/b/c, M-A..M-E, M-CHAIN, M1-M5 (global-optimality contract in M0 — collision with speed levers, flag) | s25* | speed levers / stop-checks
- H3, H4 | s25bis | cap-protection levers (rung dedup; code-identity)
- L1..L5 | s24 | speed lever candidates; L4-DEFAULT (s15) = ledger default — collision, flag
- P0/P1/P2 (triage), P1-P4 (production levers), P-1/P-2 (papers), P4 (corrector), [P-TRFLOOR], [P-FLIPMAT], PP-2 | several | overloaded P-namespace — glossary must disambiguate
- GAP-5, GAP-18, GAP-29 | s25bis | gap-map rows (GAP-29 = NEWTON_TOL_FACTOR flip; GAP-5 = natural-BC corner bias)
- A1_* flags: A1_CERT_ARGMAX, A1_REJ_SAVE, A1_COLEXEC, A1_VMAP_HESS, A1_MEMO_PROBE | s21/s25bis | arbitration env flags (T2-bis(b) registry)
- K_RICH, K_NEWT, NEWTON_TOL_FACTOR, C_FLOOR, C_OPS, L_TB, N_NEWTON, EPS sc | s22-s25bis | derived constants
- KS, TR-SQP, DWR, AMR, MPCC, SDP | s20/s22/choice-adj | methods (KS aggregation; trust-region SQP)
- [C-1], C1..C8 (audit clusters), C1 (P-2-freeze blocker), C3/C5/C7 (panel conditionals), C6 (pre-entry) | s20-s25 | overloaded C-namespace — glossary must disambiguate
- ISS-2, ISS-5 | s21/s23 | plan issue rows (P-2 decoupling/freeze rules)
- DUTY-2/4/5/6/8/15, D-A..D-F, [D1] | s21-s23, litmap | phase duties; [D1] = corner-metric testability criterion
- RT-1..RT-4 | orch-forms/s21 | red-team issue ids
- RK-A, RK-E, RK-F, RK-G | s15/s17 | risk/policy register rows (RK-G = record/replay policy)
- CEN-O1..O11 | topology-census | census open points
- N-36, N-71, N-74 | moc-critical/s23/s24 | GENO bug-register ids
- LB-c1/LB-c2 | s19 | S-LBML declared clauses
- [PAP-RIM], [PAP-D9HL], [PAP-GMAX], [PAP-P1S1389], [PAP-P1S57], [PAN-S14] | roads-insertion/s15/rao | paper/panel registry rows
- [OBJ-DOM], [G1-DISC] | s25bis | F2-entry registry rows
- STIM-1/STIM-2 | s22 | rejector stimulus ids
- TWIN-C, T0-flatness, D'(D-prime), DE-side bucket | litmap/s24 | swirl twin; Rao-Beck jump point; margin bucket
- B1/B2/B3 (interval gates), a-B2/a-B3 | s15/orch-forms | substrate certification gates
- H-E4, E4, E8, E9a-E9r, EAP, S-H | rao/gamma/s14 | hypothesis risks / erratum fixes / Kaemming-Paxson EAP / Scofield-Hoffman
- Q1-Q6, Q2/A-G, Q3(a-c), Q11 | sspeed/s25/prompt | quarantine rows
- X-SPDB, m0/m12gate/m4gate/m5gate/m5cgate/m6gate/h3gate/mbwalk | s25/s25bis | speed bench + gates
- NI, NTF | s25bis | march node count; NEWTON_TOL_FACTOR short form
- F1-F7 (twin verdict branches) | s24 | [X-DEFTW] decision branches — collision with phases F1-F6, flag
- OP-0, OP-11(-eps), OP-1..OP-10 | rao | ranked open problems
- IVL, MoC, TOC/TIC/TOP, DEF, PM, RH, CJ, NPR, BVP, KKT | many | domain terms (Sauer initial-value line; method of characteristics; …)
- ADR | orch-forms/topology | untracked advisory-copy pattern (Nygard lineage)
- [DIR-*] | various | directive registry rows
- G-B, M1-M5 (contract), F_env | s15/rao | geometry-free bound; global-optimality contract
- SAKS, Poon-Martins | s22 | adaptive-KS alternatives declared-not-adopted
- X-SCANM replay probes, CERT_PLAY, cert_diag, val_diag | s21/s22 | certification instrumentation
- T2a, T1/T2 (loop-speed thresholds) | s17/s18 | production-gate thresholds — collision with theorem T1/T2, flag
- MC8 | s25bis | S-CERT meta-claim id (plan adherence)

Distinct token count (as enumerated above, counting each id in the lists): **231**.

NAMESPACE-COLLISION FINDING for the glossary (T2-bis(a)): the letters C, P, M, L, O, T, F, D each carry 2+ unrelated namespaces (e.g. M1 = speed lever AND global-optimality contract item; O5 = obligations-ledger row AND numpy user-decision; T2 = theorem AND loop-speed threshold; F4 = plan phase AND twin verdict branch). The glossary must be namespace-qualified or these will keep minting ambiguity.

---

## 3. Reconciliation

files in authoritative list: 37 — files accounted above: 37 (MEMORY.md + 16 standing-directive/preference + 4 continuity-bridge project + 12 session-chain + python-env + repo-sota + research-rao counted in their blocks; every list line appears literally as a heading or table row). Read integrally: 37. Classified-without-read: 0. Orphans: 0.

Unique-at-risk carriers (files with non-"none" UNIQUE-AT-RISK rows feeding the nothing-lost ledger): MEMORY.md, gate-pre-esecuzione, repo-sota-standard, gamma-variable-generality, periodic-wave-data-scope, thermo-tabulated-backend, moc-critical-independent-invariants, general-vision-nondivergence, sota-library-survey-directive, generality-nonhardcoded-procedures, agnostic-milestone-review-directive, self-improvement-at-convergence, claim-dual-proof-standard, roads-insertion-matrix-directive, scope-pins-frozen-thermally-perfect, never-postpone-resolvables, choice-adjudication-convergence, pipeline-sense-expert-review, orchestration-weight-sota, agentic-orchestration-forms, python-env-cantera, research-cycle-averaged-rao, topology-census-pins, generality-litmap-review + session-chain rows s14, s15, s17, s19, s21, s22, s24, s25bis (per-file items in the table) = **32 files** carry at least one enumerable unique-at-risk item (s18, s20, s23, s25, sspeed assessed low/mirrored).
