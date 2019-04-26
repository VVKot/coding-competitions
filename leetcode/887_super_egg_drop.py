class Solution:

    def superEggDrop(self, K, N):
        cache = [[0] * (N+1) for _ in range(K+1)]
        cache[1] = list(range(N+1))
        for i in range(2, K+1):
            for j in range(1, N+1):
                cache[i][j] = float('inf')
                for m in range(1, j+1):
                    prev = max(cache[i-1][m-1], cache[i][j-m]) + 1
                    cache[i][j] = min(prev, cache[i][j])
        return cache[-1][-1]
