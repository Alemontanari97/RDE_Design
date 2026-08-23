# CH6 — Value case, onestà e roadmap: Gap A/Gap B, PB-2, deciders, ask

Capitolo di ricostruzione S-PRES (2026-08-22/23). Stadio di confronto: M0,
registries (claims/findings/choice), pipeline decision map, PROGRESS, checkpoint
S-FOUNDATIONS; [WB1] + checkpoint S-PRES (abbreviato **CKP-S** =
`validation/spres_raws_2026-08-22/SESSION_STATE_checkpoint.md`, correzioni
utente C-3/C-3bis/C-3ter di record 2026-08-23) e piano D6
(`docs/rde_nozzle_development_plan.md`). Nota di lettura: "checkpoint" NUDO in
questo capitolo = il checkpoint S-FOUNDATIONS
(`validation/sfoundations_raws_2026-08-13/SESSION_STATE_checkpoint.md`), come
nelle ancore già poste; il checkpoint S-PRES è SEMPRE citato CKP-S. Questo
testo NON aggiudica nulla di nuovo: ricostruisce, ancora,
dichiara gli aperti. Ogni claim porta ancora (file:riga) e classe di rigore.
Consumo dichiarato: storyboard v3, banca Q&A red-team, mappa F2+.

---

## 1. Ricostruzione

### 1.1 Il frame di valore: Gap A / Gap B (la domanda "quanto vale il programma" resa decidibile)

Il value case del programma è stato registrato nella finestra S-FOUNDATIONS-C4
come frame a due gap, ancora S-PRES dichiarata
(`validation/sfoundations_raws_2026-08-13/SESSION_STATE_checkpoint.md:466-472`):

- **Gap B** = J3D(x\*_pf) − J3D(x\*_legacy): la differenza di valore tra il design
  della nostra funzionale per-fase mediata e il design legacy
  (Veen/Angelino-at-mean), **misurabile IN-HOUSE a costo basso** con un
  paired-run F2 ("measurable IN-HOUSE cheap (paired-run F2 demo, our functional
  vs Veen/Angelino-at-mean)", checkpoint :468-469). Classe: quantità DEFINITA di
  record, valore MAI computato (vedi §3, A-1).
- **Gap A** = distanza dall'ottimo 3D vero, che è **INCOMPUTABILE**
  ("the UNCOMPUTABLE true 3D optimum", checkpoint :469-470): trattato
  bounded-only via lo schema delta/mu + spot-check R22-CFD.
- **Value condition di record**: "Gap B material AND Gap A < Gap B"
  (checkpoint :471-472). Il programma vale se il salto misurabile è materiale E
  se ciò che la riduzione non vede è più piccolo del salto.

Due guardie di formulazione accompagnano il frame:

1. **Wording guard (user catch, sustained)**: "best-of-sweep != argmax — NO
   paper ever optimized the true 3D case (no optimizer in any of the 4; P-M =
   hand-guided redesign)" (checkpoint :472-476; forma di record in M0:
   [ORCH-HARV-1], `docs/rde_nozzle_MASTER.md:1335-1339`, [ADV]). Nessun
   confronto in letteratura è un confronto con un argmax.
2. **Lo schema del bound di Gap A è SCHEMA, non numero**: la cella (vi) della
   forchetta dichiara "**delta AND L_H UNDERIVED — NO argmax-shift number exists
   at any grade, and none from the measured carrier alone**"
   (`docs/rde_nozzle_MASTER.md:1348`), con falsificatore armato nel claims
   registry: "any argmax-shift number quoted at any grade from this schema
   before delta/L_H land" = violazione (`docs/claims_registry.yaml:2262`).

Lo strumento di onestà che porta il frame è la **forchetta a 6 canali**
(M0:1341-1348), con regole di cella vincolanti: "bound-or-estimate declared;
rigor class per bound; provenance per number; ... NO cell above its held
evidence class" (`docs/rde_nozzle_MASTER.md:1306-1309`). Classe della tabella:
mista, dichiarata cella per cella (SCHEMA/THEOREM\*/[SE]/[REP]/[ADV]).

### 1.2 PB-2: il flag problem, e perché non è ancora un numero

PB-2 è il problema-bandiera del problem book
(`docs/rde_nozzle_problem_book.md:532-537`): "PB-1 for configuration (ii) with
L_p < l(ξ_peak) and a base-pressure closure: T4's nesting fails, max∫ < ∫max
strictly; compute the cycle-optimal truncated plug vs peak- and mean-designed
baselines (Table-1 states). This is the first concrete problem NOT solved by
any single-phase design." È il punto dove la media del ciclo produce un ottimo
GENUINAMENTE diverso da ogni design a fase singola (rottura del nesting di T4:
la sharpness clause del teorema di nesting — "a length cap L < l(xi_peak), a
base-pressure model at a truncation plane, or non-ideal adaptation break the
nesting: then max Int < Int max STRICTLY" (`docs/rde_nozzle_MASTER.md:2316-2319`)
[W2-R6]. **Classe, forma riconciliata a CH1 Q4 [WB1-R1] (critic 10)**: il
NESTING (la parte positiva) è provato — THEOREM 6 [T-T4], classe THEOREM*
sotto la chiusura di ideal-adaptation [C-HT4] (M0:2303-2315); la frase
"the nesting and the constrained-KKT structure are THEOREM (standard)"
(M0:3524-3525) copre il nesting e la struttura KKT vincolata, NON la
strictness; la **STRICTNESS sotto troncamento/caps è clausola ENUNCIATA di
record DOPO il QED ma SENZA prova scritta** (nemmeno l'ipotesi implicita
mu({xi: l(xi) > L}) > 0 è enunciata — CH1 Q4 [W2-R4],
`CH1_formulation_ladder.md:511-530`, range post-estensione W-B.1 di CH1
[WB1-C3-13 riparato]); il carrier quantitativo è PB-2 (OPEN);
il numero PB-2 stesso: **MAI computato** — nessuna riga (value,delta)
truncated-plug esiste nel record, vedi trigger C61 sotto. Su slide (e in
storyboard C7-ter, canale orchestratore): "qui la differenza è la struttura"
si dice SOLO nella forma "nesting provato; strictness = clausola senza prova
scritta; carrier = PB-2 OPEN").

**Guard di priorità sulla bandiera (locked formulation D-06)** [W2-R5]: la
forma di record del claim di novità è VINCOLATA — "PB-2 LOCKED FORMULATION OF
RECORD (D-06, 2026-08-13 — never abbreviate): 'the first genuinely averaged
and NON-COLLAPSING shape problem of the program (a CYCLE instance)'. Any
phrase of the type 'the first averaged-thrust variational problem' is DEAD of
record: Efremov-Kraiko 2004 poses a period-averaged maximum-thrust variational
problem, Kraiko-signed, with measure Int_0^1 ... dt (Eq. 1.7, p.624)
[page-verified]" (`docs/rde_nozzle_MASTER.md:2320-2326`). Efremov-Kraiko non
tocca PB-2 perché non ha wall contour (incognite = funzioni temporali dello
stato d'uscita + scalari W, Q) e il suo ottimo COLLASSA (M0:2326-2329) — è il
query-bound esplicito del claim di novità, da portare in slide con la bandiera.

Cosa serve per computarlo, dal record:

- **Baseline mean-designed**: il confronto richiesto da PB-2 è "vs peak- and
  mean-designed baselines" (:535). La baseline media è I4 del problem book:
  "I4 (single mean state): one state (⟨Pc⟩, T0, γ); classical Rao/GENO design"
  (`docs/rde_nozzle_problem_book.md:211`), con la nota "WITHIN I3's other
  hypotheses, I4 is not an approximation but EXACT" (:213). Attenzione alla
  distinzione: la baseline di record del paired-run di Gap B è "our functional
  vs Veen/Angelino-at-mean" (checkpoint :468-469), mentre I4 è "classical
  Rao/GENO design" (:211) — sono design legacy DIVERSI. L'idea di un twin
  famiglia-vs-I4 sullo STESSO engine che serva anche Gap B è una PROPOSTA di
  consolidamento di questo capitolo (una run, due baseline mean-designed:
  Rao/GENO-at-mean = I4 e Veen/Angelino-at-mean = legacy praticato), NON una
  identificazione di record. [W2-R2]
- **Chiusura p_b**: lo slot N2 è DICHIARATO e NON aggiudicato. C61
  (`docs/choice_ledger.yaml:818-830`): status **NEVER**; incumbent = "the Veen
  constant closure p_b = 0.846 p/M^1.3 is practiced in the LEGACY chain only
  ... the program's own p_b is a DECLARED SLOT, not a model" (:820); tra le
  alternative il verdetto WG10 "N2 MUST REPLACE IT" (:824). Trigger: "first
  truncated-plug (value,delta) row entering the record, or F4b window entry"
  (:829). Il blocco è registrato anche come finding:
  `docs/findings_registry.yaml:2092-2101`
  (litreview:residue-r8-r23-base-pressure-pb2-blocking): Pb/Pa=1 inammissibile
  in entrambi i regimi, transizione Pa/Pc~0.15, e "no measurement of a
  TRUNCATED-plug RDE base exists ... nozzleless->truncated-plug transfer is an
  ANALOGY, not a measurement" ([REP] sul dato, ANALOGIA dichiarata sul transfer).
- **Il warning Humphreys sul p_b** (perché la chiusura non è un dettaglio):
  scambiare il modello di p_b "moved the optimum base height ×2.45 (0.954 →
  2.34 in) and the tip wall slope −13.26° → −3.08° while moving thrust only
  +0.26% — the p_b closure moves the ARGMAX at O(1) with the VALUE nearly flat"
  (M0 [ORCH-HARV-3], `docs/rde_nozzle_MASTER.md:1455-1464`, classe [ADV];
  numeri = di Humphreys-Thompson-Hoffman 1971, CT-6). Stessa lettura nel note
  C61: "The Humphreys x2.45 argmax sensitivity is channel-(vi)-shaped, i.e.
  FOUNDATION-grade: the closure choice moves the DESIGN, not just the value"
  (`docs/choice_ledger.yaml:830`).

### 1.2-bis Quale gap domina, su quale asse? (nodo N-Q, first-level — C-3/C-3bis/C-3ter) [WB1-R2]

[Sorgente normativa: blocco C-3/C-3bis/C-3ter di CKP-S :198-254 —
correzioni utente di record 2026-08-23, portate ALLA RIGA (mai parafrasi
a memoria). Nodo N-Q istanziato dall'emendamento v2.1 §1d: albero a 22
nodi, N-Q agganciato DIRETTAMENTE a Q0 (first-level, accanto ai rami
R-I..R-IV — è LA domanda di valore che li attraversa). Celle servite
qui: Q-i, Q-iii, Q-iv; Q-v in §3 (A-9); Q-ii = F-P dichiarata (§7(a)).]

**(i) Il frame three-design (la spina del value case del deck).** Tre
design, tre gap (CKP-S:198-204): **x\*_mean** = design classico sul dato
medio — il comparatore è I4 (§1.2), e di record "I4 comparator has ZERO
computed instances" (CKP-S:198-199); **x\*_pf** = il nostro (ottimo
della famiglia per-fase); **x\*_3D** = l'ottimo 3D vero,
"uncomputable" (CKP-S:200). I tre gap, verbatim (CKP-S:200-202):
"Gaps: formulation (never computed, PB-2/twin), model (= Gap A, no
number, delta/L_H underived), composition (field controls NOTHING)".
Lettura dichiarata del terzo asse [INF]: le coppie del frame sono tre —
mean↔pf (formulazione), pf↔3D (modello), mean↔3D = la COMPOSIZIONE dei
due, il gap in cui il campo vive senza controllarne alcun pezzo.
**Nota di mappa OBBLIGATORIA (collisione di lettere)**: le etichette
C-3bis qui sotto — gap(A) = pf-vs-mean, gap(B) = pf-vs-3D — hanno le
lettere SCAMBIATE rispetto al frame di valore §1.1 (Gap B = salto
misurabile pf-vs-legacy; Gap A = distanza dal 3D): gap(A)~Gap B,
gap(B)~Gap A; C-3bis è la forma A LIVELLO ARGMAX della value condition
— "= the value condition at argmax level" (CKP-S:229-230). La domanda
utente di record è FIRST-LEVEL TREE NODE: "which gap dominates, on
which axis?" (CKP-S:202-204).

