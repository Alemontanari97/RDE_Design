# S-PRES — STORYBOARD (Blocco 1(b)) — PER APPROVAZIONE UTENTE (gate addendum-4 (2))

Deliverable finale = ppt_Heister ESTESO via pipeline project_build:
esposizione completa delle attività RDE del gruppo + sezione
nozzle-program innestata al graft point (S18, censimento di record).
Target: panel propulsione ESA, 60', NULLA di scontato su RDE/
detonazioni (iniezione utente 2026-08-22). Ogni slide-claim nuovo =
cite-only dal record alla sua classe; guardie D-44/P34/CT-6/
best-of-sweep/query-bounded attive; two-stage claim a SCHEMA
DICHIARATO (decisione utente :1450).

Formato riga: N. [origine] Titolo — MESSAGGIO (una idea) — FIGURA.
[H n] = Heister slide n migliorata in forma; [NEW] = slide nuova;
[CVA n] = figura/materiale riusato dal deck CVA (già in pipeline).

===========================================================================
## PARTE A — APERTURA + IL GRUPPO (Heister migliorato) — 22' 

A1. [H 1] Rotating Detonation Engine Activities — T(H)RUST — chi
    siamo (Montanari, Grossi, Falco, Nasuti; Sapienza) — banner
    esistente. [fix: master default + contatori]
A2. [NEW] BLUF — In one slide: il gruppo copre l'intero motore
    (camera/iniettori/turbine/ugello) con un framework CFD
    ibrido-dimensionale validato; sul TEMA UGELLI abbiamo il primo
    metodo di design variazionale per-fase con onestà quantificata;
    oggi: stato + 3 richieste (ASK preview). — Mini-mappa del talk
    (5 blocchi con minuti).
A3. [H 2] Research Roads — la mappa delle attività (5 card,
    invariate nel contenuto; refuso Bellenoue corretto; la card
    "nozzle design" riceve il puntatore "→ sezione dedicata") — le
    card esistenti ripulite.
A4. [NEW, primer 1] What a detonation buys you — deflagrazione vs
    detonazione: la combustione a volume-quasi-costante comprime DA
    SÉ; pressure-gain = il premio termodinamico (Humphrey/FJ vs
    Brayton a π_c fissato). — [CVA 27] piano p-v con i 3 cicli +
    [CVA 3] bar chart U_CJ (figure di casa, già in pipeline).
A5. [NEW, primer 2] The Rotating Detonation Engine — annulus, fronte
    a ~U_CJ (kHz), refill continuo, esausto assiale: la detonazione
    resa STAZIONARIA nel frame rotante. — [CVA 38] diagramma annulus
    di casa + [CVA 39/SK Fig.1] fixture srotolata (attribuita).
A6. [NEW, primer 3] Why averages are treacherous here — EAP: la
    pressione totale equivalente; le medie ingenue di p_t sbagliano
    (K&P caution di record); il flusso è periodico, non steady —
    tenere a mente per la sezione ugelli. — [CVA 36/image48 K&P CFD
    contours, attribuita] + strip EAP.
    [NOTA CLASSE: primer = materiale standard/di-letteratura già
    validato nel deck CVA del gruppo, attribuzioni per-figura; zero
    claim nuovi]
A7. [H 3] HYPERDE architecture — un solo framework, dimensionalità
    per componente (3D camera ↔ quasi-1D iniettori ↔ 3D URANS
    expansion) — schema esistente. [forma: alleggerire testo 100→
    ~60 parole, gerarchia bullet]
A8. [H 4] Solvers' suite — capabilities (FV II ordine, thermo
    tabulata, OpenMP+MPI) — invariata, testo asciugato.
A9. [H 5] Q2D innovation w.r.t. literature — BC BFS non-isentropica
    + z(x,y) generale [Fievisohn & Yu cit.] — figure esistenti.
A10. [H 6] V&V: ZND — CFD vs ZND sovrapposti (SDT) — 2 plot
     esistenti.
A11. [H 7] V&V: literature unwrapped (Schwer & Kailasanath) — plot
     esistenti.
