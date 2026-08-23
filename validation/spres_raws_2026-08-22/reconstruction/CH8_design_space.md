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
