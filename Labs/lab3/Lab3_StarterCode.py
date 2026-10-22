from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

"""
YOUR FULL NAME HERE
YOUR STUDENT ID HERE

ASSIGNMENT: COMPLETE count_words, fit_zipf, and compare_top below
"""

"""
ECE 105: Programming for Engineers 2
Created September 5, 2020
Steven Weber

Modified October 15, 2026
Naga Kandasamy

Zipf's law starter code

This code counts the words in three books, ranks them by count,
fits a power law c_k = C * k**m to the counts, plots count against
rank on log-log axes, and compares the most common words of two
of the books

Variable convention:
c: word counts, largest first: c[0] is the count of the rank-1 word
counts: dictionary, word -> number of times it appears
k: rank of a word (1 = the most common word)
m: slope of the fitted line on log-log axes (Zipf's law: m = -1)
C: the fitted constant: c_k is about C * k**m
ws: list of words, in the order they appear in the book
"""

# Strip these from both ends of a word: Lecture 6's list, plus the
# Spanish marks in Don Quijote
PUNCT = '.,;:!?"()_*-\'¿¡«»[]'

# Lecture 6's words(), which also splits at the Spanish dash
def words(text):
    """Lowercase words, punctuation stripped from both ends."""
    text = text.lower().replace("--", " ").replace("—", " ")
    ws = [w.strip(PUNCT) for w in text.split()]
    return [w for w in ws if w]      # drop empty strings

# Read a book (a UTF-8 text file); return its list of words
def read_words(filename):
    with open(filename, encoding="utf-8") as f:
        return words(f.read())

"""
COMPLETE (#1, by hand, no Counter):
count_words takes a list of words, ws, and returns a dictionary
that maps each distinct word to the number of times it appears:
1. start with an empty dictionary
2. for each word in ws: if it is already a key, add one to its
   count; otherwise, add it with a count of one (Lecture 6, #4)
3. return the dictionary
Example: count_words(["the", "cat", "saw", "the", "dog"]) returns
{"the": 2, "cat": 1, "saw": 1, "dog": 1}
"""
# Count each distinct word in ws
def count_words(ws):
    # 1. counts: an empty dictionary
    pass
    # 2. each word: seen before, add one; otherwise, start at one
    pass
    # 3. return counts (replace the {})
    return {}

# The counts, largest first, as an array: c[0] is the count of rank 1
def rank_counts(counts):
    return np.array(sorted(counts.values(), reverse=True))

"""
COMPLETE (#2, with ChatGPT Edu, then review it: see the slides):
Give ChatGPT Edu the def line and docstring below and ask for the
body. Then check its answer against both examples before you trust
it, and record the conversation in ai_log.md.
"""
def fit_zipf(c, kmin, kmax):
    """Fit c_k = C * k**m to the counts of ranks kmin to kmax.

    c: numpy array of word counts, largest first; c[0] is rank 1.
    kmin, kmax: the first and last rank to fit; both are included.
    Fits a straight line, log10(c_k) = m * log10(k) + b, by least
    squares (np.polyfit) to the ranks k = kmin, kmin + 1, ..., kmax.
    Returns (m, C), where C = 10**b.

    Examples (rounded to 6 decimal places):
    fit_zipf(np.array([600, 300, 200, 150]), 1, 4)
        returns (-1.0, 600.0)
    fit_zipf(np.array([5000, 900, 400, 1]), 2, 3)
        returns (-2.0, 3600.0)
    """

    k = np.arange(kmin, kmax + 1)
    counts = c[kmin - 1:kmax]

    m, b = np.polyfit(np.log10(k), np.log10(counts), 1)

    C = 10**b

    return m, C
    #return 0, 0

# The n most common words, as a set
def top_words(counts, n):
    return set(sorted(counts, key=counts.get, reverse=True)[:n])

"""
COMPLETE (#3, by hand):
compare_top takes the word counts of two books, counts_a and
counts_b, and a number n, and compares their n most common words.
It returns three sets: the words in both top-n lists, the words in
a's top n only, and the words in b's top n only:
1. top_a, top_b: the n most common words of each book (top_words)
2. return the three sets: use the set operators & and -
Example: compare_top({"a": 3, "b": 2, "c": 1},
                     {"b": 5, "c": 4, "a": 1}, 2)
returns ({"b"}, {"a"}, {"c"})
"""
# Compare the n most common words of two books
def compare_top(counts_a, counts_b, n):
    # 1. top_a, top_b: the n most common words of each book
    pass
    # 2. return: in both, in a only, in b only (replace the sets)
    return set(), set(), set()

# Plot count against rank on log-log axes: one set of dots per book,
# and a dashed line for each fit, over the fitted ranks
def plot_zipf(c_set, fits, names, kmin, kmax, filename):
    plt.figure()
    for c, (m, C), name in zip(c_set, fits, names):
        k = np.arange(1, c.size + 1)     # ranks 1, 2, ..., c.size
        plt.loglog(k, c, ".", markersize=2,
                   label=f"{name}: slope {m:.2f}")
        kf = np.arange(kmin, kmax + 1)   # the fitted ranks
        plt.loglog(kf, C * kf**m, "k--", linewidth=1)
    plt.xlabel("rank of the word, k")
    plt.ylabel("number of times it appears, c_k")
    plt.title(f"Zipf's law: lines fitted to ranks {kmin} to {kmax}")
    plt.legend(markerscale=4)        # bigger dots in the legend
    plt.savefig(filename)
    plt.show()

# Main program
if __name__ == "__main__":

    m, C = fit_zipf(np.array([600, 300, 200, 150]), 1, 4)
    print("Example 1:", round(m, 6), round(C, 6))

    m, C = fit_zipf(np.array([5000, 900, 400, 1]), 2, 3)
    print("Example 2:", round(m, 6), round(C, 6))

    quit()


    books = {"A Tale of Two Cities": "two_cities.txt",
             "King James Bible": "kjv.txt",
             "Don Quijote": "quijote.txt"}
    kmin, kmax = 1, 1000             # the ranks to fit

    counts = {}                      # book -> its word counts
    c_set, fits = [], []
    for name, filename in books.items():
        ws = read_words(filename)
        counts[name] = count_words(ws)
        same = counts[name] == Counter(ws)   # check #1 against Counter
        print(f"{name}: {len(ws):,} words, {len(counts[name]):,} "
              f"different; matches Counter: {same}")
        c = rank_counts(counts[name])
        m, C = fit_zipf(c, kmin, kmax)
        print(f"   fit, ranks {kmin} to {kmax}: c_k = {C:,.0f} * k^({m:.3f})")
        c_set.append(c)
        fits.append((m, C))

    plot_zipf(c_set, fits, list(books), kmin, kmax, "Lab3_Zipf.pdf")

    n = 20
    both, only_a, only_b = compare_top(counts["A Tale of Two Cities"],
                                       counts["King James Bible"], n)
    print(f"Top {n} words of A Tale of Two Cities and King James Bible:")
    print(f"   in both ({len(both)}):", " ".join(sorted(both)))
    print(f"   Dickens only ({len(only_a)}):", " ".join(sorted(only_a)))
    print(f"   Bible only ({len(only_b)}):", " ".join(sorted(only_b)))