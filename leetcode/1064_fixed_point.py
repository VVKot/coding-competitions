from typing import List


class Solution:

    def fixedPoint(self, A: List[int]) -> int:
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if A[mid] < mid:
                lo = mid + 1
            else:
                hi = mid
        return lo if A[lo] == lo else -1
