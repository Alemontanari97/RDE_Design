# LINEAGE SWEEP MATRIX — part 1 (slot L1, onda W-B.0, S-PRES session 2)

**NOTA DI DRIFT [C6-REPAIR 2026-08-23]**: le ancore "CHn:righe" di
questo file sono state stampate PRIMA della riscrittura dei CH1-CH10 da
parte dell'onda W-B.1 (mtime 08:33-08:44) e NON sono più affidabili
come numeri di riga (probe misurati: REFUTE_LINEAGE.md F-6). Il join
downstream usa LL-id e i § dei CH, MAI numeri di riga CH. Le ancore
non-CH (registry/findings/M0/LM/report/PDF) sono verificate sane da C6.

Data: 2026-08-23. Ordine utente C-1ter di record (finding
`methodology:lineage-recognition-gap`, `docs/findings_registry.yaml:2541`
[C6-REPAIR: era :2550]):
la ricerca di lineage era tematica/citazionale, mai per isomorfismo
strutturale — questo file esegue la META' 1 del prodotto cartesiano
{15 componenti strutturali del metodo} x {41 id del mezzo corpus L1}.

**Stadio di confronto** (artifact-connectedness): le 15 componenti del
checkpoint C-1ter confrontate con i materiali di lettura DI RECORD, mai
con il ricordo. Comandi misurati in questa finestra (SR-12):
- righe registry: `Read docs/literature_registry.yaml` (tutte le 41 righe
  del mezzo corpus stanno in :102-474 [C6-REPAIR: era ":102-490", che
  includeva :476/:484 = viviano/valeriani, colonne L2]);
- scan CH: `grep -ril <id> validation/spres_raws_2026-08-22/reconstruction/CH*.md`
  + `grep -noiE "<cognomi>" CH1..CH8` (41 id + 20 cognomi);
- findings: `grep -n -iE "<id/cognomi>" docs/findings_registry.yaml`
  (righe consumate: :1434, :1956, :2002, :2024, :2035, :2059, :2070,
  :2541 [C6-REPAIR: ":2540/:2550" erano imprecise — A31/A33/A35 vive a
  :1956-1967, il finding radice inizia a :2541]);
- fonti di sezione: CH5 integrale; `docs/rde_nozzle_pipeline_decision_map.md`
  integrale (GV-1); `validation/ADVISORY_rde_choking_2026-08-11.md#3-bis`;
  estratti CH1:350-360, CH2:205-215/235-245/345-418, CH3:211-232,
  CH6:203-210, CH7:232-238/458-464.
- DEEP-CHECK su PDF: **solo Harroun 2021** (duty (a)), pagine 670-672 del
  paper (pp. 11-13 del file
  `literature_review/harroun_2021_computational_experimental_rdre_nozzle_performance.pdf`).
  Le altre celle candidate a isomorfismo (KO-1970 (3.2), Rao 1958 Eq. [14],
  Stechmann Eq. (4), KP18 Eqq. (1)-(13)) portano ancore page-verified di
  record (M0:2908-2926; LM:381-386; `data/st_opt_validation.md`; remark EAP
  M0 verificata clause-by-clause) — nessuna ri-lettura necessaria
  (context-discipline).
- Colonne [REP]-bounded: **NESSUNA** — tutti i 41 paper hanno path su disco
  nel registry (root A/B/C/D verificate dalla riconciliazione di record,
  registry header :49-68).

**Arco di consumo**: merge dell'orchestratore con la part 2 (L2) →
LINEAGE_LEDGER → §3-bis ANTENATI DIRETTI dei writer W-B.1 + storyboard
C6/C7-bis-pre. Il refuter C6 attacca: le celle VUOTE (assenza dichiarata
dopo check, falsificabile), le celle PIENE (isomorfismo sovra-letto), E la
lista GV-1 (proposte di componenti nuove).

**Le 15 componenti (asse-righe, verbatim C-1ter)**: (1) per-phase family;
(2) averaged functional; (3) averaged wall conditions; (4) weighted
transversality; (5) imposed-BC contract; (6) periodic data class;
(7) quotient/wave-frame; (8) mu measure; (9) decomposition identity;
(10) per-phase marching; (11) discrete adjoint; (12) certificates;
(13) sector tournaments; (14) truncation/p_b; (15) monitors.

**Regola di cella**: <=3 righe, "procedura isomorfa/antenata? come la
chiamano? cosa le manca vs noi". Componenti non elencate in un blocco =
"checked: none" (dichiarato dopo scan registry+record; per le componenti
3/6/7 l'assenza quasi-totale e' essa stessa il verdetto C2-NOT-FOUND(q) di
record, LM:354-357).

**Conteggio**: celle totali 41x15 = 615; PIENE = 81; "checked: none" =
534 [C6-REPAIR: era 80/535; +1 = harroun_2021 (9) C6-FILL].

---

## BLOCCHI PER PAPER

### kraiko_osipov_1970 (registry :102-109)
- (1) per-phase family: DEGENERE — collasso alla famiglia classica sotto
  similarita' d'ingresso (Sec.4/5, antenati T-T3/T4, F-KO5); manca la
  famiglia indicizzata dalla fase sotto onda periodica.
- (2) averaged functional: ISOMORFO sull'istanza TRAIETTORIA — funzionale
  integrato nel tempo di volo; il NOSTRO record lo classifica
  "trajectory-averaged" [C6-REPAIR: etichetta del registry/M0, non
  lessico del paper]; manca la misura di ciclo, T0-esattezza.
