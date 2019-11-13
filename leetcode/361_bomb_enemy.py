"""
T: O(R*C)
S: O(C)

For the first entry in each row and column count the number of hits.
Do the same if the previous cell contains a wall.
After that, on each step update the result.
"""


from typing import List


class Solution:

    ENEMY, WALL, EMPTY = "E", "W", "0"

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not any(grid):
            return 0
        R, C = len(grid), len(grid[0])
        result, row_hits, col_hits = 0, 0, [0] * C
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if not x or grid[y][x-1] == self.WALL:
                    row_hits = 0
                    for k in range(x, C):
                        if grid[y][k] == self.WALL:
                            break
                        if grid[y][k] == self.ENEMY:
                            row_hits += 1
                if not y or grid[y-1][x] == self.WALL:
                    col_hits[x] = 0
                    for k in range(y, R):
                        if grid[k][x] == self.WALL:
                            break
                        if grid[k][x] == self.ENEMY:
                            col_hits[x] += 1
                if val == self.EMPTY:
                    result = max(result, row_hits + col_hits[x])
        return result
