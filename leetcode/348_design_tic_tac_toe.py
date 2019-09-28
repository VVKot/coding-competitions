class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.main_diagonal = [0, 0]
        self.off_diagonal = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        self.make_move(row, col, player)
        if self.has_won(row, col, player):
            return player
        return 0

    def make_move(self, row: int, col: int, player: int) -> None:
        index = player-1
        self.rows[row][index] += 1
        self.cols[col][index] += 1
        if row == col:
            self.main_diagonal[index] += 1
        if row+col+1 == self.n:
            self.off_diagonal[index] += 1

    def has_won(self, row: int, col: int, player: int) -> bool:
        index = player-1
        lines_count = [self.rows[row][index], self.cols[col][index]]
        if row == col:
            lines_count.append(self.main_diagonal[index])
        if row+col+1 == self.n:
            lines_count.append(self.off_diagonal[index])
        return any(count == self.n for count in lines_count)
