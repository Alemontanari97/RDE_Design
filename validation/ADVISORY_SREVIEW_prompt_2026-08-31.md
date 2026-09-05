# ADVISORY — PROMPT DI SESSIONE "S-REVIEW" (revisione agnostica delle fondamenta; carrier di record, deciso dall'utente a chiusura F2-B0, 2026-09-05)

Stadio di confronto: chiusura F2-B0 (log validation/PROGRESS_2026-08-31_F2B0.md;
roadmap derivata lint (xxiv) PASS; ledger 62 = 12 DECIDED / 38 MIXED / 10 NEVER /
2 single-author, misurato 2026-09-05; conteggi da RIMISURARE in apertura, SR-12).
Arco di consumo: questa advisory -> sessione S-REVIEW -> F2.REPR (il cui
carrier ADVISORY_F2REPR_prompt_2026-08-31.md CONSUMA l'assessment: GO/NO-GO +
frame di rappresentazione) -> F2.ENGINE -> ... -> F3.TWIN. Autore: F2-B0
(single-author: S-REVIEW APRE con la passata di refuter su questo prompt).
Decisione utente di record (2026-09-05, verbatim gist): "una sessione di
profonda revisione di tutta la codebase, agnostica, navigando in ogni indice
e struttura di navigazione, per valutare la bontà delle scelte del piano; ogni
scelta modellistica dimostrata a convergenza; isolare le ipotesi di base;
tastare ogni rabbit hole; completezza della pipeline intera, oggi e nei
prossimi passi; generale, con workflow a convergenza sui punti più aperti;
rivalutare la scelta alle FONDAMENTA di ogni sottoproblema — non accettare
come vero, ad esempio, l'adjoint con ottimizzatore gradient-based: c'era
qualcosa di meglio? — la facciamo appena chiude F2-B0".
Direttive standing che la governano: agnostic-milestone-review,
choice-adjudication-convergence, claim-dual-proof, doubts-to-convergence,
general-vision-nondivergence, orchestration-weight-sota, formal-first.

PERCHÉ ORA (misurato, non asserito): (1) punto più economico per cambiare
direzione — dopo F2.ENGINE un flip fondativo costa la riscrittura del motore;
(2) F2-B0 ha misurato che lo strato "provato" è legato alla versione: due
carrier di record (X-O32, X-LOCD) NON riproducono sul tree corrente e la
frontiera di certificabilità K si muove con versione/recorder — la stabilità
della certificazione deve diventare requisito fondativo esplicito PRIMA di
costruirci sopra; (3) il record stesso ammette che il paradigma è "axiologia
dichiarata, mai head-to-head" (ledger C57, nota constitution-bias).
CONTRO-RISCHIO dichiarato: sette sessioni meta consecutive (S-ORDINE, S-CERT,
S-FOUNDATIONS, S-PRES, S-ROADMAP, F2-B0, questa) — il motore non avanza dal
2026-08-13. Quindi: UNA sessione, panel di fase B contingentati dal triage,
GO/NO-GO obbligatorio; "CONFIRM su tutto" è un esito accettabile (la
costituzione diventa aggiudicata invece che dichiarata).

