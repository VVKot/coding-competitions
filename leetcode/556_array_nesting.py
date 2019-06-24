from typing import List


class Solution:

    def arrayNesting(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            j = i
            curr = 0
            while nums[j] != -1:
                new_j = nums[j]
                nums[j] = -1
                j = new_j
                curr += 1
            result = max(result, curr)
        return result
