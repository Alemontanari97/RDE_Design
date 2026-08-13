# PROMPT — Sessione parallela S-SPEED: audit avversariale a convergenza
# della logica di programmazione del motore (JAX + MoC) per la velocità
# SENZA perdita di rigore (2026-08-12; consumo: S25 "ENGINE SPEED
# SESSION" + review G0/T2)

Sei nel repo rde-lecture-code, branch rde-nozzle-program, in una
SESSIONE PARALLELA READ-ONLY (pattern della generality-review
2026-08-12): NESSUN commit, NESSUN edit a M0/PROGRESS/D-doc/carrier;
ogni delta testuale diventa DUTY con owner nell'advisory; prototipi e
microbenchmark SOLO nello scratchpad (mai committati). La sessione S24
(F1b) può essere ancora aperta: non toccare il suo perimetro (carrier
[X-DEFTW], log S24, artifact s24_*). Se trovi il repo a un HEAD
successivo, leggi il log di sessione più recente in validation/ prima
di giudicare qualunque cosa.

MANDATO: workflow avversariali A CONVERGENZA (forme di record in
memoria `agentic-orchestration-forms`: Form-1 find->verify con
verificatore default-REFUTED; Form-2 panel con refuter dedicato +
judge; regola 7 FULL-TEXT — le posizioni atterrano su FILE e i judge
leggono i FILE, mai slice inline; Form-3 red-team prima di ogni
assorbimento one-round) con esperti di livello mondiale su DUE assi,
alla RADICE del codice:
 (A) l'asse JAX/compilazione: tracing, custom_vjp, bucketing, jit
     whole-loop, cache XLA, vmap/parallelismo, costi di dispatch
     eager;
 (B) l'asse MoC/numerico: struttura della marcia (IVL+fan+arco+
     contorno), unit process di cella, certificazione Newton
     per-cella, segmentazione RK-G, driver TR-SQP, aggregazione KS.
OBIETTIVO: dove e come si accelera di 5-20x SENZA perdere UN GRAMMO
di: potenza descrittiva, capacità di trovare bug (rejector,
certificazione per-cella, controlli negativi), log/auditabilità
(record deterministico, piani congelati, verdetti riproducibili),
tolleranze derivate (R5), determinismo del replay.

EVIDENZA DI COSTO GIÀ MISURATA (di record, NON rimisurarla — usala
come baseline): record march Python adattivo ~111 s a 7818 celle
all'istanza defnoz (eps=30, L=8) vs REPLAY JITTATO della stessa
fisica ~2 s (gap ~50x = overhead interprete, ~14 ms/cella di
dispatch); la policy RK-G ri-registra a OGNI iterata accettata + a
ogni base di segmento + a ogni probe rigettata dal gate P4 (che
quindi costa 111 s per scoprire "non certifica", senza early-abort);
Hessiano misurato = 10 valutazioni di gradiente SEQUENZIALI (~20-40
s); segmento tipico 2-7 min; rung decisivo ~75 min; la riga di costo
T2 SPARÒ in S18 (121.6 s vs 35.9 s GENO, decomposizione onesta:
curvatura + re-record, non language throughput) e la review G0 è in
coda da allora. Leve già NOMINATE in S24 (partenza, non perimetro):
L1 certificazione tracciata cert_diag (~2 s, esiste già) al posto
della maggior parte dei re-record Python, un solo record a fine
segmento; L2 early-abort del record alla prima cella non certificata;
L3 vmap sull'Hessiano (10 perturbazioni in una chiamata); L4 batch
di design multipli (vmap) per multi-start/ladder/famiglie di
falsificatori; L5 record compilato (while_loop mascherato) — lift
maggiore, cambia la semantica dell'audit, richiede aggiudicazione.

FILE DI RADICE DA LEGGERE INTERI (i finder per sottosistema, whole
source leggibile): validation/a1_ideal_march_jax.py (unit process,
custom_vjp, tab); validation/a1_march_scan.py (scan/bucketing/
solvers); validation/a1_toc_variational_jax.py (record/replay/
run_trsqp/RK-G/cert_diag/val_diag/thrust_J); validation/
thermotab_c1_jax.py (chiusura C1); validation/margin_governor.py +
validation/def_twin_falsifier.py (margine KS, maschere, campagna);
docs/rde_nozzle_brick2_kickoff.md (policy di record); i log S17/S18/
S22/S24 in validation/ per i numeri e le decisioni di policy (X-LSG0
= i costi di record; S18 step 7 = attempt ladder del driver).

