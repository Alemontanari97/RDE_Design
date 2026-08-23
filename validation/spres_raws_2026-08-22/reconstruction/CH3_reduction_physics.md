# CH3 — Cosa perde il programma rispetto al 3D puro — e come tocca l'ottimo

STATO DEL DOCUMENTO: ricostruzione S-PRES (2026-08-22/23) dal record di
programma. NON aggiudica nulla di nuovo: ancora, trascrive, dichiara gli
aperti. Stadio di confronto: `docs/rde_nozzle_MASTER.md` (M0),
`docs/findings_registry.yaml`, `docs/rde_nozzle_pipeline_decision_map.md`,
`docs/glossary.yaml`. Ogni claim porta ancora + classe di rigore
(THEOREM/THEOREM*/SCHEMA/CONJECTURE/PRACTICE; provenienza [REP]/[ADV]/
[INF]/[SE]). Arco di consumo: storyboard v3, banca Q&A red-team, F2+.

---

## 1. Ricostruzione

La domanda dell'utente a cui questo capitolo risponde: *"nella
presentazione si parla di cosa il programma perde a livello di fisica
rispetto a un 3D puro e come questo influenzi l'ottimo stesso?"* La
risposta di record esiste, è strutturata, ed è stata costruita in tre
mosse formali + una campagna di misura pianificata — tutte atterrate in
M0 nella chiusura S-FOUNDATIONS-C4 (2026-08-20/21). La genesi è essa
stessa di record: la review di letteratura aveva importato l'epistemologia
empirica del campo CFD ("la domanda R22 si decide con un esperimento
CFD"); la correzione metodologica dell'utente (2026-08-13) ha imposto la
decomposizione formale-prima — (1) T-DISC, (2) T-RED, (3) M-RED, (4)
R22-CFD ri-scopato a residuo irriducibile, "no longer the decider"
(`docs/findings_registry.yaml:1459-1468`, riga
`theory:r22-formal-decomposition`, mechanism
`epistemology-bias-from-literature`).

**Box — la riduzione in 3 mosse (cappello per non-esperti) [W2-R10]:**
(1) QUOZIENTE wave-frame: sotto il pin d'onda rotante periodica pura
[T-T0P] il passaggio al riferimento solidale all'onda è ESATTO — il gap
di time-coupling è identicamente zero sulla classe certificata, modulo le
liste di gap dichiarate (M0:1343); (2) MARCH 2D PER-FASE: il campo viene
risolto fase per fase da un march 2D che non trasporta la struttura
azimutale (ciò che scarta è esattamente l'operatore K di [T-RED],
M0:1786-1807); (3) MEDIA DI CICLO: il funzionale J è la spinta
cycle-averaged sui dati per-fase full-state. Mini-glossario (definizioni
di record in `docs/glossary.yaml`): *per-fase* = indicizzato dalla fase
d'onda xi nel wave-frame; *quoziente wave-frame* = il passaggio (1);
*booking* = come il funzionale contabilizza un contenuto dai dati
d'interfaccia; *on-ray/off-ray* = dentro/fuori la famiglia di raggi della
cancellazione St^2; *fitted sheet* = foglio d'urto adattato che porta il
contenuto d'atomo; *St_n* = numero di Strouhal della riduzione; *fibra* =
insieme dei dati con identica traccia p-only (D1.1/D1.2, M0:993-1008).

### 1.1 [T-DISC] Fiber-separation: quale riduzione è CONDANNATA e quale ESONERATA (M0:977-1280)

Il primo teorema separa due oggetti che nel dibattito di letteratura
restano non distinti (tensione R26, registry :2148) [W2-R12]. Si definisce
la classe ammissibile A dei dati d'interfaccia per-fase (onda rotante
periodica pura pin H3, miscela frozen thermally-perfect pin P1,
normalizzazione H9, misura mu = pushforward della misura temporale;
D1.1, M0:993-1002) e la proiezione p-only pi che trattiene la sola
traccia di pressione P(xi) e sostituisce ogni altro campo con il default
phase-uniform (D1.2, M0:1004-1008). Il PIN decisivo [REV2-r1-1]
(M0:1010-1020): il default è PINNATO = le mu-medie della famiglia stessa
— la fibra sopra P è la fibra "calibrated-scalars", e la coordinata di
fibra è esattamente il contenuto di fluttuazione + swirl che [T-DISC-1]
spazza e che la banda B-2 di M-RED misura. Scope di settore dichiarato
[W2-R9]: gli enunciati sono fatti sul settore supersonic-map; il settore
subsonico "joins the mixture form and is out of this theorem's scope,
declared" (M0:1025-1028).

- **[T-DISC-1] FIBER NON-DEGENERACY — THEOREM\*** (M0:1030-1084): per
  ogni traccia P ammissibile con through-flow, la fibra contiene una
  famiglia a un parametro {s_lambda} con IDENTICHE tracce (P, h0, s,
  mass-flux) e flusso di energia cinetica di swirl E_theta che va da 0 a
  un valore strettamente positivo alla scala misurata del corpus — e
  NESSUN vincolo di record fissa E_theta dato P(xi) (M0:1033-1039).
  Prova per citazione (zero derivazione nuova): flux-nullity
  [MS-T-FLUXNULL] THEOREM* (M0:1041-1044), [MS-T-SKE] THEOREM
  (M0:1045-1048), K-bar = 0 fiberwise incondizionato (M0:1049-1053).
  Condizionali nominati: (c1) check simbolico assembled-balance QUEUED
  (gap G-a), (c2) H-AM0 audited-per-dataset (M0:1066-1073). Falsificatore:
  esibire UN vincolo di record che determini E_theta da (P, h0, s, mdot)
  — collasserebbe la fibra e ucciderebbe il teorema (M0:1079-1084).
- **[T-DISC-2] J-SEPARATION — split-grade dichiarato per gamba**
  (M0:1086-1182): (i) gamba di SEGNO, THEOREM* SCOPED al livello
  BOOKING su confronti physical-h0-fixed: dalla relazione esatta per
  streamline u_e^2 = 2(h0 − h) − v_e^2 − Gamma^2/r_e^2, ogni incremento
  di Gamma^2 sottrae esattamente Gamma^2/r_e^2 da u_e^2 (M0:1091-1103);
  il termine di pressione è fisso PER IPOTESI H2.2 (exit congelata,
  M0:1108-1114). Sul ramo DROP non compensato il segno è
  geometry-signed con l'angolo degenere r_e = r_in (separazione ZERO;
  M0:1115-1129). Il caso actual-pair (exit libera) NON è asserito ad
  alcun grado di teorema: è la domanda misurata della banda B-2
  (M0:1130-1139). (ii) gamba di MAGNITUDINE, SCALING-ESTIMATE
  etichettata, NON un bound: classe 1.5-3% della spinta (variante FOLD),
  con la compagna B1 (radial equilibrium) 0.6-9% di p, single-signed,
  phase-coherent, "survives EVERY mu-average" (M0:1140-1151). Lettura
  lower-bound onesta: il contenuto a grado teorema è che la variazione
  di J entro fibra è limitata dal basso da un funzionale strettamente
  positivo single-signed (il debito E_theta); il suo pavimento NUMERICO
  è estimate-class finché M-RED non lo misura — "No numeric lower bound
  is asserted at THEOREM grade" (M0:1152-1158).
- **[T-DISC-3] 2-EPSILON TRANSFER — SCHEMA** (M0:1184-1240): due gambe.
  (a) Adequacy/upper, per-surrogato: con premessa di errore uniforme
  (U_G), ogni argmax legittimo del surrogato è al più 2·eps_G
  subottimale (costante 2 sharp; (U) OPEN due volte; M0:1200-1209).
  (b) Irreducibility/lower, la direzione di condanna: con la premessa
  di realizzabilità di design (DR), OGNI surrogato che fattorizza per pi
  ha sup-error ≥ osc/2, il miglior surrogato p-only raggiunge esattamente
  sup_P eps_fib(P)/2, e nessun raffinamento dei dati p-only riduce QUESTO
  pavimento (M0:1210-1225). L'errore di ranking INTER-fibra di un
  surrogato p-only è ILLIMITATO dai diametri di fibra (M0:1226-1228).
- **[T-DISC-4] VERDETTO — SCHEMA** (M0:1242-1280): CONDANNATA la
  riduzione P-ONLY pi — "Pressure-only surrogates are therefore NOT
  adequate for percent-level thrust ranking on swirl-bearing RDE data —
  with zero CFD consumed" (M0:1245-1253). NON CONDANNATA (esonerata su
  questo asse) la media full-state per-fase del programma, che porta
  (p, h0, s, u_x, Gamma) per fase: "its data do not factor through pi"
  (M0:1254-1259). L'esposizione residua del NOSTRO J sta sugli assi
  RIDUZIONE ([T-RED]) e ADEGUATEZZA (forchetta (i)/(ii)/(iv))
  (M0:1257-1259). Falsificatore della RILEVANZA (non della verità): se
  M-RED misura eps_fib sotto il più piccolo delta di design mai
  certificato, la condanna è vera ma prezzata irrilevante — "an honest
  positive outcome, reported as such" (M0:1276-1280).

In una frase per il deck: **il teorema condanna con zero CFD la
riduzione a sola pressione, ed esonera — su quell'asse — la media
full-state che il programma effettivamente usa.**

### 1.2 [T-RED] L'operatore-residuo: ciò che il march 2D per-fase butta, scritto ESATTO (M0:1734-1909)

