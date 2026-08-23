# REFUTE_DESIGN — Refutazione del research design dell'atlas (ATLAS_RESEARCH_DESIGN.md)

Refuter S-PRES, 2026-08-23. Stadio di confronto: il design integrale contro il
perimetro VERO ri-misurato in finestra — SCAFFOLD §1+§6 (letto integrale; L0-L6
:28-65, amendment L7/L8/L9 :218-253), M0 struttura Parti I-VII (grep in
finestra: :25/:63/:409/:2982/:3008/:3047/:4246 — ancore del design CONFERMATE),
D6 spina+gate (grep: F0 :37 .. F6 :275, G0-G6 :751-816, §3 :684, §4 :737,
§7 :1093, Annex B :1133 — ancore CONFERMATE), FILE_MANIFEST.csv (826 righe,
aggregato per area in finestra), literature_registry.yaml (174 id, grep -c in
finestra; ogni id citato dal design verificato per grep esatto),
COMPLETENESS_CRITIC.md (21 righe + banco-utente, letto integrale). Arco di
consumo: gate del design prima del lancio delle onde W-A..W-D.

Attacco sui 4 fronti ordinati: (1) completezza della matrice vs perimetro;
(2) senso di ricerca genuino delle celle-letteratura; (3) eseguibilita' dei
contratti e pesi; (4) disposizione delle 21 righe del critic + banco-utente.

---

## Tabella findings