- (3) averaged wall conditions: ANTENATO DIRETTO E UNICO del corpus — loro
  (3.2) = condizione a parete PESATA integrata nel tempo (M0:2908-2926,
  page-verified S13); manca: media su fase (non su traiettoria), quoziente.
- (4) weighted transversality: ANTENATO — peso endogeno W(t) = adjoint di
  traiettoria; condizioni endpoint time-averaged per ugello length-capped
  (CH1:355-360); manca (**') su misura di ciclo + identificazione adjoint.
- (11) discrete adjoint: il peso W(t) E' un campo adjoint di traiettoria
  (continuo, ante litteram); manca ogni forma discreta/AD.
- checked: none — 5, 6, 7, 8 (assenza di misura di ciclo DICHIARATA dal
  record, CH2:210-215), 9, 10, 12, 13, 14, 15.

### shmyglevskii_1980 (registry :111-118)
- (4) weighted transversality: antenato single-phase — corner conditions
  (7) del secondo schema; manca peso/media.
- (12) certificates: rejection condition (6) = candidata identita' di
  confine (G)/Lambda-form (QUESTION, owner F4b); Fig. 4 completeness map =
  claim classico di ottimalita' del regime discontinuo (obbligo O3);
  manca certificato a posteriori eseguibile.
- (13) sector tournaments: analogia CAUTA — tassonomia Route A/B + mappa di
  completezza dei regimi = enumerazione di regimi; manca il torneo tra
  settori topologici con verdetti per-settore.
- checked: none — 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 14, 15.

### giles_ulbrich_2010_part1 (registry :120-127)
- (11) discrete adjoint: convergenza linearizzato/adjoint con shock,
  riparazione eps=h^alpha, BC interna dell'adjoint allo shock (p.886);
  contrasto capturing-vs-fitting = l'aggiudicazione che C49 consuma;
  manca il setting mediato/per-phase.
- checked: none — 1-10, 12-15.

### giles_ulbrich_2010_part2 (registry :129-135)
- (11) discrete adjoint: "the trap is a theorem" — l'adjoint discreto a
  stencil fisso converge a valore SBAGLIATO attraverso gli shock (pp. 907,
  910); e' il teorema negativo a cui rispondono C49 fitted-front + la
  scelta discrete-AD su fronti fittati; manca (ovviamente) la cura.
- checked: none — 1-10, 12-15.

### lozano_ponsin_2025 (registry :137-143)
- (11) discrete adjoint: adjoint analitici 2-D Euler a struttura
  caratteristica; argomento det-transpose = nostra Prop. A1; sponda moderna
  del ponte G14 (zero cite di Rao/Guderley/Kraiko); manca il ponte.
- (12) certificates: compatibilita' adjoint Eqq. (30)/(31) = righe bench
  O3.3 (F-O33BENCH) — oracoli certificate-class; manca classe/floor/cert
  formale nostro.
- checked: none — 1-10, 13-15.

### gonzalez_viana_2025 (registry :145-152)
- (2) averaged functional: obiettivo di IMPULSO single-cycle ottimizzato
  (PDE H2-air, CFD unsteady); "classical nozzle optimization criterion is
  no longer valid" (p.14) + length bound ATTIVO; manca: riduzione per-phase,
  condizioni di ottimalita' (design per sweep CFD).
- checked: none — 1, 3-15.

### sternin_1961 (registry :154-160)
- (12) certificates: antenato classico del confine di certificabilita' A_t
  — dy/dalpha=0 sulla pencil characteristic, "shockless solutions
  impossible left of C0", confine gamma=const Eq. (4); identificazione con
  Lambda-form/Rao-Beck Eq.(4) APERTA (residuo R4, findings :2059).
- checked: none — 1-11, 13-15.

### lozano_2018 (registry :162-168)
- (11) discrete adjoint: tassonomia objective-dependent delle singolarita'
  adjoint a shock/sonico (log singularity al throat sonico); manca setting
  mediato; caso oblique-shock dichiarato OPEN nel 2018.
- checked: none — 1-10, 12-15.

### lozano_2019 (registry :170-176)
- (11) discrete adjoint: locus di mesh-divergence degli adjoint inviscidi
  CORRETTO di record (wall/trailing-edge, non lo shock) — igiene Lemma B;
  manca setting mediato.
- checked: none — 1-10, 12-15.

### morris_2005 (registry :178-184)
- (2) averaged functional: metrica di performance single-pulse su CD
  ottimizzato (+53-57%/+20-21%/+10% per banda di pressure ratio) — obiettivo
  integrato sul pulse, trade discreto; manca famiglia per-phase, ottimalita'.
  NOTA di record: NON MoC — quasi-1D unsteady FV (correzione di metodo).
- checked: none — 1, 3-9, 10 (esplicitamente NON marching MoC), 11-15.

### owens_hanson_2007 (registry :186-192)
- (2) averaged functional: precursore EMPIRICO 2007 della regola di design
  a pressione MEDIA (PRECEDENT DUTY per P-1, accanto a S-H nella practice
  line T3); manca funzionale formale e ogni condizione di ottimalita'.
- checked: none — 1, 3-15 (gli 11 fenomeni catalogati restano fenomenologia,
  non monitor formali: (15) dichiarata none dopo valutazione).

### moretti_2002 (registry :194-200)
- (10) per-phase marching: retrospettiva shock-fitting = supporto
  metodologico del fitted-front (F4b/C49) sul brick di marching; manca
  variational side e famiglia.
- checked: none — 1-9, 11-15.

### cooper_shepherd_2008 (registry :202-208)
- (2) averaged functional: impulso single-cycle MISURATO con ugelli; regime
  quasi-steady predetto dalla pressione upstream MEDIA a 1.4 kPa (+43%) =
  istanza pubblicata di adeguatezza average-state; manca funzionale di
  design e riduzione formale.
- checked: none — 1, 3-15.

### ancourt_peter_atinault_2023 (registry :214-223)
- (11) discrete adjoint: equazioni caratteristiche dirette E adjoint in
  variabili conservative, rank-based counting; sponda moderna del ponte
  (45 refs, zero scuola classica); manca il ponte G14.
- (12) certificates: residui ACE come code verification = pratica
  certificate-class nella banca adjoint; App. C steepest descent 6-bump;
  manca classe di certificazione formale (floors, margini).
- checked: none — 1-10, 13-15.

### wolanski_2013 (registry :225-234)
- NESSUNA cella piena: survey di riferimento, "NO nozzle-design methodology
  and the nozzle argued OUTSIDE the problem"; 176 refs a zero incroci
  variazionali = il testimone piu' largo della non-citazione tra le due
  sponde. Il Wave Number W (merito, geometria-detonabilita') non e'
  strutturale rispetto alle 15 componenti.
- checked: none — 1-15.

### kaemming_paxson_2018 (registry :236-247)
- (2) averaged functional: Eqq. (1)-(8) EAP = antenato pubblicato del rung
  int-max; "choking = cycle-integral definition shift" (p.10); manca
  famiglia per-phase e ottimalita' (EAP e' metrica, non design).
- (8) mu measure: Eqq. (10)-(13) = ricostruzione state-averaged del
  reference state — una CONVENZIONE di media dichiarata (antenato della
  domanda sul denominatore); manca teorema sul peso (per noi oggetto
  THEOREM-level).
- (14) truncation/p_b: sec.VI.A + Fig.5 base-force subtraction = SOLO
  igiene di misura (graft A31, findings :1956-1967 [C6-REPAIR: era
  :2540]) — classe geometrica sbagliata, non banda PB-2.
- (15) monitors: Table 1 = l'UNICA statistica p0/T0 di gola pubblicata
  (spread Pt 237%); Fig. 6 sonic line corrugata = l'oggetto che il monitor
  T0-flatness guarda; manca il monitor formale con soglia.
- checked: none — 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13.

### paxson_miki_2022 (registry :249-259)
- (2) averaged functional: Eq. (1) = spinta cycle-averaged = "our J"
  (antenato pubblicato del funzionale); 7 design su 2 linee OFAT, NO
  optimizer; sizing M=1 steady manca l'area ratio ottima ~31%; manca:
  ottimalita', riduzione per-phase, bande.
- (5) imposed-BC contract: pratica del piano-interfaccia con dati CFD
  injector-resolved; "pressure ratio and throat Mach ILL-DEFINED" (p.2);
  manca il contratto formale (classe dati, conteggio caratteristiche, C50).
- (15) monitors: std dev d'interfaccia ~70% delle medie (Jensen breaker
  (b)) = la statistica di violazione di piattezza; manca soglia/monitor.
