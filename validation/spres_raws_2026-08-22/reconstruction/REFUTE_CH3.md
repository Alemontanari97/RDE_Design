# REFUTE_CH3 — Verifica avversariale di CH3_reduction_physics.md

REFUTER: S-PRES adversarial pass 2026-08-23. Anchor walk eseguito in-finestra su:
`docs/rde_nozzle_MASTER.md` (righe 970-1300, 1300-1500, 1734-1974, 1974-2118),
`docs/findings_registry.yaml` (:1455-1474, :1620-1633, :1918-1931, :2019-2033,
:2140-2154, :2505-2518), `docs/glossary.yaml` (:1488-1501),
`docs/rde_nozzle_pipeline_decision_map.md` (:123-131, :230-241).
Metodo: read-then-quote; ogni finding cita il sito del capitolo (riga di
CH3_reduction_physics.md) e l'ancora di record che decide.

ESITO ANCHOR WALK: 100% dei claim load-bearing aperti alla fonte. NESSUN claim
cade (0 BREAK): le scoping-clause difficili (booking-level H2.2, DROP
geometry-signed, SBV per i due canali, L_H/delta UNDERIVED, tasso sqrt della via
valore, non-convessità H-G5) sono trascritte fedelmente e ALLA classe. I difetti
trovati sono inflazioni locali di classe/status in compressione (soprattutto
nella sezione 4, il banco), un claim di novità senza ancora su una slide, e tre
buchi di completezza che un panel ostile colpirebbe.

## Tabella finding

