import collections
from typing import List, Tuple


class Solution:

    WATER, LAND = '0', '1'

    def numIslands(self, grid: List[List[str]]) -> int:
        if not any(grid):
            return 0
        self.grid = grid
        result = 0
        for y, row in enumerate(grid):
            for x, mark in enumerate(row):
                if mark == self.LAND:
                    self.bfs(y, x)
                    result += 1
        return result

    def bfs(self, y: int, x: int) -> None:
        self.grid[y][x] = self.WATER
        q = collections.deque([(y, x)])
        while q:
            curr_y, curr_x = q.popleft()
            for yy, xx in self.get_adj_nodes(curr_y, curr_x):
                self.grid[yy][xx] = self.WATER
                q.append((yy, xx))

    def get_adj_nodes(self, y: int, x: int) -> List[Tuple[int, int]]:
        r = len(self.grid)
        c = len(self.grid[0])
        adj = []
        for yy, xx in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
            if 0 <= yy < r and 0 <= xx < c:
                if self.grid[yy][xx] == self.LAND:
                    adj.append((yy, xx))
        return adj
