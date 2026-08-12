"""(xv) Claims-registry lint — theory-as-code, ENFORCED ([F1/SCAFFOLD-M] M-2).

The registry docs/claims_registry.yaml is the typed INDEX of the theory
corpus (SCAFFOLD §2). This lint makes drift MACHINE-REJECTED, mirroring
the numeric lint (vii) for claims:

  (a) PARSE: strict declared YAML subset (see the registry header);
      any unparsed line is an error. If PyYAML happens to be installed
      the file is ALSO parsed with it and the two parses must agree
      (dual-route; skipped with a declared note when absent).
  (b) REFERENCES: every entry's doc/proof "path#anchor" resolves (path
      exists; anchor is a literal substring of the file); every carrier
      ID resolves to a kind: carrier entry; every inherits ID resolves
      to a kind: conditional entry; IDs unique.
  (c) SUITE MEMBERSHIP + THE TYPED ONDEMAND FIELD (C4 closure of
      record, S25 2026-08-12 — replaces the historical scope-substring
      exemption): every kind: carrier entry carries `ondemand`
      (REQUIRED on carriers, FORBIDDEN elsewhere). ondemand: "no" =>
      the carrier must be IN THE SUITE (tests/ scripts registered in
      run_all.py; validation/ scripts invoked by a registered tests
      module). Otherwise the value must match the STRICT spec
      "env=<jax|gfortran|jax+geno>; pass=YYYY-MM-DD; suite=<none|...>"
      and the STALENESS LINK is enforced: the last git commit date
      touching the carrier file must be <= the pass date (day
      granularity, declared), else VIOLATION — editing a carrier
      without re-running its gate and re-dating pass turns this lint
      RED. Uncommitted carrier files are a violation outright.
      git-unavailable hosts get a declared skip note (the ONDEMAND
      tier of run_all.py re-checks on execution hosts).
  (d) SCHEMA: exact field set per entry; kind/class/gamma/suffices
      enums; class THEOREM* => nonempty inherits; kind theorem with
      suffices_symbolic yes => nonempty carrier; every entry has a
      nonempty falsifier and a gamma tag; gamma/suffices "n/a" only
      where declared legal (never on mathematical kinds).
  (e) ORPHANS: every bracketed registry-shaped ID cited in docs/*.md
      (spine tags like "[T-T3]") must exist in the registry.

REJECTOR, DEMONSTRATED ON EVERY RUN: after the real registry passes,
four violations are seeded IN-MEMORY (THEOREM* stripped of inherits;
symbolic-sufficient theorem stripped of carrier; dangling anchor;
stale ondemand pass-of-record date — skipped with a declared note on
git-unavailable hosts) and the checker MUST reject each — if any
seeded violation slips through, this group FAILS. Nothing is written
to disk.

Usage:
    python tests/test_claims_lint.py
"""
import copy
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, 'docs', 'claims_registry.yaml')
RUN_ALL = os.path.join(ROOT, 'tests', 'run_all.py')
DOCS_DIR = os.path.join(ROOT, 'docs')

FIELDS = ('id', 'kind', 'class', 'scope', 'statement', 'doc', 'proof',
          'inherits', 'carrier', 'suffices_symbolic', 'falsifier', 'gamma')
LIST_FIELDS = ('inherits', 'carrier')
KINDS = ('theorem', 'definition', 'conditional', 'conjecture', 'schema',
         'carrier', 'oracle', 'directive', 'paper')
CLASSES = ('THEOREM', 'THEOREM*', 'SCHEMA', 'CONJECTURE', 'PRACTICE')
GAMMAS = ('EOS-general', 'gamma-const-oracle', 'perfect-gas-oracle', 'n/a')
SUFFICES = ('yes', 'no', 'n/a')
# gamma/suffices "n/a" is legal ONLY on non-mathematical kinds:
NA_KINDS = ('directive', 'paper', 'carrier', 'oracle', 'definition')
MATH_KINDS = ('theorem', 'conditional', 'conjecture', 'schema')
# Typed ondemand spec (C4 closure; carrier-only field, see docstring (c)):
ODSPEC_RX = re.compile(r'^env=(jax|gfortran|jax\+geno); '
                       r'pass=(\d{4}-\d{2}-\d{2}); suite=(none|\S.*)$')
