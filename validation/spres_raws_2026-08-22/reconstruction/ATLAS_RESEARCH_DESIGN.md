# ATLAS_RESEARCH_DESIGN — Il design della ricerca che alimenta l'ATLAS

Research designer S-PRES, 2026-08-23. Stadio di confronto: il perimetro del
programma (SCAFFOLD §1 :28-65; M0 Parti I-VII, struttura misurata in finestra
— PART I :25, II :63, III :409, IV :2982, V :3008, VI :3047, VII :4246; spina
D6 F0-F6 :37-278 + gate G0-G6 :751-816) contro la copertura bottom-up
esistente (8 capitoli CH1-CH8 + 8 REFUTE + COMPLETENESS_CRITIC, letti/scansiti
in finestra) e il registro letteratura `docs/literature_registry.yaml`
(174 id misurati in finestra: `grep -c "id:"`). Arco di consumo: questo
documento È il contratto delle onde di estensione dell'ATLAS (chi scrive cosa,
dove atterra, quando la mappa si dichiara completa) e l'ossatura narrativa del
deck ESA. Ordine utente vincolante (verbatim-intent): copertura completa ma
con un VERO SENSO DI RICERCA — proposte SOTA sempre da letteratura e
confronto con letteratura, sia per STRUMENTI che per SENSO (precedenti di
nozzle per RDE, come vengono fatti, topologia campo).

Principio di derivazione (dichiarato): la matrice del §1 è derivata A PRIORI
dal perimetro (SCAFFOLD layer L0-L6, Parti M0, spina D6), NON dai 21 buchi del
critic; il critic entra solo al §4, come lista da DISPORRE nelle celle già
derivate. Se una riga del critic non trovasse cella, la matrice sarebbe
sbagliata — è il test di auto-consistenza del design (esito: 21/21 trovano
cella, §4).

------------------------------------------------------------------------------
## §0 Le 5 dimensioni obbligatorie (colonne della matrice)

Ogni cella (riga-aspetto × colonna-dimensione) porta UNO di: puntatore a
capitolo/sezione che la copre; "SCOPERTA" + contratto di copertura;
"FUORI-PERIMETRO" con ragione. Le colonne:

- **(i) STATO INTERNO** — teoremi/classi di rigore/aperti dell'aspetto
  (sorgente: M0 + registri; nel capitolo: §1 Ricostruzione + §2 Stato
  per-claim).
- **(ii) STRUMENTI vs LETTERATURA** — per ogni strumento usato: cosa usa il
  mondo SOTA (ref dal registry), cosa usiamo noi, perché. Strumenti censiti
  (tutti con letteratura IN literature/ e riga nel registry):
  ottimizzatore TR-Newton (`nocedal_wright` 2006; `byrd_hribar_nocedal` IP
  1999; `sun_nocedal` noise-tolerant TR 2023; UNO `vanaret_leyffer` 2026;
  `deuflhard` Newton affine-invariant 2011); adjoint continuo/discreto
  (`giles_pierce` 1997/2000/2001; `lozano_2018` singolarità adjoint Euler;
  `lozano_2019` mesh non-convergence; `hicken_zingg` dual consistency 2014);
  AD/JAX (dossier G0 `docs/rde_nozzle_G0_decision.md`, D6 :753-774);
  DWR/error estimation (`becker_rannacher`; `venditti_darmofal` 2000;
  `fidkowski_darmofal` review 2011); spline/parametrizzazione (`masters_2017`
  confronto geometrico; `lauer_ansell` review 2025); MoC e alternativa
  shock-tracking (`zucrow_hoffman_1977_vol2`; `huang_zahr` 2022;
  `thakur_nadarajah` 2025; GENO dual-code); thermo tabulata (Cantera;
  `browne_shepherd_sdtoolbox_2018`; direttiva S11 backend-tabelle);
  certificati (`yamamoto_1986` Newton-Kantorovich; `shi_xie` FD interval
  2022; disciplina rejector R5).
- **(iii) SENSO/PRECEDENTI vs LETTERATURA** — come il campo fa i nozzle per
  RDE (i 4 paper P-A..P-D, harvest, figure-atlante, topologia campo:
  `harroun_2020/2021`, `stechmann_2019`, `jourdaine_2019` aerospike,
  `liu_2022`, `li_xu...2023/2025`, `teasley_2023/2025`); i precedenti
  classici (genealogia Rao→Kraiko: `rao_1958`, `rao_1961_spike`,
  `kraiko_osipov_1970`, `kraiko_2001_plug`, `kraiko_2016_two_sided`,
  `kraiko_tillyaeva_2015`; linea Purdue `hoffman_1967`,
  `humphreys_thompson_hoffman_1971`, `scofield_hoffman_1971`,
  `vander_veen_1974`); le metriche del campo (`kaemming_paxson_2018` EAP,
  `paxson_miki_2022`); cosa manca al campo (gap NOT-FOUND(q) query-bounded,
  CH5 §1.6, G14).
- **(iv) POSIZIONE/PROPOSTA SOTA** — cosa il programma propone di
  nuovo/meglio, SEMPRE query-bounded (M0 Parte I :56-60: tre passate
  avversarie indipendenti; residuo G5 dichiarato).
