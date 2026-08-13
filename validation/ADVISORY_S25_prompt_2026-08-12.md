# PROMPT — S25 "C4-FIRST + ENGINE SPEED SESSION" (consolidato S24;
# scritto alla chiusura S24, 2026-08-12)

Sei nel repo rde-lecture-code, branch rde-nozzle-program. HEAD atteso:
589cc56 ([F1b/CLOSE][PIANO/S24] R3 closure). Se trovi commit
successivi non tuoi, FERMATI e riconcilia. GENO/ = repo indipendente
(HEAD atteso fca273a su main), MAI committato da qui. UNA SOLA
SESSIONE ALLA VOLTA; protocollo rafforzato su OGNI commit (git log -3
+ status prima, commit path-limitati, audit hunk dopo); lint (xv)
verde GATED SULL'EXIT CODE; MAI pipe negli exit code. Directory
sspeed/ = perimetro della sessione parallela S-SPEED (bench):
consultabile, non tuo deliverable.

QUESTA SESSIONE E' LA S25 — "C4-FIRST + ENGINE SPEED" (1 sessione;
cap 3 h di run decisivi; regola STOP-WHEN-MET del dispatch). Stato
d'ingresso: F1b CHIUSA (S24: twin eseguito, branch F4
margin-inactive/cert-limited, EQ-v2 = CONJECTURE + H-CLASS). PRICING
DI RECORD (advisory §1, C1-corretto): record Python 111 s vs replay
C1 di PRODUZIONE ~13 s alla classe defnoz (il "2 s" era la chiusura
LINEARE del twin-track — ogni stima del piano e' C1-prezzata);
ledger S18 veritiero ~102-108 eval (non 67); cache XLA gia' armata
nei carrier (env var NON e' una leva). NEXT di record: questa
sessione, poi F2.

(1) APERTURA S10+ (letture OBBLIGATORIE): memorie s24-f1b-def-twin,
choice-adjudication-convergence, never-postpone-resolvables,
agentic-orchestration-forms (regola 7 + lezione stallo workflow),
s18-brick2-closed (il T2/G0 originale), generality-nonhardcoded-
procedures, scope-pins-frozen-thermally-perfect; M0 Parte VI blocco
S24 (bucket DE-side, H-CLASS, verdetto twin); PROGRESS ORA +
CENSIMENTO R1-R27 (d'ora in poi sweep INCREMENTALE); D6 F1b STATUS;
poi i TRE DELIVERABLE CONSOLIDATI di questa apertura:
 (a) validation/DISPATCH_Sspeed_to_S25_2026-08-12.md — L'ORDINE
     OPERATIVO DI RECORD (M0->M1->M2->M4->M3->M5->M6 + H3/H4;
     binding orders; gate che possono rigettare; N1-N8; Q1-Q6;
     dead rows DA NON RESUSCITARE) + il suo advisory completo
     validation/ADVISORY_engine_speed_audit_2026-08-12.md (LEGGERE:
     vincoli (1)-(7) verbatim, ledger G0/T2 veritiero §7.1 — true
     evals ~102-108, la riga di costo S18 e' STRUTTURALE non
     language-throughput);
 (b) validation/ADVISORY_S24_sota_gapmap_2026-08-12.md + annex
     CHOICE LEDGER — DEPOSITATO (76 KB; 36 voci: 5 HIGH, 23 MEDIUM,
     8 LOW; 16 already-covered; ledger 45 righe di cui 23 MAI
     aggiudicate con owner; 26 probe consolidati S25). I 5 HIGH:
     GAP-1 surrogato KS-max della frontiera (spec+demo pronte,
     owner F2); GAP-2 certificato B-stazionarieta' a outcome-II
     (owner F2); GAP-3 certificato Newton senza qualificazione di
     condizionamento/branch — falso-FAIL ratio 25 near-fold e
     falso-PASS misurati su toy, CANDIDATO MECCANISMO dentro la
     frontiera (owner F2 diagnosi, caveat toy quarantinato);
     GAP-4 TR_FLOOR=1e-3 non derivato = la risoluzione dell'uscita
     outcome-II — LA FORMULA DERIVATA (K_RICH*tol_dp/||g||) SI
     ESEGUE IN QUESTA SESSIONE (aritmetica su numeri loggati,
     [RIGOR]); GAP-5 BC naturale y''(L)=0 vs not-a-knot al lip
     (76x sull'ultimo intervallo, meccanismo alternativo per
     [C-O33]) — IL TWIN NOT-A-KNOT REGISTRATO SI ESEGUE QUI se
     budget (probe economico), altrimenti F2 con riga;
 (c) le condizioni panel S24 residue: C-A oracolo esattezza termo
     (prossimo tocco X-THC1 = probabilmente M3 QUI: eseguire
     insieme), C-B/C-C/C-D (owner dichiarati), C7+O5 (gamba refine =
     S24+1 opzionale, NON questa sessione salvo ordine utente).
REGOLA DI DEDUP VINCOLANTE: gap-map e dispatch S-SPEED coprono
territorio sovrapposto — ogni item va riconciliato in UNA riga sola
(evidenza doppia = piu' forte, mai due code); ogni item nuovo entra
SOLO come delta del censimento R1-R27.

(2) GATE di pre-esecuzione (pre-dichiarazioni R5 PRIMA di ogni
modifica: baseline M0 re-ancorata su host pulito PRIMA di ogni
verdetto di accettazione — tutti gli assoluti dei bench S-SPEED sono
dichiarati contesi; ogni cambio di versione DICHIARATO (M3, M6) con
KAT + O3.1 re-pass; vincoli (1)-(7) dell'advisory verbatim). Poi i
duty in quest'ordine:

T1 [C4 CHIUSURA MECCANICA — PRIMA DI OGNI ALTRO LAVORO, collocazione
scritta S24, TERZA MIGRAZIONE VIETATA]: tier env-conditional dei
carrier on-demand in run_all.py + campo tipizzato ondemand nel
registro/lint (sostituisce il bypass a substring) + staleness link
(data PASS-of-record vs ultimo commit del carrier); l'annotazione
onesta "suite verde = carrier-esclusiva" cade SOLO a chiusura
completa; suite piena verde di verifica.

T2 [ENGINE SPEED — l'ordine del dispatch, ESEGUITO ALLA LETTERA]:
M0 re-baseline (host pulito, C1-baseline, handoff ledger G0/T2) ->
M1 record dedup -> M2 memo fun+jac/m+gm + riparazione n_eval [RIGOR
comunque] -> MEASURE M-A -> M4 plan-as-args (il refactor pesante,
1-2 sessioni di budget: se sfora, e' LUI il taglio, non i gate) ->
MEASURE M-B -> M3 chiusura fusa (con C-A oracolo esattezza nello
stesso tocco) -> MEASURE M-C -> M5a/b/c record compilato con gate
bitwise -> MEASURE M-D = STOP CHECK 1 -> M6 vmap-Hessiano (cambio
di versione dichiarato) -> MEASURE M-E = STOP CHECK 2. STOP-WHEN-MET:
target segmento <= 30 s / campagna <= 25 min a defnoz A PARITA' DI
CERTIFICAZIONE; raggiunto il target gli item di sola velocita'
restanti NON si implementano; H3+H4 si schedulano COMUNQUE prima
della prossima campagna decisiva (protezione del cap); [RIGOR] rows
comunque; shortfall -> H1/H2/H5/O1-O4 per l'advisory, conditionals
N1-N8 restano nominate. OGNI item si ferma al suo cost cap e va al
suo fallback nominato — MAI debugging in-session illimitato.

T3 [REVIEW G0/T2 — consumata QUI]: verdetto sulla riga di costo con
il ledger veritiero (§7.1) + i numeri post-M* misurati; esito nel
log + D6 annotato (la review era in coda da S18).

T4 [CHOICE LEDGER — assorbimento]: le righe NEVER-adjudicated del
ledger (annex gap-map) diventano righe di censimento con owner
(survey bounded in F2/F3 come da R25); le righe che il dispatch ha
GIA' aggiudicato (es. eager cell_scan REJECTED, external interp libs
= dead row) si chiudono con puntatore all'evidenza. NIENTE survey
aperti in questa sessione (P3): solo collocazione.

T5 [CHIUSURA R3]: sweep INCREMENTALE del censimento (delta di
R1-R27: R3c consumata, R7c consumata, R22 consumata/stato, R26
consumata, R25 aggiornata); contatore "S25 speed: target MET/NOT-MET
(numeri)"; PROGRESS/D6; memoria s25; NEXT = F2 GENERAL ENGINE
apertura (contatore "F2 session m/6", C6 pre-entry, G6 da F2a;
near-axis + rejector C1 rafforzati dalla terza istanza; F2a assorbe
mean_swirl — decisione utente 2026-08-12; U3'; census-lemma+PAP-RIM
a F2-exit) O la S24+1 opzionale (C7/O5 + adjudication O3 set
bilaterale) se l'utente la apre prima.

TERMS: verdetti S14-S24 NON si rilitigano (incl. panel S24 e survey
termo: KEEP quintica — M3 la FONDE, non la sostituisce); PIN
P1/P2/P3; R5 numeri solo da carrier committati; R4 stessa sessione
per ogni delta teorico; env numpy 2.5.1 / jax 0.11 / scipy 1.18
(O5-dispatch: numpy 2.5.2 [RIGOR] ammesso a confine di sessione);
cache XLA persistente; tasklist mai kill -0; workflow lunghi
verificati sul transcript dir. FALLBACK: ogni M-item al suo fallback
nominato; se M4 sfora il budget, dichiarare e chiudere con
M0-M3+H3/H4 (gia' ~2-4x) + il resto a S25-bis nominata. Italiano in
chat, inglese in doc/commit. Chiusura R3 obbligatoria.
