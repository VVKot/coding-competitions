class Solution:

    def get_len(self, A, L, M):
        N = len(A)
        prefix = [0] * (N+1)
        prefix[0] = 0
        for i in range(N):
            prefix[i + 1] = prefix[i] + A[i]
        ans = 0
        for i in range(L-1, N-M):
            for j in range(i+1, N-M+1):
                ans = max(ans, prefix[i + 1] -
                          prefix[i - L + 1] + prefix[j + M] - prefix[j])
        L, M = M, L
        for i in range(L-1, N-M):
            for j in range(i+1, N-M+1):
                ans = max(ans, prefix[i + 1] -
                          prefix[i - L + 1] + prefix[j + M] - prefix[j])
        return ans

    def maxSumTwoNoOverlap(self, A, L, M):
        return self.get_len(A, L, M)
