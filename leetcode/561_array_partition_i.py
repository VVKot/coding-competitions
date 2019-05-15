from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        for i, num in enumerate(sorted(nums)):
            if i % 2 == 0:
                result += num
        return result
