import collections
from typing import List, Tuple


class Solution:

    WATER, LAND = range(2)

    def maxDistance(self, grid: List[List[int]]) -> int:
        land, water = self.split_map(grid)
        if not water or not land:
            return -1
        max_dist = self.get_max_dist(grid, land)
        return max_dist

    def split_map(self, grid: List[List[int]]) -> \
            Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        land = []
        water = []
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == self.LAND:
                    land.append((y, x))
                else:
                    water.append((y, x))
        return land, water

    def get_max_dist(self,
                     grid: List[List[int]],
                     land: List[Tuple[int, int]]) -> int:
        visited = set(land)
        to_visit = collections.deque([(l, 0) for l in land])
        max_dist = 0
        while to_visit:
            node, path = to_visit.pop()
            y, x = node
            max_dist = max(max_dist, path)
            for yy, xx in self.get_near(grid, y, x):
                if (yy, xx) not in visited and grid[yy][xx] == self.WATER:
                    visited.add((yy, xx))
                    to_visit.appendleft(((yy, xx), path+1))
        return max_dist

    def get_near(self,
                 grid: List[List[int]],
                 y: int,
                 x: int) -> List[Tuple[int, int]]:
        near = []
        rows = len(grid)
        cols = len(grid[0])
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            curr_y, curr_x = y+dy, x+dx
            if 0 <= curr_y < rows and 0 <= curr_x < cols:
                near.append((curr_y, curr_x))
        return near
