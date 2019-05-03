from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {target - num: i for i, num in enumerate(nums)}
        for j, num in enumerate(nums):
            if num in complement and complement[num] != j:
                return [j, complement[num]]
        return [-1, -1]
