# REFUTE_D — Attacco avversariale a R16 (slip line di Shmyglevskii 1962)

Refuter: agente avversariale, default = la claim di blocco è sbagliata finché non regge.
Data: 2026-08-13. Tesi sotto attacco: R16 di
`validation/ADVISORY_litreview_confrontation_2026-08-13.md` (riga 1144, letta per intero).

Fonti primarie verificate su disco in questa sessione:
- `literature_review/kraiko_2001_optimal_plug_nozzles_thrust_at_start.pdf`, pp. 1347-1352 (lette).
- `docs/rde_nozzle_D25U_U3U4.md` righe 50-179; `docs/rde_nozzle_conditionals.md` righe 77-113;
  `docs/rde_nozzle_problem_book.md` righe 373-395; `docs/rde_nozzle_MASTER.md` righe 1558-1645;
  `docs/rde_nozzle_development_plan.md` righe 305-337.

---

## Linea (1) — VERIFICA TESTUALE delle tre clausole: REGGONO (con una precisazione di rango)

**Clausola A** — `docs/rde_nozzle_D25U_U3U4.md:61-64`, verbatim:

> "(F1) STRENGTH MARGIN: every front is a Lax shock of an acoustic
>       family with normal-Mach margin M_n - 1 >= delta on its whole
>       arc (equivalently: all five Lax slope inequalities of §2.1 hold
>       with margins derived from delta);"

Esiste e dice esattamente quello che R16 afferma. Nota di contesto onesta: le righe 59-60 la
qualificano come "READING OF RECORD (declared here, priced in §5)" — è una lettura dichiarata
delle clausole del ledger, non testo del ledger stesso; ma è la lettura DI RECORD, quindi il
tier certificato la porta davvero.

**Clausola B** — `docs/rde_nozzle_D25U_U3U4.md:164-165` (U3-L1(iv)), verbatim:

> " (iv)  the entropy jump satisfies [S] >= s_j(delta, C_0) > 0
>        (under the genuine-nonlinearity clause c4)"

Esiste. Precisazione di RANGO: non è una clausola indipendente ma una CONSEGUENZA (lemma su
K_delta, che già presuppone i margini di Lax) sotto la clausola c4 di genuina nonlinearità.
Il rigetto primario del contatto sta in (F1)+c4; il floor entropico è derivato. Questo non
cambia la sostanza (un contatto ha m = 0 e c4 non lo copre), ma "tre clausole" è
contabilmente "una clausola definitoria + un lemma derivato + un fatto di degenerazione".

**Clausola C** — `docs/rde_nozzle_conditionals.md:92-94`, verbatim:

> "the linearized RH is nonsingular STRICTLY inside
> the Lax condition and degenerates EXACTLY at characteristic fronts
> (= the Prop. A2 kernel law [T-A2])"

Esiste; e un fronte di contatto in flusso supersonico stazionario È caratteristico (giace su
una streamline = caratteristica della famiglia linearmente degenere). Rinforzo macchina che
R16 non cita: `rde_nozzle_D25U_U3U4.md:123-125` — "[X-U3BD P2/P3/P3b, rejectors R1/R2 active:
the characteristic-front limit IS detected singular]". Il limite caratteristico è rigettato
da un rejector ESEGUITO, non solo da testo.

**QUARTA clausola non citata da R16 che rafforza il blocco**: `rde_nozzle_D25U_U3U4.md:71-73`,
"(F3) NONINTERACTION: fronts are pairwise disjoint … front-front interactions and reflections
are OUTSIDE this class". Nella Fig. 1b di Kraiko 2001 QUATTRO fronti (fan ach, fan lcm, urto
cn, slip ct) concorrono nel punto c: la topologia del benchmark viola anche (F3),
indipendentemente dalla natura del contatto. Il rigetto è più sovradeterminato di quanto R16
dichiari.

**Verdetto (1): TIENE.** Le clausole esistono, dicono quello che R16 afferma, e il rigetto è
anzi più forte (4 clausole, una machine-verified).

---

## Linea (2) — "dentro S1, fuori dal tier": TIENE NEL CONTENUTO, con COLLISIONE DI NOMI da dichiarare

`docs/rde_nozzle_problem_book.md:373-375`, verbatim:

> "(S1) MOC-REGULAR piecewise-smooth: steady supersonic per-state flows,
>      piecewise C¹, finitely many transversal shocks/contacts, no wall
>      shock formation."

S1 include ESPLICITAMENTE i contatti ("shocks/contacts") ⇒ il tentativo di far cadere il
claim su "S1 esclude i contatti" FALLISCE. "Dentro la classe di soluzione" è testualmente
fondato.

Due riqualificazioni dovute:

