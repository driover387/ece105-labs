"""Tests for ChaosGame.play in chaos/game.py (#4 and #5). In the Lab6_Code
folder, run: pytest"""
import numpy as np
from chaos import ChaosGame, polygon, carpet, NotSame, Avoid


def targets(game, points):
    """The index of the vertex each move went toward. Move i went the
    fraction f of the way from the point before it (the center, for move 0)
    to a vertex v, so v = (p_i - (1 - f) p_before) / f. Fails if a move
    did not end the fraction f of the way to some vertex."""
    before = np.vstack([game.vertices.mean(axis=0), points[:-1]])
    v = (points - (1 - game.f) * before) / game.f
    # distance from each move's v to every vertex: an (n, k) array
    d = np.linalg.norm(v[:, None, :] - game.vertices[None, :, :], axis=2)
    assert d.min(axis=1).max() < 1e-9, "a move did not go toward a vertex"
    return d.argmin(axis=1)


# given: passes from the start
def test_shape():
    assert ChaosGame(polygon(3), seed=1).play(100).shape == (100, 2)


# #4 and #5: start at the center; every move goes the fraction f to a vertex
def test_moves_toward_vertices():
    for game in [ChaosGame(polygon(3), 1 / 2, seed=1),
                 ChaosGame(carpet(), 2 / 3, seed=2)]:
        targets(game, game.play(500))


# #5: the game follows its rule, move after move (needs #1 and #3 too)
def test_follows_rule():
    game = ChaosGame(polygon(4), 1 / 2, NotSame(), seed=3)
    t = targets(game, game.play(500))
    assert np.all(t[1:] != t[:-1])                   # never the same twice
    game = ChaosGame(polygon(4), 1 / 2, Avoid(1), seed=4)
    t = targets(game, game.play(500))
    assert np.all(t[1:] != (t[:-1] + 1) % 4)         # never the next one


# #5: the same seed plays the same game; another seed, another game
def test_seed():
    a = ChaosGame(polygon(5), seed=7).play(50)
    b = ChaosGame(polygon(5), seed=7).play(50)
    c = ChaosGame(polygon(5), seed=8).play(50)
    assert np.array_equal(a, b)
    assert not np.array_equal(a, c)