La seconda mossa scrive l'oggetto scartato. Con U il vettore di stato e
F_phi,rel il flusso azimutale wave-frame (identità riga-per-riga esatta,
sympy PASS; M0:1790-1797), l'operatore residuo di riduzione è

    K(x, r, phi) := (1/r) d_phi [ F_phi,rel( W(x, r, phi) ) ]

in senso distribuzionale, e la riduzione per-fase-2D risolve il sistema
K-DROPPED: i termini di struttura azimutale scartati sono ESATTAMENTE le
sei righe avvettive + gli atomi di fronte di K (DEFINITION, identità
THEOREM*; completezza del censimento resta gap G-f SCHEMA — "grades NOT
inflated here"; M0:1786-1807).

- **K-bar = 0 — THEOREM\*, MINTED a grado record** al landing C4
  (prova a penna + testimone macchina, vale su BV pieno: a.c. + Cantor
  + atomi; M0:1768-1773, 1833-1838). CONSEGUENZA: il residuo NON ha un
  canale mean-field al primo ordine; sopravvivono esattamente DUE canali
  al primo ordine in J: **(J)** l'accoppiamento atomi/salti
  <psi-bar, atom content> e **(H)** il canale covarianza/isteresi a.c.
  −Cov^{ac}(psi, K) (M0:1839-1849). Il "esattamente due" è condizionato
  alla clausola SBV H-RED-2 (su un campo BV-with-Cantor esisterebbe un
  terzo canale; M0:1821-1830, 1850-1853).
- **Magnitudini: tutte SCALING-ESTIMATE, etichettate** (M0:1854-1862):
  scala del coefficiente al primo ordine Lambda = 0.59-1.11·St_n;
  termine pressure-work 0.007-0.09 (= 0.7-9%); frasario licenziato con
  la condizione fitted-sheet restaurata: "single-digit-% total PLAUSIBLE
  on ray-like sawtooth cycles WITH A GOOD FITTED SHEET; >10% NOT
  EXCLUDED off-ray" (M0:1844-1849).
- **[T-RED-2G] livello gradiente di design — SCHEMA** (M0:1911-1956):
  delta(S) := norma duale proiettata del gap grad J_true − grad J_red;
  per rappresentazione aggiunta il gap eredita gli STESSI due canali
  (J)/(H) al livello gradiente (M0:1929-1938). STATO ONESTO, verbatim:
  "NO closed-form gradient bound is derivable at current record … this
  schema + the named derivers IS the deliverable at this rigor class"
  (M0:1953-1956). I tre deriver NOMINATI in ordine: (1) five-field
  content bound X-T3QS-5F (F2); (2) C51-route-B (trattamento nativo dei
  fogli elicoidali); (3) M-RED gradient-measurement rider §3.6
  (M0:1946-1952). **Cross-ref di licenza [B3-BLITE] (CH1 §1.7 H-v)**:
  accanto ai deriver esiste il metro esatto CHEAP del residuo — B-lite
  [S-BLITE], verbatim di record "the cheap exact meter of the rung-2
  sweep/D2 residual" (M0:3027-3044, verbatim :3037-3038): sul dominio
  nozzle-only con margine assiale certificato u_x − c ≥ δ il campo
  wave-frame ESATTO si calcola per space-marching elicoidale 3-D a costo
  di march (adjoint verbatim per Lemma B) — lo strumento che può
  ARBITRARE i deriver senza il solve globale né la camera; brick nominato
  da verificare per primo: G12-L1-3D. Anche **L_H** — la faccia a livello curvatura del
  residuo di riduzione (H-G6: mu_eff = (mu_meas − b_E) − L_H) — è
  UNDERIVED con deriver nominati (M0:2018-2026; forchetta (vi),
  M0:1348): finché L_H non atterra, la via gradiente non licenzia
  NESSUN numero nemmeno a-posteriori dal solo carrier misurato.

### 1.3 [R22F-FORCHETTA] La forchetta integrale: i 6 canali, fisica per canale (M0:1283-1494)

La tabella user-facing di record (M0:1341-1348), regole di cella
vincolanti: "bound-or-estimate declared; rigor class per bound; …
NO cell above its held evidence class" (M0:1305-1309). Contenuto fisico
canale per canale:

**(i) Time-coupling / unsteadiness** — *la non-stazionarietà vera del
motore vs il quoziente stazionario.* BEST: **0 (esatto)** sulla classe
certificata — [T-T0P] steadifica: sotto il pin d'onda rotante periodica
pura il quoziente in wave-frame è ESATTO, il gap è identicamente zero
MODULO le liste di gap dichiarate (strati A/B: G1,G2,G7,G8; +G5, G4;
+G3,G11,G9) e lo scoping Cor 5.1: cl(Omega_march), slip-free (M0:1343)
[W2-R13]. WORST: **CLASS EXIT, unbounded of record** — storage
aperiodico / transizioni di modo sono un'uscita di classe H-AM1, non un
numero di gap; i fronti slip-sheet ("the physically generic RDE type")
sono ESCLUSI da G9; la metà correttore steady-sweep è G3-owned, non
quantificata. Guardia = monitor di piattezza T0 + campo di contratto
f_cycle. "No number is asserted — asserting one would exceed evidence"
(M0:1343). Classe: [T-T0P] SCHEMA sui due strati; boundary PRACTICE.
Tightener: R22-CFD-1, lift G5/G9 (F2), programma correttore.
**Scope esplicito del corrector (cella M-i) [B3-MI]: il corrector O(St)
di record è una PERTURBAZIONE DELLO SWEEP STEADY sull'ancora wave-frame
— one linearized solve, ingaggiato QUANDO T0 applica (modo single/k-wave
certificato); la route generale unsteady (O5) resta SEMPRE in pipeline e
la route cheap è "a licensed specialization, not a replacement"
(M0 VI.4bis(ii), :3145-3150, verificato alla riga 2026-08-23; memoria
periodic-wave-data-scope). Il corrector NON è un solve instazionario: è
la derivata del sweep steady rispetto alla fase.**

**(ii) Riduzione della struttura azimutale** — *eliche, fronti interni,
la faccia propria di T-RED: ciò che varia in phi e il march 2D non
trasporta.* BEST: O(St_n^2) on-ray; "single-digit % plausible" [SE],
letto CON la condizione good-fitted-sheet; il canale medio è morto per
teorema (K-bar=0 THEOREM*); la cancellazione St^2 on-ray esiste in-panel
ma è LICENSE-GATED (X-T3QS-5F, F2) — "NOT bankable in this cell yet".
WORST: **">10% NOT EXCLUDED off-ray"** [SE]; i segmenti di fronte
interni alimentati azimutalmente sono IRRAGGIUNGIBILI dal march (row-13
pin), magnitudine E5 DISPUTED-OPEN; **Harroun 2021 Fig. 18 (p. 669,
page-verified) è l'istanza fisica della classe di meccanismo**
(M0:1344, 1900-1902). Contesto esterno [ADV]: P-B 2.8% gap uniforme
steady-vs-transient (≤60% trunc), P-C 0.2-1.5%; ma P-B 80% divergenza
−5.78% "flow swirling induces the trailing shock wave in advance" =
meccanismo di crescita configuration-dependent (GRAFT-G03,
M0:1377-1383). Tightener: T-RED → M-RED bande B-1/B-3 → licenza
X-T3QS-5F → R22-CFD-1.

**(iii) Swirl / contenuto tangenziale** — *l'energia cinetica azimutale
che il funzionale booka o non booka dai dati.* BEST: B2 ≈ 0 (convenzione
drop con r_exit ≈ r_in, geometry-signed) + B1 allo 0.6% di p [SE].
WORST: **B1 fino a 9% di p + B2 3% della spinta (fold) + B5 14 gradi di
angolo di swirl all'exit** [SE], tutti single-signed/phase-coherent,
"survives EVERY mu-average"; e il **MARKER DI DIREZIONE PEGGIORE
obbligatorio: lo shroud Paxson-Miki — 58.1% → ~71.5% dell'ideale
nozionale a AREA RATIO FISSATO** (V7 argmax ~71.5%, V5 raccomandata
70.0%; punti percentuali di ideale; correzioni C25 a
`findings_registry.yaml:2026`) — "larger than the entire area-ratio
design line, declared unexplained by the authors, and the registered
swirl-breaker candidate": effetti a scala di configurazione a cui la
media 2D per-fase potrebbe essere cieca (M0:1345). Dato esterno
indipendente [INF]: P-B V_cir 327-383 m/s ⇒ eps_theta ~0.17-0.20 dentro
la banda DISPATCH §9 (0.15-0.20), con il caveat film-cooling dichiarato
(GRAFT-G04, M0:1385-1406). Classe: magnitudini [SE]; shroud [REP]
page-verified; gamba di segno del debito THEOREM* ([T-DISC-2](i), scope
booking). Tightener: T-DISC → M-RED banda B-2 → predizione shroud
pre-registrata F2a → decisione build S-5F (utente, pending).

**(iv) Adeguatezza del mezzo: sizing vs ranking (R26)** — *il cuore
onesto del capitolo: la media dimostra di saper DIMENSIONARE, non ancora
di saper ORDINARE al percento.* BEST: **~1% a livello sizing** [REP] —
accordo area-ratio Paxson-Miki 6.54 vs ~6.5 (R26, registry :2147);
Harroun 1.25-flat letto ai suoi limiti verificati = nessuna
contraddizione misurata dell'adeguatezza di sizing. WORST: **"RANKING
THRESHOLD OPEN (R26)"** — i delta di contorno in-class sono FRAZIONI di
punto (scala Hoffman 0.04-0.34%; il nostro +0.51% in-class — CON il
caveat **band-underinclusion di record** stampato accanto [B3-C12]:
l'errore di rappresentazione di classe M→2M è sotto-coperto dalla
differenza J M-vs-2M, bound sistematico grezzo ~6e4 contro il surplus
2.0407e5, **~30% del datum**, M0:4216-4219 — il caveat È parte del
numero ovunque il numero compaia) contro
spread di configurazione di DECINE di punti: "the average could be blind
exactly at design-relevant scale". Harroun 1.25-flat è un dato di
NON-DISCRIMINAZIONE (nessuna spinta misurata, nessun 3D unsteady flared,
"2-D AND averaged" non isolato), NON una prova di cecità (M0:1346).
Tightener: M-RED (eps vs delta in-class) → R22-CFD-2 (coppia Harroun) →
R22-CFD-1.

**(v) Model-form** — *le barre del modello stesso: chimica congelata e
pressione di base.* BEST: classe few-%, prezzata e monitorata (bracket
frozen-vs-equilibrium al low end con ri-esecuzione per-champion, duty
P-F14, registry :1627; base pressure con chiusura a due regimi
dichiarata, transizione Pa/Pc ≈ 0.15, R8). WORST: **[T-EQBR] +6.3..+7.0%
sull'istanza interna misurata** ("can exceed claimed design deltas");
**base-pressure model-form UNPRICED su plug troncato**: Pb/Pa = 1
inammissibile in ENTRAMBI i regimi (base ~20% sotto ambiente in open
wake); NESSUNA misura di base plug-troncato RDE esiste nel corpus letto —
il trasferimento nozzleless→plug è "an ANALOGY, declared" (M0:1347).
Il vuoto R8 è ri-confermato dall'harvest C4: l'unica misura hot-fire di
base RDE è il datum Purdue V1.4 nozzleless (~0.59 atm CTAP), ed entrambi
i paper Harroun dichiarano verbatim il risultato negativo; il modello
classico puro-empirico porta banda [+19%, −15%] su dati freddi
(ORCH-HARV-2, M0:1430-1447). Tightener: P-F14 standing; R8 = procurement
esterno ("not ours"); R22-CFD-1 prezza il model-form accoppiato.

**(vi) OPTIMUM-SHIFT: value-adequacy ≠ optimum-adequacy** — *il canale
che risponde alla domanda dell'utente: come la fisica persa muove
l'ottimo stesso.* Il contenuto è uno SCHEMA a due vie, e la disciplina
è che NESSUN numero esiste (M0:1348):
- Via GRADIENTE: |argmax shift| ≤ delta/mu_curv, forma A-POSTERIORI —
  con delta = residuo di gradiente proiettato e mu_curv = pavimento di
  curvatura di J_TRUE; il carrier misurato (Hessiani TR-Newton di
  record, che sono Hessiani del funzionale RIDOTTO) lo istanzia SOLO
  sotto H-G6 (mu_eff = (mu_meas − b_E) − L_H); **delta E L_H sono
  UNDERIVED** — "NO argmax-shift number exists at any grade, and none
  from the measured carrier alone … the helical shock structure can move
  the TRUE argmax along design directions the reduced functional does
  not see, and no bound of record excludes it" (M0:1348, WORST cell).
- Via VALORE (l'unica dello schema il cui pavimento è legittimamente il
  carrier misurato as-is; il NUMERO richiede eps_U da M-RED, oggi
  F2-QUEUED [W2-R4]): |argmax
  shift| ≤ 2·sqrt(eps_U/mu_red), con mu_red legittimamente il pavimento
  misurato J_red as-is e eps_U = sweep-sup delle gambe di valore M-RED a
  classe SAMPLED-SUP (estimate); derivazione one-line di record
  (M0:2051-2077). Il tasso è Theta(sqrt(eps)): "value-level adequacy
  alone confines the shift only to O(sqrt(eps))" — solo la via gradiente
  può stringere alla scala dei delta in-class (M0:2062-2067).
- Geometria del feasible set: su set NONCONVESSO (anche connesso) la
  copertura del global argmax NON è reclamata da ALCUNA forma dello
  schema (H-G5/R-14; probe di record con violazione illimitata;
  M0:2078-2112).
- Marker empirici [ADV], nessun numero entra nello schema: shroud
  Paxson-Miki (canale (iii)); P-B flat-vs-peaked; P-C mid-ranking flips;
  P-A design-point miss (GRAFT-G07, M0:1449-1453); e l'esibizione
  classica Humphreys-Thompson-Hoffman 1971: scambiare la chiusura di
  base-pressure ha mosso l'altezza di base ottima ×2.45 e la pendenza di
  parete −13.26° → −3.08° muovendo la spinta di solo +0.26% — "the p_b
  closure moves the ARGMAX at O(1) with the VALUE nearly flat"
  (ORCH-HARV-3, M0:1455-1464).
- Regola di composizione: (vi) è un canale di OPTIMUM-adequacy, mai
  sommato con (i)-(v); compone solo attraverso lo schema delta/mu
  ([REV2-r1-19], M0:1476-1481). "A value-level bound is NEVER passed
  off as optimum coverage" (M0:1348, binding).

**Roll-up e headline di record** (M0:1466-1494): i canali NON sono
indipendenti e non si sommano; l'unico aggregatore legittimo è la misura
congiunta M-RED (famiglie F-c). BEST: on-ray, corpus-swirl, in-class —
gap plausibilmente SINGLE-DIGIT PERCENT (con good fitted sheet), canale
medio esattamente nullo (THEOREM*), debito di booking a 1.5-3% [SE].
WORST: off-ray >10% non escluso [SE]; la cecità a scala di
configurazione è la DIREZIONE peggiore documentata (linea shroud); le
uscite di classe non portano numero. "The bracket TIGHTENS in the
program order T-DISC → T-RED → M-RED → R22-CFD; nothing else tightens
it" (M0:1493-1494).

**Confine di classe (non canali) [W2-R8]:** il contenuto viscoso e di
separazione è FUORI dalla classe inviscid del censimento: "outside
inviscid class … NOT a K term — boundary named (separated-phase monitor,
T-T3-MAP(a)); no bound asserted" (M0:1886); i dati swirl esterni P-B sono
film-cooled con caveat dichiarato (M0:1388-1395). Il model-form viscoso
non è prezzato di record: il confine va detto, o la lista "canale per
canale" apparirebbe completa quando non lo è.

### 1.4 M-RED: la campagna che misura il residuo (findings_registry.yaml:2509-2517)

M-RED è lo strumento che muove i canali (ii)/(iii) da SCALING-ESTIMATE a
MEASURED per famiglia: gambe O5-lite (A)-(E) su famiglie certificate
F-a..F-d con quattro bande DERIVATE (non magiche): **B-1** Richardson su
St-ladder ≥4 punti; **B-2** debito E_theta in dmdot = rho u_x dA (misura
esattamente la coordinata di fibra di T-DISC); **B-3** massa del
complemento-finestra dello split di canale (J)/(H); **B-4** finestra
h-indipendente registrata sotto il pavimento di margine di dominio m0
(`docs/findings_registry.yaml:2512`; definizioni bande in
`docs/glossary.yaml:1495`). Stato: **F2-QUEUED**, entrambi gli esiti
pre-registrati positivi (protocollo T3-CONTROL), gira sotto G1, pin
bloccanti pre-run B-1/B-2 (righe contratto D.13) + convenzione a.c.-only
(J)/(H) (`docs/rde_nozzle_pipeline_decision_map.md:129`; catena di
consumo E28, :236). Esito classe-wide comunque (U)-gated
(`findings_registry.yaml:2512`).

### 1.5 Il fatto no-external-referee (M0:1322-1333)

Dichiarazione strutturale di record, header della tabella: "NO EXTERNAL
PUBLISHED REFEREE EXISTS for the per-phase thrust error: the literature
carries NO unsteady c_F datum that discriminates the 2D-per-phase-
averaged prediction against 3D-unsteady truth" — l'Harroun 1.25-flat è
quasi-cycle-averaged, verificato verbatim alla fonte 2026-08-20: è il
dato di NON-discriminazione, non un arbitro. CONSEGUENZA: la forchetta
si CHIUDE solo con il nostro R22-CFD o un procurement dedicato; fino ad
allora OGNI cella è bound/estimate-class, mai arbitrata esternamente.
I referee esistenti più vicini (P-B Fig. 15, P-C Figg. 13+20b) sono
nominati e SQUALIFICATI: same-solver URANS a media GLOBALE, verità non
esterna/sperimentale (GRAFT-G10, M0:1311-1320). Guardia aggiuntiva:
"best-of-sweep != argmax: no published work optimizes the true
3D-unsteady case" (ORCH-HARV-1, M0:1335-1339). [ADV]

---

## 2. Stato per-claim

Nota citazioni registry [W2-R11]: le cite :2026/:2147/:1925 sono le
righe M0 di record ([REV2-r1-17] line-verified all'epoca); nel registry
corrente il testo vive a +1 (:2027/:2148/:1926) — off-by-one ereditato
da M0, dichiarato per il retro-audit del deck.

| Claim | Classe | Ancora | Carrier / falsificatore |
|---|---|---|---|
| Le fibre della proiezione p-only sono non-degeneri: E_theta libero a parità di (P, h0, s, mdot) | THEOREM* (c1 G-a queued, c2 H-AM0 per-dataset) | M0:1030-1084 | Falsificatore: UN vincolo di record che determini E_theta da (P,h0,s,mdot) (M0:1079-1084) |
| J separa entro fibra single-signed (debito swirl esatto Gamma^2/r_e^2) | THEOREM* SCOPED booking-level, physical-h0-fixed; ramo DROP non compensato geometry-signed, degenerazione r_e=r_in | M0:1086-1139 | Probe di record r22f_v2_probe_r1_l0/l2 PASS; falsificatore ∂(mdot·u_e)/∂(Gamma^2) ≥ 0 (M0:1175-1178) |
| Scala del debito: 1.5-3% spinta (B2 fold) + B1 0.6-9% di p | SCALING-ESTIMATE [SE], etichettata, NON bound | M0:1140-1151 | M-RED banda B-2 la misura; falsificatore: famiglia certificata sotto la barra B-2 (M0:1178-1182) |
| Nessun raffinamento p-only recupera il pavimento entro-fibra; ranking inter-fibra unbounded | SCHEMA (gamba (b), premessa DR nominata; (U) OPEN) | M0:1210-1228 | Falsificatori a M0:1233-1237 |
| La media FULL-STATE per-fase è esonerata sull'asse fibra | SCHEMA (verdetto T-DISC-4(b)) | M0:1254-1259 | Esposizione residua = assi T-RED + forchetta (i)/(ii)/(iv), dichiarata |
| K esatto: la riduzione scarta esattamente 6 righe avvettive + atomi di fronte | DEFINITION + identità THEOREM* (sympy); completezza censimento G-f SCHEMA | M0:1786-1807 | Testimoni sympy judgeverify ITEM 3.1/§5.1 |
| K-bar = 0 fiberwise (nessun canale medio al primo ordine) | THEOREM* MINTED a grado record (BV pieno) | M0:1768-1773, 1833-1838 | Falsificatore f1: composito BV periodico con K-bar ≠ 0 (M0:1903-1904) |
| Esattamente due canali primo-ordine (J)/(H) | THEOREM* condizionato SBV (H-RED-2) | M0:1821-1830, 1840-1853 | Falsificatori f2-f4 (M0:1904-1909) |
| Magnitudini T-RED: Lambda 0.59-1.11·St_n; work 0.007-0.09; single-digit-% plausibile on-ray con fitted sheet; >10% non escluso off-ray | SCALING-ESTIMATE [SE] | M0:1844-1849, 1854-1862 | M-RED bande B-1/B-3; licenza on-ray X-T3QS-5F (F2) |
| delta (residuo gradiente) e L_H (residuo curvatura) | SCHEMA + deriver nominati; UNDERIVED — nessun numero ad alcun grado | M0:1911-1956, 2018-2026, 1348 | Deriver in ordine: X-T3QS-5F → C51-route-B → M-RED §3.6 rider |
| Via valore: shift ≤ 2·sqrt(eps_U/mu_red), tasso sqrt tight | SCHEMA (lemma probe-verified, 50 random + 4 adversarial) | M0:2051-2077 | eps_U = sweep-sup M-RED classe SAMPLED-SUP; H-G5 per istanza |
| Nonconvex feasible set ⇒ nessuna copertura global-argmax da alcuna forma | SCHEMA + probe (violazione illimitata isolata) | M0:2078-2112 | Rimedio (solo set DISCONNESSI): dominanza di valore cross-branch > 2·eps_U; su set connesso-nonconvesso la copertura branch-wise è UNDEFINED e nessuna forma la reclama (M0:2106-2118) [W2-R7] |
| Time-coupling: 0 esatto su classe certificata / class-exit senza numero | [T-T0P] SCHEMA condizionale; H-AM1 exit; PRACTICE al bordo | M0:1343 | Monitor T0-flatness + f_cycle (A32, registry :1925) |
| Sizing ~1% (Paxson-Miki 6.54 vs ~6.5); ranking threshold OPEN (R26) | [REP] esterno page-verified; soglia OPEN di record | M0:1346; registry :2147 | "decided by R22"; M-RED eps vs delta in-class |
| [T-EQBR] frozen-vs-eq +6.3..+7.0% istanza interna; base pressure UNPRICED su plug troncato (analogia dichiarata, R8) | misura interna + [REP] + ANALOGY dichiarata | M0:1347, 1430-1447 | P-F14 per-champion (registry :1627); R8 = procurement esterno |
| Shroud Paxson-Miki 58.1 → ~71.5 punti % di ideale a AR fisso, unexplained | [REP] page-verified (C25: findings_registry.yaml:2026) | M0:1345, 1350-1353 | Predizione shroud pre-registrata F2a; decisione S-5F (utente) |
| Harroun Fig. 18 = istanza fisica dei fronti interni azimuthally-fed | [ADV] page-verified (p. 669) | M0:1344, 1900-1902 | Magnitudine E5 DISPUTED-OPEN; decider = Delta x_s standoff |
| Nessun arbitro esterno pubblicato per l'errore di spinta per-fase | dichiarazione strutturale di record [ADV] | M0:1322-1333 | Chiusura solo via R22-CFD proprio o procurement |
| M-RED: bande derivate B-1..B-4, esiti pre-registrati entrambi positivi | carrier spec di record; PRACTICE (T3-CONTROL) | findings_registry.yaml:2509-2517; glossary.yaml:1495 | F2-QUEUED sotto G1; pin B-1/B-2 pre-run |

---

## 3. Gli APERTI

1. **delta UNDERIVED** (residuo a livello gradiente di design): nessun
   bound chiuso derivabile al record corrente; deliverable legittimo =
   SCHEMA + deriver nominati (M0:1953-1956). Owner/trigger: F2 —
   X-T3QS-5F, C51-route-B, M-RED §3.6 rider (M0:1946-1952).
2. **L_H UNDERIVED** (faccia curvatura del residuo, H-G6): finché non
   atterra, la via gradiente non licenzia numeri dal carrier misurato
   (M0:2018-2026; M0:1348). Stessi deriver, F2.
3. **R26 ranking threshold OPEN**: adeguatezza al ranking percent-level
   NON dimostrata; "decided by R22" (M0:1346). Owner: M-RED → R22-CFD-2.
4. **(U) uniformità OPEN due volte** ((U) + H-A1 class-wide): decisa dal
   teorema sub-scope S.22 shock-free (F2) + eps misurato (M0:1868-1869,
   1229-1232).
5. **Class exits senza numero di record**: aperiodicità/transizioni di
   modo (H-AM1), fronti slip-sheet (G9), correttore steady-sweep
   (G3-owned) — nessun numero asserito, guardie = monitor T0 + f_cycle
   (M0:1343). Owner: R22-CFD-1 (membership), lift G5/G9 (teoria F2).
6. **E5 magnitudine fronti azimuthally-fed DISPUTED-OPEN** — decider
   nominato: modulazione misurata dello standoff Delta x_s (M0:1885).
7. **Base pressure su plug troncato UNPRICED** (R8): nessuna misura
   esistente al mondo nel corpus letto; analogia dichiarata; procurement
   esterno, "not ours" (M0:1347, 1440-1447).
8. **H-G5 al S* margin-active OPEN** (stato di convessità del set
   KS-aggregato; residuo R-14) + critical cone O1-GATED (M0:2036-2043,
   2098-2100).
9. **M-RED non ancora eseguita**: F2-QUEUED con pin bloccanti B-1/B-2 e
   convenzione (J)/(H) (findings_registry.yaml:2509-2517).
10. **Decisioni utente pendenti a valle**: build S-5F (M0:1345, catena
    tightener) e scheduling R22-CFD (dossier presentato, non deciso;
    findings_registry.yaml:1467).
11. **Settore subsonico fuori scope di [T-DISC]** [W2-R9]: enunciati sul
    solo settore supersonic-map; il settore subsonico raggiunge la forma
    mixture ed è fuori scope del teorema, dichiarato (M0:1025-1028) — da
    dire se il deck consuma [T-DISC].
12. **G3 senza numero di kill (+ G4 nominato) [B3-G34]** (cella M-v/D-v):
    il gate di unsteadiness **G3** ("St|J1| large → rung-3 correction
    loop") è, verbatim D6 e verificato alla riga 2026-08-23,
    **"currently the only gate whose kill threshold cannot reject"**
    (`docs/rde_nozzle_development_plan.md:783-786`): il trigger "large"
    deve diventare un NUMERO con derivazione prima che parta A4. La via
    di chiusura è di record ed è **F5b**: "G3 unsteadiness trigger
    derived as a NUMBER BEFORE the corrector"
    (`docs/rde_nozzle_development_plan.md:271-273`, verificato alla
    riga) — oggi quel numero è ASSENTE, e l'assenza DICHIARATA è
    l'aperto (è anche il falsificatore del nodo N-M). Accanto va
    NOMINATO il **G4 DECOUPLING GATE** ("D2 error dominates →
    wave-frame objective", `docs/rde_nozzle_development_plan.md:787`):
    mai esercitato, nessuna soglia di record — la sua esistenza è la
    valvola strutturale se il residuo di riduzione domina. Owner: F5b
    (corrector nello scope VI.4bis(ii), cf. [B3-MI] §1.3(i)); eco
    roadmap in CH6 §1.5. Classe: PRACTICE/aperto dichiarato di piano.

---

## 3-bis. ANTENATI DIRETTI (lineage claims — nodi N-D / N-M) [B3-LIN]

Contratto di join [F-des-4]: ogni claim di novità dei nodi ospitati cita
≥1 LL-id del `LINEAGE_LEDGER.md` (lint 7); righe CANDIDATE fino al pass
del refuter C6.

**N-D (il residuo esatto della riduzione):**
- **LL-22 — convenzioni di media non dichiarate** (Liu Eq.14; quarta
  istanza in P-C `li_xu_lv_yu_zhou_2025`): il campo media senza dichiarare
  peso/denominatore — la nostra μ è l'unica PINNATA (T-O2). È l'antenato
  IN NEGATIVO del censimento K: chi non dichiara la media non può scrivere
  l'oggetto che la riduzione scarta. Il claim di assenza dell'operatore K
  esibito in forma chiusa resta query-bounded al corpus (§5.1).
- **LL-4 — Kaemming-Paxson 2018 EAP** (`kaemming_paxson_2018`): porta la
  DOMANDA (che errore fa la media?) al rung int-max, ma con le ipotesi di
  riduzione unstated/unpriced (M0:2537-2539) — antenato della domanda
  senza lo strumento (forchetta per-canale, classi di cella).

**N-M (la correzione di unsteadiness):**
- **LL-4**: il correttore P4 è "EAP's missing error bar" (M0:2537-2539) —
  l'antenato industriale definisce esattamente il buco che il corrector
  prezza.
- **LL-17 Rubino 2018** (`rubino_2018`) + **LL-18 Zahr-Persson 2016**
  (`zahr_persson_2016`): la macchina adjoint periodica (HB discrete
  adjoint duality-preserving period-averaged; adjoint fully-discrete
  sotto periodicità + verifica gradiente + monodromia) = antenati della
  **ROUTE GENERALE** del corrector (il lato O5/unsteady di VI.4bis(ii)),
  ciò che il programma specializza con la route cheap licensed sotto T0.
  **Decisione di scoping dichiarata (mandato B3, no-dup)**: LL-17/LL-18
  sono citati QUI solo sull'asse corrector/route-generale del nodo N-M;
  la loro genealogia rispetto all'adjoint per-fase del sistema di
  OTTIMALITÀ appartiene al nodo N-C (CH2, writer B7) — asse diverso,
  stesso ledger, nessuna duplicazione di claim.

---

## 4. Domande da panel

**(1) "Elencate la fisica che il 2D per-fase butta via, canale per
canale, con l'entità nota o dichiarata ignota di ciascuno."**
Risposta dal record — la tabella esiste ed è esattamente questa
([R22F-FORCHETTA], M0:1341-1348): (i) time-coupling: 0 esatto sulla
classe certificata (SCHEMA condizionale), uscite di classe SENZA numero
— dichiarato ignoto, non stimato; (ii) struttura azimutale: canale medio
esattamente nullo (THEOREM*), termine pressure-work 0.7-9% [SE] mentre la
parte avvettiva è SENZA numero di record — misurata da M-RED, bande
B-1/B-2 (M0:1883) [W2-R1], single-digit-%
plausibile on-ray con fitted sheet, >10% non escluso off-ray; (iii)
swirl: B2 1.5-3% spinta + B1 0.6-9% di p + B5 10-14 deg [SE], marker
peggiore shroud 58.1→71.5 punti [REP]; (iv) sizing supportato a ~1% su
un'istanza esterna page-verified [REP] (accordo 6.54 vs ~6.5), senza
contro-istanza misurata — mai "dimostrato" [W2-R2],
ranking threshold OPEN; (v) model-form: frozen +6.3..7.0% misurato
interno, base pressure UNPRICED su plug troncato (analogia dichiarata);
(vi) optimum-shift: SCHEMA, zero numeri per costruzione. Regola di
cella: nessuna cella sopra la propria classe di evidenza (M0:1305-1309);
i canali non si sommano (M0:1466-1475). Confine dichiarato: il contenuto
viscoso/di separazione NON è un canale della forchetta — fuori classe
inviscid, monitor di fase separata, NESSUN bound asserito (M0:1886);
model-form viscoso non prezzato di record [W2-R8].

**(2) "Il canale (vi): perché non avete NESSUN numero di argmax-shift e
come potete comunque affermare qualcosa?"**
Risposta onesta dal record: non abbiamo il numero perché i suoi due
ingredienti sono UNDERIVED — delta (residuo gradiente) e L_H (residuo
curvatura) — e asserirne uno "would exceed the held evidence class"
(M0:1348, 1953-1956). Ciò che POSSIAMO affermare è a grado SCHEMA con
struttura provata: (a) la forma del bound è nota (|shift| ≤ delta/mu_curv,
lemma argmax-shift fortemente concavo, condizioni di soundness (1)-(3)
esplicite, M0:1957-1976); (b) la via valore è eseguibile sul carrier
misurato (mu_red as-is, "executable on the measured carrier today"
riferito al LATO carrier, M0:2074-2075) NON APPENA M-RED consegna eps_U
(sweep-sup delle gambe di valore (A)-(B), classe SAMPLED-SUP,
M0:2056-2058) — oggi nessun numero: mancano eps_U e i check a-posteriori
(basin radius R-12, H-G5, coverage sweep) [W2-R4]: |shift| ≤
2·sqrt(eps_U/mu_red)
(derivazione one-line, probe verificata tight; M0:2051-2077) — con il
limite dichiarato che il tasso sqrt non raggiunge la scala dei delta
in-class; (c) i deriver di delta e L_H sono NOMINATI e ordinati in F2
(M0:1946-1952). In più il rischio è ancorato empiricamente senza fingere
numeri: l'esibizione Humphreys 1971 (argmax mosso ×2.45 con valore
+0.26%; ORCH-HARV-3, M0:1455-1464) e i marker [ADV] di GRAFT-G07 —
"no number enters the delta/mu schema" (M0:1452-1453). La disciplina è
il claim: value-adequacy non viene MAI spacciata per optimum-coverage
(M0:1348, binding).

**(3) "Harroun 2021 dice che il cycle-average è cieco al ranking: perché
il vostro programma non è morto lì?"**
Correzione dal record, verificata verbatim alla fonte (2026-08-20): il
dato Harroun 1.25-flat NON dimostra cecità — è un dato di
NON-DISCRIMINAZIONE ai suoi limiti verificati: nessuna spinta misurata,
nessun 3D-unsteady flared, il fattore "2-D AND averaged" non isolato,
nessuna barra (M0:1346; advisory :800-805). E in direzione opposta il
record ha anche il dato positivo: adeguatezza al SIZING ~1% (Paxson-Miki
6.54 vs ~6.5, R26 [REP], registry :2147). La frase onesta è: sizing
supportato a ~1% su un'istanza esterna page-verified [REP], senza
contro-istanza misurata [W2-R2]; ranking threshold OPEN di record (R26);
e il programma ha
costruito lo strumento che decide — M-RED misura eps contro i delta
in-class, e R22-CFD-2 è scopato di record sulla coppia Harroun
("field-facing demonstration on the Harroun pair", registry :1462;
tightener M0:1346) con dossier di scheduling PRESENTATO e decisione
utente pendente (registry :1467) — la pre-registrazione con esiti
dichiarati (T3-CONTROL) appartiene a M-RED, non a R22-CFD [W2-R3]. Il programma non è morto lì perché nessun
dato pubblicato lo uccide (no external referee, M0:1322-1333) E perché
non ha mai claimato l'adeguatezza al ranking: l'ha messa a registro come
soglia aperta con owner e trigger.

**(4) "Lo shroud Paxson-Miki (13+ punti a pari area ratio): se il 2D
medio non lo vede, a che serve il vostro ottimo?"**
Risposta dal record, in tre parti. (a) Il numero è NOSTRO alleato, non
nostro imbarazzo: è REGISTRATO nel record come "worst-direction marker"
obbligatorio del canale (iii) — 58.1% → ~71.5% dell'ideale a AR fisso,
"larger than the entire area-ratio design line, declared unexplained by
the authors" (M0:1345) — e come candidato swirl-breaker (debito E_theta
+ asimmetria di recupero contro il plug). (b) Il meccanismo candidato è
esattamente la coordinata di fibra che T-DISC ha isolato a teorema e che
la banda B-2 di M-RED misura (M0:1013-1015): il programma ha trasformato
l'anomalia in una PREDIZIONE PRE-REGISTRATA F2a (catena tightener del
canale (iii), M0:1345) — se il nostro framework spiega la migrazione
shroud, la fisica "invisibile" diventa contenuto del funzionale; la
decisione build S-5F è dell'utente, pending. (c) Onestà sul limite:
"configuration-scale effects the 2D-per-phase average could be blind to"
è testo di record (M0:1345) — per questo l'ottimo di programma viene
consegnato con la forchetta attaccata e con il template condizionale
F5a per-surrogato "gain net of 2·eps_G, eps_G = measured/assumed per
family" su ogni certificato di guadagno G2-class (M0:1207-1209; la forma
M0:1238-1240 scopa il caso p-only) [W2-R6]. OPEN dichiarato: la spiegazione dello
shroud oggi non esiste a nessun grado — esiste il candidato registrato e
il suo test.

