"""
T: O(R*C)
T: O(R*C)

The trick is to modify both rows and columns.

A vertical shift for each column is K // C, meaning the number of times
all columns are shifted. But we have to take big values of K into account.
Since the grid is transformed to the original one after R * C iterations,
a vertical shift is K // C % R. It is also increased by one for last K % C
columns.

A horizontal shift is just K % C, that is the number of columns moved.
"""


from typing import List


class Solution:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        vertical_shift, horizontal_shift = divmod(k, C)
        vertical_shift %= R
        cols = []
        for i, col in enumerate(zip(*grid)):
            rotate = vertical_shift + int(C-i <= horizontal_shift)
            col = col[-rotate:] + col[:-rotate]
            cols.append(col)
        cols = cols[-horizontal_shift:] + cols[:-horizontal_shift]
        return zip(*cols)
