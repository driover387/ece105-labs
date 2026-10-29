import numpy as np
import matplotlib.pyplot as plt

"""
YOUR FULL NAME HERE
YOUR STUDENT ID HERE

ASSIGNMENT: COMPLETE ramp, triangle, coefficients, and fs below,
and one more test in test_lab4.py
"""

"""
ECE 105: Programming for Engineers 2
Created September 7, 2020
Steven Weber

Modified October 23, 2026
Naga Kandasamy

Fourier series starter code

This code computes the Fourier series coefficients of three periodic
signals, adds up the first N terms of each series, prints how far
each sum overshoots its signal, and plots the sums against the
signals. Every signal repeats every 2 pi.

The Fourier series of a signal f that repeats every 2 pi:
f(x) = a0/2 + sum over n = 1, 2, ... of a_n cos(n x) + b_n sin(n x)
a_n = (1/pi) * integral of f(x) cos(n x) dx over [-pi, pi]
b_n = (1/pi) * integral of f(x) sin(n x) dx over [-pi, pi]

Variable convention:
a0: the constant coefficient (the series starts with a0 / 2)
a, b: arrays of the cosine and sine coefficients: a[n - 1] is a_n
f: a signal: a function that takes an array x and returns f(x)
M: number of sample points on one period, for the integrals
n: term number, 1, 2, ..., N
N: number of terms in the series
x: array of points
"""

# Where x falls in its period, as a point in [-pi, pi)
def wrap(x):
    return np.mod(x + np.pi, 2 * np.pi) - np.pi

# Square wave (Lecture 8): 1 on [0, pi), 0 on [-pi, 0)
def square(x):
    return np.where(wrap(x) >= 0, 1.0, 0.0)

"""
COMPLETE (#1, with np.where, as square does):
ramp(x): on [-pi, pi), 0 where x < 0, and x where x >= 0
         (Lecture 8's ramp, made to repeat)
triangle(x): on [-pi, pi), |x|: -x where x < 0, and x where x >= 0
Call wrap(x) first, so that both repeat every 2 pi.
Example: for x = np.array([-3.0, -1.0, 0.0, 1.0, 3.0]),
ramp(x) returns     [0, 0, 0, 1, 3]
triangle(x) returns [3, 1, 0, 1, 3]
"""
# Ramp: 0 on [-pi, 0), x on [0, pi); repeats every 2 pi
def ramp(x):
    # replace np.zeros_like(x) with np.where(...)
    return np.zeros_like(x)

# Triangle: |x| on [-pi, pi); repeats every 2 pi
def triangle(x):
    # replace np.zeros_like(x) with np.where(...)
    return np.zeros_like(x)

# M sample points on one period: cut [-pi, pi) into M equal pieces,
# and take the middle of each (so no point falls on a jump)
def samples(M):
    return -np.pi + 2 * np.pi * (np.arange(M) + 0.5) / M

# The coefficients a0, a_1..a_N, b_1..b_N of f, with a loop over n:
# slow, but easy to check against the formulas. The reference for #2.
def coefficients_loop(f, N, M=4096):
    x = samples(M)
    fx = f(x)
    # the integral is about the sum of f(x) cos(n x) * (2 pi / M),
    # so (1/pi) times the integral is 2 * the mean
    a0 = 2 * np.mean(fx)
    a, b = np.zeros(N), np.zeros(N)
    for n in range(1, N + 1):
        a[n - 1] = 2 * np.mean(fx * np.cos(n * x))
        b[n - 1] = 2 * np.mean(fx * np.sin(n * x))
    return a0, a, b

"""
COMPLETE (#2, with broadcasting, no loop):
coefficients returns what coefficients_loop returns, with no loop:
1. x: the M sample points; fx: f at those points; n: 1, 2, ..., N
2. a0: as in coefficients_loop
3. a table with one row per point and one column per term:
   np.cos(x[:, None] * n) has shape (M, N) (Lecture 8, #8)
4. a: 2 * the mean of fx[:, None] * that table, down each column
   (axis=0), so one a_n per column. b: the same, with np.sin
Example (the square wave, Lecture 8): a0 is 1, every a_n is about 0,
and b_n is about 2 / (pi n) for odd n, about 0 for even n
"""
# The coefficients a0, a, b of f, with broadcasting
def coefficients(f, N, M=4096):
    # 1. x, fx, and n
    pass
    # 2. a0
    pass
    # 3.-4. a and b, each of shape (N,) (replace 0 and the zeros)
    return 0, np.zeros(N), np.zeros(N)

"""
COMPLETE (#3, with broadcasting, no loop):
fs returns the sum of the first N = len(a) terms of the Fourier
series, at every point of x:
a0/2 + a_1 cos(x) + b_1 sin(x) + ... + a_N cos(N x) + b_N sin(N x)
1. n: 1, 2, ..., N
2. terms: a * np.cos(x[:, None] * n) + b * np.sin(x[:, None] * n)
   has shape (x.size, N): one row per point, one column per term
3. return a0 / 2 plus the sum of each row (axis=1) (Lecture 8, #8)
Example: fs(x, 1.0, np.array([0.0]), np.array([2.0])) returns
0.5 + 2 sin(x), at every point of x
"""
# The sum of the first len(a) terms of the Fourier series, at x
def fs(x, a0, a, b):
    # 1. n
    pass
    # 2. terms
    pass
    # 3. return (replace np.zeros_like(x))
    return np.zeros_like(x)

# Plot each signal (black) and its Fourier sums, N terms for each N
def plot_fourier(signals, coefs, Ns, filename):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 2001)     # two periods
    fig, axes = plt.subplots(len(signals), 1, sharex=True,
                             figsize=(7, 7))
    for ax, (name, f) in zip(axes, signals.items()):
        a0, a, b = coefs[name]
        ax.plot(x, f(x), "k", linewidth=1, label="signal")
        for N in Ns:
            ax.plot(x, fs(x, a0, a[:N], b[:N]), linewidth=0.8,
                    label=f"N = {N}")
        ax.set_title(name, fontsize=10)
    axes[-1].legend(loc="upper center", fontsize=8, ncols=2)
    axes[-1].set_xlabel("x")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Main program
if __name__ == "__main__":
    signals = {"square": square, "ramp": ramp, "triangle": triangle}
    N = 250                          # the most terms we will use
    coefs = {name: coefficients(f, N) for name, f in signals.items()}

    # Check: the square wave's coefficients, against Lecture 8's series
    a0, a, b = coefs["square"]
    print(f"square wave: a0 = {a0:.4f}   (want 1)")
    print("  n      a_n      b_n   want b_n")
    for n in range(1, 7):
        want = 2 / (np.pi * n) if n % 2 == 1 else 0.0
        an, bn = round(a[n - 1], 4) + 0, round(b[n - 1], 4) + 0  # + 0: no -0.0
        print(f"{n:3d} {an:8.4f} {bn:8.4f} {want:8.4f}")

    # Gibbs: how far the sum goes above the signal's largest value
    Ns = [10, 50, 250]
    x = np.linspace(-np.pi, np.pi, 20001)
    print("overshoot: largest value of the N-term sum, minus the signal's")
    print("signal  " + "".join(f"{'N = ' + str(N):>10}" for N in Ns))
    for name, f in signals.items():
        a0, a, b = coefs[name]
        over = [fs(x, a0, a[:N], b[:N]).max() - f(x).max() for N in Ns]
        print(f"{name:8}" + "".join(f"{v:10.4f}" for v in over))

    plot_fourier(signals, coefs, [3, 10, 50], "Lab4_Fourier.pdf")