- checked: none — 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14.

### wintenberger_shepherd_2004 (registry :261-271)
- (2) averaged functional: ciclo FJ come bound sul LAVORO per unita' di
  massa a monte dell'ugello — bound termodinamico medio, "not translatable
  into a propulsive bound by the authors' own admission".
- (8) mu measure: exhibit di dipendenza dallo stato di matching — ordering
  a 3 cicli che si INVERTE tra pre/post-combustion-base matching (graft
  A33, attribuzione primaria Talley & Coy 2002; findings :1956-1967
  [C6-REPAIR: era :2540]) = precedente
  del META-principio "un ordering si inverte"; manca la misura formale mu.
- (9) decomposition identity: decomposizione Delta-s + audit di bilancio
  entropico PER-PHASE Eqq. (23),(31)-(32),(38) (graft A35, findings
  :1956-1967 [C6-REPAIR: era :2540]: wiring gia'
  in src/cycles, 3 condizioni vincolanti); manca l'identita' di
  decomposizione del funzionale J.
- checked: none — 1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15.

### harroun_2021 (registry :273-285) — DEEP-CHECK ESEGUITO (duty a)
- (1) per-phase family: ISOMORFISMO PIU' FORTE del mezzo corpus — "a series
  of axisymmetric simulations ... at different constant-pressure inflow
  conditions spanning the pressure ratios of the detonation-wave cycle"
  (p.670, verificato alla fonte): famiglia di soluzioni STEADY 2-D
  indicizzate dalla fase del ciclo; manca: design/ottimalita' sulla
  famiglia, quoziente formale, certificazione (e il risultato e'
  ranking-blind: 1.25 identico per i due aerospike).
- (2) averaged functional: "quasi-cycle-averaged result" (p.671, verbatim
  loro) del C_F sulla famiglia via waveform Eq. (7); usato SOLO per ranking
  e trovato CIECO a livello di contorno; manca il funzionale come oggetto
  variazionale.
