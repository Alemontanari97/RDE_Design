#!/usr/bin/env python3
"""Extract the pipeline decision map into pipeline_graph.json.

[S-PRES W-A slot A6] De-risk of the walkable-graph deck feature (G-9,
emendamento v2.1 par.6a). STDLIB-ONLY parser (re/json/pathlib), per
GRAPH_VIZ_SPEC.md RENDER MECHANISM: "the node/edge list EXTRACTED from
the map file, never hand-typed - extraction script asserts counts
62/17/45 against the map's machine summary, so a map edit breaks the
build, not the slide truth".

Source of truth: docs/rde_nozzle_pipeline_decision_map.md (refereed,
0 BREAK / 0 REPAIR, [MAP-AM] amendments applied).

RECORD counts asserted (measured from the map itself, both from the
stage tables/section 9 AND from the section-10 machine summary; the
two measurements must agree with each other and with the record):
  - 8 stages
  - 62 ledger nodes  (61 unique stage-table rows + C46, which the map
    deliberately does NOT stage-place: note_C46 in the machine summary)
  - 17 non-ledger nodes (roster set-matched against the machine summary)
  - 45 edge entries in section 9 (44 edges + 1 declared anti-edge E34;
    id set-matched against the machine-summary roster; E33/E37/E40
    asserted ABSENT, unassigned by design)
  - status tally 12 DECIDED / 36 MIXED / 12 NEVER / 2 SINGLE-AUTHOR,
    per-id set-matched against the machine-summary rosters
A failed assert means the map moved: the deck build must BREAK.
"""

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve()
REPO = HERE.parents[3]  # graph_derisk -> spres_raws -> validation -> repo
MAP_PATH = REPO / "docs" / "rde_nozzle_pipeline_decision_map.md"
OUT_PATH = HERE.parent / "pipeline_graph.json"

# ---- record expectations (from the map's own machine summary, section 10) --
EXPECTED_STAGES = 8
EXPECTED_LEDGER = 62
EXPECTED_TABLE_LEDGER = 61  # C46 is note-only by the map's own padding policy
EXPECTED_NONLEDGER = 17
EXPECTED_EDGES = 45
EXPECTED_TALLY = {"DECIDED": 12, "MIXED": 36, "NEVER": 12, "SA": 2}
UNASSIGNED_EDGE_IDS = {"E33", "E37", "E40"}  # never edges, by design
DUAL_FACE_EXPECTED = {"C55", "R22-CFD"}  # counted once, two stage-faces

CELL_SPLIT = re.compile(r"(?<!\\)\|")  # cells may contain escaped \|
NL_MARK = "⊘"  # the map's non-ledger marker


def split_cells(line):
    parts = [c.strip() for c in CELL_SPLIT.split(line)]
    # drop the empty leading/trailing fields of "| a | b |"
    if parts and parts[0] == "":
        parts = parts[1:]
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return parts


def canon_nonledger(cell):
    """Map a non-ledger Node cell to its machine-summary roster token."""
    t = cell.strip().lstrip(NL_MARK).strip()
    if t.startswith("Contract findings block"):
        return "CONTRACT-F1..F10-block"
    head = t.split("—")[0]  # up to em-dash
    if "R22-CFD" in head or t.startswith("3D rung"):
        return "R22-CFD"
    m = re.match(r"\[([^\]]+)\]", t)
    if m:
        return m.group(1)
    return re.split(r"[\s(]", t, maxsplit=1)[0].rstrip(",.")


def parse_stages(text):
    """Return list of stage dicts with their raw table rows parsed."""
    stage_pat = re.compile(r"^## STAGE (\d+) — ([^(\n]+)(?:\(([^)]*)\))?",
                           re.M)
    hits = list(stage_pat.finditer(text))
    stages = []
    for i, h in enumerate(hits):
        start = h.end()
        end = hits[i + 1].start() if i + 1 < len(hits) else text.find(
            "\n## 9.", start)
        body = text[start:end]
        rows = []
        for line in body.splitlines():
            ls = line.strip()
            if not ls.startswith("|"):
                continue
            if ls.startswith("| Node |") or set(ls) <= set("|-: "):
                continue
            cells = split_cells(ls)
            if len(cells) >= 3:
                rows.append(cells)
        stages.append({
            "num": int(h.group(1)),
            "name": h.group(2).strip(),
            "subtitle": (h.group(3) or "").strip(),
            "rows": rows,
        })
    return stages


