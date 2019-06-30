from typing import List, Tuple


class Solution:

    EMPTY, FRESH, ROTTEN = range(3)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0
        result = 0
        fresh_count = 0
        rotten = []
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == self.FRESH:
                    fresh_count += 1
                elif val == self.ROTTEN:
                    rotten.append((y, x))
        if not fresh_count:
            return result
        time = 0
        while rotten:
            if not fresh_count:
                break
            time += 1
            new_rotten = []  # type: List[Tuple[int, int]]
            for y, x in rotten:
                fresh_near = self.get_fresh_near(grid, y, x)
                for yy, xx in fresh_near:
                    fresh_count -= 1
                    grid[yy][xx] = self.ROTTEN
                new_rotten.extend(fresh_near)
            rotten = new_rotten
        return time if not fresh_count else -1

    def get_fresh_near(self, grid, y, x):
        fresh = []
        rows = len(grid)
        cols = len(grid[0])
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            near_y, near_x = y + dy, x + dx
            if 0 <= near_y < rows and 0 <= near_x < cols:
                if grid[near_y][near_x] == self.FRESH:
                    fresh.append((near_y, near_x))
        return fresh
