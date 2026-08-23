# CH6 — Value case, onestà e roadmap: Gap A/Gap B, PB-2, deciders, ask

Capitolo di ricostruzione S-PRES (2026-08-22/23). Stadio di confronto: M0,
registries (claims/findings/choice), pipeline decision map, PROGRESS, checkpoint
S-FOUNDATIONS. Questo testo NON aggiudica nulla di nuovo: ricostruisce, ancora,
dichiara gli aperti. Ogni claim porta ancora (file:riga) e classe di rigore.
Consumo dichiarato: storyboard v3, banca Q&A red-team, mappa F2+.

---

## 1. Ricostruzione

### 1.1 Il frame di valore: Gap A / Gap B (la domanda "quanto vale il programma" resa decidibile)

Il value case del programma è stato registrato nella finestra S-FOUNDATIONS-C4
come frame a due gap, ancora S-PRES dichiarata
(`validation/sfoundations_raws_2026-08-13/SESSION_STATE_checkpoint.md:466-472`):

- **Gap B** = J3D(x\*_pf) − J3D(x\*_legacy): la differenza di valore tra il design
  della nostra funzionale per-fase mediata e il design legacy
  (Veen/Angelino-at-mean), **misurabile IN-HOUSE a costo basso** con un
  paired-run F2 ("measurable IN-HOUSE cheap (paired-run F2 demo, our functional
  vs Veen/Angelino-at-mean)", checkpoint :468-469). Classe: quantità DEFINITA di
  record, valore MAI computato (vedi §3, A-1).
- **Gap A** = distanza dall'ottimo 3D vero, che è **INCOMPUTABILE**
  ("the UNCOMPUTABLE true 3D optimum", checkpoint :469-470): trattato
  bounded-only via lo schema delta/mu + spot-check R22-CFD.
- **Value condition di record**: "Gap B material AND Gap A < Gap B"
  (checkpoint :471-472). Il programma vale se il salto misurabile è materiale E
  se ciò che la riduzione non vede è più piccolo del salto.

Due guardie di formulazione accompagnano il frame:

1. **Wording guard (user catch, sustained)**: "best-of-sweep != argmax — NO
   paper ever optimized the true 3D case (no optimizer in any of the 4; P-M =
   hand-guided redesign)" (checkpoint :472-476; forma di record in M0:
   [ORCH-HARV-1], `docs/rde_nozzle_MASTER.md:1335-1339`, [ADV]). Nessun
   confronto in letteratura è un confronto con un argmax.
2. **Lo schema del bound di Gap A è SCHEMA, non numero**: la cella (vi) della
   forchetta dichiara "**delta AND L_H UNDERIVED — NO argmax-shift number exists
   at any grade, and none from the measured carrier alone**"
   (`docs/rde_nozzle_MASTER.md:1348`), con falsificatore armato nel claims
   registry: "any argmax-shift number quoted at any grade from this schema
   before delta/L_H land" = violazione (`docs/claims_registry.yaml:2262`).

Lo strumento di onestà che porta il frame è la **forchetta a 6 canali**
(M0:1341-1348), con regole di cella vincolanti: "bound-or-estimate declared;
rigor class per bound; provenance per number; ... NO cell above its held
evidence class" (`docs/rde_nozzle_MASTER.md:1306-1309`). Classe della tabella:
mista, dichiarata cella per cella (SCHEMA/THEOREM\*/[SE]/[REP]/[ADV]).

### 1.2 PB-2: il flag problem, e perché non è ancora un numero

PB-2 è il problema-bandiera del problem book
(`docs/rde_nozzle_problem_book.md:532-537`): "PB-1 for configuration (ii) with
L_p < l(ξ_peak) and a base-pressure closure: T4's nesting fails, max∫ < ∫max
strictly; compute the cycle-optimal truncated plug vs peak- and mean-designed
baselines (Table-1 states). This is the first concrete problem NOT solved by
any single-phase design." È il punto dove la media del ciclo produce un ottimo
GENUINAMENTE diverso da ogni design a fase singola (rottura del nesting di T4:
la sharpness clause del teorema di nesting — "a length cap L < l(xi_peak), a
base-pressure model at a truncation plane, or non-ideal adaptation break the
nesting: then max Int < Int max STRICTLY" (`docs/rde_nozzle_MASTER.md:2316-2319`),
con classe dichiarata "the nesting and the constrained-KKT structure are
THEOREM (standard)" (M0:3524-3525) [W2-R6]; il numero PB-2 stesso: **MAI
computato** — nessuna riga (value,delta) truncated-plug esiste nel record,
vedi trigger C61 sotto).