| # | sito (riga CH3) | classe | severità | testo | fix proposto |
|---|---|---|---|---|---|
| 1 | 388-389 (risposta banco Q1); eco a 493 (slide 3) | REPAIR | ALTA | "(ii) struttura azimutale: ... primo ordine 0.7-9% [SE]" presenta la banda 0.007-0.09 come entità dell'INTERO primo ordine del canale (ii). Di record quella banda è il SOLO termine pressure-work ("work-term 0.007-0.09 = 0.7-9%", M0:1344; "pressure-work term order a_p·St_n·beta_w ... => 0.007-0.09", M0:1856-1858); le righe avvettive non hanno numero di record ("magnitude MEASURED by M-RED", per-term table M0:1883) — la loro entità è dichiarata ignota fino a M-RED. Un esperto chiede: "e la parte avvettiva?" e la risposta compressa non la separa. Il §1.3(ii) del capitolo è corretto; la compressione del banco no. | In Q1 e slide 3: "termine pressure-work 0.7-9% [SE]; parte avvettiva senza numero di record, misurata da M-RED (B-1/B-2)". |
| 2 | 391 (banco Q1), 425-428 (banco Q3), 492-493 (slide 3) | REPAIR | ALTA | "sizing ~1% DIMOSTRATO [REP]". La cella di record dice "~1% at sizing level [REP]: Paxson-Miki area-ratio agreement 6.54 vs ~6.5" (M0:1346) — UNA istanza esterna di accordo page-verified + una non-contraddizione (Harroun). Il record non usa mai "demonstrated" per il sizing (usa "NOT demonstrated" per il ranking); "dimostrato" su un'istanza singola è sopra la classe di evidenza tenuta e viola la regola di cella "NO cell above its held evidence class" (M0:1309). | "sizing supportato a ~1% su un'istanza esterna page-verified [REP] (accordo 6.54 vs ~6.5), senza contro-istanza misurata" — mai "dimostrato". |
| 3 | 429 (banco Q3) | REPAIR | MEDIA | "R22-CFD-2 è pre-registrato proprio sulla coppia Harroun". Di record R22-CFD-2 è RI-SCOPATO e NOMINATO sulla coppia Harroun ("field-facing demonstration on the Harroun pair", registry :1462; tightener M0:1346), ma lo scheduling è "dossier PRESENTED, decision = user, post-convergence" (registry :1467) — la pre-registrazione con esiti dichiarati (T3-CONTROL) appartiene a M-RED, non a R22-CFD. Il panel chiederebbe "quando gira?" e la slide non deve implicare che sia già schedulato/pre-registrato. | "R22-CFD-2 è scopato di record sulla coppia Harroun; dossier di scheduling presentato, decisione utente pendente (registry :1462, :1467)". |
| 4 | 250-256 (§1.3 via valore "l'unica eseguibile OGGI"), 406-410 (banco Q2), 498 (slide 4) | REPAIR | MEDIA | "la via valore è ESEGUIBILE a-posteriori oggi" senza dire nel banco che eps_U NON esiste ancora: eps_U = "sweep-sup of the M-RED value legs (A)-(B) along the design sweep" a classe SAMPLED-SUP (M0:2056-2058) e M-RED è F2-QUEUED (registry :2509-2517). Il verbatim M0 "executable on the measured carrier today" (M0:2074-2075) si riferisce al LATO carrier (mu_red as-is); il numero non è producibile oggi perché manca l'ingrediente eps_U + i check a-posteriori (basin radius R-12, H-G5, coverage sweep — M0:1348 BEST cell). Risposta com'è = invito alla domanda-trappola "allora dateci il numero". | Aggiungere in Q2(b): "eseguibile sul carrier misurato (mu_red as-is) NON APPENA M-RED consegna eps_U (sweep-sup, SAMPLED-SUP); oggi nessun numero — mancano eps_U e i check a-posteriori (R-12, H-G5)". |
| 5 | 482-484 (slide 1) | REPAIR | MEDIA | "Nessun competitor del corpus letto esibisce l'oggetto scartato in forma chiusa" — claim di novità SENZA ancora e senza query-bound formale, in violazione delle regole del capitolo stesso (ogni claim con ancora) e della disciplina novità query-bounded (R5/CT-6). Non trovato nel record letto in-finestra un enunciato comparativo equivalente; "non trovato nel record" va detto così. | O ancorare a una riga di record di assenza search-proven (se esiste nei litreview registries), o riformulare: "nel corpus letto (N PDF, litmap di record) non abbiamo trovato l'oggetto scartato esibito in forma chiusa — claim di assenza, query-bounded", o togliere la frase dalla slide. |
| 6 | 452-453 (banco Q4c), 511-512 (slide 6) | REPAIR | BASSA | Il template "gain net of 2·eps, eps = measured/assumed" è ancorato a M0:1238-1240, che scopa la frase ai certificati "over a P-ONLY pipeline" — non alla pipeline full-state del programma. La forma generale per-surrogato è la clausola F5a del leg (a): "The F5a conditional-gain template binds to the surrogate actually used: 'gain net of 2·eps_G, eps_G = measured/assumed per family'" (M0:1207-1209). Il claim del capitolo ("su ogni certificato di guadagno G2-class") è difendibile ma con l'ancora sbagliata. | Ri-ancorare a M0:1207-1209 (template F5a per-surrogato) e citare M0:1238-1240 solo per il caso p-only. |
| 7 | 335 (tabella §2, riga nonconvex, colonna rimedio) | REPAIR | BASSA | "Rimedio: dominanza di valore cross-branch > 2·eps_U (M0:2106-2111)" senza il caveat del TAIL [REV2-r4-2](d): la via branch-wise è definita SOLO dove esiste una decomposizione in componenti (set disconnessi); su un set nonconvesso CONNESSO la copertura branch-wise è UNDEFINED e nessuna forma la reclama (M0:2113-2118). Il §1.3 del capitolo lo dice; la cella tabellare no, e la tabella è ciò che finisce in slide. | Nella cella: "rimedio (solo set DISCONNESSI): dominanza cross-branch > 2·eps_U; su connesso-nonconvesso UNDEFINED (M0:2106-2118)". |
| 8 | intero capitolo; in particolare banco Q1 (382-396) | GAP | ALTA | Il capitolo risponde a "cosa butta via il 2D per-fase" ma NON dichiara il confine di classe INVISCID: il contenuto viscoso/di separazione "is NOT a K term — boundary named (separated-phase monitor, T-T3-MAP(a)); no bound asserted" (M0:1886), e i dati swirl esterni sono film-cooled con caveat (M0:1388-1395). Un panel ESA chiederà per primo "e le perdite viscose / la separazione / il film cooling?": oggi il capitolo non ha la riga. Non è un canale della forchetta ed è giusto così — ma il confine va detto, o la lista "canale per canale" appare completa quando non lo è. | Aggiungere al §1.3 (e alla risposta Q1) una riga di confine: "fuori classe (non canali): contenuto viscoso/separazione — monitor di fase separata, NESSUN bound asserito (M0:1886); model-form viscoso non prezzato di record". |
| 9 | §1.1 (30-56) | GAP | MEDIA | Lo scope di settore di [T-DISC] non è dichiarato: gli enunciati sono fatti "on the supersonic-map sector; the subsonic sector joins the mixture form and is out of this theorem's scope, declared" (M0:1025-1028). Reviewer ostile: "il vostro teorema di fibra copre le fasi subsoniche?" — la risposta onesta di record è NO, dichiarato. | Una frase in §1.1: "enunciati sul settore supersonic-map; settore subsonico fuori scope del teorema, dichiarato (M0:1025-1028)" + riga negli APERTI se consumata dal deck. |
| 10 | §1 tutto (13-317) | GAP | MEDIA | Leggibilità non-esperto: il capitolo usa senza definirli "per-fase/quoziente wave-frame", "booking", "on-ray/off-ray", "fitted sheet", "St_n", "fibra". Per il deck ESA (nulla di scontato, da mandato S-PRES) manca un cappello di 4-5 righe che dica cos'È la riduzione (quoziente T-T0P → march 2D per-fase) prima di elencare cosa perde; il canale (i) cita [T-T0P] senza mai enunciarlo. | Premettere al §1 un box "la riduzione in 3 mosse" (quoziente esatto sotto pin d'onda [T-T0P] → march 2D per-fase → media di ciclo) + mini-glossario dei 6 termini con rimando a glossary.yaml. |
| 11 | 194, 209, 296, 336-342 (cite registry :2026/:2147/:1925) | NOTE | BASSA | Le citazioni registry puntano alle righe `severity:` — il testo vive alla riga +1 (C25 magnitude a :2027, R26 a :2148, A32 a :1926). Off-by-one EREDITATO da M0 ([REV2-r1-17] dichiara :2026 line-verified; il file è slittato di 1 da allora). Non cade nulla, ma il retro-audit dichiarato del deck (catena ancora→fonte) inciamperebbe. | Dichiarare l'ereditarietà nel capitolo ("cite = righe M0 di record; testo a ±1 nel registry corrente") o correggere a :2027/:2148/:1926 con nota. |
| 12 | 32-33 | NOTE | BASSA | "separa due oggetti che il campo confonde" — editoriale senza ancora; il record documenta una TENSIONE aperta adjudicata a soglia (R26, registry :2148), non una confusione del campo. | "separa due oggetti che nel dibattito di letteratura restano non distinti (tensione R26, registry :2148)". |
| 13 | 156-165 (canale (i)) | NOTE | BASSA | La cella (i) BEST di record porta anche "Cor 5.1 scoping (cl(Omega_march), slip-free)" (M0:1343); il capitolo comprime in "MODULO le liste di gap dichiarate" perdendo lo scoping slip-free, che è proprio la faccia della esclusione G9 citata nel WORST. | Aggiungere "(+ scoping Cor 5.1: cl(Omega_march), slip-free)" nella voce (i) BEST. |