ID_RX = re.compile(r'\[((?:T|D|C|S|J|X|O|DIR|PAP)-[A-Za-z0-9-]+)\]')

_GIT_DATES = {}          # memo: relpath -> (date_or_None, note)


def carrier_last_commit(relpath):
    """Day-granular date (%cs) of the last commit touching relpath.

    Returns (date, '') on success; (None, note) with note in
    {'no committed history', 'git unavailable'} otherwise. Memoized:
    the seeded-rejector demos re-run check() several times per lint
    run and must not multiply subprocess cost.
    """
    if relpath not in _GIT_DATES:
        try:
            out = subprocess.run(
                ['git', '-C', ROOT, 'log', '-1', '--format=%cs',
                 '--', relpath],
                capture_output=True, text=True, timeout=60)
            date = out.stdout.strip()
            if out.returncode == 0 and re.match(r'^\d{4}-\d{2}-\d{2}$',
                                                date):
                _GIT_DATES[relpath] = (date, '')
            elif out.returncode == 0:
                _GIT_DATES[relpath] = (None, 'no committed history')
            else:
                _GIT_DATES[relpath] = (None, 'git unavailable')
        except OSError:
            _GIT_DATES[relpath] = (None, 'git unavailable')
    return _GIT_DATES[relpath]


def parse_registry(text):
    """Strict-subset parse -> list of entry dicts. Raises ValueError."""
    entries, cur = [], None
    for n, ln in enumerate(text.splitlines(), 1):
        if re.match(r'^\s*(#|$)', ln) or ln.strip() == 'entries:':
            continue
        m = re.match(r'^- id:\s*(\S+)\s*$', ln)
        if m:
            cur = {'id': m.group(1)}
            entries.append(cur)
            continue
        m = re.match(r'^  (\w+): (.*)$', ln)
        if not m or cur is None:
            raise ValueError('line %d not in the declared subset: %r'
                             % (n, ln))
        k, v = m.group(1), m.group(2).strip()
        if v.startswith('['):
            if not v.endswith(']'):
                raise ValueError('line %d: unterminated list' % n)
            items = [x.strip() for x in v[1:-1].split(',') if x.strip()]
            cur[k] = [x[1:-1] if re.match(r'^".*"$', x) else x
                      for x in items]
        elif re.match(r'^".*"$', v):
            cur[k] = v[1:-1]
        elif re.match(r'^\S+$', v):
            cur[k] = v
        else:
            raise ValueError('line %d: scalar must be quoted or one '
                             'token: %r' % (n, v))
    return entries


def _resolve(ref):
    """(exists, anchor_ok) for a "path#anchor" reference."""
    path, _, anchor = ref.partition('#')
    full = os.path.join(ROOT, path.replace('/', os.sep))
    if not os.path.isfile(full):
        return False, False
    if not anchor:
        return True, True
    body = io.open(full, encoding='utf-8', errors='replace').read()
    return True, anchor in body


def _suite_sources():
    """(run_all source, {registered test module: source text})."""
    run_src = io.open(RUN_ALL, encoding='utf-8').read()
    mods = {}
    for m in re.finditer(r"'(test_\w+)'", run_src):
        p = os.path.join(ROOT, 'tests', m.group(1) + '.py')
        if os.path.isfile(p):
            mods[m.group(1)] = io.open(p, encoding='utf-8').read()
    return run_src, mods


