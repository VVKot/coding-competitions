class Solution:

    def minimumTotal(self, triangle):
        N = len(triangle)
        for i in range(N-1, 0, -1):
            M = len(triangle[i])
            for j in range(M-1):
                min_ = min(triangle[i][j], triangle[i][j+1])
                triangle[i-1][j] += min_
        return triangle[0][0]