**(ii) WORKING HYPOTHESIS (dichiarata e falsificabile — mai teorema).**
Forma finale C-3bis a vincoli fissi (CKP-S:215-230; la forma precedente
mescolava gli assi eps-free vs constrained — "user catch correct",
CKP-S:216-217): a (eps,L) FISSI e settore fisso, l'argomento
STRUTTURALE ("declared hypothesis, not theorem", CKP-S:218-219) è
asimmetrico:

- **gap(A) pf-vs-mean NON ha teorema di soppressione**: "it is fed at
  FIRST order by Jensen on the Hadamard shape density G(x;s) over 10:1
  data excursions (shared-wall integrand nonlinear in s)"
  (CKP-S:219-222).
- **gap(B) pf-vs-3D ha TRE teoremi di soppressione** che ne uccidono i
  primi ordini SULLA PARTE LISCIA: "[T-T0P] exact steadification
  in-pin; K-bar=0 fiberwise; T-DISC full-state exoneration"
  (CKP-S:222-225), coi primi ordini residui "CONFINED to named
  channels" (CKP-S:225-226).

Quindi "PLAUSIBLY |x\*_pf − x\*_mean| > |x\*_3D − x\*_pf| at fixed
constraints" (CKP-S:228-230): plausibilmente **(A) > (B) in-settore** —
enunciato VALIDO SOLO insieme al tallone (J) del punto (iii), mai da solo
(guardia 1). Entità del gap di formulazione: "entity FULLY OPEN"
(CKP-S:206-207).
Fuori settore la mappa si ribalta: "model gap dominates CROSS-SECTOR
risk (swirl-breaker shroud 13+ pts, anti-spike ~1-4% predicted family
gap, STRUCTURAL-only)" (CKP-S:207-209) — le minacce a scala di
configurazione "act BETWEEN configurations, less in-play at fixed
sector" (CKP-S:227-228).

**(iii) REGOLA C-3ter — la gerarchia MAI senza il tallone (J)
(guardia 1); perimetro dei teoremi e canali residui con classe
(guardia 16 [GV-4]).** Il perimetro: i tre teoremi coprono "the
SMOOTH/advective part" (CKP-S:245-246). Il fronte obliquo rotante
(helical sheet) è visto dal per-fase solo come "the DATA-ANCHORED
SHADOW x_s(xi) (per-phase meridional trace)"; NON visti: "the azimuthal
obliquity of the jump + azimuthally-fed interior segments (unreachable,
E4/E5) + the slip-line behind it (G9: slip-sheets OUTSIDE T0P scope,
'physically generic RDE front type')" (CKP-S:238-245). I canali residui,
enumerati con classe:

- **(J) front jumps** — "IS the un-suppressed first order of gap(B) —
  no number (SBV-conditional, delta underived)" (CKP-S:246-247): il
  TALLONE nominato della gerarchia.
- **(H) hysteresis** — canale residuo nominato, nessun numero
  (CKP-S:226).
- **swirl coerente B1-B5** — canale residuo, con la variante di record
  "B2~0 drop-variant" (CKP-S:226-227).
- **slip-sheets G9** — fuori scope T0P (CKP-S:243-244); "G9 slip-line
  lift = F2 deriver" (CKP-S:252).

**Regola vincolante, verbatim**: "The C-3bis hierarchy (A)>(B) holds on
the smooth part; its named Achilles heel = (J). If (J) is large, (B)
can dominate even in-sector" (CKP-S:248-251); "Deck/atlas rule: state
the hierarchy WITH the (J) heel, never without" (CKP-S:253-254).

**(iv) DEATH SCENARIO (la paura utente, resa misurabile).** Verbatim
(CKP-S:230-237): "DEATH SCENARIO (user fear: pf close to mean AND far
from 3D) requires TWO independent failures: (A)-small needs G
quasi-linear over 10:1 (gasdynamics is not) AND (B)-large needs
suppression failure (large (J)/(H), slip-sheets G9, swirl gradient) —
each measurable separately: (A) by the TWIN at identical constraints
(cheap, FIRST), (B) by M-RED + 5F sign test. Twin-first ordering = the
honest kill-or-validate." Il twin è CHEAP e va PER PRIMO: o uccide la
gerarchia (kill) o la valida sul lato (A) — esito informativo in
entrambi i casi.

**(v) Decisori pre-registrati (entrambi gli esiti informativi).**
CKP-S:209-214: "(i) M-RED bands, (ii) TWIN family-vs-I4 at IDENTICAL
constraints (same eps, L, closure, sector; output = shape delta + J
delta) — twin spec SHARPENED by user correction, (iii) 5F gradient +
sign test (S-5F user decision pending), (iv) CFD-2/CFD-1. Both
outcomes pre-registered informative; G2 kill-gate = honest death"
(G2: §1.5). Il lato (B) si misura con le front legs di M-RED "(B-1/B-3,
comparison C: F_true vs F_2D per phase)", con la "KP18 corrugated sonic
line as the throat-reaching evidence" (CKP-S:251-253). Stato (celle
Q-i/Q-iv/Q-v): PB-2 OPEN (A-1); decisioni utente PENDENTI con owner e
finestra in A-9 (§3): twin (a)/(b) e S-5F path A/B/C + priorità C51.

**Cella Q-iii — il campo separa i tre gap? Query eseguita (protocollo
bounded G-11, emendamento §6a).** Query q (2026-08-23, in-window):
perimetro CHIUSO = `docs/literature_registry.yaml` (174 id) +
`docs/rde_nozzle_literature_map.md` + slot P-A..P-D
(`validation/sfoundations_raws_2026-08-13/blocco3/NOZZLE_RDE_STUDY_p{A,B,C,D}_*.md`);
pattern misurati in finestra: `formulation gap|design gap|three-design|
mean-designed vs|x*_mean` su registry e litmap (0 hit entrambi) e
`error budget|decompos|attribut/separat (gap|error|source)` sugli slot.
**Esito: NOT-FOUND(q)** — nessuna fonte del perimetro separa i tre gap
di DESIGN (formulazione / modello / composizione). I near-object
trovati sono decomposizioni di PERDITA DI FLUSSO, non di gap di design:
P-B "three-part TRANSIENT flow-loss decomposition" (pB:175, F-15,
"stated but not separately quantified" pB:363); P-A perdita totale
14.2% "UNDECOMPOSED ... no decomposition offered" (pA:259-261); P-D
bookkeeping Eqs. (1)-(3) (pD:410). STOP (nessun procurement in-onda,
G-11). Eco in CH5 §1.6 [WB1].

### 1.3 Le guardie pubbliche: D-44 e P34

- **D-44 — gate sui claim pubblici di adeguatezza** (armato, e vincola QUESTO
  deck): "any public adequacy claim GATED (forchetta = bracket with provenance,
  never demonstrated adequacy)" — riga della pipeline map
  (`docs/rde_nozzle_pipeline_decision_map.md:180`, stato "ARMED GATE", "fires
  on any public adequacy claim, either way (before/after R22)"), arco E31
  esplicito verso S-PRES: "D-44→S-PRES/public claims: findings :1468 'any
  public adequacy claim remains gated per D-44 either way'; PROGRESS :395
  S-PRES trigger-scan item (ii)" (:239). Owner di record: "F2 or F5 (D-44;
  R22 = the single highest-value tranche-2 item)"
  (`docs/findings_registry.yaml:2163`). Il trigger-scan S-PRES lo recepisce:
  "(ii) D-44: claim di adeguatezza gated (forchetta = bracket con provenienza,
  mai adequacy dimostrata)" (`docs/rde_nozzle_PROGRESS.md:400-401`).
- **P34 — gerarchia di evidenza per claim engine-level** (finding CONFIRMED,
  `docs/findings_registry.yaml:2530-2539`): "the staged evidence hierarchy for
  engine-level claims — V0 continuous verification -> per-champion validation
  -> pre-registered, prediction-first rig/thrust-stand terminal test ... was
  never adjudicated anywhere in the record" (:2533). Rider che spara su questa
  milestone: "S-PRES ... is a trigger-bearing external act — slide-level engine
  claims must DECLARE their evidence stage on this row's ladder at the S-PRES
  Block-0 trigger-scan" (:2538). Classe: gap dichiarato con owner
  ("P-1/G5-G6 claims window", :2537).

### 1.4 R26: la domanda a due livelli (sizing vs ranking)

