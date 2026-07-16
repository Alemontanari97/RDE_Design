# PROGRESS — cycle-averaged variational nozzle program (living state)

> Single source of truth della progressione. Aggiornare a OGNI chiusura
> di sessione/fase (CLAUDE.md R3). La sessione successiva riparte da
> qui + memoria + M0, senza ricostruire nulla.

## ORA (2026-07-16, chiusura Sessione 1)

Branch `rde-nozzle-program`, HEAD = f4cd429. Stato per fase (piano D6):

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

## NEXT (passo atomico, Sessione 2)

1. [F1/T2] Grep di controllo bonifiche bibliografiche fuori dai banner
   (chiusura formale A0.1).
2. [F1/OP-11-ε] Diagramma di fase quasi-1D: griglia (vincolo) ×
   (spread di μ via PR), topologia vincente per cella dai closed form
   + bound ladder; figure per P-1.
3. [F1/P-2] Outline del lemma-ponte Rao=aggiunto (TIME-SENSITIVE:
   Lozano-Ponsin 2025 ha costruito la sponda 2-D).
4. [F0/G5] Commissionare il passaggio biblioteca Kraiko 1979 / PMM.

## BLOCCATO / GATE APERTI

- G5 (umano, biblioteca): blocca le SUBMISSION P-1/P-2/P-3, non il lavoro.
- G0 (stack JAX/Julia): decisione a Fase 2 (spike settimane 2-5 del
  90-day plan).
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
