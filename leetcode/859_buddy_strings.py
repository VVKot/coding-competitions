"""
T: O(N)
S: O(N)

First, we check if the strings are of the same length. After that, we check if
they are already equal. In that case, all we need is to check whether they have
at least one duplicated character for the swap. If the strings are not equal,
we check if there is a valid pair for swap.
"""


class Solution:

    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) != len(A)
        pairs = [[a, b] for a, b in zip(A, B) if a != b]
        if len(pairs) != 2:
            return False
        first, second = pairs
        return first == second[::-1]
