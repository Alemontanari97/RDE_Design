# HISTORIAN_INV_b — inventario storico slot B8b (onda W-B.2, 2026-08-23)

- **Stadio di confronto**: sezioni §6 STORIA scritte da questo slot in
  CH5/CH6/CH8/CH9/CH10, contro HISTORIAN_INDEX.md + aperture mirate
  (chapters, phaseB/phaseD/hypaudit, git log, registri) — nessuna ancora
  coniata fuori dal materiale letto in finestra.
- **Arco di consumo**: C5 (retro-audit: join su DATA+PROCESSO+VERDETTO
  per battuta) + orchestratore W-B.2.

## 1. Inventario per capitolo — argomenti e split rami (a)/(b)/(c)

| CH | argomenti | (a) | (b) | (c) | misti | note |
|---|---|---|---|---|---|---|
| CH5 | 6 | 0 | 1 (6.6 L11-stance) | 4 (6.1, 6.2, 6.3, 6.5) | 1 (6.4 = eventi-correzione, non classificabile a/b/c: battute = eventi datati) | doppia prova sempre presente (litreview contraddittorio + REFUTE_CH5; VERIFY_PB 2026-08-23 come evento di QUESTA sessione) |
| CH6 | 5 | 0 | 1 (6-bis.2 N-Q, stance C-3/C-3bis/C-3ter) | 4 (6-bis.1, 6-bis.3, 6-bis.4, 6-bis.5) | 0 | N-Q scritto come verità storica delle 3 correzioni utente 2026-08-23; header "6-bis" perché §6 del capitolo = legenda W2-R10 (posizione template rispettata) |
| CH8 | 6 | 1 (6.4 dicotomia T3/T4 riderivata cieca, phaseB §3 item 5 :339-344) | 3 (6.1, 6.3, 6.5) | 1 (6.6 H20/C61, assenza search-proven) | 1 (6.2: (a) gamba esistenza Chenais + (c) gamba finitezza, census-lemma DOVUTA) | mix (a)/(b) come da nota di brief |
| CH9 | 5 | 1 (6.1 architettura certificato-first, phaseB :330-335/:347-350) | 0 | 4 (6.2, 6.3, 6.4, 6.5) | 0 | ramo (c) quasi ovunque come atteso; doppia prova = dual-seed + dual-code GENO + refuter S-CERT, ancore PROGRESS_2026-08-13_Scert / registri, mai memoria |
| CH10 | 5 | 2 (6.1 contract blind 9-elementi; 6.2 L4⇒R1 con cap r2 NOT-DRY dichiarato) | 1 (6.5 ledger, stance fitted-front 4/4) | 2 (6.3 G6 mai esercitato; 6.4 U3' premise-open) | 0 | doppia prova = hypaudit confront_contract + VERDICT_contract_and_L4R1, come da brief |

Totale argomenti: 27. Split complessivo: (a) 4 · (b) 6 · (c) 15 · misti 2.

## 2. FINDING ("doppia prova: ASSENTE")

**Zero.** Ogni ramo (c) porta una doppia prova alternativa ancorata
(litreview contraddittorio, threat ledger, hypaudit, dual-seed su 3
finestre, harvest search-proven, fork-141). Nessuna riga ha richiesto la
dichiarazione FINDING. Due datazioni sono dichiarate by-inclusion /
limite-di-join anziché a data propria (CH8 6.1-6.2 problem book senza
data; CH6 6-bis.5 riga findings:2148 senza data per-riga esibita) —
dichiarate NEL testo, non nascoste; non sono ancore fabbricate.

## 3. FUORI-PERIMETRO (file/sezioni non miei, per l'orchestratore)

1. **CH9 preambolo riga 13**: dice ancora "§6 STORIA = writer W-B.2 (qui
   solo placeholder)" — ora STALE (la sezione è scritta). Il preambolo è
   fuori dal mio perimetro di edit (regola "NON toccare nessun'altra
   sezione"); fix di una riga per l'owner B1/orchestratore.
2. **CH10 preambolo riga 12**: idem — "§6 STORIA = placeholder di round
   per W-B.2" ora stale; owner del preambolo.
3. **CH9 modificato concorrentemente su disco** durante questo round
   (correzioni anchor C1/REFUTE_CH9, es. F-10 alle righe §2): nessun
   conflitto con la mia §6; segnalato per consapevolezza di merge.
4. **HISTORIAN_INDEX.md Sezione 3**: il commit della pipeline map è
   `da91aa4`; in una mia prima stesura CH6 l'avevo trascritto male e
   l'ho corretto in-window contro `git log` (SR-12). L'indice è
   corretto; nessuna azione dovuta.

## 4. Ritorno sintetico (per il protocollo d'onda)

- CH5: 6 argomenti (0a/1b/4c/1 misto), 0 FINDING.
- CH6: 5 argomenti (0a/1b/4c), 0 FINDING.
- CH8: 6 argomenti (1a/3b/1c/1 misto a+c), 0 FINDING.
- CH9: 5 argomenti (1a/0b/4c), 0 FINDING.
- CH10: 5 argomenti (2a/1b/2c), 0 FINDING.
- Scrittura incrementale rispettata: 5 edit, uno per capitolo, più il
  fix-ancora CH6.
