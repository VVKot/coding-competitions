import heapq
from typing import List


class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        while len(blocks) > 1:
            _ = heapq.heappop(blocks)
            last = heapq.heappop(blocks)
            heapq.heappush(blocks, last+split)
        return heapq.heappop(blocks)
