"""
T: O(logN)
S: O(1)

Binary search the correct number. Since we are rounding the result down, we
should only skip the current number if it is too high.
"""


class Solution:

    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        sqrt = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid**2 <= x:
                sqrt = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return sqrt
