import heapq

class Solution:
    def swimInWater(self, grid):
        N = len(grid)
        queue = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        result = 0
        while True:
            T, x, y = heapq.heappop(queue)
            result = max(result, T)
            if x == y == N - 1:
                return result
            for xx, yy in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= xx < N and 0 <= yy < N and (xx, yy) not in visited:
                    visited.add((xx, yy))
                    heapq.heappush(queue, (grid[xx][yy], xx, yy))
