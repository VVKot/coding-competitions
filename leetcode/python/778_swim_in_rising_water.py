import heapq
from typing import List


class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return -1
        N = len(grid)
        stack = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        result = 0
        while stack:
            dist, y, x = heapq.heappop(stack)
            result = max(result, dist)
            if y == x == N - 1:
                return result
            for r, c in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                if (r, c) in visited:
                    continue
                if 0 <= r < N and 0 <= c < N:
                    heapq.heappush(stack, (grid[r][c], r, c))
                    visited.add((r, c))
        return -1