def check(entries, suite=None):
    """Return the list of violation strings for a parsed entry list."""
    v = []
    byid = {}
    for e in entries:
        if e['id'] in byid:
            v.append('duplicate id %s' % e['id'])
        byid[e['id']] = e
    run_src, mods = suite if suite else _suite_sources()
    for e in entries:
        eid = e.get('id', '?')
        # (d) schema — ondemand is REQUIRED on carriers, FORBIDDEN elsewhere
        req = FIELDS + (('ondemand',) if e.get('kind') == 'carrier' else ())
        missing = [f for f in req if f not in e]
        extra = [f for f in e if f not in req]
        if missing or extra:
            v.append('%s: fields missing %s / extra %s'
                     % (eid, missing, extra))
            continue
        for f in LIST_FIELDS:
            if not isinstance(e[f], list):
                v.append('%s: %s must be a list' % (eid, f))
        if e['kind'] not in KINDS:
            v.append('%s: bad kind %r' % (eid, e['kind']))
        if e['class'] not in CLASSES:
            v.append('%s: bad class %r' % (eid, e['class']))
        if e['gamma'] not in GAMMAS:
            v.append('%s: bad gamma %r' % (eid, e['gamma']))
        if e['suffices_symbolic'] not in SUFFICES:
            v.append('%s: bad suffices_symbolic %r'
                     % (eid, e['suffices_symbolic']))
        if e['kind'] in MATH_KINDS and e['gamma'] == 'n/a':
            v.append('%s: gamma n/a illegal on mathematical kind %s'
                     % (eid, e['kind']))
        if e['kind'] == 'theorem' and e['suffices_symbolic'] == 'n/a':
            v.append('%s: suffices_symbolic n/a illegal on a theorem' % eid)
        if not e['falsifier'].strip():
            v.append('%s: empty falsifier' % eid)
        if not e['statement'].strip():
            v.append('%s: empty statement' % eid)
        if e['class'] == 'THEOREM*' and not e['inherits']:
            v.append('%s: THEOREM* with empty inherits' % eid)
        if (e['kind'] == 'theorem' and e['suffices_symbolic'] == 'yes'
                and not e['carrier']):
            v.append('%s: symbolic-sufficient theorem without carrier' % eid)
        # (b) references
        for f in ('doc', 'proof'):
            ok_path, ok_anchor = _resolve(e[f])
            if not ok_path:
                v.append('%s: %s path missing: %s' % (eid, f, e[f]))
            elif not ok_anchor:
                v.append('%s: %s anchor unresolved: %s' % (eid, f, e[f]))
        for cid in e['carrier']:
            t = byid.get(cid)
            if t is None or t.get('kind') != 'carrier':
                v.append('%s: carrier ref %s not a carrier entry'
                         % (eid, cid))
        for cid in e['inherits']:
            t = byid.get(cid)
            if t is None or t.get('kind') != 'conditional':
                v.append('%s: inherits ref %s not a conditional entry'
                         % (eid, cid))
        # (c) suite membership + typed ondemand for carrier entries
        if e['kind'] == 'carrier':
            path = e['doc'].partition('#')[0]
            base = os.path.basename(path)
            mod = base[:-3] if base.endswith('.py') else base
            od = e['ondemand']
            if od != 'no':
                m = ODSPEC_RX.match(od if isinstance(od, str) else '')
                if not m:
                    v.append('%s: malformed ondemand spec %r' % (eid, od))
                else:
                    last, note = carrier_last_commit(path)
                    if note == 'no committed history':
                        v.append('%s: ondemand carrier file %s has no '
                                 'committed history' % (eid, path))
                    elif last is not None and last > m.group(2):
                        v.append('%s: STALE ondemand pass-of-record %s < '
                                 'last commit %s touching %s'
                                 % (eid, m.group(2), last, path))
                    # note 'git unavailable' -> declared skip (run() prints)
            elif path.startswith('tests/'):
                if "'%s'" % mod not in run_src:
                    v.append('%s: tests module %s not registered in '
                             'run_all.py' % (eid, mod))
            elif path.startswith('validation/'):
                if not any(base in src for src in mods.values()):
                    v.append('%s: validation script %s not invoked by any '
                             'registered suite module' % (eid, base))
            else:
                v.append('%s: carrier path outside tests/ and validation/: '
                         '%s' % (eid, path))
    return v


def check_orphans(byids):
    """(e) bracketed registry-shaped IDs cited in docs/*.md must exist."""
    v = []
    for f in sorted(os.listdir(DOCS_DIR)):
        if not f.endswith('.md'):
            continue
        body = io.open(os.path.join(DOCS_DIR, f), encoding='utf-8',
                       errors='replace').read()
        for m in ID_RX.finditer(body):
            if m.group(1) not in byids:
                v.append('%s cites unknown ID [%s]' % (f, m.group(1)))
    return sorted(set(v))


