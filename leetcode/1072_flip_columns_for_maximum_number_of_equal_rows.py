import collections
from typing import List, Counter, Tuple


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        result = 0
        if not any(matrix):
            return result
        pattern_count = collections.Counter()  # type: Counter[Tuple[int, ...]]
        for row in matrix:
            pattern = None
            if row[0] == 0:
                pattern = tuple(row)
            else:
                pattern = tuple(1 - i for i in row)
            pattern_count[pattern] += 1
            result = max(result, pattern_count[pattern])
        return result
