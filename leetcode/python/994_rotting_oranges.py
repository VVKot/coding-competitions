from typing import List, Tuple


class Solution:

    EMPTY, FRESH, ROTTEN = range(3)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0
        self.calculate_variables(grid)
        return self.get_time_to_rott_all()

    def calculate_variables(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.fresh_count = 0
        self.rotten = []  # type: List[Tuple[int, int]]
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == self.FRESH:
                    self.fresh_count += 1
                elif val == self.ROTTEN:
                    self.rotten.append((y, x))

    def get_time_to_rott_all(self):
        time = 0
        while self.rotten:
            if not self.fresh_count:
                return time
            time += 1
            self.rott()
        return time if not self.fresh_count else -1

    def rott(self):
        new_rotten = []
        for y, x in self.rotten:
            fresh_near = self.get_fresh_near(y, x)
            for yy, xx in fresh_near:
                self.fresh_count -= 1
                self.grid[yy][xx] = self.ROTTEN
            new_rotten.extend(fresh_near)
        self.rotten = new_rotten

    def get_fresh_near(self, y, x):
        fresh = []
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            near_y, near_x = y + dy, x + dx
            if 0 <= near_y < self.rows and 0 <= near_x < self.cols:
                if self.grid[near_y][near_x] == self.FRESH:
                    fresh.append((near_y, near_x))
        return fresh
