#!/bin/bash
# our-world chain: twin (running) -> O3.3 -> SQP-return; each only if the previous passed
cd /data10/falco/RDE/RDE_Design
PY=/data10/falco/RDE/RDE_Design-rde-nozzle-program/.venv-a1/bin/python
D=validation/_ourworld
until grep -q "##### exit" $D/run_twin_ycut_2026-09-15.log; do sleep 30; done
grep -q "##### exit=0" $D/run_twin_ycut_2026-09-15.log || { echo "twin failed -> chain stopped"; exit 1; }
( echo "##### ourworld_o33 (x0 1.50, K 161, tip cut 0.01) $(date +%F\ %T) $(hostname)"; $PY -u validation/ourworld_o33.py; echo "##### exit=$? $(date +%F\ %T)" ) > $D/run_o33_2026-09-15.log 2>&1
grep -q "##### exit=0" $D/run_o33_2026-09-15.log || { echo "o33 failed -> chain stopped"; exit 1; }
( echo "##### ourworld_sqp_return (x0 1.50, K 161, tip cut 0.01) $(date +%F\ %T) $(hostname)"; $PY -u validation/ourworld_sqp_return.py; echo "##### exit=$? $(date +%F\ %T)" ) > $D/run_sqpret_2026-09-15.log 2>&1
echo "chain done $(date +%T)"
