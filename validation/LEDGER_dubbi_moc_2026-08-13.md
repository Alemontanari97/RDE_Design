# LEDGER DEI DUBBI — audit MoC (motore differenziale + GENO), 2026-08-13
# Direttiva standing: ogni dubbio si investiga A CONVERGENZA. "Indecidibile
# staticamente" NON è terminale: vale solo con esperimento + falsificatore
# nominati E schedulati. Verdetto complessivo positivo solo a ledger vuoto.
# Stati: CHIUSO-CON-PROVA | IN VERIFICA | FERMO | ESEGUIBILE-ORA | APERTO

## A. CHIUSI CON PROVA (controprova + caso, entrambi presenti)

| # | Dubbio | Prova |
|---|---|---|
| A1 | Il motore marcia sempre in avanti su parete nota? Fasi Goursat? | Marcia diretta a parete fissa, entrambe le famiglie per cella, ZERO Goursat; causalità imposta da rejector per-cella |
| A2 | La BC di parete del motore è quella giusta? | Inverse wall Zucrow §16-3d; residuo = (16.9)+(16.11)+(16.13)+tangenza esatte; average-property; conteggio BC completo; punto fisso ≡ PC GENO; record/replay identici. Verificatore avversario: nessun item confutato |
| A3 | Le formule MoC di GENO sono fedeli a Zucrow? | Ri-derivate una per una (Ch.16 e Ch.17): esatte. Sospetto "assorbimento di segno" nelle sorgenti CONFUTATO |
| A4 | I coefficienti Sauer? | Book-exact in ENTRAMBE le implementazioni, incluso l'offset +1e-6 e l'ordine delle operazioni (listing IVLINE del libro) |
| A5 | Media di sinθ all'asse: sin(θ̄) o media dei seni? | I listing FORTRAN del libro dirimono: sin(θ̄). GENO book-exact |
| A6 | (16.43) e (16.44) sono indipendenti? GENO ne implementa una sola | DIMOSTRATO dipendenti: rango 2 su 3, det ≡ 0, EOS-generale (non richiede γ=cost). CAS + 2000 probe. GENO non perde nulla |
| A7 | L'integrale di massa di colonna è quello del libro? | ≡ (16.37) in forma priva di singolarità |
| A8 | CSTR_PA è la corner condition? | ≡ (16.42) risolta per p0 |
| A9 | Il P0 sulla spinta tocca l'algoritmo o solo l'output? | Sweep di ogni lettura di perf%f + lettura dei loop esterni: NESSUN ramo di controllo lo legge. Contorno/campo/portata intatti |

## B. IN VERIFICA (campagne in volo)

| # | Dubbio | Dove |
|---|---|---|
| B1 | N-26: due narrazioni del deficit 9e-4 (off-manifold vs proiezione/orientamento) | **AVANZATO 2026-08-13 (archeologia commit, di prima mano)**: ENTRAMBI i meccanismi atterrano nello STESSO commit 704b8c1 — `foot_state_from_invariants` (ricostruzione on-manifold) E la bracket search (`d2_best`). Il vecchio helper `find_foot_segment` era già stato rimosso in b2ff788. CONSEGUENZA: il fix N-26 ha cambiato DUE cose insieme, quindi **l'attribuzione causale del 9e-4 non è mai stata isolata sperimentalmente** — né il registro (che dice off-manifold) né il commento nel codice (che dice proiezione) hanno una misura che li distingua. Promosso a dubbio di classe D → vedi D13 |
| B2 | Il filtro di causalità x3>x4 del ramo col è corretto in OGNI fase che passa col? In una fase con dati a valle rigetterebbe il piede vero, rendendo il fallback il percorso NORMALE | march-abstraction |
| B3 | Tassonomia delle configurazioni di marcia: quali dimensioni il codice esercita davvero (NON le 4 che avevo imposto io); minimalità da dimostrare | march-abstraction |
| B4 | La convergenza dell'intera colonna è un solutore legittimo o un'euristica? A quale sistema converge davvero? | march-abstraction |
| B5 | I criteri di troncamento (massa, void, jmax plug, level-set) sono corretti, corretti-all'ordine o workaround? | march-abstraction |
| B6 | Censimento workaround: cosa compensa un difetto a monte invece di risolverlo; quali giustificazioni sono circolari | march-abstraction |
| B7 | Pipeline stadio per stadio, ogni tipo × ogni backend, vs letteratura primaria | pipelines-vs-literature |
| B8 | Salute delle citazioni: ogni ancora portante riaperta a pagina in default-REFUTE + 2 canary avvelenati | literature-triangulation |
| B9 | Direzione fonte→codice: cosa il metodo RICHIEDE e GENO OMETTE (iterazione interna su θ3, correzione strato limite, controlli di validità) | literature-triangulation |
| B10 | Contraddizioni teoria di progetto (M0/D1-D7/claims_registry) ↔ letteratura ↔ implementazione, in ENTRAMBI i sensi | literature-triangulation |
| B11 | Tipo 5 (plug): interamente scoperto dall'audit precedente — bypassa il dispatch, storage diverso, aliasing pt3/pt_prev non aggiudicato | pipelines (t5) |

