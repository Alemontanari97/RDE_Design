# STYLE ADJUDICATION — Presentazione_CVA_RDE.pptx come fonte di stile per il deck ESA

Data: 2026-08-22. Aggiudicatore: agente agnostico S-PRES Block 0 (mandato: verdetto capace di RIGETTARE).
Ruolo del documento: aggiudicazione di stile, di record, per l'estensione di ppt_Heister.pptx
via pipeline deck-as-code (`../project_build`, build_deck.py). Consuma i censimenti:
- `validation/spres_raws_2026-08-22/CENSUS_cva_rde.md` (di seguito: C-CVA)
- `validation/spres_raws_2026-08-22/CENSUS_heister.md` (di seguito: C-HEI)

## QUESTIONE

Il template/stile di Presentazione_CVA_RDE.pptx è SOTA per il TARGET = prima presentazione
milestone a un panel propulsione ESA, 60 minuti, nulla dato per scontato sulla fisica
RDE/detonazioni? Il deliverable è l'ESTENSIONE di ppt_Heister.pptx (18 slide); CVA_RDE è il
candidato stile. Fatto di record pesato: CVA_RDE è compilato dalla stessa pipeline che
produrrà il deck finale, quindi ogni suo tratto di stile è riproducibile — e ogni suo
emendamento è implementabile — a costo marginale.

## FATTI (citati per censimento)

Dal C-CVA (misurati):
- 62 slide 16:9; genere dichiarato in copertina "Graduate lecture · 90 minutes"; 5 atti con
  divisori-slide; ZERO slide di backup, ZERO ask.
- Densità testo: body media 98,2 parole/slide, mediana 95, min 28, max 206; 5 slide ≥150
  parole (18, 19, 25, 61, 62); correzione dichiarata: ~10-15 parole/slide sono
  intestazione+titoli (nessun placeholder li separa).
- Gerarchia corpi: titolo 30 pt (×61) + kicker 24 pt (×61); divisori 38 pt; corpo bullet
  dominante 13,5-14 pt (14,0×147, 13,5×114); tabelle/note figura 9-12,5 pt; minimo assoluto
  6 pt (×1, slide 18). Default master (44/28 pt) ignorati.
- Nessuna slide usa il placeholder titolo → app.xml TitlesOfParts = "Presentazione standard
  di PowerPoint" ×62 (outline e accessibilità cieche). Palatino Linotype ×970, NON
  incorporato (ppt/fonts/ assente).
- Palette hard-coded su tema grayscale inerte: #822433 ×384, #2B2B2B ×368, #FFFFFF ×309,
  #F2ECED ×132, #006778 ×106, #004D59 ×53; coerenza slide↔figure totale.
- Figure: 50 totali, ~36 di casa (stile unico serif/LaTeX, 4 colori del deck, DPI eff.
  152-489 mediana ~245, annotazioni interpretative DENTRO il plot) + 14 riusate da paper
  (qualità scansione, image78 ~154 DPI, jet solo nel pannello CFD riusato image48), TUTTE
  con attribuzione in slide; 32 strip-equazioni LaTeX→PNG uniformi a 200 DPI; 8 tabelle
  native 9-12 pt. Difetti dichiarati nei plot di casa: 2 (collisione legenda image76/s53;
  annotazione a bordo image72/s50).
