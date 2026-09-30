# CH9 — Come sa la macchina di non mentire (N-J: la catena di certificazione può dire NO)

Writer B1, onda W-B.1 dell'atlas S-PRES (sessione 2, 2026-08-23).
**Stadio di confronto**: design ATLAS_RESEARCH_DESIGN_v2.md §M riga J
(celle J-i..J-v, tutte SCOPERTE, owner B1) + cella P-ii [V2-R12], come
emendato da ATLAS_DESIGN_v2.1_AMENDMENT.md (template a 9 sezioni, §3-bis,
lint 7/8, DECK FEED), contro il record misurato in finestra:
validation/PROGRESS_2026-08-13_Scert.md (verdetto di record),
docs/findings_registry.yaml (righe audit-scert, grep in finestra),
docs/claims_registry.yaml (classi e carrier, righe citate per numero),
docs/rde_nozzle_development_plan.md (D6, gate), docs/rde_nozzle_SCAFFOLD.md
(§2/§5). **Arco di consumo**: refuter C1 (W-C.a, REFUTE_CH9) contro
GUARD_CHECKLIST.md; §6 STORIA = SCRITTA da B8b (W-B.2, 2026-08-23 —
preambolo aggiornato dall'orchestratore al landing, ex-placeholder);
storyboard v3 consuma il blocco `## DECK FEED`; le decision card joinano
su {antenato, ancora, data} per il grafo camminabile [F-des-4].

Convenzioni: ogni ref letteratura = id VERBATIM di
docs/literature_registry.yaml (174 id, `grep -c "^- id:" ` misurato in
finestra, SR-12); ogni claim porta la classe di rigore; anchor `file:NNN`
= riga misurata in finestra.

==============================================================================
## §1 LA DOMANDA

> **N-J: Come sa la macchina di non mentire — la catena di certificazione
> può dire NO?**

Un tool di design che produce un numero (J, un contorno, un ottimo) senza
un meccanismo che possa RIFIUTARE quel numero non è uno strumento di
scienza: è un generatore di plausibilità. La domanda del nodo è se la
catena di verifica del programma sia capace di emettere un NO — non in
linea di principio, ma di fatto, contro il proprio stesso lavoro.

**Il falsificatore: GIÀ SPARATO, ed è a registro.** L'audit S-CERT
(2026-08-13, contract validation/ADVISORY_Scert_prompt_2026-08-12.md) ha
emesso il verdetto di record **NON-CERTIFICABILE — 2 P0 a HEAD**
(PROGRESS_2026-08-13_Scert.md, sezione SESSION VERDICT): (P0 suite) il
gruppo (vii) del lint numerico rosso a HEAD per file-strumento senza righe
baseline — **riparato nella stessa finestra, dichiarato** (37 file, 639
literal baselined, 0 violazioni alla ri-esecuzione); (P0 staleness) il
gate di staleness CIECO al drift di import-closure/env — **aperto, owner
F2** (findings_registry.yaml:1508, riga
`audit-scert:staleness-import-closure-blind`), corroborato POSITIVAMENTE
dal carrier X-CDKAT (−13.9% di drift sui numeri di record con stamp
pass=2026-08-11 intatto, findings:1511, riga carrier-evidence :1517). Questo capitolo presenta il NO
detto come LA PROVA che il falsificatore del nodo è vivo — mai come un
incidente da ammorbidire: una catena che non ha mai detto NO non ha mai
dimostrato di poterlo dire.

**Ipotesi sotto cui la domanda è ben posta**: (i) esiste un oggetto
certificabile — la classe S1 fitted-front con march per-cella (M0 D2.5);
(ii) esiste una gerarchia di oracoli dichiarata PRIMA dei run di scienza
(G1, D6:775); (iii) i test possono RIGETTARE, non solo confermare
(disciplina R5, CLAUDE.md — tolleranze derivate, mai magiche); (iv) il
verificatore stesso è oggetto d'audit (S-CERT ha auditato il
certificatore, non solo il certificato).

==============================================================================
## §2 LETTERATURA (due colonne)

### (a) Senso / precedenti — come il campo valida i propri design

Il campo RDE-nozzle — istanziato: PKU (`liu_2022` = P-A), NUAA
(`li_xu_lv_lv_song_2023` = P-B, `li_xu_lv_yu_zhou_2025` = P-C),
KIT-Aoyama (`jourdaine_2019` = P-D), Purdue (`stechmann_2019`,
`harroun_2021`), NASA-Glenn (`paxson_miki_2022`) — valida per CONFRONTO
SINGOLO: un design contro una istanza CFD o un esperimento, senza tier di
evidenza dichiarato, senza barre derivate, senza un test che possa
rigettare. Istanze di record:

- `harroun_2021`: la validazione è una istanza senza tier — CT-3 del
  threat ledger (CH5 righe 222-227 [anchor corretto da C1, REFUTE_CH9
  F-10]: i "nearest referee-shaped pairs"
  P-B Fig. 15 / P-C Figg. 13+20b sono squalificati per compagno mediato
  globalmente e verità same-family URANS); convenzione di media
  UNDECLARED nel paper (LINEAGE_LEDGER LL-2, deep-check pp. 670-671 +
  Eq. 10).
- `liu_2022` (P-A): asserisce M_t = 1.0 anche per il caso senza gola
  (Case A) — l'istanza di choking non certificato più netta del corpus
  (nota A-L6, literature_registry.yaml:622, [ADV]).
- `paxson_miki_2022`: J cycle-averaged a livello CFD, OFAT, senza
  ottimalità né bande (LL-5).

Sul lato classico i CERTIFICATI esistono ma non formano una catena:
`hoffman_1967` porta l'E-residual Eq. (78) — un certificato di classe
VI.3 ante litteram (registry:372-378); `kraiko_tillyaeva_2015` porta la
catena interna Route B→A con certificati (LL-14). Nessuno dei due ha un
adjoint discreto verificato, né un gate che blocchi la "scienza" a valle.

### (b) Strumenti — che cosa usa il mondo per domande di questa classe

- **Errore del passo di Newton, certificato**: `yamamoto_1986_numermath48`
  — bound a-posteriori Gragg-Tapia/Potra-Ptak/Miel sotto ipotesi di
  Kantorovich (Thm 2 verificato sul PDF in-repo, pp. 91-92; identity flag
  vol. 48-vs-49 dichiarato a registro, aperto). È l'antenato della nostra
  certificazione per-cella del march (nodo N-K per il passo).
