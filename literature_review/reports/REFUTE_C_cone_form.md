# REFUTE_C — attacco alla correzione C31/C32 + S1-S3 (forma a cono di T7(c))

Refuter matematico-numerico, panel avversariale, 2026-08-13.
Default d'ingresso: la correzione è sbagliata o sovradimensionata finché non regge.
Tesi attaccata: `validation/ADVISORY_litreview_confrontation_2026-08-13.md` §3.15 (r.452-556),
§6 C31-C32 (r.1118-1119), §5 A37-A39 (r.1058-1060).

Fonti lette per intero ai loci citati: `docs/rde_nozzle_MASTER.md` r.1071-1130 (T-T7FS) e
r.1699-1704 (FIXED-EPS bookkeeping); KT2015 pp.185-188 (Eq. 2.6-2.14, page-verified su PDF);
`validation/o33_bench.py` (R1/R2 r.285-294, surface_report r.479-528, R7 r.666-695, R3 r.734-838);
`validation/margin_governor.py` r.61-73; `validation/a1_toc_variational_jax.py` r.1748, r.2344-2365;
`src/thrust/phase_diagram_real.py` r.208-229, r.273.

---

## Linea (1) — Quali vincoli sono davvero unilaterali? Il "tre regimi" è sovradimensionato?

**Fatti stabiliti.**
- La portata per fase è un'UGUAGLIANZA e NON entra nel cono all'endpoint: in T-T7FS
  (M0 r.1073-1076) è portata dal moltiplicatore funzionale `lambda2(xi)`; in KT2015 la stessa
  struttura è pubblicata: **(2.13) p.187 è un'UGUAGLIANZA** (`A^y = 0`) ottenuta esattamente
  perché la portata fissa rende `Δy_d` dipendente da `δx, Δx_d` — il vincolo di uguaglianza
  produce una condizione di uguaglianza anche a frontiera "libera". Solo i cap geometrici
  generano cono: (2.10) p.186 (`(p − p⁺ − ρuv tan μ)_f ≥ 0`, `v_f² ≥ 0`) e (2.14) p.187
  (`λ'_1 ≥ 0` su `ad_`, `A^x ≤ 0`).
- **Attività del cap di lunghezza**: KT2015 p.186 dopo (2.10): il ramo di uguaglianza `v_f = 0`
  è scartato («leads to nozzles with uniform axial exit flow, which is not of interest in motor
  applications»), e «for real values of X an inequality holds which shows that the end face ff°,
  if exists, is a region of boundary extremum». Quindi SÌ: a X finito, con `v_f ≠ 0`, il cap di
  lunghezza è sempre attivo nel problema per fase; a livello di ciclo
  `λ_L > 0 ⟺ μ({v_E ≠ 0}) > 0` (generico).
- **MA il regime a estremo libero NON è vuoto in radiale.** In produzione
  `src/thrust/phase_diagram_real.py:208-229` risolve `⟨P_E(ε)⟩_μ = Pa` per bisezione e trova
  radici INTERNE (regime di uguaglianza `D_y = 0` in ε) ogni volta che `eps_star < eps_max`;
  il cap superiore morde solo via `eps_bell = min(eps_star, eps_max)` (r.273) e quello inferiore
  via il clamp `if mean_pe(1.0) <= Pa: return 1.0` (r.215-216). Entrambi i rami occorrono nelle
  sweep. **La riduzione a "UNA disuguaglianza scalare" è REFUTATA**: la componente radiale ha
  tre rami (interno / cap alto / cap basso, con versi opposti ai due cap), la componente assiale
  ha il solo fatto binario di attività.

**Dove la tesi è sovradimensionata — tre punti, con evidenza.**
1. **La "tabella a tre regimi" non sono tre teoremi: è UN enunciato.** `D ∈ N_K(s_E*)` con K
   dichiarato per istanza li sussume tutti: K con interno contenente `s_E*` ⇒ `N_K = {0}` ⇒
   `D = 0` (regime 1); K = {punto} ⇒ `N_K = R²` ⇒ condizione all'endpoint VACUA e i "λ di segno
   libero" sono semplicemente le componenti di D (regime 2); K cono proprio ⇒ segno +
   complementarità (regime 3). La forma minimale corretta è: **un solo VI-statement + la
   dichiarazione di K per ogni enunciato/strumento**. La tabella può restare come apparato di
   navigazione, non come contenuto matematico.
