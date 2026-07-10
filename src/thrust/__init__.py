"""Analytical RDE thrust and nozzle-performance models.

sk_models        : Shepherd–Kasahara pressure-history (`ph_calc`) and
                   axial-flow (`axial_calc`, chem='eq'|'frozen') models from
                   a CJ record (`cj_calc`); Stechmann blowdown (`stech_calc`)
st_core          : Stechmann model core (c*, CF closures, blowdown means)
stechmann_nozzle : matched det/CP chamber states and bell/aerospike
                   area-ratio optimization (18/18 vs Table 1)
tables           : thrust tables + the 8 V&V verdicts (script)
"""
__all__ = ['sk_models', 'st_core', 'stechmann_nozzle', 'tables']