A12. [H 8-9, FUSE di forma] V&V: HYPERDE features + injector
     coupling — i 2 set di plot affiancati (AR sweep + profili
     accoppiamento); nessun contenuto rimosso, solo composizione.
     [Se la fusione compromette leggibilità → restano 2 slide e si
     recupera 1' altrove: decisione all'authoring, dichiarata]
A13. [H 10] V&V: Q2D→3D + VIDEO (26 s) — il video resta (forte in
     sala) — esistente.
A14. [H 11] Refill region dynamics (RMIT/NCSU) — le 4 domande + il
     dato controintuitivo (inlet divergenti degradano) — figure
     esistenti. [fix: text-box off-canvas recuperato o eliminato]
A15. [H 12] Refill: Λ sweep — perdite crescono con Λ; a Λ=2.9 inlet
     interamente supersonica, PG negativo — 4 pannelli esistenti.
     [fix: heading PNG duplicato → nativo]
A16. [H 13] Refill: il modello subsonic/supersonic — la figura di
     sintesi del gruppo — esistente.
A17. [H 14] Bladeless turbines + NCSU tunnel — hardware reale (foto)
     — esistente.
A18. [H 15] Tunnel validation — isentropico vs exp vs CFD — pannelli
     MATLAB esistenti.
A19. [H 16] Bladeless ongoing + VIDEO (14 s) — shape optimization
     matrix — esistente.
A20. [H 17] Disk RDEs (RMIT/ISAE-ENSMA/PPRIME) — 3D URANS vs Q2D —
     esistente.

## PARTE B — IL PONTE (2')

B1. [H 18, arricchita SOLO in forma] Nozzle Design for RDEs — il MoC
    in-house (2D/2D-axi non-isentropico three-waves), famiglie
    ideal/Rao/Veen implementate, e LA open question del gruppo:
    "Does an 'optimal' profile exist for an RDE exhaust?" [refs
    Harroun 2021, Stechmann 2019] — mesh 3D esistente. CHIUSA dal
    ponte narrativo (nuovo kicker): il pressure-gain guadagnato in
    camera si può PERDERE all'ugello — il campo pubblica leve da
    +4-7% Isp col choking [CT-1, numeri loro] e migrazioni da ~13
    punti di ideale a pari area ratio [shroud Paxson-Miki
    58.1→71.5, ADV] → la sezione che segue è la risposta del
    gruppo. [CRITIC riga 2: il composito "4-13 punti" non
    aggiudicato è RIMOSSO; restano i due estremi coi loro anchor
    separati, CT-6]

===========================================================================
## PARTE C — LA SEZIONE NOZZLE-PROGRAM (innesto, NUOVA) — 30'

### C-I. L'efflusso reale e la pratica del campo (10' — 7 slide
###      dopo le modifiche del gate: +C3-bis, C4 ristrutturata)

C1. [NEW] What an RDE exhaust actually looks like — LA DICOTOMIA:
    istante = shock obliquo rotante/elica, media = plume assialsim.
    pulita; 4 codici indipendenti, stessa fenomenologia. — CROP
    P-C Fig. 10 (left/right side-by-side, il più pulito) + P-D
    Fig. 9 vs 4 (thumbnails). [ADV, CT-6: figure loro, attribuite]
C2. [NEW] The throat is not steady either — KP18: sonic line
    corrugata, M=1 attraversata DUE volte per ciclo; Tab. 1 = le
    uniche statistiche p0/T0/Mx di gola pubblicate. — CROP KP18
    Fig. 6 + Tab. 1. [+ nota: il nostro pin di classe-dati è
    ESIBITO nei CFD (P-C phase-locked) ma MAI verificato
    spettralmente da alcun CFD pubblicato — search-proven, gap G1]
C3. [NEW] How the field designs RDE nozzles today — i 4 metodi
    pubblicati, ciascuno col SUO plot: Angelino ramp su medie (P-A,
    Liu 2022); MoC+max-thrust Rao/Veen su medie (P-B, Li-Xu 2023);
    conico non ottimizzato (P-D, Jourdaine); redesign manuale
    CFD-guidato (Paxson-Miki 2022). — 4 crop (P-A contour/profilo,
    P-B Fig. profilo MoC, P-D setup, P-M contour) in griglia 2x2
    con metodo+anno. [CT-6]
    TAKEAWAY: nessun optimizer sul 3D vero in NESSUNO dei 4
    (best-of-sweep ≠ argmax, guard di record).
