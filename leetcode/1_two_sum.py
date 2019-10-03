from typing import Dict, List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()  # type: Dict[int, int]
        for i, num in enumerate(nums):
            if num in complements:
                return [complements[num], i]
            complements[target-num] = i
        return [-1, -1]
