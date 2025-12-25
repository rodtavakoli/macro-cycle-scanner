import numpy as np
import pandas as pd

from .embeddings import delay_embedding
from .ph import compute_diagrams
from .scoring import cycle_strength_from_diagrams


def rolling_ph(
    series: pd.Series,
    window: int,
    m: int,
    tau: int,
):
    """
    Rolling persistent homology over a 1D time series.

    Returns a DataFrame with cycle strength indexed by window end date.
    """
    values = series.values
    dates = series.index

    records = []

    for end in range(window, len(values)):
        y_window = values[end - window : end]

        if np.any(np.isnan(y_window)):
            continue

        X = delay_embedding(y_window, m=m, tau=tau)
        dgms = compute_diagrams(X, maxdim=1)
        strength = cycle_strength_from_diagrams(dgms)

        records.append({
            "date": dates[end],
            "cycle_strength": strength,
            "window": window,
            "m": m,
            "tau": tau,
        })

    return pd.DataFrame(records).set_index("date")
