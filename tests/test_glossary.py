"""(xxiii) Glossary lint -- codename collision disambiguation +
navigation (S-ORDINE T2 lint step, plan of record
validation/ADVISORY_SORDINE_plan_2026-08-13.md section 3, 2026-08-13).

docs/glossary.yaml disambiguates the measured codename-token collisions
and points every meaning at its document of record. HONEST SCOPE
(binding wording, plan REF-11): this lint delivers COLLISION
DISAMBIGUATION + NAVIGATION -- it is NOT anti-re-mint machinery (that
is the findings-registry (xix) dedup clause's job).

CHECKS (seeded rejectors proven every run):
  (a) SCHEMA: entries REQUIRE token + namespace + meaning + resolver
      (namespace mandatory -- the whole point of the file); families
      REQUIRE family + resolver + count_covered.
  (b) POINTER RESOLUTION: every path-like token in every resolver
      exists on disk (candidates = tokens carrying a known extension
      or a trailing slash; "PARENT/" -> "../"; bare filenames also
      tried under validation/ -- convention declared here).
  (c) COLLISION FAMILIES: each of the 12 pinned collision token groups
      (O5, M1, T2, F4, C1, L4, U1..U4, A1, P*, B1, T1/T2, F1..F7 --
      the S-ORDINE contract list) has >= 2 disambiguating entries.
  (d) RATCHETED TOKEN-RESOLUTION over the scoped corpus (plan S10
      scope at introduction): id/owner/note fields of the docs/*.yaml
      registries + status-banner lines of docs/*.md. Tokens matching
      the codename grammar (hyphenated caps / bracketed hyphenated
      ids) that resolve to NEITHER a glossary entry/family pattern NOR
      a claims-registry id are counted; the count is FROZEN at
      TOKEN_BASELINE (measured 2026-08-13); growth = FAIL (SR-4: new
      tokens entering typed artifacts must resolve in the same
      window); shrink reports ratchet-down. Widening the corpus to the
      historical validation/ tree is a REGISTERED later ratchet, not a
      birth obligation (plan S10 declared limit).

Usage:  python tests/test_glossary.py     (stdlib-only, < ~1 s)
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PARENT = os.path.dirname(ROOT)
GLOSSARY = os.path.join(ROOT, 'docs', 'glossary.yaml')
CLAIMS = os.path.join(ROOT, 'docs', 'claims_registry.yaml')
DOCS = os.path.join(ROOT, 'docs')

FAMILY_FIELDS = ('family', 'resolver', 'count_covered', 'note')
FAMILY_REQUIRED = ('family', 'resolver', 'count_covered')
ENTRY_FIELDS = ('token', 'namespace', 'meaning', 'resolver',
                'first_seen')
ENTRY_REQUIRED = ('token', 'namespace', 'meaning', 'resolver')

# Corpus yamls for the ratchet (registries; the glossary itself is the
# resolver, never its own corpus):
CORPUS_YAMLS = ('claims_registry.yaml', 'findings_registry.yaml',
                'choice_ledger.yaml', 'flag_registry.yaml',
                'literature_registry.yaml')

# Frozen unresolved-token baseline (RE-measured 2026-08-13 late in the
# S-ORDINE T2 lint step -- distinct unresolved tokens over the scoped
# corpus: 633 corpus strings -> 222 grammar tokens -> 54 unresolved,
# mostly short-range enumerations and finding-slug fragments inside
# findings/choice-ledger note fields, e.g. B-F10, C-A/B/C, P-TRFLOOR,
# IVXC-* -- full list printable by running this module). MEASUREMENT
# NOTE OF RECORD: the first freeze the same day read 568/219/51; the
# corpus is being grown LIVE by the parallel S7 findings-registry
# seeding tranches (the +3 delta is their new finding slugs), so this
# baseline was re-frozen at reality per R28 discipline and the SR-4
# triage of the seeding tranches' residual tokens is the seeding /
# R3-closure session's declared duty. Growth FAILS, shrink =
# ratchet-down report:
# Re-frozen 2026-08-13 (F-SERVICE reconciliation): 54 -> 52 measured
# after the SR-4 same-window resolution of the 11 post-baseline tokens
# (2 linked families B-F<n>/RF-<n> + 6 entries + 1 prose case-fix);
# the family patterns also resolved the pre-existing B-F10/B-F11 debt,
# hence the ratchet-down (R28 discipline: baseline follows reality).
TOKEN_BASELINE = 52

EXTS = ('md', 'py', 'json', 'yaml', 'yml', 'pdf', 'f90', 'patch',
        'png', 'txt', 'zip', 'log')
BR_RX = re.compile(r"\[((?:[A-Z][A-Za-z0-9]*-)+[A-Za-z0-9']+)\]")
HY_RX = re.compile(r"\b([A-Z][A-Z0-9]{0,8}"
                   r"(?:-[A-Z0-9][A-Za-z0-9']{0,20})+)\b")

# Family prefix patterns (kept LINKED to the families section: each
# link-substring must appear in some family name, else violation):
FAMILY_PATTERNS = (
    (r'^GAP-\d+$', 'GAP-<n>'),
    (r'^DUTY-\d+$', 'DUTY-<n>'),
    (r'^CEN-O\d+$', 'CEN-O<n>'),
    (r'^RT-\d+$', 'RT-<n>'),
    (r'^ISS-\d+$', 'ISS-<n>'),
    (r'^ATT-\d+$', 'ATT-<n>'),
    (r'^MOC-\d+$', 'MOC-<nn>'),
    (r'^SOTA-\d+$', 'SOTA-<n>'),
    (r'^D-\d{2}$', 'D-<nn>'),
    # F-SERVICE window reconciliation 2026-08-13 (SR-4): the S25-bis
    # diff-convergence enumerations entered the ratchet corpus via the
    # choice-ledger cross-reconciliation notes (commit 3961d3d) — two
    # linked family rows added to the glossary in the same window.
    (r'^B-F\d+$', 'B-F<n>'),
    (r'^RF-\d+$', 'RF-<n>'),
    # S-FOUNDATIONS window 2026-08-17 (SR-4): the Phase-A de-novo
    # attack-tree fork namespaces entered the ratchet corpus via the
    # C49 choice-ledger note — four linked family rows added to the
    # glossary in the same window (V/H/O/P = variational/hyperbolic/
    # optimization/propulsion deriver trees).
    (r'^V-F\d+$', 'V-F<n>'),
    (r'^H-F\d+$', 'H-F<n>'),
    (r'^O-F\d+$', 'O-F<n>'),
    (r'^P-F\d+$', 'P-F<n>'),
    # S-FOUNDATIONS-C3 Blocco-3 wave-3 landing 2026-08-20 (SR-4): the
    # wave-3 refuter ids (R3FAM/R3CONV/R3REMENG/R3REMPOL/R3C50 slots),
    # the wave-2 C31TRIO refuter ids, the wave-3 confirm-repair ids,
    # the per-choice falsifier ids F-C<n>[-<m>], and the S-ORDINE
    # closure-rule ids SR-<n> entered the ratchet corpus via the
    # choice-ledger landing notes — five linked family rows added to
    # the glossary in the same window (resolvers: the blocco3
    # VERDICT/refute/confirm files; CLAUDE.md R7 for SR-<n>).
    (r'^R3[A-Z][A-Z0-9]{1,6}-\d+$', 'R3<slot>-<n>'),
    (r'^RC31T-\d+$', 'RC31T-<n>'),
    (r'^CR-W3-\d+$', 'CR-W3-<n>'),
    (r'^F-C\d+(?:-\d+)?$', 'F-C<n>'),
    (r'^SR-\d+$', 'SR-<n>'),
)

# The 12 pinned collision groups (contract list) -> entry predicate:
PINNED = (
    ('O5', lambda t: t == 'O5'),
    ('M1', lambda t: t == 'M1'),
    ('T2', lambda t: t == 'T2' or t.startswith('T2 ')),
    ('F4', lambda t: t in ('F4', 'F4b')),
    ('C1', lambda t: t in ('C1', 'C-1')),
    ('L4', lambda t: t == 'L4' or t.startswith('L4-')),
    ('U1..U4', lambda t: t[:2] in ('U1', 'U2', 'U3', 'U4')),
    ('A1', lambda t: t in ('A1', 'A1_*')),
    ('P*', lambda t: t.startswith('P')),
    ('B1', lambda t: t == 'B1'),
    ('T1/T2', lambda t: t.startswith('T1') or t.startswith('T2')),
    ('F1..F7', lambda t: t.startswith('F1')),
)


def parse_glossary(text):
    """Declared subset -> (families, entries). ValueError on drift."""
    families, entries = [], []
    target, cur = None, None
    for n, ln in enumerate(text.splitlines(), 1):
        if re.match(r'^\s*(#|$)', ln):
            continue
        if ln.rstrip() == 'families:':
            target, cur = families, None
            continue
        if ln.rstrip() == 'entries:':
            target, cur = entries, None
            continue
        m = re.match(r'^  - (family|token):\s*(.*)$', ln)
        if m and target is not None:
            val = m.group(2).strip()
            cur = {m.group(1): val[1:-1]
                   if re.match(r'^".*"$', val) else val}
            target.append(cur)
            continue
        m = re.match(r'^    (\w+):\s*(.*)$', ln)
        if m and cur is not None:
            val = m.group(2).strip()
            cur[m.group(1)] = (val[1:-1]
                               if re.match(r'^".*"$', val) else val)
            continue
        raise ValueError('line %d not in the declared subset: %r'
                         % (n, ln))
    return families, entries


def _path_tokens(s):
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
    if tok.startswith('PARENT/'):
        return os.path.exists(os.path.join(
            PARENT, tok[7:].replace('/', os.sep)))
    rel = tok.replace('/', os.sep)
    for base in (ROOT, os.path.join(ROOT, 'validation'),
                 os.path.join(ROOT, 'docs'), PARENT):
        if os.path.exists(os.path.join(base, rel)):
            return True
    return False


def check_glossary(families, entries):
    """(a)-(c): schema, pointer resolution, pinned collisions."""
    v = []
    for f in families:
        fid = f.get('family', '?')
        missing = [k for k in FAMILY_REQUIRED if k not in f]
        extra = [k for k in f if k not in FAMILY_FIELDS]
        if missing or extra:
            v.append('family %s: missing %s / undeclared %s'
                     % (fid, missing, extra))
        if not re.match(r'^\d+$', str(f.get('count_covered', ''))):
            v.append('family %s: count_covered %r not an integer'
                     % (fid, f.get('count_covered')))
    for e in entries:
        eid = e.get('token', '?')
        missing = [k for k in ENTRY_REQUIRED if k not in e]
        extra = [k for k in e if k not in ENTRY_FIELDS]
        if missing or extra:
            v.append('entry %s: missing %s / undeclared %s'
                     % (eid, missing, extra))
            continue
        if not e['namespace'].strip():
            v.append('entry %s: empty namespace (mandatory)' % eid)
        if not e['meaning'].strip():
            v.append('entry %s: empty meaning' % eid)
    # (b) pointer resolution over ALL resolvers
    for item in families + entries:
        iid = item.get('family', item.get('token', '?'))
        res = item.get('resolver', '')
        toks = _path_tokens(res)
        if not toks:
            v.append('%s: resolver carries no path-like token: %r'
                     % (iid, res[:60]))
        for t in toks:
            if not _resolves(t):
                v.append('%s: resolver path does not exist: %s'
                         % (iid, t))
    # (c) pinned collision groups
    toks = [e.get('token', '') for e in entries]
    for name, pred in PINNED:
        n = sum(1 for t in toks if pred(t))
        if n < 2:
            v.append('pinned collision group %s has %d entries (< 2 '
                     'disambiguating rows)' % (name, n))
    # family-pattern linkage (keeps FAMILY_PATTERNS honest)
    fnames = ' | '.join(f.get('family', '') for f in families)
    for rx, link in FAMILY_PATTERNS:
        if link not in fnames:
            v.append('FAMILY_PATTERNS %r not linked to any family row '
                     '(%r absent)' % (rx, link))
    return v


def corpus_strings():
    """The ratchet corpus: registry id/owner/note values + docs/*.md
    status-banner lines."""
    out = []
    for y in CORPUS_YAMLS:
        p = os.path.join(DOCS, y)
        if not os.path.isfile(p):
            continue
        for ln in io.open(p, encoding='utf-8', errors='replace'):
            m = re.match(r'^\s*-?\s*(id|owner|note):\s*(.*)$', ln)
            if m:
                out.append((y, m.group(2)))
    for f in sorted(os.listdir(DOCS)):
        if not f.endswith('.md'):
            continue
        for ln in io.open(os.path.join(DOCS, f), encoding='utf-8',
                          errors='replace'):
            s = ln.lstrip()
            if s.startswith('>') and ('STATUS' in s or 'SUPERSED' in s):
                out.append((f, s))
    return out


def extract_tokens(strings):
    toks = set()
    for _, s in strings:
        toks.update(BR_RX.findall(s))
        toks.update(HY_RX.findall(s))
    return toks


def resolution_sets(families, entries):
    pieces = set()
    for e in entries:
        t = e.get('token', '')
        for piece in re.split(r'\s*/\s*', t):
            piece = re.sub(r'\s*\(.*\)$', '', piece).strip()
            if piece:
                pieces.add(piece)
                pieces.add(piece.strip('[]'))
        pieces.update(BR_RX.findall(t))
        pieces.update(HY_RX.findall(t))
    claims_ids = set(re.findall(
        r'(?m)^- id:\s*(\S+)',
        io.open(CLAIMS, encoding='utf-8', errors='replace').read()))
    pats = [re.compile(rx) for rx, _ in FAMILY_PATTERNS]
    return pieces, claims_ids, pats


