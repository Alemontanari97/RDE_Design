#!/bin/bash
# run.sh <test script name without .py> [cpu list]   -- runs ON s2 (the venv exists only there), niced and pinned.
# Budget rule of the owner on s2: <= 12 threads in total across all our runs, nice 19, taskset.
T=${1:?test name}; CPUS=${2:-88-89}
RV=/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
PY=/data10/falco/RDE/venv-a1/bin/python
cd $RV/tests
export PYTHONUNBUFFERED=1 MALLOC_ARENA_MAX=2 XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
nice -n 19 taskset -c $CPUS $PY $RV/tests/$T.py > $RV/logs/$T.log 2>&1
echo "exit $? $(date +%H:%M:%S)" >> $RV/logs/$T.log
