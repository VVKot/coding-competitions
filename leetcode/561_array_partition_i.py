"""
T: O(NlogN)
S: O(N) - sorted returns an iterator, but Python sorting works in linear memory

We can determine the best solution greedily. We have to group numbers in
sorted order and take every one of them which is at the odd position.
"""


from typing import List


class Solution:

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
