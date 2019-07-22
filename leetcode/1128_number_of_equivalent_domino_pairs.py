import collections
from typing import Counter, List, Tuple


class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = collections.Counter()  # type: Counter[Tuple[int, int]]
        result = 0
        for i, j in dominoes:
            key = (i, j) if i <= j else (j, i)
            if pairs[key] > 0:
                result += pairs[key]
            pairs[key] += 1
        return result
