"""(v, slow tier) Live examples + design study — blessed printed digits EXACT.

Runs the four example scripts as subprocesses (exactly as a student would)
and asserts the golden digits in their stdout:
  example_cj.py            'U_CJ  =  1969.0 m/s' + final OK line
  example_cycles.py        'eta_FJ(CH4/air) = 0.300' + OK
  example_thrust.py        'live 237.1 s | shipped 237.1 s' + OK
  example_design_study.py  'U_CJ = 2373.5 m/s', bell 'Isp = 233.6 s',
                           aerospike 'Isp = 245.3 s', final OK
  example_headtohead.py    SL optima + LIVE throatless/nozzled closures
  example_design_10kN.py   mission-fill detonability + wave-head band + closure
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASES = [
    ('example_cj.py', ['U_CJ  =  1969.0 m/s', 'OK: CJ state reproduces']),
    ('example_cycles.py', ['OK: eta_FJ(CH4/air) = 0.300']),
    ('example_thrust.py', ['live 237.1 s | shipped 237.1 s',
                           'OK: table printed']),
    ('example_design_study.py', ['U_CJ = 2373.5 m/s',
                                 'Isp = 233.6 s', 'Isp = 245.3 s',
                                 'OK: design study complete']),
    ('example_headtohead.py', ['Isp=233.6 s', 'Isp=245.3 s',
                               'R_bar=22.6 mm',
                               'OK: head-to-head complete']),
    ('example_design_10kN.py', ['W=3.14 central', 'Isp=268.0 s',
                                'Isp=278.4 s',
                                'OK: 10 kN example complete']),
]


def run():
    ok = True
    for script, needles in CASES:
        p = subprocess.run([sys.executable, os.path.join(ROOT, 'examples',
                                                         script)],
                           capture_output=True, text=True, cwd=ROOT)
        out = p.stdout + p.stderr
        good = p.returncode == 0 and all(n in out for n in needles)
        ok &= good
        missing = [n for n in needles if n not in out]
        print('  %-28s rc=%d  %s%s'
              % (script, p.returncode, 'PASS' if good else 'FAIL',
                 ('  missing: ' + '; '.join(missing)) if missing else ''))
        if not good and p.returncode != 0:
            print('    stderr tail: ' + '\n    '.join(
                (p.stderr or p.stdout).splitlines()[-6:]))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
