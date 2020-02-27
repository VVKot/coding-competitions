"""
T: O(N)
S: O(1)

Use two pointers, one to look through the array, and another one to remember
the position of the last even element. Whenever we see an even element, push it
to the start of the array after the last known even element.
"""

from typing import List


class Solution:

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        read, write = 0, 0
        for read in range(len(A)):
            if not A[read] & 1:
                A[read], A[write] = A[write], A[read]
                write += 1
        return A
