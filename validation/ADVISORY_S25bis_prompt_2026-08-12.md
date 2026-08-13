# PROMPT SESSIONE S25-bis (censimento R30) — scritto alla chiusura S25
# (pattern ADR untracked; copia verbatim per l'apertura)

Sei nel repo rde-lecture-code, branch rde-nozzle-program. HEAD atteso:
0a01701 ([F-SERVICE/S25][PIANO/R3] S25 closure) — se esiste un
micro-commit successivo "post-closure addendum S25" (convergenza
review pipeline + repairs gap-map), e' MIO e atteso: leggilo e
prosegui; qualsiasi altro commit non tuo = FERMATI e riconcilia.
GENO/ = repo indipendente (HEAD atteso fca273a), MAI committato da
qui. UNA SOLA SESSIONE ALLA VOLTA; protocollo commit rafforzato (git
log -3 + status prima, path-limitati, audit hunk dopo); lint (xv) e
suite GATED SULL'EXIT CODE, redirect-only, MAI pipe; FREEZE degli
edit sui file tracciati mentre un consumer gira (lezione S25: due
collisioni mid-edit dichiarate); misure solo a host pulito
(pycount = 1 nel bench, strumento riparato).

QUESTA SESSIONE E' LA S25-bis — "M5c + M6 + PROTEZIONE CAP" (il
completamento nominato della sessione velocita'; 1 sessione; cap 3 h
di run decisivi; STOP-WHEN-MET al pessimistic-end sui MEASURE).
Stato d'ingresso: S25 CHIUSA (C4 chiusa; M0-M5a/b accettate con
tripla prova; record 100.84->32.09 s, val_grad 6.42->0.98 s, replay
0.66 s, K_NEWT derivato = 2; suite piena 347 s). CONTATORE ONESTO:
segmento ~46 s vs <=30 NOT-MET senza M5c; campagna ~18-23 min
MET-central. Baseline di accettazione = gli artifacts [X-SPDB]
COMMITTATI (s25_spdb_m0/mc.json) — niente re-baseline se pycount e
l'host reggono; M-D/M-E si misurano col bench committato (modi
md/me).

(1) APERTURA (letture OBBLIGATORIE): memorie s25-engine-speed,
pipeline-sense-expert-review (incl. 3-bis CONVERGENZA OBBLIGATORIA),
orchestration-weight-sota, choice-adjudication-convergence,
never-postpone-resolvables, agentic-orchestration-forms;
validation/PROGRESS_2026-08-12_S25_speed.md (log completo S25);
PROGRESS ORA + CENSIMENTO DELTA S25 (R28/R29/R30 + BLOCCATO 8);
DISPATCH_Sspeed_to_S25 + ADVISORY_engine_speed_audit §4 M5/M6 + §6
(ordini vincolanti; vincoli (1)-(7) verbatim); poi il PACCHETTO
CONVERGENZA REVIEW (landing rules — verificare SU DISCO, mai
sull'assenza di notifiche):
 (a) ADVISORY_S25_pipeline_sense_math_2026-08-12.md +
     ADVISORY_S25_pipeline_impl_fidelity_2026-08-12.md (review
     one-pass) + le refutazioni
     sota_gapmap_raws_2026-08-12/s25_refute_pipeline_math.md e
     s25_refute_pipeline_impl.md + **il VERDETTO CONVERGIUTO
     ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md** (judge
     fuso lanciato nella finestra post-chiusura S25): se e' su
     disco, LEGGERLO e assorbire le righe per-claim (adottate /
     refutate / OPEN-with-owner); se NON e' atterrato, eseguire il
     judge all'apertura (UN solo agente sulle due coppie, agenda
     stretta gia' scritta nelle tabelle di convergenza dei refuter;
     poi check Form-3 leggero inline). Oggetto principale gia'
     accertato dai refuter: lo "sliver theta_1" e' un RE-MINT della
     riga audit variational-driver:objective-omits-throat-panel
     (CONFIRMED 2026-08-07) con MAGNITUDINE CONTRADDETTA (audit
     O(1e3) J-units vs "sotto banda" dell'esperto; formula chiusa
     del refuter impl Delta_J ~ pi*p_t*yt*rtd*theta1^2) — il
     verdetto del judge su disposizione+magnitudine+owner governa.
 (b) STATO REPAIRS (gia' ESEGUITE nella finestra post-chiusura S25,
     verificare l'etichetta [S25-REPAIR] nel gap-map + il
     micro-commit "post-closure addendum"): red-team
     s25_redteam_gapmap_judge.md = ABSORB-WITH-REPAIRS 2H/3M/4L ->
     7/7 repairs APPLICATE in-document (AC10, GAP-18/N6 +
     [P-FLIPMAT] de-registrato, ricount ledger 5+3-misti/12/25
     anche in PROGRESS R25, C4 survey-decision, Q11); micro-repair
     refuter F3/F6/F8/F11 APPLICATI al sorgente + R6 portata alla
     FORMULA ESATTA (fr/i, guardia i=0) con gate THC1 re-run EXIT 0.
     Se manca il micro-commit, il working tree le contiene:
     committarle come prima azione (path-limitato).

(2) GATE di pre-esecuzione (R5): ogni cambio di versione (M5c, M6)
DICHIARATO e gated su KAT + O3.1 re-pass; ogni carrier toccato =
gate re-run + pass re-date nel registro (staleness attiva); tripla
prova per leva (gate eseguibile + refuter sul diff + sense-review
PERIMETRATA al tocco — non whole-pipeline); peso orchestrazione
right-sized (memoria orchestration-weight-sota). Poi i duty:

