"""Tests for chaos/shapes.py: given, and passing from the start."""
import numpy as np
from chaos import polygon, carpet


def test_triangle():
    v = polygon(3)
    assert v.shape == (3, 2)
    assert np.allclose(v[0], [0, 1])          # vertex 0 at the top


def test_on_unit_circle():
    for k in range(3, 9):
        assert np.allclose(np.linalg.norm(polygon(k), axis=1), 1)


def test_carpet():
    v = carpet()
    assert v.shape == (8, 2)
    assert np.all(np.abs(v).max(axis=1) == 1)  # all on the square's edge