**Guard di priorità sulla bandiera (locked formulation D-06)** [W2-R5]: la
forma di record del claim di novità è VINCOLATA — "PB-2 LOCKED FORMULATION OF
RECORD (D-06, 2026-08-13 — never abbreviate): 'the first genuinely averaged
and NON-COLLAPSING shape problem of the program (a CYCLE instance)'. Any
phrase of the type 'the first averaged-thrust variational problem' is DEAD of
record: Efremov-Kraiko 2004 poses a period-averaged maximum-thrust variational
problem, Kraiko-signed, with measure Int_0^1 ... dt (Eq. 1.7, p.624)
[page-verified]" (`docs/rde_nozzle_MASTER.md:2320-2326`). Efremov-Kraiko non
tocca PB-2 perché non ha wall contour (incognite = funzioni temporali dello
stato d'uscita + scalari W, Q) e il suo ottimo COLLASSA (M0:2326-2329) — è il
query-bound esplicito del claim di novità, da portare in slide con la bandiera.

Cosa serve per computarlo, dal record:

- **Baseline mean-designed**: il confronto richiesto da PB-2 è "vs peak- and
  mean-designed baselines" (:535). La baseline media è I4 del problem book:
  "I4 (single mean state): one state (⟨Pc⟩, T0, γ); classical Rao/GENO design"
  (`docs/rde_nozzle_problem_book.md:211`), con la nota "WITHIN I3's other
  hypotheses, I4 is not an approximation but EXACT" (:213). Attenzione alla
  distinzione: la baseline di record del paired-run di Gap B è "our functional
  vs Veen/Angelino-at-mean" (checkpoint :468-469), mentre I4 è "classical
  Rao/GENO design" (:211) — sono design legacy DIVERSI. L'idea di un twin
  famiglia-vs-I4 sullo STESSO engine che serva anche Gap B è una PROPOSTA di
  consolidamento di questo capitolo (una run, due baseline mean-designed:
  Rao/GENO-at-mean = I4 e Veen/Angelino-at-mean = legacy praticato), NON una
  identificazione di record. [W2-R2]
- **Chiusura p_b**: lo slot N2 è DICHIARATO e NON aggiudicato. C61
  (`docs/choice_ledger.yaml:818-830`): status **NEVER**; incumbent = "the Veen
  constant closure p_b = 0.846 p/M^1.3 is practiced in the LEGACY chain only
  ... the program's own p_b is a DECLARED SLOT, not a model" (:820); tra le
  alternative il verdetto WG10 "N2 MUST REPLACE IT" (:824). Trigger: "first
  truncated-plug (value,delta) row entering the record, or F4b window entry"
  (:829). Il blocco è registrato anche come finding:
  `docs/findings_registry.yaml:2092-2101`
  (litreview:residue-r8-r23-base-pressure-pb2-blocking): Pb/Pa=1 inammissibile
  in entrambi i regimi, transizione Pa/Pc~0.15, e "no measurement of a
  TRUNCATED-plug RDE base exists ... nozzleless->truncated-plug transfer is an
  ANALOGY, not a measurement" ([REP] sul dato, ANALOGIA dichiarata sul transfer).
- **Il warning Humphreys sul p_b** (perché la chiusura non è un dettaglio):
  scambiare il modello di p_b "moved the optimum base height ×2.45 (0.954 →
  2.34 in) and the tip wall slope −13.26° → −3.08° while moving thrust only
  +0.26% — the p_b closure moves the ARGMAX at O(1) with the VALUE nearly flat"
  (M0 [ORCH-HARV-3], `docs/rde_nozzle_MASTER.md:1455-1464`, classe [ADV];
  numeri = di Humphreys-Thompson-Hoffman 1971, CT-6). Stessa lettura nel note
  C61: "The Humphreys x2.45 argmax sensitivity is channel-(vi)-shaped, i.e.
  FOUNDATION-grade: the closure choice moves the DESIGN, not just the value"
  (`docs/choice_ledger.yaml:830`).

### 1.3 Le guardie pubbliche: D-44 e P34

- **D-44 — gate sui claim pubblici di adeguatezza** (armato, e vincola QUESTO
  deck): "any public adequacy claim GATED (forchetta = bracket with provenance,
  never demonstrated adequacy)" — riga della pipeline map
  (`docs/rde_nozzle_pipeline_decision_map.md:180`, stato "ARMED GATE", "fires
  on any public adequacy claim, either way (before/after R22)"), arco E31
  esplicito verso S-PRES: "D-44→S-PRES/public claims: findings :1468 'any
  public adequacy claim remains gated per D-44 either way'; PROGRESS :395
  S-PRES trigger-scan item (ii)" (:239). Owner di record: "F2 or F5 (D-44;
  R22 = the single highest-value tranche-2 item)"
  (`docs/findings_registry.yaml:2163`). Il trigger-scan S-PRES lo recepisce:
  "(ii) D-44: claim di adeguatezza gated (forchetta = bracket con provenienza,
  mai adequacy dimostrata)" (`docs/rde_nozzle_PROGRESS.md:400-401`).
- **P34 — gerarchia di evidenza per claim engine-level** (finding CONFIRMED,
  `docs/findings_registry.yaml:2530-2539`): "the staged evidence hierarchy for
  engine-level claims — V0 continuous verification -> per-champion validation
  -> pre-registered, prediction-first rig/thrust-stand terminal test ... was
  never adjudicated anywhere in the record" (:2533). Rider che spara su questa
  milestone: "S-PRES ... is a trigger-bearing external act — slide-level engine
  claims must DECLARE their evidence stage on this row's ladder at the S-PRES
  Block-0 trigger-scan" (:2538). Classe: gap dichiarato con owner
  ("P-1/G5-G6 claims window", :2537).

### 1.4 R26: la domanda a due livelli (sizing vs ranking)

