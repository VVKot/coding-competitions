import collections
from typing import List


class Solution:

    def largestUniqueNumber(self, A: List[int]) -> int:
        result = -1
        if not A:
            return result
        c = collections.Counter(A)
        for k, v in c.items():
            if v == 1:
                result = max(result, k)
        return result
