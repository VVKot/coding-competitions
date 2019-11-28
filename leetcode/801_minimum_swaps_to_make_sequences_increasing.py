"""
T: O(N)
S: O(1)

This is a classical DP problem. For each iteration, we need to consider
our previous one. If both element pairs are in order, we either leave them all
as is or swap everything before them and current elements. If they are in the
reverse correct order(prev_A < next_B and prev_B < next_A), we can either
leave the reversed order count or swapped every up until a current point and
current elements.
"""

from typing import List


class Solution:

    def minSwap(self, A: List[int], B: List[int]) -> int:
        natural, swapped = 0, 1
        N = len(A)
        for i in range(N-1):
            new_natural = new_swapped = float('inf')
            a1, b1, a2, b2 = A[i], B[i], A[i+1], B[i+1]
            if a1 < a2 and b1 < b2:
                new_natural = natural
                new_swapped = swapped + 1
            if a1 < b2 and b1 < a2:
                new_natural = min(new_natural, swapped)
                new_swapped = min(new_swapped, natural+1)
            natural, swapped = new_natural, new_swapped
        return min(natural, swapped)
