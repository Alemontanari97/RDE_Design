"""(xiv) Rigor carrier, --rigor tier — the P-A dual-route conservative check.

Runs validation/p2_pA1_symbolic_adjoint.py (registry ID X-P2A1): the
independent verification of Prop. A2 in CONSERVATIVE variables
(Grueneisen EOS-general closure, exact Weierstrass zeros, rank-3
certificate, executable (L.20) bookkeeping, boundary-data reading
lemma; three negative controls inside). Measured runtime of record
44.7 s (S9; S8 measured 51.0 s) — beyond the fast-tier budget, hence
the DECLARED rigor tier of run_all.py ([F1/SCAFFOLD-M] task M-5):
executed in every full run, skipped by --fast.

ACCEPTANCE: exit code 0 AND the literal "VERDICT: PASS" in stdout;
rejection channels as in tests/test_rigor_carriers.py.

Usage:
    python tests/test_rigor_dualroute.py
"""
import sys

from test_rigor_carriers import run_carrier


def run():
    ok, dt, tail = run_carrier('X-P2A1', 'validation/p2_pA1_symbolic_adjoint.py')
    print('  %-6s %-42s %s (%.1f s)'
          % ('X-P2A1', 'p2_pA1_symbolic_adjoint.py', 'PASS' if ok else 'FAIL',
             dt))
    if not ok:
        for ln in tail:
            print('         %s' % ln)
    print('  %-52s %s'
          % ('dual-route conservative carrier (rigor tier)',
             'PASS' if ok else 'FAIL'))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
