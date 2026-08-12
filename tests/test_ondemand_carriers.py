"""(xvii) On-demand carrier tier — the C4 closure of record (S25,
2026-08-12; audit row test-suite:ondemand-carrier-exclusion, CONFIRMED
high; written S24 placement).

REGISTRY-DRIVEN, no hardcoded carrier list (generality directive):
every kind: carrier entry of docs/claims_registry.yaml whose typed
`ondemand` field carries a spec "env=...; pass=...; suite=..." is
processed here on every FULL suite run (--fast skips this tier):

  (1) STALENESS LINK re-check: the day-granular date of the last git
      commit touching the carrier file must be <= the recorded
      PASS-of-record date (shared helper with the claims lint, which
      also enforces this as a lint violation with a seeded rejector);
      a STALE carrier FAILS this group. git-unavailable hosts get a
      declared skip note on the staleness column only.
  (2) ENV-CONDITIONAL EXECUTION: carriers whose spec declares an
      affordable suite self-check (suite != none) run as a subprocess
      when their declared env is available on THIS host (jax =
      importable jax; gfortran = gfortran on PATH; jax+geno = jax +
      GENO/ tree + wsl on PATH), gated on EXIT CODE 0 (output
      captured in-process, no shell pipes in the verdict path). Env
      unavailable => declared SKIP row, never a silent pass.
  (3) ACCOUNTING: suite=none carriers (decisive-run-scale, manual
      protocol runs only) print an accounted row (env availability +
      pass-of-record date + staleness verdict).

HONEST SCOPE (replaces the S21 "carrier-exclusive" annotation, which
falls WITH this closure): for suite=none carriers this tier verifies
ACCOUNTING and STALENESS, not re-execution — their PASS-of-record
numbers rest on the dated manual protocol runs in the registry scopes
and session logs; the staleness link is the machine channel that
fires when such a carrier's file drifts past its recorded PASS.

Group verdict: PASS iff no stale carrier, no malformed spec, and
every executed suite self-check exits 0.

Usage:
    python tests/test_ondemand_carriers.py
"""
import io
import os
import shlex
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import test_claims_lint as lint

# Per-carrier subprocess budget for declared suite self-checks. Not a
# tolerance: a generous hard backstop against hangs (the declared
# affordability bar for wiring suite != none is far below it); a
# timeout is reported as FAIL with a loud row.
SUITE_TIMEOUT_S = 900


def _env_available(env):
    """(available, note) for a declared env token of the ondemand spec."""
    def has_jax():
        try:
            import importlib.util
            return importlib.util.find_spec('jax') is not None
        except Exception:
            return False
    if env == 'jax':
        ok = has_jax()
        return ok, 'jax importable' if ok else 'jax not importable'
    if env == 'gfortran':
        from shutil import which
        ok = which('gfortran') is not None
        return ok, 'gfortran on PATH' if ok else 'gfortran not on PATH'
    if env == 'jax+geno':
        from shutil import which
        parts = []
        ok = has_jax()
        parts.append('jax' if ok else 'NO jax')
        g = os.path.isdir(os.path.join(ROOT, 'GENO'))
        parts.append('GENO/' if g else 'NO GENO/')
        w = which('wsl') is not None
        parts.append('wsl' if w else 'NO wsl')
        return ok and g and w, '+'.join(parts)
    return False, 'unknown env token %r' % env


def run():
    text = io.open(lint.REGISTRY, encoding='utf-8').read()
    entries = lint.parse_registry(text)
    rows = [e for e in entries if e.get('kind') == 'carrier'
            and e.get('ondemand', 'no') != 'no']
    ok = True
    n_exec = n_acct = n_skip = 0
    for e in rows:
        eid = e['id']
        spec = e['ondemand']
        m = lint.ODSPEC_RX.match(spec)
        if not m:
            print('  [FAIL] %-8s malformed ondemand spec %r' % (eid, spec))
            ok = False
            continue
        env, passd, suite = m.group(1), m.group(2), m.group(3)
        path = e['doc'].partition('#')[0]
        # (1) staleness link (shared helper; lint enforces too)
        last, note = lint.carrier_last_commit(path)
        if note == 'git unavailable':
            stale_txt = 'staleness SKIP (declared: git unavailable)'
        elif note == 'no committed history':
            stale_txt = 'STALE (no committed history)'
            ok = False
        elif last > passd:
            stale_txt = 'STALE (last commit %s > pass %s)' % (last, passd)
            ok = False
        else:
            stale_txt = 'fresh (pass %s >= last commit %s)' % (passd, last)
        # (2)/(3) env-conditional execution or accounting
        avail, env_txt = _env_available(env)
        if suite == 'none':
            n_acct += 1
            print('  [acct] %-8s %-42s env=%s(%s) %s'
                  % (eid, path, env, env_txt, stale_txt))
            continue
        if not avail:
            n_skip += 1
            print('  [SKIP] %-8s declared suite check NOT run — env=%s '
                  'unavailable (%s); %s' % (eid, env, env_txt, stale_txt))
            continue
        argv = [] if suite == 'default' else shlex.split(suite)
        cmd = [sys.executable, os.path.join(ROOT, path)] + argv
        try:
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True,
                               text=True, timeout=SUITE_TIMEOUT_S)
            code = r.returncode
            out = (r.stdout or '') + (('\n' + r.stderr)
                                      if code != 0 and r.stderr else '')
        except subprocess.TimeoutExpired:
            code, out = -1, 'TIMEOUT after %d s' % SUITE_TIMEOUT_S
        n_exec += 1
        good = (code == 0)
        ok &= good
        tail = out.strip().splitlines()[-1:] or ['']
        print('  [%s] %-8s exit=%s %s | %s; %s'
              % ('PASS' if good else 'FAIL', eid, code,
                 'suite=%s' % suite, tail[0][-80:], stale_txt))
        if not good:
            for ln in out.strip().splitlines()[-15:]:
                print('        | %s' % ln)
    print('  ondemand tier: %d executed, %d accounted, %d env-skipped, '
          '%d total' % (n_exec, n_acct, n_skip, len(rows)))
    print('  %-52s %s' % ('ondemand carriers: staleness + env-conditional '
                          'execution', 'PASS' if ok else 'FAIL'))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
