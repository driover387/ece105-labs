"""Tests for Lab 4. In the Lab4_Code folder, run: pytest   (or: pytest -v)
pytest finds this file (its name starts with test_) and runs every
function in it whose name starts with test_ (Lecture 9).
got == pytest.approx(want): equal, up to rounding, number by number."""
import numpy as np
import pytest
from Lab4_StarterCode import (square, ramp, triangle,
                              coefficients_loop, coefficients, fs)

X = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])

# given: passes from the start
def test_square():
    assert square(X) == pytest.approx([0, 0, 1, 1, 1])
    assert square(X + 2 * np.pi) == pytest.approx([0, 0, 1, 1, 1])

# #1: the docstring's example, and again one period later
def test_ramp():
    assert ramp(X) == pytest.approx([0, 0, 0, 1, 3])
    assert ramp(X + 2 * np.pi) == pytest.approx([0, 0, 0, 1, 3])

def test_triangle():
    assert triangle(X) == pytest.approx([3, 1, 0, 1, 3])
    assert triangle(X + 2 * np.pi) == pytest.approx([3, 1, 0, 1, 3])

# #2: Lecture 8's series for the square wave
def test_coefficients_square():
    a0, a, b = coefficients(square, 6)
    n = np.arange(1, 7)
    assert a0 == pytest.approx(1)
    assert a == pytest.approx(np.zeros(6), abs=1e-3)
    assert b == pytest.approx(np.where(n % 2 == 1, 2 / (np.pi * n), 0),
                              abs=1e-3)

# #2: the loop, which you can check by eye, is the reference
def test_coefficients_match_loop():
    for f in [square, ramp, triangle]:
        a0, a, b = coefficients(f, 20)
        a0_ref, a_ref, b_ref = coefficients_loop(f, 20)
        assert a0 == pytest.approx(a0_ref)
        assert a == pytest.approx(a_ref, abs=1e-9)
        assert b == pytest.approx(b_ref, abs=1e-9)

# #3: one term, worked out by hand: 1/2 + 2 sin(x)
def test_fs_one_term():
    x = np.linspace(-np.pi, np.pi, 9)
    got = fs(x, 1.0, np.array([0.0]), np.array([2.0]))
    assert got.shape == x.shape
    assert got == pytest.approx(0.5 + 2 * np.sin(x))

# #3: the cosine terms count too
def test_fs_cosines():
    x = np.linspace(-np.pi, np.pi, 9)
    got = fs(x, 0.0, np.array([1.0, 3.0]), np.array([0.0, 0.0]))
    assert got == pytest.approx(np.cos(x) + 3 * np.cos(2 * x))

# #2 and #3 together: at x = pi/2 the square wave is 1, and so is its sum
def test_fs_square_at_pi_over_2():
    a0, a, b = coefficients(square, 1000)
    assert fs(np.array([np.pi / 2]), a0, a, b) == pytest.approx([1], abs=1e-3)

"""
COMPLETE (#4): write one more test, of a PROPERTY: something that must
hold for every x, or every n, or every N, not one value worked out by
hand. Ideas (pick one, or your own):
- the triangle is even, triangle(-x) = triangle(x), so its b_n are 0
- the square wave minus 1/2 is odd, so its a_n are 0
- fs repeats every 2 pi: fs(x + 2 pi, ...) equals fs(x, ...)
- more terms, closer: the triangle's largest error with 50 terms is
  smaller than with 10
Name it test_something, run pytest, and see it pass. Then break your
code on purpose (change a sign in fs): does your test catch it?
"""
