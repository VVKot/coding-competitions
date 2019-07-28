from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0
        y = len(grid)
        x = len(grid[0])
        res = 0
        for i in range(y):
            for j in range(x):
                if grid[i][j]:
                    curr = self.check_square(grid, i, j)
                    res = max(res, curr)
        return res
    
    def check_square(self, grid, i, j):
        r = len(grid)
        c = len(grid[0])
        max_ = min(r-i, c-j)
        res = 0
        for k in range(0, max_+1):
            a = b = c = d = True
            for yy in range(i, i+k):
                if not grid[yy][j]:
                    a = False
                    break
            for yy in range(i, i+k):
                if not grid[yy][j+k-1]:
                    b = False
                    break
            for xx in range(j, j+k):
                if not grid[i][xx]:
                    c = False
                    break
            for xx in range(j, j+k):
                if not grid[i+k-1][xx]:
                    d = False
                    break
            if a and b and c and d:
                res = k ** 2
            elif not a or not c:
                return res
        return res
