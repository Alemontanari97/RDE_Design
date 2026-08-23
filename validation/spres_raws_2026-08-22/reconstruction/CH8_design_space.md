# CH8 — Lo spazio di design: configurazioni come output, settori, torneo

Status: capitolo di RICOSTRUZIONE S-PRES (2026-08-22/23). Non aggiudica nulla:
ancora al record (problem book §5, claims registry, census advisory, pipeline
map, driver brick-2) e dichiara gli aperti.
Consumo dichiarato: storyboard v3 deck ESA, banca Q&A red-team, mappa F2+.
Domanda utente generatrice: "come emerge un profilo ottimo? appartiene a una
categoria precisa (bell, shrouded plug, spike, expansion-deflection) o lo
spazio di ottimizzazione e' designed per muoversi in tutto cio'?"

Nota di identificazione (dovere di precisione): il teorema del torneo che il
brief di questo capitolo chiama "T-GRP10" ha registry id **[T-OP11e]**
(`docs/claims_registry.yaml:368-379`); X-GRP10/X-GRP12 sono i suoi **carrier**
(`docs/claims_registry.yaml:949-961`, `:977-989`), non l'id del claim.

---

## 1. Ricostruzione

### 1.1 La formulazione configuration-free: la variabile di design e' un insieme

Il record NON parte da una categoria di ugello. La formulazione generale
(`docs/rde_nozzle_problem_book.md:337-353`) dichiara: la variabile di design e'
il **SOLID SET S** dentro un envelope E (cilindro di lunghezza L, raggio R_max a
valle dell'annulus), con vincoli di attacco ai lip della camera e una condizione
di cono uniforme/regolarita'; il dominio fluido e' E∖S. La frase chiave e'
testuale: *"Configurations are the TOPOLOGY CLASSES of S — outputs of the
optimization, not inputs"* (`docs/rde_nozzle_problem_book.md:343-344`).

I settori elencati nella formulazione (`docs/rde_nozzle_problem_book.md:345-353`):

- **(i) BELL**: solido solo sul contorno esterno; Σ = grafo y_w ∈ C^{1,1} con
  y_w(0) = y_lip; il **dual-bell e' lo STESSO settore** (parete con kink)
  (`:345-346`).
- **(ii) PLUG (aerospike)**: solo center body — configurazione **free-boundary**;
  lunghezza di troncamento L_p e chiusura di base-pressure p_b **dichiarate
  (slot N2)** (`:347-348`).
- **(iii) SHROUDED PLUG (classe Veen)**: entrambi; causalmente separabile
  F = F_shroud + F_plug + F_kernel (dottrina GENO-Veen) (`:349-350`).
- **(iv) ulteriori settori in A_gen**: expansion-deflection (center body a valle
  del piano di uscita), multi-componente/clustered, non-axisymmetric (prezzo
  via P5) (`:351-353`).

### 1.2 La decomposizione in settori e il torneo (SCHEMA, non teorema)

La struttura logica (`docs/rde_nozzle_problem_book.md:354-363`): la condizione
di cono uniforme vieta componenti degeneranti (niente aghi/lamine), quindi
A_gen si spezza in **FINITAMENTE molti settori topologici**; esistenza
per-settore via compattezza di Chenais + continuita' S1 (P7); **l'ottimo TOTALE
su A_gen = vincitore di un torneo finito di ottimi per-settore** (basta la
semicontinuita' superiore attraverso le degenerazioni di settore). Il confronto
cross-settore e' licenziato dai vincoli condivisi e dal bound geometry-free
(D3 §10quater) (`:359-360`).

Due caveat scritti nel record, da NON ammorbidire:

1. La decomposizione e' etichettata **SCHEMA** nel problem book (`:354`), e M0
   dichiara esplicitamente che *"'FINITE' here carries NO declared rigor class
   at this site of record"* — le basi attuali sono lo SCHEMA del problem book +
   il counting theorem del census advisory (THEOREM-sketch, condizionale);
   classe e prova sono DOVUTE alla census-lemma session
   (`docs/rde_nozzle_MASTER.md:313-320`).
2. **CAUTION topological-derivative** (`docs/rde_nozzle_problem_book.md:361-363`):
   l'esplorazione via derivata topologica e' inaffidabile qui — un corpo
   infinitesimo in corrente supersonica produce solo wave drag; il center body
   paga solo a taglia finita. **Si confrontano settori interi**, non germi.

La working class A (`docs/rde_nozzle_problem_book.md:365-368`): varieta' spline
finito-dimensionali dentro le classi C^{1,1}/cono uniformi per settore
(esistenza banale, P7 da' la versione function-class); l'assialsimmetria e' una
**ASSUNZIONE dichiarata, licenziata perturbativamente da P5** (tricotomia di
simmetria), *"not by habit"*.

### 1.3 Il census topologico: la tassonomia classica collassa (ADVISORY)

Il panel census (`validation/PANEL_topology_census_2026-07-22.md`, 5-lens panel
+ 8-lens attack wave + 3-referee, 233/233 verdetti mappati — **con il caveat
del header: il criterio di convergenza formale (unanimous clean 3-critic
panel) NON fu raggiunto prima del troncamento infrastruttura** (`:11-13`);
**ADVISORY, in attesa di ratifica utente**, `:1-17`) raffina la mappa dei
settori. Headline (`:55-74`, THEOREM-sketch condizionale sui pin): bell, spike
(pieno e troncato), shrouded plug, Migdal annulare, expansion-deflection e il
bare annulus sono **tutti STRATI di UN solo settore clopen S0** (connessione
di S0 congetturale — vedi sotto); gli unici salti genuinamente discreti sono
l'aggiunta di componenti DETACHED (famiglia D(m,n)); i settori P(h)/BR sono
**vuoti per L1 + sealing A1 nell'advisory** (riga DELETED, `:170`) — con L1
CONDIZIONALE su CEN-O10 (`:102`): CEN-O10 e' PINNATO NONBLOCK+ ma la
derivazione pin→lemma e' un target S15 dichiarato (`:359-364`), e tutto resta
advisory (memoria `topology-census-pins`). Correzione Migdal **dichiarata
nell'advisory** (tag [DECLARED], Round 2, `:40-53`): "quale parete termina
prima" NON e' un invariante; la coordinata di regime corretta e' il
**lip fan opening** Δν_lip ≥ 0.

I **pin utente 2026-08-02** sono registrati nel census §7pin
(`validation/PANEL_topology_census_2026-07-22.md:329-384`):
cono uniforme sul lato FLUIDO Ω = E∖S (ipotesi di Chenais propria; tip
tangenti, trailing edge sharp, pareti sottili IN classe; gap sub-scala OUT;
barriere di contatto UNCONDITIONAL) (`:333-344`); CEN-O1 = PERMISSIVA (bare
annulus incluso; membri detached via anchor class/strut band/filtro torneo)
(`:345-352`); CEN-O10 = NONBLOCK+ (`:359-364`); CEN-O11 = Λ = i due CERCHI di
lip, attacco C0 a pendenza libera, one-attached-per-lip diventa teorema
(`:365-370`); garanzia di generalita' verificata: nessuna geometria fisica
rimossa dai pin (`:371-377`). Dove sono ATTERRATI: in M0 come **state-pointer
notes** (`docs/rde_nozzle_MASTER.md:306-312` e `:321-327`), che dichiarano
esplicitamente che gli emendamenti D2.1/D2.6 implicati dai pin sono **QUEUED**
alla census-lemma rigor session — la sessione NON e' ancora stata eseguita
(schedulata F2-exit, `docs/rde_nozzle_PROGRESS_ARCHIVE.md:413`); residuo
analitico dichiarato: CEN-O4 (hub connectedness) + CEN-O5 (continuita' del
valore alle facce) (`PANEL_topology_census_2026-07-22.md:378-384`).

Conseguenza per la domanda utente: nella lettura census (advisory), il "passare
da bell a spike" e' un passaggio tra **strati di UN solo settore clopen S0 —
ma la connessione di S0 e' CONGETTURALE**: l'advisory stesso scrive
*"conjecturally connected (hub argument owed, CEN-O4)"*
(`PANEL_topology_census_2026-07-22.md:68-69`) e CEN-O4 e' nel residuo
analitico dichiarato dei pin (`:378-379`); solo singoli confini di strato
(es. r_b → 0 sotto CEN-O2) hanno continuita' argomentata (`:60-62`). Il
torneo discreto residuo e' contro la famiglia detached. Nella lettura
of-record (problem book, SCHEMA) resta il torneo finito per settori. Le due
letture sono compatibili: il census RIDUCE il numero di partite del torneo,
non lo elimina.

### 1.4 Il torneo gia' giocato: i teoremi al rung delle chiusure

Tre risultati di registro giocano oggi il torneo, tutti al **rung eps/0-D
(chiusure certificate), non al livello shape-PDE**:

- **[T-OP11e]** (THEOREM, EOS-general, `docs/claims_registry.yaml:368-379`):
  sotto la chiusura sonic-capped **la famiglia plug domina debolmente la bell
  puntualmente**, raggiunge il ceiling capped per eps_max ≥ knee su ogni ciclo
  Pa > 0 incluso il subcritico, con **tie region caratterizzata** e il device
  di torneo **premium_bound certificato per cella**. Scope vincolante
  (`:371`): i winner rankano **CHIUSURE a pari eps_max, mai hardware**
  (semantica D3 §10quater(5)). Carrier: X-GRP10 (22 check + 8 controlli
  negativi, `tests/test_phase_diagram.py`, `:949-961`) e X-GRP12 (20/20,
  route reale + equilibrium bracket, `tests/test_phase_diagram_real.py`,
  `:977-989`).
- **[T-T4]** (THEOREM*, `docs/claims_registry.yaml:329-340`): per il plug
  free-boundary sotto la chiusura ideal-adaptation sonic-capped dichiarata, gli
  argmax per-fase sull'estensione del plug sono **half-line annidate**, quindi
  max∫ = ∫max e' raggiunto dal design **PEAK-phase NON troncato**;
  troncamento/length cap **rompono l'annidamento e aprono il primo problema di
  forma genuinamente mediato (PB-2)**. Falsificatore armato: macchina
  ideal-plug che non restituisce il peak design, o cella capped dove
  l'estensione perde strettamente (`:339`).
- **[T-P7S1]** (THEOREM*, `docs/claims_registry.yaml:589-600`): esistenza
  dell'argmax di J su ogni **level set margin-certified** A_h^δ(c) (classe
  spline finito-dimensionale **per settore topologico**, compattezza + margini
  chiusi + continuita') — e' il pezzo "esistenza per-settore" del torneo.
  Residuo dichiarato R-P7.2: argmax certificato vs sup non certificato
  (`:592`).

### 1.5 Lo stato del driver discreto: cosa esercita OGGI il codice

Il driver variazionale brick-2 di record e' `validation/a1_toc_variational_jax.py`
([X-TOCV], `:1-9`). Vettore di design (`:11-20`):
**W = [theta_B, y_1, ..., y_m]** — angolo di attacco sull'arco di gola + m
altezze di parete (**heights-as-dofs**, M_NODES = 8, `:108`) su nodi uniformi;
parete = **spline cubica naturale con estremo sinistro clamped** (y_B, tan
theta_B); il nodo di lip y_m porta il vincolo di uguaglianza eps (lineare in W,
riga LinearConstraint `:1360`, `:1748`); L fissata per costruzione; monitor di
lip/classe dichiarati, non vincoli attivi. Ottimizzatore: SciPy trust-constr,
TR-Newton segmentato a curvatura misurata (pipeline map stage 6, C31,
`docs/rde_nozzle_pipeline_decision_map.md:136`; memoria `s18-brick2-closed`).

**Dichiarazione onesta del delta formulazione↔codice**: il driver esercita
**UN solo settore — il bell/TOC** (parete esterna singola come grafo, arco di
gola + contour fino al lip, sweep interno fino all'asse, configurazione TOC
GENO-comparabile, `:2-9`, `:22-39`), assialsimmetrico, **a topologia fissata**
(la stessa docstring: *"dJ/dtheta_B exact at fixed topology"*, `:33`). La
rappresentazione che l'ottimizzatore cammina e' il cluster C1-C8 dello stage 6
della pipeline map (`docs/rde_nozzle_pipeline_decision_map.md:154-159`,
placement note `:161-162`): C1 = cubica interpolante clamped/natural
heights-as-dofs con **migrazione convergiuta verso una chart B-spline
control-polygon dello STESSO spazio spline certificato** (aperta,
F2-C1-CONTROL-CHART-MIGRATION, `:154`); C2/C3 = BC destro naturale/sinistro
clamped (`:155-156`); C7 = ratchet insertion-only dei dof (`:158`). Nessun
settore free-boundary (plug, E-D) ha oggi un driver: la generalita'
configuration-free vive nella formulazione e nel torneo alle chiusure, non
ancora nell'engine discreto.

### 1.6 Cosa manca per i settori free-boundary: H20 e C61

Due nodi della pipeline map (stage 8) bloccano l'esercizio dei settori (ii)-(iv):

- **H20 — free plume boundary p = Pa, meccanica di SOLVE MANCANTE**
  (`docs/rde_nozzle_pipeline_decision_map.md:183`; findings
  `plume:free-boundary-solve-mechanics-missing`,
  `docs/findings_registry.yaml:2519` — la mappa lo cita come ":2521 ordinal";
  1 di 2 gap genuini FORK-141): *"no home in the record; plug/E-D sectors REQUIRE the
  solve + shape-adjoint term"*. Distinto per dichiarazione dalla sola
  stabilita' (findings :1607) e dal modello di chiusura (C61). Finestra:
  F4b external-expansion.
- **C61 — chiusura base-pressure p_b: stato NEVER** (mai adottata dal
  programma) (`docs/rde_nozzle_pipeline_decision_map.md:184`): la Veen
  0.846p/M^1.3 e' praticata solo nella catena LEGACY ed e' **WG10-FAILED**
  (exhibit Humphreys 1971); il p_b di programma e' lo **SLOT DICHIARATO N2**
  (`docs/rde_nozzle_problem_book.md:347-348`), con il verdetto "MUST REPLACE
  IT" e il bracket empirico WG10 come alternativa nel campo alternatives.
  La conditional proposta C-N2 va coniata al kickoff PB-2/OP-2
  (`docs/claims_registry.yaml:181`).

Il legame e' esplicitato dall'edge E12 della mappa (`:218`): C61 = scelta del
MODELLO di chiusura, H20 = la MECCANICA di solve adiacente — due mancanze
distinte, entrambe necessarie per un plug troncato vero. A cio' si aggiunge
CEN-O8 (floor di validita' r_b) che entra nel vettore dei vincoli quando la
chiusura p_b lo richiede (`PANEL_topology_census_2026-07-22.md:382-384`).

### 1.7 Il contratto di globalita' M1-M5: ogni ottimo consegnato dichiara il suo meccanismo (riga G) [W-B.1/B6]

Sorgente unica: **M0 Parte IV — THE GLOBAL-OPTIMALITY CONTRACT**
(`docs/rde_nozzle_MASTER.md:2982-3005`, verificata alla riga in-window
2026-08-23). Il punto di partenza e' un'esclusione per teorema:
*"'Without hypotheses' is excluded by theorem"* — (i) senza classe
ammissibile nessun massimizzatore esiste (Isp strettamente crescente in
eps: vuoto); (ii) senza solution concept J e' indefinito; (iii) senza
misura la media e' indefinita. *"HYPOTHESES ARE THE PROBLEM'S
DEFINITION; the ledger instruments every one"* (`:2984-2988`). Il
contratto per ogni Sigma* consegnato: **EXISTENCE** (P7: compattezza di
Chenais + continuita' S1 uniforme in xi + convergenza dominata) +
**NECESSARY** (T7 con (**')) + **SECOND-ORDER** (reduced-Hessian) +
**GLOBALITY per meccanismo DICHIARATO** (`:2989-2993`).

I cinque meccanismi, con le istanze di record:

- **M1 — duality-gap zero contro la bound ladder** (J_ideal, Int-max,
  integral-flux) → certified global. Istanza di record: **[T-T4]** — il
  testo M0 e' esplicito, *"T4 is an instance"* (`:2994-2995`;
  [T-T4] THEOREM*, `docs/claims_registry.yaml:329-340`). E' il
  meccanismo con cui il torneo di §1.4 e' gia' stato giocato.
- **M2 — collapse transfer**: l'uguaglianza puntuale di **[T-T3]**
  (THEOREM, `docs/claims_registry.yaml:277-289`) eredita la globalita'
  classica del design al valore medio (`:2996-2997`).
- **M3 — struttura monotona/unimodale** (`:2998-2999`). Le istanze di
  record sono i teoremi del repo al **rung "oracolo quasi-1D" = oracolo
  SENZA contouring (solo eps)** — naming C-2 di record: mai "il caso
  ugello 1-DOF"; il rung fissa QUALE media entra nella condizione di
  adattamento, il contouring vincolato non c'entra (il verbatim M0
  *"repo 1-DOF theorems are instances"* va letto con questo naming).
  **Target dichiarato nel contratto**: *"unimodality of the
  truncated-plug duty variable"* (`:2999`) — cioe' esattamente PB-2.
- **M4 — enumerazione esaustiva dei punti stazionari (deflated
  continuation) + bound gap, finito-dimensionale** (`:3000-3001`).
  Posizionamento mondo (forma emendata, decisione A4 di record,
  `SESSION2_LOG.md:87-88`): la deflated continuation HA la sua riga
  registry citabile — `wanted_farrell_birkisson_funke_2015` (Farrell,
  Birkisson & Funke, SISC 2015, deflation techniques;
  `docs/literature_registry.yaml:1196-1200`, status WANTED, census
  identity PANEL_C2021.md §2.3/§4.6, asse B deflation/branch-switching)
  — identita' censita, NESSUN claim di lettura. Il quadro LOCALE
  dell'engine cita `nocedal_wright_2006_2ed`
  (`docs/literature_registry.yaml:980-987`, READ-PARTIAL: SR1 §6.2 +
  modello d'errore FD §8.1) — SOLO per il locale, mai come carrier
  degli oggetti globali.
- **M5 — certified deterministic global search
  (Lipschitz/branch-and-bound) a 2-4 DOF** (`:3002-3003`).
  Posizionamento mondo: **NOT-FOUND(q)** — query eseguita in-window
  2026-08-23: `grep -i "Lipschitz|branch.and.bound|DIRECT"` su
  `docs/literature_registry.yaml` → nessuna riga registry per solver
  Lipschitz-global/branch-and-bound (i match esistenti riguardano
  "direct characteristic equations" e "direct method" nel senso
  Allman-Hoffman, non global search deterministico). Upgrade a
  confronto pieno solo se l'orchestratore minta righe WANTED (A4).

**G-iii — il campo, alla query (search-proven, perimetro chiuso;
forma riparata WB1-C3-16).**
Claim: *nessun paper P-A..P-D dichiara un meccanismo di globalita'*.
Comando ESATTO, riproducibile dalla radice repo (ri-eseguito in-window
2026-08-23, dopo la riesecuzione del refuter C3):

```
grep -niE 'global optim|globality|global search|branch.and.bound|Lipschitz|deflat|multi-?start|globally optimal|global maximum|global minimum' \
  validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pA_liu_wang_2022.md \
  validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pB_li_xu_2023.md \
  validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pC_li_xu_2025.md \
  validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pD_jourdaine_2019.md \
  docs/rde_nozzle_literature_map.md docs/literature_registry.yaml
```

**Esito VERO**: 0 hit sui quattro study file (0/0/0/0; esistenza del
perimetro provata per glob), 0 hit sul litmap, **2 hit sul registry** —
squalificati uno per uno:

- `docs/literature_registry.yaml:1197` (match su "deflation
  techniques", campo identity) e `:1200` (match su
  "deflation/branch-switching axis B", campo owner): entrambe le righe
  appartengono all'UNICA entry `wanted_farrell_birkisson_funke_2015` —
  cioe' la riga WANTED censita DA NOI (status WANTED, identita' a
  livello abstract, nessun claim di lettura), la stessa che §1.7 M4
  cita come posizionamento-mondo. NON e' un paper del campo P-A..P-D e
  NON dichiara un meccanismo di globalita' di alcun design consegnato:
  e' il nostro censimento dello strumento M4. Non qualifica contro il
  claim.

Il claim quindi SOPRAVVIVE nella forma esatta: nessuno dei quattro
paper di campagna (glossario `docs/glossary.yaml:1523-1527`: P-A
Liu-Cheng-Zhang-Wang 2022 (PKU), P-B Li-Xu 2023 (NUAA), P-C Li-Xu 2025
(NUAA), P-D Jourdaine et al. 2019) dichiara esistenza, meccanismo o
forza di globalita'; gli unici hit del perimetro sono le nostre righe
censite, dichiarate come tali. Perimetro CHIUSO: registry + litmap +
P-A..P-D; STOP — nessuna estensione oltre il perimetro dichiarato.
[Riga candidata a registro, nella forma corretta qui sopra:
MINT-PENDING F-2.]

**G-iv — la proposta del programma**: *"Every Verdict states its
mechanism and strength"* — con le tre forze canoniche verbatim:
*"global"*, *"within delta of global, certified"*, *"local + enumerated
competitors"* (`:3004-3005`). Questo e' il deliverable di riga G: non
"abbiamo l'ottimo", ma "ogni Verdict dichiara con quale meccanismo e a
che forza".

**G-v — lo stato onesto di oggi**: il tier di esplorazione globale
dell'engine e' **C57 = NEVER** (mai aggiudicato; local-only da
continuation/warm start; `docs/rde_nozzle_pipeline_decision_map.md:138`;
gia' dichiarato in CH4 Q2: i certificati attestano stazionarieta' KKT
locale con trasversalita', NON ottimalita' globale) — card stampata in
§7. Il target M3 (unimodalita' della duty variable del truncated plug)
e' il ponte dichiarato tra il contratto e PB-2 — e il PERCHE' e'
gia' nel record come exhibit di sensibilita' d'argmax: Humphreys-
Thompson-Hoffman 1971 (AIAA J 9(8):1586-1587), scambiando la chiusura
p_b Eq.(12)→Eq.(38) l'altezza di base ottima si muove **×2.45**
(0.954→2.34 in) e la pendenza di tip −13.26°→−3.08° con spinta
+0.26% — **l'argmax nelle design variables a vincoli fissi
(troncamento/base, il problema PB-2) si muove a O(1) mentre il VALORE
resta quasi piatto** (`docs/rde_nozzle_MASTER.md:1455-1464`,
[ORCH-HARV-3], [ADV]; numeri altrui: citazione piena, non riprodotti —
CT-6). Da qui **la guardia di questa sezione (guardia 8)**:
piattezza di valore NON certifica l'argmax, quindi **i numeri di
campagna si presentano SEMPRE come best-of-sweep certificato, MAI come
ottimo globale senza il meccanismo M1-M5 dichiarato**. Best-of-sweep ≠
argmax: e' la riga da avere pronta prima che la chieda il panel.

---

## 2. Stato per-claim

| Claim | Classe | Ancora | Carrier / falsificatore |
|---|---|---|---|
| Configurazioni = classi topologiche di S, OUTPUT non input | Formulazione di record (Def.) | `docs/rde_nozzle_problem_book.md:339-344` | — (definizione; il falsificatore vive nei teoremi a valle) |
| Settori (i) bell (dual-bell stesso settore), (ii) plug free-boundary (L_p, p_b/N2), (iii) shrouded plug Veen F=F_shroud+F_plug+F_kernel, (iv) A_gen: E-D/clustered/non-axisym via P5 | Formulazione di record | `docs/rde_nozzle_problem_book.md:345-353` | — |
| Decomposizione in settori finiti + torneo finito degli ottimi per-settore | **SCHEMA** (rigor class di "FINITE" dichiaratamente NON assegnata; prova dovuta alla census-lemma session) | `docs/rde_nozzle_problem_book.md:354-363`; `docs/rde_nozzle_MASTER.md:313-320` | falsificatore implicito: un settore non-Chenais-compatto o una degenerazione senza semicontinuita' |
| CAUTION: derivata topologica inaffidabile, confronto per settori interi | Posizione dichiarata (PRACTICE) | `docs/rde_nozzle_problem_book.md:361-363` | — |
| Collasso a UN settore clopen S0 (connessione CONGETTURALE, hub argument dovuto CEN-O4, `:68-69`) + famiglia D(m,n); P(h)/BR vuoti per L1+A1 (riga DELETED `:170`; L1 condizionale su CEN-O10 `:102`, pin→lemma dovuto S15 `:359-364`) | THEOREM-sketch, **ADVISORY non ratificato** (convergenza formale del panel NON raggiunta, `:11-13`) | `validation/PANEL_topology_census_2026-07-22.md:55-74`; `docs/rde_nozzle_MASTER.md:321-327` | due strati S0 non connettibili da cammino continuo in-class (`:73-74`) |
| Pin utente 2026-08-02 (cono su Ω/Chenais, CEN-O1 permissiva, NONBLOCK+, Λ = cerchi di lip) | Decisioni utente di record; emendamenti D2.1/D2.6 QUEUED | `PANEL_topology_census_2026-07-22.md:329-384`; `docs/rde_nozzle_MASTER.md:306-312` | — (pin; la garanzia di generalita' e' verificata a `:371-377`) |
| [T-OP11e] plug domina debolmente bell puntualmente (sonic-capped, tie region, premium_bound per cella); ranka CHIUSURE mai hardware | THEOREM (EOS-general) | `docs/claims_registry.yaml:368-379` | X-GRP10 (`tests/test_phase_diagram.py`, 8 controlli negativi) + X-GRP12 (`tests/test_phase_diagram_real.py`, 6 controlli negativi) |
| [T-T4] argmax per-fase annidati ⇒ plug NON troncato peak-phase ottimo; troncamento apre PB-2 | THEOREM* (eredita **C-HT4** = chiusura sonic-capped ideal-adaptation, SCHEMA, `:171-182`, inherits `:336`; K-E citation duty) | `docs/claims_registry.yaml:329-340` | X-GRP06/X-GRP10/X-GRP12; oracle O2 o cella capped dove l'estensione perde; il falsificatore di C-HT4 (banda PB-2, `:181`) e' eseguibile solo sotto C61+H20 — C-N2 schedulata al kickoff PB-2/OP-2 |
| [T-P7S1] esistenza argmax su ogni level set margin-certified, classe spline per settore | THEOREM* (residuo R-P7.2 dichiarato) | `docs/claims_registry.yaml:589-600` | sequenza massimizzante certificata senza limite convergente che raggiunge il sup |
| Driver brick-2 esercita il solo settore bell/TOC: W=[theta_B, y_1..y_8], spline clamped/natural, lip eps equality, topologia fissata | PRACTICE ([X-TOCV], brick 2 CHIUSO di record) | `validation/a1_toc_variational_jax.py:1-50,108,1360,1748`; `docs/rde_nozzle_pipeline_decision_map.md:136,154-159` | i controlli negativi del driver (N1 gradiente corrotto, `:65`) |
| H20: free plume boundary p=Pa solve mechanics MISSING; plug/E-D lo RICHIEDONO | OPEN (gap genuino FORK-141, 1 di 2) | `docs/rde_nozzle_pipeline_decision_map.md:183` | — (gap dichiarato) |
| C61: p_b mai adottato (NEVER); Veen legacy WG10-FAILED; slot N2 | NEVER / slot dichiarato | `docs/rde_nozzle_pipeline_decision_map.md:184`; `docs/rde_nozzle_problem_book.md:347-348` | PB-2 banda troncamento/base-pressure oltre le barre (`docs/claims_registry.yaml:181`) |

---

## 3. Gli APERTI (owner / trigger)

1. **H20 — meccanica di solve del free plume boundary + termine shape-adjoint**
   (OPEN, nessuna casa nel record). Owner/finestra: **F4b external-expansion
   window** (cavalca la voce agenda base-pressure diff par.2.9; N2 e' lo slot
   di C61, finestra correlata soltanto) (`docs/rde_nozzle_pipeline_decision_map.md:183`).
2. **C61/N2 — chiusura p_b di programma** (NEVER; Veen WG10-FAILED da
   sostituire). Owner: finestra N2/F4b; trigger di coniazione C-N2 = kickoff
   PB-2/OP-2 (`docs/rde_nozzle_pipeline_decision_map.md:184`;
   `docs/claims_registry.yaml:181`). Satellite: CEN-O8 (floor r_b) entra in c
   quando la chiusura lo richiede (`PANEL_topology_census_2026-07-22.md:382-384`).
3. **Census-lemma rigor session** — promozione dell'advisory (emendamenti
   D2.1/D2.6 dai pin, lemmi di counting, CEN-O4/CEN-O5 analitici, ratifica
   utente). Owner: sessione dedicata, SCHED **F2-exit**
   (`docs/rde_nozzle_PROGRESS_ARCHIVE.md:413`; `docs/rde_nozzle_MASTER.md:306-327`).
   Fino ad allora: nessuna classe di rigore per "settori FINITI" e collasso S0
   citabile solo come advisory.
4. **PB-2 — il plug troncato come primo problema di forma genuinamente
   mediato** (aperto da [T-T4]: il troncamento rompe l'annidamento). Trigger:
   kickoff PB-2/OP-2; dipende da 1+2 (`docs/claims_registry.yaml:333`, `:181`).
5. **Estensione del driver oltre il settore bell** — nessun carrier esercita
   plug/E-D; la chart di settore (C1) ha gia' la migrazione B-spline
   convergiuta ma aperta (F2-C1-CONTROL-CHART-MIGRATION, GAP-21). Owner: F2
   engine window (`docs/rde_nozzle_pipeline_decision_map.md:154-159`).
6. **R-P7.2** — argmax certificato vs sup non certificato sul level set
   (residuo dichiarato di [T-P7S1], `docs/claims_registry.yaml:592`). Owner:
   dossier global-maximum / census-lemma (M0 Card 4, `docs/rde_nozzle_MASTER.md:319-320`).

### 3.5 Dove atterrano questi aperti nel piano: la fase F3 GEOMETRY CLASSES [W-B.1/B6]

Gli aperti 1/2/4/5 non sono orfani di calendario: il piano di record ha
una fase NOMINATA che li raccoglie — **F3 GEOMETRY CLASSES** (D6,
`docs/rde_nozzle_development_plan.md:214`, verbatim verificato alla
riga: *"F3 GEOMETRY CLASSES (3-4 sessions; plug/aerospike primary)"*).
Il suo posto nell'ordine delle fasi (`:214-229`):

- **ENTRY** (`:214-217`): RaoPlug S1/S2 fix in GENO atterrato OPPURE
  status single-oracle dichiarato (Rao 1961 spike Table-1); margine
  Λ-form del mirror plug/C- PROVATO o dichiarato conditional PRACTICE.
- **EXIT** (`:217-222`): plug optimum CERTIFICATO + oracolo spike
  Table-1 (M_E=2.4, gamma=1.23) in bande derivate; almeno UNA istanza
  plug var-gamma o stratificata; T-GB de-rated a THEOREM* con ipotesi
  nominata OPPURE il falsificatore di forma 2-D truncated-plug eseguito
  PRIMA che il primo plug optimum certificato venga consegnato.
- **ORDINE**: F3 viene dopo F2 (i gate di entry presuppongono l'exit
  F2) ed e' **ORDER-INTERCHANGEABLE con F4b dato l'exit F2** (ISS-6,
  adottata dall'esperto RDE, `:227-229`); de-risk del plug-march a
  livello spike AUTORIZZATO in parallelo a F2 (RK1 front-load,
  `:222-223`). Budget cappato ISS-4 (3-4 sessioni, cap 3h/sessione sui
  run decisivi, max 2 campagne decisive per istanza; l'esaurimento del
  cap spara il fallback BY RULE, `:224-227`).

La lettura per questo capitolo: **F3 e' la fase in cui i settori
free-boundary ricevono il loro primo entrant nel torneo a livello
engine** (aperto 5), con H20/C61 che cavalcano la finestra F4b
adiacente (aperti 1-2) e PB-2 come primo problema mediato della coppia
(aperto 4). Il capitolo la nomina perche' il deck deve poter rispondere
"QUANDO?" con una fase di piano citabile, non con un rinvio generico
(critic 8, cella F-v del design v2).

### 3-bis. ANTENATI DIRETTI (lineage, dal LINEAGE_LEDGER) [W-B.1/B6]

Claim di lineage SOLO dal ledger (guardia 10; join su {LL-id,
componenti} per contratto [F-des-4]); tutte le righe sono **CANDIDATE
finche' il refuter C6 (W-C) non passa**
(`validation/spres_raws_2026-08-22/reconstruction/LINEAGE_LEDGER.md`,
header + righe citate). Gli antenati dei nodi N-F/N-G:

- **LL-23 — Hoffman 1987 CTP (+NASA RP-1104)** (componenti 14/12;
  N-16): truncate-compress-tangency + length-band oracolo + design
  chart di pratica **senza governance**. E' l'antenato diretto della
  linea troncamento (PB-2/[T-T4]) e dell'oracolo length-band: il campo
  troncava gia', ma come chart di pratica, senza certificati.
- **LL-25 — Kraiko 2001 (linea Shmyglevskii)** (4/12): condizioni a
  disuguaglianza + slip-line strutturale → antenato dell'**acceptance
  test F4b** (la finestra degli aperti 1-2).
- **LL-27 — Allman-Hoffman 1981** (N-16/N-20/N-17): metodo direct su
  contorno a pochi dof **col prezzo misurato** vs indiretto — antenato
  della domanda "quanti dof e a che prezzo" che la chart C1 eredita.
- **LL-28 — Masters 2017 + Lauer-Ansell 2025** (N-20/N-16): censimento
  delle parametrizzazioni + prior 20-25 dof; **trasferimento a ugelli
  MoC = scope dichiarato** (mai assunto). Antenato diretto della cella
  F-ii (§7).
- **LL-29 — Kraiko 2016** (N-20/N-17): Bezier-chart + GA dentro la
  scuola classica; **il loro dato: exact batte i GA — PRO la nostra
  rotta** (chart certificata + condizioni, non ricerca diretta cieca).
- **LL-31 — linea direct-search (Kraiko-2016 GA, Fernandes, Valeriani,
  Ornano)** (N-17): engine senza condizioni di ottimalita'; i loro
  dati = evidenza PRO il driver certificato (il contrario della rotta,
  usato come controprova).

Nessun claim di novita' di nodo senza ≥1 LL-id (lint 7): per N-F la
novita' e' la coppia {configurazione come output del solid set,
torneo per-settore certificato} — nessuna riga LL la copre (il piu'
vicino: LL-23/LL-29 restano dentro UNA configurazione data); per N-G
la novita' e' il contratto M1-M5 per-Verdict — nessuna riga LL porta
un meccanismo di globalita' dichiarato (coerente con l'esito G-iii,
§1.7). Entrambi i claim restano query-bounded (guardia 9) sul
perimetro del ledger (82 paper, matrice 20×82).

---

## 4. Domande da panel (banco utente, con risposta ancorata)

**(1) "Il profilo ottimo emerge o si presuppone la categoria?"**
Nella FORMULAZIONE emerge: la variabile e' il solid set S, le configurazioni
sono classi topologiche = output (`docs/rde_nozzle_problem_book.md:339-344`), e
il census (advisory) riduce quasi tutta la tassonomia classica a strati di un
solo settore S0 — la cui percorribilita' per cammino continuo in-class e'
pero' CONGETTURALE, non acquisita: *"conjecturally connected (hub argument
owed, CEN-O4)"* (`PANEL_topology_census_2026-07-22.md:55-74`, quote `:68-69`;
CEN-O4 = residuo analitico S15, `:378-379`).
Nell'ENGINE di oggi la categoria e' presupposta: il driver brick-2 cammina una
sola chart (bell/TOC, grafo di parete, topologia fissata,
`validation/a1_toc_variational_jax.py:11-20,33`). Risposta onesta in due
livelli: emergenza by-design nella formulazione + torneo alle chiusure gia'
giocato; emergenza NON ancora esercitata al livello shape-PDE.

**(2) "Il torneo tra settori: chi lo ha gia' giocato e con che esito?"**
Giocato al rung delle chiusure certificate (eps-rung), esito di registro:
[T-OP11e] — plug domina debolmente bell puntualmente sotto chiusura
sonic-capped, tie region caratterizzata, device premium_bound certificato per
cella, carrier X-GRP10/X-GRP12 con 8+6 controlli negativi
(`docs/claims_registry.yaml:368-379`; ruoli distinti: X-GRP10 = oracolo
gamma-const, `:961`; la classe EOS-general e' portata da X-GRP12, route reale
+ equilibrium bracket, `:989`). Dentro la famiglia plug: [T-T4] — vince il
plug pieno peak-phase; il troncato apre PB-2 (`:329-340`). Da dichiarare in
un colpo solo, prima che lo chieda il panel: (a) copertura — le partite
GIOCATE sono due, bell-vs-plug ([T-OP11e]) e il match interno alla famiglia
plug ([T-T4]); **shrouded plug (settore iii), expansion-deflection, famiglia
detached D(m,n) e bare annulus non hanno oggi alcun entrant, a NESSUN rung**;
(b) eredita' — il verdetto within-family eredita la chiusura **C-HT4
(SCHEMA, sonic-capped ideal adaptation, `:171-182`; [T-T4] `inherits`
`:336`)**, e il falsificatore dichiarato di C-HT4 e' esattamente la banda
PB-2 troncamento/base-pressure — **eseguibile SOLO sotto una chiusura p_b
dichiarata (C61, oggi NEVER) e con la meccanica H20 oggi mancante**; il
programma lo sa e lo ha gia' schedulato (conditional C-N2 da coniare al
kickoff PB-2/OP-2, `:181`). Scope da dichiarare sempre: il torneo ranka
**chiusure a pari eps_max, mai hardware** (`:371`); al livello shape-PDE il
torneo non e' stato giocato (un solo settore ha un driver).

**(3) "Cosa vi manca per ottimizzare un plug troncato VERO (p_b, free boundary)?"**
Quattro pezzi, tutti gia' nominati nel record: (a) la chiusura p_b di
programma — stato NEVER, slot N2, la Veen legacy e' WG10-FAILED e va sostituita
(`docs/rde_nozzle_pipeline_decision_map.md:184`); (b) la meccanica di solve del
free plume boundary p = Pa + il termine shape-adjoint — H20, gap genuino senza
casa nel record, finestra F4b (`:183`); (c) il floor di validita' r_b (CEN-O8)
nel vettore dei vincoli quando la chiusura p_b lo esige
(`PANEL_topology_census_2026-07-22.md:382-384`); (d) la **chart di settore
nell'engine discreto**: anche con chiusura + solve, il driver brick-2 non ha
una chart per il settore plug (oggi solo bell/TOC — aperto 5, migrazione
B-spline F2-C1-CONTROL-CHART-MIGRATION aperta, owner F2 engine window,
`docs/rde_nozzle_pipeline_decision_map.md:154-159`). Il problema risultante e'
PB-2, il primo problema di forma genuinamente mediato ([T-T4],
`docs/claims_registry.yaml:333`).

**(4) "Expansion-deflection: e' nel vostro spazio o solo sulla carta?"**
Nello spazio per formulazione: settore dichiarato di A_gen
(`docs/rde_nozzle_problem_book.md:351-353`) e, nella lettura census advisory,
strato di S0 (`PANEL_topology_census_2026-07-22.md:66-68`). Ma la mappa
pipeline dichiara che i settori plug/E-D **RICHIEDONO** il solve H20 mancante
(`docs/rde_nozzle_pipeline_decision_map.md:183`): nessun carrier lo esercita.
Risposta corretta: nel dominio ammissibile si', nell'evidenza eseguibile no —
e la distinzione va detta cosi', senza riempire l'OPEN.

---

## 5. Cosa deve dire il deck

1. **"La configurazione e' un output, non un input"** — design variable =
   solid set nell'envelope; bell, plug, shrouded plug, E-D = classi topologiche
   dell'output (formulazione di record,
   `docs/rde_nozzle_problem_book.md:339-353`). [Formulazione/Def.]
2. **Il torneo per-settore (finitezza = SCHEMA, cfr. item 3) ha gia' un primo
   verdetto**: sotto la chiusura sonic-capped il plug domina debolmente la
   bell puntualmente, con tie region e device premium_bound certificato
   ([T-OP11e], THEOREM, carrier X-GRP10/12); dentro la famiglia, il plug pieno
   peak-phase e' ottimo e il troncamento apre il primo problema genuinamente
   mediato ([T-T4], THEOREM*). Caveat obbligatori a slide: **ranka chiusure,
   mai hardware**; e il verdetto within-family **eredita C-HT4 (SCHEMA)** — il
   suo falsificatore (banda PB-2) diventa eseguibile solo chiudendo C61+H20,
   gia' schedulato (C-N2 al kickoff PB-2/OP-2,
   `docs/claims_registry.yaml:181`).
3. **La decomposizione in settori e' uno SCHEMA dichiarato** (prova e classe
   dovute alla census-lemma session); il census advisory (pin utente 2026-08-02
   inclusi) indica il collasso a un settore S0 + famiglia detached — citabile
   solo come advisory. [SCHEMA + THEOREM-sketch/ADVISORY]
