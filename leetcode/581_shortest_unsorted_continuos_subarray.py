import sys
from typing import List


class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        start = sys.maxsize
        end = -sys.maxsize
        stack = []  # type: List[int]
        for i, num in enumerate(nums):
            if stack:
                while stack and nums[stack[-1]] > num:
                    last_index = stack.pop()
                    start = min(last_index, start)
            stack.append(i)
        stack = []
        for i in reversed(range(N)):
            num = nums[i]
            if stack:
                while stack and nums[stack[-1]] < num:
                    last_index = stack.pop()
                    end = max(last_index, end)
            stack.append(i)
        if start == sys.maxsize and end == -sys.maxsize:
            return 0
        return end-start+1
