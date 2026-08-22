# PROMPT DI SESSIONE — S-PRES (milestone PRESENTAZIONE ESA; catena
# user-ratified 2026-08-20: C4 -> S-PRES -> F2. Collocazione: DOPO la
# chiusura piena di S-FOUNDATIONS-C4 (R35 CONSUMED: Fase C 62 righe,
# Fase D dimostrata e atterrata, coverage gate PASS, pipeline map di
# record), PRIMA di F2 blocco 0. Regole d'ingaggio = R2-R7 CLAUDE.md +
# le regole standing dei prompt C2/C3/C4 (read-then-quote, SR-12,
# depth markers, no-assent-bias, screen-vs-measured) + il checkpoint
# SESSION_STATE (blocco C4) + il log PROGRESS_2026-08-21_
# SfoundationsC4.md.)

Verifica HEAD (commit atteso = [PIANO/R35] chiusura C4 2026-08-21);
commit non tuoi = FERMATI e riconcilia (cautela sessioni parallele).
Env pinnato (fingerprint closeC4, 29 pkgs, numpy 2.5.2). Modelli:
pin Fable invariato. Contesto: disciplina di record.

## MISSIONE (ordine utente 2026-08-20, verbatim intent)
Prima presentazione del progetto a ESA (milestone): "sviscerare il
grafo di progetto" con struttura da presentazione scientifica SOTA —
efficace, poco testo, NON over-matematica — con introduzione ottima e
affilata su letteratura e pratica degli ugelli RDE, "far vedere come
è un efflusso di RDE", nulla dato per scontato; "ogni anello SOTA
nella sua ramificazione e nella sua adozione"; piena sequenzialità
scientifica di ogni affermazione. OGNI slide-claim = CITE-ONLY dal
record alla sua classe di rigore (zero claim orfani, zero claim
sopra classe). La matematica compare come STRUTTURA; le prove nel
backup deck / M0.

## ADDENDUM UTENTE 2026-08-22 (post-chiusura C4, SUPERSEDING sul
## deliverable; il resto del prompt resta vigente):
## ARCHITETTURA DEL DECK RIDEFINITA — due presentazioni caricate in
## reference_presentations/ (Presentazione_CVA_RDE.pptx 11MB;
## ppt_Heister.pptx 12.7MB):
## (1) CENSIRE, LEGGERE E CAPIRE entrambe INTEGRALMENTE al Block 0:
## pptx = zip di XML + media -> estrazione testo slide con stdlib
## (zipfile + xml.etree, MAI installare pacchetti) + media estratti
## in scratchpad e LETTI VISIVAMENTE (le slide sono oggetti visivi:
## struttura, palette, gerarchia, figure); censimento = per-slide
## (titolo, contenuto, ruolo narrativo) per entrambi i file.
## (2) TEMPLATE/STILE: candidato = Presentazione_CVA_RDE; adozione
## SOLO SE un'aggiudicazione AGNOSTICA lo giudica SOTA per il target
## (audience tecnica ESA, milestone): criteri espliciti (densita'
## testo, gerarchia visiva, leggibilita' figure, professionalita'
## template) con verdetto motivato su file — se NON regge, stile
## alternativo proposto con ragioni (l'adozione non e' automatica:
## condizione posta dall'utente stesso).
## (3) DELIVERABLE = ESTENSIONE DI ppt_Heister: il deck finale e'
## l'esposizione COMPLETA di cio' che il gruppo dell'utente sta
## facendo sugli RDE — ppt_Heister MIGLIORATO in stile E contenuto
## (ogni miglioria di contenuto = cite-only dal record dove tocca il
## nostro programma; le parti di gruppo non-nozzle si migliorano in
## forma/chiarezza senza inventare contenuto tecnico non verificato
## — per quelle vale il vincolo: struttura/stile si', claim tecnici
## nuovi NO senza fonte dell'utente). Verso la FINE di ppt_Heister
## c'e' un accenno agli ugelli: QUELLO e' il punto d'innesto — da
## li' si apre la sezione S-PRES sul programma nozzle (lo skeleton
## del Blocco 1 sotto diventa la sezione innestata, non un deck a
## se'). Coerenza narrativa: il ponte accenno->programma va scritto
## esplicitamente (perche' il gruppo investe sugli ugelli: il
## collo di bottiglia pressure-gain, i 4-13 punti di ideale sul
## tavolo).
## (4) DECISIONE O5-CLASS al Block 0 (utente): l'authoring .pptx
## richiede realisticamente python-pptx (NON nel pinned env, 29
## pkg): opzioni = (a) install python-pptx dichiarato+fingerprint
## al confine (O5-class, decisione utente); (b) authoring in
## formato intermedio (HTML/markdown deck) con conversione manuale
## utente; (c) editing XML diretto stdlib (fattibile ma fragile,
## dichiarato). Presentare, non decidere.