## Banco utente — giudizio per domanda

- **Q1 (censimento canale-per-canale)**: struttura fedele alla forchetta di
  record; difetti = finding #1 (conflazione work-term/primo-ordine), #2
  ("dimostrato"), #8 (confine inviscid assente). Non evasiva, non circolare.
- **Q2 (zero numeri argmax-shift)**: la risposta migliore del capitolo — la
  disciplina-è-il-claim è verbatim di record (M0:1348, 1953-1956) e Humphreys
  1971 è ancorato (M0:1455-1464). Difetto = finding #4 ("eseguibile oggi").
- **Q3 (Harroun kill-shot)**: corretta e ben armata (non-discriminazione ai
  limiti verificati, M0:1326-1329, 1346; sizing vs ranking R26 registry :2148;
  no-external-referee M0:1322-1333). Difetti = finding #2 e #3.
- **Q4 (shroud)**: fedele: worst-direction marker + candidato swirl-breaker +
  catena B-2/F2a sono testo di record (M0:1345, 1013-1015); l'OPEN sulla
  spiegazione è dichiarato. Difetto marginale = finding #6 (ancora del template).

## VERDETTO

**REGGE-CON-RIPARAZIONI.**

Conteggio: **0 BREAK, 7 REPAIR (2 alta, 3 media, 2 bassa), 3 GAP (1 alta,
2 media), 3 NOTE — 13 finding totali.**

Le due riparazioni più urgenti:
1. (#1+#2, banco Q1/Q3 + slide 3) separare il work-term 0.7-9% dalla parte
   avvettiva senza-numero-di-record, e sostituire "sizing dimostrato" con
   "supportato su un'istanza [REP]" — sono le due celle che il panel legge per
   prime e oggi stanno sopra la classe tenuta.
2. (#8) aggiungere la riga di confine inviscid/viscoso (M0:1886): senza, il
   censimento "canale per canale" si fa smontare dalla prima domanda su
   separazione/film-cooling.
