# CH5 — Letteratura e posizionamento: i 4 metodi, la genealogia, i gap

Capitolo della RICOSTRUZIONE CRITICA S-PRES (2026-08-22). Stadio di
confronto: record aggiudicato (SYNTHESIS arrivi C4, literature map,
harvest C4, advisory litmap). Questo capitolo NON aggiudica nulla di
nuovo: ricostruisce, ancora, dichiara gli aperti. Arco di consumo:
storyboard v3 deck ESA + banca Q&A red-team + mappa riutilizzabile F2+.
Regola di consumo permanente ereditata: **CT-6** — nessun numero dei
paper P-A..P-D entra in bande, barre o posizioni referee nostre;
solo meccanismo/topologia/scala-gap, sempre etichettati [ADV]
(validation/sfoundations_raws_2026-08-13/blocco3/SYNTHESIS_nozzle_rde_arrivals.md:158-163).

Abbreviazioni file (tutti sotto la root repo):
- SYN = validation/sfoundations_raws_2026-08-13/blocco3/SYNTHESIS_nozzle_rde_arrivals.md
- LM  = docs/rde_nozzle_literature_map.md
- THH = validation/sfoundations_raws_2026-08-13/blocco3/THROAT_FIELD_HARVEST_c4.md
- BPH = validation/sfoundations_raws_2026-08-13/blocco3/BASE_PRESSURE_HARVEST_c4.md
- pC  = validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pC_li_xu_2025.md
- ADV-LX = validation/ADVISORY_litmap_extension_2026-08-13.md

---

## 1. Ricostruzione

### 1.1 Il campo oggi: quattro paper, quattro "metodi", nessuna riduzione per-phase

> **[W2-R6] Box definizioni (per il consumo storyboard).** Due
> riduzioni distinte, mai da confondere: **media GLOBALE** = si media
> il campo su tempo e fase in UN solo stato steady equivalente, e si
> disegna UN ugello per quello stato (quello che fa il campo, dove
> disegna); **riduzione PER-PHASE** = si tiene una FAMIGLIA di stati
> steady indicizzati dalla fase dell'onda e si ottimizza il funzionale
> MEDIATO sulla famiglia (la riduzione del programma; frame di
> confronto = centerpiece R22-F, SYN:17-20). Mini-legenda sigle:
> P-A..P-D = i 4 paper del corpus C4; CT-x = threat consolidate;
> (iv)/(vi) = celle della forchetta d'errore del centerpiece; R26 =
> questione aperta averaging-at-ranking; PB-1/PB-2 = i claim di
> novita' del programma sul problema mediato; G14/P2 = il ponte
> multiplier-adjoint.

La campagna arrivi C4 (S-FOUNDATIONS-C4, 2026-08-20) ha letto
INTEGRALMENTE i quattro paper coupled RDE+nozzle selezionati dal
brief di campagna (selezione e razionale nel brief; [W2-R2] il
record dichiara UNREAD il PARENT metodologico Li-Xu 2022, W-05
"highest method-lineage bearing" SYN:526-528, e il cugino di metodo
Fievisohn 2018, W-09 SYN:540-542 — entrambi nominati in coda
procurement, aperto 7) e li ha consolidati in una matrice a 7 assi
(SYN:29-39, evidenza [REP]/[FIG]/[INF] per cella; tutto il corpus =
[ADV] published-CFD). La colonna "Design method" (SYN:33) e' la
fotografia del campo:

- **P-A (Liu-Wang 2022, PKU)** — rampa isentropica approssimata di
  Angelino a input TIME-AVERAGED (gamma=1.26, NPR 24.9, M_e 2.69);
  trade study discreto a 4 casi, **NO optimizer** (SYN:33). La fonte
  metodologica e' Angelino 1964 (AIAA J 2(10):1834-1835), che nel
  registro NON ha ancora una riga dedicata (candidato WANTED W-18,
  SYN:559-562, caveat di record sulla riga onofri :441).
- **P-B (Li-Xu 2023, NUAA)** — MoC assialsimmetrico (unit process
  Zucrow-Hoffman) + superfici variazionali **MAX-THRUST
  Rao/Vander-Veen** shrouded-plug su stato steady da p0/T0
  TIME-AVERAGED ("empirically recognized", p. 5 §3.1). **[WB1-R10]
  Riformulazione source-verified dei corner** (catch utente,
  `VERIFY_PB_corner_pb.md`): la mediazione RDE entra SOLO nei vincoli
  di ristagno p0/T0; i corner sono DUE (Fig. 13, p. 8) — lip della
  shroud a p_inf AMBIENTE (Eq. 22) e base dello spike troncato a
  p_b = "averaged base pressure" (Eq. 26), dove "averaged" = media
  SPAZIALE sulla base (lessico plug troncato steady), MAI
  cycle-averaging; Eq. 26 senza fonte citata E senza provenienza
  dichiarata del valore di p_b (che entra anche nella spinta, Eq. 18,
  termine +pi r_J^2 p_b). La forma SYN:33 "corner a p_b MEDIATO" e'
  superseded da questa riga. E' l'unico dei quattro che usa il
  variazionale classico — applicato pero' a UN singolo stato steady
  mediato globalmente (vincoli di ristagno time-averaged "empirically
  recognized", F-01, che cita P-D come origine; SYN:34).
- **P-C (Li-Xu 2025, NUAA)** — **nessun design nuovo**: prende il
  design max-thrust di P-B come baseline e studia misalignment
  assiale cowl/spike + attuazione dinamica (SYN:33).
- **P-D (Jourdaine 2019, KIT/Aoyama)** — **NONE**: spike conico 50 gradi
  fisso, esplicitamente non ottimizzato (F-19, p. 3450); il contenuto
  di metodo e' la catena di valutazione prestazioni Eqs. (1)-(6)
  (SYN:33).

Le comunanze consolidate (tutte [ADV], SYN:41-65): C-1, tutti e
quattro praticano o approvano la scommessa "average-then-classical-
design", con P-D origine citata — che e' esattamente la nostra
questione aperta R26, mai testata a livello di ranking da nessuno di
loro a grado per-phase (SYN:42-45); C-5, **nessuno dei quattro e' una
riduzione per-phase**, il compagno "steady" dove esiste (P-B/P-C) e'
una run assialsimmetrica a inflow mediato GLOBALMENTE — riduzione
piu' cruda della nostra; nessuna certificazione di classe, nessuna
barra d'errore, e "no optimizer appears anywhere in the four papers"
(SYN:58-61 — vedi la domanda 2 del panel per la lettura corretta di
questa frase accanto al variazionale di P-B).

**[WB1-R1] Istanziazione C-7 del "campo" (guardia 4 — mai "the field"
generico).** Su slide e in mappa, "il campo" = i gruppi NOMINATI coi loro
paper, id registry verbatim: **PKU** (`liu_2022` = P-A); **NUAA**
(`li_xu_lv_lv_song_2023` = P-B, `li_xu_lv_yu_zhou_2025` = P-C);
**KIT/Aoyama** (`jourdaine_2019` = P-D); **NASA-Glenn**
(`kaemming_paxson_2018` EAP, `paxson_miki_2022`); **Purdue**
(`harroun_2021`, `harroun_2020`, `stechmann_2019`). Fonte della regola:
CKP-S C-7 :270-271 (CKP-S =
`validation/spres_raws_2026-08-22/SESSION_STATE_checkpoint.md`).

**[WB1-R2] Eco della remark EAP (posizionamento di J vs la metrica
pressure-gain del campo; casa principale CH1 §1.2, qui l'eco — critic 6).**
La linea NASA-Glenn porta la metrica standard del campo: l'Equivalent
Available Pressure di Kaemming-Paxson (`kaemming_paxson_2018`). La remark
di record (M0:2526-2539, full text letto 2026-07-16): EAP_i è "the
PRESSURE-COORDINATE of J_ideal" — expand-then-average mai
mixed-out-then-expand, quantità mass-flux-weighted "algebraically
identical to our time-integrated fluxes (O1)", nel frame di detonazione
dove "area average = time average", cioè il nostro T0(i) "used tacitly as
a fact, proved here as a theorem"; **EAP_i(axial) <= J_ideal(total)** (due
rung adiacenti della ladder); e EAP porta le ipotesi quasi-steady e
azimuthal-decoupling (le nostre D1+D2) "UNSTATED and UNPRICED — the P4
corrector is, among other things, EAP's missing error bar". Il carrier CFD
della stessa linea è `paxson_miki_2022` (LL-5). È la risposta pronta alla
domanda ESA quasi certa "come vi posizionate rispetto all'EAP".

> **[WB1-R3] Box nomenclatura (critic 9; casa definitiva CH-REF — qui il
> box di consumo).** Quattro oggetti che collidono foneticamente, MAI da
> confondere su slide: **P-B** = il paper Li-Xu 2023
> (`li_xu_lv_lv_song_2023`); **p_b** = la pressione di base — ATTENZIONE
> alla doppia accezione [WB1-R10]: **p_b in P-B** = "averaged base
> pressure" SPAZIALE sulla base del plug (Eq. 26, lessico plug steady,
> nessun nesso col cycle-averaging; fonte e provenienza del valore NON
> dichiarate — `VERIFY_PB_corner_pb.md`), mentre **p_b nel nostro
> programma** = la chiusura di base pressure del troncamento (slot N2,
> riga ledger C61; namespace PB-2/Humphreys); **PB-2** = il flag problem del
> problem book (CH6 §1.2); **Gap B** = il salto di valore misurabile del
> frame CH6 §1.1. In più le etichette argmax-level C-3bis gap(A)/gap(B)
> hanno le lettere SCAMBIATE rispetto a Gap A/Gap B (gap(A)~Gap B,
> gap(B)~Gap A — mappa dichiarata in CH6 §1.2-bis). **Namespace "G",
> famiglie distinte**: G0-G6 = gate del piano D6; **litmap G1-G12 =
> l'executive gap summary della litmap (LM:19-30), quarta famiglia
> [WB1-C3-11]** — attivamente citata come "riga G5" (LM:23, "average
> first, design second"): la "riga G5" della litmap NON è il gate G5 del
> piano (passo umano Kraiko) né il gap G5 della lista T0P; la litmap ha
> anche numerazioni proprie per i gap-verdetti (C1-C4, LM:354-362; il
> ponte è G14); G1-G12 = gap-list T0P (CH3); GRAFT-Gxx = graft M0. Su
> slide mai "G1" o "G5" nudi: sempre col namespace dichiarato.

### 1.2 La dicotomia D-1 e le due figure-ancora D-6

**D-1** (SYN:320-327), [ADV-FIG] in tutti e quattro i codici: i campi
istantanei sono manifestamente non assialsimmetrici (oblique shock
rotante, footprint bandati a parete), i campi time-averaged sono plume
classici assialsimmetrici puliti. Ancore: P-A Fig. 7 vs 9 (pp. 7-8);
P-B Fig. 14 right vs left (pp. 9-10); P-C Fig. 10 left vs right
(pp. 9-10); P-D Fig. 9 vs 4 (pp. 3449, 3447). Quattro istanze
pubblicate indipendenti della classe di fenomeni dell'operatore K
(centerpiece §2.3), accanto a Harroun Fig. 18 (SYN:46-51). D-1
"licenses NO magnitude" (SYN:326-327): e' fenomenologia, mai numero.

**D-6** (SYN:353-358), le due figure di performance: il record le
marca "the two figures the loop must see" (SYN:353); che il DECK
debba mostrarle e' direttiva di consumo S-PRES di questo capitolo,
coerente con D-6 [W2-R10]:
- **P-B Fig. 15 (p. 10)**: C_fx steady ~piatto 0.965-0.971 dove il
  transient ha un ottimo a 40% (+0.52%) e un cliff a 80% (-5.78%) —
  "vertical offset = reduction gap, SHAPE difference =
  optimum-visibility statement" (SYN:97-99, 353-356). Flat-vs-peaked:
  la riduzione steady globale NON VEDE l'ottimo che il transient vede.
- **P-C Fig. 13 (p. 11)**: barre C_fx transient-vs-steady con ENTRAMBI
  i segni (gap 0.2-1.5%) e un flip di ranking a meta' classifica,
  argmax stabile (SYN:99-102, 356-358).
Insieme sono i marker empirici delle celle (iv)/(vi) della forchetta
(SYN:358) — secondo e terzo marker accanto alla linea Paxson-Miki
(SYN:107-110). Classe: [ADV], nessun numero entra nello schema
delta/mu (SYN:263-264).

Tre righe-figura aggiuntive [WB1], stesse regole (loro numeri, CT-6;
abbreviazioni: pA/pB/pD =
validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_p{A,B,D}_*.md):

- **[WB1-R4] P-B Fig. 16 (p. 10) — il feedback ugello→camera** (critic
  16): p_0/p_infinity all'uscita del combustore sale monotono e T_0 ha un
  picco al variare della troncatura — "the nozzle back-reacts on chamber
  p_0/T_0 with truncation" (pB:405; F-13 [REP pp. 10-11 + Fig. 16],
  pB:164, 283); consolidata in CT-1 come voce "drift p0-T0"
  (SYN:54, 76-78). È la faccia-figura della minaccia CT-1 (§1.3).
  Classe: [ADV-FIG].
