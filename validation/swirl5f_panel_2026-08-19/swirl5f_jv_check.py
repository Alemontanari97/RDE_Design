"""Independent judge-verification algebra (adversarial convergence round).
Items: (1) chi adjudication + closures; (2) sonic-exit Cramer/kernel;
(3) D(W)==div-form K dictionary; (4) azimuthal-march degeneracy loci.
All checks are self-derived BEFORE reading the judge's fused text.
"""
import sympy as sp

ok = []
def check(name, cond):
    ok.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ---------------------------------------------------------------- item 1
# Symbols
r, w, u, v, c, rho, p, h, h0, gam, Om, ut = sp.symbols(
    'r w u v c rho p h h0 gamma Omega u_theta', positive=True)
Gamma = r*ut                     # swirl invariant with u_theta the azimuthal vel
eps = ut/(Om*r)                  # eps_theta
MOm = Om*r/c                     # wheel Mach
# (1a) chi = Omega*Gamma/h0 ; identity chi = eps*MOm^2*(gam-1)*h/h0 under c^2=(gam-1)h
chi = Om*Gamma/h0
chi_id1 = eps*MOm**2*(gam-1)*h/h0
check("chi == eps*MOm^2*(gam-1)*h/h0 under c^2=(gam-1)h",
      sp.simplify(chi.subs(c, sp.sqrt((gam-1)*h)) - chi_id1.subs(c, sp.sqrt((gam-1)*h))) == 0)
# (1b) KE-normalized reading: chi = (2 f_theta / eps) * (KE/h0), f_theta = ut^2/q^2, KE=q^2/2
q = sp.symbols('q', positive=True)
f_th = ut**2/q**2
KE = q**2/2
chi_id2 = (2*f_th/eps)*(KE/h0)
check("chi == (2 f_theta/eps)*(KE/h0)  [exact, EOS-free]",
      sp.simplify(chi - chi_id2) == 0)
# => the pde-doc's 0.3-0.8 evaluation of (2 f_KE)/eps_theta implicitly set KE/h0 = 1.
# (1c) closure chi*beta_tau = beta_w EXACT from definitions (EOS-free):
beta_tau = p/(rho*Om*r*ut)
beta_w   = p/(rho*h0)
check("chi*beta_tau == beta_w  EXACT (definition-level, EOS-free)",
      sp.simplify(chi*beta_tau - beta_w) == 0)
# (1d) numbers: discriminating test via wheel speed
import itertools
# wheel speed OmR = MOm*c, c=1100-1300, MOm=1.5-2.5 -> 1650-3250 m/s (record 1800-3200 claimed)
print("wheel speed range:", 1.5*1100, "to", 2.5*1300)
# chi numeric via physical numbers: OmR=2000-2500 (D_CJ), eps=0.15-0.2, h ~ c^2/(gam-1)
vals = []
for OmR in (1800., 2000., 2500., 3200.):
    for e_ in (0.15, 0.2):
        for c_ in (1100., 1300.):
            for g_ in (1.15, 1.25):
                for hr in (0.7, 0.8):   # h/h0
                    h_ = c_**2/(g_-1); h0_ = h_/hr
                    vals.append(e_*OmR**2/h0_)
print("chi physical range: %.3f - %.3f" % (min(vals), max(vals)))
# a_p*St_n*beta_w
bw = []
for g_ in (1.15, 1.25):
    for hr in (0.7, 0.8):
        bw.append((g_-1)/g_*hr)
print("beta_w range: %.3f - %.3f" % (min(bw), max(bw)))
print("a_p*St_n*beta_w range: %.4f - %.4f" % (0.7*0.1*min(bw), 0.7*1.0*max(bw)))
# (1e) spike-core bound: r_core/R_int = Gamma_tip / (R sqrt(2(h0-hmin-qm^2/2)))
#   with Gamma_tip = R*ut_int and ut_int^2 = 2 f_theta KE_int:
R, hmin, qm = sp.symbols('R h_min q_m', positive=True)
rcore = (R*ut)/sp.sqrt(2*(h0-hmin-qm**2/2))
ratio = rcore/R
ratio_f = sp.sqrt(f_th*KE/(h0-hmin-qm**2/2))
check("r_core/R == sqrt(f_theta*KE_int/(h0-hmin-qm^2/2))  [numerator f*KE, NOT f*h0]",
      sp.simplify(ratio**2 - ratio_f**2) == 0)
# lower bound when denominator <= h0: r_core/R >= sqrt(f_theta*KE_int/h0)
nums = []
for f_ in (0.03, 0.06):
    for keh in (0.13, 0.30, 0.47, 0.6):  # KE/h0 at interface..near-exit Mach
        nums.append((f_, keh, (f_*keh)**0.5))
print("sqrt(f*KE/h0) samples:", [(a, b, round(x,3)) for a,b,x in nums])

# ---------------------------------------------------------------- item 2
# Exit-datum system (var-doc r-weighted convention), n = e_x on S_e:
# BT coeffs matched to dJ integrand r(u^2 drho + 2 rho u du + dp):
p1,p2,p3,p4,p5 = sp.symbols('psi1 psi2 psi3 psi4 psi5')
eqs = [sp.Eq(p1*u - c**2*u*p5, u**2),      # drho
       sp.Eq(rho*p1 + rho*u*p2, 2*rho*u),  # du
       sp.Eq(rho*u*p3, 0),                 # dv
       sp.Eq(rho*u*p4, 0),                 # dw
       sp.Eq(p2 + u*p5, 1)]                # dp