La tensione R26 è aggiudicata come SOGLIA, non come contraddizione
(`docs/findings_registry.yaml:2148`): "is cycle-averaging adequate or blind?
Paxson-Miki says adequate for sizing (6.54 vs ~6.5); Harroun 2021 says blind to
contour ranking (c_F=1.25 identical) — PARTIALLY adjudicated: not a
contradiction, a RESOLUTION THRESHOLD (adequate for sizing, not demonstrated
adequate for percent-level ranking); exactly where the threshold falls stays
OPEN, decided by R22". La forma di record in forchetta, canale (iv)
(`docs/rde_nozzle_MASTER.md:1346`): BEST = "**~1% at sizing level** [REP]:
Paxson-Miki area-ratio agreement 6.54 vs ~6.5"; WORST = "**RANKING THRESHOLD
OPEN (R26)**: adequacy NOT demonstrated for percent-level contour ranking ...
Harroun 1.25-flat is a NON-DISCRIMINATION datum at verified limits ... NOT
proof of blindness". Classe: [REP] sul livello sizing — **su UN'ISTANZA
esterna** (forma vincolante CH3 [W2-R2], `CH3_reduction_physics.md:594-596`:
sizing "SUPPORTATO a ~1% su un'istanza esterna", mai "dimostrato") [WB1-R3];
OPEN dichiarato sul ranking. Nessun referee esterno esiste per la parte per-fase: "NO EXTERNAL
PUBLISHED REFEREE EXISTS for the per-phase thrust error: the literature carries
NO unsteady c_F datum that discriminates the 2D-per-phase-averaged prediction
against 3D-unsteady truth" ([REV2-r1-15], `docs/rde_nozzle_MASTER.md:1322-1331`,
dichiarazione strutturale di record; nearest referees nominati e squalificati
in [GRAFT-G10], M0:1311-1320, [ADV]).

### 1.5 La roadmap: i deciders in ordine, coi costi noti

Ordine ratificato al touchpoint C4 (`docs/rde_nozzle_PROGRESS.md:407-421`):

1. **M-RED — prima campagna F2, in-house** ("(c) M-RED RESTA prima campagna F2
   (nessun pull-forward)", :417). Costo: il frame utente-ratificato la marca
   "tier (b) M-RED execution = THE cheap decisive unlock, F2-gated"
   (checkpoint :462-463); il push formale tier (a) è perimetrato "~0.3M"
   (checkpoint :460-462; unità NON dichiarata all'ancora — la lettura "token
   di orchestrazione" è [INF] dal contesto del checkpoint [W2-R8]; su slide il
   numero non va portato). M-RED misura eps e alimenta le bande B-1/B-2/B-3 della
   forchetta (colonne "what tightens it", M0:1344-1346).
2. **CFD-2 — paired demo, template Li-Xu 2025 (P-C), in coda F2**: "CFD-2 (demo
   pair Harroun coi run per-fase nostri, barra = eps di M-RED, template
   paired-run Li-Xu 2025, contratto BC documentato dal throat harvest) ENTRA IN
   CODA F2" (:408-411).
3. **CFD-1 — test del pin su configurazione accoppiata reale, item di calcolo
   massimo, decisione POST-M-RED**: "CFD-1 ... SI DECIDE POST-M-RED con dossier
   procurement/collaborazione e criteri di riferimento PM22-conforme vs
   Jourdaine-patologico" (:411-414). Classe di costo di record: "~12M-cell cost
   class, M-RED dependency, G1 haste-risk" (pipeline map,
   `docs/rde_nozzle_pipeline_decision_map.md:77`; stato "USER-DECISION
   PENDING"). Le catene sono cablate nella mappa: E28 "T-RED → M-RED bands
   B-1/B-3 → X-T3QS-5F license (F2) → R22-CFD-1" e E29 (deriver (vi))
   (`docs/rde_nozzle_pipeline_decision_map.md:236-237`).

**G2 — VALUE GATE, il kill criterion del programma (theorem-grade)**
[WB1-R4] (critic 7): il piano codifica GIÀ l'esito sfavorevole, verbatim
(D6 :776-778): "G2 (M2) VALUE GATE, now theorem-grade: bound-ladder gap per
channel; gap < ~1% Isp on all of N1-N4 → pivot to certification/
operability/duty-split value proposition (honest death)". La nota
2026-08-19 (D6 :779-782, S-FOUNDATIONS-C tree-diff §4 item 10) fissa
l'ancora di calibrazione esterna del budget delta/(v) e dell'ambizione di
tolleranza: "THRUST-STAND-CLASS accuracy (~0.5-1%)" — "Note only, no
row". Il pivot dell'"honest death" è quindi NOMINATO nel piano, non
improvvisato in Q&A (consumo in Q1); e la soglia del kill si confronta con
ciò che un banco di spinta sa misurare.

**Collocazione di F4b nella catena (il QUANDO relativo di PB-2)**
[WB1-R5] (critic 18): la finestra F4b (declared-topology fitted fronts /
truncated-plug; entry D6 :233-238) ENTRA a F2-exit ed è
ORDINE-INTERSCAMBIABILE con F3: "F3 and F4b are ORDER-INTERCHANGEABLE
given F2 exit (both entry gates independent of each other)" (D6 :228-232).
Quindi il computo PB-2 (trigger C61, §1.2) cade DOPO M-RED e la coda CFD-2
(entrambe dentro F2), nella finestra F3/F4b — il cui ordine relativo non è
pinnato, per piano — mentre la decisione CFD-1 (post-M-RED) può cadere
prima o in parallelo. Il TWIN di N-Q (§1.2-bis) è invece cheap e
twin-first: non attende F4b (decisione utente pendente, A-9).

**Rischi di programma (riga di ancoraggio)** [WB1-R6] ([V2-R11]): ogni
slide-rischi si ancora al RISK REGISTER del piano — D6 §7 "Risk register
deltas (vs roadmap)" (:1093 e segg.): RK-A (rischio scoop P2' da
Lozano-Ponsin 2025, con annotazione S14 "PARTIALLY REALIZED" e deferral
count portato dall'item 9), RK-B (quadrature-switch neglect), RK-C
(data-contract violations) — mai una lista-rischi improvvisata fuori
registro.

### 1.6 Le ASK di record

Dal record, non inventate per il deck:

- **CFD-1 come collaborazione/procurement**: il dossier
  procurement/collaborazione è il veicolo deciso per CFD-1
  (`docs/rde_nozzle_PROGRESS.md:411-413`).
- **Dati motore per la classe del pin (R20)**: "no published dataset certifies
  a single-mode wave PERSISTENT in thermal-steady-state (Teasley 2023's
  observations are almost all at startup) — the periodic-pure-wave pin remains
  valid as a MODEL HYPOTHESIS but loses its hardware provenance; decided by
  high-speed imaging in steady mainstage, or published transition durations"
  (`docs/findings_registry.yaml:2148`; owner "F5 (R20)", :2152). L'ask: imaging
  ad alta velocità in mainstage termicamente stazionario, o durate di
  transizione pubblicate. **Scope dichiarato [WB1-R8] (critic 14)**: R20
  parla di DATASET HARDWARE ("no published dataset ..."); il lato CFD è un
  claim DISTINTO e bounded al corpus letto — il pin è ESIBITO nei CFD del
  corpus ma mai verificato spettralmente (riga CH5 §1.2 [WB1], con grep
  in-window) — i due scope non vanno MAI fusi in un unico "search-proven"
  su slide.
- **Canale paper** [WB1-R7] (critic 19): P-1, venue JPP ("I documenti di
  teoria sono la sorgente del paper (P-1, venue JPP)", `CLAUDE.md` R4).
  **P-2 (paper compagno): freeze FIRED, datato 2026-08-11** — "P-2 freeze
  FIRED dated 2026-08-11 (P2_outline header block; C1 blocker adjudicated
  freeze-with-declared-conditional, owner F2)"; fallback di record: "P-2
  publishes on S19 two-knob numbers" (D6 :85-100). La risposta di record a
  "cosa pubblicate e quando": P-1 in costruzione dai doc di teoria, P-2
  congelato con blocker C1 dichiarato (owner F2); G5 blocca le SUBMISSION,
  non le presentazioni (CH2 §1.8) — il wording query-bounded vincola
  comunque (CKP-S :81-82).
- **Procurement documentale attivo**: "top-3 harvest (Lim-Humble AIAA
  2020-0195, Stechmann PhD 2017, Schwer-Kailasanath AIAA 2012-3943) + i 3 ask
  fermi (More-Wild ECNoise, ASME V&V 20-2009, Xing-Stern); il resto WANTED
  passivo" (`docs/rde_nozzle_PROGRESS.md:418-421`); coda WANTED Tier-1
  W-01/W-02/W-03 = Fotia 2016 (JPP 32(3):674-681), Goto 2019 (JPP 35(1):
  213-223), Ma-Bao-Wang 2023 (AST 140:108464)
  (`docs/literature_registry.yaml:1232-1248`).

### 1.7 L'onestà come strategia (la bussola del carrier)

La bussola della milestone è testuale: "comunicare il programma SENZA gonfiare
una sola classe di rigore — l'onestà strumentata È il vantaggio competitivo del
deck" (`validation/ADVISORY_Spres_prompt_2026-08-21.md:233-235`). Non è
retorica: è la stessa disciplina che produce il no-external-referee fact
(M0:1322-1331), le celle "NO cell above its held evidence class" (M0:1309), i
12 NEVER del choice ledger (righe di scelta con incumbent dichiarato e
falsificatore pinnato, "NEVER: 12 (C25 C38 C51 C52 C53 C54 C55 C57 C59 C60 C61
C62)", `docs/rde_nozzle_pipeline_decision_map.md:293`), e i falsificatori
armati sui numeri vietati (claims :2262). Alla domanda "perché credervi senza
il numero" il programma risponde con la STRUTTURA, non con una promessa: vedi
§4, Q2.

---

## 2. Stato per-claim