- **(v) APERTI** — aperti + falsificatori + decisioni pendenti (owner e
  trigger nominati, mai riempiti nel capitolo).

------------------------------------------------------------------------------
## §1 LA MATRICE DI COPERTURA A PRIORI

Righe = 16 aspetti (A-P), enumerati dal perimetro: layer SCAFFOLD L0-L6 →
righe A, K, J, P; Parti M0 I-VII → righe B, C, D, G, H, I, L; spina+gate D6 →
righe L, M, O; corpo esistente CH1-CH8 → verificato che ogni capitolo abbia
riga (nessun capitolo orfano). 16×5 = 80 celle.

### Riga A — Problema (P), pin classe-dati, contratto d'interfaccia
(L0/L1 SCAFFOLD :30-37; M0 II D2.1-D2.6 :63-120)
- (i) COPERTA: CH1 §1.1 (:30-58) + CH1 §2.
- (ii) COPERTA (parziale): la classe A spline C^{1,1} per settore (D2.1) vive
  in CH4 §1.3 (choice ledger); il confronto con `masters_2017`/`lauer_ansell`
  → §7 POSIZIONAMENTO di CH1 (contratto in §2 qui sotto).
- (iii) SCOPERTA-parziale: la metà positiva "pin ESIBITO nei CFD (P-C
  phase-locked)" senza ancora (critic riga 14) → riga in CH5 + scope R20 in
  CH6 §1.6.
- (iv) COPERTA con riparazione: CH1 §1.1 (novità del pin dichiarato,
  search-proven) — da allineare allo scope hardware-vs-CFD (critic 14).
- (v) COPERTA: CH1 §3.

### Riga B — Ladder di idealizzazione, quoziente, rung, PB-1..PB-5
(M0 I-II; D-JEX/D-MU :73-114)
- (i) COPERTA: CH1 §1.2-1.4. (ii) FUORI-PERIMETRO strumenti: la ladder è
  struttura concettuale, non tool — il suo posizionamento è senso, colonna
  (iii). (iii) COPERTA: CH5 §1.1-1.2 (average-then-design del campo,
  dicotomia D-1). (iv) COPERTA: CH1 §1.3 (quoziente esatto + rung 2
  dichiarato = la proposta). (v) COPERTA: CH1 §3 (PB-2 OPEN).

### Riga C — Sistema di ottimalità mediato (**'), shared wall, adjoint per-fase
(M0 III :409+)
- (i) COPERTA: CH2 integrale. (iii) COPERTA: CH2 §1.8 (bridge P-2 e
  genealogia) + CH5 §1.4 (Guderley-Hantsch → per-phase brick).
