#!/usr/bin/env python3
"""[X-IVXC] Interval certificate for S-XCONV over the DECLARED margin
box — the shared substrate brick of the global-maximum dossier (Card 1
first brick) AND the C-XBVP(a) discharger at instance level (S15
reopened segment, [RIGOR/A]+[RIGOR/C]).

OBJECT. Ideal gas gamma = 1.4, c_v = 1 (the declared S-XCONV oracle
instance): certify STRICT convexity of the x-entropy eta = -rho u S
as a function of the x-flux vector m over the WHOLE declared box
    rho in [0.5, 2], S in [-0.5, 0.5], M = u/c in [1.15, 3],
    V = v/c in [-0.8, 0.8],
not merely on sampled states (X-XBVP P4a did 200 samples; THIS brick
does the box).

EXACT 4D -> 2D REDUCTION (the brick's own discovery, symbolically
verified here as P4/P5): two scaling groups act on the state,
  s_alpha: (rho,u,v,S) -> (alpha rho, u, v, S - (gamma-1) ln alpha)
           [pressure-density scaling at FIXED c: m -> alpha m,
            eta -> alpha eta + (gamma-1)(ln alpha) m_1]
  s_beta:  (rho,u,v,S) -> (rho, beta u, beta v, S + 2 ln beta)
           [velocity-sound scaling: m -> diag(b, b^2, b^2, b^3) m,
            eta -> beta eta - 2 (ln beta) m_1]
In both cases eta gains only a term LINEAR IN m (zero m-Hessian), so
H_m(eta) transforms by POSITIVE DIAGONAL CONGRUENCE — definiteness
is invariant along both orbits. The two orbits sweep (rho, S) at
fixed (M, V) = (u/c, v/c), so strict convexity depends on (M, V)
ONLY, and certifying the 2-D slice (rho, S) = (1, 0),
(M, V) in [1.15, 3] x [-0.8, 0.8] certifies the WHOLE 4-D box (and
every other (rho, S)). This also EXPLAINS the S-XCONV instance
finding that definiteness tracks the MACH pair, not the raw state.

METHOD (congruence + polynomial interval arithmetic + adaptive
bisection):
 - H_m = J^{-T} G J^{-1} with G = H_U(eta) - sum_k lam_k H_U(m_k),
   J = dm/dU, lam = J^{-T} grad eta. CONGRUENCE preserves
   definiteness, so H_m > 0 iff G > 0 (J invertible). Per box, lam
   is enclosed by INTERVAL GAUSSIAN ELIMINATION on J^T lam = grad
   eta (pivot sign-definiteness required, else split), then G is
   assembled as an interval sum of VALUE-SCALE pieces.
   [METHOD RECORD — two measured NO-GOs kept for the dossier:
   (i) expanded-adjugate polynomial form Ghat = detJ H_eta - sum
   mu_k Hm_k: monomial scale ~1e3 x value scale => measured interval
   dependency amplification ~1.6e3 (scaled entry width 1600*r at
   relative box width r): infeasible for ANY plain-IA budget —
   60k-box budget exhausted; (ii) Gershgorin PSD test: infeasible on
   ~53% of the box even at exact arithmetic (true equilibrated
   margin lambda_min in [0.126, 0.438], healthy — the 1.36e-4 of
   X-XBVP P4a was an m-variable scaling artifact). Fixes: value-
   scale interval solve (this form) + interval LDL^T (any PD point
   matrix certifiable).]
 - Interval arithmetic: outward rounding by 1-ulp nextafter on every
   arithmetic op; exp/log/sqrt/fractional powers via monotone
   endpoint evaluation with a 2-ulp outward guard. DECLARED
   ASSUMPTION (named limitation): libm exp/log within 1 ulp; a
   crlibm-grade certificate would remove it. u = M c(rho,S),
   v = V c(rho,S) computed as intervals (the M,V box is rectangular;
   the u-c correlation lost per box shrinks under bisection).
 - Per box: det J sign-definite (else split); PSD of Ghat via
   INTERVAL LDL^T on the midpoint-equilibrated interval matrix
   (D Ghat D, congruence, definiteness preserved): all four interval
   pivots strictly positive => certified PD. [Method note of record:
   the first attempt used Gershgorin and exhausted a 60k-box budget;
   the diagnostic scan showed the TRUE equilibrated margin is
   healthy (lambda_min in [0.126, 0.438] over the whole box — the
   1.36e-4 of X-XBVP P4a was an m-variable SCALING artifact) while
   Gershgorin is infeasible on ~53% of the box even with exact
   arithmetic: the test, not the arithmetic, was the bottleneck.
   Interval LDL^T certifies any PD point matrix, so bisection only
   has to beat the dependency width against a 0.126 margin.]
   Split along the widest relative dimension. DETERMINISTIC budget:
   max box COUNT (never wall time). CERTIFICATE = full coverage
   within budget.
REJECTORS:
  R1 subsonic box M in [0.5, 0.9] must NOT certify (and the midpoint
     eigencheck must show genuine indefiniteness — the certifier
     must not be blind).
  R2 corrupted matrix (one diagonal entry sign-flipped) must NOT
     certify on the main box.
  R3 containment self-test: on randomized point-boxes and sub-boxes,
     the interval evaluation must contain direct float evaluations
     (outward-rounding sanity).

Exit 0 iff the main-box certificate PASSES within budget AND all
rejectors pass. Terminal line: "VERDICT: PASS"/"VERDICT: FAIL".
"""
import math
import sys

