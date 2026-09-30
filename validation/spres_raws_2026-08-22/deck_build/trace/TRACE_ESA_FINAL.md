# TRACE_ESA_FINAL — prova di tracciabilità del consumo reale (P1, 2026-08-25)

**Oggetto**: Desktop/Presentazione_ESA.pptx (35 slide = 22 main + divisore +
backup; salvata 2026-08-24; autore = utente; READ-ONLY; testo in
ESA_FINAL_TEXT.md).
**Natura della prova**: il deck finale è il PRIMO CONSUMO dell'atlas avvenuto
fuori dal controllo dell'orchestratore — ogni claim on-slide viene tracciato
alla sua catena (slide → spec/nota di sessione → CH-feed → M0/carrier) con
verdetto per riga. I mismatch sono i finding più informativi della sessione.
**Consumatori**: (1) L'UTENTE prima del talk (i finding TR-1..TR-4 sono
riparabili in 10 minuti sul suo file e le righe Q&A sono pre-cotte);
(2) findings registry (mint P4); (3) paper P-1 (le catene = scheletro
citazionale); (4) F2 (TR-5 = gap di scope dell'atlas).

## VERDETTI: legenda
ANCHORED = catena completa fino a carrier/classe · ANCHORED-W = ancorato in
forma indebolita (sempre lecito) · DERIVA = claim più forte o diverso
dall'ancora · NO-ANCHOR = nessuna catena nel record · FUORI-SCOPE = materia
che l'atlas non copre per costruzione.

## TABELLA DI TRACCIA (slide numerate n/22; solo righe content-bearing)

| Slide | Claim on-slide | Catena | Verdetto |
|---|---|---|---|
| 14 (B1) | stakes "+4–7% Isp (choked interface) · 58.1→71.5% of ideal (shroud)" | specs_a B1 → CH-feeds; 58.1→71.5 [REP] page-verified (findings_registry:2026; M0:1345,1350-53); refs [2][3] = LL-2/LL-3 | ANCHORED |
| 15 | "literature designs on its time-average" + caution degli autori dell'EAP | = nostra A6-v2 verbatim → CH1-feed-5 + CH5-feed-7 ([IO], M0:2526-2544) | ANCHORED |
| 16 | caption "Transient (left) vs REFERENCE STEADY state (right)" (P-C Fig.10) | F-ATLAS-1 (source-verified, caption verbatim pdf p.9) | ANCHORED — **il consumatore ha APPLICATO il catch F-ATLAS-1**: la caption onesta è entrata nel deck reale |
| 16 | "time-averaged plume DIFFERENT from the one obtained from steady-equivalent stagnation conditions" | la distinzione a tre campi (medio ≠ steady-companion): operatore residuo [T-DISC]/[T-RED] (canale medio 0 provato, covarianze+salti) + offset misurato ~2.8% (harvest A.3 [REP]) | ANCHORED (qualitativo; la taglia è il programma) |
| 17 | p₀ ~4:1, T₀ ~40%, M 0.85–1.33; sonic surface corrugata | KP18 Tab.1/Fig.6 → THROAT_HARVEST A.7 [FIG/REP] | ANCHORED |
| 17 | bande subsoniche/supersoniche coesistono "(depending on the FEED TOTAL PRESSURE)" | record: discriminante = CONFIGURAZIONE (contraction ratio) **E** punto di lavoro; "configuration-dependent, must be measured, not assumed" (harvest B(c) monitor (i): KP18 bassa contrazione sì-subsonico vs PM22 throatless no); nessuno sweep pubblicato in p0 (gap G6) | **DERIVA (TR-1)**: attribuzione ristretta alla sola pressione di alimentazione — variabile non provata come discriminante; riparo: "depending on geometry and operating point" |
| 18 | 4 rotte della letteratura + "no published work formulates the optimum problem on the real RDE exhaust" (in a systematic literature review) | C3/C3-bis census (query-bounded ✓ on-slide) | ANCHORED (forma query-bounded corretta) |
| 19 | fork substitute-vs-periodic + teorema del muro ("No single phase satisfies its own wall condition — the weighted mean does") | C7-bis → CH2-feed-1 THEOREM* [T-T7FS] | ANCHORED |
| 19 | "conditions never written before" (senza bound on-slide) | guard 9: claim di novità SEMPRE query-bounded | **DERIVA-LIEVE (TR-2a)**: manca "to our literature search" on-slide; se è nelle note del relatore, il rischio è solo Q&A — riparo: 5 parole |
| 20 | "in the declared class the flow is steady in the wave frame" | C8 → quoziente, gamba THEOREM [T-T0P-E] + classe dati pin | ANCHORED |
| 20 | "The global time average mixes the phases **in an exact way**" | record: il quoziente per-fase è ESATTO; la media globale MESCOLA le fasi (riduzione più cruda) — "exact" appartiene al quoziente, non al mescolamento | **DERIVA-WORDING (TR-3)**: la frase può leggersi invertita (media globale = esatta); riparo: "mixes the phases — the cruder reduction" o "in a way we characterize exactly" se questo si intendeva |
| 20 | "Approximation (TO BE MEASURED): each phase axially expanded by a generalized 2D steady MoC" | O(St) dichiarata (CH1-feed-2) + canali residui misurabili [T-RED] + march per fase di record | ANCHORED — forma onesta ESEMPLARE (l'approssimazione dichiarata con il suo falsificatore) |
| 21 | Stechmann = Q1D per fase su famiglie fisse; Harroun = 2D axi a pressure-ratio di ciclo, solo evaluation; "this project: variational optimum on the family — never posed before" | C7-bis-pre → LL-2/LL-3 (ancestors di record); novità = D-06 locked | ANCHORED, ma **TR-2b**: "never posed before" di nuovo senza bound on-slide (stesso riparo di TR-2a) |
| 22 | "J, the cycle-averaged thrust of the **optimal** wall" | record: J = spinta ciclo-mediata della parete CONDIVISA (shared wall — una parete per tutte le fasi); "optimal wall" anticipa l'esito | **DERIVA-MINOR (TR-4)**: shorthand comunicativo; riparo: "shared wall" (come in backup s25 nostro) — nota: il backup s25 usa a sua volta "optimal wall" (stessa riga) |
| 22 | adjoint = 1 forward + 1 backward → dJ/d(shape) esatto, TR-Newton in secondi | C13/C-ADJ → T-LEMB THEOREM + X-TOCV carrier + C31 ledger | ANCHORED |
| 23 | "First per-phase variational design method" / "First hierarchical assessment of the error…" | D-06 locked (query-bounded richiesto) + programma gap/budget | ANCHORED-W nel contenuto; **TR-2c** sulla forma (bound assente on-slide, due "first") |
| 23 | head-to-head "either result could be of foremost importance" | CH6-feed-4 (both-informative, kill-or-validate) | ANCHORED — la forma both-outcomes è quella giusta |
| 23 | estensioni: altri funzionali (heat flux, pressure gain), confronto con espansioni deflagrative canoniche, 3D topologie | outlook di programma; PG-funzionale adiacente a EAP/PG di record; nessuna contraddizione col record | ANCHORED-W (classe outlook, nessun claim di risultato) |
| 25-26 (backup) | adjoint explainer + Rao benchmark ~2·10⁻³ + velocità 15–20 s / 10–14 min | nostri C-ADJ/C13-val v2 verbatim → [X-TOCV] S18 + M-CHAIN S25 (MET formali) | ANCHORED |
| 5 | JAXA 2021 primo in orbita; Warsaw 2021 primo volo liquido; NASA RDRE 251 s 2023; Venus 2025; Astrobotic 300 s 2026; DARPA/GE/91 M$ | NESSUNA catena: il registro lit/atlas copre il corpus tecnico, non la cronaca voli/mercato | **FUORI-SCOPE (TR-5)**: il consumatore ha dovuto auto-procurarsi l'intera slide di contesto; i numeri NON sono verificabili dal record — gap di copertura dell'atlas (candidato cluster WANTED "flight demos & programmes"), e rischio-verifica in Q&A a carico dell'utente |

## SINTESI DELLA PROVA
1. **La prova di consumo REGGE**: 17/20 righe ANCHORED o ANCHORED-W; le
   catene arrivano a carrier con classe; l'architettura a 9 slide, sei
   titoli, la lingua "literature", il frame per-fase e PERFINO il catch
   F-ATLAS-1 e la distinzione a tre campi (risposta data in-sessione)
   sono stati consumati dal deck reale. L'atlas ha funzionato da sorgente.
2. **Cinque finding** (mint P4): TR-1 (attribuzione feed-pressure non
   provata), TR-2a/b/c (novità senza query-bound on-slide ×3 — rischio
   Q&A, riparo a 5 parole), TR-3 (wording "exact" sul mescolamento — può
   leggersi invertito), TR-4 (optimal vs shared wall, minore), TR-5 (gap
   di scope: nessun capitolo flight-demos/programmi nell'atlas).
3. **Per l'utente PRIMA del talk** (riparabili sul suo file in minuti):
   TR-1 e TR-3 sono i due che un panelist tecnico può contestare; TR-2
   si ripara aggiungendo "to our literature search" alle tre righe; TR-5
   richiede solo di avere le fonti-notizia pronte in Q&A.
