from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = defaultdict(dict)
        for s, d, price in flights:
            prices[s][d] = price
        heap = [(0, src, k + 1)]
        while heap:
            price, curr, stops = heapq.heappop(heap)
            if curr == dst:
                return price
            if stops > 0:
                for adj in prices[curr]:
                    heapq.heappush(heap, (price + prices[curr][adj], adj, stops - 1))
        return -1