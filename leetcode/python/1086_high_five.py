import collections
import heapq
from typing import Dict, List


class Solution:

    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        high_fives = \
            collections.defaultdict(list)  # type: Dict[int, List[int]]
        for student, score in items:
            heapq.heappush(high_fives[student], score)
            if len(high_fives[student]) > 5:
                heapq.heappop(high_fives[student])
        return [[student, sum(high_fives[student])//5]
                for student in sorted(high_fives)]
