# INVENTORY — Segment 1: docs/ core (41 .md + 2 registry .yaml)
# S-ORDINE Phase 1 reader "seg1-docs-core", 2026-08-13
# Authoritative list: validation/sordine_raws_2026-08-13/seg1_docs.txt (43 files)
# Reconciliation: 43 files listed = 43 files accounted below. Discrepancy 0.

## COVERAGE DISCIPLINE (declared, honest)
- READ-INTEGRAL (3): docs/findings_registry.yaml (202 lines),
  docs/rde_nozzle_conditionals.md (137), docs/rde_nozzle_SCAFFOLD.md (216).
- CLASSIFIED-WITHOUT-INTEGRAL-READ (40), declared reason per the brief
  ("structure and status only; do NOT re-verify theory content"): every
  doc in this corpus carries a NORMATIVE STATUS BLOCK at its head
  (Status:/Registry:/Audit line convention since S8). For each of the 40,
  I read the full head status block (first 30 lines), ran a corpus-wide
  supersession grep (all SUPERSED* hits reviewed in context), mapped
  section structure (## headers) for the load-bearing files (PROGRESS,
  development_plan, SCAFFOLD, MASTER legend, claims_registry schema
  comment 1-31), and took wc -l for every file. Classification, authority
  and supersession state below derive from those reads, never invented.
  Theory/proof content is NOT summarized beyond what the status blocks
  themselves state.

## AUTHORITY ORDERING (of record, confirmed from the sources themselves)
1. M0 (rde_nozzle_MASTER.md) + D1-D7 win every conflict (M0 head; CLAUDE.md).
2. claims_registry.yaml = INDEX never content (SCAFFOLD §1 conflict rule);
   findings_registry.yaml = dedup authority for findings (R31).
3. conditionals.md (L4) = single statement location for C-D25U/C-MAJDA;
   remaining_conditionals.md = the verbatim SOURCE it transcribes.
4. development_plan.md (D6) = WORK index (F0-F6 spine ratified S21;
   A0-A7 retained as historical status ledger IN THE SAME FILE).
5. PROGRESS.md = living position (ORA/NEXT/BLOCCATO), never normative theory.
6. Historical notes (cycle_averaged_*, mathematical_foundations_*) carry
   supersession banners: consultable, never citable against M0.
