# REFUTE-A — Attacco avversariale alla tesi "per-phase adjoint = oggetto simmetria-ridotto corretto"

Refuter: panel avversariale, 2026-08-13. Default applicato: tesi SBAGLIATA finché non regge.
Tesi sotto esame: VERIFICATION_FABLE_2026-08-13.md, STAGE 3 (righe 168-198) + ADDENDUM (righe 200-214).
Fonti primarie lette in questa sessione: ZP arXiv:1512.00616v2 pp.3-8 (Eq. 1-18, §2.1-2.3, Alg. 1-2) e
pp.28-29 (App. A, Eq. A.1-A.7) sul PDF; M0 `docs/rde_nozzle_MASTER.md` righe 28-55, 100-140, 360-410,
441-515, 1180-1214, 1216-1306 (T-T0, T-NSW, D-MU, D-CONTRACT, Part V ladder, VI.1-VI.4bis, B-lite).

---

## Linea (1) — Cosa afferma davvero T-T0: il dato o il problema?

**Fatto di stampa (M0 r.442-445).** Le ipotesi di [T-T0] sono: "rotating-pattern flow
q(x,r,theta,t) = q~(x,r,theta - W t) (piecewise-smooth, transversal fronts); S fixed axisymmetric;
Pa constant". L'ipotesi è sul **CAMPO INTERO** (ansatz di pattern rotante sulla soluzione), non sul
solo dato d'interfaccia. Le claim (i)-(iii) (r.446-453) sono: spinta costante, uguaglianza wave-frame,
chiusura assiale senza forze di riferimento. T-T0 quindi dimostra: *SE il campo è un pattern rotante,
ALLORA il problema è steady nel frame co-rotante (e la spinta è costante)*.

**Il salto della tesi.** La tesi enuncia l'ancora come "dominio assialsimmetrico + BC a onda rotante
pura ⇒ il riferimento co-rotante rende il problema STEADY". Questo è un enunciato di
**PROPAGAZIONE** (dato-pattern ⇒ campo-pattern) che T-T0 **non contiene**. In M0 il campo-pattern è:
(a) l'ipotesi di classe di flusso della census row (r.1182 "The flow — not the method — selects the
reduction"; r.1185 riga single/k-wave), monitorata a posteriori dal certificato T0-flatness
(D-MU scope note r.108-114; VI.1 r.1222-1225); (b) il gradino **I1 della LADDER DI IDEALIZZAZIONE**
(D-CONTRACT r.122-123: "I1 wave-frame steady field") — cioè una idealizzazione dichiarata, non un
teorema.

**Dove le ipotesi sono nominate in M0** (la tesi le nomina; M0 pure, righe): S assialsimmetrica =
T-T0 r.444-445; parete assialsimmetrica = r.363-364 ("wall pressure on an axisymmetric wall");
Gamma_d assialsimmetrica = D-CONTRACT r.116-117. Le ipotesi geometriche CI SONO.

**Ciò che manca ed è provabile.** Sul default L4 (u_x − c ≥ δ su ogni patch, r.125-137) il campo è
l'unica soluzione del march spaziale B-lite (r.1199-1206); per equivarianza SO(2) del sistema
(dominio+parete+equazioni assialsimmetrici) la ruotata di una soluzione è soluzione col dato ruotato;
dato puro-rotante + unicità ⇒ campo-pattern. Questo **lemma di equivarianza non è scritto in M0**
(nessun enunciato lo nomina): è cheap e in-window, quindi per la direttiva "mai posticipare il
risolvibile" va scritto (duty R4), ma OGGI la tesi non può citare T-T0 da solo per il passo
"rende steady".

**VERDETTO (1): INDEBOLITO.** Forma che sopravvive: *in-pin la steadiness co-rotante vale per
(ipotesi-di-classe dichiarata + monitor) oppure, sul default L4, per un lemma
unicità+equivarianza PROVABILE ma non ancora enunciato in M0; l'attribuzione a "T-T0 exactness"
da sola è una citazione eccessiva.*

---

## Linea (2) — Il salto "3-D steady co-rotante" ⇒ "marce 2-D per fase indipendenti"

