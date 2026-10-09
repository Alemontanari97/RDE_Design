#!/bin/bash
# Re-runs every measurement cited in PROBLEM_DEFINITION.md (s2: one niced core); outputs in ../out/. A few minutes.
set -e
H=$(cd "$(dirname "$0")" && pwd); O=$H/../out; PY=/data10/falco/RDE/venv-a1/bin/python; B=/data10/falco/RDE/Nozzle/CASE_3D/q2dhp
run() { nice -n 19 taskset -c ${CPU:-40} $PY "$@"; }
run $H/q2d_axial_mach.py > $O/q2d_axial_mach.txt
run $H/q2d_station_tradeoff.py > $O/q2d_station_tradeoff.txt
run $H/front_structure.py 7.5 12.5 19.5 > $O/front_structure.txt
run $H/convention_sonic.py > $O/convention_sonic.txt
run $H/convention_sonic.py portata_HP 12.5 > $O/convention_sonic_12.5mm.txt
run $H/family_contract.py > $O/family_contract.txt
run $H/cfd_axial_mach_vertical.py $B/1atm/A/wave:26.65 $B/1atm/C/wave:24.22 $B/1atm/E/wave:28.35 $B/0.5bar/C/wave:33.28 \
    $B/0.5bar/E/wave:39.80 $B/0.5bar_Lfix/C/wave:33.67 $B/0.5bar_Lfix/E/wave:37.00 $B/1atm/C/lab:24.22 $B/0.5bar_Lfix/C/lab:33.67 \
    > $O/cfd_axial_mach_vertical.txt
echo done
