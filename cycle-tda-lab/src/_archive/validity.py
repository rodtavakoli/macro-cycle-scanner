# src/cycle_tda/validity.py
import pandas as pd
import numpy as np

def compute_threshold(
    strength: pd.Series,
    method: str = "quantile",
    q: float = 0.95,
) -> float:
    if method == "quantile":
        return strength.quantile(q)
    else:
        raise ValueError(f"Unknown threshold method: {method}")

def apply_validity(
    strength: pd.Series,
    threshold: float,
) -> pd.Series:
    return strength >= threshold