================================================================================
## A. APERTURA (R2 + R8)
R2: docs/START_HERE.md -> memoria (s-f2b0-closed, s-foundations-design,
s-foundations-c4-closed, fservice-scert-double-session, agnostic-milestone-
review-directive, choice-adjudication-convergence, s20-adaptive-obstruction,
s22-f1-governor-o4) -> M0 Parte I-II (idea + formalizzazione: gli ASSIOMI),
Parte VI (implementazione), Parte VII (mappa) -> D1 problem book (contratto
d'interfaccia, hypothesis ledger) -> D6 (fasi, gate, Annex B) -> decision map
-> PROGRESS -> roadmap rigenerata + lint (xxiv) PASS -> dichiarare: sessione
di revisione FUORI fase (milestone F2-entry), path critical (il suo GO/NO-GO
gate-a F2.REPR/F2.ENGINE).
R8 (su file, PRIMA dell'authoring): (i) consumatore ESATTO = il referee JPP
che giudicherà il numero decisivo del TWIN (persona: scettico, chiede "perché
non X?" a ogni scelta) + il PM che chiede "è il cammino più corto credibile?";
(ii) criteri d'uscita = sezione E; (iii) TETTO d'orchestrazione: PROPOSTA
Stage A = 4 derivatori de-novo + 1 giudice-diff per sottoproblema (~12 agenti);
Stage B = panel Form-2 (avvocato + refuter) + verificatore per voce
divergente, numero di voci FISSATO dal triage con cap iniziale 6 (~18 agenti);
red team del nord = 1; refuter di chiusura = 1; totale atteso 25-35 agenti
Fable, ~5-8M token subagente — sopra la guideline media del Workflow: il
tetto lo fissa l'utente all'apertura (superamento = decisione utente, SR-9);
(iv) CONFINE RABBIT-HOLE dichiarato: ogni voce deve dire come cambia
credibilità o costo del TWIN; se non lo cambia, è fuori scope dichiarato;
time box per voce; un frame alternativo per ogni ostruzione; NESSUNA
riderivazione di teoria (fatta in S-FOUNDATIONS) e NESSUNA campagna
numerica (F2): la revisione trova buchi, riordina, pre-registra pilot.

## B. TOUCHPOINT UTENTE IN APERTURA
 T1 Tetto d'orchestrazione (Stage A/B come sopra, o ridotto/ampliato).
 T2 Perimetro dei livelli: livello 2 (paradigma/costituzione) SEMPRE; il
    livello 3 (ipotesi fisiche pinnate: onda periodica pura, miscela congelata
    termicamente perfetta, niente bifase, caso A per il TWIN) si rivaluta per
    RILEVANZA sul numero decisivo (sì/no).
 T3 Esito ammesso "PILOT": i flip fondativi plausibili ma non provati
    diventano pilot pre-registrati su UN caso con kill criterion (standard
    doppia prova) — chi li esegue: sessione dedicata post-review vs dentro
    F2.REPR/F2.ENGINE (default: F2.ENGINE come duty con carrier).
 T4 Il numero decisivo stesso è in perimetro del red team (default SÌ).

## C. ORDINI (nell'ordine; il fan-out di [5] lo decide [3]-[4])
 1. REFUTER sul prompt (single-author) -> PROMPT-n nel log; correzioni prima
    dell'authoring.
 2. ENUNCIATO AGNOSTICO su file (validation/sreview_raws_<data>/
    PROBLEM_STATEMENT_agnostic.md): obiettivo (numero decisivo e claim che
    lo consuma), classi di dato A-G (Annex B), vincoli (eps, L, p_b,
    troncamento, tolleranze as-built), requisito di certificazione (che
    cosa deve essere certificato e a che classe), pin di generalità (gamma
    variabile, procedure non hardcoded, settori bell/plug/shrouded/E-D, 3D
    come orizzonte), budget (sessioni, wall-clock per run decisivo, env
    pinnato) — SENZA una sola scelta del repo. LINT DI AGNOSTICITÀ: zero id
    di registro, zero nomi di carrier/ledger nel file (grep misurato).
 3. STAGE A (Workflow, fase "derive"): k derivatori de-novo in parallelo,
    brief = SOLO l'enunciato; output tipizzato = albero degli approcci 2026
    per ogni sottoproblema con costo/generalità/rischio/precedente di
    letteratura ([KNOWLEDGE] marcato) — sottoproblemi minimi: decomposizione
    del problema nel tempo (per-fase quasi-stazionaria vs unsteady diretta
    vs ROM/space-time); solutore di campo (space-marching iperbolico/MoC vs
    Euler shock-capturing vs DG/spectral vs potenziale); sensibilità
    (adjoint discreto via AD con regole implicite vs adjoint continuo vs
    complex-step/FD vs derivative-free); ottimizzatore (locale gradient TR-SQP
    + deflazione vs globale BO/DFO/evolutivo vs ibrido; certificate-first vs
    best-effort); frame di rappresentazione (assiale / 2.5D / azimutale /
    3D — solo il FRAME: il censimento è F2.REPR); parametrizzazione (spline
    vs level-set/CAD/free-form); ingestione dati (generato caso A vs fitting
    di dati captured vs surrogato); filosofia di certificazione (Newton
    per-cella + bande Richardson vs stima a posteriori DWR vs validated
    numerics) INCLUSA la stabilità della certificazione attraverso versioni/
    recorder/env; esperimento decisivo (TWIN su plug troncato a ~1% vs
    alternative). Lint di agnosticità sugli output.
 4. DIFF vs incumbent (Workflow, fase "diff"): un giudice per sottoproblema
    legge gli alberi de-novo + le righe di record (ledger, claims, M0 Parte
    VI, decision map) e classifica: CONFIRM-candidato / DIVERGENTE / NUOVO,
    con peso = effetto su credibilità o costo del TWIN e con la classe di
    aggiudicazione esistente (DECIDED con avvocato genuino -> solo delta-
    sweep 2026; axiologia dichiarata / NEVER / single-author -> panel pieno).
    TRIAGE inline dell'orchestratore su file: lista ordinata peso ×
    divergenza, cap del touchpoint T1, time box per voce.
 5. STAGE B (Workflow, fase "converge", SOLO sulle voci selezionate):
    falsificatore CONCORDATO prima di argomentare (adversarial
    collaboration) -> avvocato genuino dell'alternativa ⇄ refuter until-dry
    (contatore: agente morto = failure, MAI round secco; dual-seed = un falso
    noto + un vero noto nel lotto per misurare i due errori del revisore) ->
    giudice -> esito per voce: CONFIRM (con ragioni NUOVE, non ereditate) /
    FLIP PREZZATO (costo di riscrittura vs guadagno sul TWIN) / PILOT
    pre-registrato (un caso, kill criterion, owner e finestra).
 6. RED TEAM DEL NORD (parallelo a 5): un agente attacca il numero decisivo
    stesso — è l'esperimento che convince un referee scettico? quale
    controllo, banda, o secondo numero chiederebbe? Esito = emendamenti
    proposti al protocollo TWIN (§9, datati) o CONFIRM con ragioni.
 7. VERIFICA (Workflow, fase "verify"): verificatore indipendente per
    verdetto (legge i file, mai riassunti); canary dual-seed valutato; ogni
    verdetto senza falsificatore concordato = RESPINTO.
 8. LANDING inline (l'orchestratore, mai gli agenti): righe findings con
    `path:` (una per gap/flip/pilot), aggiornamenti ledger (status/note con
    catena d'autorità al file VERDICT), classi claims toccate,
    PROPOSTE di emendamento D6 datate DA RATIFICARE (mai edit silenziosi al
    piano), emendamenti proposti al protocollo TWIN, PROGRESS, lint verdi,
    roadmap rigenerata; verdetto GO / NO-GO / GO-CON-PILOT per F2.REPR e
    F2.ENGINE, scritto nell'ASSESSMENT di record.
 9. REFUTER DI CHIUSURA sull'assessment (delta-audit vs E1-E6), commit per
    pathspec, HANDOFF a F2.REPR (il cui carrier consuma l'assessment).

## D. VINCOLI
Env pinnato; GENO read-only; Fable ovunque; Workflow SOLO nelle fasi
derive/diff/converge/verify (opt-in utente di record: "con workflow a
convergenza"), landing sempre inline; artefatti su file SUBITO (ogni agente
scrive incrementalmente); resume-mai-relaunch; git add per pathspec, mai -A,
mai GENO/; SR-9 (shape+round+token nel log) e SR-12 (ogni numero misurato in
finestra); nessun "cammino completo" senza lint (xxiv) PASS; nessuna
riderivazione teorica; nessuna campagna numerica; il piano si emenda solo
per ratifica utente.

## E. CRITERI D'USCITA (misurabili)
 E1 ENUNCIATO AGNOSTICO su file con lint di agnosticità PASS (0 id di
    registro).
 E2 Tabella IPOTESI DI BASE per stadio della pipeline (dato -> contratto ->
    marcia -> certificati -> ottimizzatore -> strato ciclo -> Verdict ->
    claim): ogni ipotesi con classe, falsificatore, carrier o GAP nominato;
    gap = riga findings con `path:`.
 E3 Tabella COMPLETEZZA per stadio: costruito / dimostrato / misurato /
    mancante, oggi e nei prossimi passi; ogni "mancante" con owner.
 E4 Per OGNI sottoproblema di fondamento: verdetto CONFIRM (ragioni nuove) /
    FLIP prezzato / PILOT pre-registrato, con falsificatore concordato e
    verificatore indipendente; il livello 2 completo, il livello 3 secondo
    T2.
 E5 Censimento RABBIT HOLE: lista con confine dichiarato, frame alternativo
    per ostruzione, costo stimato; nessuna voce senza il "come cambia il
    TWIN".
 E6 Verdetto GO / NO-GO / GO-CON-PILOT per F2.REPR e F2.ENGINE nell'
    ASSESSMENT di record; emendamenti D6 proposti (non applicati) al
    touchpoint; red team del nord con esito; canary dual-seed riportato;
    consumo SR-9 riportato; suite plain verde; commit; PROGRESS NEXT = F2.REPR.

## F. LEVE ESPLICITE SUI VOTI (aggiunte su domanda utente 2026-09-05: "come alziamo e cosa")
Voti di partenza dati dall'orchestratore F2-B0 (revisore, non coautore):
organizzazione 7 rigore / 5 economia; codebase 8 verifica / 5 ingegneria /
4 copertura; orchestrazione 7. La revisione produce, oltre a E1-E6:
 F1 REGOLA DI CADENZA proposta all'utente come R9 (CLAUDE.md): mai due
    sessioni meta consecutive senza un incremento di costruzione;
    rapporto meta/build in F2 <= 1:2 misurato dal censimento.
 F2 PERIMETRO MINIMO DEL MOTORE (MVE) per il numero decisivo: elenco di cio'
    che serve STRETTAMENTE al TWIN (spina troncata, caso A) separato dalla
    generalita' differibile (3D, captured, torneo), ciascuna con owner e
    trigger — il GO di E6 e' un GO su questo perimetro.
 F3 ANCHOR PER ID: censimento misurato dei riferimenti a numero di riga
    (D6 :NNN, M0 :NNNN) nei registri/tool e piano di migrazione a id/ancore
    stabili con lint di risoluzione; piu' tools/progress_counts.py (i numeri
    di PROGRESS ORA generati da comando, mai battuti); time box igiene <= 20%.
 F4 STABILITA' DELLA CERTIFICAZIONE come requisito fondativo (sottoproblema
    obbligato dello Stage A): recorder stampato e pinnato in ogni Verdict,
    gate certificato-con-margine (TWIN A-1) implementato, test di
    riproducibilita' cross-versione su un set di design marginali con banda
    dichiarata; carrier di record che non riproducono = fail= posseduto.
 F5 PIANO D'INGEGNERIA PREZZATO (costo vs credibilita'/costo del TWIN):
    modularizzazione del driver monolitico (record/replay/driver/certificati),
    --help + protocollo in testa a ogni carrier, configurazione tipizzata al
    posto delle variabili d'ambiente, persistenza della solver-cache (34 min
    di ricompilazione misurati a F2-B0), CI del tier veloce (finding
    infra:scheduled-ci-multiplatform).
 F6 ORCHESTRAZIONE: giudice INDIPENDENTE nei panel di Stage B (persona
    fissa, diverso dall'orchestratore; tasso di disaccordo misurato);
    workflow versionati come artefatti nel repo (dryness counter,
    null-as-failure, dual-seed = assert di script); KPI token per correzione
    verificata (F2-B0: ~992k token / ~20 correzioni verificate); template di
    riga di censimento con owner per ogni item [KNOWLEDGE].
 Cio' che la revisione NON alza: copertura funzionale e velocita' in se' —
 le alzano le sessioni di costruzione che il GO deve sbloccare.

================================================================================
## G. ADDENDUM UTENTE (ordine in corso di sessione, 2026-09-05; append-only —
## registrato nel log R8 di validation/PROGRESS_2026-08-31_Sreview.md)

La vera domanda di ricerca è Q0: "COME si ottimizza l'ugello di un RDE" — non
solo Q1 "il disegno sulla famiglia del ciclo batte il disegno sulla media" (la
NOSTRA affilatura di Q0) né Q2 "il TWIN su spina troncata" (il NOSTRO esperimento
decisivo). La revisione deve giudicare se abbiamo preso la strada migliore,
quindi si aggiunge un LIVELLO 0 sopra il paradigma: LA STRADA.

 1. ENUNCIATO AGNOSTICO AL LIVELLO Q0. Il PROBLEM_STATEMENT deve porre Q0
    (obiettivo candidato: Isp/spinta media, robustezza sull'inviluppo,
    operabilità, costo; dati disponibili A-G; vincoli; requisito di
    certificazione; budget) e NON presupporre funzionale cycle-averaged,
    decomposizione per-fase, MoC, adjoint, TWIN: quelli sono INCUMBENT da
    confrontare, non premesse. Lint di agnosticità: zero id del repo E zero
    termini della nostra costituzione (cycle-averaged, per-fase, TWIN,
    quasi-stazionario) nell'enunciato.
 2. STAGE A esteso: i derivatori de-novo producono anche l'albero delle STRADE
    per Q0 — almeno: (a) disegno sulla media + verifica transitoria (la
    letteratura RDE oggi); (b) funzionale cycle-averaged con decomposizione
    per-fase (noi); (c) ottimizzazione unsteady diretta con adjoint nel tempo;
    (d) ottimizzazione STAZIONARIA nel riferimento d'onda (campo elicoidale 3D,
    B-lite/route-B: la dinamica azimutale entra esatta, niente St); (e)
    ROM/space-time o surrogati data-driven + ottimizzazione globale; (f)
    ottimizzazione robusta sull'inviluppo (casi D-F) se la leva vera non è
    ciclo-vs-media ma operabilità; (g) leve fisiche alternative (base
    pressure, troncamento, dual-bell temporale) come oggetto primario; (h)
    ibridi — es. PROGETTARE per-fase ed EVALUARE entrambi i bracci nel
    riferimento d'onda (il delta libero da St al livello della valutazione; il
    residuo per-fase tocca solo l'argmax = oggetto [T-RED]/OPTSHIFT/M-RED).
    Per ogni strada: che domanda risponde davvero, costo alla risposta
    credibile, generalità (settori, classi di dato), falsificabilità, tempo al
    numero.
 3. DIFF vs la nostra strada (record: M0 Parte I-II assiomi; VI.4bis(ii)
    correttore O(St); blocco [S-BLITE]; D6 G3 :783 "St·|J1| grande" = soglia
    mai derivata; [T-DISC]/[T-RED] con δ e L_H underived → M-RED; C51/ROUTE-B;
    U3' premessa aperta; protocollo TWIN §4). Giudizio esplicito su tre punti:
    Q1 è l'affilatura giusta di Q0? Q2 è l'esperimento che risponde a Q0 o
    solo a Q1? il rung della rappresentazione (per-fase / O(St) / wave-frame)
    va scelto separatamente per progettista ed evaluatore?
 4. STAGE B sulla STRADA come voce load-bearing di default (falsificatore
    concordato prima: "quale misura ci farebbe cambiare strada"), red team del
    nord esteso da Q2 a Q0.
 5. LANDING: righe choice-ledger di livello 0 PROPOSTE da ratificare (strada
    di ottimizzazione; definizione dell'obiettivo; esperimento decisivo; classe
    di dato del test decisivo), e il GO/NO-GO per F2.REPR/F2.ENGINE diventa
    CONDIZIONATO al verdetto sulla strada: GO se la nostra strada è CONFIRM o è
    la PILOT-arm di una strada ibrida; NO-GO/RIPIANIFICAZIONE se una strada
    alternativa domina su credibilità×costo con falsificatore concordato.

Vincoli invariati (UNA sessione, workflow nelle fasi derive/diff/converge/
verify, landing inline, niente riderivazione teorica né campagne, tetto T1).
Se il tempo stringe, la voce STRADA ha priorità su ogni altro sottoproblema di
Stage B.

================================================================================
## H. ADDENDUM UTENTE (ordine in corso di sessione, 2026-09-05; append-only —
## registrato nel log R8 di validation/PROGRESS_2026-08-31_Sreview.md)

H1 BRANCH LEDGER (copertura senza rabbit hole). L'albero delle strade/scelte
   NON si espande tutto: criterio di profondità = valore dell'informazione —
   si scende in un ramo solo se la sua risoluzione può CAMBIARE il GO/NO-GO o
   la strada. Ogni ramo visto va nel BRANCH LEDGER su file con stato ESPANSO /
   POTATO (ragione) / RINVIATO (trigger + owner): "non analizzato" non esiste,
   esiste solo "potato con ragione". Ampiezza completa ai livelli 0 e 1;
   profondità dove diff × peso lo giustifica.
H2 NUMERO DI SCOPING St (misurato dal record, non dichiarato — è
   un'aritmetica su dati di record, non una campagna): per la famiglia caso A
   (numero d'onde, D_CJ da Cantera, raggio dell'anulus, lunghezza dell'ugello,
   velocità assiale media) calcola St = f_onda·L/u con banda sull'inviluppo
   dei parametri di record; consuma il finding
   problem-statement:st-marginal-numbers-uncarried (path paper) dandogli un
   carrier committato con rejector; dichiara quale rung licenzia (per-fase /
   correttore O(St) / wave-frame) e usa il numero come input MISURATO della
   voce L0 STRADA e del red team del nord. Se St risulta O(1), la strada
   per-fase da sola non è difendibile e la voce L0 lo deve dire.
H3 PRIOR SOTA DEI CAMPI ADIACENTI, solo nella fase DIFF (mai nell'enunciato
   agnostico né ai derivatori): il giudice-diff verifica che l'albero de-novo
   abbia considerato la pratica SOTA dei flussi periodicamente non stazionari
   (turbomacchine: riferimento rotante stazionario; metodi in frequenza
   harmonic-balance / time-spectral con adjoint) e dell'ottimizzazione di
   forma adjoint-based stazionaria; ogni item di questo tipo entra come
   [KNOWLEDGE] → riga di censimento letteratura con owner di procurement
   (protocollo litreview), MAI come evidenza; il lint di agnosticità resta su
   enunciato e output dei derivatori.
