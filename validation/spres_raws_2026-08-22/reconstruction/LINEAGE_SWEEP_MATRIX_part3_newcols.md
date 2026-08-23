# LINEAGE_SWEEP_MATRIX — part 3 NEW COLUMNS (slot L3, onda W-B.0 LINEAGE-SWEEP, S-PRES session 2)

**NOTA DI DRIFT [C6-REPAIR 2026-08-23]**: le ancore "CHn:righe" di
questo file sono state stampate PRIMA della riscrittura dei CH1-CH10 da
parte dell'onda W-B.1 (mtime 08:33-08:44) e NON sono più affidabili
come numeri di riga (probe misurati: REFUTE_LINEAGE.md F-6 — es.
CH4:238-240 per Masters ora punta a contenuto thermo; il contenuto
Masters sta a CH4:255 allo stato attuale). Il join downstream usa LL-id
e i § dei CH, MAI numeri di riga CH. Le ancore non-CH
(registry/findings/M0/LM/report/PDF) sono verificate sane da C6.

Data: 2026-08-23. Mini-pass MIRATO post-GV-1: il check GV-1 (part1) ha
falsificato l'asse a 15 componenti (finding F-des-1) — questo file rende
le **5 componenti NUOVE** su TUTTO il corpus (82 id, celle obbligatorie).

