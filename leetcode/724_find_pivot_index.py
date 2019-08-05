from typing import List


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + num)
        N = len(nums)
        for i, num in enumerate(nums):
            before = prefix[i]
            after = prefix[N] - prefix[i+1]
            if before == after:
                return i
        return -1
