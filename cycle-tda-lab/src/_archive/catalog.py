# src/cycle_tda/catalog.py

"""
Cycle catalog.

These cycles are treated as *hypotheses*, not truths.
Inclusion here does NOT imply validity.
"""

# Helper
def years_to_months(y: float) -> int:
    return int(round(y * 12))


CYCLE_CATALOG = {

    # =========================
    # Dewey canonical cycles
    # =========================

    # Core node
    "Dewey_17.75y": {
        "years": 17.75,
        "months": years_to_months(17.75),
        "family": "Dewey",
        "scale": "core",
        "notes": "Base node in Dewey 2x/3x lattice",
    },

    # Powers / products of 2 and 3 (commonly reported)
    "Dewey_8.88y": {
        "years": 8.88,
        "months": years_to_months(8.88),
        "family": "Dewey",
        "scale": "common",
        "notes": "Commonly reported; half of 17.75y",
    },

    "Dewey_5.92y": {
        "years": 5.92,
        "months": years_to_months(5.92),
        "family": "Dewey",
        "scale": "common",
        "notes": "17.75y / 3",
    },

    "Dewey_4.44y": {
        "years": 4.44,
        "months": years_to_months(4.44),
        "family": "Dewey",
        "scale": "common",
        "notes": "8.88y / 2",
    },

    "Dewey_2.96y": {
        "years": 2.96,
        "months": years_to_months(2.96),
        "family": "Dewey",
        "scale": "common",
        "notes": "8.88y / 3",
    },

    "Dewey_2.22y": {
        "years": 2.22,
        "months": years_to_months(2.22),
        "family": "Dewey",
        "scale": "common",
        "notes": "4.44y / 2",
    },

    "Dewey_1.48y": {
        "years": 1.48,
        "months": years_to_months(1.48),
        "family": "Dewey",
        "scale": "common",
        "notes": "4.44y / 3",
    },

    "Dewey_0.99y": {
        "years": 0.99,
        "months": years_to_months(0.99),
        "family": "Dewey",
        "scale": "short",
        "notes": "1-year class cycle",
    },

    "Dewey_0.66y": {
        "years": 0.66,
        "months": years_to_months(0.66),
        "family": "Dewey",
        "scale": "short",
        "notes": "Sub-annual cycle",
    },

    # Larger-scale Dewey cycles
    "Dewey_35.5y": {
        "years": 35.5,
        "months": years_to_months(35.5),
        "family": "Dewey",
        "scale": "long",
        "notes": "2 × 17.75y",
    },

    "Dewey_53.3y": {
        "years": 53.3,
        "months": years_to_months(53.3),
        "family": "Dewey",
        "scale": "long",
        "notes": "3 × 17.75y",
    },

    "Dewey_71y": {
        "years": 71.0,
        "months": years_to_months(71.0),
        "family": "Dewey",
        "scale": "very_long",
        "notes": "4 × 17.75y",
    },

    # =========================
    # Armstrong (ECM) cycles
    # =========================

    "Armstrong_8.6y": {
        "years": 8.6,
        "months": years_to_months(8.6),
        "family": "Armstrong",
        "scale": "core",
        "notes": "ECM base cycle (~3141 days)",
    },

    "Armstrong_51.6y": {
        "years": 51.6,
        "months": years_to_months(51.6),
        "family": "Armstrong",
        "scale": "long",
        "notes": "6 × 8.6y major ECM cycle",
    },

    "Armstrong_2.15y": {
        "years": 2.15,
        "months": years_to_months(2.15),
        "family": "Armstrong",
        "scale": "short",
        "notes": "Quarter-cycle of 8.6y",
    },

    # =========================
    # Frequently cited non-Dewey cycles
    # =========================

    "Lynx_9.6y": {
        "years": 9.6,
        "months": years_to_months(9.6),
        "family": "Empirical",
        "scale": "common",
        "notes": "Classic predator-prey cycle",
    },

    "US_Market_3.39y": {
        "years": 3.39,
        "months": years_to_months(3.39),
        "family": "Empirical",
        "scale": "common",
        "notes": "Frequently cited US market cycle (~40.7 months)",
    },

        # =========================
    # Pi-centered hypothesis cycles
    # =========================

    "Pi_3141d": {
        "days": 3141,
        "years": 3141 / 365.25,
        "months": int(round((3141 / 365.25) * 12)),
        "family": "PiHypothesis",
        "scale": "core",
        "notes": "π-centered cycle (~3141 days); included as hypothesis, not endorsement",
    },

    "Pi_1571d": {
        "days": 1571,
        "years": 1571 / 365.25,
        "months": int(round((1571 / 365.25) * 12)),
        "family": "PiHypothesis",
        "scale": "short",
        "notes": "Half π cycle (3141 / 2)",
    },

    "Pi_785d": {
        "days": 785,
        "years": 785 / 365.25,
        "months": int(round((785 / 365.25) * 12)),
        "family": "PiHypothesis",
        "scale": "short",
        "notes": "Quarter π cycle (3141 / 4)",
    },

    "Pi_6283d": {
        "days": 6283,
        "years": 6283 / 365.25,
        "months": int(round((6283 / 365.25) * 12)),
        "family": "PiHypothesis",
        "scale": "long",
        "notes": "2π-scaled cycle (optional long-horizon test)",
    },

}
