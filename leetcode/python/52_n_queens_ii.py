class Solution:
    def backtrack(self, n, row, cols, d1, d2):
        if n == row:
            self.result += 1
            return
        for col in range(n):
            id1 = col - row + n
            id2 = col + row
            if cols[col] or d1[id1] or d2[id2]:
                continue
            cols[col], d1[id1], d2[id2] = True, True, True
            self.backtrack(n, row+1, cols, d1, d2)
            cols[col], d1[id1], d2[id2] = False, False, False

    def totalNQueens(self, n):
        self.result = 0
        cols = [False] * n
        d1 = [False] * 2*n
        d2 = [False] * 2*n
        self.backtrack(n, 0, cols, d1, d2)
        return self.result
