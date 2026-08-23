# LINEAGE_SWEEP_MATRIX — part 2 (slot L2, onda W-B.0 LINEAGE-SWEEP)

**NOTA DI DRIFT [C6-REPAIR 2026-08-23]**: le ancore "CHn:righe" di
questo file sono state stampate PRIMA della riscrittura dei CH1-CH10 da
parte dell'onda W-B.1 (mtime 08:33-08:44) e NON sono più affidabili
come numeri di riga (probe misurati: REFUTE_LINEAGE.md F-6). Il join
downstream usa LL-id e i § dei CH, MAI numeri di riga CH. Le ancore
non-CH (registry/findings/M0/LM/report/PDF) sono verificate sane da C6.
Legenda [C6]: "pC:" = `validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_pC_li_xu_2025.md`.

**Stadio di confronto**: prodotto cartesiano {15 componenti strutturali
del metodo (checkpoint C-1ter verbatim)} × {metà corpus 2, 41 id
esclusivi L2} — ricerca per ISOMORFISMO STRUTTURALE, mai tematica
(ordine utente C-1ter; finding di record
`docs/findings_registry.yaml:2541` [C6-REPAIR: era :2544] = la causa
radice che questa onda
ripara). Base di ogni cella: riga registry
(`docs/literature_registry.yaml`), CH1–CH8
(`validation/spres_raws_2026-08-22/reconstruction/`),
`docs/findings_registry.yaml`, ADVISORY_lit*/ASSESSMENT*; deep-check
PDF solo su celle candidate (dichiarato in cella). Nessun numero dei
paper entra in bande nostre (CT-6).

**Arco di consumo**: merge orchestratore (part1+part2) →
LINEAGE_LEDGER → §3-bis W-B.1 + storyboard; refuter C6 su celle vuote,
piene e lista componenti (incluse le flag GV-1 in coda).

**Legenda componenti**: (1) per-phase family; (2) averaged functional;
(3) averaged wall conditions; (4) weighted transversality; (5)
imposed-BC contract; (6) periodic data class; (7) quotient/wave-frame;
(8) mu measure; (9) decomposition identity; (10) per-phase marching;
(11) discrete adjoint; (12) certificates; (13) sector tournaments;
(14) truncation/p_b; (15) monitors.

**Convenzione cella**: "antenato/isomorfo? — come LORO la chiamano —
cosa manca vs noi". Cella assente dal blocco = **checked: none**
(elencata compatta). Tier evidenza: [IO] = letto su PDF in questa
finestra; [REP] = dal record (registry/CH/findings); [REP]-bounded =
paper non su disco, solo record.

---

## Blocchi per paper

### tesi_viviano_2023 [REP, READ-PARTIAL(triaged)]
- (3): antenato single-phase: psi (4.27-4.28) = FD Lambda-form =
  lineage GENO `boundaryfunction` ("boundary function"); manca OGNI
  famiglia/media — un solo stato steady (registry :476-482).
- (10): MoC GENO single-state (lineage doc); nessuna marcia per-fase.
- checked: none — (1),(2),(4)-(9),(11)-(15).

### thesis_valeriani_2019 [REP, READ-PARTIAL(triaged)]
- (3): Rao plug fuori perfect-gas con caveat onesto — consumo della
  soluzione classica single-state; nessuna condizione su famiglia
  (registry :484-490).
- (11): PSO/fminsearch = istanze DIRECT-method — controesempio, non
  antenato, dell'adjoint discreto.
- checked: none — (1),(2),(4)-(10),(12)-(15).

### kraiko_tillyaeva_2015 [REP; seed genealogia Kraiko school VERIFICATO]
- (3): problema conjugate/moltiplicatori COMPLETO per ugello Laval
  incl. parte subsonica; catena field→shape-gradient→ottimalità→Rao
  first integrals — per UN singolo stato; manca famiglia mediata
  (registry :498-505; CH5:277-281 near-miss A).
- (4): (2.10) coefficiente terminale rho·v²·tan(mu)≥0 ⇒ lunghezza
  SEMPRE attiva; restrizione unilaterale attiva ⇒ residuo
  SIGN-DEFINITE (A13) — transversality single-phase, MAI pesata su
  fasi (findings :1893).
- (11): lo chiamano "conjugate/adjoint problem" (terminologia INTERNA,
  near-miss A ADV-LX:10-17); adjoint mixed-type (Tricomi gen.) risolto
  numericamente; manca: forma ASO, adjoint DISCRETO/AD, optimizer
  (CH5:259-272 conceded chain (2.2)→(2.9)→(2.10)→(2.12)).
- (12): (2.9)=re-espressione del residuo Hoffman-E (A12); (2.5)-(2.6)
  = terza classe certificato F4b (A5); (2.11) = candidato oracolo
  adjoint closed-form [O6] (A3) — antenati di certificati, senza
  soglie derivate/rejector (findings :1849, :1893).
