# Lab 6: the chaos game

The layout of Lecture 13:

- `chaos/`: the package. `shapes.py` (given), `rules.py` (#1 to #3), `game.py` (#4 and #5).
- `tests/`: the tests. In this folder, run `pytest`.
- `pyproject.toml`: pytest's settings (`pythonpath = ["."]`, so the tests can import `chaos`).
- `run_lab6.py`: plays six games and draws them. `python run_lab6.py` saves `Lab6_Chaos.png`.
- `.gitignore`: what Git should not track.
