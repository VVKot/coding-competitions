from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times, N, K):
        stack = [(0, K)]
        search_times = {}
        adj_nodes = defaultdict(list)
        for src, dst, time_ in times:
            adj_nodes[src].append((dst, time_))
        while stack:
            time_, curr = heappop(stack)
            if not curr in search_times:
                search_times[curr] = time_
                for dst, dst_time in adj_nodes[curr]:
                    heappush(stack, (time_+dst_time, dst))
        return max(search_times.values()) if len(search_times) == N else -1