2. **"Incompatibili finché il regime non è dichiarato" è SOVRASTIMATO.** M0 r.1699-1704 dichiara
   già, testualmente, la sostituzione di regime 2: «Rao's Eq. (14) free-endpoint corner condition
   is **REPLACED, at fixed (eps, L),** by the lip-constraint multiplier lambda_e = dJ/dy_lip …
   the classical reading pa/p_E is NOT required to vanish (it equals the constraint's shadow
   price)». Questa È una dichiarazione di regime (embrionale, non nominata). Il difetto vero e
   residuo è che manca il **regime 3** (la forma per (P) come posta, M0 r.246-247:
   `A_gen(c) = {…; g_i(S) <= c_i}`) e manca il livello ciclo. C31 va quindi riformulata: non
   "sanare un'incompatibilità", ma "estendere una dichiarazione già esistente al caso unilatero
   e al ciclo".
3. **"Il driver gira in active-set" all'ENDPOINT è FALSO come scritto.** Il driver committato
   pinna il lip per UGUAGLIANZA: `a1_toc_variational_jax.py:1748`
   `lip_eq = LinearConstraint(A * Dv[None, :], [yL], [yL])` (lower = upper = yL), e la direzione
   di perturbazione di `o33_bench.py:531-533` è dichiarata «lip pinned by the eps equality».
   L'unica NonlinearConstraint unilatera del driver è il MARGINE (r.1914,
   `NonlinearConstraint(m_np, 0.0, np.inf)`), che è un vincolo di CAMPO, non un vincolo
   dell'endpoint: non entra in K a `s_E`. All'endpoint il driver vive nel **regime 2**. I siti
   genuinamente regime-3 sono (P) come posta e la riduzione quasi-1D di produzione — non il
   driver. La riga di §3.15/C31 va corretta in questo punto.

**Verdetto linea 1**: sostanza NECESSARIA (manca la forma unilatera per (P) e per il ciclo),
presentazione SOVRADIMENSIONATA (un enunciato, non tre; incompatibilità sovrastimata; driver
mal classificato). Riduzione minimale del proponente-avversario ("una disuguaglianza scalare")
REFUTATA a sua volta: la radiale ha entrambi i lati più il ramo interno.

## Linea (2) — Lemma di trasferimento: DIMOSTRATO (in forma più elementare del claim); viceversa FALSO con controesempio

