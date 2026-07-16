"""(vii) Numeric-literal lint - the no-magic-number invariant, ENFORCED.

Every numeric literal in src/**/*.py must be one of:
  TRIVIAL     small structural integers (|n| <= 12), pure-algebra fractions
              (0.25, 0.5, 0.75) or percent/kilo/mega display scalers
              (100, 1000, 1e6);
  ALLOWLISTED declared in validation/numeric_allowlist.json under its file,
              with a class from the dof_audit taxonomy (SPEC / MODEL-CONST /
              EMPIRICAL / NUMERIC) and a one-line provenance note;
  EXEMPTED    inside a data-block assignment or a function that the same
              JSON exempts AS A CLASSIFIED UNIT (e.g. the verbatim paper
              table TABLE1 [SPEC], the mixture registry [SPEC], plot/figure
              code [presentation], literature-anchor validate rows [SPEC]).

Anything else FAILS, printing the exact JSON snippet to add: a new number
cannot enter the physics without arriving together with its class and
provenance (see validation/dof_audit.md).

Scope: src/**/*.py except src/style.py (pure presentation constants).
Strings/docstrings are never scanned; -x parses as USub(x) so signs are
structural; booleans are excluded.

Usage:
    python tests/test_numeric_lint.py               # lint (suite mode)
    python tests/test_numeric_lint.py --inventory   # JSON skeleton of every
                                                    # currently unlisted literal
"""
import ast
import fnmatch
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWLIST = os.path.join(ROOT, 'validation', 'numeric_allowlist.json')
SCOPE_DIR = os.path.join(ROOT, 'src')
SKIP_FILES = {'src/style.py'}                 # presentation-only module

TRIVIAL_INT = 12                              # |int| <= 12: arity/index/algebra
TRIVIAL_FLOAT = {0.25, 0.5, 0.75, 100.0, 1000.0, 1e6}   # fractions + scalers

CLASSES = ('SPEC', 'MODEL-CONST', 'EMPIRICAL', 'NUMERIC')


def _key(v):
    """Canonical allowlist key for a literal (stable across int/float forms)."""
    return repr(v)


def is_trivial(v):
    if isinstance(v, int):
        return abs(v) <= TRIVIAL_INT or float(v) in TRIVIAL_FLOAT
    return v in TRIVIAL_FLOAT or (float(v).is_integer() and abs(v) <= TRIVIAL_INT)


def scan_file(path, spec):
    """Yield (lineno, value) for every non-trivial literal outside exemptions."""
    src = open(path, encoding='utf-8').read()
    tree = ast.parse(src, filename=path)
    exf = list(spec.get('exempt_functions', {}))
    exa = set(spec.get('exempt_assignments', {}))
    skip = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if any(fnmatch.fnmatch(node.name, p) for p in exf):
                skip.append((node.lineno, node.end_lineno))
        elif isinstance(node, ast.Assign):
            if any(isinstance(t, ast.Name) and t.id in exa for t in node.targets):
                skip.append((node.lineno, node.end_lineno))
    for node in ast.walk(tree):
        if (isinstance(node, ast.Constant)
                and isinstance(node.value, (int, float))
                and not isinstance(node.value, bool)):
            ln = node.lineno
            if any(a <= ln <= b for a, b in skip):
                continue
            if not is_trivial(node.value):
                yield ln, node.value


def iter_scope():
    for dirpath, _dirs, files in os.walk(SCOPE_DIR):
        for f in sorted(files):
            if f.endswith('.py'):
                full = os.path.join(dirpath, f)
                rel = os.path.relpath(full, ROOT).replace(os.sep, '/')
                if rel not in SKIP_FILES:
                    yield rel, full


def load_allowlist():
    with open(ALLOWLIST, encoding='utf-8') as f:
        return json.load(f)['files']


def lint():
    """Return (violations, bad_entries): unlisted literals and malformed
    allowlist entries (missing class/note - the classification IS the point)."""
    AL = load_allowlist()
    violations, bad = [], []
    for rel, full in iter_scope():
        spec = AL.get(rel, {})
        vals = spec.get('values', {})
        for section in ('values', 'exempt_functions', 'exempt_assignments'):
            for k, meta in spec.get(section, {}).items():
                if (not isinstance(meta, dict) or not meta.get('note')
                        or (section == 'values'
                            and meta.get('cls') not in CLASSES)):
                    bad.append('%s: %s %r lacks cls/note' % (rel, section, k))
        for ln, v in scan_file(full, spec):
            if _key(v) not in vals:
                violations.append((rel, ln, v))
    return violations, bad


def inventory():
    """Print a ready-to-classify JSON skeleton of every unlisted literal."""
    try:
        AL = load_allowlist()
    except (OSError, KeyError, ValueError):
        AL = {}
    out = {}
    for rel, full in iter_scope():
        spec = AL.get(rel, {})
        vals = spec.get('values', {})
        seen = {}
        for ln, v in scan_file(full, spec):
            if _key(v) not in vals:
                seen.setdefault(_key(v), []).append(ln)
        if seen:
            out[rel] = {k: {'cls': '?', 'note': 'lines %s' %
                            ','.join(map(str, lns[:6]))}
                        for k, lns in sorted(seen.items())}
    print(json.dumps(out, indent=1))
    print('/* files: %d, distinct unlisted literals: %d */'
          % (len(out), sum(len(v) for v in out.values())))


def run():
    violations, bad = lint()
    for rel, ln, v in violations[:40]:
        print('  UNLISTED %s:%d  %r  -> add to validation/numeric_allowlist'
              '.json under "%s"."values" as %s: {"cls": "...", "note": "..."}'
              % (rel, ln, v, rel, json.dumps(_key(v))))
    for msg in bad[:40]:
        print('  MALFORMED ' + msg)
    nfiles = len(list(iter_scope()))
    ok = not violations and not bad
    print('  %-52s %s (%d files scanned, %d unlisted, %d malformed)'
          % ('numeric lint: src/ literals all classified',
             'PASS' if ok else 'FAIL', nfiles, len(violations), len(bad)))
    return ok


if __name__ == '__main__':
    if '--inventory' in sys.argv:
        inventory()
    else:
        sys.exit(0 if run() else 1)
