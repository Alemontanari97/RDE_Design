# PROGRESS — cycle-averaged variational nozzle program (living state)

> Single source of truth della progressione. Aggiornare a OGNI chiusura
> di sessione/fase (CLAUDE.md R3). PROTOCOLLO DI APERTURA (dalla S10,
> ordine S9): memoria di progetto + L0 (SCAFFOLD §1: obiettivo e
> regole) + docs/claims_registry.yaml (l'INDICE della teoria, lintato
> dal gruppo (xv)) + D6 (stati/gate) + questo file. M0 resta il master
> del proof layer, letto per profondità, non per ricostruire lo stato.

## ORA (2026-08-11, chiusura Sessione 22 — **F1 "GOVERNOR + P-2
## CAPTURE", sessione 1: O4 SCARICATA per l'istanza S20 (ramo (c)
## UNANIME — meccanismo NON-FOLD, entrambe le letture del standoff
## FALSIFICATE), il falsificatore del bridge K_disc~A_0 SPARA,
## governor [X-MGOV] costruito/derivato/rejector-provato, campagna
## decisiva A' 1/2 ESEGUITA = certifiability-limited-under-constraint
## con margine INATTIVO (predizione pre-registrata TENUTA, stop per
## monotonia)**; log: validation/PROGRESS_2026-08-11_S22_governor.md,
## 8 passi; gate PASS al passo 2)

**CONTATORE F1 (ISS-5, obbligatorio): F1 campaign 1/2, session 1/3.**

Branch `rde-nozzle-program`. Commit: apertura+gate+T0+T1 = aec2c9f,
T2+T3 = 0174bb9, chiusura = (questo). Lint (xv) verde sull'EXIT CODE
a ogni commit (129 -> 131: +[X-LOCD], +[X-MGOV]). Suite di chiusura
nel log passo 8 (carrier-esclusiva per l'annotazione C4 di record;
i carrier on-demand esercitati in sessione con run diretti:
[X-A1IM] exit 0, [X-LOCD] exit 0, [X-MGOV] derive exit 0 +
campaign exit 0).

- **[F1] T0 DECISIONE UTENTE (2026-08-11)**: sgancio P-2 = opzione
  (b) DEFAULT RATIFICATO (freeze a trigger datato a chiusura F1);
  opzione (a) declinata. BLOCCATO-4 chiusa.
- **[F1] T1 IGIENE con FINDING**: il bookkeeping S21 C2-F4 (me_gap)
  rompeva la vjp S6 di [X-A1IM] (float su tracer) — fix
  tracer-guarded, main FULL PASS end-to-end; righe S2 exit_cap / S6
  CERT_PLAY verificate CAPACI di rigettare (STIM-1 indurito a
  m_stop=0, STIM-2 a cap 0 spara a 5.4e+07, controlli tengono).
- **[F1] T2 RETRO-DIAGNOSI S20 = O4 SCARICATA, ramo (c) 5/5**:
  camminata rigenerata DETERMINISTICAMENTE (firma {1.170, 2.458x4,
  1.060, 1.455, 1.698}, artefatto bit-identico); campo val SANO su
  tutti i design rigettati (min 0.612-0.620 vs soglia 0.172; celle
  failing a val 0.65-0.86, zona NEAR-AXIS colonne 23-30) => lettura
  DEF **e** caustica interna FALSIFICATE per l'istanza; meccanismo =
  COSTRUZIONE DI CLASSE (identificazione = owner F2); **il
  falsificatore del bridge K_disc~A_0 SPARA** (bd(K) qui è
  numerico-di-classe, NON il confine di validità fisico) — la
  congettura come formulata è morta, regola nuova: ogni claim di
  bridge richiede il test per-istanza. RT-1 risolto: lo standoff era
  un artefatto di classe. Carrier [X-LOCD] (KAT-CLS 5/5, BASE-CTRL,
  determinismo PASS).
- **[F1] T3 DERIVAZIONI PRE-RUN TUTTE SCARICATE ([X-MGOV] derive
  FULL PASS)**: margine KS su campo val tracciato (val_diag
  additivo), rho DERIVATO = K_RICH ln(N)/mu0_min = 766.83 (N=3498,
  m_ref=0.6810298), scala mu0 = m_ref/2^k pre-registrata;
  G1-SURROGATO REJECTOR-PROVATO (finito-negativo -3.96e+02 al
  design rotto, gradiente zeroed+counted, camminata vincolata corta
  recuperata senza stallo) — duty tier-invariant F1 SCARICATO;
  metrica [D1]-VINCOLATA derivata (corollario del KKT col
  moltiplicatore); bande magic GENO derivate contro ricetta
  SOURCE-VERIFIED (Rao_m.f90: FD centrale dV_pert=1.0; FD in banda
  a 0.371; den-guard NON può mordere in-range); survey KS adattiva
  adopt-or-declare (adottato KS standard con rho derivato).
- **[F1] T4 CAMPAGNA A' 1/2 = BRANCH ADJUDICATED**: dal base
  outcome-II, rung più stretto mu0=0.3405: 7 rejection (worst
  1.531, un sesto design di frontiera), ratchet al floor, EXHAUSTED
  -> **certifiability-limited-under-constraint** (uscita VALIDA
  dichiarata del gate F1) con MARGINE INATTIVO (censimento cuspidi
  attive: 0 lane, 0 cluster; min val 0.6186 interno; contatori
  nonfiniti 0/0) — predizione pre-registrata TENUTA, falsificatore
  non sparato; STOP PER MONOTONIA: rung 2-4 vacui, mu = 0
  identicamente (RT-4 sign test banale); [D1] non licenziata (no
  outcome-I) => [C-O33] resta APERTA-QUANTIFICATA. Dual-proof
  completa sul claim centrale (il governor non cattura QUESTA
  frontiera): derivazione + campagna eseguita. 498 s (anchor ok).
- **NEXT-1 (S23) = DECISIONE UTENTE: CHIUSURA ANTICIPATA DI F1**
  (vedi BLOCCATO 6). Le condizioni di uscita F1 sono RAGGIUNTE
  (branch valido + locus classificato + logs obbligatori); una 2a
  campagna è misurabilmente VACUA (monotonia). La chiusura fa
  scattare il freeze P-2 datato PER REGOLA e richiede
  l'aggiudicazione della riga BLOCKER C1 del freeze (rejector
  field-level, carrier unbuilt, owner F2 — S21 passo 6): freeze con
  conditional dichiarata nel paper vs attesa F2. In coda dopo: F1b
  (twin DEF, conditional esterna GENO), F2 (motore generale — ORA
  ANCHE owner dell'identificazione del meccanismo near-axis di
  classe trovato da T2), U3' [F2a], residui S19 (b)/(c)/(d),
  census-lemma, PAP-RIM, review G0/T2.

STATO BLOCCATO / LOCK UTENTE (aggiornati 2026-08-11, chiusura S22):
 1. **G5 (decisione time-boxed)**: pendente dal 2026-07-17 — invio
    del dispatch (validation/G5_dispatch_email.md) dall'account
    istituzionale + canale di fallback; blocca SOLO le submission.
 2. **Acquisizioni (F0 dispatch)**: Sternin 1962; Shmyglevskii 1981
    (gate O3); Giles-Ulbrich SINUM 2010 x2; Lozano 2019 (entry
    F4b); Moretti/Salas CONDIZIONALE; residuo fetch AIAA 2019-0197.
 3. **Decisione preprint/arXiv**: raccomandazione invariata (armare
    il trigger); la decisione resta all'utente.
 4. **SGANCIO P-2 (ISS-2): CHIUSA 2026-08-11** — decisione utente =
    (b) default ratificato (trigger datato a chiusura F1).
 5. **DISPATCH GENO (protocollo SUO, sessione separata, MAI da
    qui)**: flagdef KAT + un caso di regressione DEF; conditional
    esterna nominata del gate F1b. NOTA S22: [X-MGOV] fornisce
    anche la BANDA derivata per la leg di cross-check (dV_pert).
 6. **NUOVO — CHIUSURA ANTICIPATA F1 (decisione utente, S23)**:
    uscita F1 raggiunta alla campagna 1/2 (branch
    certifiability-limited-under-constraint + evidenza di
    localizzazione); 2a campagna vacua per monotonia. Se si chiude:
    freeze P-2 datato PER REGOLA (contenuto = two-knob S19) +
    aggiudicazione della riga BLOCKER C1 (freeze con conditional
    dichiarata vs attesa del carrier F2). Se non si chiude: budget
    F1 resta (session 2-3/3) ma senza contenuto decisivo nominato.
 7. **NOTA ALBERO (S22)**: tre advisory untracked NUOVE atterrate
    inter-sessione, NON ingerite (fuori mandato):
    ADVISORY_Scollapse_prompt_2026-08-11,
    ADVISORY_Sgauntlet_prompt_2026-08-11,
    ADVISORY_mean_swirl_panel_2026-08-11 — ownership da assegnare.

