#!/usr/bin/env python
"""Agnosticity lint for the S-REVIEW de-novo stage (carrier §C.2/§C.3 + §G.1).

Two modes:
  --statement <file>   the agnostic PROBLEM STATEMENT: zero repo registry ids,
                       zero repo codenames, zero CONSTITUTION terms (the
                       program's own paradigm words: cycle-averaged, per-phase,
                       TWIN, quasi-steady, and the incumbent method names).
  --output <file>...   de-novo deriver OUTPUTS: zero repo registry ids and
                       zero repo codenames (a hit = the deriver read the repo
                       = tainted output, discard + re-run the lens).
  --selftest           seeded rejectors: a doctored statement carrying one
                       item of each class MUST FAIL; the clean statement MUST
                       PASS (dual-seed: the lint must be able to REJECT and
                       must not reject the clean object).

Exit code 0 = PASS, 1 = FAIL. Every hit is printed with class, pattern,
line number and the matched text. No magic thresholds: any hit fails.
"""
import re
import sys

# --- class 1: repo REGISTRY IDS / typed anchors ---------------------------
REGISTRY_IDS = [
    r"\[X-[A-Z0-9]+\]", r"\bX-[A-Z]{2,}[A-Z0-9]*\b",       # carriers X-O32, X-LOCD, ...
    r"\[T-[A-Z0-9-]+\]", r"\[S-[A-Z0-9-]+\]", r"\[D-[A-Z0-9-]+\]",
    r"\[P-[A-Z0-9-]+\]", r"\[R\d+[A-Z]*(?:-[A-Z0-9-]+)?\]", r"\[C-[A-Z0-9-]+\]",
    r"\[L4-[A-Z-]+\]", r"\[OBJ-DOM[A-Z-]*\]", r"\[MS-[A-Z-]+\]",
    r"\bGAP-\d+\b", r"\bR-TWIN-\d\b", r"\bR\d{1,2}c\b",
    r"\bC\d{1,2}\b(?![\^\d,])",                             # ledger rows C1..C62 (not C^1)
    r"\bOP-\d+\b", r"\bPB-\d\b", r"\bH-T3\.\d\b", r"\bH-[A-Z]\d\b",
    r"\bN\d\b(?=-class| channel|\))",                        # novelty channels N1..N6
    r"\bO3\.\d\b", r"\bO[1-5]\b(?= oracle)",
    r"\bF2\.[A-Z-]+\b", r"\bF[0-6]b?\b(?=[ /.,:;)])", r"\bF[0-6]-B0\b",
    r"\bG[0-6]\b(?= gate|\))", r"\bS-[A-Z]{3,}\b",              # phases/gates/sessions
    r"\bsession S\d{1,2}\b", r"\bS\d{1,2}bis\b",                 # session names (unambiguous forms only; bare S<n> = deriver strategy labels)
    r"\bE-?\d{1,2}\b(?= edge)", r"\bMAP-AM-\d\b", r"\bSR-\d{1,2}\b",
    r"\bDUTY-\d+\b", r"\bISS-\d\b", r"\bCKP-", r"\bR22F?\b", r"\bU3'?\b(?= |$)",
    r"\bB-[A-Z]{3,}\b", r"\bB\d{1,2}\b(?=\()",                  # BLOCCATO rows
    r"\bA-REPR\b", r"\bA-1\b(?= amendment| margin)",
]
# --- class 2: repo CODENAMES / documents / tools --------------------------
CODENAMES = [
    r"\bGENO\b", r"\bMoC_Gen\b", r"\bRaoPlug\b", r"\bJAX\b", r"\bscipy\b",
    r"\bCantera\b", r"\bEnzyme\b", r"\bClarabel\b", r"\bMOSEK\b",
    r"\bM0\b", r"\bD[1-8]\b(?= |\)|,|§)", r"\bPROGRESS\b", r"\bADVISORY\b",
    r"\bMASTER\b", r"\bproblem book\b", r"\bchoice[ _]ledger\b",
    r"\bfindings[ _]registry\b", r"\bclaims[ _]registry\b", r"\bROADMAP\b",
    r"\bof record\b", r"\bcarrier\b", r"\bPIANO\b", r"\bcensus\b",
    r"\bS-FOUNDATIONS\b", r"\bS-CERT\b", r"\bS-ORDINE\b", r"\bS-PRES\b",
    r"\bS-REVIEW\b", r"\bS-ROADMAP\b", r"\bF2-B0\b", r"\bTWIN\b",
    r"\bK_RICH\b", r"\bNEWTON_TOL_FACTOR\b", r"\bcert_worst\b", r"\bm_stop\b",
    r"\bcertdiag\b", r"\bondemand\b", r"\benvfp\b", r"\bMC8\b",
    r"\brde-lecture-code\b", r"\bvalidation/", r"\bdocs/", r"\btools/",
    r"\bA1[ _]brick\b", r"\bbrick[ -]2\b", r"\bB-lite\b", r"\broute-B\b",
    r"\bfive-field\b", r"\b4-field\b", r"\bfour-field\b", r"\bS-5F\b",
    r"\bI[0-4]\b(?= interface| rung|\))",                       # idealization ladder ids
    r"\bcase [A-G]\b(?= of| data| \()",                        # Annex-B case letters used as ids
    r"\bAnnex B\b", r"\bPart (?:I|II|III|IV|V|VI|VII)\b",
    r"\bVI\.\d\b", r"\bD2\.\d\b",
    r"\bKraiko school\b", r"\bZucrow Ch\.\s?1[67]\b",
]
# --- class 3: CONSTITUTION terms (statement only; §G.1) -------------------
CONSTITUTION = [
    r"cycle[- ]averag", r"per[- ]phase", r"per[- ]state thrust", r"\bTWIN\b",
    r"quasi[- ]?stead", r"quasi[- ]?station", r"\bsteadif",
    r"\badjoint\b", r"\bMoC\b", r"method of characteristics",
    r"characteristic[- ]marching", r"space[- ]marching", r"\bspline\b",
    r"trust[- ]region", r"\bRichardson\b", r"\bKS[- ]aggregat",
    r"\bdual[- ]code\b", r"\bfitted[- ]front", r"\bshock[- ]fitt",
    r"\bplug truncated\b", r"\btruncated plug\b(?= head-to-head| twin)",
    r"\bhead-to-head\b", r"\bwave[- ]frame\b(?= anchor| solve)",
    r"\bcollapse dichotom", r"\bmeasure selects\b", r"\bRao-at-",
    r"\bbound ladder\b", r"\bdeflat", r"\bsector tournament\b",
    r"\bcertificate-first\b", r"\bS1 class\b", r"\brung[- ]?[0-3]\b",
]