- (5) imposed-BC contract: Eq. (7) = legge di ciclo p-only imposta 1-D a
  monte (choking BYPASSATO) — antenato del contratto Gamma_d (seed C-1bis
  confermato); manca: stato completo, conteggio caratteristiche, contratto
  d'incertezza.
- (6) periodic data class: la waveform Eq. (7) e' un dato PERIODICO imposto
  (istanza p-only); manca la classe di dati full-state + monitor T0.
- (8) mu measure: VERIFICA ALLA FONTE (duty a) — vedi verdetto sotto.
- (9) decomposition identity [C6-FILL, dalla lettura alla fonte del
  refuter]: Fig. 21 + testo p.671 = split additivo del C_F per
  SUPERFICIE (plug vs cowl, IE vs flared) — istanza per-superficie
  della decomposizione di spinta (stesso genere della cella (9) di
  shepherd_kasahara); manca l'identita' dimostrata, i residui
  controllati e il per-fase.
- (14) truncation/p_b: base drag 8x, separazione ritardata, "base pressure
  ... poorly predicted with either analytical models or previous empirical
  results" (p.672, Conclusions) — evidenza diretta sul canale p_b; manca
  chiusura/modello.
- checked: none — 3, 4, 7, 10, 11, 12, 13, 15 [C6-REPAIR: la (9) era
  none, riempita C6-FILL].