C3-bis. [NEW — user objection 1, gate 2026-08-22] The optimization
    that has never happened — tabella per-paper "chi ottimizza
    cosa": P-A trade study 4 casi, NO optimizer [REP]; P-B applica
    le superfici max-thrust CLASSICHE steady (Rao/Vander-Veen) a
    input MEDIATI — ottimizza il problema SOSTITUTO, non l'RDE;
    P-C nessun design nuovo; P-D conico DICHIARATAMENTE non
    ottimizzato [F-19]; Paxson-Miki = redesign MANUALE CFD-guidato;
    nearest neighbors di letteratura: Kraiko-Egoryan 2020 = BOUND
    ideale (non design), Levin et al. 2010 = PDE per direct search
    (no condizioni di ottimalità). CLAIM CENTRALE (query-bounded):
    "nessun lavoro pubblicato, sotto le nostre query emendate, PONE
    il problema di ottimo sull'efflusso RDE reale — né 3D-unsteady
    né per-fase; dove l'ottimizzazione appare, è quella del problema
    steady sostituto, e l'errore della sostituzione non è mai stato
    quantificato" [C1/C2/C3 NOT-FOUND(q) litmap + C-5 synthesis +
    ORCH-HARV-1]. — Tabella 6 righe, un glifo per metodo.
C4. [NEW — user objection 2, RISTRUTTURATA] Same hardware, two
    flowfields — and the optimum moves — LA CATENA ESPLICITA in 3
    atti sui LORO dati (paired runs Li-Xu, stesso solver): (1) IL
    CAMPO È DIVERSO: steady-da-BC-medie vs transient — P-B Fig. 16
    (p0/T0 feedback con la troncatura), P-C Fig. 10 (shock interno
    one-sided vs twin assialsimmetrico); (2) LA DIFFERENZA ARRIVA
    ALL'OTTIMO: P-B Fig. 15 — curva steady FLAT (0.965-0.971) dove
    il transient ha un OTTIMO al 40% (+0.52%) e un cliff a 80%
    (−5.78%): l'ottimo vero è INVISIBILE alla curva su cui il campo
    disegna; P-C Fig. 13 — ranking flip a metà classifica (gap
    0.2-1.5%, both signs); (3) E NESSUNO LO PREZZA: l'errore
    sull'ARGMAX della sostituzione medie→vero non ha barra in
    letteratura [CT-2; R26 OPEN]. — CROP P-B Fig. 15 (il crop
    chiave) + P-C Fig. 13 + thumbnail Fig. 16. [ADV; il loro steady
    companion è GLOBAL-averaged: più crudo del nostro per-fase —
    detto in nota onestà]
C5. [NEW] Third warning, design-level: the closure moves the argmax
    — Humphreys 1971: cambiare SOLO il modello di p_b muove l'ottimo
    ×2.45 col valore piatto (+0.26%) — l'argmax è FRAGILE dove il
    valore è piatto, ESATTAMENTE il regime dei plot P-B/P-C; e la
    chiusura p_b che il campo usa ancora (Veen Eq. 9 = Humphreys
    Eq. 5.1) è GIUDICATA FAILED da WG10. — CROP Humphreys
    pp. 1586-87 (contour + tabella). [REP, pagine verificate]