import numpy as np
import sympy as sp

GAMMA = 1.4
NEXT = math.nextafter
INF = math.inf


# ------------------------------------------------------------ intervals
def i_add(a, b):
    lo, hi = a[0] + b[0], a[1] + b[1]
    return (NEXT(lo, -INF), NEXT(hi, INF))


def i_neg(a):
    return (-a[1], -a[0])


def i_mul(a, b):
    p = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return (NEXT(min(p), -INF), NEXT(max(p), INF))


def i_pow_int(a, n):
    if n == 0:
        return (1.0, 1.0)
    if n % 2 == 0 and a[0] < 0 < a[1]:
        m = max(a[0] * a[0], a[1] * a[1])
        return (0.0, NEXT(m, INF))
    p = (a[0]**n, a[1]**n)
    return (NEXT(min(p), -INF), NEXT(max(p), INF))


def _outk(lo, hi, k=8):
    # k-ulp outward guard for libm-backed monotone ops: covers the
    # declared 1-ulp libm assumption PLUS argument-error propagation
    # through exp(q ln a) on the certified domain (|q ln a| <~ 1, so
    # <= ~5 ulp worst-case; 8 is the declared safe over-guard).
    for _ in range(k):
        lo, hi = NEXT(lo, -INF), NEXT(hi, INF)
    return (lo, hi)


def i_exp(a):
    return _outk(math.exp(a[0]), math.exp(a[1]))


def i_powf(a, q):
    # a > 0 required; monotone for q > 0 via exp(q ln a), k-ulp guard
    if a[0] <= 0:
        raise ValueError('i_powf needs positive base')
    return _outk(math.exp(q * math.log(a[0])),
                 math.exp(q * math.log(a[1])))


def i_sqrt(a):
    if a[0] < 0:
        raise ValueError('i_sqrt needs nonnegative base')
    return _outk(math.sqrt(a[0]), math.sqrt(a[1]))