## C. FERMI (errore transitorio del classificatore — da rimettere in coda)

| # | Dubbio | Campagna |
|---|---|---|
| C1 | **RIENTRATA 2026-08-13** (8 famiglie derivate + giudice; raw completo nel task output della campagna). Esiti principali: (a) il giudice ha **MISURATO** i file thermo spediti e **CONFUTATO** il claim di punta di un proprio agente — la discontinuità a T_mid del cp NON è ~1e-4 relativo ma **3.7e-9**, cioè SOTTO tol_conv: il PC converge attraverso T_mid e il P0 collegato è cancellato (era una "verità generale" della letteratura NASA-7 sostituita a una misura); (b) `thermo_H2O2.dat` ha un salto di s⁰ **negativo** ⇒ G(T) non monotona ⇒ l'assunzione di orientamento di `solve_T_from_entropy` è localmente falsa, MA nessun caso spedito lo usa ⇒ latente P2 non raggiungibile; (c) migdal usa `air14` con salti **esattamente nulli** e γ≡1.4 ⇒ l'intera preoccupazione T_mid è **strutturalmente assente** dal percorso anulare/Broyden; (d) il sorgente FLINT È nel repo (submodule): interpolazione **lineare a tratti C⁰ con ginocchio a ogni Kelvin intero**, e `dG=cp/T` NON è la derivata della s⁰ interpolata; (e) l'iterazione sull'angolo di parete alla gola **non è una secante** ma una **falsa posizione a estremo congelato**, quindi convergenza **lineare**, e a esaurimento accetta incondizionatamente sovrascrivendo Me → verdetto ILL-POSED nel regime nominato; (f) `Interior_m` con y<0 ritorna uno stato **tutto-zeri senza flag**, e p=ρ=q=0 alimenta poi sqrt(γp/ρ)=0/0 → P1 confermato; (g) **RIPRODUCIBILITÀ**: `thermo_plug.dat` e `plug.plt` NON esistono nel tree (`.gitignore` esclude `thermo/`), quindi `CASES/plugnoz` — caso di **produzione attivo in CTest** — non è riproducibile dal repository | CHIUSA |
| C2 | Case space esaustivo per MOC-16..28 + mappa stencil per fase | claims-convergence |

## D. ESEGUIBILI ORA CON UN RUN STRUMENTATO (la patch ESISTE già)

La patch `RAW_geno_audit_instrumentation_2026-08-13.patch` è applicata nel
working tree di GENO (contatori DIAG_* + una variante algoritmica AUDIT VARIANT
B da rimuovere prima di misurare il comportamento nominale). Un solo run
strumentato su s3 chiude TUTTI i dubbi qui sotto. **Unico blocco: coordinamento
— la build su s3 è condivisa con le altre sessioni parallele in corso.**

