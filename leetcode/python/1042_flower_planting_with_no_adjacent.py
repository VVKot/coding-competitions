from typing import List


class Solution:

    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        result = [0] * N
        G = [[] for _ in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        colors = {1, 2, 3, 4}
        for i in range(N):
            result[i] = (colors - {result[j] for j in G[i]}).pop()
        return result