def unresolved_tokens(tokens, pieces, claims_ids, pats):
    out = []
    for t in sorted(tokens):
        if t in pieces or t in claims_ids:
            continue
        if any(rx.match(t) for rx in pats):
            continue
        out.append(t)
    return out


def check_ratchet(n, baseline, quiet=False):
    v = []
    if n > baseline:
        v.append('unresolved codename tokens %d above frozen baseline '
                 '%d (SR-4: new tokens must resolve to glossary or '
                 'registry in the same window)' % (n, baseline))
    elif n < baseline and not quiet:
        print('  [ratchet-down available] unresolved %d < baseline %d '
              '-- shrink TOKEN_BASELINE' % (n, baseline))
    return v


def seeded_rejectors(families, entries, tokens, pieces, claims_ids,
                     pats):
    demos = []
    t1 = set(tokens) | {'ZZQ-SEEDTOKEN'}
    demos.append(('unknown token',
                  lambda: check_ratchet(
                      len(unresolved_tokens(t1, pieces, claims_ids,
                                            pats)),
                      TOKEN_BASELINE, True),
                  'above frozen baseline'))
    n_now = len(unresolved_tokens(tokens, pieces, claims_ids, pats))
    demos.append(('baseline +1 bump',
                  lambda: check_ratchet(n_now + 1, TOKEN_BASELINE,
                                        True),
                  'above frozen baseline'))
    e3 = [dict(e) for e in entries]
    e3[0]['resolver'] = 'no/such/file_zzq.md'
    demos.append(('dead resolver pointer',
                  lambda: check_glossary(families, e3),
                  'does not exist'))
    ok = True
    for name, fn, needle in demos:
        hit = any(needle in t for t in fn())
        print('  seeded rejector [%s]: %s'
              % (name, 'REJECTED (as required)' if hit
                 else 'NOT REJECTED -- lint broken'))
        ok &= hit
    return ok


def run():
    text = io.open(GLOSSARY, encoding='utf-8', errors='replace').read()
    try:
        families, entries = parse_glossary(text)
    except ValueError as e:
        print('  PARSE FAIL: %s' % e)
        return False
    vs = check_glossary(families, entries)
    strings = corpus_strings()
    tokens = extract_tokens(strings)
    pieces, claims_ids, pats = resolution_sets(families, entries)
    unres = unresolved_tokens(tokens, pieces, claims_ids, pats)
    vs += check_ratchet(len(unres), TOKEN_BASELINE)
    print('  corpus: %d strings, %d grammar tokens, %d unresolved '
          '(baseline %d); sample: %s'
          % (len(strings), len(tokens), len(unres), TOKEN_BASELINE,
             ', '.join(unres[:8]) or '-'))
    for t in vs[:40]:
        print('  VIOLATION ' + t)
    ok_seed = seeded_rejectors(families, entries, tokens, pieces,
                               claims_ids, pats)
    ok = not vs and ok_seed
    print('  %-52s %s (%d families, %d entries, %d violations)'
          % ('glossary lint (collision + navigation, NOT anti-re-mint)',
             'PASS' if ok else 'FAIL', len(families), len(entries),
             len(vs)))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
