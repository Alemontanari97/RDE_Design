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
