# LANDING BRIEF — LAND-2: registries + glossary — Blocco 2, S-FOUNDATIONS-C

Files you may edit: `docs/findings_registry.yaml`, `docs/claims_registry.yaml`,
`docs/choice_ledger.yaml`, `docs/glossary.yaml`, `docs/rde_nozzle_hypothesis_ledger.md`
(if that is the hypothesis carrier — verify its role first), `docs/literature_registry.yaml`.
NO other files. Discipline: match each file's existing row schema EXACTLY
(read 2-3 existing rows first); dedup ALWAYS (grep before minting — cite,
never re-mint; the anti-re-mint rule is machine-enforced); zero
inflation: every row's class/status at the evidence actually held; run
`python` lint scripts if present for families xv/xix (find them via
docs/rde_nozzle_SCAFFOLD.md §6 or tools/ — report PASS/FAIL, repair your
own rows until green).

Authorities: VERDICT_phaseD_proofs1.md §4/§5(ii), VERDICT_contract_and_L4R1.md
C-4 + Part A (ii)/(iv), VERDICT_r2pass.md §4, VERDICT_escalation.md §6,
VERDICT_confirm.md (all under validation/sfoundations_raws_2026-08-13/ +
r2pass/), DISPATCH_swirl5f.md + swirl5f_FINAL_report.md §2/§7 (under
validation/swirl5f_panel_2026-08-19/; PANEL grades are NOT record grades
— use ONLY the dispatch §3 conversion table).

## A. claims_registry.yaml — mints (proofs-1 §5(ii); HOLD [C-XBVP](a'))
1. [C-MAJDA-3DT] (gap G3): multi-D unsteady KL stability + H^s front
   uniqueness; owner F2; falsifier per stop-proof §9 row.
2. [C-XINJ] (G7): global branch injectivity; routes r-a/r-b; owner F2.
3. [C-WSF] (G11): weak-vs-fronted-strong uniqueness; route [S-ACFR]; owner F2.
4. [L-INC]: internal lemma row (THEOREM stratum A / SCHEMA-inherited B).
5. G12 route declaration (Remark 5.3, minimal-load classical route for
   statement (i); ALSO novelty threat: P. Qu / H. Yuan queries owed at
   any paper claim).
6. [T-T0P-E] row: THEOREM, function-space complete, falsifier (t1)-(t3)
   (it is already referenced in ORA of PROGRESS pending its row — this
   closes that).
7. NOT MINTED (declare in a note field or skip): [C-XBVP](a') — HELD OUT
   with the G8 row (VERDICT_confirm: doc1 legs 3+5 open).
8. swirl5f F-2 MINT: sector-decomposition identity
   J_exact = integral of F_true(xi) dmu — mint at **SCHEMA** with
   provenance "swirl5f panel D+R (advisory; panel grades not record
   grades)" and upgrade path = one house until-dry pass; the identity's
   proof route lives in swirl5f_fun.md.
9. D.13 recovery-uniqueness THEOREM clause + D.4 curved-clause THEOREM +
   Prop 1'' "THEOREM modulo (H-UP-fam)" (VERDICT_confirm) — IF the
   claims registry carries per-theorem rows for this class, add/update;
   if these live only in M0, skip and say so.

## B. findings_registry.yaml
1. F-4..F-10 rows (P3) from VERDICT_contract_and_L4R1.md Part A (ii) —
   verbatim content basis F-4 budget-closure audits; F-5 design-sweep
   invariance falsifier (NG-5 viscous channel — "THE primary rejecting
   test of the entire cut"); F-6 phase-gauge/jitter alignment; F-7 chi
   character map UNKNOWN band; F-8 delta_qs a-priori quasi-steady
   number; F-9 wave-asymmetry demotion rule; F-10 corner-trace audit.
   Sources = "VERDICT_contract_and_L4R1.md#F-n (P3)"; owners per the
   verdict text (mostly F2 / first-ingestion windows).
2. LG-1 row `orchestration:until-dry-confirm-direction-unproven`: update
   status/magnitude — confirm direction DISCHARGED for this window and
   pool configuration (SEED_PROTOCOL_v3 result block + VERDICT_escalation
   §1); the row does NOT die silently: rewrite owner/trigger to the
   standing per-pool rule (new pool config = new dual-seed certification).
3. swirl5f flags as rows (dispatch §3 row 14 + §5): FLAG-1 (problem-book
   §8 "<<" overstates drift suppression — erratum duty); FLAG-3 (tau_n
   definition PB-vs-S.22 O(1) apart — pin duty); C8 ("CJ locus" naming
   approximate away from front); F-1 (extend to M0:377). B-1/B-2 are
   CONSUMED this window by the LAND-1 D.13 edit — record them as
   consumed-at-landing rows or notes, not open duties.
4. Escalation residues as rows IF not already carried: doc1 revision-9 +
   confirming round owed (owner: S-FOUNDATIONS-C next window; carrier
   VERDICT_confirm residues[0]); R-4 spec-seeding standing rule (8+
   instances) if a standing-discipline row fits the schema.
5. Hypaudit monitor amendments (CERTIFIED verdict, binding refuter
   amendments): M8 Schotthofer window-convergence/source-trace audit row;
   Liu 2022 census insertions ([I-GEO] census, SOTA census, measure
   library, A3 null-band anchor) — if these amend EXISTING monitor rows,
   edit in place; if they need new rows, mint with source
   "hypaudit/VERDICT_hypothesis_audit.md".

## C. choice_ledger.yaml
1. Agenda rows/annotations: D-1 mixed-signature admissibility (agenda),
   D-2 placement band (the two blinds disagree — record both pressures),
   D-4 I4 normative annotation (consumed by LAND-1's M0 edit if it lands
   the one-line warning — verify and mark accordingly).
2. C51 row: append input note — swirl5f claim 6 (azimuthal-march
   spacelikeness == |w_rel| > c; degeneracy loci == D.18 H-WR/H-NC kernel
   loci) available as DIRECT adjudication input, status PLAUSIBLE pending
   the panel's §8 verifier verdict (dispatch §6 rule 2).
3. C50 row (datum metric): note the acceptance+sensitivity semantics got
   F-3/D-3 carriers this window (cross-ref only).

## D. glossary.yaml
New tokens introduced by the landings (check each against existing
entries first): H3-w, H-SEG, [H-sgn], H-FROZEN-Gamma, H-AM0..H-AM5 (if
absent), m_n (meridional-normal margin), (H-UP-fam), [T-T0P-E], [L-INC],
F-2 identity token. NAMESPACE COLLISION (mandatory fix): the swirl5f
panel's chi = Omega*Gamma/h0 collides with the contract F-7 chi
(sub/supersonic character map) — register the panel group under a
distinct token (e.g. chi_Omega) with a collision note; do NOT land the
numeric chi value (judge-original, PLAUSIBLE pending panel §8).

## E. literature_registry.yaml
swirl5f origin-conversation litmap enrichments (dispatch §5 tail): Miki
Fig.4 tangential profile numbers; K-P +6%/+3% page-verified;
corpus-wide time-mean-tangential-field vacuum search-proven over 26
PDFs — as enrichment notes on existing rows or new rows per schema.

Return: per-file list of rows added/edited + lint outcomes + any honest
residue (rows you could NOT place with reasons).