- checked: none — (1),(2),(5)-(10),(13),(14),(15).

### giles_pierce_2001 [REP]
- (11): adjoint quasi-1D ANALITICO in 4 regimi; continuità attraverso
  shock fittato + internal shock BC; singolarità log alla gola sonica
  — "analytic adjoint solutions"; è l'ORACOLO A1 [X-GP01] adottato
  (primo indipendente da GENO e da noi), non un antenato del nostro
  adjoint discreto (registry :507-514; findings :1481).
- (12): screen m−n sul conteggio BC (A11: m=4 axisym, m=5 con swirl)
  = precondizione, non 5° certificato (findings :1893); F11d gamba 1.
- checked: none — (1)-(10),(13)-(15).

### giles_pierce_2000 [REP]
- (2): obiettivo multipoint J=Σw_i·F[Σ;s_i] (Reuther via G-P 2000) =
  antenato discreto-ensemble del funzionale pesato — MA pesi/forma MAI
  stampati: J-somma è NOSTRA inferenza (R11, findings :2117).
- (11): equivalenza generica "adjoint = moltiplicatore del vincolo di
  flusso" p.397 — CONCEDED di record (CH5:267-272); tassonomia
  continuo/discreto = frame della scelta C56.
- (12): test di correttezza complex-step + transposition-identity =
  antenati dei nostri check row; senza soglie derivate (registry
  :516-523).
- checked: none — (1),(3)-(10),(13)-(15).

### kraiko_2001_plug [REP]
- (3): contouring ottimo del plug + Busemann condition + first
  integrals — single-state; manca famiglia/media (registry :525-532).
- (4): condizioni necessarie in forma di DISUGUAGLIANZA (F-6, lineage
  Shmyglevskii 1962) — transversality single-phase, non pesata.
- (12): slip line = elemento STRUTTURALE dell'ottimo classico (G-a):
  fissa l'acceptance test della classe certificato F4b
  linearly-degenerate (findings :2128) — il loro ottimo vive fuori dal
  nostro tier certificato.
- (14): plug+TN matching SENZA base; "thrust at start" — trattamento
  endpoint/base classico, nessuna chiusura p_b su medie.
- checked: none — (1),(2),(5)-(11),(13),(15).

### kraiko_2016_two_sided [REP]
- (3): CONTROESEMPIO interno alla scuola: ottimizzazione DIRETTA
  (RANS+GA+Bezier, "zero optimality equations"); la loro stessa
  tabella: l'ugello exact-theory batte tutti i GA (registry :534-541)
  — nessuna condizione di parete, su nulla.
- (11): direct search = alternativa non-adjoint censita; niente
  gradiente.
- (12): scan price-curve a 3 valori di beta (A24) = PRACTICE
  antenata del nostro "ogni punto col proprio Verdict" — senza barre
  derivate (findings :1948).
- checked: none — (1),(2),(4)-(10),(13),(14),(15).

### efremov_kraiko_2004_augmentor [REP; MANDATORY cite]
- (2): problema variazionale di spinta PERIOD-AVERAGED, Eq. (1.7)
  ∫₀¹…dt, Kraiko-signed [page-verified M0:2320-2326] — il
  falsificatore della frase "first averaged-thrust variational
  problem" (DEAD of record); manca: contorno di PARETE (aggira lo
  shared-wall, formulato come BOUND steady/ideal-limit) (CH1:351-355;
  CH5:213-216; findings :1429).
- (6): l'ottimo periodico risulta STAZIONARIO — il contatto classico
  più vicino con PB-2/T-T3-MAP; dato periodico endogeno al problema,
  non classe-dati imposta (registry :543-550).
- checked: none — (1),(3),(4),(5),(7)-(15).

### sun_2019 [REP]
- (3): "Rao ri-derivato a gamma(T)" è la LORO motivazione ed è FALSA
  (C14: nessuna Euler-Lagrange/lambda/angle condition mai scritta;
  exit criterion delegato per referenza) — occupa la mossa
  "construction with gamma(T)", non le condizioni (findings :1994).
- (9): Tab.3 decomposizione spinta (F_mom, F_p, −pa·Ae) = antenato
  pubblicato della split a[Σ]·Pc+b[Σ] (A14, findings :1904).
- (15): outer loop di freeze termodinamico Fig.1+Eq.(9) = candidato
  fixed-point (Sun NON lo itera mai); serve residual monitor+rejector
  nostro (A16, findings :1915).
- (10) [C6-FILL, dal campione celle-vuote del refuter]: la costruzione
  del contorno TOC E' una marcia MoC single-state a chiusura gamma(T)
  (registry :552-559 "Rao TOC construction") — stesso genere delle
  celle (10) di rao_1958/johnson_boney in part1; manca famiglia
  per-fase e le condizioni di ottimalita' (che Sun NON ri-deriva, C14
  findings :1994).