**Il quoziente giustifica UN oggetto solo.** L'oggetto reso esatto dal quoziente è il funzionale
steady 3-D nel wave frame col suo adjoint: (a) forma anchor con Ω incognita ("EIGENVALUE-like
unknown (freezing formulation + phase condition)", T-T0 conseguenze r.460-461); (b) forma B-lite
nozzle-only con Ω INPUT dal dato, adjoint = march trasposto per Lemma B (r.1199-1214). Punto
strutturale che la tesi non enuncia: **il quoziente converte l'accoppiamento TEMPORALE in
accoppiamento SPAZIALE in θ** — nel wave frame le "fasi" restano accoppiate dalle derivate
elicoidali in θ (è ciò che il march B-lite integra). La periodicità sparisce; l'accoppiamento
tra fasi NO.

**La decomposizione per-fase è un passo ulteriore e M0 lo dice.** (i) CAUTION di T-T0 stessa
(r.463-464): "T0 steadifies the PROBLEM; it does NOT transfer Rao's 2-D closed-form machinery";
(ii) r.374-380: la fattorizzazione per-fase steady è "THE ONLY APPROXIMATION in the chain",
prezzata O(St) (corrector P4, backstop nonperturbativo T0); (iii) r.514-515: "The huge relative
swirl never enters rung 2: it IS the O(St) sweep term" — cioè ESATTAMENTE l'accoppiamento in θ
che il quoziente NON rimuove.

**Conseguenza sulla claim.** "L'adjoint per-fase steady È l'oggetto simmetria-ridotto CORRETTO"
confonde rung 3a (l'oggetto del quoziente) con rung 2 (la famiglia per-fase). Il punto 3 dello
Stage 3 (r.193-196) dichiara il prezzo separatamente — la consapevolezza c'è — ma il TITOLO della
tesi resta falso alla lettera.

**VERDETTO (2): REFUTED come formulata.** Forma corretta che sopravvive: *l'oggetto
simmetria-ridotto corretto è l'adjoint steady 3-D wave-frame (B-lite/anchor); l'adjoint per-fase
2-D ne è la fattorizzazione quasi-steady di rung 2, esatta a meno del termine sweep O(St)
prezzato (T-T3QS + meter B-lite r.1208), e nel gap NON resta alcun residuo di periodicità
temporale — resta solo il residuo di accoppiamento θ/sweep, che è un'altra cosa e ha un altro
prezzo.*

---

## Linea (3) — Autonomo vs guidato: l'uso di "mal posta" sopravvive?

**Verificato a stampa su ZP.** Eq. (1) p.3: ∂U/∂t = L(U,μ,t) — dipendenza esplicita da t, periodo
T FISSATO nella formulazione (sistema guidato); Eq. (15) p.6: J(u₀) = ∂u^(Nt)/∂u₀ − I; App. A
p.28: l'operatore delle sensitivity "is assumed non-singular at a time-periodic solution"; p.29:
"Since the Jacobian of the time-periodic residual, ∂u^(Nt)/∂u₀ − I, is non-singular … exists and
is unique"; §2.3 p.8: caso neutrally-stable (moltiplicatori sul cerchio unitario) = caso duro
dichiarato dagli autori.

**Il sottoproblema di design in-pin è GUIDATO.** Con dato d'interfaccia imposto e Ω input
(B-lite r.1201-1202), il problema lab-frame è driven-periodico. Sulla classe L4 il dominio è
assialmente supersonico con margine: ogni perturbazione della condizione iniziale esce dal dominio
in tempo finito (dominio di dipendenza finito) ⇒ ∂u^(Nt)/∂u₀ ≈ 0 (a livello discreto: fortemente
contrattiva) ⇒ I − M non singolare in modo robusto. **ZP si applica ed è ben posto.** Quindi, per
il problema che il programma effettivamente risolve, l'affermazione dello Stage 3 punto 2
(r.191-192) "the naive time-domain periodic adjoint would be ill-posed without the same quotient"
è **FALSA**: l'alternativa ZP in-pin è ben posta, solo strettamente dominata (ricalcola a costo
O(Nt) + solve di periodicità lo stesso oggetto steady che il quoziente dà gratis; e per unicità
la soluzione driven-periodica È il pattern rotante).

**Dove la degenerazione è vera.** Solo per la vista sistema-completo AUTONOMO (Ω output, periodo
incognito): lì il moltiplicatore banale 1 (autovettore −W ∂_θ q~, non nullo per onda non
costante; rotazione e traslazione temporale generano lo STESSO modo — un solo moltiplicatore
banale, non due) fa cadere l'assunzione di App. A; in più ZP-as-printed non ha il periodo
incognito (T fisso in Eq. 1), quindi mancherebbe comunque la phase condition/bordatura. Ma
precisione da refuter: la singolarità rompe la **PROVA di unicità** di ZP, non rende il gradiente
privo di senso — "non coperto da ZP come stampato" è l'enunciato corretto; "mal posto" è
sovra-claim anche lì (il fix bordato è standard, ed è esattamente la freezing formulation di M0
r.461 e la riga RPO "doubly bordered adjoint" r.1186).

**VERDETTO (3): INDEBOLITO.** Forma che sopravvive: *la secondaria vale come "ZP come stampato
non copre l'onda autonoma (moltiplicatore 1 + periodo incognito: l'assunzione di App. A cade e
manca la bordatura)"; applicato al sottoproblema guidato in-pin ZP è ben posto ma dominato. Le
parole "ill-posed/mal posta" vanno RITIRATE dal confronto in-pin; l'ADDENDUM (r.207-213) ha già
fatto metà di questa correzione spostando la steadiness a primario, ma il testo del punto 2 dello
Stage 3 resta a stampa con la frase falsa.*

