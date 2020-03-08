"""
T: O(N)
S: O(1)

For an array to be a mountain it has to satisfy these conditions:
1. Has an ascent
2. Has a descent from the end of the ascent
3. Both ascent and descent only happen once
First, we find a possible peak(end of the ascent), then we check if there is
a descent starting on that peak and ending at the end of the array.
"""

from typing import List


class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        end_index = len(A) - 1
        peak = 0
        while peak < end_index and A[peak] < A[peak + 1]:
            peak += 1
        if peak == 0 or peak == end_index:
            return False
        descent = peak
        while descent < end_index and A[descent] > A[descent + 1]:
            descent += 1
        return descent == end_index
