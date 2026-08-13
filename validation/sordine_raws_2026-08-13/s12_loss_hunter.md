# S-ORDINE S12(iv) — ADVERSARIAL LOSS-HUNTER REPORT (2026-08-13)

Default posture: something IS lost until independently proven otherwise.
Read-only pass. Three probes below; one file written (this one).

---

## PROBE 1 — LEDGER SAMPLE (8 rows, spread across destination kinds)

Verification method: for each row, opened the CLAIMED destination file and
independently read/grepped for the SPECIFIC content named in the row (not
mere file existence).

| id | kind | destination | check performed | result |
|---|---|---|---|---|
| LR-4 | registry | `registry:variational-driver:objective-omits-throat-panel` | read `docs/findings_registry.yaml` around the id | **VERIFIED**: row present, magnitude text matches ("gradient axis GOVERNS: d(DJ)/dthB = 5.36e3... vs O3 acceptance 9.3"), source anchor `ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md#THE MERGED SLIVER ROW` |
| LR-24 | index | `index:ADR_panel_2026-07-16.md` | read `validation/ADVISORY_INDEX.md` row | **VERIFIED**: row present, content matches claim exactly (600N headline 242.5 vs 245.3; truncation 0.20 vs 0.25-0.30; UD-4 pending) |
| LR-3 | archive | `archive:PROGRESS_ARCHIVE` | read `docs/rde_nozzle_PROGRESS_ARCHIVE.md` head + grepped for the claimed content | **VERIFIED, with a noted inconsistency**: file exists (2377 lines), banner reads "moved from docs/rde_nozzle_PROGRESS.md L120-L2173, 2026-08-13, S-ORDINE S8" and DOES contain the S25/S25-bis stacked delta blocks and NEXT-1 content. The ledger row cites a DIFFERENT line range (L295-2498) than the archive's own banner (L120-L2173) — a documentation/line-number drift, not a content loss (the substantive text is present either way) |
| LR-1 | committed | `committed:3868524` | `git ls-tree -r 3868524 -- validation/` filtered to `PROGRESS_*.md`; `git log --follow` on one file | **VERIFIED with a caveat**: 28 `validation/PROGRESS_*.md` files present in that commit's tree (matches the ~27 claimed). However `git log --follow` shows the sampled file's real history predates 3868524 by several commits — 3868524 is a snapshot where the files are present, not their origin commit. Not a loss, just an imprecise destination label |
| LR-9 | memory | `memory:gate-pre-esecuzione.md` | read the file directly (lives in the Claude project memory dir, NOT in the repo) | **VERIFIED**: file exists, full content matches the claimed standing directive (pre-execution gate: plan-adherence + upstream-rigor audit, dated 2026-07-16) |
| LR-27 | queued | `queued:tranche-e` | grepped `docs/rde_nozzle_PROGRESS.md` for "tranche" | **VERIFIED at pointer level**: census row R31 literally names "tranche residue NOMINATE: (c) refuter/red-team S25-S25bis, (d) consumption map 4 advisory, (e) corpus lit 2026-08-13 (~101 confrontation + ~40 MoC/GENO) — prima duty della prossima finestra di seeding". This is a named forward-work pointer (not yet executed content), consistent with the ledger's own adjudication text — a legitimate "home" for an open item, not a completed transfer |
| LR-10 | glossary | `glossary:R1-R6` | read `docs/glossary.yaml` (936 lines, 163 entries), checked for literal per-token rows vs family grouping | **VERIFIED with caveat**: the glossary groups census tokens under FAMILY entries (e.g. `family: "R<n>*"`) rather than minting ~278 individual rows — this is the glossary's own declared method (line 63: "counted once per segment... to existing entries/families"), so it is compression by design, not loss |
| LR-33 | registry (+cross-check) | `registry:ancourt_peter_atinault_2023`, md5 claim | read `docs/literature_registry.yaml` row AND independently ran `md5sum` on both paths | **VERIFIED BY INDEPENDENT MEASUREMENT**: registry row present with correct dual-path + summary; `md5sum literature/aerospace-10-00797.pdf literature_review/ancourt_2023_adjoint_direct_characteristic_equations.pdf` → both `53ed889bc0e63154131baea42c603b86`, exact match to the claimed hash |

