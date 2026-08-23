# REFUTE_STORIE — refutazione avversaria delle §6 STORIA (CH1-CH10) + inventari HISTORIAN

Slot C5 (refuter, giudizio), onda W-C.b, S-PRES sessione 2, 2026-08-23.
**Oggetto**: SOLO le sezioni §6 STORIA dei 10 capitoli (B8a: CH1-4, CH7;
B8b: CH5-6, CH8-10) + `HISTORIAN_INV_a.md`/`HISTORIAN_INV_b.md`; i §7(c)
per il punto 4 del mandato. Nessun edit ai capitoli (file occupati da
altri slot): SOLO questo file.
**Metodo**: cammino battuta-per-battuta ancora-per-ancora; TUTTI i 12
hash della lista C3 (`REFUTE_WB1_extensions.md:1080-1082`) verificati con
`git log`/`git show` in finestra; commit aggiuntivi citati dalle battute
1 verificati anch'essi (totale 30 hash, lista in §H); rami (a) aperti
alla riga citata di `phaseB_tree_diff.md`/file phaseD; rami (b) aperti al
verdetto per-riga; guardia 15 (`GUARD_CHECKLIST.md:28`) contata per
battuta; §7(c) contro design v2 §C (`ATLAS_RESEARCH_DESIGN_v2.md:266-289`);
15 id registry campionati con grep. Classi: BREAK / REPAIR / GAP / NOTE
con severità. Numerazione: ST-C5-nn.

Definizioni di riferimento usate come metro (aperte in finestra):
- Trittico e rami (a)/(b)/(c): design v2 §T-§6 (:185-245). (a) = perimetro
  riderivato Fase A/B §3 **o** portato a convergenza in Fase D (file
  phaseD con verdetto); (b) = scelta del LEDGER con verdetto per-riga
  Fase B (phaseB_tree_diff §1, C1-C48), dichiarata stance di fork;
  (c) = riga esplicita NON-RIDERIVATO + doppia prova alternativa ancorata
  o "doppia prova: ASSENTE" = FINDING.
- Guardia 15: OGNI battuta §6 porta DATA + PROCESSO + VERDETTO.
- 12 righe SILENT (phaseB_tree_diff.md:397-399, verificate alla riga):
  C2 cond., C5, C15, C16, C22, C23, C30, C40, C45, C46, C47, C48.

==============================================================================
## §H — VERIFICA COMMIT (mandato punto 1; eseguita in finestra)

**I 12 hash della lista C3: 12/12 ESISTONO e reggono** (git log -1, date
verificate):

| hash | data git | battuta/e che lo cita/no | esito |
|---|---|---|---|
| b0a4c15 | 2026-08-20 | CH5 6.2 b1, 6.4 b3 | REGGE — "USER CHALLENGE ... SUSTAINED 3/4 measured", "P-B/C/D never surfaced", riga findings coniata: tutto verbatim nel messaggio |
| a85e355 | 2026-08-20 | CH5 6.2 b1/b2; CH8 6.6 b1 | REGGE — "0 BREAK across 8 consolidated threats", "nothing crushes the project", "reviser 9/9 + confirm 9/9 FAITHFUL", "2 genuine gaps (H20 F4b; P34 P-1 window)" tutti verbatim; MA "90/50/1/0" NON è in questo messaggio (vive in b0a4c15) → ST-C5-18 |
| ea2abce | 2026-08-13 | CH5 6.3 b2, 6.4 b1; CH6 6-bis.3 b2 | REGGE — "D-01 gloss deleted at literature_map+theorem_ledger", "claim 1 (P2/G14) rewritten", "in-school KT2015 chain CONCEDED", "PB-2 LOCKED formulation + 7-item caveat list" tutti verbatim |
| b3da86d | 2026-08-20 | CH5 6.5 b1/b2 | REGGE — "16 sources, pages declared", Purdue CTAP, "Veen closure 0.846p/M^1.3 traced to 1966 cold curve fit FAILED by WG10 -> N2 must replace", "x2.45 at +0.26%", "ADR-D4 rider EXTENDED ... items 4-6" tutti verbatim |
| 3b2b9e6 | 2026-08-21 | CH5 6.5 b1; CH10 6.4 b2 | REGGE — "NEVER spectrally verified in ANY published CFD (zero field FFT/PSD, search-proven)", "KP18 Table 1 = only quantified throat statistics", "9 search-proven gaps G1-G9" verbatim |
| 904f950 | 2026-08-20 | CH5 6.6 b1; CH6 6-bis.1 b1/b3 | REGGE — "best-of-sweep != argmax wording guard (user catch sustained)", "Gap-A/Gap-B value frame", "no argmax-shift number at any grade, derivers ordered five-field->route-B->M-RED" verbatim |
| 1a11f2c | 2026-08-20 | CH6 6-bis.1 b2 | REGGE — "22 amendments carried / 0 contested sustained" verbatim |
| fd2d444 | 2026-08-21 | CH6 6-bis.3 b3, 6-bis.4 b1; CH8 6.6 b1; CH9 6.3 b2 | REGGE — "mints C61 p_b-closure", "SEED-OMIT P34 caught", "SEED-DECOY C50 not flagged", "dual-seed PROVEN both directions" verbatim |
| da91aa4 | 2026-08-21 | CH6 6-bis.4 b1; CH8 6.1 b3 (implicito) | REGGE — pipeline map 62+17=79 nodi, "REFUTER PASS: 0 BREAK / 0 REPAIR", "5 precision amendments" verbatim; HISTORIAN_INDEX §3 corretto (INV_b §3.4) |
| d968502 | 2026-08-23 | CH6 6-bis.4 b2 | REGGE — "S-PRES session 1: Block 0 CLOSED" |
| 318d3fd | 2026-08-20 | CH6 6-bis.5 b2 | REGGE — "(c) no-external-referee structural fact MANDATED in forchetta" verbatim |
| cc878ef | 2026-07-20 | CH4 T-1 b1, T-4 b1 | REGGE — "G0 DECIDED — GENO built (WSL gfortran), tocnoz contour reproduced to 1e-10, cross-code unit-process oracle X-GENOXC PASS; JAX primary stack" verbatim |

**Commit aggiuntivi citati dalle battute 1 e verificati in finestra
(18/18 esistono, date conformi)**: ac78ec0, f28cb03, 7255e00, e800a19,
ef0af1d, 592107d, 0b26dc7, 95d54de (CH1); 86fac06, c0e3051, c4d5a95,
f54dbf2, 514d037, 35e95f2, cbee622, 344ddfb, 079f882, 581ccb1 (CH2);
7be8b98, b54e571, 01c41a6, 07400a4, 32459ca, 7dea386, c9bacd9 (CH2/CH4);
5221529, f3c5df5, 1d9609a (CH8/CH9/CH10). Un solo mismatch di DATA
trovato su tutto il corpus: **32459ca** (v. ST-C5-07).

==============================================================================
## CH1 — Formulation ladder (§6, writer B8a: 7 argomenti T-1..T-7)

