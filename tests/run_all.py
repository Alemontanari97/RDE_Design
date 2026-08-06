#!/usr/bin/env python3
"""run_all.py — the package coherence & non-regression suite (simple runner).

    python tests/run_all.py           # everything: fast + rigor + slow tiers
    python tests/run_all.py --fast    # fast tier only (skip rigor + slow)

Tiers ([F1/SCAFFOLD-M] M-5): FAST = seconds-scale groups, always run;
RIGOR = the declared rigor tier (registry carriers beyond the fast
budget; measured runtimes in each module's docstring), run in every
full/CI run, skipped by --fast; SLOW = live examples subprocesses.

Tests (see each module's docstring):
  (i)    test_cj_coherence      one CJ from all canonical paths (<=1e-9 rel)
                                + independent solvers within 2e-3
  (ii)   test_stechmann_collapse blowdown -> steady CP identity (<=1e-6)
  (iii)  test_axial_bound       SK axial sonic vs independent eq. bound (~0%)
  (iv)   test_q_roundtrip       M_CJ -> q~ -> M_CJ exact inversion (<=1e-6)
  (v)    test_golden            blessed digits from shipped data + reports
  (vi)   test_bell_optimality   executable eps-optimality proofs (Euler lemma,
                                stationarity/globality, averaging discrimination)
  (vii)  test_numeric_lint      no-magic-number invariant: every src/ literal
                                classified in validation/numeric_allowlist.json
  (viii) test_bounds            OP-0 eps-level bound ladder (sonic cap)
  (ix)   test_gamma_probe       A0.3 gamma-channel probe
  (x)    test_phase_diagram     OP-11-eps phase diagram
  (xi)   test_bounds_gamma      OP-0-gamma real-thermo ceiling
  (xii)  test_phase_diagram_real OP-11 real-route diagram + eq bracket
  (xiii) test_rigor_carriers    registry rigor carriers, fast eight
                                (X-PA1, X-G12, X-N6, X-5F, X-SLRW,
                                X-XBVP, X-U2RG, X-U3BD)
  (xiv)  test_rigor_dualroute   X-P2A1 dual-route carrier [rigor tier]
  (xviii) test_rigor_interval   X-IVXC interval certificate (S-XCONV
                                box + T-XRED reduction) [rigor tier]
  (xv)   test_claims_lint       claims-registry lint (theory-as-code):
                                anchors, suite membership, schema, orphans;
                                seeded-violation rejector proven every run
  (xvi)  test_t3qs              T3-QS sweep-protection proof chain P1-P6
                                (ray family => J1 smooth-part = 0) + R1-R3
        test_examples [slow]    live examples + design study, digits EXACT

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
        ('(x)   OP-11-eps phase diagram', 'test_phase_diagram'),
        ('(xi)  OP-0-gamma real-thermo ceiling', 'test_bounds_gamma'),
        ('(xii) OP-11 real-route diagram + eq bracket',
         'test_phase_diagram_real'),
        ('(xiii) rigor carriers (symbolic, fast eight)',
         'test_rigor_carriers'),
        ('(xv)  claims registry lint', 'test_claims_lint'),
        ('(xvi) T3-QS sweep-protection carrier', 'test_t3qs')]
RIGOR = [('(xiv) P-A dual-route carrier [rigor tier]',
          'test_rigor_dualroute'),
         ('(xviii) X-IVXC interval certificate [rigor tier]',
          'test_rigor_interval')]
SLOW = [('(v+)  live examples & design study', 'test_examples')]


def main(argv):
    tests = FAST + ([] if '--fast' in argv else RIGOR + SLOW)
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
