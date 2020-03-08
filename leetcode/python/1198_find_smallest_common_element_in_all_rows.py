import collections
from typing import Counter, List


class Solution:

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        element_count = collections.Counter()  # type: Counter[int]
        N = len(mat)
        for row in mat:
            for num in row:
                element_count[num] += 1
                if element_count[num] == N:
                    return num
        return -1
