# SPEC — ideal-contour LENGTH comparison oracle (bell TIC vs full spike)
# Minted 2026-08-17 (S-FOUNDATIONS window, user question of record:
# "il rapporto relativo fra le lunghezze di un bell TIC ideale e uno
# spike non troncato ideale a parita di area di gola e rapporto di
# espansione"). DECIDABLE-BY-CONSTRUCTION question — neither party's
# intuition is citable as theorem; the carrier decides.

## BLOCKING PRECONDITIONS (measured 2026-08-17, this window)
1. GENO working tree is CONTAMINATED: src/lib/Profile_m.f90 +
   src/lib/MoC_Gen_m.f90 modified by the incomplete S-GENOAUDIT
   instrumentation patch, declared NON-INERT of record (baseline md5
   invalid while present). Profile_m touches geometry generation:
   NO length number from the current tree is of-record-grade.
   Patch removal/restoration = GENO-session action under GENO's own
   protocol (census R13), NEVER from this repo's windows.
2. MOC-10 P0 (wall-thrust double-count) does not touch geometry
   (main.f90:540-545 de-duplicates geometry output) but the same
   resumption session is the right window; THRUST outputs stay
   quarantined regardless (registry row
   oracles:geno-tocnoz-wall-thrust-double-count).

## THE EXPERIMENT (first item of the S-GENOAUDIT resumption)
QUESTION: dimensional axial length L (throat plane -> exit plane /
plug tip) of (A) the FULL ideal bell (TIC parent: shock-free,
uniform axial exit at M_e — NOT the Rao TOC) vs (B) the FULL
(untruncated) ideal spike (lip-centered expansion, isentropic plug
to the tip), at EQUAL throat area A_t and EQUAL expansion ratio
eps = A_e/A_t.
PINNED DEFINITIONS (no wiggle room at read time):
- L_bell: throat plane to exit plane of the uniform-exit contour.
- L_spike: cowl-lip plane to plug tip (+ report lip-to-throat offset
  separately if the construction places the throat off the lip).
- Gas: gamma(T) thermally-perfect frozen mixture OF RECORD (same
  tables both sides); gamma=const twin run as declared oracle only.
- Geometry class: AXISYMMETRIC (the program's class); planar twin
  optional as cross-check of the reflection-equivalence intuition.
- Sweep: eps in a declared ladder (e.g. 5, 10, 25, 50, 100) — a MAP,
  not one anecdote; A_t fixed across the sweep.
PROTOCOL:
1. GENO session (R13 protocol): restore clean tree (patch removed,
   md5 baselines re-verified) BEFORE any run; declare tree hash.
2. Verify GENO exposes both design modes (circular ideal-contour
   design + annular/plug ideal design); if the TIC-parent mode is
   absent, the bell side runs on the IN-REPO MoC machinery instead
   (dual-code by construction) — declared, not silently swapped.
3. Lengths read from GEOMETRY outputs only (thrust quarantined per
   MOC-10 until its fix lands); per-run convergence check (mesh
   halving, length shift within derived band).
4. Output: table L_bell(eps), L_spike(eps), ratio, bands; verdict
   sentence with hypotheses (ideal, inviscid, full-length,
   axisymmetric, gamma(T) pinned).
DUAL-PROOF NOTE: the in-repo MoC bell construction doubles as the
independent instrument for side (A); cross-code agreement != truth
(standing directive) — disagreement beyond bands = finding.
OWNER: S-GENOAUDIT resumption session (census R13), first item after
tree restoration + MOC-10 fix. NOT runnable in this window (blocking
precondition 1).
