# AGNOSTIC_GOAL_REVIEW — Revisione agnostica di obiettivo, sessione 2 S-PRES

Revisore agnostico di obiettivo, 2026-08-23 (rilancio: il revisore di fine
sessione 1 non è mai atterrato su file). **Stadio di confronto**: il piano
d'esecuzione della sessione 2 (ordine dei lavori fissato dall'utente:
W-A..W-D → critic → promozione → storyboard-gate → Blocco 2/3) confrontato
contro (i) l'obiettivo di record a due teste — (a) ATLAS FIDATO docs/atlas/,
(b) DECK ESA 60' a ~2-3 settimane — come ridefinito dall'utente 2026-08-23
nel checkpoint; (ii) i documenti letti INTEGRALI in questa finestra:
SESSION_STATE_checkpoint.md (con C-1..C-7, C-1bis/C-1ter, C-3bis/C-3ter),
ATLAS_RESEARCH_DESIGN_v2.md (658 righe: §Q/§T/§C/§M/§CH/§N/§D/§W/§L/§F),
VERIFY_DESIGN_v2.md (PRONTO-PER-ESECUZIONE + V-N1/V-N2), STORYBOARD.md,
MESSAGE_ARCHITECTURE.md; (iii) GRAPH_VIZ_SPEC.md (lettura mirata, integrale
di fatto: 74 righe). **Arco di consumo**: l'orchestratore applica le
migliorie G-* PRIMA di lanciare W-A; le sezioni RISCHI e FINDINGS armano i
checkpoint di metà corsa e le decisioni utente. Vincolo rispettato: nessuna
riapertura del design v2 (i 16 finding e la struttura albero/matrice/
template NON sono ri-litigati; le 2 NOTE del verifier assunte vere).

---

## MIGLIORIE (ordinate per rapporto valore/costo)

### G-1 — TABELLA DI ATTERRAGGIO C-1..C-7 → onde/brief (VINCOLANTE)
**Cosa**: il design v2 è stato scritto PRIMA che le correzioni concettuali
C-1..C-7 (+C-1bis/C-1ter, C-3bis/C-3ter) diventassero di record nel
checkpoint: nessun brief d'onda le nomina. Prima di lanciare W-A,
l'orchestratore scrive nei brief una tabella di routing esplicita, con
puntatore VERBATIM alle righe del checkpoint (mai parafrasi a memoria —
navigation-first):

| correzione | atterra in | brief che la porta |
|---|---|---|
| C-1 (terza linea lineage Stechmann→Harroun→KP-EAP→Fievisohn→noi) | lineage ledger + sottosezione ANTENATI DIRETTI per nodo | G-2 + G-6 |
| C-1bis (imposed-detonation-BC = antenato del contratto Γ_d; T-DISC come riparazione teorematica del loro BC p-only; Γ_d ≠ "the throat", stazione supersonica-con-margine; sonic line corrugata = perché del margine) | CH10 riga K + lineage ledger riga 4 | B2 (W-B.1), con le righe del checkpoint citate nel brief |
| C-1ter (lineage-sweep matrix componenti×corpus) | operazione dedicata pre-writer | G-2 |
| C-2 (rung discipline: quasi-1D = oracolo SENZA contouring, mai "1-DOF nozzle case"; non-sequitur T1c→gap di contouring vincolato BANDITO; Humphreys ×2.45 pertinente alle design variables a vincoli fissi) | CH1/CH3 (B3), CH8 (B6) + checklist refuter W-C | brief B3/B6 + G-7 |
| C-3/C-3bis/C-3ter (frame tre-design; gerarchia (A)>(B) a vincoli fissi SEMPRE col tallone (J); death scenario = due fallimenti indipendenti; twin-first) | CH3 (B3), CH6 (B5), CH8 (B6) | brief B3/B5/B6 + G-7 |
| C-4 (J = ∫F dµ, forma wall ≡ Rao control-surface; identità di decomposizione = MINT CANDIDATE F-2) | mint/MINT-PENDING prima dei writer | G-6 |
| C-5 (SOTA solo con standard nominato) | già esecutivo in §C + lint 6 | nessun delta (verificato conforme) |
| C-6 (effort: giudizio = inherit max) | già esecutivo in §W | nessun delta (verificato conforme) |
| C-7 ("il campo" sempre istanziato: PKU/NUAA/KIT-Aoyama/NASA-Glenn/Purdue con paper) | capitoli CH5 (B5) + deck | brief B5 + checklist G-7 |

