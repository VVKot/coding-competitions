"""
T: O(N + M + L)
S: O(N + M)

Calculate the oddness of each row and column.
After that, sum all of the odd columns if the row is even,
sum even columns otherwise.
"""


from typing import List


class Solution:

    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for y, x in indices:
            rows[y] ^= 1
            cols[x] ^= 1
        col_sum = sum(cols)
        return sum(col_sum if not r else m-col_sum for r in rows)
