class Solution:

    def is_legal(self, board, y, x):
        cols = len(board)
        rows = len(board[0])
        return 0 <= y < cols and 0 <= x < rows

    def findWords(self, board, words):
        trie = {}
        for word in words:
            t = trie
            for letter in word:
                if letter not in t:
                    t[letter] = {}
                t = t[letter]
            t['*'] = '*'
        result = []
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                self.find(board, i, j, "", trie, result)
        return list(set(result))

    def find(self, board, i, j, path, trie, res):
        if '*' in trie:
            res.append(path)
        if not self.is_legal(board, i, j):
            return
        if board[i][j] not in trie:
            return
        ch = board[i][j]
        board[i][j] = '&'
        self.find(board, i-1, j, path+ch, trie[ch], res)
        self.find(board, i+1, j, path+ch, trie[ch], res)
        self.find(board, i, j-1, path+ch, trie[ch], res)
        self.find(board, i, j+1, path+ch, trie[ch], res)
        board[i][j] = ch
