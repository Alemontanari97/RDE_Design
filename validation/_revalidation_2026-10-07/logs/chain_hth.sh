#!/bin/bash
# when both Humphreys walks have written their results: three-grid reading + figure, numbers, deck rebuild
RV=/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07
cd $RV
until [ -f out/t10_walk_hth71_rao_mi17_bump_qntr.json ] && [ -f out/t10_walk_hth71_rao_mi17_half_qntr.json ]; do
  for t in bump half; do grep -q "Traceback" logs/t10_walk_hth71_rao_mi17_${t}_qntr.log 2>/dev/null && { echo "walk $t failed $(date +%H:%M)"; exit 1; }; done
  sleep 60
done
echo "walks done $(date +%H:%M)"
bash run_walk.sh t17_hth 82 t17_slides.py hth
grep -q "saved" logs/t17_hth.log || { echo "t17 hth failed $(date +%H:%M)"; exit 1; }
python3 tests/t18_numbers.py planar methane rao61 axial hth migdal bell bellideal > logs/t18_final.log 2>&1
cd doc && /data10/falco/bin/tectonic slides.tex > ../logs/tectonic_final.log 2>&1
echo "deck rebuilt exit $? $(date +%H:%M)"
pdftotext slides.pdf - | grep -nE '\?\?|running' | head