| # | Claim | Classe | Ancora | Carrier / falsificatore |
|---|-------|--------|--------|------------------------|
| 1 | Gap B = J3D(x\*_pf) − J3D(x\*_legacy), misurabile in-house (paired-run F2, nostra funzionale vs Veen/Angelino-at-mean) | Definizione di record; valore MAI computato | checkpoint S-FOUNDATIONS :466-472 | Carrier futuro = paired-run F2 (M-RED window); oggi NESSUN numero |
| 2 | Gap A = distanza dall'ottimo 3D vero, incomputabile; solo bounded (delta/mu) + spot-check | SCHEMA (bound); delta e L_H UNDERIVED | checkpoint :469-471; M0:1348 | Falsificatore armato: claims_registry.yaml:2262 (nessun numero di argmax-shift a nessun grado prima di delta/L_H) |
| 3 | Value condition: Gap B materiale AND Gap A < Gap B | Frame registrato (S-PRES anchor), non teorema | checkpoint :471-472 | Deciso da M-RED + CFD-2/CFD-1 |
| 4 | best-of-sweep ≠ argmax; nessun paper ha mai ottimizzato il caso 3D vero | [ADV] guard di record | checkpoint :472-476; M0:1335-1339 | Query-bounded (4 paper campagna + P-M hand-guided) |
| 5 | PB-2: primo problema concreto non risolto da alcun design single-phase; T4 nesting fallisce, max∫ < ∫max strictly; novità SOLO nella locked formulation D-06 ("first genuinely averaged and NON-COLLAPSING shape problem ... a CYCLE instance", never abbreviate; near-miss Efremov-Kraiko 2004 = query-bound) [W2-R5] | Enunciato problem book (problema posato, non risolto); D-06 locked | problem_book.md:532-537; M0:2320-2329 | Carrier futuro = computo PB-2; trigger C61 :829; frasi "first averaged-thrust variational problem" = DEAD of record |
| 6 | Baseline media = I4 (⟨Pc⟩,T0,γ), esatta dentro le ipotesi I3 | Definizione di record | problem_book.md:211-213 | Twin famiglia-vs-I4 stesso engine = PROPOSTA di consolidamento col paired-run di Gap B (baseline di record di Gap B = Veen/Angelino-at-mean, checkpoint :468-469 — I4 è Rao/GENO, baseline distinta) [W2-R2] |
| 7 | Chiusura p_b: slot N2 dichiarato, NON aggiudicato; Veen legacy-only, WG10-FAILED | C61 status NEVER | choice_ledger.yaml:818-830 | Trigger: prima riga (value,delta) truncated-plug o finestra F4b |
| 8 | Swap del modello p_b muove l'argmax ×2.45 a valore quasi piatto (+0.26%) | [ADV]; numeri = Humphreys 1971 (CT-6) | M0:1455-1464; choice_ledger :830 | Exhibit classico, channel-(vi)-shaped |
| 9 | Nessuna misura di base truncated-plug RDE esiste; transfer nozzleless→plug = ANALOGIA dichiarata | [REP] sul dato + ANALOGIA dichiarata | findings :2092-2095 | Chiuso solo da misura (procurement class) |
| 10 | D-44: ogni claim pubblico di adeguatezza è GATED (forchetta = bracket con provenienza) | ARMED GATE | pipeline map :180, :239 (E31); findings :2163; PROGRESS :400-401 | Spara su questo stesso deck (trigger-scan Block-0) |
| 11 | P34: gerarchia di evidenza engine-level mai aggiudicata; le slide devono dichiarare lo stage | Finding CONFIRMED (gap con owner) | findings :2530-2539 | Rider S-PRES esplicito (:2538) |
| 12 | R26 sizing: ~1% a livello sizing (Paxson-Miki 6.54 vs ~6.5) | [REP] | M0:1346; findings :2148 | Page-verified nella confrontation |
| 13 | R26 ranking: soglia APERTA; Harroun 1.25-flat = non-discrimination datum, NOT proof of blindness | OPEN dichiarato | M0:1346; findings :2148 | Deciso da R22 (M-RED → CFD-2 → CFD-1) |
| 14 | Nessun referee esterno pubblicato per l'errore di spinta per-fase | Dichiarazione strutturale di record | M0:1322-1331 (+ :1311-1320 nearest disqualified) | Chiude solo via R22-CFD nostro o data procurement |
| 15 | R20: nessun dataset pubblicato certifica onda single-mode persistente in thermal steady state; pin = MODEL HYPOTHESIS | Residuo [REP]-based, OPEN | findings :2145-2153 | Deciso da imaging steady-mainstage o transition durations |
| 16 | Roadmap deciders: M-RED (prima campagna F2) → CFD-2 (coda F2, template Li-Xu paired) → CFD-1 (post-M-RED, ~12M-cell, user decision) | Decisione utente ratificata + pipeline map | PROGRESS :407-421; pipeline map :77, :236-237 | G1 haste-risk dichiarato sulla mappa |
| 17 | Bussola: comunicare senza gonfiare UNA SOLA classe di rigore | TERM vincolante della milestone | ADVISORY_Spres_prompt :233-235 | Refuter di rigore sul deck (doppia review) |
| 18 | N-Q working hypothesis: a (eps,L) e settore fissi, gap(A) pf-vs-mean senza teorema di soppressione (Jensen su G(x;s), escursioni 10:1) vs gap(B) pf-vs-3D con TRE teoremi sulla parte liscia → plausibilmente (A)>(B) in-settore (enunciabile SOLO col tallone (J), riga 19 — guardia 1) | IPOTESI DICHIARATA falsificabile (mai teorema) [WB1] | CKP-S:215-230 | Death scenario = 2 fallimenti indipendenti: (A) twin a vincoli identici (cheap, FIRST); (B) M-RED front legs + 5F sign test (CKP-S:230-237) |
| 19 | Tallone (J): front jumps = primo ordine NON soppresso di gap(B), SBV-conditional, delta underived; se (J) grande, (B) può dominare anche in-settore; gerarchia MAI enunciata senza il tallone | Regola C-3ter vincolante (guardie 1/16) [WB1] | CKP-S:245-254 | M-RED comparison C (F_true vs F_2D per fase); G9 slip-line lift = F2 deriver |
| 20 | G2 VALUE GATE theorem-grade: gap < ~1% Isp su tutti N1-N4 → pivot certification/operability/duty-split (honest death); calibrazione thrust-stand-class ~0.5-1% (nota, no row) | Gate di piano [WB1] | D6:776-782 | Deciso dai deciders §1.5; consumo Q1 |
| 21 | P-2 freeze FIRED 2026-08-11, blocker C1 = conditional dichiarata owner F2; fallback S19 two-knob | Stato di record [WB1] | D6:85-100 | — |

---

## 3. Gli APERTI

- **A-1 — PB-2 MAI computato.** Nessuna riga (value,delta) truncated-plug nel
  record (trigger C61 mai sparato, `docs/choice_ledger.yaml:829`). Servono:
  baseline I4 mean-designed (problem_book :211), chiusura p_b (C61 NEVER, slot
  N2; owner "N2/F4b window", :828), e la consapevolezza Humphreys ×2.45 che la
  chiusura muove il design (M0:1455-1464). Owner/trigger: F4b window / prima
  riga truncated-plug.
- **A-2 — Gap B: grandezza ignota.** Il frame è registrato, il paired-run non è
  stato eseguito (checkpoint :466-472). Owner: finestra M-RED/F2 (PROGRESS
  :417). Se Gap B risultasse trascurabile: vedi §4 Q1.
- **A-3 — Gap A: delta e L_H UNDERIVED.** Nessun numero di argmax-shift esiste
  a nessun grado (M0:1348); deriver nominati in ordine "X-T3QS-5F (F2) →
  C51-route-B → M-RED gradient rider → R22-CFD-1" (M0:1348, colonna deriver;
  pipeline map :237 E29).
- **A-4 — R26 ranking threshold OPEN.** "decided by R22" (findings :2148);
  fino ad allora D-44 gated ogni claim pubblico di adeguatezza (pipeline map
  :180).
- **A-5 — R20: provenienza hardware del pin.** Il pin onda-pura è ipotesi di
  modello, non fatto certificato da dataset pubblici in steady state
  (findings :2148). Owner "F5 (R20)"; trigger "next hardware-provenance
  campaign" (:2152-2153).
- **A-6 — P34: ladder di evidenza engine-level non aggiudicata** (findings
  :2533); a S-PRES vige solo la light-instantiation (dichiarare lo stage per
  slide, :2538); l'aggiudicazione piena resta alla finestra P-1/G5-G6 (:2537).
- **A-7 — CFD-1: decisione utente PENDING** con dossier post-M-RED (PROGRESS
  :411-414; pipeline map :77 "USER-DECISION PENDING", "G1 haste-risk").
- **A-8 — Base measurement truncated-plug RDE: inesistente nel corpus letto**
  (findings :2095) — procurement/misura, non chiudibile in-house.

- **A-9 — Decisioni utente PENDENTI del nodo N-Q (cella Q-v)** [WB1]: (a)
  **twin PB-2 (a)/(b) a vincoli IDENTICI** (stesso eps, L, chiusura,
  settore; output = shape delta + J delta, spec SHARPENED dall'utente,
  CKP-S:210-212) — presentata al GATE STORYBOARD con costo; **latest-start
  ~01/09**, oltre cui la slide resta nella forma onesta; (b) **S-5F path
  A/B/C + priorità C51** — idem (emendamento v2.1 §6a G-10; memoria
  swirl5f-panel). Owner: utente (gate storyboard); finestra: pre-authoring
  (~01/09). Fino ad allora PB-2 resta OPEN (A-1) e la gerarchia N-Q resta
  IPOTESI DICHIARATA col tallone (J) stampato (§1.2-bis).

Nessuno di questi aperti va riempito di plausibilità nel deck: si dichiarano
con owner e trigger, come sopra.

---

## 3-bis. Antenati diretti (lineage claim — template §3-bis; nodi N-O/N-L/N-Q) [WB1]

Join sul `LINEAGE_LEDGER.md` (merge W-B.0) per {LL-id, componenti},
contratto [F-des-4]; ogni riga del ledger è CANDIDATE finché il refuter C6
(W-C) non passa. Righe pertinenti ai claim di novità di questo capitolo:

- **LL-21 (Sun 2019 / Liu 2022 / Miki 2020)** — "decomposizione di spinta
  pubblicata, mai identità dimostrata né per-fase": l'antenato della
  nostra attribuzione di valore per canali; ciò che manca vs noi =
  l'identità di decomposizione [MINT-PENDING F-2: sector-decomposition
  identity J_exact = ∫ F_true dµ — THEOREM in-panel, non ancora numerato
  in M0] e il grado per-fase.
- **LL-22 (convenzioni di media non dichiarate — Liu Eq.14, P-C; +
  Harroun LL-2)** — "la nostra µ è l'unica pinnata (T-O2)":
  antenato-per-contrasto del frame di valore — senza µ dichiarata, nessun
  Gap B è nemmeno DEFINIBILE, e nessun confronto pf-vs-mean è riproducibile.
- **LL-35 (Ornano 2017)** — "gerarchia staged implicita a 3 stadi =
  analogo più vicino di P34, senza tier dichiarato": antenato della ladder
  di evidenza P34 (§1.3) — il campo la pratica implicita, il programma la
  dichiara per slide (rider :2538).
- **N-Q (frame three-design, §1.2-bis)** — ANTENATI: **NOT-FOUND(q)** —
  query Q-iii eseguita in-window (§1.2-bis, perimetro chiuso G-11):
  nessuna fonte del perimetro separa i tre gap di design; near-object =
  decomposizioni di perdita di flusso (P-B F-15 → LL-21), mai di gap di
  design. (lint 7)

---

## 4. Domande da panel (banco utente incluso, verbatim-adattate)

