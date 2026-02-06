# src/cycle_tda/registry.py
import pandas as pd

def build_series_registry(raw: dict[str, pd.Series]) -> dict[str, pd.Series]:
    reg = dict(raw)

    if "XAU" in raw and "XAG" in raw:
        reg["XAU_XAG_RATIO"] = raw["XAU"] / raw["XAG"]

    if "XAU" in raw and "M2" in raw:
        reg["XAU_M2_RATIO"] = raw["XAU"] / raw["M2"]

    return reg