La tensione R26 è aggiudicata come SOGLIA, non come contraddizione
(`docs/findings_registry.yaml:2148`): "is cycle-averaging adequate or blind?
Paxson-Miki says adequate for sizing (6.54 vs ~6.5); Harroun 2021 says blind to
contour ranking (c_F=1.25 identical) — PARTIALLY adjudicated: not a
contradiction, a RESOLUTION THRESHOLD (adequate for sizing, not demonstrated
adequate for percent-level ranking); exactly where the threshold falls stays
OPEN, decided by R22". La forma di record in forchetta, canale (iv)
(`docs/rde_nozzle_MASTER.md:1346`): BEST = "**~1% at sizing level** [REP]:
Paxson-Miki area-ratio agreement 6.54 vs ~6.5"; WORST = "**RANKING THRESHOLD
OPEN (R26)**: adequacy NOT demonstrated for percent-level contour ranking ...
Harroun 1.25-flat is a NON-DISCRIMINATION datum at verified limits ... NOT
proof of blindness". Classe: [REP] sul livello sizing; OPEN dichiarato sul
ranking. Nessun referee esterno esiste per la parte per-fase: "NO EXTERNAL
PUBLISHED REFEREE EXISTS for the per-phase thrust error: the literature carries
NO unsteady c_F datum that discriminates the 2D-per-phase-averaged prediction
against 3D-unsteady truth" ([REV2-r1-15], `docs/rde_nozzle_MASTER.md:1322-1331`,
dichiarazione strutturale di record; nearest referees nominati e squalificati
in [GRAFT-G10], M0:1311-1320, [ADV]).

### 1.5 La roadmap: i deciders in ordine, coi costi noti

Ordine ratificato al touchpoint C4 (`docs/rde_nozzle_PROGRESS.md:407-421`):

1. **M-RED — prima campagna F2, in-house** ("(c) M-RED RESTA prima campagna F2
   (nessun pull-forward)", :417). Costo: il frame utente-ratificato la marca
   "tier (b) M-RED execution = THE cheap decisive unlock, F2-gated"
   (checkpoint :462-463); il push formale tier (a) è perimetrato "~0.3M"
   (checkpoint :460-462; unità NON dichiarata all'ancora — la lettura "token
   di orchestrazione" è [INF] dal contesto del checkpoint [W2-R8]; su slide il
   numero non va portato). M-RED misura eps e alimenta le bande B-1/B-2/B-3 della
   forchetta (colonne "what tightens it", M0:1344-1346).
2. **CFD-2 — paired demo, template Li-Xu 2025 (P-C), in coda F2**: "CFD-2 (demo
   pair Harroun coi run per-fase nostri, barra = eps di M-RED, template
   paired-run Li-Xu 2025, contratto BC documentato dal throat harvest) ENTRA IN
   CODA F2" (:408-411).
3. **CFD-1 — test del pin su configurazione accoppiata reale, item di calcolo
   massimo, decisione POST-M-RED**: "CFD-1 ... SI DECIDE POST-M-RED con dossier
   procurement/collaborazione e criteri di riferimento PM22-conforme vs
   Jourdaine-patologico" (:411-414). Classe di costo di record: "~12M-cell cost
   class, M-RED dependency, G1 haste-risk" (pipeline map,
   `docs/rde_nozzle_pipeline_decision_map.md:77`; stato "USER-DECISION
   PENDING"). Le catene sono cablate nella mappa: E28 "T-RED → M-RED bands
   B-1/B-3 → X-T3QS-5F license (F2) → R22-CFD-1" e E29 (deriver (vi))
   (`docs/rde_nozzle_pipeline_decision_map.md:236-237`).

### 1.6 Le ASK di record

Dal record, non inventate per il deck:

- **CFD-1 come collaborazione/procurement**: il dossier
  procurement/collaborazione è il veicolo deciso per CFD-1
  (`docs/rde_nozzle_PROGRESS.md:411-413`).
- **Dati motore per la classe del pin (R20)**: "no published dataset certifies
  a single-mode wave PERSISTENT in thermal-steady-state (Teasley 2023's
  observations are almost all at startup) — the periodic-pure-wave pin remains
  valid as a MODEL HYPOTHESIS but loses its hardware provenance; decided by
  high-speed imaging in steady mainstage, or published transition durations"
  (`docs/findings_registry.yaml:2148`; owner "F5 (R20)", :2152). L'ask: imaging
  ad alta velocità in mainstage termicamente stazionario, o durate di
  transizione pubblicate.
- **Canale paper**: P-1, venue JPP ("I documenti di teoria sono la sorgente del
  paper (P-1, venue JPP)", `CLAUDE.md` R4).
- **Procurement documentale attivo**: "top-3 harvest (Lim-Humble AIAA
  2020-0195, Stechmann PhD 2017, Schwer-Kailasanath AIAA 2012-3943) + i 3 ask
  fermi (More-Wild ECNoise, ASME V&V 20-2009, Xing-Stern); il resto WANTED
  passivo" (`docs/rde_nozzle_PROGRESS.md:418-421`); coda WANTED Tier-1
  W-01/W-02/W-03 = Fotia 2016 (JPP 32(3):674-681), Goto 2019 (JPP 35(1):
  213-223), Ma-Bao-Wang 2023 (AST 140:108464)
  (`docs/literature_registry.yaml:1232-1248`).

