from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        N = len(A)
        for i in range(1, N - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                return i
        return -1