**[PIANO/S-GAUNTLET] SESSIONE PARALLELA ASSORBITA (2026-08-11,
stesso giorno di S22, chiusura in-sessione su ordine utente).**
Audit avversariale di generalita totale (due workflow: verticale
collasso 17 agenti + gauntlet orizzontale 22 agenti, entrambi con
red-team Form-3 + verifica di assorbimento a workflow; log
validation/PROGRESS_2026-08-11_Sgauntlet.md). VERDETTO: il piano
risponde positivamente — ledger 14 [M] / 3 [B] / 6 [S] / 11 [G],
lista [G] interamente convertita in duty ratificati (D6 §0-pre
addendum S-GAUNTLET). Claim di coincidenza generale ciclo-vs-steady
RIFIUTATA come teorema generale, PROVATA sull'angolo tier-1+vuoto:
M0 [T-T3-SI] (tier-1 THEOREM, pin Gibbs) + [T-T3-MAP] (5 breaker) +
PROTOCOL T3-CONTROL pre-registrato; registry 131 -> 133 (+T-T3-SI,
+T-T3-MAP), lint (xv) verde. PIN UTENTE di record: P1 termo =
miscela termicamente perfetta a composizione FROZEN (gamma(T)
libero); P2 niente bifase per ora; P3 anti-divergenza. Correzioni:
scope T-T3 ("EOS-general" era un'inflazione), eco P1 sections 2-4,
choking advisory 2-ter(a) (verdetto sea-level = "coincides at
<Pc>_mu" sotto la lista T-O1, non "no coincidence"). NOTA per S23:
il duty F1-window DUTY-6(i) (tolerance-ball backoff sul floor del
margine) tocca la linea del governor — da considerare alla
decisione di early-close F1.

Stato precedente (chiusura Sessione 21 — **F0 "ORDER +
INSTRUMENTATION" del piano v3 RATIFICATO: P0 chiusi con rejector,
certdiag KAT retro-valida il verdetto S20, bench o33 riparato e
FULL PASS, addendum utente (red-team + use-case + choking U3')
eseguito, EQ-v2/Λ-form/ledger a registro col footing corretto,
strumentazione ARMATA**; log:
validation/PROGRESS_2026-08-11_S21_order.md, 8 passi; gate PASS
al passo 2)

Branch `rde-nozzle-program`. Commit: apertura+gate = e73f370,
ratifica T1 = 0dd0d69, addendum = 7decfec, T2/T3-carrier = 89c3400,
T3/T4/T5 = ba5f1cf, chiusura = (questo). Lint (xv) verde sull'EXIT
CODE a ogni commit (125 -> 129: +[X-CDKAT], +[X-VMON], +[T-LFEQ4],
+[C-EQV2]). Suite --fast di chiusura nel log passo 8. NOTA C4 di
record: "suite verde = carrier-esclusiva" (annotazione onesta in
run_all.py; chiusura meccanica = riga schedulata F1).

- **[F0] T1 RATIFICA**: piano v3 in D6 §0-pre (indice di lavoro
  F0-F6; tabella G-gates→F senza perdite; tassonomia fronti con (a)
  = EQ-v2 convergente e (c) governor HOMENTROPIC-SCOPED fino a F2;
  CLAUSOLA TIER-INVARIANT vincolante: REQ-NONSTALL + G1-surrogato +
  duty di transizione).
- **[F0] ADDENDUM UTENTE (datato 2026-08-11) ESEGUITO**: correzioni
  red-team PRIMA dell'assorbimento (RT-1 consistent-with; RT-2 lembi
  S1 divisi; RT-3 H7-SEL; RT-4 mu = SIGN TEST); tre aggiudicazioni
  obbligatorie (contact/slip → F2a/F4b; o32 RI-AGGIUDICATO: riga
  obiettivo NON-CONCLUSIVA sotto il cap pre-registrato 0.5, claim
  non ucciso; totali audit corretti 82/13/12 e re-triage dei 13
  high COMPLETO); budget per fase istanziati; freeze P-2 checkable;
  flagdef = conditional esterna nominata; F3<->F4b interscambiabili;
  U1-U3 + U3' (choking RDE, PREMISE-OPEN, owner F2a) assorbiti.
- **[F0] T2 P0 CHIUSI CON REJECTOR**: C2 cert-stack (NaN→reject nei
  due certify + metric inf nel Newton; replay cert_diag sul jit TOC
  + CERT_PLAY su A1 con righe di verdetto nuove; contatori
  nonfiniti verdict-bearing nel driver; exit_cap distinto e
  riportato); [X-CDKAT] KAT PASS: la manopola N_NEWTON MORDE
  (2.1e-01 → 2.3e+05 a cap 3), bit-identica a cap 300, rejector
  replay spara a 6.1e+08 su seed stantii → **verdetto S20 8/8
  GENUINE RETRO-VALIDATO**; bench [X-O33B] riparato (bug di restore
  che rendeva ineseguibile ogni stadio dopo R7) e RI-ESEGUITO FULL
  PASS: f2 drift 9.4809e-03 in NORMA REGISTRATA (S19 confermato),
  banda DERIVATA 1.8696e-02 al posto del letterale 0.03 (con
  controllo negativo che spara), dato onesto: il drift CRESCE col
  mesh (9.5e-03 → 1.4e-02) = attribuzione classe-di-design
  corroborata.
- **[F0] T4 R4**: M0 Parte VI [S21 REGISTRATION BLOCK] — EQ-v2 al
  footing corretto (A/B CONJECTURE sotto H1-H6+H7-SEL, S4 THEOREM,
  lembi S1, standoff = consistent-with), Λ-form coi DUE bound
  (EOS-general MA NON data-general → estensione F2), lambda_e =
  dJ/dy_lip, traduzione Rao-vs-Zucrow, ledger O1-O5+G1 con owner
  di fase. Registry: [C-EQV2], [T-LFEQ4], [X-VMON].
- **[F0] T5 STRUMENTAZIONE ARMATA**: argmax/argmin-cell nel cert
  dict (additiva, default-off, env A1_CERT_ARGMAX); persistenza dei
  design RIGETTATI nel driver (result dict + A1_REJ_SAVE); monitor
  di validità [X-VMON] con KAT γ=1.4 PASS (identità al floor,
  2.7e-13 vs banda 1.1e-12; conferma viva del clamp F3 fuori box,
  riga P2). Retro-diagnosi del design S20 → riga F1-entry (tag di
  fase, non consumata qui).
- **NEXT-1 = F1 (governor + P-2 capture)**: entry gates = bande
  derivate delle magic di implementazione + variante [D1] vincolata
  PRIMA del run decisivo + monitor lungo la camminata; contatore di
  budget "F1 campaign k/2, session m/3" in ORA a ogni chiusura;
  freeze P-2 a trigger DATATO (default two-knob S19). In coda F1b
  (twin DEF; leg 1 sotto conditional esterna GENO). PRIMA di F1:
  decisione utente sullo SGANCIO P-2 (vedi BLOCCATO).

STATO BLOCCATO / LOCK UTENTE (T6, ri-presentati DATATI 2026-08-11):
 1. **G5 (decisione time-boxed)**: pendente dal 2026-07-17 — invio
    del dispatch (validation/G5_dispatch_email.md) dall'account
    istituzionale + canale di fallback; blocca SOLO le submission.
 2. **Acquisizioni (F0 dispatch)**: Sternin 1962; Shmyglevskii 1981
    (gate O3); Giles-Ulbrich SINUM 2010 x2; Lozano 2019 (entry
    F4b); Moretti/Salas CONDIZIONALE. Addendum D: AIAA 2019-0197
    (residuo — Harroun JPP 37(5) 2021 già letto 14/14 pp
    nell'advisory choking atterrato in sessione; page-verify
    formale al consumo F2a).
 3. **Decisione preprint/arXiv**: raccomandazione invariata (armare
    il trigger); la decisione resta all'utente.
 4. **NUOVO — SGANCIO P-2 (ISS-2, decisione utente)**: freeze a
    F0+1 a qualità fallback (two-knob S19) SGANCIATO dal governor,
    vs il default ratificato (trigger datato a chiusura F1). Da
    decidere all'apertura della prossima sessione.
 5. **DISPATCH GENO (protocollo SUO, sessione separata, MAI da
    qui)**: flagdef KAT (boundaryfunction_solve vs Eq.(4) chiusa,
    γ=1.4 sintetico — [X-VMON] fornisce il riferimento) + un caso
    di regressione DEF; conditional esterna nominata del gate F1b.

Stato precedente (chiusura Sessione 20 — CLASSE ADATTIVA [X-AKNO],
tentativo di scarico di [C-O33]: **OSTRUITO AL CONFINE DI
CERTIFICABILITÀ — [D1] NON TESTABILE, C-O33 NÉ SCARICATA NÉ
FALSIFICATA; gap di formulazione aggiudicato + formalizzazione
generale a registro**; log a ordine totale:
validation/PROGRESS_2026-08-07_S20_adaptive.md, 10 passi; gate
PASS al passo 2. NOTA S21: il verdetto certdiag 8/8 GENUINE è stato
RETRO-VALIDATO da [X-CDKAT]; la lettura "predicted signature DEF" è
riformulata di record in "consistent-with fino a O4" — red-team.)

Branch `rde-nozzle-program`. Commit: apertura+gate = f2be862, survey
T1 = 7cfb49b, carrier+knob+wiring = 1d93719, fix P3(ii) = ed84f6e,
fix livelock+outcome-II = cd0e204, audit critico+validity condition
= f33e813, attempt-3+R4 = 5ece8d3, chiusura = (questo). Lint (xv)
verde sull'EXIT CODE a ogni commit (124 -> 125: +[X-AKNO]). Suite
--fast di chiusura nel log passo 10.

- **[F1/P-2][F2/A1] T1 SURVEY + DECISIONE** (adopt-or-declare, in
  D6 item 9): skeleton AFEM/FITPACK (sorgente scipy 1.18 LETTA,
  costanti nascoste trovate e NON adottate); indicatore = drift di
  f2 per segmento via mappa `owner` — aggiudicato DWR-conformant
  (f2 = -lambda2 È la variabile aggiunta); base invariata (U1
  C_geo); free-knot/THB/switch-di-base RIGETTATI con ragioni. GAP
  dichiarato a posteriori (passo 9e): l'indicatore
  gradiente-sui-dof-candidati (progressive parameterization ASO)
  non era nel ventaglio — A/B in coda.
- **[F2/A1] DUE DIFETTI DEL DRIVER trovati e fixati
  policy-conformant** (esercitati dalla classe arricchita, mai da
  quella uniforme): (1) P3(ii) — la certificazione a ogni iterato
  ACCETTATO era nel testo della policy ma non nel codice, e il
  recovery ripartiva dall'iterato fallito; (2) LIVELOCK — lo shrink
  post-rigetto veniva riassorbito dalla ricrescita del raggio di
  scipy (misurato bit-identico, seg 7-17 attempt 2). Ora: ratchet
  monotono del cap + esito dichiarato `certifiability_limited`
  (KKT riportato APERTO) + rifiuto del bench su design non
  [D1]-eligible.
- **[F1/P-2] ATTEMPT 3 DI RECORD (exit 1 per costruzione)**:
  baseline riprodotta esatta (6.6295e-02; indicatore CONCENTRATO,
  41.8% nel primo intervallo dopo l'attacco — prima evidenza
  spaziale diretta della diagnosi S19); 2 knot inseriti (8 -> 10
  dof); J certificato -> **2.7775702e+07** (+1.40e+04 sul J* S18),
  KKT 1.7e+06 -> 3.8e+02; poi **CRAWL lungo la frontiera di
  certificabilità** (cinque design rigettati distinti, certdiag
  8/8 GENUINE con N_NEWTON x10 e floor intatto, margine di
  causalità INVARIATO) => firma di VINCOLO ATTIVO: il KKT della
  formulazione non vincolata non può chiudersi in linea di
  principio. [D1] NON TESTABILE; mismatch corner 6.6826e-02
  stampato SOLO informativo (design non stazionario).
- **[F1/P-2] AGGIUDICAZIONE + CONNESSIONE CLASSICA (page-verified)**:
  Rao-Beck AIAA 94-3264 letto PER INTERO + ramo DEF di GENO letto
  alla sorgente — la zona vietata ha nome classico (il confine di
  Sternin 1962 di esistenza degli ugelli ottimi shock-free; Eq. (4)
  = forma chiusa al giunto; la loro Eq. (1) È il nostro f2); DEF =
  compressione PM che coalesce ESATTAMENTE sulla superficie di
  controllo (urto interno di estensione zero, urti solo a valle
  del dominio). Sternin/Shmyglevskii citati SOLO via Rao-Beck
  (acquisizione in coda, D6 item 12) — dichiarato.
- **[F1/P-2] FORMALIZZAZIONE GENERALE A REGISTRO (M0 Parte VI,
  classi di rigore dichiarate)**: scala di classi di soluzione
  certificate (S0 shock-free ⊂ S1 fronti fitted), insieme
  ammissibile A_t(mu_0) col vettore di margini, KKT vincolato col
  MOLTIPLICATORE DI MARGINE (il termine mancante — perché
  l'outcome I era impossibile), moltiplicatore = prezzo della
  shock-freeness che decide la transizione di tier (linea G12/F2;
  DEF = caso limite + àncora di validazione). Ancoraggio SOTA:
  tassonomia Le Digabel-Wild (il vincolo oggi è
  Known-Unrelaxable-Simulation-NONQUANTIFIABLE; rimedio = margine
  quantificato), aggregazione KS = standard. Ponte K ↔ A_0 =
  CONGETTURA con falsificatore nominato (monitor Eq. (4)/Sternin
  lungo la camminata).
- **DIRETTIVA UTENTE NUOVA (in memoria,
  `agnostic-milestone-review-directive`)**: check agnostici a
  milestone su committato+non committato, confine rabbit-hole
  nominato in anticipo, un frame alternativo per ogni ostruzione.
  Applicata in sessione (passi 7 e 9).
- **NEXT-1 = DECISIONE UTENTE per S21** tra (ordine incluso):
  (E) strumentazione di localizzazione (argmax cella + posizione)
  + monitor di validità Eq. (4)/Sternin (= il test del ponte);
  (A') ri-ottimizzazione VINCOLATA al margine (fold margin
  KS-aggregato, floor derivato, gradiente AD) con la variante
  vincolata di [D1] derivata PRIMA del run decisivo; A/B
  dell'indicatore candidato; (B) fallback = P-2 coi numeri
  two-knob S19 (sempre disponibile). NIENTE altro lavoro sul
  driver (confine pre-nominato). Poi in coda invariati: residui
  (b)/(c)/(d) S19, census-lemma, PAP-RIM, review G0/T2, panchina
  rigore, G5/preprint (lock utente).

Stato precedente (chiusura Sessione 19 — CAMPAGNA O3.2/O3.3, LA
METÀ NUMERICA DI P-2: **BENCH O3.3 PASS, CRITERIO PRIMARIO
SODDISFATTO**; log a ordine totale:
validation/PROGRESS_2026-08-06_S19_o33.md, 8 passi; gate PASS al
passo 2)

Branch `rde-nozzle-program`. Commit: apertura+gate = 2664f95,
carrier O3.2 + pre-dichiarazioni = 6ea29e3, bench O3.3 = ceae2ae,
verdetto O3.2 = 514e267, R4 + diagnosi = bbde42f, chiusura =
(questo). Lint (xv) verde sull'EXIT CODE a ogni commit (122 -> 124
voci: due nuovi carrier). Suite --fast di chiusura 15/15 in 178 s.

- **[F1/P-2] O3.3 — BENCH PRE-REGISTRATO ESEGUITO, VERDICT PASS**
  (`validation/o33_bench.py`, [X-O33B], exit 0). **CRITERIO DI KILL
  PRIMARIO SODDISFATTO**: sulla famiglia di contorni perturbati
  attorno all'ottimo, la derivata direzionale AD e il residuo di Rao
  si annullano sullo STESSO design — |t_grad - t_Rao| = 6.80e-03
  contro barra derivata 3.56e-02, e il drift di f2 è una V pulita
  col minimo dove il gradiente si annulla. f2 = -lambda2 costante
  sulla superficie di controllo a **9.48e-03** (nostro ottimo S18) e
  **7.99e-03** (contorno Rao di GENO marciato dal NOSTRO motore); le
  due COSTANTI di Rao concordano a **2.42e-04** e la lettura di
  trasversalità al labbro a **2.80e-03** — il residuo è la
  discretizzazione dell'istanza, comune ai due design. Compatibilità
  aggiunta: cancella a 1.65e-04 (C+) e 2.34e-04 (C-) col segno della
  famiglia, satura a **esattamente 1.0** col segno sbagliato.
  Guardia (33)-(34) eseguibile: RIFIUTA il campo vero, ACCETTA la
  patch uniforme.
- **[F1/P-2] ERRORE DI LOCUS CORRETTO IN SESSIONE (utente)**: la
  superficie di controllo di Rao NON è tutta la C+ per il labbro, ma
  il tratto dall'ULTIMA C- emessa dall'arco di gola (confine del
  nucleo) fino al labbro. Sulla catena intera f2 deriva **2.89e-01**
  e la (ii) sembra falsificata. Entrambi i numeri restano a record.
- **[F1/P-2] O3.2 — ESITO PARZIALE, ONESTO** ([X-O32], exit 1 per
  costruzione: "exit 0 sse TUTTE le righe passano", e non tutte
  concludono). PASSA la riga dell'obiettivo J (p_fine = 2.5347,
  dp_tot = 0.6704, conclusiva). NON CONCLUSIVE: Q_u (limitata dal
  rumore) e il twin ideale. **LA RIGA AGGIUNTA NON È MISURABILE su
  una scala di raffinamento**: le differenze si fermano
  (-2.20e+04, -2.33e+03, -1.94e+03) — meccanismo = clausola LB-c2
  (il limite è a topologia FISSA, e raffinare non la tiene fissa);
  monitor di topologia MISURATO (33/92, 66/183, 99/274, 131/365,
  frazione non monotona con inversione a r=4). Apparato validato dal
  controllo negativo a primo ordine: p = 0.9997 +/- 6e-04, RIGETTATO.
  Sonda al labbro PUNTUALE: p_fine = 0.7630, conclusivamente sotto 2
  => **il pin S14 di esclusione del labbro è empiricamente
  SOSTENUTO**.
- **R4 STESSA SESSIONE**: M0 Parte VI (blocco campagna), P2_lemmaA
  §3.7 (sei voci), P2_outline §5 addendum (cinque voci, nessuna
  banda toccata), LBML §5 (nota EXECUTED su LB-c2), D3, D6 item 9
  (quattro residui in coda con la leva nominata), ledger ipotesi
  (C-O33 con residuo QUANTIFICATO), registro (+[X-O32], +[X-O33B]).
- **[C-O33] RESTA APERTA, ma con numero e causa**: l'identità del
  corner chiude a 6.63e-02 sul design a 8 nodi ed è
  MESH-INDIPENDENTE, a 1.998e-02 su una parete Rao fedele e a
  1.487e-02 lì a r=2 — converge su ENTRAMBI i limiti, non è
  confermabile a banda Richardson su un'istanza finito-dimensionale;
  il termine dominante è la CLASSE DI DESIGN.
- **NEXT-1 = da decidere con l'utente** tra: (a) ri-ottimizzazione
  in classe di design ADATTIVA (costruzione di nodi guidata da
  indicatore d'errore — NON più nodi uniformi) e ri-misura della
  riga corner; (b) gemello lambda3/lunghezza della stessa riga
  (serve L tracciato nel replay); (c) esperimento a TOPOLOGIA FISSA
  per l'esponente dell'aggiunto; (d) estrazione del campo aggiunto
  per iniezione di residuo. Restano in coda: census-lemma, PAP-RIM,
  review G0/T2, panchina rigore.

Stato precedente (chiusura Sessione 18 — PRODUCTION CODE + RUN
END-TO-END: **BRICK 2 CHIUSO, O3.3 SBLOCCATO**; log a ordine
totale: validation/PROGRESS_2026-08-06_S18_brick2run.md, 9 passi;
gate PASS al passo 2)

Branch `rde-nozzle-program`. Commit: apertura+gate = 9ca859a,
P1 = dfb169f, P2 = 85453c3, P3+P4 = a1cd786, run di record =
d1fbdec, R4 = 01c41a6, chiusura = (questo). Lint (xv) verde a ogni
commit (122 voci). Suite --fast di chiusura 15/15 in 100 s.

- **[F2/A1] LEVE DI PRODUZIONE P1-P4 ESEGUITE, OGNI GATE RI-PASSATO**:
  P1 while-Newton sulla metrica di certificazione (X-SCANM 8.9e-16
  invariata); P2 bucket-per-fase + whole-loop jit con guardia
  safe-where (jit==python 6.2e-15 bit-level, compile 4.9 s, O3.1/jit
  4.9e-11 = leak detector pulito; **T2a RI-RUN clean-host PASS:
  t_solve 0.116 s (era 39.8: 343x), grad/solve 1.593 — IL GATE DI
  PRODUZIONE È APERTO**, nota datata G0_decision §4); P3 chiusura C^1
  a due binari (X-THC1 primaria del brick, gap di chiusura 1.0e-07 vs
  banda 5.7e-01 — sette ordini sub-risoluzione; twin GENO resta
  'nasa' lineare); P4 floor di margine d'istanza delta = 0.1202 m/s
  (min_margin(W0)/K_RICH) con rejector + audit sul design finale.
- **[F2/A1] RUN END-TO-END DI RECORD: VERDICT PASS — BRICK 2 CHIUSO**
  (X-TOCV completo, exit 0; 4 tentativi dichiarati nel log, nessun
  numero dai run uccisi): da partenza perturbata 1.5%, TR-SQP sotto
  policy DIR-RKG (segmentazione + Jacobi misurato + HESSIANA PIENA
  MISURATA per base di segmento — clausola R-3 attivata sui numeri)
  converge status 1 con **KKT 7.745e-02 <= tol derivata 1.156e-01 =
  ISTANZA DI TRASVERSALITÀ PASS (le condizioni di Rao raggiunte VIA
  GRADIENTE)**; J* = 2.7761688e+07 (+1.06e+04 sul seed
  GENO-proiettato); **ORACOLO 91/91 in banda derivata cross-code**
  (max|dy| 1.86e-03, mediana err/banda 0.102; termini: cross-res
  GENO + rappresentazione di classe + ricampionamento, inviluppo di
  vicinato); N3 discrimina; audit margine PASS; lettura
  moltiplicatore lambda_eps = 1.055e+07 (Pa implicita 8.40e+05 vs
  p_lip 1.41e+06, ratio 0.595 — istanza per O3.3). **T2 FIRED di
  record** (121.6 s vs 35.9 s; decomposizione = misura di curvatura
  + re-record RK-G, NON throughput di linguaggio — T1/T2a passano
  con margine) => **REVIEW G0 IN CODA** per flip clause D6.
- **[F2/A1] FINDING DI DRIVER di record** (dai tentativi dichiarati):
  flip di wall-search ~1/passo accettato => un segmento = un passo
  produttivo e la curvatura ESTERNA è obbligatoria (fresh-BFGS è
  vincolo di policy); xtol-con-KKT-aperto = collasso da modello
  stantio => continuazione a segmento fresco; patologia degli
  stimatori puntuali |proxy| (zeri isolati) => inviluppo; leve di
  scala NOMINATE nel kickoff doc (regole implicite second'ordine,
  Hessiane colorate/sparse, emendamento flip-benigni).
- **R4 STESSA SESSIONE** (01c41a6): M0 Parte VI "A1 BRICK 2 OF
  RECORD"; D6 item 9 CHIUSO (+G0 review in coda); kickoff doc §5bis
  status completo; registro X-SCANM/X-LSG0/DIR-G0/DIR-RKG
  (carrier=[X-TOCV])/X-TOCV aggiornati.
- **NEXT-1 = CAMPAGNA O3.2/O3.3** (protocollo PRE-REGISTRATO
  P2_outline §5, intatto — la metà numerica di P-2). Poi in coda,
  ordine relativo da decidere: census-lemma session, PAP-RIM (matrice
  strade x inserzioni, pin utente 2026-08-06), review G0 (T2),
  panchina rigore (B1 intervallare s_L, C-XBVP(b), g-scan B3,
  concavità GBE — non toccati, budget esaurito dal brick).

Stato precedente (chiusura Sessione 17 — RI-AGGIUDICAZIONE BRICK-2
+ KICKOFF ESEGUITO; log a ordine totale:
validation/PROGRESS_2026-08-06_S17_brick2.md, 12 passi;
gate PASS al passo 2, VERDETTO passo 3: rinvio #4 SCADUTO,
BRICK 2 PARTITO)

Branch `rde-nozzle-program`. Commit: apertura+gate = 3b4b602,
ri-aggiudicazione = c5f0eee, duty(c) = 4a912b5, duty(d) = 0934313,
riconciliazione = 903b2d6, survey = 52d07aa, duty(b) = c47f865,
duty(a) = 8b8c695, brick stadiato = b255840, adjudicazione+review =
6c2ff8f, chiusura = (questo). Lint (xv) verde a ogni commit
(122 voci, da 117). Suite --fast di chiusura (su numpy 2.5.1,
rivalidazione unpin) nel log passo 12.

- **[F2/A1] RI-AGGIUDICAZIONE ESEGUITA — BRICK 2 PARTITO** (passo 3:
  termini waiver S15 verificati, campagna completa, controlli i-iii
  tenuti; RK-A ripesato, decisione preprint ripresentata all'utente;
  D6 item 9 annotato). **TUTTE E 4 LE KICKOFF DUTIES ESEGUITE**:
  (c) policy RK-G di record [DIR-RKG] P1-P4; (d) THERMOTAB C^1
  [X-THC1] PASS 14/14 (classe QUINTICA di Hermite — scoperta: la
  cubica lascia cp C^0; cp=dh/dT STRUTTURALE; audit EOS G>=1.089
  sul box, canale c4); (b) engine scan [X-SCANM] PASS (equivalenza
  8.9e-16 bit-level, O3.1 7.2e-9, cache solver load-bearing);
  (a) soglie loop-speed [X-LSG0] PASS clean-host (grad/solve=3.004
  nella finestra [3,4] del teorema T1; T2a FAIL-as-implemented =>
  GATE DI PRODUZIONE CHIUSO con rimediazione bucket VINCOLANTE;
  T2 armata; flip G0 non scattato).
- **[F2/A1] BRICK: ENGINE + PRIMO GRADIENTE DI FORMA DI RECORD**
  ([X-TOCV] staged PASS, b255840): marcia TOC a parete specificata
  (record adattivo certificato 4343 celle worst 1.65e-2 + replay
  scan fedele a 2.7e-12); GUARD TERMODINAMICO (omentalpico+
  omentropico via Crocco, dato stratificato RIGETTATO, slot cella
  3-famiglie nominato, hook c3); LEMMA L-DoD (troncatura al dominio
  di dipendenza: ipotesi = margine assiale UNIFORME u_x-c >= delta
  + h_min anti-Zeno — due costanti del certificato D2.5-U);
  **O3.1 su dJ/dW PASS** (diff 6.8e1 vs tol 1.6e2, N1 rigetta);
  driver RK-G su scipy trust-constr (semantiche verificate A
  SORGENTE: equality-only=Byrd-Omojokun, callback(xk,state), BFGS
  fresco per segmento, status-4=failure); oracolo GENO tipo 2
  ridotto FUNZIONA (eps 4.0016). RUN OPT end-to-end: 2 tentativi
  (fix callback; poi OOM a 46 min per churn di grafi sul path
  unjitted) — COMPLETAMENTO = NEXT-1, gated sulla mini-sessione
  production-code (P1/P2 già vincolanti). Nessun numero dal run
  morto (R5).
- **[RIGOR] PASS AVVERSARIALE (ordine utente) + FINDING GENO**
  (kickoff doc §5bis, 6c2ff8f): 2 leve CONFUTATE ed emendate
  (Newton replay a giri fissi -> while_loop su metrica di
  certificazione; GPU FP64-only), 1 ridimensionata (Hessiana),
  bucket con guardia safe-where (trappola where-NaN-gradient
  nominata, O3.1 = detector); **REJECTOR DI MARGINE ASSIALE per
  cella AGGIUNTO** (finding: stati M>1 con u_x<c calcolano FINITI
  e causalmente falsi — nessun NaN; GENO Interior_m NON ha alcun
  guard: caratteristiche all'indietro usate in silenzio, sentinella
  y<0 muta, PC senza segnale di convergenza — sano per le SUE
  costruzioni margine-compatibili, NON per un ottimizzatore che
  sonda pareti arbitrarie); memoria moc-critical aggiornata.
- **[TOOLCHAIN] direttive utente in memoria permanente** (survey
  SOTA per OGNI passo complesso + leggere-il-sorgente; toolchain
  currency; visione generale): trust-constr adottato con lettura a
  sorgente; **pin numpy SCARICATO** (np.trapezoid nei 4 siti,
  requirements numpy>=2.0, env a 2.5.1, rivalidazione = suite di
  chiusura); cache XLA persistente attiva; DECISIONE UTENTE:
  solver SDP = Clarabel primario, MOSEK accademico fallback (lock
  BLOCCATO sciolto).

Stato precedente (chiusura Sessione 16 — CAMPAGNA "FONDAZIONI
PROFONDE", SECONDA TRANCHE; log a ordine totale:
validation/PROGRESS_2026-08-06_S16_fondazioni2.md, 8 passi + 9
post-chiusura; gate PASS al passo 2, waiver brick-2 ereditato)

Branch `rde-nozzle-program`. Commit: apertura+gate = a898c24,
T1 = 20e41eb, T2 = 3b6db3a, T3 = 0b26dc7, T4a = 13f6ea4,
T4b = 084756e, chiusura = (questo). Lint (xv) verde a ogni commit
(117 voci, da 111). Suite --fast di chiusura nel log passo 8.

- **[RIGOR/A] T1 — U3+U4 SCRITTE: C-D25U COMPONENTE -a COMPLETA A
  LIVELLO CLASSE** ([S-D25U-U34], docs/rde_nozzle_D25U_U3U4.md,
  carrier [X-U3BD] PASS in (xiii)): il fronte fittato è un genuino
  shock di Lax 1-D in x-as-time; solve di bordo = sistema BORDATO
  (RH + riga caratteristica impingente; conteggio di Lax 5 = n+1
  machine-verified); SCOPERTA: C-MAJDA in-classe si AFFILA allo
  scalare di Lopatinskii-Schur U3-H1 (certificato a istanza
  s_L = 1.8685; uniformità per compattezza una volta puntuale);
  fronte C^2 auto-fornito; conteggio fronti DERIVATO dal budget di
  entropia sotto la lettura WALL-ATTACHMENT (altrimenti sesta
  costante — dichiarato); LIP_shocked esplicita nelle cinque
  costanti; stima ENTRO-STRATO (c2: cross-topology = census/RK-G).
  Inventario c1-c4 prezzato; -c/U5 intatto research-grade.
- **[RIGOR/A] T2 — ATTACCO A-CONTRACTION: ROTTA VIABLE-IN-CLASS A
  ISTANZA, ADOTTATA-COME-NOMINATA** ([S-ACFR], probe [X-ACFR] PASS,
  dichiarato probe non certificato): linea Vasseur-Krupa trapiantata
  in x-as-time con tre doni strutturali (solo fronti estremali;
  pareti GRATIS per T-XWALL; shift = il dof del fronte fittato) e un
  prezzo (clausola di CONFINAMENTO al box di convessità certificato);
  ostruzione di fronte ridotta alla condizione sul balance set
  psi_r >= 0 (sigma'-free); FATTIBILE all'oracolo su finestra pesi
  r ~ [3.2, 47], fronte invertito INFATTIBILE per ogni r
  (discriminazione); completamento gated su B1 (certificazione
  intervallare su K_delta — terzo payoff del substrato), B2
  (assembly), B3 (g-scan). NESSUNO scarico di C-MAJDA rivendicato.
- **[RIGOR/B] T3 — LEDGER PASSATA 2** ([PAP-D9HL] §4): 3 SCARICHI —
  H2/H-I2 sul nuovo default L4 DICHIARATO di record (nota M0 D2.4:
  sul default T-TH0 esatto + T-NSW teorema; patch subsoniche =
  case-class D1 §4.3bis coi monitor esistenti) e H-Pa per
  riclassificazione a istanza (misura prodotto caso D di record;
  testo (P) INTATTO per disciplina d'àncora); C-XBVP PRICED ->
  WEAKENED; 5 clausole post-passata-1 aggiudicate (tutte PRICED con
  canale eseguibile). Totali viventi: 29 righe, 3 D / 4 W / 5 N /
  17 P, zero non aggiudicate; target passata 3 nominati (B1,
  C-XBVP(b), C-P4RZ/fallback).
- **[RIGOR/A] T4a — LEMMA G-B ERGODICO SCRITTO, PP-2 RISOLTO SENZA
  DE-RATE** ([S-GBE], carrier [X-GBE] PASS 2.1 s): il soffitto
  geometry-free [T-GB] TRASFERISCE ai target ergodici —
  J_exact^+ <= F_env(flussi medi d'interfaccia) — 3-D pieno, ogni
  topologia, sotto E1-E5 dichiarate (storage limitato; superficie di
  scarico ASSIALMENTE SONICA u_x >= c — NECESSARIA, sup infinito
  senza; convessità EOS; Cesàro). Scoperte: il CAP SONICO OP-0 =
  esattamente il sup vincolato sull'insieme u >= c (non una pezza);
  NIENTE Birkhoff (Cesàro a T finito + storage limitato bastano —
  minimizzazione d'ipotesi sulla nostra stessa rotta nominata).
  Concavità: simbolica per ramo, composita 400/400 sul seam;
  inviluppo == ladder OP-0 a 3.4e-16. Etichetta quasi-steady-only di
  D5 Step 5(f)/8 RIMOSSA per la parete superiore; gap di Jensen vs
  parete per-fase dichiarato riportabile.
- **[RIGOR/A] T4b — S-LBML SCRITTO** (docs/rde_nozzle_LBML.md,
  registry upgrade): limite di mesh Lemma-B a cinque passi (Lax
  equivalence sul tangente; stabilità = ESATTAMENTE il certificato a
  cinque costanti D2.5-U con U1-U4 ora tutte scritte; solve di
  fronte discreto invertibile per h <= h_0 via U3-L1/U3-H1;
  trasposta esatta T-LEMB senza perdite; fronte C^2 auto-fornito).
  Clausole dichiarate: LB-c1 (regolarità per il RATE h^2,
  auto-monitorante via O3.2) + LB-c2 (topologia fissa = c2, RK-G).
  Nessun carrier nuovo (falsificatori = oracoli O3 pre-registrati).

Stato precedente (chiusura Sessione 15 — CAMPAGNA "FONDAZIONI
PROFONDE", PRIMA TRANCHE; log a ordine totale:
validation/PROGRESS_2026-08-04_S15_fondazioni.md, 12 passi poi
riaperta fino a 21; gate PASS + waiver brick-2 ereditati dal passo 2)

Branch `rde-nozzle-program`. Commit: T1a = a046303, T1b = 044db90,
T1c = b8f3e17, T3 = 4b19307, T2-parziale = 8e6b891, T4 = ab3cf38,
chiusura = (questo). Lint (xv) verde a ogni commit (107 voci).

- **[RIGOR/A] T1a — LEMMA CARICO LATERALE ROTANTE DI RECORD**
  ([T-SLRW], docs/rde_nozzle_side_load.md, carrier [X-SLRW] PASS
  10/10 in suite (xiii)): regola di selezione m=1 per risultanti
  trasversali (forze E momenti) su superfici di rivoluzione, prova
  cinematica (2 ipotesi, nessuna EOS, salti ammessi); n>=2 onde
  co-rotanti identiche => densità di carico trasversale
  IDENTICAMENTE nulla; n=1 => vettore a modulo costante rotante a
  Omega; corollario M_x == 0 (la pressione non può dare coppia
  assiale). DISPOSIZIONE DI RECORD: output secondario dichiarato,
  non slot in c (upgrade path CVaR a A6). R4: M0 T0 companion +
  D2.6 nota.
- **[RIGOR/A] T1b — TRASFERIMENTO CAUCHY->BVP SCRITTO** (il soft
  spot della canonicità shock-free; docs/
  rde_nozzle_cauchy_bvp_transfer.md, carrier [X-XBVP] PASS, (xiii)):
  [T-XSON] biiezione sonica THEOREM a EOS astratta; [T-XWALL] LEMMA
  DI PARETE THEOREM (flusso di entropia relativa a slip
  IDENTICAMENTE nullo, ogni g, ogni EOS — la perturbazione ammessa a
  parete è isentropica a flusso di massa costante); [S-XCONV]
  convessità dal margine ASSIALE (200/200 sul box, pinza sonica
  netta; finding: traccia u_x > c, non |u| > c); [T-XWS] THEOREM*
  weak-strong sul BVP (alternative shockate ESCLUSE PER TEOREMA a
  dato uguale) con condizionale nuovo [C-XBVP](a,b) nel ledger
  §1bis. C-MAJDA separato pulito.
- **[RIGOR/A] T1c — U1 DI D2.5-U SCRITTA PER DAVVERO**
  ([S-D25U-U1], docs/rde_nozzle_D25U_U1.md): stime C^0/C^1 +
  Lipschitz a due soluzioni (componente -a, livello liscio, costanti
  esplicite) + -b corollario; VERDETTO SUL CLAIM DI COSTO:
  CONFERMATO bounded; SCOPERTA: il set certificato richiede il
  floor di larghezza h_min (quinta costante NOMINATA — senza, il
  conteggio rimbalzi rende falsa l'uniformità); emendamento eseguito
  (ledger §1 + registro C-D25U). -c/U5 intatto research-grade.
- **[RIGOR/B] T3 — LEDGER MINIMIZZAZIONE IPOTESI, PASSATA 1**
  ([PAP-D9HL], docs/rde_nozzle_hypothesis_ledger.md): verdetto
  obbligatorio per TUTTE le 17 righe H-* di D1 §9 + 7 condizionali
  (24/24): 0 SCARICATE / 6 INDEBOLITE / 5 NECESSARIE tutte con
  controesempio citato (H-A1/H-A2 ora MACHINE-EXHIBITED da X-SLRW) /
  13 PREZZATE con canale eseguibile. Target di passata 2 nominati.
- **[RIGOR/A] T2 — SWEEP SECONDA LENTE: COMPLETATO (riapertura
  2026-08-05, log passi 13-14, commit b1b088b + 1f51da2)**: resume da
  cache 12/12 agenti 0 errori; 27/27 item aggiudicati a doppia lente
  (2 via arbitro): 22 CONFIRMED con fix structure/status ESEGUITI
  (M0 ×8 incl. pin-pending quantificatore attaccamento + status
  finitezza settori + M1-witness O2-condizionale; D4 ×2; D5; registro
  ×9; P3; ledger; D8 §6 ×2 senza adjudicazione; D6 ×2 incl. item 16
  gruppo (xvii) PROPOSTO; side_load), 4 ALREADY-FIXED, 1 IOU nominata
  (C-N2 al kickoff PB-2). Il residuo a lente singola di D8 §8 è
  CHIUSO; debiti restanti = le IOU dichiarate dentro i fix (pin
  census O1/O2 all'utente, C-N2, meccanizzazione (xvii)) + gli angoli
  di esplorazione mai eseguiti. IN PIÙ (passo 13, sfida utente di
  record): claim "average-then-design" DELIMITATO in P-1 §4.5 con le
  àncore RDE nominate a livello di verifica graduato + duty di
  acquisizione (page-verify Liu 2022 + Harroun 2021).
  [Stato precedente del punto:] PARZIALE (muro di usage):
  workflow canonico wf_c0bbb1d8-f73 (5 batch, 27 item, 2 lenti +
  arbitro) fermato dal limite account a 3/14 agenti; journal cache
  MONOTONA, zero perdite, evento dichiarato (log passo 10). HARVEST:
  batch B4 3/3 CONFIRMED a doppia lente, fix ESEGUITI (DIR-G0
  quantificazione cross-ref; DIR-PRISTINE split del falsificatore;
  D-S1 debitori nominati = sync del T1b). RIGORE: gli
  UNRECONSTRUCTABLE-da-fallimento NON sono verdetti; 24/27 item
  RESTANO residuo dichiarato. RESUME deterministico da cache al
  reset (istruzioni nel log passo 10).
- **[RIGOR/C] T4 — DOSSIER MASSIMO GLOBALE APERTO** ([PAP-GMAX],
  docs/rde_nozzle_global_maximum_dossier.md): censimento con schede
  (interval B&B / momenti-SOS / deflazione+esclusione / torneo di
  settori), NESSUN adopt senza carrier; FINDING STRUTTURALE: le tre
  vie certificate collassano su UN mattone abilitante condiviso
  (enclosure intervallare della marcia) + porta SOS nativa dal duty
  THERMOTAB; programma delta->0 assemblato a 5 livelli; sinergia: il
  primo mattone scarica anche C-XBVP(a).
- **[RIGOR/A] SEGMENTO RIAPERTO (2026-08-05, log passi 13-17) — U2 +
  MATTONE SUBSTRATO**: (i) sfida utente di record aggiudicata
  (evidence-bounding P-1 §4.5, b1b088b); (ii) T2 COMPLETATO (27/27,
  21 fix, 1f51da2); (iii) U2 BRICK [T-U2RG] (b2610d1): a parete slip
  il glancing è IMPOSSIBILE (nessun input C_geo/C_dat — riduzione di
  ipotesi su U1 (T2)); la solvibilità della riflessione degenera
  ESATTAMENTE al sonico totale q=c (esclusa dal solo margine
  assiale); R chiuso in forma; necessità di slip esibita per
  controesempio; carrier X-U2RG PASS 8/8 in (xiii) "fast seven";
  (iv) MATTONE SUBSTRATO [X-IVXC] (ab7725b): convessità S-XCONV
  CERTIFICATA A INTERVALLI sull'intero box (M,V) e, per il nuovo
  LEMMA DI RIDUZIONE [T-XRED] (definitezza = funzione della sola
  coppia di Mach, per congruenza diagonale positiva sotto due gruppi
  di scaling), per OGNI (rho,S) — C-XBVP(a) SCARICATA a livello
  istanza; Card 1 del dossier ESEGUITA con method record misurato
  (forma polinomiale espansa morta ~1.6e3; Gershgorin infattibile
  53%; vince riformulazione: Krawczyk + mean-value + quoziente di
  simmetria); suite +gruppo (xviii) rigor (59.3 s misurati).
- Suite: lint (xv) verde ad ogni commit; run --fast di chiusura nel
  log passo 12 (prima tranche) e passo 17 (segmento riaperto).

Stato precedente (chiusura Sessione 14 — PANEL DI RECORD D8 +
R4/R4-bis; sessione UNICA aperta 2026-07-22, ripresa 2026-08-02/04
su ordine utente; log a ordine totale:
validation/PROGRESS_2026-07-22_S14_panel.md, 24 passi)

Branch `rde-nozzle-program`. Commit: reads = c0298d2 (passi 5-7),
D8+registro = 7be8b98, R4 E9a-E9j = 20b4007, T5 = 901bbb3,
R4-bis E9k-E9r = dcbc5f9, addendum §8 = acf38cd, chiusura = (questo).

- **[PIANO/panel] D8 DI RECORD** (docs/rde_nozzle_panel_2026-07-22.md,
  [PAN-S14]): panel a convergenza in 4 round (7 personae indipendenti +
  loop granulare finder/per-paper + scambio inter-agente + 16 team a
  doppia lente con arbitro: 16/16 CONFIRMED, 0 dissensi). L'architettura
  del programma REGGE sette lenti ostili; due finding strutturali di
  record: (i) rischio analitico residuo CONCENTRATO al confine S1
  (C-D25U-c senza discharger nominato; il salto d'onda è esattamente
  ciò che la classe esclude); (ii) asimmetria dei falsificatori
  (gli strumenti che possono far male ritardano su quelli che
  confermano) — co-posseduta e ora prezzata (brick 2 PROTETTO).
- **[LEADS/R4] E9a-E9j + R4-bis E9k-E9r**: 48 correzioni datate su 17
  doc di record, TUTTE team-verificate prima dell'esecuzione e
  AUDITATE dopo (22/22 LANDED, quattro auditor indipendenti).
  Punte: sync P-1 §1.4/§4.5 (contraddizione K-O); Kraiko 1963
  title-verified in genealogia; K-O §5 secondo caso di collasso;
  banco O3.3 corretto ((30)/(31)+f2, MAI (32)-(34) fuori flusso
  costante); split C-D25U a/b/c con U5 NOMINATO MANCANTE; C-P4RZ
  coniato (Riesz non banale: monodromia non-compatta); ipotesi
  FIXED-MARCH-TOPOLOGY nominata nel Lemma B + rischio RK-G; norme
  O3.2/O3.3 PRE-REGISTRATE (esclusione lip/corner/sonic — 3 lenti
  convergenti sul pericolo false-kill); D-JEX/T-O2/T-T7FS/T-P7S1
  falsificatori resi rigettabili (K-B retirement, barre W1 derivate,
  sync doc-verbatim); fallback target J_exact^± definito;
  MAXIMALITY(a) ri-ancorata; H-R1 coniata; note namespace U1-U5.
- **[PIANO] Delta D6**: item 9 PROTETTO per S15 (tre rinvii dichiarati,
  niente quarto senza gate failure) con duties di kickoff (soglia
  loop-speed derivata, architettura scan/vmap, policy RK-G, duty
  THERMOTAB C^1); item 15 bundle strumenti-mu (J lineare in mu =>
  barre di sensibilità gratis); RK-A PARZIALMENTE REALIZZATO; RK-G
  coniato; G5 esteso (sweep 1991-2010, back-chase refs K-O, Kraiko
  2010 TOC, Tillyaeva 2.2(f)); banco riletichettato "PDE single-cycle
  falsification bench"; G3 duty di quantificazione.
- **RESIDUO PANEL DICHIARATO** (D8 §8): finding a lente singola in
  attesa di seconda lente (onda D5/D4 currency, facet shape-topology,
  completamenti roads-atlas, ME-2/ME-4/PP-3/PP-4/PP-5, gruppo lint
  (xvii) proposto) + angoli di esplorazione r2 mai eseguiti (tagliati
  per ordine costo). NULLA di ciò è di record finché non verificato.
- **Suite**: lint (xv) verde ad ogni commit (96 voci, rejector
  provati); lint numerico (vii) PASS live in-audit. Eventi
  infrastrutturali (3 muri di usage, 1 morte di processo) tutti
  dichiarati a log con resume da cache journal — zero perdite.

Stato precedente (chiusura Sessione 13 — LEADS/PAGE-VERIFY:
"contingenza Kraiko-Osipov AGGIUDICATA + verifiche di pagina";
sessione UNICA)

Branch `rde-nozzle-program`. Log:
validation/PROGRESS_2026-07-21_S13_leads.md (gate PASS passo 2, 11
passi). Commit: T1 = d951d4c + riparazione b2771a3 (deviazione di
processo dichiarata al passo 7), T2 = 022b9b2, chiusura = (questo).

- **CONTINGENZA K-O 1970: AGGIUDICATA (modalità containment, come
  pre-armata)** — full text letto personalmente: contouring
  variazionale MEDIATO SU TRAIETTORIA per un contorno condiviso
  (condizione di parete integrata nel tempo con peso W(t) del
  moltiplicatore di traiettoria; campi moltiplicatori sulle
  caratteristiche con salti; caso di COLLASSO alla famiglia classica
  con peso MEDIATO W° sotto similarità d'ingresso; quasi-steady
  dichiarato ma non prezzato). AZIONI: P-1 §4.5 riscritta
  (containment + citazione obbligatoria), M0 T3-C2 + T7 note di
  precedente, D2 riga di aggiudicazione, D4 §3 addendum. P-2
  INTATTA.
- **VERIFICHE DI PAGINA**: Cooper-Shepherd JPP 24(1):81-87 (2008)
  doi 10.2514/1.30192 — +72%/+43% confermati verbatim (ruoli
  precisati: vs plain tube, regime tamper vs quasi-steady); Lozano
  2019 — divergenza in mesh CONFERMATA ma locus CORRETTO
  (parete/trailing edge, NON l'urto; Lemma B §4.4 corretto,
  trovato-e-fixato); G-U Part 1 SINUM 48:882-904 — riparazione
  eps = h^alpha e lineage del controesempio confermati, contrasto
  capturing-vs-FITTING esplicito (Part 2 MANCANTE — acquisizione
  prioritaria); Lozano-Ponsin 2025 — il loro det-trasposto È la
  Prop. A1, invarianti aggiunti (32)-(34) = banco oracoli O3.3,
  jump conditions = specchio analitico di Prop. A2, urti esclusi
  dal loro scope (Lemma B/G12 intatti). [CORREZIONE S14, PAN-S14
  F-O33BENCH: il banco O3.3 di record = match componente-per-
  componente C-O33; righe supplementari = compatibilità (30)/(31) +
  drift f2 (Prop. A3); gli invarianti (32)-(34) valgono SOLO su
  patch a flusso costante (loro p. 7), salvo R1^psi = psi1 - H psi4
  che resta valido lungo le streamline.]
- CODA DICHIARATA: Owens-Hanson, Morris, Lozano-2018, check
  reference-list L-P (pp. 9-23), G-U Part 2 (upload utente).

Stato precedente (chiusura Sessione 12 — RIGORE/R4: "retro-
propagazione della review-conversation + piano rafforzato";
sessione UNICA, check pre-commit puliti)

Branch `rde-nozzle-program`. Log a ordine totale:
validation/PROGRESS_2026-07-21_S12_rigoreR4.md (gate PASS al passo 3).
Commit: C1+C2 = 981c620, C3 = 4f12068, chiusura = (questo commit).
MANDATO UTENTE: nessuna scoperta della conversazione di review
2026-07-20/21 può vivere solo in chat — tutto registrato a norma.

- **[F4-prep/T3QS] T3-QS DI RECORD** (981c620): protezione
  quasi-steady della classe del collasso — sulla famiglia-raggio
  (ciclo solo-Pc, EOS-general con e(T) arbitraria) la correzione di
  sweep al PRIMO ordine si annulla sulla parte liscia del ciclo
  (Jacobiani e sorgente adjoint invarianti lungo il raggio
  conservativo; lo sweep agisce da puro sfasamento) e si concentra
  al salto di passaggio d'onda; fuori-raggio = termine d'AREA
  (isteresi) calcolabile. Carrier validation/t3qs_sweep_protection.py
  (catena P1-P6 + rejector R1-R3, PASS 8.6/6.6 s) = gruppo suite
  (xvi); doc docs/rde_nozzle_T3QS.md (con l'anatomia fisica
  dell'operatore trascurato e il lag acustico dell'urto interno);
  remark in M0 Teorema 0 e D3 §3; registro [T-T3QS]/[X-T3QS]/
  [X-GRP16]. Conseguenze: la classe del collasso è protetta al
  secondo ordine (spiega la qualità empirica della pratica
  quasi-steady del campo); le misure O5 sono MIRATE (finestra del
  salto + cicli a due parametri).
- **[F2-prep/BLITE] B-LITE DI RECORD** ([S-BLITE], M0 Parte V): rung
  3a-lite — campo wave-frame esatto del SOLO ugello per marching
  elicoidale 3-D dove u_x − c ≥ δ (C2 del Lemma 4 esercitata in 3-D;
  Ω input dal dato I1; adjoint = Lemma B sollevato verbatim); il
  metro esatto del residuo sweep/D2 a costo di marching; mattone da
  verificare: autostruttura G12-L1-3D (carrier candidato). L'ancora
  completa resta il tier per Ω-output/camera/reazione.
- **[F1/D-GSEP] SEPARAZIONE COME VINCOLO DI STATO in (P)** (M0 D2.6
  addendum): g_sep(S; s(ξ)) ≤ 0 μ-q.o. (classe criterio R2,
  empirico dichiarato; detector runtime = monitor S1); moltiplicatore
  attivo = valore marginale del margine di attaccamento; la
  dual-bell temporale (N1) diventa decidibile ad active-set a rung 2;
  la separazione deliberata ESCE dalla classe certificata (riapre il
  canale subsonico di feedback + dinamica propria non-rotante — fuori
  scope per fisica, non solo per dichiarazione).
- **[F0-coda/D2 + PIANO/D6] GONZÁLEZ-VIANA + PIANO RAFFORZATO**
  (4f12068): Aerospace 12:502 (2025) LETTO FULL-TEXT (PDF in
  literature/) con attribuzione a tre vie di record (vincoli attivi /
  effetti di MISURA — rung-2 ne predice l'ottimo qualitativo:
  divergente piccolo, ⟨p_out⟩ ≫ Pa / residuo genuinamente unsteady
  da start-stop = ancora O5); D6: O5-LITE come esperimento di
  falsificazione PRE-REGISTRATO delle tre predizioni T3-QS (A4),
  B-lite primo item di A5, benchmark GV in A2, 90-giorni item 9-14
  (brick TOC S13 → sblocca O3.3/P-2; GV+O5-lite; B-lite;
  registro acquisizioni con priorità; ANCORA SPERIMENTALE = gap
  industriale #1; PIANO COMPUTE = gap #2), rischi +RK-E/+RK-F.
- **SUITE: 15/15 PASS in 101 s** (fast tier, host sano; nuovo gruppo
  (xvi) incluso; lint (xv) 0 violazioni con le 5 voci nuove).

Stato precedente (chiusura Sessione 11 — "FASE 2/A1 BRICK 1: la
machinery di generazione profili ESISTE ed è certificata + P-1 body
text COMPLETO"; sessione UNICA, check pre-commit puliti)

Branch `rde-nozzle-program`. Log a ordine totale:
validation/PROGRESS_2026-07-20_fase2_S11.md (gate pre-esecuzione PASS
al passo 3; 14 passi; aperta il 20, chiusa il 21 — pause utente, mai
due sessioni). Commit: T1 = 8fc815e, T2 = c0065af, chiusura = (questo
commit).

- **[F2/A1] BRICK 1 FATTO — LA MACHINERY DI GENERAZIONE PROFILI È DI
  RECORD, VERDICT PASS** (8fc815e; carrier [X-A1IM]
  validation/a1_ideal_march_jax.py, on-demand env: jax + binario GENO
  WSL): la marcia MoC differenziabile ASSEMBLATA genera l'ugello
  IDEALE end-to-end (IVL di Sauer → fan → espansione in gola su arco
  con inverse-wall/piede-su-corda/righe-void → regione uniforme con
  PARETE = STREAMLINE DI PORTATA), gemello del nozzle_type 0 di GENO;
  ogni cella = processo implicito custom_vjp (regola implicita, MAI
  unrolled) ⇒ il reverse-AD della marcia È lo sweep aggiunto discreto
  del Lemma B, eseguibilmente. VERDETTO (caso ridotto NI=21, da=0.5°,
  Ne=41, eps=4, CH4/O2 frozen; 14/14 check incl. 4 controlli
  negativi): contorno vs GENO 62/62 in banda Richardson derivata,
  max|Δy| = 7.6e-9 (banda 4.5e-3), Me gemello-identico a 8.4e-9,
  maxtheta 16.265° = GENO; O3.1 sull'INTERA marcia 2.7e-10 vs tol
  5.1e-8 (replay fidelity 1.6e-13), vjp corrotto rigettato;
  certificazione Newton per cella UNIT-CONSISTENT in spazio z (2756
  celle, worst 1.4e-2); sorgente corrotta rigettata PER RIFIUTO;
  tabella/gamma corrotte rigettate. BACKEND THERMO A TABELLE
  ([DIR-THERMOTAB], direttiva utente S11 + decisione: CANTERA UNICO
  GENERATORE DI PRODUZIONE; generatore NASA-poly GENO confinato a
  istanza oracolo cross-code, dual-route nel budget di costanti
  fisiche DERIVATO 5.3e-6 ≤ 2.5e-4·K con rejector 1e-3; gamma=const
  solo oracolo). R4 stessa sessione: M0 VI "A1 BRICK 1 OF RECORD" +
  pin DIR-THERMOTAB; D6 A1 STATUS S11; Lemma B §4.7 istanza
  march-level; registro +4 voci ([X-A1IM], [DIR-THERMOTAB],
  [PAP-P1S1389], [PAP-P1S57] found-and-aligned S10) + T-LEMB carriers.
  SCOPE ONESTO: guardia DIR-G0 SCARICATA per il tipo ideale (marcia
  diretta); il mattone TOC VARIAZIONALE ((**')/corner via dJ/dSigma
  con TR-SQP) NON è in questo carrier → NEXT S12; falsificatore
  loop-speed G0 ancora armato (scala di produzione non riaggiudicata).
- **[F1/P-1] §1, §3, §8, §9 TESTO PIENO DI RECORD — BODY TEXT
  COMPLETO** (c0065af, docs/rde_nozzle_P1_sections_1_3_8_9.md,
  [PAP-P1S1389]): §1 genealogia var-gamma con CITAZIONE OBBLIGATORIA
  Rao 1958 IAC Amsterdam (ABSTRACT-VERIFIED ONLY, attribuzione
  limitata all'abstract); §1.4 novità query-bounded contingente su
  Kraiko-Osipov; §3 T0/N-SW + confine N6 theorem-grade (class refresh
  dichiarato); §8 bridge EAP/S-H (mappe termine-a-termine, tre
  finding = istanze dei teoremi, no circolarità); §9
  limiti/outlook (spina condizionale unica). Regole (a)-(e), claim
  per ID (21, lint-risolti), grep coerenza PASS. Skeleton: restano
  SOLO appendici A1-A7 + assembly.
- **SUITE**: run completo in chiusura (verdetto nel log passo 14).
- Non mio, non toccato (dichiarato): directory `literature/`
  untracked comparsa nel tree (materiale utente); ADR panel sempre
  in attesa di ratifica, non committato.

Stato precedente (chiusura Sessione 10 — "APERTURA FASE 2: decisione
G0 col criterio GENO ESERCITATO + coda Fase 1 P-1 §5-§7 + leads";
sessione UNICA, nessuna concorrenza ai tre check pre-commit)

Branch `rde-nozzle-program`. Log a ordine totale:
validation/PROGRESS_2026-07-17_fase2_S10.md (gate pre-esecuzione PASS
al passo 3; 14 passi; aperta il 17, chiusa il 20 — pause utente, mai
due sessioni). Commit: T1 = bfd0063, T2 = 570b38c, T3 = 0fb6a21,
chiusura = (questo commit).

- **[F2/G0] G0 DECISO — IL RESIDUO TOOLCHAIN È CHIUSO CON EVIDENZA**
  (bfd0063; dossier docs/rde_nozzle_G0_decision.md, registro [DIR-G0]
  + [X-GENOXC]): (a) GENO COMPILATO in WSL Ubuntu (gfortran 11.4.0,
  CMake, Cantera/Sundials/Tecio OFF, LAPACK dall'env conda ct-env
  preesistente — ZERO installazioni nuove; submodule clonati via
  HTTPS con override non-persistente, ramo cantera/sundials saltato;
  GENO MAI modificato/committato, output gitignored); (b) tocnoz
  rigenerato: exit 0, performance fisiche sane, CONTORNO TOC
  riprodotto al riferimento committato a max |Δ| = 1e-10; convenzione
  checksum N-36 letta in-sessione e confermata (md5 field
  toolchain-dipendenti, scalari stampati identici) ⇒ confronto
  scientifico a valore; (c) NUOVO CARRIER CROSS-CODE
  validation/g0_geno_crosscode.py [X-GENOXC], on-demand (env:
  gfortran): test a RESIDUO EOS-general (banda di troncamento
  per-cella DERIVATA |R_trap| ≤ 4(|R_trap−R_end|+floor): 218/218
  celle core supersonico dentro) + RIPRODUZIONE letterale "due punti
  → punto nuovo" (chiusura energetica γ-di-cella dichiarata oracolo:
  95% in banda); controlli negativi rigettano (figlio/piede corrotto
  100%→0%, accoppiamento errato 84×); metodo onesto a log (fit
  d'ordine cross-field ABBANDONATO perché mal posto su griglia fissa
  — dichiarato); (d) DECISIONE: JAX primario (fedeltà 52/52 + O3.1;
  loop-speed standalone: solve ~322 µs, +adjoint ~327 µs ⇒
  grad/solve ~1.01 host-invariante), Julia+Enzyme alternate
  dichiarata (non benchmarcata — detto), GENO riferimento dual-code;
  falsificatore loop-speed ARMATO. R4 stessa sessione: M0 VI.7
  addendum + D6 (G0 ISTRUITO→DECISO; **FASE A1 APERTA**, primo
  mattone = unit process gamma(T) + X-GENOXC regressione permanente).
  SCOPE ONESTO (challenge utente in-sessione, scritto in registro/
  dossier): il cross-code certifica l'INTERIOR UNIT PROCESS, NON la
  machinery di generazione profili — NESSUN contorno è stato generato
  con jax; quella è A1 brick 1.
- **[F1/P-1] §5-§7 TESTO PIENO DI RECORD** (570b38c,
  docs/rde_nozzle_P1_sections_5_7.md): §5 sistema mediato (blocchi
  (a)(b)(c), fattorizzazione (**') R(ξ)w(ξ), BOXED WARNING media
  naive, riduzione quasi-1D col carrier EOS-general eps*_real
  [T-T7RED] gruppo (xii), forma chiusa declassata a oracolo, pin
  VI.4bis(iii)); §6 ceiling [T-GB] + cap sonico (controesempio
  γ=1.15, 4 righe subcritiche rigettano il naive) + ladder + DELTA
  DI PURGA −4.4..−7.9% + BRACKET DI EQUILIBRIO +6.3..+7.0% [T-EQBR];
  §7 SEMANTICS-FIRST (D3 §10quater(5) verbatim), blocco (P),
  statement (1)-(4) [T-OP11e], warning artefatto chiusura pubblicata,
  ISTANZA ROUTE REALE §7.5bis, premium_bound, molteplicità, vuoto.
  Regole (a)-(e) per sottosezione; claim per ID di registro; CLASS
  REFRESH vs skeleton DICHIARATO (SCHEMA→THEOREM* per upgrade S6/S8);
  novità CONDIZIONALE (Kraiko-Osipov). Grep coerenza PASS; skeleton
  aggiornato (restano §1, §3, §8, §9 + appendici).
- **[LEADS] ENTRAMBI I LEAD CHIUSI ALLA FONTE** (0fb6a21, metodo
  raw-HTML/raw-PDF, mai il summarizer): Rao 1958 "IAF Amsterdam"
  IDENTIFICATO = "Contoured Rocket Nozzles", Proc. IX IAC Amsterdam
  1958, Springer (DOI 10.1007/978-3-7091-4745-0_18), abstract
  verificato su HTML grezzo con conteggi: il precedente var-gamma è
  Rao stesso, 1958, STATO SINGOLO ⇒ citazione obbligatoria nella
  genealogia gamma di P-1/P-2, novità cycle-averaged INTATTA (full
  text paywalled → coda G5, dichiarato); van Meerbeeck EUCASS 2013
  LETTO INTEGRALE (15 pp): procedura puntuale TOP (TDK, sea level),
  conteggi average/trajectory/weighted/flight = 0 ⇒ G14 REGGE,
  lead CHIUSO. R4 in lit_b0bis (V1)+(A7).
- **SUITE**: 16/16 gruppi PASS exit 0 in 213 s (host sano; run pieno
  incl. tier rigor (xiv) 31.8 s ed esempi live 99.2 s). q_mapping.*
  datestamp rigenerati dagli esempi due volte in-sessione: ripristinati
  entrambe le volte (diff 2 righe, contenuto identico, dichiarato).
- NON eseguiti (dichiarato): T4 (brick PM generalizzata — confluisce
  in A1 brick 1) e T5 (carrier T-NSW) — priorità T1>T2>T3 rispettata.

Stato precedente (chiusura Sessione 9 — ORDINE DI PROGETTO
[F1/SCAFFOLD-M]: migrazione M-1..M-5 + riallineamento D6 + pulizia;
NESSUNA concorrenza rilevata — prima sessione pulita dopo sei
violazioni)

Branch `rde-nozzle-program`. Log a ordine totale:
validation/PROGRESS_2026-07-17_S9_ordine.md (gate pre-esecuzione PASS
al passo 4; 17 passi). Commit: M-1 = 898f480, M-5 = 8a2c946,
M-2 = 5aa71dd, M-3 = 605306c, M-4 = 7e1dfa9, T6 = b2b3570,
T7 = 2fc6222. Rischio matematico ZERO rispettato: ogni diff sui doc
di teoria è structure-only (ispezione hunk-per-hunk a log).

- **[M-1] REGISTRO DEI CLAIM** (`docs/claims_registry.yaml`): 83 voci
  tipizzate (schema SCAFFOLD §2: id/kind/class/scope/statement/doc/
  proof/inherits/carrier/suffices_symbolic/falsifier/gamma) — seed §2
  trascritto e COMPLETATO contro il tree reale (novità S8-op censite:
  T-EQBR, T-T7RED, X-G0AX, X-P2A1, gruppi suite come carrier;
  identificazioni Lemma A (i)/(ii)/(iii) da upgrade S6; condizionali
  di chiusura C-HT4/C-IGMIX/C-O33 giustificati per contratto §3.4;
  direttive e record paper). Ogni ancora risolve; YAML subset stretto
  dichiarato (niente dipendenza PyYAML).
- **[M-2] CLAIM LINT** (`tests/test_claims_lint.py`, gruppo (xv)):
  parse + ancore + riferimenti + appartenenza-suite (esenzione
  on-demand sintatticamente vincolata per gli spike jax) + vincoli di
  schema + grep ID orfani; REJECTOR DIMOSTRATO AD OGNI RUN (tre
  violazioni seminate in-memory → tutte rigettate, o il gruppo
  fallisce). La teoria non può più derivare silenziosamente dal suo
  indice.
- **[M-3] SPINE ID SU M0**: 29 righe, tutte pure inserzioni di tag
  ([D-P], [T-TH0], ..., [T-T7FS]; tag inline solo nei siti non
  ambigui); prove intatte al loro posto; grep di coerenza PASS.
- **[M-4] LEDGER L4** (`docs/rde_nozzle_conditionals.md`): C-D25U e
  C-MAJDA enunciati UNA volta (trascrizione dalle fonti di record) con
  dischargers ed eredi per ID; pass di riferimenti sul proof layer
  (22 inserzioni): ogni dichiarazione THEOREM* punta a un ID.
  TROVATO-E-ALLINEATO (dichiarato): due righe di classe stantie in
  lemmaA vs gli scarichi S6 ((ii) THEOREM, (iv) THEOREM*) — annotate
  con supersessione datata secondo la convenzione del corpus, zero
  matematica nuova.
- **[M-5] CARRIER IN SUITE** (eseguito PRIMA di M-2, deviazione
  d'ordine dichiarata: il check (c) del lint presuppone la
  promozione): gruppo (xiii) fast = X-PA1/X-G12/X-N6/X-5F
  (subprocess, exit-0 + verdict line; 1.4-4.4 s misurati); TIER RIGOR
  dichiarato nel runner = gruppo (xiv) X-P2A1 (44.7 s misurati), nei
  run pieni, saltato da --fast.
- **SUITE**: 16/16 gruppi PASS exit 0 (run pieno; wall 1818 s sotto
  contention auto-inflitta dichiarata a log passo 9 — non tempo di
  record); --fast pulito 14/14 in 448 s con CAVEAT host degradato di
  record (il gruppo (i) da solo 368 s vs i 201 s dell'INTERA suite
  S8; la decisione di tier poggia sui runtime standalone, non
  affetti). Lezione operativa a log: tasklist (mai ps MSYS), mai
  run di suite concorrenti.
- **[T6] D6 DELTA-PASS** (solo stati): A0 CHIUSA (incl. route reale),
  A1 avviata a livello spike con dossier G0 e residuo toolchain
  nominato, stream P-1/P-2 aggiornato (draft di record, trigger arXiv
  mezzo armato), G0 ISTRUITO col criterio interop S5, G5 con 2a fatto
  e flag Kraiko-Osipov, 90-giorni item-per-item. Un lettore di
  D6+PROGRESS ricostruisce lo stato senza i LOG.
- **[T7] PULIZIA**: scratch_{out,err}.txt ispezionati (riproducibili)
  e rimossi + regola gitignore; validation/INDEX.md = indice a una
  riga dei nove log di sessione. GENO/ e ADR panel non toccati.

Stato precedente (chiusura Sessione 8 — OPERATIVA: "P-1 §2/§4 +
spike axisym/shock + diagramma route reale"; CONCORRENTE con la
S8-rigore E col filone SCAFFOLD, riconciliata due volte)

Branch `rde-nozzle-program`. QUINTA e SESTA interleaving rilevate e
riconciliate in-sessione (S8-rigore attiva in parallelo + commit
SCAFFOLD atterrati tra i miei; TUTTI i commit S8-op path-limitati;
audit hunk post-commit PULITO: nessun contenuto estero spazzato nei
miei commit, nessun mio hunk nei loro — log S8 passi 5, 8 e audit
post-T3). Log a ordine totale:
validation/PROGRESS_2026-07-16_fase1_S8.md (gate pre-esecuzione PASS
al passo 2; la sessione ha scavalcato la mezzanotte: passi 9+ datati
2026-07-17). Commit: T1 = a4e4964, T2 = 001aecc, T3 = 528e033,
T4 = eab6cf5.

- FASE 1 — **[F1/P-1] TESTO PIENO §2 E §4 DI RECORD** (a4e4964,
  docs/rde_nozzle_P1_sections_2_4.md): §2.1-§2.5 (Theorem 2.1 media
  esatta + distinzione storage-vs-O(St) verbatim; (2.3) = UNICA
  approssimazione; O1 con canali di rottura; O2 log-uniforme; contratto
  I0-I4) e §4.1-§4.5 (dicotomia con scope per-lemma T3-A/B/C, riga
  pedagogica concordata del Lemma T3-C, dualità di quota, sharpness coi
  numeri di record INCLUSO il delta di purga -4.4..-7.9% ora citabile,
  T4 THEOREM* con dovere-di-citazione K-E, spiegazione della pratica).
  Regole (a)-(e) applicate per sottosezione (audit line [Class |
  Falsifier | Carrier | Gamma status]); claim-map cross-check C1-C4/
  C8-C11/C26; wording di novità §4.5 QUERY-BOUNDED e CONDIZIONALE su
  Kraiko-Osipov 34(6) 1970 (contingenza D4 §3 ribadita); naming guard
  Lemma T3-A/B/C vs P-2 Lemma A/B dichiarato; grep di coerenza PASS.
- FASE 2-prep — **[F2-prep/G0] SPIKE ESTESO: AXISYM + SHOCK + INTEROP
  GENO** (001aecc, validation/g0_spike_axisym_shock.py, gemello — lo
  spike S5 resta intatto): Brick A termine sorgente assialsimmetrico
  DERIVATO IN-HOUSE (rotta autovettore-sinistro, limite planare esatto
  0.0) con verifica DUAL-ROUTE contro la forma conservativa (u,v)
  Zucrow-Hoffman e rejector di scaling d'ordine (banda [4,16] per
  dimezzamento; sign-flip rigettato a ratio ~1.7); gradienti 36/36 +
  16/16 in tolleranza derivata. Brick B shock point fitted = processo
  implicito su RH (theta-beta-M + Mach normale): identità dot-product
  O3.1 a 3.4e-12 vs tol 1.2e-9 ⇒ **P-B1 SCARICATO A LIVELLO BRICK**
  (registro Lemma B aggiornato, R4 stessa sessione); certificato Lax
  con margini misurati; Lax/Majda == J_k non singolare ESEGUIBILE
  (oltre il distacco Newton non certifica ⇒ rigetto; collasso di
  sigma_min al fold con esponente 1/2 in banda derivata). Brick C
  primo mattone interop GENO (criterio G0, scambio file READ-ONLY con
  CASES/tocnoz): throat/eps/maxtheta ricalcolati dal contorno di
  riferimento vs ini + performance.dat (err 4e-4 deg su maxtheta),
  tolleranze derivate, contorno riscalato rigettato. LIMITE DICHIARATO:
  cross-check flowfield O3.4 richiede il binario GENO (gfortran ASSENTE
  su questo host) → BLOCCATO/NEXT. VERDICT PASS complessivo.
- FASE 1 — **[F1/OP-0-gamma] DIAGRAMMA DI FASE SULLA ROUTE REALE +
  BRACKET DI EQUILIBRIO** (528e033, src/thrust/phase_diagram_real.py +
  gruppo test (xii) + data/phase_diagram_real.{json,md}): OP-11-eps
  ri-derivato sulla route primaria EOS-general (riuso bounds_gamma;
  forme chiuse in NESSUN calcolo primario) — residuo S7 di M0 Prop. 7
  SCARICATO. eps*_real dalla riduzione (**') ESEGUIBILE
  <P_E(eps;xi)>_mu = Pa (primo carrier EOS-general della riduzione
  quasi-1D di T7; forma chiusa declassata a oracolo): eps* =
  3.494..3.519 su PR 1..90; knee_real 3.49..10.38, SOTTO il knee di
  forma chiusa (~12.9 a PR=90) — l'idealizzazione calorica sovrastima
  l'envelope del peak design; struttura della mappa CONFERMATA a
  gamma(T) (colonna tie, banda cappata, zero celle bell); attainment
  M1 certificato EOS-GENERALMENTE su tutte le 41 celle knee-fitting
  INCLUSE le 11 subcritiche; strumento naive mai vincente e perdita
  stretta alle celle a spread massimo (metrica a due livelli,
  precedente bounds_gamma — onestà: gap genuinamente sotto-barra a
  PR 49/64). BRACKET DI EQUILIBRIO (shifting, solver Gibbs, c^2 =
  dP/drho su tabella): ceiling +6.34..+6.97% sopra il rung frozen su
  ogni PR (barre <= 0.003 s; known-answer cp=const PASS 1e-8, route
  corrotta rigettata) — coppia [frozen, equilibrium] = bracket di
  modello eseguibile della chiusura calorica a livello ceiling
  (THEOREM* nella coppia di chiusure ideal-gas mixture). R4 stessa
  sessione: M0 Prop. 7 REAL-ROUTE DIAGRAM INSTANCE + D3 §8. Suite
  13/13 in 201 s (12 gruppi fast attesi + esempi). Lint (vii): 7
  letterali classificati.
- FASE 1 — **[F1/P-2] RIFINITURE** (eab6cf5): footnote trappola
  lessicale 94-3264 in Lemma A §3.0 (NEXT-0 S6-rigore scaricato);
  ancore continue Prop. A2/A3 esplicite nel Lemma B (§B.6 trasporta
  l'invariante di A3; J_k^{-T} usa la non-degenerazione di A2);
  consolidamento script P-A VALUTATO e rinviato con dati (5.4 s +
  51.0 s misurati, proposta gruppo (xiii)).
- NON eseguito (dichiarato): T5 leads (Rao 1958 IAF, van Meerbeeck)
  — priorità T1>T2>T3 rispettata; resta in NEXT col vincolo di metodo
  raw-HTML.

Stato precedente (chiusura Sessione 7 — OPERATIVA: "Lemma B +
OP-0-gamma + G5-2a"; CONCORRENTE con la S6 rigore, riconciliata)

Branch `rde-nozzle-program`. Sessione lanciata come "S6 operativa"
(prompt handoff-1 di S5), RINUMERATA S7 alla riconciliazione: la S6
rigore (handoff-2, stessa giornata) ha lavorato e committato in
parallelo sullo stesso tree — TERZA violazione della regola
una-sessione-alla-volta, rilevata PRIMA dei commit come da mandato,
riconciliata senza conflitti di contenuto (hunks disgiunti; log S7
passo 10). Log a ordine totale S7:
validation/PROGRESS_2026-07-16_fase1_S7.md (gate pre-esecuzione PASS
al passo 3). Commit: T2 = 1d762f8, T3 = fb82846, T1 = (vedi log).

- FASE 1 — **[F1/P-2] LEMMA B DRAFT DI RECORD SCRITTO**
  (docs/rde_nozzle_P2_lemmaB.md = §4 del paper, implementa outline
  §4): march MOC fitted = sistema block-triangolare (B.1)-(B.3),
  THEOREM B0/B1/B2 (reverse-AD con regole implicite == back-
  substitution trasposta lungo le STESSE caratteristiche discrete;
  gemello discreto di Prop. A1), identità dot-product (B.7) = O3.1
  col g0-spike come dimostratore citabile; fronte fitted = incognita
  ESPLICITA con trasversalità Lax/Majda == non-singolarità del J_k
  locale (THEOREM finito-dim; corrispondenza col b.c. interno di
  Giles-Pierce = SCHEMA); trappola Giles-Ulbrich bypassata PER
  COSTRUZIONE (clausola di onestà: il limite di mesh resta SCHEMA,
  frontiera G12); assemblaggio ciclico = (**') PESATA, mai naive
  (THEOREM a quadratura fissa); stato gamma: identità trasposta
  CLOSURE-AGNOSTIC = EOS-general per costruzione. PENDING P-B1
  (O3.1 al mattone shock), P-B2 (test d'ordine, motore A1).
- FASE 1 — **[F1/P-2] verifica DUAL-ROUTE di Prop. A2**
  (validation/p2_pA1_symbolic_adjoint.py): il pass simbolico
  operativo, scritto in concorrenza, RICONCILIATO col filone rigore —
  non ri-reclama lo scarico P-A1' (fatto da Prop. A3): verifica
  indipendente della stessa identità di annichilazione in variabili
  CONSERVATIVE (chiusura Grueneisen EOS-general c^2 = a + b h, test
  di zero esatti via Weierstrass, covettore nullo sinistro esplicito,
  certificato rank-3, bookkeeping (L.20) eseguibile, 3 controlli
  negativi) + lemma di LETTURA DEL DATO AL BORDO psi.(K w) = -lambda2
  per OGNI soluzione aggiunta (metà "costanti<->dati" della (ii) in
  forma eseguibile; il trasporto resta Prop. A3). Nota dual-route
  registrata nel draft Lemma A sotto Prop. A2.
- FASE 1 — **[F1/OP-0-gamma] PURGA ESEGUITA A LIVELLO LADDER**
  (1d762f8): route PRIMARIA del ceiling ora EOS-general (Cantera
  h(s,P) su isentropa a composizione CJ congelata; cap sonico esatto
  via inversione di w(P) = h + c^2/2); forme chiuse DECLASSATE a
  oracoli dichiarati; barre derivate (Richardson + probe exact-flash
  + rumore misurato al punto sonico); rejector known-answer (gas
  cp=const, 4.7e-7 vs tol 1e-6; route corrotta rigettata); cap
  ri-verificato ESEGUIBILMENTE a gamma(T) (scan delle uscite
  ammissibili + perdita naive stretta alla fase subcritica profonda).
  NUMERI DI RECORD: ceiling reale -4.4% (H2) .. -7.9% (RP-1) sotto
  l'oracolo gamma_s=const sulle 12 righe a Pa finita (barre ~0.002%,
  tutti significativi); righe vuoto = strumenti LOWER-BOUND a T-floor
  200 K dichiarati. Test = run_all gruppo (xi), 18/18. R4 stessa
  sessione: M0 Prop. 7 (GAMMA-PURGE INSTANCE) + D3 §8. DEVIAZIONE
  DICHIARATA: diagramma di fase su route reale RINVIATO a NEXT.
- FASE 0 (coda) — **[F0/G5-2a] SPOGLIO DIGITALE PMM COMPLETO**
  (fb82846, validation/G5_pmm_toc_sweep_1957-1990.md): 204/204
  fascicoli 1957-90, ~4300 titoli, metodo HTML-grezzo con verifica
  conteggi (SCOPERTA DI METODO: il summarizer WebFetch FABBRICA i
  contenuti di queste pagine windows-1251 — tutto l'output
  riassunto scartato). VERDETTI: aggiunto x contornatura = ZERO hit
  in 34 anni -> G14/P-2 REGGE; nessuna ottimizzazione di forma vs
  inflow mediato/periodico, MA TOP FLAG dichiarato subito:
  Kraiko-Osipov PMM 34(6) 1970 (contorno per condizioni di volo
  VARIABILI — il cugino multi-regime della media di ciclo);
  wording G6 di P-1 CONTINGENTE alla lettura full-text (contingenza
  D4 §3 ARMATA, non attivata). Lista di lettura Item 2b prodotta.
- NON eseguiti (dichiarato): T4 (P-1 §2/§4) e T5 (estensione spike)
  — budget tempo/token assorbito da riconciliazione e purga; restano
  in NEXT.

Stato precedente (chiusura Sessione 6 — DEDICATA RIGORE: "P-A1/P-A2/
P3 + studio corpus letteratura")

Branch `rde-nozzle-program`, HEAD = 0fdbe7d (T1 = 5ec62ef, T2 =
36db818, T3 = b5590f0, T4/P-A1' = 86e6d6d, T-LIT = 0fdbe7d). Log a
ordine totale: validation/PROGRESS_2026-07-16_rigore_PA.md (passi
1-19, gate PASS al passo 4). UPGRADE DI CLASSE ottenuti:

- **Lemma A (P-2): (ii) ora THEOREM** nello scope irrotazionale
  omentropico, EOS-generale — P-A1 e P-A1' SCARICATI: Prop. A2
  (risolubilità del nucleo: i covettori di flusso annichilano il
  nucleo tangente ⇒ la risolubilità non impone nulla; l'invariante
  NON vive nell'algebra puntuale al bordo) + Prop. A3 (f2 =
  invariante aggiunto TRASPORTATO: PDE dei moltiplicatori ri-derivate
  in-house, coppia chiusa HTH-1971 le risolve per ogni flusso
  ammissibile, trasversalità terminale ⇒ V cos(θ∓α)/cosα = cost).
  Carrier: validation/pa1_symbolic_lemmaA.py, PASS 19/19 con tre
  rejector (incl. verifica macchina dell'INTERA derivazione classica
  §3.2). Ancore pubblicate trovate in-house: HTH AIAA J 9(8):1581
  (1971) p. 1583; JOTA 10(3):133 (1972) Eqs. (21)-(26). Scope
  rotazionale dichiarato nel draft (domanda utente): framework
  rotazionale-generale, forma chiusa a due campi irrotazionale;
  estensione = sistema a quattro campi di Hoffman + scuola Kraiko.
- **P-A2 SCARICATO**: lettura integrale pagina-per-pagina di Hoffman
  1967 (PDF in-house, pypdf): mappa componenti esplicita
  equation-numbered nel draft §3.4(iv) (upgrade SCHEMA→THEOREM*);
  correzione simboli (h_1..h_4, g_i, C_1, C_2); p. 673 = antenato
  1967 della Prop. A2; Eq. (54) = trasporto aggiunto pubblicato;
  E (Eq. 78) == relazione (32) non usata. Resta P-A3/O3.2 (numerico,
  motore A1).
- **P3 (gap di T7): da OPEN a THEOREM*** nella classe S1 senza urti
  (docs/rde_nozzle_P3_multipliers.md): lambda2(xi) esiste, unico (CQ
  scalare via la contrazione di Prop. A2), = -f2(dati al lip)
  (EOS-generale), misurabile + L^inf(dmu) con bound esplicito;
  residui R-P3.1/2/3 nominati; D3 §9 + M0 T7 aggiornati.
- **[F1/D2-b0bis] STUDIO CORPUS COMPLETO** (direttiva utente,
  5 agenti paralleli, sintesi docs/rde_nozzle_lit_b0bis.md):
  novelty sweep PULITO su tutto GENO/literature (nessun obiettivo
  variazionale mediato/multi-punto; un lead esterno: van Meerbeeck
  EUCASS 2013); "variable inlet" RISOLTO (JTH 1974 = inlet
  GEOMETRICO variazionale con ambiente-come-output; Rao 1961 free
  lip — DOF geometrici a stato singolo, nessuna minaccia); oracoli
  verificati alla fonte (G2 2290 lbf con precisazione diagonale;
  RaoPlug C_F 1.5804 + discrepanza 2.428/2.433 di record; frontiera
  Sternin/Rao-Beck); JOTA p. 138 = dichiarazione EOS-general
  primaria; LEAD gamma-variabile: Rao 1958 IAF Amsterdam (da
  acquisire); correzioni C1-C6; registro oracoli O-b1..O-b7 (gate R5
  prima dell'adozione); Zucrow Vol. 2 illeggibile in-macchina (buco
  dichiarato).

Stato precedente (chiusura Sessione 5 — "Fase 1: P-1 skeleton + P-2
Lemma A + G0 spike"; interleaved con S4 "G5 dispatch + venue")

Branch `rde-nozzle-program`, HEAD = b07b47e (S5: T1 = 6263c22,
T2 = 18c9d88, T3 = b07b47e; S4 interleaved: f6a5112/5540fe2/cd903d1).
Log a ordine totale S5: validation/PROGRESS_2026-07-16_fase1_P1.md
(passi 1-21, gate pre-esecuzione PASS al passo 7). Stato per fase:

- FASE 1 — **P-1 SKELETON DI RECORD SCRITTO** (6263c22,
  docs/rde_nozzle_P1_skeleton.md): struttura §1-§9 + appendici, venue
  JPP, submission gated M1+G5; MAPPA DEI CLAIM C1-C26 (classe +
  falsificatore + carrier eseguibile per ognuno, gruppi run_all
  (i)-(x) + dati di record); §7 diagramma di fase SEMANTICS-FIRST
  (D3 §10quater(5): winner = chiusure, premium_bound = dispositivo del
  torneo, (P) in forma D2.6); grep di coerenza PASS (nessun winner
  letto come hardware); regola d'accettazione (a)-(e), incl. (e) =
  STATO GAMMA per claim (direttiva permanente, sotto).
- FASE 1 — **P-2 LEMMA A DRAFT DI RECORD SCRITTO** (18c9d88,
  docs/rde_nozzle_P2_lemmaA.md = §3 del paper): lato classico DERIVATO
  PER INTERO (8 passi verificabili dalla sola Lagrangiana di Rao:
  Eq. [11] superficie caratteristica come RISULTATO, Eq. [12]
  f2 = -lambda2, Eq. [13], Eq. [14] corner == CSTR_PA + specchio C-
  == CSTR_PB) — ogni riga CONFERMATA contro il corpus page-verified
  D2 §b0, zero discrepanze; lato aggiunto: Prop. A1 (caratteristiche
  aggiunte = caratteristiche del flusso) THEOREM + bookkeeping di
  dualità; identificazioni (i)-(iii) THEOREM* (struttura derivata,
  match di componente B2/B3 PENDING O3.3), (iv) Hoffman SCHEMA (ancore
  verificate Eq. 78/p.672/p.676, mappa componenti PENDING rilettura —
  nessun numero d'equazione inventato). Registro PENDING P-A1..P-A3.
  Con la venue decisa (S4), la bozza Lemma A arma metà del trigger
  "arXiv a (G5 ∧ bozza pronta)".
- **DIRETTIVA PERMANENTE UTENTE (S5): GENERALITÀ A GAMMA VARIABILE** —
  ogni pezzo di teoria dichiara il proprio stato gamma (EOS-general vs
  gamma=const) con confine nominato e falsificatore. Primo audit di
  record: il sistema di stazionarietà classico derivato (L.6)-(L.16) è
  EOS-GENERAL (usa solo Gibbs lungo l'isentropa + def. di c²) —
  THEOREM in docs/rde_nozzle_P2_lemmaA.md §3.0 + D3 §8; confini
  gamma=const veri: biiezione corner<->eps (E4, oracolo S-H 1971
  Table 2/G2), Lemma B di T3, forme chiuse S-H a livello eps.
  Memoria: gamma-variable-generality.md.
- **DECISIONE UTENTE (S5): GENO RESTA IN FORTRAN**, a condizione che
  la funzionalità dell'INTERA pipeline sia preservata — ratifica il
  dual-code di record (M0 VI.7: motore differenziabile = codice NUOVO,
  GENO = riferimento indipendente); l'interop GENO (scambio file +
  oracolo O3.4 cross-code) diventa criterio esplicito del gate G0.
- FASE 2-prep — **SPIKE G0 JAX ESEGUITO, PASS** (b07b47e,
  validation/g0_spike_jax_moc.py): interior point + inverse wall come
  sistemi impliciti Newton avvolti in custom_vjp con regola implicita
  (mai unrolled); Jacobiano completo vs differenze centrali con
  TOLLERANZA DERIVATA (Richardson a due passi + floor di roundoff):
  52/52 entrate entro tolleranza (worst err/tol 4.6e-2), residui
  Newton ~1e-16, CONTROLLO NEGATIVO rigettato (vjp corrotto: 35/36
  fuori). Ambiente: jax 0.11.0 CPU user-level, pin numpy 2.2.6 INTATTO
  (install dichiarata, reversibile). Decisione G0 resta a Fase 2, ora
  istruita da artefatto eseguibile.
- CONCORRENZA (deviazione dichiarata, passi 14-15 del log S5): S4 ha
  lavorato in parallelo sullo stesso tree (di nuovo, malgrado la
  regola una-sessione-alla-volta); riconciliata senza conflitti
  (contenuti disgiunti); questa sessione rinumerata S4->S5.

Stato precedente (chiusura Sessione 3 — "Fase 1: OP-11-eps + P-2 +
G5"): HEAD = e23bb08 (T1 = 1438b1b, T2 = 05001a5, T3 = e23bb08).
Stato per fase (piano D6):

- FASE 1 (fondazioni quasi-1D): **OP-11-ε CHIUSO** (1438b1b).
  - Diagramma di fase quasi-1D di record: src/thrust/phase_diagram.py,
    griglia 90 celle (ε_max × PR a ⟨Pc⟩ fissata, ancora CH4/O2 20 atm)
    + sweep vuoto; ladder OP-0 riusata per cella (check_chain rieseguito;
    a PR=1 la firma di degenerazione è ASSERITA, non saltata); test
    (x) con 22 check e 8 controlli negativi (rigetta topologie vincenti
    sbagliate, oracoli T3/T4 espliciti); figura P-1
    figs/phase_diagram_op11.png; suite completa 11/11 PASS (441 s).
  - DUE RISULTATI THEOREM-GRADE retro-propagati (R4, stessa sessione)
    in D3 §10quater + M0 Prop. 7 + D4: (i) con la chiusura di
    adattamento CAPPATA AL SONICO il plug domina puntualmente il bell —
    nessuna regione bell stretta a livello ε; (ii) il plug cappato
    raggiunge il ceiling cappato a ε_max ≥ knee su OGNI cella Pa > 0,
    INCLUSE le 9 celle subcritiche: attainment M1 esteso oltre le 8
    righe supercritiche di OP-0 (l'ipotesi supercritica appartiene solo
    alla chiusura naive pubblicata, che a ε_max = 1 inverte perfino il
    ranking bell/plug — artefatto eseguibile, test-rigettato).
  - Struttura della mappa: tie = {PR=1} ∪ {ε_max=1} ∪ {ε_max ≤
    ε*(Pc_min)}; banda plug-cappato (regime genuinamente mediato,
    sezione di PB-2); regione M1 ε_max ≥ knee. Il duty split NON è
    esprimibile a livello ε: OP-11 a livello contorno resta CONGETTURA.
  - SCOPE REMARK di record (addendum post-chiusura su challenge utente,
    D3 §10quater(5) + M0 Prop. 7 + modulo/md/esempio): i "winner" del
    diagramma ordinano CHIUSURE a parità di ε_max, NON i settori
    hardware del problema vincolato (P) di D2.6 — il plug cappato
    rilasciato È la rilassazione per-fase, quindi la sua dominanza
    prezza il PREMIO DI ADATTAMENTO e non decide (P); la topologia di
    S*(c) è l'OUTPUT del torneo di settori al vero vettore di vincoli
    (non a priori {bell, plug, shrouded}); regioni bell-vincenti di (P)
    sono ATTESE a livello contorno. Dispositivo per il torneo:
    premium_bound = ideal − bell per cella (THEOREM geometry-free, a
    meno della barra C4 del surrogato bell; max 64.7 s a (PR=90,
    ε_max=1)), persistito e con rejector; una banda di perdita
    certificata di settore > premium_bound chiude la cella per il bell
    con δ-certificato D2.6(iv) — la banda EMPIRICAL di troncamento
    (ADR D4, in attesa di ratifica) è la prima candidata.
  - P-2: **OUTLINE DI RECORD SCRITTO** (05001a5,
    docs/rde_nozzle_P2_outline.md): Lemmi A/B con classi di rigore e
    falsificatori, tre sponde citate, piano oracolo O3.1-O3.4,
    proposta venue (AIAA J primaria; Aerospace/JOTA alternative) —
    DECISIONE VENUE ALL'UTENTE. Stesura Lemma A = prossimo passo P-2.
- FASE 0 (coda): G5 **testo di commissioning PRONTO** (e23bb08,
  validation/G5_kraiko_pmm_commission.md) — SOLO TESTO, nessun invio:
  spedizione e destinatario sono dell'utente.

Stato precedente (chiusura Sessione 2, HEAD = 92cb8ea):

- FASE 0: **CHIUSA FORMALMENTE**. A0.1 completata: citazioni corrette
  propagate INLINE nelle note storiche (Li-Xu-Huang 2022 / Mo 2015
  spaccate con nota di conflazione; caveat Sternin→Pirumov-Roslyakov)
  e gate grep-di-controllo PASSATO fuori dai banner (92cb8ea; record
  del gate in validation/PROGRESS_2026-07-16_fase0_OP0.md, passo 17).
  Suite completa 9/9 PASS (59 s), incl. i due nuovi gruppi (viii)
  bounds e (ix) gamma probe, entrambi con rejector.
- Sessioni 1 e 2 hanno lavorato in concorrenza sullo stesso working
  tree (checkpoints f4cd429/ae9f109/9b2bcde vs 1a4ff7b/e77f63b/92cb8ea):
  nessun conflitto di contenuto; da ora una sola sessione alla volta.

Stato precedente (chiusura Sessione 1, HEAD = f4cd429):

- FASE 0 (consolidamento): **COMPLETA**.
  - Baseline M0 + D1-D7 committata (4565a6b/4565be6).
  - A0.3 probe γ: FATTO (f4cd429) — numeri di record: γ_s 1.1537→1.2093
    confermato; shift ε* = −0.56% (lo stantio −1.9% ELIMINATO, origine
    = media non pesata −2.39%, ora test-rigettata); penalità Isp
    −0.00028% (secondo ordine confermato, penalità ≤ shift²); prima
    conferma eseguibile della chiusura γ_eff. Test (ix), 12/12 PASS.
  - A0.1 bonifiche bibliografiche: banner aggiornati; grep di controllo
    residuo da fare a inizio Sessione 2 (voce NEXT).
  - Convergence pass su M0: E8 trovato-e-corretto (canonicità
    debole-forte con urti declassata; BDS CMP 305:351-361 (2011)
    VERIFICATA); Lemma B rinominato; Prop G-B con V_id esplicita;
    Teorema 6 con misurabilità/raggiungimento.
  - Concordanze col campo (M0 Parte III): EAP (Kaemming-Paxson 2018,
    full text NTRS) = coordinata-pressione di J_ideal; S-H (JSR 2019,
    spec full-text in ../project_build + validazione 18/18) = le loro
    Fig.9/Figg.10-12/Table-1-vuoto sono istanze di T3/T4/no-ottimo;
    check quantitativo chiuso-forma (bell 3-5%, spike 6-14%,
    φ-shift-consistente); φ collocato come parametro esterno annidato
    del generatore (max_φ max_Σ, lattice certificato `phi_opt`).
- FASE 1 (fondazioni quasi-1D): **AVVIATA** (in anticipo sul piano).
  - OP-0 bound ladder ε-level: FATTO (1a4ff7b) con rejector test,
    18 righe Table-1 (src/thrust/bounds.py + data/bounds_ladder.*).
    SCOPERTA retro-propagata (regola R4, già applicata): il piolo G-B
    naive richiede il CAP SONICO (choking) — M0 Prop. 7 e D3 Prop. G-B
    affilati di conseguenza; raggiungimento gap-zero M1 confermato
    sulle 8 righe supercritiche a livello del mare.
  - OP-11-ε (diagramma di fase): NON iniziato.
  - P-1 stesura: NON iniziata (outline P-2 nemmeno — è time-sensitive).

## NEXT (ri-fondato 2026-08-06, chiusura S17 — brick 2 APERTO,
## kickoff completo; il completamento del brick è gated sulla
## mini-sessione production-code)

1. [PRIMA COSA — PRODUCTION-CODE MINI-SESSION, poi RUN FINALE DEL
   BRICK] Le leve emendate dal pass avversariale (kickoff doc
   §5bis), OGNUNA col suo gate: P1 Newton replay -> lax.while_loop
   su metrica di certificazione, damping conservato (gate: X-SCANM
   equivalenza ri-passa); P2 bucket-per-fase + whole-loop jit con
   guardia safe-where (gate: T2a ri-run — il GATE DI PRODUZIONE
   resta CHIUSO finché non passa; O3.1 = detector di leak); P3
   cablaggio due-binari della chiusura C^1 (X-THC1 primaria per il
   brick, lineare per il twin GENO; gate: banda C5); sharpening del
   rejector di margine (floor delta d'istanza, non solo > 0). POI:
   run end-to-end OPT+oracolo+trasversalità (morto OOM in S17 —
   infrastruttura, non metodo) => chiusura brick 2 e SBLOCCO O3.3
   (protocollo pre-registrato P2_outline §5, intatto).
2. [RIGOR, panchina invariata] B1 certificazione intervallare s_L
   su K_delta (scarica U3-H1, arma S-ACFR-B1); C-XBVP(b); B3
   g-scan; concavita' composita GBE; C-P4RZ/fallback.
3. [CODA decisa] census-lemma session + PAP-RIM (ordine relativo da
   decidere allora); head-to-head SOS (solver DECISO S17: Clarabel
   primario, MOSEK accademico fallback — lock utente sciolto);
   meccanizzazione lint (xvii); acquisizioni -> G5.
4. [BLOCCATO->utente] G5 send (time-box); ratifiche ADR + census;
   email dataset GV; dataset RDE pubblico (RK-E); DECISIONE
   PREPRINT (RK-A ripesato in S17 passo 3 e RIPRESENTATO: con
   O3.3 a un passo, la finestra-scoop si stringe — la
   raccomandazione di record è armare il trigger arXiv appena i
   numeri O3.3 atterrano; la decisione resta tua).

[VOCE PRECEDENTE (chiusura S16, ri-aggiudicazione ESEGUITA in S17):]
## NEXT (aggiornato 2026-08-06, chiusura S16 — seconda tranche
## COMPLETA; la campagna fondazioni ha esaurito la coda [RIGOR/A]
## nominata: ORA TOCCA ALLA RI-AGGIUDICAZIONE DEL BRICK 2)

1. [FATTO 2026-08-06, S17 log passo 3 — VERDETTO: rinvio #4 SCADUTO,
   BRICK 2 PARTITO in S17 con le duties (a)-(d) + aggiunta c4/G>0;
   RK-A ripesato e decisione preprint ripresentata all'utente (lock
   invariato); D6 item 9 annotato con la ri-aggiudicazione datata.]
   [PRIMA COSA — RI-AGGIUDICAZIONE RINVIO BRICK-2] Il waiver S15
   (rinvio #4, RK-A citato, controlli compensativi i-iii) vincolava la
   ri-aggiudicazione alla FINE della campagna fondazioni: con la
   seconda tranche completa (U3/U4, a-contraction, ledger p2, G-B
   ergodico, S-LBML) la campagna dichiarata S15-S16 è ESAURITA nella
   sua coda [RIGOR/A] di registro. La prossima sessione APRE con la
   ri-aggiudicazione ai termini del waiver (S15 log passo 2): atteso
   verdetto = BRICK 2 PARTE (TOC variazionale, D6 item 9, kickoff
   duties vincolate: soglia loop-speed derivata, scan/vmap, policy
   RK-G, duty THERMOTAB C^1 — a cui S16 aggiunge il canale c4/G>0);
   ogni ulteriore rinvio richiederebbe un NUOVO ordine utente
   esplicito con RK-A ripesato.
2. [RIGOR, dopo/durante brick 2 — mattoni nominati dalla S16]
   B1 = certificazione intervallare di s_L su K_delta (scarica U3-H1
   E arma S-ACFR-B1 con la stessa macchina — terzo/quarto payoff del
   substrato condiviso [PAP-GMAX]); C-XBVP(b) (tracce Dafermos);
   B3 g-scan (economico); concavità composita GBE globale (piccolo
   brick simbolico/intervallare); C-P4RZ o fallback Kilque/CGW.
3. [CODA] census-lemma session (emendamenti D2.1/D2.6 +
   C1-C3 + CEN-O4/O5 + carrier; DOPO il brick 2 per sequenza decisa);
   [NUOVO 2026-08-06, ordine utente post-chiusura (log S16 passo 9;
   memoria roads-insertion-matrix-directive)] sessione PAP-RIM (ID
   da coniare al suo kickoff, pattern C-N2):
   censimento formale strade x punti-di-inserzione (11 slot x famiglie
   classiche+ML+esotiche; 4 campi obbligatori per cella: contratto
   dello slot / test formale citabile / verdetto / falsificatore;
   niente matematica nuova salvo richiesta dal contratto — DIR-SUFF
   riaffermata) — IN CODA DOPO IL BRICK 2 (pin utente), ordine
   relativo con census-lemma da decidere allora; fino ad allora
   NESSUN verdetto di strada coniato in chat;
   head-to-head SOS (gate env: solver SDP = decisione utente); spike
   interval-Newton cella MoC; meccanizzazione lint (xvii) (D6 item
   16 PROPOSED); acquisizioni -> G5 (+ page-verify L-X-H/Liu/Harroun
   dai passi S15-13/19; Li-Yu page anchors; query novità T-XWALL +
   a-contraction-BVP dichiarata in S-ACFR §6).
4. [BLOCCATO->utente] invariati: G5 send (time-box); ratifiche ADR +
   census; email dataset GV; dataset RDE pubblico (RK-E); decisione
   preprint (RK-A, armata durante il waiver — NOTA: la
   ri-aggiudicazione di NEXT-1 la ripesa).

[VOCE PRECEDENTE (chiusura S15, eseguita nella seconda tranche):]
## NEXT (aggiornato 2026-08-05, chiusura S15 — campagna in corso,
## SECONDA TRANCHE)

1. [FATTO 2026-08-05, log passi 13-14] T2 resume ESEGUITO: 27/27
   aggiudicati, 21 fix eseguiti, residuo D8 §8 CHIUSO (commit
   1f51da2). Debiti nuovi nominati dentro i fix: pin census O1/O2
   (utente), C-N2 (kickoff PB-2), meccanizzazione gruppo (xvii).
2. [FATTO 2026-08-05, log passo 15] U2 brick ESEGUITO ([T-U2RG],
   b2610d1: no-glancing a slip + locus sonico + R chiuso). RESTANO di
   questa voce: U3/U4 (composizione, costo bounded); attacco
   a-contraction a C-MAJDA/U3; lemma G-B ergodico o de-rate; S-LBML;
   acquisizioni -> G5 (+ Li-Yu page anchors, + query di novità
   T-XWALL, + page-verify Liu 2022/Harroun 2021/L-X-H 2022 dai passi
   13/19).
   [AGGIORNAMENTO 2026-08-06, log passo 20 — CENSIMENTO COMPLETO:
   la sessione censimento è chiusa con TUTTI i pin utente decisi
   2026-08-02 (advisory §7pin + memoria topology-census-pins: cono
   su Omega/Chenais; O1 PERMISSIVA; O10 NONBLOCK+; O11 Lambda =
   cerchi di labbro; O2/O9 dissolti). La sessione census-lemma
   (lemma + emendamenti D2.1/D2.6 + C1/C2/C3 + prove CEN-O4/O5 +
   carrier + registro) è IN CODA DOPO IL BRICK 2 per sequenza decisa
   dal censimento; ratifica advisory = lock utente.]
3. [FATTO 2026-08-05, log passo 16] MATTONE SUBSTRATO ESEGUITO
   ([X-IVXC] PASS + [T-XRED], ab7725b: C-XBVP(a) scaricata a
   istanza; Card 1 eseguita). RESTANO: head-to-head SOS (gate env:
   serve un solver SDP — decisione utente/ambiente); spike
   interval-Newton su UNA cella MoC (go/no-go card 2a/3, ora
   de-rischiato dal method record).
4. [RIGOR/B] Ledger ipotesi passata 2 (target nominati in [PAP-D9HL]
   §3: L4-default, promozione caso D, C-XBVP(a), U3/U4).
5. [BLOCCATO->utente] invariati: G5 send (time-box); ratifiche ADR +
   census; email dataset GV; dataset RDE pubblico (RK-E); decisione
   preprint (RK-A, armata durante il waiver).
6. [POI] BRICK 2 con duties vincolate (D6 item 9) — ri-aggiudicazione
   del rinvio a fine campagna, invariata.

[VOCE PRECEDENTE (apertura S15, eseguita nella prima tranche):]
## NEXT (ri-fondato 2026-08-04, ordine utente S15 — CAMPAGNA
## "FONDAZIONI PROFONDE"; waiver della protezione brick-2 ESERCITATO
## e loggato con RK-A citato + controlli compensativi: log S15 passo 2)

1. [RIGOR/A — registro aperto, depth-first] U1-U4 scritte per davvero
   (test del claim di costo) -> scarico C-D25U-a/-b; U5 via
   Breitkopf-Ulbrich 2025 (acquisire) + Bressan-Guerra/Ulbrich;
   attacco a-contraction a C-MAJDA/U3; rotta C-P4RZ (Riesz vs
   Kilque/CGW); lemma Cauchy->BVP (entropia relativa in x); lemma G-B
   ergodico o de-rate; S-LBML scritto; census lemma settori + decisioni
   A_gen (utente); LEMMA CARICO LATERALE ROTANTE (regola di selezione
   m=1; carrier simbolico; disposizione in c o output secondario);
   sweep seconda-lente del residuo D8 §8; acquisizioni -> G5.
2. [RIGOR/B — minimizzazione ipotesi] ledger con verdetto obbligatorio
   {SCARICATA / INDEBOLITA / NECESSARIA(controesempio) / PREZZATA}
   per OGNI ipotesi H-* e condizionale — teoria autosussistente.
3. [RIGOR/C — massimo globale] dossier di record: ladder più stretta;
   ricerca globale CERTIFICATA sulla classe finito-dim certificata
   (B&B Lipschitz/intervallare, gerarchie momenti/SOS, deflazione) —
   ogni via fino in fondo con verdetto adopt/kill; non-convessità
   quantificata; torneo di settori (dipende dal census lemma).
4. [ORDINE/D] SCAFFOLD L0-L6 completo; banner currency D4/D5; mappa
   M0 VII + riga D8; docstring con ID; indice carrier; lint (xvii);
   X-A1IM-lite in tier rigor; mappa-tesi (capitoli <-> ID registro).
5. [BLOCCATO->utente] G5 send (time-box); ratifiche ADR + census;
   email dataset GV; dataset RDE pubblico (RK-E); decisione preprint
   (RK-A, resta armata durante il waiver).
6. [POI] BRICK 2 (ri-aggiudicazione del rinvio a fine campagna,
   dichiarata): riparte con banco O3.3 pre-registrato, norme, RK-G,
   duty THERMOTAB — tutto già vincolato in D6 item 9.

[VOCE PRECEDENTE (S14, superseduta dal waiver — conservata):]
1. [F2/A1 — BRICK 2, PROTETTO] FINALMENTE il TOC variazionale
   (dJ/dSigma + TR-SQP + (**')/corner su [X-A1IM]): NESSUN quarto
   rinvio senza gate failure (D6 item 9, regola di record). KICKOFF
   DUTIES vincolate (D6 item 9): soglia loop-speed DERIVATA
   (protocollo clean-host), architettura scan/vmap di colonna,
   policy RK-G (topologia fissa in trust region + re-record +
   kink detection), duty THERMOTAB C^1 (interpolante Hermite +
   invarianti cp=dh/dT, s0'=cp/T + rejector). Sblocca O3.3 col
   protocollo PRE-REGISTRATO (P2_outline §5: coordinate (30)/(31)+f2,
   norme lip-escluse, controllo capturing a livello campo).
2. [F1/mu + F4-prep] BUNDLE STRUMENTI-MU (D6 item 15, una sessione):
   chiude l'eseguibilità dei falsificatori D-JEX/T-O2/D-MU; aggancio
   GV Table-8 testbed. Poi O5-lite + riproduzione GV (item 10, basi
   Morris exit-BC).
3. [PANEL-residuo] Verifica a seconda lente del residuo D8 §8
   (onda D5/D4, shape-topology, roads-atlas, lint (xvii)) — una
   sessione di verifica bounded, deterministica (finding embedded).
4. [BLOCCATO->utente] G5 send (time-box + estensioni di record);
   ratifica ADR + census topologico; email dataset GV; dataset RDE
   pubblico (RK-E).
5. [F2-prep/BLITE] mattone G12-L1-3D (invariato, dopo il brick 2).

[VOCE PRECEDENTE:]
## NEXT (Sessione 14 — consolidato S13)

1. [F2/A1 — BRICK 2] TOC variazionale (invariato; sblocca O3.3 — col
   banco oracoli CORRETTO S14: compatibilità L-P 2025 (30)/(31) +
   drift f2, protocollo pre-registrato in P2_outline §5; gli
   invarianti (32)-(34) solo su patch a flusso costante).
2. [LEADS coda] Owens-Hanson + Morris + Lozano-2018 + reference-list
   L-P; G-U Part 2 = upload utente (SINUM 48:905-921).
3. [F1/GV + F4-prep/O5-lite] riproduzione GV + build pre-registrato
   (D6 A4).
4. [F2-prep/BLITE] mattone G12-L1-3D poi march.
5. [F1/P-1] appendici + assembly (§4.5 AGGIUDICATA — un blocco in
   meno; resta G5).
[VOCE PRECEDENTE S12→S13:]


1. [F2/A1 — BRICK 2, il mattone VARIAZIONALE] invariato da S11 (voce
   sotto, era NEXT-1): TOC via dJ/dSigma + TR-SQP + (**')/corner sul
   motore [X-A1IM]. IN PIÙ (S12): questo brick SBLOCCA O3.3 (match
   forma-chiusa vs adjoint AD su un caso TOC = metà numerica di P-2,
   scarico di C-O33) — eseguirlo per primo.
2. [F1/GV + F4-prep/O5-lite] Riproduzione rung-2 di González-Viana
   con la LORO misura (D6 A2, macchina eps-level esistente) + build
   O5-lite col protocollo PRE-REGISTRATO (D6 A4: predizioni P-i/P-ii/
   P-iii + rejector, dichiarate PRIMA di girare).
3. [F2-prep/BLITE] Mattone simbolico G12-L1-3D (carrier stile pa1),
   poi dimostratore di marching elicoidale (D6 A5).
4. [LEADS] Sessione page-verify al rientro dei PDF (registro
   acquisizioni in D2/D6 item 12; Kraiko-Osipov = priorità 1).
5. [F1/P-1] Appendici A1-A7 + assembly (body text completo; wording
   §4.5 resta CONTINGENTE a Kraiko-Osipov).
6. [L6, opzionale] Carrier T-NSW.
[VOCE S11 ORIGINALE del brick 2, invariata nel merito:]

1. [F2/A1 — BRICK 2, il mattone VARIAZIONALE] TOC alla Rao IMPOSTO
   ALLA FORMULAZIONE sul motore [X-A1IM]: obiettivo spinta + vincoli
   {eps, L, lip}, con la trasversalità (**')/corner come condizione
   di stazionarietà raggiunta VIA GRADIENTE dJ/dSigma (reverse-AD
   della marcia = Lemma B, già certificato O3.1) dentro TR-SQP —
   MAI outer-loop hard-coded (il Mrao/eps loop di GENO type 2 è solo
   riferimento cross-code). Oracolo: contorno tocnoz di GENO
   (riferimento committato 1e-10) + kernel; tolleranze derivate
   (Richardson di marcia); X-GENOXC regressione permanente. Poi:
   sheet trasversale fitted ereditata (residuo P-B1 march-level) e
   plug free-boundary.
2. [F1/P-1] Appendici A1-A7 (import prove da M0) + ASSEMBLY del paper
   con la claim-map completa (il body text è COMPLETO).
3. [F0/G5, SOLO UTENTE] Invio email biblioteca (pacchetto pronto,
   validation/G5_dispatch_email.md + lista Item 2b + full text Rao
   1958 IAC). Alla risposta: Kraiko-Osipov PMM 34(6) 1970 full-text e
   scioglimento della contingenza §4.5/G6 di P-1.
4. [L6, opzionale] Carrier simbolico banale per T-NSW (candidato L6
   nel registro).
[FATTO in S11: ex-NEXT-1 (brick 1: marcia assemblata + ugello ideale
+ confronto GENO end-to-end + backend tabulato + O3.1 marcia intera)
= 8fc815e; ex-NEXT-2 (P-1 §1/§3/§8/§9 — body text completo)
= c0065af. FATTO in S3-S10: vedi voci precedenti.]

## BLOCCATO / GATE APERTI

- G5 (umano, biblioteca): blocca le SUBMISSION P-1/P-2/P-3, non il
  lavoro. PACCHETTO D'INVIO PRONTO (S4): email completa in
  validation/G5_dispatch_email.md, destinatario web-verificato
  bibliotecaboaga@uniroma1.it (ILL Boaga; DD anche via NILDE con
  credenziali IDEM-GARR). RESIDUO UTENTE: solo l'invio dall'account
  istituzionale (l'assistente non ha canale email autorizzato; per
  invii diretti futuri autorizzare il connettore Gmail su claude.ai).
  Item 2a (spoglio TOC PMM): **FATTO in S7** (fb82846,
  validation/G5_pmm_toc_sweep_1957-1990.md — 204/204 fascicoli;
  G14 regge; wording G6 di P-1 CONTINGENTE alla lettura full-text di
  Kraiko-Osipov PMM 34(6) 1970, TOP FLAG). Item 2b: lista di lettura
  RANKED pronta nel deliverable — da allegare alla richiesta
  biblioteca insieme all'Item 1 (TOC Kraiko 1979).
- Venue P-2: **DECISA (S4, delega utente)** — AIAA Journal primaria +
  preprint arXiv a (G5 pass ∧ bozza Lemma A pronta); fallback
  Aerospace con trigger dichiarati; JOTA terziaria. Decisione di
  record con evidenze in docs/rde_nozzle_P2_outline.md §7. NON PIÙ
  BLOCCANTE.
- ADR panel 2026-07-16 (validation/ADR_panel_2026-07-16.md, NON
  committato): IN ATTESA DI RATIFICA UTENTE — nessuna implementazione
  avviata, per disciplina.
- G0: **DECISO in S10** (bfd0063; dossier
  docs/rde_nozzle_G0_decision.md, [DIR-G0]): JAX primario,
  Julia+Enzyme alternate, GENO dual-code; il residuo toolchain è
  stato CHIUSO (GENO compilato in WSL, contorno 1e-10, X-GENOXC
  PASS). NON PIÙ BLOCCANTE. Ratifica utente attesa SOLO se emergono
  trade-off fuori dai criteri D6 (es. preferenza strategica
  single-language); falsificatore loop-speed armato (flip a
  Julia/Enzyme se il loop A1 assemblato è impraticabile).
- RaoPlug S1/S2 (GENO): prerequisito di OP-2/PB-2, non ancora attaccato.

## LOG SESSIONI

- **S13 (2026-07-21/22, LEADS/PAGE-VERIFY su ordine utente)** — Gate
  PASS (passo 2). K-O 1970 letto personalmente e AGGIUDICATO
  (containment; P-1 §4.5 riscritta, M0/D2/D4 aggiornati); C-S e
  Lozano-2019 verificati via agenti con quote a pagina (locus Lemma B
  §4.4 corretto — trovato-e-fixato); G-U Part 1 e L-P 2025 verificati
  personalmente (Prop. A1 = loro det-trasposto; oracoli O3.3 pronti;
  Part 2 G-U mancante). Deviazione di processo dichiarata e riparata
  (passo 7: commit chain non guardata). Tre agenti persi per session
  limit (rifatti in proprio). Commit: d951d4c, b2771a3, 022b9b2 +
  chiusura. Coda dichiarata ai passi 10-11.

- **S12 (2026-07-21, RIGORE/R4 su ordine utente: "retro-propagazione
  della review-conversation + piano rafforzato"; UNICA sessione,
  check pre-commit puliti)** — Gate PASS (log passo 3; il "sessione"
  retro-propagata è la conversazione di review 2026-07-20/21, con
  carrier scratchpad promosso a norma). C1+C2 (981c620): T3-QS
  [T-T3QS] con carrier X-T3QS (P1-P6 + R1-R3, EOS-general, PASS) =
  gruppo (xvi); doc T3QS con anatomia fisica e confini; addenda M0
  (Teorema 0, D2.6 [D-GSEP], Parte V [S-BLITE]) + D3 §3; registro +5
  voci, lint 0 violazioni. C3 (4f12068): D6 rafforzato (O5-lite
  PRE-REGISTRATO su tre predizioni T3-QS; B-lite primo item A5;
  benchmark GV in A2; 90-giorni 9-14 con ancora sperimentale e piano
  compute; rischi RK-E/RK-F) + D2 (riga GV full-text con attribuzione
  a tre vie + registro acquisizioni con priorità e stati di
  verifica). SUITE 15/15 in 101 s. DEVIAZIONE DICHIARATA: NEXT-1 di
  S11 (brick TOC) ri-prioritizzato a S13 su ordine utente; commit
  C1+C2 combinato (i tre addenda condividono M0). Verdetti: lint
  verde, carrier PASS, nessuna concorrenza.

- **S11 (2026-07-20/21, "FASE 2/A1 BRICK 1: machinery di generazione
  profili + P-1 body text completo"; sessione UNICA; log
  validation/PROGRESS_2026-07-20_fase2_S11.md, 14 passi, gate PASS al
  passo 3)** — T1 (8fc815e): [X-A1IM] marcia MoC differenziabile
  ASSEMBLATA che GENERA l'ugello ideale end-to-end (gemello GENO
  type 0), VERDICT PASS 14/14: contorno vs GENO 7.6e-9 (62/62 in
  banda derivata), Me a 8.4e-9, O3.1 marcia intera 2.7e-10 vs 5.1e-8,
  2756 celle certificate z-space, 4 rejector (incl. rigetto PER
  RIFIUTO della sorgente corrotta); backend a TABELLE
  [DIR-THERMOTAB] (Cantera unico generatore di produzione; NASA-poly
  solo istanza interop; ordine NasaPoly2 determinato empiricamente;
  budget di costanti derivato). R4: M0 VI addendum + D6 A1 BRICK 1
  DONE + Lemma B march-level + registro 89 voci (PAP-P1S57
  found-and-aligned). Trail onesto a log: NaN celle soniche →
  predictor GENO + Newton smorzato; compile XLA → fori_loop; probe
  cella-per-cella vs griglia GENO (fan ≡ GENO 3.5e-4, colonna 22 ≡
  GENO 1e-6); metrica di certificazione resa unit-consistent; N1
  crash scambiato per SKIP → struttura except corretta e verdetto
  rilanciato pulito. T2 (c0065af): P-1 §1/§3/§8/§9 di record
  ([PAP-P1S1389]; Rao 1958 IAC abstract-verified-only in genealogia;
  confine N6 theorem-grade; bridge EAP/S-H; grep PASS) — BODY TEXT
  COMPLETO, restano appendici + assembly. Deviazioni dichiarate:
  caso GENO ridotto (NI=21) per il confronto end-to-end (risoluzione
  di produzione = falsificatore loop-speed G0, armato); T3 (L6
  T-NSW) non eseguito; `literature/` untracked non mio, non toccato.

- **S10 (2026-07-17/20, "APERTURA FASE 2: G0 + P-1 §5-§7 + leads";
  sessione UNICA, tre check pre-commit puliti; log
  validation/PROGRESS_2026-07-17_fase2_S10.md, 14 passi, gate PASS
  al passo 3)** — T1 (bfd0063): G0 DECISO — GENO compilato in WSL
  (gfortran 11.4.0, zero installazioni: toolchain e LAPACK conda
  preesistenti; submodule via HTTPS non-persistente, GENO mai
  toccato/committato), tocnoz rigenerato (contorno = riferimento a
  1e-10; convenzione md5 N-36 letta e confermata), carrier
  cross-code X-GENOXC (residuo EOS-general 218/218 in banda di
  troncamento derivata + riproduzione due-punti→punto 95%, controlli
  negativi rigettano; onestà di metodo a log: fit d'ordine
  cross-field abbandonato perché mal posto), decisione JAX primario
  (grad/solve ~1.01 misurato standalone) con falsificatore armato;
  R4: M0 VI.7 + D6 (A1 APERTA). SCOPE dichiarato su challenge
  utente: certificato l'interior unit process, NON la generazione
  profili (nessun contorno jax esiste ancora → A1 brick 1, NEXT 1).
  T2 (570b38c): P-1 §5-§7 testo pieno (boxed warning naive, purga
  −4.4..−7.9%, bracket +6.3..+7.0%, §7 semantics-first + route
  reale §7.5bis; class refresh dichiarato; grep coerenza PASS).
  T3 (0fb6a21): lead chiusi — Rao 1958 IAC identificato e
  abstract-verificato (var-gamma precedente 1958 a stato singolo ⇒
  citazione obbligatoria, novità intatta, full text in coda G5);
  van Meerbeeck EUCASS 2013 letto integrale (puntuale, zero
  obiettivo mediato, G14 regge). SUITE 16/16 in 213 s (host sano).
  Deviazioni dichiarate: T4/T5 non eseguiti; q_mapping datestamp
  ripristinati due volte; cambio modello in-sessione su comando
  utente.

- **S9 (2026-07-17, ORDINE DI PROGETTO [F1/SCAFFOLD-M]: "migrazione
  M-1..M-5 + riallineamento D6 + pulizia"; UNICA SESSIONE ATTIVA —
  nessuna interleaving rilevata ai sette check pre-commit)** — Gate
  pre-esecuzione PASS (log passo 4: aderenza piena T1-T7; audit del
  seed §2 contro il tree con OTTO delta di completamento dichiarati e
  poi censiti in M-1). Esecuzione M-1 → M-5 → M-2 → M-3 → M-4 → T6 →
  T7 (deviazione d'ordine M-5<M-2 DICHIARATA al passo 6: il check
  carrier-in-suite del lint presuppone la promozione; mai suite rossa
  committata). Commit: 898f480 (M-1 registro 83 voci), 8a2c946 (M-5
  gruppi (xiii)/(xiv), runtime standalone misurati), 5aa71dd (M-2
  lint gruppo (xv), rejector triplo dimostrato ad ogni run), 605306c
  (M-3 spine su M0, 29 righe solo-tag, diff ispezionato), 7e1dfa9
  (M-4 ledger L4 + pass riferimenti THEOREM* 22 inserzioni +
  TROVATO-E-ALLINEATO: due righe di classe stantie in lemmaA vs gli
  scarichi S6, annotate con supersessione datata), b2b3570 (T6 D6
  delta-pass solo-stati), 2fc6222 (T7 pulizia + INDEX.md). SUITE:
  16/16 PASS exit 0 (run pieno; wall gonfiato da contention
  auto-inflitta dichiarata al passo 9 — incidente operativo con
  lezioni pinnate: tasklist mai ps MSYS, mai run concorrenti, output
  su file); --fast pulito 14/14 in 448 s con caveat host degradato
  (gruppo (i) 368 s da solo; tier decisi sui runtime standalone).
  DEVIAZIONI DICHIARATE: kind `paper` e tag n/a nel registro (passo
  5); esenzione on-demand per gli spike jax; T-NSW declassato a
  suffices=no con candidato L6 nominato. CLAUDE.md R2 NON toccato
  (non mandato): il nuovo protocollo d'apertura vive nell'header di
  questo file + memoria. Verdetti: migrazione COMPLETA, lint verde,
  zero violazioni, zero matematica toccata.

- **S8-operativa (2026-07-16/17, "P-1 §2/§4 + spike axisym/shock +
  diagramma reale"; concorrente con S8-rigore e coi commit SCAFFOLD —
  quinta e sesta interleaving, riconciliate)** — Gate pre-esecuzione
  PASS (log passo 2, cinque ancore di rigore ri-verificate senza
  delta). T1 (a4e4964): testo pieno di record P-1 §2+§4
  (docs/rde_nozzle_P1_sections_2_4.md, regole (a)-(e) per
  sottosezione, riga pedagogica Lemma T3-C, novità §4.5 condizionale
  su Kraiko-Osipov, naming guard, grep coerenza PASS). T2 (001aecc):
  spike gemello g0_spike_axisym_shock.py VERDICT PASS — axisym
  dual-route con rejector d'ordine, shock point RH implicito con
  O3.1 (P-B1 SCARICATO a livello brick, registro Lemma B aggiornato
  R4), trasversalità Lax/Majda == J_k eseguibile (fold exponent 1/2
  in banda derivata; il fattore arbitrario 10x della prima stesura
  FALLIVA onestamente ed è stato sostituito dalla legge di scaling
  derivata — deviazione dichiarata), interop GENO read-only
  (limite flowfield dichiarato: gfortran assente). T3 (528e033):
  diagramma di fase sulla route REALE + bracket di equilibrio
  (phase_diagram_real.py, gruppo (xii) 20/20, eps*_real = primo
  carrier EOS-general della riduzione (**'), knee reale sotto
  l'oracolo, M1 EOS-general su 41 celle incl. 11 subcritiche,
  bracket +6.3..+7.0%; fix dichiarati: floor tabella Pa/8→Pa/64
  derivato, ChemEquil→Gibbs solver, metrica naive a due livelli
  dopo scoperta sub-barra onesta); R4 in M0 Prop. 7 + D3 §8. T4
  (eab6cf5): footnote 94-3264 + ancore A2/A3 nel Lemma B +
  consolidamento P-A valutato/rinviato con runtime misurati.
  DEVIAZIONI DICHIARATE: T5 non eseguito (→ NEXT 4); suite 13/13 in
  201 s (12 fast + esempi); due eventi di concorrenza riconciliati
  con audit hunk pulito (passi 5, 8; commit sempre path-limitati;
  q_mapping.* modificati da altri MAI toccati né staged). Verdetti:
  gate PASS; spike PASS; diagramma 90/90 + bracket OK; suite verde.

- **S8-rigore (2026-07-16, "attacco G12", concorrente alla S8
  operativa — file disgiunti, quinto interleave dichiarato)** — Su
  direttiva utente ("attacchiamolo"), primo bersaglio della lista di
  attaccabilità: G12 nella classe S1. Commit 9722b9a
  (docs/rde_nozzle_G12_S1.md + validation/g12_shock_linearization.py,
  PASS 9/9 con due rejector; log
  validation/PROGRESS_2026-07-16_rigore_G12.md, passi 1-9, gate PASS
  al passo 3). RISULTATO: il gap G12 (derivata di forma multi-D con
  urti) è RIDOTTO alla teoria 1-D verificata dentro la classe S1 via
  lettura x-come-tempo (Lemma G12-L1, autostruttura machine-verified
  EOS-general) + mattone-fronte (Lemma G12-L2: RH linearizzata non
  singolare strettamente dentro Lax, degenerazione ESATTAMENTE ai
  fronti caratteristici = legge di nucleo della Prop. A2); THEOREM
  G12-S1 (THEOREM*, residui R-G12.1..3 nominati; il limite di mesh
  del Lemma B ha ora il bersaglio continuo enunciato — circolarità
  rotta). M0 T7 G12 aggiornato (R4). CAMPAGNA ESTESA su direttiva
  utente (stesso log, passi 10-17; commit 6d10df7 + da4cc31):
  N6 ATTACCATO (docs/rde_nozzle_N6_swirl.md, carrier 16/16:
  THEOREM N6-1 struttura swirl — Mach lines meridiane invariate,
  nucleo con componente swirl nulla, G12-S1 si estende; THEOREM N6-2
  estensione VERBATIM di Rao al vortice libero — nuova classe
  positiva; THEOREM N6-3 negativo affilato — chiusura puntuale fallisce
  sse non-vortice-libero, livello di campo NECESSARIO; cinque-campi =
  SCHEMA nominato); UNICITÀ S1-U architettata (mattoni THEOREM, passi
  di funzione nominati); P4-PERIODICO enunciato con formula aggiunta
  J1 = -<psi_J, S_sweep U0> e ipotesi spettrale verificabile (D3 §3);
  T7-FS + P7-S1 (docs/rde_nozzle_T7_P7_functionspace.md, ancorati a
  (P)): derivazione sotto integrale di ciclo THEOREM* — (P)(ii) è
  condizione necessaria rigorosa; esistenza dell'argmax THEOREM* sui
  level set certificati — (P)(i) attaccato, frontiera di fallimento =
  bordo dei compatti. VERDETTO DI CAMPAGNA: nessuno SCHEMA portante
  resta tra la definizione di (P) e la sua soluzione certificata
  nella classe S1 senza urti; attraverso i fronti tutto eredita UN
  solo condizionale nominato (D2.5). Direttive permanenti registrate:
  scrittura pristine; dichiarazione di sufficienza simbolico-vs-
  funzione su ogni claim; àncora sempre (P).

- **S7 (2026-07-16, OPERATIVA: "Lemma B + OP-0-gamma + G5-2a";
  lanciata come S6-op, rinumerata alla riconciliazione)** — Gate
  pre-esecuzione PASS (log passo 3). T1 (9966552): Lemma B draft di
  record (§4 del paper: B0/B1/B2 THEOREM, fronte fitted esplicito con
  Lax/Majda == J_k non singolare, bypass Giles-Ulbrich per
  costruzione con clausola d'onestà, (**') pesata a quadratura fissa)
  + verifica DUAL-ROUTE di Prop. A2 in variabili conservative
  (p2_pA1_symbolic_adjoint.py, VERDICT PASS, 3 controlli negativi
  rigettati) — riposizionata dopo la riconciliazione: NON ri-reclama
  P-A1' (Prop. A3 della S6 rigore). T2 (1d762f8): purga gamma dal
  ceiling eseguibile — route primaria EOS-general via Cantera h(s,P),
  forme chiuse declassate a oracoli, cap sonico ri-verificato a
  gamma(T), delta di record -4.4..-7.9% (12 righe Pa finita, barre
  ~0.002%), test run_all (xi) 18/18 con rejector; R4 in M0 Prop. 7 +
  D3 §8. T3 (fb82846): spoglio digitale PMM 204/204 — G14 regge (zero
  hit aggiunto x contornatura in 34 anni); TOP FLAG Kraiko-Osipov
  34(6) 1970 dichiarato subito (wording G6 di P-1 contingente alla
  lettura full-text; contingenza D4 §3 armata, non attivata);
  SCOPERTA DI METODO: WebFetch fabbrica i contenuti delle pagine
  windows-1251 dell'archivio — sweep rifatto a HTML grezzo con
  verifica dei conteggi. DEVIAZIONI DICHIARATE: T4/T5 non eseguiti
  (→ NEXT 1-2); diagramma di fase su route reale rinviato (→ NEXT 3);
  QUARTA interleaving rilevata post-riconciliazione (63ba44c,
  addendum S6-rigore atterrato tra i commit T3 e T1; l'index git era
  CONDIVISO con la sessione rigore ancora attiva — chiusura eseguita
  con commit path-limitato dei soli file S7). Verdetti: gate PASS;
  pass simbolico PASS; ladder reale 18/18; sweep query-bounded
  completo.

- **S6 (2026-07-16, DEDICATA RIGORE: "P-A1/P-A2/P3 + corpus")** —
  Stessa conversazione di S5, su richiesta utente ("attaccalo in
  questa sessione"). Gate pre-esecuzione PASS (passo 4, con estensione
  NEXT dichiarata). Esecuzione T1→T2→T3→T4→T-LIT, log passi 1-19
  (validation/PROGRESS_2026-07-16_rigore_PA.md): T1 (5ec62ef) verifica
  macchina della derivazione classica + Prop. A2 + SCOPERTA (il
  conteggio di dimensioni del draft era lasco → raffinato, P-A1
  ristretto); T2 (36db818) P-A2 scaricato (lettura integrale Hoffman
  1967, mappa componenti, correzione simboli); T3 (b5590f0) P3
  THEOREM* in S1 senza urti; T4 (86e6d6d) P-A1' scaricato (Prop. A3,
  trasporto, PASS 19/19); T-LIT (0fdbe7d) studio corpus 5-agenti +
  sintesi b0bis (novelty PULITO, variable-inlet risolto, oracoli
  alla fonte, lead Rao 1958 IAF). Deviazioni dichiarate: nessuna di
  merito; un fix tecnico sympy dichiarato (derivata wrt espressione
  composta); domande utente in-sessione (rotazionale) risposte con
  nota di scope nel draft. Verdetti: Lemma A (i)-(iii) ora
  THEOREM/THEOREM* con rotte oneste; (iv) THEOREM*; residuo numerico
  unico P-A3/O3.2 (motore A1).

- **S5 (2026-07-16, "Fase 1: P-1 skeleton + P-2 Lemma A + G0 spike")** —
  Esecuzione T1→T2→T3 con gate di pre-esecuzione (PASS, passo 7) e log
  a ordine totale (validation/PROGRESS_2026-07-16_fase1_P1.md, passi
  1-21). T1/P-1 (6263c22): skeleton di record con mappa claim C1-C26
  (classe+falsificatore+carrier ciascuno), scope discipline §7
  semantics-first, grep di coerenza PASS. T2/P-2 (18c9d88): Lemma A
  §3 draft di record — lato classico DERIVATO in 8 passi dalla sola
  Lagrangiana (Eq. [11] come risultato, [12], [13], [14]==CSTR_PA/PB),
  tutte le righe confermate contro il corpus (zero discrepanze);
  Prop. A1 + dualità THEOREM; (i)-(iii) THEOREM* con O3.3 PENDING;
  (iv) SCHEMA con ancore verificate. T3/G0 (b07b47e): spike JAX PASS
  (implicit custom_vjp, 52/52 entrate entro tolleranza derivata,
  controllo negativo rigettato; jax 0.11.0 user-level, pin numpy
  intatto). DUE DIRETTIVE/DECISIONI UTENTE registrate: (1) generalità
  a GAMMA VARIABILE = accertamento permanente (audit di record: il
  sistema classico derivato è EOS-general; confini gamma=const
  nominati; memoria + regola (e) dello skeleton); (2) GENO RESTA IN
  FORTRAN se la pipeline intera resta funzionale (dual-code M0 VI.7;
  interop = criterio G0). Deviazioni dichiarate: concorrenza con S4
  sullo stesso tree (riconciliata, contenuti disgiunti, sessione
  rinumerata S4->S5); install JAX dichiarata (reversibile). Verdetti:
  gate pre-esecuzione PASS senza delta; Lemma A: nessuna discrepanza
  teoria/corpus; spike: VERDICT PASS.

- **S4 (2026-07-16, "G5 dispatch + venue P-2", concorrente a S5)** —
  Log proprio: validation/PROGRESS_2026-07-16_S4_G5venue.md (6 passi).
  f6a5112: pacchetto d'invio G5 pronto (email completa, destinatario
  web-verificato Boaga, Item 2a rescopato in-house); 5540fe2: venue
  P-2 DECISA su delega (AIAA J + arXiv a (G5 ∧ Lemma A pronta),
  fallback Aerospace con trigger, JOTA terziaria); cd903d1: chiusura.

- **S1 (2026-07-16)** — Formalizzazione + survey + audit completi:
  M0 (Teorema 0 catena della spinta; O1/O2; T0 rafforzato; N-SW;
  T3 tre lemmi; T4; G-B + globalità M1; T7/(**')), D1-D7, piano D6,
  6 filoni survey web-verificati + panel 16 agenti + corpus GENO;
  8 errori trovati-e-corretti (E1-E8); concordanze EAP e S-H con check
  quantitativo; probe γ (numeri stantii corretti); OP-0 bound ladder;
  protocollo di aderenza istituito (CLAUDE.md R1-R6 + questo file).
  Deviazioni dal piano: nessuna; T1/T3 della Sessione 2 anticipati.
  Verdetti: novità query-bounded confermata su tutti i filoni;
  residuo esterno = G5.
  CODA S1 (stessa conversazione, post-chiusura, interleaved con S2/S3):
  D2.6 Problema di record (P) — enunciato canonico (S*, δ) con
  contratto di globalità certificata e massimalità (f51db39; già
  consumato da S3 per il δ-certificato del diagramma); D7 §5 audit
  inverso de-biasing — pipeline ri-derivata dal problema nudo, bias
  residui B1 (schedule, gated G4) e B2 (esposizione) dichiarati
  (bc73b71); collocazione formale di φ come parametro esterno annidato
  del generatore (9341fdd); consolidamenti espositivi (aggiunto a
  quattro livelli; M0 confermato come documento paper-grade unico:
  teoria Parti I-IV, licenze Parte V, implementazione/testing
  Parte VI, mappa Parte VII). Sessione S1 DEFINITIVAMENTE CHIUSA.

- **S3 (2026-07-16, "Fase 1: OP-11-ε + P-2 + G5")** — Esecuzione
  T1→T2→T3 con log a ordine totale
  (validation/PROGRESS_2026-07-16_fase1_OP11.md, passi 1-16):
  T1/OP-11-ε (1438b1b): diagramma di fase 90 celle + vuoto, riuso
  ladder_row/check_chain con firma di degenerazione PR=1 asserita,
  test (x) 22 check + 8 rejector (controlli negativi T3/T4 espliciti),
  figura P-1, suite 11/11; SCOPERTE retro-propagate (R4, D3 §10quater
  + M0 Prop. 7 + D4): dominanza puntuale del plug con chiusura cappata
  (nessuna regione bell a livello ε) e attainment M1 ESTESO alle celle
  subcritiche via cap sonico (l'ipotesi supercritica è della sola
  chiusura naive, il cui artefatto a ε_max=1 inverte il ranking:
  test-rigettato); caratterizzata la regione tie (ε_max ≤ ε*(Pc_min):
  il plug non rilascia mai). T2/P-2 (05001a5): outline di record con
  Lemmi A/B classificati, falsificatori, piano O3, venue proposta.
  T3/G5 (e23bb08): testo commissioning biblioteca, solo testo.
  Deviazioni dichiarate: NESSUNA deviazione di merito; due errori
  d'ordine nel log di sessione (righe inserite fuori sequenza)
  corretti in-sessione prima dei commit. Verdetti: OP-11 a livello
  contorno resta CONGETTURA (duty split non esprimibile a livello ε).

- **S2 (2026-07-16, "Fase 0-chiusura + OP-0")** — Esecuzione T3→T1→T2
  con rendicontazione a ordine totale
  (validation/PROGRESS_2026-07-16_fase0_OP0.md, passi 1-18):
  T3/OP-0 bound ladder (1a4ff7b): catena bell ≤ int-max == ideal ≤ B_EK
  su 18/18 righe, dual-route, 7 controlli negativi, SCOPERTA del cap
  sonico su G-B retro-propagata a M0/D3 (R4); regimi 8 supercritiche
  (M1 gap-zero) / 4 subcritiche (naive VIOLATO) / 6 vuoto.
  T1/A0.3 gamma probe (f4cd429+9b2bcde+e77f63b): γ_s confermato,
  ε* −0.56% (−1.9% eliminato, origine = media non pesata −2.39%),
  penalità −0.00028% ≤ shift²; conferma eseguibile di γ_eff.
  T2/A0.1 (92cb8ea): correzioni inline nelle note storiche + gate grep
  PASS. Suite 9/9. Deviazioni dichiarate: T4/OP-11-ε opzionale NON
  eseguito (→ NEXT 1); lavoro in concorrenza con S1 sullo stesso tree,
  riconciliato senza conflitti.
