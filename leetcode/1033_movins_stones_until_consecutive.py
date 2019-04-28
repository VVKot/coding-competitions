class Solution:

    def numMovesStones(self, a, b, c):
        a, b, c = sorted([a, b, c])
        left = abs(b-a) - 1
        right = abs(c-b)-1
        max_ = left + right
        min_ = None
        if not left and not right:
            min_ = 0
        elif not left or not right or left == 1 or right == 1:
            min_ = 1
        else:
            min_ = 2
        return [min_, max_]
