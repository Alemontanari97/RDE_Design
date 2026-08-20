# BRIEF — WAVE-1 LANDING MECHANIC (supplement page fixes + literature
# rider). Mechanical application of ADJUDICATED texts — you decide
# nothing; every edit's authority is cited below. Repo root:
# c:\Users\amont\Claude\Projects\Presentazione RDE CVA\rde-lecture-code
# BASE = validation/sfoundations_raws_2026-08-13. Lint-gated: you run
# the lints and leave them GREEN.

## TASK 1 — supplement page fixes (authority:
## BASE/blocco3/VERDICT_C9C11_supplement.md §1 + §4.4, read them first)
Edit BASE/blocco3/PANEL_C9C11_SUPPLEMENT.md, three point edits, each
as an in-place correction WITH a dated bracket annotation citing its
finding id (append-only spirit: the correction replaces the defective
text, the bracket declares it):
(a) RS911-2: reword §B.1's frozen question to the NEUTRAL
truth-referenced certification question (the judge's wording: the
question asks which adjoint realization makes the DWR estimate an
honest carrier of the J-discretization bar, effectivity measured
against E_true); MOVE the discrete-sensitivity clause into branch
(I)'s description. Do not change any conclusion.
(b) RS911-3: re-attribute arXiv:2009.07096 to Peter, Renac & Labbé
(keep [TITLE] depth marker; note "same ONERA school as the consumed
Ancourt anchor").
(c) RS911-4: fix the Hicken-Zingg citation at BOTH sites (PAPERS
NEEDED item 2 + the §4.4 rider text): of record J. Comput. Phys.
256:161-182 (2014), doi 10.1016/j.jcp.2013.08.014.

## TASK 2 — literature-registry rider (authority: VERDICT_wave1.md
## §4.7 AS CORRECTED BY VERDICT_C9C11_supplement.md §4.4; both read
## in full first)
Edit docs/literature_registry.yaml: APPEND the rider rows at the end
of the entries list, one dated comment header for the batch
("wave-1 adjudication rider, 2026-08-19"). RULES:
- IDENTITY FIDELITY IS THE WHOLE JOB: every identity comes ONLY from
  (i) the panel census one-liners that cite it
  (BASE/blocco3/PANEL_C28.md §2 / PANEL_C27.md §2.3 / PANEL_C9C11.md
  §2.3 / PANEL_C9C11_SUPPLEMENT.md census sections — copy DOIs/venues
  exactly as printed there, at the depth they declare) or (ii) the
  supplement judge's §0 web-verified witnesses. NO new web claims of
  your own; if a rider item's identity is not printed in those files,
  register it at the weakest honest tier with "identity to be settled
  on the PDF" in the identity field (the wanted_aiaa_2019_0197
  precedent).
- DEDUP FIRST: grep the registry for each id/author-year before
  minting; skip existing (Ancourt :199-208 and lozano_ponsin_2025
  :122-128 EXIST — do NOT re-mint; the §4.7 line about adding
  Lozano-Ponsin 2025 is STRUCK per RS911-8).
- ROWS TO MINT (statuses per the procurement discipline in the file
  header: UNREAD = census-cited identity, no read claim; WANTED =
  procurement item, absence on roots verified by your grep):
  from C27's census: Poon-Martins 2007 (SMO), Kennedy-Hicken 2015
  (CMAME 289:332-354), Lambe-Kennedy-Martins 2017, Shapiro 2009,
  Lopez-Still 2007, Samakhoana-Grimmer (LSE near-optimality, Dec 2025
  upd. Jul 2026, preprint tier), the three grouped-aggregation items
  (their names are in refute_C27.md finding RC27-1 / PANEL_C27 §3.2
  option (m) — copy verbatim); from C9C11's census: Becker-Rannacher
  2001, Venditti-Darmofal 2002, Fidkowski-Darmofal 2011, Roache and
  Celik (the GCI canon — mint as the panel prints them; separate rows
  if separately identified, one combined-identity row otherwise),
  Eca-Hoekstra 2014; WANTED tier: Fidkowski-Luo 2011 / Fidkowski 2017
  / the CMAME 2022 output-based-adaptation review (as printed in
  VERDICT_wave1 §4.7), Hicken-Zingg 2014 (CORRECTED cite, task 1(c)),
  Thakur-Nadarajah 2024 arXiv:2405.00904, Budd-Huang-Russell 2009
  Acta Numerica (TITLE tier). Venditti-Darmofal 2000: do NOT mint
  (leg-(b)-conditional per the supplement judge §4.4).
- Each row: id (lowercase snake, author_year pattern of the file),
  identity (verbatim-faithful), paths [] unless a PDF exists on disk
  (do not hunt), status, owner (which duty/row consumes it: name
  F2-C11-ESTIMATOR-CAMPAIGN / F2-DUTY-C27-AGGCOND / C28 duties / C56
  as appropriate, copied from the verdict texts).

## TASK 3 — lints GREEN + report
Run: python tests/test_literature_registry.py ; python
tests/test_glossary.py ; python tests/test_findings_registry.py.
Fix any violation YOUR edits introduced (token-ratchet: keep
descriptors lowercase; new caps-hyphen tokens must resolve or be
reworded). Do NOT touch anything else. Final text = ONLY:
{task1_edits: 3, rows_minted: N, rows_skipped_dedup: [ids],
lints: {lit: PASS|FAIL, glossary: PASS|FAIL, findings: PASS|FAIL}}
Env pinned; GENO/ read-only; no git.
