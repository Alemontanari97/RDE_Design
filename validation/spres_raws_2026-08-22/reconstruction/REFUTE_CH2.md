# REFUTE_CH2 — verifica avversariale di CH2_averaged_optimality.md

Refuter S-PRES, 2026-08-23. Mandato: anchor walk 100% dei claim load-bearing,
attacco al banco §4, buchi, overclaim scan. Ancore APERTE in finestra:
docs/rde_nozzle_P1_sections_5_7.md (§5 completo, r.25-207),
docs/rde_nozzle_MASTER.md r.118-129, 218-227, 2810-2969,
docs/claims_registry.yaml r.374-391, 570-600, 1920-1937,
docs/rde_nozzle_literature_map.md r.395-469, docs/choice_ledger.yaml r.733-750,
docs/rde_nozzle_pipeline_decision_map.md r.58-67, docs/rde_nozzle_PROGRESS.md
r.33-44, 112-121, tests/test_bell_optimality.py r.1-95,
tests/test_gamma_probe.py r.18-31, 95-143, validation/s25bis_closing_suite.log
r.55-83, validation/a1_toc_variational_jax.py r.1740-1753,
validation/o33_bench.py r.286-295 + grep f3, grep repo "two-sign/C32".

## Esito dell'anchor walk (sintesi)

TUTTI i numeri misurati citati dal capitolo reggono verbatim sui carrier:
T1c 6 casi (3.80/5.48 +4.94; 21.16/32.01 +3.33; 3.98/6.61 +7.45;
23.30/40.57 +5.06; 3.94/7.07 +9.71; 22.69/42.51 +6.30 — log:61-76);
drift 2.9e-01 / 9.4809e-03 (P1:54-57); shift -0.56% / penalty ~3e-6
(test_gamma_probe.py:99-107); gamma_eff <0.1 pt / <gamma> >1 pt / controllo
negativo (ibid.:126-142); eps*_real 3.49-3.52 (P1:165-170); -2.39%
(P1:106-107); lip pinned by equality (a1:1748, `lip_eq = LinearConstraint(...,
[yL], [yL])`); controesempio 2 fasi (-1,+3) (M0:2868-2870); quote verbatim
"NO phase satisfies its own wall condition..." ESATTA (P1:68-71); dottrina
5-fonti (litmap:401-404); concessione query-bounded (litmap:442-456);
Kraiko-Osipov (M0:2908-2926); H-EXO (registry:1926-1937); C54 OPEN
(choice_ledger:737-746, incumbent verificato); I4 "nudo" (M0:124 verificato).
L'OPEN §3.6 (due segni mai eseguiti su campi marched) è CONFERMATO da grep
repo: esiste solo la conferma simbolica R=(+2,-1), w=(1,4)
(literature_review/reports/VERIFICATION_FABLE_2026-08-13.md:355), che è il
carrier dell'esistenziale, non l'esecuzione sul parco. Nessun claim cade.

## Findings