### 1.7 L'onestà come strategia (la bussola del carrier)

La bussola della milestone è testuale: "comunicare il programma SENZA gonfiare
una sola classe di rigore — l'onestà strumentata È il vantaggio competitivo del
deck" (`validation/ADVISORY_Spres_prompt_2026-08-21.md:233-235`). Non è
retorica: è la stessa disciplina che produce il no-external-referee fact
(M0:1322-1331), le celle "NO cell above its held evidence class" (M0:1309), i
12 NEVER del choice ledger (righe di scelta con incumbent dichiarato e
falsificatore pinnato, "NEVER: 12 (C25 C38 C51 C52 C53 C54 C55 C57 C59 C60 C61
C62)", `docs/rde_nozzle_pipeline_decision_map.md:293`), e i falsificatori
armati sui numeri vietati (claims :2262). Alla domanda "perché credervi senza
il numero" il programma risponde con la STRUTTURA, non con una promessa: vedi
§4, Q2.

---

## 2. Stato per-claim

| # | Claim | Classe | Ancora | Carrier / falsificatore |
|---|-------|--------|--------|------------------------|
| 1 | Gap B = J3D(x\*_pf) − J3D(x\*_legacy), misurabile in-house (paired-run F2, nostra funzionale vs Veen/Angelino-at-mean) | Definizione di record; valore MAI computato | checkpoint S-FOUNDATIONS :466-472 | Carrier futuro = paired-run F2 (M-RED window); oggi NESSUN numero |
| 2 | Gap A = distanza dall'ottimo 3D vero, incomputabile; solo bounded (delta/mu) + spot-check | SCHEMA (bound); delta e L_H UNDERIVED | checkpoint :469-471; M0:1348 | Falsificatore armato: claims_registry.yaml:2262 (nessun numero di argmax-shift a nessun grado prima di delta/L_H) |
| 3 | Value condition: Gap B materiale AND Gap A < Gap B | Frame registrato (S-PRES anchor), non teorema | checkpoint :471-472 | Deciso da M-RED + CFD-2/CFD-1 |
| 4 | best-of-sweep ≠ argmax; nessun paper ha mai ottimizzato il caso 3D vero | [ADV] guard di record | checkpoint :472-476; M0:1335-1339 | Query-bounded (4 paper campagna + P-M hand-guided) |
| 5 | PB-2: primo problema concreto non risolto da alcun design single-phase; T4 nesting fallisce, max∫ < ∫max strictly; novità SOLO nella locked formulation D-06 ("first genuinely averaged and NON-COLLAPSING shape problem ... a CYCLE instance", never abbreviate; near-miss Efremov-Kraiko 2004 = query-bound) [W2-R5] | Enunciato problem book (problema posato, non risolto); D-06 locked | problem_book.md:532-537; M0:2320-2329 | Carrier futuro = computo PB-2; trigger C61 :829; frasi "first averaged-thrust variational problem" = DEAD of record |
| 6 | Baseline media = I4 (⟨Pc⟩,T0,γ), esatta dentro le ipotesi I3 | Definizione di record | problem_book.md:211-213 | Twin famiglia-vs-I4 stesso engine = PROPOSTA di consolidamento col paired-run di Gap B (baseline di record di Gap B = Veen/Angelino-at-mean, checkpoint :468-469 — I4 è Rao/GENO, baseline distinta) [W2-R2] |
| 7 | Chiusura p_b: slot N2 dichiarato, NON aggiudicato; Veen legacy-only, WG10-FAILED | C61 status NEVER | choice_ledger.yaml:818-830 | Trigger: prima riga (value,delta) truncated-plug o finestra F4b |
| 8 | Swap del modello p_b muove l'argmax ×2.45 a valore quasi piatto (+0.26%) | [ADV]; numeri = Humphreys 1971 (CT-6) | M0:1455-1464; choice_ledger :830 | Exhibit classico, channel-(vi)-shaped |
| 9 | Nessuna misura di base truncated-plug RDE esiste; transfer nozzleless→plug = ANALOGIA dichiarata | [REP] sul dato + ANALOGIA dichiarata | findings :2092-2095 | Chiuso solo da misura (procurement class) |
| 10 | D-44: ogni claim pubblico di adeguatezza è GATED (forchetta = bracket con provenienza) | ARMED GATE | pipeline map :180, :239 (E31); findings :2163; PROGRESS :400-401 | Spara su questo stesso deck (trigger-scan Block-0) |
| 11 | P34: gerarchia di evidenza engine-level mai aggiudicata; le slide devono dichiarare lo stage | Finding CONFIRMED (gap con owner) | findings :2530-2539 | Rider S-PRES esplicito (:2538) |
| 12 | R26 sizing: ~1% a livello sizing (Paxson-Miki 6.54 vs ~6.5) | [REP] | M0:1346; findings :2148 | Page-verified nella confrontation |
| 13 | R26 ranking: soglia APERTA; Harroun 1.25-flat = non-discrimination datum, NOT proof of blindness | OPEN dichiarato | M0:1346; findings :2148 | Deciso da R22 (M-RED → CFD-2 → CFD-1) |
| 14 | Nessun referee esterno pubblicato per l'errore di spinta per-fase | Dichiarazione strutturale di record | M0:1322-1331 (+ :1311-1320 nearest disqualified) | Chiude solo via R22-CFD nostro o data procurement |
| 15 | R20: nessun dataset pubblicato certifica onda single-mode persistente in thermal steady state; pin = MODEL HYPOTHESIS | Residuo [REP]-based, OPEN | findings :2145-2153 | Deciso da imaging steady-mainstage o transition durations |
| 16 | Roadmap deciders: M-RED (prima campagna F2) → CFD-2 (coda F2, template Li-Xu paired) → CFD-1 (post-M-RED, ~12M-cell, user decision) | Decisione utente ratificata + pipeline map | PROGRESS :407-421; pipeline map :77, :236-237 | G1 haste-risk dichiarato sulla mappa |
| 17 | Bussola: comunicare senza gonfiare UNA SOLA classe di rigore | TERM vincolante della milestone | ADVISORY_Spres_prompt :233-235 | Refuter di rigore sul deck (doppia review) |

