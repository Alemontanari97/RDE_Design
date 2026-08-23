# HISTORIAN_INV_b — inventario storico slot B8b (onda W-B.2, 2026-08-23;
# aggiornato al round di riparazione REFUTE_STORIE, stessa data)

- **Stadio di confronto**: sezioni §6 STORIA scritte da questo slot in
  CH5/CH6/CH8/CH9/CH10, contro HISTORIAN_INDEX.md + aperture mirate
  (chapters, phaseB/phaseD/hypaudit, git log, registri) — nessuna ancora
  coniata fuori dal materiale letto in finestra; verdetti REFUTE_STORIE
  applicati (v. §5).
- **Arco di consumo**: C5 (retro-audit: join su DATA+PROCESSO+VERDETTO
  per battuta) + orchestratore W-B.2.

## 1. Inventario per capitolo — argomenti e split rami (a)/(b)/(c)
## (post-riparazione)

| CH | argomenti | (a) | (b) | (c) | misti/eventi | note |
|---|---|---|---|---|---|---|
| CH5 | 6 | 0 | 0 | 5 (6.1, 6.2, 6.3, 6.5, 6.6 [fix ST-C5-10]) | 1 (6.4 = eventi-correzione datati) | doppia prova sempre presente (litreview contraddittorio + REFUTE_CH5; VERIFY_PB 2026-08-23 come evento di QUESTA sessione) |
| CH6 | 5 | 0 | 0 | 4 (6-bis.1, 6-bis.3, 6-bis.4, 6-bis.5) | 1 (6-bis.2 = eventi-correzione C-3/C-3bis/C-3ter, forma CH5 6.4 [fix ST-C5-12]) | finder E-K 2004 ri-ancorato a litreview_confrontation:107 [fix ST-C5-11]; header "6-bis" perché §6 del capitolo = legenda W2-R10 |
| CH8 | 6 | 1 (6.4 dicotomia T3/T4 riderivata cieca, phaseB §3 item 5 :339-344) | 2 (6.1 errata-di-fork vera; 6.5 verdetti per-riga phaseB §1 :22/:66/:159) | 2 (6.3 pin utente [fix ST-C5-16]; 6.6 assenza search-proven) | 1 (6.2: (a) esistenza-Chenais + (c) finitezza, census-lemma DOVUTA) | date note M0 corrette [fix ST-C5-17]; doppia ancora fork b0a4c15+a85e355 [fix ST-C5-18] |
| CH9 | 5 | 1 (6.1 architettura certificato-first, phaseB :330-335/:347-350) | 0 | 4 (6.2, 6.3, 6.4, 6.5) | 0 | ancora Scert:184 aggiunta alla clausola auto-assoluzione [fix ST-C5-19]; verdetto refuter: REGGE, 0 BREAK/0 REPAIR |
| CH10 | 5 | 3 (6.1 contract blind; 6.2 L4⇒R1 cap r2 NOT-DRY dichiarato; 6.5 scoped-architettura [fix ST-C5-23]) | 0 | 2 (6.3 G6 mai esercitato; 6.4 U3' premise-open) | 0 | fix NOTE ST-C5-20/21/22/24 applicati + 2 residui B2 (⇔→due direzioni a gradi; C-SBVF→C-MAJDA) |

Totale argomenti: 27. Split complessivo post-riparazione:
(a) 5 · (b) 2 · (c) 17 · misti/eventi 3.

## 2. FINDING ("doppia prova: ASSENTE")

**Zero** (invariato). Ogni ramo (c) porta una doppia prova alternativa
ancorata. Due datazioni restano dichiarate by-inclusion / limite-di-join
NEL testo (CH8 6.1-6.2 problem book senza data propria; CH6 6-bis.5
findings:2148 senza data per-riga) — il refuter le ha contate come
limiti dichiarati, non violazioni.

## 3. FUORI-PERIMETRO (file/sezioni non miei, per l'orchestratore)

1. **CH9 preambolo riga 13**: "§6 STORIA = writer W-B.2 (qui solo
   placeholder)" ora STALE — fix one-line per l'owner del preambolo.
2. **CH10 preambolo riga 12**: idem ("placeholder di round per W-B.2").
3. **CH9 modificato concorrentemente** durante il round di scrittura
   (correzioni anchor C1/REFUTE_CH9): nessun conflitto con la mia §6.
4. **HISTORIAN_INDEX.md Sezione 3**: commit pipeline map = `da91aa4`;
   trascrizione errata mia in CH6 corretta in-window contro `git log`
   (SR-12). L'indice è corretto; nessuna azione dovuta.

## 4. Ritorno sintetico (per il protocollo d'onda, post-riparazione)

- CH5: 6 argomenti (0a/0b/5c/1 eventi), 0 FINDING.
- CH6: 5 argomenti (0a/0b/4c/1 eventi), 0 FINDING.
- CH8: 6 argomenti (1a/2b/2c/1 misto), 0 FINDING.
- CH9: 5 argomenti (1a/0b/4c), 0 FINDING.
- CH10: 5 argomenti (3a/0b/2c), 0 FINDING.
- Scrittura incrementale rispettata: 5 edit di stesura + round di
  riparazione (fix marcati in-place).

## 5. Round di riparazione REFUTE_STORIE (2026-08-23) — fix applicati

| Fix | CH | Natura |
|---|---|---|
| ST-C5-10 | CH5 6.6 b2 | (b)→(c) con doppia prova L12+CT-2+REFUTE_CH5 |
| ST-C5-11 | CH6 6-bis.3 b2 | finder E-K 2004 → litreview_confrontation:107 (+:277/:285); ruolo sweep corretto |
| ST-C5-12 | CH6 6-bis.2 b2 | (b)→eventi-correzione (forma CH5 6.4); "stance" generiche ripulite |
| ST-C5-16 | CH8 6.3 b2 | (b)→(c) pin-utente (forma CH1 T-1) con doppia prova :371-377 + state-pointer |
| ST-C5-17 | CH8 6.3 b2 | data nota M0:306-312 = 2026-08-06 (la :313-320 porta 2026-08-05) |
| ST-C5-18 | CH8 6.6 b1 | doppia ancora b0a4c15 (90/50/1/0) + a85e355 (2 genuine gaps) |
| ST-C5-19 | CH9 6.4 b2 | ancora Scert:184 sulla clausola auto-assoluzione |
| ST-C5-20 | CH10 6.3 b2 | quote esatta hypaudit + ancora :459 |
| ST-C5-21 | CH10 6.3 b3 | ancora off-manifold → D6:1150-1152 |
| ST-C5-22 | CH10 6.2 b2 | conteggio ri-misurato in finestra: 2105 righe (wc -l 2026-08-23) |
| ST-C5-23 | CH10 6.5 b2 | (b)→(a) scoped-architettura (phaseB §3 item 3), scope dichiarato |
| ST-C5-24 | CH10 6.1 b2 | "workflow 10/10" ri-ancorato al commit 5221529 (verbatim nel messaggio) |
| B2-res1 | CH10 6.1 b3 | "⇔" → due direzioni a gradi dichiarati (decoupling ⇒ choking pieno; inversa solo a livello medio via [T-NSW] su L4) |
| B2-res2 | CH10 6.5 b1 | C-SBVF (inesistente nei registri) → C-MAJDA |
