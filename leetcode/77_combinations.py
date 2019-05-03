from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]  # type: List[List[int]]
        for j in range(k, 0, -1):
            combs = [
                [i] + c for c in combs for i in range(j, c[0] if c else n+1)]
        return combs
