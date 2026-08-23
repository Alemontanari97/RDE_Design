# CH4 — La macchina e le scelte: pipeline, engine, certificati — e i perché

[S-PRES ricostruzione critica, 2026-08-22. CITE-ONLY: questo capitolo non
aggiudica nulla; ricostruisce dal record e dichiara gli aperti. Ogni claim
porta ancora (file:riga o anchor) e classe di rigore. Convenzione locale:
oltre alle classi di record (THEOREM/THEOREM*/SCHEMA/CONJECTURE/PRACTICE,
[REP]=riproducibile con carrier committato, [ADV]=advisory, [INF]=inferenza
dichiarata, [SE]=sampled-estimate), uso **[PED]** per le spiegazioni
da-zero di concetti standard da manuale (trust region, AD, adjoint, MoC):
sono pedagogia per il panel, NON claim del programma, e non portano ancora
di record.]

---

## 1. Ricostruzione

### 1.1 Perché esiste "una macchina" e non solo un codice

Il programma è vincolato dalla disciplina R5 (`CLAUDE.md`, sezione R5):
nessun numero senza script committato + test; i test devono poter
RIGETTARE (rejector), non solo confermare; tolleranze derivate, non
magiche; ogni claim con falsificatore. La "macchina" è quindi tre cose
insieme: (a) un **engine differenziabile** che risolve il problema di
design (MoC per-fase + ottimizzatore), (b) una **fabbrica di certificati**
che accompagna ogni numero con soglie derivate e oracoli che possono
bocciarlo, (c) una **mappa delle decisioni** che rende ogni scelta
algoritmica un oggetto con status, alternative pesate e falsificatore
(`docs/choice_ledger.yaml`, 62 righe; misura SR-12 citata in
`docs/rde_nozzle_pipeline_decision_map.md:33-36`).

### 1.2 La pipeline a 8 stadi (l'oggetto di navigazione di record)

La mappa di record è `docs/rde_nozzle_pipeline_decision_map.md`
(S-FOUNDATIONS-C4, 2026-08-21), dichiarata **CITE-ONLY** (":7-14": zero
nuova aggiudicazione; i conflitti si risolvono CONTRO la mappa). Numeri di
struttura, misurati nella finestra della mappa (SR-12, `:262-295`):

- **8 stadi**; **79 nodi totali** = 62 nodi ledger (C1..C62) + 17 nodi
  non-ledger (roster esatto `:271-274`: PIN-WAVE, blocco findings di
  contratto, S-5F, ROUTE-B, R22-CFD, CLG, SDP-CAND-8, M-RED, T-DISC,
  R22F-FORCHETTA, OBJ-DOM, DELTA-CARRIER, OPTSHIFT, D-44, P34, H20,
  DUTY-10). Classe: [REP] (comando grep citato nella mappa).
- **45 voci di arco** in §9 = 44 archi + 1 anti-arco dichiarato E34
  (`:275-283`); confine di completezza DICHIARATO (`:193-197`: §9 non è
  la chiusura di tutte le citazioni pairwise).
- **4 superfici cluster** (`:199-220`): **A** = cluster engine F2-entry
  {C31, C57, C58, C60, [P-IPADJ], SDP-CAND-8}; **B** = cluster contratto
  {C52, C53, C54}+C50; **C** = ship-gate OBJ-DOM ↔ DELTA-CARRIER (E9);
  **D** = arco Veen → R8 → C61 → ADR-D4 (espansione esterna).
- **Tally di status** (62 nodi ledger, `:287-295`, comando citato):
  **12 DECIDED / 36 MIXED / 12 NEVER / 2 SINGLE-AUTHOR**; riconcilia con
  l'header del ledger: YES.
- La mappa ha superato un passaggio refuter dedicato: **0 BREAK /
  0 REPAIR / 5 AMENDMENT / 4 NOTE** (`:317-339`, disposition table).

Gli stadi, in una riga ciascuno (ancore = le sezioni STAGE della mappa):