4. **Stato engine, detto onestamente**: il driver brick-2 esercita oggi il solo
   settore bell/TOC (9 dof: theta_B + 8 heights, spline C^2, lip equality,
   TR-Newton segmentato) — la generalita' configuration-free e' della
   formulazione, non ancora dell'engine. [PRACTICE, X-TOCV]
5. **I due mancanti nominati per i settori free-boundary**: H20 (solve del
   plume boundary p = Pa + shape-adjoint; plug/E-D lo richiedono) e C61/N2
   (chiusura p_b, mai adottata; Veen legacy WG10-FAILED). Owner e finestre gia'
   assegnati (F4b, PB-2/OP-2). [OPEN/NEVER — dichiarati, non riempiti]
6. **Anti-claim da tenere pronto in Q&A**: niente esplorazione per derivata
   topologica (caution di record: il center body paga solo a taglia finita —
   si confrontano settori interi, `docs/rde_nozzle_problem_book.md:361-363`).
   [PRACTICE dichiarata]

---

## 6. STORIA (writer W-B.2, 2026-08-23 — trittico [V2-R2]; ogni battuta
## porta DATA + PROCESSO + VERDETTO, campi di join del retro-audit §5-bis)

### 6.1 La formulazione configuration-free (S come variabile di design)

- **Battuta 1 — derivazione originale.** DATA: anteriore al 2026-07-22
  (datazione by-inclusion, dichiarata: il panel census del 2026-07-22 la
  consuma come base; il blocco del problem book non porta data propria).
  PROCESSO: problem book D1 (`docs/rde_nozzle_problem_book.md:337-353`).
  VERDETTO: "Configurations are the TOPOLOGY CLASSES of S — outputs of
  the optimization, not inputs".
