"""
T: O(M*N)
S: O(M*N)

Count the number of killed in enemies for each row and column.
The maximum of those counts is the final result.
"""


from typing import List


class Solution:

    ENEMY, WALL, EMPTY = "E", "W", "0"

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not any(grid):
            return 0
        R, C = len(grid), len(grid[0])
        # self.get_default_killed_count(grid)
        killed_count = [[0 for _ in range(C)] for _ in range(R)]
        for y in range(R):
            curr_killed = 0
            prev = 0
            for x in range(C):
                if x == C-1 or grid[y][x] == self.WALL:
                    last = x if x == C-1 else x-1
                    for i in range(prev, last+1):
                        if grid[y][i] == self.EMPTY:
                            killed_count[y][i] += curr_killed
                    curr_killed = 0
                    prev = x+1
                elif grid[y][x] == self.ENEMY:
                    curr_killed += 1

        for x in range(C):
            curr_killed = 0
            prev = 0
            for y in range(R):
                if grid[y][x] == self.ENEMY:
                    curr_killed += 1
                if y == R-1 or grid[y][x] == self.WALL:
                    last = y if y == R-1 else x-1
                    for i in range(prev, last+1):
                        if grid[i][x] == self.EMPTY:
                            killed_count[i][x] += curr_killed
                    curr_killed = 0
                    prev = y+1
        return max(val for row in killed_count for val in row)
