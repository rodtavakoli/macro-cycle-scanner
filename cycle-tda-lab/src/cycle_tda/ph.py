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

def persistence_norms(dgm1: np.ndarray):
    """
    Compute L1, L2, and Z1 norms for H1 persistence diagram.
    """
    if dgm1.size == 0:
        return 0.0, 0.0, 0.0

    pers = dgm1[:, 1] - dgm1[:, 0]
    pers = pers[np.isfinite(pers)]

    if len(pers) == 0:
        return 0.0, 0.0, 0.0

    l1 = np.sum(pers)
    l2 = np.sqrt(np.sum(pers ** 2))
    z1 = l1 / len(pers)

    return float(l1), float(l2), float(z1)
