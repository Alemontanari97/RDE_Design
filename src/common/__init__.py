"""Shared core of the lecture package: constants, mixture registry, CJ core.

constants : G0, P_ATM, P_REF_BAR, T_STD, T_REF + the standard tolerance ladder
mixtures  : the 12-mixture registry (Cantera X string, mechanism, display
            name, fuel/ox, SK K factor) with kerosene/C12H26 aliases
cj_core   : cj_state(mix, p1, T1) — the ONE canonical CJ-state function
            (SD Toolbox chain), consumed by cycles / q_mapping / thrust via
            thin adapters; independent solvers are cross-checked in tests/

See validation/interface_audit.md for the pre-refactor audit that motivated
this package and the invariance policy for the blessed numbers.
"""
__all__ = ['constants', 'mixtures', 'cj_core']
