class Solution:
    def get_captures(self, board, r, c):
        result = 0
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            y, x = r + i, c + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[y][x] == 'p':
                    result += 1
                if board[y][x] != '.':
                    break
                y, x = y + i, x + j
        return result

    def find_rook(self, board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'R':
                    return (y, x)
        return (None, None)

    def numRookCaptures(self, board):
        r, c = self.find_rook(board)
        result = self.get_captures(board, r, c)
        return result
