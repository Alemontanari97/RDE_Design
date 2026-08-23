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

[W-B.1 estensione B4, 2026-08-23 (emendamento v2.1, nodo N-I): aggiunti il
puntatore Annex B in §1.2, la riga suite 23/23 in §1.4, §1.6 "La velocità
come scelta algoritmica" (riga I-v: ADJUDICATO estensione, non capitolo
nuovo — design v2 §M :349), §3-bis ANTENATI, §7 (celle I-ii/I-iii),
§7-bis DECISION CARD (owner riga I) e il blocco DECK FEED. La numerazione
salta §6 (STORIA, owner W-B.2 — non toccata). Ogni ancora nuova è stata
riaperta e verificata in finestra (read-then-quote).]

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

**Puntatore (non duplicazione): la tassonomia degli input.** Il contratto
di ciò che ENTRA nella pipeline (lo stadio 1) ha una tassonomia di record:
**ANNEX B di D6** — "Input taxonomy for the CFD-free design tool"
(`docs/rde_nozzle_development_plan.md:1133`; citata anche da M0 `:4263`).
La sua ricostruzione critica (classi di caso, contratto Γ_d, C-1bis) vive
in **CH10** (nodo contratto, writer B2): qui SOLO il puntatore — regola
anti-duplicazione dell'atlas.

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
- **Suite di regressione: 23/23 gruppi PASS — CON incidente dichiarato**
  (riga I-v). Il run verificato di record: 23/23 gruppi di test PASS in
  234 s, EXIT 0, righe per-gruppo catturate integralmente ((i)-(xxiii),
  incluso il lint numerico (vii) post-riparazione) — commit `c9bacd9`
  (2026-08-21, verificato con `git show` in finestra). **L'incidente,
  detto per intero**: il commit di chiusura C4 (7dea386) aveva citato
  "23/23" PRIMA della sua evidenza verificata — un run intermedio aveva
  stampato 22/23 con le righe per-gruppo perse per un errore di cattura
  (tail-4) dell'orchestratore; classe R5, colto dal ri-conteggio
  dell'orchestratore stesso e annotato nel log di sessione. Il claim
  sta TRUE con il run di c9bacd9 come carrier — e l'incidente resta
  dichiarato, non cancellato: è un esempio della disciplina SR-12
  (nessun conteggio ereditato, solo comandi misurati in finestra).
  Classe: [REP] (carrier = commit c9bacd9 + log annotato).
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

### 1.6 La velocità come scelta algoritmica (S25/S25-bis)
[Riga I-v; ADJUDICATO = estensione di questo capitolo, non capitolo
nuovo (design v2 §M `:349`).]

Il programma NON ha trattato la velocità come tuning da ingegnere: l'ha
trattata come una **scelta algoritmica sotto la stessa disciplina di
tutte le altre** — ogni leva di speed-up = gate di invarianza eseguibile
+ guadagno misurato + diff-refuter avversario (dual-proof standard,
esteso per direttiva utente in-sessione; commit `07400a4`, S25 M-CHAIN,
verbatim "every lever = executable invariance gate + measured gain +
adversarial diff-refuter").

- **La catena S25 (M-CHAIN, dispatch M0→M1→M2→M4→M3→M5a/b)**: baseline
  clean-host di record **100.84 s → 32.09 s** (3.1×) a fine S25;
  **val_grad 6.420 s → 0.979 s = 6.6×** (il "vg 6.6×" di record —
  commit `07400a4`, misura M-C; il quesito Q2/A-G RISOLTO, la
  conseguenza del falsificatore NON spara). Ogni leva accettata dal suo
  gate (m12gate/m4gate/m5gate: wall BITWISE, contatori riconciliati,
  controlli negativi che sparano). Classe: [REP], caveat host di G0
  ereditato (i rapporti sono decisionali, i secondi assoluti no).
- **I refuter hanno trovato 2 difetti veri — riparati a registro**
  (commit `07400a4`): (1) memo key cieca ai knob di classe → `_mkey`
  legge M_NODES/KNOT_XI/N_NEWTON a request time; (2) engine-cache key
  senza la design class (HIGH) → class nella ekey + CLASS-KEY REJECTOR
  aggiunto a m4gate. Il processo di velocizzazione è stato esso stesso
  refutato, non solo misurato.
- **Lo STOP-CHECK onesto** (fine S25): segmento ~46 s vs ≤ 30 = NOT-MET
  senza M5c (controfattuale tenuto) → M5c+M6 = S25-bis VINCOLANTE, non
  opzionale (commit `07400a4`). Nessun "quasi-MET" dichiarato MET.
- **S25-bis, contatore finale FORMALE (criterio pessimistic-end
  PRE-REGISTRATO)**: catena 100.84 → 32.09 → **record 5.58 s**; replay
  0.236 s; val_grad 0.449 s; Hessiana 4.5-7.0 s (≤ 8); SEGMENTO = MET
  (14.9 s [M-D] / 20.1 s [M-E] vs ≤ 30), CAMPAGNA = MET (~10-14 min
  pessimistic vs ≤ 25) (`docs/rde_nozzle_PROGRESS.md:119-125`; carrier
  [X-SPDB], riga R22 `:200`). **STOP-WHEN-MET onorato come raffinato
  dall'utente**: fuori solo l'overengineering (H2/H5/O1-O4/N8 =
  conditional nominate con trigger), dentro le migliorie reali — M6
  tentato col suo gate, e il gate ha RIGETTATO: il rigetto È il
  verdetto (PROGRESS `:126-129`). Classe: [REP].
- **La coda meccanica è essa stessa tipizzata**: chiusura C4 del canale
  velocità = tier **ONDEMAND tipizzato su tutti i 46 carrier** +
  **STALENESS LINK** nel claims-lint (pass date ≤ ultimo commit che
  tocca il carrier; rejector "stale pass date" seminato e provato a
  ogni run — e SPARATO per davvero in-sessione su un carrier non
  committato) (commit `32459ca`; riga R3c, PROGRESS `:181`). Anche la
  contabilità della velocità ha un rigettatore. Classe: [REP].

Perché questa sezione sta nel capitolo "scelte": la velocità DECIDE
scelte di record — il gate di produzione T2a e la flip clause di
linguaggio C58 sono definiti in secondi misurati (G0 §4, §1.3(a));
la review S25 di G0/T2 (riga R7c, PROGRESS `:185`) è il precedente per
cui un numero di velocità può riaprire una scelta di stack. La velocità
è un input del choice ledger, non un vanto da slide.

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
| 17 | Suite 23/23 gruppi PASS (234 s, EXIT 0) CON incidente dichiarato: 7dea386 citò 23/23 PRIMA dell'evidenza (run 22/23, cattura tail-4 persa; classe R5, auto-colto) | [REP] (carrier = run c9bacd9) | commit `c9bacd9` (git show verificato in finestra) | il ri-conteggio SR-12 È il rejector che ha colto l'incidente |
| 18 | Velocità = scelta algoritmica: M-CHAIN S25 100.84→32.09 s, val_grad 6.420→0.979 s (6.6×), ogni leva gate+refuter; 2 difetti veri trovati dai refuter e riparati; STOP-CHECK onesto NOT-MET → S25-bis | [REP] | commit `07400a4`; PROGRESS `:119-129`, `:181`, `:185` | gate m12/m4/m5 con controlli negativi; STOP-CHECK controfattuale tenuto |

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

## 3-bis. ANTENATI DIRETTI (lineage, nodo N-I)

[Emendamento v2.1 §1b: righe dal `LINEAGE_LEDGER.md` (merge W-B.0);
stato delle righe = CANDIDATE finché il refuter C6 (W-C) non passa —
dichiarato, non nascosto. Join su {LL-id, componente} (contratto
[F-des-4]). Ogni claim di novità di questo nodo cita ≥1 LL-id (lint 7).]

- **LL-30 — Byrd-Hribar-Nocedal 1999 + Nocedal-Wright 2006** (comp.
  N-17): il **parent algoritmico dell'engine** — `tr_interior_point` di
  scipy discende dall'algoritmo IP large-scale di BHN (SIOPT 9:877-900);
  SR1 (§6.2) e il modello d'errore FD (§8.1) di Nocedal-Wright sono le
  fonti delle costanti DERIVATE del programma (C44, [P-HESSREJ]).
  Cosa gli manca vs noi: nessuna disciplina di certificato sui numeri
  prodotti, nessun contratto information-only sui moltiplicatori.
- **LL-15 — Uno (Vanaret-Leyffer 2026)** (N-17): il flip candidate
  arm-B della card C31 (§7-bis) — solver unificato SQP/IP a preset;
  guardia identical-certified-outcomes + decisione O5-class d'install.
  Antenato "in avanti": è il ri-esame programmato, non un precedente.
- **LL-31 — linea direct-search del campo ugelli (Kraiko-2016 GA,
  Fernandes, Valeriani, Ornano)** (N-17): engine senza condizioni di
  ottimalità; **i loro stessi dati sono evidenza PRO il driver
  certificato** (Kraiko 2016: il metodo esatto batte i GA — LL-29).
- **LL-7 — Hoffman 1967** (comp. 4/10/11/12): campi di moltiplicatori
  su caratteristiche per flusso reagente — l'antenato di dominio
  dell'adjoint di §1.3(b); il suo E-residual Eq. (78) è consumato come
  certificato VI.3. Cosa gli manca: AD discreto, i tre ruoli, F11d.
- **LL-12 — Giles-Ulbrich 2010** (comp. 11): il **teorema negativo**
  (adjoint discreto su shock catturati) = antenato diretto
  dell'AGGIUDICAZIONE C49 (fitted-front unico portatore di certificato,
  §1.3(c)): la scelta di record discende da un limite pubblicato, non
  da una preferenza (scope dichiarato 1-D scalare nella nota C49).