- **[WB1-R5] P-C Fig. 20/21/22 (pp. 16-17) — la forza laterale rotante**
  (critic 11): forza laterale istantanea ~25-35% della spinta assiale
  istantanea (450-670 N vs 1500-1860 N, [INFER] dello slot), direzione
  phi_L che spazza 0-360 gradi a ogni ciclo (Fig. 21b sawtooth) [REP
  pp. 14, 17, Fig. 21] (pC:187-195). Lo slot la aggiudica "the cleanest
  published face of 'instantaneous azimuthal asymmetry is O(10x) the
  time-averaged percent effects'", con "large per-phase content,
  near-cancelling mean — the K-bar = 0 phenomenology" e media implicita
  ~0 ("near-zero implied mean") (pC:269-275, 301-303). L'identificazione
  "faccia pubblicata di K-bar=0" è quindi ADJUDICATA NELLO SLOT
  ([FIG]+[INFER], corpus [ADV]), non nuova qui: la slide C10 dello
  storyboard ha ora la sua catena d'ancore.
- **[WB1-R6] Il pin di classe-dati nei CFD del corpus: ESIBITO, mai
  verificato spettralmente** (critic 14). La metà positiva: P-C riporta
  "clean single-mode periodicity at every station across all [five
  configurations]" (pC:253, 347) e strutture wave-locked (pC:599;
  "multi-peak phase-locked fine structure post-throat", THH:613); P-B
  dichiara l'onda "persistent single-mode rotating wave" (pB:396); P-A
  "single-mode stable by construction" (pA:257); P-D "their solver locks
  to ONE wave" (pD:368-370). La metà negativa, BOUNDED al corpus letto
  (query in-window: grep -i 'spectral|FFT|mode purity' sui 4 slot = 0
  hit di verifica): NESSUNO dei quattro esegue una verifica SPETTRALE
  della purezza di modo — l'esibizione è a livello di forma
  d'onda/periodicità osservata, mai un test. Scope da NON fondere su
  slide col fatto R20, che riguarda i dataset HARDWARE (CH6 §1.6
  [WB1-R8]).

### 1.3 Il threat ledger consolidato CT-1..CT-8

