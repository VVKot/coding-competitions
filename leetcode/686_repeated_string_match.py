"""
T: O(A*B)
S: O(B)

There are two possibilities for the smallest match. One is just enough
repetitions of A to get to the length of B, and the second one is just
one repetition more. The second case covers an input like so:
A = "abcd" and B = "cdabcdab"
After that, simply check if every option works, and if not - return -1.
"""

import math


class Solution:

    def repeatedStringMatch(self, A: str, B: str) -> int:
        repeat_count = math.ceil(len(B) / len(A))
        for smallest_count in (repeat_count, repeat_count + 1):
            if B in A * smallest_count:
                return smallest_count
        return -1