- **LL-32 — Johnson-Boney 1975 + Scofield-Hoffman 1971** (N-18):
  precedenti tabulated-EOS/real-gas MoC del [DIR-THERMOTAB] — la
  tabulazione termodinamica nel MoC non è nostra invenzione; nostra è
  l'interfaccia-contratto differenziabile C1 con oracolo (C24).
- **LL-33 — Browne-Shepherd SDT** (N-18): il lato GENERATORE (CJ/ZND,
  Cantera-class); la giunzione formale generatore→interfaccia-tabelle
  **non è formalizzata dal campo** — il contratto S11 la occupa
  (claim di lineage, non NOT-FOUND: la riga LL-33 lo dice).

Contro-lettura onesta: nessuna di queste righe è un NOT-FOUND — il nodo
N-I NON rivendica novità dell'engine in sé; la novità rivendicata è la
CATENA (design-adjoint certificata per-fase dentro il campo RDE-nozzle),
ed è query-bounded in §7(b) via CH5.

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
(G0 `:53-58`; 1.593 a `:168`) [W2-R5][W2b-F1]. I MET di
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

## 6. STORIA — trittico condizionale [V2-R2] (writer B8a, W-B.2, 2026-08-23)

Ogni battuta: DATA + PROCESSO + VERDETTO (vincolo §5-bis). Nota di ramo:
per le scelte-macchina la battuta 2 è spesso (b) STANCE-DI-FORK — il
verdetto per-riga di Fase B (`validation/sfoundations_raws_2026-08-13/
phaseB_tree_diff.md`, 2026-08-17) è una presa di posizione a livello di
FORK, NON una riderivazione dell'implementazione. Le 12 righe SILENT del
ledger (C2 cond., C5, C15, C16, C22, C23, C30, C40, C45, C46, C47, C48)
sono ramo (c) per definizione (sotto la granularità degli alberi ciechi).

**T-1. C58 — stack differenziabile JAX (DIR-G0).**
- *Battuta 1*: 2026-07-20, sessione S10 — commit `cc878ef` "G0 DECIDED —
  GENO built (WSL gfortran), tocnoz contour reproduced to 1e-10,
  cross-code unit-process oracle X-GENOXC PASS; JAX primary stack"
  (dossier `docs/rde_nozzle_G0_decision.md`; spike JAX già 2026-07-16,
  `b54e571`). PROCESSO: gate G1-class con oracolo cross-code e controlli
  negativi. VERDETTO: G0 DECIDED, JAX primario.
- *Battuta 2*: (c) **NON-RIDERIVATO: questo aspetto non ha avuto
  riderivazione agnostica di record** (C58 > C48: fuori dal perimetro
  per-riga del diff Fase B). Doppia prova alternativa: flip clause
  quantificata ARMATA e misurata (T1 1.593 ≤ 4; T2a 0.116 ≤ 1.197 s, G0
  §4 note datate) + review S25 di G0/T2 (2026-08-12: il firing T2 di S18
  era costo strutturale, non throughput di linguaggio — la decisione STA;
  memoria `s25-engine-speed`). PROCESSO: re-esame a numeri con clausola
  di ribaltamento. VERDETTO: MIXED, ri-censimento al cluster engine
  F2-entry.
- *Battuta 3 — convergenza* [fix ST-C5-09]: DATA: 2026-08-12 (review S25
  di G0/T2 — ultima ri-convergenza della scelta a numeri). PROCESSO:
  re-esame gate-based con flip clause tenuta armata. VERDETTO: classe
  finale [REP]; caveat permanente dichiarato: Julia/Enzyme mai
  benchmarkato su questo host (G0 §4 :199-201).

