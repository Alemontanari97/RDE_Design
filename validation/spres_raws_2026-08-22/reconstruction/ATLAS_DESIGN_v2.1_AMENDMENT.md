# ATLAS_DESIGN v2.1 — EMENDAMENTO PRE-LANCIO (ordine utente 2026-08-23)

Orchestratore S-PRES sessione 2, 2026-08-23. **Carrier**: iniezione utente
di record da S-PRES-1 (post-chiusura, addendum 0f8f88c): "PRIMA di lanciare
qualunque onda, esegui l'EMENDAMENTO v2.1 secondo le 5 migliorie del
review". **Stadio di confronto**: ATLAS_RESEARCH_DESIGN_v2.md (658 righe,
letto integrale in finestra) + VERIFY_DESIGN_v2.md (2 NOTE) confrontati
contro (i) le correzioni utente vincolanti del checkpoint (C-1..C-7,
C-1bis, C-1ter, C-3/C-3bis/C-3ter — posteriori al design: mtime 05:25 vs
05:06/05:14, finding materiale del review committato), (ii) il review
committato reconstruction/AGNOSTIC_GOAL_REVIEW.md (0f8f88c, letto
integrale), (iii) il secondo review AGNOSTIC_GOAL_REVIEW_S2_relaunch.md
(rilancio in-window avvenuto quando 0f8f88c non era ancora visibile
all'apertura; ora rinominato, deduplicato qui in §6). **Arco di consumo**:
le onde W-A..W-D leggono v2 COME EMENDATO da questo file; dopo la verifica
breve (§7) il design è FROZEN (§4). Questo file supersede v2 SOLO nei punti
qui elencati; tutto il resto di v2 resta di record invariato.

HEAD riconciliato in finestra: 0f8f88c = commit addendum [PIANO/R35],
autore = utente (git show misurato), contenuto = solo il file review.

==============================================================================
## §1 — CABLAGGIO DELLE CORREZIONI POSTERIORI (miglioria ①)

### 1a. Nuova onda W-B.0 — LINEAGE-SWEEP (C-1ter, MANDATORY)

Round dedicato TRA W-A e W-B.1 (temporalmente disgiunto, file propri):

- **Slot L1, L2 (giudizio, inherit max)**: compilano UN file
  `LINEAGE_SWEEP_MATRIX.md` nelle raws — matrice **15 componenti
  strutturali × corpus letto** (49 READ-INTEGRAL + 33 READ-PARTIAL,
  enumerati da comando in finestra; totale registry 174). Componenti =
  l'elenco C-1ter del checkpoint (:170-177): per-phase family; averaged
  functional; averaged wall conditions; weighted transversality;
  imposed-BC contract; periodic data class; quotient/wave-frame; mu
  measure; decomposition identity; per-phase marching; discrete adjoint;
  certificates; sector tournaments; truncation/p_b; monitors.
  Split del corpus a metà tra L1 e L2 (righe-paper disgiunte).
- **Triage a due livelli** (review committato, miglioria 1a): scan batch
  per componente sui materiali di lettura di record (litmap, censimenti,
  CH5, threat ledger, harvest, registry) → deep-check (apertura PDF
  mirata) SOLO sulle celle candidate a isomorfismo. Il corpus è GIÀ
  letto: la matrice è ri-interrogazione strutturale, non ri-lettura.
- **Disciplina di cella**: ≤3 righe ("procedura isomorfa/antenata? come
  la chiamano? cosa le manca vs noi"); cella vuota SOLO dichiarata dopo
  check ("checked: none"); mai riempita da riassunti altrui — colonna di
  un paper non su disco = dichiarata [REP]-bounded.
- **Refuter dedicato C6 (W-C, giudizio)**: attacca celle vuote ("davvero
  nessuno?") E piene ("isomorfismo genuino o superficiale?").
- **Due duty puntuali agganciate** (checkpoint C-1, nessuna casa in v2):
  (i) verifica-fonte Harroun 2021: QUALE peso e QUALE denominatore nel
  quasi-cycle-averaging (lettura mirata, paper su disco, anchor H21-F11)
  — esito nella matrice e in CH5; (ii) Fievisohn 2018 W-09: sweep del
  disco locale PRIMA di ogni claim (lezione litreview-protocol); se
  assente → colonna [REP]-bounded + procurement RAISED resta a registro.
- **Output**: `LINEAGE_LEDGER` COMPLETO (le 4 linee già trovate
  dall'utente: Stechmann→Harroun→KP-EAP→Fievisohn→noi; + imposed-BC
  C-1bis; + ciò che la matrice fa emergere), consumato da: writer W-B.1
  (sezione ANTENATI, 1b), storyboard (C6/C7-bis-pre), Q&A.

### 1b. Template §T a 9 SEZIONI — "ANTENATI DIRETTI (lineage claim)"

Nuova sezione obbligatoria **§3-bis ANTENATI DIRETTI** (dopo §3 LA
PROPOSTA, prima di §4): per ogni claim di novità del nodo, le righe di
lineage dal LINEAGE_LEDGER (antenato → cosa fa → cosa gli manca vs noi),
o la riga esplicita "ANTENATI: NOT-FOUND(q)" con query citata. Il
template conta ora **9 sezioni** (1, 2, 3, 3-bis, 4-8): la numerazione
3-bis PRESERVA la mappa celle→sezioni di v2 ((i)→§4+§5, (ii)→§2+§7(a),
(iii)→§2+§7(b), (iv)→§3, (v)→§5), che resta invariata; la cella (iv)
ora mappa a §3+§3-bis. I capitoli GIÀ scritti ricevono §3-bis dai writer
W-B.1 (per i capitoli assegnati) e — per i capitoli non toccati da
W-B.1 — da un incarico esplicito aggiunto al writer proprietario (v.
tabella slot §6e). [R-4 refuso corretto]

**CLAUSOLE DI SUPERSESSIONE TESTUALE su v2 [R-2]** (v2 resta su disco
non editato come storia; per ogni agente e per il linter meccanico D1
valgono queste sostituzioni OVUNQUE in v2): (a) "8 sezioni" (§T :163,
D2 :584 e ovunque) → **"9 sezioni (1, 2, 3, 3-bis, 4-8)"**; (b)
"N-A..N-P" (lint 5 :610 e ovunque) → **"N-A..N-P + N-Q"** (albero 22
nodi, riga Q in matrice); (c) "i 6 lint" (§L, D1 :581 e ovunque) →
**"gli 8 lint"** (i 6 di v2 + lint 7 lineage §1c + lint 8 card §1g).
Il brief di D1 cita QUESTA clausola. Sketch comando lint 8 (D1, in
finestra): enumerare gli id-scelta presentati nei capitoli/spina (grep
'C[0-9]+' + tabelle card) → per ciascuno verificare 6/6 campi presenti
(grep dei 6 header di card) → mancante = FINDING; le righe SA/NEVER del
ledger si contano dal ledger e si confrontano con le card
"non-aggiudicata" presenti (12+2 attese).

### 1c. LINT 7 — LINEAGE (nuovo, si aggiunge ai 6 di §L)

Ogni claim di novità nei capitoli (e poi nel deck) → o cita ≥1 riga del
LINEAGE_LEDGER nel §3-bis del suo nodo, o è "ANTENATI: NOT-FOUND(q)" con
query. Violazione = FINDING. Comando misurato in finestra (grep novelty/
new/first + walk delle sezioni §3-bis). Alimenta il retro-audit del deck
come i lint 3/4/6 [V2-R16].

### 1d. NODO NUOVO N-Q — "QUALE GAP DOMINA, SU QUALE ASSE?" (C-3, first-level)

Il checkpoint designa la domanda utente FIRST-LEVEL TREE NODE. L'albero
diventa **22 nodi**: N-Q si aggancia DIRETTAMENTE a Q0 (primo livello,
accanto ai rami R-I..R-IV — è LA domanda di valore che li attraversa).

- **Domanda**: *dei tre gap del frame three-design (x*_mean / x*_pf /
  x*_3D — formulazione, modello, composizione), quale domina, su quale
  asse?* **Working hypothesis dichiarata e falsificabile** (C-3/C-3bis):
  a vincoli fissi (eps,L) e settore fisso, gap(A) pf-vs-mean non ha
  teorema di soppressione (Jensen su G(x;s) su escursioni 10:1);
  gap(B) pf-vs-3D ha TRE teoremi di soppressione ([T-T0P], K-bar=0,
  [T-DISC]) sulla parte liscia — quindi plausibilmente (A) > (B)
  in-settore. **REGOLA VINCOLANTE (C-3ter): la gerarchia NON si enuncia
  MAI senza il tallone (J)** — il canale dei front jumps è il primo
  ordine NON soppresso di gap(B) (SBV-conditional, delta underived); se
  (J) è grande, (B) può dominare anche in-settore. Death scenario = due
  fallimenti indipendenti, ciascuno misurabile ((A): twin a vincoli
  identici, cheap, FIRST; (B): M-RED front legs + 5F sign test).
- **Falsificatore**: i decisori pre-registrati — twin PB-2 kill-or-
  validate; M-RED bande (comparison C, F_true vs F_2D per fase); 5F
  gradient + sign test; CFD-2/CFD-1. Entrambi gli esiti informativi.
- **Riga Q della matrice §M** (5 celle nuove; la tabella v2 si estende,
  lint 3 ricalcola enumerando):

| cella | stato | dove / contratto / ragione | owner |
|---|---|---|---|
| Q-i | SCOPERTA | CH6 §1.2-bis nuovo "quale gap domina": frame three-design + working hypothesis + tallone (J) + death scenario, tutto con ancore checkpoint C-3/C-3bis/C-3ter | B5 |
| Q-ii | F-P | nessuno strumento proprio: i decisori (twin, M-RED, 5F, CFD) sono strumenti delle righe B/D/E/I — assorbimento dichiarato | — |
| Q-iii | SCOPERTA | il campo non pone la domanda (nessun paper P-A..P-D separa i tre gap): forma di G-iii, query citata, esito NOT-FOUND(q) o refs; eco CH5 | B5 |
| Q-iv | SCOPERTA | la proposta = gerarchia come IPOTESI DICHIARATA + decisori pre-registrati + twin-first (C-3bis); CH6 §1.2-bis | B5 |
| Q-v | SCOPERTA | PB-2 OPEN; decisioni utente twin (a)/(b) e S-5F/C51 pendenti con owner e latest-start (§2); CH6 §3 | B5 |

  Conteggio aggiornato per enumerazione: 31 COPERTE / 14 PARZIALI /
  34 SCOPERTE / 6 F-P = **85 celle** (il lint 3 non usa questo numero:
  ricalcola dalla tabella v2 + questa estensione). Casa capitolo: CH6
  (attraversa CH3/CH8 via cross-ref). Il check bidirezionale
  albero↔matrice (F-des-2) copre anche N-Q.

### 1e. REGOLE DI SCRITTURA C-2 nei brief writer (vincolanti, W-B.1)

(i) il rung quasi-1D = "ORACOLO SENZA CONTOURING (solo eps)" — MAI
"the 1-DOF nozzle case"; (ii) **BANDITO il non-sequitur T1c**: lo shift
eps* di T1c NON è evidenza del gap di contouring vincolato (T1c riguarda
QUALE media nella condizione di adattamento al rung oracolo); nel
problema vincolato standard (eps,L)=dati, la differenza mean-vs-per-fase
vive SOLO nella forma di parete via shared-wall; (iii) Humphreys ×2.45 =
pertinente alle design variables a vincoli fissi (truncation/base,
PB-2). Ogni violazione trovata da W-C = FINDING con riga C-2 citata.

### 1f. C-7 nel brief B5 + CHECKLIST-GUARDIE unica

Nel brief B5 (CH5/CH6): "il campo" SEMPRE istanziato — PKU / NUAA /
KIT-Aoyama / NASA-Glenn / Purdue con paper (id registry). Inoltre
l'orchestratore scrive UNA volta il file `GUARD_CHECKLIST.md` (raws),
consumato DUE volte (refuter W-C sui capitoli; retro-audit Blocco 2 sul
deck). **La lista delle guardie vive SOLO in quel file (oggi 15 —
sorgente unica; nessuna enumerazione parallela qui, per non creare liste
divergenti) [R-5 applicata].**

### 1g. DECISION CARD estese + LINT 8 (iniezione utente 2026-08-23, gate scelte)

Ogni SCELTA presentata — nei nodi-atlas (§7(a)/CH4 §1.3), nelle slide,
nel backup L2, nei nodi del grafo camminabile — porta la **DECISION CARD
completa a 6 campi**:

1. **scelta** (id ledger);
2. **alternative censite CON DATA E FONTE della survey** (quale survey le
   ha censite, quando, con quale perimetro — id/anchor, mai a memoria);
3. **verdetto + perché**;
4. **RECENCY/SOTA-NESS CHECK della survey stessa**: copriva lo stato
   dell'arte a quella data? è ancora attuale OGGI? — **flag STALENESS
   esplicito se no** (la survey è un claim con data, non una premessa);
5. **falsificatore**;
6. **trigger di ri-esame con FINESTRA NOMINATA** (quale evento/fase
   riapre la scelta, e quando).

**LINT 8 (nuovo)**: scelta presentata senza card completa (6/6 campi) =
violazione → FINDING. Si aggiunge a lint 7; alimenta il retro-audit del
deck come i lint 3/4/6/7.

**Card obbligatorie anche per il NON-aggiudicato**: le 2 righe
SINGLE-AUTHOR + le 12 NEVER del choice ledger (conteggio di record
12/36/12/2) portano card **"non-aggiudicata, finestra Y"** STAMPATA
(campi 1-2 compilati, campo 3 = "NON AGGIUDICATA", campo 6 = la finestra
Y di ri-esame) — MAI omesse.

**Esempio vincolante da eseguire (card di riferimento)**: la card
**C31/engine** include **Uno** (censito: paper `vanaret_leyffer_2026_uno`
+ `vanaret_montoison_2026_joss` in registry, repo QUARANTINATO in `Uno/`
— mai nei commit, come GENO/) con la sua collocazione nel cluster di
ri-esame **F2-entry** (C31-A/B, C58 delta-sweep vs landscape 2026,
SDP-CAND-8): campo 4 = il censimento solver è datato e va dichiarato
tale; campo 6 = finestra F2-entry nominata.

Owner: B4 compila le card della riga I (CH4); ogni altro writer compila
le card delle scelte che il SUO capitolo presenta (il formato è unico,
questo §); il grafo camminabile eredita i 6 campi nei nodi-scelta
(estensione della spec [V2-R16]); lo storyboard/deck eredita le card
nelle slide-scelta e nel backup L2. Refuter W-C: campiona le card contro
il ledger (guardia 14 della GUARD_CHECKLIST).

==============================================================================
## §2 — GATE DI CALENDARIO + CUT-LIST (miglioria ②)

- **Freeze atlas = T-12 giorni dalla milestone.** Milestone di record =
  early/mid Sept (banda 8-15/09) → banda freeze 27/08-03/09; **target di
  pianificazione = 2026-08-29/30** (coerente con entrambi i review). Se
  l'utente pinna la data milestone, T-12 si ricalcola e vince.
- **Budget §W presi come CAP, non stima**: W-A ≤220k; W-B.0 ≤250k;
  W-B.1 ≤600k; W-B.2 ≤240k (a budget esaurito: ramo (c) onesto /
  "doppia prova: ASSENTE" = FINDING, MAI scavo oltre-cap); W-C ≤400k;
  W-D ≤120k.
- **Tripwire**: onda oltre 1.5× il cap, O F-des-1/2 sparato, O freeze
  non raggiungibile ⇒ STOP + decisione utente (frame pre-armato F-1 del
  relaunch review: release a due timbri CORE/FULL), MAI prosecuzione
  silenziosa.
- **CUT-LIST ordinata dell'atlas** (ciò che scivola post-milestone SE il
  freeze arriva prima del completamento — sempre come FINDING dichiarato,
  mai in silenzio): 1° lint 2 full-manifest (regola BULK resta); 2° §6
  STORIA dei capitoli non deck-bearing; 3° celle SCOPERTE non consumate
  dallo storyboard → FINDING con owner. NON tagliabili: lint 1/3/4/6/7/8 [R-6],
  refutazione W-C delle sezioni nuove, anchor-walk delle storie scritte,
  righe ADVISORY_INDEX/registry alla promozione (R7).
- **Budget post-atlas DICHIARATO** (prima quantificazione su file):
  authoring deck ~400-700k (41+ slide spec, crop extract_figs, eq-strip,
  note, script grafo); Blocco 2 ~300-500k (retro-audit + comms + Q&A
  red-team + backup). Time-box giorni (dal 24/08): W-A+W-B.0 ≤1g;
  W-B.1 ≤1.5g; {W-B.2 ∥ W-C.a} ≤1g; W-C.b+W-D+critic+promozione ≤1g →
  freeze 29-30/08; storyboard v3 + gate utente 30-31/08; authoring
  31/08→05/09; Blocco 2 05→09/09; buffer+prove → milestone.

==============================================================================
## §3 — OVERLAP STORYBOARD/ONDE (miglioria ③)

- W-C si esegue in due sotto-round: **W-C.a** = C1-C4 (REFUTE_CH9,
  REFUTE_CH10, sezioni nuove dei capitoli estesi, mini-pass [W2-*]) +
  C6 (lineage matrix); **W-C.b** = C5 (storie §6 + posizionamenti §7).
- **Lo storyboard v3 PARTE alla chiusura di W-B.1 + W-C.a** (il
  contenuto deck-bearing è lì), in parallelo a W-B.2/W-C.b/W-D.
- **La promozione a docs/atlas/ resta SOLO a atlas completo** (tutti i
  lint + W-C.b): il trust meccanico non si sconta; solo lo storyboard
  parte prima.
- Regola di non-interferenza: W-C.a legge i capitoli DOPO l'atterraggio
  di W-B.1 e IGNORA le sezioni §6 (che W-B.2 sta scrivendo; le refuta
  C5 in W-C.b). Ogni file ha sempre ESATTAMENTE un writer per round
  (regola v2 invariata).
- **DECK FEED** (dedup dal relaunch review, G-4, serve l'overlap): ogni
  writer W-B.1 chiude il capitolo con blocco `## DECK FEED` (5-10
  righe): asserzioni candidate-slide in frase piena (assertion-evidence)
  + ancora + classe. Lo storyboard v3 si COMPILA dai feed, non ri-legge
  10 capitoli.

==============================================================================
## §4 — FREEZE DEL META-DESIGN (miglioria ④)

v2 + questo emendamento = **FROZEN** dopo la verifica breve (§7), salvo i
falsificatori F-des-1..3 già previsti (che restano vivi). Ogni altra
modifica proposta da chiunque = FINDING nel log d'onda con decisione a
confine, MAI re-design. Le 2 NOTE del verifier sono applicate qui:
V-N1 → il conteggio slot è ricalcolato in §6d (supersede "18"); V-N2 →
l'esecutore materiale delle disposizioni W-C = i refuter stessi, ciascuno
compila la tabella di disposizione nel PROPRIO file di refutazione.

==============================================================================
## §5 — SEMINA Q&A IN W-C (miglioria ⑤)

Ogni refuter W-C consegna le obiezioni SOSTENUTE già in formato
**domanda → risposta → ancora → slide-backup candidata** (sezione finale
del proprio REFUTE). La mappa Q&A del Blocco 2 (upgrade 4 della missione)
si ASSEMBLA da queste sezioni + dal banco-utente §D [V2-R15], non nasce
da zero.

==============================================================================
## §5-bis — CONVERGENCE PROVENANCE nel retro-audit (iniezione utente 2026-08-23, gate finale)

Il retro-audit del Blocco 2 è ESTESO: ogni slide-claim load-bearing
porta la riga di **convergence provenance**:

    claim → ancora → classe → QUANDO+COME trattato a convergenza
    (sessione, processo [panel/refuter/gate/dual-seed/...], judge,
    landing [dove è atterrato: M0/D-doc/registro])

oppure la dichiarazione STAMPATA **"non-a-convergenza: classe+owner"**
(mai omissione silenziosa).

- **Il join si fa contro le sezioni §6 STORIA dell'atlas** → VINCOLO SUI
  WRITER W-B.2 (nei brief B8a/B8b): ogni battuta del trittico porta
  **data + processo + verdetto** per ogni pezzo (non basta l'ancora: la
  battuta dice QUANDO, con QUALE processo, con QUALE esito). Il ramo (c)
  NON-RIDERIVATO resta come da [V2-R2] — la sua doppia prova alternativa
  porta anch'essa data+processo+verdetto, o "doppia prova: ASSENTE" =
  FINDING.
- **Il ROBUSTNESS VERDICT del deck aggiunge i conteggi**:
  convergenza-piena / classe-dichiarata (non-a-convergenza stampata) /
  ridotti / finding — accanto ai conteggi walked-fresh / walked-inherited
  di §6a (G-8). L'eredità dichiarata (G-8) vale anche qui: un claim la
  cui ancora punta a una riga d'atlas con §6 STORIA già camminata da C5
  eredita la provenance attraverso l'arco verificato.
- Refuter C5 (W-C.b): verifica che le STORIE portino data+processo+
  verdetto (guardia 15).

==============================================================================
## §6 — DEDUP E DECISIONI ORCHESTRATORE

### 6a. Dedup dei due review (obbligo dedup-SEMPRE)

Il rilancio in-window (AGNOSTIC_GOAL_REVIEW_S2_relaunch.md) converge col
review committato su: routing correzioni (G-1≡①), calendario+cap+tripwire
(G-3≡②), overlap (F-1/G-4≈③), freeze (implicito≡④). Adottati dal relaunch
perché compatibili e a costo ~zero: **G-4** deck-feed (→§3), **G-8**
retro-audit a eredità dichiarata (protocollo Blocco 2: conteggi separati
walked-fresh / walked-inherited / reduced / findings; l'eredità passa per
l'arco slide→atlas verificato), **G-9** de-risk grafo (slot MECCANICO,
effort ridotto DICHIARATO: estrazione JSON nodi/archi dalla pipeline map
con assert 62/17/45 [R-4] + prototipo render L0 da GRAPH_VIZ_SPEC —
lanciabile in finestra W-A, file nuovi, zero conflitto), **G-10** agenda decisioni
utente (twin PB-2 (a)/(b) a vincoli IDENTICI presentato al GATE
STORYBOARD con costo + **latest-start ~01/09** oltre cui la slide resta
nella forma onesta; S-5F path A/B/C + priorità C51 idem), **G-11**
protocollo bounded per le query in-onda (perimetro fisso = registry 174 +
litmap + P-A..P-D; esito NOT-FOUND(q) o refs + STOP; nessun procurement
in-onda salvo Fievisohn sweep-disco già approvato).
**DIVERGENZA DICHIARATA e risolta**: il relaunch (G-6) proponeva ANTENATI
dentro §3 (template a 8); l'ordine utente = 9 sezioni → vince l'ordine
(§1b, forma 3-bis). Nessun'altra divergenza sostanziale.
**ROUTING C-1bis [R-3]**: il brief B2 (CH10) porta VERBATIM il blocco
checkpoint :146-165 (imposed-detonation-BC = antenato del contratto
Γ_d; T-DISC come riparazione teorematica del BC p-only; Γ_d NON è "the
throat" — stazione axially-supersonic-with-margin; sonic line corrugata
= perché del margine; patch subsoniche = case-class dichiarata) — mai
parafrasi a memoria; il refuter la controlla via guardia 11.

### 6b. Decisione A4 (misurata in finestra, SR-12)

Delle 4 ref fuori-registro di v2: **Farrell/deflation → riga ESISTE**
(`wanted_farrell_birkisson_funke_2015`, registry :1196): la cella G-ii
la cita VERBATIM per l'asse deflated-continuation (upgrade senza mint);
NOT-FOUND(q) resta SOLO per Lipschitz-global/branch-and-bound (0 righe,
grep in finestra). **Paciorri-Bonfiglioli** → eccezione-D6 dichiarata +
vicino esistente `wanted_onofri_paciorri_2017_book` (:1142) citabile.
**Gelb-Tadmor** → eccezione-D6 confermata (0 righe; ancora D6 :256-263
già verificata dal verifier). Nessun mint pre-W-B necessario.

### 6c. MINT C-4 (identità di decomposizione, F-2)

Decisione: **MINT-PENDING con dicitura uniforme**. Tutti i writer citano
IDENTICO: "[MINT-PENDING F-2: sector-decomposition identity J_exact =
∫ F_true dµ — THEOREM in-panel, non ancora numerato in M0]". Il mint
reale (riga claims registry) avviene alla finestra di promozione insieme
alla riga "methodology lineage-recognition gap" (C-1) — stessa finestra,
R7. MAI 7 diciture diverse per lo stesso oggetto.

### 6d. Conteggio slot aggiornato (supersede V-N1 e il "18" di v2)

W-A: 3 giudizio (A1, A2, A3) + 2 meccanici (A5 historian-index; A6 =
de-risk grafo G-9) = 5; W-B.0: 2 giudizio (L1, L2); W-B.1: 7 giudizio;
W-B.2: 2 giudizio (B8a, B8b); W-C: 6 giudizio (C1-C5 + C6 lineage);
W-D: 1 meccanico + orchestratore; verifica emendamento (§7): 1 giudizio.
**Totale: 24 slot agente** (20 giudizio in-onda a inherit max + 3
meccanici dichiarati + 1 giudizio di verifica emendamento; il critic
finale a max è ULTERIORE — 25° slot, fuori dal conteggio-onde — e
l'orchestratore non è uno slot). Token stimati: ~1.35-1.95M per l'atlas
(cap per onda in §2). [R-1 applicata]

### 6e. Capitoli senza writer W-B.1 per il §3-bis

CH2 e CH7 hanno writer B7; CH1/CH3 B3; CH4 B4; CH5/CH6 B5; CH8 B6;
CH9 B1; CH10 B2 → TUTTI i 10 capitoli hanno un writer W-B.1 che riceve
l'incarico §3-bis per i nodi ospitati (nessun capitolo orfano; il
LINEAGE_LEDGER di W-B.0 è input di tutti).

==============================================================================
## §7 — VERIFICA BREVE DELL'EMENDAMENTO, POI LE ONDE

1 agente (giudizio, inherit max, Fable): verifica che (i) le 5 migliorie
ordinate ①-⑤ siano TUTTE cablate qui con sostanza (non parafrasi); (ii)
nessun punto di questo emendamento riapra parti di v2 non ordinate; (iii)
la riga Q e la sezione 3-bis siano coerenti col check bidirezionale e coi
lint (3, 5, 7); (iv) il dedup §6a non abbia perso nessuna miglioria
applicabile dei due review; (v) i conteggi di §6d tornino per
enumerazione. Esito nel file `VERIFY_AMENDMENT_v2.1.md` (raws). Poi:
W-A parte. Da lì si ESEGUE — niente altro meta-design (§4).