**Q1. "Gap B potrebbe risultare trascurabile: cosa resta del programma?"**
Risposta onesta dal record: (i) il frame è costruito per essere falsificabile —
la value condition "Gap B material AND Gap A < Gap B" (checkpoint :471-472) è
un rejector, non uno slogan: se il paired-run misura Gap B trascurabile, il
programma lo DICE, e questo è esattamente il punto di R26: il sizing è
SUPPORTATO a ~1% **su un'istanza esterna** [REP] (M0:1346; forma CH3, mai
"dimostrato" [WB1-R3]) — un Gap B piccolo sarebbe un datum
misurato che stringe la soglia R26 sul caso testato, sempre come bracket con
provenienza, mai adequacy dimostrata: D-44 vale in entrambe le direzioni,
anche su un esito favorevole alla media ("fires on any public adequacy claim,
either way", pipeline map :180). [W2-R1] E il piano codifica GIÀ questo esito
come gate, non come imbarazzo: **G2 VALUE GATE, theorem-grade** — "gap <
~1% Isp on all of N1-N4 → pivot to certification/operability/duty-split
value proposition (honest death)" (D6 :776-778, con la calibrazione
thrust-stand-class ~0.5-1% come ancora esterna, :779-782) [WB1-R4]: il
pivot è nominato nel piano di sviluppo, la risposta a "cosa resta" è di
record prima della domanda. (ii) Restano in piedi i pezzi che non dipendono dal segno
di Gap B: il corpus dei teoremi di riduzione/struttura (forchetta canali
(i)-(iii), M0:1343-1345, classi SCHEMA/THEOREM\*), PB-2 come problema
matematico nuovo (problem_book :532-537 — la rottura del nesting non dipende
dalla grandezza di Gap B su UNA configurazione), e la macchina certificata
(oracoli, catena M-RED). (iii) OPEN dichiarato: la grandezza di Gap B è A-2 —
non abbiamo il numero, e non lo promettiamo: lo misuriamo per primi in-house.

**Q2. "Chiedete CFD e dati: cosa date in cambio, e perché ESA dovrebbe
investire PRIMA del numero PB-2?"**
Dal record: quello che esiste GIÀ e non dipende dall'investimento chiesto:
(a) i teoremi di DOVE la riduzione sbaglia — la forchetta a 6 canali con classi
e provenienza per cella (M0:1341-1348), incluso il no-external-referee fact che
NESSUN altro gruppo ha dichiarato (M0:1322-1331); (b) la macchina pronta: il
carrier misurato del canale (vi) esiste (J_red Hessians di record, curvatura
TR-Newton segmentata, M0:1348) — manca la licenza formale (delta/L_H), non il
codice; (c) la campagna è COST-CLASSED e ordinata (classi di costo dichiarate, non
prezzi assoluti: quelli sono OPEN, parte del dossier post-M-RED [W2-R7]):
M-RED = "cheap decisive unlock"
(checkpoint :462-463), CFD-2 in coda con template e barra definiti (PROGRESS
:408-411), CFD-1 ~12M-cell con dossier e criteri di riferimento già nominati
(PM22-conforme vs Jourdaine-patologico, PROGRESS :411-414; pipeline map :77);
(d) i falsificatori sono ARMATI prima dei numeri (claims :2262; D-44 pipeline
map :180). In cambio ESA ottiene: il primo paired-run famiglia-vs-legacy-mean
su motore condiviso (baseline di record Veen/Angelino-at-mean, checkpoint
:468-469; l'estensione a I4/Rao-GENO nella stessa run = proposta di
consolidamento, §1.2 [W2-R2]) — "primo" per costruzione: nessun paired-run di
questo tipo esiste nel corpus letto, query-bounded alla campagna 4-paper +
litmap [W2-R11] —, la prima verifica spettrale/di persistenza del pin su dati
veri (prima nel perimetro R20 search-proven [W2-R11])
(R20, findings :2148 — l'ask specifica cosa serve: imaging steady-mainstage o
transition durations), e un canale paper JPP (CLAUDE.md R4). L'ask documentale
è minimale e già enumerata (top-3 + 3 fermi + W-01/02/03, PROGRESS :418-421;
literature_registry :1232-1248). OPEN dichiarato: il ritorno quantitativo è
condizionato all'esito di M-RED — è per questo che CFD-1 si decide POST-M-RED,
non prima (G1 haste-risk, pipeline map :77).

**Q3. "La vostra onestà dichiara delta/L_H underived e 12 NEVER: non è un
programma immaturo?"**
Distinguere i due oggetti. (i) I "12 NEVER" (pipeline map :293) non sono
lavoro non fatto: sono righe del choice ledger dove un incumbent PRATICATO è
dichiarato con alternative enumerate e falsificatore pinnato per un flip futuro
— es. C61: incumbent Veen "legacy-practiced, WG10-FAILED" con quattro
alternative pesate a grado record (choice_ledger :818-830); C62 con "honesty
clause carried from the critic (zero inflation)" (:844). La classe NEVER è lo
strumento che IMPEDISCE ai default silenziosi di diventare fondamenta — i
programmi che non hanno questa lista hanno gli stessi default, non dichiarati.
(ii) delta/L_H underived (M0:1348) è la ragione per cui NESSUN numero di
argmax-shift è mai stato quotato — con falsificatore armato (claims :2262). Il
confronto rilevante: nessun lavoro pubblicato ottimizza il caso 3D vero, e
l'evidenza sweep/redesign è ranking-signal only (guard M0:1335-1339) — quindi
nessun confronto esistente è un confronto con un argmax [W2-R3] — e la
letteratura non porta NESSUN referee esterno
per l'errore per-fase (M0:1322-1331). La maturità di un programma di design si
misura su cosa può REGGERE in verifica, non su cosa dichiara di sapere: qui
ogni cella è al suo grado, "NO cell above its held evidence class" (M0:1309).
OPEN dichiarato: sì, delta e L_H mancano; i deriver sono nominati in ordine con
finestra (M0:1348; E29).

**Q4. "Se il pin onda-pura non è mai stato verificato spettralmente in NESSUN
CFD pubblicato (search-proven), su cosa poggia tutto?"**
Prima la precisione sul fatto, come sta nel record: la forma search-proven di
record è R20 — "no published dataset certifies a single-mode wave PERSISTENT
in thermal-steady-state ... the periodic-pure-wave pin remains valid as a MODEL
HYPOTHESIS but loses its hardware provenance" (findings :2148). Su cosa poggia
il programma, dal record: (i) il pin è un'IPOTESI DI MODELLO DICHIARATA, non un
fatto assunto di nascosto — e dentro il pin la cycle-average è
"CANONICAL-INSIDE-THE-PIN ... a theorem-backed CONSEQUENCE, not a choice"
(C59, choice_ledger :795-797), con le alternative fuori-pin (harmonic-balance,
time-spectral, windowed adjoint) enumerate nella stessa riga per i regimi a pin
indebolito (:798-801); (ii) il pin ha una guardia DI RECORD, con
stato dichiarato: "T0-flatness monitor + f_cycle contract field" (forchetta
canale (i), M0:1343) — il T0-flatness monitor è la parte armata; f_cycle è un
contract field NOMINATO non ancora cablato, e i certificati orbit-spectral
Floquet/monodromy (A20) sono graft nominati, non implementati: la riga di
registro apre con "five CycleFamily/VI.1 contract additions, none wired"
(findings :1926, owner "F2 / VI.1") [W2-R4]; (iii) il test del
pin è UN DECIDER DELLA ROADMAP, non un rinvio: CFD-1 è definito esattamente
come "test del pin su configurazione accoppiata reale" (PROGRESS :411-412), e
l'ask-dati R20 nomina cosa lo chiuderebbe lato hardware (findings :2148,
:2153). OPEN dichiarato: la provenienza hardware del pin in steady state è
A-5; se il pin cade in un regime, il record ha già la mappa d'uscita (C59
alternatives; H-AM1 exit dichiarata in forchetta (i) WORST, M0:1343).

**Q5. "Il vostro bound Gap A usa curvature misurate su J_red: perché la
curvatura del modello ridotto dovrebbe dire qualcosa sul 3D vero?"**
Dal record: NON lo assumiamo — è esattamente H-G6, e finché L_H (la faccia a
livello curvatura del residuo di riduzione) non è derivata, "the GRADIENT route
licenses NO number even a-posteriori from the measured carrier alone"
(M0:1348). Esiste la value-route con floor misurato legittimo (mu_red) ma a
tasso sqrt e a classe estimate, mai spacciata per copertura d'ottimo
("A value-level bound is NEVER passed off as optimum coverage", M0:1348).

**Q6. "PB-2 dipende da p_b, e voi stessi citate Humphreys: il vostro ottimo
truncated-plug non sarà un artefatto della chiusura?"**
Risposta dal record: è il rischio che abbiamo REGISTRATO noi, a grado
foundation (C61 note: "the closure choice moves the DESIGN, not just the
value", choice_ledger :830). Per questo lo slot N2 è NEVER e non un default:
il verdetto WG10 su Veen è "N2 MUST REPLACE IT" (:824), l'unico dato RDE
esistente (Purdue CTAP, transizione Pa/Pc~0.15) è nominato (:825), e il
transfer nozzleless→plug è dichiarato ANALOGIA (findings :2095). Il computo
PB-2 entrerà nel record CON la sensibilità alla chiusura dichiarata, o non
entrerà (trigger C61 :829).

**Q7. "La value condition richiede Gap A < Gap B, ma Gap A è incomputabile e
delta/L_H sono UNDERIVED: come verificherete MAI la condizione?"** [W2-R9]
Risposta onesta dal record: oggi la condizione è INDECIDIBILE, e lo diciamo —
"delta AND L_H UNDERIVED ... NO argmax-shift number exists at any grade, and
none from the measured carrier alone" (M0:1348). Il percorso di decidibilità
è però ordinato nel record, ogni passo con la sua classe: (i) M-RED misura
eps_U (il livello uniforme di value-error sul basin esplorato, sweep-sup dei
value legs (A)-(B), classe SAMPLED-SUP/estimate); (ii) la VALUE-ROUTE dà il
bound a-posteriori |argmax shift| ≤ 2·sqrt(eps_U/mu_red) — l'unica rotta il
cui floor mu_red è legittimamente il carrier misurato as-is — a classe
estimate, a tasso sqrt, mai spacciata per copertura d'ottimo ("A value-level
bound is NEVER passed off as optimum coverage", M0:1348); (iii) la GRADIENT
route (delta/mu_curv), che sola può stringere al livello dei delta in-class,
attende delta e L_H dai deriver nominati in ordine "X-T3QS-5F (F2) →
C51-route-B → M-RED gradient rider → R22-CFD-1" (M0:1348; pipeline map :237
E29); (iv) R22-CFD chiude con lo spot-check. OPEN dichiarato: fino a M-RED
non esiste NESSUN numero su nessun lato della disuguaglianza — la condizione
è un rejector armato, non un verdetto anticipato.

---

## 5. Cosa deve dire il deck

