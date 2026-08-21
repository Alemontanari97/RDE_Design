# esc_probe_crosslowering_decades.py — S-FOUNDATIONS-C4 escalation r1,
# minor (d) CROSS-LOWERING. Executable check for the repairs of
# MIN-CROSSLOWERING-3 (E3 separation is ~4.4 decades, NOT seven) and
# MIN-CROSSLOWERING-8 (pair-matched A_FD(implied) range, robustness
# ~2.8x). Pure stdlib; pinned-env safe; no measurements — derived
# arithmetic from carried record numbers only (findings_registry.yaml
# :319-336; PROGRESS_2026-08-12_S25bis_speed.md STEP 13 :362-399).
import math

u64 = 2.0 ** -53           # binary64 unit roundoff ~1.11e-16
u32 = 2.0 ** -24           # binary32 unit roundoff ~5.96e-8

# Record numbers (carriers cited above)
abs_floor = 2.9e-2         # sequential eager-vs-jit abs divergence
g_sc = 2.0e6               # gradient scale of record
phi64 = abs_floor / g_sc   # ~1.45e-8 rel floor
Phi_chain = phi64 / u64    # ~1.3e8

# E3 predictions (CLG-D7, prediction P3)
phi32_q1 = Phi_chain * u32            # q = 1 (D2/D3): O(1-10)
ratio_sqrt = math.sqrt(u32 / u64)     # sqrt-class: 2^14.5
phi32_sqrt = phi64 * ratio_sqrt       # D4-ALT: ~3e-4
sep_decades = math.log10(phi32_q1 / phi32_sqrt)

print(f"phi64            = {phi64:.3e}")
print(f"Phi_chain        = {Phi_chain:.3e}")
print(f"phi32 (q=1)      = {phi32_q1:.3e}")
print(f"ratio sqrt-class = 2^{math.log2(ratio_sqrt):.1f} = {ratio_sqrt:.3e}")
print(f"phi32 (sqrt)     = {phi32_sqrt:.3e}")
print(f"separation       = {sep_decades:.2f} decades")

# REJECTOR: the pre-repair text said "seven decades" — that claim must
# FAIL here; the corrected ~4.4 decades must PASS.
assert abs(sep_decades - math.log2(ratio_sqrt) * math.log10(2)) < 1e-12, \
    "separation must equal log10(2^14.5) exactly (ratio-of-ratios)"
assert 4.0 < sep_decades < 5.0, f"separation {sep_decades:.2f} not ~4.4"
assert not (6.5 < sep_decades < 7.5), "seven-decade claim must be dead"

# MIN-CROSSLOWERING-8: pair-matched A_FD(implied) range.
dH = 0.18                  # mixed-lowering contamination (gate-rejected)
afd_seq = dH / phi64       # sequential-pair reading ~1.2e7
lo_rel, hi_rel = 2.2e-2 / g_sc, 8.2e-2 / g_sc  # batched-pair incident range
afd_hi, afd_lo = dH / lo_rel, dH / hi_rel
print(f"A_FD seq-pair    = {afd_seq:.3e} = 10^{math.log10(afd_seq):.2f}")
print(f"A_FD pair-matched= [{afd_lo:.3e}, {afd_hi:.3e}] "
      f"= [10^{math.log10(afd_lo):.2f}, 10^{math.log10(afd_hi):.2f}]")
shift = max(afd_hi / afd_seq, afd_seq / afd_lo)
print(f"max shift vs seq = {shift:.2f}x")
assert shift < 3.0, "pair-choice robustness claim (~2.8x) violated"
assert 6.0 < math.log10(afd_lo) and math.log10(afd_hi) < 7.5, \
    "'~7 orders' reading must be robust to pair choice"
print("ALL PASS")
