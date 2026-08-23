# CH2 — Il sistema di ottimalità mediato: (**'), shared wall, adjoint per-fase

Capitolo di ricostruzione S-PRES (2026-08-22/23). Stadio di confronto: record
aggiudicato (M0, claims registry, P1 draft §5, choice ledger, log suite).
Questo testo NON aggiudica nulla di nuovo: ricostruisce, ancora, dichiara gli
aperti. Ogni claim porta classe di rigore e ancora file:riga letta in finestra.

---

## 1. Ricostruzione

### 1.1 Da dove nasce il sistema

Il problema variazionale consegnato da §2–§4 del P1 — massimizzare
J[Sigma] = Int F[Sigma; s(xi)] dmu(xi) su contorni ammissibili, con vincoli
Euler stazionari PER FASE, portata fissata PER FASE, vincoli geometrici
CONDIVISI — ha un sistema di stazionarietà la cui struttura è "the paper's
implementable core" (docs/rde_nozzle_P1_sections_5_7.md:41-45). La struttura è
in TRE blocchi, ed è questa tripartizione (cosa è per-fase, cosa è condiviso)
che porta tutto il contenuto fisico del metodo. Formalizzazione di record:
[T-T7FS] in M0 (docs/rde_nozzle_MASTER.md:2812-2941). [W2-R1] Le classi vanno
tenute SPLITTATE come le stampa il record: la STRUTTURA a tre blocchi è
THEOREM-SCHEMA, "Stationarity structure (verified formally)" (M0:2812, 2818);
il THEOREM* del registry (docs/claims_registry.yaml:576-587, statement :580)
copre esattamente la differenziazione sotto l'integrale di ciclo — cioè che
(b)+(c) siano enunciati L^1(dmu) genuini e (P)(ii) condizione necessaria
rigorosa (prova in docs/rde_nozzle_T7_P7_functionspace.md, M0:2935-2941).

[W2-R8] Notazione (glosse one-line per il consumer deck/Q&A): G_xi(x) =
densità di forma di Hadamard della fase xi (la derivata del funzionale
rispetto a uno spostamento normale della parete nel punto x); g_L = densità
di forma del vincolo geometrico condiviso (lunghezza), con moltiplicatore
lambda_L; (P)(ii) = la parte "condizione necessaria del primo ordine" del
problema variazionale (P) come posto; N_K/T_K = normal cone / tangent cone
dell'insieme ammissibile K nel punto di ottimo.

### 1.2 Blocco (a) — adjoint Euler per-fase e il first integral f2 = -lambda2

