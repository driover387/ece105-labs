"""Vertex sets for the chaos game."""
import numpy as np


def polygon(k):
    """The k vertices of a regular polygon on the unit circle, as a
    (k, 2) array: vertex 0 at the top, the rest counterclockwise."""
    theta = np.pi / 2 + 2 * np.pi * np.arange(k) / k
    return np.column_stack([np.cos(theta), np.sin(theta)])


def carpet():
    """The 8 vertices for the Sierpinski carpet, as an (8, 2) array: the
    corners and the edge midpoints of the square from (-1, -1) to (1, 1),
    counterclockwise from the lower left corner."""
    return np.array([[-1, -1], [0, -1], [1, -1], [1, 0],
                     [1, 1], [0, 1], [-1, 1], [-1, 0]], dtype=float)