- Provenienza: disclaimer di ricostruzione NEI plot ("stylised reconstruction … not
  digitized", "representative — reconstructed"), ancore di replica sovrapposte, anomalia
  704 s* marcata e mai propagata; note relatore 56/62 con Σ 4.587 parole (canale di audit).

Dal C-HEI (misurati):
- 18 slide 16:9, media netta 50,2 parole/slide (max 151, S18); corpo moda 18 pt (×120);
  palette hard-coded #822433 ×91 + variante #822333 ×34 + #006778 ×28; Palatino Linotype
  ×245. La convergenza cromatica/tipografica col candidato è un fatto misurato.
- Difetti Heister: footer residuo di altro deck ("HEM modeling…" su S2-S18), doppio
  contatore pagina (box "2 /17" stantio + placeholder "2/18"), master/layout con default
  altrui ("M. Fiore et al", "Modular Aerospike Nozzles…", "‹N› /17"), text-box fuori canvas
  (S11), 4 figure paper-style SENZA credito, note presenter vuote 18/18.

Verifica visiva propria (campione 8 media, non un ri-censimento): image15, image18, image46,
image5 confermano i claim di qualità dei plot di casa (etichette dirette sulle curve, zone
proibite ombreggiate con motivazione in-figure, valori quotati sui punti, assi grandi);
image19 conferma strip-equazione nitida; image78 conferma qualità raster non-nativa della
figura riusata; image76 e image72 CONFERMANO i 2 difetti dichiarati (la collisione
annotazione/legenda di s53 è reale e visibile; l'annotazione di s50 preme contro il bordo
del pannello). Nessun claim campionato è caduto.

## GIUDIZIO PER-CRITERIO

### Criterio 1 — Densità testo: NON conforme al target (densità da lezione). EMENDARE.

98,2 parole body/slide di media (mediana 95, max 206) è il registro di una lezione da 90
minuti con lettura guidata — coerente col genere dichiarato del file, non col target. Per un
milestone talk a 60' davanti a un panel, lo standard di pratica è una idea per slide e testo
minimo: la spiegazione "da zero" della fisica RDE va nelle FIGURE parlanti e nel parlato,
non in bullet densi. La calibrazione interna esiste già ed è misurata: ppt_Heister viaggia a
50,2 parole nette/slide — circa metà del candidato. Anche correggendo le ~10-15 parole di
intestazione, CVA resta a ~85 parole nette/slide: fuori registro di un fattore ~1,7-2.
Le 5 slide ≥150 parole (due tabelle-mappa, summary, references) sono il caso estremo: in un
milestone deck diventano backup o si spezzano. Attenuante reale: la STRUTTURA della slide
tipica CVA (3-5 bullet da una riga e mezza + 1-2 figure) è sana; è il budget parole per
bullet che è da lezione. Il canale note relatore (4.587 parole, 56/62) è invece ESATTAMENTE
dove il surplus esplicativo deve migrare: quel canale si adotta.
Verdetto parziale: RIGETTO della densità così com'è; adottabile solo con budget-parole
emendato (E1).

### Criterio 2 — Gerarchia visiva: struttura SOTA, valori assoluti e robustezza NO. EMENDARE.

La gerarchia a tre livelli (30/24 pt titolo+kicker, corpo, 9-12,5 pt tabellare) è coerente,
disciplinata, applicata ×61 senza deviazioni: come SISTEMA è professionale. Ma i valori
assoluti sono da documento/lezione, non da proiezione in sala review: corpo dominante
13,5-14 pt è sotto la soglia di pratica per proiezione (≥18 pt corpo; Heister è già a 18 pt
moda, misurato ×120); tabelle a 9 pt sono a rischio concreto in sala; il minimo 6 pt è un
difetto puntuale senza difesa. Robustezza: l'assenza TOTALE di placeholder titolo
(TitlesOfParts default ×62) rende outline e accessibilità cieche — per un file che un panel
ESA può richiedere in anticipo e aprire, è sciatteria strutturale invisibile a schermo ma
visibile a chi ispeziona; Palatino non incorporato è fragilità reale fuori da macchine
Windows (sala altrui). Nessuno di questi difetti è strutturale: nella pipeline sono
parametri e template-fix.
Verdetto parziale: adottare la gerarchia COME SISTEMA; emendare i corpi (E2), i
placeholder (E3), la font policy (E4).

### Criterio 3 — Leggibilità figure: il pezzo più forte del candidato. SOTA, da ereditare (con 2 fix e un floor).

I plot di casa sono esattamente lo strumento che il target richiede: per un panel dove nulla
è dato per scontato, le annotazioni interpretative dentro la figura (frecce con la tesi,
zone proibite ombreggiate CON la ragione scritta, valori quotati sui punti, box parametri)
fanno il lavoro didattico senza gonfiare il testo slide — verificato visivamente su
image15/18/46/5: la figura si legge da sola. Stile unico serif + 4 colori del deck su ~36
figure = identità visiva riconoscibile; DPI mediano ~245 adeguato alla proiezione; strip
equazioni uniformi a 200 DPI nitide; "nessun testo apparente sotto ~10 pt" (C-CVA) è al
limite ma accettabile A CONDIZIONE di un floor esplicito per le figure nuove. Sul quesito
del criterio: i 9-12,5 pt sono il corpo delle TABELLE NATIVE e delle note, non il testo
interno dei plot; le tabelle a 9 pt vanno alzate (rientra in E2), i plot no. I 2 difetti
noti sono confermati, puntuali, e riparabili in pipeline a costo minimo (E5). Le 14 figure
riusate a qualità scansione sono il prezzo del contenuto altrui: la disciplina di
attribuzione per-slide + i disclaimer di ricostruzione NEI plot + le ancore di replica sono
sopra lo standard di pratica e per un panel ESA sono un attivo di credibilità, non un
difetto. Unica riserva: colormap jet (nel riuso image48) non deve comparire in figure nuove.
Verdetto parziale: ADOTTARE in blocco il sistema-figure (stile, annotazioni, strip-eq,
disciplina di provenienza), con i 2 fix e il floor tipografico in-figure (E5).

### Criterio 4 — Professionalità template: identità SOTA, meccanica e genere NO. EMENDARE / NON EREDITARE.

L'identità cromatica #822433+#006778 è coerente al 100% tra slide e figure (misurato) ed è
GIÀ l'identità di ppt_Heister (#822433 ×91 + #006778 ×28): adottarla non è un'importazione
ma la conferma ripulita dell'identità esistente (con normalizzazione della variante spuria
#822333 ×34 di Heister). La meccanica però è fragile: tema grayscale inerte + colori
hard-coded run per run significa che il "tema" vive solo nel generatore — accettabile SOLO
perché il deck finale sarà anch'esso generato (la pipeline È il tema); resterebbe fragile a
editing manuale a valle, e va detto. app.xml con titoli default ×62 = igiene file carente
(si sana con E3). Genere: 5 atti da 90', zero ask, zero backup, validazioni in prima linea —
è un'architettura da lezione magistrale, NON da milestone review; il candidato non contiene
l'architettura che il target richiede (BLUF, ask con candidates of record, time-boxing con
cut-list, backup deck dal Q&A map: tutte prescrizioni del carrier S-PRES). Su questo asse il
candidato non si emenda: semplicemente NON si eredita (E7). Un tratto di genere-lezione è
invece esportabile: la scelta di tenere le validazioni come slide di prima linea è giusta
anche per una milestone (credibilità), in forma compressa.
Verdetto parziale: adottare identità cromatica + chrome sobrio; NON ereditare
l'architettura di genere; sanare l'igiene file.