- **Battuta 2 — (b) STANCE-DI-FORK.** DATA: 2026-08-17 (Phase A/B
  S-FOUNDATIONS). PROCESSO: un albero cieco produsse un claim di
  DISCONNESSIONE topologica; l'errata di record lo aggiudica contro il
  census — "census S0-collapse beats the blind tree's disconnectedness
  claim; P-F17 divergence → Phase C agenda" (USER CATCH, commit
  5221529; verdetti per-riga nel tree diff dichiarati come stance).
  VERDETTO (stance dichiarata): il record batte il fork; la divergenza è
  consumata in agenda, non ignorata.
- **Battuta 3 — convergenza.** DATA: 2026-08-21 (pipeline decision map,
  refuter 0 BREAK). PROCESSO: la formulazione entra nella mappa come
  spina di stage. VERDETTO: classe finale = formulazione di record; il
  raffinamento census resta ADVISORY in attesa di ratifica utente.

### 6.2 Decomposizione in settori + torneo finito

- **Battuta 1 — derivazione originale.** DATA: problem book (SCHEMA,
  `docs/rde_nozzle_problem_book.md:354-363`, senza data propria) +
  2026-07-22 (counting theorem del census, THEOREM-sketch condizionale,
  `validation/PANEL_topology_census_2026-07-22.md:55-74`). PROCESSO:
  cono uniforme ⇒ finitezza dei settori; Chenais+S1 ⇒ esistenza
  per-settore; ottimo totale = torneo. VERDETTO: M0 dichiara che
  "'FINITE' here carries NO declared rigor class at this site of record"
  (`docs/rde_nozzle_MASTER.md:313-320`).
