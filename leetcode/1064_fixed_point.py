from typing import List


class Solution:

    def fixedPoint(self, A: List[int]) -> int:
        for i, num in enumerate(A):
            if i == num:
                return i
        return -1