(a) **Collisione di namespace.** `rde_nozzle_MASTER.md:1605-1608` definisce il tier ladder con
"S_0 (shock-free …) SUBSET S_1 (finitely many FITTED fronts under RH + entropy + Lax +
Lopatinskii certificates …)": nel namespace di M0, "S_1" è il TIER (che i contatti li
ESCLUDE), mentre nel problem_book "(S1)" è la CLASSE DI SOLUZIONE (che li include). La
formula di R16 "S1 \ A₁(μ₀)" è coerente SOLO con S1 = classe del problem_book e
A₁(μ₀) = A_t(μ₀) di M0:1600 con t = 1. Va scritta con la lettura dichiarata, altrimenti un
lettore di M0 legge "S_1 \ A₁" come vuoto o contraddittorio.

(b) **Membership asserita, non certificata.** Il problem_book (righe 379-381) dichiara S1
"an a-posteriori certificate class … checkable along any computed solution". Noi il campo di
Shmyglevskii 1962 NON lo abbiamo computato: che l'ottimo di Fig. 1b soddisfi TUTTE le clausole
S1 (transversalità, "no wall shock formation", C¹ a tratti) è plausibile per struttura ma non
verificato in istanza. Formulazione corretta: "S1-compatibile per struttura dichiarata, membership
a-posteriori non eseguita".

**Verdetto (2): TIENE riqualificato** — la conseguenza resta "buco di certificazione, non
esclusione di scopo", ma con lettura di namespace dichiarata e membership al condizionale.

---

## Linea (3) — RILEVANZA OPERATIVA: il regime È negli inviluppi del programma; l'operatività è AL GATE F4b

Evidenza che il regime corto/oltre-confine è toccato:
- Kraiko 2001 p.1348 col.2 (verbatim): "In 1961 Sternin20 found out that the continuous
  solutions can be designed not in any choice of point c of the initial rarefaction wave
  fan. After that, in 1962 Shmyglevskii obtained the necessary conditions of maximal thrust
  in the form of inequalities. For these cases he designed the 'discontinuous' optimal
  solutions21 (Fig. 1b, where ach and lcm are the compression and rarefaction fans, cn is
  the shock wave, and ct is the slip line, respectively)." — l'ottimo discontinuo vive
  esattamente oltre il confine di Sternin.
- `rde_nozzle_MASTER.md:1617-1619`: "the S20 instance optimum is boundary-active" (ipotesi
  measured-supported, crawl + 8/8 genuine) — il NOSTRO ottimo misurato siede SUL confine.
- I plug corti/troncati sono il caso d'uso di bandiera RDE (Kraiko 2001 Conclusions: ad
  L≈1.35 il plug ha base, regime "Aerospike"/RLV; Paxson-Miki = plug troncato; la nostra
  ancora PB-2). Il regime NON è fuori inviluppo.
- `development_plan.md:316-322` (REQ-NONSTALL, clausola tier-invariante vincolante) +
  `:330-337` (TRANSITION DUTY S0→S1): l'apertura del tier 1 è la rotta dichiarata del
  programma, col multiplicatore μ misurato come criterio quantitativo (M0:1613-1615).

MA: il tier 1 oggi NON è costruito ("the G12/F2 line", F4b aperto). "Non possiamo emettere un
Verdict sull'ottimo pubblicato" è vero oggi per QUALSIASI oggetto tier-1, non solo per quello
col contatto. Il contenuto incrementale vero di R16 è PROSPETTICO: il tier 1 COME SPECIFICATO
(Lax acustico + floor entropico + Lopatinskii) escluderà il benchmark classico ANCHE quando
sarà costruito — serve la terza classe (A5/contatti), che R16/D-22 correttamente apre.

**Verdetto (3): TIENE come gap operativo AL GATE F4b** (owner corretto), NON come blocco della
catena ratificata S-ORDINE → S-CERT → F2. Declassamento rifiutato ("buco solo teorico" è
falso: il regime è in inviluppo e la rotta tier-1 è dichiarata); scoping obbligatorio sì.

---

## Linea (4) — "Struttura inapplicabile, non tolleranza": TIENE, ed esce RAFFORZATA

Il contatto NON è nel chiuso utile della famiglia di Lax. Prova precisa, in tre pezzi:

1. **[v_t] ≡ 0 su ogni urto.** Attraverso qualunque discontinuità RH con flusso di massa
   m ≠ 0, il bilancio tangenziale dà m·[v_t] = 0 ⇒ [v_t] = 0 identicamente su TUTTA la
   famiglia acustica, a qualunque intensità. La slip line ct porta [v_t] ≠ 0 finito (a valle
   del punto di fuoco c: pressioni e direzioni uguali, velocità/entropie diverse). Nessuna
   successione di urti di Lax può convergere a un salto tangenziale finito: il limite a
   intensità → 0 (cioè [S] → 0) è la LINEA DI MACH banale a salto nullo, mai un contatto.
2. **Le due branche RH si toccano solo nel punto banale.** La varietà RH si spezza in
   {m ≠ 0, [v_t] = 0} (acustica) e {m = 0, [p] = 0, [v_n] = 0, [v_t] e [S] liberi}
   (contatto); l'intersezione è il salto nullo. Una "certificazione per continuazione"
   lungo il ramo acustico certifica quindi SOLO il fronte banale — non è una via.