- **Battuta 2 — mista, per gamba.** (a) RIDERIVATO-PIENO sulla gamba
  ESISTENZA: DATA 2026-08-17; PROCESSO derivatori ciechi — H-F34 cita
  Chenais 1975 verbatim sulla classe uniform-cone, V-F15 aggiunge la
  forma condizionale con H-STAB
  (`validation/sfoundations_raws_2026-08-13/phaseB_tree_diff.md:336-338`);
  VERDETTO: architettura (i) riderivata cieca. (c) NON-RIDERIVATO sulla
  gamba FINITEZZA: la prova è DOVUTA alla census-lemma session
  (schedulata F2-exit, `docs/rde_nozzle_PROGRESS_ARCHIVE.md:413`);
  doppia prova alternativa = il panel census stesso (5-lens + 8-lens
  attack + 3-referee, 233/233 verdetti mappati) CON il caveat di header
  dichiarato: il criterio di convergenza formale NON fu raggiunto prima
  del troncamento infrastruttura (`PANEL_topology_census_2026-07-22.md:11-13`).
  VERDETTO: esistenza confermata; finitezza resta SCHEMA con debito
  nominato.
- **Battuta 3 — convergenza.** DATA: nessun evento di chiusura ancora
  (stato al 2026-08-23). PROCESSO: le due letture (torneo per settori /
  census S0) sono aggiudicate COMPATIBILI in §1.3. VERDETTO: classe
  finale SCHEMA + THEOREM-sketch condizionale; il census RIDUCE le
  partite del torneo, non lo elimina.

