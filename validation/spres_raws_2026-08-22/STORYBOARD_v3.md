# S-PRES — STORYBOARD v3.1 (slot STORYBOARD-V3, sessione 2, 2026-08-23)

**v3.1 = v3 + revisione di registro ordinata (correzione utente CKP-S2-3,
guardia 18)**: il deck parla la lingua dell'ingegneria della propulsione,
mai la lingua del nostro processo. Delta v3→v3.1 dichiarato in coda.

**REGISTRO CALIBRATO SU (prassi NOMINATE, clausola C-5 — mai "standard"
assoluto dove non codificato)**: (1) assertion-evidence (Alley, Penn
State — asse §C-6 conformity map): ogni slide = asserzione in frase
piena come titolo + evidenza visiva dominante, mai titoli-argomento né
muri di bullet; (2) principi Doumont (*Trees, Maps, and Theorems*): un
messaggio per slide, massimo rapporto segnale/rumore, ridondanza zero
schermo/parlato — il dettaglio vive nel parlato e nelle note relatore;
(3) convenzioni da technical review d'agenzia (classe ESA/NASA): BLUF
in apertura (A2), mappa del talk con minuti, ask DECISION-READY (C18),
stato onesto con owner (C17-bis), backup pronto al drill-down su ogni
claim, numeri on-slide solo se physical o decision-bearing. Questo è il
metro del comms review del Blocco 2.

**Stadio di confronto**: STORYBOARD.md (v1 committata, la spina che questa
v3 EVOLVE) vs i 10 blocchi `## DECK FEED` di CH1-CH10 (reconstruction/,
letti su disco in finestra) vs MESSAGE_ARCHITECTURE.md vs
WA_A3_storyboard_verify.md (2 borderline) vs graph_derisk/DERISK_report.md
vs LINEAGE_LEDGER.md (LL-1..LL-37 ADJUDICATED) vs SESSION_STATE_checkpoint
:84-97/:129-145 vs GUARD_CHECKLIST.md (18 guardie) vs SESSION2_LOG
CKP-S2-3.
**Arco di consumo**: gate utente storyboard → authoring Blocco 1 (deck) +
retro-audit Blocco 2. Il deck è CONSUMER dell'atlas (ordine utente): ogni
slide joina un feed CHx-n, una riga LL-id o una card — la tabella di join
in coda prova che NESSUN feed è perso in silenzio [F-des-4].

## CONVENZIONE DI REGISTRO (guardia 18 — vincola OGNI slide)

- Il campo **ASSERZIONE** e il campo **EVIDENZA** sono ON-SLIDE: lingua
  ingegneristica, zero contabilità interna (conteggi di
  copertura/suite/registri), zero gergo di processo (sigle di classe
  nude, "query-bounded", "stage P34", "guardia N", "feed", tally card).
  I concetti restano, detti da ingegneri: "verificato indipendentemente
  contro un secondo codice, con controlli negativi", "gradiente esatto
  del problema discreto, verificato a precisione macchina", "struttura
  di prova dichiarata, non ancora la prova completa — e ne indichiamo la
  strada", "il regime di validità di questa media non è mai stato
  prezzato in letteratura", "un ottimo dichiarato porta sempre il suo
  meccanismo e la sua forza".
- I numeri FISICI e i numeri DEI PAPER restano on-slide (10:1, 6:1,
  ×2.45, +4-7%, 58→71%, 3-10 s Isp, ~1% kill threshold, 0.2-1.5%
  ranking gap, +0.52%/−5.78%): sono ingegneria, non contabilità.
- Il campo **[NOTE]** di ogni slide = nota provenance: join
  feed/LL/card, classi di rigore, tag di guardia, conteggi di
  copertura. Vive nelle NOTE RELATORE (canale add_notes.py) e nel layer
  retro-audit del Blocco 2 — MAI sulla slide.
- La tabella di join in coda e i tag di guardia restano in QUESTO
  documento (sono il carrier del retro-audit), marcati [NOTE].
- VERIFICA PER-SLIDE contro il metro nominato in header: (Alley) il
  TITOLO all'authoring è l'ASSERZIONE stessa compressa in frase piena
  (se non regge da sola, la slide non è pronta), l'evidenza visiva
  domina; (Doumont) UN messaggio per slide — dove un'asserzione qui
  sotto elenca più mosse, sono progressioni della STESSA idea, e il
  dettaglio migra nel parlato/note; (agenzia) on-slide solo numeri
  physical o decision-bearing — il criterio già applicato sopra.

Formato riga slide:
`ID [atto] TITOLO — ASSERZIONE (on-slide) — EVIDENZA (on-slide) —
[NOTE] provenance — min — cut-pos`.
[H n] = Heister slide n migliorata in forma; [CVA n] = figura di casa dal
deck CVA; [NEW] = slide nuova. Le migliorie di forma Heister e il patto di
stile (esito (b) E1-E7) restano quelli di v1 §finali — invariati, non
ricopiati.

==========================================================================
## MAPPA DEI 7 ATTI (narrativa §N del design) SUL DECK

Il filo logico-ingegneristico di CKP-S2-3 È la spina: problema fisico →
perché la modellazione per-fase (il quoziente) → idea/vantaggio vs
letteratura → formalizzazione (condizioni di ottimalità mediate) → perché
l'adjoint e quale → quale ottimizzatore e perché → evidenza concreta che
la macchina funziona (validazione sul classico) → limiti onesti →
roadmap/ask.

| atto | contenuto | slide |
|---|---|---|
| 0 pre-atto istituzionale | il gruppo e il framework (Heister migliorato) | A1-A3, A7-A20 |
| 1 CONTESTO CAMPO (problema fisico) | fisica RDE da zero + efflusso reale + pratica del campo | A4-A6, C1-C3 |
| 2 GAP | l'ottimizzazione mai avvenuta; il campo si muove; argmax fragile; genealogia | C3-bis, C4, C5, C6 |
| 3 DOMANDA | "approximately" è un avverbio da quantificare | B1 (innesto), C7, C7-bis-pre |
| 4 METODO (modellazione+formalizzazione) | i due problemi; quoziente; design space; cosa vede/perde la media | C7-bis, C7-ter, C8, C8-bis, C9, C10 |
| 5 EVIDENZA (perché le scelte + la macchina) | perché adjoint/ottimizzatore, validazione sul classico, grafo scelte, numeri | C13-pre, C13-val, C13, C14, C15, C16 |
| 6 ONESTÀ/LIMITI | forchetta, worst-marker, l'audit che ci ha bocciato, quale gap domina | C11, C12, C16-bis, C17-pre, C17-bis |
| 7 ROADMAP+ASK | deriver in ordine, decisioni pendenti, ASK+Annex B, summary | C17, C18, C19 |

Il graft point resta **Heister S18 → B1** (censimento di record). Il primer
RDE resta nulla-dato-per-scontato (decisione utente :87-92); la sezione
C-III resta sotto la regola "nulla di scontato sul METODO" (C13-pre).

==========================================================================
## PARTE A — APERTURA + IL GRUPPO (Heister migliorato) — 25'

Invariata da v1 nelle slide A1-A20 (contenuti, fix di forma, attribuzioni
"Group/collaboration material" per image5/18/19/21 — risposta utente al
gate 2026-08-22). Delta v3/v3.1 sulle sole righe qui sotto:

A2. [NEW] BLUF — come v1 (il gruppo copre l'intero motore; sul tema ugelli
    il primo metodo di design variazionale per-fase con onestà
    quantificata; ASK preview) — mini-mappa del talk a 5 blocchi CON
    minuti. — [NOTE] join: MESSAGE_ARCHITECTURE §BLUF. — 2' — cut: MAI
    (core-15').
A6. [NEW, primer 3] Why averages are treacherous here — ASSERZIONE: le
    medie ingenue della pressione totale sbagliano in un flusso
    periodico (la cautela EAP è pubblicata dagli stessi autori del
    metodo); e alla media EAP manca tuttora una barra d'errore — il
    nostro programma la costruisce (correttore P4). — EVIDENZA:
    [CVA 36/image48 K&P CFD contours, attribuita] + strip EAP. —
    [NOTE] join: CH1-feed-5 + CH5-feed-7 (remark [IO] di record,
    M0:2526-2544); classi e completamento P4 in nota relatore. — 2' —
    cut-pos 3 (primer 3→2 slide).

Budget Parte A (aggiornato, misurato sulla lista): A1-A3 4' · A4-A6 6' ·
A7-A13 8' (fusione A12; V&V walk ~1'/slide + video 26s) · A14-A20 7'.

## PARTE B — IL PONTE (2')

