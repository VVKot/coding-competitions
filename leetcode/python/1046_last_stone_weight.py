from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            biggest = -heappop(stones)
            second_biggest = -heappop(stones)
            if biggest != second_biggest:
                heappush(stones, -(biggest - second_biggest))
        return -stones[0] if stones else 0