### 6.3 I pin utente 2026-08-02 (cono su Ω, PERMISSIVA, NONBLOCK+, Λ)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-02 (pin utente di
  record, census §7pin,
  `validation/PANEL_topology_census_2026-07-22.md:329-384`). PROCESSO:
  decisioni utente registrate nel panel (cono sul lato FLUIDO/Chenais;
  CEN-O1 PERMISSIVA; CEN-O10 NONBLOCK+; CEN-O11 Λ = i due cerchi di
  lip), con garanzia di generalità verificata (`:371-377`). VERDETTO:
  pin decisi, nessuna geometria fisica rimossa.
- **Battuta 2 — (b) STANCE-DI-FORK.** DATA: 2026-08-05 (state-pointer
  notes datate in M0). PROCESSO: i pin sono DECISIONI, non derivazioni —
  M0 li porta come puntatori di stato (`docs/rde_nozzle_MASTER.md:306-312`
  e `:321-327`) che dichiarano gli emendamenti D2.1/D2.6 QUEUED; la
  derivazione pin→lemma è target dichiarato
  (`PANEL_topology_census_2026-07-22.md:359-364`). VERDETTO (stance):
  vincolanti come pin, non promossi a teoria.
- **Battuta 3 — convergenza.** DATA: NON ancora avvenuta (census-lemma
  rigor session schedulata F2-exit). PROCESSO: residuo analitico
  dichiarato CEN-O4 (hub connectedness) + CEN-O5 (`:378-384`).
  VERDETTO: stato onesto = pin di record + sessione dovuta.

