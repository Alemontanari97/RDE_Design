# CENSUS — Presentazione_CVA_RDE.pptx (censimento integrale)

Data censimento: 2026-08-22. Censitore: sessione S-PRES Block 0.
Sorgente: `reference_presentations/Presentazione_CVA_RDE.pptx` — 11.160.082 byte (misurato: `Get-ChildItem`).
Arco di consumo dichiarato: questo censimento alimenta (1) l'aggiudicazione agnostica di stile per la
presentazione ESA (60 min) e (2) il giudizio di riproducibilità della pipeline deck-as-code
`../project_build` (build_deck.py). Contiene FATTI MISURATI, non un verdetto.

## Comandi di misura (disciplina SR-12)

Tutti i conteggi sono prodotti da due script stdlib eseguiti in questa finestra
(scratchpad di sessione, Python 3.13, solo zipfile/xml.etree/re/os/json + PIL per le dimensioni pixel):

- `census_cva.py` — estrazione zip integrale in `scratchpad/cva_extract/`; parse di
  presentation.xml (ordine slide da sldIdLst→rels, p:sldSz), docProps/app.xml e core.xml,
  theme1.xml (clrScheme, fontScheme), slideMaster1.xml (txStyles), per ogni slide slideN.xml +
  _rels (titolo = placeholder type title/ctrTitle; body = concatenazione di tutti gli `a:t`
  fuori dal placeholder titolo, graphicFrame incluse; `body_words = len(body.split())`;
  immagini = p:pic→blip r:embed→rels, con dimensione di display da a:xfrm/a:ext e
  DPI efficace = px/inch); note da notesSlides (esclusi placeholder sldNum/hdr/ftr/dt).
  Output: out_census.json, out_slides_report.txt, out_media.txt, out_inventory.txt.
- `aux_style.py` — istogramma `a:srgbClr val=` su tutte le slideN.xml, layout per slide dai rels,
  somme parole, pixel centrale della fascia di copertina (PIL), classe strip-equazioni.
- Lettura visiva (tool Read sulle immagini estratte): TUTTI i 61 media > 30 KB letti uno a uno,
  più 4 campioni della classe < 30 KB (image3.jpeg, image7, image9, image61) — 65 media letti su 86.

## Conteggi globali (misurati)

