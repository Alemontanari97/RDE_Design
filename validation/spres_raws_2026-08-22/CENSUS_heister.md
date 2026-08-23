# CENSUS ppt_Heister.pptx — censimento integrale (S-PRES Block 0)

Data: 2026-08-22. Censore: sessione S-PRES, task censimento deck-da-estendere.
File censito: `reference_presentations/ppt_Heister.pptx` (12,689,146 byte misurati).

## Comandi di misura (SR-12)

Tutti i conteggi di questo documento sono stati misurati in questa finestra dai seguenti
script (Python 3.13.14, solo stdlib: zipfile, xml.etree.ElementTree, re, os, struct),
eseguiti su estrazione in scratchpad `heister_extract/`:

1. `census_extract.py` — namelist zip, ordine slide da `p:sldIdLst` + rels, dump testo
   per-slide (`a:t` per paragrafo), tabelle/chart/immagini per slide, note, hit keyword.
2. `census_style.py` — geometrie text-box per slide, istogramma colori `srgbClr`,
   istogramma `sz` font, rels video, testo master/layout, durata mp4 (parse `mvhd`).
3. `census_footer.py` — forensica footer (fill, placeholder, colori run), parole
   raw/nette per slide (nette = escluse 4 classi di boilerplate ricorrente).
4. `census_pics.py` — geometria di ogni `p:pic` per slide, placeholder del layout.

