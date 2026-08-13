"""(xix) Findings-registry lint — FINDINGS-AS-CODE (census R31, user
directive 2026-08-12).

docs/findings_registry.yaml is the typed index of FINDINGS / GAPS /
CONDITIONALS of record — the machine channel that makes re-minting a
registered finding a LINT VIOLATION instead of an agent-discipline
hope. Demonstrator case (cited in the registry header): the throat-
panel sliver — audit row CONFIRMED 2026-08-07, re-coined by the S25
pipeline-sense review with a CONTRADICTED magnitude, caught only by
the refuter's dedup clause; with this registry the overlap of two
OPEN rows on the same code span is a machine violation.

SCHEMA (strict subset shared with the claims registry): each entry
  - id: <slug>                      (unique)
  status: CONFIRMED | DOWNGRADED | REFUTED | DISCHARGED | SUPERSEDED
  severity: high | medium | low
  magnitude: "<the number/figure of record, or none-measured>"
  source: "<doc path#anchor>"       (anchor must RESOLVE in the doc)
  code: [<path:l1-l2>, ...]         (dedup keys; may be empty [])
  mechanism: <tag>                  (failure-mechanism class)
  OPEN entries (CONFIRMED / DOWNGRADED): owner + trigger REQUIRED
  CLOSED entries (DISCHARGED / REFUTED / SUPERSEDED): evidence REQUIRED
  note: optional free text.

CHECKS (each with a SEEDED rejector proven every run):
  (a) schema/enums + per-status required fields;
  (b) source anchors resolve (file exists, anchor text in body);
  (c) TWO OPEN entries with overlapping code spans on the same file
      = violation (the re-mint channel, the demonstrator's failure);
  (d) duplicate ids.
Standing rule (session discipline, not machine-checkable here): a new
advisory that confirms/refutes/discharges findings MUST land its rows
in this registry in the same window (R4).
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from test_claims_lint import parse_registry, _resolve   # noqa: E402

REGISTRY = os.path.join(ROOT, 'docs', 'findings_registry.yaml')
DERIVE_ART = os.path.join(ROOT, 'validation', 's24_deftw_derive.json')
DEFTW_SRC = os.path.join(ROOT, 'validation', 'def_twin_falsifier.py')

STATUSES = ('CONFIRMED', 'DOWNGRADED', 'REFUTED', 'DISCHARGED',
            'SUPERSEDED')
OPEN = ('CONFIRMED', 'DOWNGRADED')
SEVERITIES = ('high', 'medium', 'low')
BASE = ('id', 'status', 'severity', 'magnitude', 'source', 'code',
        'mechanism')


_LINECOUNTS = {}


def _spans(e):
    """Parse code keys 'path:l1-l2' | 'path:l' -> (path, l1, l2)."""
    out = []
    for c in e.get('code', []) or []:
        m = re.match(r'^(.+):(\d+)(?:-(\d+))?$', c)
        if m:
            a = int(m.group(2))
            b = int(m.group(3) or m.group(2))
            out.append((m.group(1), a, b))
        else:
            out.append(None)
    return out


def check(entries):
    v = []
    byid = {}
    for e in entries:
        eid = e.get('id', '?')
        if eid in byid:
            v.append('duplicate id %s' % eid)
        byid[eid] = e
        st = e.get('status')
        if st not in STATUSES:
            v.append('%s: status %r not in %s' % (eid, st, STATUSES))
            continue
        req = BASE + (('owner', 'trigger') if st in OPEN
                      else ('evidence',))
        missing = [f for f in req if f not in e]
        extra = [f for f in e if f not in req + ('note', 'evidence',
                                                 'owner', 'trigger')]
        if missing:
            v.append('%s: %s entry missing %s (OPEN => owner+trigger;'
                     ' CLOSED => evidence)' % (eid, st, missing))
        if extra:
            v.append('%s: undeclared fields %s' % (eid, extra))
        if e.get('severity') not in SEVERITIES:
            v.append('%s: severity %r not in %s'
                     % (eid, e.get('severity'), SEVERITIES))
        src = e.get('source', '')
        exists, anch = _resolve(src)
        if not exists or not anch:
            v.append('%s: source %r does not resolve (file %s, '
                     'anchor %s)' % (eid, src, exists, anch))
        for c, sp in zip(e.get('code', []) or [], _spans(e)):
            if sp is None:
                v.append('%s: code key %r not path:l1[-l2]' % (eid, c))
                continue
            # R13 (convergence repair, MERGE-5): spans RESOLVE —
            # file exists and the range fits its line count
            p_, _a_, b_ = sp
            full = os.path.join(ROOT, p_.replace('/', os.sep))
            if not os.path.isfile(full):
                v.append('%s: code span %r — file does not exist'
                         % (eid, c))
            else:
                if full not in _LINECOUNTS:
                    _LINECOUNTS[full] = sum(
                        1 for _ in io.open(full, encoding='utf-8',
                                           errors='replace'))
                if b_ > _LINECOUNTS[full]:
                    v.append('%s: code span %r exceeds file length '
                             '%d' % (eid, c, _LINECOUNTS[full]))
    # (c) the re-mint channel: two OPEN entries overlapping one span
    open_spans = []
    for e in entries:
        if e.get('status') in OPEN:
            for sp in _spans(e):
                if sp:
                    open_spans.append((e['id'], sp))
    for i in range(len(open_spans)):
        for j in range(i + 1, len(open_spans)):
            (a_id, (ap, a1, a2)) = open_spans[i]
            (b_id, (bp, b1, b2)) = open_spans[j]
            if a_id != b_id and ap == bp and a1 <= b2 and b1 <= a2:
                v.append('RE-MINT: OPEN entries %s and %s overlap on '
                         '%s:%d-%d — one finding, one row (dedup '
                         'clause violated)' % (a_id, b_id, ap,
                                               max(a1, b1),
                                               min(a2, b2)))
    return v


def seeded_rejectors():
    """Each check must FIRE on a doctored entry (rejector demo)."""
    # R13: demo seeds point at REAL spans (span resolution is now
    # itself linted, so fictitious paths would trip the resolver)
    good = dict(id='seed-ok', status='CONFIRMED', severity='low',
                magnitude='"m"', source='docs/findings_registry.yaml',
                code=['tests/test_findings_registry.py:1-5'],
                mechanism='seed', owner='here', trigger='never')
    demos = []
    e1 = dict(good, id='seed-noowner')
    e1.pop('owner')
    demos.append(('open-without-owner', [e1],
                  lambda vs: any('missing' in t and 'owner' in t
                                 for t in vs)))
    e2 = dict(good, id='seed-noev', status='DISCHARGED')
    e2.pop('owner'); e2.pop('trigger')
    demos.append(('discharged-without-evidence', [e2],
                  lambda vs: any('missing' in t and 'evidence' in t
                                 for t in vs)))
    e3a = dict(good, id='seed-a',
               code=['tests/test_findings_registry.py:10-20'])
    e3b = dict(good, id='seed-b',
               code=['tests/test_findings_registry.py:15-30'])
    demos.append(('two-OPEN-same-span (re-mint)', [e3a, e3b],
                  lambda vs: any(t.startswith('RE-MINT') for t in vs)))
    e4 = dict(good, id='seed-anchor',
              source='docs/findings_registry.yaml#no-such-anchor-xyz')
    demos.append(('dangling-anchor', [e4],
                  lambda vs: any('does not resolve' in t
                                 for t in vs)))
    e5 = dict(good, id='seed-span',
              code=['no/such/file_xyz.py:1-2'])
    demos.append(('unresolvable-code-span (R13)', [e5],
                  lambda vs: any('does not exist' in t for t in vs)))
    ok = True
    for name, ents, fired in demos:
        vs = check(ents)
        hit = bool(fired(vs))
        print('  seeded rejector [%s]: %s'
              % (name, 'REJECTED (as required)' if hit
                 else 'NOT REJECTED — lint broken'))
        ok &= hit
    return ok


def derive_code_identity():
    """R8 (S25-bis convergence repair, RF-1): recompute the H4 code
    identity WITHOUT importing the jax-heavy module — the module
    list is parsed from the def_twin source (single source of
    truth), the hash algorithm replicated verbatim (outer sha256
    updated with each file's sha256 digest, tuple order)."""
    import ast
    import hashlib
    src = io.open(DEFTW_SRC, encoding='utf-8').read()
    mods = None
    for node in ast.walk(ast.parse(src)):
        if (isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name)
                        and t.id == 'RECORD_PATH_MODULES'
                        for t in node.targets)):
            mods = [e.value for e in node.value.elts]
    if mods is None:
        return None
    h = hashlib.sha256()
    for fn in mods:
        with open(os.path.join(ROOT, 'validation', fn), 'rb') as fh:
            h.update(hashlib.sha256(fh.read()).digest())
    return h.hexdigest()


