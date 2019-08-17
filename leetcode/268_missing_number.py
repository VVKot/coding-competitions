from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i, num in enumerate(nums):
            missing += i - num + 1
        return missing
