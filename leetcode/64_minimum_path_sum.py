class Solution:

    def minPathSum(self, grid):
        if not any(grid):
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for y in range(1, m):
            for x in range(1, n):
                top = grid[y-1][x]
                left = grid[y][x-1]
                grid[y][x] += min(top, left)
        return grid[-1][-1]
