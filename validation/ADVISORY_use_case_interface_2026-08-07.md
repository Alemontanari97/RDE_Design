# ADVISORY — The user's primary USE CASE and its interface duties
# (2026-08-07, inter-session window; input to the S21 F0 ratification;
# stress-tests the plan's generality per the standing directive)

USE CASE OF RECORD (user, verbatim intent): run CFD of the chamber
ONLY, up to the throat; extract the exit data; hand it to the
machinery to design the optimal nozzle. In that data BOTH the
oblique shock AND the slip line are present, and both are CAPTURED
(smeared over cells), not sharp.

## VERDICT: architecture foreseen at the foundations; three NEW
## named duties emerge; phase ORDER unchanged.

FORESEEN (contract level): the interface contract (Gamma_d, D, mu)
of D1/D2.6 exists precisely for external-solver data; stage-A
admission audits (Crocco compatibility, characteristic completeness
on axially supersonic patches, spacelikeness margin, declared
closure on subsonic patches); periodic-wave scope + T0 flatness
monitor; front taxonomy case (b) (data-borne fronts); F2 stratified
general engine. The use case CONSUMES the plan, does not break it.

## THE PHYSICS THAT DECIDES THE DUTIES

1. CAPTURED SHOCK RE-STEEPENS UNDER EXACT MoC: a CFD-captured shock
   is a steep-but-smooth compression layer; exact characteristic
   evolution refocuses it — same-family characteristics reconverge
   and the fold RE-FORMS a short distance downstream of the
   interface. The certification gate would (correctly) refuse.
   Hence for this use case data-borne front FITTING is MANDATORY,
   requiring a new operator:
   DUTY U1 — INTERFACE FRONT-EXTRACTION OPERATOR: detect the
   captured shock in the per-phase CFD profile, reconstruct sharp
   RH-consistent states across it, seed a fitted front into the
   march; with its OWN validation oracle (synthetic captured-profile
   KAT: smear a known sharp solution, extract, compare). Upgrades
   the panel's F5-entry conditional "case-B profile generator with
   own oracle" from synthetic generator to CFD-to-contract pipeline.
   Owner: F5 entry (machinery in F4b/F2).

2. CAPTURED SLIP LINE DOES NOT SELF-STEEPEN: the contact field is
   LINEARLY DEGENERATE — a smeared shear/entropy layer advects
   along streamlines without steepening. The F2 general engine
   (three-family, s/h0 transport) marches it as smooth stratified
   data with NO fold formation; resolution is the only cost.
   DUTY U2 — CONTACT ADJUDICATION OF RECORD: default = smeared
   contact as smooth stratified data (justification: linear
   degeneracy, to be stated with rigor class); OPTION = fitted
   contact as declared-topology front for sharpness (pending the
   red-team verification of degenerate-front coverage in the
   U-series; if uncovered, the smooth-stratified route SUFFICES for
   this use case). Owner: F2a (statement), F4b (fitted option).

3. EXTRACTION SURFACE PLACEMENT: at the exact throat the per-phase
   problem is TRANSONIC with nonuniform data (no clean Sauer
   start; the contract only DECLARES closures on subsonic patches).
   DUTY U3 — EXTRACTION-SURFACE RULE: the tool's data contract
   requests the profile on a surface slightly DOWNSTREAM of the
   throat where the axial flow is per-phase SUPERSONIC (the
   stage-A characteristic-completeness audit is exactly the check);
   exact-throat hand-off (nonuniform transonic start) = a SEPARATE
   priced duty, never silently absorbed. Owner: F5 entry contract
   text; F2a audits.

CONSEQUENCE FOR THE AUDITS: stage-A admission audits (today 1-of-3
implemented, audit finding) become LOAD-BEARING for this use case —
CFD data will not satisfy Crocco/RH exactly, so the audits with
derived bands are the gatekeeper (loud reject or declared
tolerance). Their implementation priority rises accordingly (F2a).

RATIFICATION ACTION (S21 F0): add U1-U3 to the plan text (F5 entry +
F2a/F4b owners as above); record the use case itself in D1 as the
canonical consumption pattern of the interface contract.

## U1 SURVEY ADDENDUM (2026-08-11, web-verified as live lines;
## sources NOT page-verified in-repo — acquisition at the owning
## phase per the survey directive)

The captured->fitted "re-discontinuization" EXISTS in modern
literature as two complementary lines:
 (a) ENGINEERING/CFD — the modern unstructured shock-fitting school
     (Paciorri-Bonfiglioli lineage): shocks computed EXPLICITLY via
     Rankine-Hugoniot on unstructured grids, the fitted front as a
     double-sided zero-thickness internal boundary with
     upstream/downstream states obeying RH; extended to 3-D,
     unsteady, and shock-shock interactions; direct convergence
     comparisons capturing-vs-fitting published (AIAA J); recent
     bridging work (extrapolated shock tracking, arXiv 2402.13681).
     Their workflows include initializing the fitted front FROM a
     captured solution = exactly the U1 operation.
 (b) RIGOROUS APPROXIMATION THEORY — the Gelb-Tadmor CONCENTRATION
     METHOD (1999 + refinements; Tadmor Acta Numerica 2007): PROVEN
     convergence for locating jump discontinuities AND their
     amplitudes in piecewise-smooth data (K_eps * f(x) = [f](x) +
     O(eps); exponentially accurate and noise-robust variants;
     minmod-based adaptive detectors). The per-phase interface
     profile is 1-D (radial), the method's native habitat.

U1 METHOD OF RECORD (candidate, SOTA-composed; each piece citable,
the composition ours — novelty note query-bounded):
 0. LICENSE: conservativity of the capturing scheme => RH holds
    ACROSS the captured layer to scheme order (Lax-Wendroff
    heritage): plateau states outside the layer are trustworthy,
    the layer interior is not.
 1. POSITION/AMPLITUDE: concentration-kernel edge detection on the
    per-phase profile (proven convergence; noise-robust variant).
 2. STATES: piecewise-smooth high-order reconstruction of the two
    sides away from the layer, evaluated at the detected edge.
 3. EXACT CONSISTENCY: project the extracted state pair onto the
    exact RH manifold (smallest correction in a derived norm);
    contact analog: pressure/normal-flux continuity.
 4. AUDIT (stage-A): the projection residual gets a DERIVED band;
    beyond band = LOUD REJECT (under-resolved data), never a silent
    acceptance.
 5. KAT/REJECTOR: smear a known exact oblique-shock solution,
    extract, recover position/states within derived bands; a
    corrupted profile MUST be rejected.
 RDE caveat: the chamber shock is rotating/unsteady — the per-phase
 extraction lives inside the quasi-steady decomposition (T0
 monitor); the unsteady branch of line (a) is the reference if the
 per-phase assumption is ever stressed.
