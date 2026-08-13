#!/usr/bin/env python3
"""Duty D-14 (extended) — INDEX.md <-> disk consistency lint for literature_review/.

Three independent channels, each with a seeded rejector:

  (i)   NAME   every `*.pdf` filename cited anywhere in INDEX.md exists on disk
                -> original C9 channel (5 hand-found misalignments, 2026-08-13)
  (ii)  COVER  every PDF on disk appears in the ACQUISITI list
  (iii) COUNT  count(*.pdf on disk) == len(ACQUISITI list) == declared number

Channel (iii) is the one that was missing when the 2026-08-13 06:10 delivery
landed: five PDFs appeared on disk, no cited filename was wrong, and the
declared count silently stayed at 20 while the folder held 25. A lint that
only checks (i) cannot fire on that class of staleness.

Usage:
    python lint_index_consistency.py              # lint, exit 0 / 1
    python lint_index_consistency.py --selftest   # run the three seeded rejectors
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDEX = HERE / "INDEX.md"

# "**25 PDF in cartella**" / "25 PDF in cartella"
DECLARED_RE = re.compile(r"\*{0,2}(\d+)\s+PDF\s+in\s+cartella\*{0,2}")
# "ACQUISITI (25)" ... up to the blank line that ends the list block
ACQ_HEADER_RE = re.compile(r"ACQUISITI\s*\((\d+)\)")
# any `backticked_token` that looks like a paper slug (with or without .pdf)
TICKED_RE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_.\- ()]*)`")

# Filenames cited in INDEX.md that are ABSENT FROM DISK BY DESIGN. Each needs a
# stated reason; the set is deliberately tiny so it cannot be used to silence a
# real (i)-channel miss.
EXEMPT_ABSENT = {
    "autore_anno_slug.pdf": "naming template, not a file",
    "aerospace-10-00797 (1).pdf": "duplicate removed 2026-08-13 (md5 identical to ancourt_2023)",
    "s12567-023-00511-1 (2).pdf": "duplicate removed 2026-08-13 (md5 identical to fernandes_2023)",
}


def parse_index(text):
    """Return (declared_count, acquisiti_header_count, acquisiti_slugs, cited_pdf_names)."""
    m = DECLARED_RE.search(text)
    declared = int(m.group(1)) if m else None

    lines = text.splitlines()
    acq_count, acq_slugs = None, []
    for i, line in enumerate(lines):
        m = ACQ_HEADER_RE.search(line)
        if not m:
            continue
        acq_count = int(m.group(1))
        # consume from this line until the first blank line
        block = []
        for line2 in lines[i:]:
            if not line2.strip():
                break
            block.append(line2)
        for tok in TICKED_RE.findall("\n".join(block)):
            tok = tok.strip()
            if tok.endswith(".pdf"):
                tok = tok[:-4]
            acq_slugs.append(tok)
        break

    cited = {t.strip() for t in TICKED_RE.findall(text) if t.strip().endswith(".pdf")}
    return declared, acq_count, acq_slugs, cited


def lint(index_path=INDEX, folder=HERE, verbose=True):
    text = index_path.read_text(encoding="utf-8")
    declared, acq_count, acq_slugs, cited = parse_index(text)

    on_disk = sorted(p.name for p in folder.glob("*.pdf"))
    on_disk_slugs = {n[:-4] for n in on_disk}
    violations = []

    # -- channel (i) NAME ----------------------------------------------------
    for name in sorted(cited):
        if name not in on_disk and name not in EXEMPT_ABSENT:
            violations.append(f"(i) NAME  cited in INDEX but absent from disk: {name}")

    # -- channel (ii) COVER --------------------------------------------------
    acq_set = set(acq_slugs)
    for slug in sorted(on_disk_slugs - acq_set):
        violations.append(f"(ii) COVER PDF on disk missing from ACQUISITI list: {slug}.pdf")
    for slug in sorted(acq_set - on_disk_slugs):
        violations.append(f"(ii) COVER ACQUISITI entry with no file on disk: {slug}")

    # -- channel (iii) COUNT -------------------------------------------------
    n_disk, n_list = len(on_disk), len(acq_slugs)
    if declared is None:
        violations.append("(iii) COUNT no declared '<N> PDF in cartella' found in INDEX.md")
    elif not (declared == n_disk == n_list):
        violations.append(
            f"(iii) COUNT mismatch: declared={declared} disk={n_disk} acquisiti_list={n_list}"
        )
    if acq_count is not None and acq_count != n_list:
        violations.append(
            f"(iii) COUNT 'ACQUISITI ({acq_count})' header disagrees with its own list ({n_list})"
        )

    if verbose:
        print(f"INDEX: {index_path}")
        print(f"  declared={declared}  disk={n_disk}  acquisiti_list={n_list}  cited_filenames={len(cited)}")
        if violations:
            print(f"  VIOLATIONS ({len(violations)}):")
            for v in violations:
                print("   -", v)
        else:
            print("  0 violations  (channels i, ii, iii all clean)")
    return violations


# --------------------------------------------------------------------------
# Seeded rejectors: each MUST produce >=1 violation on its own channel.
# A detector that does not fire on its seed is broken.
# --------------------------------------------------------------------------
def _selftest():
    import shutil, tempfile

    baseline = lint(verbose=False)
    if baseline:
        print("SELFTEST ABORT: baseline is not clean; fix the real violations first.")
        for v in baseline:
            print("   -", v)
        return 1

    ok = True
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        for p in HERE.glob("*.pdf"):
            (td / p.name).touch()          # names only; content irrelevant to the lint
        idx = td / "INDEX.md"
        original = INDEX.read_text(encoding="utf-8")

        seeds = {
            # (i) rename a file on disk -> its cited name no longer resolves
            "i-NAME": lambda t: (
                (td / "wolanski_2013_detonative_propulsion_survey.pdf").rename(
                    td / "wolanski_2013_DOCTORED.pdf"
                ),
                t,
            )[1],
            # (ii) add a PDF nobody listed
            "ii-COVER": lambda t: ((td / "smuggled_2099_unlisted.pdf").touch(), t)[1],
            # (iii) alter ONLY the declared number, list left correct
            "iii-COUNT": lambda t: DECLARED_RE.sub("**20 PDF in cartella**", t, count=1),
        }

        for label, seed in seeds.items():
            # reset the sandbox
            for p in td.glob("*.pdf"):
                p.unlink()
            for p in HERE.glob("*.pdf"):
                (td / p.name).touch()
            idx.write_text(seed(original), encoding="utf-8")
            found = lint(index_path=idx, folder=td, verbose=False)
            channel = label.split("-")[0]
            fired = [v for v in found if v.startswith(f"({channel})")]
            status = "FIRED" if fired else "DID NOT FIRE  <-- DETECTOR BROKEN"
            print(f"  seed {label:10s} -> {status}" + (f"  [{fired[0]}]" if fired else ""))
            ok = ok and bool(fired)

    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    sys.exit(1 if lint() else 0)
