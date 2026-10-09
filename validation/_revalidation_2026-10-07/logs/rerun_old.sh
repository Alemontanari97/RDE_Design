#!/bin/bash
# rerun_old.sh <cpu> <script> [ENV=VAL ...] -- re-run of an OLD verifier of the registry with today's code (2026-10-09,
# owner's triage: redo / conditional groups). Runs from the repo root, niced and pinned, one thread; the artifacts go to
# logs/old_art/<script>/ (BPRS_ART / CHTW_ART / PMRG_ART) so the working-tree records are not overwritten.
CPU=$1; S=$2; shift 2
ROOT=/data10/falco/RDE/RDE_Design
RV=$ROOT/validation/_revalidation_2026-10-07
PY=/data10/falco/RDE/venv-a1/bin/python
ART=$RV/logs/old_art/$S; mkdir -p $ART
LOG=$RV/logs/old_$S.log
cd $ROOT
export PYTHONUNBUFFERED=1 MALLOC_ARENA_MAX=2 XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export BPRS_ART=$ART CHTW_ART=$ART PMRG_ART=$ART AFAN_ART=$ART
for kv in "$@"; do export "$kv"; done
echo "== rerun_old $S on cpu $CPU, start $(date '+%F %T'), A1_NEWTON_RESCUE=${A1_NEWTON_RESCUE:-default} PSPL_DRIVER=${PSPL_DRIVER:-default}" > $LOG
t0=$(date +%s)
nice -n 19 taskset -c $CPU $PY validation/$S.py >> $LOG 2>&1
rc=$?
echo "== exit $rc, $(( $(date +%s) - t0 )) s, end $(date '+%F %T')" >> $LOG
