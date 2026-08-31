#!/usr/bin/env python3
"""record_query.py — structured grep over the FIXED manifest of record
files (S-ROADMAP U2, 2026-08-31; navigation-first directive: every content
answer starts from the record, never from recall).

    python tools/record_query.py <regex> [--kind md|yaml|all] [--max N]
    python tools/record_query.py --manifest        # list + resolve check

Output, one hit per line:
    <path>:<line> | <anchor> | <class> | <matching line>
  anchor = for .md files the nearest preceding heading (## ...) or the
           `[TAG]`/THEOREM-style label on the line; for .yaml registries
           the enclosing entry id;
  class  = for registries the entry's status/class/path fields when
           present (findings: status+path; claims: class; choice: status;
           literature: status); for .md the rigor class token found on
           the line (THEOREM* / THEOREM / SCHEMA / CONJECTURE / PRACTICE)
           or '-'.

The MANIFEST is fixed here (not discovered at runtime) so that a moved
record file is a LINT FAILURE (tests/test_roadmap_coverage.py (c)), never
a silent hole in navigation.  Globs are allowed for dated logs and the
atlas chapters.
"""
import glob
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

MANIFEST = (
    # L0 / governance
    'CLAUDE.md',
    'docs/START_HERE.md',
    'docs/rde_nozzle_SCAFFOLD.md',
    # theory of record (M0 + D1-D8)
    'docs/rde_nozzle_MASTER.md',
    'docs/rde_nozzle_problem_book.md',
    'docs/rde_nozzle_literature_map.md',
    'docs/rde_nozzle_theorem_ledger.md',
    'docs/rde_nozzle_claims_verdict.md',
    'docs/rde_nozzle_general_scheme_panel.md',
    'docs/rde_nozzle_development_plan.md',
    'docs/rde_nozzle_pipeline_audit.md',
    'docs/rde_nozzle_panel_2026-07-22.md',
    'docs/rde_nozzle_remaining_conditionals.md',
    'docs/rde_nozzle_conditionals.md',
    'docs/rde_nozzle_pipeline_decision_map.md',
    # atlas
    'docs/atlas/*.md',
    # typed registries (machine-linted)
    'docs/claims_registry.yaml',
    'docs/findings_registry.yaml',
    'docs/choice_ledger.yaml',
    'docs/literature_registry.yaml',
    'docs/glossary.yaml',
    'docs/flag_registry.yaml',
    # living state + roadmap + archive
    'docs/rde_nozzle_PROGRESS.md',
    'docs/rde_nozzle_PROGRESS_ARCHIVE.md',
    'docs/ROADMAP_critical_path.md',
    # papers
    'docs/rde_nozzle_P1_skeleton.md',
    'docs/rde_nozzle_P2_outline.md',
    'docs/paper/P1_outline.md',
    # validation record layer: index + session logs
    'validation/ADVISORY_INDEX.md',
    'validation/PROGRESS_*.md',
)

CLASS_RX = re.compile(r'\b(THEOREM\*|THEOREM|SCHEMA|CONJECTURE|PRACTICE)\b')
HEAD_RX = re.compile(r'^(#{1,6})\s+(.*)$')
YAML_ID_RX = re.compile(r'^- id:\s*(\S+)')
YAML_FIELD_RX = re.compile(r'^  (status|class|path|kind):\s*(.*)$')


def resolve_manifest():
    files = []
    for entry in MANIFEST:
        full = os.path.join(ROOT, entry.replace('/', os.sep))
        if any(ch in entry for ch in '*?['):
            files.extend(sorted(glob.glob(full)))
        else:
            files.append(full)
    return files


def query(rx, kind='all', maxhits=200):
    hits = []
    for full in resolve_manifest():
        rel = os.path.relpath(full, ROOT).replace(os.sep, '/')
        is_yaml = rel.endswith('.yaml')
        if kind == 'md' and is_yaml or kind == 'yaml' and not is_yaml:
            continue
        try:
            lines = io.open(full, encoding='utf-8-sig',
                            errors='replace').read().split('\n')
        except OSError:
            continue
        anchor, cur_id, fields = '-', '-', {}
        for i, ln in enumerate(lines, 1):
            if is_yaml:
                m = YAML_ID_RX.match(ln)
                if m:
                    cur_id, fields = m.group(1), {}
                m = YAML_FIELD_RX.match(ln)
                if m:
                    fields[m.group(1)] = m.group(2).strip().strip('"')
            else:
                m = HEAD_RX.match(ln)
                if m:
                    anchor = m.group(2).strip()[:60]
            if rx.search(ln):
                if is_yaml:
                    cls = ' '.join('%s=%s' % (k, fields[k])
                                   for k in ('status', 'class', 'path',
                                             'kind') if k in fields) or '-'
                    a = cur_id
                else:
                    m = CLASS_RX.search(ln)
                    cls = m.group(1) if m else '-'
                    a = anchor
                hits.append((rel, i, a, cls, ln.strip()[:160]))
                if len(hits) >= maxhits:
                    return hits, True
    return hits, False


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__)
        return 0
    if argv[0] == '--manifest':
        bad = 0
        for entry in MANIFEST:
            full = os.path.join(ROOT, entry.replace('/', os.sep))
            ok = (bool(glob.glob(full)) if any(c in entry for c in '*?[')
                  else os.path.isfile(full))
            bad += 0 if ok else 1
            print('%s %s' % ('ok ' if ok else 'MISSING', entry))
        print('%d entries, %d missing' % (len(MANIFEST), bad))
        return 0 if bad == 0 else 1
    kind, maxhits, pat = 'all', 200, None
    it = iter(argv)
    for a in it:
        if a == '--kind':
            kind = next(it)
        elif a == '--max':
            maxhits = int(next(it))
        else:
            pat = a
    if pat is None:
        print('usage: record_query.py <regex> [--kind md|yaml|all] [--max N]')
        return 2
    rx = re.compile(pat, re.I)
    hits, truncated = query(rx, kind, maxhits)
    out = io.open(sys.stdout.fileno(), 'w', encoding='utf-8',
                  errors='replace', closefd=False)
    for rel, i, a, cls, txt in hits:
        out.write('%s:%d | %s | %s | %s\n' % (rel, i, a, cls, txt))
    out.write('%d hits%s\n' % (len(hits),
                               ' (TRUNCATED at --max)' if truncated else ''))
    out.flush()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
