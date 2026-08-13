# PROMPT DI SESSIONE — S-ORDINE "DE-ENTROPIZZAZIONE DEL PROGETTO"
# (scritto 2026-08-12 alla coda di S25-bis su ordine utente; censimento
# R32; collocazione di record: DOPO la coda di convergenza S25-bis,
# PRIMA dell'apertura F2 GENERAL ENGINE. Assorbe la prima duty R31 —
# seeding del corpus nel findings registry.)

Sei nel repo rde-lecture-code, branch rde-nozzle-program. Verifica
HEAD con git log -3: tutti i commit recenti portano tag
[F-SERVICE/S25bis...] e sono attesi; qualsiasi commit non tuo =
FERMATI e riconcilia. GENO/ = repo indipendente, MAI committato da
qui. UNA SESSIONE ALLA VOLTA; protocollo commit rafforzato; suite e
lint GATED SULL'EXIT CODE, redirect-only; FREEZE edit su file
tracciati mentre un consumer gira.

QUESTA SESSIONE E' LA S-ORDINE. Obiettivo (ordine utente 2026-08-12,
verbatim intent): "limitare lo sviluppo di entropia nel progetto...
un workflow dedicato di esperti SOTA che leggano ogni cosa, senza
perdere nulla, capiscano il modo SOTA di gestire tutti questi
documenti e PIANIFICHINO PRIMA DI INTERVENIRE, arrivando a
convergenza sul miglior modo di organizzare il tutto, e poi educando
anche gli sviluppi futuri a mantenere la struttura."

