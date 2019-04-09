class Solution:
    def numEnclaves(self, A):
        if not any(A):
            return 0
        rows = len(A)
        cols = len(A[0])
        borders = []
        for x in range(cols):
            borders.append((0, x))
            borders.append((rows-1, x))
        for y in range(rows):
            borders.append((y, 0))
            borders.append((y, cols-1))
        for y, x in borders:
            if A[y][x] and (y == 0 or x == 0 or y == rows-1 or x == cols-1):
                stack = [(y, x)]
                while stack:
                    yy, xx = stack.pop()
                    A[yy][xx] = 0
                    for r, c in [(yy-1, xx), (yy+1, xx), (yy, xx-1), (yy, xx+1)]:
                        if 0 <= r < rows and 0 <= c < cols and A[r][c]:
                            stack.append((r, c))
        return sum(sum(row) for row in A)