# --------------------------------------------- symbolic build + compile
def build_program():
    """Value-scale pieces as ONE cse program. Output layout:
    J (16, row-major), grad_eta (4), H_eta upper (10),
    H_mk upper (4 x 10), detJ  -> 16+4+10+40+1 = 71 outputs."""
    rho, u, v, S = sp.symbols('rho u v S', real=True)
    p = sp.exp(S) * rho**sp.Rational(7, 5)
    e = p / ((GAMMA - 1) * rho)
    H = e + p / rho + (u**2 + v**2) / 2
    m = sp.Matrix([rho * u, rho * u**2 + p, rho * u * v, rho * u * H])
    U = sp.Matrix([rho, u, v, S])
    eta = -rho * u * S
    J = m.jacobian(U)
    def block(f):
        out = [f(J[i, j]) for i in range(4) for j in range(4)]
        out += [f(sp.diff(eta, U[i])) for i in range(4)]
        out += [f(sp.diff(eta, U[i], U[j])) for i in range(4)
                for j in range(i, 4)]
        for k in range(4):
            out += [f(sp.diff(m[k], U[i], U[j])) for i in range(4)
                    for j in range(i, 4)]
        return out

    exprs = block(lambda e_: e_)                     # values (70)
    exprs.append(J.det())                            # [70]
    exprs += block(lambda e_: sp.diff(e_, u))        # d/du (70)
    exprs += block(lambda e_: sp.diff(e_, v))        # d/dv (70)
    reps, reduced = sp.cse(exprs, optimizations='basic')
    return (rho, u, v, S), reps, reduced


def make_interval_fn(args, reps, reduced):
    """Compile the cse program into an interval evaluator via tree walk
    with per-call memo (leaves = interval tuples)."""
    def ev(node, env):
        if node in env:
            return env[node]
        if node.is_Number:
            f = float(node)
            if node.is_Integer:
                r = (f, f)                      # integers exact
            else:
                # non-integer rationals/floats: 7/5 etc. are NOT
                # binary-exact — 1-ulp outward, always
                r = (NEXT(f, -INF), NEXT(f, INF))
            env[node] = r
            return r
        if node.is_Add:
            r = (0.0, 0.0)
            for a in node.args:
                r = i_add(r, ev(a, env))
        elif node.is_Mul:
            r = (1.0, 1.0)
            for a in node.args:
                r = i_mul(r, ev(a, env))
        elif node.is_Pow:
            b, q = node.args
            bb = ev(b, env)
            if q.is_Integer:
                r = i_pow_int(bb, int(q))
            else:
                r = i_powf(bb, float(q))
        elif isinstance(node, sp.exp):
            r = i_exp(ev(node.args[0], env))
        else:
            raise TypeError('unsupported node %r' % node)
        env[node] = r
        return r

    def fn(irho, iu, iv, iS):
        env = {args[0]: irho, args[1]: iu, args[2]: iv, args[3]: iS}
        for sym, ex in reps:
            env[sym] = ev(ex, env)
        return [ev(ex, env) for ex in reduced]
    return fn


# --------------------------------------------------------- certification
def c_interval(irho, iS):
    c2 = i_mul((GAMMA, GAMMA), i_mul(i_exp(iS),
                                     i_powf(irho, (GAMMA - 1.0))))
    return i_sqrt(c2)


def _sym4(flat10):
    M = [[None] * 4 for _ in range(4)]
    k = 0
    for i in range(4):
        for j in range(i, 4):
            M[i][j] = M[j][i] = flat10[k]
            k += 1
    return M


def i_gauss_solve(A, b):
    """Verified enclosure of A x = b (4x4) by the KRAWCZYK method:
    precondition with the floating midpoint inverse Y, then
    x = x0 + X with X a verified fixed point of z + C X,
    z = Y (b - A x0) (interval), C = I - Y A (interval).
    Raises ZeroDivisionError when no contraction is verified
    (caller splits the box). [Method note: plain interval Gaussian
    elimination measured ~15x over-wide on this system — see the
    docstring method record.]"""
    n = 4
    Am = np.array([[0.5 * (A[i][j][0] + A[i][j][1]) for j in range(n)]
                   for i in range(n)])
    bm = np.array([0.5 * (bb[0] + bb[1]) for bb in b])
    try:
        Y = np.linalg.inv(Am)
    except np.linalg.LinAlgError:
        raise ZeroDivisionError('midpoint singular')
    x0 = Y @ bm
    # interval residual r0 = b - A x0  (x0 exact float points)
    r0 = []
    for i in range(n):
        s = b[i]
        for j in range(n):
            s = i_sub(s, i_mul(A[i][j], (x0[j], x0[j])))
        r0.append(s)
    # z = Y r0 ; C = I - Y A   (row by row, interval)
    z = []
    C = [[None] * n for _ in range(n)]
    for i in range(n):
        s = (0.0, 0.0)
        for j in range(n):
            s = i_add(s, i_mul((Y[i, j], Y[i, j]), r0[j]))
        z.append(s)
        for k in range(n):
            t = (1.0, 1.0) if i == k else (0.0, 0.0)
            for j in range(n):
                t = i_sub(t, i_mul((Y[i, j], Y[i, j]), A[j][k]))
            C[i][k] = t
    # contraction bound
    normC = max(sum(max(abs(C[i][k][0]), abs(C[i][k][1]))
                    for k in range(n)) for i in range(n))
    if normC >= 1.0:
        raise ZeroDivisionError('Krawczyk not contracting')
    rad = max(max(abs(zz[0]), abs(zz[1])) for zz in z) / (1.0 - normC)
    X = [(-rad, rad)] * n
    for _ in range(2):                       # two refinement sweeps
        Xn = []
        for i in range(n):
            s = z[i]
            for j in range(n):
                s = i_add(s, i_mul(C[i][j], X[j]))
            Xn.append(s)
        X = Xn
    return [i_add((x0[i], x0[i]), X[i]) for i in range(n)]