### 6.4 Il torneo alle chiusure: T4 / [T-OP11e] / la dicotomia

- **Battuta 1 — derivazione originale.** DATA: 2026-07-21/22 (T3-QS
  remark S12, M0:462; precedente trajectory-averaged page-verified S13
  2026-07-22, M0:2908) e 2026-08-04 (PAN-S14: antenato del meccanismo di
  simultaneous-optimality di T4, M0:2920; classi F riviste dal panel).
  PROCESSO: derivazione in-house della catena T3/T4 + carrier X-GRP10/12
  per [T-OP11e]. VERDETTO: T4 nesting THEOREM*; [T-OP11e] THEOREM
  EOS-general con device di torneo certificato per cella.
- **Battuta 2 — (a) RIDERIVATO-PIENO (cieco).** DATA: 2026-08-17.
  PROCESSO: derivatori ciechi Phase A → tree diff §3 item 5: "delta = 0
  iff one shape is per-phase optimal mu-a.e. = the T3/T4 dichotomy
  criterion re-derived" (V-F25 P1, interchange bound = il nostro
  int-max bound;
  `validation/sfoundations_raws_2026-08-13/phaseB_tree_diff.md:339-344`).
  VERDETTO: il criterio della dicotomia riderivato alla cieca; "any J >
  B is an instant solver-bug rejector" = la dottrina bound-as-oracle
  riderivata con esso.
- **Battuta 3 — convergenza.** DATA: 2026-08-12 (S24 T2a: audit delle 5
  ipotesi del twin S18 PERFORMED, precondizione nominata del T-T3-MAP,
  M0:4138-4140). PROCESSO: audit di precondizione + scope clause.
  VERDETTO: classe finale THEOREM/THEOREM* con lo scope vincolante "i
  winner rankano CHIUSURE a pari eps_max, mai hardware"
  (claims:368-379).

### 6.5 Il driver un-settore (bell/TOC) e il delta formulazione↔codice

- **Battuta 1 — derivazione originale.** DATA: 2026-08-06 (A1 BRICK 2 OF
  RECORD, sessioni S17-S18, M0:3251-3253; carrier [X-TOCV], log S17
  passi 4-11 + S18 passi 3-7). PROCESSO: costruzione del driver
  variazionale TOC end-to-end (heights-as-dofs, TR-Newton segmentato).
  VERDETTO: strada variazionale ESISTE end-to-end — su UN settore, a
  topologia fissata ("dJ/dtheta_B exact at fixed topology").
- **Battuta 2 — (b) STANCE-DI-FORK.** DATA: 2026-08-17 (tree diff,
  verdetti per-riga dichiarati come stance). PROCESSO: C1 design basis =
  DIVERGENT-ENRICHING HIGH (`phaseB_tree_diff.md:22`); C9 mesh law =
  DIVERGENT HIGH 4/4 (`:66`); C31 optimizer = CONVERGENT su famiglia +
  DIVERGENT sulla metà IP (`:159`). VERDETTO (stance): le divergenze
  sono state consumate dalle aggiudicazioni Phase C a convergenza
  (finestre C2-C4, 2026-08-19/21), mai lasciate implicite.
- **Battuta 3 — convergenza.** DATA: 2026-08-21 (pipeline map stage 6).
  PROCESSO: cluster C1-C8 di record con la migrazione control-chart
  CONVERGIUTA come scelta aperta (F2-C1-CONTROL-CHART-MIGRATION,
  `docs/rde_nozzle_pipeline_decision_map.md:154`). VERDETTO: classe
  finale PRACTICE onesta — la generalità configuration-free vive nella
  formulazione e nel torneo alle chiusure, NON ancora nell'engine
  (dichiarazione §1.5, mai ammorbidita).

### 6.6 H20 / C61: i gap free-boundary come scoperte datate

- **Battuta 1 — derivazione originale (dei GAP, non di una teoria).**
  DATA: 2026-08-20/21. PROCESSO: fork adjudication 141 (commit a85e355:
  "2 genuine gaps (H20 F4b; P34 P-1 window)", 90/50/1/0 riconciliati) +
  coverage gate C4 (commit fd2d444: **C61 p_b-closure MINTED**, 6a
  istanza della classe no-row) + base-pressure harvest (commit b3da86d:
  Veen 0.846p/M^1.3 tracciata al fit cold 1966 WG10-FAILED; exhibit
  Humphreys ×2.45). VERDETTO: due mancanze DISTINTE (modello C61 vs
  meccanica H20, edge E12 della mappa `:218`).
- **Battuta 2 — (c) NON-RIDERIVATO esplicito (nessuna derivazione
  esiste: è il contenuto del nodo); doppia prova dell'ASSENZA.** DATA:
  2026-08-20/21. PROCESSO: l'assenza è search-proven due volte con
  strumenti indipendenti — la riconciliazione fork-141 (che trova H20
  come 1 di SOLI 2 gap genuini su 141 fork) e la coverage gate dual-seed
  (che minta C61 sotto critic avversario provato nei due sensi).
  VERDETTO: gap genuini di record, non dimenticanze.
- **Battuta 3 — convergenza.** DATA: 2026-08-21 (registrazione slot).
  PROCESSO: p_b = SLOT DICHIARATO N2 nel problem book (`:347-348`) con
  verdetto "MUST REPLACE IT" su Veen; conditional C-N2 da coniare al
  kickoff PB-2/OP-2 (`docs/claims_registry.yaml:181`). VERDETTO: classe
  finale OPEN/NEVER dichiarata con owner e finestre (F4b; PB-2/OP-2) —
  lo stato onesto È il risultato.

## 7. Posizionamento / conformity (celle F-ii + riga G) [W-B.1/B6]

### 7(a) STRUMENTI

Terna mondo-SOTA / cosa usiamo / perche', per i tool propri del nodo:

1. **Chart di parametrizzazione per-settore** — mondo:
   `masters_etal_2017` (censimento geometrico delle parametrizzazioni
   airfoil, AIAA J; registry `docs/literature_registry.yaml:1023-1029`,
   READ-PARTIAL pp.1,4,13) + `lauer_ansell_2025_pas` (review 2025
   Prog. Aerospace Sci.; `:1031-1037`, READ-PARTIAL pp.19,30) — le due
   fonti del censimento di record (wave-2 rider PANEL_C1REP.md §2.1,
   2026-08-19; retro-sweep 2026-08-20). Noi: cubica interpolante
   clamped/natural heights-as-dofs, **una chart per settore
   topologico** dentro la classe spline certificata, con migrazione
   convergiuta alla chart B-spline control-polygon dello STESSO spazio
   (C1 MIXED, `docs/choice_ledger.yaml:164-174`;
   `docs/rde_nozzle_pipeline_decision_map.md:154`). Perche': la classe
   certificata porta i teoremi di esistenza per-settore ([T-P7S1]) e i
   certificati di ammissibilita'; il dof-budget del mondo entra come
   PRIOR a scope dichiarato, mai come bound di programma.
2. **Il contratto M1-M5 come strumento di consegna** (riga G): ogni
   Verdict dichiara meccanismo e forza (§1.7; M0
   `docs/rde_nozzle_MASTER.md:2982-3005`). Mondo: il quadro locale e'
   `nocedal_wright_2006_2ed` (`:980-987`); per M4 la riga censita
   `wanted_farrell_birkisson_funke_2015` (`:1196-1200`); per M5
   NOT-FOUND(q) (query in §1.7). Perche': e' il pezzo che il campo non
   dichiara (esito G-iii) e che trasforma "ottimo" da parola a
   contratto.
3. **Devices di torneo** — premium_bound certificato per cella +
   controlli negativi ([T-OP11e], carrier X-GRP10/X-GRP12,
   `docs/claims_registry.yaml:368-379,949-961,977-989`): il confronto
   cross-settore alle chiusure e' esso stesso uno strumento con
   rejector, non un grafico.

### 7(b) SENSO

