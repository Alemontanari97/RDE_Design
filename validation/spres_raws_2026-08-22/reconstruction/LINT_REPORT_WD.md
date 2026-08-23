# LINT_REPORT_WD — gli 8 lint di completamento atlas (onda W-D, slot D1)

Slot D1 (MECCANICO dichiarato, effort ridotto), 2026-08-23. **Contratto**:
ATLAS_RESEARCH_DESIGN_v2.md §L (:592-621) COME EMENDATO da
ATLAS_DESIGN_v2.1_AMENDMENT.md — clausola di supersessione [R-2] applicata:
"9 sezioni (1, 2, 3, 3-bis, 4-8)", "N-A..N-P + N-Q" (albero 22 nodi),
"gli 8 lint" (6 di v2 + lint 7 lineage §1c + lint 8 card §1g/[GV-2]).
**Oggetti**: CH1-CH10 + LINEAGE_LEDGER.md + matrici in `reconstruction/`.
**Stadio di confronto**: registri di programma su `docs/` (universi misurati
in finestra, SR-12) + tabella §M v2 :303-384 + riga Q amendment §1d + critic
21 righe (§D v2). **Arco di consumo**: D2 (CH-REF dal lint 1, spina
ATLAS_TREE), promozione docs/atlas/, retro-audit del deck (lint 3/4/6/7/8
alimentano il ROBUSTNESS VERDICT [V2-R16]). Tutti i comandi eseguiti in
finestra; nessuna installazione (Python 3.13 stdlib dell'host, script in
scratchpad di sessione).

Universi id misurati in finestra:

    grep -cE '^- id:' docs/claims_registry.yaml      -> 163
    grep -cE '^- id:' docs/findings_registry.yaml    -> 250
    grep -c  '- flag: "A1_' docs/flag_registry.yaml  -> 45
    grep -cE '^- id: C[0-9]+$' docs/choice_ledger.yaml -> 62

==============================================================================
## LINT 1 — REGISTRI (id di programma citati nei capitoli) — VERDE

**Comando**: script stdlib (forward: per ogni id dei 4 registri, match
word-boundary `(?<![\w-])id(?![\w-])` su CH1-CH10; reverse: token id-shaped
nei capitoli non presenti nei registri).

**Esito forward (tabella id→capitolo, input di CH-REF)**: **129 id citati**
in ≥1 capitolo — 49 choice, 65 claims, 15 findings, 0 flag (i flag A1_* non
sono citati nei capitoli: nessun obbligo violato — la riga di legenda
namespace in CH-REF basta). Tabella completa in coda (§ALLEGATO L1).

**Esito reverse (id citati che NON esistono nei registri)**: 53 token
id-shaped fuori registro, TUTTI aggiudicati a namespace dichiarati NON di
registro (quindi **0 violazioni**):

- `C-1..C-7`, `C-1bis`, `C-3bis`, `C-3ter` = correzioni utente del
  checkpoint (SESSION_STATE_checkpoint.md);
- `C-A/C-B/C-C/C-D`, `C-G` = condizioni thermo (riga C24) / case-class del
  contratto (CH10);
- `D-01/D-06/D-1/D-44` = ratifiche/decisioni/guardie di programma; `D-2/
  D-4/D-5/D-6` = ancore `VERDICT_contract_and_L4R1.md#D-n`;
- `S-CERT/S-FOUNDATIONS*/S-ORDINE/S-PRES/S-GAUNTLET/S-GENOAUDIT/S-H` =
  nomi-sessione/remark M0; `S-1/S-2` = ancore `[P2.S-n]` delle matrici;
- `T-1..T-8` = numerazione dei trittici §6 ("**T-n.**"), non id;
- `C-T1` (M0, 3 hit misurati) e `X-T3QS-5F` (M0, 7 hit misurati) = oggetti
  nominati in M0 non ancora a registro, citati con finestra F2 — ancore M0
  esistenti, non fabbricazioni;
- `C-N2` = conditional PROPOSTA con trigger di coniazione dichiarato
  (CH8:200 "va coniata al kickoff PB-2/OP-2");
- `C-SBVF` = citato SOLO dentro la clausola di riparazione CH10:657
  («"C-SBVF" non esiste nei registri») — dichiarazione, non cite;
- `C-O33-STALE-CONDITIONAL` = etichetta `registry-legacy:` con ancora
  findings:747 (CH9:253); `T-GRP10` = citato SOLO nella riparazione CH8:12
  ("il brief chiama 'T-GRP10' ha registry id [T-OP11e]");