**(5) (attesa naturale) "Il vostro K-bar = 0 non è solo la periodicità?
Cosa compra davvero?"**
Dal record: sì, la prova è la nullità della massa segnata della derivata
distribuzionale periodica — ma il contenuto comprato è la STRUTTURA a
valle: nessun canale mean-field al primo ordine, ed esattamente DUE
canali residui (J)/(H) condizionati a SBV (M0:1833-1853), che è ciò che
rende M-RED una misura a bande derivate invece di un fit cieco (B-3
misura proprio la massa del complemento dello split; glossary.yaml:1495).
Il grado è dichiarato: THEOREM* mintato, con falsificatore macchina f1
(M0:1903-1904).

**(6) (attesa naturale) "Chi vi fa da arbitro esterno?"**
Nessuno, e lo dichiariamo noi per primi: "NO EXTERNAL PUBLISHED REFEREE
EXISTS for the per-phase thrust error" (M0:1322-1333); i candidati più
vicini sono nominati e squalificati (GRAFT-G10, M0:1311-1320). La
forchetta chiude solo via R22-CFD nostro o procurement dedicato — fino
ad allora ogni cella è bound/estimate-class e la presentazione lo dice.

---

## 5. Cosa deve dire il deck (2-3 slide)

1. **"Sappiamo ESATTAMENTE cosa buttiamo via"** — il residuo di
   riduzione è un operatore esplicito K, non una speranza: 6 righe
   avvettive + atomi di fronte, identità verificate a macchina
   (DEFINITION + THEOREM*, M0:1786-1807). Nel corpus letto (litmap di
   record) non abbiamo trovato l'oggetto scartato esibito in forma
   chiusa — claim di ASSENZA query-bounded al corpus, non di novità
   assoluta [W2-R5]. [classe: DEFINITION/
   THEOREM*; completezza censimento G-f SCHEMA, da dire]
