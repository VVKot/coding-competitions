import collections
import bisect


class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.store[key], (timestamp, chr(127)))
        return self.store[key][i-1][1] if i else ""