---

## Linea (4) — Assialsimmetria esatta: in-pin dichiarato? Dove?

**Dichiarazioni trovate (righe M0):** scope standing puro-periodico single-mode con monitor =
T0 flatness: D-MU scope note r.108-114 (+ memoria di progetto periodic-wave-data-scope, pin
VI.4bis r.1247-1282); Gamma_d "fixed axisymmetric surface" r.116; S assialsimmetrica T-T0 r.444-445;
parete assialsimmetrica r.363-364. Gli iniettori discreti vivono A MONTE di Gamma_d: nel contratto
D-CONTRACT entrano SOLO attraverso il dato s(y;ξ) — la rottura hardware dell'assialsimmetria è
fuori dominio di design e dentro la classe-dati. **In-pin è dichiarato.**

**Caveat da refuter (residuo nominato, non refutazione).** Un'impronta di iniettore FISSA NEL
LAB FRAME (armonica locked al conteggio iniettori, funzione di θ e non di θ−Wt) produce spinta
COSTANTE (stessa prova shift-invariante di T-T0(i) applicata a un campo lab-steady): il monitor
di FLATNESS è CIECO a questo canale. Il dato diventa a due frequenze s(θ, θ−Wt), FUORI dal
contratto CycleFamily (che ammette solo (y;ξ), r.1219-1225): il rigetto deve venire dagli audit
armonici/di contratto e dal monitor TRIPLA(Γ,h₀,s) del panel mean-swirl, non dalla flatness.
Questa distinzione di detector non è oggi esplicitata accanto al pin.

**VERDETTO (4): TIENE** (dichiarazione in-pin esistente alle righe citate), con residuo nominato:
*flatness ≠ detector della rottura lab-steady di assialsimmetria; il detector di quel canale è
l'audit armonico del contratto dati (+ delta F2a mean-swirl), e la frase va aggiunta accanto al
monitor perché il pin sia onesto sul suo strumento.*

---

## Linea (5) — Coriolis/centrifuga nel frame co-rotante: falla fatale o termine prezzato?

**Fatto di stampa.** T-T0(iii) prova SOLO l'annullamento ASSIALE delle forze di riferimento
(r.452-453, 458-459: Coriolis −2W e_x×w ⊥ e_x; centrifuga W²r radiale). Nel sistema meridionale
co-rotante scritto nelle variabili relative w le componenti radiale (2W w_θ + W²r) e azimutale
(−2W w_r) sono O(1) (W r ~ D_CJ). Equivalentemente, in variabili lab con coordinata ζ = θ−Wt non
ci sono forze apparenti ma compare il termine di sweep W∂_θ. In ENTRAMBE le scritture il sistema
steady co-rotante esatto ≠ sistema di Eulero meridionale delle marce per-fase: la differenza è
esattamente il termine di sweep/swirl relativo.