**Stadio di confronto** (artifact-connectedness): {5 componenti nuove
N-16..N-20, definizioni verbatim dalla sezione GV-1 di part1 + flag
"parametrizzazione del design" di part2} × {gli stessi 82 id delle parti
1-2}. Innesco: GV-1/F-des-1 (31 nodi della pipeline map senza componente
sull'asse C-1ter). Base di ogni cella: PRIMA gli indizi già resi nei
blocchi-paper delle parti 1-2 (i paper sono GIÀ stati ri-interrogati lì),
POI le righe registry. Comandi/letture misurati in questa finestra
(SR-12):
- `Read validation/spres_raws_2026-08-22/reconstruction/LINEAGE_SWEEP_MATRIX_part1.md` (integrale);
- `Read .../LINEAGE_SWEEP_MATRIX_part2.md` (integrale);
- `Read docs/literature_registry.yaml` righe :100-495 e :495-1075
  (tutte le righe degli 82 id).
- **DEEP-CHECK su PDF: NESSUNO** — ogni cella candidata delle 5 colonne
  si chiude dal record (parti 1-2 + registry); nessuna apertura mirata
  necessaria (context-discipline). NIENTE procurement/installazioni.
- **Colonne [REP]-bounded: NESSUNA** — tutti gli 82 id hanno path su
  disco nel registry; i 5 id `wanted_*` del corpus (breitkopf_ulbrich,
  becker_rannacher_2001, fidkowski_darmofal_2011, hicken_zingg_2014,
  thakur_nadarajah_2024) sono ARRIVATI (paths + READ-PARTIAL di record,
  registry :754-761, :862-868, :876-882, :920-926, :928-934): le loro
  celle poggiano sul record alla profondità di lettura dichiarata.

**Arco di consumo**: merge dell'orchestratore (part1+part2+part3) →
LINEAGE_LEDGER → §3-bis ANTENATI DIRETTI dei writer W-B.1 + storyboard.
Il refuter C6 attacca: le celle VUOTE (assenza dichiarata, falsificabile
sul record citato), le celle PIENE (isomorfismo sovra-letto), la
DEMARCAZIONE N-16/N-20 aggiudicata sotto, e l'esito C55.

**Le 5 componenti nuove (asse-righe di questo pass)**:
- **N-16 design chart** (C1-C8 → qui C2-C8, vedi demarcazione): il chart
  come oggetto di GOVERNANCE dello spazio di design — BC (C2), knot
  law + insertion guard (C3-C6), dof ratchet (C7), warm start (C8).
- **N-17 optimizer engine** (i 17 nodi: C16, C27, C29-C37, C40, C44,
  C48, C57, C60 + SDP-CAND-8 parziale): TR-Newton segmentato a
  curvatura misurata, NAND/SAND, exploration tier, passi FD, quadratura.
- **N-18 thermo tabulated backend** (C24-C26): chiusura termodinamica a
  tabelle, separazione generatore/interfaccia (direttiva S11).
- **N-19 external referee / evidence tier** (R22-CFD, D-44, P34):
  referee esterno, gate dei claim pubblici, gerarchia staged di evidenza.
- **N-20 parametrizzazione del design** (spline/level-set/CAD-based;
  seed: masters_etal_2017, lauer_ansell_2025_pas): la SCELTA della
  rappresentazione geometrica (basis C1).

**DEMARCAZIONE N-16/N-20 (aggiudicata in questo pass, attaccabile da
C6)**: la GV-1 di part1 metteva "basis spline" dentro N-16; il flag di
part2 e il brief orchestratore istituiscono N-20 come colonna separata.
Per evitare doppio conteggio: **C1 (basis/rappresentazione) → N-20;
C2-C8 (governance del chart) → N-16**. Un paper che parametrizza la
geometria compila N-20; compila N-16 solo se mostra struttura di
chart/budget/continuazione.

**NOTA DI RI-HOMING (valore del pass)**: le celle (11) di part2 per
byrd_hribar_nocedal_1999, nocedal_wright_2006_2ed, vanaret_leyffer_2026_uno,
vanaret_montoison_2026_joss contenevano materiale ENGINE parcheggiato
nella colonna adjoint per mancanza dell'asse: qui trovano la colonna
propria (N-17). Le celle (11) di part2 restano valide come cross-ref.

**Regola di cella**: ≤3 righe, "procedura isomorfa/antenata? come la
chiamano? cosa le manca vs noi". Ogni cella resa: compilata o
"checked: none".

**Conteggio**: celle totali 5×82 = 410; PIENE = 35 (N-16: 4, N-17: 12,
N-18: 6, N-19: 7, N-20: 6); "checked: none" = 375 [C6-REPAIR: era
33/377; +2 = P-B e P-C su N-19, C6-FILL dal campione celle-vuote].

---

## N-16 — DESIGN CHART (governance dello spazio di design, C2-C8)

### Celle piene (4)
- **allman_hoffman_1981**: principio dof-budget ante litteram — il
  metodo diretto a POCHI dof prezza la perdita vs indiretto (≤0.2%/0.66%,
  registry :388-394; litmap sec.3.9); manca: knot law, insertion guard,
  ratchet dinamico, warm start.
- **hoffman_1987_ctp**: enumerazione a GRIGLIA della famiglia CTP
  (construction + grid enumeration, registry :561-568) = design chart
  pubblicato della pratica; chart di CONSULTAZIONE, non di
  ottimizzazione: manca base formale, guardie, continuazione.
- **nasa_rp1104_1983**: curve books di troncamento = design chart
  ISTITUZIONALE a consultazione grafica (registry :444-450); manca
  parametrizzazione formale, ottimalità, ogni governance.
- **masters_etal_2017**: prior QUANTITATIVO 20-25 dof per copertura
  dello spazio di design (registry :1023-1029, CH4:238-240) = antenato
  del prior del dof ratchet (C7); claim in attesa di verifica full-text
  (owner di registry); manca ratchet dinamico, insertion guard, warm
  start.

### checked: none (78)
kraiko_osipov_1970, shmyglevskii_1980, giles_ulbrich_2010_part1,
giles_ulbrich_2010_part2, lozano_ponsin_2025, gonzalez_viana_2025,
sternin_1961, lozano_2018, lozano_2019, morris_2005, owens_hanson_2007,
moretti_2002, cooper_shepherd_2008, ancourt_peter_atinault_2023,
wolanski_2013, kaemming_paxson_2018, paxson_miki_2022,
wintenberger_shepherd_2004, harroun_2021, wintenberger_shepherd_2006_fj,
browne_shepherd_sdtoolbox_2018, shepherd_kasahara_2017, stechmann_2019,
rao_1958, rao_1961_review, rao_1961_spike, migdal_1972,
humphreys_thompson_hoffman_1971, hoffman_1967, scofield_hoffman_1971,
rao_beck_1994, rao_beck_booth_1999, hoffman_scofield_thompson_1972,
johnson_thompson_hoffman_1974, vander_veen_1974, onofri_2002_plug_survey,
nasa_sp8120_1976, johnson_boney_1975, zucrow_hoffman_1977_vol2,
tesi_viviano_2023, thesis_valeriani_2019, kraiko_tillyaeva_2015,
giles_pierce_2001, giles_pierce_2000, kraiko_2001_plug,
kraiko_2016_two_sided (chart a punti di controllo = contenuto
RAPPRESENTAZIONE → reso in N-20; 9 dof FISSI, zero governance),
efremov_kraiko_2004_augmentor, sun_2019, fernandes_2023, rubino_2018,
zahr_persson_2016, schotthofer_2024, janc_2025, liu_2022, ornano_2017,
harroun_2020, miki_2020, teasley_2023, teasley_2025,
li_xu_lv_lv_song_2023, li_xu_lv_yu_zhou_2025, jourdaine_2019,
wanted_breitkopf_ulbrich, wanted_becker_rannacher_2001,
wanted_fidkowski_darmofal_2011, wanted_hicken_zingg_2014,
wanted_thakur_nadarajah_2024, byrd_hribar_nocedal_1999,
nocedal_wright_2006_2ed, giles_pierce_1997, venditti_darmofal_2000,
huang_zahr_2022, huang_zahr_2023_companion, lauer_ansell_2025_pas,
deuflhard_2011_csm35, yamamoto_1986_numermath48,
vanaret_leyffer_2026_uno, vanaret_montoison_2026_joss.

---

## N-17 — OPTIMIZER ENGINE (driver, 17 nodi)

Verdetto GV-1 di part1 CONFERMATO con precisazione: nessun antenato del
DRIVER nostro (TR-Newton segmentato a curvatura misurata, NAND/SAND
adjudicato, exploration tier) esiste nel corpus; esistono però (a) i
PARENT algoritmici moderni dell'engine adottato, (b) le istanze
direct-search del dominio ugelli — entrambi resi qui.

### Celle piene (12)
- **ancourt_peter_atinault_2023**: App. C steepest descent su ugello
  6-bump (registry :214-223) = engine gradiente elementare accoppiato
  all'adjoint; manca TR-Newton, vincoli, certificazione del passo.
- **thesis_valeriani_2019**: PSO/fminsearch = istanze direct-method del
  dominio (registry :484-490); manca gradiente adjoint e ogni driver
  strutturato.
- **kraiko_2016_two_sided**: RANS+GA, "zero optimality equations"
  (registry :534-541) = direct search nella scuola classica stessa; la
  LORO tabella: exact-theory (2.45%) batte tutti i GA (2.90-3.68%) —
  dato PRO condizioni di ottimalità; manca gradiente, certificati.
- **fernandes_2023**: fmincon/NSGA-II generici attorno al MoC-simulatore
  (registry :570-577); manca adjoint, condizioni, e C17 mostra argmax
  NON-IDENTIFIABILITY su obiettivo flat (findings :1994).
- **ornano_2017**: optimizer presente su obiettivo time-averaged a tre
  stadi (registry :624-631); engine non censito nel record; delta 2%
  dell'ordine della propria stopping tolerance (C16, findings :1994).
- **allman_hoffman_1981**: il metodo DIRETTO guida i parametri con una
  ricerca numerica (registry :388-394); algoritmo storico non censito
  nel record; manca driver a curvatura misurata e certificazione.
- **byrd_hribar_nocedal_1999**: PARENT ALGORITMICO dell'engine di record
  (tr_interior_point; barrier update + semantica moltiplicatori,
  registry :971-978, findings :1239) — cella ri-homed dalla (11) di
  part2; manca la verifica [P-IPADJ] contro l'algoritmo pubblicato.
- **nocedal_wright_2006_2ed**: canone dell'engine — §6.2 SR1 (curvatura
  quasi-Newton), 15.3 variable elimination (multiplier provenance),
  §8.1 modello d'errore FD = l'antenato pubblicato dei passi FD C44
  (registry :980-987, findings :1371); bande derivate, non asserite.