C6. [NEW] The genealogy we inherit — Rao 1958 (calcolo variazionale,
    superficie di controllo = caratteristica come RISULTATO) →
    Hoffman 1967 (multiplier FIELDS = adjoint ante litteram) →
    Allman-Hoffman 1981 (diretto) → Kraiko-Tillyaeva (adjoint di
    campo + gradiente di forma; inflow nonuniforme/vorticoso 1994/
    2002) → NOI (per-fase + discreto-esatto + certificati). — Schema
    timeline di casa (pipeline-generated) con 1 crop RAO.pdf Eq. 14
    p. 379 (la transversalità).
    [query-bounded: "nessuna contouring classica family-averaged
    trovata sotto le nostre query (C1/C2/C3 NOT-FOUND(q))"]

### C-II. Il problema e il nostro framework (9')

C7. [NEW] The field's own conclusion — VERBATIM (P-C p. 11, concl.
    (3) p. 16): "the maximum thrust theory... proposed by Veen et
    al. is approximately applicable to the RDE nozzle under the
    premise that the propagation frequency... kHz" — SENZA barra
    d'errore: la conclusione del campo, DOPO la catena C3-bis/C4/C5
    appena mostrata (nessuno pone il problema vero; il campo si
    muove; l'argmax è fragile). La nostra tesi: "approximately" è
    un AVVERBIO DA QUANTIFICARE. Level-1 (sizing ~1%, [REP]) vs
    Level-2 (ranking a frazioni di punto: OPEN, R26). — La quote
    grande + schema two-level.
C7-bis-pre. [NEW — user catch 2026-08-23, GENEALOGIA PER-FASE
    DICHIARATA] The per-phase idea has ancestors — and we say so —
    la struttura "valuta ogni fase, somma le spinte" HA precedenti
    e il deck li dichiara PRIMA che li sollevi il panel (Stechmann
    e Harroun = gruppo Heister, il nostro deck-ospite!): Stechmann
    2019 = blowdown per-fase 0-D, C_F a ogni PR istantaneo, Isp
    mass-weighted — ma su FAMIGLIE FISSE (bell vs aerospike, sweep
    su eps), nessun ottimo variazionale del contorno; Harroun 2021
    = 2D-axi ai vari PR del profilo RDE, poi media dei c_F —
    quasi-cycle-averaged, e la media di un RAPPORTO non commuta
    (⟨F/p⟩ ≠ ⟨F⟩/⟨p⟩, bias O(Var) su cicli 10:1: quale peso e
    quale denominatore = domanda che noi poniamo formalmente,
    verifica-fonte assegnata); NOI = il problema di OTTIMO
    variazionale sulla famiglia (condizioni mediate, shared wall,
    (**')): MAI posto prima (C2 NOT-FOUND(q)). Il nostro rung-1
    quasi-1D È il livello Stechmann — con la media giusta
    DIMOSTRATA (T1c). — Timeline a 3 card: valutazione 0-D →
    valutazione 2D-axi → ottimo variazionale di famiglia. [Q&A:
    domanda attesa dal fronte Purdue/Heister, risposta pre-cotta]
C7-bis. [NEW — user gate 2026-08-22, LA SLIDE-CUORE] Two different
    optimization problems — fianco a fianco, matematica come
    struttura: SINISTRA (il campo, P-B incluso): mediare PRIMA —
    collassare il ciclo in UN campo medio s-bar, poi applicare a
    quel campo le condizioni di ottimalità STEADY di Rao/Veen
    (1958-1974): si risolve argmax J_steady(x; s-bar) — l'ottimo
    del problema SOSTITUTO, e l'errore argmax(sostituto) vs
    argmax(vero) non ha barra. DESTRA (noi): formulare il problema
    di ottimo DEL SISTEMA PERIODICO — il funzionale ciclo-mediato
    J_avg(x) = media_xi J(x; s(xi)) sulla FAMIGLIA per-fase (il
    quoziente tiene le fasi separate: niente collasso), e derivarne
    LE SUE condizioni di ottimalità (transversalità/corner MEDIATE
    — la struttura che il sistema averaged eredita con (**') al
    posto del corner single-phase, D3 §4): condizioni MAI SCRITTE
    dal campo (litmap C2 NOT-FOUND(q): "averaged Rao-type
    wall/corner conditions — zero hits"). argmax J_steady(s-bar) ≠
    argmax J_avg: la differenza non è pedanteria — è Gap B,
    misurabile in-house, e la distanza dal 3D vero è Gap A,
    bounded. — Schema a 2 colonne con le 2 catene (mediate→design
    vs famiglia→funzionale medio→ottimalità media), 2 strip-eq.
C7-ter. [RISCRITTA dopo il gate 2026-08-23 — la v1 confondeva il
    confronto intra-averaging col confronto inter-formulazione,
    obiezione utente SOSTENUTA] Where the difference is a THEOREM —
    and where it is not — la mappa ONESTA della biforcazione
    rung-1 (design single-phase/mean-state, ladder I4) vs rung-2
    (il nostro funzionale mediato, PB-1), tre righe:
    (1) RUNG QUASI-1D SENZA CONTOURING (l'oracolo eseguibile della
    catena: la parete non è variabile, conta solo l'area ε — NON è
    un ugello alla Rao, che è 2-DOF {ε,L} + contorno variazionale):
    qui, e solo qui, i due problemi COINCIDONO per costruzione
    [T-T7RED THEOREM] — e persino qui la media SBAGLIATA sposta
    l'ottimo (T1c) [precisazione utente 2026-08-23: mai presentare
    questo rung come "caso 1-DOF di ugello ottimo"];
    (2) plug PIENO ideal-adapted: coincidono ancora — gli argmax
    per-fase sono half-line annidate, il design PEAK-phase è
    ottimo [T-T4 THEOREM*, nesting];
    (3) plug TRONCATO / length caps (= LA configurazione del
    programma, default troncamento 0.20 di record): IL NESTING SI
    ROMPE [T-T4 THEOREM*] e si apre PB-2 — locked formulation
    D-06, "the first genuinely averaged and NON-COLLAPSING shape
    problem ... a CYCLE instance" (never abbreviate; near-miss
    query-bound: Efremov-Kraiko 2004); la STRICTNESS del gap
    (max Int < Int max) è clausola enunciata il cui carrier è il
    computo PB-2, OPEN. Il rompersi del nesting è teorema;
    l'entità del gap è il computo che manca. [CRITIC riga 10:
    riconciliata alla forma CH1]
    L'ENTITÀ al contouring: APERTA — e i meccanismi di record NON
    la dicono piccola: Jensen O(Var) senza parametro piccolo sul
    mean-state (C54); fluttuazioni per-fase di pressione da 10:1
    IMPOSTE nei BC pubblicati (Harroun Eq.7: 30→~2-6 atm, atlas
    H21-F11; Liu Fig. 6b sawtooth ~40→5-8 atm) e spread misurati
    ~6:1 in p_t di gola (KP18) [ancore CRITIC riga 16];
    panel swirl "single-digit % plausible ON-RAY, >10% NOT
    excluded OFF-RAY" (C-T1 OPEN) e "error could be large: not
    refutable by theory today"; strutturale-e-stretta sul plug
    troncato (PB-2). Il computo PB-2 (cycle-optimal truncated plug
    vs peak- e mean-designed baselines) è IL deliverable
    dichiarato — stato onesto sul deck: non ancora eseguito /
    prima campagna F2 / macchina pronta [oppure: numero del twin
    pre-milestone se l'utente lo ordina — decisione aperta al
    gate]. NESSUNA attesa di "piccolezza" è di record: dire
    "cambia poco" sarebbe un claim senza carrier (errore
    orchestratore corretto al gate 2026-08-23).
    — Figura: schema a 3 pannelli della biforcazione (coincide /
    coincide / SI ROMPE) con la configurazione nostra evidenziata
    nel terzo. [Inserto meccanismo, RIQUALIFICATO al suo rango:
    al DOF piu' semplice, sbagliare la media sposta eps* del
    +44-87% e costa 3-10 s Isp (T1c, carrier suite, misure
    2026-08-22) e lo shift dell'argmax e' primo ordine dove la
    penalita' di valore e' secondo ordine (G5/G6) — il pattern
    'argmax mobile a valore piatto' di Humphreys e P-B; inserto
    [P34: VERIFICATO], mai presentato come la prova del confronto
    di formulazione.]
C8. [NEW] Why the per-phase family is the right object — dentro la
    classe dati "onda rotante periodica pura" (pin dichiarato,
    monitor T0-flatness), il flusso è STEADY nel frame rotante: la
    famiglia per-fase non è un'approssimazione, è un QUOZIENTE —
    classe SCHEMA DICHIARATA (route di prova nominata, write-up S1
    in F2); e la media temporale GLOBALE (quella del campo) mescola
    le fasi — è la riduzione più crudele, non la nostra. —
    Diagramma: annulus → frame rotante → famiglia per-fase vs
    collasso globale. [two-stage claim a SCHEMA, decisione utente]
C8-bis. [NEW — user question 2026-08-23] The design space:
    configurations are OUTPUTS, not inputs — la formulazione è
    CONFIGURATION-FREE (problem book §5): la variabile di design è
    l'insieme SOLIDO S dentro un envelope, con attacco al lip e
    condizione di cono uniforme; bell / plug (aerospike troncato,
    p_b dichiarata) / shrouded plug (Veen: F_shroud + F_plug +
    F_kernel) / expansion-deflection / clustered sono le CLASSI
    TOPOLOGICHE di S — emergono, non si presuppongono. Il cono
    uniforme vieta i degeneri → A_gen si spezza in FINITI settori
    topologici [SCHEMA, pin utente 2026-08-02: cono/Chenais,
    Λ=cerchi]; esistenza per-settore (Chenais + S1, [T-P7S1]
    THEOREM* per level set certificati); OTTIMO GLOBALE = vincitore
    di un TORNEO FINITO tra gli ottimi di settore (cross-sector
    licenziato dal geometry-free bound). CAUTELA di record: niente
    topological derivative (un corpo infinitesimo in supersonico =
    solo wave drag: il center body paga a taglia finita — si
    confrontano settori INTERI). E il primo verdetto di torneo
    ESISTE già al rung ridotto: plug weakly dominates bell
    pointwise sotto chiusura sonic-capped, tie region
    caratterizzata, premium_bound certificato per cella [THEOREM,
    carrier X-GRP10/12]. Flag problems: PB-2 = plug troncato
    (primo ottimo genuinamente mediato), PB-3 = shrouded duty
    split. — Figura: envelope + i 4 settori come output con lo
    stato di ciascuno (torneo rung-ridotto deciso / PB-2 flag /
    PB-3 coda / E-D in A_gen). [Nota onesta on-slide: il driver
    discreto oggi esercita il contouring a parete singola; plug
    troncato e shrouded = le campagne nominate F2+]
C9. [NEW] What the average can and cannot see — [T-DISC] (classe
    THEOREM*): stessa traccia di pressione, contenuti swirl/
    fluttuazione diversi → spinte diverse: la riduzione p-only è
    CONVICTED (fibre non degeneri, zero CFD); la media full-state
    per-fase è ESONERATA sull'asse-fibra. — Schema fibra (P-trace
    fissata, famiglia s_lambda) di casa.
C10. [NEW] What the reduction drops — [T-RED]: i termini azimutali
     scartati = OPERATORE-RESIDUO esplicito; K-bar = 0 (THEOREM*,
     il canale medio muore); il resto va in canali (J)/(H) con
     deriver nominati. Il residuo non è "trascurabile": è MISURABILE
     (M-RED, F2). — Schema operatore + P-C Fig. 21 crop (forza
     laterale rotante ~25-35% istantanea, media ~0: la faccia
     pubblicata di K-bar=0). [ADV]
C11. [NEW] The honesty table — [R22F-FORCHETTA]: 6 canali, cella
     BEST/WORST, classe di rigore per cella, provenienza per numero,
     "what tightens it" in ordine di programma. NESSUNA cella sopra
     la sua classe; delta e L_H UNDERIVED dichiarati. — La tabella
     resa a colori (SE/THEOREM*/REP/ADV codificati), compressa ai
     highlights; versione integrale nel backup. [D-44: bracket, MAI
     adequacy]
C12. [NEW] The worst-direction marker — Paxson-Miki shroud: 58.1 →
     ~71.5% dell'ideale a AREA RATIO FISSATO (punti percentuali di
     ideale) — più grande dell'intera linea di design area-ratio,
     inspiegato dagli autori, registrato come swirl-breaker
     candidate. — CROP P-M figura shroud. [ADV; CT-6]

