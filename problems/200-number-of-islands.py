class Solution:
    def get_adj_nodes(self, grid, r, c, y, x):
        adj = []
        for yy, xx in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
            if 0 <= yy < r and 0 <= xx < c and grid[yy][xx] == '1':
                adj.append((yy, xx))
        return adj

    def dfs(self, grid, r, c, y, x):
        stack = [(y, x)]
        while stack:
            curr_y, curr_x = stack.pop()
            grid[curr_y][curr_x] = "*"
            adj_nodes = self.get_adj_nodes(grid, r, c, curr_y, curr_x)
            stack.extend(adj_nodes)

    def numIslands(self, grid):
        if not any(grid):
            return 0
        rows = len(grid)
        columns = len(grid[0])
        result = 0
        for y in range(rows):
            for x in range(columns):
                if grid[y][x] == '1':
                    self.dfs(grid, rows, columns, y, x)
                    result += 1
        return result
