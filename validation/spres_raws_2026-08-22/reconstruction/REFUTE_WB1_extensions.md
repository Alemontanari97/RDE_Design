# REFUTE_WB1_extensions — refutazione avversaria delle sezioni nuove W-B.1 (CH1–CH8)

Slot C3 (refuter, giudizio), onda W-C.a, S-PRES sessione 2, 2026-08-23.
**Oggetto**: SOLO le sezioni nuove di W-B.1 negli 8 capitoli estesi
(perimetro dal brief d'onda); le sezioni pre-esistenti restano sotto
REFUTE_CH1–8; **le §6 STORIA sono ESCLUSE** (in scrittura, C5 dopo).
**Metodo**: 100% delle righe load-bearing delle sezioni nuove aperte
contro le ancore citate (read-then-verify); query NOT-FOUND ri-eseguite
in finestra (comandi citati per blocco); §3-bis verificati riga-per-riga
contro `LINEAGE_LEDGER.md`; card contro la guardia 14 (6 campi + GV-2);
guardie = `GUARD_CHECKLIST.md` (17), conteggio HIT/CLEAN per capitolo.
**Numerazione finding**: WB1-C3-nn (globale sul file). Classi:
BREAK / REPAIR / DOWNGRADE / GAP / NOTE, con severità (ALTA/MEDIA/BASSA).
Scrittura incrementale: un blocco per capitolo appena chiuso.

---

## CH1 — Formulation ladder (sezioni nuove: §1.2-EAP [B3-EAP], §1.7 riga H [B3-H], §3-bis [B3-LIN], §7 [B3-P7]; DECK FEED)

### Verifiche eseguite (ancore aperte in finestra)

- M0:2516-2552 (Remark EAP verbatim: "expand-then-average", O1 mass-flux,
  "area average = time average"/T0(i), "UNSTATED and UNPRICED",
  "CONTAINS and COMPLETES"): TUTTE le citazioni di §1.2-EAP reggono alla
  riga, ancore corrette (2526-2534 / 2537-2539 / 2543-2544).
- M0:3005-3045 (Parte V): verbatim :3010 regge; righe tabella :3013
  (bridge CONJECTURE-with-falsifier) / :3014 (PRACTICE, "space-time
  tracking 3-D absent") / :3015 (SCHEMA/PRACTICE) / :3016 ([S-GBE]
  RESOLVED 2026-08-06, no-Birkhoff, Jensen-looser) reggono. H-ii
  (:3017-3026) regge; VI.4bis(v) M0:3162-3166 (flatness monitor
  obbligatorio) regge. H-v [S-BLITE] M0:3027-3044: verbatim :3037-3038
  regge, brick G12-L1-3D regge, certificato (M-a') regge.
- claims_registry.yaml:1843-1864: S-GBE = SCHEMA, ipotesi E1-E5
  dichiarate (conferma della dicitura "E1–E5" della riga caotica, che M0
  :3016 da solo non nomina); X-GBE PASS di record 2026-08-06 (:1856-1860).
- `docs/rde_nozzle_GB_ergodic.md` esiste; E1/E2 presenti (:50, :55).
- litmap:19/:23/:24 (G1/G5/G6) e :141-142 (K-O validity footnote,
  unpriced) verificate alla riga.
- M0:2316-2350: LL-16 Efremov-Kraiko (Eq. 1.7 p.624 page-verified,
  collasso per ammissione autori Summary p.631) e forma bloccata D-06
  verificate.
- choice_ledger.yaml:164-174 (C1): incumbent/alternative/status MIXED/
  adjudicated-split WAVE-2/tre falsificatori di migrazione/primo
  ri-pinnato chart innocent-data + conversion-map/rigetto D6 S20
  intatto/prior Masters con transfer scope: la card §7 è FEDELE al ledger.
- literature_registry.yaml: id `kraiko_osipov_1970` (:102),
  `stechmann_2019` (:318), `efremov_kraiko_2004_augmentor` (:543),
  `masters_etal_2017` (:1023), `lauer_ansell_2025_pas` (:1031) esistono.
- §3-bis vs LINEAGE_LEDGER: LL-1/LL-3/LL-11/LL-4/LL-16 fedeli alle righe
  ledger (contenuto e residui); N-H = NOT-FOUND(q) coerente con la
  scansione integrale del ledger (nessuna riga LL-1..35 copre una ladder
  di licenza per classe di flusso; l'analogo più vicino LL-35/P34 è
  sull'asse evidence-tier, non licensing).
- **Ri-esecuzione query H-iii (attenzione (v))**, comandi in finestra:
  `grep -inE 'validity|applicab|regime.*valid|assumption.*declar'
  docs/rde_nozzle_literature_map.md` → 3 hit (:142, :613, :642) =
  IDENTICO al dichiarato; `grep -inE
  'validity|applicab|unstated|undeclared' docs/literature_registry.yaml`
  → hit su righe seed-validity (f2-c20/c21) **PIÙ UN HIT NON DICHIARATO**
  a :410 (`rao_beck_booth_1999`, "optimum ON the validity boundary" —
  scuola classica, né seed-validity né P-A..P-D). Zero hit su
  P-A..P-D CONFERMATO → l'ESITO NOT-FOUND(q) sopravvive.

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-01 | NOTE (BASSA) | CH1_formulation_ladder.md:283-285 | H-iii, descrizione grep-2: "hit solo su righe del NOSTRO seed-validity program, zero sulle righe P-A..P-D" | Riesecuzione in finestra: il grep colpisce ANCHE literature_registry.yaml:410 (`rao_beck_booth_1999`, riga scuola classica, non seed-validity). La metà load-bearing ("zero su P-A..P-D") regge; la descrizione dell'insieme degli hit è infedele alla riesecuzione. Riparazione: "hit solo su righe non-RDE (seed-validity nostro + rao_beck_booth_1999 classica), zero su P-A..P-D". |
| WB1-C3-02 | NOTE (BASSA) | CH1_formulation_ladder.md:255 | Riga caotica: "carrier X-GBE PASS (`docs/claims_registry.yaml:1843-1854`)" | :1843-1854 copre il blocco S-GBE (SCHEMA, ipotesi E1-E5); il PASS del carrier vive a :1856-1860 (blocco X-GBE, "PASS of record 2026-08-06"). Contenuto vero, ancora da estendere a :1843-1864. |
| WB1-C3-03 | NOTE (BASSA) | CH1_formulation_ladder.md:660-663 | §7(b): "nel corpus letto NESSUNA riga porta la parametrizzazione DENTRO un problema di forma mediato a misura pinnata — claim di assenza query-bounded al corpus" | Lint 7 SODDISFATTO (cita LL-28/LL-29; join ledger: righe con N-20 = LL-27/28/29, nessuna con misura pinnata — verificato sul ledger integrale). MA "query-bounded" senza query citata/rieseguibile: la base reale è il JOIN sul ledger (matrice 20×82, celle rese). Riparazione lessicale: "ledger-bounded (LL-27/28/29, matrice W-B.0)" o query esplicita. |
| WB1-C3-04 | GAP (MEDIA) | CH1_formulation_ladder.md:243-271 (§1.7 intero) | §1.7 è CONSUMATORE DICHIARATO della guardia 17 (pin utente 2026-08-23, "consumatori: … CH1 §1.7 …") ma il contenuto del pin non è consumato | La tabella di licenza (riga single/k-wave) e i canali residui NON portano il canale patch-subsoniche/choking: la condizione di decoupling (pre-gola convergente + gola tutta sonica/supersonica lungo ciclo/azimut) e le patch subsoniche come canali di risalita (case-class D1 4.3bis O1-O4) non compaiono in §1.7; il consumo è solo INDIRETTO via H-ii(4) "mixed-interface decision tree (O1-O4)". Nessun claim di decoupling senza choking è ASSERITO (quindi la clausola di divieto non è violata), ma il consumo assegnato manca. Riparazione: una cella canale-residuo "patch subsoniche fuori L4 = case-class O1-O4, canali di feedback (guardia 17)" nella riga 1 + un rigo in H-ii. |

Nessun BREAK, nessun REPAIR sostanziale: le sezioni nuove di CH1 sono
ancorate con fedeltà alta (tutti i verbatim aperti reggono alla riga).

### Tabella DISPOSIZIONE (V-N2 — proposta del refuter, owner riparatore W-C/W-D)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-01 | NOTE (BASSA) | Correggere la frase descrittiva del grep-2 in H-iii (esito invariato) |
| WB1-C3-02 | NOTE (BASSA) | Estendere l'ancora a claims:1843-1864 |
| WB1-C3-03 | NOTE (BASSA) | Sostituire "query-bounded al corpus" con "ledger-bounded (join LL-27/28/29)" o citare la query |
| WB1-C3-04 | GAP (MEDIA) | Aggiungere il canale guardia-17 (patch subsoniche/choking, O1-O4) alla riga single/k-wave della tabella §1.7 + rigo H-ii |

### Q&A SEED (dal materiale nuovo CH1)

1. **D**: "EAP è già il vostro funzionale: cosa aggiungete a
   Kaemming-Paxson?" → **R**: EAP è la coordinata di pressione di
   J_ideal con le ipotesi D1+D2 unstated/unpriced; il correttore P4 è la
   sua barra d'errore mancante — la formalizzazione CONTIENE e COMPLETA
   la dottrina EAP. → **Ancora**: M0:2526-2544 ([IO], NTRS 20180006890).
   → **Backup**: slide remark EAP + delta list (1)-(3) di M0:2535-2544.
2. **D**: "Il vostro metodo vale per RDE reali multimodali/caotici?" →
   **R**: la licenza segue il flusso: tabella per classe con classe di
   rigore per riga e RIFIUTO ONESTO dei certificati sul caotico +
   ceiling [S-GBE] provato sotto E1-E5. → **Ancora**: M0:3008-3016;
   claims:1843-1864. → **Backup**: tabella §1.7 con colonna canali
   residui (guardia 16 già in forma).
3. **D**: "Chi altro dichiara il regime di validità della media?" →
   **R**: NOT-FOUND(q) sul perimetro chiuso (registry 174 + litmap +
   P-A..P-D); unica adiacenza K-O 1970, footnote dichiarata ma unpriced.
   → **Ancora**: CH1 §1.7 H-iii (grep rieseguito, esito confermato);
   litmap:141-142. → **Backup**: slide query+perimetro+esito (forma
   NOT-FOUND(q), guardia 5/9).
4. **D**: "Perché la vostra base spline e non CST/B-spline?" → **R**:
   card C1: incumbent verdict-bearing, direzione convergiuta = chart
   B-spline dello STESSO spazio certificato; certificati sullo spazio,
   non sul chart; prior dof 28-72 con transfer scope dichiarato. →
   **Ancora**: choice_ledger.yaml:164-174. → **Backup**: card 6-campi §7.

### Guardie (CH1, sezioni nuove): 16 CLEAN / 1 HIT

1 CLEAN · 2 CLEAN · 3 CLEAN · 4 CLEAN (H-iii istanzia NUAA/Purdue/
NASA-Glenn-AFRL/`jourdaine_2019`) · 5 CLEAN (card §7 con assi §C-7/§C-3)
· 6 CLEAN (nessun claim di adequacy nelle sezioni nuove) · 7 CLEAN
(nessun claim engine-level nelle sezioni nuove) · 8 CLEAN (n/a) ·
9 CLEAN (novità solo NOT-FOUND(q) bounded) · 10 CLEAN (§3-bis joina su
LL-id esistenti, fedeli al ledger) · 11 CLEAN (§1.1 pre-esistente porta
la forma m_n; nessuna violazione nelle sezioni nuove) · 12 CLEAN (n/a)
· 13 CLEAN (numeri altrui con CT-6 nel feed 9) · 14 CLEAN (card C1 6/6,
campo 4 "ATTUALE(registry 174 + corpus wave-2, 2026-08-23)" non vacuo,
GV-2 ok) · 15 CLEAN (n/a qui; §6 esclusa) · 16 CLEAN (tabella §1.7 con
colonna canali residui per riga) · **17 HIT** (consumo assegnato
mancante in §1.7 = WB1-C3-04; nessun claim di decoupling non-choked
asserito).

### DECK FEED (CH1): 10/10 verificati

Feed 5 (EAP) / 6 (licensing) / 7 (NOT-FOUND validità) / 8 (B-lite) =
sezioni nuove: ancore e classi REGGONO (feed 7 eredita la correzione
WB1-C3-01 solo nella prosa H-iii, non nel testo del feed — feed OK).
Feed 1-4, 9, 10 (materiale pre-esistente già refutato): ancore
spot-verificate in finestra (litmap:23, M0:2316-2319, M0:2320-2350),
nessun mismatch; classi dichiarate conformi alle righe registry.

### FUORI-PERIMETRO (CH1)

- findings_registry.yaml:1455 code-anchor STALE: già dichiarato dal
  capitolo stesso (§3.1) come manutenzione fuori scope S-PRES — noto,
  non ri-mintato.
- §6 STORIA: placeholder, esclusa per brief (C5).

### VERDETTO CH1 (sezioni nuove): **REGGE-CON-NOTE** (0 BREAK, 0 REPAIR, 1 GAP media, 3 NOTE)

---

## CH2 — Averaged optimality (sezioni nuove: §3-bis N-C [W-B.1/B7], §7 C56 [W-B.1/B7]; DECK FEED)

### Verifiche eseguite (ancore aperte in finestra)

- literature_registry.yaml: TUTTI gli id di §7(a) esistono alle righe
  citate (`lozano_2018`:162, `lozano_2019`:170, `hoffman_1967`:372,
  `giles_pierce_2001`:507, `giles_pierce_2000`:516, `rubino_2018`:579,
  `wanted_hicken_zingg_2014`:920, `giles_pierce_1997`:989). Contenuti
  verificati alla riga: lozano_2018 log-singularity gola sonica ✓;
  lozano_2019 "locus CORRECTED of record: wall/trailing-edge-driven,
  NOT the shock" verbatim ✓; GP2001 analytic 4 regimi ✓.
- choice_ledger.yaml:760-771 (C56): la card §7 è FEDELE alla riga —
  status MIXED, tre ruoli CLOSED, F11d = residuo misurato che riapre
  C56 (non C11), HZ Def. 1 JCP 256 p.164 + caveat primale≠duale citato
  per pagina, Fidkowski-Darmofal 2011 p.676, blind-spot wrong-branch
  fino a C20 Tier-0: tutto presente nella nota ledger.
- D6 (development_plan):753-775: verdetto G0 verificato — JAX primary,
  spikes 52/52 + O3.1 machine precision, X-G0/X-G0AX a :762-763 ✓.
- File di processo citati nella card ESISTONO
  (VERDICT_C9C11_supplement.md, PANEL_C31TRIO.md, PANEL_C1REP.md in
  validation/sfoundations_raws_2026-08-13/blocco3/).
- §3-bis vs LINEAGE_LEDGER + matrici sorgente: LL-7 (part1:348-361 ✓
  p.676 morte biiezione), LL-16 (part2:117-127 ✓ Eq. 1.7 page-verified),
  LL-17 (part2:164-175 ✓ manca per-phase/parete/contouring), LL-19
  (part2:80-90 ✓ R11 + findings :2117), LL-1 (part1:59-75 ✓) — contenuti
  fedeli alle parti sorgente; M0:2908-2926 verificato alla riga
  ("the 1970 ancestor of (b), of the weighted structure of (c)",
  mandatory citation ✓).

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-05 | NOTE (BASSA) | CH2_averaged_optimality.md:298-299 | §3-bis LL-1: "componenti 2/3/4/11" | Il ledger stampa LL-1 = (1/2/3/4/11): la componente (1) è OMESSA. Non è pedanteria vuota: la (1) esiste nel ledger come istanza DEGENERE (collasso alla famiglia classica, matrix part1:60-62) ed è materia di C6. Riparazione: lista piena, o qualificare "componenti rilevanti al nodo N-C: 2/3/4/11 (la (1) è degenere, part1:60-62)". |
| WB1-C3-06 | NOTE (BASSA) | CH2_averaged_optimality.md:334 | §3-bis LL-19: ancora "LINEAGE_LEDGER.md:134-135" per il residuo R11 | STALE alla riesecuzione: R11 vive ora a LINEAGE_LEDGER.md:139-140 ("Righe con residuo aperto nominato: … LL-19 (forma pesi R11)"). Causa nominata: la riformulazione LL-20 (VERIFY_PB_corner_pb, ledger mtime 08:43 > CH2 mtime 08:34) ha spostato le righe. Contenuto fedele, ancora da ri-puntare. |
| WB1-C3-07 | NOTE (BASSA) | CH2_averaged_optimality.md:612-613 | DECK FEED 4: ancora "M0:2826-2934" | Range di ~108 righe che ingloba materiale estraneo (T7(c), boxed warning, twin warning, K-O precedent). Le ancore giuste sono puntuali: M0:2826 (first integral) + M0:2930-2934 ([T-P3] classe). Un feed è il join dello storyboard: l'ancora larga degrada il retro-audit del deck. |

Nessun BREAK/REPAIR/GAP: card C56 e §3-bis N-C reggono alla riga con
fedeltà alta; il doppio registro continuo/discreto di §7(a) è
esattamente la riga C56 del ledger (nessuna sovra-vendita del continuo).

### Tabella DISPOSIZIONE (V-N2)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-05 | NOTE (BASSA) | Ripristinare la lista componenti piena di LL-1 o qualificare l'omissione |
| WB1-C3-06 | NOTE (BASSA) | Ri-puntare l'ancora a LINEAGE_LEDGER.md:139-140 (post-riformulazione LL-20) |
| WB1-C3-07 | NOTE (BASSA) | Sostituire con ancora composita M0:2826 + M0:2930-2934 |

### Q&A SEED (dal materiale nuovo CH2)

1. **D**: "Rubino 2018 ha già l'adjoint period-averaged
   duality-preserving: perché non basta?" → **R**: LL-17 è il gemello di
   macchina più vicino MA senza riduzione per-fase, senza condizioni di
   parete Rao-type, senza contouring d'ugello (turbomacchine RANS). →
   **Ancora**: LINEAGE_LEDGER LL-17; matrix part2:164-175; registry
   :579. → **Backup**: tabella antenato→manca del §3-bis N-C.
2. **D**: "Perché adjoint discreto AD e non il continuo classico?" →
   **R**: per-RUOLO (card C56): gradient = discrete AD (esatto per la
   discretizzazione, O3.1 a machine precision); il continuo è frame +
   referee (f2 = −lambda2 in forma chiusa); dual-consistency = criterio
   referee F11d (HZ Def. 1, caveat citato per pagina). → **Ancora**:
   choice_ledger:760-771; D6:753-775. → **Backup**: card C56 6-campi.
3. **D**: "Il funzionale pesato J=Σw_iF_i esiste già (Giles-Pierce
   multipoint)?" → **R**: sì come antenato discreto-ensemble, MA pesi e
   forma della somma MAI stampati nel paper — la J-somma è inferenza
   nostra, residuo R11 DICHIARATO e bounded. → **Ancora**: LL-19; matrix
   part2:80-84; findings :2117. → **Backup**: riga R11 del ledger.

### Guardie (CH2, sezioni nuove): 17 CLEAN / 0 HIT

1 CLEAN (nessuna enunciazione di gerarchia gap) · 2 CLEAN (feed 3
dichiara il rango T1c: "rejector all'oracolo senza contouring, solo
eps" — esattamente la forma C-2) · 3 CLEAN (naming rung conforme nel
feed 3) · 4 CLEAN (banche istanziate con id) · 5 CLEAN (§7(c) assi
§C-3+§C-2 citati con classe e divergenza dichiarata) · 6 CLEAN ·
7 CLEAN (claim O3.1 con carrier X-G0/X-G0AX dichiarato) · 8 CLEAN (n/a)
· 9 CLEAN (novità CONCESSA/query-bounded, litmap:451-456) · 10 CLEAN
(tutti i claim lineage su LL-id esistenti) · 11 CLEAN (n/a) · 12 CLEAN
(n/a) · 13 CLEAN (numeri di terzi con pagina: HZ p.164, F-D p.676) ·
14 CLEAN (card C56 6/6; campo 4 "ATTUALE(perimetro…; data-check
2026-08-23)" + finestra ri-sweep nominata — GV-2 ok) · 15 CLEAN (§6
esclusa) · 16 CLEAN (n/a: nessun claim di soppressione) · 17 CLEAN
(CH2 non è consumatore assegnato; nessun claim di decoupling).

### DECK FEED (CH2): 8/8 verificati

Feed 1-3, 7-8: ancore spot-verificate, classi conformi; feed 3 porta il
rango dichiarato (guardie 2/3 CLEAN). Feed 4: HIT anchor-width
(WB1-C3-07). Feed 5-6 (sezioni nuove): ancore verificate alla riga
(C56/G0/M0:2908-2926), classi conformi.

### FUORI-PERIMETRO (CH2)

- OPEN §3.8 (stale anchor M0:2891 su o33_bench.py:292): finding
  candidato di retro-audit CONTRO M0 già dichiarato dal capitolo —
  corretto non ri-mintarlo qui.
- §6 STORIA: riservata W-B.2, esclusa.

### VERDETTO CH2 (sezioni nuove): **REGGE-CON-NOTE** (0 BREAK, 0 GAP, 3 NOTE)

---

## CH3 — Reduction physics (sezioni nuove: §1.2 [B3-BLITE], §1.3(i) box M-i [B3-MI], §1.3(iv) caveat [B3-C12], §3.12 G3/G4 [B3-G34], §3-bis N-D/N-M, §7-DWR; DECK FEED 7-10)

### Verifiche eseguite (ancore aperte in finestra)

- M0:3131-3150 (VI.4bis header + (ii)): [B3-MI] FEDELE alla riga —
  "BOTH routes live in the pipeline … engaged WHEN T0 applies
  (certified single/k-wave mode). The cheap route is a licensed
  specialization, not a replacement" verbatim ✓; l'emendamento utente
  ("EXPLOITED AT RUNTIME when certified, never assumed structurally")
  vive nell'header :3132-3137.
- M0:4214-4222: [B3-C12] band-underinclusion verificato — caveat
  DICHIARATO in M0, bound grezzo ~6e4 vs surplus +2.0407e5 (=29.4%,
  la dicitura "~30% del datum" regge).
- M0:2018-2026 (H-G6, L_H) + M0:1946-1956 (tre deriver in ordine,
  "NO closed-form gradient bound is derivable at current record"
  verbatim) ✓; M0:3027-3044 [S-BLITE] già verificato in CH1 (verbatim
  :3037-3038, brick G12-L1-3D) — il cross-ref [B3-BLITE] porta il
  brick e la condizionalità SCHEMA, come deve.
- D6:269-275 e :781-790: G3 "currently the only gate whose kill
  threshold cannot reject" verbatim :784-786 ✓; G4 :787 verbatim
  ("D2 error dominates → wave-frame objective", nessuna soglia/STATUS
  nella riga — supporta "nessuna soglia di record") ✓; F5b "G3
  unsteadiness trigger derived as a NUMBER BEFORE the corrector"
  :271-272 ✓.
- choice_ledger.yaml:269-280 (C11, nota integrale): "DWR = target
  primary … Richardson/GCI = permanent referee … weight of record =
  DISCRETE AD-adjoint" — la frase §7-DWR "il DWR è ADOTTATO davvero"
  e la spartizione per asse sono FEDELI alla riga.
- literature_registry.yaml: `zahr_persson_2016`:588,
  `li_xu_lv_lv_song_2023`:683, `li_xu_lv_yu_zhou_2025`:690,
  `wanted_becker_rannacher_2001`:862, `wanted_fidkowski_darmofal_2011`
  :876, `venditti_darmofal_2000`:999 — tutti esistenti.
- §3-bis vs LINEAGE_LEDGER: LL-22 fedele (terza+quarta istanza; μ unica
  pinnata T-O2); LL-4 fedele (P4 = EAP's missing error bar,
  M0:2537-2539 verificata in CH1); LL-17/LL-18 fedeli con decisione di
  scoping no-dup vs CH2/N-C DICHIARATA (buona pratica anti-duplicazione,
  asse corrector vs asse ottimalità).

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-08 | NOTE (BASSA) | CH3_reduction_physics.md:740-743 | Card corrector, campo 3: "gate DATA-DRIVEN (mai assunzione strutturale — emendamento utente di VI.4bis)" senza ancora di riga | La frase verbatim "Data-driven selection, never a structural assumption" vive nell'item (i) di VI.4bis (M0:3143-3144, quadratura), NON nell'item (ii) del corrector; il supporto vero del campo 3 è l'HEADER emendato di VI.4bis (M0:3131-3137, "EXPLOITED AT RUNTIME when certified, never assumed structurally"). Sostanza corretta, ancora da puntare a :3131-3137 per il retro-audit (le card sono join dello storyboard). |

Nessun altro finding: le quattro sezioni nuove tecniche ([B3-BLITE]/
[B3-MI]/[B3-C12]/[B3-G34]) reggono verbatim alla riga; le due card sono
fedeli al ledger/piano; il §7-DWR non sovra-vende (la spartizione per
asse è esattamente la riga C11).

### Tabella DISPOSIZIONE (V-N2)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-08 | NOTE (BASSA) | Aggiungere l'ancora M0:3131-3137 al campo 3 della card corrector |

### Q&A SEED (dal materiale nuovo CH3)

1. **D**: "Il vostro correttore è un solve instazionario mascherato?" →
   **R**: no — è la derivata dello sweep steady rispetto alla fase (one
   linearized solve) sull'ancora wave-frame, INGAGGIATO solo quando T0
   applica; la route generale unsteady O5 resta SEMPRE in pipeline:
   "a licensed specialization, not a replacement". → **Ancora**:
   M0:3145-3150 + header :3131-3137. → **Backup**: card corrector §7.
2. **D**: "Chi decide QUANDO l'unsteadiness vi uccide? Avete una
   soglia?" → **R**: no, e lo diciamo noi per primi: G3 è oggi l'unico
   gate il cui kill threshold non può rigettare; la chiusura è di piano
   (F5b: trigger derivato come NUMERO prima del corrector) e G4 è la
   valvola strutturale se il residuo di riduzione domina. → **Ancora**:
   D6:783-787; D6:271-273. → **Backup**: slide feed 7 + §3.12.
3. **D**: "Perché non un error estimator goal-oriented (DWR) per tutto
   l'errore?" → **R**: il DWR presuppone un duale computabile; per la
   riduzione il riferimento è il 3D-unsteady vero (delta/L_H underived,
   nessun referee esterno) — un DWR lì fingerebbe il duale che
   dichiariamo di non avere; dove il duale esiste (discretizzazione) il
   DWR è adottato davvero (C11: target primary + referee permanente). →
   **Ancora**: choice_ledger:269-280; M0:1953-1956; M0:1322-1333. →
   **Backup**: card forchetta-vs-DWR §7-DWR.
4. **D**: "Come misurerete il residuo senza pagare il 3D globale?" →
   **R**: B-lite: campo wave-frame ESATTO a costo di march su dominio
   nozzle-only con margine assiale certificato, adjoint verbatim (Lemma
   B) — il metro cheap del residuo rung-2; classe SCHEMA con brick
   G12-L1-3D da verificare per primo, dichiarato. → **Ancora**:
   M0:3027-3044. → **Backup**: feed 10 + CH1 H-v.

### Guardie (CH3, sezioni nuove): 17 CLEAN / 0 HIT

1 CLEAN (nessuna enunciazione della gerarchia C-3bis nelle sezioni
nuove) · 2 CLEAN · 3 CLEAN · 4 CLEAN (NUAA/P-B/P-C istanziati con id) ·
5 CLEAN (§7-DWR(c): assi §C-2 + §C-6 citati, divergenza dichiarata) ·
6 CLEAN ([B3-C12] rafforza la disciplina D-44: il caveat È parte del
numero; adequacy mai asserita) · 7 CLEAN · 8 CLEAN (ORCH-HARV-1 citato
come guardia in §1.5, pre-esistente) · 9 CLEAN · 10 CLEAN (§3-bis su
LL-22/LL-4/LL-17/LL-18 esistenti e fedeli) · 11 CLEAN · 12 CLEAN ·
13 CLEAN · 14 CLEAN (2 card 6/6; campi 4 "ATTUALE(…, 2026-08-23)" non
vacui, GV-2 ok; assenza di riga ledger DICHIARATA in campo 1) ·
15 CLEAN (§6 esclusa) · 16 CLEAN · 17 CLEAN (il box M-i non asserisce
decoupling; G4 = valvola di coupling nominata).

### DECK FEED (CH3): 10/10 verificati

Feed 7 (G3/G4) / 8 (corrector) / 9 (DWR per asse) / 10 (B-lite) =
sezioni nuove: ancore verificate alla riga, classi conformi (feed 7-8
= "aperto dichiarato di piano"/"direttiva di record", onesto). Feed 4
porta il band-underinclusion accanto al +0.51% (guardia 6 rafforzata).
Feed 1-6: materiale pre-esistente riparato W2, ancore spot-verificate,
nessun mismatch.

### FUORI-PERIMETRO (CH3)

- Il claim di assenza "operatore K mai esibito in forma chiusa"
  (§5.1, richiamato da §3-bis) è nella forma corpus-read (W2-R5, già
  aggiudicata dall'onda precedente), NON una NOT-FOUND(q) con grep
  rieseguibile: nessuna query da rieseguire per attenzione (v);
  segnalato all'orchestratore come classe-di-forma, non come finding
  nuovo (la forma fu accettata dal refuter pre-esistente).
- Off-by-one registry (:2026/:2147/:1925 → +1) dichiarato dal capitolo
  stesso in testa a §2: manutenzione, non ri-mintato.

### VERDETTO CH3 (sezioni nuove): **REGGE** (0 BREAK, 0 GAP, 1 NOTE)

---

## CH4 — Machine choices (sezioni nuove: §1.2-AnnexB, §1.4-suite, §1.6 velocità, §3-bis N-I, §7, §7-bis card, righe claim 17-18; DECK FEED)

### Verifiche eseguite (ancore aperte in finestra)

- **Commit verificati con `git show` in finestra**: `c9bacd9`
  (2026-08-21) — il messaggio conferma VERBATIM l'intera narrativa
  dell'incidente suite (23/23 PASS 234 s EXIT 0, (i)-(xxiii) incluso
  (vii) post-riparazione; "the close commit 7dea386 quoted '23/23'
  AHEAD of its verified evidence"; run intermedio 22/23, tail-4,
  classe R5, auto-colto, annotato nel log) — la riga claim 17 e §1.4
  sono FEDELI al carrier. `7dea386` contiene davvero "23/23".
  `07400a4` — verbatim "every lever = executable invariance gate +
  measured gain + adversarial diff-refuter"; 100.84→32.09 s, val_grad
  6.420→0.979 (6.6×, Q2/A-G RESOLVED), STOP-CHECK "~46 s vs <=30
  NOT-MET without M5c (counterfactual held)", i 2 difetti refuter
  (memo key `_mkey`; class nella ekey + CLASS-KEY REJECTOR) — riga
  claim 18 e §1.6 FEDELI. `32459ca` — ondemand tipizzato 46 carrier +
  STALENESS LINK + rejector "stale pass date" sparato in-sessione: ok.
- PROGRESS:119-129 (MET formali, catena 100.84→32.09→5.58, replay
  0.236, val_grad 0.449, Hessiana ≤8, STOP-WHEN-MET raffinato, M6
  rigettato dal suo gate) ok; :155-160 (GAP-29: NTF/2 flippa) ok;
  righe R3c:181, R7c:185, R13:191, R22:200, R33:211, R35:213 tutte ok.
- D6:1133 header "ANNEX B — Input taxonomy for the CFD-free design
  tool" ok; M0:4263 "input taxonomy (Annex B)" ok — il puntatore §1.2
  è esatto e la regola anti-duplicazione (ricostruzione in CH10) è
  dichiarata.
- literature_registry: TUTTI i 10 id di §7(a) esistono
  (browne:300/thakur:928/byrd:971/nocedal-wright:980/huang_zahr:1007/
  deuflhard:1039/yamamoto:1047/uno:1055/joss:1064/sun_nocedal:1072);
  status onesti confermati alla riga (sun_nocedal UNREAD con consumo
  deliberato al trigger [P-TRFLOOR]; thakur file journal 2025 su
  disco; yamamoto READ-PARTIAL).
- G0:199-210: "JULIA/ENZYME NOT BENCHMARKED … stated plainly" +
  scope X-GENOXC (unit process, NOT the profile-generation machinery)
  verbatim ok.
- choice_ledger: C31:481-493 ok (alternative incl. Uno e
  proximal-bundle D6:738), C58:783-793 ok (owner delta-sweep 9(e)),
  C49:682-692 ok, C24:408-416 ok DECIDED, C17:342 ok, C18:344-353 ok
  (SINGLE-AUTHOR, sweep eseguito, derivazione duty F2-live — la card
  C18 è onesta: "lo sweep è misura sull'incumbent, non un confronto").
- Card C31 campo 2: `DOSSIER_uno_fullread.md` ESISTE
  (sfoundations_raws blocco3); repo `Uno/` presente e git-ignored
  (quarantena verificata: git check-ignore positivo, non tracciato).
- §3-bis N-I vs LINEAGE_LEDGER: LL-30/LL-15/LL-31/LL-7/LL-12/LL-32/
  LL-33 tutti esistenti e FEDELI (incluso il claim LL-33 "giunzione
  non formalizzata dal campo" = testo della riga ledger, correttamente
  etichettato "claim di lineage, non NOT-FOUND"). La contro-lettura
  ("il nodo N-I NON rivendica novità dell'engine in sé") è la forma
  onesta giusta.

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-09 | REPAIR (MEDIA) | CH4_machine_choices.md:926-928 (§7(b)); eco in DECK FEED 8 (:1216-1221) | "Claim di assenza: query-bounded in CH5 (LM:354-362, sweep avversario 1971-2026 con 2 near-miss dichiarati)" | ANCORA CONFLATA. Riesecuzione in finestra: litmap:354-362 = "Gap verdicts (b2)" (C1-C4 NOT-FOUND(q) della linea Kraiko) e grep -in 'near.miss / 1971-2026 / ISABE-2003-117 / adversar' su docs/rde_nozzle_literature_map.md = **0 hit**: il litmap NON contiene lo sweep 1971-2026 né i near-miss. Lo sweep avversario con i 2 near-miss vive in `validation/ADVISORY_litmap_extension_2026-08-13.md` (verificato: ":17 … NOT found 1971-2026"). Il CONTENUTO del claim di assenza è vero sull'unione delle due fonti; l'attribuzione a un'unica ancora è falsa e un retro-audit del deck fallirebbe il walk su feed 8. Riparazione: citare entrambe le ancore (LM:354-362 per i gap verdicts b2; ADVISORY_litmap_extension_2026-08-13.md per lo sweep 1971-2026 + near-miss), o deferire integralmente alla riga di CH5 con la SUA ancora. |

Note non mintate: (a) card C55/C59, campo 5 = "—" con spiegazione
strutturale tra parentesi — accettato perché la domanda è dichiarata
VUOTA fino al trigger (guardia 14 GV-2 governa il campo 4, che è non
vacuo in tutte le 13 card); (b) la card C58 usa correttamente il flag
`STALE → finestra F2-entry` (esattamente il flag staleness che la
guardia 14 chiede).

### Tabella DISPOSIZIONE (V-N2)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-09 | REPAIR (MEDIA) | Doppia ancora (LM:354-362 + ADVISORY_litmap_extension_2026-08-13.md) in §7(b) e feed 8, o defer pulito alla riga CH5 con ancora propria |

### Q&A SEED (dal materiale nuovo CH4)

1. **D**: "Il vostro closing commit citava 23/23 prima dell'evidenza:
   come posso fidarmi degli altri conteggi?" → **R**: l'incidente è
   DICHIARATO nel record stesso (classe R5), colto dal ri-conteggio
   dell'orchestratore (disciplina SR-12: nessun conteggio ereditato); il
   claim sta col run verificato c9bacd9 come carrier — il sistema ha
   funzionato bocciando noi. → **Ancora**: commit c9bacd9 (messaggio
   integrale). → **Backup**: slide onestà (feed 6+7 accoppiati).
2. **D**: "5.58 s, 14.9 s: tuning ad hoc?" → **R**: no — ogni leva di
   velocità = gate di invarianza eseguibile (wall BITWISE) + guadagno
   misurato + diff-refuter avversario; i refuter hanno trovato 2 difetti
   veri, riparati a registro; lo STOP-CHECK ha detto NOT-MET quando lo
   era. → **Ancora**: commit 07400a4; PROGRESS:119-129. → **Backup**:
   card catena M-CHAIN + criterio pessimistic-end.
3. **D**: "Perché scipy e non IPOPT/Uno?" → **R**: card C31: incumbent
   su numeri di QUESTO problema, Uno = flip candidate con A/B pinnato a
   constraint-set identico e install O5-class; censimento DATATO
   2026-08-19/20, ri-esame al cluster F2-entry. → **Ancora**:
   choice_ledger:481-493; card §7-bis. → **Backup**: card C31 6-campi.
4. **D**: "Cosa entra nel vostro tool senza CFD?" → **R**: la tassonomia
   di record è Annex B di D6 (input taxonomy for the CFD-free design
   tool); la ricostruzione critica vive nel capitolo contratto (CH10) —
   puntatore, non duplicazione. → **Ancora**: D6:1133; M0:4263. →
   **Backup**: CH10 §1 (fuori mio perimetro, nota per C5/B2).

### Guardie (CH4, sezioni nuove): 16 CLEAN / 1 osservazione condizionale

1 CLEAN · 2 CLEAN · 3 CLEAN · 4 CLEAN (§7(b) istanzia PKU/NUAA/
KIT-Aoyama via CH5 P-A..P-D) · 5 CLEAN (§7(c): assi 3/5/2 citati con
divergenza dichiarata; "claim SOTA senza asse = lint 6" auto-imposto)
· 6 CLEAN · 7 CLEAN (ESEMPLARE: §1.4 dichiara stage V0 per TUTTI i
numeri engine, rider P34) · 8 CLEAN (nessun claim di ottimo globale;
C57 NEVER dichiarato in Q2) · 9 CLEAN (novità query-bounded via CH5 —
ma vedi WB1-C3-09 sull'ancora) · 10 CLEAN (§3-bis su LL-id esistenti
e fedeli) · 11 CLEAN (n/a) · 12 CLEAN (n/a) · 13 CLEAN · **14 CLEAN
CONDIZIONALE**: 13 card stampate (4 aggiudicate + 2 SA + 7 NEVER);
le 5 NEVER rimanenti (C51/C52/C53/C54/C61) sono DEFERITE per regola di
ownership dichiarata a CH8/CH10 — la copertura atlas-wide della
guardia 14 dipende da quei capitoli (verifica C51/C61 nel blocco CH8
sotto; C52/C53/C54 → CH10, FUORI dal mio perimetro: nota per
l'orchestratore) · 15 CLEAN (§6 esclusa dal mio perimetro) · 16 CLEAN
· 17 CLEAN.

### DECK FEED (CH4): 10/10 verificati, 1 HIT

Feed 1 (tally 12/36/12/2 = conteggio checkpoint ok), 2-3 (G0/S18 ok),
4 (velocità ok con caveat host dichiarato), 5 (NTF ok), 6 (incidente
suite FEDELE al commit), 7 (S-CERT ok, PROGRESS:211), 9 (Uno ok),
10 (C49/LL-12 ok). **Feed 8 = HIT WB1-C3-09** (ancora conflata; il
quote "no optimizer appears anywhere in the four papers" va verificato
contro CH5 SYN:58-61 — eseguito nel blocco CH5 sotto).

### FUORI-PERIMETRO (CH4)

- §6 STORIA (scritta da B8a con trittici T-1…): ESCLUSA per brief —
  la refutazione delle battute con data+processo+verdetto è di C5.
- Card C52/C53/C54 (ownership CH10): fuori perimetro W-C.a mio slot;
  l'orchestratore assegni la verifica al refuter di CH10.
- Riga di disposizione 12 (fix Q&A-bank non applicato, indirizzato a
  valle): scelta dichiarata e motivata dal riparatore — legittima.

### VERDETTO CH4 (sezioni nuove): **REGGE-CON-RIPARAZIONI** (0 BREAK, 1 REPAIR media, 0 GAP, 2 note non mintate)

---

## CH5 — Literature positioning (sezioni nuove: righe [WB1-R1..R9] in §1.1/§1.2/§1.6/§1.7, box nomenclatura [WB1-R3], §3-bis N-N, riformulazione P-B [WB1-R10], righe claim 20-23; DECK FEED)

### Verifiche eseguite (ancore aperte in finestra)

- **[WB1-R10] riformulazione P-B**: `VERIFY_PB_corner_pb.md` letto
  INTEGRALE — CH5 §1.1/§3-bis/Q2 sono FEDELI alla verifica alla fonte
  (p0/T0 time-averaged confermato; DUE corner Fig. 13 p. 8; Eq. 22 lip
  a p_inf ambiente; Eq. 26 base a p_b = media SPAZIALE, "averaged" =
  lessico plug steady, MAI cycle-averaging; Eq. 26 senza fonte E senza
  provenienza del valore; p_b anche in Eq. 18 termine +pi r_J^2 p_b).
  La riga LL-20 del LINEAGE_LEDGER è già la forma RIFORMULATA (mtime
  08:43) e CH5 §3-bis vi è conforme.
- SYN:31-39 (matrice 7 assi, "NO optimizer" P-A) e SYN:58-61: la frase
  C-5 "no optimizer appears anywhere in the four papers" è VERBATIM
  alla riga — questo chiude anche la verifica pendente del CH4 feed 8.
- **Ri-esecuzione grep [WB1-R6] (attenzione (v))**:
  `grep -ic 'spectral|FFT|mode purity'` sui 4 slot
  NOZZLE_RDE_STUDY_p{A,B,C,D} = **0/0/0/0 hit** — la metà negativa
  ("mai verificato spettralmente") CONFERMATA dalla riesecuzione;
  la metà positiva verificata alla riga (pC:253, 347 "clean
  single-mode periodicity at every station"; pB:396 "persistent
  single-mode rotating wave"; pA:257 "single-mode stable by
  construction"; pD:368-370 "their solver locks to ONE wave").
- [WB1-R4]: pB:405 ("the nozzle back-reacts on chamber p_0/T_0 with
  truncation"), pB:164 (F-13 [REP pp. 10-11 + Fig. 16]), pB:283 —
  tutte verbatim.
- [WB1-R5]: pC:187-195 (forza laterale 450-670 N vs 1500-1860 N
  [INFER], phi_L sawtooth 0-360), pC:269-275 ("cleanest published
  face" + "the K-bar = 0 phenomenology"), pC:301-303 ("near-zero
  implied mean") — l'aggiudicazione È dello slot come dichiarato,
  etichette [FIG]+[INFER] fedeli.
- [WB1-R7]: THH:398-402 (KP18-F6, M 0.85→1.33) e THH:415-421 (Table 1:
  Pt8/Pt3 4.07/0.67 → ~6:1; 237%; Tt 41%; M8x 48%) verbatim; THH:613
  (P-C combustore ~20:1) presente; CKP-S:206/:221 portano davvero il
  "10:1" del frame utente — il bracket 6:1-20:1 e la regola di slide
  sono corretti.
- [WB1-R2] eco EAP: M0:2526-2539 già verificata (CH1);
  EAP_i(axial) <= J_ideal(total) alla riga M0:2535-2537.
- [WB1-R9] eco N-H: coerente con la riesecuzione query di CH1 (blocco
  CH1 sopra, esito confermato).
- Humphreys/Veen (righe claim 16-17, feed 8): BPH:619-625 (×2.45,
  −13.26°→−3.08°, +0.26%, "priced at the design-gradient level") e
  BPH:605-610 (Eq. 5.1 = Veen Eq. 9, "failed to produce reliable
  results", "the inherited closure is the stack's bottom") verbatim.
- Guardia 4: TUTTI gli id dell'istanziazione C-7 esistono in registry
  (kaemming:236, paxson_miki:249, harroun_2021:273, liu:615,
  harroun_2020:633, jourdaine:697 + NUAA verificati in CH3).
- §3-bis N-N vs ledger: LL-3/LL-2/LL-4/LL-5/LL-20/LL-22 FEDELI
  (LL-2: peso/denominatore UNDECLARED pp. 670-671 + Eq. 10, duty (a)
  chiuso = verbatim ledger; LL-22 "terza+quarta istanza" verbatim);
  copertura lint 7 dei claim C1/C2/C3 completa (LL-20+LL-16+LL-1;
  LL-14+LL-12).

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-10 | REPAIR (MEDIA) | CH4_machine_choices.md:1216-1221 (feed 8) — aggiudicato QUI perché la casa del claim è CH5 | CH4 feed 8: "nessuno dei quattro paper coupled ha un optimizer nella catena ('no optimizer appears anywhere in the four papers')" SENZA il caveat P-B | CH5 (casa del claim) dichiara ESPLICITAMENTE la lettura obbligatoria: "Il deck NON deve dire 'nessuno ottimizza'" (Q2) e il feed 1 di CH5 porta la forma onesta ("P-B ottimizza lo steady mediato GLOBALE col variazionale classico; NESSUNO deriva condizioni di ottimalità per la famiglia") con caveat ISABE sulla stessa slide. Il feed 8 di CH4 usa la frase C-5 nuda: uno storyboard che joina CH4 senza CH5 produce la slide attaccabile ("P-B usa già il variazionale max-thrust!"). Un feed sbagliato = una slide sbagliata. Riparazione: riscrivere CH4 feed 8 nella forma CH5-feed-1, o aggiungere il rimando vincolante "forma di slide = CH5 feed 1". |
| WB1-C3-11 | NOTE (BASSA) | CH5_literature_positioning.md:135-138 (box nomenclatura) | "Namespace G, famiglie distinte: G0-G6 = gate del piano D6; la litmap ha numerazioni proprie (i gap-verdetti qui citati sono C1-C4...); G1-G12 = gap-list T0P (CH3); GRAFT-Gxx" | La famiglia più citata manca all'appello ESPLICITO: l'executive gap summary della litmap ha le PROPRIE G1-G12 (litmap:19-30), attivamente citate come "riga G5" (litmap:23) da CH1 feed 1 e dal §1.1 di questo stesso capitolo — la collisione G5-litmap ("average first, design second") vs G5-gate-del-piano (literature gate/passo umano Kraiko) vs G5-gap-T0P è esattamente il caso che il box esiste per disinnescare, e resta coperta solo dal generico "numerazioni proprie". Riparazione: una riga "litmap G1-G12 (executive gap summary, :19-30) = quarta famiglia; 'riga G5' litmap ≠ gate G5". |

### Tabella DISPOSIZIONE (V-N2)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-10 | REPAIR (MEDIA) | Riscrivere CH4 feed 8 nella forma CH5 feed 1 (o rimando vincolante); lo storyboard NON joini CH4 feed 8 as-is |
| WB1-C3-11 | NOTE (BASSA) | Aggiungere la famiglia litmap G1-G12 al box nomenclatura con l'esempio G5 |

### Q&A SEED (dal materiale nuovo CH5)

1. **D**: "P-B usa già il variazionale max-thrust Rao/Veen: la vostra
   novità?" → **R**: P-B lo applica a UN solo stato steady da p0/T0
   time-averaged, con corner a p_inf ambiente (Eq. 22) e p_b spaziale di
   base (Eq. 26, senza fonte né provenienza del valore); nessuno deriva
   condizioni di ottimalità per la FAMIGLIA mediata (C2 NOT-FOUND(q)). →
   **Ancora**: VERIFY_PB_corner_pb.md; SYN:33-34; LM:354-357. →
   **Backup**: slide riformulazione P-B + caveat ISABE.
2. **D**: "Su cosa poggia il vostro pin single-mode? Il campo lo
   verifica?" → **R**: il pin è ESIBITO in tutti e 4 i CFD del corpus
   (periodicità osservata, wave-locked) ma NESSUNO lo verifica
   spettralmente (grep rieseguito: 0 hit); noi lo dichiariamo MODEL
   HYPOTHESIS con monitor T0-flatness — scope distinto da R20
   (hardware). → **Ancora**: pC:253/347; pB:396; pA:257; pD:368-370. →
   **Backup**: riga claim 22 + CH6 §1.6.
3. **D**: "Quanto sono grandi le escursioni per-fase reali?" → **R**:
   bracket pubblicato ~6:1 in gola (KP18 Table 1, spread Pt 237%) fino a
   ~20:1 al combustore (P-C); il "10:1" del frame è dentro il bracket —
   numeri loro, CT-6. → **Ancora**: THH:415-421, 613; CKP-S:206/221. →
   **Backup**: slide KP18 Fig. 6 + Table 1.
4. **D**: "La forza laterale rotante non distrugge la vostra media?" →
   **R**: è la faccia PUBBLICATA della fenomenologia K-bar=0: contenuto
   per-fase O(10×) gli effetti percentuali medi, media implicita ~0 —
   esattamente ciò che il teorema K-bar=0 dice e che i canali (J)/(H)
   residui prezzano. → **Ancora**: pC:187-195, 269-275, 301-303
   ([FIG]+[INFER] dichiarati). → **Backup**: feed 3 + CH3 §1.2.

### Guardie (CH5, sezioni nuove): 16 CLEAN / 1 HIT

1 CLEAN (il box nomenclatura NOMINA lo swap gap(A)/(B)↔Gap A/B con
mappa dichiarata — verificato coerente col checkpoint C-3: "model
(= Gap A)" :204, gap(B)=pf-vs-3D=model ⇒ gap(B)~Gap A corretto) ·
2 CLEAN · 3 CLEAN · **4 CLEAN ESEMPLARE** ([WB1-R1]: istanziazione
C-7 con id verbatim tutti esistenti) · 5 CLEAN (§7(c): asse §C-1
PRISMA-class con divergenza dichiarata; §7(a) clausola di vacuità
[V2-R4] legittima) · 6 CLEAN (R26 sempre OPEN, mai adequacy) ·
7 CLEAN · **8 HIT parziale → vedi WB1-C3-10** (la guardia
best-of-sweep §1.8 in CH5 è CLEAN e ben marcata [INF]; l'HIT è sul
consumo CH4-feed-8 della frase C-5, aggiudicato qui) — sulle sezioni
nuove di CH5 stesso: CLEAN · 9 CLEAN (novità query-bounded con
concessioni e near-miss dichiarati) · 10 CLEAN (§3-bis fedele, LL-20
in forma riformulata) · 11 CLEAN · 12 CLEAN · 13 CLEAN (CT-6
dichiarata in testa e per-riga; [INFER]/[FIG] etichettati) ·
14 CLEAN (lint 8 vacuo DICHIARATO in §7(a): nessuna scelta presentata
qui, card altrove — legittimo) · 15 CLEAN (§6 STORIA presente ma
ESCLUSA dal mio perimetro per brief, C5) · 16 CLEAN · 17 CLEAN
([WB1-R4] Fig. 16 feedback ugello→camera presentato come minaccia
CT-1 con confine di classe — nessun claim di decoupling non-choked;
coerente col pin guardia 17).

### DECK FEED (CH5): 10/10 verificati

Tutti gli anchor dei 10 feed aperti in finestra: feed 1 (SYN:58-61
verbatim + forma onesta + caveat ISABE on-slide ✓ — LA forma di
riferimento per il claim, cfr. WB1-C3-10), feed 2 (SYN:97-102 ✓),
feed 3 (pC ✓), feed 4 (pB:405 ✓), feed 5 (grep rieseguito 0 hit ✓),
feed 6 (LM:299-320/354-357 ✓), feed 7 (M0:2526-2539 ✓), feed 8
(BPH ✓), feed 9 (THH ✓), feed 10 (H-iii confermata + SYN:490-492 ✓).
Classi conformi, CT-6 stampata dove servono numeri altrui.

### FUORI-PERIMETRO (CH5)

- §6 STORIA (trittici 6.1-6.6, W-B.2): esclusa per brief — nota
  all'orchestratore: le battute citano commit (b0a4c15, a85e355,
  ea2abce, b3da86d, 3b2b9e6, 904f950) che C5 dovrà verificare con
  git show.
- Righe pre-esistenti §1.4/§1.5/§1.8: già refutate (REFUTE_CH5) e
  riparate W2 — spot-check senza mismatch, non ri-refutate.

### VERDETTO CH5 (sezioni nuove): **REGGE-CON-RIPARAZIONI** (0 BREAK, 1 REPAIR media cross-capitolo, 0 GAP, 1 NOTE)

---

## CH6 — Value/honesty/roadmap (sezioni nuove: §1.2-bis N-Q [IL PEZZO CRITICO], §1.2 [WB1-R1], §1.4 [WB1-R3], §1.5 [WB1-R4/R5/R6], §1.6 [WB1-R7/R8], §3 A-9, §3-bis, §6-legenda, §8 card C61/C59; DECK FEED)

### Verifiche eseguite (ancore aperte in finestra)

- **§1.2-bis vs CKP-S :198-254 — confronto ALLA RIGA, quote per quote**
  (attenzione (i)): TUTTI i verbatim reggono ESATTI — frame three-design
  e i tre gap (:198-204 ✓), "declared hypothesis, not theorem"
  (:218-219 ✓), gap(A) Jensen/G(x;s)/10:1 (:219-222 ✓), i TRE teoremi
  di gap(B) (:222-225 ✓), "CONFINED to named channels" (:225-226 ✓),
  "PLAUSIBLY |x*_pf − x*_mean| > |x*_3D − x*_pf|" e "= the value
  condition at argmax level" (:228-230 ✓), DEATH SCENARIO integrale
  (:230-237 ✓ VERBATIM ESATTO), shadow x_s(xi)/NOT-seen (:238-244 ✓),
  "SMOOTH/advective part" (:245 ✓), tallone (J) (:246-247),
  Achilles/può dominare in-settore (:248-250 ✓), decisori (:209-214 ✓).
  La sostanza è FEDELE AL MASSIMO GRADO; tre citazioni numeriche sono
  off-by-one (finding 12 sotto).
- **Guardia 1 verificata su OGNI occorrenza della gerarchia**: §1.2-bis
  (ii) porta il tallone INLINE ("enunciato VALIDO SOLO insieme al
  tallone (J) del punto (iii), mai da solo"); riga claim 18 → rimando
  riga 19 inline; DECK FEED 2 porta il VINCOLO stampato ("va in slide
  SOLO insieme alla 3 — guardia 1, mai separate"); deck §5.7 "SEMPRE
  col tallone (J) sulla STESSA slide". NESSUNA enunciazione orfana:
  guardia 1 CLEAN.
- **Nota lettere-gap PRESENTE** (attenzione (i)): §1.2-bis(i) "Nota di
  mappa OBBLIGATORIA (collisione di lettere)" con mappa gap(A)~Gap B /
  gap(B)~Gap A — VERIFICATA CORRETTA contro il checkpoint (C-3 :201
  "model (= Gap A)"; gap(B)=pf-vs-3D=modello ⇒ gap(B)~Gap A ✓);
  ripetuta in §6-legenda e coerente col box CH5 [WB1-R3].
- **Guardia 16**: §1.2-bis(iii) enumera perimetro (parte smooth) E
  canali residui CIASCUNO con classe/stato ((J) SBV-conditional delta
  underived; (H) senza numero; swirl B1-B5 con B2~0 drop-variant;
  slip-sheets G9 con deriver F2) — ESEMPLARE, è l'istanza vincolata
  della regola come da guardia.
- **Ri-esecuzione query Q-iii (attenzione (v))**: pattern design-gap
  (`formulation gap|design gap|three-design|mean-designed vs|x*_mean`)
  su registry + litmap = **0 hit / 0 hit** (CONFERMATO); near-object
  sui 4 slot confermati alle righe (pB:175 "three-part TRANSIENT
  flow-loss decomposition" verbatim; pB:363 "stated but not separately
  quantified"; pA:259-261 "no decomposition offered"; pD:410
  bookkeeping F-7). NOT-FOUND(q) REGGE alla riesecuzione; STOP G-11
  dichiarato.
- D6:776-782 (G2 VALUE GATE verbatim + thrust-stand ~0.5-1% "Note
  only, no row") ✓; D6:228-233 (F3/F4b ORDER-INTERCHANGEABLE verbatim)
  ✓; D6:85-100 (P-2 freeze FIRED 2026-08-11, C1
  freeze-with-declared-conditional owner F2, fallback S19 two-knob) ✓;
  D6:1093+ (RK-A scoop Lozano-Ponsin) ✓; D6:214-216 (F3) e :275-278
  (F6) per la legenda ✓; M0:3524-3525 ("nesting and constrained-KKT
  structure are THEOREM (standard)") ✓ — lo scoping [WB1-R1] che la
  frase NON copre la strictness è corretto.
- choice_ledger C61:818-830 (NEVER, incumbent legacy-only, "N2 MUST
  REPLACE IT", trigger verbatim :829, Humphreys nota :830) e
  C59:795-805 (CANONICAL-INSIDE-THE-PIN, alternative live-only
  weakened-pin, trigger :804): le due card §8 sono FEDELI alla riga.
- findings:2145-2153 (R20 verbatim, owner F5) ✓; claims:2262
  (falsificatore argmax-shift verbatim) ✓; amendment v2.1 :352-355
  (G-10 twin/S-5F) ✓ — A-9 fedele.
- §3-bis vs ledger: LL-21/LL-22/LL-35 FEDELI (incluso il MINT-PENDING
  F-2 sull'identità di decomposizione, coerente con CKP-S C-4
  :255-260); N-Q = NOT-FOUND(q) con query eseguita e rieseguita ✓
  (lint 7 pieno).

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-12 | NOTE (MEDIA) | CH6_value_honesty_roadmap.md:136, 202-204, 210, 214-215, 1010 | Citazioni CKP-S off-by-one nel pezzo più guardato: header blocco ":198-255" (blocco reale = :198-254; :255 = header C-4); quote (J) citata ":247-248" (vive a :246-247); "G9 slip-line lift = F2 deriver" citato ":253" (vive a :252); regola deck "state the hierarchy WITH the (J) heel" citata ":254-255" DUE volte (§1.2-bis(iii) e feed 3; vive a :253-254) | Verificato con grep -n sul checkpoint (mtime 05:25 < CH6 08:41: nessun drift del file — errore del writer). I VERBATIM sono tutti fedeli; le ancore numeriche vanno ri-puntate o il retro-audit del deck fallisce il walk esattamente sulle righe della guardia 1. |
| WB1-C3-13 | NOTE (MEDIA) | CH6_value_honesty_roadmap.md:78-79 | Cross-ref "(CH1 Q4 [W2-R4], `CH1_formulation_ladder.md:362-374`)" per la forma riconciliata della strictness | Range SBAGLIATO: CH1:362-374 = §3.1 (riconciliazione owed/landed di [S-T0P] + nota stale-anchor findings) — la forma riconciliata di PB-2 (strictness senza prova scritta, ipotesi implicita mu({xi: l(xi)>L})>0 non enunciata) vive in CH1 Q4 a CH1:511-530 (testo verificato; la stringa è spezzata su :519-520). Il nome-sezione è giusto, il range no. |
| WB1-C3-14 | REPAIR (ALTA) | CH6_value_honesty_roadmap.md:997-998 (DECK FEED 1) + :695-696 (deck §5.7) | "x*_mean — il comparatore I4, con ZERO istanze computate NEL CAMPO" | ESTENSIONE DI SCOPE NON SUPPORTATA che rende il feed attaccabile. Il verbatim di record è "I4 comparator has ZERO computed instances" (CKP-S:198-199) — scope = il RECORD del programma (il comparatore del twin mai eseguito, coerente con PB-2/twin "never computed" :200-201). "Nel campo" flippa il significato in un claim FALSO-attaccabile: il campo computa design a stato medio di continuo (litmap riga G5 "average first, design second"; P-B computa un Rao/Veen su stato mediato — CH5 §1.1) — un referee ESA con P-B in mano smonta la slide. §1.2-bis(i) è corretto (quota verbatim senza estensione); sono il feed 1 e il deck 5.7 a introdurre "nel campo". Riparazione: "con ZERO istanze computate NEL RECORD (il comparatore del twin non è mai stato eseguito)" o verbatim inglese citato. |

### Tabella DISPOSIZIONE (V-N2)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-12 | NOTE (MEDIA) | Ri-puntare le 4 citazioni (:198-254; :246-247; :252; :253-254) in §1.2-bis e feed 3 |
| WB1-C3-13 | NOTE (MEDIA) | Correggere il cross-ref a CH1:511-530 (Q4) |
| WB1-C3-14 | REPAIR (ALTA) | Riscrivere feed 1 e deck 5.7: scope "nel record", mai "nel campo"; lo storyboard NON joini feed 1 as-is |

### Q&A SEED (dal materiale nuovo CH6)

1. **D**: "Quale gap domina — quello della vostra formulazione o quello
   del vostro modello?" → **R**: ipotesi di lavoro DICHIARATA (mai
   teorema): a vincoli e settore fissi (A)>(B) — il gap di formulazione
   non ha teoremi di soppressione (Jensen su G(x;s), escursioni 10:1),
   quello di modello ne ha tre sulla parte liscia — MA col tallone (J):
   se i salti di fronte sono grandi, (B) può dominare anche in-settore.
   → **Ancora**: CKP-S:215-254. → **Backup**: slide N-Q (feed 1-4
   INSIEME, vincolo guardia 1).
2. **D**: "E se il vostro design fosse vicino al mean-design E lontano
   dal 3D vero?" → **R**: è lo scenario di morte, e richiede DUE
   fallimenti indipendenti, ciascuno misurabile separatamente: (A) dal
   twin a vincoli identici (cheap, per primo), (B) da M-RED front legs +
   5F sign test; twin-first = kill-or-validate onesto, G2 = morte
   onesta codificata nel piano. → **Ancora**: CKP-S:230-237; D6:776-778.
   → **Backup**: feed 4 + feed 6.
3. **D**: "Chi altro separa questi gap?" → **R**: nessuno nel perimetro
   chiuso: NOT-FOUND(q) (registry 174 + litmap + P-A..P-D, rieseguita);
   i near-object sono decomposizioni di perdita di flusso, mai di gap
   di design. → **Ancora**: CH6 §1.2-bis Q-iii. → **Backup**: feed 5.
4. **D**: "Il vostro ottimo truncated-plug non sarà un artefatto della
   chiusura p_b?" → **R**: rischio REGISTRATO da noi a grado foundation
   (card C61 NEVER: la chiusura muove il DESIGN — Humphreys ×2.45); il
   computo PB-2 entrerà nel record CON la sensibilità alla chiusura
   dichiarata, o non entrerà. → **Ancora**: choice_ledger:818-830;
   M0:1455-1464. → **Backup**: card C61 §8.

### Guardie (CH6, sezioni nuove): 17 CLEAN / 0 HIT

**1 CLEAN — verificata occorrenza per occorrenza** (nessuna gerarchia
orfana; il vincolo è STAMPATO anche a livello feed) · 2 CLEAN · 3 CLEAN
· 4 CLEAN · 5 CLEAN (assi §C-2/§C-6; vacuità §7(a) dichiarata) ·
6 CLEAN (D-44 consumata attivamente: Q1 "bracket con provenienza,
either way") · 7 CLEAN (P34 rider §1.3 + feed 10) · 8 CLEAN (wording
guard §1.1 + Q3 nella forma M0:1335-1339) · 9 CLEAN (D-06 locked +
near-miss + query-bounded) · 10 CLEAN (LL-21/22/35 + N-Q NOT-FOUND(q))
· 11 CLEAN (n/a) · 12 CLEAN (n/a) · 13 CLEAN (Humphreys = numeri loro,
CT-6 dichiarato) · **14 CLEAN** (card C61 + C59 "non-aggiudicata,
finestra Y" 6/6, campo 4 ATTUALE(…, 2026-08-23) non vacuo — NOTA di
riconciliazione per l'orchestratore: CH4 §7-bis dichiarava l'ownership
della card p_b "CH8/CH10", ma la card C61 vive QUI (CH6 §8): la
copertura c'è, il puntatore CH4 è impreciso) · 15 CLEAN (STORIA 6-bis
esclusa dal mio perimetro) · **16 CLEAN — istanza esemplare** ·
17 CLEAN (n/a).

### DECK FEED (CH6): 10/10 verificati, 1 HIT

Feed 2+3 (gerarchia + tallone, vincolo di accoppiamento stampato ✓),
4 (death scenario verbatim ✓), 5 (query rieseguita ✓), 6 (G2 ✓),
7 (value condition indecidibile-dichiarata ✓ — onestà corretta),
8 (forma riconciliata PB-2 ✓), 9 (roadmap ✓ D6/PROGRESS), 10 (guardie
✓). **Feed 1 = HIT WB1-C3-14** ("nel campo"). Feed 3 eredita
WB1-C3-12 (ancora :254-255).

### FUORI-PERIMETRO (CH6)

- §6-bis STORIA (trittici 6-bis.1–6-bis.5): esclusa per brief — nota a
  C5: verificare i commit citati (904f950, 1a11f2c, ea2abce, fd2d444,
  da91aa4, d968502, 318d3fd) e la battuta 6-bis.2 che porta le TRE
  correzioni utente come stance-di-fork.
- La questione "~0.3M unità non dichiarata" (§1.5) è già trattata dal
  capitolo stesso ([W2-R8]: [INF] + divieto di slide) — corretta, non
  ri-mintata.

### VERDETTO CH6 (sezioni nuove): **REGGE-CON-RIPARAZIONI** (0 BREAK, 1 REPAIR alta su feed, 0 GAP, 2 NOTE medie di ancoraggio; §1.2-bis SOSTANZA fedele al massimo grado, guardie 1/16 esemplari)

---

## CH7 — Averaging edifice (sezioni nuove: §3-bis N-E [W-B.1/B7], §7 forma [V2-R6] con card C51; DECK FEED)

### Verifiche eseguite (ancore aperte in finestra)

- registry: `wintenberger_shepherd_2004`:261 ✓, `kraiko_tillyaeva_2015`
  :498 ✓, `wanted_tillyaeva_1975`:742-746 ✓ (status WANTED, paths [],
  russo [HARD], owner "Next lit window — N6-2 novelty bound; closest
  classical antecedent to our data class" VERBATIM — la disciplina
  no-summary-del-paper-assente di §7(a) è esattamente la riga),
  `wanted_fievisohn_2018_quasi2d_moc`:1280 ✓.
- D6:803-806: riga 2.2(f) VERBATIM ("swirling-flow control-surface
  contouring — Tillyaeva Izv. AN MZhG 1975 no. 3 full-text check
  against T-N6-2's free-vortex closure") ✓ — correttamente presentata
  come DUTY del gate G5, non confronto eseguito.
- DISPATCH_swirl5f.md:100-113: priorità C51 = decisione utente in
  standing queue (:100-101 ✓); annotazione utente [T-N6-2] VERBATIM
  ("THEOREM under UNIFORM (r*Gamma, h0, s) ONLY … the dossier must
  present the fork (mixed lemma … vs declared monitored-neglect …
  TRIPLE spread monitor) before any path-A adoption") ✓ — §7(a) item 3
  FEDELE alla riga.
- choice_ledger C51:706-714 ✓ (NEVER; incumbent implicit BVP
  freezing+Newton-Krylov; alternativa marching azimutale
  dal blind-PDE formalizer; "adjudication owed at implementation time"
  = il campo 3 della card è fedele al sequencing del giudice);
  `VERDICT_contract_and_L4R1.md` ESISTE su disco
  (validation/sfoundations_raws_2026-08-13/) ✓.
- Matrice lineage: part2:51+ (kraiko_tillyaeva_2015, P2.S-2:
  conjugate/moltiplicatori COMPLETO incl. parte subsonica) ✓;
  part2:443+ (colonna FIEVISOHN W-09, sweep-disco) ✓; part1:210+
  (wintenberger) ✓ — §3-bis FEDELE alle parti sorgente e al ledger
  (LL-14/LL-13/LL-9; i due SEED dichiarati CANDIDATE-ma-attaccabili
  come da contratto).
- Perimetro di novità §3-bis: BOUNDED dal procurement Tillyaeva
  dichiarato — la forma onesta giusta (lint 7 pieno: LL-id citati; il
  claim residuo "l'edificio a tre piani" non è NOT-FOUND ma
  procurement-bounded, dichiarato).

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-15 | REPAIR (MEDIA) | CH7_averaging_edifice.md:757-758 (§7(b)) | "P-B MoC max-thrust su UN singolo stato mediato globalmente con **corner a p_b mediato** (CH5:52-71)" | FORMA SUPERSEDED. La verifica alla fonte di QUESTA sessione (`VERIFY_PB_corner_pb.md`, consumata da CH5 [WB1-R10] e dalla riga ledger LL-20 riformulata) ha stabilito: corner T a p_inf AMBIENTE (Eq. 22); corner J a p_b = media SPAZIALE di base (lessico plug steady, MAI cycle-averaging); la dicitura "corner a p_b mediato" è dichiarata superseded in CH5 §1.1. Causa nominata: CH7 scritto alle 08:37, riformulazione LL-20/CH5 alle 08:43-08:44 (staleness cross-capitolo, non errore d'autore). Nello stesso paragrafo anche i range CH5 citati sono scivolati (le comunanze C-1/C-5 vivono ora a CH5:83-93, non :73-80). Riparazione: allineare §7(b) alla forma source-verified + ri-puntare i range CH5. |

### Tabella DISPOSIZIONE (V-N2)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-15 | REPAIR (MEDIA) | §7(b): sostituire "corner a p_b mediato" con la forma [WB1-R10] (lip a p_inf; base a p_b spaziale, senza fonte) e ri-puntare CH5:83-93 |

### Q&A SEED (dal materiale nuovo CH7)

1. **D**: "Tillyaeva 1975 ha già fatto il contouring con swirl: cosa
   resta a voi?" → **R**: forma onesta di record: precedente CANDIDATO,
   NON letto (WANTED, russo, procurement aperto con owner); il claim di
   novità sul contouring con swirl resta BOUNDED da quel procurement e
   il full-text check è già un duty del gate G5 (riga 2.2(f)) — nessuna
   posizione di merito prima della lettura. → **Ancora**: registry
   :742-746; D6:803-806. → **Backup**: feed 6 (slide forma onesta).
2. **D**: "Fievisohn ha già il wave-frame MoC rotazionale: perché non
   basta?" → **R**: è il cugino più vicino ([IO] dal method-paper 2017):
   ciclo ENDOGENO (iterato, non classe-dati imposta con monitor), mai
   design, mai famiglia per-fase, mai certificati; l'estensione nozzled
   vive nel paper [REP]-bounded non su disco (procurement RAISED). →
   **Ancora**: LL-13; matrix part2:443-500. → **Backup**: feed 7.
3. **D**: "Il vostro path A usa il free-vortex: è un teorema?" → **R**:
   SOLO sotto (rΓ, h0, s) UNIFORMI ([T-N6-2]); su campi per-fase
   stratificati NON è teorema di record — fork dichiarato (lemma misto
   da scrivere vs monitored-neglect armato dal TRIPLE monitor) da
   presentare PRIMA di ogni adozione; annotazione utente di record. →
   **Ancora**: DISPATCH:105-113. → **Backup**: feed 8 + card C51.

### Guardie (CH7, sezioni nuove): 17 CLEAN / 0 HIT

1 CLEAN (§7(b) e feed 3 portano il tallone (J) accanto a ogni claim di
copertura; nessuna gerarchia orfana) · 2 CLEAN · 3 CLEAN · 4 CLEAN
(campo via CH5 istanziato; scuola Kraiko-Tillyaeva nominata con id) ·
5 CLEAN (assi §C-1/§C-2 citati; la disciplina PENDING-PROCUREMENT è
l'istanza esemplare dell'asse) · 6 CLEAN · 7 CLEAN · 8 CLEAN ·
9 CLEAN (novità procurement-bounded, mai assoluta) · 10 CLEAN (§3-bis
su LL-14/LL-13/LL-9 esistenti e fedeli) · 11 CLEAN · 12 CLEAN ·
13 CLEAN · 14 CLEAN (card C51 "non-aggiudicata" 6/6, campo 4
ATTUALE(…, data-check 2026-08-23) non vacuo, GV-2 ok — NOTA
riconciliazione guardia-14 atlas: la card C51 vive QUI (CH7 §7), non
in CH8 come il perimetro CH4 §7-bis lasciava intendere; con C61 in
CH6 §8, delle 12 NEVER restano a CH10 solo C52/C53/C54) · 15 CLEAN
(§6 STORIA esclusa) · 16 CLEAN (§7(b): applicazione esplicita della
regola — perimetro K̄=0 fiberwise SBV-conditional + canali (J)/(H) con
classe) · 17 CLEAN (n/a).

### DECK FEED (CH7): 8/8 verificati

Feed 1-5 (edificio/fibre/K̄/forchetta/monitor): ancore centerpiece e
meanswirl citate con range; numeri coerenti col record verificato in
CH3 (B2 1.5-3%, B1 0.6-9%, (J)/(H) SBV, delta/L_H underived); heel
dichiarato nel feed 3 (guardia 1 ✓). Feed 6 (Tillyaeva pending) e 7
(Fievisohn) VERIFICATI alla riga registry/matrice. Feed 8 (ASK S-5F +
C51) fedele a DISPATCH + card. Nessun feed sopra la propria classe.

### FUORI-PERIMETRO (CH7)

- §6 STORIA (trittici B8a): esclusa per brief (C5).
- Le riparazioni W-A 1-12 (disposizione :805-841): già aggiudicate
  dall'onda precedente, spot-check senza mismatch, non ri-refutate.

### VERDETTO CH7 (sezioni nuove): **REGGE-CON-RIPARAZIONI** (0 BREAK, 1 REPAIR media da staleness cross-capitolo, 0 GAP, 0 NOTE)

---

## CH8 — Design space (sezioni nuove: §1.7 M1-M5 riga G [W-B.1/B6], §3.5 F3, §3-bis N-F/N-G, §7 con 4 card; DECK FEED B6)

### Verifiche eseguite (ancore aperte in finestra)

- **M0:2982-3005 (Parte IV) letta INTEGRALE**: TUTTI i verbatim di §1.7
  reggono ESATTI — "'Without hypotheses' is excluded by theorem" +
  (i)/(ii)/(iii) (:2984-2988), "HYPOTHESES ARE THE PROBLEM'S
  DEFINITION; the ledger instruments every one" (:2987-2988), contratto
  EXISTENCE/NECESSARY/SECOND-ORDER/GLOBALITY (:2989-2993), M1 "T4 is an
  instance" (:2994-2995), M2 (:2996-2997), M3 "repo 1-DOF theorems are
  instances; target: unimodality of the truncated-plug duty variable"
  (:2998-2999), M4 (:3000-3001), M5 (:3002-3003), le tre forze canoniche
  (:3004-3005).
- **Guardia 3 (attenzione ii): CLEAN ESEMPLARE** — §1.7 M3 applica il
  naming C-2 di record SOPRA il verbatim M0 ("il verbatim M0 'repo
  1-DOF theorems are instances' va letto con questo naming": oracolo
  SENZA contouring, solo eps, mai "il caso ugello 1-DOF") — è
  esattamente la forma che la guardia chiede quando la fonte stessa
  usa il lessico vietato.
- **Guardia 2: CLEAN** — nessun uso di T1c in §1.7/§3.5/§3-bis/§7/FEED
  (grep in finestra); M3 tiene la distinzione C-2 ("il rung fissa QUALE
  media entra nella condizione di adattamento, il contouring vincolato
  non c'entra").
- **Guardia 8 (attenzione ii): CLEAN ed ESERCITATA come previsto dalla
  checklist** — G-v enuncia la regola verbatim (best-of-sweep
  certificato, mai ottimo globale senza meccanismo M1-M5) con supporto
  Humphreys [ADV]+CT-6 e stato C57=NEVER dichiarato; feed 5 la porta
  come regola di presentazione.
- SESSION2_LOG.md:87-90 (decisione A4) VERBATIM ✓ — M4/M5 di §1.7 sono
  FEDELI alla decisione (Farrell = riga esistente citabile :1196,
  identità censita NESSUN claim di lettura ✓ registry :1196-1200;
  Lipschitz-global = NOT-FOUND(q) ✓).
- **Ri-esecuzione query M5 (attenzione v)**: `grep -icE
  "Lipschitz|branch.and.bound" docs/literature_registry.yaml` = **0**
  → NOT-FOUND(q) di M5 CONFERMATO.
- **Ri-esecuzione query G-iii (attenzione v)**: pattern -E sui 4 slot
  = 0/0/0/0 ✓, litmap = 0 ✓, MA **literature_registry.yaml = 2 hit**
  (righe "deflat…" :1197/:1200 = la riga farrell censita) — vedi
  finding 16.
- D6:214-229 (F3 entry/exit/ISS-6/ISS-4/RK1) già verificata alla riga
  (blocco CH6): §3.5 FEDELE, verbatim "F3 GEOMETRY CLASSES (3-4
  sessions; plug/aerospike primary)" ✓.
- choice_ledger C57:771-780 ✓ (NEVER, incumbent none/local-only, le 3
  alternative della card verbatim), C1:164-174 ✓ (già verificata CH1),
  C61:818-830 ✓ (già verificata CH6); registry masters:1023-1029
  (READ-PARTIAL; owner ":1029 flag dichiarato" = "20-25-dof claim
  awaits full-text verification" ✓ — il flag della card C1 campo 4 è
  FEDELE), lauer:1031-1037 ✓, farrell:1196-1200 ✓, nocedal:980 ✓;
  glossary:1523-1527 (P-A..P-D) ✓; design v2 :278-279 (assi GRADE /
  ECSS-DO-178C) ✓ e :331 (cella F-ii) ✓.
- §3-bis vs ledger: LL-23/LL-25/LL-27/LL-28/LL-29/LL-31 tutti
  esistenti e FEDELI alle righe (verbatim "senza governance",
  "acceptance test F4b", "col prezzo misurato", "trasferimento =
  scope dichiarato", "exact batte i GA — PRO la nostra rotta");
  novità N-F/N-G con nearest-LL nominati e bound sul perimetro ledger
  (82 paper, matrice 20×82) — lint 7 pieno.

### Finding

| # | Classe | file:riga | Claim attaccato | Evidenza |
|---|---|---|---|---|
| WB1-C3-16 | REPAIR (MEDIA) | CH8_design_space.md:265-279 (G-iii) + DECK FEED 6 (:937-941) | G-iii: query sul perimetro "4 study file + litmap + registry" con esito dichiarato "→ **0 match**" | DOPPIO difetto alla riesecuzione (attenzione v): (1) con `grep -E` il perimetro-registry dà **2 hit** ("deflat" → `wanted_farrell_birkisson_funke_2015`, :1197/:1200) — non 0; ed è la STESSA riga che §1.7 M4 cita come esistente: auto-incoerenza interna alla sezione. (2) il comando come stampato (`grep -i "global optim|globality|…"`) senza `-E` ha i pipe LETTERALI: darebbe 0 match su qualunque contenuto — la query non è riproducibile nella forma citata (disciplina query-bounded, guardia 5/lint 6). L'ESITO DI MERITO SOPRAVVIVE: 0 hit sui 4 slot e sul litmap CONFERMATI — nessun paper P-A..P-D dichiara un meccanismo di globalità. Riparazione: stampare il comando in forma eseguibile (-E), dichiarare gli hit registry come righe censite NOSTRE (non paper del campo), correggere feed 6 ("0 match sui 4 slot + litmap; hit registry = nostre righe censite, dichiarati"). Il MINT-PENDING F-2 della riga erediti la forma corretta. |
| WB1-C3-17 | NOTE (BASSA) | CH8_design_space.md:836-860 (card C61) vs CH6_value_honesty_roadmap.md §8 | Card C61 DUPLICATA in due capitoli (CH6 §8 e CH8 §7(d)) | Oggi convergenti (stesso trigger verbatim :829, stesse alternative harvest, stesso warning Humphreys), ma la duplicazione è un rischio anti-entropia (due copie che possono divergere ai prossimi edit — precedente SR-7 blocchi-delta). Riparazione: una casa primaria (proposta: CH6 §8, il capitolo che presenta lo slot N2 nel value case) + puntatore nell'altro. Nota collegata: il perimetro di ownership dichiarato da CH4 §7-bis ("p_b → CH8/CH10") è consistente con CH8; è la copia CH6 quella fuori dal perimetro dichiarato. |

### Tabella DISPOSIZIONE (V-N2)

| Finding | Classe | Disposizione proposta |
|---|---|---|
| WB1-C3-16 | REPAIR (MEDIA) | Comando in forma -E riproducibile + dichiarazione hit registry non-field + correzione feed 6; forma corretta nel MINT-PENDING |
| WB1-C3-17 | NOTE (BASSA) | Casa primaria unica per la card C61 + puntatore |

### Q&A SEED (dal materiale nuovo CH8)

1. **D**: "Quando dite 'ottimo', ottimo di che cosa?" → **R**: mai la
   parola senza contratto — ogni Verdict dichiara meccanismo (M1-M5) e
   forza ("global" / "within delta of global, certified" / "local +
   enumerated competitors"); oggi il tier globale è C57=NEVER e i numeri
   sono best-of-sweep certificati, dichiarati tali. → **Ancora**:
   M0:2982-3005; pipeline map :138. → **Backup**: feed 4+5 + card C57.
2. **D**: "Il campo ottimizza da decenni: che vi manca da dichiarare?"
   → **R**: nessuno dei 4 paper coupled dichiara esistenza, meccanismo
   o forza di globalità (0 hit sui 4 slot, query rieseguita); il
   contratto per-Verdict è il delta — e la nostra riga censita
   (deflation, Farrell 2015) è dichiarata identità-senza-lettura. →
   **Ancora**: CH8 §1.7 G-iii (forma corretta post WB1-C3-16);
   SESSION2_LOG:87-90. → **Backup**: feed 6 corretto.
3. **D**: "Perché non level-set/topology optimization?" → **R**: ragione
   fisica di record (CAUTION derivata topologica: un corpo infinitesimo
   in supersonico dà solo wave drag) → si confrontano settori interi
   (torneo finito, esistenza per-settore Chenais/[T-P7S1]); card F-ii
   con falsificatore stampato e ramo level-set dichiarato STALE con
   finestra. → **Ancora**: problem_book:361-363; card F-ii §7(d). →
   **Backup**: feed 9.
4. **D**: "Quando arriva il plug vero?" → **R**: fase di piano NOMINATA:
   F3 GEOMETRY CLASSES (3-4 sessioni, plug/aerospike primary), entry a
   F2-exit, ordine-interscambiabile con F4b (ISS-6), budget cappato
   ISS-4 con fallback by-rule. → **Ancora**: D6:214-229. → **Backup**:
   feed 8 + §3.5.

### Guardie (CH8, sezioni nuove): 16 CLEAN / 1 HIT

1 CLEAN · **2 CLEAN** (nessun T1c; attenzione (ii) scaricata) ·
**3 CLEAN ESEMPLARE** (naming C-2 applicato SOPRA il verbatim M0
"1-DOF" — attenzione (ii) scaricata) · 4 CLEAN (PKU/NUAA/Jourdaine
nominati, glossary:1523-1527) · 5 CLEAN sul lato assi (§7(c) §C-3+§C-2
con ancore design v2) MA la riproducibilità-query è colpita dal
finding 16 · 6 CLEAN · 7 CLEAN (stato engine onesto, feed 8) ·
**8 CLEAN ESEMPLARE** (G-v + feed 5: best-of-sweep ≠ argmax, regola
esercitata come la checklist prevedeva — attenzione (ii) scaricata) ·
**9 HIT** (WB1-C3-16: esito query G-iii infedele alla riesecuzione su
un ramo del perimetro + comando non riproducibile come stampato; il
merito del claim sopravvive) · 10 CLEAN (§3-bis fedele al ledger) ·
11 CLEAN · 12 CLEAN · 13 CLEAN (Humphreys CT-6 dichiarato in G-v e
feed 7) · 14 CLEAN (4 card 6/6: F-ii con doppio stato
ATTUALE/STALE-per-ramo — forma GV-2 corretta; C57/C61 non-aggiudicate
STAMPATE; campo 4 mai vacuo; NOTA duplicazione C61 = finding 17) ·
15 CLEAN (§6 esclusa) · 16 CLEAN · 17 CLEAN.

### DECK FEED (CH8): 9/9 verificati, 1 HIT

Feed 1-3 (formulazione/torneo/[T-T4] con eredità C-HT4 dichiarata ✓),
4 (contratto M1-M5 ✓ verbatim), 5 (guardia 8 ✓), 7 (Humphreys+M3 ✓
CT-6), 8 (stato engine + F3 ✓), 9 (rotta per-settore + LL-29
CANDIDATE dichiarato ✓). **Feed 6 = HIT WB1-C3-16** (eredita "0
match" sul perimetro intero). Nessun feed sopra la propria classe;
feed 9 dichiara lo stato CANDIDATE del lineage (C6 pending) — corretto.

### FUORI-PERIMETRO (CH8)

- §6 STORIA (trittici 6.1-6.6, W-B.2): esclusa per brief (C5).
- Riparazioni W-A 1-10 (disposizione :864-895): già aggiudicate
  dall'onda precedente; la nota B6 (:897-904) sull'esercizio delle
  guardie 8/9 nelle sezioni nuove è stata VERIFICATA qui (8 CLEAN,
  9 HIT come da finding 16 — la nota B6 sulla 9 "attivata e
  soddisfatta in §3-bis" resta vera per il §3-bis; l'HIT è in §1.7).

### VERDETTO CH8 (sezioni nuove): **REGGE-CON-RIPARAZIONI** (0 BREAK, 1 REPAIR media, 0 GAP, 1 NOTE; guardie 2/3/8 delle attenzioni specifiche tutte CLEAN, due in forma esemplare)

---

# CHIUSURA COMPLESSIVA (slot C3, onda W-C.a)

## Conteggio finding per classe (totale 17)

| Classe | # | Id |
|---|---|---|
| BREAK | 0 | — |
| REPAIR | 5 | WB1-C3-09 (CH4, MEDIA), WB1-C3-10 (CH4-feed-8 via CH5, MEDIA), WB1-C3-14 (CH6 feed, ALTA), WB1-C3-15 (CH7, MEDIA), WB1-C3-16 (CH8, MEDIA) |
| GAP | 1 | WB1-C3-04 (CH1, MEDIA — consumo guardia 17 mancante in §1.7) |
| NOTE | 11 | WB1-C3-01/02/03 (CH1), 05/06/07 (CH2), 08 (CH3), 11 (CH5), 12/13 (CH6, MEDIE), 17 (CH8) |
| DOWNGRADE | 0 | — |

## Guardie: conteggio HIT aggregato (17 guardie × 8 capitoli)

- **HIT**: guardia 17 × CH1 (WB1-C3-04, consumo assegnato mancante);
  guardia 8 × consumo-CH4-di-CH5 (WB1-C3-10, feed senza caveat P-B —
  contato sul capitolo consumatore); guardia 9 × CH8 (WB1-C3-16,
  query non riproducibile come stampata + esito infedele su un ramo).
- **CLEAN**: tutte le altre celle. Guardie 1 e 16 su CH6 §1.2-bis:
  CLEAN in forma ESEMPLARE (verificate occorrenza per occorrenza);
  guardie 2/3/8 su CH8: CLEAN, due esemplari; guardia 14: 20 card
  totali verificate 6/6 con GV-2 (campo 4 mai vacuo, data+token
  presenti; flag STALE usato correttamente in C58/C61/F-ii-ramo-i);
  copertura atlas delle 12 NEVER: C25/C38/C55/C57/C59/C60/C62 (CH4) +
  C61 (CH6+CH8, dup finding 17) + C51 (CH7) = 9; C52/C53/C54 →
  CH10 (fuori perimetro, da verificare dal refuter di CH10).

## Query NOT-FOUND: tutte rieseguite (attenzione v)

H-iii (CH1) CONFERMATA-con-correzione-descrittiva (WB1-C3-01);
[WB1-R6] spettrale (CH5) CONFERMATA (0/0/0/0); Q-iii (CH6) CONFERMATA
(0+0 sul ramo design-gap; near-object alle righe dichiarate); M5
Lipschitz/BB (CH8) CONFERMATA (0); G-iii (CH8) INFEDELE su un ramo
(WB1-C3-16, merito sopravvive); N-H/N-A/N-Q ledger-scan CONFERMATE.

## FUORI-PERIMETRO complessivo

- **§6 STORIA di tutti i capitoli**: ESCLUSE per brief (C5 dopo);
  elenco commit citati dalle STORIE da verificare (per C5): b0a4c15,
  a85e355, ea2abce, b3da86d, 3b2b9e6, 904f950, 1a11f2c, fd2d444,
  da91aa4, d968502, 318d3fd, cc878ef.
- **CH9/CH10**: non nel mio perimetro (altro slot); segnalate a
  CH10: card C52/C53/C54 (guardia 14) + consumo guardia 17
  (CH10 §1/§5-U3'/§8 è consumatore dichiarato).
- Le sezioni pre-esistenti (REFUTE_CH1-8) NON ri-refutate; spot-check
  incidentali senza mismatch dichiarati nei blocchi.

## VERDETTO COMPLESSIVO (sezioni nuove W-B.1, CH1-CH8)

**REGGE-CON-RIPARAZIONI**: 0 BREAK su 8 capitoli; la sostanza delle
sezioni nuove è ancorata con fedeltà alta (tutti i verbatim aperti
reggono alla riga; le 20 card sono fedeli al ledger; i §3-bis sono
fedeli al LINEAGE_LEDGER con lint 7 pieno). I difetti veri stanno nel
LIVELLO FEED/QUERY: 3 feed che produrrebbero slide attaccabili
(WB1-C3-10/14 + feed 6 CH8) e 2 query/anchor report infedeli alla
riesecuzione (WB1-C3-01/16) — esattamente la classe di rischio per cui
il retro-audit del deck esiste. Lo storyboard v3 NON deve joinare
CH4-feed-8, CH6-feed-1 e CH8-feed-6 nella forma attuale prima delle
riparazioni. Scope del brief COMPLETO: nessun capitolo residuo.