### C-III. La macchina e il grafo (8')
### [REGOLA DI SEZIONE, user 2026-08-23: NULLA di scontato sul
### METODO — adjoint, ottimizzatore, certificati, discreto-esatto
### spiegati alla prima occorrenza, ciascuno col PERCHE' della
### scelta (ancora = choice ledger)]

C13-pre. [NEW — user order 2026-08-23] Method primer in one slide —
     4 concetti in linguaggio da primo incontro: (1) ADJOINT =
     il campo moltiplicatore che, con UNA soluzione in piu', da'
     il gradiente di J rispetto a TUTTI i DOF insieme (e non e'
     un'idea moderna: sono i multiplier fields di Hoffman 1967
     lungo le stesse caratteristiche — aggancio alla genealogia
     C6); (2) DISCRETO-ESATTO = differenziamo ESATTAMENTE il
     problema che il computer risolve (AD), non una
     discretizzazione del gradiente continuo: zero gap tra schema
     e gradiente; (3) TR-NEWTON SEGMENTATO = ottimizzatore a
     curvatura MISURATA con trust region — scelto contro
     BFGS/IP-alternatives per robustezza certificabile
     (aggiudicazione C31 di record, alternative pesate sul
     ledger); (4) CERTIFICATO = condizione verificata a
     posteriori con soglia DERIVATA (mai magica), piu' oracoli
     indipendenti che possono RIGETTARE. — 4 card con
     micro-schema ciascuna.