1. **DATA CONTRACT** (`:57-67`) — cosa entra: il dato d'interfaccia
   (onda rotante periodica pura = PIN STANDING dell'utente, `:61`),
   metrica d'incertezza (C50), piazzamento Γ_d (C53), slot P_amb (C55).
2. **REPRESENTATION** (`:69-78`) — come si rappresenta la soluzione
   per-fase: fitted-front marching (C49), scala S-5F/route-B/3D,
   forma temporale del funzionale (C59: cycle-average, canonica DENTRO
   il pin).
3. **MARCH & UNIT PROCESSES** (`:80-100`) — il MoC concreto: start line
   Sauer (C12), processo d'asse (C13), thermo a tabelle (C24-C26),
   guardie di choking (C13/C15/C45).
4. **CERTIFICATES & QUALIFICATION** (`:102-116`) — la fabbrica dei
   certificati: scala metrica (C19), qualificazione (C20), costanti di
   floor NTF (C18), lint numerico (C47), backend SDP (SDP-CAND-8).
5. **ESTIMATOR & BANDS** (`:118-130`) — barre d'errore su J: DWR/C11,
   mesh law C9, ruoli adjoint C56, campagna M-RED.
6. **OPTIMIZER & ENGINE** (`:132-163`) — il driver: TR-Newton (C31-C40),
   base spline (C1-C8), quadratura di fase (C62), stack AD (C58, C48).
7. **AGGREGATION & FRONTIER** (`:165-174`) — dal singolo run al claim:
   forchetta di adeguatezza [R22F-FORCHETTA], teorema di separazione
   [T-DISC], OBJ-DOM, delta-carrier con ship-gate.
8. **VERDICT & CLAIMS** (`:176-185`) — cosa si può dire fuori: gate D-44
   sui claim pubblici di adeguatezza, gerarchia di evidenza P34,
   scheduling R22-CFD.

**Lettura onesta dei 12 NEVER** (roster `:293`; finestre per-riga
`:296-309`): NEVER = "mai pesata contro alternative", NON "ignota". Ogni
riga NEVER è **trigger-armed** con owner e finestra dichiarati (es. C60
NAND/SAND → finestra engine F2-entry come CLUSTER; C55 → prima
istanziazione multi-punto di P_amb; C61 p_b → finestra N2/F4b). Due sono
**strutturalmente vuote fino al trigger**: C55 (default single-point
P_amb: "question EMPTY under the default", `:66`) e C59 (cycle-average
canonico dentro il pin: la domanda è vuota finché il pin regge, `:78`).
I 36 MIXED sono invece scelte **aggiudicate-split**: incumbent che porta
il verdetto + target/challenger con falsificatori pinnati e duty F2
(vedi le righe lette in §1.3). Classe di questo paragrafo: [REP]
(mappa + righe ledger citate).

### 1.3 Le scelte portanti, col perché (concetto da zero → scelta →
### alternative → falsificatore)

**(a) C58 — lo stack differenziabile: JAX, discreto-esatto.**
[PED] *Automatic differentiation* (AD): il programma calcola il gradiente
di un output rispetto a TUTTI gli input applicando la chain rule alle
operazioni elementari del codice stesso — niente differenze finite
(rumore di passo), niente derivazione a mano (errore umano). Il punto
metodologico: si differenzia **il problema discreto che si risolve
davvero**, non un'idealizzazione continua — così il gradiente è esatto
(a precisione macchina) per la J effettivamente calcolata.
- *Scelta di record*: JAX primario, `custom_vjp` + implicit-function
  rule sui solve di Newton interni ("never unrolled")
  (`docs/rde_nozzle_G0_decision.md:17-19`, DIR-G0, 2026-07-17).
- *Evidenza*: 52/52 entrate di Jacobiano dentro tolleranza DERIVATA con
  controllo negativo rigettato (G0 §2(i), `:33-38`); overhead
  dell'adjoint ~1.5% del solve primale (`:47-59`, con caveat host di
  record: decisionale è il RAPPORTO grad/solve, host-invariante);
  oracolo cross-code X-GENOXC (GENO = il codice MoC Fortran di
  riferimento del gruppo, repo indipendente, mai assunto bug-free
  [W2-R8]): 100% di 218 triangoli dentro banda di troncamento derivata,
  controlli negativi che rigettano (corruzione 1% → 100%→0%; pairing
  C+/C- errato → residuo 84x) (`:94-104`). Scope DICHIARATO in G0 per
  prevenire over-reading (`:202-210`): X-GENOXC certifica il PROCESSO
  UNITARIO interno nel core supersonico pulito (il mattone
  differenziabile), NON la macchina di generazione profili; il livello
  assemblato è coperto dall'oracolo 91/91 del run S18 (§1.4). [W2-R6]
- *Alternative pesate*: Julia+Enzyme = alternate DICHIARATO, non
  benchmarkato su questo host — detto in chiaro (G0 §4 `:199-201`);
  hand-coded adjoint; gradient-free (ledger C58,
  `docs/choice_ledger.yaml:783-793`).
- *Falsificatore*: loop-speed flip clause ARMATA e quantificata
  (T1 = grad/solve ≤ 4: misurato 1.593 PASS; T2a: 0.116 s ≤ 1.197 s
  PASS, gate di produzione APERTO; review S25: il firing T2 di S18 era
  costo strutturale, NON throughput di linguaggio → la decisione STA)
  (G0 §4, note datate `:144-198`). Status ledger: MIXED, ri-censimento
  al cluster engine F2-entry (C58 owner, `:792`). Classe: [REP].

