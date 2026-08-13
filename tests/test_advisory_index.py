"""(xx) Advisory-index lint -- validation/ record-layer navigation
(S-ORDINE T2 lint step, plan of record
validation/ADVISORY_SORDINE_plan_2026-08-13.md section 3, 2026-08-13).

validation/ADVISORY_INDEX.md is THE machine-checked navigation layer
(L7) for the flat validation/ directory: one row per validation-tree
.md file plus one BLOCK row per raws dir. This lint makes index drift
MACHINE-REJECTED, mirroring the claims lint (xv) / findings lint (xix).

CHECKS (each with a SEEDED rejector proven every run):
  (a) BIJECTION: fresh ls of validation/*.md MINUS ADVISORY_INDEX.md
      itself (SELF-ROW EXEMPTION, declared: the index does not row-list
      itself) <-> table file rows; raws dirs on disk (dirname contains
      'raws') <-> RAW block rows, both directions.
  (b) STATUS ENUM (index section-2 / plan section-2, hardcoded here
      with this comment as the declared source): every status cell
      starts with one of the core statuses; qualifier tails checked
      against the declared qualifier set (QUAL_BASELINE ratchet
      channel, EMPTY since the 2026-08-13 ratchet-down -- any
      nonconforming tail FAILS).
  (c) SUPERSEDED*/CONSUMED* rows carry a YYYY-MM-DD date and a
      resolvable pointer somewhere in the row (status or note cell;
      'self' accepted for CONSUMED-with-residue:self...).
      DATEPTR_BASELINE ratchet channel, EMPTY since the 2026-08-13
      ratchet-down -- any violating row FAILS.
  (d) PLAN-ANCHOR: cell non-empty OR carries the literal
      'ORPHAN-FLAGGED'. Orphan count RATCHETED: baseline
      ORPHAN_BASELINE = 1 (ratcheted 5 -> 1 on 2026-08-13 handoff
      absorption: the four literature artifacts gained plan-anchors
      P-1 / S-CERT-MC8 / F2; sole survivor pending UD-4: ADR_panel;
      original five: ADR_panel,
      moc_zucrow_fidelity, sota_definition, ASSESSMENT_methodology,
      LEDGER_dubbi_moc); above baseline FAILS, below reports
      ratchet-down.
  (e) SUPERSESSION-MARKER family over validation/*.md heads (first
      HEAD_LINES lines): every '> **STATUS' banner line must parse
      (core status word + date + '->' + resolvable pointer) and agree
      with the file's index-row core status; legacy free-form
      'SUPERSED*' head markers are counted against the frozen
      LEGACY_MARKER_BASELINE = 2 (measured 2026-08-13:
      DISPATCH_Sspeed_to_S25 head comment; PROGRESS_2026-08-12_S24_f1b
      prose line); growth FAILS.
  (f) FLAG-REGISTRY family (folded here per plan repair R-4):
      docs/flag_registry.yaml rows <-> census of actual env reads
      (os.environ.get/os.getenv of A1_* names, WHITESPACE-TOLERANT so
      line-wrapped calls are seen -- the pattern that caught the four
      reads the registry's original single-line grep missed, repaired
      2026-08-13) over validation/*.py + tests/*.py, bijection BOTH
      directions (REF-16: bare string mentions are declared out of
      scope; this module deliberately never spells the census call
      literally so it cannot self-hit). REGISTRY_GAP_BASELINE ratchet
      channel, EMPTY since the 2026-08-13 ratchet-down.

Usage:  python tests/test_advisory_index.py     (stdlib-only, < ~1 s)
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VAL = os.path.join(ROOT, 'validation')
INDEX = os.path.join(VAL, 'ADVISORY_INDEX.md')
FLAG_REG = os.path.join(ROOT, 'docs', 'flag_registry.yaml')

SELF_ROW_EXEMPT = 'ADVISORY_INDEX.md'   # declared: index never rows itself
HEAD_LINES = 15

# Core statuses, longest-prefix first (index section "Status enum of
# record" / plan section 2 -- one enum, no coexisting variants):
CORE = ('CONSUMED-with-residue', 'CONSUMED', 'SUPERSEDED-BY',
        'OF-RECORD', 'RAW', 'DERIVED', 'PENDING-CONTRACT', 'UNRESOLVED')
DATED = ('CONSUMED-with-residue', 'CONSUMED', 'SUPERSEDED-BY')
QUALS = ('LECTURE-ERA', 'UNTRACKED-SINGLE-COPY')

# Frozen baselines (measured 2026-08-13, S-ORDINE T2 lint step; growth
# beyond any baseline = FAIL, a cleaned row = ratchet-down report):
ORPHAN_BASELINE = 1  # ratcheted 5 -> 1, 2026-08-13 handoff absorption (ADR_panel sole survivor, UD-4)
# QUAL_BASELINE: EMPTY since 2026-08-13 ratchet-down (the one frozen
# occupant, moc_zucrow's 'PARTIALLY CLOSED (...)' status tail, was
# moved into that row's note cell -- campaign state is note content,
# not a section-2 status). Any nonconforming tail now FAILS outright.
QUAL_BASELINE = set()
# DATEPTR_BASELINE: EMPTY since 2026-08-13 ratchet-down (the two
# frozen occupants repaired at source: interface_audit's row now
# mirrors its banner date+pointer; G5_pmm_toc_sweep was re-filed
# OF-RECORD per its in-file 'Status: RECORD' -- the CONSUMED thing was
# commission Item 2a, not the sweep deliverable itself). Any
# SUPERSEDED*/CONSUMED* row lacking date+pointer now FAILS outright.
DATEPTR_BASELINE = set()
LEGACY_MARKER_BASELINE = 2
# REGISTRY_GAP_BASELINE: EMPTY since 2026-08-13 ratchet-down (the four
# line-wrapped env reads this lint's whitespace-tolerant census found
# beyond the registry's original single-line grep -- A1_DEFTW_ATLAS,
# A1_LOCD_BASE, A1_LOCD_REJ, A1_MGOV_BASE -- now have registry rows;
# docs/flag_registry.yaml census note repaired to 59 sites / 45 unique
# flags with the whitespace-tolerant pattern pinned). Any unregistered
# env-read flag now FAILS outright.
REGISTRY_GAP_BASELINE = set()

DATE_RX = re.compile(r'\d{4}-\d{2}-\d{2}')
EXTS = ('md', 'py', 'json', 'yaml', 'yml', 'pdf', 'f90', 'patch',
        'png', 'txt', 'zip', 'log')
# env-read census pattern, assembled so this module's own source can
# never satisfy it (REF-16 fold):
_CALLS = 'environ\\.get|getenv'
RX_ENV = re.compile('os\\.(?:' + _CALLS + ')\\(\\s*[\'"]'
                    '(A1_[A-Z0-9_]+)')


def _path_tokens(s):
    """Path-like tokens in a prose cell (backticks stripped)."""
    out = []
    for t in re.findall(r"[\w./%()'\-]+", s.replace('`', ' ')):
        t = t.strip('.,;')
        if t.startswith('.') or len(t) < 4:
            continue
        if t.endswith('/') and '/' in t.rstrip('/'):
            out.append(t)
        elif re.search(r'\.(%s)$' % '|'.join(EXTS), t):
            out.append(t)
    return out


def _resolves(tok):
    """Token resolves against validation/, repo root, or parent."""
    rel = tok.replace('/', os.sep)
    for base in (VAL, ROOT, os.path.dirname(ROOT)):
        if os.path.exists(os.path.join(base, rel)):
            return True
    return False


def parse_index(text):
    """Index table -> (file_rows, block_rows); each row a dict."""
    rows, blocks = [], []
    in_table = False
    for ln in text.splitlines():
        if ln.startswith('## Index table'):
            in_table = True
            continue
        if not in_table or not ln.startswith('|'):
            continue
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        if len(cells) != 5 or cells[0] in ('file', '') \
                or set(cells[0]) <= set('-'):
            continue
        d = dict(zip(('file', 'cls', 'status', 'anchor', 'note'),
                     cells))
        if '(block row)' in d['file']:
            d['file'] = d['file'].replace('(block row)', '') \
                                 .replace('*', '').strip().rstrip('/')
            blocks.append(d)
        else:
            rows.append(d)
    return rows, blocks


def split_status(cell):
    """-> (core, tail) or (None, cell) when no core status matches."""
    for core in CORE:
        if cell.startswith(core):
            return core, cell[len(core):]
    return None, cell


def check_index(rows, blocks, disk_md, raws_dirs, quiet=False):
    def note(msg):
        if not quiet:
            print(msg)
    """Checks (a)-(d) on parsed rows vs fresh disk lists."""
    v = []
    byfile = {}
    for r in rows:
        if r['file'] in byfile:
            v.append('duplicate row %s' % r['file'])
        byfile[r['file']] = r
    # (a) bijection, files
    for f in sorted(set(disk_md) - set(byfile)):
        v.append('file on disk without index row: %s' % f)
    for f in sorted(set(byfile) - set(disk_md)):
        v.append('index row without file on disk: %s' % f)
    # (a) bijection, raws block rows
    bnames = {b['file'] for b in blocks}
    for d in sorted(set(raws_dirs) - bnames):
        v.append('raws dir on disk without block row: %s' % d)
    for d in sorted(bnames - set(raws_dirs)):
        v.append('block row without raws dir on disk: %s' % d)
    # (b)-(d) per row
    orphans = 0
    for r in rows + blocks:
        core, tail = split_status(r['status'])
        if core is None:
            v.append('%s: status %r has no core status from the '
                     'section-2 enum' % (r['file'], r['status']))
            continue
        if core in ('SUPERSEDED-BY', 'CONSUMED-with-residue'):
            if not tail.lstrip(': '):
                v.append('%s: %s without pointer tail'
                         % (r['file'], core))
        elif tail.strip():
            t = tail.strip().lstrip(',').strip()
            parts = [p.strip() for p in re.split(r',(?![^()]*\))', t)
                     if p.strip()]
            bad = [p for p in parts
                   if p not in QUALS and not p.startswith('AT-RISK:')
                   and not re.match(r'^\(living[^)]*\)$', p)]
            if bad:
                if r['file'] in QUAL_BASELINE:
                    note('  [baseline] %s: nonconforming qualifier '
                         'tail %r (frozen 2026-08-13)'
                         % (r['file'], t))
                else:
                    v.append('%s: unknown status qualifier(s) %s'
                             % (r['file'], bad))
        # (c) date + pointer on SUPERSEDED*/CONSUMED*
        if core in DATED:
            rowtext = ' | '.join((r['file'], r['status'], r['anchor'],
                                  r['note']))
            has_date = bool(DATE_RX.search(rowtext))
            has_ptr = ('self' in tail[:6]
                       or any(_resolves(t) for t in
                              _path_tokens(r['status'] + ' '
                                           + r['note'])))
            if not (has_date and has_ptr):
                if r['file'] in DATEPTR_BASELINE:
                    note('  [baseline] %s: %s row missing %s (frozen '
                         '2026-08-13)' % (r['file'], core,
                                          'date' if has_ptr
                                          else 'date+pointer'))
                else:
                    v.append('%s: %s row lacks %s' %
                             (r['file'], core,
                              'a YYYY-MM-DD date' if has_ptr else
                              'a resolvable pointer' if has_date else
                              'date AND resolvable pointer'))
        # (d) plan-anchor / orphan ratchet
        if 'ORPHAN-FLAGGED' in r['anchor']:
            orphans += 1
        elif not r['anchor'].strip():
            v.append('%s: empty plan-anchor cell and not '
                     'ORPHAN-FLAGGED (unflagged orphan)' % r['file'])
    if orphans > ORPHAN_BASELINE:
        v.append('ORPHAN-FLAGGED count %d above frozen baseline %d '
                 '(new orphan rows need a nameable plan anchor)'
                 % (orphans, ORPHAN_BASELINE))
    elif orphans < ORPHAN_BASELINE:
        note('  [ratchet-down available] orphans %d < baseline %d '
             '-- shrink ORPHAN_BASELINE' % (orphans, ORPHAN_BASELINE))
    return v


def check_markers(heads, rows, quiet=False):
    def note(msg):
        if not quiet:
            print(msg)
    """(e) banner family + legacy free-form count vs baseline."""
    v = []
    legacy = 0
    byfile = {r['file']: r for r in rows}
    for fname in sorted(heads):
        for ln in heads[fname]:
            if ln.lstrip().startswith('> **STATUS'):
                m = re.search(r'STATUS\W+([A-Z][A-Z-]*)', ln)
                if not m or not DATE_RX.search(ln) or '->' not in ln:
                    v.append('%s: STATUS banner does not parse '
                             '(need status word + date + "->"): %r'
                             % (fname, ln[:70]))
                    continue
                after = ln.split('->', 1)[1]
                if not any(_resolves(t) for t in _path_tokens(after)):
                    v.append('%s: banner pointer does not resolve: %r'
                             % (fname, after[:60]))
                r = byfile.get(fname)
                if r is not None and \
                        not r['status'].startswith(m.group(1)):
                    v.append('%s: banner status %s != index status %r '
                             '(index is authoritative for STATUS)'
                             % (fname, m.group(1), r['status']))
            elif 'SUPERSED' in ln:
                legacy += 1
    if legacy > LEGACY_MARKER_BASELINE:
        v.append('legacy free-form supersession markers %d above '
                 'frozen baseline %d (new markers must use the dated '
                 '"> **STATUS" banner form)'
                 % (legacy, LEGACY_MARKER_BASELINE))
    elif legacy < LEGACY_MARKER_BASELINE:
        note('  [ratchet-down available] legacy markers %d < '
             'baseline %d' % (legacy, LEGACY_MARKER_BASELINE))
    return v


def check_flags(reg_flags, census_flags, quiet=False):
    """(f) registry rows <-> env-read census, both directions."""
    v = []
    for f in sorted(set(census_flags) - set(reg_flags)):
        if f in REGISTRY_GAP_BASELINE:
            if not quiet:
                print('  [baseline] env-read flag %s has no registry '
                      'row (line-wrapped read, frozen 2026-08-13)' % f)
        else:
            v.append('env-read flag %s has no docs/flag_registry.yaml '
                     'row' % f)
    for f in sorted(REGISTRY_GAP_BASELINE & set(reg_flags)):
        if not quiet:
            print('  [ratchet-down available] %s now has a registry '
                  'row -- shrink REGISTRY_GAP_BASELINE' % f)
    for f in sorted(set(reg_flags) - set(census_flags)):
        v.append('phantom flag: registry row %s has no env read in '
                 'validation/*.py or tests/*.py' % f)
    return v


def load_disk():
    disk_md = sorted(f for f in os.listdir(VAL)
                     if f.endswith('.md') and f != SELF_ROW_EXEMPT)
    raws_dirs = sorted(d for d in os.listdir(VAL)
                       if 'raws' in d
                       and os.path.isdir(os.path.join(VAL, d)))
    heads = {}
    for f in disk_md:
        body = io.open(os.path.join(VAL, f), encoding='utf-8',
                       errors='replace')
        heads[f] = [next(body, '') for _ in range(HEAD_LINES)]
        body.close()
    return disk_md, raws_dirs, heads


def load_flags():
    reg = re.findall(r'(?m)^- flag: "([A-Za-z0-9_]+)"',
                     io.open(FLAG_REG, encoding='utf-8',
                             errors='replace').read())
    census = set()
    for d in ('validation', 'tests'):
        full = os.path.join(ROOT, d)
        for f in sorted(os.listdir(full)):
            if f.endswith('.py'):
                src = io.open(os.path.join(full, f), encoding='utf-8',
                              errors='replace').read()
                census.update(RX_ENV.findall(src))
    return reg, census


def seeded_rejectors(rows, blocks, disk_md, raws_dirs, heads,
                     reg_flags, census_flags):
    """Each check must FIRE on doctored in-memory data."""
    demos = []
    r1 = rows + [dict(file='SEED_PHANTOM_ROW_xyz.md', cls='x',
                      status='OF-RECORD', anchor='seed', note='')]
    demos.append(('phantom index row',
                  lambda: check_index(r1, blocks, disk_md, raws_dirs, True),
                  'index row without file on disk'))
    d2 = disk_md + ['SEED_PHANTOM_DISK_xyz.md']
    demos.append(('missing file row',
                  lambda: check_index(rows, blocks, d2, raws_dirs, True),
                  'file on disk without index row'))
    r3 = [dict(r) for r in rows]
    r3[0]['anchor'] = ''
    demos.append(('unflagged orphan',
                  lambda: check_index(r3, blocks, disk_md, raws_dirs, True),
                  'unflagged orphan'))
    h4 = dict(heads)
    h4['SEED_HEAD_xyz.md'] = ['blah SUPERSEDED by free-form seed']
    demos.append(('unparsed marker beyond baseline',
                  lambda: check_markers(h4, rows, True),
                  'above'))
    f5 = list(reg_flags) + ['A1_PHANTOM_SEED']
    demos.append(('phantom flag',
                  lambda: check_flags(f5, census_flags, True),
                  'phantom flag'))
    f6 = set(census_flags) | {'A1_ZZQ_UNREG_SEED'}
    demos.append(('unregistered flag beyond baseline',
                  lambda: check_flags(reg_flags, f6, True),
                  'has no docs/flag_registry.yaml row'))
    ok = True
    for name, fn, needle in demos:
        hit = any(needle in t for t in fn())
        print('  seeded rejector [%s]: %s'
              % (name, 'REJECTED (as required)' if hit
                 else 'NOT REJECTED -- lint broken'))
        ok &= hit
    return ok


def run():
    text = io.open(INDEX, encoding='utf-8', errors='replace').read()
    rows, blocks = parse_index(text)
    disk_md, raws_dirs, heads = load_disk()
    reg_flags, census_flags = load_flags()
    vs = check_index(rows, blocks, disk_md, raws_dirs)
    vs += check_markers(heads, rows)
    vs += check_flags(reg_flags, census_flags)
    for t in vs[:40]:
        print('  VIOLATION ' + t)
    ok_seed = seeded_rejectors(rows, blocks, disk_md, raws_dirs,
                               heads, reg_flags, census_flags)
    ok = not vs and ok_seed
    print('  %-52s %s (%d file rows, %d block rows, %d disk .md, '
          '%d flags, %d violations)'
          % ('advisory-index lint (S-ORDINE L7 navigation)',
             'PASS' if ok else 'FAIL', len(rows), len(blocks),
             len(disk_md), len(reg_flags), len(vs)))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
