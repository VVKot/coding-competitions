import collections
from typing import List


class Solution:

    def fourSumCount(self,
                     A: List[int],
                     B: List[int],
                     C: List[int],
                     D: List[int]) -> int:
        ab_counter = collections.Counter(a+b for a in A for b in B)
        return sum(ab_counter[-c-d] for c in C for d in D)
