import random


def rand7():
    return random.randint(1, 7)


class Solution:

    def rand10(self) -> int:
        """
        N^b * (randN() - 1) + N^(b - 1) * (randN() - 1) + N^(b - 2) * (randN() - 1) + ... + N^0 * (randN() - 1)
        generates randX() - 1, where X = N^(b + 1).
        """
        num = 42
        while num >= 40:
            row = rand7() - 1
            col = rand7() - 1
            num = 7 * row + col
        return num % 10 + 1
