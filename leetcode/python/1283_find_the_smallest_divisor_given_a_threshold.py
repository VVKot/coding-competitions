"""
T: O(NlogM)
S: O(1)

Binary search all possible values to find the smallest one that fits.
Also, see a neat trick for the ceiling without a library call.
"""

from typing import List


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            divided_sum = sum((x + mid - 1) // mid for x in nums)
            if divided_sum > threshold:
                lo = mid + 1
            else:
                hi = mid
        return lo
