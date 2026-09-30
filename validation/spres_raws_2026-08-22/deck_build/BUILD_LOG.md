# BUILD_LOG — S-PRES sessione 3, Blocco 1 (authoring deck)

Log di build corrente (checkpoint di continuità — riprendibile da qui +
SESSION2_LOG + STORYBOARD_v3). Finestra: 2026-08-23. HEAD apertura =
060c1a0 (quota suite S2 23/23 PASS 434 s EXIT 0 nel log: confine pulito).

**Stadio di confronto**: STORYBOARD_v3.md v3.1 (APPROVATO al gate S2) +
GUARD_CHECKLIST 18 + CRITIC_FINALE note FD-1/2/3/5 + decisione twin
PB-2 = (b) forma onesta (gate S2, di record) + patto di stile (b) E1-E7
(STORYBOARD.md v1 §patto) + fix Heister 1-9 (v1 §migliorie) + vincoli
DERISK (graph_derisk/).
**Arco di consumo**: SPRES_deck_v1.pptx (deliverable Blocco 1) →
retro-audit Blocco 2 via workflow (CKP-S2-2) → loop utente → milestone.

## VINCOLI DI SESSIONE (di record)
- project_build = READ-ONLY (ordine utente 2026-08-23 in-window):
  tutti gli artefatti nuovi vivono in QUESTA repo, sotto deck_build/.
  decklib/extract_figs/eqs = idiomi letti e replicati qui, mai editati là.
- GENO/ = read-only (PDF letti per i crop Humphreys/Rao; mai scritture).
- Env pinnato: python-pptx 1.0.2, PIL 12.2, matplotlib 3.10.8,
  pdftoppm 24.04, pymupdf 1.28 — NIENTE installazioni.
- Template deck: reference_presentations/ppt_Heister.pptx (18 slide,
  16:9, 1 master / 2 layout; probe integrale in HEISTER_PROBE.txt).
- Render QA: LibreOffice headless (soffice) + pdftoppm → PNG per
  verifica visiva; PowerPoint presente sul sistema (riserva).

