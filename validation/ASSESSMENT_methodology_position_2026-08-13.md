# ASSESSMENT DI RECORD — metodologia, idea, importanza del problema, SOTA-ness e collocazione
# (2026-08-13, sessione literature-review; verificato su fonti primarie dove marcato [IO])

SCOPO (mandato utente): assessment rigoroso di (1) metodologia, (2) idea, (3) importanza del
problema, (4) SOTA-ness e appigli teorici — in particolare la legittimità dell'adjoint PER FASI
contro l'adjoint transitorio/periodico — e collocazione SOTA del progetto secondo le sue stesse
regole di rigore (R5: claim query-bounded, falsificatori, classi di rigore).

TIER DI EVIDENZA: **[IO]** = verificato da me su PDF/M0 in questa sessione (pagina/equazione);
**[REP]** = dai 25 report di lettura, la cui accuratezza è stata campionata in profondità 4/4
(KT2015, GP2001, Kraiko-2001 parziale, Harroun-cross) senza un solo errore di lettura trovato —
gli errori dimostrati stavano SOLO negli strati a valle (INDEX/riassunti: C4, C25, R1-descrittore);
**[APERTO]** = non deciso, con l'atto che lo decide nominato.

---
## 1. L'IDEA (il funzionale variazionale ciclo-mediato per ugelli RDE)

