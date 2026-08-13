# S-ORDINE S12 NOTHING-LOST GATE (contract 4-ter: (ii) destination map
# verified by machine, (iii) seeded rejectors that MUST fire, exit-code
# gated). Reads validation/sordine_raws_2026-08-13/s12_at_risk_ledger.yaml
# and verifies EVERY item's destination resolves. One unresolved item =
# FAIL (exit 1) — session cannot close R3 on a red gate.
import io, os, re, subprocess, sys

RAWS = "validation/sordine_raws_2026-08-13"
LEDGER = RAWS + "/s12_at_risk_ledger.yaml"
MEMDIR = os.path.expanduser("~") + "/.claude/projects/c--Users-amont-Claude-Projects-Presentazione-RDE-CVA-rde-lecture-code/memory"

def read(p): return io.open(p, encoding="utf-8", errors="replace").read()

REG_FILES = ["docs/findings_registry.yaml", "docs/choice_ledger.yaml",
             "docs/literature_registry.yaml", "docs/flag_registry.yaml"]
reg_ids = set()
for f in REG_FILES:
    for m in re.finditer(r"^\s*-\s+id:\s*['\"]?([^'\"\n]+)", read(f), re.M):
        reg_ids.add(m.group(1).strip())
    # flag registry may key rows by 'flag:' instead of 'id:'
    for m in re.finditer(r"^\s*-\s+flag:\s*['\"]?([A-Z0-9_]+)", read(f), re.M):
        reg_ids.add(m.group(1).strip())
index_txt = read("validation/ADVISORY_INDEX.md")
gloss_txt = read("docs/glossary.yaml")
progress_txt = read("docs/rde_nozzle_PROGRESS.md")

def dest_ok(dest):
    dest = dest.strip()
    kind, _, val = dest.partition(":")
    val = val.strip()
    if kind == "registry":
        return val in reg_ids
    if kind == "index":
        base = os.path.basename(val)
        return os.path.exists("validation/" + base) and base in index_txt
    if kind == "glossary":
        return val.rstrip("*") in gloss_txt
    if kind == "archive":
        return os.path.exists("docs/rde_nozzle_PROGRESS_ARCHIVE.md")
    if kind == "memory":
        return os.path.exists(MEMDIR + "/" + os.path.basename(val))
    if kind == "committed":
        return subprocess.call(["git", "cat-file", "-e", val],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    if kind == "queued":
        m = re.match(r"tranche-([cde])", val)
        return bool(m) and ("tranche" in progress_txt and "(%s)" % m.group(1) in progress_txt)
    return False

def parse_ledger(text):
    items = []
    cur = {}
    for line in text.splitlines():
        m = re.match(r"^\s*-\s+id:\s*(LR-\d+)", line)
        if m:
            if cur: items.append(cur)
            cur = {"id": m.group(1)}
            continue
        for k in ("item", "source", "destination", "status"):
            m = re.match(r"^\s+%s:\s*['\"]?(.+?)['\"]?\s*$" % k, line)
            if m and cur is not None:
                cur[k] = m.group(1)
    if cur: items.append(cur)
    return items

def run(items, label):
    bad = []
    for it in items:
        d = it.get("destination", "")
        if not d or it.get("status", "").upper() == "UNRESOLVED" or not dest_ok(d):
            bad.append((it.get("id", "?"), d or "<none>"))
    print("[%s] items=%d unresolved=%d" % (label, len(items), len(bad)))
    for i, d in bad[:10]:
        print("  UNRESOLVED %s -> %s" % (i, d))
    return len(bad)

items = parse_ledger(read(LEDGER))
assert items, "empty ledger parse"
real_bad = run(items, "REAL")

# SEEDED REJECTOR 1: strip one destination in-memory -> gate MUST fail.
import copy
doct = copy.deepcopy(items)
passing = next(i for i, it in enumerate(doct)
               if it.get("destination") and it.get("status","").upper() != "UNRESOLVED"
               and dest_ok(it["destination"]))
doct[passing]["destination"] = ""
rej1 = run(doct, "REJECTOR-strip") > real_bad
# SEEDED REJECTOR 2: canary item absent from every corpus -> MUST fail.
doct2 = copy.deepcopy(items)
doct2.append({"id": "LR-CANARY", "item": "canary finding that exists nowhere",
              "source": "seeded", "destination": "registry:canary:does-not-exist",
              "status": "RESOLVED"})
rej2 = run(doct2, "REJECTOR-canary") > real_bad
print("rejector-strip fired: %s ; rejector-canary fired: %s" % (rej1, rej2))
ok = (real_bad == 0) and rej1 and rej2
print("S12 GATE:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
