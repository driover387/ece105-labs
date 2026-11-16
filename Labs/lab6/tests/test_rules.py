"""Tests for chaos/rules.py (#1 to #3). In the Lab6_Code folder, run: pytest
pytest finds every test_*.py file in tests/ (pyproject.toml says where) and
runs every function in it whose name starts with test_ (Lecture 9)."""
from chaos import Rule, NotSame, Avoid


# given: passes from the start
def test_rule_any():
    assert Rule().choices(4, 2) == [0, 1, 2, 3]


# given: passes from the start (Lecture 12: a subclass is a Rule too)
def test_subclasses():
    assert isinstance(NotSame(), Rule)
    assert isinstance(Avoid(1), Rule)


# #1: the docstring's example, and one more
def test_not_same():
    assert NotSame().choices(4, 2) == [0, 1, 3]
    assert NotSame().choices(3, 0) == [1, 2]


# #2: Avoid keeps its offset
def test_avoid_repr():
    assert repr(Avoid(2)) == "Avoid(2)"


# #3: the docstring's example, and the opposite vertex of a square
def test_avoid():
    assert Avoid(1).choices(4, 3) == [1, 2, 3]       # (3 + 1) % 4 is 0
    assert Avoid(2).choices(4, 0) == [0, 1, 3]       # 2 is opposite 0


# #1 and #3: two ways to write one rule
def test_avoid_zero_is_not_same():
    for k in range(3, 9):
        for current in range(k):
            allowed = NotSame().choices(k, current)
            assert len(allowed) == k - 1             # exactly one ruled out
            assert Avoid(0).choices(k, current) == allowed