- checked: none — (1),(2),(4)-(8),(11)-(14) [C6-REPAIR: la (10) era
  none, riempita C6-FILL].

### hoffman_1987_ctp [REP]
- (12): Table 3 (24 area ratio, 4 output) = oracolo length-band
  [X-HOFF87]; tolleranza dal NOSTRO studio di convergenza (spacing MoC
  mai stampato) (A7, findings :1871).
- (14): la costruzione CTP (perfect → truncate a eps → compress
  lineare a L → tangency repair) = ANTENATO diretto del rung
  truncation; misura il premio Rao 0.04-0.34% Isp = scala esterna del
  surplus F7 (registry :561-568; A8 seed di ammissibilità).
- (15): detector di coalescenza characteristic-crossing p.151 =
  LOCALIZER (non margine C1; nonsmooth; costo una marcia in più) —
  antenato di monitor, da prezzare (A25, findings :1948).
- checked: none — (1)-(11),(13).

### fernandes_2023 [REP]
- (10): MoC usato come SIMULATORE dentro loop FFD+fmincon/NSGA-II —
  "the closest occupant of the niche we call empty" (claim 8); planar,
  gamma=1.4, NESSUNA condizione di ottimalità (registry :570-577).
- (11): gradiente via optimizer generico, niente adjoint; C17:
  obiettivo FLAT ⇒ argmax NON-IDENTIFIABILITY (Tab.1 vs Tab.2)
  — il rischio che i nostri certificati devono escludere (findings
  :1994).
- checked: none — (1)-(9),(12)-(15).

### rubino_2018 [REP]
- (2): obiettivi PERIOD-AVERAGED via harmonic balance — isomorfo del
  funzionale mediato; prova che il gap di macchina NON è tecnologico
  (claims 7/8); manca: riduzione per-phase, condizioni di parete
  Rao-type, contouring di ugello (turbomacchine RANS) (registry
  :579-586).
- (6): classe periodica trattata SPETTRALMENTE (HB) — ciclo endogeno
  al solve, non classe-dati imposta con monitor.
- (11): discrete adjoint DUALITY-PRESERVING per obiettivi mediati —
  "harmonic balance discrete adjoint"; il gemello di macchina più
  vicino alla nostra coppia (2)+(11).
- checked: none — (1),(3),(4),(5),(7)-(10),(12)-(15).

### zahr_persson_2016 [REP]
- (2): obiettivo time-averaged sotto vincolo di periodicità — famiglia
  endogenous-cycle nella tripla di non-contenimento claim 18 (registry
  :588-595).
- (6): "time-periodicity constraint" con esistenza+unicità via
  monodromia — periodicità IMPOSTA come vincolo di stato, non come
  classe-dati Gamma_d con monitor di flatness; fuori-pin route di
  record (CH1:230, :273).
- (11): adjoint FULLY DISCRETE = BVP lineare a due punti — isomorfo di
  macchina; manca MoC/per-fase e parete.
- (12): protocollo di verifica gradiente A15 (FD sul manifold,
  tolleranza interna DERIVATA eps_solve ≲ tau·delta, sweep tau ≥4
  decadi per-componente) = precedente esterno del nostro rejector O4
  (findings :1915).
- (15): certificato spettrale d'orbita (Floquet/monodromia) MODULO il
  gruppo di simmetria (A20) — moltiplicatore unitario strutturale per
  onda rotante autonoma; copia naive fallirebbe (findings :1926).
- checked: none — (1),(3),(4),(5),(7)-(10),(13),(14).

### schotthofer_2024 [REP]
- (2): windowing = regolarizzazione dell'obiettivo time-averaged —
  device ESTIMATOR-side (O5/VI.1), MAI dentro la definizione di J
  (C6 framing corretto, findings :1983).
- (8): il window è un PESO sul tempo — contrasto di record: la nostra
  mu è misura FISICA log-uniform (T-O2); ordine corretto da citare =
  Krakos et al. 2012, non Schotthofer (A9, findings :1882).
- (15): monitor M8 refuter-imposed sul verdetto H-DATA: audit
  window-convergence/source-trace per ogni famiglia estratta da
  simulazione (9% errore vettore, sign-flip da shift 29% di periodo)
  (findings :2427; A10 rejector shifted-horizon).
- checked: none — (1),(3)-(7),(9)-(14).

### janc_2025 [REP; threat vector nominato]
- (10): pattern static-shape padding + lax.scan a trip-count fisso
  (A21) = pratica di vettorizzazione della marcia; NON adottabile
  senza prova di ammortamento nostra (findings :1937).