| # | sito | classe | severita' | testo | fix |
|---|------|--------|-----------|-------|-----|
| 1 | §1 "Conteggio celle" + §5 lint-matrice | BREAK | ALTA | Il conteggio si dichiara "misurato sulla matrice qui sopra" ma e' FALSO tre volte: (a) la decomposizione dichiarata 20 (G,H,J,K) + 5 (P) + 10 parziali = 35, non 30; (b) la lista "10 parziali" contiene 12 item (A-iii, C-ii, D-ii, D-v, E-ii, F-ii, I-ii, I-iii, L-v, M-v, N-v, O-v); (c) il ricount per-riga in finestra da' 37 celle non-piene (le celle A-ii "COPERTA (parziale)", E-iii "COPERTA-parziale", L-i e M-i "COPERTA-parziale" sono etichettate parziali nel testo-riga ma ASSENTI dalla lista), e M-ii/O-iii sono COPERTA nel testo-riga ma FUORI-PERIMETRO nel conteggio (doppia classificazione). Il lint-matrice §5.3 ancora il completamento a "le 30 SCOPERTE devono risultare 0": il numero-gate e' sbagliato. Violazione SR-12 in spirito (conteggio dichiarato misurato, non misurato). | Sostituire il paragrafo con una TABELLA PER-CELLA (80 righe, stato esplicito per cella: COPERTA / SCOPERTA+contratto / FUORI-PERIMETRO / PARZIALE+contratto-residuo), rigenerata per enumerazione; lint-matrice punta alla tabella, mai a un numero riassunto. |
| 2 | §2.3 template §6 STORIA + §5 lint 5 | BREAK | ALTA | Il template impone a OGNI capitolo le tre battute "derivazione originale -> riderivazione agnostica Fase A -> convergenza" con ancore, e il lint 5 fa del trittico un criterio di completamento. Ma la Fase A di S-FOUNDATIONS ha riderivato il nucleo teorico (ottimalita'/riduzione/fondazioni), NON la materia di CH4 (scelte macchina), CH9 (certificazione), CH10 (contratto-dati) e gran parte di CH5/CH6: per quegli argomenti la battuta 2 NON HA RECORD. Come scritto, lo storico B8 puo' solo fabbricare ancore o fallire il lint per sempre: un criterio di completamento non soddisfacibile e' un difetto del design, non dei capitoli. | Battuta 2 CONDIZIONALE: "se l'argomento e' nel perimetro Fase A -> diff del derivatore cieco con ancora; altrimenti riga esplicita NON-RIDERIVATO + quale ALTRA doppia prova lo copre (refuter/panel/carrier, con ancora)". Lint 5 emendato di conseguenza. |
| 3 | §5 onda W-B (B1-B7 vs B8) | REPAIR | ALTA | B8 (historian) scrive le §6 di TUTTI i capitoli "in un solo passaggio" nella STESSA onda in cui B3 edita CH1+CH3, B4 CH4, B5 CH5+CH6, B6 CH8, B7 CH2+CH7: ogni file-capitolo e' co-editato da due agenti concorrenti. Violazione frontale della regola standing sessioni-parallele "file disgiunti" (CLAUDE.md Preferenze; incidenti R35 2026-08-13 di record). | B8 parte come ROUND 2 di W-B (dopo l'atterraggio di B1-B7), oppure consegna le §6 come file separati per-capitolo che l'orchestratore merge-a a valle. Dichiararlo nel piano-onda. |
| 4 | §1 riga A(ii) vs §2.2 CH1; §2.2 CH8 vs §5 B6; CH5/CH6 vs §5 lint 5 | REPAIR | ALTA | Cablaggio §7 rotto in tre punti: (a) A(ii) promette "confronto masters/lauer_ansell -> §7 POSIZIONAMENTO di CH1 (contratto in §2 qui sotto)" ma §2.2-CH1 NON elenca alcun §7 e nessun writer W-B lo possiede; (b) §2.2-CH8 elenca "§7 parametrizzazione (F(ii))" ma il brief B6 dice solo "§1.7 M1-M5 + §3.5"; (c) B3 per CH3 dice "caveat/cross-ref" senza nominare il §7-DWR che §2.2-CH3 prescrive. Inoltre lint 5 esige "ogni §7 cita >= 1 id di registry per strumento" per CH1-CH10, ma per CH5/CH6 la colonna (ii) e' FUORI-PERIMETRO: la meta' (a) STRUMENTI del §7 e' insoddisfacibile come scritta (nessuna regola di vacuita' dichiarata). | Assegnare esplicitamente CH1 §7 (a B3), CH8 §7 (a B6), nominare CH3 §7 nel brief B3; aggiungere al template la clausola "§7(a) puo' dichiarare NESSUNO STRUMENTO PROPRIO con puntatore alla cella FUORI-PERIMETRO della matrice" e riflettere la clausola nel lint 5. |
| 5 | §0 colonna (ii) + §1 righe C/D/I/J/K | REPAIR | MEDIA | Id citati NON verbatim dal registry (grep esatto in finestra: 0 hit): `hicken_zingg` (vero id: wanted_hicken_zingg_2014), `becker_rannacher` (wanted_becker_rannacher_2001), `fidkowski_darmofal` (wanted_fidkowski_darmofal_2011), `masters_2017` (masters_etal_2017), `thakur_nadarajah` (wanted_thakur_nadarajah_2024); `gelb_tadmor` e `paciorri_bonfiglioli` (riga K(ii)) NON HANNO alcuna riga (il piu' vicino: wanted_onofri_paciorri_2017_book). Il design viola la SUA regola "ogni ref = un id del registry; ref fuori registry = riga nuova PRIMA dell'uso" — nei contratti stessi. Il refuter C5 lo intercetterebbe in W-C, ma i writer W-B partirebbero con puntatori rotti. | Correggere gli id in §0/§1 alla forma esatta del registry; per Gelb-Tadmor e Paciorri-Bonfiglioli: mint di righe (WANTED con owner) PRIMA di W-B, oppure ri-ancorare il lineage a D6 :256-263 dichiarando l'eccezione non-registry nel contratto K(ii). |
| 6 | §1 riga E(ii) (contratto CH7 §7) | REPAIR | MEDIA | Il confronto-cardine "chiusura mean-swirl vs letteratura swirl-nozzle" e' ancorato a `wanted_tillyaeva_1975`: status WANTED, paths [] (verificato in finestra — il paper NON e' su nessuna delle 4 root, russo, [HARD]). Un §7 non puo' posizionarsi contro un paper che nessuno ha letto: come scritto il contratto o resta vuoto o induce una summary inventata (vietata dalle regole del registry stesso). | Il contratto E(ii) nomina i carrier SURROGATI di record (D6 G5 riga 2.2(f); kraiko_tillyaeva_2015 per la genealogia; T-N6-2 free-vortex come termine interno) e dichiara il confronto diretto PENDING-PROCUREMENT con owner — mai una summary del paper assente. |
| 7 | §1 riga G(ii) (contratto M4/M5) | REPAIR | MEDIA | Cella a rischio decorazione: "M4/M5 vs mondo (deflated continuation, branch-and-bound Lipschitz — `nocedal_wright` per il quadro)". Nocedal-Wright NON porta la deflated continuation (linea Farrell) ne' il B&B Lipschitz-globale: l'unico id citato non copre gli oggetti del confronto, nessun id di registry esiste per essi, e "claim di confronto query-bounded al registry" non nomina alcuna query. E' esattamente la cella "confrontare con letteratura" senza CON COSA che il fronte (2) vieta. | O mint di righe WANTED (deflation: Farrell et al.; global opt Lipschitz: un riferimento canonico) con owner PRIMA di W-B, o ri-scope del contratto: confronto dichiarato NOT-FOUND(q) con il testo della query nel §7 di CH8 (come gia' fatto, correttamente, per G(iii)). |
| 8 | §1 preambolo (derivazione righe) vs SCAFFOLD §6 | GAP | MEDIA | La derivazione a priori enumera "layer SCAFFOLD L0-L6" ma lo SCAFFOLD di record ha ANCHE L7 (validation record layer), L8 (literature layer, 4 root), L9 (governance) — amendment :218-253. Nessuna delle tre ha riga, assorbimento dichiarato o FUORI-PERIMETRO (L8 e' plausibilmente riga N, L7 riga J — ma non e' DETTO). Il falsificatore del design (§5) scatta proprio su "aspetto del perimetro senza riga": qui e' gia' vero alla nascita. | Tre righe di dichiarazione in §1: L7 -> assorbita da riga J(i)/S-CERT + CH-REF; L8 -> assorbita da riga N + lint-registri; L9 -> FUORI-PERIMETRO con ragione (governance harness, non materia d'atlas). |
| 9 | §1 riga E(iii) | GAP | MEDIA | "COPERTA-parziale: CH7 §1.4" senza contratto per la meta' mancante: viola la regola §0 ("ogni cella porta UNO di: puntatore / SCOPERTA+contratto / FUORI-PERIMETRO"). La cella non compare nella lista parziali del conteggio ne' in §2.2-CH7: il residuo e' silenziosamente perso. | Nominare il residuo di E(iii) (cosa di CH7 §1.4 NON copre il senso-precedenti dell'edificio averaging) con contratto, o rietichettare COPERTA con motivazione. Entra nella tabella per-cella del fix #1. |
| 10 | §1 riga J(iii) | GAP | BASSA | "la prassi del campo (validazione a confronto singolo)" — claim sul campo senza refs e senza query, a differenza di G(iii) che dichiara "claim search-proven da eseguire in onda". Cosi' com'e' il writer B1 la scriverebbe come asserzione non ancorata. | Aggiungere al contratto CH9(iii) la forma di G(iii): query nominata da eseguire in onda, esito NOT-FOUND(q) o refs. |
| 11 | §1 riga L vs D6 §4 :737 e §7 :1093 | GAP | BASSA | Due pezzi di perimetro D6 senza cella ne' dichiarazione: la SOTA tool matrix §4 ("what the team must actually know" — di fatto assorbita dalla colonna (ii), ma non dichiarato) e il RISK REGISTER §7 (:1093) — nessuna riga della matrice lo nomina; un panel ESA chiede i rischi di programma quasi certamente quanto chiede il globale M1-M5. | Riga L estesa: (ii) dichiarare l'assorbimento tool-matrix nella colonna (ii) trasversale; (v) o CH6 §1.5: una riga "rischi di programma" ancorata a D6 §7, oppure FUORI-PERIMETRO motivata. |
| 12 | §2.1 CH-REF ("senza claim propri") + riga P | GAP | BASSA | La disciplina theory-as-code (claims_registry + claim lint + rejector sulla TEORIA, SCAFFOLD §2/§5 — "il corpus non puo' driftare, machine-rejected") non ha cella (iv): e' una proposta di metodo vendibile a un ente (come si tengono coerenti 174 paper + 62 scelte + centinaia di claim), ma CH-REF e' dichiarato senza claim e quindi non puo' portarla, e riga P copre la storia, non la governance. | Una cella: P(ii)/(iv) esteso ("strumenti del metodo: registri tipizzati + lint come proposta") o una sottosezione del §7 di CH9; una riga nella matrice che la possiede. |
| 13 | §5 W-B B8 (peso) | REPAIR | MEDIA | B8 e' lo slot piu' fragile del piano: ~10 capitoli x 3-4 argomenti x 3 battute ANCORATE, con fonti M0 (4k+ righe), PROGRESS_ARCHIVE (append-only, storia intera), ledger e git log, dentro il budget medio di ~60-90k/agente dell'onda. Sottostimato e senza strategia di lettura dichiarata (contro la disciplina context-usage: letture mirate, niente re-read). Rischio concreto: ancore approssimative = esattamente cio' che C5 boccia. | Pre-pass economico dedicato: indice-ancore (grep dei blocchi amendment/supersession di M0 + intestazioni LOG di PROGRESS_ARCHIVE + `git log --oneline` filtrato) consegnato a B8 come input; oppure split B8a/B8b per gruppi di capitoli con budget proprio. |
| 14 | §5 lint-manifest | NOTE | BASSA | FILE_MANIFEST.csv ha 826 righe di cui ~61 __pycache__/bytecode (aggregato in finestra) piu' blocchi raws voluminosi (sfoundations 280 righe): "ogni riga -> disposizione; zero righe orfane" senza una regola di disposizione BULK per-directory spreca peso W-D su file non-portanti per definizione. | Dichiarare nel lint 2 la regola bulk: una riga di disposizione per directory-classe (pycache/raws/reports), file singoli solo per docs/src/tests/validation-advisory. |
| 15 | §4 (banco-utente) | NOTE | BASSA | Le 7 domande-utente della milestone sono mappate solo TRANSITIVAMENTE: il critic le verifica (5 coperte, riga 9 scoperta, riga 18 parziale) e il design dispone le righe 9/18 — la catena chiude, ma il design non ri-enuncia MAI la mappa domanda->capitolo, e il banco e' l'ordine vincolante della milestone, non un derivato del critic. | Una riga in §4 sotto la tabella: le 7 domande del banco con puntatore (5 -> celle gia' coperte con anchor, 2 -> righe critic 9/18 disposte). |
| 16 | §3 nota deck | NOTE | BASSA | Gli archi di consumo a valle non sono tutti nominati: la graph-visualization spec (addendum cace6db: mappa-decisioni walkable, per-nodo scelta+alternative+perche'+falsificatore) e il retro-audit con ROBUSTNESS VERDICT (addendum 1514641: conteggi walked/reduced/findings nel log di chiusura) consumano l'atlas ma il §3 nomina solo l'ossatura narrativa e il ponte B1. | Due righe nella nota deck: CH4 §1.3/§7 + choice ledger = sorgente della mappa walkable; il lint-critic/lint-matrice alimentano i conteggi del retro-audit di chiusura. |

---

## Verifiche passate (dichiarate per onesta' simmetrica)

- Ancore di perimetro del design TUTTE confermate in finestra: Parti M0
  (:25/:63/:409/:2982/:3008/:3047/:4246), D6 (F0 :37, F3 :214, F6 :275,
  G0-G6 :751-816, Annex B :1133), registry 174 id.
- Fronte (4): 21/21 righe del critic hanno disposizione nella tabella §4,
  con cella di matrice e onda; le 3 BLOCKING sono in W-A come gate.
  Nessuna riga persa (confronto riga-per-riga in finestra).
- Copertura gate: G0 (riga I), G1 (J), G2 (L(v)), G3/G4 (M(v)), G5 (coperto
  di record via CH2 §1.8, adjudicato dal critic riga 19), G6 (K). Nessun
  gate orfano.
- La maggioranza delle celle (ii)/(iii) sono contratti VERI: refs nominate,
  asse dichiarato, casa di atterraggio (le eccezioni sono le righe #5-#7,
  #10 qui sopra). Il principio di derivazione a-priori-poi-critic e' sano e
  il test di auto-consistenza e' un'idea corretta.
- L'aggiudicazione "engine-speed = estensione, non capitolo" e le mancate
  promozioni di §2.1 sono derivate dalla matrice in modo verificabile.

---

## VERDETTO

**REGGE-CON-RIPARAZIONI**

Conteggio: **16 findings — 2 BREAK / 6 REPAIR / 5 GAP / 3 NOTE**
(severita': 4 ALTA / 6 MEDIA / 6 BASSA).

I due BREAK non invalidano la matrice come mappa (le righe e i contratti
tengono): colpiscono l'ARITMETICA di completamento (#1) e la
SODDISFACIBILITA' del lint-template (#2) — entrambi gate di chiusura del
design stesso. Con #1-#4 riparati PRIMA del lancio di W-B (e #5-#7 nei
brief dei writer), il piano d'onde e' eseguibile ai pesi dichiarati salvo
B8 (#13).

Le 3 riparazioni piu' urgenti:
1. #2 — battuta-2 del template §6 resa condizionale (ramo NON-RIDERIVATO
   dichiarato) + lint 5 emendato: senza, il design non puo' completarsi
   onestamente.
2. #1 — tabella per-cella delle 80 celle al posto del conteggio (che oggi
   e' falso tre volte); lint-matrice ri-ancorato alla tabella.
3. #3+#4 — cablaggio W-B: B8 a round separato (file disgiunti) e ownership
   esplicita dei §7 di CH1/CH3/CH8 + clausola di vacuita' §7(a) per CH5/CH6.