VINCOLI NON NEGOZIABILI (ogni proposta che li tocca è REJECTED by
construction, non "trade-off"): (1) certificazione per-cella
equivalente a quella attuale (stesso metro: un passo Newton extra
sotto banda derivata) su OGNI iterata accettata — può cambiare CHI
la calcola (tracciata vs Python), MAI se e con che metro; (2)
determinismo e riproducibilità del record (piani congelati,
bit-riproducibilità del replay al floor di Newton); (3) R5:
tolleranze derivate, zero magic; (4) REQ-NONSTALL (sopravvivi +
riporta); (5) i rejector esistenti restano capaci di sparare (ogni
sostituzione porta il SUO controllo negativo); (6) la struttura di
log/verdetto (righe PASS/FAIL, contatori nonfiniti, artifact JSON)
resta o migliora; (7) niente riscritture del metodo (TR-SQP/KS/RK-G
si OTTIMIZZANO, non si sostituiscono — un cambio di solver esterno è
ammesso SOLO come raccomandazione adopt-or-declare con survey).

DIRETTIVA STANDING VINCOLANTE (utente, 2026-08-12, memoria
choice-adjudication-convergence): OGNI punto di scelta algoritmico
toccato dal piano (parametrizzazione, nodi, chiusure, aggregazioni,
solver, policy TR, metrica di certificazione, costruzione bande,
seeds, passi) va aggiudicato A CONVERGENZA contro l'insieme delle
alternative SOTA, SENZA BIAS per l'incumbent: ogni alternativa ha un
avvocato genuino, il refuter attacca ANCHE la scelta attuale, e il
deliverable porta un CHOICE LEDGER (riga per scelta: incumbent,
alternative, stato di aggiudicazione CONVERGED/single-author/NEVER,
evidenza, owner se aperta).

STRUTTURA SUGGERITA (adattala se il quadro lo chiede): fase 1 =
finder per sottosistema (record-path; replay/jit; driver/segmenti;
margine/maschere; cert/log) con lente doppia (A)+(B), max-N finding
con drop count dichiarato; fase 2 = verificatore avversariale
default-REFUTED per finding (sul SORGENTE, con microbenchmark nello
scratchpad dove il costo è contestato — es. misurare DAVVERO il
costo per-cella del record, il costo di compilazione per bucket, il
guadagno vmap-Hessiano su un caso piccolo eps=4); fase 3 = panel di
sintesi con refuter dedicato + judge che produce IL PIANO: lista
prioritizzata di interventi, ciascuno con {meccanismo, guadagno
atteso (misurato dove possibile, stimato-con-derivazione altrove),
argomento di conservazione del rigore (quale vincolo 1-7 e come),
rischio nominato, test di accettazione/rejector proprio, costo di
implementazione, owner/collocazione}. Target dichiarato del piano:
segmento <= 30 s e campagna decisiva <= 25 min A PARITÀ di
certificazione, all'istanza defnoz.

DELIVERABLE (pattern ADR, untracked): (1)
validation/ADVISORY_engine_speed_audit_2026-08-12.md — il piano
aggiudicato completo (posizioni + refuter + judge, dispute ledger,
label "judge-adjudicated in one round" se one-round); (2)
validation/DISPATCH_Sspeed_to_S25_2026-08-12.md — SOLO i finding a
convergenza + il piano d'esecuzione per la "ENGINE SPEED SESSION"
S25 (che è già collocata nel censimento S24: dopo C4-first, prima
dell'apertura F2 piena, e consuma anche la review G0/T2 in coda con
l'evidenza S18). Quarantena esplicita per ciò che NON converge.

TERMS: verdetti di record NON si rilitigano (S14-S24, panel S24
inclusi); pin P1/P2/P3; env numpy 2.5.1 / jax 0.11 / scipy 1.18,
cache XLA persistente; processi con tasklist; la S24 può avere run
attivi — NON lanciare carrier pesanti in concorrenza senza
dichiararlo (i microbenchmark si fanno a istanza PICCOLA, eps=4).
Italiano in chat, inglese nei deliverable. Chiusura: artefatti su
file + 5 righe di sintesi, nessun edit al repo.