def scan(text, classes):
    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for cname, pats in classes:
            for p in pats:
                for m in re.finditer(p, line):
                    hits.append((cname, p, lineno, m.group(0), line.strip()[:100]))
    return hits

PUBLIC_OK_IN_OUTPUT = {r"\bJAX\b", r"\bscipy\b", r"\bCantera\b", r"\bEnzyme\b", r"\bClarabel\b",
                       r"\bMOSEK\b", r"\bof record\b"}   # public libraries / generic English: leaks only in the STATEMENT

def lint(path, mode):
    text = open(path, encoding="utf-8").read()
    codenames = CODENAMES if mode == "statement" else [c for c in CODENAMES if c not in PUBLIC_OK_IN_OUTPUT]
    classes = [("REGISTRY-ID", REGISTRY_IDS), ("CODENAME", codenames)]
    if mode == "statement":
        classes.append(("CONSTITUTION", CONSTITUTION))
    hits = scan(text, classes)
    return hits

CLEAN = """# Problem
A rotating detonation engine exhausts through one fixed axisymmetric nozzle.
The inflow surface carries time-resolved gas states over the wave period.
Find the nozzle shape that maximizes the time-mean thrust of the unsteady
flow under length, exit-radius and attachment constraints, with certified
error bars; the gas is a frozen thermally-perfect mixture (gamma varies with
temperature); regularity: continuously differentiable with Lipschitz slope.
The reference accuracy class of a thrust stand is 0.5-1%. Data classes range
from specs-only to full coupling. Solution concept and derivative computation
are the solver's choices to derive and defend.
"""
SEEDS = {
    "REGISTRY-ID": "the certification frontier moved as in [X-LOCD] and row C31.",
    "CODENAME": "the reference Fortran code GENO and the JAX stack are given.",
    "CONSTITUTION": "use the cycle-averaged functional with a per-phase adjoint.",
}

def selftest():
    import tempfile, os
    ok = True
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "clean.md")
        open(p, "w", encoding="utf-8").write(CLEAN)
        h = lint(p, "statement")
        print("clean statement: %d hits -> %s" % (len(h), "PASS" if not h else "FAIL (lint over-fires)"))
        for x in h:
            print("   ", x)
        ok &= not h
        for cname, seed in SEEDS.items():
            q = os.path.join(d, "seed_%s.md" % cname)
            open(q, "w", encoding="utf-8").write(CLEAN + "\n" + seed + "\n")
            mode = "statement" if cname == "CONSTITUTION" else "output"
            h = lint(q, mode)
            classes = {x[0] for x in h}
            fired = cname in classes
            print("seeded rejector [%s] in mode %s: %s" % (cname, mode, "REJECTED (as required)" if fired else "NOT REJECTED = LINT DEFECT"))
            ok &= fired
        # the output mode must NOT fire on constitution terms (derivers may propose them)
        q = os.path.join(d, "seed_const_output.md")
        open(q, "w", encoding="utf-8").write(CLEAN + "\n" + SEEDS["CONSTITUTION"] + "\n")
        h = lint(q, "output")
        print("constitution terms in OUTPUT mode: %d hits -> %s" % (len(h), "PASS (allowed)" if not h else "FAIL (must be allowed)"))
        ok &= not h
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1

def main(argv):
    if not argv or argv[0] == "--selftest":
        return selftest()
    mode = {"--statement": "statement", "--output": "output"}.get(argv[0])
    if mode is None:
        print(__doc__); return 2
    rc = 0
    for path in argv[1:]:
        hits = lint(path, mode)
        print("%s [%s]: %d hits -> %s" % (path, mode, len(hits), "PASS" if not hits else "FAIL"))
        for cname, pat, ln, matched, ctx in hits:
            print("   %-12s line %4d  %-28r  <- %s" % (cname, ln, matched, ctx))
        rc |= 1 if hits else 0
    return rc

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
