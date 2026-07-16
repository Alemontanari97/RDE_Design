#!/usr/bin/env python3
"""run_all.py — the package coherence & non-regression suite (simple runner).

    python tests/run_all.py           # everything (fast tier + live examples)
    python tests/run_all.py --fast    # skip the slow tier (examples subprocesses)

Tests (see each module's docstring):
  (i)   test_cj_coherence      one CJ from all canonical paths (<=1e-9 rel)
                               + independent solvers within 2e-3
  (ii)  test_stechmann_collapse blowdown -> steady CP identity (<=1e-6)
  (iii) test_axial_bound       SK axial sonic vs independent eq. bound (~0%)
  (iv)  test_q_roundtrip       M_CJ -> q~ -> M_CJ exact inversion (<=1e-6)
  (v)   test_golden            blessed digits from shipped data + reports
  (vi)  test_bell_optimality   executable eps-optimality proofs (Euler lemma,
                               stationarity/globality, averaging discrimination)
  (vii) test_numeric_lint      no-magic-number invariant: every src/ literal
                               classified in validation/numeric_allowlist.json
        test_examples [slow]   live examples + design study, digits EXACT

Every test prints its own evidence lines; this runner adds timing and the
final verdict (exit code 0 iff all PASS).
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

FAST = [('(i)   CJ coherence', 'test_cj_coherence'),
        ('(ii)  Stechmann CP collapse', 'test_stechmann_collapse'),
        ('(iii) SK axial vs eq. bound', 'test_axial_bound'),
        ('(iv)  q~ round-trip', 'test_q_roundtrip'),
        ('(v)   golden numbers', 'test_golden'),
        ('(vi)  bell/spike optimality proofs', 'test_bell_optimality'),
        ('(vii) numeric lint (no magic numbers)', 'test_numeric_lint'),
        ('(viii) OP-0 eps-level bound ladder', 'test_bounds'),
        ('(ix)  A0.3 gamma-channel probe', 'test_gamma_probe'),
        ('(x)   OP-11-eps phase diagram', 'test_phase_diagram')]
SLOW = [('(v+)  live examples & design study', 'test_examples')]


def main(argv):
    tests = FAST + ([] if '--fast' in argv else SLOW)
    results = []
    t00 = time.time()
    for label, mod in tests:
        print('== %s [%s] ==' % (label, mod), flush=True)
        t0 = time.time()
        try:
            ok = __import__(mod).run()
        except Exception as e:
            import traceback
            traceback.print_exc()
            ok = False
            print('  EXCEPTION: %r' % (e,))
        dt = time.time() - t0
        results.append((label, ok, dt))
        print('-> %s (%.1f s)\n' % ('PASS' if ok else 'FAIL', dt), flush=True)
    print('=' * 64)
    npass = sum(1 for _, ok, _ in results if ok)
    for label, ok, dt in results:
        print('%-38s %s (%.1f s)' % (label, 'PASS' if ok else 'FAIL', dt))
    print('%d/%d test groups PASS in %.0f s'
          % (npass, len(results), time.time() - t00))
    return 0 if npass == len(results) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
