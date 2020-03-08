class Solution:

    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x+y == 1:
            return 3
        if x == y == 2:
            return 4
        step = max((y+1)//2, (x+1)//2, (x+y+2)//3)
        step += (step ^ x ^ y) & 1
        return step
