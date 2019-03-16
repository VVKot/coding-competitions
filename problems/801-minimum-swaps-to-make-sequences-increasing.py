class Solution:
    def minSwap(self, A, B):
        N = len(A)
        prev = [0, 1]
        for i in range(1, N):
            curr = [float('inf'), float('inf')]
            if A[i] > B[i-1] and B[i] > A[i-1]:
                curr[0] = min(curr[0], prev[1])
                curr[1] = min(curr[1], prev[0]+1)
            if A[i] > A[i-1] and B[i] > B[i-1]:
                curr[0] = min(curr[0], prev[0])
                curr[1] = min(curr[1], prev[1]+1)
            prev = curr
        return min(prev)
