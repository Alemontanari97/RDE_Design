#!/usr/bin/env python
"""check_tables.py — rejector for the E2 (hypotheses) and E3 (completeness)
tables of S-REVIEW (refuter PROMPT-29): every table row has no empty cell;
every GAP/missing cell names an owner; every findings id quoted as `id:`-
style (`family:slug`) resolves in docs/findings_registry.yaml; a seeded
doctored table (empty cell, dangling id) MUST FAIL. Exit 0 = PASS.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
E2 = os.path.join(HERE, 'TABLE_E2_hypotheses_by_stage.md')
E3 = os.path.join(HERE, 'TABLE_E3_completeness_by_stage.md')
REG = os.path.join(ROOT, 'docs', 'findings_registry.yaml')
ID_RX = re.compile(r'`([a-z0-9-]+:[a-z0-9-]+(?:-[a-z0-9]+)*)`')


def rows(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('|') and not line.startswith('|---') and not line.startswith('| stage |'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            out.append(cells)
    return out


def check(path, ids, need_owner_cols):
    bad = []
    for i, cells in enumerate(rows(path), 1):
        if any(c == '' for c in cells):
            bad.append('row %d empty cell' % i)
        for col in need_owner_cols:
            if col < len(cells) and re.search(r'\bGAP\b|\bmissing\b|\bMISSING\b', cells[col], re.I):
                if not re.search(r'\((?:owner|F[0-9]|user|PAPER|this session|F2|F3)|owner|F2\.|F3\.|PAPER|user|this session', cells[col]):
                    bad.append('row %d: gap/missing without owner: %s' % (i, cells[col][:60]))
        for m in ID_RX.findall(' '.join(cells)):
            if m not in ids:
                bad.append('row %d: dangling findings id `%s`' % (i, m))
    return bad


def main():
    reg = open(REG, encoding='utf-8').read()
    ids = set(re.findall(r'^- id:\s*(\S+)', reg, re.M))
    ok = True
    for path, cols in ((E2, (4,)), (E3, (4, 5))):
        bad = check(path, ids, cols)
        print('%s: %d rows, %s' % (os.path.basename(path), len(rows(path)), 'PASS' if not bad else 'FAIL'))
        for b in bad:
            print('   ', b)
        ok &= not bad
    # seeded rejector: doctored copy must FAIL
    import tempfile
    t = open(E2, encoding='utf-8').read().replace('| THEOREM for the full-flowing', '|  | THEOREM for the full-flowing', 1)
    t += '\n| CLAIM | seeded `no-such:finding-id` | PRACTICE | none | GAP (owner F2) |\n'
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(t); tmp = f.name
    bad = check(tmp, ids, (4,))
    os.unlink(tmp)
    fired = any('empty cell' in b for b in bad) and any('dangling' in b for b in bad)
    print('seeded rejector [doctored E2: empty cell + dangling id]: %s' % ('REJECTED (as required)' if fired else 'NOT REJECTED = CHECK DEFECT'))
    ok &= fired
    print('TABLES', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
