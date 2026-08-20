# RIDER_wave2_lit_landing — C3 block-0 literature-registry landing report

LANDING-MECHANIC agent, S-FOUNDATIONS-C3 block 0, 2026-08-20.
Mandate: VERDICT_wave2.md §4.15 (wave-2 registration rider) +
MANIFEST_papers_foundations_c.md (arrivals) + FOUR-ROOT header update
+ lint gate. Files edited: docs/literature_registry.yaml (only) +
this report. Identity sources: PANEL_C31TRIO.md §4.4 + PAPERS NEEDED,
refute_C31TRIO.md RC31T-3, PANEL_C1REP.md §2.1/§2.2/§2.3/§4 rider +
PAPERS NEEDED, PANEL_C2021.md §2.3/§4.6, manifest page-1-verified
table — never memory.

## MID-WINDOW BRIEF UPDATE (coordinator, consumed)
Becker-Rannacher 2001 was USER-UPLOADED mid-window as
literature/becker_rannacker.pdf (filename spelling of record; page-1
verified by the orchestrator: 'An optimal control approach to a
posteriori error estimation in finite element methods', Acta Numerica
(2001) pp. 1-102, text layer present). Registered ON DISK: row
wanted_becker_rannacher_2001 upgraded WANTED->UNREAD in place (id
kept), path added, owner = C11/DWR canon. This supersedes the
manifest's fetch-FAILED declaration and my earlier fetch-failed
annotation (overwritten in the same window). Root A re-measured after
the upload: 32 (command below), not the 31 of the first measurement.

## DECLARED JUDGMENT-ADJACENT ACTS (mechanical landing, all declared)
1. Uno same-paper multi-path row: vanaret_leyffer_2026_uno carries
   BOTH literature/uno_paper.pdf (published version of record, NO
   text layer — declared in-row) and the arXiv:2406.13454v2 preprint
   file, per the brief's dedup convention. The coverage lint counts
   one row per root regardless of same-root path multiplicity, so a
   balancing bulk row bulk_lit_uno_preprint_duplicate (root A, count
   1) was minted to keep root A at discrepancy 0 without splitting
   one paper into two rows. Declared in the row, the bulk row, and
   the header.
2. Upgraded rows KEEP their historical wanted_* ids (upgrade-in-place
   fidelity; ids verified registry-internal by repo-wide grep before
   the call): wanted_breitkopf_ulbrich, wanted_hicken_zingg_2014,
   wanted_fidkowski_darmofal_2011, wanted_thakur_nadarajah_2024,
   wanted_becker_rannacher_2001 — all now UNREAD with paths.
3. giles_pierce_1997 minted as a DISTINCT paper from giles_pierce_2000
   (FTaC intro) and giles_pierce_2001 (JFM quasi-1D) — dedup call on
   the AIAA 97-1850 paper number; the §4.15 held-rows clause (no new
   Giles-Pierce rows for the RIDER) is honored — this row is an
   ARRIVAL registration, not a rider mint.
4. venditti_darmofal_2000 minted (arrival forces coverage); the
   wave-1 'leg-(b)-conditional, NOT minted' deferral declared
   superseded IN BOTH rows (new row + cross-note updated in
   wanted_venditti_darmofal_2002).
5. kraiko_2016_two_sided: C1REP cross-ref landed as a summary
   one-liner on the existing READ-INTEGRAL row (cite-not-remint).
6. MPCC/bundle items (2501.13835, 2604.18192, 2604.18726) NOT minted:
   C28-F-1-gated deferral KEPT per §4.15 (declared in the section
   comment).
7. Lint invocation: the brief's `python -m pytest ...` fails in the
   pinned env (No module named pytest; installing is FORBIDDEN by the
   pinned-environment rule). The lint's own documented usage
   (`python tests/test_literature_registry.py`, stdlib-only) was run
   instead — deviation declared, verdict read then quoted.
8. OBSERVED, NOT TOUCHED (brief forbids root-D claim edits): the
   header's root-D reconciliation line still says disk 58 == rows 25
   + bulk 33; the lint measured disk D = 59 this window. Cause
   located: literature_review/CF_ASO_Paper_PrePrint.pdf (landed
   2026-08-14, covered by row unread_cf_aso_preprint since
   2026-08-17) post-dates the header's 2026-08-13 numbers. Coverage
   is GREEN (row covers the file); the stale header line is flagged
   to the orchestrator for the next reconciliation window.

## MACHINE SUMMARY