**Probe 1 verdict: 8/8 rows genuinely verified** (content present and
substantively matching claims). Two cosmetic/label imprecisions noted
(LR-3 line-range drift, LR-1 commit-hash meaning) — neither is a content
loss.

---

## PROBE 2 — INVENTORY DIFF

Fresh count (this pass): `find . -type f -not -path "./.git/*" -not -path
"./GENO/*" -not -path "./validation/sordine_raws_2026-08-13/*"` → **516**
files.

Baselines: Phase-1 `authoritative_repo_files.txt` = 436; `_S0.txt` = 500.
Confirmed all three lists use the same exclusions (0 GENO/, 0 sordine_raws
rows in either baseline).

- `comm -23 S0_sorted fresh_sorted` (S0 rows absent from fresh) → **0
  disappeared files**.
- `comm -23 P1_sorted fresh_sorted` (Phase-1 rows absent from fresh) → **0
  disappeared files**.
- `comm -13 S0_sorted fresh_sorted` (new since S0, 16 files): `docs/choice_ledger.yaml`,
  `docs/flag_registry.yaml`, `docs/glossary.yaml`, `docs/literature_registry.yaml`,
  `docs/rde_nozzle_PROGRESS_ARCHIVE.md`, 4x `literature_review/reports/REFUTE_{A,B,C,D}_*.md`,
  `tests/test_advisory_index.py`, `tests/test_glossary.py`, `tests/test_literature_registry.py`,
  `validation/ADVISORY_INDEX.md`, `validation/brick2_profiles_record.png`, plus 2
  `tests/__pycache__/*.pyc` (build noise, not of-record). All new files map
  cleanly to documented, committed work (registries, index, archive, new
  tests, the REFUTE reports from the 2026-08-13 literature window, the
  PNG copy-in adjudicated in LR-41).
- New since Phase-1 (500-436=64 additional rows already counted above at
  the S0 checkpoint): not individually itemized (no disappearance signal
  to chase), consistent with normal growth across S21→S25bis→S-ORDINE.

**Probe 2 verdict: zero disappeared files against either baseline.** No
class of file vanished from disk between Phase-1 (436), S0 (500), and now
(516).

---

## PROBE 3 — HISTORICAL TRACE (10 items + 1 probe item)

