#!/usr/bin/env python
"""anchor_census.py — MEASURED census of line-number anchors ("D6 :NNN",
"M0:NNNN", "file.md:NNN-MMM") vs stable named anchors ("file.md#heading",
registry ids) across the typed registries, the tools and the core docs.
S-REVIEW lever F3 (2026-09-05): the input of the migration plan to
stable ids (line-number anchors drift on every insertion; the D6 addendum
of 2026-09-05 had to be appended at EOF for exactly this reason).

Also checks RESOLUTION of docname:NNN anchors: the line must exist (a
line number beyond EOF = a dead anchor, reported). Text-drift cannot be
checked without stored context; the migration plan (assessment, lever F3)
adds the id-based form with a resolution lint.

Usage: python tools/anchor_census.py [--json]     exit 0 = report only
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['docs/findings_registry.yaml', 'docs/choice_ledger.yaml',
         'docs/claims_registry.yaml', 'docs/literature_registry.yaml',
         'docs/glossary.yaml', 'docs/flag_registry.yaml',
         'tools/roadmap_derive.py', 'tests/test_roadmap_coverage.py',
         'docs/rde_nozzle_pipeline_decision_map.md', 'docs/rde_nozzle_MASTER.md',
         'docs/rde_nozzle_development_plan.md', 'docs/rde_nozzle_PROGRESS.md',
         'docs/START_HERE.md', 'validation/ADVISORY_INDEX.md']
DOCMAP = {'D6': 'docs/rde_nozzle_development_plan.md', 'M0': 'docs/rde_nozzle_MASTER.md',
          'D1': 'docs/rde_nozzle_problem_book.md', 'D3': 'docs/rde_nozzle_theorem_ledger.md',
          'PROGRESS': 'docs/rde_nozzle_PROGRESS.md'}
RX_DOC = re.compile(r'\b(D6|M0|D1|D3|PROGRESS)\s?:(\d{2,4})(?:-(\d{2,4}))?\b')
RX_FILE = re.compile(r'([A-Za-z0-9_./-]+\.(?:md|yaml|py)):(\d{2,4})(?:-(\d{2,4}))?\b')
RX_NAMED = re.compile(r'([A-Za-z0-9_./-]+\.(?:md|yaml|py))#([^\s|)\]]{3,80})')
RX_ID = re.compile(r'\[(?:T|D|C|S|X|P|L4|OBJ-DOM|MS|R\d)-?[A-Za-z0-9-]*\]')


SEARCH_DIRS = ['', 'validation', 'docs', 'tests', 'tools', 'src', 'docs/atlas']


def _resolve(rel):
    """Bare filenames in the registries are cited relative to validation/ or
    docs/ (the record's convention); try the repo root, the standard dirs,
    then a recursive basename match under validation/ (raws subdirs)."""
    for d in SEARCH_DIRS:
        p = os.path.join(ROOT, d, rel)
        if os.path.exists(p):
            return p
    base = os.path.basename(rel)
    for dirpath, _, files in os.walk(os.path.join(ROOT, 'validation')):
        if base in files:
            return os.path.join(dirpath, base)
    return None


def _lines(rel):
    p = _resolve(rel)
    if p is None:
        return None
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read().splitlines()


def census():
    out = {}
    nlines = {}
    for rel in FILES:
        lines = _lines(rel)
        if lines is None:
            continue
        text = '\n'.join(lines)
        doc = RX_DOC.findall(text)
        fil = RX_FILE.findall(text)
        named = RX_NAMED.findall(text)
        ids = RX_ID.findall(text)
        dead = []
        for d, a, b in doc:
            tgt = DOCMAP[d]
            if tgt not in nlines:
                l = _lines(tgt); nlines[tgt] = len(l) if l else 0
            if int(a) > nlines[tgt]:
                dead.append('%s:%s' % (d, a))
        for f_, a, b in fil:
            rel_t = f_.replace('\\', '/')
            if rel_t not in nlines:
                l = _lines(rel_t); nlines[rel_t] = len(l) if l else -1
            if nlines[rel_t] == -1:
                dead.append('%s:%s (file missing)' % (f_, a))
            elif int(a) > nlines[rel_t]:
                dead.append('%s:%s' % (f_, a))
        out[rel] = dict(docname_line=len(doc), file_line=len(fil), named_anchor=len(named),
                        bracket_ids=len(ids), dead_line_anchors=dead)
    return out


def render(c):
    tot = dict(docname_line=0, file_line=0, named_anchor=0, bracket_ids=0, dead=0)
    rows = ['== ANCHOR CENSUS (tools/anchor_census.py, measured) ==',
            '%-46s %8s %8s %8s %8s %6s' % ('file', 'doc:NNN', 'file:NNN', 'named#', '[ids]', 'dead')]
    for rel, v in c.items():
        rows.append('%-46s %8d %8d %8d %8d %6d' % (rel, v['docname_line'], v['file_line'],
                                                    v['named_anchor'], v['bracket_ids'], len(v['dead_line_anchors'])))
        for k in ('docname_line', 'file_line', 'named_anchor', 'bracket_ids'):
            tot[k] += v[k]
        tot['dead'] += len(v['dead_line_anchors'])
    rows.append('%-46s %8d %8d %8d %8d %6d' % ('TOTAL', tot['docname_line'], tot['file_line'],
                                                tot['named_anchor'], tot['bracket_ids'], tot['dead']))
    line_total = tot['docname_line'] + tot['file_line']
    stable_total = tot['named_anchor'] + tot['bracket_ids']
    rows.append('line-number anchors %d vs stable anchors %d (named# + [ids]); dead line anchors %d'
                % (line_total, stable_total, tot['dead']))
    for rel, v in c.items():
        if v['dead_line_anchors']:
            rows.append('  DEAD in %s: %s' % (rel, ', '.join(v['dead_line_anchors'][:12])))
    return '\n'.join(rows)


if __name__ == '__main__':
    c = census()
    print(json.dumps(c, indent=1) if '--json' in sys.argv else render(c))