1. **Il value case è una condizione falsificabile, non una promessa**: Gap B
   misurabile in-house (paired-run, baseline di record = Veen/Angelino-at-mean;
   l'aggiunta di I4/Rao-GENO come seconda baseline mean-designed nella stessa
   run = proposta dichiarata, non record [W2-R2]), Gap A bounded-only; il
   programma vale se "Gap B material AND Gap A < Gap B" — e lo si dice così.
   [Frame di record, checkpoint :466-472; classi: definizione + SCHEMA]
2. **PB-2 è la bandiera**: il primo problema concreto che NESSUN design
   single-phase risolve (rottura del nesting T4, max∫ < ∫max) — posato con
   precisione, MAI computato, e il deck dichiara cosa manca (baseline I4 +
   chiusura p_b N2) e il warning Humphreys ×2.45. La slide porta la novità
   SOLO nella locked formulation D-06 ("the first genuinely averaged and
   NON-COLLAPSING shape problem of the program (a CYCLE instance)", never
   abbreviate) col near-miss Efremov-Kraiko 2004 (no wall contour) come
   query-bound esplicito; ogni frase tipo "first averaged-thrust variational
   problem" è DEAD of record (M0:2320-2329) [W2-R5]. [Enunciato problem book
   :532-537 + C61 NEVER + [ADV] Humphreys + D-06 locked]
3. **La slide onesta della forchetta**: 6 canali, ogni cella al suo grado, "NO
   cell above its held evidence class"; sizing ~1% [REP], ranking OPEN (R26),
   nessun referee esterno esiste — per nessuno. [M0:1306-1348; D-44 vincola la
   slide stessa]
4. **La roadmap ha deciders, ordine e classi di costo** (cheap in-house /
   paired demo / ~12M-cell cost class; prezzi assoluti = OPEN, dossier
   post-M-RED) [W2-R7]: M-RED (in-house, cheap decisive
   unlock) → CFD-2 (paired, template Li-Xu, barra = eps di M-RED) → CFD-1
   (~12M-cell, decisione post-M-RED, G1 haste-risk dichiarato). [PROGRESS
   :407-421; pipeline map :77; decisioni utente ratificate]
5. **Le ASK sono enumerate e minimali**: collaborazione/procurement CFD-1;
   dati motore per il pin (imaging steady-mainstage o transition durations —
   R20); 3+3 documenti fermi + W-01/02/03; canale paper JPP. [PROGRESS
   :418-421; findings :2148; literature_registry :1232-1248]
6. **L'onestà è il vantaggio competitivo, e va detta come metodo**: falsificatori
   armati PRIMA dei numeri (claims :2262), gate D-44 che vincola questo stesso
   deck, ladder P34 dichiarata per ogni claim engine-level in slide. [TERM
   milestone, ADVISORY_Spres_prompt :233-235; ARMED GATE; finding :2538]
7. **La slide N-Q — la spina del value case** [WB1]: tre design (x\*_mean:
   il comparatore I4, "ZERO computed instances" NEL RECORD — il twin mai
   eseguito [WB1-C3-14] / x\*_pf: il nostro / x\*_3D: incomputabile), tre
   gap (formulazione / modello /
   composizione); working hypothesis DICHIARATA: (A)>(B) in-settore —
   **SEMPRE col tallone (J) sulla STESSA slide** ("state the hierarchy WITH
   the (J) heel, never without", CKP-S:253-254); death scenario = due
   fallimenti indipendenti, ciascuno misurabile; twin-first =
   kill-or-validate onesto; decisori pre-registrati, entrambi gli esiti
   informativi. Sulla slide anche la riga: "il campo non separa i tre gap —
   NOT-FOUND(q)" (query §1.2-bis). [IPOTESI DICHIARATA + regola C-3ter
   vincolante + query-bounded; CKP-S:198-255]
   Nota di forma per la slide PB-2 (punto 2): la classe si dice nella forma
   riconciliata [WB1-R1] — "nesting provato (THEOREM* sotto [C-HT4]);
   strictness = clausola enunciata senza prova scritta; carrier = PB-2
   OPEN" — mai "qui la struttura è tutta THEOREM".

---

## 6. Legenda minima (per il consumo storyboard, un termine = una riga) [W2-R10]

- **M-RED**: campagna di misura in-house dell'errore di riduzione (eps) del modello per-fase, prima campagna della fase F2.
- **CFD-2**: demo CFD accoppiata "paired" (nostro design vs baseline, template Li-Xu 2025), in coda F2.
- **CFD-1**: simulazione CFD massima (~12M-cell cost class) su configurazione accoppiata reale — il test del pin; decisione utente post-M-RED.
- **R22**: la linea di verifica CFD del programma (M-RED → CFD-2 → CFD-1) che decide le soglie di adeguatezza.
- **F2/F4b/F5**: fasi del piano di sviluppo (D6): F2 = teoria+campagne correnti; F4b = finestra truncated-plug/fitted-fronts (entry a F2-exit, D6 :233-238); F5 = finestra dati/hardware (RDE machine, D6 :252).
- **F3** [WB1, critic 8]: fase GEOMETRY CLASSES del piano (D6 :214-232), "plug/aerospike primary", 3-4 sessioni — la fase in cui si ottimizza un plug VERO; ordine-interscambiabile con F4b a F2-exit (D6 :228-232).
- **F6** [WB1, critic 8]: fase 3-D / HARDWARE BRIDGE (orizzonte, non budgetata; D6 :275-278): demonstrator B-lite elicoidale + ancora sperimentale (RK-E) o gap industriale #1 dichiarato.
- **Gap A/Gap B vs gap(A)/gap(B)** [WB1]: lettere SCAMBIATE tra il frame di valore §1.1 e le etichette argmax-level C-3bis: gap(A) pf-vs-mean ~ Gap B; gap(B) pf-vs-3D ~ Gap A — mappa dichiarata in §1.2-bis(i).
- **P-B / p_b / PB-2 / Gap B** [WB1, critic 9]: quattro oggetti distinti — box di disambiguazione completo in CH5 §1.1; casa definitiva CH-REF.
- **I4**: baseline a stato medio singolo (⟨Pc⟩, T0, γ) con design classico Rao/GENO (problem book).
- **N2**: lo slot dichiarato (non ancora aggiudicato) per la chiusura di base pressure p_b del programma.
- **eps / eps_U**: errore di riduzione misurato da M-RED; eps_U = suo livello uniforme sul basin esplorato (sweep-sup).

---

## Disposizione riparazioni (onda 2)

| Finding # | Classe | Disposizione |
|---|---|---|
| 1 | REPAIR | APPLICATO [W2-R1] — Q1: promessa di adeguatezza sostituita con "datum che stringe la soglia R26, sempre bracket con provenienza; D-44 vale in entrambe le direzioni" |
| 2 | REPAIR | APPLICATO [W2-R2] — §1.2, claim 6, Q2, deck 1: fusione famiglia-vs-I4 dichiarata PROPOSTA di consolidamento; baseline di record di Gap B (Veen/Angelino-at-mean) distinta da I4 (Rao/GENO) |
| 3 | REPAIR | APPLICATO [W2-R3] — Q3: accusa al campo riformulata al contenuto dell'ancora M0:1335-1339 (nessun lavoro ottimizza il 3D vero; sweep = ranking-signal only), senza attribuzione di intenti |
| 4 | DOWNGRADE | APPLICATO [W2-R4] — Q4(ii): stato della guardia declinato (T0-flatness armato; f_cycle e A20 nominati "none wired", findings :1926, owner F2/VI.1) |
| 5 | GAP | APPLICATO [W2-R5] — §1.2 + claim 5 + deck 2: locked formulation D-06 verbatim + near-miss Efremov-Kraiko 2004 come query-bound (ancora verificata M0:2320-2329) |
| 6 | REPAIR | APPLICATO [W2-R6] — §1.2: classe della rottura ancorata alla sharpness clause M0:2316-2319 + "nesting ... THEOREM (standard)" M0:3524-3525 (ancore verificate) |
| 7 | DOWNGRADE | APPLICATO [W2-R7] — Q2(c) + deck 4: "prezzata"/"prezzi" sostituiti con "cost-classed"/"classi di costo"; prezzi assoluti = OPEN, dossier post-M-RED |
| 8 | NOTE | APPLICATO [W2-R8] — unita' di "~0.3M" marcata [INF] (non dichiarata all'ancora) + divieto di slide; miglioramento senza rischio |
| 9 | GAP | APPLICATO [W2-R9] — nuova Q7 sull'indecidibilita' odierna di "Gap A < Gap B" con percorso di decidibilita' dal record (value-route 2*sqrt(eps_U/mu_red) verificata a M0:1348, deriver chain E29) |
| 10 | GAP | APPLICATO [W2-R10] — legenda minima 8 righe in coda (§6): M-RED, CFD-1/2, R22, F2/F4b/F5, I4, N2, eps |
| 11 | NOTE | APPLICATO [W2-R11] — Q2: i due "primo" query-bounded (per costruzione / perimetro R20 search-proven); miglioramento senza rischio |

---

## 6-bis. STORIA (writer W-B.2, 2026-08-23 — trittico [V2-R2]; ogni
## battuta porta DATA + PROCESSO + VERDETTO, campi di join del
## retro-audit §5-bis; header "6-bis" perché il §6 del capitolo è già la
## legenda W2-R10 — posizione template rispettata: dopo aperti, prima di §7)

### 6-bis.1 Il frame Gap A / Gap B

- **Battuta 1 — derivazione originale.** DATA: 2026-08-20 (finestra C4
  mid-window 6, commit 904f950: "Gap-A/Gap-B value frame" ratificato;
  registrazione checkpoint
  `validation/sfoundations_raws_2026-08-13/SESSION_STATE_checkpoint.md:466-472`).
  PROCESSO: la domanda "quanto vale il programma" resa DECIDIBILE — Gap B
  misurabile in-house (paired-run F2), Gap A bounded-only. VERDETTO:
  value condition di record "Gap B material AND Gap A < Gap B".
- **Battuta 2 — (c) NON-RIDERIVATO; doppia prova = REFUTE_CH6 + panel.**
  DATA: 2026-08-20 (judge del centerpiece R22F, VERDICT_r22f: 22
  amendment carried / 0 contested sustained, commit 1a11f2c — è il panel
  che ha prodotto la forchetta con la cella (vi) nella sua forma onesta)
  + 2026-08-23 (REFUTE_CH6.md, onda W-A, riparazioni disposte nel blocco
  di questo capitolo). PROCESSO: 4 round × 3 lenti + 27 probe eseguibili
  sul centerpiece; refuter d'onda sull'atlas. VERDETTO: il frame regge
  CON la guardia "delta AND L_H UNDERIVED" intatta.