---

## 3. Gli APERTI

- **A-1 — PB-2 MAI computato.** Nessuna riga (value,delta) truncated-plug nel
  record (trigger C61 mai sparato, `docs/choice_ledger.yaml:829`). Servono:
  baseline I4 mean-designed (problem_book :211), chiusura p_b (C61 NEVER, slot
  N2; owner "N2/F4b window", :828), e la consapevolezza Humphreys ×2.45 che la
  chiusura muove il design (M0:1455-1464). Owner/trigger: F4b window / prima
  riga truncated-plug.
- **A-2 — Gap B: grandezza ignota.** Il frame è registrato, il paired-run non è
  stato eseguito (checkpoint :466-472). Owner: finestra M-RED/F2 (PROGRESS
  :417). Se Gap B risultasse trascurabile: vedi §4 Q1.
- **A-3 — Gap A: delta e L_H UNDERIVED.** Nessun numero di argmax-shift esiste
  a nessun grado (M0:1348); deriver nominati in ordine "X-T3QS-5F (F2) →
  C51-route-B → M-RED gradient rider → R22-CFD-1" (M0:1348, colonna deriver;
  pipeline map :237 E29).
- **A-4 — R26 ranking threshold OPEN.** "decided by R22" (findings :2148);
  fino ad allora D-44 gated ogni claim pubblico di adeguatezza (pipeline map
  :180).
- **A-5 — R20: provenienza hardware del pin.** Il pin onda-pura è ipotesi di
  modello, non fatto certificato da dataset pubblici in steady state
  (findings :2148). Owner "F5 (R20)"; trigger "next hardware-provenance
  campaign" (:2152-2153).
- **A-6 — P34: ladder di evidenza engine-level non aggiudicata** (findings
  :2533); a S-PRES vige solo la light-instantiation (dichiarare lo stage per
  slide, :2538); l'aggiudicazione piena resta alla finestra P-1/G5-G6 (:2537).
- **A-7 — CFD-1: decisione utente PENDING** con dossier post-M-RED (PROGRESS
  :411-414; pipeline map :77 "USER-DECISION PENDING", "G1 haste-risk").
- **A-8 — Base measurement truncated-plug RDE: inesistente nel corpus letto**
  (findings :2095) — procurement/misura, non chiudibile in-house.

Nessuno di questi aperti va riempito di plausibilità nel deck: si dichiarano
con owner e trigger, come sopra.

---

## 4. Domande da panel (banco utente incluso, verbatim-adattate)