B1. [H 18, arricchita solo in forma] Nozzle Design for RDEs — INVARIATA
    da v1: il MoC in-house, le famiglie implementate, la open question
    del gruppo; kicker con i due estremi separati coi loro anchor
    (+4-7% Isp col choking; 58.1→71.5% dell'ideale a pari area ratio,
    numeri dei rispettivi paper) — numeri FISICI: restano on-slide. —
    mesh 3D esistente. — [NOTE] WA_A3 riga critic 2
    DISPOSTA-VERIFICATA (composito "4-13" rimosso); CT-1/ADV/CT-6 in
    nota; join censimento graft S18. — 2' — cut: MAI (core-15').

==========================================================================
## PARTE C — SEZIONE NOZZLE-PROGRAM (innesto) — 33.5'

### C-I. L'efflusso reale e la pratica del campo (8.5')

C1. [atto 1] What an RDE exhaust actually looks like — ASSERZIONE: nello
    stesso ugello convivono due campi: l'istantaneo (shock obliquo
    rotante a elica) e il medio (plume assialsimmetrica pulita) — e
    quattro codici indipendenti mostrano la stessa fenomenologia. —
    EVIDENZA: CROP P-C Fig. 10 side-by-side + P-D Fig. 9 vs 4
    thumbnails, citazioni piene per figura. — [NOTE] v1 C1 [ADV, CT-6].
    — 1' — cut: no.
C2. [atto 1] The throat is not steady — and is not even "the throat" —
    ASSERZIONE: la sonic line di un RDE è corrugata e attraversa M=1 due
    volte per ciclo; le uniche statistiche di gola pubblicate mostrano
    escursioni ~6:1 in pressione totale; per questo l'interfaccia di
    design non è la gola geometrica ma la stazione supersonica-con-
    margine a valle del rilascio di calore; e nessuno dei quattro studi
    di riferimento dichiara la classe di dati su cui lavora — la
    periodicità è esibita nei CFD, mai verificata spettralmente in
    letteratura. — EVIDENZA: CROP KP18 Fig. 6 + Tab. 1 + micro-schema
    della stazione di interfaccia. — [NOTE] join: CH10-feed-3 (THEOREM
    T-TH0/T-NSW) + CH10-feed-4 ([IO], CT-6) + CH10-feed-6 e CH5-feed-5
    (search-proven, bounded al corpus); guardia 11; "search-proven" e
    classi SOLO in nota. — 1' — cut-pos 4 (→ backup, resta 1 riga in
    C1).
C3. [atto 1] How the field designs RDE nozzles today — ASSERZIONE: i
    quattro metodi pubblicati, ciascuno col suo plot: rampa di Angelino
    su medie (PKU), MoC con superfici max-thrust classiche su medie
    (NUAA), conico non ottimizzato (KIT-Aoyama), redesign manuale
    CFD-guidato (NASA-Glenn) — e il "migliore di uno sweep" non è un
    ottimo: nessuno dei quattro chiude il cerchio con un'ottimizzazione
    vera. — EVIDENZA: 4 crop in griglia 2×2 con metodo+anno, citazioni
    piene. — [NOTE] join: v1 C3 + CH8-feed-5 (regola best-of-sweep ≠
    argmax); guardie 4/8 in nota. — 1.5' — cut: no (mai sotto il
    plot-dichotomy).
C3-bis. [atto 2] The optimization that has never happened — ASSERZIONE:
    tabella per-paper "chi ottimizza cosa": trade study senza
    optimizer; superfici max-thrust CLASSICHE steady applicate a input
    mediati — si ottimizza il problema SOSTITUTO, non l'RDE (e va detto
    con precisione: quel lavoro USA il calcolo variazionale classico —
    ciò che manca è l'ottimizzazione del problema vero); nessun design
    nuovo; conico dichiaratamente non ottimizzato; redesign manuale. I
    lavori più vicini fuori dal quartetto: un bound ideale (non un
    design) e una ricerca diretta senza condizioni di ottimalità.
    CLAIM CENTRALE: per quanto un censimento sistematico della
    letteratura ci ha permesso di verificare, nessun lavoro pubblicato
    pone il problema di ottimo sull'efflusso RDE reale — né 3D-unsteady
    né per-fase; dove l'ottimizzazione appare, è quella del problema
    steady sostituto, e l'errore della sostituzione non è mai stato
    quantificato. — EVIDENZA: tabella 6 righe, un glifo per metodo. —
    [NOTE] join: CH5-feed-1 (FORMA VINCOLANTE WB1-C3-10 — mai "nessuno
    ottimizza" nudo; caveat ISABE [SE] in nota relatore, richiamabile a
    voce) + CH4-feed-8 ([ADV]+[REP], caveat P-B obbligatorio: assorbito
    nell'asserzione "usa il variazionale classico") + CH8-feed-6
    (nessun meccanismo di globalità dichiarato nei 4 — in nota);
    "NOT-FOUND(q)/query-bounded" SOLO in nota. — 1.5' — cut: no.
C4. [atto 2] Same hardware, two flowfields — and the optimum moves —
    ASSERZIONE (LA CATENA in 3 atti sui LORO dati, paired runs stesso
    solver): (1) il campo risolto è diverso — steady-da-BC-medie vs
    transient, e l'ugello retro-agisce sulla camera al variare della
    troncatura (il che vieta di assumere il disaccoppiamento senza
    verificare il choking); (2) la differenza arriva all'ottimo: la
    curva steady è PIATTA (0.965-0.971) dove il transient ha un ottimo
    al 40% di troncatura (+0.52%) e un cliff a 80% (−5.78%) — l'ottimo
    vero è INVISIBILE alla curva su cui il campo disegna; e il ranking
    tra geometrie si inverte a metà classifica con gap 0.2-1.5%; (3) e
    nessuno in letteratura prezza questo errore. — EVIDENZA: CROP P-B
    Fig. 15 (il crop chiave) + P-C Fig. 13 + thumb Fig. 16. —
    [NOTE] join: CH5-feed-2 ([ADV], CT-6) + CH5-feed-4 ([ADV-FIG],
    minaccia CT-1); guardia 17 (mai claim di decoupling senza choking
    citato) vincola anche la Q&A. — 2' — cut: MAI (core-15').
C5. [atto 2] Third warning: the closure moves the argmax — ASSERZIONE:
    già nel 1971 (Humphreys): cambiare SOLO il modello di pressione di
    base sposta l'ottimo di un fattore 2.45 mentre il valore resta
    quasi piatto (+0.26%) — l'argmax è fragile proprio dove il valore è
    piatto, esattamente il regime dei plot appena visti; e la chiusura
    che il campo RDE usa ancora oggi è la stessa, giudicata
    inaffidabile dal working group che l'ha rivalutata; per questo il
    nostro contratto di design chiede l'unimodalità della variabile di
    lavoro del plug troncato, non la piattezza. — EVIDENZA: CROP
    Humphreys pp. 1586-87 (contour + tabella). — [NOTE] join:
    CH5-feed-8 ([REP] fonte primaria, WG10-FAILED) + CH8-feed-7
    (target M3; CT-6). — 1' — cut: no.
C6. [atto 2] The genealogy we inherit — ASSERZIONE: il design
    variazionale di ugelli ha 70 anni di storia — Rao 1958 (la
    superficie di controllo emerge come risultato), Hoffman 1967 (i
    campi moltiplicatori: l'adjoint ante litteram), Allman-Hoffman 1981
    (la via diretta), la scuola Kraiko-Tillyaeva (adjoint di campo e
    gradiente di forma, inflow non uniforme e vorticoso) — e un
    antenato che citiamo sempre: Kraiko-Osipov 1970, la parete pesata
    nel tempo, cui mancano la misura di ciclo, il quoziente e i
    certificati; noi estendiamo questa linea al sistema periodico. Un
    precedente russo del 1975 non è ancora nelle nostre mani: lo
    diciamo, e non lo riassumiamo. — EVIDENZA: timeline di casa +
    crop RAO.pdf Eq. 14 p. 379 (la transversalità). — [NOTE] join:
    CH2-feed-6 (LL-1, citazione obbligatoria) + CH5-feed-6 +
    CH7-feed-6 (Tillyaeva 1975 PENDING-PROCUREMENT, forma onesta);
    lineage LL-1/7/14/27 [guardia 10]; "query-bounded" in nota. —
    1.5' — cut: no.

### C-II. Il problema e il nostro framework (10.5')

C7. [atto 3] The field's own conclusion — ASSERZIONE: VERBATIM P-C:
    "the maximum thrust theory... is approximately applicable..." —
    SENZA barra d'errore; e in tutta la letteratura del settore il
    regime di validità della media usata per il design non è mai stato
    prezzato. La nostra tesi: "approximately" è un avverbio da
    QUANTIFICARE — al livello del sizing l'errore è ~1%; al livello del
    ranking tra geometrie (frazioni di punto) la domanda è APERTA, e
    nessuno oggi sa rispondere. — EVIDENZA: la quote grande + schema
    two-level (sizing vs ranking). — [NOTE] join: CH1-feed-7
    (NOT-FOUND(q); K-O footnote unpriced) + carrier :178-180; Level-1
    [REP] / Level-2 OPEN R26 in nota. — 1.5' — cut: MAI (core-15').
