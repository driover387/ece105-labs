"""Rules for the chaos game: which vertices the next move may go toward.

Every rule is a class with a method choices(k, current). The base class,
Rule, allows any vertex. Each subclass overrides choices, and nothing else
needs to change: ChaosGame.play calls self.rule.choices, whatever the rule.
"""


class Rule:
    """The basic rule: any vertex, every time."""

    def choices(self, k, current):
        """The indices of the vertices the next move may go toward, as a
        list, when there are k vertices and the last move went to vertex
        current. Here: all of them, [0, 1, ..., k - 1]."""
        return list(range(k))

    def __repr__(self):
        return "Rule()"


class NotSame(Rule):
    """Any vertex except the one the last move went to.

    Example: NotSame().choices(4, 2) is [0, 1, 3].
    """

    def choices(self, k, current):
        # 1. every index from 0 to k - 1 except current
        #    (replace the line below)
        return [i for i in range(k) if i != current]

    def __repr__(self):
        return "NotSame()"


class Avoid(Rule):
    """Any vertex except the one offset places counterclockwise from the
    vertex the last move went to: index (current + offset) % k.

    Avoid(0) is the same rule as NotSame(). On a square, Avoid(1) rules
    out the next vertex counterclockwise, and Avoid(2) the opposite one.
    Example: Avoid(1).choices(4, 3) is [1, 2, 3]: (3 + 1) % 4 is 0.
    """

    def __init__(self, offset):
        # 2. store offset as an attribute, so choices can use it
        #    (replace None with the right value)
        self.offset = offset

    def choices(self, k, current):
        # 3. every index from 0 to k - 1 except the one ruled out,
        #    (current + self.offset) % k (replace the line below)
        return [i for i in range(k) if i != (current + self.offset) % k]

    def __repr__(self):
        return f"Avoid({self.offset})"
