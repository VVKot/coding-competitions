from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1] * (i+1) for i in range(numRows)]
        for r in range(0, numRows):
            pascal[r][0] = pascal[r][-1] = 1
            for c in range(1, r // 2 + 1):
                pascal[r][c] = pascal[r][-c - 1] = \
                    pascal[r-1][c-1] + pascal[r-1][c]
        return pascal
