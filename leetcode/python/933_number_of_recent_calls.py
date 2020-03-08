"""
T: O(N)
S: O(1)

Remember previous calls and pop the ones that have happened too long ago. The
space complexity can be considered constant since the target period is
constant.
"""

import collections


class RecentCounter:

    CUT_OFF_TIME = 3000

    def __init__(self):
        self.pings = collections.deque()

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings[-1] - self.pings[0] > self.CUT_OFF_TIME:
            self.pings.popleft()
        return len(self.pings)