**T-2. C31 — driver TR-Newton segmentato a curvatura misurata (+ run di
record S18).**
- *Battuta 1*: 2026-08-06, sessioni S17-S18 (brick 2) — driver attivato
  SU NUMERI (segmenti single-step → Hessiana piena misurata); run
  end-to-end di record: KKT 7.745e-02 ≤ 1.156e-01, oracolo 91/91,
  J* = 2.7761688e+07 (carrier
  `validation/PROGRESS_2026-08-06_S18_brick2run.md`; R4 back-propagato
  commit `01c41a6`; A1 BRICK 2 OF RECORD M0:3251-3253). PROCESSO: brick
  gated con 4 tentativi dichiarati e oracoli. VERDETTO: PASS di record.
- *Battuta 2*: (b) **STANCE-DI-FORK** — verdetto Fase B per-riga C31:
  "CONVERGENT on family + DIVERGENT (IP half)"
  (`phaseB_tree_diff.md:159`, 2026-08-17): presa di posizione a livello
  fork (famiglia TR-Newton convergente, metà interior-point sfidata),
  NON riderivazione dell'implementazione del driver. PROCESSO: diff
  alberi ciechi vs ledger. VERDETTO: MIXED con [P-IPADJ] = prima azione
  engine F2 sul critical path di C28.
- *Battuta 3*: audit aggiuntivo del run: S24 T2a five-line hypothesis
  audit sul twin S18 (2026-08-12, M0:4138-4140). Classe finale [REP];
  engine falsifiers one/two/three vivi (VERDICT_wave2 par.1.1).

**T-3. C24 — thermo a tabelle (backend-1).**
- *Battuta 1*: 2026-07-21, sessione S11 — direttiva utente
  [DIR-THERMOTAB] "tables = interface contract" (M0:3237; memoria
  `thermo-tabulated-backend`, S11); carrier [X-THC1] tabelle quintic C1
  eseguito al kickoff brick-2, S17, 2026-08-06 (memoria
  `s17-brick2-kickoff`). PROCESSO: direttiva utente + carrier con
  condizione C-A scaricata. VERDETTO: DECIDED.
- *Battuta 2*: (b) **STANCE-DI-FORK** — verdetto Fase B per-riga C24:
  "CONVERGENT + ENRICHING: V-F9 lands" (`phaseB_tree_diff.md:117-118`,
  2026-08-17), rafforzato dall'item theory-layer 6 "Thermo road:
  V-F9/H-F6 = certified gamma(T) tables with AD" (`:345`) — qui il fork
  E la sostanza convergono, ma resta stance di fork sull'implementazione
  (dCp-ingest gated C-B; C25/C26 righe separate, C25 NEVER). PROCESSO:
  diff alberi. VERDETTO: CONVERGENT-ENRICHING.
- *Battuta 3 — convergenza* [fix ST-C5-09]: DATA: 2026-08-21 (pipeline
  decision map, stage 3, righe C24-C26 `:90-92`). PROCESSO: consolidamento
  nella mappa CITE-ONLY refereed (0 BREAK). VERDETTO: classe finale
  [REP]; C25 (table box) NEVER con finestra F2.

