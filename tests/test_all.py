from synthetic_datasets import NoiseCircle

def test_shape():
    nc = NoiseCircle()

    for samples, labels in nc:
        assert samples.shape == (32, 64, 64)
        assert labels.shape == (32, 3)
        break


