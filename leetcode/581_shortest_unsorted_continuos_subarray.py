from typing import List


class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        left = N
        stack = []  # type: List[int]
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                left = min(left, stack.pop())
            stack.append(i)
        right = 0
        stack = []
        for i in reversed(range(N)):
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                right = max(right, stack.pop())
            stack.append(i)
        if right < left:
            return 0
        return right-left+1
