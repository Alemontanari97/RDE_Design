"""(xviii) Interval-certificate carrier [X-IVXC] — RIGOR TIER.

Runs the S-XCONV box certificate (validation/
ivxc_interval_certificate.py) as a subprocess, exactly as a human
would: outward-rounded interval arithmetic, Krawczyk verified solve,
mean-value form on the (M,V) slice, interval LDL^T, deterministic
adaptive bisection; the T-XRED 4D->2D reduction identities are
verified symbolically inside the carrier. Measured runtime of record:
59.3 s (S15, 2026-08-05) — rigor tier (skipped by --fast), same
placement rationale as group (xiv).

ACCEPTANCE: exit code 0 AND the literal line "VERDICT: PASS".
Rejection channels: missing script, nonzero exit, missing verdict.
The scientific rejectors live INSIDE the carrier (R1 subsonic box,
R2 corrupted diagonal, R3 containment, R4 corrupted group diagonal).

Usage:
    python tests/test_rigor_interval.py
"""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'validation', 'ivxc_interval_certificate.py')
VERDICT_LINE = 'VERDICT: PASS'


def run():
    if not os.path.exists(SCRIPT):
        print('  MISSING SCRIPT: %s' % SCRIPT)
        return False
    t0 = time.time()
    proc = subprocess.run([sys.executable, SCRIPT], capture_output=True,
                          text=True, cwd=ROOT)
    dt = time.time() - t0
    ok = proc.returncode == 0 and any(
        VERDICT_LINE in ln for ln in (proc.stdout or '').splitlines())
    print('  X-IVXC ivxc_interval_certificate.py  %s (%.1f s)'
          % ('PASS' if ok else 'FAIL', dt))
    if not ok:
        for ln in (proc.stdout or '').strip().splitlines()[-4:]:
            print('    %s' % ln)
        if proc.returncode != 0:
            print('    exit code %d' % proc.returncode)
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
