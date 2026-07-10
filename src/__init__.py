"""Lecture source package — detonation thermodynamics and RDE performance.

Use it as a library with the repo root on sys.path (any of: run Python from
the repo root, `sys.path.insert(0, <repo root>)`, or PYTHONPATH):

    from src.detonation.cj_states import CJ_state, vN_state
    from src.thrust.sk_models import cj_calc, ph_calc, axial_calc, stech_calc
    from src.thrust import stechmann_nozzle as stn
    from src.cycles.cycles import three_cycles, cj_mach, eta_fj_1g

Subpackages
-----------
detonation : CJ & von Neumann states, ZND profiles, CJ parameter sweeps
cycles     : Wintenberger–Shepherd cycle analysis, heat-release mapping
thrust     : Shepherd–Kasahara + Stechmann thrust models, tables, V&V

Modules insert the repo root into sys.path at import time, so the vendored
`sdtoolbox/` resolves regardless of the caller's cwd.  Importing never runs
the pipelines or writes files; only the CLI stages do
(`python src/<pkg>/<module>.py <stage>`, see the top-level README).
End-to-end usage: `examples/example_design_study.py`.
"""
__all__ = ['cycles', 'detonation', 'thrust']