## (1) APERTURA (R2, letture obbligatorie)
Memorie: s25bis-speed-complete, orchestration-weight-sota,
agentic-orchestration-forms (Form 1/2/3 + regola full-text),
choice-adjudication-convergence, never-postpone-resolvables,
pipeline-sense-expert-review; PROGRESS ORA + censimento (R31/R32);
docs/findings_registry.yaml (17 righe = autorita' dedup);
validation/PROGRESS_2026-08-12_S25bis_speed.md STEP 15 (mappa di
convergenza); QUESTO prompt integrale. Poi gate pre-esecuzione con
verdetto loggato.

## (2) LA DIAGNOSI DI PARTENZA (misurata 2026-08-12, da verificare
## fresca in apertura con gli stessi comandi ls/wc)
Sorgenti di entropia: (a) PROGRESS.md ~2.500 righe a crescita
monotona, censimento a blocchi-delta; (b) validation/ = 77 file .md
(31 ADVISORY/AUDIT/DISPATCH/PANEL/ADR + 27 log di sessione
PROGRESS_* + altri) TUTTI UNTRACKED (pattern ADR: copia singola,
zero storia git = rischio durabilita' DA DECIDERE), piu' 33 .py
carrier/probe, 25 .json artifact, ~20 .log, raws 17 file;
(c) docs/ = 41 .md + 2 registry .yaml; (d) memoria = 37 file;
(e) findings in prosa (audit 94 righe, gap-map 36, choice ledger 45
come ANNEX del gap-map, refuter/red-team) = il meccanismo del
re-mint; (f) memorie di sessione vecchie non marcate superseded.
PRINCIPIO VINCOLANTE: de-entropizzare = convertire prosa in
artefatti TIPIZZATI e LINTATI + status di supersessione espliciti +
archivio con banner — MAI cancellazione (R4: nulla si perde;
archive != delete).

## (3) T1 — IL WORKFLOW DEDICATO (pianificazione a convergenza,
## PRIMA di qualsiasi intervento; Workflow tool, ~12-13 agenti)

FASE 1 — INVENTORY (6 reader paralleli, effort basso/medio,
COPERTURA CONTABILE): genera in apertura la lista file autoritativa
(ls per segmento, conteggi sopra come riferimento) e passala come
args; ogni reader rende conto di OGNI file del suo segmento
(coperto / classificato-senza-lettura-integrale con ragione
dichiarata — es. i .log = evidenza derivata il cui contenuto di
record vive nei session md). COPERTURA = L'INTERO TREE, NESSUN
FILE ESCLUSO (ordine utente verbatim: "tutti i file, non ne devi
mancare uno") — misurato 2026-08-12: 428 file nel repo (238
tracciati) escl. .git e GENO; la lista autoritativa si genera con
find/git ls-files e OGNI file finisce in un segmento con status
contabilizzato; riconciliazione finale: somma dei file
contabilizzati dai reader == conteggio autoritativo, scarto 0.
Segmenti (7 reader): (i) docs/ core (41 md + 2 registry yaml: M0,
D1-D7, piano, G0, kickoff, P2, PROGRESS — struttura e taglie);
(ii) registries + tests (21 py) + CLAUDE.md + src/ + data/ +
scripts/altro (classificazione di ruolo — NON code review);
(iii) advisories A-M; (iv) advisories N-Z + AUDIT + DISPATCH +
PANEL + prompt consumati (31 file classe-advisory totali);
(v) session log PROGRESS_* (27) + raws (17) + inventario
validation/*.py (33) / *.json (25) / *.log (~20); (vi) memoria
(MEMORY.md + 37 file); (vii) LETTERATURA SU TRE RADICI (ordine
utente: "per ogni file di letteratura, qui, nel repo padre o
dentro GENO, sappiamo il contenuto e ricordiamo le analisi fatte")
— repo literature/ (13 PDF), repo PADRE "Presentazione RDE CVA/"
(~10 PDF top-level + la stirpe delle presentazioni pptx +
CONTINUATION_PROMPT.md), GENO/ (77 PDF, read-only, MAI committato
da qui): per OGNI paper -> identita' bibliografica,
riassunto-di-contenuto DI RECORD, DOVE e' stato letto/analizzato
(anchor a sessione/advisory: es. i 5 letti integrali in
ADVISORY_rde_choking, i 24 della generality litmap, il G5 PMM
sweep, Giles-Ulbrich x2 in S-SPEED), status ONESTO (READ-INTEGRAL
/ READ-PARTIAL / UNREAD / WANTED-mancante, es. AIAA 2019-0197),
dedup cross-radice (stesso paper in due posti). I paper UNREAD si
REGISTRANO come UNREAD — mai riassunti finti; la lettura vera dei
mancanti diventa duty a valle con owner. DELIVERABLE ESECUTIVO
DEDICATO (in T2): docs/literature_registry.yaml tipizzato + lint
(anchor alle analisi risolti a macchina). SCHEMA di inventario per
file: path, classe, ruolo, STATUS-AUTORITA' proposto (OF-RECORD /
SUPERSEDED-BY-x / CONSUMED / RAW / DERIVED), link di supersessione,
CONTENUTO-UNICO-A-RISCHIO (findings/numeri/verdetti che vivono
SOLO li'), refs in/out. Artefatti su file in
validation/sordine_raws_<data>/; il return = solo path + conteggi.

FASE 2 — 3 POSIZIONI ESPERTE parallele (effort alto, lenti
distinte, leggono gli inventari + spot-check degli originali):
P1 = knowledge-management/docs-as-code SOTA (lineage: ADR Nygard,
Diataxis, docs-as-code, registries tipizzati, supersession
discipline, lint di copertura); P2 = provenance/durabilita' della
ricerca (findings provenance, integrita' d'archivio, IL RISCHIO
COPIA-SINGOLA degli untracked, esigenze del paper P-1/JPP);
P3 = vincoli-repo e right-sizing (R1-R6, meccanica censimento,
costo/rischio migrazione, estensibilita' dei lint esistenti,
anti-overengineering). Ognuno propone: struttura target (albero),
tassonomia status, cosa si tipizza/linta, piano migrazione A PASSI
con verifiche nothing-lost (conteggi riconciliati), bozza REGOLE
STANDING (la meta' "educazione").

FASE 3 — REFUTER dedicato (default-refute, effort alto) sulle tre
posizioni: rischi di perdita, hazard di migrazione, ricrescita del
drift, overengineering, conflitti con R1-R6.

FASE 4 — JUDGE fuso a convergenza per-questione (effort alto;
full-text: path, MAI slice; dedup contro findings_registry) ->
validation/ADVISORY_SORDINE_plan_<data>.md: struttura target di
record, tassonomia, piano-a-passi con verifica per passo, REGOLE
STANDING convergiute, DECISIONI UTENTE aperte (in primis: commit
degli advisory OF-RECORD si'/no — raccomandazione con trade-off).

FASE 5 — RED-TEAM Form-3 sul judge PRIMA dell'assorbimento (conti
riconciliati, nessuna claim judge-added, ogni "absorbed" puntato).

## (4) T2 — ESECUZIONE (SOLO dopo la convergenza del piano; nella
## stessa sessione se il budget regge, altrimenti la coda esecutiva
## e' LA prima duty della successiva — mai generico):
(i) SEEDING R31 dal corpus (audit 94 + gap-map 36/16/10 + ledger 45
+ refuter/red-team S25/S25-bis) con find->verify bounded, dedup
contro le 17 righe esistenti, lint (xix) verde a ogni tranche;
(ii) choice ledger estratto a docs/choice_ledger.yaml tipizzato +
lint (stesso pattern strict-subset); (iii) validation/
ADVISORY_INDEX (una riga per documento con status) + archive/ con
banner + micro-lint di copertura indice (documento senza riga =
violazione); (iv) PROGRESS slim (ORA/NEXT/BLOCCATO + tabella
censimento CONSOLIDATA una-riga-per-item; storia ->
PROGRESS_ARCHIVE); (v) sweep memorie (superseded marcate);
(vi) docs/literature_registry.yaml (una riga per paper sulle TRE
radici, schema della Fase 1(vii), lint con anchor risolti; i
WANTED/UNREAD con owner); (vii) OGNI mossa con verifica
nothing-lost dichiarata (conteggio sorgente == conteggio
destinazione + anchor risolti dal lint; riconciliazione 428-file
a scarto 0).

## (4-bis) T2-bis — ALZARE IL LIVELLO (estensione utente 2026-08-12:
## "colmare altri punti per alzare il livello della codebase" —
## SOLO gli item che usano la STESSA macchineria della sessione;
## scope creep = entropia):
(a) GLOSSARIO dei codenames (docs/glossary.md o yaml tipizzato):
generato DAI reader di Fase 1 (incontrano ogni token); lint di
risoluzione — ogni [X-*]/GAP-*/R-*/C-*/M-* usato nei doc OF-RECORD
deve risolvere a una voce di glossario o riga di registry;
(b) REGISTRO DEI FLAG DI ARBITRATO (una riga per env-flag A1_*:
default, significato, gate che lo copre, coppie testate vs prodotto
cartesiano DICHIARATO non testato) — la matrice oggi vive solo nei
docstring;
(c) regola standing PESO-ORCHESTRAZIONE MISURATO (shape + token
riportati nel log di sessione per ogni orchestrazione) dentro il
deliverable educazione;
(d) igiene della directory piatta validation/: il piano la
adjudica con il VINCOLO PREZZATO — spostamenti sicuri = artifact/
log/advisory; spostare i .py carrier rompe import e anchor
(claims/findings registry) e si fa SOLO se il judge lo prezza con
verifica anchor-lint post-mossa.
FUORI SCOPE (si REGISTRANO con owner, mai eseguiti qui): split del
driver monolitico (tocca carrier -> finestra F2 + sense-review);
CI schedulata / multi-piattaforma (decisione infra/env, riga
propria); distillazione per terzi (pipeline P-1); qualunque tocco
algoritmico.

## (4-ter) GATE NOTHING-LOST (vincolante, ordine utente 2026-08-12:
## "fondamentale non perdere nulla" — la garanzia deve essere un
## GATE che puo' sparare, non un principio):
(i) LEDGER-A-RISCHIO: la Fase 1 produce l'elenco consolidato di
OGNI contenuto-unico-a-rischio (finding/numero/verdetto/analisi che
vive in UN solo posto); l'esecuzione T2 produce la MAPPA DI
DESTINAZIONE per-item (riga registry / file archiviato con riga
indice / riga glossario) e il gate verifica: ogni item del ledger
ha destinazione risolta — item senza destinazione = FAIL della
sessione, non nota a pie' di pagina.
(ii) LOSS-HUNTER AVVERSARIO: a valle dell'esecuzione, UN agente
dedicato col solo mandato di TROVARE qualcosa di perso (default:
"si e' perso qualcosa finche' non dimostro il contrario"):
campiona il ledger-a-rischio + diffa gli inventari pre/post +
tenta di risalire da 10 finding storici casuali alla loro casa
attuale. Un solo item irrintracciabile = FAIL.
(iii) REJECTOR SEMINATO del detector: si rimuove IN-MEMORIA un
item dalla mappa di destinazione e il gate (i) DEVE fallire; il
loss-hunter riceve un item-canarino assente e DEVE segnalarlo —
un detector che non spara sul seme e' rotto e la sessione non
chiude su di esso.
(iv) La riconciliazione a scarto 0 (428 file + 3 radici
letteratura) e' PRECONDIZIONE di chiusura R3 della sessione.

## (5) T3 — EDUCAZIONE (il mantenimento)
Le regole standing convergiute atterrano come: delta CLAUDE.md
(proposto all'utente per ratifica), riga di censimento standing, e
UNA riga aggiunta alla checklist di chiusura R3 ("ogni advisory
nuovo = riga indice + righe registry nella stessa finestra").
L'educazione e' fatta di lint che sparano, non di raccomandazioni.

## TERMS
R4: mai cancellare, solo archiviare con banner+indice; verdetti
S14-S25bis NON si rilitigano; le decisioni utente pendenti
(filelock/O5/M6-adozione) restano della loro finestra (confine
F2), NON si consumano qui salvo ordine; peso orchestrazione
right-sized e RIPORTATO; artefatti su file SUBITO; resume mai
relaunch; italiano in chat, inglese nei doc/commit; chiusura R3
obbligatoria con censimento aggiornato (R32 consumata, NEXT = F2).
