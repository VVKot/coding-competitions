from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i, N = 0, len(nums)
        while i < N:
            if nums[i] == val:
                nums[i] = nums[N-1]
                N -= 1
            else:
                i += 1
        return N