### Peso della riproducibilità-pipeline (fatto a favore, non decisivo)

CVA_RDE dimostra che la pipeline produce: 61 slide a chrome identico, 32 strip-eq uniformi,
zero media orfani, provenienza sistematica. Questo abbassa quasi a zero il costo di OGNI
emendamento qui prescritto (sono parametri e template-fix nel generatore) e rende
l'alternativa (c) — costruire uno stile nuovo — un costo secco senza guadagno dimostrato.
Dichiarazione esplicita: questo fatto sposta il verdetto da (c) verso (b), ma NON avrebbe
salvato uno stile sbagliato nel merito; lo stile è giusto nel sistema-figure e
nell'identità, sbagliato nel registro testo/corpi — riproducibile o no.

## VERDETTO: (b) ADOTTA-CON-EMENDAMENTI

Nessun (a): densità 98,2 parole/slide, corpo 13,5-14 pt, tabelle 9 pt, placeholder assenti e
genere-lezione sono misurati e incompatibili col target; adozione in toto propagherebbe il
registro sbagliato. Nessun (c): il sistema-figure, la disciplina di provenienza e l'identità
cromatica (già condivisa da Heister) sono SOTA e riproducibili; i difetti sono parametrici,
non strutturali — un rigetto sarebbe sproporzionato e butterebbe l'asset migliore.

Emendamenti vincolanti (tutti implementabili in build_deck.py; soglie = classe PRACTICE,
dichiarate come standard di pratica per proiezione, calibrate sull'interno misurato di
Heister):

- **E1 — Budget testo per registro milestone.** Slide di contenuto: ≤60 parole nette
  (target mediano 35-50, allineato al 50,2 misurato di Heister); slide-tabella/validazione:
  hard cap 90 nette; vietate slide ≥150 parole (le 5 di CVA non sono un modello). Una idea
  per slide. Il surplus esplicativo migra nelle note relatore (canale CVA adottato) e nel
  backup deck. Enforcement: assert di conteggio parole nel build (la pipeline già fa
  build-time asserts).
- **E2 — Corpi tipografici da proiezione.** Corpo bullet ≥18 pt (moda Heister); tabelle
  ≥12 pt (target 14); floor di deck 12 pt con deroga a 10 pt SOLO per attribuzioni/footer;
  eliminato il 6 pt. Titoli 30/24 pt e divisori 38 pt di CVA restano (funzionano).
- **E3 — Placeholder titolo reintrodotti.** Ogni slide usa il placeholder titolo del
  layout: outline, accessibilità e TitlesOfParts tornano parlanti. Fix nel generatore, non
  a mano.
- **E4 — Font policy esplicita.** Palatino Linotype incorporato nel .pptx consegnato,
  oppure PDF di cortesia di record per la sala + fallback serif dichiarato. Decisione a
  monte, non default ereditato.
