"""R22F round-2 L1 probe: interior_margin

Feeds finding R22F-L1-7 (refutation phaseD_r22f_refute_r2_l1.md).

CLAIM UNDER ATTACK ([REV2-r1-14] in phaseD_r22f_centerpiece.md, §3.4/B-4):
the per-family ENTRY-margin floor  M_entry(xi) - 1 >= m0 > 0  is presented
as the hypothesis under which B-4's registered exclusion window is
"licensed for the marched phases".  The only near-sonic loci named are the
design-march loci (Sauer IVL / lip / axis) and the INTERFACE-side
corrugated-sonic locus (limit L3), the latter gated by m0.

ATTACK: an H-RED-2(SBV)-admissible phase field with ONE front (exactly the
intended fitted-sheet class of the M-RED families F-c/F-d) can carry an
INTERIOR (post-front) Mach margin arbitrarily below ANY entry floor m0,
because an oblique front decelerates the flow: with entry Mach M1 fixed
(entry margin M1 - 1 large), the post-shock Mach M2(beta) sweeps
CONTINUOUSLY from M1 (Mach-angle limit) down through 1 to the subsonic
normal-shock value as the wave angle beta increases.  Hence for every
m > 0 there is an admissible front with 0 < M2 - 1 < m: the entry floor
implies NO interior floor, and the near-sonic locus it creates is neither
one of the registered window's excluded loci nor gated by m0.

All numbers below are standard perfect-gas oblique-shock algebra
(theta-beta-M).  No number from P-A..P-D is used (CT-6 clean).  Pinned
env, numpy only.
"""

import numpy as np


def post_shock_mach(M1, beta, g):
    """Oblique shock: upstream M1, wave angle beta, ratio of specific
    heats g.  Returns (M2, theta) = downstream Mach, flow deflection."""
    M1n = M1 * np.sin(beta)
    # deflection angle (theta-beta-M relation)
    theta = np.arctan(
        2.0 / np.tan(beta) * (M1n**2 - 1.0) / (M1**2 * (g + np.cos(2.0 * beta)) + 2.0)
    )
    # normal downstream Mach
    M2n = np.sqrt((1.0 + 0.5 * (g - 1.0) * M1n**2) / (g * M1n**2 - 0.5 * (g - 1.0)))
    M2 = M2n / np.sin(beta - theta)
    return M2, theta


def find_margin_witness(M1, g, m_target):
    """Bisection in beta for a front with 0 < M2 - 1 < m_target.
    Bracket: Mach-angle side (M2 ~ M1 > 1) vs normal-shock side (M2 < 1).
    M2(beta) is continuous on the open bracket, so a sign change of
    M2 - 1 - m_target/2 yields a witness by the intermediate value
    theorem; we then CHECK the witness directly (the assertion is the
    computed value itself, no tolerance model needed)."""
    beta_lo = np.arcsin(1.0 / M1) + 1e-9   # vanishing-strength side
    beta_hi = np.pi / 2.0 - 1e-12          # normal-shock side
    f = lambda b: post_shock_mach(M1, b, g)[0] - 1.0 - 0.5 * m_target
    assert f(beta_lo) > 0.0, "bracket low side must be supersonic-margin"
    assert f(beta_hi) < 0.0, "bracket high side must be subsonic"
    for _ in range(200):
        mid = 0.5 * (beta_lo + beta_hi)
        if f(mid) > 0.0:
            beta_lo = mid
        else:
            beta_hi = mid
    return beta_lo  # M2(beta_lo) - 1 in (m_target/2, ...) -> check outside


def main():
    for g in (1.25, 1.4):            # frozen thermally-perfect class values
        for M1 in (1.8, 2.4):        # entry margins 0.8 and 1.4 (LARGE)
            entry_margin = M1 - 1.0

            # (A2) weak-front anchor: interior stays comfortably supersonic
            beta_weak = np.arcsin(1.0 / M1) + 0.05
            M2_weak, _ = post_shock_mach(M1, beta_weak, g)
            assert M2_weak - 1.0 > 0.3, (g, M1, M2_weak)

            # (A3) normal-shock side: subsonic reachable (continuity bracket)
            M2_norm, _ = post_shock_mach(M1, np.pi / 2.0 - 1e-12, g)
            assert M2_norm < 1.0, (g, M1, M2_norm)

            # (A4) for every requested floor, an admissible single front
            #      beats it: 0 < M2 - 1 < m
            for m in (1e-2, 1e-4, 1e-6):
                beta_star = find_margin_witness(M1, g, m)
                M2_star, theta_star = post_shock_mach(M1, beta_star, g)
                interior_margin = M2_star - 1.0
                assert 0.0 < interior_margin < m, (g, M1, m, interior_margin)
                # axial-march monitor is harsher still: the flow is
                # deflected by theta, so the along-march component
                # M2*cos(theta) < M2 (reported, not asserted-on).
                M2x = M2_star * np.cos(theta_star)
                print(
                    f"g={g:4.2f} M1={M1:3.1f} entry_margin={entry_margin:4.2f} "
                    f"m={m:7.1e}  beta={np.degrees(beta_star):7.3f} deg  "
                    f"theta={np.degrees(theta_star):6.3f} deg  "
                    f"interior_margin={interior_margin:9.3e}  M2x={M2x:8.6f}"
                )

            # (A5) headline: one front collapses the margin by > 100x
            beta_star = find_margin_witness(M1, g, 1e-2)
            M2_star, _ = post_shock_mach(M1, beta_star, g)
            assert entry_margin / (M2_star - 1.0) > 100.0

            # (A6) SHARP FORM -- the march-relevant monitor is the AXIAL
            # Mach (x-hyperbolicity): produce a front with
            # 0 < M2x - 1 < m.  Such a phase PASSES any axial-march
            # supersonicity monitor (no rejection fires), yet its interior
            # margin is below any fixed m0: the B-4 window is unlicensed
            # there with no certificate exit.  Witness by bisection on
            # M2x - 1 (continuous in beta; > 0 at the weak anchor, < 0 at
            # the M2-witness angle above).
            for m in (1e-2, 1e-4, 1e-6):
                fb = lambda b: (lambda MT: MT[0] * np.cos(MT[1]) - 1.0 - 0.5 * m)(
                    post_shock_mach(M1, b, g)
                )
                b_lo, b_hi = beta_weak, beta_star
                assert fb(b_lo) > 0.0 and fb(b_hi) < 0.0
                for _ in range(200):
                    mid = 0.5 * (b_lo + b_hi)
                    if fb(mid) > 0.0:
                        b_lo = mid
                    else:
                        b_hi = mid
                M2a, tha = post_shock_mach(M1, b_lo, g)
                ax_margin = M2a * np.cos(tha) - 1.0
                assert 0.0 < ax_margin < m, (g, M1, m, ax_margin)
                print(
                    f"g={g:4.2f} M1={M1:3.1f} AXIAL witness: m={m:7.1e}  "
                    f"beta={np.degrees(b_lo):7.3f} deg  "
                    f"axial_margin={ax_margin:9.3e}  (M2={M2a:8.6f} > 1: "
                    f"march monitor PASSES)"
                )

    print(
        "\nALL ASSERTS PASS: an SBV-admissible single-front phase field "
        "carries interior (post-front)\nMach margin arbitrarily below any "
        "entry floor m0 at fixed entry margin -- the [REV2-r1-14]\n"
        "entry-only floor does not license B-4's window against interior "
        "near-sonic loci."
    )


if __name__ == "__main__":
    main()