C13. [NEW] From theory to a design machine — la pipeline end-to-end
     (contract → representation → march → certificates → estimator →
     optimizer → aggregation → verdict): 8 stadi, 62 scelte
     algoritmiche TIPIZZATE a registro — 48 aggiudicate a
     convergenza con alternative pesate + falsificatore, 2
     SINGLE-AUTHOR dichiarate (C17/C18, duty F2), 12 NEVER
     dichiarate con owner e trigger. — GRAFO L0 (overview ribbon,
     spec GRAPH_VIZ_SPEC.md): status mini-bar per stadio + 4
     superfici cluster. "12 DECIDED / 36 MIXED / 12 NEVER / 2 SA —
     il tally È la slide: dichiarati, mai nascosti." [CRITIC riga 3
     applicata: coerenza con CH4 W2-R2]
C14. [NEW] Zoom: the optimizer stage — TR-Newton segmentato a
     curvatura misurata su discreto-esatto (JAX, G0 di record);
     cluster F2-entry {C31/C57/C58/C60} DICHIARATO aperto — il
     grafo mostra anche ciò che NON abbiamo ancora deciso. — GRAFO
     L1 stadio 6 (2 pannelli).
C15. [NEW] Zoom: certificates & bands — certificati per segmento,
     oracoli indipendenti (91/91), DWR target + GCI referee; trasv.
     KKT 7.7e-2 di record. — GRAFO L1 stadio 4-5 (selezione).
     [P34: ogni numero con stage dichiarato]
