# ADVISORY — Fedeltà MoC al riferimento Zucrow-Hoffman Vol.2 Cap. 16-17
# (motore differenziale [X-A1IM]/[X-TOCV] + GENO), campagna a convergenza 2026-08-13

STATO: CAMPAGNA PARZIALMENTE CHIUSA (7 flussi su 9 completi; 2 troncati dal limite di
sessione — vedi §7 RESIDUI). Sessione avviata dalla domanda utente: "il motore
differenziale marcia sempre su profilo fisso senza fasi alla Goursat? e le routine MoC /
marcia / BC di parete di GENO sono SOTA come da letteratura (Zucrow cap. 16-17)?"

RIFERIMENTO DI RECORD: Zucrow & Hoffman, Gas Dynamics Vol.2 (Wiley 1977), Cap. 16-17
(+ §15-5 Sauer), PDF in GENO/literature/. Mappatura verificata: pagina-libro = pagina-PDF − 9.

METODO: find -> verify avversario (default-REFUTE) -> aggiudicazione. 3 lettori integrali
+ 4 verificatori avversari + 1 workflow find/verify/critic (5 finder per slice + verifier
per finding). Peso riportato: ~14 agenti dedicati + workflow (14 agenti, 7 completati).

---

## 1. RISPOSTA ALLE DOMANDE DI APERTURA

### 1.1 Motore differenziale: struttura di marcia — CONFERMATO
Il motore TOC ([X-TOCV], validation/a1_toc_variational_jax.py) è una **specified-wall
direct march**: parete NOTA E FISSA durante ogni singola marcia (vettore di design
W = [theta_B, y_1..y_m], spline C^2), che cambia SOLO nel loop esterno TR-SQP.
Propagazione **sempre a valle**, per colonne C− successive (IVL Sauer -> fan -> settore
arco -> contour -> asse); ogni cella interior risolve **entrambe le famiglie
simultaneamente** (4 residui: 2 posizioni caratteristiche + 2 compatibility).
La causalità solo-a-valle è un **rejector per-cella** (u_x > c, :335-347), non un'ipotesi.
**Nessuna fase di Goursat, mai.**

Precisazione: l'ideal march ([X-A1IM]) ha una coda di sapore generativo (fase 5: linea di
Mach d'uscita dal fuoco K come punti-testa prescritti + parete piazzata al crossing di
portata) — ma consumata come marcia in avanti ordinaria per colonne, mai come solve a due
caratteristiche. Lì la parete è OUTPUT; nel TOC è INPUT.