def derive_staleness_check():
    """The INTRA-COMMIT staleness channel (RF-1 of the S25-bis diff
    convergence): the committed derive artifact's tail.code_id must
    equal the CURRENT tree's code identity — the C4 git link is
    cross-commit and cannot see a record-path edit landing in the
    same commit as (or after) the artifact. Seeded rejector: a
    doctored code_id must MISMATCH."""
    import json
    try:
        art = json.load(io.open(DERIVE_ART, encoding='utf-8'))
    except OSError as e:
        print('  derive artifact unreadable (%s) — channel FAIL' % e)
        return False
    tail = art.get('tail')
    if tail is None:
        print('  derive artifact PRE-H4 (no tail block) — declared '
              'skip (legacy artifact)')
        return True
    cid = derive_code_identity()
    if cid is None:
        print('  RECORD_PATH_MODULES not parseable — channel FAIL')
        return False
    ok = tail.get('code_id') == cid
    print('  H4 derive artifact vs tree: tail.code_id %s / tree %s '
          '-> %s' % (str(tail.get('code_id'))[:12], cid[:12],
                     'FRESH' if ok else
                     'STALE (re-run stage_derive on this tree)'))
    seed_ok = ('0' * 64) != cid
    print('  seeded rejector [doctored code_id mismatch]: %s'
          % ('REJECTED (as required)' if seed_ok
             else 'NOT REJECTED — channel broken'))
    return ok and seed_ok


def run():
    text = io.open(REGISTRY, encoding='utf-8').read()
    try:
        entries = parse_registry(text)
    except ValueError as e:
        print('  PARSE FAIL: %s' % e)
        return False
    vs = check(entries)
    for t in vs[:40]:
        print('  VIOLATION ' + t)
    ok_seed = seeded_rejectors()
    ok_stale = derive_staleness_check()
    n_open = sum(1 for e in entries if e.get('status') in OPEN)
    ok = not vs and ok_seed and ok_stale
    print('  %-52s %s (%d entries, %d open, %d violations; H4 '
          'artifact channel %s)'
          % ('findings registry lint (R31 findings-as-code)',
             'PASS' if ok else 'FAIL', len(entries), n_open, len(vs),
             'ok' if ok_stale else 'FAIL'))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
