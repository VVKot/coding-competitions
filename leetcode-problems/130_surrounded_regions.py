class Solution:
    def solve(self, board):
        if not board or not len(board):
            return
        m = len(board)
        n = len(board[0])
        save = list({yx for k in range(m+n)
                     for yx in ((0, k), (m-1, k), (k, 0), (k, n-1))})
        while save:
            y, x = save.pop()
            if 0 <= y < m and 0 <= x < n and board[y][x] == 'O':
                board[y][x] = 'C'
                save += (y, x-1), (y, x+1), (y-1, x), (y+1, x)

        for row in board:
            for i, c in enumerate(row):
                row[i] = 'O' if c == 'C' else 'X'