**Direzione fase→ciclo (THEOREM, confermato — e la giustificazione dell'advisory è ridondante).**
Sia `K` convesso (chiuso o no), `s* ∈ K`, `N_K(s*) := {d : ⟨d, s − s*⟩ ≤ 0 ∀ s ∈ K}`. Se
`D(ξ) ∈ N_K(s*)` per μ-q.o. ξ e `D ∈ L¹(dμ)` (garantito dalla dominazione [C-D25U], M0
r.1125-1129), allora per ogni `s ∈ K` fissato: `⟨∫D dμ, s − s*⟩ = ∫⟨D(ξ), s − s*⟩ dμ ≤ 0`
per linearità e monotonia dell'integrale con μ ≥ 0. Dunque `∫D dμ ∈ N_K(s*)`. **Nota tecnica
contro l'advisory**: la catena «N_K è cono convesso CHIUSO ⇒» è vera ma non è il meccanismo —
`N_K(s*)` è per definizione un'intersezione di semispazi passanti per l'origine indicizzata da
K, e l'integrale preserva ogni semispazio separatamente; né la chiusura né la convessità vanno
invocate. (La chiusura serve solo alla rappresentazione `D = Σ λ_i ∇g_i` nel caso poliedrale,
dove è automatica per coni finitamente generati.) La correzione è cosmetica, la classe THEOREM
regge.

**Viceversa: FALSO, controesempio a due fasi esplicito.** `n = 1`, `K = {y ≤ 0}`, `s* = 0`
(cap attivo), `N_K(0) = [0, ∞)`. `μ = ½δ_{ξ₁} + ½δ_{ξ₂}`, `D(ξ₁) = −1 ∉ N_K(0)`,
`D(ξ₂) = +3 ∈ N_K(0)`. Media `= +1 ∈ N_K(0)`. Una fase fuori-cono (sotto-espansa oltre il verso
ammesso), media in-cono. Il controesempio ESISTE ⇒ la scansione per fase è sufficiente ma non
necessaria, e il rejector A39 («la famiglia una-fase-fuori/media-dentro deve essere ACCETTATA»)
è ben posto e indispensabile. Confermato.

**Verdetto linea 2**: il lemma REGGE (con dimostrazione più elementare di quella dichiarata);
il viceversa è FALSO come asserito. Nessuna refutazione sostanziale.

## Linea (3) — Confronto di segni (C32): l'esempio esiste; "più economico" è vero ma il claim va qualificato per regime

**Esempio esplicito di segni opposti.** Due fasi a masse uguali, `w > 0` fase-dipendente:
`R = (+2, −1)`, `w = (1, 4)`. Allora `∫R dμ = ½(2 − 1) = +0.5 > 0` mentre
`∫Rw dμ = ½(2 − 4) = −1 < 0`. Esiste, è a due fasi, e il pattern è fisicamente il caso tipico
(fase sovra-espansa `R < 0` a peso alto). Il fenomeno matematico di C32 è CONFERMATO.

**"Più economico" — rispetto a cosa: verificato.** La colonna C32 (advisory r.1119) lo dichiara:
rispetto al falsificatore di record precedente formulato su RADICI («media ingenua e (**')
selezionano lo stesso contorno»), che richiede **due ri-ottimizzazioni**; il confronto di segni
richiede **due quadrature su campi per-fase già marciati**. Il claim di economia è corretto e
ancorato.

**MA due qualificazioni mancanti (refutazione parziale della formulazione):**
- **Qualificatore di regime.** «La forma ingenua può certificare KKT-ammissibile un punto
  duale-INFATTIBILE» ha contenuto SOLO nel regime a cono proprio con cap attivo: nel regime 2
  (tutte le istanze eseguite, lip in uguaglianza) il segno di λ è libero e un flip di segno fra
  `∫R dμ` e `∫Rw dμ` non certifica alcuna infattibilità — misura solo la divergenza
  ingenuo-vs-pesato. Il falsificatore va enunciato CON il regime, o spara su niente.
- **Asimmetria logica.** Il claim ri-enunciato contiene un'esistenziale («possono avere segni
  opposti»), che una singola famiglia concordante non può falsificare in senso stretto; come
  test severo pre-registrato (R5) è legittimo, ma la dicitura di record deve dire che la
  concordanza famiglia-intera falsifica la RILEVANZA del modo di fallimento sulla classe
  eseguita, non l'esistenziale matematico (che è un teorema, vedi esempio sopra).

**Verdetto linea 3**: C32 CONFERMATA nella sostanza e nell'economia; formulazione da emendare
con il qualificatore di regime e la portata del falsificatore.

## Linea (4) — SUL CODICE: la cecità al segno è VERA, con una precisazione lessicale, e i carrier ciechi sono CINQUE, non tre

- **R3** (`o33_bench.py:754` `rel = abs(g[-1] - cd) / max(abs(cd), 1.0)`; r.769-780 banda e
  `strict = abs(g[-1] - cd) <= band`; r.830-838 i due knob). Il valore assoluto è applicato alla
  **DIFFERENZA**, quindi R3 è un'identità sul valore CON segno (se `|a − b|` è piccolo e i valori
  sono lontani da zero, i segni coincidono) — la dicitura dell'advisory «identità di modulo» è
  **imprecisa**. La sostanza però regge integralmente: R3 verifica `dJ/dy_lip = cd` e **non
  contiene alcuna clausola di fattibilità duale** — un λ_e di segno sbagliato per il lato attivo,
  condiviso da AD e classico, passa. Cieco alla feasibility duale: SÌ. Cieco "al segno" nel senso
  letterale: NO. Correggere il lessico in A37.