| # | Dubbio | Esperimento | Falsificatore |
|---|---|---|---|
| D1 | Quante celle escono al cap icor senza convergere (7 kernel Ch.17 + Ch.16) | contatore di uscita a iter==icor per classe di cella | qualunque conteggio non nullo su un caso di produzione falsifica "campo converso" |
| D2 | Popolazione v<0 nel kernel migdal (dimensiona il criterio con RHS firmato) | istogramma del segno di v nelle celle Ch.16 | conteggio non nullo ⇒ esaurimento silenzioso garantito in produzione |
| ~~D3~~ | **CHIUSO 2026-08-13 SENZA NUOVO RUN — la prova era GIÀ SU DISCO.** `GENO/docs/analisi_drift_portata_ch17.md` §"La prova empirica" contiene un log strumentato di una sessione precedente (idealnoz Ch.17, colonna 511, righe j=27 e j=28): `SL kseg=1 tf=0.00000 yfoot=1.0085882 col1y=1.0077696 col2y=1.0069965`. Il piede cade **SOPRA la parete**, fuori dal segmento; `t_foot` è clampato a 0 e lo stato del piede (ρ3,V3,p3,θ3) diventa **quello della PARETE**, non del campo interno, corrompendo ρ4 e q4 via isentropa+Bernoulli. **Il clamp persiste a TUTTE le passate del PC.** CONSEGUENZA: la condizione del flag (`k_seg==1 .and. t_foot<0`) è soddisfatta ⇒ `foot_clamped` SPARA in produzione ⇒ ma FASE 2 non lo legge mai (flag azzerato da FASE 1) ⇒ **la correzione che il codice prevede per esattamente questo evento non avviene**. La rete di sicurezza scollegata ha ora un **evento di produzione documentato che avrebbe dovuto intercettare**. | — |
| D4 | Flip di N_sub fra passate del PC | log di N_sub per passata; celle con flip dopo la 2ª | floor di errV ≈5e-5 invece di 1e-8 |
| D5 | Toggle di axis_mode fra passate (sistema commutato) | contatore di cambio ramo | qualunque conteggio non nullo prova che il punto fisso non esiste per quelle celle |
| D6 | kgrid(0,0): le due gambe coincidono dopo un re-anchor? | stampa della differenza prima della sovrascrittura, caso con re-expansion | differenza > tolleranza ⇒ cella d'angolo interpola fra due stati incoerenti |
| D7 | Il P0 sulla spinta: conferma diretta | snapshot/restore di perf%f + ri-run | delta atteso = +7.27e3 N (tocnoz), +2.33e4 N (defnoz) |
| D8 | Residuo Broyden a gradini | scansione di F su una retta per la radice, passo 1e-3·da, log di Nv e N_sub | un salto >1e-5 in M o θ nell'intervallo |
| D9 | Budget di bisezione in solve_T_from_entropy (margine 1.05×) | max(it) sui casi | max(it) > 45 |
| D10 | throatExpansion accetta in silenzio a iter>30? | log di iter e |M−Me| all'uscita | una sola uscita con iter>30 = target Me riscritto da un'iterazione non conversa |
| D11 | Estrapolazione di parete: |frac| quanto esce | log di frac in inwall upper/lower | |frac|>2 su un caso di produzione |
| D12 | Clamp V²≤0: scatta nel path profilo? | contatore + aggiunta di `.not.(q>0)` al guard di Profile_m | uno scatto ⇒ stato non fisico finito entra nell'integrale di massa e nella parete |
| D13 | **Chi ha davvero rimosso il deficit 9e-4 di N-26?** Il fix 704b8c1 ha cambiato DUE meccanismi insieme (ricostruzione on-manifold del piede + bracket search esatta): l'attribuzione causale non è mai stata bisezionata | TWIN BISEZIONATO su tocnoz_gen_flint: (a) build con SOLO `foot_state_from_invariants` e la vecchia stima del piede; (b) build con SOLO la bracket search e il lerp di primitive; misurare in entrambe il deficit di massa cumulato lungo la colonna e l'esito wall-recede | se (a) rimuove il 9e-4 e (b) no ⇒ il registro ha ragione e il commento nel codice è una narrazione sbagliata; se (b) rimuove e (a) no ⇒ il registro attribuisce la causa sbagliata (e la classe N-26 sarebbe un difetto di ricerca del piede, non termodinamico); se **entrambi** contribuiscono ⇒ il fallback di :177-184 conserva una frazione MISURATA del difetto storico, e la sua attuale classificazione come "tie-break" è falsa |