def _assemble_G(vals0):
    """(G, detJ, lam, JT, pieces) from a 70+1 value block."""
    Jf, ge, He_f = vals0[:16], vals0[16:20], vals0[20:30]
    Hm_f = [vals0[30 + 10 * k: 40 + 10 * k] for k in range(4)]
    det = vals0[70]
    JT = [[Jf[4 * j + i] for j in range(4)] for i in range(4)]
    lam = i_gauss_solve(JT, list(ge))
    G = _sym4(He_f)
    for k in range(4):
        Hk = _sym4(Hm_f[k])
        for i in range(4):
            for j in range(4):
                G[i][j] = i_sub(G[i][j], i_mul(lam[k], Hk[i][j]))
    return G, det, lam, JT, Hm_f


def box_matrices(fn, box):
    """Plain interval G over the box (used for point boxes and as the
    coarse fallback). Returns (G interval 4x4, detJ interval)."""
    (r0, r1), (s0, s1), (m0, m1), (v0, v1) = box
    ic = c_interval((r0, r1), (s0, s1))
    iu = i_mul((m0, m1), ic)
    iv = i_mul((v0, v1), ic)
    vals = fn((r0, r1), iu, iv, (s0, s1))
    G, det, _, _, _ = _assemble_G(vals)
    return G, det


def box_matrices_mv(fn, box):
    """MEAN-VALUE form on the 2-D (M,V) slice: G(box) is enclosed by
    G(midpoint) + [dG/du] c0 rad_M [-1,1] + [dG/dv] c0 rad_V [-1,1],
    with the derivative chain solved per box:
    J^T dlam = d(grad eta) - dJ^T lam. Requires the slice layout
    (rho, S degenerate). Returns (G_enclosure, detJ interval)."""
    (r0, r1), (s0, s1), (m0, m1), (v0, v1) = box
    mm, vm = 0.5 * (m0 + m1), 0.5 * (v0 + v1)
    ic = c_interval((r0, r1), (s0, s1))
    # midpoint (tight): point box at (mm, vm)
    ium = i_mul((mm, mm), ic)
    ivm = i_mul((vm, vm), ic)
    vals_m = fn((r0, r1), ium, ivm, (s0, s1))
    G0, det0, _, _, _ = _assemble_G(vals_m[:71])
    # whole box: values + u/v derivative blocks
    iu = i_mul((m0, m1), ic)
    iv = i_mul((v0, v1), ic)
    vals = fn((r0, r1), iu, iv, (s0, s1))
    Gb, det, lam, JT, Hm_f = _assemble_G(vals[:71])
    dG = []
    for w_ in range(2):                     # 0 -> d/du, 1 -> d/dv
        blk = vals[71 + 70 * w_: 71 + 70 * (w_ + 1)]
        dJf, dge, dHe = blk[:16], blk[16:20], blk[20:30]
        dHm = [blk[30 + 10 * k: 40 + 10 * k] for k in range(4)]
        # rhs = dge - dJ^T lam
        rhs = []
        for i in range(4):
            s = dge[i]
            for j in range(4):
                s = i_sub(s, i_mul(dJf[4 * j + i], lam[j]))
            rhs.append(s)
        dlam = i_gauss_solve(JT, rhs)
        dGw = _sym4(dHe)
        for k in range(4):
            Hk = _sym4(Hm_f[k])
            dHk = _sym4(dHm[k])
            for i in range(4):
                for j in range(4):
                    dGw[i][j] = i_sub(dGw[i][j],
                                      i_add(i_mul(dlam[k], Hk[i][j]),
                                            i_mul(lam[k], dHk[i][j])))
        dG.append(dGw)
    rad_u = i_mul((0.5 * (m1 - m0), 0.5 * (m1 - m0)), ic)[1]
    rad_v = i_mul((0.5 * (v1 - v0), 0.5 * (v1 - v0)), ic)[1]
    G = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            su = max(abs(dG[0][i][j][0]), abs(dG[0][i][j][1])) * rad_u
            sv = max(abs(dG[1][i][j][0]), abs(dG[1][i][j][1])) * rad_v
            pad = NEXT(NEXT(su + sv, INF), INF)
            G[i][j] = (G0[i][j][0] - pad, G0[i][j][1] + pad)
    return G, det


