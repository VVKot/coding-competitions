from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc, dec = True, True
        for i in range(1, len(A)):
            curr, prev = A[i], A[i-1]
            inc &= curr >= prev
            dec &= curr <= prev
        return inc or dec
