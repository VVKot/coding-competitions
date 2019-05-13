from collections import deque


class RecentCounter:

    def __init__(self):
        self.cache = deque()

    def ping(self, t: int) -> int:
        self.cache.append(t)
        while self.cache[0] < t - 3000:
            self.cache.popleft()
        return len(self.cache)