- **Intervallo FD ottimale sotto rumore**:
  `shi_xie_xuan_nocedal_2022_fd_interval` — la stima dell'intervallo di
  differenze finite come problema con soluzione derivata, non con
  costante magica: lo stesso principio della nostra regola "tolleranze
  derivate" (R5).
- **Error estimation goal-oriented (DWR)**: `wanted_becker_rannacher_2001`
  (il paradigma dual-weighted residual) e `wanted_fidkowski_darmofal_2011`
  (la review di riferimento del campo CFD, letta [PARTIAL-pp.673-676]) —
  la disciplina mondiale per "quanto errore sul funzionale obiettivo".
- **Grid Convergence Index**: `wanted_roache_gci_1994_1997`,
  `wanted_celik_2008` — la prassi V&V codificata dei journal CFD (riga
  censita a livello standard-practice, PANEL_C9C11.md 2026-08-19).
- **Verifica del gradiente sotto periodicità**: `zahr_persson_2016` —
  adjoint fully-discrete con monodromia e gradient verification (LL-18).
- **Il teorema negativo**: `giles_ulbrich_2010_part1` /
  `giles_ulbrich_2010_part2` — la convergenza dell'adjoint discreto
  attraverso gli shock può FALLIRE (scoping 1-D scalare dichiarato): il
  motivo per cui la nostra classe certificata è fitted, non captured
  (aggiudicazione C49, choice_ledger.yaml:682-692).

Il confronto disciplina-nostra vs DWR/GCI è svolto in §7(a) con decision
card.

==============================================================================
## §3 LA PROPOSTA (query-bounded)

Il programma propone, per il campo RDE-nozzle, una **catena di
certificazione con potere di veto**, quattro pezzi:

1. **G1 assoluto** — ORACLE GATE: "O1/O2/O3 or no science" (D6:775; riga
   di gate D6:285: riaffermato da F2/F3/F5, unchanged, absolute). Nessun
   numero di scienza esce da una macchina non certificata: il gate blocca
   il LAVORO a valle, non solo la pubblicazione.
2. **La catena degli oracoli** — O1 (collasso T3), O2 (T4 peak plug)
   (D6:580-582); O3.1 = esattezza del trasposto (identità dot-product al
   floor macchina, Lemma B); O3.2 = test d'ordine sul tangente; O3.3 =
   match dei moltiplicatori closed-form vs campo adjoint AD
   (claims_registry.yaml:197-205); O3.4 = oracolo cross-code GENO, due
   leg di record: leg flowfield CHIUSA S10 ([X-GENOXC], claims:795 —
   scope dichiarato: interior unit process only, non wall/corner/shock
   né contorno assemblato), leg gradiente (JAX grad vs GENO FD,
   P2_outline:251) dichiarata atterrare con il motore A1 (D6:826-830) e
   SENZA pass di record in finestra = residuo dichiarato [C1 F-8]. Più
   i KAT (known-answer tests: flagdef KAT_BFUN a gamma=1.4 closed-form
   D6:130, jitter sintetico D6:422, certdiag KAT D6:40) e il
   **dual-seed**: ogni batch di audit porta un seed
   known-true E un canary falso; l'audit passa solo se conferma il vero E
   rifiuta il falso (PROGRESS_2026-08-13_Scert.md, P0#1 DISCHARGED
   esattamente così).
3. **Il formato Verdict** (la proposta di prodotto, cella J-iv): nessun
   risultato lascia il tool fuori da un Verdict = contorno + performance
   + certificate stack + record oracoli (D6:679-681; CLAUDE.md R5:
   "contorno + certificati + barre + record oracoli"). Il certificato è
   parte dell'output, non un'appendice.
4. **L'audit del certificatore** — la catena si applica a se stessa:
   S-CERT ha auditato il verificatore con find→verify avversario a due
   passate, dual-seed dedicato e final judge; l'esito (NON-CERTIFICABILE)
   è il funzionamento, non il fallimento, del disegno.

**Query bound (guardia 9)**: il claim di novità è "nessun metodo di
design di ugelli RDE pubblicato consegna il design DENTRO una catena di
certificazione con potere di veto (gate assoluto + oracoli indipendenti
+ test che rigettano + formato Verdict)". Perimetro e esito della query:
§7(b), esito NOT-FOUND(q). Residuo G5 dichiarato (passaggio umano
Kraiko-1979/PMM, blocca submission non lavoro, D6 G5).

==============================================================================
## §3-bis ANTENATI DIRETTI (lineage claim)

Righe dal LINEAGE_LEDGER (join {LL-id, componenti}; stato CANDIDATE fino
al passaggio del refuter C6, W-C):

- **LL-12 — Giles-Ulbrich 2010** (`giles_ulbrich_2010_part1`/`_part2`;
  componente 11 discrete adjoint): il teorema negativo
  adjoint-discreto-su-shock. NON è un antenato della macchina: è
  l'antenato dell'**AGGIUDICAZIONE** — la ragione dimostrata per cui la
  classe certificata di record è fitted-front (C49,
  choice_ledger.yaml:682-692: fitted = SOLE certificate bearer, anchor
  Giles-Ulbrich tenuto a scope 1-D scalare dichiarato). Cosa gli manca
  vs noi: nessuna catena costruttiva — dice dove NON si può certificare,
  noi costruiamo dove si può.
- **LL-14 — Kraiko-Tillyaeva 2015** (`kraiko_tillyaeva_2015`; componenti
  3/11/12): catena Route B→A interna con certificati — l'antenato più
  vicino dell'idea "il design porta il proprio certificato". Cosa gli
  manca vs noi: famiglia mediata per-fase, adjoint discreto verificato
  (O3.1), gate con potere di veto sull'intero programma.
- **LL-18 — Zahr-Persson 2016** (`zahr_persson_2016`; componenti
  6/11/12/15): adjoint fully-discrete sotto periodicità + verifica del
  gradiente + monodromia — l'antenato della VERIFICA DEL GRADIENTE come
  passo obbligato. Cosa gli manca vs noi: la periodicità è endogena al
  loro solutore (noi: classe-dati imposta al contratto Γ_d); la verifica
  è un check del paper, non un gate che blocca la scienza a valle; nessun
  formato-Verdict, nessun audit del verificatore.
