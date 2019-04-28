class Solution:

    def solveNQueens(self, n):
        def DFS(queens, diag_left, diag_right):
            col = len(queens)
            if col == n:
                result.append(queens)
                return None
            for row in range(n):
                if row in queens:
                    continue
                if col-row in diag_left:
                    continue
                if col+row in diag_right:
                    continue
                DFS(queens+[row], diag_left +
                    [col-row], diag_right+[col+row])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
