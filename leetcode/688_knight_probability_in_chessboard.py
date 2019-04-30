from copy import deepcopy


class Solution:

    def get_near(self, y, x):
        return [(y-1, x-2), (y-2, x-1), (y-1, x+2), (y-2, x+1),
                (y+1, x+2), (y+2, x+1), (y+1, x-2), (y+2, x-1)]

    def recalculate_probs(self, old, new):
        for y in range(self.N):
            for x in range(self.N):
                near = self.get_near(y, x)
                total = 0
                for r, c in near:
                    if 0 <= r < self.N and 0 <= c < self.N:
                        total += old[r][c]
                new[y][x] = total / 8.0

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        self.N = N
        old = [[1 for _ in range(N)] for _ in range(N)]
        for _ in range(K):
            new = deepcopy(old)
            self.recalculate_probs(old, new)
            old = new
        return old[r][c]
