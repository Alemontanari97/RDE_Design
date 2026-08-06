"""(xiii) Rigor carriers, fast tier — the symbolic proof layer, CI-EXECUTED.

Promotes the machine-verification carriers of the theory registry
(docs/claims_registry.yaml) from on-demand validation/ scripts into the
suite ([F1/SCAFFOLD-M] task M-5). Fast tier = the carriers whose
measured runtime is seconds-scale (S9 measurements of record:
pa1 3.3 s, g12 1.4 s, n6 2.6 s, 5F 1.6 s; slrw ~4 s + xbvp ~2 s
added S15; u3bd sub-second + acfr 1.4 s added S16;
the 44.7 s dual-route carrier lives in the (xiv) rigor tier,
tests/test_rigor_dualroute.py).

Each carrier is run as a subprocess exactly as a human would run it.
ACCEPTANCE per carrier: exit code 0 AND the literal terminal line
"VERDICT: PASS" in its stdout. REJECTION channels (this module can
fail): missing script, nonzero exit, missing/failed verdict line.
The scientific rejectors live INSIDE the carriers (each ships its own
negative controls, of record in the registry entries X-PA1, X-G12,
X-N6, X-5F); this module is their CI harness, not their proof.

Usage:
    python tests/test_rigor_carriers.py
"""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (registry ID, script) — fast tier per the S9 runtime measurements.
CARRIERS = [
    ('X-PA1', 'validation/pa1_symbolic_lemmaA.py'),
    ('X-G12', 'validation/g12_shock_linearization.py'),
    ('X-N6',  'validation/n6_swirl_kernel.py'),
    ('X-5F',  'validation/n6_fivefield_adjoint.py'),
    ('X-SLRW', 'validation/side_load_rotating_lemma.py'),
    ('X-XBVP', 'validation/xbvp_entropy_transfer.py'),
    ('X-U2RG', 'validation/u2_reflection_glancing.py'),
    ('X-U3BD', 'validation/u3_bordered_front_solve.py'),
    ('X-ACFR', 'validation/acontraction_front_probe.py'),
]

VERDICT_LINE = 'VERDICT: PASS'


def run_carrier(rid, rel):
    """Run one carrier; return (ok, seconds, last_lines)."""
    full = os.path.join(ROOT, rel)
    if not os.path.exists(full):
        return False, 0.0, ['MISSING SCRIPT: %s' % rel]
    t0 = time.time()
    proc = subprocess.run([sys.executable, full], capture_output=True,
                          text=True, cwd=ROOT)
    dt = time.time() - t0
    tail = (proc.stdout or '').strip().splitlines()[-3:]
    ok = proc.returncode == 0 and any(VERDICT_LINE in ln for ln in
                                      (proc.stdout or '').splitlines())
    if proc.returncode != 0:
        tail += ['exit code %d' % proc.returncode]
        tail += (proc.stderr or '').strip().splitlines()[-3:]
    return ok, dt, tail


def run():
    all_ok = True
    for rid, rel in CARRIERS:
        ok, dt, tail = run_carrier(rid, rel)
        all_ok &= ok
        print('  %-6s %-42s %s (%.1f s)'
              % (rid, os.path.basename(rel), 'PASS' if ok else 'FAIL', dt))
        if not ok:
            for ln in tail:
                print('         %s' % ln)
    print('  %-52s %s (%d carriers)'
          % ('rigor carriers fast tier: exit 0 + verdict line each',
             'PASS' if all_ok else 'FAIL', len(CARRIERS)))
    return all_ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