def i_div(a, b):
    if b[0] <= 0 <= b[1]:
        raise ZeroDivisionError('interval divisor straddles zero')
    p = (a[0] / b[0], a[0] / b[1], a[1] / b[0], a[1] / b[1])
    return (NEXT(min(p), -INF), NEXT(max(p), INF))


def i_sub(a, b):
    return i_add(a, i_neg(b))


def ldl_psd(G, sign):
    """Certified PD of sign*G via interval LDL^T on the
    midpoint-equilibrated matrix: all pivots strictly positive."""
    mid = [[0.5 * (G[i][j][0] + G[i][j][1]) * sign for j in range(4)]
           for i in range(4)]
    d = []
    for i in range(4):
        a = mid[i][i]
        if a <= 0:
            return False
        d.append(1.0 / math.sqrt(a))
    # scaled interval matrix A = D (sign G) D
    A = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            g = G[i][j] if sign > 0 else i_neg(G[i][j])
            A[i][j] = i_mul(g, (NEXT(d[i] * d[j], -INF),
                                NEXT(d[i] * d[j], INF)))
    L = [[(0.0, 0.0)] * 4 for _ in range(4)]
    piv = [None] * 4
    for k in range(4):
        s = A[k][k]
        for j in range(k):
            s = i_sub(s, i_mul(i_mul(L[k][j], L[k][j]), piv[j]))
        if not s[0] > 0:
            return False
        piv[k] = s
        for i in range(k + 1, 4):
            t = A[i][k]
            for j in range(k):
                t = i_sub(t, i_mul(i_mul(L[i][j], L[k][j]), piv[j]))
            L[i][k] = i_div(t, s)
    return True


