# S27 (2026-09-09) — the brick-2 plug line REBUILT after the working copy was deleted

## What happened

On 2026-09-04 around 22:55 the working repository
`/data10/falco/RDE/RDE_Design` was removed with `rm -rf` (bash history of
the host). It carried the whole brick-2 plug line: 23 commits that had
never been pushed, because the account holding the checkout has read
access only on `Alemontanari97/RDE_Design`. The nightly mirror had
already propagated the deletion, the July export
`RDE_Design-rde-nozzle-program` is a NON-git snapshot that stops at
2026-08-09, and no copy of the `.git` directory existed on any volume.
The commits themselves are therefore unrecoverable as git objects.

## How the line was rebuilt

The work was reconstructed from the assistant session transcripts, which
record every tool call verbatim and so act as a write-ahead log of the
repository:

1. **Journal.** 2616 file-touching events were mined out of the four
   sessions that built the line (S21 92be2bd8, S22-S24 dd7f90e2,
   S25 3d6d0a92, S26 d13005b1): full-file writes, `Edit` old/new pairs,
   shell heredocs, python patch heredocs, `sed -i` commands, with their
   UTC timestamps.
2. **Bases.** Files grafted into the clone on 2026-08-09T12:48:46Z came
   from the zip snapshot, whose local mtimes (UTC+2) match the last
   zip-path event to the second, so that snapshot IS the graft-time
   content. Upstream files are based on `origin/rde-nozzle-program`
   6be51b9 itself. The claims registry is based on the rebase-time
   snapshot taken in S26 (upstream 163 ids + the six brick-2 carriers).
3. **Replay.** Every clone-era operation was re-applied in global
   timestamp order — string edits by exact match, python patch bodies by
   execution (their own `assert`s are the check), the S22-S24 scratchpad
   patch scripts by running them. 189 operations.
4. **History.** For each lost commit the tree was rewound, replayed up to
   that commit's instant, and committed with the original message,
   pathspecs and author/committer date recovered from the transcripts.

## Verification

- **Numeric-lint fingerprint.** The R28 ratchet stores a per-file count of
  unclassified literals. Those counts were recorded by the lint itself in
  the S26 window, before the deletion, and are a fingerprint no partial
  reconstruction can accidentally match: **100 files, 0 ratchet
  violations** — every carrier reproduces its recorded count exactly.
- **The four lints on HEAD:** claims PASS (0 violations), numeric-lint
  ratchet PASS, advisory-index PASS, on-demand carriers PASS.
- **Re-execution.** Six carriers were re-run against their restored record
  logs and reproduce them line for line: `rao1961_oracle` 18/18 PASS,
  `rao1961_control_surface` 6/6 PASS, `rao1961_our_functional` 3/3 PASS,
  `rao1961_ideal_spike` 4 FAIL / 1 PASS (the falsifier that fired, result
  of record), `rao1961_world` its own falsifier fired (result of record),
  `rao1961_twin` 6/6 PASS on the legacy p_b=0 GENO field.

## NOT recovered (declared, not faked)

These are derived artifacts of long runs; nothing was invented to stand
in for them. All are regenerable by re-running the carrier that owns
them, with the commands in the S23/S24 handoffs:

| artifact | what it was | how to regenerate |
|---|---|---|
| `validation/_plug_adaptive/design.json` | the S22 adaptive design of record | production run of `a1_plug_adaptive.py` (PAKN_M0=10 K=61 N=51, ~3 h) |
| `validation/_plug_gain/verdict.json`, `analysis.json`, `design_fine.json` | the S23 verdict vectors | `a1_plug_gain_resolve.py` rungs + `PGRS_STAGE=final` |
| `validation/_plug_gain/run_of_record_S23_final.log` | its final-stage log | same run |
| `figs/data_rao_walls.npz`, `figs/data_s24_rot.npz` | figure input data | `make_figures.py` helpers + `gen_s24_data.py` |
| `figs/fig_spike_designs.pdf`, `fig_s23_ladder.pdf`, `fig_s23_driver.pdf`, `fig_worked_example.pdf`, `fig_s24_rotational.pdf` | the S22-S24 figures | `make_figures.py` once the data above exists |
| `docs/rde_nozzle_A1_brick2_thrust.pdf` | the built document | `docs/brick2_doc_src/build.sh` once the figures exist |
| `validation/s25_spdb_m0_s2_2026-08-13.json` | the s2 re-run of the S25 bench | re-run the bench, or drop (the artifact of record is the upstream one, restored) |

The eight `_plug_gain/*.npz` and `_plug_adaptive/cycle_02.npz` run caches
were also lost, but the line had already un-tracked them (S24), so the
committed tree is unaffected. Figure binaries carried here are the
2026-08-09 snapshot versions; the four figures generated later are the
ones listed above. **The document therefore does not build until those
figures are regenerated.**

## How this history differs from the one that was lost

- 21 commits instead of 23. Two carried nothing but a lost artifact:
  the S23 `design_fine.json` commit and the S26 "no-downgrade repair"
  (whose content was the s2 bench copy). Both are recorded here instead.
- Commit dates are the original ones; the objects are new. The history is
  a re-authoring, not the original objects, and says so here.
- `validation/a1_ideal_march_jax.py`: the additive `wall_u`/`wall_v`
  export was re-grafted onto the current upstream out-dict, exactly as
  the S26 rebase had done (the recorded edit targeted the older one).
- The Italian translation of `ch_appendix.tex` and the Italian figure
  labels in `make_figures.py` were uncommitted work in the destroyed tree
  (stash of record); they are committed here rather than left floating.

## Lesson of record

Work that exists only in one unpushed working copy is one command away
from not existing. The line had been unpushable for a month (read-only
credentials) and no bundle was ever written to a second volume; a
`git bundle` costs seconds and would have made this session unnecessary.
Until push access exists, the branch should be bundled to
`/data10/falco/RDE/handoff/` after every session.
