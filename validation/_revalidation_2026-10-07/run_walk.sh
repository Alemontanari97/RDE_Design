#!/bin/bash
# run_walk.sh <log tag> <cpus> <script> [args...]  -- an argument-taking test on s2 (venv, nice 19, taskset)
TAG=${1:?tag}; CPUS=${2:?cpus}; SCR=${3:?script}; shift 3
RV=/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
PY=/data10/falco/RDE/venv-a1/bin/python
cd $RV/tests
export PYTHONUNBUFFERED=1 MALLOC_ARENA_MAX=2 XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
nice -n 19 taskset -c $CPUS $PY $RV/tests/$SCR "$@" > $RV/logs/$TAG.log 2>&1
echo "exit $? $(date +%H:%M:%S)" >> $RV/logs/$TAG.log
