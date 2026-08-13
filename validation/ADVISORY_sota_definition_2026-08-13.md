# ADVISORY — DEFINIZIONE SOTA della classe di compito «confrontazione verificata corpus × programma a tre strati»

**Data**: 2026-08-13
**Versione**: 2 — **REVISIONE DI GIUDICE DOPO ATTACCO DEL REFUTER** (round 1 di riparazione)
**Ruolo di questo documento**: verdetto di sintesi di un giudice su CINQUE proposte indipendenti e in cieco
(lenti: `evidence-synthesis`, `llm-agent-systems`, `verification-qa`, `metascience-audit`, `comparison-methodology`),
**riparato** contro l'attacco di un refuter default-REFUTE che ha esaminato criterio per criterio la
FALLIBILITÀ REALE di ogni test.
**Stato**: ADVISORY — non è ancora di record finché non ratificato e ancorato a una fase del piano (R1).
**Convergenza**: NON CONVERSO (il refuter ha chiuso il round 1 con `converged: false`); questa versione è la
risposta del giudice e va ri-sottoposta al refuter. I residui aperti sono nominati in fondo, non nascosti.

## Classe di compito definita

Dati (a) un corpus di ~25 paper primari (PDF; alcuni storici, alcuni in lingua straniera, alcuni solo
abstract-accessibili) e (b) un programma di ricerca a tre strati — TEORICO (teoremi con classe di rigore,
ipotesi nominate, esclusioni di scopo), FORMALE (condizioni di ottimalità, invarianti, identità, BC),
ALGORITMICO (pipeline eseguibile con certificati, gate, oracoli che possono rigettare) — produrre una
CONFRONTAZIONE VERIFICATA: per ogni paper `{contenuto | minaccia | da adottare | corregge}` × 3 strati; per ogni
claim del programma `{sopravvive | sopravvive-qualificato | falsificato | non-testato}`.
Vincoli reali: esecutori = agenti LLM; budget di token finito; esiti DI RECORD (citati in un paper, usati per
decidere il lavoro futuro) ⇒ falso positivo e falso negativo hanno costo alto e **asimmetrico**.

**Principio-guida del set**: nessun criterio sopravvive senza un test che possa FALLIRE su un'orchestrazione
reale. **Corollario aggiunto in v2**: nessun test sopravvive se il numero che produce non è distinguibile dal
RUMORE dell'apparato, se il METRO con cui è confrontato è prodotto dallo stesso ceppo che genera i verdetti, o
se il suo DENOMINATORE è auto-dichiarato dall'agente che ne beneficia. Questi tre buchi — non i criteri mancanti —
sono stati il contenuto principale dell'attacco.

---

# SEZIONE 0 — ESITO DEL ROUND DI ATTACCO E DISPOSIZIONI DEL GIUDICE