Il tema della cella F-ii: **parametrizzazione per-settore vs
level-set/CAD-based**. La rotta level-set/topology-optimization
metterebbe il cambio di topologia DENTRO una sola rappresentazione
continua; il record la rifiuta per ragione fisica dichiarata — la
CAUTION topological-derivative (`docs/rde_nozzle_problem_book.md:361-363`):
un corpo infinitesimo in corrente supersonica produce solo wave drag,
il center body paga solo a taglia finita, quindi **si confrontano
settori interi** (torneo finito, esistenza per-settore via Chenais
[T-P7S1]) invece di seguire germi topologici. La rotta CAD-based/global
(CST, Bezier, B-spline; censimento `masters_etal_2017` +
`lauer_ansell_2025_pas`, scope transfer a ugelli MoC dichiarato, LL-28)
e' invece ADOTTATA nella variante per-settore della classe certificata
(C1). I precedenti del tema sono in §3-bis (LL-23/25/27/28/29/31); il
dato Kraiko-2016 "exact batte i GA" (LL-29) e la linea direct-search
senza condizioni (LL-31) sono evidenza PRO la chart certificata con
condizioni di ottimalita'. Il gap che il nodo occupa (query-bounded,
perimetro ledger 82 paper + P-A..P-D, §1.7): shape optimization mediata
per-fase con chart per-settore certificate + torneo alle chiusure +
meccanismo di globalita' dichiarato — nessun paper del perimetro
combina i tre pezzi.

### 7(c) STANDARD DI RIFERIMENTO

L'asse della conformity map §C che governa il metodo di questo nodo e'
l'**asse §C-3 — tracciabilita', classe ECSS/DO-178C** (design v2
`ATLAS_RESEARCH_DESIGN_v2.md:279`): ogni scelta del nodo e' una riga
di ledger tipizzata con owner/trigger (C1/C57/C61), ogni claim
load-bearing ha id, casa nell'albero e carrier con rejector; le
DECISION CARD qui sotto sono l'istanza visibile del trace
bidirezionale scelta↔verifica. Divergenza dichiarata (dalla mappa
stessa): nessun audit esterno ne' certificazione DI standard — si
adotta la CLASSE di disciplina. Asse di supporto per la riga G:
**§C-2 — gradazione dell'evidenza, classe GRADE** (`:278`): i
meccanismi M1-M5 e le tre forze canoniche del Verdict sono esattamente
una gradazione dichiarata della certezza, mappata sulle classi
THEOREM/THEOREM*/SCHEMA di CLAUDE.md R4.

### 7(d) DECISION CARD (formato §1g dell'emendamento v2.1, 6 campi)

**CARD F-ii — rappresentazione dello spazio di design: per-settore vs level-set/CAD-based**
1. **Scelta**: working class A = chart spline finito-dimensionali
   PER SETTORE topologico dentro le classi C^{1,1}/cono uniformi
   (`docs/rde_nozzle_problem_book.md:365-368`), col torneo finito come
   meccanismo cross-settore (§1.2).
2. **Alternative censite**: (i) level-set/topology-opt (topologia dentro
   una rappresentazione continua) — censita come alternativa nella
   cella F-ii del design v2 (2026-08-22, orchestratore S-PRES,
   `ATLAS_RESEARCH_DESIGN_v2.md:331`); NESSUNA survey di record
   dedicata al level-set per ugelli supersonici — dichiarato, non
   riempito; (ii) CAD-based/global parametrization (CST/Bezier/
   B-spline) — censite da `masters_etal_2017` + `lauer_ansell_2025_pas`
   (PANEL_C1REP.md §2.1, 2026-08-19; retro-sweep 2026-08-20).
3. **Verdetto + perche'**: per-settore. La CAUTION
   topological-derivative di record (`:361-363`) toglie il fondamento
   fisico all'esplorazione a germi; Chenais+[T-P7S1] danno esistenza
   per-settore; il torneo alle chiusure e' gia' giocato ([T-OP11e]).
4. **RECENCY/SOTA check**: censimento parametrizzazioni ancorato a una
   review 2025 (`lauer_ansell_2025_pas`) riletta 2026-08-20; lato
   level-set il censimento e' solo design-cell (2026-08-22) senza
   survey dedicata → per il ramo (ii) **ATTUALE(perimetro
   parametrizzazioni curve airfoil→MoC con transfer scope dichiarato,
   check 2026-08-23)**; per il ramo (i) **STALE → finestra census-lemma
   session (F2-exit): survey level-set dedicata da mintare se il ramo
   si riapre**.
5. **Falsificatore**: un run level-set/topology-opt supersonico che
   produca un ottimo certificato cross-settore in-class che batta il
   vincitore del torneo per-settore a pari vincoli; oppure una prova
   che la derivata topologica sia informativa a taglia finita in
   questo regime.
6. **Trigger di ri-esame + finestra**: census-lemma rigor session
   (SCHED F2-exit, `docs/rde_nozzle_PROGRESS_ARCHIVE.md:413`) — se la
   promozione del census cambia la struttura dei settori, la scelta di
   rappresentazione si riapre.

**CARD C1 — chart di base del settore (design basis class)**
1. **Scelta**: C1 (`docs/choice_ledger.yaml:164-174`) — incumbent:
   cubica interpolante clamped/natural heights-as-dofs; direzione
   convergiuta: migrazione alla chart B-spline control-polygon dello
   STESSO spazio spline certificato.
2. **Alternative censite**: B-spline control polygon (de Boor/Boehm),
   CST (Kulfan), Hicks-Henne — ledger C1; aggiudicazione wave-2
   `VERDICT_wave2.md#4.5` (2026-08-19); dof-prior Masters 2017
   (retro-sweep 2026-08-20, transfer scope 2-D external-aero Euler
   dichiarato).
3. **Verdetto + perche'**: MIXED (adjudicated-split): incumbent
   verdict-bearing finche' i tre falsificatori di migrazione non
   passano; la nuova chart porta certificati di ammissibilita'
   Bernstein-exact nello stesso spazio certificato.
4. **RECENCY/SOTA check**: censimento basi = panel wave-2 2026-08-19 +
   review 2025 in registry; il prior dof attende la verifica full-text
   (`docs/literature_registry.yaml:1029`, flag dichiarato) →
   **ATTUALE(perimetro basi spline/CST/B-spline per contorni 2-D,
   check 2026-08-23)**.
5. **Falsificatore**: i tre falsificatori di migrazione di
   `VERDICT_wave2.md#4.5` (il primo ri-pinnato sulla risposta
   innocent-data della chart con conversion-map pin per-uso).
6. **Trigger + finestra**: duty **F2-C1-CONTROL-CHART-MIGRATION**
   (items 0-6 + driver leg; GAP-21 carrier) — finestra F2 engine
   window (`docs/rde_nozzle_pipeline_decision_map.md:154`).

**CARD C57 — tier di esplorazione globale (NEVER: non-aggiudicata, stampata per obbligo §1g)**
1. **Scelta**: C57 (`docs/choice_ledger.yaml:771-780`) — incumbent:
   NESSUNO (local-only da continuation/warm start).
2. **Alternative censite** (ledger C57, directive-axis verification
   2026-08-19; census esplorazione PANEL_C2021.md §2.3, 2026-08-19):
   layer globale DFO/BO/evolutionary sopra il closer certificato;
   captured-explorer reuse (tier C49); multi-start continuation sulla
   macchina di branch esistente (linea V-F26/V-F7).
3. **Verdetto**: **NON AGGIUDICATA** (status NEVER di record).
4. **RECENCY/SOTA check**: censimento alternative datato 2026-08-19
   (wave-2/PANEL_C2021) → **ATTUALE(perimetro solver/explorer census
   2026, check 2026-08-23)**.
5. **Falsificatore** (della futura scelta): un competitor enumerato da
   M4/M5 che batta il best-of-sweep del closer locale a pari
   certificati — e' la ragione per cui i numeri restano best-of-sweep
   (guardia 8, §1.7).
6. **Trigger + finestra**: **F2-entry adjudication window**,
   aggiudicata come CLUSTER con C31 A/B, C58, C60, [P-IPADJ]
   (`docs/rde_nozzle_pipeline_decision_map.md:138,199-204`).

**CARD C61 — chiusura base-pressure p_b: PUNTATORE alla casa primaria
[dedup WB1-C3-17 RISOLTO, orchestratore 2026-08-23]**
La card completa 6/6 campi vive UNA volta in **CH6 §8 (casa PRIMARIA,
decisione B5 con ragione dichiarata: la scelta e' costitutiva di PB-2 e
il trigger C61 e' PB-2-shaped)**. Qui resta solo il join richiesto
dall'obbligo §1g per le scelte che questo capitolo presenta (§1.6):
C61 = NEVER, incumbent legacy Veen WG10-FAILED, slot di programma N2
(`docs/rde_nozzle_problem_book.md:347-348`), STALE → finestra N2/F4b;
falsificatore e trigger nella card primaria. Mai due card gemelle
(regola anti-entropia SR-7).

---

## Disposizione riparazioni (W-A, 2026-08-23)

Applicazione dei 10 finding di REFUTE_CH8 (writer A2, onda W-A). Ancore
ri-verificate alla fonte in-window prima dell'uso (C-HT4
`docs/claims_registry.yaml:171-182` + inherits [T-T4] `:336` + falsifier
`:181`; census `:11-13`/`:40`/`:68-69`/`:102`/`:170`/`:359-364`/`:378-384`;
findings `docs/findings_registry.yaml:2519` + mappa `:183` "registry :2521
ordinal" verbatim; X-GRP10 `gamma-const-oracle` `:961`, X-GRP12 EOS-general
`:989`).