## BLOCCO 0 (apertura)
R2 + gate con verdetto su file. Counts rigenerati (attesi chiusura
C4: choice 62 = 12/36/12/2 / findings 249 (207) / claims 163 /
glossario 47+238 / lit 165 [79 W] + 9 bulk). DUTY VINCOLANTI:
(a) TRIGGER SWEEP da comando misurato (presentazione esterna = atto
trigger-bearing): grep dei trigger 'external presentation'/'public
claim'/'first external' su findings/choice/claims registries; esiti
attesi MINIMI: riga :1455 (equivariance+uniqueness S1 del claim
two-stage) SPARA -> decisione: eseguire la duty S1 in-window O
presentare il claim dichiaratamente SCHEMA; D-44 = claim di
adeguatezza GATED (la forchetta si presenta come bracket con
provenienza, MAI adequacy dimostrata); riga P34 (claims:engine-
level-staged-evidence-hierarchy-missing) = istanziazione LEGGERA
qui (staging dichiarato dei claim su slide: verificato / validato /
predizione); novità query-bounded anche su slide (G5 Kraiko gate =
submissions, non presentazioni — ma il wording resta bounded).
(b) DECISIONI UTENTE: formato (PPTX / PDF-Beamer / HTML deck),
durata target, audience tecnica attesa, data della milestone.

## BLOCCO 1 — ESTRAZIONE + SKELETON (cite-only)
Estrazione contenuti dal record (1-2 slot): ogni candidato-slide =
claim + ancora + classe. ASSET SORGENTE (di record, committati):
docs/rde_nozzle_pipeline_decision_map.md = LA SPINA DORSALE (62
nodi/45 archi: il grafo sviscerato con ogni scelta giustificata);
M0 [R22F-FORCHETTA] = la slide di onestà (bracket per canale,
no-referee declaration); FIELD_ATLAS + THROAT_FIELD_HARVEST +
campagna nozzle-RDE = sezione "com'è un efflusso RDE / cosa fa la
pratica" (figure pubblicate citate, dicotomia istantaneo/medio in 4
codici); BASE_PRESSURE_HARVEST (Humphreys x2.45 = il warning storico
a livello design); genealogia Rao -> Hoffman (isoperimetrici/Bolza)
-> Allman-Hoffman (diretto) -> Kraiko-Tillyaeva 2015 (adjoint di
campo + gradiente di forma) -> noi (discreto-esatto + certificati +
PER-FASE); Li-Xu 2025 conclusione (3) "approximately applicable" =
LA citazione-bisogno (il campo ha la conclusione senza barra: noi
quantifichiamo l'avverbio); GAP-A/GAP-B value frame (Gap B
misurabile in-house; Gap A bounded-only: nessuno può calcolare
l'ottimo 3D vero — noi lo limitiamo); engine numbers di record
(0.45 s val_grad, campagna 10-14 min, 18x). GUARDIE: best-of-sweep
!= argmax (nessun paper ha mai ottimizzato il 3D vero — sweep e
redesign manuale soltanto); CT-6 (numeri dei paper = mai nostre
bande); claim di copertura letteraria citano il protocollo EMENDATO.
SKELETON narrativo: contesto RDE/pressure-gain -> efflusso reale
(figure) -> pratica ugelli RDE e suo fondamento implicito -> IL
problema (media senza barra; Level-1/Level-2) -> il nostro approccio
(quoziente/per-fase, T-DISC, K-bar=0) -> il grafo delle scelte (mappa,
ogni anello aggiudicato vs alternative con recency) -> onestà
(forchetta, residui δ/L_H, deciders) -> risultati macchina (engine,
certificati, probe) -> roadmap (M-RED -> CFD-2 -> CFD-1) -> ask.

## BLOCCO 2 — DECK + DOPPIA REVIEW + LOOP UTENTE
Authoring del deck nel formato deciso. POI: (1) RIGOR REFUTER
(slide-per-slide: ogni claim <= classe della sua ancora, ancore
verificate a campione 100% sulle load-bearing, zero orfani; le
guardie rispettate); (2) COMMS REVIEW (standard SOTA presentazioni:
una idea per slide, gerarchia visiva, testo minimo, figure che
portano il messaggio); entrambe until-fix con cap 2; (3) LOOP CON
L'UTENTE sulle bozze (il target finale lo giudica lui). Backup deck
con le prove/dettagli per il Q&A.

## BLOCCO 3 — CHIUSURA R3
Log, ORA/NEXT, indice righe misurate, suite EXIT 0, fingerprint,
commit pathspec espliciti (MAI GENO/Uno/stray; re-verify HEAD),
HANDOFF. NEXT = F2 blocco 0 (contatore 0/6; re-chain; finestra
engine: cluster C31/C57/C58/C60/[P-IPADJ]; M-RED prima campagna;
CFD-2 in coda; CFD-1 post-M-RED; sessione topologia+modellistica
BLOCCATO-16 a F2-entry con scope field-reading esteso).

## TERMS
R4/R5/R7 vigenti; autorità non rilitigate (VERDICT_r22f /
VERDICT_blocco2 / VERDICT_escalation_c4 / coverage gate PASS /
pipeline map refereed); artefatti in validation/spres_raws_2026-*/;
dedup SEMPRE; HANDOFF items C4: delete P-C lockato + rmdir staging
quando il lock si libera; 3 stray mai committati. La bussola:
comunicare il programma SENZA gonfiare una sola classe di rigore —
l'onestà strumentata È il vantaggio competitivo del deck.
