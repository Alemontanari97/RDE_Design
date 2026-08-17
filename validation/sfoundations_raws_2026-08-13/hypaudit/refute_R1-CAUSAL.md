# ADVERSARIAL REFUTATION ATTEMPT — [R1-CAUSAL] verdict CONDIZIONATA
# Target: validation/sfoundations_raws_2026-08-13/hypaudit/confront_r1.md
# Refuter raw, S-FOUNDATIONS raws, 2026-08-17. IN-REPO SOURCES ONLY.

STATUS: refuter raw (untracked at write time). Mandate: refute the verdict
using the same in-repo corpus; hunt specifically for papers/data the
assessment ignored (absence attack); default refuted=true if the verdict
overclaims. Sources read for this attack: confront_r1.md (in full),
ADVISORY_rde_choking_2026-08-11.md (in full),
literature_review/reports/00_APPARATUS_BRIEF.md (in full),
reports/liu_2022_aerospike_rde.md (in full),
reports/ornano_2017_pde_shapeopt.md (in full),
reports/miki_2020_nasa_methodology.md (targeted),
reports/wolanski_2013_survey.md (targeted),
ADVISORY_litmap_extension_2026-08-13.md (targeted grep), corpus-wide grep for
coupling/back-pressure/pressure-gain evidence across all reports.
ADVISORY_litreview_confrontation is cited nowhere below as decided
(pending-ratification discipline maintained; the confront itself already
firewalls its verdict from that advisory in RR4).

## 1. Anchor verification (the misquote attack — FAILED)

Given the repo's misquote-of-record precedent (choking advisory §3), every
load-bearing anchor of the confront was re-checked against its in-repo
source:

- K-P axial Mach 0.86-1.33 avg 0.99, cycle-integral choking definition,
  M~0.5 at low PR → VERIFIED verbatim, ADVISORY_rde_choking §1(b).
- Stechmann p.889 declared-assumption verbatim → VERIFIED, §1(a) (and the
  quote there carries its own S-GAUNTLET page-verify stamp).
- Harroun p.661 quench-via-ref-[9] → VERIFIED, §1(d) and C4.
- P-M 2022 "ASSUMED, not demonstrated", total-Mach-only, "No back-pressure
  sensitivity run, no two-way coupled run, and no axial-Mach margin are
  reported anywhere in the paper" → VERIFIED, paxson_miki_2022_nasa_opt.md
  §4 l.160 — NOTE: that sentence is scoped to *the paper*. See §2.
- Miki 2020 subsonic full-state Dirichlet interface → VERIFIED,
  miki_2020_nasa_methodology.md F-3 (ll.190-198) and hypothesis 8 (l.76).
- L4 / [T-NSW] "mean upstream influence EXCLUDED BY THEOREM" →
  VERIFIED, 00_APPARATUS_BRIEF.md ll.129-130. The confront's W1 correctly
  keeps the theorem scoped to MEAN influence — no overclaim there.

No misquote found. The attack on anchor fidelity fails.

## 2. THE ABSENCE ATTACK — PARTIAL SUCCESS. The corpus DOES contain the
## coupled experiment the confront says nobody ever ran: Liu 2022.

The confront's §3(ii) states: "No two-way coupled run and no back-pressure
sensitivity run exists in any read source"; its A3 justification states
"zero back-pressure sensitivity runs in the entire corpus — the experiment
that would settle R1 has never been run"; RR2 states the back-influence
magnitude "has no external anchor"; and the assessment's monitor bundle
carries A3 as "the run the entire SOTA never did". These absolutes are
FALSE at corpus scope.

**[Liu 2022, reports/liu_2022_aerospike_rde.md]** — never cited anywhere in
confront_r1.md — is a **fully coupled, single-domain, 3-D unsteady
chamber+nozzle simulation series** (12M cells, RANS k-ω SST + PaSR,
21-species Jet-A kinetics, report §2) in which the nozzle geometry Sigma is
varied across four configurations and the CHAMBER response is measured:

- Pressure gain η = (P_c − P₀)/P₀: A (no constriction, ε=100%) **−7.4%**;
  B (flat ramp, ε=87.3%) **+8.9%**; C (isentropic ramp, ε=87.3%) **+13.2%**;
  D (C truncated to 40%) **+13.1%** (Table 5, p.10).
