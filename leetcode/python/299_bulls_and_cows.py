import collections
from typing import Counter


class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        seen = collections.Counter()  # type: Counter[str]
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                if seen[s] < 0:
                    cows += 1
                if seen[g] > 0:
                    cows += 1
                seen[s] += 1
                seen[g] -= 1
        return "{0}A{1}B".format(bulls, cows)