| Criterio v1 | Verdetto refuter | Disposizione del giudice in v2 |
|---|---|---|
| SOTA-1 | TEST-NON-MISURABILE | **RIPARATO** + ASSORBE la garanzia mancante «freeze dell'oggetto sotto test» |
| SOTA-2 | TEST-NON-MISURABILE | **RIPARATO** (prova di sparabilità resa aggiudicabile; confine con SOTA-9 dichiarato) |
| SOTA-3 | TEST-NON-MISURABILE | **RIPARATO** (witness atteso, bucket non-rilevabile, iniezione multipla, preventivo) |
| SOTA-4 | TEST-NON-MISURABILE | **RIPARATO** + ASSORBE la garanzia mancante «gold definito e validato» + l'unico contenuto di SOTA-18-v1 |
| SOTA-5 | REGGE | **CONSERVATO + ESTESO** con la garanzia mancante «voce dello span e hop-count» |
| SOTA-6 | TEST-NON-MISURABILE | **RIPARATO** (qualità OCR senza riferimento LLM; regioni prosa/equazioni/tabelle separate) |
| SOTA-7 | TEST-NON-MISURABILE | **RIPARATO** (disegno appaiato contro baseline `b`; unità «cella» unificata) |
| SOTA-8 | REGGE | **CONSERVATO + ESTESO** con la garanzia mancante «simmetria dell'attacco per polarità» |
| SOTA-9 | TEST-NON-MISURABILE | **RIPARATO** (unità di misura unica per tutto il set; soglie a due lati) |
| SOTA-10 | REGGE | **CONSERVATO**, le due riserve promosse a voci di test |
| SOTA-11 | TEST-NON-MISURABILE | **RIPARATO** (ricostruzione attributo-per-attributo, non giudizio su prosa) |
| SOTA-12 | TEST-NON-MISURABILE | **RIPARATO** (il denominatore E esce dalle mani di chi ne beneficia) |
| SOTA-13 | REGGE | **CONSERVATO**, i due semi passano al registro unico |
| SOTA-14 | REGGE | **CONSERVATO**, riserva sulla soglia promossa a voce di test; assorbe la sostanza di SOTA-18-v1 |
| SOTA-15 | TEST-NON-MISURABILE | **RIPARATO** (appaiamento obbligatorio, MR5 rimossa, preventivo dichiarato) |
| SOTA-16 | REGGE | **CONSERVATO + ESTESO**: (v) diventa la BASELINE DI RUMORE APPAIATA di record dell'intero set |
| SOTA-17 | TEST-NON-MISURABILE | **RIPARATO** (load-bearing = flip netto **oppure** detection sui semi bersaglio) |
| SOTA-18-v1 (confidenza/astensione) | RIDONDANTE | **RIMOSSO** dal set → scarto S14; contenuto assorbito in SOTA-4(ii') e SOTA-14(iii) |
| — | garanzia mancante | **NUOVO SOTA-18**: registro unico dei semi, non-interazione, de-seeding provato |

**Conteggio**: 18 criteri (15 NECESSARIO, 3 FORTE, 0 DESIDERABILE). Il set non è cresciuto di numero: una riga è
stata rimossa perché ridondante e una nuova è entrata perché copriva un buco che nessun criterio presidiava.
Quattro delle sei garanzie mancanti sono state assorbite dentro criteri esistenti invece di generare righe nuove —
moltiplicare criteri per moltiplicare apparenza di rigore è A10 applicato al set di criteri stesso.

---

# DEFINIZIONI TRASVERSALI (valide per TUTTO il set — l'ambiguità del denominatore era un difetto reale)

**D0 — CELLA.** L'unità di campionamento del set è la **cella = paper × strato**, cardinalità 25 × 3 = **75**.
La RELAZIONE non è una dimensione della griglia: è un **token del vocabolario chiuso** assegnato DENTRO la cella
`{contenuto | minaccia | da-adottare | corregge | NESSUNA-INTERAZIONE | ASTENSIONE-INDETERMINATO | NON-VALUTABILE}`,
con motivazione e classe di oracolo. **Ogni percentuale del set (15%, 20%, 30%, 10%) si riferisce a questa unità**;
qualunque numero espresso su un'altra unità va ri-espresso o dichiarato non confrontabile.

**D1 — BASELINE DI RUMORE `b` (SOTA-16 v').** Riferimento di record dell'apparato, misurato con **ri-esecuzione
IDENTICA** (stesso input, stessa configurazione, hash di configurazione uguale a quello di campagna) su un campione
stratificato di celle. Si pubblica una `b` **per ogni statistica usata a valle**: `b_verdetto` (frazione di celle in
cui cambia il verdetto), `b_span` (distanza di Jaccard media fra gli insiemi di span), `b_livello` (variazione del
livello di certezza). **Nessun criterio del set può contare flip senza sottrarre la `b` omologa e dichiarare il
margine.** Ridurre `b` abbassando la temperatura rispetto alla configurazione di campagna è una deviazione
SOTA-1 e va marcata: nasconde l'effetto invece di misurarlo.

**D2 — GOLD (SOTA-4 iii').** Sottoinsieme di riferimento **pre-registrato prima della campagna** (campione
stratificato, seme dichiarato), aggiudicato da una configurazione **disgiunta** (modello, percorso all'evidenza,
frame) con evidenza completa e contratto default-REFUTE, e **validato** con ≥3 errori seminati che l'aggiudicatore
deve trovare. Se il gold non passa la propria validazione, **è vietato parlare di FP/FN**: si riportano solo tassi
di accordo. Un gold prodotto dallo stesso ceppo che genera i verdetti misura ACCORDO e lo chiama accuratezza (A2).

**D3 — REGISTRO UNICO DEI SEMI (SOTA-18).** Tutti i programmi di seeding del set vivono in un solo registro, con
canale bersaglio dichiarato, test di non-interazione e **prova di rimozione** alla chiusura. Regola unica di
attribuzione: *un seme rilevato da un canale diverso dal bersaglio conta come MISS per il canale bersaglio*.

**D4 — SNAPSHOT DELLA FINESTRA (SOTA-1 vi).** Un unico `snapshot_id` = (commit del programma) + (manifest con hash
di tutti i PDF del corpus) vale per l'intera finestra di campagna ed è citato da ogni cella.

**D5 — ANCORA TEMPORALE.** Ogni asserzione di anteriorità («prima della lettura», «congelato prima del run») è
provata dal **DAG dei commit**, mai da `mtime` di filesystem né da un timestamp scritto dal processo sotto esame.

---

# SEZIONE 1 — I CRITERI (set unificato, deduplicato, riparato)

Ordinamento: prima ciò che deve esistere PRIMA di aprire il primo PDF (SOTA-1..4), poi l'ancoraggio alla fonte
(5..6), poi l'apparato di lettura e di attacco (7..8), poi la copertura e il campionamento (9..10), poi la
sostanza del confronto (11..13), poi la regola di decisione (14), poi i controlli sull'apparato (15..18).

---

## SOTA-1 — Freeze pre-registrato dell'apparato E dell'oggetto sotto test, con ledger delle deviazioni
**Tier: NECESSARIO**
*(fusione: evidence C1 + metascience «Rule-lock» + verification FALS-fase0 + comparison C8-tolleranze;
**esteso in v2** con la garanzia mancante «FREEZE DELL'OGGETTO SOTTO TEST» segnalata dal refuter)*

**Enunciato.** Vocabolario chiuso dei verdetti, regole evidenza→verdetto, soglie, tolleranze, elenco dei claim sotto
test, criteri di arresto e riduzioni di metodo ammesse dal budget esistono come artefatto con hash **ancorato al DAG
dei commit** prima del primo artefatto di estrazione. **E**: il PROGRAMMA (documenti di teoria, oggetti formali,
codice) e il CORPUS (PDF) sono congelati in un unico `snapshot_id` per l'intera finestra di campagna. Ogni
cambiamento successivo — di protocollo, di programma o di corpus — è una deviazione datata, motivata, firmata,
marcata come pre- o post-visione degli esiti, e invalida le celle a monte invece di lasciarle sopravvivere.

**Test misurabile.**
1. **(i')** Anteriorità `t_protocollo < min(t_estrazione)` provata dal DAG dei commit (ancora esterna), **mai da
   `mtime`**; hash ricomputato = hash dichiarato.
2. **(ii')** Diff automatico protocollo↔report sui **SEI campi nominati**: vocabolario dei verdetti; regole
   evidenza→verdetto; soglie; tolleranze; elenco dei claim; criteri di arresto + riduzioni ammesse.
   `n_modifiche_non_loggate` riportato **PER CAMPO** — un solo numero aggregato non è ammesso (un diff che passa sui
   titoli mentre si muovono le tolleranze è il modo standard di superare questo controllo).
3. **(iii')** **Rejector seminato su OGNI campo**, non su uno solo: un campo il cui rejector non spara è un campo
   non coperto e i verdetti che ne dipendono non sono di record.
4. **(iv')** La marcatura pre/post-visione degli esiti è **CALCOLATA dai log di accesso** (post ⟺ `t_deviazione` >
   `t` del primo artefatto di estrazione leggibile dall'agente che devia), non auto-dichiarata; una
   auto-dichiarazione discordante dal calcolo è **essa stessa un finding di record**. `n_deviazioni` e
   `n_deviazioni_post_visione_esiti` pubblicati; il secondo > 0 declassa a NON-DI-RECORD l'intera categoria toccata.
5. **(v)** Riduzioni di metodo imposte dal budget nominate ex ante; `verdetti_toccati_non_marcati = 0`.
6. **(vi) FREEZE DELL'OGGETTO SOTTO TEST**: `snapshot_id` unico citato da ogni cella;
   `n_celle prodotte contro snapshot ≠ dichiarato = 0`; `n_modifiche in finestra non registrate come deviazione = 0`.
   **Test seminato**: modificare in finestra un documento di teoria (o sostituire un PDF con altra edizione) deve
   marcare INVALIDE **esattamente** le celle a monte (aggancio all'impact set di SOTA-16 ii) e imporne la
   ri-esecuzione; se le celle sopravvivono, il freeze non esiste.

**Previene.** HARKing del verdetto; revisione tagliata per budget presentata come completa; **e la deriva
dell'oggetto**: su un programma vivo i due bracci di SOTA-7 possono confrontare testi diversi (il disaccordo diventa
artefatto) e la chirurgia di scopo di A8 non lascia traccia perché nessun confronto è ancorato a una versione unica.
SOTA-16 rileva la staleness DOPO; questo criterio impedisce la deriva DURANTE.

---

## SOTA-2 — Falsificatore pre-registrato per ogni claim, sparabilità PROVATA, qualificazione non-vacua
**Tier: NECESSARIO**
*(fusione: evidence C9 + verification FALS + comparison C3-prima-metà + comparison C11)*

**Enunciato.** Prima della lettura ogni claim deposita enunciato, ipotesi nominate, classe di rigore e la frase
operativa «falsificato se compare X / qualificato se compare Y». Dopo la lettura, un claim che sopravvive solo
restringendo lo scope deve conservare contenuto falsificabile **misurato**, o essere ritirato.

**Test misurabile.**
1. Copertura falsificatori 100%, con commit antecedente alla lettura (ancora DAG, D5).
2. **(ii') PROVA DI SPARABILITÀ su ≥30% dei claim** (seme dichiarato, campione stratificato, ≥1 claim per strato).
   L'abstract ipotetico non è libero: è una **perturbazione minima e nominata** di un abstract reale in-corpus (una
   condizione, un segno, un regime) e deve superare **due filtri disgiunti**:
   **(a) plausibilità aggiudicata** — un agente cieco al claim lo classifica in un test a coppie contro 3 abstract
   reali; se il tasso di riconoscimento del finto supera la soglia pre-dichiarata, il testo non è «fisicamente
   sensato» e non vale come prova;
   **(b) sparo verificabile** — il falsificatore, eseguito **alla lettera** sul testo finto, SPARA in modo
   controllabile a macchina (traccia della condizione X che compare).
   Fallimento di (a) o (b) ⇒ claim etichettato **NON-FALSIFICABILE-DA-QUESTO-CORPUS** e conteggiato.
3. Numero di claim che hanno CAMBIATO STATO: «0 falsificati e 0 qualificati su ~25 primari» è ammesso **solo** se
   SOTA-3 mostra sensibilità 100% sulle classi P0; altrimenti SOSPETTO DI STRUMENTO CIECO e nessun SOPRAVVIVE è
   di record.
4. Riformulazione post-lettura ⇒ **QUALIFICATO-A-POSTERIORI**, mai SOPRAVVIVE.
5. Per ogni SOPRAVVIVE-QUALIFICATO: diff delle ipotesi con la fonte che ha imposto ciascuna; ≥1 configurazione
   dentro lo scope in cui il claim può ancora fallire, col test che lo mostrerebbe; ≥1 testimone non banale DIVERSO
   dall'istanza che ha generato la qualificazione. Si riportano shrinkage medio dello scope e `n_claim a contenuto
   residuo nullo` (che vanno riclassificati FALSIFICATO o RITIRATO).
6. **Confine dichiarato con SOTA-9**: qui si misura la vacuità del **FALSIFICATORE**, in SOTA-9 quella del
   **WITNESS SET**. Un claim che fallisce entrambi **si conta una volta sola** (nessuna doppia contabilità della
   stessa garanzia).

**Previene.** Il claim che sopravvive perché nessuno aveva scritto come sarebbe potuto morire; il salvataggio ad hoc
che lascia a record un claim eroso fino all'invulnerabilità; e — nuovo in v2 — la prova di sparabilità cerimoniale,
soddisfatta con un abstract assurdo che nessun apparato avrebbe potuto scambiare per letteratura.

---

## SOTA-3 — Banco di mutanti stratificato: sensibilità dell'apparato MISURATA per classe di difetto
**Tier: NECESSARIO**
*(consenso 5/5: verification MUT + llm-agent G3 + metascience controlli positivi + evidence C9(ii) + comparison C3)*

**Enunciato.** Prima della campagna si prepara un banco di mutanti plausibili e di piccolo raggio, bilanciato sui tre
strati più il lato corpus; l'orchestrazione gira IN CIECO sul programma/corpus mutato. La domanda a cui risponde è:
**con un numero, che cosa questa orchestrazione è capace di trovare.**

**Test misurabile.**
1. **Semi con ≥5 istanze per classe, posizione ignota agli agenti**:
   TEORICI ≥10 (ipotesi cancellata, classe di rigore promossa THEOREM*→THEOREM, esclusione di scopo rimossa, claim
   sovra-generalizzato); FORMALI ≥10 (segno/fattore/esponente alterato in una condizione di ottimalità o identità, BC
   sostituita con la variante vicina, invariante indebolito); ALGORITMICI ≥10 (gate reso vacuo, tolleranza allentata
   10×, oracolo disattivato); LATO CORPUS ≥5 (quote fabbricata, span corretto ma paper sbagliato, pagina errata,
   paper che contraddice davvero un claim marcato «sopravvive», mistraduzione che inverte una condizione, verdetto
   cross-strato senza ponte); EQUIVALENTI ≥8 (stessa sostanza, notazione/adimensionalizzazione diversa).
2. **WITNESS ATTESO obbligatorio ex ante**: ogni mutante deposita il locus del corpus (o l'oracolo interno) che
   dovrebbe rivelarlo. I mutanti privi di witness atteso vanno nel bucket **NON-RILEVABILE-DA-QUESTO-CORPUS**,
   riportato ma **NON conteggiato** nel `detection_rate`. Motivo: un MISS su un mutante che nessun paper dei 25
   poteva rivelare misura il SILENZIO DEL CORPUS, non la CECITÀ DELL'APPARATO, e punirlo crea pressione ad allentare
   le soglie. Le classi P0 devono avere witness **per costruzione**.
3. **Numeri**: matrice `detection_rate[classe]`; falso-kill rate sugli equivalenti; costo/tempo al rilevamento.
   Attribuzione di canale secondo D3 (rilevazione da canale diverso dal bersaglio = MISS del canale bersaglio).
4. **PASS**: 100% sulle classi P0 (fabbricazione, gate vacuo, ipotesi rimossa). Soglie delle altre classi
   PRE-REGISTRATE CON MOTIVAZIONE, mai importate come default. Ogni mutante sopravvissuto con witness atteso è un
   finding con causa nominata; uno strato sotto soglia = FAIL localizzato non compensabile dagli altri.
5. **Esecuzione realistica**: **iniezione MULTIPLA per run** (k mutanti a posizioni disgiunte dichiarate) invece di
   43+ campagne complete, con **test di non-interazione su ≥20%** (un mutante rilevato in run multipla deve restare
   rilevato a k=1, e viceversa) — il test vive in SOTA-18(ii).
6. **Preventivo in token del banco dichiarato ex ante e a consuntivo.** Se il budget riduce il banco, la riduzione è
   una deviazione SOTA-1(v) **e il tier massimo dei verdetti scende di un grado**: la riduzione silenziosa di questo
   criterio è la forma più probabile di A10 in questa classe di compito.
7. Semi registrati nel **registro unico** (SOTA-18), con canale bersaglio dichiarato e prova di rimozione a fine
   campagna; nessuna classe di seme duplicata fra criteri (la classe «quote fabbricata» è la stessa di SOTA-5 iv ed
   è contata una volta).

**Previene.** Il falso negativo invisibile: un claim falsificabile entra nel paper come «sopravvissuto alla
letteratura» perché nessun canale poteva ucciderlo. Senza banco, «nessun claim falsificato» è indistinguibile da
«nessun claim testato».

---

## SOTA-4 — Controlli negativi, esche, GOLD VALIDATO e contabilità a due lati, con astensione realmente usata
**Tier: NECESSARIO**
*(fusione: metascience controlli negativi + llm-agent G4 + verification MR5 + comparison C10 + evidence tassonomia;
**esteso in v2** con la garanzia mancante «standard di riferimento definito e validato» e con l'unico contenuto
sostantivo del rimosso SOTA-18-v1)*

**Enunciato.** La pipeline deve poter dire «qui non c'è niente» e astenersi; falsi positivi e falsi negativi sono
misurati separatamente perché costano diversamente; e **il metro con cui li si misura è costruito e validato prima,
da una configurazione disgiunta**.

**Test misurabile.**
1. **(i') Esche dimensionate, non asserite.** ESCHE DI ESPOSIZIONE (paper reali fuori-scopo inseriti nel corpus senza
   annuncio) ed ESCHE DI ESITO (claim finti o fuori-programma). `M` e `K` sono **derivati da un target dichiarato**:
   dato `FPR_max` tollerato e confidenza `α`, `M = ⌈ln α / ln(1 − FPR_max)⌉`. Se il budget non consente `M`, si
   pubblica accanto al PASS il **FPR MASSIMO RILEVABILE** con le esche effettivamente usate — mai «FPR = 0» nudo
   (con M=3 un apparato a FPR reale 20% passa nel 51% dei casi: non è un PASS, è un sorteggio).
   `FPR_esche = verdetti forti su esche / esche`, PASS solo a 0 **con la potenza dichiarata accanto**; ogni falso
   allarme obbliga a ri-eseguire la famiglia di celle colpita prima della messa a record. Le esche sono tracciate nel
   registro unico (SOTA-18), **escluse dal denominatore di SOTA-9** e rimosse dal record con prova di de-seeding.
   *(MR5 «non-influenza» di SOTA-15 è questa voce, non una seconda: vive solo qui.)*
2. **(ii') Astensione con soglia, non con aggettivi.** La tassonomia contiene obbligatoriamente NESSUNA-INTERAZIONE,
   ASTENSIONE/INDETERMINATO e NON-VALUTABILE (accesso insufficiente). Si riportano: `abstention_rate` complessivo,
   **per tier di accesso**, e la **correlazione tier↔astensione come numero** (se gli abstract-only si astengono
   quanto i full-text, il tier non sta agendo — incrocio di controllo con SOTA-6). 0 astensioni su un corpus con item
   solo-abstract = FAIL, non completezza. Specularmente: **frazione di celle non-NESSUNA-INTERAZIONE oltre soglia
   pre-dichiarata ⇒ finding aperto con causa nominata** (sostituisce il non-test «è sospetto e va giustificato»).
3. **(iii') GOLD definito PRIMA e validato** (D2): campione stratificato a seme dichiarato, aggiudicato da
   configurazione disgiunta (modello, percorso all'evidenza, frame) con evidenza completa e contratto default-REFUTE,
   `m ≥ 20` verdetti; **qualità del gold misurata con ≥3 errori seminati che l'aggiudicatore deve trovare**.
   Solo se il gold passa la propria validazione si pubblica la matrice di confusione con FP-rate riportato
   separatamente sui verdetti forti; **altrimenti si riportano SOLO tassi di accordo e si vieta il lessico FP/FN**.
   Nessun tasso dichiarato «trascurabile» senza il numero. Questo gold è l'unico ammesso come metro anche per
   SOTA-15 (`shared_error_fraction`) e SOTA-17 (baseline self-consistency).

**Previene.** L'inflazione delle minacce (etichetta forzata su un paper silente); la scomparsa dell'astensione sotto
la pressione a riempire la griglia; e — nuovo in v2 — **il metro fatto dello stesso ceppo**, cioè una matrice di
confusione che misura accordo e lo chiama accuratezza (A2 spostato dal verdetto al metro).

---

## SOTA-5 — Ancoraggio verbatim risolto da un matcher NON-LLM, con VOCE dell'asserzione e catena di condensazione limitata
**Tier: NECESSARIO**
*(consenso 5/5: evidence C4 + llm-agent G1 + verification ATTRIB + metascience span verbatim + comparison C4;
**esteso in v2** con la garanzia mancante «voce dello span e lunghezza della catena di condensazione»)*

**Enunciato.** L'unità di record non è la frase dell'agente ma la coppia **(span, verdetto)**: ogni affermazione
atomica su un paper porta `paper_id`, hash del PDF, pagina, sezione/equazione e stringa verbatim ≤3 righe nella
lingua originale; lo span è ri-trovato da una procedura deterministica indipendente dall'agente che l'ha prodotto;
e porta la **VOCE** dell'asserzione, perché una frase può esistere a quella pagina senza che l'autore la sostenga.

**Test misurabile.**
1. Matcher **non-LLM** (esatto + fuzzy con soglia dichiarata) contro il testo estratto del file identificato
   dall'hash, **alla pagina dichiarata**: `quote_resolution_rate`, `page_accuracy_rate`, `n_locatori_inesistenti`.
   PASS = 1.000 su TUTTE le attribuzioni che sostengono minaccia/adottare/corregge/falsifica; campione ≥30% sulle
   altre; `n_affermazioni senza span = 0` fra le record-grade. Uno span non risolto **BLOCCA** il verdetto a valle,
   non lo degrada a nota.
2. Un solo LOCATOR-NON-TROVATO impone ri-verifica al 100% del batch di quella run, con registrazione dell'evento.
3. `n_verdetti forti privi di almeno una citazione dalla sezione IPOTESI/TEOREMA/METODO = 0`. **Regola dichiarata
   per le fonti OCR prive di marcatura di sezione**: l'attribuzione di sezione avviene per regola di regione di
   pagina dichiarata ex ante, oppure la cella è NON-VALUTABILE — mai per giudizio d'agente implicito.
4. **REJECTOR SEMINATO 3/3**: citazione plausibile ma inesistente; quote reale alterata di tre parole; span verbatim
   corretto ma proveniente da un ALTRO paper del corpus. (Semi nel registro unico, SOTA-18.)
5. Riferimenti che non risolvono e non marcati «non risolvibile» = 0.
6. **(vi) CAMPO VOCE obbligatorio** su ogni span record-grade:
   `{asserito-dagli-autori | attribuito-a-terzi | criticato | ipotetico-poi-rigettato | caso-escluso |
   sintesi-di-letteratura}`, **verificato sul CONTESTO DI PAGINA e non sullo span isolato**.
   `n_verdetti forti sostenuti da span con voce ≠ asserito-dagli-autori e senza argomento esplicito = 0`.
   **Rejector seminato**: uno span reale preso da una tesi che il paper sta CRITICANDO, usato a sostegno di un
   verdetto forte, deve essere intercettato.
7. **(vii) HOP-COUNT dichiarato**: numero di intermediari fra testo primario e verdetto, registrato per ogni verdetto.
   **Nessun verdetto forte è emesso da un agente che non abbia avuto in contesto il testo estratto della PAGINA
   INTERA** da cui proviene lo span: `n_verdetti forti con hop-count > soglia pre-dichiarata o senza pagina intera in
   contesto = 0`. Il condensato a tre righe è esattamente ciò che rende invisibile l'errore di voce.

**Previene.** Le due patologie asimmetriche dell'attribuzione: la citazione fabbricata (rara, vistosa) e soprattutto
la citazione REALE usata per una tesi che il paper non sostiene, che supera ogni controllo di esistenza e muore solo
riaprendo la pagina. Calibrazione dalla letteratura secondaria: tasso base umano di misquote ~17%, ~8% errori maggiori.

---

## SOTA-6 — Gate di ammissione della sorgente (tier di accesso, lingua, estraibilità) che CAPPA la forza del verdetto
**Tier: NECESSARIO**
*(fusione: evidence C5 + llm-agent G2 + verification ATTRIB-tier + metascience accessibilità + comparison C5)*

**Enunciato.** Nessun paper entra senza profilo materiale registrato (hash, pagine, `extractable_text_ratio`, lingua,
tier fra full-text machine-readable / scansione+OCR con qualità misurata / abstract-only / non-reperito) e il tier
limita **per regola scritta prima** la forza massima del verdetto ottenibile; i tag si propagano.

**Test misurabile.**
1. Tabella di ammissione a 25 righe completa; `n_combinazioni tier × verdetto illegali = 0` (nessun
   FALSIFICA/ADOTTARE/CORREGGE/CONTENUTO da abstract-only, da fonte secondaria, o da OCR sotto soglia).
2. **(ii') Qualità OCR misurata senza riferimento LLM** (una trascrizione prodotta dallo stesso apparato che sbaglia
   la lettura è circolare e la soglia passerebbe sempre). Tre indicatori sulle pagine portanti:
   **(a)** `disagreement_rate` carattere-per-carattere fra **DUE motori OCR indipendenti**;
   **(b)** tasso di token fuori-lessico contro dizionario di dominio + tavola dei simboli;
   **(c)** su `k ≥ 3` pagine per documento, riferimento **trascritto a mano** (o a doppio cieco verificato) ⇒
   CER/WER veri sul campione.
   Ammissione al tier full-text solo se le tre misure passano soglie pre-dichiarate.
   **Regioni separate con soglia propria**: testo corrente, **EQUAZIONI**, **TABELLE** — una pagina può avere prosa
   pulita e formule illeggibili, e sono le formule a sostenere i verdetti dello strato formale. Sotto soglia sulle
   regioni-formula ⇒ **tier degradato per i soli verdetti formali/algoritmici**, con propagazione del tag verificata
   a macchina.
3. Traduzioni: 100% dei passaggi portanti con span originale + traduzione + **BACK-CHECK indipendente** da un agente
   che vede SOLO l'originale; `n_divergenze` riportate; `n_simboli tecnici tradotti senza riferimento alla sezione di
   definizione = 0`. (Questo back-check è l'aggancio di MR3 in SOTA-15.)
4. Regola di propagazione a macchina: un verdetto sostenuto solo da fonti taggate porta il tag; violazioni = 0.
   Mai «letto» come evidenza: si elencano le pagine citate.
5. **REJECTOR SEMINATO**: sostituire un PDF con versione a testo non estraibile ⇒ riga NON-AMMESSA e verdetti
   sospesi. Se la pipeline produce comunque una riga piena e fluente, FAIL.
6. `n_paper con tier migliorato dopo tentativo di procurare il full-text` riportato.

**Previene.** Il fallimento letale specifico di questo corpus: su un paper storico scansionato o straniero,
un'estrazione fallita non produce un errore ma **una riga di confrontazione completa generata dalla memoria
parametrica**; e l'erosione dei caveat per cui un abstract del 1979 diventa «evidenza consolidata» contro un teorema.

---

## SOTA-7 — Doppia lettura diversificata, cieca alla direzione dell'esito, con accordo misurato e arbitrato
**Tier: NECESSARIO**
*(fusione: evidence C3 + verification DIFF + metascience doppia estrazione + metascience estrazione cieca alla
direzione + comparison C10)*

**Enunciato.** Ogni **cella** (D0: paper × strato) è prodotta due volte da agenti con contesti disgiunti e diversità
forzata su tre assi — ordine (un braccio legge il paper PRIMA dei documenti del programma), rubrica (uno cerca
contenimento, l'altro minaccia), modello o seme; l'estrattore non contaminato non vede il claim in forma
asserita/orientata.

**Test misurabile.**
1. Check meccanico dei log: il contesto di B non contiene output di A, né il claim orientato, né il verdetto atteso,
   né output a valle; `n_contaminazioni = 0`.
2. **(ii') FLIP-TEST DIREZIONALE con disegno APPAIATO** su ≥15% delle celle (seme registrato). Per ogni cella
   campionata si eseguono, **nella stessa configurazione**, la ri-esecuzione a claim IDENTICO (baseline di rumore
   `b_span`, D1) e quella a claim SPECULARE. **Statistica di record** = distanza di Jaccard media degli span nel
   braccio speculare **MENO `b_span`**, confrontata con un margine pre-dichiarato, con `b_span` **pubblicata
   accanto**. Oltre margine, la messa a record di quella famiglia è sospesa.
   Il **target 0 assoluto sopravvive solo sul cambio del VERDETTO**, non sull'insieme degli span (due run identici
   cambiano già gli span: il target 0 nudo o fallisce sempre o si aggira azzerando la temperatura, che nasconde
   l'effetto invece di misurarlo).
3. **(iii')** Accordo grezzo e κ/α riportati **per strato e categoria**, calcolati sui record **PRE-conciliazione**
   (post-consenso = FAIL). **κ è un numero da pubblicare, MAI un criterio di PASS.** Resta l'unica clausola non
   ambigua: **κ > 0.90 con mutanti di SOTA-3 sopravvissuti = FAIL** (firma di contaminazione, non di qualità).
4. 100% dei disaccordi chiusi da arbitrato documentato (chi, su quale span, con quale motivo);
   `n_divergenze chiuse per media o maggioranza silenziosa = 0`. Il rimedio a un accordo basso è la **definizione**,
   mai il voto.

**Previene.** La perdita sistematica del lettore singolo (~13% di studi rilevanti persi in screening singolo;
l'estrazione singola genera più errori della doppia) e l'estrazione confermativa, in cui l'agente trova nel paper
esattamente ciò di cui il programma ha bisogno.

---

## SOTA-8 — Canale avversariale default-REFUTE per via probatoria disgiunta, con kill-rate calibrato e INTENSITÀ SIMMETRICA
**Tier: NECESSARIO**
*(consenso 5/5: evidence C10 + llm-agent G3 + verification AVV + metascience verifica disgiunta + comparison C9;
**esteso in v2** con la garanzia mancante «simmetria dell'attacco per direzione dell'esito»)*

**Enunciato.** Ogni verdetto di record è attaccato da un agente che parte dal presupposto che sia falso, legge il PDF
primario e non il riassunto del proponente, e i cui errori non sono correlati per costruzione; esito da vocabolario
chiuso `{CONFERMATO, INDEBOLITO + forma qualificata, REFUTATO, NON-VERIFICABILE}`. **E l'attacco è misurato non solo
in esistenza ma in intensità, perché l'incentivo a essere blandi è asimmetrico.**

**Test misurabile.**
1. `n_verdetti il cui verificatore ha visto output o catena di ragionamento del proponente = 0`; run-id distinti;
   ≥1 asse di decorrelazione dichiarato (modello, seme, percorso probatorio).
2. % di loci citati dal refuter NON presenti nelle note del proponente, con soglia dichiarata a priori.
3. Kill/weaken rate e tasso di ribaltamento del giudice riportati, complessivi e per strato. **0% di ribaltamento su
   ≥20 verdetti NON è un PASS**: il canale è **presunto rotto** finché non cattura `k ≥ 3` finding falsi ma
   verosimili seminati (tutti REFUTATI). Se anche uno sopravvive, il canale è DICHIARATO INOPERATIVO e nessun
   verdetto chiude su di esso in quella finestra. (Semi nel registro unico, SOTA-18.)
4. `n_casi in cui un ruolo giudicante valuta materiale prodotto dalla propria configurazione = 0`, oppure deviazione
   dichiarata e caso riverificato da configurazione diversa.
5. **(v) SIMMETRIA DELL'ATTACCO.** Per ogni verdetto si registra l'**intensità**: loci esaminati, angoli d'attacco
   distinti, round, token. Kill/weaken rate e intensità sono **STRATIFICATI per polarità del verdetto**
   (minaccia/corregge/falsifica **vs** contenuto/sopravvive) **e per costo di rilavorazione dichiarato** del
   programma. Soglia di asimmetria **pre-registrata**: oltre soglia si apre un finding e **si ri-esegue la famiglia
   sotto-attaccata**. Senza questa voce un canale può risultare pienamente operativo (uccide i semi) e restare
   sostanzialmente parziale proprio sui verdetti comodi.

**Previene.** Il teatro della verifica: un secondo agente che riceve la finding col ragionamento del primo e ne
controlla la coerenza della prosa, con tasso di conferma quasi-unitario che è artefatto del contratto. L'auto-critica
senza segnale esterno non migliora e spesso degrada.

---

## SOTA-9 — Copertura CENSITA come prodotto cartesiano, bidirezionale, con vacuity check
**Tier: NECESSARIO**
*(consenso 5/5: evidence C8 + llm-agent G5 + verification COP + metascience matrice + comparison C2)*

**Enunciato.** **Direzione A**: griglia di **75 celle** (25 paper × 3 strati, D0), ognuna con un token del
vocabolario CHIUSO più motivazione e classe di oracolo. **Direzione B**: ogni claim del programma ha un
**witness set** — l'insieme delle celle che avrebbero potuto colpirlo — definito PRIMA della lettura.

**Test misurabile.**
0. **(0) Unità unica** (D0): CELLA = paper × strato (75); la RELAZIONE è un token assegnato dentro la cella. Ogni
   percentuale del set si riferisce a questa unità. *(In v1 la stessa parola valeva 300 in un criterio e 75 in altri:
   nessuna soglia percentuale era verificabile.)*
1. **(i')** `fill_rate` = celle con verdetto emesso / 75 = 1.000; `n_token fuori vocabolario = 0`; esiste un
   dizionario che definisce ogni etichetta con un **esemplare reale del corpus**.
2. `claim_touch` = claim con ≥1 tentativo di ricerca registrato / claim totali = 1.000, incluso il risultato negativo
   esplicito.
3. **VACUITY CHECK**: `|witness set| = 0` ⇒ il claim NON può ricevere SOPRAVVIVE ma **NON-TESTATO-DAL-CORPUS**.
   Si riportano `vacuity_rate` ed `evidence_depth` (mediana di `|witness set|` sui sopravvissuti; soglia dichiarata
   ≥2 celle indipendenti per un SOPRAVVIVE di record). *(Confine con SOTA-2: lì la vacuità del falsificatore, qui
   quella del witness set; un claim che fallisce entrambi si conta una volta sola.)*
4. **(iv') TRIPLO REJECTOR della metrica**: svuotare una cella in memoria deve far fallire il contatore; un
   claim-canary estraneo al corpus deve risultare NON-TESTATO; **e una cella riempita con token forte su un
   paper-esca deve essere intercettata** (aggancio esplicito a SOTA-4 i').
5. **(v') Soglie a DUE LATI sulla distribuzione congiunta token × strato**, entrambe pre-dichiarate:
   frazione N/A oltre soglia ⇒ quello strato non è stato realmente confrontato, e va detto;
   **frazione di token FORTI oltre soglia ⇒ sospetto di riempimento** con finding aperto e causa nominata.
   Senza il secondo lato, `fill_rate = 1.000` è pura pressione a riempire e la metrica premia il comportamento che
   SOTA-4 punisce.
6. Le esche di SOTA-4 sono **escluse dal denominatore** e la loro esclusione è verificata a macchina.

**Previene.** Il paper difficile saltato senza traccia (col vuoto letto a valle come «nessuna interazione») e la
**SOPRAVVIVENZA VACUA**, un falso negativo prodotto attivamente dal formato: un claim che nessun paper poteva
toccare esce rafforzato di record.

---

## SOTA-10 — Il corpus è un CAMPIONE a completezza stimata; claim di assenza e di novità query-bounded
**Tier: NECESSARIO**
*(fusione: evidence C2 + verification CORPUS + comparison C6 + llm-agent G6, che fornisce il rejector che deve
RIBALTARE la novità)*

**Enunciato.** I ~25 PDF non sono l'universo della letteratura ma un campione la cui copertura si stima e si riporta
accanto al verdetto globale; nessuna affermazione negativa («nessuno fa X», «questa condizione è nuova») è di record
senza il perimetro che la delimita e la rende falsificabile.

**Test misurabile.**
1. **KNOWN-ITEM TEST**: `k ≥ 5` lavori notoriamente rilevanti, scelti da chi NON costruisce il corpus e tenuti fuori
   dai seed, devono essere ritrovati dalla procedura dichiarata; `recall = trovati/k` riportato, PASS ≥0.80 con ogni
   mancante spiegato. **(vi-a)** Va **nominato l'asse di indipendenza del selettore**: se chi sceglie i known-item
   condivide il prior parametrico degli agenti, il recall misura il richiamo contro quel prior e non contro la
   letteratura, e questo limite si pubblica accanto al numero. **(vi-b)** La soglia 0.80 è importata: va **motivata
   o dichiarata arbitraria** (disciplina S2), mai lasciata implicita.
2. **SNOWBALLING** backward+forward a un livello sul nucleo: i nuovi rilevanti non presenti sono **ELENCATI
   NOMINALMENTE**, non solo contati; resa non trascurabile ⇒ corpus non chiuso e ogni verdetto di ASSENZA declassato.
3. Per ogni claim di assenza/novità: record di ricerca (≥1 query, timestamp, fonte, hit, screenati), copertura 1.00.
   **REJECTOR**: iniettare nel perimetro un paper noto-positivo (o rimuoverne uno e ri-eseguire) — il claim di novità
   **DEVE ribaltarsi o qualificarsi**; la frazione di claim ribaltabili è riportata (una novità irribaltabile è
   ancorata alla memoria parametrica, non al perimetro).
4. Ogni esclusione (lingua, abstract-only, paywall, epoca) registrata come GAP con owner e trigger; esclusioni non
   registrate = 0; check aritmetico `{paper citati} \ {inclusi} = ∅`.
5. Estensione FORTE **non-gate**: capture-recapture con due routine a percorsi **materialmente diversi**, stima
   riportata con l'ipotesi di indipendenza dichiarata dubbia.

**Previene.** Il falso negativo di massa, il più costoso della classe: «il programma sopravvive alla letteratura»
perché la letteratura che lo avrebbe ucciso non era nella cartella — e la frase finisce in un paper, esposta al
revisore che quel lavoro lo conosce.

---

## SOTA-11 — Corrispondenza TIPATA e relazione esplicita fra insiemi di ipotesi
**Tier: NECESSARIO**
*(fusione: comparison C1 + evidence C6-indirectness + metascience allineamento)*

**Enunciato.** Ogni cella non nulla porta una scheda a campi obbligatori: ipotesi del paper con pagina; ipotesi del
claim con documento e versione; mappa simbolo→simbolo con unità, normalizzazioni, adimensionalizzazioni e convenzioni
di segno (ogni simbolo con la pagina della sua definizione); relazione `H_paper` vs `H_programma` in
`{sottoinsieme, sovrainsieme, disgiunte, incomparabili}` col regime di intersezione; per lo strato algoritmico, la
natura del confronto in `{formulazione, metodo numerico, risultato numerico}`.

**Test misurabile.**
1. `n_record con campo mancante = 0`; `n_simboli usati nel verdetto e assenti dalla mappa = 0`; check automatico di
   coerenza dimensionale, `n_incoerenze non spiegate = 0`.
2. `n_record con intersezione VUOTA etichettati MINACCIA o CONTENUTO senza argomento esplicito che attacchi
   l'esclusione di scopo = 0`; `n_celle algoritmiche senza qualifica di natura = 0`.
3. **(iii') TEST DI SOSTITUZIONE CIECA reso misurabile.** La scheda dichiara ex ante `k ≥ 5` **ATTRIBUTI
   DISCRIMINANTI** dell'oggetto: tipo dell'oggetto matematico; argomenti e loro dominio; unità/adimensionalizzazione;
   convenzione di segno; condizione al contorno o vincolo attivo. Un secondo agente, cieco alla prosa e vedendo SOLO
   la scheda, **ricostruisce i k attributi**; il punteggio è **attributo-per-attributo**, con match esatto o entro
   un'equivalenza dichiarata, **verificato per confronto di stringhe/unità e non per giudizio**.
   Soglia: **TUTTI gli attributi P0 (tipo, argomenti, segno) corretti**; gli altri sopra soglia pre-dichiarata con
   motivazione. Fallimento ⇒ la cella non è record-grade finché la scheda non è riscritta, e la riscrittura è una
   deviazione datata (SOTA-1).
   *(La versione v1 chiedeva un «tasso di ricostruzione» giudicato su prosa: era un oracolo di classe J, vietato ai
   verdetti di record da SOTA-12(v) — il test più potente del criterio era anche il suo unico non misurabile.)*
4. **(iv')** Un revisore indipendente ri-assegna la relazione fra insiemi di ipotesi su ≥15 celle; accordo calcolato
   **appaiato sulle STESSE celle**, target ≥0.80 con la soglia **motivata o dichiarata arbitraria**.

**Previene.** L'**ISOMORFISMO NARRATIVO** — dichiarare contenimento o minaccia perché due costruzioni dicono
«funzionale», «entropia», «ottimalità» mentre gli oggetti hanno tipo, argomenti, normalizzazione o segno diversi:
è il modo n.1 in cui un confronto teoria-vs-corpus genera insieme falsi positivi (accordo apparente) e falsi negativi
(conflitto mascherato dalla notazione). Blocca anche il falso positivo di adozione, la via più rapida per corrompere
lo strato formale.

---

## SOTA-12 — Testimone ESEGUITO: riduzioni calcolate e confronto numerico con tolleranza derivata e congelata
**Tier: FORTE**
*(fusione: comparison C2-testimoni + comparison C8 + verification ORACOLO — 2/5 lenti: ammesso sul merito del test,
non sulla popolarità)*

**Enunciato.** Un CONTENUTO o una RIDUZIONE-SOTTO-H non si dichiara, si **calcola**; e dove il corpus offre numeri,
benchmark, casi risolti o figure dentro lo scope, il confronto **si esegue** con la pipeline, con tolleranza derivata
e congelata prima del run.

**Test misurabile.**
1. Ogni CONTENUTO/RIDUCE-SOTTO-H esibisce `H` non vuota + **degenerazione ESEGUITA** (sostituzione di parametri,
   passaggio al limite, specializzazione di classe) con derivazione a passi controllabili o run nel regime degenerato
   entro tolleranza: `(riduzioni con testimone eseguito)/(riduzioni) = 1`.
2. Le degenerazioni FALLITE si registrano e si classificano (limite singolare, non-uniformità). Numeri:
   `n_limiti singolari scoperti`, `n_ipotesi aggiunte per far tornare una riduzione`.
3. **(iii') Il denominatore `E` esce dalle mani di chi ne beneficia.** `E` = paper con quantità riproducibili nello
   scope, determinato in un **passo SEPARATO e ANTECEDENTE** al confronto, eseguito da un agente **che non emette
   verdetti**, con definizione operativa pre-registrata (il paper contiene tabella, figura leggibile o forma chiusa
   con valori numerici in un regime che la pipeline sa istanziare) e con **default AMMISSIBILE**: ogni esclusione da
   `E` è una riga con motivo, pagina e owner ed è **sottoposta al canale default-REFUTE di SOTA-8** (l'esclusione è
   un verdetto attaccabile, non un'omissione). Si riportano `|E|`, tentati, riprodotti, falliti,
   `n_esclusioni_ribaltate` dall'attacco. **`E = 0` su ~25 primari è esso stesso un finding** con giustificazione
   scritta e firma; `E > 0` con `tentati = 0` ⇒ FAIL.
   *(In v1 `E` era auto-dichiarato dagli stessi agenti che dovevano riprodurre: «E>0 con tentati=0 ⇒ FAIL» si
   aggirava dichiarando `E=0` con una frase sullo scopo — la chirurgia di scopo di A8 spostata sul denominatore.)*
4. Ogni tolleranza ha **derivazione scritta e congelata prima del run**, con anteriorità ancorata al DAG dei commit
   (D5); **l'artefatto congelato è la derivazione, non solo il valore**; almeno un confronto per paper riproducibile
   passa da un gate che può RIGETTARE.
5. `ORACLE_CLASS` obbligatoria in `{T testuale-localizzato, D derivato, P pseudo-oracolo, M metamorfico,
   J giudizio d'agente, U indecidibile-a-questo-budget}`: `n_verdetti J promossi a record = 0`; classe in
   `{T,D,P,M}` al 100% per FALSIFICA/ADOTTARE/CORREGGE; tasso di `U` > 0 atteso (un tasso nullo è sospetto).

**Previene.** La «riduzione ovvia» mai calcolata (si assume che annullando un parametro la teoria generale restituisca
la classica, mentre il limite è singolare e la relazione vera è coesistenza a regimi disgiunti); il confronto
puramente testuale con una letteratura che offriva un test numerico decisivo; e la tolleranza gonfiata a posteriori,
il falso positivo più difficile da smascherare perché si presenta come evidenza quantitativa.

---

## SOTA-13 — Disciplina di strato: verdetti tipati, nessun riciclo di locator, ponte nominato per il cross-strato
**Tier: NECESSARIO**
*(fusione: llm-agent G10 + comparison C7 + metascience campo-ponte)*

**Enunciato.** Ogni finding porta **due timbri distinti** — lo strato in cui vive l'EVIDENZA e lo strato in cui è
formulato il CLAIM; un'inferenza cross-strato è legale solo tramite un **ponte NOMINATO** (quale ipotesi del teorema
è consumata da quale oggetto formale e da quale passo della pipeline), a sua volta verificabile.

**Test misurabile.**
1. `n_finding con claim-layer ≠ evidence-layer e senza ponte nominato = 0` (check meccanico su due campi).
2. **AUDIT DI RIUSO DEL LOCATOR**: `n_entry multi-strato che condividono lo stesso span sorgente senza
   giustificazione esplicita di implicazione inter-strato = 0` (numero riportato, non solo il PASS).
3. Per ogni claim, catena a 3 strati completa (quale teorema, quale oggetto formale lo incarna, quale carrier
   eseguibile può rigettarlo), con % di catene complete e **LISTA NOMINALE** degli incompleti.
4. `n_verdetti che trasferiscono una garanzia teorica allo strato algoritmico senza ponte = 0`.
5. **DUE REJECTOR SEMINATI**: un finding in cui un accordo numerico è presentato come conferma di un teorema; e un
   paper che minaccia solo lo strato formale (non devono comparire righe piene sugli altri due).
   **I due semi vivono nel registro unico (SOTA-18) con canale bersaglio dichiarato**, altrimenti interagiscono con i
   mutanti di strato di SOTA-3 e le due `detection_rate` si contaminano.

**Previene.** L'inflazione dei findings (una lettura moltiplicata in tre voci che sembrano tre evidenze indipendenti)
e il suo speculare, la minaccia teorica reale mai tradotta in un test che la pipeline possa fallire — quindi
ornamentale; più il caso «il codice implementa la teoria» senza l'oggetto formale intermedio, per cui una correzione
teorica non tocca mai la pipeline.

---

## SOTA-14 — Barra probatoria ASIMMETRICA per grado di verdetto, con azione autorizzata e owner
**Tier: NECESSARIO**
*(fusione: evidence C7 + evidence C11 + verification GRADI + metascience barra asimmetrica + comparison C10;
**assorbe in v2** la garanzia sostantiva del rimosso SOTA-18-v1 sulla confidenza)*

**Enunciato.** Esiste ex ante una tabella **grado-di-verdetto → pacchetto di evidenza minimo** e una tabella
**(certezza × strato × classe di costo) → azione massima consentita** in `{registrare, sorvegliare, qualificare il
claim, adottare nel programma, dichiarare falsificato}`: il rigore speso è proporzionale al danno del verdetto
sbagliato, e le soglie di «adotta» e «falsifica» sono diverse e motivate dal costo d'errore.

**Test misurabile.**
1. Contratto auditabile, es.: NESSUNA-INTERAZIONE = 1 lettura + motivazione; MINACCIA = 2 letture diversificate +
   oracolo T/D + sopravvivenza al refuter; ADOTTARE/CORREGGE/FALSIFICATO = 2 letture diversificate + oracolo T|D|P su
   fonte PRIMARIA full-text + sopravvivenza a refuter default-refute + ri-derivazione o controesempio esplicito +
   firma di un giudice cieco all'identità dei bracci.
2. Audit su tutti i verdetti forti e ≥20% degli altri; `compliance = 1.00`; ogni non conforme è **DEMOTO
   automaticamente** al grado che il suo pacchetto sostiene e il `grade_inflation_rate` (n. demozioni) è pubblicato.
3. **(iii')** Il livello di certezza è un **calcolo**: livello + lista dei domini che l'hanno mosso; un agente
   indipendente che vede SOLO i giudizi di dominio **ri-deriva** il livello. Concordanza riportata, target ≥0.90,
   calcolata **appaiata (stesso caso, configurazione diversa)** e con la soglia **motivata o dichiarata arbitraria**.
   `n_verdetti con livello ma senza traccia di dominio = 0`. **Nessuna confidenza è pubblicata senza domini nominati e
   senza ri-derivazione indipendente** — questa clausola sostituisce integralmente il criterio di calibrazione
   rimosso (S14): è più forte perché non è statistica e non dipende da un N che non abbiamo.
4. Ogni verdetto porta l'azione conseguente **CON PROPRIETARIO**, incluso l'esplicito «nulla cambia perché…»;
   `verdetti senza azione = 0`.
5. **SOPRAVVIVE non può essere emesso per assenza di attacco**: richiede un attacco eseguito e documentato che sia
   fallito (aggancio a SOTA-8, incluso il test di intensità simmetrica).
6. Test duale contro il conservatorismo: se `ADOTTARE = CORREGGE = 0` su ~25 primari, va verificato che non sia
   effetto di soglia e la giustificazione va scritta.

**Previene.** Riscrivere il programma per una minaccia a certezza molto bassa; archiviare come «da approfondire» una
minaccia ad alta certezza; l'hedging universale che scarica sul lettore la decisione che la confrontazione doveva
prendere; e la sopravvivenza per default.

---

## SOTA-15 — Invarianza ai fattori senza contenuto e indipendenza degli errori MISURATA
**Tier: FORTE**
*(fusione ampia: verification META (MR1-MR6) + llm-agent G7 bias-giudice + llm-agent G8 correlazione-errori +
metascience invarianza/replica + comparison C9(iv))*

**Enunciato.** Il verdetto deve essere una proprietà dell'evidenza, non dell'ordine di presentazione, del lessico,
della lingua, della lunghezza dell'argomento o della parentela col giudice; e se più agenti concorrono, il peso
dell'accordo è funzione del numero di **combinazioni realmente distinte**, non del numero di agenti.

**Test misurabile.**
1. **DISEGNO APPAIATO OBBLIGATORIO.** Per ogni cella campionata (unità D0, ≥20%, seme dichiarato) si esegue la
   **ri-esecuzione IDENTICA** accanto a ogni relazione metamorfica; la **statistica di record è
   `flip_rate(MR) − b`** (D1, `b` da SOTA-16 v'), confrontata con un margine pre-dichiarato, con `b` **pubblicata**.
   Senza appaiamento non si distingue «il verdetto dipende dalla lingua» da «l'apparato non è deterministico».
2. **MR1** parafrasi / **MR2** notazione e unità / **MR3** lingua (obbligatoria sui paper stranieri, **agganciata al
   back-check di SOTA-6(iii)**) ⇒ stesso verdetto.
   **MR4** monotonia di scopo: indebolire le ipotesi non può trasformare FALSIFICATO in SOPRAVVIVE; restringere lo
   scopo non può trasformare SOPRAVVIVE in FALSIFICATO.
   **MR6** permutazione dell'ordine paper/claim e scambio «programma primo»/«paper primo», con `flip_rate` netto
   riportato; ogni flip oltre margine apre un finding e sospende la messa a record di quella cella.
   **MR5 «non-influenza» è RIMOSSA da qui**: era letteralmente l'esca di esposizione di SOTA-4(i) e contarla due
   volte è inflazione di rigore. Vive solo in SOTA-4(i') ed è qui **citata come dipendenza**.
3. **BIAS DEL GIUDICE**: inversione dell'ordine su un **campione a seme e potenza dichiarati** (non «TUTTE le coppie»
   senza preventivo, che è la voce che verrebbe tagliata per prima e in silenzio), con `order_flip_rate` netto;
   correlazione lunghezza-argomento/vittoria riportata come numero e, oltre soglia, ri-esecuzione con argomenti
   normalizzati; frazione di aggiudicazioni su materiale della stessa configurazione, target 0.
4. **INDIPENDENZA**: tripla (modello, percorso all'evidenza, frame) per ogni votante e `n_indipendenti`;
   `shared_error_fraction` **calcolata solo se esiste il gold validato di SOTA-4(iii')**; altrimenti si riporta la
   correlazione degli errori RILEVATI dai semi di SOTA-3, **dichiarando esplicitamente la sostituzione**.
   ABLAZIONE DI CONTAGIO con premessa falsa nel contesto condiviso e `propagation_rate`.
5. **REPLICA**: un auditor indipendente rifà da zero `K ≥ 5` confrontazioni (seme dichiarato), pubblicando accanto al
   verdetto concordanza di etichetta e sovrapposizione degli span.
6. **PREVENTIVO in token del criterio riportato ex ante e a consuntivo**, agganciato a SOTA-17. È il criterio più
   caro del set ed è solo FORTE: senza preventivo dichiarato sarebbe il primo a essere tagliato in silenzio (A10).

**Previene.** Il consenso di confabulazione (N agenti dello stesso ceppo, stesso contesto, stesso abbaglio, contati
come N osservazioni), la soppressione della minoranza corretta, e i verdetti decisi da variabili prive di contenuto
epistemico che però producono output perfettamente motivati.

---

## SOTA-16 — Provenienza risolvibile, chiave di record immutabile, staleness armato, e BASELINE DI RUMORE APPAIATA
**Tier: NECESSARIO**
*(consenso 5/5: evidence C12 + llm-agent G9 + verification PROV/STALE + metascience record immutabile + comparison C12;
**esteso in v2**: la voce (v) diventa la garanzia mancante «baseline di rumore appaiata», riferimento di record del set)*

**Enunciato.** Ogni verdetto di record risolve tre catene (corpus: `paper_id → file con hash → locator`; programma:
`claim_id → documento/teorema` o `commit+file+range` con identità del codice al momento del giudizio; processo:
run id, hash del prompt, modello+configurazione, data, tier) e porta una chiave; il cambiamento di una componente lo
**invalida** invece di lasciarlo sopravvivere per inerzia. **E l'apparato che produce quei verdetti dichiara il
proprio rumore, misurato in modo appaiato.**

**Test misurabile.**
1. Camminatore automatico su campione `N ≥ 15` con seme dichiarato: `broken_link_rate = 0` (file assente, hash
   diverso, range inesistente, sezione rinominata = FAIL); per lo strato algoritmico frazione con check ri-eseguibile
   = 1.00, con **ri-esecuzione effettiva**, exit code e output byte-confrontato.
2. **IMPACT SET** (claim/artefatto → verdetti che lo citano; paper → verdetti che ne dipendono) con **TEST SEMINATO
   obbligatorio**: mutare un claim in memoria o sostituire un PDF con altra edizione deve far segnalare ESATTAMENTE
   l'insieme atteso, `precision = recall = 1.00` su `k ≥ 5` mutazioni. Se il rilevatore non spara sul proprio seme,
   canale rotto. *(È lo stesso meccanismo che SOTA-1(vi) usa per invalidare le celle in caso di rottura del freeze.)*
3. Alla chiusura: `n_verdetti con chiave memorizzata ≠ ricalcolata = 0`; `n_verdetti stale non marcati = 0`;
   `n_modifiche in-place di un verdetto di record = 0` (si sostituisce solo con un nuovo record che cita il
   superato); «resume non relaunch» legittimo solo a firma degli input invariata, controllato a macchina.
4. Trigger di aggiornamento con owner e finestra; marcatura STALE a macchina; `n_verdetti STALE alla data della
   citazione nel paper` riportato.
5. **(v') BASELINE DI RUMORE APPAIATA — riferimento di record dell'intero set** (D1). Ri-esecuzione **IDENTICA**
   (stesso input, **hash di configurazione uguale a quello di campagna**, seme dichiarato) su ≥10% delle celle
   stratificate. Si pubblicano `b_verdetto`, `b_span`, `b_livello` con intervallo (bootstrap sul campione).
   Questa `b` **È DICHIARATA riferimento** di SOTA-7(ii'), SOTA-15(1) e SOTA-17(a): nessun criterio del set conta
   flip senza sottrarla. `verdict_stability` è riportata ma **MAI usata come PASS** (un apparato perfettamente
   stabile e perfettamente sbagliato la supererebbe); ogni flip resta un finding sull'apparato.
   `b` oltre soglia pre-dichiarata = finding: l'apparato è troppo rumoroso per verdetti di record in quella famiglia.
   Ridurre `b` cambiando temperatura/configurazione rispetto alla campagna è una deviazione SOTA-1 e va marcata.
   *(In v1 questa misura esisteva ma era un numero orfano: non appaiata e non dichiarata riferimento di nessuno.)*

**Previene.** Il verdetto orfano (vero forse ieri, non ricostruibile oggi, quindi non citabile); il carry-over
silenzioso (il programma evolve, la confrontazione resta ferma, e un verdetto calcolato contro una versione morta
continua a essere citato come vivo); e — nuovo in v2 — l'intera famiglia di finding aperti sul rumore e di componenti
giustificati dal rumore.

---

## SOTA-17 — Peso dell'orchestrazione giustificato dai FLIP **o** dalla potenza sui semi: nessun round rituale
**Tier: FORTE**
*(origine unica: llm-agent-systems G12; ammesso perché il budget di token finito è un vincolo dichiarato della classe
e perché è l'unico criterio che protegge dal fallimento «apparato enorme, potere di rigetto nullo»)*

**Enunciato.** Ogni componente dell'orchestrazione (round di dibattito, agente aggiuntivo, passata di giudice) è
**LOAD-BEARING**: si dimostra che ha cambiato almeno un verdetto **oppure** che uccide difetti seminati che nessun
altro canale uccide. Altrimenti è rimosso, e la classe di difetto che resta scoperta è nominata.

**Test misurabile.**
1. **Regola di record**: un componente è LOAD-BEARING se soddisfa **(a) OPPURE (b)**:
   **(a)** `verdict_flip_count` **al netto della baseline di rumore appaiata** (D1) > 0 sul corpus reale;
   **(b)** `detection_rate > 0` sui semi che lo hanno come **canale bersaglio** nel registro unico (SOTA-18).
   **È rimovibile solo un componente con (a) = 0 E (b) = 0.**
   *(La regola v1 — «flip_count = 0 ⇒ rimosso» — era logicamente rovesciata rispetto al costo d'errore asimmetrico
   della classe: su ~25 paper il canale che intercetta il caso fatale 1-su-30 mostra 0 flip e verrebbe rimosso
   esattamente prima della finestra in cui serve.)*
2. Un componente con **(b) > 0 e (a) = 0 è CONSERVATO e dichiarato controllo**, pubblicando la sua **potenza**
   (quanti semi di quale classe uccide, a che costo). L'etichetta «controllo» non è più una scelta retorica ma il
   risultato di un numero — in v1 era discrezionale, e quindi qualunque componente poteva sopravvivere con
   un'etichetta e qualunque componente scomodo poteva cadere con un numero.
3. Per ogni **rimozione** si nomina la **CLASSE DI DIFETTO che resta scoperta** e chi la copre (owner).
4. Il peso dell'orchestrazione (agenti, round, effort, token) è riportato **accanto al verdetto**.
5. Estensione desiderabile, sul **solo gold subset** e **solo se esiste il gold validato di SOTA-4(iii')**: confronto
   a parità di budget con la baseline «campionamento ripetuto della configurazione più forte» (self-consistency).
   La configurazione adottata deve batterla o pareggiare con motivo dichiarato.

**Previene.** Il rigore per volume — agenti e round aggiunti perché «più agenti sembra più serio», bruciando un
budget dichiaratamente finito senza spostare un verdetto, mentre la sensazione di rigore scoraggia i controlli veri —
e il caso opposto, eliminare il canale avversariale per risparmio senza mai misurare cosa avrebbe trovato.

---

## SOTA-18 — Registro unico dei semi, non-interazione misurata, DE-SEEDING PROVATO del record
**Tier: NECESSARIO**
*(criterio NUOVO in v2; origine: garanzia mancante n.4 del refuter — «igiene e de-seeding dei semi». Sostituisce nel
numero il criterio di calibrazione della confidenza, rimosso perché ridondante → S14)*

**Enunciato.** Il set ordina **nove programmi di seeding** (SOTA-1 deviazioni; SOTA-3 mutanti; SOTA-4 esche ed errori
del gold; SOTA-5 citazioni; SOTA-6 PDF illeggibile; SOTA-8 finding falsi; SOTA-9 cella svuotata e claim-canary;
SOTA-13 rejector di strato; SOTA-16 mutazioni d'impatto). Vivono in **UN registro** con canale bersaglio, esito
atteso e finestra; interagiscono fra loro se coesistono; e **nessun record chiude senza la prova che siano stati
rimossi**. Un record di cui non si può dimostrare la purezza non è citabile in un paper.

**Test misurabile.**
1. Registro unico versionato e **ancorato al DAG** (D5): ogni riga con `(id, classe, canale bersaglio, locus, esito
   atteso, run in cui vive, stato)`; `n_semi non registrati scoperti a posteriori = 0`.
2. **NON-INTERAZIONE**: su un campione ≥20% dei semi coesistenti, ri-esecuzione **a k=1** (seme isolato): un seme
   rilevato in run multipla deve restare rilevato isolato, e viceversa. `n_interazioni non dichiarate = 0`; ogni
   interazione trovata degrada la `detection_rate` delle classi coinvolte a **NON-INTERPRETABILE** finché non si
   ri-esegue isolati. *(È il test che rende eseguibile l'iniezione multipla di SOTA-3(5) senza 43 campagne complete.)*
3. **ATTRIBUZIONE DI CANALE (regola unica del set, D3)**: un seme rilevato da un canale diverso dal bersaglio conta
   come **MISS per il canale bersaglio**. Elimina il doppio conteggio della stessa garanzia fra SOTA-3/5/9/13/16 e
   impedisce che un canale si prenda il merito della sensibilità di un altro.
4. **DE-SEEDING GATE alla chiusura**: il record finale è **ricalcolato contro il registro** e si dichiara
   `n_semi_residui = 0` — nessuna esca nel corpus di record, nessun mutante nel programma, nessun claim finto,
   nessun finding falso sopravvissuto, nessuna cella con esca a denominatore — **con firma e hash del record
   post-rimozione**. Ogni seme non recuperato è un P0 bloccante: il record resta NON-CITABILE.
5. **REJECTOR DEL GATE**: si lascia deliberatamente un seme in un record di prova; il gate **DEVE** fallire. Se non
   fallisce, la prova di purezza non esiste e nessun verdetto è di record in quella finestra.
6. Numeri pubblicati: `n_semi` per classe e per canale; `n_semi_residui`; `n_semi interagenti`; costo del seeding in
   token (voce del preventivo di SOTA-17).

**Previene.** Il fallimento che nessun altro criterio del set presidiava: **il record che viene citato nel paper
contiene ancora i propri semi** — un'esca contata come paper, un mutante letto come teoria, un finding falso
sopravvissuto al refuter — oppure due `detection_rate` contaminate da semi che si mascherano a vicenda, con la
sensibilità dell'apparato sovrastimata proprio dove è stata «misurata».

---

## Riepilogo tier

| Tier | Criteri | N |
|---|---|---|
| NECESSARIO | SOTA-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 18 | 15 |
| FORTE | SOTA-12, 15, 17 | 3 |
| DESIDERABILE | — (nessuno: l'unico criterio DESIDERABILE di v1 è stato rimosso, non declassato) | 0 |

**Nota sul costo.** Il set è caro: il banco mutanti (SOTA-3), la doppia lettura diversificata (SOTA-7), il testimone
eseguito (SOTA-12), la famiglia di invarianze (SOTA-15) e la baseline appaiata (SOTA-16 v') valgono da soli la
maggior parte del budget. Il costo NON è un argomento per rimuoverli, ma è un argomento per SOTA-17: si taglia dove
`(a) = 0 E (b) = 0`, non dove il potere diagnostico è alto. **Novità v2**: SOTA-3(6) e SOTA-15(6) portano un
**preventivo in token dichiarato ex ante e a consuntivo**, e la riduzione del banco mutanti abbassa di un grado il
tier massimo dei verdetti. Il taglio ammesso è quello dichiarato ex ante in SOTA-1 che marca i verdetti toccati;
qualunque altro taglio è una deviazione non registrata.

---

# SEZIONE 2 — ANTIPATTERN (set unificato, 10)

**A1 — VERIFICA CHE NON PUÒ FALLIRE.**
Il verificatore riceve la finding **insieme** al ragionamento del proponente e ne controlla la coerenza interna;
domande formulate come conferma («in che modo il paper X si integra con il programma?»); refuter senza mandato di
rigetto; nessun seme iniettato. Il tasso di conferma prossimo al 100% viene letto come robustezza mentre è un
artefatto del contratto. **Variante asimmetrica** (v2): il canale che uccide i semi ma resta blando proprio sui
verdetti la cui caduta imporrebbe rilavorazione costosa — formalmente operativo, sostanzialmente parziale.
**Regola**: un verificatore senza `detection_rate` misurato su difetti seminati non è un verificatore, è un secondo
generatore che scrive «confermo». Se non esiste un esito osservabile in cui la confrontazione avrebbe detto «il
programma è cieco qui», non è stata eseguita una verifica: è stata scritta una relazione. *(unanime 5/5)*

**A2 — CONSENSO CORRELATO SPACCIATO PER REPLICAZIONE; E IL METRO FATTO DELLO STESSO CEPPO.**
N agenti dello stesso modello, stesso prompt, stesso ordine, o peggio a partire dallo stesso estratto intermedio:
è UNA osservazione replicata, non N osservazioni. Vale anche per κ altissimi — su un corpus non banale un accordo
quasi perfetto è segnale di contaminazione del contesto, non di qualità. **Forma peggiore, aggiunta in v2**: lo
stesso vizio spostato **dal verdetto al metro** — un gold subset prodotto dalla stessa famiglia di agenti rende la
matrice di confusione una misura di ACCORDO che viene chiamata accuratezza, e su di essa poggiano poi FP-rate,
`shared_error_fraction` e calibrazione. Varianti: self-consistency spacciata per replicazione indipendente; voto di
maggioranza usato come definizione di verità; soppressione della minoranza corretta. Aggiungere agenti a un errore
condiviso ne aumenta solo la confidenza dichiarata. *(unanime 5/5)*

**A3 — COPERTURA DICHIARATA E NON CENSITA; SOPRAVVIVENZA VACUA.**
«Tutti i 25 paper esaminati su tutti e tre gli strati» senza matrice cella-per-cella, vocabolario chiuso, fill rate e
un contatore che possa fallire su una cella svuotata. I paper difficili producono le righe più povere — o, peggio,
righe fluenti generate dalla memoria parametrica — e nulla lo rileva perché nessuna cella è formalmente vuota.
Gemella: la direzione inversa mai eseguita, per cui un claim che **nessun paper del corpus poteva toccare** esce
rafforzato come «sopravvive alla letteratura». Corollario v2: un `fill_rate = 1.000` **senza tetto misurato sulla
frazione di token forti** non è copertura, è pressione a riempire. *(unanime 5/5)*

**A4 — ATTRIBUZIONE SENZA LOCALIZZAZIONE, E SENZA VOCE.**
«Il paper X mostra Y» senza quote verbatim, pagina, edizione e hash. Il controllo di ESISTENZA (DOI, titolo, anno,
autori giusti) non intercetta nulla di tutto questo. Il caso peggiore non è la citazione inventata ma il **paper reale
citato per una tesi che non contiene**; varianti: lo span appartiene a un ALTRO paper del corpus; è la frase di un
lavoro che l'autore stava CRITICANDO; è un'ipotesi poi rigettata o un caso limite escluso; il claim è estratto da
abstract/introduzione/conclusioni invece che dalla sezione ipotesi/teorema/metodo; è citato di seconda mano.
**Aggravante di catena** (v2): il giudice decide su tre righe di span estratte da altri — il condensato rende
invisibile proprio l'errore di voce, che sopravvive a qualunque matcher. Correlato: presentare come «letto» un lavoro
di cui si è visto solo l'abstract, e perdere il tag lungo la catena. *(unanime 5/5)*

**A5 — ASSENZA DI EVIDENZA COME EVIDENZA DI ASSENZA.**
«Nessuno in letteratura fa questo», «il claim è nuovo», «nessun paper contraddice» — partendo dai PDF già sul disco,
senza perimetro registrato, senza known-item test, senza citation chasing. È il falso negativo più costoso della
classe perché diventa un claim di novità in un paper, esposto al revisore che conosce il lavoro fuori dal corpus.
*(4/5)*

**A6 — ISOMORFISMO NARRATIVO.**
Contenimento, minaccia o novità dedotti dalla somiglianza del lessico (stesso nome di funzionale, stessa parola
«ottimalità», stessa figura qualitativa) senza mappa tipata fra gli oggetti. Sintomo diagnostico: il rapporto abbonda
di «analogo a», «nello spirito di», «coerente con» e non contiene una sola sostituzione di variabili con unità.
Sotto-caso: la «riduzione ovvia» mai calcolata, dove il limite è in realtà singolare e la relazione vera è
coesistenza a regimi disgiunti. *(comparison, con supporto da evidence e metascience)*

**A7 — LAYER LAUNDERING.**
Un accordo numerico presentato come conferma di un teorema (può nascere da errori compensativi o da una classe di test
troppo stretta); una minaccia teorica trasferita alla pipeline senza ponte nominato; «il codice implementa la teoria»
senza l'oggetto formale intermedio. Effetto collaterale: una singola lettura moltiplicata in tre findings che sembrano
tre evidenze indipendenti. *(llm-agent, comparison, metascience)*

**A8 — CHIRURGIA DI SCOPO E HARKING SUL CORPUS — INCLUSA LA CHIRURGIA SUL DENOMINATORE.**
Leggere i paper, poi restringere ipotesi/scopo finché il claim combacia, e registrarlo come SOPRAVVIVE invece che
QUALIFICATO-A-POSTERIORI; spostare una minaccia scomoda in «fuori scopo» invocando un'esclusione che nel documento
teorico non esisteva prima; derivare la tolleranza numerica dopo aver visto il disaccordo. Variante gemella: lo
**steel-man implicito**, in cui l'agente confronta il paper con la versione interpretata/migliorata del claim,
aggiungendo al volo un'ipotesi che nessun documento contiene, e il programma risulta indistruttibile per costruzione.
**Terza forma, aggiunta in v2 — la chirurgia sul DENOMINATORE**: dichiarare `E = 0` («nessun paper ha quantità
riproducibili nello scope»), escludere in silenzio paper dalla popolazione riproducibile, contare le esche nel fill
rate, cambiare l'unità di misura fra un criterio e l'altro. Si sposta lo scope dal claim al metro, e ogni gate
costruito su quel denominatore passa sempre. *(unanime 5/5)*

**A9 — SIMMETRIA IMPLICITA DEI COSTI, HEDGING UNIVERSALE, PUNTEGGI COMPOSITI.**
Stessa soglia per «adottare» e per «dichiarare falsificato»; verdetti binari senza livello di certezza e senza domini
nominati; nessuna categoria «il paper tace» o «accesso insufficiente», così ogni paper viene forzato in una delle
quattro relazioni e il silenzio genera minacce fantasma. Speculare: qualificare tutto con «potrebbe/suggerisce»
finché nessun verdetto è più falsificabile. Terza forma: «rilevanza 7/10», «minaccia media», ranking, percentuali di
allineamento — numeri senza una procedura che li possa rigettare. Corollario: usare «falsificato» per dire «non
supportato dalla letteratura letta», che è un'affermazione sul CORPUS, non sul claim. *(unanime 5/5)*

**A10 — PESO SCAMBIATO PER RIGORE; STRUMENTO NON TARATO NÉ PULITO; TRIAGE DI BUDGET TRAVESTITO DA SCOPO.**
Round rituali, panel e giudici come segnale di serietà, senza mai riportare il potere di rigetto dell'apparato
(kill rate, mutanti uccisi, demozioni, flip per round). Un'orchestrazione grande con kill rate zero è **più
pericolosa** di una piccola: costa di più e produce fiducia ingiustificata. **Faccia «strumento» (v2)**: contare flip
senza baseline di rumore appaiata (si aprono finding sul rumore e si giustificano componenti col rumore); azzerare la
temperatura per far passare i gate, che nasconde l'effetto invece di misurarlo; lasciare i propri semi dentro il
record finale. **Faccia «budget»**: ridurre in silenzio il banco mutanti o le invarianze perché costano; escludere
senza dichiararli i paper storici, in lingua straniera, solo-abstract o dietro paywall e presentare il risultato come
confrontazione con «la letteratura». Legittimo è ridurre ed escludere **dichiarando** il gap, con owner, trigger di
riapertura, preventivo a consuntivo e copertura stimata accanto al verdetto globale.
*(llm-agent, verification, evidence, metascience)*

---

# SEZIONE 3 — SCARTI (criteri proposti e NON ammessi al set, con motivo)

Gli scarti fanno parte del verdetto: dicono dove il panel ha importato metodo da domini vicini senza che il metodo
regga il trasferimento. **S1-S13** vengono dal round di sintesi; **S14-S26** sono gli scarti prodotti dalla
riparazione post-refuter, e riguardano quasi tutti test che *sembravano* misurabili e non lo erano.

**S1 — ECE / Brier score sui verdetti come metrica di PASS** *(llm-agent G11)*.
SCARTATO. Con ~75 celle e un gold di ~20 verdetti aggiudicati l'ECE è dominato dal rumore di binning: «ECE = 0.07» su
20 punti è precisione spuria. In v1 sopravviveva la parte ordinale in SOTA-18; in v2 **anche quella è caduta** (S14).

**S2 — Soglie numeriche importate dal software testing** (mutation score ≥0.80, ≥0.70 per strato, falso-kill ≤0.10;
κ ≥0.95; accordo ≥0.80; MR violation ≤0.10) *(verification MUT/DIFF/META, evidence C3/C6)*.
SCARTATE **come numeri**, conservate come **obbligo di soglia pre-registrata con motivazione**. Provengono da
benchmark di unit test su codice, dove la popolazione di mutanti non ha relazione con «un teorema con ipotesi nominate
contro un paper del 1979». Importarli sarebbe una tolleranza magica (R5 di progetto). Resta binaria la sensibilità
100% sulle classi P0 di SOTA-3. **Estensione v2**: la stessa disciplina è applicata alle soglie superstiti del set —
recall 0.80 (SOTA-10) e concordanza 0.90 (SOTA-14) devono essere **motivate o dichiarate arbitrarie**.

**S3 — κ di Cohen / α di Krippendorff come criterio di successo** *(evidence C3, verification DIFF, comparison C10)*.
SCARTATO come gate, mantenuto come numero da pubblicare in SOTA-7. κ alto è ambiguo: può significare qualità o
contaminazione, e il suo segno dipende da SOTA-3 e SOTA-15. Una metrica il cui segno di merito si inverte a seconda
di un'altra misura non può essere una soglia di chiusura. Unico uso non ambiguo conservato: **κ > 0.90 con mutanti
sopravvissuti = FAIL**.

**S4 — Compliance PRISMA-S 16/16 e ricostruzione del corpus con recall ≥0.95** *(evidence C2)*.
SCARTATI: PRISMA-S presuppone database interrogabili con stringhe booleane riproducibili e una domanda in forma PICO;
qui il corpus è ~25 primari eterogenei, in parte storici e cartacei. La compliance formale misurerebbe la compilazione
di un modulo, non il recall. Sostituiti dalla forma operativa in SOTA-10.

**S5 — Capture-recapture come GATE con copertura stimata ± intervallo** *(verification CORPUS, comparison C6)*.
DECLASSATO a estensione FORTE dentro SOTA-10: lo stimatore richiede indipendenza delle catture, e due routine LLM
sullo stesso prior condividono il bias di richiamo (A2 applicato alla ricerca). Ammesso solo con percorsi
materialmente diversi e con l'ipotesi di indipendenza dichiarata dubbia accanto al numero.

**S6 — Living systematic review con aggiornamento continuo** *(evidence C12)*.
SCARTATO come obbligo: fuori budget e fuori scopo per un programma a fasi e gate. Ridotto alla parte load-bearing in
SOTA-16 (data di validità, trigger con owner e finestra, marcatura STALE a macchina).

**S7 — Import integrale del framework GRADE** *(evidence C7/C11, metascience, verification GRADI)*.
SCARTATO come framework: «publication bias» presuppone studi con esiti sopprimibili e non si applica a teoremi;
«imprecisione» presuppone stime con intervalli di confidenza. Conservati in SOTA-14 i due domini che si trasferiscono
(qualità della fonte, indirectness) più il contributo originale di GRADE: la separazione fra certezza dell'evidenza e
forza dell'azione autorizzata.

**S8 — DO-178C / MC-DC come riferimento normativo** *(verification COP, GRADI)*.
SCARTATO: nessuna lente ha aperto lo standard (a pagamento) e MC/DC è copertura strutturale su decisioni booleane,
senza traduzione su una matrice paper×strato. L'idea generale (rigore scalato per criticità) è già in SOTA-14.

**S9 — Auto-correzione / auto-critica dell'agente come canale di verifica**.
SCARTATO in radice e registrato perché è ciò che le orchestrazioni fanno per default: senza segnale esterno
l'auto-correzione non migliora e spesso degrada, e un giudizio prodotto dallo stesso processo la cui affidabilità è
sotto esame non è evidenza. Il canale legittimo è SOTA-8.

**S10 — `verdict_stability ≥ 0.85/0.95` come criterio di PASS** *(verification PROV, evidence C12)*.
DECLASSATO a numero riportato in SOTA-16: la stabilità misura il determinismo dell'apparato, non la verità del
verdetto; usarla come gate premia la bassa temperatura anziché la correttezza. **Nota v2**: la stessa misura,
resa **appaiata** e dichiarata riferimento, diventa la baseline `b` — utile come *metro*, mai come *promozione*.

**S11 — Baseline self-consistency a parità di budget sull'intera campagna** *(llm-agent G12)*.
DECLASSATO: raddoppia il costo di una classe budget-limitata e su ~25 paper non produce punti sufficienti.
Conservato in SOTA-17(5) sul solo gold subset, **e solo se il gold validato esiste**.

**S12 — Peer review della strategia di ricerca stile PRESS** *(evidence C2)*.
SCARTATO: richiede un revisore umano esperto di ricerca bibliografica del dominio, fuori dal perimetro di esecuzione.
La funzione che svolge è coperta in modo eseguibile dal known-item test di SOTA-10, che è un rejector e non
un'opinione.

**S13 — «Un umano esperto» come aggiudicatore obbligatorio del gold**.
NON scartato ma **declassato a opzione**: aggiudicatore = umano **oppure** agente context-free con evidenza completa
e contratto disgiunto. Ciò che conta è il contratto (default-refute, arbitro, registrazione preventiva), non la specie
dell'aggiudicatore. **Precisazione v2**: l'opzione non è libera — l'aggiudicatore deve passare la validazione a
errori seminati di SOTA-4(iii'), altrimenti il gold non è un metro. La supervisione umana resta obbligatoria dove
l'esito diventa citazione nel paper.

---

### Scarti prodotti dalla riparazione post-refuter (v2)

**S14 — SOTA-18-v1 «Astensione tarata sul tier e confidenza non pubblicata senza valutazione»**.
**RIMOSSO dal set** (verdetto refuter: RIDONDANTE). La voce (ii) — `abstention_rate` per tier e correlazione
tier↔astensione — era già obbligatoria in SOTA-4(ii) e la propagazione del tier è SOTA-6(iv): stessa garanzia
riscritta. La voce (i) — accuratezza in fascia alta **strettamente** maggiore che in fascia bassa — è una
disuguaglianza senza margine né potenza su ~20 verdetti aggiudicati: si decide a testa o croce, ed è lo stesso vizio
per cui era stato scartato S1. La garanzia sostantiva («una confidenza pubblicata deve portare informazione
dimostrata») è coperta **in forma più forte e non statistica** da SOTA-14(iii), dove il livello di certezza è un
CALCOLO ri-derivabile dai domini nominati. Assorbimento eseguito: mezza riga in SOTA-4(ii') (correlazione come
numero) e una clausola in SOTA-14(iii) (nessuna confidenza senza domini nominati e ri-derivazione indipendente).
Tenerlo come criterio autonomo era A10 applicato al set di criteri stesso.

**S15 — MR5 «non-influenza» come relazione metamorfica autonoma di SOTA-15**.
SCARTATA come voce separata: è **letteralmente** l'esca di esposizione di SOTA-4(i). Il set dichiarava la fusione e
poi contava lo stesso controllo in due gate. Vive solo in SOTA-4(i'); SOTA-15 la cita come dipendenza.

**S16 — «target 0» assoluto sull'insieme degli span nel flip-test direzionale** *(SOTA-7 ii di v1)*.
SCARTATO: senza baseline appaiata due run identici cambiano già gli span; il test o fallisce sempre, o si aggira
azzerando la temperatura, o si allenta a posteriori. Sostituito da `Jaccard(speculare) − b_span` con margine
pre-dichiarato e `b_span` pubblicata. Il target 0 assoluto sopravvive **solo sul cambio del verdetto**.

**S17 — «PASS solo a 0» su M = 3 esche come prova di FPR nullo** *(SOTA-4 i di v1)*.
SCARTATO come asserzione di potenza: con M = 3 un apparato a FPR reale 20% passa nel 51% dei casi, e i valori 3/3/20
erano importati senza derivazione (stesso vizio di S2). Sostituito da `M = ⌈ln α / ln(1 − FPR_max)⌉` e, se il budget
non lo consente, dalla pubblicazione dell'**FPR massimo rilevabile** accanto al PASS.

**S18 — CER/WER dell'OCR misurati contro una trascrizione prodotta da LLM** *(SOTA-6 ii di v1)*.
SCARTATO perché **circolare**: lo stesso apparato che sbaglia la lettura fornirebbe la verità di riferimento, e la
soglia passerebbe sempre. Sostituito dai tre indicatori di SOTA-6(ii') (disaccordo fra due motori OCR indipendenti;
token fuori-lessico; CER/WER veri su `k ≥ 3` pagine trascritte a mano) con soglie separate per prosa, equazioni e
tabelle.

**S19 — «Uno strato sotto soglia = FAIL non compensabile» applicato a TUTTI i mutanti** *(SOTA-3 di v1)*.
RISTRETTO: la regola resta per i mutanti **con witness atteso**; i mutanti che nessun paper del corpus poteva rivelare
finiscono nel bucket NON-RILEVABILE-DA-QUESTO-CORPUS, riportato ma fuori dal `detection_rate`. La formulazione
originale mescolava **cecità dell'apparato** e **silenzio del corpus**, puniva il canale sbagliato e creava pressione
ad allentare le soglie.

**S20 — Disegni di esecuzione senza preventivo: «43+ mutanti in cieco» come campagne complete, e inversione d'ordine
del giudice «su TUTTE le coppie»** *(SOTA-3 e SOTA-15 di v1)*.
SCARTATI come disegno: su un budget dichiaratamente finito la riduzione avverrebbe comunque, e in silenzio (A10).
Sostituiti da iniezione multipla per run con test di non-interazione (SOTA-18 ii) e da campione a seme e potenza
dichiarati, entrambi con **preventivo in token ex ante e a consuntivo**.

**S21 — `E` («paper con quantità riproducibili nello scope») auto-dichiarato dagli agenti che devono riprodurre**
*(SOTA-12 iii di v1)*.
SCARTATO come definizione del denominatore: «`E>0` con `tentati=0` ⇒ FAIL» si aggira dichiarando `E = 0`. È la
chirurgia di scopo di A8 spostata sul denominatore, e passa sempre. Sostituito dal passo antecedente separato, con
default AMMISSIBILE e ogni esclusione attaccabile dal canale default-REFUTE.

**S22 — «Un corpus in cui ogni paper interagisce con ogni strato è sospetto e va giustificato»** *(SOTA-4 ii di v1)*.
SCARTATO: «sospetto» non è un test. Sostituito dalle soglie a due lati sulla distribuzione dei token (SOTA-9 v') e
dalla soglia sulla frazione di celle non-NESSUNA-INTERAZIONE (SOTA-4 ii').

**S23 — «`flip_count = 0` ⇒ componente non load-bearing, rimosso» come regola nuda** *(SOTA-17 di v1)*.
SCARTATO: logicamente rovesciato rispetto al costo d'errore asimmetrico della classe (il canale che intercetta il caso
fatale 1-su-30 mostra 0 flip su ~25 paper e verrebbe rimosso proprio prima della finestra in cui serve) e privo di
baseline (un `flip > 0` può essere puro non determinismo). La clausola di salvataggio «oppure dichiarato come
controllo» era discrezionale e senza test: qualunque componente poteva sopravvivere con un'etichetta e qualunque
componente scomodo cadere con un numero. Sostituito dalla regola **(a) OR (b)** di SOTA-17(1-2).

**S24 — «Tasso di ricostruzione» del test di sostituzione cieca** *(SOTA-11 iii di v1)*.
SCARTATO: non diceva che cosa conta come ricostruzione riuscita né chi lo giudica — era un oracolo di classe **J**,
che SOTA-12(v) vieta ai verdetti di record. Il test più potente del criterio era anche il suo unico non misurabile.
Sostituito dal punteggio **attributo-per-attributo** su `k ≥ 5` attributi discriminanti, con match esatto o
equivalenza dichiarata.

**S25 — `mtime` di filesystem come prova di anteriorità**.
SCARTATO: l'ordinamento temporale si appoggiava a timestamp prodotti dallo stesso processo sotto esame. Ancora
esterna obbligatoria = **DAG dei commit** (D5). Vale per SOTA-1(i'), SOTA-2(1), SOTA-12(4), SOTA-18(1).

**S26 — Auto-dichiarazione della marcatura pre/post-visione degli esiti** *(SOTA-1 iv di v1)*.
SCARTATA come canale: la marcatura era dichiarata dall'agente che devia, quindi passava sempre. Sostituita dal
**calcolo sui log di accesso**, con la discordanza fra dichiarazione e calcolo promossa a finding di record.

---

# SEZIONE 4 — PROVENIENZA PER LENTE

**Avvertenza di record.** Tutte e cinque le lenti hanno dichiarato in modo esplicito il proprio stato di verifica
(«metadata/abstract verificati, full text NON aperto» nella maggioranza dei casi) e hanno elencato separatamente i
riferimenti citati a memoria. **Nessuna fonte citata qui sotto è stata aperta integralmente in questa sessione di
giudizio.** Prima che una qualunque di queste citazioni compaia in P-1 va aperta e verificata — coerentemente con
SOTA-5, che questo documento applica anche a se stesso. Le cifre riportate sono «come riportate dalla fonte
secondaria», non numeri controllati.

**Avvertenza v2.** Le riparazioni della Sezione 1 **non provengono da una sesta lente né da nuova letteratura**:
provengono dal round di attacco default-REFUTE, cioè da un'analisi di fallibilità dei test già scritti. Non
aggiungono quindi debito bibliografico, ma non aggiungono nemmeno supporto esterno: le nuove clausole vanno
giudicate sul loro potere di rigetto, non sulla loro provenienza.

### Lente 1 — `evidence-synthesis` (12 criteri proposti)
**Contributo distintivo**: separazione fra certezza dell'evidenza e forza dell'azione autorizzata (→ SOTA-14);
protocollo congelato con ledger delle deviazioni (→ SOTA-1); tag di accesso/lingua che si **propaga** (→ SOTA-6);
matrice a categorie esaustive con dizionario ed esemplari (→ SOTA-9).
**Fonti addotte**: PRISMA 2020 (Page et al.); PRISMA-S (Rethlefsen et al., Syst Rev 2021); GRADE Working Group e
Cochrane Handbook cap. 14; Elliott et al. (living systematic reviews, J Clin Epidemiol 2017); Gartlehner et al.
(screening a revisore singolo perde ~13% vs ~3% in doppio); Waffenschmidt et al. (BMC MRM 2019, mediana 5% mancati);
SWiM (Campbell et al., BMJ 2020;368:l6890); White et al. (Campbell EGM guidance, 2020); AMSTAR-2/ROBIS (BMC MRM 2021);
RAISE / position statement Cochrane-Campbell-JBI-CEE 2025; studi su fabbricazione di citazioni da LLM (PMC12658395;
MDPI Data 2026, ~19.9% citazioni interamente fabbricate in review generate da GPT-4o).
**Dichiarati NON verificati dalla lente stessa**: Cochrane RoB 2, ROBINS-I, PRESS, Cochrane Handbook capp. 4-5,
GRADE Evidence-to-Decision, κ di Cohen.
**Esito nel set**: 4 criteri portanti (SOTA-1, 6, 9, 14), 6 assorbiti, 3 declassati/scartati (S4, S6, S7).

### Lente 2 — `llm-agent-systems` (12 criteri proposti)
**Contributo distintivo**: il matcher **non-LLM** come risolutore degli span (→ SOTA-5); la disciplina di strato con
divieto di riciclo del locator (→ SOTA-13); la misura dell'indipendenza come `n_indipendenti` e l'ablazione di
contagio (→ SOTA-15); il rejector che deve **ribaltare** un claim di novità (→ SOTA-10); il peso dell'orchestrazione
giustificato dai flip (→ SOTA-17, criterio a origine unica).
**Fonti addotte**: Liu, Zhang, Liang (Findings EMNLP 2023: 51.5% frasi pienamente supportate, 74.5% citazioni che
supportano la frase); Gao et al. ALCE (EMNLP 2023); Tian et al. (EMNLP 2023, calibrazione/ECE); Huang et al.
(arXiv 2310.01798, «LLMs Cannot Self-Correct Reasoning Yet»); Kambhampati et al. (ICML 2024, LLM-Modulo);
Zheng et al. (NeurIPS 2023, MT-Bench: position/verbosity/self-enhancement bias); ICLR 2025 Blogposts su MAD vs
self-consistency.
**Dichiarati NON verificati dalla lente stessa**: Walters & Wilder; Wang et al. self-consistency; Rashkin et al. AIS;
DeMillo-Lipton-Sayward 1978; Jia & Harman; teorema di Condorcet; preprint su conformity/sycophancy multi-agente.
**Esito nel set**: 5 criteri portanti (SOTA-5, 10, 13, 15, 17), 6 assorbiti; **il criterio di calibrazione (G11) è
stato RIMOSSO in v2** (S14) — è l'unica lente che perde una riga nel round di riparazione.

### Lente 3 — `verification-qa` (12 criteri proposti)
**Contributo distintivo**: banco mutanti stratificato con mutanti equivalenti e falso-kill (→ SOTA-3); **vacuity
check** su witness set (→ SOTA-9), l'aggiunta più originale dell'intero panel; tassonomia dell'oracolo T/D/P/M/J/U
(→ SOTA-12); impact set con precision/recall della staleness detection (→ SOTA-16); relazioni metamorfiche
(→ SOTA-15).
**Fonti addotte**: Barr, Harman, McMinn, Shahbaz, Yoo (IEEE TSE 41(5):507-525, 2015, oracle problem);
Segura et al. (IEEE TSE 42:805-824, 2016) e Chen et al. (ACM CSUR 51(1), 2018) sul metamorphic testing;
Knight & Leveson 1986 (27 versioni, fallimenti coincidenti — il riferimento più dirimente contro A2);
Kupferman & Vardi e Beer et al. sulla vacuity detection; Just et al. FSE 2014 (parziale); Petrović & Ivanković
ICSE 2021; arXiv 2404.09241 (mutanti equivalenti); Gao et al. ALCE; Cochrane Handbook cap. 5 (Buscemi et al. 2006);
capture-recapture (PMID 8760743, PMID 18722088); Kahneman/Clark-Tetlock adversarial collaboration; PLOS Biology 2020.
**Dichiarati NON verificati / parziali dalla lente stessa**: DO-178C; GRADE; PRISMA 2020.
**Esito nel set**: 5 criteri portanti (SOTA-3, 9, 12, 15, 16), 6 assorbiti, DO-178C scartato (S8). **In v2 il suo
impact set diventa anche il motore del freeze (SOTA-1 vi) e la sua misura di stabilità diventa la baseline `b`.**

### Lente 4 — `metascience-audit` (12 criteri proposti)
**Contributo distintivo**: **estrazione cieca alla direzione dell'esito** con flip-test sul claim speculare
(→ SOTA-7); **controlli negativi ed esche** con FPR misurato (→ SOTA-4); rule-lock con distinzione fra deviazioni pre-
e post-visione degli esiti (→ SOTA-1); antipattern dello **steel-man implicito** (→ A8).
**Fonti addotte**: MacCoun & Perlmutter (Nature 526:187-189, 2015, blind analysis); Brown & Heathers (GRIM, SPPS 2017)
e Nuijten et al. (statcheck, Behav Res Methods 2016) come modello di controllo meccanico e non discrezionale;
Jergas & Baethge (PeerJ 3:e1364, 2015) e Baethge & Jergas (RIPR 2025: 16.9% [14.1-20.0] di quotazioni errate, ~8%
errori maggiori); Buscemi et al. (J Clin Epidemiol 59:697-703, 2006); Cochrane Handbook cap. 5; PRISMA 2020/PRISMA-S;
Adversarial Collaboration Project (Clark & Tetlock); Magesh et al. (arXiv 2405.20362, 17-33% risposte allucinate in
RAG legali); arXiv 2406.07791 (position bias); arXiv 2410.21819 (self-preference bias); Lipsitch et al.
(Epidemiology 21(3):383-388, 2010, negative controls).
**Dichiarati NON verificati dalla lente stessa**: DeMillo et al. 1978; Silberzahn et al. 2018; Guyatt et al. GRADE;
soglie di Krippendorff; Nosek et al. PNAS 2018.
**Esito nel set**: 2 criteri portanti (SOTA-1, 4), 9 assorbiti, 1 antipattern originale adottato. **In v2 SOTA-4
cresce: ospita il gold validato, cioè il metro dell'intero set.**

### Lente 5 — `comparison-methodology` (12 criteri proposti)
**Contributo distintivo**: contratto di corrispondenza tipata con mappa simbolo→simbolo, unità e convenzioni di segno
(→ SOTA-11); distinzione riduzione-derivazione vs riduzione-limite con **limiti singolari** e testimone eseguito
(→ SOTA-12); **qualificazione non-vacua** con shrinkage dello scope misurato (→ SOTA-2); tassonomia chiusa con
`INCOMPARABILE-FINCHÉ-x` (→ SOTA-9); indicatore di compiacenza (colonna «corregge il programma» vuota ⇒ lista dei
near-miss).
**Fonti addotte**: Nickles (J Philosophy 70(7):181-201, 1973); Panickssery, Bowman et al. (NeurIPS 2024,
arXiv 2404.13076); Kahneman & Klein (American Psychologist 64(6):515-526, 2009); DeMillo et al. 1978 e Jia & Harman
(IEEE TSE 37(5):649-678, 2011); ASME V&V 20-2009 (R2021); ACM Artifact Review and Badging v1.1 (2020); RIPR 2025;
capture-recapture (PMID 8760743).
**Dichiarati NON verificati dalla lente stessa**: Tarski-Mostowski-Robinson 1953; Goguen & Burstall; Nagel 1961 e
Batterman sui limiti singolari; PRISMA 2020; Cochrane Handbook; Cohen 1960 e Landis & Koch 1977; Popper; Lakatos 1970;
Oberkampf & Roy 2010; W3C PROV; Zheng et al. 2023.
**Nota di onestà della lente**: ha dichiarato incertezze bibliografiche residue invece di risolverle per congettura —
comportamento che questo giudizio registra come esemplare e che SOTA-5 rende obbligatorio.
**Esito nel set**: 3 criteri portanti (SOTA-2, 11, 12), 8 assorbiti, capture-recapture declassato (S5).

### Round 6 — refuter default-REFUTE (18 verdetti + 6 garanzie mancanti)
**Contributo distintivo**: non ha proposto criteri, ha attaccato test. Esito: 5 REGGE (SOTA-5, 8, 10, 13, 14, 16 —
sei, con SOTA-16), 11 TEST-NON-MISURABILE con versione riparata allegata, 1 RIDONDANTE. Le sei garanzie mancanti che
ha nominato — baseline di rumore appaiata, gold definito e validato, freeze dell'oggetto sotto test, igiene e
de-seeding dei semi, simmetria dell'attacco per polarità, voce dello span e hop-count — sono tutte entrate nel set:
quattro assorbite, una (i semi) come criterio nuovo, una (il gold) come estensione strutturale di SOTA-4.
**Contributo trasversale più importante**: aver mostrato che tre difetti — denominatore auto-dichiarato, metro dello
stesso ceppo, flip non appaiati — attraversavano criteri diversi e si tenevano a vicenda in piedi.

### Convergenza fra lenti (misura grezza del consenso)
| Cluster | Lenti che l'hanno proposto indipendentemente |
|---|---|
| Rejector/mutanti seminati (SOTA-3) | 5/5 |
| Ancoraggio verbatim localizzato (SOTA-5) | 5/5 |
| Copertura come matrice misurata (SOTA-9) | 5/5 |
| Provenienza + staleness (SOTA-16) | 5/5 |
| Verifica avversariale default-refute (SOTA-8) | 5/5 |
| Pre-registrazione / rule-lock (SOTA-1) | 4/5 |
| Doppia lettura indipendente (SOTA-7) | 4/5 |
| Tier di accesso che cappa il verdetto (SOTA-6) | 4/5 |
| Barra probatoria asimmetrica (SOTA-14) | 4/5 |
| Adeguatezza del corpus (SOTA-10) | 4/5 |
| Invarianza e bias del giudice (SOTA-15) | 4/5 |
| Matching delle ipotesi / tipizzazione (SOTA-11) | 3/5 |
| Disciplina di strato (SOTA-13) | 3/5 |
| Testimone eseguito (SOTA-12) | 2/5 |
| Peso dell'orchestrazione (SOTA-17) | 1/5 |
| Igiene e de-seeding dei semi (SOTA-18) | 0/5 lenti — **1 refuter** |

Il consenso non è di per sé evidenza (A2 vale anche per questo panel: le cinque lenti condividono famiglia di modello).
La colonna va letta come **mappa di ridondanza**, non come voto. Nota v2 di rilievo: **il criterio con il consenso più
basso (0/5) è nato dall'attacco, non dalla proposta** — cioè dal solo ruolo del processo che era contrattualmente
obbligato a cercare ciò che manca. È una conferma diretta di A1 e la ragione per cui SOTA-8 esiste.

---

## Come si usa questo set

1. È una **definizione di SOTA**, non un piano di sessione: dice a quali condizioni una confrontazione corpus×programma
   può diventare di record, non quanto costa produrla.
2. Prima di eseguirla, il set va **strumentato**, e la strumentazione è ora esplicitamente a due livelli:
   **(a) l'oggetto** — SOTA-1 (protocollo congelato **e snapshot di programma+corpus**), SOTA-2 (falsificatori),
   SOTA-3 (banco mutanti), SOTA-4 (esche **e gold validato**), SOTA-18 (registro dei semi) sono tutti pre-lettura;
   **(b) il metro** — la baseline di rumore `b` (SOTA-16 v') va misurata **prima** di qualunque criterio che conti
   flip. Se non esistono prima del primo PDF, la sessione può produrre solo esplorazione dichiarata come tale.
3. Ogni criterio porta almeno un **rejector seminato**, e tutti i semi vivono in un registro unico con prova di
   rimozione: la regola trasversale è che *un detector che non spara sul proprio seme è rotto*, e la sua gemella v2
   che *un record che non può dimostrare di essere privo dei propri semi non è citabile*.
4. Le unità di misura sono uniche per tutto il set (D0-D5). Un numero espresso su un'altra unità non è confrontabile
   e non è di record.
5. Il verdetto globale della confrontazione porta obbligatoriamente il proprio limite di validità: «rispetto a un
   corpus con copertura stimata X, con un apparato di sensibilità misurata Y per classe di difetto **e rumore
   misurato `b`**».

---

## Residui aperti dichiarati (input al prossimo round di attacco)

Il refuter ha chiuso con `converged: false`; questa versione risponde ma **non dichiara convergenza**. Restano aperti,
nominati qui invece che nascosti:

1. **Voce dello span verificata sul contesto di pagina (SOTA-5 vi)**: la verifica della voce resta in parte un
   giudizio su testo (classe J indebolita), mitigato dall'obbligo di pagina intera in contesto e dal rejector
   seminato. Non esiste ancora un test non-LLM che distingua «asserito» da «criticato». È il residuo più serio del
   set: va attaccato al prossimo round.
2. **Soglie superstiti** (recall 0.80 in SOTA-10, concordanza 0.90 in SOTA-14, tutti i margini pre-dichiarati contro
   `b`): il set impone di motivarle o dichiararle arbitrarie, ma nessuna è ancora derivata. Finché non lo sono, sono
   promesse di derivazione, non derivazioni.
3. **Potenza del gold** (SOTA-4 iii'): `m ≥ 20` con ≥3 errori seminati è un metro debole in senso statistico; il set
   lo ammette perché il divieto di parlare di FP/FN quando fallisce la validazione è più forte del numero, ma la
   dimensione resta sotto-argomentata.
4. **Preventivi in token** (SOTA-3(6), SOTA-15(6), SOTA-17): il set li impone ma non li fissa. Se al momento
   dell'esecuzione i preventivi non vengono scritti PRIMA, la riduzione tornerà silenziosa e A10 rientra dalla
   finestra.
5. **Interazione fra freeze e known-item test**: SOTA-1(vi) congela il corpus per la finestra, SOTA-10(2) può
   scoprire in finestra un rilevante mancante. La regola di record oggi è «nuovo paper ⇒ deviazione datata + nuova
   finestra», ma il costo di questa scelta non è stato misurato su un caso reale.
