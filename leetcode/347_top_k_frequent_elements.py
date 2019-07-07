import collections
import heapq
from typing import List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        result = []  # type: List[Tuple[int, int]]
        for val, count in counts.items():
            item = (count, val)
            if len(result) == k:
                heapq.heappushpop(result, item)
            else:
                heapq.heappush(result, item)
        return [val for _, val in result]