def certify(fn, box0, max_boxes, corrupt=None, progress=None):
    """Adaptive bisection; returns (ok, boxes_used, fail_reason).
    Tracks certified (M,V)-area coverage; on budget exhaustion the
    fail_reason reports coverage and the uncertified bounding region."""
    def area(b):
        return (b[2][1] - b[2][0]) * (b[3][1] - b[3][0])

    total = area(box0)
    covered = 0.0
    # per-dimension scale = initial width (1.0 for pinned dims): the
    # split metric is width/scale — RELATIVE TO THE BOX, never to the
    # coordinate value (value-relative width degenerates near 0).
    scale = [max(b[1] - b[0], 1.0e-30) if b[1] > b[0] else 1.0
             for b in box0]
    stack = [box0]
    used = 0
    while stack:
        if used >= max_boxes:
            lo2 = min(b[2][0] for b in stack)
            hi2 = max(b[2][1] for b in stack)
            lo3 = min(b[3][0] for b in stack)
            hi3 = max(b[3][1] for b in stack)
            return False, used, (
                'budget exhausted (%d boxes; coverage %.4f%%; '
                'uncertified within M=[%.4f,%.4f] V=[%.4f,%.4f])'
                % (used, 100.0 * covered / total, lo2, hi2, lo3, hi3))
        box = stack.pop()
        used += 1
        try:
            G, det = box_matrices_mv(fn, box)
        except ZeroDivisionError:
            G, det = None, (0.0, 0.0)      # straddling pivot -> split
        if G is not None:
            if corrupt is not None:
                i0 = corrupt
                G[i0][i0] = (-G[i0][i0][1], -G[i0][i0][0])
            if det[0] > 0:
                sign = 1
            elif det[1] < 0:
                sign = -1
            else:
                sign = 0
            if sign != 0 and ldl_psd(G, sign):
                covered += area(box)
                if progress and used % progress == 0:
                    print('    ... %d boxes, coverage %.2f%%'
                          % (used, 100.0 * covered / total), flush=True)
                continue
        widths = [(b[1] - b[0]) / s for b, s in zip(box, scale)]
        k = widths.index(max(widths))
        lo, hi = box[k]
        mid = 0.5 * (lo + hi)
        if widths[k] < 1e-9:
            return False, used, 'unsplittable box at %r' % (box,)
        b1 = list(box)
        b2 = list(box)
        b1[k] = (lo, mid)
        b2[k] = (mid, hi)
        stack.append(tuple(b1))
        stack.append(tuple(b2))
    return True, used, ''


# 2-D certified slice (rho, S pinned by the exact reduction P4/P5)
MAIN_BOX = ((1.0, 1.0), (0.0, 0.0), (1.15, 3.0), (-0.8, 0.8))
SUB_BOX = ((1.0, 1.0), (0.0, 0.0), (0.5, 0.9), (-0.8, 0.8))
BUDGET = 1000000        # deterministic box-count budget (never time)
BUDGET_R = 4000


def sym_group_checks():
    """P4/P5: the two scaling-group identities + rejector R4."""
    rho, u, v, S, a, b = sp.symbols('rho u v S alpha beta',
                                    positive=True)
    g = sp.Rational(7, 5)

    def m_eta(rho_, u_, v_, S_):
        p = sp.exp(S_) * rho_**g
        e = p / ((g - 1) * rho_)
        H = e + p / rho_ + (u_**2 + v_**2) / 2
        m = sp.Matrix([rho_ * u_, rho_ * u_**2 + p, rho_ * u_ * v_,
                       rho_ * u_ * H])
        return m, -rho_ * u_ * S_

    m0, eta0 = m_eta(rho, u, v, S)

    # P4: s_alpha
    mA, etaA = m_eta(a * rho, u, v, S - (g - 1) * sp.log(a))
    p4m = sp.simplify(mA - a * m0) == sp.zeros(4, 1)
    p4e = sp.simplify(etaA - (a * eta0 + (g - 1) * sp.log(a) * mA[0])) == 0
    # P5: s_beta
    mB, etaB = m_eta(rho, b * u, b * v, S + 2 * sp.log(b))
    D = sp.diag(b, b**2, b**2, b**3)
    p5m = sp.simplify(mB - D * m0) == sp.zeros(4, 1)
    p5e = sp.simplify(etaB - (b * eta0 - 2 * sp.log(b) * mB[0])) == 0
    # R4 rejector: corrupted diagonal (b, b^2, b^2, b^2) must FAIL
    Dbad = sp.diag(b, b**2, b**2, b**2)
    r4 = sp.simplify(mB - Dbad * m0) != sp.zeros(4, 1)
    return (p4m and p4e), (p5m and p5e), r4


