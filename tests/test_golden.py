"""(v) Golden numbers — the blessed values, EXACT at their display precision.

Shipped-data goldens (data/*.json are the validated build artifacts):
  U_CJ(H2/air, 1 atm, 300 K)   = 1969.0 m/s   (thrust_models_all.json)
  U_CJ(C2H4/O2, 1 atm, 300 K)  = 2373.5 m/s   (thrust_models_all.json)
  Stechmann H2/O2 Isp(sl,e=1)  = 237.1 s      (thrust_models_all.json)
  eta_FJ(CH4/air, 1 bar,300 K) = 0.300        (cycles_ws.json)

Regenerated-report goldens (run the owning module, parse its output):
  stechmann_nozzle validate    -> '18/18 rows PASS'
  tables (V&V verdicts)        -> 8/8 PASS (one PASS* with documented anomaly)
  q_mapping                    -> M_CJ recompute dev 0.00%

The live examples + design study (1969.0 / 2373.5 / 245.3 / OK) are exercised
by tests/test_examples.py (slow tier of tests/run_all.py).
"""
import io
import json
import os
import sys
import contextlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def run():
    ok = True

    def check(name, cond, detail=''):
        nonlocal ok
        ok &= bool(cond)
        print('  %-44s %s %s' % (name, 'PASS' if cond else 'FAIL', detail))

    T = json.load(open(os.path.join(ROOT, 'data', 'thrust_models_all.json')))['cases']
    C = json.load(open(os.path.join(ROOT, 'data', 'cycles_ws.json')))['fj_mixtures']

    check('U_CJ(H2/air) == 1969.0 [shipped]',
          round(T['H2/air']['cj']['UCJ'], 1) == 1969.0,
          '(%.4f)' % T['H2/air']['cj']['UCJ'])
    check('U_CJ(C2H4/O2) == 2373.5 [shipped]',
          round(T['C2H4/O2']['cj']['UCJ'], 1) == 2373.5,
          '(%.4f)' % T['C2H4/O2']['cj']['UCJ'])
    check('Stechmann H2/O2 Isp == 237.1 [shipped]',
          round(T['H2/O2']['stech']['Isp_sl_e1'], 1) == 237.1,
          '(%.4f)' % T['H2/O2']['stech']['Isp_sl_e1'])
    check("eta_FJ(CH4/air) == '0.300' [shipped]",
          '%.3f' % C['CH4/air']['eta_FJ'] == '0.300',
          '(%.6f)' % C['CH4/air']['eta_FJ'])

    # ---- 18/18: stechmann_nozzle validate (reads cached states) -----------
    from src.thrust import stechmann_nozzle as stn
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        stn.validate()
    check("stechmann validate -> '18/18 rows PASS'",
          '18/18 rows PASS' in buf.getvalue())

    # ---- 8/8: tables V&V verdicts ------------------------------------------
    from src.thrust import tables
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        tables.main()
    out = buf.getvalue()
    verd = [ln for ln in out.splitlines()
            if ln.split() and ln.split()[0].rstrip('*').replace('_', '').startswith(
                ('1', '2', '3a', '3b', '3c', '4', '5', '6'))
            and ('PASS' in ln or 'FAIL' in ln)]
    npass = sum(1 for ln in verd if ' PASS' in ln and ' FAIL' not in ln)
    check('tables V&V verdicts 8/8 PASS', npass == 8 and len(verd) == 8,
          '(%d/%d)' % (npass, len(verd)))

    # ---- q_mapping: M_CJ recompute 0.00% -----------------------------------
    from src.cycles import q_mapping
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        q_mapping.main()
    check("q_mapping 'max M_CJ recompute dev = 0.00%'",
          'max M_CJ recompute dev = 0.00%' in buf.getvalue())

    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
