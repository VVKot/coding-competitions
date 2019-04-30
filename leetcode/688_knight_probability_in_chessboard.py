from typing import Dict, Tuple


class Solution:

    def get_near(self, y, x):
        return [(y-1, x-2), (y-2, x-1), (y-1, x+2), (y-2, x+1),
                (y+1, x+2), (y+2, x+1), (y+1, x-2), (y+2, x-1)]

    def is_legal(self, r, c):
        return 0 <= r < self.N and 0 <= c < self.N

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        self.N = N
        dp = {}  # type: Dict[Tuple[int, int, int], float]

        def dfs(y, x, mult, step):
            if self.is_legal(y, x):
                if step < K:
                    if (y, x, step) in dp:
                        return dp[(y, x, step)]
                    total = 0
                    for yy, xx in self.get_near(y, x):
                        curr = 0
                        if (yy, xx, step) in dp:
                            curr = dp[(yy, xx, step)]
                        else:
                            curr = dfs(yy, xx, mult/8, step+1)
                        dp[(yy, xx, step)] = curr
                        total += curr
                    return total
                else:
                    return mult
            else:
                return 0
        return dfs(r, c, 1, 0)
