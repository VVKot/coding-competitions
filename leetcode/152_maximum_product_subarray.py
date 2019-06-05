from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        pmax = pmin = res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                pmax, pmin = pmin, pmax
            pmax = max(num, pmax * num)
            pmin = min(num, pmin * num)
            res = max(res, pmax)
        return res
