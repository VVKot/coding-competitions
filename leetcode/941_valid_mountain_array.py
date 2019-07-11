from typing import List


class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        last = len(A) - 1
        if last < 2:
            return False
        peak = 0
        while peak < last and A[peak] < A[peak+1]:
            peak += 1
        if peak == 0 or peak == last:
            return False
        downhill = peak
        while downhill < last and A[downhill] > A[downhill+1]:
            downhill += 1
        return downhill == last