C7-bis-pre. [atto 3] The per-phase idea has ancestors — and we say so —
    ASSERZIONE: l'idea "valuta ogni fase del ciclo, poi componi le
    spinte" ha antenati, e li dichiariamo noi per primi (vengono dal
    gruppo di questo stesso deck-ospite): Stechmann 2019 — blowdown
    0-D per fase, media pesata in massa dichiarata, ma su famiglie di
    ugelli FISSE; Harroun 2021 — 2D assialsimmetrico ai vari rapporti
    di pressione del ciclo, poi media dei coefficienti di spinta — ma
    la media di un RAPPORTO non commuta (⟨F/p⟩ ≠ ⟨F⟩/⟨p⟩: su cicli
    10:1 il bias è del primo ordine nella varianza, e il paper non
    dichiara quale peso usa); Fievisohn — il cugino più vicino
    (MoC rotazionale nel frame d'onda): mai design, mai famiglia
    per-fase — il quoziente esiste nel campo, l'edificio no. NOI
    poniamo l'ottimo variazionale SULLA FAMIGLIA — mai posto prima; e
    il nostro gradino di riduzione più semplice è il livello di
    RIDUZIONE di Stechmann (0-D per fase) — non una valutazione di
    famiglie d'ugello — con la media giusta DIMOSTRATA. — EVIDENZA:
    timeline a 4 card (0-D → 2D-axi → wave-frame MoC → ottimo
    variazionale di famiglia). — [NOTE] join: checkpoint C-1
    (:131-145); lineage LL-2/LL-3/LL-13 [guardia 10]; CH7-feed-7;
    fix borderline WA_A3 guardia 3 incorporato; T1c in nota. — 1.5' —
    cut: no (risposta pre-cotta fronte Purdue/Heister).
C7-bis. [atto 4, LA SLIDE-CUORE] Two different optimization problems —
    ASSERZIONE: SINISTRA (il campo): collassare il ciclo in UN campo
    medio e applicargli le condizioni di ottimo steady classiche →
    si risolve l'ottimo di un problema SOSTITUTO, e l'errore
    sull'argmax non ha barra. DESTRA (noi): formulare l'ottimo DEL
    SISTEMA PERIODICO — il funzionale ciclo-mediato sulla famiglia
    per-fase (le fasi restano separate: niente collasso) e derivarne
    LE SUE condizioni di ottimalità — transversalità e corner mediati:
    condizioni mai scritte in letteratura. E il teorema che decide la
    destra: NESSUNA fase soddisfa la propria condizione di parete — la
    media pesata sì: l'ugello ottimo di ciclo non è l'ugello ottimo di
    nessun punto operativo; dei tre modi naturali di mediare, uno solo
    è condizione necessaria del problema vero — la media PESATA delle
    condizioni; le altre due falliscono fuori da un caso degenere
    identificato. — EVIDENZA: schema a 2 colonne con le 2 catene +
    2 strip-eq. — [NOTE] join: CH1-feed-1 (I4 vs I2/I3) + CH2-feed-1
    (THEOREM* T-T7FS(b)) + CH1-feed-4 (boxed warning) + CH2-feed-2
    (THEOREM* [T-T3], classe di collasso T3); "zero hits/NOT-FOUND"
    in nota. — 2' — cut: MAI (core-15').
C7-ter. [atto 4] Where the difference is a THEOREM — and where it is
    not — ASSERZIONE (la mappa onesta della biforcazione, tre righe):
    (1) al gradino più ridotto — solo rapporto d'area, parete non
    variabile (NON è un ugello alla Rao) — i due problemi COINCIDONO,
    dimostrato; e persino lì la media sbagliata sposta l'ottimo:
    +44-87% sul rapporto d'area, 3-10 s di Isp — misurato dal nostro
    banco (il pattern è lo stesso "argmax mobile a valore piatto" di
    Humphreys e dei plot NUAA — un pattern, non la prova del caso
    generale); (2) plug PIENO adattato: coincidono ancora — il design
    di picco è ottimo, dimostrato con perimetro dichiarato; (3) plug
    TRONCATO (= la configurazione del programma): la coincidenza SI
    ROMPE — dimostrato — e si apre il primo problema di forma
    genuinamente mediato che non collassa; QUANTO renda al contouring
    è la domanda APERTA — e la fisica di record non la dice piccola:
    fluttuazioni imposte 10:1 nei BC pubblicati, escursioni ~6:1 in
    gola e ~20:1 al combustore, e il parere del panel: "l'errore
    potrebbe essere grande — la teoria oggi non può escluderlo". Il
    computo che risponde (il confronto a tre design sul plug troncato)
    non è ancora stato eseguito: macchina pronta, prima campagna della
    fase che apre ora. Nessuna attesa di "piccolezza" è nei nostri
    atti. — EVIDENZA: figura a 3 pannelli (coincide / coincide / SI
    ROMPE) con la configurazione nostra evidenziata + inserto misura
    banco. — [NOTE] join: CH1-feed-3 (THEOREM/THEOREM*/clausola
    sharpness) + CH1-feed-10 (forma bloccata D-06 per ogni claim di
    primato, in nota+Q&A) + CH2-feed-3 (PRACTICE rejector, dIsp
    +3.33…+9.71 s su 6 casi) + CH2-feed-8 (cycle-wall 2-D OPEN, owner
    F2) + CH6-feed-8 (strictness = clausola, carrier PB-2 OPEN) +
    CH5-feed-9 (escursioni, CT-6); guardie 2/3 (T1c pattern-only, mai
    "1-DOF nozzle case") incorporate nell'asserzione; biforcazione
    twin PB-2 = decisione utente APERTA, dichiarata in C17-bis. —
    1.5' — cut: no.
C8. [atto 4] Why the per-phase family is the right object —
    ASSERZIONE: dentro la classe di dati dichiarata — onda rotante
    periodica pura, monitorata sulla piattezza di T0 — il flusso è
    STAZIONARIO nel frame rotante: la famiglia per-fase non è
    un'approssimazione, è un CAMBIO DI COORDINATE esatto (un
    quoziente), con UNA sola approssimazione dichiarata (di ordine
    Strouhal) e le sue ipotesi stampate; la media temporale globale —
    quella del campo — mescola le fasi: è la riduzione più crudele,
    non la nostra. QUESTO passaggio ha oggi la STRUTTURA DI PROVA
    DICHIARATA (via: equivarianza S1), non ancora la prova completa —
    e lo scriviamo sulla slide. — EVIDENZA: diagramma annulus → frame
    rotante → famiglia per-fase vs collasso globale, organizzato sui
    tre piani (cosa entra nello stato / cosa si perde / quanto costa
    salire). — [NOTE] join: CH1-feed-2 (SCHEMA + [T-T0P-E] THEOREM) +
    CH7-feed-1 (edificio tre piani) + decisione utente :1450
    (checkpoint :95-97, guardia 12): il tag on-slide RESTA, in forma
    parlante. — 1.5' — cut: no.
