# CH10 — Il contratto dei dati: che cosa serve, in DATI, per far girare il tool su un motore NON nostro

Status: capitolo NUOVO dell'atlas S-PRES (onda W-B.1, slot B2, 2026-08-23).
Nodo servito: **N-K** (riga K della matrice §M, design v2 come emendato
v2.1). Non aggiudica nulla: ancora al record (M0 D2.4/VI.1, D6 F2a/G6/
Annex B, D1 §4.3bis, conditionals ledger, choice ledger) e dichiara gli
aperti. **Stadio di confronto**: il record aggiudicato del contratto-dati
contro la pratica del campo (linea imposed-detonation-BC, THROAT_HARVEST).
**Arco di consumo dichiarato**: storyboard v3 (via `## DECK FEED` in coda),
banca Q&A red-team (§8), refuter W-C.a (REFUTE_CH10; guardie 6/7/10/11/14
vive), mappa F2+ (§5). Template a 9 sezioni (1, 2, 3, 3-bis, 4-8);
§6 STORIA scritta dal round W-B.2 (slot B8b).

Nota di nomenclatura (dovere di precisione, namespace "L4"): in questo
capitolo convivono DUE oggetti chiamati L4 — (i) **L4 la classe-dati di
default** di D2.4 ("every patch of Gamma_d axially supersonic with margin",
`docs/rde_nozzle_MASTER.md:125-138`) e (ii) **L4 il layer-ledger dei
condizionali** (`docs/rde_nozzle_conditionals.md:1-2`, layer L4 del
SCAFFOLD). Ogni occorrenza sotto è disambiguata ("L4-DEFAULT" per la
classe, "ledger L4" per il layer). Analoga disambiguazione per "U3": la
**regola d'estrazione U3/U3'** del piano D6 (§1.5, §5, Q6) è un oggetto
DISTINTO dal **discharger U3** del condizionale C-D25U (ledger L4,
§1.4/§4.6) — stesso simbolo, due namespace.

---

## 1. LA DOMANDA (cella K-i)

**N-K** — *Che cosa serve, in DATI, per far girare il tool su un motore NON
nostro?* Falsificatore vivo: **G6 loud-reject su un dataset reale** (il gate
può dire NO, e finché nessun dataset reale è stato ingerito il NO non è mai
stato esercitato — dichiarato in §5); **U3' PREMISE-OPEN** (owner F2a,
`docs/rde_nozzle_development_plan.md:191-202`): il contratto di estrazione
non è freezabile prima.

### 1.1 L'oggetto di record: D2.4 [D-CONTRACT]

Il record risponde con un CONTRATTO, non con un formato file. D2.4
(`docs/rde_nozzle_MASTER.md:116-124`): l'interfaccia di design Gamma_d è
*"a fixed axisymmetric surface downstream of all heat release carrying the
data family s(xi)"*; il contratto è la terna **(Gamma_d, data class,
validity)** con tre requisiti — R1 separazione causale; R2 dati ben posti
(full state SOLO su patch assialmente supersoniche; patch subsoniche:
invarianti entranti + chiusura di impedenza o di choking, albero di
decisione in D1 §4.3bis); R3 misurabilità. La scala di idealizzazione è
dichiarata nel contratto stesso: I0 coupled bilevel / I1 wave-frame steady
field / I2 per-phase meridional profiles / I3 sonic family / I4 single mean
state (`:122-124`).

### 1.2 PRECISIONE VINCOLANTE: Gamma_d NON è "the throat" (guardia 11)

Riga di checkpoint di record, portata qui come contenuto ancorato (routing
C-1bis, ordine utente; verbatim dal checkpoint, righe :158-163 — la coda
di routing :163-165 "All of this -> CH10…" non è citata, è l'ordine che
questo capitolo esegue):

> PRECISION for deck/atlas: Gamma_d is NOT "the throat" — it is the
> axially-supersonic-with-margin station downstream of heat release
> (L4-DEFAULT m_n>=delta); the corrugated sonic line (KP18, M=1 crossed
> twice/cycle) is WHY the margin exists and why subsonic patches are a
> DECLARED case-class (D1 4.3bis O1-O4), never silently averaged.
> (`validation/spres_raws_2026-08-22/SESSION_STATE_checkpoint.md:158-163`)

I tre ancoraggi di questa precisione, ciascuno al proprio record:

1. **L4-DEFAULT** (`docs/rde_nozzle_MASTER.md:125-138`): il default
   certificato è la classe con ogni patch di Gamma_d assialmente
   supersonica CON margine; sul default la mdot-independence è ESATTA
   ([T-TH0] L4 note) e l'influenza media a monte è ESCLUSA PER TEOREMA
   ([T-NSW]) — le ex ipotesi H2/H-I2 sono DISCHARGED lì. Il certificato di
   record è lo split L4-CERT (M-a normal-on-surface / M-a'
   axial-on-segment+box) con forma normale meridionale
   **m_n := u·n_m − c ≥ delta** (`:139-166`) — la forma "u_x − c" nuda è
   planar-only.
2. **La sonic line corrugata** (KP18 = `kaemming_paxson_2018`, Fig. 6):
   due frammenti di harvest — *"corrugated sonic line: axial Mach
   0.85 -> 1.33"* e *"the sonic line is crossed TWICE per cycle"*
   (`validation/sfoundations_raws_2026-08-13/blocco3/
   THROAT_FIELD_HARVEST_c4.md:399-406`, riga S4 della tabella interfacce
   `:611`). È il PERCHÉ del margine: una stazione "alla gola" attraversa
   il locus di degenerazione due volte per ciclo — il contratto chiede la
   stazione a valle dove il margine m_n ≥ delta è misurato, non la gola
   geometrica.
3. **Patch subsoniche = case-class DICHIARATA** (D1 §4.3bis, opzioni O1-O4,
   `docs/rde_nozzle_problem_book.md:302-321`): O1 spostare Gamma_d a valle
   del crossing assiale-sonico; O2 dati parziali + impedenza; O3 surrogato
   di choking; O4 anchor BVP inalterato. Le chiusure delle patch subsoniche
   portano H2/H-I2 come *class assumptions* con monitor esistenti e
   downgrade di Verdict documentati (`docs/rde_nozzle_MASTER.md:131-135`)
   — mai mediate in silenzio.