- **Battuta 3 — convergenza.** DATA: 2026-08-20 (forma finale del canale
  (vi), commit 904f950: "no argmax-shift number at any grade, derivers
  ordered five-field→route-B→M-RED→R22-CFD"). PROCESSO: escalation
  refuter fino alla forma onesta. VERDETTO: classe finale SCHEMA con
  falsificatore ARMATO (claims:2262) — chi cita un numero prima dei
  deriver viola il registro.

### 6-bis.2 Il nodo N-Q ("quale gap domina?") — nato dalle correzioni
### utente C-3 / C-3bis / C-3ter (verità storica di questa finestra)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-23 (checkpoint
  S-PRES sessione 2,
  `validation/spres_raws_2026-08-22/SESSION_STATE_checkpoint.md:198-256`).
  PROCESSO: domanda utente di record elevata a FIRST-LEVEL TREE NODE
  ("which gap dominates, on which axis?") sul frame a tre design C-3
  (x*_mean con ZERO istanze computate / x*_pf / x*_3D incomputabile).
  VERDETTO: working hypothesis DICHIARATA e falsificabile — formulation
  gap plausibilmente dominante IN-SECTOR, model gap dominante come
  rischio CROSS-SECTOR; entrambi gli esiti pre-registrati informativi.
- **Battuta 2 — (b) STANCE-DI-FORK (le tre battute utente, ciascuna col
  suo verdetto dichiarato come stance).** DATA: 2026-08-23, in
  sequenza nella stessa finestra. PROCESSO e VERDETTI per-riga:
  (i) **C-3bis** (user press): l'analisi comparativa precedente MISCHIAVA
  gli assi (eps-free vs constrained) — "user catch correct" a checkpoint;
  forma corretta a (eps,L) FISSI: gap(A) NON ha teoremi di soppressione
  (Jensen sulla densità di forma G su escursioni 10:1) mentre gap(B) ne
  ha TRE ([T-T0P], K-bar=0, T-DISC) — quindi PLAUSIBILMENTE
  |x*_pf − x*_mean| > |x*_3D − x*_pf| a vincoli fissi; STANCE: "declared
  hypothesis, not theorem", con lo scenario-morte utente decomposto in
  DUE fallimenti indipendenti misurabili separatamente (twin-first =
  kill-or-validate onesto). (ii) **C-3ter** (user catch, finale):
  l'oblique shock rotante è visto dal per-phase solo come SHADOW
  data-anchored; i teoremi di soppressione coprono la parte
  SMOOTH/avvettiva; il canale (J) (salti del fronte) è il primo ordine
  NON soppresso di gap(B) — tallone d'Achille NOMINATO della gerarchia,
  senza numero (SBV-conditional, delta underived). VERDETTO complessivo
  (stance): gerarchia (A)>(B) asseribile SOLO col tallone (J) dichiarato.
- **Battuta 3 — convergenza.** DATA: 2026-08-23 (regola deck/atlas a
  checkpoint). PROCESSO: "state the hierarchy WITH the (J) heel, never
  without"; deciders ordinati (twin a vincoli identici PRIMA, poi M-RED
  front legs B-1/B-3, 5F sign test su decisione utente pendente,
  CFD-2/CFD-1); G2 kill-gate = morte onesta. VERDETTO: classe finale =
  ipotesi di lavoro dichiarata con falsificatori nominati e ordine di
  esecuzione — la storia del nodo È la catena delle tre correzioni
  utente, portata qui come verità storica.

### 6-bis.3 PB-2 e la formulazione LOCKED (D-06)

- **Battuta 1 — derivazione originale.** DATA: 2026-08-04 (PAN-S14: T4 e
  il suo meccanismo al rango di record; la sharpness clause vive nel
  blocco T4, M0:2316-2319) con carrier problem book PB-2
  (`docs/rde_nozzle_problem_book.md:532-537`). PROCESSO: teorema di
  nesting + clausola di rottura (troncamento / length cap /
  base-pressure). VERDETTO (forma riconciliata CH1 Q4): nesting PROVATO
  (THEOREM* sotto [C-HT4]); STRICTNESS = clausola enunciata DOPO il QED
  SENZA prova scritta; carrier quantitativo = PB-2, OPEN.
- **Battuta 2 — (c); doppia prova = sweep adversarial + lock di
  formulazione.** DATA: 2026-08-13. PROCESSO: il near-miss
  Efremov-Kraiko 2004 TROVATO dallo sweep 1971-2026
  (`validation/ADVISORY_litmap_extension_2026-08-13.md`) e CONSUMATO
  nella formulazione LOCKED D-06 (batch R4, commit ea2abce: "PB-2 LOCKED
  formulation + 7-item caveat list"; blocco M0:2320-2326,
  page-verified). VERDETTO: il claim di novità sopravvive SOLO nella
  forma vincolata "first genuinely averaged and NON-COLLAPSING shape
  problem" — la frase generica è DEAD of record.
- **Battuta 3 — convergenza.** DATA: 2026-08-21 (C61 mintata alla
  coverage gate, commit fd2d444 — il trigger del computo). PROCESSO:
  ricognizione dei prerequisiti (chiusura p_b N2, baseline
  mean-designed). VERDETTO: classe finale = flag-problem OPEN con
  formulazione locked; il numero PB-2 MAI computato, e il record lo
  dice.

### 6-bis.4 Le guardie pubbliche D-44 e P34

- **Battuta 1 — derivazione originale.** DATA: 2026-08-21 (pipeline
  decision map di record, commit da91aa4: riga D-44 "ARMED
  GATE" con arco E31 esplicito verso S-PRES,
  `docs/rde_nozzle_pipeline_decision_map.md:180`; riga P34 CONFIRMED
  `docs/findings_registry.yaml:2530-2539`, restaurata come SEED-OMIT
  alla coverage gate, commit fd2d444). PROCESSO: mappa + coverage gate
  C4. VERDETTO: claim pubblici di adeguatezza GATED; gerarchia di
  evidenza engine-level mai aggiudicata = gap dichiarato con owner.
- **Battuta 2 — (c) (guardie di governance, non derivazioni); doppia
  prova = il loro stesso fuoco su QUESTA milestone.** DATA: 2026-08-23
  (S-PRES sessione 1, Block 0 CLOSED, commit d968502: trigger-scan
  eseguito — item (ii) D-44 recepito, P34 istanziazione leggera;
  `docs/rde_nozzle_PROGRESS.md:400-401`). PROCESSO: trigger sweep da
  comando misurato al Block 0. VERDETTO: le guardie hanno SPARATO
  sull'atto esterno previsto e sono state consumate, non aggirate.
- **Battuta 3 — convergenza.** DATA: 2026-08-23 (questo atlas).
  PROCESSO: D-44 vincola il deck in costruzione (forchetta = bracket
  con provenienza, MAI adequacy dimostrata). VERDETTO: classe finale =
  ARMED GATE + finding con owner (F2/F5; P-1/G5-G6 claims window).

### 6-bis.5 R26: sizing vs ranking (la soglia, non la contraddizione)

- **Battuta 1 — derivazione originale.** DATA: finestra campagne
  letteratura 2026-08-13→2026-08-21 (la riga findings:2148 porta
  l'aggiudicazione; la datazione per-riga non è esibita nel capitolo —
  dichiarato come limite di join). PROCESSO: confronto Paxson-Miki
  (adeguato per sizing, 6.54 vs ~6.5) vs Harroun 2021 (c_F=1.25
  identico = non-discriminazione al ranking). VERDETTO: "not a
  contradiction, a RESOLUTION THRESHOLD" — PARTIALLY adjudicated, soglia
  OPEN decisa da R22.
- **Battuta 2 — (c); doppia prova = forchetta + dichiarazione
  strutturale.** DATA: 2026-08-20. PROCESSO: canale (iv) della forchetta
  con BEST/WORST espliciti (M0:1346) + la dichiarazione strutturale
  NO-EXTERNAL-REFEREE mandata in forchetta su disposizione (c)
  dell'injection C3 (commit 318d3fd; [REV2-r1-15], M0:1322-1331, con i
  nearest referee nominati e squalificati [GRAFT-G10]). VERDETTO: la
  tensione è portata come soglia con entrambe le sponde ancorate.
- **Battuta 3 — convergenza.** DATA: 2026-08-23 (forma vincolante
  [WB1-R3] in §1.4). PROCESSO: wording fissato — sizing "SUPPORTATO a
  ~1% su UN'istanza esterna", mai "dimostrato". VERDETTO: classe finale
  [REP]-per-sizing su una istanza / OPEN dichiarato sul ranking;
  decider = R22/M-RED.

## 7. Posizionamento / conformity (template §7; nodi N-O/N-L/N-Q) [WB1]

**(a) STRUMENTI — clausola di vacuità [V2-R4]**: NESSUNO STRUMENTO
PROPRIO. Puntatori alle celle FUORI-PERIMETRO della tabella §M del design
v2 + emendamento: **O-ii** ("nessuno strumento proprio; CH6 §7(a) =
clausola di vacuità [V2-R4]"), **L-ii** (la spina è governance; la SOTA
tool matrix D6 §4 :737 è ASSORBITA nella colonna (ii) trasversale
[V2-R11]), **Q-ii** (i decisori — twin, M-RED, 5F, CFD — sono strumenti
delle righe B/D/E/I, assorbimento dichiarato, emendamento §1d). Il lint 5
riconosce la clausola.

**(b) SENSO**: vive in §1.1-§1.4 e §1.2-bis di questo capitolo e nella
colonna-senso trasversale di CH5.

**(c) STANDARD DI RIFERIMENTO (lint 6)**: il metodo di questo capitolo è
governato dall'asse **§C-2 (classe GRADE)** della conformity map del
design v2 — ogni claim di valore porta la classe dichiarata, "NO cell
above its held evidence class" (M0:1309); divergenza dichiarata come da
mappa (si adotta la STRUTTURA di GRADE — livello + ragioni di
upgrade/downgrade — non i domini clinici). Il consumo deck è governato
dall'asse **§C-6 (assertion-evidence)** col retro-audit dichiarato.
Nessun claim "SOTA" è fatto in questo capitolo fuori da questi assi.

---

## 8. Decision card delle scelte presentate (lint 8; emendamento §1g) [WB1]

Questo capitolo presenta due scelte del choice ledger (C61 in §1.2/Q6;
C59 in Q4); entrambe classe NEVER → card "non-aggiudicata, finestra Y"
STAMPATA (mai omesse, §1g).

