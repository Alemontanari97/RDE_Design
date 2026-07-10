"""CJ & von Neumann states, ZND reaction-zone profiles, CJ parameter sweeps.

cj_states    : standalone equilibrium-Hugoniot CJ solver + frozen vN jump
               (validated vs Shepherd & Kasahara FM2017.001 Table 2)
znd_profiles : full ZND pipeline (CJspeed -> PostShock_fr -> zndsolve)
cj_sweeps    : U_CJ, p_CJ, T_CJ vs phi, N2 dilution, P1, T1 (resumable)
"""
__all__ = ['cj_states', 'cj_sweeps', 'znd_profiles']
