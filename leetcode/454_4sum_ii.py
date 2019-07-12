import collections
from typing import List


class Solution:

    def fourSumCount(self,
                     A: List[int],
                     B: List[int],
                     C: List[int],
                     D: List[int]) -> int:
        ab_counter = collections.Counter(a+b for a in A for b in B)
        cd_counter = collections.Counter(c+d for c in C for d in D)
        zero_sum_count = 0
        for ab_sum in ab_counter:
            if -ab_sum in cd_counter:
                zero_sum_count += ab_counter[ab_sum] * cd_counter[-ab_sum]
        return zero_sum_count