2. **"Il teorema condanna la riduzione sbagliata ed esonera la nostra"**
   — p-only NON adeguata al ranking percent-level su dati con swirl, con
   zero CFD (T-DISC, THEOREM*/SCHEMA); la media full-state per-fase non
   fattorizza per pi ed è esonerata su quell'asse (M0:1242-1259).
   [THEOREM* con scope booking dichiarato a voce]
3. **La forchetta come slide unica a 6 canali** — BEST/WORST per canale
   con classe stampata in cella: medio nullo per teorema, pressure-work
   0.7-9% [SE] con parte avvettiva senza numero di record (la misura
   M-RED) [W2-R1], single-digit-%
   plausibile on-ray, >10% non escluso off-ray, sizing supportato a ~1%
   su un'istanza esterna [REP] [W2-R2],
   ranking OPEN, class-exits senza numero (M0:1341-1348, headline
   :1482-1494). La slide DEVE mostrare le classi ([SE]/[REP]/THEOREM*):
   è il differenziatore, non un disclaimer.
4. **Optimum-shift: la disciplina è il claim** — nessun numero di
   argmax-shift esiste a nessun grado, PERCHÉ delta e L_H sono underived
   con deriver nominati e ordinati (F2); la via valore dà solo
   O(sqrt(eps)) e il suo numero attende eps_U da M-RED (F2-QUEUED)
   [W2-R4]; ancora storica Humphreys 1971 (argmax ×2.45, valore
   +0.26%) come istanza del meccanismo (M0:1348, 1455-1464, 2062-2067).
   [SCHEMA; marker [ADV]]
