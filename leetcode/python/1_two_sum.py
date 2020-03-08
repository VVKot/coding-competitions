"""
T: O(N)
S: O(N)

Remember numbers we have seen so far alongside their indices.
Return a sorted pair of indices when we see a number that is complement to the
previously seen one.
"""

from typing import Dict, List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}  # type: Dict[int, int]
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_nums:
                return [seen_nums[complement], i]
            seen_nums[num] = i
        return [-1, -1]
