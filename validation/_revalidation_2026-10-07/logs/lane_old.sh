#!/bin/bash
# two lanes of old-verifier re-runs (2026-10-09): cpu 91 = the fold margin (longest), cpu 95 = the rest in sequence
RV=/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
bash $RV/logs/rerun_old.sh 91 a1_plug_margin &
( for s in thermotab_c1_jax validity_monitor a1_swirl_march a1_plug_march base_pressure a1_chutkey_twin a1_rot_march o31_rot; do
    bash $RV/logs/rerun_old.sh 95 $s
  done ) &
wait
echo "lanes done $(date '+%F %T')" > $RV/logs/old_lanes_done.txt