Percorso script: `C:\Users\amont\AppData\Local\Temp\claude\...\scratchpad\heister_census\`
(output intermedi `00_inventory.txt` … `06_pics_layout.txt` ivi conservati).
Lettura visiva media: tool Read su tutte le immagini > 30 KB (33 file) + campione
delle piccole (image3, image4, image23, image28, image30, image33, image36, image200).

## Conteggi globali (misurati)

| Grandezza | Valore |
|---|---|
| Slide (sldIdLst) | 18 — ordine di presentazione == numero file slideN.xml per tutte le 18 (verificato) |
| Note slides | 18 — TUTTE vuote di contenuto (solo numero pagina, 1 parola ciascuna) |
| Media | 49 file = 47 immagini + 2 video mp4 (media1.mp4 ~26.3 s su slide 10; media2.mp4 ~13.6 s su slide 16) |
| Master / Layout / Temi | 1 master; 2 layout ("Diapositiva titolo", "Titolo e contenuto"); 3 theme xml |
| Dimensione slide | 12192000 x 6858000 EMU = 13.33 x 7.50 in = **16:9** |
| Tabelle / Chart nativi | 0 / 0 (nessun `a:tbl`, nessun chart) |
| Parole testo slide | raw 1243; **nette 903** (escluso boilerplate ricorrente, v. sotto); media netta 50.2/slide, max 151 (slide 18) |
| Lingua | Inglese (testo slide); template/istallazione PowerPoint in italiano (nomi layout, prompt "Fare clic…") |
| Proprietà file | creator: Matteo Fiore (2022-03-14); lastModifiedBy: Alessandro Montanari (2026-05-13); revision 174 |

Boilerplate ricorrente su ogni slide 2-18 (escluso dal conteggio netto): testo residuo
"HEM modeling for subcritical flows…" (11 parole), "T(H)RUST team", "Rotating Detonation
Engine Activities" (footer), contatori "N/18" e "N /17|18".

## TABELLA PER-SLIDE

Parole = nette (senza boilerplate). Figure = immagini di contenuto univoche (escluso il
logo Sapienza image2.jpeg presente su tutte le 18 slide).

| # | Titolo/heading osservato | Contenuto | Ruolo narrativo | Vincolo | Parole | Figure |
|---|---|---|---|---|---|---|
| 1 | Rotating Detonation Engine Activities – T(H)RUST | Autori: A. Montanari, M. Grossi, A. Falco, F. Nasuti; composizione banner Sapienza | Apertura | STRUTTURA | 14 | 0 (3 decorative) |
| 2 | Research Roads / Group Overview | 5 card: attività "newborn" (~1.5 anni R&D), focus numerico URANS/low-order, rete internazionale (BEFAST/NC State Braun, RMIT Michalski, ISAE-ENSMA "Belleonue" [probabile refuso per Bellenoue]), HYPERDE, open research lines (refill, turbine bladeless, disk RDE, nozzle design, heat flux) | Mappa del deck | MISTO (istituzionale + claim di capability HYPERDE) | 93 | 0 |
| 3 | Code Development and Capabilities — HYPERDE | Architettura ibrida-dimensionale: Chamber 3D/Q2D unwrapped, Plenum 3D/Q2D, Injectors fino a quasi-1D, Expansion System 3D URANS accoppiato (choked/unchoked); rationale dimensionalità | Pilastro codice | CLAIM-TECNICO | 100 | 0 |
| 4 | Code Dev — General features of the solvers' suite | FV; II ordine spazio, fino a III tempo; turbolenza modulare; thermo tabulata gas termicamente perfetto; pre-processing .yaml; OpenMP+MPI; Riemann solvers, ODE stiff; interfaccia con solutori in-house solid/multiphase/real-fluid | Capability | CLAIM-TECNICO | 86 | 0 |
| 5 | Code Dev — Q2D solver, innovation w.r.t. recent literature | Flussi diffusivi rigorosi + RANS generiche; derivazione generale z=z(x,y); BC BFS non-isentropica adattata a CFD, cit. [1] Fievisohn & Yu JPP 2017; schema unwrapped con lateral expansion + schema disk side-view + contour T disk | Claim di novità | CLAIM-TECNICO | 68 | 3 |
| 6 | Code Dev — V&V (ZND) | Validazione vs 1D ZND H2/Air da SDT; 2 plot XY (T e p vs x, CFD vs ZND sovrapposti) | Evidenza V&V | CLAIM-TECNICO | 14 | 2 |
| 7 | Code Dev — V&V (unwrapped letteratura) | Test case unwrapped [2] Schwer & Kailasanath AIAA 2012; contour Mach unwrapped + plot p(y) "Sapienza CFD" vs "Schwer et al." | Evidenza V&V | CLAIM-TECNICO | 36 | 2 |
| 8 | Code Dev — V&V (feature HYPERDE, AR=0.4) | Assessment Q2D source terms: contour M; plot Mach Q2D vs Area Law con profilo ugello (legenda "Nozzle Profile"); plot p0(y) per AR=1/0.8/0.6/0.4 | Evidenza V&V | CLAIM-TECNICO | 23 | 3 |
| 9 | Code Dev — V&V (accoppiamento iniettori) | Profili T(y) e u(y): MQ2D vs Q2D Resolved vs Q2D BC; contour M riusato (image9) | Evidenza V&V | CLAIM-TECNICO | 19 | 3 |
| 10 | Code Dev — V&V (connessione Q2D-3D) + VIDEO | Anello p su piano (Q2D BC), cilindro 3D con fronte di detonazione, contour M; video media1.mp4 (~26 s) | Evidenza V&V + demo | CLAIM-TECNICO | 19 | 3 + video |
| 11 | Characterization of Refill Region Dynamics (with RMIT and NCSU) | 4 domande di ricerca (geometria vs espansione refill; strato supersonico; modellabilità; perdite p0); inlet divergenti: introdotti per mitigare perdite BFS ma evidenza exp+num di performance degradata; figure paper-style (luminescenza α=5°; setup ε=7/10.9 quarzo H2/Air) + contour U per 6.5°/7.5°; 1 text-box FUORI CANVAS | Apertura linea 1 | MISTO (domande aperte + claim con evidenza) | 78 | 4 (+3 micro-annotazioni) |
| 12 | Characterization of Refill Region Dynamics (Λ sweep) | 4 pannelli contour p (MPa) con linee caratteristiche/espansione per diversi Λ; heading DUPLICATO come PNG (con simboli Λ) sopra text-box nativo; label caso "Λ=1, 2D, ε=0°, PG=+56.7%" e simili come micro-PNG; claim: aree refill parzialmente supersoniche, crescita perdite con Λ, per Λ=2.9 inlet line interamente supersonica e PG negativo | Risultato quantitativo | CLAIM-TECNICO | 51 | 14 (4 pannelli + colorbar + 9 PNG testo/label) |
| 13 | Characterization of Refill Region Dynamics (modello) | Schema a 2 pannelli "Subsonic refill" vs "Supersonic refill" (slip line, expansion lines, iso M=1, zone coupled/de-coupled, pressioni determinanti) — figura di sintesi modellistica del gruppo | Sintesi modellistica | CLAIM-TECNICO | 5 | 1 |
| 14 | Supersonic Bladeless Turbines (with NCSU) | Design CFD del wind tunnel supersonico NCSU (fino a Mach 4 non-reattivo; nozzle intercambiabile + second-throat diffuser); contour M+p turbina conica; FOTO hardware ("Mach 1.6 nozzle", "Conical turbine", "NEUMOTOR BLDC") | Apertura linea 2 | CLAIM-TECNICO | 43 | 2 |
| 15 | Supersonic Bladeless Turbines (validazione tunnel) | 4 pannelli MATLAB "Nozzle Pressure Ratio" P0=2.95/4.34/5.12/5.52 bar (isentropico vs sperimentale vs CFD); contour M a/b/c del tunnel; p0=3/4 bar | Evidenza | CLAIM-TECNICO | 53 | 2 |
| 16 | Supersonic Bladeless Turbines — Ongoing + VIDEO | Shape optimization turbina (matrice 6 contour Mach 1.8→4.5); CFD ejector-diffuser per RDE testing; foto cella prove; video media2.mp4 (~14 s) | Stato/prospettiva | MISTO (piani ongoing + figure tecniche) | 20 | 2 + video |
| 17 | Disk RDEs (with RMIT and ISAE-ENSMA) | Collaborazione PPRIME; CFD lead su design/analisi disk RDE H2/Air; contour 3D URANS (T fino 3450 K) vs Q2D (riuso image6) | Linea 3 | CLAIM-TECNICO | 30 | 2 |
| 18 | Nozzle Design for RDEs | MoC 2D/2D-assialsimmetrico non-isentropico three-waves come API in-house; applicazione primaria nozzle design ideal/TIC/ottimizzati; famiglie: ideal (bell, plug, shrouded plug), Rao (optimal bell/plug), Veen (optimal shrouded plug); open questions: separazione in plug/shrouded plug (shock obliquo rotante, [3]), esistenza profilo "ottimale" per RDE exhaust, esplorazione CFD dei risultati teorici di [4]; mesh 3D "Optimized shrouded plug"; refs [3] Harroun-Heister-Ruf JPP 2021, [4] Stechmann-Heister-Harroun JSR 2019 | Chiusura = GRAFT POINT | CLAIM-TECNICO | 151 | 1 |

Riusi figura misurati: image9 su slide 7/9/10; image6 su slide 5/17; image2.jpeg (logo) su tutte.

## GRAFT POINT — tutti gli hit nozzle-related (verbatim, ordine di presentazione)

Pattern primari del task (`nozzle(s)`, `ugell*`, `expansion`, `aerospike`, `plug`, `bell(s)`, `exit`), match case-insensitive a confine di parola su titoli+body+tabelle+note.

**nozzle(s)** — 6 hit:
- Slide 02 [BODY]: "Study of hot topics of the RDE community: refill region, supersonic bladeless turbines, disk RDEs, nozzle design, heat flux"
- Slide 14 [BODY]: "Swappable nozzle and second-throat diffuser system allowing for low feed pressure"
- Slide 15 [BODY]: "Swappable nozzle and second-throat diffuser system allowing for low feed pressure"
- Slide 18 [BODY]: "Nozzle Design for RDEs"
- Slide 18 [BODY]: "•  Primary application: nozzle design for ideal, TIC and optimized configurations"
- Slide 18 [BODY]: "[3]  A. J. Harroun, S. D. Heister, J. H. Ruf, “Computational and experimental study of nozzle performance for rotating detonation rocket engines,” J. Propulsion and Power 37(5), 660–673, 2021."

**ugell*** — 0 hit. **aerospike** — 0 hit nelle slide; presente però nel MASTER/LAYOUT come testo default dei placeholder footer: "Modular Aerospike Nozzles for Upper Stage Applications" (residuo del template di origine, non renderizzato sulle slide perché ogni slide sovrascrive il footer). **exit** — 0 hit.

**expansion** — 7 hit:
- Slide 02 [BODY]: "A hybrid-dimensional CFD modelling framework that solves chamber, injector, plenum and expansion with a consistent low-order formulation"
- Slide 03 [BODY]: "Expansion System"
- Slide 11 [BODY]: "How does the geometry affect the refill region expansion process?"
- Slide 11 [BODY]: "What happens if/when expansion yields supersonic Mach number in the layer?"
- Slide 12 [BODY]: "Pressure flow field comparison for different inlet expansion ratio"
- Slide 12 [BODY]: "Small amounts of expansion yield partially supersonic refill areas"
- Slide 12 [BODY]: "Supersonic area and  loss growth with increasing inlet expansion ratio"

**plug** — 3 hit (tutti slide 18):
- "•  Implemented families: ideal (bell, plug, shrouded plug), Rao (optimal bell and plug) and Veen (optimal shrouded plug)"
- "•  Separation dynamics/topology in plug / shrouded plug (effect of rotating oblique shock on incipient separation [3])"
- "Optimized shrouded plug"

**bell(s)** — 1 hit (slide 18): "•  Implemented families: ideal (bell, plug, shrouded plug), Rao (optimal bell and plug) and Veen (optimal shrouded plug)"

Sweep secondario (extra, dichiarato): **throat** su S14/S15 ("second-throat diffuser");
**diverg*** su S11 ("diverging inlets"); **exhaust** su S3 ("chamber 3D/Q2D exhaust") e
S18 ("Does an “optimal” profile exist for an RDE exhaust?"); laval/area ratio/expander: 0.

Hit a livello di FIGURA (visti in lettura visiva, non nel testo XML): legenda "Nozzle
Profile" in image12 (S8); "Throat" in image21 (S11); label "Mach 1.6 nozzle" in image39
(S14); titoli "Nozzle Pressure Ratio" in image40 (S15); image45 (S18) = mesh 3D di un
optimized shrouded plug nozzle.

### Candidato graft point: SLIDE 18 (ultima slide), "Nozzle Design for RDEs"

Motivazione:
1. E l'accenno agli ugelli "verso la fine" previsto dal mandato — di fatto e l'ULTIMA
   slide del deck: il corpo termina qui, senza backup/ringraziamenti dopo. La nuova
   sezione nozzle-program si innesta estendendo la coda del deck, con S18 come slide
   ponte/apertura di sezione, senza spostare nulla.
2. Il contenuto e esattamente il punto di aggancio del programma: la slide espone il
   MoC solver in-house (2D/2D-axi non-isentropico three-waves) e le famiglie
   ideal/Rao/Veen, e pone come open question la domanda che il programma
   cycle-averaged variational affronta: "Does an “optimal” profile exist for an RDE
   exhaust?" con "CFD exploration of the theoretical findings in [4]".
3. I riferimenti [3] Harroun-Heister-Ruf 2021 e [4] Stechmann-Heister-Harroun 2019
   sono il ponte bibliografico naturale verso la sezione nuova (coerente col nome file
   del deck).
4. Gli altri hit non sono graft point: S2 e il puntatore in avanti nella lista "open
   research lines" (da aggiornare in coerenza quando la sezione crescera); S14/S15
   usano "nozzle" nel contesto hardware del wind tunnel NCSU (linea bladeless), fuori
   tema innesto.

## NARRATIVA — arco del deck

Il deck e l'esposizione delle attivita RDE del gruppo T(H)RUST (Sapienza; autori
Montanari, Grossi, Falco, Nasuti). Arco in 4 movimenti:

1. **Apertura e mappa** (S1-S2): titolo; overview del gruppo (attivita ~1.5 anni, focus
   numerico, rete internazionale NC State/RMIT/ISAE-ENSMA, framework HYPERDE, linee aperte).
2. **Il codice** (S3-S10, 8 slide = quasi meta deck): HYPERDE, framework CFD
   ibrido-dimensionale (chamber/plenum/injectors/expansion system a dimensionalita
   dedicata), feature dei solutori, innovazioni Q2D, poi V&V in 5 slide (ZND; caso
   unwrapped di letteratura; feature Q2D; accoppiamento iniettori; connessione Q2D-3D
   con video). E la spina dorsale "strumento certificato" del racconto.
3. **Le linee di ricerca** (S11-S17): refill region con inlet divergenti (domande,
   sweep Λ quantitativo, modello subsonic/supersonic refill — con RMIT e NCSU);
   turbine bladeless supersoniche e wind tunnel NCSU (design, validazione, ongoing con
   video); disk RDE (con RMIT/ISAE-ENSMA/PPRIME).
4. **Chiusura sul nozzle design** (S18): il MoC in-house, le famiglie implementate, le
   open questions e i due riferimenti al gruppo Heister. Il deck TERMINA qui.

Confine corpo/backup: NON esistono slide di backup, ringraziamenti o "questions" — il
corpo coincide con l'intero deck (18/18). Le note presenter sono vuote (solo numeri).
Racconto: modellazione e codice + collaborazioni; nessun hardware/test proprio del
gruppo (le foto hardware sono del contesto NCSU).

## STILE — fatti misurati

**Palette effettiva** (istogramma `srgbClr` su tutte le slide; il tema dichiara una
clrScheme "Gradazioni di grigio" NON usata dai contenuti — i colori reali sono
hard-coded): #000000 x235, #2B2B2B x117 (testo), **#822433 x91 e variante #822333 x34**
(marrone Sapienza: bande header/footer, accenti), **#006778 x28** (petrolio, accento
secondario), #FF0000 x12 (enfasi), #D98291 x4, #ECC0C8 x2, #FFFFFF/bg1 (testo su banda),
#00B0F0 x1. Theme fonts dichiarati Calibri Light/Calibri (non usati dai run).

**Font effettivi** (run espliciti): Palatino Linotype x245 (corpo), Cambria Math x77
(simboli/equazioni inline), Palatino x53 (footer/counter), Times New Roman x4.
Censimento font di app.xml: Arial, Calibri, Calibri Light, Cambria Math, Palatino,
Palatino Linotype, Times New Roman.

**Gerarchia dimensioni** (istogramma `sz`): 60pt x16 (titolo S1), 32pt x18 (titoli di
sezione), 28-22pt (sottotitoli/heading card), **18pt x120 (corpo, moda)**, 16pt x38,
14pt x80 (caption/footer), 12pt x90 (riferimenti bibliografici), 10pt x24 (minimi).

**Densita testo**: media netta 50.2 parole/slide, max 151 (S18), min 5 (S13);
raw (incluso boilerplate) 69.1 di media. Slide piu dense: S18 (151), S3 (100), S2 (93),
S4 (86), S11 (78).

**Struttura visiva osservata**: banda marrone footer full-width (~0.81 in) con logo
Sapienza bottom-left (image2.jpeg su tutte le 18 slide), team a destra-centro, numero
pagina bottom-right; titolo di sezione top-left 32pt; contenuto in colonne di card o
griglie di figure (2-3 per riga); su S1 composizione banner dedicata.

**Qualita figure**: plot Tecplot/ParaView/MATLAB del gruppo ad alta risoluzione
(vettoriale-rasterizzato pulito, colorbar leggibili); 4 figure paper-style
(image5, image18, image19, image21) a risoluzione media, SENZA credito in slide;
2 foto hardware buone; equazioni/label come micro-PNG (550 B-4 KB) a bassa risoluzione.
2 video mp4 incorporati (S10 ~26.3 s; S16 ~13.6 s).

**Difetti di forma rilevati (fatti, per il lavoro di miglioria)**:
1. Testo residuo di un ALTRO deck dentro la shape della banda footer su S2-S18: "HEM
   modeling for subcritical flows in liquid rocket engine cooling systems" (14pt,
   colore ereditato, dentro la banda #822333; visibilita a render non verificabile da
   XML, presenza certa).
2. DOPPIO contatore pagina bottom-right su ogni slide: box esplicito bianco
   (x=11270512) + placeholder sldNum (x=10296000), sovrapposti; su S2 il box esplicito
   dice "2 /17" (denominatore stantio della versione a 17 slide) mentre il placeholder
   dice "2/18".
3. Master/layout portano ancora i default del template di origine: "M. Fiore et al",
   "Modular Aerospike Nozzles for Upper Stage Applications", "‹N› /17" (igiene
   template: riaffiorerebbero su ogni slide nuova creata senza override).
4. S12: heading duplicato — text-box nativo (senza simboli) + PNG renderizzato (con Λ)
   sovrapposto; equazioni e label caso come immagini non editabili (image23, 28-36).
5. S11: text-box "Inlet extension added for supersonic cases" interamente FUORI canvas
   (x=13136548 > 12192000): contenuto orfano invisibile.
6. Probabile refuso su S2: "Prof. Marc Belleonue" (atteso: Bellenoue).
7. Note presenter assenti su tutte le slide (solo numero).
8. Palette e font reali interamente hard-coded fuori tema (fragilita a restyling via theme).

## LIMITI DICHIARATI

- Nessun motore di rendering PowerPoint in ambiente: stacking/visibilita effettiva dei
  layer (in particolare il testo residuo HEM nella banda footer e la sovrapposizione dei
  due contatori) e dedotta da geometrie+z-order XML, non verificata a schermo.
- Piccole immagini non tutte lette visivamente: lette 8 su 14 sotto 30 KB; le restanti
  (image22, image210, image29, image31, image32, image34, image35, 550 B-4.1 KB) sono
  della stessa classe accertata (micro-render di equazioni/label) ma non ispezionate una
  a una.
- Video: contenuto non ispezionabile frame-by-frame (durate misurate dal box `mvhd`;
  media1 associato al contesto V&V 3D di S10, media2 al contesto cella prove di S16 e
  alla foto image42, presumibilmente poster/still coerente — inferenza dichiarata).
- Provenienza delle 4 figure paper-style (image5, image18, image19, image21) non
  determinabile dal deck: nessun credito in slide; non attribuite qui per non generare
  claim non fondati. Da risolvere in fase di miglioria (citazione per figura).
- Conteggio parole: misurato sui run `a:t` delle slide; PowerPoint (app.xml) dichiara
  Words=1689 su base di conteggio diversa (non riconciliato, entrambe le fonti citate).
- La classificazione CLAIM-TECNICO/STRUTTURA/MISTO e un giudizio di censimento sul
  testo osservato; il vincolo operativo resta: ogni modifica di contenuto su slide
  CLAIM-TECNICO/MISTO richiede fonte del gruppo, forma libera solo su STRUTTURA.
