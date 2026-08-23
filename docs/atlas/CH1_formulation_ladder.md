# CH1 — Formulazione e ladder: dal pin al problema variazionale mediato

Status: capitolo di RICOSTRUZIONE S-PRES (2026-08-22/23). Non aggiudica nulla:
ancora al record (M0, registries, problem book, P1) e dichiara gli aperti.
Consumo dichiarato: storyboard v3 deck ESA, banca Q&A red-team, mappa F2+.

---

## 0. Glossario minimo (per lettore non di programma) [W2-R6]

- **T3 / "classe di collasso"**: il regime in cui il design a ciclo COLLASSA al
  design steady classico — parete fissa ⇒ Rao allo stato medio ⟨Pc⟩
  (riga G2, `docs/rde_nozzle_literature_map.md:20`); la coincidenza NON è un
  teorema generale ([T-T3-MAP], `docs/claims_registry.yaml:316-327`).
- **Classe S1**: la classe di soluzione certificata del record (soluzioni
  ammissibili del contratto D2.4) in cui vivono i teoremi di unicità/quoziente.
- **Rung 1/2/3**: gradini di rigore della catena (problem book
  `docs/rde_nozzle_problem_book.md:573-575`): rung 1 = stato medio I4 (oracoli
  T3/T4); rung 2 = per-fase mediato (PB-1..3, unica approssimazione O(St));
  rung 3 = pienamente instazionario (T0/freezing, HB, shadowing).
- **DEF**: la costruzione GENO di riferimento (rappresentante di classe a
  9 dof nelle istanze eseguite, `docs/rde_nozzle_MASTER.md:4207-4234`).
- **Table-1 states**: gli stati termodinamici di riferimento pre-registrati
  del problem book usati come input delle campagne.

---

## 1. Ricostruzione

### 1.1 Il pin: la classe dati

