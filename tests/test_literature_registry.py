"""(xxii) Literature-registry lint -- papers-as-code (S-ORDINE T2
lint step, plan of record validation/ADVISORY_SORDINE_plan_2026-08-13.md
section 3, 2026-08-13).

docs/literature_registry.yaml is the typed index of the literature
corpus over FOUR roots (A = repo literature/, B = PARENT/ i.e. "../",
C = GENO/ read-only, D = literature_review/). This lint enforces the
registry's own machine rules:

CHECKS (each load-bearing rule with a SEEDED rejector proven each run):
  (a) SCHEMA: declared field sets on entries and bulk rows; status in
      {READ-INTEGRAL, READ-PARTIAL, READ-PARTIAL(triaged), UNREAD,
      WANTED}; duplicate ids.
  (b) HONESTY RULES: WANTED/UNREAD => owner REQUIRED; UNREAD row with
      a non-empty summary = FAIL (the never-fake-a-summary machine
      rule); WANTED rows have NO paths; non-WANTED rows have >= 1 path
      and EVERY path exists on disk (prefix map: "PARENT/" -> "../",
      "REPO/" -> stripped, everything else repo-root-relative);
      READ-* rows carry >= 1 where_read anchor whose FILE part exists.
  (c) FOUR-ROOT COVERAGE at discrepancy 0: fresh per-root disk
      counts (root A: literature/*.pdf; root B: parent-dir top-level
      files; root C: recursive GENO *.pdf; root D: recursive
      literature_review/ files) == rows-covering-that-root + bulk-row
      declared counts, exactly, per root (the DRIFT dict is the
      declared ratchet channel for measured drift; ALL ZERO since the
      2026-08-13 ratchet-down folded the four post-S6 REFUTE_*
      reports into the root-D bulk row). Uncovered or phantom files
      FAIL in either direction.

Usage:  python tests/test_literature_registry.py   (stdlib-only, <~1 s)
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PARENT = os.path.dirname(ROOT)
REGISTRY = os.path.join(ROOT, 'docs', 'literature_registry.yaml')

STATUSES = ('READ-INTEGRAL', 'READ-PARTIAL', 'READ-PARTIAL(triaged)',
            'UNREAD', 'WANTED')
ENTRY_FIELDS = ('id', 'identity', 'paths', 'status', 'where_read',
                'summary', 'owner')
ENTRY_REQUIRED = ('id', 'identity', 'paths', 'status')
BULK_FIELDS = ('id', 'class', 'root', 'count', 'covers', 'note')
BULK_REQUIRED = ('id', 'class', 'root', 'count', 'covers')
ROOTS = ('A', 'B', 'C', 'D')

# Drift allowance: ALL ZERO since the 2026-08-13 ratchet-down -- the
# four convergence-round REFUTE_* reports that landed after the S6
# registry build were folded into the root-D review-apparatus bulk row
# (count 29 -> 33, dated in-registry). Coverage is now exact per root;
# any uncovered or phantom file FAILS outright. The dict stays as the
# declared ratchet channel for any future measured drift.
DRIFT = {'A': 0, 'B': 0, 'C': 0, 'D': 0}


def _to_disk(path):
    """Registry path -> absolute path (PARENT/ and REPO/ prefixes)."""
    if path.startswith('PARENT/'):
        return os.path.join(PARENT, path[7:].replace('/', os.sep))
    if path.startswith('REPO/'):
        path = path[5:]
    return os.path.join(ROOT, path.replace('/', os.sep))


def _root_of(path):
    if path.startswith('literature/'):
        return 'A'
    if path.startswith('PARENT/'):
        return 'B'
    if path.startswith('GENO/'):
        return 'C'
    if path.startswith('literature_review/'):
        return 'D'
    return None


def parse_registry(text):
    """Strict declared-subset parse -> (entries, bulk). ValueError on
    an unrecognized line."""
    entries, bulk = [], []
    target, cur, pending = entries, None, None
    for n, ln in enumerate(text.splitlines(), 1):
        if re.match(r'^\s*(#|$)', ln):
            continue
        if ln.strip() == 'entries:':
            target, cur = entries, None
            continue
        if ln.strip() == 'bulk:':
            target, cur = bulk, None
            continue
        m = re.match(r'^- id:\s*(\S+)\s*$', ln)
        if m:
            cur = {'id': m.group(1)}
            target.append(cur)
            pending = None
            continue
        m = re.match(r'^  (\w+):\s*(.*)$', ln)
        if m and cur is not None:
            k, val = m.group(1), m.group(2).strip()
            if val == '':
                cur[k] = []
                pending = k
            elif val.startswith('['):
                cur[k] = re.findall(r'"([^"]*)"', val)
                pending = None
            else:
                cur[k] = val[1:-1] if re.match(r'^".*"$', val) else val
                pending = None
            continue
        m = re.match(r'^\s+- (.*)$', ln)
        if m and cur is not None and pending is not None:
            item = m.group(1).strip()
            cur[pending].append(item[1:-1]
                                if re.match(r'^".*"$', item) else item)
            continue
        raise ValueError('line %d not in the declared subset: %r'
                         % (n, ln))
    return entries, bulk


def check_entries(entries, bulk):
    """(a) + (b): schema, enums, honesty rules, path/anchor existence."""
    v = []
    byid = {}
    for e in entries + bulk:
        if e['id'] in byid:
            v.append('duplicate id %s' % e['id'])
        byid[e['id']] = e
    for e in entries:
        eid = e.get('id', '?')
        missing = [f for f in ENTRY_REQUIRED if f not in e]
        extra = [f for f in e if f not in ENTRY_FIELDS]
        if missing or extra:
            v.append('%s: fields missing %s / undeclared %s'
                     % (eid, missing, extra))
            continue
        st = e['status']
        if st not in STATUSES:
            v.append('%s: status %r not in %s' % (eid, st, STATUSES))
            continue
        if st in ('WANTED', 'UNREAD') and not e.get('owner', '').strip():
            v.append('%s: %s row without owner' % (eid, st))
        if st == 'UNREAD' and e.get('summary', '').strip():
            v.append('%s: UNREAD row carries a summary (never fake a '
                     'summary of an unread paper)' % eid)
        if st == 'WANTED':
            if e['paths']:
                v.append('%s: WANTED row has paths %s (a wanted paper '
                         'is on NO root)' % (eid, e['paths']))
            continue
        if not e['paths']:
            v.append('%s: non-WANTED row without any path' % eid)
        for p in e['paths']:
            if _root_of(p) is None:
                v.append('%s: path %r maps to no root A/B/C/D'
                         % (eid, p))
            elif not os.path.isfile(_to_disk(p)):
                v.append('%s: path does not exist on disk: %s'
                         % (eid, p))
        if st.startswith('READ'):
            anchors = e.get('where_read', [])
            if not anchors:
                v.append('%s: READ-* row without where_read anchors'
                         % eid)
            for a in anchors:
                fp = a.partition('#')[0]
                if not os.path.isfile(_to_disk(fp)):
                    v.append('%s: where_read anchor file missing: %s'
                             % (eid, fp))
    for b in bulk:
        bid = b.get('id', '?')
        missing = [f for f in BULK_REQUIRED if f not in b]
        extra = [f for f in b if f not in BULK_FIELDS]
        if missing or extra:
            v.append('%s: bulk fields missing %s / undeclared %s'
                     % (bid, missing, extra))
            continue
        if b['root'] not in ROOTS:
            v.append('%s: bulk root %r not in %s'
                     % (bid, b['root'], ROOTS))
        if not re.match(r'^\d+$', str(b['count'])):
            v.append('%s: bulk count %r not an integer'
                     % (bid, b['count']))
    return v


def disk_counts():
    """Fresh per-root file counts (the coverage denominators)."""
    lit = os.path.join(ROOT, 'literature')
    a = len([f for f in os.listdir(lit) if f.endswith('.pdf')])
    b = len([f for f in os.listdir(PARENT)
             if os.path.isfile(os.path.join(PARENT, f))])
    c = 0
    geno = os.path.join(ROOT, 'GENO')
    for _, _, files in os.walk(geno):
        c += sum(1 for f in files if f.endswith('.pdf'))
    d = 0
    for _, _, files in os.walk(os.path.join(ROOT, 'literature_review')):
        d += len(files)
    return {'A': a, 'B': b, 'C': c, 'D': d}


def check_coverage(entries, bulk, disk, quiet=False):
    """(c) four-root reconciliation with the frozen drift allowance."""
    v = []
    rows = {r: 0 for r in ROOTS}
    for e in entries:
        for r in {_root_of(p) for p in e.get('paths', [])} - {None}:
            rows[r] += 1
    bulks = {r: 0 for r in ROOTS}
    for b in bulk:
        if b.get('root') in ROOTS and re.match(r'^\d+$',
                                               str(b.get('count'))):
            bulks[b['root']] += int(b['count'])
    for r in ROOTS:
        covered = rows[r] + bulks[r]
        gap = disk[r] - covered
        if gap < 0 or gap > DRIFT[r]:
            v.append('root %s: disk %d != rows %d + bulk %d '
                     '(+ drift <= %d) -- unregistered or phantom '
                     'coverage' % (r, disk[r], rows[r], bulks[r],
                                   DRIFT[r]))
        elif gap > 0 and not quiet:
            print('  [baseline] root %s: %d uncovered file(s) inside '
                  'the frozen drift allowance (REFUTE_* reports, '
                  '2026-08-13)' % (r, gap))
        elif gap == 0 and DRIFT[r] > 0 and not quiet:
            print('  [ratchet-down available] root %s covered exactly '
                  '-- shrink DRIFT' % r)
    return v


def seeded_rejectors(entries, bulk, disk):
    """Each rule must FIRE on doctored in-memory data."""
    demos = []
    d1 = dict(disk)
    d1['A'] += 1   # a PDF lands on root A with no registry row
    demos.append(('unregistered PDF (root A +1)',
                  lambda: check_coverage(entries, bulk, d1, True),
                  'unregistered or phantom'))
    fake = {'id': 'seed-unread', 'identity': 'x', 'status': 'UNREAD',
            'owner': 'seed-owner', 'summary': 'a fabricated summary',
            'paths': ['literature/dan25254.pdf']}
    demos.append(('UNREAD-with-summary',
                  lambda: check_entries([fake], []),
                  'never fake a summary'))
    fake2 = {'id': 'seed-wanted', 'identity': 'x', 'status': 'WANTED',
             'owner': 'o', 'paths': ['literature/dan25254.pdf']}
    demos.append(('WANTED-with-path',
                  lambda: check_entries([fake2], []),
                  'WANTED row has paths'))
    fake3 = {'id': 'seed-deadpath', 'identity': 'x',
             'status': 'READ-PARTIAL', 'where_read': ['data/q_formal.md#'],
             'paths': ['literature/no_such_file_zzq.pdf']}
    demos.append(('dead path',
                  lambda: check_entries([fake3], []),
                  'does not exist on disk'))
    ok = True
    for name, fn, needle in demos:
        hit = any(needle in t for t in fn())
        print('  seeded rejector [%s]: %s'
              % (name, 'REJECTED (as required)' if hit
                 else 'NOT REJECTED -- lint broken'))
        ok &= hit
    return ok


def run():
    text = io.open(REGISTRY, encoding='utf-8', errors='replace').read()
    try:
        entries, bulk = parse_registry(text)
    except ValueError as e:
        print('  PARSE FAIL: %s' % e)
        return False
    disk = disk_counts()
    vs = check_entries(entries, bulk)
    vs += check_coverage(entries, bulk, disk)
    for t in vs[:40]:
        print('  VIOLATION ' + t)
    ok_seed = seeded_rejectors(entries, bulk, disk)
    n_wanted = sum(1 for e in entries if e.get('status') == 'WANTED')
    ok = not vs and ok_seed
    print('  %-52s %s (%d entries [%d WANTED], %d bulk rows, disk '
          'A/B/C/D = %d/%d/%d/%d, %d violations)'
          % ('literature registry lint (four roots)',
             'PASS' if ok else 'FAIL', len(entries), n_wanted,
             len(bulk), disk['A'], disk['B'], disk['C'], disk['D'],
             len(vs)))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
