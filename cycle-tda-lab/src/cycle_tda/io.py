import pandas as pd
from pathlib import Path
import numpy as np


def load_csv(path, date_col="Date", value_col=None):
    """
    Load a CSV with automatic value column detection.

    Rules:
    - date_col must exist
    - if value_col is None, pick the single numeric column
    - if multiple numeric columns exist, raise a clear error
    """
    df = pd.read_csv(path)

    if date_col not in df.columns:
        raise ValueError(f"{path.name}: missing date column '{date_col}'")

    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col).reset_index(drop=True)

    if value_col is not None:
        if value_col not in df.columns:
            raise ValueError(f"{path.name}: value column '{value_col}' not found")
        df = df[[date_col, value_col]].dropna()
        return df

    # --- AUTO-DETECT VALUE COLUMN ---
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_cols) == 0:
        raise ValueError(f"{path.name}: no numeric columns found")

    if len(numeric_cols) > 1:
        raise ValueError(
            f"{path.name}: multiple numeric columns found {numeric_cols}. "
            "Specify value_col explicitly."
        )

    value_col = numeric_cols[0]
    df = df[[date_col, value_col]].dropna()

    return df



def save_features(
    df: pd.DataFrame,
    path: str | Path,
    index: bool = False,
) -> None:
    """
    Save features to CSV (Power BI friendly).
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)
