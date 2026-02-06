import numpy as np
import pandas as pd

def apply_cyclic_threshold(
    df: pd.DataFrame,
    strength_col: str = "cycle_strength",
    q: float = 0.95,
) -> tuple[pd.DataFrame, float]:
    """
    Adds `cyclic_regime` column based on quantile threshold.
    """
    out = df.copy()
    thresh = out[strength_col].quantile(q)
    out["cyclic_regime"] = np.where(
        out[strength_col] >= thresh, "Cyclic", "Non-Cyclic"
    )
    return out, float(thresh)
