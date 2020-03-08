import heapq
from typing import List


class Solution:

    def connectSticks(self, sticks: List[int]) -> int:
        connection_cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            new_stick = x+y
            connection_cost += new_stick
            heapq.heappush(sticks, new_stick)
        return connection_cost