**(b) C56/C11 — adjoint discreto e DWR (con l'antenato Hoffman 1967).**
[PED] *Adjoint*: per un vincolo R(u,θ)=0 (il flusso) e un obiettivo J,
si risolve UNA equazione ausiliaria per il campo dei moltiplicatori λ
(il "prezzo" locale di una perturbazione del residuo); con λ in mano,
dJ/dθ su TUTTI i gradi di libertà costa un solo solve in più — invece di
un solve per ogni parametro. È la stessa matematica dei moltiplicatori di
Lagrange. L'antenato nel campo degli ugelli: **Hoffman 1967**, "general
method for optimum thrust nozzle contours for chemically reacting gas
flows" — campi di moltiplicatori per flusso reagente
(`docs/literature_registry.yaml:372-378`, status READ-INTEGRAL; il suo
E-residual Eq. (78) è consumato come certificato VI.3). [PED] *DWR*
(dual-weighted residual): lo stesso λ pesa i residui locali per stimare
l'errore SU J — barre d'errore orientate all'obiettivo.
- *Scelta di record (C56)*: adjoint **discreto AD** per tutti e tre i
  ruoli (gradiente / peso DWR / indicatore di adattamento); la linea
  continua characteristic-native (Ancourt 2023, Lozano-Ponsin 2025) =
  frame di formulazione + REFEREE, mai il peso ("a weight cannot referee
  itself" — verbatim nella nota C11, `docs/choice_ledger.yaml:279`, e
  supplemento `VERDICT_C9C11_supplement.md#4.2` [W2-R11]) (ledger C56,
  `docs/choice_ledger.yaml:760-769`).
- *Scelta di record (C11)*: DWR = TARGET primario per le barre su J;
  Richardson/GCI = referee permanente; bande interim = observed-p GCI
  (ledger C11, `:269-279`).
- *Falsificatore*: **F11d, due gambe** — (1) convergenza del peso AD
  all'adjoint analitico sull'oracolo quasi-1D Giles-Pierce; (2) residui
  di compatibilità (Eqs. (30)/(31) ACE/Lozano-Ponsin) ai band sites di
  produzione. UNA gamba che spara blocca la promozione F11a e riapre la
  riga C56 (ledger C11 `:279`, C56 `:768-769`). Ancoraggio pubblicato:
  Hicken-Zingg Definition 1 + il caveat p.164 che la consistenza primale
  NON implica quella duale — ragione pubblicata per cui F11d non si può
  condonare (nota C56 `:769`). Classe: [REP] (aggiudicazione);
  dual-consistency della marcia = SCHEMA (P2 Lemma B par.4.5, via nota
  C56).

**(c) C49 — fitted-front marching (e cos'è il MoC).**
[PED] *Method of characteristics* (MoC): nel flusso supersonico
l'informazione viaggia lungo linee caratteristiche; il MoC integra le
equazioni esatte lungo quelle linee, cellula per cellula — precisione
alta e discontinuità (urti, fronti) trattabili come oggetti espliciti
"fittati" con le condizioni di salto, invece che "catturati" spalmandoli
su più celle di una griglia.
- *Scelta di record*: fitted-front characteristic marching = UNICO
  portatore di certificato (classe S1 piecewise-smooth certificata);
  architettura two-tier: l'esploratore "captured" è un tier di scoperta
  nominato e build-gated, mai il certificatore (ledger C49,
  `docs/choice_ledger.yaml:682-692`; risposta di record alla domanda
  utente "perché si fitta una soluzione che potrebbe essere catturata").
- *Alternative pesate*: capturing adjoint-consistent come solver unico;
  two-tier col carrier |J_captured − J_fitted|; implicit shock tracking
  moderno (HOIST/Zahr) = upgrade path nominato con entry gate su
  checklist pubblicate (nota C49).
- *Falsificatore*: quattro falsificatori pinnati sul tier esploratore +
  la frontiera fit-vs-capture governata dal budget DWR (campagna C11 leg
  (b)) (nota C49). Classe: [REP] (aggiudicazione wave-2, ZERO finding
  refuter sulla riga).

**(d) C31 — TR-Newton segmentato a curvatura misurata.**
[PED] *Trust region*: a ogni iterazione si costruisce un modello
quadratico locale di J e lo si minimizza SOLO dentro una palla di raggio
Δ dove il modello è credibile; se la predizione concorda con la realtà
(ratio ρ) la palla cresce, sennò si stringe. Rispetto alla line search è
il modello a essere vincolato, non il passo. *Quasi-Newton (BFGS)*:
curvatura STIMATA accumulando differenze di gradienti su molte
iterazioni. *Interior point (IP)*: i vincoli diventano barriere e ci si
muove nell'interno.
- *Scelta di record*: engine = scipy trust-constr (path IP in uso da
  S22) sotto disciplina INFORMATION-ONLY dei moltiplicatori fino a
  [P-IPADJ]; driver di record = **TR-Newton segmentato a curvatura
  misurata**: i flip della wall-search rendono i segmenti single-step →
  la curvatura accumulata alla BFGS non fa in tempo a formarsi → Hessiana
  PIENA misurata per segmento (n+1 differenze forward del gradiente
  adjoint esatto), attivata SU NUMERI (memoria `s18-brick2-closed`
  :32-40; ledger C31, `docs/choice_ledger.yaml:481-493`).
- *Alternative pesate*: IPOPT, filter SQP, SLQP, Uno (= flip candidate,
  install O5-class), proximal-bundle (ledger C31 `:484-489`); A/B
  pinnato a constraint-set identico con guardia identical-certified-
  outcomes; i 10 input di spec arm-B (dossier Uno) entrano nella spec
  [P-IPADJ] per ordine utente (nota C31 `:493`).
- *Falsificatore*: engine falsifiers one/two/three (VERDICT_wave2
  par.1.1, via ledger C31); [P-IPADJ] = prima azione engine F2 sul
  critical path di C28. Classe: [REP].

**(e) C24 — thermo a tabelle.**
[PED] Le proprietà termodinamiche (gamma(T), h(T), ...) servono milioni
di volte nel loop e devono essere differenziabili: si precalcolano
tabelle lisce da un generatore di fiducia (Cantera) e l'engine legge
SOLO le tabelle — il contratto d'interfaccia è la tabella, non la
libreria.
- *Scelta di record*: [X-THC1] tabelle quintic C1 (backend-1), status
  DECIDED; direttiva S11: tables = interface contract (ledger C24,
  `docs/choice_ledger.yaml:408-416`; memoria `thermo-tabulated-backend`).
- *Alternative/condizioni*: NASA-direct = solo oracolo (condizione C-A
  SCARICATA nel carrier [X-THC1]); dCp-ingest gated C-B; box tabella
  C25 e comportamento out-of-box C26 = righe SEPARATE (C25 NEVER, F2)
  (ledger C24 nota; mappa `:90-92`). Classe: [REP].

**(f) C1 — base spline del design.**
[PED] La parete dell'ugello è rappresentata da una spline cubica: pochi
gradi di libertà (le altezze ai nodi) → lo spazio in cui l'ottimizzatore
cammina.
- *Scelta di record*: cubica interpolante clamped/natural,
  heights-as-dofs = incumbent verdetto-portante; direzione CONVERGIUTA:
  migrazione al chart control-polygon B-spline dello STESSO spazio
  spline certificato (certificati di ammissibilità Bernstein-esatti)
  (ledger C1, `docs/choice_ledger.yaml:164-174`).
- *Alternative pesate*: B-spline control polygon, CST (Kulfan),
  Hicks-Henne (`:167-170`); prior dof-budget Masters 2017 con scope di
  trasferimento dichiarato.
- *Falsificatore*: tre falsificatori di migrazione; l'incumbent regge
  finché non passano (duty F2-C1-CONTROL-CHART-MIGRATION). Classe: [REP].

**(g) C19/C20/C18 — i certificati.**
[PED] Un *certificato*, qui, è un test meccanico che accompagna un
numero: una soglia DERIVATA (da aritmetica floating-point, ordine dello
schema, condizionamento — mai "0.01 perché sì") + un oracolo che può
RIGETTARE. Un numero senza certificato non entra nel record (R5).
- *C19 (scala della metrica)*: sc = max(1, max|z|) scalare, RITENUTA SU
  COSTO con censimento di laxity derivato dal headroom GAP-29; disparità
  per-componente di record ~3 decadi DICHIARATA (posizioni certificate
  solo a ~100 eps|u|; nessun verdetto compromesso — bande
  Richardson-dominate) (ledger C19, `docs/choice_ledger.yaml:355-363`).
- *C20 (qualificazione del certificato)*: incumbent = one-extra-step
  ratio NON qualificato; architettura a tier aggiudicata (Tier-0
  monitor branch/fold sempre attivi, Tier-1 banda kappa-derivata,
  Tier-2 referee Kantorovich/Krawczyk) = duty F2 (ledger C20,
  `:365-376`).
- *C18 (costanti di floor)*: NEWTON_TOL_FACTOR=100 — non più numero
  magico: **istanza VALIDA della forma derivata NTF = η·κ_q**, blocco
  M0:3649-3766 [LAND-C4-LA2] con classi NTF-2/3 = THEOREM*, NTF-1/4 =
  SCHEMA, NTF-5 = PRACTICE e falsificatori NTF-1..4 (mappa `:109`);
  e lo sweep GAP-29 ha MISURATO che la soglia è load-bearing:
  NTF/2 → il verdetto di certificazione FLIPPA (margine x2
  load-bearing), C_FLOOR/2 e C_OPS/2 ≥ 2x headroom
  (`docs/rde_nozzle_PROGRESS.md:155-160`; ledger C18 `:344-353`,
  status SINGLE-AUTHOR: derivazione della costante = duty F2-live).
  Classe: [REP] + THEOREM*/SCHEMA sul blocco NTF.

### 1.4 I numeri engine (con lo stage di evidenza P34 dichiarato)

Dichiarazione P34 (mappa `:181`): la gerarchia di evidenza per claim
engine-level è **V0 continuous verification → per-champion validation →
test terminale pre-registrato al banco**; la gerarchia stessa NON è mai
stata aggiudicata (uno dei due gap FORK-141 genuini — l'altro è H20;
ordinali di record H20 = 1 of 2, P34 = 2 of 2, mappa PM-6 `:332`
[W2-R10]) e S-PRES porta il rider
LIGHT-INSTANTIATION: ogni claim da slide dichiara il suo stage. **Tutti
i numeri qui sotto sono stage V0 (verification): nessuna validazione
sperimentale, nessun banco.**

- **Run end-to-end di record (S18)**: TR-SQP da start perturbato 1.5% →
  **KKT transversality 7.745e-02 ≤ soglia derivata 1.156e-01 = PASS**
  (istanza di trasversalità Rao via gradiente); **oracolo cross-code
  91/91 dentro banda derivata** (max|dy| 1.86e-03), N3 discrimina;
  J* = 2.7761688e+07 (J = il funzionale di spinta cycle-averaged
  per-fase del programma, definizione di record in CH1:
  J[Σ] = ∫ F[Σ; s(ξ)] dμ(ξ), `CH1_formulation_ladder.md:56` — qui il
  suo valore discreto al run di record [W2-R7]); 4 tentativi
  dichiarati, nessun numero da run uccisi (memoria
  `s18-brick2-closed:27-39` — metà VERDICT di record; carrier
  committato `validation/PROGRESS_2026-08-06_S18_brick2run.md`,
  verificato su disco [W2-R9]).
  Classe: [REP].
- **Velocità (S25/S25-bis, criterio pessimistic-end PRE-REGISTRATO)**:
  SEGMENTO = MET: 14.9 s [M-D] / 20.1 s [M-E] vs ≤ 30; CAMPAGNA = MET:
  ~10-14 min pessimistic vs ≤ 25 (`docs/rde_nozzle_PROGRESS.md:119-123`;
  riga censimento R22 `:200`). Catena di record: 100.84 s → 32.09 →
  record 5.58 s; **replay 0.236 s; val_grad 0.449 s; Hessiana 4.5-7.0 s
  (≤ 8)** (`:124-125`). Carrier: [X-SPDB] (`:166`, `:200`). Classe:
  [REP], con caveat host di record ereditato da G0 §2(ii) (i rapporti
  sono host-invarianti, i secondi assoluti no) e riga registry
  speed-measurement-variance (`:149-150`).
- **Gate di produzione**: T2a clean-host 0.116 s ≤ 4×0.299 s = 1.197 s
  (t_GENO della re-run S18; la misura 0.286 s è la nota S17
  FAIL-as-implemented, `:148`) = PASS, gate APERTO (G0 §4 nota S18
  `:160-171`); T1 grad/solve 1.593 ≤ 4 (`:168`). Classe: [REP]. [W2-R1]
- **Un numero di onestà**: il floor di variabilità cross-lowering
  dell'adjoint attraverso ~250 solve impliciti è ~1e-8 relativo sul
  gradiente — scoperto perché un gate (m6gate) ha SPARATO, causa radice
  isolata, forma corretta misurata dentro il bound derivato; disciplina
  a registro: ogni confronto di gradienti pinna UNA lowering
  (`docs/rde_nozzle_PROGRESS.md:130-154`). Classe: [REP].

### 1.5 Cosa la macchina NON copre (onestà interna)

- **S-CERT (audit ostile di certificazione, 2026-08-13): verdetto
  vincolante NON-CERTIFICABILE, 2 P0 a HEAD** — il P0 (vii) riparato in
  chiusura dichiarata; il P0 **staleness import-closure** resta con
  owner F2. Delta vs l'audit 2026-08-07: il vecchio tier P0 è
  consumato-verificato; i difetti sono MIGRATI dall'oggetto al
  CERTIFICATORE; MC8 sopravvive 8/8
  (`docs/rde_nozzle_PROGRESS.md:211`, riga R33). **Cosa significa
  davvero**: non "l'engine è rotto", ma "la catena che certifica
  l'engine non passa il proprio stesso standard a HEAD" — e lo standard
  è stato fatto misurare da auditor ostili context-free per design.
  Classe: [REP] (verdetto d'audit di record).
- **OBJ-DOM**: l'obiettivo di record a F2-entry è il fix-A (il funzionale
  attuale omette il pannello di gola: OBJDOM-1/3 THEOREM, OBJDOM-2
  THEOREM*); l'implementazione è OPEN, trigger = primo verdetto F2 che
  consuma dJ/dthB E prima che il delta-carrier R2 spedisca (mappa
  `:172`; findings `:211-212` ivi citate). Classe: THEOREM/THEOREM*
  aggiudicati, IMPL OPEN.
- **F11d mai eseguito**: la consistenza dell'adjoint discreto è
  aggiudicata con falsificatore pinnato, non ancora misurata ai band
  sites (§1.3(b); owner F2-C11-ESTIMATOR-CAMPAIGN).
- **Cluster engine F2-entry non chiuso**: [P-IPADJ] + C57 (tier
  esplorazione: NEVER) + C60 (NAND/SAND: NEVER) + ri-censimento C58 +
  SDP-CAND-8 mint-or-retire — tutta la superficie A si aggiudica alla
  finestra F2-entry (mappa `:199-206`, `:296-309`).
- **Nessuna validazione sperimentale**: stage P34 = V0 ovunque (§1.4);
  la gerarchia P34 stessa è un gap aperto (mappa `:181`).
- **Julia/Enzyme mai benchmarkato su questo host** (G0 §4 `:199-201`) —
  il verdetto JAX poggia su "esercitato vs non esercitato", detto
  in chiaro.
- **Blind spot wrong-branch**: tutti e tre i ruoli adjoint linearizzano
  alla root rigiocata e ereditano il blind spot di branch finché C20
  Tier-0 non atterra (nota C56, `docs/choice_ledger.yaml:769`).

---

## 2. Stato per-claim

| # | Claim | Classe | Ancora | Carrier / falsificatore |
|---|---|---|---|---|
| 1 | Pipeline: 8 stadi, 79 nodi (62 ledger + 17), 45 voci-arco, 4 superfici; mappa CITE-ONLY | [REP] (misura SR-12) | `docs/rde_nozzle_pipeline_decision_map.md:262-295` | refuter pass 0-BREAK (`:317-339`) |
| 2 | Tally status 12 DECIDED / 36 MIXED / 12 NEVER / 2 SA; riconcilia con header ledger | [REP] | mappa `:287-295` (comando grep citato) | lint famiglia (xix) sul ledger |
| 3 | AD fedele: 52/52 Jacobiano in tolleranza derivata; adjoint overhead ~1.5%; X-GENOXC 218/218 con controlli negativi (scope: processo unitario; livello assemblato = 91/91 S18 [W2-R6]) | [REP] | `docs/rde_nozzle_G0_decision.md:33-59, :94-104, :202-210` | controlli negativi: vjp corrotto rigettato; corruzione 1% → 0% in banda; pairing errato 84x |
| 4 | Flip clause linguaggio ARMATA e NON SPARATA: T1 1.593 ≤ 4; T2a 0.116 ≤ 1.197 s; gate produzione APERTO | [REP], carrier X-LSG0 | G0 §4, note `:144-198` | T2a futuro FAIL = strutturale → flip diretto |
| 5 | Driver di record: TR-Newton segmentato, Hessiana piena misurata per segmento (attivazione su numeri) | [REP] | `validation/PROGRESS_2026-08-06_S18_brick2run.md` (log committato, ancora primaria [W2-R9]); memoria `s18-brick2-closed:32-40` (indice); ledger C31 `:481-493` | engine falsifiers one/two/three (VERDICT_wave2 par.1.1) |
| 6 | Run di record: KKT 7.745e-02 ≤ 1.156e-01 derivato; oracolo 91/91 (max\|dy\| 1.86e-03); J* 2.7761688e+07 (J = funzionale di spinta cycle-averaged, def. CH1 [W2-R7]) | [REP] | `validation/PROGRESS_2026-08-06_S18_brick2run.md` (ancora primaria [W2-R9]); memoria `s18-brick2-closed:27-39` (indice) | banda derivata + N3 discrimina; 4 tentativi dichiarati |
| 7 | Velocità MET: segmento 14.9-20.1 s vs ≤30; campagna ~10-14 min vs ≤25; val_grad 0.449 s; replay 0.236 s | [REP], carrier [X-SPDB] | `docs/rde_nozzle_PROGRESS.md:119-125, :200` | criterio pessimistic-end pre-registrato; caveat host dichiarato |
| 8 | Floor cross-lowering ~1e-8 rel sul gradiente; disciplina una-lowering a registro | [REP] | PROGRESS `:130-154` | m6gate (ha sparato — il rigetto È il verdetto); bound K_RICH × max(asym) |
| 9 | Soglia di certificazione load-bearing: NTF/2 flippa il verdetto; C_FLOOR/C_OPS ≥ 2x headroom | [REP] | PROGRESS `:155-160`; ledger C18 `:344-353` | sweep GAP-29 eseguito (s25bis_gap29_sweep.json via nota C18) |
| 10 | NTF=100 = istanza valida della forma derivata η·κ_q | THEOREM* (NTF-2/3), SCHEMA (NTF-1/4), PRACTICE (NTF-5) | mappa `:109` → M0:3649-3766 [LAND-C4-LA2] | falsifiers NTF-1..NTF-4 come stampati |
| 11 | Adjoint di record = discreto AD su tutti e tre i ruoli; linea continua = frame + referee | [REP] (aggiudicato); dual-consistency = SCHEMA | ledger C56 `:760-769` | F11d 2 gambe; UNA che spara riapre la riga |
| 12 | C49: fitted-front = unico portatore di certificato; capturing = explorer nominato build-gated | [REP] (wave-2, 0 finding refuter) | ledger C49 `:682-692` | 4 falsificatori pinnati; carrier \|J_capture − J_fitted\| |
| 13 | S-CERT: NON-CERTIFICABILE, 2 P0 ((vii) riparato; staleness import-closure → F2); difetti migrati oggetto→certificatore; MC8 8/8 | [REP] (verdetto audit) | PROGRESS `:211` (riga R33) | audit ostile context-free = il rejector stesso |
| 14 | OBJ-DOM: fix-A obiettivo di record a F2-entry; impl OPEN | THEOREM (OBJDOM-1/3), THEOREM* (OBJDOM-2) | mappa `:172` (findings `:211-212`) | trigger: primo verdetto F2 con dJ/dthB, prima dello ship delta-carrier |
| 15 | D-44: ogni claim pubblico di adeguatezza è GATED (forchetta = bracket, mai adeguatezza dimostrata) | gate armato di record | mappa `:180` | spara su qualunque claim pubblico, prima o dopo R22 |
| 16 | P34: i numeri engine di questo capitolo = stage V0 verification; gerarchia stessa mai aggiudicata | dichiarazione di stage; gap OPEN | mappa `:181` | rider LIGHT-INSTANTIATION su S-PRES |

---

## 3. Gli APERTI

1. **12 NEVER + 2 SINGLE-AUTHOR** con finestre per-riga (mappa
   `:296-309`): C25 (F2, con C-C/C-D), C38 (F2), C51 (rung-3a), C52/C53
   (contratto F2), C54 (prossimo tocco M0 D2.4 — flippa DECIDED con una
   riga), C55 (prima istanziazione multi-punto), C57/C60 (cluster engine
   F2-entry), C59 (trigger = regime weakened-pin), C61 (N2/F4b), C62
   (cluster numerica F2), C17/C18 (derivazioni F2).
2. **P0 S-CERT residuo**: staleness import-closure, owner F2 (PROGRESS
   `:211`). Finché non è chiuso, il verdetto NON-CERTIFICABILE resta il
   verdetto di record.
3. **[OBJ-DOM-IMPL]**: obiettivo fix-A da implementare; trigger di
   record al primo verdetto F2 che consuma dJ/dthB (mappa `:172`).
4. **F11d (2 gambe)** mai eseguito → la consistenza discreto-continuo
   dell'adjoint è aggiudicata-con-falsificatore, non misurata (ledger
   C11/C56; owner F2-C11-ESTIMATOR-CAMPAIGN).
5. **Superficie A intera** ([P-IPADJ], A/B con Uno, NAND vs SAND,
   ri-censimento C58 vs landscape 2026, SDP-CAND-8): finestra engine
   F2-entry (mappa `:199-206`).
6. **Gerarchia P34** mai aggiudicata; nessun numero oltre lo stage V0
   (mappa `:181`).
7. **Derivazione NTF della costante viva** (la forma è derivata, il
   valore 100 è istanza valida ma la derivazione della costante è duty
   F2-live; C18 SINGLE-AUTHOR, ledger `:344-353`).
8. **Hessiana esatta jax.hessian bloccata** dalle regole implicite
   first-order (custom_vjp) — leva di scala nominata, non schedulata
   (memoria `s18-brick2-closed:52-56`; classe [INF] da memoria, da
   ri-verificare a F2).
9. **Julia/Enzyme non benchmarkato** su questo host (G0 §4 `:199-201`).

---

## 4. Domande da panel (col registro alla mano)

**(1) "Perché TR-Newton e non un quasi-Newton o un IP solver
commerciale? E perché dovrei fidarmi della vostra implementazione?"**
Risposta dal record, in due metà. *Perché TR-Newton segmentato*: non per
preferenza — su questo problema i flip della wall-search terminano i
segmenti dopo un passo, quindi la curvatura accumulata alla BFGS non fa
in tempo a formarsi; la curvatura va MISURATA (Hessiana piena per
segmento da n+1 differenze del gradiente adjoint esatto), attivazione
decisa su numeri (memoria `s18-brick2-closed:32-40`). E il carry
quasi-Newton non è morto: è un challenger pinnato ([P-QNCARRY], con
[P-HESSREJ]) che entra UNCONDITIONAL a F2-entry (mappa `:142`, C32) —
la scelta attuale è su numeri di QUESTO problema, non un dogma. [W2-R3]
*E l'IP
commerciale non è escluso*: l'engine di record È scipy trust-constr
interior-point (in uso da S22) sotto disciplina information-only dei
moltiplicatori; IPOPT/filter-SQP/SLQP/Uno sono pesati nel ledger, Uno è
il flip-candidate con A/B pinnato a constraint-set identico e la sua
spec (10 input) già consumata nel contratto [P-IPADJ] (ledger C31
`:481-493`). *Perché fidarsi*: perché ogni pezzo ha un rigettatore —
oracolo cross-code 91/91 in banda DERIVATA, KKT contro soglia DERIVATA
(7.745e-02 ≤ 1.156e-01), controlli negativi che falliscono quando
devono (G0 `:33-38, :94-104`), e doppio codice con GENO trattato come
riferimento indipendente MA mai assunto bug-free (memoria
`moc-critical-independent-invariants`: accordo cross-code ≠ verità). E
la contro-onestà: l'audit ostile S-CERT ha comunque bocciato la catena a
HEAD (vedi Q2) — la fiducia che chiediamo è nei rejector, non in noi.

**(2) "Cos'è esattamente un vostro certificato e cosa NON certifica?"**
Un certificato è: soglia DERIVATA (es. NTF = η·κ_q, blocco M0:3649-3766,
THEOREM*/SCHEMA — non un 0.01 di comodo) + oracolo che può RIGETTARE
(R5, `CLAUDE.md`), e la prova che le soglie sono load-bearing è
sperimentale: dimezza NTF e il verdetto flippa (PROGRESS `:155-160`).
Cosa NON certifica, dal record: (a) ottimalità GLOBALE — certifica
stazionarietà KKT locale con trasversalità, il tier di esplorazione
globale è C57 = NEVER (mappa `:138`); (b) adeguatezza del MODELLO — la
forchetta R22F è un bracket con provenance, mai adeguatezza dimostrata,
e ogni claim pubblico in merito è gated D-44 (mappa `:170, :180`);
(c) identità della root: blind spot wrong-branch finché C20 Tier-0 non
atterra (nota C56 `:769`); (d) la qualificazione del certificato stesso
è oggi un one-extra-step ratio NON qualificato — l'architettura a tier
è aggiudicata ma è duty F2 (C20 `:365-376`); (e) la scala scalare lascia
~3 decadi di laxity per-componente, dichiarate e Richardson-dominate
(C19 `:355-363`). Diciamo tutto questo noi prima che lo chieda il panel.

**(3) "12 scelte NEVER-adjudicated: come presentate una macchina con 12
scelte mai pesate?"**
Come le presenta il record: enumerate, non nascoste. NEVER significa
"mai pesata contro alternative", e la mappa dà a OGNI riga owner e
finestra di trigger (mappa `:296-309`); due sono strutturalmente vuote
finché il trigger non esiste (C55: un solo punto P_amb di default → la
domanda di aggiudicazione è vuota, `:66`; C59: dentro il pin dell'onda
periodica il cycle-average è conseguenza teorematica, non scelta,
`:78`). La regola di fase di record: nessuna fase apre con NEVER sui
componenti che consuma (PROGRESS `:213`, scope R35(a)) — il cluster
engine si chiude alla finestra F2-entry PRIMA che l'engine agisca da
F2. E il fatto stesso che il numero "12" esista con questa precisione è
il punto: viene da un ledger tipizzato con comando misurato, non da
un'autovalutazione (mappa `:33-36`). La domanda onesta non è "perché 12
NEVER" ma "perché 48 sono aggiudicate a convergenza" — e la risposta è
S-FOUNDATIONS C2-C4: 3 wave di aggiudicazione con refuter, 0 break
(PROGRESS `:213`); le 2 SINGLE-AUTHOR (C17/C18) restano dichiarate con
duty F2 — il ledger dice esplicitamente "no derivation or panel
adjudication of N_NEWTON found" (C17 `:342`) e "derivation itself still
NEVER done" (C18 `:353`) — anche quel numero è tipizzato. [W2-R2]

**(4) "L'adjoint discreto è consistente col continuo? Come lo sapete?"**
Risposta onesta: **non lo assumiamo — lo abbiamo trasformato in un
falsificatore pinnato, non ancora eseguito.** Ciò che è provato: il
gradiente discreto è esatto per la J discreta a precisione macchina
(52/52 in tolleranza derivata, G0 `:33-38`) — questo è un fatto, ma non
è la dual-consistency. La consistenza col continuo è di classe SCHEMA
(P2 Lemma B par.4.5 via nota C56) e la sua esecuzione è F11d, due gambe:
oracolo Giles-Pierce quasi-1D per il peso, residui di compatibilità
ACE/Lozano-Ponsin ai band sites (ledger C11 `:279`). Il record cita
anche la ragione pubblicata per cui NON si può condonare il check:
Hicken-Zingg p.164 — la consistenza primale non implica quella duale
(nota C56 `:769`). Se una gamba spara: la promozione F11a si blocca e
la riga C56 si riapre — è pre-registrato. OPEN dichiarato: si risponde
"aggiudicato con falsificatore armato, misura in F2".

**(5) "Il vostro oracolo cross-code usa GENO: e se GENO fosse
sbagliato?"** (attesa dal red-team)
Direttiva standing di record: MAI assumere GENO bug-free; l'accordo
cross-code non è verità (memoria `moc-critical-independent-invariants`).
Per questo gli oracoli decisivi sono invarianti INDIPENDENTI dal twin:
identità dot-product O3.1 a livello macchina (G0 `:40-43`), bande di
troncamento derivate dall'ordine dello schema (non dai valori GENO),
controlli negativi che rompono l'accordo quando iniettiamo errori (G0
`:100-104`). GENO aggiunge un asse, non fonda la verità. Residuo
dichiarato: l'audit GENO parallelo è INCOMPLETO (memoria
`s-genoaudit-parallel-incomplete`; nessun owner di record per il
completamento — R13 in PROGRESS `:191` copre solo md5-freeze/N-74/knob,
trigger = prossima sessione GENO/s3). E le due metà sostanziali
dell'audit parziale vanno dette entrambe: ha PROVATO esatti vs Zucrow i
processi unitari gemellati (interior/axis/inverse-wall, Sauer
book-exact, BC di parete dimostrata) E ha mostrato che l'accordo tra i
due backend GENO (Ch.16 ≡ Ch.17) è VACUO sull'asse rotazionale
(chiusura a un parametro, h0/s0 globali; ramo cross-stream mai
esercitato) — un motivo in più per cui i nostri oracoli decisivi sono
GENO-indipendenti. [W2-R4]

