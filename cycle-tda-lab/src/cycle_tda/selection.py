# src/cycle_tda/selection.py

import numpy as np
from sklearn.neighbors import NearestNeighbors


def ami_tau(y: np.ndarray, max_tau: int = 60, bins: int = 32) -> np.ndarray:
    """
    Average Mutual Information for delays 1..max_tau.
    """
    y = np.asarray(y)
    y = y[np.isfinite(y)]

    hist, edges = np.histogram(y, bins=bins)
    x = np.digitize(y, edges[:-1]) - 1
    x = np.clip(x, 0, bins - 1)

    ami = np.zeros(max_tau)

    for tau in range(1, max_tau + 1):
        x1 = x[:-tau]
        x2 = x[tau:]

        joint = np.zeros((bins, bins))
        for i in range(len(x1)):
            joint[x1[i], x2[i]] += 1

        joint /= joint.sum()

        px = joint.sum(axis=1)
        py = joint.sum(axis=0)

        mi = 0.0
        for i in range(bins):
            for j in range(bins):
                if joint[i, j] > 0:
                    mi += joint[i, j] * np.log(joint[i, j] / (px[i] * py[j]))

        ami[tau - 1] = mi

    return ami


def first_local_minimum(arr: np.ndarray) -> int | None:
    """
    Returns 1-based index of first local minimum, or None if none found.
    """
    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            return i + 1
    return None


def fnn_percent(
    y: np.ndarray,
    tau: int,
    m_max: int = 12,
    rtol: float = 10.0,
) -> np.ndarray:
    """
    False nearest neighbors % for m=1..m_max at fixed tau.
    """
    y = np.asarray(y)
    y = y[np.isfinite(y)]
    N = len(y)

    def embed(m):
        n_points = N - (m - 1) * tau
        if n_points <= 2:
            return None
        return np.column_stack(
            [y[i:i + n_points] for i in range(0, m * tau, tau)]
        )

    out = np.zeros(m_max, dtype=float)

    for m in range(1, m_max + 1):
        X = embed(m)
        Xp = embed(m + 1)
        if X is None or Xp is None:
            out[m - 1] = np.nan
            continue

        L = min(len(X), len(Xp))
        X = X[:L]
        Xp = Xp[:L]

        nn = NearestNeighbors(n_neighbors=2).fit(X)
        dists, idxs = nn.kneighbors(X)

        nn_dist = dists[:, 1]
        nn_idx = idxs[:, 1]

        delta = np.abs(Xp[:, -1] - Xp[nn_idx, -1])
        false = (delta / (nn_dist + 1e-12)) > rtol
        out[m - 1] = 100.0 * false.mean()

    return out


def select_embedding_params(
    y: np.ndarray,
    max_tau: int = 60,
    max_m: int = 12,
    fnn_threshold: float = 5.0,
    tau_cap: int | None = None,
) -> tuple[int, int, dict]:
    """
    Select (tau, m) using AMI + FNN.
    """
    y = np.asarray(y)
    y = y[np.isfinite(y)]

    ami_vals = ami_tau(y, max_tau=max_tau)
    tau = first_local_minimum(ami_vals)

    if tau is None:
        tau = max_tau // 5

    if tau_cap is not None:
        tau = min(tau, tau_cap)

    fnn_vals = fnn_percent(y, tau=tau, m_max=max_m)

    try:
        m = next(i + 1 for i, v in enumerate(fnn_vals) if v < fnn_threshold)
    except StopIteration:
        m = max_m

    info = {
        "ami": ami_vals,
        "fnn": fnn_vals,
        "tau": tau,
        "m": m,
    }

    return tau, m, info
