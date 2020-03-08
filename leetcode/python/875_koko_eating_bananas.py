import math
from typing import List


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo+hi) // 2
            curr_hours = sum(math.ceil(p/mid) for p in piles)
            if curr_hours > H:
                lo = mid+1
            else:
                hi = mid
        return lo