**Q1. "Gap B potrebbe risultare trascurabile: cosa resta del programma?"**
Risposta onesta dal record: (i) il frame è costruito per essere falsificabile —
la value condition "Gap B material AND Gap A < Gap B" (checkpoint :471-472) è
un rejector, non uno slogan: se il paired-run misura Gap B trascurabile, il
programma lo DICE, e questo è esattamente il punto di R26: "adequate for
sizing" a ~1% è già [REP] (M0:1346) — un Gap B piccolo sarebbe un datum
misurato che stringe la soglia R26 sul caso testato, sempre come bracket con
provenienza, mai adequacy dimostrata: D-44 vale in entrambe le direzioni,
anche su un esito favorevole alla media ("fires on any public adequacy claim,
either way", pipeline map :180). [W2-R1] (ii) Restano in piedi i pezzi che non dipendono dal segno
di Gap B: il corpus dei teoremi di riduzione/struttura (forchetta canali
(i)-(iii), M0:1343-1345, classi SCHEMA/THEOREM\*), PB-2 come problema
matematico nuovo (problem_book :532-537 — la rottura del nesting non dipende
dalla grandezza di Gap B su UNA configurazione), e la macchina certificata
(oracoli, catena M-RED). (iii) OPEN dichiarato: la grandezza di Gap B è A-2 —
non abbiamo il numero, e non lo promettiamo: lo misuriamo per primi in-house.

**Q2. "Chiedete CFD e dati: cosa date in cambio, e perché ESA dovrebbe
investire PRIMA del numero PB-2?"**
Dal record: quello che esiste GIÀ e non dipende dall'investimento chiesto:
(a) i teoremi di DOVE la riduzione sbaglia — la forchetta a 6 canali con classi
e provenienza per cella (M0:1341-1348), incluso il no-external-referee fact che
NESSUN altro gruppo ha dichiarato (M0:1322-1331); (b) la macchina pronta: il
carrier misurato del canale (vi) esiste (J_red Hessians di record, curvatura
TR-Newton segmentata, M0:1348) — manca la licenza formale (delta/L_H), non il
codice; (c) la campagna è COST-CLASSED e ordinata (classi di costo dichiarate, non
prezzi assoluti: quelli sono OPEN, parte del dossier post-M-RED [W2-R7]):
M-RED = "cheap decisive unlock"
(checkpoint :462-463), CFD-2 in coda con template e barra definiti (PROGRESS
:408-411), CFD-1 ~12M-cell con dossier e criteri di riferimento già nominati
(PM22-conforme vs Jourdaine-patologico, PROGRESS :411-414; pipeline map :77);
(d) i falsificatori sono ARMATI prima dei numeri (claims :2262; D-44 pipeline
map :180). In cambio ESA ottiene: il primo paired-run famiglia-vs-legacy-mean
su motore condiviso (baseline di record Veen/Angelino-at-mean, checkpoint
:468-469; l'estensione a I4/Rao-GENO nella stessa run = proposta di
consolidamento, §1.2 [W2-R2]) — "primo" per costruzione: nessun paired-run di
questo tipo esiste nel corpus letto, query-bounded alla campagna 4-paper +
litmap [W2-R11] —, la prima verifica spettrale/di persistenza del pin su dati
veri (prima nel perimetro R20 search-proven [W2-R11])
(R20, findings :2148 — l'ask specifica cosa serve: imaging steady-mainstage o
transition durations), e un canale paper JPP (CLAUDE.md R4). L'ask documentale
è minimale e già enumerata (top-3 + 3 fermi + W-01/02/03, PROGRESS :418-421;
literature_registry :1232-1248). OPEN dichiarato: il ritorno quantitativo è
condizionato all'esito di M-RED — è per questo che CFD-1 si decide POST-M-RED,
non prima (G1 haste-risk, pipeline map :77).

**Q3. "La vostra onestà dichiara delta/L_H underived e 12 NEVER: non è un
programma immaturo?"**
Distinguere i due oggetti. (i) I "12 NEVER" (pipeline map :293) non sono
lavoro non fatto: sono righe del choice ledger dove un incumbent PRATICATO è
dichiarato con alternative enumerate e falsificatore pinnato per un flip futuro
— es. C61: incumbent Veen "legacy-practiced, WG10-FAILED" con quattro
alternative pesate a grado record (choice_ledger :818-830); C62 con "honesty
clause carried from the critic (zero inflation)" (:844). La classe NEVER è lo
strumento che IMPEDISCE ai default silenziosi di diventare fondamenta — i
programmi che non hanno questa lista hanno gli stessi default, non dichiarati.
(ii) delta/L_H underived (M0:1348) è la ragione per cui NESSUN numero di
argmax-shift è mai stato quotato — con falsificatore armato (claims :2262). Il
confronto rilevante: nessun lavoro pubblicato ottimizza il caso 3D vero, e
l'evidenza sweep/redesign è ranking-signal only (guard M0:1335-1339) — quindi
nessun confronto esistente è un confronto con un argmax [W2-R3] — e la
letteratura non porta NESSUN referee esterno
per l'errore per-fase (M0:1322-1331). La maturità di un programma di design si
misura su cosa può REGGERE in verifica, non su cosa dichiara di sapere: qui
ogni cella è al suo grado, "NO cell above its held evidence class" (M0:1309).
OPEN dichiarato: sì, delta e L_H mancano; i deriver sono nominati in ordine con
finestra (M0:1348; E29).

**Q4. "Se il pin onda-pura non è mai stato verificato spettralmente in NESSUN
CFD pubblicato (search-proven), su cosa poggia tutto?"**
Prima la precisione sul fatto, come sta nel record: la forma search-proven di
record è R20 — "no published dataset certifies a single-mode wave PERSISTENT
in thermal-steady-state ... the periodic-pure-wave pin remains valid as a MODEL
HYPOTHESIS but loses its hardware provenance" (findings :2148). Su cosa poggia
il programma, dal record: (i) il pin è un'IPOTESI DI MODELLO DICHIARATA, non un
fatto assunto di nascosto — e dentro il pin la cycle-average è
"CANONICAL-INSIDE-THE-PIN ... a theorem-backed CONSEQUENCE, not a choice"
(C59, choice_ledger :795-797), con le alternative fuori-pin (harmonic-balance,
time-spectral, windowed adjoint) enumerate nella stessa riga per i regimi a pin
indebolito (:798-801); (ii) il pin ha una guardia DI RECORD, con
stato dichiarato: "T0-flatness monitor + f_cycle contract field" (forchetta
canale (i), M0:1343) — il T0-flatness monitor è la parte armata; f_cycle è un
contract field NOMINATO non ancora cablato, e i certificati orbit-spectral
Floquet/monodromy (A20) sono graft nominati, non implementati: la riga di
registro apre con "five CycleFamily/VI.1 contract additions, none wired"
(findings :1926, owner "F2 / VI.1") [W2-R4]; (iii) il test del
pin è UN DECIDER DELLA ROADMAP, non un rinvio: CFD-1 è definito esattamente
come "test del pin su configurazione accoppiata reale" (PROGRESS :411-412), e
l'ask-dati R20 nomina cosa lo chiuderebbe lato hardware (findings :2148,
:2153). OPEN dichiarato: la provenienza hardware del pin in steady state è
A-5; se il pin cade in un regime, il record ha già la mappa d'uscita (C59
alternatives; H-AM1 exit dichiarata in forchetta (i) WORST, M0:1343).

