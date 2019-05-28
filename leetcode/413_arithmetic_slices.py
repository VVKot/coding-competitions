from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        result, diff, L = 0, A[1] - A[0], 2
        for i in range(2, len(A)):
            new_diff = A[i] - A[i - 1]
            if new_diff == diff:
                L += 1
            else:
                if L > 2:
                    result += (L - 2) * (L - 1) // 2
                L = 2
                diff = new_diff
        if L > 2:
            result += (L - 2) * (L - 1) // 2
        return result