def dual_route_parse(text, entries):
    """Optional PyYAML cross-check; returns (ran, ok, msg)."""
    try:
        import yaml
    except ImportError:
        return False, True, 'PyYAML absent (declared: subset parser is primary)'
    data = yaml.safe_load(text)
    ye = data.get('entries', [])
    if len(ye) != len(entries):
        return True, False, 'entry count %d != %d' % (len(ye), len(entries))
    for a, b in zip(entries, ye):
        for f in FIELDS + ('ondemand',):
            if a.get(f) != b.get(f):
                return True, False, '%s field %s differs' % (a.get('id'), f)
    return True, True, 'PyYAML dual-route parse agrees'


def seeded_rejector_demo(entries, suite):
    """(e) three in-memory violations must each be REJECTED. Returns ok."""
    demos = []
    # 1: strip inherits from the first THEOREM* entry
    m1 = copy.deepcopy(entries)
    t = next(e for e in m1 if e['class'] == 'THEOREM*')
    t['inherits'] = []
    demos.append(('THEOREM* stripped of inherits (%s)' % t['id'], m1))
    # 2: strip carrier from a symbolic-sufficient theorem
    m2 = copy.deepcopy(entries)
    t = next(e for e in m2 if e['kind'] == 'theorem'
             and e['suffices_symbolic'] == 'yes')
    t['carrier'] = []
    demos.append(('symbolic-sufficient theorem stripped of carrier (%s)'
                  % t['id'], m2))
    # 3: dangling anchor
    m3 = copy.deepcopy(entries)
    m3[0]['doc'] = 'docs/rde_nozzle_MASTER.md#NO SUCH ANCHOR 9c1f'
    demos.append(('dangling anchor seeded (%s)' % m3[0]['id'], m3))
    # 4: stale ondemand pass-of-record (staleness rejector must fire);
    #    declared skip when git is unavailable on this host
    t = next(e for e in entries if e.get('kind') == 'carrier'
             and e.get('ondemand', 'no') != 'no')
    probe_path = t['doc'].partition('#')[0]
    if carrier_last_commit(probe_path)[1] != 'git unavailable':
        m4 = copy.deepcopy(entries)
        t4 = next(e for e in m4 if e['id'] == t['id'])
        t4['ondemand'] = re.sub(r'pass=\d{4}-\d{2}-\d{2}',
                                'pass=1999-01-01', t4['ondemand'])
        demos.append(('stale ondemand pass date seeded (%s)' % t['id'], m4))
    else:
        print('  [rejector] stale-ondemand demo SKIPPED '
              '(declared: git unavailable on this host)')
    ok = True
    for label, mutated in demos:
        rejected = bool(check(mutated, suite))
        ok &= rejected
        print('  [rejector] %-58s %s'
              % (label, 'REJECTED (PASS)' if rejected else 'ACCEPTED (FAIL)'))
    return ok


def run():
    text = io.open(REGISTRY, encoding='utf-8').read()
    try:
        entries = parse_registry(text)
    except ValueError as e:
        print('  PARSE ERROR: %s' % e)
        return False
    suite = _suite_sources()
    violations = check(entries, suite)
    violations += check_orphans({e['id'] for e in entries})
    for msg in violations[:40]:
        print('  VIOLATION: %s' % msg)
    kinds = {}
    for e in entries:
        kinds[e.get('kind', '?')] = kinds.get(e.get('kind', '?'), 0) + 1
    print('  parsed %d entries: %s'
          % (len(entries), ', '.join('%s %d' % kv
                                     for kv in sorted(kinds.items()))))
    ran, dr_ok, dr_msg = dual_route_parse(text, entries)
    print('  dual-route: %s' % dr_msg)
    rej_ok = seeded_rejector_demo(entries, suite)
    ok = not violations and dr_ok and rej_ok
    print('  %-52s %s (%d violations)'
          % ('claims lint: registry coherent + rejector proven',
             'PASS' if ok else 'FAIL', len(violations)))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
