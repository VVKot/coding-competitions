from typing import List


class Solution:

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        for i in reversed(range(len(A))):
            K, A[i] = divmod(A[i] + K, 10)
        if K:
            A = [int(j) for j in str(K)] + A
        return A
