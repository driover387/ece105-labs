"""The chaos game, as a class."""
import numpy as np
from .rules import Rule


class ChaosGame:
    """One chaos game: the vertices, the fraction f, a rule, and a random
    generator of its own.

    vertices: a (k, 2) array, one vertex per row (or a list of pairs)
    f:        each move goes this fraction of the way toward a vertex
    rule:     a Rule (or subclass): which vertices the next move may go to.
              None means Rule(), any vertex.
    seed:     the same seed plays the same game, move for move
    """

    def __init__(self, vertices, f=0.5, rule=None, seed=None):
        self.vertices = np.asarray(vertices, dtype=float)
        self.f = f
        self.rule = Rule() if rule is None else rule
        self.rng = np.random.default_rng(seed)

    def __repr__(self):
        return (f"ChaosGame({len(self.vertices)} vertices, f={self.f:.3g}, "
                f"rule={self.rule!r})")

    def play(self, n):
        """Play n moves; return the n points as an (n, 2) array.

        Start at the center of the vertices (their mean), with current = 0.
        Then, for each move i = 0, 1, ..., n - 1:
          a. allowed = the rule's choices, for k vertices and current;
          b. current = self.rng.choice(allowed), this move's vertex;
          c. p = p + self.f * (v - p), where v is that vertex (Lecture 13);
          d. row i of the points is p.
        """
        points = np.zeros((n, 2))
        # 4. the start: p, k, and current (replace pass)
        pass
        # 5. the n moves, a. to d. (replace pass)
        pass
        return points
