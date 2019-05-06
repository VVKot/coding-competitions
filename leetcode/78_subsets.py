from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(combo, start):
            result.append(combo)
            for i in range(start, len(nums)):
                backtrack(combo + [nums[i]], i + 1)
        backtrack([], 0)
        return result