- **vanaret_leyffer_2026_uno**: Uno = solver NLP unificato, IL flip
  candidate arm-B dell'engine A/B (registry :1055-1062; CH4:206-213);
  manca (lato nostro) la guardia IDENTICAL-CERTIFIED-OUTCOMES prima di
  ogni adozione; install = decisione O5-class.
- **vanaret_montoison_2026_joss**: identità software di Uno (JOSS,
  paper distinto; registry :1064-1070) — alimenta la stessa card C31.
- **wanted_thakur_nadarajah_2024**: full-space mesh optimization =
  engine e rappresentazione FUSI dentro il tracking goal-oriented
  (registry :928-934; CH4:180-183) — steelman moderno, non antenato;
  manca separazione stato/design e driver segmentato.
- **deuflhard_2011_csm35**: NLEQ-RES/NLEQ-ERR affine-invariant = canone
  degli ALGORITMI Newton adattivi (registry :1039-1045); il contenuto
  soglie resta nella cella (12) di part2 (C20); manca segmentazione TR
  a curvatura misurata, NAND/SAND, exploration tier.

### checked: none (70)
kraiko_osipov_1970, shmyglevskii_1980 (condizioni chiuse, come tutti i
classici russi), giles_ulbrich_2010_part1, giles_ulbrich_2010_part2,
lozano_ponsin_2025, gonzalez_viana_2025 (design per sweep CFD, NO
optimizer — assenza già resa in (2) part1), sternin_1961, lozano_2018,
lozano_2019, morris_2005, owens_hanson_2007, moretti_2002,
cooper_shepherd_2008, wolanski_2013, kaemming_paxson_2018,
paxson_miki_2022 (OFAT, NO optimizer di record), wintenberger_shepherd_2004,
harroun_2021, wintenberger_shepherd_2006_fj, browne_shepherd_sdtoolbox_2018,
shepherd_kasahara_2017, stechmann_2019 (ottimizzazione 0-D replicata
18/18 ma engine non censito nel record: cella non compilabile senza
deep-check, non candidata — il contenuto lineage vive in (1)/(2)/(8)),
rao_1958, rao_1961_review, rao_1961_spike, migdal_1972,
humphreys_thompson_hoffman_1971, hoffman_1967, scofield_hoffman_1971,
rao_beck_1994, rao_beck_booth_1999, hoffman_scofield_thompson_1972,
johnson_thompson_hoffman_1974, vander_veen_1974, onofri_2002_plug_survey,
nasa_rp1104_1983, nasa_sp8120_1976, johnson_boney_1975,
zucrow_hoffman_1977_vol2, tesi_viviano_2023, kraiko_tillyaeva_2015
(adjoint mixed-type risolto numericamente ma NESSUN optimizer:
condizioni chiuse), giles_pierce_2001, giles_pierce_2000,
kraiko_2001_plug, efremov_kraiko_2004_augmentor, sun_2019,
hoffman_1987_ctp, rubino_2018 (shape-opt adjoint HB ma engine non
censito nel record), zahr_persson_2016 (idem: gradienti adjoint su
manifold periodico, engine non censito), schotthofer_2024, janc_2025
(abilita engine a gradiente, ma il contenuto è adjoint: resta in (11)),
liu_2022 (NO optimizer di record, C4), harroun_2020, miki_2020,
teasley_2023, teasley_2025, li_xu_lv_lv_song_2023,
li_xu_lv_yu_zhou_2025, jourdaine_2019, wanted_breitkopf_ulbrich,
wanted_becker_rannacher_2001, wanted_fidkowski_darmofal_2011,
wanted_hicken_zingg_2014, giles_pierce_1997, venditti_darmofal_2000,
huang_zahr_2022 (linea full-space resa sulla cella thakur; per questo
id il record dà solo il metodo di tracking), huang_zahr_2023_companion,
masters_etal_2017, lauer_ansell_2025_pas, yamamoto_1986_numermath48
(solo bound d'errore: resta in (12)).

---

## N-18 — THERMO TABULATED BACKEND (C24-C26)

### Celle piene (6)
- **johnson_boney_1975**: ANTENATO CLASSICO DIRETTO — MoC real-gas
  TABULATO a exit uniforme ([DIR-THERMOTAB] di record, registry
  :460-466); gamma-sensitivity ~80x sul length ratio = exhibit del
  perché la chiusura conta; manca separazione generatore/interfaccia e
  contratto tabelle.
- **scofield_hoffman_1971**: precedente tabular-EOS dentro il
  variazionale noneq (registry :380-386, nota part1) — l'altro antenato
  nominato di [DIR-THERMOTAB]; manca la pipeline C24-C26 e il contratto.
- **browne_shepherd_sdtoolbox_2018**: lato GENERATORE degli stati (CJ
  equilibrium-Hugoniot, PostShock frozen, zndsolve; registry :300-307)
  = esattamente il ruolo "generators free" della direttiva S11; manca
  l'interfaccia a tabelle come contratto.
- **hoffman_1967**: chimica reagente IN-THE-LOOP lungo le
  caratteristiche (registry :372-378) = il ramo ALTERNATIVO (non
  tabulato) che C24-C26 aggiudica contro; manca ogni tabellazione.
- **sun_2019**: chiusura di stato ri-basata su gamma(T) thermally
  perfect (registry :552-559) = la mossa "construction with variable
  closure" senza backend; manca tabellazione, separazione
  generatore/interfaccia, e le condizioni (C14, findings :1994).
- **janc_2025**: solver reagente finite-rate DIFFERENZIABILE (registry
  :606-613) = il ramo non-tabulato reso AD-compatibile (threat vector
  nominato); manca l'interfaccia a tabelle backend-1 — il confronto
  vivrà sulla coppia costo/certificabilità.

### checked: none (76)
kraiko_osipov_1970, shmyglevskii_1980, giles_ulbrich_2010_part1,
giles_ulbrich_2010_part2, lozano_ponsin_2025, gonzalez_viana_2025,
sternin_1961, lozano_2018, lozano_2019, morris_2005 (finite-rate FV ma
nessun backend a tabelle di record), owens_hanson_2007, moretti_2002,
cooper_shepherd_2008, ancourt_peter_atinault_2023, wolanski_2013,
kaemming_paxson_2018, paxson_miki_2022, wintenberger_shepherd_2004,
harroun_2021, wintenberger_shepherd_2006_fj, shepherd_kasahara_2017,
stechmann_2019, rao_1958, rao_1961_review, rao_1961_spike, migdal_1972,
humphreys_thompson_hoffman_1971, allman_hoffman_1981, rao_beck_1994,
rao_beck_booth_1999 (frozen/eq chemistry ma nessuna tabulazione di
record), hoffman_scofield_thompson_1972, johnson_thompson_hoffman_1974,
vander_veen_1974, onofri_2002_plug_survey, nasa_rp1104_1983,
nasa_sp8120_1976, zucrow_hoffman_1977_vol2, tesi_viviano_2023,
thesis_valeriani_2019 (plug fuori perfect-gas: chiusura variabile ma
nessuna evidenza-tabella nel record — non compilata, dichiarato),
kraiko_tillyaeva_2015, giles_pierce_2001, giles_pierce_2000,
kraiko_2001_plug, kraiko_2016_two_sided, efremov_kraiko_2004_augmentor,
hoffman_1987_ctp, fernandes_2023 (gamma=1.4 dichiarato), rubino_2018,
zahr_persson_2016, schotthofer_2024, liu_2022, ornano_2017,
harroun_2020, miki_2020, teasley_2023, teasley_2025,
li_xu_lv_lv_song_2023, li_xu_lv_yu_zhou_2025, jourdaine_2019,
wanted_breitkopf_ulbrich, wanted_becker_rannacher_2001,
wanted_fidkowski_darmofal_2011, wanted_hicken_zingg_2014,
wanted_thakur_nadarajah_2024, byrd_hribar_nocedal_1999,
nocedal_wright_2006_2ed, giles_pierce_1997, venditti_darmofal_2000,
huang_zahr_2022, huang_zahr_2023_companion, masters_etal_2017,
lauer_ansell_2025_pas, deuflhard_2011_csm35, yamamoto_1986_numermath48,
vanaret_leyffer_2026_uno, vanaret_montoison_2026_joss.

---

## N-19 — EXTERNAL REFEREE / EVIDENCE TIER (R22-CFD, D-44, P34)

Verdetto GV-1 di part1 CONFERMATO NELLA SOSTANZA: nessun antenato
PROCEDURALE (tier dichiarato, gate sui claim, referee pre-registrato)
esiste nel corpus (CT-3). Le 5 celle sotto sono ISTANZE/DATUM di
refereeing ad-hoc — evidenza PRO la necessità del tier, mai la
procedura; framing dichiarato per non contraddire CT-3.

### Celle piene (7) [C6-REPAIR: era 5; +P-B, +P-C]
- **harroun_2021**: coppia CFD+esperimento in cui l'esperimento SEPARA i
  due aerospike che il C_F medio non separa (1.25 flat; registry
  :273-285) = il discriminating-failure datum — referee ad-hoc che
  smaschera la cecità del modello; manca tier/gate formale (istanza,
  non procedura: coerente con CT-3).
- **harroun_2020**: paper di VALIDAZIONE sperimentale delle simulazioni
  d'ugello (registry :633-640) = pratica referee ad-hoc del filone;
  manca gerarchia di evidenza dichiarata (P34) e gate dei claim (D-44);
  la figura "+1% flared" è essa stessa second-hand (lezione provenance).
- **ornano_2017**: pipeline a TRE stadi di fedeltà crescente (steady
  DoE → averaged URANS → reactive DDT; registry :624-631) = gerarchia
  staged IMPLICITA, l'analogo più vicino di P34; manca tier dichiarato,
  gate, e il delta finale è ~stopping tolerance.
- **sun_2019**: CFD + UN hot-fire test (registry :552-559) = check
  esterno puntuale a valle del design; manca ogni gerarchia e la
  motivazione teorica è già falsificata dal record (C14).
- **cooper_shepherd_2008**: esperimento vs predizione del modello
  average-state (+43% a 1.4 kPa, registry :202-208) = confronto
  modello-esperimento puntuale in cui l'esperimento arbitra il regime;
  manca struttura di tier e falsificatori pre-registrati.
- **li_xu_lv_lv_song_2023 (P-B)** [C6-FILL, dal campione celle-vuote
  del refuter]: il CFD TRANSIENT arbitra il design fatto sullo stato
  steady mediato — Fig. 15 flat-vs-peaked (la media globale non VEDE
  l'ottimo, cliff −5.78% a 80%; registry :683-688) = referee ad-hoc
  interno, stessa classe-istanza di harroun_2021; manca tier/gate
  formale (istanza, non procedura: CT-3 conservato).
- **li_xu_lv_yu_zhou_2025 (P-C)** [C6-FILL]: coppie PAIRED
  transient-vs-steady-mediato con flip a metà ranking e argmax HELD
  (registry :690-695) = protocollo referee ad-hoc dell'adeguatezza
  della media; manca gerarchia di evidenza dichiarata e falsificatori
  pre-registrati.

### checked: none (75) [C6-REPAIR: era 77; P-B e P-C spostate in piene]
kraiko_osipov_1970, shmyglevskii_1980, giles_ulbrich_2010_part1,
giles_ulbrich_2010_part2, lozano_ponsin_2025, gonzalez_viana_2025,
sternin_1961, lozano_2018, lozano_2019, morris_2005, owens_hanson_2007,
moretti_2002, ancourt_peter_atinault_2023 (residui ACE = code
verification INTERNA → resta in (12)), wolanski_2013,
kaemming_paxson_2018, paxson_miki_2022, wintenberger_shepherd_2004,
wintenberger_shepherd_2006_fj, browne_shepherd_sdtoolbox_2018,
shepherd_kasahara_2017, stechmann_2019, rao_1958, rao_1961_review,
rao_1961_spike, migdal_1972, humphreys_thompson_hoffman_1971 (il
34,373/34,375 è insensibilità alla start-line, contratto (5) — NON
cross-code refereeing: valutato e lasciato none), hoffman_1967,
scofield_hoffman_1971, allman_hoffman_1981, rao_beck_1994,
rao_beck_booth_1999, hoffman_scofield_thompson_1972,
johnson_thompson_hoffman_1974, vander_veen_1974, onofri_2002_plug_survey,
nasa_rp1104_1983, nasa_sp8120_1976, johnson_boney_1975,
zucrow_hoffman_1977_vol2, tesi_viviano_2023, thesis_valeriani_2019,
kraiko_tillyaeva_2015, giles_pierce_2001, giles_pierce_2000,
kraiko_2001_plug, kraiko_2016_two_sided, efremov_kraiko_2004_augmentor,
hoffman_1987_ctp, fernandes_2023, rubino_2018, zahr_persson_2016,
schotthofer_2024, janc_2025, liu_2022 (A-L6: choking ASSERITO senza
verifica = l'anti-referee, già reso in (15) part2), harroun_2021 → vedi
sopra, miki_2020, teasley_2023, teasley_2025 [C6-REPAIR: P-B e P-C
rimosse da questa lista, celle riempite sopra], jourdaine_2019,
wanted_breitkopf_ulbrich,
wanted_becker_rannacher_2001, wanted_fidkowski_darmofal_2011 (stima
d'errore output-based = estimator INTERNO → resta in (12)),
wanted_hicken_zingg_2014, wanted_thakur_nadarajah_2024,
byrd_hribar_nocedal_1999, nocedal_wright_2006_2ed, giles_pierce_1997,
venditti_darmofal_2000, huang_zahr_2022, huang_zahr_2023_companion,
masters_etal_2017, lauer_ansell_2025_pas, deuflhard_2011_csm35,
yamamoto_1986_numermath48, vanaret_leyffer_2026_uno,
vanaret_montoison_2026_joss.
[Nota contabile: harroun_2021 elencato per leggibilità del punto-CT-3 —
la sua cella è PIENA; il conteggio none di questa colonna è 75
(post-C6; era 77).]

---

## N-20 — PARAMETRIZZAZIONE DEL DESIGN (basis C1: spline/Bezier/FFD/CST/CAD)

### Celle piene (6)
- **masters_etal_2017** [seed]: IL censimento geometrico delle
  parametrizzazioni di profilo (CST, B-spline, Hicks-Henne, ...; prior
  20-25 dof; registry :1023-1029, CH4:238-240) — lo chiamano "shape
  parameterization methods"; manca il trasferimento a contorni d'ugello
  sotto vincoli MoC (scope di trasferimento dichiarato nel ledger C1).
- **lauer_ansell_2025_pas** [seed]: review PAS 2025 = layer MODERNO del
  censimento C1 (registry :1031-1037); manca l'adjudicazione per la
  nostra classe (contorni con gola, vincoli caratteristici, fitted
  front).
- **kraiko_2016_two_sided**: chart Bezier a 9 punti di controllo nella
  scuola classica STESSA (C1REP cross-ref, registry :534-541) — usato
  per direct optimization; manca legge di knots/ratchet e l'esito
  interno li smentisce (exact-theory batte i GA).
- **fernandes_2023**: FFD (free-form deformation) attorno al
  MoC-simulatore (registry :570-577) — la parametrizzazione
  dell'occupante più vicino della nicchia; planar, senza condizioni;
  manca basis adjudicata e guardie di identificabilità (C17).
- **allman_hoffman_1981**: contorno PARAMETRIZZATO a pochi dof del
  metodo diretto (registry :388-394) = antenato classico della
  rappresentazione-per-ottimizzazione; basis storica non censita nel
  record; manca adjudicazione formale e certificati.
- **teasley_2025**: l'ugello ridotto a sweep di 4 SCALARI di manifattura
  (registry :661-668) = parametrizzazione degenere del campo RDE — gap
  witness della colonna; manca base geometrica ricca e ogni
  adjudicazione.

### checked: none (76)
kraiko_osipov_1970, shmyglevskii_1980, giles_ulbrich_2010_part1,
giles_ulbrich_2010_part2, lozano_ponsin_2025, gonzalez_viana_2025
(sweep 1-dof di area ratio: non è una basis), sternin_1961, lozano_2018,
lozano_2019, morris_2005, owens_hanson_2007, moretti_2002,
cooper_shepherd_2008, ancourt_peter_atinault_2023 (6-bump = test case,
non adjudicazione di basis), wolanski_2013, kaemming_paxson_2018,
paxson_miki_2022, wintenberger_shepherd_2004, harroun_2021,
wintenberger_shepherd_2006_fj, browne_shepherd_sdtoolbox_2018,
shepherd_kasahara_2017, stechmann_2019, rao_1958 (il contorno è
COSTRUITO dalle condizioni, mai parametrizzato — è il punto della
scuola indiretta), rao_1961_review, rao_1961_spike, migdal_1972,
humphreys_thompson_hoffman_1971, hoffman_1967, scofield_hoffman_1971,
rao_beck_1994, rao_beck_booth_1999, hoffman_scofield_thompson_1972,
johnson_thompson_hoffman_1974, vander_veen_1974, onofri_2002_plug_survey,
nasa_rp1104_1983, nasa_sp8120_1976, johnson_boney_1975,
zucrow_hoffman_1977_vol2, tesi_viviano_2023, thesis_valeriani_2019,
kraiko_tillyaeva_2015, giles_pierce_2001, giles_pierce_2000,
kraiko_2001_plug, efremov_kraiko_2004_augmentor, sun_2019,
hoffman_1987_ctp (la famiglia CTP è una COSTRUZIONE enumerata → resa in
N-16), rubino_2018, zahr_persson_2016, schotthofer_2024, janc_2025,
liu_2022 (4 geometrie disegnate a mano = assenza dichiarata),
ornano_2017 (parametrizzazione non censita nel record), harroun_2020,
miki_2020 (6 geometrie hand-designed = assenza dichiarata),
teasley_2023, li_xu_lv_lv_song_2023, li_xu_lv_yu_zhou_2025,
jourdaine_2019 (conico 50 deg esplicitamente non-ottimizzato),
wanted_breitkopf_ulbrich, wanted_becker_rannacher_2001,
wanted_fidkowski_darmofal_2011, wanted_hicken_zingg_2014,
wanted_thakur_nadarajah_2024 (parametrizza la MESH/il fronte, non il
design: valutato e lasciato none), byrd_hribar_nocedal_1999,
nocedal_wright_2006_2ed, giles_pierce_1997, venditti_darmofal_2000,
huang_zahr_2022, huang_zahr_2023_companion (parametrizza gli SHOCK nel
tracking, non la geometria di design: valutato e lasciato none),
deuflhard_2011_csm35, yamamoto_1986_numermath48,
vanaret_leyffer_2026_uno, vanaret_montoison_2026_joss.

---

## COLONNA EXTRA FIEVISOHN (fuori dagli 82, ereditata dal duty W-09 di part2)

Per completezza del merge: le 5 componenti nuove sulla colonna Fievisohn
(Yu 2017 JPP + PhD UMD 2016, on-disk in Downloads; nozzled AIAA
2018-0881 assente) = **checked: none su tutte e 5** dal record [IO] di
part2 (valutazione a convergenza, solver-not-designer: nessun chart,
nessun optimizer, nessuna tabella-EOS di record, nessun tier di
evidenza, nessuna parametrizzazione di design — le geometrie sono date).
Nessuna ri-lettura PDF necessaria.

---

## SEZIONE CAVEAT C55 (duty a)

**ESITO: RISOLTO — C55 resta mappato a (8) mu measure, come sotto-asse
DICHIARATO "misura sull'insieme operativo (P_amb)"; l'opzione di part1
"quinta candidata riga N-20 operating-envelope aggregation" è DECADUTA
perché l'id N-20 è ora occupato dalla parametrizzazione del design
(flag part2, brief orchestratore).**

**VINCOLO DI CONSUMO [C6, adjudicato REFUTE_LINEAGE §5]**: la
sotto-etichetta "misura sull'inviluppo operativo (P_amb)" viaggia CON
C55 in OGNI consumo downstream (§3-bis, storyboard, deck, Q&A): una
cella o claim (8) su C55 consumati SENZA sotto-etichetta re-innescano
l'escalation N-21 (mai riuso di N-20). Dichiarato inoltre [C6]: il flag
part2 "parametrizzazione del design" è assorbito da **N-20+N-16
CONGIUNTAMENTE** (censimento basis → N-20; dof-budget/prior 20-25 →
N-16 — le celle masters/lauer vivono in entrambe), non da N-20 sola.

Ragioni (3, dichiarate):
1. **Demarcazione nominata, non conflazione muta**: misura di FASE
   (dentro il ciclo, quadratura su Xi = C62) vs misura d'INVILUPPO (su
   P_amb = C55) sono due assi distinti; la mappatura a (8) vale SOLO
   con la sotto-etichetta, che questo file rende di record.
2. **Popolamento**: l'unico antenato-corpus dell'aggregazione
   d'inviluppo è giles_pierce_2000 (multipoint J=Σw_i·F, Reuther), GIÀ
   reso nelle celle (2)/(8) di part2 con il caveat R11 (pesi mai
   stampati); una colonna dedicata avrebbe ≤2 celle piene su 82 —
   valvola load-class (sufficient-not-optimized, ratifica AG-1
   2026-08-20).
3. **Escalation nominata per C6**: se il refuter giudica la
   sotto-etichetta insufficiente (conflazione over-read), la riparazione
   di record è una NUOVA riga **N-21 "operating-envelope aggregation"**
   — MAI il riuso dell'id N-20. Non dichiaro CONTESO: la decisione è
   presa, l'attacco resta possibile sulla riga qui sopra.

---

## CANDIDATE RIGHE LEDGER — 5 COLONNE NUOVE (antenato → cosa fa → cosa gli manca vs noi)

1. **Hoffman 1987 CTP + NASA RP-1104 → N-16**: design chart pubblicati
   della pratica (enumerazione a griglia CTP; curve books di
   troncamento) → manca il chart come oggetto di GOVERNANCE (knot law
   C3-C6, insertion guard, dof ratchet C7, warm start C8) e ogni
   ottimalità. Ancora: registry :561-568, :444-450.
2. **Allman-Hoffman 1981 → N-16+N-20 (+N-17)**: metodo diretto su
   contorno parametrizzato a pochi dof, prezzo MISURATO vs indiretto
   (≤0.2%/0.66%) → manca adjudicazione della basis, governance del
   chart, driver a curvatura misurata, certificati. Ancora: registry
   :388-394; litmap sec.3.9.
3. **Masters 2017 + Lauer-Ansell 2025 → N-20 (+N-16)**: censimento
   geometrico delle parametrizzazioni + prior 20-25 dof (layer moderno
   PAS 2025) → manca il trasferimento a contorni d'ugello sotto vincoli
   MoC (scope dichiarato); il prior alimenta il dof ratchet. Ancora:
   registry :1023-1037; CH4:238-240.
4. **Kraiko 2016 → N-20 (+N-17)**: chart Bezier a 9 punti di controllo
   usato per direct optimization (RANS+GA) NELLA scuola classica; la
   loro tabella: exact-theory batte tutti i GA → manca (per scelta)
   ogni condizione di ottimalità e certificazione — dato PRO la nostra
   rotta. Ancora: registry :534-541.
5. **Byrd-Hribar-Nocedal 1999 + Nocedal-Wright 2006 → N-17**: parent
   algoritmico dell'engine di record (tr_interior_point; SR1; modello
   d'errore FD per i passi C44) → manca semantica dei moltiplicatori
   repo-verified ([P-IPADJ]) e la segmentazione TR a curvatura
   misurata. Ancora: registry :971-987; findings :1239, :1371.
6. **Uno (Vanaret-Leyffer MPC 2026 + JOSS) → N-17**: solver NLP
   unificato = flip candidate arm-B → manca la guardia
   IDENTICAL-CERTIFIED-OUTCOMES e la decisione O5-class di install
   prima di ogni adozione. Ancora: registry :1055-1070; CH4:206-213.
7. **Linea direct-search del dominio (Kraiko-2016 GA; Fernandes
   fmincon/NSGA-II; Valeriani PSO; Ornano staged) → N-17**: engine
   generici senza condizioni → manca gradiente adjoint, certificati;
   i loro stessi dati (exact batte GA; argmax non identificabile C17;
   delta ~ stopping tolerance C16) sono l'evidenza PRO driver
   certificato. Ancora: registry :534-541, :570-577, :484-490,
   :624-631; findings :1994.
8. **Johnson-Boney 1975 + Scofield-Hoffman 1971 → N-18**: precedenti
   classici tabulated-EOS/real-gas MoC ([DIR-THERMOTAB]) → manca
   separazione generatore/interfaccia (S11) e il contratto tabelle
   C24-C26; gamma-sensitivity ~80x = perché la chiusura è load-bearing.
   Ancora: registry :460-466, :380-386.
9. **Browne-Shepherd SDT → N-18**: lato GENERATORE degli stati (CJ/ZND)
   → manca il contratto d'interfaccia a tabelle — il nostro split
   generatori-liberi/interfaccia-tabelle è esattamente la giunzione che
   il campo non ha formalizzato. Ancora: registry :300-307.
10. **Janc 2025 → N-18 (contrasto)**: ramo finite-rate NON-tabulato
    reso differenziabile (threat vector) → manca l'interfaccia a
    tabelle; il confronto di costo/certificabilità è il falsificatore
    costruibile della scelta backend-1. Ancora: registry :606-613.
11. **Harroun 2020+2021 → N-19**: validazione sperimentale ad-hoc +
    discriminating-failure datum (l'esperimento separa ciò che il C_F
    medio non separa, 1.25 flat) → manca tier di evidenza dichiarato
    (P34), gate dei claim (D-44), referee pre-registrato (R22-CFD) —
    istanze, mai procedura (CT-3 confermato). Ancora: registry
    :273-285, :633-640.
12. **Ornano 2017 → N-19**: gerarchia staged IMPLICITA a tre stadi di
    fedeltà → manca tier dichiarato e gate formale; l'analogo più
    vicino di P34 nel corpus. Ancora: registry :624-631.

Candidate NUOVE per il merge: **12** (nessuna duplica le righe ledger di
part1/part2: quelle coprono le componenti 1-15; queste nascono con le 5
colonne nuove; le righe 2-4 riusano paper già citati da part1/part2 ma
su componenti diverse).