**VERDETTO DUTY (a) — peso/denominatore del quasi-cycle-averaging (C-1):**
verificato alla fonte, pp. 670-671 + Eq. (10). Cosa il paper DICHIARA:
C_F = F/(P_c A_t) (Eq. 10, p.671); la media e' costruita "averaging the
discrete constant-pressure axisymmetric computations for each point in
time of the cycle" usando la waveform Eq. (7) — quindi campionamento
per-punto-di-tempo (lettura naturale: media temporale uniforme). Cosa il
paper NON dichiara: NESSUNA formula della media e' stampata; il PESO non e'
dichiarato (mass-weighted? no statement); il DENOMINATORE non e'
disambiguato — non e' scritto se il numero 1.25 e' <F(t)/(P_c(t) A_t)>_t
(media del rapporto, P_c istantaneo) oppure <F>/(<P_c> A_t) (rapporto delle
medie); con P_c(t) variabile le due differiscono. CONFERMA il finding di
record "the averaging convention is UNSPECIFIED"
(`validation/ADVISORY_rde_choking_2026-08-11.md#3-bis`), ora ri-verificato
alla fonte in questa finestra: la convenzione e' UNDECLARED — e questo e'
esso stesso il dato di lineage (Stechmann dichiara mass-weighting, Harroun
non dichiara nulla: la misura mu del campo e' in parte NON DICHIARATA).

### wintenberger_shepherd_2006_fj (registry :291-298)
- (2) averaged functional: ciclo FJ = bound medio di lavoro per ciclo
  (B1/B2/B3 = equazioni A57, validate 99/99 in src/cycles); manca
  traduzione propulsiva e design.
- (8) mu measure: inversione di ranking fixed-static vs fixed-stagnation =
  secondo exhibit di dipendenza dallo stato di riferimento della media;
  manca formalizzazione della misura.
- checked: none — 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15.

### browne_shepherd_sdtoolbox_2018 (registry :300-307)
- (5) imposed-BC contract: lato GENERATORE degli stati imposti (CJ
  equilibrium-Hugoniot, PostShock frozen, zndsolve) — esattamente il ruolo
  "generators free, interface = tables" della direttiva S11; manca il
  contratto (e' un toolbox di stati, non un contratto di dati).
- checked: none — 1-4, 6-15.

### shepherd_kasahara_2017 (registry :309-316)
- (2) averaged functional: modelli analitici di spinta TIME-AVERAGED (PH +
  axial-flow, Eqq. 6, 15-20, 44-45; validati 8/8 in-repo); il wave count N
  CANCELLA nella media (fatto quotient-flavored: la media e' invariante al
  numero d'onde); manca funzionale variazionale e famiglia.
- (9) decomposition identity: split additivo dei contributi di spinta con
  term II ~15-20% = decomposizione a termini del modello; manca l'identita'
  di decomposizione di J con residui controllati.
- checked: none — 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15.

### stechmann_2019 (registry :318-325) — seed C-1 CONFERMATO
- (1) per-phase family: blowdown 0-D per-phase con famiglie FISSE (seed
  verbatim: "0-D blowdown per-phase, FIXED families, no variational
  contouring"); manca: campi 2-D per-phase, contouring, ottimalita'.
- (2) averaged functional: Eq. (4) = antenato 0-D del funzionale (fidelity
  18/18 Table-1 in-repo, `data/st_opt_validation.md`); manca il livello
  di campo e le condizioni di ottimalita'.
- (8) mu measure: mass-weighted averaging DICHIARATO (Eq. 4) — l'unico del
  filone RDE-performance a dichiarare il peso; manca lo status THEOREM del
  peso (per noi il peso e' derivato, non un'abitudine).
- checked: none — 3, 4, 5 (choking = DECLARED ASSUMPTION p.889: assunzione,
  non contratto — valutata e lasciata none), 6, 7, 9, 10, 11, 12, 13, 14, 15.

### rao_1958 (registry :332-338)
- (3) averaged wall conditions: la condizione di parete/superficie di
  controllo classica a DUE moltiplicatori = l'oggetto single-phase che
  (**) media; manca la media (C2 NOT-FOUND(q)).
- (4) weighted transversality: corner/transversality = Eq. [14] p.379
  (verificata in-house su PDF primario, LM:381-386); manca il peso e la
  misura di ciclo ((**') al posto del corner single-phase).
- (10) per-phase marching: la costruzione TOC del bell su superficie di
  controllo = il brick single-state ([X-TOCV] 91/91); manca la famiglia
  indicizzata dalla fase.
- checked: none — 1, 2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15.

### rao_1961_review (registry :340-346)
- NESSUNA cella piena: la lista 1961 dei gap irrisolti mappa 1:1 sul
  programma (materiale di framing P-1) — posizionamento, non procedura.
- checked: none — 1-15.

### rao_1961_spike (registry :348-354)
- (4) weighted transversality: coppia di condizioni endpoint (8)/(9) per il
  plug (swap di etichette page-verified due volte; pairing GENO
  CSTR_PA/CSTR_PB corretto); manca peso/media.
- (10) per-phase marching: costruzione TOC spike/plug single-state; manca
  famiglia.
- checked: none — 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15.

### migdal_1972 (registry :356-362)
- (13) sector tournaments: analogia CAUTA — geometria dello spazio di
  design two-wall (enumerazione di configurazioni annulari, ottimizzazione
  rimandata a Rao); manca il torneo con verdetti per-settore.
- checked: none — 1-12, 14, 15.

### humphreys_thompson_hoffman_1971 (registry :364-370)
- (5) imposed-BC contract: precedente della start-line a geometria
  d'ingresso FISSA (34,373 vs 34,375 lbf) = provenienza del contratto
  d'interfaccia D1; manca dati unsteady/periodici e formalizzazione.
- (10) per-phase marching: design max-thrust plug single-state con inlet
  fissato; manca famiglia.
- (14) truncation/p_b: L'EXHIBIT — swap del modello p_b (Eq. 12->38) muove
  l'altezza di base ottima x2.45 e la pendenza al tip -13.26->-3.08 gradi
  a spinta +0.26% (pp. 1586-1587): argmax O(1), valore piatto; la lezione
  "prezzare le chiusure al design-gradient" e' del 1971.
- checked: none — 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15.

### hoffman_1967 (registry :372-378)
- (4) weighted transversality: p.676 PROVA che la biiezione del corner
  muore per gas reagente — confine frozen-composition del brick in forma
  chiusa (confine di licenza Level-A); manca (**') mediato.
- (10) per-phase marching: metodo generale di contouring single-state per
  flusso chimicamente reagente; manca famiglia.
- (11) discrete adjoint: campi di moltiplicatori lambda_1..lambda_5 su PDE
  lungo le STESSE caratteristiche del flusso = continuous adjoint avant la
  lettre (meta' pubblicata 1967 del ponte G14/P2); manca forma
  discreta/AD e l'identificazione (glossa D-01 CANCELLATA: KT2015 la
  istanzia gia' internamente).
- (12) certificates: E-residual Eq. (78) = residuo di ottimalita' a
  posteriori = antenato del certificato VI.3; manca classe/floor/rejector.
- checked: none — 1, 2, 3, 5, 6, 7, 8, 9, 13, 14, 15.

### scofield_hoffman_1971 (registry :380-386)
- (10) per-phase marching: design max-thrust single-state per gas
  dissociante di nonequilibrio; manca famiglia.
- (11) discrete adjoint: campi di moltiplicatori estesi al noneq (sponda
  Route B del ponte); manca discreto/identificazione. NOTA: precedente
  tabular-EOS per [DIR-THERMOTAB] → componente NUOVA proposta N-18 (GV-1).
- checked: none — 1-9, 12, 13, 14, 15.

### allman_hoffman_1981 (registry :388-394)
- (10) per-phase marching: metodo DIRETTO single-state (prezzo <=0.2%/0.66%
  vs indiretto) = antenato del braccio direct-parametrization; manca
  famiglia. NOTA: parametrizzazione diretta → antenato della componente
  NUOVA proposta N-16 design chart (GV-1).
- checked: none — 1-9, 11-15.

### rao_beck_1994 (registry :396-402)
- (10) per-phase marching: contorni DEF single-state; manca famiglia.
- (12) certificates: Eq. (4) == THEOREM (G) = identita' di confine
  Lambda-form (implementata come boundaryfunction_solve); identificazione
  con Sternin 1961 APERTA (R4); manca certificato eseguibile con floor.
- (14) truncation/p_b: DEF come meccanismo alternativo alla troncatura per
  ridurre la lunghezza; manca chiusura p_b e pricing del bound ladder.
- checked: none — 1-9, 11, 13, 15.

### rao_beck_booth_1999 (registry :404-410)
- (10) per-phase marching: design DEF single-state (frozen/eq chemistry);
  manca famiglia.
- (12) certificates: "optimum ON the validity boundary" = statement
  classico di margin-activity — antenato della certificazione a margine
  attivo; manca il certificato formale (trappola di rinumerazione eq.
  dichiarata di record).
- checked: none — 1-9, 11, 13, 14, 15.

### hoffman_scofield_thompson_1972 (registry :412-418)
- (10) per-phase marching: ottimizzazione single-state con boundary layer
  IN-THE-LOOP (<=0.018% gain = evidenza PRO viscous layering); manca
  famiglia; non-containment strutturale sec.6(c) dichiarato.
- checked: none — 1-9, 11-15.

### johnson_thompson_hoffman_1974 (registry :420-426)
- (4) weighted transversality: lip transversality = dJ/dy_lip classico
  (identita' di gradiente di forma all'endpoint); limite p_a>0 = istanza
  vacuum no-optimum; manca peso/media.
- (5) imposed-BC contract: inflow VARIABILE rotazionale (nonuniforme) =
  antenato di generalita' del contratto d'interfaccia; manca il contratto
  formale e i dati periodici.
- (10) per-phase marching: design plug rotazionale single-state; manca
  famiglia.
- (14) truncation/p_b: split di sensitivity della base-constant → origine
  di DUTY-10 (litmap sec.3.8); manca chiusura derivata.
- checked: none — 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 15.

### vander_veen_1974 (registry :428-434)
- (10) per-phase marching: shrouded plug come DUE problemi di Rao
  disaccoppiati, single-state; manca famiglia (bug GENO S4/S5/S6 di record
  restano).
- (13) sector tournaments: analogia CAUTA — decomposizione in problemi
  disaccoppiati per branch; manca il torneo con verdetti.
- (14) truncation/p_b: base constants 0.846/M^1.3 = il FONDO dello stack
  della chiusura p_b ereditata (riga unreliability; C61: legacy-practiced,
  WG10-FAILED); manca tutto cio' che N2 deve costruire.
- checked: none — 1-9, 11, 12, 15.

### onofri_2002_plug_survey (registry :436-442)
- (14) truncation/p_b: le costanti Veen ricompaiono come Eq. (5.1) WG10,
  riportate UNRELIABLE [+19%,-15%] = floor di model-form del canale (v);
  caveat Angelino planar-only page-anchored; manca chiusura affidabile.
- checked: none — 1-13, 15.

### nasa_rp1104_1983 (registry :444-450)
- (14) truncation/p_b: tangenza grafica di troncamento = surrogato cheap
  che il bound ladder prezza; manca pricing/argmax discipline.
- checked: none — 1-13, 15.

### nasa_sp8120_1976 (registry :452-458)
- (12) certificates: Fig. 6 = confine di fallimento ISTITUZIONALE (eco di
  Sternin) a livello handbook + dichiarazione del GAP di plug-optimization;
  manca ogni certificato formale.
- checked: none — 1-11, 13, 14, 15.

### johnson_boney_1975 (registry :460-466)
- (10) per-phase marching: design MoC real-gas TABULATO a exit uniforme
  (riclassificato non-variazionale); gamma-sensitivity ~80x sul length
  ratio = exhibit di sensibilita' EOS; manca famiglia e variational side.
  NOTA: antenato classico di [DIR-THERMOTAB] → componente NUOVA N-18 (GV-1).
- checked: none — 1-9, 11-15.

### zucrow_hoffman_1977_vol2 (registry :468-474)
- (10) per-phase marching: LA fonte degli unit process del nostro MoC
  (gemellati ESATTI per S-GENOAUDIT); 16-4(c) Rao, 17-5(c) lineage
  rotational max-thrust; manca famiglia e tutto il lato mediato.
- checked: none — 1-9, 11-15.

---

## SEZIONE GV-1 — CHECK DI COMPLETEZZA DELL'ASSE (duty b)

Mappa letta: `docs/rde_nozzle_pipeline_decision_map.md` (integrale, questa
finestra). Nodi totali di record: **79** (62 ledger C1-C62 + 17 non-ledger;
machine summary :262-274 — nota: il brief diceva "62 nodi/45 archi": i 45
archi tornano (44+1 anti-edge E34), i 62 sono i SOLI nodi ledger; il check
e' eseguito su tutti i 79).

### Tabella nodo → componente

| Nodo (stage) | Componente C-1ter | Nota |
|---|---|---|
| PIN-WAVE (1) | 6 periodic data class | pin = la classe stessa |
| C50 (1) | 5 imposed-BC contract | metrica del datum contract |
| C52 (1) | 5 | firma caratteristica su Gamma_d |
| C53 (1) | 5 | placement Gamma_d |
| C54 (1) | 2 averaged functional | rung I4 mean-state della ladder |
| C55 (1/7) | 8 mu measure — CON CAVEAT | aggregazione su P_amb = misura sull'insieme operativo, NON sulla fase; vedi proposta sotto |
| F-1..F-10 block (1) | 5 | findings del contratto |
| C49 (2) | 10 per-phase marching | rappresentazione fitted-front |
| S-5F (2) | 1 per-phase family (+7) | sistema five-field per-phase |
| ROUTE-B (2) | 7 quotient/wave-frame | trattamento elicoidale nativo |
| C51 (2) | 7 | solver wave-frame rung-3a |
| R22-CFD (2/8) | **NESSUNA** → N-19 | referee esterno/validazione |
| C59 (2) | 2 (+6) | forma temporale del funzionale, canonica nel pin |
| C12,C13,C14,C22,C15,C45 (3) | 10 | unit process / marcia; C14 anche 15 (read point) |
| C24,C25,C26 (3) | **NESSUNA** → N-18 | thermo tables backend-1 |
| C5,C6 (3) | **NESSUNA** → N-16 | knot anchoring / insertion guard (chart) |
| C19,C20,C21,C18,C17,C28,C38 (4) | 12 certificates | scale, qualificazione, seed, NTF, trip cap, frontier, stationarity |
| C47 (4) | **F-P** | lint numerico = governance/igiene repo, non componente di metodo |
| C23 (4) | **F-P** | record-failure policy = governance di processo |
| CLG (4) | 12 (+11) | floor di gradiente cross-lowering |
| SDP-CAND-8 (4) | 12 (+N-17) | solver SDP dei certificati |
| C11,C9,C10,C43,C41,C42 (5) | 12 | estimator/bande (C9 anche 10: mesh della marcia) |
| C56 (5) | 11 discrete adjoint | realizzazione adjoint per ruolo |
| C44 (5) | **NESSUNA** → N-17 | passi FD = numerica del driver |
| M-RED (5) | 9 decomposition identity | misura del residuo di riduzione |
| C31,C60,C57,C58,C48,C16,C32,C33,C34,C35,C36,C37,C27,C29,C30 (6) | **NESSUNA** → N-17 | engine/driver TR-Newton, NAND/SAND, exploration (C57 tocca 13), stack (C58 tocca 11) |
| C46 (6) [C6-REPAIR] | **NESSUNA** → N-17 | padding policy engine-internal (choice_ledger :648; "not re-listed per stage" nella mappa, note_C46 — mancava dalla tabella) |
| C39 (6) | 11 | provenienza moltiplicatori |
| C40 (6) | N-17 (+4) | lip equality = seam transversality nell'engine |
| C62 (6) | 8 mu measure | quadratura di fase su Xi = discretizzazione di mu |
| C1,C2,C3,C4,C7,C8 (6) | **NESSUNA** → N-16 | design chart (basis, BC, knots, dof, warm start) |
| R22F-FORCHETTA (7) | 9 (+12) | bracket del gap di riduzione |
| T-DISC (7) | 9 | teorema fiber-separation |
| OBJ-DOM (7) | 2 | dominio dell'obiettivo |
| DELTA-CARRIER (7) | 2 (+12) | rilassamento + campo (value, delta) del Verdict |
| OPTSHIFT (7) | 9 (+12) | rotte argmax-shift |
| D-44 (8) | **NESSUNA** → N-19 | gate dei claim pubblici di adeguatezza |
| P34 (8) | **NESSUNA** → N-19 | gerarchia staged evidence |
| H20 (8) | 14 truncation/p_b | free plume boundary p=Pa |
| C61 (8) | 14 | chiusura p_b |
| DUTY-10 (8) | 14 | sensitivity split base-constant |

### Esito e PROPOSTE (per L2 e il refuter C6)

**45 nodi mappano su una delle 15 componenti; 32 nodi NO (incl. C46);
2 nodi = F-P — totale 79.** [C6-REPAIR: la stesura dichiarava "46/31/2"
ma la tabella ne conteneva 78 (C46 assente) e il 46 non era
riproducibile — conteggio rifatto a mano dal refuter: 45/31/2 = 78,
+C46 → 45/32/2 = 79.]
L'asse C-1ter copre i layer formulazione/riduzione/certificazione ma NON
copre quattro layer interi della pipeline. Propongo **4 righe-componente
NUOVE**:

- **N-16 design-space chart / parametrizzazione** (C1-C8, 8 nodi): basis
  spline, BC, knot law, dof ratchet, warm start. Antenati nel mio mezzo
  corpus: Allman-Hoffman 1981 (metodo diretto parametrizzato); (fuori
  mezzo corpus: Kraiko 2016 Bezier 9-param, cross-ref C1REP registry :541).
- **N-17 optimizer driver / engine** (C16, C27, C29-C37, C40, C44, C46,
  C48, C57, C58, C60 + SDP-CAND-8 parziale, 18 nodi [C6-REPAIR: il
  roster ometteva C58 — che la tabella qui sopra MANDA a N-17 — e C46;
  reintegrati, "17 nodi" era un conteggio su insieme diverso]):
  TR-Newton segmentato,
  NAND/SAND, exploration tier, quadratura numerica. Antenato nel mezzo
  corpus: nessuno (i classici usano condizioni chiuse o ricerca diretta) —
  colonna genuinamente moderna.
- **N-18 thermo closure / tabulated EOS backend** (C24-C26, 3 nodi):
  antenati DIRETTI nel mezzo corpus: Johnson-Boney 1975 (MoC real-gas
  tabulato, [DIR-THERMOTAB]), Scofield-Hoffman 1971 (tabular-EOS
  precedent); Browne-Shepherd SDT = lato generatore.
- **N-19 external referee / evidence tier** (R22-CFD, D-44, P34, 3 nodi):
  referee esterno, gate dei claim, gerarchia di evidenza — nessun antenato
  procedurale nel corpus (CT-3: il campo non ha coppie referee-shaped
  discriminanti).

**F-P dichiarati (2)**: C47 (numeric lint) e C23 (record-failure policy) —
governance del repo/processo, non componenti strutturali del metodo di
design; ragione: nessun contenuto matematico-procedurale confrontabile con
un corpus di letteratura.

**Caveat su C55**: mappato a (8) mu measure SOLO come "misura su un
insieme"; l'asse della misura sull'INSIEME OPERATIVO (P_amb) e' distinto
dall'asse della misura di fase — se L2/refuter preferiscono, e' una
quinta candidata riga N-20 "operating-envelope aggregation" (io la lascio
come sotto-nota di (8), scelta dichiarata).

---

## CANDIDATE RIGHE LEDGER (antenato → cosa fa → cosa gli manca vs noi)

1. **Kraiko-Osipov 1970 → componenti 1/2/3/4/11**: condizione a parete
   pesata integrata nel tempo (3.2) con peso-adjoint W(t), endpoint
   time-averaged, collasso alla famiglia classica → manca misura di ciclo,
   T0-esattezza, quoziente, certificati, identificazione adjoint. Ancora:
   M0:2908-2926 [REP page-verified]; citazione OBBLIGATORIA (CH2:349-355).
2. **Harroun 2021 → componenti 1/2/5/6/8**: famiglia per-phase di soluzioni
   steady 2-D sul ciclo + "quasi-cycle-averaged" C_F via Eq. (7) → manca
   convenzione di media DICHIARATA (verificato alla fonte pp.670-671 questa
   finestra), ottimalita', design loop; risultato ranking-blind (1.25
   flat). Ancora: PDF pp.670-671 + Eq. 10; ADVISORY_rde_choking#3-bis.
   [Seed C-1 CONFERMATO ed ESTESO: l'isomorfismo copre anche la componente
   1, non solo l'averaging.]
3. **Stechmann 2019 Eq. (4) → componenti 1/2/8**: blowdown 0-D per-phase a
   famiglie FISSE con media mass-weighted DICHIARATA → manca contouring
   variazionale, campi 2-D, certificazione. Ancora: registry :319-325;
   `data/st_opt_validation.md` (18/18). [Seed CONFERMATO.]
4. **Kaemming-Paxson 2018 EAP → componenti 2/8/15**: Eqq. (1)-(8) rung
   int-max + (10)-(13) ricostruzione state-averaged (convenzione
   dichiarata) + Table 1/Fig. 6 statistiche di gola → manca famiglia
   per-phase, design, teorema sul peso. Ancora: registry :236-247; M0 EAP
   remark (clause-by-clause).
5. **Paxson-Miki 2022 Eq. (1) → componenti 2/5/15**: spinta cycle-averaged
   = J a livello CFD, OFAT senza optimizer, std dev interfaccia ~70% →
   manca ottimalita', riduzione, bande. Ancora: registry :249-259.
6. **Linea imposed-detonation-BC (Harroun Eq. 7 p-only; pratica
   d'interfaccia Paxson) → componente 5**: legge di ciclo imposta a monte →
   manca contratto full-state, conteggio caratteristiche, C50. [Seed
   C-1bis CONFERMATO.] Antenato STEADY della stessa componente: Humphreys
   1971 start-line fissa (provenienza D1) + Johnson-Thompson-Hoffman 1974
   inflow rotazionale variabile (generalita'). Ancora: registry :364-370,
   :420-426.
7. **Hoffman 1967 → componenti 4/10/11/12**: campi di moltiplicatori su
   caratteristiche + E-residual Eq. (78) + morte della biiezione corner
   p.676 → manca discreto/AD, identificazione (D-01), misura di ciclo.
   Ancora: LM:428-441, :457-464.
8. **Sternin 1961 + Rao-Beck 1994 Eq. (4) → componente 12**: confini
   classici di esistenza/certificabilita' del contorno ottimo →
   identificazione reciproca e con la Lambda-form APERTA (residuo R4).
   Ancora: registry :154-160, :396-402; findings :2059.
9. **Wintenberger-Shepherd 2004 (graft A35) → componente 9**: audit di
   bilancio entropico PER-PHASE Eqq. (23),(31)-(32),(38) → manca
   ri-derivazione frozen, campo contratto (Pt1,Tt1); wiring gia' in-repo.
   Ancora: findings :1956-1967 [C6-REPAIR: era :2540].
10. **Talley & Coy 2002 (via WS-2004 A33) → componente 8**: precedente del
    meta-principio "un ordering si inverte col matching state" → manca
    tutto il lato formale; full text NON in corpus (candidato procurement,
    attribuzione primaria di record). Ancora: findings :1956-1967
    [C6-REPAIR: era :2540].
11. **Sternin 1957/1959 "minimal weight" → componente 2 (PRE-KO?)**:
    candidato antenato averaged-measure PIU' VECCHIO di KO-1970, confidenza
    LOW, default-deflazionario (pesa parametri scalari, non un funzionale
    di forma) → procurement-gated (residuo R3, owner PROC D-31). Ancora:
    findings :2059.
12. **Giles-Ulbrich 2010 (part 2) → componente 11**: teorema
    dell'adjoint-discreto-sbagliato attraverso shock = il rischio che
    C49 fitted-front + discrete-AD-su-fronti-fittati rispondono → nulla
    "manca" (teorema negativo): e' l'antenato dell'AGGIUDICAZIONE, non del
    metodo. Ancora: registry :129-135.

Candidate NUOVE (non gia' nei seed del brief): **7** (righe 4, 5, 7, 8, 9,
10, 11 — le righe 1, 2, 3, 6, 12 confermano/estendono seed o record gia'
nominati; la riga 2 estende il seed C-1 con l'esito del duty (a)).
