from typing import List


class Solution:

    WATER, LAND = range(2)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        if not any(grid):
            return perimeter
        rows = len(grid)
        cols = len(grid[0])

        def get_cell_perimeter(y, x):
            perimeter = 0
            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                yy, xx = dy+y, dx+x
                if 0 <= yy < rows and 0 <= xx < cols:
                    if grid[yy][xx] == self.WATER:
                        perimeter += 1
                else:
                    perimeter += 1
            return perimeter

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == self.LAND:
                    perimeter += get_cell_perimeter(y, x)
        return perimeter