- (ii) SCOPERTA: CH2 non posiziona i SUOI strumenti (adjoint continuo
  per-fase con first integral f2=-lambda2, CH2 §1.2) contro il mondo
  (discrete-adjoint AD prevalente in ASO; dual consistency `hicken_zingg`;
  patologie `lozano_2018/2019`; `giles_pierce_2001` error correction).
  CONTRATTO: §7 POSIZIONAMENTO di CH2 — perché continuo-prima (struttura
  variazionale di Rao = il first integral È l'oggetto di design) + dove il
  discreto rientra (O3.1 machine precision, G0 :753-774).
- (iv) COPERTA: CH2 §1.3 (shared wall = frase di design). (v) COPERTA: CH2 §3.

### Riga D — Riduzione e fisica del residuo (T-DISC, T-RED, FORCHETTA, M-RED)
(M0 III; ancore CH3: M0:977-1280, :1734-1909, :1283-1494)
- (i) COPERTA: CH3 §1.1-1.4. (iii) COPERTA: CH3 §1.5 (no-external-referee)
  + CH5. (iv) COPERTA: CH3 §1.3 (forchetta a 6 canali).
- (ii) SCOPERTA: la forchetta È una error estimation goal-oriented "a mano":
  il confronto con DWR (`becker_rannacher`, `venditti_darmofal`,
  `fidkowski_darmofal`) manca. CONTRATTO: §7 di CH3 — noi bound per-canale
  con fisica nominata vs mondo bound adjoint-weighted a posteriori; perché
  (i canali sono decisioni di modellazione, non errore di discretizzazione).
- (v) SCOPERTA-parziale: G3 unsteadiness gate — "the only gate whose kill
  threshold cannot reject" (D6 :783-786) assente (critic 17). CONTRATTO:
  aperto nuovo in CH3 §3 + riga roadmap CH6.

### Riga E — L'edificio averaging/swirl (2.5-D per-fase, R22-F, swirl5f)
(M0 VI.1 [MS-*] :3047+; advisory swirl5f)
- (i) COPERTA: CH7 (3 piani). (iii) COPERTA-parziale: CH7 §1.4.
- (ii) SCOPERTA: chiusura mean-swirl e trasporto Gamma=R·w vs letteratura
  swirl-nozzle (Tillyaeva 1975 free-vortex — riga G5 2.2(f), D6 :803-806;
  `wanted_tillyaeva_1975` nel registry). CONTRATTO: §7 di CH7.
- (iv) COPERTA: CH7 §1.3 (centerpiece R22-F). (v) COPERTA: CH7 §3 (S-5F,
  C51 pendenti — decisioni utente).

### Riga F — Lo spazio di design: configuration-free, settori, torneo
(M0 I discovery (3) OP-11 :52-55; census topologico)
- (i) COPERTA: CH8 §1.1-1.5. (iii) COPERTA: CH8 §1.3 (la tassonomia classica
  collassa) + CH5 (plug/aerospike del campo: `jourdaine_2019`, `liu_2022`,
  `li_xu_lv_yu_zhou_2025` cowl regolabile). (iv) COPERTA: CH8 §1.1 (il TIPO
  è un output = la proposta).
- (ii) SCOPERTA: parametrizzazione per-settore vs mondo (level-set/CAD-based
  in `lauer_ansell`; confronto geometrico `masters_2017`). CONTRATTO: §7 di
  CH8. (v) COPERTA con estensione: CH8 §3 + fase F3 mai nominata (critic 8)
  → CH8 §3.5 + legenda CH6.

### Riga G — Il contratto di ottimalità globale M1-M5
(M0 PART IV :2982-3005: EXISTENCE + NECESSARY + SECOND-ORDER + GLOBALITY by
DECLARED MECHANISM; ogni Verdict dichiara meccanismo e forza)
- TUTTA LA RIGA SCOPERTA (critic 4; grep capitoli in finestra critic: 0 hit).
  CONTRATTO: CH8 §1.7 nuovo "Dal KKT locale al globale: il contratto M1-M5"
  — (i) i 5 meccanismi con istanze di record (T4=M1, T3=M2, 1-DOF=M3);
  (ii) M4/M5 vs mondo (deflated continuation, branch-and-bound Lipschitz —
  `nocedal_wright` per il quadro; claim di confronto query-bounded al
  registry); (iii) il mondo ASO si ferma al KKT locale (nessun paper
  P-A..P-D dichiara meccanismo di globalità — claim search-proven da
  eseguire in onda); (iv) "ogni Verdict dichiara meccanismo e forza" = la
  proposta; (v) C57 NEVER (CH4 Q2) + target M3 unimodalità truncated-plug.

### Riga H — Generality ladder e licensing fuori-pin
(M0 PART V :3008-3045: per classe di flusso; S-GBE muro ergodico; B-lite;
CVaR/DD-DRO; "honest refusal of certificates" per il caotico)
- TUTTA LA RIGA SCOPERTA (critic 5; grep "S-GBE|B-lite|ergodic|CVaR": 0 hit).
  CONTRATTO: CH1 §1.7 nuovo "Fuori dal pin: la ladder di licensing" —
  (i) tabella per classe (single-wave→certificato pieno; RPO→PRACTICE;
  multistabile→CVaR/DD-DRO; caotico→rifiuto onesto + muro [S-GBE]
  J_exact+ <= F_env senza Birkhoff); (ii) strumenti di licensing (flatness
  monitor, census refresh); (iii) il campo non dichiara MAI il regime di
  validità del proprio metodo (posizionamento da eseguire); (iv) il rifiuto
  onesto come proposta honesty-first (materiale deck); (v) B-lite = "the
  cheap exact meter of the rung-2 sweep" → cross-ref in CH3 accanto ai
  deriver (contratto del critic 5 adottato).

### Riga I — La macchina: pipeline 8 stadi, scelte, engine, velocità
(M0 PART VI :3047+; choice ledger; S25 M-CHAIN)
- (i) COPERTA: CH4 §1.1-1.4. (iv) COPERTA: CH4 §1.1.
- (ii) SCOPERTA-parziale: il choice ledger (CH4 §1.3) pesa alternative ma
  senza ref bibliografiche sistematiche. CONTRATTO: §7 di CH4 — TR-Newton
  segmentato vs SQP/IP (`nocedal_wright`, `byrd_hribar_nocedal`, UNO
  `vanaret_leyffer`), rumore (`sun_nocedal`), passo certificabile
  (`deuflhard`, `yamamoto_1986`); JAX custom_vjp vs Enzyme (G0 :753-774);
  MoC vs shock-tracking implicito (`huang_zahr`, `thakur_nadarajah`) —
  perché MoC: esattezza caratteristica + certificati per-cella (X-GENOXC);
  thermo tabulata (S11) vs Cantera-in-the-loop.
- (iii) SCOPERTA-parziale: la pipeline vs i framework ASO del mondo (i 4
  paper RDE usano CFD+sweep, nessuna catena design-adjoint: ancora CH5 §1.1)
  → una sottosezione del §7 di CH4.
- (v) COPERTA con estensioni: CH4 §3 + riga suite 23/23 con incidente
  dichiarato (critic 15) + engine-speed S25 (catena di record 100.8→32.1 s,
  vg 6.6x, tier ondemand+staleness — memoria s25/s25bis) → CH4 §1.6 nuovo
  "La velocità come scelta algoritmica" (ADJUDICATO: estensione, non
  capitolo — la matrice mostra (i) già coperto da CH4 §1.4; un capitolo
  intero sarebbe peso senza celle).

### Riga J — Certificazione e oracoli end-to-end
(SCAFFOLD L2/L4 + G1 assoluto D6 :775; S-CERT; O3.x; dual-code GENO)
- TUTTA LA RIGA SCOPERTA (celle sparse in CH4 §1.4/§2 senza casa organica).
  CONTRATTO: CH9 NUOVO "Certificazione: la catena che può dire NO" —
  (i) G1 assoluto; catena oracoli O1/O2/O3.1-O3.4; KAT; dual-seed; verdetto
  S-CERT di record = NON-CERTIFICABILE con 2 P0 (uno riparato in-window,
  staleness import-closure → F2) + MC8 8/8 (memoria fservice-scert: il
  verdetto onesto È contenuto); C-O33 quantificata (classe di design);
  (ii) `yamamoto_1986` N-K per il passo, `shi_xie` per FD interval, DWR per
  le barre vs la nostra disciplina rejector R5 (tolleranze derivate);
  (iii) il principio "cross-code agreement != truth" (memoria moc-critical) e
  gli invarianti indipendenti vs la prassi del campo (validazione a
  confronto singolo); (iv) il formato Verdict (contorno + certificati +
  barre + record oracoli) = proposta; (v) staleness → F2, C-O33 aperta.

### Riga K — Contratto-dati, ledger conditionals L4, G6, taxonomy di input
(SCAFFOLD L4 :43-46; D2.4 :116-120; G6 :808-815; Annex B D6 :1133-1134;
F2a contact/slip + U3' :176-202)
- TUTTA LA RIGA SCOPERTA (critic 20 ne è l'istanza; L4/G6/U3' mai organici).
  CONTRATTO: CH10 NUOVO "Il contratto dei dati: cosa serve per girare su un
  motore VOSTRO" — (i) D2.4 + audit stage-A (Crocco, completezza, H-I2) +
  G6 loud-reject + ledger L4 (closure- vs analysis-conditional); U3'
  choking adjudication PREMISE-OPEN; contact/slip ownership F2a;
  (ii) pipeline CFD-to-contract (lineage Gelb-Tadmor concentration +
  Paciorri-Bonfiglioli fitted-front, D6 :256-263) vs la nostra
  front-extraction con banda derivata; (iii) il campo consegna CFD, non
  contratti-dati (nessun paper P-A..P-D dichiara classe di dati — ancora
  CH5 §1.1 + critic 14); (iv) Annex B input taxonomy = la risposta pronta
  alla domanda ESA "che input serve" (D6 :1133-1134); (v) U3' aperto con
  owner F2a, contratto MAI freezato prima.

### Riga L — Fasi, gate, roadmap, canale pubblicazioni
(D6 spina F0-F6 :37-278 + G0-G6 :751-816; M0 VII :4246)
- (i) COPERTA-parziale: CH6 §1.5 (deciders) — ma legenda solo F2/F4b/F5
  (critic 8: F3 GEOMETRY CLASSES :214 e F6 :275 assenti). (iii) COPERTA:
  CH6. (iv) COPERTA: CH6 §1.6 (ask). (ii) FUORI-PERIMETRO strumenti (la
  spina è governance, non tool).
- (v) SCOPERTA-parziale: G2 VALUE GATE theorem-grade con kill criterion +
  calibrazione thrust-stand ~0.5-1% (D6 :776-782; critic 7) → CH6 §1.5+Q1;
  collocazione temporale F4b vs deciders (critic 18) → CH6 §1.5; stato P-2
  freeze FIRED 2026-08-11 con blocker C1 owner F2 (D6 :91-100; critic 19)
  → CH6 §1.6 riga canale paper.

### Riga M — Corrector e unsteadiness (G3/G4, VI.4bis, O(St))
- (i) COPERTA-parziale: CH3 (canale O(St)); scope corrector = perturbazione
  dello sweep steady (memoria periodic-wave-data-scope; M0 VI.4bis).
  (iii) COPERTA: CH5 §1.5 (linea unsteady, i tre MANDATORY, ponte adjoint).
  (iv) COPERTA: CH3. (ii) COPERTA via riga I (stessi strumenti).
- (v) SCOPERTA: il difetto DICHIARATO di G3 (trigger senza numero, D6
  :783-786) + G4 decoupling mai nominato (critic 17). CONTRATTO: CH3 §3
  aperto nuovo + una riga nella roadmap CH6 §1.5 (F5b: trigger derivato
  come NUMERO prima del corrector, D6 :271-273).

### Riga N — Letteratura RDE-nozzle e posizionamento di metrica
(CH5; remark EAP M0 :2526-2539)
- (i) COPERTA: CH5 integrale (4 metodi, genealogia, threat ledger CT-1..8,
  harvest). (ii) FUORI-PERIMETRO strumenti (è la riga-senso per eccellenza;
  gli strumenti del campo sono censiti in colonna (iii) delle altre righe).
  (iii) COPERTA: CH5 §1.1-1.8. (iv) COPERTA: CH5 §1.6 (gap G14
  query-bounded).
- (v) SCOPERTA-parziale: posizionamento J vs EAP/pressure-gain
  (`kaemming_paxson_2018`, `paxson_miki_2022`; M0 :2526-2539 "the P4
  corrector is EAP's missing error bar"; critic 6) → CH1 §1.2 accanto a
  [D-MU] + eco in CH5; ancore figura mancanti P-C Fig. 21 (critic 11),
  P-B Fig. 16 + O(10:1) (critic 16), box nomenclatura P-B/p_b/PB-2/Gap B +
  namespace G (critic 9) → CH5 §1.2/§1.8 + legenda CH6 §6.

### Riga O — Value case e onestà (Gap A/B, PB-2, G2, rifiuto onesto)
- (i) COPERTA: CH6 §1.1-1.4, §1.7. (iii) COPERTA: CH6 + CH5 (EAP come
  metrica di valore del campo — si salda alla riga N(v)). (iv) COPERTA:
  CH6 §1.7 (l'onestà come strategia). (ii) FUORI-PERIMETRO strumenti.
- (v) SCOPERTA-parziale: G2 kill criterion (critic 7, → riga L(v));
  riconciliazione strictness PB-2 tra CH1/CH6/storyboard (critic 10) →
  CH6 §1.2 alla forma CH1; hedge sizing single-instance (critic 13) →
  CH6 Q1.

### Riga P — La storia della ricerca stessa (metodo del programma)
(SCAFFOLD L0 direttive; S-FOUNDATIONS: derivazione originale → riderivazione
agnostica Fase A → convergenza; disciplina dual-proof)
- TUTTA LA RIGA SCOPERTA: nessun capitolo porta la STORIA della propria
  materia (come il claim è nato, come la Fase A lo ha riderivato alla cieca,
  dove è convergiuto — es. di record: Fase D a convergenza in M0 per
  T-DISC/FORCHETTA, memoria s-foundations-c4-closed). CONTRATTO: non un
  capitolo nuovo ma una SEZIONE OBBLIGATORIA §6 STORIA in OGNI capitolo
  (template §2 qui sotto) — la storia è per-argomento, non centralizzabile.
  È anche la risposta alla domanda-panel "come vi fidate delle vostre
  derivazioni": derivazione doppia e indipendente, diff a registro.

### Conteggio celle (misurato sulla matrice qui sopra)
- 80 celle totali (16 righe × 5 dimensioni).
- COPERTE: 44. FUORI-PERIMETRO dichiarate: 6 (B-ii, L-ii, N-ii, O-ii +
  2 assorbimenti dichiarati M-ii→I, O-iii→N).
- SCOPERTE: 30 — di cui 20 in 4 righe interamente scoperte (G, H, J, K) +
  la riga trasversale P (sezione-template, 5 celle) e 10 parziali
  (A-iii, C-ii, D-ii, D-v, E-ii, F-ii, I-ii, I-iii, L-v, M-v, N-v, O-v —
  le parziali con riparazione leggera contano mezzo nel peso, §5).

------------------------------------------------------------------------------
## §2 LA DERIVAZIONE DEI CAPITOLI DALLA MATRICE

### 2.1 Capitoli nuovi (derivati dalle righe interamente scoperte)
La regola di derivazione: una riga interamente scoperta con (i) proprio E
letteratura propria = capitolo; una riga scoperta solo su alcune dimensioni =
estensione del capitolo che già ne porta lo stato interno; una riga
trasversale = sezione di template. Applicata:

- **CH9 — Certificazione e oracoli end-to-end** (riga J: 5/5 scoperte, stato
  interno proprio = S-CERT/G1/O3.x/KAT/dual-seed, letteratura propria =
  N-K/DWR/FD-interval). Unifica i due candidati noti "certificazione/S-CERT"
  e "oracoli/adjoint-end-to-end": la matrice li mette nella STESSA riga
  (stessa famiglia di celle, G1 è il gate di entrambi) — due sezioni, un
  capitolo.
- **CH10 — Il contratto dei dati** (riga K: 5/5 scoperte, stato interno
  proprio = D2.4/L4/G6/Annex B/U3', letteratura propria = front-extraction
  lineage). Copre il candidato "contratto-dati/L4".
- **CH-REF — Atlante di riferimento** (derivato non da una riga ma dal
  criterio di completamento lint §5: "ogni id dei registri → capitolo"
  richiede una casa per gli id che nessuna riga tematica reclama —
  glossario, mappa registry→capitolo, legenda namespace (critic 9 famiglia
  G), ordine di lettura §3). Capitolo di servizio, senza claim propri:
  niente §6/§7.

Candidati NON promossi a capitolo (aggiudicazione dalla matrice, non dalla
lista): "engine-speed" → CH4 §1.6 (riga I(i) già coperta da CH4);
"corrector/G3" → CH3 §3 + CH6 §1.5 (riga M coperta-parziale, solo (v)
scoperta); "P-1/P-2 status" → CH6 §1.6 (riga L(v), una riga di canale, non
un capitolo).

### 2.2 Estensioni dei capitoli esistenti (dalle celle scoperte parziali)
- **CH1**: §1.7 nuovo "Fuori dal pin: la ladder di licensing" (riga H
  intera); §1.2 esteso con la remark EAP (N(v), critic 6); allineamento
  scope critic 14.
- **CH2**: nessuna sezione-contenuto nuova; §7 POSIZIONAMENTO (C(ii)).
- **CH3**: §3 aperto nuovo G3/G4 (M(v), critic 17); caveat band-underinclusion
  sul +0.51% in §1.3(iv) (critic 12); cross-ref B-lite (riga H); §7 con DWR
  (D(ii)).
- **CH4**: §1.6 nuovo engine-speed (I(v)); riga suite 23/23 con incidente in
  §1.4 (critic 15); puntatore Annex B in §1.2 (critic 20, con CH10); §7
  strumenti (I(ii)-(iii)) — la sezione più pesante del posizionamento.
- **CH5**: righe-ancora Fig. 21 (critic 11), Fig. 16 + ordine fluttuazioni
  (critic 16), riga P-C phase-locked (critic 14), box nomenclatura esteso
  (critic 9); eco EAP.
- **CH6**: §1.5 esteso con G2 kill criterion (critic 7), F3/F6 in legenda
  (critic 8), collocazione F4b (critic 18); §1.6 riga P-2 freeze (critic
  19); §1.2 riconciliato alla forma CH1 (critic 10); Q1 hedge single-instance
  (critic 13); scope R20 vs CFD (critic 14).
- **CH7**: tabella "Disposizione riparazioni" onda W2 (critic 1, BLOCKING);
  §7 con Tillyaeva/free-vortex (E(ii)).
- **CH8**: tabella "Disposizione riparazioni" onda W2 (critic 1, BLOCKING);
  §1.7 nuovo contratto M1-M5 (riga G intera, critic 4); §3.5 fase F3
  (critic 8); §7 parametrizzazione (F(ii)).

### 2.3 Il TEMPLATE OBBLIGATORIO arricchito (ogni capitolo, CH-REF escluso)
1. **Ricostruzione** (esistente) — con glossario minimo dove serve.
2. **Stato per-claim** (esistente) — classi di rigore + ancore.
3. **Aperti** (esistente) — owner/trigger, mai riempiti nel capitolo.
4. **Domande da panel** (esistente) — banco utente incluso, risposte ancorate.
5. **Cosa dice il deck** (esistente) — con la regola retro-audit.
6. **STORIA** (NUOVA OBBLIGATORIA, riga P) — tre battute per argomento:
   derivazione originale (sessione/commit di nascita, ancora) →
   riderivazione agnostica Fase A (cosa il derivatore cieco ha ritrovato,
   diff) → convergenza (dove il record è cambiato, classe finale). Fonte:
   M0/PROGRESS/ledger; niente ricordi, solo ancore (navigation-first).
7. **POSIZIONAMENTO LETTERATURA** (NUOVA OBBLIGATORIA, colonne (ii)+(iii)) —
   due metà FISSE: (a) STRUMENTI: per ogni tool del capitolo, la terna
   mondo-SOTA (ref dal registry `docs/literature_registry.yaml`, id citato)
   / cosa usiamo / perché; (b) SENSO: i precedenti del tema (RDE + classici)
   e il gap che il capitolo occupa, query-bounded. Ogni ref = un id del
   registry; ref fuori registry = riga nuova nel registry PRIMA dell'uso.
8. **Disposizione riparazioni** (esistente dove c'è refutazione) — nessun
   capitolo si dichiara chiuso con findings non disposti.

------------------------------------------------------------------------------
## §3 LA NARRATIVA DELLA RICERCA (ordine di lettura = ossatura deck ESA)

Research design classico, sette atti; ogni atto = capitoli in ordine:

1. **CONTESTO CAMPO** — come si fanno oggi gli ugelli per RDE: 4 paper,
   4 metodi, average-then-design o sweep CFD; metrica EAP; genealogia
   classica Rao→Kraiko che il campo eredita senza la parte variazionale.
   [CH5 §1.1-1.5 + CH1 §1.2-EAP]
2. **GAP** — nessuna riduzione per-fase dichiarata, nessun contratto-dati,
   nessun certificato, gap query-bounded NOT-FOUND(q). [CH5 §1.6 + CH10
   (iii) + CH9 (iii)]
3. **DOMANDA DI RICERCA** — il funzionale mediato sul ciclo: quando il
   design-sulla-media è esatto (e perché il campo "funziona"), quanto costa
   quando non lo è, che topologia seleziona la misura. [CH1 + CH8 §1.1]
4. **METODO** — l'ottimalità mediata (shared wall, adjoint per-fase); la
   riduzione con residuo ESATTO scritto; l'edificio swirl; la macchina a
   8 stadi con le scelte pesate; il contratto di ottimalità globale M1-M5;
   il contratto-dati; la certificazione che può dire NO. [CH2 → CH3 → CH7 →
   CH4 → CH8 §1.7 → CH10 → CH9]
5. **EVIDENZA** — il torneo già giocato (T3/T4/ceiling); i numeri engine con
   stage dichiarato; +0.51% in-class col caveat; suite 23/23 con incidente
   dichiarato; oracoli 91/91. [CH8 §1.4 + CH4 §1.4-1.6 + CH9]
6. **ONESTÀ/LIMITI** — Gap A/B; PB-2 non ancora un numero; G2 kill criterion
   (la morte onesta è nel piano); G3 senza numero; il rifiuto onesto del
   caotico; verdetto S-CERT. [CH6 + CH1 §1.7 + CH9]
7. **ROADMAP + ASK** — deciders in ordine, F2→F6 con F3 nominata, canale
   P-1/P-2, Annex B "cosa ci serve da voi". [CH6 §1.5-1.6 + CH10-Annex B]

In una riga: *il campo disegna l'ugello RDE mediando prima e sperando poi;
noi dimostriamo QUANDO mediare è esatto, misuriamo QUANTO costa quando non lo
è, e consegniamo l'ottimo con certificato e contratto-dati — dichiarando ad
alta voce dove il certificato oggi si ferma.*

Nota deck: gli atti 1-3 sono la sezione-letteratura ordinata dall'utente
(plots del campo inclusi, meccanismo extract_figs + citazione piena, CT-6
sui loro numeri — commit adf50b2/1514641); l'atto 6 è il vantaggio
competitivo honesty-first; il PONTE B1 (numero "4-13") resta sospeso finché
la sua composizione non è aggiudicata (critic 2, disposta dall'orchestratore).

------------------------------------------------------------------------------
## §4 DISPOSIZIONE DELLE 21 RIGHE DEL CRITIC (test di auto-consistenza)

Ogni riga → cella/capitolo del design. BLOCKING: 1-3; MAJOR: 4-11; MINOR:
12-21 (severità dal critic).

| # | cella matrice | disposizione (dove atterra) | onda (§5) |
|---|---|---|---|
| 1 | J/F (processo) | CH7+CH8 tabelle "Disposizione riparazioni" (22 findings; ALTI: REFUTE_CH8 #1-2, REFUTE_CH7 #2) | W-A |
| 2 | N(v) | GIÀ DISPOSTA dall'orchestratore nello storyboard (composizione "4-13" da aggiudicare o kicker riformulato; se aggiudicata → riga CH3 §1.3/CH5) | W-A (verifica) |
| 3 | I(ii) | GIÀ DISPOSTA dall'orchestratore nello storyboard (C13 riformulata alla forma CH4 W2-R2: 62 TIPIZZATE, 48 aggiudicate) | W-A (verifica) |
| 4 | G (riga intera) | CH8 §1.7 nuovo (contratto M1-M5) | W-B |
| 5 | H (riga intera) | CH1 §1.7 nuovo + cross-ref B-lite in CH3 | W-B |
| 6 | N(v)/A | CH1 §1.2 (remark EAP accanto a [D-MU]) + eco CH5 | W-B |
| 7 | L(v)/O(v) | CH6 §1.5 + Q1 (G2 VALUE GATE + thrust-stand) | W-B |
| 8 | L(v)/F(v) | CH6 legenda F3/F6 + CH8 §3.5 | W-B |
| 9 | N(v)/O | CH5 box §1.1 esteso + legenda CH6 §6 (collisioni P-B/p_b/PB-2/Gap B + namespace G) + nota stile deck; eredita casa in CH-REF | W-B |
| 10 | O(v) | CH6 §1.2 riconciliato alla forma CH1 (+ storyboard C7-ter, canale orchestratore) | W-B |
| 11 | N(v) | CH5 §1.2/§1.8 riga Fig. 21 con ancora pC | W-B |
| 12 | D(v) | CH3 §1.3(iv) caveat band-underinclusion | W-B |
| 13 | O(v) | CH6 Q1 + §1.4 forma CH3 (single-instance) | W-B |
| 14 | A(iii) | CH5 riga P-C phase-locked + CH6 §1.6 scope R20 | W-B |
| 15 | I(v) | CH4 §1.4 riga suite 23/23 + incidente capture (ancora c9bacd9) | W-B |
| 16 | N(v) | CH5 §1.2 Fig. 16; ordine fluttuazioni ancorato o riformulato (CH1/CH5) | W-B |
| 17 | M(v) | CH3 §3 aperto G3/G4 + riga roadmap CH6 | W-B |
| 18 | L(v) | CH6 §1.5 frase collocazione F4b | W-B |
| 19 | L(v) | CH6 §1.6 riga canale paper (P-1 + P-2 freeze FIRED 2026-08-11) | W-B |
| 20 | K(iv) | CH10 (casa organica) + puntatore CH4 §1.2 + CH6 ask | W-B |
| 21 | processo | Mini-pass di verifica sulle sole righe [W2-*] di CH1-CH6 (o rischio accettato dichiarato nel log di chiusura) | W-C |

Esito del test: 21/21 righe trovano cella — la matrice a priori contiene la
lista a posteriori. Le 3 BLOCKING sono in W-A (prima onda, gate di ogni onda
successiva).

------------------------------------------------------------------------------
## §5 PIANO D'ESECUZIONE (onde, contratti, peso, completamento)

Regole standing applicate: connessione artefatti (ogni brief nomina stadio di
confronto + arco di consumo), peso right-sized pre-lancio con shape/round/
token nel log (SR-9), artefatti su file subito, resume-non-relaunch, niente
installazioni, conteggi rigenerati da comando in finestra (SR-12).

### Onda W-A — RIPARAZIONI (gate: le BLOCKING a zero)
- A1 (writer): CH7 — applica i 12 findings REFUTE_CH7 + tabella
  Disposizione. A2 (writer): CH8 — 10 findings + tabella (gli ALTI #1-2
  con aggiudicazione esplicita, non softening). Brief: read-then-quote,
  ancora verificata prima di ogni edit.
- A3 (verifier): verifica che le righe critic 2-3 siano davvero disposte
  nello storyboard (diff contro STORYBOARD.md) — esito nel log.
- Peso: 3 agenti × 1 round, ~120-180k token.

### Onda W-B — ESTENSIONI + CAPITOLI NUOVI + TEMPLATE (il grosso)
- B1 (writer CH9), B2 (writer CH10): capitoli nuovi da contratto §1 righe
  J/K, template completo §2.3 (con §6 STORIA e §7 POSIZIONAMENTO nativi).
- B3 (writer CH1+CH3): §1.7 licensing + EAP + G3 + caveat/cross-ref;
  B4 (writer CH4): §1.6 engine-speed + §7 strumenti (la più carica di
  registry-refs); B5 (writer CH5+CH6): tutte le righe MAJOR/MINOR di
  colonna N(v)/L(v)/O(v); B6 (writer CH8): §1.7 M1-M5 + §3.5; B7 (writer
  CH2+CH7): §7 POSIZIONAMENTO (adjoint; swirl/Tillyaeva).
- B8 (historian): le sezioni §6 STORIA di TUTTI i capitoli in un solo
  passaggio (un agente solo: la STORIA richiede la vista trasversale
  M0/PROGRESS/ledger; consegna per-capitolo ai file).
- Vincolo per ogni writer: ogni ref = id del registry; ogni claim
  "il campo non fa X" = search-proven con query citata (grep/QUERY nel
  testo); classi di rigore dichiarate.
- Peso: 8 agenti × 1 round (+ risposte puntuali), ~500-700k token.

### Onda W-C — REFUTAZIONE (simmetrica alla costruzione)
- C1-C3 (refuter): REFUTE_CH9, REFUTE_CH10, REFUTE delle sezioni nuove nei
  capitoli estesi (un refuter per gruppo di estensioni, campione 100% delle
  righe load-bearing). C4 (refuter): mini-pass sulle righe [W2-*] di CH1-CH6
  (critic 21). C5 (refuter dedicato §6/§7): cammina le STORIE (ancora per
  ancora) e i POSIZIONAMENTI (ogni id citato esiste nel registry ed è
  pertinente — anti-cita-a-vanvera).
- Disposizione findings nella STESSA onda (tabelle per capitolo).
- Peso: 5 agenti × 1-2 round, ~250-400k token.

### Onda W-D — LINT + PROMOZIONE
- D1 (lint, script o agente con grep in finestra — NIENTE installazioni):
  i tre lint di completamento (sotto). D2 (orchestratore): CH-REF compilato
  DALL'esito del lint (mappa id→capitolo = il sottoprodotto del lint 1);
  promozione a docs/atlas/ con commit per pathspec espliciti; log R3 con
  shape/round/token per onda.
- Peso: 1-2 agenti, ~80-120k token.

Totale stimato: ~0.95-1.4M token, 4 onde, 17 slot agente (Fable ovunque —
memoria model-pinned).

### Criteri di completamento (i lint — la mappa si dichiara completa quando)
1. **Lint-registri**: ogni id dei registri di programma (claims/choice/flag/
   findings citati nei capitoli) → puntatore a capitolo in CH-REF, o riga
   FUORI-PERIMETRO con ragione; comando misurato in finestra, mai ereditato
   (SR-12).
2. **Lint-manifest**: ogni riga di FILE_MANIFEST.csv → disposizione (usata
   in capitolo / dichiarata non-portante); zero righe orfane.
3. **Lint-matrice**: ogni cella di §1 → COPERTA (puntatore che ESISTE, grep
   dell'anchor) o FUORI-PERIMETRO dichiarata; le 30 SCOPERTE devono risultare
   0 a fine W-C.
4. **Lint-critic**: 21/21 righe con disposizione ESEGUITA (BLOCKING risolte,
   MAJOR con riga-capitolo o declinazione a registro, MINOR almeno triage
   nel log) — il verdetto del critic si ribalta a COMPLETA solo qui.
5. **Lint-template**: ogni capitolo CH1-CH10 porta le 8 sezioni del template
   (CH-REF escluso); ogni §7 cita >= 1 id di registry per strumento usato
   nel capitolo; ogni §6 ha le tre battute con ancore.

Falsificatore del design stesso: se in W-B un writer trova un aspetto del
perimetro senza riga di matrice, la matrice è FALSIFICATA — si ferma l'onda,
si emenda §1 a registro, e il lint-matrice riparte (la matrice è un claim,
non una premessa — disciplina doubts-to-convergence).
