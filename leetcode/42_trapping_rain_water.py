from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r, res = 0, 0, 0
        while l <= r:
            at_l = height[l]
            at_r = height[r]
            if at_l <= at_r:
                max_l = max(max_l, at_l)
                if at_l < max_l:
                    res += max_l - at_l
                l += 1
            else:
                max_r = max(max_r, at_r)
                if at_r < max_r:
                    res += max_r - at_r
                r -= 1
        return res
