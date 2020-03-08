from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, result = 0, 0
        for num in nums:
            if num:
                count += 1
            else:
                result = max(result, count)
                count = 0
        return max(result, count)