**Perché serve l'obiettivo**: (a) e (b) insieme — senza routing scritto, le
correzioni vincolanti vivono solo nel checkpoint e le onde possono
atterrare capitoli che le violano (il refuter le troverebbe, ma al costo di
un round in più: il routing è più economico della riparazione).
**Dove atterra**: preambolo dei brief di W-A/W-B, mezz'ora orchestratore.
**Costo**: ~trascurabile (solo orchestratore). Valore/costo massimo.

### G-2 — LINEAGE-SWEEP come slot dedicato "W-B.0", non dentro i writer (VINCOLANTE)
**Cosa**: l'ordine di sessione mette la LINEAGE-SWEEP MATRIX (C-1ter) "in
testa a W-B.1". Eseguirla DENTRO i 7 writer la spalma su 7 brief e viola lo
spirito file-disgiunti (tutti scriverebbero pezzi di lineage). Proposta
applicativa (nessun cambio di design: è assegnazione d'onda, materia
dell'orchestratore come V-N2):
- **W-B.0**: 1-2 slot GIUDIZIO (inherit max, C-6) che compilano UN file
  `LINEAGE_SWEEP_MATRIX.md` nelle raws: ~15 componenti strutturali
  (l'elenco del checkpoint C-1ter è già la riga di partenza) × corpus letto
  (49 READ-INTEGRAL + partials). Con 2 slot: split del corpus a metà,
  righe-paper disgiunte.
- **Disciplina di cella**: ogni cella ≤ 3 righe ("procedura isomorfa/
  antenata? come la chiamano? cosa manca vs noi"); vuota SOLO se dichiarata
  dopo check; strategia di lettura dichiarata nel brief: litmap/censimenti/
  registry PRIMA, apertura del PDF solo su sospetto di isomorfismo
  (context-discipline) — il corpus è GIÀ letto, la matrice è
  ri-interrogazione strutturale, non ri-lettura.
- **Refuter sulle celle** (vuote: "davvero nessuno?"; piene: "isomorfismo
  genuino o superficiale?"): assegnato a C5 di W-C con mandato esteso (C5 è
  già lo slot che cammina storie e posizionamenti — la lineage è
  posizionamento), o slot C6 nuovo se il carico sfora.
- **Due duty puntuali agganciate** (entrambe di record nel checkpoint,
  nessuna casa nelle onde v2): (i) verifica-fonte Harroun 2021 "quale peso
  e quale denominatore" (lettura mirata, il paper è su disco — anchor
  H21-F11 esistente); (ii) Fievisohn 2018 W-09 procurement RAISED: sweep
  del disco locale PRIMA (lezione litreview-verification-protocol), esito
  nel log di W-A; se assente, la colonna Fievisohn della matrice è
  dichiarata [REP]-bounded, mai riempita da riassunti altrui.
- **Output**: LINEAGE_LEDGER completo (le 4 righe già trovate dall'utente +
  ciò che la matrice fa emergere), consumato dai writer W-B.1 (ANTENATI
  DIRETTI per nodo) e dallo storyboard (C6/C7-bis-pre).
**Perché**: (a) — la lineage è la falla trovata dall'utente TRE volte
(C-1, C-1bis, C-1ter): il rischio più alto di "atlas non fidato" è qui;
(b) — il fronte Q&A Purdue/Heister (C7-bis-pre) si difende solo con la
matrice fatta. **Dove**: nuovo round W-B.0 tra W-A e W-B.1 (temporalmente
disgiunto, file proprio). **Costo**: ~150-250k token + delta refuter; è IL
costo nuovo della sessione, e va pagato — ma col cap di cella e la
strategia niente-ri-lettura resta un round, non una campagna.

### G-3 — CALENDARIO ANCORATO: freeze-date atlas + tripwire (VINCOLANTE)
**Cosa**: dichiarare ORA, nel log di apertura sessione: (i) **target
freeze atlas = 2026-08-30** (7 giorni; milestone deck ~10-15 settembre ⇒
almeno il 50-60% del calendario resta al deck: authoring pipeline, Blocco 2,
prove); (ii) budget per onda = quelli di §W presi come CAP e non come stima
(W-A ≤220k; W-B.0 ≤250k; W-B.1 ≤600k; W-B.2 ≤240k; W-C ≤400k; W-D ≤120k);
(iii) **tripwire**: onda oltre 1.5× il cap, o falsificatore di design
F-des-1/2 sparato, o fine-giornata-3 senza W-B.1 atterrata ⇒ STOP e
presentazione all'utente della decisione di split (FINDING F-1 sotto), mai
prosecuzione silenziosa; (iv) budget DICHIARATO per il lavoro post-atlas
oggi non prezzato da nessun documento: authoring deck ~400-700k (41+ slide
specs, crop extract_figs, strip-eq, note, script grafo), Blocco 2
~300-500k (retro-audit+comms+Q&A red-team+backup). **Perché**: (b) — il
vincolo esplicito dell'ordine di sessione ("time-box l'atlas e proteggi il
tempo-deck") oggi non ha NESSUN numero su file: senza date e tripwire il
piano d'onde è strutturalmente capace di mangiare le 3 settimane (vedi
RISCHI). **Dove**: log di apertura + preambolo brief. **Costo**: zero.

### G-4 — DECK-FEED per capitolo: il ponte atlas→storyboard reso meccanico
**Cosa**: ogni writer W-B.1 (e gli historian per la sola parte storia-che-
serve-al-deck, es. genealogia C6) chiude il proprio capitolo con un blocco
`## DECK FEED` di 5-10 righe: le asserzioni candidate-slide del capitolo,
ciascuna in frase piena (assertion-evidence, asse §C-6) + ancora + classe.
Lo storyboard v3 al passo (4) si COMPILA dai feed invece di ri-leggere 10
capitoli interi; il retro-audit eredita ancore già in formato slide.
**Perché**: (b) — è l'arco di consumo atlas→deck reso operativo: oggi il
piano dice "storyboard v3 scritto DALL'atlas" ma non come; senza feed il
passo (4) costa una ri-lettura integrale (~10 capitoli × writer nuovo).
**Dove**: una riga in ogni brief W-B.1/W-B.2. **Costo**: quasi nullo in
scrittura, risparmio stimato 100-200k al passo (4).

### G-5 — V-N1/V-N2 applicate in-line all'apertura di W-A (VINCOLANTE, già raccomandate dal verifier)
**Cosa**: (i) fix cosmetico "18"→"19 slot" nella riga totale §W (V-N1);
(ii) esecutore materiale della disposizione findings di W-C nominato al
lancio (V-N2) — proposta: i refuter stessi compilano le tabelle di
disposizione nel loro round (un solo writer per file di refutazione, regola
d'onda già copre). **Perché**: (a) — igiene del contratto d'onda; il
verifier le ha già dichiarate applicabili senza ri-verifica. **Dove**:
apertura W-A. **Costo**: zero.

### G-6 — ANTENATI DIRETTI senza toccare il conteggio-template + mint C-4 prima dei writer
**Cosa**: C-1 ordina una sottosezione obbligatoria "ANTENATI DIRETTI
(lineage claim)" per nodo e il lint "novelty senza riga antenati =
violazione". Esecuzione senza riaprire il design: (i) la sottosezione vive
DENTRO la sezione 3 LA PROPOSTA del template (§T resta a 8 sezioni; la
proposta è esattamente il luogo del claim di novità); (ii) il lint entra
come clausola aggiuntiva del lint 5 (che già verifica il template),
registrata nel log come esecuzione di C-1, non meta-design; (iii) il MINT
CANDIDATE C-4 (identità di decomposizione J_exact = ∫F_true dµ, F-2) viene
risolto dall'orchestratore in W-A accanto alla decisione A4 (stessa classe:
"mint prima dei writer o eccezione dichiarata"): o riga a registro con id
stabile, o dicitura MINT-PENDING uniforme che tutti i writer citano
identica. Il registry row "methodology lineage-recognition gap" (C-1) si
minta alla chiusura come già ordinato. **Perché**: (a) — senza id stabile i
writer inventerebbero 7 diciture diverse per lo stesso oggetto (R4:
retro-propagazione nella stessa sessione). **Dove**: W-A (orchestratore) +
template-clausola nei brief. **Costo**: piccolo (< 20k).

### G-7 — CHECKLIST-GUARDIE unica per refuter W-C e retro-audit Blocco 2
**Cosa**: una checklist scritta UNA volta e consumata due volte (W-C sui
capitoli, Blocco 2 sul deck): (1) gerarchia C-3bis mai enunciata senza il
tallone (J) (C-3ter: "state the hierarchy WITH the (J) heel, never
without"); (2) non-sequitur T1c→gap di contouring vincolato = BANDITO
(C-2); il rung quasi-1D mai chiamato "1-DOF nozzle case"; (3) "il campo"
sempre istanziato con gruppi+paper (C-7); (4) SOTA solo con asse §C o
query-bound (già lint 6 — la checklist lo cita, non lo duplica); (5) D-44
mai adequacy; (6) P34 stage dichiarato; (7) best-of-sweep ≠ argmax; (8)
novità query-bounded. **Perché**: (a)+(b) — le guardie oggi sono sparse su
checkpoint/message-architecture/design; una sorgente unica evita che il
retro-audit del deck ri-derivi la lista (e la divergenza tra le due liste
sarebbe essa stessa un difetto di trust). **Dove**: file breve nelle raws,
citato dai brief W-C e dal protocollo Blocco 2. **Costo**: ~mezz'ora
orchestratore.

### G-8 — Retro-audit a eredità dichiarata (economia del Blocco 2)
**Cosa**: dichiarare nel protocollo del retro-audit: un claim-slide la cui
ancora punta a una riga d'atlas già camminata dai lint 3/4/6 e dal refuter
W-C eredita quel walk attraverso l'arco slide→atlas (che il retro-audit
verifica); il walk FRESCO fino alla sorgente si esegue solo per i claim
deck-nativi (crop e numeri dei paper CT-6, composizioni narrative, numeri
di time-boxing, kicker B1). Il ROBUSTNESS VERDICT conta separatamente
walked-fresh / walked-inherited / reduced / findings — nessun
ammorbidimento: l'eredità È un cammino alla sorgente, per arco verificato,
e viene dichiarata tale nel log (coerente con [V2-R16], che già alimenta il
retro-audit dai lint). **Perché**: (b) — il retro-audit 100% dei
load-bearing su ~41 slide senza eredità costerebbe un round W-C-size
duplicato; l'atlas esiste esattamente per questo. **Dove**: protocollo
Blocco 2 (scritto ora, una riga nel piano). **Costo**: negativo (risparmio
stimato 150-300k).

### G-9 — De-risk anticipato del grafo camminabile
**Cosa**: lo script di estrazione JSON nodi/archi dalla pipeline map con
assert 62/17/45 + un prototipo di render L0 (matplotlib, spec
GRAPH_VIZ_SPEC) si costruiscono come slot MECCANICO (effort ridotto
dichiarato, SR-9) in parallelo alle onde atlas — file nuovi, zero
conflitto; la sorgente (mappa refereed) è frozen. **Perché**: (b) — il
grafo è la promessa visiva più rischiosa del deck (3 layer, leggibilità a
3 m, split Stage 6 in 2 pannelli): scoprire un problema di layout in
settimana-3 è il classico buco di calendario; il round-trip test Blocco 0
insegna che i rischi-veicolo si scaricano PRESTO. **Dove**: slot meccanico
lanciabile da subito (W-A window). **Costo**: ~30-60k.

### G-10 — Agenda delle decisioni utente con impatto-calendario dichiarato
**Cosa**: le due decisioni pendenti si presentano in momenti nominati e CON
la stima d'impatto: (i) **twin PB-2 (a)/(b) a vincoli identici** — al GATE
STORYBOARD (lo storyboard C7-ter tiene già aperta la biforcazione "stato
onesto vs numero del twin"); la presentazione include costo macchina/
sessioni e la **latest-start date** (~1 settembre) oltre la quale il twin
non entra nel deck e la slide resta nella forma onesta già scritta; (ii)
**S-5F path A/B/C + priorità C51** — idem al gate (tocca CH7 §3 / cella
E-v e la roadmap C17). Nessuna delle due blocca le onde: i capitoli
scrivono lo stato onesto con decisione-pendente + owner (il template §5 lo
prevede già). **Perché**: (b) — "al momento giusto" senza data diventa "al
momento sbagliato"; il twin ordinato tardi è il rischio n.1 di sforamento.
**Dove**: agenda orchestratore, gate storyboard. **Costo**: zero.

### G-11 — Protocollo bounded per le query in-onda
**Cosa**: le celle che ordinano query da eseguire in onda (G-ii/G-iii,
H-iii, J-iii, C8-note) ricevono nei brief un protocollo chiuso: testo della
query citato nel capitolo + perimetro fisso (registry 174 + litmap + i
paper P-A..P-D già letti) + esito NOT-FOUND(q) o refs + STOP — nessun
procurement in-onda (unica eccezione: Fievisohn, già pre-approvata in G-2),
nessuna escalation di ricerca senza decisione a confine d'onda. **Perché**:
(a) mantiene i claim search-proven; (b) chiude la porta al rabbit-hole di
ricerca dentro i writer. **Dove**: brief B1/B3/B6 + regola d'onda.
**Costo**: zero (è un cap, non un lavoro).

---

## RISCHI DI CALENDARIO

Il quadro: milestone ~10-15 settembre (2-3 settimane). Consumato finora
dalla ricostruzione: Wave 1 ~1.26M token per 6 capitoli (checkpoint). Il
piano d'onde v2 dichiara ~1.1-1.6M; con W-B.0 (G-2) ~1.3-1.85M. A valle
restano: critic finale, promozione, storyboard v3, gate utente, authoring
pipeline (~41 slide + grafo + crop), Blocco 2 (retro-audit + comms + Q&A
red-team + backup deck), Blocco 3, prove orali. Rischi nominati:

- **RC-1 (strutturale): il piano d'onde non ha date, solo token.** 5 round
  seriali in 4 onde + W-B.0 + critic = ~7 barriere di sincronizzazione;
  ogni barriera è un confine di sessione potenziale. Mitigazione = G-3
  (freeze 08-30, cap per onda, tripwire 1.5×). Criterio di taglio se il
  tripwire spara: FINDING F-1 all'utente (sotto), mai prosecuzione muta.
- **RC-2: le 30 celle SCOPERTE non sono equi-costose.** Le righe J/K (2
  capitoli NUOVI interi) + riga G/H (2 sezioni nuove) portano quasi tutto
  il peso; le query in-onda (G-11) e la matrice lineage (G-2) sono i due
  amplificatori. Mitigazione: cap di cella (≤3 righe) e protocollo bounded;
  profondità = contratto dello slot (direttiva roads-insertion-matrix: no
  over-math).
- **RC-3: W-B.2 (storia) è il lavoro più affamato di letture** (M0 +
  PROGRESS_ARCHIVE + raws per 10 capitoli). Mitigazione già nel design
  (HISTORIAN_INDEX A5 + budget proprio 160-240k): il budget si tiene come
  CAP; l'argomento che a budget esaurito non ha ancora ancora di storia
  chiude onesto in ramo (c)/"doppia prova: ASSENTE"=FINDING (previsto da
  F-des-3), MAI scavo oltre-cap.
- **RC-4: il lavoro post-atlas è oggi NON prezzato da alcun documento.**
  Authoring + Blocco 2 stimati qui ~700k-1.2M (G-3(iv)) e — più vincolante
  dei token — giorni di calendario con un gate utente in mezzo.
  Mitigazione: G-3 (≥50-60% del calendario protetto), G-4 (storyboard v3
  compilativo), G-8 (retro-audit a eredità), G-9 (grafo de-riskato).
- **RC-5: il twin PB-2, se ordinato, è una campagna di calcolo** dentro la
  finestra deck. Mitigazione: G-10 (latest-start ~01-09 dichiarata al
  gate; fallback = la forma onesta GIÀ scritta in C7-ter, costo zero).
- **Che cosa è differibile a DOPO il deck senza perdere il trust
  meccanico** (il trust = anchor-walk + 6 lint + refutazione, tutti
  in-window e non differibili): (1) upgrade delle celle NOT-FOUND via
  procurement nuovo (Tillyaeva 1975, deflated-continuation, Lipschitz-
  global — già PENDING-PROCUREMENT/eccezione per design); (2) le slide L1
  di backup oltre i nodi Q&A-mapped (template identico, compilazione
  meccanica); (3) l'inventario esteso dei rami (c) oltre la lista minima
  per CH-REF (la lista È obbligatoria, la sua prosa no); (4) la
  maintenance rule R3-extension da ratificare (già "at close" per il
  checkpoint). NON differibili: lint 1-6, refutazione W-C, anchor-walk
  delle storie, promozione con righe ADVISORY_INDEX/registry stessa
  finestra (R7).

Proposta di time-box concreta (giorni-lavoro dal 24-08): W-A + G-9 avvio =
0.5 g; W-B.0 = 0.5-1 g; W-B.1 = 1-1.5 g; W-B.2 = 0.5 g; W-C = 1 g; W-D +
critic + promozione = 0.5-1 g → **freeze atlas 29/30-08**; storyboard v3 +
gate utente = 30/31-08; authoring = 31-08→05-09; Blocco 2 = 05→09-09;
buffer + prove = 09→milestone. Ogni sforamento di casella = voce nel log,
due sforamenti consecutivi = tripwire G-3.

---

## FINDINGS (riaperture di design — SOLO per decisione utente)

### F-1 — Release a due timbri (pre-armato, NON applicato)
L'ordine dei lavori fissato è strettamente seriale: TUTTE le onde (incluse
storie W-B.2 e refutazione completa W-C) → critic → promozione → storyboard.
Se il tripwire G-3 spara (atlas non freezabile entro ~30-08), la
prosecuzione seriale mangia il tempo-deck in violazione del vincolo di
calendario dell'ordine stesso. **Frame alternativo nominato**: release a
due timbri — timbro CORE (W-A + W-B.0 + W-B.1 + W-C sui capitoli/sezioni
nuove + lint 3/4/6 sul perimetro deck-feeding) ⇒ storyboard v3 + avvio
authoring; timbro FULL (W-B.2 storie + C5 + lint 5 + inventario rami (c) +
promozione completa) atterra in parallelo all'authoring su file disgiunti
(le §6 STORIA non alimentano quasi nulla del deck: consumer principale =
testa (a)). Il trust meccanico resta integro perché NULLA si promuove a
docs/atlas/ senza il timbro FULL; solo lo storyboard parte prima. Decisione
utente, presentata SOLO se il tripwire spara; fino ad allora l'ordine
fissato resta l'ordine.

### F-2 — Nessun'altra riapertura necessaria
Le correzioni C-1..C-7 atterrano tutte nelle onde per via di brief (G-1,
G-2, G-6, G-7) senza toccare albero, matrice, template-conteggio o lint
oltre le clausole che l'utente stesso ha ordinato (C-1). Il design v2 +
verify reggono il confronto con l'obiettivo a due teste: la testa (a) è
servita dalla struttura, la testa (b) dagli archi §N/[V2-R16] — ciò che
mancava era SOLO il tessuto connettivo operativo (routing correzioni,
date, ponte deck-feed), che le G-* forniscono senza meta-design.

---

## VERDETTO

**GO-CON-MIGLIORIE.**

Vincolanti prima del lancio di W-A: **G-1** (routing C-1..C-7 nei brief),
**G-2** (lineage-sweep come W-B.0 dedicato + duty Harroun/Fievisohn),
**G-3** (freeze-date 30-08 + cap per onda + tripwire + budget post-atlas
dichiarato), **G-5** (V-N1/V-N2 in-line), **G-6** (ANTENATI DIRETTI in §3
+ mint C-4 in W-A), **G-7** (checklist-guardie unica W-C/Blocco-2).
Raccomandate forti: G-4 (deck-feed), G-8 (retro-audit a eredità), G-10
(agenda decisioni con latest-start twin), G-9 e G-11. Nessuna ostruzione:
l'unica riapertura potenziale (F-1, release a due timbri) è pre-armata come
decisione utente condizionata al tripwire, non necessaria oggi.
