"""Wintenberger–Shepherd detonation-cycle analysis and heat-release mapping.

cycles    : one-gamma model (Eqs. A19–A60, B2–B3) + real-chemistry FJ /
            Humphrey / Brayton cycles (`three_cycles`), 99-check validation
q_mapping : q, q-tilde, q_eff traceability across the papers' definitions
q_formal  : standard-state heat release q° and the q_c(T1) identity
"""
__all__ = ['cycles', 'q_formal', 'q_mapping']