- (Supporto, stessa fonte) **LL-7 — Hoffman 1967** (`hoffman_1967`;
  componenti 4/10/11/12): l'E-residual Eq. (78) come certificato VI.3 —
  antenato del singolo certificato, senza catena né veto.

Ogni claim di novità del §3 cita ≥1 riga qui sopra (lint 7): il pezzo 2
(catena oracoli) ha antenati parziali LL-14/LL-18/LL-7; i pezzi 1, 3, 4
(gate assoluto, Verdict come formato di prodotto, audit del
certificatore) restano coperti dalla query di §7(b): ANTENATI:
NOT-FOUND(q_J3) sul perimetro dichiarato.

==============================================================================
## §4 ANALISI FORMALE (classi di rigore, con ancore)

| oggetto | classe | ancora | contenuto |
|---|---|---|---|
| G1 oracle gate | PRACTICE (governance di gate, vincolante) | D6:775, D6:285 | O1/O2/O3 o nessuna scienza; assoluto, riaffermato a ogni fase scienza |
| T-LEMB (O3.1) | **THEOREM** (finite-dim; mesh limit ESCLUSO, vive in S-LBML) | claims_registry.yaml:485-497 | il march fitted è block-triangular e il reverse-AD con regole implicite È lo sweep adjoint trasposto; falsifier = fallimento dell'identità dot-product su qualunque brick (i carrier X-G0/X-G0AX/X-A1IM rigettano vjp corrotti) |
| S-LBML (limite mesh di Lemma B) | SCHEMA | claims_registry.yaml:656-668 | rotta Lax-equivalence (i)-(v) scritta; inherits C-D25U, C-MAJDA; O3.2 misura l'ordine reale |
| [X-O31CS] (O3.1-cs) | carrier PRACTICE | claims_registry.yaml:1940-1946 | strumento d'audit primal-independent: twin numpy-complex indipendente + complex-step IFT vs il custom_vjp del motore; il buco common-mode di O3.1 (coppie transpose-consistent-but-wrong) DIMOSTRATO dal negative control CS4 e CHIUSO a livello unit-process; coverage dichiarata: interior only, wall/axis/legge = residuo registrato owner F2 |
| C-O33 | conditional **SCHEMA** (residuo NUMERIC dichiarato, non gap analitico) | claims_registry.yaml:197-205 | match moltiplicatori O3.3: la campagna pre-registrata È girata (X-O33B, S19: criterio primario R6 PASS, f2 constant 9.5e-03/8.0e-03); aperto = residuo design-class della riga corner + riformulazione margin-constrained (M0 Parte VI) — NON disponibilità del motore |
| Verdetto S-CERT | verdetto d'audit di record | PROGRESS_2026-08-13_Scert.md | NON-CERTIFICABILE, 2 P0 a HEAD; P0 audit-integrity SCARICATO via dual-seed (canary REFUTED + known-true CONFIRMED, 0 slot nulli) |
| MC8 (lente primaria utente) | esito d'audit | PROGRESS_2026-08-13_Scert.md, WHAT SURVIVED | REGGE 8/8 branchings campionati — KS aggregation, RK-G policy, C1 thermo closure, M5c executor, fitted-front rule, T7(c) cone form: tutti tracciano a bisogni di piano nominati con aggiudicazione a tre livelli |
| Run end-to-end di record | verified (stage P34 dichiarato, guardia 7) | D6:883; memoria s18 | trasversalità KKT 7.7e-02 ≤ tol derivata, oracolo 91/91 — machine-verified, non validated-su-hardware, non prediction |

Tre fatti formali portano il peso del capitolo:

1. **Il trasposto non è approssimato, è esatto** (T-LEMB, THEOREM): in
   dimensione finita il gradiente reverse-AD è lo sweep adjoint
   trasposto — l'oracolo O3.1 verifica un'IDENTITÀ, non una convergenza.
   Il limite mesh resta SCHEMA (S-LBML): la separazione è dichiarata, mai
   confusa.
2. **Il buco common-mode di un self-check è dimostrabile e chiudibile**:
   O3.1 da solo passerebbe una coppia (march, adjoint) coerentemente
   sbagliata; [X-O31CS] lo DIMOSTRA (CS4) e lo chiude con un twin
   primal-independent. Un check che non può fallire non certifica: qui il
   modo di fallimento è stato costruito, esibito e sbarrato.
3. **Il verdetto negativo è un teorema d'esistenza del NO**: la catena ha
   rifiutato di certificare il proprio stato a HEAD, due volte (prima
   passata: rifiuto di auto-assoluzione su verification layer rotto;
   seconda: layer provato via dual-seed, e ANCORA NON-CERTIFICABILE su
   2 P0 di merito). Delta di livello, frase del final judge di record:
   "the 2026-08-07 defects were in the certified object; the 2026-08-13
   defects are in the certifier" — il pavimento è salito, il tetto è in
   coda (PROGRESS_2026-08-13_Scert.md, DELTA).

==============================================================================
## §5 STATO (aperti con owner e trigger)

