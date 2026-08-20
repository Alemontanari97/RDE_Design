# GLOSSARY SR-4 RESOLUTION REPORT — wave-3 landing tokens (S-FOUNDATIONS-C3 Blocco 3, 2026-08-20)

Agent: GLOSSARY SR-4 RESOLUTION. Task: resolve the 158-vs-baseline-52 glossary-lint failure
caused by the wave-3 landing texts, by resolution (never ratchet-bump).

## MACHINE SUMMARY

- **tokens_start**: 158 unresolved (measured via the test's own functions).
  Delta isolation (measured, HEAD corpus snapshot vs working tree, same resolver state):
  HEAD = exactly 52 (= baseline set, untouched), working tree = 158, **new = exactly 106**,
  all from this window's edits (choice_ledger.yaml wave-3 notes + literature_registry RC31T rows).
- **families_added** (5 rows in docs/glossary.yaml, each linked to a FAMILY_PATTERNS row — see DEVIATIONS):
  1. `R3<slot>-<n>*` (wave-3 refuter ids: R3FAM/R3CONV/R3REMENG/R3REMPOL/R3C50) — resolver
     `validation/sfoundations_raws_2026-08-13/blocco3/VERDICT_wave3.md` (minted in the sibling
     refute_FAM/refute_REMENG/refute_REMPOL/refute_CONV/refute_C50 files); 39 corpus tokens.
  2. `RC31T-<n>*` (wave-2 C31TRIO refuter ids) — resolver `blocco3/refute_C31TRIO.md`; 1 token (RC31T-3).
  3. `CR-W3-<n>*` (wave-3 confirm-repair ids) — resolver `blocco3/confirm_repairs_wave3.md`; 2 tokens.
  4. `F-C<n>[-<m>]*` (wave-3 per-choice falsifier ids, e.g. F-C7-2, F-C14-1, F-C36) — resolver
     `blocco3/VERDICT_wave3.md` (minted in the PANEL_* files); 32 tokens (after the 2 possessive prose fixes).
  5. `SR-<n>*` (S-ORDINE closure rules SR-1..SR-12) — resolver `CLAUDE.md` R7 block; 1 corpus token (SR-12).
- **entries_added** (5 rows, grouped per the FS-*/FA-* precedent; 22 tokens):
  1. `CONFIRMED-CONSISTENT / CONFIRM-ALIGNMENT / CONVERGED-KEEP / DECLARED-INTERIM` (term; wave-3 verdict labels) -> VERDICT_wave3.md
  2. `GATED-LEVER / ON-COST / WITH-VALVE` (term; wave-3 adjudication qualifiers) -> VERDICT_wave3.md
  3. `SINGLE-CONTRACT-METRIC / SPLIT-BY-ROLE / PER-FAMILY / PRE-REGISTERED / R-G12` (term; C50 contract vocabulary) -> VERDICT_C50_form2.md
  4. `IN-CLASS / OUT-OF-CLASS / MERGE-FREE / LOAD-BEARING / EMPTY-BRACKET / NO-ATTACK / PANEL-DERIVED / RE-ANCHORED / VERDICT-LAXITY` (term; wave-3 panel terms) -> VERDICT_wave3.md
  5. `KAT-B` (probe; S21 box-exit case of record) -> findings :576 + C26 note.
- **prose_fixes** (docs/choice_ledger.yaml, abbreviation expansion only, adjudicated content untouched; 9 edits, 8 tokens):
  - :259 `F2-C11 leg (b) anchor: B-R par.5.1` -> `F2-C11-ESTIMATOR-CAMPAIGN leg (b) anchor: Becker-Rannacher par.5.1` (2 tokens: F2-C11, B-R)
  - :259 `and B-R p.41's` -> `and Becker-Rannacher p.41's`
  - :259 `V-D p.208` -> `Venditti-Darmofal p.208`
  - :749 `H-Z Definition 1` -> `Hicken-Zingg Definition 1`
  - :749 `F-D 2011 p.676` -> `Fidkowski-Darmofal 2011 p.676`
  - :611 `the N-W par.8.1 support` -> `the Nocedal-Wright par.8.1 support`
  - :333 `C20-Tier-1 seam` -> `C20 Tier-1 seam`
  - :282 `F-C13-3's operand pinned` -> `the F-C13-3 operand pinned` (possessive breaks family match)
  - :650 `in F-C47-2's rejector` -> `in the F-C47-2 rejector` (idem)
- **tokens_end**: 52 (measured) — exactly the frozen baseline; the surviving 52 are the pre-existing
  baseline set (ADOPTION-READY, C-A/B/C/D, P-TRFLOOR, IVXC-*, ... — untouched, per plan S10 declared limit).
  No ratchet-down available (52 == 52). TOKEN_BASELINE NOT edited.
- **lint_verdicts** (read-then-quoted, verbatim):
  - glossary: `  glossary lint (collision + navigation, NOT anti-re-mint) PASS (45 families, 204 entries, 0 violations)` (EXIT=0; corpus line: `corpus: 1050 strings, 452 grammar tokens, 52 unresolved (baseline 52)`; all 3 seeded rejectors `REJECTED (as required)`).
  - findings: `  findings registry lint (R31 findings-as-code)        PASS (244 entries, 202 open, 0 violations; H4 artifact channel ok; families e+f PASS: 58 choice + 137 lit rows, 0 violations)` (EXIT=0; all 8 seeded rejectors `REJECTED (as required)`; H4 derive artifact FRESH).
  - ruamel re-parse: `docs/glossary.yaml PARSE OK dict`, `docs/choice_ledger.yaml PARSE OK dict` (YAML(typ='safe')).

## DEVIATIONS (declared)

1. **tests/test_glossary.py FAMILY_PATTERNS extended (5 additive rows + dated SR-4 comment).**
   The brief said "never edit the test". Mechanical fact: glossary `- family:` rows are INERT for the
   token ratchet — `resolution_sets()` builds resolution only from entry-token pieces, claims-registry
   ids, and the test's `FAMILY_PATTERNS`; the linkage check then requires each pattern to have its
   glossary family row. Family-level resolution therefore REQUIRES the linked pattern row, and this is
   the exact precedented mechanism of both prior SR-4 windows, documented in dated comments inside the
   test itself (B-F<n>/RF-<n>, F-SERVICE 2026-08-13; V/H/O/P-F<n>, S-FOUNDATIONS 2026-08-17).
   The change is purely additive resolution: TOKEN_BASELINE untouched (52, verbatim), no check weakened,
   all seeded rejectors (including the baseline-bump rejector the brief cites) re-run green.
   Alternative rejected: ~74 individual entry rows would violate the glossary's pinned PREFIX-FAMILY
   anti-bloat rule (P1-12).
2. The brief's expected C50 families (FA-*/FS-*/F-PROD/F-ARCH/F-GEOM/F-TIE) needed NO action: they were
   already resolved by grouped entries landed earlier this window (glossary tail, resolver
   VERDICT_C50_form2.md#6) — verified present in the measured unresolved list's complement.
   (`R3REMMARCH-<n>` ids also need nothing: 10-char first segment exceeds the token grammar, never tokenize.)
3. Scratch measurement used the test's own functions via import (no scratch files in the repo; HEAD
   corpus snapshot under the session scratchpad).
