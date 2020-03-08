from heapq import heappush, heappop


class Solution:
    def getSkyline(self, buildings):
        res = [[0, 0]]
        deq = [(0, float("inf"))]
        events = sorted([(l, -h, r) for l, r, h in buildings] +
                        list({(r, 0, None) for _, r, _ in buildings}))
        for l, minusH, r in events:
            while l >= deq[0][1]:
                heappop(deq)
            if minusH:
                heappush(deq, (minusH, r))
            if res[-1][1] + deq[0][0]:
                res.append([l, -deq[0][0]])
        return res[1:]