Dimostrato / eseguito: G1 armato (D6:775); O3.1 a precisione macchina sui
brick + common-mode chiuso a unit-process ([X-O31CS]); O3.4 leg
flowfield PASS con entrambi i negative control che rigettano
([X-GENOXC], scope interior unit process; la leg gradiente di O3.4
resta senza pass di record — residuo dichiarato, D6:826-830, primo
blocco oracoli F2 [C1 F-8]); dual-seed
provato in entrambe le direzioni (S-CERT P0#1 discharged); MC8 8/8.

Aperti, ciascuno con owner e trigger (mai riempiti qui):

| aperto | riga registro | owner | trigger |
|---|---|---|---|
| Staleness gate cieco a import-closure/env drift (P0#3); include il canale tracked-but-uncommitted | `audit-scert:staleness-import-closure-blind` (findings:1508) | **F2** | F2 entry; carrier-evidence X-CDKAT (findings:1511, riga carrier-evidence :1517, −13.9% con stamp intatto) |
| pass= futuri accettati (auto-disinnesco latente) | `audit-scert:future-pass-dates-accepted` (findings:1562) | F2 | F2 entry, stessa fix family del P0#3 |
| C-O33 aperta ma QUANTIFICATA: residuo design-class della corner row, non gap del motore; riformulazione margin-constrained | claims:197-205 + `registry-legacy:C-O33-STALE-CONDITIONAL` (findings:747, DISCHARGED-statement S21) | F2 (M0 Parte VI) | primo blocco oracoli F2 (claims:201 owner F2; finestra condivisa con `oracles:a1-gp01-quasi1d-not-built`, il cui trigger è findings:1486 — anchor ri-attribuito da C1, F-9) |
| Rejector H4 doctored-code_id vacuo | `audit-scert:h4-doctored-rejector-vacuous` (findings:1553) | F2 | F2 entry |
| Classe ondemand senza artefatti di run persistiti (evidence layer) | `audit-scert:ondemand-no-run-artifacts` (findings:1571) | F2 | F2 entry |
| Canale anti-re-mint: 3 classi di evasione dimostrate | `audit-scert:anti-remint-evasion-classes` (findings:1535) | F2 | F2 entry |
| Coverage [X-O31CS]: wall/axis/legge/composition non coperti | claims:1945 (coverage declared) | F2 | F2 entry |
| Fedeltà del continuo adjoint (A1/A3 mai run; A2 copre solo l'interior) | PROGRESS_2026-08-13_Scert.md, DECLARED LIMITS | F2 | F2, decisione A2=(a) di record 2026-08-13 |

Nessuna decisione utente pendente propria di questo nodo; le decisioni
di quadro (F2 entry) vivono in CH6 §3.

==============================================================================
## §6 STORIA (writer W-B.2, 2026-08-23 — trittico [V2-R2]; ogni battuta
## porta DATA + PROCESSO + VERDETTO, campi di join del retro-audit §5-bis)

### 6.1 G1 e la gerarchia degli oracoli (il gate assoluto)

- **Battuta 1 — derivazione originale.** DATA: 2026-07-16 (protocollo di
  aderenza CLAUDE.md R5/R6, data dichiarata in testa al protocollo) con il
  piano D6 come carrier ("O1/O2/O3 or no science",
  `docs/rde_nozzle_development_plan.md:775`; riga gate `:285`). PROCESSO:
  stesura del piano a fasi con gate + disciplina R5 (test che RIGETTANO,
  tolleranze derivate). VERDETTO: G1 dichiarato ASSOLUTO alla nascita del
  piano — blocca il lavoro a valle, non solo la pubblicazione.
- **Battuta 2 — (a) RIDERIVATO-PIENO (architettura).** DATA: 2026-08-17
  (Phase A/B S-FOUNDATIONS, derivatori ciechi su brief agnostico).
  PROCESSO: tree diff dei 4 alberi ciechi vs il record. VERDETTO: la
  classe di soluzione certificata è raggiunta da 4/4 alberi con
  "capturing never a certificate"
  (`validation/sfoundations_raws_2026-08-13/phaseB_tree_diff.md:330-335`)
  e la certificabilità-come-vincolo-prezzato è raggiunta 4/4 — "the
  strongest single methodological validation in the diff" (`:347-350`).
- **Battuta 3 — convergenza.** DATA: 2026-08-13 (S-CERT). PROCESSO: il
  gate applicato al certificatore stesso (§3 punto 4). VERDETTO: nessun
  flip; classe finale PRACTICE di governance (vincolante), con
  l'architettura convalidata cieca alle spalle.

### 6.2 T-LEMB / O3.1: l'esattezza del trasposto

- **Battuta 1 — derivazione originale.** DATA: 2026-08-06 (sessioni
  S17-S18, brick 2 A1 di record: "the VARIATIONAL TOC ROAD EXISTS
  END-TO-END", `docs/rde_nozzle_MASTER.md:3251-3253`; enunciato e classe
  in `docs/claims_registry.yaml:485-497`). PROCESSO: derivazione Lemma B
  (march fitted block-triangular ⇒ reverse-AD = sweep adjoint trasposto)
  + carrier con identità dot-product al floor macchina. VERDETTO: THEOREM
  finite-dim; limite mesh ESCLUSO e separato (S-LBML, SCHEMA,
  claims:656-668).
- **Battuta 2 — (c) NON-RIDERIVATO (nessuna riderivazione cieca del
  lemma); doppia prova alternativa.** DATA: 2026-08-13 ([X-O31CS]
  costruito all'apertura S-CERT, decisione utente A2=(a)) + 2026-07-20
  (dual-code GENO [X-GENOXC], pass= della riga carrier,
  claims:795-800). PROCESSO: twin numpy-complex primal-independent +
  complex-step IFT vs il custom_vjp del motore (CS3 dentro bande
  DERIVATE 1.9e-8..9.5e-8; negative control CS4 che DIMOSTRA il buco
  common-mode e lo rigetta dal lato indipendente) + oracolo cross-code
  interior unit process 218/218 con negative control che rigettano.
  VERDETTO: identità confermata da due strumenti indipendenti; coverage
  interior-only DICHIARATA (owner F2, claims:1945).
- **Battuta 3 — convergenza.** DATA: 2026-08-13 (S-CERT). PROCESSO:
  audit del certificatore. VERDETTO: l'esattezza non protegge dallo
  staleness — X-CDKAT −13.9% con stamp intatto (findings:1511, riga carrier-evidence :1517); classe
  finale THEOREM (T-LEMB) + residuo staleness owner F2 (findings:1508).

### 6.3 Il dual-seed (canary + known-true)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-13. PROCESSO:
  ordine utente "NOTHING-LOST da principio a FIRING GATE" (rejector
  seminati: un detector che non spara sul proprio seed è rotto —
  prompt S-ORDINE, commit f3c5df5) → prima esecuzione bidirezionale alla
  chiusura S-CERT. VERDETTO: P0 audit-integrity SCARICATO — canary
  REFUTED con falsificazione positiva alla fonte, known-true CONFIRMED,
  0 slot nulli (PROGRESS_2026-08-13_Scert.md, P0#1).
- **Battuta 2 — (c) strumento, non teorema; doppia prova = istanze
  indipendenti di fuoco.** DATA: 2026-08-17/20 (hypaudit: SEED-A canary
  CAUGHT, SEED-B known-true non flaggato,
  `validation/sfoundations_raws_2026-08-13/hypaudit/VERDICT_hypothesis_audit.md:15-19`;
  il primo seed MIS-DESIGN fu catturato dal refuter e ri-eseguito —
  catch onesto di record, commit 5221529) + 2026-08-21 (coverage gate
  C4: SEED-OMIT P34 catturato, SEED-DECOY C50 non flaggato, commit
  fd2d444). PROCESSO: ri-esecuzione su tre finestre indipendenti.
  VERDETTO: lo strumento è provato in ENTRAMBE le direzioni su tre
  occasioni datate distinte.
- **Battuta 3 — convergenza.** DATA: 2026-08-17 (S-FOUNDATIONS parte 1).
  PROCESSO: adozione come gate R3 standing ("instrument
  adopted-as-candidate standing R3 gate", commit 5221529). VERDETTO:
  classe PRACTICE con rejector che DEVE sparare sul seed; nessuna
  regressione registrata da allora.

### 6.4 Il NO di record: NON-CERTIFICABILE (evento datato)

- **Battuta 1 — derivazione originale (l'evento).** DATA: 2026-08-13
  (contract `validation/ADVISORY_Scert_prompt_2026-08-12.md`; verdetto
  in PROGRESS_2026-08-13_Scert.md, SESSION VERDICT). PROCESSO:
  find→verify avversario a due passate (21 agenti, verifier
  default-REFUTE, campione stratificato seed 20260813, judge finale +
  Form-3 red-team). VERDETTO: **NON-CERTIFICABILE, 2 P0 a HEAD** —
  (vii) riparato in-window con dichiarazione; staleness import-closure
  APERTO owner F2.
- **Battuta 2 — (c) NON-RIDERIVATO (un verdetto d'audit non si
  rideriva); doppia prova = dual-seed + dual-code GENO + refuter
  S-CERT.** DATA: 2026-08-13. PROCESSO: (i) dual-seed dedicato
  (P0#1 discharged, entrambe le direzioni); (ii) catena dual-code
  ([X-GENOXC] claims:795 + MOC-08 falsificatore ESEGUITO PASS nella
  stessa finestra: J_def riprodotto a 1e-14 rel, meccanismo common-mode
  della claim-19 REGGE); (iii) lo stack refuter S-CERT stesso, che alla
  prima passata RIFIUTÒ l'auto-assoluzione su un verification layer non
  provato ("pass refused to certify itself on a broken verification
  layer", `validation/PROGRESS_2026-08-13_Scert.md:184`
  [fix ST-C5-19]). VERDETTO: il NO regge alle sue stesse controprove —
  è segnale, non rumore.
- **Battuta 3 — convergenza.** DATA: 2026-08-13 (DELTA del final judge)
  → consumo S-PRES 2026-08-23. PROCESSO: confronto misurato con l'audit
  2026-08-07. VERDETTO: "the 2026-08-07 defects were in the certified
  object; the 2026-08-13 defects are in the certifier" — pavimento
  salito, tetto in coda F2; MC8 8/8; classe finale = verdetto d'audit di
  record, presentato come LA PROVA che il falsificatore del nodo è vivo
  (§1). Residui tutti nominati con owner (findings:1508/1535/1553/
  1562/1571).

### 6.5 O3.4 cross-code GENO: accordo ≠ verità

- **Battuta 1 — derivazione originale.** DATA: 2026-07-20 (pass= della
  riga carrier [X-GENOXC], claims:795-800). PROCESSO: oracolo G0
  cross-code all'interior unit process (218/218 clean-core; negative
  control corrupted-child 100%→0%, wrong pairing 84x). VERDETTO: PASS
  con entrambi i controlli negativi che rigettano; scope dichiarato
  interior-only.
- **Battuta 2 — (c); doppia prova = l'audit critico del PARTNER di
  cross-code.** DATA: 2026-08-13 (S-GENOAUDIT parallela,
  `validation/ADVISORY_moc_zucrow_fidelity_2026-08-13.md`: unit process
  gemellati ESATTI, ma accordo Ch.16≡Ch.17 VACUO sul rotazionale e ramo
  cross-stream mai esercitato) + 2026-08-17 (P0 MOC-10 wall-thrust
  double-count su output committati: **riferimenti di spinta GENO messi
  in QUARANTENA**, commit 5221529). PROCESSO: dubbi-a-convergenza
  applicati all'oracolo stesso. VERDETTO: il programma ha dimostrato DA
  SÉ che l'accordo cross-code non è verità, e ha quarantenato il proprio
  oracolo dove serviva.
- **Battuta 3 — convergenza.** DATA: 2026-08-13 (dottrina standing "mai
  assumere GENO bug-free"; lista di invarianti indipendenti — O3.1-cs è
  esattamente questo). PROCESSO: sostituzione della fiducia cross-code
  con strumenti primal-independent. VERDETTO: classe finale carrier
  PRACTICE con scope e quarantena dichiarati; la coppia
  [X-GENOXC]+[X-O31CS] è la forma matura del nodo.

==============================================================================
## §7 POSIZIONAMENTO / CONFORMITY (tre metà)

### (a) STRUMENTI — terne mondo-SOTA / cosa usiamo / perché

| strumento del nodo | mondo-SOTA (id registry) | cosa usiamo | perché |
|---|---|---|---|
| errore del passo Newton | `yamamoto_1986_numermath48` (bound Kantorovich a-posteriori) | certificazione per-cella del march ([X-TOCV], claims:1253: "per-cell certification") con floor derivato ‖A‖_inf × floor_z ([X-O31CS] CS1, honest catch di record: il moltiplicatore magico 1e6x è stato RIMOSSO derivando il floor) | il bound è derivabile dalla struttura del problema, non stimato |
| intervallo FD | `shi_xie_xuan_nocedal_2022_fd_interval` | intervalli complex-step h=1e-20 dove possibile ([X-O31CS]), FD a intervallo derivato altrove (C44 — card non stampata qui:
aggiudicazione wave-3 2026-08-20 enum MIXED, choice_ledger:622-631,
owner F2-C44-FDSTEP, finestra F2 [C1 F-13]) | il principio è lo stesso: l'intervallo è un output derivato, non un input magico |
| stima d'errore sul funzionale | DWR: `wanted_becker_rannacher_2001`, `wanted_fidkowski_darmofal_2011`; GCI: `wanted_roache_gci_1994_1997`, `wanted_celik_2008` | disciplina R5: tolleranze DERIVATE + test che RIGETTANO (rejector), bande per canale con fisica nominata (CH3 §1.3) | vedi CARD J/2 — R5 come legge di certificato, DWR complemento nominato |
| verifica del gradiente | `zahr_persson_2016` (gradient verification sotto periodicità) | O3.1 identità dot-product al floor macchina + [X-O31CS] primal-independent | l'identità esatta (T-LEMB THEOREM) batte il confronto a tolleranza dove è disponibile |
| verità indipendente | dual-code: GENO-Fortran ([DIR-G0], claims:1184) | O3.4 [X-GENOXC] + regola "cross-code agreement ≠ truth" (sotto, §7(b)) | vedi CARD J/1 |

**DECISION CARD (formato §1g dell'emendamento, 6 campi):**

**CARD J/1 — dual-code independent reference**
1. *Scelta*: [DIR-G0] (claims_registry.yaml:1184) — stack JAX primario +
   GENO-Fortran come riferimento dual-code indipendente, oracolo O3.4.
2. *Alternative censite*: dossier G0 `docs/rde_nozzle_G0_decision.md`,
   survey del 2026-07-17 (S10), perimetro = stack differenziabili della
   tool matrix D6 §4: Julia+Enzyme (alternate dichiarata), Tapenade
   (fallback).
3. *Verdetto + perché*: JAX primario (O3.1 a precisione macchina su
   52/52 spikes, X-G0/X-G0AX; solve del singolo unit process ~322
   µs/call, solve+grad ~327 µs = overhead adjoint ~1.5%,
   G0_decision.md §(ii) — caveat di record: i µs assoluti sono
   host-dependent e "do NOT constitute a record timing" [C1 F-11]) +
   GENO mai modificato come referee cross-code ([X-GENOXC] PASS leg
   flowfield, entrambi i negative control rigettano).
4. *Recency/SOTA check*: censimento stack datato 2026-07-17;
   **STALE → finestra F2-entry** (cluster di ri-esame C58 delta-sweep vs
   landscape 2026 + card C31/engine con Uno, emendamento §1g; il ruolo
   dual-code di GENO non è in discussione, il censimento stack sì).
5. *Falsificatore*: loop-speed falsifier di D6 (loop A1 impraticabile a
   mesh di produzione ⇒ flip a Julia+Enzyme); X-GENOXC negative control.
6. *Trigger di ri-esame*: F2-entry (finestra nominata di record).

**CARD J/2 — legge di certificato dei numeri: R5 vs DWR/GCI**
1. *Scelta*: disciplina R5 (tolleranze derivate + rejector; CLAUDE.md
   R5) come legge di certificato — NON una riga del choice ledger
   (governance di repo); righe ledger adiacenti: C9/C11 (stima d'errore
   e spacing, choice_ledger.yaml).
2. *Alternative censite*: PANEL_C9C11.md, survey del 2026-08-19, wave-1
   S-FOUNDATIONS-C: DWR goal-oriented
   (`wanted_becker_rannacher_2001`, `wanted_fidkowski_darmofal_2011`),
   GCI (`wanted_roache_gci_1994_1997`, `wanted_celik_2008`).
3. *Verdetto + perché*: R5 resta la legge del certificato (le bande sono
   derivate per canale con fisica nominata, e ogni banda ha un test che
   può sparare); DWR = complemento ADOTTATO in ruolo nominato
   (fit-vs-capture boundary = DWR-budget policy via campagna C11 leg (b),
   choice_ledger.yaml:692; equidistribuzione A36 log-weighted DWR come
   legge statica adottata, C9).
4. *Recency/SOTA check*: il canone error-estimation censito (2001-2011 +
   GCI codificato anni '90) è lo standard stabile del campo CFD;
   **ATTUALE(perimetro: error-estimation goal-oriented + V&V journal
   practice, data-check 2026-08-23)**.
5. *Falsificatore*: una banda "derivata" che non può rigettare (rejector
   vacuo) — il falsificatore HA sparato una volta:
   `audit-scert:h4-doctored-rejector-vacuous` (findings:1553), riga a
   registro, owner F2.
6. *Trigger di ri-esame*: campagna C11 leg (b) in F2 (finestra F2).

**CARD J/3 — governance di staleness (la card il cui falsificatore ha
sparato)**
1. *Scelta*: staleness link git-backed + tier ONDEMAND registry-driven —
   non riga ledger (governance di suite); riga findings di adozione:
   `test-suite:ondemand-carrier-exclusion` DISCHARGED (findings:257-264,
   commit 32459ca).
2. *Alternative censite*: aggiudicazione tier S25/C4, survey del
   2026-08-13 (memoria s25-engine-speed): re-run integrale in CI vs
   link git-backed vs nessun gate.
3. *Verdetto + perché*: link git-backed adottato (costo ~zero, 4°
   rejector seminato) — POI FALSIFICATO-IN-PARTE da S-CERT: cieco a
   import-closure/env e a edit tracked-but-uncommitted (P0#3).
4. *Recency/SOTA check*: survey 2026-08-13, perimetro = solo file-level
   staleness; **STALE → finestra F2** (la fix family
   `audit-scert:staleness-import-closure-blind` +
   `future-pass-dates-accepted` riapre la scelta a F2 entry).
5. *Falsificatore*: un carrier "fresh" con numeri di record che non
   riproducono — **SPARATO**: X-CDKAT −13.9% con stamp intatto
   (findings:1511, riga carrier-evidence :1517).
6. *Trigger di ri-esame*: F2 entry (owner F2, righe findings:1508/1562).

### (a-bis) IL METODO COME STRUMENTO — governance theory-as-code (cella P-ii, [V2-R12])

La stessa disciplina che certifica i numeri è applicata alla TEORIA. I
registri tipizzati (claims/findings/choice/flag, SCAFFOLD §6 REGISTRY
MAP) portano schema con classe, scope, inherits, carrier, falsifier per
OGNI oggetto teorico (SCAFFOLD §2, docs/rde_nozzle_SCAFFOLD.md:68-95); il
CLAIM LINT committato "(c) REJECTS on any violation. The theory then
cannot silently drift from its index — the same rejector discipline the
numbers already have" (SCAFFOLD:93-95); e in §5 la lista di ciò che è
**machine-rejected**: "class inflation, orphan claims, silent
gamma=const, missing falsifiers are all MACHINE-REJECTED"
(SCAFFOLD:198-200). S-CERT ha verificato i rejector di questo strato COL
FUOCO: 4 famiglie di lint + 9 claim id verificati con rejector che
sparano, due su drift reale in-flight DURANTE l'audit (MC3,
PROGRESS_2026-08-13_Scert.md).

Posizionamento sugli assi della conformity map (design v2 §C):

- **Asse §C-3 (classe ECSS / DO-178C — bidirectional trace)**: la catena
  id→nodo→verifica (ogni claim load-bearing ha id nei registri, una casa
  nell'albero, un carrier con rejector) è la nostra istanza della
  disciplina di trace bidirezionale; i lint (xv)/(xix)/(xx)/(xxii)/(xxiii)
  sono i trace-lint machine-checked. Divergenza dichiarata (dalla mappa
  §C): nessun audit esterno né certificazione DI standard — adottiamo la
  CLASSE di disciplina, claim query-bounded.
- **Asse §C-4 (docs-as-code / Diátaxis)**: registri YAML machine-linted
  = reference normativa; atlas = explanation mai normativa contro M0;
  storia append-only (SR-10). Divergenza dichiarata: Diátaxis come mappa
  dei ruoli-documento, non come rito dei 4 quadranti.

La proposta della cella P-iv (dual-proof + riderivazione cieca +
refutazione simmetrica come modo di lavorare) è co-firmata da questo
capitolo e dal template §6: la sua istanza massima è precisamente S-CERT
— il metodo che si lascia auditare e perde, a registro.

### (b) SENSO — il gap che il nodo occupa, query-bounded

**Query di nodo (cella J-iii, [V2-R10]; protocollo bounded G-11 —
perimetro CHIUSO, STOP, nessun procurement):**

> q_J3: "Esiste, nel perimetro letto (registry 174 id — conteggio da
> `grep -c '^- id:' docs/literature_registry.yaml` in finestra — +
> docs/rde_nozzle_literature_map.md + i 4 paper P-A..P-D letti
> integralmente), un paper di DESIGN di ugelli RDE che consegni il
> proprio claim di performance con una catena di verifica dichiarata —
> oracolo indipendente, tolleranze/barre derivate, o un test capace di
> RIGETTARE — oltre il confronto singolo CFD-vs-CFD o
> CFD-vs-esperimento?"

Esecuzione in finestra: grep
`grid convergence|verification|V&V|uncertainty quant|error bar|certif`
su literature_registry.yaml e rde_nozzle_literature_map.md + walk delle
righe P-A..P-D e del threat ledger CH5. **Esito: NOT-FOUND(q_J3)** sul
campo RDE-nozzle. I hit esistenti NON soddisfano q_J3, ciascuno per
ragione dichiarata: (i) `hoffman_1967` (E-residual) e
`kraiko_tillyaeva_2015` (certificati Route B→A) = corpus CLASSICO, non
RDE, e certificato singolo senza catena/veto; (ii)
`wanted_fidkowski_darmofal_2011` / `wanted_roache_gci_1994_1997` /
`ancourt_peter_atinault_2023` (ACE residuals as code verification,
registry:223) = righe
del NOSTRO censimento strumenti (PANEL_C9C11), non pratica dei paper
RDE-nozzle; (iii) i "nearest referee-shaped pairs" del campo (P-B
Fig. 15, P-C Figg. 13+20b) squalificati con le due ragioni CT-3 (compagno
mediato globalmente; verità same-family URANS). STOP — nessun
procurement in-onda.

**Il principio: cross-code agreement ≠ truth** (direttiva standing,
memoria moc-critical, verificata su file in finestra). L'accordo col
dual-code GENO è consistenza, non verità: un bug specchiato produce
errori CORRELATI che la banda cross-code non vede. Perciò i claim di
verità poggiano su invarianti GENO-INDIPENDENTI, ciascuno con carrier a
registro:

- **O3.1** esattezza del trasposto — T-LEMB THEOREM
  (claims:485-497) + [X-O31CS] primal-independent (claims:1940-1946);
- **certificazione per-cella** del Newton di march — [X-TOCV]
  (claims:1253: "adaptive record with per-cell certification");
- **invarianti strutturali thermo** — [X-THC1] (claims:1206: cp = dh/dT,
  G > 0, roundtrip);
- **bench O3.3** pre-registrato (residui di compatibilità L-P su campo
  NOSTRO) — [X-O33B] (claims:1276): per costruzione l'oracolo
  GENO-indipendente dove un bug specchiato condiviso emergerebbe.

### (c) STANDARD DI RIFERIMENTO

L'asse che governa questo nodo è **§C-3 (classe ECSS/DO-178C,
tracciabilità bidirezionale requirement↔verification)**: il criterio di
conformità è la catena id→nodo→carrier-con-rejector; la divergenza
dichiarata è l'assenza di audit esterno di standard (la classe di
disciplina è adottata, la certificazione DI standard no — claim
query-bounded, mai "compliance"). Per lo strato di verifica avversaria
il nodo cita anche l'asse **§C-7** (peer-review avversaria interna, con
divergenza dichiarata: il reviewer esterno resta G5/JPP, dichiarato non
sostituito). Il sotto-strato theory-as-code (a-bis) aggiunge l'asse
**§C-4** con la sua divergenza dichiarata.

==============================================================================
## §8 DOMANDE DA PANEL

**D1. "Il vostro audit dice NON-CERTIFICABILE. Perché dovremmo fidarci di
un tool bocciato dal suo stesso audit?"**
R. È l'inverso: un audit interno che non ha mai bocciato nulla non
distingue una catena sana da una vacua. Il verdetto ha TRE proprietà che
lo rendono evidenza pro, non contro: (i) è a doppia direzione — il
dual-seed ha rifiutato il canary E confermato il known-true, quindi il
NO non è rumore (PROGRESS_2026-08-13_Scert.md, P0#1); (ii) è
quantificato — 2 P0 nominati, uno riparato nella stessa finestra, l'altro
con owner F2 e carrier-evidence (X-CDKAT); (iii) è progressivo — il
delta vs l'audit 2026-08-07 mostra l'intero tier P0 vecchio consumato e i
difetti migrati dall'oggetto al certificatore. Ancora: sezione DELTA del
log S-CERT.

**D2. "Che cosa distingue i vostri oracoli da un test di regressione?"**
R. Tre cose: l'identità (O3.1 verifica un'uguaglianza esatta, T-LEMB
THEOREM, non una tolleranza empirica); l'indipendenza ([X-O31CS] è un
twin primal-independent con complex-step, non un replay; O3.4 è un altro
codice, in un altro linguaggio, mai modificato); il potere di veto (G1 è
un gate sul lavoro, D6:775 — un rosso ferma la scienza, non apre un
ticket).

**D3. "L'accordo con GENO non basta come validazione?"**
R. No, per principio dichiarato: cross-code agreement ≠ truth — un bug
specchiato dà errori correlati. La verità poggia sugli invarianti
GENO-indipendenti (§7(b)): identità del trasposto, certificazione
per-cella, invarianti thermo, bench O3.3 su campo nostro. GENO è un
referee addizionale, non la sorgente di verità.

**D4. "Chi certifica il certificatore?"**
R. L'audit del certificatore è esattamente ciò che S-CERT ha eseguito
(find→verify avversario, due passate, judge finale): la prima passata ha
RIFIUTATO di certificarsi su un verification layer rotto; la seconda ha
provato il layer (dual-seed dedicato) e mantenuto il NO sul merito. Il
regresso si ferma su un fatto meccanico: i rejector sparano su drift
reale (2 lo hanno fatto DURANTE l'audit, MC3) e le classi di evasione
trovate sono righe a registro con owner (findings:1535).

**D5. "C-O33 è aperta: il vostro oracolo dei moltiplicatori non passa?"**
R. Formulazione corretta di record: la campagna O3.3 È girata (X-O33B,
criterio primario PASS, f2 constant 9.5e-03); l'aperto è il residuo
DESIGN-CLASS della riga corner — quantificato, non un guasto del motore
(claims:197-205). La riga è una conditional SCHEMA dichiarata con owner
F2 e riformulazione margin-constrained in M0 Parte VI. Non viene
presentata come passata: viene presentata come aperta e prezzata.

**D6. "Quanto della catena sopravvive su un motore vero (dati sporchi)?"**
R. Domanda del nodo N-K (CH10): il contratto-dati con audit stage-A e
G6 loud-reject è il pezzo di catena rivolto ai dati; qui vale il
principio: il tool rifiuta rumorosamente dataset fuori classe invece di
certificare in silenzio (D6 G6). Stage di evidenza dichiarato (guardia
7): il loud-reject è verified su dataset sintetici, non ancora validated
su dataset motore reale — owner F2/G6.

**D7. "Perché fitted e non captured, se il mondo cattura?"**
R. Per un teorema negativo altrui e un'aggiudicazione nostra:
`giles_ulbrich_2010_part1`/`_part2` mostrano che l'adjoint discreto su
shock catturati può convergere male (scope 1-D scalare dichiarato); la
card C49 (choice_ledger.yaml:682-692, wave-2 2026-08-19, zero finding
del refuter; card estesa nell'atlas: CH4 §(c) C49 + tabella scelte riga
C49, falsificatori pinnati e carrier |J_capture − J_fitted| [C1 F-14])
fissa: fitted = unico certificate bearer, captured =
explorer nominato build-gated, shock tracking implicito = upgrade path
con entry gate pubblicato.

==============================================================================
## DECK FEED (asserzioni candidate-slide; frase piena + ancora + classe)

1. "La nostra catena di certificazione ha già detto NO a noi stessi: il
   verdetto d'audit di record è NON-CERTIFICABILE, con i due difetti
   nominati, un owner e una data — questo è il falsificatore vivo, non un
   incidente." — PROGRESS_2026-08-13_Scert.md SESSION VERDICT — verdetto
   d'audit di record.
2. "Nessun risultato lascia il tool fuori da un Verdict: contorno,
   certificati, barre derivate e record oracoli viaggiano insieme al
   numero." — D6:679-681 + CLAUDE.md R5 — PRACTICE di prodotto.
3. "Il gate G1 è assoluto: oracoli O1/O2/O3 verdi o nessuna scienza a
   valle — un gate sul lavoro, non sulla pubblicazione." — D6:775 —
   governance di gate.
4. "Il gradiente non è approssimato: il reverse-AD del march fitted È lo
   sweep adjoint trasposto (THEOREM in dimensione finita), e O3.1
   verifica quell'identità al floor macchina." — T-LEMB,
   claims_registry.yaml:485-497 — THEOREM (limite mesh separato, SCHEMA
   S-LBML).
5. "Abbiamo costruito il modo in cui il nostro self-check poteva mentire
   — coppie transpose-consistent-but-wrong — lo abbiamo esibito con un
   negative control e chiuso con un twin primal-independent." —
   [X-O31CS], claims:1940-1946 — carrier PRACTICE, coverage interior
   dichiarata.
6. "L'accordo tra i nostri due codici non è verità: i claim poggiano su
   invarianti GENO-indipendenti — identità del trasposto, certificazione
   per-cella, invarianti thermo, bench O3.3 su campo nostro." — memoria
   moc-critical + carrier claims:1253/:1206/:1276 — principio standing
   con carrier.
7. "Ogni audit passa solo se conferma il vero E rifiuta il falso: il
   dual-seed ha rifiutato il canary e confermato il known-true prima che
   il verdetto contasse." — PROGRESS_2026-08-13_Scert.md P0#1 —
   protocollo d'audit di record.
8. "Nel campo RDE-nozzle nessun metodo di design pubblicato consegna il
   design dentro una catena di verifica che possa rigettare: esito
   NOT-FOUND della query dichiarata sul perimetro letto (174 id + litmap
   + P-A..P-D)." — §7(b) q_J3 — claim query-bounded (guardia 9).
9. "La stessa disciplina governa la teoria: classi gonfiate, claim
   orfani, falsificatori mancanti sono machine-rejected dai lint dei
   registri — e due rejector hanno sparato su drift reale durante
   l'audit." — SCAFFOLD:198-200 + MC3 — governance theory-as-code,
   asse §C-3/§C-4.
10. "Il progresso tra i due audit è misurabile: i difetti del 2026-08-07
    stavano nell'oggetto certificato, quelli del 2026-08-13 nel
    certificatore — il pavimento è salito, e il tetto ha lo stesso
    trattamento in coda a F2." — PROGRESS_2026-08-13_Scert.md DELTA —
    verdetto di livello del final judge.
