"""
T: O(NlogN)
S: O(N) - sorted returns an iterator, but Python sorting works in linear memory

We can determine the best solution greedily. We have to group numbers in
sorted order and take minimum of every pair which are at the odd positions.
"""

from typing import List


class Solution:

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
