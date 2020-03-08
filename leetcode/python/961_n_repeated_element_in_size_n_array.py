from typing import List


class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)
        for i in range(2, N):
            if A[i] == A[i-1] or A[i] == A[i-2]:
                return A[i]
        return A[0]
