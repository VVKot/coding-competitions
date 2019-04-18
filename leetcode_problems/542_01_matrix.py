from collections import deque


class Solution:
    def multihead_bfs_update(self, matrix, heads):
        rows = len(matrix)
        cols = len(matrix[0])
        stack = deque([(y, x, 2) for y, x in heads])
        while stack:
            y, x, val = stack.popleft()
            near = self.get_near(y, x)
            for r, c in near:
                if 0 <= r < rows and 0 <= c < cols:
                    if (r, c) not in heads and matrix[r][c] == 1:
                        matrix[r][c] = val
                        stack.append((r, c, val+1))

    def get_bfs_heads(self, matrix):
        heads = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for y, row in enumerate(matrix):
            for x, num in enumerate(row):
                if not num or (y, x) in heads:
                    continue
                for r, c in self.get_near(y, x):
                    if 0 <= r < rows and 0 <= c < cols:
                        if not matrix[r][c]:
                            heads.add((y, x))
                            break
        return heads

    def get_near(self, y, x):
        return [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]

    def updateMatrix(self, matrix):
        heads = self.get_bfs_heads(matrix)
        self.multihead_bfs_update(matrix, heads)
        return matrix