### 1.2 Il termine "Goursat" — CORRETTO, con correzione di definizione
Goursat = problema a dati su **due archi caratteristici di famiglie opposte** che si
intersecano; Zucrow lo usa esattamente così (p. 162 verbatim: "data specified on two
characteristics of opposite families (i.e., a Goursat problem)").
**CORREZIONE DI RECORD**: la chiusura del profilo con conservazione della portata **NON fa
parte della definizione di Goursat**. Sono due ingredienti distinti che convivono nella
stessa fase di design: (i) il Goursat determina il CAMPO nella regione R; (ii) la parete è
individuata DENTRO quel campo dove la portata cumulata eguaglia mdot (p. 162, Fig. 16.30).
Per flusso stazionario "level-set di massa" ≡ "streamline delimitante".
In GENO le fasi Goursat vive sono: regione R nel design, e il kernel anulare
(throatExpansionShrouded_solve) che è un Goursat a due parametri genuino.

### 1.3 Direct wall vs inverse wall — DISTINZIONE DI RECORD
"Marcia diretta" (tipo di PROBLEMA: parete nota) NON implica "direct wall process"
(processo UNITARIO, Zucrow §16-3c). Il motore differenziale usa **SEMPRE l'inverse wall
(§16-3d), mai il direct**, a ogni stazione (arco + contour spline).
Entrambi i processi impongono **le stesse equazioni** (tangenza + compatibility della
famiglia entrante); differiscono solo in cosa è prescritto:
 - direct: punto interno noto -> posizione del punto parete = OUTPUT (spaziatura dettata
   dalle caratteristiche);
 - inverse: punto parete (posizione + pendenza) prescritto -> piede = OUTPUT.
Il libro raccomanda l'inverse dove i punti vanno prescritti / i gradienti sono alti
(pp. 130-131, 145 verificate: il direct dà spaziatura di parete TROPPO RADA in gola).
Per il motore variazionale l'inverse è preferibile anche strutturalmente: le stazioni SONO
i gradi di libertà di design -> topologia congelata -> dJ/dW esatto nel replay
differenziabile. Col direct la topologia diventerebbe dipendente dalla soluzione.
IPOTESI DICHIARATA (ri-aggiudicabile): la spline tra le stazioni non è interrogata dal
solve; in-hypothesis perché la classe di parete è spline C^2 a Nw congelato e J è quadrato
sulle stesse stazioni. Test che la chiuderebbe empiricamente: march su profilo fissato con
Nw raddoppiato (Richardson su spinta e campo).
Dove il direct SAREBBE il processo giusto: analisi di contorni fissati/esterni (es.
ri-marciare un contorno GENO per un O2 più stretto), off-design, o classe di parete con
contenuto inter-stazione. In GENO esiste ed è il path di analisi (DirectWall_m, tipi 3 e 6).

---

## 2. BC DI PARETE DEL MOTORE — DIMOSTRATA (era il dubbio centrale dell'utente)

Verificatore avversario default-REFUTE, ri-derivazione da zero: **nessun item confutato**.

| Task | Esito |
|---|---|
| Residuo = (16.9) posizione C+ + (16.11)/(16.13) compatibility + tangenza v4=slope*u4 sostituita ESATTAMENTE | CONFERMATO, simbolo per simbolo |
| Coefficienti agli stati MEDI (average-property, 16.22-16.23) — la variante che il libro RACCOMANDA (§17-6(h) p. 264-265) | CONFERMATO |
| Famiglia C+ corretta per parete superiore; sorgente S+ mai valutata a y=0 | CONFERMATO |
| Processo = inverse wall §16-3d (non direct); interpolazione del piede = costruzione "line 13" del libro, parametro D condiviso da posizione E stato | CONFERMATO |
| Residuo=0 caratterizza ESATTAMENTE il punto fisso a convergenza del PC di GENO (InverseWall_m) | CONFERMATO |
| record / replay / jitted risolvono residuo identico, indici corda (N,Nv) congelati | CONFERMATO |
| Conteggio BC completo: 2 incognite <-> tangenza + 1 compatibility della sola famiglia ENTRANTE (imporre anche C− = sovradeterminato; non c'è) | CONFERMATO |
| Continuità C^1 arco->spline in theta_B (clamped end riproduce tan(theta_B) esattamente) | CONFERMATO |

DIFFERENZA A FAVORE DEL MOTORE: dove GENO esce al cap icor con iterata non convergente e
SILENZIOSA, il motore fallisce rumorosamente la certificazione Newton per cella (rejector).

Micro-finding (P2, nessuno di correttezza): locale morto `lmch`
(a1_ideal_march_jax.py:573); docstring cita tol 1e-8 dove la costante interna GENO è 1e-6
(InverseWall_m.f90:62); caso degenere mai registrato nel path jitted (clip su corsia PAD se
N=len(prev)+1, a1_toc_variational_jax.py:1067); disciplina chiavi `cached_solvers`
affidata al chiamante.

---

## 3. FORMULE GENO vs ZUCROW — RI-DERIVATE AVVERSARIALMENTE: TUTTE ESATTE

| Elemento | Riferimento | Esito |
|---|---|---|
| Interior Ch.16: Q=u²−a², R=2uv−Qλ, S=δa²v/y, compat 16.11-16.14 | Tab. 16.3-16.4 | CONFERMATO esatto |
| Casi λ=∞ special-cased | avvertenza p. 120/127 | CONFERMATO |
| Interior Ch.17: p4, θ4 da eliminazione 17.50+17.51 | Tab. 17.2-17.3 | CONFERMATO esatto; **sospetto "assorbimento di segno" nelle sorgenti CONFUTATO** (l'eliminazione diretta riproduce il codice alla lettera, incluso +(θ2−θ1)) |
| Axis Ch.17: p4 da 17.51 con θ4=0; ȳ=½y1; sin(θ̄) | §17-4(e) + **listing AXIS pp. 215-216** | CONFERMATO **book-exact** (la prosa del libro è ambigua — p.215 "average of sin θ" vs p.199 "average of θ" — i listing FORTRAN dirimono: `A=0.5*(A1+A4)` poi `SIN(A)`, cioè sin(θ̄): esattamente GENO) |
| Inverse wall Ch.17 (upper C+ / lower C−): p4 da 17.50 / 17.51 | Tab. 17.3 | CONFERMATO esatto, struttura di segno speculare corretta |
| Jet points, stream point: mappatura lato/famiglia e segni | 17.50/17.51 | CONFERMATO |
| Streamline Ch.17: isentropa log-space + Bernoulli trapezoidale sub-stepped al posto di 17.56-17.57 | 17.56-17.57 | CONFERMATO equivalente O(Δp³)/passo (derivazione LTE eseguita); soglia sub-step 0.1 = euristica non derivata (tensione già a registro in GENO/CLAUDE.md) |
| Integrale di massa di colonna: fn = Δy·cosθ − Δx·sinθ | (16.37) ρV[sin(φ−θ)/sinφ]2πy dy | CONFERMATO **identico**, in forma priva di singolarità (nessuna /sinφ) |
| Corner condition CSTR_PA: p_a = p − ½ρV²sin(2θ)tanα | (16.42) | CONFERMATO **algebricamente la stessa equazione** risolta per p0 |
| Rao boundarycurvestep: {d(16.43)=0 + compatibility C+} | (16.43)/(16.44) | Formule CONFERMATE esatte; **equivalenza a {(16.43)+(16.44)} DIMOSTRATA** (R-1 chiuso, vedi §7.1) |
| Sauer §15-5: α, c1, c2, ε, offset +1e-6, ordine delle operazioni | listing IVLINE p. 94 | CONFERMATO **esatto in ENTRAMBE le implementazioni**, incluso l'ordine non ovvio (u dalla x non traslata, poi shift −ε) e l'offset +1e-6 che è NEL LISTING DEL LIBRO |
| Organizzazione marcia (IVL -> triangolo -> arco a punti inverse -> C− all'asse; design: kernel -> superficie di controllo -> regione R -> parete da massa) | §16-4(a)/(b)/(c) | CONFERMATO conforme |

ANCORE DEL LIBRO: 11/11 CONFERMATE su rilettura pagina per pagina (2 precisazioni minori:
la Table 17.3 stampata contiene solo 8 delle equazioni attribuite — le altre sono nel testo
del §17-4(b), formule tutte corrette; "streamline secants" è un misnomer per le
compatibility di streamline 17.56-17.57).

---

## 4. FINDING SOPRAVVISSUTI ALL'ATTACCO (da registrare come righe tipizzate)

| ID | Sede | Severità | Claim |
|---|---|---|---|
| MOC-01 | Interior_m.f90:65 + InverseWall_m.f90:87 | P1 | Criterio di convergenza velocità con **RHS FIRMATO** (`abs(Δv) < E2*vc`, vc = iterata precedente firmata): per **v ≤ 0 il test è identicamente falso** -> esaurimento silenzioso garantito di tutte le 21 passate. VIVO in produzione: famiglia inferiore del kernel anulare/migdal (θ<0 -> v<0), caso con baseline md5 congelata. Danno limitato per celle contraenti (iterata al cap ~1e-11 dal punto fisso); il danno vero è il **mascheramento delle celle NON contraenti**, le sole pericolose. Viola GENO/CLAUDE.md §3 "zero silent exit". |
| MOC-02 | InverseWall_m.f90:31-64 | P1 | Il loop interno di posizione **non ha alcun cap di iterazione**: oscillazione sopra 1e-6 = hang infinito dentro subroutine `pure` (nessun I/O possibile, non diagnosticabile). |
| MOC-03 | CircularContour_m.f90:112 | P1 | `throatExpansion_solve`: esaurimento THROAT_MAXITER esce dallo **STESSO ramo** del caso convergente (`.or. iter>THROAT_MAXITER`), **sovrascrivendo Me** con il Mach d'asse raggiunto, senza messaggio. `iter` è locale, non in firma: **nessun chiamante può distinguere convergenza da esaurimento**. Consumatori: run_ideal (tipo 0), run_conico (tipo 3), run_tic (secante su Me, tipo 1), raocore_solve (M1d intent(inout), tipi 2/4/6). Per tipi 0/3 non esiste loop esterno -> ugello progettato per il Mach sbagliato con output di aspetto nominale. Il gemello anulare fa **error stop** sullo stesso THROAT_MAXITER (L744-754): asimmetria che prova che la regola è nota. |
| MOC-04 | Profile_m.f90:649 (+ L806, L1283, L1379) | P1 | Path legacy **Ch.16** (ideal, TIC, migdal): il ramo di crossing di massa è l'**UNICO scrittore** di sol(1,i), thrust e Nv. Se la massa cumulata di colonna non attraversa mai mdot_ref, il loop termina **senza chiusura di parete e senza diagnostica**: per Nv=1 il punto interno di scratch (goursat j=1) finisce NELLA riga di parete, e la colonna successiva lo consuma come prev_col(1)/perf%yw/pw. Il gemello **Ch.17 tratta lo stesso stato come FATALE** (error stop "converged WITHOUT a mass crossing", L391-398) e ha il restore `wall_save` che Ch.16 non ha -> **difetto mascherato dalla dualità di backend**. Il solo path TOC Ch.16 fu patchato con chiusura forzata (`.or. j == Nv` + D=min(D,1), L1026-1028): asimmetria che prova che il buco era noto e turato su uno solo dei tre path. |
| MOC-05 | MoC_Gen_m.f90:559-574 | P1 | Inverse wall Ch.17: estrapolazione del piede **non clampata e senza guardia di positività** su ρ,p -> ρ2≤0 o p2≤0 danno NaN silenzioso al giro dopo (aP=√(γp/ρ)). Latente: segmento esattamente orizzontale passa la guardia L563 ma dà frac=Inf a L567. Nota di trasparenza: commento di dubbio in italiano non chiuso a L576-578 (consistenza dell'interpolazione del piede streamline). |
| MOC-06 | IO_m.f90:312-317, 560-561 | P2 | Default `icor=20`, `tol_conv=1e-8`, E1=E2=tol_conv **vivi in TUTTA la produzione** (sweep su ogni .ini: zero override; `[GENO-solver]` di tocnoz è letteralmente vuoto) contro la prescrizione di economia del libro (≤2 correttori giustificati p. 261; frazionale 1e-3 sufficiente; 1e-8 costa ~2× per nulla, Fig. 17.36; "reduce point spacing rather than iterating more" p. 120). Costo misurato analiticamente: ~2.3× su cella convergente, 7× su cella al cap (2 `td%solve` per passata). **Leva velocità lato GENO** (aggancio a S25/S25-bis). |
| MOC-07 | tutti i moduli MoC | P2 | Nessun monitor di incrocio caratteristiche/fold. Il libro discute 3 opzioni (p. 149, validità fino a rapporto di pressione ~4-5) e NOZZLE usa l'opzione 1 = lasciarle incrociare: GENO è opzione-1-**senza monitor**. Guardie indirette non fold-specifiche (kgrid loud scan solo anulare; identità di massa A4 al 10% con 3-4 ordini di margine; NaN check solo bootstrap); `Interior_m.f90:51-55` (y<0 -> return silenzioso con u=v=0) è un **anti-guard**. Copertura: **affermativamente in-hypothesis** — scoperta collaterale: **il contorno TOP e il cono NON vengono MAI marciati** (sono output geometrici, non domini MoC: run_top fitta e scrive; run_conico marcia l'ideal design), quindi la giunzione arc->cone temuta dal libro non entra nel calcolo. Esposizione **latente**, non viva. |
| MOC-08 | InitialValues_m.f90:73-96 + a1_ideal_march_jax.py prep_tab | P2 | Raffinamento del critical speed a **M=1.000005 NON esiste nel libro** (IVLINE usa a* analitico perfetto). Deviazione nata in GENO e **copiata deliberatamente** dal motore. Difendibile per thermo tabulare (a* analitico non dà più M=1 sulle tabelle) ma **senza fonte nel riferimento**: registrare come deviazione dichiarata, non come errore. |
| MOC-09 | Extension_m.f90:305 | P1-NON VERIFICATO | Nella fase di fan (do_axis=.true., j2 fisso) `march_column` wira il punto noto C+ come pt2=old(jj+1) mentre memorizza alla riga jj — **una riga di scarto** rispetto al legacy e al contratto di griglia, e fabbrica un punto asse dove il legacy calcola un punto interno. **Verifica troncata dal limite di sessione**: da confermare/confutare prima di qualunque uso. |

### 4.1 CLAIM UCCISI DALL'ATTACCO (onestà di record)
- "Test relativo su v quasi insoddisfacibile vicino all'asse": **FALSO** — un test relativo è
  scale-invariant, la piccolezza di v non lo rompe. Il difetto vero è il segno (MOC-01).
- "E1=1e-8 assoluto = machine-forcing": **FALSO** — raggiungibile (round-off intersezione ~1e-15).
- "Costo 10× vs icor=2": **gonfiato** — reale ~2.3× (convergente) / 7× (al cap).
- "Le sorgenti Ch.17 devono assorbire un segno per far tornare p4": **CONFUTATO**.
- "Smoothing_m assente/inutilizzato": **impreciso** — esiste ed è chiamato, ma solo da
  `write_profile` (post-processing di output, mai reimmesso nella soluzione).

---

## 5. AGGIUDICAZIONE SOTA

**GENO**: le routine MoC, la marcia e le BC di parete sono **fedeli allo Zucrow
formula-per-formula**, con la variante che il libro stesso raccomanda (average property) e
upgrade dichiarati (streamline trapezoidale-adattiva al posto delle secanti linearizzate;
piede da invarianti, fix N-26). Le distanze dal riferimento NON sono di correttezza delle
equazioni ma di **robustezza/trasparenza** (MOC-01..05) ed **economia** (MOC-06).

**Motore differenziale**: BC di parete dimostrata equazione per equazione; percorre l'altra
strada canonica del libro rispetto a GENO — campo calcolato su contorno assunto + rilassato
verso il massimo di spinta via gradiente — che è esattamente la via che Zucrow indica per il
caso generale (p. 232 verificata, Scofield-Hoffman: "the flow field [must be] calculable for
an assumed contour, which is then relaxed to obtain the maximum thrust contour"). Le due
formulazioni sono duali sullo stesso ottimo; O2 le confronta per questo.

---

## 6. IPOTESI E DEVIAZIONI DICHIARATE (nessuna silenziosa)
1. Motore: la parete tra le stazioni non è interrogata dal solve (in-hypothesis per classe
   spline C^2 a Nw congelato; test di chiusura: Richardson su Nw raddoppiato).
2. M=1.000005 (MOC-08): deviazione dal libro, GENO-originata, copiata dal motore.
3. Soglia sub-step 0.1 sulla streamline Ch.17: euristica non derivata da analisi d'errore
   (tensione rigore-vs-robustezza già documentata in GENO/CLAUDE.md §2).
4. Tolleranza 1e-6 assoluta nel loop interno inverse wall Ch.16: coincide con la costante
   del listing INWALL del libro (p. 132); scale-safe fino a yt ~1e-3, non raggiunto in
   nessun caso committato.
5. Fold non monitorato (MOC-07): in-hypothesis per tutto ciò che GENO marcia oggi.

---

## 7. RESIDUI APERTI (dichiarati, con leva nominata)

| # | Residuo | Leva |
|---|---|---|
| R-1 | **CHIUSO 2026-08-13 — vedi §7.1.** Dipendenza (16.43)/(16.44) DIMOSTRATA (rank 2, CAS + 2000 probe). GENO non perde nulla non codificando mai la (16.44). | — |
| R-2 | **CHIUSO 2026-08-13 (resume, 14/14) — vedi §7.2.** 110 call-site puliti, 8 finding verificati (1 P0 quantificato + 3 P1 nuovi + 2 P2 + 2 split) + critic. Restano non verificati i finding oltre il cap di severità (dichiarati nel log del workflow, non a registro come veri) e il residuo mappato dal critic (tipo 5 plug, azzeramento righe run_toc). | Prossima finestra: tipo 5 (plug) = buco maggiore. |
| R-3 | **Item chiudibili solo empiricamente**: istogramma delle iterazioni d'uscita per classe di cella (chiude la congettura di lentezza near-axis e la frazione di celle al cap per MOC-06) e popolazione reale v<0 nel kernel migdal (dimensiona MOC-01). | Un run strumentato su s3 (print di `iter` all'uscita). |
| R-4 | Fine print §17-4(e) sulla media di sinθ: **CHIUSO** (listing del libro -> GENO book-exact). | — |

### 7.1 R-1 CHIUSO — dipendenza (16.43)/(16.44) DIMOSTRATA (2026-08-13)

**VERDETTO: DEPENDENT, rango 2 su 3.** Il sistema {d(16.43)=0, compatibility C+, d(16.44)=0}
nei differenziali (dV/V, dθ, ds/y) ha determinante **identicamente nullo** e rango esattamente
2: **due qualsiasi implicano la terza** (tutte e tre le coppie verificate a rango 2).
Quindi GENO, imponendo {d(16.43)=0 + compat C+} e non toccando MAI la (16.44), **non perde
nulla**: la (16.44) è un **integrale primo automaticamente conservato** dallo stepping, con
C2 fissata dal punto iniziale su DE.

Ipotesi sotto cui vale (tutte soddisfatte nel problema di Rao): δ=1 (assialsimmetrico — la
(16.44) contiene y ed è priva di senso nel piano; il bracket planare NON è identicamente
nullo), omoentropico + omoentalpico (α=α(V), dρ/ρ=−M²dV/V), DE genuinamente caratteristica.
**NON richiede γ=cost**: l'identità vale per Λ=V·dα/dV come simbolo libero, quindi è
EOS-generale esattamente come la boundary function di GENO.

Meccanismo (A=tan(θ−α), B=tanα, Λ=V·dα/dV, x=dV/V, N = ΛB(A+B) − (A−B) = numeratore `val`):
```
(C) compat C+ axisym:  x − B·dθ = S,  S := δ·B·sinα·sinθ·(ds/y)
(A) d ln[V cos(θ−α)/cosα] = 0  =>  x·[1+Λ(A+B)] = A·dθ   =>   S = −x·N/A
(B) sostituendo dθ e ds/y:  d ln(B) = x·[Λ·c1 + c0],
    con c1, c0 entrambi ∝ P = sin(θ+α)cos(θ−α) − sinθcosθ − sinαcosα ≡ 0
    (identità prodotto->somma: ½(sin2θ+sin2α) − ½sin2θ − ½sin2α)
```
CAS: c1 -> 0 esatto, c0 -> 0 esatto, bracket completo -> 0 per Λ arbitrario; 2000 probe
casuali (ramo C+ e specchio C− via α->−α) a 1e-9.

Cross-validazione col codice (check indipendente più forte): `Rao_m.f90:93-100` implementa
LETTERALMENTE {(C) con sorgente, d(A)=0}, e il termine sorgente derivato indipendentemente
δ·sinα·tanα·sinθ·dx/(y·cos(θ+α)) coincide termine per termine con L93-95, incluso il
/(A−B) dell'eliminazione.

Provenienza: **NESSUN doc GENO lo aggiudicava** (grep su GENO/docs per "16.44 | 16-44 |
C2 = | secondo integrale": zero match). Zucrow non lo decide (rimanda a Rao 1958). Derivato
e provato qui; RAO.pdf non è stato necessario.

**[R4 — RETRO-PROPAGAZIONE, nuovo, da portare nei doc di teoria]**: la relazione esatta
`δ·B·sinα·sinθ·(ds/y) = −(dV/V)·[ΛB(A+B) − (A−B)]/A` identifica il **numeratore della
boundary function di GENO come l'ostruzione della sorgente assialsimmetrica per unità di
dV/V**. Ne segue che `boundary_equivalence_derivation.md` §1 / Parte II Passo 4 è la
**riduzione δ=0** (usa la compatibility SOURCE-FREE): corretta per il suo scopo (condizione
PUNTUALE di validità, coerente con `Rao_m.f90:169` "val > 0 <=> valid design region", mai
imposta lungo la curva), ma la formulazione "dalla compatibilità C+" si legge come se
valesse LUNGO DE. Lungo una DE assialsimmetrica, (A)+(C) NON implicano N=0: determinano
ds/y. Classe di rigore: THEOREM* (derivazione simbolica + CAS + probe numerici).

### 7.2 R-2 CHIUSO — workflow wiring completo 14/14 (2026-08-13, resume)

110 call-site verificati puliti; 35 finding grezzi; 8 verificati + critic di completezza.
**IL FINDING PRINCIPALE DELLA CAMPAGNA È QUI, ed è un P0.**

#### MOC-10 [P0 CONFERMATO CON NUMERI] — thrust di parete doppio-contato sugli overshoot
Sede: `CircularContour_m.f90:79-83` (chiamata `thrust_solve` nel ramo j=1) vs `:112-141`
(test di accettazione dell'asse). `thrust_solve` (`Performance_m.f90:64`, `perf%f = perf%f + df`)
è chiamato **PRIMA** del test accept/reject; sul reject la colonna viene scartata ma
**`perf%f` NON viene MAI ripristinato** — non esiste alcun save/restore nella routine.
Ogni tentativo di colonna scartato lascia accumulato il suo pannello di parete completo,
sempre a partire dalla stessa base (`perf%yw = sol%y(1,i-1)`, L48).
Il ramo overshoot scatta praticamente in ogni run (il Mach d'asse attraversa Me a passi da
finiti; centrare |M−Me|<1e-5 per caso è trascurabile).
**Il gemello anulare fa la cosa giusta** (`f_save` a L234, ri-calcolo della spinta di parete
solo sulle colonne sopravvissute in Fase 6, L852-878): la regola era nota.
Corroborazione indipendente: `main.f90:540-545` ha logica dedicata per **saltare le colonne
duplicate** dell'overshoot nell'output geometrico — gli autori sapevano dei duplicati e
hanno de-duplicato la GEOMETRIA lasciando accumulata la SPINTA.

MISURA su output di produzione COMMITTATI (ricostruzione con le formule ESATTE di GENO:
Simpson non-uniforme di `Math_m:585` sui 401 punti Field per la IVL + trapezio `thrust_solve`
sui punti Wall; `perf%f` ancorato a Isp×mdot a 7 cifre, non al CF a 4 decimali):

| caso | F_geno | F_ricostruito | eccesso | rel | eccesso / pannello d'arco |
|---|---|---|---|---|---|
| tocnoz (tipo 2, eps=30) | 1.41150447e+08 | 1.41143176e+08 | **+7.2715e+03 N** | **+5.15e-5** | 1.109 |
| defnoz (tipo 2, eps=30) | 1.37381527e+08 | 1.37358212e+08 | **+2.3315e+04 N** | **+1.70e-4** | 4.92 |

Non è artefatto di arrotondamento: il CF ricostruito cade **FUORI** dalla banda di
arrotondamento del CF stampato, mentre il CF via Isp ci cade dentro.
**L'eccesso si decompone ESATTAMENTE come predice il meccanismo**: tocnoz termina l'arco a
374.1148·da (atterraggio frazionario = la secante ha sparato); pannello pieno 6.5601e+03 N,
pannello frazionario accettato 7.522e+02 N; eccesso osservato = 6.5601e+03 + 7.11e+02
-> `iter = 2` tentativi scartati. defnoz: 463.5687·da, pannello pieno 4.7429e+03,
frazionario 2.6888e+03 -> n ≈ 7, cioè `iter ≈ 8`. Un pannello di sovrappiù per iterazione,
sempre di segno positivo, sempre alla stazione di overshoot.

Propagazione: `perf%f`, `perf%spi`, `perf%etaf`, `perf%etai`, colonne 5/6 di
`performance.dat`. **Tipi colpiti: 0, 1, 2, 3, 4, 6** (tutti quelli che passano da
`throatExpansion_solve`). Magnitudine = iter × pannello d'arco = **O(da): contaminazione al
PRIM'ORDINE di un integrale di parete altrimenti O(da²)** — NON svanisce al raffinamento al
rate dello schema. **Congelato nelle baseline md5** (idealnoz/ticnoz/tocnoz/planarnoz/conicnoz).
Fix già presente nello stesso file: snapshot di `perf%f` a L47 + restore nel ramo flag=1
prima di `cycle outer` (oppure il pattern `f_save` del gemello).

**Finding secondario di doc**: `docs/audit_thrust_planar_axi.md` §3 attribuisce i residui
E8(b) (3.9e-5 idealnoz, 7.2e-5 ticnoz…) a "ordine d'integrazione trapezio vs GENO": sono in
larga parte QUESTO difetto. L'oracolo `scripts/oracle_momentum.py` lo stava già vedendo, ma
ri-integra la IVL con trapezio semplice invece del Simpson di GENO e il segnale finisce nel
rumore di quadratura. Doc che ricicla un bug reale come rumore numerico.

RISERVA DI RIGORE: verdetto di UN verificatore avversario con ricostruzione quantitativa da
output committati (nessuna esecuzione di GENO possibile da qui). Test decisivo a costo ~zero:
snapshot/restore di `perf%f` e ri-run -> il delta atteso è esattamente quello in tabella.

**PERIMETRO DEL DANNO — verificato di prima mano (2026-08-13): CONTABILITÀ, NON ALGORITMO.**
Sweep di ogni lettura di `perf%f` in `GENO/src`: le UNICHE consumazioni sono
`perf%etaf = perf%f/fod` (`Performance_m.f90:65`), `perf%spi = perf%f/perf%mdot` (:67, e
`main.f90:217`), la scrittura di `performance.dat` (`main.f90:809`) e i reset
`perf%f = spinta0` (`main.f90:254, 325, 354`). **Nessun ramo di controllo legge `perf%f`:**
nessun `if`, nessun residuo di convergenza, nessuna bisezione.
Verificato sui loop esterni (letti a `main.f90:246-365`): la secante TIC gira su `ticErr`
(residuo geometrico di `ticNozzleSub_solve`), la bisezione TOC/TOP su `fun = ye − ye_target`
oppure su `constraint_residual` (vincoli geometrici / corner condition sulla curva, che
usano pe, rhoe, Ve, thetae — MAI `perf%f`). Anche il design di Rao massimizza la spinta
**variazionalmente** (condizione boundary val=0), non valutando `perf%f`.
CONSEGUENZE: (i) **contorno, campo MoC, portata e tutte le decisioni di design sono INTATTI**;
(ii) sono sbagliati SOLO i numeri di prestazione (F, CF, Isp, spi, etaf, etai) — che però
sono **numeri di record** usati nei confronti con la letteratura e nell'oracolo E8(b);
(iii) il reset a inizio di ogni passata esterna limita l'errore a **UNA dose** (gli overshoot
della passata finale), non composta sulle iterazioni;
(iv) l'oracolo cross-code **O2 del motore differenziale confronta CONTORNI** (banda di
Richardson sul contorno Rao di GENO), quindi **O2 NON è contaminato**.

#### Altri finding verificati (nuovi)
| ID | Sede | Sev | Claim |
|---|---|---|---|
| MOC-11 | InitialValues_m.f90:193/195 | P1 CONF | `IVLINE_annular_solve` (tipo 9) chiama `simpson_nu` con `cfg%NI`, ma la guardia di parità NI-dispari (`IO_m.f90:568`) **esclude il tipo 9** e non esiste altra guardia: con NI pari il loop `do k=1,n-2,2` di `Math_m` **perde l'ultimo intervallo** -> portata/spinta IVL sbagliate. |
| MOC-12 | Extension_m.f90:41 | P1 CONF | Carica la colonna base del fan come slice grezza `sol%x(1:j2_0,i_col)` **senza compattazione void/Nv**; `Extension_m` non ha alcun parametro Nv, quindi ingerisce le righe void (zeri) del layout TOC come punti fisici. Tipo 6. |
| MOC-13 | CircularContour_m.f90:355, :681 | P1 CONF | **Colonna a backend MISTO silenzioso** nel tipo 9 (Migdal anulare): con `moc_gen=.false.` (esattamente la baseline md5 `migdalnoz_ni50`) i punti di parete inferiore passano comunque dal kernel Ch.17 (`inwall_lower` non ha fallback Ch.16) -> Ch.16 e Ch.17 mescolati dentro la stessa colonna, senza segnalazione. |
| MOC-14 | CircularContour_m.f90:65-78 | P2 | `wall_search`: invariante di terminazione non asserito — nessun bound `Nv+1 <= j2` / `size()` prima di `load_point`. |
| MOC-15 | main.f90:501 | P2 (declassato da P0) | `vacuum_base_performance` integra j=1..n−1 **senza skip delle righe void**, a differenza di ogni altro consumatore di colonna. |

#### Verdetti SPLIT (onestà di record)
Due finding hanno ricevuto verdetti diversi da verificatori diversi (la dedup non li ha
fusi perché i path erano scritti in due forme): **MOC-03** (THROAT_MAXITER) = CONFERMATO P1
da uno, DECLASSATO a P2 dall'altro ("nessun numero sbagliato dimostrato"); **MOC-04**
(chiusura di parete Ch.16 mancante) = CONFERMATO P1 da uno, P2-con-trigger-di-escalation
dall'altro. Lettura conservativa: P2 con condizione di escalation nominata; lettura
aggressiva: P1. Da dirimere con il run strumentato di R-3.

#### Residuo mappato dal critic (non auditato)
1. **Tipo 5 (plug) completamente scoperto**: `PlugNozzle_m.f90` chiama i kernel Ch.17
   DIRETTAMENTE (zero call-site di `MoC_Dispatch_m`) e usa un modello di storage DIVERSO
   (array 1-D `char1/char2/char3` + `jmax`, non `sol(j,i)`/`j2`/`Nv`): **nessuna conclusione
   di questo audit si trasferisce**. Segnalato in particolare l'aliasing a L576/L808 (lo
   stesso attuale `pt3` passato sia come bracket sia come `pt_prev`) — non aggiudicato.
   È un tipo di produzione: **il buco singolo più grande**.
2. `run_toc` azzera in blocco le righe `sol%x(jj+1:j2,:) = 0` (`main.f90:402-403`) **senza
   aggiornare j2**, violando il contratto "j2 settato solo da throatExpansion_solve": ogni
   consumatore a valle legge righe azzerate.

---

## 8. PROSSIMI PASSI PROPOSTI (nessuno eseguito senza ratifica utente)
1. Registrare MOC-01..09 come righe tipizzate nel findings registry (R31) lato programma e
   nel MASTER_PLAN/CHANGELOG lato GENO (i P1 sono difetti GENO, owner GENO).
2. Chiudere R-1 (Rao 1958) e R-2 (resume workflow) nella prossima finestra.
3. Pianificare il run strumentato R-3 con la campagna velocità (aggancio MOC-06).
4. MOC-01/02/03/04 sono **riparazioni a basso costo e alto valore** su GENO (flag di
   mancata convergenza, cap sul loop, error stop coerente col gemello, guardia sul
   no-crossing): candidarle alla finestra GENO, non al programma.

---

## 9. APPENDICE — KERNEL Ch.17: PIEDE DELLA STREAMLINE E STRUTTURA DI
## CONVERGENZA (2026-08-13, verifica agnostica su richiesta utente)

Motivo: la campagna §1-§8 aveva verificato le FORMULE dei kernel Ch.17, NON
la POLITICA del piede né la struttura dei punti fissi. Gap colmato qui.
(Un terzo taglio — caccia avversaria su violazioni monte/valle, asimmetria
clamp/estrapolazione, iterazione interna su theta3 — era ancora in volo alla
scrittura di questa appendice.)

### 9.1 Politica del piede: 3 modalità, scelte dal CHIAMANTE
`inter_solve_gen` è l'UNICO kernel che CERCA un piede. Selettore unico:
`if (present(col))` (MoC_Gen_m.f90:139). Nessuna rilevazione a runtime.
- **B (bracket search)**: scansione parametrica su OGNI segmento della
  poligonale `col`, argmin di distanza da pt4 fra i crossing a monte
  (:153-202); fallback su segmento terminale; **hard clamp** di t + flag
  `foot_clamped`. Mai estrapolazione.
- **G (corda geometrica)**: intersezione con la corda pt5-pt_base (:218-245).
- **D (corda diretta)**: pt5=pt1 => corda = linea dati pt1-pt2 (Zucrow classico).
In G/D: `foot_clamped` forzato .false. (:217) + **snap del piede al vertice
più vicino** quando l'intersezione esce dalla corda (:230-234) = clamp duro
SILENZIOSO, senza equivalente in Zucrow. theta3/p3 sono lerp geometrici;
(rho3,V3) ricostruiti dagli invarianti (s,h0) — fix N-26.
**Il piede è ri-cercato a OGNI passata del PC** (blocco dentro il loop, th0
ri-mediata a :397).

Censimento: 23 siti. La regola monte/valle (2 fattori: marcia diretta/inversa
x riempimento wall->axis/axis->wall) È documentata (sprint_plans/
streamline_foot_rebracket.md, audit_goursat_streamline_ch17.md) ma **vive nei
doc, non nel solver**: nessuna asserzione, nessun commento nei siti critici.
Rispettata in 20/23. **Scarti**: (a) marcia di profilo tipi 0/1/2 — la regola
dice MISTE=>rebracket(B), PASS-1 usa B ma **FASE 1 ri-spazza lo STESSO range
in modo G e sovrascrive tutto**: a convergenza gira G, B è solo bootstrap;
(b) plug Fase 3 passa `col=` (B) dove la regola dice D (i doc ammettono che la
classificazione "concorde" usava convenzione y invertita).

### 9.2 [MOC-16, P1] La rete di sicurezza dei punti clampati è CODICE MORTO
FASE 1 gira in modo G, che forza `foot_clamped=.false.` incondizionatamente
(MoC_Gen_m:217) => `foot_was_clamped(j)` azzerato per tutto il range
(Profile_m:469) **prima che qualcuno lo legga**. `correct_clamped_points`
(Profile_m:525-550, FASE 2) **non esegue mai il proprio corpo**, in nessuna
iterazione. Il rilevatore di clamp è vivo solo in PASS-1, dove nessuno lo
consuma. Rete di sicurezza scritta e scollegata.

### 9.3 [MOC-17, P1 sistemico] METÀ di MoC_Gen_m.f90 è morta — ed è la metà rigorosa
Zero chiamanti (grep su tutto src/ e test/): `wall_refine_gen` (:1186-1296,
Newton FD + backtracking, tol derivate sqrt(eps)/10eps, cap LOUD),
`evaluate_theta`, `wall_inner_pc` (cap 100 LOUD), `streamline_state_from_p`,
**`isentropic_bernoulli_adaptive` + `integrate_N` (:1541-1607, Richardson
halving, TOL=sqrt(eps), cap LOUD)**, `characteristic_mdot_scale`,
`mdot_cm_to_wall`. Il ritiro di `wall_refine_gen` è dichiarato
(Profile_m:239-254, verdetto A2); la conseguenza NON dichiarata è che sono
morte **le uniche implementazioni con cap rumorosi e tolleranze derivate**.
In particolare `isentropic_bernoulli_adaptive` è il metodo che GENO/CLAUDE.md
rende OBBLIGATORIO ("Sub-stepping = Richardson halving, MAI `ceiling(|dp/p|/
0.1)`") — e il path VIVO usa esattamente `ceiling(dp_ratio/0.1)` (:276, :340).

### 9.4 [MOC-18, P1] Cap silenzioso su TUTTI E 7 i kernel Ch.17 vivi
`inter_`, `axis_`, `inwall_`, `inwall_lower_`, `stream_`, `jet_`,
`jet_cminus_`: `do iter = 0, cfg%icor` e fine subroutine. Nessun flag, nessun
`write`, nessun argomento `converged`; il chiamante NON può distinguere una
passata convergente da 21 divergenti.
**CORREZIONE al §4 (MOC-01)**: il criterio MAL POSTO (RHS firmato) è Ch.16-only,
ma **l'uscita silenziosa al cap è UNIVERSALE**, Ch.17 incluso. Le 4
implementazioni conformi a "zero silent exit" nello stesso file sono TUTTE nel
ramo morto (§9.3).

### 9.5 Punto fisso di `inter_solve_gen`: ben posto A RAMI, non globalmente
Stato z = (x4,y4,p4,theta4,rho4,V4,theta0_bar) in R^7. **La posizione del piede
NON è nello stato**: (k_seg,t_foot) è ricalcolata da zero a ogni passata come
funzione a valori DISCRETI di z; la memoria del piede vive in theta0_bar.
**A punto fisso, ramo regolare: sistema algebrico 7x7 che È esattamente lo
schema Zucrow §17-4 a proprietà medie** (C- e C+ geometriche, 17.51/17.52,
isentropa + Bernoulli trapezoidale, geometria del piede). RISULTATO POSITIVO.
Ma G è definita a pezzi su **4 partizioni**: `axis_mode` (:132, confronto
floating-point ESATTO `y4==0.0`), `k_seg` (argmin), clamp/snap del piede
(:202, :230-234), `N_sub` (:340).
Deviazioni da Zucrow, tutte a valle del piede: (D1) dominio del piede =
poligonale intera invece della base fissa pt1-pt2 (motivata: fix N-26, colonne
TOC con dx/dy~4); (D2) stato del piede da invarianti invece che lerp (motivata);
(D3) **snap del piede (:230-234) = clamp duro dentro il loop di punto fisso,
senza equivalente in Zucrow — ed è il ramo usato da TUTTO il riempimento kgrid**.

### 9.6 [MOC-19, P1] Il criterio d'uscita sorveglia 2 componenti su 7
`errP` (su p) e `errV` (su V) relativi; NON sorvegliati: theta4, x4, y4,
theta0_bar, (k_seg,t_foot). In regime regolare NON è un buco (l'errore
relativo di posizione è ~1e-4 volte quello di p: margine ~7e3). Lo diventa in
4 casi derivati:
(i) **`p4` è CIECO al piede per costruzione** (:320 dipende solo dalle
    mean-state acustiche): un salto di `k_seg` all'ultima passata non tocca
    `errP` e si manifesta su `errV` solo al second'ordine => uscita con piede
    appena migrato e mai riconfermato.
(ii) **clamp `V_sq<=0` (:365)** => V4=0 => alla passata dopo `errV` = Inf
    (q>0) o NaN (q=0) => **il criterio non può MAI scattare** => 21 passate =>
    uscita silenziosa con q=0, M=0: stato non fisico ma **FINITO** (nessun
    NaN). CircularContour:464 lo intercetta (`G-PHYS`) ma **solo nel kgrid**;
    il guard di Profile_m:466-467 testa **solo NaN, non la positività** => nel
    path profilo passa inosservato e finisce nell'integrale di massa e nella
    parete. **Riparazione a costo zero: aggiungere `.not.(q>0)` al guard.**
(iii) **toggle `axis_mode`**: se una passata dà y4<0 (clampato => ramo asse,
    theta4:=0, 4 equazioni) e la successiva y4=+1e-15 (ramo interno, 7
    equazioni), G non è una mappa ma un **sistema commutato**: un ciclo di
    periodo 2 non ha punto fisso; uscita al cap col ramo che capita per ultimo.
(iv) jet_solve / jet_solve_cminus: p prescritta => **si sorveglia solo errV**;
    theta4, che è l'output fisicamente primario (direzione della frontiera del
    getto), **non è mai testata**.

### 9.7 Contrazione: regime nominale sano, due regimi di rottura nominati
Derivazione: rho_contr ~ 1/2 [ c_Q (dp/p)_cella + c_S h/y_bar ], c_Q ~ M²/(M²-1).
Griglia di produzione (NI=401, dp/p~1e-3..1e-2, M~2-4): **rho ~ 6e-4..7e-3 =>
2-4 passate** per 1e-8 (coerente con Zucrow "<=2 corrector"; icor=20 dà 5-10x
di margine). **Il degrado 1/y vicino all'asse NON è un breaker** (y_bar >= y1/2
sempre => h/y_bar <= 2 => ~8 passate, sotto il cap); il fallimento vicino
all'asse è il TOGGLE DI RAMO (§9.6-iii), non un degrado continuo.
**Breaker vero: M->1.** Condizione di contrazione `M-1 >~ (1/4)(dp/p)`; al
floor `M_FLOOR=1+1e-6`: c_Q ~ 5e5 => **rho ~ 250 >> 1: punto fisso REPULSIVO**,
l'iterazione diverge ed esce al cap in silenzio. Inoltre `MM = max(V/a,
M_FLOOR)` (:114) **rende supersonico un dato subsonico senza segnalarlo**.
gamma(T) NON degrada la contrazione, ma i backend danno gamma C^0 con ginocchi
(FLINT: interpolazione lineare su nodi interi in K) => nessuna accelerazione
superlineare lecita; e in `solve_T_from_entropy` la derivata usata (cp/T) NON è
la derivata dell's interpolato => Newton degrada a lineare (assorbito da rtsafe).
Nota: `solve_T_from_entropy` MAX_IT=53 ha **margine 1.05x** sul path di sola
bisezione => un bracket più largo esaurisce il budget e l'error stop diagnostica
male ("check s0 continuity" invece di "budget di bisezione").

### 9.8 [MOC-20, P1] L'inversione di tolleranza vera è GRADINO-vs-tolleranza
`N_sub = ceiling(|dp/p3|/0.1)` cambia fra passate del PC (p4 cambia; p3 cambia
perché il piede si muove) => **G discontinua a tratti**. Ampiezza del salto,
derivata: le N³ si cancellano => **dV/V ~ 5.3e-5, INDIPENDENTE da N** e pari a
**5e3 volte tol_conv**.
Oscillazione di periodo 2 (nessun punto fisso): richiede che r* cada in una
finestra di ampiezza relativa ~3e-6 attorno a 0.1n. **Su griglia di produzione
NI=401 NON è raggiungibile** (dp/p~1e-3 => N_sub==1, partizione singola,
patologia INATTIVA). Nei regimi a forte espansione (spigolo di gola, kernel
anulare con da grossolano, migdal a NI basso) è attesa in ~3 celle su 1e6.
**CONSEGUENZA PIÙ GRAVE, indipendente dall'oscillazione**: anche a branch
stabile G è discontinua con salto 5.3e-5. Ogni metodo esterno che DIFFERENZIA
attraverso `inter_solve_gen` — Broyden FD di `refine_K` (tol 1e-5), secante su
Me di `throatExpansion_solve` (tol 1e-5), bisezioni Mrao/xsol — ha un **floor
di rumore ~5e-5, CINQUE VOLTE più lasco della propria tolleranza d'uscita**.
Il commento CircularContour:735-741 riconosce che 1e-5 non è derivata, ma
attribuisce il limite al condizionamento FD: la causa vera è che **il residuo
non è continuo a livello 1e-5**.

### 9.9 Kernel Goursat anulare: due risultati POSITIVI verificati
(a) **Riempimento ACICLICO, verificato blocco per blocco**: dipendenza
(i_U,i_L) <- (i_U,i_L-1) U (i_U-1,i_L) = ordine parziale stretto sul reticolo
=> DAG per costruzione; i tre blocchi incrementali (new x old, old x new,
new x new) sono stati tracciati uno per uno e ogni lettura risulta già
calcolata. Nessuna iterazione di griglia; fill deterministico (poison
`kgrid%q=-1` dopo re-espansione: nessuno stato stantio).
(b) **Il ricalcolo parziale del Broyden È ESATTAMENTE il cono d'influenza**:
perturbare wa_cm tocca solo la riga i_U*, wa_cp solo la colonna i_L*; il codice
ricalcola colonna i_L* poi riga i_U*, e la cella letta a :719 non è nel cono di
nessuna delle due => correttamente invariata, non stantia. **Punto di progetto
corretto, da registrare come tale.**
(c) Anche la **trappola clamp+Broyden** di GENO/CLAUDE.md è correttamente
EVITATA: f_cm,f_cp frazionali senza alcun clamp = la riparametrizzazione
prescritta.
MA: il riempimento kgrid usa il ramo **senza `col`** => quello con lo snap duro
del piede (§9.1); e non esiste alcun commento né asserzione che giustifichi
quale indice porti la C- e quale la C+ (§(b) del censimento).

### 9.10 [MOC-21, P1] Il residuo del Broyden è a gradini SOPRA la sua tolleranza
5 sorgenti di discontinuità in F(f_cm,f_cp): G1 `Nv` incrementato da una soglia
su f (delta_M ~ 1e-3); G2 clamp d'indice su pt5; G3 `if (j<=Nv) cycle`; G4 snap
del piede; G5 branch N_sub (5.3e-5). **G1 e G5 sono ENTRAMBI maggiori della
tolleranza d'uscita 1e-5**: se la radice cade fra due gradini il test non può
essere soddisfatto => 30 iterazioni => error stop (RUMOROSO, quindi non un
falso zero silenzioso) ma con **attribuzione errata** ("focus K unpinned"
invece di "residuo a gradini").
Debolezze residue: **F è una funzione PARZIALE** (error stop a :636/:690 dentro
il dominio) e Broyden non ha line search né trust region => un passo nella
regione di indefinitezza **aborta il programma** invece di rifiutare il residuo
(il pattern corretto `f_res=huge`+backtracking esiste... nel ramo MORTO); e il
seed di J è una secante su passo delta_f=1, che se attraversa un flip di Nv
misura la pendenza del GRADINO invece che della funzione.

### 9.11 Verdetti di caratterizzazione (i)/(ii)/(iii)
(i) ben posto e convergente · (ii) ben posto, convergenza non garantita in
regimi nominati · (iii) non caratterizzato (decisioni discrete dentro iterazioni
continue).

| Procedura | Verdetto |
|---|---|
| `inter_solve_gen` | **(iii)** — 4 partizioni discrete; ramo per ramo è (ii) col sistema 7x7 di Zucrow |
| `axis_solve_gen` | (ii) — liscia; `yax` congelato elimina la sensibilità 1/y; diverge per M-1 <~ (1/4)(dp/p) |
| `inwall_solve_gen` / `_lower_` | (ii) — frac NON clampata; regime nominato `slope_seg-lP -> 0` => frac -> ±inf, stato estrapolato non fisico; unica guardia = soglia ASSOLUTA 1e-30 |
| `stream_solve_gen` | (ii) |
| `jet_solve` / `_cminus` | (ii) con buco esplicito: theta4 mai testata |
| `foot_state_from_invariants` -> `solve_T_from_entropy` | **(i)** con caveat (monotonia stretta, bracket verificato, cap RUMOROSO; margine 1.05x su MAX_IT) |
| `iterate_column_moc_gen` | **(iii)** — iterata MISTA (R^2n, Z, B): il criterio richiede simultaneamente Cauchy continuo E punto fisso INTERO (`Nv_new` da argmax discreto); nessuna teoria garantisce il secondo; rho~0.955 documentata su migdal |
| `throatExpansion_solve` | **(iii)** — il peggiore: wall_search SENZA BOUND; accettazione silenziosa; **target Me riscritto**; reset di stato discreto dentro la secante |
| `throatExpansionShrouded_solve` | **(i)** per la parte discreta — cap tutti rumorosi, Goursat DAG verificato |
| `refine_K` (Broyden) | **(iii)** — residuo deterministico e cono esatto (positivi), ma a gradini sopra tolleranza; F parziale senza line search |

### 9.12 Test empirici nominati (chiudibili solo con run strumentato su s3)
T1 censimento dei cap silenziosi (arg opzionale `iters` sui 7 kernel; rigettore:
con icor=2 il conteggio deve esplodere, con tol=1e-3 azzerarsi) · T2
completezza del criterio (istogramma di errTh/errX/errY/delta k_seg) · T3 misura
della contrazione vs M e vs y/h (predizione falsificabile: ginocchio a
M-1 ~ (1/4)(dp/p)) · T4 rilevatore di flip N_sub (predizione: floor 5e-5) ·
**T4-bis autopsia della quadratura adattiva** (ri-cablare la morta
`isentropic_bernoulli_adaptive` con print dello stato a MAX_REFINE: chiude il
"fail non diagnosticato" di GENO/CLAUDE.md; ipotesi = p_b<0 / T fuori tabella,
non budget di halving) · T5 toggle axis_mode (qualunque conteggio non nullo
prova il sistema commutato) · T6 scansione del residuo Broyden · T7 aciclicità
kgrid · T8 ciclo dell'indice di massa · **T9 laundering del clamp V²<=0**
(+ riparazione del guard Profile_m:466) · T10 estrapolazione di parete
(falsificatore |frac|>2) · T11 budget di bisezione (falsificatore max(it)>45) ·
**T12 accettazione silenziosa alla gola** (falsificatore: una sola uscita con
iter>30 = Me di design riscritto da un'iterazione non conversa).

### 9.13 Marciume documentale rilevato (doc che descrivono codice inesistente)
- `wall_refine_gen` presentato come FASE 4 in `audit_goursat_streamline_ch17.md`
  §4/§5.3/§6 e nel docstring di `idealNozzleSub_solve`: ha **zero call-site**.
- Modulo `DirectPlug_m` a cui `streamline_foot_rebracket.md` §4 prescrive fix su
  4 siti: **non esiste in src/lib/**. Il suo "reference pattern"
  (`PlugNozzle_m.f90:585-597`, loop `MAX_REBRACKET`) non esiste più.
- `theory_MoC_stencil.md` descrive solo 2 regimi (il modo B è **assente**),
  afferma che `inwall_solve_gen` non interpola su segmento (lo fa, :563-574), e
  cita uno snippet che non esiste nel sorgente; §8.5 dichiara l'estrapolazione
  `frac3>1` "fisicamente corretta" mentre `inter_solve_gen` clampa o snappa.
- `PlugNozzle_m.f90:575`: ammissione in-code che la Fase 1 non ha il
  `wall_search` che entrambi i siti di parete di CircularContour_m hanno.

### 9.14 Caccia avversaria sulla politica del piede (terzo taglio, atterrato)

**Tesi "la politica del piede è unica e coerente": RIFIUTATA** — coesistono TRE
politiche selezionate implicitamente dalla PRESENZA di argomenti opzionali, con
la doc di record disallineata dal codice spedito.

#### ASSOLUZIONI (importanti quanto i difetti)
- **A1 monte/valle: NESSUN DIFETTO.** In OGNI sito con `pt5=pt1`, pt1 è il
  vicino backward sulla colonna corrente e pt2 quello sulla precedente; poiché
  per M>1 vale theta-alpha < theta < theta+alpha, la streamline all'indietro
  giace STRETTAMENTE dentro il cono di Mach delimitato da C-(pt1) e C+(pt2):
  **il piede cade dentro pt1-pt2 per teorema, non per fortuna**. Il sospetto
  principale (kgrid, due fan diversi) **NON REGGE**: le due famiglie vengono da
  lip diversi solo sulle GAMBE, non nella cella (pt1,pt2 sono i due vicini
  backward nei due indici caratteristici = rete di Goursat pura).
  MA la conformità **non è applicata da nulla** (nessuna asserzione runtime) ed
  è ACCIDENTALE rispetto alla doc: `streamline_foot_rebracket.md` §3.3 elenca 9
  siti "DA FIXARE" prescrivendo pt5 e pb ENTRAMBI sulla colonna precedente,
  mentre il codice spedito mette pt5 sulla colonna CORRENTE.
- **A3 invariante pt1/pt2 fissi: RISPETTATO** (tutti `intent(in)`; le medie del
  corrector usano solo pt1,pt2,pt4). La trappola documentata è oggi INFIRABILE
  perché il loop di rebracket non esiste più.
- **A3-iv lag di pt5: la tesi del codice REGGE** — a convergenza il sistema
  risolto è implicito e accoppiato sulla colonna, la soluzione non dipende
  dall'ordinamento (Gauss-Seidel vs Jacobi cambiano solo il cammino).
- **A4 lerp nei piedi CARATTERISTICI: NON è la classe N-26.** N-26 era grave
  perché (rho3,V3) del piede STREAMLINE è la condizione iniziale
  dell'integrazione lungo streamline => il bias di corda si ACCUMULA lungo la
  marcia (deficit di massa 9e-4). Il piede caratteristico entra solo nella
  compat acustica e nelle medie del corrector: errore LOCALE, stesso ordine
  dello schema, non accumulativo. Nessun sito fa alimentare un'integrazione
  lungo streamline da un piede interpolato con lerp.
- **A6 nessuna perdita d'ordine**: GENO fonde la rilocalizzazione del piede
  nella passata del PC esterno invece dell'iterazione annidata del libro; se il
  PC fuso converge il punto fisso è LO STESSO.

#### DIFETTI NUOVI CONFERMATI
| ID | Sede | Sev | Claim |
|---|---|---|---|
| MOC-22 | MoC_Gen_m.f90:563-564, 695-696, 837-838 | **P1** | La guardia di **segmento verticale** esiste in `inter_solve_gen` (:218) ma **manca nelle 3 routine gemelle** che usano la STESSA formula (inwall upper/lower, stream). La guardia presente protegge solo dal punto coincidente, non da dx=0 con dy!=0: `slope_seg=±Inf` => `x2 = Inf/Inf` = **NaN** => frac, rho2, V2, th2, p2, pt4 tutti NaN. Raggiungibile per theta±alpha -> pi/2 (lip plug fortemente deviato). Stessa esposizione su lP/lM infiniti (il guard `huge()` esiste solo in `inter_solve_gen`). |
| MOC-23 | MoC_Gen_m.f90:562/601/616 + Types_thermo_sm.f90:195-229, 282 | **P1** | **La catena NaN è SILENZIOSA fino all'uscita del PC**: `NaN < tol` è .false. => il loop non esce mai per convergenza, esaurisce icor e **ritorna normalmente con pt4 NaN**. Il guard `if (y<0) error stop` è NaN-permeabile (`NaN<0` = false). Inoltre la thermo NASA valuta il polinomio **senza alcun controllo di range**: con T<0 (da rho<0) ritorna un cp finito spazzatura e `gam=cp/(cp-Rg)` può dividere per ~0. |
| MOC-24 | MoC_Gen_m.f90:177-184 | **P1** | **La root cause di N-26 è ANCORA VIVA nel path di fallback.** Il commento :146-150 descrive il difetto storico (proiezione a `col(1)%x` -> fallback all'estremo OPPOSTO al piede vero -> th0 dal lato sbagliato -> rotazione uniforme della colonna -> deficit di massa 9e-4) e poi il ramo `k_seg==0` esegue **LA STESSA PROIEZIONE** (`y_foot = pt4%y + tan(th0)*(col(1)%x - pt4%x)`), declassata a "tie-break". **Non è un tie-break**: sceglie a quale estremo della linea dati clampare il piede — esattamente la decisione diagnosticata come sbagliata — e il ramo si prende PRECISAMENTE quando il piede esce dalla poligonale, cioè la situazione in cui N-26 si manifestava. |
| MOC-25 | CircularContour_m.f90:407-416 | **P1** | **`kgrid(0,0)` scritto DUE volte** (una per gamba) e il secondo valore **sovrascrive il primo senza alcun confronto**. La cella d'angolo `kgrid(1,1)` prende poi pt1 dal ramo cm e pt2 dal ramo cp e interpola il piede sul segmento fra le due gambe. Nel caso single-kernel i due valori risalgono allo stesso punto e sono plausibilmente bit-identici; **dopo un re-anchor** (col_base_cm/cp saltano alla colonna far-corner) **nulla garantisce la coincidenza**. Il commento :455 nomina esplicitamente "seam incoherence" e la guardia G-PHYS esiste per intercettarne l'esito: il fenomeno **è già stato osservato**. Entità del salto = NON DECIDIBILE staticamente (decisore: stampare la differenza prima della sovrascrittura, con re-expansion attiva). |
| MOC-26 | PlugNozzle_m.f90:472-521, 589, 827 | **P1** | `interp_char` (densificazione G7 fra Fase 1 e Fase 2) **lerpa x,y,rho,q,theta,p,T,c,M,gam TUTTI indipendentemente** => `char1` contiene punti con `T != p/(Rg rho)`, `c != sqrt(gam p/rho)`, `M != q/c`: stato **termodinamicamente inconsistente**. Quel `char1` è poi la linea dati di Fase 2/3, l'array `col` su cui gira lo scan del piede, E la sorgente di (s_a,h0_a) per `foot_state_from_invariants`: **la garanzia on-manifold di N-26 è distrutta ALLA SORGENTE**. A registro come N-39/N-63 APERTO; la motivazione lì data ("latente perché thermo_plug ha gamma costante") **sottostima**: il bias di corda su rho(p) ~ p^(1/gamma) è non-lineare **anche a gamma costante** — è esattamente l'argomento di N-26. |
| MOC-27 | MASTER_PLAN.md:345, :423 (registro GENO) | **P1 epistemico** | **Il ramo cross-stream della ricostruzione da invarianti NON È MAI STATO ESERCITATO**: il registro GENO stesso dichiara che `t*(s_b-s_a)` (MoC_Gen:1834) è "MAI esercitato" e che N-26 è "dimostrato omentropico / **ASSERITO-non-validato rotazionale**". La riparazione del piede è validata **solo nel caso in cui coincide con il lerp banale**. |
| MOC-28 | MoC_Gen_m.f90:164 vs :216-246 | **P1 se attivo** | Il ramo `col` **esclude esplicitamente il piede a valle** (`if (x3_try > pt4%x) cycle`); il ramo pt5-pb — **quello che produce il risultato converso in produzione** (§9.1) — **non ha quel test**: accetta x3 ovunque cada, incluso a valle. Asimmetria indiscutibile; se sia mai attiva NON è decidibile staticamente. Decisore: contatore `x3 - pt4%x > 0` per fase. |

#### Difetti P2 aggiuntivi
`G_lo*G_hi >= 0` **fail-open su NaN** (MoC_Gen:1649: `NaN >= 0` è false => la
guardia passa, rtsafe itera 53 volte su NaN e l'error stop diagnostica
"check s0 continuity" — causa vera a monte) · clamp lato **asse** mai segnalato
(:200-202: solo il lato parete è strumentato) · convergenza di colonna dichiarata
su un **sottoinsieme stretto** dello stato che itera (Profile_m:217-219 itera
[Nv_in+1, j2-1] ma :373-377 testa [Nv_new+1, j2-1], e solo su x,y non su
p/rho/q/theta; le righe non testate sono lette come pt5) · `pt5=wall` gated su
`Nv_in` invece di `Nv_new` (Profile_m:439-443: con Nv_new>Nv_in il caso speciale
scatta alla riga sbagliata e la prima riga fisica riceve un pt5 extra-dominio;
la semantica dichiarata a :417 è **falsa** appena Nv_new>Nv_in) · `frac3`
calcolata **solo sulla proiezione y** con soglia **assoluta** 1e-30 e fallback
0.5 **muto** (:235-239; il ramo `col` usa il t parametrico esatto: asimmetria
non giustificata; a registro come A3-W2b "progettato", non fatto) ·
**argomenti morti con rationale FALSO** (PlugNozzle:820-827 giustifica in
dettaglio la scelta di `pt_base` in una chiamata che passa anche `col`, e con
`col` presente il dispatch **ignora sia pt5 sia pt_base**: segnale forte che il
comportamento reale di quei siti non è mai stato verificato) · Extension usa
`inter_dispatch` mentre il DAG di GENO/CLAUDE.md afferma che **bypassa** il
dispatch, e non esiste gemello `_gen` in CTest: con moc_gen=.true. il sito :307
entra nel kernel Ch.17 **senza copertura**.

#### Nota metodologica di record
Il registro GENO classifica l'asimmetria `foot_clamped` (N-12) come
"cosm — **provato inerte**: FASE1 lagged resetta i flag prima di FASE2".
**L'argomento è CIRCOLARE**: il flag è inerte PERCHÉ viene azzerato, e
l'azzeramento è giustificato dall'affermazione che il clamp non può scattare.
Un clamp reale nel ramo pt5-pb **non è oggi osservabile da nessuna parte**.

FINE ADVISORY.
