"""
T: O(N)
S: O(1)

DP magic. Upsolve.
"""


class Solution:

    def numWays(self, n: int, k: int) -> int:
        if not n or not k:
            return 0
        if n == 1:
            return k
        prev_prev, prev = k, k**2
        for _ in range(2, n):
            curr = (prev_prev + prev) * (k - 1)
            prev_prev, prev = prev, curr
        return prev
