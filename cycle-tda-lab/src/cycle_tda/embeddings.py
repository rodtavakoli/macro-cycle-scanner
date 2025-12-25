import numpy as np


def delay_embedding(
    y: np.ndarray,
    m: int,
    tau: int,
) -> np.ndarray:
    """
    Time-delay embedding of a 1D signal.

    Parameters
    ----------
    y : np.ndarray
        1D time series
    m : int
        Embedding dimension
    tau : int
        Delay (in samples)

    Returns
    -------
    np.ndarray
        Point cloud of shape (n_points, m)
    """
    T = len(y)
    n_points = T - (m - 1) * tau

    if n_points <= 0:
        raise ValueError("Time series too short for chosen m and tau.")

    return np.column_stack(
        [y[i : i + n_points] for i in range(0, m * tau, tau)]
    )
