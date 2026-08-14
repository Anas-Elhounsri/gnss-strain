import numpy as np


def strain_rates(velocities, coords, radius=50.0):
    """Least-squares strain rates from a local velocity field."""
    v = np.asarray(velocities, dtype=float)
    x = np.asarray(coords, dtype=float)
    d = x[:, None, :] - x[None, :, :]
    w = np.exp(-(np.linalg.norm(d, axis=-1) ** 2) / (2 * radius ** 2))
    return np.linalg.lstsq(w, v, rcond=None)[0]