5. **Il gap non resta un'opinione: M-RED lo misura** — campagna
   pre-registrata (T3-CONTROL, entrambi gli esiti positivi), bande
   DERIVATE B-1..B-4, F2-QUEUED sotto G1; ordine di serraggio unico e
   dichiarato: T-DISC → T-RED → M-RED → R22-CFD
   (findings_registry.yaml:2509-2517; M0:1493-1494). [carrier spec di
   record + PRACTICE]
6. **No-external-referee, detto da noi per primi** — la letteratura non
   contiene il dato che arbitri l'errore per-fase; per questo il
   programma costruisce il proprio arbitro invece di citarne uno
   inesistente (M0:1322-1333). Ogni guadagno futuro esce col template
   F5a per-surrogato "net of 2·eps_G, eps_G = measured/assumed per
   family" (M0:1207-1209; M0:1238-1240 = caso p-only) [W2-R6].
   [dichiarazione strutturale di record]

---

## 6. STORIA

Trittico condizionale [V2-R2] (writer B8a, W-B.2, 2026-08-23).

Ogni battuta: DATA + PROCESSO + VERDETTO (vincolo §5-bis). Nota di
perimetro: il nucleo di questo capitolo è nato DENTRO la Fase D
(S-FOUNDATIONS-C4, 2026-08-20/21) — per questi argomenti la battuta 2 in
ramo (a) cita i file phaseD col verdetto del giudice, e la refutazione
until-dry è essa stessa la seconda prova.

