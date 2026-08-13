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
  dimensionamento; Harroun 2021 la mostra CIECA al ranking (c_F=1.25 identico per due aerospike che
  l'esperimento separa) [REP, cross-checked con ADVISORY_rde_choking]. Il nostro programma è
  l'arbitro strutturale di quel dibattito; R22 (esperimento di disentanglement 3D/3D-mediato/2D) è
  l'atto che lo decide ed è NOSTRO.

## 3. LA METODOLOGIA — ha senso? ha appigli teorici?

### 3.1 L'adjoint per fasi vs l'adjoint periodico (la domanda dirimente) — VERDETTO: **LEGITTIMO,
con appiglio teorico FORTE, entro il pin dichiarato** [IO su Zahr-Persson pp.1-8]
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
- Correzione matematica accettata alla nostra teoria: T7(c) come UGUAGLIANZA (M0:1090 [IO]) è la
  condizione del solo estremo libero; con vincoli attivi la forma è a cono D ∈ N_K(s_E*) — KT2015
  (2.10)/(2.14) mostra le disuguaglianze-con-slack nella scuola classica [IO]; falsificatore a SEGNI
  (C32). DA RATIFICARE.

### 3.3 MoC e linea classica — VERDETTO: **contenimento pulito, un buco bloccante dichiarato.**
- Kraiko 2001 Eq. (1)-(2) [IO]: la coppia corner/trasversalità in forma ± combacia con la disciplina
  CSTR_PA/PB di GENO; la storia CCM (Nikolskii→Guderley-Hantsch→Shmyglevskii/Sternin→Rao, priorità
  di stampa a Rao fine-1958 secondo il resoconto di Kraiko 2001, parte in causa) è ora citabile con
  il rider corretto [IO].
- BUCO BLOCCANTE R16 [IO su Kraiko 2001 p.1348 + clausole nostre]: l'ottimo discontinuo di
  Shmyglevskii 1962 porta slip line `ct` come elemento strutturale; il nostro tier certificato la
  rigetta per costruzione (fronte caratteristico, Lopatinskii degenere) ⇒ lo stack non può emettere
  un Verdict sull'ottimo che il corpus ha pubblicato. Test di accettazione F4b nominato.

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
   ad A1/A2/A3); che il pin d'onda abbia provenienza hardware (R20).

## 5. RESIDUI CHE GATE-ANO LA COLLOCAZIONE FINALE (owner nominati)
R1 ISABE-2003 full text (PB-2, P0) · R2 tesi Harroun 2019 (P0) · R22 esperimento disentanglement
(P0, il singolo atto di maggior valore) · R16 certificato slip-line (F4b, bloccante per "ottimo
classico certificabile") · R28 Shmyglevskii 1962 (gate della formulazione C30) · A1/A2/A3 oracoli di
fedeltà (F2/S-CERT) · ratifiche utente pendenti: D-01 (glossa), C31 (forma a cono), C30
(attribuzione).

## 6. COPERTURA DI QUESTO ASSESSMENT
Personalmente verificati [IO]: HTH-1971, Hoffman-1967(parz.), Rao-Beck, Hoffman-1987,
Efremov-Kraiko-2004, Paxson-Miki(metodo), KT2015(13/18pp), GP2001(19/19), Zahr-Persson(pp.1-8),
Kraiko-2001(pp.1-2), Harroun(via advisory 08-11 + cross-check), M0 righe 1071-1130 + grep glossa.
Al tier [REP] (letture campionate 4/4 accurate, correzioni a valle già assorbite): Ancourt, GP2000,
Rubino(dettaglio), Schotthöfer, Kaemming-Paxson, Wintenberger, Wolanski, JANC, Sun, Fernandes, Liu,
Ornano, Kraiko-2016, set NASA. La verifica personale di questi continua in coda dichiarata
(VERIFICATION_FABLE_2026-08-13.md); nessuno di essi porta da solo un claim di record senza
riverifica alla citazione (regola A4 della sweep, standing).
