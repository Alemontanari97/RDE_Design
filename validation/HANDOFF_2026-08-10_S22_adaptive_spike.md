# HANDOFF — [F2/A1] adaptive spike, S22 (2026-08-10)

**READ THIS FIRST when resuming the nozzle optimizer** (it supersedes
`HANDOFF_2026-08-09_S21_brick2plug.md` as the entry point; that file
remains authoritative for the rebase story, the GENO -O0 trap and the
S21 traps 1-5, all still in force). Full narrative:
`PROGRESS_2026-08-10_S22_adaptive_spike.md`.

## 1. Where things stand in one paragraph

[X-AKNO] was applied to the spike: new carrier **[X-PAKN]**
(`validation/a1_plug_adaptive.py`), production run **11/12 PASS** with
the sole FAIL being the verdict check A-8 itself. Adaptivity WORKS
(one adjoint-guided knot at x = 0.4575 buys +0.1921 % where a uniform
11th knot buys +0.0002 %; second insertion buys nothing), but on the
3-point march ladder up to (241,201) the gain over the fan streamline
falls 0.313 → 0.186 → 0.080 % against a 0.426 % band, so **the
free-form-spike claim remains NOT ESTABLISHED at 16× the S21
resolution** — and the finding is that resolution now needs a better
INSTRUMENT (optimize at (121,101), or Richardson-extrapolate the
paired ladder), not more knots. Nothing was committed; the S21 stage
(82 files) is untouched and the S22 edits sit on top of it unstaged.

## 2. State of the trees (delta from S21)

| item | state |
|---|---|
| `brick2-plug` stage | the S21 82 staged files, untouched, still uncommitted |
| NEW unstaged/untracked | `validation/a1_plug_adaptive.py` (carrier), `validation/PROGRESS_2026-08-10_S22_adaptive_spike.md`, this handoff, `validation/_plug_adaptive/` artifacts, edits to `docs/claims_registry.yaml` (X-PSPL statement fix + X-PAKN entry), `validation/INDEX.md` (S21 row correction + S22 row), `validation/a1_plug_spline_opt.py` (settings-tagged checkpoint save) |
| GENO | unchanged from S21 (4 src/lib edits uncommitted, -O0 pinning) |
| venv | unchanged: `/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python` |

## 3. New traps (S21's five remain in force)

6. **[X-PSPL] used to OVERWRITE its checkpoint unconditionally** at a
   fixed name; a quick verify run at (M=6,K=81,N=61) destroyed the
   S21 10-knot production npz this session (never git-tracked, gone).
   Damage bounded: the class-0 cold start reproduced the recorded
   optimum J **bit-for-bit** (115739431.39643042) and the design
   vector now lives in `validation/_plug_adaptive/design.json` +
   `cycle_01.npz`. The save is now settings-tagged in both carriers —
   do not "simplify" it back.
7. **At default settings (M=6, K=81, N=61) the TR-SQP driver takes NO
   step from the raw streamline** in either direction ("no motion"),
   so C-6/R-1 degenerate there. Records are made at production
   settings (M=10, K=61, N=51), where it walks. No recorded number
   exists at defaults; don't create one without understanding this.
8. **The gain falls under march refinement, on every ladder measured**
   (adaptive 0.313→0.186→0.080 %, uniform 0.127→0.068→0.029 %).
   Any coarse-grid gain quote without its own ladder band is
   presumptively optimizer-fit-to-discretization. The rung-to-rung
   decay ratio is ~0.84 — extending the ladder brute-force is a
   losing race (rung 3 alone costs ~2×4300 s).

## 4. Results of record

See `PROGRESS_2026-08-10_S22_adaptive_spike.md` §"Numbers of record".
Registry: [X-PAKN] added (128 → 129), [X-PSPL] statement REWRITTEN
(it still asserted the S21-retracted +0.0908 % headline — drift
caught and fixed this session), claims lint PASS.

## 5. What is open, in priority order

1. **Resolve the gain with a better instrument**: (a) re-optimize AT
   (121,101) so the incumbent is not tuned to the coarse march, then
   ladder from there; (b) Richardson-extrapolate the PAIRED
   difference on the existing 3-rung ladders (both converge
   monotonically; an extrapolated gain ± derived band may settle the
   sign); (c) longer term, the [X-FMTR] exact-functional route once
   its ~1 % field residual is understood. The raw material for (b) is
   already in `_plug_adaptive/design.json`.
2. O3.3 locus a priori (unchanged from S21).
3. The plug's ~1 % momentum residual (unchanged).
4. Rao comparison at full expansion, L = 5.825 m (unchanged).
5. config_compare closures onto a1_flux_meter (unchanged).
6. CFD P1 blocked on SU2 install (unchanged).

**Owner decisions pending:** the S21 two (commit the stage; bless the
GENO edits + -O0 pinning) plus one new: whether the S22 working-tree
set joins that commit or follows it.

## 6. Commands

```bash
U=/data10/falco/RDE/RDE_Design
PY=/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python
cd $U

# the S22 production run of record (~3.4 h; ladder rung 3 dominates)
PAKN_M0=10 PAKN_K=61 PAKN_N=51 PAKN_MAXCYC=3 PAKN_MAXINS=2 \
  PAKN_ITERS=30 PAKN_CONTROL=1 $PY validation/a1_plug_adaptive.py

# quick structural smoke (~6 min, 9/10 — A-8 honestly fails there)
PAKN_M0=6 PAKN_K=21 PAKN_N=17 PAKN_MAXCYC=1 PAKN_MAXINS=1 \
  PAKN_ITERS=6 $PY validation/a1_plug_adaptive.py

$PY tests/test_claims_lint.py     # registry lint (now 129 entries)
```

Artifacts: `validation/_plug_adaptive/{design.json, cycle_01.npz,
cycle_02.npz, run_of_record_S22.log}` — the full production log is
preserved in the tree alongside every number of record.