Otto minacce consolidate da 16 slot threats; esito: **0 BREAK, 1
ENRICHMENT-AMENDMENT (CT-3), 1 rider duty (CT-4), 6 do-not-fire**
(SYN:181-188). Nessuna riga THEOREM/THEOREM* di record contraddetta
da nessuno dei quattro paper (SYN:185-188). In sintesi:
- **CT-1** data-nozzle coupling (la piu' affilata): scala di evidenza
  mdot -2.8% / drift p0-T0 / +3.89% / +50-60% Pc; NON spara (confine
  di scope, non theorem breaker) ma il fatto di programma resta: "the
  largest published performance lever (choked +4-7% Isp) lives OUTSIDE
  the fixed-interface design class"; decider = CFD-1 (SYN:75-94).
- **CT-2** optimum blindness lungo direzioni di design reali (Fig. 15
  flat-vs-peaked + Fig. 13 flip + drag tail P-A): gia' prezzata dalle
  celle (vi)/(iv); NEEDS F2-MEASUREMENT (M-RED) per convertire [SE]
  in misurato (SYN:96-110).
- **CT-3** l'unica che spara, come ENRICHMENT: la frase di record
  sull'assenza di referee esterno e' STRETTAMENTE VERA cosi' come
  scritta (la clausola restrittiva "...THAT DISCRIMINATES the
  2D-per-phase-averaged prediction against 3D-unsteady truth" fa parte
  della frase); P-B Fig. 15 / P-C Figg. 13+20b sono i "nearest
  referee-shaped pairs", squalificati per due ragioni dichiarate:
  compagno mediato GLOBALMENTE (non per-phase) e verita' same-family
  URANS (non esterna/sperimentale) (SYN:112-132, 477-492).
- **CT-4** troncamento "40% ottimo" P-B vs default 0.20 nostro: NON
  commensurabili senza mapping (removed-fraction-of-cowl vs
  retained-fraction-of-plug); decisione di record STANDS, rider
  obbligatorio sul dossier ADR-D4 (SYN:134-143, 387-411).
- **CT-6** = la standing consumption rule citata in testa (SYN:158-163).
- CT-5/CT-7/CT-8: pin single-mode gia' prezzato (R20), retorica di
  value-proposition col proprio contro-esempio interno, raccomandazione
  di convergenza come contesto (SYN:145-179).

### 1.4 La genealogia variazionale (linea steady): da Guderley-Hantsch al "per-phase brick"

Linea canonica verificata (LM:271-283): Guderley-Hantsch 1955; **Rao
1958** (Jet Propulsion 28(6):377-382) con struttura a due
moltiplicatori su superficie di controllo confermata via NASA
TM-103175; correzioni di record: Rao TOP = ARS J. 1960, "Rao 1961" =
paper SPIKE (Planet. Space Sci. 4:92-101); Guderley-Armitage 1962/1965
= problema variazionale "exact" full-contour; Shmyglevskii PMM
1957/1962. Il dettaglio "Eq. 14": il web-side lo dava UNVERIFIED
(originale paywalled, LM:277), ma la **risoluzione in-house** chiude
il caveat — la condizione corner/transversality di Rao 1958 E'
"Eq. [14], p. 379", verificata contro RAO.pdf primario con numeri di
pagina per-equazione (LM:381-386). Classe: [REP] su fonte primaria
in-repo.

**Lo schema comune** (Rao 1958, generalizzato Hoffman 1967; LM:387-404),
verificato contro cinque fonti primarie: massimizzare il funzionale di
spinta sulla superficie di controllo CE soggetto a ESATTAMENTE DUE
vincoli isoperimetrici — massa (lambda_2) e lunghezza (lambda_3,
f_3 = cot phi); terzo moltiplicatore h = 0 (Guderley-Hantsch). La
prima variazione consegna: (i) la superficie di controllo ottima E'
una caratteristica (RISULTATO, non assunzione); (ii) integrali primi;
(iii) transversality di endpoint = corner conditions. Punto dottrinale
(LM:400-404): la pressione ambiente/base entra SOLO per transversality
di endpoint, mai come terzo moltiplicatore integrale — esattamente la
struttura che il sistema mediato (D3 §4) eredita, con (**') al posto
del corner single-phase.

**Hoffman 1967** e' la meta' mancante di G14/P2 pubblicata nel 1967:
per flusso chimicamente reagente il sistema di ottimalita' e' fatto di
CAMPI di moltiplicatori di Lagrange lambda_1..lambda_4 (+lambda_5 per
specie) che soddisfano PDE lungo le STESSE caratteristiche del flusso
— un continuous adjoint avant la lettre, con residuo di ottimalita' E
a posteriori (Eq. 78) (LM:428-435). Nota di rigore D-01 (ratificata
2026-08-13): la glossa "residuo classico = gradiente adjoint /
antenato del certificato Level-C" e' CANCELLATA di record, perche'
KT2015 Eqq. (2.9)-(2.10) istanziano gia' letteralmente quella
identificazione (LM:435-441). Inoltre Hoffman 1967 p. 676 PROVA che
la biiezione del corner muore per gas reagente: il per-phase brick in
forma chiusa e' frozen-composition-only (LM:457-464) — supporto
classico page-verified del confine di licenza Level-A. Allman-Hoffman
1981 e Sternin 1962 sono nel corpus primario in-repo (LM:368-374);
Sternin 1962 (+ Rao-Beck 1994 Eq. 4) = confine classico di
esistenza/regolarita' del contorno ottimo, gia' implementato come
`boundaryfunction_solve` (LM:465-469).

**La scuola Kraiko** — tutti e quattro i paper rivendicati CONFERMATI
(LM:299-314): Kraiko-Tillyaeva 1982 (inflow non uniforme alla sezione
minima); Kraiko-Telyakovskii-Tillyaeva 1994 (profiling per flusso
altamente rotazionale/vorticoso); Kraiko-P'yankov-Tillyayeva 2002
(plug con inflow transonico NON UNIFORME — ignorare la non-uniformita'
transonica costa spinta reale: supporto diretto allo status
first-order del canale N3); Kraiko-Tillyayeva 2007 (spike + direzione
ottima del flusso primario). A monte, Kraiko 1963 (formulazione
variazionale EOS-general, riga di registro a profondita'
TITLE-VERIFIED, full text UNACQUIRED — duty di acquisizione sulla
lista umana G5; LM:284-293). **Scope map di record** (LM:315-320): il
risultato piu' generale per-stato-singolo e' il contouring ottimo
bell/plug, planare/assialsimmetrico, per inflow steady ARBITRARIO non
uniforme e vorticoso, vincoli di dimensione/backpressure, EOS
arbitraria a due parametri (1994+2002). **Tutto e' per UN singolo
stato steady di inflow — esattamente il "per-phase brick" del
programma T2, confermato esistere alla generalita' richiesta.**

### 1.5 La linea unsteady (i tre MANDATORY) e il ponte adjoint

La linea unsteady, risolta con una distinzione (LM:322-342):
- **Efremov-Kraiko 2004**: condizioni variazionali di OUTFLOW ottimo
  per max thrust dati flussi INTEGRALI d'ingresso; motivato dal
  pulsed-detonation ma formulato come BOUND steady/ideal-limit —
  aggira il problema unsteady a parete condivisa. MANDATORY CITATION.
- **Kraiko-Egoryan 2020** (+ AIP 2018): cicli a detonazione valutati
  con bound di ugello IDEALE (istantaneamente adattato) — la chiusura
  ideal-adaptation di T4 HA precedente pubblicato COME BOUND; il
  teorema shape-level nested-argmax di T4 resta unfound. MANDATORY
  CITATION accanto a T4.
- **Levin-Manuilovich-Markov 2010**: impulso cycle-averaged di un
  motore PULSE-detonation massimizzato su forme di condotto
  assialsimmetriche — per ricerca parametrica/numerica DIRETTA,
  **senza condizioni di ottimalita'/transversality**. L'artefatto
  esistente piu' vicino a PB-1/PB-2 nello spirito; MANDATORY CITATION.

[W2-R4] Vicino di metodo da citare in posizionamento:
**Fievisohn-Hoke-Schauer 2018** (quasi-2D MoC di RDE con ugello) e'
il lineage "MoC-native unsteady RDE+nozzle, never extended to design"
(ADV-LX:99-100) — il piu' prossimo alla riduzione del programma come
STRUMENTO, mai portato al DESIGN: il gap C1/C2 non e' toccato. Full
text = W-09 in coda procurement (SYN:540-542).

Ponte adjoint (G14): Giles-Pierce JFM 2001 confermato senza alcuna
connessione Rao/Guderley; ancora nuova Lozano-Ponsin 2025 (adjoint
analitici 2-D supersonici a struttura caratteristica, zero menzioni di
Rao/Guderley/Kraiko): "the P2 bridge lemma now has both banks built
... and the bridge itself confirmed missing" (LM:344-352). Con
Hoffman 1967 le sponde diventano TRE (classical multiplier fields /
quasi-1D analytic adjoint / 2-D analytic adjoint), nessuna delle quali
cita il lato delle altre (LM:437-441).

### 1.6 I gap query-bounded e la formulazione P2/G14 di record

Verdetti gap (LM:354-362), tutti query-bounded [claim di novita'
NOT-FOUND(q), R5]:
- **C1** family-averaged classical contouring: NOT-FOUND(q).
- **C2** averaged Rao-type wall/corner conditions: NOT-FOUND(q) — zero
  hit sotto query ensemble/phase-averaged-optimality.
- **C3** identificazione Rao = adjoint: NOT-FOUND(q) —
  folklore-adjacent (multiplier=adjoint e' da manuale) ma
  l'identificazione pubblicata specifica e' assente.
- **C4** PARTIAL (la linea unsteady sopra). Blind spot dichiarato: TOC
  del libro Kraiko 1979 non verificata — passo umano PMM/biblioteca
  (D4 §3) raccomandato prima della stampa, come due diligence
  (LM:359-362).

**P2/G14 formulazione di record** (query-bounded 2026-08-13,
LM:442-456): nessun lavoro pubblicato esegue l'identificazione tra il
campo moltiplicatore del design variazionale classico (Route B:
Hoffman 1967, Scofield-Hoffman 1971, Kraiko, Shmyglevskii, HTH) e
l'adjoint continuo/discreto della shape optimization moderna, in
nessuna delle tre forme rivendicate: (i) enunciata in linguaggio ASO
moderno; (ii) connessa ad adjoint DISCRETI / reverse-mode AD; (iii)
usata per guidare un optimizer gradient-based moderno.
**ESPLICITAMENTE CONCEDED**: l'equivalenza generica "adjoint variable
= moltiplicatore di Lagrange del vincolo di flusso" (Giles-Pierce 2000
p. 397; Lions 1971; Jameson 1988) e la catena completa Route B ->
Route A DENTRO la scuola classica (KT2015 Eqq. (2.2)->(2.9)->(2.10)->
(2.12)). "Residual novelty = articulation + operationalization, not
mathematical content of the bridge" (LM:455-456).

L'estensione avversaria 1971->2026 (ADV-LX, 4 auditor indipendenti a
mandato falsificatorio, evidenza web-tier salvo dove dichiarato):
tutti e quattro i claim SOPRAVVIVONO nei bound dichiarati, con **due
near-miss nominati** (ADV-LX:8-40): (A) Kraiko-Tillyaeva JMS 208
(2015) chiama il sistema dei moltiplicatori "conjugate/adjoint
problem" — terminologia interna, nessuna equivalenza ASO; la versione
non qualificata "nessuno ha mai chiamato i moltiplicatori adjoint"
sarebbe FALSA (ADV-LX:10-17); (B) **Kraiko-Pyankov-Tillyayeva
ISABE-2003-117 + Bogdanov et al. 2002**: contouring variazionale
maximum-AVERAGE-thrust sotto parametri di ristagno time-dependent —
falsifica la lettura NON qualificata di "nessuno ha mai posto il
design mediato"; presunto quasi-steady a inflow uniforme (full text
UNREAD = rischio residuo #1) (ADV-LX:25-31). Il delta residuo che
sopravvive comunque: inflow a onda rotante spazialmente non uniforme;
dinamica genuinamente unsteady nel vincolo; Jensen gap del funzionale
mediato; condizioni di ottimalita' sotto vincolo periodic-wave
(ADV-LX:32-35). Vettore di minaccia nominato: JANC (JAX reacting
solver differenziabile, demo adjoint su RDC inverse problem) — "makes
the discrete falsifier buildable. Watch 2026+" (ADV-LX:38-40).

**[WB1-R8] Eco N-Q (cella Q-iii)**: alla lista dei gap query-bounded si
aggiunge la query eseguita in W-B.1 (perimetro chiuso G-11: registry 174
id + litmap + slot P-A..P-D): *"il campo separa i tre gap di design —
formulazione / modello / composizione?"* — **NOT-FOUND(q)**. I
near-object sono decomposizioni di PERDITA di flusso, mai di gap di
design: P-B "three-part TRANSIENT flow-loss decomposition" (pB:175;
"stated but not separately quantified", pB:363); P-A 14.2% "UNDECOMPOSED
... no decomposition offered" (pA:259-261). Query, pattern e STOP in CH6
§1.2-bis.

**[WB1-R9] Eco N-H (cella H-iii — handoff B3, query eseguita in CH1
§1.7)**: *"il campo RDE-nozzle dichiara il regime di validità della
propria media/metodo con prezzo d'errore?"* — **NOT-FOUND(q)** sul campo
istanziato: NUAA (`li_xu_lv_lv_song_2023`, `li_xu_lv_yu_zhou_2025`),
Purdue (`harroun_2021` — media UNDECLARED), NASA-Glenn/AFRL
(`kaemming_paxson_2018` "UNSTATED and UNPRICED", `paxson_miki_2022`),
KIT/Aoyama (`jourdaine_2019`), PKU (`liu_2022` — assioma dichiarato mai
prezzato); unica istanza adiacente FUORI campo RDE = `kraiko_osipov_1970`
"validity footnote, unpriced" (litmap:141-142). Testo completo della
query e perimetro: CH1 §1.7 (non duplicati qui). Coerente con la
conclusione (3) di P-C (§1.8, L12): "approximately applicable" sotto
premessa kHz è una PREMESSA dichiarata, mai un prezzo d'errore.

### 1.7 Harvest di ancore: gola corrugata, Humphreys, Veen Eq. 9

- **KP18 Fig. 6 — la sonic line corrugata** (THH:398-412, [REP p.10]
  + [FIG]): "with a non-uniform flow, any choking condition ... will
  have a range of axial Mach numbers... typically will contain both
  subsonic and supersonic portions" — il concetto verbatim di gola
  "effectively choked" corrugata. Forma (re-render di Fig. 6): la
  sonic line e' attraversata DUE volte per ciclo — plateau ~1.01, dip
  ~0.96 davanti all'onda, salto a 1.33, rilassamento attraverso M=1
  fino a un minimo largo ~0.85. **KP18 Table 1** (THH:415-421,
  [FIG p.6]): l'UNICO set quantitativo pubblicato di statistiche
  p0/T0 di gola — Pt8/Pt3 max 4.07 / min 0.67 / avg 1.43 (spread
  237%); Tt8/Tt3 41%; M8x 48%. Nessun paper del corpus disegna una
  superficie M=1: Fig. 6 e' l'oggetto piu' vicino (THH:712-713).
  Tutto CT-6: numeri loro, contesto, mai bande nostre.
- **Humphreys 1971, l'exhibit di design-sensitivity x2.45**
  (BPH:619-625; riassunto BPH:720-723): alle pp. 1586-1587, cambiare
  il modello di p_b (6a->6b, Eq. 12->38) sposta l'altezza di base
  ottima di un fattore **2.45** e la pendenza di parete al tip da
  -13.26 a -3.08 gradi, muovendo la spinta di solo +0.26%: **la
  chiusura p_b muove l'ARGMAX a O(1) con il VALORE quasi piatto**.
  Conseguenza di record: ogni scelta di chiusura N2 va prezzata a
  livello design-gradient, non a livello valore (BPH:623-625).
- **Veen Eq. 9 = il fondo dello stack** (BPH:465-472, 605-610): la
  chiusura p_b = 0.846 p_e / M_e^1.3 ereditata dalla dottrina
  GENO/Veen e' verbatim l'Eq. (5.1) del rapporto WG10 (fit near-wake
  Rom-1966 via Humphreys 1971), giudicata "FAILED to produce reliable
  results" da Fick & Schmucker (JSR 1996) — "the inherited closure is
  the stack's bottom"; N2 deve sostituirla (BPH:716-718). Il MIGLIOR
  modello puro-empirico classico (Univ. Rome Eq. 5.7) porta comunque
  una banda [+19%, -15%] su dati freddi misurati (BPH:488-492,
  600-602): il floor di model-form del canale (v).
- **[WB1-R7] L'ordine delle escursioni per-fase: il bracket pubblicato**
  (critic 16): il numero-frame "10:1" delle correzioni utente C-2/C-3bis
  (CKP-S:206, :221 — "Jensen ... over 10:1 data excursions") sta DENTRO
  il bracket pubblicato del corpus: **~6:1 in gola** (KP18 Table 1,
  Pt8/Pt3 max/min 4.07/0.67, THH:415-421) fino a **~20:1 alla stazione
  combustore** ("jump + exponential relaxation, peak/trough ~20:1 at
  combustor station", P-C Fig. 15(a-d)+16, THH:613). Regola di slide: o
  il bracket ancorato (6:1-20:1, coi loro numeri, CT-6), o "O(10:1)"
  SOLO come cifra del frame utente con ancora CKP-S — mai come numero
  di record nostro.

### 1.8 La guardia best-of-sweep vs argmax e la conclusione (3) di P-C

Due letture gemelle dallo stesso punto del record (pC:138-152):
- **L11** (pC:138-146): tutte le configurazioni, transient e steady,
  restano sopra 0.94; gap [FIG] ~0.2-1.5% in C_fx con ENTRAMBI i
  segni, spread di configurazione ~2.5 punti. Il verdetto (vi)
  (pC:375-379): l'argmax sulla LORO famiglia discreta di 5
  configurazioni e' lo stesso in steady e transient, MA il flip a
  meta' ranking mostra che "reduced-vs-true ordering CAN differ along
  real design directions at their gap scale". **La guardia**: un
  best-of-sweep discreto a argmax coincidente NON e' una prova di
  stabilita' dell'argmax in generale — e' una istanza [ADV] che
  "brushes" la cella (vi), consumabile solo come marker, mai come
  chiusura del rischio ranking (che resta R26/M-RED). [Classe:
  [INF]/sintesi-capitolo da pC:375-379 + CT-2 (SYN:103-110), non
  frase di record — W2-R8]
- **L12, verbatim** (pC:147-152): il caso di riferimento raggiunge
  exit Mach medio massimo 3.03 — "implying that the maximum thrust
  theory for the steady supersonic axisymmetric flow proposed by Veen
  et al. [48] **is approximately applicable** to the RDE nozzle under
  the premise that the propagation frequency of detonation waves are
  in the magnitude of kHz" [REP p. 11; conclusion (3) p. 16]. E' il
  campo stesso che dichiara la propria premessa: "approximately
  applicable", condizionata alla frequenza — non un teorema, non una
  banda, non un test di ranking.

---

## 2. Stato per-claim

| # | Claim | Classe | Ancora | Carrier / falsificatore |
|---|---|---|---|---|
| 1 | I 4 metodi del campo: Angelino ramp su medie (P-A), MoC+Rao-Veen max-thrust su medie (P-B), nessun design nuovo (P-C), conico fisso non ottimizzato (P-D) | [REP] per-cella su lettura integrale; corpus [ADV] | SYN:31-39 | slot files 4/4 [FULL] (SYN:12-16) |
| 2 | Nessuno dei 4 e' una riduzione per-phase; compagno steady = media GLOBALE; nessun error bar; nessuna certificazione di classe | [ADV] (C-5) | SYN:58-61 | re-test onesto (e).6 SYN:465-492 |
| 3 | Dicotomia istantaneo/medio in tutti e 4 i codici (D-1) | [ADV-FIG]; "licenses NO magnitude" | SYN:320-327 | figure citate per pagina nei 4 slot |
| 4 | P-B Fig. 15 flat-vs-peaked: la riduzione steady non vede l'ottimo transient (+0.52% a 40%, cliff -5.78% a 80%) | [ADV], marker empirico cella (vi) | SYN:97-99, 353-356 | falsificatore di record: schema \|argmax shift\| <= delta/mu, decider M-RED + R22-CFD-2 (SYN:103-106) |
| 5 | P-C Fig. 13: gap 0.2-1.5% entrambi i segni, flip mid-ranking, argmax stabile sulla famiglia discreta | [ADV] + [FIG] | SYN:99-102; pC:138-146, 375-379 | idem riga 4 |
| 6 | Threat ledger: 0 BREAK, 1 enrichment (CT-3), nessuna riga THEOREM/THEOREM* contraddetta | verdetto di campagna, refuter-passed [REV-NRS] | SYN:181-188, 630-648 | tabella revisione NRS-1..9 (SYN:634-644) |
| 7 | Rao 1958 corner = Eq. [14] p. 379, verificata in-house su PDF primario | [REP] fonte primaria | LM:381-386 | RAO.pdf + theory_variational_understanding §1.2 |
| 8 | Schema comune: 2 vincoli isoperimetrici (massa, lunghezza), h=0; superficie ottima = caratteristica (risultato); p_a/p_b solo via transversality | risultato classico (teoremi del campo), [REP] verificato su 5 fonti primarie in-repo [W2-R5] | LM:387-404 | GENO implementation match (LM:408-424) |
| 9 | Hoffman 1967 = multiplier FIELDS su caratteristiche (adjoint avant la lettre); p. 676: corner bijection muore per gas reagente -> brick chiuso = frozen-composition-only | [REP] page-verified; glossa adjoint-residuo CANCELLATA (D-01) | LM:428-441, 457-464 | confine di licenza Level-A |
| 10 | Scuola Kraiko 1982/1994/2002/2007 confermata; scope: tutto per UN singolo stato steady = il per-phase brick esiste alla generalita' richiesta | [REP] (riferimenti verificati; DOI dove presenti — il 1994 ZhVMMF e' senza DOI, LM:299-314) [W2-R9] | LM:299-320 | — |
| 11 | Linea unsteady: Efremov-Kraiko 2004 (bound, aggira shared-wall), Kraiko-Egoryan 2020 (ideal-adaptation COME BOUND; nested-argmax T4 unfound), Levin 2010 (ricerca diretta, NESSUNA condizione di ottimalita') — tre MANDATORY citations | [REP] + verdetto C4 PARTIAL | LM:322-342 | query-bounded |
| 12 | C1 family-averaged contouring NOT-FOUND(q); C2 averaged corner conditions NOT-FOUND(q); C3 Rao=adjoint NOT-FOUND(q) folklore-adjacent | claim di novita' query-bounded (R5) | LM:354-362 | sweep avversario 1971-2026: SURVIVE con 2 near-miss (ADV-LX:8-40) |
| 13 | P2/G14: identificazione multiplier-field/ASO-adjoint non eseguita in nessuna delle 3 forme; CONCEDED equivalenza generica + catena interna KT2015; novita' residua = articolazione+operazionalizzazione | formulazione di record query-bounded | LM:442-456 | tre sponde senza ponte (LM:344-352, 437-441) |
| 14 | ISABE-2003-117/Bogdanov 2002 = near-miss di PB-2 (average-thrust sotto parametri time-dependent, presunto quasi-steady); caveat OBBLIGATORIO sui claim PB-2/D2-G3 | [SE] web-tier, full text UNREAD | ADV-LX:25-35, 87-88, 125-128 | rischio residuo #1; procurement G5 |
| 15 | KP18 Fig. 6 sonic line corrugata (M 0.85->1.33, 2 attraversamenti/ciclo) + Table 1 = l'unica statistica p0/T0 di gola pubblicata (spread Pt 237%) | [REP]+[FIG], consumo CT-6 (contesto, mai bande) | THH:398-421, 696-697, 712-713 | — |
| 16 | Humphreys 1971: swap chiusura p_b -> argmax x2.45, valore +0.26% — la chiusura p_b va prezzata a livello design-gradient | [REP] pp. 1586-1587, exhibit che vincola N2/canale (vi) | BPH:619-625, 720-723 | — |
| 17 | Veen Eq. 9 = WG10 Eq. (5.1), FAILED per Fick-Schmucker; best classico Univ. Rome = [+19%,-15%] su dati freddi | [REP] WG10 + verdetto MODEL-UNREL | BPH:465-472, 488-492, 605-610 | N2 deve sostituire la chiusura ereditata (BPH:718) |
| 18 | P-C conclusion (3): teoria max-thrust Veen "approximately applicable" sotto premessa kHz | [REP p. 11/16] — auto-dichiarazione del campo, non teorema | pC:147-152 | R26 resta aperta al ranking (SYN:373-385) |
| 19 | Frase no-external-referee di record STRETTAMENTE VERA cosi' come scritta; nearest referees P-B/P-C nominati e squalificati (media globale; URANS same-family) | verdetto re-test [REV-NRS-1] | SYN:465-492 | il bracket chiude solo via R22-CFD nostro o procurement dedicato (SYN:490-492) |
| 20 | P-B Fig. 16: l'ugello retro-agisce su p0/T0 di camera con la troncatura (voce "drift p0-T0" di CT-1) | [ADV-FIG], CT-6 [WB1-R4] | pB:164, 283, 405; SYN:54, 76-78 | — |
| 21 | P-C Fig. 20/21/22: forza laterale ~25-35% dell'assiale rotante a frequenza d'onda, media implicita ~0 — faccia pubblicata della fenomenologia K-bar=0 (aggiudicazione dello slot) | [FIG]+[INFER], corpus [ADV], CT-6 [WB1-R5] | pC:187-195, 269-275, 301-303 | — |
| 22 | Pin single-mode ESIBITO nei CFD del corpus (periodicita' osservata, strutture wave-locked) ma MAI verificato spettralmente da nessuno dei 4 | bounded al corpus letto (grep in-window) [WB1-R6] | pC:253, 347, 599; pB:396; pA:257; pD:368-370; THH:613 | scope distinto da R20 (hardware, CH6 §1.6) |
| 23 | Escursioni per-fase pubblicate: bracket ~6:1 (gola, KP18 Table 1) - ~20:1 (combustore, P-C); il "10:1" del frame utente sta nel bracket | [REP]+[FIG], CT-6 [WB1-R7] | THH:415-421, 613; CKP-S:206, 221 | — |

---

## 3. Gli APERTI

1. **ISABE-2003-117 + Bogdanov 2002 full text UNREAD** — il rischio
   residuo #1 dell'intera posizione di novita' ("flips B's near-miss
   either way", ADV-LX:111-112). Owner/trigger: lista human-read G5
   (ADV-LX:127-128); i claim PB-2/D2-G3 portano gia' il caveat
   obbligatorio (ADV-LX:87-88, 125-126).
2. **Kraiko 1979 book TOC unverified** + reference list di
   Kraiko-Tillyaeva 2015 non controllata ("could flip A's near-miss to
   bridge", ADV-LX:112) — passo umano PMM/biblioteca (D4 §3),
   declassato a due diligence pre-print ma non eseguito (LM:359-362).
   Kraiko 1963 full text UNACQUIRED (LM:284-293).
3. **R26, la scommessa di averaging al livello ranking**: "adequate
   for sizing, unpriced at ranking" — SHARPENED, non mossa, dai 4
   arrivi (SYN:373-385). Decider di record: M-RED (gradiente misurato)
   + R22-CFD-2 (SYN:103-110). Nessuno dei 4 paper la testa a grado
   per-phase (SYN:42-45).
4. **Il no-external-referee bracket**: nessuna coppia pubblicata
   discrimina la predizione 2D-per-phase-averaged contro verita'
   3D-unsteady; chiude SOLO via R22-CFD nostro o procurement dedicato
   (SYN:490-492).
5. **R8**: nessuna MISURA di base pressure su plug troncato RDE
   hot-fire esiste in alcuna fonte letta; il closer nominato e'
   strumentazione CTAP V1.4-class su base troncata in condizioni
   rocket, sweep NPR ~4-20 — classe procurement, esterna (BPH:627-634).
6. **Il leverage choked vive fuori dalla classe fixed-interface**
   (CT-1): il piu' grande lever di performance pubblicato (+4-7% Isp)
   e' un class-changing move; prezzarlo e' il nucleo irriducibile di
   CFD-1 (SYN:87-94, 413-423).
7. **Procurement Tier-1 W-01..W-08 non eseguito** (Fotia 2016 citato
   da TUTTI e quattro; Li-Xu 2022 = il PARENT metodologico di P-B/P-C;
   Angelino 1964 senza riga dedicata) (SYN:510-538, 559-562).
8. **JANC watch 2026+**: il falsificatore discreto del claim C
   diventa costruibile (ADV-LX:38-40). Non trovato nel record un
   owner formale oltre la voce watch.

---

## 3-bis. Antenati diretti (lineage claim — template §3-bis; nodo N-N) [WB1]

Join sul `LINEAGE_LEDGER.md` (merge W-B.0) per {LL-id, componenti},
contratto [F-des-4]; ogni riga del ledger è CANDIDATE finché il refuter
C6 (W-C) non passa (i SEED utente sono confermati dalle parti, restano
attaccabili). La linea EVALUATION per-fase + le istanze crude del campo:

- **LL-3 Stechmann 2019** (`stechmann_2019`, Purdue): blowdown 0-D
  per-phase, media mass-weighted DICHIARATA, famiglie FISSE — l'inizio
  della linea evaluation; manca vs noi: contouring variazionale sulla
  famiglia.
- **LL-2 Harroun 2021 (+2020)** (`harroun_2021`, `harroun_2020`,
  Purdue): famiglia per-phase steady 2-D + C_F quasi-cycle-averaged,
  convenzione di media UNDECLARED (peso/denominatore UNDECLARED nel
  paper, pp. 670-671 + Eq. 10 — duty (a) chiuso alla fonte); manca:
  media dichiarata, condizioni di ottimalità, tier di validazione (CT-3).
- **LL-4 Kaemming-Paxson 2018 EAP** (`kaemming_paxson_2018`,
  NASA-Glenn): rung int-max + ricostruzione state-averaged + statistiche
  di gola; manca: la barra d'errore (la remark [WB1-R2]: "the P4
  corrector is EAP's missing error bar").
- **LL-5 Paxson-Miki 2022** (`paxson_miki_2022`, NASA-Glenn): J
  cycle-averaged a livello CFD, OFAT, "senza ottimalità né bande".
- **LL-20 Li-Xu 2023 (P-B)** (`li_xu_lv_lv_song_2023`, NUAA): Rao su
  stato steady da p0/T0 time-averaged — istanza cruda della scommessa
  average-then-design; corner: lip a p_inf ambiente (Eq. 22), base a
  p_b = media SPAZIALE di base (Eq. 26, senza fonte né provenienza del
  valore — forma corretta source-verified, `VERIFY_PB_corner_pb.md`,
  che supersede la dicitura ledger "corner a p_b mediato"); manca: la
  famiglia per-fase e le condizioni di ottimalità MEDIATE
  (C2 NOT-FOUND(q)).
- **LL-22 convenzioni di media non dichiarate** (Liu Eq. 14, P-C; +
  Harroun LL-2): "terza+quarta istanza — la nostra µ è l'unica pinnata
  (T-O2)".

Copertura lint 7 dei claim di novità del capitolo: C1/C2 (contouring
famiglia-mediata / corner conditions mediate) → antenati più vicini
LL-20 + LL-16 (Efremov-Kraiko 2004: variazionale period-averaged SENZA
parete, già MANDATORY in §1.5) + LL-1 (Kraiko-Osipov 1970, parete
pesata W(t), citazione OBBLIGATORIA); C3 (ponte multiplier-adjoint) →
LL-14 (KT2015: catena Route B→A interna) + LL-12 (Giles-Ulbrich 2010,
teorema negativo); linea evaluation → LL-2..LL-5 sopra. Nessun claim di
novità di questo capitolo resta senza riga di lineage.

---

## 4. Domande da panel

**(1) "Come distinguete il vostro claim di novita' da Kraiko-Egoryan
2020 e Levin 2010?"**
Risposta dal record (LM:322-342): li citiamo MANDATORY, e la
distinzione e' strutturale su due assi. Kraiko-Egoryan 2020 valuta
cicli a detonazione con bound di ugello IDEALE istantaneamente
adattato: e' un BOUND, non un contouring — da' precedente pubblicato
alla chiusura ideal-adaptation di T4, mentre "T4's shape-level
nested-argmax theorem remains unfound" (LM:329-334). Levin 2010
massimizza l'impulso cycle-averaged di un PDE su forme di condotto per
ricerca parametrica DIRETTA, "no optimality/transversality
conditions" (LM:335-340): e' l'artefatto piu' vicino a PB-1/PB-2
nello spirito, ma il nostro claim e' esattamente cio' che manca li' —
le CONDIZIONI di ottimalita' (corner/transversality Rao-type) sulla
famiglia mediata sotto vincolo periodic-wave (C2 NOT-FOUND(q),
LM:355-357; delta residuo ADV-LX:32-35). In piu' il caveat onesto:
ISABE-2003-117 (average-thrust, presunto quasi-steady) e' il
near-miss dichiarato e il suo full text e' UNREAD (ADV-LX:25-31).

**(2) "P-B usa GIA' il variazionale max-thrust: la vostra frase
'nessuno ottimizza' e' falsa?"**
Se detta cosi', sarebbe indifendibile — e infatti NON e' la frase di
record. P-B applica le superfici variazionali max-thrust
Rao/Vander-Veen, ma a UN singolo stato steady mediato GLOBALMENTE
(p0/T0 time-averaged; corner a p_inf ambiente e a p_b spaziale di
base, Eq. 22/26 — forma source-verified [WB1-R10],
`VERIFY_PB_corner_pb.md`; SYN:33-34): consuma la soluzione classica
single-state, non pone il problema mediato. La frase C-5 "no
optimizer appears anywhere in the four papers" (SYN:58-61) si legge
nel suo contesto: nessun loop di ottimizzazione, nessuna riduzione
per-phase, nessuna condizione di ottimalita' sulla famiglia. I claim
di record sono query-bounded e precisi: C1 (family-averaged classical
contouring) e C2 (averaged Rao-type corner conditions) NOT-FOUND(q)
(LM:354-357). Il deck NON deve dire "nessuno ottimizza": deve dire
"P-B ottimizza lo steady mediato con il variazionale classico; nessuno
deriva condizioni di ottimalita' per la famiglia media/per-phase". E
c'e' un dettaglio a nostro favore dal record: la Eq. (26) di P-B usa
p_b al corner di design SENZA fonte (BPH:723-724), su una chiusura di
famiglia giudicata FAILED da WG10 (BPH:605-610).

**(3) "Le vostre query di novita': quanto sono robuste? Cosa avete
concesso?"**
Robustezza: ogni claim e' NOT-FOUND(q) — legato alle query, mai
assoluto (R5); sweep avversario dedicato 1971->2026 con 4 auditor
indipendenti a mandato falsificatorio: tutti i claim SOPRAVVIVONO nei
bound dichiarati (ADV-LX:1-8), con evidenza affermativa forte sul
ponte (Ancourt-Peter-Atinault 2023 full-text, 47 refs ispezionate,
zero citazioni della scuola classica: "the community best positioned
to state the bridge does not", ADV-LX:17-23). CONCESSO esplicitamente
(LM:451-456): l'equivalenza generica adjoint=moltiplicatore
(Giles-Pierce 2000 p. 397, Lions 1971, Jameson 1988) e la catena
Route B -> Route A DENTRO la scuola classica (KT2015); "residual
novelty = articulation + operationalization, not mathematical content
of the bridge". CONCESSO anche: la scuola russa chiama internamente i
moltiplicatori "conjugate/adjoint problem" (KT 2015, ADV-LX:10-17).
Rischi residui dichiarati e non riempiti di plausibilita':
ISABE-2003/Bogdanov full text unread (#1), KT2015 reference list
unchecked, Kraiko 1979 TOC unverified (ADV-LX:111-112; LM:359-362).

**(4) "Perche' Humphreys 1971 (un paper del '71 su ugelli steady)
sarebbe rilevante per gli RDE?"**
Perche' e' l'exhibit quantitativo della NOSTRA tesi metodologica, sul
terreno del campo classico: alle pp. 1586-1587, il solo swap del
modello di base pressure (Eq. 12->38) sposta l'altezza di base OTTIMA
di x2.45 e la pendenza al tip da -13.26 a -3.08 gradi, con la spinta
che si muove di +0.26% (BPH:619-625) — il valore e' piatto, l'ARGMAX
si muove a O(1). E' la stessa struttura del rischio RDE (P-B Fig. 15
flat-vs-peaked, P-C flip di ranking: SYN:97-102): le decisioni di
DESIGN sono sensibili dove il VALORE non lo e'. Corollario diretto:
la chiusura p_b ereditata dalla linea Veen e' la Eq. (5.1) WG10,
giudicata FAILED (BPH:605-610) — quindi la disciplina "prezzare le
chiusure a livello design-gradient, non value" (BPH:623-625) non e'
pedanteria nostra, e' una lezione classica del 1971 che, [W2-R7] nei
4 paper letti, non risulta consumata: la chiusura p_b entra al corner
di design senza fonte ne' sensitivity (P-B Eq. (26) NO source; Li-Xu
2025 "did not consider the recirculation zone", BPH:723-725).
Classe: [REP] su fonte primaria in-repo.

**(5) (anticipabile) "Vi appoggiate a 4 paper CFD: quanto vi fidate
dei loro numeri?"**
Zero, per regola: CT-6 — P-D si auto-giudica "the absolute values are
completely different" (p. 3451); nessun numero P-A..P-D entra in
bande, barre o posizioni referee; solo meccanismo/topologia/scala-gap,
[ADV] (SYN:158-163, 364-368). Il deck mostra le LORO figure con i
LORO numeri, dichiarati come tali.

**(6) (anticipabile) "Il campo dice che il design su medie funziona —
P-C lo scrive: perche' un programma nuovo?"**
Risposta onesta: P-C dice "approximately applicable" sotto premessa
kHz (pC:147-152) — e gli stessi 4 paper portano il contro-lato:
14.2% di shortfall non decomposto (P-A), 4% di miss del design point
medio, +0.52% invisibile alla curva steady piatta, flip di ranking
(SYN:373-385). Il verdetto di record: scommessa "adequate for sizing,
unpriced at ranking" — R26 APERTA; il programma e' il prezzo di quella
riga, non la sua negazione (CT-7: "if the premise were wrong at
ranking level, the per-phase program is the fix, not the victim",
SYN:165-171).

**(7) [W2-R3] "Vi posizionate su 4 paper CFD; gli esperimenti che
TUTTI e quattro citano (Fotia 2016, Goto 2019, Ma 2023 hot-fire) e il
parent metodologico Li-Xu 2022 non li avete letti: come escludete che
la vostra mappa dei gap sia un artefatto del campione?"**
Risposta dal record: il campione e' dichiarato, non nascosto — 4
paper coupled RDE+nozzle a lettura INTEGRALE (SYN:12-16) piu' il
corpus classico primario in-repo (RAO.pdf, Hoffman, Allman-Hoffman,
Sternin, WG10: LM:368-374, 381-404). Il non-letto e' CENSITO e
tierato: 30 candidati WANTED (8 Tier-1, 22 Tier-2) + 17 Tier-3, con
ordine di procurement proposto W-01..W-08 prima (cluster brief-named
+ all-four-cited + lineage parents), poi W-09 (SYN:607-611); Fotia
2016 = W-01 (citato da TUTTI e quattro), Li-Xu 2022 = W-05 (il
PARENT, "highest method-lineage bearing"), Fievisohn 2018 = W-09
(SYN:510-542). Soprattutto: i claim di novita' NON sono
corpus-bounded ma query-bounded (R5) — C1/C2/C3 = NOT-FOUND(q) su
query dichiarate (LM:354-362) piu' sweep avversario dedicato
1971->2026 a 4 auditor falsificatori (ADV-LX:1-8), che copre il campo
ben oltre i 4 paper. Il rischio residuo che il campione lascia aperto
e' NOMINATO, non negato: aperti 1, 2 e 7 di questo capitolo.

---

## 5. Cosa deve dire il deck

1. [W2-R1] **Nei 4 paper RDE-nozzle letti integralmente: P-B
   ottimizza lo steady mediato GLOBALE col variazionale classico;
   NESSUNO deriva condizioni di ottimalita' per la famiglia
   mediata/per-phase** (C1/C2 NOT-FOUND(q), LM:354-357): Angelino
   ramp su medie / MoC+Rao-Veen classico su medie / nessun design /
   conico fisso; il compagno steady, dove esiste, e' una media
   GLOBALE, piu' cruda della nostra riduzione per-phase (SYN:31-39,
   58-61). Scope esplicito sulla slide: claim sul corpus letto +
   query-bounded, con caveat ISABE-2003 (average-thrust
   time-dependent, presunto quasi-steady, full text UNREAD,
   ADV-LX:25-31) sulla STESSA slide. [Classe: [REP] per-cella, corpus
   [ADV], caveat [SE]]
2. **Due figure del campo raccontano il rischio**: P-B Fig. 15
   (steady piatto vs transient con ottimo e cliff) e P-C Fig. 13
   (flip di ranking a gap 0.2-1.5%) — con i LORO numeri, regola CT-6
   dichiarata sulla slide (SYN:97-102, 353-358, 158-163). [ADV]
3. **La genealogia ci da' il brick, non la soluzione**: la scuola
   Rao-Guderley-Kraiko risolve il contouring ottimo per UN singolo
   stato steady a generalita' piena (inflow vorticoso non uniforme,
   EOS arbitraria) — il "per-phase brick" esiste; il problema MEDIATO
   sotto onda periodica no: C1/C2 NOT-FOUND(q) (LM:299-320, 354-357).
   [risultato classico (teoremi del campo), [REP] su 5 fonti primarie
   in-repo + claim query-bounded — W2-R5]
4. **I tre MANDATORY e la distinzione**: Efremov-Kraiko 2004 (bound),
   Kraiko-Egoryan 2020 (ideal-adaptation come bound), Levin 2010
   (ricerca diretta senza condizioni di ottimalita') — citati in
   slide, con il caveat ISABE-2003 dichiarato (LM:322-342;
   ADV-LX:25-35). [REP + caveat [SE] dichiarato]
5. **Humphreys 1971 come exhibit**: argmax x2.45 a valore +0.26% — le
   chiusure si prezzano al design-gradient; e la chiusura p_b che il
   campo RDE eredita (Veen Eq. 9) e' FAILED per WG10 (BPH:619-625,
   605-610). [REP fonte primaria]
6. **Onesta' strutturale in chiusura di sezione**: 0 teoremi
   contraddetti dai 4 arrivi (SYN:185-188), MA il piu' grande lever
   pubblicato (choking) vive FUORI dalla classe fixed-interface
   (CT-1, decider CFD-1) e nessun referee esterno per-phase esiste:
   il bracket lo chiudiamo noi o non e' chiuso (SYN:87-94, 490-492).
   [verdetto di campagna + OPEN dichiarati]

---

## Disposizione riparazioni (onda 2)

| Finding # | Classe | Disposizione |
|---|---|---|
| 1 | REPAIR | APPLICATO [W2-R1] — deck punto 1 riformulato (P-B ottimizza il mediato globale; nessuna condizione di ottimalita' per-phase), scope corpus+query-bounded esplicito, caveat ISABE sulla stessa slide (ADV-LX:25-31 verificato) |
| 2 | REPAIR | APPLICATO [W2-R2] — §1.1: "definiscono lo stato dell'arte" sostituito con campione dichiarato dal brief; W-05 (SYN:526-528) e W-09 (SYN:540-542) dichiarati inline (ancore verificate) |
| 3 | GAP | APPLICATO [W2-R3] — Q(7) aggiunta con risposta dal record (SYN:510-542, 607-611 verificati; query-bounded vs corpus-bounded) |
| 4 | GAP | APPLICATO [W2-R4] — riga Fievisohn 2018 in §1.5 (ADV-LX:99-100 verificato: "MoC-native unsteady RDE+nozzle lineage, never extended to design"; W-09 SYN:540-542) |
| 5 | DOWNGRADE | APPLICATO [W2-R5] — claim 8 e deck punto 3 rietichettati "risultato classico (teoremi del campo), [REP] su 5 fonti primarie in-repo" |
| 6 | GAP | APPLICATO [W2-R6] — box definizioni media GLOBALE vs riduzione PER-PHASE + mini-legenda sigle in testa a §1.1 (SYN:17-20 verificato) |
| 7 | REPAIR | APPLICATO [W2-R7] — coda Q4 bounded al corpus letto (BPH:723-725 verificato: Eq. (26) NO source; "did not consider the recirculation zone") |
| 8 | NOTE | APPLICATO [W2-R8] — guardia §1.8 taggata [INF]/sintesi-capitolo (miglioria senza rischio) |
| 9 | NOTE | APPLICATO [W2-R9] — claim 10: "DOI dove presenti", 1994 ZhVMMF senza DOI (LM:302 verificato) |
| 10 | NOTE | APPLICATO [W2-R10] — D-6 §1.2: "deve mostrare" marcato come direttiva di consumo S-PRES, frase di record = "the two figures the loop must see" (SYN:353 verificato) |

---

## 6. STORIA (writer W-B.2, 2026-08-23 — trittico [V2-R2]; ogni battuta
## porta DATA + PROCESSO + VERDETTO, campi di join del retro-audit §5-bis)

### 6.1 La genealogia variazionale steady (Rao → Hoffman → Kraiko)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-12/13. PROCESSO:
  mappa di generalizzazione refuter-passed su 24 PDF
  (`validation/ADVISORY_generality_litmap_2026-08-12.md`, sessione
  parallela) + sweep adversarial 1971-2026
  (`validation/ADVISORY_litmap_extension_2026-08-13.md`). VERDETTO:
  linea canonica verificata su fonti primarie (LM:271-283), con lo
  schema comune a DUE moltiplicatori confermato contro cinque fonti.
- **Battuta 2 — (c) NON-RIDERIVATO (una genealogia non si rideriva);
  doppia prova = protocollo litreview a contraddittorio simmetrico +
  refuter d'onda.** DATA: 2026-08-13 (confronto alla riga su 25 paper,
  39 graft / 33 correzioni / zero teoremi caduti,
  `validation/ADVISORY_litreview_confrontation_2026-08-13.md`) +
  2026-08-23 (REFUTE_CH5.md, onda W-A, riparazioni disposte nel blocco
  "Disposizione riparazioni" di questo capitolo). PROCESSO: tier
  [IO]/[REP]/[APERTO], confronto alla riga mai al brief. VERDETTO: la
  linea sopravvive al contraddittorio nei due assi paper+claim.
- **Battuta 3 — convergenza.** DATA: 2026-08-20/21 (finestra C4, chiusura
  in-house del caveat Eq. 14 su RAO.pdf primario, LM:381-386). PROCESSO:
  correzioni incorporate di record (Rao TOP = ARS J. 1960; "Rao 1961" =
  paper SPIKE; Eq. 14 = corner/transversality verificata per-pagina).
  VERDETTO: classe finale [REP] su fonte primaria in-repo.

### 6.2 La dicotomia D-1 e il posizionamento dei 4 metodi

- **Battuta 1 — derivazione originale.** DATA: 2026-08-20. PROCESSO:
  campagna nozzle-RDE 4 paper su ORDINE UTENTE (lancio commit b0a4c15;
  chiusura A CONVERGENZA commit a85e355: 0 BREAK su 8 threat
  consolidati, reviser 9/9 + confirm 9/9 FAITHFUL); lettura INTEGRALE +
  matrice a 7 assi + threat ledger. VERDETTO: nessun paper del campo
  esegue la riduzione per-phase; D-1 è [ADV-FIG] in quattro codici
  indipendenti.
- **Battuta 2 — (c); doppia prova = threat ledger + refuter d'onda.**
  DATA: 2026-08-20 (CT-1..CT-8 consolidate, con CT-6 regola standing di
  consumo: numeri loro, contesto, mai bande nostre) + 2026-08-23
  (REFUTE_CH5.md). PROCESSO: le threat furono costruite APPOSTA per
  schiacciare il progetto e non lo schiacciarono ("nothing crushes the
  project", commit a85e355). VERDETTO: posizionamento regge sotto
  attacco dedicato.
- **Battuta 3 — convergenza.** DATA: 2026-08-20 (chiusura campagna).
  PROCESSO: D-1 fissata come fenomenologia. VERDETTO: classe finale
  [ADV-FIG], "licenses NO magnitude" — mai promossa a numero.

### 6.3 I gap query-bounded C1-C4 e la formulazione P2/G14

- **Battuta 1 — derivazione originale.** DATA: 2026-08-13 (query-bounded
  di record, LM:442-456, su base litmap 2026-08-12). PROCESSO: query
  ensemble/phase-averaged con perimetro dichiarato. VERDETTO:
  NOT-FOUND(q) su C1/C2/C3; C4 PARTIAL; blind spot dichiarato = TOC
  Kraiko 1979 non verificata (passo umano G5 raccomandato pre-stampa).
- **Battuta 2 — (c); doppia prova = contraddittorio + ratifica con
  concessioni.** DATA: 2026-08-13. PROCESSO: sweep adversarial con i due
  near-miss NOMINATI (Kraiko-Tillyaeva 2015, ISABE-2003-117 —
  `validation/ADVISORY_litmap_extension_2026-08-13.md`, "all claims
  survive, 2 near-misses named") + ratifica D-01 eseguita (commit
  ea2abce: glossa CANCELLATA a literature_map+theorem_ledger, claim 1
  P2/G14 RISCRITTO al blocco di record con equivalenza generica +
  catena in-school KT2015 CONCESSE). VERDETTO: il claim sopravvive
  SOLO nella forma ristretta a tre rami (i)/(ii)/(iii) — la concessione
  è parte del claim.
- **Battuta 3 — convergenza.** DATA: 2026-08-13 (forma finale a
  registro). PROCESSO: riscrittura di record. VERDETTO: classe finale =
  claim di novità query-bounded con confini e concessioni dichiarati.

### 6.4 Le correzioni utente come eventi storici del capitolo

- **Battuta 1 — la misquote Harroun (ritirata).** DATA: 2026-08-13
  (finestra sessione letteratura chiusa: glossa e claim-Harroun
  RITIRATI; la ratifica D-01 esegue la cancellazione della glossa a
  literature_map+theorem_ledger — commit ea2abce). PROCESSO: sfida
  utente → verifica alla fonte → RITIRO a registro, mai ammorbidimento.
  VERDETTO: ritiro di record.
- **Battuta 2 — il catch p_b/corner di QUESTA sessione
  (source-verified).** DATA: 2026-08-23. PROCESSO: dubbio utente ("loro
  usano p0 e T0 mediate, credo — cosa sarebbe p_b lì?") → verifica
  MIRATA sul PDF P-B pp. 4-11
  (`validation/spres_raws_2026-08-22/reconstruction/VERIFY_PB_corner_pb.md`).
  VERDETTO: (a) p0/T0 mediate CONFERMATO — l'utente ha ragione; (b) i
  DUE corner sono distinti: corner T a p_inf (Eq. 22), corner J a p_b
  (Eq. 26); (c) "averaged base pressure" = media SPAZIALE steady sulla
  base, MAI collegata dal paper al time-averaging RDE, e il VALORE di
  p_b usato nel design è SENZA fonte dichiarata — correzione LL-20.
- **Battuta 3 — convergenza (il pattern di metodo).** DATA: 2026-08-20
  (sfida utente sulla profondità del lit-census SOSTENUTA 3/4 misurato,
  commit b0a4c15: P-B/P-C/P-D mai emersi = vicinato di citazioni non
  inseguito → emendamento standing del protocollo censimento, riga
  findings coniata). PROCESSO: le correzioni utente entrano come eventi
  datati e producono regole standing, non scuse. VERDETTO: il capitolo
  è onesto PERCHÉ questa catena di catch è a registro.

### 6.5 L'harvest delle ancore fisiche (KP18, Humphreys, Veen)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-20 (base-pressure
  harvest su user catch topology-lens, commit b3da86d: 16 fonti con
  pagine dichiarate; Purdue CTAP = unica misura hot-fire; Veen
  0.846p/M^1.3 tracciata al fit cold 1966 e WG10-FAILED → N2 deve
  sostituirla; Humphreys: lo swap di p_b sposta l'argmax ×2.45 a valore
  quasi piatto +0.26%) + 2026-08-21 (throat harvest, commit 3b2b9e6:
  KP18 Fig. 6 sonic line corrugata + Table 1 unica statistica
  quantitativa di gola). PROCESSO: harvest a lente dedicata, crop e
  numeri per-pagina. VERDETTO: ancore [REP]/[FIG] di record.
- **Battuta 2 — (c); doppia prova.** DATA: 2026-08-20 (rider ADR-D4
  ESTESO su BLOCCATO 9, items 4-6: p_b argmax-criticality, Veen
  never-adopt, Purdue datum — commit b3da86d) + 2026-08-23 (la verifica
  P-B di questa sessione CORROBORA indipendentemente la criticità N2:
  il paper di design del campo usa p_b senza dichiararne la fonte,
  VERIFY_PB_corner_pb.md). PROCESSO: doppio consumo indipendente della
  stessa warning. VERDETTO: la warning "channel-(vi)-shaped" regge.
- **Battuta 3 — convergenza.** DATA: 2026-08-20/21. PROCESSO: regola
  CT-6 standing (numeri loro, mai bande nostre); Humphreys = exhibit del
  principio "ogni chiusura N2 va prezzata a livello design-gradient,
  non a valore" (BPH:623-625). VERDETTO: classe [REP] su numeri altrui,
  consumo vincolato.

### 6.6 La guardia best-of-sweep vs argmax (L11/L12)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-20 (user catch
  SOSTENUTO, commit 904f950: "best-of-sweep != argmax wording guard").
  PROCESSO: catch utente in finestra C4, forma di record in M0
  ([ORCH-HARV-1]). VERDETTO: guardia coniata — nessun confronto in
  letteratura è un confronto con un argmax.
- **Battuta 2 — (b) STANCE-DI-FORK.** DATA: 2026-08-23 (marcatura
  W2-R8 in §1.8). PROCESSO: la lettura L11 è DICHIARATA come
  [INF]/sintesi-capitolo da pC:375-379 + CT-2, non frase di record — il
  verdetto per-riga è portato come stance, con L12 tenuto verbatim
  ([REP p. 11]: "approximately applicable", condizionato alla frequenza,
  dichiarato dal campo stesso). VERDETTO (stance): istanza [ADV] che
  "brushes" la cella (vi), mai chiusura.
- **Battuta 3 — convergenza.** DATA: 2026-08-23 (forma d'atlas).
  PROCESSO: consumo vincolato in §1.8. VERDETTO: classe finale = marker,
  mai prova di stabilità dell'argmax; il rischio ranking resta
  R26/M-RED (CH6).

## 7. Posizionamento / conformity (template §7; nodo N-N) [WB1]

**(a) STRUMENTI — clausola di vacuità [V2-R4]**: NESSUNO STRUMENTO
PROPRIO — questo è il capitolo-senso per eccellenza. Puntatore alla
cella **N-ii = FUORI-PERIMETRO** della tabella §M del design v2
("riga-senso per eccellenza; gli strumenti del campo sono censiti nella
colonna (iii) delle altre righe; CH5 §7(a) = clausola di vacuità con
puntatore QUI"). Il lint 5 riconosce la clausola. **Lint 8 senza oggetto
qui, dichiarato**: nessuna SCELTA di programma è presentata in questo
capitolo — le scelte citate hanno casa e card altrove (C61 → CH6 §8; il
rider CT-4 sul troncamento → dossier ADR-D4, SYN:387-411).

**(b) SENSO**: è l'intero §1 (i 4 metodi, la genealogia, i gap, gli
harvest) + §3-bis (lineage).

**(c) STANDARD DI RIFERIMENTO (lint 6)**: il metodo di questo capitolo è
governato dall'asse **§C-1 (classe PRISMA)** della conformity map del
design v2 — query dichiarate, criteri di inclusione, flusso censito
(registry 174 id con read-status onesto READ-INTEGRAL/READ-PARTIAL/
UNREAD/WANTED), claim di assenza SOLO NOT-FOUND(q); divergenza
dichiarata come da mappa: si adotta la DISCIPLINA (query+flusso+status),
non la checklist 27-item nata per trial clinici — nessun claim di
PRISMA-compliance formale. Nessun claim "SOTA" è fatto in questo
capitolo fuori da quest'asse.

---

## Disposizione W-B.1 (slot B5; celle N-v/A-iii; critic 6/9/11/14/16 + C-7)

| # | Item del mandato | Disposizione |
|---|---|---|
| C-7 (guardia 4) | campo istanziato | APPLICATO [WB1-R1] — §1.1: PKU/NUAA/KIT-Aoyama/NASA-Glenn/Purdue con id registry verbatim (grep-verificati in finestra) |
| critic 6 | remark EAP eco | APPLICATO [WB1-R2] — §1.1 (M0:2526-2539 verificata alla riga; casa principale CH1 §1.2) |
| critic 9 | box nomenclatura | APPLICATO [WB1-R3] — §1.1 box P-B/p_b/PB-2/Gap B + swap gap(A)/(B) + namespace G; casa definitiva CH-REF; legenda CH6 §6 con puntatore |
| critic 16 | P-B Fig. 16 | APPLICATO [WB1-R4] — §1.2 riga con ancore pB:164/283/405 + SYN:54,76-78; riga claim 20 |
| critic 11 | P-C Fig. 21 | APPLICATO [WB1-R5] — §1.2 riga con ancore pC:187-195/269-275/301-303; identificazione K-bar=0 = aggiudicazione DELLO SLOT, dichiarata; riga claim 21 |
| critic 14 (A-iii) | pin esibito/mai spettrale | APPLICATO [WB1-R6] — §1.2 riga a due metà, bounded al corpus (grep in-window), scope separato da R20; riga claim 22 |
| critic 16 | ordine O(10:1) | APPLICATO [WB1-R7] — §1.7 bracket ancorato 6:1-20:1 (THH:415-421, 613) + regola di slide; riga claim 23 |
| Q-iii | eco | APPLICATO [WB1-R8] — §1.6 (query in CH6 §1.2-bis) |
| H-iii (handoff B3) | eco | APPLICATO [WB1-R9] — §1.6 (query completa in CH1 §1.7) |
| §3-bis | antenati LL-2..LL-5, LL-20, LL-22 | APPLICATO — §3-bis (join {LL-id}; copertura lint 7 dei claim C1/C2/C3) |
| [V2-R4] | vacuità §7(a) + metà (c) | APPLICATO — §7 (puntatore N-ii F-P; asse §C-1; lint 8 vacuo dichiarato) |

---

## DECK FEED (asserzioni candidate-slide; frase piena + ancora + classe)

1. "Nei 4 paper RDE-nozzle letti integralmente — PKU `liu_2022`, NUAA
   `li_xu_lv_lv_song_2023`/`li_xu_lv_yu_zhou_2025`, KIT-Aoyama
   `jourdaine_2019` — P-B ottimizza lo steady mediato GLOBALE col
   variazionale classico; NESSUNO deriva condizioni di ottimalità per la
   famiglia mediata/per-fase." — SYN:31-39, 58-61; LM:354-357 — [REP]
   per-cella, corpus [ADV]; caveat ISABE [SE] sulla STESSA slide.
   [FORMA DI SLIDE VINCOLANTE per ogni consumo della frase C-5 "no
   optimizer" (WB1-C3-10): i feed di altri capitoli (es. CH4 feed 8)
   joinano QUESTA forma, mai la frase C-5 nuda — Q2 di questo capitolo:
   "il deck NON deve dire 'nessuno ottimizza'".]
2. "Due figure del campo raccontano il rischio: P-B Fig. 15 (steady
   piatto che non vede l'ottimo transient +0.52%, cliff −5.78%) e P-C
   Fig. 13 (flip di ranking a gap 0.2-1.5%)." — SYN:97-102, 353-358 —
   [ADV], CT-6 dichiarata on-slide.
3. "P-C Fig. 21: forza laterale ~25-35% dell'assiale, rotante a frequenza
   d'onda, media implicita ~0 — la faccia pubblicata della fenomenologia
   K-bar=0." — pC:187-195, 269-275, 301-303 — [FIG]+[INFER] slot, CT-6.
4. "P-B Fig. 16: l'ugello retro-agisce su p0/T0 di camera al variare
   della troncatura — il coupling dati-ugello è la minaccia CT-1, e vive
   FUORI dalla classe fixed-interface." — pB:405; SYN:76-78, 87-94 —
   [ADV-FIG] + fatto di programma.
5. "Il pin single-mode è ESIBITO nei CFD del corpus (P-C: periodicità
   single-mode a ogni stazione) ma NESSUNO dei quattro lo verifica
   spettralmente." — pC:253, 347; grep in-window — bounded al corpus
   letto; scope distinto da R20.
6. "La scuola Rao-Guderley-Kraiko consegna il per-phase brick a
   generalità piena (inflow vorticoso non uniforme, EOS arbitraria); il
   problema MEDIATO sotto onda periodica non esiste in letteratura:
   C1/C2 NOT-FOUND(q)." — LM:299-320, 354-357 — teoremi del campo [REP]
   + claim query-bounded.
7. "EAP = la coordinata-pressione di J_ideal; le sue ipotesi (le nostre
   D1+D2) sono UNSTATED e UNPRICED — il corrector P4 è la barra d'errore
   mancante dell'EAP." — M0:2526-2539 — remark di record.
8. "Humphreys 1971: cambiare la chiusura p_b sposta l'argmax di x2.45
   col valore quasi piatto (+0.26%); la chiusura che il campo RDE eredita
   (Veen Eq. 9) è WG10-FAILED." — BPH:619-625, 605-610 — [REP] fonte
   primaria.
9. "Le escursioni per-fase pubblicate vanno da ~6:1 in gola (KP18
   Table 1) a ~20:1 al combustore (P-C)." — THH:415-421, 613 —
   [REP]+[FIG], CT-6.
10. "Nessun paper del campo dichiara il regime di validità della propria
    media con un prezzo d'errore (NOT-FOUND(q), campo istanziato); e
    nessun referee esterno per-phase esiste: il bracket lo chiudiamo noi
    o non è chiuso." — CH1 §1.7 (H-iii); M0:1322-1331; SYN:490-492 —
    query-bounded + dichiarazione strutturale di record.