C16. [NEW] Engine numbers (verified stage) — val_grad 0.449 s;
     segmento 14.9-20.1 s (target ≤30 MET); campagna 10-14 min
     (target ≤25 MET); 18× sul record; suite 23/23 EXIT 0. — Tabella
     compatta con [X-SPDB] + barre target-vs-measured.
     [stage: VERIFICATO (misure nostre, carrier committati)]

### C-IV. Roadmap e richieste (4')

C17. [NEW] What tightens the bracket, in order — la roadmap = i
     deriver della forchetta: M-RED (misura il residuo su famiglie
     certificate, F2, in-house cheap) → CFD-2 (paired-run Harroun
     pair, template P-C) → CFD-1 (il decider di classe, ~12M-cell).
     Gap A/Gap B: Gap B misurabile in-house (nostro vs Veen/
     Angelino-at-mean); Gap A bounded-only — NESSUNO può calcolare
     l'ottimo 3D vero, noi lo LIMITIAMO. Value condition esplicita.
     — Timeline F2→F5 con 3 gate colorati.
C18. [NEW] ASK — (1) CFD-1: collaborazione/procurement sul reference
     run di classe; (2) dati motore per la classe del pin (high-speed
     p/imaging hot-fire: T0-flatness + f_cycle); (3) canali paper
     (P-1 JPP) + i 3 procurement Tier-1 (Fotia/Goto/Ma). — 3 card.
C19. [NEW] Summary — il doppio takeaway finale: (ing.) primo metodo
     variazionale per-fase con residuo operatorizzato e bracket
     onesto; (progr.) macchina veloce + piano di validazione
     incrementale già prezzato. — 5 bullet + il grafo L0 in
     miniatura come firma. [chiude il deck]