**T-4. C49 — fitted-front marching come unico portatore di certificato.**
- *Battuta 1*: pratica fitted dal G0 (2026-07-20, `cc878ef`: X-GENOXC su
  processi unitari con punto d'urto fittato); come RIGA aggiudicata del
  ledger: onda wave-2 blocco3, 2026-08-19
  (`blocco3/VERDICT_wave2.md`; ledger C49
  `docs/choice_ledger.yaml:682-692`), in risposta alla domanda utente
  "perché si fitta una soluzione che potrebbe essere catturata".
  PROCESSO: aggiudicazione a convergenza con refuter (ZERO finding sulla
  riga). VERDETTO: fitted = certificatore; captured = explorer nominato
  build-gated.
- *Battuta 2* [fix ST-C5-08]: (c) **NON-RIDERIVATO: questo aspetto non ha
  avuto riderivazione agnostica di record** — C49 > C48, NESSUN verdetto
  per-riga di Fase B esiste (il diff §1 copre C1-C48; unico tocco
  adiacente: candidatura "C49-class" a `phaseB_tree_diff.md:233`).
  Doppia prova alternativa: aggiudicazione wave-2 blocco3 a ZERO finding
  refuter (2026-08-19, `blocco3/VERDICT_wave2.md`; ledger C49
  `docs/choice_ledger.yaml:682-692`) + la classe S1 certificata su cui il
  fitted poggia, riderivata 4/4 dagli alberi (item 3,
  `phaseB_tree_diff.md:330`). PROCESSO: wave blocco3 + diff alberi
  sull'oggetto di classe. VERDETTO: [REP]; etichetta di ramo onesta —
  l'implementazione del march NON è coperta dagli alberi ciechi.
- *Battuta 3 — convergenza* [fix ST-C5-09]: DATA: 2026-08-19 (verdetto
  wave-2, riga C49 chiusa a zero finding). PROCESSO: aggiudicazione a
  convergenza con upgrade path pinnato. VERDETTO: upgrade path HOIST/Zahr
  nominato con entry gate; frontiera fit-vs-capture governata dal budget
  DWR (campagna C11 leg (b), F2).

**T-5. C18 — NTF: da costante magica a forma derivata.**
- *Battuta 1*: NEWTON_TOL_FACTOR = 100 come costante engine del brick 2
  (S17/S18, 2026-08-06); GAP-29 sweep S25-bis (2026-08-12/13): soglia
  MISURATA load-bearing (NTF/2 flippa il verdetto di certificazione).
  PROCESSO: sweep pre-registrato. VERDETTO: load-bearing, non cosmetica.
- *Battuta 2*: (a) RIDERIVATO-PIENO in Fase D — minore (a) NTF:
  derivazione `phaseD/phaseD_minor_ntf.md`, refutazione one-round
  completa `refute_minor_ntf.md` + escalation a forma piena r1/r2 DRY
  (`esc_refute_ntf_r1.md`, `esc_refute_ntf_r2.md` + probe
  `esc_probe_ntf_*.py`, finestra C4 2026-08-20/21; "4 minori ESCALATI a
  forma piena e TUTTI DRY", PROGRESS ORA :17-18). PROCESSO: derivazione
  formale + escalation refuter. VERDETTO: NTF = η·κ_q, istanza valida.
- *Battuta 3*: landing M0 [LAND-C4-LA2] (M0:3649-3766, 2026-08-21):
  NTF-2/3 THEOREM*, NTF-1/4 SCHEMA, NTF-5 PRACTICE, falsificatori
  NTF-1..4; la riga ledger resta SINGLE-AUTHOR con duty F2-live sulla
  derivazione della costante.

**T-6. La velocità come scelta algoritmica (S25/S25-bis).**
- *Battuta 1*: 2026-08-12, sessione S25 — M-CHAIN (commit `07400a4`,
  verbatim "every lever = executable invariance gate + measured gain +
  adversarial diff-refuter"): 100.84 → 32.09 s, val_grad 6.6×;
  STOP-CHECK onesto NOT-MET → S25-bis vincolante; S25-bis (2026-08-12/13)
  = record 5.58 s, SEGMENTO e CAMPAGNA MET al criterio pessimistic-end
  PRE-REGISTRATO (PROGRESS :119-129). PROCESSO: catena gated con
  controlli negativi. VERDETTO: MET formale.
- *Battuta 2*: (c) NON-RIDERIVATO in Fase A (fuori perimetro alberi);
  doppia prova alternativa: diff-refuter avversario a convergenza sulla
  catena (2 difetti VERI trovati e riparati a registro: memo key cieca,
  engine-cache senza design class — commit `07400a4`) + diff convergiuto
  di chiusura 21/4/0/0
  (`validation/ADVISORY_S25bis_diff_convergence_2026-08-12.md`; memoria
  `s25bis-speed-complete`). PROCESSO: refutazione del processo di
  velocizzazione stesso. VERDETTO: [REP] con caveat host.
- *Battuta 3 — convergenza* [fix ST-C5-07]: DATA: **2026-08-12** (commit
  `32459ca`, chiusura "C4"-di-S25 — etichetta INTERNA del canale velocità
  S25, `[F-SERVICE/S25][PIANO/R3c] C4 MECHANICAL CLOSURE`; da NON
  confondere con la finestra S-FOUNDATIONS-C4 del 2026-08-20/21 —
  namespace C4: v. REFUTE_STORIE §FP). PROCESSO: chiusura meccanica del
  canale velocità con tier ONDEMAND tipizzato sui 46 carrier + STALENESS
  LINK nel claims-lint, rejector provato e SPARATO in-sessione.
  VERDETTO: classe finale [REP].

**T-7. La mappa delle decisioni (pipeline a 8 stadi).**
- *Battuta 1*: 2026-08-21, chiusura S-FOUNDATIONS-C4 — mappa di record
  `docs/rde_nozzle_pipeline_decision_map.md` (CITE-ONLY; 8 stadi, 79
  nodi, 45 voci-arco, tally 12/36/12/2 misurato SR-12 :262-295).
  PROCESSO: compilazione cite-only con comandi misurati. VERDETTO: 100%
  archi verificati.
- *Battuta 2*: (c) NON-RIDERIVATO (artefatto di navigazione, non
  enunciato); doppia prova alternativa: passaggio refuter dedicato = 0
  BREAK / 0 REPAIR / 5 AMENDMENT / 4 NOTE (mappa :317-339; "refuter 0
  BREAK/0 REPAIR, amendment applicati", PROGRESS ORA :35-37, 2026-08-21).
  PROCESSO: refutazione della mappa. VERDETTO: retta.
- *Battuta 3 — convergenza* [fix ST-C5-09]: DATA: 2026-08-21 (chiusura
  C4, mappa di record). PROCESSO: regola CITE-ONLY con passaggio refuter
  consumato. VERDETTO: doppio consumer dichiarato (F2 + S-PRES); i
  conflitti si risolvono CONTRO la mappa (regola :7-14).

**T-8. S-CERT e la disciplina dell'onestà (incidente 23/23 incluso).**
- *Battuta 1*: 2026-08-13, sessione S-CERT (R33, prompt
  `validation/ADVISORY_Scert_prompt_2026-08-12.md`) — audit OSTILE
  context-free della catena di certificazione: verdetto vincolante
  NON-CERTIFICABILE, 2 P0 a HEAD ((vii) riparato in-window; staleness
  import-closure → owner F2); difetti MIGRATI dall'oggetto al
  certificatore; MC8 regge 8/8 (memoria
  `fservice-scert-double-session`; PROGRESS :211 riga R33). PROCESSO:
  audit avversario per design. VERDETTO: NON-CERTIFICABILE dichiarato.
- *Battuta 2*: (c) NON-RIDERIVATO (è esso stesso una seconda prova
  ostile del certificatore); istanza gemella della disciplina: incidente
  suite 23/23 — il commit di chiusura C4 `7dea386` (2026-08-21) citò
  "23/23" PRIMA dell'evidenza verificata (run intermedio 22/23, cattura
  tail-4 persa); colto dal ri-conteggio SR-12 dell'orchestratore e
  sanato dal run di record commit `c9bacd9` (2026-08-21, git show
  verificato in finestra §1.4). PROCESSO: rejector di conteggio SR-12.
  VERDETTO: claim TRUE sul carrier giusto, incidente DICHIARATO mai
  cancellato.
- *Battuta 3 — convergenza* [fix ST-C5-09]: DATA: 2026-08-13 (verdetto
  S-CERT, R33) e 2026-08-21 (sanatoria incidente 23/23 col run `c9bacd9`).
  PROCESSO: audit ostile context-free + rejector di conteggio SR-12.
  VERDETTO: classe finale [REP] (verdetti d'audit); la storia operativa
  del programma include i propri incidenti come istanze della disciplina,
  non come eccezioni.

---

## 7. Posizionamento / conformity del nodo N-I (celle I-ii / I-iii)

[La numerazione salta §6: STORIA, owner W-B.2. Tre metà fisse per
template §T-§7; id registry VERBATIM, tutti confermati con grep in
finestra su `docs/literature_registry.yaml`.]

### 7(a) STRUMENTI — la terna mondo-SOTA / cosa usiamo / perché (cella I-ii)

- **Driver: TR-Newton segmentato vs SQP/IP.** Mondo-SOTA: interior
  point large-scale — `byrd_hribar_nocedal_1999` (SIOPT 9:877-900,
  READ-PARTIAL pp.877/879/884: barrier law p.879, moltiplicatori
  least-squares Eq. (3.15)) è il **parent algoritmico** di scipy
  trust-constr (LL-30); `nocedal_wright_2006_2ed` (§6.2 SR1, §8.1
  modello d'errore FD pp.194-197 [FULL] — la fonte delle bande DERIVATE
  di [P-HESSREJ]/[P-QNCARRY]); filter-SQP/SLQP pesati nel ledger C31;
  `vanaret_leyffer_2026_uno` (Uno, MPC 2026, pubbl. 10-06-2026) +
  `vanaret_montoison_2026_joss` (JOSS 2026, paper software DISTINTO) =
  il solver unificato flip-candidate. Cosa usiamo: trust-constr IP +
  driver TR-Newton segmentato a curvatura misurata. Perché: i flip
  della wall-search rendono i segmenti single-step (curvatura BFGS non
  si forma → si misura), attivazione su numeri (§1.3(d)).
- **Rumore e passo certificabile.** Mondo-SOTA rumore:
  `sun_nocedal_2023_noisy_tr` (TR per funzioni rumorose; status
  registry UNREAD DICHIARATO — consumo deliberato al trigger
  [P-TRFLOOR], owner C34: non lo citiamo oltre l'identità). Passo
  certificabile: `deuflhard_2011_csm35` (affine invariance, monitor
  Θ pp.51-53, NLEQ-ERR pp.147-148 verificato verbatim) +
  `yamamoto_1986_numermath48` (bound Kantorovich two-sided Gragg-Tapia
  Thm 2; identity flag vol. 48-vs-49 DICHIARATO nel registry, non
  aggiudicato) = la linea C20 Tier-1/Tier-2 (§1.3(g)). Perché: la
  qualificazione del certificato deve poggiare su bound pubblicati,
  non su ratio di comodo.
- **Stack AD: JAX custom_vjp vs Enzyme.** La decisione G0 vive in D6
  `docs/rde_nozzle_development_plan.md:753-774` (verificata in
  finestra): JAX primario (custom_vjp + implicit rules), Julia+Enzyme
  = alternate DICHIARATO, GENO-Fortran = riferimento dual-code
  indipendente; falsificatore loop-speed tenuto (assembled loop
  impraticabile → flip a Julia+Enzyme, `:773-774`). Dettaglio evidenze
  in §1.3(a); recency in card C58 (§7-bis).
- **MoC fitted-front vs shock-tracking implicito.** Mondo-SOTA:
  `huang_zahr_2022` (HOIST, JCP 454:110981, robust high-order implicit
  shock tracking) + `wanted_thakur_nadarajah_2024` (adjoint-based
  goal-oriented tracking full-space; su disco la versione journal JCP
  523:113633, 2025 — più NUOVA dell'ask 2024, dichiarato nel registry).
  Cosa usiamo: fitted-front marching (C49). Perché: unico portatore di
  certificato nella classe S1; la linea implicita = upgrade path
  NOMINATO con entry gate sulle checklist PUBBLICATE della linea stessa
  (HZ §5.2-5.3; Thakur p.26 open issues) — il confine fit-vs-capture è
  governato dal budget DWR, non da gusto (§1.3(c), LL-12).
- **Thermo tabulata (S11) vs Cantera-in-the-loop.** Mondo-SOTA lato
  generatore: `browne_shepherd_sdtoolbox_2018` (SDT, CJ/ZND — LL-33);
  precedenti tabulated-EOS nel MoC = LL-32. Cosa usiamo: tabelle
  quintic C1 come CONTRATTO d'interfaccia (C24, [X-THC1]); Cantera
  resta il generatore di fiducia, mai nel loop differenziato. Perché:
  milioni di valutazioni differenziabili per solve; NASA-direct tenuto
  come ORACOLO (C-A scaricata). Threat 2025 censita: LL-34 (Janc,
  finite-rate differenziabile non-tabulato) = falsificatore costruibile.

### 7(b) SENSO — pipeline nostra vs framework ASO del campo (cella I-iii)

Ancora di record: **CH5 §1.1** — i quattro paper coupled RDE+nozzle del
corpus C4 (campo ISTANZIATO, guardia 4: P-A Liu-Wang 2022 PKU; P-B/P-C
Li-Xu 2023/2025 NUAA; P-D Jourdaine 2019 KIT/Aoyama) praticano CFD
pubblicata + trade study discreto o sweep: P-A "NO optimizer", P-C
nessun design nuovo, P-D "NONE — esplicitamente non ottimizzato", e la
sintesi consolidata dice verbatim **"no optimizer appears anywhere in
the four papers"** (CH5 §1.1, SYN:58-61; P-B usa il variazionale
classico ma su UN solo stato mediato globalmente). **Nessuna catena
design-adjoint** nel campo RDE-nozzle: il gap che il nodo N-I occupa è
la catena design-adjoint certificata per-fase. Lignaggio dichiarato
(lint 7): gli antenati dell'engine vivono FUORI dal campo (LL-30
Byrd-Nocedal; LL-7 Hoffman per il dominio ugelli reagenti); dentro il
campo la linea è direct-search/GA (LL-31), i cui dati sono evidenza PRO
il driver certificato (LL-29). Il confronto con i framework ASO
generalisti (adjoint shape optimization aeronautica) è il §7(a):
adottiamo i loro parent algoritmici (LL-30) e i loro criteri pubblicati
(Hicken-Zingg, HOIST) MA aggiungiamo lo strato che a loro manca nel
nostro problema: certificati con rejector per-numero (R5) + choice
ledger tipizzato + per-fase. Claim di assenza: query-bounded su DUE
fonti DISTINTE [WB1-C3-09]: (i) i gap verdicts (b2) — C1 family-averaged
contouring / C2 / C3 NOT-FOUND(q) — vivono in LM:354-362
(`docs/rde_nozzle_literature_map.md`); (ii) lo sweep avversario
1971-2026 coi 2 near-miss dichiarati (Kraiko-Tillyaeva 2015,
ISABE-2003-117) vive in `validation/ADVISORY_litmap_extension_2026-08-13.md`
(":17 … NOT found 1971-2026") — il litmap NON lo contiene. Il claim di
assenza sta sull'UNIONE delle due fonti; non lo ri-deriviamo qui
(navigation-first, riga di record in CH5).

### 7(c) STANDARD DI RIFERIMENTO (assi §C della conformity map)

Gli assi che governano il metodo di QUESTO nodo (design v2 §C, mappa
citata non duplicata): **asse 3 (tracciabilità, classe ECSS/DO-178C)**
— la catena id→nodo→verifica del choice ledger + i lint machine-checked
sono il nostro trace bidirezionale; divergenza dichiarata: nessun audit
esterno né certificazione DI standard. **Asse 5 (FAIR/provenance)** —
nessun numero engine senza script committato + test + commit di nascita
(R5; i numeri di §1.4/§1.6 ne sono le istanze). Per i confronti di
strumenti in §7(a) vale l'**asse 2 (GRADE-class)**: ogni claim porta la
classe di rigore e il read-status onesto del registry (READ-PARTIAL con
pagine, UNREAD dichiarato). Claim "SOTA" di questo capitolo senza asse
citato = violazione lint 6 — per questo ogni voce di §7(a) porta l'id
registry e lo status.

---

## 7-bis. DECISION CARD — riga I (owner B4, emendamento v2.1 §1g)

[Formato vincolante a 6 campi. Fonte delle righe: `docs/choice_ledger.yaml`
(righe riaperte e citate in §1.3). Perimetro di ownership DICHIARATO:
card qui per le scelte che QUESTO capitolo presenta — 4 aggiudicate
(C31, C58, C49, C24) + 9 "non-aggiudicata" (le righe SA/NEVER della
riga I toccate dal capitolo: C17, C18, C25, C38, C55, C57, C59, C60,
C62). I token di roster C51/C52/C53/C54/C61 in §3 sono ENUMERAZIONE
della mappa, non scelte presentate: le loro card vivono nei capitoli
proprietari (C51 → CH7 §7; C52/C53/C54 → CH10 §5; **C61 → CH6 §8, casa
PRIMARIA di record — dedup WB1-C3-17 risolto, orchestratore
2026-08-23; CH8 tiene solo il puntatore**), per la regola di ownership
§1g ("ogni altro writer compila le card delle scelte che il SUO
capitolo presenta").]

### CARD C31/engine (card di riferimento OBBLIGATORIA)

1. **Scelta**: C31 — optimizer engine (ledger `:481-493`).
2. **Alternative censite (data+fonte)**: IPOPT / filter-SQP
   (Fletcher-Leyffer) / SLQP / **Uno** / proximal-bundle (D6:738, mai
   costruito) — censimento del panel wave-2 **2026-08-19**
   (`PANEL_C31TRIO` via `VERDICT_wave2.md#4.1`, sfoundations_raws);
   dossier Uno full-read **2026-08-20** (`DOSSIER_uno_fullread.md` §3,
   10 input di spec arm-B, consumati nel contratto [P-IPADJ] per
   ordine utente); censimento warm-start IP **2023-2026** = input
   [P-IPADJ] (nota C31). Registry: `vanaret_leyffer_2026_uno` (MPC
   2026, pubbl. 2026-06-10, versione pubblicata = upload utente
   2026-08-20) + `vanaret_montoison_2026_joss` (JOSS 2026, riga
   propria). **Repo Uno QUARANTINATO in `Uno/` — mai nei commit, come
   GENO/.**
3. **Verdetto + perché**: incumbent = scipy trust-constr IP (in uso da
   S22) sotto disciplina INFORMATION-ONLY dei moltiplicatori fino a
   [P-IPADJ]; driver = TR-Newton segmentato a curvatura misurata,
   attivato SU NUMERI (§1.3(d)). Uno = flip candidate (install =
   decisione O5-class); A/B pinnato a constraint-set identico con
   guardia identical-certified-outcomes; falsifier-two CONDIZIONATO al
   leg semantico del falsifier-one (aggiudicazione orchestratore di
   record, nota C31).
4. **RECENCY/SOTA-ness del censimento**: il censimento solver è DATATO
   (2026-08-19/20) e dichiarato tale; copre il landscape 2026 incluso
   Uno (paper 2026-06) e la linea warm-start 2023-2026; la sua
   ri-verifica è COLLOCATA nel cluster di ri-esame F2-entry (C31-A/B +
   C58 delta-sweep vs landscape 2026 + SDP-CAND-8, mappa `:199-206`).
   `ATTUALE(engine NLP nonlineare vincolato incl. Uno 2026, 2026-08-23)`
5. **Falsificatore**: engine falsifiers one/two/three (VERDICT_wave2
   §1.1 via ledger); la guardia identical-certified-outcomes sull'A/B.
6. **Trigger ri-esame + finestra**: [P-IPADJ] = PRIMA azione engine F2
   sul critical path di C28; **finestra NOMINATA = F2-entry** (cluster
   superficie A; nessuna fase apre con NEVER sui componenti che
   consuma, PROGRESS `:213` scope R35(a)).

### CARD C58/stack differenziabile

1. **Scelta**: C58 — fondazione dello stack AD (ledger `:783-793`).
2. **Alternative censite (data+fonte)**: hand-coded adjoint /
   AD-in-altro-framework (Julia+Enzyme, Fortran+Tapenade, landscape
   2026) / gradient-free — censimento G0 **2026-07-17** (DIR-G0,
   `docs/rde_nozzle_G0_decision.md`; D6 `:753-774`); riga C58 coniata
   **2026-08-20** con entry contract (la domanda ri-ancorata da "gradienti
   esatti affordable" a "quale fondazione realizza l'architettura
   aggiudicata").
3. **Verdetto + perché**: JAX primario, custom_vjp + implicit-function
   rules ("never unrolled"); evidenza 52/52 Jacobiano in tolleranza
   derivata, overhead adjoint ~1.5%, X-GENOXC 218/218 con controlli
   negativi (§1.3(a)).
4. **RECENCY/SOTA-ness del censimento**: la survey di fondazione è
   del **2026-07-17** e il ledger stesso ORDINA il delta-sweep di G0
   vs il landscape 2026 (owner C58: "census+refuter panel as 9(e)
   delta-sweep"); Julia/Enzyme mai benchmarkato su questo host
   (G0 §4 `:199-201`). `STALE → finestra F2-entry (delta-sweep 9(e),
   cluster superficie A)`
5. **Falsificatore**: loop-speed flip clause ARMATA e quantificata
   (T1 1.593 ≤ 4; T2a 0.116 ≤ 1.197 s, PASS; review S25 = firing T2
   di S18 strutturale, decisione STA); assembled-loop impraticabile →
   flip Julia+Enzyme (D6 `:773-774`).
6. **Trigger ri-esame + finestra**: ri-censimento C58 al cluster
   engine **F2-entry** (stessa superficie A della C31).

### CARD C49/rappresentazione (fitted-front)

1. **Scelta**: C49 — rappresentazione per-fase per il design (ledger
   `:682-692`).
2. **Alternative censite (data+fonte)**: capturing adjoint-consistent
   come solver unico / two-tier col carrier |J_captured − J_fitted| /
   implicit shock tracking moderno (HOIST `huang_zahr_2022`;
   `wanted_thakur_nadarajah_2024` JCP 523:113633) — aggiudicazione
   wave-2 **2026-08-19** (`VERDICT_wave2.md#4.8`, 4 alberi de-novo
   ciechi come avvocati genuini); entry-gate items ancorati al
   retro-sweep **2026-08-20** (HZ §5.2-5.3 + Thakur p.26).
3. **Verdetto + perché**: fitted-front = UNICO portatore di
   certificato (classe S1); capturing = tier esploratore nominato
   build-gated; argomento portante = adjoint front-motion term (classe
   Giles-Pierce) + teorema negativo Giles-Ulbrich (LL-12, scope 1-D
   scalare dichiarato). ZERO finding refuter sulla riga.
4. **RECENCY/SOTA-ness del censimento**: censimento 2026-08-19/20;
   copre la linea implicita 2022-2025 (HOIST JCP 454; Thakur versione
   journal 2025, più nuova dell'ask). `ATTUALE(shock handling per
   marcia MoC certificata, 2026-08-23)`
5. **Falsificatore**: 4 falsificatori pinnati sul tier esploratore;
   frontiera fit-vs-capture governata dal budget DWR (C11 leg (b)).
6. **Trigger ri-esame + finestra**: duty F2/F5-C49-CAPTURE-EXPLORER
   (nominata, non schedulata); entry gate dell'upgrade implicito su
   checklist pubblicate — spara quando la linea le soddisfa.

### CARD C24/thermo tabulata

1. **Scelta**: C24 — chiusura termodinamica (ledger `:408-416`).
2. **Alternative censite (data+fonte)**: NASA-direct (solo oracolo,
   condizione C-A) / dCp-ingest (gated C-B) / Cantera-in-the-loop
   (scartata dalla direttiva S11 tables-as-interface) — survey
   `ADVISORY_S24_thermo_closure_survey` **2026-08-12** (riga R23,
   PROGRESS `:201`); verifica wave-3 **2026-08-20** (nota C24).
   Precedenti di campo: LL-32 (Johnson-Boney 1975, Scofield-Hoffman
   1971); generatore: LL-33 (`browne_shepherd_sdtoolbox_2018`).
3. **Verdetto + perché**: [X-THC1] tabelle quintic C1 (backend-1),
   status DECIDED; C-A SCARICATA nel carrier (oracolo NASA-direct a
   roundoff, tocco M3 S25); il contratto d'interfaccia è la tabella.
4. **RECENCY/SOTA-ness del censimento**: survey 2026-08-12; la threat
   2025 è censita dal lineage sweep **2026-08-23** (LL-34, Janc 2025:
   finite-rate differenziabile NON-tabulato = vettore di minaccia
   nominato). `ATTUALE(chiusure thermo per marcia differenziabile,
   2026-08-23)`
5. **Falsificatore**: condizioni C-B/C-C/C-D aperte e nominate;
   LL-34 = falsificatore COSTRUIBILE del backend-1.
6. **Trigger ri-esame + finestra**: F2 (C-B..C-D, owner dichiarato);
   il box tabella (C25) e l'out-of-box (C26) sono righe SEPARATE con
   finestre proprie (card C25 sotto).

### Card "non-aggiudicata, finestra Y" (2 SA + 7 NEVER toccate qui — MAI omesse)

1. **C17 — trip cap N_NEWTON=30** [SINGLE-AUTHOR]. (2) Alt: derivazione
   dal contraction budget — censita in `ADVISORY_S24_sota_gapmap`
   **2026-08-12**; cross-reconciled 2026-08-13, wave-3 2026-08-20
   ("no derivation or panel adjudication found", ledger `:342`).
   (3) **NON AGGIUDICATA** (KAT prova che morde, non la deriva).
   (4) censimento 2026-08-12/20: `ATTUALE(costanti Newton del driver,
   2026-08-23)`. (5) nessun falsificatore pinnato — lo pinna la
   finestra. (6) **Finestra: F2** (owner delta VERDICT_wave3 par.3).
2. **C18 — costanti di floor (NTF=100, C_FLOOR=8)** [SINGLE-AUTHOR].
   (2) Alt: Higham gamma_n / More-Wild noise floors — gapmap
   **2026-08-12**; sweep GAP-29 ESEGUITO S25-bis.
   (3) **NON AGGIUDICATA** (lo sweep è misura sull'incumbent — 1 flip —
   non un confronto Higham/More-Wild; la FORMA NTF=η·κ_q è derivata,
   la costante no). (4) `ATTUALE(floor di certificazione, 2026-08-23)`.
   (5) sweep GAP-29 (NTF/2 flippa) = rejector già provato. (6)
   **Finestra: derivazione F2-live** (condivisa col Tier-1 C20).
3. **C25 — box tabella (1050/3900 K, N_TAB=8192)** [NEVER]. (2) Alt:
   box envelope-derived + margine dichiarato + certificato per-run —
   gapmap **2026-08-12**, verifica wave-3 2026-08-20.
   (3) **NON AGGIUDICATA** (i letterali restano underived; l'attacco
   "over-engineering" fu judge-REJECTED, che non è un'aggiudicazione).
   (4) `ATTUALE(dominio tabelle, 2026-08-23)`. (5) H-F6 reachable-set
   box = l'oggetto che C45/C26 consumano per nome. (6) **Finestra: F2
   (con C-C/C-D)**.
4. **C38 — dichiarazione di stazionarietà outcome-II** [NEVER]. (2)
   Alt: certificato di B-stationarity / reporting normalizzato —
   gapmap **2026-08-12** (GAP-2 "squarely on-axis", pipeline-sense
   R4). (3) **NON AGGIUDICATA**. (4) `ATTUALE(stazionarietà
   nonsmooth, 2026-08-23)`. (5) i carrier committati con qualifier
   "until O1" (claims `:1350`, `:1874`) = i casi che la policy deve
   comporre. (6) **Finestra: F2**.
5. **C55 — aggregazione P_amb** [NEVER, strutturalmente vuota]. (2)
   Alt: nu-weighted mean / minimax / CVaR-DRO — slot mintato
   **2026-08-19** (problem book, P_amb SLOT OF RECORD).
   (3) **NON AGGIUDICATA** — domanda VUOTA sotto il default single-point
   (mappa `:66`). (4) `ATTUALE(aggregazione ambiente, 2026-08-23)`.
   (5) — (la struttura: F affine in Pa, envelope morde solo via
   ammissibilità). (6) **Finestra: prima istanziazione multi-punto di
   P_amb** (aggiudicazione dovuta a istanziazione, non prima).
6. **C57 — tier di esplorazione globale** [NEVER]. (2) Alt: layer
   DFO/BO/evolutionary sopra il closer certificato / captured-explorer
   C49 / multi-start continuation — mint wave-2 **2026-08-19**
   (VERDICT_wave2 §4.14); pilota rival-paradigm ratificato dall'utente
   **2026-08-20** come CANDIDATE. (3) **NON AGGIUDICATA** (il
   certificate-first resta assiologia dichiarata, mai head-to-head).
   (4) `ATTUALE(esplorazione globale, 2026-08-23)`. (5) il pilota
   one-shot (J per arm + budget + costo di certificazione del
   vincitore) = il falsificatore disegnato. (6) **Finestra: F2-entry**
   (con C31 A/B e C49 explorer).
7. **C59 — forma temporale del funzionale** [NEVER, strutturalmente
   vuota]. (2) Alt: harmonic-balance / time-spectral / windowed
   unsteady adjoint — mint **2026-08-21** (coverage gate C4; ancore
   rubino_2018, schotthofer_2024, zahr_persson_2016).
   (3) **NON AGGIUDICATA** — dentro il pin dell'onda il cycle-average
   è CANONICO (conseguenza teorematica, scoping VINCOLANTE): la
   domanda è vuota finché il pin regge. (4) `ATTUALE(forme temporali
   del funzionale, 2026-08-23)`. (5) — (le alternative vivono SOLO a
   pin indebolito). (6) **Finestra: trigger = regime weakened-pin
   (multi-frequenza / aperiodico) in scope**.
8. **C60 — NAND vs SAND (LNKS)** [NEVER]. (2) Alt: SAND full-space
   one-shot / ibridi — mint **2026-08-21** (coverage gate; pesata
   FUORI ledger in `docs/rde_nozzle_pipeline_audit.md:105` "deferred,
   not dismissed"). (3) **NON AGGIUDICATA** (incumbent NAND DICHIARATO:
   praticato, supporti misurati, head-to-head mai corso). (4)
   `ATTUALE(architettura state-design coupling, 2026-08-23)`. (5) un
   flip futuro rientra nelle righe consumatrici SOLO via i loro
   falsificatori pinnati (disciplina C58). (6) **Finestra: F2-entry
   (cluster con C57/C58/[P-IPADJ])**.
9. **C62 — quadratura di fase su Ξ** [NEVER]. (2) Alt: Gauss /
   adattiva event-stratified / QMC / risoluzione declared-canonicity
   (pattern C59) — mint **2026-08-21** (coverage gate; unica ancora di
   copertura = diff par.2.10). (3) **NON AGGIUDICATA** (clausola di
   onestà del critic: l'asse è pesato UNA volta, senza tabella di
   alternative). (4) `ATTUALE(quadratura del funzionale mediato,
   2026-08-23)`. (5) findings `:988` (barra di quadratura omessa) = il
   promemoria armato. (6) **Finestra: F2 cluster numerica; trigger =
   primo accuracy budget della campagna** (il budget non chiude senza
   barra di quadratura nominata).

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

---

## DECK FEED

[Emendamento v2.1 §3 (G-4): asserzioni candidate-slide in frase piena
(assertion-evidence) + ancora + classe. Lo storyboard v3 joina su
queste righe, non ri-legge il capitolo.]

1. **Ogni scelta algoritmica della macchina è un oggetto tipizzato con
   status, alternative pesate e falsificatore: 62 righe, 12 DECIDED /
   36 MIXED / 12 NEVER / 2 SINGLE-AUTHOR — e vi mostriamo anche le
   non pesate, ognuna con la sua finestra.** — mappa
   `docs/rde_nozzle_pipeline_decision_map.md:287-309` — [REP].
2. **Il gradiente è esatto per il problema discreto che risolviamo
   davvero: 52/52 entrate di Jacobiano in tolleranza DERIVATA, adjoint
   a ~1.5% del solve, oracolo cross-code 218/218 con controlli negativi
   che rigettano.** — G0 `:33-59, :94-104` — [REP].
3. **Il run di record chiude con trasversalità KKT 7.7e-02 contro
   soglia derivata 1.156e-01 e oracolo cross-code 91/91 — stage V0
   verification, dichiarato su slide.** —
   `validation/PROGRESS_2026-08-06_S18_brick2run.md` + rider P34 —
   [REP] + dichiarazione di stage.
4. **La velocità è stata una scelta algoritmica, non tuning: ogni leva
   con gate di invarianza + refuter; 100.84→32.09 s (S25, val_grad
   6.6×) → record 5.58 s e target MET formali pre-registrati (segmento
   14.9-20.1 s vs ≤30; campagna 10-14 min vs ≤25).** — commit
   `07400a4`; PROGRESS `:119-125` — [REP], caveat host dichiarato.
5. **Un certificato che non può bocciare non è un certificato: NTF ha
   forma derivata η·κ_q e lo sweep GAP-29 prova che la soglia morde —
   NTF/2 flippa il verdetto.** — M0:3649-3766 [LAND-C4-LA2]; PROGRESS
   `:155-160` — THEOREM*/SCHEMA + [REP].
6. **La suite dice 23/23 E il record dichiara l'incidente: il claim era
   stato citato PRIMA dell'evidenza, il ri-conteggio l'ha colto, il run
   verificato è il carrier.** — commit `c9bacd9` — [REP] (slide di
   onestà, accoppiare alla #7).
7. **Abbiamo commissionato un audit ostile alla nostra catena di
   certificazione: verdetto NON-CERTIFICABILE, 2 P0 — uno riparato in
   finestra, uno con owner F2. Il sistema funziona perché boccia noi.**
   — PROGRESS `:211` (R33) — [REP].
8. **Nel campo RDE-nozzle nessuno dei quattro paper coupled ha un
   optimizer nella catena ("no optimizer appears anywhere in the four
   papers"); la nostra catena design-adjoint per-fase discende dai
   parent FUORI campo (Byrd-Nocedal; Hoffman 1967) — lineage
   dichiarato, novità query-bounded.** — CH5 §1.1 (SYN:58-61) + §3-bis
   LL-30/LL-7/LL-31; assenza query-bounded su DUE fonti: LM:354-362
   (gap verdicts b2) + `ADVISORY_litmap_extension_2026-08-13.md`
   (sweep 1971-2026, 2 near-miss) [WB1-C3-09] — [ADV]+[REP].
   **CAVEAT P-B OBBLIGATORIO** (slide che usa questo feed lo porta o
   punta al box nomenclatura CH5 §1.1 [WB1-R3]): P-B (Li-Xu 2023) USA
   il variazionale classico Rao/Vander-Veen — ma su UNO stato steady da
   p0/T0 TIME-AVERAGED ("empirically recognized", p. 5), e il suo
   p_b = "averaged base pressure" SPAZIALE sulla base del plug (Eq. 26,
   nessun nesso dichiarato col cycle-averaging; fonte e provenienza del
   valore NON dichiarate) — `VERIFY_PB_corner_pb.md` (source-verified
   2026-08-23). "Nessun optimizer" ≠ "nessun variazionale": la frase
   SYN vale per la catena di OTTIMIZZAZIONE, P-B resta il caso
   variazionale-su-stato-mediato.
9. **Il flip-candidate dell'engine ha nome, data e finestra: Uno
   (MPC 2026), A/B a constraint-set identico, decisione d'install
   O5-class, ri-esame al cluster F2-entry — il censimento solver è
   DATATO e dichiarato tale.** — card C31 (§7-bis); ledger `:481-493`
   — [REP].
10. **Il fitted-front è l'unico portatore di certificato per un motivo
    pubblicato (teorema negativo di Giles-Ulbrich), e l'upgrade
    implicito ha un entry gate sulle checklist pubblicate della linea
    stessa.** — ledger C49 `:682-692`; §3-bis LL-12 — [REP].
