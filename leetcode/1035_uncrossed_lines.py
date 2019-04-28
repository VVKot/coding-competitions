class Solution:

    def maxUncrossedLines(self, A, B):
        dp = {}
        a, b = len(A)-1, len(B)-1

        def helper(i, j):
            result = 0
            if i > a or j > b:
                return result
            if (i, j) in dp:
                return dp[(i, j)]
            if A[i] == B[j]:
                result = 1 + helper(i+1, j+1)
            else:
                result = max(helper(i, j+1), helper(i+1, j))
            dp[(i, j)]=result
            return result
        return helper(0, 0)
