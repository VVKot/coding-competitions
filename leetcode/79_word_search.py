class Solution:

    def dfs(self, board, y, x, word):
        if not word:
            return True
        rows = len(board)
        cols = len(board[0])
        if not (0 <= y < rows and 0 <= x < cols):
            return False
        if board[y][x] != word[0]:
            return False
        temp = board[y][x]
        board[y][x] = '#'
        result = False
        result = self.dfs(board, y+1, x, word[1:]) or self.dfs(board, y-1, x, word[1:]) \
            or self.dfs(board, y, x+1, word[1:]) or self.dfs(board, y, x-1, word[1:])
        board[y][x] = temp
        return result

    def exist(self, board, word):
        if not any(board) or not word:
            return False
        rows = len(board)
        cols = len(board[0])
        for y in range(rows):
            for x in range(cols):
                found = self.dfs(board, y, x, word)
                if found:
                    return True
        return False