## DECISIONI DI AUTHORING DICHIARATE
- **A12 = 2 slide fisiche (A12a=H8, A12b=H9)** — clausola esplicita
  storyboard v1 A12 ("se la fusione compromette leggibilità → restano
  2 slide, decisione all'authoring dichiarata"): misurato sui render
  (heister-08/09.png) 3+3 plot densi con label d'asse già al limite;
  6 pannelli su una slide violerebbero leggibilità a 3 m (criterio (c)
  Blocco 2). Main deck fisico = 51 slide; il conteggio-storyboard 50
  resta l'unità di join (A12 = coppia dichiarata). Il minuto è
  recuperato sul pace A14-A20 (già 1'/slide nel budget v3.1).
- **Twin PB-2 = (b)** applicata in spec: C7-ter porta "macchina pronta,
  prima campagna della fase che apre ora"; card twin di C17 = "prima
  campagna F2"; C17-bis riga (1) risolta a (b) — nessuna decisione
  aperta residua sul twin nel deck.
- **Note critic applicate in spec**: FD-1 (A6: "correttore P4" solo in
  nota; asserzione = "la barra d'errore mancante è ciò che il nostro
  programma costruisce"); FD-2 (C2: "i quattro studi che vedremo");
  FD-3 (nota relatore C5 glossa "truncated plug"/"working variable");
  FD-5 (C7-ter "numerical test bench, with rejecting checks"; C17-pre
  back-pointer parlato ai tre risultati C8/C9/C10).
- **C13-val**: brick2_profiles_record.png usata AS-IS (figura di
  record S18 [X-TOCV]); restyling leggero rimandato solo se il QA
  visivo lo impone senza rigenerazione (il carrier del PNG è di
  record; nessuna rigenerazione fuori contratto).
- FIX HEISTER (1-9) implementati alla build: (1) footer residuo "HEM
  modeling..." (vive nel gruppo footer di ogni slide) rimosso; (2)
  contatori unici N/51 rigenerati; (3) master ripulito (M. Fiore /
  Modular Aerospike / N/17); (4) A15 heading nativo con Λ da
  strip-eq; (5) A14 text-box off-canvas ("Oval 465" a x=14.37")
  rimossa (contenuto = nota di dettaglio, migrata nelle note
  relatore); (6) Bellenoue fix su A3; (7) note relatore per TUTTE le
  slide; (8) image5/18/19/21 marcate "Group/collaboration material";
  (9) card open-research-lines con puntatore alla sezione.

## ARRICCHIMENTI DICHIARATI IN AUTHORING (user catch, 2026-08-23)
- **C5 ← Harroun base-pressure RDE-vs-steady**: user catch in-window —
  il dato di record (Harroun-Heister-Ruf 2021 pp. 666-667: base 0.59 atm
  detonation-wave CFD vs 0.95 atm constant-pressure a pari portata,
  ~8× base drag, 5 hot-fire sul ramo detonation; BPH_c4:79-92,
  H21-F12/F13, commit b3da86d) NON era consumato da alcuna slide
  sull'asse base-pressure (il join C5 di storyboard = CH5-feed-8 +
  CH8-feed-7 non lo portava). RIPARATO: bullet on-slide C5 esteso +
  script/note con caveat vincolante configuration-dependent (Schwer
  AIAA 2018-4968 counter-finding; nozzleless ≠ truncated plug senza
  etichetta di analogia, R8). Il retro-audit Blocco 2 lo troverà
  dichiarato qui e nella nota della spec.

## INCIDENTE QUOTA (2026-08-23)
- Agente graph-renders TERMINATO da limite di spesa mensile API DOPO
  aver prodotto tutti i 13 render + script + JSON assert-gated; QA
  visivo completato dall'orchestratore in-sessione (stesso modello,
  nessun downgrade): L0 e stage-6a PULITI; fix applicato = etichette
  L0 in inglese ("choices", takeaway tradotto) + re-render 13/13.
  GRAPH_RENDER_NOTES.md scritto dall'orchestratore (l'agente è morto
  prima). RISCHIO NOMINATO per Blocco 2: il workflow multi-agente
  ratificato (CKP-S2-2) può essere bloccato dallo stesso limite —
  decisione utente richiesta prima del Blocco 2 (alzare il limite vs
  esecuzione sequenziale in-sessione con deviazione dichiarata).

## GRAFO: VARIANTI-SLIDE vs DEVELOPER-GRADE (pin utente 2026-08-23)
- User pin in-window: i render graph/ densi = utili da grafo-sviluppatore,
  troppo pesanti in presentazione. Lettura di record CONCORDE: v3.1
  C13 [NOTE] ordina "tally MAI on-slide" (guardia 18) e i render DERISK
  portano tally/legenda numerica/id C-interni → ammessi SOLO nel backup
  (walkable graph promise D1-D8). DECISIONE: main deck consuma varianti
  ALLEGGERITE (render_graph_slide_variants.py → L0_slide / stage6_slide /
  stage45_slide: niente numeri di tally, niente id interni, card in
  lingua parlante, max 6-8 card); backup consuma i render integrali.
  Join storyboard invariato (C13=L0, C14=st.6, C15=st.4-5, D1-D8=full).
- Limite di spesa RIALZATO (utente): Blocco 2 torna alla forma workflow
  ratificata CKP-S2-2.

## CKP-S3-1 (utente, 2026-08-23, VINCOLANTE) — REGISTRO SLIDE MAGRE
Verbatim (estratto): "vedo slide troppo piene, troppo complesse, devi
rispettare lo stile sota, e lo stile di presentazione delle slide di
heister precedenti e migliorarlo anche in stile sota, ma non sono
ammesse slide troppo cariche di parole, di parole stile llm tipo
tracherous o simili. Questo è fondamentale".
LETTURA DI RECORD: (i) densità = stile Heister migliorato — titolo +
2-4 bullet CORTI (≤ ~15 parole) + evidenza visiva dominante; target
~35 parole nette/slide, cap 60 (card mandate ≤100); la prosa vive
nello script/note relatore, mai on-slide; (ii) BANDITE parole di
colore da LLM/di processo interno on-slide: treacherous, "buys you",
"not lying", "honest death", "says NO", metafore da tribunale
(convicted/exonerated → plain engineering); titoli-asserzione ≤ ~10
parole. Cablaggio: riscrittura on-slide di TUTTE le slide C + A2/A4-A6
(note INVARIATE — la provenance resta); lint build esteso (parole
bandite + bullet >20 parole = warn, cap slide abbassato); consumatore:
comms review Blocco 2 criterio (c)/(k).

## CKP-S3-2 (utente, 2026-08-23, VINCOLANTE) — LOOP UTENTE BLOCCO 1, ONDA 1
Ordini sul deck costruito (v1): (1) A2: niente minuti per sezione;
niente ripetizione dell'introduzione del gruppo (la fa meglio la
vecchia Research Roads A3); niente focus ugelli nell'introduzione →
A2 = pura agenda + preview delle richieste; (2) A6 (averaging/EAP) nel
primer è senza nesso ("perché parli subito di averaging?") → SPOSTATA
dopo il ponte B1, come cerniera verso la sezione ugelli (il posto dove
il nesso è immediato: "il campo disegna su medie; mediare QUI è
delicato"); (3) revisione di senso/nesso di tutte le slide → passata
di raccordo sugli script (ponti parlati alle cuciture) + il Blocco 2
ri-audita la consecutio sull'autorato. DEVIAZIONE DICHIARATA dallo
storyboard v3.1 (A2 mini-mappa CON minuti; A6 = primer 3): decisione
utente al loop, prevale sul v3.1; join table invariata (gli id A2/A6
restano, posizione/contenuto emendati e dichiarati qui).

## CKP-S3-3 (utente, 2026-08-23, VINCOLANTE) — GRAFI → SPIEGAZIONE DEL METODO
I grafi (anche ridotti) non comunicano e sanno di LLM. Le slide C13-C15
devono SPIEGARE il modello: quale funzionale, perché l'adjoint, quale
ottimizzatore, obiettivo di ogni fase — chiaro, mai cervellotico.
CABLAGGIO: C13 = method-flow diagram (fig_method_flow: dati→famiglia
per-fase→funzionale J→solve per fase→adjoint=gradiente esatto→TR-Newton
→certifica, con loop di iterazione); C14/C15 = card in lingua piana sui
perché; grafi densi SOLO backup D1-D8 (valore da sviluppatore,
riconosciuto dall'utente). Varianti leggere L0_slide/stage*_slide
DISMESSE dal main (restano su disco per il backup/riuso).

## CKP-S3-4 (utente, 2026-08-23, VINCOLANTE) — TAGLIO SLIDE
"Troppe slide: tagliare mantenendo il senso profondo del metodo,
dell'idea e di ciò a cui può portare." Proposta orchestratore (da
riconciliare col verdetto spine-wave): 51→~44-45 main; tagli via
cut-list DICHIARATA (mai silenzio): C2/C12/C15 → backup con riga
residua; C17-bis → fusa in C18; C3-bis → fusa in C3; C13-pre → fusa
nel C13 method-flow. Cuore intoccabile: C4, C7, C7-bis, C7-ter, C8,
C13-val, C16-bis, C17, C18.

## ONDA NARRATIVA (workflow, 2026-08-23) — CONSUMATA
Shape: workflow 3 agenti sequenziali (proposer → refuter-ESA → judge-
repair), ~388k token, 157 tool use, 26 min [SR-9]. Artefatti:
NARRATIVE_SPINE_v2.md (convergiuta, disposition 24/0) + SPINE_ATTACK.md
(7 CRIT / 8 MAJ / 9 MIN). ESITO: arco REGGE; 1 ponte rotto trovato
(36→37) sanato da MOVE-1; TUTTI i 24 finding APPLICATI e verificati sul
render: F-1 (violazione CKP-S3-1 su C19: honest-death→stop criterion),
F-2 (6-vs-8 stadi: fig-note + firma C19 = method-flow), F-3 (tabella
onestà backup COSTRUITA), F-4 (C18 = 3 card vere; ladder → backup D-L),
F-5 (C1 residuo-C2 liberato dal footer), F-6 (fig Rao RIETICHETTATA:
relabel_c13val.py, dati intatti, id interni → note), F-7 (heading A15
soppresso: header host resta), F-8/F-9 (sweep "we say so"/"phase/owner/
window" → lingua ingegneri), F-10 (teorema C7-bis promosso, bold),
F-11 (MOVE-2 + frecce d'ordine su C17 + C17-pre a 2 bande), F-12/F-13
(riletture ostili disinnescate; scope audit in card+script), F-14
(C8-bis headline bullets), F-16..F-23 (question emphasis B1, gloss EAP,
punch-card con formula, C5 snellita, banda C7-ter, "affordable",
maiuscole, miniatura leggibile), F-24 (manifest già coerente).
RIORDINI DI RECORD (walk combinato verificato dal refuter): 35..45 =
C10→C13→C14→C13-val→C16→C16-bis→C11→C17-pre→C17→C18→C19 (bonus weld:
scala-Rao in C11 dopo il benchmark Rao). MERGES vs storyboard v3.1
(deviazioni dichiarate, F-24/MOVE-5): C2→C1, C3-bis→C3, C12→C11,
C13-pre→C13, C17-bis→C18, C15→backup; A6 post-B1; A2 agenda.

## FINDING F-ATLAS-1 (user catch 2026-08-23, source-verified, PENDING MINT a R3)
CH5 §1 (docs/atlas/CH5_literature_positioning.md:149-151) elenca
"quattro istanze" della dicotomia istantaneo-vs-medio; alla fonte DUE
delle quattro sono transient-vs-STEADY-COMPANION, non medio temporale:
- P-C Fig. 10 caption verbatim (pdf p.9): "Mach numbers ... for
  transient (left) and reference steady states (right)";
- P-B Fig. 14 caption verbatim (pdf p.9): "... nozzles with different
  spike lengths: steady (left) and transient (right)".
P-A Fig.7-vs-9 e P-D Fig.9-vs-4 reggono (P-D Fig.4 = "Time-averaged
exhaust flow structure" verbatim). CONSUMO DECK: C1 riparata (caption
onesta + bullet "a third field exists: the steady state the field
designs on"); nessun claim di record cade (la distinzione transient/
steady-companion è già la spina di C4). MINT: riga findings a chiusura
R3 (atlas FROZEN: modifica = finding, mai edit in-window), lint registri
da ri-eseguire alla mint.

## ===== CKP-S3-5 (utente, 2026-08-23) — ORDINI APERTI PER LA SESSIONE 4 =====
Ordini utente arrivati al confine di sessione, DA ESEGUIRE in apertura S4
(nessuno abbozzato a metà — stato build VERDE, 67 slide, lint 0):
(a) [FATTO in-window] C4/slide-25: scope Fig.13 corretto alla fonte —
    caption verbatim "Comparison of thrust coefficients between the
    transient and reference steady states"; contesto verbatim: "the
    thrust coefficients of FIVE ADJUSTMENT LOCATIONS [cowl/spike] are
    compared" → on-slide ora "the ranking of five cowl/spike settings
    inverts"; caption slide aggiornata.
(b) SWEEP DEADLINE INTERNE on-slide (utente: "troppi riferimenti a
    deadline che ci siamo dati internamente"): rimuovere da TUTTE le
    slide "September milestone", "starting September", "campaign
    starting now — September" (C7-ter banda, C17 card-1 window, C18
    card-2 WHEN) → solo ordine relativo ("first campaign", "after the
    residual measurement", "now/next"). Le date restano nelle note.
(c) NUOVA SLIDE "What is an adjoint" (utente: "definizione di adjoint
    e cosa è, come ottimizziamo tramite adjoint e quale è l'obiettivo"):
    prima di C13, linguaggio da primo incontro: obiettivo = spinta
    ciclo-mediata J del contorno condiviso; serve dJ/d(forma) per MOLTI
    parametri; differenze finite = N+1 soluzioni; adjoint = 1 forward +
    1 backward → TUTTE le derivate; poi Newton trust-region sale.
    Visual: confronto di costo naive-vs-adjoint (schema semplice).
(d) SLIDE 34 (C9 same-pressure-different-thrust): "non si capisce
    assolutamente" → rifare visual (due ingressi con STESSO manometro,
    swirl diverso, spinta diversa — cartoon, non schema astratto) +
    bullet piani ("misura solo la pressione all'ingresso: due flussi
    identici al manometro danno spinte diverse").
(e) C16-bis (racconto audit ostile): utente — "parli di audit...
    dettagli di come abbiamo proceduto, proprio ciò da evitare" →
    RIMUOVERE il racconto-processo dal main deck; l'onestà si mostra
    col CONTENUTO (la tabella errori C11 che segue). Decisione di
    destinazione (backup vs kill con residuo in C11/C15-backup) da
    prendere in S4 CON l'utente; cut-list dichiarata, mai silenzio.
(f) PASSATA DI COMPRENSIBILITÀ slide 25→45 col metro utente: "cosa
    facciamo all'atto pratico" — spiegare, non elencare; zero lingua
    LLM/progetto residua; "non siamo a convergenza per comprensibilità
    e chiarezza" = il verdetto vigente, la passata riparte da lì.
(g) F-ATLAS-1: mint findings a chiusura R3 (2 gambe source-verified,
    sezione sopra) + log deviazioni-da-storyboard (merges, riordini).
(h) A valle di (b)-(f) e del giro utente: BLOCCO 2 (workflow retro-audit
    4 stadi + Q&A red-team, CKP-S2-2) e BLOCCO 3 (R3 pieno).
(i) REVISIONE DI STILE VERA (utente 2026-08-23: "alcuni titoli in
    grassetto altri no, c'è molto da migliorare"): pass di
    NORMALIZZAZIONE tipografica su tutto il deck — titoli identici
    ovunque (dimensione/peso/colore/posizione: host = textbox 32pt
    bold RED a (0.32,0.38); nuove = placeholder 30pt → UNIFICARE),
    convenzione di capitalizzazione dei titoli, scala tipografica
    unica per card/bande/caption, griglia di spaziatura, marker
    bullet; RENDERE MACCHINA-VERIFICABILE nel builder (assert di
    uniformità titoli + scala) — mai più a occhio. ISTANZA 2 (utente):
    la POSIZIONE dei testi di footer ("Rotating Detonation Engine
    Activities" / "T(H)RUST team") cambia da slide a slide — host =
    placeholder a (1.57/9.06, 6.76) con loro allineamento; nuove =
    textbox a (…, 6.80) left-aligned → unificare a UNA geometria e
    allineamento esatti (misurare dal placeholder host, replicare
    identico sulle nuove; assert di posizione nel builder).

## ===== HANDOFF SESSIONE 4 (ordine di apertura) =====
R2: memoria + M0 (mirato) + PROGRESS + SESSION2_LOG (checkpoint+gate) +
QUESTO file INTEGRALE (è il log della sessione 3: tutte le CKP-S3-1..5,
l'onda narrativa consumata, F-ATLAS-1) + NARRATIVE_SPINE_v2.md
(spina convergiuta: contratti di senso per slide + ponti + ordine di
record) + SPINE_ATTACK.md (i 24 finding, tutti applicati).
STATO: deck v1.2 BUILD OK (67 slide = 45 main + 22 backup; ordine di
record in DECK_ORDER dentro build_deck_spres.py); tutti gli ordini
utente CKP-S3-1..4 applicati; CKP-S3-5 (b)-(f) APERTI = primo lavoro S4.
PIPELINE: python build_deck_spres.py (assert-gated); render QA:
soffice --headless → pdftoppm (tmp_pages/deck_qa); l'utente tiene i
.pptx aperti in PowerPoint → il builder salva su _new/_new2 (riallineare
il canonico a file chiusi).
LA BUSSOLA (ribadita dall'utente in sessione): standard = presentazione
SOTA per comprensibilità — spiegare il modello e le esigenze a cui
risponde (funzionale, perché adjoint, quale ottimizzatore, obiettivo di
ogni fase), stile Heister migliorato, zero lingua interna/LLM, zero
contabilità e zero racconti di processo on-slide; il rigore vive nelle
note/backup/retro-audit. Loop utente a lotti PICCOLI.
Vincoli: project_build READ-ONLY; GENO read-only; env pinnato; Fable
ovunque; commit pathspec (mai GENO/stray; data/q_mapping.* NON nostri).
SUITE QUOTA (misurata 2026-08-31, tests/run_all.py, log scratchpad
suite_close_S4.log): PRIMA CORSA 21/23 PASS in 319 s, EXIT 1 — FAIL (vii)
numeric lint + FAIL (xxii) literature registry.
(vii) RIPARATO IN-WINDOW (never-postpone-resolvables; file miei + righe
per-file dei JSON baseline): causa 1 = _probe_typography_new.py con BOM
UTF-8 (PowerShell Set-Content) -> ast.parse crash -> file RIMOSSO
(f0db836); causa 2 = 8 violazioni ratchet R28 -> canone tipografico
DERIVATO in typo_canon.py (32 costanti misurate, nominate), builder
605->568 literal (< baseline 577 -> ratchet DOWN a realta'), down-ratchet
specs_c12 9->2 / specs_c34 5->1 / spreslib 78->76, righe new-file misurate
(_fig_s4_lot2 154, _probe_footerband 4, _probe_subtitles 4,
_probe_typography 5, typo_canon 32); ri-esecuzione: PASS (91 file, 0
violazioni) — commit cf0ca0f; build ri-verificata OK.
(xxii) NON riparato qui (file condivisi / non miei): VIOLATION root B =
cartella PADRE top-level: disk 48 != 9 rows + 38 bulk. Il lint conta OGNI
file top-level della cartella padre (os.listdir + isfile, non solo .pdf);
il +1 e' **Projects.lnk (2026-08-24)**, collegamento Windows creato
dall'utente — non un paper. DUTY (a S-ROADMAP o all'utente): rimuovere/
spostare Projects.lnk dalla cartella padre (nessuna riga registry da
inventare) OPPURE restringere l'enumerazione di root B ai .pdf nel lint
(tests/ condiviso). Nota: literature_addition_nozzle_rde/ (untracked, 1
PDF Elsevier S1270963824010071, AST 2024) NON e' una root del lint ma e'
un paper non registrato -> candidato WANTED/READ per la finestra lit.
OSSERVATO 2026-08-31 durante la chiusura: tests/test_numeric_lint.py
risulta MODIFICATO nel working tree — NON da questa sessione (mai toccato;
non committato da me): lavoro della sessione parallela S-ROADMAP in corso
sullo stesso checkout. Regola parallela rispettata: nessun mio commit
include tests/.
ESITO DI CHIUSURA: 22/23 verdi dopo la riparazione (vii); (xxii) pending
con causa nominata e duty assegnata.
## ===== FINE HANDOFF =====

## ===== SESSIONE 4 (2026-08-23) — LOG LOTTI CKP-S3-5 =====
### LOTTO 1 — (b) sweep deadline interne on-slide: ESEGUITO, in giro utente
- Occorrenze on-slide rimosse (4): C7-ter honesty_band "starting September"
  → tagliata ("it is the first campaign."); C17 card-1 window "campaign
  starting now — September milestone" → "first campaign — starting now";
  C18 card-2 "WHEN: starting now — September" → "WHEN: starting now";
  C17-bis (backup) intro "no pre-milestone number ... of the phase" →
  "no number exists before it runs — and it runs as the first campaign".
- ESTENSIONE DICHIARATA (stessa classe F-9, vista al QA): C17-bis card
  "owner and window named" → "lead and date named"; "with an owner" →
  "with a named lead".
- KEEP legittimi (scan rejector, 3 hit): A1 "September 2026" = data
  evento (non deadline interna); C18 "instrumentation window" = termine
  ingegneristico; backup-59 "re-exam window" + tally = slide-contenitore
  della contabilità off-main (ammessa dal pin guardia-18 backup).
- Build: 67 slide, register-lint 0, OK; salvataggio sul canonico
  SPRES_deck_v1.pptx (file non lockato in finestra). QA visivo render
  31/43/44/67: nessuna deadline residua, layout intatti.
- Rejector: scan python-pptx on-slide (note escluse) September/Settembre/
  milestone/deadline = 1 hit legittimo (A1); owner/window = 2 hit
  legittimi. Comando nel log di sessione, misurato in-window [SR-12].

### LOTTO 2 — (i) tipografia + (c) slide adjoint + (d) rework C9: ESEGUITO, in giro utente
- **(i) NORMALIZZAZIONE TIPOGRAFICA (anticipata su ordine utente in-window)**,
  causa-radice MISURATA (probe _probe_typography.py, mai a occhio):
  (1) titoli host = textbox 32pt bold ancorati in BASSO in box H=0.60
  (testo a ~0.55-0.98"; i titoli a 2 righe TRABOCCAVANO sopra il box, es.
  A14) vs nuove = placeholder 30pt ancorato in ALTO a 0.30 → CANONE UNICO
  applicato a TUTTE le slide (A1 esclusa): box (0.32, 0.38) × 12.7 × 0.95,
  anchor TOP, 32pt bold RED Palatino (font già identici, misurato);
  (2) footer host = placeholder a top 6.76 CENTRATO nel box vs nuove =
  textbox a 6.80 left → nuove riallineate a (1.57/9.06, 6.76) CENTER.
  ASSERT nel builder (blocco typo in build_deck_spres.py, tolleranza
  ±0.02"): size/bold titolo, geometria e centratura footer — build FAIL
  se violate. ROLE_SIZES title 30→32 (floor 28 invariato).
  Residuo dichiarato: titolo A14 resta a 2 righe (62 char) — sfiora il
  sottotitolo host a 1.22", non collide; eventuale accorciamento = tocco
  di contenuto host, da ordinare.
- **(c) SLIDE C-ADJ COSTRUITA** (What is an adjoint — the whole gradient
  for one extra solve): posizione pre-C13; fig di casa fig_cadj_cost.png
  (N solve vs forward+backward, palette deck, _fig_s4_lot2.py); 3 bullet
  primo-incontro (J, dJ/d(shape), 1+1 solve → TR-Newton); note = script
  disteso + provenance (T-LEMB/X-TOCV in note, guard 18). DEVIAZIONE
  DICHIARATA: main 45→46 (ordine utente CKP-S3-5(c)); assert census
  aggiornato 46; totale 68.
- **(d) C9 RIFATTA** (slide 34): titolo "Same pressure reading, different
  thrust"; visual = cartoon due condotti + manometri identici, swirl
  diverso, spinta diversa (fig_c9_gauge.png, di casa); 3 bullet piani.
- **WELD IMPOSED-BC/Q2D (user catch in-window, atlas-verificato)**: la
  domanda "era noto prendere lo stato camera/gola e imporlo come BC?" ha
  risposta DI RECORD: CH10 lineage LL-24 (Miki 2020 = antenato operativo,
  replay periodico dello stato Q2D come inlet BC del dominio ugello,
  THROAT_HARVEST A.6), LL-5 (Paxson-Miki 2022, stessa architettura, A.8),
  LL-6 (Harroun Eq.7 analitica p-only, A.5); posizione CH10: pratica del
  campo = imposed-BC SENZA contratto, noi = stessa architettura CON
  contratto d'ammissione. NON era consumato da alcuna slide → cablato in
  C9 bullet 3 (autore-anno on-slide) + script/note (claim capability Q2D
  in-house = CLASS-level, nessuna campagna promessa; ancora = credenziale
  host A9 HYPERDE Q2D). 
- Build: 68 slide, lint 0, OK. NOTA: canonico LOCKATO (PowerPoint aperto
  dall'utente) → salvato su SPRES_deck_v1_new.pptx; riallineare a file
  chiuso. QA render: s3-vs-s4 uniformi (titolo+footer), s14 sanata,
  s34/s36 verificate.
- APERTO (ordine utente in-window, fine lotto 2): slide 41-46 (atto
  finale C16-bis→C19) "non si capiscono, AI flavor, non SOTA" →
  proposta lotto 3 = rebuild dell'atto con workflow naive-listener
  (sotto, da ratificare col giro).

### LOTTO 3 (in corso) — ordini utente in-window + workflow atto finale
- **C2 PROMOSSA IN MAIN** (ordine utente: "slide 64 nel punto giusto, non
  backup"): posizione post-C9 (35/46); titolo "Not just pressure — the
  whole interface state varies"; bullet nuovi (tutte le grandezze variano
  KP18 Tab.1; superficie sonica corrugata con bande subsoniche; estensione
  = geometria+punto di lavoro, "published both ways", misurata mai
  assunta). VERIFICA FISICA della tesi utente (alta p0/portata → tutto
  sonico anche throatless) DA ATLAS+HARVEST: SUPPORTATA non provata —
  PM22 throatless M 1.1-1.4 a tutte le fasi (A.8) e Jourdaine open
  "principally sonic or supersonic" (A.1) = polo FOR; KP18 bassa
  contrazione = bande subsoniche anche "effectively choked" (A.7);
  Jourdaine choked micro = camera subsonica con shock a monte; NESSUNO
  sweep pubblicato della transizione (gap G6/G7) → il monitor misura il
  segno di Mach per fase. Tutto nelle note C2 con ancore harvest.
- **fig_c2_interface.png RIDISEGNATA SOTA** (ordine utente): taglio
  meridiano canale+plug, fronte rotante, superficie sonica corrugata con
  bande M<1/M>1, interfaccia di progetto a valle (in _fig_s4_lot2.py).
- **C16-bis → BACKUP eseguito** (CKP-S3-5(e); destinazione = backup con
  Q&A-readiness, raccomandazione orchestratore non obiettata al giro).
  Main = 46 (45 CKP-S3-4 + C-ADJ + C2 − C16-bis); cut-list = C3-bis,
  C12, C15, C17-bis, C16-bis(S4e).
- **NUMERAZIONE MAIN-ONLY + DIVISORE** (ordine utente): contatori n/46
  solo sulle main; slide di demarcazione "Backup Slides" (BKDIV, layout
  divider) a posizione 47; backup marcate B-1..B-22 (set_backup_counter
  sostituisce campo+/18 del band). Totale fisico 69.
- **TIPOGRAFIA: ENFORCEMENT TOTALE** (ordine utente "una volta per
  tutte"): il pass del builder ora RISCRIVE (non solo verifica) ogni
  titolo (box/anchor/margini-0/autofit KILLED — PowerPoint restringe i
  placeholder in overflow, LibreOffice no: era il residuo invisibile ai
  QA — ogni run 32pt bold RED font deck) e ogni footer top-level
  (geometria esatta, margini 0, CENTER, 14pt bold white) su host+nuove.
  Probe post-build su _new: zero deviazioni titolo/footer (residui =
  sottotitoli teal host 28pt = design host, A1 esente). Build 69 slide
  lint 0 OK. File: canonico RIAPERTO dall'utente in PowerPoint → build
  su SPRES_deck_v1_new.pptx; _new intermedie PRECEDENTI ELIMINATE
  (igiene: un solo file per stato); riallineare canonico a file chiuso.
- **TR-NEWTON: aggiudicazione verificata in atlas** (domanda utente):
  CH4 §6 (d) C31 = ledger choice_ledger.yaml:481-493 — TR-Newton
  segmentato a curvatura misurata = driver di record, alternative censite
  (quasi-Newton, proximal-bundle, [P-IPADJ] interior-point adjoint),
  survey SOTA datata 2026-08-19/20 ATTUALE con ri-sweep nominato a
  F2-entry (cluster C31/C58 vs landscape 2026); criteri pubblicati
  ancorati (Hicken-Zingg, Fidkowski-Darmofal, CH2:684). Il deck lo dice
  su C14 + backup B-12/B-13 (optimizer full record).
- **WORKFLOW ATTO FINALE LANCIATO** (ordine utente): run wf_a5a1f897-8a9,
  4 agenti sequenziali (listener-naive sui render 34-46 → rewriter con
  BRIEF vincolante → refuter record/registro → converger + listener-2);
  carrier = act_rework/BRIEF.md (regole CKP-S3-1 + lista vietata +
  contratti SENSE spine + arco di consumo dichiarato); deliverable =
  act_rework/REWRITE_FINAL.md, consumo = orchestratore S4 → specs →
  rebuild → gate utente. [SR-9: shape 4 agenti seq, peso a consuntivo
  alla chiusura.]

- **AUDIT FULL-DECK LANCIATO** (ordine utente in-window: "audit simile per
  tutto il deck tranne backup" = lettera (f) operativa): run
  wf_8140508c-b17, 5 agenti (4 listener paralleli: full-arc 1-46 +
  sezioni 1-22 / 23-35 / 36-41, + synthesizer con tabella difetti per
  severità, pattern trasversali, slide PASS intoccabili, batching in
  2-3 lotti per il giro utente); slide host 3-21 = HOST-LIMITED (riparo
  solo titoli/caption/note). Render sorgente = deck_audit/s-01..46 dal
  build corrente (_new, 69 slide, enforcement attivo). L'atto 42-46
  resta al workflow act-rework (wf_a5a1f897), nessuna sovrapposizione
  di scrittura: entrambi read-only sul deck, artefatti in cartelle
  disgiunte. [SR-9 a consuntivo alla chiusura.]

## CKP-S4-1 (utente, 2026-08-23, VINCOLANTE) — PERSONA ESATTA + CONVERGENZA A 4 ASSI
Verbatim: "il target di ascoltatore deve essere esattamente quello che
sarà, e deve essere a convergenza con piena chiarezza, completezza,
comprensione e collocazione." LETTURA DI RECORD: (1) persona listener =
l'audience DI RECORD (decisione utente S1, PROGRESS_2026-08-22_Spres1
:28-30): **ESA propulsion panel** — ingegneri di propulsione senior,
esperti di ugelli classici/CFD, zero interni RDE assunti
(nothing-assumed physics intro), che valutano il gruppo e DECIDONO
sulle tre richieste; 60'. Mai più listener generici. (2) Il ciclo
audit → riparo → re-audit itera CON LISTENER FRESCO della persona
esatta fino a PASS per-slide su QUATTRO assi: CHIAREZZA (parafrasabile
in una frase dal panel), COMPLETEZZA (nessuna domanda essenziale senza
risposta o senza rinvio esplicito a note/backup), COMPRENSIONE
(takeaway del listener == contratto SENSE della spine), COLLOCAZIONE
(slide al posto giusto nell'arco; contenuto al livello giusto
main/backup/note). Verdetto di convergenza = tabella per-slide 4-assi,
tutte PASS. I run già in volo (wf_a5a1f897 atto, wf_8140508c full-deck)
valgono come PRIMA ONDA (difetti trovati restano difetti); il gate di
convergenza usa la persona esatta da qui in poi.

### LOTTO A — ATTO FINALE IMPLEMENTATO (REWRITE_FINAL 5 slide + duty residue)
- Workflow act-rework CONSUMATO [SR-9: 4 agenti seq, 305k tok, 47 tool
  use, 17 min; listener→rewriter→refuter (31 PASS / 8 STRENGTHENED / 8
  REGISTER-HIT / 1 UNANCHORED / 1 SENSE-LOST, riparazioni word-exact)
  →converger, LISTENER-2 = 5/5 SENSE YES]. Audit full-deck CONSUMATO
  come prima onda [SR-9: 5 agenti (4 parallel + synth), 386k tok, 132
  tool use, 9 min; sintesi = 43 difetti, batching B/C/D].
- IMPLEMENTATO nelle spec (C11 in specs_c12; C17-pre/C17/C18/C19 in
  specs_c34): titoli-asserzione nuovi, lessico "source" ovunque
  (channel/heel/booking-debt/sizing → parole ingegneri), C17 = catena
  frecce 4 step con conseguenze, C18 = 3 richieste in lingua piana,
  C19 = chiusura senza universali né "honesty" narrata. Lessico
  sincronizzato anche su backup D-F (tabella completa).
- **DICHIARAZIONI DI BUDGET (mai silenzio)**: C19 summary ≈66 parole
  nette > cap 60 e 5 bullet > 3 — trattamento dichiarato = grammatica
  two-column di record (REFUTE (12)); C11 honesty_table vicino al cap
  ~100 (tabella 6 righe = il contenuto della slide); C17 porta 2 bande
  slim oltre le card (forma d'ordine, REFUTE (10)).
- Duty residue scaricate: (3) pointer C19 "spoken as in A2" RICONCILIATO
  (A2 è agenda-only: forma query-bounded guard-9 resa in-script, nota
  superseded dichiarata); (6) s-60/D-F NON era stub — tabella completa
  già in build (F-3 scaricata), solo sync lessicale; fix collisione
  footer C19 in ly_summary (reprise sopra la banda, bottom ≤5.9");
  ly_roadmap_cards closing opzionale.
- **WELD HEAD-TO-HEAD (domanda utente in-window, atlas-verificata)**:
  card 2 di C17 affilata alla forma d'atlante CH6 :440 (I4 = Rao/GENO
  su (⟨Pc⟩,T0,γ)) + :490 (twin a vincoli IDENTICI) + :712 (comparatore
  ZERO computed instances) — on-slide: "our per-phase design vs the
  classical design at cycle-mean p₀/T₀ — identical constraints; no such
  number exists yet". Script C17 la dichiara "the reason this programme
  exists". Script C11 aggiunge la DIAGNOSI DI CLASSE del +0.51%
  ([C-O33] quantificata: cert-limited a margine inattivo, 3 istanze
  S20/S22/S24; il rung-1 già +44-87% argmax / 3-10 s Isp) — weld di
  contesto, indebolisce la lettura del numero piccolo, zero claim nuovi.

## ===== CKP-S4-2 (utente, 2026-08-23, VINCOLANTE) — ARCHITETTURA v2 =====
Ordini utente in-window (verbatim compressi): (1) "da slide 22 a 46,
parte nozzle, troppe slide, troppa roba... massimo 10 slides"; (2) "è
terribile la slide di richiesta, NON CHIEDIAMO NULLA, e non capisco il
senso di slide 46"; (3) "slide 2 non ha senso di esistere, partire
dalla 3"; (4) "eliminare le immagini illeggibili, come la tabella di
Humphreys"; (5) titoli/footer: sottotitoli host non uniformi (FATTO:
enforcement 28pt teal bold prima riga, probe verde) + footer non
centrato nella barra rossa (FATTO: label/team/numero tutti MIDDLE sul
box banda 6.71x0.81, assert aggiornato; campo residuo "n/17" del
gruppo host azzerato).
DECISIONI DI STRUTTURA (deviazioni dichiarate, ordine utente prevale
su CKP-S3-4 "cuore intoccabile" e su A2/C18 di storyboard):
- A2 (agenda) → KILL dal main (backup, dichiarata); si apre A1 → A3.
- C18 (asks) → KILL dal main (backup per Q&A): il deck PRESENTA, non
  chiede; la chiusura non promette richieste.
- SCHELETRO NOZZLE v2 (≤10 slide, posizioni 21+: B1 resta a 20):
  N1 hinge = A6⊕C1 (efflusso periodico; il campo disegna su una media
     senza barra d'errore; due flowfield);
  N2 evidenza = C4⊕C5 (ranking inverte, Li-Xu; 1971 argmax ×2.45 SOLO
     testo — scan Humphreys ELIMINATO perché illeggibile; verdetto
     censimento C3 in una riga);
  N3 tesi = C7 INVARIATA (protetta);
  N4 formulazione = C7-bis (protetta, riparazioni Lotto B; C7-bis-pre
     e C8-essenza in script);
  N5 dove si apre + domanda head-to-head = C7-ter v2 (Lotto B);
  N6 contratto dati = C9⊕C2 (manometro + tutte-le-grandezze + pratica
     imposed-BC + Q2D in-house);
  N7 macchina = C-ADJ⊕C13 (idea adjoint + 6 stadi);
  N8 prova+prezzo = C13-val⊕C16 (riproduce Rao; minuti non settimane);
  N9 budget errori = C11 (+essenza C10 in script);
  N10 piano+chiusura = C17⊕C19 (4 misure + takeaway; ZERO asks).
- A BACKUP (dichiarati): A2, C1, C3, C5(scan), C6, C7-bis-pre, C8,
  C8-bis, C10, C13(grafo pieno già), C14, C16, C17-pre, C18, C19-forma
  -vecchia assorbita in N10. Main v2 = 19 (A1,A3..A20) + B1 + 10 = 30.
- ESECUZIONE: dopo l'atterraggio del workflow Lotto B (wf_46daf52e, i
  cui testi alimentano N4/N5 e i backup teorici), implementazione in
  UN passo (DECK_ORDER v2 + spec merged + assert census 30 + A2/C18
  cut) → rebuild → render → gate persona-esatta 4 assi (CKP-S4-1).

### S4v2 IMPLEMENTATA (2026-08-23, build verde 69 = 29 main + div + 39 bk)
- Nozzle = 9: A6(rework: "the literature designs on its time-average",
  verità formale nello script) → C4(rework: evidenza + verdetto
  'approximately' assorbito da C7) → C7-bis(titolo: "Designing on the
  average solves a different problem — provably") → C7-ter(banda =
  head-to-head mai computato + segnale rung-1) → C9(+numeri interfaccia
  ex-C2) → C13(bullet: J/adjoint/registro) → C13-val(+velocità ex-C16)
  → C11 → C17(closing takeaway, chiude il deck, zero asks).
- Lingua: "the literature" ovunque on-slide (mai "the field").
- Cut S4v2 → backup (17 nuovi, census 22): A2, C1, C2, C3, C5(scan
  Humphreys via dal main), C6, C7, C7-bis-pre, C8, C8-bis, C10, C-ADJ,
  C14, C16, C17-pre, C18(no-asks), C19. Assert 29/22 aggiornati.
- PENDING: integrazione Lotto B (wf_46daf52e) al suo arrivo —
  cherry-pick su C7-bis/C7-ter main + backup teorici; poi gate persona
  4-assi. Residuo dichiarato: script/notes dei superstiti citano ancora
  qua e là slide ora in backup (segnale-posti A2, "two slides ahead") —
  passata di coerenza note al gate.

## ===== CKP-S4-3 (utente, 2026-08-25, VINCOLANTE) — CAMBIO DI ROTTA =====
(1) DECK COMPLETATO DALL'UTENTE per conto proprio; versione finale =
Desktop/Presentazione_ESA (fuori repo, di proprietà utente — READ-ONLY
per noi, oggetto di prova, mai deliverable nostro da qui in poi).
Il thread deck-authoring S-PRES Blocchi 1-3 è CHIUSO dall'utente.
(2) Lotto B workflow: rewriter+refuter COMPLETATI (REWRITE_LOTB_v1 +
REFUTE_LOTB_v1 su disco, NON consumati), converger MORTO su limite di
spesa mensile [SR-9: 3 agenti, 297k tok, 36 tool use, 22 min; 2/3
done]. Da direttiva modello-pinnato: STOP, nessun relaunch, harvest
inline dei 2 artefatti superstiti.
(3) NUOVA ROTTA (ordine utente): completare la sessione con le fasi
che valgono come PROVE PER L'ATLAS — tracciabilità, prove di lettura,
consequenzialità logica di ogni scelta — informative per il resto del
lavoro (F2, paper). Esecuzione SOLO a valle di rielaborazione critica
(consegnata nel turno). VINCOLO OPERATIVO: quota critica — zero
subagenti/workflow da qui a fine sessione, tutto inline e mirato.

## ===== HANDOFF (sessione parallela S-ROADMAP aperta dall'utente 2026-08-31) =====
STATO DI QUESTA SESSIONE (S-PRES S4, coda di chiusura): R3/R7 eseguite —
PROGRESS in place (ORA 08-25, NEXT = S-ROADMAP, BLOCCATO 18 CONSUMED CON
PIVOT, righe censimento R37/R38), ADVISORY_INDEX (riga advisory
PENDING-CONTRACT + addendum blocco raws 456 file), findings mint 2 righe,
memoria aggiornata; lint misurati in-finestra: (xix) PASS 253/0, (xx) PASS
107/107 (riparato da 1 violazione status-enum), (xxii) PASS. Commit di
chiusura: c4dc1d0, 3fa7839, dad95dd, e4b7366, 78c19a9, 07237c1.
IN VOLO: tests/run_all.py (suite completa) lanciata 2026-08-31 in
background — esito NON ancora quotato; rischio noto = test (vii) baseline
new-file sui nuovi script deck_build (_probe_*.py, _fig_s4_lot2.py,
_extract_esa_final.py). REGOLA PARALLELA: questa sessione NON accetta
baseline né tocca tests/ finché S-ROADMAP è aperta (file condivisi);
l'esito viene quotato QUI e, se (vii) fallisce, la duty "accettare le
righe baseline dei 6 script S4" passa a S-ROADMAP (o a chi chiude per
ultimo), dichiarata come pending. File che questa sessione può ancora
toccare: SOLO questo BUILD_LOG + scratchpad. Untracked non nostri
(pending conferma utente per lo spazzatura "t --count HEAD:q"):
NASA_STUFF_Nozzle_Inlet/, Three-Dimensional-Nozzle-Design-Code/,
literature_addition_nozzle_rde/, er.name, mailmap.txt.
Conteggi rigenerati da comando in questa finestra (SR-12): findings 253
(211 OPEN), index 107 file rows + 5 block rows, deck_build 387 file,
spres_raws 456 file, commit branch 292 (git rev-list --count HEAD dopo 383a855 = 291 + questo; 7 commit di chiusura: c4dc1d0, 3fa7839, dad95dd, e4b7366, 78c19a9, 07237c1, 383a855; il '286' della finestra 08-31 mattina era pre-chiusura).
## ===== FINE HANDOFF =====

## STATO (aggiornare a ogni confine)
- [x] R2 apertura + censimento asset (PDF tutti localizzati; mappa
  P-A/P-B/P-C/P-D/KP18/P-M/HUM/RAO in FIGS_MANIFEST quando atterra)
- [~] AGENTE crops paper → figs_paper/ + FIGS_MANIFEST.md (in volo)
- [~] AGENTE graph renders → graph/ + GRAPH_RENDER_NOTES.md (in volo)
- [ ] specs_a.py (A1-A20+B1) / specs_c.py (C 29) / specs_d.py (backup)
- [ ] eqs_spres.py (strip equazioni)
- [ ] figure di casa (schemi nativi pptx nel builder; matplotlib:
  fiber C9, bars C16, quotient C8 se serve)
- [ ] build_deck_spres.py + spreslib.py + asserts + DECK_MANIFEST.md
- [ ] notes_spres.py (guardia 15/18) via canale add_notes
- [ ] SPRES_deck_v1.pptx + render QA visivo + BUILD_REPORT.md
