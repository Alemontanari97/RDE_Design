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

================================================================================
## E. ADDENDUM 2026-08-31 (domanda utente: "il full ottimizzatore che spanna
##    ogni geometria per dati vincoli, per quando?") — CORREZIONE AL CAMMINO
Di record (CH8 :541-548, :981-984; D6 :214-227 F3; :233-240 F4b):
- La generalita' configuration-free (un corpo solido nell'inviluppo, classi
  che EMERGONO, ottimo globale = torneo tra ottimi di settore, spline
  certificate per settore) e' della FORMULAZIONE, non ancora dell'ENGINE.
- Oggi il driver esercita UN settore: bell/TOC, 9 dof (theta_B + 8 heights,
  spline C^2, lip equality, TR-Newton segmentato) [PRACTICE, X-TOCV].
- I settori free-boundary (plug/aerospike/E-D/shrouded) hanno DUE mancanti
  nominati: H20 (solve del plume boundary p = Pa + shape-adjoint) e C61/N2
  (chiusura p_b, mai adottata; Veen legacy FAILED) — owner e finestre F4b /
  PB-2 / OP-2.
- FASE DI PIANO: **F3 GEOMETRY CLASSES (3-4 sessioni; plug/aerospike
  primary)**, ENTRY = F2 exit + RaoPlug S1/S2 fix in GENO (o status
  single-oracle dichiarato) + margine Lambda-form plug/C- PROVATO o PRACTICE
  dichiarata; EXIT = ottimo plug certificato + oracolo spike Table-1 in bande
  derivate + >= 1 istanza var-gamma/stratificata + falsificatore di forma del
  plug troncato 2-D eseguito PRIMA del primo ottimo plug certificato; budget
  ISS-4 (cap 3 h/sessione, max 2 campagne decisive, contatore m/4, fallback
  BY RULE). F3 e F4b (fronti fitted, 2-3 sessioni) sono ORDER-INTERCHANGEABLE
  dato F2 exit. Il "full envelope" (tutte le classi + torneo) = F3 EXIT (+F4b
  per i fronti data-borne); il de-risk del plug-march a livello spike e'
  AUTORIZZATO in parallelo a F2 (RK1 front-load).
CONSEGUENZA SUL CAMMINO CRITICO (correzione dichiarata alle sezioni B e D):
il TWIN DECISIVO vive dove il teorema di rottura vale — il PLUG TRONCATO —
quindi richiede il settore plug nell'engine (F3), non solo F2. Il twin su
bell/TOC ESISTE gia' (F1b, S24: +0.51% +-30%, cert-limited) ed e' il twin
del settore corrente, NON quello decisivo. Cammino critico CORRETTO:
F2-B0 -> M-RED (residuo, delta/L_H) -> [RK1 plug-march de-risk in parallelo]
-> F3 settore plug (H20 + chiusura p_b C61/N2 + oracolo spike) -> TWIN
decisivo su plug troncato -> CFD-2 -> (CFD-1) -> P-1. Schema D aggiornato:
inserire "F3 plug sector (3-4 sess., budget ISS-4)" tra la riga 3 e la riga
4; la riga 4 eredita ENTRY = F3 exit (o istanza plug certificata). U1 deve
scrivere il cammino in QUESTA forma. Per il torneo su TUTTE le classi
(inviluppo pieno): F3 exit + F4b — nessuna data di calendario di record
(solo ordine + budget per sessione); stima di ordine: F2 (2-4 sess.) +
F3 (3-4) + F4b (2-3) = ~7-11 sessioni da qui.

