from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_bigger, seen_first = False, False
        for i in range(1, len(A)):
            curr, prev = A[i], A[i-1]
            if curr == prev:
                continue
            if not seen_first:
                seen_first = True
                is_bigger = curr > prev
            else:
                if (curr > prev) ^ is_bigger:
                    return False
        return True
