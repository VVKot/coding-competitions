from typing import List


class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        end_index = len(A) - 1
        peak = 0
        while peak < end_index and A[peak] < A[peak+1]:
            peak += 1
        if peak == 0 or peak == end_index:
            return False
        downhill = peak
        while downhill < end_index and A[downhill] > A[downhill+1]:
            downhill += 1
        return downhill == end_index