**È prezzato?** SÌ, a stampa: r.514-515 ("the huge relative swirl … IS the O(St) sweep term" —
il termine non entra in rung 2 ed è l'oggetto del corrector); VI.4bis(ii) r.1261-1266 (due rotte
del corrector O(St), quella steady = sweep-perturbation solve sull'anchor wave-frame); T-T3QS
r.392-410 (primo ordine nullo sui ray cycles lisci, residuo jump-localizzato); B-lite = "cheap
exact meter of the rung-2 sweep/D2 residual" r.1208. **Non è la falla fatale della FORMULAZIONE**:
è la voce di ledger dichiarata (r.379-380) con backstop nonperturbativo (rung 3a).

**Due precisazioni da refuter.** (i) L'etichetta "O(St)" porta le sue ipotesi: sul fronte di
passaggio d'onda il gradiente in θ non è O(1) e il residuo di primo ordine è jump-localizzato —
il suo assorbimento da parte della fitted sheet è la predizione O5 P-ii, **CONGETTURALE finché
non misurata** (r.403-406). (ii) Il fatto che il termine sia prezzato NON salva il titolo della
tesi: è precisamente questo termine a rendere l'adjoint per-fase ≠ oggetto del quoziente
(alimenta il verdetto REFUTED della linea 2).

**VERDETTO (5): TIENE-come-prezzato** (termine dichiarato, corrector + meter + backstop a
registro; residuo congetturale P-ii dichiarato), e simultaneamente conferma la refutazione del
titolo della tesi.

---

## Linea (6) — aggiunta del refuter: la claim del moltiplicatore banale

Per un sistema autonomo con orbita periodica non costante la monodromia ha moltiplicatore 1 con
autovettore du/dt; per un'onda rotante du/dt = −W ∂_θ q~ coincide col modo di rotazione — il
gruppo agisce con orbita unidimensionale, quindi UN solo moltiplicatore banale generico (la tesi
non ne reclama due: coerente). ZP §2.3 p.8 conferma che già il caso neutrally-stable è il caso
duro dichiarato; il moltiplicatore ESATTAMENTE 1 rende J (Eq. 15) singolare, peggio del caso
duro. **TIENE** (struttura verificata; nessuna refutazione trovata su questa gamba).

---

## VERDETTO COMPLESSIVO

La tesi NON regge nella formulazione a stampa: **(a)** l'ancora primaria cita T-T0 per un passo di
propagazione (dato ⇒ campo) che T-T0 non enuncia — INDEBOLITA (lemma equivarianza+unicità su L4:
provabile, NON scritto; duty R4); **(b)** il titolo "l'adjoint per-fase È l'oggetto
simmetria-ridotto corretto" confonde rung 3a con rung 2 — REFUTED alla lettera; **(c)** l'uso
"l'applicazione ingenua sarebbe mal posta" è falso per il sottoproblema in-pin guidato —
INDEBOLITO.

**FORMULAZIONE CORRETTA CHE SOPRAVVIVE ALL'ATTACCO** (da sostituire al titolo di Stage 3):

> In-pin (dato puro-rotante single-mode su Gamma_d assialsimmetrica, parete assialsimmetrica,
> margine L4), il quoziente per rotazione è esatto e rimuove TUTTO e SOLO l'accoppiamento
> temporale: l'oggetto simmetria-ridotto corretto è **l'adjoint steady 3-D nel wave frame**
> (march trasposto B-lite quando Ω è input; forma freezing+phase-condition bordata quando Ω è
> output — la bordatura È il residuo simmetria-ridotto della macchina periodica, non la sua
> assenza), a valle di un lemma di propagazione dato⇒campo (unicità L4 + equivarianza SO(2))
> oggi non enunciato in M0 e da scrivere. **L'adjoint per-fase 2-D non è quell'oggetto**: ne è
> la fattorizzazione quasi-steady di rung 2, il cui gap è il termine sweep in θ — prezzato
> O(St) (T-T3QS; meter B-lite; residuo jump P-ii congetturale fino a O5) e privo di qualunque
> residuo di periodicità temporale. Quanto all'alternativa: ZP come stampato non copre l'onda
> AUTONOMA (App. A p.28-29: (I − monodromia) assunta non singolare; moltiplicatore banale 1;
> periodo incognito assente dalla formulazione Eq. 1), mentre sul sottoproblema GUIDATO in-pin
> è ben posto ma strettamente dominato dal quoziente — "dominata", mai "mal posta".

Azioni minime perché la parte sopravvissuta diventi citabile (tutte cheap, in-window per la
direttiva never-postpone): (1) scrivere in M0 il lemma di equivarianza/propagazione (classe L4)
accanto a T-T0; (2) emendare il punto 2 di Stage 3 sostituendo "ill-posed" con "not covered as
printed (autonomous) / well-posed but dominated (driven in-pin)"; (3) annotare accanto al pin
che il detector della rottura lab-steady di assialsimmetria è l'audit armonico del contratto,
non la flatness.

Stato: verdetto di refuter single-pass; per lo standard dual-proof del progetto resta da
consumare in panel (giudice) prima dell'ingresso in M0.
