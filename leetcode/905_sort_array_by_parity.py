from typing import List


class Solution:

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j, N = 0, 0, len(A)
        while i < N:
            if not A[i] & 1:
                A[i], A[j] = A[j], A[i]
                j += 1
            i += 1
        return A
