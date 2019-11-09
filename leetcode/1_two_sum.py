"""
T: O(N)
S: O(N)

Remember numbers we have seen so far alongside their indices.
Return a sorted pair of indices when there is a match.
"""


from typing import Dict, List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # type: Dict[int, int]
        for i, num in enumerate(nums):
            other = target-num
            if other in seen:
                return sorted([i, seen[other]])
            seen[num] = i
        return [-1, -1]
