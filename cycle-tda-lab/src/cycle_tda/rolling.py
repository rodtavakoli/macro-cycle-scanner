# src/cycle_tda/rolling.py

import numpy as np
import pandas as pd

from .embeddings import delay_embedding
from .ph import compute_diagrams, max_h1_persistence, persistence_norms
from .utils import white_noise_like


# ============================
# Configuration (PH Backbone)
# ============================

MIN_EMBED_POINTS = 30   # hard floor for meaningful PH
EPS = 1e-12


def rolling_ph(
    series: pd.Series,
    window: int,
    stride: int = 1,
    m: int = 3,
    tau: int = 1,
    normalize: bool = True,
    include_null: bool = False,
) -> pd.DataFrame:
    """
    Rolling persistent homology over a 1D time series.

    This function is intentionally cycle-agnostic.
    It measures structural recurrence in reconstructed state space.

    Parameters
    ----------
    series : pd.Series
        Time-indexed 1D series (must be sortable)
    window : int
        Rolling window length (in samples)
    stride : int
        Step size between windows
    m : int
        Embedding dimension
    tau : int
        Embedding delay
    normalize : bool
        Whether to z-score each window before embedding
    include_null : bool
        Whether to compute PH on a white-noise null model

    Returns
    -------
    pd.DataFrame
        Indexed by window end date, with PH metrics and metadata
    """

    # ----------------------------
    # Defensive preprocessing
    # ----------------------------
    if not isinstance(series, pd.Series):
        raise TypeError("series must be a pandas Series")

    series = series.sort_index()
    values = np.asarray(series.values, dtype=float)
    dates = series.index

    if len(values) < window:
        raise ValueError("Series shorter than rolling window")

    min_embed = (m - 1) * tau + 1
    if window < min_embed:
        raise ValueError(
            f"Window {window} < embedding requirement {min_embed} (m={m}, tau={tau})"
        )

    records = []

    # ----------------------------
    # Rolling loop
    # ----------------------------
    for end in range(window, len(values) + 1, stride):
        yw = values[end - window : end]

        if not np.all(np.isfinite(yw)):
            continue

        # Embedded point count check
        n_points = window - (m - 1) * tau
        if n_points < MIN_EMBED_POINTS:
            continue

        # ----------------------------
        # Normalization (explicit)
        # ----------------------------
        if normalize:
            std = np.std(yw, ddof=0)
            if std < EPS:
                continue
            yw_proc = (yw - yw.mean()) / std
        else:
            yw_proc = yw

        # ----------------------------
        # Delay embedding
        # ----------------------------
        X = delay_embedding(yw_proc, m=m, tau=tau)

        # ----------------------------
        # Persistent homology
        # ----------------------------
        dgms = compute_diagrams(X, maxdim=1)
        dgm1 = dgms[1]

        if dgm1.size == 0:
            l1 = l2 = z1 = max_h1 = 0.0
        else:
            l1, l2, z1 = persistence_norms(dgm1)
            max_h1 = max_h1_persistence(dgm1)

        row = {
            "start_date": dates[end - window],
            "end_date": dates[end - 1],
            "l1": float(l1),
            "l2": float(l2),
            "z1": float(z1),
            "max_h1": float(max_h1),
            "window": window,
            "m": m,
            "tau": tau,
            "n_embed_points": n_points,
            "std": float(np.std(yw)),
            "range": float(np.ptp(yw)),
        }

        # ----------------------------
        # Optional null model
        # ----------------------------
        if include_null:
            yw_null = white_noise_like(yw_proc)
            Xn = delay_embedding(yw_null, m=m, tau=tau)
            dgms_n = compute_diagrams(Xn, maxdim=1)
            dgm1_n = dgms_n[1]

            if dgm1_n.size == 0:
                row["z1_null"] = 0.0
                row["max_h1_null"] = 0.0
            else:
                _, _, z1n = persistence_norms(dgm1_n)
                row["z1_null"] = float(z1n)
                row["max_h1_null"] = float(max_h1_persistence(dgm1_n))

        records.append(row)

    if not records:
        return pd.DataFrame(
            columns=[
                "start_date",
                "end_date",
                "l1",
                "l2",
                "z1",
                "max_h1",
                "window",
                "m",
                "tau",
                "n_embed_points",
                "std",
                "range",
            ]
        )

    return pd.DataFrame(records).set_index("end_date")