A_mat, b_vec = sp.linear_eq_to_matrix(eqs, [p1,p2,p3,p4,p5])
det = sp.factor(A_mat.det())
print("system det =", det)
# Cramer numerator for psi5:
A5 = A_mat.copy(); A5[:,4] = b_vec
num5 = sp.simplify(A5.det())
check("Cramer numerator for psi5 == 0 identically (exact-zero RHS)", num5 == 0)
sol = sp.solve(eqs, [p1,p2,p3,p4,p5], dict=True)
print("generic solution:", sol)
check("generic solution == (u,1,0,0,0)",
      sol and all(sp.simplify(sol[0][s]-t)==0 for s,t in
                  zip([p1,p2,p3,p4,p5],[u,1,0,0,0])))
# consistency AT u=c: substitute u=c, solution (c,1,0,0,0) must satisfy all eqs
subs_sonic = {u:c, p1:c, p2:1, p3:0, p4:0, p5:0}
check("(u,1,0,0,0) still solves the system at u=c (no blow-up: consistent, rank-deficient)",
      all(sp.simplify(e.lhs.subs(subs_sonic)-e.rhs.subs(subs_sonic))==0 for e in eqs))
# kernel at u=c:
Ah = A_mat.subs(u, c)
ns = Ah.nullspace()
print("kernel at u=c:", [sp.simplify(sp.nsimplify(vv.T)) for vv in ns])
kv = ns[0]/ns[0][4]
check("kernel direction == (c^2, -c, 0, 0, 1)",
      all(sp.simplify(kv[i]-t)==0 for i,t in enumerate([c**2,-c,0,0,1])))
# dictionary vs record terminal gauge l(e_x) = (1, -r/c, 0, 0, r/c^2) carrier conv.
# here-conv: psi_i = psi_i^carrier / r (i=2..5), psi_1 same -> (1, -1/c, 0, 0, 1/c^2)
l_here = sp.Matrix([1, -1/c, 0, 0, 1/c**2])
check("kernel direction parallel to dictionary-mapped terminal gauge l(e_x)",
      sp.simplify(sp.Matrix([kv[i]-c**2*l_here[i] for i in range(5)]).norm()) == 0)

# ---------------------------------------------------------------- item 3
# D(W) = (1/r) d_phi[F_theta(U) - Omega r U] vs div-form K rows (1/r) d_phi F_phi_rel
E, w_rel = sp.symbols('E w_rel', positive=True)
h0e = E + p/rho                    # h0 = E + p/rho
U  = sp.Matrix([rho, rho*u, rho*v, rho*Gamma.subs(ut,w), rho*E])
Fth = sp.Matrix([rho*w, rho*u*w, rho*v*w, rho*w*(r*w)+r*p, (rho*E+p)*w])
Frel_claim = sp.Matrix([rho*(w-Om*r), rho*u*(w-Om*r), rho*v*(w-Om*r),
                        rho*(w-Om*r)*(r*w)+r*p, rho*(w-Om*r)*h0e + Om*r*p])
diff = sp.simplify(Fth - Om*r*U - Frel_claim)
check("F_theta(U) - Omega r U == F_phi,rel row-for-row (operator dictionary EXACT)",
      diff == sp.zeros(5,1))
# K-bar fiberwise: total mass of D(f) on the circle for periodic BV f is 0,
# atoms included: Df((phi0,phi0+2pi]) = f(phi0+) - f(phi0+) = 0.  (principle;
# numeric witness with a jump + smooth part)
import numpy as np
phis = np.linspace(0, 2*np.pi, 200001)
f = np.sin(3*phis) + np.where((phis>1.0)&(phis<4.0), 1.7, 0.0)   # BV, 2 atoms
# total distributional-derivative mass = f(2pi)-f(0) (periodic rep) == 0
mass = (f[-1]-f[0])
check("numeric witness: total d_phi mass over circle == 0 with atoms (BV periodic)",
      abs(mass) < 1e-12)

# ---------------------------------------------------------------- item 4
# 3-D symbol on the leaf theta'=const: zeta = e_theta
zx, zr, zt = sp.symbols('zeta_x zeta_r zeta_theta')
wvec_dot = u*zx + v*zr + w_rel*zt
detsym = wvec_dot**3*(wvec_dot**2 - c**2*(zx**2+zr**2+zt**2))
d_leaf = detsym.subs({zx:0, zr:0, zt:1})
print("leaf symbol det factor:", sp.factor(d_leaf))
check("leaf char. degeneracies exactly {w_rel=0} (advective) and {|w_rel|=c} (acoustic)",
      sp.factor(d_leaf) == w_rel**3*(w_rel**2-c**2))
# dependence-arc bracket sanity (numbers, record class): C_geo upper bound
for (W_, u_, c_) in [(2.0,1.5,1.0),(1.2,1.2,1.0),(2.1,2.0,1.0)]:
    upper = (1+c_/W_)*u_/(u_-c_)
    # max acoustic winding / advective winding:
    ratio = ((W_+c_)/(u_-c_)) / (W_/u_)
    print("W=%.1f u=%.1f: upper=%.2f ratio(max/adv)=%.2f (must be <= upper)" %
          (W_, u_, upper, ratio), "OK" if ratio <= upper + 1e-12 else "VIOLATION")

print()
print("ALL:", all(c for _, c in ok), "-", sum(1 for _,c in ok if c), "/", len(ok))