| # | sito (riga capitolo) | classe | severità | testo | fix proposto |
|---|---|---|---|---|---|
| 1 | r.20-22 (§1.1) + r.207 (tabella riga 1) | REPAIR | MEDIA | Class bundling: la tabella mette "Sistema di stazionarietà a 3 blocchi" sotto THEOREM* [T-T7FS] in blocco. Ma M0:2812 stampa "[T-T7FS] THEOREM-SCHEMA 8 ... SCHEMA." e "(verified formally)" per la STRUTTURA (M0:2818); il THEOREM* di record (registry:578-580; M0:2935-2941) copre esattamente la differenziazione sotto l'integrale di ciclo — cioè che (b)+(c) siano L^1(dmu) genuini e (P)(ii) necessaria. §1.6 lo dice giusto; §1.1 e la tabella no. Un panelist ostile che apre M0:2812 legge "SCHEMA" per primo. | Splittare la riga 1: struttura a 3 blocchi = SCHEMA verified-formally (M0:2812,2818); L^1-genuinità + necessità = THEOREM* (registry:580). Allineare §1.1 ("classe THEOREM* nel registry" è vero ma va detto CHE COSA il registry classifica). |
| 2 | r.260-271 (banco Q1) | REPAIR | MEDIA | Risposta parzialmente evasiva sul comparatore chiesto: il panel chiede la differenza vs "design sul campo medio" (= I4, design-on-mean-state); la risposta pivota sui numeri di naive-mean (-2.39%) e mass-mean (T1c) — che sono gli ALTRI due comparatori sbagliati, non I4. Un'istanza computata I4-vs-(**') non esiste nel record letto A NESSUN DOF (non trovata in finestra), e la risposta non lo dice. | Aggiungere la frase esplicita: "il comparatore design-on-mean-state (I4) non ha NESSUNA istanza computata di record, a nessun DOF — i numeri citati misurano gli altri due modi sbagliati (naive e mass-mean)". Poi il resto regge. |
| 3 | r.286-290 (banco Q2, chiusa) | REPAIR | MEDIA | Overfit di mappatura: G6 è dichiarata "istanza misurata della distinzione (ii)-vs-(iii)". G6 discrimina chiusure DEL DATO (gamma_eff pesata vs <gamma> aritmetica) dentro l'oracolo gamma-const (test_gamma_probe.py:23-27): entrambe sono riduzioni mean-data — istanzia pesata-vs-naive sul lato dato, non design-on-mean-state-vs-(**'). L'ultima frase del capitolo ("anche la media giusta del dato deve essere pesata") è la lettura corretta; l'etichetta (ii)-vs-(iii) no. | Riformulare: "istanza della lezione pesata-vs-aritmetica SUL LATO DATO (chiusura gamma)", senza l'etichetta (ii)-vs-(iii). |
| 4 | r.207 (tabella riga 1, colonna falsificatore) | DOWNGRADE | BASSA-MEDIA | Il falsificatore citato include la metà RITIRATA: "famiglia ... con derivata non dominata in L^1" è la vecchia forma che registry:586 dichiara sostituita di record (S14: "the former negative-existential-over-envelopes form was not finitely observable"). | Tenere solo la forma di record: famiglia di ciclo certificata con dJ /= Int F' dmu oltre barre (O3-class, eseguibile). |
| 5 | r.213 (tabella content split) + r.90-91 eredità | REPAIR | BASSA | Ancora che non regge alla riga citata: "f3* nodewise in validation/o33_bench.py:292" — la r.292 reale è dentro l'helper `drift()`; la formula f3* è a o33_bench.py:320 (docstring r.32). L'ancora stantia viene da M0:2891 stesso: il capitolo la riproduce senza read-verify (viola la sua stessa regola read-then-quote) e per la regola del retro-audit è anche un finding candidato CONTRO M0. | Citare o33_bench.py:320 (+ docstring :32) e mintare il finding di stale-anchor su M0:2891. |
| 6 | r.98, 300, 350-355 (T3 invocata, mai definita) | GAP | MEDIA | La classe T3 porta il peso della slide "tre modi di mediare" (caso di coincidenza) ed è invocata >=5 volte, ma il capitolo non dice mai che cosa È fisicamente la classe di collasso T3 (quando/perché w diventa fase-indipendente). Il non-esperto non può parsare la slide 2; l'esperto chiede "what is T3?" e il capitolo non ha la risposta locale. | Una frase + ancora alla definizione di T3 (P1 §2-§4 / M0 Parte III T3) in §1.5; stessa frase nella nota della slide 2. |
| 7 | r.294-297 (banco Q3) | GAP | MEDIA | w(xi) mai dato: "peso geometrico-cinematico, w > 0" senza forma esplicita né puntatore al doc dove la forma vive. La domanda del panel è "da dove viene" — la risposta è genealogica (derivazione, Kraiko-Osipov W(t)) ma non costruttiva. Nelle slice lette (P1 §5, M0 T7) la forma esplicita non compare. | O citare la forma esplicita dal doc di prova (T7/D3) con ancora, o dichiarare in Q3: "forma esplicita in <doc>, non riprodotta qui" / "non trovata nella finestra" — mai lasciarla implicita davanti al banco. |
| 8 | r.48-50, 62-64, 121-123 | GAP | BASSA | Glosse per non-esperto mancanti: G_xi "densità di Hadamard", g_L, (P)(ii), N_K/T_K (normal/tangent cone) usati senza definizione one-line. CH2 può appoggiarsi a CH1, ma il consumer Q&A/deck ha bisogno delle glosse locali (una riga ciascuna). | Aggiungere 3-4 glosse one-line al primo uso (o box notazione a inizio capitolo). |
| 9 | r.245 (§3.5) | NOTE | BASSA | Ancora imprecisa nel nome file: "pipeline_decision_map.md:65" — il file di record è docs/rde_nozzle_pipeline_decision_map.md (la r.65 È la riga C54: contenuto regge). | Correggere il path completo. |
| 10 | r.246-251 (§3.6) e r.104 | NOTE | BASSA | Collisione di namespace "C32": choice_ledger.yaml C32 (r.495) è la curvature policy SR1 — oggetto DIVERSO dal "C32 falsifier" a due segni di M0:2895. Nella banca Q&A la sigla nuda è ambigua. | Disambiguare: "falsificatore-C32 (M0:2895, CLAIM-16 companion)", mai "C32" nudo. |
| 11 | r.322 (banco Q5) | REPAIR | BASSA | "è l'UNICA spina condizionale analitica" — il capitolo stesso elenca [C-MAJDA] (§3.2) e [C-O33] (§3.4) come conditionals vivi. P1:131-137 dice "the ONE named analytic conditional" per la spina di differenziazione, CON [C-MAJDA] ereditata a parte sui fronti; il deck point 4 (r.360-362) porta già la parentesi giusta. Q5 no. | Allineare Q5 al deck point 4: "l'unico conditional analitico della spina di differenziazione ([C-D25U]); [C-MAJDA] sui fronti e [C-O33] numerico restano nominati a parte". |
| 12 | globale | NOTE | — | Positivo di verifica: tutti i numeri, la quote verbatim P1:68-71, il controesempio (-1,+3), le classi [T-P3]/[T-T7CN]/[T-T7RED]/C-HEXO e gli OPEN §3.1-3.7 reggono alle ancore alla classe dichiarata; l'OPEN §3.6 è ora anche grep-confermato sul repo (solo carrier simbolico VERIFICATION_FABLE_2026-08-13.md:355, nessuna esecuzione su campi marched). Il capitolo può citare quel carrier come prova dell'esistenziale. | Aggiungere l'ancora VERIFICATION_FABLE:355 all'OPEN §3.6 (rafforza, non cambia il verdetto OPEN). |

## Conteggio

- BREAK: 0
- REPAIR: 5 (#1, #2, #3, #5, #11)
- DOWNGRADE: 1 (#4)
- GAP: 3 (#6, #7, #8)
- NOTE: 3 (#9, #10, #12)

## VERDETTO

**REGGE-CON-RIPARAZIONI.** Nessun claim load-bearing cade; i numeri e le
quote sono esatti ai carrier; gli OPEN sono dichiarati onestamente (e §3.6
esce RAFFORZATO dal grep del refuter). Le riparazioni obbligatorie prima del
consumo deck/Q&A: (1) lo split di classe SCHEMA-struttura vs
THEOREM*-differenziazione su [T-T7FS] (finding #1 — è il punto dove un
panelist ostile con M0 in mano smonta la tabella); (2) la frase esplicita
"I4 mai computato a nessun DOF" nella risposta Q1 (finding #2 — senza, la
risposta al banco è un pivot). #3/#4/#5/#11 sono riformulazioni locali;
#6/#7 sono i due buchi di completezza da chiudere perché la storia regga
davanti a esperto e non-esperto.
