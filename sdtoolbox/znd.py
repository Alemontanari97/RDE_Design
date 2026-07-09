"""
SDToolbox 'znd' module (official, GALCIT FM2018.001, rev. Jan 2021).
Solves the ZND detonation-structure ODEs.
"""
import cantera as ct
import numpy as np
from sdtoolbox.thermo import soundspeed_fr
from scipy.integrate import solve_ivp


class ZNDSys(object):
    def __init__(self, gas, U1, r1):
        self.gas = gas
        self.U1 = U1
        self.r1 = r1

    def __call__(self, t, y):
        self.gas.DPY = y[1], y[0], y[3:]
        c = soundspeed_fr(self.gas)
        U = self.U1*self.r1/self.gas.density
        M = U/c
        eta = 1 - M**2
        sigmadot = getThermicity(self.gas)
        Pdot = -self.gas.density*U**2*sigmadot/eta
        rdot = -self.gas.density*sigmadot/eta
        dYdt = self.gas.net_production_rates*self.gas.molecular_weights/self.gas.density
        return np.hstack((Pdot, rdot, U, dYdt))


def getThermicity(gas):
    """Thermicity = sum( (W/Wi - hsi/(cp*T)) * dYi/dt )  [1/s]."""
    w = gas.molecular_weights
    hs = gas.standard_enthalpies_RT*ct.gas_constant*gas.T/w
    dydt = gas.net_production_rates*w/gas.density
    thermicity = sum((gas.mean_molecular_weight/w - hs/(gas.cp_mass*gas.T))*dydt)
    return thermicity


def getTempDeriv(gas, r1, U1):
    rx = gas.density
    U = U1*r1/rx
    M = U/soundspeed_fr(gas)
    eta = 1 - M**2
    DTDt = gas.T*((1-gas.cp/gas.cv*M**2)*getThermicity(gas)/eta
                  - gas.mean_molecular_weight*sum(gas.net_production_rates)/rx)
    return DTDt


def zndsolve(gas, gas1, U1, t_end=1e-3, max_step=1e-4, t_eval=None,
             relTol=1e-5, absTol=1e-8, advanced_output=False, Method='LSODA'):
    """Solve the ZND ODEs. Returns dict with time, distance, T, P, rho, U,
    thermicity, species, M, af, g, wt, sonic, and (advanced) induction/exothermic lengths."""
    r1 = gas1.density
    x_start = 0.
    y0 = np.hstack((gas.P, gas.density, x_start, gas.Y))
    tel = [0., t_end]
    output = {}
    out = solve_ivp(ZNDSys(gas, U1, r1), tel, y0, method=Method,
                    atol=absTol, rtol=relTol, max_step=max_step, t_eval=t_eval)
    output['time'] = out.t
    output['P'] = out.y[0, :]
    output['rho'] = out.y[1, :]
    output['distance'] = out.y[2, :]
    output['species'] = out.y[3:, :]
    output['tfinal'] = t_end
    output['xfinal'] = output['distance'][-1]
    b = len(output['time'])
    for k in ['T', 'U', 'thermicity', 'af', 'g', 'wt', 'dTdt']:
        output[k] = np.zeros(b)
    for i, P in enumerate(output['P']):
        gas.DPY = output['rho'][i], P, output['species'][:, i]
        af = soundspeed_fr(gas)
        U = U1*r1/gas.density
        output['T'][i] = gas.T
        output['U'][i] = U
        output['thermicity'][i] = getThermicity(gas)
        output['af'][i] = af
        output['g'][i] = gas.cp/gas.cv
        output['wt'][i] = gas.mean_molecular_weight
        output['dTdt'][i] = getTempDeriv(gas, r1, U1)
    output['M'] = output['U']/output['af']
    eta = 1 - output['M']**2
    output['sonic'] = eta*output['af']**2
    if advanced_output:
        n = output['thermicity'].argmax()
        output['ind_time_ZND'] = output['time'][n]
        output['ind_len_ZND'] = output['distance'][n]
        output['max_thermicity_ZND'] = max(output['thermicity'])
        max_sigmadot = max(output['thermicity'])
        f1 = f2 = 0; tstep1 = 0; tstep2 = 0
        for j, th in enumerate(list(output['thermicity'])):
            if f1 == 0:
                if th > 0.5*max_sigmadot:
                    f1 = 1; tstep1 = j
            elif f2 == 0:
                if th < 0.5*max_sigmadot:
                    f2 = 1; tstep2 = j
                else:
                    tstep2 = 0
        if tstep2 == 0:
            output['exo_time_ZND'] = 0; output['exo_len_ZND'] = 0
        else:
            output['exo_time_ZND'] = output['time'][tstep2] - output['time'][tstep1]
            output['exo_len_ZND'] = output['distance'][tstep2] - output['distance'][tstep1]
    output['gas1'] = gas1
    output['U1'] = U1
    return output
