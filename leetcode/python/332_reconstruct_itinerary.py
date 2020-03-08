from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        routes = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            routes[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while routes[stack[-1]]:
                stack += routes[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]
