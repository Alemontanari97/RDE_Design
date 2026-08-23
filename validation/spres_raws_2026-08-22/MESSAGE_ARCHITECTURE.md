# S-PRES — MESSAGE ARCHITECTURE (Blocco 1(a), addendum-4 upgrade 1)

Carrier: ADVISORY_Spres_prompt_2026-08-21.md AS AMENDED (5 addenda).
Constraints consumed: 60' target (addendum 5); audience = ESA
propulsion panel with NOTHING assumed on RDE/detonation physics (user
qualification 2026-08-22); every slide-claim cite-only at its rigor
class; D-44 guard (no adequacy claim); P34 light instantiation
(evidence stage declared per engine claim); query-bounded novelty;
best-of-sweep != argmax guard; CT-6 (their numbers stay theirs).

## MESSAGGIO CENTRALE (unico)

> Il campo disegna ugelli RDE collassando il ciclo in un campo
> medio e applicandogli il design steady classico (fino alle
> superfici max-thrust di Rao/Veen): risolve l'ottimo di un
> PROBLEMA SOSTITUTO, dichiarato "approximately applicable" senza
> mai quantificare l'avverbio. Noi formuliamo e risolviamo il
> problema di ottimo DEL SISTEMA PERIODICO: il funzionale
> ciclo-mediato sulla famiglia per-fase (quoziente esatto dentro la
> classe-dati dichiarata), con le SUE condizioni di ottimalità
> (transversalità e corner mediati — mai scritti dal campo,
> NOT-FOUND query-bounded), ciò che la riduzione trascura reso
> operatore-residuo con forchetta per canale, e la soluzione
> calcolata da una macchina discreto-esatta certificata — ogni
> scelta a registro, ogni numero con la sua classe di evidenza.
> argmax del sostituto ≠ argmax del problema vero: la differenza è
> Gap B (misurabile in-house) e Gap A (bounded-only, e solo noi lo
> limitiamo). L'onestà strumentata non è un limite del metodo: È il
> metodo.

(Every clause anchors: "approximately applicable" = P-C Li-Xu 2025
conclusion (3), the need-quote of record [carrier :178-180]; media
diventa teorema = [S-T0P]/[T-T0P] quotient inside the
periodic-rotating-wave pin, SCHEMA DECLARED on slide per user
decision :1450; operatore-residuo = [T-RED] K-bar=0 THEOREM*;
forchetta = [R22F-FORCHETTA] M0:1283; discreto-esatto certificato =
brick-2/engine record; scelte a registro = choice ledger 62 +
pipeline decision map refereed.)

## I 3 PILASTRI

P1 — LA MEDIA, DA SCOMMESSA A TEOREMA (rigore come struttura).
  Il campo scommette sull'average-then-design (P-D origine, P-B la
  cita come "empirically recognized"); noi: dentro il pin
  onda-periodica il quoziente rende la media ESATTA (per-fase,
  K-bar=0), T-DISC CONVICTS la riduzione p-only e ESONERA la media
  full-state sull'asse-fibra — con zero CFD. Ciò che resta è un
  residuo NOMINATO (T-RED) con deriver ordinati.
  Takeaway ing.: il per-fase non è "una media migliore": è la media
  giusta dentro una classe dichiarata, con l'errore residuo reso
  operatore.
  Takeaway progr.: la teoria è il de-risking più economico — i
  teoremi hanno sostituito campagne CFD intere (formal-first).

P2 — LA MACCHINA CERTIFICATA (design tool, non paper study).
  Pipeline discreto-esatta end-to-end: MoC certificato + thermo a
  tabelle + TR-Newton segmentato + certificati/oracoli/gate; 62
  scelte algoritmiche aggiudicate a registro (12 DECIDED / 36 MIXED
  / 12 NEVER / 2 SA — dichiarate, non nascoste); mappa decisionale
  refereed (0 BREAK / 0 REPAIR su 45 archi); engine: val_grad 0.45 s,
  campagna 10-14 min, 18x speedup di record. Evidence stage
  DICHIARATO per ogni claim engine (P34 rider).
  Takeaway ing.: ogni anello ha alternative pesate + falsificatore:
  il grafo si cammina, nodo per nodo.
  Takeaway progr.: la macchina è veloce abbastanza da rendere le
  campagne di validazione (M-RED, paired-run) atti economici.

