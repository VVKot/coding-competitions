class Solution(object):

    def is_land(self, grid, y, x):
        rows = len(grid)
        cols = len(grid[0])
        return 0 <= y < rows and 0 <= x < cols and grid[y][x]

    def get_nearest(self, y, x):
        return [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    def get_perimeter(self, grid, start):
        stack = [start]
        visited = set(stack)
        result = 0
        while stack:
            y, x = stack.pop()
            nearest = self.get_nearest(y, x)
            near = 0
            for r, c in nearest:
                if not self.is_land(grid, r, c):
                    continue
                near += 1
                if (r, c) in visited:
                        continue
                visited.add((r,c))
                stack.append((r,c))
            result += 4 - near
        return result

    def islandPerimeter(self, grid):
        result = 0
        if not any(grid):
            return result
        start = None
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num:
                    start = (i, j)
                    break
            if start:
                break
        result = self.get_perimeter(grid, start)
        return result