**Q5. "Il vostro bound Gap A usa curvature misurate su J_red: perché la
curvatura del modello ridotto dovrebbe dire qualcosa sul 3D vero?"**
Dal record: NON lo assumiamo — è esattamente H-G6, e finché L_H (la faccia a
livello curvatura del residuo di riduzione) non è derivata, "the GRADIENT route
licenses NO number even a-posteriori from the measured carrier alone"
(M0:1348). Esiste la value-route con floor misurato legittimo (mu_red) ma a
tasso sqrt e a classe estimate, mai spacciata per copertura d'ottimo
("A value-level bound is NEVER passed off as optimum coverage", M0:1348).

**Q6. "PB-2 dipende da p_b, e voi stessi citate Humphreys: il vostro ottimo
truncated-plug non sarà un artefatto della chiusura?"**
Risposta dal record: è il rischio che abbiamo REGISTRATO noi, a grado
foundation (C61 note: "the closure choice moves the DESIGN, not just the
value", choice_ledger :830). Per questo lo slot N2 è NEVER e non un default:
il verdetto WG10 su Veen è "N2 MUST REPLACE IT" (:824), l'unico dato RDE
esistente (Purdue CTAP, transizione Pa/Pc~0.15) è nominato (:825), e il
transfer nozzleless→plug è dichiarato ANALOGIA (findings :2095). Il computo
PB-2 entrerà nel record CON la sensibilità alla chiusura dichiarata, o non
entrerà (trigger C61 :829).

**Q7. "La value condition richiede Gap A < Gap B, ma Gap A è incomputabile e
delta/L_H sono UNDERIVED: come verificherete MAI la condizione?"** [W2-R9]
Risposta onesta dal record: oggi la condizione è INDECIDIBILE, e lo diciamo —
"delta AND L_H UNDERIVED ... NO argmax-shift number exists at any grade, and
none from the measured carrier alone" (M0:1348). Il percorso di decidibilità
è però ordinato nel record, ogni passo con la sua classe: (i) M-RED misura
eps_U (il livello uniforme di value-error sul basin esplorato, sweep-sup dei
value legs (A)-(B), classe SAMPLED-SUP/estimate); (ii) la VALUE-ROUTE dà il
bound a-posteriori |argmax shift| ≤ 2·sqrt(eps_U/mu_red) — l'unica rotta il
cui floor mu_red è legittimamente il carrier misurato as-is — a classe
estimate, a tasso sqrt, mai spacciata per copertura d'ottimo ("A value-level
bound is NEVER passed off as optimum coverage", M0:1348); (iii) la GRADIENT
route (delta/mu_curv), che sola può stringere al livello dei delta in-class,
attende delta e L_H dai deriver nominati in ordine "X-T3QS-5F (F2) →
C51-route-B → M-RED gradient rider → R22-CFD-1" (M0:1348; pipeline map :237
E29); (iv) R22-CFD chiude con lo spot-check. OPEN dichiarato: fino a M-RED
non esiste NESSUN numero su nessun lato della disuguaglianza — la condizione
è un rejector armato, non un verdetto anticipato.

---

## 5. Cosa deve dire il deck

1. **Il value case è una condizione falsificabile, non una promessa**: Gap B
   misurabile in-house (paired-run, baseline di record = Veen/Angelino-at-mean;
   l'aggiunta di I4/Rao-GENO come seconda baseline mean-designed nella stessa
   run = proposta dichiarata, non record [W2-R2]), Gap A bounded-only; il
   programma vale se "Gap B material AND Gap A < Gap B" — e lo si dice così.
   [Frame di record, checkpoint :466-472; classi: definizione + SCHEMA]
2. **PB-2 è la bandiera**: il primo problema concreto che NESSUN design
   single-phase risolve (rottura del nesting T4, max∫ < ∫max) — posato con
   precisione, MAI computato, e il deck dichiara cosa manca (baseline I4 +
   chiusura p_b N2) e il warning Humphreys ×2.45. La slide porta la novità
   SOLO nella locked formulation D-06 ("the first genuinely averaged and
   NON-COLLAPSING shape problem of the program (a CYCLE instance)", never
   abbreviate) col near-miss Efremov-Kraiko 2004 (no wall contour) come
   query-bound esplicito; ogni frase tipo "first averaged-thrust variational
   problem" è DEAD of record (M0:2320-2329) [W2-R5]. [Enunciato problem book
   :532-537 + C61 NEVER + [ADV] Humphreys + D-06 locked]
3. **La slide onesta della forchetta**: 6 canali, ogni cella al suo grado, "NO
   cell above its held evidence class"; sizing ~1% [REP], ranking OPEN (R26),
   nessun referee esterno esiste — per nessuno. [M0:1306-1348; D-44 vincola la
   slide stessa]
