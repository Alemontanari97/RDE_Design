# CH_REF — Annex di servizio dell'atlas (nessun claim proprio)

Slot D2 (giudizio), onda W-D, S-PRES sessione 2, 2026-08-23.

- **Ruolo di record** (design v2 §Q/§CH): "CH-REF resta ANNEX di servizio
  fuori albero (nessuna domanda propria, nessun claim: mappa id→nodo,
  glossario, legenda namespace, ordine di lettura)". L'ordine di lettura
  vive in ATLAS_TREE.md (consecutio walk, CKP-S2-4); qui vivono legenda,
  inventario rami (c), coda-d'attacco e mappa id→capitolo.
- **Stadio di confronto**: HISTORIAN_INV_a.md + HISTORIAN_INV_b.md (letti
  integrali) + REFUTE_STORIE.md §FP e verdetto + REFUTE_CH9.md §(d) +
  LINEAGE_LEDGER.md (header/code) + le sezioni card dei capitoli
  (CH4 §7-bis, CH6 §8, CH7 :816, CH8 §7(d), CH10 §5.1) + design v2 §M/§L
  + emendamento v2.1 §1d/§1g/§6.
- **Arco di consumo**: retro-audit deck (join disambiguazione namespace);
  storyboard/deck (box nomenclatura); lint 1/8 (D1: la tabella §(d) è
  generata qui per grep e il lint 1 la cross-verifica); F2-entry (la
  coda-d'attacco È l'agenda delle righe non chiuse); promozione
  docs/atlas/.
- Ogni riga qui sotto è consolidamento ancorato di materiale altrui:
  nessuna aggiudicazione nuova. Dove i conteggi degli inventari sono
  stati toccati dalle rietichettature ST-C5-*, vale la regola
  REFUTE_STORIE §FP.4(iii): i conteggi si RIGENERANO da comando misurato
  (SR-12), mai ereditati — i comandi usati qui sono citati in-place.

==============================================================================
## §(a) LEGENDA NAMESPACE + LE DUE COLLISIONI DICHIARATE

### Famiglie di identificatori (per il lettore del deck e del retro-audit)

| prefisso/forma | che cosa nomina | sorgente di record |
|---|---|---|
| C1..C62 | righe del choice ledger (scelte algoritmiche) | `docs/choice_ledger.yaml` (62 righe; tally 12 DECIDED / 36 MIXED / 12 NEVER / 2 SINGLE-AUTHOR, mappa `docs/rde_nozzle_pipeline_decision_map.md:287-295`) |
| C1-C4 (litgap) | i quattro verdetti gap query-bounded della litmap | CH5 §1.6, LM:354-362 — OMONIMIA con le righe ledger C1..C4: il contesto (capitolo-letteratura vs ledger) disambigua; il box nomenclatura CH5 [WB1-R3] la registra |
| CT-1..CT-8 | threat ledger letteratura | CH5 §1.3 |
| PB-1..PB-5 | problemi del problem book §10 | `docs/rde_nozzle_problem_book.md:521-575` |
| P-A..P-D | i 4 paper del campo (censimento) | CH5 §1.1 |
| P-1 / P-2 | i paper del programma (canale JPP / compagno) | D6 :91-100 |
| P-B vs p_b | P-B = paper B del campo; p_b = base pressure | box nomenclatura CH5 §1.1 esteso + legenda CH6 §6 (critic 9) |
| [T-...] / [S-...] | claims con classe THEOREM/SCHEMA | `docs/claims_registry.yaml` (id verbatim) |
| [C-...] (conditionals) | condizionali analitici (C-MAJDA, C-D25U, C-HT4, C-O33) | ledger L4 / claims registry — OMONIMIA di prefisso con le righe ledger C-nn: i condizionali portano sempre trattino+lettere, mai numero puro |
| LL-1..LL-37 | righe del LINEAGE_LEDGER (antenati) | `LINEAGE_LEDGER.md` (ADJUDICATED post-C6) |
| N-A..N-Q | nodi-domanda dell'albero (22 nodi) | design v2 §Q + emendamento §1d |
| G0..G6, G14 | gate del piano / query-gap | D6 (gate) / CH5 §1.6 (G14) — omonimia dichiarata, contesto disambigua (famiglia G già segnalata WB1-C3-11) |
| M1-M5 | meccanismi di globalità | CH8 §1.7 — omonimia con M0-M5ab (milestone S25, memoria s25) : nel corpus atlas M1-M5 = SOLO meccanismi |
| F-1..F-4 | finding "doppia prova" degli inventari storici | HISTORIAN_INV_a §2 — omonimia con F1/F2 (fasi del piano): le fasi non portano trattino |
| CW-1..CW-5 | finding di consecutio del walk | ATLAS_TREE.md (questo round) |
| ST-C5-nn / WB1-* / [W2-*] / [V2-R*] / [GV-*] | fix e riparazioni per onda | REFUTE_STORIE / round W-B.1 / onda 2 / design v2 §F / emendamento §5-ter |

