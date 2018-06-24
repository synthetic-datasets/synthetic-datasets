import numpy as np
from synthetic_datasets import NoiseCircle

def test_shape():
    nc = NoiseCircle()

    for samples, labels in nc:
        assert samples.shape == (32, 64, 64)
        assert isinstance(labels, dict)
        assert isinstance(labels["X"], np.ndarray)
        assert isinstance(labels["Y"], np.ndarray)
        assert isinstance(labels["R"], np.ndarray)
        assert labels["X"].shape == (32,)
        assert labels["Y"].shape == (32,)
        assert labels["R"].shape == (32,)
        break



