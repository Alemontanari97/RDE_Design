#!/usr/bin/env python3
"""Compare re-run JSON outputs with the committed ones, value by value, wall times excepted.
usage: restamp_compare.py <committed json> <re-run json> [...pairs]"""
import json
import math
import re
import sys

TIMEY = re.compile(r"(^|_)(t|time|times|seconds|sec|secs|elapsed|wall|date|stamp|when|started|ended|t_[a-z_]+)$|seconds|_s$")


def walk(a, b, path, out):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if TIMEY.search(str(k)):
                continue
            if k not in a or k not in b:
                out.append("%s.%s missing in %s" % (path, k, "old" if k not in a else "new"))
                continue
            walk(a[k], b[k], "%s.%s" % (path, k), out)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append("%s len %d vs %d" % (path, len(a), len(b)))
            return
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, "%s[%d]" % (path, i), out)
    else:
        if isinstance(a, float) and isinstance(b, float) and math.isnan(a) and math.isnan(b):
            return
        if a != b:
            out.append("%s: %r vs %r" % (path, a, b))


args = sys.argv[1:]
bad = 0
for old, new in zip(args[0::2], args[1::2]):
    out = []
    walk(json.load(open(old)), json.load(open(new)), "", out)
    print("%-60s %s" % (new.split("/")[-1], "IDENTICAL (times excepted)" if not out else "DIFFERS: %d paths, e.g. %s" % (len(out), "; ".join(out[:3]))))
    bad += bool(out)
sys.exit(1 if bad else 0)