4. **La roadmap ha deciders, ordine e classi di costo** (cheap in-house /
   paired demo / ~12M-cell cost class; prezzi assoluti = OPEN, dossier
   post-M-RED) [W2-R7]: M-RED (in-house, cheap decisive
   unlock) → CFD-2 (paired, template Li-Xu, barra = eps di M-RED) → CFD-1
   (~12M-cell, decisione post-M-RED, G1 haste-risk dichiarato). [PROGRESS
   :407-421; pipeline map :77; decisioni utente ratificate]
5. **Le ASK sono enumerate e minimali**: collaborazione/procurement CFD-1;
   dati motore per il pin (imaging steady-mainstage o transition durations —
   R20); 3+3 documenti fermi + W-01/02/03; canale paper JPP. [PROGRESS
   :418-421; findings :2148; literature_registry :1232-1248]
6. **L'onestà è il vantaggio competitivo, e va detta come metodo**: falsificatori
   armati PRIMA dei numeri (claims :2262), gate D-44 che vincola questo stesso
   deck, ladder P34 dichiarata per ogni claim engine-level in slide. [TERM
   milestone, ADVISORY_Spres_prompt :233-235; ARMED GATE; finding :2538]

---

## 6. Legenda minima (per il consumo storyboard, un termine = una riga) [W2-R10]

- **M-RED**: campagna di misura in-house dell'errore di riduzione (eps) del modello per-fase, prima campagna della fase F2.
- **CFD-2**: demo CFD accoppiata "paired" (nostro design vs baseline, template Li-Xu 2025), in coda F2.
- **CFD-1**: simulazione CFD massima (~12M-cell cost class) su configurazione accoppiata reale — il test del pin; decisione utente post-M-RED.
- **R22**: la linea di verifica CFD del programma (M-RED → CFD-2 → CFD-1) che decide le soglie di adeguatezza.
- **F2/F4b/F5**: fasi del piano di sviluppo (D6): F2 = teoria+campagne correnti; F4b = finestra truncated-plug; F5 = finestra dati/hardware.
- **I4**: baseline a stato medio singolo (⟨Pc⟩, T0, γ) con design classico Rao/GENO (problem book).
- **N2**: lo slot dichiarato (non ancora aggiudicato) per la chiusura di base pressure p_b del programma.
- **eps / eps_U**: errore di riduzione misurato da M-RED; eps_U = suo livello uniforme sul basin esplorato (sweep-sup).

---

## Disposizione riparazioni (onda 2)

| Finding # | Classe | Disposizione |
|---|---|---|
| 1 | REPAIR | APPLICATO [W2-R1] — Q1: promessa di adeguatezza sostituita con "datum che stringe la soglia R26, sempre bracket con provenienza; D-44 vale in entrambe le direzioni" |
| 2 | REPAIR | APPLICATO [W2-R2] — §1.2, claim 6, Q2, deck 1: fusione famiglia-vs-I4 dichiarata PROPOSTA di consolidamento; baseline di record di Gap B (Veen/Angelino-at-mean) distinta da I4 (Rao/GENO) |
| 3 | REPAIR | APPLICATO [W2-R3] — Q3: accusa al campo riformulata al contenuto dell'ancora M0:1335-1339 (nessun lavoro ottimizza il 3D vero; sweep = ranking-signal only), senza attribuzione di intenti |
| 4 | DOWNGRADE | APPLICATO [W2-R4] — Q4(ii): stato della guardia declinato (T0-flatness armato; f_cycle e A20 nominati "none wired", findings :1926, owner F2/VI.1) |
| 5 | GAP | APPLICATO [W2-R5] — §1.2 + claim 5 + deck 2: locked formulation D-06 verbatim + near-miss Efremov-Kraiko 2004 come query-bound (ancora verificata M0:2320-2329) |
| 6 | REPAIR | APPLICATO [W2-R6] — §1.2: classe della rottura ancorata alla sharpness clause M0:2316-2319 + "nesting ... THEOREM (standard)" M0:3524-3525 (ancore verificate) |
| 7 | DOWNGRADE | APPLICATO [W2-R7] — Q2(c) + deck 4: "prezzata"/"prezzi" sostituiti con "cost-classed"/"classi di costo"; prezzi assoluti = OPEN, dossier post-M-RED |
| 8 | NOTE | APPLICATO [W2-R8] — unita' di "~0.3M" marcata [INF] (non dichiarata all'ancora) + divieto di slide; miglioramento senza rischio |
| 9 | GAP | APPLICATO [W2-R9] — nuova Q7 sull'indecidibilita' odierna di "Gap A < Gap B" con percorso di decidibilita' dal record (value-route 2*sqrt(eps_U/mu_red) verificata a M0:1348, deriver chain E29) |
| 10 | GAP | APPLICATO [W2-R10] — legenda minima 8 righe in coda (§6): M-RED, CFD-1/2, R22, F2/F4b/F5, I4, N2, eps |
| 11 | NOTE | APPLICATO [W2-R11] — Q2: i due "primo" query-bounded (per costruzione / perimetro R20 search-proven); miglioramento senza rischio |
