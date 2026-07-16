# PROGRESS — cycle-averaged variational nozzle program (living state)

> Single source of truth della progressione. Aggiornare a OGNI chiusura
> di sessione/fase (CLAUDE.md R3). La sessione successiva riparte da
> qui + memoria + M0, senza ricostruire nulla.

## ORA (2026-07-16, chiusura Sessione 7 — OPERATIVA: "Lemma B +
## OP-0-gamma + G5-2a"; CONCORRENTE con la S6 rigore, riconciliata)

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

## NEXT (passo atomico, Sessione 8)

1. [F1/P-1] Prima stesura testuale delle sezioni §2 (Theorem 0 + O1/O2)
   e §4 (dicotomia) dello skeleton 6263c22, con la regola
   d'accettazione (a)-(e) applicata sezione per sezione (T4 di S7,
   non eseguito — dichiarato).
2. [F2-prep/G0] Estensione dello spike: variante assialsimmetrica
   (termine sorgente) + shock point (regola implicita su RH; scarica
   P-B1/O3.1 al mattone shock), e primo confronto cross-code col caso
   TOC GENO (criterio interop G0; GENO resta Fortran, decisione S5).
3. [F1/OP-0-gamma, coda] Diagramma di fase OP-11-eps sulla route
   REALE (il condizionale "se regge" di S7: la ladder regge, il
   diagramma è rinviato) + route a espansione di EQUILIBRIO come
   bracket superiore del rung frozen (M0 Prop. 7, residuo dichiarato).
4. [F1/P-2, rifiniture] Footnote "adjoint constraints" (94-3264,
   trappola lessicale — NEXT-0 della S6 rigore, non ancora inserito
   nei draft); integrare nel §4 il riferimento a Prop. A2/A3 di
   record; consolidare i due script P-A (pa1_symbolic_lemmaA.py +
   p2_pA1_symbolic_adjoint.py) in un runner unico o gruppo test.
5. [LEADS, query-bounded, ereditati dalla S6 rigore] Rao 1958 IAF
   Amsterdam (precedente var-gamma, HIGH); van Meerbeeck EUCASS 2013
   (LOW, parametrico).
[FATTO in S7 (operativa): ex-NEXT-1 spoglio PMM → fb82846 (G14 regge;
top flag Kraiko-Osipov 1970 → Item 2b); ex-NEXT-2 Lemma B →
docs/rde_nozzle_P2_lemmaB.md + verifica dual-route Prop. A2 → 9966552
(lo scarico P-A1/P-A1' era già della S6 rigore, Prop. A3);
ex-NEXT-5 purga gamma (livello ladder) → 1d762f8. FATTO in S3-S6:
vedi voci precedenti.]

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
- G0 (stack JAX/Julia): decisione a Fase 2 — lo spike S5 (b07b47e) è
  PASS su JAX 0.11.0 CPU (implicit-vjp, tolleranze derivate, rejector);
  criterio aggiunto (decisione utente S5): interop con GENO-Fortran
  (pipeline intera funzionante, O3.4 cross-code) — il punto NEXT 4 lo
  esercita prima della decisione formale.
- RaoPlug S1/S2 (GENO): prerequisito di OP-2/PB-2, non ancora attaccato.

## LOG SESSIONI

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
  rotta). M0 T7 G12 aggiornato (R4). Prossimi attacchi del filone
  rigore (ordine valutato): N6 (nucleo 3-D + cinque campi swirl),
  unicità S1-interna, P4 periodico liscio.

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
