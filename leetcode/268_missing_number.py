"""
T: O(N)
S: O(1)

The idea is to get the sum of range [0, N] and subtract from it the sum of
the array. The code demonstrates how to do that in overflow-prone languages.
"""

from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i, num in enumerate(nums):
            missing += i - num + 1
        return missing