**(6) "0.449 s, 14.9 s: su quale hardware? Numeri replicabili?"**
Caveat host DI RECORD sin da G0: i tempi assoluti sono host-dependent e
non costituiscono record timing; le quantità decisionali sono rapporti
host-invarianti (overhead adjoint ~1.5%, ratio grad/solve 1.593 ≤ 4)
(G0 `:55-59`). [W2-R5] I MET di
S25-bis sono su baseline clean-host [X-SPDB] con criterio
pessimistic-end pre-registrato, e la varianza di misura è essa stessa
una riga di registro (speed-measurement-variance, PROGRESS `:149-150`).
Stage P34: V0 verification, dichiarato su slide.

---

## 5. Cosa deve dire il deck

1. **Una slide-grafo, non un organigramma**: 8 stadi, 62+17 nodi, 45
   archi, 4 superfici cluster, con lo status per-nodo codificato a
   colore E il tally detto ad alta voce: 12/36/12/2 — "vi mostriamo
   anche le scelte non ancora pesate, ognuna col suo trigger". Classe:
   [REP] (mappa `:262-309`).
2. **"Nessun numero senza rigettatore"** come tesi identitaria: soglie
   derivate (NTF = η·κ_q, THEOREM*/SCHEMA) + la prova che mordono: NTF/2
   flippa il verdetto (PROGRESS `:155-160`). Un certificato che non può
   bocciare non è un certificato. Classe: THEOREM* + [REP].
