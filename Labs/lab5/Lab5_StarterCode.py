from collections import Counter
from functools import lru_cache
import matplotlib.pyplot as plt

"""
Derek Rioveros
14819708

ASSIGNMENT: COMPLETE length, peak, champion, and pmf_cdf below
"""

"""
ECE 105: Programming for Engineers 2
Created September 7, 2020
Steven Weber

Modified October 31, 2026
Naga Kandasamy

Collatz sequences starter code

This code finds the starting numbers whose Collatz sequences are the
longest, and the ones that climb the highest, for every n up to a
million. Then it plots how the lengths are distributed: their PMF
and CDF.

The Collatz step: c(n) = n / 2 if n is even, 3 n + 1 if n is odd.
The Collatz sequence from n: n, c(n), c(c(n)), ..., down to 1.

Variable convention:
f: a function of one positive integer, such as length or peak
n: a starting number, 1, 2, 3, ...
n_max: the largest starting number
data: a list of numbers
values: the distinct numbers in data, smallest first
pmf, cdf: lists with one entry per value (see pmf_cdf)
"""

# One Collatz step (Lecture 11)
def c(n):
    if n % 2 == 0:               # even: halve it
        return n // 2
    return 3 * n + 1             # odd: 3n + 1

# The Collatz sequence from n down to 1, as a list, with a loop
# (Lecture 11, #4): slow, but easy to check. The reference for #1.
def collatz(n):
    seq = [n]
    while n != 1:
        n = c(n)
        seq.append(n)
    return seq

"""
COMPLETE (#1, recursively; the cache is already there):
length(n): the number of terms in the Collatz sequence from n,
           counting n and 1 (Lecture 11, #6)
peak(n):   the largest number in the Collatz sequence from n
Both have the same base case, n == 1. Otherwise, combine n with
the answer for c(n), the rest of the sequence.
Example: collatz(6) is [6, 3, 10, 5, 16, 8, 4, 2, 1], so
length(6) is 9 and peak(6) is 16
"""
# Terms in the Collatz sequence from n >= 1, counting n and 1
@lru_cache(maxsize=None)
def length(n):
    # the base case, then the recursive case (replace return 0)
    if n == 1:
        return 1
    return 1 + length(c(n))

# Largest number in the Collatz sequence from n >= 1
@lru_cache(maxsize=None)
def peak(n):
    # the base case, then the recursive case (replace return 0)
    if n == 1:
        return 1
    return max(n, peak(c(n)))

"""
COMPLETE (#2):
champion(f, n_max): the n from 1 to n_max with the largest f(n),
as a tuple (n, f(n)). On a tie, the smallest such n.
f is any function of one number: champion(length, 1000) finds the
longest sequence, and champion(peak, 1000) the highest climb.
1. best = 1
2. for n = 2, 3, ..., n_max: if f(n) is larger than f(best), n is
   the new best. Larger, not equal: on a tie, the first one stays.
3. return best and f(best)
Going up from n = 1 fills the cache from the bottom up (Lecture 11,
#3).
Example: champion(length, 10) is (9, 20): the sequence from 9 has
20 terms, more than from any other n from 1 to 10
"""
# The n from 1 to n_max with the largest f(n), and f(n)
def champion(f, n_max):
    # 1.-2. best
    best = 1

    # 3. return (replace 0, 0)
    for n in range(2, n_max + 1):
            if f(n) > f(best):
                best = n
                
    return best, f(best)

"""
COMPLETE (#3):
pmf_cdf(data): how the numbers in the list data are distributed,
as three lists, one entry per distinct value:
values: the distinct numbers in data, smallest first
pmf:    pmf[i] is the fraction of data equal to values[i]
cdf:    cdf[i] is the fraction of data less than or equal to values[i]
1. counts: how many times each value occurs: a Counter (Lecture 6)
2. values: the counted values, sorted
3. pmf: each value's count, divided by len(data)
4. cdf: a running total of the counts, divided by len(data)
Example: for data = [1, 1, 2, 4, 5, 5, 5, 8, 9, 12],
values is [1, 2, 4, 5, 8, 9, 12]
pmf    is [0.2, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1]
cdf    is [0.2, 0.3, 0.4, 0.7, 0.8, 0.9, 1.0]
"""
# The values in data, and their PMF and CDF
def pmf_cdf(data):
    # 1. counts
    counts = Counter(data)
    # 2. values
    values = sorted(counts)
    # 3. pmf
    pmf = []
    for value in values:
        pmf.append(counts[value] / len(data))
    # 4. cdf
    cdf = []
    running_total = 0

    for value in values:
        running_total += counts[value]
        cdf.append(running_total / len(data))

    # return the three lists (replace the empty ones)
    return values, pmf, cdf

# The median: the first value where the CDF reaches 1/2
# (0 if there are no values)
def median(values, cdf):
    for v, F in zip(values, cdf):
        if F >= 0.5:
            return v
    return 0

# Plot the PMF (blue stems, left axis) and the CDF (red steps, right
# axis) of each list of lengths, one panel for each n_max
def plot_pmf_cdf(dists, filename):
    fig, axes = plt.subplots(2, 3, figsize=(11, 6))
    for ax, (n_max, (values, pmf, cdf)) in zip(axes.flat, dists.items()):
        ax.set_title(f"n = 1 to {n_max:,}", fontsize=10)
        if not values:           # nothing to plot yet
            continue
        ax.stem(values, pmf, markerfmt=" ", basefmt=" ")
        ax.set_ylabel("PMF", color="C0")
        ax2 = ax.twinx()         # a second y-axis, on the right
        ax2.plot(values, cdf, "r", drawstyle="steps-post")
        ax2.set_ylim(0, 1.05)
        ax2.set_ylabel("CDF", color="r")
    for ax in axes[1]:
        ax.set_xlabel("sequence length")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Main program
if __name__ == "__main__":
    # Check three sequences against Lecture 11
    for n in [6, 7, 27]:
        print(f"from {n}: {length(n)} terms, up to {peak(n)}")

    # The record holders: the longest sequence, and the highest climb
    n_maxes = [10, 100, 1000, 10_000, 100_000, 1_000_000]
    print("    n_max   longest from  terms   highest from            peak")
    for n_max in n_maxes:
        n1, L = champion(length, n_max)
        n2, P = champion(peak, n_max)
        print(f"{n_max:>9,} {n1:>14,} {L:>6} {n2:>14,} {P:>15,}")
    print(f"numbers in length's cache: {length.cache_info().currsize:,}")

    # How the lengths are distributed, for n = 1 to n_max
    print("    n_max    mean  median")
    dists = {}
    for n_max in n_maxes:
        data = [length(n) for n in range(1, n_max + 1)]
        values, pmf, cdf = pmf_cdf(data)
        dists[n_max] = values, pmf, cdf
        print(f"{n_max:>9,} {sum(data) / n_max:7.1f} {median(values, cdf):7}")

    plot_pmf_cdf(dists, "Lab5_Collatz.pdf")