**[WB1-C3-17 — decisione anti-entropia sulla card C61]: la card C61 di
QUESTO capitolo è la PRIMARIA.** Ragione: la scelta è presentata qui
come parte costitutiva di PB-2 (§1.2: cosa manca per computarlo; Q6: il
rischio-artefatto), e il trigger di C61 è PB-2-shaped ("first
truncated-plug (value,delta) row ... or F4b window entry", ledger :829)
— la casa naturale è il capitolo del value case. Ogni altra occorrenza
(CH8; il puntatore CH4 §7-bis "CH8/CH10", impreciso per nota del
refuter) va ridotta a PUNTATORE a questa card — mai due card gemelle;
la riduzione lato CH8/CH4 è disposta all'orchestratore (file non miei).

**CARD C61 — chiusura base-pressure p_b (truncated plug / shrouded):**

1. **Scelta**: C61 (`docs/choice_ledger.yaml:818-830`) — chiusura p_b;
   incumbent DICHIARATO senza adozione di programma: Veen 0.846·p/M^1.3
   praticata nella SOLA catena legacy; lo slot di programma è N2.
2. **Alternative censite (data + fonte survey)**: WG10 empirical bracket
   [+19%,−15%]; Nasuti-Onofri transition-PR ([MODEL-VAL], WG10 pp. 10-11);
   derived N2 closure (verdetto WG10 su Eq. (5.1): "N2 MUST REPLACE IT");
   measured V1.4-class CTAP (Purdue, unica misura RDE, Pa/Pc~0.15) —
   survey = `BASE_PRESSURE_HARVEST_c4.md` (campagna arrivi
   S-FOUNDATIONS-C4, **2026-08-20**; mint riga ledger 2026-08-21).
3. **Verdetto + perché**: **NON AGGIUDICATA** (status NEVER) — incumbent
   legacy WG10-FAILED, nessun default silenzioso: lo slot resta dichiarato
   finché il trigger non spara.
4. **RECENCY/SOTA check**: la survey (2026-08-20) copre il corpus classico
   delle chiusure p_b (WG10/Humphreys/Nasuti-Onofri) + l'UNICO dato RDE
   hot-fire esistente (Purdue CTAP); check 2026-08-23: nessun elemento
   nuovo entrato nel record da allora. ATTUALE(chiusure p_b classiche +
   unico dato RDE hot-fire, 2026-08-23).
5. **Falsificatore**: una riga (value,delta) truncated-plug computata
   SENZA sensibilità alla chiusura dichiarata = violazione (nota C61: la
   chiusura muove il DESIGN — Humphreys ×2.45); una misura CTAP-class
   fuori dal bracket dichiarato uccide la chiusura adottata.
6. **Trigger di ri-esame + finestra**: verbatim ledger :829 — "first
   truncated-plug (value,delta) row entering the record, or F4b window
   entry — whichever fires first" (collocazione F4b: §1.5 [WB1-R5]).

**CARD C59 — forma temporale del funzionale (cycle-average):**

1. **Scelta**: C59 (`docs/choice_ledger.yaml:795-805`) — cycle-average vs
   harmonic-balance adjoint vs time-spectral vs windowed unsteady adjoint.
2. **Alternative censite (data + fonte)**: HB adjoint / time-spectral /
   windowed unsteady adjoint — ancore di record `rubino_2018`,
   `schotthofer_2024`, `zahr_persson_2016` (registry, root D,
   READ-INTEGRAL); censimento alla mint **2026-08-21**
   (`BRIEF_blocco2_phaseD_addendum_c4.md` §(e), scoping BINDING).
3. **Verdetto + perché**: **NON AGGIUDICATA** nel senso del ledger (status
   NEVER) MA con scoping vincolante di record: dentro il pin
   onda-periodica il cycle-average è "CANONICAL-INSIDE-THE-PIN ... a
   theorem-backed CONSEQUENCE, not a choice"; le alternative vivono SOLO
   nei regimi a pin indebolito — la riga non riapre MAI il funzionale del
   regime pinnato.
4. **RECENCY/SOTA check**: censimento temporal-form datato 2026-08-21 sul
   root D del registry (HB/time-spectral/windowed); check 2026-08-23:
   nessun ingresso nuovo nel record. ATTUALE(root D registry +
   addendum-c4 §(e), 2026-08-23).
5. **Falsificatore**: un regime a pin indebolito (multi-frequenza /
   aperiodico) che entra nello scope senza ri-aggiudicazione della riga =
   violazione; dentro il pin, un controesempio alla canonicità del
   quoziente romperebbe C59 e con esso il layer T0.
6. **Trigger di ri-esame + finestra**: "F2-entry census window; trigger =
   any weakened-pin regime (multi-frequency / aperiodic / windowed)
   entering scope" (ledger :804).

---

## Disposizione W-B.1 (slot B5; celle L-v/O-v/Q-i/Q-iii/Q-iv/Q-v; critic 7/10/13/18/19)

| # | Item del mandato | Disposizione |
|---|---|---|
| Q-i/Q-iv | §1.2-bis N-Q | APPLICATO [WB1-R2] — frame three-design + working hypothesis + tallone (J) (guardie 1/16) + death scenario + decisori, tutto ancorato ALLA RIGA a CKP-S:198-255 |
| Q-iii | query "il campo separa i tre gap?" | ESEGUITA in-window, perimetro chiuso G-11 → NOT-FOUND(q), near-object nominati, STOP; eco CH5 §1.6 |
| Q-v | decisioni pendenti | APPLICATO — A-9 (§3): twin (a)/(b) + S-5F A/B/C + C51, owner utente, finestra ~01/09 |
| critic 7 | G2 VALUE GATE + thrust-stand | APPLICATO [WB1-R4] — §1.5 + Q1 (D6 :776-782 verificata in finestra) |
| critic 10 | PB-2 forma CH1 | APPLICATO [WB1-R1] — §1.2 riconciliato (nesting THEOREM* / strictness senza prova scritta / carrier PB-2 OPEN) + nota slide in §5.7 |
| critic 13 | hedge sizing single-instance | APPLICATO [WB1-R3] — §1.4 + Q1 (forma CH3 W2-R2) |
| critic 18 | collocazione F4b | APPLICATO [WB1-R5] — §1.5 (D6 :228-238 verificata) |
| critic 19 | canale paper P-1 + P-2 freeze | APPLICATO [WB1-R7] — §1.6 (D6 :85-100 verificata) + riga claim 21 |
| [V2-R11] | riga rischi → RISK REGISTER | APPLICATO [WB1-R6] — §1.5 (D6 §7 :1093, RK-A/B/C) |
| critic 14 | scope R20 vs CFD | APPLICATO [WB1-R8] — §1.6 (metà CFD in CH5 §1.2) |
| critic 8 | legenda F3/F6 | APPLICATO — §6 (D6 :214-232, :275-278) |
| §1g | decision card | APPLICATO — §8: card C61 + C59 "non-aggiudicata, finestra Y" (6/6 campi, token ATTUALE) |
| [V2-R4] | vacuità §7(a) + metà (c) | APPLICATO — §7 (celle O-ii/L-ii/Q-ii; assi §C-2/§C-6) |
| §3-bis | antenati LL-21/LL-22/LL-35 + N-Q | APPLICATO — §3-bis (join {LL-id}, dicitura MINT-PENDING F-2 uniforme §6c) |

---

## DECK FEED (asserzioni candidate-slide; frase piena + ancora + classe)

1. "Tre design: x\*_mean — il comparatore I4, con ZERO istanze computate
   NEL RECORD ("I4 comparator has ZERO computed instances": il
   comparatore del twin non è mai stato eseguito; il campo computa
   design a stato medio, ma mai questo confronto) — x\*_pf (il nostro) e
   x\*_3D (incomputabile): tre gap — formulazione, modello, composizione
   — e la domanda di valore è quale domina, su quale asse." —
   CKP-S:198-204 — frame di record (N-Q). [WB1-C3-14 riparato: scope =
   il record del programma, MAI "nel campo".]
2. "A vincoli fissi (eps,L) e settore fisso il gap di formulazione non ha
   alcun teorema di soppressione, mentre il gap di modello ne ha tre sulla
   parte liscia ([T-T0P], K-bar=0 fiberwise, [T-DISC]): plausibilmente
   (A)>(B) in-settore — ipotesi dichiarata e falsificabile, non teorema."
   — CKP-S:215-230 — IPOTESI DICHIARATA. [VINCOLO: questa asserzione va
   in slide SOLO insieme alla 3 (tallone (J)) — guardia 1, mai separate.]
3. "Il tallone dichiarato della gerarchia: i front jumps (J) sono il primo
   ordine NON soppresso del gap di modello (SBV-conditional, delta
   underived); se (J) è grande, il modello può dominare anche in-settore
   — la gerarchia non si enuncia MAI senza questa riga." — CKP-S:245-254
   — regola C-3ter (guardia 1).
4. "Lo scenario di morte del programma richiede DUE fallimenti
   indipendenti, e ciascuno è misurabile separatamente: (A) dal TWIN a
   vincoli identici (cheap, per primo — kill-or-validate); (B) dalle front
   legs di M-RED + 5F sign test." — CKP-S:230-237 — decisori
   pre-registrati, entrambi gli esiti informativi.
5. "Il campo non separa i tre gap: NOT-FOUND(q) su perimetro chiuso
   (registry 174 id + litmap + P-A..P-D); i near-object sono
   decomposizioni di perdita di flusso (P-B F-15), mai di gap di design."
   — CH6 §1.2-bis (query in-window) — claim query-bounded.
6. "Il programma ha un kill criterion theorem-grade: G2 VALUE GATE — gap
   < ~1% Isp su N1-N4 → pivot nominato a certificazione/operabilità
   (honest death); l'ambizione si calibra su accuratezza thrust-stand-class
   ~0.5-1%." — D6:776-782 — gate di piano.
7. "La value condition 'Gap B material AND Gap A < Gap B' è un rejector
   armato, oggi INDECIDIBILE — e lo diciamo: nessun numero esiste su
   nessun lato prima di M-RED." — checkpoint S-FOUNDATIONS :466-472;
   M0:1348 — frame + SCHEMA, D-44 gated.
8. "PB-2: il nesting è provato (THEOREM* sotto [C-HT4]); la strictness è
   clausola enunciata senza prova scritta; il carrier quantitativo è PB-2,
   OPEN e mai computato." — M0:2303-2319; CH1 Q4 — forma riconciliata.
9. "Roadmap con ordine e classi di costo: M-RED (cheap decisive unlock) →
   CFD-2 (paired, template Li-Xu) → CFD-1 (~12M-cell, decisione
   post-M-RED); F3/F4b a F2-exit ordine-interscambiabili; canale paper
   P-1 JPP + P-2 freeze FIRED 2026-08-11." — PROGRESS:407-421;
   D6:228-238, :85-100 — decisioni ratificate.
10. "L'onestà è strumentata, non dichiarata: D-44 arma questo stesso deck,
    ogni claim engine-level porta lo stage P34, le scelte non aggiudicate
    portano card stampata con finestra." — pipeline map :180; findings
    :2538; §8 — gate armati.
