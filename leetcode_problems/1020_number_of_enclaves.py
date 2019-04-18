class Solution:
    def dfs(self, A, y, x):
        rows = len(A)
        cols = len(A[0])
        stack = [(y, x)]
        while stack:
            yy, xx = stack.pop()
            A[yy][xx] = 0
            for r, c in [(yy-1, xx), (yy+1, xx), (yy, xx-1), (yy, xx+1)]:
                if 0 <= r < rows and 0 <= c < cols and A[r][c]:
                    stack.append((r, c))

    def find_borders(self, A):
        rows = len(A)
        cols = len(A[0])
        borders = []
        for x in range(cols):
            borders.append((0, x))
            borders.append((rows-1, x))
        for y in range(rows):
            borders.append((y, 0))
            borders.append((y, cols-1))
        return borders

    def numEnclaves(self, A):
        if not any(A):
            return 0
        borders = self.find_borders(A)
        for y, x in borders:
            if A[y][x]:
                self.dfs(A, y, x)
        return sum(sum(row) for row in A)