def build_nodes(stages):
    nodes = OrderedDict()
    for st in stages:
        for cells in st["rows"]:
            node_cell, choice = cells[0], cells[1] if len(cells) > 1 else ""
            status_cell = cells[2] if len(cells) > 2 else ""
            cond = cells[3] if len(cells) > 3 else ""
            duty = cells[4] if len(cells) > 4 else ""
            edges_cell = cells[5] if len(cells) > 5 else ""
            is_nl = (NL_MARK in node_cell) or (NL_MARK in status_cell)
            if is_nl:
                nid = canon_nonledger(node_cell)
                ntype = "nonledger"
                status = status_cell.lstrip(NL_MARK).strip()
            else:
                m = re.match(r"C(\d+)\b", node_cell.strip())
                if not m:
                    raise AssertionError(
                        "unclassifiable table row (stage %d): %r"
                        % (st["num"], node_cell))
                nid = "C" + m.group(1)
                ntype = "ledger"
                status = status_cell.strip()
            if nid in nodes:
                n = nodes[nid]
                n["stage_faces"].append(st["num"])
                if ntype == "ledger" and n["status"] != status:
                    raise AssertionError(
                        "dual-face status mismatch on %s: %r vs %r"
                        % (nid, n["status"], status))
            else:
                nodes[nid] = {
                    "id": nid,
                    "type": ntype,
                    "stage": st["num"],       # primary (first) face
                    "stage_faces": [st["num"]],
                    "choice": choice,
                    "status": status,
                    "conditions": cond,
                    "open_duty": duty,
                    "edges_cell": edges_cell,
                }
    return nodes


def parse_section9(text):
    s9 = text[text.find("\n## 9."):text.find("\n## 10.")]
    surfaces = []
    edges = OrderedDict()
    cur_surface = None
    surf_pat = re.compile(r"\*\*SURFACE ([A-Z]) — (.+?)\*\*")
    edge_pat = re.compile(r"^- (E(?:-C59|-THC|\d+))\b\s*(.*)$")
    for line in s9.splitlines():
        ms = surf_pat.search(line)
        if ms:
            cur_surface = ms.group(1)
            title = ms.group(2)
            members = re.findall(r"\bC\d+\b", title)
            members += re.findall(r"\[P-IPADJ\]|SDP-CAND-8|OBJ-DOM|"
                                  r"DELTA-CARRIER|ADR-D4|Veen|R8\b", title)
            surfaces.append({"surface": cur_surface, "title": title.strip(),
                             "members": members})
            continue
        if line.startswith("**Pairwise") or line.startswith(
                "**Documented-coupling"):
            cur_surface = None
            continue
        me = edge_pat.match(line.strip())
        if me:
            eid, rest = me.group(1), me.group(2)
            header = rest.split(":", 1)[0]
            endpoints = re.findall(r"\bC\d+\b", header)
            for tok in ("PIN-WAVE", "S-5F", "M-RED", "DUTY-10", "P34",
                        "D-44", "SDP-CAND-8", "OBJ-DOM", "DELTA-CARRIER",
                        "vander_veen_1974", "ADR-D4", "NTF-4", "NTF-block",
                        "[P-IPADJ]", "findings", "plan", "S-PRES",
                        "uniformity fork", "forchetta", "Stage-7"):
                if tok in header and tok not in endpoints:
                    endpoints.append(tok)
            kind = "anti-edge" if ("ANTI-edge" in line or "⊥" in line) \
                else "edge"
            if not endpoints and cur_surface:
                for s in surfaces:
                    if s["surface"] == cur_surface:
                        endpoints = list(s["members"])
            edges[eid] = {
                "id": eid,
                "kind": kind,
                "surface": cur_surface,
                "endpoints": endpoints,
                "header": header.strip(),
                "text": rest.strip(),
            }
    return surfaces, edges


