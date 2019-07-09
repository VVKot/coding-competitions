from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = duplicated = 0
        for i, num in enumerate(nums):
            val = abs(num)
            duplicated ^= (i+1) ^ val
            index = val - 1
            if nums[index] < 0:
                missing = val
            else:
                nums[index] = -nums[index]
        duplicated ^= missing
        return [missing, duplicated]
