from typing import List


class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        min_num = max_num = float('inf')

        for i in range(1, N):
            if nums[i] < nums[i-1]:
                min_num = min(nums[i:])
                break

        for i in reversed(range(N-1)):
            if nums[i] > nums[i+1]:
                max_num = max(nums[:i+1])
                break

        if min_num == float('inf'):
            return 0
        left = right = 0

        for i in range(N):
            if nums[i] > min_num:
                left = i
                break

        for i in reversed(range(N)):
            if nums[i] < max_num:
                right = i
                break
        return right-left+1