C8-bis. [atto 4] The design space: configurations are OUTPUTS, not
    inputs — ASSERZIONE: la variabile di design è il corpo solido
    dentro un envelope: bell, plug, shrouded plug,
    expansion-deflection non si presuppongono — EMERGONO come classi
    topologiche del risultato; i settori ammissibili sono in numero
    finito e l'ottimo globale è il vincitore di un torneo tra gli
    ottimi di settore; ogni ottimo che consegniamo dichiara il suo
    meccanismo di globalità e la sua forza — mai la parola "ottimo"
    senza contratto. Il primo verdetto di torneo esiste già: alle
    chiusure certificate il plug domina debolmente la bell punto per
    punto, con la zona di pareggio caratterizzata — un ranking tra
    CHIUSURE a pari rapporto d'area, mai tra hardware. La rotta di
    parametrizzazione è spline certificata per settore, non level-set:
    un corpo infinitesimo in supersonico paga solo wave drag — si
    confrontano settori interi; e il dato della scuola classica ("il
    metodo esatto batte i genetici") conforta la rotta. Stato onesto:
    oggi il driver esercita UN settore (bell, 9 gradi di libertà); gli
    altri hanno owner e finestre nominate. — EVIDENZA: envelope + 4
    settori come output con lo stato di ciascuno. — [NOTE] join:
    CH8-feed-1 (feed di punta) + CH8-feed-2 (THEOREM, X-GRP10/12) +
    CH8-feed-3 (THEOREM*) + CH8-feed-4 (contratto M1-M5 — sigla in
    nota, concetto on-slide) + CH8-feed-8 + CH8-feed-9 (LL-29);
    guardia 8. — 1.5' — cut: no.
C9. [atto 4] What the average can and cannot see — ASSERZIONE: due
    flussi con la STESSA traccia di pressione ma contenuti di swirl e
    fluttuazione diversi producono spinte diverse — dimostrato senza
    un solo run CFD: la riduzione a sola pressione è CONDANNATA (il
    passo finale sugli ottimi ha la struttura di prova dichiarata, con
    la sua premessa esplicita — lo distinguiamo dal teorema); la media
    full-state per fase è invece ESONERATA su quell'asse; il peso in
    gioco: 1.5-3% della spinta, con contributi fino al 9% della
    pressione. Conseguenza di contratto: il campo impone al bordo la
    sola pressione — quella proiezione perde informazione di spinta;
    il nostro contratto full-state È la riparazione. — EVIDENZA:
    schema fibra di casa (traccia P fissata, famiglia di stati
    compatibili). — [NOTE] join: CH3-feed-3 (THEOREM*/SCHEMA) +
    CH10-feed-5 (forma riparata REFUTE_CH10 F1 letta su disco: classi
    PER GAMBA — T-DISC-1 THEOREM*, T-DISC-2 split-grade SCOPED,
    T-DISC-3(b) SCHEMA con premessa (DR), mai "THEOREM" secco: le
    classi vivono in nota, l'asserzione le dice in forma parlante) +
    CH7-feed-2 ([SE] pesi); lineage LL-6/LL-24. — 1.5' — cut: no.
C10. [atto 4] What the reduction drops — ASSERZIONE: ciò che la
    riduzione scarta non è una speranza: è un OPERATORE ESPLICITO, con
    le identità verificate a macchina; il suo canale medio è
    esattamente NULLO — dimostrato — e al primo ordine sopravvivono
    esattamente due canali: i salti ai fronti (il TALLONE dichiarato:
    la loro taglia non ha ancora un numero) e la covarianza; il
    residuo non è "trascurabile" — è MISURABILE, e la campagna che lo
    misura è la prima della fase che apre ora. La faccia pubblicata di
    questo teorema esiste: la forza laterale istantanea è il 25-35%
    dell'assiale, ruota alla frequenza d'onda, e media a zero. —
    EVIDENZA: schema operatore + CROP P-C Fig. 21. — [NOTE] join:
    CH3-feed-1 (DEFINITION+THEOREM*) + CH3-feed-2 (THEOREM*, clausola
    SBV) + CH5-feed-3 ([FIG]+[INFER], CT-6) + CH7-feed-3 (guardie
    1/16: il tallone si dichiara sempre); M-RED in C17. — 1.5' —
    cut: no.
C11. [atto 6] The honesty table — ASSERZIONE: il nostro errore
    residuo, canale per canale: sei canali, per ciascuno il caso
    migliore e il peggiore CON il livello di evidenza dichiarato
    (teorema / misura nostra / stima d'ordine / dato di letteratura) —
    i canali non si sommano; nel migliore dei casi (fuori asse
    escluso) l'errore plausibile è di singole cifre percentuali; fuori
    asse, oltre il 10% non è escluso; il canale "spostamento
    dell'ottimo" NON HA ANCORA UN NUMERO — lo diciamo, e la strada per
    dargli un numero è nominata e ordinata; l'unico numero in-classe
    che abbiamo (+0.51%) porta stampata accanto la sua incertezza
    (~30% del dato) — contro la scala classica di Rao 0.04-0.34%
    (numeri loro). E nessun arbitro esterno esiste per questo errore:
    il bracket lo chiudiamo noi, o non è chiuso. — EVIDENZA: la
    tabella resa a colori per livello di evidenza, compressa ai
    highlights (integrale nel backup). — [NOTE] join: CH3-feed-4
    (classi per cella) + CH3-feed-5 (delta/L_H underived, SCHEMA) +
    CH7-feed-4 (celle verbatim) + CH1-feed-9 (band-underinclusion) +
    CH2-feed-7 (spina condizionale C-D25U, in nota) + CH5-feed-10;
    [D-44 guardia 6: bracket, MAI adequacy — tag in nota, la slide lo
    DICE col contenuto]. — 2' — cut: no (core-15', fusa con C9).
C12. [atto 6] The worst-direction marker — ASSERZIONE: il segnale più
    grande in direzione peggiore è pubblicato: aggiungere uno shroud
    porta un plug dal 58.1 al ~71.5% dell'ideale A PARI RAPPORTO
    D'AREA — più dell'intera linea di design sul rapporto d'area,
    inspiegato dagli autori; lo teniamo a registro come candidato
    "swirl-breaker". — EVIDENZA: CROP figura shroud Paxson-Miki, CT-6.
    — [NOTE] join: v1 C12 [ADV]; lineage LL-5 (la loro metrica è la
    nostra spinta ciclo-mediata, mai posta come funzionale — nota
    Q&A). — 1' — cut-pos 7 (→ backup, 1 riga resta in C11).

### C-III. La macchina: perché queste scelte, e la prova (9')
### [regola di sezione invariata: NULLA di scontato sul metodo — ogni
### concetto spiegato alla prima occorrenza, col PERCHÉ ingegneristico]

C13-pre. [atto 5] Why an adjoint, and which one — method primer —
    ASSERZIONE (4 concetti da primo incontro, ciascuno col perché):
    (1) ADJOINT: con UNA soluzione in più si ottiene il gradiente
    rispetto a TUTTI i gradi di libertà insieme — e non è un'idea
    moderna: sono i campi moltiplicatori di Hoffman 1967, lungo le
    stesse caratteristiche (la genealogia di prima); (2)
    DISCRETO-ESATTO: differenziamo ESATTAMENTE il problema che il
    computer risolve — il gradiente calcolato all'indietro È l'adjoint
    trasposto del march, un'identità algebrica verificata a precisione
    macchina: zero gap tra schema e gradiente (continuo-prima nella
    formulazione, discreto-esatto nella macchina: le condizioni di
    ottimalità si capiscono nel continuo, il numero si calcola senza
    approssimare il gradiente); (3) OTTIMIZZATORE: trust-region Newton
    segmentato a curvatura MISURATA — scelto per robustezza su
    problemi con tratti a curvatura irregolare e per la
    certificabilità del passo, contro alternative pesate e documentate;
    (4) CERTIFICATO: ogni condizione verificata a posteriori con
    soglia DERIVATA (mai magica) e oracoli indipendenti che possono
    RIGETTARE. — EVIDENZA: 4 card con micro-schema. — [NOTE] join:
    CH9-feed-4 (THEOREM T-LEMB; limite mesh separato SCHEMA S-LBML —
    in nota) + CH2-feed-5 (C56 ruoli CLOSED; O3.1 PRACTICE);
    aggiudicazione C31 in nota. — 1.5' — cut: no.
C13-val. [atto 5, NUOVA v3.1] Before going where Rao cannot, the
    machine reproduces Rao — ASSERZIONE: sul problema CLASSICO
    (ugello massima spinta, caso ridotto), il nostro ottimizzatore —
    adjoint esatto + trust-region Newton, per una rotta completamente
    indipendente dalla costruzione classica — RITROVA il contorno di
    Rao: due rotte indipendenti, un solo contorno, scarto massimo
    ~2·10⁻³ del raggio di gola, dentro la banda d'errore derivata dal
    confronto tra i codici. Il metodo nuovo poggia su una macchina che
    ha già superato il benchmark che il campo riconosce. — EVIDENZA:
    **l'immagine di casa ESISTE ed è di record:
    `validation/brick2_profiles_record.png`** (contorno variazionale
    W* sovrapposto al contorno Rao classico GENO + pannello |dy| in
    banda derivata; titolo del png già in inglese, restyling
    all'authoring secondo il patto di stile — asse |dy| log e legenda
    da alleggerire). — [NOTE] carrier:
    `validation/PROGRESS_2026-08-06_S18_brick2run.md` (run di record
    S18, [X-TOCV]); i conteggi di verifica del run (oracolo 91/91,
    KKT vs soglia) stanno in nota relatore, NON on-slide; ponte
    naturale alla C13 (il grafo delle scelte di quella macchina). —
    1' — cut: no (è il ponte-credibilità dell'atto 5).
C13. [atto 5] From theory to a design machine — ASSERZIONE: la
    pipeline end-to-end in 8 stadi — dal contratto sui dati al
    verdetto finale — dove OGNI scelta algoritmica è a registro con le
    alternative pesate e un falsificatore; anche le scelte NON ancora
    prese sono dichiarate, con owner e finestra: il grafo mostra anche
    ciò che non abbiamo deciso. E il confronto col campo: nessun
    metodo di design pubblicato consegna il proprio risultato dentro
    una catena di verifica capace di rigettarlo. — EVIDENZA: GRAFO L0
    (overview ribbon). **VINCOLI DI RENDER (di record, prototipo
    1920×1080 esistente)**: (i) NOMI-DISPLAY CORTI ≤10 caratteri,
    full name in sottotitolo/parlato — LISTA PROPOSTA: 1 CONTRACT ·
    2 REPRESENT · 3 MARCH · 4 CERTIFY · 5 ESTIMATE · 6 OPTIMIZE ·
    7 AGGREGATE · 8 VERDICT; (ii) footnote C46 (somma per-stadio ≠
    totale); (iii) Stage 7 mini-bar neutra grigia con badge; (iv)
    arco solo per il cluster A (4↔6), halo per B/C/D; (v) glifo
    compatto "2-faces". — [NOTE] join: CH4-feed-1 ([REP]: 62 scelte,
    tally 12/36/12/2, 48 aggiudicate — TUTTO il tally in nota
    relatore e retro-audit, MAI on-slide) + CH9-feed-8 (NOT-FOUND(q)
    in nota) + DERISK §1-§4 + pipeline_graph.json (79 nodi/45
    archi/4 superfici, estratti mai hand-typed); forma CH4 W2-R2
    conservata NEL DOCUMENTO per il retro-audit (WA_A3 critic 3). —
    1.5' — cut: no.
C14. [atto 5] Zoom: the optimizer stage — ASSERZIONE: dentro lo
    stadio ottimizzatore: il driver trust-region Newton segmentato su
    gradiente discreto-esatto, e — detto apertamente — il gruppo di
    scelte che RIESAMINEREMO all'ingresso della prossima fase, con
    un candidato di ricambio nominato dalla letteratura 2026 e un
    criterio di confronto pre-registrato a parità di vincoli: il
    censimento dei solver è datato, e lo dichiariamo. — EVIDENZA:
    GRAFO L1 stadio 6 in **3 PANNELLI** (vincolo DERISK §3.1: 24 nodi
    misurati, non 20; lo split a 2 violerebbe la regola ≤12
    card/slide): (6a) engine+driver; (6b) numerics & tolleranze; (6c)
    design-basis. Shape glyphs sui node card (canale colore+forma). —
    [NOTE] join: CH4-feed-9 (card C31 6-campi con Uno/MPC-2026 —
    la card COMPLETA in nota e backup, on-slide la forma parlante;
    guardia 14 soddisfatta nel layer) + DERISK §3.1; LL-15/LL-30. —
    1.5' — cut: no.
C15. [atto 5] Zoom: certificates & bands — ASSERZIONE: come la
    macchina sa di non mentire: il gradiente è esatto per il problema
    discreto davvero risolto, verificato a precisione macchina e
    controllato in modo indipendente contro un secondo codice, CON
    controlli negativi che rigettano; ogni certificato ha una soglia
    DERIVATA e la soglia MORDE (dimezzarla ribalta il verdetto — un
    certificato che non può bocciare non è un certificato); l'errore
    di discretizzazione ha il suo stimatore dedicato con un arbitro
    indipendente, l'errore di modello la sua forchetta per canale —
    mai confusi; e il fronte è trattato col solo schema che può
    portare un certificato di gradiente, per un motivo PUBBLICATO
    (il teorema negativo di Giles-Ulbrich). Nessun risultato lascia
    la macchina senza il suo corredo: contorno, certificati, barre e
    verdetto viaggiano insieme. — EVIDENZA: GRAFO L1 stadi 4-5
    (selezione) + strip della soglia derivata. — [NOTE] join:
    CH4-feed-2 (52/52, 218/218 — in nota) + CH4-feed-3 (KKT 7.7e-2
    vs 1.156e-1, oracolo 91/91, stage V0 — in nota, guardia 7) +
    CH4-feed-5 (NTF η·κ_q, GAP-29) + CH3-feed-9 (DWR C11) +
    CH4-feed-10 (C49, LL-12) + CH9-feed-2 (Verdict) + CH9-feed-3
    (G1 assoluto — in nota). — 1' — cut-pos 2 (→ backup D4-D5).
C16. [atto 5] Engine numbers — ASSERZIONE: la velocità è stata
    progettata, non trovata: ogni leva di accelerazione è passata da
    un gate di invarianza (stessi risultati, certificati inclusi);
    oggi: valutazione+gradiente in 0.45 s; un segmento di design in
    15-20 s (obiettivo ≤30: superato); una campagna completa in 10-14
    minuti (obiettivo ≤25: superato); 18× sul run di riferimento —
    misure nostre, su host dichiarato. Le campagne di validazione
    diventano atti economici. — EVIDENZA: tabella compatta + barre
    target-vs-measured. — [NOTE] join: CH4-feed-4 ([REP], caveat
    host; catena 100.84→32.09→5.58 s in nota) + v1 C16; "suite 23/23
    EXIT 0" e [X-SPDB] SOLO in nota (contabilità); stage
    "verificato" detto a voce, tag P34 in nota (guardia 7/18). — 1' —
    cut: MAI (core-15').
C16-bis. [atto 6] The machine that says NO — to us — ASSERZIONE:
    abbiamo commissionato un audit OSTILE alla nostra stessa catena
    di certificazione, e la catena ci ha bocciato: verdetto "non
    certificabile", due difetti nominati — uno riparato subito e
    dichiarato, uno con un responsabile e una scadenza; prima ancora,
    avevamo costruito noi il modo in cui il nostro auto-controllo
    avrebbe potuto mentire, lo abbiamo esibito con un controllo
    negativo e chiuso con una verifica indipendente dal solutore;
    ogni audit passa solo se conferma il vero E rifiuta il falso (un
    esca costruita apposta È stata rifiutata prima che il verdetto
    contasse); e l'accordo tra i nostri due codici non lo trattiamo
    come verità: i claim poggiano su invarianti che non dipendono da
    nessuno dei due. Tra il primo audit e il secondo i difetti sono
    migrati dall'oggetto certificato al certificatore: il pavimento è
    salito. Il sistema funziona perché boccia noi. — EVIDENZA:
    timeline dei 2 audit + card dei 2 difetti (riparato/owner). —
    [NOTE] join: CH9-feed-1 + CH4-feed-7 + CH4-feed-6 (incidente
    "claim prima dell'evidenza" colto dal ri-conteggio — in nota,
    accoppiato come da feed) + CH9-feed-5 + CH9-feed-7 + CH9-feed-6
    + CH9-feed-10; "23/23", "2 P0", nomi interni degli audit in
    nota. — 1.5' — cut: no (È il pilastro P2 in forma ESA).

### C-IV. Onestà finale, roadmap e richieste (6.5')

C17-pre. [atto 6] Which gap dominates — the honest map — ASSERZIONE:
    tre design sulla lavagna: quello a stato medio (il comparatore —
    che NESSUNO ha mai computato in questo confronto, noi compresi:
    il campo computa design a stato medio, ma il confronto testa a
    testa non è mai stato eseguito), il nostro per-fase, e l'ottimo
    3D vero (incomputabile per chiunque): tre gap — formulazione,
    modello, composizione — e la domanda di valore è quale domina, su
    quale asse. La nostra IPOTESI DI LAVORO, dichiarata e
    falsificabile (non un teorema): a vincoli e settore fissi il gap
    di formulazione domina — perché sul gap di modello abbiamo tre
    teoremi di soppressione sulla parte liscia, sul gap di
    formulazione nessuno. MA con il suo TALLONE, sempre detto
    insieme: i salti ai fronti sono il primo ordine NON soppresso del
    gap di modello, e la loro taglia non ha ancora un numero — se
    sono grandi, il modello può dominare comunque. Lo scenario di
    morte del programma richiede DUE fallimenti indipendenti, e
    ciascuno è misurabile separatamente: il primo dal confronto testa
    a testa (economico, si fa per primo: uccide o valida), il secondo
    dalle gambe di misura del residuo. — EVIDENZA: schema a 3
    colonne (mean / per-fase / 3D-vero) con i gap come frecce + box
    tallone. — [NOTE] join: CH6-feed-1 (scope "nel record", riparo
    WB1-C3-14) + CH6-feed-2 + CH6-feed-3 (CO-PRESENZA gerarchia+
    tallone sulla STESSA slide — vincolo stampato nei feed, guardia
    1) + CH6-feed-4 + CH6-feed-5 (il campo non separa i gap —
    NOT-FOUND in nota). — 1.5' — cut: no (cerniera atto 6→7).
C17. [atto 7] What tightens the bracket, in order — ASSERZIONE: la
    roadmap È l'elenco ordinato di ciò che stringe la forchetta:
    prima la campagna che MISURA il residuo su famiglie certificate
    (economica, decisiva — costruisce l'arbitro che in letteratura
    non esiste); poi il run CFD accoppiato in coppia sul template del
    campo; solo dopo, e solo se serve, il run di riferimento di
    classe (~milioni di celle). Gap B (nostro design vs design a
    stato medio) è misurabile in-house; Gap A (distanza dall'ottimo
    3D vero) non è computabile da nessuno — noi siamo gli unici a
    LIMITARLO. La condizione di valore è un rifiutatore armato, oggi
    indecidibile — e lo diciamo: nessun numero esiste su nessun lato
    prima della campagna; e il programma ha un criterio di morte
    onesta: se il guadagno misurato resta sotto ~1% di Isp, il
    programma dichiara il pivot (certificazione e operabilità) — non
    insiste. Stato temporale: la fase è APPENA APERTA — nessun
    risultato di campagna viene promesso come già acquisito;
    milestone: inizio/metà settembre. — EVIDENZA: timeline F2→F5 con
    3 gate colorati. — [NOTE] join: CH6-feed-9 + CH6-feed-6 (G2
    value gate) + CH6-feed-7 (D-44 gated) + CH3-feed-6 (M-RED bande
    derivate, esiti pre-registrati) + CH3-feed-10 e CH1-feed-8
    (B-lite metro cheap del residuo — in nota relatore come leva) +
    checkpoint :93-94. — 1.5' — cut: MAI.
C17-bis. [atto 6/7] Decisions we have NOT taken yet — ASSERZIONE: le
    decisioni ancora aperte, dette al panel prima che le chieda:
    (1) il confronto testa-a-testa sul plug troncato: numero
    PRE-milestone oppure "macchina pronta, prima campagna della
    fase" — la scelta è aperta, il deck porterà l'una o l'altra, mai
    una via di mezzo; (2) due strade tecniche con biforcazione
    dichiarata (trattamento del mean-swirl; priorità di una chiusura
    di parete) — presentate con le alternative e il criterio, non
    già decise; (3) il contratto dati non è congelato — un'ipotesi
    fisica (choking RDE) è dichiarata aperta con responsabile; (4)
    uno dei nostri gate non ha ancora una soglia capace di
    rigettare: la deriveremo come NUMERO, e intanto lo diciamo. —
    EVIDENZA: card "OPEN" con owner+finestra. — [NOTE] join:
    CH7-feed-8 (S-5F path A/B/C + C51, card non-aggiudicate nel
    layer) + CH10-feed-7 (U3' PREMISE-OPEN F2a) + CH3-feed-7 (G3/
    F5b) + cross-ref C7-ter (twin PB-2, decisione utente al gate);
    nomi interni (S-5F, C51, U3', G3, PB-2) in nota — on-slide la
    forma parlante. — 1' — cut-pos 5 (compressa a card dentro C18).
C18. [atto 7] ASK — con Annex B on-slide — ASSERZIONE: tre richieste:
    (1) il run di riferimento di classe: collaborazione o
    procurement (costo di classe ~12M celle, criteri di qualità
    pubblicati); (2) dati motore nella classe che il metodo richiede:
    pressione high-speed / imaging da hot-fire per verificare la
    piattezza di T0 e la frequenza di ciclo — il nostro monitor
    DECIDE, non benedice: è costruito per rigettare il dato che non
    rispetta la classe, e ci aspettiamo che i dati reali lo
    esercitino; (3) canali di pubblicazione e tre paper chiave da
    procurare. E LA RISPOSTA ALLA DOMANDA "che input vi serve":
    per progettare l'ugello del VOSTRO motore bastano le specs —
    ogni dato in più sale una scala dichiarata di affidabilità
    (livello di evidenza: predizione di contratto, non ancora
    esercitato su un dataset reale — lo diciamo); il dato non
    "entra": viene AMMESSO, e il gate d'ingresso sa dire no. FORMA
    DECISION-READY (prassi d'agenzia, header): ogni card porta cosa
    chiediamo / cosa serve al panel per decidere / entro quando (le
    finestre: campagna residuo entro la fase appena aperta, milestone
    inizio/metà settembre; il run di classe si decide DOPO quella
    misura — la decisione oggi è sul canale, non sul commit). —
    EVIDENZA: 3 card + ladder Annex B (casi A-G). — [NOTE] join:
    CH10-feed-1 (il feed più prezioso; stage P34 prediction in
    nota) + CH10-feed-2 (G6 loud-reject, mai esercitato — detto
    on-slide in forma parlante) + CH7-feed-5 (monitor TRIPLE:
    dettaglio "un monitor Γ-only licenzierebbe il falso" in nota) +
    MESSAGE_ARCHITECTURE §ASK (Fotia/Goto/Ma in nota). — 1.5' —
    cut: MAI (core-15').
C19. [atto 7] Summary — ASSERZIONE (doppio takeaway): per gli
    ingegneri — il primo metodo di design variazionale per-fase per
    ugelli RDE, con ciò che la riduzione trascura reso operatore
    misurabile e una forchetta d'errore onesta, canale per canale;
    per i programmi — una macchina abbastanza veloce da rendere la
    validazione un atto economico, un piano incrementale già
    prezzato, e un criterio di morte onesta dichiarato. La nostra
    onestà non è un disclaimer: è strumentata dentro il metodo — i
    limiti li avete visti scritti sulle slide, coi loro livelli di
    evidenza. — EVIDENZA: 5 bullet + grafo L0 in miniatura come
    firma. — [NOTE] join: CH6-feed-10 (D-44/P34/card — la
    strumentazione si DICE col contenuto, le sigle restano in nota;
    guardia 18) + MESSAGE_ARCHITECTURE takeaway duali. — 1' — cut:
    MAI.

==========================================================================
## PARTE D — BACKUP DECK (skeleton; si costruisce DALLA mappa Q&A
## del Blocco 2 — qui SOLO struttura + puntatori, nessuna ricopiatura)

[Il registro guardia 18 vale ANCHE sul backup: le card portano la
lingua ingegneristica in faccia e la contabilità (classi, conteggi,
id di registro) nel corpo-nota — il backup è il posto dove il panel
che CHIEDE la contabilità la riceve, su domanda.]

D1-D8. GRAFO L1 degli 8 stadi completi (walkable graph promise; Stage 6
    = 3 pannelli anche qui; L1 porta gli archi long-range E9/E28/E29
    come stub-label — vincolo DERISK §5; node card L2 popolate da
    pipeline_graph.json, compressione ≤40 parole/campo = atto di
    authoring, cite-only).
D9+. Node cards L2 per i nodi Q&A-mapped, INCLUSI i consumi
    dichiarati-a-backup della tabella di join: card f2=−λ2 (CH2-feed-4),
    card corrector-as-perturbation (CH3-feed-8), card licenza-di-classe
    ("la licenza segue il flusso": single-wave → certificato pieno; RPO
    → pratica dichiarata; multistabile → layer robusto; caotico →
    RIFIUTO ONESTO, CH1-feed-6), card theory-as-code (CH9-feed-9), card
    C50 incertezza-del-dato (CH10-feed-8), card C31 completa a 6 campi
    (da C14), card tally del choice ledger (da C13: 62/48/12/2 — la
    contabilità spostata OFF-main vive QUI).
D-F. FORCHETTA integrale (6 righe complete, celle verbatim con classi)
    + C2/C12 versioni integrali se tagliate dal main.
D-N. Metodologia figure/riuso: manifest + audit di provenienza.

**PUNTATORI Q&A SEED (la banca-obiezioni NON si ricopia: il Blocco 2
la consuma da qui)**:
- `reconstruction/REFUTE_WB1_extensions.md` — Q&A SEED per-capitolo:
  CH1 :85 · CH2 :196 · CH3 :305 · CH4 :441 · CH5 :574 · CH6 :725 ·
  CH7 :843 · CH8 :973.
- `reconstruction/REFUTE_CH9.md` :206 (obiezioni SOSTENUTE → semina).
- `reconstruction/REFUTE_CH10.md` :265 (domanda→risposta→ancora→backup).
- `reconstruction/REFUTE_LINEAGE.md` :549 (fronte Purdue/Heister — la
  slide C7-bis-pre è la risposta pre-cotta on-deck).
- `reconstruction/REFUTE_W2_minipass.md` :103.
- Banchi domanda dei refuter W-A (REFUTE_CH1..CH8, sezioni "Banco
  utente"/"Attacco al banco") = seconda sorgente, già refutata.
[Guardia 17 vincola le risposte Q&A su feedback ugello→camera: nessun
claim di decoupling senza condizione di choking citata. Guardia 18
vincola il REGISTRO delle risposte.]

==========================================================================
## TIME-BOXING SUL 60' (v3.1 — conteggi misurati su QUESTA lista)

| Blocco | slide | min |
|---|---|---|
| A1-A3 apertura+BLUF+mappa | 3 | 4 |
| A4-A6 primer RDE | 3 | 6 |
| A7-A13 codice+V&V (fusione A12) | 7 | 8 |
| A14-A20 linee di ricerca | 7 | 7 |
| B1 ponte | 1 | 2 |
| C-I efflusso+campo (C1-C6 + C3-bis) | 7 | 8.5 |
| C-II problema+framework (C7-C12 + bis/ter/pre) | 10 | 10.5 |
| C-III macchina (C13-pre, C13-val, C13, C14, C15, C16, C16-bis) | 7 | 9 |
| C-IV onestà finale+roadmap+ask (C17-pre..C19) | 5 | 6.5 |
| **TOTALE main deck** | **50** | **61.5 → 60** (buffer video 26s+14s + pace A14-A20 1'/slide assorbono 1.5') |

[La slide nuova C13-val (+1') è assorbita da: C15 2→1' (asserzione
snellita, contabilità in nota) e C-I/C-II −1' complessivo (C2 1.5→1',
C7-ter 2→1.5': in entrambe la parte-contabilità è migrata in nota).]

**CUT-LIST ordinata v3.1 (pre-decisa, si taglia in quest'ordine)**:
1. A12 fusione già assorbita / A19 video (−1')
2. C15 zoom certificates → backup D4-D5 (−1')
3. A4-A6 primer compresso a 2 slide (−2')
4. C2 throat → backup (resta 1 riga in C1) (−1')
5. C17-bis compressa a card dentro C18 (−1')
6. A14-A20 linee compresse (−3')
7. C12 worst-marker → backup (resta 1 riga in C11) (−1')
[C13-val NON è in cut-list: è il ponte-credibilità dell'atto 5.]

**CORE-15' (modulo di resilienza)**: A2 BLUF (2') + B1 (1') + C4 (2') +
C7 (1.5') + C7-bis (2') + C11 con C9 fusa (3') + C13-val+C16 fuse (1.5')
+ C18 (2') = 15'. [Invariante: il core contiene sempre la slide-cuore
C7-bis, la catena-evidenza C4, la validazione sul classico, la
forchetta e l'ASK.]

==========================================================================
## DELTA vs v1 (v3, invariato) — [NOTE] layer retro-audit

1. **Deck = consumer dell'atlas**: ogni slide porta il join esplicito
   CHx-feed-n / LL-id / card (ordine utente; contratto [F-des-4]).
2. **+C16-bis "The machine that says NO — to us"**: i feed CH4-6/7
   chiedevano la slide di onestà accoppiata; assorbe CH9-1/5/6/7/10.
3. **+C17-pre "Which gap dominates" (N-Q)**: consuma CH6-1..5 col
   vincolo di co-presenza gerarchia+tallone-(J) sulla stessa slide.
4. **+C17-bis "Decisions we have NOT taken yet"**: twin PB-2 aperto al
   gate, S-5F/C51, U3', G3-senza-rejector — forma onesta.
5. **Fix borderline WA_A3**: C7-bis-pre ("livello di RIDUZIONE di
   Stechmann"); C7-ter (T1c pattern-only vincolante).
6. **CH10 feed 5 nella forma riparata** (classi per gamba, T-DISC-3(b)
   SCHEMA con premessa (DR)).
7. **Vincoli DERISK incorporati** (nomi corti, C46, Stage-7, halo,
   2-faces; Stage 6 in 3 pannelli; grafo estratto mai hand-typed).
8. **C8 con tag :1450 on-slide** (in v3.1: forma parlante).
9. **C18 con pannello Annex B** + G6 + monitor TRIPLE.
10. **C6/C7-bis-pre joinano il LINEAGE_LEDGER per LL-id**.
11. **Time-boxing ricontato dalla lista** (v1 dichiarava 41 vs 46
    effettive; conteggio rigenerato in finestra).
12. **A6 consuma il feed EAP** (CH1-5/CH5-7).

## DELTA v3 → v3.1 (revisione di registro CKP-S2-3 / guardia 18)

1. **REGISTRO INGEGNERISTICO SU OGNI SLIDE (ordine utente, intento non
   lista)**: tutte le ASSERZIONI riscritte in lingua della propulsione;
   la contabilità interna (62/48/12, 52/52, 218/218, 91/91, 23/23,
   tally card, "2 P0") e il gergo di processo (sigle di classe nude,
   query-bounded/NOT-FOUND(q), stage P34, guardia N, nomi interni
   S-5F/C51/U3'/G3/PB-2/M-RED sulle slide dove erano nudi) MIGRATI nel
   campo [NOTE] = note relatore + layer retro-audit. I numeri FISICI e
   dei PAPER restano on-slide (10:1, 6:1, ×2.45, +4-7%, 58→71%,
   3-10 s, ~1%, 0.2-1.5%, +0.52%/−5.78%, 0.45 s/15-20 s/10-14 min/18×,
   1.5-3%/9%, 25-35%, +0.51% con ~30%). Slide più toccate: C2, C3-bis,
   C6, C7, C7-bis, C7-ter, C8, C8-bis, C9, C10, C11, C13-pre, C13,
   C14, C15, C16, C16-bis, C17-pre, C17, C17-bis, C18, C19.
5. **C8**: il tag di decisione utente resta ON-SLIDE (ordine esplicito)
   ma in forma parlante: "questo passaggio ha la struttura di prova
   dichiarata (via: equivarianza S1), non ancora la prova completa".
2. **+C13-val "Before going where Rao cannot, the machine reproduces
   Rao"** — IMMAGINE DI CASA TROVATA SU DISCO:
   `validation/brick2_profiles_record.png` (S18 record: contorno
   variazionale adjoint/TR sovrapposto al contorno Rao classico GENO,
   max |dy| = 1.9e-3, pannello scarto in banda derivata; carrier
   `validation/PROGRESS_2026-08-06_S18_brick2run.md`, [X-TOCV]) —
   nessuna figura da generare; restyling leggero all'authoring (patto
   di stile). Inserita tra C13-pre e C13 (il perché delle scelte → la
   prova → il grafo). Nota mandato: la slide è UN'istanza del
   registro, non un requisito — adottata perché il filo la regge
   (ponte-credibilità); entra anche nel core-15' (fusa con C16).
3. **C13-pre/C13/C14/C15/C16 riscritte in chiave "perché"**: perché
   l'adjoint e quale (continuo-prima in formulazione, discreto-esatto
   in macchina — le due ragioni dette da ingegneri), quale
   ottimizzatore e perché (curvatura misurata, robustezza,
   certificabilità del passo), certificati come "come la macchina sa
   di non mentire" — meno registri, più ragioni.
4. **Sezione C-III rinominata** "La macchina: perché queste scelte, e
   la prova"; atto 5 esteso col passo "evidenza concreta che la
   macchina funziona" del filo CKP-S2-3.
6. **Time-boxing**: 50 slide main, 61.5→60 (C13-val +1' assorbito da
   C15/C2/C7-ter snellite); cut-list invariata nell'ordine, C13-val
   esclusa dai tagli; core-15' aggiornato (C13-val+C16 fuse).
7. **Convenzione [NOTE] dichiarata in testa** (nuovo campo "nota
   provenance" per slide): la tabella di join e i tag di guardia
   restano in QUESTO documento come layer retro-audit, mai parte
   dell'asserzione. Il backup deck resta il luogo dove la contabilità
   è disponibile su domanda (card tally, card C31 completa, forchetta
   con classi).
8. **Registro calibrato su prassi mondiali NOMINATE (integrazione
   utente al mandato, clausola C-5)**: assertion-evidence (Alley) +
   principi Doumont + convenzioni technical review d'agenzia
   (ESA/NASA-class) — dichiarati in header come metro del comms
   review; verifica per-slide aggiunta alla convenzione di registro;
   C18 resa esplicitamente DECISION-READY (cosa chiediamo / cosa serve
   per decidere / entro quando).

==========================================================================
## TABELLA DI JOIN feed→slide [F-des-4] — 93 feed, NESSUNO perso
## [NOTE — layer retro-audit: questa tabella NON è contenuto on-slide]

Legenda: M = consumato su slide main (nell'asserzione in forma
ingegneristica e/o nel campo [NOTE]); B = consumato a backup
(dichiarato); ogni riga backup ha la sua card in D9+.

| feed | slide | modo |
|---|---|---|
| CH1-1 (I4 vs I2/I3) | C7-bis | M |
| CH1-2 (quoziente + O(St)) | C8 | M |
| CH1-3 (dove il mean-state basta) | C7-ter | M |
| CH1-4 (wall condition, μ sì) | C7-bis | M |
| CH1-5 (EAP + P4) | A6 | M (nota+strip) |
| CH1-6 (licenza segue il flusso) | D9+ card | B — troppo interno per il main 60'; materiale Q&A classe-dati |
| CH1-7 (campo non dichiara regime) | C7 | M |
| CH1-8 (B-lite metro cheap) | C17 | M ([NOTE]) |
| CH1-9 (+0.51% con band) | C11 | M |
| CH1-10 (primato forma D-06) | C7-ter | M ([NOTE]+Q&A) |
| CH2-1 (T-T7FS(b)) | C7-bis | M |
| CH2-2 (tre modi di mediare) | C7-bis | M |
| CH2-3 (dIsp +3.33..+9.71 s) | C7-ter (inserto) | M |
| CH2-4 (f2=−λ2 al lip) | D9+ card | B — eleganza tecnica da Q&A, non regge da sola il ritmo main |
| CH2-5 (continuo-prima/AD per-ruolo) | C13-pre | M |
| CH2-6 (K-O 1970 obbligatoria) | C6 | M |
| CH2-7 (spina [C-D25U]) | C11 | M ([NOTE]) |
| CH2-8 (cycle-wall 2-D OPEN) | C7-ter | M |
| CH3-1 (operatore K esplicito) | C10 | M |
| CH3-2 (K̄=0, canali (J)/(H)) | C10 | M |
| CH3-3 (T-DISC convicts/esonera) | C9 | M |
| CH3-4 (forchetta classi per cella) | C11 | M |
| CH3-5 (argmax-shift senza numero) | C11 | M |
| CH3-6 (arbitro M-RED) | C17 | M |
| CH3-7 (G3 senza rejector, F5b) | C17-bis | M |
| CH3-8 (corrector perturbativo) | D9+ card | B — dettaglio algoritmico da Q&A |
| CH3-9 (model-form vs DWR) | C15 | M |
| CH3-10 (B-lite residuo) | C17 | M ([NOTE]) |
| CH4-1 (62 tipizzate, tally) | C13 | M (tally in [NOTE]/backup) |
| CH4-2 (52/52, 218/218) | C15 | M (numeri in [NOTE]) |
| CH4-3 (KKT 7.7e-2, stage V0) | C15 | M (numeri in [NOTE]) |
| CH4-4 (velocità, target MET) | C16 | M |
| CH4-5 (NTF morde, GAP-29) | C15 | M |
| CH4-6 (23/23 + incidente) | C16-bis | M (in [NOTE]) |
| CH4-7 (audit NON-CERTIFICABILE) | C16-bis | M |
| CH4-8 (no optimizer + lineage + caveat P-B) | C3-bis | M (forma CH5-1) |
| CH4-9 (card C31 / Uno) | C14 | M (card in [NOTE]/backup) |
| CH4-10 (fitted-front Giles-Ulbrich) | C15 | M |
| CH5-1 (forma vincolante 4-paper) | C3-bis | M |
| CH5-2 (Fig.15 + Fig.13) | C4 | M |
| CH5-3 (Fig.21 K̄=0) | C10 | M |
| CH5-4 (Fig.16 coupling CT-1) | C4 | M (+guardia 17) |
| CH5-5 (pin esibito mai verificato) | C2 | M |
| CH5-6 (scuola classica / mediato assente) | C6 | M |
| CH5-7 (EAP coordinata di J_ideal) | A6 | M |
| CH5-8 (Humphreys ×2.45 WG10) | C5 | M |
| CH5-9 (escursioni 6:1..20:1) | C7-ter | M |
| CH5-10 (nessun regime prezzato / referee) | C11 | M (kicker) |
| CH6-1 (tre design, tre gap) | C17-pre | M |
| CH6-2 (gerarchia ipotesi) | C17-pre | M (co-presenza) |
| CH6-3 (tallone (J)) | C17-pre | M (STESSA slide) |
| CH6-4 (due fallimenti, twin) | C17-pre | M |
| CH6-5 (campo non separa i gap) | C17-pre | M |
| CH6-6 (G2 value gate) | C17 | M |
| CH6-7 (value condition indecidibile) | C17 | M |
| CH6-8 (PB-2 forma riconciliata) | C7-ter | M |
| CH6-9 (roadmap ordinata) | C17 | M |
| CH6-10 (onestà strumentata) | C19 | M (sigle in [NOTE]) |
| CH7-1 (edificio tre piani) | C8 | M (organizzatore visivo) |
| CH7-2 (fibre + pesi [SE]) | C9 | M |
| CH7-3 (residuo + tallone) | C10 | M |
| CH7-4 (forchetta celle verbatim) | C11 | M |
| CH7-5 (monitor TRIPLE) | C18 | M (dettaglio in [NOTE]) |
| CH7-6 (Tillyaeva PENDING) | C6 | M |
| CH7-7 (Fievisohn cugino) | C7-bis-pre | M |
| CH7-8 (S-5F/C51 pendenti) | C17-bis | M (nomi in [NOTE]) |
| CH8-1 (tipo = OUTPUT) | C8-bis | M |
| CH8-2 (torneo plug⪰bell) | C8-bis | M |
| CH8-3 (peak-phase / PB-2) | C8-bis | M (join C7-ter) |
| CH8-4 (meccanismo M1-M5) | C8-bis | M (sigla in [NOTE]) |
| CH8-5 (best-of-sweep regola) | C3 | M |
| CH8-6 (nessun meccanismo nei 4) | C3-bis | M ([NOTE]) |
| CH8-7 (p_b ×2.45 → target M3) | C5 | M |
| CH8-8 (driver UN settore, F3) | C8-bis | M |
| CH8-9 (rotta spline, no TD) | C8-bis | M |
| CH9-1 (catena ha detto NO) | C16-bis | M |
| CH9-2 (Verdict format) | C15 | M |
| CH9-3 (G1 assoluto) | C15 | M ([NOTE]) |
| CH9-4 (reverse-AD = adjoint) | C13-pre | M |
| CH9-5 (self-check poteva mentire) | C16-bis | M |
| CH9-6 (accordo ≠ verità) | C16-bis | M |
| CH9-7 (dual-seed canary) | C16-bis | M |
| CH9-8 (nessuna catena che rigetta nel campo) | C13 | M (kicker) |
| CH9-9 (theory-as-code lint) | D9+ card | B — governance interna, da Q&A processo |
| CH9-10 (progresso tra audit) | C16-bis | M |
| CH10-1 (Annex B specs ladder) | C18 | M |
| CH10-2 (G6 ammette il dato) | C18 | M |
| CH10-3 (Γ_d non è la gola) | C2 | M |
| CH10-4 (sonic line corrugata) | C2 | M |
| CH10-5 (p-only convicted, classi per gamba) | C9 | M (forma riparata; classi in [NOTE]) |
| CH10-6 (nessuna classe dati dichiarata) | C2 | M |
| CH10-7 (U3' PREMISE-OPEN) | C17-bis | M (nome in [NOTE]) |
| CH10-8 (contratto C50 incertezza) | D9+ card | B — istanziazione = duty F2, materiale Q&A dati |

**CONTEGGIO (misurato su questa tabella): 93 feed totali = 88 consumati
main + 5 consumati backup-con-ragione + 0 non-consumati / 0 persi.**
(La slide C13-val consuma il carrier S18 [X-TOCV], che non è un feed
CH: nessun impatto sul conteggio feed.)

## NOTE DI CHIUSURA SLOT [NOTE]

- Ereditati invariati da v1: patto di stile (b) E1-E7, migliorie di
  forma Heister 1-9, attribuzioni primer, formato Verdict del ponte B1.
- Guardie: sweep di costruzione fatto contro GUARD_CHECKLIST 1-18; le
  istanze vincolanti sono citate nei campi [NOTE]; guardia 18 =
  convenzione di registro in testa, applicata a ogni asserzione;
  guardia 15 (convergence provenance) = onere all'authoring: ogni
  slide-claim load-bearing porta la riga claim→ancora→classe→
  quando-a-convergenza nelle note relatore (canale add_notes.py).
- Il retro-audit del Blocco 2 cammina la tabella di join: ogni
  slide→feed→ancora è il percorso all'indietro dichiarato; il
  retro-audit verifica ANCHE la guardia 18 (nessuna contabilità/gergo
  scivolati on-slide all'authoring).