**T-1. La correzione formal-first (genesi della decomposizione R22).**
- *Battuta 1*: 2026-08-13 — correzione metodologica dell'UTENTE: la
  review di letteratura aveva importato l'epistemologia empirica del
  campo ("R22 si decide con un esperimento CFD"); ordine = decomposizione
  formale-prima, CFD ri-scopato a residuo irriducibile. Riga di record:
  `docs/findings_registry.yaml:1459-1468`
  (`theory:r22-formal-decomposition`, mechanism
  `epistemology-bias-from-literature`); memoria standing
  `formal-first-epistemology`. PROCESSO: direttiva utente a registro.
  VERDETTO: T-DISC/T-RED/M-RED/R22-CFD = il piano di record, "no longer
  the decider".
- *Battuta 2*: (c) NON-RIDERIVATO (è una decisione metodologica, non un
  enunciato); doppia prova alternativa = la decomposizione ESEGUITA a
  convergenza in C4 (2026-08-20/21): i quattro oggetti nominati sono
  atterrati con giudici (`blocco3/VERDICT_r22f.md`,
  `blocco3/VERDICT_escalation_c4.md`, 2026-08-20). PROCESSO: esecuzione
  del piano con refutazione. VERDETTO: direttiva CONSUMATA con evidenza.
- *Battuta 3*: classe finale: standing directive + landing M0 C4.

**T-2. [T-DISC] — fiber-separation (condanna p-only, esonero full-state).**
- *Battuta 1*: finestra C4, 2026-08-20 — PART 1 del centerpiece
  (`phaseD/phaseD_r22f_centerpiece.md:108-431`, mtime 2026-08-20; mandato
  = riga registry `theory:r22-formal-decomposition`). PROCESSO:
  derivazione formale author-draft con pin [REV2-r1-1] e prova per
  citazione (MS-T-FLUXNULL, MS-T-SKE, K̄=0). VERDETTO: THEOREM*/SCHEMA
  per gamba come stampato.
- *Battuta 2*: (a) RIDERIVATO-PIENO in Fase D — 4 round × 3 lenti
  (L0/L1/L2) = 66 findings (4 BREAK, 23 REPAIR), 14 probe eseguiti dai
  refuter (probe di record `r22f_v2_probe_r1_l0_fiber_sign_2eps.py`,
  `r22f_v2_probe_r1_l1_atom_mass.py`, ecc.); giudice
  `blocco3/VERDICT_r22f.md:508-521` (2026-08-20): NOT-DRY-AT-CAP ma
  APPROVED FOR LANDING, labels §1 = autorità unica; escalation E-1..E-4
  DRY + E-5 0 BREAK unanime, 53/53 findings SUSTAINED
  (`blocco3/VERDICT_escalation_c4.md:542-553`, 2026-08-20). PROCESSO:
  refutazione avversaria multi-lente con probe. VERDETTO: sostenuto.
- *Battuta 3*: landing M0 2026-08-21 (chiusura C4, gate NOTHING-LOST
  dual-seed PASS): [T-DISC-1] THEOREM* (c1/c2 nominati), [T-DISC-2]
  split-grade, [T-DISC-3]/[T-DISC-4] SCHEMA (M0:977-1280). Classi finali
  come §2.

**T-3. [T-RED] — l'operatore K e K̄ = 0.**
- *Battuta 1*: doppia radice datata: (i) le sei righe K nascono come
  D.18 [MS-DEF-KRES] del piano mean-swirl — panel 2026-08-11
  (`validation/ADVISORY_mean_swirl_panel_2026-08-11.md`) formalizzato in
  Fase D (`phaseD/phaseD_meanswirl_formalization.md`, mtime 2026-08-19);
  (ii) K̄ = 0 confermato UNCONDITIONAL dal verifier del panel swirl5f
  (finestra parallela 2026-08-17→19, `DISPATCH_swirl5f.md:64`).
  PROCESSO: panel + formalizzazione + verifier sympy. VERDETTO: identità
  riga-per-riga machine-witnessed (sympy PASS).
- *Battuta 2*: (a) RIDERIVATO-PIENO in Fase D — PART 2 del centerpiece
  (`phaseD_r22f_centerpiece.md:432-1182`) con saldatura testuale a D.18
  (:459-481), tre derivazioni indipendenti in-panel del censimento righe
  + doppia derivazione a mano L1 + judgeverify ITEM 3.1; giudice
  `VERDICT_r22f.md:77` (2026-08-20). PROCESSO: derivazioni indipendenti
  convergenti + refuter. VERDETTO: DEFINITION + identità THEOREM*;
  completezza = G-f SCHEMA ("grades NOT inflated").
