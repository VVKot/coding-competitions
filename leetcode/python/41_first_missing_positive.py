from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] < N:
                should_be_at = nums[i]-1
                if nums[should_be_at] == nums[i]:
                    break
                nums[i], nums[should_be_at] = nums[should_be_at], nums[i]

        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return N+1
