# src/cycle_tda/metrics.py

import numpy as np


def summarize_series(x: np.ndarray) -> dict:
    x = x[np.isfinite(x)]
    if len(x) == 0:
        return dict(mean=np.nan, p90=np.nan, std=np.nan, cv=np.nan, active_rate=np.nan)

    mean = np.mean(x)
    p90 = np.percentile(x, 90)
    std = np.std(x)
    cv = std / (mean + 1e-12)
    active_rate = np.mean(x >= p90)

    return dict(
        mean=mean,
        p90=p90,
        std=std,
        cv=cv,
        active_rate=active_rate,
    )


def usability_score(p90: float, cv: float) -> float:
    return p90 / (cv + 1e-12)