- *Battuta 3*: K̄ = 0 **MINTED a grado record** al landing C4 2026-08-21
  (prova a penna + testimone macchina su BV pieno, M0:1768-1773,
  :1833-1838); "esattamente due canali (J)/(H)" THEOREM* condizionato
  SBV. Classi finali come §2.

**T-4. [R22F-FORCHETTA] — i sei canali.**
- *Battuta 1*: finestra C4, 2026-08-20 — PART 5 del centerpiece
  (:1458-1743), mandato utente verbatim in testa ("mi devi dare
  onestamente quale è la forchetta da aspettarsi..."). PROCESSO: tabella
  bound-or-estimate per cella con regola "NO cell above its held evidence
  class". VERDETTO: per-cella, mai aggregata.
- *Battuta 2*: (a) RIDERIVATO-PIENO in Fase D — i round refuter hanno
  colpito e riparato la tabella (qualificatore good-fitted-sheet caduto e
  RESTAURATO in tre siti dopo tre round, :1745-1755; header
  no-external-referee verificato verbatim alla fonte 2026-08-20);
  giudice `VERDICT_r22f.md:106-122` (2026-08-20). PROCESSO: refutazione
  multi-round con riparazioni tracciate. VERDETTO: sostenuta con residui
  RES-CAP nominati.
- *Battuta 3*: landing M0 2026-08-21 (M0:1283-1494) con i graft harvest
  C4 (GRAFT-G03/G04/G07, ORCH-HARV-1/2/3 — letteratura 2026-08-20/21) e
  regola di composizione [REV2-r1-19]. Classi finali per cella come §1.3.

**T-5. Il canale (vi): delta e L_H UNDERIVED (optimum-shift).**
- *Battuta 1*: finestra C4, 2026-08-20/21 — schema a due vie con
  derivazione one-line della via valore (M0:2051-2077) e dichiarazione
  UNDERIVED per delta/L_H con TRE deriver nominati in ordine
  (M0:1946-1952, :2018-2026). PROCESSO: derivazione parziale +
  dichiarazione onesta del non-derivato. VERDETTO: SCHEMA; "NO
  argmax-shift number exists at any grade".
- *Battuta 2*: (c) NON-RIDERIVATO — per costruzione: il residuo dichiara
  se stesso underived. Doppia prova alternativa SULLA DICHIARAZIONE:
  escalation delta-r4 (RES-CAP-1) refereed a 0 BREAK unanime con 3 REPAIR
  judge-verified (`blocco3/VERDICT_escalation_c4.md`, 2026-08-20; probe
  `esc_probe_r4delta_*.py`) + probe nonconvex con violazione illimitata
  isolata (M0:2078-2112). PROCESSO: escalation a forma piena. VERDETTO:
  la dichiarazione di underivedness regge; il numero resta ASSENTE per
  costruzione (owner F2, deriver ordinati) — non un finding: aperto
  strutturato di record.
- *Battuta 3*: classe finale SCHEMA su entrambe le route; RES-CAP-1
  SCARICATO in chiusura C4 (2026-08-21, PROGRESS ORA :19-20).

**T-6. M-RED e il fatto no-external-referee.**
- *Battuta 1*: finestra C4, 2026-08-20 — spec M-RED PART 3 del
  centerpiece (:1184-1391) con bande B-1..B-4 DERIVATE; riga findings
  `docs/findings_registry.yaml:2509-2517`; header strutturale
  no-external-referee (M0:1322-1333) con Harroun 1.25-flat verificato
  verbatim alla fonte 2026-08-20. PROCESSO: spec di carrier con
  protocollo T3-CONTROL, entrambi gli esiti pre-registrati positivi.
  VERDETTO: PRACTICE (spec).
- *Battuta 2*: (c) NON-RIDERIVATO come esecuzione (la campagna è
  F2-QUEUED, mai girata); doppia prova alternativa SULLA SPEC: ogni banda
  è stata riparata da probe refuter di record (:1237-1374) e il giudice
  ha coperto la PART 3 (`VERDICT_r22f.md:90-97`, 2026-08-20); i pin
  bloccanti B-1/B-2 vengono dal dispatch swirl5f (2026-08-19).
  PROCESSO: refutazione della spec. VERDETTO: spec sostenuta; esecuzione
  = duty F2 sotto G1, esito class-wide (U)-gated.
- *Battuta 3*: classe finale PRACTICE/F2-QUEUED; "the bracket TIGHTENS in
  the program order T-DISC → T-RED → M-RED → R22-CFD; nothing else
  tightens it" (M0:1493-1494).

---

## 7-DWR. POSIZIONAMENTO / CONFORMITY (cella D-ii; owner B3) [B3-P7]

La cella: perché la contabilità dell'errore di riduzione è una FORCHETTA
per-canale "a mano" con fisica nominata, e non un estimator goal-oriented
di classe DWR.

**(a) STRUMENTI — forchetta per-canale vs DWR goal-oriented.**
- *Mondo-SOTA (id registry)*: `wanted_becker_rannacher_2001` — il canone
  dual-weighted residual (menu pubblicato degli operatori di enrichment,
  pp.40-41, con effectivity misurate); `venditti_darmofal_2000` — adjoint
  error quasi-1D, la forma two-level fine-space residual;
  `wanted_fidkowski_darmofal_2011` — la review output-based adaptation.
- *Cosa usiamo*: per l'errore di RIDUZIONE/modello, la forchetta
  per-canale a fisica nominata [R22F-FORCHETTA] (M0:1283-1494), regola di
  cella binding "NO cell above its held evidence class" (M0:1305-1309);
  per l'errore di DISCRETIZZAZIONE del march, il DWR è ADOTTATO davvero —
  target primary con AD-weight discreto + referee Richardson/GCI
  permanente (riga C11, `docs/choice_ledger.yaml:269-279`).
- *Perché per-canale con fisica nominata*: (1) il DWR presuppone un DUALE
  COMPUTABILE del problema di riferimento; per l'errore di riduzione il
  riferimento è il 3D-unsteady VERO, il cui residuo a livello gradiente è
  delta UNDERIVED e senza arbitro esterno pubblicato (M0:1953-1956;
  M0:1322-1333) — un "DWR sulla riduzione" fingerebbe esattamente il
  duale che il record dichiara di non avere; (2) i sei canali hanno
  fisica DISTINTA (time-coupling / azimutale / swirl / adequacy /
  model-form / optimum-shift), ciascuno con owner, classe e falsificatore
  propri — un aggregato a numero singolo cancellerebbe la struttura che
  la disciplina di cella impone (i canali NON si sommano, M0:1466-1481);
  (3) dove il duale computabile ESISTE (la discretizzazione del march) il
  programma usa il DWR sul serio (C11) — la spartizione è PER ASSE
  (model-form vs discretizzazione), non un rifiuto del DWR.

**DECISION CARD — contabilità dell'errore di riduzione (6 campi, §1g):**
1. **Scelta**: forchetta per-canale a fisica nominata [R22F-FORCHETTA]
   (M0:1283-1494) come contabilità dell'errore di riduzione/model-form.
   Nessuna riga choice_ledger propria (dichiarato): la riga estimator
   C11 (`docs/choice_ledger.yaml:269-279`) governa l'asse DISTINTO della
   discretizzazione.
2. **Alternative censite (data+fonte)**: DWR/goal-oriented
   (`wanted_becker_rannacher_2001`, `venditti_darmofal_2000`,
   `wanted_fidkowski_darmofal_2011`) — censite dal panel C9/C11
   (2026-08-19, PANEL_C9C11.md + VERDICT_C9C11_supplement.md) e dalla
   wave-1 S-FOUNDATIONS (2026-08-19, VERDICT_wave1.md §2.4); retro-sweep
   ancore Becker-Rannacher/Venditti-Darmofal 2026-08-20.
3. **Verdetto + perché**: per-canale — il duale del problema VERO non è
   computabile al record corrente (delta/L_H underived, no external
   referee); i canali portano classi/owner/falsificatori distinti; DWR
   adottato sull'asse dove il suo duale esiste (C11). Spartizione per
   asse, dichiarata.
4. **RECENCY/SOTA check**: censimento DWR 2026-08-19 (panel + wave-1),
   con `wanted_fidkowski_darmofal_2011` (review di campo) su disco e
   consumo dichiarato per asse; nessuna forma DWR per model-form error di
   riduzione unsteady→per-fase trovata in registry al check 2026-08-23.
   **ATTUALE(registry 174 + ledger C11, 2026-08-23)**.
5. **Falsificatore**: un duale computabile del problema vero (o un
   surrogato certificato del suo gradiente) che produca un bound
   per-design più stretto della forchetta a parità di classe di evidenza;
   oppure M-RED che misura un canale fuori banda (la forchetta si ri-tara,
   M0:1178-1182).
6. **Trigger di ri-esame (finestra)**: F2 — M-RED (bande B-1..B-4,
   F2-QUEUED) + F2-C11-ESTIMATOR-CAMPAIGN leg (b); **finestra F2-entry**.

**DECISION CARD — route del corrector O(St) (cella M-i; 6 campi, §1g):**
1. **Scelta**: corrector = perturbazione dello SWEEP STEADY sull'ancora
   wave-frame (one linearized solve), specializzazione LICENZIATA quando
   T0 applica; route generale unsteady (O5) sempre in pipeline — M0
   VI.4bis(ii) (:3145-3150). Nessuna riga choice_ledger propria: direttiva
   pinnata di record (S5/S6, 2026-07-16; re-scoping memoria
   periodic-wave-data-scope), dichiarato.
2. **Alternative censite (data+fonte)**: (a) confronto unsteady pieno O5
   (route generale, VIVA in pipeline); (b) macchina adjoint periodica
   HB/fully-discrete (`rubino_2018`, `zahr_persson_2016`) — censite dallo
   sweep lineage W-B.0 (2026-08-23, LINEAGE_SWEEP_MATRIX part2, righe
   LL-17/LL-18) e dalla litmap §b6 (time-homogenization / quasi-steady
   validity).
3. **Verdetto + perché**: both-routes con gate DATA-DRIVEN (mai
   assunzione strutturale — emendamento utente nell'HEADER di VI.4bis,
   M0:3131-3137: "periodic structure is EXPLOITED AT RUNTIME when
   certified, never assumed structurally" [fix WB1-C3-08]): la route
   cheap è esatta al primo ordine sotto T0 certificato e costa un solve
   linearizzato; "a licensed specialization, not a replacement".
4. **RECENCY/SOTA check**: direttiva 2026-07-16, re-scoping 2026-08-11;
   lo sweep lineage del 2026-08-23 non ha esibito una route più economica
   CON certificato (LL-17/LL-18 = route generale, non cheap). Check
   2026-08-23. **ATTUALE(registry + litmap b6 + LINEAGE_LEDGER,
   2026-08-23)**.
5. **Falsificatore**: il monitor T0-flatness rigetta la purezza di modo
   (licenza cheap revocata, route generale obbligata); o residuo del
   corrector oltre le barre O(St) sul bench O5-lite.
6. **Trigger di ri-esame (finestra)**: **F5b** — G3 trigger derivato come
   NUMERO PRIMA del corrector (D6:271-273); finestra F5b (con G3/G4 come
   aperto dichiarato, §3.12).

**(b) SENSO.** Il campo RDE prezza l'errore steady-vs-transient come DATO
puntuale di campagna — NUAA `li_xu_lv_lv_song_2023` (2.8% uniforme ≤60%
trunc), `li_xu_lv_yu_zhou_2025` (0.2-1.5%, un flip mid-ranking) — mai
come contabilità per-canale con classi di evidenza; la comunità
output-based (Becker-Rannacher → Venditti-Darmofal → Fidkowski-Darmofal)
possiede l'errore di DISCRETIZZAZIONE, non il model-form di riduzione. Il
gap che la cella occupa: una contabilità dell'errore di RIDUZIONE
per-canale, classe-dichiarata, con misura pre-registrata (M-RED) —
query-bounded al corpus (lint 7; join §3-bis).

**(c) STANDARD DI RIFERIMENTO.** Asse **§C-2** (classe GRADE): ogni cella
della forchetta porta la propria classe di evidenza (THEOREM*/[SE]/[REP]/
[ADV]) con la regola binding "NO cell above its held evidence class"
(M0:1305-1309) — conformità piena alla STRUTTURA GRADE (livello
dichiarato + ragioni di upgrade/downgrade); divergenza dichiarata: i
livelli sono le classi R4 del programma, non i domini clinici. Asse di
supporto **§C-6** (assertion-evidence): la slide-forchetta mostra le
classi in cella come differenziatore, non come disclaimer (§5.3).

---

## Disposizione riparazioni (onda 2)

Onda 2 eseguita 2026-08-23 su REFUTE_CH3.md (verdetto
REGGE-CON-RIPARAZIONI, 0 BREAK, 13 finding). Ogni ancora citata dal
refuter ri-aperta alla fonte prima dell'edit (read-then-quote):
M0:1344/1856-1858/1883 (R1), M0:1346/1309 (R2), registry :1462/:1467
(R3), M0:2051-2077 (R4), M0:1207-1209/1238-1240 (R6), M0:2106-2118 (R7),
M0:1886 (R8), M0:1025-1028 (R9), M0:1343 (R13), registry
:2027/:2148/:1926 (R11 — off-by-one confermato).

| Finding # | Classe | Disposizione |
|---|---|---|
| 1 | REPAIR (alta) | APPLICATO [W2-R1] — Q1 + slide 3: work-term 0.7-9% separato dalla parte avvettiva senza numero di record (M0:1883 verificata) |
| 2 | REPAIR (alta) | APPLICATO [W2-R2] — Q1, Q3, slide 3: "dimostrato" sostituito con "supportato su un'istanza esterna [REP]" (regola di cella M0:1309 verificata) |
| 3 | REPAIR (media) | APPLICATO [W2-R3] — Q3: "pre-registrato" corretto in "scopato di record, dossier presentato, decisione utente pendente" (registry :1462/:1467 verificate) |
| 4 | REPAIR (media) | APPLICATO [W2-R4] — §1.3 via valore, Q2(b), slide 4: eseguibilita' scopata al lato carrier; il numero attende eps_U da M-RED + check a-posteriori (M0:2056-2058, 2074-2075 verificate) |
| 5 | REPAIR (media) | APPLICATO [W2-R5] — slide 1: claim di novita' riformulato come claim di assenza query-bounded al corpus letto |
| 6 | REPAIR (bassa) | APPLICATO [W2-R6] — Q4(c) + slide 6: template ri-ancorato a F5a per-surrogato M0:1207-1209; M0:1238-1240 citata solo per il caso p-only (entrambe verificate) |
| 7 | REPAIR (bassa) | APPLICATO [W2-R7] — tabella §2: caveat TAIL [REV2-r4-2](d) aggiunto (branch-wise UNDEFINED su connesso-nonconvesso, M0:2113-2118 verificata) |
| 8 | GAP (alta) | APPLICATO [W2-R8] — paragrafo di confine inviscid/viscoso in §1.3 + frase in Q1 (M0:1886 verificata) |
| 9 | GAP (media) | APPLICATO [W2-R9] — scope supersonic-map in §1.1 + voce 11 negli APERTI (M0:1025-1028 verificata) |
| 10 | GAP (media) | APPLICATO [W2-R10] — box "la riduzione in 3 mosse" + mini-glossario premessi al §1 |
| 11 | NOTE | APPLICATO [W2-R11] (variante dichiarativa) — nota off-by-one registry in testa al §2; cite di M0 lasciate intatte per fedelta' al record, drift dichiarato per il retro-audit |
| 12 | NOTE | APPLICATO [W2-R12] — "il campo confonde" sostituito con la forma ancorata (tensione R26, registry :2148) |
| 13 | NOTE | APPLICATO [W2-R13] — scoping Cor 5.1 (cl(Omega_march), slip-free) restaurato nella voce (i) BEST (M0:1343 verificata) |

---

## DECK FEED

Asserzioni candidate-slide (assertion-evidence: frase piena + ancora +
classe), compilate per lo storyboard v3 — che joina QUI, non ri-legge il
capitolo (contratto §3 emendamento).

1. "Il residuo della riduzione è un operatore ESPLICITO K — 6 righe
   avvettive + atomi di fronte, identità verificate a macchina — non una
   speranza." — M0:1786-1807 — DEFINITION + THEOREM* (censimento G-f
   SCHEMA, da dire).
2. "Il canale medio del residuo è esattamente NULLO; sopravvivono
   esattamente due canali al primo ordine, (J) e (H)." — M0:1833-1853 —
   THEOREM* mintato (clausola SBV H-RED-2 dichiarata).
3. "Il teorema condanna la riduzione a sola pressione con ZERO CFD, ed
   esonera — su quell'asse — la media full-state che usiamo." —
   M0:1242-1259 — THEOREM*/SCHEMA (scope booking a voce).
4. "La forchetta a 6 canali con la CLASSE stampata in ogni cella; i
   canali non si sommano; il +0.51% porta il suo band-underinclusion
   (~30% del datum) stampato accanto." — M0:1341-1348, 1466-1481,
   4216-4219 — classi per cella ([SE]/[REP]/THEOREM*).
5. "Nessun numero di argmax-shift esiste a nessun grado — delta e L_H
   sono underived con deriver nominati e ordinati: la disciplina È il
   claim." — M0:1348, 1953-1956, 1946-1952 — SCHEMA.
6. "Nessun arbitro esterno pubblicato esiste per l'errore di spinta
   per-fase — lo dichiariamo noi per primi, e costruiamo l'arbitro:
   M-RED, bande DERIVATE B-1..B-4, esiti pre-registrati." —
   M0:1322-1333; findings_registry:2509-2517 — dichiarazione strutturale
   + carrier spec (PRACTICE T3-CONTROL).
7. "G3 è oggi l'unico gate il cui kill threshold non può rigettare; F5b
   lo chiude derivando il trigger come NUMERO prima del corrector — e lo
   diciamo noi." — D6:783-786, 271-273 — aperto dichiarato di piano
   (PRACTICE).
8. "Il corrector è una perturbazione dello sweep STEADY (one linearized
   solve), licenza data-driven sotto T0; la route generale unsteady resta
   in pipeline." — M0:3145-3150 (VI.4bis(ii)) — direttiva di record.
9. "Per il model-form: forchetta per-canale a fisica nominata; per la
   discretizzazione: DWR adottato davvero (C11, AD-weight + referee) —
   spartizione per asse, dichiarata." — M0:1283-1494;
   choice_ledger:269-279 — scelta con card (§7-DWR).
10. "B-lite è il metro esatto CHEAP del residuo rung-2: arbitra i deriver
    a costo di march, senza camera." — M0:3027-3044 (verbatim
    :3037-3038) — [S-BLITE] SCHEMA, brick G12-L1-3D nominato.
