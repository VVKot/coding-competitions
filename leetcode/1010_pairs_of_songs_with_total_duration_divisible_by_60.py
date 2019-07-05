import collections
from typing import List


class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pair_count = 0
        comp = collections.defaultdict(int)
        for t in time:
            pair_count += comp[-t % 60]
            comp[t % 60] += 1
        return pair_count
