# ATLAS_RESEARCH_DESIGN v2 — L'albero delle domande di ricerca

Research designer v2 S-PRES, 2026-08-23. Input: ATLAS_RESEARCH_DESIGN.md (v1)
+ REFUTE_DESIGN.md (16 finding: 2 BREAK / 6 REPAIR / 5 GAP / 3 NOTE, verdetto
REGGE-CON-RIPARAZIONI) — entrambi letti integralmente in finestra. Stadio di
confronto: v1 contro (a) i 16 finding, (b) il record Fase A/B/D ri-misurato in
finestra (`validation/sfoundations_raws_2026-08-13/`: phaseA_problem_brief.md
letto integrale; phaseB_tree_diff.md header+§3-§5; phaseD/ censita), (c) il
registry (`grep -c "id:" docs/literature_registry.yaml` = 174 in finestra;
ogni id citato qui ri-verificato per grep esatto in finestra), (d) SCAFFOLD §6
amendment :218-253 (L7/L8/L9, letto). Arco di consumo: questo documento
SUPERSEDE v1 come contratto delle onde di estensione dell'ATLAS e ossatura del
deck ESA; v1 resta su disco come storia.

Ordini utente vincolanti recepiti in v2 (quattro trasformazioni):
(1) TUTTE le 16 riparazioni del refuter applicate, marcate [V2-R1..R16],
disposte in tabella finale §F; (2) struttura PRIMARIA = ALBERO DELLE DOMANDE
DI RICERCA (§Q), matrice 80-celle retrocessa a check di copertura (§M),
capitoli rimappati non riscritti (§CH); (3) CONFORMITY MAP contro standard
mondiali (§C) — definizione utente di SOTA = "rispetto alle convenzioni,
prassi e standardizzazioni mondiali"; claim SOTA senza standard citato =
violazione del design (lint 6); (4) piano d'esecuzione emendato (§W): onde
con file-disgiunti rigorosi, ownership per sezione, effort policy dichiarata,
lint ancorati alla tabella per-cella (§L).

