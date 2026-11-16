"""
YOUR FULL NAME HERE
YOUR STUDENT ID HERE

ASSIGNMENT: COMPLETE NotSame and Avoid in chaos/rules.py,
and ChaosGame.play in chaos/game.py
"""

"""
ECE 105: Programming for Engineers 2
Created September 9, 2020
Steven Weber

Modified November 7, 2026
Naga Kandasamy

Chaos game starter code (Lab 6)

This script plays six chaos games with the chaos package (in the chaos
folder), and draws them in one figure, Lab6_Chaos.png. Run it from the
Lab6_Code folder:
    python run_lab6.py
"""
import matplotlib.pyplot as plt
from chaos import ChaosGame, polygon, carpet, Rule, NotSame, Avoid

GOLDEN = 2 / (1 + 5 ** 0.5)          # 1 / phi = 0.618...

# (name, game). With these seeds, your pictures match the slides'.
GAMES = [
    ("triangle", ChaosGame(polygon(3), 1 / 2, Rule(), seed=1)),
    ("square", ChaosGame(polygon(4), 1 / 2, NotSame(), seed=2)),
    ("square", ChaosGame(polygon(4), 1 / 2, Avoid(1), seed=3)),
    ("square", ChaosGame(polygon(4), 1 / 2, Avoid(2), seed=4)),
    ("pentagon", ChaosGame(polygon(5), GOLDEN, Rule(), seed=5)),
    ("carpet", ChaosGame(carpet(), 2 / 3, Rule(), seed=6)),
]


def draw(games, n, filename):
    """Play n moves of each game, draw the games in a 2 x 3 grid, and save
    the figure as filename."""
    fig, axes = plt.subplots(2, 3, figsize=(9, 6.4))
    for ax, (name, game) in zip(axes.flat, games):
        p = game.play(n)
        ax.plot(p[:, 0], p[:, 1], ".", markersize=0.3, rasterized=True)
        ax.set_title(f"{name}: {game.rule!r}, f = {game.f:.3g}", fontsize=10)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(filename, dpi=200)


if __name__ == "__main__":
    for name, game in GAMES:
        print(f"{name:9s} {game!r}")
    draw(GAMES, 50_000, "Lab6_Chaos.png")
    print("saved Lab6_Chaos.png")
    plt.show()
