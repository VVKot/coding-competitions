from typing import List


class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        changed = False
        for i in range(1, N):
            curr = nums[i]
            prev = nums[i - 1]
            if curr < prev:
                if changed:
                    return False
                changed = True
                if i-2 < 0 or nums[i-2] <= curr:
                    nums[i-1] = curr
                else:
                    nums[i] = prev
        return True