Tutto il programma vive dentro un pin dichiarato sulla classe dei dati di
interfaccia: **pure periodic single-mode rotating wave** (pin H3), con
monitor = **T0 flatness** (M0 VI.4bis; enunciato del pin:
`docs/rde_nozzle_MASTER.md:995`; scope note sulla misura:
`docs/rde_nozzle_MASTER.md:108-114`). Il pin è una **MODEL HYPOTHESIS
dichiarata, senza provenienza hardware certificata** (R20) — così è scritto nel
record stesso, tra i "honest boundaries, separately priced" del blocco [S-T0P]
(`docs/rde_nozzle_MASTER.md:560-561`). Una fase che contiene una MODE
TRANSITION (cambia il numero d'onda n) è FUORI dalla definizione della misura
μ e viene instradata al layer robusto (A6/PB-5), mai mediata silenziosamente
(`docs/rde_nozzle_MASTER.md:110-114`).

Il contratto di interfaccia è [D-CONTRACT] D2.4: superficie assialsimmetrica
fissa Γ_d a valle di ogni rilascio di calore, con requisiti R1 (separazione
causale), R2 (dati ben posti), R3 (misurabilità)
(`docs/rde_nozzle_MASTER.md:116-121`). Il DEFAULT certificato è la classe L4:
ogni patch di Γ_d supersonica con margine nel senso del certificato di record
[L4-CERT], che è la forma NORMALE-MERIDIANA **m_n := u·n_m − c ≥ δ** con SPLIT
in due oggetti certificati (M-a) normal-on-surface / (M-a') axial-on-segment +
box, e con R1 CONDIZIONATA alla finestra W1–W4
(`docs/rde_nozzle_MASTER.md:139-169`); la forma "assialmente supersonica"
(u_x − c nudo) è il caso PLANARE — su Γ_d curva/tiltata può licenziare una
marcia ill-posed (tilted-element counterexample,
`docs/rde_nozzle_MASTER.md:151-153`). Su L4 la
mdot-indipendenza è ESATTA e l'influenza a monte è ESCLUSA PER TEOREMA
[T-NSW] (`docs/rde_nozzle_MASTER.md:125-138`). [W2-R5]

### 1.2 La ladder di idealizzazione I0–I4

Dentro D2.4 il record dichiara la ladder (`docs/rde_nozzle_MASTER.md:122-124`):

- **I0** coupled bilevel — il problema accoppiato camera+ugello;
- **I1** wave-frame steady field — campo stazionario nel riferimento d'onda;
- **I2** per-phase meridional profiles — profili meridiani per fase;
- **I3** sonic family (P0,T0)(ξ) — famiglia di stati sonici parametrizzata dalla fase;
- **I4** single mean state — un solo stato medio: il punto dove vive la
  pratica di progetto pubblicata del campo (average-first, design-second) —
  claim di survey, query-bounded [REP]: riga G5 "All published MOC RDE designs
  average first, design second" (`docs/rde_nozzle_literature_map.md:23`).
  [W2-R7]

L'oggetto variazionale è definito da [D-MU] D2.3: μ = pushforward del tempo di
ciclo normalizzato sotto t → ξ; obiettivo mediato (rung 2)
**J[Σ] = ∫ F[Σ; s(ξ)] dμ(ξ)**, con F la spinta stazionaria per-stato
(forma wall o control-surface di Rao, uguali per il teorema della quantità di
moto nella classe S1) (`docs/rde_nozzle_MASTER.md:103-107`).
L'UNICA approssimazione della catena è il passo quasi-steady (rung 2):
⟨F_wall⟩ = ∫ F_steady dμ + O(St), esatta per St → 0, prezzata dal correttore
P4 (`docs/rde_nozzle_MASTER.md:444-450`); il termine di storage è pura
contabilità, esattamente zero in media per periodicità
(`docs/rde_nozzle_MASTER.md:451-461`).

**Remark EAP — il posizionamento industriale di [D-MU] (verificato alla
riga 2026-08-23) [B3-EAP].** L'Equivalent Available Pressure del filone
industriale (`kaemming_paxson_2018`; consumo a valle in `paxson_miki_2022`)
è, verbatim dalle sue Eq. 1-8, la COORDINATA DI PRESSIONE di J_ideal:
expand-then-average (mai mixed-out-then-expand), pesi mass-flux
algebricamente identici ai nostri flussi time-integrated (O1), calcolata nel
detonation frame dove "area average = time average" — cioè il nostro T0(i)
usato tacitamente come fatto, provato qui come teorema
(`docs/rde_nozzle_MASTER.md:2526-2534`). Delta di record: EAP porta le
ipotesi quasi-steady e di disaccoppiamento azimutale (le nostre D1+D2)
"UNSTATED and UNPRICED — the P4 corrector is, among other things, EAP's
missing error bar" (`docs/rde_nozzle_MASTER.md:2537-2539`); e la
formalizzazione "CONTAINS and COMPLETES the EAP doctrine rather than
competing with it" (`docs/rde_nozzle_MASTER.md:2543-2544`). Classe: remark
di record M0 Parte III, fonte [IO] (full text letto 2026-07-16, NTRS
20180006890).

### 1.3 Il quoziente: per-fase = quoziente esatto + rung 2 dichiarato

Il claim onesto di record è a DUE STADI (forma REFUTE_A 2026-08-13, che
sostituisce ogni "the correct object" tout court;
`docs/claims_registry.yaml:1903`, `docs/rde_nozzle_MASTER.md:546-559`):

- **STAGE 1 (esatto)**: dati puri periodici rotanti + dominio/BC
  assialsimmetrici ⇒ la soluzione certificata è un pattern co-rotante
  stazionario; l'aggiunto per-fase/wave-frame è l'oggetto CORRETTO
  symmetry-reduced nella classe pinnata — l'aggiunto periodic-BVP naive è
  DEGENERE (moltiplicatore di Floquet triviale lungo l'orbita di gruppo,
  I − monodromia singolare). Registrato come **[S-T0P] SCHEMA**
  (`docs/claims_registry.yaml:1900-1911`; blocco M0:
  `docs/rde_nozzle_MASTER.md:533-568`), con route di prova nominata
  (equivarianza del gruppo elicoidale + unicità S1 + dominio di dipendenza
  finito da L4). ATTERRAGGI 2026-08-19: la metà di equivarianza
  **[T-T0P-E] è THEOREM** (assembly condizionale in function-space, EOS
  astratta) con famiglia di lemmi di supporto THEOREM
  (`docs/rde_nozzle_MASTER.md:569-601`); e il **MAIN STATEMENT [T-T0P] è
  ATTERRATO** (S-FOUNDATIONS-C2, doc1 rev10 DRY di record): steadificazione +
  canonicità, **SCHEMA su ENTRAMBI gli strati** con split gap lists G1–G12
  (`docs/rde_nozzle_MASTER.md:602-628`). TRE boundaries di record del main
  statement, da portare sempre: (a) **quantificatore ristretto alla classe
  t-PERIODICA** (l1-F2: finché G5 non è scritto, [T-T0P] prova l'enunciato
  RISTRETTO agli elementi t-periodici, `docs/rde_nozzle_MASTER.md:614-616`);
  (b) conclusioni solo su **cl(Ω_march)**; (c) **solo istanze SLIP-FREE**
  (pricing G9) — e il record dichiara testualmente che "the excluded slip
  sheets are the physically generic RDE front type"
  (`docs/rde_nozzle_MASTER.md:616-619`). [W2-R1]
- **STAGE 2 (approssimazione dichiarata)**: le marce 2-D per-fase scartano il
  theta-coupling — rung 2, "the only approximation in the chain"
  (`docs/rde_nozzle_MASTER.md:556-558`).

Il write-up completo della prova stage-1 a livello S1 è un finding APERTO di
record: `docs/findings_registry.yaml:1450-1458`
(id `theory:s-t0p-proof-writeup-pending`, CONFIRMED, severity low, owner = F2
theory window, **trigger = "F2 entry, or the first external presentation of
the two-stage per-phase claim"** — cioè S-PRES stessa arma questo trigger).

### 1.4 I problemi PB-1..PB-5 e la catena dei rung

Il problem book §10 (`docs/rde_nozzle_problem_book.md:521-575`) fissa gli
enunciati precisi:

- **PB-1** (il core): dato I2/I3 con famiglia s(·) e misura μ, classe
  ammissibile A, classe soluzione S1: **massimizzare J[Σ] = ∫F[Σ; s(ξ)]dμ(ξ)**;
  deliverable = sistema di stazionarietà T2 (condizioni Rao/Kraiko per fase +
  wall condition μ-mediata + trasversalità endpoint μ-mediata pesata),
  esistenza in classi ristrette, regolarità dei moltiplicatori
  (`docs/rde_nozzle_problem_book.md:524-530`).
- **PB-2**: PB-1 per plug troncato con L_p < l(ξ_peak) e chiusura di base
  pressure: il nesting di T4 cade, **max∫ < ∫max strictly** — "the first
  concrete problem NOT solved by any single-phase design"
  (`docs/rde_nozzle_problem_book.md:532-536`).
- **PB-3**: duty split shrouded (congettura C1)
  (`docs/rde_nozzle_problem_book.md:538-542`).
- **PB-4**: bilevel/coupled, adjoint reagente = frontiera dichiarata
  (`docs/rde_nozzle_problem_book.md:544-547`).
- **PB-5**: robusto (multistabilità di modo, misura mal specificata: E_π[J],
  CVaR, Wasserstein-DRO) — la formulazione di record quando H-A1 cade
  (`docs/rde_nozzle_problem_book.md:549-551`).

Catena dei rung ("rigor obligations, not slogans",
`docs/rde_nozzle_problem_book.md:573-575`):
**rung1 (= I4 / oracoli T3, T4) ⊂ rung2 (PB-1..3)** — ponte O(St) P4 →
rung3 (T0/freezing, HB, shadowing) — coupling → PB-4/PB-5.

### 1.5 Le degenerazioni e la biforcazione (il cuore)

La mappa esatta di DOVE il design single-phase/mean-state basta e DOVE
fallisce strutturalmente:

**(i) Solo DOF di area di uscita — i due metodi coincidono.**
[T-T7RED] **THEOREM** (`docs/claims_registry.yaml:381-392`; blocco M0
`docs/rde_nozzle_MASTER.md:2977`): con il solo DOF ε, le condizioni mediate
wall+endpoint degenerano alla condizione PESATA **⟨P_E(ε; ξ)⟩_μ = Pa**,
risolta sull'inversione area-ratio reale (forma chiusa NPR(ε*) = ⟨Pc⟩/Pa
demota a oracolo γ-costante). Nota di precisione: coincidenza col design a
"stato medio equivalente", ma con la media PESATA — il falsificatore di
record è esattamente il wrong-averaging rejector ("the unweighted mean
reproducing the weighted eps* beyond bars", `docs/claims_registry.yaml:391`).

**(ii) Plug pieno ideal-adapted — il design peak-phase è ottimo per TUTTE le
fasi insieme.** [T-T4] THEOREM 6, classe **THEOREM\*** (sotto la chiusura di
ideal-adaptation [C-HT4]) (`docs/claims_registry.yaml:329-340`; enunciato e
prova `docs/rde_nozzle_MASTER.md:2294-2315`): per fase F è non-decrescente
nell'estensione l del plug, costante per l ≥ l(ξ), l(ξ) crescente in Pc(ξ);
gli argmax per fase sono half-line ANNIDATE [l(ξ), ∞), quindi
**max_Σ ∫F dμ = ∫ max_Σ F dμ**, raggiunto dal design della fase di PICCO
(plug non troncato a NPR = P_CJ/Pa). Carrier: X-GRP06/X-GRP10/X-GRP12;
falsificatore: oracolo O2 (`docs/claims_registry.yaml:337-339`).

**(iii) Troncamento / length caps — il nesting SI ROMPE, si apre PB-2.**
Clausola di sharpness dentro THEOREM 6 (`docs/rde_nozzle_MASTER.md:2316-2319`):
"a length cap L < l(ξ_peak), a base-pressure model at a truncation plane, or
non-ideal adaptation break the nesting: then **max∫ < ∫max STRICTLY** and the
optimum satisfies the averaged system (T7) with the μ-averaged plug corner
condition". Questa è la biforcazione: a sinistra il mondo I4 basta (con la
media giusta), a destra nessun design single-phase risolve il problema.

**(iv) Il sistema mediato stesso.** [T-T7FS] THEOREM-SCHEMA 8, classe
**SCHEMA** (`docs/rde_nozzle_MASTER.md:2812-2891`): (a) per-fase l'adjoint
Euler (forma chiusa classica nel sottoclasse irrotazionale-omentropico);
(b) **shared wall**: ∫ G_ξ dμ + λ_L g_L = 0 — "NO phase satisfies its own
wall condition; the μ-average does" (`docs/rde_nozzle_MASTER.md:2827-2829`,
`docs/rde_nozzle_P1_sections_5_7.md:66-70`); (c) **endpoint condiviso** in
FORMA A CONO (C31, ratifica utente 2026-08-13): D := ∫(∂F/∂s_E)dμ ∈ N_K(s_E*)
(`docs/rde_nozzle_MASTER.md:2830-2851`). BOXED WARNING di record: il peso
w(ξ) è indipendente dalla fase ESATTAMENTE nella classe di collasso T3 — lì e
solo lì (**') si riduce alla media naive; **ovunque altrove la media naive è
SBAGLIATA** (`docs/rde_nozzle_P1_sections_5_7.md:96-104`,
`docs/rde_nozzle_MASTER.md:2856-2859`). Lemma di trasferimento a cono
[T-T7CN] **THEOREM** con CONVERSO FALSO (controesempio a due fasi di record)
(`docs/claims_registry.yaml:1913-1924`, `docs/rde_nozzle_MASTER.md:2862-2874`).

**(v) La mappa dei breaker del collasso.** [T-T3-MAP] **SCHEMA** (container;
classi per clausola marcate nel blocco M0) (`docs/claims_registry.yaml:316-327`):
il claim GENERALE di coincidenza cycle-vs-steady è **rifiutato come teorema
generale** e provato sul corner tier-1+vacuum (T-T3-SI); i breaker (Pa ≠ 0,
variazione per-fase di M/T0/γ/s, swirl, patch subsoniche, convenzione di
misura) rompono ciascuno un oggetto distinto.

### 1.6 Il caso FIXED-(ε, L)

P1 §5.1(c) (`docs/rde_nozzle_P1_sections_5_7.md:72-94`): nella forma a cono
della trasversalità, **K = {point} (fixed-(ε,L) pinning) ⇒ condizione
VACUA**, i λ sono le componenti di D a segno libero — "the fixed-eps
bookkeeping in which all executed instances live"
(`docs/rde_nozzle_P1_sections_5_7.md:80-82`; gemello M0:
`docs/rde_nozzle_MASTER.md:2840-2845`, che ancora il driver committato:
`a1_toc_variational_jax.py:1748`). Conseguenza strutturale: a (ε, L) fissati
**TUTTA la differenza tra design a ciclo e design a stato medio vive nella
shared-wall condition** (§5.1(b), `docs/rde_nozzle_P1_sections_5_7.md:66-70`)
— nessun contributo dall'endpoint. Split di contenuto: la componente assiale è
puntualmente non-negativa (contenuto binario: attività del length cap,
λ_L = ∫(−λ3/q)dμ ≥ 0); la componente radiale CAMBIA SEGNO lungo il ciclo e
porta TUTTO il contenuto di averaging
(`docs/rde_nozzle_P1_sections_5_7.md:90-94`,
`docs/rde_nozzle_MASTER.md:2875-2884`).

### 1.7 Riga H — licensing: fin dove vale il metodo (nodo N-H) [B3-H]

Principio di record (M0 Parte V, `docs/rde_nozzle_MASTER.md:3008-3045`,
verificato alla riga 2026-08-23): **"The flow — not the method — selects
the reduction, per design point"** (:3010). La tabella di licenza per
classe di flusso, portata QUI con i canali residui per riga (guardia 16:
ogni claim di copertura enumera perimetro E canali residui non coperti,
con classe):

| classe di flusso (census) | macchina | deliverable / classe | canali residui NON coperti (classe) |
|---|---|---|---|
| single/k-wave rotating mode | steadificazione T0 (esatta in classe); rung 2 mediato + barra O(St); ancora BVP wave-frame | Σ* + certificato PIENO; teoremi per-fase | rung-2 O(St) (prezzato P4, SCHEMA/corrector G3-owned); gap list G1–G12 di [T-T0P] (SCHEMA sui due strati); slip-free G9 + cl(Ω_march) (boundary dichiarati, §1.3); bridge = CONJECTURE-with-falsifier (:3013); patch subsoniche FUORI dal default L4 = case-class DICHIARATA (D1 4.3bis O1-O4), canali di RISALITA dell'informazione — mai mediate in silenzio (consumo guardia 17 [B3-G17]) |
| modulated / counter-rotating (RPO) | BVP periodico, (Ω,T) incognite, adjoint doubly-bordered; dimostratore 2-D+t | **PRACTICE** — "space-time tracking 3-D absent" (:3014) | nessun certificato di classe; tutta la riga è pratica dichiarata |
| multistable mode set | ottimizzazione per-branch + layer robusto CVaR/DD-DRO sulla misura di modo | Σ* robusto; **SCHEMA/PRACTICE** (:3015) | misura di modo mal specificata = PB-5 (formulazione di record, CH1 §1.4); nessuna provenienza hardware della misura (R20) |
| chaotic / mode-hopping | SOLO bound + surrogati robusti; shadowing RIFIUTATO ("hypotheses fail across shocks") | **RIFIUTO ONESTO dei certificati** + muro [S-GBE] | il muro è un CEILING, non un design: J_exact⁺ ≤ F_env(flussi medi d'interfaccia) sotto ipotesi E1–E5 dichiarate, niente Birkhoff (Cesàro finite-T + storage limitato); classe **SCHEMA**, carrier X-GBE PASS di record 2026-08-06 (`docs/claims_registry.yaml:1843-1864` — blocco S-GBE :1843-1854 + blocco X-GBE :1856-1864 [fix WB1-C3-02]); sul scope periodico il muro ergodico è Jensen-looser del muro per-fase (gap riportabile, :3016) |

Ancora del muro: [S-GBE] RESOLVED 2026-08-06 (S16 T4,
`docs/rde_nozzle_GB_ergodic.md`), inline nella riga caotica della tabella
M0 (:3016) — il named missing lemma è SCRITTO, l'etichetta
quasi-steady-only del muro superiore è LIFTED; i rung inferiori
(attainability) restano steady-setting.

**H-ii — gli strumenti di licensing** (M0:3017-3026 + VI.4bis(v)
M0:3162-3166): (1) **thrust-trace flatness** = distanza dalla
steadificabilità — e il flatness monitor è OBBLIGATORIO in ogni data
contract (VI.4bis(v)); (2) **census refresh per accepted optimizer step**
(tier-flip detection): la classe di flusso viene RI-VERIFICATA a ogni
passo accettato, mai assunta; (3) St_n e numeri di drift DAI DATI (un solo
Strouhal governa, D1 ⊃ D2); (4) mixed-interface decision tree (O1–O4).
Classe: strumentazione di record (PRACTICE armata, DEFINITION per il
monitor).

**Consumo guardia 17 — feedback ugello→camera [B3-G17]** (pin utente
2026-08-23, `GUARD_CHECKLIST.md` riga 17; registrato in SESSION2_LOG
CKP-S2-1). Il licensing per classe di flusso PRESUPPONE la lettura
choking-pieno/patch-subsoniche: il decoupling a monte (assenza di
feedback) si può asserire SOLO se la porzione pre-gola è convergente E la
gola è tutta sonica o supersonica lungo ciclo/azimut; se la gola — anche
throatless geometrica (superficie sonica senza gola geometrica) —
presenta patch subsoniche, il feedback C'È: le patch sono i canali di
risalita dell'informazione, case-class DICHIARATA (D1 4.3bis O1-O4,
coerente con C-1bis/KP18 sonic line corrugata), mai mediate in silenzio.
NESSUN claim di decoupling/one-way BC senza la condizione di choking
citata; il regime forte-transiente (unstart) è fuori dalla lettura a
piccole perturbazioni (confine dichiarato se toccato). **La regola è di
CASA in CH10** (§1.2 lettura fisica del contratto, U3', Q7): questo
capitolo la CITA come precondizione della tabella di licenza —
cross-ref, non duplicazione.

**H-iii — la query "dichiarazione del regime di validità nel campo"
(protocollo bounded G-11, eseguita in-onda 2026-08-23).**
- **q**: "il campo RDE-nozzle dichiara il REGIME DI VALIDITÀ della propria
  media / del proprio metodo di design (quasi-steady, averaging), con
  prezzo d'errore?"
- **Perimetro CHIUSO**: `docs/literature_registry.yaml` (174 id) +
  `docs/rde_nozzle_literature_map.md` + campagne P-A..P-D (`liu_2022`,
  `li_xu_lv_lv_song_2023`, `li_xu_lv_yu_zhou_2025`, `jourdaine_2019`).
- **Comandi misurati in finestra**: grep -i
  `validity|applicab|regime.*valid|assumption.*declar` su litmap → 3 hit
  (:142, :613, :642; :613/:642 = sezione b6 nostra, non del campo); grep -i
  `validity|applicab|unstated|undeclared` su registry → hit solo su righe
  NON-RDE (il NOSTRO seed-validity program f2-c20/c21 +
  `rao_beck_booth_1999` :410, scuola classica — "optimum ON the validity
  boundary"), zero sulle righe P-A..P-D [fix WB1-C3-01].
- **ESITO: NOT-FOUND(q) sul campo RDE-nozzle istanziato** (guardia 4):
  NUAA `li_xu_lv_lv_song_2023`/`li_xu_lv_yu_zhou_2025` (gap
  steady-vs-transient riportati come DATI di campagna, nessun regime
  dichiarato); Purdue `harroun_2021` (convenzione di media UNDECLARED nel
  paper — deep-check LL-2, pp.670-671 + Eq.10); NASA-Glenn/AFRL
  `kaemming_paxson_2018` (ipotesi D1+D2 "UNSTATED and UNPRICED",
  M0:2537-2539) e `paxson_miki_2022` (OFAT senza bande); `jourdaine_2019`
  (3-D unsteady, nessuna dichiarazione di regime della media usata);
  `liu_2022` (assioma average-then-design dichiarato verbatim, mai
  prezzato — litmap:91-93). **Unica istanza ADIACENTE trovata, FUORI dal
  campo RDE** (scuola classica): `kraiko_osipov_1970` dichiara
  l'approssimazione quasi-stazionaria con "validity footnote, unpriced"
  (litmap:141-142, testo citato) — dichiarata ma NON prezzata. **STOP**
  (nessun procurement in-onda). Eco: CH5 (riga N).
- Classe dell'esito: NOT-FOUND(q), query-bounded al perimetro sopra.

**H-iv — il rifiuto onesto come proposta (materiale deck).** La riga
caotica non è una lacuna da nascondere: è la proposta honesty-first del
programma — il metodo DICE dove i suoi certificati non valgono, con lo
strumento che rileva l'uscita di classe (flatness monitor + census
refresh) e con il muro [S-GBE] che al posto del certificato consegna un
ceiling PROVATO sotto ipotesi dichiarate. Combinato con H-iii: il campo
non dichiara il proprio regime di validità; noi dichiariamo il nostro E il
punto esatto in cui rifiutiamo il certificato. Classe: posizionamento su
fatti di record (tabella M0 V + NOT-FOUND(q) sopra).

**H-v — B-lite, il metro cheap del rung 2** ([S-BLITE], addendum di
record 2026-07-21, S12; M0:3027-3044): sul dominio NOZZLE-ONLY con margine
assiale certificato u_x − c ≥ δ > 0 (dati classe I1, Ω INPUT dai dati;
certificato (M-a') di L4-CERT), la condizione C2 del Lemma 4 è SODDISFATTA
e il campo wave-frame ESATTO è computabile per space-marching elicoidale
3-D a costo di march (fitted sheet come incognita per-stazione), con
l'adjoint che si solleva verbatim per Lemma B. Verbatim di record:
**"B-lite is the cheap exact meter of the rung-2 sweep/D2 residual"**
(M0:3037-3038, verificato alla riga). L'ancora PIENA della Parte V resta
necessaria dove entra la camera (Ω come output, tasche subsoniche,
reazione). Brick nominato da verificare per primo: G12-L1-3D. Cross-ref:
CH3 §1.2 lo cita accanto ai deriver di delta/L_H come l'arbitro a costo di
march. Classe: scheda [S-BLITE] di record (SCHEMA con brick nominato).

---

## 2. Stato per-claim

| Claim | Classe | Ancora | Carrier / falsificatore |
|---|---|---|---|
| Pin dati: pure periodic single-mode rotating wave, monitor T0-flatness | MODEL HYPOTHESIS dichiarata (nessuna provenienza hardware certificata, R20) | M0:995; M0:560-561; M0:108-114 | monitor T0-flatness (VI.4bis); fuori-pin → route Zahr-Persson/Rubino (M0:563-565) |
| Ladder I0–I4, contratto D2.4, default L4 | DEFINITION/contract (L4: [T-NSW] THEOREM per l'esclusione upstream) | M0:116-138 | L4-CERT split (M-a)/(M-a'), M0:139-166 |
| Obiettivo J = ∫F dμ (rung 2); unica approssimazione = O(St) | DEFINITION [D-MU] + passo quasi-steady prezzato (P4) | M0:103-107; M0:444-450 | corrector P4; backstop Theorem 3 (M0:448) |
| Per-fase = quoziente esatto (stage 1) | [S-T0P] SCHEMA; metà equivarianza [T-T0P-E] THEOREM | claims_registry:1900-1911; M0:533-568; M0:574-581 | falsificatore: istanza L4 pure-periodic con soluzione certificata NON co-rotante (claims:1910); batteria [X-T0P] owed, owner F2 |
| Claim a due stadi (mai "the correct object" tout court) | SCHEMA (forma REFUTE_A) | claims_registry:1903; M0:546-559 | — |
| Solo exit-area DOF: degenerazione a ⟨P_E(ε;ξ)⟩_μ = Pa | [T-T7RED] THEOREM (EOS-general) | claims_registry:381-392; M0:2977 | carrier X-GRP06/10/12; wrong-averaging rejector (claims:391) |
| Plug pieno ideal-adapted: nesting, peak-phase design ottimo | [T-T4] THEOREM* (sotto [C-HT4]) | claims_registry:329-340; M0:2294-2315 | carrier X-GRP06/10/12; oracolo O2 (claims:339) |
| Troncamento/caps: max∫ < ∫max STRICTLY, apre PB-2 | clausola sharpness di THEOREM 6 (stessa classe THEOREM*, stesso scope di chiusura) | M0:2316-2319; problem_book:532-536 | gap quantitativo NON calcolato (PB-2 aperto, §3) |
| Sistema di stazionarietà mediato (wall + endpoint pesato) | [T-T7FS] SCHEMA | M0:2812-2891 | boxed warning naive-average (P1:96-104) |
| Cone transfer (per-fase in cono ⇒ ciclo in cono; converso FALSO) | [T-T7CN] THEOREM | claims_registry:1913-1924; M0:2862-2874 | rejector S3/A39: famiglia one-phase-out/mean-in DEVE essere accettata (claims:1923) |
| Fixed-(ε,L): endpoint vacuo, differenza tutta nella shared wall | dentro T7(c) forma a cono (C31, ratifica utente 2026-08-13) | P1_sections_5_7:72-94; M0:2840-2845 | regime di TUTTE le istanze eseguite (driver :1748) |
| Coincidenza generale cycle-vs-steady RIFIUTATA come teorema generale | [T-T3-MAP] SCHEMA (container; clausole con classi proprie) | claims_registry:316-327 | carrier CARRIER-A..E nominati, dispatch F5a/F2/F2a (claims:319) |
| Datum in-class F7: rappresentante DEF non è argmax, +0.51% | dato MISURATO con caveat dichiarati: RECORDED-CONSISTENT, NON ri-eseguibile; claim cap in-class | M0:4207-4234 | riproduzione aritmetica da s24_deftw_f3f7.json; rigenerazione = conditional, owner F2 |
| Scala esterna del premio Rao in-class: 0.04–0.34% Isp (loro numeri, CT-6) | [REP] (literature registry) | literature_registry.yaml:568 | — |
| Novità G1/G5/G6 | NOT-FOUND(q) — sempre query-bounded | literature_map:19,23,24 | caveat list estesa obbligatoria (M0:2339-2350) |

---

## 3. Gli APERTI

1. **Write-up completo della prova [S-T0P] a livello S1** — findings
   `theory:s-t0p-proof-writeup-pending` (CONFIRMED, severity low), owner =
   F2 theory window, trigger = F2 entry O la prima presentazione esterna del
   claim a due stadi (`docs/findings_registry.yaml:1450-1458`). **S-PRES arma
   questo trigger**: il deck può presentare il claim solo nella forma a due
   stadi con lo stato SCHEMA/THEOREM-parziale dichiarato. RICONCILIAZIONE
   owed vs landed [W2-R1][W2-R8]: è LANDED il main statement [T-T0P]
   (steadificazione + canonicità, quantificatore t-periodico, cl(Ω_march),
   slip-free; SCHEMA su entrambi gli strati, `docs/rde_nozzle_MASTER.md:602-628`)
   e la metà di equivarianza [T-T0P-E] THEOREM; RESTA owed il write-up a
   livello S1 + la batteria [X-T0P]. Nota di manutenzione (fuori scope
   S-PRES): la riga findings porta un code-anchor STALE
   (`docs/findings_registry.yaml:1455` cita M0:463-498; il blocco [S-T0P]
   vive a M0:533+) e pre-data l'atterraggio 2026-08-19 — il deck NON deve
   ereditare quell'ancora né presentare come interamente owed ciò che è
   parzialmente landed.
2. **PB-2 mai eseguito**: il gap quantitativo max∫ vs ∫max sul plug troncato
   (cycle-optimal vs baselines peak- e mean-designed, Table-1 states) è un
   deliverable formulato, non calcolato (`docs/rde_nozzle_problem_book.md:532-536`).
   La strictness è enunciata come sharpness di THEOREM 6 sotto chiusura
   [C-HT4]; nessun numero di gap esiste nel record.
3. **Il pin non ha provenienza hardware certificata** (R20): ipotesi di
   modello dichiarata, monitor specificato; fuori-pin la route registrata è
   Zahr-Persson/Rubino + LSS/NILSS (`docs/rde_nozzle_MASTER.md:560-565`).
4. **Batteria eseguibile [X-T0P]** (rejector simbolici della famiglia di
   lemmi T0P): owed, owner F2 (`docs/rde_nozzle_MASTER.md:586-589`).
5. **Il datum +0.51% è NOT RE-EXECUTABLE**: il design vector F7 non fu
   persistito; rigenerazione = conditional dichiarata, owner F2
   (`docs/rde_nozzle_MASTER.md:4219-4227`).
6. **P0 di letteratura non letti** che condizionano la forma del claim di
   novità: ISABE-2003-117 + Bogdanov 2002 (descrittore average-thrust =
   inferenza NON verificata), Harroun M.S. Thesis 2019 ("the closest prior
   art... NOT READ"), Levin-Manulovich 2010, Billings 2000
   (`docs/rde_nozzle_MASTER.md:2339-2350`).

---

## 3-bis. ANTENATI DIRETTI (lineage claims — nodi N-A / N-B / N-H) [B3-LIN]

Contratto di join [F-des-4]: ogni claim di novità dei nodi ospitati cita
≥1 LL-id del `LINEAGE_LEDGER.md` (lint 7); righe CANDIDATE fino al pass
del refuter C6, salvo i SEED confermati dalle parti.

**N-A (il problema e i suoi dati — contratto, misura μ):**
- **LL-1 Kraiko-Osipov 1970** (`kraiko_osipov_1970`): parete pesata W(t)
  integrata nel tempo + condizioni endpoint time-averaged, moltiplicatori
  su caratteristiche → cosa gli manca vs noi: misura di ciclo μ PINNATA
  ([D-MU]), steadificazione T0/quoziente, certificati. Citazione
  OBBLIGATORIA in ogni claim di primato (già cablata nei caveat D-06,
  §4 Q3). Nota H-iii: la sua footnote di validità (dichiarata, unpriced,
  litmap:141-142) è l'istanza adiacente più vicina alla NOSTRA disciplina
  di regime dichiarato.
- **LL-3 Stechmann 2019** (`stechmann_2019`, SEED utente): blowdown 0-D
  per-phase con media mass-weighted DICHIARATA, famiglie fisse → manca:
  contorno variazionale, contratto d'interfaccia Γ_d, classe-dati
  certificata.
- **LL-11 Sternin 1957/1959**: possibile antenato PRE-KO della linea
  variazionale a media temporale — confidenza LOW, **procurement-gated**
  (residuo R3 del ledger): NESSUN claim finché non letto; dichiarato qui
  perché il §3-bis è il posto dove l'assenza va detta, non taciuta.

**N-B (quando mediare è esatto):**
- **LL-4 Kaemming-Paxson 2018 EAP** (`kaemming_paxson_2018`, SEED): rung
  int-max + ricostruzione state-averaged + statistiche di gola → manca: le
  ipotesi D1+D2 sono unstated/unpriced; il correttore P4 è la loro barra
  d'errore mancante (remark §1.2, M0:2537-2539).
- **LL-16 Efremov-Kraiko 2004** (`efremov_kraiko_2004_augmentor`):
  variazionale di spinta period-averaged (Eq. 1.7, p.624, page-verified)
  SENZA contorno di parete, che COLLASSA a steady per ammissione degli
  autori (M0:2320-2330) → è la ragione per cui la formulazione PB-2 di
  record è BLOCCATA nella forma D-06 ("genuinely averaged and
  NON-COLLAPSING", §4 Q3), mai "the first averaged-thrust variational
  problem".

**N-H (licensing):**
- **ANTENATI: NOT-FOUND(q)** — nessuna riga del LINEAGE_LEDGER (LL-1..35)
  copre una ladder di licenza per classe di flusso con rifiuto dichiarato
  dei certificati; query di supporto = H-iii (§1.7: il campo non dichiara
  il regime di validità; perimetro chiuso citato lì, STOP). L'istanza
  adiacente parziale resta la validity footnote unpriced di LL-1
  (dichiarazione senza prezzo né strumento di monitoraggio).

---

## 4. Domande da panel (banco utente incluso)

**Q1. "A lunghezza ed ε fissati, il nostro programma vs un variazionale su
dati al contorno medi alla Li-Xu: dove è trattato nel record e che entità di
differenza ci aspettiamo?"**
Trattato in P1 §5.1(c) + M0 T7(c): a (ε, L) fissati la condizione di endpoint
è VACUA (K = {point}), quindi la differenza tra i due programmi vive
INTERAMENTE nella shared-wall condition ∫G_ξ dμ + λ_L g_L = 0
(`docs/rde_nozzle_P1_sections_5_7.md:72-94` e `:66-70`;
`docs/rde_nozzle_MASTER.md:2840-2845`). Entità: la differenza è ZERO per
teorema sul corner PROVATO (T-T3-SI, tier-1+vacuum; la coincidenza
cycle-vs-steady resta "refuted as a general theorem",
`docs/claims_registry.yaml:316-327`); nella classe T3 il peso w è
fase-indipendente e (**') collassa alla media naive
(`docs/rde_nozzle_P1_sections_5_7.md:96-104`) [W2-R3]; fuori, il record ha UN
dato misurato in-class: il rappresentante DEF-wall non è l'argmax J della sua
classe tier-0, surplus **+0.51%** (+2.0407e5 vs banda pre-registrata 5.38e3,
38×), con caveat dichiarati (RECORDED-CONSISTENT ma non ri-eseguibile;
claim cap: statement in-class sul rappresentante a 9 dof, MAI sull'ottimalità
della costruzione DEF nella sua famiglia; **band-underinclusion di record**:
l'errore di rappresentazione di classe satura M → 2M ed è sotto-coperto dalla
differenza J M-vs-2M, bound sistematico grezzo **~6e4** contro il surplus
2.0407e5 — ~30% del datum, `docs/rde_nozzle_MASTER.md:4216-4219`) [W2-R2]
(`docs/rde_nozzle_MASTER.md:4207-4234`).
Scala esterna di riferimento (numeri LORO, CT-6): il premio Rao in-class
misurato dalla letteratura dei truncated perfect nozzles è 0.04–0.34% Isp
(`docs/literature_registry.yaml:568`). Il confronto DIRETTO
cycle-designed vs mean-designed contour è PB-2/N1: formulato, **non ancora
calcolato** (OPEN, `docs/rde_nozzle_problem_book.md:532-536`). Nota di
precisione su "alla Li-Xu": l'attribuzione di metodo "MOC su stato
time-averaged" a Li-Xu-Huang 2022 è QUARANTINED di record (non supportata a
livello di abstract verificabile, full text non letto)
(`docs/rde_nozzle_literature_map.md:74-91`); il claim di pratica del campo si
ancora invece a Liu 2022 (design axiom verbatim) e alla riga G5.

**Q2. "Se P-B già applica Rao/Veen a input mediati, cosa portiamo noi?"**
Dal record: tutta la pratica pubblicata è "average first, design second"
(riga G5: "All published MOC RDE designs average first, design second",
`docs/rde_nozzle_literature_map.md:23`; Harroun 2021 = steady MOC a NPR
fissato, `:20`; Liu 2022 dichiara l'assioma verbatim, `:91-93`). Noi portiamo
tre cose che quella pratica non ha: (1) i **teoremi che dicono QUANDO
average-then-design è esattamente ottimo** — T-T7RED (solo-ε: sì, ma con la
media PESATA giusta, non quella naive; claims:381-392) e T-T4 (plug pieno
ideal-adapted: sì, al design peak-phase; claims:329-340) — cioè la
giustificazione che il campo assume per assioma; (2) la **mappa di dove
fallisce strutturalmente**: troncamento/caps ⇒ max∫ < ∫max strictly ⇒ PB-2,
il primo problema non risolto da alcun design single-phase
(M0:2316-2319; problem_book:532-536); (3) il **sistema di ottimalità mediato
corretto** ((**'), forma a cono, boxed warning: fuori T3 la media naive dei
progetti o dei residui non soddisfa alcuna condizione di ottimalità del
problema mediato — P1:96-104). In una riga: il campo applica Rao a input
mediati; noi dimostriamo quando quello è un teorema, quando è un errore, e
cosa va risolto al suo posto.

**Q3. "In che forma ESATTA regge il claim 'nessuno ha mai posto il problema
di ottimo per RDE'?"**
In QUELLA forma non regge e non va mai detta. Le forme di record, tutte
query-bounded: (a) G1 "cycle/phase-averaged SHAPE-FUNCTIONAL variational
formulation of the RDE nozzle" = NOT-FOUND(q)
(`docs/rde_nozzle_literature_map.md:19`); (b) G6 "averaged-Rao optimality
system" = NOT-FOUND(q) (`:24`); (c) per PB-2 la FORMULAZIONE BLOCCATA di
record (D-06, "never abbreviate") è: **"the first genuinely averaged and
NON-COLLAPSING shape problem of the program (a CYCLE instance)"** — la frase
"the first averaged-thrust variational problem" è DEAD di record perché
Efremov-Kraiko 2004 pone un problema variazionale a spinta mediata sul
periodo (Eq. 1.7 p.624, page-verified) che però non ha contorno di parete e
COLLASSA a steady per ammissione degli autori (Summary p.631)
(`docs/rde_nozzle_MASTER.md:2320-2330`). Caveat obbligatori quando si
presenta: Kraiko-Osipov PMM 1970 pone già condizioni endpoint time-averaged
per ugello length-capped ("first" = program-internal: prima istanza
CYCLE-averaged per il plug RDE, non primo problema di forma mediato tout
court); lista estesa D-06 (ISABE-2003-117/Bogdanov non letti-P0, Reuther ×2,
Ornano, Harroun thesis P0, Levin-Manulovich, Billings)
(`docs/rde_nozzle_MASTER.md:2331-2350`).

**Q4. "PB-2 dice max∫ < ∫max strictly: dov'è la prova e che scope ha?"**
La prova del NESTING (la parte positiva) è la prova di THEOREM 6 [T-T4],
classe THEOREM* sotto la chiusura di ideal-adaptation [C-HT4]
(`docs/rde_nozzle_MASTER.md:2303-2315`; monotonia da (p_wall − Pa)dA_proj > 0,
nesting degli argmax, attainment al picco). La STRICTNESS sotto
troncamento/caps è la clausola di sharpness dello stesso teorema, ENUNCIATA
di record DOPO il QED ma **SENZA prova scritta** nel record (la prova a
M0:2303-2315 copre solo la parte positiva del nesting; nemmeno l'ipotesi
implicita μ({ξ: l(ξ) > L}) > 0 è enunciata) — risposta onesta al banco: "il
nesting è provato; la strictness è clausola enunciata senza prova scritta; il
carrier quantitativo è PB-2 (OPEN)"; un eventuale write-up della strictness è
un finding da mintare, non da riempire qui [W2-R4]
(`docs/rde_nozzle_MASTER.md:2316-2319`). Scope dichiarato: free-boundary plug
sotto [C-HT4], con citation duty Kraiko-Egoryan sulla chiusura
(claims_registry:332, M0:2350-2352). Risposta onesta sul quantitativo:
**il gap non è mai stato calcolato** — PB-2 è formulato
(problem_book:532-536) ma il computo cycle-optimal vs baselines è OPEN
(owner: campagna PB-2, nessuna data di record). Il falsificatore vivo di T-T4
è l'oracolo O2 ("ideal-plug machinery not returning the peak design; or a
capped cell where extension strictly loses", claims_registry:339).

**Q5 (attesa). "Il vostro 'pin' è realistico? Gli RDE reali hanno modi
multipli, controrotanti, instabilità."**
Risposta dal record: il pin è un'IPOTESI DI MODELLO dichiarata, con monitor
(T0 flatness) specificato e senza provenienza hardware certificata (R20)
(M0:560-561); le fasi con mode transition sono FUORI definizione e instradate
a PB-5 (robust layer), mai mediate silenziosamente (M0:108-114); fuori-pin la
route registrata è Zahr-Persson/Rubino + LSS/NILSS (M0:563-565). Carta attesa
dal panel sulla fisica degli scarichi (slip lines): il teorema di
steadificazione [T-T0P] vale su istanze SLIP-FREE per pricing G9 dichiarato,
e il record stesso dichiara che le slip sheets escluse sono "the physically
generic RDE front type" (M0:616-619) — la restrizione è di record, non
nascosta; carrier eseguibile [X-T0P] owed, owner F2 [W2-R1]. Non si
difende il pin come fatto fisico: si difende la disciplina di dichiararlo.

**Q6 (attesa). "Perché l'aggiunto per-fase non è un surrogato povero
dell'aggiunto instazionario vero?"**
Perché nella classe pinnata l'aggiunto periodic-BVP naive è DEGENERE
(moltiplicatore di Floquet triviale lungo l'orbita di gruppo): il quoziente di
simmetria non è una scorciatoia, è ciò che rende il problema ben posto; la
macchina generale applicata naive sarebbe essa stessa ill-posed senza lo
stesso quoziente (M0:548-555). Classe: SCHEMA con metà equivarianza THEOREM
(M0:574-581) e main statement [T-T0P] LANDED con boundaries dichiarati
(t-periodico, cl(Ω_march), slip-free; M0:602-628) [W2-R1], write-up completo
a livello S1 owner F2 — dichiarato.

---

## 5. Cosa deve dire il deck

1. **La ladder come spina dorsale narrativa** (DEFINITION di record,
   M0:116-124): I0→I4, con la pratica del campo collocata a I4 e il programma
   a I2/I3 + μ — un'immagine, tutta la storia.
2. **Il claim a due stadi, mai di più** (SCHEMA + [T-T0P-E] THEOREM +
   main statement [T-T0P] landed con boundaries, claims:1903, M0:533-628):
   "per-fase = quoziente esatto + rung 2 dichiarato"; l'unica approssimazione
   della **CATENA DI FORMULAZIONE** è O(St) (M0:444-450) — sulla stessa
   slide: le condizionalità dello stage-1 (t-periodico, slip-free,
   cl(Ω_march)) sono ipotesi DICHIARATE del teorema, non approssimazioni
   [W2-R9]. S-PRES arma il trigger del write-up: lo stato parziale va
   dichiarato.
3. **La biforcazione come slide centrale** (T-T7RED THEOREM / T-T4 THEOREM* /
   sharpness): solo-ε ⇒ i metodi coincidono (con la media pesata); plug pieno
   ideal-adapted ⇒ il design di picco è ottimo; troncamento/caps ⇒
   max∫ < ∫max strictly e nasce PB-2. Il messaggio: sappiamo ESATTAMENTE dove
   il design a stato medio basta e dove no.
4. **Il fatto di design centrale** (SCHEMA, T-T7FS(b), M0:2827-2829):
   "nessuna fase soddisfa la propria wall condition — la media μ sì; la
   parete cycle-optimal non è la parete ottima di alcun punto operativo."
   Con il boxed warning: fuori T3 la media naive è SBAGLIATA (P1:96-104).
5. **Novità solo query-bounded** (NOT-FOUND(q), litmap G1/G5/G6 + caveat
   D-06): mai "nessuno ha mai posto il problema"; la formula bloccata PB-2 e
   la lista caveat (K-O 1970, Efremov-Kraiko 2004, P0 non letti) si portano
   in backup slide.
6. **Un solo numero in-class, con le sue barre** (dato misurato con caveat,
   M0:4207-4234 + literature_registry:568): +0.51% in-class (caveat
   dichiarati, INCLUSO il band-underinclusion di record: bound sistematico
   grezzo ~6e4 vs surplus 2.0407e5, ~30% del datum — se il numero va su
   slide, quel caveat È parte del numero, M0:4216-4219 [W2-R2]) contro la
   scala 0.04–0.34% del premio Rao classico (numeri
   loro, CT-6); il gap PB-2 vero = OPEN, e dirlo è parte del messaggio di
   rigore.

---

## 6. STORIA — trittico condizionale [V2-R2] (writer B8a, W-B.2, 2026-08-23)

Convenzione: ogni battuta porta DATA + PROCESSO + VERDETTO (vincolo §5-bis);
le ancore di Fase A/B puntano a `validation/sfoundations_raws_2026-08-13/`
(alberi ciechi datati 2026-08-17, `phaseB_tree_diff.md` 2026-08-17). Nessuna
ancora di Fase A è asserita dove non esiste (F-des-3).

**T-1. Il pin dati (onda rotante periodica pura, monitor T0-flatness).**
- *Battuta 1 — derivazione originale*: 2026-07-16, sessione S6, addendum
  utente di record — commit `ac78ec0` "periodic-wave standing scope +
  algorithmic pins of record" (pin in M0 VI.4bis; enunciato M0:995).
  PROCESSO: pin utente dichiarato + amendment M0 (`f28cb03` stesso giorno,
  "M0 VI.4bis full-generality amendment"). VERDETTO: MODEL HYPOTHESIS
  dichiarata, senza provenienza hardware (R20).
- *Battuta 2 — seconda prova*: (c) **NON-RIDERIVATO: questo aspetto non ha
  avuto riderivazione agnostica di record** — è un PIN utente, per
  costruzione fuori dal perimetro derivativo di Fase A. Doppia prova
  alternativa: pricing dei boundary nel blocco [S-T0P] (M0:560-561,
  refutazioni 2026-08-17/19, `phaseD/VERDICT_phaseD_proofs1.md` +
  `r2pass/VERDICT_doc1_rev10.md`) + monitor T0-flatness ARMATO come campo
  obbligatorio del data contract (VI.4bis(v)) + routing fuori-pin a PB-5
  (M0:108-114). PROCESSO: refuter Fase D che trattano il pin come ipotesi
  prezzata; VERDETTO: ipotesi dichiarata con rejector armato, mai promossa.
- *Battuta 3 — convergenza*: scope ri-affilato 2026-08-11 (finestra
  POST-S21, corrector re-scoped a perturbazione dello sweep steady, memoria
  `periodic-wave-data-scope`; M0 VI.4bis(ii) :3145-3150). Classe finale:
  MODEL HYPOTHESIS + DEFINITION del monitor.

**T-2. [D-MU] e il rung 2 (unica approssimazione O(St)).**
- *Battuta 1*: 2026-07-16 — commit `7255e00` "program baseline: M0 master +
  D1-D7" (D2.3 [D-MU], J = ∫F dμ; ladder rung in D6/problem book).
  PROCESSO: derivazione single-author al baseline M0, con carrier
  quantitativo T3/T4 vs S-H Table 1 lo stesso giorno (`e800a19`).
  VERDETTO: DEFINITION + passo quasi-steady prezzato (P4).
- *Battuta 2*: (a) RIDERIVATO-PIENO — Fase A/B 2026-08-17: item 1
  "Steadification exactness (T-T0 road)" (`phaseB_tree_diff.md:315`,
  H-F1(b) ri-deriva) + item 2 "Rao-collapse under averaging (T7 road)"
  (`:325`, H-F35). PROCESSO: 4 alberi ciechi de-novo → diff vs record;
  VERDETTO: CONVERGENT (theory-layer validations §3).
- *Battuta 3*: classe finale DEFINITION [D-MU] + O(St) prezzato P4
  (M0:444-450); correttore G3-owned, mai quantificato — dichiarato in
  forchetta (i) al landing C4 (2026-08-21).

**T-3. Stage-1: per-fase = quoziente esatto ([S-T0P] → [T-T0P]).**
- *Battuta 1*: esattezza T0 al baseline 2026-07-16 (`7255e00`; consumata
  dalla remark EAP `95d54de` stesso giorno, T0(i) "area avg = time avg");
  forma a due stadi con aggiunto naive DEGENERE = riparazione REFUTE_A
  2026-08-13 (sessione litreview-confrontation/F-SERVICE;
  `docs/claims_registry.yaml:1903`). PROCESSO: derivazione + riparazione
  carrier da confronto avversario con la letteratura. VERDETTO: [S-T0P]
  SCHEMA con route di prova nominata.
- *Battuta 2*: (a) RIDERIVATO-PIENO — doppia gamba: Fase A/B 2026-08-17,
  H-F1(b) ri-deriva la steadificazione (`phaseB_tree_diff.md:315`); Fase D
  proof loop 1 (S-T0P), giudice `phaseD/VERDICT_phaseD_proofs1.md`
  (2026-08-17, 3 round × 2 lenti) → doc1 rev10 DRY di record 2026-08-19
  (`r2pass/VERDICT_doc1_rev10.md`, S-FOUNDATIONS-C2). PROCESSO:
  derivazione de-novo + refutazione until-dry con giudice. VERDETTO:
  [T-T0P-E] THEOREM (metà equivarianza); main statement ATTERRATO.
- *Battuta 3*: landing M0 2026-08-19 (M0:602-628): [T-T0P] SCHEMA sui due
  strati con gap G1-G12 e tre boundaries (t-periodico, cl(Ω_march),
  slip-free); write-up S1 resta owed (findings :1450-1458, trigger armato
  da S-PRES stessa). Classe finale: SCHEMA + THEOREM parziale, dichiarati.

**T-4. Contratto D2.4, ladder I0-I4 e default L4.**
- *Battuta 1*: 2026-07-16 al baseline M0 (`7255e00`, D2.4 + ladder);
  L4-DEFAULT OF RECORD 2026-08-06 (S16 [RIGOR/B], ledger pass 2, commit
  `0b26dc7`; M0:125) e FRONT-CHAIN COMPLETION 2026-08-06 (S16 [RIGOR/A],
  M0:221) con forma normale-meridiana m_n e split (M-a)/(M-a')
  (M0:139-169). PROCESSO: campagna fondazioni S15/S16 (hypothesis ledger
  con discharge). VERDETTO: DEFINITION/contract + [T-NSW] THEOREM.
- *Battuta 2*: (a) RIDERIVATO-PIENO — Fase A contract-blind 2026-08-17:
  brief cieco `contract_blind_brief.md` + doppia derivazione
  (`contract_blind_data.md`/`contract_blind_pde.md`), giudice
  `VERDICT_contract_and_L4R1.md` (2026-08-17); più item 3 "Certified
  solution class (D2.5/S1 road): 4/4 trees" (`phaseB_tree_diff.md:330`).
  PROCESSO: derivazione cieca + verdetto giudice. VERDETTO: CONVERGENT;
  L4⇒R1 formalizzato in Fase D (`phaseD_L4_implies_R1.md`, 2026-08-19).
- *Battuta 3 — convergenza* [fix ST-C5-02]: DATA: 2026-08-06 (S16,
  FRONT-CHAIN COMPLETION + ledger pass 2, commit `0b26dc7`). PROCESSO:
  campagna fondazioni [RIGOR/A]/[RIGOR/B] con hypothesis-ledger discharge.
  VERDETTO: R1 CONDIZIONATA alla finestra W1-W4 di record (M0:139-169);
  classe finale come stampata in §2.

**T-5. La biforcazione: T-T7RED / T-T4 / sharpness (PB-2).**
- *Battuta 1*: nucleo al baseline 2026-07-16 (`7255e00` + check
  quantitativo T3/T4 `e800a19`); demozione delle forme chiuse a oracoli
  2026-07-16 (`ef0af1d`, "closed forms demoted to oracles" — la forma
  primaria di T-T7RED diventa l'inversione reale); T-T4 corretto in S14
  (PAN-S14 addendum 2026-08-04, arbiter-confirmed, M0:397). PROCESSO:
  derivazione + panel D8 (2026-07-22, 16/16 CONFIRMED) + correzione
  arbiter. VERDETTO: [T-T7RED] THEOREM; [T-T4] THEOREM* sotto [C-HT4].
- *Battuta 2*: SPLIT per gamba. T-T7RED: (a) RIDERIVATO-PIENO via T7-road
  H-F35 (`phaseB_tree_diff.md:325`, 2026-08-17). T-T4: (c)
  **NON-RIDERIVATO: questo aspetto non ha avuto riderivazione agnostica di
  record**; doppia prova alternativa = panel PAN-S14 arbiter-confirmed
  (2026-07-22/2026-08-04) + carrier X-GRP06/10/12 + falsificatore O2 vivo
  (`docs/claims_registry.yaml:339`). Clausola di SHARPNESS (max∫ < ∫max
  strictly): (c) NON-RIDERIVATO e **doppia prova: ASSENTE** — enunciata di
  record senza prova scritta (W2-R4, M0:2316-2319) e il carrier
  quantitativo PB-2 è OPEN mai eseguito = **FINDING dichiarato**
  (inventario `HISTORIAN_INV_a.md`).
- *Battuta 3 — convergenza* [fix ST-C5-02]: DATA: 2026-08-04 (PAN-S14
  addendum, correzione T-T4 arbiter-confirmed, M0:397). PROCESSO: panel a
  convergenza + arbiter sul claim register. VERDETTO: classi finali come
  §2; PB-2 resta il primo problema aperto del programma
  (problem_book:532-536), nessuna data di record — dichiarato.

**T-6. [T-T3-MAP] — la coincidenza cycle-vs-steady rifiutata come teorema.**
- *Battuta 1*: 2026-08-11, S-GAUNTLET — breaker map of record (M0:879;
  advisory `ADVISORY_Sgauntlet_generality_ledger_2026-08-11.md`).
  PROCESSO: gauntlet avversario sulla generalità del ledger. VERDETTO:
  SCHEMA container, claim generale RIFIUTATO, corner T-T3-SI provato.
- *Battuta 2*: (c) NON-RIDERIVATO in Fase A come mappa; doppia prova
  alternativa = S18 five-line hypothesis audit, precondizione NOMINATA del
  clause S18 ESEGUITA in S24 T2a (2026-08-12, M0:4138-4140; log
  `validation/PROGRESS_2026-08-12_S24_f1b.md`). PROCESSO: audit
  pre-registrato su record S18. VERDETTO: corner-reading qualificata retta.
- *Battuta 3 — convergenza* [fix ST-C5-02]: DATA: 2026-08-12 (S24 T2a:
  precondizione nominata PERFORMED, M0:4138-4140). PROCESSO: audit
  pre-registrato delle 5 ipotesi del clause S18 + qualificatori
  corner-reading portati. VERDETTO: classe finale SCHEMA container con
  classi per clausola (claims:316-327); carrier CARRIER-A..E dispatch
  F5a/F2/F2a.

**T-7. Riga H (licensing), [S-GBE] e B-lite.**
- *Battuta 1*: tabella di licenza in M0 Parte V con la riga caotica
  arbiter-annotata al panel S14 (2026-07-22/2026-08-04: named missing
  lemma); [S-GBE] RESOLVED 2026-08-06 (S16 T4,
  `docs/rde_nozzle_GB_ergodic.md`, M0 riga :3016); [S-BLITE] addendum
  2026-07-21 (S12, commit `592107d` [F2-prep/BLITE]; M0:3027-3044).
  PROCESSO: panel + campagna S16 con lemma scritto. VERDETTO: muro
  ergodico SCRITTO, etichetta quasi-steady-only LIFTED.
- *Battuta 2*: (c) NON-RIDERIVATO in Fase A (la ladder di licenza non è
  nel perimetro degli alberi). Doppia prova alternativa per [S-GBE]:
  carrier eseguibile X-GBE PASS (`docs/claims_registry.yaml:1843-1864` —
  il PASS del carrier vive a :1856-1860 [fix ST-C5-01]).
  Per B-LITE: **doppia prova: ASSENTE** — [S-BLITE] è SCHEMA con brick
  nominato G12-L1-3D MAI eseguito (M0:3037-3044) = **FINDING dichiarato**
  (inventario). PROCESSO: censimento storico di questa battuta,
  2026-08-23. VERDETTO: dichiarazioni come stampate, nessuna promozione.
- *Battuta 3 — convergenza* [fix ST-C5-02]: DATA: 2026-08-06 (S16 T4,
  [S-GBE] RESOLVED — named missing lemma SCRITTO, etichetta
  quasi-steady-only LIFTED). PROCESSO: campagna S16 [RIGOR/A] con lemma +
  carrier X-GBE (`docs/claims_registry.yaml:1843-1864` [fix ST-C5-01]).
  VERDETTO: classi finali: tabella M0 V per riga (THEOREM…SCHEMA/PRACTICE,
  rifiuto onesto sulla riga caotica); [S-GBE] SCHEMA con carrier PASS;
  [S-BLITE] SCHEMA con brick nominato.

---

## 7. POSIZIONAMENTO / CONFORMITY (cella A-ii — residuo; owner B3) [B3-P7]

Residuo dichiarato in §M: la classe-spline è nel ledger (coperta CH4
§1.3); QUI il confronto con il censimento mondiale delle parametrizzazioni.

**(a) STRUMENTI — classe di base del design vs il censimento mondiale.**
- *Mondo-SOTA (id registry)*: `masters_etal_2017` — confronto geometrico
  sistematico delle parametrizzazioni airfoil: B-spline ~42 dv medi
  (range 28-72) per convergenza one-count, correlazione lineare errore
  geometrico/errore di forza, tolleranza Kulfan/CST insufficiente di >1
  ordine; `lauer_ansell_2025_pas` — censimento parametrizzazioni 2025,
  prior 20-25 dof (LL-28: trasferimento a ugelli MoC = scope DICHIARATO,
  non nostro claim).
- *Cosa usiamo*: C1 incumbent = cubica interpolante clamped/natural,
  heights-as-dofs, VERDICT-BEARING; direzione di migrazione convergiuta
  (WAVE-2 2026-08-19) = chart B-spline control-polygon dello STESSO
  spazio spline certificato, con certificati di ammissibilità
  Bernstein-exact (`docs/choice_ledger.yaml:164-174`).
- *Perché*: i certificati di ammissibilità (R5) vivono sullo SPAZIO, non
  sul chart — la migrazione di chart non tocca la classe certificata; il
  prior esterno di dof-budget (28-72 dv) incornicia il nostro conteggio
  con scope di trasferimento dichiarato (2-D external-aero Euler, mai
  bound program-side — retro-sweep 2026-08-20); il confronto con le
  alternative censite è aggiudicato a livello ledger, non per preferenza.

**DECISION CARD — C1 "Design basis class" (6 campi, §1g):**
1. **Scelta**: C1 (`docs/choice_ledger.yaml:164-174`) — base del design:
   cubica interpolante clamped/natural, heights-as-dofs (incumbent
   verdict-bearing); direzione convergiuta: migrazione al chart B-spline
   control-polygon dello stesso spazio certificato.
2. **Alternative censite (data+fonte)**: B-spline control polygon
   (de Boor/Boehm), CST (Kulfan), Hicks-Henne — censite dall'annex S24
   gapmap (2026-08-12, `validation/ADVISORY_S24_sota_gapmap_2026-08-12.md`)
   e ri-aggiudicate WAVE-2 S-FOUNDATIONS (2026-08-19,
   `validation/sfoundations_raws_2026-08-13/blocco3/VERDICT_wave2.md#4.5`);
   prior dof-budget `masters_etal_2017` (retro-sweep 2026-08-20);
   censimento 2025 `lauer_ansell_2025_pas` (harvest C4, 2026-08-20).
3. **Verdetto + perché**: adjudicated-split, enum MIXED — la direzione è
   convergiuta (chart B-spline = nuovo asse dei certificati
   Bernstein-exact) ma l'incumbent resta verdict-bearing finché i tre
   falsificatori di migrazione non passano; il rigetto D6 S20 del
   control-point SWITCH resta intatto sul suo asse (era un cambio di
   spazio, non di chart).
4. **RECENCY/SOTA check**: survey aggiudicata 2026-08-19; copertura
   letteratura fino al censimento 2025 (`lauer_ansell_2025_pas`);
   prior Masters con scope di trasferimento dichiarato; nessun censimento
   più recente in registry al check 2026-08-23.
   **ATTUALE(registry 174 + corpus wave-2, 2026-08-23)**.
5. **Falsificatore**: i tre falsificatori di migrazione della riga C1 —
   il primo ri-pinnato sulla chart innocent-data response con pin
   conversion-map; più il rejector di oscillazione dell'asse D6.
6. **Trigger di ri-esame (finestra)**: duty F2-C1-CONTROL-CHART-MIGRATION
   (items 0-6 + driver leg; GAP-21 carrier) — **finestra F2-entry**.

**(b) SENSO.** I precedenti del tema: la scuola classica arriva a
Bezier-chart + GA (LL-29, Kraiko 2016 — il LORO dato: l'exact batte i GA,
evidenza PRO la rotta certificata) e la comunità aero ai censimenti di
parametrizzazione (LL-28); nel corpus letto NESSUNA riga porta la
parametrizzazione DENTRO un problema di forma mediato a misura pinnata —
claim di assenza LEDGER-BOUNDED (join sulle righe N-20 del
LINEAGE_LEDGER: LL-27/LL-28/LL-29, matrice W-B.0 20×82 a celle rese;
lint 7; §3-bis/N-A) [fix WB1-C3-03].

**(c) STANDARD DI RIFERIMENTO.** Asse **§C-7** (verifica multi-livello,
classe journal-review avversaria): la scelta C1 è passata per panel a
convergenza + refuter con burden esplicito (WAVE-2), criterio di
conformità = riga ledger con evidence/owner/falsificatori; divergenza
dichiarata: reviewer interno a convergenza, il passaggio esterno resta
G5/JPP. Asse di supporto **§C-3** (tracciabilità ECSS/DO-178C-class):
catena id→ledger→duty F2 con carrier e rejector.

---

## Disposizione riparazioni (onda 2)

Riparatore W2, 2026-08-23. Ogni ancora citata dal refuter è stata aperta e
verificata prima dell'edit (read-then-quote: M0:602-628, M0:4207-4236,
M0:139-169, M0:2303-2319, P1:96-104, litmap:19-24, findings_registry:1450-1458).

| Finding # | Classe | Disposizione |
|---|---|---|
| 1 | REPAIR (ALTA) | APPLICATO [W2-R1] — §1.3 (main statement [T-T0P] landed + tre boundaries), §3.1 (riconciliazione owed/landed), Q5 (risposta pre-cotta slip-sheets), Q6 e §5.2 (stato landed citato) |
| 2 | REPAIR (ALTA) | APPLICATO [W2-R2] — caveat band-underinclusion (~6e4 vs 2.0407e5, M0:4216-4219) aggiunto in Q1 e §5.6 |
| 3 | DOWNGRADE (MEDIA) | APPLICATO [W2-R3] — Q1 riformulata: "ZERO per teorema" scoped al corner provato T-T3-SI; nella classe T3 collassa il PESO (P1:96-104) |
| 4 | REPAIR (MEDIA) | APPLICATO [W2-R4] — Q4: strictness = clausola enunciata SENZA prova scritta (ipotesi implicita mu({xi: l(xi) > L}) > 0 non enunciata); write-up = finding da mintare |
| 5 | REPAIR (MEDIA) | APPLICATO [W2-R5] — §1.1: forma normale-meridiana m_n di record + split (M-a)/(M-a') + finestra R1 W1-W4 (M0:139-169); "assialmente supersonica" = caso planare |
| 6 | GAP (MEDIA) | APPLICATO [W2-R6] — glossario §0 in testa (T3/collasso, S1, rung 1/2/3, DEF, Table-1) |
| 7 | NOTE (BASSA) | APPLICATO [W2-R7] — migliora senza rischio: ancora spostata su litmap:23, quantificatore ammorbidito e marcato [REP survey / query-bounded] |
| 8 | NOTE (BASSA) | APPLICATO [W2-R8] — migliora senza rischio: §3.1 riconcilia owed vs landed e segnala la staleness dell'ancora findings_registry:1455 come manutenzione fuori scope S-PRES |
| 9 | NOTE (BASSA) | APPLICATO [W2-R9] — migliora senza rischio: §5.2 scoping "catena DI FORMULAZIONE" + condizionalità stage-1 = ipotesi dichiarate, non approssimazioni |

---

## DECK FEED

Asserzioni candidate-slide (assertion-evidence: frase piena + ancora +
classe), compilate per lo storyboard v3 — che joina QUI, non ri-legge il
capitolo (contratto §3 emendamento).

1. "La pratica pubblicata del campo disegna a I4 (average-first,
   design-second); il programma vive a I2/I3 con misura μ pinnata." —
   litmap:23 (riga G5) + M0:122-124 — [REP survey query-bounded] +
   DEFINITION.
2. "Per-fase = quoziente esatto + UNA sola approssimazione dichiarata
   O(St), con le condizionalità stage-1 (t-periodico, slip-free,
   cl(Ω_march)) come ipotesi stampate." — claims:1903; M0:533-628;
   M0:444-450 — SCHEMA + [T-T0P-E] THEOREM.
3. "Sappiamo ESATTAMENTE dove il design a stato medio basta e dove no:
   solo-ε ⇒ coincide (con la media PESATA); plug pieno ideal-adapted ⇒
   design di picco; troncamento/caps ⇒ max∫ < ∫max STRICTLY (PB-2)." —
   claims:381-392, 329-340; M0:2316-2319 — THEOREM / THEOREM* / clausola
   di sharpness (senza prova scritta, dichiarato).
4. "Nessuna fase soddisfa la propria wall condition — la media μ sì; fuori
   T3 la media naive è SBAGLIATA." — M0:2827-2829; P1:96-104 — SCHEMA
   [T-T7FS] + boxed warning di record.
5. "EAP contenuta e completata: il correttore P4 è la barra d'errore
   mancante di EAP." — M0:2526-2544 (`kaemming_paxson_2018`) — remark
   [IO] di record.
6. "La licenza segue il FLUSSO, non il metodo: single-wave → certificato
   pieno; RPO → PRACTICE; multistabile → layer robusto; caotico → RIFIUTO
   ONESTO + muro [S-GBE]." — M0:3008-3016; claims:1843-1854 — classi per
   riga (THEOREM…SCHEMA/PRACTICE), canali residui in tabella §1.7.
7. "Il campo non dichiara il regime di validità della propria media:
   NOT-FOUND(q) sul perimetro chiuso; unica istanza adiacente K-O 1970,
   footnote dichiarata ma unpriced." — CH1 §1.7 H-iii; litmap:141-142 —
   NOT-FOUND(q) query-bounded.
8. "B-lite è il metro esatto CHEAP dello sweep rung-2: campo wave-frame
   esatto a costo di march, adjoint verbatim." — M0:3027-3044 (verbatim
   :3037-3038) — [S-BLITE] SCHEMA con brick nominato G12-L1-3D.
9. "Un solo numero in-class: +0.51%, CON il band-underinclusion (~30% del
   datum) stampato accanto — contro la scala Rao 0.04-0.34% (numeri loro,
   CT-6)." — M0:4207-4234, 4216-4219; literature_registry:568 — misura
   con caveat dichiarati.
10. "Ogni claim di primato in forma bloccata D-06, con K-O 1970 citato e
    i P0 non letti dichiarati." — M0:2320-2350 — regola di record
    (guardia 9/13).