Principio di derivazione (invariato da v1, emendato [V2-R8]): la matrice §M
è derivata A PRIORI dal perimetro — layer SCAFFOLD L0-L6 PIÙ i tre layer
dell'amendment §6 :218-253: **L7 (validation record layer) → assorbita dalla
riga/nodo J** (la catena di evidenza e adjudication È materia di
certificazione; l'indice ADVISORY_INDEX entra in CH-REF via lint 1);
**L8 (literature layer, 4 root + registry) → assorbita dalla riga/nodo N**
(+ lint-registri come verifica); **L9 (governance layer: CLAUDE.md, memoria,
glossario, flag) → FUORI-PERIMETRO** con ragione: governance dell'harness,
non materia d'atlas — la sua metà "metodo tenuto coerente" è invece materia
del nodo N-P via [V2-R12]. I 21 buchi del critic entrano solo al §D come
lista da disporre (esito: 21/21 trovano cella).

==============================================================================
## §Q L'ALBERO DELLE DOMANDE (STRUTTURA PRIMARIA DELL'ATLAS)

### Q0 — la domanda madre

> **Q0: Come si disegna l'ugello OTTIMO per un flusso RDE, con errore
> CONTROLLATO?**

Falsificatore di Q0 (il programma intero): esibire un ugello prodotto dalla
catena il cui J misurato/certificato sia battuto oltre le barre dichiarate da
un design della stessa classe ammissibile, o un errore |J_exact − J| fuori
dalla forchetta dichiarata (M0 Parte I; D6 G2 kill criterion :776-782). Le
barre e il contratto-dati sono PARTE della domanda: senza "errore
controllato" Q0 collassa nella pratica corrente del campo (sweep CFD).

Q0 si ramifica in quattro rami di raccordo (R-I..R-IV, nodi organizzativi
DICHIARATI: non portano template proprio, la loro sostanza è l'unione dei
figli) e sedici nodi-domanda N-A..N-P, uno per aspetto della matrice §M.
Ogni nodo-domanda porta il template a 8 sezioni del §T. Due nodi sono
**foglie di servizio dichiarate** (N-L roadmap, N-P metodo): domanda
falsificabile anche loro, ma infrastrutturale — il loro template ammette le
clausole di vacuità del §T. CH-REF resta ANNEX di servizio fuori albero
(nessuna domanda propria, nessun claim: mappa id→nodo, glossario, legenda
namespace, ordine di lettura).

### L'albero

```
Q0 come si disegna l'ugello ottimo per un flusso RDE, con errore controllato?
|
+- R-I   CHE PROBLEMA RISOLVIAMO (formulazione)
|   +- N-A  il problema e i suoi dati      (riga A; CH1)
|   +- N-B  quando mediare e' esatto       (riga B; CH1)
|   +- N-F  che forma puo' emergere        (riga F; CH8)
|
+- R-II  CHE TEORIA LO RISOLVE (ottimalita' e riduzione)
|   +- N-C  l'ottimalita' mediata          (riga C; CH2)
|   +- N-D  il residuo esatto              (riga D; CH3)
|   +- N-E  lo swirl nell'edificio         (riga E; CH7)
|   +- N-G  dal locale al globale          (riga G; CH8 §1.7 nuovo)
|   +- N-H  fin dove vale (licensing)      (riga H; CH1 §1.7 nuovo)
|
+- R-III CHE MACCHINA LO CALCOLA (strumenti e verita')
|   +- N-I  gli strumenti e le scelte      (riga I; CH4)
|   +- N-J  la catena che puo' dire NO     (riga J; CH9 NUOVO)
|   +- N-K  il contratto dei dati          (riga K; CH10 NUOVO)
|   +- N-M  la correzione di unsteadiness  (riga M; CH3+CH6)
|
+- R-IV  CHE VALORE HA E COME LO SI RACCONTA (campo, valore, programma)
    +- N-N  cosa fa oggi il campo          (riga N; CH5)
    +- N-O  quanto vale e dove ci fermiamo (riga O; CH6)
    +- N-L  in che ordine si decide        (riga L; CH6)   [servizio]
    +- N-P  perche' fidarsi del metodo     (riga P; §6 ovunque + CH9 §7) [servizio]
```

Conteggio nodi: 1 (Q0) + 4 (rami) + 16 (nodi-domanda) = **21 nodi**.

### Le sedici domande (precise, falsificabili)

- **N-A** — *Che cosa è dato e che cosa è cercato? Esiste un contratto
  d'interfaccia (classe-dati su Γ_d, misura µ, pin onda-pura H-DATA) che
  renda il problema ben posto a valle dell'interfaccia?* Falsificatore:
  violazione H-DATA rilevata dal flatness monitor; dataset motore fuori
  classe → G6 loud-reject (D6 :808-815).
- **N-B** — *Quando disegnare sulla MEDIA è esatto — e quando non lo è,
  quanto costa?* (quoziente, rung, PB-1..PB-5). Falsificatore: PB-2 — il
  gap medio-vs-esatto misurato oltre la forchetta (CH1 §3, OPEN).
- **N-C** — *Che forma hanno le condizioni di ottimalità per il funzionale
  mediato sul ciclo (parete condivisa, adjoint per-fase, sistema (**'))?*
  Falsificatore: un caso certificato in cui il sistema (**') fallisce KKT/
  trasversalità (record: 7.7e-02, oracolo 91/91 — memoria s18).
- **N-D** — *Qual è il residuo ESATTO della riduzione per-fase, canale per
  canale?* Falsificatore: un canale della forchetta misurato fuori banda
  (caveat band-underinclusion, critic 12).
- **N-E** — *Come entra il momento angolare medio (swirl) nell'edificio
  per-fase 2.5-D?* Falsificatore: la ladder di refutazione R22-F / i refuti
  SWIRL-2D (phaseD/, r1-r4 × l0-l2).
- **N-F** — *Che geometria/topologia seleziona la misura — il TIPO di ugello
  può essere un OUTPUT?* Falsificatore: il torneo dei settori — un settore
  escluso il cui champion batte il vincitore (T3/T4/ceiling, CH8 §1.4).
- **N-G** — *Con quale MECCANISMO DICHIARATO si passa dal KKT locale a un
  claim di globalità (M1-M5)?* Falsificatore: bound-as-oracle — un J oltre
  il bound B = bug istantaneo (dottrina riderivata cieca, phaseB §3.5).
- **N-H** — *Fin dove il metodo è licenziabile FUORI dal pin single-wave —
  e dove il certificato va RIFIUTATO onestamente?* Falsificatore: il muro
  ergodico S-GBE (caotico: J_exact+ ≤ F_env senza Birkhoff); flatness
  monitor come trigger di classe.
- **N-I** — *Con quali strumenti si calcola l'ottimo — e ogni scelta regge
  il confronto con le alternative mondiali?* Falsificatore: una riga del
  choice ledger con alternativa dominante non confutata (62 righe, memoria
  s-foundations-c4-closed).
- **N-J** — *Come sa la macchina di non mentire — la catena di
  certificazione può dire NO?* Falsificatore: GIÀ SPARATO ed è a registro —
  verdetto S-CERT NON-CERTIFICABILE con 2 P0 (uno riparato in-window,
  staleness → F2; memoria fservice-scert). Il NO detto è la prova che il
  falsificatore è vivo.
- **N-K** — *Che cosa serve, in DATI, per far girare il tool su un motore
  NON nostro?* Falsificatore: G6 loud-reject su dataset reale; U3' choking
  adjudication PREMISE-OPEN (owner F2a).
- **N-L** [servizio] — *In che ordine si decide, e che cosa può uccidere il
  programma?* Falsificatore: un gate senza kill criterion (G3 ne è
  l'istanza DICHIARATA, D6 :783-786).
- **N-M** — *Quanto vale la correzione di non-stazionarietà a St marginale —
  e quando serve il corrector?* Falsificatore: il trigger G3 derivato come
  NUMERO (F5b, D6 :271-273) — oggi assente, e l'assenza è l'aperto.
- **N-N** — *Come fa OGGI il campo gli ugelli per RDE — e che cosa risulta
  NOT-FOUND alle query?* Falsificatore: una ref che soddisfi una query G14 —
  il gap si chiude e il claim query-bounded cade (comportamento corretto).
- **N-O** — *Quanto VALE il metodo (Gap A/B) — e dove ci fermiamo
  onestamente?* Falsificatore: G2 VALUE GATE con kill criterion
  theorem-grade + calibrazione thrust-stand ~0.5-1% (D6 :776-782).
- **N-P** [servizio] — *Perché fidarsi delle derivazioni del programma?*
  Falsificatore: una divergenza Fase B non adjudicata; un ramo
  NON-RIDERIVATO senza doppia prova alternativa (§T-§6).

### Regola di copertura albero↔matrice (il check, non la struttura)

Ogni riga X della matrice §M = il nodo N-X; ogni CELLA della riga mappa a
sezioni fisse del template di nodo: **(i)→§4+§5, (ii)→§2-strumenti+§7(a),
(iii)→§2-senso+§7(b), (iv)→§3, (v)→§5**. Il check è BIDIREZIONALE: cella
senza sezione di nodo che la ospita = design falsificato; sezione di nodo il
cui contenuto non ha cella = matrice incompleta → stesso trattamento
(falsificatore del design, §L).

==============================================================================
## §T IL TEMPLATE DI NODO (8 sezioni, ordine utente vincolante)

Ogni nodo-domanda N-A..N-P porta, NEI CAPITOLI CHE LO SERVONO (§CH — il
materiale si rimappa, non si riscrive), le otto sezioni:

1. **LA DOMANDA** — l'enunciato preciso del §Q, con il falsificatore e le
   ipotesi sotto cui la domanda è ben posta.
2. **LETTERATURA (due colonne)** — (a) *senso/precedenti*: come il campo
   affronta QUESTA domanda (RDE + classici, genealogia); (b) *strumenti*:
   che cosa usa il mondo per domande di questa classe. OGNI ref = un id
   VERBATIM di `docs/literature_registry.yaml` [V2-R5]; ref fuori registry =
   riga nuova nel registry PRIMA dell'uso (WANTED con owner ammessa).
3. **LA PROPOSTA** — che cosa il programma propone di nuovo/meglio, SEMPRE
   query-bounded (M0 Parte I :56-60; tre passate avversarie; residuo G5).
4. **ANALISI FORMALE** — teoremi/classi di rigore con ancora M0/D-doc.
5. **STATO** — dimostrato / parziale / aperto, falsificatori vivi, decisioni
   pendenti con owner e trigger (mai riempite nel capitolo).
6. **STORIA** — vedi sotto, ramo condizionale [V2-R2].
7. **POSIZIONAMENTO / CONFORMITY** — vedi sotto [V2-R4] + colonna standard
   (§C).
8. **DOMANDE DA PANEL** — banco utente incluso, risposte ancorate.

### §T-§6 STORIA — il trittico CONDIZIONALE [V2-R2] (BREAK #2 riparato)

Tre battute per argomento: *derivazione originale* (sessione/commit di
nascita, ancora) → *seconda prova* (ramo condizionale sotto) → *convergenza*
(dove il record è cambiato, classe finale). Fonti: M0 / PROGRESS_ARCHIVE /
ledger / raws; niente ricordi, solo ancore (navigation-first).

La battuta 2 è CONDIZIONALE su che cosa la Fase A/B/D di S-FOUNDATIONS ha
DAVVERO riderivato — verificato in finestra dalle raws
(`validation/sfoundations_raws_2026-08-13/`):

- Il brief cieco (phaseA_problem_brief.md, self-contained, "any
  project-specific document is off-limits") ha prodotto 4 alberi d'attacco
  de-novo: variational 34 / hyperbolic 41 / optimization 32 / propulsion 34
  fork = 141 (phaseB_tree_diff.md, header).
- Il diff Fase B (§3 "theory-layer convergent validations") ha riderivato
  CIECO: il sistema di ottimalità T7/(**') (§3.2); la classe di soluzione
  fitted-front certificata con scoping Li-Yu/Majda (§3.3); la strada di
  esistenza Chenais/uniform-cone (§3.4); il delta-mechanism con la dicotomia
  T3/T4 e la dottrina bound-as-oracle (§3.5); la strada thermo γ(T) a
  tabelle (§3.6); la certifiability-as-priced-constraint 4/4 lenti (§3.7).
- Il diff per-riga del ledger (48 righe, §5): 8 DIVERGENT/CHALLENGED,
  10 CONVERGENT, 11 ENRICHING-only, 6 PARTIAL, 1 CONDITIONAL, e **12 SILENT**
  — SILENT dichiarato nel diff stesso "below the trees' granularity — no
  evidence either way; NOT support" (righe C2 cond., C5, C15, C16, C22,
  C23, C30, C40, C45, C46, C47, C48).
- La Fase D ha portato a convergenza (refuter ladder + probe, phaseD/):
  R22-F centerpiece, formalizzazione mean-swirl, NTF, objdom, deltacarrier,
  crosslowering; in M0: T-DISC/FORCHETTA/T-DCRX/NTF/CLG (memoria
  s-foundations-c4-closed).

Quindi la battuta 2 ha TRE esiti ammessi, ciascuno con la sua ancora:

- **(a) RIDERIVATO-PIENO** — l'argomento è nel perimetro riderivato di Fase
  A/B §3 o portato a convergenza in Fase D: citare il diff del derivatore
  cieco (phaseB_tree_diff.md §riga) o il file phaseD con verdetto.
  Copre il nucleo di: N-A/N-B/N-C/N-D/N-F/N-G-meccanismo/N-H-classe,
  N-E via Fase D (mean-swirl, R22-F).
- **(b) STANCE-DI-FORK** — l'argomento è una scelta del ledger con verdetto
  Fase B CONVERGENT/DIVERGENT/ENRICHING/PARTIAL: citare il verdetto
  per-riga (phaseB_tree_diff.md §1), DICHIARANDO che è una presa di
  posizione a livello di fork dei 4 alberi, non una riderivazione
  dell'implementazione. Copre gran parte delle scelte di N-I.
- **(c) NON-RIDERIVATO** — riga esplicita obbligatoria: *"NON-RIDERIVATO:
  questo aspetto non ha avuto riderivazione agnostica di record"* + QUALE
  ALTRA doppia prova lo copre, con ancora (standard claim-dual-proof).
  Vale per: le 12 righe SILENT del ledger; la certificazione ESEGUITA
  (S-CERT/oracoli/KAT → doppia prova = dual-seed + dual-code GENO + refuter
  S-CERT, memoria fservice-scert); il contratto-dati implementato (→ audit
  stage-A + hypaudit confront_contract.md nelle raws); i numeri
  engine/suite/velocità (→ suite 23/23 con rejector R5, ancora c9bacd9);
  il posizionamento letteratura (→ protocollo litreview a contraddittorio
  simmetrico + REFUTE_CH5); il value case (→ REFUTE_CH6 + panel); la
  storia stessa (→ questo design + refuter di design).
  **MAI fabbricare ancore di Fase A dove non esistono**: se per un
  argomento manca ANCHE la doppia prova alternativa, la riga (c) resta con
  "doppia prova: ASSENTE" e diventa FINDING a registro — un buco onesto,
  non un lint fallito per sempre né un'ancora inventata.

Il lint 5 (§L) è emendato di conseguenza: verifica che battuta 2 sia UNA
delle tre forme CON ancora (o FINDING dichiarato), mai che sia la forma (a).

### §T-§7 POSIZIONAMENTO / CONFORMITY [V2-R4] + standard (§C)

Tre metà FISSE:
- **(a) STRUMENTI**: per ogni tool del nodo, la terna mondo-SOTA (id
  registry) / cosa usiamo / perché. **Clausola di vacuità [V2-R4]**: un §7(a)
  può dichiarare *"NESSUNO STRUMENTO PROPRIO"* con puntatore alla cella
  (ii) FUORI-PERIMETRO della tabella §M (vale per i capitoli di N-N, N-O,
  N-L, N-B: celle N-ii, O-ii, L-ii, B-ii). Il lint 5 riconosce la clausola.
- **(b) SENSO**: i precedenti del tema (RDE + classici) e il gap che il nodo
  occupa, query-bounded.
- **(c) STANDARD DI RIFERIMENTO**: quale asse della conformity map §C
  governa il metodo di questo nodo, con il criterio di conformità e la
  divergenza dichiarata (se c'è). Un §7 senza la metà (c) non passa il
  lint 6.

Ownership: ogni §7 ha UN owner di onda, tabella in §W [V2-R4] — nessun §7
promesso senza writer che lo possiede.

==============================================================================
## §C CONFORMITY MAP — il metodo contro gli standard mondiali

Definizione utente di SOTA (vincolante): *"rispetto alle convenzioni, prassi
e standardizzazioni mondiali"*. Otto assi; sette con LO standard nominato +
criterio di conformità + divergenza dichiarata; l'ottavo con l'ASSENZA
dichiarata. Regola di design: **un claim "SOTA" in qualsiasi capitolo/deck
senza l'asse di questa mappa citato (o senza query-bound esplicito) =
violazione del design** → lint 6 (§L).

| asse del metodo | standard di riferimento | criterio di conformità (il nostro carrier) | divergenza dichiarata |
|---|---|---|---|
| 1. Copertura letteratura | disciplina systematic-review, classe **PRISMA** | query dichiarate + criteri di inclusione + flusso censito: registry 174 id con read-status onesto (L8: READ-INTEGRAL/READ-PARTIAL/UNREAD/WANTED, SCAFFOLD :232-239); claim di assenza SOLO query-bounded NOT-FOUND(q); protocollo litreview a due assi con contraddittorio simmetrico (memoria litreview-verification-protocol) | adottiamo la DISCIPLINA (query+flusso+status), non la checklist 27-item nata per trial clinici; nessun claim di PRISMA-compliance formale |
| 2. Gradazione evidenza | classe **GRADE** (certezza dell'evidenza a livelli) | mappa esplicita delle nostre classi → livelli riconoscibili: THEOREM (prova completa + carrier machine-checked) ≈ certezza alta; THEOREM* (ipotesi dichiarate non tutte scaricate) ≈ moderata; SCHEMA (struttura di prova, gap nominati) ≈ bassa; CONJECTURE/PRACTICE ≈ molto bassa/expert-practice (classi da CLAUDE.md R4); assi letteratura [IO] (fonte letta integrale) / [REP] (riportato, non verificato alla fonte) / [APERTO] (memoria litreview); evidenza di record [ADV] (advisory L7, mai normativa) / raws-RAW (enum status ADVISORY_INDEX, SCAFFOLD :224-230) | GRADE è nato per evidenza clinica: prendiamo la STRUTTURA (livello dichiarato per ogni claim + ragioni di upgrade/downgrade), non i domini clinici |
| 3. Tracciabilità | classe **ECSS** / **DO-178C** (bidirectional trace requirement↔verification) | catena id→nodo→verifica: ogni claim load-bearing ha id nei registri tipizzati (claims/findings/choice/flag, SCAFFOLD §6 REGISTRY MAP :241-253), una casa nell'albero (nodo/cella §M), e un carrier con rejector (R5); i lint xv/xix/xx/xxii/xxiii = i nostri trace-lint machine-checked | nessun audit esterno né certificazione DI standard: adottiamo la CLASSE di disciplina (trace bidirezionale, lint automatici), query-bounded |
| 4. Documentazione | **docs-as-code** + **Diátaxis** | registri YAML machine-linted + M0 = *reference* (normativi); atlas/capitoli = *explanation* (mai normativi contro M0 — regola di record); D6/piani = *how-to* procedurale; PROGRESS = stato vivente ORA/NEXT; storia append-only (SR-10) | Diátaxis usato come mappa dei ruoli-documento, non adottato come rito dei 4 quadranti (nessun tutorial: fuori scopo di un atlas di ricerca) |
| 5. Dati e claim | **FAIR** | Findable: id + indici (ADVISORY_INDEX, CH-REF); Accessible: file testuali nel repo, path di record; Interoperable: YAML tipizzato a schema strict-subset (SCAFFOLD :241); Reusable: provenance completa — nessun numero senza script committato + test + sessione/commit di nascita (R5/R4) | FAIR per un repo di ricerca chiuso: "Accessible" = accessibile all'ente e al team, non open-data pubblico (dichiarato) |
| 6. Deck | **assertion-evidence** | ogni slide = un'asserzione in frase piena + evidenza visiva; il retro-audit dichiarato del deck (commit 1514641: ogni claim-slide camminato all'indietro fino alla sorgente, findings mai ammorbiditi) RAFFORZA lo standard con la verifica d'ancora | — |
| 7. Verifica multi-livello del contenuto | prassi di peer-review avversaria (refuter/panel), classe journal-review | ogni capitolo con REFUTE simmetrico; trittico gate+refuter+sense-review (memoria pipeline-sense-expert-review); dual-proof standard | il "reviewer" è interno e a convergenza, non anonimo esterno: il passaggio esterno resta G5/JPP (dichiarato, non sostituito) |
| 8. Orchestrazione multi-agente | **NESSUNO standard mondiale codificato ESISTE** (claim query-bounded: nessuna convenzione/standardizzazione internazionale nota al cutoff per orchestrazioni find→verify/panel-a-convergenza; query da ripetere a ogni uso nel deck) | le nostre forme (find→verify avversario, panel a convergenza, dual-seed, effort tiering, peso riportato SR-9 — memorie agentic-orchestration-forms / orchestration-weight-sota) = PRASSI INTERNA DICHIARATA | ogni claim su quest'asse è SEMPRE query-bounded e dichiarato tale; mai "standard" senza virgolette |

Conteggio: **7 standard nominati** (PRISMA, GRADE, ECSS, DO-178C,
docs-as-code/Diátaxis, FAIR, assertion-evidence) + 1 assenza dichiarata.
Ogni §7(c) di nodo punta all'asse pertinente; la mappa vive qui (una sola
sorgente), i nodi la citano.

==============================================================================
## §M LA TABELLA PER-CELLA [V2-R1] (BREAK #1 riparato)

Stati ammessi (composizione dei tre primitivi d'ordine utente):
**COPERTA**(dove) · **PARZIALE** = COPERTA(dove) + contratto-residuo ·
**SCOPERTA**(contratto: dove atterra, owner §W) · **F-P** = FUORI-PERIMETRO
(ragione). La tabella È l'ancora del lint 3: i conteggi si RIGENERANO
enumerandola (mai citati da altro documento, SR-12); le doppie
classificazioni v1 (M-ii, O-iii) sono risolte a UNO stato; le celle
etichettate parziali nel testo v1 ma assenti dal conteggio (A-ii, E-iii,
L-i, M-i) sono in tabella col loro stato vero.

| cella | stato | dove / contratto / ragione | owner |
|---|---|---|---|
| A-i | COPERTA | CH1 §1.1 (:30-58) + CH1 §2 | — |
| A-ii | PARZIALE | coperta: CH4 §1.3 (classe spline nel ledger); residuo: confronto `masters_etal_2017`/`lauer_ansell_2025_pas` → CH1 §7(a) | B3 |
| A-iii | PARZIALE | coperta: CH5 §1.1 (il campo consegna CFD); residuo: riga "pin ESIBITO nei CFD P-C phase-locked" (critic 14) → CH5 + scope R20 in CH6 §1.6 | B5 |
| A-iv | PARZIALE | coperta: CH1 §1.1 (novità pin query-bounded); residuo: allineamento scope hardware-vs-CFD (critic 14) | B3 |
| A-v | COPERTA | CH1 §3 | — |
| B-i | COPERTA | CH1 §1.2-1.4 | — |
| B-ii | F-P | ladder = struttura concettuale, non tool; posizionamento in colonna (iii); CH1-§7(a) usa la clausola di vacuità SOLO per questa metà | — |
| B-iii | COPERTA | CH5 §1.1-1.2 (average-then-design, dicotomia D-1) | — |
| B-iv | COPERTA | CH1 §1.3 (quoziente esatto + rung 2) | — |
| B-v | COPERTA | CH1 §3 (PB-2 OPEN) | — |
| C-i | COPERTA | CH2 integrale | — |
| C-ii | SCOPERTA | CH2 §7: adjoint continuo per-fase (first integral f2=−λ2, CH2 §1.2) vs discrete-adjoint AD prevalente; ids: `wanted_hicken_zingg_2014`, `lozano_2018`, `lozano_2019`, `giles_pierce_1997`/`giles_pierce_2000`/`giles_pierce_2001`; perché continuo-prima + dove il discreto rientra (O3.1, G0 :753-774) | B7 |
| C-iii | COPERTA | CH2 §1.8 (bridge P-2, genealogia) + CH5 §1.4 | — |
| C-iv | COPERTA | CH2 §1.3 (shared wall = frase di design) | — |
| C-v | COPERTA | CH2 §3 | — |
| D-i | COPERTA | CH3 §1.1-1.4 | — |
| D-ii | SCOPERTA | CH3 §7: forchetta = error estimation goal-oriented "a mano" vs DWR (`wanted_becker_rannacher_2001`, `venditti_darmofal_2000`, `wanted_fidkowski_darmofal_2011`); perché per-canale con fisica nominata | B3 |
| D-iii | COPERTA | CH3 §1.5 (no-external-referee) + CH5 | — |
| D-iv | COPERTA | CH3 §1.3 (forchetta a 6 canali) | — |
| D-v | PARZIALE | coperta: CH3 §3 (aperti esistenti); residuo: G3 "the only gate whose kill threshold cannot reject" (D6 :783-786, critic 17) → CH3 §3 aperto nuovo + roadmap CH6 | B3+B5 |
| E-i | COPERTA | CH7 (3 piani) | — |
| E-ii | SCOPERTA | CH7 §7 [V2-R6]: mean-swirl/trasporto Γ=R·w posizionato sui CARRIER SURROGATI di record — D6 G5 riga 2.2(f) :803-806, `kraiko_tillyaeva_2015` (genealogia), T-N6-2 free-vortex come termine interno; confronto diretto con `wanted_tillyaeva_1975` = PENDING-PROCUREMENT (status WANTED, paths [], russo [HARD]) con owner; MAI summary del paper assente | B7 |
| E-iii | PARZIALE | [V2-R9] coperta: CH7 §1.4; residuo NOMINATO: il senso-precedenti dell'edificio averaging 2.5-D (cosa fa il campo con medie quasi-1D senza struttura per-fase — ancora CH5 §1.1) → mezza sezione in CH7 §7(b) | B7 |
| E-iv | COPERTA | CH7 §1.3 (centerpiece R22-F) | — |
| E-v | COPERTA | CH7 §3 (S-5F, C51 — decisioni utente) | — |
| F-i | COPERTA | CH8 §1.1-1.5 | — |
| F-ii | SCOPERTA | CH8 §7: parametrizzazione per-settore vs level-set/CAD-based (`lauer_ansell_2025_pas`; `masters_etal_2017`) | B6 |
| F-iii | COPERTA | CH8 §1.3 + CH5 (`jourdaine_2019`, `liu_2022`, `li_xu_lv_yu_zhou_2025`) | — |
| F-iv | COPERTA | CH8 §1.1 (il TIPO è un output) | — |
| F-v | PARZIALE | coperta: CH8 §3; residuo: fase F3 mai nominata (critic 8) → CH8 §3.5 + legenda CH6 | B6+B5 |
| G-i | SCOPERTA | CH8 §1.7 nuovo: i 5 meccanismi M1-M5 con istanze di record (T4=M1, T3=M2, 1-DOF=M3; M0 IV :2982-3005) | B6 |
| G-ii | SCOPERTA | [V2-R7] confronto M4/M5 col mondo RI-SCOPATO: dichiarato NOT-FOUND(q) con il TESTO della query nel §7 di CH8 (deflated continuation; global opt Lipschitz/B&B) — `nocedal_wright_2006_2ed` citato SOLO per il quadro locale, mai come carrier degli oggetti globali; upgrade a confronto pieno SOLO SE l'orchestratore minta righe WANTED pre-W-B (decisione A4, §W) | B6 |
| G-iii | SCOPERTA | claim search-proven DA ESEGUIRE IN ONDA: nessun paper P-A..P-D dichiara meccanismo di globalità (query citata nel testo) | B6 |
| G-iv | SCOPERTA | "ogni Verdict dichiara meccanismo e forza" = la proposta; CH8 §1.7 | B6 |
| G-v | SCOPERTA | C57 NEVER (CH4 Q2) + target M3 unimodalità truncated-plug; CH8 §1.7+§3 | B6 |
| H-i | SCOPERTA | CH1 §1.7 nuovo: tabella per classe di flusso (single-wave→certificato pieno; RPO→PRACTICE; multistabile→CVaR/DD-DRO; caotico→rifiuto onesto + muro [S-GBE]; M0 V :3008-3045) | B3 |
| H-ii | SCOPERTA | strumenti di licensing: flatness monitor, census refresh; CH1 §1.7 | B3 |
| H-iii | SCOPERTA | "il campo non dichiara MAI il regime di validità" → forma di G-iii: query nominata da eseguire in onda, esito NOT-FOUND(q) o refs; CH1 §1.7 + eco CH5 | B3 |
| H-iv | SCOPERTA | il rifiuto onesto come proposta honesty-first (materiale deck); CH1 §1.7 | B3 |
| H-v | SCOPERTA | B-lite = "the cheap exact meter of the rung-2 sweep" → cross-ref in CH3 accanto ai deriver; CH1 §1.7 | B3 |
| I-i | COPERTA | CH4 §1.1-1.4 | — |
| I-ii | PARZIALE | coperta: CH4 §1.3 (choice ledger pesa alternative); residuo: refs sistematiche → CH4 §7(a): TR-Newton segmentato vs SQP/IP (`nocedal_wright_2006_2ed`, `byrd_hribar_nocedal_1999`, `vanaret_leyffer_2026_uno`), rumore (`sun_nocedal_2023_noisy_tr`), passo certificabile (`deuflhard_2011_csm35`, `yamamoto_1986_numermath48`); JAX custom_vjp vs Enzyme (G0 :753-774); MoC vs shock-tracking implicito (`huang_zahr_2022`, `wanted_thakur_nadarajah_2024`); thermo tabulata S11 (`browne_shepherd_sdtoolbox_2018`) vs Cantera-in-the-loop | B4 |
| I-iii | PARZIALE | coperta: ancora CH5 §1.1 (i 4 paper usano CFD+sweep, nessuna catena design-adjoint); residuo: sottosezione del §7 di CH4 (pipeline vs framework ASO) | B4 |
| I-iv | COPERTA | CH4 §1.1 | — |
| I-v | PARZIALE | coperta: CH4 §3; residui: riga suite 23/23 CON incidente dichiarato (ancora c9bacd9, critic 15) in §1.4 + §1.6 nuovo "La velocità come scelta algoritmica" (S25: 100.8→32.1 s, vg 6.6×; ADJUDICATO estensione, non capitolo) | B4 |
| J-i | SCOPERTA | CH9 §1: G1 assoluto (D6 :775); catena O1/O2/O3.1-O3.4; KAT; dual-seed; verdetto S-CERT di record = NON-CERTIFICABILE, 2 P0 (uno riparato in-window; staleness import-closure → F2) + MC8 8/8; C-O33 quantificata | B1 |
| J-ii | SCOPERTA | CH9 §7(a): `yamamoto_1986_numermath48` (N-K per il passo), `shi_xie_xuan_nocedal_2022_fd_interval` (FD interval), DWR (`wanted_becker_rannacher_2001`, `wanted_fidkowski_darmofal_2011`) vs disciplina rejector R5 (tolleranze derivate) | B1 |
| J-iii | SCOPERTA | [V2-R10] forma di G-iii: query NOMINATA da eseguire in onda su "validazione a confronto singolo nel campo" — esito NOT-FOUND(q) o refs; + principio "cross-code agreement ≠ truth" (memoria moc-critical) con gli invarianti indipendenti | B1 |
| J-iv | SCOPERTA | il formato Verdict (contorno+certificati+barre+record oracoli) = proposta; CH9 | B1 |
| J-v | SCOPERTA | staleness → F2; C-O33 aperta (classe di design); CH9 §5-aperti | B1 |
| K-i | SCOPERTA | CH10 §1: D2.4 + audit stage-A (Crocco, completezza, H-I2) + G6 loud-reject + ledger L4 (closure- vs analysis-conditional); U3' PREMISE-OPEN; contact/slip ownership F2a | B2 |
| K-ii | SCOPERTA | [V2-R5] pipeline CFD-to-contract: lineage RI-ANCORATO a D6 :256-263 (concentration-based front extraction + fitted-front) con ECCEZIONE NON-REGISTRY DICHIARATA nel contratto (Gelb-Tadmor e Paciorri-Bonfiglioli: 0 righe registry, grep in finestra; vicino esistente: `wanted_onofri_paciorri_2017_book`); upgrade SOLO SE minted pre-W-B (decisione A4, §W) | B2 |
| K-iii | SCOPERTA | il campo consegna CFD, non contratti-dati (nessun paper P-A..P-D dichiara classe di dati — ancora CH5 §1.1 + critic 14) | B2 |
| K-iv | SCOPERTA | Annex B input taxonomy = la risposta pronta alla domanda ESA "che input serve" (D6 :1133-1134); CH10 + puntatore CH4 §1.2 + CH6 ask | B2 |
| K-v | SCOPERTA | U3' aperto, owner F2a; contratto MAI freezato prima; CH10 | B2 |
| L-i | PARZIALE | coperta: CH6 §1.5 (deciders); residuo: legenda F3 GEOMETRY CLASSES (D6 :214) e F6 (:275) assenti (critic 8) | B5 |
| L-ii | F-P | la spina è governance, non tool; [V2-R11] ASSORBIMENTO DICHIARATO: la SOTA tool matrix D6 §4 :737 ("what the team must actually know") è assorbita dalla colonna (ii) trasversale — ogni riga tematica censisce i PROPRI strumenti | — |
| L-iii | COPERTA | CH6 | — |
| L-iv | COPERTA | CH6 §1.6 (ask) | — |
| L-v | PARZIALE | coperta: CH6 §1.5-1.6; residui: G2 VALUE GATE kill criterion + thrust-stand ~0.5-1% (D6 :776-782, critic 7) → §1.5+Q1; collocazione F4b (critic 18); riga canale paper P-1 + P-2 freeze FIRED 2026-08-11 blocker C1 owner F2 (D6 :91-100, critic 19); + [V2-R11] riga "rischi di programma" ancorata al RISK REGISTER D6 §7 :1093 (o F-P motivata nel capitolo) | B5 |
| M-i | PARZIALE | coperta: CH3 (canale O(St)); residuo: frase di scope esplicita "corrector = perturbazione dello sweep steady" con ancora M0 VI.4bis (memoria periodic-wave-data-scope) | B3 |
| M-ii | F-P | [V2-R1] doppia classificazione v1 RISOLTA a UNO stato: nessuno strumento proprio del corrector — gli strumenti sono quelli della riga I (cella I-ii); assorbimento dichiarato | — |
| M-iii | COPERTA | CH5 §1.5 (linea unsteady, i tre MANDATORY, ponte adjoint) | — |
| M-iv | COPERTA | CH3 | — |
| M-v | SCOPERTA | CH3 §3 aperto nuovo G3/G4 (trigger senza numero, D6 :783-786; G4 decoupling mai nominato — critic 17) + riga roadmap CH6 §1.5 (F5b: trigger derivato come NUMERO, D6 :271-273) | B3+B5 |
| N-i | COPERTA | CH5 integrale (4 metodi, genealogia, threat ledger CT-1..8, harvest) | — |
| N-ii | F-P | riga-senso per eccellenza; gli strumenti del campo sono censiti nella colonna (iii) delle altre righe; CH5 §7(a) = clausola di vacuità con puntatore QUI | — |
| N-iii | COPERTA | CH5 §1.1-1.8 | — |
| N-iv | COPERTA | CH5 §1.6 (gap G14 query-bounded) | — |
| N-v | PARZIALE | coperta: CH5; residui: remark EAP (`kaemming_paxson_2018`, `paxson_miki_2022`; M0 :2526-2539 "the P4 corrector is EAP's missing error bar", critic 6) → CH1 §1.2 + eco CH5; ancora P-C Fig. 21 (critic 11); P-B Fig. 16 + O(10:1) (critic 16); box nomenclatura P-B/p_b/PB-2/Gap B + namespace G (critic 9) → §1.2/§1.8 + legenda CH6 §6 + casa CH-REF | B5+B3 |
| O-i | COPERTA | CH6 §1.1-1.4, §1.7 | — |
| O-ii | F-P | nessuno strumento proprio; CH6 §7(a) = clausola di vacuità [V2-R4] | — |
| O-iii | COPERTA | [V2-R1] doppia classificazione v1 RISOLTA: COPERTA — CH6 + CH5; la metà EAP-metrica vive in N-v (saldatura dichiarata, non assorbimento) | — |
| O-iv | COPERTA | CH6 §1.7 (l'onestà come strategia) | — |
| O-v | PARZIALE | coperta: CH6; residui: PB-2 riconciliato alla forma CH1 (critic 10) → §1.2; hedge sizing single-instance (critic 13) → Q1+§1.4; (G2 → già in L-v) | B5 |
| P-i | SCOPERTA | §6 STORIA in OGNI capitolo col trittico condizionale [V2-R2]; non centralizzabile | B8a/B8b |
| P-ii | SCOPERTA | [V2-R12] la cella che POSSIEDE la governance theory-as-code: registri tipizzati + lint + rejector sulla TEORIA (SCAFFOLD §2/§5: "machine-rejected drift") come STRUMENTO del metodo — atterra in CH9 §7 sottosezione "il metodo come strumento" (con asse §C-3/§C-4) | B1 |
| P-iii | SCOPERTA | come il mondo tiene coerenti corpora di ricerca = gli assi §C-1/-4/-5 (PRISMA-class, docs-as-code/Diátaxis, FAIR); il posizionamento del METODO contro standard vive nella mappa §C, citata dal §7(c) di ogni nodo | orch. |
| P-iv | SCOPERTA | la proposta: dual-proof + riderivazione cieca + refutazione simmetrica come modo di lavorare (memoria claim-dual-proof-standard); §6 template + CH9 §7 | B8+B1 |
| P-v | SCOPERTA | gli aperti del metodo: l'inventario dei rami (c) NON-RIDERIVATO (sottoprodotto del lint 5) = la lista onesta di ciò che non ha seconda derivazione; consegnato in CH-REF | B8+D2 |

### Conteggio (RIGENERATO enumerando la tabella qui sopra — SR-12)

**COPERTE: 31 · PARZIALI: 14 · SCOPERTE: 30 · FUORI-PERIMETRO: 5 — totale
80.** (Per riga: A=2C/3P; B=4C/1F; C=4C/1S; D=3C/1P/1S; E=3C/1P/1S;
F=3C/1P/1S; G=5S; H=5S; I=2C/3P; J=5S; K=5S; L=2C/2P/1F; M=2C/1P/1F/1S;
N=3C/1P/1F; O=3C/1P/1F; P=5S.) Questi numeri SUPERSEDONO il "44/6/30" di v1
(falso tre volte, BREAK #1) e valgono solo insieme alla tabella: il lint 3
non usa MAI questo paragrafo, ricalcola dalla tabella.

==============================================================================
## §CH MAPPA CAPITOLI → NODI (il materiale si rimappa, non si riscrive)

| capitolo | nodi serviti | ruolo |
|---|---|---|
| CH1_formulation_ladder | N-A, N-B + N-H (§1.7 nuovo) | casa di R-I + licensing |
| CH2_averaged_optimality | N-C | casa unica |
| CH3_reduction_physics | N-D + N-M (metà teoria) | casa doppia |
| CH4_machine_choices | N-I | casa unica (+ §1.6 velocità) |
| CH5_literature_positioning | N-N + colonna-senso di TUTTI i nodi | servizio trasversale (iii) |
| CH6_value_honesty_roadmap | N-O + N-L + N-M (metà roadmap) | casa doppia + servizio |
| CH7_averaging_edifice | N-E | casa unica |
| CH8_design_space | N-F + N-G (§1.7 nuovo) | casa doppia |
| CH9 NUOVO certificazione | N-J + P-ii/P-iv (governance §7) | casa nuova |
| CH10 NUOVO contratto-dati | N-K | casa nuova |
| §6 STORIA (in ogni capitolo) | N-P (distribuito) | trasversale |
| CH-REF annex | nessun nodo (servizio) | mappa id→nodo, glossario, legenda, inventario rami (c) |

La spina fisica resta per-capitolo (i file esistono, le refutazioni sono
per-capitolo); la spina LOGICA è l'albero: in W-D l'orchestratore compila la
SPINA-INDICE (un file `ATLAS_TREE.md` in promozione) con, per ogni nodo, i
puntatori alle 8 sezioni nei capitoli serventi. Un nodo a cavallo di due
capitoli (N-M, N-P) dichiara nella spina quale sezione vive dove.

==============================================================================
## §N LA NARRATIVA DELLA RICERCA (ordine di lettura = ossatura deck ESA)

Sette atti (invariati da v1 nella sostanza, ri-etichettati sull'albero):

1. **CONTESTO CAMPO** — N-N: come si fanno oggi gli ugelli per RDE.
   [CH5 §1.1-1.5 + CH1 §1.2-EAP]
2. **GAP** — N-N(iv) + K-iii + J-iii: nessuna riduzione per-fase dichiarata,
   nessun contratto-dati, nessun certificato; NOT-FOUND(q). [CH5 §1.6 +
   CH10 + CH9]
3. **DOMANDA DI RICERCA** — Q0 via N-B + N-F: quando mediare è esatto,
   quanto costa, che topologia seleziona la misura. [CH1 + CH8 §1.1]
4. **METODO** — R-II + R-III: N-C → N-D → N-E → N-I → N-G → N-K → N-J.
   [CH2 → CH3 → CH7 → CH4 → CH8 §1.7 → CH10 → CH9]
5. **EVIDENZA** — N-F(torneo) + N-I(numeri con stage dichiarato) +
   N-J(oracoli 91/91; 23/23 con incidente). [CH8 §1.4 + CH4 §1.4-1.6 + CH9]
6. **ONESTÀ/LIMITI** — N-O + N-H + N-J: Gap A/B; PB-2 non ancora un numero;
   G2 kill; G3 senza numero; rifiuto onesto del caotico; verdetto S-CERT.
   [CH6 + CH1 §1.7 + CH9]
7. **ROADMAP + ASK** — N-L + N-K: deciders, F2→F6 con F3, canale P-1/P-2,
   Annex B "cosa ci serve da voi". [CH6 §1.5-1.6 + CH10]

In una riga: *il campo disegna l'ugello RDE mediando prima e sperando poi;
noi dimostriamo QUANDO mediare è esatto, misuriamo QUANTO costa quando non
lo è, e consegniamo l'ottimo con certificato e contratto-dati — dichiarando
ad alta voce dove il certificato oggi si ferma.*

Nota deck e ARCHI DI CONSUMO A VALLE [V2-R16]: (a) atti 1-3 = sezione
letteratura ordinata dall'utente (plots del campo, extract_figs + citazione
piena, CT-6 sui loro numeri — commit adf50b2/1514641); (b) la
graph-visualization spec (commit cace6db: mappa-decisioni walkable, per-nodo
scelta+alternative+perché+falsificatore) CONSUMA L'ALBERO STESSO — ogni
nodo-domanda porta per template proposta+alternative+falsificatore — con
sorgente di dettaglio CH4 §1.3/§7 + choice ledger; (c) il retro-audit del
deck con ROBUSTNESS VERDICT (commit 1514641: conteggi walked/reduced/
findings nel log di chiusura) È ALIMENTATO dai lint 3/4/6 di §L; (d) il
PONTE B1 (numero "4-13") resta sospeso finché la composizione non è
aggiudicata (critic 2, disposta dall'orchestratore).

==============================================================================
## §D DISPOSIZIONE DELLE 21 RIGHE DEL CRITIC (test di auto-consistenza)

Ogni riga → cella §M / capitolo. BLOCKING: 1-3; MAJOR: 4-11; MINOR: 12-21.

| # | cella §M | disposizione | onda |
|---|---|---|---|
| 1 | J/F (processo) | CH7+CH8 tabelle "Disposizione riparazioni" (22 findings; ALTI: REFUTE_CH8 #1-2, REFUTE_CH7 #2) | W-A |
| 2 | N-v | GIÀ DISPOSTA dall'orchestratore nello storyboard (composizione "4-13" da aggiudicare o kicker riformulato) — A3 verifica | W-A |
| 3 | I-ii | GIÀ DISPOSTA nello storyboard (C13 → forma CH4 W2-R2: 62 TIPIZZATE, 48 aggiudicate) — A3 verifica | W-A |
| 4 | G (riga intera) | CH8 §1.7 nuovo (contratto M1-M5) | W-B.1 |
| 5 | H (riga intera) | CH1 §1.7 nuovo + cross-ref B-lite in CH3 | W-B.1 |
| 6 | N-v/A | CH1 §1.2 (remark EAP accanto a [D-MU]) + eco CH5 | W-B.1 |
| 7 | L-v/O-v | CH6 §1.5 + Q1 (G2 VALUE GATE + thrust-stand) | W-B.1 |
| 8 | L-i/F-v | CH6 legenda F3/F6 + CH8 §3.5 | W-B.1 |
| 9 | N-v/O | CH5 box §1.1 esteso + legenda CH6 §6 + nota stile deck; casa in CH-REF | W-B.1 |
| 10 | O-v | CH6 §1.2 riconciliato alla forma CH1 (+ storyboard C7-ter, canale orchestratore) | W-B.1 |
| 11 | N-v | CH5 §1.2/§1.8 riga Fig. 21 con ancora pC | W-B.1 |
| 12 | D-v | CH3 §1.3(iv) caveat band-underinclusion | W-B.1 |
| 13 | O-v | CH6 Q1 + §1.4 forma CH3 (single-instance) | W-B.1 |
| 14 | A-iii | CH5 riga P-C phase-locked + CH6 §1.6 scope R20 | W-B.1 |
| 15 | I-v | CH4 §1.4 riga suite 23/23 + incidente capture (ancora c9bacd9) | W-B.1 |
| 16 | N-v | CH5 §1.2 Fig. 16; ordine fluttuazioni ancorato o riformulato | W-B.1 |
| 17 | M-v | CH3 §3 aperto G3/G4 + riga roadmap CH6 | W-B.1 |
| 18 | L-v | CH6 §1.5 frase collocazione F4b | W-B.1 |
| 19 | L-v | CH6 §1.6 riga canale paper (P-1 + P-2 freeze FIRED 2026-08-11) | W-B.1 |
| 20 | K-iv | CH10 (casa organica) + puntatore CH4 §1.2 + CH6 ask | W-B.1 |
| 21 | processo | Mini-pass di verifica sulle sole righe [W2-*] di CH1-CH6 (C4 refuter) | W-C |

Esito del test: 21/21 righe trovano cella — invariato.

### [V2-R15] BANCO-UTENTE — mappa domanda → nodo/capitolo (ri-enunciata)

Le 7 domande della milestone (ordine vincolante, verificate dal critic in
finestra critic :52-58):

| domanda utente | nodo | dove | stato |
|---|---|---|---|
| "fixed (L,eps): entità della differenza?" | N-B/N-D | CH1 Q1 (vacuità endpoint, shared-wall, +0.51% con caveat, PB-2 OPEN) | COPERTA |
| "se P-B ottimizza su medie, cosa portiamo?" | N-B/N-N | CH1 Q2; CH5 Q2 + deck 1 | COPERTA |
| "cosa perde il per-fase vs 3D e come tocca l'ottimo?" | N-D/N-E | CH3 integrale; CH7 Q3 | COPERTA |
| "come emerge il profilo ottimo / categorie?" | N-F | CH8 (capitolo dedicato) | COPERTA |
| "P-B vs p_b nomenclatura" | N-N | critic riga 9 → CH5 box + legenda CH6 + CH-REF | DISPOSTA (W-B.1) |
| "scaletta descrittiva + decisioni pendenti S-5F, C51" | N-E | CH7 §1.4, Q2, §3 | COPERTA |
| "PB-2: quando e come" | N-B/N-L | critic riga 18 → CH6 §1.5 collocazione F4b (il QUANDO relativo) | DISPOSTA (W-B.1) |

==============================================================================
## §W PIANO D'ESECUZIONE EMENDATO (onde, ownership, effort, pesi)

Regole standing: connessione artefatti (ogni brief nomina stadio di
confronto + arco di consumo), SR-9 (shape/round/token nel log), artefatti su
file subito, resume-non-relaunch, NIENTE installazioni, SR-12 (conteggi in
finestra), Fable ovunque (memoria model-pinned).

**EFFORT POLICY (dichiarata, vincolante):** ogni slot di GIUDIZIO (writer,
refuter, historian, verifier) = **INHERIT del session max — NESSUN
override**; slot MECCANICI (lint-grep, indice-ancore) = effort ridotto CON
DICHIARAZIONE esplicita nel log SR-9. Nessun altro caso.

**FILE-DISGIUNTI (rigoroso):** in ogni round, ogni file ha ESATTAMENTE un
writer; nessun agente edita un file che un altro agente della stessa onda
ha aperto in scrittura. La violazione v1 (B8 concorrente coi writer) è
riparata: lo storico scrive in un ROUND SEPARATO [V2-R3].

### Onda W-A — RIPARAZIONI + PRE-REQUISITI (gate: BLOCKING a zero + puntatori risolti)
- A1 (writer, CH7): applica i 12 findings REFUTE_CH7 + tabella Disposizione.
- A2 (writer, CH8): 10 findings + tabella (ALTI #1-2 con aggiudicazione
  esplicita, non softening).
- A3 (verifier): righe critic 2-3 davvero disposte nello storyboard (diff
  contro STORYBOARD.md) — esito nel log.
- A4 (orchestratore, decisione a registro) [V2-R5][V2-R7]: per le 4 ref
  fuori registry (Gelb-Tadmor, Paciorri-Bonfiglioli, deflated-continuation/
  Farrell, Lipschitz-global) UNA di: mint righe WANTED con owner PRIMA di
  W-B, oppure conferma del ri-scope già scritto nelle celle K-ii/G-ii
  (eccezione-D6 / NOT-FOUND(q)). La decisione va nel log di chiusura onda.
- A5 (slot meccanico, effort ridotto DICHIARATO) [V2-R13]: PRE-PASS
  INDICE-ANCORE per lo storico — grep dei blocchi amendment/supersession di
  M0 + intestazioni LOG di PROGRESS_ARCHIVE + `git log --oneline` filtrato
  + estratto verdetti phaseB_tree_diff §1/§3 + lista file phaseD/ → un file
  `HISTORIAN_INDEX.md` nelle raws (input di B8a/B8b).
- Peso: 3 slot giudizio + 1 meccanico + orchestratore, ~150-220k token.

### Onda W-B.1 — WRITER (estensioni + capitoli nuovi; 7 slot, file-disgiunti)
| slot | file (esclusivi) | mandato (sezioni possedute) |
|---|---|---|
| B1 | CH9 (nuovo) | N-J template completo (§1-§5, §7 con P-ii governance [V2-R12], §8); celle J-i..J-v |
| B2 | CH10 (nuovo) | N-K template completo; celle K-i..K-v (K-ii nella forma [V2-R5]) |
| B3 | CH1 + CH3 | CH1 §1.7 (riga H intera) + EAP §1.2 + **CH1 §7 [V2-R4: owner ESPLICITO]** (A-ii residuo); CH3 §3 G3/G4 + caveat critic 12 + cross-ref B-lite + scope M-i + **CH3 §7-DWR [V2-R4: nominato nel brief]** (D-ii) |
| B4 | CH4 | §1.6 velocità + riga 23/23 (I-v) + puntatore Annex B + **CH4 §7** (I-ii/I-iii — la più carica di refs) |
| B5 | CH5 + CH6 | tutte le righe N-v/L-v/O-v/A-iii (critic 6-11, 13-14, 16-19) + clausole di vacuità §7(a) di CH5/CH6 [V2-R4] |
| B6 | CH8 | §1.7 M1-M5 (G-i..G-v, G-ii nella forma [V2-R7]) + §3.5 F3 + **CH8 §7 parametrizzazione [V2-R4: nel brief]** (F-ii) |
| B7 | CH2 + CH7 | CH2 §7 (C-ii); CH7 §7 nella forma [V2-R6] (E-ii surrogati + PENDING-PROCUREMENT) + residuo E-iii [V2-R9] |
- Vincoli per ogni writer: ogni ref = id VERBATIM del registry (forme esatte
  come in §M [V2-R5]); ogni claim "il campo non fa X" = search-proven con
  query citata nel testo; classi di rigore dichiarate; §7 con metà (c)
  standard (§C).
- Peso: 7 slot giudizio × 1 round (+ risposte puntuali), ~450-600k token.

### Onda W-B.2 — STORICO (round separato DOPO l'atterraggio di W-B.1) [V2-R3][V2-R13]
- B8a (historian): §6 STORIA di CH1, CH2, CH3, CH4, CH7.
- B8b (historian): §6 STORIA di CH5, CH6, CH8, CH9, CH10.
- File-disgiunti tra loro e temporalmente disgiunti dai writer (round dopo);
  input comune: HISTORIAN_INDEX.md (A5) — strategia di lettura dichiarata:
  indice prima, aperture mirate poi, niente re-read (context-discipline).
- Mandato: trittico condizionale [V2-R2] — esito (a)/(b)/(c) per argomento
  con ancora; ramo (c) con doppia prova alternativa o "doppia prova:
  ASSENTE" = FINDING; MAI ancore fabbricate. L'inventario dei rami (c)
  viene consegnato come lista a parte per CH-REF (P-v).
- Peso: 2 slot giudizio, budget PROPRIO ~160-240k token (riparazione della
  sottostima v1).

### Onda W-C — REFUTAZIONE (simmetrica; 5 slot)
- C1-C3 (refuter): REFUTE_CH9, REFUTE_CH10, REFUTE delle sezioni nuove nei
  capitoli estesi (campione 100% delle righe load-bearing).
- C4 (refuter): mini-pass righe [W2-*] di CH1-CH6 (critic 21).
- C5 (refuter §6/§7): cammina le STORIE (ancora per ancora, INCLUSA la
  correttezza del ramo scelto (a)/(b)/(c) contro le raws Fase A/B/D) e i
  POSIZIONAMENTI (ogni id esiste VERBATIM nel registry ed è pertinente;
  ogni §7(c) cita l'asse §C giusto).
- Disposizione findings nella STESSA onda (tabelle per capitolo).
- Peso: 5 slot giudizio × 1-2 round, ~250-400k token.

### Onda W-D — LINT + PROMOZIONE
- D1 (slot meccanico, effort ridotto DICHIARATO): i 6 lint di §L, con
  comandi eseguiti in finestra (niente installazioni).
- D2 (orchestratore): CH-REF compilato DALL'esito del lint 1 + inventario
  rami (c) da B8; SPINA-INDICE `ATLAS_TREE.md` (nodo → puntatori alle 8
  sezioni); promozione a docs/atlas/ con commit per pathspec espliciti;
  log R3 con shape/round/token per onda (SR-9).
- Peso: 1 meccanico + orchestratore, ~80-120k token.

Totale stimato: ~1.1-1.6M token, 5 round in 4 onde, 18 slot agente.

==============================================================================
## §L CRITERI DI COMPLETAMENTO (i 6 lint) + FALSIFICATORI DEL DESIGN

1. **Lint-registri**: ogni id dei registri di programma citato nei capitoli
   → puntatore a capitolo in CH-REF, o riga FUORI-PERIMETRO con ragione;
   comando misurato in finestra (SR-12).
2. **Lint-manifest** [V2-R14]: FILE_MANIFEST.csv (826 righe) con REGOLA
   BULK dichiarata — una riga di disposizione PER DIRECTORY-CLASSE per
   __pycache__/bytecode (~61 righe), raws voluminose (es. sfoundations,
   280 righe), reports; disposizione per-file SOLO per docs/src/tests/
   validation-advisory. Zero righe orfane sotto questa regola.
3. **Lint-matrice** [V2-R1]: ancorato ALLA TABELLA §M, mai a un numero:
   per ogni riga-tabella — COPERTA: l'anchor ESISTE (grep); PARZIALE: il
   residuo è disposto (edit atterrato o FINDING); SCOPERTA: 0 a fine W-C;
   F-P: ragione presente. I conteggi si RICALCOLANO enumerando la tabella.
4. **Lint-critic**: 21/21 righe con disposizione ESEGUITA (BLOCKING
   risolte, MAJOR con riga-capitolo o declinazione a registro, MINOR
   almeno triage nel log); solo qui il verdetto INCOMPLETA-CON-LISTA si
   ribalta.
5. **Lint-template** [V2-R2][V2-R4]: ogni nodo N-A..N-P → 8 sezioni
   presenti nei capitoli serventi (spina-indice compilabile); ogni §6 =
   trittico con battuta 2 ∈ {(a) RIDERIVATO-PIENO, (b) STANCE-DI-FORK,
   (c) NON-RIDERIVATO} CON ancora — il ramo (c) senza doppia prova
   alternativa = FINDING a registro (MAI fabbricazione, MAI fail-forever);
   ogni §7(a) ≥ 1 id per strumento O clausola di vacuità con puntatore
   alla cella F-P; ogni §7 porta la metà (c) standard.
6. **Lint-conformity** [NUOVO, §C]: ogni occorrenza di "SOTA" (e claim
   equivalenti "state of the art / migliore pratica mondiale") nei
   capitoli e nel deck → o cita l'asse+standard della mappa §C, o è
   query-bounded con query citata; violazione = FINDING. Alimenta i
   conteggi del retro-audit del deck [V2-R16].

**Falsificatori del design stesso** (disciplina doubts-to-convergence — la
matrice e l'albero sono CLAIM, non premesse):
- (F-des-1) un writer W-B trova un aspetto del perimetro senza riga di
  matrice → matrice FALSIFICATA: stop onda, emenda §M a registro, lint 3
  riparte.
- (F-des-2) il check bidirezionale albero↔matrice fallisce (cella senza
  sezione di nodo, o contenuto di nodo senza cella) → design FALSIFICATO:
  stesso trattamento.
- (F-des-3) il lint 5 risulta INSODDISFACIBILE per un capitolo (un ramo (c)
  il cui argomento non ha NESSUNA doppia prova esistente né dichiarabile)
  → non si fabbrica: FINDING + decisione utente al confine di sessione.

==============================================================================
## §F DISPOSIZIONE DEI 16 FINDING DEL REFUTER (tabella finale)

| # | classe | marcatore | disposizione in v2 | stato |
|---|---|---|---|---|
| 1 | BREAK | [V2-R1] | tabella per-cella 80 righe in §M con stati espliciti; conteggi rigenerati per enumerazione (31/14/30/5); doppie classificazioni M-ii/O-iii risolte a UNO stato; celle A-ii/E-iii/L-i/M-i in tabella; lint 3 ancorato ALLA tabella, mai a numeri | APPLICATA |
| 2 | BREAK | [V2-R2] | §T-§6: battuta 2 CONDIZIONALE a tre esiti (a)/(b)/(c) col ramo "NON-RIDERIVATO: questo aspetto non ha avuto riderivazione agnostica di record" + doppia prova alternativa; perimetro Fase A/B/D VERIFICATO in finestra dalle raws (4 alberi/141 fork; §3 diff; 12 righe SILENT; phaseD); lint 5 emendato; fabbricazione vietata (F-des-3) | APPLICATA |
| 3 | REPAIR | [V2-R3] | B8 → onda W-B.2, ROUND SEPARATO dopo l'atterraggio dei writer; split B8a/B8b su gruppi di capitoli disgiunti; file-disgiunti dichiarati regola d'onda | APPLICATA |
| 4 | REPAIR | [V2-R4] | ownership §7 ESPLICITA per tutti i 10 capitoli (tabella W-B.1: CH1§7→B3, CH3§7→B3 nominato nel brief, CH8§7→B6 nel brief, CH2/CH7→B7, CH4→B4, CH9→B1, CH10→B2, CH5/CH6→B5 via clausola); clausola di vacuità §7(a) nel template + riflessa nel lint 5 | APPLICATA |
| 5 | REPAIR | [V2-R5] | id corretti VERBATIM ovunque (§M): wanted_hicken_zingg_2014, wanted_becker_rannacher_2001, wanted_fidkowski_darmofal_2011, masters_etal_2017, wanted_thakur_nadarajah_2024 + forme esatte estese (nocedal_wright_2006_2ed, byrd_hribar_nocedal_1999, sun_nocedal_2023_noisy_tr, vanaret_leyffer_2026_uno, deuflhard_2011_csm35, yamamoto_1986_numermath48, shi_xie_xuan_nocedal_2022_fd_interval, huang_zahr_2022, lauer_ansell_2025_pas, venditti_darmofal_2000 — grep in finestra); Gelb-Tadmor/Paciorri-Bonfiglioli (0 righe): K-ii ri-ancorata a D6 :256-263 con eccezione dichiarata, upgrade solo su mint A4 | APPLICATA |
| 6 | REPAIR | [V2-R6] | cella E-ii: carrier surrogati di record (D6 G5 2.2(f), kraiko_tillyaeva_2015, T-N6-2) + confronto diretto wanted_tillyaeva_1975 = PENDING-PROCUREMENT con owner; mai summary del paper assente | APPLICATA |
| 7 | REPAIR | [V2-R7] | cella G-ii ri-scopata: NOT-FOUND(q) con testo query nel §7 CH8; nocedal_wright_2006_2ed solo per il quadro locale; upgrade solo su mint A4 (WANTED deflation/Lipschitz-global) | APPLICATA |
| 8 | GAP | [V2-R8] | preambolo: L7→riga J (+CH-REF), L8→riga N (+lint-registri), L9→FUORI-PERIMETRO motivato (metà metodo → N-P via R12) — con ancora SCAFFOLD :218-253 letta in finestra | APPLICATA |
| 9 | GAP | [V2-R9] | cella E-iii: residuo NOMINATO (senso-precedenti dell'edificio averaging vs medie quasi-1D del campo) con contratto CH7 §7(b), owner B7; entra nella tabella §M | APPLICATA |
| 10 | GAP | [V2-R10] | cella J-iii nella forma di G-iii: query nominata da eseguire in onda, esito NOT-FOUND(q) o refs (mai asserzione non ancorata) | APPLICATA |
| 11 | GAP | [V2-R11] | L-ii: assorbimento tool-matrix D6 §4 :737 DICHIARATO nella colonna (ii) trasversale; L-v: riga "rischi di programma" ancorata a D6 §7 :1093 (o F-P motivata nel capitolo) | APPLICATA |
| 12 | GAP | [V2-R12] | cella P-ii possiede la governance theory-as-code (registri+lint+rejector come proposta di metodo); atterra in CH9 §7 sottosezione, owner B1; assi §C-3/§C-4 la posizionano | APPLICATA |
| 13 | REPAIR | [V2-R13] | pre-pass HISTORIAN_INDEX.md (A5, slot meccanico dichiarato) + split B8a/B8b con budget proprio 160-240k + strategia di lettura dichiarata nel brief | APPLICATA |
| 14 | NOTE | [V2-R14] | lint 2 con regola BULK per directory-classe (pycache/raws/reports); per-file solo docs/src/tests/validation-advisory | APPLICATA |
| 15 | NOTE | [V2-R15] | mappa banco-utente ri-enunciata in §D: 7 domande → nodo/capitolo/stato (5 COPERTE con anchor, 2 DISPOSTE via critic 9/18) | APPLICATA |
| 16 | NOTE | [V2-R16] | nota deck §N estesa: graph-viz spec consuma l'ALBERO (per-nodo scelta+alternative+perché+falsificatore) + CH4 §1.3/§7 + choice ledger; retro-audit ROBUSTNESS VERDICT alimentato dai lint 3/4/6 | APPLICATA |

Fine di ATLAS_RESEARCH_DESIGN_v2.md — supersede v1; le onde partono da §W.