- (11): solver reagente JAX DIFFERENZIABILE con demo adjoint su RDC =
  "the named 2026+ threat vector" — rende costruibile il falsificatore
  discreto del claim C (registry :606-613; ADV-LX:38-40); backsolve
  continuo NON soddisfa O3.1 → checkpointed discrete (A22).
- checked: none — (1)-(9),(12)-(15).

### liu_2022 (P-A) [REP]
- (2): membro "average-then-classical": media gli INPUT (rampa
  Angelino su time-averaged), mai il funzionale — 4 geometrie fisse,
  NO optimizer (C4 corretta: "only formal optimizer" slot VUOTO)
  (registry :615-622; findings :1972).
- (8): Eq. 14 ricostruzione stagnazione STATE-AVERAGED = terza
  convenzione di media NON dichiarata nella convention library
  (findings :2436).
- (9): Tab.6 decomposizione spinta = secondo antenato della split
  a[Σ]/b[Σ] (A14, findings :1904).
- (15): CONTRASTO: A-L6 = l'istanza più affilata di choking
  non-certificato (M_t=1.0 asserito ANCHE per il caso throatless) —
  nessun monitor; esattamente ciò che i nostri margini vietano
  (registry :622 nota G-13).
- checked: none — (1),(3)-(7),(10)-(14).

### ornano_2017 [REP]
- (2): shape optimization a TRE stadi con obiettivo TIME-AVERAGED
  (steady DoE → averaged URANS → reactive DDT) per PDC — optimizer
  presente, ma nessuna riduzione per-fase né condizioni; il delta 2%
  è dell'ordine della propria stopping tolerance (C16) (registry
  :624-631; findings :1994).
- (3): "proving the validity of Rao's method" = OVERCLAIM di record —
  accordo 5.689 vs 5.690 kN con tre qualifier; non è una condizione di
  parete mediata (findings :1994).
- checked: none — (1),(4)-(15).

### harroun_2020 [REP]
- (5): ascendenza imposed-detonation-BC del contratto Gamma_d nominata
  di record "Paxson & Harroun" (checkpoint C-1bis, findings :2544) —
  la linea harroun simula l'ugello con stato d'ingresso imposto dal
  ciclo; manca: contratto dati tipizzato + falsificatori.
- (14): base drag AMPLIFICATO dal ciclo oltre la stima
  constant-pressure — datum per la chiusura p_b (canale v); la figura
  "+1% flared" è second-hand (primaria = thesis 2019 WANTED) (registry
  :633-640).
- checked: none — (1)-(4),(6)-(13),(15).

### miki_2020 [REP]
- (5): BC d'ingresso unsteady CONGELATA e riusata su 6 geometrie
  disegnate a mano — "frozen unsteady inlet BC"; l'antenato operativo
  più diretto del contratto imposed-BC: "states our gap in its own
  words" (registry :642-650; A23 protocollo frozen-and-reused).
- (9): p.8 decomposizione spinta = terzo antenato della split A14
  (findings :1904).
- checked: none — (1)-(4),(6)-(8),(10)-(15).

### teasley_2023 [REP]
- (6): R20 — le osservazioni single-mode sono quasi tutte allo
  STARTUP: nessun dataset pubblicato certifica onda single-mode
  persistente in thermal-steady-state ⇒ il pin classe-dati resta
  MODEL HYPOTHESIS senza provenienza hardware (findings :2148;
  CH6:196).
- checked: none — (1)-(5),(7)-(15). [C19: geometria ugello NON
  ricostruibile dalla fonte — UNAVAILABILITY, findings :2005.]

### teasley_2025 [REP]
- (15): R25 — regime non-choked-feed (100-415 psid, no chug) senza
  margine di choking MISURATO all'interfaccia in alcuna fonte letta —
  datum negativo per il design dei monitor di margine (findings
  :2148).
- checked: none — (1)-(14). [Ugello = subcomponente di MANIFATTURA,
  4-scalar sweep: gap witness claims 8/7/5/6, registry :661-668.]

### li_xu_lv_lv_song_2023 (P-B) [REP]
- (2): Fig. 15 steady ~flat 0.965-0.971 vs transient con ottimo a 40%
  (+0.52%) e cliff a 80% (−5.78%) — flat-vs-peaked: la media GLOBALE
  non VEDE l'ottimo; marker cella (vi) (CH5:101-105).
- (3): UNICO del corpus C4 a usare il variazionale classico: superfici
  MAX-THRUST Rao/Vander-Veen applicate a UN singolo stato mediato
  GLOBALMENTE, vincoli di ristagno time-averaged "empirically
  recognized" (F-01) — l'istanza cruda più vicina; manca: famiglia
  per-fase, condizioni di ottimalità SULLA media (CH5:58-64, 439-456).
- (10): MoC assialsimmetrico (unit process Zucrow-Hoffman) su stato
  mediato — cugino crudo della marcia per-fase: una sola marcia, non
  una famiglia (registry :683-688).
