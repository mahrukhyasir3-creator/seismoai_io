import numpy as np
import seismoai_io


def test_normalize_traces():
    dummy = np.array([[1, 2, 3]])
    normalized = seismoai_io.normalize_traces(dummy)

    assert normalized.max() <= 1
    assert normalized.min() >= 0


test_normalize_traces()

print("All Tests Passed Successfully")
