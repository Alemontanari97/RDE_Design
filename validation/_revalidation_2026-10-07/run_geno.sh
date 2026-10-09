#!/bin/bash
# run_geno.sh <case dir under geno/>  -- runs ON s3 (GENO needs libgfortran.so.4); nice 19, one thread.
C=${1:?case}; RV=/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
cd $RV/geno/$C || exit 2
md5sum /data10/falco/RDE/codes/GENO/bin/GENO > geno_binary.md5
( time nice -n 19 /data10/falco/RDE/codes/GENO/bin/GENO ) > run.log 2>&1
echo "exit $? $(date +%H:%M:%S)" >> run.log