P3 — IL VALUE CASE ONESTO (Gap A / Gap B).
  Gap B = J3D(x*_per-fase) - J3D(x*_legacy): misurabile IN-HOUSE
  (paired-run F2: nostro funzionale vs Veen/Angelino-at-mean).
  Gap A = distanza dall'ottimo 3D vero: INCOMPUTABILE per chiunque —
  nessun paper ha MAI ottimizzato il 3D vero (sweep e redesign
  manuale soltanto: guard best-of-sweep != argmax) — noi siamo gli
  unici a LIMITARLO (schema delta/mu + spot-check R22-CFD).
  Value condition esplicita: Gap B materiale AND Gap A < Gap B.
  Takeaway ing.: bound-or-estimate dichiarato cella per cella; MAI
  adequacy asserita (D-44).
  Takeaway progr.: 4-13 punti di ideale sul tavolo (pressure-gain
  bottleneck); il costo di scoprirlo = una campagna F2, non un
  programma hardware.

## SLIDE BLUF (in testa, subito dopo il titolo)

Una slide: (1) cosa facciamo (primo framework variazionale per-fase
certificato per ugelli RDE), (2) perche' ora (il campo ha la
conclusione senza barra; pressure-gain bottleneck), (3) cosa abbiamo
(teoria a convergenza + macchina 18x + forchetta onesta), (4) cosa
chiediamo (ASK preview). Poi la mappa del talk.

## SLIDE ASK (candidate di record, carrier addendum-4 (1))

1. CFD-1: collaborazione/procurement per il decider di classe
   (3D-unsteady coupled reference run; ~12M-cell cost class di
   record da P-A; criteri PM22-compliant).
2. Accesso dati motore per la classe del pin: high-speed pressure /
   imaging da hot-fire per T0-flatness + f_cycle (la classe-dati del
   nostro contratto; R20: nessun dataset pubblicato certifica
   single-mode persistente in thermal steady state).
3. Canali paper: P-1 (JPP target) + interesse a co-authorship /
   review sulle campagne di validazione.
   [+ procurement letteratura: top-3 harvest = W-01 Fotia 2016,
   W-02 Goto 2019, W-03 Ma 2023 — la lista WANTED Tier-1 esiste
   a registro.]

## GUARDIE VINCOLANTI SULL'INTERO DECK (trigger sweep Block 0)

- :1450 two-stage claim -> SCHEMA DECLARED on-slide (user decision).
- D-44: forchetta = bracket con provenienza; adequacy MAI asserita.
- P34: ogni engine claim porta lo stage (verificato/validato/
  predizione).
- Novita' query-bounded ("first ... that we could find under the
  amended census protocol", mai assoluta).
- CT-6: numeri dei paper = loro, mai nostre bande.
- best-of-sweep != argmax su ogni claim di letteratura.

## TIME-BOXING 60' (budget indicativo, da adattare allo storyboard)

| # | Sezione | min | cut-priority (1 = si taglia per primo) |
|---|---------|-----|---|
| 0 | Titolo + BLUF | 3 | mai |
| 1 | RDE e detonazioni DA ZERO (fisica, PGC, perche') | 9 | 5 (comprimibile a 5') |
| 2 | L'efflusso RDE reale (atlas: istantaneo vs medio) | 6 | 4 |
| 3 | Come il campo disegna ugelli RDE (4 metodi + genealogia + i loro plot) | 8 | 3 |
| 4 | Il problema: la media senza barra ("approximately applicable") | 4 | mai (cerniera) |
| 5 | Il nostro framework (quoziente/per-fase, T-DISC, T-RED, forchetta) | 9 | mai (core) |
| 6 | Il grafo delle scelte (overview 8 stadi + 2-3 zoom) | 7 | 2 (zoom riducibili) |
| 7 | La macchina (engine, certificati, numeri con stage) | 6 | 4 (comprimibile) |
| 8 | Onesta' quantificata (forchetta a colori, residui, deciders) | 5 | mai (il vantaggio) |
| 9 | Roadmap (M-RED -> CFD-2 -> CFD-1) + ASK | 3 | mai |
|   | TOTALE | 60 | |

CORE-15' (modulo di resilienza, addendum 5): BLUF + 4 + 5 (compresso)
+ 8 (compresso) + 9. CUT-LIST ordinata: prima gli zoom di 6, poi
compressione 1 e 7, poi 2, poi 3 (mai sotto il plot-dichotomy).

## COMPLETEZZA (tripletto, addendum 5)

main deck (60') + GRAFO CAMMINABILE (la mappa come oggetto visivo
navigabile: overview -> zoom per stadio) + BACKUP DECK costruito
DALLA mappa Q&A red-team (assi tecnico/programmatico/TRL/costi).
