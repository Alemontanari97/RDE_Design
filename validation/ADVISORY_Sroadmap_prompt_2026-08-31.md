# ADVISORY — PROMPT DI SESSIONE "S-ROADMAP" (carrier di record, 2026-08-31)

Stadio di confronto: chiusura S-PRES S4 (commit c4dc1d0; trace/CONSECUTIO_S4
L1-L4; misure SR-12 del 2026-08-31: M0 4285 righe, atlas 13/10704, PROGRESS
445+2647 archivio, findings 253 [211 OPEN], BLOCCATO 17, validation 1017 file,
36 log, 60 memorie, 286 commit). Arco di consumo: questa advisory -> sessione
S-ROADMAP (esegue U1-U7) -> F2-B0 -> ... -> TWIN -> P-1. Struttura CONVERGIUTA
inline (auto-refutazione, quota: zero agenti) — deviazioni dichiarate qui.

================================================================================
## A. DIAGNOSI DI RECORD (perché questa sessione)
Storage/rigore/persistenza-di-stato = SOTA (registri as-code con rejector,
sorgente unica con classi di rigore, R1-R7, log per sessione). NON SOTA:
(1) retrieval — 27k righe di record navigate a lettura umana; 2 miss provati
in S4 (persona di record inutilizzata; lineage CH10 non consumata);
(2) coda aperta non triata (211/253 finding, 17 BLOCCATO);
(3) piano a livello-fase (D6) senza cammino critico a livello-risultato;
(4) nessun budget d'orchestrazione per fase (S4: ~2.4M tok subagenti fino al
limite di spesa); (5) salute GENO non chiusa (S-GENOAUDIT incompleta, patch
non inerte nel working tree GENO) = rischio sul cammino critico;
(6) nessun consumatore dichiarato per il record (asse comunicazione).

================================================================================
## B. IL NUMERO DECISIVO (asse unico del programma)
Head-to-head TWIN: design per-fase vs design classico su (<Pc>,T0,gamma) [I4]
a vincoli IDENTICI, swirl bracketato, kill-or-validate (atlas CH6 :440/:490/
:712, comparatore ZERO istanze computate). Stop criterion ~1% Isp pre-fissato.
Cammino critico: F2-B0 -> M-RED -> TWIN -> CFD-2 -> (CFD-1 decisione) -> P-1.
Ogni voce aperta del record è BLOCKING / NON-BLOCKING / PAPER-ONLY rispetto a
questo numero — o non è classificata, e questo è il difetto da chiudere.

================================================================================
## C. ORDINI DI SESSIONE (S-ROADMAP, 1 sessione; Fable; ZERO subagenti;
##    tetto orchestrazione dichiarato in apertura = inline only)
R2 obbligatoria: memoria (spres-session4-close, s-genoaudit-parallel-incomplete,
topology-census-pins, s25bis-speed-complete, fservice-scert-double-session) +
M0 mirato (Parte VII mappa) + PROGRESS + CONSECUTIO_S4 + questa advisory.

U1  docs/ROADMAP_critical_path.md (≤ 2 pagine, di record): B + i passi con
    INGRESSO / USCITA / FALSIFICATORE / OWNER; i doveri TEORICI come passi
    (delta/L_H underived -> M-RED; completamento T-DISC L3; finding
    atlas:ch5-...-mislabel; residui T-DCRX/NTF dichiarati a C4); GENO health
    come passo di F2-B0. + CAMPO `path:` nei registri (findings; BLOCCATO in
    PROGRESS) con valori critical|non-critical|paper + LINT
    (tests/test_findings_registry.py esteso: ogni riga OPEN ha `path:`;
    rejector seminato: riga OPEN senza tag = violazione).
U2  docs/START_HERE.md (≤ 60 righe): dove vive cosa (M0/D1-D7/atlas/5
    registri/PROGRESS+archivio/ADVISORY_INDEX/glossario/log/memoria) + le 6
    direttive standing (navigation-first, claim-dual-proof, doubts-to-
    convergence, never-postpone-resolvables, model-pinned, R8) + il comando
    di query. tools/record_query.py: grep strutturato su MANIFEST fisso di
    file di record, output = riga + ancora + classe se presente; test che il
    manifest risolva (lint). R2 di CLAUDE.md aggiornata: START_HERE si legge
    PER PRIMO.
