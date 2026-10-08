import numpy as np
import matplotlib.pyplot as plt

"""
YOUR FULL NAME HERE
YOUR STUDENT ID HERE

ASSIGNMENT: COMPLETE play_MAB_ave and plot_MAB functions below
"""

"""
ECE 105: Programming for Engineers 2
Created October 1, 2025
Naga Kandasamy

Modified October 4, 2026
Naga Kandasamy

Multi-armed bandit starter code

This code plays a multi-armed bandit with an explore-then-exploit
strategy, uses Monte Carlo simulation to estimate the fraction of
the best possible wealth that the strategy earns, and plots that
fraction against the number of pulls

Variable convention:
k: actual number of "explore" pulls on each arm
m: number of arms
M: outcomes of the arm pulls (m rows, n columns, entries 0 or 1)
n: number of pulls
N: number of independent trials for Monte Carlo averaging
p: probability of win (either scalar or array)
t: maximum number of "explore" pulls on each arm
"""

# Return the random results of n pulls on an arm with win prob. p
def pull_arm(p, n):
    # length-n array of 0s and 1s: 1 w.p. p, 0 w.p. 1 - p
    return np.random.choice([0, 1], p=[1 - p, p], size=n)

# Create a MAB: m arms, n pulls, a random win prob. on each arm
def create_MAB(m, n):
    # a random win probability (0 to 1) for each of the m arms
    p = np.random.uniform(0, 1, m)
    # pull each arm n times: M[a, j] = 1 if pull j on arm a wins
    M = np.array([pull_arm(pa, n) for pa in p])
    return p, M

# Number of explore pulls on each arm: t, if there are enough
def explore_MAB(m, n, t):
    # m arms, t times each, takes m * t pulls; but no arm can
    # have more than n // m
    return min(t, n // m)

# Play the MAB once: return wealth won / best possible wealth
def play_MAB(m, n, t):
    # a fresh bandit: win probabilities p and the outcomes M
    p, M = create_MAB(m, n)
    # number of explore pulls on each arm
    k = explore_MAB(m, n, t)
    # explore: arm a uses pulls a*k to (a+1)*k - 1; count wins
    wins = [np.sum(M[a, a*k:(a+1)*k]) for a in range(m)]
    # the arm that looks best (argmax: lowest index on a tie)
    a_est = np.argmax(wins)
    # exploit: pull arm a_est for the rest, m*k through n - 1
    wealth = np.sum(wins) + np.sum(M[a_est, m*k:])
    # best possible: knowing p, pull the best arm all n times
    best = np.sum(M[np.argmax(p), :])
    # if even the best arm never won, wealth / best is 0 / 0:
    # return -1 to mark a failed trial
    return wealth / best if best > 0 else -1

"""
COMPLETE:
play_MAB_ave takes m, n, t, and N, and returns the Monte Carlo
average of play_MAB(m, n, t) over N independent trials:
1. results: call play_MAB(m, n, t) N times; keep all N results
2. good: keep only the results that are not -1 (failed trials)
3. return the average of the results in good
"""
# Monte Carlo average of play_MAB(m, n, t) over N trials
def play_MAB_ave(m, n, t, N):
    # 1. results: list of N results of play_MAB(m, n, t)
    pass
    # 2. good: the results that are >= 0
    pass
    # 3. return the average of good (replace the 0)
    return 0

"""
COMPLETE:
plot_MAB takes m, N, n_set, t_set, f_set, and filename, where
m: number of arms (show it in the title)
N: number of Monte Carlo trials (show it in the title)
n_set: the numbers of pulls, the x-axis values
t_set: the explore parameters, one labeled curve for each t
f_set: f_set[i] is the curve for t_set[i], one value per n
filename: the file to save the plot to
1. start a new figure
2. plot n_set against each curve f in f_set, labeled with its t
   (walk f_set and t_set together with zip)
3. add an x-axis label
4. add a y-axis label
5. add a title, including the values of m and N
6. add a legend
7. save the figure to filename
8. show the figure
"""
# Plot the average fraction of the best wealth against n
def plot_MAB(m, N, n_set, t_set, f_set, filename):
    # 1. start a new figure
    pass
    # 2. one labeled curve per t: zip over f_set and t_set
    pass
    # 3. x-axis label
    pass
    # 4. y-axis label
    pass
    # 5. title, including m and N
    pass
    # 6. legend
    pass
    # 7. save to filename
    pass
    # 8. show
    pass

# Main program
if __name__ == "__main__":
    np.random.seed(105)      # same random numbers every run
    m = 2                    # number of arms
    N = 100                  # 100 to develop; 10000 to finish
    n_set = np.arange(20, 601, 20)   # pulls: 20, 40, ..., 600
    t_set = [1, 2, 4, 8, 16, 32]     # max explore pulls per arm

    # f_set[i]: average fractions for t_set[i], one per n
    f_set = []
    for t in t_set:
        f_set.append([play_MAB_ave(m, n, t, N) for n in n_set])
        print(f"t = {t:2d} done")

    filename = f"Lab2_m{m}_N{N}.pdf"
    plot_MAB(m, N, n_set, t_set, f_set, filename)
