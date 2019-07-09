from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicated, missing = -1, -1
        for num in nums:
            val = abs(num)
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
            else:
                duplicated = val
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                break
        return [duplicated, missing]
