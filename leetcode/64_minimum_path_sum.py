from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for y in range(1, rows):
            grid[y][0] += grid[y-1][0]
        for x in range(1, cols):
            grid[0][x] += grid[0][x-1]
        for y in range(1, rows):
            for x in range(1, cols):
                top = grid[y-1][x]
                left = grid[y][x-1]
                grid[y][x] += min(top, left)
        return grid[-1][-1]