## D-bis. ESITO DEL RED TEAM SUI 16 FINDING DI RECORD (2026-08-13, 5 lenti + giudice)

**Rejector seminato: 2/2 uccisi da TUTTE E CINQUE le lenti.** Le due claim
fabbricate (Eulero esplicito nella curva di Rao; media aritmetica dei raggi
nella portata) sono state verificate false dal giudice sul codice: la curva di
Rao usa un **midpoint iterato doppiamente annidato** (trapezio implicito,
second'ordine), e `massflow` pesa **ogni estremo col proprio raggio**. Nessuna
lente squalificata per falsi positivi.

**MA la calibrazione è fallita nell'altra direzione**: la lente di deflazione
ha ucciso F08 (che il giudice ha poi provato VERO) e ha marcato WEAKENED 14
finding su 16 in modo quasi uniforme — firma di uno sconto costante applicato
senza leggere i casi. Il giudice ha scontato quei verdetti e ri-derivato le
severità da sé. **Lezione di metodo: il canary misura solo i falsi positivi;
serve un secondo seme per i falsi negativi** (un finding vero, noto, iniettato
per vedere se la lente lo uccide).

| Finding | Esito | Correzione rispetto a quanto avevo riportato |
|---|---|---|
| F01 spinta doppio-contata | **CONFERMATO** e sotto-valutato dall'attacco | **I NUMERI (+7.27e3 N / +2.33e4 N) NON sono provati staticamente**: li avevo presentati come misurati, il red team li dichiara UNDECIDABLE e chiede un diff strumentato. Ma trova evidenza che l'audit non aveva usato: **il gemello anulare fa già `f_save`/restore** — quindi il rollback ESISTE nel modulo fratello: è un'omissione fra due gemelli, non una scelta |
| F02 criterio con RHS firmato | **CONFERMATO ma RISTRETTO** | **La mia raggiungibilità era SBAGLIATA**: la famiglia inferiore va incondizionatamente a Ch.17 (nessun fallback Ch.16), quindi `InverseWall_m` NON è vivo lì. Ciò che è vivo: `v→0` vicino ad asse e uscita sui casi `moc_gen=.false.`. Corroborazione decisiva mancata dall'audit: **`DirectWall_m` ha lo STESSO test scritto correttamente con `abs()`** ⇒ "intenzionale" non è una difesa |
| F03 loop senza cap | CONFERMATO latente | Mitigazione mancata dall'audit: `xa` non è reset per passata, quindi da iter≥1 il loop gira una volta sola ⇒ rischio confinato a iter==0 |
| F04 target Me sovrascritto | **CONFERMATO senza qualifiche** | — |
| F11 criterio cieco al piede | **UCCISO da tutte e cinque le lenti** | Era un mio P1: cade |
| F13 kgrid(0,0) doppia scrittura | **UCCISO** (4 lenti su 5) | Era un mio P1: cade |
| F08 rete di sicurezza morta | ucciso dalla lente correttezza, ma **provato VERO dal giudice** | Sopravvive |

## D-ter. LOOP-UNTIL-DRY SUI MODULI NON COPERTI — 35 finding, ma DRYNESS FALSA

**AVVERTENZA SUI NUMERI DELLA CAMPAGNA STESSA**: il workflow riporta
`rounds:3, dry_rounds:2, survivors:35`. **Tutti e tre i numeri sono
contaminati dal limite di sessione**: gli 8 finder dei round 2 e 3 sono
FALLITI (non hanno trovato zero: non sono girati), e un agente fallito
restituisce lista vuota, che il contatore ha letto come "round secco".
Quindi la convergenza a secco **non è avvenuta**: è un artefatto. Idem per
"35 survivors": 48 verificatori su 87 agenti sono falliti, quindi la maggior
parte dei finding non è stata sottoposta ad attacco. Solo l'agente di chiusura
ha aggiudicato ciò che poteva, ribaltando quattro verdetti sull'evidenza.
**Lezione**: un contatore di dryness deve distinguere "lista vuota" da
"agente fallito", altrimenti un limite di quota si traveste da esaurimento.
Da riparare nello script prima del resume.

**Finding nuovi rilevanti (moduli mai auditati prima), dal raw su file:**
- `Extension_m` (tipo 6): `j2` è `intent(inout)` e viene **monotonamente
  ridotto** dalle marce interne; al ritorno vale la lunghezza dell'ULTIMA
  colonna, e i writer lo usano per TUTTE ⇒ ogni colonna precedente, kernel TOC
  incluso, è **troncata nei file di output**. Caso degenere: il loop jet può
  lasciare `j2=0` ⇒ **file di campo scritti vuoti con exit code 0**. Difetto
  strutturale sottostante: l'estensione produce un campo **ragged** e il
  contratto dei writer è rettangolare — nessun singolo j2 è corretto.
- `Extension_m`: tutte e tre le uscite della bisezione (target raggiunto,
  collasso dei bound, budget esaurito) cadono nella stessa stampa
  **"EXT: converged"**, e su una di esse `deviaz` **non è mai assegnata**
  (stampa una variabile indefinita). Nessun argomento di stato: il chiamante
  non può sapere.
- `Extension_m`: il restart dopo la guardia backward **mescola livelli di
  colonna** — il triangolo MoC viene costruito con due livelli caratteristici
  diversi. Silenzioso, campo sbagliato, non NaN.
- **Ch.16 `inter_solve` con y<0 ⇒ punto AVVELENATO**: il dispatch pone q=0,
  θ=atan2(0,0)=0 e chiama la chiusura con q=0, che converge a uno **stato di
  ristagno con M=0**; lo stencil successivo calcola `asin(1/M)` = `asin(Inf)`
  = **NaN**, che si propaga. Su **17 call-site del dispatch, solo 2 reagiscono**
  (l'error stop della gola e la degradazione graziosa di Extension); gli altri
  15 memorizzano il punto così com'è. E il NaN **non è rilevabile dalla suite**:
  `run_case.sh` esclude per nome gli output binari dallo scan NaN.
- **Guardia `huge()` sui coefficienti angolari: MORTA e SBAGLIATA.** `tan()` di
  un double finito è limitato da ~1.6e16, mentre `huge`=1.8e308: la condizione
  non può mai essere vera. E il ramo che proteggerebbe ricostruisce `rm` (un
  coefficiente C−, basato su pt1) usando **pt2**. Difetto latente P3, ma è una
  **trappola**: chi ripara la soglia eredita una formula sbagliata al primo
  scatto.
- **Criterio con RHS firmato: RISTRETTO ULTERIORMENTE** (terza revisione).
  Poiché u>0 in tutto il dominio supersonico, si rompe **solo** il test su v; e
  quando si rompe, il loop gira fino a `icor` e restituisce l'iterata
  `icor`-esima, che è **PIÙ accurata**, non sbagliata. Il difetto reale non è
  l'accuratezza ma che **il criterio applicato non è quello dichiarato** e la
  routine non sa distinguere convergenza da esaurimento. Corroborazione: DUE
  routine sorelle nello stesso codebase lo scrivono correttamente con `abs()`.
- Altri finding nel raw (non verificati per il limite): Simpson con n pari che
  perde l'ultimo pannello; divisione per zero in un rendimento migdal; equazioni
  normali singolari nello smoothing; `rialloca` che raddoppia entrambe le
  dimensioni; restart senza cap in `leggeAree`; range di validità FLINT e NASA
  presi dalla prima specie; parità NI non imposta al tipo 9; match delle specie
  **posizionale senza controllo del nome**; file di dimensioni condiviso fra
  scritture.

## E. APERTI SENZA ESPERIMENTO ANCORA NOMINATO
(sezione da tenere VUOTA: se un dubbio finisce qui, o gli si dà un esperimento
o lo si chiude con derivazione. Al 2026-08-13: vuota.)

## F. RITRATTAZIONI (claim miei, ritirati dopo lettura diretta sotto pressione utente)

**F-R1 — "il lettore di IVL da file proietta i dati importati sull'isentropa
globale": RITIRATO.** `IO_m.f90:715-720` ha un ramo esplicito: se il file
contiene `p` e `rho` li prende DAL FILE e ricava γ dall'equazione di stato
(commento in-code: "no isentropic expansion assumed"). In quel percorso ogni
punto porta il proprio stato ⇒ entropia e ristagno **possono variare da
streamline a streamline**: genuinamente rotazionale. La proiezione avviene solo
nel ramo di fallback (p e rho ASSENTI dal file), dove peraltro è inevitabile:
con u,v soltanto lo stato non è determinato.
**Formulazione corretta del difetto residuo**: il fallback è **SILENZIOSO** —
nessun avviso, nessun flag ⇒ il chiamante non può sapere quale ramo è scattato,
e ottiene un campo omoentropico credendo di aver importato dati rotazionali
(basta che le variabili abbiano nomi diversi da quelli cercati, o che ce ne sia
una sola delle due). Difetto di TRASPARENZA, riparazione = una riga di avviso.
Resta separato e non verificato: il match delle variabili è **posizionale** per
x,y,u,v e per nome solo per p,rho.
Nota di scopo: quel canale di import esiste per il **tipo 3**; per gli altri la
IVL nasce da Sauer, omoentropica per costruzione. Quindi **la strada per far
entrare dati rotazionali nel Ch.17 ESISTE ed è corretta**, ma passa da un solo
tipo e non è mai stata esercitata con entropia variabile.

**F-R2 — "la contabilità di prestazione ricostruisce lo stato dalla sola
velocità sul percorso Ch.17": RITIRATO.** Tutti i 18 call-site di
`thrust_solve` compaiono **in coppia**, come i due rami di un `if` sul backend:
il ramo Ch.17 passa **sempre** la pressione del solutore (`pt4%p` /
`sol%p(1,i)`), solo il Ch.16 la ricostruisce. Vale per gola, kernel anulare,
profilo ideale/TIC/TOC e le due metà migdal. `massflow` riceve rho e q **come
argomenti** dai punti della soluzione. Quindi **nessuno stato di parete è
ricostruito dalla sola velocità in Ch.17**.
Resta, ed è di natura diversa: `td%solve_gcost` viene chiamata all'inizio della
routine per la spinta ideale 1-D a γ costante, che è il **DENOMINATORE** dei
rendimenti. È un riferimento ideale, non uno stato del campo: legittimo per
definizione, purché si sappia che etaf/etai sono rapporti a un riferimento
γ-costante anche su campo a γ variabile. Nota di interpretazione, non difetto.

**REGOLA DERIVATA DA ENTRAMBE (vale per il resto dell'audit)**: la presenza di
una costruzione sospetta in un file NON è un difetto finché non si è verificato
**quale ramo la produzione percorre** e **con quali argomenti i chiamanti la
invocano**. Entrambe le ritrattazioni nascono dalla stessa scorciatoia: avere
visto una chiamata e averne inferito il comportamento senza seguire i call-site.
Sono errori di classe "correttezza tecnica" nella tassonomia del red team.

## NOTE DI PROCESSO
- Due miei claim di questa sessione sono stati SBAGLIATI e corretti: "root
  cause di N-26 ancora viva" (falsa: quella di record è chiusa) e la tassonomia
  a 4 pattern (imposta da me, non derivata). Entrambi trovati solo tornando a
  verificare di prima mano: nessun verdetto di questa campagna è esente.
- Il ramo cross-stream della ricostruzione del piede (t·(s_b−s_a)) risulta MAI
  esercitato secondo il registro GENO: la riparazione N-26 è validata SOLO dove
  coincide col lerp banale. Questo è un dubbio di classe D (serve un caso
  rotazionale reale), non chiudibile leggendo.
