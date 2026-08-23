# REFUTE_LINEAGE — refutazione avversaria matrice LINEAGE-SWEEP + LEDGER (slot C6, onda W-C.a)

Data: 2026-08-23. Mandato C-1ter lato refuter: attacco alle celle PIENE
(isomorfismo genuino o superficiale?), alle celle VUOTE (davvero
nessuno?), e alla LISTA (GV-1: l'asse a 20 componenti e' completo?), piu'
adjudicazione riga-per-riga del LINEAGE_LEDGER. Oggetti:
`LINEAGE_SWEEP_MATRIX_part1.md` (41x15), `part2.md` (41x15 + colonna
Fievisohn), `part3_newcols.md` (5x82), `LINEAGE_LEDGER.md` (LL-1..LL-35
+ 4 seed). Aggiornamento in-onda recepito: LL-5 riletta dallo stato su
disco POST-affilatura; LL-20 gia' riformulata pre-lancio (VERIFY_PB).

**Stadio di confronto** (artifact-connectedness): ogni claim della
matrice/ledger confrontato con l'ANCORA che cita, mai col ricordo.
Comandi/letture misurati in questa finestra (SR-12):
- `docs/findings_registry.yaml`: mappa integrale degli id con numero di
  riga (`grep -nE "^- id:"`); blocchi letti: :1956-1967 (A31/A33/A35),
  :2002-2012 (C19), :2059-2069 (R3/R4/R7), :2114-2135 (R11, R16),
  :2145-2155 (R20/R25/R26), :2541-2551 (lineage-recognition-gap);
- `docs/literature_registry.yaml`: id+riga per TUTTE le righe :102-1093
  (misurato con awk); summary integrali letti per tutti gli 82 id del
  corpus + i 3 id post-:1070 (sun_nocedal/shi/messud = UNREAD, misurato)
  + tier dei 33 `wanted_*`/`unread_*` esclusi (tutti WANTED paths:[] o
  UNREAD, misurato);
- `docs/rde_nozzle_MASTER.md` :2318-2345, :2905-2930 (KO 3.2, EK 1.7,
  caveat PB-2); `docs/rde_nozzle_literature_map.md` :350-360, :378-390,
  :426-466 (C2 NOT-FOUND(q), Rao Eq.[14], Hoffman 1967/D-01, Sternin);
- `docs/rde_nozzle_pipeline_decision_map.md` :255-320 (machine summary
  79 nodi, roster non-ledger, note_C46); `docs/choice_ledger.yaml` :648
  (C46); conteggio nodi della tabella GV-1 rifatto a mano;
- conteggi celle: part1 80 piene ricontate blocco-per-blocco (=80);
  part2 83+7 ricontate (=83, Fievisohn 7 [IO/REP] + 8 none = 15);
  part3 none-list contate a macchina (python): N-16 78/78, N-17 70/70,
  N-18 76/76, N-19 77 effettive (nota contabile del file corretta),
  N-20 76/76; aritmetiche 615/80/535 e 410/33/377 tornano;
- **DEEP-CHECK alla fonte (2)**: Harroun 2021 pp. 670-673 (pp. 11-14
  del PDF `literature_review/harroun_2021_...pdf`); Fievisohn & Yu JPP
  2017 pp. 89-94 (pp. 1-6 di `C:\Users\amont\Downloads\fievisohn-yu-2016-...pdf`);
- fonti di riforma: `VERIFY_PB_corner_pb.md` integrale;
  `literature_review/reports/paxson_miki_2022_nasa_opt.md` :35-50,
  :175-185, :340-348; `validation/ADVISORY_rde_choking_2026-08-11.md`
  :114-140 (#3-bis); `.../blocco3/NOZZLE_RDE_STUDY_pC_li_xu_2025.md`
  :150; `data/st_opt_validation.md` (esistenza); checkpoint C-1/C-1bis/
  C-1ter (SESSION_STATE_checkpoint.md :100-210); Fievisohn PDFs in
  Downloads (esistenza misurata); CH1/CH2/CH4/CH5 probe di drift (righe
  citate dalla matrice riaperte una per una).

**Arco di consumo**: orchestratore S-PRES (disposizione ledger + repair
matrice) → writer W-B.1 §3-bis + storyboard C6/C7-bis-pre + Q&A deck
(sezione Q&A SEED qui sotto = fronte Purdue/Heister).

---

## 1. PERIMETRO E COPERTURA (right-sizing dichiarato)

- **Celle piene: copertura 100%.** Tutte le 203 celle piene (80 L1 + 83
  L2 + 7 Fievisohn + 33 L3) lette e giudicate genuino/superficiale.
  Fedelta' verificata contro le ancore citate per ogni cella la cui
  ancora e' STABILE (registry/findings/M0/LM/report/PDF: ~45 probe di
  ancora aperti, esiti in §2); le ancore CH sono affette dal drift
  sistemico F-6 e verificate per contenuto via ancora alternativa.
- **Ancore load-bearing del ledger: 20+ aperte** — tutte le righe LL
  poggiano su almeno un'ancora riaperta in questa finestra (dettaglio
  §5); 2 deep-check PDF alla fonte (Harroun = la cella piu'
  load-bearing del corpus; Fievisohn = il seed [IO] nuovo).
- **Celle vuote: campionamento dichiarato** (§4): 20 componenti x 3-5
  celle = 76 celle vuote campionate su ~1437 (~5.3%), regola in §4.
  MAI spacciato per totale: i vuoti non campionati restano coperti solo
  dalla dichiarazione "checked: none" degli slot L, che resta
  falsificabile.

---

## 2. VERIFICHE POSITIVE DI RECORD (cosa REGGE — con evidenza)

