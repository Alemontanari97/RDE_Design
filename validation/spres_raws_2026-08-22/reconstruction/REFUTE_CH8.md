# REFUTE_CH8 — refuto avversariale di CH8_design_space.md

Refuter run 2026-08-23 (S-PRES ricostruzione). Mandato: anchor walk 100%,
attacco al banco utente (4 domande), buchi di completezza, overclaim scan.

## Anchor walk (esito)

Ancore aperte e verificate a testo E classe: ~40/40. Verificate ESATTE:
`docs/rde_nozzle_problem_book.md:337-368` (formulazione, settori (i)-(iv),
SCHEMA a :354, CAUTION :361-363, working class :365-368; quote "outputs of
the optimization, not inputs" verbatim a :343-344);
`docs/rde_nozzle_MASTER.md:306-327` (state-pointer pins, "FINITE ... NO
declared rigor class" verbatim :313-320, headline advisory :321-327);
`validation/PANEL_topology_census_2026-07-22.md:1-17` (advisory, 233/233),
`:40-53` (Migdal/Delta-nu_lip), `:55-74` (collasso S0, falsificatore :73-74),
`:329-384` (7pin completo, generality guarantee :371-377, CEN-O8 :382-384);
`docs/claims_registry.yaml:368-379` [T-OP11e] (scope :371 "rank CLOSURES ...
never hardware" esatto), `:329-340` [T-T4] (falsifier :339), `:589-600`
[T-P7S1] (R-P7.2 in scope :592), `:181` (C-N2 al kickoff PB-2/OP-2),
`:949-961` X-GRP10 (22+8), `:977-989` X-GRP12 (20/20, 6 negativi);
`docs/rde_nozzle_pipeline_decision_map.md:136` (C31), `:154-159` (C1-C8),
`:161-163` (placement note), `:183` (H20), `:184` (C61 NEVER/WG10-FAILED/
Humphreys 1971/N2), `:218` (E12); `docs/findings_registry.yaml:1607` e
`:2519` (vedi finding 9); `validation/a1_toc_variational_jax.py:1-50`
(docstring W, spline, monitors), `:33` ("dJ/dtheta_B exact at fixed
topology" verbatim), `:65` (N1), `:108` (M_NODES=8), `:1360`/`:1748` (riga
lip LinearConstraint); `docs/rde_nozzle_PROGRESS_ARCHIVE.md:413` (R5c
census-lemma SCHED F2-exit). La nota di identificazione T-GRP10→[T-OP11e]
e' corretta e meritoria. Due soli difetti d'ancora: findings 7 e 9.

## Tabella findings

| # | sito | classe | severita' | testo | fix |
|---|---|---|---|---|---|
| 1 | §4(2) + §5 item 2 (catena T-T4→C-HT4→C61/H20 non collegata) | REPAIR | ALTA | "Il plug pieno peak-phase vince" e' relativo alla chiusura C-HT4 (sonic-capped ideal-adaptation, SCHEMA, `docs/claims_registry.yaml:172-181`), il cui falsificatore DICHIARATO e' esattamente la banda PB-2 troncamento/base-pressure ("closure's premium unreachable by any real plug", :181) — eseguibile SOLO sotto una chiusura p_b che e' NEVER (C61) e con la meccanica H20 mancante. CH8 possiede tutti i pezzi (tabella §2, aperti 1-2-4) ma NON dichiara il loop: il falsificatore del verdetto within-family e' oggi non-eseguibile per le stesse due mancanze elencate in Q&A(3). Un panel ostile lo chiede in un colpo solo. | In Q&A(2) e deck item 2 aggiungere una riga: "il verdetto within-family eredita C-HT4; il suo falsificatore (banda PB-2) diventa eseguibile solo chiudendo C61+H20 — il programma lo sa e lo ha gia' schedulato (C-N2 al kickoff PB-2/OP-2, `:181`)". |
| 2 | §1.3 ("cammino continuo dentro S0") + §4(1) ("percorribile con continuita'") | REPAIR | ALTA | Sopra-classe rispetto all'advisory stesso: il census dice S0 "conjecturally connected (hub argument owed, CEN-O4)" (`PANEL_topology_census_2026-07-22.md:68-69`) e CEN-O4 e' nel residuo analitico dichiarato (:378-379). Solo singoli confini di strato (r_b→0, e→0) hanno continuita' argomentata; la connessione bell→spike per cammino in-class e' CONGETTURA. Q&A(1) la presenta come acquisita ("percorribile con continuita'"). | In §1.3 e §4(1): "strati di un solo settore clopen S0, connessione congetturale (hub argument dovuto, CEN-O4)"; la parola "percorribile" va condizionata esplicitamente. |
| 3 | §5 item 2 ("Il torneo e' finito e ha gia' un primo verdetto") | REPAIR | MEDIA | Overclaim interno al capitolo: la finitezza dei settori e' SCHEMA con classe di rigore NON assegnata (M0:313-320) — lo dice lo stesso item 3 due righe sotto. L'item 2 la asserisce piatta. | Item 2: "Il torneo per-settore (finitezza = SCHEMA, cfr. item 3) ha gia' un primo verdetto...". |
| 4 | §1.4 titolo + §4(2) (copertura del torneo non enumerata) | GAP | MEDIA | "Il torneo gia' giocato" enumera solo le partite giocate, mai quelle NON giocate: al rung delle chiusure hanno un entrant solo {bell, plug} ([T-OP11e]) + il match interno alla famiglia plug ([T-T4]). Shrouded plug (settore iii), expansion-deflection, famiglia detached D(m,n) e bare annulus NON hanno alcuna voce a NESSUN rung. L'esperto ostile lo estrae come reticenza. | In §4(2) frase esplicita: "partite giocate: bell-vs-plug e plug-interno; shrouded plug, E-D e detached non hanno oggi alcun entrant nemmeno al rung delle chiusure". |
| 5 | §4(3) (risposta a 3 pezzi, manca il quarto) | GAP | MEDIA | La risposta elenca (a) p_b, (b) H20, (c) CEN-O8 ma OMETTE il pezzo che CH8 stesso lista come aperto 5: anche con chiusura+solve, l'engine discreto non ha una chart per il settore plug (driver = solo bell/TOC, GAP-21/F2 engine window, `docs/rde_nozzle_pipeline_decision_map.md:154-159`). "Ottimizzare un plug troncato VERO" richiede il quarto pezzo. | Aggiungere (d): "la chart di settore nell'engine (estensione driver oltre bell, aperto 5, owner F2)". |
| 6 | §1.3 ("Correzione Migdal di record") | DOWNGRADE | MEDIA | Il census e' ADVISORY con clausola esplicita "Nothing here is of record until ratified" (`PANEL_topology_census_2026-07-22.md:13-14`); il tag della correzione e' [DECLARED] dentro l'advisory (:40). "Di record" e' sopra-classe. | "Correzione Migdal dichiarata nell'advisory (Round 2)". |
| 7 | §1.3 ("P(h)/BR sono provati vuoti", ancora :55-74) | REPAIR | MEDIA | Doppio difetto: (a) ancora sbagliata — la cancellazione P(h)/BR vive a census `:170` ("DELETED: P(h) (hole vector identically 0 — L1) and BR(h>=1) (A1)"), non nella headline :55-74; (b) "provati" e' sopra-classe: L1 e' CONDITIONAL su CEN-O10 (:102) — CEN-O10 e' PINNATO NONBLOCK+ ma la derivazione pin→lemma e' un target S15 dichiarato (:363-364), e tutto resta advisory. | "vuoti per L1+A1 nell'advisory (L1 condizionale su CEN-O10 pinnato; pin→lemma dovuto a S15)", ancora census `:170` + `:102`. |
| 8 | §1.3 (presentazione del panel census) | GAP | BASSA | CH8 cita "233/233 verdetti mappati" ma tace il caveat del header: "the formal-convergence criterion (unanimous clean 3-critic panel) was NOT met before infrastructure truncation" (`:11-13`). Per un capitolo che alimenta un deck honesty-first, il caveat deve viaggiare con la citazione. | Aggiungere il caveat di non-convergenza formale accanto a 233/233. |
| 9 | §1.6 e §3.1 ("registry :2521") | NOTE | BASSA | La riga findings `plume:free-boundary-solve-mechanics-missing` sta a `docs/findings_registry.yaml:2519` (misurato con grep in-window); ":2521" e' l'"ordinal" citato dalla mappa (:183) e CH8 lo riporta senza la parola "ordinal", facendolo sembrare un'ancora di riga; l'edge E12 (:218) cita :2519. | Citare `:2519` (riga) o riportare ":2521 ordinal" tra virgolette come testo della mappa. |
| 10 | §4(2) ("carrier X-GRP10/X-GRP12 con 8+6 controlli negativi") | NOTE | BASSA | X-GRP10 e' gamma: "gamma-const-oracle" (`docs/claims_registry.yaml:961`); la classe EOS-general di [T-OP11e] cavalca X-GRP12 (route reale, "structure confirmed at gamma(T)", scope :371). Se in Q&A si citano i due carrier in coppia, il ruolo va distinto per non esporre il fianco ("il vostro teorema EOS-general ha un carrier gamma-const"). | Una parentesi: "(X-GRP10 = oracolo gamma-const; l'EOS-general e' portato da X-GRP12)". |

## Attacco al banco utente — esito

(1) Risposta a due livelli, onesta e ancorata; unico difetto = finding 2
(continuita' di S0 sopra-classe). (2) Non evasiva sul rung; difetti =
finding 1 (loop C-HT4 non dichiarato) e 4 (partite non giocate non
enumerate). (3) Ancorata, ma incompleta di un pezzo = finding 5.
(4) La migliore delle quattro: distinzione dominio-ammissibile /
evidenza-eseguibile detta esattamente come il record la consente. Nessuna
risposta e' circolare; nessun OPEN e' stato riempito.

## Overclaim scan

Nessun superlativo non ancorato; nessun claim di novita' (nulla da
query-bounding in questo capitolo); CT-6 non toccato (nessun numero di
paper citato). Gli overclaim trovati sono i findings 2, 3, 6, 7 (tutti
di classe, non di sostanza).

## VERDETTO

**REGGE-CON-RIPARAZIONI** — 0 BREAK / 4 REPAIR / 3 GAP / 1 DOWNGRADE /
2 NOTE (10 findings totali). L'impianto del capitolo e' solido: la
struttura a due livelli (formulazione configuration-free vs engine
mono-settore) e' esattamente quella del record, le classi di rigore sono
quasi ovunque dichiarate, gli OPEN non sono riempiti. Le riparazioni sono
tutte locali (frasi e ancore), nessuna tocca la struttura.
