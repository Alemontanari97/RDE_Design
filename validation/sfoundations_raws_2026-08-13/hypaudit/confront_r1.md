# HYPOTHESIS AUDIT — [R1-CAUSAL] Causal separation (nozzle design does not
# alter the interface data family; no upstream influence through Gamma_d)
# vs. the in-repo literature corpus. S-FOUNDATIONS raws, 2026-08-17.

STATUS: audit raw (untracked at write time). Sources: IN-REPO ONLY —
literature_review/reports/*, validation/ADVISORY_rde_choking_2026-08-11.md,
validation/ADVISORY_mean_swirl_panel_2026-08-11.md,
validation/ADVISORY_litmap_extension_2026-08-13.md,
validation/ADVISORY_litreview_confrontation_2026-08-13.md (**CAVEAT: NON
RATIFICATA — cited below only as pending-ratification evidence, never as a
decided position**), validation/ASSESSMENT_methodology_position_2026-08-13.md,
literature_review/reports/VERIFICATION_FABLE_2026-08-13.md, and the frozen
problem statement's own apparatus (literature_review/reports/00_APPARATUS_BRIEF.md).
No web access used. Adversarial stance: literature data over internal preference.

## 0. The hypothesis as posed

[R1-CAUSAL], from the frozen problem-statement bundle: *the nozzle design
Sigma does not alter the interface data family (no upstream influence through
Gamma_d)*. As posed it is UNCONDITIONAL — no interface-class qualifier appears
in the bundle sentence. The repo's own apparatus carries the conditional
version: the L4 interface class ("every patch axially supersonic with margin"),
on which mdot-independence is EXACT and "mean upstream influence is EXCLUDED BY
THEOREM [T-NSW]" (00_APPARATUS_BRIEF.md, lines 129-131). The audit question is
therefore: does the literature license the unconditional statement, the
conditional one, or neither — and what does it force us to monitor?

## 1. What the corpus actually does with this hypothesis: ASSUMES it, four ways

Every source in the read corpus that needs causal separation *imposes* it;
none demonstrates it. This is the single most consistent finding across the
25-paper corpus.

(a) **[Paxson-Miki 2022, reports/paxson_miki_2022_nasa_opt.md §4]** — the
sharpest instance, with a dedicated verification section in the report. Claim
under test (their abstract, p.1): "The fluid in the RDRE chamber leading to
the nozzle is choked at its exit so that its cyclic behavior is unaffected by
any changes to the nozzle design." Report verdict: **"ASSUMED, not
demonstrated — a modeling hypothesis with partial internal support."** The
decoupling is (i) built into the Q2D outflow BC ("the exit plane boundary
condition ... **ensures** that the flow is sonic or supersonic at all times",
p.2; "If the resulting flow is sonic, or supersonic, then the imposed pressure
is disregarded", p.4 — the code *switches off* downstream influence);
(ii) structurally guaranteed by the one-way two-code architecture (the annulus
solution is computed once, before any nozzle exists, and reused unchanged for
all seven nozzles); (iii) supported only by the *total-velocity* Mach field
(1.15-1.45, Fig. 3), which "comprised of both axial and circumferential
velocity components" — the axial Mach, the one that decides upstream
influence, is never shown, while the same paper reports "significant local
tangential velocity components" (p.2). **"No back-pressure sensitivity run,
no two-way coupled run, and no axial-Mach margin are reported anywhere in the
paper."** The oft-cited 6% interface-placement check (p.5) compares two
stations of the *same* Q2D solution — it tests where the interface was placed,
"not whether the nozzle can talk back."

(b) **[Miki 2020, reports/miki_2020_nasa_methodology.md T-3, F-3]** — verbatim
p.4: "this approach is based on the **assumption** that the flow is chocked
[sic] at the throat. As a result, the change of the nozzle shape should not
significantly affect the combustor characteristics upstream." Worse than
Paxson-Miki structurally: their interface sits "just upstream of physical
throat", i.e. in **subsonic** flow, where a full-state Dirichlet BC (Pt, Tt,
u, v, w, y_i) is characteristically over-determined and "mechanically
suppresses upstream influence" (F-3). The decoupling is a numerical fiat that
buys the reusable-BC architecture — it is what makes multi-geometry studies
affordable, i.e. the assumption is load-bearing for their economics, not
tested physics.

(c) **[Stechmann 2019, via ADVISORY_rde_choking §1(a)]** — choking is a
DECLARED ASSUMPTION, p.889 verbatim: "It is thus assumed that the flow at the
RDE exit plane is sonic at all points in the cycle to simplify the analysis";
throat = channel exit plane by declaration; no transonic analysis anywhere.

(d) **[Harroun 2020, reports/harroun_2020_validation.md H-U1; Harroun 2021,
reports/harroun_2021_jpp_nozzle_perf.md]** — choking BYPASSED: the chamber is
never simulated; an analytic rotating pressure waveform is imposed one
diameter upstream of the channel exit (Eqs. (1)-(2)), identical for every
downstream geometry. Report H-U1 (undeclared-but-necessary): "The inlet plane
is a valid, one-way (non-reflecting-in-practice) boundary: the imposed
waveform is unaffected by the nozzle downstream. This is exactly the
*upstream-influence* assumption our program handles with the L4
axially-supersonic-with-margin interface class and [T-NSW]; here it is imposed
by fiat with no characteristic-completeness audit." No characteristic-
admissibility or choking-margin statement is made anywhere despite a 30 atm
wave peak entering a nominally 8.6 atm chamber (harroun_2021 report, item d
of the undeclared-hypothesis list).

Aggregate [pending-ratification corroboration:
ADVISORY_litreview_confrontation §3.24 "Choking come assunzione → CONFERMATO
×3"; §3bis-G]: no read source can be cited as evidence that RDE exit data IS
L4-admissible — "solo che la SOTA *assume* o *impone* un'interfaccia
sonica-o-supersonica" — and a citation ban (C24/D-36) is proposed on using
published exit-plane Mach numbers as L4 evidence, because they are
total-velocity Mach.

CONSEQUENCE 1: [R1-CAUSAL] cannot be cited to the literature as a
demonstrated property. The corpus's universal practice makes it a
*hypothesis with a named enforcement mechanism*, never a result. Any claim of
the form "the literature shows the chamber decouples" is a misreading of
BC-enforced architectures.

## 2. What the corpus establishes AGAINST the unconditional form

Three independent, page-anchored causal paths from nozzle geometry back into
the interface data family exist in the read corpus. Each one breaks
unconditional R1.

### 2.1 The supersonic premise itself fails on part of every cycle (generic mu(Xi_sub) > 0)

**[Kaemming-Paxson 2018, via ADVISORY_rde_choking §1(b), §2 C1]**: their own
data (Table 1 p.6, Fig. 6 p.10) — healthy-case throat-plane AXIAL Mach spans
**0.86-1.33, average 0.99**: "a per-phase axially-SUBSONIC patch exists AT THE
THROAT during part of EVERY cycle even when the device is 'effectively
choked'"; at low PR the exit is substantially subsonic (M8x ~ 0.5, §VI.H,
p.14). Choking in their frame is CYCLE-INTEGRAL (maximum mass flow), not
pointwise-sonic — "any choking condition ... will have a range of axial Mach
numbers ... both subsonic and supersonic portions" (p.10). The advisory's C1:
"NO GENERIC SUPERSONIC SURFACE: the per-phase axially-supersonic extraction
surface FAILS on part of every cycle in the healthy K-P case and entirely in
low-PR regimes." [Pending-ratification: confrontation §3bis-G registers
"mu(Xi_sub) > 0 è il caso generico, page-verified".] Harroun 2020's own
waveform arithmetic (harroun_2020 report §4) independently corroborates the
weighting: 64% of the cycle sits below CTAP, and the flared design spends most
of every cycle far below its design NPR (F5: "mu(Xi_sub) > 0 is the generic
RDE case, not a corner").

Consequence: wherever an axially-subsonic patch exists, incoming
characteristics reach the interface and downstream geometry CAN write onto
Gamma_d. On those patches R1 is not weakened — it is the wrong sign of
statement: upstream influence is the *generic mechanism*, and its absence
must be *engineered* (the two-regime contract's declared closure), not
assumed.

### 2.2 Physical exit restriction can change or kill the wave system

**[Harroun 2021, via ADVISORY_rde_choking §1(d), C4]**: "throat RESTRICTIONS
can quench detonation at rocket conditions (p.661, via ref [9])". This is the
strongest possible violation of R1: a converging-throat design choice does
not merely perturb the interface family — it can remove the detonative
solution branch entirely. The advisory's C4 already scopes this as a
DATA-VALIDITY caveat on any use case whose chamber CFD runs up to a physical
throat. A design family that includes exit-restriction geometry therefore
contains members for which Gamma_d(Sigma) is not even the same *kind* of
object.

### 2.3 Chamber pressure sets the wave mode; exit restriction sets chamber pressure

**[Teasley 2025, reports/teasley_2025_rdre_dev.md T-4]**: NASA's
program-of-record data says "the **wave mode is a function of chamber pressure
and propellant**", with mode multiplicity a design requirement across throttle
(p.9: hydrogen "yields a vastly different number of wave at low pressure, and
pure deflagration at higher pressures exceeding 250 psia CTAP or so"; p.7:
"future designs must implement strategies by which multi-mode operation is
achieved even at throttled conditions"). **[Wolanski 2013,
reports/wolanski_2013_survey.md F4]** organizes the same physics by the Wave
Number W = t_r/t_mf (Eqs. (4)-(5), p.144): W ~ integer gives n stable heads;
W << 1 gives galloping and degeneration to deflagration — mode structure is a
function of operating parameters, empirically documented (pp.143-145).

The chain is: nozzle/exit geometry -> effective exit impedance -> mean chamber
pressure at fixed feed -> wave count/mode -> interface data family. The
corpus documents links 2-3 (mode vs. chamber pressure) directly; link 1
(restriction -> chamber pressure) is elementary mass-flow bookkeeping that
every 0-D closure in the corpus embodies (Stechmann's effective throat area
definition, choking advisory §1(a)). Note the important boundary: **when the
interface is genuinely choked with margin, the chamber pressure is set by
feed + effective throat area, and *downstream-of-throat* contour changes at
fixed throat area leave it unchanged** — that is precisely the corpus's
(assumed) mechanism, and it is why R1 has a legitimate core. But a design
vector that touches the throat area, the annulus exit, or any restriction
upstream of the interface moves chamber pressure and hence potentially the
wave mode — a family-level change, not a per-phase perturbation. Teasley's
own undeclared hypothesis 1 ("nozzle/chamber separability", teasley report §4)
shows the SOTA silently assumes this never happens for their nozzle-extension
parameterization (length, angles, exit diameter — all downstream of the
choked annulus exit): their design vector is *chosen inside the R1-safe
subspace*, which is exactly the discipline R1 must state rather than assume.

### 2.4 Feed-side coupling is not automatically saturated either

[Pending-ratification: confrontation R25] — Teasley 2025 reports 100-415 psid
injectors on 700-1250 psia chambers, "ben sotto la condizione di choking,
senza chug": the *injector*-side choking that would isolate the feed system is
not guaranteed in flight-relevant hardware, and "nessuna delle fonti lette
pubblica" a measured choking margin at the interface. Upstream influence that
reaches the chamber can therefore propagate further than the chamber alone —
the interface family's *provenance* (feed conditions) is itself
pressure-coupled. This does not act through Gamma_d directly but widens the
blast radius of any R1 failure.

## 3. What the repo's own machinery adds (and what it may and may not claim)

The program is the only actor in this landscape with a *theorem* where the
corpus has an assumption: on the L4 class (every patch axially supersonic
with margin), mean upstream influence is excluded by [T-NSW]
(00_APPARATUS_BRIEF.md line 129-131), and the two-regime contract
(ADVISORY_rde_choking §2, C1-C3) handles the generic mu(Xi_sub) > 0 case by a
declared closure instead of a silent fiat. The confrontation advisory
[pending ratification] proposes the exact hypothesis-form R1 must take:
**(H-EXO)** "La misura di ciclo e la mappa di stato d'interfaccia sono ESOGENE
al design: dmu/dSigma = 0 e ds(xi)/dSigma = 0, garantite sulla classe L4 ...
dall'esclusione dell'influenza a monte per [T-NSW]. Falsificatore nominato:
una dmu/dSigma != 0 misurata. Diventa portante a F5 (RDE accoppiato) e ovunque
mu(Xi_sub) > 0" (§ line ~629, duty D-02). That is: causal separation is a
*named, falsifiable hypothesis with a theorem-backed validity class*, not a
fact.

Two honesty constraints bind any claim built on this:

(i) **Nobody has ever verified that real RDE interface data lives in L4.** The
published exit Mach fields are total-velocity (P-M Fig. 3); axial Mach is
reported only by K-P, and it dips to 0.86 at the throat in the healthy case.
The empirically supported expectation is that L4 holds at best on *part* of
the cycle, patch-wise — which is exactly how the two-regime contract is built.

(ii) **The back-influence magnitude when the margin thins is unmeasured in the
corpus.** No two-way coupled run and no back-pressure sensitivity run exists
in any read source (paxson_miki report §4; miki report). The audit R1 needs
has literally never been run by the SOTA — which simultaneously means (a) our
stage-A audits are doing non-redundant work (paxson_miki F3: "our audit list
... is doing work that the SOTA does not do"), and (b) there is no external
anchor to calibrate a tolerance against.

## 4. VERDICT: **CONDIZIONATA**

[R1-CAUSAL] as posed (unconditional causal separation) is contradicted by the
corpus as a *generic* claim: axially-subsonic interface patches are the
generic RDE case (K-P measured; Harroun-derived weighting), physical
restrictions can quench the wave system (Harroun 2021 p.661), and chamber
pressure — which exit-restriction design controls — selects the wave mode
(Teasley 2025, Wolanski 2013). But the hypothesis has an exact, theorem-backed
core on a NAMED validity window, and inside that window it is stronger than
anything the SOTA holds (they assume; we prove-on-class + monitor). Hence:
legitimate ONLY in the following declared window, with the audits of §5
armed. It is not DA-RISCOPARE: no re-formulation is needed, because the
repo's own L4/[T-NSW]/two-regime/H-EXO apparatus already IS the correct
scoping — what is illegitimate is only the unconditional reading.

**VALIDITY WINDOW (all four clauses required):**

W1. **Interface class**: every patch of the extraction surface axially
    supersonic with measured margin, min_xi(M_axial - 1) >= m0 > 0, AXIAL Mach
    (swirl separated out — the tangential component does not buy
    spacelikeness; choking advisory C2; mean-swirl panel P4: total Mach with
    swirl "overstates axial marching margin"). On this class R1 is
    theorem-exact for mean upstream influence ([T-NSW]).

W2. **Design-vector scope**: the design family varies only geometry
    DOWNSTREAM of the certified interface — no throat-area change, no
    converging restriction upstream of the interface (Harroun 2021 p.661
    quench caveat = choking advisory C4). Teasley's nozzle-extension
    parameterization (length/angles/exit diameter downstream of a choked
    annulus exit) is the SOTA instance of staying inside this subspace.

W3. **Operating-point exogeneity**: chamber pressure and feed condition fixed
    by the operating measure mu, not altered by the design loop; wave mode
    definite and stable at every point of supp(mu) (Teasley T-4; Wolanski
    W ~ integer; D2.3 mode-transition exclusion). Where the design loop can
    move chamber pressure, H-EXO's falsifier (dmu/dSigma != 0) is live and R1
    is NOT available — this becomes load-bearing at F5 (coupled RDE).

W4. **Per-phase failure routed, not ignored**: on any axially-subsonic patch
    (mu(Xi_sub) > 0, the generic case) R1 is replaced by the declared
    two-regime closure (O1/O2/O3 path, load-bearing per choking advisory C1)
    — never silently extended.

## 5. AUDITS THE LITERATURE JUSTIFIES (each one is the certified version of a
## gap the corpus itself exhibits)

A1. **Axial-margin monitor** — min_xi(M_axial - 1) with derived margin,
    per patch, per phase, tangential component explicitly separated. Justified
    by: P-M publishing only total Mach while asserting decoupling; K-P's
    0.86-1.33 axial span. (= stage-A characteristic-completeness audit,
    choking advisory C1/C2.)

A2. **Outgoing-characteristics certificate** — "all normal characteristics
    outgoing at every phase on the extraction surface, else LOUD REJECT" — the
    certified version of P-M's BC (choking advisory C3). Justified by: the
    SOTA's decoupling being enforced by exactly this BC without ever checking
    it.

A3. **H-EXO falsifier, armed** — a measured back-pressure/geometry sensitivity
    of the interface family: perturb downstream impedance (or Sigma) and
    measure d(Gamma_d)/dSigma and dmu/dSigma against a null band. Justified
    by: zero back-pressure sensitivity runs in the entire corpus — the
    experiment that would settle R1 has never been run; it is cheap on our
    own data pipeline and is the named falsifier of D-02 [pending
    ratification]. Becomes MANDATORY at F5.

A4. **Restriction/quench data-validity flag** — any design family member or
    use-case chamber with a converging restriction upstream of the interface
    carries the Harroun p.661 quench caveat as a DATA-VALIDITY flag (choking
    advisory C4): R1 unavailable for that member until the chamber data is
    re-generated with that geometry.

A5. **Mode-definiteness / family-provenance label** — Wave Number W
    provenance label (Wolanski Eqs. (4)-(5), PRACTICE-grade, never a
    certificate) + T0-flatness monitor + D2.3 mode-transition exclusion on
    supp(mu). Justified by: Teasley T-4 (mode transitions expected INSIDE the
    support of throttle-relevant measures) and Wolanski pp.143-145
    (galloping regime real). If a design change can move chamber pressure
    across a mode boundary, the interface family must be RE-GENERATED, never
    reused — reuse is exactly the P-M architecture whose validity is assumed.

A6. **Two-regime routing audit** — mu(Xi_sub) measured per dataset; if > 0,
    the declared closure is engaged and reported (J as written is UNDEFINED
    otherwise, per the apparatus). Justified by: K-P measured subsonic
    patches in the healthy case; Harroun-derived 64%-below-CTAP weighting.

## 6. RESIDUAL RISKS (named, with owners where the record has them)

RR1. **Empirical vacuum on the margin**: no read source publishes a measured
     choking/axial margin at the interface [pending-ratification R25]; the L4
     admissibility of real RDE data is unverified ANYWHERE. Risk: the L4
     window may be empty on part of every cycle for all real hardware (K-P
     suggests exactly this), making W4/A6 the *operative* path, not the
     exception. Owner: stage-A audits on first real dataset (F2).

RR2. **Back-influence magnitude unquantified**: no two-way coupled run exists
     in the corpus; the size of dGamma_d/dSigma when the margin thins has no
     external anchor. A3's null band must be derived internally. Owner: F5 /
     H-EXO.

RR3. **Quench threshold unquantified in-corpus**: Harroun p.661 is a warning
     via ref [9], not a mapped boundary; A4 is a flag, not a predictor.

RR4. **Ratification dependency**: the sharpest registered formulations
     (H-EXO/D-02, mu(Xi_sub)>0-generic/3bis-G, citation ban C24/D-36, R25)
     live in ADVISORY_litreview_confrontation_2026-08-13.md, which is NOT
     ratified. This audit's verdict does not depend on them (the primary
     anchors are the per-paper reports and the ratified-in-substance choking
     advisory), but the *duty wording* should be consumed from the advisory
     once ratified, not re-derived.

RR5. **Swirl-margin interaction**: spacelikeness of the interface is decided
     by the axial cone, but published fields are total-Mach with significant
     swirl (P-M p.2); mean-swirl panel P4 warns the closure class + margin is
     overstated by total Mach. The margin monitor A1 must consume the
     (Gamma, h0, s)-triple-aware decomposition, else it can falsely certify
     L4.

RR6. **F5 phase change**: at coupled-RDE (F5) the measure itself becomes
     design-coupled and R1's protected content shrinks to W1-W2 only;
     everything else transfers to H-EXO's measured-falsifier regime. The
     hypothesis must be re-audited at F5 entry — this window's verdict does
     not carry over.

## 7. One-line summary

The corpus never proves causal separation — it enforces it by boundary
condition and architecture (P-M 2022 verbatim "ASSUMED, not demonstrated") —
and it documents three real back-channels (subsonic patches generic, K-P;
restriction quench, Harroun p.661; mode-vs-chamber-pressure, Teasley/Wolanski);
[R1-CAUSAL] is therefore legitimate only on the named window {axial-supersonic
with measured margin; design vector downstream of the certified interface;
mode-definite exogenous operating point; subsonic patches routed to the
declared closure}, with the six audits of §5 armed — inside that window it is
theorem-backed ([T-NSW]) and strictly stronger than SOTA practice; outside it,
the literature says the influence R1 denies is the generic mechanism.
