class Solution:

    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde",
                 "fghij",
                 "klmno",
                 "pqrst",
                 "uvwxy",
                 "z"]
        result = ""
        coords = {}
        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                coords[ch] = (r, c)
        initial = (0, 0)
        for ch in target:
            to = coords[ch]
            result += self.get_path(initial, to)
            result += "!"
            initial = to
        return result

    def get_path(self, fr, to):
        fy, fx = fr
        ty, tx = to
        path = ""
        path += "L" * (fx-tx) if tx < fx else ""
        path += "U" * (fy-ty) if ty < fy else ""
        path += "R" * (tx-fx) if tx > fx else ""
        path += "D" * (ty-fy) if ty > fy else ""
        return path
