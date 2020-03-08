class Solution:

    def superEggDrop(self, K, N):
        cache = [[0] * (K+1) for _ in range(N+1)]
        for m in range(1, N+1):
            for k in range(1, K+1):
                cache[m][k] = 1 + cache[m-1][k-1] + cache[m-1][k]
            if cache[m][-1] >= N:
                return m