- (14) [RIFORMULATA C6 da VERIFY_PB_corner_pb.md, source-verified]: DUE
  corner distinti (Fig. 13, p. 8): lip della SHROUD a p_inf AMBIENTE
  (Eq. 22); base dello SPIKE a p_b = "averaged base pressure" (Eq. 26)
  = media SPAZIALE sulla base (lessico plug troncato steady, MAI
  cycle-averaging), fonte dell'equazione e provenienza del VALORE non
  dichiarate; su chiusura Veen giudicata FAILED da WG10 — lezione
  Humphreys non consumata. La mediazione RDE entra SOLO nei vincoli di
  ristagno p0/T0 (cella (3)). [supersede la formulazione "corner a p_b
  MEDIATO"; forma di record = LL-20]
- checked: none — (1),(4)-(9),(11)-(13),(15).

### li_xu_lv_yu_zhou_2025 (P-C) [REP]
- (2): coppie transient vs steady-mediato: gap C_fx 0.2-1.5% ENTRAMBI
  i segni, flip a metà ranking, argmax stabile sulla famiglia discreta
  — marker (iv)/(vi); guardia best-of-sweep ≠ prova argmax
  (CH5:106-108, 327-342); conclusion (3): Veen "approximately
  applicable" sotto premessa kHz (pC:147-152).
- (8): compagno steady da media MASS-WEIGHTED — ulteriore convenzione
  di media non pinnata del campo (registry :690-695).
- checked: none — (1),(3)-(7),(9)-(15). [Nessun design nuovo: consuma
  il max-thrust di P-B, CH5:65-67.]

### jourdaine_2019 (P-D) [REP]
- (2): L'ORIGINE CITATA della premessa "average-then-classical-design"
  del corpus (C-1) — valutazione, mai formulazione mediata; si
  auto-giudica "the absolute values are completely different"
  (registry :697-702).
- (5): CONTRASTO CT-1: il lever più grande pubblicato (choked +4-7%
  Isp, +50/60% p statica camera) vive FUORI dalla classe
  fixed-interface — il prezzo del nostro contratto imposed-BC;
  decider CFD-1 (CH5:120-124, 406-409).
- checked: none — (1),(3),(4),(6)-(15).

### wanted_breitkopf_ulbrich [REP, READ-PARTIAL p.1]
- (11): dipendenza C1 posizione-shock/stato inter-shock via
  trasformazione front-fixing in reference space — TEMPLATE nominato
  (non consumato) per le duty di front-differentiability F2 (g2b;
  M-RED gamba (E) fitted-sheet sensitivity) (registry :754-761).
- checked: none — (1)-(10),(12)-(15).

### wanted_becker_rannacher_2001 [REP, READ-PARTIAL pp.3,40-41,46]
- (12): il metodo DWR — adjoint-weighted residual come stima d'errore
  SUL funzionale: la classe di estimatori stessa; canone C11 (barre su
  J = DWR target primario) (registry :862-868; CH4:143-155).
- checked: none — (1)-(11),(13)-(15).

### wanted_fidkowski_darmofal_2011 [REP, READ-PARTIAL pp.673-676]
- (12): review di riferimento del campo per output-based error
  estimation + mesh adaptation — canone C9/C11 della campagna
  estimator (registry :876-882).
- checked: none — (1)-(11),(13)-(15).

### wanted_hicken_zingg_2014 [REP, READ-PARTIAL pp.161-165,174]
- (11): Definition 1 dual consistency — l'ancoraggio pubblicato della
  scelta C56 (adjoint discreto AD nei tre ruoli) (CH4:160-165).
- (12): caveat p.164: consistenza PRIMALE non implica quella DUALE =
  la ragione pubblicata per cui F11d non si può condonare (CH4:161-163).
- checked: none — (1)-(10),(13)-(15).

### wanted_thakur_nadarajah_2024 (JCP 523, 2025) [REP, READ-PARTIAL]
- (10): implicit shock tracking goal-oriented full-space = steelman
  moderno dell'alternativa al fitted-front marching (C49 upgrade path
  con entry gate; axis-a modern-best) (registry :928-934; CH4:180-183).
- (11): adjoint-based goal-oriented — variante moderna del ruolo
  adjoint dentro il tracking, non antenata del nostro O3.1.
- checked: none — (1)-(9),(12)-(15).

### byrd_hribar_nocedal_1999 [REP, READ-PARTIAL]
- (11): parent algoritmico di scipy tr_interior_point (engine card
  C31): barrier update law + semantica dei moltiplicatori da
  verificare contro l'ALGORITMO pubblicato, non solo l'implementazione
  ([P-IPADJ] source companion; disciplina INFORMATION-ONLY fino a
  [P-IPADJ]) (registry :971-978; findings :1239).
