# PROGRESS — cycle-averaged variational nozzle program (living state)

> Single source of truth della progressione. Aggiornare a OGNI chiusura
> di sessione/fase (CLAUDE.md R3). La sessione successiva riparte da
> qui + memoria + M0, senza ricostruire nulla.

## ORA (2026-07-16, chiusura Sessione 2 — "Fase 0-chiusura + OP-0")

Branch `rde-nozzle-program`, HEAD = 92cb8ea. Stato per fase (piano D6):

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

## NEXT (passo atomico, Sessione 3)

1. [F1/OP-11-ε] Diagramma di fase quasi-1D (era il T4 opzionale della
   Sessione 2, DECLINATO deliberatamente per disciplina di chiusura):
   griglia (ε_max o L) × (spread di μ via PR), topologia vincente per
   cella dai closed form + bound ladder di src/thrust/bounds.py
   (riusare ladder_row/check_chain; attenzione al regime subcritico:
   usare il ceiling CAPPATO, mai il naive); figure per P-1.
2. [F1/P-2] Outline del lemma-ponte Rao=aggiunto (TIME-SENSITIVE:
   Lozano-Ponsin 2025 ha costruito la sponda 2-D).
3. [F0/G5] Commissionare il passaggio biblioteca Kraiko 1979 / PMM.
[FATTO in S2: ex-NEXT-1 grep di controllo A0.1 → gate PASS, 92cb8ea.]

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