- `X-GP01` = etichetta di programma dell'oracolo A1 (D-20, "not built,
  F2-prioritized"), casa a registro = findings `oracles:a1-gp01-quasi1d-
  not-built` (:1478); citata in CH2:653 come oracolo indipendente — label
  di record, non riga claims;
- `J-SEPARATION` = nome della gamba di [T-DISC-2]; `L-P` = residui di
  compatibilità (termine matematico); `C0` = classe di continuità
  (CH8:101), falso positivo del pattern.

**Caveat dichiarato per CH-REF**: il token `C1` è omonimo (choice C1 del
ledger vs "blocker C1" del freeze P-2) — la riga CH-REF deve disambiguare.

**VERDETTO LINT 1: VERDE (0 violazioni).**

==============================================================================
## LINT 2 — MANIFEST [V2-R14] (regola BULK) — VERDE

**Comando**: parse CSV stdlib di `FILE_MANIFEST.csv`; conteggio in finestra:

    righe dati = 825 (+1 header = 826, come da design)

**Regola BULK applicata** (una riga di disposizione per directory-classe;
per-file SOLO docs/src/tests/validation-advisory) — **537 righe bulk in 10
classi**:

| classe (una disposizione per classe) | righe | disposizione |
|---|---|---|
| `**/__pycache__/` (tutte le dir, misurate whole-path) | 97 | bytecode: non-portante per definizione, F-P |
| `validation/sfoundations_raws_2026-08-13/` | 280 | raws Fase A/B/D: sorgente delle STORIE §6 e del lineage; consumo via ancore per-file nei capitoli |
| `validation/sordine_raws_2026-08-13/` | 36 | raws S-ORDINE: storia de-entropizzazione, consumo via PROGRESS_ARCHIVE |
| `validation/sota_gapmap_raws_2026-08-12/` | 17 | raws gapmap: censite nelle card (survey 2026-08-12) |
| `validation/scert_raws_2026-08-13/` | 5 | raws S-CERT: consumo CH9 (verdetto NON-CERTIFICABILE) |
| `validation/spres_raws_2026-08-22/` | 22 | raws di QUESTA missione (snapshot al momento del manifest) |
| `validation/swirl5f_panel_2026-08-19/` | 12 | raws panel swirl5f: consumo CH7 §1.4 |
| `literature_review/reports/` | 31 | report litreview: consumo CH5 via protocollo litreview |
| `literature_review/` (harvest/sintesi top-level) | 28 | classe harvest: consumo CH5 §1.7 + registry |
| `examples/` | 9 | classe esempi eseguibili (R5-adiacenti, no claim propri) |

**288 righe per-file, tutte disposte, 0 orfane**:

- 117 CITATE-ATLAS (basename presente in CH1-CH10/matrici/ledger);
- 46 ADVISORY-INDEX (riga in `validation/ADVISORY_INDEX.md`);
- 27 `validation/*.py` = classe CARRIER-R5 (script committato + test,
  casa = claims/findings registry per id);
- 46 `validation/*.json|*.log|*.patch` = classe ARTIFACT-DI-RUN (evidenza
  campagne S20-S25bis, referenziate dai registri; il `.patch` GENO =
  strumentazione S-GENOAUDIT dichiarata in memoria);
- 15 `tests/*` = classe SUITE (23/23 con incidente dichiarato, CH4 §1.4);
- 10 `src/*` = classe ENGINE (pipeline CH4 §1.2);
- 27 `docs/*` non citati direttamente dall'atlas, disposti per-file in 4
  sotto-classi dichiarate: (a) 2 STORICO-SUPERSEDED con banner
  (`cycle_averaged_variational_nozzle.md`,
  `mathematical_foundations_rde_nozzle.md` — CLAUDE.md); (b) 7 canale
  paper P-1/P-2 (`rde_nozzle_P1_*`, `rde_nozzle_P2_*` — consumo CH6 §1.6
  "canale paper"); (c) 2 ledger di record (`rde_nozzle_theorem_ledger.md`,
  `rde_nozzle_hypothesis_ledger.md` — citati per nome informale, es.
  CH6 "literature_map+theorem_ledger"); (d) 16 dossier/teoria satellite
  di record (`D25U_*`, `G12_S1`, `N6_swirl`, `T3QS`, `LBML`,
  `S1_uniqueness`, `side_load`, `acontraction_attack`, `cauchy_bvp`,
  `general_scheme_panel`, `global_maximum_dossier`, `claims_verdict`,
  `remaining_conditionals`, `brick2_kickoff`, `lit_b0bis`,
  `roadmap_geno_rde`) — consumo via M0 Parte VII (mappa D-doc), non via
  atlas: disposizione dichiarata, non orfane.

Nota di misura: il "~61 righe pycache" di v2 era un aggregato a 2 livelli;
la misura whole-path di finestra dà 97 (include i `__pycache__` annidati
sotto `src/*` e `tests/`). Conteggio, non discrepanza di sostanza.

**VERDETTO LINT 2: VERDE (825/825 righe disposte, 0 orfane sotto la
regola BULK).**

==============================================================================
## LINT 3 — MATRICE [V2-R1] (tabella §M + riga Q; 85 celle) — 2 VIOLAZIONI

**Comando**: parse della tabella §M (v2 :303-384) + riga Q (amendment §1d);
per ogni cella, grep dell'anchor `CHn §x` contro gli header dei capitoli;
conteggi RICALCOLATI enumerando (SR-12):

    celle enumerate = 85
    COPERTA=31  PARZIALE=14  SCOPERTA=34  F-P=6
    per riga: A..P = 5 ciascuna (16 righe) + Q = 5

I conteggi ricalcolati COINCIDONO con l'amendment §1d (31/14/34/6 = 85).

**Verifica per stato**:
- **31 COPERTE**: tutti gli anchor dichiarati esistono (header verificato
  via grep; range "§1.2-1.4" verificati sull'estremo sinistro).
- **34 SCOPERTE**: la sezione dichiarata è ORA SCRITTA e sostanziale
  (lunghezze misurate, estratto: CH2 §7 = 5906 char; CH3 §7-DWR = 6889;
  CH7 §7 = 6381; CH8 §7 = 9595; CH8 §1.7 = 7270; CH1 §1.7 = 7669; CH9
  §1 = 2010; CH10 §1 = 8489; CH9 §(a-bis) = 2003; CH6 §1.2-bis = 7024;
  CH8 §3.5 = 1860; CH4 §1.6 = 3262). Le celle query (G-iii, H-iii,
  J-iii, Q-iii) portano NOT-FOUND(q) nel capitolo dichiarato (grep
  verificato). P-i = §6 in 10/10 capitoli (misurato al lint 5). P-iii =
  mappa §C di v2 + metà (c) in ogni §7 (misurato al lint 5). **P-v =
  inventario rami (c): atterra in CH-REF, che è compito D2 A VALLE di
  questo lint** — pending-D2 dichiarato, non violazione (arco §L/D2).
- **6 F-P**: ragione presente in-tabella per tutte (B-ii, L-ii, M-ii,
  N-ii, O-ii, Q-ii).
- **14 PARZIALI**: residuo disposto verificato a keyword per 13/14
  (batteria misurata: A-ii `masters_etal_2017` in CH1 §7 OK; A-iii
  phase-locked/CH5 + R20/CH6 OK; A-iv hardware-vs-CFD OK; E-iii CH7
  §7(b) OK; F-v F3 OK; I-ii/I-iii/I-v OK (c9bacd9 = 7 hit in CH4);
  L-i F6 OK; L-v G2/thrust-stand/F4b/freeze/risk-register OK; M-i
  VI.4bis OK; N-v EAP/Fig.21/Fig.16/p_b OK; O-v PB-2/single-instance
  OK) — **1/14 NON disposto** (violazione 1, sotto).

**VIOLAZIONE V-1 (celle D-v e M-v, stessa radice)**: il residuo dichiara
"→ CH3 §3 aperto nuovo + roadmap CH6" (D-v) e "+ riga roadmap CH6 §1.5
(F5b: trigger derivato come NUMERO, D6 :271-273)" (M-v). La metà CH3 è
atterrata (CH3 §3 aperto 12 [B3-G34], G3+G4 con ancore, :439-457). La
metà CH6 NO — comando misurato:

    grep -c "G3" CH6_value_honesty_roadmap.md   -> 0
    grep -n "F5b\|unstead\|corrector" CH6_value_honesty_roadmap.md -> 0 righe pertinenti

CH6 §1.5 (roadmap, letto integrale :305-361) elenca M-RED/CFD-2/CFD-1/
G2/F4b/rischi ma NON la riga G3/F5b; CH3:455 dichiara "eco roadmap in
CH6 §1.5" — l'eco NON esiste (cross-ref pendente). Il nodo N-M non è mai
nominato in CH6 (`grep -c "N-M" CH6 -> 0`).

**VIOLAZIONE V-2 (cella K-iv, terza gamba)**: dichiarata "CH10 + puntatore
CH4 §1.2 + CH6 ask". CH10 casa organica OK (8 hit "Annex B"); CH4 §1.2
OK ("ANNEX B di D6", CH4:105-108). CH6 ask NO — comando misurato:

    grep -in "annex\|input serve\|che input\|cosa ci serve" CH6_value_honesty_roadmap.md -> 0 righe

CH6 §1.6 (ASK di record, letto :362-400) porta CFD-1/dati-R20/canale
paper/procurement ma NESSUN puntatore Annex B / input taxonomy; CH10:274
delega esplicitamente "(CH6 §1.6 per le ASK)" — arco monco dal lato CH6.

**VERDETTO LINT 3: 2 VIOLAZIONI** (83/85 celle verificate; V-1 = residuo
D-v/M-v metà CH6 non atterrato; V-2 = gamba "CH6 ask" di K-iv assente).
Entrambe sono righe singole a casa nota: riparabili da un edit B5-class in
CH6 (§1.5 riga G3/F5b; §1.6 riga Annex B) o FINDING a registro.

==============================================================================
## LINT 4 — CRITIC (21 righe, disposizione ESEGUITA) — 2 VIOLAZIONI (stessa radice del lint 3)

**Comando**: per ogni riga della tabella §D (v2 :463-485), grep del target
di disposizione nel capitolo/file dichiarato.

| riga | classe | verifica misurata | esito |
|---|---|---|---|
| 1 | BLOCKING | tabelle "Disposizione riparazioni (W-A)" presenti in CH7 (12 finding) e CH8 (10 finding); ALTI aggiudicati esplicitamente (CH8 #1-2 "RIPARATO" con ancore ri-verificate; CH7 #2 "classificato ALTO... ACCOLTO IN PIENO", :846) | ESEGUITA |
| 2 | BLOCKING | `WA_A3_storyboard_verify.md` VERDETTO: riga 2 "DISPOSTA-VERIFICATA (forma (b) — composito '4-13' rimosso)" | ESEGUITA |
| 3 | BLOCKING | idem: riga 3 "DISPOSTA-VERIFICATA (forma CH4 W2-R2 esatta, aritmetica coerente)" | ESEGUITA |
| 4 | MAJOR | CH8 §1.7 M1-M5 scritto (7270 char) | ESEGUITA |
| 5 | MAJOR | CH1 §1.7 scritto (7669 char) + `grep -c "B-lite" CH3` = 2 | ESEGUITA |
| 6 | MAJOR | EAP in CH1 §1.2 + eco CH5 (`grep -c EAP CH5` = 12) | ESEGUITA |
| 7 | MAJOR | CH6 §1.5 blocco G2 VALUE GATE + thrust-stand (:330-341) + consumo Q1 | ESEGUITA |
| 8 | MAJOR | CH6 §6 legenda F3/F6 (:721 sgg.) + CH8 §3.5 (1860 char) | ESEGUITA |
| 9 | MAJOR | CH5 box §1.1 + legenda CH6 §6; **casa CH-REF = pending D2 dichiarato** (a valle di questo lint) | ESEGUITA (coda D2 nominata) |
| 10 | MAJOR | CH6 §1.2 riconciliato (disposizione B5 [WB1-R1]) | ESEGUITA |
| 11 | MAJOR | CH5 riga Fig. 21 presente | ESEGUITA |
| 12 | MINOR | `grep -c "band-underinclusion" CH3` = 2 | ESEGUITA |
| 13 | MINOR | CH6 Q1 + §1.4 single-instance [WB1-R3] | ESEGUITA |
| 14 | MINOR | CH5 phase-locked + CH6 §1.6 scope R20 [WB1-R8] | ESEGUITA |
| 15 | MINOR | CH4 §1.4 riga 23/23 + incidente (`grep -c c9bacd9 CH4` = 7) | ESEGUITA |
| 16 | MINOR | CH5 §1.2 Fig. 16 presente | ESEGUITA |
| 17 | MINOR | CH3 §3 aperto G3/G4 SÌ; **riga roadmap CH6 NO (= V-1 del lint 3)** | **PARZIALE** |
| 18 | MINOR | CH6 §1.5 collocazione F4b [WB1-R5] | ESEGUITA |
| 19 | MINOR | CH6 §1.6 canale paper P-1 + P-2 freeze FIRED [WB1-R7] | ESEGUITA |
| 20 | MINOR | CH10 casa + CH4 §1.2 puntatore SÌ; **CH6 ask NO (= V-2 del lint 3)** | **PARZIALE** |
| 21 | MINOR | `REFUTE_W2_minipass.md` esiste (C4, W-C) | ESEGUITA |

**VERDETTO LINT 4: 19/21 ESEGUITE PIENE, 2 PARZIALI** — le 2 parziali
(righe 17 e 20) sono le STESSE violazioni V-1/V-2 del lint 3 (radice
unica, contate una volta nel totale). BLOCKING 3/3 risolte; MAJOR 8/8 con
riga (una con coda D2 dichiarata); MINOR 8/10 piene, 2 parziali.

==============================================================================
## LINT 5 — TEMPLATE [R-2: 9 sezioni × 22 nodi] — VERDE con 2 note

**Comando**: per capitolo, presenza dei 9 slot template (mappa di
equivalenza dichiarata per i capitoli "house" CH1-CH8: §1 Ricostruzione =
DOMANDA+PROPOSTA; §2 Stato per-claim = ANALISI (classi+ancore); §3 APERTI
= STATO; §3-bis = ANTENATI; §4 Domande da panel = DOMANDE; §7 (a)/(b)/(c)
= LETTERATURA-strumenti + POSIZIONAMENTO; §6/6-bis = STORIA; CH9/CH10 in
numerazione template nativa 1..8 + 3-bis).

- **Slot: 10/10 capitoli = 9/9 sezioni presenti** (misurato via header).
  CH6 usa header "6-bis" per la STORIA (il §6 è la legenda W2-R10) con
  dichiarazione esplicita in header — posizione template rispettata.
- **Nodi (22 = Q0 + 4 rami + 16 + N-Q)**: i 17 nodi-domanda/servizio
  mappano ai capitoli serventi (§CH v2 + N-Q→CH6 amendment §1d); token
  del nodo presente nel capitolo per 15/17. Eccezioni: **N-P** (servizio
  distribuito: §6 presente in 10/10 capitoli + CH9 §7(a-bis) governance
  P-ii = 2003 char — servito, il token compare 1 volta in CH9);
  **N-M in CH6 = 0 occorrenze** — è la radice V-1 (metà roadmap assente),
  già contata al lint 3; la metà CH3 di N-M è completa.
- **§6 trittici**: 10/10 capitoli con STORIA sostanziale (7.8k-11k char;
  misura: CH1 9355, CH2 8997, CH3 7812, CH4 10997, CH5 8132, CH6 8721,
  CH7 9135, CH8 9138, CH9 7847, CH10 8060). Battute 2 marcate: 58 totali;
  forme (a)=13, (b)=3, (c)=21 tutte CON ancora; ogni battuta porta
  DATA+PROCESSO+VERDETTO (conteggi DPV 30-54 per capitolo, vincolo
  §5-bis). Ogni (c) porta la doppia prova alternativa (verificato blocco
  per blocco; i 4 flag del primo passaggio erano wrap di riga o forme
  auto-dichiarate con ancora: CH4:853 "è esso stesso una seconda prova
  ostile", CH7:603 [fix ST-C5-15], CH6:862 e CH10:636 wrap). **Nessuna
  battuta "doppia prova: ASSENTE"** = zero FINDING da questo canale.
  **Nota 1**: 2 battute-2 in forma "eventi-correzione, non classificabile
  a/b/c" (CH5 §6.4 e CH6 §6-bis.2) — forma AGGIUDICATA dal refuter
  storie (REFUTE_STORIE ST-C5-12, REPAIR eseguita; eco HISTORIAN_INV_b
  split 0a/0b/4c/1misto): deviazione dichiarata di record, non
  violazione.
- **§7(a)**: ≥1 id registry per strumento in CH1(2), CH2(6), CH3(7),
  CH4(13), CH7(2), CH8(4), CH9(10), CH10(1); CH5 e CH6 = clausola di
  vacuità "NESSUNO STRUMENTO PROPRIO" con puntatore alle celle F-P
  (N-ii; O-ii/L-ii/Q-ii) — riconosciuta [V2-R4].
- **§7 metà (c)**: presente in 10/10 (STANDARD DI RIFERIMENTO / asse §C).
- **Nota 2**: l'inventario dei rami (c) per CH-REF (P-v) è il
  sottoprodotto di questo lint: 21 rami (c) + 2 misto-eventi, consegnati
  a D2 con i conteggi qui sopra.

**VERDETTO LINT 5: VERDE (0 violazioni nuove; radice N-M/CH6 già contata
come V-1; 2 note dichiarate).**

==============================================================================
## LINT 6 — CONFORMITY (SOTA → asse §C o query-bound) — VERDE

**Comando**: grep `SOTA|state of the art|state-of-the-art|stato dell'arte`
su CH1-CH10 + check di contesto (±3 righe) per asse §C / query-bound.

**Esito**: **40 occorrenze totali**; 23 con marcatore §C/query-bound nel
contesto immediato (terne "mondo-SOTA (id registry)" del §7(a) = formato
§C-dichiarato; dichiarazioni esplicite "Nessun claim SOTA fuori da questi
assi" in CH4:970, CH5:940, CH6:918); 17 residue aggiudicate a lettura:

- 15 = header di campo card "RECENCY/SOTA check" (nome del campo 4 del
  formato §1g, non claim — il campo stesso porta data + token ATTUALE/
  STALE, verificato al lint 8);
- 1 = CH6:902, citazione della cella L-ii di v2 ("la SOTA tool matrix
  D6 §4" = nome proprio della matrice del piano, non claim);
- 1 = CH10:612, **nota-borderline dichiarata**: citazione VERBATIM del
  verdetto d'audit ("are non-redundant work the SOTA never did",
  `VERDICT_hypothesis_audit.md:459`, ancora citata in riga, dentro una
  battuta §6 con DATA+PROCESSO+VERDETTO) — claim di un documento di
  record citato con ancora, non claim nuovo del capitolo. Se il deck la
  solleva a slide, il retro-audit [V2-R16] DEVE portarla con l'ancora e
  l'asse §C-7 (verifica avversaria) — nota consegnata al Blocco 2.

**VERDETTO LINT 6: VERDE (0 violazioni; 1 nota-borderline consegnata al
retro-audit).**

==============================================================================
## LINT 7 — LINEAGE (claim di novità → LL-id in §3-bis o NOT-FOUND(q)) — VERDE

**Comando**: (i) walk delle sezioni §3-bis di CH1-CH10 (presenza, LL-id,
NOT-FOUND); (ii) grep novelty (`novel|novità|per primo|first to|nessuno
ha/fa/dichiara|mai fatto/derivato/dichiarato/proposto|never been/done`) +
contesto ±3 righe; (iii) check LL-id citati vs ledger.

**Esito**:
- LINEAGE_LEDGER: 37 righe LL-1..LL-37 (misurato), stato ADJUDICATED
  post-C6.
- **§3-bis presenti 10/10**, ognuno con LL-id: CH1=5, CH2=5, CH3=4,
  CH4=8, CH5=10, CH6=4, CH7=3, CH8=6, CH9=4, CH10=5 (+ NOT-FOUND
  espliciti in CH1/CH4(2)/CH5/CH6/CH9).
- **0 LL-id citati che non esistono nel ledger** (in nessun capitolo).
- Sweep novelty: 61 hit; 45 con LL/NOT-FOUND/query-bound nel contesto
  immediato; 16 residui letti e aggiudicati TUTTI non-violazioni: guardie
  anti-claim (CH5:377/381, CH7:763), forme vincolate con near-miss citato
  (CH6:671/842 — locked formulation D-06 + Efremov-Kraiko 2004 come
  query-bound, frase generica "DEAD of record"), lista P0-non-letti che
  CONDIZIONANO il claim (CH1:401, ancora M0:2339-2350), ordinamenti "per
  primo"/meta (CH1:341, CH3:170, CH6:225, CH8:910, CH9:157 esso stesso
  query-bounded, CH4:604 quote ledger, CH5:38 legenda, CH5:518/600 meta).

**VERDETTO LINT 7: VERDE (0 violazioni).**

==============================================================================
## LINT 8 — CARD [GV-2] (6/6 campi + date 2/4 + token campo 4) — VERDE

**Comando**: enumerazione card (`### CARD|**CARD|**DECISION CARD` + lista
numerata non-aggiudicate CH4) + parser campi; copertura TOTALE, non
campionaria.

**Esito enumerazione**: **31 card piene + 1 puntatore dichiarato** =
- CH1: C1. CH2: C56. CH3: 2 card cell-level (forchetta [R22F-FORCHETTA];
  route corrector M-i) — entrambe con dichiarazione esplicita "Nessuna
  riga choice_ledger propria (dichiarato)" nel campo 1: forma onesta.
- CH4 §7-bis: C31 (card di riferimento OBBLIGATORIA: presente, con Uno
  censito `vanaret_leyffer_2026_uno`+`vanaret_montoison_2026_joss`, repo
  QUARANTINATO, campo 4 `ATTUALE(engine NLP... 2026-08-23)`, finestra
  F2-entry — CONFORME all'esempio vincolante §1g), C58 (token
  `STALE → finestra F2-entry` — l'unico STALE, corretto: survey G0
  2026-07-17), C49, C24 + 9 non-aggiudicate (C17, C18, C25, C38, C55,
  C57, C59, C60, C62).
- CH6 §8: C61 (casa PRIMARIA di record, dedup WB1-C3-17) + C59.
- CH7 §7: C51 non-aggiudicata. CH8 §7(d): card F-ii (cell-level), C1,
  C57 + **puntatore C61** ("PUNTATORE alla casa primaria" — conforme
  all'ordine dedup: CH8 tiene solo il puntatore). CH9 §7: J/1 (DIR-G0),
  J/2, J/3. CH10 §5.1: C50, C52, C53, C54.

**Campi [GV-2], misurati su tutte le 31 card piene**: 6/6 campi presenti
31/31; data parsabile (YYYY-MM o YYYY-MM-DD) nel campo 2: 31/31; nel
campo 4: 31/31; campo 4 chiude con token canonico `ATTUALE(perimetro,
data-check)` o `STALE → finestra`: 31/31 (30 ATTUALE, 1 STALE = C58,
con finestra F2-entry nominata). (Il primo passaggio del parser aveva
flaggato le 9 card-lista di CH4 per formato inline "(2)..(6)": ri-parse
dedicato = 9/9 campi 2-6 presenti, date 2/4 presenti, token presenti;
campo 1 = id in grassetto in testa riga.)

**Righe SA/NEVER vs card "non-aggiudicata"**: dal ledger (comando in
finestra) `status: SINGLE-AUTHOR` = 2 (C17, C18); `status: NEVER` = 12
(C25, C38, C51, C52, C53, C54, C55, C57, C59, C60, C61, C62) — conteggio
di record 12/36/12/2 confermato. **Card non-aggiudicate stampate: 14/14
id coperti** (CH4: 9; CH7: C51; CH10: C52/C53/C54; CH6: C61), con campo 3
"NON AGGIUDICATA" e campo 6 finestra Y nominata. **C61 primaria-unica in
CH6** con puntatore in CH8 — esattamente la forma attesa.

**Nota (non violazione)**: C57 e C59 hanno DUE card piene ciascuna
(CH4+CH8; CH4+CH6): conforme alla regola di ownership §1g ("ogni writer
compila le card delle scelte che il SUO capitolo presenta") — il dedup a
primaria-unica era ordinato SOLO per C61 (WB1-C3-17). Le coppie sono
coerenti tra loro a lettura (stessa finestra, stesso verdetto); consegna
al retro-audit: se una slide-scelta cita C57/C59, scegliere UNA card come
sorgente.

**VERDETTO LINT 8: VERDE (0 violazioni; 1 nota di duplicazione conforme).**

==============================================================================
## VERDETTO FINALE (8 righe)

| # | lint | verdetto |
|---|---|---|
| 1 | Lint-registri | **PASS** (129 id→capitolo per CH-REF; 0 id inesistenti; 53 token aggiudicati a namespace dichiarati) |
| 2 | Lint-manifest [V2-R14] | **PASS** (825 righe: 537 bulk/10 classi + 288 per-file; 0 orfane) |
| 3 | Lint-matrice [V2-R1] | **FAIL — 2 violazioni** (85 celle ricontate 31/14/34/6; V-1 residuo D-v/M-v metà CH6; V-2 gamba "CH6 ask" di K-iv) |
| 4 | Lint-critic | **FAIL — stesse 2 radici** (19/21 piene; righe 17 e 20 PARZIALI = V-1/V-2; BLOCKING 3/3 risolte) |
| 5 | Lint-template [R-2] | **PASS** (9 sezioni × 10 capitoli; 22 nodi serviti; 58 battute-2 in {(a),(b),(c)} o forma ST-C5-12 aggiudicata, tutte con ancora; §7(a)/(c) conformi; 0 "doppia prova: ASSENTE") |
| 6 | Lint-conformity | **PASS** (40 occorrenze, 0 violazioni, 1 nota-borderline CH10:612 al retro-audit) |
| 7 | Lint-lineage | **PASS** (§3-bis 10/10 con LL-id; 0 LL inesistenti; 61 hit novelty, 0 violazioni) |
| 8 | Lint-card [GV-2] | **PASS** (31 card 6/6+date+token; 14/14 SA/NEVER stampate; C61 primaria-unica; C31 conforme all'esempio vincolante) |

**VIOLAZIONI TOTALI (radici uniche): 2**

- **V-1** — riga roadmap G3/F5b ("trigger derivato come NUMERO", D6
  :271-273) ASSENTE in CH6 §1.5; dichiarata da celle D-v/M-v, critic 17
  e dal cross-ref CH3:455 ("eco roadmap in CH6 §1.5"); N-M mai nominato
  in CH6. Riparazione = 1 riga B5-class in CH6 §1.5 (o FINDING a
  registro con owner).
- **V-2** — puntatore Annex B / input taxonomy ASSENTE in CH6 §1.6 (ASK);
  dichiarato da cella K-iv, critic 20 e dalla delega CH10:274 ("CH6 §1.6
  per le ASK"). Riparazione = 1 riga B5-class in CH6 §1.6 (o FINDING).

Note consegnate a valle: pending-D2 (CH-REF: tabella L1, inventario rami
(c), casa critic-9); nota-borderline lint 6 e nota-duplicazione lint 8 al
retro-audit del deck [V2-R16]; caveat omonimia C1 per CH-REF.

==============================================================================
## §ALLEGATO L1 — tabella id→capitolo (input CH-REF; trascrizione integrale del comando in finestra)

### choice (49 id citati)

| id | capitoli |
|---|---|
| `C1` | CH1, CH2, CH4, CH5, CH6, CH7, CH8, CH9 |
| `C2` | CH1, CH4, CH5, CH8 |
| `C3` | CH4, CH5, CH6, CH7, CH8 |
| `C4` | CH1, CH3, CH4, CH5, CH6, CH7, CH8, CH9, CH10 |
| `C5` | CH4, CH7 |
| `C6` | CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH8, CH9, CH10 |
| `C7` | CH8 |
| `C9` | CH2, CH3, CH4, CH8, CH9 |
| `C10` | CH5 |
| `C11` | CH2, CH3, CH4, CH9 |
| `C12` | CH4 |
| `C13` | CH2, CH4 |
| `C15` | CH4 |
| `C16` | CH4 |
| `C17` | CH4 |
| `C18` | CH4 |
| `C19` | CH4 |
| `C20` | CH2, CH4 |
| `C22` | CH4 |
| `C23` | CH4 |
| `C24` | CH4 |
| `C25` | CH3, CH4, CH6 |
| `C26` | CH4 |
| `C28` | CH4 |
| `C30` | CH4 |
| `C31` | CH1, CH2, CH4, CH8, CH9 |
| `C32` | CH2, CH4 |
| `C34` | CH4 |
| `C38` | CH4, CH6 |
| `C40` | CH4 |
| `C44` | CH4, CH9 |
| `C45` | CH4 |
| `C46` | CH4 |
| `C47` | CH4 |
| `C48` | CH4 |
| `C49` | CH4, CH8, CH9 |
| `C50` | CH4, CH9, CH10 |
| `C51` | CH4, CH6, CH7 |
| `C52` | CH4, CH6, CH10 |
| `C53` | CH4, CH6, CH10 |
| `C54` | CH2, CH4, CH6, CH10 |
| `C55` | CH4, CH6 |
| `C56` | CH2, CH4 |
| `C57` | CH4, CH6, CH8 |
| `C58` | CH2, CH4, CH8, CH9 |
| `C59` | CH4, CH6 |
| `C60` | CH4, CH6, CH8 |
| `C61` | CH4, CH5, CH6, CH8 |
| `C62` | CH4, CH6 |

### claims (65 id citati)

| id | capitoli |
|---|---|
| `C-D25U` | CH2, CH9, CH10 |
| `C-HT4` | CH1, CH6, CH8, CH10 |
| `C-IGMIX` | CH10 |
| `C-MAJDA` | CH2, CH9, CH10 |
| `C-O33` | CH2, CH9, CH10 |
| `D-CONTRACT` | CH1, CH10 |
| `D-GSEP` | CH10 |
| `D-MU` | CH1 |
| `DIR-G0` | CH4, CH9 |
| `DIR-THERMOTAB` | CH4 |
| `PAN-S14` | CH1, CH2, CH6, CH7, CH8 |
| `S-5F` | CH3, CH4, CH6, CH7 |
| `S-BLITE` | CH1, CH3 |
| `S-GBE` | CH1 |
| `S-LBML` | CH9 |
| `S-T0P` | CH1 |
| `T-A2` | CH2 |
| `T-A3` | CH2 |
| `T-DISC` | CH3, CH4, CH6, CH7, CH10 |
| `T-DISC-1` | CH3, CH7, CH10 |
| `T-DISC-2` | CH3, CH7, CH10 |
| `T-DISC-3` | CH3, CH7, CH10 |
| `T-DISC-4` | CH3 |
| `T-EQBR` | CH3 |
| `T-G12S1` | CH2 |
| `T-GB` | CH8 |
| `T-LEMA-CL` | CH2 |
| `T-LEMB` | CH9 |
| `T-N6-2` | CH7 |
| `T-NSW` | CH1, CH2, CH10 |
| `T-O2` | CH3, CH5, CH6, CH10 |
| `T-OP11e` | CH8 |
| `T-P3` | CH2 |
| `T-P7S1` | CH2, CH8 |
| `T-RED` | CH3, CH6, CH7 |
| `T-RED-1` | CH7 |
| `T-RED-2` | CH7 |
| `T-RED-2G` | CH3 |
| `T-T0` | CH1 |
| `T-T0P` | CH1, CH3, CH6, CH7 |
| `T-T0P-E` | CH1 |
| `T-T3` | CH2, CH8 |
| `T-T3-MAP` | CH1, CH3, CH8 |
| `T-T3-SI` | CH1 |
| `T-T4` | CH1, CH6, CH8 |
| `T-T7CN` | CH1, CH2 |
| `T-T7FS` | CH1, CH2 |
| `T-T7RED` | CH1, CH2 |
| `T-TH0` | CH10 |
| `X-A1IM` | CH9 |
| `X-CDKAT` | CH9 |
| `X-G0` | CH2, CH9 |
| `X-G0AX` | CH2, CH9 |
| `X-GBE` | CH1 |
| `X-GENOXC` | CH4, CH9 |
| `X-GRP06` | CH1, CH8 |
| `X-GRP10` | CH1, CH8 |
| `X-GRP12` | CH1, CH8 |
| `X-LSG0` | CH4 |
| `X-O31CS` | CH9 |
| `X-O33B` | CH9 |
| `X-SPDB` | CH4 |
| `X-T0P` | CH1 |
| `X-THC1` | CH4, CH9 |
| `X-TOCV` | CH8, CH9 |

### findings (15 id citati)

| id | capitoli |
|---|---|
| `audit-scert:anti-remint-evasion-classes` | CH9 |
| `audit-scert:future-pass-dates-accepted` | CH9 |
| `audit-scert:h4-doctored-rejector-vacuous` | CH9 |
| `audit-scert:ondemand-no-run-artifacts` | CH9 |
| `audit-scert:staleness-import-closure-blind` | CH9 |
| `contract:chi-character-map-unknown-band-missing` | CH10 |
| `contract:datum-uncertainty-contract-missing` | CH10 |
| `contract:phase-gauge-jitter-alignment-unpinned` | CH10 |
| `litreview:residue-r8-r23-base-pressure-pb2-blocking` | CH6 |
| `oracles:a1-gp01-quasi1d-not-built` | CH9 |
| `plume:free-boundary-solve-mechanics-missing` | CH8 |
| `registry-legacy:C-O33-STALE-CONDITIONAL` | CH9 |
| `test-suite:ondemand-carrier-exclusion` | CH9 |
| `theory:r22-formal-decomposition` | CH3, CH7 |
| `theory:s-t0p-proof-writeup-pending` | CH1 |

### flag (0 id citati)

Nessun flag A1_* citato nei capitoli (universo 45; obbligo: nessuno — riga di legenda namespace in CH-REF).

Caveat omonimia (dichiarato): il match e' meccanico word-boundary — `C1`
include gli usi "blocker C1" (freeze P-2), `C4` gli usi "touchpoint C4",
ecc.; CH-REF disambigua alla compilazione. Sorgente machine-readable dei
match: `lint1_raw.json` nello scratchpad di sessione, rigenerabile con
`lint_core.py`; i conteggi di questo report sono TUTTI da comando in
finestra (SR-12), mai ereditati.

## ADDENDUM RE-STAMP [FC-1, orchestratore 2026-08-23] — lint 3 e 4 RIVERIFICATI POST-FIX

I fix V-1/V-2 sono atterrati in CH6 (:308-313 riga G3/F5b; :372-377
puntatore Annex B) — riverifica dei criteri falliti, comandi in
finestra:
    grep -c "G3" CH6_value_honesty_roadmap.md  -> 1   (era 0)
    grep -ci "annex" CH6_value_honesty_roadmap.md -> 1 (era 0)
Con V-1/V-2 scaricate: **lint 3 = PASS** (85/85 celle verificate, il
pending-D2 su P-v e' scaricato da CH_REF.md ora su disco) e
**lint 4 = PASS** (21/21 disposizioni critic ESEGUITE — righe 17 e 20
ora piene). **VERDETTO COMPLESSIVO: 8/8 PASS.**