Per q.o. xi il sistema adjoint di Euler della fase. Nella sottoclasse
IRROTAZIONALE-OMOENTROPICA di S1 (qualificatore di scope S21, audit C1: sui
membri rotazionali l'identificazione sopravvive solo a livello di CAMPO) esso
si riduce alla forma chiusa classica del contouring thrust-optimal: la
superficie di controllo ottima è la caratteristica C+ tracciata all'indietro
dal lip e FERMATA AL BORDO DEL KERNEL (S19 locus correction di record: sul C+
completo fino all'asse l'invariante deriva 2.9e-01 e l'identità sarebbe
falsificata; sulla superficie kernel-stopped il drift misurato è 9.5e-03,
re-issue in norma registrata 9.4809e-03) — P1_sections_5_7.md:47-58;
M0:2819-2826. Lungo di essa il first integral

    f2 = V cos(theta -/+ alpha)/cos(alpha) = -lambda2(xi)

identifica il moltiplicatore di portata della fase con i soli dati al lip
[T-P3] (P1:58-63; M0:2826). [T-P3] è THEOREM* in S1 shock-free: lambda2(xi)
unica, misurabile, L^inf(dmu); attraverso fronti fittati eredita [C-MAJDA]
(M0:2930-2934; prova docs/rde_nozzle_P3_multipliers.md, residui R-P3.1/2 ivi
nominati). L'identificazione di questa macchina classica CON l'adjoint
continuo è contenuto del paper compagno (P-2 Lemma A; P1:62-64 e §5.3).

### 1.3 Blocco (b) — SHARED WALL: la frase di design del programma

    Int_Xi G_xi(x) dmu(xi) + lambda_L g_L(x) = 0   q.o. x sulla parete,

con G_xi la densità di forma di Hadamard della fase (P1:66-71; M0:2827-2829).
La lettura è il fatto centrale di design del paper, verbatim dal testo di
record: "NO phase satisfies its own wall condition — the mu-average does. A
cycle-optimal wall is not the optimal wall of any operating point"
(P1:68-71). Classe: parte di [T-T7FS], THEOREM* — la condizione a parete è un
enunciato genuino L^1(dmu) grazie alla differenziazione sotto l'integrale di
ciclo (registry :580; M0:2935-2941).

### 1.4 Blocco (c) — la weighted transversality (**') in FORMA CONO (C31)

Forma di record, user-ratified 2026-08-13 (P1:72-94; M0:2830-2861):

    D := Int_Xi (dF/ds_E)[Sigma; s(xi)] dmu(xi)  in  N_K(s_E*),

cioè <D, d> <= 0 per ogni d in T_K(s_E*), con K = insieme ammissibile
dell'endpoint CONDIVISO, DICHIARATO per ogni enunciato e strumento. Tre casi:
K localmente non vincolato => D = 0 (l'uguaglianza free-endpoint — Rao
Eq. (14), la vecchia forma stampata); K = {punto} (fixed-(eps, L)) =>
condizione vacua, i lambda sono componenti di D a segno libero — il regime in
cui vivono TUTTE le istanze eseguite (il driver committato fissa il lip per
UGUAGLIANZA, a1_toc_variational_jax.py:1748, M0:2840-2845); K con cap
unilaterali ((P) come posto) => segno + complementarità per componente,
direzione DERIVATA dal lato attivo (KT2015 (2.10)). La portata per-fase resta
UGUAGLIANZA fuori dal cono (KT2015 (2.13); M0:2852-2854).

D fattorizza come R(xi)·w(xi): R il residuo di corner classico (la condizione
endpoint di Rao mono-fase), w > 0 peso geometrico-cinematico; la
fattorizzazione è STRUTTURA DERIVATA, non modellata (P1:87-89, 141).

CONE TRANSFER LEMMA [T-T7CN], THEOREM elementare con prova di record
(M0:2862-2874): in-cono fase-per-fase mu-q.o. implica in-cono del ciclo; la
CONVERSA È FALSA (controesempio a due fasi di record: N_K = [0,inf),
D(xi_1) = -1, D(xi_2) = +3, media +1 dentro con la fase 1 fuori). Conseguenza
strumentale: uno scan di segno all-in-cone CERTIFICA senza mediare
(sufficiente, non necessario); ogni tool armato su di esso deve ACCETTARE una
famiglia one-phase-out/mean-in (rejector S3 di record, A39; M0:2871-2874).

CONTENT SPLIT (M0:2875-2884; P1:90-94): la componente assiale è puntualmente
e identicamente >= 0 — la sua condizione di ciclo è automatica per il lemma,
il suo contenuto è binario (attività del cap di lunghezza, lambda_L =
Int (-lambda3/q) dmu >= 0, il gemello di lunghezza di [T-P3] via Rao Eq. (13),
M0:2885-2894). La componente RADIALE cambia segno lungo il ciclo (fasi sovra-
e sotto-espanse): TUTTO il contenuto di averaging della condizione unilaterale
vive lì.

### 1.5 Il BOXED WARNING (e il suo gemello)

Testo di record (P1:96-114; M0:2856-2861): il peso w(xi) è indipendente dalla
fase ESATTAMENTE nella classe di collasso T3 — lì, e solo lì, (**') si riduce
alla media naive non pesata delle condizioni di corner classiche. Ovunque
altrove LA MEDIA NAIVE È SBAGLIATA: mediare gli ottimi per-fase, o mediare i
residui di corner non pesati, produce un contorno che non soddisfa NESSUNA
condizione di ottimalità del problema mediato. Ogni implementazione deve usare
(**'). La classe eps* stantia a -2.39% colpita in §4.3 era esattamente un
artefatto di media naive (P1:106-107). [W2-R6] Che cosa È la classe T3: la
classe di collasso [T-T3] (M0:746-754) — un solo gamma frozen comune a tutte
le fasi, parete fissa full-flowing con uscita supersonica a ogni fase
(interno ambient-blind), forma d'ingresso adimensionale fase-indipendente
(le fasi differiscono solo per (P0(xi), T0(xi))); lì, per teorema,
J[Sigma] = F[Sigma; <Pc>_mu] puntualmente e l'ugello ottimo di ciclo È il
contour classico disegnato alla pressione media. TWIN WARNING (C31): il peso NON deforma
il cono — pesatura e unilateralità sono correzioni INDIPENDENTI; in regime
unilaterale la forma naive può inoltre certificare come KKT-ammissibile un
punto DUAL-INFEASIBLE (segni opposti di Int R dmu vs Int R w dmu — il
falsificatore a due segni di record, qualificato per regime; P1:108-113;
M0:2895-2907, con qualificatore: la lettura dual-infeasibility ha contenuto
SOLO a cap unilaterale attivo).

Punto dottrinale ereditato dal corpus classico (P1:116-121; verificato su
cinque fonti primarie, docs/rde_nozzle_literature_map.md:401-404): la
pressione ambiente entra nel problema variazionale SOLO attraverso la
transversality d'endpoint, mai nelle equazioni di campo — quindi tutta la
ciclo-dipendenza della condizione d'endpoint è portata dalla fattorizzazione
peso-residuo.

### 1.6 Classi e conditionals (la "spina dorsale" unica)

Voce di onestà del paper (P1:128-150): differenziazione sotto l'integrale di
ciclo — quindi che (b)+(c) siano enunciati L^1(dmu) genuini e (P)(ii) una
condizione necessaria rigorosa — è THEOREM* [T-T7FS], che eredita L'UNICO
conditional analitico nominato del programma ([C-D25U], stabilità semiglobale
uniforme della mappa soluzione S1; registry :583); [T-P3] THEOREM* eredita
[C-MAJDA] sui fronti fittati; il calcolo di forma multi-D con shock fittato si
riduce alla teoria 1-D verificata dentro S1 [T-G12S1] (M0:2962). "One
conditional spine, stated once, inherited by ID — not a diffuse cloud of
caveats" (P1:137-138). In aggiunta, ipotesi nominata H-EXO su [T-T7FS]
(registry :1929): esogeneità della misura di ciclo e della mappa di stato —
garantita su L4 da [T-NSW], diventa LOAD-BEARING a F5 (RDE accoppiato).

### 1.7 La riduzione quasi-1D eseguibile e i rejector

Con il solo DOF area d'uscita (il rung su cui vivono §6–§7), i blocchi
(b)-(c) degenerano a UNA condizione scalare [T-T7RED], classe THEOREM
(P1:152-189): <P_E(eps; xi)>_mu = Pa. Forma PRIMARIA di record: inversione
reale dell'area-ratio per fase sull'isentropa Cantera frozen-CJ, gamma(T)
variabile — eps*_real = 3.49–3.52 sulla griglia PR = 1–90 (carrier run_all
gruppo (xii), numeri in data/phase_diagram_real.json; P1:165-170). La forma
chiusa NPR(eps*) = <Pc>/Pa è DECLASSATA a oracolo dichiarato gamma-const, mai
passo di solver (P1:171-174, pin motore M0 VI.4bis(iii), claim C13).

I rejector eseguibili, AL LORO RANGO (istanze del meccanismo al DOF più
semplice, NON prova del confronto di formulazione a DOF pieno):

- T1c (tests/test_bell_optimality.py:13-15, 75-85): la condizione
  plausibile-ma-sbagliata a media PESATA IN MASSA NPR = <Pc>_mdot/Pa dà un
  eps misurabilmente più grande e Isp strettamente minore. Numeri misurati di
  record (validation/s25bis_closing_suite.log:61-76): eps* 3.80 vs alt 5.48
  (H2/20, dIsp +4.94 s); 21.16 vs 32.01 (H2/200, +3.33 s); 3.98 vs 6.61
  (CH4/20, +7.45 s); 23.30 vs 40.57 (CH4/200, +5.06 s); 3.94 vs 7.07
  (RP-1/20, +9.71 s); 22.69 vs 42.51 (RP-1/200, +6.30 s). Range dIsp
  +3.33…+9.71 s su 6 casi.
- G5/G6 (tests/test_gamma_probe.py:22-27, 121-142): G5 = struttura a
  inviluppo 0 < penalty <= shift^2 (la penalità di design è di SECONDO
  ordine mentre lo shift della condizione è di primo ordine: shift eps*
  -0.56%, penalty Isp ~3e-6, righe 99-107); G6 = la chiusura pesata
  gamma_eff = <Pc gamma>/<Pc> riproduce lo shift vero (<0.1 pt), la media
  NON pesata <gamma> è RIGETTATA (>1 pt), e un record corrotto
  (gamma_s invertito) è RIGETTATO (controllo negativo).
- gruppo (vi)/(xii): il boxed warning "è un test, non una frase"
  (P1:176-179) — il rejector wrong-averaging rigetta la media naive (la
  classe -2.39%) e il carrier (xii) verifica che la media non pesata NON
  riproduce l'eps* pesato oltre barre derivate.

### 1.8 Il bridge P-2 e la genealogia classica

L'identificazione macchina classica ⇄ adjoint continuo (superficie
caratteristica = superficie di chiusura adjoint, f2 = invariante adjoint
trasportato, condizioni di corner = transversality) è contenuto del compagno
P-2 (Lemma A; lato discreto Lemma B: reverse-mode AD della marcia MOC fittata
= sweep adjoint trasposto) — P1:191-207; classi: sistema classico per-fase
THEOREM ([T-LEMA-CL], [T-A2], [T-A3]), identificazioni di componente
THEOREM*/pending il residuo numerico O3.3 [C-O33] (P1:200-203).

Banche del bridge (docs/rde_nozzle_literature_map.md:428-456): Hoffman 1967 È
la metà mancante di G14/P2 — per flusso chimicamente reagente il sistema di
ottimalità è campi di moltiplicatori di Lagrange lambda_1..lambda_4
(+lambda_5 per specie) che soddisfano PDE lungo le STESSE caratteristiche del
flusso, con residuo di ottimalità a-posteriori E (Eq. 78); tre banche mai
mutuamente citate (Hoffman 1967, Giles-Pierce 2001, Lozano-Ponsin 2025).
CONCESSO esplicitamente (query-bounded 2026-08-13, :451-456): l'equivalenza
generica "adjoint ≡ moltiplicatore" e la catena completa Route B → Route A
DENTRO la scuola classica (KT2015 Eqq. (2.2)→(2.9)→(2.10)→(2.12)); novità
residua = articolazione + operazionalizzazione. Hoffman 1967 p.676 prova che
la biiezione di corner muore per gas reagente (:457-463) — il brick per-fase
in forma chiusa è frozen-composition-only, e per questo il sistema mediato
(**') è formulato al livello Hadamard/adjoint, non solo al corner.

Precedente MEDIATO (M0:2908-2926, page-verified S13): Kraiko-Osipov PMM
34(6):1067-1075 (1970) derivano, per l'istanza TRAIETTORIA della stessa
struttura, la condizione a parete pesata integrata nel tempo (loro (3.2),
peso = adjoint di traiettoria W(t)) e il collasso alla famiglia classica
sotto similarità d'ingresso — "the 1970 ancestor of (b), of the weighted
structure of (c)". NON presente lì: la misura di ciclo, l'esattezza (T0), il
passo O(St) prezzato, il collasso puntuale affilato con confine provato, i
certificati, l'identificazione adjoint di P-2. Citazione obbligatoria; gate
umano G5 su Kraiko-1979/PMM blocca ogni SUBMISSION (CLAUDE.md R6).

---

## 2. Stato per-claim

| Claim | Classe | Ancora | Carrier / Falsificatore |
|---|---|---|---|
| Sistema di stazionarietà a 3 blocchi (struttura) [W2-R1] | THEOREM-SCHEMA, "verified formally" (M0:2812, 2818) | M0:2812-2941; P1:41-45 | C: enunciato-schema M0 Parte III T7; le componenti provate stanno nelle righe sotto |
| Differenziazione sotto l'integrale di ciclo: (b)+(c) enunciati L^1(dmu) genuini; (P)(ii) condizione necessaria rigorosa [W2-R1] | THEOREM* [T-T7FS], eredita [C-D25U] | claims_registry.yaml:576-587 (statement :580); M0:2935-2941; P1:128-150 | F [W2-R4]: famiglia di ciclo certificata con dJ ≠ Int F' dmu oltre barre (O3-class, eseguibile; registry :586 — la vecchia forma negative-existential è RITIRATA di record, non finitamente osservabile). C: prova docs/rde_nozzle_T7_P7_functionspace.md §1 |
| f2 = -lambda2(xi) (moltiplicatore = dati al lip); lambda2 unica, misurabile, L^inf | THEOREM* [T-P3], eredita [C-MAJDA] su fronti fittati | M0:2930-2934; P1:58-63, 132-135 | F: lambda2(xi) computato che deriva da -f2(lip) oltre margini (P1:143-144). C: rde_nozzle_P3_multipliers.md |
| Superficie ottima = C+ kernel-stopped (locus S19) | THEOREM* (dentro T-T7FS(a), scope irrot.-omoentropico S1) | P1:47-58; M0:2819-2826 | Drift misurato 9.4809e-03 vs 2.9e-01 sul locus sbagliato (P1:55-57) |
| Shared wall: nessuna fase soddisfa la propria condizione, la mu-media sì | THEOREM* (T-T7FS(b)) | P1:66-71; M0:2827-2829 | Nessun caso 2-D computato di record (OPEN §3.3); il degenerato quasi-1D è il carrier (xii) |
| (**') forma cono (C31): 3 casi K; portata fuori dal cono; D = R·w derivata | THEOREM* (T-T7FS(c)); fattorizzazione = struttura derivata | P1:72-94, 141; M0:2830-2861 | Istanze eseguite tutte nel regime fixed-(eps,L) (M0:2840-2845) |
| Cone transfer lemma; conversa FALSA (controesempio 2 fasi) | THEOREM [T-T7CN] | M0:2862-2874 | Rejector S3/A39: il tool deve accettare famiglia one-phase-out/mean-in |
| Content split: assiale vacuo/binario, radiale porta tutto l'averaging; lambda_L = Int(-lambda3/q)dmu | THEOREM (graft Route-A, Rao Eq. (13)) | M0:2875-2894 | [W2-R5] f3* nodewise in validation/o33_bench.py:320-321 (formula (L.13), docstring :32) — l'ancora ":292" stampata in M0:2891 è STANTIA (r.292 reale = helper `drift()`; finding candidato di retro-audit CONTRO M0, registrato in §3.8); limite onesto REFUTE_C: f3* >= 0 identicamente, contenuto falsificabile = identità + complementarità (M0:2891-2894) |
| Boxed warning: media naive sbagliata fuori da T3; -2.39% = artefatto naive | THEOREM* (corollario T-T7FS) + carrier PRACTICE | P1:96-114; M0:2856-2859 | Rejector gruppi (vi)/(xii) (P1:176-179) |
| Twin warning: naive può certificare punto dual-infeasible (regime-qualified) | THEOREM (esistenziale, controesempio 2 fasi) + falsificatore di rilevanza | M0:2895-2907; P1:108-113 | F a due segni (due quadrature): esecuzione sul parco esistente non trovata nella mia finestra — dichiarato in §3.6 |
| Riduzione quasi-1D <P_E>=Pa; eps*_real 3.49-3.52; forma chiusa = oracolo demoted | THEOREM [T-T7RED], EOS-general primaria | P1:152-189; registry :381 | C: run_all (vi)/(xii), data/phase_diagram_real.json. F: media non pesata che riproduce eps* pesato oltre barre |
| T1c: mass-mean condition rigettata, dIsp +3.33…+9.71 s | PRACTICE (rejector eseguibile, rango dichiarato: DOF più semplice) | test_bell_optimality.py:75-85; s25bis_closing_suite.log:61-76 | Il test PUÒ rigettare (rejector, R5) |
| G5/G6: shift primo ordine, penalità secondo ordine; gamma_eff pesata sì, <gamma> no | PRACTICE (rejector + controllo negativo) | test_gamma_probe.py:22-27, 99-142 | Record corrotto rigettato (G6 negative control) |
| Bridge P-2 (Hoffman 1967 / KT2015); novità = articolazione+operazionalizzazione, query-bounded | THEOREM* / pending [C-O33]; claim P2/G14 query-bounded | P1:191-207; literature_map:428-456 | F: term-match O3.3 su caso TOC (P1:205-206) |
| Kraiko-Osipov 1970 = antenato traiettoria di (b) e della struttura pesata di (c) | [REP] page-verified S13, citazione obbligatoria | M0:2908-2926 | Gate G5 (passaggio umano) su submission |

---

## 3. Gli APERTI

1. **[C-D25U] non scaricato** — stabilità semiglobale uniforme della mappa
   soluzione S1: l'unico conditional analitico della spina, ereditato da
   [T-T7FS]/[T-P7S1]/[T-P3] (registry :583, :596; M0:223: catena di stima
   U1+U2+U3+… componente -a completa, ma il conditional resta NOMINATO, non
   scaricato). Owner/trigger di record: campagna analitica; nessuna data.
2. **[C-MAJDA]** sui fronti fittati (affilata a U3-H1 di record, memoria
   S15/S16): eredità dichiarata di [T-P3]/[T-G12S1]; resta conditional.
3. **Nessun contorno cycle-wall computato**: il blocco (b) a DOF di parete
   2-D non ha alcun caso computato nel record letto — tutte le istanze
   eseguite vivono nel regime fixed-(eps,L) quasi-1D (M0:2840-2845;
   P1:152-156). Owner: F2 (prima campagna M-RED,
   docs/rde_nozzle_PROGRESS.md:37-40, 116-117).
4. **[C-O33]** — residuo numerico dell'identificazione di componente del
   bridge P-2 (P1:203; memoria S19/S20: quantificata, causa = classe di
   design; O3 ri-aggiudicata ADJUDICATE). Trigger: term-match su caso TOC.
5. **C54 / rung I4 (mean-state)**: la riga del choice ledger è OPEN
   (docs/choice_ledger.yaml:738-744;
   docs/rde_nozzle_pipeline_decision_map.md:65 [W2-R9]) — M0 D2.4
   tiene "I4 single mean state" NUDO (M0:124) senza l'annotazione O(Var)
   no-small-parameter (controesempio Jensen blind-data); trigger di record:
   prossimo tocco a M0 D2.4.
6. **Falsificatore-C32 (M0:2895, CLAIM-16 companion) non eseguito** [W2-R10:
   sigla sempre qualificata così — "C32" nudo collide con choice_ledger.yaml
   C32 = curvature policy SR1, oggetto diverso]: il confronto
   sign(Int R dmu) vs sign(Int R w dmu) sul parco marched è dichiarato
   "cheap, two quadratures" (M0:2899-2903) ma un'esecuzione non è stata
   trovata nella mia finestra di lettura — dichiarato come NON TROVATO NEL
   RECORD. [W2-R12] Il grep del refuter sul repo lo CONFERMA: esiste solo la
   conferma simbolica R=(+2,-1), w=(1,4) => segni opposti
   (literature_review/reports/VERIFICATION_FABLE_2026-08-13.md:355), che è
   il carrier dell'ESISTENZIALE (citabile come tale), non l'esecuzione sui
   campi marched.
7. **H-EXO diventa load-bearing a F5** (registry :1929): esogeneità della
   misura di ciclo — garantita su L4 da [T-NSW], da riprovare quando
   mu(Xi_sub) > 0 o al coupled RDE.
8. **[W2-R5] Finding candidato di retro-audit CONTRO M0**: M0:2891 stampa
   l'ancora stantia "validation/o33_bench.py:292" per f3* nodewise; la riga
   292 reale è dentro l'helper `drift()`, la formula f3* (L.13) vive a
   o33_bench.py:320-321 (docstring :32). Il contenuto regge, l'ancora no —
   da mintare come finding del registro nel retro-audit del deck (regola
   S-PRES: claim che fallisce il walk = finding, mai slide ammorbidita).

---

## 3-bis. ANTENATI DIRETTI (lineage claim, nodo N-C) [W-B.1/B7]

Join dichiarato (contratto [F-des-4], LINEAGE_LEDGER.md:8-16): ogni claim
di novità di questo nodo cita ≥1 riga LL (lint 7); la prosa integrale di
ogni riga vive nella parte sorgente (Pn.r). Stato righe: CANDIDATE fino
al pass del refuter C6 (LL-1 è nel gruppo dei seed/righe con verifica
page-verified di record). Formato: antenato → cosa fa → cosa gli manca.

- **LL-1 Kraiko-Osipov 1970** (`kraiko_osipov_1970`, registry :102;
  componenti 1/2/3/4/11 — la (1) in istanza DEGENERE, collasso alla
  famiglia classica sotto similarità d'ingresso, matrix part1:60-62;
  rilevanti al nodo N-C: 2/3/4/11) — **citazione OBBLIGATORIA** (M0:2908-2926,
  page-verified S13; gate umano G5 su submission, CLAUDE.md R6).
  Cosa fa: per l'istanza TRAIETTORIA della stessa struttura, condizione a
  parete PESATA integrata nel tempo (loro (3.2), peso = adjoint di
  traiettoria W(t)) + endpoint time-averaged + collasso alla famiglia
  classica sotto similarità d'ingresso [P1.1; matrix part1:59-75].
  Cosa gli manca: misura di ciclo, esattezza (T0), quoziente, collasso
  puntuale con confine provato, certificati, identificazione adjoint P-2
  (già §1.8).
- **LL-7 Hoffman 1967** (`hoffman_1967`, registry :372; componenti
  4/10/11/12). Cosa fa: campi di moltiplicatori lambda_1..lambda_5 su PDE
  lungo le STESSE caratteristiche del flusso (continuous adjoint avant la
  lettre — metà 1967 del ponte G14/P2), residuo di ottimalità a-posteriori
  E (Eq. 78), e la prova (p.676) che la biiezione di corner muore per gas
  reagente [P1.7; matrix part1:348-361]. Cosa gli manca: forma
  discreta/AD, l'identificazione continuo⇄discreto, il sistema mediato
  (**').
- **LL-16 Efremov-Kraiko 2004** (`efremov_kraiko_2004_augmentor`,
  registry :543; componente 2). Cosa fa: problema variazionale di spinta
  PERIOD-AVERAGED, Eq. (1.7), Kraiko-signed — è il falsificatore di
  record della frase "first averaged-thrust variational problem" (frase
  DEAD) [P2.1; matrix part2:117-127]. Cosa gli manca: il contorno di
  PARETE — il problema aggira lo shared-wall (formulato come bound
  steady/ideal-limit), quindi non tocca il blocco (b) né (**').
- **LL-17 Rubino 2018** (`rubino_2018`, registry :579; componenti 2/11).
  Cosa fa: discrete adjoint harmonic-balance DUALITY-PRESERVING per
  obiettivi period-averaged — il gemello di macchina più vicino della
  nostra coppia funzionale-mediato + adjoint [P2.2; matrix
  part2:164-175]. Cosa gli manca: riduzione per-phase, condizioni di
  parete Rao-type, contouring d'ugello (setting turbomacchine RANS).
- **LL-19 Giles-Pierce 2000 multipoint** (`giles_pierce_2000`, registry
  :516; componenti 2/8). Cosa fa: obiettivo multipoint J = Σ w_i F_i =
  antenato discreto-ensemble del funzionale pesato. **Residuo R11
  DICHIARATO**: pesi e forma della somma MAI stampati nel paper — la
  J-somma è inferenza nostra, e resta bounded finché R11 non chiude
  [P2.4; matrix part2:80-90; LINEAGE_LEDGER.md:139-140]. Cosa gli manca:
  misura di ciclo continua, condizioni di parete, per-phase.

Perimetro di novità conseguente (già query-bounded in §1.8): l'antenato
copre la STRUTTURA pesata (LL-1), i moltiplicatori su caratteristiche
(LL-7), il funzionale period-averaged (LL-16), la macchina adjoint
mediata (LL-17), l'ensemble pesato discreto (LL-19); ciò che NESSUNA
riga porta è la combinazione per-fase + misura di ciclo + shared wall +
(**') in forma cono + certificati — novità residua = articolazione +
operazionalizzazione (literature_map:451-456, CONCESSO di record).

---

## 4. Domande da panel

**(1) "La shared-wall condition mediata: che differenza di CONTORNO produce
rispetto al design sul campo medio, e c'è un caso computato?"**
Risposta onesta dal record: a DOF di parete 2-D la differenza di contorno NON
è mai stata computata — OPEN dichiarato, owner F2 (§3.3). [W2-R2] E sul
comparatore ESATTO chiesto dalla domanda va detto esplicitamente: il
confronto design-on-mean-state (I4) vs (**') non ha NESSUNA istanza computata
di record, a nessun DOF (non trovata nella finestra di lettura) — i numeri
citati qui sotto misurano gli ALTRI due modi sbagliati di mediare (media
naive e mass-weighted mean), non I4. Ciò che È computato
è il degenerato quasi-1D: al DOF area d'uscita la condizione mediata dà
eps*_real = 3.49–3.52 (P1:165-170) e le alternative sbagliate sono rigettate
con numeri: la classe naive-mean valeva un errore eps* del -2.39% (P1:106-107,
colpita in §4.3), e la condizione mass-weighted-mean sposta eps* da 3.80 a
5.48 (H2/20) fino a 22.69→42.51 (RP-1/200) con perdita Isp +3.33…+9.71 s
(s25bis_closing_suite.log:61-76). La FORMA della differenza a parete è nota
per teorema (media pesata delle densità di Hadamard vs densità del campo
medio), la sua MAGNITUDINE sul contorno è OPEN.

**(2) "La media naive non soddisfa nulla: e la media GIUSTA del campo (design
su s-bar)? È la stessa cosa o no?"**
Sono TRE oggetti distinti e il record li tiene separati. (i)
Naive-average-of-optima: media delle SOLUZIONI (o dei residui non pesati) —
per il boxed warning non soddisfa NESSUNA condizione del problema mediato
fuori dalla classe di collasso T3 (P1:96-107; M0:2856-2859). (ii)
Design-on-mean-state: UNA soluzione sul DATO mediato — è il rung I4 della
scala di idealizzazione (M0:122-124), legittimo come rung ma con errore
O(Var) SENZA parametro piccolo (controesempio Jensen blind-data,
choice_ledger.yaml:738-744; annotazione non ancora atterrata, riga OPEN —
lo dichiariamo). (iii) (**'): media pesata delle CONDIZIONI di ottimalità —
l'unico dei tre che è condizione necessaria del problema vero [T-T7FS]. Nella
classe T3 i tre coincidono (w fase-indipendente); fuori, no. [W2-R3] G6 va
citata al suo rango esatto: è un'istanza misurata della lezione
pesata-vs-aritmetica SUL LATO DATO (chiusura gamma dentro l'oracolo
gamma-const, "closure discrimination", test_gamma_probe.py:23-27) — entrambe
le chiusure confrontate sono riduzioni mean-data, quindi G6 NON istanzia il
confronto (ii)-vs-(iii): la chiusura pesata gamma_eff = <Pc gamma>/<Pc>
riproduce lo shift vero (<0.1 pt), la media semplice <gamma> sbaglia di
>1 pt (G6, test_gamma_probe.py:126-133) — anche "la media giusta del dato"
deve essere quella pesata dalla struttura, non la media aritmetica.

**(3) "Perché la weighted form e non quella semplice: il peso w(xi) da dove
viene e quando conta?"**
w non è modellato: emerge dalla derivazione — D = Int (dF/ds_E) dmu
fattorizza come R(xi)·w(xi) con R il residuo di corner classico mono-fase e
w > 0 peso geometrico-cinematico; "the (**') factorization itself is derived
structure" (P1:87-89, 141; M0:2855-2857). [W2-R7] Onestà sulla forma: la
FORMULA chiusa di w(xi) non è stampata nelle slice di record lette (P1 §5,
M0 T7); le proprietà di record sono che w è "an explicit algebraic factor in
the same bounded quantities", misurabile e L^inf(dmu)
(docs/rde_nozzle_T7_P7_functionspace.md:46-47, 78-79) — davanti al banco si
dichiara il puntatore, non si lascia il peso implicito. Conta quando R cambia segno lungo
il ciclo: la componente radiale cambia segno tra fasi sovra- e sotto-espanse
e porta TUTTO il contenuto di averaging (M0:2881-2884); w è fase-indipendente
ESATTAMENTE nella classe T3, dove naive e pesata coincidono (M0:2857-2859).
Il caso peggiore è il twin warning: con R a segno variabile, Int R dmu e
Int R w dmu possono avere segni OPPOSTI, e in regime unilaterale con cap
attivo la forma naive certificherebbe un punto dual-infeasible
(M0:2895-2907). Precedente storico dichiarato: il peso di Kraiko-Osipov 1970
è l'adjoint di traiettoria W(t) — la struttura pesata non è un'invenzione
nostra ma l'istanza-ciclo di una struttura del 1970 (M0:2908-2926).

**(4) "I vostri rejector T1c/G6 cosa dimostrano esattamente e cosa NO?"**
Dimostrano: che al DOF più semplice (scalare eps, quasi-1D) la scelta di
averaging è ESEGUIBILE E RIGETTABILE — la suite può rigettare la condizione
sbagliata, non solo confermare quella giusta (test_bell_optimality.py:13-15),
con controllo negativo (record corrotto rigettato, test_gamma_probe.py:
134-142) e con la separazione shift-primo-ordine / penalità-secondo-ordine
misurata (G5: 0 < penalty <= shift^2; shift -0.56%, penalty ~3e-6). NON
dimostrano: i teoremi del sistema mediato (che restano THEOREM* per prova in
M0, non per test), il confronto di formulazione a DOF di parete pieno (OPEN
§3.3), né la magnitudine del gap naive-vs-(**') sul contorno 2-D. Rango
dichiarato nel brief stesso del programma: istanze del meccanismo al DOF più
semplice, non la prova del confronto di formulazione.

**(5) [anticipata] "Tutto il sistema è condizionale a [C-D25U]: se cade?"**
Onesto: sì — [W2-R11] [C-D25U] è l'unico conditional ANALITICO della spina
di differenziazione, dichiarato una volta ed ereditato per ID (P1:131-138,
"the ONE named analytic conditional"); [C-MAJDA] sui fronti fittati (§3.2) e
[C-O33] numerico sul bridge P-2 (§3.4) restano nominati A PARTE, non
assorbiti nella spina. Se [C-D25U] cadesse, [T-T7FS]/[T-P3]
degradano da THEOREM* alla classe schema: la struttura resta derivata ma la
giustificazione L^1(dmu) del passaggio sotto integrale perde il suo
fondamento uniforme. Il falsificatore è nominato ed eseguibile in linea di
principio (registry :586). La catena di stima -a (U1+U2+U3+U4) è completa di
record (M0:223) ma il conditional NON è scaricato.

**(6) [anticipata] "Kraiko-Osipov 1970 ha già fatto questo: cosa c'è di
nuovo?"**
Dal record, senza difese: è l'antenato dichiarato e a citazione OBBLIGATORIA
(M0:2908-2926) — condizione a parete pesata integrata nel tempo, campi di
moltiplicatori, collasso alla famiglia classica. Non presente lì: la misura
di ciclo, l'esattezza (T0), il passo O(St) prezzato, il collasso puntuale
affilato con confine provato, i certificati, l'identificazione adjoint P-2.
Ogni claim di novità è query-bounded (P1:29-34) e la submission è bloccata
dal gate umano G5 su Kraiko finché un umano non ha fatto il passaggio
(CLAUDE.md R6).

---

## 5. Cosa deve dire il deck

1. **LA frase di design** (slide-carrier del capitolo): "nessuna fase
   soddisfa la propria condizione di parete — la mu-media sì; l'ugello
   ottimo di ciclo non è l'ugello ottimo di nessun punto operativo"
   [THEOREM* T-T7FS(b), P1:68-71]. È il fatto che rende il problema NON
   riducibile al design classico su un punto.
2. **Tre modi di mediare, uno solo giusto**: media degli ottimi (sbagliata
   per teorema), design sul dato medio (errore O(Var) senza parametro
   piccolo — rung I4, riga OPEN dichiarata), media pesata delle condizioni
   (**') (la condizione necessaria) [THEOREM* + boxed warning; choice
   ledger C54]. Slide a tre colonne, con la classe T3 come caso di
   coincidenza. [W2-R6] Nota di slide: T3 = classe di collasso [T-T3]
   (M0:746-754) — gamma frozen comune, parete fissa full-flowing
   supersonica, forma d'ingresso fase-indipendente: lì l'ottimo di ciclo
   È il contour classico alla pressione media <Pc>_mu.
3. **Il warning è un test, non una frase**: rejector T1c/G6 con i numeri
   misurati (eps* 3.80 vs 5.48 → 22.69 vs 42.51; dIsp +3.33…+9.71 s;
   <gamma> rigettata >1 pt, gamma_eff <0.1 pt) — AL RANGO DICHIARATO:
   istanze al DOF più semplice [PRACTICE, log s25bis:61-76].
4. **Una sola spina condizionale**: tutto il sistema THEOREM* eredita
   [C-D25U] (+[C-MAJDA] sui fronti), dichiarato una volta, ereditato per
   ID — non una nube di caveat [voce di onestà, P1:128-138].
5. **Genealogia dichiarata, novità query-bounded**: Kraiko-Osipov 1970 =
   antenato traiettoria (citazione obbligatoria), Hoffman 1967 = campi di
   moltiplicatori (bridge P-2); nostro = misura di ciclo + esattezza +
   certificati + identificazione adjoint [REP page-verified,
   M0:2908-2926; literature_map:428-456].
6. **Cosa manca, detto in slide**: il contorno cycle-wall 2-D non è mai
   stato computato (owner F2) e il conditional analitico non è scaricato —
   il programma lo sa e lo ha nominato [OPEN §3.1, §3.3].

---

## 6. STORIA — trittico condizionale [V2-R2] (writer B8a, W-B.2, 2026-08-23)

Ogni battuta: DATA + PROCESSO + VERDETTO (vincolo §5-bis). Ancore Fase A/B:
`validation/sfoundations_raws_2026-08-13/` (alberi ciechi 2026-08-17,
`phaseB_tree_diff.md` 2026-08-17).

**T-1. [T-T7FS] — il sistema a tre blocchi e la differenziazione sotto
l'integrale di ciclo.**
- *Battuta 1*: 2026-07-16, campagna rigore-S8 — commit `86fac06`
  "[F1/T7-FS + F1/P7]: T7 and P7 attacked in function space — the chain of
  (P) closes at THEOREM* grade" (prova
  `docs/rde_nozzle_T7_P7_functionspace.md`); testo di record P1 §5-7 con
  boxed warning: 2026-07-20, S10, commit `c0e3051`. PROCESSO: attacco in
  function space + stesura P1. VERDETTO: THEOREM* sulla differenziazione,
  struttura THEOREM-SCHEMA.
- *Battuta 2*: (a) RIDERIVATO-PIENO — Fase A/B 2026-08-17, item 2
  "Rao-collapse under averaging (T7 road): H-F35 proves-sketch"
  (`phaseB_tree_diff.md:325`); più panel D8 PAN-S14 2026-07-22 (16/16
  team-CONFIRMED, commit `7be8b98`). PROCESSO: derivazione de-novo cieca +
  panel a convergenza. VERDETTO: CONVERGENT sul road T7.
- *Battuta 3*: spina condizionale unica [C-D25U] dichiarata dal 2026-07-17
  (commit `c4d5a95`, conditionals ledger L4); ipotesi H-EXO aggiunta alla
  finestra litreview (2026-08-13, registry :1929). Classe finale come §2.

**T-2. [T-P3] — f2 = −λ2, il moltiplicatore dai dati al lip.**
- *Battuta 1*: 2026-07-16, rigore-S8 — commit `f54dbf2` "[F1/P3]: averaged
  multiplier gap ATTACKED — THEOREM* in shock-free S1" + `514d037`
  "Prop. A3, f2 = transported adjoint invariant" (prova
  `docs/rde_nozzle_P3_multipliers.md`). PROCESSO: attacco derivativo con
  doppia route (Prop. A2 dual-route `35e95f2`). VERDETTO: THEOREM*
  shock-free, eredita [C-MAJDA] sui fronti fittati.
- *Battuta 2*: (c) **NON-RIDERIVATO: questo aspetto non ha avuto
  riderivazione agnostica di record** (non è tra i 7 item theory-layer di
  `phaseB_tree_diff.md:315-347`). Doppia prova alternativa: panel D8
  PAN-S14 2026-07-22 (16/16) + carrier eseguibile O3.3 bench PASS al
  criterio primario, campagna S19 2026-08-06/07 (memoria
  `s19-o33-campaign`; [C-O33] aperta ma QUANTIFICATA — residuo dichiarato,
  P1:200-203). PROCESSO: panel + campagna di misura pre-registrata.
  VERDETTO: identificazione THEOREM*/pending [C-O33].
- *Battuta 3*: classe finale THEOREM* con residui R-P3.1/2 nominati
  (M0:2930-2934).

**T-3. Il locus S19 — superficie ottima = C+ kernel-stopped.**
- *Battuta 1*: 2026-08-06/07, sessione S19 (campagna O3.2/O3.3, M0:3291) —
  la misura sul C+ completo fino all'asse dà drift 2.9e-01 (identità
  falsificata), sulla superficie kernel-stopped 9.5e-03; re-issue in norma
  registrata 9.4809e-03 in S21 (2026-08-07, M0:3613). PROCESSO: rejector
  misurato che ha SPARATO → correzione di locus. VERDETTO: locus
  correction di record.
- *Battuta 2*: (c) NON-RIDERIVATO in Fase A; doppia prova alternativa = il
  falsificatore misurato stesso (due misure discriminanti a due decadi di
  distanza) + qualificatore di scope aggiunto dall'audit C1 in S21
  (2026-08-07, M0:368, :2821: identificazione limitata al sottoclasse
  irrotazionale-omoentropico). PROCESSO: audit di scope post-correzione.
  VERDETTO: THEOREM* scoped.
- *Battuta 3*: classe finale THEOREM* dentro T-T7FS(a), scope dichiarato.

**T-4. La forma a CONO di (**') + [T-T7CN] + content split.**
- *Battuta 1*: forma free-endpoint (Rao Eq. (14)) al testo P1 2026-07-20
  (`c0e3051`); RIFORMA a cono = ratifica utente C31, 2026-08-13, sessione
  F-SERVICE (R36) — con mint del lemma [T-T7CN] e controesempio a due fasi
  (memoria `fservice-scert-double-session`; M0:2830-2874). PROCESSO:
  ratifica utente su proposta istruita + prova elementare con
  controesempio. VERDETTO: THEOREM (T-T7CN), conversa FALSA.
- *Battuta 2*: (c) NON-RIDERIVATO in Fase A: la forma a cono (2026-08-13)
  precede gli alberi (2026-08-17), ma la riga endpoint non compare tra gli
  item theory-layer §3 del diff (`phaseB_tree_diff.md:315-347`) — nessuna
  ancora di Fase A viene fabbricata (F-des-3). Doppia prova alternativa:
  prova di record del lemma con
  controesempio esplicito + rejector S3/A39 armato (il tool DEVE accettare
  one-phase-out/mean-in, M0:2871-2874) + cross-check KT2015 (2.10)/(2.13)
  page-verified. PROCESSO: prova + rejector + confronto alla fonte.
  VERDETTO: THEOREM con falsificatore vivo.
- *Battuta 3*: content split (assiale binario / radiale porta l'averaging)
  registrato nello stesso blocco M0:2875-2894; classe finale come §2.

**T-5. Il BOXED WARNING (media naive sbagliata fuori T3) e il twin.**
- *Battuta 1*: boxed warning nel testo di record P1 §5-7, 2026-07-20
  (`c0e3051`, "averaged system T7/(**') with boxed naive-average
  warning"); twin warning (dual-infeasibility, regime-qualified) alla
  finestra della ratifica C31, 2026-08-13 (M0:2895-2907). PROCESSO:
  derivazione + controesempio esistenziale a due fasi. VERDETTO:
  corollario THEOREM* + THEOREM esistenziale.
- *Battuta 2*: boxed warning: (a) parziale via T7-road H-F35
  (`phaseB_tree_diff.md:325`, 2026-08-17) + rejector eseguibili gruppi
  (vi)/(xii) e T1c/G5/G6 (numeri re-misurati suite S25-bis,
  `validation/s25bis_closing_suite.log:61-76`, 2026-08-13). Twin warning:
  (c) NON-RIDERIVATO e il falsificatore di rilevanza a due segni NON è mai
  stato eseguito sul parco esistente (dichiarato in §3.6) — la prova
  esistenziale c'è, la seconda prova di RILEVANZA è **ASSENTE** =
  **FINDING dichiarato** (inventario `HISTORIAN_INV_a.md`). PROCESSO:
  diff Fase B + rejector; censimento onesto. VERDETTO: come stampato.
- *Battuta 3*: classi finali §2; la classe eps* stantia a −2.39% resta
  l'istanza storica dell'artefatto naive (P1:106-107).

**T-6. [T-T7RED] e la demozione delle forme chiuse a oracoli.**
- *Battuta 1*: 2026-07-16 — commit `ef0af1d` "[F1/OP-0-gamma]: gamma
  purged from the executable ceiling — real-thermo primary route, closed
  forms demoted to oracles" (direttiva rafforzata `cbee622` S5); carrier
  run_all gruppo (xii), eps*_real 3.49-3.52. PROCESSO: inversione di
  architettura per direttiva gamma-variabile + carrier. VERDETTO: THEOREM
  EOS-general con forma chiusa demota a oracolo (pin VI.4bis(iii)).
- *Battuta 2*: (a) RIDERIVATO-PIENO — T7-road H-F35
  (`phaseB_tree_diff.md:325`) + thermo road item 6 "V-F9/H-F6 = certified
  gamma(T) tables with AD" (`:345`), 2026-08-17. PROCESSO: alberi ciechi
  convergenti su route reale + tabelle certificate. VERDETTO: CONVERGENT.
- *Battuta 3*: rejector T1c/G5/G6 al rango dichiarato, numeri di record
  re-misurati 2026-08-13 (suite S25-bis); classe finale THEOREM.

**T-7. La genealogia (Kraiko-Osipov 1970, Hoffman 1967, concessione
KT2015).**
- *Battuta 1*: 2026-07-16 — sweep PMM 1957-1990 di record, "top flag
  Kraiko-Osipov 1970" (commit `344ddfb`); Hoffman 1967 full page-level
  read (`079f882`); adjudicazione contenimento K-O: 2026-07-22, S13,
  commit `581ccb1` + precedente page-verified (M0:2908-2926). PROCESSO:
  sweep sistematico + lettura alla pagina + adjudicazione. VERDETTO: [REP]
  page-verified, citazione obbligatoria.
- *Battuta 2*: (c) NON-RIDERIVATO (non derivabile: è storia esterna);
  doppia prova alternativa = confronto litreview avversario alla riga,
  2026-08-13 (25 paper, `ADVISORY_litreview_confrontation_2026-08-13.md`;
  concessione query-bounded adjoint≡moltiplicatore litmap:451-456; morte
  di "first averaged-thrust variational problem" per Efremov-Kraiko 2004,
  M0:2320-2330). PROCESSO: contraddittorio simmetrico paper/claim
  (protocollo di record). VERDETTO: claim di novità ristretti alle forme
  bloccate D-06.
- *Battuta 3*: gate umano G5 (Kraiko-1979/PMM) resta il blocco di ogni
  SUBMISSION (CLAUDE.md R6); classe finale [REP] + query-bounded.

## 7. POSIZIONAMENTO / CONFORMITY (cella C-ii) [W-B.1/B7]

### 7(a) STRUMENTI — adjoint continuo per-fase vs discrete-adjoint AD

Terna mondo-SOTA / cosa usiamo / perché (id verificati con grep in
finestra su docs/literature_registry.yaml).

**Il mondo**: la prassi prevalente del design adjoint è il
DISCRETE-adjoint AD; la tassonomia continuo/discreto di riferimento è
`giles_pierce_2000` (registry :516; matrix part2:80-90 — l'equivalenza
generica "adjoint = moltiplicatore" p.397 è CONCEDED di record); il
criterio di qualità del discreto è la dual consistency di
`wanted_hicken_zingg_2014` (registry :920-926, PDF arrivato, id tenuto
per upgrade in place; Def. 1 JCP 256 p.164 + caveat pubblicato: la
consistenza primale NON implica quella duale — C56 note); gli hazard
pubblicati del discreto su Euler inviscido sono `lozano_2018` (registry
:162: tassonomia delle singolarità adjoint, log-singularity alla gola
sonica) e `lozano_2019` (registry :170: mesh-divergence — locus
CORRETTO di record: wall/trailing-edge-driven, non lo shock); il ramo
ANALITICO continuo è `giles_pierce_1997` (registry :989, adjoint
equations AIAA 97-1850) e `giles_pierce_2001` (registry :507: adjoint
quasi-1D analitico in 4 regimi — adottato come ORACOLO indipendente
[X-GP01], matrix part2:70-78, non come antenato del nostro discreto).

**Cosa usiamo** (doppio registro per-RUOLO, riga C56 del ledger,
choice_ledger.yaml:760-769): al livello di FORMULAZIONE
l'identificazione CONTINUA per-fase — il first integral
f2 = −lambda2(xi) (§1.2, [T-P3] THEOREM*): il moltiplicatore di portata
della fase si LEGGE dai soli dati al lip, senza risolvere alcun sistema
adjoint; al livello di ESECUZIONE il discrete AD-adjoint
(custom_vjp, one-lowering) come realization di record del gradiente.

**Perché continuo-prima**: (i) la macchina classica dà lambda2 in forma
chiusa misurabile — struttura derivata, non solve numerico (§1.2); (ii)
il sistema mediato (**') è formulato al livello Hadamard/adjoint
continuo perché la biiezione di corner muore per gas reagente (Hoffman
1967 p.676, §1.8): il continuo è il livello a cui i teoremi vivono.
**Dove il discreto rientra**: O3.1 — il verdetto G0 di record
(D6 :753-774, verificato alla riga): JAX primary con gradient fidelity
a machine precision (spikes 52/52 + O3.1, carrier X-G0/X-G0AX,
D6 :762-763); il discreto è il carrier ESEGUIBILE del gradiente e O3.1
il suo rejector; il residuo numerico dell'identificazione
continuo⇄discreto resta [C-O33] (§3.4), e la dual-consistency è il
criterio-referee (C56 note: F11d = esecuzione all'estimator-site, con
il criterio pubblicato Hicken-Zingg citato per pagina). La scelta di
STACK (C58/G0, JAX vs alternative) è della riga I: card owner B4/CH4 —
qui solo l'ancora G0.

**DECISION CARD C56** (formato emendamento v2.1 §1g, 6 campi):

| campo | contenuto |
|---|---|
| 1. scelta | C56 — adjoint REALIZATION per-ruolo (gradient / DWR weight / indicator): discrete AD-adjoint vs continuo separately-discretized vs sintesi dual-consistent (choice_ledger.yaml:760-769, status MIXED, tre ruoli CLOSED) |
| 2. alternative censite (data+fonte) | (i) discrete AD-adjoint (incumbent); (ii) continuo separately-discretized (linea Ancourt/Lozano-Ponsin); (iii) sintesi dual-consistent (criteri Hicken-Zingg). Censimento: mint 2026-08-19, VERDICT_C9C11_supplement.md §4.3; aggiudicazione wave-2 2026-08-19 (PANEL_C31TRIO §3.1-bis + PANEL_C1REP §3.4-bis, VERDICT_wave2 §2.10); ancoraggio criteri pubblicati 2026-08-20 (retro-sweep: HZ Def. 1 JCP 256 p.164; Fidkowski-Darmofal 2011 p.676) |
| 3. verdetto + perché | gradient role = discrete AD-adjoint (esatto per la discretizzazione, O3.1-verificabile a machine precision); linea continua = frame + referee (l'identificazione f2 = −lambda2 [T-P3]); indicator role chiuso per transitività (f2 = −lambda2, stesso oggetto); weight role chiuso dal supplement C11 con F11d pinnato |
| 4. RECENCY/SOTA check | survey datata 2026-08-19/20 (perimetro: registry + census C9/C11 + panel wave-2). **ATTUALE(perimetro: registry 174 + VERDICT_C9C11_supplement + wave-2; data-check 2026-08-23)** — con finestra di ri-sweep nominata: cluster F2-entry (C31/C58 delta-sweep vs landscape 2026) |
| 5. falsificatore | F11d che SPARA (bookkeeping d'ordine dual-consistency contro HZ Def. 1 — il caveat pubblicato vieta di derogarlo su evidenza primale) riapre la riga; guardia di premessa: blind spot wrong-branch fino a C20 Tier-0 (C56 note) |
| 6. trigger ri-esame (finestra) | F2-C11-ESTIMATOR-CAMPAIGN (esecuzione F11d, owner di riga); un F11d sparato riapre C56, non C11; finestra = F2 |

### 7(b) SENSO — precedenti e gap (query-bounded)

Tre banche mai mutuamente citate (Hoffman 1967, Giles-Pierce 2001,
Lozano-Ponsin 2025 — literature_map:428-456, già §1.8); ensemble
discreto pesato = LL-19 (R11 dichiarato, §3-bis); macchina adjoint
period-averaged completa = LL-17 (HB, senza per-fase né parete);
funzionale period-averaged senza parete = LL-16. Il gap che il nodo
occupa: NESSUNA banca fa l'identificazione adjoint per-fase su misura
di ciclo con transversality PESATA in forma cono — l'equivalenza
generica adjoint≡moltiplicatore e la catena Route B→A interna alla
scuola classica sono CONCESSE (query-bounded 2026-08-13,
literature_map:451-456); novità residua = articolazione +
operazionalizzazione (§1.8, §3-bis).

### 7(c) STANDARD DI RIFERIMENTO (asse §C)

Asse governante: **§C-3 (tracciabilità, classe ECSS/DO-178C)** —
criterio di conformità: ogni claim di gradiente ha catena id→carrier→
rejector (O3.1 52/52 a tolleranza derivata, X-G0/X-G0AX; F11d con
criterio pubblicato citato per pagina); divergenza dichiarata: nessun
audit esterno né certificazione DI — adottiamo la CLASSE di disciplina
(trace bidirezionale + lint automatici). Secondo asse citato: §C-2
(gradazione evidenza, classe GRADE) per le classi THEOREM*/pending
[C-O33] con cui questo capitolo stampa ogni identificazione.

---

## Disposizione riparazioni (onda 2)

Riparatore S-PRES, 2026-08-23. Ogni fix applicato con read-then-quote:
ancora del refuter aperta e verificata in finestra PRIMA dell'edit
(M0:2812/2818/2935-2941; registry:576-587; o33_bench.py:32, 286-295,
316-322; test_gamma_probe.py:18-31; P1:80-150; M0:746-754 [T-T3];
rde_nozzle_T7_P7_functionspace.md:40-84; VERIFICATION_FABLE_2026-08-13.md:
350-358).

| Finding # | Classe | Disposizione |
|---|---|---|
| 1 | REPAIR | APPLICATO [W2-R1] — split di classe in §1.1 e tabella §2 (riga 1 divisa in due: struttura = THEOREM-SCHEMA verified-formally, M0:2812/2818; L^1-genuinità + necessità = THEOREM*, registry :580) |
| 2 | REPAIR | APPLICATO [W2-R2] — Q1: frase esplicita "I4 vs (**') mai computato a nessun DOF; i numeri misurano gli altri due comparatori" |
| 3 | REPAIR | APPLICATO [W2-R3] — Q2: G6 ri-etichettata come lezione pesata-vs-aritmetica SUL LATO DATO (closure discrimination, test_gamma_probe.py:23-27), etichetta (ii)-vs-(iii) rimossa |
| 4 | DOWNGRADE | APPLICATO [W2-R4] — falsificatore tabella riga [T-T7FS]: tenuta solo la forma di record dJ /= Int F' dmu (O3-class); forma negative-existential dichiarata RITIRATA (registry :586) |
| 5 | REPAIR | APPLICATO [W2-R5] — ancora f3* corretta a o33_bench.py:320-321 (+docstring :32); stale-anchor su M0:2891 registrato come finding candidato di retro-audit (nuovo OPEN §3.8) |
| 6 | GAP | APPLICATO [W2-R6] — definizione one-line di T3 con ancora [T-T3] M0:746-754 in §1.5 e nella nota della slide 2 |
| 7 | GAP | APPLICATO [W2-R7] — Q3: dichiarato che la formula chiusa di w non è stampata nelle slice lette; proprietà di record con ancora T7_P7_functionspace.md:46-47, 78-79 |
| 8 | GAP | APPLICATO [W2-R8] — box notazione in §1.1 (glosse one-line: G_xi, g_L, (P)(ii), N_K/T_K) |
| 9 | NOTE | APPLICATO [W2-R9] — path completo docs/rde_nozzle_pipeline_decision_map.md:65 in §3.5 (miglioria senza rischio) |
| 10 | NOTE | APPLICATO [W2-R10] — §3.6: sigla disambiguata "falsificatore-C32 (M0:2895, CLAIM-16 companion)", collisione con choice_ledger C32 dichiarata (miglioria senza rischio) |
| 11 | REPAIR | APPLICATO [W2-R11] — Q5 allineata al deck point 4: [C-D25U] = unico conditional analitico DELLA SPINA di differenziazione; [C-MAJDA]/[C-O33] nominati a parte |
| 12 | NOTE | APPLICATO [W2-R12] — ancora VERIFICATION_FABLE_2026-08-13.md:355 aggiunta all'OPEN §3.6 come carrier dell'esistenziale (rafforza, verdetto OPEN invariato) |

---

## DECK FEED (asserzioni candidate-slide, assertion-evidence) [W-B.1/B7]

1. "Nessuna fase soddisfa la propria condizione di parete — la mu-media
   sì: l'ugello ottimo di ciclo non è l'ugello ottimo di nessun punto
   operativo." — ancora P1:68-71; M0:2827-2829 — classe THEOREM*
   (T-T7FS(b)).
2. "Tre modi di mediare, uno solo è condizione necessaria del problema
   vero: la media PESATA delle condizioni (**'); naive e design-su-dato-
   medio falliscono fuori dalla classe di collasso T3." — ancora
   P1:96-114; M0:2856-2861; [T-T3] M0:746-754 — classe THEOREM* +
   boxed warning.
3. "La media sbagliata costa Isp misurato: dIsp +3.33…+9.71 s su 6 casi
   (rango dichiarato: rejector all'oracolo senza contouring, solo
   eps)." — ancora s25bis_closing_suite.log:61-76 — classe PRACTICE
   (rejector eseguibile).
4. "Il moltiplicatore di fase si legge al lip: f2 = −lambda2, in forma
   chiusa, senza risolvere alcun sistema adjoint." — ancora P1:58-63;
   M0:2826 (first integral) + M0:2930-2934 ([T-P3] classe) — classe
   THEOREM* (T-P3, eredita C-MAJDA sui fronti).
5. "Continuo-prima in formulazione, discreto AD come realization
   per-ruolo, con oracolo O3.1 a machine precision e dual-consistency
   come referee (F11d)." — ancora choice_ledger.yaml:760-769 (C56);
   D6:753-774 (G0) — classe: decisione di record (ruoli CLOSED) +
   PRACTICE (O3.1).
6. "La struttura pesata ha un antenato dichiarato e a citazione
   obbligatoria: Kraiko-Osipov 1970, parete pesata W(t); la novità
   residua è query-bounded (articolazione + operazionalizzazione)." —
   ancora M0:2908-2926; LL-1; literature_map:451-456 — classe [REP]
   page-verified + query-bounded.
7. "Una sola spina condizionale: [C-D25U], dichiarata una volta ed
   ereditata per ID — non una nube di caveat." — ancora P1:128-150 —
   classe: voce di onestà (THEOREM* con conditional nominato).
8. "Il contorno cycle-wall 2-D non è mai stato computato: OPEN
   dichiarato, owner F2." — ancora §3.3; M0:2840-2845 — classe OPEN
   di record.