================================================================================
## F. ADDENDUM 2026-08-31 — REGOLA DI CERTEZZA (domanda utente: "non avevi
##    visto il piano nella sua interezza? come fai a esserne certo ora?")
AMMISSIONE DI RECORD: lo schema D e la sezione B sono stati AUTORATI da
contesto parziale (NEXT di PROGRESS + fette di CH6/CH10 + memorie + grep
mirati su D6), NON da una lettura integrale di D6 (1157 righe, fasi F0-F6 +
7 gate), della pipeline decision map ne' di CH8. Prova del buco: lo schema
ignorava F3, F4b, F5 (RDE MACHINE) e F6 (hardware bridge). La certezza NON
si ottiene per lettura (nemmeno integrale: la lettura non e' verificabile);
si ottiene per DERIVAZIONE + LINT. Percio' U1 e' RISCRITTA cosi':
U1' ROADMAP DERIVATA, NON AUTORATA. Sorgenti-macchina (tutte esistenti,
    misurate 2026-08-31): D6 tabella fasi F0..F6 (:37,:55,:101,:160,:214,
    :233,:252,:275) + 7 gate G0-G6; docs/rde_nozzle_pipeline_decision_map.md
    (di record, refuter 0 BREAK); validation/spres_raws_2026-08-22/
    graph_derisk/pipeline_graph.json (79 nodi / 45 archi, assert-gated);
    docs/choice_ledger.yaml (62 righe); docs/findings_registry.yaml (253,
    211 OPEN); PROGRESS BLOCCATO (17). tools/roadmap_derive.py legge queste
    sorgenti e produce docs/ROADMAP_critical_path.md come TABELLA di passi
    con, per ogni passo: fase D6, gate, nodi di pipeline consumati, righe
    ledger, finding/BLOCCATO taggate. tests/test_roadmap_coverage.py =
    BIIEZIONE: ogni fase, gate, nodo, riga ledger, finding OPEN e voce
    BLOCCATO compare in >= 1 passo OPPURE porta il tag esplicito OUT:<why>
    (paper-only / non-critical / horizon-F6); rejector seminato (un nodo
    orfano piantato deve far FALLIRE il lint). Il cammino critico al TWIN
    decisivo (sez. E) e' una VISTA filtrata (path: critical) di quella
    tabella, mai un documento separato scritto a mano.
R2' di S-ROADMAP: lettura INTEGRALE di D6 e della pipeline decision map
    (non grep), PRIMA di scrivere tools/roadmap_derive.py; ogni deviazione
    tra lo schema D di questa advisory e la roadmap derivata va LOGGATA
    come finding di metodo (classe: authored-from-partial-context).
Precedenti che provano la fattibilita' del metodo NEL record: ADVISORY_INDEX
biiezione 90/90 con lint (xx); findings registry con rejector seminati (253,
0 violazioni); TRACE_ESA_FINAL (20 righe tracciate a carrier). Lo stesso
strumento va applicato AL PIANO. Fino al PASS di quel lint, NESSUNA
affermazione "il cammino e' completo" e' citabile — nemmeno la sezione E.
ATLAS COME SORGENTE (domanda utente, verificata 2026-08-31): l'atlas
RENDICONTA il piano — 290 menzioni di fase F0-F6 nei capitoli (CH4 62,
CH6 50, CH8 34, CH3 29, CH9 29, CH1 19, CH_REF 18, CH10 15, ...), CH6 §
"Collocazione di F4b nella catena" + "F3 and F4b ORDER-INTERCHANGEABLE",
ATLAS_TREE ATTO 7 = ROADMAP, ogni oggetto (C61/N2, H20, delta/L_H, ...)
porta il SUO atterraggio di fase. La vista dell'atlas e' INDICIZZATA PER
OGGETTO (per ogni oggetto: quando/dove atterra); D6 e' INDICIZZATO PER FASE
(per ogni fase: cosa entra/esce). Il buco NON era nel record: era la
mancanza del JOIN macchina fra le due viste — e la mia lettura parziale.
tools/roadmap_derive.py DEVE fare quel join (fase x oggetti-atlas x
registri) e il lint di copertura deve contare ANCHE le menzioni di fase
nell'atlas: ogni "F<n>" citato in un capitolo = un oggetto che deve
comparire nel passo di quella fase o portare OUT:<why>. Il record e' completo
per costruzione; la certezza e' il lint del join, non la mia memoria.