| item | current home (exact anchor) | traced? |
|---|---|---|
| (a) S19 corner-mismatch residual figure | `docs/findings_registry.yaml#parametrization:natural-BC-lip-bias` — magnitude field explicitly: "...the natural BC accounts for the bulk of the S19 corner residual of record" (6.629e-2 → 1.166e-2, r=1, -82%) | YES |
| (b) audit finding "objective omits throat panel" | `docs/findings_registry.yaml#variational-driver:objective-omits-throat-panel` | YES |
| (c) GAP-29 NEWTON_TOL_FACTOR flip verdict | `docs/findings_registry.yaml#engine-core:F5-underived-factors` — "GAP-29 sweep EXECUTED S25-bis (s25bis_gap29_sweep.json): 1 FLIP of record — NEWTON_TOL_FACTOR/2 flips cert_verdict" | YES |
| (d) EQ-v2 A/B conjecture status | `docs/claims_registry.yaml#C-EQV2` (class CONJECTURE; Direction A/B statement verbatim), proof anchor `docs/rde_nozzle_MASTER.md#EQ-v2 OF RECORD` | YES |
| (e) S14 panel 16/16 CONFIRMED verdict | `docs/claims_registry.yaml#PAN-S14` — "16 two-lens convergence teams (16/16 CONFIRMED, 0 dissent)" | YES |
| (f) mean-swirl P1 flux-nullity THEOREM* | `validation/ADVISORY_mean_swirl_panel_2026-08-11.md#S5` — "statement of record = P1 flux-nullity THEOREM* (conditional, [T-SLRW] kernel machine-verified...)" | YES, but flagged: the panel's own plan action ("Write P1 as a conditional theorem of record in M0/N6... same-session absorption") was NOT found executed — no `flux-nullity`/`H-AM1` hit in `docs/rde_nozzle_MASTER.md` or `docs/rde_nozzle_N6_swirl.md`. Content is intact and committed (home = the advisory doc), but the R4 retro-propagation into the theory corpus itself appears still outstanding — an open R4 gap, not a content loss |
| (g) M6 vmap-Hessian gate rejection + corrected-form adoption-readiness | `docs/findings_registry.yaml#engine:vmap-hessian-adjoint-divergence` + `#engine:cross-lowering-gradient-floor`, sourced `validation/PROGRESS_2026-08-12_S25bis_speed.md#M6` / `#STEP 13` | YES |
| (h) choice-ledger row: interpolating-spline vs control-points | `docs/choice_ledger.yaml#C1` (Design basis class: clamped/natural interpolating cubic vs "B-spline control polygon (de Boor/Boehm)") and `#C2` (Right-end BC: natural vs "free-end control points") | YES |
| (i) Harroun "near-perfect expansion" misquote correction | `docs/literature_registry.yaml#harroun_2021` — "MISQUOTE OF RECORD — 'near-perfect time-averaged expansion' DOES NOT EXIST in the paper"; double-anchored at `validation/ADVISORY_rde_choking_2026-08-11.md#3. THE MISQUOTE OF RECORD` | YES (two independent anchors) |
| (j) S25-bis recorder-dependence catch | `docs/findings_registry.yaml#record-path:cert-verdict-recorder-dependence` | YES |
| (k) [PROBE ITEM] S22 "X-QDRIFT quarterly drift bench 3/3 PASS with padded-lane rejector" | none found | **NO — UNTRACEABLE** |

### Detail on (k)

Searched the entire repo (516 files, excl. `.git`/`GENO`/sordine_raws) for
`QDRIFT`, `quarterly`, `padded.lane`/`padded_lane`, and `drift.bench` —
**zero hits for all four terms, in any file, any extension.** Also read
the authoritative S22 session log (`validation/PROGRESS_2026-08-11_S22_governor.md`,
matched for "drift": 0 hits) and the S22 memory file
(`memory/s22-f1-governor-o4.md`, full read): S22's actual, fully-documented
content is the F1 "GOVERNOR + P-2 CAPTURE" session — O4 discharge, the
three-way locus test (BRANCH (c) UNANIMOUS), the K_disc~A_0 bridge
falsification, `[X-MGOV]`/`[X-LOCD]` carriers, campaign 1/2. There is no
drift-bench sub-thread, no `X-QDRIFT` carrier, no padded-lane rejector
anywhere in that record. This item does not resolve to any registry row,
index row, archive entry, or committed doc.

---

## VERDICT

Probes 1 and 2 are clean: every sampled ledger row is genuinely backed by
its claimed destination content (one row cross-verified by an independent
md5sum), and zero files present in either historical inventory snapshot
are missing from disk today. Probe 3 traces 9/10 named items plus one
partial (f, content present but not yet retro-propagated per R4 — a
process gap, not a loss) to exact, content-matching anchors.

Item (k) breaks the run: **UNTRACEABLE**, with a strong negative control
(the real S22 record is fully accounted for and contains no trace of it
under any spelling). Per the probe's own binding rule — one untraceable
item that should exist fails the gate — this pass returns **LOSS-FOUND**,
scoped to a single item, pending user/session adjudication on whether
(k) was ever a real artifact or is a planted/mis-specified probe.

```
{
  "report_path": "validation/sordine_raws_2026-08-13/s12_loss_hunter.md",
  "ledger_sample_ok": true,
  "disappeared_files": 0,
  "untraceable": ["(k) S22 X-QDRIFT quarterly drift bench 3/3 PASS w/ padded-lane rejector"],
  "verdict": "LOSS-FOUND"
}
```
