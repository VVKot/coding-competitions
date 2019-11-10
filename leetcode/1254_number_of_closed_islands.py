"""
T: O(M*N)
S: O(M*N)

This problem builds upon 733. Flood Fill.
https://leetcode.com/problems/flood-fill/
We first fill all the cells near the border.
After that, every island is a closed island, count them.
"""


from typing import List, Tuple


class Solution:

    LAND, WATER = range(2)

    def closedIsland(self, grid: List[List[int]]) -> int:
        self.fill_border_islands(grid)
        closed_islands = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == self.LAND:
                    self.fill(grid, y, x)
                    closed_islands += 1
        return closed_islands

    def fill_border_islands(self, grid: List[List[int]]) -> None:
        for y, x in self.get_borders(grid):
            if grid[y][x] == self.LAND:
                self.fill(grid, y, x)

    def get_borders(self, grid: List[List[int]]) -> List[Tuple[int, int]]:
        borders = []
        rows = len(grid)
        cols = len(grid[0])
        for y in range(rows):
            borders.append((y, 0))
            borders.append((y, cols-1))
        for x in range(1, cols-1):
            borders.append((0, x))
            borders.append((rows-1, x))
        return borders

    def fill(self, grid: List[List[int]], y: int, x: int) -> None:
        stack = [(y, x)]
        while stack:
            curr_y, curr_x = stack.pop()
            grid[curr_y][curr_x] = self.WATER
            neighbors = self.get_neighbors(grid, curr_y, curr_x)
            for neig_y, neig_x in neighbors:
                if grid[neig_y][neig_x] == self.LAND:
                    stack.append((neig_y, neig_x))

    def get_neighbors(self,
                      grid: List[List[int]],
                      y: int,
                      x: int) -> List[Tuple[int, int]]:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = []
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            curr_y, curr_x = y+dy, x+dx
            if 0 <= curr_y < rows and 0 <= curr_x < cols:
                neighbors.append((curr_y, curr_x))
        return neighbors