- Fuel mass flow ṁ_f: 6.17 / 6.06 / 6.01 / 6.00 g/s (Table 7, p.12).

This IS a measured design-to-chamber sensitivity experiment — the
design-perturbation direction of the confront's own A3 (perturb Sigma,
measure the chamber/interface-family response) — executed by the SOTA,
in the read corpus, with a report on file. The chamber state (P_c, η, ṁ)
is upstream of any admissible interface, so a change in it IS a change in
the interface data family Gamma_d. Secondarily, **[Ornano 2017,
reports/ornano_2017_pde_shapeopt.md §3 stage 3]** is a coupled 3-D reacting
tube+nozzle simulation in the pulsed-detonation class (<1 Hz, outside RDE),
a second corpus counterexample to the "any read source" absolute. (Miki
2020 p.3 additionally *prices* a coupled limit-cycle run at "3-5 calendar
days", miki report l.205 — the coupled option is named in the NASA line
itself, merely not exercised for design.)

**What survives of the confront's claim once re-scoped**: no source in the
NASA decoupled-architecture line (P-M 2022, Miki 2020) ran a coupled or
back-pressure run — true and verified; and no read source ran the
*controlled impedance-only perturbation at fixed geometry with the
interface family as the measured object against a null band* — Liu's is a
discrete four-point geometry family with viscous/reacting confounders and
no interface-state decomposition, not a certified A3. So A3 remains
justified as a monitor. But "the experiment that would settle R1 has never
been run" is an overclaim: a coarse, published version of exactly that
experiment exists in-corpus and the confront missed it.

## 3. What the missed dataset actually says about R1 — it CUTS FOR the
## verdict's structure, not against it

Read against the confront's own window W1-W4, Liu's four points are a
ready-made experimental decomposition:

(a) **A vs B** (add a converging restriction, ε 100→87.3%): chamber
    pressure gain FLIPS SIGN (−7.4 → +8.9%). Measured, coupled
    confirmation of back-channels §2.2/§2.3 (restriction → chamber state):
    the confront asserted this link partly by "elementary mass-flow
    bookkeeping"; the corpus in fact contains a direct measurement.
(b) **B vs C** (SAME constriction ratio ε=87.3%, different ramp contour —
    the ramp forms the aerospike throat): η moves **8.9 → +13.2%** (4.3
    points), thrust 150.49 → 166.36 N, ṁ_f 6.06 → 6.01. A fixed
    throat-AREA scalar is therefore measurably INSUFFICIENT to freeze the
    chamber: contour changes at the throat station move the chamber state
    at fixed ε. This does not break W2's primary clause (the ramp is not
    "downstream of a certified interface" — it *is* the throat), but it
    kills any operational reading of W2 as "throat area unchanged ⇒ safe".
(c) **C vs D** (purely downstream truncation, throat identical): η
    13.2 → 13.1%, ṁ_f 6.01 → 6.00 — chamber essentially INVARIANT. This is
    the corpus's ONLY measured positive instance of the R1-safe subspace
    (design change strictly downstream ⇒ chamber unchanged), on a coupled
    simulation. The confront claimed the safe subspace had no empirical
    instance beyond Teasley's *untested* parameterization choice; in fact
    a measured instance exists and it CONFIRMS the conditional core.

Caveats binding any use of (a)-(c): viscous, turbulent, finite-rate — a
declared structural non-containment of the program's S1 class (liu report
F4); no error bars; single operating point; ṁ comparability across cases
not enforced (liu report, undeclared hypothesis 13). Order-of-magnitude
anchor, not a certified band.

Minor ignored pro-premise datum, for completeness: Wolanski p.148
(wolanski report §(i)) — "the products from the detonation chamber are
flowing out with supersonic velocity, there is no need to apply a
converging–diverging nozzle" — an unquantified corpus *assertion* of the
supersonic premise (no axial/total decomposition, no margin), dominated by
K-P's measured 0.86-1.33 axial span. It changes nothing; noted so that the
absence sweep is complete. Gonzalez-Viana 2025 (read in full per choking
advisory §5, no report on disk) is absent from the confront's sweep; the
only R1-adjacent content documented in-repo (choking advisory §1(e)) is an
optimization-criterion remark, not a coupling result — no verdict-bearing
content lost, but the confront's "every source in the read corpus" framing
silently excludes a fully-read source.