def parse_machine_summary(text):
    s10 = text[text.find("\n## 10."):text.find("\n## 11.")]
    block = re.search(r"```(.*?)```", s10, re.S).group(1)

    def num(pat):
        return int(re.search(pat, block).group(1))

    ms = {
        "stages": num(r"stages:\s*(\d+)"),
        "nodes_total": num(r"nodes_total:\s*(\d+)"),
        "ledger_nodes": num(r"ledger_nodes:\s*(\d+)"),
        "nonledger_nodes": num(r"nonledger_nodes:\s*(\d+)"),
        "edges_total": num(r"edges_total:\s*(\d+)\s+entries"),
    }
    ros = re.search(r"nonledger_nodes:.*?\[(.*?)\]", block, re.S).group(1)
    ms["nonledger_roster"] = [t.strip() for t in ros.replace("\n", " ")
                              .split(",") if t.strip()]
    ed = re.search(r"exact roster:(.*?)id-gaps", block, re.S).group(1)
    ms["edge_roster"] = re.findall(r"E(?:-C59|-THC|\d+)", ed)
    tally = {}
    tally_rosters = {}
    for key in ("DECIDED", "MIXED", "NEVER", "SA"):
        m = re.search(key + r":\s*(\d+)\s*\((.*?)\)", block, re.S)
        tally[key] = int(m.group(1))
        tally_rosters[key] = re.findall(r"C\d+\b", m.group(2))
    ms["status_tally"] = tally
    ms["status_rosters"] = tally_rosters
    mnote = re.search(r"note_C46:\s*(\w+)", block)
    ms["note_C46_status"] = mnote.group(1) if mnote else None
    return ms


