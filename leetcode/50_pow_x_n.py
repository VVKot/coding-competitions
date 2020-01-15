"""
T: O(logN)
S: O(1)

We do better than brute force by finding the powers of two in the required
power and multiplying the result by appropriate numbers.
"""


class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n + 1
        result = 1.0
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result