**V-1 Harroun 2021 — deep-check duty (a) CONFERMATO alla fonte.**
Letto pp. 670-673: (i) Eq. (10) C_F = F/(P_c A_t) stampata p. 671; (ii)
"This quasi-cycle-averaged result estimated the coefficient of thrust
for both the IE and flared aerospike to be 1.25" p. 671 verbatim —
ranking-blind confermato, e l'esperimento paired (Table 3 + Fig. 22)
SEPARA i due aerospike ("the flared aerospike was outperformed by the
IE aerospike", p. 672); (iii) NESSUNA formula della media stampata: solo
"averaging the discrete constant-pressure axisymmetric computations for
each point in time of the cycle" — peso e denominatore NON dichiarati:
il verdetto L1 "UNDECLARED" e ADVISORY choking #3-bis (":136 THE
AVERAGING CONVENTION IS UNSPECIFIED") sono fedeli alla fonte; (iv)
famiglia per-phase: "A series of axisymmetric simulations ... spanning
the pressure ratios of the detonation-wave cycle" p. 670 verbatim; (v)
"The base pressure ... shown to be poorly predicted with either
analytical models or previous empirical results" p. 672 verbatim.
LL-2 e SEED-1..3 estesi: GENUINI.

**V-2 Fievisohn — colonna [IO] 7/7 fedele alla fonte.** Letto JPP 33(1)
pp. 89-94: abstract p. 89 "the ideal steady-state solution of an RDE in
the wave-fixed reference frame" + "ideal performance estimates one step
up from a basic thermodynamic model ... for large parametric studies" +
"This process is repeated until the solutions converge" (celle (6), (1),
(15) ✓); p. 91 "The authors have not found a mass flow injection
boundary condition for 2-D MOC in the literature. Therefore, a new
boundary..." (cella (5) ✓); jump eqs = Eqs. (12)-(14) esatte (§II.D ✓);
p. 93 "similar to the boundary condition developed by Paxson and
Wilson" verbatim ✓; p. 94 counterflow u_det − u_lab + "total velocity
equal to the detonation velocity D to satisfy the steady-state
requirement" ✓; §III Zucrow-Hoffman + Powers-O'Neill mass-entropy +
slip-line unit process "not commonly in the literature or textbooks" +
3 regioni marciate concorrentemente ✓; Fig. 12 "blocked | unchoked |
choked flow" ✓. Il confine [IO]/[REP] e' rispettato riga per riga: la
SOLA cella (14) e' [REP]-bounded sul nozzled paper assente, chiusa con
"nessun claim oltre questa riga" ✓; il PhD UMD e' su disco e il TOC
senza capitolo ugello e' un claim verificabile dal file. LL-13: GENUINA.

**V-3 LL-5 AFFILATA — verificata contro il report d'esperto.**
`literature_review/reports/paxson_miki_2022_nasa_opt.md` :40-44 stampa
la formula Eq. (1) F = (1/t_cycle)[∬ρv²dA dt + ∬(p−pa)dA dt] ✓; :177-181
(finding F1 CONTAINED): "This is our J = ∫_Ξ F[S;s(ξ)] dμ with μ =
normalized cycle time ... evaluated on an exit-plane control surface
rather than on the wall. They evaluate J; they never differentiate it"
✓; :340-344: "The declared objective and the applied objective differ"
(V5 scelto sotto multi-obiettivo non dichiarato) ✓. La riga LL-5 nella
forma su disco e' fedele, ancora inclusa. REGGE.

**V-4 LL-20 — la forma su disco E' quella riformulata.** Confrontata
clausola per clausola con `VERIFY_PB_corner_pb.md` (d): lip shroud a
p_inf (Eq. 22), base spike a p_b "averaged base pressure" (Eq. 26) =
media SPAZIALE di base, lessico plug steady, MAI cycle-averaging, fonte
e provenienza del valore NON dichiarate ✓✓. REGGE. (Ma vedi F-7: la
prosa sorgente in part2 NON e' stata riformulata.)

**V-5 LL-10/LL-11 procurement-gated: PULITE.** LL-10 attribuisce il
meta-principio a Talley & Coy SOLO come attribuzione primaria di record
via WS-2004 (findings :1959: "primary attribution to Talley & Coy" ✓)
e dichiara "full-text FUORI corpus → candidato procurement" — nessun
claim di lettura o merito ✓. LL-11 conserva "confidenza LOW" e (in
part1) "default-deflazionario", fedele a findings :2059 (R3: "the
trajectory weighs SCALAR parameters, not a shape functional; confidence
LOW") ✓. LL-8 conserva l'identificazione APERTA (R4: "Kraiko 2001 cites
it primarily but does NOT make the identification") ✓ — nessuna
sovra-chiusura.

**V-6 Seed utente 4/4 CONFERMATI, non sovra-estesi.** SEED-1..3: le
estensioni (Harroun copre anche (1); peso UNDECLARED) sono
source-backed (V-1); la promozione Fievisohn a [IO] e' legittima e
dichiarata (documenti primari TROVATI su disco in Downloads, esistenza
misurata; il nozzled 2018-0881 resta [REP]-bounded + procurement RAISED,
riga registry wanted_fievisohn_2018 :1280 esistente ✓). SEED-4
(imposed-BC): P1.6 + antenati steady Humphreys/JTH74 con ancore registry
:364-370/:420-426 verificate ✓; l'estensione operativa Miki (LL-24)
poggia sul verbatim registry "states our gap in its own words" ✓.

**V-7 Asse-colonne (82 id) SANO.** Tutti gli id del registry esclusi
dagli 82 sono WANTED (paths:[]) o UNREAD (unread_cf_aso_preprint,
sun_nocedal_2023, shi_2022, messud_2021 — tutti status UNREAD misurato):
nessun paper LETTO e' fuori matrice. Il claim part3 "5 wanted_* arrivati
inclusi" e' verificato (paths + READ-PARTIAL a registro ✓). La
dichiarazione part1/part3 "Colonne [REP]-bounded: NESSUNA" regge.

**V-8 Conteggi TUTTI riprodotti** (SR-12): 41+41 colonne; 80/83+7/33
piene; 535/377 none; none-list part3 contate a macchina (la nota
contabile N-19 su harroun_2021 e' corretta: 77 effettive). Nessun
conteggio ereditato.

**V-9 Ancore stabili: ~45 probe, esito sano** salvo le riparazioni
F-1/F-6: registry (28 id-riga esatti), findings (24 blocchi, id-riga
combacianti), M0:2908-2926 ✓, M0:2320-2326 ✓ (incl. "optimum COLLAPSES
to steady by the authors' own admission, Summary p.631" = cella EK (6)
✓), LM:354-357/:381-386/:428-441/:457-464 ✓ (D-01 glossa CANCELLATA
riportata fedelmente nella cella hoffman_1967 (11) ✓), pC:150
"approximately applicable ... under the premise" ✓.

**V-10 La trappola C-1ter e' rispettata nelle celle piene.** Ogni cella
piena porta il grading (ISOMORFO / ANTENATO / CAUTA / CONTROESEMPIO /
CONTRASTO) + la clausola "cosa manca vs noi"; le analogie (13) sono
dichiarate CAUTE e mai vendute come isomorfismi; i controesempi
(kraiko_2016, valeriani PSO) sono dichiarati tali. Non ho trovato
NESSUNA cella piena in cui un tema condiviso sia spacciato per procedura
isomorfa — l'inverso del difetto che C-1ter ripara. Nessuna cella piena
cade.

---

## 3. FINDINGS (classe BREAK / REPAIR / GAP / NOTE)

**F-1 REPAIR — ancora findings ":2540" ERRATA (3 celle + 2 righe
ledger).** Part1: KP18 (14) "graft A31, findings :2540"; WS-2004 (8)
"graft A33 ... :2540"; WS-2004 (9) "graft A35 ... :2540"; righe
candidate 9 e 10 (→ LL-9, LL-10) "Ancora: findings :2540". Misurato: il
contenuto A31/A33/A35 vive a `docs/findings_registry.yaml:1956-1967`
(id `litreview:graft-a31-a33-a35-external-precedent-corroborations`);
:2540 cade tra il blocco staged-evidence e il blocco
lineage-recognition-gap. Riparazione: sostituire ":2540" con
":1956-1967" nelle 5 occorrenze (part1) e propagare a LL-9/LL-10 se le
righe verranno dotate di ancora findings diretta.

**F-2 NOTE — ancore header del finding radice imprecise.** Part1 cita
":2550", part2 ":2544": il blocco `methodology:lineage-recognition-gap`
inizia a :2541 (misurato). Interne al blocco, risolvibili; normalizzare
a ":2541".

**F-3 NOTE — range header part1 ":102-490" impreciso.** Le 41 righe L1
stanno in :102-474; :476/:484 sono viviano/valeriani (colonne L2).

**F-4 REPAIR — GV-1: nodo C46 ASSENTE dalla tabella; conteggio
dichiarato non riproducibile.** La tabella nodo→componente di part1
contiene 61 nodi ledger + 17 non-ledger = 78, non 79: manca **C46**
(esiste: choice_ledger :648 "Padded-lane fill policy for the M5c
per-column vmapped bucket executor"; la mappa lo dichiara "not re-listed
per stage", note_C46 :311-312 — la tabella GV-1, che dichiara "il check
e' eseguito su tutti i 79", doveva includerlo comunque). Inoltre il
conteggio dichiarato "46 mappano / 31 no / 2 F-P" non e' riproducibile
dalla tabella: misurato 45 / 31 / 2 = 78. Riparazione: riga
"C46 → NESSUNA → N-17 (padding policy engine-internal)" e conteggio
riemesso 45 / 32 / 2 = 79. L'ESITO dell'asse non cambia (C46 cade in
N-17 gia' istituita): per questo REPAIR e non BREAK.

**F-5 GAP — roster N-17 incoerente su C58 tra tabella e proposta.** La
tabella part1 manda C58 → N-17 (riga stage-6, con nota "C58 tocca 11");
il roster della proposta N-16..N-19 di part1 E il roster di part3
("C16, C27, C29-C37, C40, C44, C48, C57, C60 + SDP parziale") OMETTONO
C58 e dichiarano entrambi "17 nodi" — stesso conteggio, insiemi diversi
(la tabella da' 15+C40+C44 = 17 INCLUSO C58 ma il roster ne nomina 16
SENZA C58 + SDP). Adjudicare: C58 (stack) sta in N-17 con cross-touch
(11), o la sua esclusione va dichiarata. Con la riparazione F-4 il
roster N-17 diventa 18 voci (C46 incluso).

**F-6 REPAIR (SISTEMICO) — staleness delle ancore CH.** I CH1-CH10 sono
stati riscritti dai writer W-B.1 (mtime 08:33-08:44) DOPO la stesura
della matrice (06:12-06:21). Probe misurati: CH4:206-213 (citata per
Uno) → il contenuto Uno sta ora a CH4:222-225; CH4:238-240 (citata per
Masters 20-25 dof) → ora thermo-tables, il contenuto Masters sta a
CH4:255; CH1:355-360 (KO endpoint) → drifted; CH2:349-355 ("citazione
OBBLIGATORIA", riga candidate 1/LL-1) → ora domanda-panel; CH5:101-105
(P-B Fig. 15) → drifted; CH5:58-64 (P-B blocco) ANCORA valida. Ogni
ancora "CHn:righe" di part1/part2/part3/ledger e' quindi inaffidabile
allo stato attuale dei CH. Il CONTENUTO delle celle resta verificato
sano via ancore stabili (V-9). Riparazione (meccanica, non
contenutistica): re-stamp delle ancore CH contro lo stato corrente,
oppure dichiarazione esplicita in testa alle parti "ancore CH valide vs
stato dei CH alla stesura (2026-08-23 ~06:00)" con pin del blob/commit.
E' la classe di staleness intra-finestra gia' nota al programma (RF-1):
la regola "re-chain include re-stamp artifact" si applica.

**F-7 REPAIR — part2 P-B: prosa sorgente NON riformulata dopo
VERIFY_PB.** La cella (14) di li_xu_lv_lv_song_2023 e la riga candidate
5 di part2 portano ancora "corner a p_b MEDIATO", formulazione che
VERIFY_PB_corner_pb.md (d) giudica DA RIFORMULARE (fuorviante: "averaged"
= media spaziale di base, mai cycle-averaging; il corner T usa p_inf).
Il ledger (LL-20) e CH5 ([WB1-R10]) sono gia' riformati; ma il contratto
di join dichiara "la prosa integrale di ogni riga vive nella parte
sorgente [Pn.r]" → un writer che risale a P2.5 consuma la formulazione
morta. Riparazione: nota di supersessione in part2 (cella (14) e riga
candidate 5): "SUPERSEDED da VERIFY_PB_corner_pb.md → forma di record in
LL-20".

**F-8 NOTE — KO-1970 cella (2): "lo chiamano ... 'trajectory-averaged'".**
L'etichetta "trajectory-averaged" e' del NOSTRO record (registry
identity :103; M0 "TRAJECTORY-AVERAGED PRECEDENT"), non lessico del
paper. La colonna "come la chiamano" qui sovra-attribuisce. Riformulare:
"il record lo classifica trajectory-averaged".

**F-9 GAP — demarcazione della componente (3) INCOERENTE tra L1 e L2.**
L1 riserva (3) agli antenati della MEDIA (KO unico "ANTENATO DIRETTO E
UNICO del corpus", Rao 1958 come oggetto single-phase che (**) media) e
lascia (3) vuota per Hoffman 1967, Rao-Beck 94/99, JTH74. L2 invece
riempie (3) per OGNI istanza single-phase di condizione di parete:
viviano, valeriani, KT2015, kraiko_2001, perfino sun (la cui (3) e' una
motivazione FALSA) e ornano (overclaim). Istanza piu' netta della
collisione: la Λ-form/boundary-function sta in (3) in part2 (viviano psi
4.27-4.28 "= FD Lambda-form") ma in (12) in part1 (Rao-Beck Eq. (4) ==
THEOREM (G) = Λ-form). Stesso genere di oggetto, due componenti diverse.
Conseguenza ledger: LL-14 e LL-20 accreditano (3) a KT2015/P-B mentre
LL-7 (Hoffman 1967, che GENERALIZZA la condizione di parete) non porta
(3). Riparazione proposta: regola dichiarata — (3) = SOLO oggetti
wall-condition con media/pesatura o loro antenati diretti (KO; Rao 1958
come oggetto mediato-da-(**)); le istanze single-state passano a
cross-ref "(3s)" dentro (10)/(12) — e ri-etichetta coerente delle 7
celle L2, con LL-14/LL-20 che dichiarano la sotto-classe
("(3)-single-state" vs "(3)-averaged"). In alternativa la regola lasca,
ma applicata ANCHE a Hoffman/RB94/JTH74 (che oggi risultano
falso-vuoti sotto la regola L2).

**F-10 GAP — harroun_2021 (9): FALSO-VUOTO CANDIDATO (dalla mia lettura
alla fonte).** Fig. 21 + testo p. 671 pubblicano lo split additivo del
C_F per SUPERFICIE (plug vs cowl, IE vs flared) — stesso genere della
cella (9) accordata a shepherd_kasahara ("split additivo dei contributi
di spinta con term II ~15-20%"). O si riempie harroun (9) (istanza
per-superficie, con "manca l'identita' dimostrata e il per-fase"), o si
degrada SK17 (9): oggi la soglia e' incoerente. Se riempita, LL-2 o
LL-21 la assorbono.

**F-11 GAP — sun_2019 (10): FALSO-VUOTO CANDIDATO.** Registry :552-559:
"Rao TOC construction with state closure re-based on ..." — una
COSTRUZIONE di contorno via MoC single-state, stesso genere delle celle
(10) riempite per rao_1958 (costruzione TOC) e johnson_boney (MoC
tabulato). L2 ha lasciato (10) vuota per sun. Riempire ("costruzione
TOC single-state a chiusura variabile; manca famiglia e condizioni —
che sun NON ri-deriva, C14") o dichiarare la ragione.

**F-12 NOTE — campione (13): due analogie-cauta non rese.**
kraiko_2016 (confronto two-sided vs simmetrico con criterio
VECTORIAL/Pareto, registry :534-541) e nasa_sp8120 (enumerazione
istituzionale delle famiglie di ugello a livello handbook) sono dello
stesso genere CAUTA delle celle (13) accordate a migdal/veen/
shmyglevskii; vuote senza ragione dichiarata. Peso basso (la componente
e' dichiarata senza antenato procedurale), ma la simmetria di soglia va
ristabilita o motivata.

**F-13 NOTE — campione N-16: nasa_sp8120 vuota, RP1104 piena.** I due
handbook NASA sono il medesimo genere (curve/figure di design a
consultazione); la none-list N-16 non da' ragione per SP-8120.

**F-14 GAP — N-19: P-B e P-C falso-vuoto CANDIDATI.** Il framing
dichiarato della colonna e' "istanze/datum di refereeing ad-hoc —
evidenza PRO la necessita' del tier". P-B (CFD transient che arbitra il
design steady: flat-vs-peaked Fig. 15, cliff −5.78% a 80%) e P-C
(coppie transient/steady con flip a meta' ranking) sono esattamente
questa classe — il referee esterno smaschera cio' che lo stato mediato
non vede — e sono nella none-list SENZA ragione, mentre harroun_2021 e
cooper_shepherd (stesso genere) hanno la cella piena. Riempire entrambe
(coerenti con CT-3: istanze, mai procedura) o dichiarare la
demarcazione (es. "referee INTERNO allo stesso paper ≠ coppia
CFD-esperimento"): se questa e' la regola, va scritta, perche' oggi
harroun_2021 (CFD+esperimento nello STESSO paper) la violerebbe.

**F-15 NOTE — N-20: demarcazione ancourt debole.** "6-bump = test case,
non adjudicazione di basis" vs fernandes N-20 PIENA per l'FFD
dell'occupante: anche ancourt usa una basis (bumps) per design d'ugello
in loop di ottimizzazione (App. C). La distinzione regge solo se la
regola e' "basis su problema di DESIGN d'ugello proprio vs test case
dimostrativo" — dichiararla nella colonna.

**F-16 REPAIR — LEDGER: canale (14) truncation/p_b SOTTO-CONSOLIDATO.**
(i) LL-2 omette la componente (14) di harroun_2021 (base drag 8x,
"poorly predicted" p. 672 — verificata alla fonte in questa finestra) e
il (14) di harroun_2020 (base drag amplificato dal ciclo); (ii) LL-4
omette il (14) di KP18 (A31, igiene di misura); (iii) NESSUNA riga
ledger porta lo stack classico del canale p_b: Veen 1974 (costanti
0.846/M^1.3 = il FONDO dello stack, C61 legacy WG10-FAILED), Onofri
2002 (floor UNRELIABLE [+19%,−15%]), Humphreys 1971 (L'EXHIBIT x2.45 —
pertinente per pin utente C-2), mentre RP1104 e' coperta da LL-23.
Conseguenza: i nodi C61 / DUTY-10 / H20 joinano sul ledger (lint 7)
senza antenati del proprio canale. Riparazione proposta: **riga nuova
LL-36 "stack classico p_b/troncatura"** (Veen → Onofri/WG10 → Humphreys
exhibit → Harroun 2020/21 cycle-amplified; componente 14; ancore
registry :428-434, :436-442, :364-370, :273-285, :633-640) + reintegro
di (14) in LL-2 e LL-4.

**F-17 REPAIR — LEDGER: componenti droppate rispetto alle celle
sorgente, senza regola dichiarata.** Il join di record e' {LL-id,
componenti}; oggi e' lossy: LL-13 omette (14)[REP] (il contenuto vive
solo in prosa); LL-14 omette (4) (KT2015 (2.10) coefficiente terminale,
A13 sign-definite); LL-17 omette (6) (rubino, classe periodica
spettrale); LL-18 omette (2) (zahr, obiettivo time-averaged della
tripla claim-18). Riparazione: reintegrare le componenti (per LL-13
nella forma "(14 [REP]-bounded)") oppure dichiarare in testa al ledger
la regola "solo componenti portanti nella parentesi; il resto in
prosa".

**F-18 GAP — componente (13) senza NESSUNA riga ledger.** Tre analogie
CAUTA in matrice (shmyglevskii, migdal, veen) + 2 candidate dal
campione (F-12), ma zero LL-id: un claim di novita' sul nodo C57 /
tornei di settore non puo' soddisfare il lint 7 ("ogni claim di novita'
cita ≥1 LL-id"). Riparazione: riga dichiarativa **LL-37 "(13) — nessun
antenato procedurale; analogie enumerative CAUTE"** (shmyglevskii Route
A/B + Fig. 4 map; migdal two-wall; veen decoupling; kraiko_2016
Pareto), cosi' il claim di novita' ha l'ancora e la sua forma onesta.

**F-19 NOTE — marching classico (10) non consolidato.** Rao 1958/1961
spike (TOC), Zucrow-Hoffman 1977 (LA fonte degli unit process,
gemellati ESATTI), Moretti (fitted-front) vivono solo come celle: i
nodi C12-C15/C45/C49 joinano su LL-7/LL-12/LL-13 sole. Valutare riga
LL-38 "linea marching/unit-process classica" o dichiarare che il
baseline Rao/Zucrow e' gia' cite-mandatory altrove (M0/LM) e fuori
scopo ledger.

**F-20 NOTE — sigla "pC:" mai definita in part2.** Referente misurato:
`validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pC_li_xu_2025.md`
(:150 "approximately applicable ... under the premise" ✓). Aggiungere
alla legenda.

**F-21 NOTE — Fievisohn (1): cella piena con contenuto di assenza.** La
cella descrive il ruolo di cugino di VALUTAZIONE e dichiara "NESSUNA
famiglia indicizzata dalla fase". Il "1?" del ledger e' onesto: il
punto interrogativo va MANTENUTO in ogni consumo downstream (storyboard,
§3-bis) — mai promosso a (1) piena.

**F-22 NOTE — SK17: gloss e residuo dichiarato.** (i) "fatto
quotient-flavored" in (2) e' una gloss della matrice, non del record
(registry: solo "wave count N cancels") — mantenerla dichiarata come
tale. (ii) Campione (7): il vuoto SK17 non e' ri-verificabile dal solo
record (i modelli PH/axial potrebbero lavorare nel frame d'onda);
l'owner esiste gia' a registro ("choking-relevant re-read queued, never
executed" — registry :316): il residuo e' gated su quella coda, non
nuovo.

**F-23 NOTE — gonzalez_viana (5): residuo di campione dichiarato.** Il
vuoto regge dal record (design per sweep CFD, 1-dof), ma il trattamento
del dato di detonazione all'ingresso dell'ugello non e' esplicitato nel
record: falso-vuoto possibile a bassa probabilita'; probe mirato di 2
pagine alla prossima finestra lit. Nessun claim downstream ne dipende.

**F-24 NOTE — flag part2 "parametrizzazione": assorbito da N-20+N-16,
non da N-20 sola.** La meta' "dof-budget" del flag (Masters prior 20-25
dof → ratchet C7) vive nella cella N-16 di masters; la meta' "censimento
basis" in N-20. La coda del ledger dice "ASSORBITO in N-20": innocuo
(masters/lauer hanno celle in entrambe) ma impreciso — correggere in
"N-20+N-16".

**BREAK: nessuno.**

---

## 4. CAMPIONAMENTO CELLE VUOTE (regola dichiarata + esiti)

**Regola di campione (dichiarata, mai spacciata per totale):** per
ciascuna delle 20 componenti, 3-5 celle vuote a massimo rischio di
falso-vuoto secondo tre criteri: (i) stessa scuola/filone di una cella
piena adiacente sulla stessa componente; (ii) parole-chiave della
componente nella riga registry del paper; (iii) componenti contigue
piene nello stesso paper (chi ha (2) e' sospetto su (8), chi ha (10) su
(11), ecc.). Verifica dai materiali di RECORD (summary registry
integrali di tutti gli 82 id + findings + advisory + VERIFY/report);
deep-check PDF gia' eseguiti su Harroun/Fievisohn (celle piene). Totale:
**76 celle vuote campionate su ~1437 (~5.3%)**. Esiti: **68 vuoti
CONFERMATI; 4 falso-vuoto candidati (F-10, F-11, F-14 x2); 2 residui
dichiarati con owner (F-22ii, F-23); 6 note di demarcazione/cauta.**

| Comp. | Campione (ragione) | Esito |
|---|---|---|
| (1) | gonzalez (scuola single-cycle opt), morris (pulse), liu (scuola average-then-classical), jourdaine (origine premessa), owens | 5 vuoti confermati |
| (2) | harroun_2020 (stessa scuola del pieno 2021), teasley_2023 (NASA), fernandes (obiettivo steady), viviano | 4 confermati |
| (3) | hoffman_1967, rao_beck_1994, jth74 (wall condition rotazionale), sp8120 | confermati SOLO sotto regola L1 → F-9 |
| (4) | vander_veen (consuma corner Rao), rb_booth_1999, humphreys, fernandes | 4 confermati (consumo ≠ istanza; regola da dichiarare, F-9) |
| (5) | gonzalez (inlet detonazione), morris, cooper, stechmann (none motivato in-cella ✓) | 3 confermati + 1 residuo F-23 |
| (6) | paxson_miki (dati interfaccia periodici → demarcato in (15)), schotthofer, janc, morris | 4 confermati, 1 nota demarcazione |
| (7) | shepherd_kasahara (modelli wave-attached?), stechmann, kp18, wolanski | 3 confermati + 1 residuo con owner F-22ii |
| (8) | cooper (pressione media upstream = convenzione non dichiarata — candidato debole per la convention library LL-22), morris, owens, sk17 | 3 confermati + 1 nota |
| (9) | **harroun_2021 (Fig. 21 split per superficie)**, rubino, zahr, gp2000 | **1 FALSO-VUOTO candidato (F-10)** + 3 confermati |
| (10) | **sun_2019 (TOC construction)**, liu (rampa Angelino ≠ MoC ✓), gonzalez, morris (dichiarato NON MoC in-cella ✓) | **1 FALSO-VUOTO candidato (F-11)** + 3 confermati |
| (11) | venditti (adjoint strumentale → demarcato ✓), deuflhard, yamamoto, moretti | 4 confermati |
| (12) | humphreys (34,373/34,375 → adjudicato (5) nella none-list N-19 ✓), moretti, migdal, onofri (→(14) ✓) | 4 confermati |
| (13) | kraiko_2016 (Pareto two-sided), sp8120 (enumerazione famiglie), wolanski, fernandes (NSGA ≠ settori ✓) | 2 note cauta (F-12) + 2 confermati |
| (14) | liu (aerospike: record muto su p_b — confermato dal record), cooper, rao_1961_spike, gonzalez | 4 confermati |
| (15) | owens (adjudicato in-cella ✓), harroun_2021 (separation location ≠ monitor formale), miki, deuflhard (→(12) ✓) | 4 confermati |
| N-16 | sp8120 (handbook charts), migdal, zucrow (textbook ≠ chart), stechmann | 3 confermati + 1 nota (F-13) |
| N-17 | morris (CD "ottimizzato", engine non censito), stechmann/rubino/zahr/gonzalez (tutti con ragione DICHIARATA in none-list ✓ — pratica esemplare) | 5 confermati, 1 nota debole |
| N-18 | morris (✓ dichiarato), valeriani (✓), rb_booth (✓), kt2015 | 4 confermati |
| N-19 | **li_xu P-B**, **li_xu P-C** (transient arbitra steady), ancourt (verifica interna → demarcato ✓), wolanski | **2 FALSO-VUOTO candidati (F-14)** + 2 confermati |
| N-20 | ancourt (6-bump → F-15), gonzalez (✓ dichiarato), liu (✓), jourdaine (✓) | 4 confermati, 1 nota |

Nota di metodo: le none-list di part3 con RAGIONE in-linea per i casi
borderline (es. "stechmann: engine non censito, cella non compilabile
senza deep-check") sono la pratica giusta — e' la stessa disciplina che
F-12/F-13/F-14 chiedono di estendere ai casi che ne sono privi.

---

## 5. LA LISTA (GV-1) — adjudicazione dell'asse a 20 componenti

**Tabella nodo→componente:** verificata contro la mappa di record (79 =
62 ledger + 17 non-ledger, machine summary :262-274; roster non-ledger
combaciante 17/17; C55 e R22-CFD a due stage-face contati una volta ✓).
Difetti: F-4 (C46 assente; conteggio 46/31/2 non riproducibile → 45/31/2
misurato; con C46: 45/32/2 = 79) e F-5 (C58 nel roster N-17).

**Le 2 dichiarazioni F-P:** C47 (numeric lint) e C23 (record-failure
policy) — CONFERMATE: governance di repo/processo, nessun contenuto
matematico-procedurale confrontabile con un corpus. Nessun altro nodo
della tabella e' un F-P mancato (verificato scorrendo i 78: i
candidati piu' vicini, D-44/P34, hanno correttamente una componente
N-19 perche' il tier di evidenza E' parte del metodo).

**Caveat C55 — RISOLTO, N-21 NON necessaria.** Le tre ragioni di part3
reggono: (i) la demarcazione fase/inviluppo e' NOMINATA di record nel
file (non conflazione muta); (ii) il popolamento di una colonna
dedicata sarebbe ≤2 celle su 82 (GP2000 multipoint + al piu' il
candidato debole cooper di §4-(8)) → valvola load-class AG-1
(sufficient-not-optimized, ratificata 2026-08-20) legittimamente
invocata; (iii) l'escalation e' gia' nominata con id riservato (N-21,
mai riuso di N-20). CONDIZIONE del verdetto: la sotto-etichetta
"misura sull'insieme operativo (P_amb)" viaggia CON C55 in ogni consumo
downstream (storyboard, §3-bis, deck) — una cella (8) senza
sotto-etichetta re-innescherebbe l'escalation N-21. Osservazione non
bloccante: la componente (8) ospita ormai tre sotto-assi (misura di
fase/C62; convenzioni-di-media dei paper; inviluppo/C55) — le celle li
distinguono gia' una per una, quindi la famiglia regge.

**Flag part2 "parametrizzazione":** assorbito, ma da N-20+N-16
congiuntamente (F-24) — la formulazione della coda ledger va corretta;
nessun contenuto perso (masters/lauer hanno celle in entrambe le
colonne).

**Completezza dell'asse:** dopo F-4/F-5, ogni nodo dei 79 ha una casa
su {15 componenti C-1ter} ∪ {N-16..N-20} ∪ {F-P}. Non ho trovato un
21-esimo asse mancante: i quattro layer scoperti da GV-1
(chart/engine/thermo/referee) + la parametrizzazione coprono tutti i
nodi orfani; l'unico candidato residuo (inviluppo operativo) e'
adjudicato sopra come sotto-asse di (8) con escalation nominata.
**VERDETTO LISTA: COMPLETA-CON-EMENDAMENTI** (C46→N-17; C58
adjudicato; conteggio riemesso; sotto-etichetta C55 vincolante).

---

## 6. DISPOSIZIONE LEDGER (riga per riga)

Legenda: OK = fedele alla cella sorgente, nessun edit; EDIT = riparazione proposta.

| Riga | Verdetto | Edit proposto |
|---|---|---|
| LL-1 KO 1970 (1/2/3/4/11) | OK — M0:2908-2926 verificata; "citazione OBBLIGATORIA" = M0 "Mandatory citation" ✓ | re-stamp ancora CH2 (F-6) |
| LL-2 Harroun 21+20 (1/2/5/6/8; N-19) | OK nel merito (deep-check V-1) | **aggiungere (14)** — base drag 8x/"poorly predicted" p.672 + 2020 cycle-amplified (F-16) |
| LL-3 Stechmann (1/2/8) | OK — registry :318-325 ✓, 18/18 file esistente ✓ | — |
| LL-4 KP18 EAP (2/8/15) | OK nel merito | **aggiungere (14)** (A31 igiene, ancora findings :1956-1967, F-1/F-16) |
| LL-5 Paxson-Miki (2/5/15) | OK — forma AFFILATA verificata contro report :41-44/:177-181/:343-344 (V-3) | — |
| LL-6 linea imposed-BC (5) | OK — seed C-1bis + antenati steady con ancore registry ✓ | — |
| LL-7 Hoffman 1967 (4/10/11/12) | OK — LM:428-441 ✓ (glossa D-01 cancellata rispettata) | valutare "(3s)" sotto la regola F-9 |
| LL-8 Sternin+RB94 (12) | OK — R4 fedele, APERTA non chiusa (V-5) | **aggiungere Shmyglevskii 1980 (6)** al cluster Λ-form (la cella part1 lo candida; oggi orfano) |
| LL-9 WS-2004 A35 (9) | OK nel merito | ancora findings → :1956-1967 (F-1) |
| LL-10 Talley&Coy (8) | OK — procurement-gated pulita (V-5) | ancora findings → :1956-1967 (F-1) |
| LL-11 Sternin 57/59 (2) | OK — LOW/deflazionario preservati (V-5) | — |
| LL-12 Giles-Ulbrich (11) | OK — "antenato dell'AGGIUDICAZIONE, non del metodo" = framing corretto | — |
| LL-13 Fievisohn (1?/5/6/7/10/15) | OK — [IO] 7/7 alla fonte (V-2); "1?" onesto (F-21) | **aggiungere "(14 [REP]-bounded)"** (F-17) |
| LL-14 KT2015 (3/11/12) | OK — registry :498-505, findings :1849/:1893 ✓ | **aggiungere (4)** (A13 sign-definite, F-17); dichiarare sotto-classe (3)-single (F-9) |
| LL-15 Uno (11/12; N-17) | OK — nessun merito pre-install, O5-class preservata ✓ | re-stamp CH4 (F-6) |
| LL-16 Efremov-Kraiko (2) | OK — M0:2320-2340 ✓ incl. collasso a steady | — |
| LL-17 Rubino (2/11) | OK | valutare "(+6)" (F-17) |
| LL-18 Zahr-Persson (6/11/12/15) | OK — A15/A20 findings ✓ | valutare "(+2)" (F-17) |
| LL-19 GP2000 (2/8) | OK — R11 "nostra inferenza" preservata (findings :2114-2124 ✓, NPSOL caveat incluso nel record) | — |
| LL-20 Li-Xu P-B (3/14) | OK — forma RIFORMULATA = VERIFY_PB clausola per clausola (V-4) | supersessione in part2 (F-7); sotto-classe (3) (F-9) |
| LL-21 Sun/Liu/Miki (9) | OK — A14 findings :1901 ✓ | valutare assorbimento harroun (9) se F-10 accolta |
| LL-22 convenzioni non dichiarate (8) | OK — :2433-2442 ✓; "l'unica pinnata (T-O2)" e' claim nostro di record, non del campo ✓ | candidato debole cooper (§4-(8)) se si vuole la quinta istanza |
| LL-23 Hoffman 87 CTP + RP1104 (14/12; N-16) | OK — registry :561-568/:444-450 ✓ | — |
| LL-24 Miki 2020 (5) | OK — verbatim registry ✓ | — |
| LL-25 Kraiko 2001 (4/12) | OK — F-6/G-a findings :2125-2135 ✓ | (3)/(14) della cella restano in prosa: dichiarare la regola (F-17) |
| LL-26 Schotthofer (8/15) | OK — Krakos order + M8 ✓ | — |
| LL-27 Allman-Hoffman (N-16/N-20/N-17) | OK — registry :388-394 ✓ | — |
| LL-28 Masters+Lauer (N-20/N-16) | OK — "claim in attesa di verifica full-text" preservato in part3 ✓ | re-stamp CH4:238-240 → :255 (F-6) |
| LL-29 Kraiko 2016 (N-20/N-17) | OK — "exact batte i GA" = loro tabella, registry ✓ | — |
| LL-30 Byrd+Nocedal (N-17) | OK — [P-IPADJ] information-only preservata ✓ | — |
| LL-31 linea direct-search (N-17) | OK — evidenza PRO driver = loro dati, con findings :1994 ✓ | — |
| LL-32 JB75+SH71 (N-18) | OK — [DIR-THERMOTAB] registry ✓ | — |
| LL-33 Browne-Shepherd SDT (N-18) | OK — ruolo generatore S11 ✓ | — |
| LL-34 Janc (N-18 CONTRASTO) | OK — threat vector, mai antenato ✓ | — |
| LL-35 Ornano (N-19) | OK — gerarchia implicita, delta ~ tolerance preservato in part3 ✓ | — |
| **NUOVE** | | **LL-36** stack p_b classico (F-16); **LL-37** riga dichiarativa (13) (F-18); valutare **LL-38** marching classico (F-19) |

Seed utente: 4/4 CONFERMATI (V-6), nessuna sovra-estensione trovata.

---

## 7. Q&A SEED — obiezioni di lineage sostenute (fronte Purdue/Heister)

**Q1. "Harroun (Purdue/Heister) ha gia' fatto il cycle-averaged
aerospike: cosa aggiungete?"**
R: Si' — ed e' l'isomorfismo piu' forte del corpus: famiglia di
soluzioni steady indicizzata dalla fase + media sul ciclo (LL-2, la
citiamo come antenato diretto). Ma: (i) la convenzione di media NON e'
dichiarata nel paper — nessuna formula stampata, peso e denominatore
indecidibili (<F/P_c> vs <F>/<P_c> differiscono su cicli 10:1); (ii) il
risultato e' ranking-blind: C_F = 1.25 IDENTICO per i due aerospike che
il LORO stesso esperimento separa; (iii) nessun problema variazionale:
la famiglia e' valutata, mai ottimizzata. Noi: misura µ pinnata a
teorema (T-O2), condizioni di ottimalita' SULLA famiglia, certificati.
Ancora: PDF pp. 670-671 + Eq. (10); ADVISORY choking #3-bis; LL-2.
Backup: slide con quote verbatim p. 671 + tabella <F/P>≠<F>/<P>.

**Q2. "Stechmann (Purdue) ha gia' il modello per-phase."**
R: Confermato e citato (LL-3): blowdown 0-D per-phase, l'UNICO del
filone a dichiarare il peso (mass-weighted, Eq. 4) — l'abbiamo
replicato 18/18 (data/st_opt_validation.md). Manca tutto il livello di
campo: contouring, condizioni di ottimalita', certificazione. E' il
gradino 0-D della nostra scala, non il nostro problema.

**Q3. "Paxson-Miki hanno gia' ottimizzato l'ugello RDRE in CFD."**
R: La loro Eq. (1) E' il nostro J (µ = tempo-ciclo, formula stampata) —
lo diciamo noi per primi (LL-5). Ma su control surface exit-plane, non
parete; VALUTATA, mai differenziata: 7 design OFAT, nessun optimizer, e
l'obiettivo dichiarato differisce da quello applicato (V5 scelto per
diametro/massa, fuori Eq. (1)). "Pressure ratio and throat Mach
ILL-DEFINED" e' una LORO frase (p. 2): il contratto d'interfaccia che
manca e' esattamente il nostro Γ_d. Ancora: report :41-44/:177-181/
:343-344; registry :249-259.

**Q4. "Fievisohn ha gia' il MoC wave-frame per RDE — e nel 2018 con
l'ugello."**
R: Il cugino di metodo piu' vicino, e lo classifichiamo [IO] dalla
fonte (LL-13): wave-fixed frame esplicito, MoC rotazionale shock-fitted
con unit process Zucrow-Hoffman, inflow BC nuova. Ma: una SOLA
soluzione globale del ciclo (nessuna famiglia per-fase), valutazione e
mai design, terminazione a convergenza senza monitor ne' certificati.
Sull'ugello 2018 (AIAA 2018-0881) il paper NON e' nel corpus letto:
claim volutamente [REP]-bounded, procurement gia' RAISED — e il PhD UMD
2016 (letto) non ha capitolo ugello nel TOC. Ancora: JPP 33(1)
pp. 89-94; LL-13.

**Q5. "Il variazionale a spinta mediata l'ha gia' posto la scuola
russa (Efremov-Kraiko)."**
R: Vero, e la frase "first averaged-thrust variational problem" e'
DEAD di record proprio per questo (LL-16): EK 2004 pone il problema
period-averaged Eq. (1.7). Ma senza contorno di parete, e con ottimo
che COLLASSA a steady per loro stessa ammissione (Summary p. 631). Il
nostro claim e' un altro: primo problema di FORMA mediato
NON-COLLASSANTE con parete condivisa (PB-2, formulazione LOCKED
M0:2320-2326). E KO-1970 e' citazione obbligatoria come antenato della
struttura pesata (LL-1).

**Q6. "La macchina adjoint per obiettivi mediati esiste gia' (Rubino,
Zahr-Persson)."**
R: Confermato e citato (LL-17/LL-18): sono i gemelli di MACCHINA — HB
discrete adjoint duality-preserving, fully-discrete adjoint sotto
periodicita'. Proprio per questo il gap che chiudiamo NON e'
tecnologico: e' di FORMULAZIONE (nessuno di loro ha parete Rao-type,
riduzione per-fase, contouring d'ugello). La loro esistenza e'
l'argomento PRO fattibilita' della nostra macchina.

**Q7. "Le medie le usa gia' tutto il campo RDE-nozzle (Li-Xu)."**
R: Il campo media gli INPUT e disegna classico (LL-20, riformulata
source-verified): p0/T0 time-averaged come vincoli, corner del cowl a
p_inf AMBIENTE, p_b di base = media SPAZIALE senza fonte ne'
provenienza del valore, su costanti Veen giudicate UNRELIABLE dal campo
stesso (WG10 ±19/15%). Nessuna condizione di ottimalita' SULLA media
esiste in letteratura (C2 NOT-FOUND, query-bounded). E le convenzioni
di media del campo sono in maggioranza NON dichiarate (LL-22: Harroun
undeclared, Liu Eq. 14, P-C) — la nostra µ e' l'unica pinnata a teorema.

**Q8. "Come fate a dire 'nessuno l'ha fatto'? La letteratura e'
enorme."**
R: Non lo diciamo per ricordo: e' stato eseguito il prodotto cartesiano
{20 componenti strutturali del metodo} x {82 paper letti del corpus} —
1640 celle rese, ogni vuoto dichiarato dopo check, refutato
avversarialmente (questo file), con regola di campione dichiarata; i
claim di assenza forti restano query-bounded (C2 NOT-FOUND(q), LM:354-357)
e i due candidati piu' vecchi/vicini sono gestiti a procurement
dichiarato (Sternin 57/59 LOW; Fievisohn 2018). Ancora: matrice
part1-3 + questo REFUTE.

---

## 8. FUORI-PERIMETRO (dichiarato)

- Ri-lettura integrale degli 82 PDF: eseguiti 2 deep-check alla fonte
  (Harroun 4 pp., Fievisohn 6 pp.) + 3 file di riforma/report; per il
  resto la fedelta' e' verificata contro il RECORD page-verified
  (registry/findings/M0/LM), non contro i PDF — attaccata solo dove il
  record stesso mostrava incoerenza interna.
- La correttezza dei contenuti di record a monte (es. che M0:2908-2926
  sia page-verified S13) e' assunta come di record: attacco alle celle,
  non alla catena S13.
- Il consumo storyboard/deck delle righe ledger (onda a valle) e la
  ri-verifica delle ancore CH dopo l'eventuale re-stamp (F-6).
- I probe residui nominati con owner: SK17 (7) (owner = re-read queued
  a registro), gonzalez (5) (probe 2 pp. prossima finestra lit).

---

## 9. VERDETTO

- **MATRICE (part1+part2+part3): REGGE-CON-RIPARAZIONI.** 0 BREAK;
  nessuna cella piena cade — il grading isomorfo/antenato/cauta e'
  onesto e la clausola "cosa manca" e' ovunque; 2 deep-check alla fonte
  confermano le celle piu' load-bearing; conteggi tutti riprodotti.
  Riparazioni: ancore (F-1 :2540; F-6 drift CH sistemico), demarcazioni
  da uniformare (F-9 su (3); soglie (9)/(10)/N-19/N-20: F-10, F-11,
  F-14, F-15), prosa P-B superseded (F-7), 4 falso-vuoto candidati dal
  campione.
- **LEDGER (LL-1..LL-35 + 4 seed): REGGE-CON-EMENDAMENTI.** Tutte le
  35 righe fedeli alle celle sorgente; LL-5 e LL-20 (le due riformate)
  verificate alla fonte/al report; LL-10/LL-11 procurement-pulite;
  seed 4/4 confermati senza sovra-estensione. Emendamenti: componenti
  droppate da reintegrare o regola dichiarata (F-17), canale (14) da
  consolidare con LL-36 (F-16), riga dichiarativa LL-37 per (13)
  (F-18), ancore F-1/F-6.
- **LISTA (asse a 20): COMPLETA-CON-EMENDAMENTI.** C46 → N-17 e
  conteggio GV-1 riemesso 45/32/2 = 79 (F-4); C58 adjudicato in N-17 o
  spostamento dichiarato (F-5); C55 RISOLTO sotto (8) con
  sotto-etichetta vincolante nel consumo — N-21 NON necessaria; flag
  parametrizzazione assorbito da N-20+N-16 (F-24). Nessun 21-esimo
  asse trovato.

Conteggi per classe: **BREAK 0 · REPAIR 6 (F-1, F-4, F-6, F-7, F-16,
F-17) · GAP 6 (F-5, F-9, F-10, F-11, F-14, F-18) · NOTE 12 (F-2, F-3,
F-8, F-12, F-13, F-15, F-19..F-24).**

---

## 10. ROUND DI RIPARAZIONE ESEGUITO (C6, stessa finestra — pattern V-N2)

Su ordine orchestratore, le disposizioni di questo file sono state
APPLICATE dallo stesso refuter ai 4 file oggetto (unico writer del
round; marcature [C6-REPAIR]/[C6-FILL]/[C6-NEW] in-file):
- **LINEAGE_LEDGER.md**: LL-36 (stack p_b) e LL-37 (dichiarativa (13))
  aggiunte; componenti reintegrate LL-2(+14), LL-4(+14), LL-8(+Shm.
  1980), LL-13(+14 [REP]-bounded), LL-14(+4), LL-17(+6), LL-18(+2);
  regola-componenti dichiarata in testa; coda corretta (N-20+N-16;
  vincolo sotto-etichetta C55; stato ADJUDICATED; conteggi 81/84+7/35).
- **part1**: nota di drift CH in testa; riga C46→N-17 aggiunta alla
  tabella GV-1 + conteggio riemesso 45/32/2=79 con nota; roster N-17
  reintegrato (C58, C46 → 18 nodi); harroun_2021 (9) C6-FILL (Fig. 21
  split per superficie); ancore :2540→:1956-1967 (6 occorrenze),
  :2550→:2541, :102-490→:102-474; F-8 (etichetta KO) riformulata;
  conteggio piene 80→81.
- **part2**: nota di drift CH + legenda "pC:"; finding radice
  :2544→:2541; sun_2019 (10) C6-FILL (TOC = marcia MoC single-state);
  cella P-B (14) e riga candidate 5 RIFORMULATE alla forma VERIFY_PB
  con puntatore di supersessione a LL-20.
- **part3**: nota di drift CH; P-B e P-C su N-19 C6-FILL
  (referee-ad-hoc transient-vs-steady) + none-list e conteggi riemessi
  (35 piene / 375 none; N-19 7/75); VINCOLO DI CONSUMO C55
  (sotto-etichetta obbligatoria, escalation N-21) e assorbimento
  N-20+N-16 dichiarati nella sezione C55.
NON toccate: LL-5 e LL-20 (già nella forma affilata/riformulata di
record, verificate in §2). Celle riempite totali: **4** (harroun (9);
sun (10); P-B N-19; P-C N-19). Restano aperte (owner nominati, NON
riparabili in-window): F-9 (demarcazione (3), decisione di regola
L1-vs-L2 = orchestratore), F-19 (eventuale LL-38 marching), F-12/F-13/
F-15 (note cauta), residui SK17 (7) e gonzalez (5).
