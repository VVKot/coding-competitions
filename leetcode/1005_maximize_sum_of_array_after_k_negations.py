from typing import List


class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while K and A[i] <= 0:
            A[i] = -A[i]
            K -= 1
            i += 1
        total = sum(A)
        if K and K & 1:
            total -= min(A) * 2
        return total
