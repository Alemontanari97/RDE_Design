"""SDToolbox thermo module (official) - soundspeed_eq (TP method, identical to April 2026 release), eq_state, state; soundspeed_fr patched to Cantera analytic gas.sound_speed (equivalence vs official FD: 6-10e-5, ZND impact <=0.02%; see validation/sdt_official_audit.md)."""
import numpy as np

def soundspeed_eq(gas):
    T0 = gas.T; P0 = gas.P; x0 = gas.X
    T2 = 1.01*T0; T1 = 0.99*T0
    gas.TP = T1, P0; gas.equilibrate('TP'); s1 = gas.entropy_mass
    gas.TP = T2, P0; gas.equilibrate('TP'); s2 = gas.entropy_mass
    DSDT = (s2 - s1)/(T2 - T1)
    P1 = 0.99*P0; P2 = 1.01*P0
    gas.TP = T0, P1; gas.equilibrate('TP'); s1 = gas.entropy_mass
    gas.TP = T0, P2; gas.equilibrate('TP'); s2 = gas.entropy_mass
    DSDP = (s2 - s1)/(P2 - P1); DTDP = -DSDP/DSDT
    TA = T0 + DTDP*(P1-P0); gas.TP = TA, P1; gas.equilibrate('TP'); rhoA = gas.density
    TB = T0 + DTDP*(P2-P0); gas.TP = TB, P2; gas.equilibrate('TP'); rhoB = gas.density
    DRHODP = (P2-P1)/(rhoB-rhoA); ae = np.sqrt(DRHODP)
    gas.TPX = T0, P0, x0
    return ae

def soundspeed_fr(gas):
    # Frozen (fixed-composition) sound speed. For an ideal-gas mixture this equals
    # Cantera's built-in gas.sound_speed = sqrt(gamma*R*T/W) exactly, but is ~100x
    # faster than the SVX finite-difference below (used in the reference SDToolbox).
    return gas.sound_speed

def _soundspeed_fr_fd(gas):
    rho0 = gas.density; p0 = gas.P; s0 = gas.entropy_mass
    rho1 = 1.001*rho0; x0 = gas.X
    if gas.n_species > 1:
        gas.SVX = s0, 1./rho1, x0
    else:
        gas.SV = s0, 1./rho1
    p1 = gas.P
    dpdrho_s = (p1 - p0)/(rho1 - rho0); afrz = np.sqrt(dpdrho_s)
    if gas.n_species > 1:
        gas.SVX = s0, 1./rho0, x0
    else:
        gas.SV = s0, 1./rho0
    return afrz

def eq_state(gas,r1,T1):
    gas.TD = T1,r1; gas.equilibrate('TV')
    return [gas.P, gas.enthalpy_mass]

def state(gas,r1,T1):
    gas.TD = T1,r1
    return [gas.P, gas.enthalpy_mass]