7. roadmap_geno_rde.md: superseded IN SUBSTANCE by D6 ("Where this plan and
   the old roadmap differ, THIS plan wins", D6 head) but carries NO BANNER
   — hygiene finding, see FINDINGS below.

==============================================================================
## PER-FILE INVENTORY (43 rows; PATH / CLASS / ROLE / STATUS-AUTHORITY /
## PLAN-ANCHOR / UNIQUE-AT-RISK / REFS)

### Registries (2)

**docs/claims_registry.yaml** (1896 lines)
- CLASS: registry (theory-as-code index)
- ROLE: typed index of the theory corpus — 136 entries (id/kind/class/
  scope/statement/doc/proof/inherits/carrier/suffices_symbolic/falsifier/
  gamma + ondemand field with staleness link). Never carries content.
- STATUS-AUTHORITY: OF-RECORD (lint-enforced, suite group (xv))
- PLAN-ANCHOR: SCAFFOLD §2 / migration M-1 [F1/SCAFFOLD-M]; R5 discipline;
  C4 closure (S25) added the ondemand/staleness schema; X-SPDB scope rows.
- UNIQUE-AT-RISK: the live `inherits` heir index; per-carrier ondemand
  pass-dates (staleness links of record); falsifier one-liners per claim.
  These exist NOWHERE else in machine form.
- REFS: in — every doc cites claims by ID; out — doc#anchor paths to all
  D-docs and validation/ carriers; checked by tests/test_claims_lint.py.

**docs/findings_registry.yaml** (202 lines, READ-INTEGRAL)
- CLASS: registry (findings-as-code)
- ROLE: typed registry of findings/gaps/conditionals of record; 20 entries
  as of today (17 at S25-bis close + 3 landed since: derive-artifact
  staleness, cross-lowering floor group, val-diag twin). OPEN rows require
  owner+trigger; CLOSED require evidence; code-span dedup is the machine
  anti-re-mint rule.
- STATUS-AUTHORITY: OF-RECORD (lint group (xix), 4 seeded rejectors)
- PLAN-ANCHOR: census R31 (user directive 2026-08-12); the S-ORDINE
  session ABSORBS its first duty (full corpus seeding: audit 94 +
  gap-map 36/16/10 + choice ledger 45 + refuter/red-team) — declared in
  the file's own SEEDING STATUS comment.
- UNIQUE-AT-RISK: owner + trigger + magnitude-of-record strings for all
  20 findings (magnitudes cite advisories, but the OWNER/TRIGGER
  adjudications live only here); the demonstrator narrative (throat-panel
  re-mint case).
- REFS: in — S-ORDINE prompt, PROGRESS R31 row; out — source anchors into
  AUDIT_agnostic, ADVISORY_S24_sota_gapmap, ADVISORY_S25_pipeline_sense_
  CONVERGED, PROGRESS_2026-08-12_S25bis_speed, code spans in validation/.

### Superseded historical notes (2 — banners PRESENT and correct)

**docs/cycle_averaged_variational_nozzle.md** (776)
- CLASS: doc-theory (historical research note)
- ROLE: the ORIGINAL engineering formulation (T0-T4, averaged Rao system,
  novelty channels N1-N6, ladder) that seeded the program.
- STATUS-AUTHORITY: SUPERSEDED-BY-D1-D4 (dated banner 2026-07-16 at top,
  listing the known corrections: T1 = definition+conjecture; (**) -> (**');
  "Rao verbatim in 3-D" overclaim; §5.1b numbers re-derived inline via
  A0.3 examples/gamma_cycle_probe.py, eps* shift -0.56% not -1.9%;
  "Mo, Huang" conflation; T0 strengthened).
- PLAN-ANCHOR: CLAUDE.md canonical-reference list (historical note with
  supersession banner); memory research-cycle-averaged-rao. Not orphan:
  it is the named genealogy source of P-1 §1.
- UNIQUE-AT-RISK: none material — corrections were propagated to D4 §1
  and the carrier; the surviving unique content is genealogical prose.
- REFS: in — roadmap_geno_rde head, mathematical_foundations head, D1
  status block; out — D1-D4.

**docs/mathematical_foundations_rde_nozzle.md** (443)
- CLASS: doc-theory (historical research note)
- ROLE: original rigorous formalization (solution concepts, P1-P7,
  oracles O1-O5, SOTA toolbox map).
- STATUS-AUTHORITY: SUPERSEDED-BY-D1-D4 (dated banner 2026-07-16;
  corrections: P1 biconditional FALSE -> P1a/P1b in D3 §7; Giles-Pierce
  quasi-1D published; Dapogny 2023 DRO citation duty).
- PLAN-ANCHOR: same as above (historical note of record).
- UNIQUE-AT-RISK: none material (corrections live in D4 §2 / D3 §7).
- REFS: in — roadmap head; out — D1-D4.

### Deliverables D1-D8 + plan layer (10)

**docs/rde_nozzle_problem_book.md** (555)
- CLASS: doc-theory (deliverable D1)
- ROLE: frozen definitions, notation, objective functional + operating
  measure, design-interface formalization, hypothesis ledger (§9),
  PB-n problem rows.
- STATUS-AUTHORITY: OF-RECORD (supersedes the informal §1 definitions of
  both historical notes — declared in its status block).
- PLAN-ANCHOR: D6 canonical reading order; L1 layer of SCAFFOLD; (P) of
  D2.6 is defined downstream of this notation.
- UNIQUE-AT-RISK: frozen notation table; PB-n problem statements; D1 §9
  hypothesis ledger rows (the 17 rows adjudicated by [PAP-D9HL]).
- REFS: in — nearly every doc (notation "as in D1 §1"); out — D2/D3/D4.

**docs/rde_nozzle_literature_map.md** (675)
- CLASS: doc-survey (deliverable D2)
- ROLE: six-strand (b1-b6) web-verified literature map; executive gap
  table G1-G14 with query-bounded verdicts; per-gap nearest prior art.
- STATUS-AUTHORITY: OF-RECORD (with dated in-place corrections, e.g. the
  Harroun "near-perfect time-averaged expansion" MISQUOTE row corrected
  S24 per the 2026-08-11 choking census).
- PLAN-ANCHOR: D6 §3 publication stream (novelty defense of P-1);
  generality-litmap review directive; G5 gate context.
- UNIQUE-AT-RISK: the G1-G14 verdict table with NOT-FOUND(q) bounds and
  nearest-prior-art attributions — the program's novelty case lives here.
- REFS: in — D4, P-1 sections, M0; out — external literature, lit_b0bis.

**docs/rde_nozzle_theorem_ledger.md** (954)
- CLASS: doc-theory (deliverable D3)
- ROLE: formal statements with class tags (THEOREM/THEOREM*/SCHEMA/
  CONJECTURE/HEURISTIC/WEAKENED), verified proofs/counterexamples/open
  problems; §10quater rigor ledger; §11 falsifier index; S14 legend
  extension recorded.
- STATUS-AUTHORITY: OF-RECORD
- PLAN-ANCHOR: L2/L3 layers; source of P-1 rigor classes; [J-CT1] frame.
- UNIQUE-AT-RISK: the per-item class history and counterexamples (e.g.
  two-gamma counterexample), P1a/P1b corrected forms, §11 falsifier index.
- REFS: in — P-1/P-2 drafts, registry proof fields; out — D1/D2/D4.

**docs/rde_nozzle_claims_verdict.md** (256)
- CLASS: doc-audit (deliverable D4)
- ROLE: verdict on the internal notes + ordered open-problem list; b2
  gate resolution (zero hits C1-C3, Kraiko line characterized C4);
  bibliographic corrections of record (Rao TOP = ARS J. 30(6):561 1960;
  Rao 1961 = spike paper; Eq.[14] row later VERIFIED in-house — dated
  in-doc supersession marker added S15).
- STATUS-AUTHORITY: OF-RECORD (contains internal dated supersession
  markers — the corpus convention: original preserved, marker dated).
- PLAN-ANCHOR: D6 §3 (novelty contingencies for P-1); G5 gate residue
  (Kraiko 1979 human pass) is named here.
- UNIQUE-AT-RISK: b2-strand verdicts and the bibliographic-correction
  ledger; the supersession-route decision for the historical notes.
- REFS: in — P-1 sections, D2; out — historical notes, literature.

**docs/rde_nozzle_general_scheme_panel.md** (125)
- CLASS: doc-panel (deliverable D5)
- ROLE: 16-agent adversarial panel synthesis — the FINAL SCHEME steps
  0-8 (modeling ledger, mode census, tier RE engine, KKT solve, ...)
  each with rigor class/cost/falsifier; 3 verification searches.
- STATUS-AUTHORITY: OF-RECORD
- PLAN-ANCHOR: D6 integrates it ("D5 scheme + D5-Annex-A stages"); the
  tier ladder and REQ-NONSTALL genealogy trace here.
- UNIQUE-AT-RISK: the per-step scheme table with cost estimates and
  the panel's verification-search links.
- REFS: in — D6, D7; out — external SOTA links.

**docs/rde_nozzle_development_plan.md** (1120)
- CLASS: doc-plan (deliverable D6 — THE work index)
- ROLE: phase plan. STRUCTURE (load-bearing for de-entropy): §0-pre =
  PLAN v3 OF RECORD (F0-F6 spine, ratified 2026-08-11 S21, user
  decision; SUPERSEDES A0-A7 as WORK index); §2 = Phases A0-A7 RETAINED
  as historical/status ledger; §3 publication stream (P-1/P-2, RK-A);
  §4 SOTA tool matrix; §5 gates G0-G6 + kill criteria; §6 90-days with
  STATUS REFRESH layers; §7 risk register; ANNEX B input taxonomy.
  Item 9 carries the brick-2 duty bundle + waiver annotations; line 128
  carries a dated in-place SUPERSEDED marker (2026-08-12 dispatch).
- STATUS-AUTHORITY: OF-RECORD (two-spine layering INTERNAL to the file:
  F0-F6 live, A0-A7 historical — a named entropy pattern but explicitly
  governed by the §0-pre ratification note)
- PLAN-ANCHOR: it IS the plan (R1 anchor target for every commit tag).
- UNIQUE-AT-RISK: F0-F6 phase definitions/exit gates; gate table G0-G6;
  risk register (RK-A scooping risk); ANNEX B taxonomy; the
  ratification+amendment history.
- REFS: in — CLAUDE.md, PROGRESS, every commit tag; out — roadmap
  (amends), D5, ADVISORY_plan_v3_panel (its convergence source).

**docs/rde_nozzle_pipeline_audit.md** (162)
- CLASS: doc-audit (deliverable D7)
- ROLE: per-step triple verdict (SOTA?/GENERAL?/CORRECT?) over the
  assembled pipeline; PASS/PASS-D with declared residues R1-R8; E9
  dated correction rows (S14).
- STATUS-AUTHORITY: OF-RECORD
- PLAN-ANCHOR: D6 gates context; PAN-S14 corrections landed here.
- UNIQUE-AT-RISK: the R1-R8 residue register; per-step SOTA adjudication.
- REFS: in — D8 panel, PROGRESS; out — D2/D3/D5.

**docs/rde_nozzle_panel_2026-07-22.md** (373)
- CLASS: doc-panel (deliverable D8, [PAN-S14])
- ROLE: four-round convergence panel of record: 16 record-driving
  findings table (each with fix locus), the two standing structural
  criticisms (C-D25U-c concentration; falsifier-vs-flatterer allocation
  bias), verdict summary, §8 residue.
- STATUS-AUTHORITY: OF-RECORD (verdicts S14 not re-litigable)
- PLAN-ANCHOR: census/memory s14-panel-verdict-canonical-loop; the E9*
  correction wave and legend extensions all trace here.
- UNIQUE-AT-RISK: the 16-finding table with per-finding fix loci; the
  canonical multi-agent loop form genealogy.
- REFS: in — pipeline_audit, SCAFFOLD §5 note, conditionals component
  split; out — PROGRESS S14 log.

**docs/roadmap_geno_rde.md** (358)
- CLASS: doc-plan (historical program roadmap, WP0-WP8/G0-G4)
- ROLE: the pre-D6 execution roadmap (who builds what, kill criteria);
  presents itself as "third document of the set" with the two
  historical notes as companions.
- STATUS-AUTHORITY: SUPERSEDED-BY-D6 IN SUBSTANCE — but carries NO
  supersession banner. D6's status block states "Integrates and AMENDS
  docs/roadmap_geno_rde.md ... Where this plan and the old roadmap
  differ, THIS plan wins." FINDING (hygiene, loud): this file SHOULD
  carry the dated banner the two historical notes have; today a cold
  reader can land here and read WP-phases as live. Also its companion
  list cites the two superseded notes without noting their banners.
- PLAN-ANCHOR: D6 predecessor (historical layer). Not orphan.
- UNIQUE-AT-RISK: WP0-WP8 structure and original kill criteria (the
  only place the pre-D6 work breakdown lives); tool-goal statement
  (certificate/error-bar/robustness-flags shipping list).
- REFS: in — D6 (amends it); out — the two historical notes.

**docs/rde_nozzle_PROGRESS.md** (2498)
- CLASS: doc-progress (living state — THE named entropy source)
- ROLE: ORA/NEXT/BLOCCATO/LOG + census. R3-mandated update every close.
- STATUS-AUTHORITY: OF-RECORD (living)
- PLAN-ANCHOR: CLAUDE.md R2/R3; census rows R1-R33 live here.
- BLOCK STRUCTURE (measured, for the slimming plan — the growth is
  BIDIRECTIONAL accretion, not a log-append):
  - L1-9: header + opening protocol (stable).
  - L10-32: ORA = ONE ~23-line ## heading (S25-bis synthesis). Each
    session REWRITES ORA (this part does not grow).
  - L33-294: bullet ledger of the last ~2 sessions ([S25-bis]/[S25]
    blocks: final speed counter, M6 adjudication, rigor data, NEXT
    chain of record S-ORDINE(R32) -> S-CERT(R33) -> F2). Grows by
    prepend, older bullets pushed down.
  - L295-372: CENSIMENTO DELTA S25-bis (INCREMENTAL sweep — only rows
    touched: R30 CONSUMATA, R28, R29, R31, R25 + new-finding channel).
  - L373-491: CENSIMENTO DELTA S25 (same incremental pattern: R3c,
    R7c, R18/R21, R22, R23, R25, R26, R28, R29, R30, R31).
  - L492-~560: CENSIMENTO POSTICIPI — STATO FINALE S24 = the one-time
    CONSOLIDATED table R1-R27 (one row per item with state ORA/SCHED/
    GATED/LOCK/CHIUSA). => THE CENSUS PATTERN: one consolidated
    snapshot (S24) + per-session DELTA BLOCKS stacked above it; a
    reader must fold >=3 blocks to know a row's current state. This is
    exactly the entropy mechanism named in the S-ORDINE prompt (2b);
    the T2(iv) consolidation target ("tabella censimento CONSOLIDATA
    una-riga-per-item") maps 1:1 onto folding L295-560.
  - L~560-1918: reverse-chronological per-session summary blocks
    (S22/F1 counter, S-GAUNTLET absorbed, S21/F0, S20..., S17/S18
    brick-2, S15/S16 RIGOR tranches, S14 panel, S12-S13...) — each a
    frozen mini-ORA of its day. Monotone growth by insertion.
  - L1919-2149: FIVE STALE NEXT BLOCKS retained verbatim (S17 close,
    S16 close, S15 x2, S14) — superseded in fact by the current NEXT
    chain in ORA but carrying NO supersession marker each. Hygiene
    finding: candidates for PROGRESS_ARCHIVE with banner (T2(iv)).
  - L2150-2182: BLOCCATO / GATE APERTI (live; 8 rows incl. filelock).
  - L2183-2498: LOG SESSIONI — but ONLY S13 and earlier live here;
    from S14 on, session logs moved to validation/PROGRESS_<date>_S*.md
    files (27 of them, segment 5). The in-file LOG is a fossil tail.
- UNIQUE-AT-RISK: census row states R1-R33 (the ONLY consolidated
  record of postponements with owner/trigger); BLOCCATO 1-8 decisions
  pending; the NEXT chain of record (S-ORDINE -> S-CERT -> F2 with F2
  session counter 0/6); early-session LOG entries S1-S13 (not
  duplicated in validation/ logs, which start S14-era); F1 counter,
  freeze dates, per-session commit hashes in mid-file blocks.
- REFS: in — CLAUDE.md R2/R3, every session open; out — validation/
  PROGRESS_* logs, advisories, D6, registries.

### SCAFFOLD + conditionals layer (3)

**docs/rde_nozzle_SCAFFOLD.md** (216, READ-INTEGRAL)
- CLASS: doc-architecture
- ROLE: corpus architecture of record: six layers L0-L6 + registry;
  claim schema; maintainer contract (6 rules); migration plan M-1..M-5
  (executed S9); §5 payoff with S14 dated supersession note.
- STATUS-AUTHORITY: OF-RECORD
- PLAN-ANCHOR: [F1/SCAFFOLD]; DIRECT PRECEDENT for S-ORDINE — this is
  the in-corpus prior art for "de-entropy via typed registry + layered
  reading order + lint". The S-ORDINE target structure should extend,
  not duplicate, L0-L6.
- UNIQUE-AT-RISK: layer definitions L0-L6; maintainer contract; the §2
  seed inventory table (historical); conflict rule text.
- REFS: in — claims_registry head, conditionals head, PROGRESS opening
  protocol; out — registry, L4 ledger, D6.

**docs/rde_nozzle_conditionals.md** (137, READ-INTEGRAL)
- CLASS: doc-ledger (L4)
- ROLE: THE single statement location of the two analytic conditionals
  C-D25U (component split -a/-b/-c; dischargers U1-U5 with dated status:
  U1 S15, U2 S15, U3/U4 S16, U5 MISSING research-grade) and C-MAJDA
  (with the S16 U3-H1 sharpening s_L = 1.8685 and the a-contraction
  named route); heirs by ID; reading rule.
- STATUS-AUTHORITY: OF-RECORD (transcription-only content rule)
- PLAN-ANCHOR: SCAFFOLD L4 / migration M-4; heirs lint (xv).
- UNIQUE-AT-RISK: the dated discharger-status notes and the in-class
  supersession markers (the "WHAT REMAINS" correction chain) — the
  authoritative current state of both conditionals is readable ONLY here.
- REFS: in — every THEOREM* via inherits; out — remaining_conditionals
  §1 (verbatim source), G12_S1 §2, D25U docs, acontraction_attack.

**docs/rde_nozzle_remaining_conditionals.md** (240)
- CLASS: doc-theory (proof-architecture source)
- ROLE: pristine statements + proof architectures for the last four
  function-space gaps (D2.5-U §1, P4-Fredholm, Lemma-B mesh limit §3,
  second order); carries the S15 h_min AMENDMENT OF RECORD and the S14
  cost re-pricing supersession for component -c.
- STATUS-AUTHORITY: OF-RECORD (verbatim source that L4 transcribes)
- PLAN-ANCHOR: [F1/D25U + F1/P4F + F1/LBML + F1/SO]; C-D25U source.
- UNIQUE-AT-RISK: the full proof architectures with constant
  dependencies (only stated here); dated amendment chain.
- REFS: in — conditionals.md, D25U_U1/U3U4, LBML; out — M0 D2.5.

### Rigor-attack documents of record (13)

(Homogeneous class: each = "RIGOR ATTACK OF RECORD" with status block
declaring registry ID, carrier, audit line [Class|Falsifier|Carrier|
Gamma], and VERDICT UP FRONT. All OF-RECORD, all plan-anchored to the
rigor campaigns of census record — none orphan. Unique-at-risk = the
full proof/derivation text + the verdict numbers named below; the
registry indexes them but never carries the content.)

**docs/rde_nozzle_G12_S1.md** (189) — attack on gap G12 (multi-D shape
  derivative across shocks) via x-as-time; G12-L1/G12-L2 bricks.
  Anchor [F1/G12-S1]; registry [T-G12S1], carrier X-G12. At-risk: the
  lemma proofs + the reduction argument.
**docs/rde_nozzle_N6_swirl.md** (156) — N6 swirl structure theorems +
  free-vortex extension + sharp negative. Anchor [F1/N6-S1]; [T-N6-1/2/3],
  X-N6 (16/16). At-risk: machine-verified identity list (a)(b)... and
  the sharp-negative statement.
**docs/rde_nozzle_S1_uniqueness.md** (75) — S1-internal uniqueness
  statement + proof architecture. Anchor [F1/S1-uniq]; [S-S1U] SCHEMA
  with proven bricks. At-risk: the assembly-step naming.
**docs/rde_nozzle_T7_P7_functionspace.md** (166) — T7 first-order
  system + P7 existence in the working class. Anchor [F1/T7-FS + F1/P7];
  [T-T7FS]/[T-P7S1] THEOREM* inheriting C-D25U. At-risk: proof text.
**docs/rde_nozzle_P3_multipliers.md** (154) — measurable averaged
  multipliers lambda2 in L^inf(dmu); THEOREM* in shock-free S1 class.
  Anchor [F1/P3]; [T-P3]. At-risk: proof + the dated SINGLE-WALL SCOPE
  NOTE (multi-wall owed to a dedicated session — an OPEN duty recorded
  only here and in D8 §8 residue).
**docs/rde_nozzle_cauchy_bvp_transfer.md** (290) — Cauchy->steady-BVP
  transfer, relative entropy in x. Anchor S15 [RIGOR/A]; [T-XSON]/
  [T-XWALL]/[S-XCONV]/[T-XWS]/[C-XBVP], carrier X-XBVP. At-risk: proof
  chain + declared novelty-status paragraph (wall-lemma sweep IOU).
**docs/rde_nozzle_D25U_U1.md** (277) — U1 smooth-region semiglobal
  estimates; cost-claim CONFIRMED with the h_min DISCOVERY. Anchor S15
  [RIGOR/A]; [S-D25U-U1]. At-risk: the estimates + the h_min discovery
  narrative (amendment executed at L4/ledger, but derivation only here).
**docs/rde_nozzle_D25U_U3U4.md** (437) — U3+U4 fronts and composition;
  C-D25U -a complete at class level; clause inventory c1-c4; U3-H1.
  Anchor S16 [RIGOR/A]; [S-D25U-U34], carrier X-U3BD. At-risk: the
  five-constant certificate derivation + priced clauses.
**docs/rde_nozzle_acontraction_attack.md** (227) — a-contraction /
  shifted relative entropy route to C-MAJDA at weak level; instance-
  feasible weight window r ~ [3.2, 47], best ~6.8; bricks B1-B3 named.
  Anchor S16 T2 [RIGOR/A]; [S-ACFR], probe X-ACFR. At-risk: §3
  balance-set reduction + the probe-finding table (B1 supersedes note).
**docs/rde_nozzle_GB_ergodic.md** (201) — ergodic G-B lemma (PP-2
  missing lemma written); ceiling transfers to J_exact^+; OP-0 sonic
  cap structural finding. Anchor S16 T4 [RIGOR/A]; [S-GBE], X-GBE.
  At-risk: E1-E5 hypotheses + the two structural findings.
**docs/rde_nozzle_LBML.md** (201) — Lemma-B mesh limit as five-step
  Lax-equivalence; no new carrier (O3 oracles are the falsifiers);
  clause LB-c2 (fixed march topology). Anchor S16 T4b [RIGOR/A];
  [S-LBML]. At-risk: the five-step argument + LB-c2.
**docs/rde_nozzle_side_load.md** (201) — rotating side-load m=1
  selection rule; THEOREM, closure-agnostic. Anchor S15 [RIGOR/A];
  [T-SLRW], X-SLRW. At-risk: full proof + disposition-of-record
  (secondary output vs c-slot).
**docs/rde_nozzle_T3QS.md** (122) — quasi-steady protection of the
  collapse class (first-order sweep cancellation on ray families).
  Anchor [F4-prep/T3QS], R4 back-propagation of the 2026-07-20/21
  review; [T-T3QS], X-T3QS. At-risk: theorem statement + jump-localized
  residue characterization.

### Governance / campaign documents (5)

**docs/rde_nozzle_G0_decision.md** (249)
- CLASS: doc-decision (gate record)
- ROLE: formal G0 stack decision — JAX primary (custom_vjp/jvp, implicit
  rules), Julia+Enzyme declared fallback, GENO-Fortran independent
  reference; opens Phase A1; armed loop-speed falsifier.
- STATUS-AUTHORITY: OF-RECORD ([F2/G0], S10; G0/T2 review CONSUMED S25
  with no flip — decision stands)
- PLAN-ANCHOR: gate G0 of D6 §5; DIR-G0; carrier X-GENOXC.
- UNIQUE-AT-RISK: the criteria/evidence/verdict table and fallback
  rationale (only decision record for the stack choice).
- REFS: in — brick2_kickoff, PROGRESS; out — D6 §5, registry DIR-G0.

**docs/rde_nozzle_brick2_kickoff.md** (571)
- CLASS: doc-kickoff (binding duty record)
- ROLE: the four binding kickoff duties of D6 item 9 before brick-2
  optimization runs + S16 addition (EOS G>0 audit, channel c4); each
  duty: normative content + EXECUTED status (carrier + verdict).
  DIR-RKG policy of record (§1: fixed topology in trust region,
  re-record on acceptance, kink detection).
- STATUS-AUTHORITY: OF-RECORD (brick 2 CLOSED S18 — duties CONSUMED but
  the normative policies DIR-RKG etc. remain live and are cited from
  the engine layer)
- PLAN-ANCHOR: D6 item 9; [F2/A1]; memories s17-brick2-kickoff /
  s18-brick2-closed.
- UNIQUE-AT-RISK: the DIR-RKG normative text (schedule = march topology
  semantics) — load-bearing for every gradient claim; duty execution
  statuses.
- REFS: in — engine docstrings, PROGRESS S17/S18; out — [S-D25U-U34] D2,
  [S-LBML] LB-c2, [PAP-D9HL] §4.2, DIR-THERMOTAB, X-A1IM.

**docs/rde_nozzle_global_maximum_dossier.md** (189)
- CLASS: doc-dossier (census + screening, OPENED not closed)
- ROLE: census/first-screening of certified global-search routes on the
  finite-dim class; route cards with cost/hypotheses/preliminary
  verdicts; rule: NO route adopted without a carrier; first bricks §6.
- STATUS-AUTHORITY: OF-RECORD (open dossier)
- PLAN-ANCHOR: (P)(iv) of M0 D2.6 (delta -> 0 program); [RIGOR/C] S15;
  registry [PAP-GMAX].
- UNIQUE-AT-RISK: the route cards + named first bricks (the only
  globality-program planning record).
- REFS: in — PROGRESS R-rows on globality; out — M0 D2.6, A1 engine.

**docs/rde_nozzle_hypothesis_ledger.md** (179)
- CLASS: doc-ledger (governance, D9 candidate)
- ROLE: hypothesis-minimization ledger passes 1+2 over D1 §9's 17 rows
  + 7 registry conditionals; verdict vocabulary DISCHARGED/WEAKENED/
  NECESSARY/PRICED; pass-1 totals 0/6/5/13, pass-2 dated totals (3
  DISCHARGED...). Zero rows unadjudicated.
- STATUS-AUTHORITY: OF-RECORD; registry [PAP-D9HL]
- PLAN-ANCHOR: [RIGOR/B] S15/S16 mandate ("mandatory verdict per
  standing hypothesis").
- UNIQUE-AT-RISK: the per-row verdict table with grounds citations —
  sole consolidated hypothesis-status record.
- REFS: in — brick2_kickoff §4.2 channel c4, PROGRESS; out — D1 §9,
  registry C-*.

**docs/rde_nozzle_lit_b0bis.md** (246)
- CLASS: doc-survey (in-house corpus evaluation)
- ROLE: five-agent primary-source pass over GENO/literature vs the
  averaged variational theory; headline verdict V1 novelty CLEAN on the
  whole in-house corpus; per-paper nearest-non-threat quotes; oracle
  candidates O-Ob1..7.
- STATUS-AUTHORITY: OF-RECORD (deepens D2 §b0, supersedes nothing —
  declared)
- PLAN-ANCHOR: [F1/D2-b0bis] user directive; feeds T2(vi)
  literature_registry.yaml (segment 7's deliverable) — the anchors
  "where was this paper analyzed" for the GENO root partially live here.
- UNIQUE-AT-RISK: per-paper evaluation verdicts + the pointer that full
  agent reports live in validation/PROGRESS_2026-07-16_rigore_PA.md
  step 13 (cross-segment dependency for the literature registry).
- REFS: in — D2, P-1 citations; out — GENO/literature PDFs, session log.

### Paper drafts P-1 / P-2 (7)

(Homogeneous class doc-paper-draft; all OF-RECORD drafts; plan anchor =
D6 §3 publication stream, submission gated M1+G5 — the writing is not.
Unique-at-risk for all: the paper prose itself + per-subsection audit
lines [Class|Falsifier|Carrier|Gamma] + citation-depth annotations;
sources declared as M0/D2/D3/D4 with "in conflict, M0 wins".)

**docs/rde_nozzle_P1_skeleton.md** (399) — P-1 skeleton of record; JPP
  target; tracks which sections have full text (all body complete;
  appendices A1-A7 remain at skeleton level — the OPEN remainder).
  Registry [PAP-P1S1389] for §1/3/8/9. At-risk: acceptance rules
  (a)-(e), section-status ledger, class-refresh declarations.
**docs/rde_nozzle_P1_sections_2_4.md** (504) — §2+§4 full text (S8);
  naming guard T3-A/B/C vs P-2 Lemma A/B; claim-map cross-check.
**docs/rde_nozzle_P1_sections_5_7.md** (501) — §5-§7 full text (S10);
  class refresh SCHEMA -> THEOREM* declared; purge delta -4.4..-7.9%.
**docs/rde_nozzle_P1_sections_1_3_8_9.md** (397) — §1/§3/§8/§9 full
  text (S11); var-gamma genealogy; Rao 1958 IAC abstract-verified-only
  citation discipline; §3.2 N6 theorem-grade refresh.
**docs/rde_nozzle_P2_outline.md** (379) — P-2 outline + the P-2 FREEZE
  OF RECORD block (dated 2026-08-11, fired by ISS-5 rule at F1 close):
  numeric half frozen at fallback-B quality — f2 drift 9.4809e-03 vs
  derived band 1.8696e-02, drift-grows-with-mesh honest datum,
  two-knob convergence statement. At-risk: THE freeze numbers block
  (C1 conditional context; unique consolidated statement).
**docs/rde_nozzle_P2_lemmaA.md** (610) — P-2 §3 draft: term-by-term
  Rao/Kraiko == continuous adjoint identification, equation-numbered
  against the page-verified corpus (RAO.pdf in-house). At-risk: the
  full derivation + Zucrow-Hoffman characteristic-naming trap note.
**docs/rde_nozzle_P2_lemmaB.md** (374) — P-2 §4 draft: reverse-AD of
  shock-fitted MOC march IS the discrete adjoint sweep; demonstrator
  g0_spike_jax_moc.py 52/52. At-risk: the finite-dimensional argument
  + disambiguations.

### The master (1)

**docs/rde_nozzle_MASTER.md** (2126)
- CLASS: doc-theory (M0 — master of record)
- ROLE: self-contained thesis-grade reference: Part I idea, Part II
  definitions/contracts (D2.x incl. (P) of D2.6), Part III proofs in
  full, Part V ladder/tiers, Part VI implementation formulation +
  VI.4bis pins + S21 registration block (EQ-v2 of record at L1653,
  superseding the earlier statement — dated in-place), Part VII
  deliverable map. Rigor legend + S14 legend extension at head.
  Contains dated in-place supersessions (e.g. L1560 citation-status
  row SUPERSEDED 2026-08-12 S24 R4).
- STATUS-AUTHORITY: OF-RECORD (top of the conflict order with D1-D7)
- PLAN-ANCHOR: CLAUDE.md R2 mandatory reading; L0-L3+L5 of SCAFFOLD
  map onto its parts; R4 back-propagation target of every session.
- UNIQUE-AT-RISK: the FULL PROOFS of the core theorems (only location,
  by SCAFFOLD L3 design); the VI.4bis algorithmic pins; EQ-v2
  statement of record; Part VII map. Highest-value single file in the
  segment.
- REFS: in — everything; out — D1-D7, registry IDs, attack docs.

==============================================================================
## SEGMENT-LEVEL FINDINGS (for Phase 2/judge; loud, none silently absorbed)

F-SEG1-1 (hygiene, banner gap): docs/roadmap_geno_rde.md is superseded
  in substance by D6 (D6's own status block says so) but carries NO
  supersession banner, unlike the two historical notes. Proposed:
  dated banner pointing to D6 (R4-compliant, no deletion).
F-SEG1-2 (PROGRESS entropy, characterized): the census lives as ONE
  consolidated S24 snapshot + TWO stacked delta blocks (S25, S25-bis)
  + new-rows-in-ORA; current state of any R-row requires folding >= 3
  blocks. Five stale NEXT blocks (L1919-2149) and a fossil LOG tail
  (S13 and earlier only; later logs live in validation/) are retained
  unmarked. Maps 1:1 to T2(iv) PROGRESS-slim + PROGRESS_ARCHIVE.
F-SEG1-3 (precedent, positive): SCAFFOLD is the in-corpus prior art
  for exactly the S-ORDINE operation (typed registry + layers + lint +
  migration-with-acceptance). The converged target structure should
  EXTEND L0-L6 (add validation/-layer + literature + glossary), not
  invent a parallel taxonomy — else two competing architectures = new
  entropy.
F-SEG1-4 (supersession convention, works): the corpus-wide convention
  "original text preserved + dated in-place supersession marker" is
  applied consistently INSIDE docs (D4 §3bis row, D6 L128, M0 L1560/
  L1653, SCAFFOLD §5, conditionals, remaining_conditionals). The
  convention is prose-only (grep-able but not linted); a lint that
  every "SUPERSEDED" marker carries a date + pointer is a cheap T2-bis
  extension.
F-SEG1-5 (cross-segment dependency): lit_b0bis declares its full
  agent reports live in validation/PROGRESS_2026-07-16_rigore_PA.md
  (segment 5) — the literature registry (T2(vi)) must anchor GENO-root
  paper analyses through BOTH files.
F-SEG1-6 (orphans): ZERO orphan candidates in this segment — all 43
  files carry a nameable plan need (phase tag, census row, registry
  ID, gate, or standing directive) in their own status blocks. The
  segment is well-anchored; the entropy here is layering/growth, not
  orphanhood.

==============================================================================
## NOTHING-LOST LEDGER FEED (files with enumerable unique-at-risk content)

39 of 43 files carry unique-at-risk content (see per-file rows). The 4
with "none material": cycle_averaged_variational_nozzle.md,
mathematical_foundations_rde_nozzle.md (corrections propagated to D4/D3;
remaining uniqueness is genealogical prose kept under banner), plus none
others — recount: 41 files carry unique content; only the 2 historical
notes are none-material. FINAL: 41 at-risk carriers / 2 none-material.
Highest-concentration items (single-location, verdict-bearing):
 1. claims_registry ondemand pass-dates + inherits index (machine state).
 2. findings_registry owner/trigger adjudications (20 rows).
 3. PROGRESS census R1-R33 states + BLOCCATO 1-8 + NEXT chain + S1-S13
    early LOG entries.
 4. conditionals.md dated discharger-status chain (C-D25U/C-MAJDA
    current state).
 5. P2_outline FREEZE block numbers (f2 9.4809e-03 / band 1.8696e-02).
 6. M0 full proofs + VI.4bis pins + EQ-v2.
 7. D2 G1-G14 novelty verdict table; D4 bibliographic corrections.
 8. D8 16-finding table; D7 R1-R8 residues; hypothesis_ledger verdicts.
 9. Attack docs: each proof text + verdict numbers (s_L 1.8685; r window
    [3.2,47]; h_min amendment; -82% GAP-5 twin lives in findings_registry).
10. G0 decision evidence table; brick2 DIR-RKG normative semantics.

==============================================================================
## CODENAME TOKENS COLLECTED (feeds T2-bis glossary; token | seen | meaning)

Census/rules: R1-R6 | CLAUDE.md | plan-adherence rules; R1-R33 | PROGRESS
census | postponement/census rows (R28 numeric-lint hole, R29 pipeline-
sense, R30 S25-bis, R31 findings-as-code, R32 S-ORDINE, R33 S-CERT).
Gates: G0-G6 | D6 §5 | plan gates (G0 stack DECIDED; G1 oracles absolute;
G5 Kraiko human pass blocks submission).
Gaps (D2 table): G1-G14 | literature_map §0 | candidate-novelty gaps
(G12 = multi-D shape derivative with shocks; N6 = swirl transfer).
GAP-<n>: GAP-1, GAP-5 (natural-BC lip bias, twin -82%), GAP-18, GAP-27,
GAP-29 (underived factors; 1 flip NEWTON_TOL_FACTOR), GAP-30 (val-diag
starvation twin) | findings_registry/PROGRESS | gap-map rows.
Conditionals: C-D25U (-a/-b/-c), C-MAJDA, C-HT4, C-IGMIX, C-O33, C-P4RZ,
C-XBVP, C-EQV2 | conditionals.md/registry | analytic + closure
conditionals. C-A | thermotab | edge-stencil finding row. C1-C45 |
choice ledger annex | adjudicated choices. C1-C8 | AUDIT clusters.
Theorem/schema IDs: T-TH0, T-O1, T-O2, T-T0, T-NSW, T-T3, T-T3-CE, T-T4,
T-GB, T-OP11e, T-LEMA-CL, T-LEMA-iv, T-A2, T-A3, T-LEMB, T-P3, T-G12S1,
T-N6-1/2/3, T-N6-5F, T-T7FS, T-P7S1, T-SLRW, T-XSON, T-XWALL, T-XWS,
T-U2RG, T-T3QS, T-EQBR, T-T7RED, T-LBML, T-T3-MAP | SCAFFOLD §2 seed +
attack docs | registry theorem IDs. S-S1U, S-5F, S-P4F, S-LBML, S-ACFR,
S-GBE, S-BLITE, S-XCONV, S-D25U-U1, S-D25U-U34 | attack docs | schema/
attack registry IDs. D-P, D-CONTRACT, D-S1 | SCAFFOLD | definitions.
J-CT1, J-OP11 | SCAFFOLD/D3 | conjectures.
Carriers [X-*]: X-PA1, X-G12, X-N6, X-5F, X-G0, X-GBE, X-ACFR, X-XBVP,
X-U3BD, X-SLRW, X-T3QS, X-A1IM, X-GENOXC, X-TOCV, X-O32, X-O33B, X-IVXC,
X-MGOV, X-SPDB, X-CDKAT, X-TBAK, X-THC1, X-SCANM, X-LSG0, X-U2RG,
X-DEFTW, X-T3SI-conv | registry/attack docs/PROGRESS | executable
carriers in validation/.
Oracles: O1-O5 | mathematical_foundations/D3 | program oracles; O3.1/
O3.2/O3.3 | gradient exactness oracles (dot-product/order/term-match);
O-G2, O-RAOPLUG, O-Ob1..7 | SCAFFOLD seed | literature oracles.
Paper/pubs: P-1 (JPP paper), P-2 (bridge paper), P1-P7 (math
foundations problems), P1a/P1b (corrected biconditional), PB-2/PB-3
(problem-book rows), PP-2 (S14 panel finding, discharged by S-GBE),
PAP-GMAX, PAP-D9HL, PAP-P1S1389, PAP-RIM | registry doc IDs.
P-TRFLOOR, P-FLIPMAT | PROGRESS/findings | conditional rows.
Directives: DIR-G0, DIR-RKG, DIR-CITE, DIR-THERMOTAB, DIR-* | decision/
kickoff docs | standing directives. REQ-NONSTALL | plan v3 | optimizer
must never stall on incomputable field. EQ-v2 | M0 Part VI | DEF-
equivalence statement of record.
Speed program: M0-M6 (M-CHAIN levers; M5a/M5c per-column executor; M6
vmap-Hessian gate-rejected), M-D/M-E (stop-check measures), H3/H4 (cap
protection levers), H1-H6 (EQ-v2 hypotheses; also T3 H1-H4) | PROGRESS
S25/S25-bis. A1_COLEXEC, A1_VMAP_HESS, A1_FUSED_CERT, A1_PLAN_ARGS |
findings row structure:monolithic-driver | arbitration env-flags
(registry due at T2-bis(b)). K_RICH, K_NEWT, NEWTON_TOL_FACTOR, C_FLOOR,
C_OPS | GAP-29 | engine constants. NTF | PROGRESS | NEWTON_TOL_FACTOR
derivation duty. KAT | memory/S23 | GENO known-answer tests. m5cgate/
m6gate/h3gate/m12gate | PROGRESS | speed-program gates.
Phases: F0-F6 (+F1b, F2a, F4b, F5a; F-SERVICE tag) | D6 §0-pre | work
spine of record; A0-A7 | D6 §2 | historical spine; WP0-WP8 | roadmap |
pre-D6 breakdown. L0-L6 | SCAFFOLD | corpus layers. LB-c2 | LBML |
fixed-march-topology clause. U1-U5 | conditionals | C-D25U dischargers;
U3-H1, U3-L1 | D25U_U3U4 | Lopatinskii scalar condition/floor lemma.
Panel/session: PAN-S14, E8, E9a-E9r | D8/pipeline_audit | panel finding
+ correction wave; EAP | M0 remarks; S-H | Stechmann-Heister-Harroun
model; N-SW | axial spacelikeness lemma; N1-N6 | novelty channels;
b0-b6 | D2 survey strands; b2 | novelty search strand. RK-A, RK-G | D6
risk register / kickoff policy. ISS-5 | P2_outline freeze rule.
OBJ-DOM, G1-DISC | findings owners | F2-entry adjudication rows.
Q3, Q11 | pipeline-sense review items. OP-0 | sonic cap. T0-T7 |
theory theorems (T0 steadification ... T7 averaged system); T2a |
production gate; T3-QS | quasi-steady protection. S1 | solution class.
D1-D8, D2.1-D2.6, D2.5-U | deliverables + definition sections. B1-B3 |
acontraction bricks (B1 interval certificate supersedes probe); B1/B2 |
also rungs in D6 §5 context (collision noted for glossary).
G12-L1/G12-L2 | G12_S1 | bricks. R-G12.1/R-G12.2, R-P3.1, R-T7.1,
R-P7.1, R-U | remaining_conditionals | residue IDs. LIP_shocked |
D25U_U3U4 | explicit Lipschitz certificate constant.
(Distinct tokens collected: 214.)

==============================================================================
## RECONCILIATION
Files in seg1_docs.txt: 43. Rows above: 2 registries + 2 superseded
notes + 10 deliverable/plan-layer + 3 scaffold/conditionals + 13 attack
+ 5 governance/campaign + 7 paper drafts + 1 master = 43. Discrepancy 0.
