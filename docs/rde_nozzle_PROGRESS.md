# PROGRESS — cycle-averaged variational nozzle program (living state)

> Single source of truth della progressione. Aggiornare a OGNI chiusura
> di sessione/fase (CLAUDE.md R3). La sessione successiva riparte da
> qui + memoria + M0, senza ricostruire nulla.

## ORA (2026-07-16, chiusura Sessione 3 — "Fase 1: OP-11-eps + P-2 + G5")

Branch `rde-nozzle-program`, HEAD = e23bb08 (T1 = 1438b1b, T2 = 05001a5,
T3 = e23bb08). Stato per fase (piano D6):

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

## NEXT (passo atomico, Sessione 4)

1. [F1/P-1] Skeleton della stesura P-1 (venue JPP): la teoria è pronta
   (M0 Parti I-III + i due ponti EAP/S-H + numeri OP-0 + figura e
   teoremi OP-11-ε di questa sessione); partire dallo scheletro
   sezione-per-sezione con la mappa claim→(classe, falsificatore,
   carrier eseguibile).
2. [F1/P-2] Stesura Lemma A §3 (identificazione termine-a-termine,
   equation-numbered vs corpus b0) sull'outline 05001a5.
3. [F2-prep/G0] Spike JAX: UN unit process MOC (interior + inverse
   wall) con custom_vjp + regola implicita; gradiente vs differenze
   centrali e vs GENO su un caso TOC (90-day plan item 2).
[FATTO in S3: ex-NEXT-1 OP-11-ε → 1438b1b; ex-NEXT-2 outline P-2 →
05001a5; ex-NEXT-3 testo commissioning G5 → e23bb08.]

## BLOCCATO / GATE APERTI

- G5 (umano, biblioteca): blocca le SUBMISSION P-1/P-2/P-3, non il
  lavoro. TESTO DI COMMISSIONING PRONTO
  (validation/G5_kraiko_pmm_commission.md): invio e destinatario in
  mano all'utente.
- Venue P-2: proposta nell'outline (AIAA J / Aerospace / JOTA) —
  decisione utente.
- ADR panel 2026-07-16 (validation/ADR_panel_2026-07-16.md, NON
  committato): IN ATTESA DI RATIFICA UTENTE — nessuna implementazione
  avviata, per disciplina.
- G0 (stack JAX/Julia): decisione a Fase 2 (lo spike NEXT-3 la
  istruisce).
- RaoPlug S1/S2 (GENO): prerequisito di OP-2/PB-2, non ancora attaccato.

## LOG SESSIONI

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
