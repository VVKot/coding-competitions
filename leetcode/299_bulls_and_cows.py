import collections
from typing import Counter


class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_count = collections.Counter()  # type: Counter[str]
        guess_count = collections.Counter()  # type: Counter[str]
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1
        common_digits_count = secret_count & guess_count
        cows = sum(common_digits_count.values())
        return "{0}A{1}B".format(bulls, cows)
