#!/bin/bash
# lanes of the agnostic-driver regression (2026-10-08): each lane runs its walks one after the other, one core each
cd /data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
lane(){ cpu=$1; shift; for job in "$@"; do set -- $job; t=$1; shift; bash run_walk.sh $t $cpu "$@"; done; }
lane 86 "t08b_walk_A0_qntr t08b_rao_walk.py A 0" "t08b_walk_C0_qntr t08b_rao_walk.py C 0" "t10_walk_axial_e381_RD04_mi15_bump_qntr t10_rao_walk.py axial_e381_RD04_mi15 bump" &
lane 87 "t08a_walk_B0_K80_qntr t08a_planar_walk.py B 0" "t08a_walk_C0_K80_qntr t08a_planar_walk.py C 0" "t10_walk_axial_e381_RD04_mi15_half_qntr t10_rao_walk.py axial_e381_RD04_mi15 half" &
lane 88 "t08a_walk_A1_K80_qntr t08a_planar_walk.py A 1" "t08a_walk_B1_K80_qntr t08a_planar_walk.py B 1" &
lane 89 "t08c_walk_0_qntr t08c_migdal_walk.py 0" "t08c_walk_1_qntr t08c_migdal_walk.py 1" &
wait
echo "lanes done $(date +%H:%M:%S)"