- checked: none — (1)-(10),(12)-(15).

### nocedal_wright_2006_2ed [REP, READ-PARTIAL §8.1+App.A]
- (11): §6.2 SR1 = target citato per la curvatura quasi-Newton
  (engine); 15.3 variable elimination = via per multiplier provenance
  solver-trusted → repo-verified (findings :1371).
- (12): modello d'errore FD §8.1 (eq. 8.5-class) + float model App. A
  — le bande [P-HESSREJ]/[P-QNCARRY] DERIVATE dal modello, non
  asserite (R5) (registry :980-987).
- checked: none — (1)-(10),(13)-(15).

### giles_pierce_1997 [REP, READ-INTEGRAL 17/17 pp]
- (11): costruzione adjoint via funzione di Green; singolarità log
  gola sonica (§3.1.1) + continuità allo shock (§3.1.2); dicotomia
  region-of-influence/lateral-pressure-relief 2D (self-graded
  heuristic) — base del verdetto G-c leg-(ii) DISCHARGED-citable
  (registry :989-997).
- (12): R27 bridge + oracolo F11d leg-1 (trasferimento del rate
  near-sonic quasi-1D → axisym: decider nominato) (findings :2159).
- checked: none — (1)-(10),(13)-(15).

### venditti_darmofal_2000 [REP, READ-PARTIAL]
- (12): adjoint error estimation sul problema quasi-1D — l'algebra
  two-level della gamba (b) di C11 (registry :999-1005).
- checked: none — (1)-(11),(13)-(15).

### huang_zahr_2022 [REP, READ-PARTIAL]
- (10): HOIST (robust high-order implicit shock tracking) — il
  candidato upgrade NOMINATO del fitted-front marching C49, con entry
  gate su checklist pubblicate; mai antenato: posterità alternativa
  (registry :1007-1013; CH4:180-183).
- checked: none — (1)-(9),(11)-(15).

### huang_zahr_2023_companion [REP, READ-PARTIAL]
- (10): BC per shock PARAMETRIZZATI nel tracking implicito — input
  della ri-valutazione entry-gate W4 di C49 (registry :1015-1021).
- checked: none — (1)-(9),(11)-(15).

### masters_etal_2017 [REP, READ-PARTIAL]
- checked: none — TUTTE (1)-(15). NOTA GV-1 per refuter C6: il paper
  porta sul dof-budget della base di design (prior 20-25 dof, scope di
  trasferimento dichiarato, ledger C1 CH4:238-240) — la
  PARAMETRIZZAZIONE del design non è coperta dalle 15 componenti:
  candidata componente nuova (assorbimento C6).

### lauer_ansell_2025_pas [REP, READ-PARTIAL]
- checked: none — TUTTE (1)-(15). Stessa NOTA GV-1 di masters_etal_2017
  (layer moderno della census C1, registry :1031-1037).

### deuflhard_2011_csm35 [REP, READ-PARTIAL pp.51-53,96-98,130-131,147-148]
- (12): monitor Theta + terminazione (2.13)-(2.14), NLEQ-RES/NLEQ-ERR
  affine-invariant — la banda Tier-1 di record di C20: soglie di
  terminazione Newton DERIVATE da criterio pubblicato (registry
  :1039-1045).
- checked: none — (1)-(11),(13)-(15).

### yamamoto_1986_numermath48 [REP, READ-PARTIAL pp.91-92]
- (12): bound d'errore Newton-Kantorovich TWO-SIDED (Gragg-Tapia eq.
  7, Potra-Ptak, Miel) — strengthener Tier-2 r_K di C20; flag identità
  vol. 48/49 APERTA (registry :1047-1053).
- checked: none — (1)-(11),(13)-(15).

### vanaret_leyffer_2026_uno [REP, READ-PARTIAL; seed card C31 VERIFICATO]
- (11): Uno = solver unificato NLP — IL flip candidate nominato
  dell'engine A/B (arm-B preset spec, 10 input di spec per ordine
  utente; install = decisione O5-class, full text richiesto PRIMA)
  (registry :1055-1062; CH4:206-213). Cella → card C31 cluster
  F2-entry, come da seed.
- (12): l'A/B è pinnato a constraint-set identico con guardia
  IDENTICAL-CERTIFIED-OUTCOMES — il certificato che disciplina
  l'eventuale flip (CH4:208-210).
- checked: none — (1)-(10),(13)-(15).

### vanaret_montoison_2026_joss [REP, READ-PARTIAL pp.2-3]
- (11): identità software di Uno (JOSS companion, paper DISTINTO dal
  solver paper MPC) — alimenta la stessa card C31 (registry
  :1064-1070).
- checked: none — (1)-(10),(12)-(15).

---

## DUTY EXTRA — colonna FIEVISOHN (W-09), esito sweep disco

