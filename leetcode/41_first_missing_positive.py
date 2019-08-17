from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] <= N:
                correct_idx = nums[i] - 1
                if nums[correct_idx] == nums[i]:
                    break
                nums[correct_idx], nums[i] = nums[i], nums[correct_idx]

        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return N+1