**La lettura fisica che tiene insieme i tre ancoraggi** — regola di
interpretazione del feedback ugello→camera (pin utente 2026-08-23,
verbatim: *"ci dovrebbe essere solo se la porzione pre gola è convergente
e con gola tutta sonica o supersonica, o se la gola, anche throatless
geometrica, è a patch subsoniche"*; **guardia 17 / CKP-S2-1**). Lettura di
record: il **DECOUPLING** a monte (l'assenza di feedback che legittima
ogni architettura one-way/imposed-BC) è asseribile SOLO sotto **choking
pieno** — porzione pre-gola convergente E gola/superficie sonica tutta
sonica-o-supersonica lungo ciclo e azimut; il **feedback ESISTE** se la
gola — anche throatless geometrica: la superficie sonica fa da gate —
presenta patch subsoniche, che sono i canali di risalita
dell'informazione. È il PERCHÉ fisico dei due lati del contratto, in DUE
direzioni distinte a gradi dichiarati: **decoupling ⇒ choking pieno** (la
direzione del pin — NECESSITÀ: il choking pieno è la condizione di
ammissibilità di ogni claim di decoupling/one-way, ed è ciò che il
margine m_n ≥ delta verifica su Gamma_d patch per patch); la direzione
INVERSA non è il pin e vale nel record solo al livello MEDIO e sulla
classe — su L4-DEFAULT [T-NSW] esclude per teorema l'influenza media a
monte (lettura a piccole perturbazioni). E **patch subsoniche ⇒ canale di
feedback**: è il perché O1-O4 è una case-class DICHIARATA con H2/H-I2 come
class assumptions — una patch subsonica non è un dettaglio numerico, è un
canale di risalita aperto. NESSUN claim di decoupling/one-way BC senza la
condizione di choking citata; regime forte-transiente (unstart) = fuori
dalla lettura a piccole perturbazioni, confine dichiarato se toccato.

### 1.3 L'ammissione: audit stage-A + G6 loud-reject

Il contratto non si fida del dato: lo AUDITA. Stage-A
(`docs/rde_nozzle_development_plan.md:174-176`; M0 VI.1 :3067-3075):
completezza caratteristica; residuo di **Crocco**; margine di
spacelikeness dichiarato come m_n(xi) = ess inf_y (M_n − 1) sulla normale
meridionale (TOTAL Mach PROIBITO come quantità di audit); margini
H-I2/choking; certificato di T0 flatness/harmonic-decay. Il gate:

> G6 (new) DATA-CONTRACT GATE: any CycleFamily failing stage-A audits
> (Crocco, completeness, H-I2) is rejected loud — no design on
> inconsistent data. (`docs/rde_nozzle_development_plan.md:808-810`;
> operativo da F2a, tabella gate `:290`)

Il loud-reject set è ESTESO di record (2026-08-19) dal rejector TRIPLE di
D.14 e dalla riga di audit angular-momentum D.16 — entrambi PRACTICE,
SPECIFIED-NOT-ARMED fino alla prima ingestione
(`docs/rde_nozzle_development_plan.md:811-815`; M0 VI.1 :3076-3082).
Invariante di Annex B: gli audit stage-A si applicano ANCHE ai dati
GENERATI — "a generator emitting off-manifold data is a generator bug"
(`docs/rde_nozzle_development_plan.md:1150-1151`).

### 1.4 Ledger L4: quali condizionali il contratto eredita

Il ledger dei condizionali (`docs/rde_nozzle_conditionals.md:1-16`) separa
due nature che il capitolo tiene distinte: i condizionali **analitici**
(C-D25U stabilità semiglobale uniforme, con struttura -a/-b/-c e
discharger U1-U5; C-MAJDA) — enunciati UNA volta nel ledger, ereditati BY
ID da ogni THEOREM* — e i condizionali di **chiusura/residuo numerico**
del claims registry (C-HT4, C-IGMIX, C-O33: *"model closures and numeric
residuals, NOT analytic gaps"*, `:7-9`). Per il contratto-dati la
conseguenza operativa: un dataset che entra dal contratto eredita i
condizionali dichiarati della classe su cui atterra (L4-DEFAULT: H2/H-I2
scaricate per teorema; patch subsoniche: H2/H-I2 come class assumptions),
e ogni Verdict a valle li stampa — mai ipotesi silenziose.

### 1.5 I due aperti di proprietà F2a

- **U3' (choking adjudication RDE)** — PREMISE-OPEN: la regola U3 di
  estrazione presuppone una superficie per-fase assialmente supersonica a
  valle della gola, intuizione steady-nozzle il cui trasferimento all'RDE
  (gola spazzata da un pattern rotante; letteratura con claim "steady
  criteria are invalid") NON è stabilito; U3' deve aggiudicare ipotesi,
  monitor eseguibile e il caso NO (patch subsonica con chiusura
  dichiarata). *"U3 stays PREMISE-OPEN until U3' closes; NO freeze of the
  extraction contract before"* (`docs/rde_nozzle_development_plan.md:
  191-202`, ribadito `:264-267`).
- **Contact/slip** — le discontinuità di contatto (linearmente degeneri,
  IL carrier principale di stratificazione nell'esausto RDE, DENTRO la
  data class del problem book) non sono coperte dalla macchineria d'urto
  U3/U4 (Lax-shock-only BY CONSTRUCTION): ownership F2a, default = smeared
  contact marched as smooth stratified data (giustificazione: degenerazione
  lineare, no self-steepening; classe di rigore dichiarata), opzione
  FITTED-contact = estensione F4b, mai ereditata dai certificati d'urto
  (`docs/rde_nozzle_development_plan.md:176-190`).

---

## 2. LETTERATURA (due colonne)

### 2(a) Senso / precedenti: il campo consegna CFD, non contratti-dati (cella K-iii)

Claim ancorato (non nuovo in quest'onda): **nessuno dei quattro paper
P-A..P-D dichiara una classe di dati d'interfaccia** — il campo consegna
campi CFD e sweep, mai un contratto (ancora: CH5 §1.1,
`validation/spres_raws_2026-08-22/reconstruction/
CH5_literature_positioning.md:25-…` — "quattro paper, quattro 'metodi',
nessuna riduzione per-phase"; residuo A-iii del design v2). La riga di
harvest che lo inchioda sul lato spettrale: *"Periodicity is exhibited,
never spectrally verified"* — il pin periodico è ESIBITO nei CFD del
corpus, MAI verificato spettralmente (zero figure FFT/PSD nei 9 paper CFD
censiti; `validation/sfoundations_raws_2026-08-13/blocco3/
THROAT_FIELD_HARVEST_c4.md:571-573`, `:687`).

Il precedente più vicino è la linea **IMPOSED-DETONATION-BC** — routing
C-1bis di record, portato verbatim dal checkpoint (righe :146-158):

> C-1bis FOURTH LINEAGE LINE (user question, late window): the
> IMPOSED-DETONATION-BC ARCHITECTURE — Paxson & Harroun impose an
> external detonation profile as inlet BC to a decoupled nozzle domain
> (Harroun 2021 Eq.7: analytic rotating P(theta) 30->2atm 13.8kHz,
> p-ONLY, no swirl — atlas H21-F11; "BC contract p-only documented",
> THROAT_HARVEST) = the direct ancestor of OUR Gamma_d data-contract
> pipeline (CFD/engine-data up to the interface -> our tool downstream;
> Annex B front-end taxonomy).
> (`validation/spres_raws_2026-08-22/SESSION_STATE_checkpoint.md:146-153`)

Ancore primarie della linea: `harroun_2021` Eq. 7 / Fig. 11 (H21-F11) — il
contratto BC estratto integralmente dall'harvest: p-only, radially flat,
swirl-free, T uniforme; profilo di record dell'harvest: log-decay sawtooth
30 → ~2-6 atm per settore da 180° (il "30->2atm" del checkpoint è la
compressione di quel range); gli autori stessi flaggano la T uniforme come
controfattuale alla loro fonte (`THROAT_FIELD_HARVEST_c4.md:276`, `:296`,
`:608`, `:763`). Caveat CT-6, valido per OGNI numero altrui del capitolo
alla sua prima occorrenza: numeri di `harroun_2021` (e degli altri paper
citati) riportati con citazione piena e MAI riprodotti da noi.
Le altre ancore: `harroun_2020` Eqs. 1-2 (stessa architettura);
`miki_2020` = l'antenato OPERATIVO (frozen unsteady inlet BC su 6
geometrie); `paxson_miki_2022` (J cycle-averaged a livello CFD sulla
stessa pratica). Antenati steady della prescrizione-dati:
`humphreys_thompson_hoffman_1971` (start-line) e
`johnson_thompson_hoffman_1974` (inflow rotazionale). Cugino più vicino
sul lato inflow-BC wave-frame: Fievisohn (LL-13). Tutto il lineage claim è
formalizzato in §3-bis dal LINEAGE_LEDGER (guardia 10).

### 2(b) Strumenti: la pipeline CFD-to-contract, forma [V2-R5] (cella K-ii)

Come i dati arrivano al contratto quando l'input è un CFD (caso a monte
del front-end): il piano di record definisce l'operatore di estrazione
d'interfaccia — lineage RI-ANCORATO a D6:

> case-B per-phase generator UPGRADED per use-case duty U1 to a
> CFD-to-contract PIPELINE: interface front-extraction operator —
> captured-shock detection (Gelb-Tadmor concentration method lineage) +
> RH-consistent sharp-state reconstruction (Paciorri-Bonfiglioli
> fitted-front lineage) + exact-RH projection with DERIVED residual band
> + LOUD REJECT + synthetic smear-extract-compare KAT as its own oracle
> (`docs/rde_nozzle_development_plan.md:256-263`)

**ECCEZIONE NON-REGISTRY DICHIARATA** (decisione A4 dell'emendamento v2.1
§6b, misurata in finestra lì): i due lignaggi "Gelb-Tadmor" e
"Paciorri-Bonfiglioli" sono NOMINATI in D6 :256-263 ma hanno **0 righe nel
literature registry** (grep della finestra A4 di record); il vicino
esistente citabile è `wanted_onofri_paciorri_2017_book`
(`docs/literature_registry.yaml:1142`). L'upgrade a confronto pieno
avviene SOLO SE le righe WANTED vengono mintate (finestra di promozione,
R7) — qui il capitolo dichiara l'eccezione nel testo, come da forma
[V2-R5], e non cita i due lignaggi come ref di registry.

Strumenti-monitor del contratto (già censiti in §1.3): stage-A audits,
TRIPLE spread monitor (D.14), angular-momentum audit (D.16), T0
flatness/harmonic-decay ([S14 F-FLAT], M0 VI.1 :3073-3075), recovery di
stato UNICO sotto AUD-cp + AUD-c2T (THEOREM, gamma(T)-exact; M0 VI.1
:3084-3087) con flag-never-extrapolate (AUD-hRANGE).

---

## 3. LA PROPOSTA

**La proposta del programma è il CONTRATTO STESSO**: sostituire
l'imposizione di un profilo p-only con un'interfaccia tipizzata, staged e
auto-rigettante — *CFD/engine-data fino all'interfaccia → il tool a valle*
— così che il tool giri su un motore NON nostro senza ereditarne il CFD.

1. **Contratto staged full-state** (D.13, §4 per l'analisi formale): non
   "dateci tutto", ma una scala dichiarata di ricchezza d'input — la
   **Annex B input taxonomy** (cella K-iv; `docs/rde_nozzle_development_plan.md:
   1132-1157`): caso A (solo specs: propellente, φ, pressione media,
   geometria annulus, Pa) → fully predictive, con il fixed full-flowing
   bell = Rao-at-⟨Pc⟩ BY THEOREM; caso B (+ modello di struttura d'onda
   non-CFD) → il full CFD-free tool, con il generatore di profili come
   UNICO modulo di fisica nuovo; casi C-G (calibrazione sperimentale,
   profilo di missione, envelope di throttle, incertezza dichiarata,
   coupling di camera) — ogni input ammissibile mappa a un generatore
   CycleFamily DICHIARATO con la sua classe di rigore, macchina a valle
   identica. Questa tabella È la risposta pronta alla domanda ESA "che
   input vi serve" (puntatori: CH4 §1.2 per la pipeline a 8 stadi che la
   consuma; CH6 §1.6 per le ASK). Stage di evidenza P34 (guardia 7): il
   caso A è **prediction** — contratto e teoremi di struttura, mai ancora
   esercitato su un motore reale; nessun claim engine-level di validazione.
2. **L'ARGOMENTO DI CHIUSURA** (correzione theorem-backed dell'antenato) —
   verbatim dal checkpoint (routing C-1bis, righe :154-158):

   > THE CLOSING ARGUMENT (theorem-backed correction of the ancestor):
   > their BC is p-only — exactly the projection T-DISC CONVICTS; our
   > staged full-state contract (D.13: +w/Gamma, h0 profile-grade, TRIPLE
   > monitor, m_n margin) IS the theorem-driven repair of their BC.
   > (`validation/spres_raws_2026-08-22/SESSION_STATE_checkpoint.md:154-158`)

   Il ponte formale è esatto, non retorico: la D1.2 di [T-DISC] definisce
   la **p-only projection** pi: s(xi) ↦ (P(xi), uniform) — *"the EAP-style
   / pressure-only reading of the interface"* (`docs/rde_nozzle_MASTER.md:
   1004-1008`) — cioè LA classe di BC che la linea Paxson-Harroun impone;
   e la catena convice la proiezione A GRADI DICHIARATI: [T-DISC-1]
   (`:1030`, THEOREM*) dà fibre non-degeneri, [T-DISC-2] (`:1086`,
   split-grade per gamba: sign leg THEOREM* SCOPED, confronti
   physical-h0-fixed) dà la J-separazione dentro la fibra — due dataset
   con la STESSA P(theta), le stesse medie di ciclo (pin [REV2-r1-1]:
   fibra = calibrated-scalars) e contenuto di fluttuazione/swirl diverso
   hanno J diversi; la conseguenza sugli OTTIMI è [T-DISC-3](b) (`:1184`,
   SCHEMA, con la premessa (DR) design-realizability NOMINATA, "checked
   per family at M-RED time"). Il p-only BC non è un'approssimazione
   innocua: perde informazione J-rilevante dentro lo scope dichiarato. La
   riparazione è il contratto D.13 (+w/Gamma, h0 profile-grade, TRIPLE
   monitor, margine m_n) — v. §4.
3. **Il rigetto come feature**: G6 loud-reject + stage-A + monitor armabili
   = il contratto può dire NO a un dataset reale (falsificatore di N-K).
   Novità query-bounded: il claim "nessun contratto-dati dichiarato nel
   campo" resta nella forma di CH5 (query G14, NOT-FOUND alle query citate
   lì) — questo capitolo non minta claim di novità nuovi oltre §3-bis.

---

## 3-bis. ANTENATI DIRETTI (lineage claim)

Join sul LINEAGE_LEDGER per {LL-id, componente} (contratto di join
[F-des-4]; guardia 10: lineage SOLO da lì; righe CANDIDATE fino al passo
C6 di W-C, i SEED utente sono confermati dalle parti e restano
attaccabili). Componente strutturale di questo nodo: (5) imposed-BC
contract (+ (6) periodic data class dove indicato).

| antenato (LL-id) | cosa fa | cosa gli manca vs noi |
|---|---|---|
| **LL-6** linea imposed-BC (Harroun Eq.7 p-only / pratica Paxson) — SEED C-1bis [P1.6] | impone una legge di ciclo analitica come inlet BC a un dominio ugello disaccoppiato (`harroun_2021` Eq.7: P(theta) rotante 30 → ~2-6 atm per settore, 13.8 kHz — harvest :608, CT-6 §2a; p-only, no swirl; H21-F11) | full-state, conteggio caratteristiche, metrica di contratto C50; è ESATTAMENTE la proiezione p-only che [T-DISC] convice (§3) |
| **LL-24** Miki 2020 — antenato OPERATIVO [P2.9] | frozen unsteady inlet BC applicato su 6 geometrie (`miki_2020`): la pratica imposed-BC portata a metodologia di design | nessun contratto dichiarato (classe dati, validità, audit); nessun rigetto; nessuna classe di rigore per fase |
| **LL-2** Harroun 2021 (+2020) [P1.2+P3.11] | famiglia per-phase steady 2-D + C_F quasi-cycle-averaged; convenzione di media UNDECLARED (deep-check alla fonte, duty (a) chiuso: peso/denominatore non dichiarati, pp.670-671 + Eq.10) | media non pinnata (la nostra mu è dichiarata, T-O2); validazione = istanza senza tier (CT-3); BC p-only |
| **LL-13** Fievisohn (JPP 2017 + PhD 2016) — SEED, [IO] [P2.S-1] | wave-frame + rotational shock-fitted MoC + **inflow BC**: il cugino più vicino della classe reduced-MoC (l'ugello resta [REP]-bounded via `wanted_fievisohn_2018_quasi2d_moc`, procurement 2018-0881 RAISED) | mai design, mai famiglia per-fase, mai contratto d'interfaccia con audit/margini |
| SEED-4 antenati steady (in LL: righe seed, stato post-sweep) | `humphreys_thompson_hoffman_1971` start-line; `johnson_thompson_hoffman_1974` inflow rotazionale: la prescrizione-dati steady classica | nessuna struttura di ciclo, nessuna classe periodica, nessun monitor |
| **LL-5** Paxson-Miki 2022 [P1.5] | J cycle-averaged valutato a livello CFD con la stessa architettura imposed-BC (`paxson_miki_2022`), OFAT | né ottimalità né bande; il dato non passa per un contratto |

Nessun claim di novità di questo nodo è senza riga: la genealogia
imposed-BC → Gamma_d è la QUARTA linea di lineage (SEED-4, *"CONFERMATA
(P1.6) con antenati steady aggiunti… e antenato operativo Miki 2020
(LL-24)"* — `validation/spres_raws_2026-08-22/reconstruction/
LINEAGE_LEDGER.md:27-29`).

---

## 4. ANALISI FORMALE

Classi di rigore dichiarate riga per riga (R4/R5):

1. **[D-CONTRACT] D2.4** — definizione di record (M0 :116-124) con
   **L4-DEFAULT** (M0 :125-138): sul default, mdot-independence ESATTA
   ([T-TH0] L4 note — THEOREM) e mean upstream influence esclusa
   ([T-NSW] — THEOREM); H2/H-I2 DISCHARGED lì, class assumptions altrove.
2. **L4-CERT split + forma normale** (M0 :139-166) — THEOREM di record
   (D.4 curved clause CONFIRMED THEOREM): (M-a) m_n ≥ delta on-surface =
   certificato d'ammissione; (M-a') axial-on-segment + box = certificato
   di volume che i teoremi di causalità consumano; la forma nuda u_x − c è
   planar-only (controesempio tilted-element = rejector di wiring).
3. **D.13 [MS-DEF-CONTRACT]** — la CycleFamily di record (M0 VI.1
   :3049-3087): {P0, T0, gamma(.;xi) | M_in meridionale, theta_in,
   s(y;xi), **w(y;xi) ≡ Gamma(y;xi) = R·w** (riga di trasporto,
   DEFINITION + recovery THEOREM), **h0(y;xi) PROFILE-grade** (promozione
   di record: sotto il contratto pre-swirl h0 era costante per costruzione
   → ogni monitor Delta_h0 sarebbe stato VACUO, rejector-incapable;
   staging Rmk 4.1, THEOREM)} + mu + provenance + risultati stage-A.
   Classe dati: righe in BV ∩ L∞(y), piecewise C¹ sufficiente.
4. **Monitor**: TRIPLE spread di D.14 (G6 rejector; PRACTICE con la gamba
   LICENSING = SCHEMA a due gambe G-b1/G-b2, conditional G-b1 stampata in
   ogni verdetto di licensing; direzione BLOCKING usabile ora,
   conservativa — M0 VI.1 :3076-3080); D.16 angular-momentum (PRACTICE);
   pin bloccanti pre-ingestione B-1 (normalizzazione A4 del "3-6%
   tangential energy": KE-normalized vs h0-normalized ~4x) e B-2
   (h0-convention provenance clause: se h0 include u_theta²/2 è un CAMPO
   DICHIARATO del contratto — M0 VI.1 :3088-3099; consumato da [T-DISC]
   D1.1 come hypothesis switch, M0 :999-1002).
5. **[T-DISC]** (M0 :977-1219, landed S-FOUNDATIONS-C4 2026-08-20) — il
   teorema che regge l'argomento di chiusura: D1.2 p-only projection
   (:1004-1008) con pin [REV2-r1-1] (default fase-uniforme = le mu-medie
   della famiglia stessa: fibra = calibrated-scalars); [T-DISC-1] fiber
   non-degeneracy (:1030, **THEOREM***); [T-DISC-2] J-separation lower
   bound within a fiber (:1086, **split-grade per gamba**: sign leg
   THEOREM* SCOPED, booking level sotto H2.2, confronti physical-h0-fixed;
   ramo uncompensated-DROP geometry-signed a separazione ZERO nel corner
   degenere — nessun floor positivo asserito lì); [T-DISC-3] 2-epsilon
   transfer sull'ottimizzazione (:1184, **SCHEMA**; la gamba (b) porta la
   premessa (DR) design-realizability nominata, checked per family a
   M-RED time). Scope: classe A di D1.1 (pure periodic single-mode, frozen
   thermally-perfect, H9, mu pushforward) — la catena convice la
   proiezione DENTRO la classe dichiarata, non oltre, e ogni gamba parla
   al SUO grado.
6. **Condizionali ereditati** (ledger L4): C-D25U (-a/-b/-c con U5 NAMED
   MISSING) per gli heir THEOREM*; chiusure C-HT4/C-IGMIX/C-O33 =
   closure-conditional del registry, non gap analitici
   (`docs/rde_nozzle_conditionals.md:1-60`). Il Verdict di ogni run su
   dati esterni stampa l'eredità.

Perimetro e canali residui (guardia 16, regola di classe): i teoremi del
punto 1-2 coprono la classe L4-DEFAULT; i canali NON coperti sono nominati
con classe — patch subsoniche (case-class O1-O4, H2/H-I2 class
assumptions, downgrade documentati), contact/slip (ownership F2a, default
smeared con classe di rigore da dichiarare, §1.5), choking RDE (U3'
PREMISE-OPEN), fronti/jitter del datum (metrica C50, componente
front-block: shift-differentiability rigorosa in 1-D,
practice-without-theorem in multi-D — theorem_ledger :235, FS-2 guardia
empirica viva).

---

## 5. STATO (dimostrato / parziale / aperto; decisioni con owner e trigger — cella K-v)

**Dimostrato**: D2.4 + L4-DEFAULT + L4-CERT (THEOREM, con condizionali
ledger); D.13 recovery theorem; h0-promotion (THEOREM); [T-DISC-1]
(THEOREM*) e [T-DISC-2] sign leg (THEOREM* SCOPED, confronti
physical-h0-fixed) su classe A dichiarata. **Parziale**: [T-DISC-3]
(SCHEMA; gamba (b) con premessa (DR) nominata, checked per family a M-RED
time); monitor TRIPLE/D.16 (PRACTICE, SPECIFIED-NOT-ARMED fino a prima
ingestione; gamba licensing SCHEMA G-b1/G-b2); metrica C50 aggiudicata
nella FORMA, istanziazione = duty F2.
**Aperto** (owner/trigger espliciti):

- **U3'** — PREMISE-OPEN, owner **F2a**; trigger = ingresso F2a; il
  contratto di estrazione NON si freeza prima (D6 :191-202, :264-267).
  In termini della regola di interpretazione (guardia 17 / CKP-S2-1,
  §1.2): la premessa SCOPERTA di U3' è la metà gola/superficie-sonica del
  **choking pieno** — l'esistenza, lungo ciclo e azimut, di una superficie
  sonica (anche throatless geometrica) tutta sonica-o-supersonica che
  faccia da gate (identificazione parziale dichiarata: U3' possiede anche
  corrector e monitor eseguibile, D6 :196-201);
  finché U3' non la adjudica (ipotesi + monitor eseguibile + il caso NO =
  patch subsonica con chiusura dichiarata), il decoupling che ogni lettura
  one-way presuppone resta un'ipotesi dichiarata, non un fatto.
- **Contact/slip** — owner **F2a** (default smeared; FITTED-contact =
  estensione F4b) (D6 :176-190).
- **G6 su dataset reale** — il falsificatore di N-K non è mai stato
  esercitato: nessun dataset reale ingerito a oggi (2026-08-23); trigger =
  prima ingestione (F2a in poi). Dichiarazione onesta, non difetto.
- **F2-C50-CONTRACT-METRIC** — istanziazione + costanti numeriche della
  metrica di contratto; armato al PRIMO tra findings :1668 (F2
  freeze/prima famiglia reale) e :2324 (prima ingestione
  unsteady-generator); sequenced con
  `contract:datum-uncertainty-contract-missing`
  (`docs/findings_registry.yaml:1661`) e
  `contract:phase-gauge-jitter-alignment-unpinned`.
- **C52/C53/C54** — agenda del blind-contract diff (card sotto: C52/C53
  finestra F2 contract window; C54 al prossimo touch di M0 D2.4).

### 5.1 DECISION CARD delle scelte presentate (formato §1g, 6 campi)

**CARD C50 — Datum-space metric del contratto di incertezza dati**

1. *Scelta (id ledger)*: **C50** (`docs/choice_ledger.yaml:694`).
2. *Alternative censite (data + fonte survey)*: L1(A) (lente blind-PDE) /
   thrust-calibrated flux-weighted L2 + guardia L∞ (lente blind-data/UQ) /
   split-by-role — censite dai due formalizzatori CIECHI del
   blind-contract diff (2026-08-13, raws S-FOUNDATIONS) ed escalate a
   Form-2 piena il 2026-08-20
   (`validation/sfoundations_raws_2026-08-13/blocco3/VERDICT_C50_form2.md`
   §4); censimento di escalation: Hoffman et al. 1995 [ABS],
   Ben-Tal–Nemirovski / Bertsimas [ABS], Fidkowski-Darmofal 2011 [ABS],
   Métivier OT (chiuso).
3. *Verdetto + perché*: **SINGLE-CONTRACT-METRIC, forma PRODOTTO** — d =
   L1(A) su campi phase-aligned ⊕ fronti dichiarati (posizioni/velocità
   con barre) dentro guardia L∞; acceptance = product-ball membership,
   fuori da W = NO DATUM (rejected, not error-barred); il flux-weighted
   L2 = strumento di sensitività U-slot, NON seconda metrica. Perché: le
   posizioni dei jump non sono mai misurate a precisione TV; la sharpness
   passa per la dualità sul ball certificato.
4. *RECENCY/SOTA check della survey*: escalation datata 2026-08-20 con
   censimento SOTA proprio (Hoffman/Ben-Tal/Fidkowski verificati [ABS]);
   nessun evento successivo noto in-perimetro alla data odierna —
   **ATTUALE(perimetro: blind-contract diff + Form-2 escalation census,
   data-check 2026-08-23)**.
5. *Falsificatore*: FS-1..FS-4 (probe family incl. near-sonic axis;
   rank-correlation; validity-neighborhood stability) + **F-ARCH flip
   pre-registrato**: alla prima famiglia di dati reali, se gli intervalli
   product-form pareggiano una maggioranza di coppie che lo strumento U-a
   separa E la via sampled [min,max] è priced infeasible, la riga si
   riapre verso SPLIT-BY-ROLE come ledger update.
6. *Trigger di ri-esame + finestra*: duty **F2-C50-CONTRACT-METRIC**,
   armato al primo tra findings :1668 / :2324 — **finestra F2**.

**CARD C52 — Status di una signature caratteristica MIXED/phase-crossing
su Gamma_d** (riga NEVER del ledger: card "non-aggiudicata" stampata)

1. *Scelta*: **C52** (`docs/choice_ledger.yaml:716`).
2. *Alternative censite (data + fonte)*: lettura di record (patch
   subsoniche = case-class ammissibile con monitor, O1-O4, downgrade
   documentati) vs lettura blind-PDE (P3) (signature costante o
   INADMISSIBLE outright, sonic set = free boundary) — censite dal
   blind-contract diff, minted 2026-08-19
   (`validation/sfoundations_raws_2026-08-13/VERDICT_contract_and_L4R1.md#D-1`).
3. *Verdetto*: **NON AGGIUDICATA** (status NEVER; mostly mooted dal
   L4-DEFAULT, load-bearing il giorno in cui la case-class subsonica è
   usata).
4. *RECENCY check*: censimento datato 2026-08-19, perimetro =
   blind-contract diff; nessun input nuovo noto alla data —
   **ATTUALE(perimetro: blind-contract diff D-1, data-check 2026-08-23)**.
5. *Falsificatore*: H3-cl atteso FAIL su pattern migranti (K-P Fig. 6) —
   l'esito decide quale lettura governa.
6. *Finestra di ri-esame*: **F2 contract window** (agenda del judge; feeds
   `contract:chi-character-map-unknown-band-missing`).

**CARD C53 — Gamma_d PLACEMENT policy** (riga NEVER: card
"non-aggiudicata" stampata)

1. *Scelta*: **C53** (`docs/choice_ledger.yaml:726`).
2. *Alternative censite (data + fonte)*: blind-DATA (stazione più a MONTE
   con beta = 0, pressione di trasportabilità) vs blind-PDE (banda
   ammissibile [z_I^-, z_I^+], POSSIBLY EMPTY, preferenza a VALLE) — i due
   ciechi in disaccordo GENUINO tra loro; censite 2026-08-19
   (`validation/sfoundations_raws_2026-08-13/VERDICT_contract_and_L4R1.md#D-2`).
3. *Verdetto*: **NON AGGIUDICATA** (status NEVER; il record fissa Gamma_d
   per caso senza registrare il trade).
4. *RECENCY check*: censimento 2026-08-19, perimetro blind-contract diff —
   **ATTUALE(perimetro: blind-contract diff D-2, data-check 2026-08-23)**
5. *Falsificatore*: il verdetto di VUOTEZZA della banda è parte del
   deliverable — banda vuota = la policy a banda muore sul caso.
6. *Finestra di ri-esame*: **F2 contract window** (carrier suggerito dal
   judge: placement-band remark in M0 D2.4). Input harvest disponibile
   per l'aggiudicazione: la tabella interfacce dà il decadimento assiale
   (87.8% pulse damping, S6) = DOVE piazzare l'interfaccia per una
   corrugazione target (`THROAT_FIELD_HARVEST_c4.md:613`).

**CARD C54 — Status normativo del rung I4 (single mean state) nella
scala D2.4** (riga NEVER del ledger: card "non-aggiudicata" stampata;
perimetro CH10: la scala I0-I4 è presentata in §1.1)

1. *Scelta*: **C54** (`docs/choice_ledger.yaml:737`).
2. *Alternative censite (data + fonte)*: blind-DATA Claim 3.4 (BAN del
   mean-datum solve come riduzione — reject-only: errore O(Var) SENZA
   parametro piccolo, controesempio Jensen) vs compatibilizzazione del
   judge (annotazione one-line a I4 in M0 D2.4 col warning O(Var)
   no-small-parameter: I4 resta rung DICHIARATO della scala, mai claim di
   approssimazione) — censite dal blind-contract diff, minted 2026-08-19
   (`validation/sfoundations_raws_2026-08-13/VERDICT_contract_and_L4R1.md#D-4`).
3. *Verdetto*: **NON AGGIUDICATA** (status NEVER; consumption-check
   2026-08-19 NEGATIVO: la riga D2.4 legge ancora "I4 single mean state."
   nuda — l'annotazione non è atterrata, riga OPEN).
4. *RECENCY check*: censimento 2026-08-19, perimetro blind-contract diff,
   con verifica di consumo su M0 eseguita nella stessa finestra —
   **ATTUALE(perimetro: blind-contract diff D-4 + consumption-check M0,
   data-check 2026-08-23)**
5. *Falsificatore*: l'atterraggio dell'annotazione one-line in M0 D2.4
   flippa la riga a DECIDED con l'anchor M0 come evidence (il ledger lo
   pre-registra).
6. *Finestra di ri-esame*: **prossimo touch di M0 D2.4** (owner della
   riga; quando la line atterra, la card si chiude).

---

## 6. STORIA (writer W-B.2, 2026-08-23 — trittico [V2-R2]; ogni battuta
## porta DATA + PROCESSO + VERDETTO, campi di join del retro-audit §5-bis)

### 6.1 D2.4 [D-CONTRACT]: la terna (Gamma_d, data class, validity)

- **Battuta 1 — derivazione originale.** DATA: anteriore al 2026-07-21
  (datazione by-inclusion, dichiarata: il blocco D2.4 non porta data
  propria; l'addendum S12 [D-GSEP] del 2026-07-21 emenda la stessa Parte
  II di M0, `docs/rde_nozzle_MASTER.md:274`, quindi la struttura
  contrattuale gli preesiste). PROCESSO: catena D1→M0 (D2.4,
  `docs/rde_nozzle_MASTER.md:116-124`): interfaccia come superficie
  fissa a valle di ogni rilascio di calore + tre requisiti R1/R2/R3 +
  scala di idealizzazione I0-I4. VERDETTO: il contratto è la risposta di
  record alla domanda-dati, non un formato file.
- **Battuta 2 — (a) RIDERIVATO-PIENO (formalizzazione cieca).** DATA:
  2026-08-17. PROCESSO: contract blind formalization S-FOUNDATIONS
  (brief agnostico; workflow 10/10; judge
  `validation/sfoundations_raws_2026-08-13/VERDICT_contract_and_L4R1.md`).
  VERDETTO: 9 elementi del contratto riderivati ciechi; 3 gap P2 emersi
  = righe F-1/F-2/F-3 (data-class unpinned, audit RH/entropia del datum,
  contratto d'incertezza) — arricchimenti, non smentite (commit 5221529).
- **Battuta 3 — convergenza.** DATA: 2026-08-22/23 (S-PRES). PROCESSO:
  precisione guardia 11 (Gamma_d NON è "the throat", checkpoint
  `validation/spres_raws_2026-08-22/SESSION_STATE_checkpoint.md:158-163`)
  + pin utente 2026-08-23 decoupling⇔choking pieno (guardia 17 /
  CKP-S2-1, §1.2). VERDETTO: classe finale = contratto di record con
  case-class subsonica DICHIARATA e lettura fisica del feedback fissata.

### 6.2 L4-DEFAULT e il margine m_n ≥ delta

- **Battuta 1 — derivazione originale.** DATA: 2026-08-06 (blocco
  [L4-DEFAULT OF RECORD, dated 2026-08-06 (S16, ledger pass 2)],
  `docs/rde_nozzle_MASTER.md:125-138`). PROCESSO: campagna fondazioni
  S15/S16 (ledger dei condizionali p1/p2 + default L4). VERDETTO:
  default certificato con ogni patch assialmente supersonica CON
  margine; H2/H-I2 DISCHARGED sul default per teorema
  ([T-TH0]/[T-NSW]).
- **Battuta 2 — (a) RIDERIVATO-PIENO con cap dichiarato.** DATA:
  2026-08-17. PROCESSO: prova Phase D L4⇒R1
  (`validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md`,
  1529 righe; refutazioni r1/r2; judge VERDICT_contract_and_L4R1.md,
  autorità downgrade-only). VERDETTO: core THEOREM/THEOREM* con confine
  unstart ONESTO (classe M_s>M_x esclusa+monitorata); caveat di record:
  loop refuter cappato a round 2 NOT-DRY, dichiarato nel verdict stesso.
- **Battuta 3 — convergenza.** DATA: 2026-08-17/20 (hypaudit).
  PROCESSO: audit di legittimità delle ipotesi con dual-seed dedicato.
  VERDETTO: [R1-CAUSAL] = **CONDIZIONATA** (l'unico verdetto non-LDM dei
  sei: finestra W1-W4, mu(Xi_sub)>0 generico sui dati reali, monitor
  suite unarmed = live breach di M0 VI.4bis(v), owner F2 —
  `validation/sfoundations_raws_2026-08-13/hypaudit/VERDICT_hypothesis_audit.md:482`);
  classe finale: teorema ESATTO solo su L4, condizionato-monitorato
  fuori.

### 6.3 Stage-A audit + G6 loud-reject

- **Battuta 1 — derivazione originale.** DATA: 2026-08-11 (piano v3,
  finestra S21). PROCESSO: G6 coniato come gate nel piano ("G6 (new)
  DATA-CONTRACT GATE ... rejected loud — no design on inconsistent
  data", `docs/rde_nozzle_development_plan.md:808-810`; tabella gate
  `:290`), con gli audit stage-A specificati (`:174-176`; M0 VI.1
  :3067-3075). VERDETTO: gate dichiarato, operativo da F2a.
- **Battuta 2 — (c) NON-ESERCITATO su dati reali (il NO di G6 non ha
  mai sparato: nessun dataset reale è mai stato ingerito — dichiarato in
  §5); doppia prova alternativa.** DATA: 2026-08-17 (hypaudit
  `confront_contract.md`: bundle [CONTRACT-MU] E1-E5 =
  LEGITTIMA-DICHIARATA-MONITORATA con E3 CONDIZIONATA dentro,
  VERDICT_hypothesis_audit.md:381-385 — "the stage-A audits are work
  the published SOTA never did", commit 5221529) + 2026-08-19
  (estensione del loud-reject set: rejector TRIPLE D.14 +
  angular-momentum D.16, PRACTICE SPECIFIED-NOT-ARMED,
  `docs/rde_nozzle_development_plan.md:811-815`). PROCESSO: audit di
  legittimità + estensione specificata del set. VERDETTO: la legittimità
  del contratto è auditata; l'armamento del gate = evento futuro F2a con
  owner — aperto dichiarato, non difetto taciuto.
- **Battuta 3 — convergenza.** DATA: 2026-08-19 (Annex B). PROCESSO:
  invariante "a generator emitting off-manifold data is a generator
  bug" (`docs/rde_nozzle_development_plan.md:1155-1157`). VERDETTO:
  classe PRACTICE-gate; gli audit valgono ANCHE sui dati generati —
  nessuna asimmetria fidata.

### 6.4 U3' PREMISE-OPEN e contact/slip (i due aperti F2a)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-11. PROCESSO:
  censimento choking (`validation/ADVISORY_rde_choking_2026-08-11.md`,
  5 paper) + addendum S21 eseguito integralmente (commit 1d9609a);
  U3' scritto nel piano (`docs/rde_nozzle_development_plan.md:191-202`,
  ribadito `:264-267`). VERDETTO: "U3 stays PREMISE-OPEN until U3'
  closes; NO freeze of the extraction contract before".
- **Battuta 2 — (c) NON-RIDERIVATO (l'apertura È il contenuto); doppia
  prova alternativa dell'apertura.** DATA: 2026-08-21 (throat harvest
  C4, commit 3b2b9e6: pin esibito ma MAI verificato spettralmente in
  ALCUN CFD pubblicato, search-proven; KP18 Table 1 = unica statistica
  quantitativa di gola; gap G1-G9) + 2026-08-17 (hypaudit: "L4 possibly
  empty on real engines", VERDICT_hypothesis_audit.md:485). PROCESSO:
  harvest a lente dedicata + audit ipotesi. VERDETTO: l'apertura è
  corroborata da due lati indipendenti — genuina, non pigrizia.
- **Battuta 3 — convergenza.** DATA: 2026-08-22/23 (S-PRES, guardia 11).
  PROCESSO: la sonic line corrugata KP18 (M=1 attraversata due
  volte/ciclo) diventa il PERCHÉ fisico del margine e della case-class
  subsonica (§1.2). VERDETTO: owner F2a confermato; contact/slip default
  = smeared-contact dichiarato con opzione FITTED a F4b
  (`docs/rde_nozzle_development_plan.md:176-190`).

### 6.5 Il ledger L4 dei condizionali (eredità BY ID)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-05/06 (S15/S16:
  ledger pass 1 + pass 2 con L4-default; carrier
  `docs/rde_nozzle_conditionals.md:1-16`). PROCESSO: campagna fondazioni
  — i condizionali analitici (C-D25U, C-SBVF) enunciati UNA volta,
  ereditati BY ID da ogni THEOREM*. VERDETTO: ledger di record.
- **Battuta 2 — (b) STANCE-DI-FORK.** DATA: 2026-08-17 (tree diff).
  PROCESSO: 4/4 alberi ciechi atterrano su classi fitted-front
  piecewise-smooth con la scoping Li-Yu/Majda ricostruita e "wild
  non-uniqueness fenced by class fiat, declared openly"
  (`validation/sfoundations_raws_2026-08-13/phaseB_tree_diff.md:330-335`)
  — il verdetto per-riga del diff è dichiarato come stance, non come
  prova. VERDETTO: l'architettura condizionale-dichiarato è raggiunta
  indipendentemente dai fork; la sostanza analitica dei singoli
  condizionali resta quella del ledger.
- **Battuta 3 — convergenza.** DATA: 2026-08-06 (C-MAJDA affilata a
  U3-H1, S16) e separazione di natura nel claims registry (analitici vs
  "model closures and numeric residuals, NOT analytic gaps",
  `docs/rde_nozzle_conditionals.md:7-9`). PROCESSO: consolidamento.
  VERDETTO: classe finale = ledger con due nature SEPARATE; ogni Verdict
  a valle stampa i condizionali ereditati — mai ipotesi silenziose.

---

## 7. POSIZIONAMENTO / CONFORMITY

**(a) STRUMENTI** (terna mondo-SOTA / cosa usiamo / perché):

| strumento del nodo | mondo-SOTA (id registry) | cosa usiamo / perché |
|---|---|---|
| front-extraction dall'input CFD | lignaggi "Gelb-Tadmor" (concentration-based detection) e "Paciorri-Bonfiglioli" (fitted-front) nominati in D6 :256-263 — **ECCEZIONE NON-REGISTRY DICHIARATA** (0 righe registry, decisione A4 emendamento §6b); vicino esistente: `wanted_onofri_paciorri_2017_book` | operatore proprio: detection + ricostruzione RH-consistent + proiezione exact-RH con banda residua DERIVATA + LOUD REJECT + KAT smear-extract-compare come oracolo proprio — perché il contratto deve poter RIGETTARE, non solo interpolare |
| ammissione dati | pratica del campo = imposed-BC senza audit (LL-6/LL-24) | stage-A (Crocco, completeness, H-I2) + G6 + TRIPLE/D.16 + T0 flatness con soglia DERIVATA — perché "no design on inconsistent data" (D6 :808-810) |
| metrica del datum | UQ/robust classi Ben-Tal–Nemirovski / Bertsimas; distortion decomposition Hoffman 1995 (censimento C50 [ABS], dedup registry owed) | product-form C50 di record (card §5.1) — acceptance ≠ sensitivity, ruoli separati per costruzione |
| recovery di stato da tabelle | precedenti tabulated-EOS MoC (LL-32: `johnson_boney`/`scofield_hoffman` — riga ledger P3.8) | recovery UNICO sotto AUD-cp/AUD-c2T (THEOREM) + flag-never-extrapolate — perché l'esistenza fuori-range è un rigetto, non un extrapolation warning |

**(b) SENSO**: il gap che il nodo occupa — il campo consegna CFD (o impone
BC analitici p-only), mai un contratto-dati con classe, audit e rigetto
(K-iii, ancora CH5 §1.1; query-bounded lì). Il precedente diretto è la
linea imposed-BC (§2a, §3-bis): la nostra posizione non è "loro
sbagliano", è "loro impongono la proiezione che il nostro teorema convice,
e il contratto staged è la riparazione" — correzione con teorema, non
opinione (guardia di stile: parte-da-record e parte-aperta separate; la
parte aperta è U3'/C52/C53, dichiarata in §5).

**(c) STANDARD DI RIFERIMENTO**: asse **§C-5 (Dati e claim, classe
FAIR)** della conformity map (design v2 §C :281): il contratto-dati è
l'istanza più letterale del criterio — Findable/Interoperable (campi
tipizzati D.13, provenance obbligatoria nel tuple), Reusable (nessun
numero senza generatore + audit + classe), con la divergenza dichiarata
della mappa (FAIR per repo chiuso: accessibile a ente e team, non
open-data). Asse secondario **§C-3 (tracciabilità ECSS/DO-178C-class)**
(:279): i campi del contratto sono requirement machine-checkable (gli
audit stage-A sono i trace-lint del dato). Criterio di conformità:
l'ingestione di un dataset esterno produce un Verdict con eredità di
condizionali stampata; divergenza: nessuna certificazione DI standard,
classe di disciplina adottata query-bounded.

---

## 8. DOMANDE DA PANEL (risposte ancorate)

**Q1 (ESA, LA domanda attesa): "Che input vi serve da noi?"** — La
risposta di record è la Annex B input taxonomy (D6 :1132-1157): al minimo
le SPECS (caso A: propellente, φ, pressione media, geometria annulus, Pa)
— il tool è fully predictive a quel rung (stage P34: prediction); ogni
dato in più (waveform, tracce di pressione, spinta, f, n; profilo di
missione; envelope; incertezze) sale la scala casi B-G con classe di
rigore dichiarata e macchina a valle IDENTICA. Non serve il vostro CFD;
se c'è, entra dalla pipeline CFD-to-contract (D6 :256-263) e viene
AUDITATO come tutto il resto.

**Q2: "Perché non chiedete semplicemente le condizioni alla gola?"** —
Perché Gamma_d NON è "the throat" (guardia 11): è la stazione
axially-supersonic-with-margin a valle del rilascio di calore (m_n ≥
delta, L4-DEFAULT); la sonic line è corrugata (KP18: M=1 attraversata due
volte per ciclo, harvest :399-406) — "la gola" attraversa la degenerazione
parabolica due volte per ciclo e non può portare il full-state.

**Q3: "E se i dati hanno patch subsoniche?"** — Case-class DICHIARATA, mai
mediata in silenzio: O1-O4 (D1 §4.3bis :302-321) con H2/H-I2 come class
assumptions, monitor e downgrade di Verdict documentati; lo status
contrattuale di una signature migrante è la card C52 (non-aggiudicata,
finestra F2, stampata sopra).

**Q4: "Come sapete che il dataset è buono?"** — Non lo assumiamo: stage-A
(Crocco, completeness, H-I2) + T0 flatness a soglia derivata + TRIPLE/D.16
+ recovery theorem con flag-never-extrapolate; il fallimento = G6
loud-reject (D6 :808-810). Il gate vale anche per i dati GENERATI da noi
(invariante Annex B).

**Q5: "Harroun/Paxson fanno girare l'ugello con un BC imposto da anni: che
cosa aggiungete?"** — Il loro BC è p-only: esattamente la proiezione
pi di [T-DISC] D1.2 (M0 :1004-1008). Dentro la classe A: [T-DISC-1]
(THEOREM*) + [T-DISC-2] sign leg (THEOREM* SCOPED) danno fibre
non-degeneri e J-separazione — due dataset con la stessa traccia di
pressione e le stesse medie di ciclo ma contenuto di fluttuazione/swirl
diverso hanno J diversi, dove il confronto physical-h0-fixed è
ammissibile; la conseguenza sugli OTTIMI è [T-DISC-3](b) (SCHEMA, con la
premessa (DR) nominata). Il contratto staged full-state (D.13) è la
riparazione theorem-driven, e la loro linea è il nostro antenato
DICHIARATO (LL-6/LL-24, §3-bis) — con citazione piena e caveat CT-6 sui
loro numeri (30 → ~2-6 atm per settore, 13.8 kHz: numeri di
`harroun_2021`, harvest :608, non riprodotti da noi).

**Q6: "Quando freezate il contratto d'estrazione?"** — Non prima di U3'
(owner F2a): la regola U3 presuppone una superficie per-fase supersonica
il cui trasferimento all'RDE non è stabilito; PREMISE-OPEN di record, "NO
freeze of the extraction contract before" (D6 :191-202). Dichiararlo È la
risposta: un contratto freezato oggi sarebbe un claim non coperto.

**Q7: "L'ugello retro-agisce sulla camera? Potete davvero progettare a
valle senza chiudere il loop?"** — Regola di interpretazione di record
(guardia 17 / CKP-S2-1; pin utente verbatim: *"ci dovrebbe essere solo se
la porzione pre gola è convergente e con gola tutta sonica o supersonica,
o se la gola, anche throatless geometrica, è a patch subsoniche"*): il
decoupling è asseribile SOLO sotto choking pieno — pre-gola convergente +
gola/superficie sonica (anche throatless geometrica) tutta
sonica-o-supersonica lungo ciclo e azimut; con patch subsoniche il
feedback C'È, e le patch sono i canali di risalita. Il contratto rende la
regola OPERATIVA: m_n ≥ delta su Gamma_d è la verifica del choking
(L4-DEFAULT, [T-NSW]), e la sonic line corrugata (KP18, C-1bis) dice che
la verifica va fatta lungo il ciclo e l'azimut, non a un istante; le patch
subsoniche sono la case-class O1-O4 con H2/H-I2 come class assumptions —
mai un decoupling assunto in silenzio. La linea imposed-BC del campo
(§3-bis) presuppone questo decoupling senza mai citarne la condizione;
regime forte-transiente (unstart) = fuori dalla lettura a piccole
perturbazioni, confine dichiarato se toccato.

---

## DECK FEED

Asserzioni candidate-slide (assertion-evidence: frase piena + ancora +
classe):

1. **"Per progettare l'ugello del VOSTRO motore ci bastano le specs — ogni
   dato in più sale una scala dichiarata di rigore."** — Annex B casi A-G,
   `docs/rde_nozzle_development_plan.md:1132-1157`. Classe: contratto di
   record; stage P34 = prediction (dichiarato on-slide). [LA risposta alla
   domanda ESA "che input vi serve" — il feed più prezioso.]
2. **"Il dato non entra: viene AMMESSO — e il gate sa dire no."** — G6
   DATA-CONTRACT GATE, stage-A (Crocco, completeness, H-I2), loud-reject:
   `docs/rde_nozzle_development_plan.md:808-810`; falsificatore vivo di
   N-K (mai esercitato su dataset reale: dichiarazione onesta §5). Classe:
   gate di record.
3. **"L'interfaccia NON è la gola: è la stazione supersonica-con-margine a
   valle del rilascio di calore."** — D2.4 + L4-DEFAULT m_n ≥ delta,
   `docs/rde_nozzle_MASTER.md:116-138`; guardia 11. Classe: THEOREM
   (T-TH0/T-NSW sul default).
4. **"La sonic line di un RDE è corrugata — attraversa M=1 due volte per
   ciclo: ecco perché il margine esiste."** — KP18 Fig. 6
   (`kaemming_paxson_2018`), `THROAT_FIELD_HARVEST_c4.md:399-406`; patch
   subsoniche = case-class dichiarata O1-O4
   (`docs/rde_nozzle_problem_book.md:302-321`). Classe: [IO] harvest +
   record D1; CT-6 sui numeri altrui.
5. **"Il campo impone BC p-only; i nostri teoremi dimostrano che quella
   proiezione perde informazione di spinta — il contratto full-state È la
   riparazione."** — Harroun Eq.7 p-only (`harroun_2021`, harvest :608,
   :763) vs [T-DISC] D1.2 + T-DISC-1/2/3 (`docs/rde_nozzle_MASTER.md:
   1004-1008, 1030, 1086, 1184`); lineage LL-6/LL-24 (§3-bis). Classe:
   per gamba — T-DISC-1 THEOREM*, T-DISC-2 split-grade (sign leg THEOREM*
   SCOPED), conseguenza-ottimi T-DISC-3(b) SCHEMA con premessa (DR);
   scope classe A dichiarato (mai "THEOREM" secco on-slide).
6. **"Nessuno dei quattro paper di riferimento dichiara una classe di
   dati; la periodicità è esibita nei CFD, mai verificata
   spettralmente."** — CH5 §1.1 + `THROAT_FIELD_HARVEST_c4.md:571-573,
   687`. Classe: [ADV]/[IO], query-bounded via CH5.
7. **"Il contratto non è freezato — e lo diciamo: U3' (choking RDE) è
   PREMISE-OPEN, owner F2a."** — `docs/rde_nozzle_development_plan.md:
   191-202`. Classe: aperto dichiarato (honesty-first, materiale ask CH6
   §1.6).
8. **"Anche l'incertezza del dato ha un contratto: metrica prodotto
   aggiudicata, flip alternativo pre-registrato."** — C50 di record
   (VERDICT_C50_form2 §4; card §5.1 con F-ARCH). Classe: aggiudicazione
   Form-2 di record; istanziazione = duty F2 dichiarato.
