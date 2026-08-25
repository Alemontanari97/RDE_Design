# -*- coding: utf-8 -*-
"""S-PRES deck — Part D: BACKUP skeleton (16 slides).

Storyboard rule: the backup is BUILT FROM the Q&A map of Block 2 — here
only structure + pointers, no re-copying. Guard 18 holds on backup too:
cards carry engineering language up front and the accounting (classes,
counts, registry ids) in the note-body — the backup is where a panel
that ASKS for the accounting receives it, on demand.

Skeleton = D1-D8 (L1 graphs of the 8 stages) + D9..D14 (six L2 node
cards incl. the declared to-backup joins) + D-F (full honesty table) +
D-N (figure-reuse methodology). 8+6+1+1 = 16.
Block 2's Q&A red-team may re-target D9+ cards; that pass edits, never
silently drops (cut-list discipline).
"""

_L2_CARD_IDS = [
    # (slide id, card title, content source pointer, joined feed)
    ("D9",  "Boundary-condition licence follows the flow",
     "single-wave → full certificate; RPO → declared practice; multistable → robust layer; chaotic → HONEST REFUSAL",
     "CH1-feed-6"),
    ("D10", "Why the lip multiplier vanishes (f2 = −λ2)",
     "the elegant identity at the lip — technical Q&A card",
     "CH2-feed-4"),
    ("D11", "The corrector as a perturbation of the steady sweep",
     "algorithmic detail — Q&A card",
     "CH3-feed-8"),
    ("D12", "Theory-as-code: the registry lint layer",
     "internal governance — process Q&A card",
     "CH9-feed-9"),
    ("D13", "Data uncertainty enters the contract (C50)",
     "instantiation = duty of the opening phase — data Q&A card",
     "CH10-feed-8"),
    ("D14", "The optimizer choice, full record (C31 card + choice tally)",
     "6-field decision card (incumbent / alternatives with survey data / verdict / recency check / falsifier / re-exam window) + the choice-ledger tally (62 = 12 decided / 36 mixed / 12 never / 2 single-author) — the accounting moved OFF-main lives HERE",
     "CH4-feed-9 + CH4-feed-1"),
]

SLIDES_D = (
    [
        dict(
            id=f"D{i}", kind="new", layout="backup_graph", minutes=0, cut="backup",
            title=f"Backup — design pipeline, stage {i} in depth",
            content=dict(
                fig=(f"graph/L1_stage{i}.png", None),
                note_line=("walkable graph: every node card carries its choice, alternatives and falsifier; "
                           "long-range links labelled with their target stage"),
            ),
            notes=(
                f"Backup L1 graph, stage {i}. Populated from pipeline_graph.json "
                "(assert-gated extraction, never hand-typed). Stage 6 carries the "
                "3-panel split of record (DERISK §3.1); long-range edges "
                "E9/E28/E29 stub-labelled (DERISK §5). Serve on drill-down "
                "questions about the machine; L2 card slides follow."
            ),
        )
        for i in range(1, 9)
    ]
    + [
        dict(
            id=sid, kind="new", layout="backup_card", minutes=0, cut="backup",
            title=f"Backup — {title}",
            content=dict(card_title=title, card_body=body),
            notes=(
                f"L2 node card ({join}). Declared to-backup consumption of the "
                "storyboard join table [F-des-4]: this card is the landing site "
                "of a feed consumed at backup-with-reason. Compression is "
                "cite-only from the atlas/pipeline_graph fields (≤40 words per "
                "field). Q&A mapping to be refined by the Block-2 red-team "
                "pass (edits, never silent drops)."
            ),
        )
        for (sid, title, body, join) in _L2_CARD_IDS
    ]
    + [
        dict(
            id="D-F", kind="new", layout="backup_table", minutes=0, cut="backup",
            title="Backup — the honesty table, complete",
            content=dict(
                note_line=("all six error sources, best/worst, how estimated, and what tightens each — "
                           "the main deck showed the highlights (C11)"),
                table_header=["source", "best", "worst", "how estimated", "what tightens it"],
                table=[
                    ("Mean azimuthal residual", "exactly 0", "exactly 0", "proven (hypotheses stated)", "—"),
                    ("Swirl thrust unmodelled", "1.5% of thrust", "3% of thrust", "order estimate", "residual-measurement campaign"),
                    ("Input-data bias", "0.6% of pressure", "9% of pressure", "order estimate + literature", "data contract + campaign"),
                    ("Jumps at the wave fronts", "no number yet", "—", "open — derivation planned", "derivation chain, then campaign"),
                    ("Designing the nozzle alone", "~1%", "~1%", "literature, page-verified", "coupled-pair run"),
                    ("Optimum shift", "no number yet", "—", "open", "head-to-head comparison"),
                ],
            ),
            notes=(
                "Full FORCHETTA (6 rows, verbatim cells with classes) -> "
                "CH3-feed-4 / CH7-feed-4 (CH7 PART 5 of record, :1458-1743 "
                "anchors). Cells carry bound-or-estimate declared + class + "
                "provenance + 'what tightens it'. Serve when C11 highlights "
                "are challenged; also home of C2/C12 integral versions if cut "
                "from main."
            ),
        ),
        dict(
            id="D-N", kind="new", layout="backup_card", minutes=0, cut="backup",
            title="Backup — figure provenance & reuse methodology",
            content=dict(
                card_title="Every third-party figure: full citation + non-reproduction caveat",
                card_body=("manifest of reused figures with per-figure attribution and audit trail; "
                           "our own figures traced to committed, tested scripts"),
            ),
            notes=(
                "Reuse manifest -> deck_build/FIGS_MANIFEST.md (crops, full "
                "citations, CT-6 standing rule) + host-pipeline provenance "
                "discipline (validate_reused_figs pattern). Serve on any "
                "figure-rights / provenance question (audit criterion (e))."
            ),
        ),
    ]
)

SLIDES_D.append(dict(
    id="D-L", kind="new", layout="backup_graph", minutes=0, cut="backup",
    title="Backup — what input the method needs: the reliability ladder",
    content=dict(
        fig=("figs/fig_c18_ladder.png", None),
        note_line="cases A–G: from engine specs alone to class-verified hot-fire data — the entry gate can reject",
    ),
    notes=("Annex-B ladder moved from C18 (F-4: three asks = three cards; "
           "ladder legibility). Source: CH10-feed-1 specs ladder; entry "
           "gate G6 loud-reject (never exercised - said in C18 notes)."),
))