- **E5 — Sistema figure: 2 fix + floor.** (i) Riparare la collisione annotazione/legenda
  di image76 (s53) e (ii) l'annotazione a bordo pannello di image72 (s50) — entrambe
  confermate visivamente; (iii) floor del testo in-figure ~12 pt apparenti alla dimensione
  di display per le figure nuove; (iv) DPI efficace ≥200 mantenuto; (v) niente colormap jet
  nelle figure nuove (il riuso attribuito resta com'è).
- **E6 — Igiene chrome e contatori.** Numerazione N/M rigenerata dal build (mai
  denominatori stantii: il "2 /17" di Heister è il controesempio misurato); UN solo
  contatore; normalizzazione #822333→#822433; footer e master ripuliti dai residui altrui
  (HEM, "Modular Aerospike Nozzles…", "M. Fiore et al").
- **E7 — Confine di genere (non-eredità dichiarata).** Ask slide, BLUF, backup deck da Q&A
  map, time-boxing con cut-list NON provengono da CVA (che misura 0 backup, 0 ask):
  l'architettura milestone è quella del carrier S-PRES. Da CVA si esporta solo il principio
  "validazioni in prima linea", compresso.

## COSA EREDITA IL DECK FINALE (Heister esteso)

Eredita da CVA_RDE:
1. Il sistema-figure di casa completo: stile matplotlib serif a 4 colori del deck,
   annotazioni interpretative in-figure (frecce-tesi, zone ombreggiate motivate, valori
   quotati), bar/plot con etichette dirette — con i fix e il floor E5.
2. Le strip-equazioni LaTeX→PNG uniformi a 200 DPI (nessuna equazione OMML nativa).
3. La disciplina di provenienza integrale: attribuzione per-figura in slide, disclaimer di
   ricostruzione dentro i plot, ancore di replica sovrapposte, anomalie marcate e non
   propagate — estesa anche alle 4 figure senza credito di Heister (difetto C-HEI da
   sanare).
4. Le note relatore come canale di audit parallelo (Heister le ha vuote 18/18: si
   riempiono).
5. La gerarchia visiva come sistema (titolo+kicker, divisori-slide), coi corpi emendati E2.
6. Il chrome sobrio: logo + team + numerazione N/M rigenerata (E6), palette
   #822433/#006778 — che è conferma dell'identità già presente in Heister, normalizzata.

NON eredita da CVA_RDE: la densità testo (98,2 → budget E1), i corpi 13,5-14/9 pt (→ E2),
l'assenza di placeholder (→ E3), le slide-tabellone ≥150 parole, l'architettura 5-atti da
90' senza ask né backup (→ E7).

Conserva di Heister: corpo 18 pt e densità netta ~50 (già a registro), i contenuti
CLAIM-TECNICO immutati nel merito (vincolo di censimento C-HEI); ne ripara i difetti
misurati (footer HEM, doppio contatore, master default, box fuori canvas S11, refuso
"Belleonue", figure senza credito, note vuote) attraverso il re-build in pipeline col
template emendato.

## LIMITI DEL GIUDIZIO

1. Nessun rendering composto delle slide in ambiente (limite dichiarato da entrambi i
   censimenti): la composizione testo+figure a pagina è giudicata da XML+media, non da
   screenshot; sovrapposizioni a livello slide non sono escludibili.
2. La mia verifica visiva è un campione mirato (8 media: image5, 15, 18, 19, 46, 72, 76,
   78): tutti i claim campionati reggono (2 difetti confermati, qualità confermata); per il
   resto il giudizio si appoggia ai censimenti di record, non a ri-misure.
3. Le soglie E1/E2/E5 sono classe PRACTICE: standard di pratica professionale per talk
   proiettati, non grandezze derivate; la calibrazione interna citata (18 pt, 50,2
   parole/slide) è misurata su Heister, ma la scelta delle soglie resta un giudizio
   esperto, emendabile dall'utente.
4. Non ho consultato linee guida o template imposti ESA per le milestone review: se il
   panel prescrive un formato, questa aggiudicazione va ri-aperta su quel vincolo.
5. La ripartizione dei 60' (parlato vs Q&A) non è nota: il budget slide totale discende da
   quella decisione (carrier: time-boxing modulare) e non è aggiudicato qui.
6. La riproducibilità-pipeline è stata pesata come abilitatore di costo degli emendamenti,
   non come merito di stile: se emergesse che un emendamento NON è implementabile in
   build_deck.py (es. placeholder titolo), il suo costo va ri-prezzato e l'emendamento
   resta dovuto a mano.