## 4. Attacks on the verdict category itself — FAILED

(i) **Should it be REFUTED outright (unconditional R1 dead ⇒ hypothesis
dead)?** No: the confront never defends the unconditional form — it
declares it "contradicted by the corpus as a generic claim" and restricts
legitimacy to the W1-W4 window. Liu (a)/(b) add measured coupled
confirmation of the failure modes outside the window; Liu (c) adds
measured confirmation inside it. The two-sided evidence is exactly what
"CONDIZIONATA" encodes.

(ii) **Should it be DA-RISCOPARE?** No: the repo's L4/[T-NSW]/two-regime/
H-EXO apparatus already is the scoping the data demands (confront §4); the
missed dataset requires an evidence-bundle correction and one wording
hardening (W2, below), not a reformulation.

(iii) **Does the window overclaim theorem coverage?** No: W1 states
"theorem-exact for MEAN upstream influence ([T-NSW])" — scoped exactly as
the apparatus brief states it (ll.129-130), fluctuating-influence exclusion
is not claimed from the theorem. Checked; honest.

(iv) **Do the monitors overclaim?** One phrase: A3's "the run the entire
SOTA never did" (also confront §3(ii)/RR2 absolutes) — per §2, false as an
absolute; A3's *content* (impedance perturbation vs null band, mandatory
at F5) stays justified and is now CALIBRATABLE against Liu instead of
anchor-free.

## 5. VERDICT ON THE VERDICT: **NOT REFUTED** (refuted = false)

CONDIZIONATA with window W1-W4 and monitors A1-A6 survives adversarial
re-reading; the missed Liu 2022 dataset strengthens both halves of the
verdict (failure outside the window measured; invariance inside the window
measured). The refutation succeeds only against the evidence bundle's
absolute absence claims. SURVIVING OBJECTIONS (each a mandatory correction
to the assessment's evidence/monitor text, none verdict-flipping):

SO-1. FALSE ABSOLUTE: "no two-way coupled run / no back-pressure
      sensitivity run exists in any read source; the experiment that would
      settle R1 has never been run" (confront §3(ii), §5 A3, RR2; monitor
      A3 wording). Counterexamples in-corpus: Liu 2022 (coupled
      chamber+nozzle, four geometries, measured chamber response,
      Tables 5/7); Ornano 2017 stage 3 (coupled, PDE class). Re-scope to:
      "no coupled or back-pressure run exists in the NASA
      decoupled-architecture line, and no read source ran a controlled
      impedance-only perturbation at fixed geometry with the interface
      family as the measured object."

SO-2. RR2 "no external anchor to calibrate a tolerance against" is
      overclaimed: Liu 2022 provides a coarse published anchor for A3's
      null band — η response ~4.3 points at fixed ε under a throat-contour
      change, ≤0.1 point under a purely-downstream change, ṁ_f spread ~1%
      — usable order-of-magnitude only, with the declared viscous/reacting
      non-containment caveats.

SO-3. W2 wording hazard: the gloss "no throat-area change" invites a
      fixed-A_t operational test that Liu B-vs-C measurably defeats (same
      ε=87.3%, η moves 8.9→13.2%). W2 must be enforced solely by its
      primary clause — geometry variation strictly downstream of the
      CERTIFIED interface — with throat-area invariance explicitly marked
      NECESSARY-NOT-SUFFICIENT.

SO-4. Missed corroboration (completeness of the evidence sweep): Liu
      C-vs-D is the corpus's only measured chamber-invariance under a
      purely downstream design change and belongs IN the evidence bundle
      as the empirical instance of the R1-safe subspace (currently the
      bundle offers only Teasley's untested parameterization choice); and
      the confront's "every source in the read corpus" sweep silently
      omits Liu 2022, Ornano 2017 and Gonzalez-Viana 2025.

## 6. One-line summary

The verdict stands — CONDIZIONATA is what the corpus supports, and the
assessment's window/monitors are the right machinery — but its evidence
bundle contains a false absolute ("the SOTA never ran the coupled
experiment": Liu 2022 did, coupled, four geometries, measured chamber
response) and missed that the same dataset supplies both the strongest
measured confirmation of the back-channels AND the only measured instance
of the R1-safe subspace; A3 gains a calibration anchor, W2 needs one
wording hardening, and the "no external anchor" residual is downgraded.
