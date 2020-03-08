class Solution:

    def uniquePaths(self, cols: int, rows: int) -> int:
        curr = [1] + [0] * (cols-1)
        for _ in range(rows):
            for i in range(1, cols):
                curr[i] += curr[i-1]
        return curr[-1]