3. **Origine a punto triplo.** Nella Fig. 1b il ct nasce dal fuoco c della compressione con
   l'urto cn — un'INTERAZIONE di fronti, che (F3) esclude comunque dalla classe.

E il fatto è già rilevato a macchina: i rejector R1/R2 di [X-U3BD] dichiarano singolare il
limite di fronte caratteristico. La degenerazione lineare del contatto non è un margine
stretto: è un'ALTRA famiglia caratteristica, con un altro problema (trasporto lungo la
caratteristica + stabilità di vortex sheet alla Miles, non solve RH bordato). "Tolleranza da
allargare" è quindi la descrizione SBAGLIATA e R16 la rigetta a ragione.

**Verdetto (4): TIENE, rafforzato** dalla prova [v_t] ≡ 0 e dalla clausola (F3).

---

## Linea (5) — TEST DI ACCETTAZIONE: MAL POSTO COME SCRITTO (procurement-gated non dichiarato); esiste un sostituto su disco

Il test richiede il campo dell'ottimo 1962. Stato delle fonti:
- Kraiko 2001 dà SOLO lo schema (Fig. 1b), le relazioni (1)-(3) su cb e la frase "two more
  conditions of transversality appear in point c" (p.1348) — condizioni, NON un algoritmo di
  costruzione; il campo non è ricostruibile da qui senza un lavoro di ri-derivazione che
  sarebbe esso stesso ricerca non citabile.
- Shmyglevskii PMM 26(1):110-125 (1962), ref. [21] del paper, è in russo e NON su disco —
  esattamente la riga R28 dello stesso advisory ("non letto … procurement"). R16 dichiara il
  procurement per Miles/Coulombel-Secchi ma NON per la fonte del proprio benchmark:
  incoerenza interna.
- SOSTITUTO SU DISCO: `rde_nozzle_MASTER.md:1566-1576` registra Shmyglevskii = 
  `literature/0041-5553(80)90091-9.pdf` (USSR CMMP 20(5):113-127, letto due volte,
  page-verified) col "SECOND SCHEME (discontinuous SHOCKLESS solutions from variational
  corner conditions, his Eq. (7), completeness map Fig. 4 …); its CONTACT front needs a
  certificate class of its own, F4b open item". Un benchmark a fronte di contatto
  RICOSTRUIBILE da fonte su disco esiste già.

Corollario sulla NOVITÀ: la chiosa di R16 "[il buco contatti NON è più astratto, ha
un'ISTANZA CLASSICA NOMINATA]" sopravvaluta — M0:1575-1576 nominava GIÀ (S24, 2026-08-12)
un'istanza classica a fronte di contatto con l'item F4b aperto. Il delta vero di R16 è:
la seconda istanza (1962, slip line con urto), il test di accettazione e lo screen di Miles.

**Verdetto (5): VA RIQUALIFICATO.** Il test è ben concepito ma inoperabile come scritto:
o si dichiara la dipendenza dal procurement di PMM 26(1) 1962 (allineandolo a R28), o si
ri-punta il benchmark primario sul secondo schema CMMP già su disco (con l'istanza 1962 come
estensione post-procurement).

---

## VERDETTO COMPLESSIVO: R16 TIENE NEL NUCLEO — VA RIQUALIFICATO IN QUATTRO PUNTI

Il nucleo regge a ogni attacco: le clausole citate esistono e sono citate fedelmente (linea 1,
anzi sovradeterminate da (F3) e dal rejector X-U3BD); S1 include i contatti per testo, quindi
"dentro la classe, fuori dal tier" è la lettura giusta (linea 2); il regime è negli inviluppi
del programma (linea 3); "struttura, non tolleranza" è matematicamente esatto ([v_t] ≡ 0 su
ogni urto ⇒ nessuna continuazione; linea 4).

Riqualificazioni obbligatorie:
1. **Namespace**: dichiarare S1 = classe problem_book ≠ S_1 = tier M0; scrivere
   "problem_book-S1 \ A₁(μ₀)" o equivalente; membership del campo 1962 = "compatibile per
   struttura, a-posteriori non eseguita".
2. **Contabilità delle clausole**: (F1)+c4 definitoria, floor entropico = lemma derivato,
   Lopatinskii = degenerazione machine-verified; AGGIUNGERE (F3) noninteraction (il punto c
   è un'interazione a quattro fronti).
3. **Scoping dell'operatività**: gap vincolante AL GATE F4b (e alla spec della terza classe
   A5), non blocco della catena corrente; oggi NESSUN oggetto tier-1 è certificabile, il
   contenuto di R16 è che il tier-1 specificato non lo sarà MAI per questo benchmark.
4. **Test di accettazione**: dichiarare il procurement di Shmyglevskii PMM 26(1) 1962
   (coerenza con R28) o ri-puntare al secondo schema CMMP su disco; ridimensionare la chiosa
   di novità (l'istanza contatti era già nominata in M0:1575).
