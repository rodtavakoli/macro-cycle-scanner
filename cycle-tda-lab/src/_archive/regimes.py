import numpy as np
import pandas as pd

def build_macro_regimes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Expects columns: CPI, M2, FedFunds
    Returns dataframe with regime labels added.
    """
    out = df.copy()

    out["inflation_yoy"] = out["CPI"].pct_change(12)
    out["inflation_accel"] = out["inflation_yoy"].diff()
    out["inflation_regime"] = np.where(
        out["inflation_accel"] > 0, "Accelerating", "Decelerating"
    )

    out["m2_yoy"] = out["M2"].pct_change(12)
    m2_med = out["m2_yoy"].median(skipna=True)
    out["liquidity_regime"] = np.where(
        out["m2_yoy"] > m2_med, "Loose", "Tight"
    )

    ff_med = out["FedFunds"].median(skipna=True)
    out["rate_regime"] = np.where(
        out["FedFunds"] > ff_med, "High", "Low"
    )

    return out
