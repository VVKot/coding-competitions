from typing import List


class Solution:

    def fixedPoint(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < mid:
                left = mid + 1
            else:
                right = mid
        return left if A[left] == left else -1