VERDETTO: **originale nella forma qualificata, contenimento verificato sulle equazioni.**
- Il corpus classico è CONTENUTO, non somigliante: il nostro T7(b) (∫G_ξ dμ + λ_L g_L = 0, densità
  di Hadamard per fase, M0:1086-1088) ristretto a misura di Dirac riproduce lettera per lettera il
  B^x = y^(ν−1)ρv(u−λ₁)′ di Kraiko-Tillyaeva 2015 (2.9) [IO]. Il collasso T-T3 ha un precedente di
  fenomeno (Efremov-Kraiko 2004: problema periodico che collassa a stazionario, causa NOMINATA =
  portate preassegnate [IO]) che va citato accanto al teorema, col monito: verificare che il nostro
  collasso non sia constraint-indotto (test: cambiare l'insieme dei vincoli).
- La frase "primo problema variazionale di spinta mediata" è MORTA (Efremov-Kraiko Eq. 1.7 [IO]);
  la forma difendibile è quella BLOCCATA: "primo problema di FORMA genuinamente mediato e
  NON-COLLASSANTE (istanza di ciclo)", con la lista caveat estesa (§3.6 verdetto) e i due Tier-1
  russi ancora da leggere (ISABE-2003-117, Bogdanov 2002 — il descrittore "average-thrust" per essi
  è inferenza NON verificata [REP/APERTO R1]).

## 2. IMPORTANZA DEL PROBLEMA

VERDETTO: **massima nel suo campo, e testimoniata dal campo stesso, non da noi.**
- Il corpus RDE 2020-2026 progetta ugelli su stati mediati SENZA teoria: la giustificazione è sempre
  a-posteriori CFD (IJHE 2026 la "prova" via URANS [REP]); NASA pratica varianza parametrica hardware
  e sweep a 2 variabili (Paxson-Miki: 7 progetti OFAT, +13.4 PUNTI di ideale [IO pp.3-5]); nessuno
  pone la domanda "quale funzionale estremizza il flusso medio".
- Il dibattito interno al corpus è APERTO e senza arbitro: Paxson-Miki mostra la media adeguata al
  dimensionamento; Harroun 2021 mostra un valutatore ciclo-mediato CIECO al ranking (c_F=1.25
  identico per due aerospike) [IO p.671]. PRECISIONE OBBLIGATORIA [IO + grep report]: nel paper NON
  esiste alcuna spinta di caso transitorio — né calcolata (il c_F viene SOLO da snapshot steady a
  pressione costante mediati; le CFD a onda servono alla regione di base) né misurata (strumenti =
  CTAP + prese di pressione; Table 3 dà CTAP e portata, MAI spinta); i tre test appaiati
  distinguono i due profili SOLO via pressioni superficiali, con inferenza qualitativa ("may thus
  be the better design"). **CORREZIONE POST-CONTRADDITTORIO (REFUTE_B)**: la clausola "la nostra
  teoria lo prevede" è REFUTED e RITIRATA (doppio abuso di T-T3: fuori ipotesi — valutatore RANS
  viscoso ambient-coupled con separazione = breaker (a); e il collasso parla di fasi, mai di
  geometrie); "mass-weighted" non è stampato in Harroun (convention UNDECLARED). Sopravvive: il tie
  non trasferisce a noi (valutatori INCOMPARABILI, proiezione valida solo sul canale inflow);
  lezione primaria = FRAGILITÀ DELLA CONVENZIONE DI MEDIA, che tocca anche la nostra scelta di μ;
  rischi condivisi 2-D e quasi-steady, più il rischio **INVISCIDO solo nostro** (il loro valutatore
  vede la separazione, il nostro no). **REQUALIFICA 2026-08-13
  (sfida utente, aggiudicata sulle fonti — v. VERIFICATION file, Stage 4 add. 2)**: il valutatore
  cieco è la PROIEZIONE scalare-uniforme (snapshot 2-D a pressione costante lungo un waveform 0-D
  alla Stechmann, media mass-weighted Eq. 4 [IO]) — un membro della nostra classe T3-CONTROL, la cui
  povertà informativa la NOSTRA teoria prevede. La cecità NON trasferisce formalmente al nostro
  valutatore (stati di fase risolti in caratteristica): resta (a) il fatto-opportunità che i
  valutatori standard del campo sono ciechi, (b) la NON-dimostrazione che il nostro discrimini al
  percento, (c) il rischio CONDIVISO della riduzione 2-D-per-fase (attribuzione degli autori
  stessi). R22 (3D-unsteady vs 3D-mediato vs 2D-mediato) decide (b) e (c) ed è NOSTRO.

## 3. LA METODOLOGIA — ha senso? ha appigli teorici?

### 3.1 L'adjoint per fasi vs l'adjoint periodico (la domanda dirimente) — VERDETTO
**POST-CONTRADDITTORIO (REFUTE_A): FONDATO A DUE STADI, entro il pin** [IO + refuter]
- STADIO 1 (esatto, lemma da scrivere): il quoziente di simmetria giustifica l'adjoint steady 3-D
  nel wave-frame; T-T0 IPOTIZZA il pattern sul campo — il lemma di propagazione "BC pura + dominio
  assialsimmetrico ⇒ steady co-rotante" è provabile su classe L4 ma NON è scritto in M0 (duty R4).
- STADIO 2 (approssimazione dichiarata): le marce 2-D per fase scartano l'accoppiamento in θ —
  M0 stesso lo dichiara "the only approximation in the chain" (rung 2). La claim onesta è quindi:
  per-fase = quoziente esatto + rung-2 dichiarato, MAI "l'oggetto corretto" tout court.
- "ZP mal posta" RITIRATO: sul sottoproblema guidato in-pin ZP è ben posta e DOMINATA in costo;
  la degenerazione (moltiplicatore di Floquet banale) vale per la vista autonoma [IO App. A].
- La macchineria generale esiste in due forme: adjoint time-domain con vincolo di periodicità
  (Zahr-Persson: BVP lineare a due punti, esistenza/unicità via monodromia, App. A) e adjoint
  harmonic-balance (Rubino; "all time instances coupled, extremely large-scale" per ZP p.2).
- **Punto decisivo**: per un'onda rotante AUTONOMA il BVP periodico come stampato è degenere — il
  moltiplicatore di Floquet banale (modo di fase lungo l'orbita del gruppo) rende (I − monodromia)
  singolare. La mossa corretta nella nostra classe è la RIDUZIONE PER SIMMETRIA (quoziente per la
  rotazione), che è ESATTAMENTE ciò che fa la formulazione wave-frame/per-fase (T-T0). Quindi:
  l'adjoint per-fase NON è un surrogato povero dell'adjoint periodico "vero" — nella classe pinnata
  È l'oggetto simmetria-ridotto corretto, e l'applicazione ingenua della macchina generale sarebbe
  essa stessa mal posta senza lo stesso quoziente.
- Confini onesti, separati e prezzati: (i) il pin (onda rotante pura, monitor T0-flatness) è
  un'IPOTESI DI MODELLO senza provenienza hardware certificata (R20); (ii) il passo O(St)/riduzione
  dimensionale del problema per-fase è un'approssimazione DISTINTA dal time-coupling, ed è lì che
  vive la minaccia Harroun (R22 decide); (iii) fuori pin la rotta nominata è ZP/Rubino (+LSS/NILSS
  per il caotico) — da citare come alternativa registrata.

### 3.2 La costruzione adjoint in sé — VERDETTO: **struttura corretta e sul lato PROVATO delle
controversie; fedeltà al continuo ANCORA NON TESTATA** [IO su Giles-Pierce 2001, 19/19 pp]
- Il nostro approccio fitted-front (differenziare il fronte fittato con RH imposte) è la
  configurazione in cui GP2001 DIMOSTRA (quasi-1D) continuità dell'aggiunto + BC interna
  v₂(x_s)=−1/(dh/dx) + gradiente nullo all'urto; le due letture rivali (Iollo v=0; Cliff salto) sono
  rigettate nel paper stesso [IO]. In 2-D il risultato è "preliminary analysis + numerical evidence"
  (p.343): ogni enunciato F4b di M0 deve portare QUESTO grado, mai "provato".
- O3.1 (identità del trasposto, 2.7e-10) certifica AUTO-consistenza della coppia discreta, non
  fedeltà al continuo (D-08). I primi oracoli di fedeltà indipendenti sono aggiudicati e non ancora
  implementati: A1 (GP2001 quasi-1D, γ=const, J=∫p dx, costanti da ri-derivare perché il paper
  pubblica PLOT [IO]), A3 (forma chiusa KT2015, valida solo all'ottimo nel triangolo [IO]), A2
  (complex-step, chiude il modo comune). FINCHÉ non girano, "il nostro adjoint è fedele" resta
  un'ipotesi con falsificatori nominati — questo è lo stato onesto.
- La singolarità logaritmica dell'aggiunto alla gola sonica (GP2001 §6.1, ereditata dal rung shocked
  — Fig. 4 asintoto a x≈0, NON all'urto [IO]) giustifica in forma DERIVATA il locus escluso delle
  nostre barre DWR presso la IVL di Sauer (C33); nel nostro dominio la singolarità è al BORDO, non
  interna — strutturalmente più mite del caso GP.
- Correzione matematica accettata alla nostra teoria: T7(c) come UGUAGLIANZA (M0:1090 [IO] al
  momento della lettura; ANCHOR AGGIORNATO alla chiusura S-CERT 2026-08-13: l'innesto C31 ha
  sostituito l'uguaglianza con la forma a cono di record — il contenuto T7(c) vive ora in M0
  ~1154-1198, [T-T7CN]; la citazione storica resta fedele allo stato pre-C31) è la
  condizione del solo estremo libero; con vincoli attivi la forma è a cono D ∈ N_K(s_E*) — KT2015
  (2.10)/(2.14) mostra le disuguaglianze-con-slack nella scuola classica [IO]; falsificatore a SEGNI
  (C32). DA RATIFICARE.

### 3.3 MoC e linea classica — VERDETTO: **contenimento pulito, un buco bloccante dichiarato.**
- Kraiko 2001 Eq. (1)-(2) [IO]: la coppia corner/trasversalità in forma ± combacia con la disciplina
  CSTR_PA/PB di GENO; la storia CCM (Nikolskii→Guderley-Hantsch→Shmyglevskii/Sternin→Rao, priorità
  di stampa a Rao fine-1958 secondo il resoconto di Kraiko 2001, parte in causa) è ora citabile con
  il rider corretto [IO].
- BUCO R16 [IO + REFUTE_D: TIENE nel nucleo, RIQUALIFICATO]: l'ottimo discontinuo di Shmyglevskii
  1962 porta slip line `ct` strutturale; il nostro tier la rigetta per costruzione — rigetto anzi
  SOVRADETERMINATO (anche (F3) noninteraction; il rejector X-U3BD aveva GIÀ rilevato singolare il
  limite caratteristico). Il regime corto È dentro l'inviluppo RDE, ma il gap **vincola al GATE
  F4b, non blocca la catena S-ORDINE→S-CERT→F2**; membership in S1 asserita non certificata
  (+ collisione nomi S_1-tier/S1-classe da sanare); test di accettazione da riqualificare sul
  sostituto su disco (secondo schema Shmyglevskii CMMP, M0:1572-76, che GIÀ nominava l'istanza —
  chiosa di novità ridimensionata). C31 (forma a cono): NECESSARIA nella sostanza, forma MINIMALE
  `D ∈ N_K` con K per istanza; portata = uguaglianza FUORI dal cono; cecità duale confermata SUL
  CODICE su CINQUE carrier (REFUTE_C, righe citate); emenda S2 (f3*≥0 ⇒ rejector sull'identità).

## 4. LA METODOLOGIA È SOTA? — collocazione

**SÌ nella forma seguente, difendibile davanti a referee ostile:**
1. **Ponte P2/G14** (query-bounded 2026-08-13, test bibliografico KT2015 eseguito [IO]: 8 titoli
   russi, zero ASO; nona bibliografia indipendente a zero incroci GP2001 [IO]: 26 ref, zero scuola
   ugelli E zero Lions/Pironneau): nessuna identificazione pubblicata nelle tre gambe (linguaggio
   ASO; aggiunti discreti/reverse-AD; ottimizzatore certificato). Si CONCEDE l'equivalenza generica
   e la catena interna classica; la glossa "residual = adjoint gradient" si CANCELLA (istanziata da
   KT2015 (2.9) [IO]). Valore = articolazione + operazionalizzazione.
2. **Nicchia** "formulazione variazionale MoC + ottimizzatore moderno": verificata non occupata
   (Fernandes = MoC come simulatore in loop black-box, zero condizioni di ottimalità [REP+census]).
3. **Il regime di certificazione** (oracoli che rigettano, tolleranze derivate, falsificatori,
   Verdict) NON ha equivalente in nessuno dei 25: né la scuola classica (Fig. 5 di HTH = confronto
   grafico) né il corpus RDE (validazioni a bias +17% senza convergenza di griglia, R18) né la
   scuola adjoint (che ha dual-consistency ma non il resto). È il differenziatore più robusto.
4. **Cosa NON possiamo dire**: che il contenuto matematico del ponte sia nostro; che la struttura
   disuguaglianze-all'inammissibilità sia nostra (Shmyglevskii 1962, C30 [IO]); che la media basti
   per il ranking al percento (APERTO, R22/R26); che l'adjoint sia fedele al continuo (APERTO fino
   ad A1/A2/A3); che il pin d'onda abbia provenienza hardware (R20); **che siamo "sopra"
   Zahr-Persson/Rubino sull'asse MACCHINERIA adjoint instazionaria** — su quell'asse loro sono
   production-grade (fully discrete, duality-preserving, gradiente verificato, viscoso/turbolento,
   SU2 open source) e noi deliberatamente NON la costruiamo perché in-pin non serve (quoziente);
   fuori pin loro SONO la rotta nominata. La superiorità rivendicabile è di FORMULAZIONE per la
   classe RDE (teoria del problema mediato + condizioni di ottimalità + certificati), non di
   solver. Assi distinti, mai confonderli in una presentazione.

**GENEALOGIA DI POSIZIONAMENTO (la "scala di Stechmann", registrata 2026-08-13)** — doppia
discendenza citabile, entrambe [IO]: *lato valutazione* (scuola NASA/Purdue): rung 0 = Stechmann
Eq. (4), media mass-weighted di prestazioni 0-D per-istante su waveform; rung 1 = Harroun 2021,
stessi istanti ma campi 2-D steady a pressione costante; rung 2 = il nostro J = ∫F[Σ;s(ξ)]dμ con
stati di fase = TRACCE D'INTERFACCIA NON UNIFORMI risolte in caratteristica (da profili a campi);
rung 3 = il layer VARIAZIONALE su rung 2 (design come incognita + T7 + certificati) — che NON
discende da Stechmann (lì nessuna variazione di design) ma dalla linea classica: Rao →
Kraiko-Osipov 1970 (antenato variazionale mediato, citazione obbligatoria di record) →
Efremov-Kraiko 2004 (mediato collassante). La scala rende il lavoro leggibile a ENTRAMBE le
scuole; caveat da portare sempre: l'assunzione 3 di Stechmann (uscita chocked in ogni istante) e
lo spike idealmente adattato sono le idealizzazioni che il nostro L4/T-T4 sostituisce con oggetti
gated.

## 5. RESIDUI CHE GATE-ANO LA COLLOCAZIONE FINALE (owner nominati)
R1 ISABE-2003 full text (PB-2, P0) · R2 tesi Harroun 2019 (P0) · R22 esperimento disentanglement
(P0, il singolo atto di maggior valore) · R16 certificato slip-line (F4b, bloccante per "ottimo
classico certificabile") · R28 Shmyglevskii 1962 (gate della formulazione C30) · A1/A2/A3 oracoli di
fedeltà (F2/S-CERT) · ratifiche utente pendenti: D-01 (glossa), C31 (forma a cono), C30
(attribuzione).

## 6. COPERTURA DI QUESTO ASSESSMENT
Personalmente verificati [IO]: HTH-1971, Hoffman-1967(parz.), Rao-Beck, Hoffman-1987,
Efremov-Kraiko-2004, Paxson-Miki(metodo), KT2015(13/18pp), GP2001(19/19), Zahr-Persson(pp.1-8 +
App. A), Kraiko-2001(pp.1-2), Harroun-2021(p.671 + cross-check advisory 08-11 + grep integrale),
Stechmann(§§I-II), Fernandes(pp.868-872: nicchia CONFERMATA), Rubino(pp.221-225: HB 2K+1
accoppiate), Ancourt(refs 45/45: zero scuola variazionale ugelli), M0 righe 246-247/442-445/
660-664/1071-1130/1572-76/1699-1704 + carrier in codice (o33_bench, a1_toc, margin_governor via
REFUTE_C). **Più contraddittorio consumato: 4 refuter (REFUTE_A/B/C/D) sui 4 punti teoricamente
ricchi — 1 clausola REFUTED e ritirata, 2 riqualificate, 1 sovradimensionamento ridotto, 5 carrier
duale-ciechi confermati sul codice.** Al tier [REP] residuo (non portante; regola A4 standing):
GP2000, Schotthöfer, Kaemming-Paxson, Wintenberger, Wolanski, JANC, Sun, Liu, Ornano, Kraiko-2016,
set NASA.
