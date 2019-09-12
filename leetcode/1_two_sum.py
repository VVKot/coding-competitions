from typing import Dict, List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}  # type: Dict[int, int]
        for i, num in enumerate(nums):
            complement = target-num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i
        return [-1, -1]