def main():
    text = MAP_PATH.read_text(encoding="utf-8")
    stages = parse_stages(text)
    nodes = build_nodes(stages)
    surfaces, edges = parse_section9(text)
    ms = parse_machine_summary(text)

    ledger_ids = {k for k, v in nodes.items() if v["type"] == "ledger"}
    nonledger_ids = {k for k, v in nodes.items() if v["type"] == "nonledger"}

    # ---- C46: declared in the machine-summary note, never stage-placed ----
    assert "C46" not in ledger_ids, "C46 unexpectedly present in stage tables"
    assert ms["note_C46_status"] == "DECIDED", \
        "note_C46 missing or moved in machine summary"
    nodes["C46"] = {
        "id": "C46", "type": "ledger", "stage": None, "stage_faces": [],
        "choice": "padding policy, engine-internal (note_C46: not re-listed "
                  "per stage; evidence ADVISORY_S25bis_diff_convergence)",
        "status": "DECIDED", "conditions": "", "open_duty": "",
        "edges_cell": "",
    }
    ledger_ids.add("C46")

    # ---------------- ASSERTS (record counts, SR-12 measured) --------------
    checks = []

    def check(name, cond, detail):
        checks.append((name, bool(cond), detail))
        assert cond, "%s FAILED: %s" % (name, detail)

    check("A1-stages", len(stages) == EXPECTED_STAGES == ms["stages"],
          "measured %d, summary %d, record %d"
          % (len(stages), ms["stages"], EXPECTED_STAGES))
    check("A2-table-ledger", len(ledger_ids) - 1 == EXPECTED_TABLE_LEDGER,
          "unique ledger rows in stage tables = %d (expected 61 = 62 - C46)"
          % (len(ledger_ids) - 1))
    check("A3-ledger-62",
          len(ledger_ids) == EXPECTED_LEDGER == ms["ledger_nodes"],
          "measured %d, summary %d, record %d"
          % (len(ledger_ids), ms["ledger_nodes"], EXPECTED_LEDGER))
    check("A4-ledger-contiguous",
          ledger_ids == {"C%d" % i for i in range(1, 63)},
          "ledger id set is not exactly C1..C62: diff=%s"
          % sorted(ledger_ids ^ {"C%d" % i for i in range(1, 63)}))
    check("A5-nonledger-17",
          len(nonledger_ids) == EXPECTED_NONLEDGER == ms["nonledger_nodes"],
          "measured %d, summary %d, record %d"
          % (len(nonledger_ids), ms["nonledger_nodes"], EXPECTED_NONLEDGER))
    check("A6-nonledger-roster",
          nonledger_ids == set(ms["nonledger_roster"]),
          "roster mismatch: measured-only=%s summary-only=%s"
          % (sorted(nonledger_ids - set(ms["nonledger_roster"])),
             sorted(set(ms["nonledger_roster"]) - nonledger_ids)))
    check("A7-nodes-total",
          len(nodes) == ms["nodes_total"] == EXPECTED_LEDGER
          + EXPECTED_NONLEDGER,
          "measured %d, summary %d" % (len(nodes), ms["nodes_total"]))
    check("A8-edges-45",
          len(edges) == EXPECTED_EDGES == ms["edges_total"],
          "measured %d, summary %d, record %d"
          % (len(edges), ms["edges_total"], EXPECTED_EDGES))
    check("A9-edge-roster", set(edges) == set(ms["edge_roster"]),
          "measured-only=%s summary-only=%s"
          % (sorted(set(edges) - set(ms["edge_roster"])),
             sorted(set(ms["edge_roster"]) - set(edges))))
    check("A10-antiedge",
          edges.get("E34", {}).get("kind") == "anti-edge"
          and sum(1 for e in edges.values() if e["kind"] == "anti-edge") == 1,
          "E34 must be the single declared anti-edge")
    check("A11-unassigned-ids", not (set(edges) & UNASSIGNED_EDGE_IDS),
          "E33/E37/E40 must not exist (unassigned by design)")
    check("A12-surfaces-4", len(surfaces) == 4,
          "cluster surfaces measured %d (spec L0 draws 4 arcs)"
          % len(surfaces))
    dual = {k for k, v in nodes.items() if len(v["stage_faces"]) > 1}
    check("A13-dual-face", dual == DUAL_FACE_EXPECTED,
          "dual-stage-face nodes measured %s, declared %s"
          % (sorted(dual), sorted(DUAL_FACE_EXPECTED)))
    tally = {"DECIDED": 0, "MIXED": 0, "NEVER": 0, "SA": 0}
    by_status = {k: set() for k in tally}
    for k in ledger_ids:
        s = nodes[k]["status"]
        assert s in tally, "ledger %s has non-enum status %r" % (k, s)
        tally[s] += 1
        by_status[s].add(k)
    check("A14-tally",
          tally == EXPECTED_TALLY == ms["status_tally"],
          "measured %s, summary %s" % (tally, ms["status_tally"]))
    for key in tally:
        check("A15-roster-" + key,
              by_status[key] == set(ms["status_rosters"][key]),
              "%s per-id mismatch: measured-only=%s summary-only=%s"
              % (key, sorted(by_status[key]
                             - set(ms["status_rosters"][key])),
                 sorted(set(ms["status_rosters"][key]) - by_status[key])))

    # ---------------- per-stage tallies (for L0 render + report) -----------
    stage_summary = []
    for st in stages:
        led = [k for k, v in nodes.items()
               if v["type"] == "ledger" and v["stage"] == st["num"]]
        nl = [k for k, v in nodes.items()
              if v["type"] == "nonledger" and v["stage"] == st["num"]]
        faces = [k for k, v in nodes.items()
                 if st["num"] in v["stage_faces"] and v["stage"] != st["num"]]
        sb = {"DECIDED": 0, "MIXED": 0, "NEVER": 0, "SA": 0}
        for k in led:
            sb[nodes[k]["status"]] += 1
        stage_summary.append({
            "num": st["num"], "name": st["name"], "subtitle": st["subtitle"],
            "ledger_ids": sorted(led, key=lambda x: int(x[1:])),
            "nonledger_ids": nl, "secondary_faces": faces,
            "status_tally": sb,
        })

    out = {
        "source": str(MAP_PATH.relative_to(REPO)).replace("\\", "/"),
        "map_version_line": re.search(r"map_version: (.+)", text).group(1),
        "record_counts": {
            "stages": EXPECTED_STAGES, "ledger_nodes": EXPECTED_LEDGER,
            "nonledger_nodes": EXPECTED_NONLEDGER,
            "edge_entries": EXPECTED_EDGES,
        },
        "machine_summary": ms,
        "stages": stage_summary,
        "nodes": list(nodes.values()),
        "edges": list(edges.values()),
        "surfaces": surfaces,
        "asserts": [{"name": n, "pass": p, "detail": d} for n, p, d in checks],
    }
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False),
                        encoding="utf-8")

    print("MAP: %s" % MAP_PATH)
    print("MEASURED: stages=%d ledger=%d (table rows %d + C46 note) "
          "nonledger=%d edges=%d (incl. anti-edge E34) surfaces=%d"
          % (len(stages), len(ledger_ids), len(ledger_ids) - 1,
             len(nonledger_ids), len(edges), len(surfaces)))
    print("STATUS TALLY: " + " ".join("%s=%d" % kv for kv in tally.items()))
    print("PER-STAGE (ledger + nonledger):")
    for s in stage_summary:
        extra = (" [+faces: %s]" % ",".join(s["secondary_faces"])
                 if s["secondary_faces"] else "")
        print("  Stage %d %-22s %2d + %d%s"
              % (s["num"], s["name"], len(s["ledger_ids"]),
                 len(s["nonledger_ids"]), extra))
    print("ASSERTS: %d/%d PASS" % (sum(1 for _, p, _ in checks if p),
                                   len(checks)))
    print("WROTE: %s" % OUT_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