3. **La storia dell'adjoint in 3 battute**: Hoffman 1967 (campi di
   moltiplicatori per ugelli reagenti, lit registry `:372-378`) → oggi
   si differenzia il problema discreto che si risolve davvero (52/52,
   overhead ~1.5%, G0 §2) → una soluzione in più = gradiente su tutti i
   DOF. Con l'aperto dichiarato: dual-consistency = SCHEMA + F11d armato.
   Classe: [REP] + SCHEMA dichiarata.
4. **I numeri engine con lo stage stampato**: KKT 7.7e-02 ≤ soglia
   derivata, oracolo 91/91, val_grad 0.449 s, segmento 14.9-20.1 s (MET
   pre-registrato) — ogni cifra etichettata "stage V0: verification"
   (rider P34). Classe: [REP] + dichiarazione di stage obbligatoria.
5. **La slide di onestà che nessuno si aspetta**: "abbiamo commissionato
   un audit ostile alla nostra catena di certificazione: verdetto
   NON-CERTIFICABILE, 2 P0; uno riparato in finestra, uno con owner F2"
   (PROGRESS `:211`). Messaggio: il sistema di controllo funziona
   perché boccia NOI; i difetti sono migrati dall'oggetto al
   certificatore. Classe: [REP] (verdetto d'audit).
6. **Cosa NON diciamo**: nessun claim pubblico di adeguatezza (gate
   D-44 armato, mappa `:180`); nessuna ottimalità globale (C57 NEVER);
   nessun numero sperimentale. I confini detti prima delle domande.
   Classe: gate di record.

---

## Disposizione riparazioni (onda 2)

[Refuter: REFUTE_CH4.md, verdetto REGGE-CON-RIPARAZIONI, 0 BREAK /
5 REPAIR / 3 GAP / 4 NOTE. Ogni fix applicato con read-then-quote:
ancora del refuter aperta e verificata prima dell'edit.]

| finding # | classe | disposizione |
|---|---|---|
| 1 | REPAIR | APPLICATO [W2-R1] — §1.4 gate di produzione riallineato alla misura S18 (t_GENO 0.299 s, soglia 1.197 s; G0 `:148`, `:167-169` verificate) |
| 2 | REPAIR | APPLICATO [W2-R2] — Q3: "50 pesate" → "48 aggiudicate + 2 SINGLE-AUTHOR dichiarate"; "0 righe cassate" → "0 break"; ledger C17 `:342` e C18 `:353` verificati verbatim |
| 3 | REPAIR | APPLICATO [W2-R3] — Q1: challenger [P-QNCARRY]+[P-HESSREJ] unconditional a F2-entry aggiunto (mappa `:142` verificata) |
| 4 | REPAIR | APPLICATO [W2-R4] — Q5: "con owner" rimosso (memoria genoaudit senza owner di record; R13 PROGRESS `:191` = solo md5/N-74/knob, verificata); entrambe le metà dell'audit parziale citate (positivo unit-process + vacuità Ch.16≡Ch.17) |
| 5 | REPAIR | APPLICATO [W2-R5] — Q6: etichette corrette (overhead adjoint ~1.5%; ratio grad/solve 1.593 ≤ 4; G0 `:53-58` verificate) |
| 6 | GAP | APPLICATO [W2-R6] — scope X-GENOXC (G0 `:202-210` verificata) aggiunto in §1.3(a) e nella riga claim 3 |
| 7 | GAP | APPLICATO [W2-R7] — J* con cross-ref esplicito alla definizione di record (`CH1_formulation_ladder.md:56`, verificata) in §1.4 e claim 6 |
| 8 | GAP | APPLICATO [W2-R8] — definizione di GENO alla prima occorrenza (§1.3(a)) |
| 9 | NOTE | APPLICATO [W2-R9] — log committato `validation/PROGRESS_2026-08-06_S18_brick2run.md` (esistenza verificata su disco) = ancora primaria dei claim 5-6, memoria = indice |
| 10 | NOTE | APPLICATO [W2-R10] — ordinali FORK-141 esplicitati (H20 = 1 of 2, P34 = 2 of 2; mappa PM-6 `:332` verificata) |
| 11 | NOTE | APPLICATO [W2-R11] — attribuzione "a weight cannot referee itself" spostata su nota C11 `:279` / supplemento §4.2 (verbatim verificato in C11 `:279`) |
| 12 | NOTE | NON-APPLICATO — il fix proposto ("avete mai pubblicato un numero poi risultato falso?" → G0 `:177-198`, LEDGER TRUTH REPAIR) è indirizzato alla banca Q&A (artefatto a valle dell'arco di consumo), non a questo capitolo; registrato qui perché lo storyboard/banca lo consumino |
