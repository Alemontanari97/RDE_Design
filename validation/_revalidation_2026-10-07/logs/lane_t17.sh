#!/bin/bash
# slide readings re-run WITHOUT their ladder caches (2026-10-09): the optimiser cases' proofs re-marched by today's code
RV=/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
cd $RV
bash run_walk.sh t17_planar_r 84 t17_slides.py planar &
bash run_walk.sh t17_methane_r 85 t17_slides.py methane &
bash run_walk.sh t17_rao61_r 87 t17_slides.py rao61 &
bash run_walk.sh t17_axial_r 89 t17_slides.py axial &
bash run_walk.sh t17_hth_r 90 t17_slides.py hth &
bash run_walk.sh t17_migdal_r 91 t17_slides.py migdal &
bash run_walk.sh t17_bell_r 93 t17_slides.py bell &
bash run_walk.sh t17_bellideal_r 95 t17_slides.py bellideal &
wait
echo "t17 lanes done $(date '+%F %T')" > $RV/logs/t17_lanes_done.txt