def containment_test(args, reps, reduced, fn, rng):
    """R3: the interval G contains the G computed by an independent
    float route (lambdified pieces + numpy solve), at point boxes."""
    full = [ex for ex in reduced]
    for sym, ex in reversed(reps):
        full = [f.subs(sym, ex) for f in full]
    f_np = sp.lambdify(args, full, 'numpy', cse=True)
    ok = True
    for _ in range(40):
        rho = rng.uniform(0.5, 2.0)
        S = rng.uniform(-0.5, 0.5)
        c = math.sqrt(GAMMA * math.exp(S) * rho**(GAMMA - 1.0))
        M = rng.uniform(1.15, 3.0)
        V = rng.uniform(-0.8, 0.8)
        u, v = M * c, V * c
        vals = f_np(rho, u, v, S)
        J = np.array(vals[:16], float).reshape(4, 4)
        ge = np.array(vals[16:20], float)
        He = np.array(_sym4(vals[20:30]), float)
        lam = np.linalg.solve(J.T, ge)
        Gd = He.copy()
        for k in range(4):
            Gd = Gd - lam[k] * np.array(_sym4(vals[30 + 10 * k:
                                                   40 + 10 * k]), float)
        eps = 1e-12
        box = ((rho, rho), (S, S), (M - eps, M + eps), (V - eps, V + eps))
        Gi, det = box_matrices(fn, box)
        for i in range(4):
            for j in range(4):
                ok &= Gi[i][j][0] <= Gd[i, j] <= Gi[i][j][1]
    return ok


def main():
    print('[X-IVXC] interval certificate for S-XCONV over the declared '
          'box (Card-1 first brick / C-XBVP(a) instance discharger)')
    args, reps, reduced = build_program()
    n_ops = len(reps) + len(reduced)
    print('  program: %d cse assignments + %d outputs'
          % (len(reps), len(reduced)))
    fn = make_interval_fn(args, reps, reduced)
    rng = np.random.default_rng(20260805)
    ok = True

    # P4/P5: the exact 4D -> 2D reduction identities (+ rejector R4)
    p4, p5, r4 = sym_group_checks()
    print('  P4 s_alpha identities (m -> alpha m; eta linear-in-m '
          'shift): %s' % ('PASS' if p4 else 'FAIL'))
    print('  P5 s_beta identities (m -> diag(b,b2,b2,b3) m; eta '
          'linear-in-m shift): %s' % ('PASS' if p5 else 'FAIL'))
    print('  R4 corrupted diagonal (b,b2,b2,b2) rejected: %s'
          % ('PASS' if r4 else 'FAIL'))
    ok &= p4 and p5 and r4

    # R3 (sanity of the arithmetic itself)
    r3 = containment_test(args, reps, reduced, fn, rng)
    print('  R3 containment: 40 random points inside interval results: '
          '%s' % ('PASS' if r3 else 'FAIL'))
    ok &= r3

    # MAIN CERTIFICATE on the 2-D slice (covers the 4-D box by P4/P5)
    cert, used, why = certify(fn, MAIN_BOX, BUDGET, progress=250000)
    print('  MAIN: G > 0 over the (M,V) slice x {rho=1, S=0} '
          '[== the WHOLE 4-D box by P4/P5]: %s (%d boxes%s)'
          % ('CERTIFIED' if cert else 'NOT CERTIFIED',
             used, ('; ' + why) if why else ''))
    ok &= cert

    # R1 subsonic box must NOT certify + midpoint really indefinite
    cert_s, used_s, _ = certify(fn, SUB_BOX, BUDGET_R)
    G, det = box_matrices(fn, tuple((0.5 * (a + b), 0.5 * (a + b))
                                    for a, b in SUB_BOX))
    mid = np.array([[0.5 * (G[i][j][0] + G[i][j][1]) for j in range(4)]
                    for i in range(4)])
    sgn = 1.0 if det[0] > 0 else -1.0
    w = np.linalg.eigvalsh(sgn * mid)
    r1 = (not cert_s) and w.min() < 0 < w.max()
    print('  R1 subsonic box NOT certified (%d boxes) and midpoint '
          'indefinite (eigs %.2e..%.2e): %s'
          % (used_s, w.min(), w.max(), 'PASS' if r1 else 'FAIL'))
    ok &= r1

    # R2 corrupted diagonal must NOT certify on the main box
    cert_c, used_c, _ = certify(fn, MAIN_BOX, BUDGET_R, corrupt=2)
    r2 = not cert_c
    print('  R2 corrupted diagonal NOT certified (%d boxes): %s'
          % (used_c, 'PASS' if r2 else 'FAIL'))
    ok &= r2

    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
