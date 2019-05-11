from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        result = 0
        N = len(A)
        for i in range(2, N):
            big = A[i-2]
            small = A[i-1]
            for j in range(i, N):
                if A[j] + small > big:
                    result = max(result, A[j] + small + big)
                    break
        return result