- **R7** (`o33_bench.py:689-695`): `dpa = abs(rep_star["pa_ratio"] - rep_geno["pa_ratio"])`,
  check `dpa < max(drift)`. Pura concordanza cross-design. **Ciò che passa indisturbato**: il
  VALORE COMUNE di `pa/p_E` (definito in `surface_report`, r.516-528), incluso un valore di segno
  o di lato sbagliato per il vincolo attivo — mai confrontato con il verso richiesto, mai con la
  complementarità. Confermato alla lettera, incluse le r.512-515 che DICHIARANO l'intenzione
  («it equals the constraint's multiplier … it must be the SAME number for two designs»): la
  cecità è by-design, non un bug — ma resta cecità.
- **f3*** (`o33_bench.py:292-293`): consumata SOLO come drift (r.502-507, r.526 `d3`; riga R2).
  Mai integrata su μ, mai confrontata con λ_L. Confermato. **Aggravante contro S2 come
  "rejector di segno"**: `f3* = 2π y ρ q² sin²θ tanα ≥ 0` PUNTUALMENTE E IDENTICAMENTE per campi
  fisici (ogni fattore ≥ 0 con α ∈ (0, π/2)) — un check di segno su f3* **non può sparare** su
  alcun dato fisico, violazione R5 se armato come tale. Il contenuto falsificabile di S2/A38 è
  l'IDENTITÀ `λ_L = ∫ f3*/q dμ` + la complementarità, e il seed rejector va costruito su quelle
  (corruzione dell'identità), non sul segno. L'advisory lo dice quasi (assiale = contenuto
  binario), ma A38 non lo scolpisce nel seed.
- **Carrier aggiuntivi trovati (Grep `lambda_e` su validation/*.py) — la lista dell'advisory è
  incompleta per difetto, il che RAFFORZA A37:**
  - `a1_toc_variational_jax.py:2356-2365`: stampa `lambda_eps` RAW «(with sign)» ma non gate
    nulla sul segno, e l'unica quantità derivata usa **`abs(lam)`** (`Pa_impl = abs(lam)/(2π yL)`,
    r.2357) — sign-stripping esplicito e dichiarato «instance reading».
  - `margin_governor.py:64-73`: metrica [D1]-constrained
    `rel_c = |gJ_lip + mu gm_lip − cd| / |cd|` — di nuovo modulo della differenza, nessuna
    clausola di verso; `mu` entra sotto qualificatore B-stationarity.
- **`phase_diagram_real.py`**: r.208-229 e r.273 verificate riga per riga: il clamp inferiore
  (r.215-216) e il cap superiore (r.273) esistono e sono MUTI (nessun residuo, segno,
  complementarità stampati); il segno esce giusto per monotonia di `P_E(ε)`. La lettura
  dell'advisory («salvi per accidente strutturale») è conforme al codice.

**Verdetto linea 4**: la claim sul codice è VERIFICATA nel merito (nessun carrier testa la
fattibilità duale), con due emende: (i) «identità di modulo» → «identità sul valore firmato
senza clausola duale»; (ii) i punti ciechi sono CINQUE (R3, R7, f3*-drift, reading O3 in a1,
rel_c del governor), e S1 va esteso anche a questi due ultimi.

---

## VERDETTO COMPLESSIVO

**C31: NECESSARIA nella sostanza, SOVRADIMENSIONATA nella forma.** Il gap è reale e provato:
T7(c) di record (M0 r.1089-1095) è la condizione del solo regime bilatero-libero; (P) come posta
(M0 r.246-247) e la riduzione di produzione (phase_diagram_real) portano disuguaglianze; KT2015
p.186-187 pubblica la struttura corretta (2.10)+(2.13)-(2.14) — disuguaglianze per i cap
geometrici, uguaglianza per la portata; nessuno strumento committato testa segno o
complementarità. **MA**: (a) i "tre regimi" collassano in UN enunciato `D ∈ N_K(s_E*)` con K
dichiarato per istanza — la tabella è navigazione, non matematica; (b) l'"incompatibilità
interna" di M0 è sovrastimata: r.1699-1704 è già una dichiarazione di regime 2, il buco è il solo
regime 3 + livello ciclo; (c) "il driver gira in active-set" all'endpoint è falso
(`a1:1748` = uguaglianza), i siti regime-3 veri sono (P) e la riduzione quasi-1D; (d) la
riduzione minimale opposta ("una disuguaglianza scalare") è anch'essa falsa (la radiale ha ramo
interno + due cap di verso opposto).

**Forma minimale che sopravvive (proposta del refuter):**
> **T7(c), forma di record**: `D := ∫_Ξ (∂F/∂s_E)[Σ; s(ξ)] dμ ∈ N_K(s_E*)`, con `K` = insieme
> ammissibile dell'endpoint **dichiarato per ogni enunciato e per ogni strumento** (interno ⇒
> `D = 0`; punto ⇒ condizione vacua, λ = componenti di D a segno libero — il bookkeeping M0
> r.1699 già in essere; cap unilateri ⇒ complementarità per componente con verso dal lato
> attivo). `D` fattorizza `R·w`, `w > 0`: il peso non deforma il cono. **Lemma di trasferimento**
> (fase-in-cono μ-q.o. ⇒ ciclo-in-cono; viceversa falso, controesempio a due fasi a registro) con
> il rejector A39. Contenuto assiale = identità `λ_L = ∫f3*/q dμ` + complementarità (il segno è
> automatico e NON è un falsificatore); contenuto radiale = l'intera condizione unilatera.

**C32: CONFERMATA** (esempio di segni opposti esiste; economia verificata contro il falsificatore
a radici) **con emenda obbligatoria**: qualificatore di regime (il contenuto duale vive solo a
cap attivo) e portata del falsificatore (falsifica la rilevanza sulla classe, non l'esistenziale).

**S1-S3 (A37-A39): NECESSARIE**, con tre emende: S1 estesa ai due carrier ciechi aggiuntivi
(`a1:2356-2365`, `margin_governor:64-73`); S2 con seed rejector sull'IDENTITÀ, non sul segno
(f3* ≥ 0 identicamente ⇒ un sign-check non può sparare, violazione R5); lessico «identità di
modulo» corretto in «identità firmata senza clausola duale».