===========================================================================
## PARTE D — BACKUP DECK (dalla mappa Q&A, Blocco 2(c))

D1-D8. GRAFO L1 degli 8 stadi completi (walkable graph promise).
D9+. Node cards L2 per i nodi Q&A-mapped (dalla banca-obiezioni
     refuter: assi tecnico/programmatico/TRL/costi).
D-F. FORCHETTA integrale (6 righe complete con celle verbatim).
D-N. Metodologia figure/riuso: manifest + audit (una slide di
     provenienza).
[Il backup si costruisce DALLA mappa Q&A al Blocco 2 — qui solo lo
skeleton.]

===========================================================================
## TIME-BOXING SUL 60' (aggiornato al deck intero)

| Blocco | Slide | min |
|---|---|---|
| A1-A3 apertura+BLUF+mappa | 3 | 4 |
| A4-A6 primer RDE | 3 | 6 |
| A7-A13 codice+V&V | 7 | 10 |
| A14-A20 linee di ricerca | 7 | 9 |
| B1 ponte | 1 | 2 |
| C1-C6 efflusso+campo (con C3-bis) | 7 | 10 |
| C7-C12 problema+framework | 6 | 9 |
| C13-C16 grafo+macchina | 4 | 7 |
| C17-C19 roadmap+ask+summary | 3 | 4 |
| TOTALE (main deck ~41 slide) | 41 | 61→60 (C13-C16 −1' + buffer video) |

CUT-LIST ordinata (si taglia in quest'ordine, pre-deciso):
1. A12 fusione già assorbita / A19 video (−1')
2. C15 zoom certificates (→ backup) (−2')
3. A4-A6 primer compresso a 2 slide (−2')
4. C2 throat (→ backup, resta 1 riga in C1) (−2')
5. A14-A20 linee compresse (−3')
CORE-15' (resilienza): A2 BLUF + B1 + C4 + C7 + C9/C11 (fusa) +
C16 + C18.

## PATTO DI STILE (verdetto STYLE_ADJUDICATION recepito: esito (b))

Aggiudicazione agnostica di record (STYLE_ADJUDICATION_cva_rde.md):
**(b) ADOTTA-CON-EMENDAMENTI, E1-E7.** Il deck finale EREDITA da
CVA_RDE: sistema-figure di casa (annotazioni interpretative
in-figure, plot serif matplotlib), strip-equazioni LaTeX 200 DPI,
disciplina di provenienza per-figura, identità cromatica
#822433/#006778 (già comune a Heister). EMENDA (vincolante
all'authoring): budget ≤60 parole nette/slide; corpo ≥18 pt (allineato
al corpo Heister); placeholder titolo reintrodotti (outline/
accessibilità); font policy esplicita; fix dei 2 difetti figura
(image76 legenda, image72 bordo) se riusate; chrome/contatori
rigenerati UNICI. L'architettura milestone (BLUF/ask/backup/
time-boxing) viene dal carrier S-PRES, NON da CVA (misurati 0 ask,
0 backup nel deck-lezione).

## MIGLIORIE DI FORMA HEISTER (dal censimento, tutte non-contenuto)

1. Footer: rimozione testo residuo "HEM modeling..." (S2-18).
2. Contatore pagina UNICO (fix "2/17" stantio; placeholder solo).
3. Master ripulito dai default "M. Fiore / Modular Aerospike
   Nozzles" (igiene per le slide nuove).
4. S12: heading PNG → testo nativo (con Λ via strip-eq pipeline).
5. S11: text-box off-canvas recuperato o rimosso (decisione
   all'authoring, dichiarata).
6. Refuso "Belleonue" → "Bellenoue" (S2).
7. Note relatore: aggiunte via add_notes.py per TUTTE le slide
   (canale di provenienza, come nel deck CVA).
8. 4 figure paper-style senza credito (image5/18/19/21) → marcate
   "Group/collaboration material" (RISPOSTA UTENTE al gate
   2026-08-22: sono materiale del gruppo/collaboratori — nessuna
   citazione esterna, nessun claim di paper altrui).
9. S2: card "open research lines" aggiornata col puntatore alla
   sezione nozzle estesa.