T1 [ASSORBIMENTI — prima di ogni edit algoritmico]: chiudere (1a-c)
con verdetti per-claim (adottata / refutata-con-evidenza /
aperta-con-owner); il carrier R2 (ceiling marcia ideale alla stessa
(eps, thermo) -> Verdict (valore, delta)) se ADOTTATO diventa riga
F2-entry nominata, NON si costruisce qui salvo ordine utente.

T2 [M5c — IL CENTERPIECE]: executor per-colonna F6-AMENDED
(advisory M5c verbatim: hoisted, module-level, jit per-colonna su
shape BUCKETED PADDED in stile plan-as-args; seeds in-trace;
(z, cert_step, cert_scale, margin) come stack per-cella,
host-checked con STESSO bound e STESSA semantica FAIL; Python tiene
OGNI decisione adattiva a granularita' di colonna; discard
sub-crossing MAI nel piano; bucketing = quello del replay [V1b];
eager cell_scan RESTA REJECTED). GATE (puo' RIGETTARE): dec-vector
IDENTITA' BITWISE + z nella banda floor-Newton + plan bit-identity
su twin E defnoz-mild; QUALSIASI differenza di piano = REJECT ->
fallback H2 (>=1.86x misurato) -> shortfall -> N1 (mai debugging
illimitato; cost cap 1 sessione QUI dentro). Controlli: doctored
cell spara al (column,row) giusto; coppia near-seam con STESSO flip
su entrambi i recorder; legacy Python record dietro env flag
(arbitration). MEASURE M-D = STOP CHECK 1 (bench md; pessimistic-end;
target segmento <= 30 s).

T3 [M6 — vmap-Hessiano]: jit(vmap(value_and_grad)) su (n+1, n) FD
rows + blocco Jacobi 2n (M4 prerequisito GIA' dentro); NON bitwise
(floor-order) => version change dichiarato, KAT + O3.1 re-pass;
fallback sequenziale su lane nonfinita + counter (REQ-NONSTALL);
accettazione: per-lane vmap == sequenziale al floor + controllo
lane corrotta + blocco <= 8 s a defnoz. MEASURE M-E = STOP CHECK 2.
STOP-WHEN-MET: raggiunto il target, gli item di sola velocita'
restanti NON si implementano; H3/H4 comunque (sotto).

T4 [H3+H4 — VINCOLANTI PRIMA DI OGNI CAMPAGNA DECISIVA]: H3
campaign rung-boundary dedup (C3 repeat riusa st_new come st_cur;
run_trsqp ritorna l'ultimo (out, plan) certificato + accetta
preplan=; stesso fix in margin_governor; ~3 file) + H4
tail-to-derive & persistenza stage con chiave CODE-IDENTITY (load
stale = REFUSE forte; il C5 S24 replayed come controllo di
accettazione; F3/F7 references = numeri pre-registrati del derive).
Gate: bitwise sul riuso + controlli di M1 condivisi.

T5 [RIGOR/cheap, in-window se il budget regge]: GAP-29 sweep
halved-constants (AUDIT:426) + notaknot-twin (GAP-5,
rejector-formed: banda GENO NON si muove) + R28 numeric-lint esteso
a validation/ (attenzione volume: allowlist per i letterali
derivati-nel-commento) + [P-TRFLOOR] SE esiste il primo artifact di
campagna post-8761dce (altrimenti resta blocked-with-named-cause).

T5-bis [R31 FINDINGS-AS-CODE — direttiva utente, se il budget non
regge diventa LA prima duty della sessione successiva, mai
generico]: docs/findings_registry.yaml gemello del claims registry
(schema: id-slug, status CONFIRMED/DOWNGRADED/REFUTED/DISCHARGED/
SUPERSEDED, severita', magnitudine-di-record, doc#anchor,
owner+trigger, chiavi dedup file:line + tag meccanismo) + lint
macchina con rejector seminati (anchor risolti; OPEN => owner;
DISCHARGED => evidenza; advisory nuovi DEVONO registrare le righe;
DUE OPEN sullo stesso span file:line = violazione) + seeding dal
corpus con find->verify bounded (audit 94, gap-map 36/16/10, ledger
45, refuter/red-team S25). Caso dimostrativo del perche' (da citare
nel doc): il re-mint dello sliver throat-panel (audit CONFIRMED
2026-08-07, ri-coniato S25 con magnitudine contraddetta, beccato
solo dalla clausola dedup del refuter). Peso orchestrazione
right-sized (estrazione meccanica = effort basso).

T6 [CHIUSURA R3]: contatore finale "S25-bis speed: segmento
MET/NOT-MET (M-D), campagna MET/NOT-MET (M-E/proiezione §5)";
sweep INCREMENTALE censimento (R30 consumata/stato, R28, R25
riparata, R29 = prima convergenza completata); PROGRESS/D6; memoria
s25bis; NEXT = F2 GENERAL ENGINE apertura (contatore "F2 session
m/6", C6 pre-entry, G6 da F2a, F2a assorbe mean_swirl, U3', righe
F2-entry nuove: R2-ceiling se adottato, GAP-1/GAP-2 surrogato KS +
B-stationarity, IP-adjudication [P-IPADJ]).

TERMS: verdetti S14-S25 NON si rilitigano; PIN P1/P2/P3; R5 numeri
solo da carrier committati; R4 stessa sessione; env numpy 2.5.1 /
jax 0.11 / scipy 1.18; BLOCCATO 8 = decisione utente sulla dep
`filelock` per il cap LRU cache (chiedere SOLO se serve il cap in
sessione, altrimenti resta conditional); tasklist mai kill -0;
workflow/agent verificati sul transcript dir; italiano in chat,
inglese in doc/commit. FALLBACK: M5c al suo cap -> H2 -> N1
dichiarata, chiusura onesta con M-D comunque misurato; chiusura R3
obbligatoria.