**ESITO SWEEP** (lezione litreview-protocol, eseguito PRIMA di ogni
claim): glob+grep `*[Ff]ievisohn*` su TUTTO il repo (0 PDF; 21 file
testo lo citano), su `literature/`, `literature_review/`, PARENT/ e
GENO non-elencato via find: **il paper W-09 (Fievisohn-Hoke-Schauer,
AIAA 2018-0881, "Quasi-2D simulations of nozzled RDEs with the method
of characteristics") NON è su disco su alcuna root** — procurement
RAISED resta valido. PERÒ lo sweep esteso del disco locale ha TROVATO
in `C:\Users\amont\Downloads\` due documenti Fievisohn primari, letti
mirati in questa finestra:
- `fievisohn-yu-2016-steady-state-analysis-...-method-of-characteristics.pdf`
  = Fievisohn & Yu, JPP 33(1):89-, 2017, DOI 10.2514/1.B36103 (pp.
  1-6 lette) — il METHOD paper della classe reduced-MoC;
- `Fievisohn_umd_0117E_17679.pdf` = Fievisohn, PhD dissertation, Univ.
  of Maryland 2016 (abstract + TOC letti) — contiene il modello
  completo (Ch. 4-7); **NESSUN capitolo ugello nel TOC**: l'estensione
  nozzled resta SOLO in AIAA 2018-0881.

Colonna quindi MISTA: celle [IO] dal method paper/dissertation on-disk,
cella (14) [REP]-bounded sul nozzled paper assente.

### FIEVISOHN (Yu 2017 JPP + PhD UMD 2016; W-09 stesso lineage) [IO salvo nota]
- (1) [IO]: la soluzione steady wave-frame è UNA soluzione globale del
  ciclo, usata per stime di performance ("ideal performance estimates
  one step up from a basic thermodynamic model... for large parametric
  studies", p.89) — cugino di VALUTAZIONE per-fase (linea Stechmann →
  Harroun → KP-EAP → Fievisohn → noi, seed CONFERMATO); NESSUNA
  famiglia di stati d'ugello indicizzata dalla fase, mai design.
- (5) [IO]: "mass flow injection boundary condition"/"inflow unit
  process" NUOVA per il MoC 2D (jump eqs sudden-expansion (12)-(14);
  segmentazione blocked/unchoked/choked lungo il fondo; dichiarata
  "similar to the boundary condition developed by Paxson and Wilson",
  p.93) — antenato della MECCANICA di BC imposta, feed-coupled al
  plenum: manca il contratto-dati Gamma_d tipizzato con falsificatori.
- (6) [IO]: la soluzione convergita È l'onda rotante single-mode
  steady ("ideal steady-state solution of an RDE in the wave-fixed
  reference frame", abstract p.89; §5.5 multi-wave nel PhD) — ciclo
  ENDOGENO ottenuto per iterazione a convergenza, non classe-dati
  IMPOSTA; nessun monitor di flatness.
- (7) [IO]: quotient/wave-frame ESPLICITO — lo chiamano "wave-fixed
  reference frame" (+ counterflow u_lab per chiudere lo steady-state
  requirement, p.94) — la stessa mossa del nostro quoziente; manca la
  formalizzazione a quoziente e ogni uso di design.
- (10) [IO]: rotational MoC shock-fitted con unit process
  Zucrow-Hoffman + mass-entropy modificato (Powers-O'Neill), slip-line
  unit process dedicato, 3 regioni marciate concorrentemente (§III,
  pp.92-94) — IL cugino pubblicato più vicino della nostra marcia
  fitted-front per-fase (elevated bearing, SYN:540-542); manca: marcia
  PER-FASE su famiglia, ottimalità, certificati.
- (14) [REP]-bounded: l'ugello compare SOLO in AIAA 2018-0881 (assente
  su disco): dal record, "MoC-native unsteady RDE+nozzle lineage,
  never extended to design" (ADV-LX:99-100; CH5:228-233) — nessun
  claim oltre questa riga.
- (15) [IO]: terminazione = "process is repeated until the solutions
  converge" (p.89) — iterazione a convergenza senza classe di monitor,
  soglie derivate o rejector.
- checked: none — (2),(3),(4),(8),(9),(11),(12),(13).

---

## CANDIDATE RIGHE LEDGER (antenato → cosa fa → cosa gli manca vs noi)

Verifiche/estensioni dei SEED (3):
- **S-1 Fievisohn (linea per-phase evaluation)** — VERIFICATO+ESTESO
  [IO]: wave-frame + rotational shock-fitted MoC + inflow BC = cugino
  più vicino di (7)+(10)+(5); mai design, mai famiglia per-fase;
  ugello solo nell'AIAA 2018-0881 assente. Ancora: JPP 33(1) pp.89-94
  (Downloads, letto), PhD UMD 2016 TOC; SYN:540-542; ADV-LX:99-100.
- **S-2 kraiko_tillyaeva_2015 (genealogia Kraiko school)** —
  VERIFICATO+ESTESO: non solo genealogia design: catena Route B→A
  interna (2.2)→(2.12) per (3)/(11) e certificati (2.9)/(2.10)/(2.5-6)
  per (12); manca famiglia mediata + adjoint discreto. Ancora:
  registry :498-505; findings :1849, :1893; CH5:259-281.
- **S-3 Uno (card C31/engine)** — VERIFICATO: celle (11)/(12)
  compilate per la card (flip candidate arm-B, guardia
  identical-certified-outcomes). Ancora: CH4:206-213; registry
  :1055-1070.

NUOVE (11):
1. **Efremov-Kraiko 2004 → (2)**: pone il variazionale di spinta
   PERIOD-AVERAGED (Eq. 1.7) — manca il contorno di parete (bound,
   aggira shared-wall). Ancora: M0:2320-2326; findings :1429.
2. **Rubino 2018 → (2)+(11)**: HB discrete adjoint duality-preserving
   per obiettivi period-averaged (macchina COMPLETA) — manca riduzione
   per-phase/MoC + condizioni di parete + contouring. Ancora: registry
   :579-586.
3. **Zahr-Persson 2016 → (6)+(11)+(12)+(15)**: fully-discrete adjoint
   sotto vincolo di periodicità + protocollo verifica gradiente A15 +
   certificato monodromia A20 — periodicità endogena, manca classe-dati
   imposta Gamma_d e la parete. Ancora: registry :588-595; findings
   :1915, :1926.
4. **Giles-Pierce 2000 (Reuther multipoint) → (2)/(8)**: J=Σw_i·F =
   antenato discreto-ensemble del funzionale pesato — pesi/forma MAI
   stampati (R11 = nostra inferenza). Ancora: findings :2117.
5. **Li-Xu 2023 (P-B) → (3)+(14)** [RIFORMULATA C6 da
   VERIFY_PB_corner_pb.md]: Rao/Vander-Veen max-thrust su stato steady
   da p0/T0 TIME-AVERAGED ("empirically recognized", p. 5); corner: lip
   shroud a p_inf ambiente (Eq. 22), base spike a p_b = "averaged base
   pressure" (Eq. 26, media SPAZIALE di base, fonte e provenienza del
   valore NON dichiarate) — l'istanza cruda più vicina; manca famiglia
   per-fase e ogni condizione SULLA media. Forma di record = LL-20.
   Ancora: VERIFY_PB_corner_pb.md; CH5 §P-B (numeri di riga CH
   soggetti a NOTA DI DRIFT).
6. **Sun 2019 / Liu 2022 / Miki 2020 → (9)**: decomposizione di spinta
   (F_mom, F_p, −pa·Ae) = antenato pubblicato della split
   a[Σ]·Pc+b[Σ] (A14) — mai identità dimostrata, mai per-fase.
   Ancora: findings :1904.
7. **Liu 2022 Eq.14 + P-C mass-weighted → (8)**: convenzioni di media
   NON dichiarate del campo (terza+quarta istanza) — la nostra mu è
   l'unica pinnata (T-O2). Ancora: findings :2436; registry :690-695.
8. **Hoffman 1987 → (14)+(12)**: costruzione CTP
   truncate-compress-tangency + Table 3 oracolo length-band [X-HOFF87]
   — misura il premio Rao (scala esterna F7); niente medie, tolleranze
   da derivare noi. Ancora: registry :561-568; findings :1871.
9. **Miki 2020 → (5)**: frozen unsteady inlet BC riusata su 6
   geometrie = antenato operativo del contratto imposed-BC — manca
   contratto tipizzato, falsificatori, famiglia per-fase. Ancora:
   registry :642-650; findings :1937 (A23).
10. **Kraiko 2001 (Shmyglevskii lineage) → (4)+(12)**: condizioni in
    forma di disuguaglianza + slip line strutturale dell'ottimo (G-a)
    → fissa l'acceptance test F4b linearly-degenerate — il loro ottimo
    è FUORI dal nostro tier certificato. Ancora: registry :525-532;
    findings :2128.
11. **Schotthofer 2024 → (8)/(15)**: windowing = estimator-side con
    monitor M8 refuter-imposed su famiglie simulation-sourced — MAI
    dentro J (mu fisica ≠ peso-finestra). Ancora: findings :1882,
    :1983, :2427.

FLAG GV-1 per refuter C6 (non righe ledger): Masters 2017 +
Lauer-Ansell 2025 portano su una componente NON coperta dalle 15
(parametrizzazione del design / dof-budget, ledger C1) — candidata
componente nuova dell'asse.
