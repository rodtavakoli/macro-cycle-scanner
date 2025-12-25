import numpy as np
from ripser import ripser


def compute_diagrams(
    X: np.ndarray,
    maxdim: int = 1,
):
    """
    Compute persistence diagrams using Ripser.
    """
    return ripser(X, maxdim=maxdim)["dgms"]


def max_h1_persistence(dgm1: np.ndarray) -> float:
    """
    Maximum H1 persistence (loop strength).
    """
    if dgm1.size == 0:
        return 0.0

    persistence = dgm1[:, 1] - dgm1[:, 0]
    persistence = persistence[np.isfinite(persistence)]

    return float(persistence.max()) if persistence.size else 0.0
