# PROMPT DI SESSIONE — S-COLLAPSE (sessione teorica DEDICATA,
# parallela alla linea F; ordinata dall'utente 2026-08-11 per
# saturazione della finestra corrente. Advisory, untracked.)

Sei nel repo rde-lecture-code, branch rde-nozzle-program. SESSIONE
TEORICA DEDICATA S-COLLAPSE, parallela alla linea sequenziale F.
VINCOLO DI NON-INTERFERENZA (obbligatorio): dichiara HEAD
all'apertura e riconcilialo col log della linea F; tocca SOLO file
propri (nuovo log a ordine totale
validation/PROGRESS_<data>_Scollapse.md, nuovi advisory/doc);
NESSUN file del motore (validation/*.py del march/driver); delta a
M0/D-doc SOLO nelle sezioni di tua competenza (G2/T3/T0), commit
path-limitati, lint (xv) gated sull'exit code, audit hunk dopo ogni
commit.

MANDATO: formalizzare CON RIGORE A CONVERGENZA la QUESTIONE DEL
COLLASSO: se e perche', nel caso GENERALE del progetto, il profilo
ottimo e l'Isp ottimo di un bell a vincoli dati coincidono (o no)
con l'ottimo del motore steady equivalente A PARI PORTATA
(metodologia alla Harroun). L'affermazione di uguaglianza e' FORTE:
va dimostrata dove vale, rotta dove non vale, e mappata sul piano.

INPUT OBBLIGATORI (leggere per interi, in quest'ordine):
 1. validation/ADVISORY_rde_choking_2026-08-11.md — TUTTO, in
    particolare §2-bis (matching a pari portata; item (ii) sotto
    panel; (ii-bis assente: v. 2-ter); §2-ter = la CORREZIONE DI
    RECORD del lead ("bell ~ 0" era in-hypothesis only) +
    l'analisi di scale-invariance con i breaker (a)-(e) + lo swirl
    primo-vs-secondo momento col verbatim K-P.
 2. L'esito del panel mean-swirl (workflow wf_d37cefa8-e69):
    l'advisory atterrato al suo completamento (se assente,
    leggere il journal del workflow).
 3. M0: enunciato T3/T7, Lemma T3-A (pin ideal-gas, audit
    theory-core:F2), la misura T0, il blocco EAP-containment.
 4. docs/rde_nozzle_literature_map.md riga G2 (+63-70).
 5. Pagine di record (PDF nella dir sopra il repo): Stechmann
    Figg. 8-9 + p.889 (assunzioni); Kaemming-Paxson §V.C p.7 e
    §VI.F p.11 (non-axial: "no net momentum... there is some
    energy"; +6%/+3%); Harroun pp.665-671 (matching pari-portata,
    C_F quasi-cycle-averaged SENZA C_F unsteady, Fig. 19).
 6. Memorie: claim-dual-proof-standard, agentic-orchestration-forms
    (Form 2 + Form 3), agnostic-milestone-review-directive,
    generality-nonhardcoded-procedures.

TASK (ognuno con lo standard DOPPIA PROVA: derivazione aggiudicata
a convergenza con refuter dedicato + carrier/misura nominata; Form
2 panel-a-convergenza per T1/T2; Form 3 red-team del giudice PRIMA
di ogni assorbimento):

T1 [ENUNCIATO ESATTO DI T3]: estrai enunciato e ipotesi REALI di
T3 dal corpus (quale media compare? "Rao a <Pc>" con quale peso?);
deriva formalmente la SCALE-INVARIANCE: sotto scaling p-only k(xi)
(Lemma T3-A) e obiettivo scale-invariante (vacuum-equivalent),
F(xi)=k F1, mdot(xi)=k mdot1 => Isp = F1/mdot1 indipendente dalla
distribuzione di k => ottimo di FORMA identico per ogni fase e per
OGNI convenzione di media (la domanda "quale pressione media"
diventa moot DENTRO le ipotesi). Verifica se questo E' gia' il
contenuto di T3 o va registrato come precisazione (classe di
rigore; delta a M0 G2 se la frase "Rao a <Pc>" e' impropria).

T2 [I BREAKER, UNO PER UNO]: per ciascuno: enunciato formale,
derivazione, grandezza attesa con ancora di pagina, e la
misura/carrier che lo decide.
 (a) TERMINE AMBIENTE pa != 0: derivare Isp(xi) =
     (k F1 - pa dA)/(k mdot1) e la dipendenza dell'ottimo dalla
     intera distribuzione di k; le fasi basse sovraespanse
     (Stechmann Fig. 8); stima per un booster; VERDETTO ATTESO: il
     bell sea-level e' FUORI collasso al PRIM'ORDINE, il
     vacuum-equivalent e' protetto. Quantificare l'ordine.
 (b) VARIAZIONE M/T/s PER-FASE: termini di Jensen con
     (sigma/mu)^2 ~ 0.5 (P-M p.5); quali funzionali sono convessi/
     concavi nel dato e segno atteso dello shift.
 (c) SWIRL: primo momento (assorbire l'esito del panel mean-swirl:
     bilancio del momento angolare, ipotesi esatte) vs ENERGIA
     (3-6% EAP, K-P verbatim) + ASIMMETRIA DI RECUPERO
     (u_theta = Gamma/r: espansione outward recupera, inward
     concentra — termine CONTRO il plug, segno opposto agli
     altri; N6-2 Bernoulli come meccanismo); formalizzare il
     termine di selezione-famiglia e il rung axial-vs-total
     mancante (bounds.py — nominare il carrier, non implementarlo
     qui se tocca il motore: dispatch alla linea F).
 (d) PATCH SUBSONICHE (K-P Fig. 6): cambio di regime, non
     perturbazione; conseguenza sul collasso e sul contratto a due
     regimi.
 (e) LA MISURA T0: quando la scelta della media conta (esattamente
     quando la scaling si rompe), quanto vale la differenza
     (Var(p)/<p> ~ 50% alle ampiezze RDE) e perche' il funzionale
     formale NON ha questo parametro libero mentre la metodologia
     mean-field si' — il valore del programma anche sul bell.

T3 [LA MAPPA "SIAMO NEL COLLASSO?"]: inventario formale di dove il
programma si muove dentro/fuori: twin attuale (vacuum-equivalent +
omentropico + single-phase) = DENTRO per costruzione (il +0.04% di
S18 = misura d'angolo, MAI citarla come fatto generale);
applicazione RDE (backpressure di booster, dato reale stratificato
con swirl) = FUORI sugli assi (a)-(e); tabella per fase del piano F
di quando ogni asse acquisisce la sua macchina.

T4 [PROTOCOLLO T3-CONTROL DEFINITIVO, pre-registrato]: la riga di
controllo collasso-vs-guadagno va specificata DI RECORD prima di
ogni run decisiva futura: backpressure dell'APPLICAZIONE (non solo
vuoto), matching dichiarati (pari-portata vs pari-<p> vs momento
angolare), ENTRAMBE le pesature dove la scaling e' rotta, barre
derivate, esiti entrambi onesti (collasso certificato / guadagno
misurato). Il protocollo e' testo pre-registrato R5.

T5 [R4 STESSA SESSIONE]: teorema + breakers + mappa in un
doc/advisory di record con classi di rigore dichiarate; delta a M0
(G2/T3/T0) se gli enunciati vanno precisati; registro aggiornato;
chiusura R3 del log.

TERMS OF REFERENCE: standard doppia-prova vincolante; Form 3
(red-team del giudice) prima di ogni assorbimento; nessun numero
senza carrier committato (le stime di grandezza sono ATTESE
letteratura-ancorate, marcate come tali); cauto-ma-SOTA (curiosita'
larga in survey, rigore stretto all'adozione); novita'
query-bounded (Kraiko/Guderley/Shmyglevskii per il collasso
classico multi-punto: verificare che nessuno abbia gia' enunciato
il collasso cycle-averaged — la G2 dice NOT-FOUND(q), ri-boundare);
italiano in chat, inglese in doc/commit. IN CODA DOPO (NON
eseguire qui): implementazione del carrier T3-control (linea F);
rung bounds.py (linea F); qualsiasi run del motore.