### COLLISIONE 1 — "C31" (ledger-vs-ratifica-cono) [ADIUDICATA in REFUTE_STORIE §FP.1]

Nel corpus S-PRES "C31" indica DUE oggetti DIVERSI, entrambi usati
correttamente nei rispettivi capitoli:

- **C31-ledger** = riga optimizer engine del choice ledger
  (`docs/choice_ledger.yaml:481-493`) — così in CH4 (§6 T-2, card
  C31/engine :991) e CH8 §6 6.5.
- **ratifica-C31** = ratifica utente della forma a CONO della
  trasversalità T7(c) (F-SERVICE 2026-08-13, memoria
  `fservice-scert-double-session`) — così in CH1 §1.5(iv) e CH2 §1.4/§6.

Regola di scrittura (disposizione §FP.1, vincolante per storici,
storyboard, deck, Q&A): scrivere SEMPRE "ratifica-C31" (o "C31-ratifica,
F-SERVICE 2026-08-13") vs "C31 (ledger, optimizer)". Il join del
retro-audit su "C31" nudo è AMBIGUO e va rifiutato. Casa dell'avviso nel
deck: box nomenclatura CH5 [WB1-R3].

### COLLISIONE 2 — "C4" (etichetta-S25 vs finestra) [REFUTE_STORIE §FP.2]

- **C4-finestra** = la sessione S-FOUNDATIONS-C4 (2026-08-20/21, chiusura
  Fase D — memoria `s-foundations-c4-closed`).
- **C4-di-S25** = etichetta interna S25 "C4 MECHANICAL CLOSURE" (commit
  `32459ca`, 2026-08-12; memoria `s25-engine-speed` "C4 CHIUSA").

Questa collisione ha PRODOTTO l'unico errore di data del corpus storie
(CH4 §6 T-6 b3, riparato — ST-C5-07). Regola: ogni occorrenza di "C4"
in storie/deck porta il qualificatore ("finestra C4" / "C4-di-S25").
(Terza omonimia minore, innocua e dichiarata: "C4" è anche il refuter
del mini-pass W-C — solo nei log d'onda, mai nel deck.)

==============================================================================
## §(b) INVENTARIO DEI RAMI (c) NON-RIDERIVATO (consolidato da INV_a + INV_b)

Consolidamento POST-riparazione (REFUTE_STORIE applicato; fix ST-C5-08/
-10/-12/-14/-16/-23 già riflessi nelle righe). Ogni riga = un argomento
di trittico §6 in ramo (c) "NON-RIDERIVATO: nessuna riderivazione
agnostica di record", con la doppia prova alternativa (standard
claim-dual-proof) o il FINDING. Le 12 righe SILENT del ledger (C2 cond.,
C5, C15, C16, C22, C23, C30, C40, C45, C46, C47, C48) sono ramo (c) PER
DEFINIZIONE (phaseB_tree_diff.md:393-399; dichiarato in CH4 §6 testata).

### B8a — CH1, CH2, CH3, CH4, CH7 (INV_a §1, post-fix)

| # | CH · argomento | Doppia prova alternativa | Ancora |
|---|---|---|---|
| 1 | CH1 · T-1 pin dati H3 (pin utente) | pricing boundary [S-T0P] + monitor T0-flatness armato + routing PB-5 | M0:560-561; M0 VI.4bis(v); M0:108-114 |
| 2 | CH1 · T-5 gamba [T-T4] | PAN-S14 arbiter-confirmed + carrier X-GRP06/10/12 + falsificatore O2 | M0:397; claims:329-340 |
| 3 | CH1 · T-5 gamba SHARPNESS (max∫<∫max strictly) | **ASSENTE — FINDING F-1** | M0:2316-2319; problem_book:532-536; CH1 §4 Q4 |
| 4 | CH1 · T-6 [T-T3-MAP] | audit S24 T2a eseguito + corner T-T3-SI provato | M0:4138-4140; M0:879 |
| 5 | CH1 · T-7 gamba [S-GBE] | carrier eseguibile X-GBE PASS | claims:1843-1854 (estendere a :1843-1864, ST-C5-01) |
| 6 | CH1 · T-7 gamba [S-BLITE] | **ASSENTE — FINDING F-2** | M0:3027-3044 |
| 7 | CH2 · T-2 [T-P3] | PAN-S14 16/16 + bench O3.3 PASS criterio primario S19 | commit 7be8b98; memoria s19; P1:200-203 |
| 8 | CH2 · T-3 locus S19 kernel-stopped | falsificatore misurato a due decadi (2.9e-01 vs 9.4809e-03) + audit scope C1 S21 | M0:3305, :3613; M0:368, :2821 |
| 9 | CH2 · T-4 forma a cono (**') + [T-T7CN] | prova di record con controesempio + rejector S3/A39 + cross-check KT2015 | M0:2862-2874; M0:2830-2861 |
| 10 | CH2 · T-5 TWIN WARNING | prova esistenziale c'è; RILEVANZA (falsificatore a due segni sul parco) **ASSENTE — FINDING F-3** | M0:2895-2907; CH2 §2 |
| 11 | CH2 · T-7 genealogia K-O/Hoffman | litreview avversario alla riga (25 paper, 2026-08-13) | ADVISORY_litreview_confrontation; litmap:451-456 |
| 12 | CH3 · T-1 correzione formal-first | decomposizione ESEGUITA a convergenza in C4-finestra con giudici | findings:1459-1468; blocco3/VERDICT_r22f.md |
| 13 | CH3 · T-5 canale (vi) delta/L_H UNDERIVED | escalation E-5 delta-r4 0 BREAK + probe nonconvex; assenza PER COSTRUZIONE (aperto strutturato, owner F2) — NON finding | VERDICT_escalation_c4; M0:1946-1952, :2078-2112 |
| 14 | CH3 · T-6 M-RED (esecuzione) | spec refutata da probe + giudice PART 3; esecuzione F2-QUEUED sotto G1 — NON finding (structurally-gated) | phaseD_r22f_centerpiece:1237-1374; VERDICT_r22f:90-97 |
| 15 | CH4 · T-1 C58 stack JAX | flip clause quantificata armata + review S25 G0/T2 | G0_decision.md §4 :144-198; memoria s25 |
| 16 | CH4 · T-4 C49 fitted-front [fix ST-C5-08: (b)→(c)] | wave-2 blocco3 ZERO finding + classe S1 riderivata 4/4; adiacenza fork phaseB:233 | VERDICT_wave2; phaseB:330/:233; ledger :682-692 |
| 17 | CH4 · T-6 velocità S25/S25-bis | diff-refuter avversario (2 difetti veri riparati) + diff convergiuto 21/4/0/0 | commit 07400a4; ADVISORY_S25bis_diff |
| 18 | CH4 · T-7 mappa pipeline | passaggio refuter dedicato 0 BREAK/0 REPAIR/5 AMENDMENT/4 NOTE | pipeline_decision_map:317-339 |
| 19 | CH4 · T-8 S-CERT + incidente 23/23 | audit ostile context-free = la seconda prova; incidente colto dal rejector SR-12 | PROGRESS :211 (R33); c9bacd9 vs 7dea386 |
| 20 | CH4 · (testata) 12 righe SILENT del ledger | sotto la granularità degli alberi ciechi; doppia prova = i carrier per-riga del ledger dove esistono | phaseB:393-399; choice_ledger.yaml |
| 21 | CH7 · T-1 correzione utente C-1 (evento storico) | il trittico stesso + camminata C5 (join data+processo+verdetto) | CH7 header :3-8; REFUTE_STORIE blocco CH7 |
| 22 | CH7 · T-4 panel swirl5f [fix ST-C5-14: (b)→(c)] | panel a convergenza con judge-verifier sympy; "panel grades are NOT record grades" — consumo dichiarato a ogni uso | DISPATCH_swirl5f:12-33, :118-128 |
| 23 | CH7 · T-6 saldatura 3 (scaletta unica) [F-4 RIFORMULATA] | doppia prova = REFUTE_CH7 #5 (camminata + riparazione applicata); residuo CONSUMATO da W-C.b (ST-C5-13) — NON più ASSENTE | CH7 §1.5.3; REFUTE_CH7 #5 |

### B8b — CH5, CH6, CH8, CH9, CH10 (INV_b §1/§4, post-riparazione; 0 FINDING)

INV_b certifica per i suoi 5 capitoli: "Ogni ramo (c) porta una doppia
prova alternativa ancorata" (INV_b §2 — zero ASSENTE); le doppie prove
per-argomento vivono nelle rispettive §6 (battute con
DATA+PROCESSO+VERDETTO, guardia 15: B8b 0 HIT).

| # | CH · argomento (c) | nota di doppia prova (dalla tabella INV_b) |
|---|---|---|
| 24 | CH5 · 6.1 genealogia steady (Rao→Hoffman→Kraiko) | litreview contraddittorio + REFUTE_CH5 |
| 25 | CH5 · 6.2 dicotomia D-1 e i 4 metodi | idem |
| 26 | CH5 · 6.3 gap query-bounded C1-C4 / P2-G14 | idem |
| 27 | CH5 · 6.5 harvest ancore (KP18, Humphreys, Veen) | idem (VERIFY_PB 2026-08-23 = evento di questa sessione) |
| 28 | CH5 · 6.6 guardia best-of-sweep (L11/L12) [fix ST-C5-10: (b)→(c)] | L12 + CT-2 + REFUTE_CH5 |
| 29 | CH6 · 6-bis.1 frame Gap A/Gap B | doppia prova ancorata in §6-bis.1 (INV_b riga CH6) |
| 30 | CH6 · 6-bis.3 PB-2 e formulazione LOCKED (D-06) | finder E-K 2004 ri-ancorato a litreview_confrontation:107 (ST-C5-11) |
| 31 | CH6 · 6-bis.4 guardie pubbliche D-44/P34 | ancorata in §6-bis.4 |
| 32 | CH6 · 6-bis.5 R26 sizing vs ranking | ancorata (findings:2148 senza data per-riga = limite dichiarato, non violazione) |
| 33 | CH8 · 6.3 pin utente 2026-08-02 [fix ST-C5-16: (b)→(c)] | forma CH1 T-1: doppia prova :371-377 + state-pointer |
| 34 | CH8 · 6.6 assenza search-proven (H20/C61) | doppia ancora fork b0a4c15 (90/50/1/0) + a85e355 (ST-C5-18) |
| 35 | CH8 · 6.2 metà-(c) finitezza settori | census-lemma DOVUTA (dichiarato; l'altra metà è (a) esistenza-Chenais) |
| 36 | CH9 · 6.2 T-LEMB / O3.1 | doppia prova in §6.2 (refuter C5: CH9 0 BREAK/0 REPAIR) |
| 37 | CH9 · 6.3 dual-seed (canary + known-true) | idem |
| 38 | CH9 · 6.4 il NO di record (NON-CERTIFICABILE) | idem + ancora Scert:184 (ST-C5-19) |
| 39 | CH9 · 6.5 O3.4 cross-code (accordo ≠ verità) | idem |
| 40 | CH10 · 6.3 G6 mai esercitato | quote esatta hypaudit + :459 (ST-C5-20) + D6:1150-1152 (ST-C5-21) |
| 41 | CH10 · 6.4 U3' premise-open | ancorata in §6.4 |

**Conteggio (SR-12, enumerazione delle due tabelle qui sopra): 41 righe
inventario** (23 B8a + 18 B8b), di cui **3 FINDING "doppia prova
ASSENTE" residui** (F-1, F-2, F-3 — righe 3, 6, 10) e **1 FINDING
riformulato-consumato** (F-4, riga 23). NOTA DI DELTA dichiarata: il
brief D2 (SESSION2_LOG) citava "4 ASSENTE" — il numero corrente è 3+1,
per effetto della riformulazione ST-C5-13 (REFUTE_STORIE, posteriore al
brief). Gli split (a)/(b)/(c) per capitolo NON sono riprodotti qui:
vanno rigenerati da comando (regola §FP.4(iii)).

==============================================================================
## §(c) ANNEX CODA-D'ATTACCO (ordine utente: l'unione, con owner + finestra)

L'agenda unificata di ciò che il record dichiara NON chiuso. Le card
vivono NEI capitoli (mai duplicate qui — regola §1g/SR-7): la tabella dà
id → capitolo§ + finestra.

### (c.1) Le 12 NEVER + 2 SINGLE-AUTHOR del choice ledger (card stampate)

Roster di record: "NEVER: 12 (C25 C38 C51 C52 C53 C54 C55 C57 C59 C60
C61 C62)" + 2 SA (C17, C18) — `docs/rde_nozzle_pipeline_decision_map.md:293`
(citato in CH6 :407-409 e CH4 §1.2).

| id | classe | card (capitolo§) | finestra / trigger di ri-esame | owner |
|---|---|---|---|---|
| C17 trip cap N_NEWTON=30 | SA | CH4 §7-bis card 1 (:1106) | **F2** | delta VERDICT_wave3 par.3 |
| C18 costanti floor (NTF, C_FLOOR) | SA | CH4 §7-bis card 2 (:1114) | **derivazione F2-live** (con Tier-1 C20) | riga ledger :344-353 |
| C25 box tabella thermo | NEVER | CH4 §7-bis card 3 (:1122) | **F2** (con C-C/C-D) | riga ledger |
| C38 stazionarietà outcome-II | NEVER | CH4 §7-bis card 4 (:1130) | **F2** | riga ledger |
| C51 solver wave-frame rung-3a | NEVER | CH7 card (:816-827) | **rung-3a implementation window**; PRIORITÀ = decisione utente PENDENTE (DISPATCH_swirl5f:100-101) — candidata slide ASK | owner di riga + utente |
| C52 signature MIXED/phase-crossing | NEVER | CH10 §5.1 (:471) | **F2 contract window** (feeds `contract:chi-character-map-unknown-band-missing`) | judge agenda |
| C53 Γ_d placement policy | NEVER | CH10 §5.1 (:492) | **F2 contract window** (carrier: placement-band remark M0 D2.4; harvest 87.8% damping disponibile) | judge agenda |
| C54 status rung I4 nella scala D2.4 | NEVER | CH10 §5.1 (:513) | **prossimo touch di M0 D2.4** (l'annotazione one-line flippa la riga a DECIDED) | owner riga |
| C55 aggregazione P_amb | NEVER (strutturalmente vuota) | CH4 §7-bis card 5 (:1137) | **prima istanziazione multi-punto di P_amb** | riga ledger |
| C57 tier esplorazione globale | NEVER | CH4 §7-bis card 6 (:1145) + CH8 §7(d) (:848) | **F2-entry adjudication window** (cluster C31-ledger A/B, C49 explorer, C58, C60, [P-IPADJ]) | cluster A pipeline map :199-204 |
| C59 forma temporale del funzionale | NEVER (canonica-in-pin) | CH6 §8 (:965) E CH4 §7-bis card 7 (:1155) — v. NOTA DEDUP sotto | **trigger = regime weakened-pin in scope** (F2-entry census window, ledger :804) | riga ledger |
| C60 NAND vs SAND (LNKS) | NEVER | CH4 §7-bis card 8 (:1165) | **F2-entry** (cluster con C57/C58/[P-IPADJ]) | riga ledger |
| C61 chiusura base-pressure p_b | NEVER | CH6 §8 PRIMARIA (:938); CH8 :868 = puntatore (dedup WB1-C3-17 RISOLTO) | **"first truncated-plug (value,delta) row … or F4b window entry — whichever fires first"** (ledger :829) | riga ledger; collocazione F4b: CH6 §1.5 |
| C62 quadratura di fase su Ξ | NEVER | CH4 §7-bis card 9 (:1174) | **F2 cluster numerica; trigger = primo accuracy budget della campagna** | riga ledger |

**NOTA DEDUP C59 (segnalazione di consolidamento, owner: orchestratore
W-D / retro-audit)**: a differenza di C61 (dedup RISOLTO: primaria CH6,
CH8 ridotto a puntatore), C59 ha DUE card complete — CH6 §8 (:965) e
CH4 §7-bis card 7 (:1155) — senza primaria dichiarata. La regola "mai
due card gemelle" (SR-7, applicata a C61 in CH6 :928-936) non risulta
applicata a C59. Nessuna contraddizione di contenuto rilevata tra le due
(stesso verdetto, stesso trigger weakened-pin); resta un difetto di
unicità da disporre (riduzione di una delle due a puntatore).

### (c.2) FINDING "doppia prova ASSENTE" residui (dagli inventari, §(b))

| id | contenuto | scarico nominato (owner/finestra) |
|---|---|---|
| F-1 | sharpness di THEOREM 6 enunciata senza prova scritta; carrier PB-2 mai eseguito | write-up da mintare (W2-R4) + campagna PB-2 — nessuna data di record |
| F-2 | [S-BLITE] SCHEMA con brick G12-L1-3D nominato, mai eseguito | esecuzione brick — **finestra F2** |
| F-3 | twin warning: falsificatore di rilevanza a due segni mai eseguito sul parco | esecuzione a cap unilaterale attivo (regime-qualified) |
| (F-4) | consumato: riformulato NON-ASSENTE (doppia prova = REFUTE_CH7 #5) — resta qui solo come traccia del delta vs brief | ST-C5-13, CONSUMATO da W-C.b |

### (c.3) Clausola O3.4 leg-gradiente MATURATA senza consumo

REFUTE_CH9 §(d) FP-1 (fuori-perimetro del refuter, MAI disposta): la
clausola D6:826-830 "the gradient leg of O3.4 lands with the A1 engine"
è maturata — il motore A1 è atterrato (S18, X-TOCV) — ma NESSUN run
O3.4-gradiente (JAX grad vs GENO FD) risulta a registro (grep "O3.4" in
finestra del refuter: 10 hit, nessun pass della leg). Stato nei
capitoli: CH9 §3/§5 già riscritti a DUE leg (flowfield CHIUSA S10 con
scope X-GENOXC; gradiente = residuo dichiarato). **Azione in coda:
candidata riga findings (classe gate-scope/instrumentation-gap) alla
prima finestra utile; owner naturale = F2, primo blocco oracoli.**

### (c.4) Procurement aperti (documentali, MAI in-onda — protocollo G-11)

| oggetto | stato | ancora |
|---|---|---|
| Talley & Coy 2002 (ordering/matching, componente 8) | candidato emerso da W-B.0 | LINEAGE_LEDGER coda :215 (LL-10); attribuzione primaria via WS-2004, findings :1956-1967 |
| Sternin 1957/1959 (possibile antenato PRE-KO, confidenza LOW) | candidato, procurement-gated | LL-11; CH1 §3-bis :427-428 |
| Tillyaeva 1975 (`wanted_tillyaeva_1975`, russo [HARD]) | **PENDING-PROCUREMENT con owner** (cella E-ii [V2-R6]: confronto diretto vietato finché assente — carrier surrogati di record) | CH7 §7(a) :732; design v2 §M E-ii |
| Fievisohn AIAA 2018-0881 (`wanted_fievisohn_2018_quasi2d_moc`) | **RAISED** (già a registro; l'ugello Fievisohn resta [REP]-bounded finché assente) | CH10 §3-bis :323; LINEAGE_LEDGER SEED-1..3 |

### (c.5) Condizionale-(J) re-ancorato a C-MAJDA (nessun mint necessario — di record)

Il tallone (J) del nodo N-Q (front jumps, primo ordine NON soppresso di
gap(B); SBV-conditional, delta underived — emendamento §1d/C-3ter) era
citato in CH10 §6.5 con l'etichetta "C-SBVF", INESISTENTE nei registri:
fix B2-res2 (HISTORIAN_INV_b §5; CH10 :656) lo ri-ancora a **[C-MAJDA]**
(condizionale analitico di record, affilato a U3-H1, stated-once nel
ledger L4 — commit c4d5a95, verificato da C5: REFUTE_STORIE :138, :685).
NESSUN mint di registro è necessario: il condizionale esiste già; l'unica
azione era la ri-ancora, ESEGUITA. Resta in coda-d'attacco SOLO come
promemoria di join per il retro-audit: ogni occorrenza deck del tallone
(J) cita [C-MAJDA], mai sigle non-di-registro.

### Conteggio coda-d'attacco (SR-12, enumerazione §(c) qui sopra)

**24 voci**: 14 card SA/NEVER (c.1) + 1 nota dedup C59 + 3 FINDING
residui + 1 traccia F-4 consumata (c.2) + 1 clausola O3.4 (c.3) +
4 procurement (c.4) + 1 promemoria (J)/C-MAJDA (c.5). Di queste, le
AZIONI vive (non-tracce) sono 22.

==============================================================================
## §(d) MAPPA id → CAPITOLO (generata per grep; lint 1 la cross-verifica)

**Dichiarazione di metodo (SR-12)**: `LINT_REPORT_WD.md` NON esiste nelle
raws al momento della compilazione (verificato: `ls` in finestra, D1 in
parallelo non ancora atterrato) → la tabella è generata QUI dal comando
`grep -l <token> CH*.md` eseguito in finestra (2026-08-23) su un roster
di token load-bearing; il lint 1 di D1 (lint-registri, comando proprio)
la CROSS-VERIFICA e, in caso di divergenza, VINCE il lint (regola
navigation-first). La mappa è per-capitolo, non per-riga: le righe
esatte vivono nei capitoli.

| id/token | capitoli che lo portano |
|---|---|
| [T-T0P] | CH1, CH3, CH6, CH7 |
| [S-T0P] | CH1 |
| [T-T4] | CH1, CH6, CH8 |
| [T-T7RED] | CH1, CH2 |
| [T-T7FS] | CH1, CH2 |
| [T-T7CN] | CH1, CH2 |
| [T-T3-MAP] | CH1, CH3, CH8 |
| [T-P3] | CH2 |
| [T-NSW] | CH1, CH2, CH10 |
| [T-DISC] | CH3, CH4, CH6, CH7, CH10 |
| [T-RED] | CH3, CH7 |
| M-RED | CH2, CH3, CH4, CH5, CH6, CH7, CH10 |
| [R22F-FORCHETTA] | CH3 (+ consumo CH6/CH7) |
| [S-GBE] | CH1 |
| [S-BLITE] | CH1, CH3 |
| [S-LBML] | CH9 |
| [T-LEMB] | CH9 |
| [C-MAJDA] | CH2, CH9, CH10 |
| [C-D25U] | CH2, CH9, CH10 |
| [C-O33] | CH2, CH9, CH10 |
| [C-HT4] | CH1, CH6, CH8, CH10 |
| [T-N6-2] | CH7 |
| [T-EQBR] | CH3 |
| [T-OP11e] | CH8 |
| [X-GENOXC] | CH4, CH9 |
| X-TOCV | CH8, CH9 |
| [X-O31CS] | CH9 |
| [D-MU] | CH1 |
| [D-CONTRACT] | CH1, CH10 |
| [L4-CERT] | CH1, CH10 |
| PB-2 | CH1, CH5, CH6, CH8 |
| CT-6 (threat ledger) | CH1, CH5, CH6, CH7, CH8, CH10 |
| D-44 / P34 (guardie pubbliche) | CH4, CH6 / CH4, CH6, CH8, CH9, CH10 |
| H20 | CH4, CH8 |
| C61 | CH4, CH5, CH6, CH8 (card primaria: CH6 §8) |
| EAP (remark) | CH1, CH3, CH5, CH6, CH7, CH10 |
| **[T-DCRX]** | **0 hit nei capitoli** — vive in M0 (memoria s-foundations-c4-closed). Riga FUORI-CAPITOLO dichiarata per il lint 1: se un capitolo lo consuma in futuro, la mappa si rigenera |

Mappa id→NODO: composizione di questa tabella con §CH del design v2
(capitolo → nodi serviti) e con ATLAS_TREE (nodo → 9 sezioni); LL-id →
capitolo§3-bis: elenco per-nodo in ATLAS_TREE, righe integrali nel
LINEAGE_LEDGER (join su LL-id, contratto F-des-4).

Fine di CH_REF.md — annex di servizio: nessun claim proprio; ogni riga
è consolidamento ancorato. Consumatori: retro-audit (disambiguazione
C31/C4, promemoria (J)); D1/lint 1 e lint 8 (cross-check §(d), card
c.1); F2-entry (agenda c.1-c.3); procurement (c.4); promozione
docs/atlas/.