| Grandezza | Valore |
|---|---|
| Slide | **62** (sldIdLst; app.xml concorda: Slides=62, HiddenSlides=0) |
| Dimensione slide | 12192000×6858000 EMU = **13,33×7,50 in — 16:9** (PresentationFormat "Widescreen") |
| Master / Layout / Temi | **1 master, 2 layout** ("Diapositiva titolo" usato 1 volta; "Titolo e contenuto" 61 volte), 3 theme part |
| Note relatore | 57 part notesSlide; **56 slide con testo note non vuoto** (vuote: 1, 4, 17, 26, 37, 56) |
| Media | **86 file** (83 .png = 10.714.866 B; 3 .jpeg = 169.565 B); nessun media orfano (tutti referenziati da .rels) |
| Classi media | 4 brand (fasce/loghi Sapienza) + **32 strip-equazioni LaTeX→PNG** (criterio misurato: h<300 px e w/h≥2,5; tutte esattamente a 200 DPI efficaci) + 50 figure (plot/diagrammi/figure di paper) |
| Grafici nativi / SmartArt / OLE / video / hyperlink | **0 / 0 / 0 / 0 / 0** (misurato sui rels e sull'XML di tutte le slide) |
| Equazioni OMML native | **0** — tutte le equazioni sono PNG renderizzate |
| Tabelle native (a:tbl) | **8 slide**: 5, 19, 20, 21, 25, 30, 48, 54 |
| Parole | body Σ=6.087 (media 98,2/slide, mediana 95, min 28, max 206); note Σ=4.587; app.xml dichiara Words=14639 (tokenizzazione PowerPoint, non confrontabile 1:1 — i numeri di record sono quelli misurati) |
| Sezioni pptx | NESSUNA (p14:sectionLst assente); i divisori sono slide dedicate |
| Font incorporati | NESSUNO (ppt/fonts/ assente) |
| Provenienza file | core.xml: creator "Matteo Fiore", created 2022-03-14; lastModifiedBy "Alessandro Montanari", modified 2026-07-09; revision 174; app "Microsoft Office PowerPoint" 16.0; TotalTime 11223 min |
| Zip entries | 352 |

Nota di misura sul conteggio parole: le slide NON usano il placeholder titolo (vedi Stile), quindi
`body_words` include la striscia di intestazione presente su ogni slide 2-62
("T(H)RUST team · Detonation & Rotating Detonation Engines · N/62", ~7 parole) e le righe
titolo/sottotitolo. Il contenuto "vero" per slide è quindi ~10-15 parole sotto il numero riportato.

## Tabella per-slide

Convenzione titolo: primo blocco di testo dopo la striscia di intestazione (nessun placeholder titolo esiste).
"(+logo)" = image4.png (logo Sapienza, header) presente su OGNI slide 2-62: non ripetuto in tabella.
Parole = body_words misurate (intestazione inclusa).

| # | Titolo | Contenuto | Ruolo | Parole | Figure (lette visivamente) |
|---|---|---|---|---|---|
| 1 | (copertina) Detonation and Rotating Detonation Engines | Autore, Sapienza, sottotitolo ("A rigorous thermo-gasdynamic treatment..."), "Graduate lecture · 90 minutes" | apertura | 28 | image1/3 (fasce piene cremisi #822434), image2 (banner logo Sapienza) |
| 2 | Outline | 5 "movimenti" I-V con sottotemi; filo dichiarato: "the entropy of a combustion wave" | agenda | 132 | (+logo) |
| 3 | Why detonation for propulsion? | Pressure-gain vs Brayton; RDE = realizzazione continua; bar chart CJ live | motivazione | 120 | image5: bar chart U_CJ 9 coppie propellenti (matplotlib casa, teal/cremisi, valori e M sulle barre) |
| 4 | Part I — Detonation as a thermo-gasdynamic phenomenon | Divisore con tesi di sezione | divisore | 32 | — |
| 5 | Deflagration vs. detonation | Tabella nativa di confronto (7 proprietà, valori tipici) | teoria | 136 | — (tabella nativa) |
| 6 | The combustion wave as a discontinuity | Volume di controllo nel wave frame; 3 jump conditions | teoria | 58 | image6: diagramma CV vettoriale casa (reactants/products, onda cremisi) |
| 7 | Rankine–Hugoniot jump conditions | Massa/quantità di moto/energia in forma di entalpia totale; 1 parametro libero | teoria | 104 | image7-10: 4 strip-equazioni LaTeX (nitide, 200 DPI) |
| 8 | The heat-release parameter q | Definizione rigorosa q_c (W&S Eq. B1); numeri per H2/CH4, aria/O2 | teoria | 114 | image11-13: 3 strip-equazioni |
| 9 | The Rayleigh line | Retta nel piano (p,v), pendenza = flusso di massa; regione proibita | teoria | 89 | image14 (strip-eq); image15: plot Rayleigh+Hugoniot con famiglia M1, annotazione "CJ tangency" |
| 10 | The Hugoniot curve | Luogo degli stati finali; famiglia in q̃ | teoria | 103 | image16 (strip-eq); image17: plot famiglia Hugoniot (colormap plasma, punti CJ) |
| 11 | Rayleigh line meets Hugoniot | Mappa completa: 5 regioni, 2 tangenze, regione proibita ombreggiata | teoria | 79 | image18: plot sintesi (cremisi/teal/ocra, etichette dirette sulle curve, zone grigie) |
| 12 | The Chapman–Jouguet condition | Tangenza = sonico = velocità minima; classificazione rami; forme chiuse one-γ | teoria | 117 | image19-22: 4 strip-equazioni |
| 13 | CJ as an entropy extremum | Δs minimo (detonazione) / massimo (deflagrazione) esattamente ai punti CJ | teoria | 82 | image23: plot Δs/R vs v2/v1 con estremi annotati e parametri nel riquadro |
| 14 | Resolving the wave: the ZND model | Shock inerte + zona di reazione; spike von Neumann; ruolo di Δᵢ | teoria | 97 | image24: diagramma p(x) stile casa (CJ plane, vN spike, induzione) |
| 15 | ZND governing equations | Termicità; ODE con fattore 1/(1−M²); condizione di regolarità = CJ | teoria | 102 | image25-26: 2 strip-equazioni |
| 16 | ZND structure — computed | zndsolve ufficiale (GRI-3.0): p_vN/p1≈27, Δᵢ=0.245 mm H2/air | risultato | 87 | image27: plot p/T/termicità vs x con zona induzione ombreggiata |
| 17 | Part II — Worked examples (SD Toolbox / Cantera) | Divisore | divisore | 34 | — |
| 18 | Computing the CJ state | Algoritmo CJspeed (min della velocità sull'Hugoniot di equilibrio); box validazione vs Caltech (0,5%) | metodo | 153 | (+logo; box testuale di validazione) |
| 19 | CJ states — twelve propellant combinations | Tabella nativa 12 miscele (U_CJ, M_CJ, p2/p1, T2, γ_e vs γ_fr) | risultato | 164 | image28: strip-eq cremisi γ_e≡ρ2a²_eq/p2 ≈1.13-1.17 ≠ frozen |
| 20 | SD Toolbox vs. published values | Tabella nativa: 5 miscele vs Shepherd–Kasahara Table 2 (≤0,1% su U_CJ) | validazione | 107 | image29: scatter p2/p1 & T2 vs M_CJ con banda modello a 2 assi colorati |
| 21 | The one-γ model vs. real thermochemistry | Tabella nativa: fuel-air ≤2%, fuel-O2 +25-40%; q_eff/q_c | risultato | 128 | — (tabella nativa) |
| 22 | Effect of equivalence ratio | U_CJ(φ) per 3 fuel-air; massimi lievemente ricchi | risultato | 86 | image30: plot 3 curve con marker |
| 23 | CJ speed — dilution and initial state | Diluizione = leva più forte; p1 debole (log), T1 lenta inversa | risultato | 50 | image31: U_CJ,T_CJ vs β diluizione (2 assi); image32: 2 pannelli p1/T1 |
| 24 | ZND reaction zones across propellants | Δᵢ spanna ~12×; lega la detonabilità alla geometria del canale | risultato | 93 | image33: termicità normalizzata 4 miscele, asse x log |
| 25 | Models & assumptions map | Tabella nativa "phase rule": quale termochimica/γ dove, con ancora V&V per riga (96/96, 18/18...) | metodo (mappa onestà) | 206 (max) | — (tabella nativa) |
| 26 | Part III — The thermodynamic advantage | Divisore | divisore | 33 | — |
| 27 | Three idealised combustion cycles | Brayton/Humphrey/FJ su chimica reale CH4-air, π_c=5, p_CJ≈56 bar | teoria+risultato | 89 | image34: piano p-v log con i 3 cicli e annotazioni ZND/leading shock |
| 28 | The Fickett–Jacobs cycle | Ciclo pistone-cilindro; η fuel-air 0.28-0.31 > fuel-O2 (dissociazione) | teoria+risultato | 127 | **image35: FIGURA RIUSATA** W&S JPP 2006 Fig. 1 (sequenza pistone a-h, grayscale, attribuzione in slide); image36: strip-eq η_th |
| 29 | Cycle efficiency compared | A π_c fissato: FJ ≳ Humphrey > Brayton; caveat inversione a picco fissato | risultato | 92 | image37: η(π_c) 3 cicli con avvertenza nel plot; image38 strip-eq |
| 30 | The one-γ cycle family and q̃ | Famiglia A22 ricreata; mappatura curve→miscele reali; limiti fuel-O2 | risultato | 88 | image39: famiglia η(π_c) con nota di mappatura nel plot; image40 strip-eq; mini-tabella nativa |
| 31 | A crucial subtlety | Stato STATICO vs STAGNAZIONE fissato: il frame decide il verdetto | teoria (svolta narrativa) | 125 | **image41: FIGURA RIUSATA** W&S AIAA 2004-1033 Fig. 2 (schema onda, grayscale, piccola, attribuzione in slide) |
| 32 | The entropy penalty of a standing detonation | Split Δs_min/Δs_irr: 3,5% vs 56,7% irreversibile | risultato | 95 | image42 strip-eq; image43: bar chart impilato con quote |
| 33 | Where the total pressure goes | pt2/pt1 = 0,074/0,054 a M1≈4,6-5: ~93-95% distrutto dallo shock | risultato | 82 | image44: plot log pt2/pt1 vs M1, onda completa vs shock solo, punti CJ |
| 34 | Rotating vs. standing detonation | Il reference frame è tutta la storia (sintesi visiva) | sintesi | 37 | image45: diagramma 2 pannelli casa (rotating/standing, verdetti sotto) |
| 35 | Same cycles, two verdicts | η vs M0: 0.86/0.83/0.82 vs 0.35; esistenza standing solo M0>4.25 | risultato | 105 | image46: plot sintesi con zona non-esistenza ombreggiata e valori quotati |
| 36 | Quantifying pressure gain — EAP | EAP_i = pressione totale equivalente a pari spinta ideale; caso lavorato +49%; medie di p_t sbagliate | metodo+risultato | 89 | image47 strip-eq; **image48: FIGURA RIUSATA** contorni CFD T/logP/Mx (colormap jet, K&P/NASA, attribuzione in slide); image49: diagramma concettuale casa EAP (denso, con disclaimer "concept figure" nel piede) |
| 37 | Part IV — Thrust models for RDEs | Divisore | divisore | 31 | — |
| 38 | The Rotating Detonation Engine | Principio annulus, fronte a ~U_CJ, esausto assiale | contesto | 95 | image50: diagramma annulus casa (fresh layer, fronte) |
| 39 | The Shepherd–Kasahara model problem | Fixture sperimentale srotolata sul piano periodico; obiettivo closed-form | metodo | 48 | **image51: FIGURA RIUSATA** SK GALCIT FM2017.001 Fig. 1 (3D + piano θ-z, stile del paper, attribuzione in slide) |
| 40 | Thrust from a control-volume balance | Due CV equivalenti: exit-plane (razzo) vs injector face (termini I/II/III) | teoria | 92 | image52: diagramma doppio CV casa con equazioni e sottotermini etichettati; image53-54 strip-eq |
| 41 | Detonation of a layer: the triple point | Shock obliquo + PM + triple point autosimile; solo H e Δp_CJ contano | teoria | 79 | image55: diagramma casa con inserto zoom TP e box "matching" |
| 42 | Shock-polar matching at the triple point | Soluzione grafica PM∩polare; θ3 cresce con l'energia; origine di K | risultato | 109 | image56: 3 pannelli polari (C2H4-air, H2-air, C2H4-O2) termochimica reale |
| 43 | Pressure-history model | ψ=e^(−αξ), K=1.02/1.54; F_I=Δp_CJ·W·H·K; N si cancella | metodo+risultato | 85 | image57-58 strip-eq; image59: modello vs tracce CFD S&K "stylised reconstruction... not digitized" (disclaimer NEL plot) |
| 44 | Pressure-history performance maps | Spinta specifica ∝ U_CJ; Isp_f guidata da 1/Y_f | risultato | 74 | image60: 2 pannelli (6 combinazioni); image61 strip-eq |
| 45 | Axial-flow model | Swirl netto nullo (rotalpia); espansione sull'isentropa di equilibrio per il CJ | teoria | 100 | image62 strip-eq (+image10 riusata da slide 7); image63: diagramma annulus+unwrap casa |
| 46 | The CJ isentrope, Pm and the sonic maps | Pm≈0.24 p2 = pressione di ristagno efficace; plateau di T/Ṁ; regole di primo taglio | risultato | 134 | image64: 2 pannelli h(P)+plateau con stati numerati; image65: sensibilità T1/p1 con ancore "Table 2" a rombo |
| 47 | Validation against CFD and experiment | Kato +20-60% (mixing); Rankin/Schauer bracketed; X rosso = replica −0.1% | validazione | 93 | image66: 2 pannelli con dati ridisegnati e nota "representative — reconstructed... (not digitized)" nel piede |
| 48 | Thrust models vs. literature | Tabella nativa replica SK Table 1; anomalia 704 s* documentata, mai propagata | validazione | 139 | image67: scatter F/Ṁ vs U_CJ con retta |
| 49 | Stechmann–Heister performance model | Catena razzo 0-D quasi-stazionaria; Isp mass-weighted | metodo | 91 | **image68: FIGURA RIUSATA** SHH JSR 2019 Fig. 1 (piano di iniezione, attribuzione in slide); image69-71 strip-eq |
| 50 | Cycle histories: chamber pressure and c* | Blowdown esponenziale periodico; ancore 71.8/72 atm, 2329/2330 m/s | risultato | 101 | image72: 2 pannelli con ancore del paper annotate; image73 strip-eq |
| 51 | Mass flux and the matching protocol | Choked sempre; protocollo massa+gola uguali; pivot comune | metodo+risultato | 106 | image74: 2 pannelli mass flux (famiglie T_i) |
| 52 | The DC shift | Media camera +2.5-4.5% vs CP; replica ±0.05 pt con overlay del paper | risultato | 102 | image75: plot con marker replica sovrapposti a cerchi/quadrati "paper Fig. 7" |
| 53 | Transient thrust coefficient and Isp(ε) | Bell fuori progetto nel tail; aerospike si adatta; +2.6%/+7.3% | risultato | 87 | image76: 2 pannelli (NOTA: nel pannello sx un'annotazione collide con la legenda — unico difetto di leggibilità osservato nei plot casa) |
| 54 | Nozzle optimisation — bell vs. aerospike | Tabella nativa: replica 18/18 righe Stechmann Table 1; vuoto: vantaggio collassa | validazione | 144 | image77: 2 pannelli C_F(t) e Isp(ε) con ottimi cerchiati |
| 55 | Aerospike nozzles and model results | ~6-8% realizzabile; aerospike preferito; warning di misurabilità | sintesi | 109 | **image78: FIGURA RIUSATA** Stechmann Fig. 2 (plume 3 regimi, raster grossolano ~154 DPI, attribuzione in slide) |
| 56 | Part V — RDE engineering practice | Divisore (Wolański) | divisore | 35 | — |
| 57 | From spin detonation to the RDE | Timeline 1940-oggi (Zel'dovich→Voitsekhovskii→patent→volo 2008) | contesto | 113 | **image79: FIGURA RIUSATA** Wolański Fig. 28 (camera anulare, grayscale, attribuzione in slide) |
| 58 | The unrolled annulus and the wave number | Piano 2D periodico; W = t_rev/t_refill; regimi W≈n / galloping / deflagrazione | teoria+contesto | 89 | **image80: FIGURA RIUSATA** Wolański Fig. 43 (CFD unwrap a colori); image81 strip-eq W (cremisi); **image82 RIUSATA** Fig. 37 (grayscale) |
| 59 | Feeding the wave: injection and geometry | Sawtooth per giro: choked→subsonico→INVERTITO; zoo di geometrie | contesto | 84 | **image83: FIGURA RIUSATA** Fig. 30 (5 geometrie, scansione line-art); **image84 RIUSATA** Fig. 31 (stati iniettore a/b/c) |
| 60 | Standing waves and pulsed engines | ODWE frame-locked (M≈5-7 soltanto); PDE valvole/purge; verdetto per il rotante | contesto+sintesi | 101 | **image85: FIGURA RIUSATA** Fig. 6 (ODWE); **image86 RIUSATA** Fig. 14 (ciclo PDE, scansione datata di qualità legacy) |
| 61 | Summary | 5 bullet: catena jump conditions → CJ/ZND → cicli → EAP → CV thrust → Isp motore | chiusura | 182 | (+logo) |
| 62 | References | Fonti primarie raggruppate per tema + dichiarazione: figure originali con attribuzione per-slide, numeri tracciabili agli script | riferimenti | 201 | (+logo) |

## Sezione narrativa

L'arco è una lezione magistrale a 5 atti con spina dorsale dichiarata in slide 2 ("dove nasce
l'entropia di un'onda di combustione, e chi la paga"): copertina+agenda+motivazione (1-3), poi
Parte I fenomenologia (4-16: jump conditions → Rayleigh/Hugoniot → CJ → ZND), Parte II esempi
calcolati e validati SD Toolbox/Cantera (17-25, chiusa dalla "mappa di onestà" delle assunzioni),
Parte III vantaggio termodinamico e sua INVERSIONE statico/stagnazione (26-36, climax narrativo in
31-35, chiusa da EAP), Parte IV modelli di spinta (37-55: Shepherd–Kasahara pressure-history +
axial-flow, poi Stechmann–Heister con ugelli bell/aerospike), Parte V pratica ingegneristica da
Wolański (56-60). Chiusura: summary a 5 bullet (61) e references con dichiarazione di tracciabilità
(62). I divisori sono slide contate (4, 17, 26, 37, 56), non sezioni pptx. NON esistono slide di
backup/appendice né una slide di "ask": coerente con il genere dichiarato in copertina
("Graduate lecture · 90 minutes") — NON è il formato milestone-review ESA a 60 min; l'adattamento
di genere (ask, backup, time-boxing) andrebbe aggiunto, non c'è da copiare.
Le validazioni non sono relegate in appendice ma sono slide di prima linea (18, 20, 25, 47, 48,
52, 54): la replica della letteratura È parte della storia.

## Sezione stile (fatti misurati per l'aggiudicatore)

**Palette.** theme1.xml è in scala di grigi (dk2 000000, lt2 F8F8F8, accent1-6 DDDDDD→4D4D4D):
il tema NON porta l'identità. I colori operativi sono hard-coded per run/shape (istogramma
`a:srgbClr` su tutte le slide): **#822433 cremisi Sapienza ×384**, #2B2B2B inchiostro ×368,
#FFFFFF ×309, #F2ECED tinta chiara ×132, **#006778 teal ×106**, #004D59 teal scuro ×53.
Il pixel centrale della fascia di copertina misura #822434 (jpeg del cremisi). Le figure di casa
usano ESATTAMENTE la stessa coppia cremisi/teal + ocra + navy: coerenza slide↔figure totale.

**Tipografia.** Theme fonts Calibri Light/Calibri MAI usati nelle slide: ogni run dichiara
**Palatino Linotype** (970 occorrenze; 4 "Palatino"). Font NON incorporati nel file (rischio di
sostituzione fuori da Windows). Gerarchia misurata dall'istogramma dei corpi espliciti (pt:count):
titolo slide 30 pt (×61) + kicker/sottotitolo 24 pt (×61); divisori 38 pt (×5) + 17 pt;
corpo bullet dominante 13.5-14 pt (14.0×147, 13.5×114); tabelle e note di figura 9-12.5 pt
(9.0×11 ... 12.5×87); minimo assoluto 6 pt (×1, slide 18). Default del master (44/28 pt) ignorati.

**Struttura template.** 1 master + 2 soli layout (nomi italiani, "Diapositiva titolo" ×1 e
"Titolo e contenuto" ×61) — ma NESSUNA slide usa il placeholder titolo: i titoli sono text box
liberi. Conseguenza misurata: app.xml TitlesOfParts = "Presentazione standard di PowerPoint" ×62
(outline view e accessibilità cieche sui titoli). Chrome costante su ogni slide 2-62: logo Sapienza
(image4) + "T(H)RUST team" + titolo lezione + **numerazione N/62**.

**Densità testo.** Media 98,2 parole body/slide (mediana 95, min 28, max 206) — intestazione
(~7 parole) e righe titolo incluse nel conteggio. Slide ≥150 parole: 5 (18, 19, 25, 61, 62 — due
sono tabelle-mappa, due sono summary/references). Slide di contenuto tipica: 3-5 bullet da una
riga e mezza + 1-2 figure. 8 tabelle native dense ma con corpo 9-12 pt leggibile.

**Figure — inventario di qualità (lettura visiva di tutti i media >30 KB).**
- 50 figure totali: ~36 di produzione propria (plot matplotlib + diagrammi vettoriali) e
  **14 figure di paper riusate** (image35, 41, 48, 51, 68, 78, 79, 80, 82, 83, 84, 85, 86 + il
  pannello CFD in image48), concentrate dove si espone il lavoro altrui (FJ, fixture SK, SHH,
  Wolański 57-60).
- Plot di casa: stile unico e riconoscibile (serif/LaTeX, stessi 4 colori del deck, assi grandi,
  niente chartjunk), DPI efficace 152-489 (mediana ~245); font degli assi sempre leggibili alla
  dimensione di display (nessun testo apparente sotto ~10 pt). Marchio distintivo: annotazioni
  interpretative DENTRO il plot (frecce, quote numeriche, zone proibite ombreggiate, box parametri).
- Strip-equazioni: 32 PNG uniformi a 200 DPI, nitide; le equazioni-chiave in cremisi, le altre nere.
- Figure riusate: qualità da scansione/paper (le Wolański image83/86 sono line-art datate, il
  pannello CFD image48 usa colormap jet, image78 raster ~154 DPI) — adeguate alla dimensione di
  display ma visibilmente NON native dello stile del deck.
- Difetti osservati nei plot di casa: 1 collisione annotazione/legenda (image76, slide 53, pannello
  sx); 1 annotazione che tocca il bordo pannello (image72, slide 50). Nient'altro rilevato sui 61
  media letti.

**Disciplina di provenienza (misurata sul testo slide + dentro le figure).**
- Attribuzione "Adapted from <autori, rivista/report, anno, Fig. N>" SULLA slide per ogni figura
  riusata (slide 28, 31, 36, 39, 49, 55, 57, 58, 59, 60 — riga per riga nel body estratto).
- Onestà di ricostruzione dichiarata NEI plot: "stylised reconstruction ... not digitized"
  (image59), "data points representative — reconstructed from the deviations reported" (image66),
  "concept figure; per-cell fields illustrative, calibrated to the paper worked example" (image49).
- Ancore di replica sovrapposte ai dati del paper (image65 "Table 2 anchors", image75 "paper
  Fig. 7", image77 "Table 1 optima"); anomalia di letteratura marcata con asterisco e mai
  propagata (slide 48, 704 s*).
- Slide references (62) chiude con la dichiarazione di tracciabilità agli script compagni; le note
  relatore (56/62 slide, Σ 4.587 parole) portano i numeri di audit (96/96, 18/18, γ-audit) — le
  note sono un canale di provenienza parallelo, non un copione.
- Nessun puntatore a slide di backup (non esistono backup).

**Fatti rilevanti per il giudizio di riproducibilità pipeline.** Tutto il contenuto grafico è
raster referenziato (nessun grafico nativo/OLE/SmartArt), equazioni = PNG LaTeX a 200 DPI uniformi,
colori e font hard-coded run per run, chrome e numerazione N/62 identici su 61 slide: firma
coerente con generazione programmatica (build_deck.py) sopra un template .pptx preesistente
(creator 2022 "Matteo Fiore", layout in italiano). Il file round-trippa da PowerPoint 16
(lastModified 2026-07-09, revision 174) senza media orfani.

## Limiti dichiarati del censimento

1. Non ho eseguito il rendering delle slide composte (nessun PowerPoint/LibreOffice invocabile):
   la composizione testo+figure sulla pagina è inferita da posizioni/dimensioni XML e dalla lettura
   dei media, non da uno screenshot. Sovrapposizioni A LIVELLO DI SLIDE non sono escludibili
   (quelle DENTRO le figure sì: lette).
2. 21 media della classe <30 KB non letti singolarmente (letti 4 campioni): sono tutti
   strip-equazioni per criterio dimensionale misurato (h<300 px, w/h≥2,5, 200 DPI) — il contenuto
   matematico esatto di ciascuna strip non è verificato una per una.
3. `body_words` include intestazione e titoli (nessun placeholder separa il titolo): la densità
   "contenuto puro" è sistematicamente ~10-15 parole sotto il valore riportato.
4. app.xml Words=14639 non riconciliato esattamente con la mia somma (10.674 body+note): la
   tokenizzazione PowerPoint conta elementi che il mio split su whitespace non replica; i conteggi
   di record sono i miei, col comando citato.
5. La corrispondenza figura-riusata ↔ figura del paper originale è verificata sulla dichiarazione
   in slide + aspetto visivo, non per confronto pixel col PDF sorgente (fuori scope Block 0).
6. Nessuna verifica dei 3 theme part oltre theme1 (theme2/3 = temi dei notesMaster/handout, non
   delle slide).