| # | classe | cambiamento (sezione+riga) | esito |
|---|---|---|---|
| 1 | REPAIR (ALTA) | §4(2) punto (b): loop C-HT4 dichiarato per esteso (eredita' SCHEMA, falsificatore = banda PB-2 eseguibile solo sotto C61+H20, C-N2 schedulata `:181`); §5 item 2: caveat di eredita' C-HT4 aggiunto; §2 riga [T-T4]: classe e falsificatore estesi con inherits `:336` | RIPARATO |
| 2 | REPAIR (ALTA) | §1.3 (paragrafo "Conseguenza"): "cammino continuo dentro S0" sostituito con connessione CONGETTURALE (quote "conjecturally connected (hub argument owed, CEN-O4)" `:68-69`, residuo `:378-379`, continuita' argomentata solo ai confini di strato `:60-62`); §4(1): "percorribile con continuita'" condizionato con la stessa quote; §1.3 headline + §2 riga collasso: inciso congetturale | RIPARATO |
| 3 | REPAIR (MEDIA) | §5 item 2, prima riga: "Il torneo e' finito" → "Il torneo per-settore (finitezza = SCHEMA, cfr. item 3)" | RIPARATO |
| 4 | GAP (MEDIA) | §4(2) punto (a): enumerazione esplicita — giocate solo bell-vs-plug e plug-interno; shrouded plug, E-D, D(m,n) e bare annulus senza entrant a nessun rung | RIPARATO |
| 5 | GAP (MEDIA) | §4(3): "Tre pezzi" → "Quattro pezzi", aggiunto (d) chart di settore nell'engine (aperto 5, F2-C1-CONTROL-CHART-MIGRATION, owner F2, `docs/rde_nozzle_pipeline_decision_map.md:154-159`) | RIPARATO |
| 6 | DOWNGRADE (MEDIA) | §1.3: "Correzione Migdal di record" → "Correzione Migdal dichiarata nell'advisory (tag [DECLARED], Round 2)" — declassamento dichiarato: il census e' advisory non ratificato (`:13-14`), nessuna classe of-record disponibile | DECLASSATO (classe corretta = [DECLARED] in advisory) |
| 7 | REPAIR (MEDIA) | §1.3: "provati vuoti" → "vuoti per L1+A1 nell'advisory" con ancora corretta `:170` (riga DELETED) + condizionalita' L1 su CEN-O10 (`:102`) + pin→lemma S15 (`:359-364`); §2 riga collasso allineata | RIPARATO |
| 8 | GAP (BASSA) | §1.3, citazione panel: caveat header aggiunto accanto a 233/233 — criterio di convergenza formale NON raggiunto (`:11-13`) | RIPARATO |
| 9 | NOTE (BASSA) | §1.6: ancora corretta a `docs/findings_registry.yaml:2519` (riga misurata) con glossa ":2521 ordinal" = testo verbatim della mappa `:183` (verificato in-window) | RIPARATO |
| 10 | NOTE (BASSA) | §4(2): parentesi ruoli carrier — X-GRP10 = oracolo gamma-const (`:961`), EOS-general portato da X-GRP12 (`:989`) | RIPARATO |

Esito complessivo: 9 RIPARATO + 1 DECLASSATO-con-ragione (finding 6: il
claim non era riparabile ad ancora perche' nessuna classe of-record esiste
per la correzione Migdal — il declassamento a [DECLARED]-in-advisory e' la
classe vera, non un softening); 0 RESPINTO. Guardie GUARD_CHECKLIST
verificate sul delta: 2/3 non toccate (nessun T1c, nessun rung quasi-1D
introdotto), 8 non toccata (nessun claim best-of-sweep in CH8, §1.7 = W-B.1),
9 non attivata (nessun claim di novita'), 1 non attivata (gerarchia gap non
enunciata in CH8). Base per B6 (W-B.1: aggiunge §1.7/§3.5/§7) e per lo
storico B8b.

[Nota B6, W-B.1 2026-08-23: le sezioni §1.7, §3.5, §3-bis, §7 e il DECK
FEED sono state AGGIUNTE dopo questa disposizione senza toccare le
riparazioni W-A; la guardia 8, sopra "non toccata", e' ora ESERCITATA
in §1.7 come previsto dalla checklist ("CH8 §1.7 in scrittura W-B.1");
la guardia 9 e' ora attivata e soddisfatta in §3-bis (novita'
query-bounded sul perimetro ledger); le guardie 2/3 restano rispettate
(§1.7 M3 usa il naming "oracolo quasi-1D senza contouring", nessun
T1c).]

[Riparazione B6 post-refuter, 2026-08-23 — WB1-C3-16 (REPAIR MEDIA)
APPLICATA: query G-iii rieseguita dal writer nel perimetro dichiarato,
comando stampato in forma -E ESATTA riproducibile, esito vero
dichiarato (0/0/0/0 study file + 0 litmap + 2 hit registry
`:1197`/`:1200` squalificati uno per uno = la nostra riga censita
`wanted_farrell_birkisson_funke_2015`, non un paper del campo); DECK
FEED 6 allineato alla forma corretta; MINT-PENDING F-2 eredita la
forma riparata. WB1-C3-17 (NOTE BASSA) applicata a costo zero: nota di
dedup sotto la card C61 (§7(d)) con rinvio all'orchestratore per la
casa primaria unica. Il merito del claim G-iii sopravvive (conferma
del refuter stesso).]

---

## DECK FEED (B6, W-B.1 — asserzioni candidate-slide, frase piena + ancora + classe)

1. **Il TIPO di ugello e' un OUTPUT dell'ottimizzazione, non un input:
   la variabile di design e' il solid set nell'envelope, e bell / plug /
   shrouded plug / expansion-deflection sono classi topologiche del
   risultato.** — `docs/rde_nozzle_problem_book.md:339-353` —
   [Formulazione di record / Def.] *(feed di punta del capitolo)*
2. **Il torneo tra configurazioni ha gia' un primo verdetto alle
   chiusure certificate: il plug domina debolmente la bell puntualmente
   sotto chiusura sonic-capped, con tie region caratterizzata — e il
   verdetto ranka CHIUSURE a pari eps_max, mai hardware.** —
   [T-OP11e], `docs/claims_registry.yaml:368-379`, carrier
   X-GRP10/X-GRP12 — [THEOREM, EOS-general]
3. **Dentro la famiglia plug vince il plug pieno peak-phase; il
   troncamento rompe l'annidamento e apre il primo problema di forma
   genuinamente mediato (PB-2).** — [T-T4],
   `docs/claims_registry.yaml:329-340` (eredita C-HT4, SCHEMA) —
   [THEOREM* con eredita' dichiarata]
4. **Ogni ottimo consegnato dichiara il suo meccanismo di globalita'
   (M1-M5) e la sua forza — "global" / "within delta of global,
   certified" / "local + enumerated competitors" — mai la parola
   "ottimo" senza contratto.** — M0 IV,
   `docs/rde_nozzle_MASTER.md:2982-3005` — [contratto di record /
   proposta G-iv]
5. **Best-of-sweep ≠ argmax: i numeri di campagna si presentano come
   best-of-sweep certificato, mai come ottimo globale senza meccanismo
   dichiarato.** — M0 IV + GUARD_CHECKLIST guardia 8; C57 NEVER,
   `docs/rde_nozzle_pipeline_decision_map.md:138` — [regola di
   presentazione / PRACTICE]
6. **Nessuno dei quattro paper di campagna del campo (PKU Liu 2022,
   NUAA Li-Xu 2023/2025, Jourdaine 2019) dichiara un meccanismo di
   globalita' — il contratto per-Verdict e' il nostro delta.** — query
   G-iii rieseguita 2026-08-23 (forma riparata WB1-C3-16): 0 hit sui
   4 study file + 0 sul litmap; i 2 hit registry (`:1197`/`:1200`) =
   la NOSTRA riga censita `wanted_farrell_birkisson_funke_2015`,
   squalificata con ragione in §1.7 — [search-proven NOT-FOUND(q) con
   hit squalificati dichiarati; MINT-PENDING F-2]
7. **Il p_b sposta l'argmax del plug troncato di ×2.45 a valore quasi
   piatto (Humphreys 1971): la piattezza del valore NON certifica il
   design — per questo il target M3 e' l'unimodalita' della duty
   variable del truncated plug.** — `docs/rde_nozzle_MASTER.md:1455-1464`
   [ORCH-HARV-3] + M0 :2999 — [[ADV] exhibit + target di contratto;
   CT-6: numeri citati, non riprodotti]
8. **Stato engine detto onestamente: oggi il driver esercita UN settore
   (bell/TOC, 9 dof); i settori free-boundary hanno owner e finestre
   nominate (H20/C61 → F4b, chart → F2), e la fase di piano che li
   raccoglie si chiama F3 GEOMETRY CLASSES (plug/aerospike primary).**
   — [X-TOCV] + `docs/rde_nozzle_development_plan.md:214` — [PRACTICE +
   piano di record]
9. **La rotta di parametrizzazione e' per-settore nella classe spline
   certificata (migrazione B-spline convergiuta), non
   level-set/derivata topologica — e il dato della scuola classica
   "exact batte i GA" (Kraiko 2016) e' evidenza PRO la rotta
   certificata.** — CAUTION `docs/rde_nozzle_problem_book.md:361-363` +
   card C1 (§7) + LL-29 (CANDIDATE, C6 pending) — [PRACTICE/MIXED +
   lineage CANDIDATE]