```
rows_minted: 34 total = 12 UNREAD arrival rows (byrd_hribar_nocedal_1999,
  nocedal_wright_2006_2ed, giles_pierce_1997, venditti_darmofal_2000,
  huang_zahr_2022, huang_zahr_2023_companion, masters_etal_2017,
  lauer_ansell_2025_pas, deuflhard_2011_csm35, yamamoto_1986_numermath48,
  vanaret_leyffer_2026_uno [2 paths], vanaret_montoison_2026_joss)
  + 21 WANTED rider rows (wanted_conn_gould_toint_trm,
  wanted_nadarajah_jameson_2000, wanted_warp_ip_warmstart_2026,
  wanted_dual_shifted_ipm_coap_2023, wanted_conic_ipm_central_path_2025,
  wanted_kulfan_cst_2008, wanted_hicks_henne_1978,
  wanted_mdg_ice_2311_00701, wanted_onofri_paciorri_2017_book,
  wanted_dfo_competitive_2505_09088, wanted_kantorovich_1948,
  wanted_ferreira_svaiter_kantorovich,
  wanted_ferreira_goncalves_svaiter_robust, wanted_hauenstein_sottile_2012,
  wanted_breiding_rose_timme_2023, wanted_issac_2024_krawczyk_tracking,
  wanted_icms_2024_interval_alpha, wanted_farrell_birkisson_funke_2015,
  wanted_signed_sigma_min_2208_05954, wanted_nurkanovic_2019_asrti,
  wanted_automatica_2021_memory_warmstart)
  + 1 bulk balance row (bulk_lit_uno_preprint_duplicate, root A, count 1)
rows_upgraded: 8 = 5 WANTED->UNREAD in place with paths
  (wanted_breitkopf_ulbrich, wanted_hicken_zingg_2014,
  wanted_fidkowski_darmofal_2011, wanted_thakur_nadarajah_2024
  [journal-version JCP 523:113633 of arXiv:2405.00904 noted],
  wanted_becker_rannacher_2001 [mid-window user upload]) + 3 in-place
  text edits (kraiko_2016_two_sided summary cross-ref one-liner;
  wanted_venditti_darmofal_2002 cross-note updated; FOUR-ROOT header
  root-A block rewritten with measured numbers)
dedup_skipped: 9 rider identities NOT re-minted (cite-not-remint /
  held / deferred): Vanaret-Leyffer Uno 2024/2026 -> arrival row;
  Byrd-Hribar-Nocedal 1999 -> arrival row; Nocedal-Wright 2e ->
  arrival row; Masters comparison -> arrival row; Huang-Zahr 2022 +
  arXiv:2304.11427 -> arrival rows; PAS review 2025 -> arrival row;
  Deuflhard CSM 35 -> arrival row; Yamamoto 1986 -> arrival row;
  kraiko_2016_two_sided -> existing row updated. HELD per §4.15 (no
  new rows): ancourt_peter_atinault_2023, giles_pierce_2001,
  giles_ulbrich_2010_part1/part2, lozano_ponsin_2025. DEFERRED per
  §4.15: MPCC/bundle 2501.13835 / 2604.18192 / 2604.18726
  (C28-F-1-gated).
identity_flags: 7 items landed below full bibliographic fidelity
  (mint at the fidelity the on-file text supports, NEVER invented):
  (1) wanted_conn_gould_toint_trm — no year/venue in the panel text;
  (2) wanted_kulfan_cst_2008 — no venue in the panel text;
  (3) wanted_hicks_henne_1978 — no venue in the panel text;
  (4) wanted_kantorovich_1948 — theorem-statement level only, no
      title/venue in the panel text;
  (5) yamamoto_1986_numermath48 — VOLUME DISCREPANCY declared in-row:
      page-1 verification says Numer. Math. 48:91-98, PANEL_C2021 §2.3
      cites the 'sharp error bounds' paper as Numer. Math. 49 (1986);
      settled at first read;
  (6) wanted_dual_shifted_ipm_coap_2023 + wanted_conic_ipm_central_path_2025
      + wanted_automatica_2021_memory_warmstart — search-level
      provenance declared, authors/titles to be settled on the PDFs;
  (7) giles_pierce_1997 — identity anchored on the AIAA 97-1850 paper
      number + filename (manifest gives no full title).
root_A_measured: 32 (command: Get-ChildItem literature -Filter *.pdf |
  Measure-Object — run TWICE this window: 31 before, 32 after the
  mid-window Becker-Rannacher upload; 32 is the number of record)
registry_total_measured: 137 (command: (Select-String -Path
  docs\literature_registry.yaml -Pattern '^- id:' | Measure-Object).Count;
  arithmetic check: 103 rows at open + 33 entry mints + 1 bulk mint = 137;
  lint parse concurs: 128 entries [48 WANTED] + 9 bulk rows)
lint_verdict: "  literature registry lint (four roots)                PASS (128 entries [48 WANTED], 9 bulk rows, disk A/B/C/D = 32/47/77/59, 0 violations)"
  (read-then-quoted, verbatim last line; all 4 seeded rejectors
  REJECTED as required; invocation deviation declared above: direct
  stdlib run, pytest module absent from the pinned env)
```
