from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        L, res = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                L += 1
                res += L
            else:
                L = 0
        return res
