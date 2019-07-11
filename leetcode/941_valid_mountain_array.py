from typing import List


class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        if N < 3:
            return False
        max_height = max(A)
        max_index = A.index(max_height)
        if max_index == 0 or max_index == N-1:
            return False
        for i, height in enumerate(A):
            if i < max_index:
                if height >= A[i+1]:
                    return False
            elif i > max_index:
                if height >= A[i-1]:
                    return False
        return True
