class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.main_diagonal = 0
        self.off_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.make_move(row, col, player)
        if self.has_won(row, col, player):
            return player
        return 0

    def make_move(self, row: int, col: int, player: int) -> None:
        diff = 1 if player == 1 else -1
        self.rows[row] += diff
        self.cols[col] += diff
        if row == col:
            self.main_diagonal += diff
        if row+col+1 == self.n:
            self.off_diagonal += diff

    def has_won(self, row: int, col: int, player: int) -> bool:
        total = self.n if player == 1 else -self.n
        counts = [self.rows[row], self.cols[col]]
        if row == col:
            counts.append(self.main_diagonal)
        if row+col+1 == self.n:
            counts.append(self.off_diagonal)
        return any(c == total for c in counts)
