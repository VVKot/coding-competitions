class Solution:
    def maxAreaOfIsland(self, grid):
        grid_y = len(grid)
        grid_x = len(grid[0])
        result = 0

        for y in range(grid_y):
            for x in range(grid_x):
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    adj_nodes = [(y, x)]

                    for r, c in adj_nodes:
                        for node_y, node_x in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                            if 0 <= node_y < grid_y and 0 <= node_x < grid_x and grid[node_y][node_x] == 1:
                                grid[node_y][node_x] = 0
                                adj_nodes.append((node_y, node_x))

                    result = max(result, len(adj_nodes))

        return result
