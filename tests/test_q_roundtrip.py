"""(iv) q~ round-trip: M_CJ -> q~ -> M_CJ exact inversion (Paper B Eq. 2).

The pair (m_cj, h_inv) of src/cycles: M = sqrt(H+1)+sqrt(H) and
H = (M^2-1)^2/(4 M^2) are exact inverses.  Asserted at:
  * the spec benchmark (gamma = 1.4, q~ = 4 -> M_CJ = 4.599 -> q~ back);
  * the 12 shipped physical M_CJ values (data/q_mapping.json).
Tolerance TOL['qtilde_roundtrip'] = 1e-6 (measured: machine epsilon).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src.common.constants import TOL
from src.cycles.q_mapping import h_inv, m_cj


def run():
    ok = True

    # spec benchmark
    g, qt = 1.4, 4.0
    M = m_cj(0.5 * (g + 1.0) * qt)
    qt_back = h_inv(M) * 2.0 / (g + 1.0)
    err = abs(qt_back / qt - 1.0)
    good = err <= TOL['qtilde_roundtrip'] and abs(M - 4.599) < 5e-3
    ok &= good
    print('  benchmark g=1.4 q~=4: M_CJ=%.4f  roundtrip err %.2e  %s'
          % (M, err, 'PASS' if good else 'FAIL'))

    # 12 shipped mixtures
    rows = json.load(open(os.path.join(ROOT, 'data', 'q_mapping.json'))
                     )['mixtures']
    worst = 0.0
    for r in rows:
        M0 = r['M_CJ']
        M1 = float(m_cj(h_inv(M0)))
        worst = max(worst, abs(M1 / M0 - 1.0))
    good = worst <= TOL['qtilde_roundtrip']
    ok &= good
    print('  12 mixtures M->q~->M: worst rel err %.2e  %s'
          % (worst, 'PASS' if good else 'FAIL'))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
