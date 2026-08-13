# S-ORDINE S8: mechanical PROGRESS slim (verbatim range moves).
# Live keeps: L1-119 (header + ORA S25bis + FINESTRA INTER-SESSIONE +
# chain) + consolidated census table (new) + BLOCCATO L2174-2206 (+
# appended rows) + LOG pointer. Archive gets, verbatim under dated
# provenance banners: L120-2173 (stati precedenti + delta census +
# stale NEXT) and L2207-2522 (LOG SESSIONI).
import io, sys

SRC = "docs/rde_nozzle_PROGRESS.md"
ARC = "docs/rde_nozzle_PROGRESS_ARCHIVE.md"
CEN = "validation/sordine_raws_2026-08-13/s8_census_block.txt"

lines = io.open(SRC, encoding="utf-8").read().splitlines(keepends=False)
n = len(lines)
assert n >= 2500, n

def block(a, b):  # 1-indexed inclusive
    return lines[a-1:b]

head = block(1, 119)
hist1 = block(120, 2173)
blocc = block(2174, 2206)
log_sec = block(2207, n)
census = io.open(CEN, encoding="utf-8").read().splitlines()

new_blocc_rows = [
    " 9. ADR_panel_2026-07-16: DUE call utente aperte (UD-4 S-ORDINE",
    "    2026-08-13, 'ancora pendente'): (a) headline spike 600N:",
    "    re-bless 242.5 s constrained vs tenere 245.3 s + companion;",
    "    (b) default troncamento 0.20 vs 0.25-0.30. Indice: UNRESOLVED.",
    " 10. Ratifiche corpus letteratura (handoff 2026-08-13): D-01",
    "    (cancellazione glossa literature_map.md:432 +",
    "    theorem_ledger.md:410), C31-minimale (T7(c) -> D in N_K),",
    "    C30 (attribuzione Shmyglevskii 1962, gated su R28-lit);",
    "    owner = finestra F-SERVICE ratifiche post-S-ORDINE/pre-S-CERT.",
    " 11. Schedulazione R22-lit (esperimento disentanglement",
    "    3D/3D-mediato/2D) — candidato primo blocco F2 (handoff).",
    " 12. P0 procurement: ISABE-2003-117, Bogdanov 2002, tesi Harroun",
    "    Purdue 2019, Shmyglevskii PMM 26(1) 1962 (righe WANTED nel",
    "    literature registry).",
]

live = []
live += head
live += [""]
live += census
live += [""]
live += blocc
live += new_blocc_rows
live += [""]
live += ["## LOG SESSIONI"]
live += ["I log per-sessione vivono in validation/PROGRESS_*.md (indice:",
         "validation/ADVISORY_INDEX.md). La storia integrale di questo file",
         "(stati precedenti, delta censimento, NEXT storici, log S1-S25bis)",
         "e' in docs/rde_nozzle_PROGRESS_ARCHIVE.md (append-only, SR-10)."]

arch = []
arch += ["# PROGRESS ARCHIVE — rde nozzle program (append-only, SR-10:",
         "# content enters only with a provenance banner; nothing inside is",
         "# ever edited beyond its banner. Created 2026-08-13, S-ORDINE S8.)",
         ""]
arch += ["== moved from docs/rde_nozzle_PROGRESS.md L120-L2173, 2026-08-13, S-ORDINE S8 =="]
arch += hist1
arch += [""]
arch += ["== moved from docs/rde_nozzle_PROGRESS.md L2207-L%d, 2026-08-13, S-ORDINE S8 ==" % n]
arch += log_sec

io.open(ARC, "w", encoding="utf-8", newline="\n").write("\n".join(arch) + "\n")
io.open(SRC, "w", encoding="utf-8", newline="\n").write("\n".join(live) + "\n")

# LINE-MULTISET CHECK vs the pre-edit content we still hold in `lines`:
# every old non-blank line must appear verbatim in live UNION archive.
from collections import Counter
old_c = Counter(l for l in lines if l.strip())
new_c = Counter(l for l in live if l.strip()) + Counter(l for l in arch if l.strip())
missing = {l: c - new_c.get(l, 0) for l, c in old_c.items() if new_c.get(l, 0) < c}
print("old_nonblank=%d live=%d archive=%d missing_distinct=%d" %
      (sum(old_c.values()), len(live), len(arch), len(missing)))
for l in list(missing)[:20]:
    print("MISSING:", repr(l[:100]))
sys.exit(0 if not missing else 1)