### Cammino eseguito
- Battute 1: 8 commit verificati (sopra), tutti con data+soggetto
  conformi alla battuta ("S6-addendum" ✓, "rigore"-tags ✓, "top flag
  Kraiko-Osipov 1970" verbatim ✓). M0:995 (enunciato pin H3 + monitor T0)
  ✓ alla riga; M0:560-561 (pin = MODEL HYPOTHESIS senza provenienza
  hardware R20) ✓; M0:108-114 (scope note ME-2/PB-5) ✓.
- Battuta 2 rami (a): T-2 via phaseB:315 (item 1 "Steadification
  exactness (T-T0 road)", H-F1(b)) + :325 (item 2 "Rao-collapse under
  averaging", H-F35) — APERTI ALLA RIGA: i numeri di riga sono ESATTI e
  il perimetro copre l'argomento ([D-MU]/rung 2: item 1 ri-deriva la
  steadificazione E la decomposizione del residuo O(St) via H-F2, item 2
  la struttura per-fase+parete-media). T-3 via :315 + Fase D proof loop 1
  (`phaseD/VERDICT_phaseD_proofs1.md` esiste; `r2pass/VERDICT_doc1_rev10.md`
  esiste) ✓. T-4 via contract blind (file esistono; giudice
  `VERDICT_contract_and_L4R1.md` esiste) + :330 (item 3, "4/4 trees ...
  capturing never a certificate" verbatim) ✓. T-5 gamba T-T7RED via :325
  ✓. **NESSUN (a) INDEBITO in CH1.**
- Battuta 2 rami (c): T-1 doppia prova ([S-T0P] pricing + monitor armato
  + PB-5) ancorata ✓; T-5 gambe T-T4 (claims:339 falsificatore O2 ✓ per
  join con INV_a :329-340) e sharpness ASSENTE = F-1 dichiarato ✓
  coerente con M0:2316-2319 (verificato da C3 alla riga) e problem_book
  :532-536; T-6 doppia prova S24 T2a — M0:4138-4140 APERTO: "S18
  FIVE-LINE HYPOTHESIS AUDIT [T-T3-MAP S18-clause NAMED PRECONDITION —
  PERFORMED, S24 T2a]" VERBATIM ✓; `PROGRESS_2026-08-12_S24_f1b.md`
  esiste ✓; T-7 [S-GBE] carrier + [S-BLITE] ASSENTE = F-2 dichiarato ✓
  (M0:3027-3044 verificato da C3).
- findings:1450-1458 (T-3 b3): APERTO — la riga
  `theory:s-t0p-proof-writeup-pending` vive lì (id a :1451), trigger
  "F2 entry, or the first external presentation of the two-stage
  per-phase claim" = "trigger armato da S-PRES stessa" ✓ FEDELE. La
  battuta NON cita :1455 secco (v. §FP).

### Finding

| # | Classe | CH1 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-01 | NOTE (BASSA) | T-7 battuta 2 (e battuta 3) | "carrier eseguibile X-GBE PASS (claims_registry.yaml:1843-1854)": il blocco :1843-1854 è S-GBE (SCHEMA, E1-E5); il PASS del carrier vive a :1856-1860. Stessa ancora corta già trovata da C3 nelle sezioni nuove (WB1-C3-02): la §6 la EREDITA. Estendere a :1843-1864 nei due punti. |
| ST-C5-02 | GAP (MEDIA) | T-4/T-5/T-6/T-7 battuta 3 — guardia 15 | Le battute 3 di T-4 ("R1 CONDIZIONATA ... classe finale come §2"), T-5 ("classi finali come §2; ... nessuna data di record"), T-6 ("classe finale SCHEMA container ..."), T-7 ("classi finali: ...") portano VERDETTO e ancora ma NON portano DATA né PROCESSO propri della convergenza (T-1/T-2/T-3 b3 li portano). Il retro-audit joina su data+processo+verdetto: 4 battute su 21 mancano di 2 campi su 3. Riparazione: una data di convergenza per battuta (T-4: 2026-08-06 S16 per la finestra R1; T-5: 2026-08-04 PAN-S14 per le classi + PB-2 "nessuna data" già dichiarata; T-6: 2026-08-12 S24 T2a; T-7: 2026-08-06 S16 per S-GBE) + il processo in una riga. |

### Disposizione (proposta C5; esecuzione = storici B8a, file occupato)

| Finding | Disposizione proposta |
|---|---|
| ST-C5-01 | Estendere l'ancora a claims:1843-1864 (T-7 b2 e b3) |
| ST-C5-02 | Aggiungere DATA+PROCESSO alle 4 battute 3 nominate |

### Q&A SEED (dalla storia CH1)
1. **D**: "Il vostro pin dati è un'ipotesi comoda: chi l'ha mai messa
   alla prova?" → **R**: è un PIN utente dichiarato MODEL HYPOTHESIS
   (mai promosso), prezzato dai refuter di Fase D sul blocco [S-T0P],
   con monitor T0-flatness obbligatorio nel contratto e routing PB-5
   fuori-pin. → **Ancora**: M0:560-561; M0 VI.4bis(v); CH1 §6 T-1. →
   **Backup**: slide pin+monitor+rejector.
2. **D**: "La vostra 'sharpness' max∫<∫max è dimostrata?" → **R**: no,
   e lo dichiariamo noi per primi: clausola enunciata senza prova
   scritta, carrier PB-2 mai eseguito — FINDING F-1 a registro, non una
   slide ammorbidita. → **Ancora**: M0:2316-2319; problem_book:532-536;
   HISTORIAN_INV_a F-1. → **Backup**: riga F-1 + roadmap PB-2.
3. **D**: "Le riderivazioni cieche sono davvero cieche?" → **R**: brief
   self-contained con divieto di documenti di progetto; 4 alberi, 141
   fork; il diff è per-riga con 12 righe SILENT dichiarate NOT-support —
   il negativo è stampato accanto al positivo. → **Ancora**:
   phaseB_tree_diff.md:1-12, :397-399. → **Backup**: tabella split
   (a)/(b)/(c) per capitolo (INV_a/INV_b).

### Guardie CH1 §6: 15 = **4 HIT** (ST-C5-02) / resto CLEAN
Guardia 10 CLEAN (lineage solo via ledger nelle battute); 9 CLEAN (novità
solo nelle forme bloccate); 13 CLEAN (nessun numero altrui nudo); 14 n/a
(nessuna card in §6); 5 n/a qui (v. §AXES).

### VERDETTO CH1 §6: **REGGE-CON-NOTE** (0 BREAK, 0 REPAIR, 1 GAP guardia-15, 1 NOTE; nessun (a) indebito; F-1/F-2 dichiarati correttamente)

==============================================================================
## CH2 — Averaged optimality (§6, writer B8a: 7 argomenti T-1..T-7)

### Cammino eseguito
- Battute 1: 10 commit verificati, tutti conformi (86fac06 "(rigore-S8)"
  ✓; c4d5a95 "conditionals ledger (L4) — C-D25U and C-MAJDA stated once,
  inherited by ID" ✓ = esattamente la battuta T-1 b3; 344ddfb "204/204
  issues ... top flag Kraiko-Osipov 1970" ✓; 581ccb1 "[LEADS/S13]
  Kraiko-Osipov contingency ADJUDICATED (containment)" ✓ = T-7 b1).
- Rami (a): T-1 via :325 (H-F35 = "our T7/(**') system re-derived blind"
  verbatim alla riga) ✓ COPRE l'argomento. T-6 via :325 + :345 (item 6
  "Thermo road: V-F9/H-F6 = certified gamma(T) tables with AD" ✓ alla
  riga) ✓. T-5 boxed warning "(a) parziale": il contenuto matematico
  ("nessuna fase soddisfa la propria wall condition, la media sì") È
  dentro H-F35 (ONE averaged wall condition) — sostenibile con
  l'auto-qualifica "parziale"; NON indebito.
- Rami (c): T-2 [T-P3] — la dichiarazione "non è tra i 7 item
  theory-layer di :315-347" VERIFICATA (aperti tutti e 7: nessuno copre
  l'identificazione f2=−λ2); ramo (c) CORRETTO e conservativo, doppia
  prova (PAN-S14 + O3.3 S19 quantificata) ancorata ✓. T-3/T-4 (c)
  corretti (la forma a cono 2026-08-13 precede gli alberi ma non compare
  negli item — dichiarato con F-des-3 ✓). T-5 twin warning ASSENTE = F-3
  dichiarato ✓. T-7 (c) storia esterna ✓ con doppia prova litreview
  contraddittorio ✓.
- `s25bis_closing_suite.log` esiste ✓ (T-5/T-6 rejector re-misurati).

### Finding

| # | Classe | CH2 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-03 | GAP (MEDIA) | T-2/T-3/T-5/T-7 battuta 3 — guardia 15 | Battute 3 senza DATA né PROCESSO propri: T-2 ("classe finale THEOREM* con residui ... M0:2930-2934"), T-3 ("classe finale THEOREM* dentro T-T7FS(a)"), T-5 ("classi finali §2; la classe eps* stantia..."), T-7 ("gate umano G5 resta ... classe finale"). T-4 b3 borderline ("stesso blocco" eredita la data 2026-08-13 per inferenza — esplicitarla). Riparazione: data+processo di convergenza per battuta (T-2: 2026-08-13 F-SERVICE per i residui R-P3 nominati; T-3: 2026-08-07 S21; T-5: 2026-08-13 suite; T-7: già in b2). |
| ST-C5-04 | NOTE (BASSA) | T-5 battuta 2, gamba boxed warning | "(a) parziale via T7-road H-F35 (:325)": l'ancora di Fase B più FORTE per "fuori T3 la media naive è sbagliata" è l'item 5 (:339-344, "delta = 0 iff one shape is per-phase optimal mu-a.e. = the T3/T4 dichotomy criterion re-derived") — non citato. Aggiungerlo rafforza la gamba senza cambiarne l'esito (già consumato da CH8 6.4 b2, coerenza d'atlas). |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-03 | Data+processo alle 4 battute 3; esplicitare la data in T-4 b3 |
| ST-C5-04 | Co-citare phaseB:339-344 nella gamba boxed-warning |

### Q&A SEED (dalla storia CH2)
1. **D**: "La forma a cono è arrivata DOPO: avete aggiustato la teoria a
   posteriori?" → **R**: la riforma a cono è una ratifica UTENTE datata
   (2026-08-13, F-SERVICE) con lemma [T-T7CN] + controesempio e rejector
   S3/A39 armato; la storia dichiara che PRECEDE gli alberi ciechi e che
   NON è coperta dal loro perimetro — nessuna ancora fabbricata
   (F-des-3). → **Ancora**: CH2 §6 T-4; M0:2830-2874. → **Backup**:
   card trittico T-4.
2. **D**: "Il twin warning è mai stato testato sul vostro parco?" →
   **R**: no — la prova esistenziale c'è (M0:2895-2907), il falsificatore
   di rilevanza a due segni NON è mai stato eseguito: FINDING F-3 a
   registro con scarico nominato. → **Ancora**: HISTORIAN_INV_a F-3. →
   **Backup**: piano di esecuzione regime-qualified.
3. **D**: "f2=−λ2: chi ve l'ha verificato oltre a voi?" → **R**:
   riderivazione cieca NON disponibile (dichiarato: fuori dai 7 item);
   doppia prova = panel 16/16 + bench O3.3 PASS criterio primario con
   residuo [C-O33] QUANTIFICATO e stampato. → **Ancora**: CH2 §6 T-2;
   P1:200-203. → **Backup**: slide O3.3 con barre.

### Guardie CH2 §6: 15 = **4 HIT + 1 borderline** (ST-C5-03) / resto CLEAN

### VERDETTO CH2 §6: **REGGE-CON-NOTE** (0 BREAK, 0 REPAIR, 1 GAP guardia-15, 1 NOTE; nessun (a) indebito; F-3 dichiarato correttamente)

==============================================================================
## CH3 — Reduction physics (§6, writer B8a: 6 argomenti T-1..T-6)

### Cammino eseguito
- T-1: findings:1459-1468 APERTO ALLA RIGA — id
  `theory:r22-formal-decomposition`, mechanism
  `epistemology-bias-from-literature`, evidence "EXECUTED to cap-4
  (2026-08-20 ... VERDICT_r22f NOT-DRY-AT-CAP approved-for-landing)":
  battute 1-2 FEDELI al registro ✓.
- T-2 (a): `VERDICT_r22f.md:508-521` APERTO — "NOT-DRY-AT-CAP; ...
  APPROVED FOR LANDING", "findings_total: 66 (4 BREAKs, 23 REPAIRs...)",
  "rounds: 4" VERBATIM = la battuta è esatta al numero.
  `VERDICT_escalation_c4.md:542-553` APERTO — "E-1 DRY(r2), E-2 DRY(r3),
  E-3 DRY(r3), E-4 DRY(r3) ... E-5 ... 0 BREAK unanimous",
  "findings_adjudicated: 53/53 SUSTAINED" VERBATIM ✓. Probe citati
  esistono su disco (phaseD/esc_probe_r4delta_*.py ✓). **(a) LEGITTIMO
  ed esemplare.**
- T-3 (a): VERDICT_r22f Part-2 rows APERTE (T-RED-1 DEFINITION +
  identities THEOREM* "machine-witnessed (judgeverify ITEM 3.1) +
  re-derived by hand by L1 twice; census ... G-f SCHEMA — NOT inflated")
  ✓ = esattamente la battuta. `DISPATCH_swirl5f.md:64` APERTO (riga 9:
  "K̄ = 0 fiberwise UNCONDITIONAL ... verifier CONFIRMED") ✓. K̄=0 MINT:
  M0:1768-1773 APERTO ("MINTED AT RECORD GRADE at this landing ...
  THEOREM*: pen proof + machine witness; holds on full BV") VERBATIM ✓.
- T-4 (a): VERDICT_r22f:106-122 APERTO (Part 5 forchetta,
  good-fitted-sheet "restored at all three sites [REV2-r1-7],
  [REV2-r3-7]") ✓; M0:1493-1494 ("The bracket TIGHTENS in the program
  order...") VERBATIM ✓.
- T-5 (c): honesty-form corretta (aperto strutturato, NON finding) —
  coerente col metro `never-postpone-resolvables` (structurally-gated con
  owner+deriver nominati) ✓; escalation anchors verificate ✓.
- T-6 (c): VERDICT_r22f:90-97 APERTO (Part 3 M-RED "PRACTICE (carrier
  spec) ... execution = F2 duty named"; bande B-1..B-4 "zero magic
  constants ... L2 probes") VERBATIM ✓; structurally-gated dichiarato ✓.

### Finding

| # | Classe | CH3 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-05 | NOTE (BASSA) | T-3 battuta 2 | Ancora "VERDICT_r22f.md:77": la riga 77 è il separatore di tabella; le righe di contenuto ([T-RED-1]/[T-RED-2]) sono :78-81. Off-by-one: ri-puntare a :78-81 (lo stesso ±1 tocca CH7 T-6 b2 che eredita ":77"). |
| ST-C5-06 | GAP (BASSA) | T-1/T-6 battuta 3 — guardia 15 | T-1 b3 ("classe finale: standing directive + landing M0 C4") e T-6 b3 (classe+quote M0:1493-1494) senza DATA (la data 2026-08-21 del landing è ricostruibile ma non stampata) né PROCESSO. 2 battute su 18. |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-05 | Ri-puntare a VERDICT_r22f.md:78-81 (anche in CH7 T-6 b2) |
| ST-C5-06 | Stampare 2026-08-21 + processo (landing C4 gate NOTHING-LOST) nelle 2 battute 3 |

### Q&A SEED (dalla storia CH3)
1. **D**: "Il vostro centerpiece non è arrivato DRY: perché fidarsi?" →
   **R**: NOT-DRY-AT-CAP è STAMPATO nel verdetto con recount (2 BREAK +
   1 REPAIR al round 4), l'escalation dedicata E-1..E-5 ha chiuso DRY con
   53/53 sustained e 0 BREAK unanime — il residuo era nominato
   (RES-CAP-1) ed è stato scaricato, non nascosto. → **Ancora**:
   VERDICT_r22f.md:508-521; VERDICT_escalation_c4.md:542-553. →
   **Backup**: slide catena refutazione→escalation→landing.
2. **D**: "K̄=0 l'avete provato una volta sola?" → **R**: tre provenienze
   indipendenti datate: panel swirl5f con verifier sympy (2026-08-19),
   refutazione centerpiece con probe (2026-08-20), mint a grado record
   con prova a penna + testimone macchina su BV pieno (2026-08-21). →
   **Ancora**: DISPATCH_swirl5f.md:64; M0:1768-1773. → **Backup**:
   trittico CH3 T-3 / CH7 T-5.

### Guardie CH3 §6: 15 = **2 HIT deboli** (ST-C5-06) / resto CLEAN

### VERDETTO CH3 §6: **REGGE** (0 BREAK, 0 REPAIR, 1 GAP bassa, 1 NOTE; i tre (a) di Fase D sono i meglio ancorati dell'atlas)

==============================================================================
## CH4 — Machine choices (§6, writer B8a: 8 argomenti T-1..T-8 + testata SILENT)

### Cammino eseguito
- Testata: le 12 righe SILENT dichiarate ramo (c) per definizione — LISTA
  IDENTICA a phaseB_tree_diff.md:397-399 aperto alla riga (somma
  8+10+11+6+12+1=48 ✓). CONFORME al mandato punto 3 (v. §SILENT).
- T-1 (c): "C58 > C48: fuori dal perimetro per-riga" VERIFICATO (il diff
  §1 è C1-C48); doppia prova (flip clause T1/T2a misurata + review S25)
  già verificata da C3 su G0:199-210 ✓; coerenza: stessa logica NON
  applicata a T-4 → ST-C5-08.
- T-2 (b): phaseB:159 APERTO — "**C31 optimizer engine (MIXED)** —
  CONVERGENT on family + DIVERGENT on the IP half" VERBATIM ALLA RIGA ✓;
  la battuta dichiara correttamente "presa di posizione a livello fork,
  NON riderivazione dell'implementazione" ✓ ((b) LEGITTIMO).
  `PROGRESS_2026-08-06_S18_brick2run.md` esiste ✓; 01c41a6 ✓;
  M0:4138-4140 ✓.
- T-3 (b): phaseB:117-118 APERTO — "**C24 thermo closure (DECIDED
  KEEP)** — CONVERGENT + ENRICHING: V-F9 lands" VERBATIM ✓; :345 item 6
  co-citato ✓ ((b) LEGITTIMO).
- T-5 (a): phaseD_minor_ntf.md + refute_minor_ntf.md +
  esc_refute_ntf_r1/r2.md + esc_probe_ntf_*.py TUTTI su disco ✓;
  M0:3649+ APERTO ("[LAND-C4-LA2] NTF DERIVATION BLOCK ... landed
  S-FOUNDATIONS-C4 2026-08-21 ... escalation E-1 CLOSED DRY at round 2")
  ✓ ((a) LEGITTIMO — Fase D con verdetto).
- T-7: 79 nodi = 62+17 ✓ (da91aa4); tally 12/36/12/2 ✓ (fd2d444); mappa
  :317-341 APERTA — "0 BREAK / 0 REPAIR / 5 AMENDMENT / 4 NOTE — map
  SURVIVES" VERBATIM ✓.
- T-8: incidente 23/23 FEDELE ai due commit (7dea386 contiene "23/23";
  c9bacd9 2026-08-21 lo sana con run verificato) ✓ — già confermato da
  C3 con git show integrale.

### Finding

| # | Classe | CH4 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-07 | **REPAIR (ALTA)** | T-6 battuta 3 | "coda tipizzata alla chiusura C4: tier ONDEMAND sui 46 carrier + STALENESS LINK ... (commit `32459ca`, **2026-08-21**)". `git log 32459ca` = **2026-08-12**, tag `[F-SERVICE/S25][PIANO/R3c] C4 MECHANICAL CLOSURE`: il "C4" del messaggio è l'etichetta INTERNA della sessione S25 (cfr. memoria s25-engine-speed "C4 CHIUSA (tier ondemand+staleness)"), NON la finestra S-FOUNDATIONS-C4 (2026-08-20/21). Data sbagliata di 9 giorni + attribuzione di finestra sbagliata su un campo di join del retro-audit (guardia 15). Il contenuto (ondemand 46 carrier, staleness link, rejector sparato in-sessione) è VERO e verbatim nel messaggio. Riparazione: "commit 32459ca, 2026-08-12, chiusura C4-di-S25 (etichetta interna S25 ≠ finestra C4 S-FOUNDATIONS)". |
| ST-C5-08 | REPAIR (MEDIA) | T-4 battuta 2 | Etichetta "(b) STANCE-DI-FORK" INDEBITA: C49 NON esiste come riga del diff per-riga Fase B (perimetro C1-C48; unico tocco = ":233 candidate choice-ledger row (C49-class)", mai un verdetto per-riga); "l'aggiudicazione wave-2 È il verdetto di fork di Fase B-estesa (blocco3)" usa una categoria («Fase B-estesa») che il design §T-§6 non ammette. La doppia prova ESISTE ed è forte (wave-2 blocco3 zero-finding + item 3 :330 per la classe S1): il ramo CORRETTO è (c) NON-RIDERIVATO con quella doppia prova; opzionale co-citare phaseB:233 come adiacenza genuina di fork. Direzione non inflattiva sull'EVIDENZA ma inflattiva sull'ETICHETTA (fa sembrare C49 coperto dagli alberi ciechi). |
| ST-C5-09 | GAP (MEDIA) | T-1/T-3/T-4/T-7/T-8 battuta 3 — guardia 15 | Battute 3 senza DATA/PROCESSO propri (T-1 caveat G0 §4; T-3 "classe finale [REP]; C25 NEVER"; T-4 upgrade path; T-7 doppio consumer; T-8 "classe finale [REP]"). 5 battute; T-2/T-5/T-6 b3 portano data (ma T-6 la porta SBAGLIATA → ST-C5-07). |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-07 | Correggere data a 2026-08-12 + disambigua "C4-di-S25"; propagare la disambiguazione al §FP (collisione "C4") |
| ST-C5-08 | Rietichettare T-4 b2 come (c) con doppia prova invariata (+ phaseB:233 opzionale); aggiornare split INV_a CH4 (b)=3→2, (c)=4→5 |
| ST-C5-09 | Data+processo alle 5 battute 3 |

### Q&A SEED (dalla storia CH4)
1. **D**: "Una data sbagliata nella vostra storia: quante altre?" →
   **R**: il retro-audit ha camminato TUTTI i 30 commit citati dalle
   storie: 30/30 esistono, 1 solo mismatch di data (32459ca, riparato a
   registro con la causa nominata: collisione di etichetta "C4") — il
   tasso d'errore è stampato, non stimato. → **Ancora**: questo file §H.
   → **Backup**: tabella hash→data→battuta.
2. **D**: "Perché fidarsi del fitted se gli alberi ciechi non l'hanno
   riderivato?" → **R**: dichiarato: nessuna riderivazione
   dell'implementazione; la CLASSE S1 su cui poggia è riderivata 4/4
   (item 3), l'aggiudicazione della riga C49 è wave-2 a zero finding —
   doppia prova su due piani distinti, etichettata (c). → **Ancora**:
   phaseB:330-335; VERDICT_wave2; ledger C49:682-692. → **Backup**: card
   C49 (CH4 §7-bis).

### Guardie CH4 §6: 15 = **6 HIT** (5 campi mancanti + 1 data errata) / testata SILENT CLEAN / resto CLEAN

### VERDETTO CH4 §6: **REGGE-CON-RIPARAZIONI** (0 BREAK, 2 REPAIR di cui 1 ALTA, 1 GAP; contenuti fedeli ai carrier, difetti nei campi di join e in un'etichetta di ramo)

==============================================================================
## CH5 — Literature positioning (§6, writer B8b: 6 argomenti 6.1-6.6)

### Cammino eseguito
- Forma: OGNI battuta stampa DATA/PROCESSO/VERDETTO etichettati —
  guardia 15 CLEAN al 100%, la forma migliore dell'atlas insieme a CH9.
  6.4 dichiarata "mista eventi-correzione" (INV_b) — deviazione di
  template DICHIARATA e giustificata (eventi datati, non enunciati).
- 6.1: `ADVISORY_generality_litmap_2026-08-12.md` esiste ✓ (24 PDF ✓
  memoria); litreview confrontation ✓; b3 caveat Eq. 14 in-house C4 —
  coerente con LM (non ri-aperto: fuori nucleo).
- 6.2: b0a4c15 (lancio) + a85e355 (chiusura, "0 BREAK ... nothing
  crushes the project", "reviser 9/9 + confirm 9/9 FAITHFUL") VERBATIM
  nei messaggi ✓. [ADV-FIG] mai promossa a numero ✓ (guardia 6/13).
- 6.3: ea2abce VERBATIM ("D-01 gloss deleted ... three claimed forms ...
  KT2015 chain CONCEDED") ✓; near-miss dello sweep = KT2015 +
  ISABE-2003-117 ✓ (advisory + memoria).
- 6.4: VERIFY_PB_corner_pb.md ✓ (letto integrale da C3: due corner, Eq.
  22 p_inf / Eq. 26 p_b spaziale senza fonte — la battuta 2 è FEDELE);
  b3 = b0a4c15 "USER CHALLENGE ... SUSTAINED 3/4 measured ... unchased
  citation neighborhood" VERBATIM ✓.
- 6.5: b3da86d + 3b2b9e6 VERBATIM (v. §H) ✓; BPH:623-625 coerente con
  la verifica C3 (BPH:619-625) ✓.
- 6.6: 904f950 VERBATIM ✓; MA v. finding sull'etichetta di ramo.

### Finding

| # | Classe | CH5 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-10 | REPAIR (MEDIA) | 6.6 battuta 2 | Etichetta "(b) STANCE-DI-FORK" INDEBITA: il design §T-§6 definisce (b) = scelta del LEDGER con verdetto per-riga Fase B (phaseB §1) dichiarata stance di fork. L11 non è una riga ledger e NON ha verdetto Fase B; la battuta usa "stance" nel senso generico "lettura [INF] di capitolo dichiarata". Il contenuto è onesto e ancorato (pC:375-379, CT-2, L12 [REP] verbatim); il ramo CORRETTO è (c) NON-RIDERIVATO con doppia prova = L12 verbatim + regola CT-2 + REFUTE_CH5. Un retro-audit che joina su "(b)" cercherebbe un verdetto phaseB che non esiste. |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-10 | Rietichettare 6.6 b2 come (c); aggiornare split INV_b CH5 (0a/1b/4c/1misto → 0a/0b/5c/1misto) |

### Q&A SEED (dalla storia CH5)
1. **D**: "Le vostre correzioni-utente in storia: marketing
   dell'onestà?" → **R**: ogni correzione è un evento DATATO con
   carrier: misquote Harroun ritirata a registro (ea2abce), catch
   p_b/corner verificato alla fonte in-sessione (VERIFY_PB), sfida sul
   censimento SOSTENUTA 3/4 con riga findings coniata (b0a4c15) — le
   correzioni producono regole standing, non scuse. → **Ancora**: CH5
   §6 6.4. → **Backup**: catena catch→regola.
2. **D**: "P-B ottimizza già: la vostra dicotomia D-1 regge?" → **R**:
   la campagna 4-paper fu costruita APPOSTA per schiacciare il progetto
   (8 threat consolidate) e non lo schiacciò; P-B ottimizza UNO stato
   steady da p0/T0 mediate con p_b senza fonte (verificato alla pagina).
   → **Ancora**: a85e355; VERIFY_PB_corner_pb.md. → **Backup**: slide
   forma onesta CH5 feed 1 (vincolo WB1-C3-10).

### Guardie CH5 §6: 15 = **0 HIT** (CLEAN, forma esemplare) / lint-5 = 1 HIT di ramo (ST-C5-10)

### VERDETTO CH5 §6: **REGGE-CON-RIPARAZIONI** (0 BREAK, 1 REPAIR di taxonomy; ancore commit 6/6 verbatim-fedeli)

==============================================================================
## CH6 — Value/honesty/roadmap (§6-bis, writer B8b: 5 argomenti)

### Cammino eseguito
- Header "6-bis" con ragione dichiarata (legenda W2-R10 al posto §6) —
  posizione template rispettata ✓.
- 6-bis.1: 904f950 ("Gap-A/Gap-B value frame") ✓; checkpoint sfound
  :466-472 APERTO ("GAP-A/GAP-B VALUE FRAME registered (S-PRES anchor)
  ... value condition = Gap B material AND Gap A < Gap B") VERBATIM ✓;
  1a11f2c ("22 amendments carried / 0 contested sustained") VERBATIM ✓;
  claims:2262 APERTO (falsificatore "any argmax-shift number quoted at
  any grade ... before delta/L_H land") ✓ = esattamente la battuta 3.
- 6-bis.2: checkpoint S-PRES :198-256 APERTO (C-3 three-design frame,
  "which gap dominates, on which axis?" FIRST-LEVEL TREE NODE, working
  hypothesis dichiarata) ✓ FEDELE; MA v. finding etichetta.
- 6-bis.3: ea2abce ("PB-2 LOCKED formulation + 7-item caveat list") ✓;
  M0:2316-2319/2320-2326 ✓ (C3); fd2d444 ("mints C61 p_b-closure") ✓;
  MA v. finding attribuzione near-miss.
- 6-bis.4: da91aa4 ✓; mappa :180 APERTA ("⊘ D-44 — public
  adequacy-claim gate ... never demonstrated adequacy" + trigger
  findings:1468) ✓; findings:2530-2539 P34 ✓ (C3 guardia 7); d968502 ✓;
  PROGRESS:400-401 APERTO ("(ii) D-44: claim di adeguatezza gated...")
  ✓ = il trigger-scan Block 0 HA recepito D-44 come la battuta dice.
- 6-bis.5: findings:2148 datazione by-inclusion DICHIARATA nel testo ✓
  (limite di join stampato, non nascosto); 318d3fd ✓ VERBATIM;
  M0:1322-1331/[GRAFT-G10] ✓ (C3 + VERDICT_r22f:106-122 "GRAFT-G10
  nearest-referee enrichment (named and disqualified)").

### Finding

| # | Classe | CH6 §6-bis argomento | Evidenza |
|---|---|---|---|
| ST-C5-11 | REPAIR (MEDIA) | 6-bis.3 battuta 2 | ATTRIBUZIONE SBAGLIATA del finder: "il near-miss Efremov-Kraiko 2004 TROVATO dallo sweep 1971-2026 (`ADVISORY_litmap_extension_2026-08-13.md`)". Riesecuzione in finestra: `grep -in efremov ADVISORY_litmap_extension_2026-08-13.md` = **0 hit**; i 2 near-miss dello sweep sono Kraiko-Tillyaeva 2015 e ISABE-2003-117 (advisory + memoria post-s25bis-litmap). Efremov-Kraiko 2004 vive nell'ALTRO artefatto della stessa giornata: `ADVISORY_litreview_confrontation_2026-08-13.md:107` (riga 7 del confronto 25-paper, "massima spinta MEDIA SUL PERIODO ... l'ottimo periodico risulta STAZIONARIO") e :277/:285. Stessa classe della WB1-C3-09 di C3 (conflazione dei due artefatti lit del 2026-08-13). Il CONTENUTO della battuta (lock D-06 che consuma E-K 2004, commit ea2abce) è vero; il processo attribuito è falso. Riparazione: "trovato dal confronto litreview 25-paper (ADVISORY_litreview_confrontation:107); lo sweep 1971-2026 (litmap_extension) aggiunge i near-miss KT2015/ISABE e NON scalfisce il lock". |
| ST-C5-12 | REPAIR (MEDIA) | 6-bis.2 battuta 2 | Etichetta "(b) STANCE-DI-FORK (le tre battute utente...)" INDEBITA: le correzioni utente C-3/C-3bis/C-3ter (2026-08-23) non sono verdetti per-riga di Fase B — nessun fork degli alberi ciechi è coinvolto. Il contenuto è ancorato (checkpoint :198-256) e la forma onesta esiste già nell'atlas: CH5 6.4 tratta le correzioni utente come "eventi-correzione, non classificabile a/b/c" DICHIARATO. Riparazione: stessa forma di CH5 6.4 (misto eventi datati) o (c) con doppia prova = checkpoint + REFUTE_CH6; aggiornare split INV_b CH6 (0a/1b/4c → 0a/0b/4c/1misto). |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-11 | Ri-ancorare il finder a ADVISORY_litreview_confrontation:107 (+ ruolo corretto dello sweep) |
| ST-C5-12 | Rietichettare 6-bis.2 b2 come misto eventi-correzione (forma CH5 6.4) o (c); allineare INV_b |

### Q&A SEED (dalla storia CH6)
1. **D**: "Chi vi impedisce di citare un numero di optimum-shift in
   conferenza?" → **R**: il registro stesso: falsificatore ARMATO su
   claims:2262 — "any argmax-shift number quoted at any grade before
   delta/L_H land" fa scattare la riga findings; la storia mostra che la
   forma onesta è il PRODOTTO di escalation refuter, non una cautela
   verbale. → **Ancora**: claims:2262; 904f950. → **Backup**: slide
   canale (vi) con deriver ordinati.
2. **D**: "Il vostro claim di novità PB-2 è sopravvissuto per fortuna?"
   → **R**: no: il confronto 25-paper ha TROVATO l'antenato mediato
   (Efremov-Kraiko 2004, collassante per ammissione degli autori) e il
   claim è stato RISCRITTO nella forma vincolata D-06 con concessioni
   stampate; lo sweep 1971-2026 separato ha aggiunto 2 near-miss
   nominati senza ucciderla. → **Ancora**: ADVISORY_litreview
   _confrontation:107; ea2abce; M0:2320-2326. → **Backup**: slide forma
   bloccata D-06.

### Guardie CH6 §6-bis: 15 = **0 HIT** (1 datazione by-inclusion DICHIARATA, conteggiata come limite dichiarato, non violazione) / lint-5 = 1 HIT di ramo (ST-C5-12)

### VERDETTO CH6 §6-bis: **REGGE-CON-RIPARAZIONI** (0 BREAK, 2 REPAIR: 1 attribuzione di processo, 1 taxonomy)

==============================================================================
## CH7 — Averaging edifice (§6, writer B8a: 6 argomenti T-1..T-6)

### Cammino eseguito
- T-2: formalization :92-96 APERTO ("the verification layer is UNPROVEN
  in the confirm direction this window (known-true seed FAILED); nothing
  in this revision may be cited as layer-certified and the Blocco-2
  landing gate stays CLOSED") VERBATIM ✓; :209-211 APERTO ("FOURTH
  consecutive over-certification (counter updated)") VERBATIM ✓; file =
  3090 righe → ancora :3061-3090 (§7 absorption targets) in-range ✓;
  r2pass/VERDICT_r2pass.md e VERDICT_confirm.md esistono ✓. Il ramo (a)
  è quello PRE-ASSEGNATO dal design ("N-E via Fase D (mean-swirl,
  R22-F)", §T-§6:221-222) e la battuta porta INLINE i caveat vincolanti
  — la tensione "RIDERIVATO-PIENO" vs "landing gate CLOSED" è governata
  dal caveat stampato: ACCETTATO senza finding.
- T-3: mirror di CH3 T-2..T-4, ancore già verificate ✓ (rimando
  dichiarato, no duplicazione ✓).
- T-4: DISPATCH_swirl5f anchors ✓ (:64 verificata; :118-128
  grades-not-record e :179-183 decisioni utente coerenti con memoria
  swirl5f-panel); MA v. finding etichetta "(a)-IN-PANEL".
- T-5 (a): tre provenienze verificate (v. CH3; M0:1768-1773 VERBATIM) —
  (a) LEGITTIMO.
- T-6: saldature 1-2 ancore verificate (centerpiece :461-463 saldatura
  testuale a D.18 — coerente con la mia lettura :459-481; VERDICT_r22f
  Part-2 ✓); saldatura 3 = F-4 — MA v. finding di sovra-dichiarazione.

### Finding

| # | Classe | CH7 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-13 | REPAIR (MEDIA) | T-6 battuta 2 / FINDING F-4 (+ HISTORIAN_INV_a §2 riga F-4) | "doppia prova: ASSENTE ... in attesa della refutazione d'onda W-C" è SOVRA-DICHIARATA: la refutazione della saldatura 3 È GIÀ AVVENUTA — `REFUTE_CH7.md` finding 5 (REPAIR MEDIA) ha camminato esattamente §1.1+§1.5(3), ha bocciato la forma "STAGED" e ha disposto la riparazione ("dichiarare la saldatura 3 come lettura di assemblaggio ... ancorata a B-1/B-2 + :101-102") che il capitolo ha APPLICATO — la forma attuale di §1.5.3 è il prodotto post-refutazione. Incoerenza interna: CH5 6.1 b2 conta REFUTE_CH5 (stessa onda) come doppia prova valida. F-4 non va cancellata ma RIFORMULATA: "doppia prova = REFUTE_CH7 #5 (camminata + riparazione applicata); residuo = re-refutazione della forma riparata" — residuo che QUESTO passaggio (W-C.b) consuma sul piano storico: la classificazione assemblaggio-vs-testuale di T-6 regge alla mia camminata. |
| ST-C5-14 | REPAIR (BASSA) | T-4 battuta 2 | Etichetta "(a)-IN-PANEL con clausola di provenienza" FUORI TAXONOMY: il panel swirl5f (finestra parallela 2026-08-17→19) NON è Fase A/B/D di S-FOUNDATIONS; il lint 5 ammette (a)/(b)/(c). La sostanza è onesta (grades-not-record stampato, :118-128). Ramo corretto: (c) NON-RIDERIVATO in Fase A/B/D; doppia prova = panel a convergenza con judge-verifier sympy (advisory, consumo dichiarato a ogni uso). |
| ST-C5-15 | GAP (BASSA) | T-1 b2/b3, T-6 b3 — guardia 15 | T-1 b2 senza DATA propria (il "PROCESSO/VERDETTO" ci sono; la doppia prova è il trittico stesso — auto-referenza ammessa da INV_a ma il join resta senza data); T-1 b3 e T-6 b3 senza DATA né PROCESSO. 3 battute. |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-13 | Riformulare F-4 in CH7 T-6 b2 E in HISTORIAN_INV_a §2 (doppia prova = REFUTE_CH7 #5; residuo consumato da W-C.b); il conteggio finding B8a scende da 4 "assenti" a 3 + 1 riformulata |
| ST-C5-14 | Rietichettare T-4 b2 come (c) con doppia prova panel+verifier; INV_a CH7 split (a)=4→3, (c)=2→3 |
| ST-C5-15 | Data (+processo) alle 3 battute nominate |

### Q&A SEED (dalla storia CH7)
1. **D**: "Il capitolo nasce da una vostra falla (i tre piani slegati):
   perché fidarsi della saldatura?" → **R**: le saldature sono
   CLASSIFICATE: 1-2 testuali nei file refereed di Fase D (ancore alla
   riga), la 3 dichiarata lettura di assemblaggio, attaccata dal refuter
   di capitolo (REFUTE_CH7 #5), riparata nella forma dichiarata e
   ri-camminata da questo passaggio — la falla è l'origine DICHIARATA
   del capitolo, non un retrofit. → **Ancora**: CH7 header :3-8;
   REFUTE_CH7 #5; questo file. → **Backup**: tabella saldature con stato
   di prova.
2. **D**: "Mean-swirl: 'riderivato-pieno' ma 'landing gate CLOSED' —
   quale dei due?" → **R**: entrambi, e la storia li stampa insieme:
   catena until-dry r1-r7 con carrier sympy ESEGUITA, MA verification
   layer unproven in confirm direction dichiarato VERBATIM fino a r7 e
   contatore di over-certificazione a 4 — advisory-class finché
   l'absorption non passa; niente auto-promozione. → **Ancora**:
   formalization :92-96, :209-211. → **Backup**: slide stato dei tre
   piani (T-2/T-3/T-4 battute 3).

### Guardie CH7 §6: 15 = **3 HIT deboli** (ST-C5-15) / lint-5 = 1 HIT di ramo (ST-C5-14)

### VERDETTO CH7 §6: **REGGE-CON-RIPARAZIONI** (0 BREAK, 2 REPAIR, 1 GAP; l'onestà dei caveat T-2 è la migliore istanza dell'atlas)

==============================================================================
## CH8 — Design space (§6, writer B8b: 6 argomenti 6.1-6.6)

### Cammino eseguito
- 6.1 (b): quote errata VERIFICATA VERBATIM nel messaggio di 5221529
  ("topology errata (census S0-collapse beats the blind tree's
  disconnectedness claim; P-F17 divergence -> Phase C agenda)") ✓ —
  QUESTO è un (b) legittimo (vero evento di fork con aggiudicazione).
  problem_book:337-353 ✓ (non ri-aperto: quota corta e coerente con §1).
- 6.2 misto (a)+(c): gamba esistenza via phaseB:336-338 APERTO (item 4
  "Existence road (P7/Chenais): H-F34 cites Chenais 1975 ... verbatim;
  V-F15 adds the conditional-theorem form with H-STAB" — righe ESATTE)
  ✓ (a) LEGITTIMO; gamba finitezza (c) con caveat census APERTO
  (":11-13 the formal-convergence criterion ... was NOT met before
  infrastructure truncation. Nothing here is of record until...")
  VERBATIM ✓ — il caveat del panel è STAMPATO nella battuta: forma
  esemplare; M0:313-320 APERTO ("'FINITE' here carries NO declared
  rigor class at this site of record") VERBATIM ✓;
  PROGRESS_ARCHIVE:413 APERTO ("R5c census-lemma — SCHED(F2-exit...)")
  ✓.
- 6.3: census §7pin :329+ APERTO ("USER PIN RECORD (2026-08-02...)") ✓;
  M0:306-312 APERTO (nota "PINS SINCE DECIDED — added 2026-08-06") ✓;
  MA v. finding etichetta + data.
- 6.4 (a): phaseB:339-344 APERTO (item 5: "delta = 0 iff one shape is
  per-phase optimal mu-a.e. = the T3/T4 dichotomy criterion re-derived
  ... 'any J > B is an instant solver-bug rejector' = bound-as-oracle
  doctrine") VERBATIM — il perimetro copre ESATTAMENTE la gamba
  rivendicata (criterio della dicotomia; [T-OP11e] resta su carrier
  in-house, correttamente NON attribuito agli alberi) ✓ (a) LEGITTIMO.
  M0:4138-4140 ✓; claims:368-379 APERTO (scope [T-OP11e]: "winners rank
  CLOSURES at equal eps_max, never hardware") VERBATIM ✓.
- 6.5 (b): phaseB:22 (C1 "DIVERGENT-ENRICHING, HIGH"), :66 (C9
  "DIVERGENT, HIGH, 4/4 CONVERGENT AGAINST THE INCUMBENT"), :159 (C31
  "CONVERGENT on family + DIVERGENT on the IP half") — TUTTE APERTE
  ALLA RIGA, esatte ✓ (b) LEGITTIMO con la dichiarazione giusta.
- 6.6: a85e355/fd2d444/b3da86d ✓ (v. §H); problem_book:347-348 APERTO
  ("base-pressure closure p_b declared (N2)") ✓; claims:181 in-range
  della riga PB-2 ✓; mappa edge E12 non ri-aperta (coerente con
  da91aa4).
- Guardia 15: le battute 3 di 6.2/6.3 dichiarano "nessun evento di
  chiusura ancora / NON ancora avvenuta (stato al 2026-08-23)" — forma
  CONFORME (la data è quella dello stato; il processo è nominato).

### Finding

| # | Classe | CH8 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-16 | REPAIR (MEDIA) | 6.3 battuta 2 | Etichetta "(b) STANCE-DI-FORK" INDEBITA: i pin utente 2026-08-02 (cono/PERMISSIVA/NONBLOCK+/Λ) non sono righe del choice ledger e NON hanno verdetto per-riga Fase B (perimetro C1-C48; i CEN-O* non vi compaiono). Incoerenza interna d'atlas: CH1 T-1 tratta il pin utente correttamente come (c) "PIN utente, per costruzione fuori dal perimetro derivativo". Ramo corretto: (c) con doppia prova = garanzia di generalità del census (:371-377) + state-pointer M0 con emendamenti QUEUED. Aggiornare split INV_b CH8. |
| ST-C5-17 | NOTE (BASSA) | 6.3 battuta 2 | "DATA: 2026-08-05 (state-pointer notes datate in M0)": la nota M0:306-312 è datata **2026-08-06**; è la nota :313-320 (sector-finiteness) a portare 2026-08-05. Stampare entrambe le date per nota o correggere. |
| ST-C5-18 | NOTE (BASSA) | 6.6 battuta 1 | "fork adjudication 141 (commit a85e355: ... 90/50/1/0 riconciliati)": il conteggio "90/50/1/0 reconciled" vive nel messaggio di **b0a4c15** ("FORK_LEDGER_141 DONE (90/50/1/0 reconciled...)"); a85e355 porta "48/50 covered-by-cluster, 2 genuine gaps". Le virgolette sui "2 genuine gaps" sono corrette; doppia ancora richiesta (b0a4c15 + a85e355). |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-16 | Rietichettare 6.3 b2 come (c) (forma CH1 T-1); INV_b CH8 split 1a/3b/1c/1misto → 1a/2b/2c/1misto |
| ST-C5-17 | Correggere/duplicare la data delle note M0 |
| ST-C5-18 | Doppia ancora b0a4c15+a85e355 sul conteggio fork |

### Q&A SEED (dalla storia CH8)
1. **D**: "Un albero cieco vi ha contraddetto sulla topologia: chi ha
   vinto e perché?" → **R**: il record, per errata ADIUDICATA e datata:
   "census S0-collapse beats the blind tree's disconnectedness claim" —
   e la divergenza P-F17 è entrata in agenda Phase C, non nel cestino.
   → **Ancora**: commit 5221529 (verbatim). → **Backup**: slide
   fork-divergenze e loro consumo.
2. **D**: "La finitezza dei settori è un teorema?" → **R**: NO, e il
   record lo stampa due volte: M0 "'FINITE' carries NO declared rigor
   class" + caveat del panel census ("criterio formale NON raggiunto
   prima del troncamento"); la prova è un DEBITO schedulato (census-lemma,
   F2-exit). → **Ancora**: M0:313-320; census :11-13;
   PROGRESS_ARCHIVE:413. → **Backup**: riga debito con finestra.

### Guardie CH8 §6: 15 = **0 HIT** (stati-aperti datati conformi) / lint-5 = 1 HIT di ramo (ST-C5-16)

### VERDETTO CH8 §6: **REGGE-CON-RIPARAZIONI** (0 BREAK, 1 REPAIR taxonomy, 2 NOTE; i due (a) e i due (b) legittimi sono verificati alla riga)

==============================================================================
## CH9 — Certification (§6, writer B8b: 5 argomenti 6.1-6.5)

### Cammino eseguito
- 6.1: D6:775 e :285 APERTI ("ORACLE GATE (absolute): O1/O2/O3 or no
  science") VERBATIM ✓; (a) "architettura" via phaseB:330-335
  ("capturing never a certificate" ✓ alla riga) + :347-350 (item 7,
  "The strongest single methodological validation in the diff" ✓
  verbatim) — lo SCOPING "(architettura)" rende il ramo (a) corretto:
  ciò che gli alberi hanno riderivato è la classe+il vincolo prezzato,
  non il gate di governance (che la battuta 3 classifica PRACTICE) ✓.
- 6.2: claims:485-497/656-668/795-800/1945 non tutte ri-aperte (C3 e
  join interni coerenti); findings:1511/:1517 (X-CDKAT −13.9% stamp
  intatto) coerenti con memoria e con CARD J/3 §7 ✓.
- 6.3: f3c5df5 APERTO ("S-ORDINE prompt: NOTHING-LOST elevated from
  principle to FIRING GATE (user order)") VERBATIM ✓; hypaudit :15-19
  APERTO ("Canary (SEED-A...) FIRED correctly ... Known-true seed
  (SEED-B...) DID NOT [flag]") VERBATIM ✓; 5221529 APERTO ("first seed
  mis-design caught by the refuter, adjudicated, re-run PASSED both
  directions" + "instrument adopted-as-candidate standing R3 gate")
  VERBATIM ✓; fd2d444 ✓. Tre finestre indipendenti di fuoco = la
  battuta 2 è ESATTA.
- 6.4: PROGRESS_2026-08-13_Scert.md esiste ✓; la clausola (iii) "alla
  prima passata RIFIUTÒ l'auto-assoluzione su un verification layer non
  provato" VERIFICATA: Scert progress :184 "pass refused to certify
  itself on a broken verification layer" ✓ (ancora non citata dalla
  battuta → nota migliorativa sotto); delta oggetto→certificatore ✓
  (memoria fservice-scert).
- 6.5: claims:795-800 [X-GENOXC] ✓ (per join CH9 6.2);
  ADVISORY_moc_zucrow_fidelity_2026-08-13.md ✓ (memoria s-genoaudit:
  accordo Ch.16≡Ch.17 VACUO, ramo cross-stream mai esercitato — la
  battuta è FEDELE alla memoria/advisory); MOC-10 quarantena VERBATIM in
  5221529 ("GENO thrust references QUARANTINED") ✓.
- Guardia 15: TUTTE le battute con DATA/PROCESSO/VERDETTO espliciti ✓.

### Finding

| # | Classe | CH9 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-19 | NOTE (BASSA) | 6.4 battuta 2 (iii) | La clausola auto-assoluzione è VERA ma senza ancora di riga: aggiungere `validation/PROGRESS_2026-08-13_Scert.md:184` ("pass refused to certify itself on a broken verification layer") per chiudere il join. |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-19 | Aggiungere l'ancora Scert:184 alla clausola (iii) |

### Q&A SEED (dalla storia CH9)
1. **D**: "Vi siete auto-certificati NON-certificabili: teatro?" →
   **R**: il NO ha superato le SUE controprove: dual-seed provato nei
   due sensi su tre finestre datate (con un seed mal disegnato COLTO dal
   refuter e ri-eseguito — a registro), dual-code con quarantena del
   proprio oracolo dove l'audit l'ha imposto, e il refuter che ha
   rifiutato l'auto-assoluzione su un layer non provato. → **Ancora**:
   CH9 §6 6.3/6.4; 5221529; Scert:184. → **Backup**: slide "il NO come
   segnale".
2. **D**: "Accordo cross-code = verità?" → **R**: NO per dottrina di
   record, e l'abbiamo dimostrato DA NOI: l'audit del partner GENO ha
   trovato accordo VACUO sul rotazionale e un double-count wall-thrust
   (MOC-10) → riferimenti di spinta QUARANTENATI; la coppia matura è
   [X-GENOXC]+[X-O31CS] primal-independent. → **Ancora**: CH9 §6 6.5;
   5221529. → **Backup**: slide invarianti indipendenti.

### Guardie CH9 §6: 15 = **0 HIT** (CLEAN)

### VERDETTO CH9 §6: **REGGE** (0 BREAK, 0 REPAIR, 1 NOTE; la storia meglio ancorata dell'atlas — ogni quote verbatim ha retto all'apertura)

==============================================================================
## CH10 — Data contract (§6, writer B8b: 5 argomenti 6.1-6.5)

### Cammino eseguito
- 6.1 (a): VERDICT_contract_and_L4R1.md APERTO — "(i) RE-DERIVED —
  independent validation (9 items)" (:30) ✓ = "9 elementi riderivati
  ciechi"; F-1/F-2/F-3 (P2) alle righe :54/:61/:66 con contenuti ESATTI
  (function-space pin / audit stage-A datum-internal / uncertainty
  contract) ✓; "arricchimenti, non smentite" = fedele alla struttura
  (ii) del diff ✓. (a) LEGITTIMO. Battuta 3: guardie 11/17 con ancore
  checkpoint ✓ (GUARD_CHECKLIST :24/:30 coerenti).
- 6.2 (a): phaseD_L4_implies_R1.md esiste; giudice "downgrade-only" e
  cap r2 NOT-DRY DICHIARATI nella battuta (VERDICT B.1/B.3) ✓;
  hypaudit :482 APERTO ("[R1-CAUSAL] causal separation | CONDIZIONATA
  (window W1–W4) ... mu(Xi_sub)>0") VERBATIM ✓. (a) LEGITTIMO con cap
  stampato. MA v. finding conteggio righe.
- 6.3: D6:808-810 APERTO ("G6 (new) DATA-CONTRACT GATE ... rejected
  loud — no design on inconsistent data") VERBATIM ✓; :811-815
  (TRIPLE D.14 + D.16 "SPECIFIED-NOT-ARMED") VERBATIM ✓; hypaudit
  :381-385 APERTO ([CONTRACT-MU] E1-E5 LDM con "E3 CONDIZIONATA"
  dentro) ✓; MA la QUOTE stage-A è altrove (v. finding).
- 6.4: 1d9609a ✓ (S21 close); 3b2b9e6 ✓ VERBATIM; hypaudit :485
  ("L4 possibly empty on real engines") in-range della tabella ✓;
  D6:176-190 smeared-contact non ri-aperto (coerente col piano).
- 6.5: phaseB:330-335 APERTO ("wild non-uniqueness fenced by class
  fiat, declared openly" ✓ verbatim, item 3); conditionals doc :1-16/
  :7-9 coerenti (C-D25U/C-MAJDA stated-once = commit c4d5a95 ✓);
  MA v. finding etichetta.

### Finding

| # | Classe | CH10 §6 argomento | Evidenza |
|---|---|---|---|
| ST-C5-20 | NOTE (MEDIA) | 6.3 battuta 2 | Quote e ancora disallineate: la battuta stampa «"the stage-A audits are work the published SOTA never did"» ancorata a VERDICT_hypothesis_audit.md:381-385; la frase reale vive a **:459** ed è «The program's stage-A audits are non-redundant work the SOTA never did». Quasi-verbatim inesatto + ancora sbagliata su un campo di join. Riparazione: quote esatta + ancora :459 (la :381-385 resta per il bundle LDM). |
| ST-C5-21 | NOTE (BASSA) | 6.3 battuta 3 | Ancora "D6:1155-1157" per l'invariante off-manifold: la frase "(a generator emitting off-manifold data is a generator bug)" vive a **D6:1151**. Ri-puntare :1150-1152. |
| ST-C5-22 | NOTE (BASSA) | 6.2 battuta 2 | "phaseD_L4_implies_R1.md, **1529 righe**": misura in finestra `wc -l` = **2105 righe**. Conteggio stale (probabile revisione precedente) — SR-12: i conteggi si misurano nella propria finestra o si omettono. Riparazione: "2105 righe (wc -l 2026-08-23)" o togliere il numero. |
| ST-C5-23 | NOTE (BASSA) | 6.5 battuta 2 | Etichetta (b) con ancora di §3 theory-layer (phaseB:330-335 = item 3), non un verdetto per-riga §1: mislabel in direzione CONSERVATIVA (l'ancora citata licenzia (a) sulla gamba architettura-della-classe, o un (c) pulito). Nessuna inflazione; allineare per coerenza di taxonomy (e INV_b CH10 split). |
| ST-C5-24 | NOTE (BASSA) | 6.1 battuta 2 | "workflow 10/10" non riscontrato nel giudice (grep su VERDICT_contract_and_L4R1.md = 0 hit; il "(ii)" del diff ha 10 item ma è la lista demanded-missing). Citare l'ancora reale o rimuovere il frammento. |

### Disposizione

| Finding | Disposizione proposta |
|---|---|
| ST-C5-20 | Quote esatta + ancora hypaudit:459 |
| ST-C5-21 | Ri-puntare a D6:1150-1152 |
| ST-C5-22 | Conteggio ri-misurato in finestra o rimosso |
| ST-C5-23 | Etichetta allineata ((a) scoped o (c)); INV_b aggiornato |
| ST-C5-24 | Ancora reale per "workflow 10/10" o rimozione |

### Q&A SEED (dalla storia CH10)
1. **D**: "G6 non ha mai rigettato nulla: gate di carta?" → **R**: il NO
   di G6 non ha mai sparato perché NESSUN dataset reale è mai stato
   ingerito — dichiarato in §5, non nascosto; la legittimità del
   contratto è però AUDITATA (bundle E1-E5 LDM con E3 CONDIZIONATA
   dentro) e il loud-reject set è già esteso (TRIPLE/D.16,
   SPECIFIED-NOT-ARMED con owner F2a). → **Ancora**: CH10 §6 6.3;
   hypaudit:381-385; D6:808-815. → **Backup**: slide stato del gate con
   finestra di armamento.
2. **D**: "Il contratto è un formato inventato da voi: chi l'ha
   convalidato?" → **R**: una formalizzazione CIECA (brief agnostico) ne
   ha riderivato 9 elementi su 9 e ha CHIESTO 3 cose che mancavano
   (F-1/F-2/F-3, a registro come righe P2) — convalida + arricchimento,
   con i disaccordi genuini (C52/C53/C54) in card NEVER stampate. →
   **Ancora**: VERDICT_contract_and_L4R1.md:30,54-66. → **Backup**:
   card C52/C53/C54 (CH10 §5).

### Guardie CH10 §6: 15 = **0 HIT** (by-inclusion dichiarate) / 5 NOTE d'ancora

### VERDETTO CH10 §6: **REGGE-CON-NOTE** (0 BREAK, 0 REPAIR, 5 NOTE di cui 1 MEDIA; entrambi gli (a) verificati alla riga)

==============================================================================
## §SILENT — Le 12 righe SILENT (mandato punto 3)

Lista di record (phaseB_tree_diff.md:397-399, APERTA): C2(conditional),
C5, C15, C16, C22, C23, C30, C40, C45, C46, C47, C48 — somma verdetti
8+10+11+6+12+1 = 48 ✓.

- **Unica comparsa nelle storie**: CH4 §6 testata (:694-696) — dichiarate
  "ramo (c) per definizione (sotto la granularità degli alberi ciechi)"
  ✓ CONFORME al design §T-§6:231; ancora INV_a (phaseB:393-399) ✓
  corretta.
- **Sweep negativo eseguito**: nessuna delle 12 righe è usata come
  supporto (a)/(b) in alcuna battuta dei 10 capitoli (le righe ledger
  citate nelle battute 2 sono C31/C24/C1/C9 — tutte NON-SILENT, verdetti
  per-riga verificati alla riga; C49/C53/C54/C58/C61 sono FUORI perimetro
  C1-C48 e le battute che le toccano lo dichiarano o vengono riparate da
  ST-C5-08).
- **Esito: CLEAN** — nessuna riga SILENT spacciata per convergenza.

==============================================================================
## §AXES — §7(c) vs conformity map §C (mandato punto 4)

Metro: design v2 §C (:266-289, otto assi; "ogni §7(c) di nodo punta
all'asse pertinente"). Nessuna tabella nodo→asse è pre-fissata dal
design: il giudizio è di pertinenza + fedeltà della divergenza
dichiarata alla mappa.

| CH | assi citati | giudizio |
|---|---|---|
| CH1 §7(c) | §C-7 (peer-review avversaria) + §C-3 | PERTINENTE (aggiudicazione di scelta via panel/refuter; divergenza "reviewer interno, esterno resta G5/JPP" = riga 7 della mappa verbatim) ✓ |
| CH2 §7(c) | §C-3 (ECSS/DO-178C) + §C-2 | PERTINENTE (catena id→carrier→rejector del gradiente; divergenza "nessun audit esterno né certificazione DI" = mappa) ✓ |
| CH3 §7-DWR(c) | §C-2 (GRADE) | PERTINENTE (classi per cella + "NO cell above its held evidence class" = il criterio GRADE-struttura della mappa) ✓ |
| CH4 §7(c) | §C-3 + §C-5 (FAIR) + §C-2 | PERTINENTE (numeri engine sotto R5-provenance = riga 5 della mappa; auto-vincolo lint 6 stampato) ✓ |
| CH5 §7(c) | §C-1 (PRISMA) | ESATTO (capitolo letteratura = riga 1; divergenza "disciplina, non checklist 27-item" verbatim dalla mappa) ✓ |
| CH6 §7(c) | §C-2 + §C-6 (assertion-evidence) | PERTINENTE (classi di valore + consumo deck col retro-audit = riga 6) ✓ |
| CH7 §7(c) | §C-1 + §C-2 | PERTINENTE (lineage/procurement con read-status; il PENDING-PROCUREMENT Tillyaeva come istanza della disciplina è l'uso GIUSTO della riga 1) ✓ |
| CH8 §7(c) | §C-3 (con ancora di riga :279) + §C-2 (:278) | PERTINENTE ed ESEMPLARE (unico §7(c) che cita la mappa alla RIGA) ✓ |
| CH9 §7 | §C-3 + §C-4 (docs-as-code/Diátaxis) | PERTINENTE (registri machine-linted = reference; divergenza Diátaxis "mappa dei ruoli, non rito" = mappa verbatim) ✓ |
| CH10 §7(c) | §C-5 (FAIR, ancora :281) + §C-3 (:279) | PERTINENTE (il contratto-dati È l'istanza letterale della riga 5; divergenza repo-chiuso dichiarata = mappa) ✓ |

**Esito: 10/10 assi PERTINENTI, zero assi sbagliati**; divergenze
dichiarate fedeli alla mappa (nessuna divergenza inventata o taciuta).

**Campione 15 id registry citati nei §7 (grep in finestra, `id:` esatto)**:
yamamoto_1986_numermath48 (:1047), shi_xie_xuan_nocedal_2022_fd_interval
(:1078), wanted_roache_gci_1994_1997 (:884), wanted_celik_2008 (:890),
wanted_onofri_paciorri_2017_book (:1142), wintenberger_shepherd_2004
(:261), kraiko_tillyaeva_2015 (:498), wanted_tillyaeva_1975 (:742),
masters_etal_2017 (:1023), lauer_ansell_2025_pas (:1031),
giles_pierce_2001 (:507), wanted_hicken_zingg_2014 (:920), lozano_2019
(:170), venditti_darmofal_2000 (:999), li_xu_lv_yu_zhou_2025 (:690) —
**15/15 ESISTONO** alle righe stampate. (Il campione integra i ~30 id già
verificati da C3 su CH1-CH8; la copertura CH9/CH10 è nuova di questa
finestra.)

==============================================================================
## §FP — FUORI-PERIMETRO EREDITATI (mandato punto 5) + nuovi

1. **Collisione namespace "C31" (ereditata da B8a, ADIUDICATA QUI).**
   Occorrenze NELLE STORIE: CH2 §6 T-4 b1 (:543) e T-5 b1 (:564) =
   senso RATIFICA UTENTE (T7(c) forma a cono, F-SERVICE 2026-08-13);
   CH4 §6 T-2 (:717+) e CH8 §6 6.5 b2 (:667) = senso RIGA LEDGER
   (optimizer engine, choice_ledger:481-493). Entrambi gli usi sono
   INTERNAMENTE corretti ma il join del retro-audit su "C31" ambiguo.
   **Disambiguazione proposta (per storici + storyboard + CH-REF)**:
   (i) nelle storie e nel deck scrivere SEMPRE "ratifica-C31" (o
   "C31-ratifica, F-SERVICE 2026-08-13") vs "C31 (ledger, optimizer)";
   (ii) una riga di glossario/CH-REF che registra la collisione con le
   due ancore (choice_ledger:481-493 vs memoria
   fservice-scert-double-session); (iii) il box nomenclatura di CH5
   [WB1-R3] è la casa naturale dell'avviso (già segnalato da C3 per la
   famiglia G: WB1-C3-11 — estendere lo stesso box a C31).
2. **NUOVA collisione namespace "C4"** (emersa da ST-C5-07): "C4" =
   finestra S-FOUNDATIONS-C4 (2026-08-20/21) MA ANCHE etichetta interna
   S25 ("C4 MECHANICAL CLOSURE", commit 32459ca, 2026-08-12; memoria
   s25-engine-speed "C4 CHIUSA"). È esattamente il meccanismo che ha
   prodotto l'unico errore di data del corpus storie. Stessa
   disposizione: riga nel box nomenclatura/CH-REF.
3. **Ancora stale findings_registry:1455 su [S-T0P]** (ereditata da
   INV_a §3.2): VERIFICA ESEGUITA — `grep -n 1455 CH*.md` : le
   occorrenze in CH3/CH6/CH8 sono `M0:1455-1464` (file DIVERSO, blocco
   Humphreys ORCH-HARV-3 — nessuna collisione di contenuto); le uniche
   citazioni di findings:1455 sono CH1 §3.1 (:383, FUORI §6, con la
   staleness GIÀ dichiarata in-place [W2-R8]) e la disposizione W2. **Le
   §6 NON citano findings:1455**: CH1 §6 T-3 b3 cita il range
   :1450-1458, che contiene la riga `theory:s-t0p-proof-writeup-pending`
   (id a :1451) — range CORRETTO allo stato attuale del registry. CLEAN;
   nessuna eredità dell'ancora stale nel piano-storie.
4. **Per l'orchestratore / owner altrui**: (i) preamboli CH9:13 e
   CH10:12 ancora "placeholder W-B.2" = STALE (già segnalato da INV_b
   §3.1-3.2, owner B1/orchestratore); (ii) la riformulazione F-4
   (ST-C5-13) tocca ANCHE `HISTORIAN_INV_a.md` §2 — file non mio, edit
   agli storici; (iii) gli split (a)/(b)/(c) degli inventari cambiano
   dopo le rietichettature ST-C5-08/-10/-12/-14/-16/-23: i conteggi
   INV_a/INV_b vanno RIGENERATI da comando misurato (SR-12), mai
   aggiornati a mano dai delta qui elencati; (iv) il totale trittici
   B8a+B8b resta 34+27 = 61 argomenti, non toccato dalle riparazioni.

==============================================================================
## CONTEGGIO GUARDIE (aggregato §6, 10 capitoli)

- **Guardia 15 (convergence provenance)** — il fuoco del mandato:
  - B8b (CH5/6/8/9/10): **0 HIT** su 27 argomenti — campi DATA/PROCESSO/
    VERDETTO etichettati esplicitamente in OGNI battuta; 2 datazioni
    by-inclusion/limite-di-join DICHIARATE nel testo (CH8 6.1-6.2, CH6
    6-bis.5) = conformi come limite stampato.
  - B8a (CH1/2/3/4/7): **19 HIT** su 34 argomenti — 18 battute-3 (e 2
    battute T-1 CH7) senza DATA e/o PROCESSO propri (ST-C5-02/-03/-06/
    -09/-15) + **1 data ERRATA** (ST-C5-07, l'unico caso in cui il campo
    c'è ed è sbagliato — il più grave). Pattern sistematico: la
    convenzione di testata "ogni battuta porta DATA+PROCESSO+VERDETTO" è
    rispettata quasi sempre in b1/b2 e spesso NO in b3.
  - Riparazione di classe (una volta sola, per gli storici): template
    battuta-3 = "DATA: <data evento di convergenza o 'stato al
    2026-08-23'> PROCESSO: <landing/audit/ratifica> VERDETTO: classe
    finale" — la forma CH8 6.2 b3 ("nessun evento di chiusura ancora,
    stato al 2026-08-23") è il precedente conforme per gli aperti.
- Guardia 10 (lineage solo dal ledger): CLEAN nelle §6 (nessun claim di
  lineage fuori §3-bis).
- Guardia 9/13 (novità query-bounded / CT-6): CLEAN nelle §6 (le battute
  rimandano alle forme bloccate; numeri altrui con commit/pagina).
- Lint 5 (battuta 2 = una delle tre forme con ancora): **6 HIT** =
  ST-C5-08 (CH4), ST-C5-10 (CH5), ST-C5-12 (CH6), ST-C5-14 (CH7),
  ST-C5-16 (CH8), ST-C5-23 (CH10, conservativo) — tutti etichette, mai
  evidenza mancante.

==============================================================================
## VERDETTO COMPLESSIVO (C5, W-C.b)

**LE STORIE REGGONO-CON-RIPARAZIONI. 0 BREAK su 10 capitoli.** La
sostanza storica è FEDELE ai carrier: 30/30 commit citati esistono
(12/12 della lista C3 + 18 aggiuntivi), con UN solo mismatch di data
(32459ca — ST-C5-07, causa nominata: collisione di etichetta "C4");
tutti i verbatim aperti (phaseB alle righe :22/:66/:117-118/:159/:315/
:325/:330-335/:336-338/:339-344/:345/:347-350/:397-399; VERDICT_r22f
:508-521/:90-97/:106-122; escalation :542-553; hypaudit :15-19/:381-385/
:459/:482; census :11-13/:329+; M0 e D6 ai siti citati) REGGONO ALLA
RIGA. **Nessun (a) indebito**: tutti i rami (a) aperti coprono davvero
l'argomento rivendicato (le seconde prove di Fase A/B/D non sono
gonfiate). L'inflazione sta invece nella famiglia **(b)**: 5 etichette
"(b) STANCE-DI-FORK" senza verdetto per-riga Fase B (+1 "(a)-IN-PANEL"
fuori taxonomy) — mai con evidenza mancante, sempre con doppia prova
reale sotto l'etichetta sbagliata.

Conteggi per classe: **0 BREAK · 8 REPAIR** (1 ALTA: data 32459ca;
6 MEDIE: 2 attribuzioni/sovra-dichiarazioni [ST-C5-11 finder E-K 2004,
ST-C5-13 F-4 sovra-dichiarata], 4 taxonomy [ST-C5-08/-10/-12/-16];
1 BASSA [ST-C5-14]) **· 4 GAP** guardia-15 (ST-C5-02/-03/-09 MEDIE,
ST-C5-06/-15 BASSE — contati 4 raggruppati per capitolo) **· 12 NOTE**
(ST-C5-01/-04/-05/-17/-18/-19/-20/-21/-22/-23/-24 + quote stage-A).

Guardia 15: B8b 0 HIT / B8a 19 HIT (18 campi mancanti concentrati nelle
battute 3 + 1 data errata); riparazione di classe proposta (template
battuta-3). 12 righe SILENT: CLEAN (solo CH4 testata, (c) per
definizione, lista esatta). §7(c): 10/10 assi pertinenti, 15/15 id
campione esistono. F-1/F-2/F-3 degli inventari CONFERMATI come buchi
onesti; F-4 da riformulare (la doppia prova esiste: REFUTE_CH7 #5).

Scope del brief COMPLETO; scope CRESCIUTO dichiarato: (i) verifica dei
18 commit extra-lista (le battute 1 li citavano: il cammino
ancora-per-ancora li impone); (ii) collisione "C4" nuova, mintata qui.
Le riparazioni alle §6 NON sono state eseguite (file occupati): tabella
DISPOSIZIONE per capitolo, owner = storici B8a/B8b + orchestratore per
gli inventari.

