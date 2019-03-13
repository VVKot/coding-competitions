class Solution:
    def get_area(self, grid, x, y):
        grid_y = len(grid)
        grid_x = len(grid[0])
        result = 0
        if x < 0 or x == grid_x or y < 0 or y == grid_y or grid[y][x] == 0:
            return result
        grid[y][x] = 0
        result += self.get_area(grid, x+1, y)
        result += self.get_area(grid, x-1, y)
        result += self.get_area(grid, x, y+1)
        result += self.get_area(grid, x, y-1)
        result += 1
        return result

    def maxAreaOfIsland(self, grid):
        max_island = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    curr_island = self.get_area(grid, x, y)
                    max_island = max(max_island, curr_island)
        return max_island
