#!/bin/bash
# re-run of the model tests with the committed defaults (rescue on, agnostic driver) + their rejectors (2026-10-09)
RV=/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
cd $RV
lane(){ cpu=$1; shift; for t in "$@"; do bash run.sh $t $cpu; done; }
lane 84 t01_thermo t02_cells t09_literature t03_planar_lipfan_plug t04_axi_source_channel t05b_cert_stall t06_geno_rao &
lane 85 t05_geno_migdal t16_bell_march &
lane 87 t07_gradients &
lane 89 t07b_phases &
wait
echo "model lanes done $(date '+%F %T')" > $RV/logs/model_lanes_done.txt