U3  TRIAGE = SOLI TAG (nessun cambio di status senza evidenza, R5): sweep
    misurato dei 211 OPEN + 17 BLOCCATO -> path: tag; conteggi PRIMA/DOPO
    da comando nel log; le chiusure con evidenza, se cheap e in-window,
    una per una (never-postpone-resolvables); obiettivo dichiarato a fine
    sessione: quante BLOCKING (attese ≤ ~40).
U4  CLAUDE.md regola R8 (SESSIONE GATE-FIRST): ogni sessione dichiara in
    apertura (i) consumatore/persona del deliverable, (ii) criteri d'uscita
    (artefatti comunicativi: 4 assi CKP-S4-1), (iii) TETTO di budget
    d'orchestrazione (subagenti/token) riportato a R3 [SR-9 + cap];
    difetti di forma -> enforcement+assert alla prima occorrenza; listener
    = persona esatta, delta-audit mai full ripetuti.
U5  PROGRESS snello: ORA = tabella 10 righe (fase, HEAD, ultimo gate, passo
    atomico, BLOCKING attive, budget) + puntatore al log; NEXT atomico;
    BLOCCATO tabella con path:; LOG = 1 riga/sessione con puntatore; i
    blocchi ORA storici migrano in PROGRESS_ARCHIVE (append-only, SR-7/10).
U6  GENO HEALTH (report + azione minima): stato del working tree GENO (patch
    VARIANT B non inerte? baseline md5?), lista dei dubbi aperti di
    S-GENOAUDIT; se la quarantena della patch è cheap e sicura -> eseguire e
    ri-baselinare md5; altrimenti passo BLOCKING nominato in ROADMAP con
    trigger. Mai commit da GENO in questo repo.
U7  docs/paper/P1_outline.md (scheletro, no prosa): sezioni -> capitoli atlas
    -> registri -> carrier; convenzioni: scala L1/L2/L3 (HARVEST H-1), regola
    numeri (H-4: grandezza + scope + caveat), novità query-bounded (guard 9),
    gate G5 Kraiko-1979 prima della submission; consumatore = persona
    referee JPP (dichiarata).
R3  chiusura: lint verdi (findings esteso, manifest query, registri
    xix/xx/xxii/xxiii), ADVISORY_INDEX righe, conteggi misurati, commit
    pathspec, memoria, HANDOFF a F2-B0.
Vincoli: env pinnato (niente install); GENO/ read-only; Fable ovunque; git add
solo pathspec; stray dirs non nostri restano untracked.

================================================================================
## D. SCHEMA DELLE PROSSIME SESSIONI (obiettivo + criterio d'uscita)
| # | Sessione | Obiettivo | Uscita (misurabile) |
|---|---|---|---|
| 1 | S-ROADMAP | U1-U7 | lint verdi; BLOCKING contate; START_HERE + query operativi; ROADMAP di record; R8 in CLAUDE.md |
| 2 | F2-B0 (1-2 sess.) | re-chain + finestra engine (C31/C57/C58/C60/[P-IPADJ] a convergenza), P0 staleness import-closure, GENO health chiusa, O3.4 gamba gradiente, BLOCCATO-16 ratifica, sessione topologia+modellistica (pin di record) | G1 intatto, suite verde, protocollo TWIN pre-registrato (config, vincoli, decision rule, stop) |
| 3 | F2-M-RED (1-2) | campagna residuo: bande B-1..B-4, operatore scartato misurato, derivazione delta/L_H (five-field -> route-B), fix finding CH5 nella finestra atlas | numeri di record o strada nominata; sorgenti C11 aggiornate |
| 4 | F2-TWIN (1-2) | head-to-head su regime plug troncato FUORI dalla classe cert-limited ([C-O33]); vincoli identici; both-outcomes | IL numero + disposizione (materiale -> il metodo paga; piccolo -> la letteratura ha ragione a quel rango); stop-rule applicata |
| 5 | F2-CFD2 (1) | run accoppiata appaiata: prezzo della sostituzione (template della letteratura) | banda ~1% regge o riga budget aggiornata; priorità CFD-1 decisa |
| 6 | P-1 (2-3, in parallelo da 3) | stesura dall'atlas con L1/L2/L3; consumption-trace sul draft (metodo TRACE); refuter persona-referee | draft con ogni claim tracciato; G5 gate umano prima della submission |
| 7 | CFD-1 decisione | canale (partner/procurement) deciso dopo il residuo; commit solo se banda superata | decisione registrata, nessun run promesso |
Regola trasversale: ogni sessione apre gate-first (R8) e chiude R3+R7 con
conteggi misurati; il cammino critico si rilegge a ogni apertura.
