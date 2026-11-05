"""Tests for Lab 5. In the Lab5_Code folder, run: pytest   (or: pytest -v)
pytest finds this file (its name starts with test_) and runs every
function in it whose name starts with test_ (Lecture 9).
got == pytest.approx(want): equal, up to rounding, number by number."""
import pytest
from Lab5_StarterCode import collatz, length, peak, champion, pmf_cdf

# given: passes from the start
def test_collatz():
    assert collatz(1) == [1]
    assert collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]

# #1: the base case
def test_base_case():
    assert length(1) == 1
    assert peak(1) == 1

# #1: the docstring's example
def test_six():
    assert length(6) == 9
    assert peak(6) == 16

# #1: the loop is the reference (Lecture 9)
def test_match_loop():
    for n in range(1, 1000):
        seq = collatz(n)
        assert length(n) == len(seq)
        assert peak(n) == max(seq)

# #2: the docstring's example, and the smallest n_max
def test_champion_length():
    assert champion(length, 10) == (9, 20)
    assert champion(length, 1) == (1, 1)

# #2: a tie: from 7 and from 9, the sequence climbs to 52.
# The smallest n wins
def test_champion_tie():
    assert champion(peak, 10) == (7, 52)

# #2: any function of n works
def last_digit(n):
    return n % 10

def test_champion_any_function():
    assert champion(last_digit, 25) == (9, 9)

# #3: the docstring's example
def test_pmf_cdf_example():
    values, pmf, cdf = pmf_cdf([1, 1, 2, 4, 5, 5, 5, 8, 9, 12])
    assert values == [1, 2, 4, 5, 8, 9, 12]
    assert pmf == pytest.approx([0.2, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1])
    assert cdf == pytest.approx([0.2, 0.3, 0.4, 0.7, 0.8, 0.9, 1.0])

# #3: data in any order; the values come back sorted
def test_pmf_cdf_unsorted():
    values, pmf, cdf = pmf_cdf([3, 1, 2, 3, 3, 1])
    assert values == [1, 2, 3]
    assert pmf == pytest.approx([2 / 6, 1 / 6, 3 / 6])
    assert cdf == pytest.approx([2 / 6, 3 / 6, 1])
