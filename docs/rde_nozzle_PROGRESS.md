# PROGRESS — cycle-averaged variational nozzle program (living state)

> Single source of truth della progressione. Aggiornare a OGNI chiusura
> di sessione/fase (CLAUDE.md R3). PROTOCOLLO DI APERTURA (dalla S10,
> ordine S9): memoria di progetto + L0 (SCAFFOLD §1: obiettivo e
> regole) + docs/claims_registry.yaml (l'INDICE della teoria, lintato
> dal gruppo (xv)) + D6 (stati/gate) + questo file. M0 resta il master
> del proof layer, letto per profondità, non per ricostruire lo stato.

## ORA (2026-07-21, chiusura Sessione 11 — "FASE 2/A1 BRICK 1: la
## machinery di generazione profili ESISTE ed è certificata + P-1 body
## text COMPLETO"; sessione UNICA, check pre-commit puliti)

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

## NEXT (Sessione 12)

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
