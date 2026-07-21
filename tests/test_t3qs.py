"""(xvi) T3-QS sweep-protection carrier — CI harness ([F4-prep/T3QS], S12).

Runs validation/t3qs_sweep_protection.py (registry X-T3QS): the
symbolic proof chain P1-P6 of theorem T-T3QS (quasi-steady protection
of the collapse class — first-order sweep correction vanishes on the
smooth part of ray cycles, concentrates at the wave-passage jump;
EOS-general, arbitrary caloric e(T)) with three built-in rejectors
(non-ray direction, H3 violation, non-affine objective). Measured
runtime of record: 8.6 s clean host (29.1 s first run under load) —
fast tier.

ACCEPTANCE: exit 0 AND literal "VERDICT: PASS" (harness contract of
tests/test_rigor_carriers.py, reused).

Usage:
    python tests/test_t3qs.py
"""
import sys

from test_rigor_carriers import run_carrier


def run():
    ok, dt, tail = run_carrier('X-T3QS', 'validation/t3qs_sweep_protection.py')
    print('  %-7s %-41s %s (%.1f s)'
          % ('X-T3QS', 't3qs_sweep_protection.py', 'PASS' if ok else 'FAIL',
             dt))
    if not ok:
        for ln in tail:
            print('         %s' % ln)
    print('  %-52s %s'
          % ('T3-QS proof chain P1-P6 + rejectors R1-R3',
             'PASS' if ok else 'FAIL'))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
