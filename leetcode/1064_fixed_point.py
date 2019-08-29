import bisect
from typing import List


class Solution:

    def fixedPoint(self, A: List[int]) -> int:
        i = bisect.bisect(A, 0) - 1
        while i < len(A):
            if i == A[i]:
                return i
            i += 1
        return -1
